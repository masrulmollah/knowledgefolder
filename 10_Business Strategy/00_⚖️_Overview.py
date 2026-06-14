import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🎯 Business Strategy — Complete Course Overview")
    st.markdown("*Your comprehensive guide to all 12 modules — summaries, frameworks, formulas, and interactive review tools*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🗺️ Course Map", "📖 Module Summaries", "🧮 Formula Bank",
        "📊 Visual Dashboard", "✅ Master Quiz", "🎓 Study Planner"
    ])

    # ══════════════════════════════════════════════════════════════════
    modules_info = [
        {"num": 1, "title": "Foundations of Business Strategy",
         "icon": "🎯", "color": "#1B3A6B",
         "topics": ["Strategy vs tactics vs operations", "Three levels of strategy", "Schools of strategic thought", "Finance as strategic partner"],
         "key_skill": "Define strategy at all three levels and articulate the finance professional's strategic role",
         "difficulty": "Beginner"},

        {"num": 2, "title": "External Environment Analysis",
         "icon": "🌍", "color": "#2563EB",
         "topics": ["PESTLE macro analysis", "Porter's Five Forces", "Market sizing (TAM/SAM/SOM)", "Scenario planning"],
         "key_skill": "Conduct PESTLE and Five Forces analysis and translate external trends into financial assumptions",
         "difficulty": "Beginner"},

        {"num": 3, "title": "Internal Analysis & Competitive Advantage",
         "icon": "🔬", "color": "#0D7377",
         "topics": ["VRIN framework", "Porter's Value Chain", "Financial capabilities as strategic assets", "SWOT / TOWS analysis"],
         "key_skill": "Apply VRIN, map the value chain with cost analysis, and build a TOWS strategic options matrix",
         "difficulty": "Intermediate"},

        {"num": 4, "title": "Business-Level Strategy & Competitive Positioning",
         "icon": "⚔️", "color": "#7C3AED",
         "topics": ["Porter's generic strategies", "Strategy clock", "ROIC as strategy metric", "Competitive moats"],
         "key_skill": "Evaluate competitive strategy using ROIC, pricing power analysis, and moat identification",
         "difficulty": "Intermediate"},

        {"num": 5, "title": "Corporate Strategy: Growth, Portfolio & Diversification",
         "icon": "🏢", "color": "#D97706",
         "topics": ["Ansoff growth matrix", "BCG portfolio matrix", "M&A valuation & synergies", "Capital allocation framework"],
         "key_skill": "Analyse corporate portfolio, evaluate M&A synergies, and design capital allocation frameworks",
         "difficulty": "Intermediate"},

        {"num": 6, "title": "Innovation, Disruption & Digital Strategy",
         "icon": "💡", "color": "#059669",
         "topics": ["Types of innovation", "3-Horizon model", "Disruptive innovation (Christensen)", "Digital transformation ROI"],
         "key_skill": "Evaluate innovation investments with real options thinking and build digital transformation business cases",
         "difficulty": "Intermediate"},

        {"num": 7, "title": "Strategy & Financial Performance",
         "icon": "📊", "color": "#E74C3C",
         "topics": ["Value creation framework (EVA)", "Balanced Scorecard", "DuPont ROIC analysis", "Capital structure & FCF signals"],
         "key_skill": "Link strategy to financial value using EVA, DuPont decomposition, and Balanced Scorecard KPIs",
         "difficulty": "Advanced"},

        {"num": 8, "title": "Strategic Planning, Implementation & Change",
         "icon": "🗺️", "color": "#0EA5E9",
         "topics": ["Integrated planning calendar", "McKinsey 7-S Framework", "Kotter's 8-step change model", "Rolling forecasts"],
         "key_skill": "Design integrated strategic and financial planning processes and lead organisational change",
         "difficulty": "Advanced"},

        {"num": 9, "title": "Risk, Resilience & Strategic Decision-Making",
         "icon": "⚠️", "color": "#DC2626",
         "topics": ["Strategic risk register", "Decision trees & expected value", "Scenario stress testing", "Behavioural biases"],
         "key_skill": "Build risk registers, apply decision trees, run scenario stress tests, and design resilient organisations",
         "difficulty": "Advanced"},

        {"num": 10, "title": "Global Strategy, ESG & Stakeholder Value",
         "icon": "🌐", "color": "#7C3AED",
         "topics": ["Global vs multidomestic strategy", "CAGE distance framework", "ESG as strategic imperative", "Stakeholder value mapping"],
         "key_skill": "Design global entry strategies, integrate ESG into financial modelling, and build stakeholder value frameworks",
         "difficulty": "Advanced"},

        {"num": 11, "title": "Strategic Finance: FP&A, Scenario Modelling & Business Cases",
         "icon": "💰", "color": "#B45309",
         "topics": ["Strategic FP&A vs traditional budgeting", "Driver-based financial modelling", "Investment appraisal (NPV/IRR/Payback)", "Business case development"],
         "key_skill": "Build driver-based financial models, develop investment business cases, and design strategic management reporting",
         "difficulty": "Advanced"},

        {"num": 12, "title": "Capstone: Integrated Business Strategy Project",
         "icon": "🏆", "color": "#1B3A6B",
         "topics": ["Full strategic analysis (PESTLE, Five Forces, VRIN)", "Strategic options evaluation (SAFe)", "3-year financial plan & scenario analysis", "Boardroom strategy presentation"],
         "key_skill": "Deliver a complete strategic analysis and boardroom-ready financial plan demonstrating full programme mastery",
         "difficulty": "Expert"},
    ]

    difficulty_colors = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🟠", "Expert": "🔴"}

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("🗺️ Course Map — 12 Modules at a Glance")

        st.markdown("""
        ### Welcome to the Business Strategy Course for Finance Professionals
        This course transforms finance professionals from **financial scorekeepers into strategic co-pilots**
        who shape, challenge, and execute organisational strategy.
        Below is your complete learning roadmap across **12 comprehensive modules**.
        """)

        for row_start in range(0, len(modules_info), 3):
            cols = st.columns(3)
            for col_idx, mod in enumerate(modules_info[row_start:row_start + 3]):
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
            "Phase": ["Phase 1: Strategic Foundations", "Phase 2: Strategy Development", "Phase 3: Strategy & Finance", "Phase 4: Advanced Dimensions", "Phase 5: Capstone"],
            "Modules": ["1 – 3", "4 – 6", "7 – 8", "9 – 11", "12"],
            "Focus": [
                "Foundations, external environment, internal capabilities",
                "Competitive strategy, corporate strategy, innovation & disruption",
                "Value creation, financial performance, planning & implementation",
                "Risk, global strategy, ESG, and strategic FP&A",
                "Integrated real-world strategy project and board presentation"
            ],
            "Duration": ["~3 weeks", "~10 weeks", "~6 weeks", "~9 weeks", "~4 weeks"]
        })
        st.dataframe(learning_path, use_container_width=True, hide_index=True)

        st.subheader("🎓 Professional Relevance")
        cert_df = pd.DataFrame({
            "Role / Context": [
                "CFO / Finance Director",
                "FP&A Manager / Business Partner",
                "Management Accountant (CIMA / CGMA)",
                "Investment Analyst / M&A Analyst",
                "General Manager / Commercial Director"
            ],
            "Modules Most Relevant": [
                "M5, M7, M8, M9, M10 — corporate strategy, value creation, planning, risk, ESG",
                "M1, M7, M8, M11 — foundations, BSC, planning, FP&A and business cases",
                "M3, M4, M7, M11 — internal analysis, competitive strategy, value creation, investment appraisal",
                "M5, M6, M9, M11 — M&A, innovation, risk, financial modelling",
                "M1, M2, M3, M4, M8 — strategy foundations, external/internal analysis, execution"
            ],
            "Programme Coverage": ["~95%", "~90%", "~85%", "~80%", "~85%"]
        })
        st.dataframe(cert_df, use_container_width=True, hide_index=True)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("📖 Module-by-Module Summaries")
        st.markdown("Quick reference summaries for all 12 modules.")

        selected_module = st.selectbox("Select a Module to Review:", [
            f"Module {m['num']}: {m['title']}" for m in modules_info
        ])

        mod_num = int(selected_module.split(":")[0].replace("Module ", ""))
        mod = modules_info[mod_num - 1]

        st.markdown(f"## {mod['icon']} Module {mod['num']}: {mod['title']}")
        st.markdown(f"**Difficulty:** {difficulty_colors.get(mod['difficulty'], '⚪')} {mod['difficulty']} | **Key Skill:** {mod['key_skill']}")

        summaries = {
            1: {
                "overview": "The foundation of strategic thinking — what strategy is, how it differs from tactics and operations, the three levels of strategy, and how finance professionals evolve from scorekeepers into strategic co-pilots.",
                "key_concepts": [
                    "Strategy = integrated choices about WHERE to compete, HOW to compete, and WHAT capabilities to build",
                    "Three levels: Corporate (scope & portfolio), Business Unit (how to compete), Functional (finance, marketing, ops)",
                    "Strategy vs Tactics: strategy = long-term direction (3–10 years); tactics = short-term execution (months)",
                    "Schools of strategic thought: Design (SWOT), Planning (formal process), Positioning (Porter), Resource-Based (VRIN), Dynamic Capabilities",
                    "The strategic management cycle: Analysis → Formulation → Implementation → Evaluation → repeat",
                    "Finance professional as strategic co-pilot: scenario modelling, capital allocation, business case development, strategic KPIs"
                ],
                "key_formulas": {
                    "Strategic Value": "Competitive Advantage × Scale of Opportunity × Execution Quality",
                    "Finance Strategic Contribution": "Analysis Insight + Capital Allocation Skill + Financial Storytelling",
                    "Strategy Map Logic": "Learning & Growth → Internal Process → Customer → Financial Outcomes"
                },
                "exam_tips": [
                    "Strategy is not a plan — it is a set of integrated CHOICES about where to compete and how to win",
                    "Corporate strategy ≠ Business strategy: Corporate = which businesses; Business = how to win in each",
                    "Finance leaders add most value in the Analysis and Evaluation stages — quantifying strategic options and measuring performance"
                ]
            },
            2: {
                "overview": "Systematic frameworks for analysing the macro-environment and industry forces that shape strategic opportunity and financial performance — from PESTLE to Five Forces to scenario planning.",
                "key_concepts": [
                    "PESTLE: Political, Economic, Social, Technological, Legal, Environmental — each factor has direct financial implications",
                    "Porter's Five Forces: New Entrants, Supplier Power, Buyer Power, Substitutes, Rivalry — measures industry profit potential",
                    "High average Five Forces score → structurally unattractive industry → ROIC likely below WACC",
                    "TAM (Total Addressable Market) → SAM (Serviceable) → SOM (Obtainable) — sets revenue targets in financial plan",
                    "Scenario planning: base, bull, bear scenarios tested against financial plan covenants and liquidity",
                    "PESTLE Priority Score = Likelihood × Impact (1–5 each); score ≥16 = Critical strategic risk"
                ],
                "key_formulas": {
                    "PESTLE Priority Score": "Likelihood (1–5) × Impact (1–5)",
                    "Five Forces Avg": "Sum of all force scores / 5  (lower = more attractive)",
                    "TAM": "Total Population × Average Annual Spend per Customer",
                    "SAM": "TAM × % of market your business model can serve",
                    "SOM": "SAM × % realistically capturable in 3–5 year planning horizon"
                },
                "exam_tips": [
                    "Five Forces measures INDUSTRY attractiveness — not company attractiveness. Strong companies can still earn good returns in tough industries",
                    "SOM — not TAM — is what goes into your revenue forecast in the financial model",
                    "Scenario planning: always build at least three scenarios (base, bull, bear) and test against covenant thresholds"
                ]
            },
            3: {
                "overview": "Internal analysis reveals WHERE competitive advantage comes from — unique resources (VRIN), value chain cost drivers, and financial capabilities that act as strategic assets.",
                "key_concepts": [
                    "VRIN: Valuable, Rare, Inimitable, Non-Substitutable — all four needed for Sustainable Competitive Advantage",
                    "Porter's Value Chain: Primary activities (Inbound/Ops/Outbound/Marketing/Service) + Support activities (Infrastructure/HR/Tech/Procurement)",
                    "Firm Infrastructure (Finance) is a Support Activity — but influences ALL primary activities through capital allocation, pricing, and cost management",
                    "Activity-Based Costing maps costs to value chain activities — revealing value vs. cost by activity",
                    "Financial capabilities as strategic assets: fortress balance sheet, working capital efficiency, capital allocation skill",
                    "TOWS matrix converts SWOT into SO (grow), ST (defend), WO (fix to win), WT (survive) strategic options"
                ],
                "key_formulas": {
                    "VRIN Test": "Valuable + Rare + Inimitable + Non-Substitutable = Sustainable Competitive Advantage",
                    "Capability Gap": "Required Capability Level − Current Capability Level",
                    "Value/Cost Ratio": "Value Score (1–5) / Cost ($) — higher = strategic activity worth protecting"
                },
                "exam_tips": [
                    "A resource that is V but not R gives only competitive parity. Need all four VRIN criteria for SCA",
                    "Finance sits in 'Firm Infrastructure' — a Support Activity — but its influence reaches every part of the value chain",
                    "TOWS: SO options have the best NPV potential; WT options are survival-critical — prioritise both"
                ]
            },
            4: {
                "overview": "How firms compete within their chosen markets — Porter's generic strategies, pricing power, ROIC as the definitive strategy metric, and competitive moats that protect financial returns.",
                "key_concepts": [
                    "Porter's Generic Strategies: Cost Leadership (broad, low cost), Differentiation (broad, premium), Cost Focus (narrow, low cost), Differentiation Focus (narrow, premium)",
                    "'Stuck in the middle' = pursuing both cost leadership AND differentiation without excelling at either → worst ROIC",
                    "ROIC = NOPAT / Invested Capital — the fundamental financial test of competitive strategy success",
                    "Value Created = (ROIC − WACC) × Invested Capital: ROIC > WACC = value creation; ROIC < WACC = value destruction",
                    "Pricing power is the #1 financial indicator of competitive advantage — 1% price increase ≈ 10% EBIT uplift (typical business)",
                    "Moats: Network effects, switching costs, intangible assets (brand/IP), cost advantages, efficient scale"
                ],
                "key_formulas": {
                    "ROIC": "NOPAT / Invested Capital",
                    "NOPAT": "EBIT × (1 − Tax Rate)",
                    "EVA (Economic Value Added)": "(ROIC − WACC) × Invested Capital",
                    "DuPont ROIC": "NOPAT Margin × Asset Turnover",
                    "EBIT Pricing Impact": "Price Change (%) × (1 / EBIT Margin %)"
                },
                "exam_tips": [
                    "ROIC < WACC = value destruction, regardless of how profitable the business looks on an absolute basis",
                    "DuPont: Luxury = high margin / low turnover; Discounter = low margin / high turnover — both can achieve same ROIC",
                    "Pricing power (not just revenue growth) is the clearest evidence that a competitive strategy is working"
                ]
            },
            5: {
                "overview": "Corporate-level strategy: which businesses to own, how to grow, portfolio analysis, M&A value creation, and the capital allocation decisions that define the CFO's most strategic role.",
                "key_concepts": [
                    "Ansoff Matrix: Market Penetration (lowest risk) → Market Development → Product Development → Diversification (highest risk)",
                    "BCG Matrix: Stars (invest), Cash Cows (harvest), Question Marks (selective), Dogs (divest)",
                    "M&A creates value only if: Synergy NPV > Acquisition Premium paid",
                    "Cost synergies (70–80% achievable) are more reliable than revenue synergies (30–40% achievable)",
                    "Capital allocation hierarchy: Maintain → Grow → M&A → Return capital (dividends/buybacks)",
                    "Conglomerate discount: when market values diversified company below sum-of-parts → break-up may unlock value"
                ],
                "key_formulas": {
                    "BCG Relative Market Share": "Your Market Share / Largest Competitor Share",
                    "M&A Net Value Created": "Synergy NPV − Acquisition Premium Paid",
                    "Synergy NPV": "PV(Cost Synergies × Confidence%) + PV(Revenue Synergies × Confidence%)",
                    "Capital Allocation Test": "Expected ROIC on each use > WACC hurdle rate"
                },
                "exam_tips": [
                    "BCG Cash Cows fund Stars — always trace the cash flow logic of the portfolio",
                    "Revenue synergies are systematically over-estimated. Conservative CFOs model cost synergies only for deal approval",
                    "Diversification (Ansoff) carries the highest risk because BOTH the product AND the market are new"
                ]
            },
            6: {
                "overview": "Innovation types, the 3-Horizon model for investment allocation, disruptive innovation theory, digital transformation strategy, and real options thinking for innovation investment decisions.",
                "key_concepts": [
                    "Innovation types: Incremental → Architectural → Radical → Disruptive (increasing risk and uncertainty)",
                    "3-Horizon model: H1 (70% budget, 0–2yr, ROIC metric) → H2 (20%, 2–5yr) → H3 (10%, 5yr+, option value metric)",
                    "Christensen disruption: simple/cheap product at low end → improves → attacks incumbent core → incumbent responds too late",
                    "Digital transformation is strategic repositioning — not an IT project",
                    "Real options: Total Strategic Value = Traditional NPV + Real Option Value (expand, defer, abandon, switch)",
                    "The 'window to respond' to disruption is early — finance must model displacement risk before it is obvious"
                ],
                "key_formulas": {
                    "Real Option Value": "P(Success) × max(0, Phase 2 NPV − Phase 2 Investment)",
                    "Total Strategic Value": "Traditional NPV + Real Option Value",
                    "Digital ROI": "(Total Benefits − Total Costs) / Total Investment × 100%",
                    "3-Horizon Allocation": "H1: 70% | H2: 20% | H3: 10% of innovation budget"
                },
                "exam_tips": [
                    "Traditional NPV systematically UNDERVALUES innovation by ignoring real option value (flexibility to expand if it succeeds)",
                    "Disruption starts below the radar — incumbents ignore it because early disruptors target low-margin customers",
                    "H1 funds H2 and H3 — without healthy Cash Cows and Stars, there is no budget for visionary bets"
                ]
            },
            7: {
                "overview": "The master module — linking strategy directly to financial value through EVA, Balanced Scorecard, DuPont ROIC decomposition, FCF signals, and capital structure decisions.",
                "key_concepts": [
                    "Four value drivers: Revenue Growth + Margin Improvement + Capital Efficiency + WACC Reduction",
                    "EVA = (ROIC − WACC) × Invested Capital — the single best measure of whether strategy is creating value",
                    "Balanced Scorecard: Financial (outcome) → Customer (enabler) → Internal Process (engine) → Learning & Growth (foundation)",
                    "DuPont: ROIC = NOPAT Margin × Asset Turnover — reveals whether advantage is margin-led or turnover-led",
                    "FCF trend: Growing FCF + Rising ROIC = ✅ Invest; Falling FCF + Falling ROIC = 🔴 Urgent strategic review",
                    "Capital structure is a strategic choice: fortress balance sheet = strategic optionality; over-leverage = strategic trap"
                ],
                "key_formulas": {
                    "EVA": "(ROIC − WACC) × Invested Capital",
                    "ROIC (DuPont)": "NOPAT Margin × Asset Turnover = (NOPAT/Revenue) × (Revenue/Invested Capital)",
                    "FCF": "NOPAT − Net Reinvestment (Capex + ΔNWC − Depreciation)",
                    "WACC": "(E/V × Re) + (D/V × Rd × (1 − Tax Rate))"
                },
                "exam_tips": [
                    "Balanced Scorecard is causal: L&G capabilities → better processes → better customer outcomes → financial results",
                    "EVA is the most honest measure — it charges for ALL capital deployed, not just debt",
                    "A fortress balance sheet (low debt) is a strategic ASSET — it creates optionality to invest counter-cyclically"
                ]
            },
            8: {
                "overview": "Translating strategy into executable plans — the integrated planning calendar, 7-S organisational alignment, Kotter's change model, rolling forecasts, and agile strategy adaptation.",
                "key_concepts": [
                    "67% of strategies fail in EXECUTION, not formulation — the implementation gap is the primary failure point",
                    "McKinsey 7-S: Strategy, Structure, Systems (Hard Ss) + Shared Values (centre) + Skills, Style, Staff (Soft Ss)",
                    "All seven Ss must align — Shared Values is the central element linking all others",
                    "Kotter Step 1: Create urgency — finance quantifies the cost of inaction; Step 6: Report early financial wins",
                    "Integrated planning: Environmental scan → Strategic options → LRP (3–5yr) → Annual budget → KPI cascade",
                    "Rolling forecast: always 12–18 months forward; updated monthly/quarterly; supports strategy, not just control"
                ],
                "key_formulas": {
                    "Transformation Cost": "Σ (Gap size × Cost to close each 7-S gap)",
                    "Initiative Priority Score": "(Strategic Fit × 2 + NPV/Investment × Risk Adj + 5/Payback) / 3",
                    "Rolling Forecast Horizon": "Always = Fixed forward period (e.g. 12 months) — never shrinks"
                },
                "exam_tips": [
                    "7-S Shared Values is the centre — if culture is misaligned, even perfect strategy, structure, and systems will fail",
                    "Strategy execution gaps: Vision → Resource → Management → People — finance addresses all four",
                    "Rolling forecast ≠ Annual budget revision. Rolling forecasts always look forward a fixed period, adapting to new information"
                ]
            },
            9: {
                "overview": "Strategic risk quantification, decision trees, scenario stress testing, behavioural biases in strategic decisions, and building financial resilience — the risk management toolkit for strategic finance.",
                "key_concepts": [
                    "Risk types: Strategic, Operational, Financial, Compliance, Reputational — each requires different finance response",
                    "Strategic Risk Score = Likelihood (1–5) × Impact (1–5): ≥16 = Critical; 9–15 = High; 4–8 = Medium",
                    "Expected Value (EV) = Σ [Probability × Payoff] — optimal strategic decision = highest risk-adjusted EV",
                    "Tornado chart: ranks assumptions by their NPV impact — widest bar = most critical risk driver",
                    "Four financial resilience dimensions: Liquidity, Earnings, Capital, Operational resilience",
                    "Six behavioural biases: Overconfidence, Anchoring, Sunk Cost, Groupthink, Optimism Bias, Confirmation Bias"
                ],
                "key_formulas": {
                    "Inherent Risk Score": "Likelihood (1–5) × Impact (1–5)",
                    "Expected Value": "Σ [Probability(i) × Payoff(i)] for all outcomes",
                    "Residual Risk": "Inherent Risk − Control Effectiveness",
                    "Liquidity Buffer": "Max monthly cash burn × Survival horizon (3–6 months)"
                },
                "exam_tips": [
                    "Sunk costs are IRRELEVANT to future decisions — only future incremental cash flows matter. Sunk cost fallacy destroys strategic value",
                    "Decision trees use EXPECTED VALUE — but risk-averse boards may choose lower-EV options with lower downside",
                    "Financial resilience test: can the business survive EBITDA -40% for 18 months without covenant breach?"
                ]
            },
            10: {
                "overview": "International strategy (CAGE framework, entry modes), ESG as strategic and financial imperative, and stakeholder value — the modern dimensions every strategic finance professional must master.",
                "key_concepts": [
                    "CAGE Distance: Cultural, Administrative, Geographic, Economic — each dimension increases entry cost and risk",
                    "Global strategy types: Global (standardise for efficiency) vs Multidomestic (customise locally) vs Transnational (both — hardest)",
                    "Entry modes: Exporting (least commitment) → Licensing → JV → Greenfield → Acquisition (most commitment)",
                    "ESG reduces WACC: strong ESG profile → lower investor risk premium → 15–40bp cost of capital saving",
                    "Carbon cost = Emissions (tonnes) × Carbon price ($/tonne) — must be in long-range financial plan from $30/tonne upward",
                    "Stakeholder map: High importance + Low satisfaction = urgent investment priority"
                ],
                "key_formulas": {
                    "CAGE Weighted Distance": "Σ (Score(dimension) × Weight(dimension))",
                    "ESG WACC Benefit": "Enterprise Value × WACC Reduction (bp) / 10,000",
                    "Carbon Cost ($)": "Emissions (000 tonnes) × Carbon Price ($/tonne)",
                    "Entry Mode Priority": "f(Control needed, Capital available, Speed required, Risk tolerance)"
                },
                "exam_tips": [
                    "Transnational strategy (global efficiency + local responsiveness) is the most powerful but hardest to execute — high management complexity",
                    "ESG is not just reputational — it has direct financial impact via WACC, talent retention, and customer preference",
                    "Use OPTIONS not forwards to hedge M&A FX — if deal fails, a forward creates a naked currency position"
                ]
            },
            11: {
                "overview": "The operational core of strategic finance — driver-based modelling, investment appraisal, rolling forecasts, and the nine-component business case that wins board approval.",
                "key_concepts": [
                    "Strategic FP&A answers 'What should we do?' — traditional FP&A answers 'What happened?'",
                    "Driver-based models: Strategic drivers → Operational drivers → Financial outputs (changes cascade automatically)",
                    "NPV is the primary appraisal method: directly measures dollar value created after accounting for time value and risk",
                    "IRR flaw: assumes reinvestment at IRR (often too high) — use MIRR for more realistic returns",
                    "Business case must include: Do Nothing option, options appraisal, NPV/IRR/payback, risks, benefits realisation plan",
                    "Rolling forecast: always 12–18 months forward; adapts to new information; combined with annual budget = best practice"
                ],
                "key_formulas": {
                    "NPV": "Σ [CFt / (1+r)^t] − Initial Investment",
                    "IRR": "Discount rate where NPV = 0",
                    "Payback (simple)": "Initial Investment / Annual Cash Flow",
                    "MIRR": "(FV of positive CFs at WACC / PV of costs)^(1/n) − 1"
                },
                "exam_tips": [
                    "NPV > 0 is necessary but not sufficient — also check IRR vs WACC, payback vs liquidity needs, and strategic fit",
                    "Driver-based models force explicit assumptions — every line is explainable and challengeable by business leadership",
                    "The 'Do Nothing' option in a business case defines the cost of inaction — often the most powerful argument for investment"
                ]
            },
            12: {
                "overview": "The Capstone brings together all 12 modules into a single integrated deliverable: complete strategic analysis, financial plan, scenario modelling, risk register, and boardroom-ready strategy presentation.",
                "key_concepts": [
                    "SAFe evaluation: Suitability (does strategy fit?), Acceptability (will stakeholders accept it?), Feasibility (can we execute it?)",
                    "Integrated strategic analysis: External (PESTLE + Five Forces) + Internal (VRIN + Value Chain) + SWOT/TOWS",
                    "3-year driver-based financial plan: P&L + BS indication + FCF + ROIC bridge from current to target",
                    "Scenario analysis: bull/base/bear → test all scenarios against covenant thresholds and liquidity",
                    "Boardroom communication: Lead with the financial punchline; quantify every strategic claim; own the risks proactively",
                    "The CFO's ask: specific capital amount + governance path + decision timeline + ROIC return commitment"
                ],
                "key_formulas": {
                    "Master Value Creation Formula": "EVA = (ROIC − WACC) × Invested Capital",
                    "SAFe Score": "(Suitability + Acceptability + Feasibility) / 3",
                    "Boardroom Punchline Template": "'This strategy grows ROIC from X% to Y% in Z years, creating $NM of EVA. Here's how.'",
                    "Strategic Finance Value": "Analysis × Insight × Capital Allocation × Communication Quality"
                },
                "exam_tips": [
                    "Integration is the key — every framework from Modules 1–11 must connect: external → internal → strategy → financials → implementation → risk",
                    "Lead with the financial headline in the board presentation — not the methodology",
                    "Quantify every strategic claim: not 'better customer experience' but 'NPS +15pts → churn -4% → $6M revenue retention'"
                ]
            },
        }

        summary = summaries[mod_num]

        st.markdown("### 📋 Overview")
        st.info(summary["overview"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 💡 Key Concepts")
            for concept in summary["key_concepts"]:
                st.markdown(f"• {concept}")
        with col2:
            st.markdown("### 📐 Key Formulas")
            for formula, expression in summary["key_formulas"].items():
                st.markdown(f"**{formula}:**")
                st.code(expression)

        st.markdown("### 🎯 Exam & Application Tips")
        for tip in summary["exam_tips"]:
            st.warning(f"💡 {tip}")

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("🧮 Formula Bank — All 12 Modules")
        st.markdown("Complete framework and formula reference for the entire Business Strategy curriculum.")

        formula_category = st.selectbox("Filter by Category:", [
            "All Formulas",
            "Strategic Foundations (M1–M3)",
            "Competitive & Corporate Strategy (M4–M5)",
            "Innovation & Value Creation (M6–M7)",
            "Planning, Risk & Resilience (M8–M9)",
            "Global, ESG & Financial Modelling (M10–M11)",
            "Capstone Integration (M12)"
        ])

        all_formulas = [
            # M1 Foundations
            ("M1", "Strategic Value", "Competitive Advantage × Scale of Opportunity × Execution Quality", "Holistic strategy quality test"),
            ("M1", "Finance Strategic Contribution", "Analysis Insight + Capital Allocation Skill + Financial Storytelling", "CFO value-add formula"),
            ("M1", "Strategy Map Logic", "Learning & Growth → Process → Customer → Financial Outcomes", "BSC cause-and-effect chain"),
            # M2 External Analysis
            ("M2", "PESTLE Priority Score", "Likelihood (1–5) × Impact (1–5)", "Critical if ≥ 16/25"),
            ("M2", "Five Forces Average", "Sum of force scores / 5  (lower = more attractive)", "Industry attractiveness rating"),
            ("M2", "TAM", "Total Population × Average Annual Spend per Customer ($)", "Maximum market opportunity"),
            ("M2", "SAM", "TAM × % your business model can serve", "Serviceable market for financial plan"),
            ("M2", "SOM", "SAM × % realistically capturable in 3–5yr horizon", "Revenue target for financial model"),
            # M3 Internal Analysis
            ("M3", "VRIN Test", "V + R + I + N = Sustainable Competitive Advantage", "All four criteria required"),
            ("M3", "Value/Cost Ratio", "Value Score (1–5) / Cost ($000s)", "Activity worth protecting if high"),
            ("M3", "Capability Gap", "Required Capability Level − Current Capability Level", "Investment target sizing"),
            # M4 Business Strategy
            ("M4", "ROIC", "NOPAT / Invested Capital", "Fundamental strategy scorecard"),
            ("M4", "NOPAT", "EBIT × (1 − Tax Rate)", "Net Operating Profit After Tax"),
            ("M4", "EVA (Economic Value Added)", "(ROIC − WACC) × Invested Capital", "Dollar value created above cost of capital"),
            ("M4", "DuPont ROIC", "NOPAT Margin × Asset Turnover", "Reveals margin-led vs turnover-led advantage"),
            ("M4", "EBIT Pricing Impact", "Price Change (%) × (1 / EBIT Margin %)", "~10× leverage for typical business"),
            # M5 Corporate Strategy
            ("M5", "BCG Relative Share", "Your Market Share / Largest Competitor Share", "≥1.0 = market leader"),
            ("M5", "M&A Net Value", "Synergy NPV − Acquisition Premium Paid", "Positive = deal creates value"),
            ("M5", "Synergy NPV", "PV(Cost Synergies × Confidence%) + PV(Revenue Synergies × Confidence%)", "Risk-adjusted synergy value"),
            ("M5", "Capital Allocation Test", "Expected ROIC on each use vs WACC hurdle rate", "Invest if ROIC > WACC"),
            # M6 Innovation
            ("M6", "Real Option Value", "P(Success) × max(0, Phase 2 NPV − Phase 2 Investment)", "Option to expand if Phase 1 succeeds"),
            ("M6", "Total Strategic Value", "Traditional NPV + Real Option Value", "Full investment value including flexibility"),
            ("M6", "Digital ROI", "(Total Benefits − Total Costs) / Total Investment × 100%", "Digital transformation return"),
            ("M6", "3-Horizon Allocation", "H1: 70% | H2: 20% | H3: 10% of innovation budget", "Balanced innovation portfolio"),
            # M7 Value Creation
            ("M7", "EVA", "(ROIC − WACC) × Invested Capital", "Value created in dollar terms"),
            ("M7", "ROIC (DuPont)", "(NOPAT / Revenue) × (Revenue / Invested Capital)", "Margin × Turnover decomposition"),
            ("M7", "FCF", "NOPAT − Net Reinvestment (Capex + ΔNWC − Depreciation)", "Cash generation signal"),
            ("M7", "WACC", "(E/V × Re) + (D/V × Rd × (1 − Tax Rate))", "Minimum acceptable return on capital"),
            # M8 Planning
            ("M8", "Transformation Cost", "Σ (Gap size × Cost to close each 7-S gap)", "Budget for strategic change"),
            ("M8", "Initiative Priority Score", "(Strategic Fit × 2 + NPV/Investment × Risk Adj + 5/Payback) / 3", "Rank competing initiatives"),
            # M9 Risk
            ("M9", "Inherent Risk Score", "Likelihood (1–5) × Impact (1–5)", "≥16 = Critical; 9–15 = High"),
            ("M9", "Expected Value", "Σ [Probability(i) × Payoff(i)] for all outcomes", "Probability-weighted strategic payoff"),
            ("M9", "Residual Risk", "Inherent Risk − Control Effectiveness", "Risk after mitigation"),
            ("M9", "Liquidity Buffer", "Max monthly cash burn × Survival horizon (months)", "Minimum liquidity reserve"),
            # M10 Global / ESG
            ("M10", "CAGE Weighted Distance", "Σ (Score(dimension) × Weight(dimension))", "International expansion complexity"),
            ("M10", "ESG WACC Benefit", "Enterprise Value × WACC Reduction (bp) / 10,000", "Annual cost of capital saving ($)"),
            ("M10", "Carbon Cost", "Emissions (000 tonnes) × Carbon Price ($/tonne)", "P&L exposure to carbon pricing"),
            # M11 FP&A
            ("M11", "NPV", "Σ [CFt / (1+r)^t] − Initial Investment", "Primary investment appraisal method"),
            ("M11", "IRR", "Discount rate where NPV = 0", "Compare to WACC — accept if IRR > WACC"),
            ("M11", "Payback (simple)", "Initial Investment / Annual Cash Flow", "Liquidity recovery test"),
            ("M11", "MIRR", "(FV positive CFs at WACC / PV costs)^(1/n) − 1", "Realistic IRR using WACC reinvestment rate"),
            # M12 Capstone
            ("M12", "SAFe Score", "(Suitability + Acceptability + Feasibility) / 3", "Strategy option evaluation — max 5"),
            ("M12", "ROIC Bridge", "Current ROIC + Margin Uplift + Turnover Improvement − WACC = New Spread", "Strategy impact on value creation"),
        ]

        cat_filter = {
            "All Formulas": list(range(13)),
            "Strategic Foundations (M1–M3)": [1, 2, 3],
            "Competitive & Corporate Strategy (M4–M5)": [4, 5],
            "Innovation & Value Creation (M6–M7)": [6, 7],
            "Planning, Risk & Resilience (M8–M9)": [8, 9],
            "Global, ESG & Financial Modelling (M10–M11)": [10, 11],
            "Capstone Integration (M12)": [12]
        }

        filtered_mods = cat_filter[formula_category]
        filtered_formulas = [(m, n, f, u) for m, n, f, u in all_formulas
                              if int(m.replace("M", "")) in filtered_mods]

        formula_df = pd.DataFrame(filtered_formulas, columns=["Module", "Formula / Framework Name", "Expression / Logic", "Use / Notes"])
        st.dataframe(formula_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔍 Formula & Framework Lookup")
        search_term = st.text_input("Search for a formula or framework (type any keyword):", placeholder="e.g. ROIC, NPV, PESTLE, VRIN, EVA, WACC...")
        if search_term:
            matches = [(m, n, f, u) for m, n, f, u in all_formulas
                        if search_term.lower() in n.lower() or search_term.lower() in f.lower() or search_term.lower() in u.lower()]
            if matches:
                st.dataframe(pd.DataFrame(matches, columns=["Module", "Name", "Expression", "Notes"]),
                             use_container_width=True, hide_index=True)
            else:
                st.warning(f"No formulas found matching '{search_term}'. Try a different keyword.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("📊 Visual Dashboard")

        st.subheader("Difficulty Progression Across 12 Modules")
        difficulty_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3, "Expert": 4}
        diff_values = [difficulty_map[m["difficulty"]] for m in modules_info]
        diff_colors = [m["color"] for m in modules_info]

        fig_diff = go.Figure(go.Scatter(
            x=list(range(1, 13)),
            y=diff_values,
            mode="lines+markers+text",
            line=dict(color="#1B3A6B", width=3),
            marker=dict(size=22, color=diff_colors),
            text=[f"M{m['num']}" for m in modules_info],
            textposition="middle center",
            textfont=dict(color="white", size=10)
        ))
        fig_diff.update_layout(
            title="Difficulty Progression Across 12 Modules",
            xaxis_title="Module Number",
            yaxis=dict(tickvals=[1, 2, 3, 4], ticktext=["Beginner", "Intermediate", "Advanced", "Expert"]),
            hovermode="x unified"
        )
        fig_diff.add_hrect(y0=0.5, y1=1.5, fillcolor="green", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=1.5, y1=2.5, fillcolor="yellow", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=2.5, y1=3.5, fillcolor="orange", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=3.5, y1=4.5, fillcolor="red", opacity=0.08, line_width=0)
        st.plotly_chart(fig_diff, use_container_width=True)

        st.subheader("Strategic Finance Competencies Developed")
        skill_categories = ["Strategic Analysis", "Financial Modelling", "Risk Management",
                            "Global & ESG", "Decision-Making", "Communication & Leadership"]
        skill_scores = [10, 10, 9, 8, 9, 9]
        skill_scores_r = skill_scores + [skill_scores[0]]
        categories_r = skill_categories + [skill_categories[0]]

        fig_radar = go.Figure(go.Scatterpolar(
            r=skill_scores_r,
            theta=categories_r,
            fill="toself",
            name="Skills Covered",
            line=dict(color="#1B3A6B", width=3),
            fillcolor="rgba(27,58,107,0.3)"
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False,
            title="Strategic Finance Competencies — All 12 Modules Combined"
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        st.subheader("Topics per Module")
        fig_topics = go.Figure(go.Bar(
            x=[f"M{m['num']}" for m in modules_info],
            y=[len(m["topics"]) for m in modules_info],
            marker_color=[m["color"] for m in modules_info],
            text=[f"{len(m['topics'])} topics" for m in modules_info],
            textposition="auto"
        ))
        fig_topics.update_layout(
            title="Number of Major Topic Areas per Module",
            xaxis_title="Module", yaxis_title="Number of Major Topics"
        )
        st.plotly_chart(fig_topics, use_container_width=True)

        st.subheader("Programme Coverage — Finance Competency Areas")
        col1, col2 = st.columns(2)
        with col1:
            phases = ["Phase 1\nFoundations (M1–3)", "Phase 2\nStrategy Dev (M4–6)",
                      "Phase 3\nFinance Link (M7–8)", "Phase 4\nAdvanced (M9–11)", "Phase 5\nCapstone (M12)"]
            weeks = [9, 10, 6, 9, 4]
            fig_ph = go.Figure(go.Pie(
                labels=phases, values=weeks, hole=0.35,
                marker=dict(colors=["#1B3A6B", "#2563EB", "#0D7377", "#D97706", "#7C3AED"])
            ))
            fig_ph.update_layout(title="Programme Time Allocation by Phase (~38 weeks total)")
            st.plotly_chart(fig_ph, use_container_width=True)
        with col2:
            competencies = ["Strategic Analysis", "Financial Modelling", "M&A & Valuation",
                            "Risk Management", "ESG & Global", "Communication"]
            module_counts = [8, 7, 3, 4, 3, 4]
            fig_comp = go.Figure(go.Pie(
                labels=competencies, values=module_counts, hole=0.35,
                marker=dict(colors=["#1B3A6B", "#0D7377", "#D97706", "#E74C3C", "#059669", "#7C3AED"])
            ))
            fig_comp.update_layout(title="Modules Addressing Each Finance Competency")
            st.plotly_chart(fig_comp, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("✅ Master Quiz — All 12 Modules")
        st.markdown("Test your knowledge across the entire Business Strategy curriculum!")

        quiz_mode = st.radio("Quiz Mode:", [
            "Quick Fire (5 questions)", "Standard (10 questions)", "Full Exam (12 questions)"
        ], horizontal=True)
        num_q = {"Quick Fire (5 questions)": 5, "Standard (10 questions)": 10, "Full Exam (12 questions)": 12}[quiz_mode]

        all_quiz_questions = [
            {"q": "Strategy differs from tactics because:",
             "opts": ["Strategy is set by analysts; tactics by the CEO",
                      "Strategy defines long-term competitive direction; tactics are short-term execution actions",
                      "Strategy focuses on cost reduction; tactics on revenue growth",
                      "There is no meaningful difference in modern organisations"],
             "ans": "Strategy defines long-term competitive direction; tactics are short-term execution actions",
             "mod": 1,
             "exp": "Strategy = WHERE and WHY (3–10 year horizon). Tactics = HOW in the short term. Operations = daily activities. All three levels are distinct."},

            {"q": "A high average score across Porter's Five Forces indicates:",
             "opts": ["The industry is very attractive with high profit potential",
                      "The industry is structurally unattractive — ROIC likely below WACC",
                      "The company has a strong competitive position",
                      "Market growth rate is high"],
             "ans": "The industry is structurally unattractive — ROIC likely below WACC",
             "mod": 2,
             "exp": "High Five Forces = intense competitive pressure from multiple directions → structural margin erosion → ROIC below WACC for average competitor. Finance implication: set low return expectations, require exceptional capability to justify capital investment."},

            {"q": "For a resource to provide Sustainable Competitive Advantage under the VRIN framework, it must be:",
             "opts": ["Valuable and rare only", "Valuable, rare, and expensive",
                      "Valuable, rare, inimitable, AND non-substitutable",
                      "Rare and non-substitutable only"],
             "ans": "Valuable, rare, inimitable, AND non-substitutable",
             "mod": 3,
             "exp": "All four VRIN criteria must be met. Valuable alone = parity. V+R = temporary advantage. V+R+I = sustained. Only V+R+I+N = Sustainable Competitive Advantage that holds over time."},

            {"q": "EVA (Economic Value Added) is positive when:",
             "opts": ["Revenue is growing", "EBITDA is positive",
                      "ROIC exceeds WACC", "The company pays no dividends"],
             "ans": "ROIC exceeds WACC",
             "mod": 4,
             "exp": "EVA = (ROIC − WACC) × Invested Capital. Positive EVA only when ROIC > WACC — the strategy earns more than the cost of the capital deployed. This is the fundamental test of whether strategy creates economic value."},

            {"q": "In the BCG Matrix, which quadrant requires the MOST investment to maintain position?",
             "opts": ["Cash Cows", "Dogs", "Stars", "Question Marks"],
             "ans": "Stars",
             "mod": 5,
             "exp": "Stars (high growth + high share) require heavy investment to maintain market leadership in a fast-growing market. The investment roughly equals cash generated — they are self-funding but need capex to stay ahead."},

            {"q": "Real option value captures something that traditional NPV misses — specifically:",
             "opts": ["The risk of project failure",
                      "The strategic value of flexibility to expand, defer, or abandon based on future information",
                      "The tax benefits of capital investment",
                      "The depreciation shield from capex"],
             "ans": "The strategic value of flexibility to expand, defer, or abandon based on future information",
             "mod": 6,
             "exp": "Traditional NPV assumes a fixed decision path. Real options add the value of flexibility — if Phase 1 succeeds, you invest more; if it fails, you abandon. This optionality has real financial value that NPV ignores."},

            {"q": "In DuPont analysis, a luxury retailer's ROIC is typically driven by:",
             "opts": ["High asset turnover and low margins",
                      "High NOPAT margins and lower asset turnover",
                      "Low WACC and high financial leverage",
                      "High capex intensity"],
             "ans": "High NOPAT margins and lower asset turnover",
             "mod": 7,
             "exp": "ROIC = NOPAT Margin × Asset Turnover. Luxury brands command price premiums → high margins. But they sell less volume per $1 of capital → lower turnover. Both routes (high margin OR high turnover) can deliver strong ROIC above WACC."},

            {"q": "In McKinsey's 7-S Framework, the central element linking all others is:",
             "opts": ["Strategy", "Structure", "Shared Values", "Systems"],
             "ans": "Shared Values",
             "mod": 8,
             "exp": "Shared Values (organisational culture) sits at the centre of the 7-S model. Culture influences and connects all other six elements. If culture is misaligned with strategy, even perfect structure and systems will not deliver effective execution."},

            {"q": "The 'sunk cost fallacy' in strategic decision-making means:",
             "opts": ["Future investments are too uncertain to evaluate",
                      "Continuing to invest in a failing initiative because of capital already spent",
                      "Underestimating the total cost of a new project",
                      "Overweighting short-term returns vs long-term value"],
             "ans": "Continuing to invest in a failing initiative because of capital already spent",
             "mod": 9,
             "exp": "Sunk costs are irrelevant to future decisions. Only future incremental cash flows matter. Letting past spend drive future investment is the sunk cost fallacy — and one of the most value-destructive biases in corporate strategy."},

            {"q": "The CAGE framework helps finance professionals assess international expansion by:",
             "opts": ["Calculating the currency-adjusted IRR of overseas investments",
                      "Measuring the four dimensions of distance that increase entry cost and risk",
                      "Identifying the optimal capital structure for foreign subsidiaries",
                      "Assessing ESG compliance in target markets"],
             "ans": "Measuring the four dimensions of distance that increase entry cost and risk",
             "mod": 10,
             "exp": "CAGE = Cultural, Administrative, Geographic, Economic distance. Each dimension adds cost and complexity to international expansion. High CAGE distance = higher entry investment, longer payback, greater execution risk."},

            {"q": "A driver-based financial model differs from a traditional budget because:",
             "opts": ["It is prepared by the operations team, not finance",
                      "It links financial outputs to operational and commercial drivers — one assumption change cascades through the whole model",
                      "It focuses only on cost reduction opportunities",
                      "It uses historical averages to project future performance"],
             "ans": "It links financial outputs to operational and commercial drivers — one assumption change cascades through the whole model",
             "mod": 11,
             "exp": "Driver-based models build revenue and costs from underlying operational drivers (e.g. customer count × ARPC × retention). Change one driver assumption and the entire P&L, BS, and CF update automatically — enabling real-time scenario analysis and decision support."},

            {"q": "In a Capstone boardroom presentation, the finance professional should:",
             "opts": ["Present all analysis before revealing the financial implications",
                      "Focus primarily on the methodology used",
                      "Lead with the financial punchline and quantify every strategic claim",
                      "Avoid mentioning risks to maintain board confidence"],
             "ans": "Lead with the financial punchline and quantify every strategic claim",
             "mod": 12,
             "exp": "'This strategy grows ROIC from 10% to 18%, creating $45M of EVA. Here's how.' Boards need numbers first, then logic. Every strategic claim must be quantified. Risks must be owned proactively — they build credibility, not undermine it."},
        ]

        selected_questions = all_quiz_questions[:num_q]

        if "bs_quiz_submitted" not in st.session_state:
            st.session_state.bs_quiz_submitted = {}

        for idx, q in enumerate(selected_questions):
            st.markdown("---")
            st.markdown(f"**Q{idx+1}. [Module {q['mod']}] {q['q']}**")
            answer = st.radio("", q["opts"], key=f"bsmq_{idx}")

            if st.button(f"Check Answer Q{idx+1}", key=f"bsmqc_{idx}"):
                if answer == q["ans"]:
                    st.success(f"✅ Correct! {q['exp']}")
                    st.session_state.bs_quiz_submitted[idx] = True
                else:
                    st.error(f"❌ Incorrect. The correct answer is: **{q['ans']}**")
                    st.info(f"💡 Explanation: {q['exp']}")
                    st.session_state.bs_quiz_submitted[idx] = False

        st.markdown("---")
        answered = len(st.session_state.bs_quiz_submitted)
        correct = sum(1 for v in st.session_state.bs_quiz_submitted.values() if v)
        if answered > 0:
            pct = correct / answered * 100
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Questions Answered", f"{answered}/{num_q}")
            with col2: st.metric("Correct Answers", f"{correct}")
            with col3: st.metric("Score", f"{pct:.0f}%")

            if pct >= 90:
                st.success("🏆 Outstanding! You have strategic finance mastery across all 12 modules!")
            elif pct >= 75:
                st.info("✅ Great work! Strong understanding of the Business Strategy curriculum.")
            elif pct >= 60:
                st.warning("⚠️ Good progress! Review the modules where you made mistakes.")
            else:
                st.error("❌ Keep studying! Return to the modules you found challenging and revisit the key frameworks.")

        if st.button("🔄 Reset Quiz"):
            st.session_state.bs_quiz_submitted = {}
            st.rerun()

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("🎓 Study Planner & Progress Tracker")

        st.subheader("📅 Suggested Study Schedule")
        schedule_df = pd.DataFrame({
            "Week": ["Week 1–3", "Week 4–6", "Week 7–9", "Week 10–12", "Week 13–15",
                     "Week 16–18", "Week 19–21", "Week 22–24", "Week 25–27",
                     "Week 28–30", "Week 31–33", "Week 34–38"],
            "Module": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12 + Review"],
            "Topics": [
                "Foundations: strategy levels, schools of thought, strategic management cycle, finance as strategic partner",
                "External analysis: PESTLE, Five Forces, market sizing (TAM/SAM/SOM), scenario planning",
                "Internal analysis: VRIN, value chain, financial capabilities, SWOT/TOWS",
                "Competitive strategy: generic strategies, ROIC, pricing power, competitive moats",
                "Corporate strategy: Ansoff, BCG, GE-McKinsey, M&A valuation, capital allocation",
                "Innovation: 3-horizon model, disruptive innovation, digital transformation, real options",
                "Value creation: EVA, Balanced Scorecard, DuPont, FCF signals, capital structure",
                "Implementation: 7-S framework, Kotter's change model, rolling forecasts, agile strategy",
                "Risk: strategic risk register, decision trees, scenario stress testing, resilience",
                "Global & ESG: CAGE, entry modes, ESG financial impact, stakeholder value mapping",
                "Strategic Finance: FP&A, driver-based modelling, NPV/IRR, business case development",
                "Capstone: integrated strategy project, financial plan, board presentation prep"
            ],
            "Focus Activity": [
                "Strategy classifier exercise + strategy map builder",
                "PESTLE impact scorer + Five Forces rater + TAM/SAM/SOM calculator",
                "VRIN assessor + value chain cost mapper + TOWS builder",
                "ROIC calculator + pricing power simulator + strategy scorer",
                "BCG portfolio analyser + M&A synergy calculator + capital allocation optimizer",
                "Innovation investment evaluator + digital ROI calculator + disruption radar",
                "EVA bridge calculator + Balanced Scorecard builder + DuPont analyser",
                "7-S alignment analyser + initiative prioritiser + rolling forecast builder",
                "Risk register builder + decision tree EV calculator + scenario stress test",
                "CAGE distance analyser + ESG financial impact calculator + stakeholder map",
                "Investment appraisal calculator (NPV/IRR) + driver model + business case builder",
                "Full capstone analysis + scenario financial plan + board presentation checklist"
            ]
        })
        st.dataframe(schedule_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("✅ My Progress Tracker")
        st.markdown("Track your completion of each module:")

        total_completed = 0
        for mod in modules_info:
            col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
            with col1:
                st.markdown(f"**{mod['icon']} Module {mod['num']}: {mod['title']}**")
            with col2:
                completed = st.checkbox("Completed ✅", key=f"bs_prog_done_{mod['num']}")
            with col3:
                practiced = st.checkbox("Practised 🧮", key=f"bs_prog_prac_{mod['num']}")
            with col4:
                confidence = st.select_slider(
                    "Confidence", ["❓", "😰", "😐", "😊", "🌟"],
                    value="😐", key=f"bs_prog_conf_{mod['num']}"
                )
            if completed:
                total_completed += 1

        overall_progress = total_completed / 12 * 100
        st.progress(overall_progress / 100)
        st.metric("Overall Progress", f"{total_completed}/12 modules ({overall_progress:.0f}%)")

        if total_completed == 12:
            st.success("🎉 🏆 Congratulations! You have completed all 12 modules of the Business Strategy curriculum! You are now equipped to operate as a true strategic finance professional.")
            st.balloons()

        st.markdown("---")
        st.subheader("📌 The 12 Golden Rules of Strategic Finance")

        rules = [
            ("1", "Strategy is a choice — not a plan",
             "Strategy = integrated choices about WHERE to compete, HOW to win, and WHAT to build. A plan without choices is just a budget.",
             "M1"),
            ("2", "ROIC vs WACC is the ultimate test",
             "ROIC > WACC = value creation. ROIC < WACC = value destruction, regardless of how 'busy' or 'growing' the business looks.",
             "M4, M7"),
            ("3", "External forces set the ceiling; internal capabilities determine your share",
             "Five Forces defines industry profit potential. VRIN defines YOUR capture rate within that potential.",
             "M2, M3"),
            ("4", "BCG logic: Cash Cows fund Stars — never starve your Stars",
             "The portfolio must be self-funding. Cash Cows generate the capital to invest in Stars and selective Question Marks.",
             "M5"),
            ("5", "Disruption starts where you're not looking",
             "Disruptors target your least profitable customers first. By the time they threaten your core, it's often too late. Finance must model displacement risk early.",
             "M6"),
            ("6", "The Balanced Scorecard is causal, not just measurement",
             "L&G capabilities → better processes → better customer outcomes → financial results. The arrows matter as much as the metrics.",
             "M7"),
            ("7", "67% of strategies fail in execution, not formulation",
             "7-S alignment gaps, resource misallocation, and incentive misalignment — not strategic thinking — kill most strategies.",
             "M8"),
            ("8", "Sunk costs are irrelevant — only future cash flows matter",
             "Past investment never justifies future investment. Every strategic decision must stand on its own incremental future cash flows.",
             "M9"),
            ("9", "ESG is not a cost — it is a source of value",
             "Strong ESG → lower WACC, better talent, customer preference, regulatory trust. Treat ESG as a strategic investment, not a compliance burden.",
             "M10"),
            ("10", "A business case without a 'Do Nothing' option is incomplete",
             "The Do Nothing option defines the cost of inaction — often the most powerful argument for investment. Always include it.",
             "M11"),
            ("11", "Lead with the financial punchline in the boardroom",
             "'This strategy grows ROIC from X% to Y% and creates $NM of EVA over 3 years.' Then explain how. Numbers first.",
             "M12"),
            ("12", "Finance professionals create most value by saying what others won't",
             "Challenge optimistic revenue synergies. Model the bear case. Quantify the risk of inaction. This intellectual honesty is the CFO's most valuable contribution.",
             "M1–12"),
        ]

        rules_df = pd.DataFrame(rules, columns=["#", "Rule", "Why It Matters", "Module(s)"])
        st.dataframe(rules_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔗 Module Connections — How Everything Links Together")
        st.markdown("""
        Understanding how modules connect deepens your mastery:

        | Connection | Strategic Logic |
        |-----------|----------------|
        | **M2 → M3** | External opportunities × Internal capabilities = Strategic fit (SWOT synthesis) |
        | **M3 → M4** | Internal VRIN strengths determine WHICH generic strategy is achievable |
        | **M4 → M7** | Generic strategy chosen → ROIC profile (margin-led vs turnover-led) → EVA |
        | **M2 + M3 → M5** | External TAM + Internal capabilities → Ansoff growth direction; BCG portfolio logic |
        | **M5 → M11** | M&A strategy from M5 → synergy modelling and NPV analysis in M11 |
        | **M6 → M7** | Innovation investment (real options) feeds into EVA and FCF trajectory |
        | **M7 → M8** | Balanced Scorecard from M7 is the KPI framework for M8 implementation |
        | **M8 → M9** | Rolling forecasts from M8 are the base for scenario stress testing in M9 |
        | **M9 → M11** | Risk scenarios from M9 feed into bear case financial model in M11 |
        | **M10 → M5** | CAGE distance analysis from M10 informs international M&A/entry in M5 |
        | **M10 → M7** | ESG from M10 reduces WACC — directly improving EVA in M7 |
        | **M11 → M12** | Driver-based model and business case from M11 are the financial engine of the Capstone |
        | **M1–11 → M12** | The Capstone synthesises ALL prior modules into one integrated strategic financial plan |
        """)

        st.success("🎓 Use this overview page as your constant companion throughout the course. Return to it for quick reference, formula lookup, progress tracking, and exam preparation — the strategic finance professional's handbook!")

if __name__ == "__main__":
    show()