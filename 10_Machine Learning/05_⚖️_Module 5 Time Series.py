"""
Machine Learning for Finance & Accounts
Module 5 – Time Series & Forecasting

USAGE: import ml_module_05; ml_module_05.show()
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#B45309"; SECONDARY="#F59E0B"; SUCCESS="#10B981"; DANGER="#EF4444"; ACCENT="#6366F1"


def _css():
    st.markdown("""
    <style>
    .main { background:#FFFBEB; }
    .hero-banner { background:linear-gradient(135deg,#B45309 0%,#D97706 60%,#F59E0B 100%);
        border-radius:16px; padding:2.4rem 2.8rem; color:white; margin-bottom:1.6rem; }
    .hero-banner h1 { font-size:2.1rem; margin:0 0 .4rem; font-weight:700; }
    .hero-banner p  { font-size:1.05rem; margin:0; opacity:.9; }
    .hero-badge { display:inline-block; background:rgba(255,255,255,.2);
        border:1px solid rgba(255,255,255,.35); border-radius:20px;
        padding:.18rem .8rem; font-size:.8rem; margin-bottom:.7rem; }
    .section-title { font-size:1.35rem; font-weight:700; color:#1E293B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #B45309; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .info-card .card-icon { font-size:1.7rem; margin-bottom:.4rem; }
    .info-card h4 { font-size:1rem; font-weight:700; color:#1E293B; margin:0 0 .3rem; }
    .info-card p  { font-size:.88rem; color:#475569; margin:0; line-height:1.55; }
    .definition-box { background:#FEF3C7; border-left:5px solid #B45309;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    .definition-box p { margin:0; color:#1E293B; font-size:.96rem; line-height:1.65; }
    .quiz-box { background:white; border-radius:12px; padding:1.4rem 1.6rem;
        box-shadow:0 2px 10px rgba(0,0,0,.08); margin-top:1rem; }
    .quiz-q { font-weight:700; color:#1E293B; font-size:1rem; margin-bottom:.8rem; }
    </style>""", unsafe_allow_html=True)


def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 5 — Time Series &amp; Forecasting</h1>
      <p>Master revenue forecasting, cash flow projection, and budget modelling
         using statistical and ML-based time series methods.</p>
    </div>""", unsafe_allow_html=True)
    for col,(icon,label,val) in zip(st.columns(4),[
        ("📅","Level","Intermediate"),("⏱️","Read time","~35 minutes"),
        ("📋","Methods","5 covered"),("🏆","Outcome","Build forecasting models"),
    ]):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""", unsafe_allow_html=True)


def _section_intro():
    st.markdown('<div class="section-title">⏱️ 1. What is Time Series Data?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p>A <strong>time series</strong> is a sequence of data points recorded at regular
      time intervals — daily, weekly, monthly, quarterly. Finance is fundamentally
      time-series: every transaction, balance, and metric has a timestamp.
      Forecasting means using past patterns to predict future values.</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### 📊 The four components of any time series")
    components = [
        ("📈","Trend","The long-term direction — is revenue growing or declining over years?"),
        ("🌊","Seasonality","Regular repeating patterns — December sales spike every year."),
        ("🔄","Cyclicality","Longer irregular cycles — economic boom and bust cycles."),
        ("⚡","Noise / Residual","Random variation — unpredictable day-to-day fluctuations."),
    ]
    cols = st.columns(4)
    for col, (icon, title, desc) in zip(cols, components):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    st.markdown("#### 📉 Decomposition of a retail revenue time series")
    np.random.seed(7)
    months = pd.date_range("2021-01-01", periods=48, freq="M")
    trend = np.linspace(100, 145, 48)
    seasonality = 15 * np.sin(2 * np.pi * np.arange(48) / 12 - np.pi/2)
    noise = np.random.randn(48) * 3
    revenue = trend + seasonality + noise

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=revenue, mode="lines", name="Actual revenue",
                             line=dict(color=PRIMARY, width=2)))
    fig.add_trace(go.Scatter(x=months, y=trend, mode="lines", name="Trend",
                             line=dict(color=DANGER, width=2, dash="dash")))
    fig.update_layout(title="Revenue with visible trend and seasonal pattern",
                      height=280, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=10),
                      xaxis=dict(gridcolor="#E2E8F0"), yaxis=dict(gridcolor="#E2E8F0", title="Revenue ($M)"),
                      legend=dict(x=0, y=1))
    st.plotly_chart(fig, use_container_width=True)


def _section_moving_average():
    st.markdown('<div class="section-title">📊 2. Moving Averages & Smoothing</div>', unsafe_allow_html=True)
    st.markdown("The simplest forecasting technique — average the last N periods. Used heavily in finance for trend identification and budget smoothing.")

    np.random.seed(42)
    months = pd.date_range("2022-01-01", periods=36, freq="M")
    actual = 80 + np.cumsum(np.random.randn(36)*2 + 0.8) + 12*np.sin(np.linspace(0,6,36))

    window = st.slider("Moving average window (months)", 2, 12, 3)
    ma = pd.Series(actual).rolling(window).mean().values

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=actual, mode="lines", name="Actual",
                             line=dict(color=SECONDARY, width=1.5), opacity=.7))
    fig.add_trace(go.Scatter(x=months, y=ma, mode="lines",
                             name=f"{window}-month MA", line=dict(color=PRIMARY, width=2.5)))
    fig.update_layout(title=f"Revenue with {window}-month moving average",
                      height=280, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=10),
                      xaxis=dict(gridcolor="#E2E8F0"), yaxis=dict(gridcolor="#E2E8F0"),
                      legend=dict(x=0,y=1))
    st.plotly_chart(fig, use_container_width=True)
    st.info(f"💡 A {window}-month moving average smooths out noise. Larger windows = smoother trend but slower to react to changes.")


def _section_arima():
    st.markdown('<div class="section-title">📐 3. ARIMA — Statistical Forecasting</div>', unsafe_allow_html=True)
    st.markdown("""
    **ARIMA (AutoRegressive Integrated Moving Average)** is the gold standard
    statistical forecasting model. It captures trend, autocorrelation (how today
    depends on yesterday), and moving average components.

    **ARIMA(p, d, q) parameters:**
    - **p** = number of lag observations (autoregression)
    - **d** = degree of differencing (to make series stationary)
    - **q** = size of moving average window
    """)

    np.random.seed(15)
    history_months = pd.date_range("2021-01-01", periods=36, freq="M")
    forecast_months = pd.date_range("2024-01-01", periods=12, freq="M")
    history = 100 + np.cumsum(np.random.randn(36)*2.5 + 1.2) + 10*np.sin(np.linspace(0,6,36))
    last = history[-1]
    forecast = last + np.cumsum(np.random.randn(12)*2 + 1.0) + 8*np.sin(np.linspace(0,2,12))
    ci_upper = forecast + 8 + np.linspace(0, 6, 12)
    ci_lower = forecast - 8 - np.linspace(0, 6, 12)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=history_months, y=history, mode="lines", name="Historical",
                             line=dict(color=PRIMARY, width=2)))
    fig.add_trace(go.Scatter(x=forecast_months, y=forecast, mode="lines", name="ARIMA Forecast",
                             line=dict(color=DANGER, width=2, dash="dash")))
    fig.add_trace(go.Scatter(
        x=list(forecast_months) + list(forecast_months[::-1]),
        y=list(ci_upper) + list(ci_lower[::-1]),
        fill="toself", fillcolor="rgba(239,68,68,0.1)",
        line=dict(color="rgba(0,0,0,0)"), name="95% CI"
    ))
    fig.add_vline(x=str(forecast_months[0]), line_dash="dot",
                  line_color="gray", annotation_text="Forecast start")
    fig.update_layout(title="ARIMA Revenue Forecast with 95% Confidence Interval",
                      height=300, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=10),
                      xaxis=dict(gridcolor="#E2E8F0"), yaxis=dict(gridcolor="#E2E8F0", title="Revenue ($M)"),
                      legend=dict(x=0,y=1))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    > **Finance tip:** ARIMA works best on stationary time series (no strong trend or seasonality).
    For seasonal data (like quarterly financials), use **SARIMA** — the seasonal extension.
    """)


def _section_ml_forecasting():
    st.markdown('<div class="section-title">🤖 4. ML-Based Forecasting (XGBoost for Time Series)</div>', unsafe_allow_html=True)
    st.markdown("""
    Traditional ARIMA uses only the time series itself. ML models can use
    **many additional features** (called exogenous variables), making them
    often more accurate for complex financial forecasting.
    """)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **Features you can add to ML forecasting models:**

        | Feature type | Examples |
        |--------------|---------|
        | Lag features | Revenue last month, last quarter |
        | Calendar | Month, quarter, is_month_end |
        | Macro | GDP growth, interest rates |
        | Business | Pipeline value, headcount |
        | Industry | Sector index, commodity prices |
        """)
    with c2:
        methods = ["ARIMA","Exponential Smoothing","Random Forest","XGBoost","LSTM (Deep Learning)"]
        mape = [8.2, 9.1, 6.8, 5.4, 5.1]
        complexity = [2, 1, 3, 3, 5]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=methods, y=mape, name="MAPE % (lower=better)",
                             marker_color=[SECONDARY, WARNING, SUCCESS, SUCCESS, ACCENT]))
        fig.update_layout(title="Forecast accuracy (MAPE %) by method",
                          height=270, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          margin=dict(t=35,b=60,l=10,r=10),
                          yaxis=dict(gridcolor="#E2E8F0", title="MAPE %"),
                          xaxis=dict(tickangle=20))
        st.plotly_chart(fig, use_container_width=True)

    st.success("💡 **Recommendation for finance professionals:** Start with ARIMA for simple series. "
               "Use XGBoost when you have multiple business drivers to include. "
               "Use LSTMs only for very large datasets (3+ years of daily data).")


def _section_interactive_forecast():
    st.markdown('<div class="section-title">🎛️ 5. Interactive: Build Your Cash Flow Forecast</div>', unsafe_allow_html=True)
    st.markdown("Adjust the business parameters below to see how they affect the 12-month cash flow forecast:")

    col1, col2, col3 = st.columns(3)
    with col1:
        base_revenue = st.number_input("Monthly base revenue ($K)", 100, 5000, 500, 50)
        growth_rate = st.slider("Monthly growth rate (%)", -5.0, 10.0, 2.0, 0.5)
    with col2:
        seasonality_amp = st.slider("Seasonality strength", 0, 50, 15)
        operating_cost_pct = st.slider("Operating costs (% of revenue)", 40, 90, 65)
    with col3:
        capex_monthly = st.number_input("Monthly capex ($K)", 0, 500, 50, 10)
        tax_rate = st.slider("Tax rate (%)", 0, 40, 25)

    months = pd.date_range("2025-01-01", periods=12, freq="M")
    month_nums = np.arange(12)
    revenue = base_revenue * (1 + growth_rate/100) ** month_nums
    seasonal = seasonality_amp * np.sin(2*np.pi*month_nums/12 - np.pi/2)
    revenue = revenue + seasonal

    operating_costs = revenue * operating_cost_pct / 100
    ebitda = revenue - operating_costs - capex_monthly
    tax = np.maximum(ebitda * tax_rate / 100, 0)
    free_cash_flow = ebitda - tax

    df_forecast = pd.DataFrame({
        "Month": [m.strftime("%b %Y") for m in months],
        "Revenue ($K)": revenue.round(1),
        "Operating Costs ($K)": operating_costs.round(1),
        "EBITDA ($K)": ebitda.round(1),
        "Free Cash Flow ($K)": free_cash_flow.round(1),
    })

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_forecast["Month"], y=df_forecast["Revenue ($K)"],
                         name="Revenue", marker_color=SECONDARY, opacity=.7))
    fig.add_trace(go.Bar(x=df_forecast["Month"], y=df_forecast["Operating Costs ($K)"],
                         name="Operating Costs", marker_color=DANGER, opacity=.7))
    fig.add_trace(go.Scatter(x=df_forecast["Month"], y=df_forecast["Free Cash Flow ($K)"],
                             mode="lines+markers", name="Free Cash Flow",
                             line=dict(color=SUCCESS, width=2.5), marker=dict(size=7)))
    fig.update_layout(
        title="12-Month Cash Flow Forecast", barmode="group",
        height=320, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=35,b=60,l=10,r=10),
        xaxis=dict(gridcolor="#E2E8F0", tickangle=30),
        yaxis=dict(gridcolor="#E2E8F0", title="$K"),
        legend=dict(x=0, y=1)
    )
    st.plotly_chart(fig, use_container_width=True)

    total_revenue = df_forecast["Revenue ($K)"].sum()
    total_fcf = df_forecast["Free Cash Flow ($K)"].sum()
    m1, m2, m3 = st.columns(3)
    m1.metric("Total 12M Revenue", f"${total_revenue:,.0f}K")
    m2.metric("Total Free Cash Flow", f"${total_fcf:,.0f}K",
              delta=f"{total_fcf/total_revenue*100:.1f}% FCF margin")
    m3.metric("Avg Monthly FCF", f"${total_fcf/12:,.0f}K")


def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 5 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q":"Q1. Revenue spikes every December and dips every January. This pattern is called:",
         "opts":["Trend","Noise","Seasonality","Cyclicality"],
         "ans":"Seasonality",
         "exp":"✅ Correct! Regular, repeating patterns tied to the calendar are called seasonality."},
        {"q":"Q2. Which forecasting method can incorporate external business drivers like pipeline value and headcount?",
         "opts":["Simple Moving Average","ARIMA","XGBoost ML Forecasting","Exponential Smoothing"],
         "ans":"XGBoost ML Forecasting",
         "exp":"✅ Correct! ML models like XGBoost accept multiple input features (exogenous variables), unlike pure statistical methods."},
        {"q":"Q3. ARIMA(2,1,1) — what does the '1' in the middle represent?",
         "opts":["One autoregressive term","One differencing step","One moving average term","One seasonal component"],
         "ans":"One differencing step",
         "exp":"✅ Correct! The middle parameter 'd' in ARIMA(p,d,q) represents the degree of differencing applied to make the series stationary."},
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("", q["opts"], key=f"mod5_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"❌ Correct answer: **{q['ans']}**\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True); st.markdown("")


def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 ML for Finance & Accounts** · Module 5 of 10")
    c2.markdown("<div style='text-align:center'><a href='?module=4' style='color:#B45309'>◀ Module 4</a>"
                " &nbsp;|&nbsp; <a href='?module=6' style='color:#B45309'>Module 6 ▶</a></div>",
                unsafe_allow_html=True)
    c3.markdown("<div style='text-align:right;color:#64748B;font-size:.85rem'>Knowledge Folder</div>",
                unsafe_allow_html=True)


def show():
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 5 — Sections")
        st.markdown("1. Time Series Basics\n2. Moving Averages\n3. ARIMA\n"
                    "4. ML Forecasting\n5. Interactive Forecast Builder\n---\n🧩 Quiz")
        st.progress(50, text="Module 5 / 10")
    _section_intro(); st.markdown("")
    _section_moving_average(); st.markdown("")
    _section_arima(); st.markdown("")
    _section_ml_forecasting(); st.markdown("")
    _section_interactive_forecast(); st.markdown("")
    _knowledge_check(); _footer()


if __name__ == "__main__":
    st.set_page_config(page_title="Module 5 – Time Series & Forecasting | Knowledge Folder",
                       page_icon="📅", layout="wide")
    show()