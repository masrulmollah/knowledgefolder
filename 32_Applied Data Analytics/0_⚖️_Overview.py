import streamlit as st

st.set_page_config(
    page_title="Applied Data Analytics for Finance Professionals",
    page_icon="📊",
    layout="wide",
)

# ----------------------------------------------------------------------------
# SESSION STATE (used to track module completion across the app)
# ----------------------------------------------------------------------------
MODULES = [
    ("Module 1", "Foundations & Types of Data Analytics", "1_🧭_Module_1_Foundations.py"),
    ("Module 2", "The Data Analytics Process", "2_🔄_Module_2_The_Analytics_Process.py"),
    ("Module 3", "Descriptive Analytics — Ratios & Trends", "3_📊_Module_3_Descriptive_Analytics.py"),
    ("Module 4", "Diagnostic Analytics — Variance & Root Cause", "4_🔍_Module_4_Diagnostic_Analytics.py"),
    ("Module 5", "Predictive Analytics — Forecasting", "5_📈_Module_5_Predictive_Forecasting.py"),
    ("Module 6", "Predictive Analytics — Risk & Monte Carlo Simulation", "6_🎲_Module_6_Risk_Scenario_Simulation.py"),
    ("Module 7", "Prescriptive Analytics — Optimization & Decisions", "7_🎯_Module_7_Prescriptive_Optimization.py"),
    ("Module 8", "Data Visualization & Dashboards for Finance", "8_📉_Module_8_Data_Visualization_Dashboards.py"),
    ("Module 9", "Capstone Project — End-to-End Case Study", "9_🏆_Module_9_Capstone_Project.py"),
]

if "completed" not in st.session_state:
    st.session_state.completed = {m[0]: False for m in MODULES}

# ----------------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------------
st.title("📊 Applied Data Analytics — for Finance Professionals")
st.subheader("Learn by doing: adjust the numbers, watch the analysis change.")

st.markdown(
    """
Welcome! This section is a **hands-on curriculum** that takes a finance manager from
*"what is data analytics?"* all the way to confidently running descriptive, diagnostic,
predictive and prescriptive analysis on real finance problems — budgeting, forecasting,
variance analysis, risk simulation, and resource allocation.

Every module is **interactive**: you change inputs (revenue, budgets, growth rates,
probabilities...) with sliders and see the charts, ratios, and insights update live.
There is no substitute for doing — so each module ends with a short exercise.
"""
)

st.divider()

# ----------------------------------------------------------------------------
# WHY THIS MATTERS
# ----------------------------------------------------------------------------
col1, col2 = st.columns([1.3, 1])
with col1:
    st.markdown("### 🎯 What you will be able to do by the end")
    st.markdown(
        """
    1. **Follow a repeatable process** for any analytics problem — from defining the
       question to communicating a recommendation.
    2. **Diagnose which type of analytics** (descriptive, diagnostic, predictive,
       prescriptive) fits a given business question.
    3. **Extract insights** from financial data using ratios, trends, variance and
       correlation analysis.
    4. **Forecast and simulate risk** using moving averages, exponential smoothing,
       regression, and Monte Carlo simulation.
    5. **Support decision-making** with optimization and expected-value techniques.
    6. **Highlight improvement areas and opportunities**, and communicate them through
       well-designed dashboards.
    """
    )
with col2:
    st.markdown("### 🧭 How to navigate")
    st.info(
        "Use the **sidebar** (left) to move between the Overview and each Module page. "
        "Modules are numbered — we recommend going in order the first time through, "
        "then returning to any module for reference."
    )
    st.markdown("### ✅ Track your progress")
    for code, title, _ in MODULES:
        st.session_state.completed[code] = st.checkbox(
            f"{code}: {title}", value=st.session_state.completed[code], key=f"chk_{code}"
        )
    done = sum(st.session_state.completed.values())
    st.progress(done / len(MODULES))
    st.caption(f"{done} / {len(MODULES)} modules marked complete")

st.divider()

# ----------------------------------------------------------------------------
# FULL SYLLABUS
# ----------------------------------------------------------------------------
st.markdown("## 📘 Full Syllabus")

syllabus = [
    {
        "mod": "Module 1 — Foundations & Types of Data Analytics",
        "goal": "Understand what analytics is and self-diagnose which type (descriptive, "
                "diagnostic, predictive, prescriptive) fits a given finance question.",
        "topics": [
            "The four types of analytics and the questions each answers",
            "Interactive diagnostic tool: 'which type of analytics do I need?'",
            "Finance examples for each type (variance reports, forecasting, budget optimization...)",
        ],
    },
    {
        "mod": "Module 2 — The Data Analytics Process",
        "goal": "Learn the repeatable, end-to-end process analysts follow, and practice it "
                "on a mini finance case.",
        "topics": [
            "Define objective → Collect → Clean → Explore → Analyze → Interpret → Communicate → Act → Monitor",
            "Interactive data-cleaning exercise (missing values, duplicates, outliers)",
            "Applying the process to a declining-gross-margin scenario",
        ],
    },
    {
        "mod": "Module 3 — Descriptive Analytics: Ratios & Trend Analysis",
        "goal": "Answer 'what happened?' using financial ratios, KPIs and trend charts.",
        "topics": [
            "Profitability, liquidity, leverage and efficiency ratios",
            "Interactive P&L / balance sheet sliders that recompute ratios and KPI cards live",
            "Multi-year trend visualization and automatic insight flags",
        ],
    },
    {
        "mod": "Module 4 — Diagnostic Analytics: Variance & Root Cause",
        "goal": "Answer 'why did it happen?' using variance and correlation analysis.",
        "topics": [
            "Budget-vs-actual variance bridge (waterfall chart)",
            "Favorable vs unfavorable variance interpretation",
            "Correlation explorer: strength of relationship vs causation",
        ],
    },
    {
        "mod": "Module 5 — Predictive Analytics: Forecasting",
        "goal": "Answer 'what will happen?' using classic forecasting techniques.",
        "topics": [
            "Moving average and exponential smoothing (adjustable window / alpha)",
            "Linear regression trend forecasting",
            "Comparing forecast accuracy (MAPE, RMSE) across methods",
        ],
    },
    {
        "mod": "Module 6 — Predictive Analytics: Risk & Monte Carlo Simulation",
        "goal": "Quantify uncertainty in financial projections.",
        "topics": [
            "Monte Carlo simulation for NPV / cash-flow projections",
            "Adjustable growth rate, discount rate, and volatility assumptions",
            "Probability of loss, percentile outcomes, and risk interpretation",
        ],
    },
    {
        "mod": "Module 7 — Prescriptive Analytics: Optimization & Decisions",
        "goal": "Answer 'what should we do?' using optimization and decision analysis.",
        "topics": [
            "Budget allocation optimizer with diminishing returns",
            "Expected value / decision-tree calculator for scenario-based decisions",
            "Turning analysis into a concrete recommendation",
        ],
    },
    {
        "mod": "Module 8 — Data Visualization & Dashboards for Finance",
        "goal": "Communicate insights effectively and pick the right chart for the job.",
        "topics": [
            "Chart-type recommender based on the nature of your data",
            "Build a live KPI dashboard from adjustable inputs",
            "Dashboard design principles for finance audiences",
        ],
    },
    {
        "mod": "Module 9 — Capstone Project: End-to-End Case Study",
        "goal": "Apply everything to one integrated case, from question to recommendation.",
        "topics": [
            "A realistic 'declining margin' case at a fictional company",
            "Identify analytics type → clean/explore → diagnose → forecast → decide",
            "Generate a one-page management summary of your findings",
        ],
    },
]

for item in syllabus:
    with st.expander(f"**{item['mod']}**"):
        st.markdown(f"**Learning goal:** {item['goal']}")
        st.markdown("**Topics & exercises:**")
        for t in item["topics"]:
            st.markdown(f"- {t}")

st.divider()
st.markdown(
    """
### 🚀 Ready to start?
Head to **Module 1** in the sidebar to begin, or jump straight to any module you need.
Every page is self-contained and interactive — change the numbers and see what happens!
"""
)
