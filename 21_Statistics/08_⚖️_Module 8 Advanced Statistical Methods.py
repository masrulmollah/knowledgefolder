import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #4a148c 0%, #6a1b9a 50%, #7b1fa2 100%);
    }
    h1 {
        color: #e1bee7;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #ce93d8;
        border-left: 6px solid #e1bee7;
        padding-left: 15px;
    }
    h3 {
        color: #f3e5f5;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>🔬 Module 8: Advanced Statistical Methods</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #f3e5f5;'>Beyond Basic Statistics</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 8 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("8.1 Principal Component Analysis (PCA)")
    
    st.subheader("What is PCA?")
    
    st.warning("""
    **Principal Component Analysis:**
    
    A dimensionality reduction technique that transforms correlated variables 
    into a smaller set of uncorrelated variables called principal components.
    
    **Key Idea:**
    Find new axes that capture maximum variance in the data.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Why Use PCA?**
        
        1. **Reduce Dimensionality**
           - 100 stocks → 5-10 factors
           - Simplify complex data
           - Remove noise
        
        2. **Identify Risk Factors**
           - Market factor
           - Sector factors
           - Style factors
        
        3. **Portfolio Construction**
           - Factor-based investing
           - Risk decomposition
           - Diversification
        
        4. **Multicollinearity**
           - Remove correlation
           - Improve regression
           - Better predictions
        """)
    
    with col2:
        st.success("""
        **How PCA Works:**
        
        **Step 1:** Standardize the data
        - Mean = 0, Std = 1
        
        **Step 2:** Calculate covariance matrix
        - Shows relationships
        
        **Step 3:** Find eigenvectors & eigenvalues
        - Eigenvectors = Principal components
        - Eigenvalues = Variance explained
        
        **Step 4:** Sort by variance explained
        - PC1 explains most variance
        - PC2 explains second most
        - And so on...
        
        **Step 5:** Select top components
        - Keep 80-90% of variance
        - Reduce dimensions
        """)
    
    st.markdown("---")
    
    st.subheader("Mathematical Foundation")
    
    st.latex(r"X = T \times P^T + E")
    
    st.markdown("""
    **Where:**
    - X: Original data matrix (n × p)
    - T: Scores matrix (n × k)
    - P: Loadings matrix (p × k)
    - E: Residuals
    - k: Number of components (k < p)
    """)
    
    st.info("""
    **Variance Explained:**
    """)
    
    st.latex(r"\text{Variance Explained by PC}_i = \frac{\lambda_i}{\sum_{j=1}^{p} \lambda_j}")
    
    st.markdown("""
    Where λᵢ is the i-th eigenvalue
    """)
    
    st.markdown("---")
    
    st.subheader("PCA in Finance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Applications:**
        
        **1. Factor Models**
        - Extract market factors
        - Industry factors
        - Style factors (value, growth)
        
        **2. Yield Curve Analysis**
        - Level (parallel shift)
        - Slope (steepening/flattening)
        - Curvature (butterfly)
        - 3 PCs explain 95%+ of variance
        
        **3. Risk Management**
        - Portfolio risk attribution
        - Stress testing
        - Scenario analysis
        """)
    
    with col2:
        st.success("""
        **Interpretation:**
        
        **PC1 (First Component):**
        - Usually "market factor"
        - Explains 40-60% of variance
        - All stocks load positively
        
        **PC2 (Second Component):**
        - Often sector or style factor
        - Explains 10-20% of variance
        - Mixed signs in loadings
        
        **PC3+ (Higher Components):**
        - Specific factors
        - Less variance explained
        - More noise
        """)
    
    st.markdown("---")
    
    # Non-parametric Methods
    st.header("8.2 Non-Parametric Methods")
    
    st.subheader("What are Non-Parametric Methods?")
    
    st.info("""
    **Non-Parametric Statistics:**
    
    Methods that don't assume a specific distribution for the data.
    
    **Why "Non-Parametric"?**
    - No assumption about parameters (μ, σ)
    - No assumed distribution (normal, t, etc.)
    - Distribution-free methods
    
    **When to Use:**
    - Non-normal data
    - Outliers present
    - Small samples
    - Ordinal data
    - Robust alternatives needed
    """)
    
    st.markdown("---")
    
    st.subheader("Key Non-Parametric Tests")
    
    # Mann-Whitney U Test
    st.markdown("### 1. Mann-Whitney U Test")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Purpose:**
        Compare two independent groups
        
        **Non-parametric alternative to:**
        Independent samples t-test
        
        **How it works:**
        1. Rank all observations
        2. Sum ranks for each group
        3. Calculate U statistic
        4. Test if ranks differ
        
        **Hypothesis:**
        - H₀: Distributions are equal
        - H₁: Distributions differ
        """)
    
    with col2:
        st.success("""
        **Financial Applications:**
        
        - Compare returns: Strategy A vs B
        - Performance: Before vs After
        - Market regimes: Bull vs Bear
        - Asset classes: Stocks vs Bonds
        
        **Advantages:**
        - Robust to outliers
        - No normality assumption
        - Works with small samples
        
        **Disadvantages:**
        - Less powerful if data is normal
        - Loses some information (uses ranks)
        """)
    
    st.markdown("---")
    
    # Kruskal-Wallis Test
    st.markdown("### 2. Kruskal-Wallis Test")
    
    st.warning("""
    **Purpose:**
    Compare three or more independent groups
    
    **Non-parametric alternative to:**
    One-way ANOVA
    
    **Example:**
    Compare returns across multiple sectors (Tech, Finance, Healthcare, Energy)
    
    **When to use:**
    - More than 2 groups
    - Non-normal distributions
    - Unequal variances
    - Presence of outliers
    """)
    
    st.markdown("---")
    
    # Wilcoxon Signed-Rank Test
    st.markdown("### 3. Wilcoxon Signed-Rank Test")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Purpose:**
        Compare paired/matched samples
        
        **Non-parametric alternative to:**
        Paired t-test
        
        **How it works:**
        1. Calculate differences
        2. Rank absolute differences
        3. Assign signs
        4. Sum positive and negative ranks
        
        **Financial Use Cases:**
        - Before/after analysis
        - Matched pairs trading
        - Event studies
        """)
    
    with col2:
        st.success("""
        **Example:**
        Test if a trading strategy improves returns
        
        **Data:**
        - Same stocks before and after strategy
        - Paired observations
        - Non-normal differences
        
        **Advantages:**
        - Handles asymmetry
        - Robust to outliers
        - Uses magnitude and direction
        
        **Better than sign test:**
        - Considers size of differences
        - More powerful
        """)
    
    st.markdown("---")
    
    # Spearman Correlation
    st.markdown("### 4. Spearman Rank Correlation")
    
    st.latex(r"\rho_s = 1 - \frac{6\sum d_i^2}{n(n^2-1)}")
    
    st.info("""
    **Spearman's ρ (rho):**
    
    Non-parametric measure of correlation based on ranks
    
    **vs Pearson Correlation:**
    - Pearson: Measures linear relationship
    - Spearman: Measures monotonic relationship
    
    **When Spearman is better:**
    - Non-linear relationships
    - Ordinal data
    - Outliers present
    - Non-normal distributions
    
    **Financial Application:**
    - Ranking stocks by multiple criteria
    - Credit ratings (ordinal)
    - Portfolio rankings
    - Factor exposure ranks
    """)
    
    st.markdown("---")
    
    # Bayesian Statistics
    st.header("8.3 Bayesian Statistics")
    
    st.subheader("Bayesian vs Frequentist")
    
    comparison_df = pd.DataFrame({
        'Aspect': ['View of Probability', 'Parameters', 'Inference', 'Prior Knowledge', 'Uncertainty'],
        'Frequentist': [
            'Long-run frequency',
            'Fixed but unknown',
            'Confidence intervals',
            'Not incorporated',
            'Via confidence intervals'
        ],
        'Bayesian': [
            'Degree of belief',
            'Random variables with distributions',
            'Credible intervals',
            'Incorporated via priors',
            'Via posterior distributions'
        ]
    })
    
    st.table(comparison_df)
    
    st.markdown("---")
    
    st.subheader("Bayes' Theorem (Revisited)")
    
    st.latex(r"P(\theta|Data) = \frac{P(Data|\theta) \times P(\theta)}{P(Data)}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Components:**
        
        **Posterior:** P(θ|Data)
        - What we want to know
        - Updated belief after seeing data
        - Combines prior and likelihood
        
        **Likelihood:** P(Data|θ)
        - Probability of observing data given parameter
        - Information from data
        
        **Prior:** P(θ)
        - Initial belief before data
        - Can be informative or uninformative
        
        **Evidence:** P(Data)
        - Normalizing constant
        - Ensures posterior sums to 1
        """)
    
    with col2:
        st.success("""
        **Bayesian Workflow:**
        
        **Step 1: Choose Prior**
        - Expert opinion
        - Historical data
        - Uninformative (if no knowledge)
        
        **Step 2: Observe Data**
        - Collect new information
        - Market data, returns, etc.
        
        **Step 3: Calculate Likelihood**
        - P(Data|θ) for different θ values
        
        **Step 4: Update to Posterior**
        - Combine prior and likelihood
        - New belief distribution
        
        **Step 5: Make Decisions**
        - Use posterior for inference
        - Update as new data arrives
        """)
    
    st.markdown("---")
    
    st.subheader("Bayesian Methods in Finance")
    
    st.warning("""
    **Applications:**
    
    **1. Portfolio Optimization**
    - Black-Litterman model
    - Incorporates views and confidence
    - Shrinkage estimators
    
    **2. Risk Management**
    - Updating VaR estimates
    - Credit risk models
    - Operational risk
    
    **3. Asset Pricing**
    - Parameter uncertainty
    - Model averaging
    - Regime switching
    
    **4. Algorithmic Trading**
    - Online learning
    - Sequential decision making
    - Adaptive strategies
    """)
    
    st.markdown("---")
    
    # Bootstrap
    st.header("8.4 Bootstrap Methods")
    
    st.subheader("What is Bootstrap?")
    
    st.info("""
    **Bootstrap:**
    
    A resampling method that estimates the sampling distribution of a statistic 
    by repeatedly sampling from the data with replacement.
    
    **Key Idea:**
    "The data is the best estimate of the population"
    
    **Process:**
    1. Take original sample (n observations)
    2. Resample with replacement (n observations)
    3. Calculate statistic (mean, median, etc.)
    4. Repeat 1,000-10,000 times
    5. Examine distribution of statistic
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Why Bootstrap?**
        
        **Advantages:**
        - No distributional assumptions
        - Works for complex statistics
        - Estimates confidence intervals
        - Assesses uncertainty
        
        **When to Use:**
        - Unknown sampling distribution
        - Complex statistics (Sharpe ratio, VaR)
        - Small samples
        - Non-normal data
        
        **Not Magic:**
        - Can't create information
        - Assumes sample is representative
        - Computational cost
        """)
    
    with col2:
        st.warning("""
        **Financial Applications:**
        
        **1. Confidence Intervals**
        - Sharpe ratio CI
        - VaR confidence bands
        - Parameter estimates
        
        **2. Hypothesis Testing**
        - Non-parametric tests
        - Strategy comparison
        
        **3. Model Validation**
        - Cross-validation
        - Out-of-sample testing
        - Backtesting
        
        **4. Risk Metrics**
        - Bootstrap VaR
        - Expected shortfall
        - Tail risk measures
        """)
    
    st.markdown("---")
    
    # Machine Learning Preview
    st.header("8.5 Advanced Techniques Overview")
    
    st.subheader("Modern Methods in Finance")
    
    techniques = pd.DataFrame({
        'Method': [
            'PCA',
            'Factor Analysis',
            'Cluster Analysis',
            'LASSO Regression',
            'Ridge Regression',
            'Random Forests',
            'Neural Networks',
            'Support Vector Machines'
        ],
        'Type': [
            'Dimensionality Reduction',
            'Dimensionality Reduction',
            'Unsupervised Learning',
            'Regularization',
            'Regularization',
            'Ensemble Learning',
            'Deep Learning',
            'Classification/Regression'
        ],
        'Use Case': [
            'Factor extraction, risk decomposition',
            'Hidden factors, latent variables',
            'Portfolio segmentation, regime detection',
            'Feature selection, sparse models',
            'Multicollinearity, overfitting prevention',
            'Return prediction, risk modeling',
            'Complex patterns, alternative data',
            'Binary outcomes, default prediction'
        ]
    })
    
    st.table(techniques)
    
    st.info("""
    **Note:** Machine Learning methods are covered in detail in Module 9.
    
    These advanced techniques complement traditional statistical methods and 
    are increasingly important in modern finance.
    """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Advanced Methods Examples")
    
    # Example 1: PCA
    st.subheader("Example 1: PCA on Stock Returns")
    
    st.markdown("""
    **Scenario:** Apply PCA to identify key factors driving stock returns.
    """)
    
    # Generate sample data
    np.random.seed(42)
    n_stocks = 10
    n_days = 250
    
    # Create correlated returns (market factor + noise)
    market_factor = np.random.normal(0.05, 1.5, n_days)
    
    returns_data = {}
    for i in range(n_stocks):
        beta = 0.5 + np.random.random() * 1.0  # Beta between 0.5 and 1.5
        stock_return = beta * market_factor + np.random.normal(0, 1, n_days)
        returns_data[f'Stock_{i+1}'] = stock_return
    
    df_returns = pd.DataFrame(returns_data)
    
    # Standardize
    scaler = StandardScaler()
    returns_scaled = scaler.fit_transform(df_returns)
    
    # Apply PCA
    pca = PCA()
    pca.fit(returns_scaled)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Sample Data (First 10 Days):**")
        st.dataframe(df_returns.head(10).style.format("{:.2f}"))
        
        st.markdown("**PCA Results:**")
        
        # Variance explained
        var_explained = pca.explained_variance_ratio_ * 100
        cumvar_explained = np.cumsum(var_explained)
        
        pca_results = pd.DataFrame({
            'Component': [f'PC{i+1}' for i in range(len(var_explained))],
            'Variance (%)': var_explained,
            'Cumulative (%)': cumvar_explained
        })
        
        st.dataframe(pca_results.style.format({
            'Variance (%)': '{:.2f}',
            'Cumulative (%)': '{:.2f}'
        }))
        
        st.success(f"""
        **Key Findings:**
        
        - PC1 explains {var_explained[0]:.1f}% of variance
        - First 3 PCs explain {cumvar_explained[2]:.1f}% of variance
        - Reduced from {n_stocks} stocks to 3 factors
        - 10x dimensionality reduction!
        """)
    
    with col2:
        # Scree plot
        fig1 = go.Figure()
        
        fig1.add_trace(go.Bar(
            x=[f'PC{i+1}' for i in range(n_stocks)],
            y=var_explained,
            marker_color='#e1bee7',
            name='Variance Explained'
        ))
        
        fig1.add_trace(go.Scatter(
            x=[f'PC{i+1}' for i in range(n_stocks)],
            y=cumvar_explained,
            mode='lines+markers',
            line=dict(color='yellow', width=3),
            marker=dict(size=10),
            name='Cumulative',
            yaxis='y2'
        ))
        
        fig1.update_layout(
            title="Scree Plot - Variance Explained",
            xaxis_title="Principal Component",
            yaxis_title="Variance Explained (%)",
            yaxis2=dict(
                title="Cumulative (%)",
                overlaying='y',
                side='right'
            ),
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # Loadings for PC1
        loadings_pc1 = pca.components_[0]
        
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=[f'Stock_{i+1}' for i in range(n_stocks)],
            y=loadings_pc1,
            marker_color='#ce93d8'
        ))
        
        fig2.update_layout(
            title="PC1 Loadings (Market Factor)",
            xaxis_title="Stock",
            yaxis_title="Loading",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        st.info("""
        **Interpretation:**
        - All stocks load positively on PC1
        - PC1 represents market-wide movement
        - Similar to "market factor" in factor models
        """)
    
    st.markdown("---")
    
    # Example 2: Non-Parametric Test
    st.subheader("Example 2: Mann-Whitney U Test")
    
    st.markdown("""
    **Scenario:** Compare returns of two trading strategies.
    
    **Data:** Non-normally distributed returns
    """)
    
    # Generate sample data
    np.random.seed(42)
    
    # Strategy A: Normal returns
    strategy_a = np.random.normal(0.5, 2, 50)
    
    # Strategy B: Higher median but with outliers
    strategy_b_base = np.random.normal(0.8, 1.5, 45)
    strategy_b_outliers = np.random.choice([-10, 15], 5)
    strategy_b = np.concatenate([strategy_b_base, strategy_b_outliers])
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Descriptive statistics
        st.markdown("**Descriptive Statistics:**")
        
        stats_df = pd.DataFrame({
            'Metric': ['Mean', 'Median', 'Std Dev', 'Min', 'Max'],
            'Strategy A': [
                np.mean(strategy_a),
                np.median(strategy_a),
                np.std(strategy_a),
                np.min(strategy_a),
                np.max(strategy_a)
            ],
            'Strategy B': [
                np.mean(strategy_b),
                np.median(strategy_b),
                np.std(strategy_b),
                np.min(strategy_b),
                np.max(strategy_b)
            ]
        })
        
        st.table(stats_df.style.format({
            'Strategy A': '{:.2f}',
            'Strategy B': '{:.2f}'
        }))
        
        # Mann-Whitney U test
        statistic, p_value = stats.mannwhitneyu(strategy_a, strategy_b, alternative='two-sided')
        
        st.markdown("**Mann-Whitney U Test:**")
        st.code(f"""
U-statistic: {statistic:.2f}
p-value: {p_value:.4f}

H₀: Distributions are equal
H₁: Distributions differ
α = 0.05
        """)
        
        if p_value < 0.05:
            st.success(f"""
            ✅ **Reject H₀** (p = {p_value:.4f} < 0.05)
            
            Strategies have significantly different distributions.
            Despite outliers, test detects difference.
            """)
        else:
            st.info(f"""
            ❌ **Fail to Reject H₀** (p = {p_value:.4f} ≥ 0.05)
            
            No significant difference detected.
            """)
    
    with col2:
        # Box plots
        fig = go.Figure()
        
        fig.add_trace(go.Box(
            y=strategy_a,
            name='Strategy A',
            marker_color='#e1bee7',
            boxmean='sd'
        ))
        
        fig.add_trace(go.Box(
            y=strategy_b,
            name='Strategy B',
            marker_color='#ce93d8',
            boxmean='sd'
        ))
        
        fig.update_layout(
            title="Strategy Returns Comparison",
            yaxis_title="Returns (%)",
            template="plotly_dark",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.warning("""
        **Why Mann-Whitney?**
        
        - Strategy B has outliers
        - Non-normal distributions
        - Robust to extreme values
        - Better than t-test here
        
        **Note:**
        t-test might be misleading due to outliers
        """)
    
    st.markdown("---")
    
    # Example 3: Bootstrap
    st.subheader("Example 3: Bootstrap Confidence Interval for Sharpe Ratio")
    
    st.markdown("""
    **Scenario:** Estimate confidence interval for Sharpe ratio using bootstrap.
    
    **Challenge:** Sharpe ratio's sampling distribution is complex and unknown.
    """)
    
    # Generate returns
    np.random.seed(42)
    returns = np.random.normal(0.8, 2, 100)
    risk_free = 0.3
    
    # Calculate Sharpe ratio
    sharpe_actual = (np.mean(returns) - risk_free) / np.std(returns, ddof=1)
    
    # Bootstrap
    n_bootstrap = 1000
    sharpe_bootstrap = []
    
    np.random.seed(42)
    for _ in range(n_bootstrap):
        # Resample with replacement
        bootstrap_sample = np.random.choice(returns, size=len(returns), replace=True)
        sharpe_boot = (np.mean(bootstrap_sample) - risk_free) / np.std(bootstrap_sample, ddof=1)
        sharpe_bootstrap.append(sharpe_boot)
    
    sharpe_bootstrap = np.array(sharpe_bootstrap)
    
    # Calculate confidence intervals
    ci_lower = np.percentile(sharpe_bootstrap, 2.5)
    ci_upper = np.percentile(sharpe_bootstrap, 97.5)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Bootstrap Parameters:**")
        st.code(f"""
Sample Size: {len(returns)}
Bootstrap Iterations: {n_bootstrap}
Risk-Free Rate: {risk_free}%
        """)
        
        st.markdown("**Results:**")
        st.metric("Observed Sharpe Ratio", f"{sharpe_actual:.4f}")
        st.metric("Bootstrap Mean", f"{np.mean(sharpe_bootstrap):.4f}")
        st.metric("Bootstrap Std Dev", f"{np.std(sharpe_bootstrap):.4f}")
        
        st.success(f"""
        **95% Confidence Interval:**
        
        [{ci_lower:.4f}, {ci_upper:.4f}]
        
        **Interpretation:**
        We are 95% confident the true Sharpe ratio 
        lies between {ci_lower:.3f} and {ci_upper:.3f}.
        """)
        
        st.info("""
        **Why Bootstrap?**
        - Sharpe ratio distribution is complex
        - No simple analytical formula for CI
        - Bootstrap provides empirical distribution
        - No normality assumption needed
        """)
    
    with col2:
        # Histogram of bootstrap distribution
        fig = go.Figure()
        
        fig.add_trace(go.Histogram(
            x=sharpe_bootstrap,
            nbinsx=50,
            marker_color='#e1bee7',
            opacity=0.7,
            name='Bootstrap Distribution'
        ))
        
        # Add confidence interval lines
        fig.add_vline(x=ci_lower, line_dash="dash", line_color="red",
                     annotation_text=f"2.5%: {ci_lower:.3f}")
        fig.add_vline(x=ci_upper, line_dash="dash", line_color="red",
                     annotation_text=f"97.5%: {ci_upper:.3f}")
        
        # Add observed value
        fig.add_vline(x=sharpe_actual, line_dash="solid", line_color="yellow",
                     annotation_text=f"Observed: {sharpe_actual:.3f}")
        
        fig.update_layout(
            title="Bootstrap Distribution of Sharpe Ratio",
            xaxis_title="Sharpe Ratio",
            yaxis_title="Frequency",
            template="plotly_dark",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Advanced Methods")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["PCA Explorer", "Non-Parametric Test Comparison", 
         "Bootstrap Simulator", "Bayesian Updating"]
    )
    
    if exercise == "PCA Explorer":
        st.subheader("📊 PCA Explorer")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Generate Synthetic Data:**")
            
            n_variables = st.slider("Number of variables:", 3, 20, 5)
            n_observations = st.slider("Number of observations:", 50, 500, 100)
            correlation = st.slider("Average correlation:", 0.0, 0.9, 0.5, 0.1)
            
            if st.button("Generate Data & Run PCA"):
                # Generate correlated data
                np.random.seed(42)
                
                # Create correlation matrix
                corr_matrix = np.full((n_variables, n_variables), correlation)
                np.fill_diagonal(corr_matrix, 1.0)
                
                # Generate data
                mean = np.zeros(n_variables)
                data = np.random.multivariate_normal(mean, corr_matrix, n_observations)
                
                # Standardize
                scaler = StandardScaler()
                data_scaled = scaler.fit_transform(data)
                
                # PCA
                pca = PCA()
                pca.fit(data_scaled)
                
                # Store in session state
                st.session_state['pca_model'] = pca
                st.session_state['n_vars'] = n_variables
        
        with col2:
            if 'pca_model' in st.session_state:
                pca = st.session_state['pca_model']
                n_vars = st.session_state['n_vars']
                
                var_explained = pca.explained_variance_ratio_ * 100
                cumvar = np.cumsum(var_explained)
                
                # Scree plot
                fig = go.Figure()
                
                fig.add_trace(go.Bar(
                    x=[f'PC{i+1}' for i in range(len(var_explained))],
                    y=var_explained,
                    marker_color='#e1bee7',
                    name='Individual'
                ))
                
                fig.add_trace(go.Scatter(
                    x=[f'PC{i+1}' for i in range(len(var_explained))],
                    y=cumvar,
                    mode='lines+markers',
                    line=dict(color='yellow', width=3),
                    name='Cumulative',
                    yaxis='y2'
                ))
                
                fig.update_layout(
                    title="Variance Explained by Components",
                    xaxis_title="Component",
                    yaxis_title="Variance (%)",
                    yaxis2=dict(
                        title="Cumulative (%)",
                        overlaying='y',
                        side='right'
                    ),
                    template="plotly_dark",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Find how many PCs for 80% variance
                n_for_80 = np.where(cumvar >= 80)[0][0] + 1
                
                st.success(f"""
                **Results:**
                - PC1 explains {var_explained[0]:.1f}% of variance
                - Need {n_for_80} PCs for 80% variance
                - Reduction: {n_vars} → {n_for_80} dimensions
                """)
    
    elif exercise == "Non-Parametric Test Comparison":
        st.subheader("🔬 Non-Parametric vs Parametric Tests")
        
        st.markdown("Compare t-test and Mann-Whitney U test on different data types.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            data_type = st.selectbox("Data Type:", 
                                    ["Normal", "Skewed", "Heavy Outliers"])
            
            n_samples = st.slider("Sample size per group:", 20, 200, 50)
            
            if st.button("Generate Data & Run Tests"):
                np.random.seed(42)
                
                if data_type == "Normal":
                    group1 = np.random.normal(10, 2, n_samples)
                    group2 = np.random.normal(11, 2, n_samples)
                elif data_type == "Skewed":
                    group1 = np.random.exponential(2, n_samples)
                    group2 = np.random.exponential(2.5, n_samples)
                else:  # Heavy Outliers
                    group1_base = np.random.normal(10, 1, n_samples-5)
                    group1_outliers = np.array([50, 60, -30, -40, 70])
                    group1 = np.concatenate([group1_base, group1_outliers])
                    
                    group2_base = np.random.normal(11, 1, n_samples-5)
                    group2_outliers = np.array([55, 65, -35, -45, 75])
                    group2 = np.concatenate([group2_base, group2_outliers])
                
                # t-test
                t_stat, t_pval = stats.ttest_ind(group1, group2)
                
                # Mann-Whitney
                u_stat, u_pval = stats.mannwhitneyu(group1, group2)
                
                st.session_state['test_data'] = {
                    'group1': group1,
                    'group2': group2,
                    't_pval': t_pval,
                    'u_pval': u_pval
                }
        
        with col2:
            if 'test_data' in st.session_state:
                data = st.session_state['test_data']
                
                # Box plot
                fig = go.Figure()
                
                fig.add_trace(go.Box(
                    y=data['group1'],
                    name='Group 1',
                    marker_color='#e1bee7'
                ))
                
                fig.add_trace(go.Box(
                    y=data['group2'],
                    name='Group 2',
                    marker_color='#ce93d8'
                ))
                
                fig.update_layout(
                    title=f"Data Distribution ({data_type})",
                    yaxis_title="Value",
                    template="plotly_dark",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Results
                st.markdown("**Test Results:**")
                
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown("**t-test (Parametric)**")
                    st.metric("p-value", f"{data['t_pval']:.4f}")
                    if data['t_pval'] < 0.05:
                        st.success("Reject H₀")
                    else:
                        st.info("Fail to reject H₀")
                
                with col_b:
                    st.markdown("**Mann-Whitney (Non-Parametric)**")
                    st.metric("p-value", f"{data['u_pval']:.4f}")
                    if data['u_pval'] < 0.05:
                        st.success("Reject H₀")
                    else:
                        st.info("Fail to reject H₀")
                
                # Interpretation
                if data_type == "Heavy Outliers":
                    st.warning("""
                    **With outliers:**
                    Mann-Whitney is more robust and reliable!
                    """)
                elif data_type == "Normal":
                    st.info("""
                    **With normal data:**
                    Both tests work well, t-test slightly more powerful.
                    """)
    
    elif exercise == "Bootstrap Simulator":
        st.subheader("🎲 Bootstrap Confidence Interval Simulator")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Parameters:**")
            
            sample_size = st.slider("Sample size:", 20, 200, 50)
            n_bootstrap = st.slider("Bootstrap iterations:", 100, 5000, 1000, 100)
            
            statistic = st.selectbox("Statistic:", 
                                    ["Mean", "Median", "Std Dev", "Sharpe Ratio"])
            
            if st.button("Run Bootstrap"):
                # Generate sample data
                np.random.seed(42)
                data = np.random.normal(10, 3, sample_size)
                
                # Bootstrap
                bootstrap_stats = []
                
                for _ in range(n_bootstrap):
                    bootstrap_sample = np.random.choice(data, size=sample_size, replace=True)
                    
                    if statistic == "Mean":
                        stat = np.mean(bootstrap_sample)
                    elif statistic == "Median":
                        stat = np.median(bootstrap_sample)
                    elif statistic == "Std Dev":
                        stat = np.std(bootstrap_sample, ddof=1)
                    else:  # Sharpe Ratio
                        stat = np.mean(bootstrap_sample) / np.std(bootstrap_sample, ddof=1)
                    
                    bootstrap_stats.append(stat)
                
                bootstrap_stats = np.array(bootstrap_stats)
                
                # Calculate CI
                ci_lower = np.percentile(bootstrap_stats, 2.5)
                ci_upper = np.percentile(bootstrap_stats, 97.5)
                
                # Calculate observed
                if statistic == "Mean":
                    observed = np.mean(data)
                elif statistic == "Median":
                    observed = np.median(data)
                elif statistic == "Std Dev":
                    observed = np.std(data, ddof=1)
                else:
                    observed = np.mean(data) / np.std(data, ddof=1)
                
                st.session_state['bootstrap'] = {
                    'stats': bootstrap_stats,
                    'ci_lower': ci_lower,
                    'ci_upper': ci_upper,
                    'observed': observed
                }
        
        with col2:
            if 'bootstrap' in st.session_state:
                boot = st.session_state['bootstrap']
                
                # Histogram
                fig = go.Figure()
                
                fig.add_trace(go.Histogram(
                    x=boot['stats'],
                    nbinsx=50,
                    marker_color='#e1bee7',
                    opacity=0.7
                ))
                
                fig.add_vline(x=boot['ci_lower'], line_dash="dash", line_color="red",
                             annotation_text=f"2.5%: {boot['ci_lower']:.3f}")
                fig.add_vline(x=boot['ci_upper'], line_dash="dash", line_color="red",
                             annotation_text=f"97.5%: {boot['ci_upper']:.3f}")
                fig.add_vline(x=boot['observed'], line_dash="solid", line_color="yellow",
                             annotation_text=f"Observed: {boot['observed']:.3f}")
                
                fig.update_layout(
                    title=f"Bootstrap Distribution of {statistic}",
                    xaxis_title=statistic,
                    yaxis_title="Frequency",
                    template="plotly_dark",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.success(f"""
                **95% Confidence Interval:**
                [{boot['ci_lower']:.3f}, {boot['ci_upper']:.3f}]
                
                **Observed {statistic}:** {boot['observed']:.3f}
                """)
    
    elif exercise == "Bayesian Updating":
        st.subheader("🔄 Bayesian Updating Simulator")
        
        st.markdown("""
        See how beliefs update as new data arrives.
        
        **Example:** Estimating probability of a stock going up.
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Prior Belief:**")
            prior_up = st.slider("P(Stock Up):", 0.0, 1.0, 0.5, 0.05)
            
            st.markdown("**Observe Data:**")
            n_up = st.number_input("Days stock went up:", 0, 100, 6, 1)
            n_down = st.number_input("Days stock went down:", 0, 100, 4, 1)
            
            if st.button("Update Beliefs"):
                # Beta distribution (conjugate prior for binomial)
                # Prior: Beta(α, β)
                alpha_prior = prior_up * 10  # Convert to beta parameters
                beta_prior = (1 - prior_up) * 10
                
                # Posterior: Beta(α + successes, β + failures)
                alpha_post = alpha_prior + n_up
                beta_post = beta_prior + n_down
                
                # Posterior mean
                posterior_mean = alpha_post / (alpha_post + beta_post)
                
                st.session_state['bayesian'] = {
                    'alpha_prior': alpha_prior,
                    'beta_prior': beta_prior,
                    'alpha_post': alpha_post,
                    'beta_post': beta_post,
                    'prior_mean': prior_up,
                    'posterior_mean': posterior_mean
                }
        
        with col2:
            if 'bayesian' in st.session_state:
                bay = st.session_state['bayesian']
                
                # Plot prior and posterior
                x = np.linspace(0, 1, 100)
                
                prior_pdf = stats.beta.pdf(x, bay['alpha_prior'], bay['beta_prior'])
                posterior_pdf = stats.beta.pdf(x, bay['alpha_post'], bay['beta_post'])
                
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=x, y=prior_pdf,
                    mode='lines',
                    name='Prior',
                    line=dict(color='yellow', width=2, dash='dash')
                ))
                
                fig.add_trace(go.Scatter(
                    x=x, y=posterior_pdf,
                    mode='lines',
                    name='Posterior',
                    line=dict(color='#e1bee7', width=3),
                    fill='tozeroy',
                    fillcolor='rgba(225, 190, 231, 0.3)'
                ))
                
                fig.update_layout(
                    title="Bayesian Updating",
                    xaxis_title="P(Stock Up)",
                    yaxis_title="Probability Density",
                    template="plotly_dark",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.success(f"""
                **Updated Belief:**
                
                Prior: {bay['prior_mean']:.2%}
                Posterior: {bay['posterior_mean']:.2%}
                
                Data: {n_up} up, {n_down} down
                Updated probability of up: {bay['posterior_mean']:.2%}
                """)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Advanced Methods Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["Spearman Correlation", "Bootstrap CI", "Sample Size for Non-Parametric"]
    )
    
    if calc_type == "Spearman Correlation":
        st.subheader("Spearman Rank Correlation Calculator")
        
        st.markdown("**Enter two variables (comma-separated):**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            x_input = st.text_area("Variable X:", height=100)
        
        with col2:
            y_input = st.text_area("Variable Y:", height=100)
        
        if st.button("Calculate Correlation"):
            try:
                x = np.array([float(v.strip()) for v in x_input.split(',')])
                y = np.array([float(v.strip()) for v in y_input.split(',')])
                
                if len(x) != len(y):
                    st.error("Variables must have same length")
                else:
                    # Pearson correlation
                    pearson_r, pearson_p = stats.pearsonr(x, y)
                    
                    # Spearman correlation
                    spearman_r, spearman_p = stats.spearmanr(x, y)
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Pearson Correlation:**")
                        st.metric("r", f"{pearson_r:.4f}")
                        st.metric("p-value", f"{pearson_p:.4f}")
                    
                    with col2:
                        st.markdown("**Spearman Correlation:**")
                        st.metric("ρ", f"{spearman_r:.4f}")
                        st.metric("p-value", f"{spearman_p:.4f}")
                    
                    # Scatter plot
                    fig = go.Figure()
                    
                    fig.add_trace(go.Scatter(
                        x=x, y=y,
                        mode='markers',
                        marker=dict(size=10, color='#e1bee7')
                    ))
                    
                    fig.update_layout(
                        title="Scatter Plot",
                        xaxis_title="X",
                        yaxis_title="Y",
                        template="plotly_dark",
                        height=400
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    if abs(spearman_r - pearson_r) > 0.2:
                        st.warning("""
                        **Large difference between Pearson and Spearman!**
                        
                        This suggests:
                        - Non-linear relationship
                        - Presence of outliers
                        - Or non-monotonic relationship
                        
                        Spearman may be more appropriate.
                        """)
                    
            except Exception as e:
                st.error(f"Error: {e}")

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 8 Quiz: Advanced Statistical Methods")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'PCA is used to:',
            'options': [
                'Increase dimensionality',
                'Reduce dimensionality while preserving variance',
                'Create more variables',
                'Remove all correlation'
            ],
            'correct': 'Reduce dimensionality while preserving variance',
            'explanation': 'PCA reduces dimensions by finding principal components that capture maximum variance.'
        },
        {
            'id': 2,
            'question': 'The first principal component (PC1):',
            'options': [
                'Explains the least variance',
                'Explains the most variance',
                'Is always the mean',
                'Has no economic interpretation'
            ],
            'correct': 'Explains the most variance',
            'explanation': 'PC1 is the direction of maximum variance in the data.'
        },
        {
            'id': 3,
            'question': 'Non-parametric methods are useful when:',
            'options': [
                'Data is perfectly normal',
                'Sample size is infinite',
                'Distribution assumptions are violated',
                'You want less power'
            ],
            'correct': 'Distribution assumptions are violated',
            'explanation': 'Non-parametric methods don\'t assume specific distributions, making them robust.'
        },
        {
            'id': 4,
            'question': 'Mann-Whitney U test is the non-parametric alternative to:',
            'options': [
                'Paired t-test',
                'Independent samples t-test',
                'ANOVA',
                'Chi-square test'
            ],
            'correct': 'Independent samples t-test',
            'explanation': 'Mann-Whitney compares two independent groups without assuming normality.'
        },
        {
            'id': 5,
            'question': 'Spearman correlation measures:',
            'options': [
                'Linear relationships only',
                'Monotonic relationships',
                'Causation',
                'Time series trends'
            ],
            'correct': 'Monotonic relationships',
            'explanation': 'Spearman uses ranks and captures any monotonic (consistently increasing or decreasing) relationship.'
        },
        {
            'id': 6,
            'question': 'In Bayesian statistics, the posterior is:',
            'options': [
                'Your initial belief',
                'The likelihood function',
                'Updated belief after seeing data',
                'Always normal'
            ],
            'correct': 'Updated belief after seeing data',
            'explanation': 'Posterior = Prior × Likelihood, representing updated belief after observing data.'
        },
        {
            'id': 7,
            'question': 'Bootstrap method involves:',
            'options': [
                'Assuming normality',
                'Resampling with replacement',
                'Collecting new data',
                'Using population parameters'
            ],
            'correct': 'Resampling with replacement',
            'explanation': 'Bootstrap creates many samples by resampling the original data with replacement.'
        },
        {
            'id': 8,
            'question': 'Bootstrap is particularly useful for:',
            'options': [
                'Known distributions only',
                'Complex statistics with unknown distributions',
                'Small samples only',
                'Linear regression'
            ],
            'correct': 'Complex statistics with unknown distributions',
            'explanation': 'Bootstrap estimates sampling distributions empirically when analytical formulas are unavailable.'
        },
        {
            'id': 9,
            'question': 'PCA in yield curve analysis typically shows that:',
            'options': [
                'All rates move independently',
                '3 factors explain 95%+ of variance',
                'You need 100 factors',
                'No patterns exist'
            ],
            'correct': '3 factors explain 95%+ of variance',
            'explanation': 'Yield curves are typically explained by level, slope, and curvature (3 PCs).'
        },
        {
            'id': 10,
            'question': 'A key advantage of Bayesian methods is:',
            'options': [
                'They\'re always faster',
                'They incorporate prior knowledge',
                'They require no data',
                'They always give exact answers'
            ],
            'correct': 'They incorporate prior knowledge',
            'explanation': 'Bayesian methods formally incorporate prior beliefs and update them with data.'
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
    st.header("Module 8 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **PCA**
        - Dimensionality reduction
        - Extract key factors
        - PC1 explains most variance
        - Useful for risk decomposition
        """)
        
        st.success("""
        **Bootstrap**
        - Resampling method
        - Estimate uncertainty
        - No distribution assumption
        - CI for complex statistics
        """)
    
    with col2:
        st.warning("""
        **Non-Parametric Methods**
        - No distribution assumption
        - Robust to outliers
        - Mann-Whitney, Wilcoxon, Kruskal-Wallis
        - Less powerful but more robust
        """)
        
        st.info("""
        **Bayesian Statistics**
        - Incorporates prior knowledge
        - Updates beliefs with data
        - Posterior = Prior × Likelihood
        - Useful for sequential learning
        """)
    
    st.markdown("---")
    st.subheader("📐 Method Comparison")
    
    methods_df = pd.DataFrame({
        'Method': ['PCA', 'Mann-Whitney', 'Bootstrap', 'Bayesian', 'Spearman'],
        'Type': ['Dimensionality Reduction', 'Non-Parametric Test', 'Resampling', 'Probabilistic', 'Non-Parametric Correlation'],
        'Use When': [
            'Many correlated variables',
            'Non-normal, outliers',
            'Unknown distribution',
            'Have prior knowledge',
            'Non-linear monotonic relationship'
        ]
    })
    st.table(methods_df)
    
    st.markdown("---")
    st.subheader("💼 Financial Applications")
    
    tab1, tab2, tab3 = st.tabs(["PCA", "Non-Parametric", "Bayesian"])
    
    with tab1:
        st.markdown("""
        **PCA in Finance:**
        
        1. **Factor Models**
           - Extract market factors
           - Sector factors
           - Style factors
        
        2. **Yield Curve**
           - Level, slope, curvature
           - 3 PCs explain 95%+
           - Risk management
        
        3. **Portfolio Construction**
           - Factor-based investing
           - Risk budgeting
           - Diversification
        
        4. **Risk Attribution**
           - Decompose portfolio risk
           - Identify exposures
           - Stress testing
        """)
    
    with tab2:
        st.markdown("""
        **Non-Parametric Methods:**
        
        1. **Strategy Comparison**
           - Mann-Whitney for A/B testing
           - Robust to outliers
           - Real-world returns are non-normal
        
        2. **Ranking Systems**
           - Spearman for factor rankings
           - Credit ratings
           - Performance rankings
        
        3. **Event Studies**
           - Wilcoxon for paired data
           - Before/after analysis
           - Abnormal returns
        
        4. **Multi-Group Analysis**
           - Kruskal-Wallis for sectors
           - Asset class comparison
           - Market regime comparison
        """)
    
    with tab3:
        st.markdown("""
        **Bayesian Applications:**
        
        1. **Black-Litterman Model**
           - Combines market equilibrium (prior)
           - With investor views (update)
           - Optimal portfolio allocation
        
        2. **Credit Risk**
           - Update default probabilities
           - Incorporate new information
           - Dynamic risk assessment
        
        3. **Algorithmic Trading**
           - Online learning
           - Adaptive strategies
           - Sequential decisions
        
        4. **Parameter Estimation**
           - Incorporate uncertainty
           - Shrinkage estimators
           - Robust to overfitting
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 9?**
    
    Module 9: Machine Learning for Finance covers:
    - Supervised learning
    - Classification and regression
    - Model evaluation
    - ML applications in finance
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #f3e5f5; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 8 of 12: Advanced Statistical Methods</p>
</div>
""", unsafe_allow_html=True)