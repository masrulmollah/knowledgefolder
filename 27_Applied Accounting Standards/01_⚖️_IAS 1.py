import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📋 IAS 1: Presentation of Financial Statements")
    st.markdown("*Master the core requirements for how financial statements must be structured, presented, and disclosed under IFRS*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Scope")
        st.markdown("""
        **IAS 1** prescribes the basis for presentation of general purpose financial statements to ensure comparability
        both with the entity's own financial statements of previous periods and with the financial statements of other entities.

        **IAS 1 applies to all general purpose financial statements prepared in accordance with IFRS.**

        **Key purposes:**
        - Ensure comparability across periods and entities
        - Provide a framework for the structure of financial statements
        - Define minimum content requirements
        - Establish overarching presentation principles
        """)

        st.subheader("2. Complete Set of Financial Statements")
        fs_data = {
            "Statement": [
                "Statement of Financial Position (Balance Sheet)",
                "Statement of Profit or Loss and Other Comprehensive Income",
                "Statement of Changes in Equity",
                "Statement of Cash Flows",
                "Notes to the Financial Statements",
                "Comparative Information"
            ],
            "Purpose": [
                "Snapshot of assets, liabilities and equity at reporting date",
                "Performance over the period — P&L and OCI items",
                "Changes in each component of equity during the period",
                "Cash inflows and outflows (operating, investing, financing)",
                "Accounting policies, disaggregation, disclosures",
                "Prior period comparatives (at least one prior period)"
            ],
            "Key Content": [
                "Current/non-current classification; line items prescribed by IAS 1",
                "Single statement or two-statement approach; OCI net or gross of tax",
                "Retained earnings, share capital, reserves movements",
                "Covered by IAS 7; indirect or direct method",
                "Judgements, estimates, related party info, etc.",
                "Restated if there is a change in accounting policy"
            ]
        }
        st.dataframe(pd.DataFrame(fs_data), use_container_width=True, hide_index=True)

        st.subheader("3. General Features of Financial Statements")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Fair Presentation & Compliance**
            - Must fairly present financial position, performance and cash flows
            - Compliance with IFRS must be explicitly stated
            - In rare circumstances, departure is permitted if compliance would be misleading

            **Going Concern**
            - Prepared on going concern basis unless management intends to liquidate
            - Disclose material uncertainties about going concern

            **Accrual Basis**
            - All statements except cash flows use accrual basis
            - Recognise effects when they occur, not when cash moves
            """)
        with col2:
            st.markdown("""
            **Materiality & Aggregation**
            - Present each material class of similar items separately
            - Do not offset assets/liabilities or income/expenses unless permitted

            **Frequency**
            - Present at least annually
            - If period changes, disclose and explain

            **Comparative Information**
            - Minimum one prior period for all amounts reported
            - Three balance sheets required if retrospective restatement occurs
            """)

        st.subheader("4. Structure of the Statement of Financial Position")
        st.markdown("""
        IAS 1 requires the following minimum line items on the balance sheet:

        | **Assets** | **Equity & Liabilities** |
        |-----------|--------------------------|
        | Property, plant & equipment | Share capital and reserves |
        | Investment property | Non-controlling interests |
        | Intangible assets | Long-term borrowings |
        | Financial assets | Deferred tax liabilities |
        | Investments (equity method) | Provisions |
        | Biological assets | Trade & other payables |
        | Inventories | Short-term borrowings |
        | Trade & other receivables | Current tax liabilities |
        | Cash & cash equivalents | |

        **Current vs Non-Current Classification:**
        - Current assets: expected to be realised within 12 months or the operating cycle
        - Current liabilities: due within 12 months or no unconditional right to defer beyond 12 months
        - Liquidity presentation is an alternative when it provides more relevant information (e.g., banks)
        """)

        st.subheader("5. Statement of Profit or Loss and OCI")
        st.markdown("""
        **Two Presentation Approaches:**

        **Single Statement:** Combines P&L and OCI in one continuous statement

        **Two-Statement Approach:** Separate P&L statement + a second statement starting from P&L total and adding OCI

        **Expense Classification (choose one method, apply consistently):**

        | **By Nature** | **By Function** |
        |--------------|----------------|
        | Raw materials | Cost of sales |
        | Employee costs | Distribution costs |
        | Depreciation | Administrative expenses |
        | Other expenses | Other operating expenses |

        **Items that CANNOT be presented as extraordinary:**
        - IAS 1 prohibits presentation of any items as extraordinary
        - All items must be classified within the normal line items

        **OCI Components include:**
        - Revaluation surplus (IAS 16, IAS 38)
        - Remeasurements of defined benefit plans (IAS 19)
        - Translation differences on foreign operations (IAS 21)
        - Fair value changes on FVOCI instruments (IFRS 9)
        - Effective portion of hedging gains/losses (IFRS 9)
        """)

        st.subheader("6. Notes to Financial Statements")
        st.markdown("""
        Notes must:
        1. Present information about the basis of preparation and accounting policies
        2. Disclose information required by IFRS not presented elsewhere
        3. Provide additional information relevant to understanding

        **Key disclosures in notes:**
        - Significant judgements and estimates
        - Capital management disclosures
        - Dividends proposed or declared
        - Entity's domicile, legal form, country of incorporation
        - Description of operations and principal activities
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Statement of Financial Position — ABC Manufacturing Ltd")
        st.markdown("**As at 31 December 2024 (in $000s)**")

        sfp_data = {
            "Line Item": [
                "ASSETS", "Non-Current Assets",
                "Property, Plant & Equipment", "Intangible Assets", "Investments (equity method)",
                "Total Non-Current Assets", "",
                "Current Assets", "Inventories", "Trade Receivables",
                "Cash & Cash Equivalents", "Total Current Assets", "TOTAL ASSETS",
                "EQUITY & LIABILITIES", "Equity",
                "Share Capital", "Retained Earnings", "Revaluation Reserve",
                "Total Equity", "",
                "Non-Current Liabilities", "Borrowings", "Deferred Tax",
                "Total Non-Current Liabilities", "",
                "Current Liabilities", "Trade Payables", "Current Tax Payable",
                "Short-term Borrowings", "Total Current Liabilities",
                "TOTAL EQUITY & LIABILITIES"
            ],
            "2024 $000": [
                "", "", "12,400", "3,200", "1,800",
                "17,400", "",
                "", "4,500", "3,800",
                "2,100", "10,400", "27,800",
                "", "", "5,000", "8,200", "1,600",
                "14,800", "",
                "", "8,000", "1,400",
                "9,400", "",
                "", "2,100", "800",
                "700", "3,600", "27,800"
            ],
            "2023 $000": [
                "", "", "11,200", "2,900", "1,600",
                "15,700", "",
                "", "4,100", "3,200",
                "1,900", "9,200", "24,900",
                "", "", "5,000", "6,800", "1,400",
                "13,200", "",
                "", "7,500", "1,200",
                "8,700", "",
                "", "1,900", "600",
                "500", "3,000", "24,900"
            ]
        }
        st.dataframe(pd.DataFrame(sfp_data), use_container_width=True, hide_index=True)

        st.subheader("Example 2: Profit or Loss — Nature vs Function Classification")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**By Nature (in $000s)**")
            nature_data = {
                "Item": ["Revenue", "Other income", "Changes in inventories",
                         "Raw materials used", "Employee costs", "Depreciation",
                         "Other expenses", "Finance costs", "Profit Before Tax"],
                "Amount": ["25,000", "500", "400", "(8,200)", "(6,100)", "(2,300)",
                           "(1,800)", "(500)", "7,000"]
            }
            st.dataframe(pd.DataFrame(nature_data), use_container_width=True, hide_index=True)

        with col2:
            st.markdown("**By Function (in $000s)**")
            func_data = {
                "Item": ["Revenue", "Cost of Sales", "Gross Profit",
                         "Distribution Costs", "Administrative Expenses",
                         "Other Income", "Finance Costs", "Profit Before Tax"],
                "Amount": ["25,000", "(14,600)", "10,400",
                           "(1,400)", "(1,900)", "500", "(600)", "7,000"]
            }
            st.dataframe(pd.DataFrame(func_data), use_container_width=True, hide_index=True)

        st.subheader("Example 3: OCI Items Classification")
        st.markdown("""
        **Items that may be reclassified to P&L (recycled):**
        - Foreign currency translation differences on foreign operations — **reclassified** when operation is disposed
        - Effective portion of hedging gains/losses — **reclassified** when hedged item affects P&L

        **Items that will NOT be reclassified to P&L (not recycled):**
        - Revaluation surplus on PPE/intangibles — **never recycled**
        - Remeasurements of defined benefit plans — **never recycled**
        - Equity instruments designated at FVOCI — **never recycled**

        This distinction matters because it signals the permanence of gains/losses.
        """)

        st.subheader("Example 4: Going Concern Disclosure")
        st.markdown("""
        **Scenario:** A company has net current liabilities of $2M and its primary bank facility expires in 6 months.

        **Required disclosure:** Management must assess whether the going concern assumption is appropriate. If material
        uncertainty exists:

        > *"The Directors have identified a material uncertainty which may cast significant doubt upon the Group's
        ability to continue as a going concern. The Group's ability to continue trading is dependent on successfully
        renewing the $5M revolving credit facility which expires on 30 June 2025. Negotiations with the bank are
        ongoing and management believes renewal is likely. The financial statements have been prepared on a going
        concern basis."*

        If going concern is not appropriate, the financial statements must be prepared on a break-up basis and this
        fact must be disclosed.
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Current vs Non-Current Classification Checker")
        st.markdown("Determine whether items should be classified as current or non-current:")

        col1, col2 = st.columns(2)
        with col1:
            item_type = st.selectbox("Item Type:", ["Asset", "Liability"])
            days_to_realise = st.number_input("Expected realisation/settlement (days):", 0, 3650, 180)
            operating_cycle = st.number_input("Entity's operating cycle (days):", 30, 730, 90)
            held_for_trading = st.checkbox("Held primarily for trading purposes?")

        with col2:
            if item_type == "Asset":
                threshold = max(365, operating_cycle)
                if held_for_trading or days_to_realise <= threshold:
                    st.success(f"✅ **CURRENT ASSET**")
                    st.markdown(f"Realisation within {days_to_realise} days ≤ threshold of {threshold} days (max of 365 days or operating cycle of {operating_cycle} days)")
                else:
                    st.info(f"📌 **NON-CURRENT ASSET**")
                    st.markdown(f"Realisation in {days_to_realise} days > threshold of {threshold} days")
            else:
                if held_for_trading or days_to_realise <= 365:
                    st.success(f"✅ **CURRENT LIABILITY**")
                    st.markdown(f"Settlement within {days_to_realise} days ≤ 365 days")
                else:
                    st.info(f"📌 **NON-CURRENT LIABILITY**")
                    st.markdown(f"Settlement in {days_to_realise} days > 365 days")

        st.markdown("---")
        st.subheader("🔧 Tool 2: OCI Item Classifier")
        st.markdown("Classify OCI items as recyclable or non-recyclable:")

        oci_item = st.selectbox("Select OCI Item:", [
            "Foreign currency translation differences",
            "Effective portion of cash flow hedges",
            "Revaluation surplus on PPE (IAS 16)",
            "Revaluation surplus on intangibles (IAS 38)",
            "Remeasurements of defined benefit plans (IAS 19)",
            "Equity instruments at FVOCI (IFRS 9)",
            "Debt instruments at FVOCI (IFRS 9)"
        ])

        recyclable = {
            "Foreign currency translation differences": (True, "Reclassified when the foreign operation is disposed of"),
            "Effective portion of cash flow hedges": (True, "Reclassified when the hedged item affects P&L or is no longer expected"),
            "Revaluation surplus on PPE (IAS 16)": (False, "Cannot be recycled; transferred directly to retained earnings on disposal"),
            "Revaluation surplus on intangibles (IAS 38)": (False, "Cannot be recycled; transferred directly to retained earnings"),
            "Remeasurements of defined benefit plans (IAS 19)": (False, "Permanently in OCI; never recycled to P&L"),
            "Equity instruments at FVOCI (IFRS 9)": (False, "Irrevocable designation; gains/losses never recycled"),
            "Debt instruments at FVOCI (IFRS 9)": (True, "Recycled to P&L on derecognition or impairment")
        }

        result, explanation = recyclable[oci_item]
        if result:
            st.warning(f"♻️ **Recyclable (may be reclassified to P&L)**\n\n{explanation}")
        else:
            st.info(f"🔒 **Non-Recyclable (will NOT be reclassified to P&L)**\n\n{explanation}")

        st.markdown("---")
        st.subheader("🔧 Tool 3: Financial Statement Completeness Checker")
        st.markdown("Check whether your financial statement package is complete under IAS 1:")

        components = {
            "Statement of Financial Position (Balance Sheet)": st.checkbox("Statement of Financial Position (Balance Sheet)"),
            "Statement of P&L and OCI": st.checkbox("Statement of Profit or Loss and Other Comprehensive Income"),
            "Statement of Changes in Equity": st.checkbox("Statement of Changes in Equity"),
            "Statement of Cash Flows (IAS 7)": st.checkbox("Statement of Cash Flows"),
            "Notes to Financial Statements": st.checkbox("Notes including significant accounting policies"),
            "Comparative Information": st.checkbox("Comparative information for prior period")
        }

        if st.button("Check Completeness"):
            missing = [k for k, v in components.items() if not v]
            if not missing:
                st.success("✅ Complete set of financial statements under IAS 1!")
            else:
                st.error(f"❌ Missing components:\n" + "\n".join([f"- {m}" for m in missing]))

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("Financial Statement Structure — IAS 1 Framework")
        labels = ["Complete Financial Statements", "Statement of Financial Position",
                  "Statement of P&L & OCI", "Statement of Changes in Equity",
                  "Statement of Cash Flows", "Notes",
                  "Non-Current Assets", "Current Assets", "Equity",
                  "Non-Current Liabilities", "Current Liabilities",
                  "P&L Section", "OCI Section"]
        parents = ["", "Complete Financial Statements", "Complete Financial Statements",
                   "Complete Financial Statements", "Complete Financial Statements",
                   "Complete Financial Statements",
                   "Statement of Financial Position", "Statement of Financial Position",
                   "Statement of Financial Position", "Statement of Financial Position",
                   "Statement of Financial Position",
                   "Statement of P&L & OCI", "Statement of P&L & OCI"]
        values = [100, 30, 25, 15, 15, 15, 10, 10, 10, 10, 10, 15, 10]

        fig = go.Figure(go.Sunburst(
            labels=labels, parents=parents, values=values,
            branchvalues="total",
            marker=dict(colors=["#1B3A6B", "#2563EB", "#0D7377", "#10B981",
                                 "#F59E0B", "#6366F1", "#93C5FD", "#BAE6FD",
                                 "#6EE7B7", "#FDE68A", "#C4B5FD", "#60A5FA", "#34D399"])
        ))
        fig.update_layout(title="IAS 1 — Complete Financial Statement Structure", height=500)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("OCI: Recyclable vs Non-Recyclable Items")
        oci_categories = ["Translation\nDifferences", "Cash Flow\nHedges",
                          "Debt FVOCI", "PPE\nRevaluation", "IAS 19\nRemeasure",
                          "Equity\nFVOCI"]
        recyclable_flag = [1, 1, 1, 0, 0, 0]
        colors = ["#34D399" if r else "#F87171" for r in recyclable_flag]
        labels_oci = ["♻️ Recyclable" if r else "🔒 Non-Recyclable" for r in recyclable_flag]

        fig2 = go.Figure(go.Bar(
            x=oci_categories, y=[1]*6,
            marker_color=colors,
            text=labels_oci, textposition="inside",
            textfont=dict(color="white", size=11)
        ))
        fig2.update_layout(title="OCI Components — Reclassification Treatment",
                           yaxis=dict(visible=False), height=300)
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Expense Classification Comparison")
        categories = ["Revenue", "Cost of Goods", "Employee\nCosts", "Depreciation",
                      "Distribution", "Admin", "Finance\nCosts"]
        by_function = [25000, 14600, 0, 0, 1400, 1900, 600]
        by_nature = [25000, 8200, 6100, 2300, 0, 1800, 500]

        fig3 = go.Figure()
        fig3.add_trace(go.Bar(name="By Function", x=categories, y=by_function, marker_color="#2563EB"))
        fig3.add_trace(go.Bar(name="By Nature", x=categories, y=by_nature, marker_color="#0D7377"))
        fig3.update_layout(barmode="group", title="Expense Classification — By Function vs By Nature ($000s)", height=400)
        st.plotly_chart(fig3, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IAS 1, which of the following is NOT part of a complete set of financial statements?**")
        q1 = st.radio("", [
            "Statement of Cash Flows",
            "Statement of Changes in Equity",
            "Directors' Report",
            "Notes to Financial Statements"
        ], key="ias1q1")
        if st.button("Check Answer", key="ias1c1"):
            if q1 == "Directors' Report":
                st.success("✅ Correct! The Directors' Report is NOT part of the financial statements under IAS 1. It is a separate narrative report.")
            else:
                st.error("❌ Incorrect. The Directors' Report is a narrative report and NOT one of the five components of financial statements under IAS 1.")

        st.markdown("---")
        st.markdown("**2. When must three balance sheets (statements of financial position) be presented?**")
        q2 = st.radio("", [
            "Every year as standard practice",
            "When there is a retrospective restatement or retrospective change in accounting policy",
            "When the entity changes its year-end",
            "When the entity lists on a stock exchange"
        ], key="ias1q2")
        if st.button("Check Answer", key="ias1c2"):
            if q2 == "When there is a retrospective restatement or retrospective change in accounting policy":
                st.success("✅ Correct! IAS 1 requires a third balance sheet (at the beginning of the comparative period) when there is a retrospective restatement or change in accounting policy.")
            else:
                st.error("❌ Incorrect. Three balance sheets are required only when there is a retrospective restatement or a retrospective change in accounting policy.")

        st.markdown("---")
        st.markdown("**3. Remeasurements of defined benefit plans (IAS 19) are presented in OCI. These items are:**")
        q3 = st.radio("", [
            "Reclassified to P&L when the plan is terminated",
            "Reclassified to P&L in the following period",
            "Never reclassified to P&L (non-recyclable)",
            "Reclassified to P&L when actuarial assumptions change"
        ], key="ias1q3")
        if st.button("Check Answer", key="ias1c3"):
            if q3 == "Never reclassified to P&L (non-recyclable)":
                st.success("✅ Correct! IAS 19 remeasurements are permanently in OCI and are NEVER recycled to profit or loss.")
            else:
                st.error("❌ Incorrect. IAS 19 remeasurements are non-recyclable — they go to OCI permanently and are never reclassified to P&L.")

        st.markdown("---")
        st.markdown("**4. An entity has an operating cycle of 18 months. A receivable expected to be collected in 14 months should be classified as:**")
        q4 = st.radio("", [
            "Current — it is within 18 months (the operating cycle)",
            "Non-current — it exceeds the standard 12-month threshold",
            "It depends on whether the receivable is trade or non-trade",
            "Either; management can choose"
        ], key="ias1q4")
        if st.button("Check Answer", key="ias1c4"):
            if q4 == "Current — it is within 18 months (the operating cycle)":
                st.success("✅ Correct! Current assets include items expected to be realised within the operating cycle OR 12 months, whichever is longer. With an 18-month cycle, 14 months qualifies as current.")
            else:
                st.error("❌ Incorrect. Current assets are realised within 12 months OR the operating cycle, whichever is longer. An 18-month cycle means 14-month receivables are current.")

        st.markdown("---")
        st.markdown("**5. Under IAS 1, can an entity present extraordinary items?**")
        q5 = st.radio("", [
            "Yes, if they are both unusual and infrequent",
            "Yes, but only in the notes",
            "No — IAS 1 prohibits the presentation of any items as extraordinary",
            "Yes, for items exceeding 10% of profit before tax"
        ], key="ias1q5")
        if st.button("Check Answer", key="ias1c5"):
            if q5 == "No — IAS 1 prohibits the presentation of any items as extraordinary":
                st.success("✅ Correct! IAS 1 explicitly prohibits presenting any items as extraordinary in the financial statements or in the notes.")
            else:
                st.error("❌ Incorrect. IAS 1 explicitly prohibits extraordinary items — all items must be classified within normal line items.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Objective of IAS 1
        IAS 1 sets the framework for how general purpose financial statements must be presented — ensuring **comparability,
        transparency and completeness** across entities and periods.

        ### 2. Complete Set of Financial Statements
        | Component | Key Content |
        |-----------|-------------|
        | Statement of Financial Position | Assets, liabilities, equity at reporting date |
        | Statement of P&L and OCI | Revenue, expenses, other comprehensive income |
        | Statement of Changes in Equity | Movements in equity components |
        | Statement of Cash Flows | Operating, investing, financing cash flows (IAS 7) |
        | Notes | Policies, judgements, estimates, disclosures |
        | Comparatives | Minimum one prior period |

        ### 3. General Features
        - **Fair presentation** — present faithfully in accordance with IFRS
        - **Going concern** — default basis; disclose any material uncertainties
        - **Accrual basis** — for all statements except cash flows
        - **Materiality** — separate presentation of material classes
        - **No offsetting** — do not offset assets vs liabilities or income vs expenses
        - **No extraordinary items** — prohibited by IAS 1

        ### 4. Balance Sheet Classification
        - **Current assets**: realisable within 12 months OR operating cycle (whichever longer)
        - **Current liabilities**: due within 12 months OR no unconditional right to defer

        ### 5. OCI Classification
        | Recyclable to P&L | Non-Recyclable |
        |-------------------|----------------|
        | FX translation differences | PPE revaluation surplus |
        | Cash flow hedge reserve | IAS 19 remeasurements |
        | Debt instruments at FVOCI | Equity instruments at FVOCI |

        ### 6. Key Disclosures
        - Significant accounting judgements and estimates
        - Capital management policies
        - Dividends and non-adjusting post-balance sheet events
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Current Asset Threshold = max(12 months, Operating Cycle)
Three Balance Sheets required when: Retrospective restatement OR change in accounting policy
Extraordinary items = PROHIBITED under IAS 1
OCI items = Recyclable OR Non-recyclable (must present separately)
        """)

        st.success("🎓 **IAS 1 Complete!** You can now identify the components of financial statements, classify items correctly and understand key presentation requirements under IAS 1.")
        st.info("💡 **Next**: IAS 2 — Inventories")

if __name__ == "__main__":
    show()