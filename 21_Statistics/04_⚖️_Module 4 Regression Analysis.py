import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #2d1b3d 0%, #3d2b4d 50%, #4d3b5d 100%);
    }
    h1 {
        color: #ff6b9d;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #ffa8c5;
        border-left: 6px solid #ff6b9d;
        padding-left: 15px;
    }
    h3 {
        color: #ffc4d6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>📈 Module 4: Regression Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffc4d6;'>Modeling Relationships in Finance</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 4 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("4.1 Simple Linear Regression")
    
    st.subheader("The Regression Model")
    
    st.latex(r"Y = \beta_0 + \beta_1 X + \epsilon")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Components:**
        - **Y:** Dependent variable (response)
        - **X:** Independent variable (predictor)
        - **β₀:** Intercept (Y when X = 0)
        - **β₁:** Slope (change in Y per unit X)
        - **ε:** Error term (residual)
        
        **Example:** 
        Stock Return = β₀ + β₁ × Market Return + ε
        """)
    
    with col2:
        st.success("""
        **Ordinary Least Squares (OLS):**
        
        Minimizes the sum of squared residuals:
        """)
        st.latex(r"\min \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2")
        
        st.markdown("""
        **Estimates:**
        """)
        st.latex(r"\hat{\beta}_1 = \frac{\sum(X_i - \bar{X})(Y_i - \bar{Y})}{\sum(X_i - \bar{X})^2}")
        st.latex(r"\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1\bar{X}")
    
    st.markdown("---")
    
    # Interpretation
    st.subheader("Interpreting Regression Coefficients")
    
    with st.expander("**Slope (β₁)** - Click to expand", expanded=True):
        st.markdown("""
        **Interpretation:** For every 1-unit increase in X, Y changes by β₁ units (on average)
        
        **Financial Examples:**
        - **CAPM Beta:** If β₁ = 1.2, when market returns increase by 1%, stock returns increase by 1.2%
        - **Price Elasticity:** If β₁ = -0.5, a 1% price increase leads to 0.5% decrease in quantity
        - **Advertising ROI:** If β₁ = 2.5, each $1 in advertising generates $2.50 in revenue
        
        **Statistical Significance:**
        - Test H₀: β₁ = 0 (no relationship)
        - If p-value < 0.05, reject H₀ (significant relationship)
        """)
    
    with st.expander("**Intercept (β₀)**"):
        st.markdown("""
        **Interpretation:** Expected value of Y when X = 0
        
        **Caution:** 
        - May not be meaningful if X = 0 is outside the data range
        - In CAPM: α (alpha) represents abnormal returns when market return = 0
        
        **Financial Significance:**
        - Positive α: Outperforming the market
        - Negative α: Underperforming the market
        - α = 0: Fair pricing (no abnormal returns)
        """)
    
    st.markdown("---")
    
    # R-squared
    st.subheader("Goodness of Fit: R-squared")
    
    st.latex(r"R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum(Y_i - \hat{Y}_i)^2}{\sum(Y_i - \bar{Y})^2}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **R² Interpretation:**
        - Proportion of variance in Y explained by X
        - Range: 0 to 1 (0% to 100%)
        - R² = 0.75 means X explains 75% of variation in Y
        
        **Rule of Thumb:**
        - R² > 0.7: Strong relationship
        - 0.3 < R² < 0.7: Moderate relationship
        - R² < 0.3: Weak relationship
        """)
    
    with col2:
        st.warning("""
        **Limitations of R²:**
        - High R² doesn't mean causation
        - Low R² doesn't mean model is useless
        - Adding variables always increases R²
        - Use Adjusted R² for multiple regression
        
        **Adjusted R²:**
        """)
        st.latex(r"\bar{R}^2 = 1 - \frac{(1-R^2)(n-1)}{n-k-1}")
        st.markdown("""
        Penalizes for adding unnecessary variables
        """)
    
    st.markdown("---")
    
    # Assumptions
    st.subheader("OLS Assumptions")
    
    st.markdown("""
    For valid inference, OLS requires:
    """)
    
    assumptions = pd.DataFrame({
        'Assumption': [
            '1. Linearity',
            '2. Independence',
            '3. Homoscedasticity',
            '4. Normality',
            '5. No multicollinearity'
        ],
        'Description': [
            'Relationship between X and Y is linear',
            'Observations are independent',
            'Constant variance of errors',
            'Errors are normally distributed',
            'Predictors are not highly correlated (multiple regression)'
        ],
        'Test/Check': [
            'Residual plot',
            'Durbin-Watson test',
            'Breusch-Pagan test',
            'Q-Q plot, Shapiro-Wilk',
            'VIF (Variance Inflation Factor)'
        ]
    })
    
    st.table(assumptions)
    
    st.markdown("---")
    
    # Multiple Regression
    st.header("4.2 Multiple Linear Regression")
    
    st.latex(r"Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k + \epsilon")
    
    st.info("""
    **Multiple Regression:**
    - Model Y using multiple predictors
    - Each β represents partial effect (holding other variables constant)
    - More realistic for financial modeling
    
    **Example - Stock Returns:**
    """)
    
    st.latex(r"R_{stock} = \alpha + \beta_{market} R_{market} + \beta_{size} SMB + \beta_{value} HML + \epsilon")
    
    st.markdown("""
    **Fama-French 3-Factor Model:**
    - Market factor (systematic risk)
    - Size factor (small vs large cap)
    - Value factor (value vs growth)
    """)
    
    st.markdown("---")
    
    # Model Selection
    st.subheader("Model Selection Criteria")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**AIC (Akaike Information Criterion):**")
        st.latex(r"AIC = 2k - 2\ln(\hat{L})")
        st.markdown("""
        - Lower is better
        - Penalizes model complexity
        - k = number of parameters
        """)
    
    with col2:
        st.markdown("**BIC (Bayesian Information Criterion):**")
        st.latex(r"BIC = k\ln(n) - 2\ln(\hat{L})")
        st.markdown("""
        - Lower is better
        - Stronger penalty for complexity
        - Prefers simpler models than AIC
        """)
    
    st.markdown("---")
    
    # Diagnostics
    st.header("4.3 Regression Diagnostics")
    
    st.subheader("Residual Analysis")
    
    st.warning("""
    **Residuals = Actual - Predicted**
    
    **What to check:**
    1. **Pattern in residuals:** Should be random
    2. **Heteroscedasticity:** Constant variance
    3. **Outliers:** Unusual observations
    4. **Normality:** Q-Q plot
    
    **Key Plots:**
    - Residuals vs Fitted values
    - Q-Q plot
    - Scale-Location plot
    - Residuals vs Leverage
    """)
    
    st.markdown("---")
    
    # Multicollinearity
    st.subheader("Multicollinearity Detection")
    
    st.markdown("**VIF (Variance Inflation Factor):**")
    st.latex(r"VIF_j = \frac{1}{1 - R_j^2}")
    
    st.info("""
    **Interpretation:**
    - VIF = 1: No correlation
    - VIF < 5: Acceptable
    - VIF > 5: Moderate multicollinearity
    - VIF > 10: Severe multicollinearity (problem!)
    
    **Solution:**
    - Remove highly correlated variables
    - Use PCA (Principal Component Analysis)
    - Ridge regression (regularization)
    """)
    
    st.markdown("---")
    
    # Financial Applications
    st.header("Financial Applications")
    
    tabs = st.tabs(["CAPM", "Factor Models", "Forecasting"])
    
    with tabs[0]:
        st.subheader("Capital Asset Pricing Model (CAPM)")
        
        st.latex(r"R_i - R_f = \alpha + \beta(R_m - R_f) + \epsilon")
        
        st.markdown("""
        **Where:**
        - Rᵢ = Stock return
        - Rf = Risk-free rate
        - Rm = Market return
        - α (alpha) = Abnormal return
        - β (beta) = Systematic risk
        
        **Beta Interpretation:**
        - β = 1: Moves with market
        - β > 1: More volatile than market (aggressive)
        - β < 1: Less volatile than market (defensive)
        - β < 0: Moves opposite to market (rare)
        
        **Alpha Interpretation:**
        - α > 0: Positive abnormal returns (skill)
        - α = 0: Fairly priced
        - α < 0: Negative abnormal returns
        """)
    
    with tabs[1]:
        st.subheader("Multi-Factor Models")
        
        st.markdown("""
        **Fama-French 3-Factor:**
        """)
        st.latex(r"R_i - R_f = \alpha + \beta_M(R_m - R_f) + \beta_S SMB + \beta_V HML + \epsilon")
        
        st.markdown("""
        **Factors:**
        - **Market (Rm - Rf):** Market excess return
        - **SMB (Small Minus Big):** Size premium
        - **HML (High Minus Low):** Value premium
        
        **Extensions:**
        - **5-Factor:** + Profitability + Investment
        - **Momentum:** Past performance factor
        - **Quality:** Earnings quality factor
        """)
    
    with tabs[2]:
        st.subheader("Financial Forecasting")
        
        st.markdown("""
        **Applications:**
        
        1. **Revenue Forecasting:**
           - Revenue = f(GDP, inflation, seasonality)
        
        2. **Credit Scoring:**
           - Default = f(income, debt ratio, credit history)
        
        3. **Option Pricing:**
           - Option price = f(stock price, volatility, time)
        
        4. **Risk Management:**
           - Portfolio risk = f(market factors, exposures)
        
        **Key Considerations:**
        - Out-of-sample validation
        - Structural breaks
        - Non-stationarity in time series
        - Overfitting risk
        """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Real-World Examples")
    
    # Example 1: Simple Linear Regression
    st.subheader("Example 1: CAPM Beta Estimation")
    
    st.markdown("""
    **Scenario:** Estimate the beta of a stock using monthly returns.
    
    **Data:** 36 months of returns
    """)
    
    # Generate sample data
    np.random.seed(42)
    market_returns = np.random.normal(0.8, 3, 36)
    stock_returns = 0.3 + 1.2 * market_returns + np.random.normal(0, 2, 36)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Perform regression
        X = market_returns.reshape(-1, 1)
        y = stock_returns
        
        model = LinearRegression()
        model.fit(X, y)
        
        beta = model.coef_[0]
        alpha = model.intercept_
        y_pred = model.predict(X)
        
        r2 = r2_score(y, y_pred)
        mse = mean_squared_error(y, y_pred)
        rmse = np.sqrt(mse)
        
        # Calculate standard errors
        n = len(y)
        residuals = y - y_pred
        se_residual = np.sqrt(np.sum(residuals**2) / (n - 2))
        se_beta = se_residual / np.sqrt(np.sum((X.flatten() - X.mean())**2))
        
        # t-statistic for beta
        t_stat_beta = beta / se_beta
        p_value_beta = 2 * (1 - stats.t.cdf(abs(t_stat_beta), n - 2))
        
        st.markdown("**Regression Results:**")
        
        st.metric("Alpha (α)", f"{alpha:.4f}")
        st.metric("Beta (β)", f"{beta:.4f}")
        st.metric("R-squared", f"{r2:.4f}")
        st.metric("RMSE", f"{rmse:.4f}")
        
        st.markdown("**Statistical Significance:**")
        st.metric("t-statistic (β)", f"{t_stat_beta:.3f}")
        st.metric("p-value (β)", f"{p_value_beta:.4f}")
        
        if p_value_beta < 0.05:
            st.success("✅ Beta is statistically significant (p < 0.05)")
        else:
            st.warning("⚠️ Beta is not statistically significant")
        
        st.markdown(f"""
        **Interpretation:**
        - Alpha = {alpha:.4f}%: Monthly abnormal return
        - Beta = {beta:.4f}: Stock is {'more' if beta > 1 else 'less'} volatile than market
        - R² = {r2:.2%}: Market explains {r2:.1%} of stock variance
        """)
    
    with col2:
        # Scatter plot with regression line
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=market_returns,
            y=stock_returns,
            mode='markers',
            name='Actual Returns',
            marker=dict(size=8, color='#ff6b9d', opacity=0.6)
        ))
        
        # Regression line
        x_line = np.linspace(market_returns.min(), market_returns.max(), 100)
        y_line = alpha + beta * x_line
        
        fig.add_trace(go.Scatter(
            x=x_line,
            y=y_line,
            mode='lines',
            name=f'Regression Line (β={beta:.3f})',
            line=dict(color='yellow', width=3)
        ))
        
        fig.update_layout(
            title="CAPM Regression: Stock vs Market Returns",
            xaxis_title="Market Return (%)",
            yaxis_title="Stock Return (%)",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Residual plot
        fig2 = go.Figure()
        
        fig2.add_trace(go.Scatter(
            x=y_pred,
            y=residuals,
            mode='markers',
            marker=dict(size=8, color='#ff6b9d', opacity=0.6)
        ))
        
        fig2.add_hline(y=0, line_dash="dash", line_color="yellow")
        
        fig2.update_layout(
            title="Residual Plot",
            xaxis_title="Fitted Values",
            yaxis_title="Residuals",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Example 2: Multiple Regression
    st.subheader("Example 2: Multiple Regression - Sales Forecasting")
    
    st.markdown("""
    **Scenario:** Forecast monthly sales using multiple predictors.
    
    **Variables:**
    - Y: Sales (in thousands)
    - X₁: Advertising spend (in thousands)
    - X₂: Number of promotions
    - X₃: Month (seasonality)
    """)
    
    # Generate sample data
    np.random.seed(123)
    n_obs = 50
    advertising = np.random.uniform(5, 50, n_obs)
    promotions = np.random.randint(0, 5, n_obs)
    month = np.random.randint(1, 13, n_obs)
    
    # True model: Sales = 20 + 2*ad + 5*promo + 0.5*month + noise
    sales = 20 + 2*advertising + 5*promotions + 0.5*month + np.random.normal(0, 5, n_obs)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Sales': sales,
        'Advertising': advertising,
        'Promotions': promotions,
        'Month': month
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Multiple regression
        X_multi = df[['Advertising', 'Promotions', 'Month']].values
        y_multi = df['Sales'].values
        
        model_multi = LinearRegression()
        model_multi.fit(X_multi, y_multi)
        
        y_pred_multi = model_multi.predict(X_multi)
        
        r2_multi = r2_score(y_multi, y_pred_multi)
        adj_r2 = 1 - (1 - r2_multi) * (n_obs - 1) / (n_obs - X_multi.shape[1] - 1)
        
        st.markdown("**Regression Equation:**")
        st.latex(f"Sales = {model_multi.intercept_:.2f} + {model_multi.coef_[0]:.2f} \\times Ad + {model_multi.coef_[1]:.2f} \\times Promo + {model_multi.coef_[2]:.2f} \\times Month")
        
        st.markdown("**Coefficients:**")
        coef_df = pd.DataFrame({
            'Variable': ['Intercept', 'Advertising', 'Promotions', 'Month'],
            'Coefficient': [model_multi.intercept_] + list(model_multi.coef_),
            'Interpretation': [
                'Base sales',
                'Per $1k advertising',
                'Per promotion',
                'Per month'
            ]
        })
        st.table(coef_df)
        
        st.metric("R-squared", f"{r2_multi:.4f}")
        st.metric("Adjusted R-squared", f"{adj_r2:.4f}")
        
        st.success(f"""
        **Model explains {r2_multi:.1%} of sales variation**
        
        **Key Insights:**
        - Each $1k in advertising → ${model_multi.coef_[0]:.2f}k sales increase
        - Each promotion → ${model_multi.coef_[1]:.2f}k sales increase
        - Seasonal effect: ${model_multi.coef_[2]:.2f}k per month
        """)
    
    with col2:
        # Actual vs Predicted
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=y_multi,
            y=y_pred_multi,
            mode='markers',
            name='Predictions',
            marker=dict(size=8, color='#ff6b9d', opacity=0.6)
        ))
        
        # 45-degree line
        min_val = min(y_multi.min(), y_pred_multi.min())
        max_val = max(y_multi.max(), y_pred_multi.max())
        
        fig.add_trace(go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            name='Perfect Prediction',
            line=dict(color='yellow', dash='dash', width=2)
        ))
        
        fig.update_layout(
            title="Actual vs Predicted Sales",
            xaxis_title="Actual Sales ($k)",
            yaxis_title="Predicted Sales ($k)",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'Feature': ['Advertising', 'Promotions', 'Month'],
            'Coefficient': model_multi.coef_
        }).sort_values('Coefficient', ascending=True)
        
        fig2 = px.bar(feature_importance, x='Coefficient', y='Feature', 
                     orientation='h',
                     title='Feature Importance',
                     color='Coefficient',
                     color_continuous_scale=['red', 'yellow', 'green'])
        fig2.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(fig2, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Regression Analysis")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["Simple Linear Regression", "Multiple Regression Explorer", 
         "Residual Analysis", "Beta Calculator"]
    )
    
    if exercise == "Simple Linear Regression":
        st.subheader("📊 Simple Linear Regression Explorer")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Generate Data:**")
            
            n_points = st.slider("Number of points:", 20, 200, 50)
            true_slope = st.slider("True slope (β₁):", -3.0, 3.0, 1.0, 0.1)
            true_intercept = st.slider("True intercept (β₀):", -10.0, 10.0, 0.0, 0.5)
            noise_level = st.slider("Noise level:", 0.1, 5.0, 1.0, 0.1)
            
            # Generate data
            np.random.seed(42)
            X_sim = np.random.uniform(0, 10, n_points)
            y_sim = true_intercept + true_slope * X_sim + np.random.normal(0, noise_level, n_points)
            
            # Fit regression
            X_reshape = X_sim.reshape(-1, 1)
            model_sim = LinearRegression()
            model_sim.fit(X_reshape, y_sim)
            
            y_pred_sim = model_sim.predict(X_reshape)
            r2_sim = r2_score(y_sim, y_pred_sim)
            
            st.markdown("**Estimated Model:**")
            st.metric("Estimated β₀", f"{model_sim.intercept_:.3f}")
            st.metric("Estimated β₁", f"{model_sim.coef_[0]:.3f}")
            st.metric("R-squared", f"{r2_sim:.3f}")
            
            st.markdown("**True Model:**")
            st.write(f"β₀ = {true_intercept}")
            st.write(f"β₁ = {true_slope}")
        
        with col2:
            # Plot
            fig = go.Figure()
            
            # Data points
            fig.add_trace(go.Scatter(
                x=X_sim,
                y=y_sim,
                mode='markers',
                name='Data',
                marker=dict(size=8, color='#ff6b9d', opacity=0.6)
            ))
            
            # True line
            x_line = np.linspace(X_sim.min(), X_sim.max(), 100)
            y_true_line = true_intercept + true_slope * x_line
            
            fig.add_trace(go.Scatter(
                x=x_line,
                y=y_true_line,
                mode='lines',
                name='True Relationship',
                line=dict(color='green', width=2, dash='dash')
            ))
            
            # Fitted line
            y_fitted_line = model_sim.intercept_ + model_sim.coef_[0] * x_line
            
            fig.add_trace(go.Scatter(
                x=x_line,
                y=y_fitted_line,
                mode='lines',
                name='Fitted Line',
                line=dict(color='yellow', width=3)
            ))
            
            fig.update_layout(
                title="Linear Regression Fit",
                xaxis_title="X",
                yaxis_title="Y",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Residuals
            residuals_sim = y_sim - y_pred_sim
            
            fig2 = go.Figure()
            
            fig2.add_trace(go.Scatter(
                x=y_pred_sim,
                y=residuals_sim,
                mode='markers',
                marker=dict(size=8, color='#ff6b9d', opacity=0.6)
            ))
            
            fig2.add_hline(y=0, line_dash="dash", line_color="yellow")
            
            fig2.update_layout(
                title="Residual Plot",
                xaxis_title="Fitted Values",
                yaxis_title="Residuals",
                template="plotly_dark",
                height=300
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    elif exercise == "Multiple Regression Explorer":
        st.subheader("🎯 Multiple Regression Explorer")
        
        st.markdown("**Upload your data or use sample data:**")
        
        use_sample = st.checkbox("Use sample data", value=True)
        
        if use_sample:
            # Generate sample data
            np.random.seed(42)
            n = 100
            X1 = np.random.normal(50, 10, n)
            X2 = np.random.normal(100, 20, n)
            X3 = np.random.normal(5, 2, n)
            
            y = 10 + 2*X1 + 0.5*X2 - 3*X3 + np.random.normal(0, 10, n)
            
            df_multi = pd.DataFrame({
                'Y': y,
                'X1': X1,
                'X2': X2,
                'X3': X3
            })
            
            st.dataframe(df_multi.head(10))
        else:
            uploaded = st.file_uploader("Upload CSV", type=['csv'])
            if uploaded:
                df_multi = pd.read_csv(uploaded)
                st.dataframe(df_multi.head())
            else:
                st.info("Please upload a CSV file")
                df_multi = None
        
        if df_multi is not None:
            # Select variables
            col1, col2 = st.columns(2)
            
            with col1:
                y_col = st.selectbox("Select Y (dependent):", df_multi.columns)
            
            with col2:
                x_cols = st.multiselect("Select X (independent):", 
                                       [col for col in df_multi.columns if col != y_col])
            
            if len(x_cols) > 0 and st.button("Run Regression"):
                X_multi = df_multi[x_cols].values
                y_multi = df_multi[y_col].values
                
                model = LinearRegression()
                model.fit(X_multi, y_multi)
                
                y_pred = model.predict(X_multi)
                r2 = r2_score(y_multi, y_pred)
                n_obs = len(y_multi)
                adj_r2 = 1 - (1 - r2) * (n_obs - 1) / (n_obs - len(x_cols) - 1)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Results:**")
                    
                    st.metric("R-squared", f"{r2:.4f}")
                    st.metric("Adjusted R-squared", f"{adj_r2:.4f}")
                    
                    # Coefficients
                    coef_df = pd.DataFrame({
                        'Variable': ['Intercept'] + x_cols,
                        'Coefficient': [model.intercept_] + list(model.coef_)
                    })
                    st.table(coef_df)
                
                with col2:
                    # Actual vs Predicted
                    fig = go.Figure()
                    
                    fig.add_trace(go.Scatter(
                        x=y_multi,
                        y=y_pred,
                        mode='markers',
                        marker=dict(size=8, color='#ff6b9d', opacity=0.6)
                    ))
                    
                    # 45-degree line
                    min_val = min(y_multi.min(), y_pred.min())
                    max_val = max(y_multi.max(), y_pred.max())
                    
                    fig.add_trace(go.Scatter(
                        x=[min_val, max_val],
                        y=[min_val, max_val],
                        mode='lines',
                        line=dict(color='yellow', dash='dash')
                    ))
                    
                    fig.update_layout(
                        title="Actual vs Predicted",
                        xaxis_title="Actual",
                        yaxis_title="Predicted",
                        template="plotly_dark",
                        height=400
                    )
                    st.plotly_chart(fig, use_container_width=True)
    
    elif exercise == "Residual Analysis":
        st.subheader("🔍 Residual Analysis Tool")
        
        st.markdown("Generate data and analyze residuals:")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            n_points = st.slider("Sample size:", 30, 200, 100)
            
            issue = st.selectbox("Simulate issue:", 
                               ["None", "Heteroscedasticity", "Non-linearity", "Outliers"])
            
            # Generate data
            np.random.seed(42)
            X = np.random.uniform(0, 10, n_points)
            
            if issue == "None":
                y = 2 + 3*X + np.random.normal(0, 2, n_points)
            elif issue == "Heteroscedasticity":
                y = 2 + 3*X + np.random.normal(0, 0.5 + 0.5*X, n_points)
            elif issue == "Non-linearity":
                y = 2 + 3*X + 0.5*X**2 + np.random.normal(0, 2, n_points)
            else:  # Outliers
                y = 2 + 3*X + np.random.normal(0, 2, n_points)
                outlier_idx = np.random.choice(n_points, 5, replace=False)
                y[outlier_idx] += np.random.choice([-15, 15], 5)
            
            # Fit model
            model = LinearRegression()
            model.fit(X.reshape(-1, 1), y)
            y_pred = model.predict(X.reshape(-1, 1))
            residuals = y - y_pred
            
            st.metric("Issue Type", issue)
            st.metric("R-squared", f"{r2_score(y, y_pred):.3f}")
        
        with col2:
            # Residual plots
            fig = go.Figure()
            
            # Residuals vs Fitted
            fig.add_trace(go.Scatter(
                x=y_pred,
                y=residuals,
                mode='markers',
                marker=dict(size=8, color='#ff6b9d', opacity=0.6),
                name='Residuals'
            ))
            
            fig.add_hline(y=0, line_dash="dash", line_color="yellow")
            
            fig.update_layout(
                title="Residuals vs Fitted Values",
                xaxis_title="Fitted Values",
                yaxis_title="Residuals",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Q-Q plot
            from scipy.stats import probplot
            
            theoretical_quantiles = probplot(residuals, dist="norm")[0][0]
            sample_quantiles = probplot(residuals, dist="norm")[0][1]
            
            fig2 = go.Figure()
            
            fig2.add_trace(go.Scatter(
                x=theoretical_quantiles,
                y=sample_quantiles,
                mode='markers',
                marker=dict(size=8, color='#ff6b9d', opacity=0.6)
            ))
            
            # 45-degree line
            min_q = min(theoretical_quantiles.min(), sample_quantiles.min())
            max_q = max(theoretical_quantiles.max(), sample_quantiles.max())
            
            fig2.add_trace(go.Scatter(
                x=[min_q, max_q],
                y=[min_q, max_q],
                mode='lines',
                line=dict(color='yellow', dash='dash')
            ))
            
            fig2.update_layout(
                title="Q-Q Plot (Normality Check)",
                xaxis_title="Theoretical Quantiles",
                yaxis_title="Sample Quantiles",
                template="plotly_dark",
                height=300
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    elif exercise == "Beta Calculator":
        st.subheader("📊 CAPM Beta Calculator")
        
        st.markdown("""
        Calculate the beta of a stock relative to the market.
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**Enter Returns (comma-separated):**")
            
            stock_input = st.text_area("Stock Returns (%):", 
                                      value="2.5, -1.2, 3.1, 0.8, -0.5, 2.0, 1.5",
                                      height=100)
            
            market_input = st.text_area("Market Returns (%):",
                                       value="1.8, -0.8, 2.5, 1.0, -0.2, 1.5, 1.2",
                                       height=100)
            
            if st.button("Calculate Beta"):
                try:
                    stock_ret = np.array([float(x.strip()) for x in stock_input.split(',')])
                    market_ret = np.array([float(x.strip()) for x in market_input.split(',')])
                    
                    if len(stock_ret) != len(market_ret):
                        st.error("Stock and market returns must have same length")
                    else:
                        # Regression
                        X_beta = market_ret.reshape(-1, 1)
                        y_beta = stock_ret
                        
                        model_beta = LinearRegression()
                        model_beta.fit(X_beta, y_beta)
                        
                        beta = model_beta.coef_[0]
                        alpha = model_beta.intercept_
                        r2_beta = r2_score(y_beta, model_beta.predict(X_beta))
                        
                        st.session_state['beta_results'] = {
                            'stock': stock_ret,
                            'market': market_ret,
                            'beta': beta,
                            'alpha': alpha,
                            'r2': r2_beta
                        }
                        
                except Exception as e:
                    st.error(f"Error: {e}")
        
        with col2:
            if 'beta_results' in st.session_state:
                results = st.session_state['beta_results']
                
                st.markdown("**Results:**")
                st.metric("Alpha (α)", f"{results['alpha']:.4f}%")
                st.metric("Beta (β)", f"{results['beta']:.4f}")
                st.metric("R-squared", f"{results['r2']:.4f}")
                
                # Interpretation
                if results['beta'] > 1:
                    risk_type = "More volatile (aggressive)"
                elif results['beta'] < 1:
                    risk_type = "Less volatile (defensive)"
                else:
                    risk_type = "Similar volatility to market"
                
                st.info(f"""
                **Interpretation:**
                - Beta = {results['beta']:.3f}
                - {risk_type}
                - When market moves 1%, stock moves {results['beta']:.2f}%
                """)
                
                # Plot
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=results['market'],
                    y=results['stock'],
                    mode='markers',
                    marker=dict(size=10, color='#ff6b9d')
                ))
                
                # Regression line
                x_line = np.linspace(results['market'].min(), results['market'].max(), 100)
                y_line = results['alpha'] + results['beta'] * x_line
                
                fig.add_trace(go.Scatter(
                    x=x_line,
                    y=y_line,
                    mode='lines',
                    line=dict(color='yellow', width=3),
                    name=f'β = {results["beta"]:.3f}'
                ))
                
                fig.update_layout(
                    title="CAPM: Stock vs Market Returns",
                    xaxis_title="Market Return (%)",
                    yaxis_title="Stock Return (%)",
                    template="plotly_dark",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Regression Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["Simple Linear Regression", "Multiple Regression", "Beta Calculator", 
         "R-squared Calculator"]
    )
    
    if calc_type == "Simple Linear Regression":
        st.subheader("Simple Linear Regression Calculator")
        
        st.markdown("**Enter Data:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            x_data = st.text_area("X values (comma-separated):",
                                 placeholder="1, 2, 3, 4, 5",
                                 height=100)
        
        with col2:
            y_data = st.text_area("Y values (comma-separated):",
                                 placeholder="2, 4, 5, 4, 5",
                                 height=100)
        
        if st.button("Calculate Regression"):
            try:
                X = np.array([float(x.strip()) for x in x_data.split(',')])
                y = np.array([float(x.strip()) for x in y_data.split(',')])
                
                if len(X) != len(y):
                    st.error("X and Y must have the same length")
                elif len(X) < 3:
                    st.error("Need at least 3 data points")
                else:
                    # Fit model
                    model = LinearRegression()
                    model.fit(X.reshape(-1, 1), y)
                    
                    y_pred = model.predict(X.reshape(-1, 1))
                    
                    beta_1 = model.coef_[0]
                    beta_0 = model.intercept_
                    r2 = r2_score(y, y_pred)
                    
                    # Standard errors
                    n = len(y)
                    residuals = y - y_pred
                    se_residual = np.sqrt(np.sum(residuals**2) / (n - 2))
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Results:**")
                        
                        st.latex(f"Y = {beta_0:.4f} + {beta_1:.4f}X")
                        
                        st.metric("Intercept (β₀)", f"{beta_0:.4f}")
                        st.metric("Slope (β₁)", f"{beta_1:.4f}")
                        st.metric("R-squared", f"{r2:.4f}")
                        st.metric("Residual Std Error", f"{se_residual:.4f}")
                    
                    with col2:
                        # Plot
                        fig = go.Figure()
                        
                        fig.add_trace(go.Scatter(
                            x=X, y=y,
                            mode='markers',
                            name='Data',
                            marker=dict(size=10, color='#ff6b9d')
                        ))
                        
                        x_line = np.linspace(X.min(), X.max(), 100)
                        y_line = beta_0 + beta_1 * x_line
                        
                        fig.add_trace(go.Scatter(
                            x=x_line, y=y_line,
                            mode='lines',
                            name='Regression Line',
                            line=dict(color='yellow', width=3)
                        ))
                        
                        fig.update_layout(
                            title="Regression Line",
                            xaxis_title="X",
                            yaxis_title="Y",
                            template="plotly_dark",
                            height=400
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    # Interpretation
                    st.success(f"""
                    **Interpretation:**
                    - For every 1-unit increase in X, Y increases by {beta_1:.4f} units
                    - When X = 0, Y = {beta_0:.4f}
                    - Model explains {r2:.1%} of variance in Y
                    """)
                    
            except Exception as e:
                st.error(f"Error: {e}")
    
    elif calc_type == "Beta Calculator":
        st.subheader("CAPM Beta Calculator")
        
        st.markdown("""
        Calculate beta (systematic risk) for CAPM.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            stock_returns = st.text_area("Stock Returns (%):",
                                        placeholder="2.5, -1.0, 3.2, ...",
                                        height=150)
            
            market_returns = st.text_area("Market Returns (%):",
                                         placeholder="1.8, -0.5, 2.5, ...",
                                         height=150)
            
            risk_free = st.number_input("Risk-Free Rate (%):", value=0.5)
        
        with col2:
            if st.button("Calculate Beta"):
                try:
                    stock_ret = np.array([float(x.strip()) for x in stock_returns.split(',')])
                    market_ret = np.array([float(x.strip()) for x in market_returns.split(',')])
                    
                    # Excess returns
                    stock_excess = stock_ret - risk_free
                    market_excess = market_ret - risk_free
                    
                    # Regression
                    model = LinearRegression()
                    model.fit(market_excess.reshape(-1, 1), stock_excess)
                    
                    beta = model.coef_[0]
                    alpha = model.intercept_
                    r2 = r2_score(stock_excess, model.predict(market_excess.reshape(-1, 1)))
                    
                    st.markdown("**CAPM Results:**")
                    st.metric("Alpha (α)", f"{alpha:.4f}%")
                    st.metric("Beta (β)", f"{beta:.4f}")
                    st.metric("R-squared", f"{r2:.4f}")
                    
                    # Interpretation
                    if alpha > 0.5:
                        alpha_interp = "Positive abnormal returns (outperforming)"
                    elif alpha < -0.5:
                        alpha_interp = "Negative abnormal returns (underperforming)"
                    else:
                        alpha_interp = "Fairly priced (no abnormal returns)"
                    
                    if beta > 1.2:
                        beta_interp = "High systematic risk (aggressive)"
                    elif beta > 0.8:
                        beta_interp = "Moderate systematic risk"
                    else:
                        beta_interp = "Low systematic risk (defensive)"
                    
                    st.info(f"""
                    **Interpretation:**
                    
                    **Alpha:** {alpha_interp}
                    
                    **Beta:** {beta_interp}
                    - When market excess return = 1%, stock excess return = {beta:.2f}%
                    """)
                    
                except Exception as e:
                    st.error(f"Error: {e}")

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 4 Quiz: Regression Analysis")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'In simple linear regression Y = β₀ + β₁X + ε, what does β₁ represent?',
            'options': [
                'Y-intercept',
                'Change in Y for a 1-unit change in X',
                'Error term',
                'Predicted value of Y'
            ],
            'correct': 'Change in Y for a 1-unit change in X',
            'explanation': 'β₁ (slope) represents the change in Y for each 1-unit increase in X.'
        },
        {
            'id': 2,
            'question': 'R-squared measures:',
            'options': [
                'The correlation between X and Y',
                'The proportion of variance in Y explained by X',
                'The standard error of the regression',
                'The significance of the coefficients'
            ],
            'correct': 'The proportion of variance in Y explained by X',
            'explanation': 'R² tells us what percentage of variation in Y is explained by the model.'
        },
        {
            'id': 3,
            'question': 'In CAPM, a stock with Beta = 1.5 is:',
            'options': [
                'Less volatile than the market',
                'Equally volatile as the market',
                'More volatile than the market',
                'Negatively correlated with the market'
            ],
            'correct': 'More volatile than the market',
            'explanation': 'Beta > 1 means the stock is more volatile than the market (amplifies market movements).'
        },
        {
            'id': 4,
            'question': 'What is the main purpose of residual analysis?',
            'options': [
                'Calculate R-squared',
                'Check regression assumptions',
                'Determine the intercept',
                'Find outliers only'
            ],
            'correct': 'Check regression assumptions',
            'explanation': 'Residual plots help verify assumptions like linearity, homoscedasticity, and normality.'
        },
        {
            'id': 5,
            'question': 'Multicollinearity occurs when:',
            'options': [
                'Y and X are highly correlated',
                'Independent variables are highly correlated with each other',
                'Residuals are correlated',
                'The model has high R-squared'
            ],
            'correct': 'Independent variables are highly correlated with each other',
            'explanation': 'Multicollinearity is correlation among independent variables, making it hard to isolate individual effects.'
        },
        {
            'id': 6,
            'question': 'VIF (Variance Inflation Factor) > 10 indicates:',
            'options': [
                'Good model fit',
                'Severe multicollinearity',
                'Heteroscedasticity',
                'Non-linearity'
            ],
            'correct': 'Severe multicollinearity',
            'explanation': 'VIF > 10 suggests severe multicollinearity that should be addressed.'
        },
        {
            'id': 7,
            'question': 'Adjusted R-squared is preferred over R-squared because it:',
            'options': [
                'Is always higher',
                'Penalizes adding unnecessary variables',
                'Is easier to calculate',
                'Only works for simple regression'
            ],
            'correct': 'Penalizes adding unnecessary variables',
            'explanation': 'Adjusted R² accounts for the number of predictors, preventing overfitting.'
        },
        {
            'id': 8,
            'question': 'In CAPM, alpha (α) represents:',
            'options': [
                'Systematic risk',
                'Market correlation',
                'Abnormal returns not explained by market',
                'Total risk'
            ],
            'correct': 'Abnormal returns not explained by market',
            'explanation': 'Alpha is the excess return above what CAPM predicts - positive alpha suggests outperformance.'
        },
        {
            'id': 9,
            'question': 'Heteroscedasticity means:',
            'options': [
                'Linear relationship',
                'Constant variance of residuals',
                'Non-constant variance of residuals',
                'Normal distribution of residuals'
            ],
            'correct': 'Non-constant variance of residuals',
            'explanation': 'Heteroscedasticity is when residual variance changes across fitted values, violating OLS assumptions.'
        },
        {
            'id': 10,
            'question': 'The Fama-French 3-Factor model includes:',
            'options': [
                'Market, interest rate, inflation',
                'Market, size, value',
                'Market, momentum, volatility',
                'Market, beta, alpha'
            ],
            'correct': 'Market, size, value',
            'explanation': 'Fama-French uses Market (Rm-Rf), Size (SMB), and Value (HML) factors.'
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
    st.header("Module 4 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Simple Linear Regression**
        - Y = β₀ + β₁X + ε
        - β₁: slope (effect of X on Y)
        - β₀: intercept (Y when X=0)
        - OLS minimizes squared residuals
        """)
        
        st.success("""
        **CAPM & Beta**
        - R = α + β(Rm - Rf) + ε
        - Beta: systematic risk
        - Alpha: abnormal returns
        - Used for risk assessment
        """)
    
    with col2:
        st.warning("""
        **Model Evaluation**
        - R²: variance explained
        - Adjusted R²: penalizes complexity
        - Residual analysis: check assumptions
        - VIF: detect multicollinearity
        """)
        
        st.info("""
        **Multiple Regression**
        - Multiple predictors
        - Each β is partial effect
        - Factor models (Fama-French)
        - Model selection (AIC, BIC)
        """)
    
    st.markdown("---")
    st.subheader("📐 Essential Formulas")
    
    formulas_df = pd.DataFrame({
        'Concept': ['Slope', 'Intercept', 'R-squared', 'Adjusted R²', 'Beta', 'VIF'],
        'Formula': [
            'β₁ = Σ(X-X̄)(Y-Ȳ) / Σ(X-X̄)²',
            'β₀ = Ȳ - β₁X̄',
            '1 - SSres/SStot',
            '1 - (1-R²)(n-1)/(n-k-1)',
            'Cov(Rs,Rm) / Var(Rm)',
            '1 / (1 - R²ⱼ)'
        ]
    })
    st.table(formulas_df)
    
    st.markdown("---")
    st.subheader("💼 Financial Applications")
    
    tab1, tab2, tab3 = st.tabs(["CAPM", "Factor Models", "Forecasting"])
    
    with tab1:
        st.markdown("""
        **CAPM Applications:**
        
        1. **Risk Assessment:** Beta measures systematic risk
        2. **Performance:** Alpha shows skill vs luck
        3. **Portfolio:** Expected returns from betas
        4. **Hedging:** Match betas for risk neutrality
        """)
    
    with tab2:
        st.markdown("""
        **Multi-Factor Models:**
        
        1. **Fama-French:** Market + Size + Value
        2. **Carhart:** + Momentum factor
        3. **5-Factor:** + Profitability + Investment
        4. **Custom:** Industry-specific factors
        """)
    
    with tab3:
        st.markdown("""
        **Forecasting Uses:**
        
        1. **Sales:** Revenue = f(advertising, season)
        2. **Credit:** Default = f(income, debt ratio)
        3. **Valuation:** Price = f(earnings, growth)
        4. **Risk:** VaR = f(market factors)
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 5?**
    
    Module 5: Time Series Analysis covers:
    - Stationarity and trends
    - ARIMA models
    - Volatility modeling (GARCH)
    - Forecasting techniques
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #ffc4d6; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 4 of 12: Regression Analysis</p>
</div>
""", unsafe_allow_html=True)