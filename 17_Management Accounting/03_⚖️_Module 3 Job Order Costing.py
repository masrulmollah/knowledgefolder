import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏭 Module 3: Job Order Costing Systems")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators", 
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])
    
    with tab1:
        st.header("Core Concepts")
        
        st.subheader("1. Job Order Costing Overview")
        
        st.markdown("""
        #### What is Job Order Costing?
        A costing system used when products are manufactured based on specific customer orders or jobs.
        
        #### When to Use:
        - Custom products (furniture, construction, printing)
        - Each job is unique
        - Costs tracked by individual job
        - Service industries (law firms, consulting, repair shops)
        
        #### Key Features:
        - Each job has a unique job number
        - Costs accumulated on job cost sheet
        - Direct materials and labor traced to specific jobs
        - Overhead allocated using predetermined rate
        """)
        
        st.subheader("2. Document Flow")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Materials Requisition Form:**
            - Authorizes withdrawal of materials
            - Records direct/indirect materials
            - Posted to job cost sheet
            
            **Time Ticket:**
            - Records labor hours per job
            - Shows direct/indirect labor
            - Basis for labor cost assignment
            """)
        
        with col2:
            st.markdown("""
            **Job Cost Sheet:**
            - Master document for each job
            - Accumulates all costs
            - Contains:
              - Direct materials
              - Direct labor
              - Applied overhead
            
            **Predetermined Overhead Rate:**
            - Calculated before period begins
            - Used to apply overhead to jobs
            """)
        
        st.subheader("3. Predetermined Overhead Rate")
        
        st.markdown("""
        #### Formula:
        ```
        Predetermined OH Rate = Estimated Total Manufacturing Overhead / Estimated Allocation Base
        ```
        
        #### Common Allocation Bases:
        - Direct labor hours (most common)
        - Direct labor cost
        - Machine hours
        - Units produced
        
        #### Applied Overhead:
        ```
        Applied Overhead = Predetermined OH Rate × Actual Allocation Base
        ```
        """)
        
        st.subheader("4. Job Cost Sheet Components")
        
        st.markdown("""
        ```
        JOB COST SHEET
        Job Number: _______
        Customer: _______
        Date Started: _______
        Date Completed: _______
        
        DIRECT MATERIALS
        Date | Requisition # | Amount
        
        DIRECT LABOR
        Date | Time Ticket # | Hours | Rate | Amount
        
        MANUFACTURING OVERHEAD APPLIED
        Date | Hours/Base | Rate | Amount
        
        COST SUMMARY
        Direct Materials      $______
        Direct Labor          $______
        Overhead Applied      $______
        Total Job Cost        $______
        Units Produced        ______
        Cost per Unit         $______
        ```
        """)
        
        st.subheader("5. Under/Overapplied Overhead")
        
        st.markdown("""
        #### Actual vs. Applied Overhead:
        - **Underapplied**: Actual OH > Applied OH (debit balance)
        - **Overapplied**: Applied OH > Actual OH (credit balance)
        
        #### Calculation:
        ```
        Under/Overapplied OH = Actual OH - Applied OH
        ```
        
        #### Disposition Methods:
        
        **1. Close to Cost of Goods Sold (if immaterial):**
        - Underapplied: Increase COGS
        - Overapplied: Decrease COGS
        
        **2. Prorate (if material):**
        - Allocate to WIP, Finished Goods, and COGS
        - Based on ending balances
        """)
        
        st.subheader("6. Flow of Costs")
        
        st.markdown("""
        ```
        RAW MATERIALS
        ↓
        Direct Materials → WORK IN PROCESS
        Indirect Materials → Manufacturing Overhead
        
        LABOR
        ↓
        Direct Labor → WORK IN PROCESS
        Indirect Labor → Manufacturing Overhead
        
        OTHER OVERHEAD COSTS → Manufacturing Overhead
        
        Manufacturing Overhead (Applied) → WORK IN PROCESS
        
        WORK IN PROCESS (Completed jobs) → FINISHED GOODS
        
        FINISHED GOODS (Sold) → COST OF GOODS SOLD
        ```
        """)
    
    with tab2:
        st.header("Practical Examples")
        
        st.subheader("Example 1: Predetermined Overhead Rate")
        
        st.markdown("""
        **Given:**
        - Estimated Manufacturing Overhead: $500,000
        - Estimated Direct Labor Hours: 25,000 hours
        - Estimated Machine Hours: 10,000 hours
        
        **Calculate:** Predetermined OH rates using both bases
        
        **Solution:**
        
        **Using Direct Labor Hours:**
        ```
        Predetermined OH Rate = $500,000 / 25,000 hours
                             = $20 per direct labor hour
        ```
        
        **Using Machine Hours:**
        ```
        Predetermined OH Rate = $500,000 / 10,000 hours
                             = $50 per machine hour
        ```
        """)
        
        st.subheader("Example 2: Complete Job Costing")
        
        st.markdown("""
        **Job #101 Information:**
        - Direct Materials: $15,000
        - Direct Labor: 200 hours @ $25/hour
        - Predetermined OH Rate: $20 per DLH
        - Units Produced: 100 units
        
        **Solution:**
        
        **Step 1: Calculate Direct Labor Cost**
        ```
        Direct Labor = 200 hours × $25/hour = $5,000
        ```
        
        **Step 2: Calculate Applied Overhead**
        ```
        Applied OH = 200 hours × $20/hour = $4,000
        ```
        
        **Step 3: Calculate Total Job Cost**
        ```
        Direct Materials      $15,000
        Direct Labor           $5,000
        Overhead Applied       $4,000
        ─────────────────────────────
        Total Job Cost        $24,000
        ```
        
        **Step 4: Calculate Cost per Unit**
        ```
        Cost per Unit = $24,000 / 100 units = $240 per unit
        ```
        """)
        
        st.subheader("Example 3: Under/Overapplied Overhead")
        
        st.markdown("""
        **Year-End Information:**
        - Actual Manufacturing Overhead: $485,000
        - Applied Manufacturing Overhead: $500,000
        - Ending Balances:
          - Work in Process: $50,000
          - Finished Goods: $150,000
          - Cost of Goods Sold: $800,000
        
        **Solution:**
        
        **Step 1: Calculate Over/Underapplied**
        ```
        Applied OH           $500,000
        Actual OH            $485,000
        ─────────────────────────────
        Overapplied OH       $15,000 (credit)
        ```
        
        **Step 2: Disposition - Close to COGS (if immaterial)**
        ```
        Debit: Manufacturing Overhead    $15,000
        Credit: Cost of Goods Sold       $15,000
        ```
        
        **Step 3: Disposition - Prorate (if material)**
        ```
        Total = $50,000 + $150,000 + $800,000 = $1,000,000
        
        WIP: ($50,000 / $1,000,000) × $15,000 = $750
        FG: ($150,000 / $1,000,000) × $15,000 = $2,250
        COGS: ($800,000 / $1,000,000) × $15,000 = $12,000
        ```
        """)
        
        st.subheader("Example 4: Multiple Jobs")
        
        st.markdown("""
        **Company Data:**
        - Predetermined OH Rate: $30 per machine hour
        
        | Job | DM | DL | Machine Hours | Status |
        |-----|----|----|---------------|---------|
        | 201 | $8,000 | $6,000 | 150 | In Process |
        | 202 | $12,000 | $9,000 | 200 | Completed |
        | 203 | $5,000 | $4,000 | 100 | Completed & Sold |
        
        **Calculate:** WIP, FG, and COGS
        
        **Solution:**
        
        **Job 201 (WIP):**
        ```
        Direct Materials        $8,000
        Direct Labor            $6,000
        Applied OH (150 × $30)  $4,500
        Total                  $18,500
        ```
        
        **Job 202 (Finished Goods):**
        ```
        Direct Materials        $12,000
        Direct Labor             $9,000
        Applied OH (200 × $30)   $6,000
        Total                   $27,000
        ```
        
        **Job 203 (COGS):**
        ```
        Direct Materials        $5,000
        Direct Labor            $4,000
        Applied OH (100 × $30)  $3,000
        Total                  $12,000
        ```
        
        **Summary:**
        - Work in Process: $18,500
        - Finished Goods: $27,000
        - Cost of Goods Sold: $12,000
        """)
    
    with tab3:
        st.header("Interactive Calculators")
        
        calc_option = st.selectbox(
            "Select Calculator:",
            ["Predetermined OH Rate", "Job Cost Sheet", "Under/Overapplied OH", 
             "Multiple Jobs Analysis", "T-Account Analysis"]
        )
        
        if calc_option == "Predetermined OH Rate":
            st.subheader("🧮 Predetermined Overhead Rate Calculator")
            
            col1, col2 = st.columns(2)
            
            with col1:
                est_overhead = st.number_input(
                    "Estimated Manufacturing Overhead ($)", 
                    min_value=0.0, value=500000.0, step=10000.0
                )
            
            with col2:
                allocation_base = st.selectbox(
                    "Allocation Base",
                    ["Direct Labor Hours", "Machine Hours", "Direct Labor Cost", "Units"]
                )
            
            est_base = st.number_input(
                f"Estimated {allocation_base}", 
                min_value=0.0, value=25000.0, step=1000.0
            )
            
            if est_base > 0:
                pohr = est_overhead / est_base
                
                st.markdown("---")
                st.markdown("### Results:")
                
                if allocation_base in ["Direct Labor Hours", "Machine Hours"]:
                    st.success(f"**Predetermined OH Rate:** ${pohr:.2f} per {allocation_base.lower()}")
                elif allocation_base == "Direct Labor Cost":
                    st.success(f"**Predetermined OH Rate:** {pohr:.2%} of direct labor cost")
                else:
                    st.success(f"**Predetermined OH Rate:** ${pohr:.2f} per unit")
                
                # Application example
                st.markdown("**Apply to a Job:**")
                actual_base = st.number_input(
                    f"Actual {allocation_base} for Job", 
                    min_value=0.0, value=200.0, step=10.0
                )
                
                applied_oh = pohr * actual_base
                st.info(f"**Applied Overhead for this Job:** ${applied_oh:,.2f}")
            else:
                st.error("Estimated allocation base must be greater than zero")
        
        elif calc_option == "Job Cost Sheet":
            st.subheader("🧮 Job Cost Sheet Calculator")
            
            job_number = st.text_input("Job Number", value="101")
            customer = st.text_input("Customer Name", value="ABC Corporation")
            units = st.number_input("Units Produced", min_value=1, value=100, step=1)
            
            st.markdown("---")
            st.markdown("### Cost Inputs:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Direct Materials:**")
                dm_cost = st.number_input("Direct Materials Cost ($)", min_value=0.0, value=15000.0, step=100.0)
                
                st.markdown("**Direct Labor:**")
                dl_hours = st.number_input("Direct Labor Hours", min_value=0.0, value=200.0, step=10.0)
                dl_rate = st.number_input("Labor Rate ($/hour)", min_value=0.0, value=25.0, step=1.0)
            
            with col2:
                st.markdown("**Manufacturing Overhead:**")
                oh_base_type = st.selectbox(
                    "OH Allocation Base",
                    ["Direct Labor Hours", "Machine Hours", "Direct Labor Cost"],
                    key="job_oh_base"
                )
                
                if oh_base_type == "Direct Labor Hours":
                    oh_base_amount = dl_hours
                elif oh_base_type == "Machine Hours":
                    oh_base_amount = st.number_input("Machine Hours", min_value=0.0, value=150.0, step=10.0)
                else:
                    oh_base_amount = dl_hours * dl_rate
                
                oh_rate = st.number_input("Predetermined OH Rate", min_value=0.0, value=20.0, step=1.0)
            
            # Calculations
            dl_cost = dl_hours * dl_rate
            applied_oh = oh_rate * oh_base_amount
            total_cost = dm_cost + dl_cost + applied_oh
            cost_per_unit = total_cost / units if units > 0 else 0
            
            st.markdown("---")
            st.markdown("### Job Cost Summary:")
            
            cost_summary = pd.DataFrame({
                'Cost Element': ['Direct Materials', 'Direct Labor', 'Manufacturing Overhead', 'Total Job Cost'],
                'Amount': [dm_cost, dl_cost, applied_oh, total_cost],
                'Percentage': [
                    (dm_cost/total_cost*100) if total_cost > 0 else 0,
                    (dl_cost/total_cost*100) if total_cost > 0 else 0,
                    (applied_oh/total_cost*100) if total_cost > 0 else 0,
                    100.0
                ]
            })
            
            cost_summary['Amount'] = cost_summary['Amount'].apply(lambda x: f"${x:,.2f}")
            cost_summary['Percentage'] = cost_summary['Percentage'].apply(lambda x: f"{x:.1f}%")
            
            st.dataframe(cost_summary, use_container_width=True, hide_index=True)
            
            col_result1, col_result2 = st.columns(2)
            with col_result1:
                st.metric("Total Job Cost", f"${total_cost:,.2f}")
            with col_result2:
                st.metric("Cost per Unit", f"${cost_per_unit:.2f}")
            
            # Complete Job Cost Sheet
            if st.checkbox("Show Complete Job Cost Sheet"):
                st.markdown(f"""
                ```
                ═══════════════════════════════════════════════
                             JOB COST SHEET
                ═══════════════════════════════════════════════
                Job Number:      {job_number}
                Customer:        {customer}
                Units Produced:  {units}
                ───────────────────────────────────────────────
                DIRECT MATERIALS                    ${dm_cost:,.2f}
                
                DIRECT LABOR
                {dl_hours:.0f} hours @ ${dl_rate:.2f}/hour    ${dl_cost:,.2f}
                
                MANUFACTURING OVERHEAD APPLIED
                {oh_base_amount:.0f} {oh_base_type.lower()} @ ${oh_rate:.2f}
                                                    ${applied_oh:,.2f}
                ───────────────────────────────────────────────
                TOTAL JOB COST                      ${total_cost:,.2f}
                
                COST PER UNIT                       ${cost_per_unit:.2f}
                ═══════════════════════════════════════════════
                ```
                """)
        
        elif calc_option == "Under/Overapplied OH":
            st.subheader("🧮 Under/Overapplied Overhead Calculator")
            
            col1, col2 = st.columns(2)
            
            with col1:
                actual_oh = st.number_input(
                    "Actual Manufacturing Overhead ($)", 
                    min_value=0.0, value=485000.0, step=1000.0
                )
            
            with col2:
                applied_oh = st.number_input(
                    "Applied Manufacturing Overhead ($)", 
                    min_value=0.0, value=500000.0, step=1000.0
                )
            
            variance = applied_oh - actual_oh
            
            st.markdown("---")
            st.markdown("### Analysis:")
            
            if variance > 0:
                st.success(f"**Overapplied Overhead:** ${abs(variance):,.2f}")
                st.info("Applied OH > Actual OH → Too much overhead charged to jobs")
            elif variance < 0:
                st.error(f"**Underapplied Overhead:** ${abs(variance):,.2f}")
                st.info("Applied OH < Actual OH → Too little overhead charged to jobs")
            else:
                st.success("**Perfectly Applied** - No variance")
            
            # Disposition
            st.markdown("---")
            st.markdown("### Disposition Options:")
            
            disposition = st.radio(
                "Select Disposition Method:",
                ["Close to COGS (Immaterial)", "Prorate (Material)"]
            )
            
            if disposition == "Close to COGS (Immaterial)":
                st.markdown("**Journal Entry:**")
                if variance > 0:
                    st.code(f"""
Debit: Manufacturing Overhead        ${abs(variance):,.2f}
Credit: Cost of Goods Sold            ${abs(variance):,.2f}

Effect: Decreases COGS by ${abs(variance):,.2f}
                    """)
                elif variance < 0:
                    st.code(f"""
Debit: Cost of Goods Sold             ${abs(variance):,.2f}
Credit: Manufacturing Overhead        ${abs(variance):,.2f}

Effect: Increases COGS by ${abs(variance):,.2f}
                    """)
            
            else:  # Prorate
                st.markdown("**Enter Ending Balances:**")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    wip_balance = st.number_input("Work in Process ($)", min_value=0.0, value=50000.0, step=1000.0)
                with col2:
                    fg_balance = st.number_input("Finished Goods ($)", min_value=0.0, value=150000.0, step=1000.0)
                with col3:
                    cogs_balance = st.number_input("Cost of Goods Sold ($)", min_value=0.0, value=800000.0, step=1000.0)
                
                total_balance = wip_balance + fg_balance + cogs_balance
                
                if total_balance > 0:
                    wip_allocation = (wip_balance / total_balance) * abs(variance)
                    fg_allocation = (fg_balance / total_balance) * abs(variance)
                    cogs_allocation = (cogs_balance / total_balance) * abs(variance)
                    
                    prorate_data = pd.DataFrame({
                        'Account': ['Work in Process', 'Finished Goods', 'Cost of Goods Sold', 'Total'],
                        'Balance': [wip_balance, fg_balance, cogs_balance, total_balance],
                        'Percentage': [
                            (wip_balance/total_balance*100),
                            (fg_balance/total_balance*100),
                            (cogs_balance/total_balance*100),
                            100.0
                        ],
                        'Allocation': [wip_allocation, fg_allocation, cogs_allocation, abs(variance)]
                    })
                    
                    prorate_data['Balance'] = prorate_data['Balance'].apply(lambda x: f"${x:,.2f}")
                    prorate_data['Percentage'] = prorate_data['Percentage'].apply(lambda x: f"{x:.2f}%")
                    prorate_data['Allocation'] = prorate_data['Allocation'].apply(lambda x: f"${x:,.2f}")
                    
                    st.dataframe(prorate_data, use_container_width=True, hide_index=True)
        
        elif calc_option == "Multiple Jobs Analysis":
            st.subheader("🧮 Multiple Jobs Analyzer")
            
            st.markdown("**Overhead Information:**")
            multi_oh_rate = st.number_input(
                "Predetermined OH Rate ($/hour)", 
                min_value=0.0, value=30.0, step=1.0,
                key="multi_oh"
            )
            
            st.markdown("---")
            st.markdown("### Job Details:")
            
            num_jobs = st.number_input("Number of Jobs", min_value=1, max_value=10, value=3, step=1)
            
            jobs_data = []
            
            for i in range(num_jobs):
                st.markdown(f"**Job #{i+1}:**")
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    dm = st.number_input(f"Direct Materials", min_value=0.0, value=10000.0, step=100.0, key=f"dm_{i}")
                with col2:
                    dl = st.number_input(f"Direct Labor", min_value=0.0, value=5000.0, step=100.0, key=f"dl_{i}")
                with col3:
                    hours = st.number_input(f"Hours", min_value=0.0, value=100.0, step=10.0, key=f"hours_{i}")
                with col4:
                    status = st.selectbox(
                        f"Status", 
                        ["In Process", "Completed", "Sold"],
                        key=f"status_{i}"
                    )
                
                applied_oh_job = multi_oh_rate * hours
                total_cost_job = dm + dl + applied_oh_job
                
                jobs_data.append({
                    'Job': f'Job {i+1}',
                    'DM': dm,
                    'DL': dl,
                    'Hours': hours,
                    'Applied OH': applied_oh_job,
                    'Total Cost': total_cost_job,
                    'Status': status
                })
            
            df_jobs = pd.DataFrame(jobs_data)
            
            st.markdown("---")
            st.markdown("### Jobs Summary:")
            
            display_df = df_jobs.copy()
            display_df['DM'] = display_df['DM'].apply(lambda x: f"${x:,.2f}")
            display_df['DL'] = display_df['DL'].apply(lambda x: f"${x:,.2f}")
            display_df['Applied OH'] = display_df['Applied OH'].apply(lambda x: f"${x:,.2f}")
            display_df['Total Cost'] = display_df['Total Cost'].apply(lambda x: f"${x:,.2f}")
            
            st.dataframe(display_df, use_container_width=True, hide_index=True)
            
            # Calculate balances
            wip_total = df_jobs[df_jobs['Status'] == 'In Process']['Total Cost'].sum()
            fg_total = df_jobs[df_jobs['Status'] == 'Completed']['Total Cost'].sum()
            cogs_total = df_jobs[df_jobs['Status'] == 'Sold']['Total Cost'].sum()
            
            st.markdown("### Account Balances:")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Work in Process", f"${wip_total:,.2f}")
            with col2:
                st.metric("Finished Goods", f"${fg_total:,.2f}")
            with col3:
                st.metric("Cost of Goods Sold", f"${cogs_total:,.2f}")
        
        else:  # T-Account Analysis
            st.subheader("🧮 T-Account Flow Analysis")
            
            st.markdown("### Beginning Balances:")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                beg_rm = st.number_input("Raw Materials", min_value=0.0, value=20000.0, step=1000.0, key="beg_rm")
            with col2:
                beg_wip = st.number_input("Work in Process", min_value=0.0, value=30000.0, step=1000.0, key="beg_wip")
            with col3:
                beg_fg = st.number_input("Finished Goods", min_value=0.0, value=40000.0, step=1000.0, key="beg_fg")
            
            st.markdown("### Transactions:")
            
            purchases = st.number_input("Raw Materials Purchased", min_value=0.0, value=100000.0, step=1000.0)
            direct_mat = st.number_input("Direct Materials Used", min_value=0.0, value=80000.0, step=1000.0)
            indirect_mat = st.number_input("Indirect Materials Used", min_value=0.0, value=10000.0, step=1000.0)
            direct_lab = st.number_input("Direct Labor", min_value=0.0, value=50000.0, step=1000.0)
            indirect_lab = st.number_input("Indirect Labor", min_value=0.0, value=15000.0, step=1000.0)
            other_oh = st.number_input("Other Manufacturing OH", min_value=0.0, value=25000.0, step=1000.0)
            applied = st.number_input("Overhead Applied to WIP", min_value=0.0, value=45000.0, step=1000.0)
            completed = st.number_input("Cost of Jobs Completed", min_value=0.0, value=150000.0, step=1000.0)
            sold = st.number_input("Cost of Jobs Sold", min_value=0.0, value=140000.0, step=1000.0)
            
            # Calculate ending balances
            end_rm = beg_rm + purchases - direct_mat - indirect_mat
            end_wip = beg_wip + direct_mat + direct_lab + applied - completed
            end_fg = beg_fg + completed - sold
            actual_oh = indirect_mat + indirect_lab + other_oh
            variance_oh = applied - actual_oh
            
            st.markdown("---")
            st.markdown("### Ending Balances:")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Raw Materials", f"${end_rm:,.2f}", f"{end_rm - beg_rm:,.2f}")
            with col2:
                st.metric("Work in Process", f"${end_wip:,.2f}", f"{end_wip - beg_wip:,.2f}")
            with col3:
                st.metric("Finished Goods", f"${end_fg:,.2f}", f"{end_fg - beg_fg:,.2f}")
            
            st.markdown("### Manufacturing Overhead Analysis:")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Actual Overhead", f"${actual_oh:,.2f}")
            with col2:
                st.metric("Applied Overhead", f"${applied:,.2f}")
            with col3:
                if variance_oh > 0:
                    st.metric("Overapplied", f"${variance_oh:,.2f}")
                else:
                    st.metric("Underapplied", f"${abs(variance_oh):,.2f}")
            
            st.metric("Cost of Goods Sold", f"${sold:,.2f}")
    
    with tab4:
        st.header("Visual Analytics")
        
        st.subheader("Job Cost Flow Diagram")
        
        # Sankey diagram for cost flow
        labels = ["Raw Materials", "Direct Materials", "Indirect Materials", "Labor", 
                 "Direct Labor", "Indirect Labor", "Other OH Costs", 
                 "Mfg Overhead", "Work in Process", "Finished Goods", "COGS"]
        
        source = [0, 0, 3, 3, 6, 7, 7, 1, 4, 7, 8, 9]
        target = [1, 2, 4, 5, 7, 2, 5, 8, 8, 8, 9, 10]
        value = [80, 10, 50, 15, 25, 10, 15, 80, 50, 45, 150, 140]
        
        fig_sankey = go.Figure(data=[go.Sankey(
            node = dict(
                pad = 15,
                thickness = 20,
                line = dict(color = "black", width = 0.5),
                label = labels,
                color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#ff9896"]
            ),
            link = dict(
                source = source,
                target = target,
                value = value
            )
        )])
        
        fig_sankey.update_layout(
            title="Cost Flow in Job Order Costing",
            font_size=10,
            height=600
        )
        
        st.plotly_chart(fig_sankey, use_container_width=True)
        
        # Job cost composition
        st.subheader("Job Cost Composition")
        
        job_composition = pd.DataFrame({
            'Cost Element': ['Direct Materials', 'Direct Labor', 'Manufacturing Overhead'],
            'Amount': [15000, 5000, 4000]
        })
        
        fig_pie = px.pie(
            job_composition, 
            values='Amount', 
            names='Cost Element',
            title='Typical Job Cost Breakdown',
            color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # Overhead variance visualization
        st.subheader("Overhead Variance Analysis")
        
        oh_data = pd.DataFrame({
            'Type': ['Actual OH', 'Applied OH'],
            'Amount': [485000, 500000]
        })
        
        fig_bar = px.bar(
            oh_data, 
            x='Type', 
            y='Amount',
            title='Actual vs. Applied Overhead',
            color='Type',
            color_discrete_map={'Actual OH': '#ff7f0e', 'Applied OH': '#1f77b4'}
        )
        
        fig_bar.add_hline(
            y=492500, 
            line_dash="dash", 
            annotation_text="Target",
            line_color="red"
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab5:
        st.header("Knowledge Check Quiz")
        
        st.subheader("Test Your Understanding")
        
        # Question 1
        st.markdown("**1. Job order costing is most appropriate for:**")
        q1 = st.radio(
            "Select your answer:",
            [
                "Oil refining",
                "Custom furniture manufacturing",
                "Soft drink bottling",
                "Flour milling"
            ],
            key="q1"
        )
        
        if st.button("Check Answer", key="check1"):
            if q1 == "Custom furniture manufacturing":
                st.success("✅ Correct! Job order costing is used for custom, unique products.")
            else:
                st.error("❌ Incorrect. Job order costing is best for custom, made-to-order products.")
        
        st.markdown("---")
        
        # Question 2
        st.markdown("""
        **2. If estimated overhead is $400,000 and estimated direct labor hours are 20,000, 
        what is the predetermined overhead rate?**
        """)
        q2 = st.radio(
            "Select your answer:",
            ["$10 per DLH", "$15 per DLH", "$20 per DLH", "$25 per DLH"],
            key="q2"
        )
        
        if st.button("Check Answer", key="check2"):
            if q2 == "$20 per DLH":
                st.success("✅ Correct! POHR = $400,000 / 20,000 = $20 per DLH")
            else:
                st.error("❌ Incorrect. POHR = $400,000 / 20,000 hours = $20 per DLH")
        
        st.markdown("---")
        
        # Question 3
        st.markdown("""
        **3. If actual overhead is $450,000 and applied overhead is $430,000, overhead is:**
        """)
        q3 = st.radio(
            "Select your answer:",
            [
                "Overapplied by $20,000",
                "Underapplied by $20,000",
                "Overapplied by $430,000",
                "Perfectly applied"
            ],
            key="q3"
        )
        
        if st.button("Check Answer", key="check3"):
            if q3 == "Underapplied by $20,000":
                st.success("✅ Correct! Actual ($450,000) > Applied ($430,000) = Underapplied $20,000")
            else:
                st.error("❌ Incorrect. When actual > applied, overhead is underapplied.")
        
        st.markdown("---")
        
        # Question 4
        st.markdown("""
        **4. A job has DM = $10,000, DL = 100 hours @ $30/hour, and applied OH = $25/DLH. 
        What is the total job cost?**
        """)
        q4 = st.radio(
            "Select your answer:",
            ["$13,000", "$15,500", "$17,500", "$20,000"],
            key="q4"
        )
        
        if st.button("Check Answer", key="check4"):
            if q4 == "$15,500":
                st.success("✅ Correct! DM ($10,000) + DL ($3,000) + OH ($2,500) = $15,500")
            else:
                st.error("❌ Incorrect. $10,000 + (100×$30) + (100×$25) = $15,500")
        
        st.markdown("---")
        
        # Question 5
        st.markdown("**5. Which document authorizes the withdrawal of materials from the storeroom?**")
        q5 = st.radio(
            "Select your answer:",
            [
                "Job cost sheet",
                "Materials requisition form",
                "Time ticket",
                "Purchase order"
            ],
            key="q5"
        )
        
        if st.button("Check Answer", key="check5"):
            if q5 == "Materials requisition form":
                st.success("✅ Correct! The materials requisition form authorizes material withdrawal.")
            else:
                st.error("❌ Incorrect. The materials requisition form is used to withdraw materials.")
    
    with tab6:
        st.header("Module Summary")
        
        st.subheader("🎯 Key Takeaways")
        
        st.markdown("""
        ### 1. Job Order Costing System
        
        **When to Use:**
        - Custom products
        - Each job is unique
        - Made-to-order production
        - Service industries (law, consulting, repair)
        
        **Industries:**
        - Construction
        - Custom furniture
        - Printing
        - Repair services
        - Professional services
        
        ### 2. Key Documents
        
        | Document | Purpose |
        |----------|---------|
        | Job Cost Sheet | Master document for accumulating all job costs |
        | Materials Requisition | Authorizes withdrawal of materials |
        | Time Ticket | Records labor hours by job |
        | Predetermined OH Rate | Used to apply overhead to jobs |
        
        ### 3. Important Formulas
        
        #### Predetermined Overhead Rate:
        ```
        POHR = Estimated Total Manufacturing Overhead
               ─────────────────────────────────────
               Estimated Allocation Base
        ```
        
        #### Applied Overhead:
        ```
        Applied OH = POHR × Actual Allocation Base
        ```
        
        #### Total Job Cost:
        ```
        Job Cost = Direct Materials + Direct Labor + Applied Overhead
        ```
        
        #### Cost Per Unit:
        ```
        Cost per Unit = Total Job Cost / Units Produced
        ```
        
        #### Under/Overapplied Overhead:
        ```
        Variance = Applied Overhead - Actual Overhead
        
        If positive → Overapplied (credit balance)
        If negative → Underapplied (debit balance)
        ```
        
        ### 4. Cost Flow Summary
        
        ```
        RAW MATERIALS
        ↓
        Direct Materials → WORK IN PROCESS
        Indirect Materials → Manufacturing Overhead
        
        LABOR
        ↓
        Direct Labor → WORK IN PROCESS
        Indirect Labor → Manufacturing Overhead
        
        Manufacturing Overhead (Applied) → WORK IN PROCESS
        
        WORK IN PROCESS (Completed) → FINISHED GOODS
        
        FINISHED GOODS (Sold) → COST OF GOODS SOLD
        ```
        
        ### 5. Overhead Disposition
        
        **Immaterial Variance (Close to COGS):**
        - Underapplied: Debit COGS, Credit MOH
        - Overapplied: Debit MOH, Credit COGS
        
        **Material Variance (Prorate):**
        - Allocate to WIP, FG, and COGS
        - Based on ending balances
        - Maintains better matching
        
        ### 6. Common Allocation Bases
        
        | Base | Best Used When |
        |------|----------------|
        | Direct Labor Hours | Labor-intensive processes |
        | Machine Hours | Automated/machine-intensive |
        | Direct Labor Cost | Different wage rates |
        | Units Produced | Homogeneous products |
        
        ### 7. Job Cost Sheet Template
        
        ```
        JOB COST SHEET
        Job Number: ___________
        Customer: ___________
        Date Started: ___________
        Date Completed: ___________
        
        DIRECT MATERIALS
        Date    Req#    Amount
        
        DIRECT LABOR
        Date    Ticket#    Hours    Rate    Amount
        
        OVERHEAD APPLIED
        Base    Rate    Amount
        
        SUMMARY
        Direct Materials        $_______
        Direct Labor            $_______
        Overhead Applied        $_______
        ──────────────────────────────
        Total Job Cost          $_______
        Units                   _______
        Cost per Unit           $_______
        ```
        
        ### 8. Decision-Making Applications
        
        **Pricing Decisions:**
        - Calculate full product cost
        - Add desired markup
        - Consider market conditions
        
        **Profitability Analysis:**
        - Compare job costs to revenue
        - Identify high-cost jobs
        - Improve cost estimation
        
        **Capacity Planning:**
        - Track job completion times
        - Identify bottlenecks
        - Optimize resource allocation
        
        ### 9. Best Practices
        
        1. **Accurate Time Tracking:** Essential for proper cost allocation
        2. **Regular OH Rate Updates:** Review and adjust annually
        3. **Timely Job Costing:** Update job cost sheets regularly
        4. **Variance Analysis:** Investigate significant variances
        5. **Document Control:** Maintain proper authorization
        6. **Cost Estimation:** Learn from historical job data
        
        ### 10. Common Mistakes to Avoid
        
        ❌ Using actual OH instead of applied OH
        ❌ Forgetting to update POHR annually
        ❌ Mixing direct and indirect costs
        ❌ Not reconciling OH at period end
        ❌ Ignoring material variances
        ❌ Poor documentation of time and materials
        """)
        
        st.subheader("📊 Quick Reference Table")
        
        quick_ref = {
            'Account': ['Raw Materials', 'Work in Process', 'Finished Goods', 'COGS', 'Mfg Overhead'],
            'Debited For': [
                'Purchases',
                'DM used, DL, Applied OH',
                'Completed jobs',
                'Sold jobs',
                'Actual OH costs'
            ],
            'Credited For': [
                'Materials issued',
                'Completed jobs',
                'Sold jobs',
                'OH adjustments',
                'Applied OH'
            ]
        }
        
        df_ref = pd.DataFrame(quick_ref)
        st.dataframe(df_ref, use_container_width=True, hide_index=True)
        
        st.success("🎓 **You've completed Module 3!** You can now implement and analyze job order costing systems.")
        
        st.info("💡 **Next Steps**: Proceed to Module 4 to learn about Process Costing Systems.")

if __name__ == "__main__":
    show()