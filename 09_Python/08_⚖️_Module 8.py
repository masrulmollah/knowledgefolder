import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 8: Visualization",
        page_icon="📊",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("📊 Module 8: Visualization for Executive Reporting")
st.markdown("""
A spreadsheet tells a story, but a chart provides the "Aha!" moment. In this module, we use **Plotly** to build interactive, audit-ready visualizations that help stakeholders identify trends and outliers instantly.
""")

st.divider()

# --- SECTION 1: TREND ANALYSIS (LINE CHARTS) ---
st.header("1. Visualizing Trends Over Time")
st.write("Line charts are essential for monitoring Revenue, OPEX, or Cash Flow trends.")

# Generate Dummy Time Series Data
dates = pd.date_range(start="2025-01-01", periods=12, freq="M")
data_trends = pd.DataFrame({
    "Month": dates,
    "Actual_Spend": [120, 135, 130, 145, 160, 155, 150, 170, 185, 180, 195, 210],
    "Budget": [130] * 12
})

fig_line = px.line(
    data_trends, 
    x="Month", 
    y=["Actual_Spend", "Budget"],
    title="Monthly OPEX vs. Budget (Interactive)",
    labels={"value": "Amount (000s)", "variable": "Category"},
    markers=True,
    template="plotly_white"
)

st.plotly_chart(fig_line, use_container_width=True)

st.code("""
import plotly.express as px
fig = px.line(df, x='Month', y=['Actual', 'Budget'], title='Trend Analysis')
st.plotly_chart(fig)
""", language="python")

st.divider()

# --- SECTION 2: COMPOSITION & VARIANCES (BAR & PIE) ---
st.header("2. Analyzing Cost Composition")
st.write("Bar charts and Pie charts help executive teams understand where the money is going.")

# Sample Cost Data
cost_data = pd.DataFrame({
    "Category": ["Raw Materials", "Labor", "Utilities", "Logistics", "Maintenance"],
    "Amount": [450000, 320000, 120000, 95000, 65000]
})

col1, col2 = st.columns(2)

with col1:
    chart_type = st.radio("Select Visualization Type", ["Bar Chart", "Pie Chart"])
    
    if chart_type == "Bar Chart":
        fig_cost = px.bar(cost_data, x="Category", y="Amount", color="Category", text_auto='.2s')
    else:
        fig_cost = px.pie(cost_data, values="Amount", names="Category", hole=0.4)
    
    st.plotly_chart(fig_cost, use_container_width=True)

with col2:
    st.subheader("Data Insights")
    st.write("Interactive charts allow you to:")
    st.markdown("""
    * **Hover:** See exact values without looking at a table.
    * **Isolate:** Click 'Utilities' in the legend to hide it and compare other costs.
    * **Export:** Download the chart as a PNG directly from the dashboard.
    """)

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 8 Quiz")
st.write("Choosing the right tool for the job.")

q_viz = st.radio(
    "Which type of chart is best for showing the 'Actual vs. Budget' variance across 10 different Cost Centers simultaneously?",
    ["Pie Chart", "Grouped Bar Chart", "Scatter Plot"]
)

if st.button("Check Visualization Logic"):
    if q_viz == "Grouped Bar Chart":
        st.balloons()
        st.success("Correct! Grouped Bar Charts allow for side-by-side comparison of two metrics (Actual vs Budget) across categories.")
    else:
        st.error("Not quite. Pie charts are for parts-of-a-whole, while Bar charts are superior for direct comparisons.")

st.markdown("---")
st.caption("Knowledge Folder | Module 8: Visualization for Executive Reporting")