"""
Module 3 — Histograms & Distribution Plots: Understanding Spread and Risk
==========================================================================
Run standalone:
    streamlit run pages/3_📉_Histograms.py
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats
import streamlit as st

st.set_page_config(page_title="Histograms & Distributions", page_icon="📉", layout="wide")

st.title("📉 Module 3: Histograms & Distribution Plots — Spread and Risk")

with st.expander("📌 When should you use a histogram / distribution plot?", expanded=True):
    st.markdown(
        """
    Use a **histogram** when you have:
    - A **single numeric variable** (daily returns, P&L outcomes, deal sizes, credit scores)
    - And you want to see its **shape**: is it symmetric, skewed, fat-tailed, bimodal?

    Typical finance examples: distribution of daily stock returns, portfolio P&L outcomes
    from a Monte Carlo simulation, distribution of loan default probabilities.

    This is the foundation of **risk analysis** — most risk metrics (VaR, volatility,
    skewness, kurtosis) are just numbers that describe this shape.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_data(n=1000, seed=11):
    rng = np.random.default_rng(seed)
    normal_rets = rng.normal(0.0005, 0.012, n)
    fat_tail_rets = stats.t.rvs(df=3, size=n, random_state=seed) * 0.010 + 0.0003
    return pd.DataFrame({
        "Blue-Chip Stock Daily Return": normal_rets,
        "Emerging-Market Stock Daily Return": fat_tail_rets,
    })

if src == "Upload my own CSV":
    up = st.file_uploader("Upload a CSV with one or more numeric columns (e.g., returns)", type="csv")
    if up is not None:
        df = pd.read_csv(up)
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_data()
else:
    df = make_sample_data()

num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
st.dataframe(df.head(), use_container_width=True)

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2, c3 = st.columns(3)
with c1:
    col = st.selectbox("Variable to analyze", num_cols)
with c2:
    bins = st.slider("Number of bins", 10, 150, 50)
with c3:
    show_normal = st.checkbox("Overlay a normal distribution curve", value=True)

show_stats_lines = st.checkbox("Show mean & median lines", value=True)

series = df[col].dropna()

fig = go.Figure()
fig.add_trace(go.Histogram(x=series, nbinsx=bins, histnorm="probability density", name=col, opacity=0.75))

if show_normal:
    x = np.linspace(series.min(), series.max(), 200)
    y = stats.norm.pdf(x, series.mean(), series.std())
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Normal curve (same mean/std)", line=dict(color="red")))

if show_stats_lines:
    fig.add_vline(x=series.mean(), line_dash="dash", line_color="green", annotation_text="mean")
    fig.add_vline(x=series.median(), line_dash="dot", line_color="orange", annotation_text="median")

fig.update_layout(height=500, xaxis_title=col, yaxis_title="Density", bargap=0.02)
st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- **Bar height** = how often values in that range occur (probability density).
- **Symmetric, bell-shaped** = roughly normal — most values cluster near the mean.
- **Skew**: a long tail stretching right = positive skew (occasional big gains);
  a long tail stretching left = negative skew (occasional big losses) — the latter is
  a key risk warning sign.
- **Fat tails** (more extreme values than a normal curve predicts) mean the "normal curve"
  overlay under-predicts how often extreme moves actually happen — a classic finance risk issue.
- **Mean vs. median gap**: if they diverge, the distribution is skewed by outliers.
"""
)

st.header("💡 Step 4 — Extract the insight")
mean_v, std_v = series.mean(), series.std()
skew_v = series.skew()
kurt_v = series.kurt()
var95 = np.percentile(series, 5)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Mean", f"{mean_v:.4f}")
c2.metric("Std Dev (volatility)", f"{std_v:.4f}")
c3.metric("Skewness", f"{skew_v:.2f}")
c4.metric("5% VaR (historical)", f"{var95:.4f}")

skew_note = "right-skewed (upside surprises more extreme)" if skew_v > 0.2 else (
    "left-skewed (downside surprises more extreme — watch for tail risk)" if skew_v < -0.2 else "roughly symmetric"
)
tail_note = "fatter than normal (excess kurtosis) — extreme moves are more common than a normal model would predict" if kurt_v > 1 else "close to normal tail thickness"

st.success(
    f"**Auto-insight:** `{col}` is **{skew_note}**, with tails that are **{tail_note}**. "
    f"There is a 5% historical chance of a return worse than **{var95:.4f}** on any given period."
)

with st.expander("📝 Practice checklist"):
    st.checkbox("I can explain what skewness tells me about risk")
    st.checkbox("I can explain why fat tails matter even when volatility looks normal")
    st.checkbox("I understand what 'VaR' (Value at Risk) shown above represents")
    st.checkbox("I compared two variables and identified which has the riskier distribution")