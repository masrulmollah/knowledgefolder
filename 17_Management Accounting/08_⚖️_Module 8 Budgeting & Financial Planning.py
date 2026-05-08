import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📋 Module 8: Budgeting & Financial Planning")
    st.markdown("*Build the complete master budget from sales forecast to financial statements*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. What Is a Budget?")
        st.markdown("""
        A **budget** is a detailed quantitative plan expressed in financial terms, prepared for a specific future period (usually one year, broken into months or quarters).

        #### Four Key Functions of Budgeting:
        | Function | Description |
        |----------|-------------|
        | **Planning** | Forces management to think ahead, set objectives, and anticipate problems |
        | **Coordination** | Ensures all departments work toward the same goals |
        | **Control** | Provides benchmarks to compare actual results against plan |
        | **Motivation** | Sets measurable targets that drive employee performance |
        """)

        st.subheader("2. The Master Budget — Complete Structure")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Operating Budgets (in order):**
            1. 🎯 **Sales Budget** ← START HERE
            2. Production Budget
            3. Direct Materials Budget
            4. Direct Labor Budget
            5. Manufacturing Overhead Budget
            6. Ending Inventory Budget
            7. Cost of Goods Sold Budget
            8. Selling & Admin Expense Budget
            """)
        with col2:
            st.markdown("""
            **Financial Budgets:**
            9. Cash Budget
            10. Budgeted Income Statement
            11. Budgeted Balance Sheet

            **Golden Rule:**
            Every budget flows from the **Sales Budget**.
            You cannot prepare any other budget until
            you have a sales forecast!
            """)

        st.subheader("3. Sales Budget")
        st.markdown("""
        The foundation of the entire master budget. Everything else depends on this.

        ```
        Budgeted Sales Units
        × Budgeted Selling Price per Unit
        ───────────────────────────────────
        = Budgeted Sales Revenue

        ──── Cash Collections Schedule ────
        Based on historical collection patterns.
        Example: 70% collected in month of sale,
                 25% next month, 5% two months later
        ```
        """)

        st.subheader("4. Production Budget")
        st.markdown("""
        Determines how many units must be produced to meet sales and inventory goals.

        ```
        Budgeted Sales (units)
        + Desired Ending Finished Goods Inventory
        − Beginning Finished Goods Inventory
        ──────────────────────────────────────────
        = Required Production (units)
        ```

        **Common Inventory Policy:** Ending inventory = X% of **next period's** budgeted sales
        """)

        st.subheader("5. Direct Materials Budget")
        st.markdown("""
        **Step 1 — Calculate Raw Materials Needed for Production:**
        ```
        Required Production (units)
        × Standard Raw Material per Unit (lbs, kg, etc.)
        ──────────────────────────────────────────────────
        = Total Production Needs (quantity)
        ```

        **Step 2 — Calculate Purchases:**
        ```
        Total Production Needs
        + Desired Ending Raw Materials Inventory
        − Beginning Raw Materials Inventory
        ──────────────────────────────────────────────────
        = Required Purchases (quantity)
        × Cost per Unit of Material
        = Total Purchase Cost ($)
        ```
        """)

        st.subheader("6. Direct Labor Budget")
        st.markdown("""
        ```
        Required Production (units)
        × Standard Direct Labor Hours per Unit
        ──────────────────────────────────────────────────
        = Total Direct Labor Hours Required
        × Standard Labor Rate per Hour ($)
        ──────────────────────────────────────────────────
        = Total Direct Labor Cost ($)
        ```
        """)

        st.subheader("7. Manufacturing Overhead Budget")
        st.markdown("""
        ```
        Variable Manufacturing Overhead:
          Budgeted DL Hours × Variable OH Rate per DLH  = Variable OH

        Fixed Manufacturing Overhead:                   = Fixed OH (set amount)

        Total Manufacturing Overhead = Variable OH + Fixed OH
        ```
        """)

        st.subheader("8. Cash Budget — The Most Critical Financial Budget")
        st.markdown("""
        Shows when cash will be available and when the company might need to borrow.

        ```
        Beginning Cash Balance
        + Total Cash Receipts (collections from customers)
        ──────────────────────────────────────────────────
        = Total Cash Available
        − Total Cash Disbursements:
            • Materials purchases
            • Labor payments
            • Overhead (cash items only)
            • S&A expenses
            • Capital expenditures
            • Loan repayments
            • Tax payments
        ──────────────────────────────────────────────────
        = Tentative Ending Cash Balance
        + Borrowings (if below minimum cash balance)
        − Loan Repayments (if excess cash available)
        ──────────────────────────────────────────────────
        = Ending Cash Balance  (must ≥ Minimum Required)
        ```
        """)

        st.subheader("9. Types of Budgets")
        budget_types = pd.DataFrame({
            "Budget Type": ["Static Budget", "Flexible Budget", "Rolling / Continuous Budget",
                             "Zero-Based Budget (ZBB)", "Activity-Based Budget (ABB)"],
            "Description": [
                "Prepared for ONE level of activity — never revised",
                "Adjusts to ACTUAL activity — better for performance comparison",
                "Always covers 12 months ahead; adds a new month as each month passes",
                "All expenses must be justified from scratch every period",
                "Budgets driven by activity cost drivers (connects to ABC costing)"
            ],
            "Best For": [
                "Initial planning and goal-setting",
                "Performance evaluation and variance analysis",
                "Continuous planning environments",
                "Cost reduction and efficiency drives",
                "Companies using activity-based costing"
            ]
        })
        st.dataframe(budget_types, use_container_width=True, hide_index=True)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Complete Master Budget Example — Sunrise Manufacturing (3 months)")
        st.markdown("""
        **Given Data:**
        | Item | Value |
        |------|-------|
        | Selling price per unit | $60 |
        | Sales forecast: Jan/Feb/Mar/Apr | 1,000 / 1,200 / 1,500 / 1,400 units |
        | Ending FG inventory policy | 20% of next month's sales |
        | Beginning FG inventory (Jan 1) | 200 units @ $28 cost |
        | Raw material needed per unit | 3 lbs |
        | Cost per lb of raw material | $4 |
        | Ending RM inventory policy | 10% of next month's production needs |
        | Beginning RM inventory | 312 lbs |
        | Direct labor per unit | 2 hours @ $15/hr |
        | Variable OH per DLH | $3 |
        | Fixed OH per month | $8,000 |
        | Variable S&A per unit sold | $2 |
        | Fixed S&A per month | $5,000 |
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **STEP 1 — Sales Budget:**
            ```
                      Jan      Feb      Mar    Q1 Total
            Units:   1,000    1,200    1,500     3,700
            × $60:  $60,000  $72,000  $90,000  $222,000
            ```

            **STEP 2 — Production Budget:**
            ```
                           Jan    Feb    Mar
            Sales Units   1,000  1,200  1,500
            + End FG Inv    240    300    280
            − Beg FG Inv   (200)  (240)  (300)
            ─────────────────────────────────
            Production    1,040  1,260  1,480
            ```
            End Inv Jan = 20% × 1,200 = 240
            End Inv Mar = 20% × 1,400 = 280
            """)
        with col2:
            st.markdown("""
            **STEP 3 — Direct Labor Budget:**
            ```
                       Jan     Feb     Mar
            Prod:     1,040   1,260   1,480
            × 2 hrs:  2,080   2,520   2,960
            × $15:   $31,200 $37,800 $44,400
            Q1 Total DL Cost: $113,400
            ```

            **STEP 4 — Manufacturing OH Budget:**
            ```
                        Jan      Feb      Mar
            Var OH:    $6,240   $7,560   $8,880
            Fixed OH:  $8,000   $8,000   $8,000
            ─────────────────────────────────────
            Total OH: $14,240  $15,560  $16,880
            Q1 Total OH: $46,680
            ```
            """)

        st.markdown("""
        **STEP 5 — Direct Materials Budget:**
        ```
                          Jan       Feb       Mar
        Production       1,040     1,260     1,480
        × 3 lbs/unit     3,120     3,780     4,440   Production needs
        + End RM Inv       378       444       xxx
        − Beg RM Inv      (312)     (378)     (444)
        ───────────────────────────────────────────
        Purchases (lbs)  3,186     3,846     xxx
        × $4/lb         $12,744   $15,384    xxx
        ```

        **STEP 6 — Budgeted Income Statement (Full Q1):**
        ```
        Sales (3,700 × $60)                         $222,000
        Cost of Goods Sold:
          DM (3,700 × 12)                            $44,400
          DL (3,700 × 30)                            $111,000
          OH                                          $46,680
          COGS                                       ($202,080)
        ──────────────────────────────────────────────────────
        Gross Margin                                   $19,920
        Variable S&A (3,700 × $2)                     ($7,400)
        Fixed S&A (3 × $5,000)                       ($15,000)
        ──────────────────────────────────────────────────────
        Net Operating Income (Loss)                   ($2,480)
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Budget Calculator:", [
            "📊 Sales Budget",
            "🏭 Production Budget",
            "🔩 Direct Materials Budget",
            "👷 Direct Labor Budget",
            "⚙️ Manufacturing Overhead Budget",
            "💵 Cash Budget",
            "📋 Complete Mini Master Budget"
        ])

        if calc_choice == "📊 Sales Budget":
            st.subheader("Sales Budget Calculator")
            num_periods = st.number_input("Number of Periods", 1, 12, 4)
            period_type = st.radio("Period Type", ["Monthly", "Quarterly"], horizontal=True)
            selling_price = st.number_input("Selling Price per Unit ($)", 0.0, value=60.0, step=1.0)

            units_per_period, period_labels = [], []
            for i in range(int(num_periods)):
                label = f"{'Month' if period_type == 'Monthly' else 'Quarter'} {i+1}"
                period_labels.append(label)
                u = st.number_input(f"{label} — Budgeted Units", 0, value=1000 + i * 200, step=50, key=f"sb_u_{i}")
                units_per_period.append(u)

            sales_revenues = [u * selling_price for u in units_per_period]
            total_units = sum(units_per_period)
            total_revenue = sum(sales_revenues)

            df = pd.DataFrame({
                "Period": period_labels,
                "Budgeted Units": [f"{u:,}" for u in units_per_period],
                "Selling Price": [f"${selling_price:.2f}"] * int(num_periods),
                "Sales Revenue": [f"${r:,.2f}" for r in sales_revenues],
                "% of Total": [f"{r/total_revenue*100:.1f}%" for r in sales_revenues]
            })
            st.dataframe(df, use_container_width=True, hide_index=True)

            col1, col2 = st.columns(2)
            with col1: st.metric("Total Budgeted Units", f"{total_units:,}")
            with col2: st.metric("Total Budgeted Revenue", f"${total_revenue:,.2f}")

            fig = go.Figure(go.Bar(
                x=period_labels, y=sales_revenues,
                marker_color="#2E86C1",
                text=[f"${r:,.0f}" for r in sales_revenues], textposition="auto"
            ))
            fig.update_layout(title="Budgeted Sales Revenue by Period", yaxis_title="Sales ($)")
            st.plotly_chart(fig, use_container_width=True)

        elif calc_choice == "🏭 Production Budget":
            st.subheader("Production Budget Calculator")
            num_periods = st.number_input("Number of Periods", 1, 12, 4)
            end_inv_pct = st.number_input("Ending FG Inventory Policy (% of next period's sales)", 0.0, 100.0, 20.0)

            sales_forecasts = []
            for i in range(int(num_periods) + 1):
                label = f"Period {i+1} Sales" if i < int(num_periods) else "Next Period Sales (for ending inv)"
                s = st.number_input(label, 0, value=1000 + i * 200, step=50, key=f"pb_s_{i}")
                sales_forecasts.append(s)

            beg_inv_p1 = st.number_input("Beginning Inventory — Period 1 Only (units)", 0, value=200, step=10)

            rows, beg = [], beg_inv_p1
            for i in range(int(num_periods)):
                end_inv = int(sales_forecasts[i + 1] * end_inv_pct / 100)
                production = sales_forecasts[i] + end_inv - beg
                rows.append({
                    "Period": f"P{i+1}", "Budgeted Sales": f"{sales_forecasts[i]:,}",
                    "+ Desired End Inv": f"{end_inv:,}", "− Beg Inv": f"({beg:,})",
                    "Required Production": f"{production:,}"
                })
                beg = end_inv

            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            total_prod = sum([int(r["Required Production"].replace(",", "")) for r in rows])
            st.metric("Total Production Required", f"{total_prod:,} units")

        elif calc_choice == "🔩 Direct Materials Budget":
            st.subheader("Direct Materials Budget Calculator")
            num_periods = st.number_input("Number of Periods", 1, 6, 3)
            mat_per_unit = st.number_input("Raw Material per Unit (lbs/kg/etc.)", 0.0, value=3.0, step=0.5)
            cost_per_unit_mat = st.number_input("Cost per Unit of Material ($)", 0.0, value=4.0, step=0.1)
            end_rm_pct = st.number_input("Ending RM Inventory (% of next period's production needs)", 0.0, 100.0, 10.0)

            productions = []
            for i in range(int(num_periods) + 1):
                label = f"Period {i+1} Production" if i < int(num_periods) else "Next Period Production"
                p = st.number_input(label, 0, value=1000 + i * 200, step=50, key=f"dm_p_{i}")
                productions.append(p)

            beg_rm = st.number_input("Beginning RM Inventory (units)", 0.0, value=312.0, step=10.0)

            rows, beg = [], beg_rm
            for i in range(int(num_periods)):
                prod_need = productions[i] * mat_per_unit
                end_rm = productions[i + 1] * mat_per_unit * end_rm_pct / 100
                purchases_qty = prod_need + end_rm - beg
                purchase_cost = purchases_qty * cost_per_unit_mat
                rows.append({
                    "Period": f"P{i+1}", "Production": productions[i],
                    "Prod Needs (units)": f"{prod_need:,.0f}",
                    "+ End RM Inv": f"{end_rm:,.0f}", "− Beg RM Inv": f"({beg:,.0f})",
                    "Purchases (qty)": f"{purchases_qty:,.0f}",
                    "Purchase Cost": f"${purchase_cost:,.2f}"
                })
                beg = end_rm

            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

        elif calc_choice == "👷 Direct Labor Budget":
            st.subheader("Direct Labor Budget Calculator")
            num_periods = st.number_input("Number of Periods", 1, 12, 3)
            dlh_per_unit = st.number_input("Standard DL Hours per Unit", 0.0, value=2.0, step=0.25)
            dl_rate = st.number_input("DL Rate per Hour ($)", 0.0, value=15.0, step=0.5)

            productions = []
            for i in range(int(num_periods)):
                p = st.number_input(f"Period {i+1} Production (units)", 0, value=1000 + i * 200, step=50, key=f"dl_p_{i}")
                productions.append(p)

            total_dlh = [p * dlh_per_unit for p in productions]
            dl_costs = [h * dl_rate for h in total_dlh]

            df = pd.DataFrame({
                "Period": [f"P{i+1}" for i in range(int(num_periods))],
                "Production (units)": [f"{p:,}" for p in productions],
                "DLH/Unit": [f"{dlh_per_unit:.2f}"] * int(num_periods),
                "Total DLH": [f"{h:,.0f}" for h in total_dlh],
                "Rate/Hr": [f"${dl_rate:.2f}"] * int(num_periods),
                "Total DL Cost": [f"${c:,.2f}" for c in dl_costs]
            })
            st.dataframe(df, use_container_width=True, hide_index=True)

            col1, col2 = st.columns(2)
            with col1: st.metric("Total DL Hours", f"{sum(total_dlh):,.0f} hrs")
            with col2: st.metric("Total DL Cost", f"${sum(dl_costs):,.2f}")

        elif calc_choice == "⚙️ Manufacturing Overhead Budget":
            st.subheader("Manufacturing Overhead Budget Calculator")
            num_periods = st.number_input("Number of Periods", 1, 12, 3)
            var_oh_rate = st.number_input("Variable OH Rate per DLH ($)", 0.0, value=3.0, step=0.5)
            fixed_oh_per_period = st.number_input("Fixed OH per Period ($)", 0.0, value=8000.0, step=500.0)

            dlh_list = []
            for i in range(int(num_periods)):
                dlh = st.number_input(f"Period {i+1} Total DLH", 0.0, value=2000.0 + i * 200, step=100.0, key=f"oh_dlh_{i}")
                dlh_list.append(dlh)

            var_oh_list = [dlh * var_oh_rate for dlh in dlh_list]
            total_oh_list = [v + fixed_oh_per_period for v in var_oh_list]

            df = pd.DataFrame({
                "Period": [f"P{i+1}" for i in range(int(num_periods))],
                "Total DLH": [f"{h:,.0f}" for h in dlh_list],
                "Variable OH": [f"${v:,.2f}" for v in var_oh_list],
                "Fixed OH": [f"${fixed_oh_per_period:,.2f}"] * int(num_periods),
                "Total OH": [f"${t:,.2f}" for t in total_oh_list]
            })
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.metric("Total Budgeted OH", f"${sum(total_oh_list):,.2f}")

        elif calc_choice == "💵 Cash Budget":
            st.subheader("Cash Budget Calculator")
            num_months = st.number_input("Number of Months", 1, 12, 3)
            beg_cash = st.number_input("Beginning Cash Balance ($)", 0.0, value=50000.0, step=1000.0)
            min_cash_bal = st.number_input("Minimum Required Cash Balance ($)", 0.0, value=30000.0, step=1000.0)

            st.markdown("### Monthly Cash Flows:")
            receipts_list, disbursements_list = [], []
            for i in range(int(num_months)):
                st.markdown(f"**Month {i+1}:**")
                col1, col2 = st.columns(2)
                with col1:
                    r = st.number_input("Cash Receipts ($)", 0.0, value=80000.0, step=1000.0, key=f"cb_r_{i}")
                with col2:
                    d = st.number_input("Cash Disbursements ($)", 0.0, value=75000.0, step=1000.0, key=f"cb_d_{i}")
                receipts_list.append(r)
                disbursements_list.append(d)

            if st.button("🧮 Build Cash Budget", type="primary"):
                st.markdown("---")
                st.markdown("### Cash Budget Results:")
                rows = []
                beg = beg_cash
                total_borrowed = 0

                for i in range(int(num_months)):
                    avail = beg + receipts_list[i]
                    tentative = avail - disbursements_list[i]
                    borrow = max(0, min_cash_bal - tentative)
                    end = tentative + borrow
                    total_borrowed += borrow

                    rows.append({
                        "Month": f"Month {i+1}",
                        "Beg Cash": f"${beg:,.2f}",
                        "+ Receipts": f"${receipts_list[i]:,.2f}",
                        "= Cash Available": f"${avail:,.2f}",
                        "− Disbursements": f"(${disbursements_list[i]:,.2f})",
                        "Tentative End": f"${tentative:,.2f}",
                        "+ Borrowings": f"${borrow:,.2f}",
                        "Ending Cash": f"${end:,.2f}"
                    })
                    beg = end

                st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

                col1, col2 = st.columns(2)
                with col1: st.metric("Ending Cash Balance", f"${beg:,.2f}")
                with col2: st.metric("Total Borrowings Required", f"${total_borrowed:,.2f}")

                if total_borrowed > 0:
                    st.warning(f"⚠️ Total borrowing needed: ${total_borrowed:,.2f} — arrange credit line in advance!")
                else:
                    st.success("✅ No borrowing needed — strong cash position throughout the period!")

        else:  # Complete Mini Master Budget
            st.subheader("Complete Mini Master Budget")
            st.markdown("### Enter All Data:")

            col1, col2, col3 = st.columns(3)
            with col1:
                price = st.number_input("Selling Price ($/unit)", 0.0, value=60.0, step=1.0)
                sales = st.number_input("Budgeted Sales (units)", 0, value=1000, step=50)
                end_fg_pct = st.number_input("End FG Inv % next period", 0.0, value=20.0)
                next_per_sales = st.number_input("Next Period Sales (for end inv)", 0, value=1200, step=50)
                beg_fg = st.number_input("Beginning FG Inventory (units)", 0, value=200, step=10)

            with col2:
                dm_per_unit = st.number_input("Raw Material/unit", 0.0, value=3.0, step=0.5)
                dm_cost = st.number_input("Material Cost/unit ($)", 0.0, value=4.0, step=0.1)
                dl_per_unit = st.number_input("DL Hours/unit", 0.0, value=2.0, step=0.25)
                dl_rate = st.number_input("DL Rate/hr ($)", 0.0, value=15.0, step=0.5)

            with col3:
                var_oh_dlh = st.number_input("Variable OH/DLH ($)", 0.0, value=3.0, step=0.5)
                fixed_oh = st.number_input("Fixed OH ($)", 0.0, value=8000.0, step=500.0)
                var_sa = st.number_input("Variable S&A/unit sold ($)", 0.0, value=2.0, step=0.5)
                fixed_sa = st.number_input("Fixed S&A ($)", 0.0, value=5000.0, step=500.0)

            if st.button("🧮 Build Master Budget", type="primary"):
                # Production
                end_fg = int(next_per_sales * end_fg_pct / 100)
                production = sales + end_fg - beg_fg

                # DM
                dm_total = production * dm_per_unit * dm_cost

                # DL
                dl_hrs = production * dl_per_unit
                dl_cost = dl_hrs * dl_rate

                # OH
                var_oh_total = dl_hrs * var_oh_dlh
                total_oh = var_oh_total + fixed_oh
                oh_rate = total_oh / production if production > 0 else 0

                # Unit cost
                unit_cost = dm_cost * dm_per_unit + dl_rate * dl_per_unit + oh_rate

                # Income statement
                cogs = sales * unit_cost
                gross_margin = sales * price - cogs
                sa_exp = sales * var_sa + fixed_sa
                net_income = gross_margin - sa_exp

                st.markdown("---")
                st.markdown("### Budget Results:")

                col1, col2 = st.columns(2)
                with col1:
                    budget_summary = pd.DataFrame({
                        "Budget Item": ["Budgeted Sales", "Required Production", "Total DM Cost",
                                         "Total DL Cost", "Total OH", "Unit Product Cost"],
                        "Amount": [f"{sales:,} units", f"{production:,} units", f"${dm_total:,.2f}",
                                    f"${dl_cost:,.2f}", f"${total_oh:,.2f}", f"${unit_cost:.2f}"]
                    })
                    st.dataframe(budget_summary, use_container_width=True, hide_index=True)

                with col2:
                    st.markdown("**Budgeted Income Statement:**")
                    st.markdown(f"""
                    ```
                    Sales ({sales:,} × ${price:.2f})      ${sales*price:,.2f}
                    COGS ({sales:,} × ${unit_cost:.2f})   (${cogs:,.2f})
                    ──────────────────────────────────
                    Gross Margin                ${gross_margin:,.2f}
                    S&A Expenses               (${sa_exp:,.2f})
                    ──────────────────────────────────
                    Net Operating Income        ${net_income:,.2f}
                    ══════════════════════════════════
                    ```
                    """)

                if net_income > 0:
                    st.success(f"✅ Budget shows profit of ${net_income:,.2f}")
                else:
                    st.error(f"❌ Budget shows a loss of ${abs(net_income):,.2f} — review pricing or cost structure!")

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Quarterly Sales Budget")
        quarters = ["Q1", "Q2", "Q3", "Q4"]
        sales_vals = [500000, 620000, 750000, 680000]
        fig1 = go.Figure(go.Bar(
            x=quarters, y=sales_vals,
            marker_color=["#2E86C1", "#27AE60", "#E67E22", "#8E44AD"],
            text=[f"${v:,.0f}" for v in sales_vals], textposition="auto"
        ))
        fig1.update_layout(title="Annual Sales Budget by Quarter", xaxis_title="Quarter", yaxis_title="Sales ($)")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Monthly Cash Budget Projection")
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        cash_in = [80000, 92000, 110000, 98000, 105000, 118000]
        cash_out = [75000, 88000, 95000, 102000, 90000, 108000]
        net_flow = [i - o for i, o in zip(cash_in, cash_out)]

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=months, y=cash_in, name="Cash Inflows", marker_color="#27AE60"))
        fig2.add_trace(go.Bar(x=months, y=cash_out, name="Cash Outflows", marker_color="#E74C3C"))
        fig2.add_trace(go.Scatter(x=months, y=net_flow, name="Net Cash Flow",
                                   mode="lines+markers", line=dict(color="navy", width=3), marker=dict(size=8)))
        fig2.add_hline(y=0, line_dash="dash", line_color="black")
        fig2.update_layout(title="6-Month Cash Flow Projection", barmode="group", yaxis_title="Amount ($)")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Cost Budget Composition")
        cost_data = pd.DataFrame({
            "Category": ["Direct Materials", "Direct Labor", "Variable OH", "Fixed OH", "Variable S&A", "Fixed S&A"],
            "Amount": [180000, 120000, 75000, 96000, 30000, 60000]
        })
        fig3 = px.pie(cost_data, values="Amount", names="Category",
                      title="Total Budgeted Cost Structure",
                      color_discrete_sequence=["#2E86C1","#27AE60","#E67E22","#8E44AD","#E74C3C","#95A5A6"])
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Master Budget Flow Diagram")
        fig4 = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15, thickness=20,
                label=["Sales Budget", "Production Budget", "DM Budget", "DL Budget",
                       "OH Budget", "Ending Inv Budget", "COGS Budget", "S&A Budget",
                       "Cash Budget", "Income Stmt", "Balance Sheet"],
                color=["#E74C3C","#E67E22","#F1C40F","#27AE60","#2ECC71","#1ABC9C",
                        "#3498DB","#9B59B6","#2E86C1","#1A5276","#0E3460"]
            ),
            link=dict(
                source=[0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 9],
                target=[1, 7, 2, 3, 4, 6, 6, 6, 6, 8, 8, 10],
                value=[50, 30, 30, 30, 30, 20, 20, 20, 20, 40, 20, 40]
            )
        )])
        fig4.update_layout(title="Master Budget Flow", height=500)
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. The FIRST budget prepared in the master budget process is:**")
        q1 = st.radio("", [
            "Production budget — must know what to make",
            "Sales budget — everything flows from sales",
            "Cash budget — cash is most important",
            "Ending inventory budget — needed for production"
        ], key="m8q1")
        if st.button("Check Q1", key="m8c1"):
            if q1 == "Sales budget — everything flows from sales":
                st.success("✅ Correct! The Sales Budget is ALWAYS first. All other budgets depend on the sales forecast.")
            else:
                st.error("❌ Incorrect. The Sales Budget must be prepared first because ALL other budgets flow from it.")

        st.markdown("---")
        st.markdown("**Q2. Production Budget formula — Required Production = Sales + End FG Inventory minus ?**")
        q2 = st.radio("", [
            "Next period's sales",
            "Beginning Finished Goods Inventory",
            "Raw materials used",
            "Total factory overhead"
        ], key="m8q2")
        if st.button("Check Q2", key="m8c2"):
            if q2 == "Beginning Finished Goods Inventory":
                st.success("✅ Correct! Production = Sales + Desired End FG Inv − Beginning FG Inv")
            else:
                st.error("❌ Incorrect. Production = Sales + Ending FG Inv − Beginning FG Inv")

        st.markdown("---")
        st.markdown("""
        **Q3. Sales = 6,000 units. Desired ending inventory = 800 units. Beginning inventory = 500 units.
        Required production = ?**
        """)
        q3 = st.radio("", ["5,700 units", "6,000 units", "6,300 units", "7,300 units"], key="m8q3")
        if st.button("Check Q3", key="m8c3"):
            if q3 == "6,300 units":
                st.success("✅ Correct! 6,000 + 800 − 500 = 6,300 units")
            else:
                st.error("❌ Incorrect. 6,000 + 800 − 500 = 6,300 units")

        st.markdown("---")
        st.markdown("**Q4. The PRIMARY benefit of a cash budget is:**")
        q4 = st.radio("", [
            "It maximises company profits automatically",
            "It shows customer payment history",
            "It reveals future cash shortfalls BEFORE they happen",
            "It replaces the need for financial accounting"
        ], key="m8q4")
        if st.button("Check Q4", key="m8c4"):
            if q4 == "It reveals future cash shortfalls BEFORE they happen":
                st.success("✅ Correct! The cash budget allows management to arrange financing in advance.")
            else:
                st.error("❌ Incorrect. The cash budget's key benefit is identifying future cash shortfalls before they occur.")

        st.markdown("---")
        st.markdown("**Q5. Zero-Based Budgeting (ZBB) requires:**")
        q5 = st.radio("", [
            "Budget starts at zero profit",
            "Every expense justified from scratch each period",
            "Using last year's budget as the starting point",
            "Budget must equal exactly zero at year end"
        ], key="m8q5")
        if st.button("Check Q5", key="m8c5"):
            if q5 == "Every expense justified from scratch each period":
                st.success("✅ Correct! ZBB forces managers to justify every budget line item from zero — no automatic rollovers.")
            else:
                st.error("❌ Incorrect. ZBB means justifying every expense from scratch each period — nothing is automatically approved based on prior years.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Master Budget Sequence")
        st.markdown("""
        ```
        ┌─────────────────────────────────────────────────────────┐
        │  1. SALES BUDGET  ← Always First!                       │
        └─────────────────────────┬───────────────────────────────┘
                                   ↓
        ┌─────────────────────────────────────────────────────────┐
        │  2. PRODUCTION BUDGET                                    │
        └──────┬──────────────────┬──────────────────┬────────────┘
               ↓                  ↓                  ↓
          3. DM Budget      4. DL Budget      5. OH Budget
               ↓                  ↓                  ↓
        ┌─────────────────────────────────────────────────────────┐
        │  6. Ending Inventory Budget → 7. COGS Budget             │
        └─────────────────────────────────────────────────────────┘
                                   +
               8. Selling & Admin Expense Budget
                                   ↓
        ┌─────────────────────────────────────────────────────────┐
        │  9. CASH BUDGET                                          │
        └─────────────────────────────────────────────────────────┘
                                   ↓
                      10. Budgeted Income Statement
                                   ↓
                       11. Budgeted Balance Sheet
        ```
        """)

        st.subheader("🎯 Key Budget Formulas")
        formulas_df = pd.DataFrame({
            "Budget": ["Production", "DM Purchases", "DL Cost", "Variable OH", "Cash Available", "Ending Cash"],
            "Formula": [
                "Sales + Desired Ending FG Inv − Beginning FG Inv",
                "(Prod Needs + End RM Inv − Beg RM Inv) × Cost per unit",
                "Production × DLH/unit × Rate/hr",
                "Budgeted DLH × Variable OH Rate per DLH",
                "Beginning Cash Balance + All Cash Receipts",
                "Cash Available − All Cash Disbursements ± Financing"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Budget Types Comparison")
        types_df = pd.DataFrame({
            "Type": ["Static Budget", "Flexible Budget", "Rolling Budget", "Zero-Based (ZBB)", "Activity-Based (ABB)"],
            "Key Feature": [
                "One fixed activity level", "Adjusts to actual activity", "Always extends 12 months",
                "All costs re-justified", "Driven by cost drivers"
            ],
            "Primary Use": [
                "Initial planning", "Performance evaluation", "Continuous planning",
                "Cost control", "ABC environments"
            ]
        })
        st.dataframe(types_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Budgeting Mistakes")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Starting with the production budget (not sales)",
                "Forgetting timing differences in cash receipts",
                "Ignoring beginning inventory in production/DM budgets",
                "Not including all cash items in cash budget",
                "Building in budgetary slack (padding budgets)",
                "Using prior year budget without justification"
            ],
            "Correct Approach": [
                "ALWAYS start with Sales Budget — it drives everything",
                "Sales ≠ cash collected; build a collections schedule",
                "Production = Sales + End Inv − Beginning Inv (not just Sales)",
                "Include capital expenditures, loan payments, taxes",
                "Challenge all budget requests — not just new spending",
                "Use ZBB periodically to eliminate unnecessary costs"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 8 Complete! You can now build a complete master budget from scratch.")
        st.info("💡 Next: Module 9 — Standard Costing & Variance Analysis")

if __name__ == "__main__":
    show()