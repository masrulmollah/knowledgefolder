"""
Module 5 — Box Plots: Comparing Spread Across Groups
======================================================
Run standalone:
    streamlit run pages/5_📦_Box_Plots.py
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Box Plots", page_icon="📦", layout="wide")

st.title("📦 Module 5: Box Plots — Comparing Spread Across Groups")

with st.expander("📌 When should you use a box plot?", expanded=True):
    st.markdown(
        """
    Use a **box plot** when you have:
    - A **numeric variable** measured across **multiple groups**
    - And you want to compare not just averages, but **spread, consistency, and outliers**

    Typical finance examples: monthly return distributions across sectors, deal-size
    distributions across years, volatility across fund managers, expense ratios across
    fund categories.

    Box plots are more information-dense than bar charts of averages — they show you
    the **entire spread**, not just one summary number.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_data(seed=9):
    rng = np.random.default_rng(seed)
    sectors = {
        "Tech": (0.015, 0.09),
        "Utilities": (0.004, 0.03),
        "Energy": (0.006, 0.11),
        "Healthcare": (0.008, 0.05),
        "Financials": (0.007, 0.07),
    }
    rows = []
    for sector, (mean, std) in sectors.items():
        rets = rng.normal(mean, std, 90)
        for r in rets:
            rows.append({"Sector": sector, "Monthly Return": r})
    return pd.DataFrame(rows)

if src == "Upload my own CSV":
    up = st.file_uploader("Upload a CSV with a group column and a numeric column", type="csv")
    if up is not None:
        df = pd.read_csv(up)
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_data()
else:
    df = make_sample_data()

cat_cols = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
st.dataframe(df.head(10), use_container_width=True)

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2, c3 = st.columns(3)
with c1:
    group_col = st.selectbox("Group by (x-axis)", cat_cols, index=0 if cat_cols else None)
with c2:
    val_col = st.selectbox("Value (numeric variable)", num_cols, index=0 if num_cols else None)
with c3:
    chart_type = st.radio("Chart style", ["Box plot", "Violin plot"], horizontal=True)

show_points = st.checkbox("Show all individual data points", value=False)

points_mode = "all" if show_points else "outliers"
if chart_type == "Box plot":
    fig = px.box(df, x=group_col, y=val_col, color=group_col, points=points_mode)
else:
    fig = px.violin(df, x=group_col, y=val_col, color=group_col, box=True, points=points_mode)

fig.update_layout(height=520, showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- The **box** spans the interquartile range (IQR) — the middle 50% of observations.
- The **line inside the box** is the median.
- The **whiskers** extend to the most extreme values within 1.5× the IQR.
- **Dots beyond the whiskers** are statistical outliers worth investigating.
- A **taller box** = more spread/inconsistency within that group; a **short box** =
  tightly clustered, consistent values.
- If you switched to a **violin plot**, the width at each point shows the density of
  observations there — it reveals shape (e.g., bimodal distributions) that a box plot alone hides.
"""
)

st.header("💡 Step 4 — Extract the insight")
summary = df.groupby(group_col)[val_col].agg(["median", "std", "count"]).sort_values("median", ascending=False)
st.dataframe(summary, use_container_width=True)

most_consistent = summary["std"].idxmin()
most_volatile = summary["std"].idxmax()
top_median = summary.index[0]

st.success(
    f"**Auto-insight:** **{top_median}** has the highest median value. "
    f"**{most_consistent}** is the most consistent group (lowest spread), while "
    f"**{most_volatile}** is the most volatile/inconsistent group (highest spread)."
)

with st.expander("📝 Practice checklist"):
    st.checkbox("I can identify the median, IQR, and outliers just by looking at a box")
    st.checkbox("I compared spread (not just averages) across groups")
    st.checkbox("I tried the violin plot and can explain when it adds value over a box plot")
    st.checkbox("I flagged at least one outlier group/point and hypothesized why it's unusual")