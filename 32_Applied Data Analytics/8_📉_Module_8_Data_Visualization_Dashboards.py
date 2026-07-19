import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Module 8 — Visualization & Dashboards", page_icon="📉", layout="wide")

st.title("📉 Module 8: Data Visualization & Dashboards for Finance")
st.caption("Learning goal: pick the right chart for the job, and build a clear KPI dashboard.")

st.markdown(
    "Great analysis fails if it's poorly communicated. This module covers choosing the "
    "right chart type and building a clean, decision-ready dashboard."
)

st.divider()

# ----------------------------------------------------------------------------
# CHART TYPE RECOMMENDER
# ----------------------------------------------------------------------------
st.markdown("## 🧭 Chart-Type Recommender")
st.markdown("Answer these about your data, and we'll suggest the right chart.")

c1, c2 = st.columns(2)
with c1:
    nature = st.radio("What's the nature of your data?", [
        "Change over time (e.g. monthly revenue)",
        "Comparison across categories (e.g. spend by department)",
        "Composition / parts of a whole (e.g. cost breakdown)",
        "Relationship between two variables (e.g. spend vs sales)",
    ])
with c2:
    n_items = st.radio("How many categories / series are involved?", ["Few (2-6)", "Many (7+)"])

recommendation = ""
if nature.startswith("Change over time"):
    recommendation = "**Line chart** — shows trend and direction clearly over time. Use bars only if you want to emphasize discrete period-to-period comparison."
elif nature.startswith("Comparison across categories"):
    recommendation = "**Bar chart** (horizontal if labels are long, or many categories)."
elif nature.startswith("Composition"):
    recommendation = "**Stacked bar** for composition over time, or a **single pie/donut** only for a one-time snapshot with few (≤5) categories. Avoid pie charts with many slices or for time comparisons."
else:
    recommendation = "**Scatter plot** (with trendline) — best for showing correlation or relationship strength between two numeric variables."

if n_items == "Many (7+)" and "pie" in recommendation.lower():
    recommendation += " ⚠️ With many categories, a pie chart becomes unreadable — use a sorted bar chart instead."

st.success(f"**Recommended chart:** {recommendation}")

st.divider()

# ----------------------------------------------------------------------------
# LIVE DASHBOARD BUILDER
# ----------------------------------------------------------------------------
st.markdown("## 🏗️ Build a Live KPI Dashboard")
st.markdown("Adjust the inputs — the dashboard below updates instantly, just like a real BI tool.")

c1, c2, c3 = st.columns(3)
revenue_growth = c1.slider("YoY Revenue Growth (%)", -10, 40, 12)
margin_pct = c2.slider("Gross Margin (%)", 5, 60, 38)
cash_runway = c3.slider("Cash Runway (months)", 1, 36, 14)

k1, k2, k3 = st.columns(3)
k1.metric("Revenue Growth (YoY)", f"{revenue_growth}%", delta=f"{revenue_growth-10}pp vs target (10%)")
k2.metric("Gross Margin", f"{margin_pct}%", delta=f"{margin_pct-35}pp vs target (35%)")
k3.metric("Cash Runway", f"{cash_runway} months", delta=f"{cash_runway-12} vs 12mo minimum")

months = pd.date_range("2025-01-01", periods=12, freq="MS")
np.random.seed(3)
rev = 100 * (1 + revenue_growth/100/12) ** np.arange(12) + np.random.normal(0, 3, 12)
dept_spend = pd.DataFrame({
    "Department": ["Sales", "Marketing", "R&D", "Ops", "G&A"],
    "Spend ($'000)": [420, 310, 260, 180, 140],
})
cost_breakdown = pd.DataFrame({
    "Category": ["COGS", "Salaries", "Marketing", "Rent", "Other"],
    "Amount": [100 - margin_pct, 30, 12, 8, 5],
})

col1, col2 = st.columns(2)
with col1:
    fig1 = px.line(x=months, y=rev, markers=True, title="Monthly Revenue Trend ($'000)",
                    labels={"x": "Month", "y": "Revenue"})
    fig1.update_traces(line_color="#5B8FF9")
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    fig2 = px.bar(dept_spend.sort_values("Spend ($'000)"), x="Spend ($'000)", y="Department",
                   orientation="h", title="Spend by Department ($'000)", color_discrete_sequence=["#5AD8A6"])
    st.plotly_chart(fig2, use_container_width=True)

fig3 = px.pie(cost_breakdown, names="Category", values="Amount", title="Cost Structure (% of Revenue)", hole=0.4)
st.plotly_chart(fig3, use_container_width=True)

st.divider()
st.markdown(
    """
### 🎨 Dashboard Design Principles for Finance Audiences
- **Lead with the decision-relevant number**, not every number you have.
- **Consistent color meaning**: e.g. always green = favorable, red = unfavorable, across every chart.
- **Avoid 3D charts and excessive decimals** — they add noise, not insight.
- **Order matters**: put the most important KPI top-left (where eyes go first).
- **One message per chart** — if you need three sentences to explain a chart, split it into two.
"""
)

st.divider()
st.info("➡️ Next: **Module 9 — Capstone Project**, where you apply every module to one integrated case.")
