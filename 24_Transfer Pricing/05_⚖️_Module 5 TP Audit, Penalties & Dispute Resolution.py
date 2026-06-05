import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("🔍 Module 5: Transfer Pricing Audit, Penalties & Dispute Resolution")
    st.markdown("*Based on Sections 181–182 & 185, ITA 2023*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Law", "🧮 Examples", "💡 Interactive Exercise",
        "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────────────────────
    with tab1:
        st.header("Theory & Legal Concepts")

        st.subheader("1. Transfer Pricing Audit Framework")
        st.markdown("""
        **Section 181, ITA 2023** empowers the **Transfer Pricing Officer (TPO)** to:

        - Review the TP study submitted by the taxpayer
        - Scrutinise all international transactions and specified domestic transactions
        - Call for additional information, documents and explanations
        - Conduct a detailed audit of the taxpayer's affairs
        - Determine the arm's length price independently
        - Pass a **TP order** with proposed adjustments

        #### Who is the Transfer Pricing Officer (TPO)?
        The Commissioner of Taxes or any officer authorised by NBR, designated specifically 
        to examine transfer pricing matters. The TPO operates alongside but separately from the 
        regular assessing officer.
        """)

        st.subheader("2. TP Audit Trigger Factors")
        st.markdown("""
        NBR typically initiates TP audits based on:

        | Risk Factor | Description |
        |-------------|-------------|
        | High-value transactions | Large international transaction values |
        | Persistent losses | Entity shows losses year after year despite group profitability |
        | Low margins | Significantly below industry benchmarks |
        | Related-party revenue dependence | Most revenue/costs from AEs |
        | Payment of large management fees | Without clear service documentation |
        | Royalty/IP payments | Payments to low-tax jurisdictions |
        | Debt-laden structure | High intra-group loans with above-market interest |
        | Missing/inadequate documentation | No TP study or outdated comparables |
        | Sector focus | Garments, pharma, telecom, banking — NBR priority sectors |
        """)

        st.subheader("3. TP Adjustment Mechanism")
        st.markdown("""
        When the TPO determines that the transfer price is not arm's length:

        **Step 1:** TPO determines the ALP using appropriate method  
        **Step 2:** Compare with the price actually used in the transaction  
        **Step 3:** If difference exists → **upward adjustment** to taxable income  
        **Step 4:** Issue a draft TP assessment order  
        **Step 5:** Taxpayer given opportunity to be heard  
        **Step 6:** Final TP order issued  

        > ⚠️ Under ITA 2023, adjustments are **only upward** — NBR does not make downward adjustments 
        > (i.e., the taxpayer cannot benefit from TP adjustment if they over-charged).

        #### Corresponding Adjustment
        When NBR makes a TP adjustment for Bangladesh, the associated enterprise in the other country 
        may request a **corresponding adjustment** to avoid double taxation — handled via the 
        **Mutual Agreement Procedure (MAP)** under tax treaties.
        """)

        st.subheader("4. Penalties under ITA 2023")
        st.markdown("""
        **Section 182, ITA 2023** prescribes the following penalties:

        | Violation | Penalty |
        |-----------|---------|
        | **Failure to maintain documentation** | 2% of the value of international transactions |
        | **Failure to report transactions** in tax return | 2% of transaction value |
        | **Failure to furnish documentation** within 30 days of notice | 2% of transaction value |
        | **Concealment / misrepresentation** | 100%–300% of tax on understated income |
        | **Understatement of income** due to TP | Additional tax @ 15% of income adjustment |

        > 🔑 **Key principle:** If the taxpayer maintains documentation in good faith and applies 
        > a recognised method, penalties for documentation failure may be waived even if the TP 
        > price is later adjusted.

        #### Minimum Penalty Protection
        If a taxpayer:
        ✅ Maintained contemporaneous documentation  
        ✅ Disclosed all transactions in the return  
        ✅ Applied a recognised TP method  
        → **Documentation penalties may be waived** by NBR.
        """)

        st.subheader("5. Dispute Resolution Options")
        st.markdown("""
        #### Option 1: Objection to Commissioner (Appeals)
        - File objection against TPO's assessment order
        - Before the Commissioner of Taxes (Appeals)
        - Deadline: **45 days** from receipt of order

        #### Option 2: Appellate Tribunal
        - Appeal against the Commissioner (Appeals) order
        - Before the Taxes Appellate Tribunal
        - Independent quasi-judicial body

        #### Option 3: High Court / Supreme Court
        - Further appeal on **legal/constitutional grounds only**
        - Questions of law, not fact

        #### Option 4: Mutual Agreement Procedure (MAP)
        - **Section 185, ITA 2023**
        - Available where Bangladesh has a **Double Tax Agreement (DTA)** with the AE's country
        - Competent authorities of both countries negotiate to resolve double taxation
        - Countries with Bangladesh DTAs: India, UK, USA, Singapore, Malaysia, UAE, China, Japan, etc.

        #### Option 5: Advance Pricing Agreement (APA)
        - **Pre-emptive resolution** — agree the TP method in advance with NBR
        - Covered in Module 6
        """)

        st.subheader("6. Double Tax Relief")
        st.markdown("""
        When a TP adjustment results in **double taxation** (same income taxed in two countries):

        **Relief mechanisms:**
        1. **Corresponding adjustment** — the other country reduces tax on its entity
        2. **MAP** — competent authorities resolve the dispute bilaterally
        3. **Unilateral relief** — foreign tax credit in Bangladesh return

        Bangladesh has DTAs with **35+ countries** providing MAP provisions. Key treaty partners:
        India, UK, Singapore, USA, Malaysia, South Korea, Japan, UAE, China, Sweden, Norway, etc.
        """)

    # ─────────────────────────────────────────────
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: TP Audit and Adjustment")
        st.markdown("""
        **Scenario:**  
        TechServe BD Ltd. provides IT services to its Singapore parent.  
        During an audit, NBR finds:
        - Actual NCPM charged: 3%
        - ALP (IQR median): 11%
        - Total costs of TechServe BD: BDT 50 Crore

        **TP Adjustment Calculation:**
        ```
        Actual income = 50 Crore × 3% = BDT 1.5 Crore
        ALP income    = 50 Crore × 11% = BDT 5.5 Crore
        ─────────────────────────────────────────────
        TP Adjustment = BDT 5.5 Cr − BDT 1.5 Cr = BDT 4.0 Crore
        
        Tax impact (at 27.5% corporate rate):
        = BDT 4.0 Crore × 27.5% = BDT 1.1 Crore
        
        Additional tax @ 15% on adjustment:
        = BDT 4.0 Crore × 15% = BDT 0.6 Crore
        ─────────────────────────────────────────────
        Total liability = BDT 1.7 Crore
        ```
        """)

        st.subheader("Example 2: Documentation Penalty Calculation")
        st.markdown("""
        **Scenario:**  
        Pharma BD Ltd. fails to maintain TP documentation for international transactions worth BDT 200 Crore.

        **Penalty Calculation (Section 182):**
        ```
        Penalty rate = 2% of transaction value
        Penalty      = BDT 200 Crore × 2% = BDT 4 Crore
        ```

        ⚠️ If Pharma BD had maintained documentation:
        - Penalty = Nil (good faith protection applies)
        - Even if TP adjustment made, documentation penalty waived

        **Lesson:** Cost of preparing TP documentation (BDT 10–50 lakh typical) << Cost of penalty (BDT 4 Crore).
        """)

        st.subheader("Example 3: MAP Procedure")
        st.markdown("""
        **Scenario:**  
        NBR makes a BDT 30 Crore TP adjustment to the income of Garments BD Ltd.  
        The corresponding UK parent (Global Apparel UK) has already paid UK tax on the same amount.

        **MAP Process:**
        1. Garments BD files MAP request with NBR's competent authority within **3 years** of assessment
        2. NBR's competent authority contacts UK HMRC under Bangladesh-UK DTA
        3. Both competent authorities negotiate: either Bangladesh reduces adjustment OR UK gives credit
        4. Resolution reached → double taxation eliminated
        5. If no resolution → **arbitration** may be available under certain DTAs

        ✅ Key benefit: Prevents the same BDT 30 Crore from being taxed twice (in Bangladesh AND UK).
        """)

    # ─────────────────────────────────────────────
    with tab3:
        st.header("Interactive Exercise")

        st.subheader("💰 TP Adjustment & Penalty Calculator")

        total_costs = st.number_input("Tested party total costs (BDT Crore)", min_value=0.0, value=100.0, step=5.0)
        actual_ncpm = st.number_input("Actual NCPM (%)", min_value=0.0, value=3.0, step=0.5)
        alp_ncpm = st.number_input("ALP NCPM / Median (%)", min_value=0.0, value=11.0, step=0.5)
        corp_tax_rate = st.number_input("Corporate tax rate (%)", min_value=0.0, value=27.5, step=0.5)
        has_documentation = st.selectbox("Did taxpayer maintain contemporaneous TP documentation?", ["Yes", "No"])
        txn_value = st.number_input("Total international transaction value for penalty (BDT Crore)", min_value=0.0, value=100.0, step=5.0)

        if st.button("Calculate TP Exposure"):
            actual_profit = total_costs * actual_ncpm / 100
            alp_profit = total_costs * alp_ncpm / 100
            adjustment = max(0, alp_profit - actual_profit)

            tax_on_adj = adjustment * corp_tax_rate / 100
            surcharge = adjustment * 15 / 100
            total_tax = tax_on_adj + surcharge

            doc_penalty = 0 if has_documentation == "Yes" else txn_value * 2 / 100

            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            col1.metric("TP Adjustment (BDT Crore)", f"{adjustment:.2f}")
            col2.metric("Corporate Tax on Adjustment", f"{tax_on_adj:.2f} Cr")
            col3.metric("15% Surcharge", f"{surcharge:.2f} Cr")

            st.metric("Total Tax Liability (BDT Crore)", f"{total_tax:.2f}")
            if doc_penalty > 0:
                st.error(f"📌 Documentation Penalty: BDT {doc_penalty:.2f} Crore (2% of transaction value)")
                st.error(f"📌 TOTAL EXPOSURE (Tax + Penalty): BDT {total_tax + doc_penalty:.2f} Crore")
            else:
                st.success("✅ No documentation penalty — taxpayer maintained contemporaneous documentation.")
                st.success(f"📌 TOTAL TAX LIABILITY: BDT {total_tax:.2f} Crore")

            fig = go.Figure(go.Bar(
                x=["Actual Profit", "ALP Profit", "Adjustment"],
                y=[actual_profit, alp_profit, adjustment],
                marker_color=["steelblue", "orange", "crimson"]
            ))
            fig.update_layout(title="Profit vs ALP vs Adjustment (BDT Crore)",
                               yaxis_title="BDT Crore", height=350)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader("📋 Dispute Resolution Path Selector")
        outcome = st.selectbox("What is your situation?", [
            "TPO has issued an assessment order I disagree with",
            "Assessment confirmed but I suspect double taxation",
            "I want to avoid dispute before filing",
            "I missed the documentation deadline"
        ])

        if st.button("Show Recommended Path"):
            if outcome == "TPO has issued an assessment order I disagree with":
                st.info("""
                **Recommended Path:**
                1. File objection with Commissioner of Taxes (Appeals) — within **45 days**
                2. If unsuccessful → appeal to Taxes Appellate Tribunal
                3. If unsuccessful → High Court (on points of law only)
                4. Simultaneously consider MAP if a DTA exists with the AE's country
                """)
            elif outcome == "Assessment confirmed but I suspect double taxation":
                st.info("""
                **Recommended Path:**
                1. File MAP request with NBR's competent authority — within **3 years** of assessment
                2. NBR negotiates with foreign competent authority under applicable DTA
                3. Consider APA for future years to prevent recurrence
                """)
            elif outcome == "I want to avoid dispute before filing":
                st.success("""
                **Recommended Path:**
                1. Prepare contemporaneous TP documentation (Local File + Master File)
                2. Consider filing for an **Advance Pricing Agreement (APA)** with NBR
                3. Conduct annual TP health-check before filing
                4. Ensure intercompany agreements are in place
                """)
            elif outcome == "I missed the documentation deadline":
                st.warning("""
                **Recommended Path:**
                1. Prepare documentation **immediately** — minimise delay
                2. Submit proactively to NBR with explanation
                3. 2% penalty on transaction value is likely unavoidable
                4. Good-faith cooperation may reduce penalties
                5. Engage a TP specialist immediately
                """)

    # ─────────────────────────────────────────────
    with tab4:
        st.header("Quiz")

        st.markdown("**1. Under Section 182 ITA 2023, the penalty for failure to maintain TP documentation is:**")
        q1 = st.radio("Select:", ["1% of transaction value", "2% of transaction value", "5% of transaction value", "BDT 50 Lakh flat"], key="m5q1")
        if st.button("Check", key="m5c1"):
            if q1 == "2% of transaction value":
                st.success("✅ Correct! Section 182 imposes a penalty of 2% of the value of international transactions.")
            else:
                st.error("❌ Incorrect. The penalty is 2% of the value of international transactions.")

        st.markdown("---")
        st.markdown("**2. Under ITA 2023, TP adjustments by NBR are:**")
        q2 = st.radio("Select:", [
            "Both upward and downward",
            "Only downward",
            "Only upward",
            "Either, depending on the method used"
        ], key="m5q2")
        if st.button("Check", key="m5c2"):
            if q2 == "Only upward":
                st.success("✅ Correct! ITA 2023 allows only upward adjustments — NBR adds to taxable income, not reduces it.")
            else:
                st.error("❌ Incorrect. Under ITA 2023, only upward adjustments are permitted by NBR.")

        st.markdown("---")
        st.markdown("**3. The Mutual Agreement Procedure (MAP) is available under:**")
        q3 = st.radio("Select:", [
            "All Bangladesh tax cases",
            "Only cases with documented TP study",
            "Cases involving double taxation where a DTA exists",
            "Cases involving domestic transactions"
        ], key="m5q3")
        if st.button("Check", key="m5c3"):
            if q3 == "Cases involving double taxation where a DTA exists":
                st.success("✅ Correct! MAP under Section 185 is available where Bangladesh has a DTA with the relevant country.")
            else:
                st.error("❌ Incorrect. MAP is available where a DTA (Double Tax Agreement) exists between the countries.")

        st.markdown("---")
        st.markdown("**4. What is the deadline to file an objection against a TPO order with the Commissioner of Taxes (Appeals)?**")
        q4 = st.radio("Select:", ["15 days", "30 days", "45 days", "90 days"], key="m5q4")
        if st.button("Check", key="m5c4"):
            if q4 == "45 days":
                st.success("✅ Correct! An objection against a TP assessment order must be filed within 45 days.")
            else:
                st.error("❌ Incorrect. The deadline for objection is 45 days from receipt of the assessment order.")

        st.markdown("---")
        st.markdown("**5. Which additional tax rate applies on TP adjustments under ITA 2023?**")
        q5 = st.radio("Select:", ["5%", "10%", "15%", "20%"], key="m5q5")
        if st.button("Check", key="m5c5"):
            if q5 == "15%":
                st.success("✅ Correct! Section 182 imposes an additional 15% tax on the amount of TP income adjustment.")
            else:
                st.error("❌ Incorrect. The additional tax rate on TP adjustments is 15% under Section 182, ITA 2023.")

    # ─────────────────────────────────────────────
    with tab5:
        st.header("Module Summary")

        st.markdown("""
        ### 🎯 Key Takeaways

        | Item | Key Provision |
        |------|--------------|
        | TPO powers | Section 181, ITA 2023 |
        | Penalty — no documentation | 2% of transaction value |
        | Penalty — no filing | 2% of transaction value |
        | Additional tax on TP adjustment | 15% of adjustment |
        | Concealment/misrepresentation | 100%–300% of tax understated |
        | Objection deadline | 45 days from assessment order |
        | MAP provision | Section 185, ITA 2023 |
        | MAP deadline | Within 3 years of assessment |

        ### 📊 TP Audit Risk Indicators
        ```
        🔴 High Risk:
           - Persistent losses in BD entity
           - Large management fee payments
           - All revenue from AEs
           - No documentation
        
        🟡 Medium Risk:
           - Margins below industry average
           - High royalty payments
           - One-sided transactions
        
        🟢 Low Risk:
           - Contemporaneous documentation
           - Margins within ALP range
           - APA in place
        ```

        ### 🛡️ Penalty Protection Strategy
        1. Maintain **contemporaneous** documentation (before filing)
        2. Apply a **recognised TP method** (one of the 6 under ITA 2023)
        3. Disclose **all transactions** in the tax return
        4. Respond to NBR notices **within 30 days**
        5. Consider **APA** for high-value or recurring transactions
        """)

        st.success("🎓 **Module 5 Complete!** You now understand TP audits, penalties and dispute resolution in Bangladesh.")
        st.info("💡 **Next**: Proceed to Module 6 — Advance Pricing Agreements (APA) & Safe Harbours.")

if __name__ == "__main__":
    show()