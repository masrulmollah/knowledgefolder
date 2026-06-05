import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import date

def show():
    st.title("📁 Module 4: Transfer Pricing Documentation & Compliance")
    st.markdown("*Based on Section 180, ITA 2023 & Rules 77–78, Income Tax Rules 2023*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Law", "🧮 Examples", "💡 Interactive Exercise",
        "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────────────────────
    with tab1:
        st.header("Theory & Legal Concepts")

        st.subheader("1. Why TP Documentation Matters")
        st.markdown("""
        Transfer pricing documentation serves two critical purposes:

        1. **Compliance:** Demonstrates that transactions are priced at arm's length
        2. **Penalty protection:** Good-faith, contemporaneous documentation protects against penalties

        Under ITA 2023, taxpayers with international transactions must maintain documentation 
        **before filing** their tax return — it must be **contemporaneous** (prepared at the time of transaction).
        """)

        st.subheader("2. Who Must Maintain TP Documentation?")
        st.markdown("""
        **Section 180, ITA 2023** — Documentation is required for:

        | Category | Threshold |
        |----------|-----------|
        | International transactions (goods, services, IP, loans) | **Any value** (no de minimis) |
        | Specified domestic transactions | **≥ BDT 30 Crore** in aggregate |
        | Permanent Establishment transactions | **Any value** |

        > ⚠️ Unlike some countries, Bangladesh does **not** have a general de minimis threshold for 
        > international transactions — all international transactions between associated enterprises require 
        > documentation under ITA 2023.
        """)

        st.subheader("3. Three-Tiered Documentation Framework")
        st.markdown("""
        Bangladesh has adopted the **OECD BEPS Action 13** three-tier documentation structure under ITA 2023:

        #### Tier 1: Master File (MF)
        **Group-level information** about the MNE group:
        - Organisational structure of the MNE group
        - Description of business: key value drivers, main geographies
        - Intangibles owned by the group, R&D policy
        - Intercompany financial activities (financing, treasury)
        - Consolidated financial statements
        - APAs and tax rulings

        #### Tier 2: Local File (LF)
        **Entity-level information** specific to the Bangladeshi taxpayer:
        - Description of management structure and organisation chart
        - List of all international transactions with associated enterprises
        - Financial information of the entity
        - For each transaction:
          - Amount and nature
          - Method selected and why (MAM analysis)
          - Comparability analysis (FAR analysis)
          - Comparables used and adjustments made
          - ALP determination

        #### Tier 3: Country-by-Country Report (CbCR)
        **Group-wide, country-level financial data:**
        - Filed by the **Ultimate Parent Entity (UPE)** or a surrogate entity
        - Required for MNE groups with **consolidated group revenue ≥ BDT 3,000 Crore** (approx. USD 275M)
        - Contains: Revenue, profit before tax, tax paid, employees, assets per country
        """)

        st.subheader("4. Specific Documentation Requirements (Rule 77)")
        st.markdown("""
        The **Local File** must contain at minimum:

        **A. Entity Information**
        - Name, address, TIN of the taxpayer
        - Nature of business, products/services
        - Organisational chart

        **B. Associated Enterprise Details**
        - List of all AEs with relationship description
        - Countries of residence of AEs

        **C. Transaction-wise Information (for each transaction type)**
        - Description and nature of transaction
        - Amount in BDT
        - Method used (MAM) and justification
        - Comparables used: internal/external
        - ALP determination (price or margin)
        - Any adjustments made

        **D. Supporting Documents**
        - Intercompany agreements (contracts, MSAs, TSAs)
        - Price lists, invoices
        - Relevant industry information
        - Financial statements
        - Database search results (Orbis, Prowess, etc.)
        """)

        st.subheader("5. Filing & Submission Requirements")
        st.markdown("""
        | Requirement | Deadline |
        |-------------|----------|
        | Maintain documentation | Before filing tax return |
        | Report TP transactions | In income tax return (Form IT-11GA) |
        | Submit TP study on request | Within **30 days** of NBR notice |
        | CbCR filing | **12 months** after the close of the reporting fiscal year |

        > 📌 The documentation does **not** need to be filed with the tax return.  
        > It must be **available and ready** to submit within **30 days** when NBR requests it.
        """)

        st.subheader("6. Intercompany Agreements")
        st.markdown("""
        A key documentation requirement under ITA 2023 is that **intercompany agreements** must exist 
        and be **consistent with** the transfer pricing policies applied:

        **Common agreements in Bangladesh:**
        - **Sales/Purchase Agreements** — for goods transactions
        - **Management Services Agreements (MSA)** — for management/technical fees
        - **Technology Services Agreements (TSA)** — for IT services
        - **Licence Agreements** — for IP/trademark/brand royalties
        - **Loan Agreements** — for intra-group financing
        - **Cost Sharing Agreements (CSA)** — for shared services/R&D

        > ⚠️ *Transactions without supporting intercompany agreements are a major red flag 
        > in NBR audits.*
        """)

    # ─────────────────────────────────────────────
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Three-Tier Documentation — Who Files What?")
        st.markdown("""
        **Scenario:**  
        Global Apparel Group (UK) has consolidated revenue of BDT 5,000 Crore.  
        Its Bangladesh subsidiary, Garments BD Ltd., has international transactions with the group.

        | Document | Filed By | Content |
        |----------|----------|---------|
        | **Master File** | Global Apparel Group (UK) prepared; BD entity holds copy | Group structure, intangibles, global TP policies |
        | **Local File** | Garments BD Ltd. (Bangladesh) | BD entity's transactions, FAR analysis, ALP determination |
        | **CbCR** | Global Apparel Group UK (UPE) files in UK; shared with NBR via exchange | Revenue, profit, tax, employees per country |

        ✅ All three tiers required as group revenue (BDT 5,000 Crore) exceeds CbCR threshold (BDT 3,000 Crore).
        """)

        st.subheader("Example 2: Contents of a Local File — Step by Step")
        with st.expander("Click to see a sample Local File structure"):
            st.markdown("""
            **Garments BD Ltd. — Transfer Pricing Local File FY 2023-24**

            **Section 1: Entity Overview**
            - Name: Garments BD Ltd., TIN: 123-456-789
            - Business: Contract garment manufacturing
            - Org. chart: Reports to Global Apparel Group UK

            **Section 2: Associated Enterprises**
            | AE Name | Country | Relationship | Transaction Type |
            |---------|---------|--------------|-----------------|
            | Global Apparel UK | UK | Parent (100%) | Sale of finished goods |
            | Apparel Logistics SG | Singapore | Sister (common parent) | Freight/logistics services |

            **Section 3: Transaction Analysis — Sale of Garments to Global Apparel UK**
            - Transaction value: BDT 450 Crore
            - Method: Cost Plus Method
            - FAR: Contract manufacturer — limited functions, minimal risk
            - Comparables: 8 comparable contract manufacturers (Orbis database)
            - ALP markup range: 8%–12% (IQR); Median: 10%
            - Actual markup: 9.5% ✅ Within range — no adjustment required

            **Section 4: Supporting Documents**
            - Manufacturing agreement dated 01 April 2023
            - Price lists and invoices
            - Orbis comparable search documentation
            """)

        st.subheader("Example 3: CbCR Threshold Check")
        st.markdown("""
        **Scenarios:**

        | Company | Group Revenue (BDT Crore) | CbCR Required? |
        |---------|--------------------------|---------------|
        | Alpha MNC Group | 5,000 | ✅ Yes (> BDT 3,000 Cr) |
        | Beta SME Group | 1,500 | ❌ No (< BDT 3,000 Cr) |
        | Gamma Group | 3,000 | ✅ Yes (= BDT 3,000 Cr) |
        | Delta Startup Group | 200 | ❌ No |

        > Note: Even if CbCR is not required, **Master File and Local File** are still required 
        > for all international transactions.
        """)

    # ─────────────────────────────────────────────
    with tab3:
        st.header("Interactive Exercise")

        st.subheader("📋 TP Documentation Checklist Generator")
        st.markdown("Complete this checklist to assess your documentation readiness:")

        st.markdown("**Entity & Transactions:**")
        has_ae_list = st.checkbox("List of all associated enterprises with relationship description")
        has_txn_list = st.checkbox("List of all international transactions with values (BDT)")
        has_agreements = st.checkbox("Intercompany agreements for each transaction type")
        has_invoices = st.checkbox("Invoices and price lists supporting transaction values")

        st.markdown("**TP Analysis:**")
        has_far = st.checkbox("FAR analysis (Functions, Assets, Risks) for each transaction")
        has_method = st.checkbox("Most Appropriate Method (MAM) selection and justification")
        has_comparables = st.checkbox("Comparability analysis with search documentation")
        has_alp = st.checkbox("ALP determination and arm's length range calculation")
        has_adjustments = st.checkbox("Comparability adjustments documented and explained")

        st.markdown("**Financial Information:**")
        has_financials = st.checkbox("Entity financial statements (P&L, Balance Sheet)")
        has_seg_data = st.checkbox("Segmented financial data by transaction type (if applicable)")

        st.markdown("**Group Documents (Master File):**")
        has_group_structure = st.checkbox("MNE group organisation chart")
        has_global_tp = st.checkbox("Global TP policies and value chain description")
        has_intangibles = st.checkbox("Group intangibles description and ownership")

        if st.button("Generate Readiness Report"):
            items = [has_ae_list, has_txn_list, has_agreements, has_invoices,
                     has_far, has_method, has_comparables, has_alp, has_adjustments,
                     has_financials, has_seg_data, has_group_structure, has_global_tp, has_intangibles]
            score = sum(items)
            total = len(items)
            pct = score / total * 100

            st.markdown(f"### Documentation Score: {score}/{total} ({pct:.0f}%)")
            if pct >= 85:
                st.success("✅ Excellent! Your documentation appears comprehensive. Maintain contemporaneously.")
            elif pct >= 60:
                st.warning("⚠️ Moderate. Key gaps exist — address before tax return filing or NBR audit.")
            else:
                st.error("❌ Significant gaps. High penalty risk. Immediately prepare missing documentation.")

            missing = []
            labels = ["AE list", "Transaction list", "Intercompany agreements", "Invoices",
                      "FAR analysis", "MAM justification", "Comparability analysis", "ALP determination",
                      "Adjustments", "Financial statements", "Segmented financials",
                      "Group structure", "Global TP policy", "Intangibles description"]
            for i, item in enumerate(items):
                if not item:
                    missing.append(labels[i])
            if missing:
                st.markdown("**Missing items:**")
                for m in missing:
                    st.markdown(f"- ❌ {m}")

        st.markdown("---")
        st.subheader("📅 CbCR Obligation Checker")
        group_revenue = st.number_input("MNE Group Consolidated Revenue (BDT Crore)", min_value=0.0, value=2000.0, step=100.0)
        has_bd_sub = st.selectbox("Does the group have a Bangladesh entity?", ["Yes", "No"])
        if st.button("Check CbCR Obligation"):
            if has_bd_sub == "Yes" and group_revenue >= 3000:
                st.error(f"🔴 **CbCR Required!** Group revenue BDT {group_revenue:,.0f} Crore ≥ threshold of BDT 3,000 Crore.")
                st.markdown("Filing deadline: 12 months after the reporting fiscal year end.")
            elif has_bd_sub == "Yes" and group_revenue < 3000:
                st.success(f"🟢 CbCR NOT required. Revenue BDT {group_revenue:,.0f} Crore < BDT 3,000 Crore threshold.")
                st.markdown("Master File and Local File are still required.")
            else:
                st.info("No Bangladesh entity — no Bangladesh CbCR obligation.")

    # ─────────────────────────────────────────────
    with tab4:
        st.header("Quiz")

        st.markdown("**1. Under ITA 2023, when must TP documentation be prepared?**")
        q1 = st.radio("Select:", [
            "Within 30 days after NBR notice",
            "Within 1 year of filing the return",
            "Contemporaneously — before or at time of filing the tax return",
            "Only when an audit is initiated"
        ], key="m4q1")
        if st.button("Check", key="m4c1"):
            if q1 == "Contemporaneously — before or at time of filing the tax return":
                st.success("✅ Correct! Documentation must be contemporaneous — prepared before or at the time of filing.")
            else:
                st.error("❌ Incorrect. TP documentation must be contemporaneous (prepared before/at filing).")

        st.markdown("---")
        st.markdown("**2. What is the CbCR threshold for MNE groups under Bangladesh ITA 2023?**")
        q2 = st.radio("Select:", ["BDT 1,000 Crore", "BDT 2,000 Crore", "BDT 3,000 Crore", "BDT 5,000 Crore"], key="m4q2")
        if st.button("Check", key="m4c2"):
            if q2 == "BDT 3,000 Crore":
                st.success("✅ Correct! CbCR is required for groups with consolidated revenue ≥ BDT 3,000 Crore.")
            else:
                st.error("❌ Incorrect. The CbCR threshold is BDT 3,000 Crore consolidated group revenue.")

        st.markdown("---")
        st.markdown("**3. Within how many days must a taxpayer submit TP documentation after receiving an NBR notice?**")
        q3 = st.radio("Select:", ["15 days", "30 days", "60 days", "90 days"], key="m4q3")
        if st.button("Check", key="m4c3"):
            if q3 == "30 days":
                st.success("✅ Correct! Under ITA 2023, TP documentation must be submitted within 30 days of NBR's request.")
            else:
                st.error("❌ Incorrect. The deadline is 30 days from the date of NBR notice.")

        st.markdown("---")
        st.markdown("**4. The three-tier documentation framework under OECD BEPS Action 13 consists of:**")
        q4 = st.radio("Select:", [
            "Tax Return, Audit Report, Annual Report",
            "Master File, Local File, Country-by-Country Report",
            "Entity Profile, Transaction Analysis, ALP Calculation",
            "Group Policy, FAR Analysis, Database Search"
        ], key="m4q4")
        if st.button("Check", key="m4c4"):
            if q4 == "Master File, Local File, Country-by-Country Report":
                st.success("✅ Correct! BEPS Action 13: Master File + Local File + CbCR = three-tier documentation.")
            else:
                st.error("❌ Incorrect. The three tiers are: Master File, Local File, Country-by-Country Report.")

        st.markdown("---")
        st.markdown("**5. Which document contains entity-level information specific to the Bangladeshi taxpayer?**")
        q5 = st.radio("Select:", ["Master File", "Local File", "CbCR", "Group Tax Policy"], key="m4q5")
        if st.button("Check", key="m4c5"):
            if q5 == "Local File":
                st.success("✅ Correct! The Local File contains entity-specific information including each transaction's TP analysis.")
            else:
                st.error("❌ Incorrect. The Local File is entity-specific. The Master File is group-level.")

    # ─────────────────────────────────────────────
    with tab5:
        st.header("Module Summary")

        st.markdown("""
        ### 🎯 Key Takeaways

        | Item | Key Requirement |
        |------|----------------|
        | Who must document | All entities with international transactions |
        | De minimis | No threshold for international transactions |
        | Domestic transaction threshold | BDT 30 Crore |
        | Timing | Contemporaneous (before/at time of return filing) |
        | Submission on request | Within 30 days of NBR notice |
        | CbCR threshold | Consolidated group revenue ≥ BDT 3,000 Crore |
        | CbCR deadline | 12 months after end of reporting fiscal year |

        ### 📄 Three-Tier Documentation Framework

        | Tier | Document | Prepared By | Content Level |
        |------|----------|-------------|---------------|
        | 1 | Master File | MNE Group | Group-wide |
        | 2 | Local File | Bangladesh entity | Entity-specific |
        | 3 | CbCR | Ultimate Parent Entity | Country-by-country |

        ### ✅ Local File Must-Haves
        ```
        1. Associated enterprise list and relationships
        2. List of all international transactions (amounts + nature)
        3. FAR analysis for each transaction
        4. Most Appropriate Method selection and justification
        5. Comparability analysis and ALP determination
        6. Intercompany agreements
        7. Financial statements
        8. Database search results / comparable information
        ```

        ### ⚠️ Common Documentation Failures in BD Audits
        - No intercompany agreements in place
        - Method chosen without justification
        - Outdated comparables (> 3 years old)
        - No FAR analysis performed
        - Documentation prepared after audit notice (not contemporaneous)
        """)

        st.success("🎓 **Module 4 Complete!** You now understand TP documentation requirements under ITA 2023.")
        st.info("💡 **Next**: Proceed to Module 5 — TP Audit, Penalties & Dispute Resolution.")

if __name__ == "__main__":
    show()