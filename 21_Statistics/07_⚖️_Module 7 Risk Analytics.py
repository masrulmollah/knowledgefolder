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
        background: linear-gradient(135deg, #b71c1c 0%, #c62828 50%, #d32f2f 100%);
    }
    h1 {
        color: #ffcdd2;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #ef9a9a;
        border-left: 6px solid #ffcdd2;
        padding-left: 15px;
    }
    h3 {
        color: #ffebee;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>⚠️ Module 7: Risk Analytics</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffebee;'>Measuring and Managing Financial Risk</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 7 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("7.1 Value at Risk (VaR)")
    
    st.subheader("What is VaR?")
    
    st.warning("""
    **Value at Risk (VaR):**
    
    The maximum loss expected over a given time period at a given confidence level.
    
    **Example:** 1-day 95% VaR = $1 million means:
    - 95% of days, losses will be less than $1 million
    - 5% of days (1 in 20), losses could exceed $1 million
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Three Parameters:**
        
        1. **Time Horizon:**
           - 1 day (for trading desks)
           - 10 days (for regulatory capital)
           - 1 month (for portfolio managers)
        
        2. **Confidence Level:**
           - 95% (common)
           - 99% (regulatory)
           - 99.9% (extreme risk)
        
        3. **Currency:**
           - Dollar amount
           - Percentage of portfolio
        """)
    
    with col2:
        st.success("""
        **Interpretation:**
        
        **1-day 95% VaR = $100,000**
        
        "We are 95% confident that our maximum loss over the next day will not exceed $100,000"
        
        OR
        
        "On 95% of days, we expect to lose less than $100,000"
        
        OR
        
        "On average, 1 out of 20 days, we expect losses to exceed $100,000"
        """)
    
    st.markdown("---")
    
    # VaR Methods
    st.subheader("VaR Calculation Methods")
    
    st.markdown("### 1. Parametric VaR (Variance-Covariance)")
    
    st.latex(r"VaR = -(\mu - z_{\alpha} \times \sigma) \times V")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Components:**
        - μ: Expected return
        - z_α: z-score for confidence level
        - σ: Standard deviation
        - V: Portfolio value
        
        **z-scores:**
        - 90%: 1.28
        - 95%: 1.645
        - 99%: 2.33
        
        **Assumptions:**
        - Returns are normally distributed
        - Linear relationships
        - Constant volatility
        """)
    
    with col2:
        st.warning("""
        **Advantages:**
        - Fast and simple
        - Easy to calculate
        - Analytically tractable
        
        **Disadvantages:**
        - Assumes normality (fat tails in reality)
        - Ignores skewness and kurtosis
        - Poor for options/non-linear products
        - Underestimates tail risk
        
        **Best for:**
        - Linear portfolios
        - Normal market conditions
        - Quick estimates
        """)
    
    st.markdown("---")
    
    st.markdown("### 2. Historical Simulation VaR")
    
    st.success("""
    **Method:**
    1. Collect historical returns (e.g., 250 days)
    2. Apply these returns to current portfolio
    3. Sort the outcomes from worst to best
    4. Find the α-th percentile
    
    **Example (95% VaR):**
    - 250 days of data
    - Sort from worst to best
    - 5% × 250 = 12.5 → 13th worst day
    - VaR = 13th worst loss
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Advantages:**
        - No distribution assumption
        - Captures fat tails
        - Includes actual market behavior
        - Easy to understand
        
        **Best for:**
        - Non-normal returns
        - Complex portfolios
        - When history is relevant
        """)
    
    with col2:
        st.warning("""
        **Disadvantages:**
        - Requires long history
        - Past may not predict future
        - Ignores recent regime changes
        - Discrete (not smooth)
        
        **Issues:**
        - Structural breaks
        - Rare events not in sample
        - Data availability
        """)
    
    st.markdown("---")
    
    st.markdown("### 3. Monte Carlo Simulation VaR")
    
    st.latex(r"\text{Generate } N \text{ scenarios using: } R_t = \mu + \sigma \epsilon_t")
    
    st.info("""
    **Method:**
    1. Specify return distribution (normal, t-distribution, etc.)
    2. Generate thousands of random scenarios
    3. Calculate portfolio value for each scenario
    4. Sort outcomes and find α-th percentile
    
    **Example:**
    - Generate 10,000 random return paths
    - Calculate portfolio value in each scenario
    - Sort results
    - 95% VaR = 500th worst outcome (5% × 10,000)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Advantages:**
        - Handles non-linearity
        - Flexible distributions
        - Can model correlations
        - Works for complex derivatives
        
        **Best for:**
        - Options portfolios
        - Complex structures
        - Path-dependent products
        - Stress scenarios
        """)
    
    with col2:
        st.warning("""
        **Disadvantages:**
        - Computationally intensive
        - Model risk (wrong assumptions)
        - Requires parameter estimation
        - Can be slow
        
        **Challenges:**
        - Choosing right distribution
        - Correlation modeling
        - Calibration
        """)
    
    st.markdown("---")
    
    # CVaR
    st.header("7.2 Conditional VaR (CVaR / Expected Shortfall)")
    
    st.subheader("Beyond VaR: CVaR")
    
    st.warning("""
    **Problem with VaR:**
    VaR tells you the threshold but not how bad losses could be beyond that threshold.
    
    **Example:**
    - 95% VaR = $1 million
    - But losses in the worst 5% could be $1.1M, $5M, or $50M!
    - VaR doesn't tell you
    """)
    
    st.latex(r"CVaR_{\alpha} = E[Loss | Loss > VaR_{\alpha}]")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Conditional VaR (CVaR):**
        
        Also called Expected Shortfall (ES)
        
        **Definition:**
        Average loss given that loss exceeds VaR
        
        **Example:**
        - 95% VaR = $1M
        - 95% CVaR = $1.5M
        - Meaning: When losses exceed VaR (5% of time), average loss is $1.5M
        
        **Always:** CVaR ≥ VaR
        """)
    
    with col2:
        st.success("""
        **Why CVaR is Better:**
        
        1. **Captures tail risk**
           - Shows severity, not just frequency
           - Accounts for extreme losses
        
        2. **Coherent risk measure**
           - Satisfies mathematical properties
           - Subadditive (diversification benefit)
        
        3. **Regulatory preference**
           - Basel III uses ES
           - More conservative
        
        4. **Portfolio optimization**
           - Better for risk minimization
           - Smooth objective function
        """)
    
    st.markdown("---")
    
    # Risk Decomposition
    st.header("7.3 Risk Decomposition")
    
    st.subheader("Component VaR")
    
    st.info("""
    **Component VaR:**
    How much does each position contribute to total portfolio VaR?
    
    **Key Insight:**
    Individual VaRs don't add up to portfolio VaR (due to diversification)
    
    **Component VaR considers:**
    - Position size
    - Position volatility  
    - Correlation with portfolio
    """)
    
    st.latex(r"CVaR_i = \beta_i \times VaR_{portfolio}")
    
    st.markdown("""
    **Where:**
    - β_i = sensitivity of position i to portfolio
    - Σ Component VaR = Total Portfolio VaR
    """)
    
    st.markdown("---")
    
    st.subheader("Marginal VaR")
    
    st.success("""
    **Marginal VaR:**
    Change in portfolio VaR from a small change in position
    
    **Use cases:**
    - Incremental position sizing
    - Risk limits
    - Trading decisions
    
    **Interpretation:**
    "Adding $1 to position X increases portfolio VaR by $Y"
    
    **Formula:**
    """)
    
    st.latex(r"MVaR_i = \frac{\partial VaR_p}{\partial w_i}")
    
    st.markdown("---")
    
    # Stress Testing
    st.header("7.4 Stress Testing")
    
    st.subheader("Beyond VaR: Scenario Analysis")
    
    st.warning("""
    **Why Stress Testing?**
    
    **VaR Limitations:**
    - Based on normal times
    - Underestimates crisis risk
    - Assumes stable correlations
    - Ignores regime changes
    
    **Stress testing asks:**
    "What if something really bad happens?"
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Types of Stress Tests:**
        
        **1. Historical Scenarios:**
        - 2008 Financial Crisis
        - 1987 Black Monday
        - 2020 COVID crash
        - 2000 Dot-com bust
        
        **2. Hypothetical Scenarios:**
        - Interest rates +300 bps
        - Market crash -30%
        - Currency crisis
        - Credit spread blowout
        
        **3. Reverse Stress Testing:**
        - What scenario breaks us?
        - Work backwards from failure
        """)
    
    with col2:
        st.success("""
        **Implementation:**
        
        **Step 1: Define scenario**
        - Market moves (stocks -20%, bonds +5%)
        - Correlation changes
        - Volatility spikes
        
        **Step 2: Apply to portfolio**
        - Revalue all positions
        - Calculate P&L
        
        **Step 3: Analyze results**
        - Total loss
        - Position-level impacts
        - Concentration risks
        
        **Step 4: Action plan**
        - Risk limits
        - Hedges
        - Contingency plans
        """)
    
    st.markdown("---")
    
    # Other Risk Metrics
    st.header("7.5 Other Risk Metrics")
    
    st.subheader("Maximum Drawdown (MDD)")
    
    st.latex(r"MDD = \max_{t \in [0,T]} \left[ \max_{s \in [0,t]} V_s - V_t \right]")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Maximum Drawdown:**
        
        Largest peak-to-trough decline in portfolio value
        
        **Example:**
        - Portfolio peaks at $1.2M
        - Falls to $900K
        - MDD = ($1.2M - $900K) / $1.2M = 25%
        
        **Why it matters:**
        - Historical worst-case loss
        - Easy to understand
        - Behavioral finance (pain of losses)
        - Recovery time indicator
        """)
    
    with col2:
        st.warning("""
        **Characteristics:**
        
        **Advantages:**
        - Actual historical loss
        - No distributional assumptions
        - Intuitive
        
        **Disadvantages:**
        - Backward-looking only
        - Doesn't predict future
        - One data point (doesn't show frequency)
        - Path-dependent
        
        **Use with:**
        - Recovery time
        - Frequency of drawdowns
        - Current drawdown level
        """)
    
    st.markdown("---")
    
    st.subheader("Risk-Adjusted Return Metrics")
    
    metrics_comparison = pd.DataFrame({
        'Metric': ['Sharpe Ratio', 'Sortino Ratio', 'Calmar Ratio', 'MAR Ratio', 'Omega Ratio'],
        'Formula': [
            '(R - Rf) / σ',
            '(R - Rf) / σ_downside',
            'R / MDD',
            'CAGR / MDD',
            'Prob(gains) / Prob(losses)'
        ],
        'Risk Measure': [
            'Total volatility',
            'Downside volatility',
            'Max drawdown',
            'Max drawdown',
            'Full distribution'
        ],
        'When to Use': [
            'General use',
            'Asymmetric returns',
            'Recovery focus',
            'Long-term performance',
            'Non-normal returns'
        ]
    })
    
    st.table(metrics_comparison)
    
    st.markdown("---")
    
    # Regulatory Capital
    st.header("7.6 Regulatory Capital Requirements")
    
    st.subheader("Basel III Market Risk")
    
    st.warning("""
    **Regulatory VaR:**
    
    Banks must hold capital based on market risk
    
    **Basel Requirements:**
    - 99% confidence level (not 95%)
    - 10-day holding period
    - At least 1 year of historical data
    - Daily backtesting required
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Market Risk Capital:**
        
        **Standard Approach:**
        - Bucketing by risk factors
        - Standardized risk weights
        - Simple but conservative
        
        **Internal Models Approach:**
        - Bank's own VaR model
        - Must be approved by regulator
        - Backtesting required
        - More risk-sensitive
        """)
    
    with col2:
        st.success("""
        **Key Concepts:**
        
        **Scaling VaR:**
        - 1-day to 10-day VaR
        - √10 rule (if normal)
        - VaR_10d ≈ VaR_1d × √10
        
        **Backtesting:**
        - Compare VaR forecasts to actual losses
        - Count "exceptions" (losses > VaR)
        - Green/Yellow/Red zones
        - Too many exceptions → Increase capital
        """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Risk Analytics Examples")
    
    # Example 1: Parametric VaR
    st.subheader("Example 1: Parametric VaR Calculation")
    
    st.markdown("""
    **Scenario:** Calculate 1-day 95% VaR for a stock portfolio.
    
    **Given:**
    - Portfolio value: $1,000,000
    - Expected daily return: 0.05%
    - Daily volatility: 1.5%
    - Confidence level: 95%
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Given data
        portfolio_value = 1_000_000
        mu = 0.05  # daily return %
        sigma = 1.5  # daily volatility %
        confidence = 0.95
        
        # z-score for 95%
        z_score = stats.norm.ppf(confidence)
        
        # VaR calculation
        var_pct = -(mu - z_score * sigma)
        var_dollar = var_pct / 100 * portfolio_value
        
        st.markdown("**Step-by-Step Calculation:**")
        
        st.code(f"""
Step 1: Find z-score
For 95% confidence: z = {z_score:.4f}

Step 2: Calculate VaR percentage
VaR% = -(μ - z × σ)
VaR% = -({mu}% - {z_score:.4f} × {sigma}%)
VaR% = -{mu - z_score * sigma:.4f}%
VaR% = {var_pct:.4f}%

Step 3: Convert to dollars
VaR($) = {var_pct:.4f}% × ${portfolio_value:,}
VaR($) = ${var_dollar:,.2f}
        """)
        
        st.metric("1-day 95% VaR", f"${var_dollar:,.2f}")
        
        st.success(f"""
        **Interpretation:**
        
        We are 95% confident that the portfolio will not lose 
        more than ${var_dollar:,.2f} in one day.
        
        On average, losses will exceed this amount on 
        approximately 1 out of 20 days (5% of the time).
        """)
    
    with col2:
        # Visualize distribution
        returns = np.linspace(-5, 5, 1000)
        prob_density = stats.norm.pdf(returns, mu, sigma)
        
        fig = go.Figure()
        
        # Full distribution
        fig.add_trace(go.Scatter(
            x=returns,
            y=prob_density,
            mode='lines',
            fill='tozeroy',
            line=dict(color='#ffcdd2', width=2),
            fillcolor='rgba(255, 205, 210, 0.3)',
            name='Return Distribution'
        ))
        
        # VaR region (left tail)
        var_threshold = mu - z_score * sigma
        tail_returns = returns[returns <= var_threshold]
        tail_density = stats.norm.pdf(tail_returns, mu, sigma)
        
        fig.add_trace(go.Scatter(
            x=tail_returns,
            y=tail_density,
            mode='lines',
            fill='tozeroy',
            line=dict(color='red', width=2),
            fillcolor='rgba(255, 0, 0, 0.5)',
            name='VaR (5% tail)'
        ))
        
        # VaR line
        fig.add_vline(x=var_threshold, line_dash="dash", line_color="yellow",
                     annotation_text=f"VaR = {var_threshold:.2f}%")
        
        fig.update_layout(
            title="Return Distribution and VaR",
            xaxis_title="Daily Return (%)",
            yaxis_title="Probability Density",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 2: Historical VaR
    st.subheader("Example 2: Historical Simulation VaR")
    
    st.markdown("""
    **Scenario:** Calculate VaR using historical returns.
    """)
    
    # Generate sample historical returns
    np.random.seed(42)
    n_days = 250
    historical_returns = np.random.normal(0.05, 1.5, n_days)
    
    # Sort returns
    sorted_returns = np.sort(historical_returns)
    
    # Find 5th percentile (95% VaR)
    var_95_idx = int(0.05 * n_days)
    var_95_return = sorted_returns[var_95_idx]
    var_95_dollar = abs(var_95_return) / 100 * portfolio_value
    
    # CVaR (average of losses beyond VaR)
    tail_returns = sorted_returns[:var_95_idx + 1]
    cvar_95_return = np.mean(tail_returns)
    cvar_95_dollar = abs(cvar_95_return) / 100 * portfolio_value
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Historical Returns Summary:**")
        
        st.code(f"""
Number of observations: {n_days}
Mean return: {np.mean(historical_returns):.3f}%
Std deviation: {np.std(historical_returns):.3f}%
Min return: {np.min(historical_returns):.3f}%
Max return: {np.max(historical_returns):.3f}%
        """)
        
        st.markdown("**VaR Calculation:**")
        
        st.code(f"""
Step 1: Sort returns worst to best

Step 2: Find 5th percentile
Position = 5% × {n_days} = {var_95_idx + 1}

Step 3: VaR (95%)
{var_95_idx + 1}th worst return = {var_95_return:.3f}%
VaR (dollar) = ${var_95_dollar:,.2f}
        """)
        
        st.metric("95% VaR (Historical)", f"${var_95_dollar:,.2f}")
        st.metric("95% CVaR", f"${cvar_95_dollar:,.2f}")
        
        st.warning(f"""
        **CVaR Interpretation:**
        
        When losses exceed VaR (worst 5% of days),
        the average loss is ${cvar_95_dollar:,.2f}.
        
        This is {cvar_95_dollar/var_95_dollar:.2f}x worse than VaR threshold.
        """)
    
    with col2:
        # Histogram of returns
        fig = go.Figure()
        
        fig.add_trace(go.Histogram(
            x=historical_returns,
            nbinsx=30,
            marker_color='#ffcdd2',
            opacity=0.7,
            name='Returns'
        ))
        
        # VaR line
        fig.add_vline(x=var_95_return, line_dash="dash", line_color="red",
                     annotation_text=f"95% VaR: {var_95_return:.2f}%")
        
        # CVaR line
        fig.add_vline(x=cvar_95_return, line_dash="dot", line_color="yellow",
                     annotation_text=f"CVaR: {cvar_95_return:.2f}%")
        
        fig.update_layout(
            title="Historical Returns Distribution",
            xaxis_title="Daily Return (%)",
            yaxis_title="Frequency",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 3: Stress Testing
    st.subheader("Example 3: Stress Testing Scenario")
    
    st.markdown("""
    **Scenario:** "2008-Style Financial Crisis"
    
    **Portfolio:**
    - 60% US Stocks
    - 30% Bonds
    - 10% REITs
    
    **Portfolio Value:** $10,000,000
    """)
    
    # Portfolio composition
    positions = {
        'Asset': ['US Stocks', 'Bonds', 'REITs'],
        'Current Value ($M)': [6.0, 3.0, 1.0],
        'Weight (%)': [60, 30, 10],
        'Normal Scenario (%)': [-5, 2, -3],
        'Crisis Scenario (%)': [-35, 10, -45]
    }
    
    df_stress = pd.DataFrame(positions)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.table(df_stress)
        
        # Calculate losses
        normal_loss = sum(
            df_stress['Current Value ($M)'] * df_stress['Normal Scenario (%)'] / 100
        )
        
        crisis_loss = sum(
            df_stress['Current Value ($M)'] * df_stress['Crisis Scenario (%)'] / 100
        )
        
        st.markdown("**Results:**")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.metric("Normal Scenario Loss", f"${abs(normal_loss):.2f}M")
            st.metric("% of Portfolio", f"{abs(normal_loss)/10*100:.1f}%")
        
        with col_b:
            st.metric("Crisis Scenario Loss", f"${abs(crisis_loss):.2f}M", delta_color="inverse")
            st.metric("% of Portfolio", f"{abs(crisis_loss)/10*100:.1f}%")
        
        multiplier = abs(crisis_loss) / abs(normal_loss)
        
        st.error(f"""
        **Crisis Impact:**
        
        Loss is {multiplier:.1f}x worse than normal scenario!
        
        **Key Risks Identified:**
        - Heavy concentration in equities
        - REITs hit hardest (-45%)
        - Bonds provide some protection
        """)
    
    with col2:
        # Visualize scenario impact
        scenarios = ['Normal', 'Crisis']
        
        fig = go.Figure()
        
        for i, asset in enumerate(df_stress['Asset']):
            fig.add_trace(go.Bar(
                name=asset,
                x=scenarios,
                y=[df_stress['Normal Scenario (%)'].iloc[i],
                   df_stress['Crisis Scenario (%)'].iloc[i]],
                text=[f"{df_stress['Normal Scenario (%)'].iloc[i]}%",
                      f"{df_stress['Crisis Scenario (%)'].iloc[i]}%"],
                textposition='auto'
            ))
        
        fig.update_layout(
            title="Scenario Comparison by Asset",
            xaxis_title="Scenario",
            yaxis_title="Return (%)",
            barmode='group',
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Risk Analytics")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["VaR Calculator", "Historical VaR Simulator", 
         "Stress Testing Tool", "Maximum Drawdown Analyzer"]
    )
    
    if exercise == "VaR Calculator":
        st.subheader("📊 Parametric VaR Calculator")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Input Parameters:**")
            
            portfolio_val = st.number_input("Portfolio Value ($):", 
                                           value=1000000, step=100000)
            
            mu_daily = st.slider("Expected Daily Return (%):", -0.5, 0.5, 0.05, 0.01)
            sigma_daily = st.slider("Daily Volatility (%):", 0.5, 5.0, 1.5, 0.1)
            confidence = st.slider("Confidence Level (%):", 90, 99, 95)
            time_horizon = st.selectbox("Time Horizon:", [1, 5, 10, 20], index=0)
            
            # Calculate VaR
            z = stats.norm.ppf(confidence / 100)
            
            # Scale for time horizon
            mu_scaled = mu_daily * time_horizon
            sigma_scaled = sigma_daily * np.sqrt(time_horizon)
            
            var_pct = -(mu_scaled - z * sigma_scaled)
            var_dollar = var_pct / 100 * portfolio_val
            
            # CVaR approximation (for normal distribution)
            pdf_at_var = stats.norm.pdf(z)
            cvar_pct = sigma_scaled * pdf_at_var / (1 - confidence/100)
            cvar_dollar = cvar_pct / 100 * portfolio_val
            
            st.markdown("**Results:**")
            
            st.metric(f"{time_horizon}-day {confidence}% VaR", f"${var_dollar:,.2f}")
            st.metric(f"{time_horizon}-day {confidence}% CVaR", f"${cvar_dollar:,.2f}")
            st.metric("VaR as % of Portfolio", f"{var_pct:.2f}%")
            
            st.info(f"""
            **Interpretation:**
            
            {confidence}% of the time, losses over {time_horizon} day(s) 
            will be less than ${var_dollar:,.2f}.
            
            In the worst {100-confidence}% of cases, average loss is ${cvar_dollar:,.2f}.
            """)
        
        with col2:
            # Visualize distribution
            returns_range = np.linspace(-10, 10, 1000)
            pdf = stats.norm.pdf(returns_range, mu_scaled, sigma_scaled)
            
            fig = go.Figure()
            
            # Full distribution
            fig.add_trace(go.Scatter(
                x=returns_range,
                y=pdf,
                mode='lines',
                fill='tozeroy',
                line=dict(color='#ffcdd2', width=2),
                fillcolor='rgba(255, 205, 210, 0.3)',
                name='Return Distribution'
            ))
            
            # VaR region
            var_threshold = mu_scaled - z * sigma_scaled
            tail = returns_range[returns_range <= var_threshold]
            tail_pdf = stats.norm.pdf(tail, mu_scaled, sigma_scaled)
            
            fig.add_trace(go.Scatter(
                x=tail,
                y=tail_pdf,
                mode='lines',
                fill='tozeroy',
                line=dict(color='red', width=2),
                fillcolor='rgba(255, 0, 0, 0.5)',
                name=f'{100-confidence}% Tail'
            ))
            
            fig.add_vline(x=var_threshold, line_dash="dash", line_color="yellow",
                         annotation_text=f"VaR: {var_threshold:.2f}%")
            
            fig.update_layout(
                title=f"{time_horizon}-Day Return Distribution",
                xaxis_title="Return (%)",
                yaxis_title="Probability Density",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif exercise == "Historical VaR Simulator":
        st.subheader("📈 Historical VaR Simulator")
        
        st.markdown("**Generate or upload historical returns:**")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            data_source = st.radio("Data source:", ["Generate Sample", "Manual Input"])
            
            if data_source == "Generate Sample":
                n_obs = st.slider("Number of observations:", 100, 1000, 250)
                dist_type = st.selectbox("Distribution:", 
                                        ["Normal", "Student-t (fat tails)", "Skewed"])
                
                np.random.seed(42)
                
                if dist_type == "Normal":
                    returns = np.random.normal(0.05, 1.5, n_obs)
                elif dist_type == "Student-t (fat tails)":
                    returns = stats.t.rvs(df=5, loc=0.05, scale=1.5, size=n_obs)
                else:  # Skewed
                    returns = stats.skewnorm.rvs(a=-5, loc=0.05, scale=1.5, size=n_obs)
            else:
                returns_input = st.text_area("Enter returns (comma-separated):", 
                                            height=150)
                if returns_input:
                    returns = np.array([float(x.strip()) for x in returns_input.split(',')])
                else:
                    returns = None
            
            if data_source == "Generate Sample" or (data_source == "Manual Input" and returns is not None):
                confidence = st.slider("Confidence Level (%):", 90, 99, 95, key="hist_conf")
                portfolio_val = st.number_input("Portfolio Value ($):", 
                                               value=1000000, step=100000, key="hist_val")
                
                # Calculate VaR
                var_percentile = (100 - confidence) / 100
                var_return = np.percentile(returns, var_percentile * 100)
                var_dollar = abs(var_return) / 100 * portfolio_val
                
                # Calculate CVaR
                tail_returns = returns[returns <= var_return]
                cvar_return = np.mean(tail_returns) if len(tail_returns) > 0 else var_return
                cvar_dollar = abs(cvar_return) / 100 * portfolio_val
                
                st.markdown("**Results:**")
                st.metric(f"{confidence}% VaR", f"${var_dollar:,.2f}")
                st.metric(f"{confidence}% CVaR", f"${cvar_dollar:,.2f}")
                st.metric("Observations", len(returns))
        
        with col2:
            if data_source == "Generate Sample" or (data_source == "Manual Input" and returns is not None):
                # Histogram
                fig = go.Figure()
                
                fig.add_trace(go.Histogram(
                    x=returns,
                    nbinsx=50,
                    marker_color='#ffcdd2',
                    opacity=0.7,
                    name='Returns'
                ))
                
                fig.add_vline(x=var_return, line_dash="dash", line_color="red",
                             annotation_text=f"VaR: {var_return:.2f}%")
                
                fig.add_vline(x=cvar_return, line_dash="dot", line_color="yellow",
                             annotation_text=f"CVaR: {cvar_return:.2f}%")
                
                fig.update_layout(
                    title="Historical Returns Distribution",
                    xaxis_title="Return (%)",
                    yaxis_title="Frequency",
                    template="plotly_dark",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
    
    elif exercise == "Stress Testing Tool":
        st.subheader("⚡ Stress Testing Tool")
        
        st.markdown("""
        Build a portfolio and test it against market stress scenarios.
        """)
        
        # Define scenarios
        scenarios = {
            '2008 Financial Crisis': {
                'US Stocks': -37,
                'Intl Stocks': -43,
                'Bonds': 5,
                'REITs': -39,
                'Commodities': -36
            },
            '2020 COVID Crash (March)': {
                'US Stocks': -34,
                'Intl Stocks': -32,
                'Bonds': 3,
                'REITs': -28,
                'Commodities': -24
            },
            'Interest Rate Shock (+3%)': {
                'US Stocks': -15,
                'Intl Stocks': -12,
                'Bonds': -20,
                'REITs': -18,
                'Commodities': -5
            },
            'Inflation Surge': {
                'US Stocks': -10,
                'Intl Stocks': -8,
                'Bonds': -15,
                'REITs': 5,
                'Commodities': 25
            }
        }
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**Build Your Portfolio:**")
            
            total_value = st.number_input("Total Portfolio Value ($M):", 
                                         value=10.0, step=1.0)
            
            weights = {}
            assets = ['US Stocks', 'Intl Stocks', 'Bonds', 'REITs', 'Commodities']
            
            for asset in assets:
                weights[asset] = st.slider(f"{asset} (%):", 0, 100, 20, 5)
            
            total_weight = sum(weights.values())
            
            if total_weight != 100:
                st.error(f"Weights sum to {total_weight}%. Must equal 100%!")
            
            scenario_name = st.selectbox("Select Stress Scenario:", 
                                        list(scenarios.keys()))
        
        with col2:
            if total_weight == 100:
                st.markdown(f"**Scenario: {scenario_name}**")
                
                scenario = scenarios[scenario_name]
                
                # Calculate impact
                results = []
                total_loss = 0
                
                for asset in assets:
                    weight = weights[asset] / 100
                    value = total_value * weight
                    scenario_return = scenario[asset] / 100
                    loss = value * scenario_return
                    total_loss += loss
                    
                    results.append({
                        'Asset': asset,
                        'Weight (%)': weights[asset],
                        'Value ($M)': value,
                        'Scenario Return (%)': scenario[asset],
                        'P&L ($M)': loss
                    })
                
                df_results = pd.DataFrame(results)
                st.dataframe(df_results.style.format({
                    'Weight (%)': '{:.0f}',
                    'Value ($M)': '{:.2f}',
                    'Scenario Return (%)': '{:.0f}',
                    'P&L ($M)': '{:.2f}'
                }))
                
                st.markdown("**Summary:**")
                
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.metric("Total P&L", f"${total_loss:.2f}M")
                with col_b:
                    st.metric("Loss %", f"{total_loss/total_value*100:.1f}%")
                
                if total_loss < -3:
                    st.error(f"⚠️ Severe loss: ${abs(total_loss):.2f}M!")
                elif total_loss < -1:
                    st.warning(f"⚠️ Moderate loss: ${abs(total_loss):.2f}M")
                elif total_loss < 0:
                    st.info(f"Minor loss: ${abs(total_loss):.2f}M")
                else:
                    st.success(f"Gain: ${total_loss:.2f}M")
    
    elif exercise == "Maximum Drawdown Analyzer":
        st.subheader("📉 Maximum Drawdown Analyzer")
        
        st.markdown("**Generate a portfolio value time series:**")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            n_periods = st.slider("Number of periods:", 50, 500, 200)
            drift = st.slider("Drift (%):", -0.5, 1.0, 0.05, 0.05)
            volatility = st.slider("Volatility (%):", 0.5, 5.0, 2.0, 0.1)
            initial_value = st.number_input("Initial Value ($):", value=1000000)
            
            # Generate returns
            np.random.seed(42)
            returns = np.random.normal(drift, volatility, n_periods)
            
            # Calculate cumulative portfolio value
            portfolio_value = initial_value * np.exp(np.cumsum(returns / 100))
            
            # Calculate drawdown
            running_max = np.maximum.accumulate(portfolio_value)
            drawdown = (portfolio_value - running_max) / running_max * 100
            
            # Find max drawdown
            max_dd = np.min(drawdown)
            max_dd_idx = np.argmin(drawdown)
            
            # Find peak before max dd
            peak_idx = np.argmax(portfolio_value[:max_dd_idx+1])
            peak_value = portfolio_value[peak_idx]
            trough_value = portfolio_value[max_dd_idx]
            
            st.markdown("**Results:**")
            st.metric("Maximum Drawdown", f"{abs(max_dd):.2f}%")
            st.metric("Peak Value", f"${peak_value:,.0f}")
            st.metric("Trough Value", f"${trough_value:,.0f}")
            st.metric("Recovery Time", f"{n_periods - max_dd_idx} periods")
            
            st.warning(f"""
            **Analysis:**
            
            The portfolio experienced its worst drawdown of 
            {abs(max_dd):.1f}% from peak to trough.
            
            Peak at period {peak_idx}, trough at period {max_dd_idx}.
            """)
        
        with col2:
            # Plot portfolio value and drawdown
            fig = go.Figure()
            
            # Portfolio value
            fig.add_trace(go.Scatter(
                y=portfolio_value,
                mode='lines',
                name='Portfolio Value',
                line=dict(color='#ffcdd2', width=2),
                yaxis='y'
            ))
            
            # Running max
            fig.add_trace(go.Scatter(
                y=running_max,
                mode='lines',
                name='Running Max',
                line=dict(color='yellow', width=1, dash='dash'),
                yaxis='y'
            ))
            
            # Drawdown
            fig.add_trace(go.Scatter(
                y=drawdown,
                mode='lines',
                name='Drawdown (%)',
                line=dict(color='red', width=2),
                fill='tozeroy',
                fillcolor='rgba(255, 0, 0, 0.3)',
                yaxis='y2'
            ))
            
            fig.update_layout(
                title="Portfolio Value and Drawdown",
                xaxis_title="Time Period",
                yaxis=dict(title="Portfolio Value ($)"),
                yaxis2=dict(
                    title="Drawdown (%)",
                    overlaying='y',
                    side='right'
                ),
                template="plotly_dark",
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Risk Analytics Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["VaR Calculator", "CVaR Calculator", "VaR Scaling", "Drawdown Calculator"]
    )
    
    if calc_type == "VaR Calculator":
        st.subheader("Value at Risk (VaR) Calculator")
        
        method = st.radio("Select Method:", ["Parametric", "Historical"])
        
        if method == "Parametric":
            col1, col2 = st.columns(2)
            
            with col1:
                portfolio_val = st.number_input("Portfolio Value ($):", value=1000000)
                mu = st.number_input("Expected Return (%):", value=0.05, format="%.3f")
                sigma = st.number_input("Volatility (%):", value=1.5)
                confidence = st.selectbox("Confidence Level:", [90, 95, 99])
                
                if st.button("Calculate VaR"):
                    z = stats.norm.ppf(confidence / 100)
                    var_pct = -(mu - z * sigma)
                    var_dollar = var_pct / 100 * portfolio_val
                    
                    st.markdown("**Results:**")
                    st.metric(f"{confidence}% VaR", f"${var_dollar:,.2f}")
                    st.metric("VaR (%)", f"{var_pct:.3f}%")
                    
                    st.success(f"""
                    {confidence}% of the time, losses will be less than ${var_dollar:,.2f}
                    """)
            
            with col2:
                st.info("""
                **Parametric VaR Formula:**
                
                VaR = -(μ - z_α × σ) × Portfolio Value
                
                **z-scores:**
                - 90%: 1.282
                - 95%: 1.645
                - 99%: 2.326
                
                **Assumptions:**
                - Normal distribution
                - Constant volatility
                - Linear positions
                """)
    
    elif calc_type == "VaR Scaling":
        st.subheader("VaR Time Horizon Scaling")
        
        st.markdown("""
        Scale VaR from one time horizon to another using the square root of time rule.
        
        **Formula:** VaR(T days) = VaR(1 day) × √T
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            var_1day = st.number_input("1-Day VaR ($):", value=100000, step=10000)
            target_days = st.selectbox("Target Horizon (days):", [5, 10, 20, 252])
            
            if st.button("Scale VaR"):
                var_scaled = var_1day * np.sqrt(target_days)
                
                st.metric(f"{target_days}-Day VaR", f"${var_scaled:,.2f}")
                
                scaling_factor = np.sqrt(target_days)
                st.info(f"Scaling factor: √{target_days} = {scaling_factor:.3f}")
                
                # Show scaling for multiple horizons
                st.markdown("**VaR at Different Horizons:**")
                
                horizons = [1, 5, 10, 20, 252]
                scaled_vars = [var_1day * np.sqrt(h) for h in horizons]
                
                df_scaling = pd.DataFrame({
                    'Horizon (days)': horizons,
                    'VaR ($)': scaled_vars,
                    'Scaling Factor': [np.sqrt(h) for h in horizons]
                })
                
                st.table(df_scaling.style.format({
                    'VaR ($)': '${:,.0f}',
                    'Scaling Factor': '{:.3f}'
                }))
        
        with col2:
            st.warning("""
            **Important Notes:**
            
            **Square Root Rule Assumptions:**
            - Returns are independent
            - Constant volatility
            - Normal distribution
            
            **When it Breaks Down:**
            - Mean reversion
            - Volatility clustering
            - Autocorrelation
            
            **Better for:**
            - Short horizons (1-20 days)
            - Liquid markets
            - Quick estimates
            
            **Use with caution for:**
            - Long horizons (> 1 month)
            - Volatile periods
            - Illiquid assets
            """)

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 7 Quiz: Risk Analytics")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': '1-day 95% VaR of $100,000 means:',
            'options': [
                'Average daily loss is $100,000',
                'Maximum possible loss is $100,000',
                '95% of days, loss will be less than $100,000',
                'Expected loss is $100,000'
            ],
            'correct': '95% of days, loss will be less than $100,000',
            'explanation': 'VaR is a threshold - losses exceed it only 5% of the time at 95% confidence.'
        },
        {
            'id': 2,
            'question': 'CVaR (Expected Shortfall) is:',
            'options': [
                'Always equal to VaR',
                'Always less than VaR',
                'Average loss when loss exceeds VaR',
                'Maximum possible loss'
            ],
            'correct': 'Average loss when loss exceeds VaR',
            'explanation': 'CVaR measures the expected loss in the tail beyond VaR, so CVaR ≥ VaR.'
        },
        {
            'id': 3,
            'question': 'Parametric VaR assumes returns follow:',
            'options': [
                'Uniform distribution',
                'Normal distribution',
                'Exponential distribution',
                'No distribution assumption'
            ],
            'correct': 'Normal distribution',
            'explanation': 'Parametric VaR uses normal distribution assumption, which can underestimate tail risk.'
        },
        {
            'id': 4,
            'question': 'Historical VaR advantage over Parametric VaR:',
            'options': [
                'Faster to calculate',
                'No distribution assumption needed',
                'Always more accurate',
                'Requires less data'
            ],
            'correct': 'No distribution assumption needed',
            'explanation': 'Historical VaR uses actual historical returns without assuming a specific distribution.'
        },
        {
            'id': 5,
            'question': 'To scale 1-day VaR to 10-day VaR, multiply by:',
            'options': [
                '10',
                '√10',
                '10²',
                'log(10)'
            ],
            'correct': '√10',
            'explanation': 'Square root of time rule: VaR(T days) = VaR(1 day) × √T'
        },
        {
            'id': 6,
            'question': 'Maximum Drawdown measures:',
            'options': [
                'Average loss',
                'Largest peak-to-trough decline',
                'Daily volatility',
                'Expected shortfall'
            ],
            'correct': 'Largest peak-to-trough decline',
            'explanation': 'MDD is the largest historical decline from a peak to subsequent trough.'
        },
        {
            'id': 7,
            'question': 'Stress testing is useful because:',
            'options': [
                'It replaces VaR completely',
                'It tests portfolio under extreme scenarios',
                'It assumes normal markets',
                'It requires no historical data'
            ],
            'correct': 'It tests portfolio under extreme scenarios',
            'explanation': 'Stress testing examines portfolio behavior under extreme but plausible scenarios.'
        },
        {
            'id': 8,
            'question': 'Basel III requires banks to use VaR with:',
            'options': [
                '95% confidence, 1-day horizon',
                '99% confidence, 10-day horizon',
                '90% confidence, 5-day horizon',
                '99.9% confidence, 1-day horizon'
            ],
            'correct': '99% confidence, 10-day horizon',
            'explanation': 'Basel III mandates 99% confidence and 10-day holding period for regulatory capital.'
        },
        {
            'id': 9,
            'question': 'Component VaR shows:',
            'options': [
                'Total portfolio VaR',
                'Each position\'s contribution to portfolio VaR',
                'VaR of individual positions',
                'Historical losses'
            ],
            'correct': 'Each position\'s contribution to portfolio VaR',
            'explanation': 'Component VaR decomposes total portfolio VaR into contributions from each position.'
        },
        {
            'id': 10,
            'question': 'A main limitation of VaR is:',
            'options': [
                'Too complex to calculate',
                'Requires too much data',
                'Doesn\'t indicate severity of tail losses',
                'Only works for stocks'
            ],
            'correct': 'Doesn\'t indicate severity of tail losses',
            'explanation': 'VaR only shows the threshold; it doesn\'t tell you how bad losses beyond VaR could be.'
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
    st.header("Module 7 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Value at Risk (VaR)**
        - Maximum expected loss
        - Confidence level + time horizon
        - 3 methods: Parametric, Historical, Monte Carlo
        - Widely used but has limitations
        """)
        
        st.success("""
        **Stress Testing**
        - Tests extreme scenarios
        - Historical or hypothetical
        - Complements VaR
        - Identifies vulnerabilities
        """)
    
    with col2:
        st.warning("""
        **CVaR / Expected Shortfall**
        - Average loss beyond VaR
        - Better tail risk measure
        - Coherent risk measure
        - Preferred by regulators
        """)
        
        st.info("""
        **Other Risk Metrics**
        - Maximum Drawdown
        - Component VaR
        - Marginal VaR
        - Risk-adjusted returns
        """)
    
    st.markdown("---")
    st.subheader("📐 Essential Formulas")
    
    formulas_df = pd.DataFrame({
        'Metric': ['Parametric VaR', 'CVaR', 'VaR Scaling', 'Max Drawdown', 'Component VaR'],
        'Formula': [
            'VaR = -(μ - z_α × σ) × V',
            'E[Loss | Loss > VaR]',
            'VaR_T = VaR_1 × √T',
            'max(Peak - Trough) / Peak',
            'β_i × VaR_portfolio'
        ]
    })
    st.table(formulas_df)
    
    st.markdown("---")
    st.subheader("💼 Practical Applications")
    
    tab1, tab2, tab3 = st.tabs(["Risk Management", "Regulatory", "Portfolio Management"])
    
    with tab1:
        st.markdown("""
        **Daily Risk Management:**
        
        1. **VaR Monitoring**
           - Calculate daily VaR
           - Compare to limits
           - Escalate breaches
        
        2. **Stress Testing**
           - Weekly stress tests
           - Multiple scenarios
           - Action thresholds
        
        3. **Risk Reporting**
           - Dashboard for management
           - Trend analysis
           - Attribution
        
        4. **Position Limits**
           - VaR-based limits
           - Concentration limits
           - Stop-loss rules
        """)
    
    with tab2:
        st.markdown("""
        **Regulatory Requirements:**
        
        1. **Basel III Market Risk**
           - 99% confidence
           - 10-day horizon
           - Backtesting required
           - Capital multiplier
        
        2. **SEC Regulations**
           - Risk disclosures
           - VaR reporting
           - Stress test results
        
        3. **Internal Models**
           - Model approval process
           - Independent validation
           - Documentation
           - Governance
        
        4. **Capital Requirements**
           - Risk-weighted assets
           - Capital ratios
           - Buffer requirements
        """)
    
    with tab3:
        st.markdown("""
        **Portfolio Applications:**
        
        1. **Risk Budgeting**
           - Allocate VaR across strategies
           - Risk-return optimization
           - Diversification benefits
        
        2. **Performance Attribution**
           - Risk-adjusted returns
           - Component VaR analysis
           - Source of risk/return
        
        3. **Rebalancing**
           - Risk-based triggers
           - Maintain VaR targets
           - Opportunistic adjustments
        
        4. **Hedge Decisions**
           - Tail risk protection
           - Cost-benefit analysis
           - Scenario hedging
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 8?**
    
    Module 8: Advanced Statistical Methods covers:
    - Principal Component Analysis (PCA)
    - Non-parametric methods
    - Bayesian statistics
    - Advanced techniques
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #ffebee; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 7 of 12: Risk Analytics</p>
</div>
""", unsafe_allow_html=True)