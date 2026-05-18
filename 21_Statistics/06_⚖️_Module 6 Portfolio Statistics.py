import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #43a047 100%);
    }
    h1 {
        color: #81c784;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #a5d6a7;
        border-left: 6px solid #81c784;
        padding-left: 15px;
    }
    h3 {
        color: #c8e6c9;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>💼 Module 6: Portfolio Statistics</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #c8e6c9;'>Modern Portfolio Theory & Risk Management</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 6 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("6.1 Portfolio Return and Risk")
    
    st.subheader("Portfolio Return")
    
    st.latex(r"R_p = \sum_{i=1}^{n} w_i R_i")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Portfolio Return Formula:**
        - Rₚ: Portfolio return
        - wᵢ: Weight of asset i
        - Rᵢ: Return of asset i
        - Σwᵢ = 1 (weights sum to 100%)
        
        **Example:**
        - 60% stocks (R = 10%)
        - 40% bonds (R = 5%)
        - Portfolio return = 0.6×10% + 0.4×5% = 8%
        """)
    
    with col2:
        st.success("""
        **Properties:**
        - Linear combination of returns
        - Weighted average
        - Easy to calculate
        - No diversification effect on expected return
        
        **Key Insight:**
        Expected portfolio return = weighted average of expected asset returns
        
        No "free lunch" from diversification in terms of return!
        """)
    
    st.markdown("---")
    
    # Portfolio Risk
    st.subheader("Portfolio Risk (Standard Deviation)")
    
    st.latex(r"\sigma_p^2 = \sum_{i=1}^{n}\sum_{j=1}^{n} w_i w_j \sigma_i \sigma_j \rho_{ij}")
    
    st.warning("""
    **Simplified for 2 assets:**
    """)
    
    st.latex(r"\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\sigma_1\sigma_2\rho_{12}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Components:**
        - σₚ: Portfolio standard deviation (risk)
        - wᵢ: Weight of asset i
        - σᵢ: Standard deviation of asset i
        - ρᵢⱼ: Correlation between assets i and j
        
        **Key Point:**
        Portfolio risk is NOT a simple weighted average!
        
        Risk depends on:
        1. Individual asset risks
        2. Portfolio weights
        3. **Correlations between assets**
        """)
    
    with col2:
        st.success("""
        **Diversification Effect:**
        
        **Correlation (ρ) matters:**
        - ρ = +1: No diversification benefit
        - ρ = 0: Some diversification
        - ρ = -1: Maximum diversification
        
        **Example (2 assets, equal weights):**
        - If ρ = +1: σₚ = 0.5σ₁ + 0.5σ₂
        - If ρ = 0: σₚ < 0.5σ₁ + 0.5σ₂
        - If ρ = -1: σₚ can approach 0!
        
        **This is the "magic" of diversification**
        """)
    
    st.markdown("---")
    
    # Covariance and Correlation
    st.subheader("Covariance and Correlation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Covariance:**")
        st.latex(r"\sigma_{ij} = E[(R_i - \mu_i)(R_j - \mu_j)]")
        
        st.info("""
        **Interpretation:**
        - Measures how assets move together
        - Positive: Tend to move together
        - Negative: Tend to move oppositely
        - Zero: No linear relationship
        
        **Problem:** Scale-dependent
        - Hard to interpret magnitude
        - Not standardized
        """)
    
    with col2:
        st.markdown("**Correlation:**")
        st.latex(r"\rho_{ij} = \frac{\sigma_{ij}}{\sigma_i \sigma_j}")
        
        st.success("""
        **Properties:**
        - Range: -1 to +1
        - Scale-independent
        - Easier to interpret
        - ρ = 0: Uncorrelated
        - |ρ| = 1: Perfect linear relationship
        
        **Financial Reality:**
        - Most stocks: ρ ≈ 0.3 to 0.7
        - Stocks-bonds: ρ ≈ 0 to 0.3
        - Same sector: Higher correlation
        - Different countries: Lower correlation
        """)
    
    st.markdown("---")
    
    # Efficient Frontier
    st.header("6.2 Modern Portfolio Theory")
    
    st.subheader("The Efficient Frontier")
    
    st.info("""
    **Efficient Portfolio:**
    - Maximum return for given risk level
    - Minimum risk for given return level
    
    **Efficient Frontier:**
    - Set of all efficient portfolios
    - Plots risk (x-axis) vs return (y-axis)
    - Curved line in risk-return space
    - Rational investors choose portfolios on this frontier
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Key Concepts:**")
        
        st.success("""
        **Minimum Variance Portfolio (MVP):**
        - Leftmost point on efficient frontier
        - Lowest possible risk
        - May have low return
        
        **Tangency Portfolio:**
        - Maximum Sharpe ratio
        - Best risk-adjusted returns
        - Optimal for most investors
        
        **Dominated Portfolios:**
        - Below efficient frontier
        - Suboptimal risk-return tradeoff
        - Should be avoided
        """)
    
    with col2:
        st.warning("""
        **Markowitz Portfolio Optimization:**
        
        **Objective:** Minimize risk for target return
        """)
        
        st.latex(r"\min_w \sigma_p^2 = w^T \Sigma w")
        
        st.markdown("""
        **Subject to:**
        """)
        
        st.latex(r"w^T \mu = R_{target}")
        st.latex(r"\sum w_i = 1")
        
        st.markdown("""
        **Where:**
        - w: Vector of portfolio weights
        - Σ: Covariance matrix
        - μ: Vector of expected returns
        - R_target: Target return
        """)
    
    st.markdown("---")
    
    # Risk Measures
    st.header("6.3 Risk Measures")
    
    st.subheader("Standard Deviation vs Other Risk Metrics")
    
    risk_comparison = pd.DataFrame({
        'Measure': ['Standard Deviation', 'Semi-Deviation', 'Value at Risk (VaR)', 'CVaR/ES', 'Maximum Drawdown'],
        'What it Measures': [
            'Total volatility (up and down)',
            'Downside volatility only',
            'Maximum loss at confidence level',
            'Expected loss beyond VaR',
            'Peak-to-trough decline'
        ],
        'Pros': [
            'Easy to calculate, widely used',
            'Focuses on downside',
            'Simple to communicate',
            'Tail risk measure',
            'Actual historical loss'
        ],
        'Cons': [
            'Penalizes upside too',
            'Harder to optimize',
            'Ignores tail beyond VaR',
            'Harder to estimate',
            'Backward-looking'
        ]
    })
    
    st.table(risk_comparison)
    
    st.markdown("---")
    
    # Sharpe Ratio
    st.subheader("Sharpe Ratio")
    
    st.latex(r"SR = \frac{R_p - R_f}{\sigma_p}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Sharpe Ratio:**
        - Risk-adjusted return measure
        - Return per unit of risk
        - Higher is better
        
        **Components:**
        - Rₚ: Portfolio return
        - Rf: Risk-free rate
        - σₚ: Portfolio standard deviation
        
        **Interpretation:**
        - SR > 1: Good risk-adjusted return
        - SR > 2: Very good
        - SR > 3: Excellent (rare)
        - SR < 0: Underperforming risk-free rate
        """)
    
    with col2:
        st.warning("""
        **Example:**
        
        **Portfolio A:**
        - Return: 12%
        - Std Dev: 15%
        - Risk-free: 2%
        - SR = (12% - 2%) / 15% = 0.67
        
        **Portfolio B:**
        - Return: 10%
        - Std Dev: 8%
        - Risk-free: 2%
        - SR = (10% - 2%) / 8% = 1.00
        
        **Portfolio B is better risk-adjusted!**
        - Lower return but much lower risk
        - Higher return per unit of risk
        """)
    
    st.markdown("---")
    
    # Other Performance Metrics
    st.subheader("Other Performance Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Sortino Ratio:**")
        st.latex(r"Sortino = \frac{R_p - R_f}{\sigma_{downside}}")
        
        st.info("""
        - Like Sharpe but uses downside deviation
        - Only penalizes downside volatility
        - Better for asymmetric returns
        """)
        
        st.markdown("---")
        
        st.markdown("**Information Ratio:**")
        st.latex(r"IR = \frac{R_p - R_b}{TE}")
        
        st.info("""
        - Excess return vs benchmark
        - TE = Tracking error (std of excess returns)
        - Measures active management skill
        """)
    
    with col2:
        st.markdown("**Treynor Ratio:**")
        st.latex(r"Treynor = \frac{R_p - R_f}{\beta_p}")
        
        st.success("""
        - Return per unit of systematic risk
        - Uses beta instead of total risk
        - Better for diversified portfolios
        """)
        
        st.markdown("---")
        
        st.markdown("**Jensen's Alpha:**")
        st.latex(r"\alpha = R_p - [R_f + \beta_p(R_m - R_f)]")
        
        st.success("""
        - Excess return vs CAPM prediction
        - α > 0: Outperformance
        - Measures manager skill
        """)
    
    st.markdown("---")
    
    # Diversification
    st.header("6.4 Diversification")
    
    st.subheader("Benefits of Diversification")
    
    st.warning("""
    **Key Principle:**
    "Don't put all your eggs in one basket"
    
    **Diversification reduces risk without reducing expected return!**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Systematic vs Unsystematic Risk:**
        
        **Total Risk = Systematic + Unsystematic**
        
        **Systematic Risk (Market Risk):**
        - Cannot be diversified away
        - Affects all assets
        - Examples: recession, interest rates
        - Measured by beta
        
        **Unsystematic Risk (Specific Risk):**
        - CAN be diversified away
        - Asset-specific
        - Examples: CEO resignation, product recall
        - Eliminated with ~20-30 stocks
        """)
    
    with col2:
        st.success("""
        **How Many Stocks?**
        
        **Research findings:**
        - 1 stock: 100% risk
        - 10 stocks: ~70% risk eliminated
        - 20 stocks: ~80% risk eliminated
        - 30 stocks: ~85% risk eliminated
        - 100+ stocks: ~90% risk eliminated
        
        **Practical takeaway:**
        - 20-30 stocks capture most benefits
        - Beyond that, marginal benefit decreases
        - International diversification adds more
        
        **But correlations matter!**
        - 20 tech stocks ≠ well diversified
        - Need different sectors/countries
        """)
    
    st.markdown("---")
    
    # Capital Market Line
    st.subheader("Capital Market Line (CML)")
    
    st.latex(r"E[R_p] = R_f + \frac{E[R_m] - R_f}{\sigma_m} \times \sigma_p")
    
    st.info("""
    **Capital Market Line:**
    - Line from risk-free asset to market portfolio
    - All efficient portfolios with risk-free asset lie on CML
    - Steeper slope = Better risk-return tradeoff
    - Slope = Sharpe ratio of market portfolio
    
    **Implications:**
    - Can lend at Rf (invest in risk-free asset)
    - Can borrow at Rf (leverage market portfolio)
    - Separation theorem: All investors hold same risky portfolio
    - Only differ in allocation to risk-free asset
    """)
    
    st.markdown("---")
    
    # Rebalancing
    st.header("6.5 Portfolio Management")
    
    st.subheader("Rebalancing")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Why Rebalance?**
        
        **Problem:** Portfolio drifts over time
        - Stocks outperform → Portfolio becomes riskier
        - Weights change from target allocation
        - Risk profile no longer matches goals
        
        **Example:**
        - Start: 60% stocks, 40% bonds
        - After 1 year: 70% stocks, 30% bonds
        - Portfolio is now riskier than intended
        
        **Solution:** Sell stocks, buy bonds to restore 60/40
        """)
    
    with col2:
        st.success("""
        **Rebalancing Strategies:**
        
        **1. Calendar Rebalancing:**
        - Fixed schedule (quarterly, annually)
        - Simple and systematic
        - May trade unnecessarily
        
        **2. Threshold Rebalancing:**
        - Rebalance when weights deviate by X%
        - Example: Rebalance when stocks hit 65% or 55%
        - More responsive to markets
        
        **3. Hybrid:**
        - Check quarterly, rebalance if threshold exceeded
        - Balances both approaches
        
        **Costs to Consider:**
        - Trading commissions
        - Taxes on gains
        - Bid-ask spreads
        """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Portfolio Statistics Examples")
    
    # Example 1: Portfolio Return and Risk
    st.subheader("Example 1: Two-Asset Portfolio")
    
    st.markdown("""
    **Scenario:** Calculate portfolio return and risk for a two-asset portfolio.
    
    **Given:**
    - Asset A: E[R] = 12%, σ = 20%
    - Asset B: E[R] = 8%, σ = 12%
    - Correlation (ρ) = 0.3
    - Weight in A (w₁) = 60%, Weight in B (w₂) = 40%
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Given data
        w1, w2 = 0.6, 0.4
        r1, r2 = 12, 8
        s1, s2 = 20, 12
        rho = 0.3
        
        # Portfolio return
        rp = w1 * r1 + w2 * r2
        
        # Portfolio variance
        var_p = (w1**2 * s1**2 + w2**2 * s2**2 + 
                 2 * w1 * w2 * s1 * s2 * rho)
        
        # Portfolio std dev
        sp = np.sqrt(var_p)
        
        st.markdown("**Step-by-Step Solution:**")
        
        st.code(f"""
Step 1: Portfolio Return
Rₚ = w₁R₁ + w₂R₂
Rₚ = {w1}×{r1}% + {w2}×{r2}%
Rₚ = {rp:.2f}%

Step 2: Portfolio Variance
σₚ² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ
σₚ² = {w1}²×{s1}² + {w2}²×{s2}² + 2×{w1}×{w2}×{s1}×{s2}×{rho}
σₚ² = {var_p:.2f}

Step 3: Portfolio Standard Deviation
σₚ = √{var_p:.2f}
σₚ = {sp:.2f}%
        """)
        
        st.metric("Portfolio Return", f"{rp:.2f}%")
        st.metric("Portfolio Risk (σ)", f"{sp:.2f}%")
        
        # Diversification benefit
        weighted_avg_risk = w1 * s1 + w2 * s2
        benefit = weighted_avg_risk - sp
        
        st.success(f"""
        **Diversification Benefit:**
        - Weighted average risk: {weighted_avg_risk:.2f}%
        - Portfolio risk: {sp:.2f}%
        - Benefit: {benefit:.2f}% reduction in risk!
        """)
    
    with col2:
        # Visualize effect of correlation
        correlations = np.linspace(-1, 1, 50)
        portfolio_risks = []
        
        for rho_test in correlations:
            var_test = (w1**2 * s1**2 + w2**2 * s2**2 + 
                       2 * w1 * w2 * s1 * s2 * rho_test)
            portfolio_risks.append(np.sqrt(var_test))
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=correlations,
            y=portfolio_risks,
            mode='lines',
            line=dict(color='#81c784', width=3),
            name='Portfolio Risk'
        ))
        
        # Mark current correlation
        fig.add_vline(x=rho, line_dash="dash", line_color="yellow",
                     annotation_text=f"Current ρ={rho}")
        
        # Mark actual portfolio risk
        fig.add_scatter(x=[rho], y=[sp], mode='markers',
                       marker=dict(size=15, color='red'),
                       name='Your Portfolio')
        
        fig.update_layout(
            title="Portfolio Risk vs Correlation",
            xaxis_title="Correlation (ρ)",
            yaxis_title="Portfolio Risk (%)",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Key Insight:**
        - Lower correlation → Lower portfolio risk
        - ρ = -1: Maximum diversification
        - ρ = +1: No diversification benefit
        """)
    
    st.markdown("---")
    
    # Example 2: Efficient Frontier
    st.subheader("Example 2: Efficient Frontier Construction")
    
    st.markdown("""
    **Scenario:** Plot the efficient frontier for three assets.
    """)
    
    # Generate sample data
    np.random.seed(42)
    n_assets = 3
    
    # Expected returns (annualized %)
    returns = np.array([8, 12, 15])
    
    # Covariance matrix (annualized)
    cov_matrix = np.array([
        [100, 30, 20],
        [30, 225, 60],
        [20, 60, 400]
    ])
    
    # Generate random portfolios
    n_portfolios = 5000
    portfolio_returns = []
    portfolio_risks = []
    
    np.random.seed(42)
    for _ in range(n_portfolios):
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)
        
        ret = np.dot(weights, returns)
        risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        portfolio_returns.append(ret)
        portfolio_risks.append(risk)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Asset Characteristics:**")
        
        asset_df = pd.DataFrame({
            'Asset': ['A', 'B', 'C'],
            'Expected Return (%)': returns,
            'Std Dev (%)': np.sqrt(np.diag(cov_matrix))
        })
        st.table(asset_df)
        
        st.markdown("**Correlation Matrix:**")
        # Calculate correlation from covariance
        stds = np.sqrt(np.diag(cov_matrix))
        corr_matrix = cov_matrix / np.outer(stds, stds)
        
        corr_df = pd.DataFrame(
            corr_matrix,
            columns=['A', 'B', 'C'],
            index=['A', 'B', 'C']
        )
        st.dataframe(corr_df.style.format("{:.3f}"))
        
        # Find minimum variance portfolio
        def portfolio_variance(weights):
            return np.dot(weights.T, np.dot(cov_matrix, weights))
        
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(n_assets))
        initial_weights = np.array([1/n_assets] * n_assets)
        
        result = minimize(portfolio_variance, initial_weights,
                         method='SLSQP', bounds=bounds, constraints=constraints)
        
        mvp_weights = result.x
        mvp_return = np.dot(mvp_weights, returns)
        mvp_risk = np.sqrt(result.fun)
        
        st.markdown("**Minimum Variance Portfolio:**")
        st.metric("Expected Return", f"{mvp_return:.2f}%")
        st.metric("Risk (σ)", f"{mvp_risk:.2f}%")
        
        mvp_weights_df = pd.DataFrame({
            'Asset': ['A', 'B', 'C'],
            'Weight (%)': mvp_weights * 100
        })
        st.table(mvp_weights_df)
    
    with col2:
        # Plot efficient frontier
        fig = go.Figure()
        
        # Random portfolios
        fig.add_trace(go.Scatter(
            x=portfolio_risks,
            y=portfolio_returns,
            mode='markers',
            marker=dict(
                size=3,
                color=np.array(portfolio_returns) / np.array(portfolio_risks),
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Sharpe<br>Ratio")
            ),
            name='Random Portfolios',
            opacity=0.5
        ))
        
        # Individual assets
        individual_risks = np.sqrt(np.diag(cov_matrix))
        fig.add_trace(go.Scatter(
            x=individual_risks,
            y=returns,
            mode='markers+text',
            marker=dict(size=15, color='red', symbol='star'),
            text=['A', 'B', 'C'],
            textposition='top center',
            name='Individual Assets'
        ))
        
        # MVP
        fig.add_trace(go.Scatter(
            x=[mvp_risk],
            y=[mvp_return],
            mode='markers',
            marker=dict(size=15, color='yellow', symbol='diamond'),
            name='Min Variance Portfolio'
        ))
        
        fig.update_layout(
            title="Efficient Frontier",
            xaxis_title="Risk (Standard Deviation %)",
            yaxis_title="Expected Return (%)",
            template="plotly_dark",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.success("""
    **Key Observations:**
    - Points on the upper edge form the efficient frontier
    - Points below are dominated (suboptimal)
    - Color shows Sharpe ratio (darker = better)
    - MVP has lowest risk but not highest return
    """)
    
    st.markdown("---")
    
    # Example 3: Sharpe Ratio Comparison
    st.subheader("Example 3: Comparing Portfolios with Sharpe Ratio")
    
    st.markdown("""
    **Scenario:** Compare three portfolios using Sharpe ratio.
    
    **Risk-free rate:** 3%
    """)
    
    portfolios_data = {
        'Portfolio': ['Aggressive Growth', 'Balanced', 'Conservative'],
        'Return (%)': [15, 10, 6],
        'Risk (%)': [25, 12, 5],
        'Sharpe Ratio': []
    }
    
    rf = 3
    
    for i in range(len(portfolios_data['Portfolio'])):
        ret = portfolios_data['Return (%)'][i]
        risk = portfolios_data['Risk (%)'][i]
        sharpe = (ret - rf) / risk
        portfolios_data['Sharpe Ratio'].append(sharpe)
    
    df_portfolios = pd.DataFrame(portfolios_data)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.table(df_portfolios)
        
        st.markdown("**Calculations:**")
        for i, row in df_portfolios.iterrows():
            st.code(f"""
{row['Portfolio']}:
SR = ({row['Return (%)']}% - {rf}%) / {row['Risk (%)']}%
SR = {row['Sharpe Ratio']:.4f}
            """)
        
        best_idx = df_portfolios['Sharpe Ratio'].idxmax()
        best = df_portfolios.iloc[best_idx]
        
        st.success(f"""
        **Winner: {best['Portfolio']}**
        
        Despite having moderate return, the Balanced portfolio
        has the best risk-adjusted performance with 
        Sharpe Ratio of {best['Sharpe Ratio']:.4f}
        """)
    
    with col2:
        # Visualize
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df_portfolios['Risk (%)'],
            y=df_portfolios['Return (%)'],
            mode='markers+text',
            marker=dict(
                size=df_portfolios['Sharpe Ratio'] * 100,
                color=df_portfolios['Sharpe Ratio'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Sharpe Ratio")
            ),
            text=df_portfolios['Portfolio'],
            textposition='top center',
            name='Portfolios'
        ))
        
        # Risk-free rate
        fig.add_trace(go.Scatter(
            x=[0],
            y=[rf],
            mode='markers',
            marker=dict(size=15, color='yellow', symbol='star'),
            name='Risk-Free'
        ))
        
        fig.update_layout(
            title="Risk-Return Space",
            xaxis_title="Risk (%)",
            yaxis_title="Return (%)",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Portfolio Analysis")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["Two-Asset Portfolio", "Efficient Frontier Explorer", 
         "Portfolio Optimizer", "Diversification Simulator"]
    )
    
    if exercise == "Two-Asset Portfolio":
        st.subheader("📊 Two-Asset Portfolio Builder")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Asset A:**")
            r1 = st.slider("Expected Return A (%):", 0, 30, 12)
            s1 = st.slider("Std Dev A (%):", 1, 50, 20)
            
            st.markdown("**Asset B:**")
            r2 = st.slider("Expected Return B (%):", 0, 30, 8)
            s2 = st.slider("Std Dev B (%):", 1, 50, 12)
            
            st.markdown("**Portfolio:**")
            w1 = st.slider("Weight in A (%):", 0, 100, 60) / 100
            w2 = 1 - w1
            
            rho = st.slider("Correlation (ρ):", -1.0, 1.0, 0.3, 0.1)
            
            # Calculate portfolio stats
            rp = w1 * r1 + w2 * r2
            var_p = (w1**2 * s1**2 + w2**2 * s2**2 + 
                     2 * w1 * w2 * s1 * s2 * rho)
            sp = np.sqrt(var_p)
            
            st.markdown("**Results:**")
            st.metric("Portfolio Return", f"{rp:.2f}%")
            st.metric("Portfolio Risk", f"{sp:.2f}%")
            st.metric("Weight in B", f"{w2*100:.0f}%")
        
        with col2:
            # Plot feasible set
            weights_a = np.linspace(0, 1, 100)
            port_returns = []
            port_risks = []
            
            for w_a in weights_a:
                w_b = 1 - w_a
                ret = w_a * r1 + w_b * r2
                var = (w_a**2 * s1**2 + w_b**2 * s2**2 + 
                       2 * w_a * w_b * s1 * s2 * rho)
                risk = np.sqrt(var)
                
                port_returns.append(ret)
                port_risks.append(risk)
            
            fig = go.Figure()
            
            # Feasible set
            fig.add_trace(go.Scatter(
                x=port_risks,
                y=port_returns,
                mode='lines',
                line=dict(color='#81c784', width=3),
                name='Feasible Set'
            ))
            
            # Individual assets
            fig.add_trace(go.Scatter(
                x=[s1, s2],
                y=[r1, r2],
                mode='markers+text',
                marker=dict(size=15, color='red'),
                text=['A', 'B'],
                textposition='top center',
                name='Assets'
            ))
            
            # Current portfolio
            fig.add_trace(go.Scatter(
                x=[sp],
                y=[rp],
                mode='markers',
                marker=dict(size=20, color='yellow', symbol='star'),
                name='Your Portfolio'
            ))
            
            fig.update_layout(
                title="Portfolio Possibilities",
                xaxis_title="Risk (σ %)",
                yaxis_title="Expected Return (%)",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.info(f"""
            **Interpretation:**
            - Your portfolio: {w1*100:.0f}% in A, {w2*100:.0f}% in B
            - The curve shows all possible combinations
            - Notice how shape changes with correlation!
            """)
    
    elif exercise == "Efficient Frontier Explorer":
        st.subheader("🎯 Efficient Frontier Explorer")
        
        n_assets = st.slider("Number of assets:", 2, 5, 3)
        
        st.markdown("**Asset Parameters:**")
        
        returns = []
        risks = []
        
        cols = st.columns(n_assets)
        for i in range(n_assets):
            with cols[i]:
                st.markdown(f"**Asset {i+1}:**")
                ret = st.number_input(f"Return (%):", value=8+i*3, key=f"ret{i}")
                risk = st.number_input(f"Risk (%):", value=10+i*5, key=f"risk{i}")
                returns.append(ret)
                risks.append(risk)
        
        # Create correlation matrix
        st.markdown("**Average Correlation:**")
        avg_corr = st.slider("Average correlation:", 0.0, 1.0, 0.3, 0.1)
        
        # Build covariance matrix
        corr_matrix = np.full((n_assets, n_assets), avg_corr)
        np.fill_diagonal(corr_matrix, 1.0)
        
        stds = np.array(risks)
        cov_matrix = np.outer(stds, stds) * corr_matrix
        
        if st.button("Generate Efficient Frontier"):
            # Generate random portfolios
            n_portfolios = 5000
            portfolio_returns = []
            portfolio_risks = []
            
            np.random.seed(42)
            for _ in range(n_portfolios):
                weights = np.random.random(n_assets)
                weights /= np.sum(weights)
                
                ret = np.dot(weights, returns)
                risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
                
                portfolio_returns.append(ret)
                portfolio_risks.append(risk)
            
            # Plot
            fig = go.Figure()
            
            # Random portfolios
            fig.add_trace(go.Scatter(
                x=portfolio_risks,
                y=portfolio_returns,
                mode='markers',
                marker=dict(
                    size=3,
                    color=portfolio_returns,
                    colorscale='Viridis',
                    showscale=True
                ),
                name='Portfolios',
                opacity=0.6
            ))
            
            # Individual assets
            fig.add_trace(go.Scatter(
                x=risks,
                y=returns,
                mode='markers+text',
                marker=dict(size=15, color='red', symbol='star'),
                text=[f"{i+1}" for i in range(n_assets)],
                textposition='top center',
                name='Individual Assets'
            ))
            
            fig.update_layout(
                title="Efficient Frontier",
                xaxis_title="Risk (%)",
                yaxis_title="Return (%)",
                template="plotly_dark",
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif exercise == "Portfolio Optimizer":
        st.subheader("⚡ Portfolio Optimizer")
        
        st.markdown("""
        Find the optimal portfolio for your risk tolerance.
        """)
        
        # Sample assets
        asset_data = {
            'Asset': ['US Stocks', 'Intl Stocks', 'Bonds', 'Real Estate', 'Commodities'],
            'Return': [10, 12, 5, 8, 7],
            'Risk': [15, 18, 5, 12, 20]
        }
        
        df_assets = pd.DataFrame(asset_data)
        
        st.dataframe(df_assets)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            target_return = st.slider("Target Return (%):", 5, 12, 8)
            
            # Simple correlation assumption
            avg_corr = 0.4
            n = len(df_assets)
            
            corr_matrix = np.full((n, n), avg_corr)
            np.fill_diagonal(corr_matrix, 1.0)
            
            stds = np.array(df_assets['Risk'])
            cov_matrix = np.outer(stds, stds) * corr_matrix
            
            # Optimization
            def portfolio_variance(weights):
                return np.dot(weights.T, np.dot(cov_matrix, weights))
            
            constraints = [
                {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
                {'type': 'eq', 'fun': lambda x: np.dot(x, df_assets['Return']) - target_return}
            ]
            
            bounds = tuple((0, 1) for _ in range(n))
            initial_weights = np.array([1/n] * n)
            
            try:
                result = minimize(portfolio_variance, initial_weights,
                                method='SLSQP', bounds=bounds, constraints=constraints)
                
                if result.success:
                    optimal_weights = result.x
                    optimal_risk = np.sqrt(result.fun)
                    
                    st.markdown("**Optimal Weights:**")
                    
                    weights_df = pd.DataFrame({
                        'Asset': df_assets['Asset'],
                        'Weight (%)': optimal_weights * 100
                    })
                    
                    # Filter out negligible weights
                    weights_df = weights_df[weights_df['Weight (%)'] > 0.5]
                    st.table(weights_df)
                    
                    st.metric("Portfolio Risk", f"{optimal_risk:.2f}%")
                    st.metric("Target Return", f"{target_return}%")
                else:
                    st.error("Optimization failed. Try different target return.")
            except:
                st.error("Could not find feasible portfolio.")
        
        with col2:
            if 'optimal_weights' in locals():
                # Pie chart
                fig = go.Figure(data=[go.Pie(
                    labels=df_assets['Asset'],
                    values=optimal_weights * 100,
                    hole=0.3
                )])
                
                fig.update_layout(
                    title="Optimal Portfolio Allocation",
                    template="plotly_dark",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
    
    elif exercise == "Diversification Simulator":
        st.subheader("🎲 Diversification Benefits Simulator")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            n_stocks = st.slider("Number of stocks:", 1, 50, 1)
            avg_stock_risk = st.slider("Avg stock risk (%):", 10, 50, 30)
            avg_correlation = st.slider("Avg correlation:", 0.0, 0.9, 0.3, 0.1)
            
            # Calculate portfolio risk
            # Simple approximation
            portfolio_risk = avg_stock_risk * np.sqrt(
                (1 / n_stocks) + ((n_stocks - 1) / n_stocks) * avg_correlation
            )
            
            # Risk reduction
            risk_reduction = (avg_stock_risk - portfolio_risk) / avg_stock_risk * 100
            
            st.markdown("**Results:**")
            st.metric("Single Stock Risk", f"{avg_stock_risk}%")
            st.metric("Portfolio Risk", f"{portfolio_risk:.2f}%")
            st.metric("Risk Reduction", f"{risk_reduction:.1f}%")
            
            st.info(f"""
            **Interpretation:**
            
            By holding {n_stocks} stocks instead of 1,
            you've reduced risk by {risk_reduction:.1f}%!
            
            This is the power of diversification.
            """)
        
        with col2:
            # Show how risk decreases with number of stocks
            n_range = np.arange(1, 51)
            risks = []
            
            for n in n_range:
                risk = avg_stock_risk * np.sqrt(
                    (1 / n) + ((n - 1) / n) * avg_correlation
                )
                risks.append(risk)
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=n_range,
                y=risks,
                mode='lines',
                line=dict(color='#81c784', width=3),
                fill='tozeroy',
                fillcolor='rgba(129, 199, 132, 0.3)'
            ))
            
            # Mark current portfolio
            fig.add_scatter(
                x=[n_stocks],
                y=[portfolio_risk],
                mode='markers',
                marker=dict(size=15, color='yellow'),
                name='Your Portfolio'
            )
            
            # Asymptote
            asymptote = avg_stock_risk * np.sqrt(avg_correlation)
            fig.add_hline(y=asymptote, line_dash="dash", line_color="red",
                         annotation_text=f"Systematic Risk: {asymptote:.1f}%")
            
            fig.update_layout(
                title="Portfolio Risk vs Number of Stocks",
                xaxis_title="Number of Stocks",
                yaxis_title="Portfolio Risk (%)",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.warning("""
            **Key Insight:**
            
            - Risk drops rapidly with first 10-20 stocks
            - Beyond that, marginal benefit decreases
            - Cannot eliminate systematic risk (dashed line)
            - Lower correlation → More diversification benefit
            """)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Portfolio Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["Portfolio Return & Risk", "Sharpe Ratio", "Optimal Weights", "Rebalancing"]
    )
    
    if calc_type == "Portfolio Return & Risk":
        st.subheader("Portfolio Return & Risk Calculator")
        
        st.markdown("**Two-Asset Portfolio:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Asset 1:**")
            r1 = st.number_input("Expected Return (%):", value=12.0, key="r1")
            s1 = st.number_input("Standard Deviation (%):", value=20.0, key="s1")
            w1 = st.number_input("Weight (%):", value=60.0, key="w1") / 100
        
        with col2:
            st.markdown("**Asset 2:**")
            r2 = st.number_input("Expected Return (%):", value=8.0, key="r2")
            s2 = st.number_input("Standard Deviation (%):", value=12.0, key="s2")
            w2 = st.number_input("Weight (%):", value=40.0, key="w2") / 100
        
        rho = st.slider("Correlation:", -1.0, 1.0, 0.3, 0.1)
        
        if st.button("Calculate"):
            if abs((w1 + w2) - 1.0) > 0.01:
                st.error("Weights must sum to 100%!")
            else:
                # Portfolio return
                rp = w1 * r1 + w2 * r2
                
                # Portfolio variance and std dev
                var_p = (w1**2 * s1**2 + w2**2 * s2**2 + 
                         2 * w1 * w2 * s1 * s2 * rho)
                sp = np.sqrt(var_p)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Results:**")
                    st.metric("Portfolio Return", f"{rp:.2f}%")
                    st.metric("Portfolio Risk (σ)", f"{sp:.2f}%")
                    st.metric("Portfolio Variance", f"{var_p:.2f}")
                
                with col2:
                    # Diversification benefit
                    weighted_risk = w1 * s1 + w2 * s2
                    benefit = weighted_risk - sp
                    benefit_pct = benefit / weighted_risk * 100
                    
                    st.markdown("**Diversification Benefit:**")
                    st.metric("Weighted Avg Risk", f"{weighted_risk:.2f}%")
                    st.metric("Risk Reduction", f"{benefit:.2f}%")
                    st.metric("Benefit", f"{benefit_pct:.1f}%")
    
    elif calc_type == "Sharpe Ratio":
        st.subheader("Sharpe Ratio Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            portfolio_return = st.number_input("Portfolio Return (%):", value=12.0)
            risk_free = st.number_input("Risk-Free Rate (%):", value=3.0)
            portfolio_risk = st.number_input("Portfolio Risk (σ %):", value=15.0)
            
            if st.button("Calculate Sharpe Ratio"):
                sharpe = (portfolio_return - risk_free) / portfolio_risk
                
                st.markdown("**Result:**")
                st.metric("Sharpe Ratio", f"{sharpe:.4f}")
                
                st.markdown("**Calculation:**")
                st.latex(f"SR = \\frac{{{portfolio_return} - {risk_free}}}{{{portfolio_risk}}} = {sharpe:.4f}")
                
                if sharpe > 2:
                    st.success("🌟 Excellent risk-adjusted return!")
                elif sharpe > 1:
                    st.success("✅ Good risk-adjusted return")
                elif sharpe > 0:
                    st.warning("⚠️ Modest risk-adjusted return")
                else:
                    st.error("❌ Underperforming risk-free rate")
        
        with col2:
            st.info("""
            **Sharpe Ratio Interpretation:**
            
            - **SR > 3:** Exceptional (rare)
            - **SR > 2:** Excellent
            - **SR > 1:** Good
            - **SR > 0:** Positive excess return
            - **SR < 0:** Underperforming risk-free
            
            **What it means:**
            - Return earned per unit of risk
            - Higher is better
            - Compare portfolios on risk-adjusted basis
            - Most useful for comparing similar strategies
            """)

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 6 Quiz: Portfolio Statistics")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'Portfolio return is calculated as:',
            'options': [
                'Average of individual returns',
                'Weighted average of individual returns',
                'Geometric mean of returns',
                'Maximum return minus minimum return'
            ],
            'correct': 'Weighted average of individual returns',
            'explanation': 'Portfolio return = Σ(wᵢ × Rᵢ), a weighted average based on portfolio weights.'
        },
        {
            'id': 2,
            'question': 'Portfolio risk depends on:',
            'options': [
                'Only individual asset risks',
                'Only portfolio weights',
                'Individual risks, weights, AND correlations',
                'Just the highest risk asset'
            ],
            'correct': 'Individual risks, weights, AND correlations',
            'explanation': 'Portfolio variance includes individual variances, weights, and crucially, the correlations between assets.'
        },
        {
            'id': 3,
            'question': 'Maximum diversification benefit occurs when correlation is:',
            'options': [
                'ρ = +1',
                'ρ = 0',
                'ρ = -1',
                'ρ = 0.5'
            ],
            'correct': 'ρ = -1',
            'explanation': 'Perfect negative correlation (ρ = -1) provides maximum diversification, potentially eliminating all risk.'
        },
        {
            'id': 4,
            'question': 'The Sharpe ratio measures:',
            'options': [
                'Total return',
                'Risk per unit of return',
                'Excess return per unit of risk',
                'Correlation with market'
            ],
            'correct': 'Excess return per unit of risk',
            'explanation': 'Sharpe ratio = (Rₚ - Rf) / σₚ, showing risk-adjusted performance.'
        },
        {
            'id': 5,
            'question': 'The efficient frontier consists of portfolios that:',
            'options': [
                'Have the highest returns',
                'Have the lowest risks',
                'Maximize return for given risk',
                'Have equal weights'
            ],
            'correct': 'Maximize return for given risk',
            'explanation': 'Efficient frontier contains portfolios with maximum return for each risk level (or minimum risk for each return).'
        },
        {
            'id': 6,
            'question': 'Unsystematic risk can be:',
            'options': [
                'Never eliminated',
                'Eliminated through diversification',
                'Only hedged with derivatives',
                'Increased with more assets'
            ],
            'correct': 'Eliminated through diversification',
            'explanation': 'Unsystematic (specific) risk can be diversified away; systematic (market) risk cannot.'
        },
        {
            'id': 7,
            'question': 'If correlation = +1, diversification:',
            'options': [
                'Provides maximum benefit',
                'Provides some benefit',
                'Provides no benefit',
                'Increases risk'
            ],
            'correct': 'Provides no benefit',
            'explanation': 'When ρ = +1, assets move perfectly together, so no risk reduction from diversification.'
        },
        {
            'id': 8,
            'question': 'The minimum variance portfolio:',
            'options': [
                'Has maximum return',
                'Has minimum risk',
                'Has highest Sharpe ratio',
                'Contains only bonds'
            ],
            'correct': 'Has minimum risk',
            'explanation': 'MVP is the portfolio with the lowest possible risk (leftmost point on efficient frontier).'
        },
        {
            'id': 9,
            'question': 'Rebalancing is done to:',
            'options': [
                'Maximize returns',
                'Minimize taxes',
                'Maintain target risk level',
                'Eliminate all risk'
            ],
            'correct': 'Maintain target risk level',
            'explanation': 'Rebalancing restores original asset allocation as market movements cause portfolio drift.'
        },
        {
            'id': 10,
            'question': 'Research suggests that most diversification benefits are captured with:',
            'options': [
                '5 stocks',
                '20-30 stocks',
                '100 stocks',
                '500 stocks'
            ],
            'correct': '20-30 stocks',
            'explanation': 'Studies show 20-30 stocks across different sectors eliminate most unsystematic risk.'
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
    st.header("Module 6 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Portfolio Return & Risk**
        - Return: Weighted average
        - Risk: NOT weighted average
        - Correlation matters for risk
        - Diversification reduces risk
        """)
        
        st.success("""
        **Efficient Frontier**
        - Maximum return per risk
        - Optimal portfolios
        - Minimum variance portfolio
        - Tangency portfolio (max Sharpe)
        """)
    
    with col2:
        st.warning("""
        **Risk-Adjusted Performance**
        - Sharpe ratio: Excess return/risk
        - Sortino: Uses downside risk
        - Treynor: Uses beta
        - Information ratio: vs benchmark
        """)
        
        st.info("""
        **Diversification**
        - Eliminates unsystematic risk
        - Cannot eliminate systematic risk
        - 20-30 stocks capture most benefit
        - Correlation is key
        """)
    
    st.markdown("---")
    st.subheader("📐 Essential Formulas")
    
    formulas_df = pd.DataFrame({
        'Concept': ['Portfolio Return', 'Portfolio Risk (2 assets)', 'Sharpe Ratio', 'Correlation', 'Beta'],
        'Formula': [
            'Rₚ = Σwᵢ Rᵢ',
            'σₚ² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ₁₂',
            'SR = (Rₚ - Rf) / σₚ',
            'ρ = Cov(X,Y) / (σₓσᵧ)',
            'β = Cov(Rᵢ,Rₘ) / Var(Rₘ)'
        ]
    })
    st.table(formulas_df)
    
    st.markdown("---")
    st.subheader("💼 Practical Applications")
    
    tab1, tab2, tab3 = st.tabs(["Asset Allocation", "Risk Management", "Performance"])
    
    with tab1:
        st.markdown("""
        **Strategic Asset Allocation:**
        
        1. **Determine risk tolerance**
           - Conservative: 30/70 stocks/bonds
           - Moderate: 60/40
           - Aggressive: 80/20
        
        2. **Optimize within constraints**
           - Use efficient frontier
           - Consider transaction costs
           - Tax implications
        
        3. **Diversify globally**
           - US stocks
           - International stocks
           - Emerging markets
           - Bonds, REITs, commodities
        
        4. **Rebalance regularly**
           - Maintain target allocation
           - Control risk drift
           - Harvest gains
        """)
    
    with tab2:
        st.markdown("""
        **Risk Management:**
        
        1. **Measure total risk**
           - Standard deviation
           - VaR, CVaR
           - Maximum drawdown
        
        2. **Identify sources**
           - Systematic vs unsystematic
           - Factor exposures
           - Concentration risk
        
        3. **Manage exposure**
           - Diversification
           - Hedging
           - Position sizing
        
        4. **Monitor continuously**
           - Risk metrics dashboard
           - Stress testing
           - Scenario analysis
        """)
    
    with tab3:
        st.markdown("""
        **Performance Evaluation:**
        
        1. **Absolute returns**
           - Total return
           - Annualized return
           - Time-weighted return
        
        2. **Risk-adjusted**
           - Sharpe ratio
           - Sortino ratio
           - Calmar ratio
        
        3. **Relative performance**
           - vs Benchmark
           - Information ratio
           - Tracking error
        
        4. **Attribution analysis**
           - Asset allocation effect
           - Security selection
           - Interaction effects
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 7?**
    
    Module 7: Risk Analytics covers:
    - Value at Risk (VaR)
    - Stress testing
    - Risk decomposition
    - Advanced risk metrics
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #c8e6c9; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 6 of 12: Portfolio Statistics</p>
</div>
""", unsafe_allow_html=True)