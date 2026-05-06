import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🎯 Module 5: Activity-Based Costing & Management")
    st.markdown("*Achieve more accurate product costs with multi-driver overhead allocation*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Why Traditional Costing Can Distort Costs")
        st.markdown("""
        Traditional costing uses **one or two allocation bases** (e.g., direct labor hours) for ALL overhead.
        This works fine when products are homogeneous and overhead is small.

        **But when:**
        - Products are diverse (high-volume simple vs low-volume complex)
        - Overhead is large relative to direct costs
        - Automated production (little direct labor)

        → Traditional costing **overcosts high-volume products** and **undercosts low-volume / complex products**
        """)

        st.subheader("2. ABC Philosophy")
        st.markdown("""
        ```
        Products consume Activities
        Activities consume Resources
        Resources cost Money
        ```

        Instead of one rate, ABC assigns overhead through multiple activities,
        each with its own cost driver that best reflects actual consumption.
        """)

        st.subheader("3. Cost Hierarchy — Four Levels")
        hierarchy = pd.DataFrame({
            "Level": ["Unit-level", "Batch-level", "Product-level", "Facility-level"],
            "Description": [
                "Done each time a unit is produced",
                "Done each time a batch/setup occurs",
                "Support a specific product line",
                "Sustain entire facility"
            ],
            "Examples": [
                "Machine operations, direct energy",
                "Machine setups, purchase orders, quality inspections",
                "Product design, engineering changes",
                "Plant depreciation, security, GM salary"
            ],
            "Driver Examples": [
                "Units, machine hours",
                "# setups, # batches, # orders",
                "# products, engineering hours",
                "Not easily traced"
            ]
        })
        st.dataframe(hierarchy, use_container_width=True, hide_index=True)

        st.subheader("4. ABC Implementation — 5 Steps")
        st.markdown("""
        | Step | Action |
        |------|--------|
        | 1 | **Identify activities** — list major tasks consuming overhead |
        | 2 | **Create activity cost pools** — group costs by activity |
        | 3 | **Select cost drivers** — cause-and-effect relationship |
        | 4 | **Calculate activity rates** — Cost Pool ÷ Total Driver Quantity |
        | 5 | **Assign costs to products** — Rate × Product's driver usage |

        ```
        Activity Rate = Total Activity Cost / Total Driver Quantity

        Product OH = Σ (Activity Rate × Product's Driver Usage)
        ```
        """)

        st.subheader("5. Activity-Based Management (ABM)")
        st.markdown("""
        Using ABC information to **improve operations and strategy**.

        **Operational ABM:**
        - Identify and eliminate non-value-added activities
        - Improve process efficiency
        - Reduce waste

        **Strategic ABM:**
        - Profitable product mix decisions
        - Customer profitability analysis
        - Pricing strategies
        - Outsourcing decisions

        **Value-Added vs Non-Value-Added:**
        | Type | Definition | Examples |
        |------|-----------|---------|
        | Value-Added | Customer willing to pay | Assembly, testing |
        | Non-Value-Added | Waste — eliminate! | Rework, storage, waiting, moving |
        """)

        st.subheader("6. Customer Profitability Analysis")
        st.markdown("""
        ABC extends beyond products to **customers**.

        ```
        Customer Revenue
        − COGS
        ────────────────────────────────────
        Gross Margin
        − Customer-specific activity costs:
            • Order processing
            • Sales visits
            • Special deliveries
            • Returns handling
            • Credit & collections
        ────────────────────────────────────
        Customer Profit Margin
        ```

        Two customers with the same gross margin can have very **different profitability** when
        service costs are included!
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Traditional vs ABC Overhead")
        st.markdown("""
        **Company produces two products. Total overhead: $200,000**

        | | Product A (High Vol) | Product B (Low Vol) |
        |-|---------------------|---------------------|
        | Units | 10,000 | 2,000 |
        | Machine hours | 1,000 | 1,000 |

        **Traditional Costing (machine hours):**
        ```
        OH Rate = $200,000 / 2,000 MH = $100/MH

        Product A: 1,000 × $100 = $100,000  →  $10/unit
        Product B: 1,000 × $100 = $100,000  →  $50/unit
        ```

        **ABC — Three Activity Pools:**
        | Activity | Cost | Driver | Total | Rate |
        |----------|------|--------|-------|------|
        | Machine ops | $100,000 | Machine hrs | 2,000 | $50/MH |
        | Setups | $60,000 | # Setups | 80 | $750/setup |
        | Inspections | $40,000 | # Inspections | 400 | $100/inspection |

        **Driver Consumption:**
        | | Product A | Product B |
        |-|-----------|-----------|
        | Machine hrs | 1,000 | 1,000 |
        | Setups | 20 | 60 |
        | Inspections | 100 | 300 |

        **ABC Overhead Assignment:**
        ```
        Product A:
          Machine ops: 1,000 × $50     =  $50,000
          Setups:         20 × $750    =  $15,000
          Inspections:   100 × $100    =  $10,000
          ──────────────────────────────────────
          Total OH                     =  $75,000  →  $7.50/unit

        Product B:
          Machine ops: 1,000 × $50     =  $50,000
          Setups:         60 × $750    =  $45,000
          Inspections:   300 × $100    =  $30,000
          ──────────────────────────────────────
          Total OH                     = $125,000  →  $62.50/unit
        ```

        **Comparison:**
        | | Traditional | ABC | Difference |
        |-|------------|-----|-----------|
        | Product A | $10.00 | $7.50 | **−$2.50 (overcost)** |
        | Product B | $50.00 | $62.50 | **+$12.50 (undercost)** |

        Product B is far more expensive than traditional costing revealed!
        """)

        st.subheader("Example 2: Customer Profitability")
        st.markdown("""
        **Two customers with same sales — different service demands:**

        | Activity | Rate | Customer X | Customer Y |
        |----------|------|-----------|-----------|
        | Order processing | $50/order | 10 orders | 50 orders |
        | Sales visits | $200/visit | 5 visits | 20 visits |
        | Shipments | $75/shipment | 10 | 60 |
        | Special handling | $100/request | 2 | 15 |

        ```
        Customer X Profit:                Customer Y Profit:
        Gross Margin    $40,000           Gross Margin    $40,000
        − Orders:          500           − Orders:         2,500
        − Visits:        1,000           − Visits:         4,000
        − Shipments:       750           − Shipments:      4,500
        − Special:         200           − Special:        1,500
        ─────────────────────            ─────────────────────
        Customer Profit $37,550          Customer Profit  $27,500
        Profit %:        37.6%           Profit %:         27.5%
        ```
        Same revenue — but Customer X is $10,050 MORE profitable!
        """)

    with tab3:
        st.header("Interactive Calculators")

        calc = st.selectbox("Choose Calculator", [
            "ABC Product Costing",
            "Traditional vs ABC Comparison",
            "Customer Profitability Analysis",
            "Activity Value Analysis"
        ])

        if calc == "ABC Product Costing":
            st.subheader("🎯 ABC Product Cost Calculator")
            num_activities = st.number_input("Number of Activity Pools", 1, 8, 3)
            num_products = st.number_input("Number of Products", 1, 5, 2)

            st.markdown("### Activity Cost Pools:")
            activities = []
            for i in range(int(num_activities)):
                st.markdown(f"**Activity {i+1}:**")
                col1, col2, col3 = st.columns(3)
                with col1: a_name = st.text_input("Activity", value=f"Activity {i+1}", key=f"abc_aname_{i}")
                with col2: a_cost = st.number_input("Cost ($)", 0.0, value=50000.0+i*20000, step=1000.0, key=f"abc_acost_{i}")
                with col3: a_driver = st.text_input("Driver Name", value="Units", key=f"abc_adrv_{i}")
                activities.append({"name": a_name, "cost": a_cost, "driver": a_driver})

            st.markdown("### Product Driver Consumption:")
            product_names = []
            product_usages = []
            for p in range(int(num_products)):
                p_name = st.text_input(f"Product {p+1} Name", value=f"Product {chr(65+p)}", key=f"abc_pname_{p}")
                product_names.append(p_name)
                usages = []
                cols = st.columns(int(num_activities))
                for i, act in enumerate(activities):
                    with cols[i]:
                        u = st.number_input(f"{act['driver']}", 0.0, value=100.0, step=10.0, key=f"abc_usage_{p}_{i}")
                        usages.append(u)
                product_usages.append(usages)

            if st.button("🧮 Calculate ABC Costs", type="primary"):
                # Compute totals per activity
                total_usages = [sum([product_usages[p][i] for p in range(int(num_products))]) for i in range(int(num_activities))]
                rates = [activities[i]['cost'] / total_usages[i] if total_usages[i] > 0 else 0 for i in range(int(num_activities))]

                st.markdown("### Activity Rates:")
                rate_df = pd.DataFrame({
                    "Activity": [a['name'] for a in activities],
                    "Total Cost": [f"${a['cost']:,.2f}" for a in activities],
                    "Total Driver Qty": [f"{t:,.0f}" for t in total_usages],
                    "Activity Rate": [f"${r:,.2f}" for r in rates]
                })
                st.dataframe(rate_df, use_container_width=True, hide_index=True)

                st.markdown("### Product OH Costs:")
                result_rows = []
                for p in range(int(num_products)):
                    total_oh = sum([product_usages[p][i] * rates[i] for i in range(int(num_activities))])
                    row = {"Product": product_names[p]}
                    for i, act in enumerate(activities):
                        row[act['name']] = f"${product_usages[p][i] * rates[i]:,.2f}"
                    row["Total OH"] = f"${total_oh:,.2f}"
                    result_rows.append(row)
                st.dataframe(pd.DataFrame(result_rows), use_container_width=True, hide_index=True)

        elif calc == "Traditional vs ABC Comparison":
            st.subheader("⚖️ Traditional vs ABC Comparison")
            total_oh = st.number_input("Total Overhead ($)", 0.0, value=200000.0, step=5000.0)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Product A:**")
                a_units = st.number_input("Units", 1, value=10000, key="trad_a_u")
                a_mh = st.number_input("Machine Hours (trad base)", 0.0, value=1000.0, key="trad_a_mh")
                a_setups = st.number_input("Setups", 0.0, value=20.0, key="trad_a_s")
                a_insp = st.number_input("Inspections", 0.0, value=100.0, key="trad_a_i")
            with col2:
                st.markdown("**Product B:**")
                b_units = st.number_input("Units", 1, value=2000, key="trad_b_u")
                b_mh = st.number_input("Machine Hours (trad base)", 0.0, value=1000.0, key="trad_b_mh")
                b_setups = st.number_input("Setups", 0.0, value=60.0, key="trad_b_s")
                b_insp = st.number_input("Inspections", 0.0, value=300.0, key="trad_b_i")

            col1, col2, col3 = st.columns(3)
            with col1: mach_pool = st.number_input("Machine Ops Pool ($)", 0.0, value=100000.0, step=5000.0)
            with col2: setup_pool = st.number_input("Setup Pool ($)", 0.0, value=60000.0, step=5000.0)
            with col3: insp_pool = st.number_input("Inspection Pool ($)", 0.0, value=40000.0, step=5000.0)

            # Traditional
            trad_rate = total_oh / (a_mh + b_mh) if (a_mh + b_mh) > 0 else 0
            trad_a_unit = (a_mh * trad_rate) / a_units if a_units > 0 else 0
            trad_b_unit = (b_mh * trad_rate) / b_units if b_units > 0 else 0

            # ABC
            mach_rate = mach_pool / (a_mh + b_mh) if (a_mh + b_mh) > 0 else 0
            setup_rate = setup_pool / (a_setups + b_setups) if (a_setups + b_setups) > 0 else 0
            insp_rate = insp_pool / (a_insp + b_insp) if (a_insp + b_insp) > 0 else 0

            abc_a_total = a_mh * mach_rate + a_setups * setup_rate + a_insp * insp_rate
            abc_b_total = b_mh * mach_rate + b_setups * setup_rate + b_insp * insp_rate
            abc_a_unit = abc_a_total / a_units if a_units > 0 else 0
            abc_b_unit = abc_b_total / b_units if b_units > 0 else 0

            diff_a = abc_a_unit - trad_a_unit
            diff_b = abc_b_unit - trad_b_unit

            comparison_df = pd.DataFrame({
                "Method": ["Traditional", "ABC", "Difference"],
                "Product A (per unit)": [f"${trad_a_unit:.2f}", f"${abc_a_unit:.2f}", f"${diff_a:+.2f}"],
                "Product B (per unit)": [f"${trad_b_unit:.2f}", f"${abc_b_unit:.2f}", f"${diff_b:+.2f}"]
            })
            st.dataframe(comparison_df, use_container_width=True, hide_index=True)

            if abs(diff_a) > 0.5 or abs(diff_b) > 0.5:
                st.warning("⚠️ Significant cost distortion detected! Traditional costing is misleading.")
                if diff_a < 0:
                    st.info(f"Product A is OVERCOST by ${abs(diff_a):.2f}/unit under traditional costing.")
                if diff_b > 0:
                    st.info(f"Product B is UNDERCOST by ${diff_b:.2f}/unit under traditional costing.")

        elif calc == "Customer Profitability Analysis":
            st.subheader("👥 Customer Profitability Analysis")
            st.markdown("**Activity Rates:**")
            col1, col2, col3, col4 = st.columns(4)
            with col1: order_rate = st.number_input("Order Processing ($/order)", 0.0, value=50.0)
            with col2: visit_rate = st.number_input("Sales Visit ($/visit)", 0.0, value=200.0)
            with col3: ship_rate = st.number_input("Shipment ($/shipment)", 0.0, value=75.0)
            with col4: special_rate = st.number_input("Special Handling ($/req)", 0.0, value=100.0)

            num_customers = st.number_input("Number of Customers", 1, 6, 2)
            customers = []
            for i in range(int(num_customers)):
                st.markdown(f"**Customer {chr(65+i)}:**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    name = st.text_input("Name", value=f"Customer {chr(65+i)}", key=f"cust_name_{i}")
                    sales = st.number_input("Sales ($)", 0.0, value=100000.0, step=1000.0, key=f"cust_sales_{i}")
                    cogs = st.number_input("COGS ($)", 0.0, value=60000.0, step=1000.0, key=f"cust_cogs_{i}")
                with col2:
                    orders = st.number_input("Orders", 0, value=10+i*40, key=f"cust_orders_{i}")
                    visits = st.number_input("Visits", 0, value=5+i*15, key=f"cust_visits_{i}")
                with col3:
                    shipments = st.number_input("Shipments", 0, value=10+i*50, key=f"cust_ship_{i}")
                    special = st.number_input("Special Requests", 0, value=2+i*13, key=f"cust_spec_{i}")
                customers.append({"name": name, "sales": sales, "cogs": cogs,
                                   "orders": orders, "visits": visits, "shipments": shipments, "special": special})

            if st.button("🧮 Calculate Customer Profitability", type="primary"):
                results = []
                for c in customers:
                    gm = c['sales'] - c['cogs']
                    activity_costs = (c['orders'] * order_rate + c['visits'] * visit_rate +
                                      c['shipments'] * ship_rate + c['special'] * special_rate)
                    profit = gm - activity_costs
                    profit_pct = profit / c['sales'] * 100 if c['sales'] > 0 else 0
                    results.append({"Customer": c['name'], "Sales": f"${c['sales']:,.0f}",
                                     "Gross Margin": f"${gm:,.0f}", "Activity Costs": f"${activity_costs:,.0f}",
                                     "Customer Profit": f"${profit:,.0f}", "Profit %": f"{profit_pct:.1f}%"})
                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

        else:  # Activity Value Analysis
            st.subheader("🔍 Activity Value Analysis")
            num_acts = st.number_input("Number of Activities", 1, 10, 5)
            activities = []
            for i in range(int(num_acts)):
                col1, col2, col3 = st.columns(3)
                with col1: aname = st.text_input("Activity", value=f"Activity {i+1}", key=f"ava_n_{i}")
                with col2: acost = st.number_input("Annual Cost ($)", 0.0, value=20000.0+i*5000, step=1000.0, key=f"ava_c_{i}")
                with col3:
                    va = st.selectbox("Value Type", ["Value-Added", "Non-Value-Added"], key=f"ava_v_{i}")
                activities.append({"name": aname, "cost": acost, "type": va})

            df = pd.DataFrame(activities)
            total = df['cost'].sum()
            va_total = df[df['type'] == 'Value-Added']['cost'].sum()
            nva_total = df[df['type'] == 'Non-Value-Added']['cost'].sum()

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Total Activity Cost", f"${total:,.2f}")
            with col2: st.metric("Value-Added", f"${va_total:,.2f}", f"{va_total/total*100:.1f}%" if total > 0 else "0%")
            with col3: st.metric("Non-Value-Added (Waste!)", f"${nva_total:,.2f}", f"{nva_total/total*100:.1f}%" if total > 0 else "0%")

            if nva_total / total > 0.2 if total > 0 else False:
                st.error(f"❌ {nva_total/total*100:.1f}% of costs are non-value-added. Target these for elimination!")
            else:
                st.success("✅ Healthy value-added ratio.")

    with tab4:
        st.header("Visual Analytics")

        st.subheader("Traditional vs ABC — Cost Per Unit Comparison")
        products = ["Product A\n(High Volume)", "Product B\n(Low Volume)"]
        trad = [10, 50]
        abc_vals = [7.5, 62.5]
        fig1 = go.Figure(data=[
            go.Bar(name="Traditional", x=products, y=trad, marker_color="#AED6F1"),
            go.Bar(name="ABC", x=products, y=abc_vals, marker_color="#1A5276")
        ])
        fig1.update_layout(title="Traditional vs ABC — OH per Unit", barmode="group", yaxis_title="Overhead per Unit ($)")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Cost Hierarchy Breakdown")
        hierarchy_data = pd.DataFrame({
            "Level": ["Unit-Level", "Batch-Level", "Product-Level", "Facility-Level"],
            "Cost": [100000, 60000, 40000, 50000]
        })
        fig2 = px.pie(hierarchy_data, values="Cost", names="Level",
                      title="Overhead by Cost Hierarchy Level",
                      color_discrete_sequence=["#2E86C1", "#27AE60", "#E67E22", "#8E44AD"])
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Value-Added vs Non-Value-Added Activities")
        va_data = pd.DataFrame({"Type": ["Value-Added", "Non-Value-Added"], "Cost": [150000, 50000]})
        fig3 = px.pie(va_data, values="Cost", names="Type", title="Activity Value Analysis",
                      color="Type", color_discrete_map={"Value-Added": "#27AE60", "Non-Value-Added": "#E74C3C"})
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Customer Profitability Comparison")
        cust_data = pd.DataFrame({
            "Customer": ["Customer A", "Customer B", "Customer C", "Customer D"],
            "Gross Margin": [40000, 40000, 30000, 25000],
            "Activity Costs": [2450, 12500, 8000, 20000],
            "Profit": [37550, 27500, 22000, 5000]
        })
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(x=cust_data["Customer"], y=cust_data["Gross Margin"], name="Gross Margin", marker_color="#27AE60"))
        fig4.add_trace(go.Bar(x=cust_data["Customer"], y=cust_data["Activity Costs"], name="Activity Costs", marker_color="#E74C3C"))
        fig4.add_trace(go.Scatter(x=cust_data["Customer"], y=cust_data["Profit"],
                                   name="Net Profit", mode="lines+markers",
                                   marker=dict(size=12, color="#1A5276"), line=dict(width=3)))
        fig4.update_layout(title="Customer Profitability Analysis", barmode="group", yaxis_title="Amount ($)")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("🧠 Knowledge Check Quiz")

        st.markdown("**Q1. ABC is most beneficial when:**")
        q1 = st.radio("", ["All products are identical", "Products are diverse and consume overhead differently",
                            "Direct labor is the only cost", "The company makes one product"], key="m5q1")
        if st.button("Check Q1", key="m5c1"):
            st.success("✅ Correct! ABC shines when products have diverse overhead consumption.") if q1 == "Products are diverse and consume overhead differently" else st.error("❌ Incorrect. ABC is most useful with diverse products.")

        st.markdown("---")
        st.markdown("**Q2. A machine setup is which level of the cost hierarchy?**")
        q2 = st.radio("", ["Unit-level", "Batch-level", "Product-level", "Facility-level"], key="m5q2")
        if st.button("Check Q2", key="m5c2"):
            st.success("✅ Correct! Setups occur once per batch, not per unit.") if q2 == "Batch-level" else st.error("❌ Incorrect. Machine setups are batch-level activities.")

        st.markdown("---")
        st.markdown("**Q3. Activity pool = $90,000. Driver quantity = 450. Activity rate = ?**")
        q3 = st.radio("", ["$100", "$150", "$200", "$250"], key="m5q3")
        if st.button("Check Q3", key="m5c3"):
            st.success("✅ Correct! $90,000 / 450 = $200.") if q3 == "$200" else st.error("❌ Incorrect. $90,000 ÷ 450 = $200 per driver unit.")

        st.markdown("---")
        st.markdown("**Q4. A non-value-added activity is best described as:**")
        q4 = st.radio("", ["Assembly", "Testing", "Moving inventory between stores", "Customer delivery"], key="m5q4")
        if st.button("Check Q4", key="m5c4"):
            st.success("✅ Correct! Moving inventory does not add value — it's waste.") if q4 == "Moving inventory between stores" else st.error("❌ Incorrect. Moving inventory is non-value-added waste.")

        st.markdown("---")
        st.markdown("**Q5. Traditional costing tends to:**")
        q5 = st.radio("", [
            "Overcost low-volume complex products",
            "Undercost high-volume simple products",
            "Overcost high-volume products and undercost low-volume products",
            "Give perfectly accurate costs always"
        ], key="m5q5")
        if st.button("Check Q5", key="m5c5"):
            st.success("✅ Correct! High-volume products get too much overhead; complex low-volume products get too little.") if q5 == "Overcost high-volume products and undercost low-volume products" else st.error("❌ Incorrect. Traditional costing overcosts high-volume and undercosts low-volume.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Formulas")
        formulas = pd.DataFrame({
            "Formula": ["Activity Rate", "Product OH Cost (ABC)", "Total Product Cost", "Customer Profit"],
            "Expression": [
                "Total Activity Cost / Total Driver Quantity",
                "Σ (Activity Rate × Product's Driver Usage)",
                "DM + DL + ABC Overhead",
                "Gross Margin − Customer-Specific Activity Costs"
            ]
        })
        st.dataframe(formulas, use_container_width=True, hide_index=True)

        st.subheader("📊 ABC vs Traditional Summary")
        compare = pd.DataFrame({
            "Feature": ["Overhead rates", "Allocation bases", "Accuracy", "Complexity", "Best for", "GAAP?"],
            "Traditional": ["One or two", "DLH or MH only", "Lower", "Simple", "Homogeneous products", "Yes"],
            "ABC": ["Multiple (one per activity)", "Multiple cause-effect drivers", "Higher", "More complex", "Diverse products", "Not required"]
        })
        st.dataframe(compare, use_container_width=True, hide_index=True)

        st.subheader("📌 ABC 5-Step Process")
        st.markdown("""
        ```
        Step 1 ── Identify Activities
                  List all significant overhead-consuming activities

        Step 2 ── Create Activity Cost Pools
                  Group related costs together

        Step 3 ── Select Cost Drivers
                  Choose drivers with strong cause-effect relationship

        Step 4 ── Calculate Activity Rates
                  Rate = Pool Cost / Total Driver Quantity

        Step 5 ── Assign Costs to Products
                  Product OH = Σ (Rate × Product's Usage)
        ```
        """)

        st.subheader("💡 Cost Hierarchy Quick Reference")
        hier_summary = pd.DataFrame({
            "Level": ["Unit", "Batch", "Product", "Facility"],
            "Triggered by": ["Each unit produced", "Each batch/setup", "Each product line", "Entire company"],
            "ABC Allocatable?": ["Yes ✅", "Yes ✅", "Yes ✅", "Difficult ❌"]
        })
        st.dataframe(hier_summary, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes = pd.DataFrame({
            "Mistake": [
                "Using only one driver for complex environments",
                "Allocating facility-level costs to products",
                "Ignoring customer-specific activity costs",
                "Not validating cause-effect of drivers",
                "Implementing ABC when products are homogeneous"
            ],
            "Correct Approach": [
                "Use multiple drivers matched to activity consumption",
                "Treat facility costs as period costs or allocate carefully",
                "Extend ABC to customer profitability analysis",
                "Choose drivers that truly cause cost changes",
                "ABC adds complexity — only use when it adds value"
            ]
        })
        st.dataframe(mistakes, use_container_width=True, hide_index=True)

        st.success("🎓 Module 5 Complete! You can now design and implement ABC systems and perform customer profitability analysis.")
        st.info("💡 Next: Module 6 — Cost Allocation & Joint Products")

if __name__ == "__main__":
    show()