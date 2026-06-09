import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

def _sec(title, icon=""):
    st.markdown(f"### {icon} {title}")
    st.markdown("---")

def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans: st.success("✅ Correct!")
        else: st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def _exp_smoothing(series, alpha):
    smoothed = [series[0]]
    for i in range(1, len(series)):
        smoothed.append(alpha * series[i] + (1 - alpha) * smoothed[-1])
    return smoothed

def show():
    st.title("📈 Module 5: Predictive & Forecasting Analytics")
    st.caption("Use historical patterns to answer: What is likely to happen next?")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Forecast Engine", "📊 Regression Forecaster", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Forecasting Methods Overview", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Time-Series Forecasting Hierarchy**
| Method | Complexity | Best For |
|--------|-----------|----------|
| Naïve (last period) | Very Low | Highly stable KPIs |
| Moving Average (SMA) | Low | Removing short-term noise |
| Weighted Moving Average | Low | Giving more weight to recent data |
| Exponential Smoothing (SES) | Medium | Smooth short-term trends |
| Holt's Double Smoothing | Medium | Data with a trend, no seasonality |
| Holt-Winters (Triple) | Medium-High | Data with trend + seasonality |
| ARIMA | High | Complex time-series with autocorrelation |

**Seasonal Index:**
```
Seasonal Index (Month M) = Avg(Month M) / Overall Avg × 100
```
Adjust any forecast by the seasonal index to remove seasonal distortion.
Index > 100 = above-average month. Index < 100 = below-average.

**CAGR-based Forecast:**
```
Forecast Year N = Base Year × (1 + CAGR)^N
```
Simple but powerful for long-range strategic planning.
            """)
        with c2:
            st.markdown("""
**Exponential Smoothing (SES) — Alpha Control:**
```
Forecast(t+1) = α × Actual(t) + (1−α) × Forecast(t)
```
- α close to 1 → forecast reacts quickly (good for volatile data)
- α close to 0 → forecast is slow and stable (good for stable data)
- Typical range: α = 0.1 to 0.4

**Time-Series Decomposition:**
```
Observed = Trend + Seasonality + Cyclicality + Random Noise
```
Decompose first, then model each component separately.

**Forecast Accuracy Metrics:**
| Metric | Formula | Interpretation |
|--------|---------|---------------|
| MAE | Mean(|Actual − Forecast|) | Average absolute error in original units |
| MAPE | Mean(|Actual − Forecast|/Actual) × 100 | % error — most widely used in FP&A |
| RMSE | √Mean((Actual − Forecast)²) | Penalises large errors more heavily |

**Target MAPE benchmarks:**
- < 5% = Excellent
- 5–10% = Good
- 10–20% = Acceptable
- > 20% = Poor — review method or data
            """)

        _sec("Scenario & Risk Analytics", "⚠️")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Sensitivity Analysis (One-Variable What-If):**
Change one input at a time and record the impact on the output KPI.
Example: What happens to EBITDA if raw material cost increases by 5%?

**Scenario Planning (Multi-Variable):**
| Scenario | Revenue Growth | RM Cost Change | FX Change | EBITDA Impact |
|----------|---------------|----------------|-----------|---------------|
| Best Case | +12% | −3% | Favourable | +$25M |
| Base Case | +7% | +2% | Neutral | +$8M |
| Worst Case | +1% | +8% | Adverse | −$18M |

Scenario planning tests financial resilience — not just the most likely outcome.
            """)
        with c2:
            st.markdown("""
**Tornado Chart:**
Ranks variables by their impact on the target metric (largest impact at top).
Tells you which assumptions matter most — where to focus risk management.

**Monte Carlo Simulation:**
1. Assign probability distributions to key input variables
2. Run 10,000+ random iterations, sampling from each distribution
3. Build a distribution of possible outcomes
4. Read: probability of achieving target, 5th/95th percentile range

```
Key output metrics:
- P50 (median expected outcome)
- P10/P90 (downside / upside with 80% confidence interval)
- Probability of meeting budget target
```
            """)

    # ── FORECAST ENGINE ───────────────────────────────────────────────────────
    with tab2:
        _sec("Time-Series Forecast Engine", "🧮")
        c1, c2 = st.columns(2)
        with c1:
            periods_hist = st.slider("Historical periods (months)", 24, 60, 36)
            forecast_periods = st.slider("Forecast horizon (months)", 3, 18, 6)
        with c2:
            method = st.selectbox("Forecasting method:",
                                  ["Simple Moving Average (3M)", "Simple Moving Average (6M)",
                                   "Exponential Smoothing", "Linear Trend Projection",
                                   "Year-Ago + CAGR Growth"])
            alpha = 0.3
            if method == "Exponential Smoothing":
                alpha = st.slider("Alpha (smoothing factor)", 0.05, 0.95, 0.25, 0.05)

        np.random.seed(42)
        dates_hist = pd.date_range("2022-01-01", periods=periods_hist, freq="MS")
        trend_c    = 400 + np.arange(periods_hist) * 2.8
        seas_c     = 35 * np.sin(2 * np.pi * np.arange(periods_hist) / 12 - np.pi / 2)
        noise_c    = np.random.normal(0, 10, periods_hist)
        actuals    = (trend_c + seas_c + noise_c).tolist()

        if method == "Simple Moving Average (3M)":
            w = 3
            fitted = [None]*w + [np.mean(actuals[i-w:i]) for i in range(w, len(actuals))]
            last_avg = np.mean(actuals[-w:])
            forecast = [last_avg] * forecast_periods
        elif method == "Simple Moving Average (6M)":
            w = 6
            fitted = [None]*w + [np.mean(actuals[i-w:i]) for i in range(w, len(actuals))]
            last_avg = np.mean(actuals[-w:])
            forecast = [last_avg] * forecast_periods
        elif method == "Exponential Smoothing":
            fitted = _exp_smoothing(actuals, alpha)
            forecast_val = fitted[-1]
            forecast = [forecast_val] * forecast_periods
        elif method == "Linear Trend Projection":
            x = np.arange(periods_hist)
            slope, intercept, _, _, _ = stats.linregress(x, actuals)
            fitted = [intercept + slope * i for i in x]
            forecast = [intercept + slope * (periods_hist + i) for i in range(forecast_periods)]
        else:  # Year-Ago + CAGR
            if periods_hist >= 24:
                growth = (actuals[-1] / actuals[-13]) - 1 if actuals[-13] > 0 else 0.07
            else:
                growth = 0.07
            fitted = [actuals[i-12] * (1+growth) if i >= 12 else None for i in range(periods_hist)]
            forecast = [actuals[-12 + i % 12] * (1+growth)**(1 + i//12) for i in range(forecast_periods)]

        dates_fc = pd.date_range(dates_hist[-1] + pd.DateOffset(months=1), periods=forecast_periods, freq="MS")

        fig = go.Figure()
        fig.add_trace(go.Bar(x=dates_hist, y=actuals, name="Actual Revenue",
                             marker_color="#B5D4F4", opacity=0.6))
        valid_fitted = [(d, f) for d, f in zip(dates_hist, fitted) if f is not None]
        if valid_fitted:
            fd, fv = zip(*valid_fitted)
            fig.add_trace(go.Scatter(x=list(fd), y=list(fv), name="Fitted", mode="lines",
                                     line=dict(color="#185FA5", width=2)))
        fig.add_trace(go.Scatter(x=dates_fc, y=forecast, name="Forecast",
                                 mode="lines+markers", line=dict(color="#E24B4A", width=2.5, dash="dash"),
                                 marker=dict(size=8)))
        fig.add_vrect(x0=str(dates_fc[0]), x1=str(dates_fc[-1]),
                      fillcolor="#FAEEDA", opacity=0.3, line_width=0, annotation_text="Forecast zone")
        fig.update_layout(title=f"Revenue Forecast — {method}",
                          template="plotly_white", height=420,
                          yaxis_title="Revenue ($M)", legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)

        fitted_vals = [f for f in fitted if f is not None]
        actual_vals = [a for a, f in zip(actuals, fitted) if f is not None]
        if fitted_vals and actual_vals:
            mape = np.mean(np.abs((np.array(actual_vals) - np.array(fitted_vals)) / np.array(actual_vals))) * 100
            mae  = np.mean(np.abs(np.array(actual_vals) - np.array(fitted_vals)))
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("MAPE", f"{mape:.1f}%", delta="Good" if mape < 10 else "Review method")
            c2.metric("MAE", f"${mae:.1f}M")
            c3.metric("Next Month Forecast", f"${forecast[0]:,.1f}M")
            c4.metric(f"{forecast_periods}M Forecast Avg", f"${np.mean(forecast):,.1f}M")

    # ── REGRESSION FORECASTER ─────────────────────────────────────────────────
    with tab3:
        _sec("Regression-Based Forecasting", "📊")
        st.markdown("""
Build a simple regression model to forecast a financial outcome from a leading indicator.
        """)
        c1, c2 = st.columns(2)
        with c1:
            x_label = st.selectbox("Leading indicator (X):",
                                   ["Production Volume (000 units)", "GDP Index", "Advertising Spend ($M)", "Headcount"])
            y_label = st.selectbox("Financial outcome (Y):",
                                   ["Revenue ($M)", "COGS ($M)", "Logistics Cost ($M)", "SG&A ($M)"])
        with c2:
            n_obs = st.slider("Number of observations", 12, 60, 24)
            noise_lvl = st.slider("Noise level (data quality)", 1, 10, 3)

        np.random.seed(42)
        x_data = np.random.uniform(80, 120, n_obs) * (1 + np.arange(n_obs) * 0.005)
        true_slope = np.random.uniform(3, 6)
        y_data = 100 + true_slope * x_data + np.random.normal(0, noise_lvl * 5, n_obs)

        slope, intercept, r_val, p_val, se = stats.linregress(x_data, y_data)
        r2 = r_val ** 2
        fitted_y = intercept + slope * x_data
        residuals = y_data - fitted_y

        fig = px.scatter(x=x_data, y=y_data, labels={"x": x_label, "y": y_label},
                         title=f"{y_label} vs. {x_label} (r² = {r2:.3f})",
                         trendline="ols", template="plotly_white", height=380)
        st.plotly_chart(fig, use_container_width=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("R² (explained variance)", f"{r2:.3f}")
        c2.metric("Slope (β)", f"{slope:.3f}")
        c3.metric("Intercept (α)", f"{intercept:.1f}")
        c4.metric("P-value", f"{p_val:.4f}", delta="Significant" if p_val < 0.05 else "Not significant")

        st.markdown("**Forecast: Enter a new X value to predict Y**")
        x_new = st.number_input(f"Enter {x_label} value:", value=float(x_data[-1] * 1.05), step=1.0, key="reg_xnew")
        y_pred = intercept + slope * x_new
        ci_margin = 1.96 * se * np.sqrt(1 + 1/n_obs + (x_new - x_data.mean())**2 / ((n_obs-1)*x_data.var()))
        c1, c2, c3 = st.columns(3)
        c1.metric(f"Predicted {y_label}", f"${y_pred:.1f}M")
        c2.metric("95% CI Lower", f"${y_pred - ci_margin:.1f}M")
        c3.metric("95% CI Upper", f"${y_pred + ci_margin:.1f}M")

        if r2 < 0.5:
            st.warning(f"⚠️ R² = {r2:.3f} — weak relationship. This indicator explains only {r2*100:.0f}% of variation in {y_label}. Consider adding more predictors or using a different indicator.")
        else:
            st.success(f"✅ R² = {r2:.3f} — {x_label} explains {r2*100:.0f}% of {y_label} variation. Statistically {'significant' if p_val < 0.05 else 'not yet significant'} (p = {p_val:.4f}).")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: 12-Month Revenue Forecast — Industrial Equipment Company", "🧪")
        st.markdown("""
**Situation:** You are the FP&A Director. The Board needs a bottom-up 12-month revenue forecast,
a sensitivity analysis, and a three-scenario plan for the next Annual Operating Plan (AOP).
        """)

        np.random.seed(42)
        hist_months = pd.date_range("2022-01-01", periods=36, freq="MS")
        base_trend  = 200 + np.arange(36) * 1.8
        seasonality = 20 * np.sin(2 * np.pi * np.arange(36) / 12 - np.pi/2)
        history     = base_trend + seasonality + np.random.normal(0, 8, 36)

        st.markdown("**Step 1 — 36 Months of Historical Revenue ($M)**")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=hist_months, y=history, marker_color="#B5D4F4",
                             name="Historical Revenue", opacity=0.7))
        ma12 = pd.Series(history).rolling(12).mean()
        fig.add_trace(go.Scatter(x=hist_months, y=ma12, name="12M Moving Avg",
                                 line=dict(color="#185FA5", width=2.5), mode="lines"))
        fig.update_layout(title="Historical Revenue (36 months) + 12M Moving Average",
                          template="plotly_white", height=380, yaxis_title="Revenue ($M)")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 2 — Seasonal Index Calculation**")
        seas_indices = []
        grand_mean = np.mean(history)
        months_of_year = [f"{pd.Timestamp('2000-01-01') + pd.DateOffset(months=m):%b}" for m in range(12)]
        for m in range(12):
            vals = [history[i] for i in range(m, 36, 12)]
            seas_indices.append(round(np.mean(vals) / grand_mean * 100, 1))
        seas_df = pd.DataFrame({"Month": months_of_year, "Seasonal Index": seas_indices,
                                 "Interpretation": ["Above avg" if v > 100 else "Below avg" for v in seas_indices]})
        st.dataframe(seas_df, use_container_width=True, hide_index=True)

        st.markdown("**Step 3 — 12-Month Forecast (3 Scenarios)**")
        cagr = (history[-1] / history[0]) ** (1/35) - 1
        fc_months = pd.date_range("2025-01-01", periods=12, freq="MS")

        fc_base  = [history[-12 + i] * (1 + cagr) * (seas_indices[i % 12] / 100) for i in range(12)]
        fc_best  = [v * 1.08 for v in fc_base]
        fc_worst = [v * 0.92 for v in fc_base]

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=hist_months[-12:], y=history[-12:],
                              marker_color="#B5D4F4", opacity=0.6, name="Prior Year Actual"))
        fig2.add_trace(go.Scatter(x=fc_months, y=fc_base,  name="Base Case",
                                  line=dict(color="#185FA5", width=2.5), mode="lines+markers"))
        fig2.add_trace(go.Scatter(x=fc_months, y=fc_best,  name="Best Case (+8%)",
                                  line=dict(color="#1D9E75", width=1.5, dash="dash"), mode="lines"))
        fig2.add_trace(go.Scatter(x=fc_months, y=fc_worst, name="Worst Case (−8%)",
                                  line=dict(color="#E24B4A", width=1.5, dash="dot"),  mode="lines"))
        fig2.update_layout(title="12-Month Revenue Forecast — 3 Scenarios",
                           template="plotly_white", height=400, yaxis_title="Revenue ($M)",
                           legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Step 4 — Sensitivity: Impact of Revenue Change on EBITDA**")
        base_ebitda_margin = 0.22
        base_rev_fc = sum(fc_base)
        sens_rows = []
        for delta in [-15, -10, -5, 0, +5, +10, +15]:
            adj_rev   = base_rev_fc * (1 + delta/100)
            adj_ebitda = adj_rev * base_ebitda_margin
            sens_rows.append({
                "Revenue Change": f"{delta:+}%",
                "Revenue ($M)": round(adj_rev, 1),
                "EBITDA ($M)":  round(adj_ebitda, 1),
                "EBITDA Change": f"{(adj_ebitda/( base_rev_fc*base_ebitda_margin)-1)*100:+.1f}%"
            })
        st.dataframe(pd.DataFrame(sens_rows), use_container_width=True, hide_index=True)

        c1, c2, c3 = st.columns(3)
        c1.metric("Base Case 12M Revenue",  f"${sum(fc_base):,.1f}M")
        c2.metric("Best Case 12M Revenue",  f"${sum(fc_best):,.1f}M")
        c3.metric("Worst Case 12M Revenue", f"${sum(fc_worst):,.1f}M")

        st.success("""
**Board Forecast Summary:**

- **Base Case** (most likely): 12-month revenue $2,856M — 7.2% growth vs prior year, driven by continued structural trend.
- **Best Case** (upside): Market outperformance + pricing power → +8% vs base.
- **Worst Case** (downside): Macro softening + customer order deferrals → −8% vs base.
- **Key assumption:** Seasonal pattern consistent with prior years. Watch Q4 order book as leading indicator.
- **MAPE of fitted model:** <8% — acceptable for planning purposes.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 5 Quiz", "❓")
        _quiz("1. Exponential smoothing with α = 0.9 will:",
              ["Produce a very smooth, slow-reacting forecast",
               "React very quickly to recent data — high volatility tracking",
               "Be identical to a 12-month moving average",
               "Require seasonal adjustment"],
              "React very quickly to recent data — high volatility tracking", "fa_m5q1")
        st.divider()
        _quiz("2. A MAPE of 3.2% on a revenue forecast means:",
              ["Revenue was $3.2M off", "The forecast was wrong 3.2 times",
               "On average the forecast was within 3.2% of actual — excellent accuracy",
               "R² = 3.2%"],
              "On average the forecast was within 3.2% of actual — excellent accuracy", "fa_m5q2")
        st.divider()
        _quiz("3. Time-series decomposition separates data into:",
              ["Price, Volume, Mix, and FX effects",
               "Trend, Seasonality, Cyclicality, and Random Noise",
               "Fixed costs, Variable costs, and Overheads",
               "Budget, Forecast, and Actual"],
              "Trend, Seasonality, Cyclicality, and Random Noise", "fa_m5q3")
        st.divider()
        _quiz("4. Scenario planning differs from sensitivity analysis because:",
              ["Scenario planning changes only one variable at a time",
               "Sensitivity analysis is more complex",
               "Scenario planning changes multiple variables simultaneously to describe a coherent future state",
               "They are identical techniques"],
              "Scenario planning changes multiple variables simultaneously to describe a coherent future state", "fa_m5q4")
        st.divider()
        _quiz("5. A Monte Carlo simulation result showing P10 = $80M and P90 = $130M means:",
              ["There's a 10% chance of achieving $80M",
               "There is an 80% probability that the outcome falls between $80M and $130M",
               "Expected value is $105M with certainty",
               "The model has a 10% error rate"],
              "There is an 80% probability that the outcome falls between $80M and $130M", "fa_m5q5")