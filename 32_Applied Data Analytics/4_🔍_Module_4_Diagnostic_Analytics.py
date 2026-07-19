import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Module 4 — Diagnostic Analytics", page_icon="🔍", layout="wide")

st.title("🔍 Module 4: Diagnostic Analytics — Variance & Root Cause")
st.caption("Learning goal: answer 'why did it happen?' using variance and correlation analysis.")

st.markdown(
    "Diagnostic analytics drills into a descriptive result to find the *cause*. "
    "The two workhorse techniques are **variance analysis** and **correlation analysis**."
)

st.divider()

# ----------------------------------------------------------------------------
# VARIANCE / WATERFALL
# ----------------------------------------------------------------------------
st.markdown("## 🌉 Interactive Variance Bridge: Budget → Actual")
st.markdown("Set the budget and actual for each P&L line, and see exactly what drove the profit variance.")

lines = ["Revenue", "COGS", "Marketing", "Salaries", "Other Opex"]
budget_defaults = [20000, 12000, 2000, 3000, 1000]
actual_defaults = [19000, 12500, 2600, 3000, 900]

st.markdown("**Budget vs Actual ($'000):**")
budget_vals, actual_vals = [], []
cols = st.columns(len(lines))
for i, line in enumerate(lines):
    with cols[i]:
        st.markdown(f"**{line}**")
        b = st.number_input(f"Budget - {line}", value=budget_defaults[i], step=100, key=f"b_{line}")
        a = st.number_input(f"Actual - {line}", value=actual_defaults[i], step=100, key=f"a_{line}")
        budget_vals.append(b)
        actual_vals.append(a)

budget_profit = budget_vals[0] - sum(budget_vals[1:])
actual_profit = actual_vals[0] - sum(actual_vals[1:])

# Build waterfall: start at budget profit, add/subtract each line's variance, end at actual profit
measures = ["absolute"]
x_labels = ["Budget Profit"]
y_values = [budget_profit]

for i, line in enumerate(lines):
    if line == "Revenue":
        var = actual_vals[i] - budget_vals[i]   # higher revenue = favorable (+)
    else:
        var = -(actual_vals[i] - budget_vals[i])  # higher cost = unfavorable (-)
    measures.append("relative")
    x_labels.append(f"{line} variance")
    y_values.append(var)

measures.append("total")
x_labels.append("Actual Profit")
y_values.append(actual_profit)

fig = go.Figure(go.Waterfall(
    x=x_labels,
    measure=measures,
    y=y_values,
    connector={"line": {"color": "rgba(120,120,120,0.5)"}},
    decreasing={"marker": {"color": "#E8684A"}},
    increasing={"marker": {"color": "#5AD8A6"}},
    totals={"marker": {"color": "#5B8FF9"}},
))
fig.update_layout(title="Profit Bridge: Budget → Actual", height=450, margin=dict(t=50))
st.plotly_chart(fig, use_container_width=True)

variance_total = actual_profit - budget_profit
if variance_total >= 0:
    st.success(f"Actual profit beat budget by **${variance_total:,.0f}k**. Biggest favorable driver: "
               f"{lines[np.argmax([ (actual_vals[i]-budget_vals[i]) if lines[i]=='Revenue' else -(actual_vals[i]-budget_vals[i]) for i in range(len(lines))])]}.")
else:
    worst_idx = np.argmin([(actual_vals[i]-budget_vals[i]) if lines[i]=='Revenue' else -(actual_vals[i]-budget_vals[i]) for i in range(len(lines))])
    st.error(f"Actual profit missed budget by **${-variance_total:,.0f}k**. Biggest unfavorable driver: **{lines[worst_idx]}**. "
             "This is where a finance manager should investigate first.")

st.divider()

# ----------------------------------------------------------------------------
# CORRELATION EXPLORER
# ----------------------------------------------------------------------------
st.markdown("## 🔗 Correlation Explorer: Relationship vs. Causation")
st.markdown(
    "Drag the slider to set how strongly two variables move together (e.g. *marketing spend* vs *sales*), "
    "and see how the scatter plot and correlation coefficient change."
)

corr_target = st.slider("Target correlation coefficient", -1.0, 1.0, 0.7, step=0.05)
n_points = 60
np.random.seed(42)
x = np.random.normal(50, 15, n_points)
noise = np.random.normal(0, 15, n_points)
y = corr_target * x + np.sqrt(max(1 - corr_target**2, 0)) * noise
actual_corr = np.corrcoef(x, y)[0, 1]

scatter_df = pd.DataFrame({"Marketing Spend ($'000)": x, "Sales ($'000)": y})
fig2 = px.scatter(scatter_df, x="Marketing Spend ($'000)", y="Sales ($'000)", trendline="ols",
                   title=f"Marketing Spend vs Sales (actual correlation ≈ {actual_corr:.2f})")
fig2.update_traces(marker=dict(size=9, color="#5B8FF9"))
st.plotly_chart(fig2, use_container_width=True)

st.warning(
    "⚠️ **Correlation is not causation.** A strong correlation between marketing spend and sales is "
    "*consistent with* marketing driving sales — but it could also be reverse causation (more sales budget "
    "allows more marketing) or a hidden third factor (e.g. seasonality) driving both. Diagnostic analytics "
    "narrows down causes; it doesn't always prove them. Controlled tests (e.g. A/B tests) get you closer to causation."
)

st.divider()
st.info("➡️ Next: **Module 5 — Predictive Analytics: Forecasting**, to project what happens next.")
