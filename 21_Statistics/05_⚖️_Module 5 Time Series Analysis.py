import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1a3a52 0%, #2a4a62 50%, #3a5a72 100%);
    }
    h1 {
        color: #4dd0e1;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #80deea;
        border-left: 6px solid #4dd0e1;
        padding-left: 15px;
    }
    h3 {
        color: #b2ebf2;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>📉 Module 5: Time Series Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #b2ebf2;'>Analyzing Sequential Data in Finance</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 5 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("5.1 Time Series Fundamentals")
    
    st.subheader("What is Time Series Data?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Definition:**
        Data points collected sequentially over time
        
        **Key Characteristics:**
        - Temporal ordering matters
        - Often exhibits patterns
        - May have dependencies
        - Used for forecasting
        
        **Examples in Finance:**
        - Stock prices
        - Interest rates
        - GDP growth
        - Trading volume
        - Exchange rates
        """)
    
    with col2:
        st.success("""
        **Components of Time Series:**
        
        **1. Trend (T):**
        - Long-term direction
        - Upward, downward, or flat
        
        **2. Seasonality (S):**
        - Regular periodic patterns
        - Daily, monthly, quarterly
        
        **3. Cyclical (C):**
        - Longer-term fluctuations
        - Business cycles
        
        **4. Irregular/Random (I):**
        - Unpredictable noise
        - Random shocks
        """)
    
    st.markdown("---")
    
    # Stationarity
    st.subheader("Stationarity")
    
    st.warning("""
    **Stationary Time Series:**
    Statistical properties (mean, variance, autocorrelation) remain constant over time
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Conditions for Stationarity:**")
        st.latex(r"E[Y_t] = \mu \text{ (constant mean)}")
        st.latex(r"Var[Y_t] = \sigma^2 \text{ (constant variance)}")
        st.latex(r"Cov[Y_t, Y_{t-k}] = \gamma_k \text{ (depends only on lag k)}")
        
        st.markdown("""
        **Why It Matters:**
        - Many models assume stationarity
        - Makes forecasting reliable
        - Allows for statistical inference
        """)
    
    with col2:
        st.markdown("**Testing for Stationarity:**")
        
        st.info("""
        **Augmented Dickey-Fuller (ADF) Test:**
        - H₀: Series has unit root (non-stationary)
        - H₁: Series is stationary
        - If p-value < 0.05 → Reject H₀ (stationary)
        
        **KPSS Test:**
        - H₀: Series is stationary
        - H₁: Series has unit root
        - Complement to ADF test
        """)
        
        st.markdown("""
        **Making Series Stationary:**
        - Differencing: Yₜ - Yₜ₋₁
        - Log transformation
        - Detrending
        - Seasonal adjustment
        """)
    
    st.markdown("---")
    
    # Autocorrelation
    st.subheader("Autocorrelation and Partial Autocorrelation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**ACF (Autocorrelation Function):**")
        
        st.latex(r"\rho_k = \frac{Cov(Y_t, Y_{t-k})}{Var(Y_t)}")
        
        st.info("""
        **Measures:**
        - Correlation between Yₜ and Yₜ₋ₖ
        - Includes indirect effects
        - Shows persistence in data
        
        **Interpretation:**
        - High autocorrelation → Strong persistence
        - Slow decay → Trend present
        - Spikes at specific lags → Seasonality
        """)
    
    with col2:
        st.markdown("**PACF (Partial Autocorrelation Function):**")
        
        st.info("""
        **Measures:**
        - Direct correlation between Yₜ and Yₜ₋ₖ
        - Removes intermediate effects
        - Shows pure lag-k relationship
        
        **Use in Model Selection:**
        - **AR(p):** PACF cuts off after lag p
        - **MA(q):** ACF cuts off after lag q
        - **ARMA:** Both decay gradually
        """)
    
    st.markdown("---")
    
    # Time Series Models
    st.header("5.2 Time Series Models")
    
    st.subheader("Autoregressive (AR) Models")
    
    st.latex(r"Y_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + ... + \phi_p Y_{t-p} + \epsilon_t")
    
    st.info("""
    **AR(p) Model:**
    - Current value depends on p past values
    - φ: autoregressive coefficients
    - p: order (number of lags)
    
    **Example AR(1):**
    """)
    st.latex(r"Y_t = c + \phi_1 Y_{t-1} + \epsilon_t")
    
    st.markdown("""
    **Applications:**
    - Stock returns (mean reversion)
    - Interest rates
    - GDP growth
    
    **Characteristics:**
    - Models persistence
    - PACF cuts off at lag p
    - ACF decays gradually
    """)
    
    st.markdown("---")
    
    st.subheader("Moving Average (MA) Models")
    
    st.latex(r"Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + ... + \theta_q \epsilon_{t-q}")
    
    st.info("""
    **MA(q) Model:**
    - Current value depends on q past errors
    - θ: moving average coefficients
    - q: order (number of lags)
    
    **Example MA(1):**
    """)
    st.latex(r"Y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1}")
    
    st.markdown("""
    **Applications:**
    - Shocks to financial markets
    - Trading signals
    - Forecast errors
    
    **Characteristics:**
    - Models temporary shocks
    - ACF cuts off at lag q
    - PACF decays gradually
    """)
    
    st.markdown("---")
    
    st.subheader("ARMA Models")
    
    st.latex(r"Y_t = c + \sum_{i=1}^{p}\phi_i Y_{t-i} + \epsilon_t + \sum_{j=1}^{q}\theta_j \epsilon_{t-j}")
    
    st.success("""
    **ARMA(p,q):**
    - Combines AR and MA components
    - More flexible than pure AR or MA
    - Both ACF and PACF decay
    
    **Model Selection:**
    - Use ACF/PACF plots
    - Information criteria (AIC, BIC)
    - Grid search over p, q
    """)
    
    st.markdown("---")
    
    st.subheader("ARIMA Models")
    
    st.latex(r"\text{ARIMA(p,d,q)}")
    
    st.warning("""
    **ARIMA = ARMA + Differencing**
    
    **Parameters:**
    - **p:** AR order
    - **d:** Degree of differencing
    - **q:** MA order
    
    **Differencing:**
    - d=0: No differencing (ARMA)
    - d=1: First difference (Δy = yₜ - yₜ₋₁)
    - d=2: Second difference
    
    **When to Use:**
    - Non-stationary series
    - Trending data
    - Most financial time series
    
    **Example:**
    - ARIMA(1,1,1): One AR lag, first difference, one MA lag
    - ARIMA(0,1,0): Random walk with drift
    """)
    
    st.markdown("---")
    
    # Volatility Models
    st.header("5.3 Volatility Modeling")
    
    st.subheader("ARCH Models")
    
    st.latex(r"\sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 + ... + \alpha_q \epsilon_{t-q}^2")
    
    st.info("""
    **ARCH(q) - Autoregressive Conditional Heteroscedasticity:**
    
    **Key Idea:**
    - Variance changes over time
    - Large shocks → Higher volatility
    - Volatility clustering
    
    **Financial Phenomena:**
    - Volatility clusters in markets
    - "Calm periods and storms"
    - Risk changes over time
    """)
    
    st.markdown("---")
    
    st.subheader("GARCH Models")
    
    st.latex(r"\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2")
    
    st.success("""
    **GARCH(1,1) - Most Common:**
    
    **Components:**
    - ω: Constant term
    - α: Impact of past shocks (ARCH effect)
    - β: Persistence of volatility (GARCH effect)
    
    **Properties:**
    - α + β < 1 for stationarity
    - High β → Long memory in volatility
    - Widely used in risk management
    
    **Applications:**
    - VaR estimation
    - Option pricing
    - Portfolio risk
    - Hedging strategies
    
    **Advantages over ARCH:**
    - More parsimonious
    - Better long-term forecasts
    - Captures persistence
    """)
    
    st.markdown("---")
    
    # Forecasting
    st.header("5.4 Forecasting")
    
    st.subheader("Forecast Evaluation Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Mean Absolute Error (MAE):**")
        st.latex(r"MAE = \frac{1}{n}\sum_{t=1}^{n}|y_t - \hat{y}_t|")
        
        st.markdown("**Mean Squared Error (MSE):**")
        st.latex(r"MSE = \frac{1}{n}\sum_{t=1}^{n}(y_t - \hat{y}_t)^2")
        
        st.markdown("**Root MSE:**")
        st.latex(r"RMSE = \sqrt{MSE}")
    
    with col2:
        st.markdown("**Mean Absolute Percentage Error (MAPE):**")
        st.latex(r"MAPE = \frac{100\%}{n}\sum_{t=1}^{n}\left|\frac{y_t - \hat{y}_t}{y_t}\right|")
        
        st.info("""
        **Choosing a Metric:**
        - **MAE:** Same units as data
        - **RMSE:** Penalizes large errors
        - **MAPE:** Scale-independent (%)
        - **AIC/BIC:** In-sample model selection
        """)
    
    st.markdown("---")
    
    st.subheader("Financial Forecasting Applications")
    
    tabs = st.tabs(["Stock Returns", "Volatility", "Economic Indicators"])
    
    with tabs[0]:
        st.markdown("""
        **Forecasting Stock Returns:**
        
        **Challenges:**
        - Weak autocorrelation
        - Random walk hypothesis
        - Market efficiency
        
        **Approaches:**
        - ARIMA for short-term
        - Factor models
        - Machine learning
        - Sentiment analysis
        
        **Reality Check:**
        - Point forecasts often poor
        - Interval forecasts more useful
        - Direction prediction hard
        - Risk forecasting more reliable
        """)
    
    with tabs[1]:
        st.markdown("""
        **Volatility Forecasting:**
        
        **Better Success Rate:**
        - Volatility more predictable
        - Strong persistence
        - GARCH models work well
        
        **Applications:**
        - VaR calculations
        - Option pricing
        - Risk management
        - Portfolio allocation
        
        **Models:**
        - GARCH(1,1) baseline
        - EGARCH for asymmetry
        - Realized volatility
        - Implied volatility
        """)
    
    with tabs[2]:
        st.markdown("""
        **Economic Indicators:**
        
        **Common Series:**
        - GDP growth
        - Inflation (CPI)
        - Unemployment
        - Interest rates
        
        **Characteristics:**
        - Strong trends
        - Seasonal patterns
        - Policy interventions
        
        **Models:**
        - ARIMA for trends
        - Seasonal ARIMA
        - VAR for multi-series
        - Structural breaks
        """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Real-World Time Series Examples")
    
    # Example 1: Stationarity Testing
    st.subheader("Example 1: Testing for Stationarity")
    
    st.markdown("""
    **Scenario:** Analyze a stock price series for stationarity.
    """)
    
    # Generate sample data
    np.random.seed(42)
    n = 200
    
    # Non-stationary: Random walk with drift
    drift = 0.1
    noise = np.random.normal(0, 1, n)
    price = 100 + np.cumsum(drift + noise)
    
    # Stationary: Returns
    returns = np.diff(price) / price[:-1] * 100
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Stock Prices (Non-Stationary):**")
        
        # ADF test on prices
        adf_price = adfuller(price)
        
        st.code(f"""
ADF Test on Prices:
ADF Statistic: {adf_price[0]:.4f}
p-value: {adf_price[1]:.4f}
Critical Values:
  1%: {adf_price[4]['1%']:.4f}
  5%: {adf_price[4]['5%']:.4f}
  10%: {adf_price[4]['10%']:.4f}
        """)
        
        if adf_price[1] > 0.05:
            st.error("❌ Non-Stationary (p > 0.05)")
            st.markdown("**Conclusion:** Series has unit root - not suitable for direct modeling")
        else:
            st.success("✅ Stationary (p < 0.05)")
        
        st.markdown("---")
        
        st.markdown("**Returns (Stationary):**")
        
        # ADF test on returns
        adf_returns = adfuller(returns)
        
        st.code(f"""
ADF Test on Returns:
ADF Statistic: {adf_returns[0]:.4f}
p-value: {adf_returns[1]:.4f}
Critical Values:
  1%: {adf_returns[4]['1%']:.4f}
  5%: {adf_returns[4]['5%']:.4f}
  10%: {adf_returns[4]['10%']:.4f}
        """)
        
        if adf_returns[1] > 0.05:
            st.error("❌ Non-Stationary (p > 0.05)")
        else:
            st.success("✅ Stationary (p < 0.05)")
            st.markdown("**Conclusion:** Returns are stationary - suitable for modeling")
    
    with col2:
        # Plot prices
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            y=price,
            mode='lines',
            name='Stock Price',
            line=dict(color='#4dd0e1', width=2)
        ))
        fig1.update_layout(
            title="Stock Prices (Non-Stationary)",
            xaxis_title="Time",
            yaxis_title="Price ($)",
            template="plotly_dark",
            height=250
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Plot returns
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            y=returns,
            mode='lines',
            name='Returns',
            line=dict(color='#80deea', width=1)
        ))
        fig2.add_hline(y=0, line_dash="dash", line_color="yellow")
        fig2.update_layout(
            title="Returns (Stationary)",
            xaxis_title="Time",
            yaxis_title="Return (%)",
            template="plotly_dark",
            height=250
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Example 2: ACF/PACF Analysis
    st.subheader("Example 2: ACF and PACF Analysis")
    
    st.markdown("""
    **Scenario:** Determine appropriate ARIMA model using ACF and PACF plots.
    """)
    
    # Generate AR(1) process
    np.random.seed(123)
    n = 200
    phi = 0.7
    ar1_data = [0]
    for t in range(1, n):
        ar1_data.append(phi * ar1_data[t-1] + np.random.normal(0, 1))
    ar1_data = np.array(ar1_data)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**ACF Analysis:**")
        
        # Calculate ACF
        acf_values = acf(ar1_data, nlags=20)
        
        fig_acf = go.Figure()
        fig_acf.add_trace(go.Bar(
            x=list(range(len(acf_values))),
            y=acf_values,
            marker_color='#4dd0e1'
        ))
        
        # Confidence bands
        conf_level = 1.96 / np.sqrt(len(ar1_data))
        fig_acf.add_hline(y=conf_level, line_dash="dash", line_color="red")
        fig_acf.add_hline(y=-conf_level, line_dash="dash", line_color="red")
        
        fig_acf.update_layout(
            title="Autocorrelation Function (ACF)",
            xaxis_title="Lag",
            yaxis_title="ACF",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig_acf, use_container_width=True)
        
        st.info("""
        **ACF Pattern:**
        - Gradual decay (exponential)
        - Significant at multiple lags
        - Suggests AR process
        """)
    
    with col2:
        st.markdown("**PACF Analysis:**")
        
        # Calculate PACF
        pacf_values = pacf(ar1_data, nlags=20)
        
        fig_pacf = go.Figure()
        fig_pacf.add_trace(go.Bar(
            x=list(range(len(pacf_values))),
            y=pacf_values,
            marker_color='#80deea'
        ))
        
        # Confidence bands
        fig_pacf.add_hline(y=conf_level, line_dash="dash", line_color="red")
        fig_pacf.add_hline(y=-conf_level, line_dash="dash", line_color="red")
        
        fig_pacf.update_layout(
            title="Partial Autocorrelation Function (PACF)",
            xaxis_title="Lag",
            yaxis_title="PACF",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig_pacf, use_container_width=True)
        
        st.success("""
        **PACF Pattern:**
        - Significant spike at lag 1
        - Cuts off after lag 1
        - Other lags within confidence bands
        - **Conclusion: AR(1) model appropriate**
        """)
    
    st.markdown("---")
    
    # Example 3: ARIMA Forecasting
    st.subheader("Example 3: ARIMA Forecasting")
    
    st.markdown("""
    **Scenario:** Forecast future values using ARIMA model.
    """)
    
    # Simulate ARIMA process
    np.random.seed(456)
    n = 100
    forecast_horizon = 10
    
    # Simple AR(1) for demonstration
    data = [10]
    phi = 0.8
    for t in range(1, n):
        data.append(5 + phi * data[t-1] + np.random.normal(0, 2))
    data = np.array(data)
    
    # Simple forecast (AR1 continuation)
    forecasts = []
    last_value = data[-1]
    for h in range(forecast_horizon):
        forecast = 5 + phi * last_value
        forecasts.append(forecast)
        last_value = forecast
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Model Summary:**")
        
        st.code(f"""
Model: ARIMA(1,0,0)

Coefficients:
  AR(1): {phi:.3f}
  Constant: 5.000

Sample Size: {n}
Forecast Horizon: {forecast_horizon}

Forecasts:
{[f"{f:.2f}" for f in forecasts[:5]]}...
        """)
        
        st.info("""
        **Interpretation:**
        - AR(1) coefficient shows persistence
        - Mean-reverting to constant level
        - Forecast uncertainty increases with horizon
        """)
    
    with col2:
        # Plot forecast
        fig = go.Figure()
        
        # Historical data
        fig.add_trace(go.Scatter(
            y=data,
            mode='lines',
            name='Historical',
            line=dict(color='#4dd0e1', width=2)
        ))
        
        # Forecasts
        forecast_x = list(range(n, n + forecast_horizon))
        fig.add_trace(go.Scatter(
            x=forecast_x,
            y=forecasts,
            mode='lines',
            name='Forecast',
            line=dict(color='#ffa726', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="ARIMA Forecast",
            xaxis_title="Time",
            yaxis_title="Value",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.success("""
    **Forecast Characteristics:**
    - Point forecasts show expected path
    - Converges to long-run mean
    - Uncertainty grows with horizon
    - Use confidence intervals in practice
    """)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Time Series Analysis")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["Stationarity Explorer", "ACF/PACF Analyzer", "ARIMA Simulator", "Volatility Clustering"]
    )
    
    if exercise == "Stationarity Explorer":
        st.subheader("📊 Stationarity Explorer")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Generate Time Series:**")
            
            series_type = st.selectbox("Series Type:", 
                                      ["Random Walk", "Trend", "Stationary AR(1)", "White Noise"])
            
            n_points = st.slider("Number of points:", 50, 500, 200)
            
            if series_type == "Random Walk":
                drift = st.slider("Drift:", -0.5, 0.5, 0.0, 0.05)
                noise_std = st.slider("Noise Std Dev:", 0.1, 5.0, 1.0)
                
                np.random.seed(42)
                noise = np.random.normal(0, noise_std, n_points)
                series = 100 + np.cumsum(drift + noise)
                
            elif series_type == "Trend":
                slope = st.slider("Trend slope:", -1.0, 1.0, 0.1, 0.05)
                noise_std = st.slider("Noise Std Dev:", 0.1, 5.0, 1.0)
                
                np.random.seed(42)
                trend = slope * np.arange(n_points)
                noise = np.random.normal(0, noise_std, n_points)
                series = 100 + trend + noise
                
            elif series_type == "Stationary AR(1)":
                phi = st.slider("AR coefficient (φ):", -0.9, 0.9, 0.7, 0.1)
                noise_std = st.slider("Noise Std Dev:", 0.1, 5.0, 1.0)
                
                np.random.seed(42)
                series = [100]
                for t in range(1, n_points):
                    series.append(phi * series[t-1] + np.random.normal(0, noise_std))
                series = np.array(series)
                
            else:  # White Noise
                noise_std = st.slider("Noise Std Dev:", 0.1, 5.0, 1.0)
                
                np.random.seed(42)
                series = np.random.normal(100, noise_std, n_points)
            
            # ADF Test
            if st.button("Run ADF Test"):
                adf_result = adfuller(series)
                
                st.markdown("**ADF Test Results:**")
                st.metric("ADF Statistic", f"{adf_result[0]:.4f}")
                st.metric("p-value", f"{adf_result[1]:.4f}")
                
                if adf_result[1] < 0.05:
                    st.success("✅ Stationary (reject H₀)")
                else:
                    st.error("❌ Non-Stationary (fail to reject H₀)")
                
                st.code(f"""
Critical Values:
  1%: {adf_result[4]['1%']:.4f}
  5%: {adf_result[4]['5%']:.4f}
  10%: {adf_result[4]['10%']:.4f}
                """)
        
        with col2:
            # Plot series
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                y=series,
                mode='lines',
                line=dict(color='#4dd0e1', width=2)
            ))
            fig.update_layout(
                title=f"{series_type} Series",
                xaxis_title="Time",
                yaxis_title="Value",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Rolling statistics
            window = 20
            if len(series) >= window:
                rolling_mean = pd.Series(series).rolling(window=window).mean()
                rolling_std = pd.Series(series).rolling(window=window).std()
                
                fig2 = go.Figure()
                
                fig2.add_trace(go.Scatter(
                    y=rolling_mean,
                    mode='lines',
                    name='Rolling Mean',
                    line=dict(color='yellow', width=2)
                ))
                
                fig2.add_trace(go.Scatter(
                    y=rolling_std,
                    mode='lines',
                    name='Rolling Std',
                    line=dict(color='orange', width=2)
                ))
                
                fig2.update_layout(
                    title="Rolling Statistics (Window=20)",
                    xaxis_title="Time",
                    yaxis_title="Value",
                    template="plotly_dark",
                    height=300
                )
                st.plotly_chart(fig2, use_container_width=True)
    
    elif exercise == "ACF/PACF Analyzer":
        st.subheader("📈 ACF/PACF Analyzer")
        
        st.markdown("**Generate or Upload Data:**")
        
        data_source = st.radio("Data Source:", ["Generate", "Manual Input"])
        
        if data_source == "Generate":
            col1, col2 = st.columns(2)
            
            with col1:
                model_type = st.selectbox("Model:", ["AR(1)", "AR(2)", "MA(1)", "MA(2)", "ARMA(1,1)"])
                n_obs = st.slider("Observations:", 50, 500, 200)
            
            with col2:
                if "AR" in model_type:
                    phi1 = st.slider("φ₁:", -0.9, 0.9, 0.6, 0.1)
                    if "AR(2)" in model_type:
                        phi2 = st.slider("φ₂:", -0.5, 0.5, 0.3, 0.1)
                
                if "MA" in model_type:
                    theta1 = st.slider("θ₁:", -0.9, 0.9, 0.5, 0.1)
                    if "MA(2)" in model_type:
                        theta2 = st.slider("θ₂:", -0.5, 0.5, 0.2, 0.1)
            
            # Generate data
            np.random.seed(42)
            
            if model_type == "AR(1)":
                data = [0]
                for t in range(1, n_obs):
                    data.append(phi1 * data[t-1] + np.random.normal(0, 1))
                data = np.array(data)
                
            elif model_type == "AR(2)":
                data = [0, 0]
                for t in range(2, n_obs):
                    data.append(phi1 * data[t-1] + phi2 * data[t-2] + np.random.normal(0, 1))
                data = np.array(data)
                
            elif model_type == "MA(1)":
                errors = np.random.normal(0, 1, n_obs)
                data = [errors[0]]
                for t in range(1, n_obs):
                    data.append(errors[t] + theta1 * errors[t-1])
                data = np.array(data)
                
            elif model_type == "MA(2)":
                errors = np.random.normal(0, 1, n_obs)
                data = [errors[0], errors[1]]
                for t in range(2, n_obs):
                    data.append(errors[t] + theta1 * errors[t-1] + theta2 * errors[t-2])
                data = np.array(data)
                
            else:  # ARMA(1,1)
                errors = np.random.normal(0, 1, n_obs)
                data = [errors[0]]
                for t in range(1, n_obs):
                    data.append(phi1 * data[t-1] + errors[t] + theta1 * errors[t-1])
                data = np.array(data)
        
        else:
            data_input = st.text_area("Enter data (comma-separated):",
                                     height=100)
            if data_input:
                try:
                    data = np.array([float(x.strip()) for x in data_input.split(',')])
                except:
                    st.error("Invalid data format")
                    data = None
            else:
                data = None
        
        if data is not None and len(data) > 10:
            col1, col2 = st.columns(2)
            
            with col1:
                # ACF
                acf_vals = acf(data, nlags=min(40, len(data)//4))
                
                fig_acf = go.Figure()
                fig_acf.add_trace(go.Bar(
                    x=list(range(len(acf_vals))),
                    y=acf_vals,
                    marker_color='#4dd0e1'
                ))
                
                conf = 1.96 / np.sqrt(len(data))
                fig_acf.add_hline(y=conf, line_dash="dash", line_color="red")
                fig_acf.add_hline(y=-conf, line_dash="dash", line_color="red")
                
                fig_acf.update_layout(
                    title="Autocorrelation Function (ACF)",
                    xaxis_title="Lag",
                    yaxis_title="ACF",
                    template="plotly_dark",
                    height=400
                )
                st.plotly_chart(fig_acf, use_container_width=True)
            
            with col2:
                # PACF
                pacf_vals = pacf(data, nlags=min(40, len(data)//4))
                
                fig_pacf = go.Figure()
                fig_pacf.add_trace(go.Bar(
                    x=list(range(len(pacf_vals))),
                    y=pacf_vals,
                    marker_color='#80deea'
                ))
                
                fig_pacf.add_hline(y=conf, line_dash="dash", line_color="red")
                fig_pacf.add_hline(y=-conf, line_dash="dash", line_color="red")
                
                fig_pacf.update_layout(
                    title="Partial Autocorrelation Function (PACF)",
                    xaxis_title="Lag",
                    yaxis_title="PACF",
                    template="plotly_dark",
                    height=400
                )
                st.plotly_chart(fig_pacf, use_container_width=True)
            
            st.info("""
            **Interpretation Guide:**
            - **AR(p):** PACF cuts off after lag p, ACF decays
            - **MA(q):** ACF cuts off after lag q, PACF decays
            - **ARMA:** Both ACF and PACF decay gradually
            """)
    
    elif exercise == "ARIMA Simulator":
        st.subheader("🔮 ARIMA Simulator")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Model Parameters:**")
            
            p = st.slider("AR order (p):", 0, 3, 1)
            d = st.slider("Differencing (d):", 0, 2, 0)
            q = st.slider("MA order (q):", 0, 3, 0)
            
            n_obs = st.slider("Observations:", 100, 500, 200)
            forecast_steps = st.slider("Forecast steps:", 5, 50, 10)
            
            if st.button("Simulate & Forecast"):
                # Simple simulation (AR1 for demo)
                np.random.seed(42)
                
                if p > 0:
                    phi = 0.7
                    data = [0]
                    for t in range(1, n_obs):
                        data.append(phi * data[t-1] + np.random.normal(0, 1))
                    data = np.array(data)
                    
                    # Simple forecast
                    forecasts = []
                    last_val = data[-1]
                    for h in range(forecast_steps):
                        fc = phi * last_val
                        forecasts.append(fc)
                        last_val = fc
                else:
                    data = np.random.normal(0, 1, n_obs)
                    forecasts = [0] * forecast_steps
                
                st.session_state['sim_data'] = data
                st.session_state['forecasts'] = forecasts
                st.session_state['n_obs'] = n_obs
        
        with col2:
            if 'sim_data' in st.session_state:
                data = st.session_state['sim_data']
                forecasts = st.session_state['forecasts']
                n = st.session_state['n_obs']
                
                fig = go.Figure()
                
                # Historical
                fig.add_trace(go.Scatter(
                    y=data,
                    mode='lines',
                    name='Historical',
                    line=dict(color='#4dd0e1', width=2)
                ))
                
                # Forecast
                fc_x = list(range(n, n + len(forecasts)))
                fig.add_trace(go.Scatter(
                    x=fc_x,
                    y=forecasts,
                    mode='lines',
                    name='Forecast',
                    line=dict(color='#ffa726', width=2, dash='dash')
                ))
                
                fig.update_layout(
                    title=f"ARIMA({p},{d},{q}) Simulation & Forecast",
                    xaxis_title="Time",
                    yaxis_title="Value",
                    template="plotly_dark",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
    
    elif exercise == "Volatility Clustering":
        st.subheader("📊 Volatility Clustering Demonstration")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**GARCH Parameters:**")
            
            omega = st.slider("ω (constant):", 0.01, 0.5, 0.1, 0.01)
            alpha = st.slider("α (ARCH):", 0.01, 0.5, 0.15, 0.01)
            beta = st.slider("β (GARCH):", 0.01, 0.95, 0.75, 0.01)
            
            n_obs = st.slider("Observations:", 200, 1000, 500)
            
            if alpha + beta >= 1:
                st.error("⚠️ α + β must be < 1 for stationarity!")
            
            if st.button("Simulate GARCH"):
                # Simulate GARCH(1,1)
                np.random.seed(42)
                
                sigma2 = np.zeros(n_obs)
                returns = np.zeros(n_obs)
                
                sigma2[0] = omega / (1 - alpha - beta)
                
                for t in range(n_obs):
                    epsilon = np.random.normal(0, 1)
                    returns[t] = np.sqrt(sigma2[t]) * epsilon
                    
                    if t < n_obs - 1:
                        sigma2[t+1] = omega + alpha * returns[t]**2 + beta * sigma2[t]
                
                st.session_state['garch_returns'] = returns
                st.session_state['garch_vol'] = np.sqrt(sigma2)
        
        with col2:
            if 'garch_returns' in st.session_state:
                returns = st.session_state['garch_returns']
                volatility = st.session_state['garch_vol']
                
                # Returns plot
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(
                    y=returns,
                    mode='lines',
                    name='Returns',
                    line=dict(color='#4dd0e1', width=1)
                ))
                fig1.update_layout(
                    title="Simulated Returns (Volatility Clustering)",
                    xaxis_title="Time",
                    yaxis_title="Return",
                    template="plotly_dark",
                    height=250
                )
                st.plotly_chart(fig1, use_container_width=True)
                
                # Volatility plot
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    y=volatility,
                    mode='lines',
                    name='Conditional Volatility',
                    line=dict(color='#ffa726', width=2),
                    fill='tozeroy',
                    fillcolor='rgba(255, 167, 38, 0.3)'
                ))
                fig2.update_layout(
                    title="Conditional Volatility (σₜ)",
                    xaxis_title="Time",
                    yaxis_title="Volatility",
                    template="plotly_dark",
                    height=250
                )
                st.plotly_chart(fig2, use_container_width=True)
                
                st.success("""
                **Observe:**
                - Periods of high volatility cluster together
                - Returns show varying variance over time
                - GARCH captures this dynamic behavior
                """)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Time Series Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["Stationarity Test", "ACF/PACF Calculator", "ARIMA Forecast", "Forecast Evaluation"]
    )
    
    if calc_type == "Stationarity Test":
        st.subheader("Stationarity Test Calculator")
        
        st.markdown("**Enter your time series data (comma-separated):**")
        
        data_input = st.text_area("Data:", height=150)
        
        if st.button("Run Tests"):
            try:
                data = np.array([float(x.strip()) for x in data_input.split(',')])
                
                if len(data) < 10:
                    st.error("Need at least 10 observations")
                else:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # ADF Test
                        st.markdown("**Augmented Dickey-Fuller Test:**")
                        
                        adf_result = adfuller(data)
                        
                        st.metric("ADF Statistic", f"{adf_result[0]:.4f}")
                        st.metric("p-value", f"{adf_result[1]:.6f}")
                        
                        st.code(f"""
Critical Values:
  1%: {adf_result[4]['1%']:.4f}
  5%: {adf_result[4]['5%']:.4f}
  10%: {adf_result[4]['10%']:.4f}
                        """)
                        
                        if adf_result[1] < 0.05:
                            st.success("✅ Stationary at 5% level")
                        else:
                            st.error("❌ Non-Stationary at 5% level")
                    
                    with col2:
                        # Descriptive stats
                        st.markdown("**Descriptive Statistics:**")
                        
                        st.metric("Mean", f"{np.mean(data):.4f}")
                        st.metric("Std Dev", f"{np.std(data):.4f}")
                        st.metric("Min", f"{np.min(data):.4f}")
                        st.metric("Max", f"{np.max(data):.4f}")
                        
                        st.info("""
                        **Interpretation:**
                        - If p-value < 0.05: Reject null (series is stationary)
                        - If p-value ≥ 0.05: Fail to reject (series has unit root)
                        - Consider differencing if non-stationary
                        """)
                    
            except Exception as e:
                st.error(f"Error: {e}")
    
    elif calc_type == "Forecast Evaluation":
        st.subheader("Forecast Evaluation Metrics")
        
        st.markdown("**Enter actual and predicted values:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            actual = st.text_area("Actual values:", height=100)
        
        with col2:
            predicted = st.text_area("Predicted values:", height=100)
        
        if st.button("Calculate Metrics"):
            try:
                y_true = np.array([float(x.strip()) for x in actual.split(',')])
                y_pred = np.array([float(x.strip()) for x in predicted.split(',')])
                
                if len(y_true) != len(y_pred):
                    st.error("Actual and predicted must have same length")
                else:
                    # Calculate metrics
                    mae = np.mean(np.abs(y_true - y_pred))
                    mse = np.mean((y_true - y_pred)**2)
                    rmse = np.sqrt(mse)
                    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric("MAE", f"{mae:.4f}")
                    with col2:
                        st.metric("MSE", f"{mse:.4f}")
                    with col3:
                        st.metric("RMSE", f"{rmse:.4f}")
                    with col4:
                        st.metric("MAPE", f"{mape:.2f}%")
                    
                    # Plot
                    fig = go.Figure()
                    
                    fig.add_trace(go.Scatter(
                        y=y_true,
                        mode='lines+markers',
                        name='Actual',
                        line=dict(color='#4dd0e1', width=2)
                    ))
                    
                    fig.add_trace(go.Scatter(
                        y=y_pred,
                        mode='lines+markers',
                        name='Predicted',
                        line=dict(color='#ffa726', width=2, dash='dash')
                    ))
                    
                    fig.update_layout(
                        title="Actual vs Predicted",
                        xaxis_title="Time",
                        yaxis_title="Value",
                        template="plotly_dark",
                        height=400
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    st.info("""
                    **Metric Interpretation:**
                    - **MAE:** Average absolute error (same units as data)
                    - **RMSE:** Root mean squared error (penalizes large errors)
                    - **MAPE:** Mean absolute percentage error (scale-independent)
                    - Lower values indicate better forecast accuracy
                    """)
                    
            except Exception as e:
                st.error(f"Error: {e}")

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 5 Quiz: Time Series Analysis")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'A stationary time series has:',
            'options': [
                'Constant mean and variance over time',
                'Increasing trend',
                'Seasonal patterns',
                'Random walk behavior'
            ],
            'correct': 'Constant mean and variance over time',
            'explanation': 'Stationarity requires constant statistical properties (mean, variance, autocorrelation) over time.'
        },
        {
            'id': 2,
            'question': 'The ADF test null hypothesis is:',
            'options': [
                'Series is stationary',
                'Series has unit root (non-stationary)',
                'Series has no autocorrelation',
                'Series is normally distributed'
            ],
            'correct': 'Series has unit root (non-stationary)',
            'explanation': 'ADF test H₀ is that series has unit root. Small p-value means reject H₀ (series is stationary).'
        },
        {
            'id': 3,
            'question': 'In an AR(1) model, the PACF:',
            'options': [
                'Decays gradually',
                'Cuts off after lag 1',
                'Is always zero',
                'Shows seasonal pattern'
            ],
            'correct': 'Cuts off after lag 1',
            'explanation': 'For AR(p), PACF shows significant spike at lag p and cuts off after that.'
        },
        {
            'id': 4,
            'question': 'ARIMA(1,1,1) means:',
            'options': [
                '1 AR term, 1 difference, 1 MA term',
                '1 trend, 1 seasonal, 1 error',
                '1 lag, 1 forecast, 1 confidence level',
                '1 year of data, 1 model, 1 prediction'
            ],
            'correct': '1 AR term, 1 difference, 1 MA term',
            'explanation': 'ARIMA(p,d,q): p=AR order, d=degree of differencing, q=MA order.'
        },
        {
            'id': 5,
            'question': 'GARCH models are used for:',
            'options': [
                'Forecasting mean returns',
                'Modeling time-varying volatility',
                'Seasonal adjustment',
                'Trend estimation'
            ],
            'correct': 'Modeling time-varying volatility',
            'explanation': 'GARCH models capture volatility clustering and time-varying variance in financial data.'
        },
        {
            'id': 6,
            'question': 'Differencing is used to:',
            'options': [
                'Remove seasonality',
                'Remove trend and achieve stationarity',
                'Increase sample size',
                'Improve forecast accuracy'
            ],
            'correct': 'Remove trend and achieve stationarity',
            'explanation': 'Differencing (Yₜ - Yₜ₋₁) removes trends and helps achieve stationarity.'
        },
        {
            'id': 7,
            'question': 'ACF measures:',
            'options': [
                'Direct correlation only',
                'Total correlation including indirect effects',
                'Causation between variables',
                'Forecast error'
            ],
            'correct': 'Total correlation including indirect effects',
            'explanation': 'ACF shows total correlation between Yₜ and Yₜ₋ₖ, including indirect effects through intermediate lags.'
        },
        {
            'id': 8,
            'question': 'In GARCH(1,1), if α + β ≈ 1:',
            'options': [
                'Model is invalid',
                'High persistence in volatility',
                'No volatility clustering',
                'Perfect forecast accuracy'
            ],
            'correct': 'High persistence in volatility',
            'explanation': 'α + β close to 1 indicates high persistence - shocks to volatility decay very slowly.'
        },
        {
            'id': 9,
            'question': 'The random walk hypothesis suggests:',
            'options': [
                'Stock prices are perfectly predictable',
                'Stock price changes are unpredictable',
                'Stocks always trend upward',
                'Volatility is constant'
            ],
            'correct': 'Stock price changes are unpredictable',
            'explanation': 'Random walk means past prices don\'t help predict future changes - market is efficient.'
        },
        {
            'id': 10,
            'question': 'MAPE is preferred over MSE when:',
            'options': [
                'Data has outliers',
                'Comparing forecasts across different scales',
                'Sample size is small',
                'Series is non-stationary'
            ],
            'correct': 'Comparing forecasts across different scales',
            'explanation': 'MAPE is scale-independent (percentage), making it useful for comparing forecasts of different magnitude series.'
        }
    ]
    
    for q in questions:
        st.subheader(f"Question {q['id']}")
        st.markdown(f"**{q['question']}**")
        
        answer = st.radio(
            f"Select answer:",
            q['options'],
            key=f"q{q['id']}",
            disabled=st.session_state.quiz_submitted
        )
        
        st.session_state.quiz_answers[q['id']] = answer
        
        if st.session_state.quiz_submitted:
            if answer == q['correct']:
                st.success(f"✅ Correct! {q['explanation']}")
            else:
                st.error(f"❌ Incorrect. Answer: **{q['correct']}**")
                st.info(q['explanation'])
        
        st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if not st.session_state.quiz_submitted:
            if st.button("Submit Quiz", type="primary"):
                st.session_state.quiz_submitted = True
                st.rerun()
    
    with col2:
        if st.session_state.quiz_submitted:
            if st.button("Retake Quiz"):
                st.session_state.quiz_submitted = False
                st.session_state.quiz_answers = {}
                st.rerun()
    
    if st.session_state.quiz_submitted:
        correct = sum(1 for q in questions 
                     if st.session_state.quiz_answers.get(q['id']) == q['correct'])
        percentage = (correct / len(questions)) * 100
        
        st.markdown("---")
        st.subheader("📊 Results")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Score", f"{correct}/{len(questions)}")
        with col2:
            st.metric("Percentage", f"{percentage:.0f}%")
        with col3:
            grade = "🌟 Excellent" if percentage >= 80 else "👍 Good" if percentage >= 60 else "📚 Review"
            st.metric("Grade", grade)

# ======================
# SUMMARY PAGE
# ======================
elif page == "📋 Summary":
    st.header("Module 5 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Stationarity**
        - Constant mean & variance
        - ADF/KPSS tests
        - Differencing to achieve it
        - Required for many models
        """)
        
        st.success("""
        **ARIMA Models**
        - AR: Past values
        - MA: Past errors
        - I: Differencing
        - ACF/PACF for selection
        """)
    
    with col2:
        st.warning("""
        **Volatility Models**
        - ARCH: Volatility clustering
        - GARCH: Persistence
        - Used in risk management
        - VaR estimation
        """)
        
        st.info("""
        **Forecasting**
        - Point & interval forecasts
        - Evaluation metrics
        - Out-of-sample testing
        - Uncertainty quantification
        """)
    
    st.markdown("---")
    st.subheader("📐 Essential Models")
    
    models_df = pd.DataFrame({
        'Model': ['AR(p)', 'MA(q)', 'ARIMA(p,d,q)', 'GARCH(1,1)'],
        'Equation': [
            'Yₜ = φ₁Yₜ₋₁ + ... + φₚYₜ₋ₚ + εₜ',
            'Yₜ = εₜ + θ₁εₜ₋₁ + ... + θqεₜ₋q',
            'Combines AR, differencing, MA',
            'σₜ² = ω + αεₜ₋₁² + βσₜ₋₁²'
        ],
        'Use': [
            'Persistence in levels',
            'Temporary shocks',
            'Non-stationary series',
            'Time-varying volatility'
        ]
    })
    st.table(models_df)
    
    st.markdown("---")
    st.subheader("💼 Financial Applications")
    
    tab1, tab2, tab3 = st.tabs(["Returns", "Volatility", "Risk Management"])
    
    with tab1:
        st.markdown("""
        **Forecasting Returns:**
        
        **Challenges:**
        - Weak autocorrelation
        - Near random walk
        - Low R-squared
        
        **Approaches:**
        - Short-term ARIMA
        - Factor models
        - ML methods
        - Focus on direction not magnitude
        """)
    
    with tab2:
        st.markdown("""
        **Volatility Forecasting:**
        
        **Success factors:**
        - Strong persistence
        - Volatility clusters
        - GARCH works well
        
        **Applications:**
        - Option pricing
        - VaR calculation
        - Risk budgeting
        - Portfolio allocation
        """)
    
    with tab3:
        st.markdown("""
        **Risk Management:**
        
        **Time Series Role:**
        - Dynamic VaR models
        - Stress testing
        - Scenario analysis
        - Backtesting
        
        **Key Tools:**
        - GARCH for volatility
        - Historical simulation
        - Monte Carlo
        - Extreme value theory
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 6?**
    
    Module 6: Portfolio Statistics covers:
    - Return and risk measures
    - Portfolio optimization
    - Diversification benefits
    - Performance evaluation
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #b2ebf2; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 5 of 12: Time Series Analysis</p>
</div>
""", unsafe_allow_html=True)