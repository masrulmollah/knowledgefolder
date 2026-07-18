"""
Module 1 — Line Charts: Time Series & Trend Analysis
======================================================
Standalone-runnable Streamlit page. Also auto-registers in the sidebar
when placed inside a `pages/` folder next to a root app.py.

Run standalone:
    streamlit run pages/1_📈_Line_Charts.py
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Line Charts", page_icon="📈", layout="wide")

st.title("📈 Module 1: Line Charts — Time Series & Trend Analysis")

# ----------------------------------------------------------------------
# THEORY
# ----------------------------------------------------------------------
with st.expander("📌 When should you use a line chart?", expanded=True):
    st.markdown(
        """
    Use a **line chart** when you have:
    - A **continuous numeric variable** (price, index level, rate, revenue)
    - Measured **repeatedly over time** (daily, monthly, quarterly)
    - And you care about **trend, momentum, or comparing trajectories** of 2+ series

    Typical finance examples: stock price history, portfolio NAV over time,
    benchmark comparison (your fund vs. S&P 500), interest rate curves over time.

    **Avoid** a line chart when there's no natural time/sequence ordering on the x-axis —
    use a bar chart for categorical comparisons instead.
    """
    )

st.divider()

# ----------------------------------------------------------------------
# DATA SOURCE
# ----------------------------------------------------------------------
st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_data(days=500, seed=7):
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end=pd.Timestamp.today(), periods=days)
    assets = {}
    for name, drift, vol, start in [
        ("Your Portfolio", 0.0006, 0.012, 100),
        ("S&P 500 (Benchmark)", 0.0004, 0.010, 100),
        ("Bond Index", 0.0002, 0.004, 100),
    ]:
        rets = rng.normal(drift, vol, size=days)
        prices = start * np.cumprod(1 + rets)
        assets[name] = prices
    df = pd.DataFrame(assets, index=dates)
    df.index.name = "Date"
    return df.reset_index()

if src == "Upload my own CSV":
    up = st.file_uploader(
        "Upload a CSV with a date column and one or more numeric series columns",
        type="csv",
    )
    if up is not None:
        df = pd.read_csv(up)
        date_col = st.selectbox("Which column is the date?", df.columns)
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df = df.rename(columns={date_col: "Date"}).sort_values("Date")
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_data()
else:
    df = make_sample_data()

numeric_cols = [c for c in df.columns if c != "Date" and pd.api.types.is_numeric_dtype(df[c])]

st.dataframe(df.head(), use_container_width=True)

# ----------------------------------------------------------------------
# CONTROLS
# ----------------------------------------------------------------------
st.header("🎛️ Step 2 — Build & edit the chart live")

c1, c2, c3 = st.columns(3)
with c1:
    series = st.multiselect("Series to plot", numeric_cols, default=numeric_cols[: min(3, len(numeric_cols))])
with c2:
    rebase = st.checkbox("Rebase all series to 100 at start (compare relative performance)", value=True)
with c3:
    log_scale = st.checkbox("Log scale y-axis", value=False)

c4, c5 = st.columns(2)
with c4:
    show_ma = st.checkbox("Overlay moving average", value=False)
with c5:
    ma_window = st.slider("Moving average window (periods)", 5, 100, 20, disabled=not show_ma)

if not series:
    st.warning("Select at least one series to plot.")
    st.stop()

plot_df = df[["Date"] + series].dropna().copy()
if rebase:
    for s in series:
        plot_df[s] = plot_df[s] / plot_df[s].iloc[0] * 100

fig = go.Figure()
for s in series:
    fig.add_trace(go.Scatter(x=plot_df["Date"], y=plot_df[s], mode="lines", name=s))
    if show_ma:
        ma = plot_df[s].rolling(ma_window).mean()
        fig.add_trace(
            go.Scatter(
                x=plot_df["Date"], y=ma, mode="lines", name=f"{s} — {ma_window}p MA",
                line=dict(dash="dash", width=1),
            )
        )

fig.update_layout(
    yaxis_type="log" if log_scale else "linear",
    yaxis_title="Rebased to 100" if rebase else "Value",
    xaxis_title="Date",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02),
    height=500,
)
st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------------------
# HOW TO READ
# ----------------------------------------------------------------------
st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- **Slope** tells you the rate of change — steeper = faster growth/decline.
- **Crossovers** between two lines mark a change in relative leadership (e.g., your
  portfolio overtaking the benchmark).
- **A widening gap** between series = increasing outperformance/underperformance.
- **"Noisiness" of the line** is a rough visual proxy for volatility — jagged lines are riskier.
- If you turned on the **moving average**, the dashed line smooths out day-to-day noise so
  you can see the underlying trend; price crossing above/below its MA is a classic trend signal.
"""
)

# ----------------------------------------------------------------------
# INSIGHT EXERCISE
# ----------------------------------------------------------------------
st.header("💡 Step 4 — Extract the insight")
if len(series) >= 1:
    total_return = (plot_df[series].iloc[-1] / plot_df[series].iloc[0] - 1) * 100
    best = total_return.idxmax()
    worst = total_return.idxmin()
    cols = st.columns(len(series))
    for i, s in enumerate(series):
        cols[i].metric(f"{s} total return", f"{total_return[s]:.1f}%")
    st.success(
        f"**Auto-insight:** Over this period, **{best}** delivered the strongest "
        f"return ({total_return[best]:.1f}%), while **{worst}** lagged "
        f"({total_return[worst]:.1f}%)."
    )

with st.expander("📝 Practice checklist"):
    st.checkbox("I can identify which series outperformed just by looking at the chart")
    st.checkbox("I can explain what a crossover between two lines means")
    st.checkbox("I tried rebasing and understand why it enables fair comparison")
    st.checkbox("I tried adding a moving average and can explain what it smooths out")
    st.checkbox("I uploaded my own dataset and reproduced this analysis")