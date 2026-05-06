import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📈 Module 2: Cost Behavior and Cost-Volume-Profit Analysis")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators", 
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])
    
    with tab1:
        st.header("Core Concepts")
        
        st.subheader("1. Cost Behavior Patterns")
        
        st.markdown("""
        #### Variable Costs
        - **Definition**: Costs that change in direct proportion to activity level
        - **Per unit**: Constant
        - **Total**: Changes with activity
        - **Examples**: Direct materials, direct labor, sales commissions
        
        #### Fixed Costs
        - **Definition**: Costs that remain constant in total within relevant range
        - **Per unit**: Decreases as activity increases
        - **Total**: Constant (within relevant range)
        - **Examples**: Rent, salaries, depreciation
        
        #### Mixed Costs
        - **Definition**: Costs containing both variable and fixed components
        - **Formula**: Y = a + bX
          - Y = Total cost
          - a = Fixed component
          - b = Variable rate per unit
          - X = Activity level
        - **Examples**: Utilities, maintenance, phone bills
        
        #### Step Costs
        - Remain fixed over small ranges of activity
        - Jump to new higher level when capacity exceeded
        - **Example**: Supervisor salary (one supervisor per 20 workers)
        """)
        
        st.subheader("2. Methods to Analyze Mixed Costs")
        
        st.markdown("""
        #### High-Low Method
        1. Identify highest and lowest activity levels
        2. Calculate variable cost per unit:
           ```
           Variable Rate = (High Cost - Low Cost) / (High Activity - Low Activity)
           ```
        3. Calculate fixed cost:
           ```
           Fixed Cost = Total Cost - (Variable Rate × Activity Level)
           ```
        
        #### Scatter Diagram Method
        - Plot cost data points against activity levels
        - Visual inspection to identify patterns
        - Draw line of best fit
        
        #### Regression Analysis (Least Squares)
        - Statistical method for best fit line
        - Minimizes sum of squared deviations
        - Provides R² (goodness of fit measure)
        - Most accurate method
        """)
        
        st.subheader("3. Contribution Margin Concept")
        
        st.markdown("""
        #### Contribution Margin (CM)
        ```
        CM = Sales Revenue - Variable Costs
        ```
        
        #### Contribution Margin Ratio (CM Ratio)
        ```
        CM Ratio = Contribution Margin / Sales Revenue
        ```
        
        #### Contribution Margin Per Unit
        ```
        CM per Unit = Selling Price per Unit - Variable Cost per Unit
        ```
        
        **Key Insight**: CM represents the amount available to cover fixed costs and provide profit
        """)
        
        st.subheader("4. Break-Even Analysis")
        
        st.markdown("""
        #### Break-Even Point in Units
        ```
        BEP (units) = Fixed Costs / Contribution Margin per Unit
        ```
        
        #### Break-Even Point in Dollars
        ```
        BEP ($) = Fixed Costs / CM Ratio
        ```
        
        #### Target Profit Analysis
        ```
        Required Sales (units) = (Fixed Costs + Target Profit) / CM per Unit
        Required Sales ($) = (Fixed Costs + Target Profit) / CM Ratio
        ```
        
        #### Target Profit After Tax
        ```
        Required Pre-Tax Profit = Target After-Tax Profit / (1 - Tax Rate)
        ```
        """)
        
        st.subheader("5. Margin of Safety")
        
        st.markdown("""
        #### Margin of Safety
        ```
        MOS ($) = Actual Sales - Break-Even Sales
        MOS (%) = (Actual Sales - Break-Even Sales) / Actual Sales × 100
        ```
        
        **Interpretation**: How much sales can drop before reaching break-even
        """)
        
        st.subheader("6. Operating Leverage")
        
        st.markdown("""
        #### Degree of Operating Leverage (DOL)
        ```
        DOL = Contribution Margin / Net Operating Income
        ```
        
        #### % Change in Profit
        ```
        % Change in Profit = DOL × % Change in Sales
        ```
        
        **High Operating Leverage**: High fixed costs, high risk, high reward
        **Low Operating Leverage**: Low fixed costs, low risk, low reward
        """)
    
    with tab2:
        st.header("Practical Examples")
        
        st.subheader("Example 1: High-Low Method")
        
        st.markdown("""
        **Given**: Monthly production and utility costs:
        
        | Month | Units | Utility Cost |
        |-------|-------|-------------|
        | Jan   | 1,000 | $4,500      |
        | Feb   | 1,500 | $5,250      |
        | Mar   | 800   | $4,100      |
        | Apr   | 1,800 | $6,000      |
        """)
        
        st.markdown("""
        **Solution:**
        
        **Step 1**: Identify high and low activity
        - High: April (1,800 units, $6,000)
        - Low: March (800 units, $4,100)
        
        **Step 2**: Calculate variable cost per unit
        ```
        Variable Rate = ($6,000 - $4,100) / (1,800 - 800)
                     = $1,900 / 1,000
                     = $1.90 per unit
        ```
        
        **Step 3**: Calculate fixed cost
        ```
        Using high point:
        Fixed Cost = $6,000 - ($1.90 × 1,800)
                  = $6,000 - $3,420
                  = $2,580
        ```
        
        **Cost Formula**: Y = $2,580 + $1.90X
        """)
        
        st.subheader("Example 2: Break-Even Analysis")
        
        st.markdown("""
        **Given:**
        - Selling Price per Unit: $50
        - Variable Cost per Unit: $30
        - Fixed Costs: $100,000
        
        **Calculate:** Break-even point in units and dollars
        
        **Solution:**
        
        **Step 1**: Calculate CM per unit
        ```
        CM per Unit = $50 - $30 = $20
        ```
        
        **Step 2**: Calculate BEP in units
        ```
        BEP (units) = $100,000 / $20 = 5,000 units
        ```
        
        **Step 3**: Calculate BEP in dollars
        ```
        BEP ($) = 5,000 units × $50 = $250,000
        
        OR using CM Ratio:
        CM Ratio = $20 / $50 = 0.40 or 40%
        BEP ($) = $100,000 / 0.40 = $250,000
        ```
        """)
        
        st.subheader("Example 3: Target Profit Analysis")
        
        st.markdown("""
        **Given:** (using same data as Example 2)
        - Desired Profit: $60,000
        - Tax Rate: 30%
        
        **Calculate:** Required sales for target after-tax profit
        
        **Solution:**
        
        **Step 1**: Calculate required pre-tax profit
        ```
        Pre-Tax Profit = $60,000 / (1 - 0.30)
                      = $60,000 / 0.70
                      = $85,714
        ```
        
        **Step 2**: Calculate required sales in units
        ```
        Required Units = ($100,000 + $85,714) / $20
                      = $185,714 / $20
                      = 9,286 units
        ```
        
        **Step 3**: Calculate required sales in dollars
        ```
        Required Sales = 9,286 × $50 = $464,300
        ```
        """)
        
        st.subheader("Example 4: Operating Leverage")
        
        st.markdown("""
        **Given:**
        - Sales: $500,000
        - Variable Costs: $300,000
        - Fixed Costs: $150,000
        
        **Calculate:** DOL and predict profit change if sales increase 10%
        
        **Solution:**
        
        **Step 1**: Calculate contribution margin and profit
        ```
        CM = $500,000 - $300,000 = $200,000
        Profit = $200,000 - $150,000 = $50,000
        ```
        
        **Step 2**: Calculate DOL
        ```
        DOL = $200,000 / $50,000 = 4.0
        ```
        
        **Step 3**: Predict profit change
        ```
        % Change in Profit = 4.0 × 10% = 40%
        New Profit = $50,000 × 1.40 = $70,000
        ```
        
        **Interpretation**: A 10% increase in sales leads to a 40% increase in profit due to operating leverage of 4.0
        """)
    
    with tab3:
        st.header("Interactive Calculators")
        
        calc_option = st.selectbox(
            "Select Calculator:",
            ["High-Low Method", "Break-Even Analysis", "Target Profit", 
             "Margin of Safety", "Operating Leverage", "Multi-Product CVP"]
        )
        
        if calc_option == "High-Low Method":
            st.subheader("🧮 High-Low Method Calculator")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**High Activity Point:**")
                high_units = st.number_input("Units (High)", min_value=0.0, value=1800.0, step=100.0)
                high_cost = st.number_input("Total Cost (High) ($)", min_value=0.0, value=6000.0, step=100.0)
            
            with col2:
                st.markdown("**Low Activity Point:**")
                low_units = st.number_input("Units (Low)", min_value=0.0, value=800.0, step=100.0)
                low_cost = st.number_input("Total Cost (Low) ($)", min_value=0.0, value=4100.0, step=100.0)
            
            if high_units > low_units:
                variable_rate = (high_cost - low_cost) / (high_units - low_units)
                fixed_cost = high_cost - (variable_rate * high_units)
                
                st.markdown("---")
                st.markdown("### Results:")
                
                result_col1, result_col2 = st.columns(2)
                with result_col1:
                    st.metric("Variable Cost per Unit", f"${variable_rate:.2f}")
                with result_col2:
                    st.metric("Fixed Cost", f"${fixed_cost:.2f}")
                
                st.success(f"**Cost Formula:** Y = ${fixed_cost:.2f} + ${variable_rate:.2f}X")
                
                # Prediction
                st.markdown("**Predict Total Cost:**")
                predict_units = st.number_input("Units for Prediction", min_value=0.0, value=1500.0, step=100.0)
                predicted_cost = fixed_cost + (variable_rate * predict_units)
                st.info(f"Predicted Total Cost = ${predicted_cost:,.2f}")
            else:
                st.error("High activity units must be greater than low activity units")
        
        elif calc_option == "Break-Even Analysis":
            st.subheader("🧮 Break-Even Point Calculator")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                selling_price = st.number_input("Selling Price per Unit ($)", min_value=0.0, value=50.0, step=1.0)
            with col2:
                variable_cost = st.number_input("Variable Cost per Unit ($)", min_value=0.0, value=30.0, step=1.0)
            with col3:
                fixed_costs = st.number_input("Total Fixed Costs ($)", min_value=0.0, value=100000.0, step=1000.0)
            
            if selling_price > variable_cost:
                cm_per_unit = selling_price - variable_cost
                cm_ratio = cm_per_unit / selling_price
                
                bep_units = fixed_costs / cm_per_unit
                bep_dollars = bep_units * selling_price
                
                st.markdown("---")
                st.markdown("### Results:")
                
                metric_col1, metric_col2, metric_col3 = st.columns(3)
                with metric_col1:
                    st.metric("CM per Unit", f"${cm_per_unit:.2f}")
                with metric_col2:
                    st.metric("CM Ratio", f"{cm_ratio:.1%}")
                with metric_col3:
                    st.metric("BEP (Units)", f"{bep_units:,.0f}")
                
                st.success(f"**Break-Even Point:** {bep_units:,.0f} units or ${bep_dollars:,.2f}")
            else:
                st.error("Selling price must be greater than variable cost")
        
        elif calc_option == "Target Profit":
            st.subheader("🧮 Target Profit Calculator")
            
            col1, col2 = st.columns(2)
            
            with col1:
                tp_selling_price = st.number_input("Selling Price per Unit ($)", min_value=0.0, value=50.0, step=1.0, key="tp_sp")
                tp_variable_cost = st.number_input("Variable Cost per Unit ($)", min_value=0.0, value=30.0, step=1.0, key="tp_vc")
                tp_fixed_costs = st.number_input("Total Fixed Costs ($)", min_value=0.0, value=100000.0, step=1000.0, key="tp_fc")
            
            with col2:
                target_profit = st.number_input("Target After-Tax Profit ($)", min_value=0.0, value=60000.0, step=1000.0)
                tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, max_value=100.0, value=30.0, step=1.0) / 100
            
            if tp_selling_price > tp_variable_cost:
                tp_cm_per_unit = tp_selling_price - tp_variable_cost
                
                pre_tax_profit = target_profit / (1 - tax_rate) if tax_rate < 1 else target_profit
                required_units = (tp_fixed_costs + pre_tax_profit) / tp_cm_per_unit
                required_sales = required_units * tp_selling_price
                
                st.markdown("---")
                st.markdown("### Results:")
                
                result_col1, result_col2, result_col3 = st.columns(3)
                with result_col1:
                    st.metric("Pre-Tax Profit Needed", f"${pre_tax_profit:,.2f}")
                with result_col2:
                    st.metric("Required Units", f"{required_units:,.0f}")
                with result_col3:
                    st.metric("Required Sales ($)", f"${required_sales:,.2f}")
                
                # Income statement projection
                st.markdown("**Projected Income Statement:**")
                revenue = required_sales
                var_costs = required_units * tp_variable_cost
                contribution = revenue - var_costs
                operating_income = contribution - tp_fixed_costs
                tax_expense = operating_income * tax_rate
                net_income = operating_income - tax_expense
                
                income_data = {
                    'Item': ['Sales Revenue', 'Variable Costs', 'Contribution Margin', 
                            'Fixed Costs', 'Operating Income', 'Tax Expense', 'Net Income'],
                    'Amount': [revenue, -var_costs, contribution, -tp_fixed_costs, 
                              operating_income, -tax_expense, net_income]
                }
                df_income = pd.DataFrame(income_data)
                df_income['Amount'] = df_income['Amount'].apply(lambda x: f"${x:,.2f}")
                st.dataframe(df_income, use_container_width=True, hide_index=True)
            else:
                st.error("Selling price must be greater than variable cost")
        
        elif calc_option == "Margin of Safety":
            st.subheader("🧮 Margin of Safety Calculator")
            
            col1, col2 = st.columns(2)
            
            with col1:
                mos_actual_sales = st.number_input("Actual Sales ($)", min_value=0.0, value=500000.0, step=10000.0)
                mos_sp = st.number_input("Selling Price per Unit ($)", min_value=0.0, value=50.0, step=1.0, key="mos_sp")
            
            with col2:
                mos_vc = st.number_input("Variable Cost per Unit ($)", min_value=0.0, value=30.0, step=1.0, key="mos_vc")
                mos_fc = st.number_input("Fixed Costs ($)", min_value=0.0, value=100000.0, step=1000.0, key="mos_fc")
            
            if mos_sp > mos_vc:
                mos_cm_ratio = (mos_sp - mos_vc) / mos_sp
                bep_sales = mos_fc / mos_cm_ratio
                
                mos_dollars = mos_actual_sales - bep_sales
                mos_percentage = (mos_dollars / mos_actual_sales) * 100 if mos_actual_sales > 0 else 0
                
                st.markdown("---")
                st.markdown("### Results:")
                
                result_col1, result_col2, result_col3 = st.columns(3)
                with result_col1:
                    st.metric("Break-Even Sales", f"${bep_sales:,.2f}")
                with result_col2:
                    st.metric("Margin of Safety ($)", f"${mos_dollars:,.2f}")
                with result_col3:
                    st.metric("MOS Percentage", f"{mos_percentage:.2f}%")
                
                if mos_percentage > 30:
                    st.success(f"✅ Strong margin of safety: {mos_percentage:.1f}% - Sales can drop {mos_percentage:.1f}% before reaching break-even")
                elif mos_percentage > 15:
                    st.warning(f"⚠️ Moderate margin of safety: {mos_percentage:.1f}%")
                else:
                    st.error(f"❌ Weak margin of safety: {mos_percentage:.1f}% - Operating close to break-even")
            else:
                st.error("Selling price must be greater than variable cost")
        
        elif calc_option == "Operating Leverage":
            st.subheader("🧮 Operating Leverage Calculator")
            
            col1, col2 = st.columns(2)
            
            with col1:
                ol_sales = st.number_input("Current Sales ($)", min_value=0.0, value=500000.0, step=10000.0, key="ol_sales")
                ol_variable = st.number_input("Variable Costs ($)", min_value=0.0, value=300000.0, step=10000.0, key="ol_var")
            
            with col2:
                ol_fixed = st.number_input("Fixed Costs ($)", min_value=0.0, value=150000.0, step=10000.0, key="ol_fixed")
                sales_change = st.number_input("Expected % Change in Sales", min_value=-100.0, max_value=200.0, value=10.0, step=1.0)
            
            ol_cm = ol_sales - ol_variable
            ol_profit = ol_cm - ol_fixed
            
            if ol_profit > 0:
                dol = ol_cm / ol_profit
                profit_change = dol * sales_change
                new_profit = ol_profit * (1 + profit_change / 100)
                
                st.markdown("---")
                st.markdown("### Results:")
                
                result_col1, result_col2, result_col3 = st.columns(3)
                with result_col1:
                    st.metric("Current Profit", f"${ol_profit:,.2f}")
                with result_col2:
                    st.metric("DOL", f"{dol:.2f}")
                with result_col3:
                    st.metric("% Change in Profit", f"{profit_change:.2f}%")
                
                st.info(f"**Prediction:** If sales change by {sales_change}%, profit will change by {profit_change:.2f}%")
                st.success(f"**New Profit:** ${new_profit:,.2f}")
                
                # Interpretation
                if dol > 5:
                    st.warning("⚠️ High operating leverage - High risk, high reward. Small sales changes cause large profit swings.")
                elif dol > 2:
                    st.info("📊 Moderate operating leverage - Balanced risk/reward profile.")
                else:
                    st.success("✅ Low operating leverage - More stable profits, less sensitive to sales changes.")
            else:
                st.error("Company is currently unprofitable. Operating leverage calculation requires positive profit.")
        
        else:  # Multi-Product CVP
            st.subheader("🧮 Multi-Product CVP Calculator")
            
            st.markdown("**Product A:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                a_price = st.number_input("Price ($)", min_value=0.0, value=50.0, step=1.0, key="a_price")
            with col2:
                a_vc = st.number_input("Variable Cost ($)", min_value=0.0, value=30.0, step=1.0, key="a_vc")
            with col3:
                a_mix = st.number_input("Sales Mix %", min_value=0.0, max_value=100.0, value=60.0, step=1.0, key="a_mix")
            
            st.markdown("**Product B:**")
            col4, col5, col6 = st.columns(3)
            with col4:
                b_price = st.number_input("Price ($)", min_value=0.0, value=80.0, step=1.0, key="b_price")
            with col5:
                b_vc = st.number_input("Variable Cost ($)", min_value=0.0, value=50.0, step=1.0, key="b_vc")
            with col6:
                b_mix = st.number_input("Sales Mix %", min_value=0.0, max_value=100.0, value=40.0, step=1.0, key="b_mix")
            
            total_fixed = st.number_input("Total Fixed Costs ($)", min_value=0.0, value=150000.0, step=1000.0, key="mp_fixed")
            
            if abs((a_mix + b_mix) - 100) < 0.01:  # Account for floating point
                a_cm = a_price - a_vc
                b_cm = b_price - b_vc
                
                weighted_cm = (a_cm * a_mix / 100) + (b_cm * b_mix / 100)
                total_bep_units = total_fixed / weighted_cm if weighted_cm > 0 else 0
                
                a_bep_units = total_bep_units * (a_mix / 100)
                b_bep_units = total_bep_units * (b_mix / 100)
                
                a_bep_sales = a_bep_units * a_price
                b_bep_sales = b_bep_units * b_price
                total_bep_sales = a_bep_sales + b_bep_sales
                
                st.markdown("---")
                st.markdown("### Results:")
                
                result_col1, result_col2 = st.columns(2)
                with result_col1:
                    st.metric("Weighted Avg CM", f"${weighted_cm:.2f}")
                with result_col2:
                    st.metric("Total BEP (Units)", f"{total_bep_units:,.0f}")
                
                st.markdown("**Break-Even by Product:**")
                bep_data = {
                    'Product': ['Product A', 'Product B', 'Total'],
                    'Units': [f"{a_bep_units:,.0f}", f"{b_bep_units:,.0f}", f"{total_bep_units:,.0f}"],
                    'Sales ($)': [f"${a_bep_sales:,.2f}", f"${b_bep_sales:,.2f}", f"${total_bep_sales:,.2f}"]
                }
                df_bep = pd.DataFrame(bep_data)
                st.dataframe(df_bep, use_container_width=True, hide_index=True)
            else:
                st.error("Sales mix percentages must total 100%")
    
    with tab4:
        st.header("Visual Analytics")
        
        # Cost behavior visualization
        st.subheader("Cost Behavior Patterns")
        
        units = np.linspace(0, 10000, 100)
        
        variable_costs = units * 5  # $5 per unit
        fixed_costs_line = np.full_like(units, 30000)  # $30,000 fixed
        mixed_costs = 30000 + (units * 5)  # $30,000 + $5 per unit
        
        fig_behavior = go.Figure()
        
        fig_behavior.add_trace(go.Scatter(
            x=units, y=variable_costs, mode='lines',
            name='Variable Cost', line=dict(color='blue', width=2)
        ))
        
        fig_behavior.add_trace(go.Scatter(
            x=units, y=fixed_costs_line, mode='lines',
            name='Fixed Cost', line=dict(color='red', width=2, dash='dash')
        ))
        
        fig_behavior.add_trace(go.Scatter(
            x=units, y=mixed_costs, mode='lines',
            name='Mixed Cost', line=dict(color='green', width=2, dash='dot')
        ))
        
        fig_behavior.update_layout(
            title='Cost Behavior Patterns',
            xaxis_title='Units of Activity',
            yaxis_title='Total Cost ($)',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_behavior, use_container_width=True)
        
        # CVP Chart
        st.subheader("Cost-Volume-Profit Chart")
        
        cvp_units = np.linspace(0, 10000, 100)
        price_per_unit = 50
        vc_per_unit = 30
        fixed = 100000
        
        total_revenue = cvp_units * price_per_unit
        total_cost = fixed + (cvp_units * vc_per_unit)
        profit = total_revenue - total_cost
        
        # Break-even point
        bep_units_calc = fixed / (price_per_unit - vc_per_unit)
        bep_revenue = bep_units_calc * price_per_unit
        
        fig_cvp = go.Figure()
        
        fig_cvp.add_trace(go.Scatter(
            x=cvp_units, y=total_revenue, mode='lines',
            name='Total Revenue', line=dict(color='green', width=3)
        ))
        
        fig_cvp.add_trace(go.Scatter(
            x=cvp_units, y=total_cost, mode='lines',
            name='Total Cost', line=dict(color='red', width=3)
        ))
        
        # Add break-even point
        fig_cvp.add_trace(go.Scatter(
            x=[bep_units_calc], y=[bep_revenue],
            mode='markers+text',
            name='Break-Even Point',
            marker=dict(size=15, color='orange'),
            text=[f'BEP: {bep_units_calc:.0f} units'],
            textposition='top center'
        ))
        
        # Shade profit and loss areas
        fig_cvp.add_vrect(
            x0=0, x1=bep_units_calc,
            fillcolor="red", opacity=0.1,
            layer="below", line_width=0,
            annotation_text="Loss Area", annotation_position="top left"
        )
        
        fig_cvp.add_vrect(
            x0=bep_units_calc, x1=10000,
            fillcolor="green", opacity=0.1,
            layer="below", line_width=0,
            annotation_text="Profit Area", annotation_position="top right"
        )
        
        fig_cvp.update_layout(
            title='CVP Chart - Break-Even Analysis',
            xaxis_title='Units Sold',
            yaxis_title='Dollars ($)',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_cvp, use_container_width=True)
        
        # Profit-Volume Chart
        st.subheader("Profit-Volume (P-V) Chart")
        
        fig_pv = go.Figure()
        
        fig_pv.add_trace(go.Scatter(
            x=cvp_units, y=profit, mode='lines',
            name='Profit/Loss', line=dict(color='purple', width=3),
            fill='tozeroy'
        ))
        
        fig_pv.add_hline(y=0, line_dash="dash", line_color="black", annotation_text="Break-Even")
        
        fig_pv.add_trace(go.Scatter(
            x=[bep_units_calc], y=[0],
            mode='markers+text',
            name='Break-Even Point',
            marker=dict(size=15, color='orange'),
            text=[f'{bep_units_calc:.0f} units'],
            textposition='top center'
        ))
        
        fig_pv.update_layout(
            title='Profit-Volume Chart',
            xaxis_title='Units Sold',
            yaxis_title='Profit/Loss ($)',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_pv, use_container_width=True)
    
    with tab5:
        st.header("Knowledge Check Quiz")
        
        st.subheader("Test Your Understanding")
        
        # Question 1
        st.markdown("**1. Which cost behavior pattern has a constant per-unit cost?**")
        q1 = st.radio(
            "Select your answer:",
            ["Fixed costs", "Variable costs", "Mixed costs", "Step costs"],
            key="q1"
        )
        
        if st.button("Check Answer", key="check1"):
            if q1 == "Variable costs":
                st.success("✅ Correct! Variable costs have a constant per-unit cost but total varies with activity.")
            else:
                st.error("❌ Incorrect. Variable costs have constant per-unit costs.")
        
        st.markdown("---")
        
        # Question 2
        st.markdown("**2. The contribution margin ratio is calculated as:**")
        q2 = st.radio(
            "Select your answer:",
            [
                "Sales / Variable Costs",
                "Contribution Margin / Sales",
                "Fixed Costs / Sales",
                "Profit / Sales"
            ],
            key="q2"
        )
        
        if st.button("Check Answer", key="check2"):
            if q2 == "Contribution Margin / Sales":
                st.success("✅ Correct! CM Ratio = Contribution Margin / Sales Revenue")
            else:
                st.error("❌ Incorrect. CM Ratio = Contribution Margin / Sales")
        
        st.markdown("---")
        
        # Question 3
        st.markdown("""
        **3. Given: Selling Price = $100, Variable Cost = $60, Fixed Costs = $80,000**
        
        **What is the break-even point in units?**
        """)
        q3 = st.radio(
            "Select your answer:",
            ["800 units", "1,333 units", "2,000 units", "4,000 units"],
            key="q3"
        )
        
        if st.button("Check Answer", key="check3"):
            if q3 == "2,000 units":
                st.success("✅ Correct! BEP = $80,000 / ($100 - $60) = $80,000 / $40 = 2,000 units")
            else:
                st.error("❌ Incorrect. BEP = Fixed Costs / CM per unit = $80,000 / $40 = 2,000 units")
        
        st.markdown("---")
        
        # Question 4
        st.markdown("**4. A high degree of operating leverage means:**")
        q4 = st.radio(
            "Select your answer:",
            [
                "Low fixed costs relative to variable costs",
                "High fixed costs relative to variable costs",
                "Profit is not sensitive to sales changes",
                "The company is highly profitable"
            ],
            key="q4"
        )
        
        if st.button("Check Answer", key="check4"):
            if q4 == "High fixed costs relative to variable costs":
                st.success("✅ Correct! High operating leverage means high fixed costs, making profit very sensitive to sales changes.")
            else:
                st.error("❌ Incorrect. High DOL indicates high fixed costs relative to variable costs.")
        
        st.markdown("---")
        
        # Question 5
        st.markdown("""
        **5. Using the High-Low method:**
        - High: 5,000 units, $45,000 cost
        - Low: 3,000 units, $35,000 cost
        
        **What is the variable cost per unit?**
        """)
        q5 = st.radio(
            "Select your answer:",
            ["$3", "$5", "$7", "$10"],
            key="q5"
        )
        
        if st.button("Check Answer", key="check5"):
            if q5 == "$5":
                st.success("✅ Correct! Variable rate = ($45,000 - $35,000) / (5,000 - 3,000) = $10,000 / 2,000 = $5 per unit")
            else:
                st.error("❌ Incorrect. Variable rate = Change in cost / Change in activity = $10,000 / 2,000 = $5")
        
        st.markdown("---")
        
        # Question 6
        st.markdown("""
        **6. If actual sales are $500,000 and break-even sales are $350,000, what is the margin of safety percentage?**
        """)
        q6 = st.radio(
            "Select your answer:",
            ["20%", "30%", "40%", "50%"],
            key="q6"
        )
        
        if st.button("Check Answer", key="check6"):
            if q6 == "30%":
                st.success("✅ Correct! MOS% = ($500,000 - $350,000) / $500,000 = $150,000 / $500,000 = 30%")
            else:
                st.error("❌ Incorrect. MOS% = (Actual - BEP) / Actual = $150,000 / $500,000 = 30%")
    
    with tab6:
        st.header("Module Summary")
        
        st.subheader("🎯 Key Takeaways")
        
        st.markdown("""
        ### 1. Cost Behavior Patterns
        
        | Cost Type | Total Cost | Per Unit Cost | Example |
        |-----------|------------|---------------|---------|
        | Variable | Changes with activity | Constant | Direct materials |
        | Fixed | Constant (in relevant range) | Decreases as activity increases | Rent |
        | Mixed | Changes but not proportionally | Changes | Utilities |
        | Step | Constant over ranges | Changes at steps | Supervision |
        
        ### 2. Key Formulas
        
        #### Mixed Cost Analysis (High-Low Method)
        ```
        Variable Rate = (High Cost - Low Cost) / (High Activity - Low Activity)
        Fixed Cost = Total Cost - (Variable Rate × Activity)
        Cost Formula: Y = a + bX
        ```
        
        #### Contribution Margin
        ```
        CM per Unit = Selling Price - Variable Cost per Unit
        CM Ratio = CM / Sales Revenue
        Total CM = Sales Revenue - Total Variable Costs
        ```
        
        #### Break-Even Analysis
        ```
        BEP (units) = Fixed Costs / CM per Unit
        BEP ($) = Fixed Costs / CM Ratio
        ```
        
        #### Target Profit
        ```
        Required Units = (Fixed Costs + Target Profit) / CM per Unit
        Pre-Tax Profit = After-Tax Profit / (1 - Tax Rate)
        ```
        
        #### Margin of Safety
        ```
        MOS ($) = Actual Sales - Break-Even Sales
        MOS (%) = MOS ($) / Actual Sales × 100
        ```
        
        #### Operating Leverage
        ```
        DOL = Contribution Margin / Net Operating Income
        % Change in Profit = DOL × % Change in Sales
        ```
        
        ### 3. CVP Analysis Applications
        
        **Break-Even Analysis:**
        - Determine minimum sales to avoid losses
        - Essential for new product launches
        - Helps in pricing decisions
        
        **Target Profit Analysis:**
        - Plan sales volume for desired profit
        - Consider tax implications
        - Set realistic sales targets
        
        **What-If Analysis:**
        - Evaluate impact of price changes
        - Assess cost structure changes
        - Analyze sales volume scenarios
        
        **Multi-Product CVP:**
        - Use weighted average CM
        - Maintain constant sales mix
        - Analyze product line profitability
        
        ### 4. Operating Leverage Insights
        
        **High Operating Leverage (High Fixed Costs):**
        - ✅ High profit potential with sales growth
        - ❌ High risk if sales decline
        - Examples: Airlines, manufacturing
        
        **Low Operating Leverage (Low Fixed Costs):**
        - ✅ More stable profits
        - ❌ Lower profit growth potential
        - Examples: Consulting, services
        
        ### 5. Important Assumptions
        
        CVP analysis assumes:
        - Costs can be classified as variable or fixed
        - Cost behavior is linear within relevant range
        - Selling price is constant
        - Production = Sales (no inventory changes)
        - Sales mix is constant (multi-product)
        - Technology and efficiency remain constant
        
        ### 6. Decision-Making Framework
        
        **Step 1:** Identify relevant costs (variable vs. fixed)
        **Step 2:** Calculate contribution margin
        **Step 3:** Determine break-even point
        **Step 4:** Analyze margin of safety
        **Step 5:** Assess operating leverage
        **Step 6:** Perform sensitivity analysis
        
        ### 7. Practical Tips
        
        - Always work within the relevant range
        - Update cost behavior assumptions regularly
        - Consider both financial and non-financial factors
        - Use CVP for short-term tactical decisions
        - Combine with other tools for strategic planning
        - Remember: High CM ratio = more profitable sales
        """)
        
        st.subheader("📊 Quick Reference Card")
        
        quick_ref = {
            'Concept': ['Variable Cost per Unit', 'Fixed Cost Total', 'CM per Unit', 
                       'CM Ratio', 'BEP Units', 'BEP Dollars', 'Target Profit Units', 'MOS %', 'DOL'],
            'Formula': [
                'ΔCost / ΔActivity',
                'Total Cost - (Var Rate × Activity)',
                'Price - Variable Cost',
                'CM / Sales',
                'Fixed Costs / CM per Unit',
                'Fixed Costs / CM Ratio',
                '(Fixed + Profit) / CM per Unit',
                '(Actual - BEP) / Actual × 100',
                'CM / Profit'
            ]
        }
        
        df_quick = pd.DataFrame(quick_ref)
        st.dataframe(df_quick, use_container_width=True, hide_index=True)
        
        st.success("🎓 **You've completed Module 2!** You can now analyze cost behavior and perform comprehensive CVP analysis.")
        
        st.info("💡 **Next Steps**: Proceed to Module 3 to learn about Job Order Costing Systems.")

if __name__ == "__main__":
    show()