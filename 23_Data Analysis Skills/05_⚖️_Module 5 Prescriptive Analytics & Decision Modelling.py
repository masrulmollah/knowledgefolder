import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# NO st.set_page_config() — Homepage.py owns that call.

def _sec(title, icon=""):
    st.markdown(f"### {icon} {title}")
    st.markdown("---")

def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans: st.success("✅ Correct!")
        else: st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def show():
    st.title("⚖️ Module 5: Prescriptive Analytics & Decision Modelling")
    st.caption("Move from insight to recommended action")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Decision EV", "📊 Portfolio Optimiser", "🧪 Worked Example", "❓ Quiz"
    ])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("The Analytics Ladder", "🪜")
        st.dataframe(pd.DataFrame({
            "Level":          ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
            "Question":       ["What happened?", "Why?", "What will happen?", "What should we DO?"],
            "Finance Example":["Revenue fell 8% in Q3", "Mid-Market churn drove miss",
                                "Churn will reach 15% by Q4", "Offer 15% retention discount now"],
            "Value":          ["Low", "Medium", "High", "Highest"],
        }), use_container_width=True, hide_index=True)

        _sec("Decision Frameworks", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Expected Value Formula**
```
EV = Σ (Probability × Outcome)

Example: Should we bid on this contract?
  40% chance win  → profit +$5M  → EV = +$2.0M
  60% chance lose → cost  -$0.5M → EV = -$0.3M
  Net EV = +$1.7M  →  BID!
```
**Decision Rule:** Choose the option with the highest EV,
adjusted for your organisation's risk tolerance.
            """)
        with c2:
            st.markdown("""
**Markowitz Portfolio Optimisation**
```
Portfolio Return   = Σ wᵢ × rᵢ
Portfolio Variance = Σ Σ wᵢ wⱼ σᵢⱼ
Sharpe Ratio       = (Rp − Rf) / σp

Constraints:
  Σ wᵢ = 1   (fully invested)
  wᵢ ≥ 0     (long only, basic version)
```
**Efficient Frontier** = set of portfolios that
maximise return for each level of risk.
Any portfolio inside the frontier is suboptimal.
            """)

    # ── DECISION EV ───────────────────────────────────────────────────────────
    with tab2:
        _sec("Expected Value Decision Calculator", "🧮")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Option A: Invest in the Project**")
            ps = st.slider("Probability of success", 0.0, 1.0, 0.55, 0.05)
            vs = st.number_input("Value if success ($M)", value=25.0, step=1.0)
            vf = st.number_input("Value if failure ($M)", value=-8.0, step=1.0)
            ic = st.number_input("Upfront investment cost ($M)", value=5.0, step=0.5)
        with c2:
            st.markdown("**Option B: Do Not Invest**")
            sq = st.number_input("Status quo value ($M)", value=3.0, step=0.5)

        ev_i = ps * vs + (1 - ps) * vf - ic
        ev_n = sq
        rec  = "✅ Invest" if ev_i > ev_n else "⚠️ Do Not Invest"

        c1, c2, c3 = st.columns(3)
        c1.metric("EV — Invest",      f"${ev_i:+.2f}M")
        c2.metric("EV — Do Nothing",  f"${ev_n:+.2f}M")
        c3.metric("Recommendation",   rec)

        if ev_i > ev_n:
            st.success(f"Investing creates **${ev_i - ev_n:.2f}M** more value than doing nothing.")
        else:
            st.warning(f"Doing nothing is worth **${ev_n - ev_i:.2f}M** more than investing at these probabilities.")

        st.markdown("**Sensitivity — Tornado Chart**")
        base = ev_i; sens = []
        for factor, lo, hi in [
            ("P(Success)",       max(0, ps-0.15), min(1, ps+0.15)),
            ("Value if Success", vs*0.7,          vs*1.3),
            ("Value if Failure", vf*1.3,          vf*0.7),
            ("Investment Cost",  ic*1.3,          ic*0.7),
        ]:
            if   factor == "P(Success)":       el=lo*vs+(1-lo)*vf-ic; eh=hi*vs+(1-hi)*vf-ic
            elif factor == "Value if Success": el=ps*lo+(1-ps)*vf-ic; eh=ps*hi+(1-ps)*vf-ic
            elif factor == "Value if Failure": el=ps*vs+(1-ps)*lo-ic; eh=ps*vs+(1-ps)*hi-ic
            else:                              el=ps*vs+(1-ps)*vf-lo; eh=ps*vs+(1-ps)*vf-hi
            sens.append({"Factor": factor, "Low": round(el,2), "High": round(eh,2),
                          "Range": abs(eh-el)})
        sdf = pd.DataFrame(sens).sort_values("Range", ascending=True)
        fig = go.Figure()
        fig.add_trace(go.Bar(y=sdf["Factor"], x=sdf["Low"]-base,  orientation="h",
                             name="Low scenario",  marker_color="#E24B4A"))
        fig.add_trace(go.Bar(y=sdf["Factor"], x=sdf["High"]-base, orientation="h",
                             name="High scenario", marker_color="#1D9E75"))
        fig.add_vline(x=0, line_color="black")
        fig.update_layout(title="Change in EV vs Base Case ($M)",
                          barmode="overlay", template="plotly_white", height=300)
        st.plotly_chart(fig, use_container_width=True)

    # ── PORTFOLIO OPTIMISER ───────────────────────────────────────────────────
    with tab3:
        _sec("Efficient Frontier — Portfolio Optimisation", "📊")
        assets   = ["Equities","Bonds","Real Estate","Commodities","Private Equity"]
        defaults = [8.5, 3.2, 6.0, 4.5, 12.0]
        cols_r   = st.columns(len(assets))
        rets     = []
        for i, col in enumerate(cols_r):
            with col:
                rets.append(st.number_input(f"{assets[i]} (%)", value=defaults[i],
                                            step=0.5, key=f"rt{i}") / 100)
        vols = np.array([0.16, 0.05, 0.12, 0.18, 0.22])
        corr = np.array([
            [1.00,-0.30, 0.50, 0.20, 0.65],
            [-0.30,1.00,-0.10,-0.05,-0.25],
            [0.50,-0.10, 1.00, 0.15, 0.40],
            [0.20,-0.05, 0.15, 1.00, 0.18],
            [0.65,-0.25, 0.40, 0.18, 1.00],
        ])
        cov = np.outer(vols, vols) * corr
        rf  = 0.04
        np.random.seed(7)
        pr, pv, ps2 = [], [], []
        for _ in range(5000):
            w = np.random.dirichlet(np.ones(5))
            r = np.dot(w, rets); v = np.sqrt(w @ cov @ w)
            pr.append(r*100); pv.append(v*100); ps2.append((r-rf)/v)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=pv, y=pr, mode="markers",
            marker=dict(color=ps2, colorscale="Viridis", size=3, opacity=0.5,
                        colorbar=dict(title="Sharpe")), name="Portfolios"))
        for i, a in enumerate(assets):
            fig.add_trace(go.Scatter(x=[vols[i]*100], y=[rets[i]*100],
                mode="markers+text", text=[a], textposition="top center",
                marker=dict(size=12, color="#E24B4A", symbol="diamond"), name=a))
        fig.update_layout(title="Efficient Frontier — Yellow dots have the highest Sharpe Ratio",
                          xaxis_title="Portfolio Volatility (%)", yaxis_title="Expected Return (%)",
                          template="plotly_white", height=460, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Red diamonds = individual assets. Colour scale = Sharpe ratio (yellow = best). Upper-left curve = Efficient Frontier.")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Capital Allocation — $50M Investment Budget", "🧪")

        st.markdown("""
**Business Situation:** The CFO of a manufacturing company has **$50M** to allocate across
5 proposed business initiatives for FY2025. Each project team has submitted a business case.
Your job as Head of FP&A is to recommend the **optimal portfolio** of projects.
        """)

        st.markdown("**Step 1 — Submitted Business Cases**")
        proj = pd.DataFrame({
            "Initiative":     ["ERP Upgrade","Asia Market Expansion","R&D Innovation Lab",
                                "Factory Automation","Competitor Acquisition"],
            "Cost ($M)":      [12, 20, 8, 15, 35],
            "NPV ($M)":       [18, 45, 22, 28, 80],
            "Payback (yrs)":  [3, 4, 5, 2, 6],
            "Risk":           ["Low","High","Medium","Low","High"],
            "Strategic Fit":  ["★★★","★★★★★","★★★★","★★★","★★★★★"],
        })
        proj["NPV per $M Cost"] = (proj["NPV ($M)"] / proj["Cost ($M)"]).round(2)
        st.dataframe(proj, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — Allocation by NPV Efficiency (NPV per $M spent)**")
        proj_s = proj.sort_values("NPV per $M Cost", ascending=False)
        budget = 50; chosen = []; tc = 0; tn = 0; alloc_rows = []
        for _, row in proj_s.iterrows():
            sel = "✅ Selected" if tc + row["Cost ($M)"] <= budget else "❌ Excluded"
            if sel == "✅ Selected":
                tc += row["Cost ($M)"]
                tn += row["NPV ($M)"]
                chosen.append(row["Initiative"])
            alloc_rows.append({
                "Initiative":         row["Initiative"],
                "Cost ($M)":          row["Cost ($M)"],
                "NPV ($M)":           row["NPV ($M)"],
                "NPV per $M":         row["NPV per $M Cost"],
                "Decision":           sel,
                "Cumulative Cost":    f"${tc}M",
            })
        st.dataframe(pd.DataFrame(alloc_rows), use_container_width=True, hide_index=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Budget Available",  "$50M")
        c2.metric("Capital Deployed",  f"${tc}M")
        c3.metric("Total NPV",         f"${tn}M")
        c4.metric("Return on Capital", f"{tn/tc*100:.0f}% NPV/Cost")

        st.markdown("**Step 3 — Cost vs NPV Visualisation**")
        colours = ["#1D9E75" if p in chosen else "#E24B4A" for p in proj["Initiative"]]
        fig = go.Figure()
        for idx, row in proj.iterrows():
            fig.add_trace(go.Scatter(
                x=[row["Cost ($M)"]], y=[row["NPV ($M)"]],
                mode="markers+text", text=[row["Initiative"]], textposition="top center",
                marker=dict(size=max(12, row["NPV ($M)"]//4),
                            color=colours[idx], line=dict(width=2, color="black")),
                showlegend=False))
        fig.add_vline(x=budget, line_dash="dash", line_color="navy",
                      annotation_text=f"Budget = ${budget}M")
        fig.update_layout(
            title="Project Selection — Green = Selected, Red = Excluded",
            xaxis_title="Project Cost ($M)", yaxis_title="NPV ($M)",
            template="plotly_white", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 4 — Budget Sensitivity: How does portfolio NPV change with budget?**")
        b_sens = []
        for b in [30, 40, 50, 60, 70]:
            sel2 = []; tc2 = 0; tn2 = 0
            for _, row in proj_s.iterrows():
                if tc2 + row["Cost ($M)"] <= b:
                    sel2.append(row["Initiative"])
                    tc2 += row["Cost ($M)"]
                    tn2 += row["NPV ($M)"]
            b_sens.append({"Budget ($M)": b, "Projects": len(sel2),
                            "NPV ($M)": tn2, "NPV/Cost": f"{tn2/tc2*100:.0f}%"})
        st.dataframe(pd.DataFrame(b_sens), use_container_width=True, hide_index=True)

        fig2 = go.Figure(go.Bar(
            x=[r["Budget ($M)"] for r in b_sens],
            y=[r["NPV ($M)"] for r in b_sens],
            marker_color="#185FA5",
            text=[f"${r['NPV ($M)']}M NPV" for r in b_sens], textposition="outside"))
        fig2.update_layout(title="Portfolio NPV by Budget Level ($M)",
                           xaxis_title="Available Budget ($M)", yaxis_title="Total Portfolio NPV ($M)",
                           template="plotly_white", height=340)
        st.plotly_chart(fig2, use_container_width=True)

        st.success("""
**📋 CFO Recommendation:**

**Select:** R&D Lab ($8M) + Factory Automation ($15M) + Asia Expansion ($20M) = **$43M deployed, $95M total NPV**

**Rationale:**
- These 3 projects deliver the best NPV per dollar spent (2.75×, 1.87×, 2.25× respectively)
- Combined NPV/Cost = **221%** — far superior to any single large project
- Acquisition ($35M) is the highest absolute NPV but exceeds remaining budget and carries High risk

**Residual $7M:** Hold as contingency or fund partial ERP scope (Phase 1 only: $6M for $10M NPV)

**Risk flag:** Asia Expansion is rated High risk — recommend phased deployment with a Stage Gate review at $10M invested.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 5 Quiz", "❓")
        _quiz("1. Project: 60% chance +$10M, 40% chance -$4M, cost $2M. EV?",
              ["$4.4M","$2.4M","$5.0M","$8.0M"], "$2.4M", "m5q1")
        st.divider()
        _quiz("2. Portfolios BELOW the Efficient Frontier are:",
              ["Highest Sharpe ratio portfolios",
               "Suboptimal — dominated by portfolios offering more return for same risk",
               "Only accessible to institutional investors",
               "Zero-volatility portfolios"],
              "Suboptimal — dominated by portfolios offering more return for same risk", "m5q2")
        st.divider()
        _quiz("3. VaR(95%) = $5M means:",
              ["You will lose exactly $5M",
               "95% chance of making at least $5M",
               "On 95% of days losses will NOT exceed $5M",
               "Average daily loss is $5M"],
              "On 95% of days losses will NOT exceed $5M", "m5q3")
        st.divider()
        _quiz("4. A/B testing in finance is most useful for:",
              ["Predicting future stock prices",
               "Measuring the causal impact of a pricing or product change",
               "Building credit scoring models",
               "Stress testing a loan portfolio"],
              "Measuring the causal impact of a pricing or product change", "m5q4")
        st.divider()
        _quiz("5. Sharpe Ratio measures:",
              ["Return relative to a benchmark index",
               "Return relative to risk-free rate, per unit of volatility",
               "Maximum drawdown over a period",
               "Probability of achieving a positive return"],
              "Return relative to risk-free rate, per unit of volatility", "m5q5")