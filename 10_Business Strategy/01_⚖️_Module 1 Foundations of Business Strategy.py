import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🎯 Module 1: Foundations of Business Strategy")
    st.markdown("*Understand what strategy is, how it evolved, and how finance professionals drive strategic value*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. What Is Business Strategy?")
        st.markdown("""
        **Strategy** is a set of integrated choices about where to compete, how to compete, and what capabilities to build
        in order to create sustainable competitive advantage and long-term value.

        **Key distinctions:**
        - **Strategy** = Long-term direction and positioning (the "where and why")
        - **Tactics** = Short-term actions to execute strategy (the "how now")
        - **Operations** = Day-to-day processes and activities (the "what we do daily")
        """)

        compare_data = {
            "Dimension": ["Time Horizon", "Focus", "Who Decides", "Financial Link", "Examples"],
            "Strategy": ["3–10 years", "Competitive positioning, resource allocation", "CEO, Board, CFO", "Capital allocation, ROIC, long-range plan", "Enter new market, acquire competitor, divest unit"],
            "Tactics": ["Months–1 year", "Execution of strategic initiatives", "Business unit leaders", "Budgets, project ROI", "Launch product line, open new office, hire salesforce"],
            "Operations": ["Daily–weekly", "Efficiency, quality, service", "Functional managers", "Cost control, KPIs", "Process improvement, inventory management, customer service"]
        }
        st.dataframe(pd.DataFrame(compare_data), use_container_width=True, hide_index=True)

        st.subheader("2. The Three Levels of Strategy")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **🏢 Corporate Level**
            - Scope of the firm
            - Where to compete
            - Portfolio management
            - Capital allocation
            - M&A decisions
            - Diversification choices
            """)
        with col2:
            st.markdown("""
            **⚙️ Business Unit Level**
            - How to compete in a market
            - Competitive positioning
            - Cost vs. differentiation
            - Customer targeting
            - Pricing strategy
            - Competitive response
            """)
        with col3:
            st.markdown("""
            **🔧 Functional Level**
            - Finance strategy
            - Marketing strategy
            - Operations strategy
            - HR strategy
            - Technology strategy
            - Supply chain strategy
            """)

        st.subheader("3. Schools of Strategic Thought")
        schools_data = {
            "School": ["Design School", "Planning School", "Positioning School", "Resource-Based School", "Dynamic Capabilities"],
            "Core Idea": [
                "Strategy as fit between firm and environment (SWOT)",
                "Strategy as formal planning and structured processes",
                "Strategy as choosing competitive position in industry",
                "Strategy based on unique internal resources and capabilities",
                "Strategy as building capacity to adapt and innovate"
            ],
            "Key Tools": ["SWOT Analysis", "Strategic Planning Calendar", "Porter's Five Forces, Generic Strategies", "VRIN Framework, Value Chain", "Capability audits, Innovation pipeline"],
            "Finance Relevance": ["Align financial resources with external opportunities", "Long-range financial planning (LRP)", "ROIC by competitive position", "Capitalize on financial strength as a moat", "Invest in adaptable, scalable capabilities"]
        }
        st.dataframe(pd.DataFrame(schools_data), use_container_width=True, hide_index=True)

        st.subheader("4. The Strategic Management Process")
        st.markdown("""
        Strategy is not a one-time event — it is a continuous cycle:

        1. **Strategic Analysis** — Understand the external environment and internal capabilities
        2. **Strategy Formulation** — Develop strategic options and select the best path
        3. **Strategy Implementation** — Execute through plans, resources, structures, and systems
        4. **Strategic Evaluation** — Measure performance against strategic objectives and adapt

        **Finance professional's role in each phase:**
        - *Analysis*: Financial benchmarking, market sizing, economic modelling
        - *Formulation*: Investment appraisal, scenario modelling, capital allocation
        - *Implementation*: Budgeting, resource allocation, project governance
        - *Evaluation*: KPI design, financial dashboards, strategic reporting
        """)

        st.subheader("5. Vision, Mission, and Strategic Intent")
        st.markdown("""
        | Element | Definition | Finance Connection |
        |--------|-----------|-------------------|
        | **Vision** | Aspirational future state — where the company wants to be | Sets the long-term value creation target |
        | **Mission** | Purpose of the organization — why it exists | Defines the scope of capital deployment |
        | **Values** | Principles guiding behaviour and decisions | Shapes governance and risk culture |
        | **Strategic Intent** | Ambitious, stretching goal that focuses organizational energy | Drives investment priorities and resource allocation |
        | **Strategy** | Integrated plan to achieve the vision through competitive positioning | The financial plan made concrete |
        """)

        st.subheader("6. Finance as Strategic Partner")
        st.markdown("""
        The finance professional's role has evolved dramatically. The modern CFO is a **strategic co-pilot**:

        **Traditional Finance Role:** Scorekeeper → Record, report, control
        **Modern Finance Role:** Strategic Partner → Analyse, advise, drive decisions

        **How Finance Professionals Add Strategic Value:**
        - Translating strategy into quantified financial models
        - Challenging strategic assumptions with financial data
        - Providing business case rigour for investment decisions
        - Allocating capital to highest-return strategic priorities
        - Designing performance frameworks that incentivise strategic behaviour
        - Communicating strategy's financial impact to investors and board
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Strategy vs. Tactics vs. Operations")
        st.markdown("**Company: Global Retailer — Moving into E-Commerce**")
        example1 = {
            "Level": ["Strategy", "Tactics", "Operations"],
            "Decision": [
                "Shift from physical-only retail to omnichannel model to capture digital market growth",
                "Launch online store, hire 50 digital marketing staff, partner with logistics provider",
                "Process web orders within 24 hours, maintain 99.5% inventory accuracy, handle returns in 3 days"
            ],
            "Key Metrics": [
                "Online revenue % of total sales, Digital market share, ROIC from digital investments",
                "Online store launch date, Digital team productivity, Partnership NPS",
                "Order fulfilment rate, Returns rate, Customer service response time"
            ],
            "Finance Role": [
                "Build 5-year digital P&L model; evaluate capital required; assess ROIC vs. hurdle rate",
                "Approve project budgets; track ROI of marketing spend; monitor logistics costs",
                "Daily cost reporting; variance analysis; operational KPI dashboards"
            ]
        }
        st.dataframe(pd.DataFrame(example1), use_container_width=True, hide_index=True)

        st.subheader("Example 2: The Three Levels in Action — Apple Inc.")
        st.markdown("""
        **Corporate Level Strategy:**
        - Compete in smartphones, computers, wearables, services, and entertainment
        - Capital allocation: $90B+ annual R&D and capex; massive share buyback programme
        - Diversification into services (App Store, Apple Music, iCloud) for recurring revenue

        **Business Unit Level Strategy (iPhone):**
        - Differentiation strategy: premium positioning, ecosystem lock-in, brand premium
        - NOT competing on price — maintaining 40%+ gross margins despite lower market share than Android
        - Competitive response: rapid feature iteration, supply chain exclusivity

        **Functional Level Strategy (Finance):**
        - Maintain fortress balance sheet ($160B+ cash) as strategic optionality
        - Use low-cost debt for buybacks to enhance EPS
        - Manage foreign exchange exposure from $300B+ international revenue
        """)
        st.info("💡 **Finance Insight**: Apple's CFO allocates capital across the three levels simultaneously — deciding which business units grow, how much to return to shareholders, and how to fund the functional investments that sustain each unit's competitive position.")

        st.subheader("Example 3: Mission–Vision–Strategy Alignment")
        st.markdown("""
        **Tesla Inc. — Strategic Alignment Example**

        | Element | Tesla's Answer |
        |---------|---------------|
        | Mission | "To accelerate the world's transition to sustainable energy" |
        | Vision | Leader in electric vehicles, energy storage, and solar globally |
        | Strategic Intent | Make EVs affordable and accessible to mass market |
        | Corporate Strategy | Vertical integration across EVs, batteries, energy, and software |
        | Finance Strategy | Scale manufacturing aggressively; sacrifice near-term margins for market position; raise capital from equity markets to fund growth |

        **CFO's strategic challenge:** Balance growth investment (negative FCF) against investor expectations for profitability — and communicate a credible long-range financial model that justifies the strategy.
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("Interactive Tools")

        st.subheader("🧮 Strategy Level Classifier")
        st.markdown("Classify the following business decision to understand which level of strategy it belongs to:")

        decision_input = st.text_area("Describe a business decision:", value="We are considering acquiring a smaller competitor to expand our market share in Southeast Asia.", height=80)

        time_horizon = st.select_slider("Time Horizon:", options=["Days/Weeks", "Months", "1–2 Years", "3–5 Years", "5+ Years"], value="3–5 Years")
        who_decides = st.multiselect("Who is involved in this decision?", ["CEO", "CFO", "Board", "Business Unit Head", "Marketing Director", "Operations Manager", "Finance Analyst"], default=["CEO", "CFO", "Board"])
        resource_level = st.radio("Scale of Resource Commitment:", ["Minor (< $100K)", "Moderate ($100K–$1M)", "Major ($1M–$50M)", "Transformational ($50M+)"])

        if st.button("Classify Decision"):
            score = 0
            if time_horizon in ["3–5 Years", "5+ Years"]: score += 3
            elif time_horizon in ["1–2 Years"]: score += 2
            else: score += 1
            strategic_roles = [r for r in who_decides if r in ["CEO", "CFO", "Board"]]
            score += len(strategic_roles)
            if resource_level == "Transformational ($50M+)": score += 3
            elif resource_level == "Major ($1M–$50M)": score += 2
            elif resource_level == "Moderate ($100K–$1M)": score += 1

            if score >= 6:
                st.success("🏢 **Corporate-Level Strategy Decision**")
                st.markdown("This is a major strategic decision affecting the scope and direction of the entire organization. Requires board approval, detailed financial modelling, due diligence, and a comprehensive business case.")
            elif score >= 4:
                st.info("⚙️ **Business Unit-Level Strategy Decision**")
                st.markdown("This decision shapes how a specific business unit competes. Requires competitive analysis, market assessment, and a financial investment case approved by senior leadership.")
            else:
                st.warning("🔧 **Functional/Tactical Decision**")
                st.markdown("This is an operational or tactical decision within a function. Still needs financial justification, but within existing strategic and budget parameters.")

        st.markdown("---")
        st.subheader("🗺️ Strategy Map Builder")
        st.markdown("Define your organisation's strategic alignment across the four perspectives of the Strategy Map:")

        col1, col2 = st.columns(2)
        with col1:
            financial_goal = st.text_input("💰 Financial Perspective Goal:", value="Grow revenue by 15% and achieve 20% ROIC")
            customer_goal = st.text_input("👥 Customer Perspective Goal:", value="Become the preferred partner for mid-market clients")
        with col2:
            process_goal = st.text_input("⚙️ Internal Process Goal:", value="Reduce cost-to-serve by 25% through automation")
            learning_goal = st.text_input("🎓 Learning & Growth Goal:", value="Build digital and data analytics capabilities across teams")

        if st.button("Generate Strategy Map Summary"):
            st.markdown("---")
            st.markdown("### 📊 Your Strategy Map")
            st.markdown(f"""
            | Perspective | Strategic Objective | Finance Implication |
            |-------------|--------------------|--------------------|
            | 💰 Financial | {financial_goal} | Revenue model, margin targets, ROIC hurdle rate |
            | 👥 Customer | {customer_goal} | Customer acquisition cost, CLV, NPS investment |
            | ⚙️ Internal Process | {process_goal} | Process investment budget, productivity metrics |
            | 🎓 Learning & Growth | {learning_goal} | Training capex, talent investment, capability build cost |
            """)
            st.success("✅ A well-aligned strategy map creates a cause-and-effect chain: Learning & Growth capabilities → Better processes → Happier customers → Financial results.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("The Strategic Management Cycle")
        phases = ["Strategic\nAnalysis", "Strategy\nFormulation", "Strategy\nImplementation", "Strategy\nEvaluation"]
        colors = ["#2563EB", "#0D7377", "#D97706", "#7C3AED"]
        fig_cycle = go.Figure()
        angles = [90, 0, 270, 180]
        x_pos = [0, 1.5, 1.5, 0]
        y_pos = [1.5, 1.5, 0, 0]
        for i, (phase, color, x, y) in enumerate(zip(phases, colors, x_pos, y_pos)):
            fig_cycle.add_trace(go.Scatter(
                x=[x], y=[y], mode="markers+text",
                marker=dict(size=80, color=color, opacity=0.85),
                text=[phase], textposition="middle center",
                textfont=dict(color="white", size=11, family="Arial"),
                showlegend=False
            ))
        fig_cycle.add_annotation(x=0.75, y=1.5, text="→", font=dict(size=30, color="#64748B"), showarrow=False)
        fig_cycle.add_annotation(x=1.5, y=0.75, text="↓", font=dict(size=30, color="#64748B"), showarrow=False)
        fig_cycle.add_annotation(x=0.75, y=0, text="←", font=dict(size=30, color="#64748B"), showarrow=False)
        fig_cycle.add_annotation(x=0, y=0.75, text="↑", font=dict(size=30, color="#64748B"), showarrow=False)
        fig_cycle.update_layout(title="The Strategic Management Cycle", height=400,
                                xaxis=dict(visible=False, range=[-0.5, 2]),
                                yaxis=dict(visible=False, range=[-0.5, 2]),
                                plot_bgcolor="white")
        st.plotly_chart(fig_cycle, use_container_width=True)

        st.subheader("Finance Professional's Evolving Strategic Role")
        roles = ["Cost Controller", "Financial Analyst", "Business Partner", "Strategic Advisor", "CFO / Strategic Co-Pilot"]
        impact = [20, 40, 60, 80, 100]
        skills = ["Reporting & compliance", "Analysis & modelling", "Commercial insight", "Strategic challenge", "Vision & leadership"]
        fig_role = go.Figure(go.Bar(
            x=roles, y=impact,
            marker_color=["#94A3B8", "#60A5FA", "#34D399", "#FBBF24", "#1B3A6B"],
            text=[f"{v}% Strategic Impact" for v in impact],
            textposition="auto",
            textfont=dict(color="white", size=11)
        ))
        fig_role.update_layout(
            title="Finance Professional — Evolution of Strategic Contribution",
            xaxis_title="Role Level", yaxis_title="Strategic Value Added (%)",
            yaxis=dict(range=[0, 115]), height=400
        )
        st.plotly_chart(fig_role, use_container_width=True)

        st.subheader("Three Levels of Strategy — Resource Allocation")
        levels = ["Corporate Strategy", "Business Unit Strategy", "Functional Strategy"]
        time_h = [7, 4, 1.5]
        capital = [85, 55, 20]
        fig_levels = go.Figure()
        fig_levels.add_trace(go.Bar(name="Avg. Time Horizon (Years)", x=levels, y=time_h, marker_color="#2563EB"))
        fig_levels.add_trace(go.Bar(name="Typical Capital Commitment ($M)", x=levels, y=capital, marker_color="#0D7377"))
        fig_levels.update_layout(barmode="group", title="Three Strategy Levels — Key Characteristics", height=400)
        st.plotly_chart(fig_levels, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding of Strategy Foundations")

        st.markdown("**1. What is the primary difference between strategy and tactics?**")
        q1 = st.radio("", [
            "Strategy is about cutting costs; tactics are about growing revenue",
            "Strategy sets long-term direction and positioning; tactics are short-term actions to execute it",
            "Strategy is decided by analysts; tactics by the CEO",
            "There is no meaningful difference between strategy and tactics"
        ], key="bs1q1")
        if st.button("Check Answer", key="bs1c1"):
            if q1 == "Strategy sets long-term direction and positioning; tactics are short-term actions to execute it":
                st.success("✅ Correct! Strategy defines WHERE and WHY, while tactics define HOW in the short term.")
            else:
                st.error("❌ Incorrect. Strategy defines long-term direction and competitive positioning; tactics are short-term execution actions.")

        st.markdown("---")
        st.markdown("**2. At which level of strategy are decisions about diversification and M&A made?**")
        q2 = st.radio("", ["Functional level", "Operational level", "Business unit level", "Corporate level"], key="bs1q2")
        if st.button("Check Answer", key="bs1c2"):
            if q2 == "Corporate level":
                st.success("✅ Correct! Corporate strategy determines the scope of the firm — which businesses to own, acquire, or divest.")
            else:
                st.error("❌ Incorrect. M&A and diversification are corporate-level decisions about the overall scope of the firm.")

        st.markdown("---")
        st.markdown("**3. The Resource-Based View of strategy focuses on:**")
        q3 = st.radio("", [
            "Choosing the most attractive industry to compete in",
            "Formal annual planning processes",
            "Building unique internal capabilities and resources as the basis for advantage",
            "Setting financial budgets for each business unit"
        ], key="bs1q3")
        if st.button("Check Answer", key="bs1c3"):
            if q3 == "Building unique internal capabilities and resources as the basis for advantage":
                st.success("✅ Correct! The Resource-Based View holds that sustainable advantage comes from unique, hard-to-copy internal capabilities (VRIN).")
            else:
                st.error("❌ Incorrect. The Resource-Based View focuses on internal resources and capabilities as the source of competitive advantage.")

        st.markdown("---")
        st.markdown("**4. A finance professional acting as a 'strategic partner' would:**")
        q4 = st.radio("", [
            "Only prepare financial reports after decisions are made",
            "Focus exclusively on cost control and variance analysis",
            "Actively shape strategy by modelling financial scenarios, challenging assumptions, and driving capital allocation decisions",
            "Avoid involvement in strategic discussions to maintain independence"
        ], key="bs1q4")
        if st.button("Check Answer", key="bs1c4"):
            if q4 == "Actively shape strategy by modelling financial scenarios, challenging assumptions, and driving capital allocation decisions":
                st.success("✅ Correct! A strategic finance partner proactively contributes to strategy — not just reports on it.")
            else:
                st.error("❌ Incorrect. Strategic finance professionals proactively shape decisions through financial insight and modelling.")

        st.markdown("---")
        st.markdown("**5. In the Strategic Management Cycle, what comes BEFORE strategy formulation?**")
        q5 = st.radio("", ["Strategy implementation", "Strategy evaluation", "Strategic analysis", "Capital allocation"], key="bs1q5")
        if st.button("Check Answer", key="bs1c5"):
            if q5 == "Strategic analysis":
                st.success("✅ Correct! Analysis (understanding the environment and capabilities) must precede formulation of strategy.")
            else:
                st.error("❌ Incorrect. Strategic Analysis (external + internal environment) comes first, then formulation, implementation, and evaluation.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")

        st.markdown("""
        ### 1. Defining Business Strategy
        - Strategy = integrated choices about **where to compete, how to compete, and what capabilities to build**
        - Strategy differs from tactics (short-term execution) and operations (daily activities)
        - Strategy operates at three levels: **Corporate, Business Unit, and Functional**

        ### 2. The Three Levels of Strategy
        | Level | Focus | Finance Role |
        |-------|-------|-------------|
        | Corporate | Scope, portfolio, M&A, diversification | Capital allocation, valuation, portfolio analysis |
        | Business Unit | Competitive positioning, pricing, product | ROIC analysis, business case, pricing modelling |
        | Functional | Finance, marketing, HR, ops strategies | Budget, metrics, performance tracking |

        ### 3. Schools of Strategic Thought
        - **Design School**: Strategy as fit (SWOT)
        - **Planning School**: Formal strategy planning process
        - **Positioning School**: Industry positioning (Porter)
        - **Resource-Based School**: Internal capabilities (VRIN)
        - **Dynamic Capabilities**: Adaptability and innovation

        ### 4. The Strategic Management Process
        ```
        Strategic Analysis → Strategy Formulation → Implementation → Evaluation → (repeat)
        ```

        ### 5. Finance as Strategic Partner
        - Evolved from **scorekeeper → strategic co-pilot**
        - Finance professionals contribute at every stage of the strategy cycle
        - Key activities: scenario modelling, capital allocation, business case development, strategic KPIs

        ### 6. Key Frameworks Introduced
        | Framework | Purpose |
        |-----------|---------|
        | Strategy Map | Link learning → process → customer → financial outcomes |
        | SWOT | Identify strategic fit between firm and environment |
        | Strategic Management Cycle | Guide continuous strategy development |
        | Three Levels Framework | Align decisions to the right strategic level |
        """)

        st.subheader("📌 Key Formulas")
        st.code("Strategic Value = Competitive Advantage × Scale of Opportunity × Execution Quality")
        st.code("Finance Strategic Contribution = Analysis Insight + Capital Allocation Skill + Financial Storytelling")

        st.success("🎓 **Module 1 Complete!** You now understand the foundations of business strategy and the role of finance professionals in shaping strategic direction.")
        st.info("💡 **Next**: Module 2 — External Environment Analysis (PESTLE + Five Forces + Scenario Planning)")

if __name__ == "__main__":
    show()