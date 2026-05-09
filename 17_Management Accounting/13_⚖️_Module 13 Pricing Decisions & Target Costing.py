import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏷️ Module 13: Pricing Decisions & Target Costing")
    st.markdown("*Set optimal prices and engineer costs to meet market-driven targets*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Pricing Approaches Overview")
        st.markdown("""
        There are two fundamental pricing philosophies:

        | Approach | Logic | Used When |
        |---------|-------|----------|
        | **Cost-Plus Pricing** | Start with cost, add markup | Cost-based industries, regulated markets |
        | **Target Costing** | Start with market price, work back to allowable cost | Competitive markets, consumer goods |

        #### Key Pricing Considerations:
        - Customer demand and price elasticity
        - Competitor pricing
        - Company cost structure
        - Desired profit margins
        - Strategic positioning (premium vs. value)
        - Product life cycle stage
        """)

        st.subheader("2. Cost-Plus Pricing Methods")
        st.markdown("""
        **Start with cost, add a markup percentage.**

        #### A. Absorption Cost-Plus:
        ```
        Base: Full Absorption Cost per Unit (DM + DL + Variable OH + Fixed OH)
        Selling Price = Absorption Cost + (Markup % × Absorption Cost)

        Markup % chosen to cover: S&A expenses + desired profit
        ```

        #### B. Variable Cost-Plus (Contribution Approach):
        ```
        Base: Variable Cost per Unit
        Selling Price = Variable Cost + (Markup % × Variable Cost)

        Markup % chosen to cover: Fixed costs + desired profit
        ```

        #### C. Total Cost-Plus:
        ```
        Base: Total Cost per Unit (manufacturing + S&A)
        Selling Price = Total Cost + (Markup % × Total Cost)

        Markup % chosen to earn desired return on investment
        ```

        #### D. Time-and-Materials Pricing (Service Industries):
        ```
        Labor Rate = Hourly Wage + Overhead per Hour + Profit per Hour
        Materials Charge = Cost of Materials + Materials Handling Markup

        Total Price = (Hours × Labor Rate) + Materials Charge
        ```
        """)

        st.subheader("3. Markup Determination — Return on Investment (ROI) Method")
        st.markdown("""
        Calculate the required markup to earn a target ROI:

        ```
        Step 1: Required Return = Target ROI % × Invested Capital
        Step 2: Required Markup ($) = Required Return + S&A Expenses
        Step 3: Markup % = Required Markup / (Volume × Unit Cost) × 100
        Step 4: Price = Unit Cost × (1 + Markup %)

        OR using formula directly:
        Required Markup % on Manufacturing Cost =
        (Required Return + S&A Expenses) / (Unit Volume × Manufacturing Cost per Unit)
        ```
        """)

        st.subheader("4. Target Costing")
        st.markdown("""
        **Target Costing** works backwards from the market — used when price is set by competition.

        ```
        Step 1: Determine Target Selling Price
                (What will the market pay?)

        Step 2: Determine Target Profit Margin
                (What return do we need?)

        Step 3: Calculate Allowable (Target) Cost
                Target Cost = Target Price − Target Profit Margin

        Step 4: Engineer the product to meet the target cost
                Use value engineering to eliminate waste while maintaining value
        ```

        **Key Insight:** Under target costing, cost is a CONSTRAINT set by the market,
        not a result of production decisions!

        **If Estimated Cost > Target Cost:**
        - Redesign the product
        - Find cheaper materials
        - Improve processes
        - Negotiate with suppliers
        - OR abandon the product if target cannot be met
        """)

        st.subheader("5. Value Engineering")
        st.markdown("""
        **Value Engineering:** Systematic process of reducing costs while maintaining or improving customer value.

        #### Two Types of Value:
        - **Use Value**: The function performed (what the product does)
        - **Esteem Value**: The satisfaction derived from owning the product

        #### Value Engineering Process:
        1. Identify customer value: What do customers ACTUALLY value?
        2. Function analysis: What does each component DO?
        3. Evaluate alternatives: Can this function be performed cheaper?
        4. Eliminate non-value features: What can be removed without reducing value?
        5. Target new cost: Redesign to meet cost target

        #### Cost Tables:
        Databases showing how costs change with different design choices, materials, and processes.
        """)

        st.subheader("6. Life-Cycle Costing")
        st.markdown("""
        **Life-Cycle Costing:** Considers ALL costs over a product's entire life cycle.

        ```
        Life-Cycle Costs:
        ├── Development Phase:  R&D, design, prototype
        ├── Production Phase:   Manufacturing, quality control
        ├── Marketing Phase:    Advertising, distribution, sales
        └── Customer Phase:     Installation, maintenance, disposal

        Life-Cycle Price = Σ (All phase costs) + Required Profit
        ```

        **80% Rule:** Up to 80% of a product's costs are **locked in** during the design phase,
        even though most are incurred later during production and service.
        This is why design decisions are so critical!
        """)

        st.subheader("7. Kaizen Costing")
        st.markdown("""
        **Kaizen** (改善) = Japanese for "continuous improvement"

        While target costing focuses on new products, **Kaizen costing** reduces costs
        on EXISTING products during the production phase.

        ```
        Kaizen Cost Reduction Cycle:
        1. Establish current cost baseline
        2. Set continuous improvement targets (e.g., reduce costs 2% per quarter)
        3. Implement process improvements
        4. Track and measure cost reductions
        5. Set new target and repeat
        ```

        **Key Difference:**
        - Target Costing → New products, design stage
        - Kaizen Costing → Existing products, production stage
        """)

        st.subheader("8. Pricing Strategies")
        st.markdown("""
        | Strategy | Description | When to Use |
        |---------|-------------|-------------|
        | **Premium Pricing** | High price for high quality/prestige | Strong brand, differentiated product |
        | **Penetration Pricing** | Low price to gain market share | New market entry, price-sensitive market |
        | **Skimming** | High initial price, then lower | Innovative products, tech market |
        | **Competitive Pricing** | Match or beat competitors | Commodity markets |
        | **Value-Based Pricing** | Price based on perceived customer value | Strong differentiation |
        | **Predatory Pricing** | Below cost to eliminate competition | Illegal in many jurisdictions ⚠️ |
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Absorption Cost-Plus Pricing")
        st.markdown("""
        **Product Data (10,000 units):**
        | Cost Item | Amount |
        |-----------|--------|
        | Direct Materials | $15/unit |
        | Direct Labor | $10/unit |
        | Variable Mfg OH | $8/unit |
        | Fixed Mfg OH | $60,000 total |
        | Variable S&A | $5/unit |
        | Fixed S&A | $30,000 total |
        | Desired ROI | 20% on $500,000 investment |

        **Step 1 — Absorption Cost per Unit:**
        ```
        Direct Materials            $15.00
        Direct Labor                $10.00
        Variable Mfg OH              $8.00
        Fixed Mfg OH ($60K/10K)      $6.00
        ────────────────────────────────────
        Absorption Cost per Unit    $39.00
        ```

        **Step 2 — Required Markup:**
        ```
        Required Return: 20% × $500,000     = $100,000
        Variable S&A: $5 × 10,000           = $50,000
        Fixed S&A:                          = $30,000
        ────────────────────────────────────────────────
        Total Required Markup               = $180,000

        Markup % = $180,000 / (10,000 × $39) = 46.15%
        ```

        **Step 3 — Selling Price:**
        ```
        Price = $39.00 × (1 + 46.15%) = $39.00 × 1.4615 = $57.00/unit
        ```

        **Verification:**
        ```
        Revenue: 10,000 × $57         = $570,000
        Manufacturing costs           = ($390,000)
        S&A expenses                  = ($80,000)
        ────────────────────────────────────────────
        Operating Income              = $100,000 = 20% × $500,000 ✓
        ```
        """)

        st.subheader("Example 2: Target Costing")
        st.markdown("""
        **Market Research shows:**
        - Competitors price at $50
        - To win market share, target price = $48
        - Company needs 20% profit margin
        - Estimated current cost = $42 per unit

        **Target Cost Calculation:**
        ```
        Target Selling Price         = $48.00
        − Target Profit (20% × $48)  = ($9.60)
        ────────────────────────────────────────
        Target (Allowable) Cost      = $38.40

        Current Estimated Cost       = $42.00
        Required Cost Reduction      = $3.60 per unit
        ```

        **Value Engineering Actions to Close the $3.60 Gap:**
        ```
        1. Substitute cheaper material (saves $1.20/unit)
        2. Redesign assembly process (saves $0.80/unit)
        3. Reduce packaging weight (saves $0.60/unit)
        4. Consolidate component suppliers (saves $1.00/unit)
        ────────────────────────────────────────────────────────
        Total savings                            $3.60 ✅

        New estimated cost = $42.00 − $3.60 = $38.40 = Target Cost!
        ```
        """)

        st.subheader("Example 3: Time-and-Materials Pricing")
        st.markdown("""
        **Auto Repair Shop:**
        - Mechanic hourly wage: $30/hr
        - Overhead allocation per labor hour: $25
        - Desired profit per labor hour: $15
        - Parts cost for a job: $200
        - Materials handling markup: 25%

        ```
        Labor Rate per Hour:
        Wage                    $30
        Overhead                $25
        Profit                  $15
        ──────────────────────────────────
        Total Rate per Hour     $70

        Materials Charge:
        Parts cost:           $200.00
        + 25% handling:        $50.00
        Total:                $250.00

        For a 3-hour job:
        Labor: 3 hrs × $70    = $210.00
        Materials:             = $250.00
        ──────────────────────────────────
        Total Price            = $460.00
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Calculator:", [
            "🏭 Absorption Cost-Plus Pricing",
            "📊 Variable Cost-Plus Pricing",
            "🎯 Target Costing Analysis",
            "🔧 Time-and-Materials Pricing",
            "📈 ROI Markup Calculator",
            "🔄 Kaizen Cost Improvement"
        ])

        if calc_choice == "🏭 Absorption Cost-Plus Pricing":
            st.subheader("Absorption Cost-Plus Pricing Calculator")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Manufacturing Costs:**")
                dm_unit = st.number_input("Direct Materials ($/unit)", 0.0, value=15.0, step=0.5)
                dl_unit = st.number_input("Direct Labor ($/unit)", 0.0, value=10.0, step=0.5)
                var_oh_unit = st.number_input("Variable Mfg Overhead ($/unit)", 0.0, value=8.0, step=0.5)
                fixed_mfg_total = st.number_input("Total Fixed Mfg OH ($)", 0.0, value=60000.0, step=1000.0)
                volume = st.number_input("Budgeted Volume (units)", 1, value=10000, step=100)

            with col2:
                st.markdown("**S&A and Return Requirements:**")
                var_sa_unit = st.number_input("Variable S&A ($/unit)", 0.0, value=5.0, step=0.5)
                fixed_sa_total = st.number_input("Total Fixed S&A ($)", 0.0, value=30000.0, step=1000.0)
                target_roi = st.number_input("Target ROI (%)", 0.0, value=20.0, step=1.0)
                invested_capital = st.number_input("Invested Capital ($)", 0.0, value=500000.0, step=10000.0)

            if st.button("🧮 Calculate Absorption Cost-Plus Price", type="primary"):
                fixed_oh_unit = fixed_mfg_total / volume if volume > 0 else 0
                absorption_cost = dm_unit + dl_unit + var_oh_unit + fixed_oh_unit

                required_return = target_roi / 100 * invested_capital
                total_var_sa = var_sa_unit * volume
                total_markup_needed = required_return + total_var_sa + fixed_sa_total
                markup_pct = total_markup_needed / (volume * absorption_cost) * 100 if (volume * absorption_cost) > 0 else 0
                selling_price = absorption_cost * (1 + markup_pct / 100)

                st.markdown("---")
                st.markdown("### Cost Build-Up:")
                cost_df = pd.DataFrame({
                    "Cost Element": ["Direct Materials", "Direct Labor", "Variable Mfg OH",
                                      "Fixed Mfg OH (per unit)", "Absorption Cost per Unit",
                                      "Markup (per unit)", "SELLING PRICE"],
                    "Per Unit": [f"${dm_unit:.2f}", f"${dl_unit:.2f}", f"${var_oh_unit:.2f}",
                                  f"${fixed_oh_unit:.2f}", f"${absorption_cost:.2f}",
                                  f"${absorption_cost * markup_pct/100:.2f}",
                                  f"${selling_price:.2f}"]
                })
                st.dataframe(cost_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Absorption Cost", f"${absorption_cost:.2f}/unit")
                with col2: st.metric("Required Markup %", f"{markup_pct:.2f}%")
                with col3: st.metric("Selling Price", f"${selling_price:.2f}/unit")

                total_revenue = selling_price * volume
                total_mfg = absorption_cost * volume
                total_sa = var_sa_unit * volume + fixed_sa_total
                operating_income = total_revenue - total_mfg - total_sa
                actual_roi = operating_income / invested_capital * 100 if invested_capital > 0 else 0

                st.markdown("### Verification:")
                verif_df = pd.DataFrame({
                    "Item": ["Total Revenue", "Total Mfg Costs", "Total S&A",
                              "Operating Income", "ROI Achieved"],
                    "Amount": [f"${total_revenue:,.2f}", f"(${total_mfg:,.2f})",
                                f"(${total_sa:,.2f})", f"${operating_income:,.2f}",
                                f"{actual_roi:.2f}%"]
                })
                st.dataframe(verif_df, use_container_width=True, hide_index=True)

                if abs(actual_roi - target_roi) < 0.01:
                    st.success(f"✅ Target ROI of {target_roi:.1f}% achieved at price ${selling_price:.2f}!")

        elif calc_choice == "📊 Variable Cost-Plus Pricing":
            st.subheader("Variable (Contribution) Cost-Plus Pricing Calculator")

            col1, col2 = st.columns(2)
            with col1:
                vc_dm = st.number_input("Variable DM ($/unit)", 0.0, value=15.0, step=0.5)
                vc_dl = st.number_input("Variable DL ($/unit)", 0.0, value=10.0, step=0.5)
                vc_mfg_oh = st.number_input("Variable Mfg OH ($/unit)", 0.0, value=8.0, step=0.5)
                vc_sa = st.number_input("Variable S&A ($/unit)", 0.0, value=5.0, step=0.5)
            with col2:
                total_fixed = st.number_input("Total Fixed Costs ($)", 0.0, value=90000.0, step=1000.0)
                target_profit_vc = st.number_input("Target Profit ($)", 0.0, value=100000.0, step=1000.0)
                volume_vc = st.number_input("Expected Volume (units)", 1, value=10000, step=100)

            total_vc_unit = vc_dm + vc_dl + vc_mfg_oh + vc_sa
            total_markup_vc = total_fixed + target_profit_vc
            markup_pct_vc = total_markup_vc / (volume_vc * total_vc_unit) * 100 if (volume_vc * total_vc_unit) > 0 else 0
            price_vc = total_vc_unit * (1 + markup_pct_vc / 100)
            cm_unit = price_vc - total_vc_unit
            cm_ratio = cm_unit / price_vc * 100 if price_vc > 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Variable Cost per Unit", f"${total_vc_unit:.2f}")
            with col2: st.metric("Required Markup %", f"{markup_pct_vc:.2f}%")
            with col3: st.metric("Selling Price", f"${price_vc:.2f}")

            col1, col2 = st.columns(2)
            with col1: st.metric("Contribution Margin per Unit", f"${cm_unit:.2f}")
            with col2: st.metric("CM Ratio", f"{cm_ratio:.1f}%")

            total_cm = cm_unit * volume_vc
            profit = total_cm - total_fixed
            col1, col2 = st.columns(2)
            with col1: st.metric("Total Contribution Margin", f"${total_cm:,.2f}")
            with col2: st.metric("Operating Profit", f"${profit:,.2f}")

        elif calc_choice == "🎯 Target Costing Analysis":
            st.subheader("Target Costing Calculator")

            col1, col2 = st.columns(2)
            with col1:
                market_price = st.number_input("Market / Target Selling Price ($)", 0.0, value=48.0, step=1.0)
                target_profit_pct = st.number_input("Target Profit Margin (%)", 0.0, 100.0, 20.0, step=1.0)

            with col2:
                st.markdown("**Current Estimated Costs (per unit):**")
                curr_dm = st.number_input("Current Direct Materials", 0.0, value=18.0, step=0.5)
                curr_dl = st.number_input("Current Direct Labor", 0.0, value=12.0, step=0.5)
                curr_oh = st.number_input("Current Overhead", 0.0, value=8.0, step=0.5)
                curr_sa = st.number_input("Current S&A", 0.0, value=4.0, step=0.5)

            target_profit = market_price * target_profit_pct / 100
            target_cost = market_price - target_profit
            current_cost = curr_dm + curr_dl + curr_oh + curr_sa
            cost_gap = current_cost - target_cost

            st.markdown("---")
            st.markdown("### Target Cost Analysis:")
            target_df = pd.DataFrame({
                "Item": ["Target Selling Price", f"Target Profit ({target_profit_pct:.0f}%)",
                          "Target (Allowable) Cost", "Current Estimated Cost", "Cost Gap (must reduce by)"],
                "Amount": [f"${market_price:.2f}", f"(${target_profit:.2f})",
                            f"${target_cost:.2f}", f"${current_cost:.2f}",
                            f"${cost_gap:.2f}"]
            })
            st.dataframe(target_df, use_container_width=True, hide_index=True)

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Target Cost", f"${target_cost:.2f}")
            with col2: st.metric("Current Cost", f"${current_cost:.2f}")
            with col3: st.metric("Required Reduction", f"${cost_gap:.2f}", delta=f"{cost_gap/current_cost*100:.1f}% of cost")

            if cost_gap > 0:
                st.error(f"❌ Current cost (${current_cost:.2f}) exceeds target (${target_cost:.2f}) by ${cost_gap:.2f}. Value engineering needed!")
                st.markdown("### Value Engineering — Cost Reduction Plan:")
                num_actions = st.number_input("Number of Cost Reduction Actions", 1, 8, 4)
                total_savings = 0
                action_rows = []
                for i in range(int(num_actions)):
                    col1, col2, col3 = st.columns(3)
                    with col1: action_desc = st.text_input("Action", value=f"Redesign action {i+1}", key=f"tc_a_{i}")
                    with col2: action_type = st.selectbox("Area", ["Materials", "Labor", "Overhead", "S&A"], key=f"tc_t_{i}")
                    with col3: savings = st.number_input("Savings ($/unit)", 0.0, value=cost_gap/4, step=0.1, key=f"tc_s_{i}")
                    total_savings += savings
                    action_rows.append({"Action": action_desc, "Area": action_type, "Savings": f"${savings:.2f}"})

                if action_rows:
                    st.dataframe(pd.DataFrame(action_rows), use_container_width=True, hide_index=True)
                    remaining_gap = cost_gap - total_savings
                    if remaining_gap <= 0:
                        st.success(f"✅ Target achievable! Total savings ${total_savings:.2f} closes the gap of ${cost_gap:.2f}!")
                    else:
                        st.warning(f"⚠️ Still ${remaining_gap:.2f} short of target. Need more engineering actions or reconsider product.")
            else:
                st.success(f"✅ Current cost (${current_cost:.2f}) is at or below target (${target_cost:.2f}). Product is viable!")

        elif calc_choice == "🔧 Time-and-Materials Pricing":
            st.subheader("Time-and-Materials Pricing Calculator")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Labor Rate Components:**")
                hourly_wage = st.number_input("Hourly Wage Rate ($)", 0.0, value=30.0, step=1.0)
                oh_per_hour = st.number_input("Overhead per Labor Hour ($)", 0.0, value=25.0, step=1.0)
                profit_per_hour = st.number_input("Desired Profit per Hour ($)", 0.0, value=15.0, step=1.0)

            with col2:
                st.markdown("**Materials Components:**")
                materials_markup_pct = st.number_input("Materials Handling Markup (%)", 0.0, value=25.0, step=5.0)

            labor_rate = hourly_wage + oh_per_hour + profit_per_hour

            st.markdown("### Price a Specific Job:")
            col1, col2 = st.columns(2)
            with col1:
                hours_worked = st.number_input("Labor Hours for Job", 0.0, value=3.0, step=0.5)
            with col2:
                materials_cost = st.number_input("Materials Cost ($)", 0.0, value=200.0, step=10.0)

            labor_charge = hours_worked * labor_rate
            materials_charge = materials_cost * (1 + materials_markup_pct / 100)
            total_job_price = labor_charge + materials_charge

            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Labor Rate per Hour", f"${labor_rate:.2f}")
                st.metric("Labor Charge", f"${labor_charge:.2f}")
            with col2:
                st.metric("Materials Handling Charge", f"${materials_charge - materials_cost:.2f}")
                st.metric("Total Materials Charge", f"${materials_charge:.2f}")

            st.metric("TOTAL JOB PRICE", f"${total_job_price:.2f}")

            st.markdown(f"""
            **Job Price Breakdown:**
            ```
            LABOR:
            Hourly Wage:           ${hourly_wage:.2f}/hr
            Overhead:              ${oh_per_hour:.2f}/hr
            Profit:                ${profit_per_hour:.2f}/hr
            ─────────────────────────────────────────────
            Labor Rate:            ${labor_rate:.2f}/hr
            × Hours:               {hours_worked:.1f} hrs
            Labor Charge:          ${labor_charge:.2f}

            MATERIALS:
            Materials Cost:        ${materials_cost:.2f}
            + Markup ({materials_markup_pct:.0f}%):       ${materials_cost*materials_markup_pct/100:.2f}
            Materials Charge:      ${materials_charge:.2f}

            ═════════════════════════════════════════════
            TOTAL JOB PRICE:       ${total_job_price:.2f}
            ```
            """)

        elif calc_choice == "📈 ROI Markup Calculator":
            st.subheader("ROI-Based Markup Calculator")
            col1, col2 = st.columns(2)
            with col1:
                roi_inv = st.number_input("Invested Capital ($)", 0.0, value=500000.0, step=10000.0)
                roi_target = st.number_input("Target ROI (%)", 0.0, value=20.0, step=1.0)
                roi_volume = st.number_input("Budgeted Volume (units)", 1, value=10000, step=100)
            with col2:
                roi_mfg_cost = st.number_input("Manufacturing Cost per Unit ($)", 0.0, value=39.0, step=0.5)
                roi_sa = st.number_input("Total S&A Expenses ($)", 0.0, value=80000.0, step=1000.0)

            roi_req_return = roi_target / 100 * roi_inv
            roi_markup_needed = roi_req_return + roi_sa
            roi_markup_pct = roi_markup_needed / (roi_volume * roi_mfg_cost) * 100 if (roi_volume * roi_mfg_cost) > 0 else 0
            roi_price = roi_mfg_cost * (1 + roi_markup_pct / 100)

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Required Return", f"${roi_req_return:,.2f}")
            with col2: st.metric("Required Markup %", f"{roi_markup_pct:.2f}%")
            with col3: st.metric("Selling Price", f"${roi_price:.2f}")

        else:  # Kaizen Costing
            st.subheader("Kaizen Cost Improvement Tracker")
            current_cost_base = st.number_input("Current Cost per Unit ($)", 0.0, value=42.0, step=0.5)
            improvement_pct = st.number_input("Quarterly Improvement Target (%)", 0.0, value=2.0, step=0.1)
            num_quarters = st.number_input("Number of Quarters", 1, 20, 8)

            quarters = []
            costs = []
            cost = current_cost_base
            cum_savings = 0
            rows = []
            for q in range(int(num_quarters)):
                reduction = cost * improvement_pct / 100
                new_cost = cost - reduction
                cum_savings += reduction
                quarters.append(f"Q{q+1}")
                costs.append(new_cost)
                rows.append({
                    "Quarter": f"Q{q+1}",
                    "Start Cost": f"${cost:.3f}",
                    "Reduction ({:.1f}%)".format(improvement_pct): f"${reduction:.3f}",
                    "End Cost": f"${new_cost:.3f}",
                    "Cum. Savings": f"${cum_savings:.3f}"
                })
                cost = new_cost

            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Starting Cost", f"${current_cost_base:.2f}")
            with col2: st.metric(f"Cost After {int(num_quarters)} Quarters", f"${cost:.2f}")
            with col3: st.metric("Total Cost Reduction", f"${current_cost_base - cost:.2f}", f"{(current_cost_base - cost)/current_cost_base*100:.1f}%")

            fig_kai = go.Figure(go.Scatter(x=quarters, y=costs, mode="lines+markers",
                                            line=dict(color="#27AE60", width=3), marker=dict(size=8)))
            fig_kai.add_hline(y=current_cost_base, line_dash="dash", annotation_text="Baseline Cost", line_color="red")
            fig_kai.update_layout(title=f"Kaizen Cost Reduction ({improvement_pct:.1f}% per quarter)",
                                   xaxis_title="Quarter", yaxis_title="Cost per Unit ($)")
            st.plotly_chart(fig_kai, use_container_width=True)

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Cost-Plus vs Target Costing Philosophy")
        fig1 = go.Figure()
        fig1.add_trace(go.Funnel(
            name="Cost-Plus", orientation="h",
            y=["Production Cost", "+ Markup", "= Selling Price"],
            x=[39, 18, 57],
            textinfo="value+label",
            marker=dict(color=["#2E86C1", "#3498DB", "#AED6F1"])
        ))
        fig1.update_layout(title="Cost-Plus Pricing: Start with Cost, Add Markup")
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = go.Figure()
        fig2.add_trace(go.Funnel(
            name="Target Costing", orientation="h",
            y=["Market Price", "− Profit Margin", "= Target Cost"],
            x=[48, 9.6, 38.4],
            textinfo="value+label",
            marker=dict(color=["#27AE60", "#2ECC71", "#82E0AA"])
        ))
        fig2.update_layout(title="Target Costing: Start with Market Price, Work Back")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Life-Cycle Cost Lock-In")
        stages = ["Design\nPhase", "Development", "Production", "Marketing", "Customer\nService"]
        costs_locked = [80, 10, 5, 3, 2]
        costs_incurred = [5, 15, 40, 25, 15]

        fig3 = go.Figure()
        fig3.add_trace(go.Bar(name="% Costs LOCKED IN at Stage", x=stages, y=costs_locked,
                               marker_color="#E74C3C", yaxis="y"))
        fig3.add_trace(go.Scatter(name="% Costs INCURRED at Stage", x=stages, y=costs_incurred,
                                   mode="lines+markers", line=dict(color="#2E86C1", width=3),
                                   marker=dict(size=10), yaxis="y2"))
        fig3.update_layout(
            title="Life-Cycle Costing: 80% of Costs Locked In at Design Stage!",
            yaxis=dict(title="% Costs Locked In (bar)", side="left"),
            yaxis2=dict(title="% Costs Incurred (line)", overlaying="y", side="right")
        )
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Markup % vs Return on Sales")
        cost_vals = [20, 30, 40, 50]
        markup_pcts = [10, 20, 30, 40, 50]
        fig4 = go.Figure()
        for cost in cost_vals:
            prices = [cost * (1 + m/100) for m in markup_pcts]
            ros = [cost * (m/100) / price * 100 for m, price in zip(markup_pcts, prices)]
            fig4.add_trace(go.Scatter(x=markup_pcts, y=ros, mode="lines+markers", name=f"Cost=${cost}"))
        fig4.update_layout(title="Markup % vs Return on Sales % (for different cost levels)",
                           xaxis_title="Markup % on Cost", yaxis_title="Return on Sales %")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. Target costing starts with:**")
        q1 = st.radio("", [
            "The manufacturing cost and adds a markup",
            "The desired profit and adds to costs",
            "The market price and subtracts the required profit",
            "The variable cost and applies contribution approach"
        ], key="m13q1")
        if st.button("Check Q1", key="m13c1"):
            if q1 == "The market price and subtracts the required profit":
                st.success("✅ Correct! Target Cost = Market Price − Required Profit Margin")
            else:
                st.error("❌ Incorrect. Target costing starts with the market price and works backwards: Target Cost = Market Price − Required Profit.")

        st.markdown("---")
        st.markdown("""
        **Q2. Market price = $80. Target margin = 25%. Target cost = ?**
        """)
        q2 = st.radio("", ["$20", "$60", "$80", "$100"], key="m13q2")
        if st.button("Check Q2", key="m13c2"):
            if q2 == "$60":
                target = 80 * (1 - 0.25)
                st.success(f"✅ Correct! Target Cost = $80 × (1 − 25%) = ${target:.2f}")
            else:
                st.error("❌ Incorrect. Target Cost = $80 − (25% × $80) = $80 − $20 = $60")

        st.markdown("---")
        st.markdown("**Q3. Value engineering is best described as:**")
        q3 = st.radio("", [
            "Adding more features to justify a higher price",
            "Reducing costs while maintaining customer value",
            "Increasing the markup percentage",
            "Cutting quality to reduce costs"
        ], key="m13q3")
        if st.button("Check Q3", key="m13c3"):
            if q3 == "Reducing costs while maintaining customer value":
                st.success("✅ Correct! Value engineering reduces costs without reducing customer-perceived value.")
            else:
                st.error("❌ Incorrect. Value engineering systematically reduces costs while MAINTAINING or improving customer value.")

        st.markdown("---")
        st.markdown("**Q4. The 80% rule in life-cycle costing means:**")
        q4 = st.radio("", [
            "80% of costs are variable",
            "80% of revenue comes from 20% of products",
            "80% of product costs are locked in during the design phase",
            "80% of customers are profitable"
        ], key="m13q4")
        if st.button("Check Q4", key="m13c4"):
            if q4 == "80% of product costs are locked in during the design phase":
                st.success("✅ Correct! Design decisions lock in up to 80% of a product's total life-cycle costs.")
            else:
                st.error("❌ Incorrect. The 80% rule states that up to 80% of a product's costs are determined (locked in) during the design phase.")

        st.markdown("---")
        st.markdown("**Q5. Kaizen costing differs from target costing because:**")
        q5 = st.radio("", [
            "Kaizen applies to NEW products; target applies to existing products",
            "Kaizen focuses on continuous improvement of EXISTING products; target is for new products",
            "They are the same concept with different names",
            "Kaizen uses market prices; target uses cost-plus"
        ], key="m13q5")
        if st.button("Check Q5", key="m13c5"):
            if q5 == "Kaizen focuses on continuous improvement of EXISTING products; target is for new products":
                st.success("✅ Correct! Target costing = new product design. Kaizen costing = continuous improvement of existing products.")
            else:
                st.error("❌ Incorrect. Target costing applies to new products at design stage; Kaizen applies to existing products during production.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Pricing Methods Comparison")
        pricing_df = pd.DataFrame({
            "Method": ["Absorption Cost-Plus", "Variable Cost-Plus", "Target Costing", "Time & Materials", "ROI Pricing"],
            "Starting Point": ["Absorption cost/unit", "Variable cost/unit", "Market price", "Labor hours + materials", "Required ROI"],
            "Add/Subtract": ["+ Markup %", "+ Markup %", "− Profit margin", "+ OH + profit rate", "Required markup"],
            "= Result": ["Selling price", "Selling price", "Allowable cost", "Job price", "Selling price"],
            "Best For": ["Standard manufacturing", "Competitive bidding", "Competitive markets", "Service industries", "Investment centers"]
        })
        st.dataframe(pricing_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "Absorption Cost-Plus Price",
                "Variable Cost-Plus Price",
                "Target Cost",
                "Required Markup ($)",
                "Markup % on Manufacturing Cost",
                "Time & Materials Labor Rate",
                "After-Tax Salvage (for capital budgets)"
            ],
            "Expression": [
                "Absorption Unit Cost × (1 + Markup %)",
                "Variable Unit Cost × (1 + Markup %)",
                "Target Selling Price − Target Profit Margin",
                "Required Return + S&A Expenses",
                "Required Markup / (Volume × Unit Mfg Cost) × 100",
                "Hourly Wage + OH per Hour + Profit per Hour",
                "Market Value of Old Asset × (1 − Tax Rate) [if gain on disposal]"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Cost-Plus vs Target Costing")
        compare_df = pd.DataFrame({
            "Feature": ["Starting point", "Market orientation", "Price driver", "Cost driver", "When used", "Flexibility"],
            "Cost-Plus Pricing": [
                "Internal cost", "Low — ignores market", "Cost determines price",
                "Cost is what it is", "Regulated markets, custom products", "Low"
            ],
            "Target Costing": [
                "Market price", "High — market-driven", "Market determines price",
                "Cost must meet target", "Competitive markets, consumer goods", "High"
            ]
        })
        st.dataframe(compare_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Using cost-plus in highly competitive markets",
                "Ignoring market price when setting target",
                "Treating fixed costs as variable in short-term pricing",
                "Forgetting life-cycle costs in pricing decisions",
                "Using full cost for special orders (short-term)",
                "Abandoning target costing when gap seems too large"
            ],
            "Correct Approach": [
                "In competitive markets, start with market price → target costing",
                "Target cost must be achievable — conduct thorough value engineering",
                "In short-term, only variable costs are relevant to minimum price",
                "Consider all phases: design, production, marketing, service, disposal",
                "Special orders: minimum price = variable cost + opportunity cost",
                "Explore all value engineering options before abandoning the product"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 13 Complete! You can set prices using multiple methods and apply target costing in competitive markets.")
        st.info("💡 Next: Module 14 — Quality Management & Lean Accounting")

if __name__ == "__main__":
    show()