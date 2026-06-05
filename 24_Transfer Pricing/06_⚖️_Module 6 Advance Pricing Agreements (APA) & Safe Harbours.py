import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("🤝 Module 6: Advance Pricing Agreements (APA) & Safe Harbours")
    st.markdown("*Based on Sections 183–184, ITA 2023 & Income Tax Rules 2023*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Law", "🧮 Examples", "💡 Interactive Exercise",
        "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────────────────────
    with tab1:
        st.header("Theory & Legal Concepts")

        st.subheader("1. What is an Advance Pricing Agreement (APA)?")
        st.markdown("""
        An **Advance Pricing Agreement (APA)** is a binding agreement between a **taxpayer** and the 
        **National Board of Revenue (NBR)** that pre-determines the **transfer pricing method** and 
        **arm's length price/range** for specified international transactions **before they occur**.

        > *"The Board may enter into an agreement with a taxpayer to determine the arm's length price 
        > or the manner in which the arm's length price shall be determined in relation to an 
        > international transaction to be undertaken by such person."*  
        > — **Section 183, ITA 2023**

        #### Key Characteristics of an APA:
        - **Prospective** — covers future transactions (not past)
        - **Binding** — both NBR and taxpayer are bound by its terms
        - **Certainty** — eliminates TP uncertainty for covered transactions
        - **Time-limited** — valid for a specified period (typically **3–5 years**)
        - **Voluntary** — taxpayer applies; not mandatory
        """)

        st.subheader("2. Types of APAs under ITA 2023")
        st.markdown("""
        **Section 183** provides for three types:

        | Type | Parties | Description |
        |------|---------|-------------|
        | **Unilateral APA** | Taxpayer + NBR only | Only Bangladesh's view confirmed; risk of double taxation remains |
        | **Bilateral APA (BAPA)** | Taxpayer + NBR + foreign CA | Both countries agree; eliminates double taxation risk |
        | **Multilateral APA (MAPA)** | Taxpayer + NBR + 2+ foreign CAs | Multiple countries agree; used for complex global supply chains |

        > 💡 **Bilateral APAs** are the most beneficial as they bind both tax authorities and 
        > prevent double taxation entirely.
        """)

        st.subheader("3. APA Application Process")
        st.markdown("""
        **Step-by-Step APA Process under ITA 2023:**

        ```
        Step 1: Pre-filing consultation (informal meeting with NBR)
               → Discuss eligibility, transactions, method
        
        Step 2: Formal APA application
               → File with NBR's competent authority
               → Include: description of transactions, proposed method,
                 FAR analysis, comparables, financial projections
        
        Step 3: NBR review and due diligence
               → NBR may request additional information
               → Site visits and discussions
        
        Step 4: Negotiation (bilateral: NBR + foreign CA)
               → Competent authorities exchange positions
               → Agree on TP method and arm's length range
        
        Step 5: APA agreement signed
               → Valid for agreed period (3–5 years)
               → Annual compliance report required
        
        Step 6: Annual compliance reporting
               → Taxpayer files annual report confirming APA terms met
               → Transactions remain within agreed ALP range
        ```
        """)

        st.subheader("4. APA Coverage & Eligibility")
        st.markdown("""
        **Who can apply?**
        - Any taxpayer with **international transactions**
        - Particularly beneficial for high-value or complex transactions

        **What transactions can be covered?**
        - Sale/purchase of goods
        - Services (management, technical, shared services)
        - IP licensing and royalties
        - Intra-group financing (loans)
        - Cost contribution arrangements

        **Rollback provision:**  
        An APA can also be applied to **prior years** (rollback) — typically up to **4 preceding years** 
        — if the facts and circumstances were the same. This resolves pending TP disputes for prior years.

        **Duration:** Typically **3–5 years**, renewable.
        """)

        st.subheader("5. Safe Harbour Provisions")
        st.markdown("""
        **Section 184, ITA 2023** — Safe Harbours:

        A **safe harbour** is a set of **simplified rules** under which certain eligible taxpayers may 
        determine their ALP without going through a full comparability analysis, as long as their 
        transactions meet specified conditions.

        #### Benefits of Safe Harbour
        - **Administrative ease** — reduced compliance burden
        - **Certainty** — if within safe harbour, no TP adjustment
        - **Proportionate regulation** — appropriate for smaller/simpler transactions

        #### Types of Safe Harbours under Bangladesh ITA 2023:

        | Transaction Type | Safe Harbour Condition |
        |-----------------|----------------------|
        | **Intra-group loans** | Interest rate within ±1% of base rate (Bangladesh Bank rate / LIBOR equivalent) |
        | **Low-value-adding services** | Mark-up of 5% on costs (no benefit test required) |
        | **Commodity transactions** | Price matches publicly quoted commodity exchange price ±5% |
        | **Small taxpayers** | Aggregate transaction value < BDT 15 Crore: simplified documentation |
        | **IT / ITES services** | NCPM ≥ 15% (without detailed comparability analysis) |

        > ⚠️ *Safe harbour rules under Section 184 are still being progressively implemented by NBR. 
        > Taxpayers should check the latest SROs for applicable safe harbour rates.*
        """)

        st.subheader("6. APA vs Safe Harbour vs Full TP Study")
        st.markdown("""
        | Feature | Full TP Study | Safe Harbour | APA |
        |---------|--------------|--------------|-----|
        | Required for | All international transactions | Eligible simplified transactions | High-value/complex transactions |
        | Certainty level | Medium (audit risk remains) | High (within SH) | Highest (binding) |
        | Compliance cost | Medium | Low | High (upfront) |
        | Time to obtain | N/A | N/A | 12–24 months |
        | Duration | Annual | Annual (or per SRO) | 3–5 years |
        | Eliminates double tax | No | No | Yes (BAPA/MAPA) |
        | Retroactive application | No | No | Yes (rollback) |
        """)

    # ─────────────────────────────────────────────
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Unilateral APA for Management Services")
        st.markdown("""
        **Scenario:**  
        BankBD Ltd. pays USD 2 million/year in management fees to its UK parent. NBR has been scrutinising 
        this payment. BankBD applies for a **Unilateral APA**.

        **APA Agreement:**
        - Transaction: Management services fee
        - Method: TNMM (Operating Margin of the UK parent's service division)
        - Agreed range: 5%–8% of Bangladesh entity's revenue
        - Duration: 3 years (FY 2024–2026)

        **Outcome:**
        ✅ For 3 years, if management fees stay within 5%–8% of revenue, no TP audit/adjustment  
        ✅ Annual compliance report confirming fee within range  
        ⚠️ UK HMRC not bound — double taxation risk remains (use BAPA for full protection)
        """)

        st.subheader("Example 2: Bilateral APA — Garment Manufacturer")
        st.markdown("""
        **Scenario:**  
        Dhaka Garments Ltd. (Bangladesh) manufactures for its German parent.  
        Annual transaction: BDT 600 Crore. Both Germany and Bangladesh have been auditing the entity.

        **BAPA Process:**
        1. Dhaka Garments applies to NBR + simultaneously requests German competent authority
        2. NBR and German BZSt (Federal Central Tax Office) exchange positions
        3. **Agreed TP method:** Cost Plus Method
        4. **Agreed markup:** 10% ± 2% (range: 8%–12%)
        5. **Duration:** 5 years, with rollback to FY 2021–2023 (resolves pending audits)

        **Benefits:**
        ✅ No TP audit for 5 years  
        ✅ Pending audits resolved via rollback  
        ✅ Germany gives corresponding deduction to parent  
        ✅ **Zero double taxation**
        """)

        st.subheader("Example 3: Safe Harbour for Intra-Group Loan")
        st.markdown("""
        **Scenario:**  
        Telecom BD Ltd. borrows USD 10 million from its Singaporean parent at **SOFR + 2%**.  
        Bangladesh Bank base rate for similar loans: SOFR + 1.5%.  
        Safe harbour: interest rate within **±1% of base rate**.

        **Safe Harbour Analysis:**
        ```
        Base rate: SOFR + 1.5%
        Actual rate: SOFR + 2.0%
        Difference: +0.5%

        Safe harbour tolerance: ±1.0%
        0.5% is WITHIN the ±1% safe harbour band.
        ```
        ✅ **Safe harbour applies** — no detailed comparability analysis required.  
        ✅ No risk of TP adjustment on this loan for the year.
        """)

    # ─────────────────────────────────────────────
    with tab3:
        st.header("Interactive Exercise")

        st.subheader("🏦 APA Decision Tool")
        st.markdown("Assess whether an APA is appropriate for your situation:")

        txn_value = st.number_input("Annual transaction value (BDT Crore)", min_value=0.0, value=100.0)
        is_recurring = st.selectbox("Is this transaction recurring (multi-year)?", ["Yes", "No"])
        has_audit_history = st.selectbox("Has this transaction been audited before?", ["Yes", "No"])
        complexity = st.selectbox("Transaction complexity:", ["Simple (goods, routine services)", "Moderate (mixed)", "High (IP, integrated, loans)"])
        has_dta = st.selectbox("Does a DTA exist with the AE's country?", ["Yes", "No"])

        if st.button("Recommend APA Strategy"):
            score = 0
            reasons = []

            if txn_value >= 50:
                score += 2
                reasons.append(f"✅ High transaction value (BDT {txn_value:.0f} Cr) — justifies APA cost")
            if is_recurring == "Yes":
                score += 2
                reasons.append("✅ Recurring transaction — long-term certainty valuable")
            if has_audit_history == "Yes":
                score += 2
                reasons.append("✅ Prior audit history — APA prevents future disputes")
            if "High" in complexity:
                score += 2
                reasons.append("✅ High complexity — APA provides clearest framework")
            elif "Moderate" in complexity:
                score += 1
            if has_dta == "Yes":
                score += 1
                reasons.append("✅ DTA exists — Bilateral APA possible (full double-tax protection)")

            for r in reasons:
                st.markdown(r)

            if score >= 7:
                st.error("🔴 **Strong APA Candidate** — Strongly recommend applying for a Bilateral APA (BAPA). Complexity and value justify the investment.")
            elif score >= 4:
                st.warning("🟡 **Potential APA Candidate** — Consider Unilateral APA or enhanced TP documentation first. Evaluate cost-benefit.")
            else:
                st.success("🟢 **APA may not be cost-effective** — Maintain robust TP documentation and consider safe harbour rules if applicable.")

        st.markdown("---")
        st.subheader("📐 Safe Harbour Eligibility Checker")
        sh_type = st.selectbox("Transaction type:", [
            "Intra-group loan",
            "Low-value-adding services",
            "Commodity transaction",
            "IT/ITES services"
        ])

        if sh_type == "Intra-group loan":
            actual_rate = st.number_input("Actual interest rate (%)", min_value=0.0, value=7.0, step=0.25)
            base_rate = st.number_input("Base/market reference rate (%)", min_value=0.0, value=6.5, step=0.25)
            if st.button("Check Safe Harbour"):
                diff = abs(actual_rate - base_rate)
                if diff <= 1.0:
                    st.success(f"✅ Safe harbour applies! Rate difference ({diff:.2f}%) is within ±1% tolerance.")
                else:
                    st.error(f"❌ Safe harbour does NOT apply. Rate difference ({diff:.2f}%) exceeds ±1% tolerance. Full TP study required.")

        elif sh_type == "Low-value-adding services":
            actual_markup = st.number_input("Actual cost mark-up (%)", min_value=0.0, value=5.0, step=0.5)
            if st.button("Check Safe Harbour"):
                if actual_markup == 5.0:
                    st.success("✅ Safe harbour applies! 5% markup on costs is the OECD/Bangladesh safe harbour rate for LVAS.")
                elif 4.5 <= actual_markup <= 5.5:
                    st.warning("⚠️ Near safe harbour — check latest NBR SRO for exact tolerance.")
                else:
                    st.error(f"❌ Markup of {actual_markup}% does not meet the 5% LVAS safe harbour. Full TP analysis needed.")

        elif sh_type == "IT/ITES services":
            actual_ncpm = st.number_input("Actual NCPM (%)", min_value=0.0, value=15.0, step=0.5)
            if st.button("Check Safe Harbour"):
                if actual_ncpm >= 15.0:
                    st.success(f"✅ Safe harbour applies! NCPM of {actual_ncpm}% ≥ 15% safe harbour threshold for IT/ITES.")
                else:
                    st.error(f"❌ NCPM of {actual_ncpm}% is below 15% safe harbour. Full comparability analysis required.")

        elif sh_type == "Commodity transaction":
            quoted_price = st.number_input("Publicly quoted market price (BDT/unit)", min_value=0.0, value=1000.0)
            actual_price = st.number_input("Actual transaction price (BDT/unit)", min_value=0.0, value=1040.0)
            if st.button("Check Safe Harbour"):
                diff_pct = abs(actual_price - quoted_price) / quoted_price * 100
                if diff_pct <= 5.0:
                    st.success(f"✅ Safe harbour applies! Price deviation ({diff_pct:.1f}%) is within ±5% of quoted market price.")
                else:
                    st.error(f"❌ Price deviation ({diff_pct:.1f}%) exceeds ±5% commodity safe harbour. Full CUP analysis required.")

    # ─────────────────────────────────────────────
    with tab4:
        st.header("Quiz")

        st.markdown("**1. An Advance Pricing Agreement (APA) under Section 183 ITA 2023 is:**")
        q1 = st.radio("Select:", [
            "A retrospective settlement of past TP disputes",
            "A binding agreement pre-determining TP method for future transactions",
            "An exemption from transfer pricing rules",
            "A penalty waiver certificate"
        ], key="m6q1")
        if st.button("Check", key="m6c1"):
            if q1 == "A binding agreement pre-determining TP method for future transactions":
                st.success("✅ Correct! An APA is a prospective, binding agreement on TP methodology for future transactions.")
            else:
                st.error("❌ Incorrect. An APA is a binding, prospective agreement on TP method/price for future transactions.")

        st.markdown("---")
        st.markdown("**2. Which type of APA best eliminates the risk of double taxation?**")
        q2 = st.radio("Select:", ["Unilateral APA", "Bilateral APA", "Tax holiday", "Safe Harbour"], key="m6q2")
        if st.button("Check", key="m6c2"):
            if q2 == "Bilateral APA":
                st.success("✅ Correct! A Bilateral APA (BAPA) binds both countries' tax authorities, eliminating double taxation risk.")
            else:
                st.error("❌ Incorrect. A Bilateral APA, involving both countries' competent authorities, best eliminates double taxation.")

        st.markdown("---")
        st.markdown("**3. Safe harbour provisions under Section 184 ITA 2023 are designed to:**")
        q3 = st.radio("Select:", [
            "Allow any price to be used without documentation",
            "Provide simplified rules for eligible transactions to determine ALP without full comparability analysis",
            "Replace the arm's length principle entirely",
            "Apply only to domestic transactions"
        ], key="m6q3")
        if st.button("Check", key="m6c3"):
            if q3 == "Provide simplified rules for eligible transactions to determine ALP without full comparability analysis":
                st.success("✅ Correct! Safe harbours provide simplified compliance for eligible taxpayers/transactions.")
            else:
                st.error("❌ Incorrect. Safe harbours provide simplified rules to reduce compliance burden for eligible transactions.")

        st.markdown("---")
        st.markdown("**4. The 'rollback' feature of an APA allows:**")
        q4 = st.radio("Select:", [
            "Cancelling penalties from past years",
            "Applying the agreed APA terms to prior open years",
            "Extending the APA without negotiation",
            "Filing late tax returns"
        ], key="m6q4")
        if st.button("Check", key="m6c4"):
            if q4 == "Applying the agreed APA terms to prior open years":
                st.success("✅ Correct! APA rollback applies the agreed TP method to prior open years (typically up to 4 years back).")
            else:
                st.error("❌ Incorrect. Rollback means applying the APA's agreed terms to prior open assessment years.")

        st.markdown("---")
        st.markdown("**5. The safe harbour markup rate for 'low-value-adding intra-group services' under ITA 2023 is:**")
        q5 = st.radio("Select:", ["2%", "3%", "5%", "10%"], key="m6q5")
        if st.button("Check", key="m6c5"):
            if q5 == "5%":
                st.success("✅ Correct! The OECD-aligned and Bangladesh safe harbour rate for low-value-adding services is 5% markup on costs.")
            else:
                st.error("❌ Incorrect. The safe harbour markup for low-value-adding services is 5% (aligned with OECD guidelines).")

    # ─────────────────────────────────────────────
    with tab5:
        st.header("Module Summary")

        st.markdown("""
        ### 🎯 Key Takeaways

        | Item | Key Point |
        |------|-----------|
        | APA legal basis | Section 183, ITA 2023 |
        | Safe Harbour basis | Section 184, ITA 2023 |
        | APA types | Unilateral, Bilateral, Multilateral |
        | Best APA for double tax | Bilateral APA (BAPA) |
        | APA duration | 3–5 years (renewable) |
        | Rollback | Up to 4 prior open years |
        | LVAS safe harbour | 5% markup on costs |
        | IT/ITES safe harbour | NCPM ≥ 15% |
        | Intra-group loan SH | ±1% of base rate |
        | Commodity SH | ±5% of quoted market price |

        ### 🗺️ Complete Transfer Pricing Framework — Bangladesh

        ```
        TRANSFER PRICING IN BANGLADESH (ITA 2023)
        ├── Who is covered? (S.175–176)
        │   ├── Associated Enterprises (≥26% ownership, etc.)
        │   └── International Transactions
        ├── Arm's Length Principle (S.177)
        │   └── Comparability Analysis (Rule 69)
        ├── TP Methods (S.178–179)
        │   ├── CUP, RPM, CPM, PSM, TNMM
        │   └── Most Appropriate Method
        ├── Documentation (S.180 / Rule 77–78)
        │   ├── Master File
        │   ├── Local File
        │   └── CbCR (≥ BDT 3,000 Crore)
        ├── Audit & Penalties (S.181–182)
        │   ├── TPO assessment
        │   ├── 2% penalty (no docs)
        │   └── 15% additional tax on adjustment
        ├── Dispute Resolution (S.185)
        │   ├── Commissioner (Appeals)
        │   ├── Appellate Tribunal
        │   └── MAP (DTA countries)
        └── Proactive Compliance (S.183–184)
            ├── Advance Pricing Agreement (APA)
            └── Safe Harbours
        ```

        ### ✅ Best Practice TP Compliance Calendar
        | Action | Timing |
        |--------|--------|
        | Review/update intercompany agreements | Start of fiscal year |
        | Conduct benchmarking analysis | During the year |
        | Prepare Local File | Before year-end / tax return filing |
        | File tax return with TP disclosures | As per income tax deadline |
        | Annual APA compliance report | If APA in place |
        | CbCR filing | 12 months after fiscal year end |
        """)

        st.success("🎓 **Module 6 Complete! Transfer Pricing in Bangladesh — Full Course Completed!**")
        st.balloons()
        st.info("""
        📚 **Congratulations!** You have completed all 6 modules of Transfer Pricing in Bangladesh.
        
        **Modules Covered:**
        1. Introduction & Legal Framework
        2. Arm's Length Principle & Comparability Analysis
        3. Transfer Pricing Methods
        4. Documentation & Compliance
        5. Audit, Penalties & Dispute Resolution
        6. Advance Pricing Agreements & Safe Harbours
        """)

if __name__ == "__main__":
    show()