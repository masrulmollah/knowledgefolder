import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📋 IFRS 18: Presentation and Disclosure in Financial Statements")
    st.markdown("*Master the new structured income statement categories and Management-Defined Performance Measures*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Effective Date")
        st.markdown("""
        **IFRS 18** replaces IAS 1's income statement requirements (IAS 1 continues to govern the balance sheet, statement of changes in equity, and general features). It is effective for annual reporting periods beginning on or after **1 January 2027**, with earlier application permitted.

        **Three Key Objectives:**
        1. Improve comparability of the income statement through **defined categories and required subtotals**
        2. Require disclosure of **Management-Defined Performance Measures (MPMs)** — i.e., "non-GAAP" metrics — within the financial statements
        3. Set enhanced principles for **aggregation and disaggregation** of information
        """)

        st.subheader("2. Five Defined Categories of the Income Statement")
        st.markdown("""
        IFRS 18 requires income and expenses to be classified into FIVE categories, with **two new mandatory subtotals**:

        | Category | Content |
        |---|---|
        | **1. Operating** | Default category — includes income/expenses not classified in the other four categories. ALL entities have this category |
        | **2. Investing** | Income/expenses from assets that generate returns INDEPENDENTLY of other resources (e.g., associates, JVs, investment property, dividend/interest income on investments not core to operations) |
        | **3. Financing** | Income/expenses from liabilities involving raising finance (interest expense on borrowings, lease liability interest) |
        | **4. Income Tax** | Income tax expense per IAS 12 |
        | **5. Discontinued Operations** | Per IFRS 5 |

        **Two New Required Subtotals:**
        ```
        Operating Profit (subtotal)
        Profit Before Financing and Income Tax (subtotal) = Operating Profit + Investing Category
        ```
        """)

        st.subheader("3. Classification — Operating vs Investing vs Financing")
        st.markdown("""
        **Default rule:** Income/expense is classified as **OPERATING** unless it specifically qualifies for Investing or Financing.

        **Investing category includes:**
        - Income from associates/JVs (equity method share of profit)
        - Gains/losses on disposal of investments
        - Dividend and interest income from investments that don't relate to the entity's main business activities

        **Financing category includes:**
        - Interest expense on ALL borrowings (loans, bonds)
        - Interest on lease liabilities (IFRS 16)
        - Unwinding of discount on liabilities (e.g., provisions) — entity accounting policy choice on classification

        **Entities with specified main business activities** (e.g., banks holding investments, insurers issuing insurance contracts) may classify related income/expenses as OPERATING even though they'd otherwise fall into Investing/Financing — reflecting the entity's actual business model.
        """)

        st.subheader("4. Management-Defined Performance Measures (MPMs)")
        st.markdown("""
        An **MPM** is a subtotal of income/expenses that:
        - Is used in public communications OUTSIDE the financial statements (e.g., earnings releases, investor presentations)
        - Communicates management's view of an aspect of financial performance
        - Is NOT a subtotal specifically required or listed by IFRS (e.g., not gross profit, not the new mandatory subtotals)

        **Common examples:** "Adjusted EBITDA," "Underlying profit," "Core earnings"

        **NEW REQUIREMENT:** MPMs must now be disclosed **IN THE FINANCIAL STATEMENTS** (in a single note), including:
        - Why the measure communicates management's view of performance
        - **Reconciliation** to the most directly comparable IFRS-specified subtotal/total
        - Income tax effect and effect on NCI for each reconciling item
        - This brings "non-GAAP" or "alternative performance measures" under **audit scrutiny** for the first time
        """)

        st.subheader("5. Aggregation and Disaggregation Principles")
        st.markdown("""
        - Items must be aggregated/disaggregated based on **shared characteristics** (not dissimilar items lumped together)
        - **Enhanced guidance on "operating expenses by nature vs function"** — if presenting by function (e.g., cost of sales), required to disclose certain "by nature" information in the notes (e.g., depreciation, employee benefits, amortisation) if not separately presented on the face of the income statement
        - Items labelled "other" should be used sparingly and only for genuinely individually immaterial items
        """)

        st.subheader("6. Statement of Cash Flows Changes (Consequential)")
        st.markdown("""
        IFRS 18 makes consequential amendments to IAS 7:
        - The starting point for the **indirect method operating activities** section is now **Operating Profit** (the new IFRS 18 subtotal) — rather than profit before tax
        - Removes the choice of classifying interest/dividends in the cash flow statement for MOST entities — aligns with the income statement classification (with limited exceptions for entities with specified main business activities)
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: New Income Statement Structure")
        income_statement_18 = pd.DataFrame({
            "Line Item": [
                "Revenue", "Cost of sales", "Gross profit", "Other operating expenses",
                "**OPERATING PROFIT**", "Share of profit of associates", "Gain on disposal of investment property",
                "**PROFIT BEFORE FINANCING AND INCOME TAX**", "Interest expense on borrowings", "Interest on lease liabilities",
                "**PROFIT BEFORE TAX**", "Income tax expense", "**PROFIT FOR THE YEAR**"
            ],
            "Category": [
                "Operating", "Operating", "Operating", "Operating",
                "Subtotal", "Investing", "Investing",
                "Subtotal", "Financing", "Financing",
                "Subtotal", "Tax", "Total"
            ],
            "$000": [
                "25,000", "(14,000)", "11,000", "(4,500)",
                "**6,500**", "400", "250",
                "**7,150**", "(600)", "(150)",
                "**6,400**", "(1,600)", "**4,800**"
            ]
        })
        st.dataframe(income_statement_18, use_container_width=True, hide_index=True)
        st.markdown("Note the TWO mandatory new subtotals: **Operating Profit** and **Profit Before Financing and Income Tax**")

        st.subheader("Example 2: Classification Decision — Bank vs Manufacturer")
        st.markdown("""
        | Item | Manufacturer Classification | Bank Classification |
        |---|---|---|
        | Interest income on cash deposits | Investing (incidental to main business) | **Operating** (core to banking business) |
        | Interest expense on borrowings | Financing | **Operating** (core to banking — taking deposits, lending) |
        | Dividend income on equity investments | Investing | Depends on whether investing is a main business activity |

        This shows how the SAME item can be classified differently depending on the entity's main business activities.
        """)

        st.subheader("Example 3: MPM Disclosure — Adjusted EBITDA")
        st.markdown("""
        *Extract from Notes — Management-Defined Performance Measures:*

        *"Adjusted EBITDA is a measure used by management and reported to investors to assess underlying operating performance, excluding the effects of restructuring costs and impairment charges which management considers not reflective of ongoing operations."*

        **Reconciliation:**

        | | $000 |
        |---|---|
        | Operating Profit (IFRS subtotal) | 6,500 |
        | Add: Depreciation and amortisation | 1,800 |
        | Add: Restructuring costs | 450 |
        | Add: Impairment charges | 300 |
        | **Adjusted EBITDA (MPM)** | **9,050** |
        | Tax effect of adjustments | (188) |
        | NCI effect of adjustments | (50) |

        This level of reconciliation and tax/NCI disclosure is a NEW requirement under IFRS 18 — previously "Adjusted EBITDA" might have appeared ONLY in an earnings press release with no formal reconciliation requirement.
        """)

        st.subheader("Example 4: Operating Expenses — By Nature Disclosure Requirement")
        st.markdown("""
        Entity presents expenses **by function** on the face of the income statement (Cost of Sales, Distribution, Admin).

        IFRS 18 requires disclosure of certain **by-nature** information in the notes:

        | By-Nature Item | Amount ($000) |
        |---|---|
        | Depreciation of PPE | 1,200 |
        | Amortisation of intangibles | 600 |
        | Employee benefits expense | 8,500 |
        | Impairment losses | 300 |

        This ensures users get BOTH functional clarity (on the face) AND nature-based insight (in notes) — useful for forecasting and cash flow analysis.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Income Statement Category Classifier")
        item_18 = st.selectbox("Select the income/expense item:", [
            "Revenue from sale of goods",
            "Interest expense on bank loan",
            "Share of profit from associate",
            "Interest income on excess cash (manufacturer)",
            "Interest income on customer deposits (bank's core business)",
            "Gain on disposal of investment property",
            "Income tax expense",
            "Depreciation of factory equipment",
            "Interest on lease liability"
        ])
        category_map_18 = {
            "Revenue from sale of goods": "Operating",
            "Interest expense on bank loan": "Financing",
            "Share of profit from associate": "Investing",
            "Interest income on excess cash (manufacturer)": "Investing (incidental to main business)",
            "Interest income on customer deposits (bank's core business)": "Operating (core banking activity)",
            "Gain on disposal of investment property": "Investing",
            "Income tax expense": "Income Tax",
            "Depreciation of factory equipment": "Operating",
            "Interest on lease liability": "Financing"
        }
        result_18 = category_map_18[item_18]
        if "Operating" in result_18:
            st.success(f"📌 **{result_18}**")
        elif "Investing" in result_18:
            st.info(f"📌 **{result_18}**")
        elif "Financing" in result_18:
            st.warning(f"📌 **{result_18}**")
        else:
            st.error(f"📌 **{result_18}**")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Build the New Income Statement Structure")
        col1, col2 = st.columns(2)
        with col1:
            revenue_18 = st.number_input("Revenue ($000)", value=25000)
            cogs_18 = st.number_input("Cost of Sales ($000)", value=14000)
            opex_18 = st.number_input("Other Operating Expenses ($000)", value=4500)
            investing_income = st.number_input("Investing Category Income ($000)", value=650)
        with col2:
            financing_exp = st.number_input("Financing Category Expense ($000)", value=750)
            tax_18 = st.number_input("Income Tax Expense ($000)", value=1600)

        if st.button("Generate Income Statement"):
            operating_profit = revenue_18 - cogs_18 - opex_18
            pre_financing_tax = operating_profit + investing_income
            pre_tax_profit = pre_financing_tax - financing_exp
            net_profit_18 = pre_tax_profit - tax_18

            is_table = pd.DataFrame({
                "Line Item": ["Revenue", "Cost of Sales", "Other Operating Expenses", "**OPERATING PROFIT**",
                              "Investing Income", "**PROFIT BEFORE FINANCING AND TAX**",
                              "Financing Expense", "**PROFIT BEFORE TAX**", "Income Tax", "**PROFIT FOR THE YEAR**"],
                "$000": [f"{revenue_18:,.0f}", f"({cogs_18:,.0f})", f"({opex_18:,.0f})", f"**{operating_profit:,.0f}**",
                        f"{investing_income:,.0f}", f"**{pre_financing_tax:,.0f}**",
                        f"({financing_exp:,.0f})", f"**{pre_tax_profit:,.0f}**", f"({tax_18:,.0f})", f"**{net_profit_18:,.0f}**"]
            })
            st.dataframe(is_table, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔧 Tool 3: MPM Reconciliation Builder")
        op_profit_mpm = st.number_input("Operating Profit (IFRS subtotal) ($000)", value=6500, key="mpm_op")
        depr_mpm = st.number_input("Add: Depreciation & Amortisation ($000)", value=1800, key="mpm_depr")
        restructuring = st.number_input("Add: Restructuring Costs ($000)", value=450, key="mpm_restr")
        impairment_mpm = st.number_input("Add: Impairment Charges ($000)", value=300, key="mpm_imp")

        if st.button("Build MPM Reconciliation"):
            mpm_total = op_profit_mpm + depr_mpm + restructuring + impairment_mpm
            tax_effect = (depr_mpm + restructuring + impairment_mpm) * 0.21
            st.markdown(f"""
            | Item | $000 |
            |---|---|
            | Operating Profit (IFRS subtotal) | {op_profit_mpm:,.0f} |
            | + Depreciation & Amortisation | {depr_mpm:,.0f} |
            | + Restructuring Costs | {restructuring:,.0f} |
            | + Impairment Charges | {impairment_mpm:,.0f} |
            | **Adjusted EBITDA (MPM)** | **{mpm_total:,.0f}** |
            | Estimated Tax Effect of Adjustments (21%) | ({tax_effect:,.0f}) |
            """)
            st.info("⚠️ Per IFRS 18, this reconciliation must appear IN THE FINANCIAL STATEMENTS (not just in an earnings release).")

    with tab4:
        st.header("Visualizations")

        st.subheader("New IFRS 18 Income Statement Structure")
        st.markdown("""
        ```
        Revenue, COGS, Other Operating Items
                    |
                    ▼
          ═══ OPERATING PROFIT ═══  (NEW mandatory subtotal)
                    |
            + Investing Category
                    |
                    ▼
    ═══ PROFIT BEFORE FINANCING AND INCOME TAX ═══  (NEW mandatory subtotal)
                    |
            − Financing Category
                    |
                    ▼
            PROFIT BEFORE TAX
                    |
            − Income Tax
                    |
                    ▼
            PROFIT FOR THE YEAR
        ```
        """)

        st.subheader("Income Statement Category Waterfall")
        categories_w = ["Operating\nProfit", "Investing\nIncome", "Profit Before\nFin. & Tax", "Financing\nExpense", "Profit Before\nTax", "Tax", "Net Profit"]
        values_w = [6500, 650, 0, -750, 0, -1600, 0]
        measures_w = ["relative", "relative", "total", "relative", "total", "relative", "total"]
        fig = go.Figure(go.Waterfall(
            x=categories_w, y=values_w, measure=measures_w,
            increasing={"marker": {"color": "#34D399"}},
            decreasing={"marker": {"color": "#F87171"}},
            totals={"marker": {"color": "#2563EB"}}
        ))
        fig.update_layout(title="IFRS 18 Income Statement Build-Up ($000)", height=420)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. IFRS 18 introduces how many defined categories for the income statement?**")
        q1 = st.radio("", ["Three", "Four", "Five", "Six"], key="ifrs18q1")
        if st.button("Check Answer", key="ifrs18c1"):
            if q1 == "Five":
                st.success("✅ Correct! The FIVE categories are: Operating, Investing, Financing, Income Tax, and Discontinued Operations.")
            else:
                st.error("❌ IFRS 18 has FIVE categories: Operating, Investing, Financing, Income Tax, Discontinued Operations.")

        st.markdown("---")
        st.markdown("**2. The two new mandatory subtotals required by IFRS 18 are:**")
        q2 = st.radio("", [
            "Gross Profit and Net Profit",
            "Operating Profit and Profit Before Financing and Income Tax",
            "EBITDA and EBIT",
            "Revenue and Total Comprehensive Income"
        ], key="ifrs18q2")
        if st.button("Check Answer", key="ifrs18c2"):
            if q2 == "Operating Profit and Profit Before Financing and Income Tax":
                st.success("✅ Correct! These are the two NEW mandatory subtotals introduced by IFRS 18 to improve comparability across entities.")
            else:
                st.error("❌ The two NEW subtotals are: OPERATING PROFIT and PROFIT BEFORE FINANCING AND INCOME TAX.")

        st.markdown("---")
        st.markdown("**3. A Management-Defined Performance Measure (MPM) is:**")
        q3 = st.radio("", [
            "Any subtotal specifically required by IFRS",
            "Gross profit, as defined by IAS 1",
            "A subtotal used in public communications outside the financial statements that communicates management's view of performance",
            "The statutory net profit figure"
        ], key="ifrs18q3")
        if st.button("Check Answer", key="ifrs18c3"):
            if q3 == "A subtotal used in public communications outside the financial statements that communicates management's view of performance":
                st.success("✅ Correct! An MPM is essentially a 'non-GAAP' measure (e.g., Adjusted EBITDA) used in earnings releases/investor communications — NOW required to be disclosed and reconciled within the financial statements.")
            else:
                st.error("❌ MPMs are 'non-GAAP'-style measures used OUTSIDE the financial statements that communicate management's view — NOT IFRS-required subtotals.")

        st.markdown("---")
        st.markdown("**4. For an MPM, IFRS 18 requires disclosure of:**")
        q4 = st.radio("", [
            "Only the final MPM figure", "A reconciliation to the most comparable IFRS subtotal, including tax and NCI effects", "Nothing — MPMs remain outside financial statements", "Only a qualitative description"
        ], key="ifrs18q4")
        if st.button("Check Answer", key="ifrs18c4"):
            if q4 == "A reconciliation to the most comparable IFRS subtotal, including tax and NCI effects":
                st.success("✅ Correct! IFRS 18 requires a full reconciliation with the tax effect and NCI effect of each reconciling item — bringing MPMs into the audited financial statements for the first time.")
            else:
                st.error("❌ MPM disclosure requires a RECONCILIATION to the nearest IFRS subtotal, INCLUDING tax and NCI effects of adjustments.")

        st.markdown("---")
        st.markdown("**5. Under IFRS 18's consequential changes to IAS 7, the indirect method starting point for operating cash flows is now:**")
        q5 = st.radio("", ["Profit before tax", "Operating Profit (the new IFRS 18 subtotal)", "Net profit after tax", "Revenue"], key="ifrs18q5")
        if st.button("Check Answer", key="ifrs18c5"):
            if q5 == "Operating Profit (the new IFRS 18 subtotal)":
                st.success("✅ Correct! The starting point shifts to OPERATING PROFIT (the new mandatory IFRS 18 subtotal), rather than profit before tax as under the old IAS 7.")
            else:
                st.error("❌ The new starting point is OPERATING PROFIT — a consequential amendment aligning IAS 7 with the new IFRS 18 income statement structure.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Three Key Objectives
        1. Improved comparability via defined categories and subtotals
        2. MPM disclosure brought into financial statements
        3. Enhanced aggregation/disaggregation principles

        ### 2. Five Categories
        ```
        Operating (default) | Investing | Financing | Income Tax | Discontinued Operations
        ```

        ### 3. Two New Mandatory Subtotals
        ```
        OPERATING PROFIT
        PROFIT BEFORE FINANCING AND INCOME TAX = Operating Profit + Investing Category
        ```

        ### 4. Classification Principle
        - Default = Operating
        - Investing = returns independent of other resources (associates, JVs, investment income)
        - Financing = costs of raising finance (borrowings, leases)
        - Entities with specified main business activities may reclassify items as Operating

        ### 5. MPM Requirements
        - Must disclose IN financial statements (single note)
        - Reconciliation to nearest IFRS subtotal
        - Tax effect + NCI effect of each reconciling item
        - Why it reflects management's view of performance

        ### 6. Effective Date
        Annual periods beginning on or after **1 January 2027** (early application permitted)
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
5 Categories: Operating | Investing | Financing | Income Tax | Discontinued Ops
2 New Subtotals: Operating Profit | Profit Before Financing & Income Tax
MPM = non-GAAP-style measure → NOW requires reconciliation + tax/NCI effects IN financial statements
Default classification = Operating (unless qualifies for Investing/Financing)
IAS 7 indirect method now starts from OPERATING PROFIT (not profit before tax)
Effective: periods beginning on/after 1 January 2027
        """)

        st.success("🎓 **IFRS 18 Complete!** You can now apply the new income statement categories, build the required subtotals, and prepare MPM reconciliation disclosures.")
        st.info("🎉 **Congratulations!** You have completed the full Accounting Standards curriculum — from IAS 1 through IFRS 18!")

if __name__ == "__main__":
    show()