"""
Module 6 — Heatmaps & Correlation Matrices
============================================
Run standalone:
    streamlit run pages/6_🔥_Heatmaps.py
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Heatmaps", page_icon="🔥", layout="wide")

st.title("🔥 Module 6: Heatmaps & Correlation Matrices")

with st.expander("📌 When should you use a heatmap?", expanded=True):
    st.markdown(
        """
    Use a **heatmap** when you have:
    - A **grid/matrix of values** — either naturally (e.g., month × year performance)
      or derived (e.g., a correlation matrix between many assets)
    - And scanning a table of numbers would be slow, but colors would pop out patterns instantly

    Typical finance examples: asset correlation matrices for portfolio construction,
    monthly return "seasonality" tables, sector performance grids across time.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio(
    "Choose a data source",
    ["Use sample data (asset price correlation)", "Upload my own CSV (wide numeric table)"],
    horizontal=True,
)

@st.cache_data
def make_sample_prices(seed=21):
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end=pd.Timestamp.today(), periods=400)
    tickers = ["AAPL", "MSFT", "GOOG", "XOM", "CVX", "JPM", "GS", "PG", "KO"]
    factor = rng.normal(0, 0.01, len(dates))
    data = {}
    for t in tickers:
        beta = rng.uniform(0.4, 1.3)
        idio = rng.normal(0.0003, 0.008, len(dates))
        rets = beta * factor + idio
        data[t] = 100 * np.cumprod(1 + rets)
    return pd.DataFrame(data, index=dates)

if src.startswith("Upload"):
    up = st.file_uploader("Upload a wide CSV (columns = assets/categories, rows = observations)", type="csv")
    if up is not None:
        raw = pd.read_csv(up)
        raw = raw.select_dtypes(include=[np.number])
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        raw = make_sample_prices()
else:
    raw = make_sample_prices()

st.dataframe(raw.head(), use_container_width=True)

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2, c3 = st.columns(3)
with c1:
    metric = st.selectbox("Correlation method", ["pearson", "spearman", "kendall"])
with c2:
    use_returns = st.checkbox("Convert levels to % change first (recommended for prices)", value=True)
with c3:
    color_scale = st.selectbox("Color scale", ["RdBu", "Viridis", "RdYlGn", "Blues"])

selected_cols = st.multiselect("Columns to include", list(raw.columns), default=list(raw.columns))
work = raw[selected_cols].copy()
if use_returns:
    work = work.pct_change().dropna()

corr = work.corr(method=metric)

fig = px.imshow(
    corr, text_auto=".2f", color_continuous_scale=color_scale, zmin=-1, zmax=1,
    aspect="auto",
)
fig.update_layout(height=550)
st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- Each **cell** shows the correlation between the row asset and the column asset,
  ranging from **-1 (perfect inverse)** to **+1 (perfectly move together)**.
- The **diagonal** is always 1.0 — every asset perfectly correlates with itself.
- The matrix is **symmetric** — the upper and lower triangles mirror each other.
- **Dark red/blue extremes** (depending on your color scale) flag pairs that move
  strongly together or strongly opposite — for a colorblind-safe read, always check
  the numeric labels too, not just color.
- **Near-zero (pale) cells** indicate little relationship — useful for diversification.
"""
)

st.header("💡 Step 4 — Extract the insight")
corr_no_diag = corr.copy()
np.fill_diagonal(corr_no_diag.values, np.nan)
stacked = corr_no_diag.stack()
if not stacked.empty:
    most_corr_pair = stacked.idxmax()
    least_corr_pair = stacked.idxmin()
    st.success(
        f"**Auto-insight:** **{most_corr_pair[0]}** and **{most_corr_pair[1]}** are the "
        f"most correlated pair (r = {stacked[most_corr_pair]:.2f}) — holding both adds little "
        f"diversification. **{least_corr_pair[0]}** and **{least_corr_pair[1]}** are the least "
        f"correlated pair (r = {stacked[least_corr_pair]:.2f}) — a better diversification combo."
    )

with st.expander("📝 Practice checklist"):
    st.checkbox("I can read any cell's correlation value directly off the heatmap")
    st.checkbox("I understand why the matrix is symmetric and the diagonal is always 1.0")
    st.checkbox("I identified a highly correlated pair (concentration risk) and a low-correlation pair (diversifier)")
    st.checkbox("I toggled 'convert to % change' and understand why raw price-level correlation can be misleading")