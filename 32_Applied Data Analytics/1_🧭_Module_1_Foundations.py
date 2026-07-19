import streamlit as st
import pandas as pd

st.set_page_config(page_title="Module 1 — Foundations", page_icon="🧭", layout="wide")

st.title("🧭 Module 1: Foundations & Types of Data Analytics")
st.caption("Learning goal: know the four types of analytics and diagnose which one your question needs.")

st.markdown(
    """
Every analytics question a finance manager faces falls into one of **four types**.
Knowing which type you're dealing with tells you which techniques and tools to reach for.
"""
)

# ----------------------------------------------------------------------------
# THE FOUR TYPES — REFERENCE TABLE
# ----------------------------------------------------------------------------
data = {
    "Type": ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    "Core Question": ["What happened?", "Why did it happen?", "What will happen?", "What should we do?"],
    "Finance Example": [
        "Monthly P&L summary, ratio dashboard, KPI trend",
        "Why did gross margin drop 3 points this quarter?",
        "Forecasting next quarter's revenue or cash flow",
        "Which budget allocation maximizes ROI?",
    ],
    "Typical Techniques": [
        "Summary stats, ratios, trend charts",
        "Variance analysis, drill-down, correlation",
        "Moving average, regression, Monte Carlo",
        "Optimization, decision trees, expected value",
    ],
}
st.markdown("### 📚 The Four Types of Analytics")
st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

st.divider()

# ----------------------------------------------------------------------------
# INTERACTIVE DIAGNOSTIC TOOL
# ----------------------------------------------------------------------------
st.markdown("## 🔧 Interactive Tool: Which Type of Analytics Do I Need?")
st.markdown("Answer these questions about the situation you're facing, and we'll recommend an analytics type.")

c1, c2 = st.columns(2)
with c1:
    knows_what = st.radio(
        "Do you already know **what** happened (e.g. you have the numbers), "
        "or are you still trying to summarize the situation?",
        ["I need to summarize/report what happened", "I already know what happened"],
    )
    wants_cause = st.radio(
        "Are you trying to understand the **cause** behind a result (e.g. a variance)?",
        ["Yes, I need to find the cause", "No, that's not my focus right now"],
    )
with c2:
    wants_future = st.radio(
        "Do you need to know something about the **future** (e.g. next quarter)?",
        ["Yes, I need a forecast or risk estimate", "No"],
    )
    wants_action = st.radio(
        "Do you need a recommendation on the **best action** to take given constraints "
        "(e.g. budget, capacity)?",
        ["Yes, I need the optimal decision", "No, I just need analysis, not a decision"],
    )

# simple rule-based recommender
recommend = []
if knows_what.startswith("I need to summarize"):
    recommend.append("Descriptive")
if wants_cause.startswith("Yes"):
    recommend.append("Diagnostic")
if wants_future.startswith("Yes"):
    recommend.append("Predictive")
if wants_action.startswith("Yes"):
    recommend.append("Prescriptive")

if not recommend:
    recommend = ["Descriptive"]

st.markdown("### 🎯 Recommendation")
st.success(
    f"Based on your answers, start with **{', then '.join(recommend)}** analytics. "
    "It's common for a real finance question to need more than one type in sequence — "
    "e.g. Descriptive (see the drop) → Diagnostic (find the cause) → Predictive (project forward) "
    "→ Prescriptive (decide what to do)."
)

st.divider()

# ----------------------------------------------------------------------------
# QUICK QUIZ
# ----------------------------------------------------------------------------
st.markdown("## ✏️ Quick Self-Check")
q = st.selectbox(
    "\"Our churned-customer revenue rose 12% last month — which technique should we reach for FIRST "
    "to understand why?\"",
    ["-- choose an answer --", "Monte Carlo simulation", "Variance / correlation analysis (Diagnostic)",
     "Linear regression forecast", "Budget optimization"],
)
if q != "-- choose an answer --":
    if q == "Variance / correlation analysis (Diagnostic)":
        st.success("Correct! You already know *what* happened (revenue rose); next you need to know *why* — that's Diagnostic analytics.")
    else:
        st.error("Not quite. You already know what happened — the next step is to find the *cause*, which is Diagnostic analytics.")

st.divider()
st.info("➡️ Next: **Module 2 — The Data Analytics Process**, where you'll learn the step-by-step workflow analysts use.")
