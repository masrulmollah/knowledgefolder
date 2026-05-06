import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏭 Module 4: Process Costing Systems")
    st.markdown("*Master equivalent units, weighted average, and FIFO methods*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────── TAB 1 LEARN ──────────────────────────────
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. When to Use Process Costing")
        st.markdown("""
        Process costing is used when **identical or homogeneous units** flow continuously through production.

        | Feature | Job Order Costing | Process Costing |
        |---------|------------------|-----------------|
        | Product type | Unique / custom | Identical / mass |
        | Cost tracking | Per job | Per department |
        | Cost document | Job cost sheet | Production cost report |
        | Industries | Construction, printing | Oil refining, food, chemicals |
        """)

        st.subheader("2. Equivalent Units of Production (EUP)")
        st.markdown("""
        Because units at the end of a period are partially complete, we cannot simply add them to completed units.
        We convert partially-done units into **equivalent fully-complete units**.

        ```
        100 units that are 60% complete  =  60 equivalent units
        ```

        #### Two Cost Categories:
        - **Materials** — often added at the **start** of the process (100% at beginning)
        - **Conversion** (Labor + Overhead) — added **throughout** the process

        #### Key Equation:
        ```
        Beginning WIP + Started = Completed + Ending WIP
        ```
        """)

        st.subheader("3. Weighted Average Method")
        st.markdown("""
        Combines **beginning WIP costs** with **current period costs** — treats all units as if started this period.

        #### EUP Calculation:
        ```
        EUP (Materials)   = Units Completed + (Ending WIP × % Complete for Materials)
        EUP (Conversion)  = Units Completed + (Ending WIP × % Complete for Conversion)
        ```

        #### Cost per EUP:
        ```
        Cost per EUP = (Beginning WIP Cost + Current Period Cost) / EUP
        ```

        #### Assign Costs:
        ```
        Cost transferred out = Units completed × Cost per EUP (total)
        Ending WIP cost      = EUP (mat) × Cost/EUP(mat) + EUP (conv) × Cost/EUP(conv)
        ```
        """)

        st.subheader("4. FIFO Method")
        st.markdown("""
        Keeps **beginning WIP costs separate** from current period costs. More accurate for performance evaluation.

        #### EUP Calculation:
        ```
        EUP = (Beg WIP × % still needed to complete)
              + Units started AND completed this period
              + (Ending WIP × % complete)
        ```

        #### Cost per EUP (current period costs ONLY):
        ```
        Cost per EUP = Current Period Cost / Current Period EUP
        ```

        #### Cost of Transferred Out:
        ```
        = Prior period cost in Beg WIP
          + Cost to complete Beg WIP (current period EUP × Cost per EUP)
          + Cost of units started & completed (Units S&C × Total Cost per EUP)
        ```
        """)

        st.subheader("5. Production Cost Report — 5 Steps")
        st.markdown("""
        | Step | Task |
        |------|------|
        | 1 | Summarize physical flow of units |
        | 2 | Calculate equivalent units of production |
        | 3 | Calculate cost per equivalent unit |
        | 4 | Assign costs to units transferred out |
        | 5 | Assign costs to ending WIP |
        | ✔️ | Reconcile: Step 4 + Step 5 = Total costs available |
        """)

        st.subheader("6. Transferred-In Costs (Multiple Departments)")
        st.markdown("""
        When products move from Department 1 → Department 2:
        - Department 2 receives **transferred-in costs** from Dept 1
        - Treat as a **third cost category** (100% complete for transferred-in)
        - Three pools: Transferred-in, Materials, Conversion

        ```
        Dept 2 Cost per Unit = Transferred-in cost + Dept 2 Materials + Dept 2 Conversion
        ```
        """)

    # ─────────────────────────────── TAB 2 EXAMPLES ───────────────────────────
    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1 — Weighted Average Method")
        st.markdown("""
        **Given:**
        - Beginning WIP: 2,000 units — 100% materials, 60% conversion
        - Started this period: 10,000 units
        - Completed & transferred: 9,000 units
        - Ending WIP: 3,000 units — 100% materials, 40% conversion
        - Beg WIP Costs: Materials $4,000 | Conversion $2,400
        - Current Period Costs: Materials $20,000 | Conversion $18,600
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Step 1 — Physical Flow:**
            ```
            Beg WIP           2,000
            + Started        10,000
            ───────────────────────
            Total             12,000

            Completed out      9,000
            + Ending WIP       3,000
            ───────────────────────
            Total             12,000  ✓
            ```
            """)
        with col2:
            st.markdown("""
            **Step 2 — EUP (Weighted Average):**
            ```
                          Materials  Conversion
            Completed       9,000      9,000
            End WIP×%
              3,000×100%    3,000
              3,000×40%                1,200
            ─────────────────────────────────
            EUP            12,000     10,200
            ```
            """)

        st.markdown("""
        **Step 3 — Cost per EUP:**
        ```
                      Materials   Conversion    Total
        Beg WIP cost   $4,000      $2,400      $6,400
        + Current     $20,000     $18,600     $38,600
        ─────────────────────────────────────────────
        Total         $24,000     $21,000     $45,000

        ÷ EUP          12,000      10,200
        ─────────────────────────────────────────────
        Cost/EUP        $2.00      $2.059      $4.059
        ```

        **Step 4 — Transferred Out:**
        ```
        9,000 units × $4.059 = $36,531
        ```

        **Step 5 — Ending WIP:**
        ```
        Materials:   3,000 × $2.000 = $6,000
        Conversion:  1,200 × $2.059 = $2,471
        Total Ending WIP              $8,471
        ```

        **Reconciliation:**
        ```
        Transferred out   $36,531
        + Ending WIP       $8,471
        ─────────────────────────
        Total             $45,002  ≈ $45,000  ✓ (rounding)
        ```
        """)

        st.subheader("Example 2 — FIFO Method (Same Data)")
        st.markdown("""
        **Step 2 — EUP (FIFO):**
        ```
                                   Materials   Conversion
        Complete Beg WIP:
          2,000 × 0%                    0
          2,000 × 40%                              800

        Started & Completed:
          7,000 × 100%              7,000        7,000

        Ending WIP:
          3,000 × 100%              3,000
          3,000 × 40%                            1,200
        ─────────────────────────────────────────────────
        EUP                        10,000        9,000
        ```

        **Step 3 — Cost per EUP (current period ONLY):**
        ```
        Materials:  $20,000 / 10,000 = $2.000
        Conversion: $18,600 /  9,000 = $2.067
        ```

        **Step 4 — Transferred Out:**
        ```
        Beg WIP prior costs:                    $6,400
        + To complete Beg WIP: 800 × $2.067     $1,654
        + Started & Completed: 7,000 × $4.067  $28,469
        ──────────────────────────────────────────────
        Total Transferred Out:                 $36,523
        ```
        """)

    # ────────────────────────── TAB 3 CALCULATORS ─────────────────────────────
    with tab3:
        st.header("Interactive Calculators")

        method = st.radio("🔢 Select Method", ["Weighted Average", "FIFO"], horizontal=True)
        st.markdown("---")

        st.subheader("📥 Enter Process Data")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Unit Information:**")
            beg_wip = st.number_input("Beginning WIP (units)", min_value=0, value=2000, step=100)
            beg_mat_pct = st.number_input("Beg WIP — Materials % Complete", 0.0, 100.0, 100.0, step=5.0)
            beg_conv_pct = st.number_input("Beg WIP — Conversion % Complete", 0.0, 100.0, 60.0, step=5.0)
            started = st.number_input("Units Started This Period", min_value=0, value=10000, step=100)

        with col2:
            st.markdown("**Completion Data:**")
            completed = st.number_input("Units Completed & Transferred Out", min_value=0, value=9000, step=100)
            end_mat_pct = st.number_input("Ending WIP — Materials % Complete", 0.0, 100.0, 100.0, step=5.0)
            end_conv_pct = st.number_input("Ending WIP — Conversion % Complete", 0.0, 100.0, 40.0, step=5.0)

        ending_wip = beg_wip + started - completed
        st.info(f"📦 **Calculated Ending WIP:** {ending_wip:,} units  |  Check: {beg_wip:,} + {started:,} − {completed:,} = {ending_wip:,}")

        st.markdown("**Cost Information:**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("*Beginning WIP Costs:*")
            beg_mat_cost = st.number_input("Beg WIP — Materials ($)", 0.0, value=4000.0, step=100.0)
            beg_conv_cost = st.number_input("Beg WIP — Conversion ($)", 0.0, value=2400.0, step=100.0)
        with col2:
            st.markdown("*Current Period Costs:*")
            curr_mat_cost = st.number_input("Current — Materials ($)", 0.0, value=20000.0, step=100.0)
            curr_conv_cost = st.number_input("Current — Conversion ($)", 0.0, value=18600.0, step=100.0)

        if st.button("🧮 Calculate Production Cost Report", type="primary"):
            st.markdown("---")
            st.subheader(f"📋 Production Cost Report — {method}")

            # ── WEIGHTED AVERAGE ──────────────────────────────────────────────
            if method == "Weighted Average":
                eup_mat = completed + (ending_wip * end_mat_pct / 100)
                eup_conv = completed + (ending_wip * end_conv_pct / 100)

                total_mat = beg_mat_cost + curr_mat_cost
                total_conv = beg_conv_cost + curr_conv_cost

                cpu_mat = total_mat / eup_mat if eup_mat > 0 else 0
                cpu_conv = total_conv / eup_conv if eup_conv > 0 else 0
                cpu_total = cpu_mat + cpu_conv

                transferred_cost = completed * cpu_total

                end_mat_eup = ending_wip * end_mat_pct / 100
                end_conv_eup = ending_wip * end_conv_pct / 100
                ending_wip_cost = (end_mat_eup * cpu_mat) + (end_conv_eup * cpu_conv)

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Step 2 — Equivalent Units:**")
                    eup_df = pd.DataFrame({
                        "Component": ["Units Completed", f"End WIP ({end_mat_pct:.0f}%)", "Total EUP"],
                        "Materials": [f"{completed:,}", f"{end_mat_eup:,.0f}", f"{eup_mat:,.0f}"],
                        "Conversion": [f"{completed:,}", f"{end_conv_eup:,.0f}", f"{eup_conv:,.0f}"]
                    })
                    st.dataframe(eup_df, use_container_width=True, hide_index=True)

                with col2:
                    st.markdown("**Step 3 — Cost per EUP:**")
                    cpu_df = pd.DataFrame({
                        "Item": ["Beg WIP Cost", "Current Cost", "Total", "÷ EUP", "Cost per EUP"],
                        "Materials": [f"${beg_mat_cost:,.2f}", f"${curr_mat_cost:,.2f}", f"${total_mat:,.2f}", f"{eup_mat:,.0f}", f"${cpu_mat:.4f}"],
                        "Conversion": [f"${beg_conv_cost:,.2f}", f"${curr_conv_cost:,.2f}", f"${total_conv:,.2f}", f"{eup_conv:,.0f}", f"${cpu_conv:.4f}"]
                    })
                    st.dataframe(cpu_df, use_container_width=True, hide_index=True)

                st.markdown("**Steps 4 & 5 — Cost Assignment:**")
                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Transferred Out", f"${transferred_cost:,.2f}")
                with col2: st.metric("Ending WIP", f"${ending_wip_cost:,.2f}")
                with col3:
                    total_assigned = transferred_cost + ending_wip_cost
                    total_available = total_mat + total_conv
                    diff = abs(total_assigned - total_available)
                    st.metric("Total Assigned", f"${total_assigned:,.2f}")

                if diff < 1.0:
                    st.success(f"✅ Reconciliation: Costs Assigned (${total_assigned:,.2f}) = Costs Available (${total_available:,.2f})")
                else:
                    st.warning(f"⚠️ Rounding difference: ${diff:.2f}")

            # ── FIFO ─────────────────────────────────────────────────────────
            else:
                started_completed = completed - beg_wip
                if started_completed < 0:
                    st.error("❌ Completed units cannot be less than beginning WIP. Check inputs.")
                else:
                    # EUP FIFO
                    eup_mat_beg = beg_wip * (1 - beg_mat_pct / 100)
                    eup_conv_beg = beg_wip * (1 - beg_conv_pct / 100)
                    eup_mat_sc = started_completed
                    eup_conv_sc = started_completed
                    eup_mat_end = ending_wip * end_mat_pct / 100
                    eup_conv_end = ending_wip * end_conv_pct / 100

                    eup_mat = eup_mat_beg + eup_mat_sc + eup_mat_end
                    eup_conv = eup_conv_beg + eup_conv_sc + eup_conv_end

                    cpu_mat = curr_mat_cost / eup_mat if eup_mat > 0 else 0
                    cpu_conv = curr_conv_cost / eup_conv if eup_conv > 0 else 0
                    cpu_total = cpu_mat + cpu_conv

                    # Cost assignment
                    beg_wip_prior = beg_mat_cost + beg_conv_cost
                    cost_complete_beg = (eup_conv_beg * cpu_conv) + (eup_mat_beg * cpu_mat)
                    cost_sc = started_completed * cpu_total
                    transferred_cost = beg_wip_prior + cost_complete_beg + cost_sc
                    ending_wip_cost = (eup_mat_end * cpu_mat) + (eup_conv_end * cpu_conv)

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Step 2 — EUP (FIFO):**")
                        eup_df = pd.DataFrame({
                            "Component": ["Complete Beg WIP", "Started & Completed", "Ending WIP", "Total EUP"],
                            "Materials": [f"{eup_mat_beg:,.0f}", f"{eup_mat_sc:,.0f}", f"{eup_mat_end:,.0f}", f"{eup_mat:,.0f}"],
                            "Conversion": [f"{eup_conv_beg:,.0f}", f"{eup_conv_sc:,.0f}", f"{eup_conv_end:,.0f}", f"{eup_conv:,.0f}"]
                        })
                        st.dataframe(eup_df, use_container_width=True, hide_index=True)

                    with col2:
                        st.markdown("**Step 3 — Cost per EUP (current only):**")
                        cpu_df = pd.DataFrame({
                            "Item": ["Current Cost", "÷ EUP", "Cost per EUP"],
                            "Materials": [f"${curr_mat_cost:,.2f}", f"{eup_mat:,.0f}", f"${cpu_mat:.4f}"],
                            "Conversion": [f"${curr_conv_cost:,.2f}", f"{eup_conv:,.0f}", f"${cpu_conv:.4f}"]
                        })
                        st.dataframe(cpu_df, use_container_width=True, hide_index=True)

                    st.markdown("**Steps 4 & 5 — Cost Assignment (FIFO):**")
                    assign_df = pd.DataFrame({
                        "Item": ["Prior period cost in Beg WIP", "Cost to complete Beg WIP", "Started & Completed", "Total Transferred Out", "Ending WIP"],
                        "Amount": [f"${beg_wip_prior:,.2f}", f"${cost_complete_beg:,.2f}", f"${cost_sc:,.2f}", f"${transferred_cost:,.2f}", f"${ending_wip_cost:,.2f}"]
                    })
                    st.dataframe(assign_df, use_container_width=True, hide_index=True)

                    total_available = beg_mat_cost + beg_conv_cost + curr_mat_cost + curr_conv_cost
                    total_assigned = transferred_cost + ending_wip_cost
                    diff = abs(total_assigned - total_available)
                    if diff < 1.0:
                        st.success(f"✅ Reconciliation: Assigned (${total_assigned:,.2f}) = Available (${total_available:,.2f})")
                    else:
                        st.warning(f"⚠️ Rounding difference: ${diff:.2f}")

    # ─────────────────────────────── TAB 4 VISUALS ────────────────────────────
    with tab4:
        st.header("Visual Analytics")

        st.subheader("Cost Flow Through Departments")
        fig_sankey = go.Figure(data=[go.Sankey(
            node=dict(
                pad=20, thickness=25,
                label=["Raw Materials", "Dept 1\nMixing", "Dept 2\nProcessing", "Dept 3\nFinishing", "Finished Goods", "COGS"],
                color=["#AED6F1", "#2E86C1", "#1A5276", "#0E3460", "#27AE60", "#E74C3C"]
            ),
            link=dict(
                source=[0, 1, 2, 3, 4],
                target=[1, 2, 3, 4, 5],
                value=[100, 120, 140, 160, 155],
                color=["rgba(46,134,193,0.4)"] * 5
            )
        )])
        fig_sankey.update_layout(title="Cost Flow Through Production Departments", height=400)
        st.plotly_chart(fig_sankey, use_container_width=True)

        st.subheader("Weighted Average vs FIFO — EUP Comparison")
        wa_eup = [12000, 10200]
        fifo_eup = [10000, 9000]
        labels = ["Materials EUP", "Conversion EUP"]
        fig_eup = go.Figure(data=[
            go.Bar(name="Weighted Average", x=labels, y=wa_eup, marker_color="#2E86C1"),
            go.Bar(name="FIFO", x=labels, y=fifo_eup, marker_color="#E67E22")
        ])
        fig_eup.update_layout(title="EUP Comparison: Weighted Average vs FIFO", barmode="group", yaxis_title="Equivalent Units")
        st.plotly_chart(fig_eup, use_container_width=True)

        st.subheader("Cost per EUP — Materials vs Conversion")
        cost_categories = ["Materials", "Conversion"]
        wa_cpu = [2.00, 2.059]
        fig_cpu = go.Figure(data=[
            go.Bar(name="Cost per EUP (WA)", x=cost_categories, y=wa_cpu,
                   marker_color=["#3498DB", "#E74C3C"],
                   text=[f"${v:.3f}" for v in wa_cpu], textposition="auto")
        ])
        fig_cpu.update_layout(title="Cost per Equivalent Unit Breakdown", yaxis_title="Cost per EUP ($)")
        st.plotly_chart(fig_cpu, use_container_width=True)

        st.subheader("Cost Assignment Summary")
        assignment = pd.DataFrame({"Category": ["Transferred Out", "Ending WIP"], "Amount": [36531, 8471]})
        fig_pie = px.pie(assignment, values="Amount", names="Category",
                         title="Cost Assignment Split", color_discrete_sequence=["#27AE60", "#2E86C1"])
        st.plotly_chart(fig_pie, use_container_width=True)

    # ─────────────────────────────── TAB 5 QUIZ ───────────────────────────────
    with tab5:
        st.header("🧠 Knowledge Check Quiz")

        st.markdown("**Q1. Process costing is best suited for:**")
        q1 = st.radio("", ["Custom furniture", "Oil refining", "Aircraft manufacturing", "Wedding photography"], key="m4q1")
        if st.button("Check Q1", key="m4c1"):
            st.success("✅ Correct! Oil refining produces homogeneous units in a continuous process.") if q1 == "Oil refining" else st.error("❌ Incorrect. Process costing is for mass production of identical units.")

        st.markdown("---")
        st.markdown("**Q2. If 500 units are 60% complete for conversion, their EUP for conversion is:**")
        q2 = st.radio("", ["500", "300", "200", "60"], key="m4q2")
        if st.button("Check Q2", key="m4c2"):
            st.success("✅ Correct! 500 × 60% = 300 EUP.") if q2 == "300" else st.error("❌ Incorrect. EUP = 500 × 60% = 300.")

        st.markdown("---")
        st.markdown("**Q3. Under FIFO, the cost per EUP is based on:**")
        q3 = st.radio("", ["All costs (prior + current)", "Current period costs only", "Prior period costs only", "Average of all periods"], key="m4q3")
        if st.button("Check Q3", key="m4c3"):
            st.success("✅ Correct! FIFO uses only current period costs to calculate cost per EUP.") if q3 == "Current period costs only" else st.error("❌ Incorrect. FIFO uses current period costs only.")

        st.markdown("---")
        st.markdown("**Q4. Beginning WIP = 1,000 units; Started = 8,000; Completed = 7,500. Ending WIP = ?**")
        q4 = st.radio("", ["500", "1,000", "1,500", "7,500"], key="m4q4")
        if st.button("Check Q4", key="m4c4"):
            st.success("✅ Correct! 1,000 + 8,000 − 7,500 = 1,500.") if q4 == "1,500" else st.error("❌ Incorrect. 1,000 + 8,000 − 7,500 = 1,500 units.")

        st.markdown("---")
        st.markdown("**Q5. Weighted average vs FIFO — the main difference is:**")
        q5 = st.radio("", [
            "FIFO is simpler", "WA mixes prior and current costs; FIFO keeps them separate",
            "FIFO gives lower income", "WA is more accurate"
        ], key="m4q5")
        if st.button("Check Q5", key="m4c5"):
            st.success("✅ Correct! WA blends all costs; FIFO isolates current period costs.") if q5 == "WA mixes prior and current costs; FIFO keeps them separate" else st.error("❌ Incorrect. WA blends all costs together; FIFO separates them.")

    # ─────────────────────────────── TAB 6 SUMMARY ────────────────────────────
    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Formulas")
        formulas = pd.DataFrame({
            "Formula": [
                "Physical Flow Check",
                "EUP (Weighted Avg) — Conv",
                "EUP (FIFO) — Conv",
                "Cost per EUP (WA)",
                "Cost per EUP (FIFO)",
                "Transferred Out (WA)",
                "Ending WIP Cost",
                "Reconciliation Check"
            ],
            "Expression": [
                "Beg WIP + Started = Completed + Ending WIP",
                "Completed + (End WIP × % Complete)",
                "Beg WIP×(1−% done) + S&C + End WIP×%",
                "(Beg Cost + Current Cost) / EUP",
                "Current Period Cost / Current EUP",
                "Units Completed × Total Cost per EUP",
                "End EUP(mat) × CPU(mat) + End EUP(conv) × CPU(conv)",
                "Transferred Out + End WIP = Total Available Costs"
            ]
        })
        st.dataframe(formulas, use_container_width=True, hide_index=True)

        st.subheader("🔍 Weighted Average vs FIFO")
        compare_df = pd.DataFrame({
            "Feature": ["Simplicity", "Costs used", "EUP (Beg WIP)", "Best for", "Accuracy"],
            "Weighted Average": ["Simpler ✅", "Prior + Current blended", "Included in completed", "Stable costs", "Lower"],
            "FIFO": ["More complex", "Current period only", "Separated out", "Changing costs", "Higher ✅"]
        })
        st.dataframe(compare_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Step-by-Step Production Cost Report")
        st.markdown("""
        ```
        Step 1 ── Physical Flow
               Beg WIP + Started = Completed + Ending WIP

        Step 2 ── Equivalent Units
               Materials EUP  = Completed + (End WIP × mat%)
               Conversion EUP = Completed + (End WIP × conv%)

        Step 3 ── Cost per Equivalent Unit
               Total Cost (WA) or Current Cost (FIFO) ÷ EUP

        Step 4 ── Assign cost to Transferred Out
               Completed units × Total CPU

        Step 5 ── Assign cost to Ending WIP
               End EUP(mat) × CPU(mat) + End EUP(conv) × CPU(conv)

        ✅ Check: Step 4 + Step 5 = Total Costs Available
        ```
        """)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes = pd.DataFrame({
            "Mistake": [
                "Using physical units instead of EUP",
                "Forgetting materials timing (start vs end)",
                "Using total costs for FIFO CPU",
                "Not reconciling final costs",
                "Mixing WA and FIFO in one problem"
            ],
            "Correct Approach": [
                "Always convert partially-done units to EUP first",
                "Check when materials are added — affects ending WIP EUP",
                "FIFO uses current period costs ONLY",
                "Always verify: Transferred + Ending WIP = Total Available",
                "Pick one method and use it consistently throughout"
            ]
        })
        st.dataframe(mistakes, use_container_width=True, hide_index=True)

        st.success("🎓 Module 4 Complete! You can now prepare production cost reports using both the weighted average and FIFO methods.")
        st.info("💡 Next: Module 5 — Activity-Based Costing and Management")

if __name__ == "__main__":
    show()