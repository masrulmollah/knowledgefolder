import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💵 IAS 7: Statement of Cash Flows")
    st.markdown("*Master the preparation, classification and analysis of cash flow statements under IFRS*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Scope")
        st.markdown("""
        **IAS 7** requires entities to present a Statement of Cash Flows as part of their financial statements.
        It shows **actual cash generated and used** during the period, classified under three activities.

        **Why cash flows matter:**
        - Profit ≠ Cash (accruals accounting creates timing differences)
        - Cash is the lifeblood of any business
        - Enables assessment of liquidity, solvency and financial flexibility
        - Allows comparison across entities with different accounting policies
        """)

        st.subheader("2. Three Categories of Cash Flows")
        category_data = {
            "Category": ["Operating Activities", "Investing Activities", "Financing Activities"],
            "Definition": [
                "Principal revenue-producing activities and other activities not investing or financing",
                "Acquisition and disposal of long-term assets and other investments",
                "Activities that change the size/composition of equity and borrowings"
            ],
            "Examples": [
                "Cash receipts from customers; payments to suppliers; tax paid; interest paid (if classified here); dividends received (if classified here)",
                "Purchase/sale of PPE; purchase/sale of investments; loans made to other parties; acquisition of subsidiaries",
                "Proceeds from share issuance; repayment of borrowings; payment of dividends; lease liability payments"
            ],
            "IAS 7 Treatment Options": [
                "Interest paid: operating or financing\nInterest received: operating or investing\nDividends received: operating or investing\nDividends paid: operating or financing",
                "Specific classification required",
                "Specific classification required"
            ]
        }
        st.dataframe(pd.DataFrame(category_data), use_container_width=True, hide_index=True)

        st.subheader("3. Two Methods for Operating Activities")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Direct Method (Preferred by IAS 7)**
            - Shows gross cash receipts from customers
            - Shows gross cash payments to suppliers and employees
            - More informative but harder to prepare
            - Requires detailed cash transaction records

            *Example:*
            - Cash received from customers: $X
            - Cash paid to suppliers: $(X)
            - Cash paid to employees: $(X)
            - Interest paid: $(X)
            - Tax paid: $(X)
            """)
        with col2:
            st.markdown("""
            **Indirect Method (Most Common in Practice)**
            - Starts with profit before tax
            - Adjusts for non-cash items and working capital changes
            - Reconciles accrual profit to cash
            - More widely used

            *Adjustments include:*
            - + Depreciation & amortisation
            - + Impairment losses
            - +/− Working capital changes
            - − Unrealised gains / + unrealised losses
            - − Tax paid
            """)

        st.subheader("4. Key Classification Choices (IAS 7 Flexibility)")
        flex_data = {
            "Item": ["Interest paid", "Interest received", "Dividends received", "Dividends paid", "Tax paid"],
            "Option 1": ["Operating", "Operating", "Operating", "Operating", "Operating (default)"],
            "Option 2": ["Financing", "Investing", "Investing", "Financing", "Split if practicable"],
            "Common Practice": ["Financing (IFRS)", "Investing (IFRS)", "Investing (IFRS)", "Financing (IFRS)", "Operating"]
        }
        st.dataframe(pd.DataFrame(flex_data), use_container_width=True, hide_index=True)
        st.warning("⚠️ Once a classification is chosen, it must be applied consistently. Disclose the method used.")

        st.subheader("5. Non-Cash Transactions")
        st.markdown("""
        **Non-cash investing and financing transactions are EXCLUDED from the cash flow statement** but must be
        disclosed in the notes. Examples:

        - Acquisition of assets through finance leases
        - Conversion of debt to equity
        - Issue of shares as consideration in a business combination
        - Non-cash settlement of liabilities
        - Exchange of assets
        """)

        st.subheader("6. Special Items")
        st.markdown("""
        | Item | Treatment |
        |------|-----------|
        | **Taxes** | Classify as operating unless specifically identifiable with financing/investing |
        | **Foreign currency cash flows** | Translate at the rate at date of cash flow (or average rate) |
        | **FX differences on cash held** | Presented separately as reconciling item — not operating/investing/financing |
        | **Acquisitions/disposals of subsidiaries** | Single line in investing activities (net of cash acquired/disposed) |
        | **Lease payments (IFRS 16)** | Principal portion → financing; interest portion → financing or operating |
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Indirect Method — Operating Activities")
        st.markdown("**XYZ Ltd — Year ended 31 December 2024 ($000s)**")

        indirect_data = {
            "Item": [
                "Profit Before Tax",
                "Adjustments for non-cash items:",
                "  + Depreciation", "  + Amortisation",
                "  + Impairment loss", "  − Gain on disposal of PPE",
                "Changes in working capital:",
                "  − Increase in receivables",
                "  + Decrease in inventories",
                "  + Increase in payables",
                "Cash generated from operations",
                "Interest paid", "Tax paid",
                "Net Cash from Operating Activities"
            ],
            "Amount $000": [
                "5,200", "",
                "1,800", "400",
                "300", "(250)",
                "", "(600)", "400", "350",
                "7,600",
                "(480)", "(1,100)",
                "6,020"
            ]
        }
        st.dataframe(pd.DataFrame(indirect_data), use_container_width=True, hide_index=True)

        st.subheader("Example 2: Investing Activities")
        invest_data = {
            "Item": [
                "Purchase of property, plant & equipment",
                "Proceeds from disposal of PPE",
                "Acquisition of subsidiary (net of $200 cash acquired)",
                "Purchase of equity investments (FVOCI)",
                "Interest received",
                "Dividends received",
                "Net Cash Used in Investing Activities"
            ],
            "Amount $000": [
                "(3,200)", "750", "(1,800)",
                "(500)", "120", "80", "(4,550)"
            ]
        }
        st.dataframe(pd.DataFrame(invest_data), use_container_width=True, hide_index=True)

        st.subheader("Example 3: Financing Activities")
        finance_data = {
            "Item": [
                "Proceeds from issue of shares",
                "Proceeds from new bank borrowings",
                "Repayment of borrowings",
                "Payment of lease liabilities (principal)",
                "Dividends paid",
                "Net Cash from Financing Activities"
            ],
            "Amount $000": [
                "2,000", "3,000",
                "(2,500)", "(600)",
                "(800)", "1,100"
            ]
        }
        st.dataframe(pd.DataFrame(finance_data), use_container_width=True, hide_index=True)

        st.subheader("Example 4: Cash Flow Statement Reconciliation")
        recon_data = {
            "Item": [
                "Net Cash from Operating Activities",
                "Net Cash Used in Investing Activities",
                "Net Cash from Financing Activities",
                "Effect of FX changes on cash",
                "Net increase in cash",
                "Cash at beginning of period",
                "Cash at End of Period"
            ],
            "Amount $000": ["6,020", "(4,550)", "1,100", "30", "2,600", "1,900", "4,500"]
        }
        st.dataframe(pd.DataFrame(recon_data), use_container_width=True, hide_index=True)

        st.subheader("Example 5: Working Capital Adjustment — Trade Receivables")
        st.markdown("""
        **Reconciling accrual revenue to cash received:**

        | | $000 |
        |--|------|
        | Revenue (P&L) | 25,000 |
        | Add: Opening receivables | 3,200 |
        | Less: Closing receivables | (3,800) |
        | **Cash received from customers** | **24,400** |

        The increase in receivables of $600k means we earned $600k more than we actually collected in cash — hence deducted in the indirect method.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Indirect Method — Operating Cash Flow Builder")
        st.markdown("Enter figures to build the operating section:")
        col1, col2 = st.columns(2)
        with col1:
            pbt = st.number_input("Profit Before Tax ($000)", value=5200)
            depreciation = st.number_input("Depreciation & Amortisation ($000)", value=2200)
            impairment = st.number_input("Impairment Losses ($000)", value=300)
            disposal_gain = st.number_input("Gain on Disposal (enter as positive) ($000)", value=250)
        with col2:
            rec_change = st.number_input("Change in Receivables — increase=negative ($000)", value=-600)
            inv_change = st.number_input("Change in Inventories — increase=negative ($000)", value=400)
            pay_change = st.number_input("Change in Payables — increase=positive ($000)", value=350)
            interest_paid = st.number_input("Interest Paid ($000)", value=480)
            tax_paid = st.number_input("Tax Paid ($000)", value=1100)

        if st.button("Calculate Operating Cash Flow"):
            cfo = pbt + depreciation + impairment - disposal_gain + rec_change + inv_change + pay_change - interest_paid - tax_paid
            st.markdown("---")
            st.markdown(f"""
            | Item | $000 |
            |------|------|
            | Profit Before Tax | {pbt:,} |
            | + Depreciation & Amortisation | {depreciation:,} |
            | + Impairment | {impairment:,} |
            | − Gain on disposal | ({disposal_gain:,}) |
            | Working capital changes | {rec_change + inv_change + pay_change:,} |
            | Interest paid | ({interest_paid:,}) |
            | Tax paid | ({tax_paid:,}) |
            | **Net Cash from Operations** | **{cfo:,}** |
            """)
            if cfo > pbt:
                st.success(f"✅ Strong cash conversion! Operating cash of ${cfo:,}k exceeds profit of ${pbt:,}k.")
            elif cfo > 0:
                st.info(f"ℹ️ Positive operating cash flow of ${cfo:,}k but below reported profit.")
            else:
                st.error(f"⚠️ Negative operating cash flow of ${cfo:,}k — monitor working capital!")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Cash Conversion Ratio Analyser")
        revenue = st.number_input("Revenue ($000)", value=25000, key="ccr_rev")
        net_profit = st.number_input("Net Profit ($000)", value=4000, key="ccr_np")
        op_cash = st.number_input("Operating Cash Flow ($000)", value=6020, key="ccr_ocf")

        if st.button("Analyse Cash Conversion", key="ccr_btn"):
            if net_profit > 0:
                ccr = op_cash / net_profit
                cash_margin = op_cash / revenue * 100
                profit_margin = net_profit / revenue * 100
                st.markdown(f"""
                | Metric | Value | Interpretation |
                |--------|-------|----------------|
                | Cash Conversion Ratio | {ccr:.2f}x | {'✅ >1x: Good quality earnings' if ccr > 1 else '⚠️ <1x: Earnings not fully converting to cash'} |
                | Operating Cash Margin | {cash_margin:.1f}% | Cash generated per $ of revenue |
                | Net Profit Margin | {profit_margin:.1f}% | Profit per $ of revenue |
                | Cash vs Profit Gap | ${op_cash - net_profit:,}k | {'Cash exceeds profit (non-cash charges dominant)' if op_cash > net_profit else 'Profit exceeds cash (working capital build or accruals)'} |
                """)

    with tab4:
        st.header("Visualizations")

        st.subheader("Cash Flow Waterfall — Full Statement")
        items = ["Operating\nCash Flow", "Investing\nActivities", "Financing\nActivities", "FX Effect", "Net Change"]
        values = [6020, -4550, 1100, 30, 2600]
        colors = ["#34D399" if v >= 0 else "#F87171" for v in values]

        fig = go.Figure(go.Waterfall(
            name="Cash Flows", orientation="v",
            measure=["relative", "relative", "relative", "relative", "total"],
            x=items, y=values,
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            decreasing={"marker": {"color": "#F87171"}},
            increasing={"marker": {"color": "#34D399"}},
            totals={"marker": {"color": "#2563EB"}}
        ))
        fig.update_layout(title="Cash Flow Waterfall — XYZ Ltd 2024 ($000s)", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Operating vs Net Profit — Quality of Earnings")
        years = ["2020", "2021", "2022", "2023", "2024"]
        op_cash_vals = [3200, 4100, 5000, 5600, 6020]
        net_profit_vals = [2800, 3500, 4200, 4600, 4000]

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=years, y=op_cash_vals, name="Operating Cash Flow", marker_color="#2563EB"))
        fig2.add_trace(go.Bar(x=years, y=net_profit_vals, name="Net Profit", marker_color="#10B981"))
        fig2.update_layout(barmode="group", title="Cash Flow vs Profitability — 5-Year Trend ($000s)", height=400)
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Cash Flow Mix by Activity")
        fig3 = go.Figure(go.Pie(
            labels=["Operating", "Investing (outflows)", "Financing"],
            values=[6020, 4550, 1100],
            hole=0.4,
            marker_colors=["#2563EB", "#F87171", "#10B981"]
        ))
        fig3.update_layout(title="Cash Activity Distribution 2024", height=350)
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IAS 7, dividends paid may be classified as:**")
        q1 = st.radio("", [
            "Operating activities only",
            "Financing activities only",
            "Either operating or financing activities",
            "Either investing or financing activities"
        ], key="ias7q1")
        if st.button("Check Answer", key="ias7c1"):
            if q1 == "Either operating or financing activities":
                st.success("✅ Correct! IAS 7 allows dividends paid to be classified as either operating (as a cost of obtaining equity finance) or financing activities. The choice must be consistent.")
            else:
                st.error("❌ Incorrect. IAS 7 permits dividends paid to be classified as either operating OR financing activities.")

        st.markdown("---")
        st.markdown("**2. In the indirect method, an INCREASE in trade receivables is:**")
        q2 = st.radio("", [
            "Added to profit — it represents cash received",
            "Deducted from profit — cash collected was less than revenue",
            "Shown as an investing activity outflow",
            "Ignored — it is a non-cash item"
        ], key="ias7q2")
        if st.button("Check Answer", key="ias7c2"):
            if q2 == "Deducted from profit — cash collected was less than revenue":
                st.success("✅ Correct! An increase in receivables means revenue was recognised but not yet collected in cash — so cash flow is LESS than profit. Deduct from profit in the indirect method.")
            else:
                st.error("❌ Incorrect. Rising receivables means cash collected < revenue → deduct the increase from profit in the indirect method.")

        st.markdown("---")
        st.markdown("**3. An entity acquires $2M of equipment through a finance lease. How is this in the cash flow statement?**")
        q3 = st.radio("", [
            "Shown as an investing outflow of $2M",
            "Shown as a financing inflow of $2M",
            "Excluded from the cash flow statement; disclosed in notes as a non-cash transaction",
            "Shown as an operating outflow"
        ], key="ias7q3")
        if st.button("Check Answer", key="ias7c3"):
            if q3 == "Excluded from the cash flow statement; disclosed in notes as a non-cash transaction":
                st.success("✅ Correct! Non-cash investing and financing transactions (like leases) are excluded from the cash flow statement. They must be disclosed in the notes.")
            else:
                st.error("❌ Incorrect. Finance lease acquisition involves no cash — it is excluded from the statement and disclosed in notes as a non-cash transaction.")

        st.markdown("---")
        st.markdown("**4. The effect of exchange rate changes on cash held in foreign currencies should be:**")
        q4 = st.radio("", [
            "Included in operating activities",
            "Included in financing activities",
            "Excluded entirely from the cash flow statement",
            "Presented separately as a reconciling item to the movement in cash"
        ], key="ias7q4")
        if st.button("Check Answer", key="ias7c4"):
            if q4 == "Presented separately as a reconciling item to the movement in cash":
                st.success("✅ Correct! FX effects on cash cannot be classified as operating, investing or financing. IAS 7 requires them to be shown separately to reconcile opening and closing cash balances.")
            else:
                st.error("❌ Incorrect. FX differences on cash held are shown as a separate reconciling item — not within any of the three activity categories.")

        st.markdown("---")
        st.markdown("**5. Which method of presenting operating cash flows is ENCOURAGED (preferred) by IAS 7?**")
        q5 = st.radio("", [
            "Indirect method",
            "Direct method",
            "Either — IAS 7 has no preference",
            "Net method"
        ], key="ias7q5")
        if st.button("Check Answer", key="ias7c5"):
            if q5 == "Direct method":
                st.success("✅ Correct! IAS 7 encourages (but does not require) the direct method as it provides more useful information. However, the indirect method is more common in practice.")
            else:
                st.error("❌ Incorrect. IAS 7 encourages the direct method as it shows gross cash flows and is more informative, though both methods are permitted.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Three Categories of Cash Flows
        | Category | Content |
        |----------|---------|
        | **Operating** | Day-to-day business cash flows; profit adjusted for non-cash items and working capital |
        | **Investing** | Long-term asset purchases/sales, acquisitions, investment income |
        | **Financing** | Equity raised, debt borrowed/repaid, dividends paid |

        ### 2. Two Methods for Operating Cash Flows
        | Method | Approach | IAS 7 View |
        |--------|----------|------------|
        | Direct | Gross cash receipts and payments | Encouraged (preferred) |
        | Indirect | Profit + non-cash adjustments + WC changes | Common in practice |

        ### 3. Indirect Method — Key Adjustments
        ```
        Profit Before Tax
        + Depreciation & Amortisation
        + Impairment losses
        − Gains on disposal (+ losses)
        +/− Working capital changes (↑ receivables = minus; ↑ payables = plus)
        − Interest paid
        − Tax paid
        = Operating Cash Flow
        ```

        ### 4. Classification Flexibility
        - **Interest paid**: Operating OR Financing
        - **Interest received**: Operating OR Investing
        - **Dividends received**: Operating OR Investing
        - **Dividends paid**: Operating OR Financing
        - Must be **consistent** year to year

        ### 5. Exclusions & Disclosures
        - Non-cash transactions → excluded from statement; disclosed in notes
        - FX differences on cash → separate reconciling item
        - Tax → operating (unless specifically identifiable elsewhere)

        ### 6. Key Ratios
        ```
        Cash Conversion Ratio = Operating Cash Flow / Net Profit (target: >1x)
        Operating Cash Margin = Operating Cash Flow / Revenue
        Free Cash Flow = Operating Cash Flow − Capex
        ```
        """)

        st.success("🎓 **IAS 7 Complete!** You can now prepare and analyse the statement of cash flows under both direct and indirect methods.")
        st.info("💡 **Next**: IAS 8 — Accounting Policies, Changes in Accounting Estimates and Errors")

if __name__ == "__main__":
    show()