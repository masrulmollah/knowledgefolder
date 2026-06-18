import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💹 IFRS 9: Financial Instruments")
    st.markdown("*Master classification, measurement, impairment (ECL) and hedge accounting of financial instruments*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Scope and Structure")
        st.markdown("""
        **IFRS 9** covers three main areas:
        1. **Classification and Measurement** of financial assets and liabilities
        2. **Impairment** — the Expected Credit Loss (ECL) model
        3. **Hedge Accounting**

        It replaced IAS 39, simplifying classification and introducing forward-looking impairment.
        """)

        st.subheader("2. Classification of Financial Assets — The Business Model + Cash Flow Test")
        st.markdown("""
        Classification depends on TWO tests:

        **Test 1 — Business Model:** How does the entity manage the financial asset?
        - Hold to collect contractual cash flows
        - Hold to collect AND sell
        - Other (e.g., trading)

        **Test 2 — SPPI Test (Solely Payments of Principal and Interest):** Do the contractual cash flows represent solely payments of principal and interest on the principal outstanding?

        | Business Model | SPPI Test | Classification |
        |---|---|---|
        | Hold to collect | Passes | **Amortised Cost** |
        | Hold to collect AND sell | Passes | **FVOCI (recycling)** |
        | Other (e.g., trading) | N/A | **FVTPL** |
        | Any | Fails | **FVTPL** (mandatorily) |

        **Equity investments:** Always at FVTPL, UNLESS irrevocably elected at FVOCI (non-recycling) at initial recognition — this election is a one-time, instrument-by-instrument choice.
        """)

        st.subheader("3. Classification of Financial Liabilities")
        st.markdown("""
        Most financial liabilities → **Amortised Cost** (using the effective interest method)

        Exceptions measured at **FVTPL**:
        - Held for trading (including derivatives)
        - Designated at FVTPL (Fair Value Option) if it eliminates an accounting mismatch
        - Contingent consideration in a business combination

        **Own Credit Risk:** For liabilities designated at FVTPL, changes in fair value due to the entity's OWN credit risk → recognised in **OCI** (not P&L) to avoid the counter-intuitive result of recognising gains when an entity's own creditworthiness deteriorates.
        """)

        st.subheader("4. The Expected Credit Loss (ECL) Model — Three Stages")
        st.markdown("""
        IFRS 9 requires a **forward-looking** impairment model (replacing the old "incurred loss" model under IAS 39):

        | Stage | Credit Risk Change | ECL Measured | Interest Revenue |
        |---|---|---|---|
        | **Stage 1** | No significant increase since origination | 12-month ECL | Effective interest on gross carrying amount |
        | **Stage 2** | Significant increase in credit risk (but not credit-impaired) | Lifetime ECL | Effective interest on gross carrying amount |
        | **Stage 3** | Credit-impaired (objective evidence of default) | Lifetime ECL | Effective interest on NET carrying amount (after allowance) |

        **Simplified Approach** (mandatory for trade receivables/contract assets without significant financing component; optional for lease receivables):
        - Always measure at **lifetime ECL** — no need to track stage migration
        - Often uses a **provision matrix** based on historical loss rates by aging bucket

        **ECL Formula:**
        ```
        ECL = Probability of Default (PD) × Loss Given Default (LGD) × Exposure at Default (EAD)
        ```
        """)

        st.subheader("5. Derecognition")
        st.markdown("""
        **Financial Asset derecognition:** when contractual rights to cash flows expire, OR the asset is transferred and substantially all risks/rewards are transferred (or control is given up).

        **Financial Liability derecognition:** when the obligation is discharged, cancelled, or expires.

        **Modification of financial liabilities:**
        - Substantial modification (>10% change in PV of cash flows) → derecognise old liability, recognise new one
        - Non-substantial modification → adjust carrying amount, recognise gain/loss in P&L
        """)

        st.subheader("6. Hedge Accounting — Three Types")
        hedge_data = pd.DataFrame({
            "Hedge Type": ["Fair Value Hedge", "Cash Flow Hedge", "Net Investment Hedge"],
            "Risk Hedged": [
                "Exposure to changes in FV of recognised asset/liability or firm commitment",
                "Exposure to variability in cash flows of forecast transaction or recognised item",
                "FX exposure on a net investment in a foreign operation"
            ],
            "Accounting Treatment": [
                "Hedging instrument at FV through P&L; hedged item's carrying amount adjusted for the hedged risk (also through P&L) — gains/losses offset",
                "Effective portion of hedging instrument's gain/loss → OCI (cash flow hedge reserve); ineffective portion → P&L",
                "Effective portion → OCI (FX translation reserve); ineffective portion → P&L"
            ]
        })
        st.dataframe(hedge_data, use_container_width=True, hide_index=True)
        st.markdown("""
        **Hedge effectiveness requirements:**
        - Economic relationship between hedged item and hedging instrument
        - Credit risk does not dominate the value changes
        - Hedge ratio consistent with risk management strategy
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Classification — Business Model + SPPI Test")
        class_data = pd.DataFrame({
            "Instrument": [
                "Government bond held to collect coupons and principal",
                "Corporate bond portfolio managed to collect AND opportunistically sell",
                "Equity shares held for trading",
                "Loan with interest linked to borrower's revenue (not SPPI)",
                "Investment in unlisted equity, elected at FVOCI"
            ],
            "Business Model": ["Hold to collect", "Hold to collect and sell", "Trading", "N/A (fails SPPI)", "N/A (equity)"],
            "SPPI Test": ["Pass", "Pass", "N/A", "Fail", "N/A"],
            "Classification": ["Amortised Cost", "FVOCI (recycling)", "FVTPL", "FVTPL (mandatory)", "FVOCI (non-recycling, irrevocable election)"]
        })
        st.dataframe(class_data, use_container_width=True, hide_index=True)

        st.subheader("Example 2: 12-Month vs Lifetime ECL Calculation")
        st.markdown("""
        **Loan: $1,000,000 carrying amount**

        **Stage 1 (12-month ECL):**
        - PD (12-month) = 2%
        - LGD = 40%
        - EAD = $1,000,000
        - **ECL = 2% × 40% × $1,000,000 = $8,000**

        **Stage 2 (Lifetime ECL — credit risk has increased significantly):**
        - Lifetime PD = 15%
        - LGD = 40%
        - EAD = $1,000,000
        - **ECL = 15% × 40% × $1,000,000 = $60,000**

        Movement from Stage 1 to Stage 2 increases the loss allowance from $8,000 to $60,000 — a $52,000 additional impairment charge to P&L, even though no default has yet occurred.
        """)

        st.subheader("Example 3: Trade Receivables — Provision Matrix (Simplified Approach)")
        provision_matrix = pd.DataFrame({
            "Aging": ["Current", "1-30 days", "31-60 days", "61-90 days", ">90 days"],
            "Gross Amount ($)": [500000, 200000, 100000, 50000, 30000],
            "Loss Rate": ["1%", "3%", "10%", "30%", "60%"],
            "ECL Provision ($)": [5000, 6000, 10000, 15000, 18000]
        })
        st.dataframe(provision_matrix, use_container_width=True, hide_index=True)
        st.markdown("**Total ECL Provision = $5,000+$6,000+$10,000+$15,000+$18,000 = $54,000** (always lifetime ECL under simplified approach)")

        st.subheader("Example 4: Fair Value Hedge — Inventory Price Risk")
        st.markdown("""
        Entity holds inventory and enters a futures contract to hedge against price decline.

        | | Hedging Instrument (Futures) | Hedged Item (Inventory) |
        |---|---|---|
        | Fair value change | +$50,000 gain | ($48,000) loss |
        | Recognised in | P&L | P&L (carrying amount adjusted) |

        **Net P&L impact = $50,000 − $48,000 = $2,000 (ineffective portion)**

        Both gain and loss go through P&L, demonstrating the offsetting effect of an effective fair value hedge.
        """)

        st.subheader("Example 5: Cash Flow Hedge — Forecasted Foreign Currency Purchase")
        st.markdown("""
        Entity hedges a forecasted USD purchase in 6 months using a forward contract.

        - Forward contract fair value gain: $30,000 (fully effective)
        - **Entire gain → OCI (Cash Flow Hedge Reserve)**

        When the forecasted purchase occurs and inventory is recognised:
        - Reclassify the $30,000 from OCI → adjust the cost of inventory (basis adjustment)

        When inventory is later sold → flows through COGS in P&L.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Financial Asset Classifier")
        col1, col2 = st.columns(2)
        with col1:
            asset_class = st.selectbox("Asset type:", ["Debt instrument", "Equity instrument"])
            if asset_class == "Debt instrument":
                business_model = st.selectbox("Business model:", ["Hold to collect contractual cash flows", "Hold to collect and sell", "Other (e.g., trading)"])
                sppi_pass = st.checkbox("Passes SPPI test (cash flows = principal + interest only)?")
            else:
                fvoci_election = st.checkbox("Irrevocably elect FVOCI (non-recycling) at initial recognition?")
        with col2:
            if asset_class == "Debt instrument":
                if business_model == "Other (e.g., trading)":
                    st.error("📌 **FVTPL** — Trading business model")
                elif not sppi_pass:
                    st.error("📌 **FVTPL (mandatory)** — Fails SPPI test regardless of business model")
                elif business_model == "Hold to collect contractual cash flows":
                    st.success("📌 **AMORTISED COST**")
                else:
                    st.info("📌 **FVOCI (recycling)** — Hold to collect and sell + passes SPPI")
            else:
                if fvoci_election:
                    st.info("📌 **FVOCI (non-recycling)** — Irrevocable election; gains/losses never reclassified to P&L")
                else:
                    st.error("📌 **FVTPL** — Default classification for equity instruments")

        st.markdown("---")
        st.subheader("🔧 Tool 2: ECL Calculator")
        col1, col2 = st.columns(2)
        with col1:
            ead = st.number_input("Exposure at Default (EAD) ($)", value=1000000, step=10000)
            pd_12m = st.number_input("12-month Probability of Default (%)", value=2.0, step=0.5) / 100
            pd_lifetime = st.number_input("Lifetime Probability of Default (%)", value=15.0, step=0.5) / 100
            lgd = st.number_input("Loss Given Default (LGD) (%)", value=40.0, step=5.0) / 100
        with col2:
            stage = st.selectbox("Stage:", ["Stage 1 (12-month ECL)", "Stage 2 (Lifetime ECL)", "Stage 3 (Credit-impaired, Lifetime ECL)"])
            if "Stage 1" in stage:
                ecl = ead * pd_12m * lgd
                st.success(f"**12-month ECL = ${ead:,.0f} × {pd_12m*100:.1f}% × {lgd*100:.0f}% = ${ecl:,.0f}**")
            else:
                ecl = ead * pd_lifetime * lgd
                st.warning(f"**Lifetime ECL = ${ead:,.0f} × {pd_lifetime*100:.1f}% × {lgd*100:.0f}% = ${ecl:,.0f}**")
            if "Stage 3" in stage:
                st.info("Note: Interest revenue recognised on NET carrying amount (after deducting allowance) for Stage 3.")

        st.markdown("---")
        st.subheader("🔧 Tool 3: Provision Matrix Builder (Simplified Approach)")
        buckets_pm = ["Current", "1-30 days", "31-60 days", "61-90 days", ">90 days"]
        pm_rows = []
        for b in buckets_pm:
            c1, c2 = st.columns(2)
            amt = c1.number_input(f"{b} Amount ($)", value=200000, key=f"pm_a_{b}")
            rate = c2.number_input(f"{b} Loss Rate (%)", value=2.0, step=0.5, key=f"pm_r_{b}")
            pm_rows.append((b, amt, rate))
        if st.button("Calculate Total ECL Provision"):
            total_ecl_pm = sum([amt * rate / 100 for _, amt, rate in pm_rows])
            results_pm = pd.DataFrame({
                "Bucket": [r[0] for r in pm_rows],
                "Amount ($)": [f"{r[1]:,.0f}" for r in pm_rows],
                "Loss Rate": [f"{r[2]:.1f}%" for r in pm_rows],
                "ECL ($)": [f"{r[1]*r[2]/100:,.0f}" for r in pm_rows]
            })
            st.dataframe(results_pm, use_container_width=True, hide_index=True)
            st.success(f"**Total ECL Provision = ${total_ecl_pm:,.0f}**")

    with tab4:
        st.header("Visualizations")

        st.subheader("Three-Stage ECL Model")
        stages = ["Stage 1\n(12-month ECL)", "Stage 2\n(Lifetime ECL)", "Stage 3\n(Credit-impaired)"]
        ecl_amounts = [8000, 60000, 150000]
        colors_stage = ["#34D399", "#F59E0B", "#F87171"]
        fig = go.Figure(go.Bar(x=stages, y=ecl_amounts, marker_color=colors_stage))
        fig.update_layout(title="ECL Amount by Stage — Credit Risk Deterioration", yaxis_title="ECL Provision ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Financial Asset Classification Decision Tree")
        st.markdown("""
        ```
        Financial Asset
              |
        ┌─────┴──────┐
        Debt        Equity
        Instrument  Instrument
              |           |
        SPPI Test?   FVOCI Election?
        Pass / Fail   Yes / No
              |           |
        ┌─────┴────┐   ┌──┴────┐
        Business    FVTPL    FVOCI    FVTPL
        Model?    (mandatory) (non-     (default)
              |              recycling)
        ┌─────┴──────┐
        Hold to    Hold to     Other
        collect    collect &   (trading)
                   sell
           |            |          |
        Amortised    FVOCI      FVTPL
        Cost      (recycling)
        ```
        """)

        st.subheader("Hedge Accounting — Effect on P&L vs OCI")
        hedge_types = ["Fair Value Hedge", "Cash Flow Hedge", "Net Investment Hedge"]
        pl_pct = [100, 5, 5]
        oci_pct = [0, 95, 95]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=hedge_types, y=pl_pct, name="P&L (effective portion)", marker_color="#2563EB"))
        fig2.add_trace(go.Bar(x=hedge_types, y=oci_pct, name="OCI (effective portion)", marker_color="#10B981"))
        fig2.update_layout(barmode="stack", title="Hedge Accounting — Where Gains/Losses Are Recognised (Illustrative)", yaxis_title="% of Effective Gain/Loss", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. A debt instrument held to collect contractual cash flows and passing the SPPI test is classified at:**")
        q1 = st.radio("", ["FVTPL", "FVOCI (recycling)", "Amortised Cost", "FVOCI (non-recycling)"], key="ifrs9q1")
        if st.button("Check Answer", key="ifrs9c1"):
            if q1 == "Amortised Cost":
                st.success("✅ Correct! Hold-to-collect business model + passing SPPI test = Amortised Cost classification.")
            else:
                st.error("❌ Hold to collect + SPPI pass = AMORTISED COST.")

        st.markdown("---")
        st.markdown("**2. Equity instruments are classified by default at:**")
        q2 = st.radio("", ["Amortised Cost", "FVOCI (recycling)", "FVTPL", "Cost less impairment"], key="ifrs9q2")
        if st.button("Check Answer", key="ifrs9c2"):
            if q2 == "FVTPL":
                st.success("✅ Correct! Equity instruments default to FVTPL, UNLESS an irrevocable election is made at initial recognition for FVOCI (non-recycling).")
            else:
                st.error("❌ Equity instruments default classification = FVTPL (unless FVOCI election made).")

        st.markdown("---")
        st.markdown("**3. The simplified approach for trade receivables requires measuring ECL at:**")
        q3 = st.radio("", ["12-month ECL always", "Lifetime ECL always", "12-month or lifetime depending on credit risk stage", "No ECL is required for trade receivables"], key="ifrs9q3")
        if st.button("Check Answer", key="ifrs9c3"):
            if q3 == "Lifetime ECL always":
                st.success("✅ Correct! The simplified approach (mandatory for trade receivables without significant financing component) always uses LIFETIME ECL — no need to track stage migration.")
            else:
                st.error("❌ Simplified approach = LIFETIME ECL always, regardless of stage.")

        st.markdown("---")
        st.markdown("**4. For a financial liability designated at FVTPL, changes in fair value due to the entity's own credit risk are recognised in:**")
        q4 = st.radio("", ["P&L", "OCI", "Retained earnings directly", "Not recognised"], key="ifrs9q4")
        if st.button("Check Answer", key="ifrs9c4"):
            if q4 == "OCI":
                st.success("✅ Correct! Own credit risk changes on FVTPL-designated liabilities go to OCI — avoiding the counter-intuitive P&L gain when the entity's own credit quality deteriorates.")
            else:
                st.error("❌ Own credit risk on FVTPL liabilities → OCI (not P&L) — a specific IFRS 9 requirement.")

        st.markdown("---")
        st.markdown("**5. In a cash flow hedge, the effective portion of the hedging instrument's gain/loss is recognised in:**")
        q5 = st.radio("", ["P&L immediately", "OCI (cash flow hedge reserve)", "Retained earnings", "Goodwill"], key="ifrs9q5")
        if st.button("Check Answer", key="ifrs9c5"):
            if q5 == "OCI (cash flow hedge reserve)":
                st.success("✅ Correct! The effective portion goes to OCI (cash flow hedge reserve); the ineffective portion goes to P&L immediately.")
            else:
                st.error("❌ Cash flow hedge: effective portion → OCI; ineffective portion → P&L.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Classification — Debt Instruments
        | Business Model | SPPI Pass? | Classification |
        |---|---|---|
        | Hold to collect | Yes | Amortised Cost |
        | Hold to collect and sell | Yes | FVOCI (recycling) |
        | Other/Trading | N/A | FVTPL |
        | Any | No | FVTPL (mandatory) |

        ### 2. Classification — Equity Instruments
        - Default: **FVTPL**
        - Optional irrevocable election: **FVOCI (non-recycling)**

        ### 3. ECL Three-Stage Model
        ```
        Stage 1 (no significant ↑ credit risk) → 12-month ECL
        Stage 2 (significant ↑ credit risk)    → Lifetime ECL
        Stage 3 (credit-impaired)               → Lifetime ECL + interest on NET amount

        ECL = PD × LGD × EAD
        ```
        Simplified approach (trade receivables) → always Lifetime ECL

        ### 4. Hedge Accounting
        | Type | Effective Portion |
        |---|---|
        | Fair Value Hedge | P&L (both hedged item and instrument) |
        | Cash Flow Hedge | OCI |
        | Net Investment Hedge | OCI |

        ### 5. Own Credit Risk
        FVTPL-designated liabilities: own credit risk changes → **OCI** (not P&L)
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Classification = Business Model Test + SPPI Test (for debt)
Equity → FVTPL (default) or FVOCI non-recycling (election)
ECL = PD × LGD × EAD
Stage 1 → 12-month ECL | Stage 2 & 3 → Lifetime ECL
Simplified approach (trade receivables) → always Lifetime ECL
Cash flow hedge effective portion → OCI; ineffective → P&L
Own credit risk on FVTPL liabilities → OCI
        """)

        st.success("🎓 **IFRS 9 Complete!** You can now classify financial instruments, calculate ECL across all three stages, and apply hedge accounting principles.")
        st.info("💡 **Next**: IFRS 10 — Consolidated Financial Statements")

if __name__ == "__main__":
    show()