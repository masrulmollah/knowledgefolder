import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

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
    st.title("🤖 Module 8: Advanced & AI-Powered Analytics")
    st.caption("Machine learning, Monte Carlo simulation, advanced segmentation, and insight storytelling")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Monte Carlo Simulator", "📊 Driver Importance", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Advanced Statistical & ML Techniques", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**From Traditional Statistics to Machine Learning:**

| Technique | Finance Application | Output |
|-----------|--------------------|-----------------------------|
| Multiple Regression | Revenue forecasting from multiple drivers | Coefficient per driver |
| Decision Tree | Customer churn / credit risk classification | Decision rules |
| Random Forest | Cost driver identification across 100+ variables | Feature importance score |
| Gradient Boosting | High-accuracy forecast (EBITDA, cashflow) | Prediction + confidence |
| K-Means Clustering | Customer / supplier / SKU segmentation | Segment labels |
| PCA | Reduce 50 cost variables to 5 key components | Principal components |
| Isolation Forest | Automated anomaly detection in GL data | Anomaly score |

**Key ML Concepts for Finance Professionals:**
- **Overfitting:** Model fits historical data perfectly but fails on new data → use train/test split
- **Feature Importance:** Which variables drive the prediction most → replaces manual driver analysis
- **Regularisation (Lasso/Ridge):** Prevents model from relying on too many weak variables
- **Cross-Validation:** Test model accuracy across multiple data splits, not just one
            """)
        with c2:
            st.markdown("""
**Monte Carlo Simulation for Finance:**
```
1. Define key uncertain variables (revenue growth, 
   raw material cost, FX rate, churn rate)
2. Assign a probability distribution to each
   (normal, triangular, uniform, lognormal)
3. Run 10,000 iterations — each samples randomly
   from every distribution simultaneously
4. Compile the distribution of output outcomes
5. Read: P10, P50 (median), P90, probability of
   achieving budget target
```
**Why it beats scenario planning:**
Scenario planning gives 3 snapshots (Best/Base/Worst).
Monte Carlo gives the full probability distribution — 
you know there's a 23% chance of missing budget, not just 
that a worst case exists.

**Tornado Chart (Sensitivity Ranking):**
Each input variable is moved ±10% (or 1 std dev) while
others stay fixed. The output range for each variable is 
plotted as a horizontal bar. Longest bar = most critical risk.
            """)

        _sec("AI-Assisted Finance & Insight Storytelling", "✨")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**AI Applications in Corporate Finance:**

| Application | What AI Does | Time Saved |
|------------|-------------|------------|
| Variance commentary | Auto-generates written narrative for P&L movements | 2–4 hrs/month |
| Anomaly detection | Screens all GL transactions for outliers at close | 1–2 days/month |
| Driver-based forecasting | Learns relationships between drivers and outcomes | Improves accuracy |
| Cash flow prediction | LSTM / ML models predict 13-week cash | Increases precision |
| Contract analytics | NLP extracts payment terms, penalties from contracts | Days → minutes |
| Earnings call analysis | Sentiment scoring of management commentary | Real-time insights |

**Copilot-Assisted Financial Modelling:**
- Drafting Excel formulas from natural language prompts
- Auto-formatting management report templates
- Generating SQL queries for financial data extraction
- Explaining complex financial models in plain language
            """)
        with c2:
            st.markdown("""
**The Insight Communication Framework:**

**SCR (Situation → Complication → Resolution):**
```
Situation:    "Revenue is $482M, $18M below budget."
Complication: "The miss is entirely volume-driven; 
               price is actually +$6M ahead."
Resolution:   "Two Mid-Market accounts deferred orders. 
               We recommend a targeted retention offer 
               approved by CFO by Friday."
```
**The So-What? Test:**
Every data point must pass: *"So what does this mean for the business?"*
Data without a so-what is a number, not an insight.

**Insight → Action → Outcome Framework:**
- **Insight:** Revenue mix shifting to lower-margin products
- **Action:** Implement sales incentive to push premium SKUs
- **Outcome:** +1.5pp GM improvement within 2 quarters

**Chart design principles for finance:**
- Lead with the insight in the chart title (not just the metric)
- Use colour purposefully: red = bad, green = good, grey = context
- Annotate the key point — don't make the reader find it
- Show the comparison the audience needs (vs. budget, vs. prior year)
            """)

    # ── MONTE CARLO SIMULATOR ─────────────────────────────────────────────────
    with tab2:
        _sec("Monte Carlo EBITDA Simulator", "🧮")
        st.markdown("Define uncertainty ranges for key drivers and simulate 10,000 possible EBITDA outcomes:")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Revenue Driver**")
            rev_base    = st.number_input("Base Revenue ($M)",    value=500.0, step=10.0, key="mc_rev")
            rev_mu      = st.number_input("Expected Growth %",    value=7.0,   step=0.5,  key="mc_rmu")
            rev_sigma   = st.number_input("Std Dev of Growth %",  value=4.0,   step=0.5,  key="mc_rsd")
        with c2:
            st.markdown("**COGS Driver**")
            cogs_base   = st.number_input("Base COGS % of Rev",   value=56.0,  step=1.0,  key="mc_cogs")
            cogs_mu     = st.number_input("Expected COGS % Drift",value=1.0,   step=0.5,  key="mc_cmu",
                                          help="Positive = cost inflation")
            cogs_sigma  = st.number_input("Std Dev of COGS %",    value=2.5,   step=0.5,  key="mc_csd")
        with c3:
            st.markdown("**SG&A Driver**")
            sga_base    = st.number_input("Base SG&A % of Rev",   value=20.0,  step=1.0,  key="mc_sga")
            sga_sigma   = st.number_input("Std Dev of SG&A %",    value=1.5,   step=0.5,  key="mc_ssd")

        budget_ebitda = st.number_input("Budget EBITDA ($M) — target line",
                                        value=115.0, step=5.0, key="mc_budget")
        n_sims = 10000
        np.random.seed(42)

        rev_sims  = rev_base * (1 + np.random.normal(rev_mu/100, rev_sigma/100, n_sims))
        cogs_sims = (cogs_base + np.random.normal(cogs_mu, cogs_sigma, n_sims)) / 100
        sga_sims  = (sga_base  + np.random.normal(0, sga_sigma, n_sims)) / 100
        ebitda_sims = rev_sims * (1 - cogs_sims - sga_sims)

        p10   = np.percentile(ebitda_sims, 10)
        p50   = np.percentile(ebitda_sims, 50)
        p90   = np.percentile(ebitda_sims, 90)
        prob_budget = (ebitda_sims >= budget_ebitda).sum() / n_sims * 100
        prob_loss   = (ebitda_sims < 0).sum() / n_sims * 100

        fig = go.Figure()
        fig.add_trace(go.Histogram(x=ebitda_sims, nbinsx=80,
                                   marker_color="#185FA5", opacity=0.7, name="EBITDA simulations"))
        fig.add_vline(x=p10,           line_dash="dash", line_color="#E24B4A",
                      annotation_text=f"P10: ${p10:.0f}M", annotation_position="top")
        fig.add_vline(x=p50,           line_dash="solid", line_color="#1D9E75",
                      annotation_text=f"P50: ${p50:.0f}M", annotation_position="top")
        fig.add_vline(x=p90,           line_dash="dash", line_color="#1D9E75",
                      annotation_text=f"P90: ${p90:.0f}M", annotation_position="top")
        fig.add_vline(x=budget_ebitda, line_dash="dot", line_color="orange",
                      annotation_text=f"Budget: ${budget_ebitda:.0f}M", annotation_position="top")
        fig.update_layout(title=f"Monte Carlo EBITDA Distribution — {n_sims:,} Simulations",
                          xaxis_title="EBITDA ($M)", yaxis_title="Frequency",
                          template="plotly_white", height=420)
        st.plotly_chart(fig, use_container_width=True)

        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("P10 (Downside)",   f"${p10:.0f}M")
        c2.metric("P50 (Base/Median)",f"${p50:.0f}M")
        c3.metric("P90 (Upside)",     f"${p90:.0f}M")
        c4.metric("Prob of Meeting Budget", f"{prob_budget:.0f}%",
                  delta="✅ High confidence" if prob_budget > 65 else "⚠️ At risk")
        c5.metric("Prob of EBITDA Loss",    f"{prob_loss:.1f}%")

        st.markdown("**Tornado Chart — Which Driver Has Most Impact?**")
        base_ebitda_est = rev_base * (1 - cogs_base/100 - sga_base/100) * (1 + rev_mu/100)
        tornado_data = []
        for name, delta, direction in [
            ("Revenue Growth ±1σ",    rev_sigma,  "rev"),
            ("COGS % ±1σ",            cogs_sigma, "cogs"),
            ("SG&A % ±1σ",            sga_sigma,  "sga"),
        ]:
            if direction == "rev":
                hi = rev_base * (1 + (rev_mu + rev_sigma)/100) * (1 - cogs_base/100 - sga_base/100)
                lo = rev_base * (1 + (rev_mu - rev_sigma)/100) * (1 - cogs_base/100 - sga_base/100)
            elif direction == "cogs":
                hi = rev_base * (1 + rev_mu/100) * (1 - (cogs_base - cogs_sigma)/100 - sga_base/100)
                lo = rev_base * (1 + rev_mu/100) * (1 - (cogs_base + cogs_sigma)/100 - sga_base/100)
            else:
                hi = rev_base * (1 + rev_mu/100) * (1 - cogs_base/100 - (sga_base - sga_sigma)/100)
                lo = rev_base * (1 + rev_mu/100) * (1 - cogs_base/100 - (sga_base + sga_sigma)/100)
            tornado_data.append({"Driver": name, "Low ($M)": round(lo,1), "High ($M)": round(hi,1),
                                  "Range ($M)": round(hi - lo, 1)})

        tornado_df = pd.DataFrame(tornado_data).sort_values("Range ($M)", ascending=True)
        fig2 = go.Figure()
        for _, row in tornado_df.iterrows():
            fig2.add_trace(go.Bar(
                y=[row["Driver"]], x=[row["Range ($M)"]],
                orientation="h", name=row["Driver"],
                marker_color="#185FA5",
                text=f"${row['Range ($M)']:.0f}M range",
                textposition="outside",
            ))
        fig2.update_layout(title="Tornado Chart — EBITDA Sensitivity by Driver (1 Std Dev)",
                           xaxis_title="EBITDA Range ($M)", template="plotly_white",
                           height=300, showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)
        st.info(f"📌 **Most critical risk driver: {tornado_df.iloc[-1]['Driver']}** — accounts for the widest range of EBITDA outcomes. This is where risk management effort should be focused.")

    # ── DRIVER IMPORTANCE ─────────────────────────────────────────────────────
    with tab3:
        _sec("Feature / Driver Importance Analysis (Simulated ML)", "📊")
        st.markdown("""
In machine learning, **feature importance** quantifies how much each input variable
contributes to predicting the target metric. In finance, this replaces subjective
driver analysis with data-driven evidence.
        """)
        target = st.selectbox("Target metric to explain:",
                              ["EBITDA Variance", "Customer Churn", "Revenue Growth", "Working Capital Days"])

        driver_sets = {
            "EBITDA Variance":   ["Volume","Raw Material Price","FX Rate","Headcount","Energy Cost","Mix Shift","Price Realisation","Overheads"],
            "Customer Churn":    ["Contract Age","Last Purchase Days","Support Tickets","Discount Received","Account Manager Tenure","Industry","Payment History","Product Count"],
            "Revenue Growth":    ["GDP Growth","Marketing Spend","Sales Headcount","New Product Launches","Price Change","Market Share","Customer NPS","Competitor Activity"],
            "Working Capital Days":["Payment Terms","Invoice Accuracy","Sales Volume Variation","Supplier Concentration","ERP System","Manual Process %","Credit Limit Policy","Seasonality"],
        }

        drivers = driver_sets[target]
        np.random.seed(hash(target) % 999)
        importances = np.random.dirichlet(np.ones(len(drivers)) * 2) * 100
        importances = np.sort(importances)[::-1]

        imp_df = pd.DataFrame({
            "Driver": drivers,
            "Importance %": importances.round(1),
            "Cumulative %": np.cumsum(importances).round(1),
            "Tier": ["🔴 Critical" if v >= np.percentile(importances, 75)
                     else "🟡 Significant" if v >= np.percentile(importances, 50)
                     else "⚪ Minor" for v in importances]
        }).sort_values("Importance %", ascending=False)

        fig = go.Figure(go.Bar(
            y=imp_df["Driver"], x=imp_df["Importance %"],
            orientation="h",
            marker_color=["#E24B4A" if t == "🔴 Critical"
                          else "#EF9F27" if t == "🟡 Significant"
                          else "#B5D4F4" for t in imp_df["Tier"]],
            text=[f"{v:.1f}%" for v in imp_df["Importance %"]],
            textposition="outside",
        ))
        fig.update_layout(title=f"Driver Importance — {target}",
                          xaxis_title="Importance (%)", template="plotly_white",
                          height=420, yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(imp_df, use_container_width=True, hide_index=True)

        top3 = imp_df.head(3)["Driver"].tolist()
        st.success(f"📌 **Top 3 drivers of {target}:** {', '.join(top3)}. "
                   f"These account for {imp_df.head(3)['Importance %'].sum():.0f}% of explained variance. "
                   f"Focus diagnostic and risk management efforts here first.")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Full Analytics-to-Insight Narrative — Annual Plan Review", "🧪")
        st.markdown("""
**Situation:** It's October. You are the CFO of a $600M revenue manufacturing group.
The Board has asked for a complete analytics narrative covering:
1. How did FY2024 perform vs. plan?
2. Where is value being created and destroyed?
3. What does the Monte Carlo model say about FY2025 budget achievability?
4. What are the top 3 actions to take before year-end?

This is the integrated analytics story you present.
        """)

        st.markdown("**Chapter 1 — FY2024 Performance vs. Plan**")
        categories = ["Revenue", "Gross Profit", "SG&A", "EBITDA", "FCF"]
        budget_24  = [600, 252, -120, 132, 88]
        actual_24  = [587, 241, -128, 113, 71]
        variance   = [a-b for a,b in zip(actual_24, budget_24)]

        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=categories, y=budget_24, name="Budget", marker_color="#B5D4F4"))
        fig1.add_trace(go.Bar(x=categories, y=actual_24, name="Actual", marker_color="#185FA5"))
        fig1.update_layout(title="FY2024: Budget vs. Actual ($M)",
                           barmode="group", template="plotly_white", height=360,
                           yaxis_title="$M", legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig1, use_container_width=True)

        c1, c2, c3 = st.columns(3)
        c1.metric("Revenue vs. Budget",  f"${variance[0]:+}M", delta=f"{variance[0]/budget_24[0]*100:+.1f}%")
        c2.metric("EBITDA vs. Budget",   f"${variance[3]:+}M", delta=f"{variance[3]/budget_24[3]*100:+.1f}%")
        c3.metric("FCF vs. Budget",      f"${variance[4]:+}M", delta=f"{variance[4]/budget_24[4]*100:+.1f}%")

        st.markdown("**Chapter 2 — Value Creation Map by Business Unit**")
        bus_units = ["Consumer", "Industrial", "Pharma", "Services", "Corporate"]
        rev_bu    = [220, 180, 110, 77, 0]
        ebitda_bu = [38, 29, 31, 8, -14]
        wacc_bu   = 0.10
        cap_emp   = [85, 95, 60, 35, 20]
        eva_bu    = [e - w * c for e, w, c in zip(ebitda_bu, [wacc_bu]*5, cap_emp)]

        bu_df = pd.DataFrame({
            "Business Unit": bus_units,
            "Revenue ($M)": rev_bu,
            "EBITDA ($M)":  ebitda_bu,
            "EBITDA Margin %": [round(e/r*100,1) if r > 0 else "N/A" for e, r in zip(ebitda_bu, rev_bu)],
            "Capital Employed ($M)": cap_emp,
            "EVA ($M)":     [round(e, 1) for e in eva_bu],
            "Value Status": ["✅ Creating" if e > 0 else "🔴 Destroying" for e in eva_bu],
        })
        st.dataframe(bu_df, use_container_width=True, hide_index=True)

        fig2 = go.Figure(go.Bar(
            x=bus_units, y=eva_bu,
            marker_color=["#1D9E75" if e > 0 else "#E24B4A" for e in eva_bu],
            text=[f"${e:+.1f}M" for e in eva_bu], textposition="outside"
        ))
        fig2.add_hline(y=0, line_color="black", line_width=1)
        fig2.update_layout(title="Economic Value Added (EVA) by Business Unit ($M) — WACC = 10%",
                           template="plotly_white", height=360, yaxis_title="EVA ($M)")
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Chapter 3 — FY2025 Budget Achievability (Monte Carlo)**")
        np.random.seed(24)
        n = 10000
        rev_fc   = np.random.normal(620, 35, n)
        cogs_fc  = rev_fc * np.random.normal(0.575, 0.025, n)
        sga_fc   = rev_fc * np.random.normal(0.21, 0.015, n)
        ebitda_fc = rev_fc - cogs_fc - sga_fc
        budget_25 = 130

        p10_fc = np.percentile(ebitda_fc, 10)
        p50_fc = np.percentile(ebitda_fc, 50)
        p90_fc = np.percentile(ebitda_fc, 90)
        prob_25 = (ebitda_fc >= budget_25).mean() * 100

        fig3 = go.Figure()
        fig3.add_trace(go.Histogram(x=ebitda_fc, nbinsx=80,
                                    marker_color="#185FA5", opacity=0.7))
        fig3.add_vline(x=p50_fc,    line_dash="solid", line_color="#1D9E75",
                       annotation_text=f"P50: ${p50_fc:.0f}M", annotation_position="top")
        fig3.add_vline(x=budget_25, line_dash="dot",   line_color="orange",
                       annotation_text=f"Budget: ${budget_25}M", annotation_position="top")
        fig3.add_vline(x=p10_fc,    line_dash="dash",  line_color="#E24B4A",
                       annotation_text=f"P10: ${p10_fc:.0f}M", annotation_position="top")
        fig3.update_layout(title=f"FY2025 EBITDA Monte Carlo — Budget Achievability: {prob_25:.0f}%",
                           xaxis_title="EBITDA ($M)", template="plotly_white", height=380)
        st.plotly_chart(fig3, use_container_width=True)

        st.success(f"""
**Board Narrative — Integrated Analytics Story:**

**FY2024 Performance:** Revenue missed by $13M (−2.2%) due to volume shortfall in Industrial and Services.
EBITDA missed by $19M (−14%) — revenue miss plus $8M SG&A over-run (pre-approved hiring ahead of revenue).
FCF underperformed by $17M; working capital built $9M above plan.

**Value Creation:** Consumer and Pharma are creating economic value (positive EVA).
Industrial is marginally negative EVA — capital efficiency must improve.
Corporate overhead is the largest single value drag at −$14M EVA.

**FY2025 Budget Achievability:** Monte Carlo shows **{prob_25:.0f}% probability** of hitting the $130M EBITDA budget.
P50 (median) = ${p50_fc:.0f}M. P10 downside = ${p10_fc:.0f}M.
The budget is achievable but stretching — it requires both revenue growth AND cost discipline.

**Top 3 Pre-Year-End Actions:**
1. ✅ Resolve Industrial EVA gap: 5pp margin improvement programme → closes $6M EVA deficit
2. ✅ Freeze Corporate overhead at current run-rate; zero-base 2 cost lines before AOP lock
3. ✅ Accelerate AR collection to release $8M trapped cash before Dec 31 year-end
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 8 Quiz", "❓")
        _quiz("1. A Monte Carlo simulation shows P10 = $80M, P50 = $105M, P90 = $130M for EBITDA. What does P10 mean?",
              ["There is a 10% chance EBITDA exceeds $80M",
               "There is a 90% probability that EBITDA will be at least $80M",
               "There is a 10% probability that EBITDA will be at least $80M",
               "$80M is the most likely outcome"],
              "There is a 90% probability that EBITDA will be at least $80M", "fa_m8q1")
        st.divider()
        _quiz("2. In a Tornado chart, the longest bar indicates:",
              ["The most complex variable to model",
               "The variable with the greatest impact on the output — top priority for risk management",
               "The variable with the highest average value",
               "The variable most likely to improve"],
              "The variable with the greatest impact on the output — top priority for risk management", "fa_m8q2")
        st.divider()
        _quiz("3. Feature importance in a Random Forest model tells you:",
              ["The value of each input variable",
               "Which input variables contributed most to explaining the target outcome",
               "Whether the model is overfitting",
               "The accuracy of the training data"],
              "Which input variables contributed most to explaining the target outcome", "fa_m8q3")
        st.divider()
        _quiz("4. The SCR communication framework stands for:",
              ["Statistics, Charts, Recommendations",
               "Situation, Complication, Resolution",
               "Summary, Context, Results",
               "Source, Calculation, Report"],
              "Situation, Complication, Resolution", "fa_m8q4")
        st.divider()
        _quiz("5. EVA (Economic Value Added) is positive when:",
              ["Revenue exceeds operating costs",
               "EBITDA margin exceeds industry average",
               "NOPAT exceeds the total cost of capital employed (WACC × Invested Capital)",
               "The company has no debt"],
              "NOPAT exceeds the total cost of capital employed (WACC × Invested Capital)", "fa_m8q5")
        st.divider()
        _quiz("6. Overfitting in a predictive model means:",
              ["The model is too simple to capture patterns",
               "The model memorised the training data but performs poorly on new data",
               "The model has too few input variables",
               "The forecast MAPE is below 5%"],
              "The model memorised the training data but performs poorly on new data", "fa_m8q6")