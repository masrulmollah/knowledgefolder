import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📊 Module 7: Variable Costing vs Absorption Costing")
    st.markdown("*Understand income differences, reconciliation, and when each method applies*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. The Only Difference Between the Two Methods")
        st.markdown("""
        Both methods treat **Direct Materials, Direct Labor, and Variable Manufacturing Overhead** 
        identically as product costs. The **one and only** difference is the treatment of 
        **Fixed Manufacturing Overhead**.
        """)
        diff_df = pd.DataFrame({
            "Cost Type": [
                "Direct Materials", "Direct Labor", "Variable Mfg Overhead",
                "⭐ Fixed Mfg Overhead", "Variable S&A Expenses", "Fixed S&A Expenses"
            ],
            "Absorption Costing": [
                "Product Cost", "Product Cost", "Product Cost",
                "✅ Product Cost (INVENTORIED)", "Period Cost", "Period Cost"
            ],
            "Variable Costing": [
                "Product Cost", "Product Cost", "Product Cost",
                "❌ Period Cost (EXPENSED NOW)", "Period Cost", "Period Cost"
            ]
        })
        st.dataframe(diff_df, use_container_width=True, hide_index=True)
        st.info("⭐ **The ONLY difference:** Fixed Manufacturing Overhead is a product cost under Absorption and a period cost under Variable.")

        st.subheader("2. Unit Product Cost Calculation")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Absorption Costing — Unit Cost:**
            ```
            Direct Materials              $XX
            Direct Labor                  $XX
            Variable Mfg Overhead         $XX
            Fixed Mfg Overhead / Unit     $XX  ← Included!
            ────────────────────────────────
            Total Unit Product Cost       $XX

            Fixed OH Rate per Unit =
            Total Fixed Mfg OH / Units Produced
            ```
            """)
        with col2:
            st.markdown("""
            **Variable Costing — Unit Cost:**
            ```
            Direct Materials              $XX
            Direct Labor                  $XX
            Variable Mfg Overhead         $XX
            Fixed Mfg Overhead            N/A  ← Excluded!
            ────────────────────────────────
            Total Unit Product Cost       $XX
                          (lower amount)

            Fixed OH expensed in FULL
            as a period cost regardless
            of units produced/sold
            ```
            """)

        st.subheader("3. Income Statement Formats")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Absorption Costing Format:**
            ```
            Sales Revenue
            − Cost of Goods Sold
              (DM + DL + Var OH + Fixed OH)
            ─────────────────────────────────
            Gross Margin          ← Key subtotal
            − Selling & Admin Expenses
              (both variable and fixed)
            ─────────────────────────────────
            Net Operating Income
            ```
            """)
        with col2:
            st.markdown("""
            **Variable Costing Format:**
            ```
            Sales Revenue
            − Variable Expenses:
              • Variable COGS (DM+DL+VarOH)
              • Variable S&A
            ─────────────────────────────────
            Contribution Margin   ← Key subtotal
            − Fixed Expenses:
              • Fixed Mfg Overhead
              • Fixed S&A
            ─────────────────────────────────
            Net Operating Income
            ```
            """)

        st.subheader("4. Income Reconciliation")
        st.markdown("""
        The **only** reason income differs between methods is fixed manufacturing overhead in inventory.

        ```
        Variable Costing Net Income
        + Fixed OH in Ending Inventory    [ending units × fixed OH rate/unit]
        − Fixed OH in Beginning Inventory [beginning units × fixed OH rate/unit]
        ──────────────────────────────────────────────────────────────────────────
        = Absorption Costing Net Income

        ─── SHORTCUT ───
        Income Difference = Inventory Change (units) × Fixed OH Rate per Unit
        ```

        | Production vs Sales | Inventory Change | Absorption Income vs Variable |
        |---------------------|-----------------|-------------------------------|
        | Production = Sales | No change | **Equal** |
        | Production > Sales | Increases | **Absorption HIGHER** (fixed OH deferred) |
        | Production < Sales | Decreases | **Absorption LOWER** (fixed OH released) |
        """)

        st.subheader("5. Advantages & Disadvantages")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Absorption Costing:**
            ✅ Required by GAAP (external reports)
            ✅ Required for income tax reporting
            ✅ Full product cost for long-term pricing
            ✅ Matches all production costs to revenue
            ❌ Income manipulable via overproduction
            ❌ Fixed cost per unit changes with volume
            ❌ Obscures cost behavior (variable vs fixed)
            ❌ Not suitable for CVP analysis
            """)
        with col2:
            st.markdown("""
            **Variable Costing:**
            ✅ Income tracks SALES (not production)
            ✅ Better for internal decisions
            ✅ CVP analysis works perfectly
            ✅ No incentive to overproduce
            ✅ Consistent unit cost regardless of volume
            ✅ Shows contribution margin clearly
            ❌ Not acceptable for GAAP reporting
            ❌ Not acceptable for tax returns
            ❌ May understate costs for pricing
            """)

        st.subheader("6. When to Use Each Method")
        use_df = pd.DataFrame({
            "Purpose": [
                "External financial statements", "Tax reporting", "Internal management reports",
                "CVP and break-even analysis", "Segment performance evaluation",
                "Short-term pricing decisions", "Long-term pricing decisions"
            ],
            "Recommended": [
                "Absorption ✅", "Absorption ✅", "Variable ✅",
                "Variable ✅", "Variable ✅", "Variable ✅", "Absorption ✅"
            ],
            "Reason": [
                "GAAP requirement", "IRS requirement", "Shows true cost behaviour",
                "Fixed costs treated separately", "Income tracks sales performance",
                "Marginal cost pricing", "Must recover all costs"
            ]
        })
        st.dataframe(use_df, use_container_width=True, hide_index=True)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Complete Side-by-Side Income Statements")
        st.markdown("""
        **Given Data:**
        | Item | Value |
        |------|-------|
        | Units Produced | 10,000 |
        | Units Sold | 8,000 |
        | Beginning Inventory | 0 units |
        | Selling Price | $50/unit |
        | Variable Manufacturing Cost | $20/unit |
        | Fixed Manufacturing Overhead | $100,000 total |
        | Variable Selling & Admin | $5/unit sold |
        | Fixed Selling & Admin | $40,000 total |

        **Derived Values:**
        ```
        Fixed OH Rate = $100,000 / 10,000 units = $10/unit
        Absorption Unit Cost = $20 + $10 = $30/unit
        Variable Unit Cost   = $20/unit
        Ending Inventory     = 10,000 − 8,000 = 2,000 units
        ```
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Absorption Costing Income Statement:**
            ```
            Sales (8,000 × $50)            $400,000
            ─────────────────────────────────────────
            Cost of Goods Sold:
              Beg Inventory            $        0
              + Production (10,000×$30)  $300,000
              − End Inv (2,000 × $30)    ($60,000)
              COGS                      ($240,000)
            ─────────────────────────────────────────
            Gross Margin                $160,000
            ─────────────────────────────────────────
            Variable S&A (8,000×$5)     ($40,000)
            Fixed S&A                   ($40,000)
            ─────────────────────────────────────────
            Net Operating Income         $80,000
            ═════════════════════════════════════════
            ```
            """)
        with col2:
            st.markdown("""
            **Variable Costing Income Statement:**
            ```
            Sales (8,000 × $50)            $400,000
            ─────────────────────────────────────────
            Variable Costs:
              Variable COGS (8,000×$20)  ($160,000)
              Variable S&A  (8,000×$5)    ($40,000)
            ─────────────────────────────────────────
            Contribution Margin          $200,000
            ─────────────────────────────────────────
            Fixed Manufacturing OH      ($100,000)
            Fixed S&A                    ($40,000)
            ─────────────────────────────────────────
            Net Operating Income         $60,000
            ═════════════════════════════════════════
            ```
            """)

        st.markdown("""
        **Reconciliation:**
        ```
        Variable Costing Income                              $60,000
        + Fixed OH in Ending Inventory (2,000 × $10)        +$20,000
        − Fixed OH in Beg Inventory (0 × $10)               −$0
        ─────────────────────────────────────────────────────────────
        Absorption Costing Income                            $80,000  ✓

        Shortcut: 2,000 unit inventory increase × $10/unit = $20,000 difference
        ```
        """)

        st.subheader("Example 2: Three-Year Analysis — Variable Costing Income is Stable!")
        years_df = pd.DataFrame({
            "Year": ["Year 1", "Year 2", "Year 3", "Total"],
            "Produced": ["10,000", "8,000", "12,000", "30,000"],
            "Sold": ["8,000", "10,000", "10,000", "28,000"],
            "Inventory Change": ["+2,000", "−2,000", "+2,000", "+2,000"],
            "Absorption NOI": ["$80,000", "$45,000", "$86,667", "$211,667"],
            "Variable NOI": ["$60,000", "$80,000", "$80,000", "$220,000"],
            "Which Higher?": ["Absorption +$20K", "Variable +$35K", "Absorption +$6.7K", "Variable higher overall"]
        })
        st.dataframe(years_df, use_container_width=True, hide_index=True)
        st.info("💡 **Key Insight:** Variable costing income moves in lockstep with **sales**. Absorption income fluctuates with production changes. Variable costing is a truer performance measure!")

    with tab3:
        st.header("💡 Interactive Calculators")
        st.subheader("🧮 Complete Absorption vs Variable Costing Calculator")

        st.markdown("### Enter Production & Sales Data:")
        col1, col2, col3 = st.columns(3)
        with col1:
            beg_inv = st.number_input("Beginning Inventory (units)", min_value=0, value=0, step=100)
            production = st.number_input("Units Produced", min_value=1, value=10000, step=100)
            sales_units = st.number_input("Units Sold", min_value=0, value=8000, step=100)
        with col2:
            selling_price = st.number_input("Selling Price ($/unit)", min_value=0.0, value=50.0, step=1.0)
            var_mfg = st.number_input("Variable Mfg Cost ($/unit)", min_value=0.0, value=20.0, step=1.0)
            var_sa = st.number_input("Variable S&A ($/unit sold)", min_value=0.0, value=5.0, step=0.5)
        with col3:
            fixed_mfg = st.number_input("Fixed Mfg Overhead ($)", min_value=0.0, value=100000.0, step=1000.0)
            fixed_sa = st.number_input("Fixed S&A ($)", min_value=0.0, value=40000.0, step=1000.0)

        ending_inv = beg_inv + production - sales_units

        # ── Absorption calculations ──
        foh_rate = fixed_mfg / production if production > 0 else 0
        abs_unit_cost = var_mfg + foh_rate
        abs_cogs = sales_units * abs_unit_cost
        abs_gross_margin = sales_units * selling_price - abs_cogs
        abs_sa_total = sales_units * var_sa + fixed_sa
        abs_income = abs_gross_margin - abs_sa_total
        abs_end_inv_value = ending_inv * abs_unit_cost
        abs_beg_inv_value = beg_inv * abs_unit_cost

        # ── Variable calculations ──
        var_cogs = sales_units * var_mfg
        var_sa_total = sales_units * var_sa
        cm = sales_units * selling_price - var_cogs - var_sa_total
        cm_ratio = cm / (sales_units * selling_price) * 100 if sales_units > 0 else 0
        var_income = cm - fixed_mfg - fixed_sa
        var_end_inv_value = ending_inv * var_mfg

        # ── Reconciliation ──
        foh_ending = ending_inv * foh_rate
        foh_beginning = beg_inv * foh_rate
        inv_change = ending_inv - beg_inv
        recon_result = var_income + foh_ending - foh_beginning

        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📋 Absorption Costing Income Statement")
            st.markdown(f"""
            ```
            Sales ({sales_units:,} × ${selling_price:.2f})
                                         ${sales_units*selling_price:,.2f}
            ────────────────────────────────────────────
            Cost of Goods Sold:
              Beg Inventory ({beg_inv:,} × ${abs_unit_cost:.2f})
                                         ${abs_beg_inv_value:,.2f}
              + Production ({production:,} × ${abs_unit_cost:.2f})
                                         ${production*abs_unit_cost:,.2f}
              − End Inv ({ending_inv:,} × ${abs_unit_cost:.2f})
                                        (${abs_end_inv_value:,.2f})
              ─────────────────────────────────────────
              COGS                      (${abs_cogs:,.2f})
            ────────────────────────────────────────────
            Gross Margin                 ${abs_gross_margin:,.2f}
            ────────────────────────────────────────────
            Variable S&A ({sales_units:,}×${var_sa:.2f})
                                        (${sales_units*var_sa:,.2f})
            Fixed S&A                   (${fixed_sa:,.2f})
            ────────────────────────────────────────────
            Net Operating Income         ${abs_income:,.2f}
            ════════════════════════════════════════════
            Unit product cost: ${abs_unit_cost:.2f}
            Ending inv value:  ${abs_end_inv_value:,.2f}
            ```
            """)

        with col2:
            st.markdown("### 📋 Variable Costing Income Statement")
            st.markdown(f"""
            ```
            Sales ({sales_units:,} × ${selling_price:.2f})
                                         ${sales_units*selling_price:,.2f}
            ────────────────────────────────────────────
            Variable Costs:
              Var COGS ({sales_units:,} × ${var_mfg:.2f})
                                        (${var_cogs:,.2f})
              Var S&A ({sales_units:,} × ${var_sa:.2f})
                                        (${var_sa_total:,.2f})
            ────────────────────────────────────────────
            Contribution Margin          ${cm:,.2f}
            CM Ratio: {cm_ratio:.1f}%
            ────────────────────────────────────────────
            Fixed Mfg Overhead          (${fixed_mfg:,.2f})
            Fixed S&A                   (${fixed_sa:,.2f})
            ────────────────────────────────────────────
            Net Operating Income         ${var_income:,.2f}
            ════════════════════════════════════════════
            Unit product cost: ${var_mfg:.2f}
            Ending inv value:  ${var_end_inv_value:,.2f}
            ```
            """)

        st.markdown("---")
        st.markdown("### 📊 Comparison Summary")
        summary_df = pd.DataFrame({
            "Metric": ["Net Operating Income", "Unit Product Cost", "Ending Inventory Value", "Key Subtotal"],
            "Absorption Costing": [
                f"${abs_income:,.2f}", f"${abs_unit_cost:.2f}",
                f"${abs_end_inv_value:,.2f}", f"Gross Margin: ${abs_gross_margin:,.2f}"
            ],
            "Variable Costing": [
                f"${var_income:,.2f}", f"${var_mfg:.2f}",
                f"${var_end_inv_value:,.2f}", f"CM: ${cm:,.2f} ({cm_ratio:.1f}%)"
            ]
        })
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

        st.markdown("### 🔄 Reconciliation")
        recon_df = pd.DataFrame({
            "Item": [
                "Variable Costing Net Income",
                f"+ Fixed OH in Ending Inventory  ({ending_inv:,} units × ${foh_rate:.2f})",
                f"− Fixed OH in Beginning Inventory  ({beg_inv:,} units × ${foh_rate:.2f})",
                "= Absorption Costing Net Income"
            ],
            "Amount": [
                f"${var_income:,.2f}",
                f"${foh_ending:,.2f}",
                f"(${foh_beginning:,.2f})",
                f"${recon_result:,.2f}"
            ]
        })
        st.dataframe(recon_df, use_container_width=True, hide_index=True)

        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Absorption Income", f"${abs_income:,.2f}")
        with col2: st.metric("Variable Income", f"${var_income:,.2f}")
        with col3: st.metric("Difference", f"${abs_income - var_income:,.2f}")

        if inv_change > 0:
            st.success(f"📈 Production ({production:,}) > Sales ({sales_units:,}): Inventory ↑ {inv_change:,} units → Absorption income is ${foh_ending-foh_beginning:,.2f} HIGHER (fixed OH deferred in inventory)")
        elif inv_change < 0:
            st.error(f"📉 Production ({production:,}) < Sales ({sales_units:,}): Inventory ↓ {abs(inv_change):,} units → Absorption income is ${abs(foh_ending-foh_beginning):,.2f} LOWER (fixed OH released from inventory)")
        else:
            st.info(f"➡️ Production ({production:,}) = Sales ({sales_units:,}): No inventory change → Both methods produce EQUAL income!")

        # Multi-year projection
        st.markdown("---")
        st.subheader("📅 Multi-Year Impact Analysis")
        st.markdown("See how changing production levels affect income under each method:")
        num_years = st.number_input("Number of years to project", 2, 5, 3)
        year_data = []
        cum_beg = beg_inv
        for y in range(int(num_years)):
            col1, col2 = st.columns(2)
            with col1: yr_prod = st.number_input(f"Year {y+1} Production", 0, value=production, step=100, key=f"m7_yprod_{y}")
            with col2: yr_sales = st.number_input(f"Year {y+1} Sales", 0, value=sales_units, step=100, key=f"m7_ysales_{y}")
            year_data.append({"prod": yr_prod, "sales": yr_sales, "beg_inv": cum_beg})
            cum_beg = cum_beg + yr_prod - yr_sales

        if st.button("📊 Run Multi-Year Analysis", type="primary"):
            yr_results = []
            for y, yd in enumerate(year_data):
                yr_rate = fixed_mfg / yd["prod"] if yd["prod"] > 0 else 0
                yr_abs_unit = var_mfg + yr_rate
                yr_abs_cogs = yd["sales"] * yr_abs_unit
                yr_end_inv = yd["beg_inv"] + yd["prod"] - yd["sales"]
                yr_abs_gm = yd["sales"] * selling_price - yr_abs_cogs
                yr_abs_ni = yr_abs_gm - yd["sales"] * var_sa - fixed_sa

                yr_var_cm = yd["sales"] * (selling_price - var_mfg - var_sa)
                yr_var_ni = yr_var_cm - fixed_mfg - fixed_sa

                yr_results.append({
                    "Year": f"Year {y+1}",
                    "Produced": f"{yd['prod']:,}",
                    "Sold": f"{yd['sales']:,}",
                    "Inv Change": f"{yd['prod']-yd['sales']:+,}",
                    "Absorption NOI": f"${yr_abs_ni:,.2f}",
                    "Variable NOI": f"${yr_var_ni:,.2f}",
                    "Difference": f"${yr_abs_ni - yr_var_ni:+,.2f}"
                })

            st.dataframe(pd.DataFrame(yr_results), use_container_width=True, hide_index=True)

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Income vs Production Level (Sales Fixed)")
        prod_range = np.arange(5000, 16000, 500)
        fixed_oh_val = 100000
        var_cost_val = 20
        sp_val = 50
        sold_val = 8000
        fsa_val = 40000
        vsa_val = 5

        abs_inc_list, var_inc_list = [], []
        for p in prod_range:
            rate = fixed_oh_val / p if p > 0 else 0
            a_unit = var_cost_val + rate
            a_cogs = sold_val * a_unit
            a_gm = sold_val * sp_val - a_cogs
            abs_inc_list.append(a_gm - sold_val * vsa_val - fsa_val)
            var_inc_list.append(sold_val * (sp_val - var_cost_val - vsa_val) - fixed_oh_val - fsa_val)

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=prod_range, y=abs_inc_list, name="Absorption Costing",
                                   line=dict(color="#2E86C1", width=3), mode="lines"))
        fig1.add_trace(go.Scatter(x=prod_range, y=var_inc_list, name="Variable Costing (constant!)",
                                   line=dict(color="#E74C3C", width=3, dash="dash"), mode="lines"))
        fig1.add_vline(x=sold_val, line_dash="dot", line_color="green",
                       annotation_text=f"Prod = Sales ({sold_val:,})")
        fig1.update_layout(
            title=f"Net Operating Income vs Production Level (Units Sold Fixed at {sold_val:,})",
            xaxis_title="Units Produced", yaxis_title="Net Operating Income ($)",
            hovermode="x unified"
        )
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Three Scenarios: Production vs Sales")
        scenarios = ["Prod = Sales\n(no change)", "Prod > Sales\n(inv. increases)", "Prod < Sales\n(inv. decreases)"]
        abs_s = [60000, 80000, 40000]
        var_s = [60000, 60000, 60000]

        fig2 = go.Figure(data=[
            go.Bar(name="Absorption Costing", x=scenarios, y=abs_s,
                   marker_color="#2E86C1", text=[f"${v:,.0f}" for v in abs_s], textposition="auto"),
            go.Bar(name="Variable Costing", x=scenarios, y=var_s,
                   marker_color="#E74C3C", text=[f"${v:,.0f}" for v in var_s], textposition="auto")
        ])
        fig2.update_layout(title="Income Under Different Production Scenarios", barmode="group", yaxis_title="NOI ($)")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Fixed Manufacturing Overhead — Two Treatment Paths")
        fig3 = go.Figure(data=[go.Sankey(
            node=dict(
                pad=20, thickness=25,
                label=["Fixed Mfg OH\n$100,000", "Absorption:\nInventory (deferred)", "Variable:\nExpensed NOW",
                       "Later: COGS\n(when sold)", "Income Stmt\nThis Period"],
                color=["#AED6F1", "#27AE60", "#E74C3C", "#1E8449", "#C0392B"]
            ),
            link=dict(
                source=[0, 0, 1, 2],
                target=[1, 2, 3, 4],
                value=[20000, 80000, 20000, 80000],
                color=["rgba(39,174,96,0.4)", "rgba(231,76,60,0.4)",
                       "rgba(39,174,96,0.4)", "rgba(231,76,60,0.4)"]
            )
        )])
        fig3.update_layout(title="How Fixed Manufacturing OH Flows Under Each Method", height=420)
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Inventory Value Comparison")
        methods = ["Absorption Costing\n(DM+DL+VarOH+FixedOH)", "Variable Costing\n(DM+DL+VarOH only)"]
        inv_values = [60000, 40000]
        fig4 = go.Figure(go.Bar(
            x=methods, y=inv_values,
            marker_color=["#2E86C1", "#E74C3C"],
            text=[f"${v:,}\n(2,000 units × $30)" if i == 0 else f"${v:,}\n(2,000 units × $20)" for i, v in enumerate(inv_values)],
            textposition="auto"
        ))
        fig4.update_layout(title="Ending Inventory Value (2,000 units)", yaxis_title="Inventory Value ($)")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. Under variable costing, fixed manufacturing overhead is treated as:**")
        q1 = st.radio("", [
            "A product cost included in inventory value",
            "A period cost expensed immediately in full",
            "Allocated to units using a predetermined rate",
            "Added to Cost of Goods Sold only"
        ], key="m7q1")
        if st.button("Check Q1", key="m7c1"):
            if q1 == "A period cost expensed immediately in full":
                st.success("✅ Correct! Variable costing expenses ALL fixed manufacturing OH immediately as a period cost.")
            else:
                st.error("❌ Incorrect. Under variable costing, fixed manufacturing OH is a period cost — expensed fully in the period incurred.")

        st.markdown("---")
        st.markdown("**Q2. When production EXCEEDS sales during a period:**")
        q2 = st.radio("", [
            "Variable income > Absorption income",
            "Absorption income > Variable income",
            "Both incomes are always equal",
            "It depends on the selling price"
        ], key="m7q2")
        if st.button("Check Q2", key="m7c2"):
            if q2 == "Absorption income > Variable income":
                st.success("✅ Correct! Production > sales means inventory grows. Under absorption, some fixed OH is deferred in ending inventory, boosting absorption income.")
            else:
                st.error("❌ Incorrect. When production > sales, inventory increases, fixed OH is deferred under absorption → absorption income is HIGHER.")

        st.markdown("---")
        st.markdown("""
        **Q3. Units produced = 12,000. Units sold = 9,000. Fixed Mfg OH = $60,000.
        By how much is Absorption income higher than Variable income?**
        """)
        q3 = st.radio("", ["$10,000", "$15,000", "$18,000", "$20,000"], key="m7q3")
        if st.button("Check Q3", key="m7c3"):
            if q3 == "$15,000":
                rate = 60000 / 12000
                diff = 3000 * rate
                st.success(f"✅ Correct! Rate = $60,000/12,000 = $5/unit. Inventory increase = 3,000 units. 3,000 × $5 = $15,000")
            else:
                st.error("❌ Incorrect. Rate = $60,000/12,000 = $5/unit. Inventory increase = 3,000. Difference = 3,000 × $5 = $15,000")

        st.markdown("---")
        st.markdown("**Q4. The Contribution Margin appears on which income statement?**")
        q4 = st.radio("", [
            "Absorption Costing income statement",
            "Variable Costing income statement",
            "Both income statements",
            "Neither — it's only used for CVP"
        ], key="m7q4")
        if st.button("Check Q4", key="m7c4"):
            if q4 == "Variable Costing income statement":
                st.success("✅ Correct! The Contribution Margin is the key subtotal in the Variable Costing format. Absorption uses Gross Margin.")
            else:
                st.error("❌ Incorrect. Contribution Margin is the key subtotal in the Variable Costing income statement. Absorption uses Gross Margin.")

        st.markdown("---")
        st.markdown("""
        **Q5. Variable costing income = $50,000. Fixed OH rate = $8/unit.
        Beginning inventory = 1,000 units. Ending inventory = 4,000 units.
        What is Absorption costing income?**
        """)
        q5 = st.radio("", ["$26,000", "$50,000", "$74,000", "$82,000"], key="m7q5")
        if st.button("Check Q5", key="m7c5"):
            if q5 == "$74,000":
                end_foh = 4000 * 8
                beg_foh = 1000 * 8
                result = 50000 + end_foh - beg_foh
                st.success(f"✅ Correct! $50,000 + (4,000×$8) − (1,000×$8) = $50,000 + $32,000 − $8,000 = ${result:,}")
            else:
                st.error("❌ Incorrect. Absorption = $50,000 + (4,000×$8) − (1,000×$8) = $50,000 + $24,000 = $74,000")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "Fixed OH Rate per Unit",
                "Absorption Unit Product Cost",
                "Variable Unit Product Cost",
                "Reconciliation (Var → Absorption)",
                "Income Difference Shortcut",
                "Contribution Margin",
                "Contribution Margin Ratio"
            ],
            "Expression": [
                "Total Fixed Manufacturing OH / Units PRODUCED",
                "DM + DL + Variable OH + Fixed OH Rate per Unit",
                "DM + DL + Variable OH only",
                "Var Income + Fixed OH in Ending Inv − Fixed OH in Beg Inv",
                "Inventory Change (units) × Fixed OH Rate per Unit",
                "Sales − Variable COGS − Variable S&A",
                "Contribution Margin / Sales Revenue × 100"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Reconciliation Rules at a Glance")
        rules_df = pd.DataFrame({
            "Scenario": [
                "Production = Sales",
                "Production > Sales (inv. ↑)",
                "Production < Sales (inv. ↓)"
            ],
            "Inventory Movement": ["No change", "Increases by X units", "Decreases by X units"],
            "Absorption vs Variable": ["EQUAL", "Absorption HIGHER by X × Rate", "Absorption LOWER by X × Rate"],
            "Fixed OH Movement": ["All expensed same period", "X units' worth deferred to inventory", "X units' worth released from inventory"]
        })
        st.dataframe(rules_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Complete Method Comparison")
        compare_df = pd.DataFrame({
            "Feature": [
                "Fixed Mfg OH treatment", "GAAP compliant", "Tax (IRS) compliant",
                "Income tracks", "CVP analysis", "Shows Contribution Margin",
                "Inventory value", "Overproduction incentive", "Primary use"
            ],
            "Absorption Costing": [
                "Product cost (inventoried)", "✅ Yes", "✅ Yes",
                "Production level", "❌ Difficult", "❌ No",
                "Higher (fixed OH included)", "⚠️ Yes — manipulable", "External reports & tax"
            ],
            "Variable Costing": [
                "Period cost (expensed now)", "❌ No", "❌ No",
                "Sales level ✅", "✅ Easy", "✅ Yes",
                "Lower (variable only)", "✅ None", "Internal decisions & CVP"
            ]
        })
        st.dataframe(compare_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Using variable costing for GAAP/tax reports",
                "Dividing fixed OH by units SOLD (not produced)",
                "Confusing Gross Margin with Contribution Margin",
                "Forgetting beginning inventory in reconciliation",
                "Thinking production level affects variable income",
                "Including fixed OH in the variable costing unit cost"
            ],
            "Correct Approach": [
                "Absorption is mandatory for external reporting — no choice",
                "Fixed OH rate = Total Fixed OH ÷ Units PRODUCED",
                "Gross Margin = Sales − COGS; CM = Sales − ALL variable costs",
                "Always: Var + End Inv FOH − Beg Inv FOH = Absorption",
                "Variable income only changes when SALES change",
                "Variable costing unit cost = DM + DL + Variable OH ONLY"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 7 Complete! You understand the critical difference between absorption and variable costing and can reconcile them perfectly.")
        st.info("💡 Next: Module 8 — Budgeting & Financial Planning")

if __name__ == "__main__":
    show()