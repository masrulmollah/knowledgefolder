import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("⚖️ Module 11: Relevant Costs for Decision Making")
    st.markdown("*Apply differential analysis to make better short-term business decisions*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Relevant vs Irrelevant Costs")
        st.markdown("""
        **Relevant Cost:** A future cost that DIFFERS between decision alternatives.
        - Must be a **future** cost (not already incurred)
        - Must **differ** between the options being compared

        **Irrelevant Costs — Never affect the decision:**
        - **Sunk Costs**: Already spent and cannot be recovered (e.g., equipment purchase price)
        - **Future costs identical** across all alternatives

        **⭐ Opportunity Cost:** The benefit FOREGONE by choosing one option over another.
        - Always relevant!
        - Never appears in accounting records, but MUST be included in decisions
        - Example: Using factory space for Product A means you cannot use it for Product B

        #### Decision Rule:
        ```
        Choose the alternative with the HIGHEST net relevant benefit
        (or lowest net relevant cost)

        Only include costs/revenues that CHANGE between alternatives!
        ```
        """)

        st.subheader("2. Special Order Decision")
        st.markdown("""
        **Question:** Should we accept a one-time order at a price below our normal selling price?

        **Accept if:** Incremental Revenue > Incremental Costs

        **Relevant Costs:**
        - Variable manufacturing costs (change with the order)
        - Any special order-specific costs (extra shipping, setup)

        **Irrelevant:**
        - Fixed manufacturing overhead (does NOT change)
        - Normal selling and admin expenses (assuming they don't change)

        **Critical Condition:** The company must have **excess capacity** for the full analysis to apply.
        If capacity must be displaced, add the lost contribution margin as an opportunity cost.

        ```
        Accept if:
        Special Order Revenue > Variable Costs + Opportunity Costs + Special Fixed Costs
        ```
        """)

        st.subheader("3. Make or Buy Decision (Outsourcing)")
        st.markdown("""
        **Question:** Should we produce a component internally or buy it from an outside supplier?

        **Relevant Costs to MAKE:**
        - All variable manufacturing costs per unit
        - Fixed costs that can be AVOIDED if we stop making (avoidable fixed costs)
        - Opportunity cost of resources used

        **Relevant Cost to BUY:**
        - Purchase price per unit

        ```
        Buy if:  Purchase Price < (Variable Cost + Avoidable Fixed Cost + Opportunity Cost)
        Make if: Purchase Price > (Variable Cost + Avoidable Fixed Cost + Opportunity Cost)
        ```

        **Qualitative factors:** Quality control, supply reliability, proprietary know-how, flexibility
        """)

        st.subheader("4. Drop or Keep a Segment")
        st.markdown("""
        **Question:** Should we eliminate a product, department, or segment?

        **Keep if:** The segment's Contribution Margin > Avoidable Fixed Costs

        ```
        Impact of dropping segment:
        − Contribution Margin Lost       (negative — we lose this)
        + Avoidable Fixed Costs Saved    (positive — we stop paying these)
        − Lost CM from other segments    (if segment supports other products)
        ──────────────────────────────────────────────────────────────
        = Net Impact (Positive = Drop; Negative = Keep)
        ```

        **⚠️ Warning:** Common fixed costs that are merely REALLOCATED to other segments
        should be ignored — the company still pays them whether you drop the segment or not!
        """)

        st.subheader("5. Product Mix with Constrained Resource")
        st.markdown("""
        **Question:** When a scarce resource limits production, which products to prioritize?

        **Answer:** Maximize Contribution Margin per unit of the SCARCE RESOURCE.

        ```
        Step 1: Calculate CM per unit for each product
        Step 2: Calculate CM per unit of scarce resource
                = CM per unit / Units of scarce resource required
        Step 3: Rank products by CM per scarce resource (highest first)
        Step 4: Produce in rank order until resource is exhausted
        ```

        **Common Constraints:** Machine hours, labor hours, materials, floor space, cash
        """)

        st.subheader("6. Theory of Constraints (TOC)")
        st.markdown("""
        **Throughput Accounting** focuses on the bottleneck (constraint).

        ```
        Throughput Contribution = Sales − Direct Materials

        Rank products by: Throughput per bottleneck hour
        ```

        **Five Steps to Manage Constraints:**
        1. Identify the constraint (bottleneck)
        2. Exploit the constraint (maximize throughput at the bottleneck)
        3. Subordinate everything else to the constraint
        4. Elevate the constraint (invest to increase bottleneck capacity)
        5. Repeat — don't let inertia become the constraint
        """)

        st.subheader("7. Sell or Process Further")
        st.markdown("""
        **Question:** Sell at the split-off point or process further?

        ```
        Process Further if:
        Incremental Revenue from further processing > Incremental Separable Costs

        Net Benefit = (Final Price − Split-off Price) × Units
                    − Additional Processing Costs
        ```

        **⚠️ Joint costs are SUNK — completely irrelevant to this decision!**
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Special Order")
        st.markdown("""
        **Company normally sells 50,000 units/year at $40 each. Full capacity = 60,000 units.**
        **Special order received: 8,000 units at $28 each.**

        **Cost structure:**
        - Variable manufacturing: $18/unit
        - Fixed manufacturing overhead: $300,000 total
        - Normal selling expenses: $200,000 total

        **Analysis (excess capacity of 10,000 units — no displacement):**
        ```
        Special Order Revenue:  8,000 × $28          $224,000
        Variable Mfg Cost:      8,000 × $18          ($144,000)
        ─────────────────────────────────────────────────────────
        Net Benefit from Order:                         $80,000

        ✅ ACCEPT — adds $80,000 to profit!
        ```

        **Why ignore fixed overhead?** Fixed overhead is $300,000 whether you accept or not.
        It doesn't CHANGE — so it's irrelevant!
        """)

        st.subheader("Example 2: Make or Buy")
        st.markdown("""
        **Currently making 20,000 units of Part X. Supplier offers $15/unit.**

        **Current manufacturing costs:**
        | Cost | Per Unit |
        |------|----------|
        | Direct materials | $5.00 |
        | Direct labor | $4.00 |
        | Variable overhead | $2.50 |
        | Fixed overhead (avoidable 60%) | $3.00 |
        | Fixed overhead (unavoidable 40%) | $2.00 |
        | **Total** | **$16.50** |

        ```
        MAKE (relevant costs only):
        Variable costs:               $5.00 + $4.00 + $2.50 = $11.50
        Avoidable fixed:              60% × $5.00              = $3.00
        Total relevant cost to MAKE:                           = $14.50

        BUY cost:                                              = $15.00

        Difference: $15.00 − $14.50 = $0.50 per unit in favor of MAKING

        Total savings from MAKING: 20,000 × $0.50 = $10,000/year

        ✅ MAKE — saves $10,000 per year
        ```

        **But if freed capacity can generate $30,000 CM from other use:**
        ```
        Cost to Make (relevant):   20,000 × $14.50 = $290,000
        Opportunity Cost:                            = $30,000
        Total cost to Make:                          = $320,000

        Cost to Buy:               20,000 × $15.00 = $300,000

        ✅ BUY — saves $20,000 when opportunity cost is included!
        ```
        """)

        st.subheader("Example 3: Product Mix with Machine Hour Constraint")
        st.markdown("""
        **Available machine hours: 12,000/month. Demand is unlimited.**

        | Product | Price | Var Cost | CM/unit | Machine Hrs | CM/MH | Rank |
        |---------|-------|----------|---------|-------------|-------|------|
        | Alpha | $50 | $30 | $20 | 4 hrs | **$5.00** | 3rd |
        | Beta | $45 | $15 | $30 | 2 hrs | **$15.00** | 1st |
        | Gamma | $60 | $40 | $20 | 2 hrs | **$10.00** | 2nd |

        **Optimal production plan:**
        ```
        1st: Beta    — produce as much as needed (demand = 3,000 units × 2 hrs = 6,000 hrs)
        2nd: Gamma   — produce as much as needed (demand = 2,000 units × 2 hrs = 4,000 hrs)
        3rd: Alpha   — remaining hours: 12,000 − 6,000 − 4,000 = 2,000 hrs ÷ 4 = 500 units
        ```

        **Wrong approach:** Ranking by CM per unit gives Alpha and Gamma tied at $20 — but Beta is more valuable!
        **Correct approach:** Ranking by CM per machine hour puts Beta first!
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        decision_type = st.selectbox("Choose Decision Type:", [
            "📦 Special Order Analysis",
            "🏭 Make or Buy Decision",
            "🗑️ Drop or Keep a Segment",
            "⚙️ Optimal Product Mix (Constrained Resource)",
            "🔀 Sell or Process Further"
        ])

        if decision_type == "📦 Special Order Analysis":
            st.subheader("Special Order Analysis")
            st.info("A special order is a one-time order that does not affect regular sales.")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Regular Business:**")
                normal_capacity = st.number_input("Total Production Capacity (units)", 0, value=60000, step=1000)
                normal_sales = st.number_input("Normal Sales Volume (units)", 0, value=50000, step=1000)
                normal_price = st.number_input("Normal Selling Price ($/unit)", 0.0, value=40.0, step=1.0)
                var_mfg_cost = st.number_input("Variable Mfg Cost ($/unit)", 0.0, value=18.0, step=0.5)
                var_sa_cost = st.number_input("Variable S&A Cost ($/unit)", 0.0, value=3.0, step=0.5)
                fixed_mfg_oh = st.number_input("Total Fixed Mfg OH ($)", 0.0, value=300000.0, step=5000.0)

            with col2:
                st.markdown("**Special Order Details:**")
                order_units = st.number_input("Special Order Units", 0, value=8000, step=100)
                order_price = st.number_input("Special Order Price ($/unit)", 0.0, value=28.0, step=0.5)
                special_var_sa = st.number_input("Special Variable S&A for this Order ($/unit)", 0.0, value=0.0, step=0.5)
                special_fixed_cost = st.number_input("Special Fixed Costs for this Order ($)", 0.0, value=0.0, step=500.0)

            # Capacity analysis
            excess_capacity = normal_capacity - normal_sales
            units_displaced = max(0, order_units - excess_capacity)
            units_from_excess = min(order_units, excess_capacity)

            if st.button("🧮 Analyze Special Order", type="primary"):
                st.markdown("---")

                # Incremental revenue
                order_revenue = order_units * order_price
                # Incremental costs
                order_var_cost = order_units * (var_mfg_cost + special_var_sa)
                # Opportunity cost (lost normal CM from displaced units)
                normal_cm_per_unit = normal_price - var_mfg_cost - var_sa_cost
                displaced_cm = units_displaced * normal_cm_per_unit
                # Net benefit
                net_benefit = order_revenue - order_var_cost - displaced_cm - special_fixed_cost

                st.markdown("### Capacity Analysis:")
                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Excess Capacity", f"{excess_capacity:,} units")
                with col2: st.metric("Units From Excess Capacity", f"{units_from_excess:,} units")
                with col3: st.metric("Units Displacing Normal Sales", f"{units_displaced:,} units")

                st.markdown("### Incremental Analysis:")
                analysis_df = pd.DataFrame({
                    "Item": [
                        f"Revenue ({order_units:,} × ${order_price:.2f})",
                        f"Variable Mfg Cost ({order_units:,} × ${var_mfg_cost:.2f})",
                        f"Special Var S&A ({order_units:,} × ${special_var_sa:.2f})",
                        f"Opportunity Cost — Displaced CM ({units_displaced:,} × ${normal_cm_per_unit:.2f})",
                        f"Special Fixed Costs",
                        "NET BENEFIT / (LOSS)"
                    ],
                    "Amount": [
                        f"${order_revenue:,.2f}",
                        f"(${order_units * var_mfg_cost:,.2f})",
                        f"(${order_units * special_var_sa:,.2f})",
                        f"(${displaced_cm:,.2f})",
                        f"(${special_fixed_cost:,.2f})",
                        f"${net_benefit:,.2f}"
                    ]
                })
                st.dataframe(analysis_df, use_container_width=True, hide_index=True)

                if net_benefit > 0:
                    st.success(f"✅ ACCEPT the special order — adds ${net_benefit:,.2f} to company profit!")
                else:
                    st.error(f"❌ REJECT the special order — would reduce profit by ${abs(net_benefit):,.2f}")

                st.info(f"💡 Fixed overhead of ${fixed_mfg_oh:,.2f} is IRRELEVANT — it does not change regardless of the order decision.")

        elif decision_type == "🏭 Make or Buy Decision":
            st.subheader("Make or Buy Decision Calculator")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Current Manufacturing Costs per Unit:**")
                dm = st.number_input("Direct Materials", 0.0, value=5.0, step=0.5)
                dl = st.number_input("Direct Labor", 0.0, value=4.0, step=0.5)
                var_oh = st.number_input("Variable Overhead", 0.0, value=2.5, step=0.5)
                total_fixed_oh = st.number_input("Total Fixed OH per Unit", 0.0, value=5.0, step=0.5)
                avoidable_fixed_pct = st.number_input("% of Fixed OH that is AVOIDABLE if we buy", 0.0, 100.0, 60.0)
                units_needed = st.number_input("Units Needed per Year", 0, value=20000, step=100)

            with col2:
                st.markdown("**Outsourcing:**")
                buy_price = st.number_input("Supplier's Purchase Price per Unit ($)", 0.0, value=15.0, step=0.5)
                opportunity_cm = st.number_input("CM from Alternative Use of Freed Capacity (total $)", 0.0, value=0.0, step=1000.0)
                quality_risk = st.radio("Supplier Quality Risk", ["Low", "Medium", "High"])
                supply_reliability = st.radio("Supply Reliability", ["Very Reliable", "Somewhat Reliable", "Unreliable"])

            if st.button("🧮 Analyze Make vs Buy", type="primary"):
                avoidable_fixed = total_fixed_oh * avoidable_fixed_pct / 100
                unavoidable_fixed = total_fixed_oh - avoidable_fixed

                # Relevant cost to make per unit
                make_var_cost = dm + dl + var_oh
                make_relevant_per_unit = make_var_cost + avoidable_fixed
                make_total = (make_relevant_per_unit * units_needed) + opportunity_cm

                buy_total = buy_price * units_needed

                diff = buy_total - make_total

                st.markdown("---")
                st.markdown("### Cost Comparison:")
                cost_df = pd.DataFrame({
                    "Cost Element": [
                        "Direct Materials", "Direct Labor", "Variable Overhead",
                        "Avoidable Fixed OH", "Unavoidable Fixed OH (irrelevant)",
                        "Opportunity Cost", "Purchase Price", "Total Relevant Cost"
                    ],
                    "Make (per unit)": [
                        f"${dm:.2f}", f"${dl:.2f}", f"${var_oh:.2f}",
                        f"${avoidable_fixed:.2f}", f"IRRELEVANT",
                        f"${opportunity_cm/units_needed:.2f}" if units_needed > 0 else "$0.00",
                        "—", f"${make_relevant_per_unit + (opportunity_cm/units_needed if units_needed > 0 else 0):.2f}"
                    ],
                    "Buy (per unit)": [
                        "—", "—", "—", "—", "IRRELEVANT",
                        "—", f"${buy_price:.2f}", f"${buy_price:.2f}"
                    ]
                })
                st.dataframe(cost_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Total Cost to Make", f"${make_total:,.2f}")
                with col2: st.metric("Total Cost to Buy", f"${buy_total:,.2f}")
                with col3: st.metric("Annual Savings", f"${abs(diff):,.2f} {'(Buy)' if diff < 0 else '(Make)'}")

                if make_total < buy_total:
                    st.success(f"✅ MAKE — saves ${diff:,.2f} per year vs buying.")
                else:
                    st.error(f"🛒 BUY — saves ${abs(diff):,.2f} per year vs making.")

                # Qualitative factors
                st.markdown("### Qualitative Considerations:")
                qual_df = pd.DataFrame({
                    "Factor": ["Quality Risk", "Supply Reliability", "Strategic Flexibility"],
                    "Assessment": [
                        f"{quality_risk} quality risk from supplier",
                        f"Supplier is {supply_reliability.lower()}",
                        "Buying may risk losing production know-how"
                    ],
                    "Implication": [
                        "High risk → prefer making internally" if quality_risk == "High" else "Risk manageable",
                        "Unreliable → prefer making" if supply_reliability == "Unreliable" else "Supply risk manageable",
                        "Consider long-term strategic impact"
                    ]
                })
                st.dataframe(qual_df, use_container_width=True, hide_index=True)

        elif decision_type == "🗑️ Drop or Keep a Segment":
            st.subheader("Drop or Keep a Segment")
            st.info("Keep a segment if its Contribution Margin exceeds its Avoidable Fixed Costs.")

            segment_name = st.text_input("Segment Name", value="Product Line C")
            col1, col2 = st.columns(2)
            with col1:
                seg_sales = st.number_input("Segment Sales ($)", 0.0, value=150000.0, step=5000.0)
                seg_var_costs = st.number_input("Segment Variable Costs ($)", 0.0, value=100000.0, step=5000.0)
                seg_trace_fixed = st.number_input("Total Traceable Fixed Costs ($)", 0.0, value=80000.0, step=5000.0)
            with col2:
                avoidable_fixed_pct2 = st.number_input("% of Traceable Fixed that is AVOIDABLE", 0.0, 100.0, 75.0)
                lost_other_cm = st.number_input("Lost CM from Other Segments if This is Dropped ($)", 0.0, value=5000.0, step=500.0)

            if st.button("🧮 Analyze Drop/Keep Decision", type="primary"):
                seg_cm = seg_sales - seg_var_costs
                avoidable_fixed2 = seg_trace_fixed * avoidable_fixed_pct2 / 100
                unavoidable_fixed = seg_trace_fixed - avoidable_fixed2
                seg_margin = seg_cm - seg_trace_fixed

                net_impact_of_dropping = -seg_cm + avoidable_fixed2 - lost_other_cm

                st.markdown("### Segment Analysis:")
                analysis_df = pd.DataFrame({
                    "Item": [
                        f"Contribution Margin LOST (Sales ${seg_sales:,.0f} − VC ${seg_var_costs:,.0f})",
                        f"Avoidable Fixed Costs SAVED ({avoidable_fixed_pct2:.0f}% of ${seg_trace_fixed:,.0f})",
                        f"Unavoidable Fixed (still paid anyway — irrelevant)",
                        "Lost CM from Other Segments",
                        "NET IMPACT OF DROPPING"
                    ],
                    "Amount": [
                        f"(${seg_cm:,.2f})",
                        f"${avoidable_fixed2:,.2f}",
                        f"IRRELEVANT: ${unavoidable_fixed:,.2f}",
                        f"(${lost_other_cm:,.2f})",
                        f"${net_impact_of_dropping:,.2f}"
                    ]
                })
                st.dataframe(analysis_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Contribution Margin", f"${seg_cm:,.2f}")
                with col2: st.metric("Segment Margin", f"${seg_margin:,.2f}")
                with col3: st.metric("Net Impact of Dropping", f"${net_impact_of_dropping:,.2f}")

                if net_impact_of_dropping > 0:
                    st.success(f"✅ DROP the segment — company is ${net_impact_of_dropping:,.2f} better off!")
                else:
                    st.error(f"❌ KEEP the segment — dropping would reduce profit by ${abs(net_impact_of_dropping):,.2f}")

                st.info(f"💡 The ${unavoidable_fixed:,.2f} of unavoidable fixed costs remains even if the segment is dropped — it's irrelevant to this decision!")

        elif decision_type == "⚙️ Optimal Product Mix (Constrained Resource)":
            st.subheader("Optimal Product Mix — Constrained Resource")

            col1, col2 = st.columns(2)
            with col1:
                constraint_name = st.text_input("Constrained Resource Name", value="Machine Hours")
                total_resource = st.number_input("Total Available Resource", 0.0, value=12000.0, step=100.0)
            with col2:
                num_products = st.number_input("Number of Products", 2, 6, 3)

            products = []
            for i in range(int(num_products)):
                st.markdown(f"**Product {chr(65+i)}:**")
                col1, col2, col3, col4 = st.columns(4)
                with col1: price = st.number_input("Selling Price ($)", 0.0, value=[50.0,45.0,60.0,55.0,40.0][i] if i<5 else 50.0, key=f"pm_p_{i}")
                with col2: vc = st.number_input("Variable Cost ($)", 0.0, value=[30.0,15.0,40.0,25.0,22.0][i] if i<5 else 30.0, key=f"pm_vc_{i}")
                with col3: res = st.number_input(f"{constraint_name[:6]}/unit", 0.0, value=[4.0,2.0,2.0,3.0,1.5][i] if i<5 else 2.0, step=0.5, key=f"pm_r_{i}")
                with col4: demand = st.number_input("Max Demand", 0, value=[2000,3000,2000,1500,4000][i] if i<5 else 2000, key=f"pm_d_{i}")
                cm = price - vc
                cm_per_res = cm / res if res > 0 else 0
                products.append({"name": chr(65+i), "price": price, "vc": vc, "cm": cm,
                                   "res": res, "cm_per_res": cm_per_res, "demand": demand})

            if st.button("🧮 Optimize Product Mix", type="primary"):
                # Rank by CM per constrained resource
                products_sorted = sorted(products, key=lambda x: x["cm_per_res"], reverse=True)

                st.markdown("### Product Ranking (by CM per scarce resource):")
                rank_df = pd.DataFrame([{
                    "Rank": idx+1, "Product": p["name"],
                    "Price": f"${p['price']:.2f}", "Var Cost": f"${p['vc']:.2f}",
                    "CM/Unit": f"${p['cm']:.2f}", f"{constraint_name}/Unit": f"{p['res']:.1f}",
                    f"CM/{constraint_name}": f"${p['cm_per_res']:.2f}",
                    "Max Demand": f"{p['demand']:,}"
                } for idx, p in enumerate(products_sorted)])
                st.dataframe(rank_df, use_container_width=True, hide_index=True)

                st.markdown("### Optimal Production Plan:")
                remaining = total_resource
                plan_rows = []
                total_cm_earned = 0

                for p in products_sorted:
                    max_from_resource = remaining / p["res"] if p["res"] > 0 else 0
                    units_to_produce = min(p["demand"], max_from_resource)
                    resource_used = units_to_produce * p["res"]
                    cm_earned = units_to_produce * p["cm"]
                    remaining -= resource_used
                    total_cm_earned += cm_earned

                    plan_rows.append({
                        "Product": p["name"],
                        f"{constraint_name} Available": f"{remaining + resource_used:,.0f}",
                        "Units Produced": f"{units_to_produce:,.0f}",
                        f"{constraint_name} Used": f"{resource_used:,.0f}",
                        f"{constraint_name} Remaining": f"{remaining:,.0f}",
                        "Total CM": f"${cm_earned:,.2f}"
                    })

                st.dataframe(pd.DataFrame(plan_rows), use_container_width=True, hide_index=True)
                st.metric("Total Contribution Margin", f"${total_cm_earned:,.2f}")
                st.metric("Resource Utilization", f"{(total_resource - remaining)/total_resource*100:.1f}%")

        else:  # Sell or Process Further
            st.subheader("Sell or Process Further Decision")
            st.warning("⚠️ Joint costs are SUNK and IRRELEVANT to this decision!")

            col1, col2 = st.columns(2)
            with col1:
                product_name = st.text_input("Product Name", value="Product B")
                units = st.number_input("Units Available", 0, value=15000, step=100)
                split_off_price = st.number_input("Selling Price at Split-Off ($/unit)", 0.0, value=20.0, step=0.5)
                joint_cost_pu = st.number_input("Joint Cost/unit (for info only — SUNK)", 0.0, value=10.0, step=0.5)
            with col2:
                final_price = st.number_input("Final Price if Processed Further ($/unit)", 0.0, value=28.0, step=0.5)
                process_cost_pu = st.number_input("Additional Processing Cost ($/unit)", 0.0, value=5.0, step=0.5)
                process_fixed = st.number_input("Additional Fixed Processing Costs ($)", 0.0, value=0.0, step=1000.0)

            if st.button("🧮 Analyze Decision", type="primary"):
                incr_rev = (final_price - split_off_price) * units
                incr_var_cost = process_cost_pu * units
                total_incr_cost = incr_var_cost + process_fixed
                net_benefit = incr_rev - total_incr_cost

                st.markdown("### Incremental Analysis:")
                analysis_df = pd.DataFrame({
                    "Item": [
                        f"Revenue if processed further ({units:,} × ${final_price:.2f})",
                        f"Revenue if sold now ({units:,} × ${split_off_price:.2f})",
                        "Incremental Revenue from Processing",
                        f"Variable Processing Costs ({units:,} × ${process_cost_pu:.2f})",
                        "Fixed Processing Costs",
                        "NET BENEFIT FROM PROCESSING FURTHER"
                    ],
                    "Amount": [
                        f"${units * final_price:,.2f}",
                        f"${units * split_off_price:,.2f}",
                        f"${incr_rev:,.2f}",
                        f"(${incr_var_cost:,.2f})",
                        f"(${process_fixed:,.2f})",
                        f"${net_benefit:,.2f}"
                    ]
                })
                st.dataframe(analysis_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Incremental Revenue", f"${incr_rev:,.2f}")
                with col2: st.metric("Incremental Cost", f"${total_incr_cost:,.2f}")
                with col3: st.metric("Net Benefit", f"${net_benefit:,.2f}")

                if net_benefit > 0:
                    st.success(f"✅ PROCESS FURTHER — adds ${net_benefit:,.2f} to profit!")
                else:
                    st.error(f"❌ SELL AT SPLIT-OFF — processing further loses ${abs(net_benefit):,.2f}")

                st.info(f"💡 Joint cost of ${joint_cost_pu:.2f}/unit (total ${joint_cost_pu*units:,.2f}) is a SUNK COST. Completely irrelevant to this decision!")

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Make vs Buy — Cost Comparison")
        make_elements = ["DM", "DL", "Var OH", "Avoidable Fixed", "Total Make"]
        make_vals = [5.0, 4.0, 2.5, 3.0, 14.5]
        buy_vals = [0, 0, 0, 0, 15.0]

        fig1 = go.Figure(data=[
            go.Bar(name="Make", x=make_elements, y=make_vals, marker_color="#2E86C1",
                   text=[f"${v:.2f}" for v in make_vals], textposition="auto"),
            go.Bar(name="Buy", x=make_elements, y=buy_vals, marker_color="#E74C3C",
                   text=[f"${v:.2f}" if v > 0 else "" for v in buy_vals], textposition="auto")
        ])
        fig1.update_layout(title="Make vs Buy — Cost per Unit Comparison", barmode="group", yaxis_title="Cost per Unit ($)")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Product Mix — CM per Machine Hour Ranking")
        products_viz = ["Product Alpha\n(4 MH, $20 CM)", "Product Beta\n(2 MH, $30 CM)", "Product Gamma\n(2 MH, $20 CM)"]
        cm_per_mh = [5.0, 15.0, 10.0]
        colors_viz = ["#E74C3C", "#27AE60", "#E67E22"]

        fig2 = go.Figure(go.Bar(
            x=products_viz, y=cm_per_mh,
            marker_color=colors_viz,
            text=[f"${v:.2f}/MH" for v in cm_per_mh], textposition="auto"
        ))
        fig2.add_hline(y=10, line_dash="dash", annotation_text="Average CM/MH", line_color="navy")
        fig2.update_layout(title="Contribution Margin per Machine Hour — Ranking (Highest = Produce First!)",
                           yaxis_title="CM per Machine Hour ($)")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Special Order — Incremental Revenue vs Cost")
        spec_categories = ["Revenue", "Variable Cost", "Net Benefit"]
        spec_vals = [224000, 144000, 80000]
        spec_colors = ["#27AE60", "#E74C3C", "#2E86C1"]
        fig3 = go.Figure(go.Bar(
            x=spec_categories, y=spec_vals,
            marker_color=spec_colors,
            text=[f"${v:,}" for v in spec_vals], textposition="auto"
        ))
        fig3.update_layout(title="Special Order — Incremental Analysis (8,000 units @ $28)", yaxis_title="Amount ($)")
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Drop/Keep — Net Impact Analysis")
        items = ["CM Lost", "Fixed Costs Saved", "Net Impact"]
        vals = [-50000, 60000, 10000]
        cols_drop = ["#E74C3C", "#27AE60", "#2E86C1"]
        fig4 = go.Figure(go.Bar(
            x=items, y=vals, marker_color=cols_drop,
            text=[f"${abs(v):,}" for v in vals], textposition="auto"
        ))
        fig4.add_hline(y=0, line_color="black", line_width=2)
        fig4.update_layout(title="Drop/Keep Decision — Net Impact of Dropping", yaxis_title="Amount ($)")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. A sunk cost is:**")
        q1 = st.radio("", [
            "A cost that differs between alternatives",
            "A future cost relevant to decisions",
            "A cost already incurred that cannot be changed",
            "An opportunity cost"
        ], key="m11q1")
        if st.button("Check Q1", key="m11c1"):
            if q1 == "A cost already incurred that cannot be changed":
                st.success("✅ Correct! Sunk costs are past costs — irrelevant to future decisions.")
            else:
                st.error("❌ Incorrect. A sunk cost is already incurred and cannot be changed by any future decision — always irrelevant!")

        st.markdown("---")
        st.markdown("**Q2. When accepting a special order with excess capacity, fixed overhead is:**")
        q2 = st.radio("", [
            "Relevant — must be included",
            "Irrelevant — does not change",
            "Variable — changes with the order",
            "Avoidable — can be eliminated"
        ], key="m11q2")
        if st.button("Check Q2", key="m11c2"):
            if q2 == "Irrelevant — does not change":
                st.success("✅ Correct! Fixed overhead doesn't change when you accept the special order — it's irrelevant!")
            else:
                st.error("❌ Incorrect. Fixed overhead is irrelevant to special order decisions because it doesn't change.")

        st.markdown("---")
        st.markdown("""
        **Q3. Products A and B have CM/unit of $20 and $30. Product A needs 2 machine hours; B needs 4 hours.
        Machine hours are limited. Which product should be prioritized?**
        """)
        q3 = st.radio("", [
            "Product B — higher CM per unit",
            "Product A — higher CM per machine hour ($10/MH vs $7.50/MH)",
            "Both equally — produce same amount",
            "Product B — more profitable overall"
        ], key="m11q3")
        if st.button("Check Q3", key="m11c3"):
            if q3 == "Product A — higher CM per machine hour ($10/MH vs $7.50/MH)":
                st.success("✅ Correct! A: $20/2hrs = $10/MH. B: $30/4hrs = $7.50/MH. Prioritize A!")
            else:
                st.error("❌ Incorrect. With a constraint, rank by CM per scarce resource. A: $10/MH vs B: $7.50/MH → Prioritize A!")

        st.markdown("---")
        st.markdown("""
        **Q4. A segment has CM of $80,000 and traceable fixed costs of $100,000 ($70,000 avoidable).
        Net impact of dropping = ?**
        """)
        q4 = st.radio("", ["$20,000 benefit from dropping", "$10,000 loss from dropping", "$10,000 benefit from dropping", "$30,000 loss from dropping"], key="m11q4")
        if st.button("Check Q4", key="m11c4"):
            net = -80000 + 70000
            if q4 == "$10,000 loss from dropping":
                st.success(f"✅ Correct! −CM ($80,000) + Avoidable Fixed Saved ($70,000) = ${net:,} → ${abs(net):,} loss. KEEP it!")
            else:
                st.error(f"❌ Incorrect. Net = −$80,000 CM + $70,000 saved = −$10,000. Dropping REDUCES profit by $10,000 → Keep!")

        st.markdown("---")
        st.markdown("**Q5. In a make-or-buy decision, unavoidable fixed costs are:**")
        q5 = st.radio("", [
            "Relevant — must be included in the analysis",
            "Irrelevant — continue regardless of decision",
            "Variable — change with production volume",
            "Avoidable — eliminated by buying"
        ], key="m11q5")
        if st.button("Check Q5", key="m11c5"):
            if q5 == "Irrelevant — continue regardless of decision":
                st.success("✅ Correct! Unavoidable fixed costs don't change whether you make or buy — they're irrelevant!")
            else:
                st.error("❌ Incorrect. Unavoidable fixed costs are irrelevant — they continue regardless of whether you make or buy.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Decision Framework Summary")
        decision_df = pd.DataFrame({
            "Decision": ["Special Order", "Make or Buy", "Drop Segment", "Product Mix", "Process Further"],
            "Accept/Choose if...": [
                "Incremental Revenue > Incremental Cost (incl. opportunity cost)",
                "Total relevant cost to Make < Purchase Price",
                "CM Lost < Avoidable Fixed Costs Saved",
                "Highest CM per unit of scarce resource (not CM per unit!)",
                "Incremental Revenue > Incremental Separable Costs"
            ],
            "Key Irrelevant Cost": [
                "Fixed overhead (doesn't change)",
                "Unavoidable fixed costs",
                "Common and unavoidable fixed costs",
                "Fixed costs don't affect the ranking",
                "Joint costs (sunk!)"
            ]
        })
        st.dataframe(decision_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Relevant Cost Identification Rules")
        rules_df = pd.DataFrame({
            "Cost Type": ["Future, differs between alternatives", "Sunk cost (already incurred)",
                           "Future cost, same in all alternatives", "Opportunity cost",
                           "Avoidable fixed cost", "Unavoidable fixed cost"],
            "Relevant?": ["✅ Yes", "❌ No", "❌ No", "✅ Yes — always!", "✅ Yes", "❌ No"],
            "Example": [
                "Variable manufacturing cost for special order",
                "Original purchase price of old machine",
                "Fixed rent when comparing products",
                "CM lost by diverting resources",
                "Supervisory cost eliminated if segment dropped",
                "Head office allocation that continues regardless"
            ]
        })
        st.dataframe(rules_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Including fixed overhead in special order analysis",
                "Forgetting opportunity costs in make-or-buy",
                "Ranking products by CM/unit instead of CM/constraint",
                "Treating unavoidable fixed costs as savings when dropping segment",
                "Including sunk costs in equipment replacement decisions",
                "Ignoring qualitative factors (quality, reliability, strategy)"
            ],
            "Correct Approach": [
                "Fixed OH doesn't change with special order — exclude it",
                "Full capacity = include opportunity cost (lost external CM)",
                "With constraints, rank by CM per unit of scarce resource",
                "Only count avoidable fixed costs as savings",
                "Original purchase price is sunk — only consider future cash flows",
                "Always consider non-financial factors alongside quantitative analysis"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 11 Complete! You can apply differential analysis to all major short-term decisions.")
        st.info("💡 Next: Module 12 — Capital Budgeting")

if __name__ == "__main__":
    show()