import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📚 Managerial Accounting — Complete Course Overview")
    st.markdown("*Your comprehensive guide to all 15 modules — summaries, formulas, and interactive review tools*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🗺️ Course Map", "📖 Module Summaries", "🧮 Formula Bank",
        "📊 Visual Dashboard", "✅ Master Quiz", "🎓 Study Planner"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("🗺️ Course Map — 15 Modules at a Glance")

        st.markdown("""
        ### Welcome to the Complete Managerial Accounting Course
        This course transforms you from a beginner to an **expert** in managerial accounting.
        Below is your complete learning roadmap across **15 comprehensive modules**.
        """)

        # Module cards
        modules_info = [
            {"num": 1, "title": "Foundations of Managerial Accounting",
             "icon": "📊", "color": "#2E86C1",
             "topics": ["Managerial vs Financial Accounting", "Cost Classifications", "Product vs Period Costs", "IMA Ethics"],
             "key_skill": "Classify any cost correctly", "difficulty": "Beginner"},

            {"num": 2, "title": "Cost-Volume-Profit (CVP) Analysis",
             "icon": "📈", "color": "#27AE60",
             "topics": ["Cost Behaviour Patterns", "Contribution Margin", "Break-Even Analysis", "Operating Leverage"],
             "key_skill": "Calculate break-even and target profit", "difficulty": "Beginner"},

            {"num": 3, "title": "Job Order Costing Systems",
             "icon": "🏭", "color": "#8E44AD",
             "topics": ["Job Cost Sheets", "Predetermined OH Rate", "Under/Overapplied OH", "Cost Flow"],
             "key_skill": "Build a complete job cost sheet", "difficulty": "Intermediate"},

            {"num": 4, "title": "Process Costing Systems",
             "icon": "🔄", "color": "#E67E22",
             "topics": ["Equivalent Units (EUP)", "Weighted Average Method", "FIFO Method", "Production Cost Report"],
             "key_skill": "Prepare a production cost report", "difficulty": "Intermediate"},

            {"num": 5, "title": "Activity-Based Costing (ABC)",
             "icon": "🎯", "color": "#E74C3C",
             "topics": ["Cost Hierarchy", "Activity Rate Calculation", "ABC vs Traditional", "Customer Profitability"],
             "key_skill": "Design and implement an ABC system", "difficulty": "Intermediate"},

            {"num": 6, "title": "Cost Allocation & Joint Products",
             "icon": "🔀", "color": "#1ABC9C",
             "topics": ["Direct Method", "Step-Down Method", "Joint Cost Allocation", "Sell or Process Further"],
             "key_skill": "Allocate service costs and joint costs", "difficulty": "Intermediate"},

            {"num": 7, "title": "Variable vs Absorption Costing",
             "icon": "⚖️", "color": "#3498DB",
             "topics": ["Absorption Costing", "Variable Costing", "Income Reconciliation", "Production Effects"],
             "key_skill": "Reconcile absorption and variable income", "difficulty": "Intermediate"},

            {"num": 8, "title": "Budgeting & Financial Planning",
             "icon": "📋", "color": "#2C3E50",
             "topics": ["Master Budget", "Production Budget", "Cash Budget", "Budgeted Statements"],
             "key_skill": "Build a complete master budget", "difficulty": "Intermediate"},

            {"num": 9, "title": "Standard Costing & Variance Analysis",
             "icon": "🎯", "color": "#D35400",
             "topics": ["Standard Cost Card", "DM Variances", "DL Variances", "OH Variances"],
             "key_skill": "Calculate and interpret all cost variances", "difficulty": "Advanced"},

            {"num": 10, "title": "Responsibility Accounting & Segments",
             "icon": "🏢", "color": "#16A085",
             "topics": ["Responsibility Centers", "Segment Margin", "ROI & DuPont", "RI and EVA"],
             "key_skill": "Evaluate division performance with ROI/RI/EVA", "difficulty": "Advanced"},

            {"num": 11, "title": "Relevant Costs for Decision Making",
             "icon": "⚖️", "color": "#8E44AD",
             "topics": ["Sunk vs Relevant Costs", "Special Orders", "Make or Buy", "Product Mix Constraints"],
             "key_skill": "Apply differential analysis to business decisions", "difficulty": "Advanced"},

            {"num": 12, "title": "Capital Budgeting",
             "icon": "💰", "color": "#27AE60",
             "topics": ["Payback Period", "Net Present Value", "IRR", "After-Tax Cash Flows"],
             "key_skill": "Evaluate investments using NPV and IRR", "difficulty": "Advanced"},

            {"num": 13, "title": "Pricing Decisions & Target Costing",
             "icon": "🏷️", "color": "#E74C3C",
             "topics": ["Cost-Plus Pricing", "Target Costing", "Value Engineering", "Life-Cycle Costing"],
             "key_skill": "Set prices and engineer costs to meet targets", "difficulty": "Advanced"},

            {"num": 14, "title": "Quality Management & Lean Accounting",
             "icon": "🏆", "color": "#F39C12",
             "topics": ["Cost of Quality (COQ)", "Six Sigma & DMAIC", "JIT & Lean", "Value Stream Costing"],
             "key_skill": "Build COQ reports and identify lean wastes", "difficulty": "Advanced"},

            {"num": 15, "title": "Strategic Management Accounting",
             "icon": "🌐", "color": "#1A5276",
             "topics": ["Value Chain Analysis", "Benchmarking", "Customer Lifetime Value", "Sustainability Accounting"],
             "key_skill": "Apply strategic tools for competitive advantage", "difficulty": "Expert"},
        ]

        # Display in rows of 3
        difficulty_colors = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🟠", "Expert": "🔴"}

        for row_start in range(0, len(modules_info), 3):
            cols = st.columns(3)
            for col_idx, mod in enumerate(modules_info[row_start:row_start+3]):
                with cols[col_idx]:
                    difficulty_icon = difficulty_colors.get(mod["difficulty"], "⚪")
                    st.markdown(f"""
                    <div style="background-color:{mod['color']}22; border-left:5px solid {mod['color']};
                    padding:12px; border-radius:8px; margin-bottom:8px; min-height:180px;">
                    <h4 style="color:{mod['color']}; margin:0;">{mod['icon']} Module {mod['num']}</h4>
                    <strong>{mod['title']}</strong><br>
                    <small>{difficulty_icon} {mod['difficulty']}</small><br><br>
                    <small>🔑 <em>{mod['key_skill']}</em></small>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("📈 Learning Progression")

        learning_path = pd.DataFrame({
            "Phase": ["Phase 1: Foundations", "Phase 2: Costing Systems", "Phase 3: Planning & Control", "Phase 4: Decisions & Strategy"],
            "Modules": ["1 – 2", "3 – 7", "8 – 10", "11 – 15"],
            "Focus": ["Cost concepts, CVP", "Job, Process, ABC, Allocation", "Budgets, Variances, Performance", "Capital, Pricing, Quality, Strategy"],
            "Duration": ["~2 weeks", "~4 weeks", "~3 weeks", "~5 weeks"]
        })
        st.dataframe(learning_path, use_container_width=True, hide_index=True)

        st.subheader("🎓 Professional Certifications Covered")
        cert_df = pd.DataFrame({
            "Certification": ["CMA (USA) — IMA", "CIMA (UK)", "ACCA (Global)", "CPA — Management Accounting"],
            "Modules Most Relevant": [
                "All 15 modules — CMA covers managerial accounting comprehensively",
                "Modules 1-13 cover P1 (Management Accounting) and P2 (Advanced Management Accounting)",
                "Modules 1-11 cover PM (Performance Management) paper",
                "Modules 1-10 cover FAR and BEC management accounting sections"
            ],
            "Exam Coverage": ["~100%", "~85%", "~75%", "~70%"]
        })
        st.dataframe(cert_df, use_container_width=True, hide_index=True)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("📖 Module-by-Module Summaries")
        st.markdown("Quick reference summaries for all 15 modules.")

        selected_module = st.selectbox("Select a Module to Review:", [
            f"Module {m['num']}: {m['title']}" for m in modules_info
        ])

        mod_num = int(selected_module.split(":")[0].replace("Module ", ""))
        mod = modules_info[mod_num - 1]

        st.markdown(f"## {mod['icon']} Module {mod['num']}: {mod['title']}")
        st.markdown(f"**Difficulty:** {difficulty_colors.get(mod['difficulty'], '⚪')} {mod['difficulty']} | **Key Skill:** {mod['key_skill']}")

        summaries = {
            1: {
                "overview": "The foundation of managerial accounting — understanding what managerial accounting IS and how to classify costs correctly.",
                "key_concepts": [
                    "Managerial accounting: internal, future-oriented, no external rules",
                    "Financial accounting: external, historical, GAAP required",
                    "Product costs: DM + DL + Manufacturing OH → go to inventory",
                    "Period costs: S&A expenses → expensed immediately",
                    "Variable costs: change with activity; Fixed costs: constant within relevant range",
                    "Sunk costs: always irrelevant; Opportunity costs: always relevant"
                ],
                "key_formulas": {
                    "Total Product Cost": "DM + DL + Manufacturing Overhead",
                    "Total Period Cost": "Selling Expenses + Administrative Expenses",
                    "COGS": "Beginning Inventory + Product Costs − Ending Inventory"
                },
                "exam_tips": [
                    "Always ask: Does this cost go to inventory? → Product cost. Expensed now? → Period cost.",
                    "Fixed OH is a product cost under absorption, but a period cost under variable costing (Module 7)",
                    "Sunk costs are NEVER relevant to decisions — ignore them always"
                ]
            },
            2: {
                "overview": "CVP analysis is the most powerful short-term planning tool. Master contribution margin and you can answer almost any profitability question.",
                "key_concepts": [
                    "Contribution Margin = Sales − ALL Variable Costs",
                    "CM Ratio = CM / Sales × 100 — shows % of each sales dollar contributing to fixed costs and profit",
                    "Break-even: where total revenue = total costs (profit = zero)",
                    "Operating leverage: how a % change in sales magnifies % change in profit",
                    "Higher fixed costs = higher operating leverage = higher risk AND reward",
                    "Multi-product: use WEIGHTED AVERAGE CM ratio"
                ],
                "key_formulas": {
                    "Contribution Margin": "Sales Revenue − Variable Costs",
                    "CM Ratio": "CM / Sales Revenue",
                    "BEP (Units)": "Fixed Costs / CM per Unit",
                    "BEP ($)": "Fixed Costs / CM Ratio",
                    "Target Profit Units": "(Fixed Costs + Target Profit) / CM per Unit",
                    "Margin of Safety": "(Actual Sales − BEP Sales) / Actual Sales × 100",
                    "Degree of Operating Leverage": "CM / Net Operating Income"
                },
                "exam_tips": [
                    "BEP in dollars = Fixed Costs / CM Ratio (not CM per unit!)",
                    "Margin of safety tells you how much sales can fall before loss",
                    "DOL × % Change in Sales = % Change in Profit"
                ]
            },
            3: {
                "overview": "Job order costing tracks costs for each unique job — used in custom manufacturing, construction, and professional services.",
                "key_concepts": [
                    "Each job has a unique Job Cost Sheet accumulating DM, DL, and Applied OH",
                    "Predetermined OH Rate = Estimated OH / Estimated Allocation Base",
                    "Applied OH = POHR × Actual Allocation Base for each job",
                    "Under/Overapplied OH = Actual OH − Applied OH",
                    "Underapplied: increase COGS; Overapplied: decrease COGS (if immaterial)"
                ],
                "key_formulas": {
                    "POHR": "Estimated Total Manufacturing OH / Estimated Allocation Base",
                    "Applied OH": "POHR × Actual Allocation Base",
                    "Under/Overapplied": "Actual OH − Applied OH",
                    "Total Job Cost": "DM + DL + Applied OH",
                    "Cost per Unit": "Total Job Cost / Units Produced"
                },
                "exam_tips": [
                    "POHR is calculated BEFORE the period using ESTIMATED amounts",
                    "Applied OH uses ACTUAL allocation base (actual hours worked)",
                    "Actual OH goes into the OH account; Applied OH comes out — the difference is under/overapplied"
                ]
            },
            4: {
                "overview": "Process costing is for mass production of identical units — costs flow through departments and are averaged over all units.",
                "key_concepts": [
                    "EUP = Equivalent Units of Production (convert partial units to whole units)",
                    "Weighted Average: blends prior and current period costs",
                    "FIFO: keeps current period costs separate from prior period",
                    "Five-step production cost report: Flow → EUP → Cost/EUP → Assign to completed → Assign to ending WIP",
                    "Materials added at start = 100% in ending WIP; at end = 0%"
                ],
                "key_formulas": {
                    "Physical Flow": "Beg WIP + Started = Completed + Ending WIP",
                    "EUP (WA)": "Completed + (Ending WIP × % Complete)",
                    "EUP (FIFO)": "Beg WIP×(1−%) + Started&Completed + Ending WIP×%",
                    "Cost per EUP (WA)": "(Beg WIP Cost + Current Cost) / EUP",
                    "Cost per EUP (FIFO)": "Current Period Cost Only / EUP",
                    "Reconciliation": "Transferred Out Cost + Ending WIP Cost = Total Costs Available"
                },
                "exam_tips": [
                    "Always verify physical flow equation first",
                    "WA includes beginning WIP costs; FIFO uses current costs ONLY",
                    "Always reconcile: costs assigned must equal costs available"
                ]
            },
            5: {
                "overview": "ABC assigns overhead using multiple cost drivers, giving far more accurate product costs when products consume resources differently.",
                "key_concepts": [
                    "Traditional costing distorts costs when product diversity is high",
                    "Cost Hierarchy: Unit, Batch, Product, and Facility level activities",
                    "ABC: Products consume activities; Activities consume resources",
                    "Activity Rate = Total Activity Cost / Total Driver Quantity",
                    "Customer profitability: extend ABC to trace costs to individual customers"
                ],
                "key_formulas": {
                    "Activity Rate": "Total Activity Cost / Total Driver Quantity",
                    "Product OH Cost": "Σ (Activity Rate × Product's Driver Usage)",
                    "Customer Profit": "Gross Margin − Customer-Specific Activity Costs",
                    "Total Product Cost": "DM + DL + ABC Overhead"
                },
                "exam_tips": [
                    "High-volume simple products: overcost under traditional; undercost complex products",
                    "Batch-level: per batch (setup); Unit-level: per unit (machining)",
                    "Facility-level costs are difficult to assign to products — often excluded"
                ]
            },
            6: {
                "overview": "Service department costs must flow to production departments, then to products. Joint costs are arbitrary allocations — irrelevant for decisions.",
                "key_concepts": [
                    "Direct Method: allocate service costs only to production (ignore inter-service)",
                    "Step-Down: allocate sequentially; once closed, dept receives no more costs",
                    "NRV = Final Sales Value − Separable Costs",
                    "Sell or Process Further: compare incremental revenue vs incremental separable cost",
                    "Joint costs are SUNK — completely irrelevant to sell-or-process-further!"
                ],
                "key_formulas": {
                    "Direct Method Alloc %": "Prod Dept Usage / Total Production Usage",
                    "Sales Value Alloc %": "Product Sales Value / Total Sales Value",
                    "NRV": "Final Sales Value − Separable Costs",
                    "Process Further Net Benefit": "(Final Price − Split-off Price) × Units − Separable Costs"
                },
                "exam_tips": [
                    "Direct method IGNORES inter-service usage — only production department usage",
                    "Step-Down: once a dept is allocated, it CANNOT receive any more costs",
                    "NEVER include joint costs in process-further analysis — they are sunk!"
                ]
            },
            7: {
                "overview": "The ONLY difference between absorption and variable costing is where fixed manufacturing overhead goes — inventory vs immediate expense.",
                "key_concepts": [
                    "Absorption: Fixed Mfg OH is a PRODUCT cost (inventoried)",
                    "Variable: Fixed Mfg OH is a PERIOD cost (expensed immediately)",
                    "Production > Sales: Absorption income HIGHER (fixed OH deferred in inventory)",
                    "Production < Sales: Absorption income LOWER (fixed OH released from inventory)",
                    "GAAP and tax require absorption costing; variable used internally"
                ],
                "key_formulas": {
                    "Fixed OH Rate": "Total Fixed Mfg OH / Units PRODUCED",
                    "Absorption Unit Cost": "DM + DL + Var OH + Fixed OH Rate",
                    "Variable Unit Cost": "DM + DL + Variable OH",
                    "Reconciliation": "Variable Income + Fixed OH in Ending Inv − Fixed OH in Beg Inv = Absorption Income",
                    "Income Difference": "Inventory Change (units) × Fixed OH Rate per Unit"
                },
                "exam_tips": [
                    "Fixed OH rate uses units PRODUCED (not sold)",
                    "Contribution Margin appears on VARIABLE costing statement; Gross Margin on ABSORPTION",
                    "If Production = Sales → Both methods give EQUAL income"
                ]
            },
            8: {
                "overview": "Budgeting is the financial expression of management's plans. The master budget flows top-down starting from the sales forecast.",
                "key_concepts": [
                    "Sales Budget is ALWAYS first — everything else depends on it",
                    "Production = Sales + Desired End FG Inv − Beginning FG Inv",
                    "DM Purchases = Production Needs + End RM Inv − Beg RM Inv",
                    "Cash Budget reveals future borrowing needs BEFORE they occur",
                    "Flexible budget adjusts to actual activity — better for performance evaluation"
                ],
                "key_formulas": {
                    "Production Budget": "Sales + Desired End FG Inv − Beginning FG Inv",
                    "DM Purchases": "(Prod Needs + End RM Inv − Beg RM Inv) × Cost per unit",
                    "DL Cost": "Production × DLH per unit × Rate per hour",
                    "Cash Available": "Beginning Cash + All Cash Receipts",
                    "Ending Cash": "Cash Available − Disbursements ± Financing"
                },
                "exam_tips": [
                    "Sales Budget → Production → Materials → Labor → OH → Cash → Income Statement",
                    "Ending inventory policy links budget periods together",
                    "Cash budget deals with CASH flows — not accrual revenues and expenses"
                ]
            },
            9: {
                "overview": "Variance analysis is management by exception — identify where actual costs differ from standards and investigate significant gaps.",
                "key_concepts": [
                    "Favorable (F): Actual < Standard; Unfavorable (U): Actual > Standard",
                    "Standard Qty Allowed / Standard Hrs Allowed = Standard per unit × ACTUAL units produced",
                    "DM Price Variance uses AQ PURCHASED; Quantity Variance uses AQ USED",
                    "DL Rate Variance uses Actual Hours; Efficiency Variance compares AH vs SH Allowed",
                    "FOH Volume Variance: produced more or less than denominator volume"
                ],
                "key_formulas": {
                    "DM Price Variance": "(AP − SP) × AQ Purchased",
                    "DM Quantity Variance": "(AQ Used − SQ Allowed) × SP",
                    "DL Rate Variance": "(AR − SR) × AH Worked",
                    "DL Efficiency Variance": "(AH Worked − SH Allowed) × SR",
                    "VOH Spending Variance": "Actual VOH − (AH × Standard Rate)",
                    "VOH Efficiency Variance": "(AH − SH Allowed) × Standard VOH Rate",
                    "FOH Budget Variance": "Actual FOH − Budgeted FOH",
                    "FOH Volume Variance": "Budgeted FOH − Applied FOH"
                },
                "exam_tips": [
                    "SQ/SH Allowed is ALWAYS based on ACTUAL production, not budgeted",
                    "Price variance = purchasing decision; Quantity variance = production decision",
                    "F variance is always: actual cost < standard cost"
                ]
            },
            10: {
                "overview": "Responsibility accounting holds managers accountable for what they control. ROI, RI, and EVA measure investment center performance.",
                "key_concepts": [
                    "Cost Center: costs only; Revenue Center: revenues only; Profit: both; Investment: + assets",
                    "Segment Margin = CM − Traceable Fixed Costs (key performance metric)",
                    "Common fixed costs are irrelevant to drop/keep decisions",
                    "RI avoids ROI rejection problem: managers always accept projects with positive RI",
                    "Transfer price range: Min (seller's variable cost + opp cost) to Max (buyer's market price)"
                ],
                "key_formulas": {
                    "ROI": "NOI / Average Operating Assets",
                    "Margin": "NOI / Sales",
                    "Asset Turnover": "Sales / Average Operating Assets",
                    "ROI (DuPont)": "Margin × Asset Turnover",
                    "Residual Income": "NOI − (Required Return % × Average Operating Assets)",
                    "EVA": "After-Tax NOPAT − (WACC × Total Capital Employed)",
                    "Min Transfer Price": "Seller's Variable Cost + Opportunity Cost"
                },
                "exam_tips": [
                    "RI is better than ROI for investment decisions — no rejection problem",
                    "Traceable costs: disappear if segment dropped. Common: stay regardless",
                    "Always use CONTRIBUTION approach for segment reporting, not full-cost absorption"
                ]
            },
            11: {
                "overview": "Short-term decisions require differential analysis — only consider costs and revenues that CHANGE between alternatives.",
                "key_concepts": [
                    "Sunk costs: NEVER relevant; Opportunity costs: ALWAYS relevant",
                    "Special orders: fixed OH irrelevant if excess capacity exists",
                    "Make or Buy: only variable costs + AVOIDABLE fixed costs are relevant",
                    "Drop segment: keep if CM > Avoidable Fixed Costs",
                    "Product mix constraint: rank by CM per UNIT OF SCARCE RESOURCE"
                ],
                "key_formulas": {
                    "Special Order Net Benefit": "Order Revenue − Variable Costs − Opportunity Costs − Special Fixed Costs",
                    "Make vs Buy": "Compare total relevant cost to make vs purchase price",
                    "Drop Decision": "CM Lost vs Avoidable Fixed Costs Saved",
                    "CM per Scarce Resource": "CM per Unit / Units of Scarce Resource Required",
                    "Process Further Net Benefit": "(Final Price − Split-off Price) × Units − Separable Costs"
                },
                "exam_tips": [
                    "Fixed costs ONLY relevant if they can be AVOIDED by the decision",
                    "Rank products by CM per CONSTRAINT unit (not total CM or CM per product unit)",
                    "Joint costs are sunk in sell-or-process-further — use only in Module 6 NRV method"
                ]
            },
            12: {
                "overview": "Capital budgeting evaluates long-term investments. NPV is the gold standard — it measures real value added in dollar terms.",
                "key_concepts": [
                    "Time value of money: $1 today > $1 in the future",
                    "NPV > 0: Accept; NPV < 0: Reject; Higher NPV = better project",
                    "IRR: discount rate making NPV = 0; Accept if IRR > required return",
                    "For mutually exclusive projects: ALWAYS use NPV (not IRR)",
                    "Depreciation Tax Shield = Depreciation × Tax Rate (increases annual CF)"
                ],
                "key_formulas": {
                    "PV Factor": "1 / (1 + r)^n",
                    "PV Annuity Factor": "[1 − (1+r)^−n] / r",
                    "NPV": "Σ [CFt / (1+r)^t] − Initial Investment",
                    "Payback Period": "Initial Investment / Annual CF (equal flows)",
                    "Profitability Index": "PV of Future CFs / Initial Investment",
                    "Annual After-Tax CF": "Pre-Tax CF × (1 − Tax Rate) + (Depreciation × Tax Rate)",
                    "Depreciation Tax Shield": "Annual Depreciation × Tax Rate",
                    "After-Tax Salvage": "Salvage − (Salvage − Book Value) × Tax Rate"
                },
                "exam_tips": [
                    "Always use AFTER-TAX cash flows (not income) for NPV/IRR",
                    "Depreciation tax shield is a CASH benefit — add it back to after-tax operating CF",
                    "For mutually exclusive projects: if NPV and IRR conflict → USE NPV"
                ]
            },
            13: {
                "overview": "Pricing can start from cost (cost-plus) or from the market (target costing). Target costing works backwards to engineer costs to meet market demands.",
                "key_concepts": [
                    "Cost-Plus: Start with cost, add markup to get price",
                    "Target Costing: Start with market price, subtract required profit → allowable cost",
                    "Value Engineering: reduce costs while maintaining customer value",
                    "80% Rule: 80% of life-cycle costs locked in at design stage",
                    "Kaizen: continuous improvement of existing products (vs target = new products)"
                ],
                "key_formulas": {
                    "Absorption Cost-Plus Price": "Absorption Cost × (1 + Markup %)",
                    "Target Cost": "Target Selling Price − Target Profit Margin",
                    "Required Markup $": "Required Return + S&A Expenses",
                    "Markup % on Mfg Cost": "Required Markup / (Volume × Unit Mfg Cost) × 100",
                    "Time & Materials Rate": "Hourly Wage + OH per Hour + Profit per Hour",
                    "CLV": "Annual Margin / (1 + Discount Rate − Retention Rate)"
                },
                "exam_tips": [
                    "Target cost is a ceiling — engineering must bring actual costs DOWN to meet it",
                    "Kaizen = continuous improvement of EXISTING products (already in production)",
                    "80% rule: design decisions are most critical — costs locked in early!"
                ]
            },
            14: {
                "overview": "Quality has four cost categories. Prevention is cheapest in the long run. Lean eliminates waste. Six Sigma achieves near-perfect quality.",
                "key_concepts": [
                    "Prevention: stop defects before they occur (most valuable!)",
                    "Appraisal: detect defects before customer receives product",
                    "Internal Failure: defects found BEFORE delivery (scrap, rework)",
                    "External Failure: defects found AFTER delivery (warranty, returns, lost goodwill)",
                    "Six Sigma: 3.4 DPMO; DMAIC framework for improvement projects",
                    "8 Wastes (TIMWOODS): Transportation, Inventory, Motion, Waiting, Overproduction, Over-processing, Defects, Skills"
                ],
                "key_formulas": {
                    "DPMO": "(Defects / Total Opportunities) × 1,000,000",
                    "Process Efficiency": "Value-Added Time / Total Lead Time × 100",
                    "Total COQ": "Prevention + Appraisal + Internal Failure + External Failure",
                    "Conformance Costs": "Prevention + Appraisal",
                    "Non-Conformance Costs": "Internal Failure + External Failure",
                    "OEE": "Availability × Performance × Quality"
                },
                "exam_tips": [
                    "Invest more in PREVENTION — reduces failure costs by much more than the investment",
                    "DMAIC: Define, Measure, Analyze, Improve, Control",
                    "JIT = PULL system; Traditional = PUSH system"
                ]
            },
            15: {
                "overview": "Strategic Management Accounting bridges accounting and strategy — using financial tools to build and sustain competitive advantage.",
                "key_concepts": [
                    "SMA integrates external competitive data into management accounting",
                    "Porter's strategies: Cost Leadership, Differentiation, Focus",
                    "Value chain: map all activities creating value; compare with competitors",
                    "CLV:CAC ratio > 3:1 is healthy; < 1:1 means losing money on customers",
                    "Triple Bottom Line: People, Planet, Profit",
                    "Analytics levels: Descriptive → Diagnostic → Predictive → Prescriptive"
                ],
                "key_formulas": {
                    "CLV (simplified)": "Annual Margin / (1 + Discount Rate − Retention Rate)",
                    "CLV:CAC Ratio": "CLV / Customer Acquisition Cost",
                    "Carbon Footprint": "Σ (Activity Level × Emission Factor)",
                    "Carbon Cost": "Total CO₂ tonnes × Carbon Price per tonne",
                    "Benchmarking Gap %": "(Our Value − Best in Class) / Best in Class × 100",
                    "Value Chain Position": "Σ (Competitor Cost − Our Cost) for all activities"
                },
                "exam_tips": [
                    "CLV:CAC ratio < 1 = company destroying value on customer acquisition",
                    "Value chain analysis: find where YOU have cost or value advantage over competitors",
                    "Prescriptive analytics = highest value — it tells you WHAT TO DO, not just what happened"
                ]
            }
        }

        s = summaries[mod_num]

        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown(f"**{s['overview']}**")
            st.markdown("### 🔑 Key Concepts:")
            for concept in s["key_concepts"]:
                st.markdown(f"- {concept}")

        with col2:
            st.markdown("### 🧮 Key Formulas:")
            for formula_name, formula_expr in s["key_formulas"].items():
                st.markdown(f"**{formula_name}:**")
                st.code(formula_expr)

        st.markdown("### 💡 Exam Tips:")
        for tip in s["exam_tips"]:
            st.info(f"💡 {tip}")

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("🧮 Complete Formula Bank")
        st.markdown("Every important formula across all 15 modules — your ultimate quick reference.")

        formula_category = st.selectbox("Filter by Category:", [
            "All Formulas",
            "Module 1-2: Foundations & CVP",
            "Module 3-5: Costing Systems",
            "Module 6-7: Allocation & Reporting",
            "Module 8-9: Budgeting & Standards",
            "Module 10-11: Performance & Decisions",
            "Module 12-13: Capital & Pricing",
            "Module 14-15: Quality & Strategy"
        ])

        all_formulas = [
            # Module 1
            {"Module": 1, "Topic": "Product Cost", "Formula Name": "Total Product Cost", "Formula": "Direct Materials + Direct Labor + Manufacturing Overhead", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 1, "Topic": "Cost of Goods Sold", "Formula Name": "COGS", "Formula": "Beginning Inventory + Product Costs − Ending Inventory", "Category": "Module 1-2: Foundations & CVP"},
            # Module 2
            {"Module": 2, "Topic": "CVP", "Formula Name": "Contribution Margin", "Formula": "Sales Revenue − All Variable Costs", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 2, "Topic": "CVP", "Formula Name": "CM Ratio", "Formula": "CM / Sales Revenue × 100", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 2, "Topic": "CVP", "Formula Name": "Break-Even (Units)", "Formula": "Fixed Costs / CM per Unit", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 2, "Topic": "CVP", "Formula Name": "Break-Even ($)", "Formula": "Fixed Costs / CM Ratio", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 2, "Topic": "CVP", "Formula Name": "Target Profit (Units)", "Formula": "(Fixed Costs + Target Profit) / CM per Unit", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 2, "Topic": "CVP", "Formula Name": "Margin of Safety %", "Formula": "(Actual Sales − BEP Sales) / Actual Sales × 100", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 2, "Topic": "CVP", "Formula Name": "Degree of Operating Leverage", "Formula": "Contribution Margin / Net Operating Income", "Category": "Module 1-2: Foundations & CVP"},
            {"Module": 2, "Topic": "CVP", "Formula Name": "High-Low Variable Rate", "Formula": "(High Cost − Low Cost) / (High Activity − Low Activity)", "Category": "Module 1-2: Foundations & CVP"},
            # Module 3
            {"Module": 3, "Topic": "Job Order", "Formula Name": "Predetermined OH Rate", "Formula": "Estimated Total Mfg OH / Estimated Allocation Base", "Category": "Module 3-5: Costing Systems"},
            {"Module": 3, "Topic": "Job Order", "Formula Name": "Applied Overhead", "Formula": "POHR × Actual Allocation Base", "Category": "Module 3-5: Costing Systems"},
            {"Module": 3, "Topic": "Job Order", "Formula Name": "Total Job Cost", "Formula": "Direct Materials + Direct Labor + Applied Overhead", "Category": "Module 3-5: Costing Systems"},
            {"Module": 3, "Topic": "Job Order", "Formula Name": "Under/Overapplied OH", "Formula": "Actual OH − Applied OH (positive = underapplied)", "Category": "Module 3-5: Costing Systems"},
            # Module 4
            {"Module": 4, "Topic": "Process Costing", "Formula Name": "Physical Flow", "Formula": "Beg WIP + Started = Completed + Ending WIP", "Category": "Module 3-5: Costing Systems"},
            {"Module": 4, "Topic": "Process Costing", "Formula Name": "EUP (Weighted Avg)", "Formula": "Completed + (Ending WIP × % Complete)", "Category": "Module 3-5: Costing Systems"},
            {"Module": 4, "Topic": "Process Costing", "Formula Name": "EUP (FIFO)", "Formula": "Beg WIP×(1−%) + Started&Completed + Ending WIP×%", "Category": "Module 3-5: Costing Systems"},
            {"Module": 4, "Topic": "Process Costing", "Formula Name": "Cost per EUP (WA)", "Formula": "(Beg WIP Cost + Current Period Cost) / EUP", "Category": "Module 3-5: Costing Systems"},
            # Module 5
            {"Module": 5, "Topic": "ABC", "Formula Name": "Activity Rate", "Formula": "Total Activity Cost / Total Driver Quantity", "Category": "Module 3-5: Costing Systems"},
            {"Module": 5, "Topic": "ABC", "Formula Name": "Product OH (ABC)", "Formula": "Σ (Activity Rate × Product's Driver Usage)", "Category": "Module 3-5: Costing Systems"},
            # Module 6
            {"Module": 6, "Topic": "Joint Products", "Formula Name": "NRV", "Formula": "Final Sales Value − Separable Costs", "Category": "Module 6-7: Allocation & Reporting"},
            {"Module": 6, "Topic": "Joint Products", "Formula Name": "Sales Value Allocation %", "Formula": "Product Sales Value / Total Sales Value × Joint Costs", "Category": "Module 6-7: Allocation & Reporting"},
            {"Module": 6, "Topic": "Joint Products", "Formula Name": "Process Further Net Benefit", "Formula": "(Final Price − Split-off Price) × Units − Separable Costs", "Category": "Module 6-7: Allocation & Reporting"},
            # Module 7
            {"Module": 7, "Topic": "Absorption/Variable", "Formula Name": "Fixed OH Rate per Unit", "Formula": "Total Fixed Mfg OH / Units PRODUCED", "Category": "Module 6-7: Allocation & Reporting"},
            {"Module": 7, "Topic": "Absorption/Variable", "Formula Name": "Absorption Unit Cost", "Formula": "DM + DL + Var OH + Fixed OH Rate per Unit", "Category": "Module 6-7: Allocation & Reporting"},
            {"Module": 7, "Topic": "Absorption/Variable", "Formula Name": "Income Reconciliation", "Formula": "Var Income + Fixed OH in End Inv − Fixed OH in Beg Inv = Absorption Income", "Category": "Module 6-7: Allocation & Reporting"},
            {"Module": 7, "Topic": "Absorption/Variable", "Formula Name": "Income Difference (shortcut)", "Formula": "Inventory Change (units) × Fixed OH Rate per Unit", "Category": "Module 6-7: Allocation & Reporting"},
            # Module 8
            {"Module": 8, "Topic": "Budgeting", "Formula Name": "Production Budget", "Formula": "Sales + Desired End FG Inv − Beginning FG Inv", "Category": "Module 8-9: Budgeting & Standards"},
            {"Module": 8, "Topic": "Budgeting", "Formula Name": "DM Purchases", "Formula": "(Prod Needs + End RM Inv − Beg RM Inv) × Cost per unit", "Category": "Module 8-9: Budgeting & Standards"},
            {"Module": 8, "Topic": "Budgeting", "Formula Name": "Direct Labor Cost", "Formula": "Production × DLH per unit × Labor Rate per hour", "Category": "Module 8-9: Budgeting & Standards"},
            {"Module": 8, "Topic": "Budgeting", "Formula Name": "Total Cash Available", "Formula": "Beginning Cash Balance + All Cash Receipts", "Category": "Module 8-9: Budgeting & Standards"},
            # Module 9
            {"Module": 9, "Topic": "Variances", "Formula Name": "DM Price Variance", "Formula": "(AP − SP) × AQ Purchased", "Category": "Module 8-9: Budgeting & Standards"},
            {"Module": 9, "Topic": "Variances", "Formula Name": "DM Quantity Variance", "Formula": "(AQ Used − SQ Allowed) × SP", "Category": "Module 8-9: Budgeting & Standards"},
            {"Module": 9, "Topic": "Variances", "Formula Name": "DL Rate Variance", "Formula": "(AR − SR) × Actual Hours Worked", "Category": "Module 8-9: Budgeting & Standards"},
            {"Module": 9, "Topic": "Variances", "Formula Name": "DL Efficiency Variance", "Formula": "(Actual Hours − SH Allowed) × Standard Rate", "Category": "Module 8-9: Budgeting & Standards"},
            {"Module": 9, "Topic": "Variances", "Formula Name": "Standard Qty/Hrs Allowed", "Formula": "Standard per Unit × Actual Units PRODUCED", "Category": "Module 8-9: Budgeting & Standards"},
            # Module 10
            {"Module": 10, "Topic": "Performance", "Formula Name": "ROI", "Formula": "Net Operating Income / Average Operating Assets", "Category": "Module 10-11: Performance & Decisions"},
            {"Module": 10, "Topic": "Performance", "Formula Name": "Margin", "Formula": "Net Operating Income / Sales", "Category": "Module 10-11: Performance & Decisions"},
            {"Module": 10, "Topic": "Performance", "Formula Name": "Asset Turnover", "Formula": "Sales / Average Operating Assets", "Category": "Module 10-11: Performance & Decisions"},
            {"Module": 10, "Topic": "Performance", "Formula Name": "ROI (DuPont)", "Formula": "Margin × Asset Turnover", "Category": "Module 10-11: Performance & Decisions"},
            {"Module": 10, "Topic": "Performance", "Formula Name": "Residual Income", "Formula": "NOI − (Required Return % × Average Operating Assets)", "Category": "Module 10-11: Performance & Decisions"},
            {"Module": 10, "Topic": "Performance", "Formula Name": "EVA", "Formula": "After-Tax NOPAT − (WACC × Total Capital Employed)", "Category": "Module 10-11: Performance & Decisions"},
            {"Module": 10, "Topic": "Transfer Pricing", "Formula Name": "Min Transfer Price", "Formula": "Selling Division Variable Cost + Opportunity Cost", "Category": "Module 10-11: Performance & Decisions"},
            # Module 11
            {"Module": 11, "Topic": "Decisions", "Formula Name": "CM per Scarce Resource", "Formula": "CM per Unit / Units of Scarce Resource Required", "Category": "Module 10-11: Performance & Decisions"},
            {"Module": 11, "Topic": "Decisions", "Formula Name": "Drop Decision Net Impact", "Formula": "−CM Lost + Avoidable Fixed Saved − Lost CM from Other Segments", "Category": "Module 10-11: Performance & Decisions"},
            # Module 12
            {"Module": 12, "Topic": "Capital Budgeting", "Formula Name": "NPV", "Formula": "Σ [CFt / (1+r)^t] − Initial Investment", "Category": "Module 12-13: Capital & Pricing"},
            {"Module": 12, "Topic": "Capital Budgeting", "Formula Name": "PV Annuity Factor", "Formula": "[1 − (1+r)^−n] / r", "Category": "Module 12-13: Capital & Pricing"},
            {"Module": 12, "Topic": "Capital Budgeting", "Formula Name": "Profitability Index", "Formula": "PV of Future Cash Flows / Initial Investment", "Category": "Module 12-13: Capital & Pricing"},
            {"Module": 12, "Topic": "Capital Budgeting", "Formula Name": "Annual After-Tax CF", "Formula": "Pre-Tax CF × (1 − Tax Rate) + (Depreciation × Tax Rate)", "Category": "Module 12-13: Capital & Pricing"},
            {"Module": 12, "Topic": "Capital Budgeting", "Formula Name": "Depreciation Tax Shield", "Formula": "Annual Depreciation × Tax Rate", "Category": "Module 12-13: Capital & Pricing"},
            {"Module": 12, "Topic": "Capital Budgeting", "Formula Name": "Payback Period", "Formula": "Initial Investment / Annual CF (for equal cash flows)", "Category": "Module 12-13: Capital & Pricing"},
            # Module 13
            {"Module": 13, "Topic": "Pricing", "Formula Name": "Target Cost", "Formula": "Target Selling Price − Target Profit Margin", "Category": "Module 12-13: Capital & Pricing"},
            {"Module": 13, "Topic": "Pricing", "Formula Name": "Absorption Cost-Plus Price", "Formula": "Absorption Unit Cost × (1 + Markup %)", "Category": "Module 12-13: Capital & Pricing"},
            {"Module": 13, "Topic": "Pricing", "Formula Name": "Required Markup %", "Formula": "Required Markup $ / (Volume × Unit Mfg Cost) × 100", "Category": "Module 12-13: Capital & Pricing"},
            # Module 14
            {"Module": 14, "Topic": "Quality", "Formula Name": "Total COQ", "Formula": "Prevention + Appraisal + Internal Failure + External Failure", "Category": "Module 14-15: Quality & Strategy"},
            {"Module": 14, "Topic": "Quality", "Formula Name": "DPMO", "Formula": "(Defects / Total Opportunities) × 1,000,000", "Category": "Module 14-15: Quality & Strategy"},
            {"Module": 14, "Topic": "Quality", "Formula Name": "Process Efficiency", "Formula": "Value-Added Time / Total Lead Time × 100", "Category": "Module 14-15: Quality & Strategy"},
            # Module 15
            {"Module": 15, "Topic": "Strategy", "Formula Name": "Customer Lifetime Value", "Formula": "Annual Margin / (1 + Discount Rate − Retention Rate)", "Category": "Module 14-15: Quality & Strategy"},
            {"Module": 15, "Topic": "Strategy", "Formula Name": "CLV:CAC Ratio", "Formula": "CLV / Customer Acquisition Cost (target: > 3:1)", "Category": "Module 14-15: Quality & Strategy"},
            {"Module": 15, "Topic": "Strategy", "Formula Name": "Carbon Footprint", "Formula": "Σ (Activity Level × Emission Factor) for all sources", "Category": "Module 14-15: Quality & Strategy"},
            {"Module": 15, "Topic": "Strategy", "Formula Name": "Carbon Cost", "Formula": "Total CO₂ Tonnes × Carbon Price per Tonne", "Category": "Module 14-15: Quality & Strategy"},
        ]

        formula_df = pd.DataFrame(all_formulas)

        if formula_category != "All Formulas":
            formula_df = formula_df[formula_df["Category"] == formula_category]

        search_term = st.text_input("🔍 Search formulas:", placeholder="Type a keyword (e.g., NPV, variance, break-even)...")
        if search_term:
            mask = formula_df.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)
            formula_df = formula_df[mask]

        display_df = formula_df[["Module", "Topic", "Formula Name", "Formula"]].copy()
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        st.info(f"Showing {len(display_df)} formulas. Total in bank: {len(all_formulas)}")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("📊 Visual Learning Dashboard")

        st.subheader("Course Structure — Topic Relationships")

        fig_treemap = go.Figure(go.Treemap(
            labels=["Managerial Accounting", "Foundations", "Costing Systems", "Planning & Control", "Decisions & Strategy",
                    "M1: Foundations", "M2: CVP", "M3: Job Order", "M4: Process", "M5: ABC",
                    "M6: Allocation", "M7: Absorption", "M8: Budgeting", "M9: Variances",
                    "M10: Performance", "M11: Relevant Costs", "M12: Capital", "M13: Pricing",
                    "M14: Quality", "M15: Strategy"],
            parents=["", "Managerial Accounting", "Managerial Accounting", "Managerial Accounting", "Managerial Accounting",
                     "Foundations", "Foundations", "Costing Systems", "Costing Systems", "Costing Systems",
                     "Costing Systems", "Costing Systems", "Planning & Control", "Planning & Control",
                     "Planning & Control", "Decisions & Strategy", "Decisions & Strategy", "Decisions & Strategy",
                     "Decisions & Strategy", "Decisions & Strategy"],
            values=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            marker=dict(colorscale="Blues")
        ))
        fig_treemap.update_layout(title="Course Module Structure", height=500)
        st.plotly_chart(fig_treemap, use_container_width=True)

        st.subheader("Module Difficulty Progression")
        difficulty_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3, "Expert": 4}
        diff_values = [difficulty_map[m["difficulty"]] for m in modules_info]
        diff_colors = [m["color"] for m in modules_info]

        fig_diff = go.Figure(go.Scatter(
            x=list(range(1, 16)),
            y=diff_values,
            mode="lines+markers+text",
            line=dict(color="#2E86C1", width=3),
            marker=dict(size=18, color=diff_colors),
            text=[f"M{m['num']}" for m in modules_info],
            textposition="middle center",
            textfont=dict(color="white", size=10)
        ))
        fig_diff.update_layout(
            title="Difficulty Progression Across 15 Modules",
            xaxis_title="Module Number",
            yaxis=dict(tickvals=[1, 2, 3, 4], ticktext=["Beginner", "Intermediate", "Advanced", "Expert"]),
            hovermode="x unified"
        )
        fig_diff.add_hrect(y0=0.5, y1=1.5, fillcolor="green", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=1.5, y1=2.5, fillcolor="yellow", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=2.5, y1=3.5, fillcolor="orange", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=3.5, y1=4.5, fillcolor="red", opacity=0.1, line_width=0)
        st.plotly_chart(fig_diff, use_container_width=True)

        st.subheader("Key Skills Radar — What You Learn")
        skill_categories = ["Cost Classification", "Financial Analysis", "Decision Making",
                             "Strategic Thinking", "Quantitative Methods", "Reporting & Control"]
        skill_scores = [10, 9, 9, 8, 9, 9]
        skill_scores_append = skill_scores + [skill_scores[0]]
        categories_append = skill_categories + [skill_categories[0]]

        fig_radar = go.Figure(go.Scatterpolar(
            r=skill_scores_append,
            theta=categories_append,
            fill="toself",
            name="Skills Covered",
            line=dict(color="#2E86C1", width=3),
            fillcolor="rgba(46,134,193,0.3)"
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False,
            title="Skills Developed — All 15 Modules Combined"
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        st.subheader("Module Topic Coverage Map")
        topics_all = [m["topics"] for m in modules_info]
        all_topics_flat = [f"M{m['num']}: {t}" for m in modules_info for t in m["topics"]]
        topic_modules = [m["num"] for m in modules_info for _ in m["topics"]]

        fig_topics = go.Figure(go.Bar(
            x=[f"M{m['num']}" for m in modules_info],
            y=[len(m["topics"]) for m in modules_info],
            marker_color=[m["color"] for m in modules_info],
            text=[f"{len(m['topics'])} topics" for m in modules_info],
            textposition="auto"
        ))
        fig_topics.update_layout(
            title="Topics per Module", xaxis_title="Module", yaxis_title="Number of Major Topics"
        )
        st.plotly_chart(fig_topics, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("✅ Master Quiz — All 15 Modules")
        st.markdown("Test your knowledge across the entire course with this comprehensive quiz!")

        quiz_mode = st.radio("Quiz Mode:", ["Quick Fire (5 questions)", "Standard (10 questions)", "Full Exam (15 questions)"], horizontal=True)
        num_q = {"Quick Fire (5 questions)": 5, "Standard (10 questions)": 10, "Full Exam (15 questions)": 15}[quiz_mode]

        all_quiz_questions = [
            {"q": "Which of the following is a PRODUCT cost?", "opts": ["Sales commission", "CEO salary", "Factory rent", "Advertising expense"], "ans": "Factory rent", "mod": 1, "exp": "Factory rent is a manufacturing overhead cost → product cost inventoried until sold."},
            {"q": "If Fixed Costs = $90,000 and CM per unit = $15, the Break-Even Point in units is:", "opts": ["4,500 units", "6,000 units", "7,500 units", "9,000 units"], "ans": "6,000 units", "mod": 2, "exp": "BEP = $90,000 / $15 = 6,000 units."},
            {"q": "Predetermined Overhead Rate is calculated using:", "opts": ["Actual costs and actual base", "Estimated costs and estimated base", "Actual costs and estimated base", "Standard costs only"], "ans": "Estimated costs and estimated base", "mod": 3, "exp": "POHR = Estimated Total OH / Estimated Allocation Base — both are estimates made BEFORE the period."},
            {"q": "Under FIFO process costing, the cost per EUP is based on:", "opts": ["All costs (prior + current)", "Current period costs ONLY", "Prior period costs only", "Average of all years"], "ans": "Current period costs ONLY", "mod": 4, "exp": "FIFO isolates current period costs to give a pure current-period cost per EUP."},
            {"q": "A machine setup is which level in the ABC cost hierarchy?", "opts": ["Unit-level", "Batch-level", "Product-level", "Facility-level"], "ans": "Batch-level", "mod": 5, "exp": "Setups occur once per batch/production run, making them batch-level activities."},
            {"q": "Joint costs in a sell-or-process-further decision are:", "opts": ["Always relevant", "Irrelevant — they are sunk costs", "Differential costs", "Avoidable costs"], "ans": "Irrelevant — they are sunk costs", "mod": 6, "exp": "Joint costs are incurred before the split-off point regardless of what you do — completely irrelevant to the decision."},
            {"q": "When Production > Sales, absorption costing income is:", "opts": ["Equal to variable costing income", "Lower than variable costing income", "Higher than variable costing income", "Cannot be determined"], "ans": "Higher than variable costing income", "mod": 7, "exp": "Inventory increases, fixed OH is deferred in ending inventory under absorption → absorption income is higher."},
            {"q": "The FIRST budget prepared in the master budget process is:", "opts": ["Production budget", "Cash budget", "Sales budget", "Manufacturing overhead budget"], "ans": "Sales budget", "mod": 8, "exp": "Everything flows from the sales forecast — the sales budget is ALWAYS prepared first."},
            {"q": "The DM Quantity Variance formula is:", "opts": ["(AP-SP) × AQ Purchased", "(AQ Used - SQ Allowed) × SP", "(AR-SR) × AH", "(AH-SH) × SR"], "ans": "(AQ Used - SQ Allowed) × SP", "mod": 9, "exp": "MQV = (AQ Used − SQ Allowed) × Standard Price. SQ Allowed = Standard qty/unit × Actual units produced."},
            {"q": "Residual Income is BETTER than ROI for investment decisions because:", "opts": ["It is simpler to calculate", "It prevents managers from rejecting value-adding projects that dilute their ROI", "It is higher than ROI", "It uses WACC"], "ans": "It prevents managers from rejecting value-adding projects that dilute their ROI", "mod": 10, "exp": "RI avoids the ROI rejection problem — a manager always accepts a project if it adds positive RI, regardless of existing ROI."},
            {"q": "A sunk cost is:", "opts": ["Always relevant to decisions", "A future cost that differs between alternatives", "A cost already incurred that cannot be changed", "An opportunity cost"], "ans": "A cost already incurred that cannot be changed", "mod": 11, "exp": "Sunk costs are past costs — NEVER relevant to any future decision."},
            {"q": "NPV > 0 means:", "opts": ["Reject the project", "Project earns exactly the required return", "Project creates value above the required return — ACCEPT", "IRR equals cost of capital"], "ans": "Project creates value above the required return — ACCEPT", "mod": 12, "exp": "NPV > 0 means the PV of inflows exceeds the investment — the project adds economic value."},
            {"q": "Target Cost is calculated as:", "opts": ["Manufacturing cost plus markup", "Target Price minus Required Profit", "Variable cost only", "Full absorption cost"], "ans": "Target Price minus Required Profit", "mod": 13, "exp": "Target Cost = Target Selling Price − Required Profit Margin. Work backwards from market!"},
            {"q": "Six Sigma achieves approximately:", "opts": ["Zero defects", "3.4 defects per million opportunities", "3.4% defect rate", "34 defects per thousand"], "ans": "3.4 defects per million opportunities", "mod": 14, "exp": "Six Sigma = 3.4 DPMO — near-perfect quality with only 3.4 defects per million opportunities."},
            {"q": "Customer Lifetime Value (simplified) = Annual Margin ÷ ?", "opts": ["Discount Rate", "1 + Discount Rate − Retention Rate", "Retention Rate", "1 − Discount Rate"], "ans": "1 + Discount Rate − Retention Rate", "mod": 15, "exp": "CLV = Annual Margin / (1 + Discount Rate − Retention Rate). Higher retention = much higher CLV!"},
        ]

        selected_questions = all_quiz_questions[:num_q]

        if "quiz_score" not in st.session_state:
            st.session_state.quiz_score = 0
        if "quiz_submitted" not in st.session_state:
            st.session_state.quiz_submitted = {}

        score = 0
        for idx, q in enumerate(selected_questions):
            st.markdown(f"---")
            st.markdown(f"**Q{idx+1}. [Module {q['mod']}] {q['q']}**")
            answer = st.radio("", q["opts"], key=f"mq_{idx}")

            if st.button(f"Check Answer Q{idx+1}", key=f"mqc_{idx}"):
                if answer == q["ans"]:
                    st.success(f"✅ Correct! {q['exp']}")
                    st.session_state.quiz_submitted[idx] = True
                else:
                    st.error(f"❌ Incorrect. The correct answer is: **{q['ans']}**")
                    st.info(f"💡 Explanation: {q['exp']}")
                    st.session_state.quiz_submitted[idx] = False

        st.markdown("---")
        answered = len(st.session_state.quiz_submitted)
        correct = sum(1 for v in st.session_state.quiz_submitted.values() if v)
        if answered > 0:
            pct = correct / answered * 100
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Questions Answered", f"{answered}/{num_q}")
            with col2: st.metric("Correct Answers", f"{correct}")
            with col3: st.metric("Score", f"{pct:.0f}%")

            if pct >= 90:
                st.success("🏆 Outstanding! You have expert-level knowledge!")
            elif pct >= 75:
                st.info("✅ Great work! Good understanding across the course.")
            elif pct >= 60:
                st.warning("⚠️ Good progress! Review the modules where you made mistakes.")
            else:
                st.error("❌ Keep studying! Focus on the modules you found challenging.")

        if st.button("🔄 Reset Quiz"):
            st.session_state.quiz_submitted = {}
            st.rerun()

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("🎓 Study Planner & Progress Tracker")

        st.subheader("📅 Suggested Study Schedule")

        schedule_df = pd.DataFrame({
            "Week": ["Week 1", "Week 2", "Week 3-4", "Week 5-6", "Week 7", "Week 8-9", "Week 10", "Week 11-12", "Week 13", "Week 14"],
            "Modules": ["1-2", "3", "4-5", "6-7", "8", "9-10", "11", "12-13", "14-15", "All (Review)"],
            "Topics": [
                "Foundations, Cost Classification, CVP Analysis",
                "Job Order Costing",
                "Process Costing, Activity-Based Costing",
                "Cost Allocation, Variable vs Absorption Costing",
                "Master Budgeting",
                "Standard Costing & Variances, Responsibility Accounting",
                "Relevant Costs & Decision Making",
                "Capital Budgeting, Pricing & Target Costing",
                "Quality Management, Strategic Accounting",
                "Full review, practice exams"
            ],
            "Focus Activity": [
                "Read theory + calculator practice",
                "Build complete job cost sheets",
                "Production cost reports + ABC problems",
                "Service dept allocation + income reconciliation",
                "Build a complete master budget from scratch",
                "All 8 variances + ROI/RI/EVA problems",
                "Special order + make-or-buy + product mix",
                "NPV + after-tax CFs + cost-plus vs target costing",
                "COQ report + DMAIC + value chain analysis",
                "Timed practice questions across all 15 modules"
            ]
        })
        st.dataframe(schedule_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("✅ My Progress Tracker")
        st.markdown("Track your completion of each module:")

        progress_data = []
        total_completed = 0
        for mod in modules_info:
            col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
            with col1:
                st.markdown(f"**{mod['icon']} Module {mod['num']}: {mod['title']}**")
            with col2:
                completed = st.checkbox("Completed ✅", key=f"prog_done_{mod['num']}")
            with col3:
                practiced = st.checkbox("Practised 🧮", key=f"prog_prac_{mod['num']}")
            with col4:
                confidence = st.select_slider(
                    "Confidence", ["❓", "😰", "😐", "😊", "🌟"],
                    value="😐", key=f"prog_conf_{mod['num']}"
                )
            if completed:
                total_completed += 1
            progress_data.append({
                "Module": f"M{mod['num']}: {mod['title'][:30]}...",
                "Done": "✅" if completed else "⬜",
                "Practised": "🧮" if practiced else "⬜",
                "Confidence": confidence
            })

        overall_progress = total_completed / 15 * 100
        st.progress(overall_progress / 100)
        st.metric("Overall Progress", f"{total_completed}/15 modules ({overall_progress:.0f}%)")

        if total_completed == 15:
            st.success("🎉 🏆 Congratulations! You have completed all 15 modules of Managerial Accounting! You are ready for professional certification exams.")
            st.balloons()

        st.markdown("---")
        st.subheader("📌 Quick Reference — Top 10 Rules to Remember")

        rules = [
            ("1", "Sunk costs are ALWAYS irrelevant", "Never include past costs in future decisions", "M1, M11"),
            ("2", "Opportunity costs are ALWAYS relevant", "The benefit you give up must always be counted", "M11"),
            ("3", "Fixed OH rate = Total OH ÷ Units PRODUCED", "Not units sold — a classic exam trap!", "M7"),
            ("4", "BEP = Fixed Costs ÷ CM per Unit", "Not selling price, not total cost — CM per unit!", "M2"),
            ("5", "SQ/SH Allowed uses ACTUAL production", "Standard × Actual units produced — not budgeted units", "M9"),
            ("6", "NPV > 0 → Accept; Mutually exclusive → use NPV not IRR", "IRR can mislead for mutually exclusive projects", "M12"),
            ("7", "DM Price Variance uses AQ PURCHASED", "Quantity Variance uses AQ USED — different quantities!", "M9"),
            ("8", "Joint costs are sunk in sell-or-process-further", "Only consider separable costs and incremental revenue", "M6, M11"),
            ("9", "Target Cost = Target Price − Required Profit", "Work BACKWARDS from market — then engineer to cost", "M13"),
            ("10", "RI avoids ROI rejection problem", "Accept projects if RI positive — regardless of ROI dilution", "M10"),
        ]

        rules_df = pd.DataFrame(rules, columns=["#", "Rule", "Why It Matters", "Module(s)"])
        st.dataframe(rules_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔗 Module Connections — How Everything Links Together")
        st.markdown("""
        Understanding how modules connect deepens your mastery:

        | Connection | Link |
        |-----------|------|
        | **M1 → M7** | Cost classification drives absorption vs variable costing choice |
        | **M2 → M11** | CVP contribution margin = foundation for relevant cost decisions |
        | **M3 + M4 → M5** | Job and process costing limitations → why ABC was developed |
        | **M6 → M11** | Joint cost methods ↔ sell-or-process-further decisions |
        | **M8 → M9** | Master budget provides standards; variance analysis measures deviations |
        | **M9 → M10** | Variances → responsibility accounting → which manager to hold accountable |
        | **M11 → M12** | Relevant cost principles apply equally to short-term and capital decisions |
        | **M12 → M13** | Capital budgeting and pricing both require life-cycle cost thinking |
        | **M14 → M15** | Lean accounting and quality → strategic competitive advantage |
        | **M10 → M15** | ROI/EVA → segment profitability → customer lifetime value → strategy |
        """)

        st.success("🎓 Use this overview page as your constant companion throughout the course. Return to it for quick reference, formula lookup, progress tracking, and exam preparation!")

if __name__ == "__main__":
    show()