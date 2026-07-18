"""
Module 7 — Candlestick & OHLC Charts: Price Action
====================================================
Run standalone:
    streamlit run pages/7_🕯️_Candlestick_Charts.py
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

st.set_page_config(page_title="Candlestick Charts", page_icon="🕯️", layout="wide")

st.title("🕯️ Module 7: Candlestick & OHLC Charts — Price Action")

with st.expander("📌 When should you use a candlestick chart?", expanded=True):
    st.markdown(
        """
    Use a **candlestick / OHLC chart** when you have **Open, High, Low, Close (OHLC)**
    price data for each period (daily, hourly, etc.) — not just closing prices.

    Typical finance examples: equity/FX/commodity price action for trading and technical
    analysis, understanding intraday volatility, spotting reversal/continuation patterns.

    This is the standard chart used by traders — a line chart of closes alone throws away
    the open/high/low information a candlestick preserves.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_ohlc(days=180, seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end=pd.Timestamp.today(), periods=days)
    close = 150.0
    rows = []
    for d in dates:
        o = close * (1 + rng.normal(0, 0.003))
        move = rng.normal(0.0003, 0.015)
        c = o * (1 + move)
        h = max(o, c) * (1 + abs(rng.normal(0, 0.006)))
        l = min(o, c) * (1 - abs(rng.normal(0, 0.006)))
        vol = rng.integers(1_000_000, 8_000_000)
        rows.append({"Date": d, "Open": o, "High": h, "Low": l, "Close": c, "Volume": vol})
        close = c
    return pd.DataFrame(rows)

if src == "Upload my own CSV":
    up = st.file_uploader("Upload a CSV with Date, Open, High, Low, Close (and optionally Volume) columns", type="csv")
    if up is not None:
        df = pd.read_csv(up)
        date_col = st.selectbox("Which column is the date?", df.columns)
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df = df.rename(columns={date_col: "Date"}).sort_values("Date")
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_ohlc()
else:
    df = make_sample_ohlc()

required = {"Open", "High", "Low", "Close"}
if not required.issubset(df.columns):
    st.error(f"Your data must contain columns: {required}. Found: {list(df.columns)}")
    st.stop()

st.dataframe(df.head(), use_container_width=True)

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2, c3 = st.columns(3)
with c1:
    n_periods = st.slider("Show last N periods", 20, len(df), min(90, len(df)))
with c2:
    show_ma1 = st.checkbox("Show 20-period MA", value=True)
with c3:
    show_ma2 = st.checkbox("Show 50-period MA", value=True)
show_volume = st.checkbox("Show volume panel", value="Volume" in df.columns, disabled="Volume" not in df.columns)

plot_df = df.tail(n_periods).copy()

rows = 2 if (show_volume and "Volume" in plot_df.columns) else 1
fig = make_subplots(
    rows=rows, cols=1, shared_xaxes=True, vertical_spacing=0.03,
    row_heights=[0.75, 0.25] if rows == 2 else [1],
)

fig.add_trace(
    go.Candlestick(
        x=plot_df["Date"], open=plot_df["Open"], high=plot_df["High"],
        low=plot_df["Low"], close=plot_df["Close"], name="Price",
    ),
    row=1, col=1,
)

if show_ma1:
    fig.add_trace(go.Scatter(x=plot_df["Date"], y=plot_df["Close"].rolling(20).mean(), name="20-period MA", line=dict(width=1.5)), row=1, col=1)
if show_ma2:
    fig.add_trace(go.Scatter(x=plot_df["Date"], y=plot_df["Close"].rolling(50).mean(), name="50-period MA", line=dict(width=1.5)), row=1, col=1)

if rows == 2:
    colors = np.where(plot_df["Close"] >= plot_df["Open"], "green", "red")
    fig.add_trace(go.Bar(x=plot_df["Date"], y=plot_df["Volume"], marker_color=colors, name="Volume"), row=2, col=1)

fig.update_layout(height=650, xaxis_rangeslider_visible=False, legend=dict(orientation="h", yanchor="bottom", y=1.02))
st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- Each **candle** covers one period. The **body** spans open-to-close: **green/hollow**
  = closed higher than it opened (bullish); **red/filled** = closed lower (bearish) —
  exact colors depend on your chart theme.
- The **wicks (thin lines)** above/below the body show the period's high and low —
  long wicks mean lots of intraday volatility that didn't stick.
- **Moving averages** smooth the noise; price crossing above/below its MA, or a shorter
  MA crossing a longer MA ("golden cross" / "death cross"), are classic trend signals.
- **Volume bars** below confirm conviction — a big price move on high volume is more
  meaningful than the same move on low volume.
"""
)

st.header("💡 Step 4 — Extract the insight")
last = plot_df.iloc[-1]
period_return = (plot_df["Close"].iloc[-1] / plot_df["Close"].iloc[0] - 1) * 100
avg_range_pct = ((plot_df["High"] - plot_df["Low"]) / plot_df["Close"]).mean() * 100
up_days = (plot_df["Close"] >= plot_df["Open"]).sum()
down_days = len(plot_df) - up_days

c1, c2, c3 = st.columns(3)
c1.metric("Return over window", f"{period_return:.1f}%")
c2.metric("Avg daily range", f"{avg_range_pct:.2f}%")
c3.metric("Up days vs down days", f"{up_days} / {down_days}")

st.success(
    f"**Auto-insight:** Over the last {n_periods} periods, price moved **{period_return:.1f}%**, "
    f"with an average intraday range of **{avg_range_pct:.2f}%** — "
    + ("a relatively volatile window." if avg_range_pct > 2 else "a relatively calm window.")
)

with st.expander("📝 Practice checklist"):
    st.checkbox("I can identify a bullish vs. bearish candle by its body color")
    st.checkbox("I can explain what a long upper/lower wick suggests about intraday trading")
    st.checkbox("I can spot a moving-average crossover and explain what it signals")
    st.checkbox("I connected a volume spike to a corresponding price move")