import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def show():
    st.title("📊 Module 1: Foundations of Managerial Accounting")
    
    # Create tabs for better organization
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools", 
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])
    
    with tab1:
        st.header("Core Concepts")
        
        st.subheader("1. Managerial vs. Financial Accounting")
        
        comparison_data = {
            'Aspect': ['Primary Users', 'Time Focus', 'Regulation', 'Frequency', 
                      'Scope', 'Type', 'Precision'],
            'Managerial Accounting': [
                'Internal managers',
                'Future-oriented',
                'No external rules',
                'As needed (daily/weekly)',
                'Segments/divisions',
                'Detailed, flexible',
                'Estimates acceptable'
            ],
            'Financial Accounting': [
                'External stakeholders',
                'Historical data',
                'GAAP/IFRS required',
                'Quarterly/Annual',
                'Entire organization',
                'Standardized format',
                'Precision required'
            ]
        }
        
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True, hide_index=True)
        
        st.subheader("2. Role of Management Accountant")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Key Responsibilities:**
            - Planning and budgeting
            - Performance evaluation
            - Cost management
            - Decision support
            - Risk management
            - Strategic analysis
            """)
        
        with col2:
            st.markdown("""
            **Skills Required:**
            - Analytical thinking
            - Business acumen
            - Communication skills
            - Technology proficiency
            - Ethical judgment
            - Strategic mindset
            """)
        
        st.subheader("3. Cost Classifications")
        
        st.markdown("""
        #### By Function:
        - **Manufacturing Costs**: Direct Materials, Direct Labor, Manufacturing Overhead
        - **Non-Manufacturing Costs**: Selling Expenses, Administrative Expenses
        
        #### By Behavior:
        - **Variable Costs**: Change with activity level (e.g., direct materials)
        - **Fixed Costs**: Remain constant within relevant range (e.g., rent)
        - **Mixed Costs**: Contain both variable and fixed components (e.g., utilities)
        
        #### By Traceability:
        - **Direct Costs**: Can be traced to cost object (e.g., direct materials)
        - **Indirect Costs**: Cannot be easily traced (e.g., factory supervision)
        
        #### By Relevance:
        - **Differential Costs**: Differ between alternatives
        - **Opportunity Costs**: Benefit forgone from next best alternative
        - **Sunk Costs**: Already incurred, cannot be changed
        """)
        
        st.subheader("4. Product vs. Period Costs")
        
        st.markdown("""
        **Product Costs (Inventoriable):**
        - Direct Materials
        - Direct Labor  
        - Manufacturing Overhead
        - Become COGS when sold
        
        **Period Costs (Expensed Immediately):**
        - Selling Expenses
        - Administrative Expenses
        - Not included in inventory value
        """)
        
        st.subheader("5. IMA Statement of Ethical Professional Practice")
        
        ethics_cols = st.columns(4)
        
        with ethics_cols[0]:
            st.markdown("""
            **Competence**
            - Maintain skills
            - Perform duties
            - Provide accurate info
            - Recognize limitations
            """)
        
        with ethics_cols[1]:
            st.markdown("""
            **Confidentiality**
            - Keep information confidential
            - Inform subordinates
            - Refrain from disclosure
            - Monitor activities
            """)
        
        with ethics_cols[2]:
            st.markdown("""
            **Integrity**
            - Mitigate conflicts
            - Refuse gifts
            - Refrain from activities
            - Recognize limits
            """)
        
        with ethics_cols[3]:
            st.markdown("""
            **Credibility**
            - Communicate fairly
            - Disclose information
            - Disclose delays
            - Report information
            """)
    
    with tab2:
        st.header("Practical Examples")
        
        st.subheader("Example 1: Cost Classification")
        
        st.markdown("""
        **Scenario**: ABC Manufacturing Company produces furniture.
        Classify the following costs:
        """)
        
        example_costs = {
            'Cost Item': [
                'Wood used in tables',
                'Factory supervisor salary',
                'Sales commissions',
                'Depreciation on factory equipment',
                'CEO salary',
                'Carpenter wages',
                'Factory utilities',
                'Advertising expenses'
            ],
            'Direct/Indirect': [
                'Direct Material',
                'Indirect (Overhead)',
                'Period Cost',
                'Indirect (Overhead)',
                'Period Cost',
                'Direct Labor',
                'Indirect (Overhead)',
                'Period Cost'
            ],
            'Product/Period': [
                'Product',
                'Product',
                'Period',
                'Product',
                'Period',
                'Product',
                'Product',
                'Period'
            ],
            'Variable/Fixed': [
                'Variable',
                'Fixed',
                'Variable',
                'Fixed',
                'Fixed',
                'Variable',
                'Mixed',
                'Mixed'
            ]
        }
        
        df_example = pd.DataFrame(example_costs)
        st.dataframe(df_example, use_container_width=True, hide_index=True)
        
        st.subheader("Example 2: Product Cost Calculation")
        
        st.markdown("""
        **Given Information:**
        - Direct Materials: $50,000
        - Direct Labor: $30,000
        - Manufacturing Overhead: $25,000
        - Selling Expenses: $15,000
        - Administrative Expenses: $10,000
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Total Product Cost:**
            ```
            Direct Materials        $50,000
            Direct Labor            $30,000
            Manufacturing Overhead  $25,000
            ─────────────────────────────
            Total Product Cost     $105,000
            ```
            """)
        
        with col2:
            st.markdown("""
            **Total Period Cost:**
            ```
            Selling Expenses        $15,000
            Administrative Exp.     $10,000
            ─────────────────────────────
            Total Period Cost       $25,000
            ```
            """)
        
        st.info("💡 **Key Insight**: Product costs of $105,000 go to inventory and become COGS when sold. Period costs of $25,000 are expensed immediately on the income statement.")
    
    with tab3:
        st.header("Interactive Calculators")
        
        st.subheader("🧮 Product vs. Period Cost Calculator")
        
        st.markdown("Enter the costs to calculate total product and period costs:")
        
        calc_col1, calc_col2 = st.columns(2)
        
        with calc_col1:
            st.markdown("**Product Costs:**")
            direct_materials = st.number_input("Direct Materials ($)", min_value=0.0, value=50000.0, step=1000.0)
            direct_labor = st.number_input("Direct Labor ($)", min_value=0.0, value=30000.0, step=1000.0)
            mfg_overhead = st.number_input("Manufacturing Overhead ($)", min_value=0.0, value=25000.0, step=1000.0)
        
        with calc_col2:
            st.markdown("**Period Costs:**")
            selling_exp = st.number_input("Selling Expenses ($)", min_value=0.0, value=15000.0, step=1000.0)
            admin_exp = st.number_input("Administrative Expenses ($)", min_value=0.0, value=10000.0, step=1000.0)
        
        # Calculations
        total_product_cost = direct_materials + direct_labor + mfg_overhead
        total_period_cost = selling_exp + admin_exp
        total_costs = total_product_cost + total_period_cost
        
        st.markdown("---")
        
        result_col1, result_col2, result_col3 = st.columns(3)
        
        with result_col1:
            st.metric("Total Product Cost", f"${total_product_cost:,.2f}")
        
        with result_col2:
            st.metric("Total Period Cost", f"${total_period_cost:,.2f}")
        
        with result_col3:
            st.metric("Total Costs", f"${total_costs:,.2f}")
        
        # Show breakdown
        if st.checkbox("Show Detailed Breakdown"):
            breakdown_data = {
                'Category': ['Direct Materials', 'Direct Labor', 'Manufacturing Overhead', 
                           'Selling Expenses', 'Administrative Expenses'],
                'Amount': [direct_materials, direct_labor, mfg_overhead, selling_exp, admin_exp],
                'Type': ['Product', 'Product', 'Product', 'Period', 'Period'],
                'Percentage': [
                    (direct_materials/total_costs*100),
                    (direct_labor/total_costs*100),
                    (mfg_overhead/total_costs*100),
                    (selling_exp/total_costs*100),
                    (admin_exp/total_costs*100)
                ]
            }
            
            df_breakdown = pd.DataFrame(breakdown_data)
            df_breakdown['Percentage'] = df_breakdown['Percentage'].apply(lambda x: f"{x:.2f}%")
            df_breakdown['Amount'] = df_breakdown['Amount'].apply(lambda x: f"${x:,.2f}")
            
            st.dataframe(df_breakdown, use_container_width=True, hide_index=True)
    
    with tab4:
        st.header("Visual Analytics")
        
        st.subheader("Cost Structure Visualization")
        
        # Pie chart for cost breakdown
        cost_data = pd.DataFrame({
            'Category': ['Direct Materials', 'Direct Labor', 'Manufacturing Overhead', 
                        'Selling Expenses', 'Administrative Expenses'],
            'Amount': [direct_materials, direct_labor, mfg_overhead, selling_exp, admin_exp],
            'Type': ['Product Cost', 'Product Cost', 'Product Cost', 
                    'Period Cost', 'Period Cost']
        })
        
        fig_pie = px.pie(cost_data, values='Amount', names='Category', 
                        title='Cost Distribution',
                        color='Type',
                        color_discrete_map={'Product Cost': '#1f77b4', 'Period Cost': '#ff7f0e'})
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # Bar chart comparison
        fig_bar = go.Figure(data=[
            go.Bar(name='Product Costs', x=['Direct Materials', 'Direct Labor', 'Mfg Overhead'],
                  y=[direct_materials, direct_labor, mfg_overhead],
                  marker_color='#1f77b4'),
            go.Bar(name='Period Costs', x=['Selling Expenses', 'Admin Expenses'],
                  y=[selling_exp, admin_exp],
                  marker_color='#ff7f0e')
        ])
        
        fig_bar.update_layout(
            title='Product vs. Period Costs Comparison',
            xaxis_title='Cost Category',
            yaxis_title='Amount ($)',
            barmode='group'
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Value chain visualization
        st.subheader("Value Chain Activities")
        
        value_chain_data = pd.DataFrame({
            'Activity': ['R&D', 'Design', 'Production', 'Marketing', 'Distribution', 'Customer Service'],
            'Cost': [15000, 12000, 105000, 10000, 8000, 5000],
            'Type': ['Primary', 'Primary', 'Primary', 'Primary', 'Primary', 'Primary']
        })
        
        fig_chain = px.bar(value_chain_data, x='Activity', y='Cost',
                          title='Value Chain Cost Analysis',
                          color='Cost',
                          color_continuous_scale='Blues')
        
        st.plotly_chart(fig_chain, use_container_width=True)
    
    with tab5:
        st.header("Knowledge Check Quiz")
        
        st.subheader("Test Your Understanding")
        
        # Question 1
        st.markdown("**1. Which of the following is NOT a product cost?**")
        q1 = st.radio(
            "Select your answer:",
            ["Direct materials", "Factory supervisor salary", "Sales commission", "Factory depreciation"],
            key="q1"
        )
        
        if st.button("Check Answer", key="check1"):
            if q1 == "Sales commission":
                st.success("✅ Correct! Sales commission is a period cost (selling expense), not a product cost.")
            else:
                st.error("❌ Incorrect. Sales commission is a period cost, not a product cost.")
        
        st.markdown("---")
        
        # Question 2
        st.markdown("**2. What is the primary purpose of managerial accounting?**")
        q2 = st.radio(
            "Select your answer:",
            [
                "To prepare financial statements for external users",
                "To provide information for internal decision-making",
                "To comply with GAAP requirements",
                "To calculate tax obligations"
            ],
            key="q2"
        )
        
        if st.button("Check Answer", key="check2"):
            if q2 == "To provide information for internal decision-making":
                st.success("✅ Correct! Managerial accounting focuses on providing information to internal managers for decision-making.")
            else:
                st.error("❌ Incorrect. The primary purpose is to provide information for internal decision-making.")
        
        st.markdown("---")
        
        # Question 3
        st.markdown("**3. A cost that has already been incurred and cannot be changed is called:**")
        q3 = st.radio(
            "Select your answer:",
            ["Opportunity cost", "Differential cost", "Sunk cost", "Variable cost"],
            key="q3"
        )
        
        if st.button("Check Answer", key="check3"):
            if q3 == "Sunk cost":
                st.success("✅ Correct! Sunk costs are past costs that cannot be changed by any future decision.")
            else:
                st.error("❌ Incorrect. This describes a sunk cost.")
        
        st.markdown("---")
        
        # Question 4
        st.markdown("**4. Which ethical principle requires management accountants to maintain professional knowledge and skills?**")
        q4 = st.radio(
            "Select your answer:",
            ["Integrity", "Competence", "Confidentiality", "Credibility"],
            key="q4"
        )
        
        if st.button("Check Answer", key="check4"):
            if q4 == "Competence":
                st.success("✅ Correct! Competence requires maintaining appropriate levels of professional knowledge and skill.")
            else:
                st.error("❌ Incorrect. Competence is the principle that requires maintaining professional knowledge and skills.")
        
        st.markdown("---")
        
        # Question 5
        st.markdown("**5. Calculate: If Direct Materials = $40,000, Direct Labor = $25,000, Manufacturing Overhead = $20,000, and Selling Expenses = $10,000, what is the total product cost?**")
        q5 = st.radio(
            "Select your answer:",
            ["$75,000", "$85,000", "$95,000", "$105,000"],
            key="q5"
        )
        
        if st.button("Check Answer", key="check5"):
            if q5 == "$85,000":
                st.success("✅ Correct! Product Cost = DM + DL + MOH = $40,000 + $25,000 + $20,000 = $85,000")
            else:
                st.error("❌ Incorrect. Product Cost = $40,000 + $25,000 + $20,000 = $85,000 (Selling expenses are period costs)")
    
    with tab6:
        st.header("Module Summary")
        
        st.subheader("🎯 Key Takeaways")
        
        st.markdown("""
        ### 1. Managerial vs. Financial Accounting
        - **Managerial accounting** serves internal users and focuses on future decisions
        - **Financial accounting** serves external stakeholders and reports historical data
        - Managerial accounting has no external regulatory requirements
        
        ### 2. Cost Classifications
        
        #### By Function:
        - **Product Costs**: Direct Materials + Direct Labor + Manufacturing Overhead
        - **Period Costs**: Selling + Administrative Expenses
        
        #### By Behavior:
        - **Variable Costs**: Change proportionally with activity
        - **Fixed Costs**: Remain constant within relevant range
        - **Mixed Costs**: Contain both variable and fixed components
        
        #### By Traceability:
        - **Direct Costs**: Easily traced to cost object
        - **Indirect Costs**: Cannot be easily traced
        
        #### For Decision-Making:
        - **Differential Costs**: Differ between alternatives (relevant)
        - **Opportunity Costs**: Benefits forgone (relevant)
        - **Sunk Costs**: Already incurred (irrelevant)
        
        ### 3. Role of Management Accountant
        - Planning and budgeting
        - Performance measurement and evaluation
        - Cost management and control
        - Strategic decision support
        - Risk assessment and management
        
        ### 4. IMA Ethical Standards
        - **Competence**: Maintain professional skills
        - **Confidentiality**: Protect sensitive information
        - **Integrity**: Avoid conflicts of interest
        - **Credibility**: Communicate information fairly
        
        ### 5. Product Cost Flow
        ```
        Product Costs → Inventory → Cost of Goods Sold (when sold)
        Period Costs → Income Statement (immediately expensed)
        ```
        
        ### 6. Important Formulas
        
        **Total Product Cost:**
        ```
        Product Cost = Direct Materials + Direct Labor + Manufacturing Overhead
        ```
        
        **Total Manufacturing Cost:**
        ```
        Total Mfg Cost = Product Cost + Beginning WIP - Ending WIP
        ```
        
        **Cost of Goods Sold:**
        ```
        COGS = Beginning Inventory + Product Cost - Ending Inventory
        ```
        """)
        
        st.subheader("📌 Quick Reference Table")
        
        quick_ref = {
            'Cost Type': ['Direct Materials', 'Direct Labor', 'Manufacturing Overhead', 
                         'Selling Expenses', 'Administrative Expenses'],
            'Classification': ['Product/Direct/Variable', 'Product/Direct/Variable', 
                             'Product/Indirect/Mixed', 'Period/Indirect/Mixed', 'Period/Indirect/Fixed'],
            'Example': ['Wood, steel, fabric', 'Assembly workers wages', 
                       'Factory rent, utilities', 'Advertising, commissions', 'Office salaries, supplies'],
            'Financial Treatment': ['Inventory → COGS', 'Inventory → COGS', 
                                   'Inventory → COGS', 'Expense immediately', 'Expense immediately']
        }
        
        df_ref = pd.DataFrame(quick_ref)
        st.dataframe(df_ref, use_container_width=True, hide_index=True)
        
        st.success("🎓 **You've completed Module 1!** You now understand the foundations of managerial accounting and can classify costs appropriately.")
        
        st.info("💡 **Next Steps**: Proceed to Module 2 to learn about Cost Behavior and Cost-Volume-Profit Analysis.")

if __name__ == "__main__":
    show()