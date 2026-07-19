import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Module 5 — Predictive Forecasting", page_icon="📈", layout="wide")

st.title("📈 Module 5: Predictive Analytics — Forecasting")
st.caption("Learning goal: answer 'what will happen?' using moving average, exponential smoothing, and regression.")

st.markdown(
    "Generate a synthetic monthly revenue history using the controls below, then compare three "
    "classic forecasting techniques side by side."
)

st.divider()
st.markdown("## 🎛️ Generate Historical Data")

c1, c2, c3, c4 = st.columns(4)
base = c1.slider("Starting monthly revenue ($'000)", 50, 500, 200, step=10)
growth = c2.slider("Monthly growth rate (%)", -5.0, 10.0, 1.5, step=0.1)
seasonality = c3.slider("Seasonality strength", 0, 50, 15, step=5)
noise_level = c4.slider("Random noise level", 0, 50, 10, step=5)

n_hist = 24
n_forecast = st.slider("Months to forecast ahead", 1, 12, 6)

months = np.arange(n_hist)
trend = base * (1 + growth / 100) ** months
season = seasonality * np.sin(2 * np.pi * months / 12)
np.random.seed(1)
noise = np.random.normal(0, noise_level, n_hist)
history = trend + season + noise
history = np.clip(history, 1, None)

hist_dates = pd.date_range("2024-01-01", periods=n_hist, freq="MS")
hist_df = pd.DataFrame({"Date": hist_dates, "Revenue": history})

st.markdown("## 🔧 Forecasting Method Settings")
m1, m2 = st.columns(2)
ma_window = m1.slider("Moving Average window (months)", 2, 12, 3)
alpha = m2.slider("Exponential Smoothing alpha (0 = smooth, 1 = reactive)", 0.05, 0.95, 0.3, step=0.05)

# --- Moving Average forecast ---
ma_last = hist_df["Revenue"].rolling(ma_window).mean().iloc[-1]
ma_forecast = np.full(n_forecast, ma_last)

# --- Exponential Smoothing (simple) ---
es_level = history[0]
es_fitted = [es_level]
for v in history[1:]:
    es_level = alpha * v + (1 - alpha) * es_level
    es_fitted.append(es_level)
es_forecast = np.full(n_forecast, es_level)

# --- Linear Regression trend forecast ---
coeffs = np.polyfit(months, history, 1)
future_months = np.arange(n_hist, n_hist + n_forecast)
lr_forecast = np.polyval(coeffs, future_months)
lr_fitted = np.polyval(coeffs, months)

future_dates = pd.date_range(hist_dates[-1] + pd.DateOffset(months=1), periods=n_forecast, freq="MS")

# --- plot ---
fig = go.Figure()
fig.add_trace(go.Scatter(x=hist_dates, y=history, mode="lines+markers", name="Actual History",
                          line=dict(color="#444", width=2)))
fig.add_trace(go.Scatter(x=hist_dates, y=lr_fitted, mode="lines", name="Regression Trend (fitted)",
                          line=dict(color="#5B8FF9", dash="dot")))
fig.add_trace(go.Scatter(x=future_dates, y=ma_forecast, mode="lines+markers", name=f"Moving Avg (n={ma_window}) Forecast",
                          line=dict(color="#5AD8A6", width=3)))
fig.add_trace(go.Scatter(x=future_dates, y=es_forecast, mode="lines+markers", name=f"Exp. Smoothing (α={alpha}) Forecast",
                          line=dict(color="#E8684A", width=3)))
fig.add_trace(go.Scatter(x=future_dates, y=lr_forecast, mode="lines+markers", name="Linear Regression Forecast",
                          line=dict(color="#5B8FF9", width=3)))
fig.update_layout(title="Revenue History & Forecasts", height=480, legend=dict(orientation="h", y=-0.25))
st.plotly_chart(fig, use_container_width=True)

st.divider()

# ----------------------------------------------------------------------------
# ACCURACY COMPARISON (in-sample, via one-step-ahead backtesting)
# ----------------------------------------------------------------------------
st.markdown("## 📏 Comparing Forecast Accuracy (in-sample backtest)")

ma_fitted = hist_df["Revenue"].rolling(ma_window).mean().shift(1)
es_fitted_arr = pd.Series(es_fitted).shift(1)
lr_fitted_shift = pd.Series(lr_fitted)  # regression uses all data, not shifted

def mape(actual, pred):
    mask = ~pred.isna() if isinstance(pred, pd.Series) else ~np.isnan(pred)
    a = np.array(actual)[mask]
    p = np.array(pred)[mask]
    return np.mean(np.abs((a - p) / a)) * 100

acc_df = pd.DataFrame({
    "Method": ["Moving Average", "Exponential Smoothing", "Linear Regression"],
    "MAPE (%)": [
        mape(history, ma_fitted),
        mape(history, es_fitted_arr),
        mape(history, lr_fitted_shift),
    ],
})
st.dataframe(acc_df.style.format({"MAPE (%)": "{:.2f}"}), use_container_width=True, hide_index=True)

best = acc_df.loc[acc_df["MAPE (%)"].idxmin(), "Method"]
st.success(f"Lowest error (best in-sample fit) for this dataset: **{best}**. "
           "Note: the 'best' method depends on your data's shape — try increasing seasonality "
           "or noise above and see which method holds up best.")

st.markdown(
    """
**Rules of thumb:**
- **Moving average** — good for stable, low-trend, low-seasonality data.
- **Exponential smoothing** — reacts faster to recent changes; tune alpha up for volatile data.
- **Linear regression** — best when there's a clear, consistent trend; poor with strong seasonality (without adjustment).
"""
)

st.divider()
st.info("➡️ Next: **Module 6 — Risk & Monte Carlo Simulation**, to quantify uncertainty in your projections.")
