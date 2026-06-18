import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📋 IFRS 7: Financial Instruments: Disclosures")
    st.markdown("*Master the disclosure requirements for the significance and risks of financial instruments*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective")
        st.markdown("""
        **IFRS 7** requires entities to provide disclosures that enable users to evaluate:
        1. The **significance** of financial instruments to the entity's financial position and performance
        2. The **nature and extent of risks** arising from financial instruments, and how the entity manages those risks

        IFRS 7 works alongside IFRS 9 (recognition/measurement) and IAS 32 (presentation) — together these form the complete financial instruments framework.
        """)

        st.subheader("2. Significance Disclosures")
        st.markdown("""
        **By category (per IFRS 9 classification):**
        - Financial assets at amortised cost
        - Financial assets at FVOCI (debt and equity separately)
        - Financial assets at FVTPL
        - Financial liabilities at amortised cost
        - Financial liabilities at FVTPL

        **Other key significance disclosures:**
        - Carrying amounts by category
        - Items of income, expense, gains, losses by category (interest income/expense, fee income, impairment)
        - Reclassifications between categories (rare under IFRS 9)
        - Collateral pledged/held
        - Allowance account for credit losses (ECL)
        - Defaults and breaches of loan terms
        """)

        st.subheader("3. Risk Disclosures — The Three Major Risk Types")
        risk_data = pd.DataFrame({
            "Risk Type": ["Credit Risk", "Liquidity Risk", "Market Risk"],
            "Definition": [
                "Risk that one party to a financial instrument will fail to discharge an obligation, causing financial loss to the other party",
                "Risk that an entity will encounter difficulty meeting obligations associated with financial liabilities",
                "Risk that fair value or future cash flows will fluctuate due to changes in market prices"
            ],
            "Sub-Categories": [
                "Concentration risk, counterparty risk",
                "Funding risk, refinancing risk",
                "Currency risk, interest rate risk, other price risk (e.g., equity price risk)"
            ],
            "Key Disclosure": [
                "Maximum exposure to credit risk; collateral held; credit quality analysis; ECL roll-forward",
                "Maturity analysis of financial liabilities (contractual undiscounted cash flows)",
                "Sensitivity analysis showing the effect of reasonably possible changes in market variables"
            ]
        })
        st.dataframe(risk_data, use_container_width=True, hide_index=True)

        st.subheader("4. Qualitative and Quantitative Disclosures")
        st.markdown("""
        For each type of risk, IFRS 7 requires BOTH:

        **Qualitative disclosures:**
        - Exposures to risk and how they arise
        - Objectives, policies and processes for managing risk
        - Methods used to measure risk
        - Changes from prior period

        **Quantitative disclosures:**
        - Summary data based on information provided internally to key management personnel
        - Concentrations of risk
        - Sensitivity analysis for market risk (e.g., impact of +/-1% interest rate change)
        """)

        st.subheader("5. Credit Risk Disclosures (Linked to IFRS 9 ECL)")
        st.markdown("""
        Since IFRS 9 introduced the Expected Credit Loss (ECL) model, IFRS 7 requires:
        - Reconciliation of the **loss allowance** from opening to closing balance
        - Analysis of financial assets by **credit risk stage** (Stage 1: 12-month ECL; Stage 2: lifetime ECL, not credit-impaired; Stage 3: lifetime ECL, credit-impaired)
        - Inputs, assumptions and estimation techniques used
        - Amounts arising from ECL (including write-offs and recoveries)
        - Collateral and credit enhancements held
        """)

        st.subheader("6. Fair Value Disclosures")
        st.markdown("""
        - Fair value of each class of financial asset/liability, compared to carrying amount
        - Fair value hierarchy level (IFRS 13: Level 1, 2, 3)
        - For Level 3: reconciliation of opening to closing balances, sensitivity analysis
        - Disclosures when fair value cannot be reliably measured (rare — mostly unquoted equity)
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Maturity Analysis — Liquidity Risk Disclosure")
        st.markdown("""
        **Contractual undiscounted cash flows of financial liabilities at 31 December 2024:**

        | | Less than 1 year | 1-2 years | 2-5 years | Over 5 years | Total |
        |---|---|---|---|---|---|
        | Trade payables | $2,500,000 | — | — | — | $2,500,000 |
        | Bank borrowings | $1,200,000 | $1,500,000 | $4,000,000 | $2,000,000 | $8,700,000 |
        | Lease liabilities | $400,000 | $400,000 | $900,000 | $300,000 | $2,000,000 |
        | **Total** | **$4,100,000** | **$1,900,000** | **$4,900,000** | **$2,300,000** | **$13,200,000** |

        This shows users WHEN cash outflows are expected, helping assess liquidity risk.
        """)

        st.subheader("Example 2: Credit Risk — ECL Stage Analysis")
        st.markdown("""
        **Trade receivables by ECL stage (using simplified approach):**

        | Days Past Due | Gross Carrying Amount | Expected Loss Rate | Loss Allowance |
        |---|---|---|---|
        | Current | $4,000,000 | 0.5% | $20,000 |
        | 1-30 days | $1,200,000 | 2% | $24,000 |
        | 31-60 days | $500,000 | 8% | $40,000 |
        | 61-90 days | $200,000 | 25% | $50,000 |
        | Over 90 days | $100,000 | 60% | $60,000 |
        | **Total** | **$6,000,000** | | **$194,000** |

        This provision matrix disclosure is common for trade receivables under the IFRS 9 simplified approach.
        """)

        st.subheader("Example 3: Interest Rate Sensitivity Analysis")
        st.markdown("""
        **Sensitivity to a 100 basis point (1%) change in interest rates:**

        | | Impact on P&L | Impact on Equity |
        |---|---|---|
        | +1% interest rate | ($85,000) decrease in profit | ($85,000) |
        | -1% interest rate | $85,000 increase in profit | $85,000 |

        *Based on floating rate borrowings of $8,500,000 outstanding at year-end. This assumes all other variables remain constant.*
        """)

        st.subheader("Example 4: Currency Risk Disclosure")
        st.markdown("""
        **Net foreign currency exposure by currency (functional currency: SGD):**

        | Currency | Financial Assets | Financial Liabilities | Net Exposure |
        |---|---|---|---|
        | USD | $3,200,000 | ($1,800,000) | $1,400,000 |
        | EUR | €1,500,000 | (€2,200,000) | (€700,000) |
        | GBP | £600,000 | (£100,000) | £500,000 |

        **Sensitivity:** A 10% strengthening of SGD against USD would decrease profit by approximately SGD 140,000 (assuming USD net asset position).
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Liquidity Maturity Analysis Builder")
        st.markdown("Build a contractual cash flow maturity table:")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            tp_1y = st.number_input("Trade Payables <1yr ($)", value=2500000, step=10000)
        with col2:
            bb_1y = st.number_input("Bank Borrowings <1yr ($)", value=1200000, step=10000)
            bb_2y = st.number_input("Bank Borrowings 1-2yr ($)", value=1500000, step=10000)
            bb_5y = st.number_input("Bank Borrowings 2-5yr ($)", value=4000000, step=10000)
        with col3:
            ll_1y = st.number_input("Lease Liab <1yr ($)", value=400000, step=10000)
            ll_2y = st.number_input("Lease Liab 1-2yr ($)", value=400000, step=10000)
        with col4:
            bb_5plus = st.number_input("Bank Borrowings >5yr ($)", value=2000000, step=10000)
            ll_5y = st.number_input("Lease Liab 2-5yr ($)", value=900000, step=10000)

        if st.button("Build Maturity Table"):
            maturity_df = pd.DataFrame({
                "Liability": ["Trade Payables", "Bank Borrowings", "Lease Liabilities", "TOTAL"],
                "<1 year": [tp_1y, bb_1y, ll_1y, tp_1y+bb_1y+ll_1y],
                "1-2 years": [0, bb_2y, ll_2y, bb_2y+ll_2y],
                "2-5 years": [0, bb_5y, ll_5y, bb_5y+ll_5y],
                ">5 years": [0, bb_5plus, 0, bb_5plus]
            })
            maturity_df["Total"] = maturity_df[["<1 year","1-2 years","2-5 years",">5 years"]].sum(axis=1)
            st.dataframe(maturity_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔧 Tool 2: ECL Provision Matrix Calculator")
        st.markdown("Calculate expected credit losses using a provision matrix:")
        buckets = ["Current", "1-30 days", "31-60 days", "61-90 days", ">90 days"]
        rows_input = []
        for b in buckets:
            c1, c2 = st.columns(2)
            amt = c1.number_input(f"{b} — Gross Amount ($)", value=1000000, step=10000, key=f"ecl_amt_{b}")
            rate = c2.number_input(f"{b} — Loss Rate (%)", value=1.0, step=0.5, key=f"ecl_rate_{b}")
            rows_input.append((b, amt, rate))

        if st.button("Calculate ECL Provision"):
            ecl_rows = []
            total_gross = 0
            total_ecl = 0
            for b, amt, rate in rows_input:
                ecl = amt * rate / 100
                total_gross += amt
                total_ecl += ecl
                ecl_rows.append({"Bucket": b, "Gross Amount ($)": f"{amt:,.0f}", "Loss Rate (%)": f"{rate:.1f}%", "ECL Provision ($)": f"{ecl:,.0f}"})
            ecl_rows.append({"Bucket": "TOTAL", "Gross Amount ($)": f"{total_gross:,.0f}", "Loss Rate (%)": "—", "ECL Provision ($)": f"{total_ecl:,.0f}"})
            st.dataframe(pd.DataFrame(ecl_rows), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Interest Rate Sensitivity Calculator")
        floating_debt = st.number_input("Floating Rate Debt Outstanding ($)", value=8500000, step=100000)
        rate_shift = st.number_input("Interest Rate Shift (basis points)", value=100, step=25)
        if st.button("Calculate Sensitivity"):
            impact = floating_debt * (rate_shift / 10000)
            st.markdown(f"""
            | Scenario | P&L Impact |
            |---|---|
            | +{rate_shift}bp rate increase | (${impact:,.0f}) decrease in profit |
            | -{rate_shift}bp rate decrease | ${impact:,.0f} increase in profit |
            """)

    with tab4:
        st.header("Visualizations")

        st.subheader("Liquidity Risk — Maturity Profile")
        buckets_chart = ["<1 year", "1-2 years", "2-5 years", ">5 years"]
        amounts_chart = [4100000, 1900000, 4900000, 2300000]
        fig = go.Figure(go.Bar(x=buckets_chart, y=amounts_chart, marker_color=["#F87171","#F59E0B","#FBBF24","#34D399"]))
        fig.update_layout(title="Contractual Maturity Profile of Financial Liabilities", yaxis_title="Amount ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Credit Risk — ECL by Aging Bucket")
        buckets2 = ["Current", "1-30 days", "31-60 days", "61-90 days", ">90 days"]
        gross_vals = [4000000, 1200000, 500000, 200000, 100000]
        loss_rates = [0.5, 2, 8, 25, 60]
        ecl_vals = [g*r/100 for g, r in zip(gross_vals, loss_rates)]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=buckets2, y=gross_vals, name="Gross Receivable", marker_color="#2563EB", yaxis="y"))
        fig2.add_trace(go.Scatter(x=buckets2, y=loss_rates, name="Loss Rate (%)", line=dict(color="#F87171", width=2), mode="lines+markers", yaxis="y2"))
        fig2.update_layout(title="Trade Receivables — ECL Provision Matrix",
                          yaxis=dict(title="Gross Amount ($)"), yaxis2=dict(title="Loss Rate (%)", overlaying="y", side="right"), height=400)
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Three Major Risk Categories Under IFRS 7")
        fig3 = go.Figure(go.Pie(labels=["Credit Risk", "Liquidity Risk", "Market Risk"], values=[1,1,1], hole=0.4,
                                marker_colors=["#F87171","#F59E0B","#2563EB"]))
        fig3.update_layout(title="IFRS 7 Risk Disclosure Framework", height=350)
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. IFRS 7 disclosures are designed to help users evaluate:**")
        q1 = st.radio("", [
            "Only the fair value of financial instruments",
            "The significance of financial instruments and the nature/extent of risks arising from them",
            "Only credit risk",
            "Compliance with banking regulations"
        ], key="ifrs7q1")
        if st.button("Check Answer", key="ifrs7c1"):
            if q1 == "The significance of financial instruments and the nature/extent of risks arising from them":
                st.success("✅ Correct! IFRS 7's twin objectives are: (1) significance to financial position/performance, and (2) nature and extent of risks and how they are managed.")
            else:
                st.error("❌ IFRS 7 covers BOTH significance AND risk disclosures — not just fair value or one risk type.")

        st.markdown("---")
        st.markdown("**2. The three major categories of risk disclosed under IFRS 7 are:**")
        q2 = st.radio("", [
            "Credit risk, liquidity risk, market risk",
            "Operational risk, strategic risk, reputational risk",
            "Currency risk, interest rate risk, equity risk",
            "Audit risk, business risk, fraud risk"
        ], key="ifrs7q2")
        if st.button("Check Answer", key="ifrs7c2"):
            if q2 == "Credit risk, liquidity risk, market risk":
                st.success("✅ Correct! IFRS 7's three major risk categories are Credit Risk, Liquidity Risk, and Market Risk (with market risk further split into currency, interest rate, and other price risk).")
            else:
                st.error("❌ The three IFRS 7 risk categories are: Credit Risk, Liquidity Risk, and Market Risk.")

        st.markdown("---")
        st.markdown("**3. A maturity analysis of financial liabilities discloses:**")
        q3 = st.radio("", [
            "Discounted present value of liabilities",
            "Contractual undiscounted cash flows by time bucket",
            "Fair value of liabilities only",
            "Historical cost of liabilities"
        ], key="ifrs7q3")
        if st.button("Check Answer", key="ifrs7c3"):
            if q3 == "Contractual undiscounted cash flows by time bucket":
                st.success("✅ Correct! The liquidity risk maturity analysis shows CONTRACTUAL UNDISCOUNTED cash flows grouped into time bands — this differs from the discounted balance sheet carrying amount.")
            else:
                st.error("❌ Maturity analysis uses CONTRACTUAL UNDISCOUNTED cash flows, not discounted/fair value amounts.")

        st.markdown("---")
        st.markdown("**4. Sensitivity analysis for market risk shows:**")
        q4 = st.radio("", [
            "Historical volatility over the past 5 years",
            "The effect on P&L/equity of reasonably possible changes in a relevant market variable",
            "Only worst-case scenario losses",
            "Credit rating changes"
        ], key="ifrs7q4")
        if st.button("Check Answer", key="ifrs7c4"):
            if q4 == "The effect on P&L/equity of reasonably possible changes in a relevant market variable":
                st.success("✅ Correct! Sensitivity analysis shows the impact of REASONABLY POSSIBLE changes (e.g., +/-1% interest rate, +/-10% FX rate) on P&L and equity — not extreme or historical scenarios.")
            else:
                st.error("❌ Sensitivity analysis = effect of REASONABLY POSSIBLE changes in market variables on P&L/equity.")

        st.markdown("---")
        st.markdown("**5. Under IFRS 9's ECL model, financial assets are typically disclosed by:**")
        q5 = st.radio("", [
            "Legal jurisdiction only",
            "Credit risk stage (12-month ECL vs lifetime ECL, credit-impaired or not)",
            "Currency denomination only",
            "Original maturity date only"
        ], key="ifrs7q5")
        if st.button("Check Answer", key="ifrs7c5"):
            if q5 == "Credit risk stage (12-month ECL vs lifetime ECL, credit-impaired or not)":
                st.success("✅ Correct! IFRS 7 requires disclosure by ECL stage: Stage 1 (12-month ECL), Stage 2 (lifetime ECL, not credit-impaired), Stage 3 (lifetime ECL, credit-impaired).")
            else:
                st.error("❌ ECL disclosures are organised by STAGE (1, 2, 3) reflecting credit risk deterioration, as required to link with IFRS 9.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Two Disclosure Objectives
        1. **Significance** of financial instruments to financial position/performance
        2. **Nature and extent of risks** + risk management

        ### 2. Significance Disclosures
        - Carrying amounts by IFRS 9 category
        - Income/expense/gains/losses by category
        - Collateral, ECL allowance, defaults/breaches

        ### 3. Three Major Risk Types
        | Risk | Key Disclosure |
        |---|---|
        | Credit Risk | Maximum exposure, ECL stage analysis, collateral |
        | Liquidity Risk | Contractual undiscounted maturity analysis |
        | Market Risk | Sensitivity analysis (interest rate, currency, price) |

        ### 4. Qualitative + Quantitative
        - Qualitative: exposures, policies, risk management objectives
        - Quantitative: summary data, concentrations, sensitivity analysis

        ### 5. Fair Value Disclosures
        - FV vs carrying amount by class
        - IFRS 13 hierarchy level (1, 2, 3)
        - Level 3 reconciliation and sensitivity
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Maturity Analysis → CONTRACTUAL UNDISCOUNTED cash flows
ECL Disclosures → organised by STAGE (1/2/3)
Sensitivity Analysis → REASONABLY POSSIBLE changes only
Three Risks → Credit, Liquidity, Market
Both Qualitative AND Quantitative disclosures required for each risk
        """)

        st.success("🎓 **IFRS 7 Complete!** You can now prepare significance disclosures, risk disclosures, maturity analyses and sensitivity analyses for financial instruments.")
        st.info("💡 **Next**: IFRS 8 — Operating Segments")

if __name__ == "__main__":
    show()