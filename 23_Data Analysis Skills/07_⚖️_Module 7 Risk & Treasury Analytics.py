import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

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
    st.title("🏦 Module 7: Risk & Treasury Analytics")
    st.caption("Quantify, model and manage financial risk")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts","🧮 VaR Calculator","📊 ECL Calculator","🧪 Worked Example","❓ Quiz"
    ])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Risk Categories in Finance","⚠️")
        st.dataframe(pd.DataFrame({
            "Risk Type":       ["Market Risk","Credit Risk","Liquidity Risk",
                                 "Operational Risk","FX / Rate Risk"],
            "Definition":      ["Loss from adverse market price moves (equities, rates, FX)",
                                 "Loss from borrower or counterparty default",
                                 "Inability to meet obligations as they fall due",
                                 "Loss from failed processes, systems, people or external events",
                                 "Adverse impact from FX or interest rate movements"],
            "Key Metrics":     ["VaR, CVaR, Greeks, Stress P&L",
                                 "PD, LGD, EAD, ECL, NPL ratio",
                                 "LCR, NSFR, Cash Flow at Risk",
                                 "Loss frequency × severity, KRI dashboards",
                                 "DV01, duration, net open FX position"],
            "Regulation":      ["FRTB (Basel IV)","IFRS 9 / Basel III",
                                 "LCR (Basel III)","Basel III SMA","IFRS 9"],
        }), use_container_width=True, hide_index=True)

        _sec("VaR Methods Compared","📐")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("""**Parametric (Variance-Covariance)**

`VaR = P × σ × z × √t`

P = portfolio value
σ = daily volatility
z = 1.645 (95%) / 2.326 (99%)

✅ Fast to calculate
⚠️ Assumes normality — understates fat tails""")
        with c2:
            st.info("""**Historical Simulation**

1. Take last 250–500 days of returns
2. Apply each day's return to today's portfolio
3. Sort P&L low → high
4. VaR = 5th percentile loss

✅ No distributional assumption
⚠️ Limited by historical window""")
        with c3:
            st.info("""**Monte Carlo**

1. Simulate 10,000+ return paths
2. Apply to all positions
3. Read off the loss distribution

✅ Handles complex instruments
✅ Can model fat tails explicitly
⚠️ Computationally intensive""")

        _sec("IFRS 9 Expected Credit Loss (ECL)","📊")
        st.markdown("""
**Three-Stage Model**
| Stage   | Criteria                                | ECL Measurement             |
|---------|-----------------------------------------|-----------------------------|
| Stage 1 | No significant credit deterioration     | 12-month ECL                |
| Stage 2 | Significant increase in credit risk     | Lifetime ECL                |
| Stage 3 | Credit-impaired / defaulted             | Lifetime ECL + NPV recoveries|

**ECL Formula:**  `ECL = PD × LGD × EAD × DF`

- **PD** = Probability of Default (12-month or lifetime)
- **LGD** = Loss Given Default = 1 − Recovery Rate
- **EAD** = Exposure at Default
- **DF** = Discount Factor at effective interest rate
        """)

    # ── VaR CALCULATOR ────────────────────────────────────────────────────────
    with tab2:
        _sec("Value at Risk (VaR) Calculator","🧮")
        c1, c2, c3 = st.columns(3)
        with c1:
            pv  = st.number_input("Portfolio Value ($M)", value=100.0, step=10.0)
            dv  = st.slider("Daily Volatility (%)", 0.1, 5.0, 1.2, 0.1)
        with c2:
            conf = st.selectbox("Confidence Level", ["90%","95%","99%","99.9%"], index=1)
            hd   = st.slider("Holding Period (days)", 1, 30, 1)
        with c3:
            meth = st.selectbox("Method", ["Parametric","Historical Simulation"])

        zm = {"90%":1.282,"95%":1.645,"99%":2.326,"99.9%":3.090}
        z  = zm[conf]; cp = float(conf.rstrip("%"))

        if meth == "Parametric":
            v1   = pv * (dv/100) * z
            vt   = v1 * np.sqrt(hd)
            cvar = pv * (dv/100) * stats.norm.pdf(z) / (1-cp/100)
            c1,c2,c3 = st.columns(3)
            c1.metric(f"1-day VaR ({conf})",           f"${v1:.3f}M")
            c2.metric(f"{hd}-day VaR ({conf})",         f"${vt:.3f}M")
            c3.metric("Expected Shortfall (CVaR)",       f"${cvar:.3f}M")
            cs = np.arange(0.90, 0.9991, 0.005)
            vc = [pv*(dv/100)*stats.norm.ppf(c2) for c2 in cs]
            fig = go.Figure(go.Scatter(x=cs*100, y=vc, line=dict(color="#185FA5",width=2)))
            fig.add_vline(x=cp, line_dash="dash", line_color="red", annotation_text=conf)
            fig.update_layout(title="1-Day Parametric VaR vs Confidence Level",
                              xaxis_title="Confidence Level (%)", yaxis_title="VaR ($M)",
                              template="plotly_white", height=360)
            st.plotly_chart(fig, use_container_width=True)
        else:
            np.random.seed(42)
            rets = np.random.normal(0, dv/100, 500)
            pnl  = pv * rets
            vhs  = -np.percentile(pnl, 100-cp)
            cvhs = -pnl[pnl <= -vhs].mean()
            c1,c2 = st.columns(2)
            c1.metric(f"Historical VaR ({conf})", f"${vhs:.3f}M")
            c2.metric("Historical CVaR",           f"${cvhs:.3f}M")
            fig = go.Figure(go.Histogram(x=pnl, nbinsx=50, marker_color="#185FA5", opacity=0.7))
            fig.add_vline(x=-vhs, line_dash="dash", line_color="red",
                          annotation_text=f"VaR: -${vhs:.2f}M")
            fig.update_layout(title="Historical P&L Distribution (500 days)",
                              xaxis_title="Daily P&L ($M)", template="plotly_white", height=360)
            st.plotly_chart(fig, use_container_width=True)

    # ── ECL CALCULATOR ────────────────────────────────────────────────────────
    with tab3:
        _sec("IFRS 9 ECL Calculator","📊")
        c1, c2, c3 = st.columns(3)
        with c1:
            ead   = st.number_input("EAD ($M)", value=10.0, step=1.0)
            stage = st.selectbox("IFRS 9 Stage",["Stage 1 (12-month)","Stage 2 (Lifetime)","Stage 3 (Impaired)"])
        with c2:
            pd12  = st.slider("12-month PD (%)", 0.1, 30.0, 2.0)
            lgd   = st.slider("LGD (%)", 10.0, 90.0, 45.0)
        with c3:
            mat   = st.slider("Remaining maturity (years)", 1, 10, 3)
            er    = st.slider("Effective interest rate (%)", 2.0, 15.0, 6.0)

        annual_pd = pd12/100
        life_pd   = 1 - (1 - annual_pd)**mat
        df_factor = 1 / (1 + er/100)**(mat/2)

        if "Stage 1" in stage:
            ecl = ead * annual_pd * (lgd/100) * df_factor; pdu = annual_pd; lbl="12-month PD"
        else:
            ecl = ead * life_pd   * (lgd/100) * df_factor; pdu = life_pd;   lbl="Lifetime PD"

        c1,c2,c3,c4 = st.columns(4)
        c1.metric(lbl,          f"{pdu*100:.2f}%")
        c2.metric("LGD",        f"{lgd:.1f}%")
        c3.metric("ECL ($M)",   f"${ecl:.4f}M")
        c4.metric("Coverage %", f"{ecl/ead*100:.3f}%")

        mig = pd.DataFrame({
            "To Stage 1": [92.5, 8.0, 2.0],
            "To Stage 2": [ 6.5,82.0,12.0],
            "To Stage 3": [ 1.0,10.0,86.0],
        }, index=["From Stage 1","From Stage 2","From Stage 3"])
        fig = px.imshow(mig, text_auto=".1f", color_continuous_scale="RdYlGn",
                        title="Annual Stage Migration Matrix (%)")
        fig.update_layout(template="plotly_white", height=280)
        st.plotly_chart(fig, use_container_width=True)

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Credit Portfolio Review — Retail Bank Q3 2024","🧪")

        st.markdown("""
**Business Situation:** You are the Chief Risk Officer's analyst at a retail bank.
The Q3 2024 IFRS 9 impairment run has just been completed. You must present the
ECL movement, stage migration analysis, and early warning signals to the Risk Committee.
        """)

        st.markdown("**Step 1 — Portfolio Overview by Segment**")
        portfolio = pd.DataFrame({
            "Segment":          ["Mortgages","Personal Loans","Credit Cards","SME Loans","Auto Finance"],
            "EAD ($M)":         [4500, 1200, 800, 650, 420],
            "Stage 1 %":        [91.2, 82.4, 74.1, 78.6, 88.3],
            "Stage 2 %":        [ 7.1, 14.2, 19.8, 16.4,  9.8],
            "Stage 3 %":        [ 1.7,  3.4,  6.1,  5.0,  1.9],
            "ECL ($M)":         [18.2, 28.4, 31.5, 22.6,  7.8],
            "Coverage % (S3)":  [12.5, 38.2, 55.1, 42.0, 28.4],
        })
        st.dataframe(portfolio, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — ECL Movement (Opening → Closing Balance)**")
        ecl_mv = pd.DataFrame({
            "Movement":  ["Opening ECL Q2-24","New Originations","Stage Migrations",
                           "PD/LGD Assumption Changes","Write-offs","Recoveries","Closing ECL Q3-24"],
            "Amount ($M)": [102.4, 8.2, 15.6, 3.8, -12.4, 1.7, 119.3],
            "Type":        ["Opening","New","Migration","Model","Write-off","Recovery","Closing"],
        })
        measures = ["absolute","relative","relative","relative","relative","relative","total"]
        fig = go.Figure(go.Waterfall(
            orientation="v", measure=measures,
            x=ecl_mv["Movement"], y=ecl_mv["Amount ($M)"],
            text=[f"${v:+.1f}M" if i>0 and i<6 else f"${abs(v):.1f}M"
                  for i,v in enumerate(ecl_mv["Amount ($M)"])],
            textposition="outside",
            connector={"line":{"color":"#888"}},
            increasing={"marker":{"color":"#E24B4A"}},
            decreasing={"marker":{"color":"#1D9E75"}},
            totals={"marker":{"color":"#185FA5"}}))
        fig.update_layout(title="ECL Movement Q2→Q3 2024 ($M) — $16.9M increase",
                          template="plotly_white", height=420)
        st.plotly_chart(fig, use_container_width=True)
        st.warning("⚠️ The $15.6M stage migration charge is the primary driver. Credit Cards and SME Loans show deteriorating performance.")

        st.markdown("**Step 3 — Stage Migration Heatmap by Segment**")
        migration_data = pd.DataFrame({
            "Mortgages":     [91.2, 7.1, 1.7],
            "Personal Loans":[82.4,14.2, 3.4],
            "Credit Cards":  [74.1,19.8, 6.1],
            "SME Loans":     [78.6,16.4, 5.0],
            "Auto Finance":  [88.3, 9.8, 1.9],
        }, index=["Stage 1 %","Stage 2 %","Stage 3 %"])
        fig2 = px.imshow(migration_data, text_auto=".1f",
                         color_continuous_scale="RdYlGn_r",
                         title="Stage Distribution by Segment (%)")
        fig2.update_layout(template="plotly_white", height=300)
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Step 4 — Early Warning Indicators (KRIs)**")
        kri_df = pd.DataFrame({
            "KRI":             ["30+ days past due","90+ days past due","Debt-to-income > 50%",
                                 "Utilisation > 90% (Credit Cards)","Payment deferrals active"],
            "Q2-24":           ["3.2%","1.4%","18.2%","12.4%","2.1%"],
            "Q3-24":           ["4.1%","1.9%","20.6%","15.8%","3.4%"],
            "QoQ Change":      ["+0.9pp","+0.5pp","+2.4pp","+3.4pp","+1.3pp"],
            "Threshold":       ["4.5%","2.5%","22.0%","18.0%","4.0%"],
            "RAG Status":      ["🟡 Amber","🟢 Green","🟡 Amber","🟡 Amber","🟡 Amber"],
        })
        st.dataframe(kri_df, use_container_width=True, hide_index=True)

        st.success("""
**📋 Risk Committee Summary — Key Findings:**

1. **ECL increased $16.9M (16.5%)** in Q3-24, driven primarily by stage migrations in Credit Cards (+$8.2M) and SME Loans (+$5.1M).

2. **Credit Cards** are the highest concern: Stage 2 exposure at 19.8% (vs 14.1% one year ago) and Stage 3 at 6.1%. High-utilisation accounts (>90%) showing accelerated delinquency.

3. **Mortgages** remain robust: Stage 3 only 1.7%, ECL coverage of 12.5% — well within regulatory expectations. No action required.

4. **Early Warning:** All 5 monitored KRIs are trending adversely but remain below threshold. Credit card utilisation KRI is approaching threshold fastest — recommend proactive limit management.

**Recommended Actions:**
- Tighten Credit Card origination criteria for DTI > 45% (effective Q4-24)
- Activate enhanced monitoring for SME Loans in Retail and Hospitality sectors
- Board to be informed of ECL increase via Audit Committee briefing note
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 7 Quiz","❓")
        _quiz("1. Parametric VaR(99%), $50M portfolio, 1.5% daily vol (z=2.326)?",
              ["$0.75M","$1.13M","$1.74M","$3.49M"],"$1.74M","m7q1")
        st.divider()
        _quiz("2. Under IFRS 9, a loan moves Stage 1 → Stage 2 when:",
              ["The borrower defaults",
               "There has been a significant increase in credit risk since origination",
               "The loan has been outstanding more than 12 months","LGD exceeds 50%"],
              "There has been a significant increase in credit risk since origination","m7q2")
        st.divider()
        _quiz("3. CVaR is better than VaR because:",
              ["It is always lower than VaR",
               "It captures the average loss in the tail BEYOND the VaR threshold",
               "It requires less data","It assumes normality"],
              "It captures the average loss in the tail BEYOND the VaR threshold","m7q3")
        st.divider()
        _quiz("4. LCR (Liquidity Coverage Ratio) measures:",
              ["Long-term assets vs short-term liabilities",
               "High-quality liquid assets vs net cash outflows over 30 days",
               "12-month probability of default","Balance sheet leverage"],
              "High-quality liquid assets vs net cash outflows over 30 days","m7q4")
        st.divider()
        _quiz("5. ECL = PD×LGD×EAD×DF. PD=2%, LGD=40%, EAD=$10M, DF=0.95?",
              ["$0.076M","$0.760M","$0.800M","$0.038M"],"$0.076M","m7q5")