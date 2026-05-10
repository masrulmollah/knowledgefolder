import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏆 Module 14: Quality Management & Lean Accounting")
    st.markdown("*Master quality cost systems, TQM, Six Sigma, Lean, and modern cost management*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Cost of Quality (COQ) Framework")
        st.markdown("""
        **Cost of Quality** encompasses ALL costs associated with achieving and maintaining product/service quality.

        There are **four categories** of quality costs:

        #### Category 1: Prevention Costs
        - Costs incurred to PREVENT defects from occurring
        - Most valuable investment — prevents problems before they happen
        - **Examples:**
          - Quality training programs
          - Quality engineering & planning
          - Statistical process control
          - Supplier evaluation and certification
          - Process improvement projects
          - Design reviews

        #### Category 2: Appraisal Costs
        - Costs to DETECT defects through inspection and testing
        - Catching problems before they reach the customer
        - **Examples:**
          - Incoming materials inspection
          - In-process inspection
          - Final product inspection and testing
          - Quality audits
          - Calibration of test equipment
          - Test equipment depreciation

        #### Category 3: Internal Failure Costs
        - Costs from defects discovered BEFORE delivery to customer
        - Problems caught internally but still costly
        - **Examples:**
          - Scrap materials and labor
          - Rework and repair
          - Re-inspection after rework
          - Downtime due to quality problems
          - Yield losses
          - Process failure analysis

        #### Category 4: External Failure Costs
        - Costs from defects discovered AFTER delivery to customer
        - Most damaging — affects customer relationships and brand
        - **Examples:**
          - Warranty claims and repairs
          - Product recalls
          - Customer complaint handling
          - Lost future sales (lost goodwill)
          - Legal liability costs
          - Product returns and replacements
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### COQ Classification:
            ```
            CONFORMANCE COSTS (to make it right):
            ├── Prevention Costs
            └── Appraisal Costs

            NON-CONFORMANCE COSTS (because it went wrong):
            ├── Internal Failure Costs
            └── External Failure Costs
            ```
            """)
        with col2:
            st.markdown("""
            #### Optimal Quality Level:
            ```
            The optimal quality investment point is where:

            Marginal Prevention Cost
            = Marginal Failure Cost Saved

            As prevention ↑:
            - Failure costs ↓ dramatically
            - Total COQ initially ↓ then ↑
            ```
            """)

        st.subheader("2. Total Quality Management (TQM)")
        st.markdown("""
        **TQM** is a management philosophy focused on continuous quality improvement throughout the entire organization.

        #### TQM Principles:
        | Principle | Description |
        |-----------|-------------|
        | **Customer Focus** | Quality defined by customer expectations |
        | **Total Involvement** | Every employee responsible for quality |
        | **Continuous Improvement** | Never-ending process of getting better |
        | **Process Orientation** | Improve processes, not just outcomes |
        | **Integrated System** | Quality embedded in all functions |
        | **Strategic Planning** | Quality is a strategic priority |
        | **Decision by Facts** | Data-driven decision making |

        #### TQM vs Traditional Approach:
        | Traditional | TQM |
        |-------------|-----|
        | Quality is inspection | Quality is prevention |
        | Defects are inevitable | Zero defects is the goal |
        | Quality costs money | Quality saves money |
        | Quality dept responsible | Everyone responsible |
        | Product focus | Process focus |
        """)

        st.subheader("3. Six Sigma")
        st.markdown("""
        **Six Sigma** = A rigorous, data-driven methodology for achieving near-perfect quality.

        #### The Statistical Meaning:
        ```
        Sigma (σ) = Standard deviation
        Six Sigma = 3.4 defects per MILLION opportunities
        3-Sigma   = 66,807 defects per million (common)
        6-Sigma   = 3.4 defects per million (world-class)
        ```

        #### The DMAIC Process:
        | Phase | Actions |
        |-------|---------|
        | **D**efine | Define problem, customer requirements, project scope |
        | **M**easure | Measure current process performance and collect data |
        | **A**nalyze | Analyze data to identify root causes of defects |
        | **I**mprove | Implement solutions to address root causes |
        | **C**ontrol | Control improved process to sustain gains |

        #### Six Sigma Roles:
        - **Champion**: Executive sponsor providing resources
        - **Master Black Belt**: Six Sigma expert and trainer
        - **Black Belt**: Dedicated project leader
        - **Green Belt**: Part-time project contributor
        - **Yellow Belt**: Team member with basic training
        """)

        st.subheader("4. Just-In-Time (JIT) Production")
        st.markdown("""
        **JIT** = Produce only what is needed, when it is needed, in the amount needed.

        #### JIT Goals:
        - **Zero inventory** (eliminate all forms of waste)
        - **Zero defects** (quality built in, not inspected in)
        - **Zero setup time** (eliminate changeover delays)
        - **Zero breakdowns** (preventive maintenance)
        - **Zero lead time** (immediate response to demand)

        #### Pull vs Push Systems:
        ```
        Traditional (PUSH):
        Production forecast → Make products → Push to inventory → Customer buys

        JIT (PULL):
        Customer orders → Pull from assembly → Pull materials → Produce only what's needed
        ```

        #### JIT Benefits:
        - Reduced inventory carrying costs
        - Improved quality (problems visible immediately)
        - Faster throughput
        - Less waste
        - More flexible production
        """)

        st.subheader("5. Lean Manufacturing & Lean Accounting")
        st.markdown("""
        **Lean** = A system for eliminating waste (muda) from all processes.

        #### The 8 Wastes (TIMWOODS):
        | Waste | Description | Example |
        |-------|-------------|---------|
        | **T**ransportation | Moving items unnecessarily | Moving parts between distant workstations |
        | **I**nventory | Excess stock beyond immediate needs | Large raw material stockpiles |
        | **M**otion | Unnecessary movement of people | Workers walking long distances |
        | **W**aiting | Idle time between processes | Machines waiting for materials |
        | **O**verproduction | Producing more than needed | Making to forecast, not orders |
        | **O**verprocessing | More work than customer requires | Extra features nobody wants |
        | **D**efects | Rework, scrap, returns | Defective products requiring rework |
        | **S**kills | Underutilizing people's talents | Experts doing routine tasks |

        #### Lean Accounting:
        Traditional accounting doesn't work well for lean environments. Lean accounting uses:
        - **Value stream costing** instead of product costing
        - **Visual management** with visual scorecards
        - **Plain language** financial statements
        - **Box scores** for value stream performance
        - **Eliminate standard costing variances** (often mislead in lean)
        """)

        st.subheader("6. Backflush Costing")
        st.markdown("""
        **Backflush costing** is a simplified costing approach used in JIT environments.

        **Traditional costing** traces costs through each production stage sequentially.
        **Backflush costing** delays cost assignment until production is completed (or even sold).

        ```
        Traditional:    Raw Mat → WIP Stage 1 → WIP Stage 2 → Finished Goods → COGS
        Backflush:      Costs accumulated → "Flushed" back to products when completed/sold

        Three trigger points commonly used:
        1. Purchase of raw materials AND completion of goods
        2. Completion of goods (skip raw materials stage)
        3. Sale of goods (most extreme backflush)
        ```

        **Suitable when:**
        - Low inventory levels (JIT environment)
        - Short production cycle times
        - Stable, consistent production processes
        - Strong actual-to-standard cost alignment
        """)

        st.subheader("7. Value Stream Costing")
        st.markdown("""
        **Value Stream** = All activities required to bring a product from raw material to customer.

        **Value Stream Costing vs Traditional:**
        ```
        Traditional Product Costing:
        - Assign all costs to individual products
        - Uses complex allocations
        - Focuses on inventory valuation
        - Drives overproduction (absorb fixed OH)

        Value Stream Costing:
        - Costs assigned to value streams, not products
        - All costs within value stream are period costs
        - Focuses on cash flow and customer value
        - Simple and visible
        - Encourages flow and pull
        ```

        **Box Score Format:**
        | Metric | Current State | Future State | Target |
        |--------|--------------|--------------|--------|
        | Operational metrics | | | |
        | Capacity metrics | | | |
        | Financial metrics | | | |
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Cost of Quality Report")
        st.markdown("""
        **Annual Sales: $10,000,000. Quality Costs:**

        | Category | Activity | Cost |
        |----------|---------|------|
        | Prevention | Quality training | $50,000 |
        | Prevention | Process improvement | $80,000 |
        | Prevention | Supplier certification | $30,000 |
        | Appraisal | Incoming inspection | $60,000 |
        | Appraisal | In-process testing | $90,000 |
        | Appraisal | Final inspection | $40,000 |
        | Internal Failure | Scrap | $120,000 |
        | Internal Failure | Rework | $150,000 |
        | External Failure | Warranty costs | $200,000 |
        | External Failure | Customer returns | $80,000 |

        **Summary Analysis:**
        ```
        Prevention Costs:      $160,000  (1.6% of sales)
        Appraisal Costs:       $190,000  (1.9% of sales)
        Internal Failure:      $270,000  (2.7% of sales)
        External Failure:      $280,000  (2.8% of sales)
        ────────────────────────────────────────────────
        Total COQ:             $900,000  (9.0% of sales)

        Conformance Costs:     $350,000  (38.9% of COQ)
        Non-conformance Costs: $550,000  (61.1% of COQ)
        ```

        **Insight:** Non-conformance costs ($550K) far exceed conformance costs ($350K).
        Investing more in prevention ($160K → higher) could dramatically reduce failure costs ($550K).
        A $50K increase in prevention could potentially save $200K+ in failures!
        """)

        st.subheader("Example 2: Six Sigma DMAIC Project")
        st.markdown("""
        **Problem: Customer complaint rate is 5% — too high. Target: < 1%.**

        **Define Phase:**
        ```
        Problem:     5% of delivered orders have quality issues
        Customer:    Commercial clients expecting < 1% defect rate
        Scope:       Order fulfillment process from picking to delivery
        Goal:        Reduce defects from 5% to < 1% in 6 months
        ```

        **Measure Phase:**
        ```
        Current Sigma Level:
        DPMO = (Defects / Opportunities) × 1,000,000
             = (500 / 10,000) × 1,000,000
             = 50,000 DPMO
             ≈ 3.1 Sigma

        Target: < 1% = 10,000 DPMO = 3.8 Sigma
        Stretch Target: 3.4 DPMO = 6 Sigma
        ```

        **Analyze Phase (Root Causes identified):**
        ```
        Fishbone Analysis:
        - Wrong items picked (40% of defects) ← Most impactful
        - Damaged in packing (25%)
        - Incorrect quantities (20%)
        - Wrong shipping address (15%)
        ```

        **Improve Phase:**
        ```
        - Implement barcode scanning at picking (addresses 40%)
        - Add packing checklist and cushioning protocols (25%)
        - Automate quantity verification (20%)
        - Address verification software (15%)
        ```

        **Control Phase:**
        ```
        - SPC charts for ongoing monitoring
        - Weekly defect rate reporting
        - Monthly Six Sigma review
        - Result: Defect rate reduced to 0.8% (< 1% target ✅)
        ```
        """)

        st.subheader("Example 3: Lean Value Stream Analysis")
        st.markdown("""
        **Production Process: Customer order to delivery.**

        **Current State Value Stream Map:**
        ```
        Process Step    | Time      | Value-Added? | Waste Type
        ─────────────────────────────────────────────────────
        Receive order   | 2 hours   | ✅ Yes        | —
        Wait for batch  | 3 days    | ❌ No         | Waiting
        Material pickup | 30 min    | ❌ No         | Transportation
        Setup machine   | 4 hours   | ❌ No         | Waiting/Motion
        Machining       | 2 hours   | ✅ Yes        | —
        Inspection      | 1 hour    | ❌ Partial    | Overprocessing
        Wait for QC     | 1 day     | ❌ No         | Waiting
        Pack & ship     | 30 min    | ✅ Yes        | —
        ─────────────────────────────────────────────────────
        Total Lead Time: ~5 days | Value-Added: ~4.5 hrs
        Process Efficiency: 4.5 hrs / 40 hrs = 11.25% (very poor!)
        ```

        **Future State Targets (after Lean):**
        ```
        Eliminate batch waiting: 3 days → 2 hours (JIT pull)
        Reduce setup time: 4 hours → 30 min (SMED)
        Eliminate wait for QC: 1 day → integrated process
        ─────────────────────────────────────────────────────
        New Lead Time: ~1 day (from ~5 days)
        Value-Added %: 4.5/9 hrs = 50% (significant improvement!)
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Calculator:", [
            "📊 Cost of Quality Report Builder",
            "🎯 Six Sigma DPMO Calculator",
            "🔍 Waste Identification Tool",
            "📈 Quality Improvement ROI",
            "🔄 Value Stream Analysis",
            "⚙️ Lean Metrics Dashboard"
        ])

        if calc_choice == "📊 Cost of Quality Report Builder":
            st.subheader("Cost of Quality (COQ) Report Builder")

            annual_sales = st.number_input("Annual Sales Revenue ($)", 0.0, value=10000000.0, step=100000.0)
            st.markdown("---")
            st.markdown("### Enter Quality Costs by Category:")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**🛡️ PREVENTION COSTS:**")
                prev_costs = {}
                default_prev = {"Quality Training": 50000, "Process Improvement": 80000,
                                "Supplier Certification": 30000, "Design Reviews": 20000}
                for item, default in default_prev.items():
                    prev_costs[item] = st.number_input(item, 0.0, value=float(default), step=1000.0, key=f"prev_{item}")

                st.markdown("**🔍 APPRAISAL COSTS:**")
                appr_costs = {}
                default_appr = {"Incoming Inspection": 60000, "In-Process Testing": 90000,
                                "Final Inspection": 40000, "Quality Audits": 25000}
                for item, default in default_appr.items():
                    appr_costs[item] = st.number_input(item, 0.0, value=float(default), step=1000.0, key=f"appr_{item}")

            with col2:
                st.markdown("**⚠️ INTERNAL FAILURE COSTS:**")
                int_fail_costs = {}
                default_int = {"Scrap": 120000, "Rework": 150000,
                               "Re-inspection": 30000, "Process Downtime": 50000}
                for item, default in default_int.items():
                    int_fail_costs[item] = st.number_input(item, 0.0, value=float(default), step=1000.0, key=f"int_{item}")

                st.markdown("**❌ EXTERNAL FAILURE COSTS:**")
                ext_fail_costs = {}
                default_ext = {"Warranty Claims": 200000, "Customer Returns": 80000,
                               "Complaint Handling": 40000, "Lost Goodwill": 100000}
                for item, default in default_ext.items():
                    ext_fail_costs[item] = st.number_input(item, 0.0, value=float(default), step=1000.0, key=f"ext_{item}")

            if st.button("🧮 Generate COQ Report", type="primary"):
                total_prev = sum(prev_costs.values())
                total_appr = sum(appr_costs.values())
                total_int = sum(int_fail_costs.values())
                total_ext = sum(ext_fail_costs.values())
                total_coq = total_prev + total_appr + total_int + total_ext
                total_conform = total_prev + total_appr
                total_nonconform = total_int + total_ext

                st.markdown("---")
                st.markdown("### 📋 Cost of Quality Report:")

                coq_summary = pd.DataFrame({
                    "Category": ["Prevention Costs", "Appraisal Costs",
                                  "Internal Failure Costs", "External Failure Costs", "TOTAL COQ"],
                    "Amount": [f"${total_prev:,.2f}", f"${total_appr:,.2f}",
                                f"${total_int:,.2f}", f"${total_ext:,.2f}", f"${total_coq:,.2f}"],
                    "% of Sales": [f"{total_prev/annual_sales*100:.2f}%", f"{total_appr/annual_sales*100:.2f}%",
                                    f"{total_int/annual_sales*100:.2f}%", f"{total_ext/annual_sales*100:.2f}%",
                                    f"{total_coq/annual_sales*100:.2f}%"],
                    "% of COQ": [f"{total_prev/total_coq*100:.1f}%", f"{total_appr/total_coq*100:.1f}%",
                                  f"{total_int/total_coq*100:.1f}%", f"{total_ext/total_coq*100:.1f}%", "100.0%"]
                })
                st.dataframe(coq_summary, use_container_width=True, hide_index=True)

                col1, col2, col3, col4 = st.columns(4)
                with col1: st.metric("Conformance Costs", f"${total_conform:,.2f}")
                with col2: st.metric("Non-conformance Costs", f"${total_nonconform:,.2f}")
                with col3: st.metric("Total COQ", f"${total_coq:,.2f}")
                with col4: st.metric("COQ as % of Sales", f"{total_coq/annual_sales*100:.2f}%")

                st.markdown("### Management Insights:")
                if total_nonconform > total_conform:
                    st.error(f"❌ Non-conformance costs (${total_nonconform:,.2f}) exceed conformance costs (${total_conform:,.2f}). Invest more in prevention!")
                    potential_savings = total_nonconform * 0.40
                    additional_prevention = potential_savings * 0.15
                    st.info(f"💡 Increasing prevention spending by ${additional_prevention:,.2f} could potentially reduce failure costs by ${potential_savings:,.2f}!")
                else:
                    st.success(f"✅ Conformance costs dominate — good quality investment strategy!")

                if total_ext > total_int:
                    st.warning(f"⚠️ External failures (${total_ext:,.2f}) exceed internal failures (${total_int:,.2f}). Strengthen inspection processes!")
                else:
                    st.success("✅ More defects caught internally than externally — good detection process!")

                # COQ Trend benchmark
                coq_pct = total_coq / annual_sales * 100
                if coq_pct > 10:
                    st.error(f"❌ COQ is {coq_pct:.1f}% of sales — HIGH. Industry average is 5-8%. Significant improvement needed.")
                elif coq_pct > 6:
                    st.warning(f"⚠️ COQ is {coq_pct:.1f}% of sales — AVERAGE. Target < 5% for world-class quality.")
                elif coq_pct > 3:
                    st.info(f"ℹ️ COQ is {coq_pct:.1f}% of sales — GOOD. World-class target is < 2-3%.")
                else:
                    st.success(f"✅ COQ is {coq_pct:.1f}% of sales — WORLD-CLASS quality performance!")

        elif calc_choice == "🎯 Six Sigma DPMO Calculator":
            st.subheader("Six Sigma DPMO & Sigma Level Calculator")

            col1, col2 = st.columns(2)
            with col1:
                total_units = st.number_input("Total Units Processed", 1, value=10000, step=100)
                total_defects = st.number_input("Total Defects Found", 0, value=500, step=10)
                opportunities_per_unit = st.number_input("Defect Opportunities per Unit", 1, value=5, step=1)

            with col2:
                st.markdown("**Six Sigma Reference Table:**")
                ref_df = pd.DataFrame({
                    "Sigma Level": ["1σ", "2σ", "3σ", "4σ", "5σ", "6σ"],
                    "DPMO": ["691,462", "308,538", "66,807", "6,210", "233", "3.4"],
                    "Yield %": ["30.9%", "69.1%", "93.3%", "99.4%", "99.98%", "99.9997%"],
                    "Classification": ["Very Poor", "Poor", "Industry Avg", "Good", "Excellent", "World-Class"]
                })
                st.dataframe(ref_df, use_container_width=True, hide_index=True)

            total_opportunities = total_units * opportunities_per_unit
            dpo = total_defects / total_opportunities if total_opportunities > 0 else 0
            dpmo = dpo * 1000000
            defect_rate = total_defects / total_units * 100 if total_units > 0 else 0
            yield_pct = 100 - defect_rate

            # Approximate sigma level using lookup
            sigma_lookup = [(3.4, 6.0), (233, 5.0), (6210, 4.0), (66807, 3.0), (308538, 2.0)]
            sigma_level = 1.0
            for dpmo_ref, sigma_ref in sigma_lookup:
                if dpmo <= dpmo_ref:
                    sigma_level = sigma_ref
                    break
                elif dpmo <= dpmo_ref * 10:
                    sigma_level = sigma_ref - 0.5

            col1, col2, col3, col4 = st.columns(4)
            with col1: st.metric("DPMO", f"{dpmo:,.0f}")
            with col2: st.metric("Defect Rate", f"{defect_rate:.2f}%")
            with col3: st.metric("Process Yield", f"{yield_pct:.2f}%")
            with col4:
                if dpmo <= 3.4:
                    st.metric("Sigma Level", "6σ 🏆")
                elif dpmo <= 233:
                    st.metric("Sigma Level", "5σ ✅")
                elif dpmo <= 6210:
                    st.metric("Sigma Level", "4σ 🟡")
                elif dpmo <= 66807:
                    st.metric("Sigma Level", "3σ ⚠️")
                else:
                    st.metric("Sigma Level", "<3σ ❌")

            st.markdown(f"""
            **Detailed Calculation:**
            ```
            Total Opportunities = {total_units:,} × {opportunities_per_unit} = {total_opportunities:,}
            DPO = {total_defects:,} / {total_opportunities:,} = {dpo:.6f}
            DPMO = {dpo:.6f} × 1,000,000 = {dpmo:,.0f}
            Process Yield = 100% − {defect_rate:.2f}% = {yield_pct:.2f}%
            ```
            """)

            # Improvement targets
            st.markdown("### Improvement Targets:")
            targets_df = pd.DataFrame({
                "Target Sigma": ["3σ (Baseline)", "4σ (Good)", "5σ (Excellent)", "6σ (World-Class)"],
                "Target DPMO": ["66,807", "6,210", "233", "3.4"],
                "Required Defects Reduction": [
                    f"{max(0, total_defects - int(66807 * total_opportunities / 1000000)):,}" if dpmo > 66807 else "Already achieved",
                    f"{max(0, total_defects - int(6210 * total_opportunities / 1000000)):,}" if dpmo > 6210 else "Already achieved",
                    f"{max(0, total_defects - int(233 * total_opportunities / 1000000)):,}" if dpmo > 233 else "Already achieved",
                    f"{max(0, total_defects - int(3.4 * total_opportunities / 1000000)):,}" if dpmo > 3.4 else "Already achieved"
                ]
            })
            st.dataframe(targets_df, use_container_width=True, hide_index=True)

        elif calc_choice == "🔍 Waste Identification Tool":
            st.subheader("Lean Waste (Muda) Identification Tool")
            st.info("Rate the severity of each waste type in your process (1=None, 5=Severe)")

            wastes = {
                "Transportation": {"icon": "🚛", "desc": "Moving materials/products unnecessarily", "example": "Moving parts between distant workstations"},
                "Inventory": {"icon": "📦", "desc": "Excess materials or WIP beyond immediate needs", "example": "Large buffer stocks between processes"},
                "Motion": {"icon": "🚶", "desc": "Unnecessary movement of people", "example": "Workers walking far to get tools/materials"},
                "Waiting": {"icon": "⏳", "desc": "Idle time, people or machines waiting", "example": "Machine waiting for operator, operator waiting for machine"},
                "Overproduction": {"icon": "🏭", "desc": "Making more than needed, sooner than needed", "example": "Building to forecast instead of customer orders"},
                "Over-processing": {"icon": "⚙️", "desc": "More work or features than customer requires", "example": "Painting surfaces that won't be seen"},
                "Defects": {"icon": "❌", "desc": "Rework, scrap, incorrect information", "example": "Parts requiring rework or scrapping"},
                "Skills (unused)": {"icon": "🧠", "desc": "Underutilizing people's talents and knowledge", "example": "Experts spending time on routine tasks"}
            }

            waste_scores = {}
            annual_cost = st.number_input("Annual Operating Cost ($)", 0.0, value=5000000.0, step=100000.0)
            st.markdown("---")

            for waste_name, waste_info in wastes.items():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{waste_info['icon']} {waste_name}:** {waste_info['desc']}")
                    st.caption(f"Example: {waste_info['example']}")
                with col2:
                    score = st.slider("Severity", 1, 5, 3, key=f"waste_{waste_name}")
                    waste_scores[waste_name] = score

            if st.button("🧮 Generate Waste Analysis Report", type="primary"):
                st.markdown("---")
                st.markdown("### Waste Analysis Results:")

                total_score = sum(waste_scores.values())
                max_score = len(wastes) * 5
                waste_index = total_score / max_score * 100

                sorted_wastes = sorted(waste_scores.items(), key=lambda x: x[1], reverse=True)

                waste_df = pd.DataFrame([{
                    "Waste Type": name,
                    "Severity Score": score,
                    "Priority": "🔴 Critical" if score >= 4 else ("🟡 Monitor" if score >= 3 else "🟢 Low"),
                    "Estimated % of Cost": f"{score/max_score*100*len(wastes):.1f}%",
                    "Estimated Annual Cost": f"${annual_cost * score / (max_score * len(wastes) / len(wastes)):.0f}"
                } for name, score in sorted_wastes])
                st.dataframe(waste_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Overall Waste Index", f"{waste_index:.1f}%")
                with col2:
                    critical_wastes = [k for k, v in waste_scores.items() if v >= 4]
                    st.metric("Critical Wastes", f"{len(critical_wastes)}")
                with col3:
                    est_waste_cost = annual_cost * waste_index / 100 * 0.3
                    st.metric("Estimated Waste Cost", f"${est_waste_cost:,.0f}")

                if waste_index > 60:
                    st.error(f"❌ High waste index ({waste_index:.0f}%). Urgent lean transformation needed!")
                elif waste_index > 40:
                    st.warning(f"⚠️ Moderate waste ({waste_index:.0f}%). Lean improvement program recommended.")
                else:
                    st.success(f"✅ Low waste index ({waste_index:.0f}%). Lean practices appear effective.")

                st.markdown("### Top 3 Priority Actions:")
                for i, (waste_name, score) in enumerate(sorted_wastes[:3]):
                    icon = wastes[waste_name]["icon"]
                    st.markdown(f"**{i+1}. {icon} {waste_name} (Score: {score}/5)**")
                    st.markdown(f"   Action: Analyze and eliminate {wastes[waste_name]['desc'].lower()}")

        elif calc_choice == "📈 Quality Improvement ROI":
            st.subheader("Quality Investment ROI Calculator")
            st.markdown("Analyze the return on investing in quality prevention activities.")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Current Situation:**")
                curr_sales = st.number_input("Annual Sales ($)", 0.0, value=5000000.0, step=100000.0)
                curr_internal_fail = st.number_input("Current Internal Failure Cost ($)", 0.0, value=300000.0, step=10000.0)
                curr_external_fail = st.number_input("Current External Failure Cost ($)", 0.0, value=250000.0, step=10000.0)
                curr_appraisal = st.number_input("Current Appraisal Cost ($)", 0.0, value=150000.0, step=5000.0)
                curr_prevention = st.number_input("Current Prevention Cost ($)", 0.0, value=100000.0, step=5000.0)

            with col2:
                st.markdown("**Proposed Investment:**")
                additional_prevention = st.number_input("Additional Prevention Investment ($)", 0.0, value=80000.0, step=5000.0)
                expected_fail_reduction = st.number_input("Expected Failure Cost Reduction (%)", 0.0, 100.0, 35.0, step=5.0)
                expected_appraisal_reduction = st.number_input("Expected Appraisal Cost Reduction (%)", 0.0, 100.0, 15.0, step=5.0)
                implementation_years = st.number_input("Years to Full Implementation", 1, 5, 2)

            if st.button("🧮 Calculate Quality Investment ROI", type="primary"):
                curr_total_fail = curr_internal_fail + curr_external_fail
                curr_total_coq = curr_prevention + curr_appraisal + curr_total_fail

                fail_savings = curr_total_fail * expected_fail_reduction / 100
                appraisal_savings = curr_appraisal * expected_appraisal_reduction / 100
                total_annual_savings = fail_savings + appraisal_savings
                net_annual_savings = total_annual_savings - additional_prevention

                payback = additional_prevention / net_annual_savings if net_annual_savings > 0 else float('inf')
                roi = net_annual_savings / additional_prevention * 100 if additional_prevention > 0 else 0

                new_total_coq = (curr_prevention + additional_prevention) + (curr_appraisal - appraisal_savings) + (curr_total_fail - fail_savings)

                st.markdown("---")
                st.markdown("### Investment Analysis Results:")

                results_df = pd.DataFrame({
                    "Metric": ["Current Total COQ", "New Prevention Cost", "Failure Cost Reduction",
                                "Appraisal Cost Reduction", "Total Annual Savings", "Net Annual Savings",
                                "New Total COQ", "COQ Reduction"],
                    "Amount": [f"${curr_total_coq:,.2f}", f"${curr_prevention + additional_prevention:,.2f}",
                                f"${fail_savings:,.2f}", f"${appraisal_savings:,.2f}",
                                f"${total_annual_savings:,.2f}", f"${net_annual_savings:,.2f}",
                                f"${new_total_coq:,.2f}", f"${curr_total_coq - new_total_coq:,.2f}"]
                })
                st.dataframe(results_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Quality Investment ROI", f"{roi:.1f}%")
                with col2: st.metric("Payback Period", f"{payback:.1f} years" if payback != float('inf') else "No payback")
                with col3: st.metric("COQ % of Sales (new)", f"{new_total_coq/curr_sales*100:.2f}%",
                                     delta=f"{(new_total_coq - curr_total_coq)/curr_sales*100:.2f}%")

                if roi > 50:
                    st.success(f"✅ Excellent ROI of {roi:.1f}%! Quality investment is highly justified.")
                elif roi > 20:
                    st.info(f"✅ Good ROI of {roi:.1f}%. Quality investment is worthwhile.")
                elif roi > 0:
                    st.warning(f"⚠️ Positive but modest ROI of {roi:.1f}%. Consider if non-financial benefits justify the investment.")
                else:
                    st.error(f"❌ Negative ROI. Re-evaluate the investment or expected savings.")

        elif calc_choice == "🔄 Value Stream Analysis":
            st.subheader("Value Stream Analysis Tool")
            st.markdown("Map and analyze your production process for waste and improvement opportunities.")

            num_steps = st.number_input("Number of Process Steps", 2, 12, 6)
            steps = []
            for i in range(int(num_steps)):
                st.markdown(f"**Step {i+1}:**")
                col1, col2, col3, col4 = st.columns(4)
                with col1: step_name = st.text_input("Step Name", value=f"Step {i+1}", key=f"vs_name_{i}")
                with col2: cycle_time = st.number_input("Cycle Time (mins)", 0.0, value=30.0, key=f"vs_ct_{i}")
                with col3: wait_time = st.number_input("Wait Time (mins)", 0.0, value=120.0, key=f"vs_wt_{i}")
                with col4:
                    value_added = st.selectbox("Type", ["Value-Added ✅", "Non-Value-Added ❌", "Required NVA ⚠️"], key=f"vs_va_{i}")
                steps.append({"name": step_name, "cycle": cycle_time, "wait": wait_time, "type": value_added})

            if st.button("🧮 Analyze Value Stream", type="primary"):
                total_cycle = sum([s["cycle"] for s in steps])
                total_wait = sum([s["wait"] for s in steps])
                total_lead = total_cycle + total_wait
                va_time = sum([s["cycle"] for s in steps if "Value-Added" in s["type"] and "Non" not in s["type"]])
                nva_time = total_lead - va_time
                process_efficiency = va_time / total_lead * 100 if total_lead > 0 else 0

                col1, col2, col3, col4 = st.columns(4)
                with col1: st.metric("Total Lead Time", f"{total_lead/60:.1f} hrs")
                with col2: st.metric("Value-Added Time", f"{va_time:.0f} mins")
                with col3: st.metric("Non-Value-Added Time", f"{nva_time:.0f} mins")
                with col4:
                    color = "normal" if process_efficiency > 50 else "inverse"
                    st.metric("Process Efficiency", f"{process_efficiency:.1f}%")

                vs_df = pd.DataFrame([{
                    "Step": s["name"], "Cycle Time (min)": s["cycle"],
                    "Wait Time (min)": s["wait"], "Total Time": s["cycle"] + s["wait"],
                    "Type": s["type"],
                    "Elimination Priority": "HIGH" if "Non-Value-Added" in s["type"] and "Required" not in s["type"] else "LOW"
                } for s in steps])
                st.dataframe(vs_df, use_container_width=True, hide_index=True)

                if process_efficiency < 25:
                    st.error(f"❌ Process efficiency of {process_efficiency:.1f}% is very poor. Significant lean opportunity!")
                    wait_reduction = total_wait * 0.60
                    st.info(f"💡 Potential: Reducing wait time by 60% would save {wait_reduction:.0f} mins and improve efficiency to {(va_time/(total_lead - wait_reduction))*100:.1f}%")
                elif process_efficiency < 50:
                    st.warning(f"⚠️ Moderate process efficiency ({process_efficiency:.1f}%). Good lean improvement potential.")
                else:
                    st.success(f"✅ Reasonable process efficiency ({process_efficiency:.1f}%). Continue with Kaizen improvements.")

        else:  # Lean Metrics Dashboard
            st.subheader("Lean Performance Metrics Dashboard")
            st.markdown("### Enter Your Lean Metrics:")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Inventory Metrics:**")
                raw_mat_days = st.number_input("Raw Material Days on Hand", 0.0, value=15.0, step=1.0)
                wip_days = st.number_input("WIP Days on Hand", 0.0, value=8.0, step=0.5)
                fg_days = st.number_input("Finished Goods Days on Hand", 0.0, value=12.0, step=1.0)

                st.markdown("**Quality Metrics:**")
                defect_rate = st.number_input("Defect Rate (%)", 0.0, value=2.5, step=0.1)
                first_pass_yield = st.number_input("First Pass Yield (%)", 0.0, 100.0, value=94.0, step=0.5)

            with col2:
                st.markdown("**Delivery Metrics:**")
                on_time_delivery = st.number_input("On-Time Delivery (%)", 0.0, 100.0, value=87.0, step=1.0)
                customer_lead_time = st.number_input("Customer Lead Time (days)", 0.0, value=8.0, step=1.0)
                target_lead_time = st.number_input("Target Lead Time (days)", 0.0, value=3.0, step=0.5)

                st.markdown("**Productivity:**")
                oee = st.number_input("Overall Equipment Effectiveness (%)", 0.0, 100.0, value=72.0, step=1.0)
                productivity = st.number_input("Labor Productivity (units/hr)", 0.0, value=45.0, step=1.0)

            total_inventory_days = raw_mat_days + wip_days + fg_days

            st.markdown("---")
            st.markdown("### Lean Scorecard:")

            metrics_data = [
                {"Metric": "Total Inventory Days", "Current": f"{total_inventory_days:.0f} days", "Lean Target": "< 10 days",
                 "Status": "✅" if total_inventory_days < 10 else ("⚠️" if total_inventory_days < 20 else "❌")},
                {"Metric": "Defect Rate", "Current": f"{defect_rate:.1f}%", "Lean Target": "< 0.5%",
                 "Status": "✅" if defect_rate < 0.5 else ("⚠️" if defect_rate < 2 else "❌")},
                {"Metric": "First Pass Yield", "Current": f"{first_pass_yield:.1f}%", "Lean Target": "> 99%",
                 "Status": "✅" if first_pass_yield > 99 else ("⚠️" if first_pass_yield > 95 else "❌")},
                {"Metric": "On-Time Delivery", "Current": f"{on_time_delivery:.1f}%", "Lean Target": "> 98%",
                 "Status": "✅" if on_time_delivery > 98 else ("⚠️" if on_time_delivery > 90 else "❌")},
                {"Metric": "Customer Lead Time", "Current": f"{customer_lead_time:.1f} days", "Lean Target": f"< {target_lead_time:.1f} days",
                 "Status": "✅" if customer_lead_time <= target_lead_time else ("⚠️" if customer_lead_time <= target_lead_time * 1.5 else "❌")},
                {"Metric": "OEE", "Current": f"{oee:.1f}%", "Lean Target": "> 85%",
                 "Status": "✅" if oee > 85 else ("⚠️" if oee > 70 else "❌")},
            ]

            scorecard_df = pd.DataFrame(metrics_data)
            st.dataframe(scorecard_df, use_container_width=True, hide_index=True)

            green_count = sum(1 for m in metrics_data if "✅" in m["Status"])
            yellow_count = sum(1 for m in metrics_data if "⚠️" in m["Status"])
            red_count = sum(1 for m in metrics_data if "❌" in m["Status"])

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("✅ On Target", f"{green_count}/6")
            with col2: st.metric("⚠️ Needs Improvement", f"{yellow_count}/6")
            with col3: st.metric("❌ Critical", f"{red_count}/6")

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Cost of Quality Distribution")
        coq_categories = ["Prevention", "Appraisal", "Internal Failure", "External Failure"]
        coq_values = [160000, 190000, 270000, 280000]
        coq_colors = ["#27AE60", "#3498DB", "#E67E22", "#E74C3C"]

        fig1 = px.pie(values=coq_values, names=coq_categories,
                      title="Cost of Quality Breakdown ($900,000 Total)",
                      color_discrete_sequence=coq_colors)
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Quality Cost Relationship — Prevention vs Failure")
        prevention_invest = np.linspace(0, 500000, 100)
        failure_costs = 800000 * np.exp(-prevention_invest / 150000)
        appraisal_costs = 200000 * np.exp(-prevention_invest / 300000)
        total_coq = prevention_invest + appraisal_costs + failure_costs

        optimal_idx = np.argmin(total_coq)

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=prevention_invest, y=failure_costs, mode="lines",
                                   name="Failure Costs", line=dict(color="#E74C3C", width=2)))
        fig2.add_trace(go.Scatter(x=prevention_invest, y=appraisal_costs, mode="lines",
                                   name="Appraisal Costs", line=dict(color="#3498DB", width=2)))
        fig2.add_trace(go.Scatter(x=prevention_invest, y=prevention_invest, mode="lines",
                                   name="Prevention Costs", line=dict(color="#27AE60", width=2)))
        fig2.add_trace(go.Scatter(x=prevention_invest, y=total_coq, mode="lines",
                                   name="Total COQ", line=dict(color="#2C3E50", width=3, dash="dash")))
        fig2.add_vline(x=prevention_invest[optimal_idx], line_dash="dot", line_color="purple",
                       annotation_text=f"Optimal: ${prevention_invest[optimal_idx]:,.0f}")
        fig2.update_layout(title="Optimal Quality Investment Point",
                           xaxis_title="Prevention Investment ($)", yaxis_title="Cost ($)",
                           hovermode="x unified")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Six Sigma Levels — Defects per Million")
        sigma_levels = ["1σ", "2σ", "3σ", "4σ", "5σ", "6σ"]
        dpmo_values = [691462, 308538, 66807, 6210, 233, 3.4]
        colors_sigma = ["#E74C3C", "#E67E22", "#F1C40F", "#2ECC71", "#27AE60", "#1A5276"]

        fig3 = go.Figure(go.Bar(
            x=sigma_levels, y=[np.log10(d) for d in dpmo_values],
            marker_color=colors_sigma,
            text=[f"{d:,.0f} DPMO" for d in dpmo_values],
            textposition="auto"
        ))
        fig3.update_layout(title="Six Sigma Levels (log scale — lower is better)",
                           xaxis_title="Sigma Level", yaxis_title="Log10(DPMO)")
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("8 Wastes Impact Analysis")
        wastes_viz = ["Transportation", "Inventory", "Motion", "Waiting",
                      "Overproduction", "Over-processing", "Defects", "Skills"]
        waste_pct = [8, 15, 6, 20, 25, 7, 12, 7]
        waste_colors_viz = ["#3498DB", "#E74C3C", "#27AE60", "#E67E22",
                             "#9B59B6", "#1ABC9C", "#E74C3C", "#95A5A6"]

        fig4 = go.Figure(go.Bar(
            x=waste_pct, y=wastes_viz, orientation="h",
            marker_color=waste_colors_viz,
            text=[f"{p}%" for p in waste_pct], textposition="auto"
        ))
        fig4.update_layout(title="Typical Waste Distribution in Manufacturing (%)",
                           xaxis_title="% of Total Waste Cost", yaxis_title="Waste Type")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. Which cost of quality category is MOST valuable to invest in?**")
        q1 = st.radio("", [
            "Appraisal costs — detect defects before they reach customers",
            "Internal failure costs — fix problems before shipping",
            "Prevention costs — prevent defects from occurring at all",
            "External failure costs — learn from customer complaints"
        ], key="m14q1")
        if st.button("Check Q1", key="m14c1"):
            if q1 == "Prevention costs — prevent defects from occurring at all":
                st.success("✅ Correct! Prevention is the most valuable — stopping defects before they occur yields the highest return on quality investment.")
            else:
                st.error("❌ Incorrect. Prevention costs are the most valuable — preventing defects yields far greater savings than detecting or fixing them.")

        st.markdown("---")
        st.markdown("**Q2. Six Sigma achieves approximately:**")
        q2 = st.radio("", [
            "Zero defects — 100% perfect quality",
            "3.4 defects per million opportunities",
            "3.4% defect rate",
            "34 defects per thousand units"
        ], key="m14q2")
        if st.button("Check Q2", key="m14c2"):
            if q2 == "3.4 defects per million opportunities":
                st.success("✅ Correct! Six Sigma = 3.4 DPMO — only 3.4 defects per million opportunities.")
            else:
                st.error("❌ Incorrect. Six Sigma achieves 3.4 defects per MILLION opportunities (DPMO), not per thousand or as a percentage.")

        st.markdown("---")
        st.markdown("**Q3. JIT (Just-In-Time) production is based on which system?**")
        q3 = st.radio("", [
            "Push system — produce to forecast, push to inventory",
            "Pull system — produce only when customer demand triggers it",
            "Batch system — large batches to maximize efficiency",
            "Safety stock system — maintain large buffer inventories"
        ], key="m14q3")
        if st.button("Check Q3", key="m14c3"):
            if q3 == "Pull system — produce only when customer demand triggers it":
                st.success("✅ Correct! JIT uses a pull system — customer demand triggers production, eliminating excess inventory.")
            else:
                st.error("❌ Incorrect. JIT uses a PULL system — production is triggered by actual demand, not pushed ahead of demand.")

        st.markdown("---")
        st.markdown("""
        **Q4. Warranty costs of $500,000 and rework costs of $300,000 are:
        What types of quality costs are these?**
        """)
        q4 = st.radio("", [
            "Both are prevention costs",
            "Warranty = External Failure; Rework = Internal Failure",
            "Both are appraisal costs",
            "Warranty = Internal Failure; Rework = External Failure"
        ], key="m14q4")
        if st.button("Check Q4", key="m14c4"):
            if q4 == "Warranty = External Failure; Rework = Internal Failure":
                st.success("✅ Correct! Warranty costs occur after the customer receives the product (external). Rework is caught before delivery (internal).")
            else:
                st.error("❌ Incorrect. Warranty = External Failure (after customer receives it). Rework = Internal Failure (caught before delivery).")

        st.markdown("---")
        st.markdown("**Q5. In lean accounting, the main focus is on:**")
        q5 = st.radio("", [
            "Allocating overhead costs as accurately as possible",
            "Value stream costing and eliminating waste from all processes",
            "Maximizing standard costing accuracy",
            "Increasing inventory to absorb fixed overhead"
        ], key="m14q5")
        if st.button("Check Q5", key="m14c5"):
            if q5 == "Value stream costing and eliminating waste from all processes":
                st.success("✅ Correct! Lean accounting focuses on value stream costing, visual management, and driving out all forms of waste.")
            else:
                st.error("❌ Incorrect. Lean accounting focuses on value stream costing and waste elimination, not complex overhead allocation or inventory building.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Cost of Quality Framework")
        coq_df = pd.DataFrame({
            "Category": ["Prevention", "Appraisal", "Internal Failure", "External Failure"],
            "When": ["Before defects occur", "Detecting defects", "Before delivery", "After delivery to customer"],
            "Goal": ["Prevent problems", "Detect problems", "Fix before shipping", "Recover from failures"],
            "Examples": [
                "Training, SPC, supplier certification, design review",
                "Inspection, testing, quality audits, calibration",
                "Scrap, rework, downtime, re-inspection",
                "Warranty, returns, complaints, recalls, lost goodwill"
            ],
            "Type": ["Conformance ✅", "Conformance ✅", "Non-conformance ❌", "Non-conformance ❌"]
        })
        st.dataframe(coq_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Six Sigma DMAIC Framework")
        dmaic_df = pd.DataFrame({
            "Phase": ["Define", "Measure", "Analyze", "Improve", "Control"],
            "Key Question": ["What is the problem?", "How big is the problem?", "What causes the problem?",
                              "How do we fix it?", "How do we sustain the fix?"],
            "Key Tools": [
                "Project charter, VOC, SIPOC",
                "Process mapping, data collection, measurement system analysis",
                "Fishbone diagram, Pareto chart, regression, hypothesis testing",
                "Design of experiments, pilot testing, implementation",
                "Control charts (SPC), control plan, standard work"
            ]
        })
        st.dataframe(dmaic_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Lean vs Traditional Manufacturing")
        lean_compare = pd.DataFrame({
            "Feature": ["Inventory philosophy", "Production trigger", "Quality approach",
                         "Batch sizes", "Setup time", "Lead time", "Cost accounting"],
            "Traditional": ["Build buffer stocks", "Push (make to forecast)", "Inspect in quality",
                             "Large batches (efficiency)", "Long (minimize changeovers)", "Long",
                             "Standard costing, variances"],
            "Lean / JIT": ["Minimize to near-zero", "Pull (make to order)", "Build in quality",
                            "Small / single piece flow", "Short (SMED)", "Short",
                            "Value stream costing, visual"]
        })
        st.dataframe(lean_compare, use_container_width=True, hide_index=True)

        st.subheader("📊 Key Quality Metrics")
        metrics_summary = pd.DataFrame({
            "Metric": ["Defect Rate", "DPMO", "Sigma Level", "First Pass Yield",
                        "Process Efficiency", "OEE"],
            "Formula": [
                "Defects / Total Units × 100",
                "(Defects / Opportunities) × 1,000,000",
                "Derived from DPMO table (3σ=66,807, 6σ=3.4)",
                "Units passing on first attempt / Total Units × 100",
                "Value-Added Time / Total Lead Time × 100",
                "Availability × Performance × Quality"
            ],
            "World-Class Target": [
                "< 0.034% (6σ)", "3.4 DPMO", "6σ", "> 99.97%",
                "> 85%", "> 85%"
            ]
        })
        st.dataframe(metrics_summary, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Investing only in appraisal, not prevention",
                "Treating quality cost reports as accounting exercises only",
                "Implementing Six Sigma without management commitment",
                "Building safety stock as a substitute for quality",
                "Using traditional standard costing in lean environments",
                "Measuring only defect rate, not cost of quality"
            ],
            "Correct Approach": [
                "Shift investment toward prevention — every $1 in prevention saves $5-$10 in failures",
                "Use COQ reports to drive improvement decisions and resource allocation",
                "Six Sigma needs champion support, resources, and cultural change",
                "Fix the root cause of variability instead of buffering with inventory",
                "Lean accounting uses value stream costing and visual management",
                "Track all four COQ categories — total picture is much larger than defect rate alone"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 14 Complete! You can build COQ reports, apply Six Sigma DMAIC, identify lean wastes, and implement lean accounting.")
        st.info("💡 Next: Module 15 — Strategic Management Accounting")

if __name__ == "__main__":
    show()