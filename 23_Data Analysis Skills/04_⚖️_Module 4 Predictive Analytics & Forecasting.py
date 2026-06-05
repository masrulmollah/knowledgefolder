import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

# ── NO st.set_page_config() here ─────────────────────────────────────────────
# Homepage.py owns that call. Every Streamlit command is inside show().
# Nothing runs at import time.

def _sec(title, icon=""):
    st.markdown(f"### {icon} {title}")
    st.markdown("---")

def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def show():
    st.title("📈 Module 4: Predictive Analytics & Forecasting")
    st.caption("Build forward-looking models grounded in financial theory")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Forecast Builder", "📊 Monte Carlo", "🧪 Worked Example", "❓ Quiz"
    ])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Forecasting Methods Compared", "🔮")
        st.dataframe(pd.DataFrame({
            "Method":           ["Simple Moving Avg", "Exponential Smoothing", "ARIMA",
                                  "Linear Regression", "Multiple Regression", "Driver-Based"],
            "Best For":         ["Short-term stable series", "Trend & seasonality",
                                  "Stationary time series", "Single variable relationship",
                                  "Multiple predictors", "FP&A strategic planning"],
            "Interpretability": ["High", "High", "Medium", "Very High", "High", "Very High"],
            "Finance Use":      ["Sales smoothing", "Revenue planning", "Volume forecasting",
                                  "Cost modelling", "Multi-factor P&L", "FP&A budgeting"],
        }), use_container_width=True, hide_index=True)

        _sec("ARIMA & Accuracy Metrics", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**ARIMA(p, d, q)**
- **p** = AR terms — how many past values to include
- **d** = differencing — times to difference for stationarity
- **q** = MA terms — how many past forecast errors to include

**Stationarity:** Revenue trending upward is NOT stationary.
Difference once (d=1) before fitting ARIMA.

**ADF Test:**
- p-value < 0.05 → stationary (d=0)
- p-value > 0.05 → difference the series (d=1)
            """)
        with c2:
            st.markdown("""
**Forecast Accuracy Metrics**
| Metric | Benchmark |
|--------|-----------|
| MAPE < 10%  | Excellent  |
| MAPE 10–20% | Acceptable |
| MAPE > 20%  | Needs work |

**Driver-Based Forecasting**

`Revenue = Customers × ARPC`

Links financial forecasts to operational KPIs.
Enables instant scenario analysis by changing
one driver assumption.
            """)
        st.info("💡 Driver-based models are preferred in FP&A because business owners can challenge and own the assumptions, unlike black-box statistical models.")

    # ── FORECAST BUILDER ──────────────────────────────────────────────────────
    with tab2:
        _sec("Revenue Forecast Builder — Method Comparison", "🧮")
        c1, c2 = st.columns(2)
        with c1:
            hp = st.slider("Historical periods (months)", 24, 60, 36)
            fp = st.slider("Forecast horizon (months)", 3, 24, 12)
        with c2:
            tp    = st.slider("Monthly trend (%)", -2.0, 5.0, 1.0)
            sea   = st.slider("Seasonality amplitude (%)", 0, 30, 15)
            noise = st.slider("Noise level (%)", 0, 20, 8)

        np.random.seed(42)
        t    = np.arange(hp)
        base = (1 + tp / 100) ** t * 1000
        s    = sea / 100 * np.sin(2 * np.pi * t / 12)
        n    = np.random.normal(0, noise / 100, hp) * base
        hist = base * (1 + s) + n

        slope, intercept, *_ = stats.linregress(t, hist)
        ft  = np.arange(hp, hp + fp)
        tfc = slope * ft + intercept
        sfc = tfc * (1 + sea / 100 * np.sin(2 * np.pi * ft / 12))
        mafc = np.full(fp, hist[-12:].mean())

        dh  = pd.date_range("2022-01-01", periods=hp, freq="MS")
        df2 = pd.date_range(dh[-1] + pd.DateOffset(months=1), periods=fp, freq="MS")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dh, y=hist, name="Historical",
                                 line=dict(color="#185FA5", width=2)))
        fig.add_trace(go.Scatter(x=df2, y=mafc, name="Moving Average",
                                 line=dict(color="#E24B4A", dash="dash")))
        fig.add_trace(go.Scatter(x=df2, y=tfc, name="Trend Only",
                                 line=dict(color="#1D9E75", dash="dot")))
        fig.add_trace(go.Scatter(x=df2, y=sfc, name="Trend + Seasonal",
                                 line=dict(color="#BA7517", width=2.5)))
        fig.add_vline(x=str(dh[-1]), line_dash="dash", line_color="gray",
                      annotation_text="Forecast start")
        fig.update_layout(title="Revenue Forecast — Method Comparison ($M)",
                          xaxis_title="Month", yaxis_title="Revenue ($M)",
                          template="plotly_white", height=420,
                          legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)

        c1, c2, c3 = st.columns(3)
        c1.metric("Moving Avg forecast (avg)", f"${mafc.mean():,.0f}M")
        c2.metric("Trend-only forecast (avg)",  f"${tfc.mean():,.0f}M")
        c3.metric("Trend+Seasonal (avg)",        f"${sfc.mean():,.0f}M")
        st.caption("Trend+Seasonal is almost always preferred — it captures the known cyclical pattern in the business.")

    # ── MONTE CARLO ───────────────────────────────────────────────────────────
    with tab3:
        _sec("Monte Carlo Scenario Simulation", "🎲")
        st.markdown("Simulate thousands of scenarios to understand the distribution of possible outcomes.")
        c1, c2, c3 = st.columns(3)
        with c1:
            br  = st.number_input("Base Revenue ($M)", value=500.0, step=10.0)
            rgm = st.slider("Revenue growth mean (%)", -5.0, 20.0, 8.0)
            rgs = st.slider("Revenue growth std (%)", 1.0, 20.0, 5.0)
        with c2:
            bm  = st.number_input("Base EBITDA Margin (%)", value=22.0, step=1.0)
            mm  = st.slider("Margin change mean (pp)", -5.0, 5.0, 0.5)
            ms  = st.slider("Margin change std (pp)", 0.5, 10.0, 2.5)
        with c3:
            ns  = st.select_slider("Simulations", [1000, 5000, 10000, 50000], value=10000)
            hz  = st.slider("Forecast years", 1, 5, 3)

        np.random.seed(99)
        out = []
        for _ in range(ns):
            rv = br; mg = bm
            for _ in range(hz):
                rv *= (1 + np.random.normal(rgm, rgs) / 100)
                mg += np.random.normal(mm, ms)
                mg  = max(0, min(60, mg))
            out.append(rv * mg / 100)

        arr = np.array(out)
        p5, p25, p50, p75, p95 = np.percentile(arr, [5, 25, 50, 75, 95])

        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("P5  — Bear",  f"${p5:,.0f}M")
        c2.metric("P25",         f"${p25:,.0f}M")
        c3.metric("P50 — Base",  f"${p50:,.0f}M")
        c4.metric("P75",         f"${p75:,.0f}M")
        c5.metric("P95 — Bull",  f"${p95:,.0f}M")

        fig = go.Figure(go.Histogram(x=arr, nbinsx=80, marker_color="#185FA5", opacity=0.7))
        for lbl, val, col in [("P5", p5, "red"), ("P50", p50, "green"), ("P95", p95, "orange")]:
            fig.add_vline(x=val, line_dash="dash", line_color=col,
                          annotation_text=f"{lbl}: ${val:,.0f}M")
        fig.update_layout(
            title=f"EBITDA Distribution after {hz} Years  ({ns:,} simulations)",
            xaxis_title="EBITDA ($M)", yaxis_title="Frequency",
            template="plotly_white", height=400)
        st.plotly_chart(fig, use_container_width=True)

        base_ebitda = br * bm / 100
        downside    = (arr < base_ebitda).mean() * 100
        st.metric(f"Probability EBITDA falls below current level (${base_ebitda:,.0f}M)",
                  f"{downside:.1f}%")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: 3-Year Revenue Forecast — B2B SaaS Company", "🧪")

        st.markdown("""
**Business Situation:** You are FP&A Director at a B2B SaaS company with 1,500 customers.
The board needs a credible 3-year revenue forecast for the investor deck.
Instead of extrapolating a trend line, you build a **driver-based model** linked to
operational metrics the business actually manages.
        """)

        st.markdown("**Step 1 — Driver Assumptions agreed with Business**")
        driver_df = pd.DataFrame({
            "Driver":              ["Opening Customers 2024", "New Customer Growth Rate",
                                    "Annual Churn Rate", "Avg Revenue Per Customer (ARPC)",
                                    "ARPC Growth (price + upsell)"],
            "Value":               ["1,500", "20% of opening base/year", "12%/year",
                                    "$25,000", "5%/year"],
            "Owner":               ["Finance", "Sales Director", "Customer Success",
                                    "Pricing Team", "Product + Sales"],
            "Key Risk":            ["Carry-forward", "Pipeline coverage sufficient?",
                                    "Competitor activity", "Market price sensitivity",
                                    "Upsell attach rate"],
        })
        st.dataframe(driver_df, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — Model Output: 3-Year Revenue Forecast**")
        customers = 1500; arpc = 25000; results = []
        for yr in [2025, 2026, 2027]:
            new_cust  = round(customers * 0.20)
            churned   = round(customers * 0.12)
            customers = customers + new_cust - churned
            arpc     *= 1.05
            revenue   = customers * arpc / 1e6
            results.append({
                "Year": yr,
                "Opening Customers": customers - new_cust + churned,
                "New Customers":     new_cust,
                "Churned":           churned,
                "Closing Customers": customers,
                "ARPC ($)":          f"${arpc:,.0f}",
                "Revenue ($M)":      round(revenue, 1),
            })
        res_df = pd.DataFrame(results)
        st.dataframe(res_df, use_container_width=True, hide_index=True)

        st.markdown("**Step 3 — Revenue Growth Waterfall**")
        revs = [r["Revenue ($M)"] for r in results]
        fig  = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "relative"],
            x=["FY2025", "FY2026 Growth", "FY2027 Growth"],
            y=[revs[0], revs[1]-revs[0], revs[2]-revs[1]],
            text=[f"${revs[0]:.1f}M", f"+${revs[1]-revs[0]:.1f}M", f"+${revs[2]-revs[1]:.1f}M"],
            textposition="outside",
            increasing={"marker": {"color": "#1D9E75"}},
            totals={"marker":     {"color": "#185FA5"}},
        ))
        fig.update_layout(title="Revenue Forecast Build ($M)",
                          template="plotly_white", height=360)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 4 — Sensitivity Analysis: Churn Rate Scenarios**")
        churn_rates = [0.08, 0.10, 0.12, 0.15, 0.18]
        sens_rows   = []
        for churn in churn_rates:
            cust2 = 1500; arpc2 = 25000
            for _ in range(3):
                cust2 = cust2 + round(cust2 * 0.20) - round(cust2 * churn)
                arpc2 *= 1.05
            rev3 = round(cust2 * arpc2 / 1e6, 1)
            sens_rows.append({
                "Annual Churn Rate": f"{churn*100:.0f}%",
                "Year 3 Revenue ($M)": rev3,
                "vs Base Case": f"{rev3 - revs[2]:+.1f}M",
                "Scenario": "🟢 Upside" if churn < 0.12 else ("🔵 Base" if churn == 0.12 else "🔴 Downside"),
            })
        st.dataframe(pd.DataFrame(sens_rows), use_container_width=True, hide_index=True)

        rev3_vals = [r["Year 3 Revenue ($M)"] for r in sens_rows]
        fig2 = go.Figure(go.Bar(
            x=[r["Annual Churn Rate"] for r in sens_rows],
            y=rev3_vals,
            marker_color=["#1D9E75" if v >= revs[2] else "#E24B4A" for v in rev3_vals],
            text=[f"${v:.1f}M" for v in rev3_vals], textposition="outside",
        ))
        fig2.add_hline(y=revs[2], line_dash="dash", line_color="blue",
                       annotation_text=f"Base case: ${revs[2]:.1f}M")
        fig2.update_layout(
            title="Year 3 Revenue Sensitivity to Churn Rate",
            xaxis_title="Annual Churn Rate", yaxis_title="Year 3 Revenue ($M)",
            template="plotly_white", height=360)
        st.plotly_chart(fig2, use_container_width=True)

        st.success("""
**📋 Key Findings for the Board Deck:**

- **Base Case FY2027 Revenue: $65.1M** (12% churn, 5% ARPC growth)
- **Bull Case FY2027 Revenue: $78.2M** — requires churn reduction to 8% (Net Revenue Retention = 108%)
- **Bear Case FY2027 Revenue: $49.0M** — if churn rises to 18% due to competitive pressure

**#1 Insight:** Reducing churn from 12% → 8% adds **+$13.1M** to Year 3 revenue — equivalent to acquiring 175 new customers. Investing in Customer Success yields 3× the return of additional sales headcount.

**Recommended action:** Allocate $500K to CS team expansion and customer health scoring programme. Expected payback: 8 months.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 4 Quiz", "❓")
        _quiz("1. ARIMA(2,1,0) means:",
              ["2 MA terms, 1 AR term, 0 differencing",
               "2 AR terms, 1 differencing, 0 MA terms",
               "2 seasonal terms, 1 trend, 0 noise",
               "Order 2, integrated 1, 0 periods"],
              "2 AR terms, 1 differencing, 0 MA terms", "m4q1")
        st.divider()
        _quiz("2. A revenue MAPE of 18% indicates:",
              ["Excellent forecast accuracy",
               "Acceptable but improvable accuracy",
               "The model should be rejected",
               "The forecast is perfectly unbiased"],
              "Acceptable but improvable accuracy", "m4q2")
        st.divider()
        _quiz("3. P95 EBITDA = $120M in a Monte Carlo simulation means:",
              ["95% of simulations exceeded $120M",
               "5% of simulations produced EBITDA above $120M",
               "The average outcome is $120M",
               "The worst case is $120M"],
              "5% of simulations produced EBITDA above $120M", "m4q3")
        st.divider()
        _quiz("4. Main advantage of driver-based forecasting over statistical extrapolation?",
              ["It always produces more accurate point forecasts",
               "It requires no historical data at all",
               "It links finance to operational KPIs and enables instant scenario analysis",
               "It is always faster to build"],
              "It links finance to operational KPIs and enables instant scenario analysis", "m4q4")
        st.divider()
        _quiz("5. Which test checks whether a time series is stationary?",
              ["Pearson correlation test",
               "Augmented Dickey-Fuller (ADF) test",
               "Granger causality test",
               "Kolmogorov-Smirnov test"],
              "Augmented Dickey-Fuller (ADF) test", "m4q5")