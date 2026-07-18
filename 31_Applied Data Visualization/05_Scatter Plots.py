"""
Module 4 — Scatter Plots: Relationships & Correlation
=======================================================
Run standalone:
    streamlit run pages/4_🔵_Scatter_Plots.py
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Scatter Plots", page_icon="🔵", layout="wide")

st.title("🔵 Module 4: Scatter Plots — Relationships & Correlation")

with st.expander("📌 When should you use a scatter plot?", expanded=True):
    st.markdown(
        """
    Use a **scatter plot** when you have:
    - **Two continuous numeric variables** measured for the same set of entities
    - And you want to see whether they **move together** (correlate), and how strongly

    Typical finance examples: risk (volatility) vs. return by asset, P/E ratio vs.
    earnings growth by stock, beta vs. alpha, deal size vs. time-to-close.

    Add a **third variable** via bubble size or color (e.g., market cap, sector) to
    pack more information into one chart.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_data(n=40, seed=5):
    rng = np.random.default_rng(seed)
    sectors = rng.choice(["Tech", "Financials", "Healthcare", "Energy", "Consumer"], n)
    risk = rng.uniform(8, 45, n)
    ret = 2 + risk * 0.6 + rng.normal(0, 6, n)
    market_cap = rng.uniform(2, 800, n)
    return pd.DataFrame({
        "Ticker": [f"TICK{i:03d}" for i in range(n)],
        "Sector": sectors,
        "Annualized Volatility (%)": risk,
        "Annualized Return (%)": ret,
        "Market Cap ($B)": market_cap,
    })

if src == "Upload my own CSV":
    up = st.file_uploader("Upload a CSV with at least two numeric columns", type="csv")
    if up is not None:
        df = pd.read_csv(up)
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_data()
else:
    df = make_sample_data()

num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
cat_cols = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
st.dataframe(df.head(10), use_container_width=True)

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2 = st.columns(2)
with c1:
    x_col = st.selectbox("X-axis", num_cols, index=0)
with c2:
    y_col = st.selectbox("Y-axis", num_cols, index=min(1, len(num_cols) - 1))

c3, c4, c5 = st.columns(3)
with c3:
    color_col = st.selectbox("Color by (optional)", ["(none)"] + cat_cols + num_cols)
with c4:
    size_col = st.selectbox("Bubble size by (optional)", ["(none)"] + num_cols)
with c5:
    trendline = st.checkbox("Show trendline (linear regression)", value=True)

color = None if color_col == "(none)" else color_col
size = None if size_col == "(none)" else size_col

fig = px.scatter(
    df, x=x_col, y=y_col, color=color, size=size,
    hover_data=df.columns, trendline="ols" if trendline else None,
)
fig.update_layout(height=550)
st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- Each **dot** = one entity (a stock, a deal, a fund).
- **Position** encodes its value on the x and y variables simultaneously.
- A **tight, upward-sloping cloud** = strong positive correlation; a tight downward
  slope = strong negative correlation; a shapeless cloud = little to no correlation.
- **Bubble size / color** adds a third dimension without needing a 3D chart.
- **Outliers** (points far from the main cloud) are worth investigating individually —
  they may be mispriced, mislabeled, or genuinely unusual.
- The **trendline** (if shown) is the best-fit linear relationship — points far above it
  are "outperforming" the relationship; points far below are "underperforming" it.
"""
)

st.header("💡 Step 4 — Extract the insight")
corr = df[[x_col, y_col]].corr().iloc[0, 1]
strength = (
    "strong" if abs(corr) > 0.7 else "moderate" if abs(corr) > 0.4 else "weak"
)
direction = "positive" if corr > 0 else "negative"
st.metric("Correlation coefficient", f"{corr:.2f}")
st.success(
    f"**Auto-insight:** `{x_col}` and `{y_col}` show a **{strength} {direction}** "
    f"relationship (r = {corr:.2f}). "
    + ("As one rises, the other tends to rise too." if corr > 0 else "As one rises, the other tends to fall.")
)

with st.expander("📝 Practice checklist"):
    st.checkbox("I can estimate the correlation strength just from the shape of the cloud")
    st.checkbox("I identified at least one outlier and can explain why it stands out")
    st.checkbox("I used color/size to add a third variable to the chart")
    st.checkbox("I can explain the difference between correlation and causation using this chart")