"""Module 7: ARIMA - Stock Price Time Series Forecasting"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

st.set_page_config(page_title="ARIMA - Stock Forecasting", page_icon="📉", layout="wide")

st.title("📉 Module 7: ARIMA Time Series")
st.subheader("Forecasting a stock price or index level")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    ARIMA(p, d, q) models a series using:
    - **AR(p)**: past values predict future values
    - **I(d)**: differencing d times to make the series stationary
    - **MA(q)**: past forecast errors predict future values

    Prices are usually **non-stationary** (trending), so ARIMA typically
    differences the series once (d=1) — modeling *changes* in price, which
    is close to modeling returns. The **ACF/PACF plots** are the classic
    tool analysts use to pick p and q.
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic price series", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=500, seed=13):
    rng = np.random.default_rng(seed)
    returns = rng.normal(0.0003, 0.014, n)
    # add mild autocorrelation to make ARIMA meaningfully better than naive
    for i in range(1, n):
        returns[i] += 0.15 * returns[i - 1]
    price = 100 * np.exp(np.cumsum(returns))
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n, freq="B")
    return pd.DataFrame({"date": dates, "price": price})


if data_source == "Synthetic price series":
    n_points = st.slider("Number of trading days", 100, 1500, 500, 50)
    df = make_synthetic_data(n_points)
    st.caption("Synthetic daily closing price with mild autocorrelation baked in.")
else:
    uploaded = st.file_uploader("Upload CSV with a date column and a price column", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

date_col = st.selectbox("Date column", df.columns, index=0)
price_col = st.selectbox("Price column", [c for c in df.columns if c != date_col],
                          index=len(df.columns) - 2 if len(df.columns) > 1 else 0)
df = df[[date_col, price_col]].dropna().rename(columns={date_col: "date", price_col: "price"})
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

fig0 = go.Figure(go.Scatter(x=df["date"], y=df["price"], mode="lines", name="Price"))
fig0.update_layout(title="Price history")
st.plotly_chart(fig0, use_container_width=True)

# ------------------------------------------------------------------
# STATIONARITY CHECK
# ------------------------------------------------------------------
st.header("2️⃣ Check stationarity")
adf_result = adfuller(df["price"])
c1, c2 = st.columns(2)
c1.metric("ADF statistic", f"{adf_result[0]:.3f}")
c2.metric("p-value", f"{adf_result[1]:.4f}")
if adf_result[1] > 0.05:
    st.warning("p-value > 0.05 → series is likely non-stationary (as expected for raw prices). "
               "ARIMA will difference it internally using the 'd' parameter below.")
else:
    st.success("p-value ≤ 0.05 → series looks stationary already.")

with st.expander("Show ACF / PACF plots (used to pick p and q)"):
    diff_order = st.radio("Difference the series before plotting?", [0, 1], index=1, horizontal=True)
    series_to_plot = df["price"].diff(diff_order).dropna() if diff_order else df["price"]
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    plot_acf(series_to_plot, ax=ax1, lags=30)
    plot_pacf(series_to_plot, ax=ax2, lags=30)
    st.pyplot(fig1)

# ------------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------------
st.header("3️⃣ Train the model")
c1, c2, c3, c4 = st.columns(4)
p = c1.slider("p (AR order)", 0, 5, 1)
d = c2.slider("d (differencing)", 0, 2, 1)
q = c3.slider("q (MA order)", 0, 5, 1)
forecast_horizon = c4.slider("Forecast horizon (days)", 5, 60, 20)

train_size = int(len(df) * 0.9)
train, test = df["price"][:train_size], df["price"][train_size:]

with st.spinner("Fitting ARIMA..."):
    model = ARIMA(train, order=(p, d, q))
    fitted = model.fit()

forecast_res = fitted.get_forecast(steps=len(test) + forecast_horizon)
forecast_mean = forecast_res.predicted_mean
conf_int = forecast_res.conf_int(alpha=0.1)

# backtest error on the held-out test portion
backtest_pred = forecast_mean[: len(test)]
rmse = np.sqrt(np.mean((test.values - backtest_pred.values) ** 2))
mape = np.mean(np.abs((test.values - backtest_pred.values) / test.values)) * 100

col1, col2, col3 = st.columns(3)
col1.metric("AIC", f"{fitted.aic:.1f}")
col2.metric("Backtest RMSE", f"{rmse:.2f}")
col3.metric("Backtest MAPE", f"{mape:.2f}%")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("4️⃣ See it work")
all_dates = list(df["date"]) + list(
    pd.bdate_range(start=df["date"].iloc[-1] + pd.Timedelta(days=1), periods=forecast_horizon)
)
forecast_dates = all_dates[train_size:]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df["date"][:train_size], y=train, mode="lines", name="Train"))
fig2.add_trace(go.Scatter(x=df["date"][train_size:], y=test, mode="lines", name="Actual (held out)"))
fig2.add_trace(go.Scatter(x=forecast_dates, y=forecast_mean, mode="lines", name="Forecast", line=dict(dash="dash")))
fig2.add_trace(go.Scatter(
    x=list(forecast_dates) + list(forecast_dates)[::-1],
    y=list(conf_int.iloc[:, 1]) + list(conf_int.iloc[:, 0])[::-1],
    fill="toself", fillcolor="rgba(99,110,250,0.15)", line=dict(width=0), name="90% CI", showlegend=True,
))
fig2.update_layout(title=f"ARIMA({p},{d},{q}) forecast")
st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
st.markdown(
    f"""
- Backtest MAPE of **{mape:.1f}%** tells you the model's typical forecast error over the held-out period —
  compare it against simply predicting "tomorrow = today" (a naive baseline) to see if ARIMA earns its complexity.
- **AIC = {fitted.aic:.1f}** is only meaningful *relative to other (p,d,q) combinations* — try a few
  settings above and keep the one with the lowest AIC that still backtests well.
- The widening confidence interval further into the future is the honest signal: ARIMA forecasts
  decay in reliability quickly — good for short-horizon tactical calls, weak for long-run price targets.
"""
)
