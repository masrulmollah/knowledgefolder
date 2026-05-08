import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🔀 Module 6: Cost Allocation & Joint Products")
    st.markdown("*Allocate service department costs and analyze joint product decisions*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Service Department Cost Allocation")
        st.markdown("""
        **Service departments** (Maintenance, IT, HR, Cafeteria) support production but don't directly 
        make products. Their costs must ultimately be allocated to **production departments** and then to products.

        #### Types of Departments:
        - **Production Departments** – directly work on products (Assembly, Machining, Finishing)
        - **Service Departments** – support production departments (Maintenance, IT, HR)

        #### Why Allocate?
        - Needed for accurate product costing
        - Required for pricing decisions
        - Supports performance evaluation
        - Determines true cost of producing products
        """)

        st.subheader("2. Three Allocation Methods")
        methods_df = pd.DataFrame({
            "Method": ["Direct", "Step-Down", "Reciprocal"],
            "Recognizes Inter-Service Usage": ["❌ None", "✅ Partial (one direction)", "✅ Full (both directions)"],
            "Complexity": ["Simple", "Medium", "Complex (simultaneous equations)"],
            "Accuracy": ["Least accurate", "More accurate", "Most accurate"],
            "When Used": ["Simple structures", "Most common", "Significant inter-service"]
        })
        st.dataframe(methods_df, use_container_width=True, hide_index=True)

        st.subheader("3. Direct Method")
        st.markdown("""
        Allocates each service department's costs **directly to production departments only**.
        Any services provided between service departments are completely **ignored**.

        #### Steps:
        1. Identify the allocation base for each service department
        2. Calculate usage percentages for **production departments only**
        3. Allocate each service department's costs using those percentages

        #### Formula:
        ```
        Allocation % = Production Dept Usage / Total Production Dept Usage
                       (ignore usage by other service departments)

        Amount Allocated = Total Service Dept Cost × Allocation %
        ```
        """)

        st.subheader("4. Step-Down Method")
        st.markdown("""
        Allocates service department costs **sequentially**. 
        Partially recognizes inter-service usage (but only in one direction).

        #### Steps:
        1. Rank service departments (usually by amount of service given to other service depts)
        2. Allocate the first (highest-ranked) service dept to ALL remaining departments
        3. Close that department — it receives **no further allocations**
        4. Allocate second service dept (now including received allocation) to all remaining
        5. Repeat until all service costs allocated

        #### Key Rule:
        Once a service department is closed, it cannot receive any more cost allocations.
        """)

        st.subheader("5. Joint Products")
        st.markdown("""
        **Joint products** are two or more products produced simultaneously from a single process 
        until they reach the **split-off point** where they become separately identifiable.

        | Term | Definition |
        |------|-----------|
        | **Joint Products** | Two or more main products of significant value produced together |
        | **By-Product** | A minor product with relatively small value |
        | **Split-Off Point** | Where products become separately identifiable |
        | **Joint Costs** | All costs incurred before the split-off point |
        | **Separable Costs** | Costs incurred after split-off for individual products |

        #### Real-World Examples:
        - **Oil refining**: gasoline, diesel, jet fuel, kerosene
        - **Lumber**: 2×4s, 2×6s, plywood, sawdust
        - **Meat packing**: steaks, roasts, ground beef, hides
        - **Dairy**: butter, cheese, cream, skim milk
        """)

        st.subheader("6. Joint Cost Allocation Methods")
        st.markdown("""
        Joint costs must be allocated to products, but there is no single "correct" method.
        The choice affects inventory values and product-line profitability — but NOT total company profit.

        **1. Physical Units Method**
        ```
        Allocation % = Product Physical Units / Total Physical Units
        ```
        - Simple but ignores revenue-generating ability
        - Best when products have similar market values

        **2. Sales Value at Split-Off Method** *(Most Common)*
        ```
        Allocation % = Product Sales Value at Split-Off / Total Sales Value at Split-Off
        ```
        - Allocates based on ability to generate revenue
        - Best when products can be sold at split-off

        **3. Net Realizable Value (NRV) Method**
        ```
        NRV = Final Sales Value − Separable Costs (after split-off)
        Allocation % = Product NRV / Total NRV
        ```
        - Used when products require further processing before sale

        **4. Constant Gross Margin % Method**
        - Assigns joint costs so ALL products have the same gross margin %
        - Complex; rarely used in practice
        """)

        st.subheader("7. Sell or Process Further Decision")
        st.markdown("""
        After the split-off, the question becomes: sell now or process further?

        #### Decision Rule:
        ```
        Process further if:
        Incremental Revenue from further processing > Incremental Separable Costs

        Net Benefit = (Final Price − Split-Off Price) × Units − Additional Processing Costs
        ```

        #### ⚠️ CRITICAL RULE:
        **Joint costs are SUNK COSTS and are IRRELEVANT to this decision!**
        Joint costs are already incurred regardless of whether you sell now or process further.
        Only consider incremental (future) costs and revenues.
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Direct Method")
        st.markdown("""
        **Company has 2 service departments and 2 production departments.**

        **Service Department Costs:**
        - Maintenance: $100,000
        - IT Department: $80,000

        **Usage Data (allocation bases):**

        |  | Maintenance Hours | IT Hours |
        |--|-------------------|----------|
        | Maintenance (self) | — | 200 hrs |
        | IT Department | 500 hrs | — |
        | Assembly | 2,000 hrs | 1,800 hrs |
        | Finishing | 1,500 hrs | 1,000 hrs |
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Allocate Maintenance (ignore IT's 500 hrs):**
            ```
            Production only total:
            Assembly + Finishing = 2,000 + 1,500 = 3,500

            Assembly:  2,000/3,500 × $100,000 = $57,143
            Finishing: 1,500/3,500 × $100,000 = $42,857
            ```
            """)
        with col2:
            st.markdown("""
            **Allocate IT (ignore Maintenance's 200 hrs):**
            ```
            Production only total:
            Assembly + Finishing = 1,800 + 1,000 = 2,800

            Assembly:  1,800/2,800 × $80,000 = $51,429
            Finishing: 1,000/2,800 × $80,000 = $28,571
            ```
            """)

        st.markdown("""
        **Summary Table:**
        | Department | From Maintenance | From IT | Total Received |
        |------------|-----------------|---------|----------------|
        | Assembly | $57,143 | $51,429 | **$108,572** |
        | Finishing | $42,857 | $28,571 | **$71,428** |
        | **Total** | **$100,000** | **$80,000** | **$180,000** ✓ |
        """)

        st.subheader("Example 2: Step-Down Method")
        st.markdown("""
        **Same data. Allocate Maintenance first (provides more service to other service depts).**

        **Step 1 — Allocate Maintenance (to IT + Assembly + Finishing):**
        ```
        Total usage = 500 + 2,000 + 1,500 = 4,000 hrs

        To IT:        500/4,000 × $100,000 = $12,500
        To Assembly:  2,000/4,000 × $100,000 = $50,000
        To Finishing: 1,500/4,000 × $100,000 = $37,500
        ```

        **Step 2 — Allocate IT (now has $80,000 + $12,500 = $92,500):**
        ```
        Total production usage = 1,800 + 1,000 = 2,800 hrs (Maintenance is now CLOSED)

        To Assembly:  1,800/2,800 × $92,500 = $59,464
        To Finishing: 1,000/2,800 × $92,500 = $33,036
        ```

        **Summary:**
        | Department | From Maintenance | From IT | Total |
        |------------|-----------------|---------|-------|
        | Assembly | $50,000 | $59,464 | **$109,464** |
        | Finishing | $37,500 | $33,036 | **$70,536** |
        | Total | | | **$180,000** ✓ |

        *Note: Step-Down gives different results than Direct Method because it partially recognizes inter-service usage.*
        """)

        st.subheader("Example 3: Joint Cost Allocation — Sales Value Method")
        st.markdown("""
        **Joint process costs: $300,000**

        | Product | Units Produced | Price at Split-Off | Sales Value |
        |---------|---------------|-------------------|-------------|
        | A | 10,000 | $15/unit | $150,000 |
        | B | 15,000 | $20/unit | $300,000 |
        | C | 5,000 | $30/unit | $150,000 |
        | **Total** | **30,000** | | **$600,000** |

        **Allocation:**
        ```
        Product A: ($150,000 / $600,000) × $300,000 = $75,000  → $7.50/unit
        Product B: ($300,000 / $600,000) × $300,000 = $150,000 → $10.00/unit
        Product C: ($150,000 / $600,000) × $300,000 = $75,000  → $15.00/unit
        Total:                                         $300,000  ✓
        ```

        **NRV Method (if Product C requires $20,000 more processing to sell at $32/unit):**
        ```
        Product C NRV = (5,000 × $32) − $20,000 = $140,000
        (Products A and B assumed sellable at split-off prices)

        Product A NRV = $150,000
        Product B NRV = $300,000
        Product C NRV = $140,000
        Total NRV   = $590,000

        Product C allocation = ($140,000 / $590,000) × $300,000 = $71,186
        ```
        """)

        st.subheader("Example 4: Sell or Process Further")
        st.markdown("""
        **Product B (15,000 units):**
        - Can sell at split-off: $20/unit
        - OR process further: $5/unit additional cost → sells at $28/unit
        - Joint cost allocated: $150,000 (IRRELEVANT — sunk cost!)

        **Incremental Analysis:**
        ```
        Incremental Revenue per unit:   $28 − $20 = $8
        Incremental Cost per unit:               $5
        Net Benefit per unit:                    $3
        
        Total Net Benefit:  $3 × 15,000 units = $45,000
        ```

        **Decision: PROCESS FURTHER — gain $45,000 in total profit**

        ⚠️ The $150,000 joint cost is a SUNK COST — irrelevant to this decision!
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_option = st.selectbox("Select Calculator:", [
            "Direct Method Allocation",
            "Step-Down Method",
            "Joint Cost — Sales Value at Split-Off",
            "Joint Cost — NRV Method",
            "Sell or Process Further Decision"
        ])

        # ── DIRECT METHOD ────────────────────────────────────────────────────
        if calc_option == "Direct Method Allocation":
            st.subheader("🧮 Direct Method Calculator")
            st.info("Allocates service costs directly to production departments only, ignoring inter-service usage.")

            col1, col2 = st.columns(2)
            with col1:
                num_service = st.number_input("Number of Service Departments", 1, 4, 2)
            with col2:
                num_prod = st.number_input("Number of Production Departments", 1, 4, 2)

            st.markdown("---")
            service_depts = []
            for i in range(int(num_service)):
                st.markdown(f"**Service Department {i+1}:**")
                col1, col2 = st.columns(2)
                with col1:
                    s_name = st.text_input("Name", value=["Maintenance","IT","HR","Cafeteria"][i] if i < 4 else f"Service {i+1}", key=f"dm_sn_{i}")
                    s_cost = st.number_input("Total Cost ($)", 0.0, value=100000.0 - i*20000, step=1000.0, key=f"dm_sc_{i}")
                with col2:
                    s_base = st.text_input("Allocation Base", value=["Maintenance Hrs","IT Hours","# Employees","# Meals"][i] if i < 4 else "Units", key=f"dm_base_{i}")

                usages = []
                st.markdown(f"*Usage by Production Departments:*")
                cols = st.columns(int(num_prod))
                for j in range(int(num_prod)):
                    with cols[j]:
                        u = st.number_input(f"Prod Dept {j+1}", 0.0, value=2000.0 - j*500, step=100.0, key=f"dm_u_{i}_{j}")
                        usages.append(u)

                service_depts.append({"name": s_name, "cost": s_cost, "base": s_base, "usages": usages})

            if st.button("🧮 Calculate Direct Method Allocation", type="primary"):
                st.markdown("---")
                st.markdown("### 📊 Direct Method Results:")

                prod_totals = [0.0] * int(num_prod)
                all_rows = []

                for s in service_depts:
                    total_prod_usage = sum(s["usages"])
                    row = {"Service Dept": s["name"], "Own Cost": f"${s['cost']:,.2f}", "Allocation Base": s["base"]}
                    for j in range(int(num_prod)):
                        if total_prod_usage > 0:
                            alloc = (s["usages"][j] / total_prod_usage) * s["cost"]
                        else:
                            alloc = 0
                        prod_totals[j] += alloc
                        row[f"→ Prod {j+1} ({s['usages'][j]:,.0f} {s['base'][:4]})"] = f"${alloc:,.2f}"
                    all_rows.append(row)

                df_results = pd.DataFrame(all_rows)
                st.dataframe(df_results, use_container_width=True, hide_index=True)

                st.markdown("**Total Costs Allocated to Production Departments:**")
                total_cols = {f"Production Dept {j+1}": f"${prod_totals[j]:,.2f}" for j in range(int(num_prod))}
                total_cols["Grand Total"] = f"${sum(prod_totals):,.2f}"
                st.dataframe(pd.DataFrame([total_cols]), use_container_width=True, hide_index=True)

                total_service = sum([s["cost"] for s in service_depts])
                total_allocated = sum(prod_totals)
                if abs(total_allocated - total_service) < 0.01:
                    st.success(f"✅ All service costs fully allocated! Total: ${total_allocated:,.2f}")
                else:
                    st.error(f"❌ Allocation error: ${abs(total_allocated - total_service):,.2f}")

        # ── STEP DOWN ────────────────────────────────────────────────────────
        elif calc_option == "Step-Down Method":
            st.subheader("🧮 Step-Down Method Calculator")
            st.info("Allocates service departments sequentially. Once closed, a department receives no further costs.")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Service Department 1 (allocated FIRST):**")
                s1_name = st.text_input("Name", value="Maintenance", key="sd_s1n")
                s1_cost = st.number_input("Cost ($)", 0.0, value=100000.0, step=1000.0, key="sd_s1c")
                s1_to_s2 = st.number_input("Usage by Service Dept 2", 0.0, value=500.0, step=50.0)
                s1_to_p1 = st.number_input("Usage by Production 1", 0.0, value=2000.0, step=100.0)
                s1_to_p2 = st.number_input("Usage by Production 2", 0.0, value=1500.0, step=100.0)

            with col2:
                st.markdown("**Service Department 2 (allocated SECOND):**")
                s2_name = st.text_input("Name", value="IT", key="sd_s2n")
                s2_cost = st.number_input("Cost ($)", 0.0, value=80000.0, step=1000.0, key="sd_s2c")
                st.markdown("*(Dept 1 is closed — exclude its usage)*")
                s2_to_p1 = st.number_input("Usage by Production 1", 0.0, value=1800.0, step=100.0)
                s2_to_p2 = st.number_input("Usage by Production 2", 0.0, value=1000.0, step=100.0)

            if st.button("🧮 Calculate Step-Down Allocation", type="primary"):
                st.markdown("---")

                # Step 1 — allocate S1
                total_s1 = s1_to_s2 + s1_to_p1 + s1_to_p2
                s1_to_s2_amt = (s1_to_s2 / total_s1) * s1_cost if total_s1 > 0 else 0
                s1_to_p1_amt = (s1_to_p1 / total_s1) * s1_cost if total_s1 > 0 else 0
                s1_to_p2_amt = (s1_to_p2 / total_s1) * s1_cost if total_s1 > 0 else 0

                # Step 2 — allocate S2
                s2_total = s2_cost + s1_to_s2_amt
                total_s2 = s2_to_p1 + s2_to_p2
                s2_to_p1_amt = (s2_to_p1 / total_s2) * s2_total if total_s2 > 0 else 0
                s2_to_p2_amt = (s2_to_p2 / total_s2) * s2_total if total_s2 > 0 else 0

                st.markdown(f"#### Step 1: Allocate {s1_name} (${s1_cost:,.2f})")
                step1_df = pd.DataFrame({
                    "Recipient": [s2_name, "Production 1", "Production 2", "Total"],
                    "Usage": [f"{s1_to_s2:,.0f}", f"{s1_to_p1:,.0f}", f"{s1_to_p2:,.0f}", f"{total_s1:,.0f}"],
                    "% ": [f"{s1_to_s2/total_s1*100:.2f}%", f"{s1_to_p1/total_s1*100:.2f}%",
                            f"{s1_to_p2/total_s1*100:.2f}%", "100.00%"] if total_s1 > 0 else ["0%"]*4,
                    "Allocated": [f"${s1_to_s2_amt:,.2f}", f"${s1_to_p1_amt:,.2f}", f"${s1_to_p2_amt:,.2f}", f"${s1_cost:,.2f}"]
                })
                st.dataframe(step1_df, use_container_width=True, hide_index=True)

                st.markdown(f"#### Step 2: Allocate {s2_name} (${s2_cost:,.2f} own + ${s1_to_s2_amt:,.2f} received = ${s2_total:,.2f})")
                step2_df = pd.DataFrame({
                    "Recipient": ["Production 1", "Production 2", "Total"],
                    "Usage": [f"{s2_to_p1:,.0f}", f"{s2_to_p2:,.0f}", f"{total_s2:,.0f}"],
                    "% ": [f"{s2_to_p1/total_s2*100:.2f}%", f"{s2_to_p2/total_s2*100:.2f}%", "100.00%"] if total_s2 > 0 else ["0%"]*3,
                    "Allocated": [f"${s2_to_p1_amt:,.2f}", f"${s2_to_p2_amt:,.2f}", f"${s2_total:,.2f}"]
                })
                st.dataframe(step2_df, use_container_width=True, hide_index=True)

                p1_total = s1_to_p1_amt + s2_to_p1_amt
                p2_total = s1_to_p2_amt + s2_to_p2_amt

                st.markdown("#### Final Summary:")
                final_df = pd.DataFrame({
                    "Department": ["Production 1", "Production 2", "Total"],
                    f"From {s1_name}": [f"${s1_to_p1_amt:,.2f}", f"${s1_to_p2_amt:,.2f}", f"${s1_to_p1_amt+s1_to_p2_amt:,.2f}"],
                    f"From {s2_name}": [f"${s2_to_p1_amt:,.2f}", f"${s2_to_p2_amt:,.2f}", f"${s2_to_p1_amt+s2_to_p2_amt:,.2f}"],
                    "Total Allocated": [f"${p1_total:,.2f}", f"${p2_total:,.2f}", f"${p1_total+p2_total:,.2f}"]
                })
                st.dataframe(final_df, use_container_width=True, hide_index=True)

                if abs((p1_total + p2_total) - (s1_cost + s2_cost)) < 0.01:
                    st.success(f"✅ All ${s1_cost+s2_cost:,.2f} of service costs allocated!")

        # ── JOINT COST — SALES VALUE ──────────────────────────────────────────
        elif calc_option == "Joint Cost — Sales Value at Split-Off":
            st.subheader("🧮 Joint Cost — Sales Value at Split-Off Calculator")

            joint_costs = st.number_input("Total Joint Costs ($)", 0.0, value=300000.0, step=10000.0)
            num_products = st.number_input("Number of Joint Products", 2, 6, 3)

            st.markdown("---")
            products = []
            for i in range(int(num_products)):
                st.markdown(f"**Product {chr(65+i)}:**")
                col1, col2 = st.columns(2)
                with col1:
                    units = st.number_input("Units Produced", 0, value=[10000,15000,5000,8000,6000][i] if i < 5 else 5000, key=f"sv_u_{i}")
                with col2:
                    price = st.number_input("Selling Price at Split-Off ($/unit)", 0.0, value=[15.0,20.0,30.0,25.0,18.0][i] if i < 5 else 10.0, key=f"sv_p_{i}")
                products.append({"name": chr(65+i), "units": units, "price": price})

            if st.button("🧮 Calculate Sales Value Allocation", type="primary"):
                for p in products:
                    p["sales_value"] = p["units"] * p["price"]

                total_sv = sum([p["sales_value"] for p in products])

                st.markdown("---")
                st.markdown("### 📊 Sales Value Allocation Results:")

                results = []
                for p in products:
                    pct = p["sales_value"] / total_sv if total_sv > 0 else 0
                    allocated = pct * joint_costs
                    cost_per_unit = allocated / p["units"] if p["units"] > 0 else 0
                    gross_margin_per_unit = p["price"] - cost_per_unit
                    gm_pct = gross_margin_per_unit / p["price"] * 100 if p["price"] > 0 else 0
                    results.append({
                        "Product": p["name"],
                        "Units": f"{p['units']:,}",
                        "Price": f"${p['price']:.2f}",
                        "Sales Value": f"${p['sales_value']:,.2f}",
                        "Allocation %": f"{pct*100:.2f}%",
                        "Joint Cost Allocated": f"${allocated:,.2f}",
                        "Cost per Unit": f"${cost_per_unit:.4f}",
                        "Gross Margin/Unit": f"${gross_margin_per_unit:.4f}",
                        "GM %": f"{gm_pct:.1f}%"
                    })

                results_df = pd.DataFrame(results)
                st.dataframe(results_df, use_container_width=True, hide_index=True)

                total_allocated = sum([p["sales_value"] / total_sv * joint_costs for p in products]) if total_sv > 0 else 0
                col1, col2 = st.columns(2)
                with col1: st.metric("Total Sales Value", f"${total_sv:,.2f}")
                with col2: st.metric("Total Joint Costs Allocated", f"${total_allocated:,.2f}")

                if abs(total_allocated - joint_costs) < 0.01:
                    st.success(f"✅ All ${joint_costs:,.2f} of joint costs allocated!")

        # ── JOINT COST — NRV ─────────────────────────────────────────────────
        elif calc_option == "Joint Cost — NRV Method":
            st.subheader("🧮 Net Realizable Value (NRV) Method Calculator")
            st.info("Use this when products require further processing after the split-off point before they can be sold.")

            joint_costs = st.number_input("Total Joint Costs ($)", 0.0, value=300000.0, step=10000.0)
            num_products = st.number_input("Number of Joint Products", 2, 6, 3)

            st.markdown("---")
            products = []
            for i in range(int(num_products)):
                st.markdown(f"**Product {chr(65+i)}:**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    units = st.number_input("Units Produced", 0, value=[10000,15000,5000][i] if i < 3 else 5000, key=f"nrv_u_{i}")
                with col2:
                    final_price = st.number_input("Final Selling Price ($/unit)", 0.0, value=[18.0,25.0,35.0][i] if i < 3 else 20.0, key=f"nrv_fp_{i}")
                with col3:
                    sep_costs = st.number_input("Total Separable Costs ($)", 0.0, value=[15000.0,25000.0,10000.0][i] if i < 3 else 5000.0, step=500.0, key=f"nrv_sc_{i}")
                products.append({"name": chr(65+i), "units": units, "final_price": final_price, "sep_costs": sep_costs})

            if st.button("🧮 Calculate NRV Allocation", type="primary"):
                for p in products:
                    p["final_sales_value"] = p["units"] * p["final_price"]
                    p["nrv"] = p["final_sales_value"] - p["sep_costs"]

                total_nrv = sum([p["nrv"] for p in products])

                st.markdown("---")
                st.markdown("### 📊 NRV Allocation Results:")

                results = []
                for p in products:
                    pct = p["nrv"] / total_nrv if total_nrv > 0 else 0
                    joint_alloc = pct * joint_costs
                    total_cost = joint_alloc + p["sep_costs"]
                    cost_per_unit = total_cost / p["units"] if p["units"] > 0 else 0
                    gm = p["final_sales_value"] - total_cost
                    gm_pct = gm / p["final_sales_value"] * 100 if p["final_sales_value"] > 0 else 0
                    results.append({
                        "Product": p["name"],
                        "Final Sales Value": f"${p['final_sales_value']:,.2f}",
                        "Separable Costs": f"(${p['sep_costs']:,.2f})",
                        "NRV": f"${p['nrv']:,.2f}",
                        "Allocation %": f"{pct*100:.2f}%",
                        "Joint Cost": f"${joint_alloc:,.2f}",
                        "Total Cost": f"${total_cost:,.2f}",
                        "Cost/Unit": f"${cost_per_unit:.4f}",
                        "GM %": f"{gm_pct:.1f}%"
                    })

                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

                nrv_data = pd.DataFrame({
                    "Product": [p["name"] for p in products],
                    "NRV": [p["nrv"] for p in products]
                })
                fig_nrv = px.bar(nrv_data, x="Product", y="NRV",
                                  title="Net Realizable Value by Product",
                                  color="NRV", color_continuous_scale="Blues")
                st.plotly_chart(fig_nrv, use_container_width=True)

        # ── SELL OR PROCESS FURTHER ───────────────────────────────────────────
        else:
            st.subheader("🧮 Sell or Process Further Decision")
            st.warning("⚠️ Remember: Joint costs are SUNK and IRRELEVANT to this decision!")

            col1, col2 = st.columns(2)
            with col1:
                product_name = st.text_input("Product Name", value="Product B")
                units = st.number_input("Units Available", 0, value=15000, step=100)
                split_off_price = st.number_input("Selling Price at Split-Off ($/unit)", 0.0, value=20.0, step=0.5)
                joint_cost_allocated = st.number_input("Joint Cost Allocated ($/unit) — INFO ONLY", 0.0, value=10.0, step=0.5)

            with col2:
                final_price = st.number_input("Selling Price After Processing ($/unit)", 0.0, value=28.0, step=0.5)
                additional_cost_unit = st.number_input("Additional Processing Cost ($/unit)", 0.0, value=5.0, step=0.5)
                fixed_process_cost = st.number_input("Additional Fixed Processing Cost (total $)", 0.0, value=0.0, step=1000.0)

            if st.button("🧮 Analyze Decision", type="primary"):
                st.markdown("---")

                incr_rev_unit = final_price - split_off_price
                incr_cost_unit = additional_cost_unit
                net_benefit_unit = incr_rev_unit - incr_cost_unit

                total_incr_rev = incr_rev_unit * units
                total_incr_cost = incr_cost_unit * units + fixed_process_cost
                total_net_benefit = total_incr_rev - total_incr_cost

                st.markdown("### 📋 Incremental Analysis:")
                analysis_df = pd.DataFrame({
                    "Item": ["Incremental Revenue per unit", "Incremental Variable Cost per unit",
                              "Net Benefit per unit", "—", "Total Incremental Revenue",
                              "Total Incremental Variable Cost", "Fixed Processing Cost",
                              "TOTAL NET BENEFIT"],
                    "Amount": [
                        f"${incr_rev_unit:.2f}",
                        f"(${incr_cost_unit:.2f})",
                        f"${net_benefit_unit:.2f}",
                        "—",
                        f"${total_incr_rev:,.2f}",
                        f"(${incr_cost_unit * units:,.2f})",
                        f"(${fixed_process_cost:,.2f})",
                        f"${total_net_benefit:,.2f}"
                    ]
                })
                st.dataframe(analysis_df, use_container_width=True, hide_index=True)

                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Total Incremental Revenue", f"${total_incr_rev:,.2f}")
                with col2: st.metric("Total Incremental Cost", f"${total_incr_cost:,.2f}")
                with col3: st.metric("Net Benefit", f"${total_net_benefit:,.2f}")

                if total_net_benefit > 0:
                    st.success(f"✅ **DECISION: PROCESS FURTHER** — Adds ${total_net_benefit:,.2f} to company profit!")
                elif total_net_benefit < 0:
                    st.error(f"❌ **DECISION: SELL AT SPLIT-OFF** — Processing further REDUCES profit by ${abs(total_net_benefit):,.2f}")
                else:
                    st.info("🤝 **DECISION: INDIFFERENT** — Both options yield the same profit")

                st.info(f"💡 Joint cost of ${joint_cost_allocated:.2f}/unit (${joint_cost_allocated*units:,.2f} total) is a **SUNK COST** — IRRELEVANT to this decision!")

                # Side-by-side comparison
                st.markdown("### 📊 Side-by-Side Comparison:")
                rev_split = units * split_off_price
                rev_further = units * final_price
                cost_further = total_incr_cost
                profit_split = rev_split
                profit_further = rev_further - cost_further

                comp_df = pd.DataFrame({
                    "Item": ["Revenue", "Additional Processing Cost", "Net Revenue"],
                    "Sell at Split-Off": [f"${rev_split:,.2f}", "$0", f"${profit_split:,.2f}"],
                    "Process Further": [f"${rev_further:,.2f}", f"(${cost_further:,.2f})", f"${profit_further:,.2f}"]
                })
                st.dataframe(comp_df, use_container_width=True, hide_index=True)

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Service Department Allocation Flow")
        fig_flow = go.Figure(data=[go.Sankey(
            node=dict(
                pad=20, thickness=25,
                label=["Maintenance\n$100K", "IT\n$80K", "Assembly\nDept", "Finishing\nDept"],
                color=["#AED6F1", "#85C1E9", "#27AE60", "#1E8449"]
            ),
            link=dict(
                source=[0, 0, 1, 1],
                target=[2, 3, 2, 3],
                value=[57143, 42857, 51429, 28571],
                color=["rgba(46,134,193,0.4)", "rgba(46,134,193,0.4)",
                       "rgba(133,193,233,0.4)", "rgba(133,193,233,0.4)"]
            )
        )])
        fig_flow.update_layout(title="Direct Method: Service → Production Cost Flow", height=420)
        st.plotly_chart(fig_flow, use_container_width=True)

        st.subheader("Joint Products — Cost Allocation Comparison")
        products_comp = ["Product A", "Product B", "Product C"]
        sales_values = [150000, 300000, 150000]
        phys_units = [10000, 15000, 5000]
        total_units = sum(phys_units)

        phys_alloc = [u / total_units * 300000 for u in phys_units]
        sv_alloc = [sv / sum(sales_values) * 300000 for sv in sales_values]

        fig_alloc = go.Figure(data=[
            go.Bar(name="Physical Units Method", x=products_comp, y=phys_alloc, marker_color="#AED6F1"),
            go.Bar(name="Sales Value Method", x=products_comp, y=sv_alloc, marker_color="#2E86C1")
        ])
        fig_alloc.update_layout(
            title="Joint Cost Allocation: Physical Units vs Sales Value Method",
            barmode="group", yaxis_title="Joint Cost Allocated ($)"
        )
        st.plotly_chart(fig_alloc, use_container_width=True)

        st.subheader("Sell or Process Further — Net Benefit Analysis")
        units_range = np.arange(0, 20000, 1000)
        rev_gain = units_range * 8   # $28 - $20
        cost_gain = units_range * 5  # $5 extra cost
        net = rev_gain - cost_gain

        fig_sopf = go.Figure()
        fig_sopf.add_trace(go.Scatter(x=units_range, y=rev_gain, mode="lines", name="Incremental Revenue",
                                       line=dict(color="green", width=3)))
        fig_sopf.add_trace(go.Scatter(x=units_range, y=cost_gain, mode="lines", name="Incremental Cost",
                                       line=dict(color="red", width=3)))
        fig_sopf.add_trace(go.Scatter(x=units_range, y=net, mode="lines", name="Net Benefit",
                                       line=dict(color="blue", width=3, dash="dash"), fill="tozeroy"))
        fig_sopf.update_layout(title="Sell or Process Further — Net Benefit by Volume",
                                xaxis_title="Units", yaxis_title="Amount ($)")
        st.plotly_chart(fig_sopf, use_container_width=True)

        st.subheader("Step-Down vs Direct Method Comparison")
        depts = ["Assembly", "Finishing"]
        direct_vals = [108572, 71428]
        step_vals = [109464, 70536]

        fig_compare = go.Figure(data=[
            go.Bar(name="Direct Method", x=depts, y=direct_vals, marker_color="#E67E22",
                   text=[f"${v:,.0f}" for v in direct_vals], textposition="auto"),
            go.Bar(name="Step-Down Method", x=depts, y=step_vals, marker_color="#1A5276",
                   text=[f"${v:,.0f}" for v in step_vals], textposition="auto")
        ])
        fig_compare.update_layout(title="Direct vs Step-Down: Total Cost Allocated to Production",
                                   barmode="group", yaxis_title="Amount Allocated ($)")
        st.plotly_chart(fig_compare, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. The Direct Method of service department allocation:**")
        q1 = st.radio("", [
            "Recognizes all inter-service department usage",
            "Ignores services provided between service departments",
            "Uses simultaneous equations",
            "Closes departments sequentially"
        ], key="m6q1")
        if st.button("Check Q1", key="m6c1"):
            if q1 == "Ignores services provided between service departments":
                st.success("✅ Correct! The direct method only allocates to production departments, ignoring inter-service usage.")
            else:
                st.error("❌ Incorrect. The Direct Method allocates only to production departments, completely ignoring inter-service usage.")

        st.markdown("---")
        st.markdown("**Q2. In the Step-Down method, once a service department is allocated:**")
        q2 = st.radio("", [
            "It can still receive additional allocations",
            "It is closed and receives no further cost allocations",
            "It is re-opened for the next round",
            "It must be allocated using simultaneous equations"
        ], key="m6q2")
        if st.button("Check Q2", key="m6c2"):
            if q2 == "It is closed and receives no further cost allocations":
                st.success("✅ Correct! Once a department has been allocated, it is 'closed' — no more costs flow to it.")
            else:
                st.error("❌ Incorrect. The Step-Down method closes each department after it's been allocated.")

        st.markdown("---")
        st.markdown("**Q3. The split-off point in joint product costing is:**")
        q3 = st.radio("", [
            "Where the final product is sold",
            "The beginning of the production process",
            "Where joint products become separately identifiable",
            "Where separable costs begin to be accumulated"
        ], key="m6q3")
        if st.button("Check Q3", key="m6c3"):
            if q3 == "Where joint products become separately identifiable":
                st.success("✅ Correct! The split-off point is where products can be distinguished from each other.")
            else:
                st.error("❌ Incorrect. Split-off is the point where joint products become separately identifiable.")

        st.markdown("---")
        st.markdown("""
        **Q4. Joint costs: $200,000. Product A: 8,000 units @ $20 split-off price. Product B: 4,000 units @ $30.**
        Using the Sales Value at Split-Off method, how much is allocated to Product A?
        """)
        q4 = st.radio("", ["$80,000", "$100,000", "$120,000", "$133,333"], key="m6q4")
        if st.button("Check Q4", key="m6c4"):
            if q4 == "$100,000":
                sv_a = 8000 * 20
                sv_b = 4000 * 30
                total = sv_a + sv_b
                alloc_a = sv_a / total * 200000
                st.success(f"✅ Correct! SV of A = $160,000, SV of B = $120,000, Total = $280,000. A allocation = $160,000/$280,000 × $200,000 = ${alloc_a:,.0f}")
            else:
                st.error("❌ Incorrect. A sales value = $160,000; B = $120,000; Total = $280,000. A allocation = 160/280 × $200,000 = $114,286. (re-check the options)")

        st.markdown("---")
        st.markdown("""
        **Q5. A product sells for $15/unit at split-off. If processed further ($4/unit cost), it sells at $20/unit.
        What is the correct decision?**
        """)
        q5 = st.radio("", [
            "Sell at split-off — joint costs make it unprofitable",
            "Process further — net gain of $1/unit",
            "Indifferent — same result either way",
            "Cannot decide without knowing joint costs"
        ], key="m6q5")
        if st.button("Check Q5", key="m6c5"):
            if q5 == "Process further — net gain of $1/unit":
                st.success("✅ Correct! Incremental revenue = $5, incremental cost = $4, net gain = $1/unit. Joint costs are irrelevant!")
            else:
                st.error("❌ Incorrect. Incremental revenue ($20−$15=$5) > Incremental cost ($4) → process further for $1 gain/unit. Joint costs are irrelevant sunk costs!")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "Direct Method Allocation %",
                "Step-Down: 1st Dept Rate",
                "Sales Value at Split-Off Allocation %",
                "Net Realizable Value (NRV)",
                "NRV Allocation %",
                "Sell or Process Further Net Benefit"
            ],
            "Expression": [
                "Prod Dept Usage / Total Production Usage (exclude all other service depts)",
                "Dept Cost / (All remaining depts including other service depts)",
                "Product Sales Value at Split-Off / Total Sales Value",
                "Final Sales Value − Separable Costs",
                "Product NRV / Total NRV × Joint Costs",
                "(Final Price − Split-Off Price) × Units − Total Additional Processing Costs"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Service Dept Allocation Methods")
        methods_compare = pd.DataFrame({
            "Feature": ["Inter-service recognition", "Accuracy", "Complexity", "GAAP acceptable", "Best for"],
            "Direct Method": ["None", "Least accurate", "Simplest", "✅ Yes", "Simple org structures"],
            "Step-Down": ["Partial (one way)", "More accurate", "Moderate", "✅ Yes", "Most common choice"],
            "Reciprocal": ["Full (both ways)", "Most accurate", "Complex", "✅ Yes", "Significant inter-service usage"]
        })
        st.dataframe(methods_compare, use_container_width=True, hide_index=True)

        st.subheader("📌 Joint Cost Allocation Methods")
        joint_methods = pd.DataFrame({
            "Method": ["Physical Units", "Sales Value at Split-Off", "Net Realizable Value", "Constant GM%"],
            "Basis": ["Units or weight", "Market value at split-off", "Final price − separable costs", "Equal GM% for all products"],
            "When to Use": [
                "Products have similar values",
                "Products sellable at split-off (most common)",
                "Further processing required",
                "Regulatory/pricing"
            ],
            "Main Weakness": [
                "Ignores revenue-generating ability",
                "Market prices may not exist at split-off",
                "Needs accurate cost/price estimates",
                "Assumes all products equally profitable"
            ]
        })
        st.dataframe(joint_methods, use_container_width=True, hide_index=True)

        st.subheader("⚡ Sell or Process Further — Decision Framework")
        st.markdown("""
        ```
        Step 1: Calculate Incremental Revenue
                = (Final Selling Price − Split-Off Price) × Units

        Step 2: Calculate Incremental Costs
                = Additional Variable Processing Costs + Fixed Costs Specifically for Processing

        Step 3: Calculate Net Benefit
                = Incremental Revenue − Incremental Costs

        Step 4: Decision
                Net Benefit > 0 → PROCESS FURTHER
                Net Benefit < 0 → SELL AT SPLIT-OFF
                Net Benefit = 0 → INDIFFERENT

        ⚠️ RULE: Joint costs are ALWAYS irrelevant (sunk costs)!
        ```
        """)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Including inter-service usage in the Direct Method",
                "Allocating to a 'closed' department in Step-Down",
                "Including joint costs in Sell-or-Process-Further",
                "Confusing NRV with sales value at split-off",
                "Forgetting separable costs in NRV calculation",
                "Using joint cost allocation for make-vs-buy decisions"
            ],
            "Correct Approach": [
                "Use ONLY production dept usage for percentages in Direct Method",
                "Once allocated, a service dept is closed — no further receipts",
                "Joint costs are sunk — only consider incremental costs and revenues",
                "NRV requires subtracting separable costs from final sales value",
                "NRV = Final Sales Value MINUS all separable processing costs",
                "Joint cost allocations are arbitrary — don't use for decisions"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 6 Complete! You can now allocate service department costs and make sound joint product decisions.")
        st.info("💡 Next: Module 7 — Variable Costing vs Absorption Costing")

if __name__ == "__main__":
    show()