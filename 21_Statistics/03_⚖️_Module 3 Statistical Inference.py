import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e3a5f 0%, #2e4a6f 50%, #3e5a8f 100%);
    }
    h1 {
        color: #4fc3f7;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #81d4fa;
        border-left: 6px solid #4fc3f7;
        padding-left: 15px;
    }
    h3 {
        color: #b3e5fc;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>🔬 Module 3: Statistical Inference</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #b3e5fc;'>Making Decisions from Data</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 3 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("3.1 Sampling and Estimation")
    
    # Sampling Methods
    st.subheader("Sampling Methods")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Simple Random Sampling**
        - Every element has equal chance
        - Best for unbiased estimates
        
        **Stratified Sampling**
        - Divide population into groups
        - Sample from each group
        - Example: Sample by industry sector
        
        **Cluster Sampling**
        - Divide into clusters
        - Randomly select entire clusters
        - Example: Select entire branches
        """)
    
    with col2:
        st.success("""
        **Systematic Sampling**
        - Every kth element selected
        - Example: Every 10th transaction
        
        **Convenience Sampling**
        - Easy to access samples
        - May introduce bias
        
        **Financial Application:**
        - Audit sampling
        - Market research
        - Portfolio analysis
        """)
    
    st.markdown("---")
    
    # Point Estimation
    st.subheader("Point Estimation")
    
    with st.expander("**Sample Mean as Estimator**", expanded=True):
        st.latex(r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i")
        st.markdown("""
        **Properties:**
        - Unbiased estimator of population mean μ
        - E(x̄) = μ
        - Most efficient under normality
        
        **Financial Use:** Estimate expected return from sample of historical returns
        """)
    
    with st.expander("**Sample Standard Deviation**"):
        st.latex(r"s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}")
        st.markdown("""
        **Note the (n-1):** Bessel's correction for unbiased estimate
        
        **Why n-1?** We lose one degree of freedom by estimating the mean
        
        **Financial Use:** Estimate volatility from sample returns
        """)
    
    st.markdown("---")
    
    # Confidence Intervals
    st.subheader("Confidence Intervals")
    
    st.success("""
    **Definition:** A range that likely contains the true population parameter
    
    **Interpretation:** "We are 95% confident the true mean lies in this interval"
    
    **NOT:** "There's a 95% probability the true mean is in this interval"
    """)
    
    with st.expander("**CI for Population Mean (σ known)**", expanded=True):
        st.latex(r"\bar{x} \pm z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}")
        st.markdown("""
        **Components:**
        - x̄: Sample mean
        - z: Critical value from standard normal (1.96 for 95%)
        - σ: Population standard deviation
        - n: Sample size
        
        **95% CI:** x̄ ± 1.96 × (σ/√n)
        **99% CI:** x̄ ± 2.576 × (σ/√n)
        """)
    
    with st.expander("**CI for Population Mean (σ unknown)**"):
        st.latex(r"\bar{x} \pm t_{\alpha/2, n-1} \times \frac{s}{\sqrt{n}}")
        st.markdown("""
        **Use t-distribution when:**
        - Population σ is unknown (most real cases)
        - Sample size is small (n < 30)
        
        **Components:**
        - t: Critical value from t-distribution
        - s: Sample standard deviation
        - df = n - 1: Degrees of freedom
        
        **Financial Application:**
        - Estimate mean portfolio return with confidence
        - Risk-adjusted performance metrics
        """)
    
    st.markdown("---")
    
    # Standard Error
    st.subheader("Standard Error")
    
    st.latex(r"SE = \frac{\sigma}{\sqrt{n}} \quad \text{or} \quad SE = \frac{s}{\sqrt{n}}")
    
    st.info("""
    **Standard Error (SE):**
    - Measures variability of the sample mean
    - Smaller SE = More precise estimate
    - SE decreases as sample size increases
    - SE = σ/√n (law of large numbers)
    
    **Key Insight:** To halve the SE, need 4× the sample size
    
    **Financial Use:**
    - Precision of return estimates
    - Margin of error in forecasts
    """)
    
    st.markdown("---")
    
    # Hypothesis Testing
    st.header("3.2 Hypothesis Testing")
    
    st.subheader("The Hypothesis Testing Framework")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Null Hypothesis (H₀):**
        - Status quo / no effect
        - Assumed true until proven otherwise
        - Example: μ = 0 (no abnormal returns)
        
        **Alternative Hypothesis (H₁ or Hₐ):**
        - What we're testing for
        - Contradicts H₀
        - Example: μ ≠ 0 (abnormal returns exist)
        """)
    
    with col2:
        st.warning("""
        **Types of Tests:**
        
        **Two-tailed:** H₁: μ ≠ μ₀
        - Testing for difference (any direction)
        
        **Right-tailed:** H₁: μ > μ₀
        - Testing if greater than
        
        **Left-tailed:** H₁: μ < μ₀
        - Testing if less than
        """)
    
    st.markdown("---")
    
    # Errors in Hypothesis Testing
    st.subheader("Type I and Type II Errors")
    
    error_df = pd.DataFrame({
        '': ['H₀ is True', 'H₀ is False'],
        'Reject H₀': ['Type I Error (α)\nFalse Positive', 'Correct Decision\nPower = 1-β'],
        'Fail to Reject H₀': ['Correct Decision\nConfidence = 1-α', 'Type II Error (β)\nFalse Negative']
    })
    
    st.table(error_df)
    
    st.info("""
    **Type I Error (α):**
    - Reject true H₀
    - False positive
    - Significance level (usually 0.05)
    - Example: Conclude strategy works when it doesn't
    
    **Type II Error (β):**
    - Fail to reject false H₀
    - False negative
    - Related to statistical power
    - Example: Miss a profitable strategy
    
    **Power = 1 - β:**
    - Probability of correctly rejecting false H₀
    - Higher power = Better test
    """)
    
    st.markdown("---")
    
    # Test Statistics
    st.subheader("Common Test Statistics")
    
    with st.expander("**Z-Test (σ known, large n)**", expanded=True):
        st.latex(r"z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}")
        st.markdown("""
        **When to use:**
        - Population σ is known
        - Large sample (n ≥ 30)
        - Population is normal or n is large (CLT)
        
        **Decision Rule:**
        - Reject H₀ if |z| > z_critical
        - For α = 0.05: |z| > 1.96 (two-tailed)
        """)
    
    with st.expander("**t-Test (σ unknown)**"):
        st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}")
        st.markdown("""
        **When to use:**
        - Population σ is unknown (most cases)
        - Small to medium samples
        - Population approximately normal
        
        **Degrees of freedom:** df = n - 1
        
        **Decision Rule:**
        - Reject H₀ if |t| > t_critical
        - Critical value depends on df and α
        
        **Financial Applications:**
        - Test if mean return differs from zero
        - Compare portfolio performance to benchmark
        - Test strategy effectiveness
        """)
    
    with st.expander("**Two-Sample t-Test**"):
        st.latex(r"t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}")
        st.markdown("""
        **Purpose:** Compare means of two groups
        
        **Applications:**
        - Compare returns of two portfolios
        - Before/after intervention analysis
        - Compare two investment strategies
        
        **Assumptions:**
        - Independent samples
        - Approximately normal distributions
        - Similar variances (or use Welch's t-test)
        """)
    
    st.markdown("---")
    
    # p-value
    st.subheader("p-value Interpretation")
    
    st.success("""
    **p-value:** Probability of observing data as extreme as ours, assuming H₀ is true
    
    **Interpretation:**
    - p < 0.01: Very strong evidence against H₀
    - p < 0.05: Strong evidence against H₀ (reject H₀)
    - p < 0.10: Moderate evidence against H₀
    - p > 0.10: Weak evidence against H₀ (fail to reject H₀)
    
    **Decision Rule:**
    - If p-value ≤ α: Reject H₀
    - If p-value > α: Fail to reject H₀
    
    **Important:** p-value is NOT the probability that H₀ is true!
    """)
    
    st.markdown("---")
    
    # Chi-Square Test
    st.subheader("Chi-Square Test")
    
    with st.expander("**Chi-Square Goodness of Fit**"):
        st.latex(r"\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}")
        st.markdown("""
        **Purpose:** Test if observed frequencies match expected frequencies
        
        **Components:**
        - O_i: Observed frequency
        - E_i: Expected frequency
        
        **Financial Applications:**
        - Test if returns follow normal distribution
        - Verify uniform distribution of events
        - Quality control testing
        """)
    
    with st.expander("**Chi-Square Test of Independence**"):
        st.markdown("""
        **Purpose:** Test relationship between two categorical variables
        
        **Example in Finance:**
        - Is credit default independent of industry?
        - Relationship between rating and default
        - Market sector vs. performance category
        
        **H₀:** Variables are independent
        **H₁:** Variables are dependent
        """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Real-World Examples")
    
    # Example 1: Confidence Interval
    st.subheader("Example 1: Confidence Interval for Portfolio Return")
    
    st.markdown("""
    **Scenario:** You manage a portfolio and want to estimate the true mean annual return.
    
    **Sample Data:** 36 months of returns
    - Sample mean: 0.8% per month
    - Sample std dev: 2.5% per month
    - Confidence level: 95%
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Given data
        n = 36
        x_bar = 0.8
        s = 2.5
        confidence = 0.95
        alpha = 1 - confidence
        
        # Calculate CI
        df = n - 1
        t_critical = stats.t.ppf(1 - alpha/2, df)
        se = s / np.sqrt(n)
        margin_error = t_critical * se
        ci_lower = x_bar - margin_error
        ci_upper = x_bar + margin_error
        
        # Annualize
        annual_mean = x_bar * 12
        annual_lower = ci_lower * 12
        annual_upper = ci_upper * 12
        
        st.markdown("**Solution:**")
        st.code(f"""
Step 1: Calculate Standard Error
SE = s / √n = {s} / √{n} = {se:.4f}

Step 2: Find t-critical value
df = n - 1 = {df}
t_critical (95%, df={df}) = {t_critical:.3f}

Step 3: Calculate Margin of Error
ME = t × SE = {t_critical:.3f} × {se:.4f} = {margin_error:.4f}

Step 4: Construct CI
CI = {x_bar} ± {margin_error:.4f}
CI = [{ci_lower:.4f}, {ci_upper:.4f}] monthly

Step 5: Annualize
Annual CI = [{annual_lower:.2f}%, {annual_upper:.2f}%]
        """, language="text")
        
        st.metric("Monthly Mean", f"{x_bar}%")
        st.metric("95% CI (Monthly)", f"[{ci_lower:.3f}%, {ci_upper:.3f}%]")
        st.metric("95% CI (Annual)", f"[{annual_lower:.2f}%, {annual_upper:.2f}%]")
    
    with col2:
        # Visualization
        x = np.linspace(x_bar - 4*se, x_bar + 4*se, 1000)
        y = stats.t.pdf((x - x_bar) / se, df) / se
        
        fig = go.Figure()
        
        # Distribution
        fig.add_trace(go.Scatter(
            x=x, y=y,
            fill='tozeroy',
            name='t-distribution',
            line_color='#4fc3f7',
            fillcolor='rgba(79, 195, 247, 0.3)'
        ))
        
        # CI region
        x_ci = x[(x >= ci_lower) & (x <= ci_upper)]
        y_ci = stats.t.pdf((x_ci - x_bar) / se, df) / se
        fig.add_trace(go.Scatter(
            x=x_ci, y=y_ci,
            fill='tozeroy',
            name='95% CI',
            line_color='green',
            fillcolor='rgba(0, 255, 0, 0.3)'
        ))
        
        fig.add_vline(x=x_bar, line_dash="dash", line_color="yellow",
                     annotation_text=f"x̄={x_bar}%")
        fig.add_vline(x=ci_lower, line_dash="dot", line_color="red",
                     annotation_text=f"Lower: {ci_lower:.3f}%")
        fig.add_vline(x=ci_upper, line_dash="dot", line_color="red",
                     annotation_text=f"Upper: {ci_upper:.3f}%")
        
        fig.update_layout(
            title="Sampling Distribution and 95% CI",
            xaxis_title="Monthly Return (%)",
            yaxis_title="Density",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"""
        **Interpretation:**
        
        We are 95% confident that the true mean annual return 
        lies between **{annual_lower:.2f}%** and **{annual_upper:.2f}%**.
        
        This means if we repeated this sampling 100 times, 
        about 95 of the intervals would contain the true mean.
        """)
    
    st.markdown("---")
    
    # Example 2: Hypothesis Testing
    st.subheader("Example 2: Testing a Trading Strategy")
    
    st.markdown("""
    **Scenario:** A trader claims their strategy generates positive returns.
    
    **Test:** Does the strategy generate returns significantly different from zero?
    
    **Data:** 50 trades with the following results:
    - Mean return: 1.2%
    - Std dev: 4.5%
    - Significance level: α = 0.05
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Given data
        n = 50
        x_bar = 1.2
        s = 4.5
        mu_0 = 0
        alpha = 0.05
        
        # Hypothesis test
        t_stat = (x_bar - mu_0) / (s / np.sqrt(n))
        df = n - 1
        p_value_two = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        p_value_right = 1 - stats.t.cdf(t_stat, df)
        t_critical_two = stats.t.ppf(1 - alpha/2, df)
        t_critical_right = stats.t.ppf(1 - alpha, df)
        
        st.markdown("**Hypotheses:**")
        st.latex(r"H_0: \mu = 0 \text{ (no effect)}")
        st.latex(r"H_1: \mu > 0 \text{ (positive returns)}")
        
        st.markdown("**Solution:**")
        st.code(f"""
Step 1: Calculate test statistic
t = (x̄ - μ₀) / (s / √n)
t = ({x_bar} - {mu_0}) / ({s} / √{n})
t = {t_stat:.4f}

Step 2: Find critical value (one-tailed)
df = {df}
t_critical (α={alpha}) = {t_critical_right:.4f}

Step 3: Calculate p-value
p-value = {p_value_right:.6f}

Step 4: Decision
Since p-value ({p_value_right:.6f}) < α ({alpha})
and t ({t_stat:.4f}) > t_critical ({t_critical_right:.4f})
        """, language="text")
        
        st.metric("t-statistic", f"{t_stat:.4f}")
        st.metric("p-value", f"{p_value_right:.6f}")
        st.metric("Critical value", f"{t_critical_right:.4f}")
        
        if p_value_right < alpha:
            st.success("""
            **Decision: REJECT H₀**
            
            There is sufficient evidence to conclude 
            the strategy generates positive returns.
            """)
        else:
            st.warning("""
            **Decision: FAIL TO REJECT H₀**
            
            Insufficient evidence to conclude 
            the strategy generates positive returns.
            """)
    
    with col2:
        # Visualization
        x = np.linspace(-4, 4, 1000)
        y = stats.t.pdf(x, df)
        
        fig = go.Figure()
        
        # Full distribution
        fig.add_trace(go.Scatter(
            x=x, y=y,
            fill='tozeroy',
            name='t-distribution',
            line_color='#4fc3f7',
            fillcolor='rgba(79, 195, 247, 0.3)'
        ))
        
        # Rejection region
        x_reject = x[x >= t_critical_right]
        y_reject = stats.t.pdf(x_reject, df)
        fig.add_trace(go.Scatter(
            x=x_reject, y=y_reject,
            fill='tozeroy',
            name='Rejection Region',
            line_color='red',
            fillcolor='rgba(255, 0, 0, 0.3)'
        ))
        
        # Test statistic
        fig.add_vline(x=t_stat, line_dash="solid", line_color="yellow",
                     annotation_text=f"t = {t_stat:.3f}")
        fig.add_vline(x=t_critical_right, line_dash="dash", line_color="red",
                     annotation_text=f"Critical: {t_critical_right:.3f}")
        
        fig.update_layout(
            title=f"t-distribution (df={df}) - Right-Tailed Test",
            xaxis_title="t-value",
            yaxis_title="Density",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 3: Two-Sample Test
    st.subheader("Example 3: Comparing Two Investment Strategies")
    
    st.markdown("""
    **Scenario:** Compare returns of two different trading strategies.
    
    **Question:** Is there a significant difference in mean returns?
    """)
    
    # Generate sample data
    np.random.seed(42)
    strategy_a = np.random.normal(1.5, 3.0, 30)
    strategy_b = np.random.normal(2.2, 3.5, 30)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Calculate statistics
        mean_a = np.mean(strategy_a)
        mean_b = np.mean(strategy_b)
        std_a = np.std(strategy_a, ddof=1)
        std_b = np.std(strategy_b, ddof=1)
        n_a = len(strategy_a)
        n_b = len(strategy_b)
        
        # Two-sample t-test
        t_stat_two, p_value_two = stats.ttest_ind(strategy_a, strategy_b)
        
        st.markdown("**Data:**")
        
        data_comp = pd.DataFrame({
            'Metric': ['Sample Size', 'Mean Return (%)', 'Std Dev (%)', 'Min (%)', 'Max (%)'],
            'Strategy A': [n_a, f"{mean_a:.2f}", f"{std_a:.2f}", 
                          f"{np.min(strategy_a):.2f}", f"{np.max(strategy_a):.2f}"],
            'Strategy B': [n_b, f"{mean_b:.2f}", f"{std_b:.2f}", 
                          f"{np.min(strategy_b):.2f}", f"{np.max(strategy_b):.2f}"]
        })
        st.table(data_comp)
        
        st.markdown("**Hypothesis Test:**")
        st.latex(r"H_0: \mu_A = \mu_B")
        st.latex(r"H_1: \mu_A \neq \mu_B")
        
        st.metric("t-statistic", f"{t_stat_two:.4f}")
        st.metric("p-value", f"{p_value_two:.6f}")
        
        if p_value_two < 0.05:
            st.success("""
            **Reject H₀** (p < 0.05)
            
            Significant difference between strategies.
            """)
        else:
            st.warning("""
            **Fail to Reject H₀** (p ≥ 0.05)
            
            No significant difference between strategies.
            """)
    
    with col2:
        # Box plot comparison
        fig = go.Figure()
        
        fig.add_trace(go.Box(
            y=strategy_a,
            name='Strategy A',
            marker_color='#4fc3f7',
            boxmean='sd'
        ))
        
        fig.add_trace(go.Box(
            y=strategy_b,
            name='Strategy B',
            marker_color='#81d4fa',
            boxmean='sd'
        ))
        
        fig.update_layout(
            title="Distribution Comparison",
            yaxis_title="Returns (%)",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Statistical Inference")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["Confidence Interval Explorer", "Hypothesis Testing Simulator", 
         "Sample Size Calculator", "Power Analysis"]
    )
    
    if exercise == "Confidence Interval Explorer":
        st.subheader("🎯 Confidence Interval Explorer")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Input Parameters:**")
            
            sample_mean = st.number_input("Sample Mean (x̄):", value=10.0)
            sample_std = st.number_input("Sample Std Dev (s):", min_value=0.1, value=2.0)
            sample_size = st.slider("Sample Size (n):", 5, 200, 30)
            conf_level = st.slider("Confidence Level (%):", 80, 99, 95)
            
            # Calculate CI
            alpha = (100 - conf_level) / 100
            df = sample_size - 1
            t_crit = stats.t.ppf(1 - alpha/2, df)
            se = sample_std / np.sqrt(sample_size)
            me = t_crit * se
            ci_low = sample_mean - me
            ci_high = sample_mean + me
            
            st.markdown("**Results:**")
            st.metric("Standard Error", f"{se:.4f}")
            st.metric("Margin of Error", f"{me:.4f}")
            st.metric("CI Lower Bound", f"{ci_low:.4f}")
            st.metric("CI Upper Bound", f"{ci_high:.4f}")
            st.metric("CI Width", f"{ci_high - ci_low:.4f}")
            
            st.info(f"""
            **Interpretation:**
            
            We are {conf_level}% confident that the true 
            population mean lies between 
            **{ci_low:.3f}** and **{ci_high:.3f}**.
            """)
        
        with col2:
            # Visualization
            x = np.linspace(sample_mean - 4*se, sample_mean + 4*se, 1000)
            y = stats.t.pdf((x - sample_mean) / se, df) / se
            
            fig = go.Figure()
            
            # Full distribution
            fig.add_trace(go.Scatter(
                x=x, y=y,
                fill='tozeroy',
                name='Sampling Distribution',
                line_color='#4fc3f7',
                fillcolor='rgba(79, 195, 247, 0.2)'
            ))
            
            # CI region
            x_ci = x[(x >= ci_low) & (x <= ci_high)]
            y_ci = stats.t.pdf((x_ci - sample_mean) / se, df) / se
            fig.add_trace(go.Scatter(
                x=x_ci, y=y_ci,
                fill='tozeroy',
                name=f'{conf_level}% CI',
                line_color='green',
                fillcolor='rgba(0, 255, 0, 0.4)'
            ))
            
            fig.add_vline(x=sample_mean, line_dash="solid", line_color="yellow",
                         annotation_text=f"x̄={sample_mean}")
            fig.add_vline(x=ci_low, line_dash="dash", line_color="red")
            fig.add_vline(x=ci_high, line_dash="dash", line_color="red")
            
            fig.update_layout(
                title=f"{conf_level}% Confidence Interval",
                xaxis_title="Value",
                yaxis_title="Density",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Effect of sample size
            st.markdown("**Effect of Sample Size on CI Width:**")
            
            sizes = [10, 20, 30, 50, 100, 200]
            widths = []
            for n in sizes:
                se_n = sample_std / np.sqrt(n)
                t_n = stats.t.ppf(1 - alpha/2, n-1)
                me_n = t_n * se_n
                widths.append(2 * me_n)
            
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=sizes, y=widths,
                mode='lines+markers',
                line_color='#4fc3f7',
                marker=dict(size=10)
            ))
            fig2.update_layout(
                title="CI Width vs Sample Size",
                xaxis_title="Sample Size",
                yaxis_title="CI Width",
                template="plotly_dark",
                height=300
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    elif exercise == "Hypothesis Testing Simulator":
        st.subheader("🧪 Hypothesis Testing Simulator")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Test Parameters:**")
            
            test_type = st.radio("Test Type:", 
                                ["Two-tailed (μ ≠ μ₀)", 
                                 "Right-tailed (μ > μ₀)", 
                                 "Left-tailed (μ < μ₀)"])
            
            sample_mean = st.number_input("Sample Mean:", value=5.0)
            pop_mean = st.number_input("Hypothesized Mean (μ₀):", value=0.0)
            sample_std = st.number_input("Sample Std Dev:", min_value=0.1, value=3.0)
            sample_size = st.slider("Sample Size:", 5, 200, 30)
            alpha = st.slider("Significance Level (α):", 0.01, 0.10, 0.05, 0.01)
            
            # Calculate test statistic
            t_stat = (sample_mean - pop_mean) / (sample_std / np.sqrt(sample_size))
            df = sample_size - 1
            
            # Calculate p-value based on test type
            if "Two-tailed" in test_type:
                p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
                t_crit_low = stats.t.ppf(alpha/2, df)
                t_crit_high = stats.t.ppf(1 - alpha/2, df)
            elif "Right-tailed" in test_type:
                p_value = 1 - stats.t.cdf(t_stat, df)
                t_crit_high = stats.t.ppf(1 - alpha, df)
                t_crit_low = None
            else:  # Left-tailed
                p_value = stats.t.cdf(t_stat, df)
                t_crit_low = stats.t.ppf(alpha, df)
                t_crit_high = None
            
            # Decision
            reject = p_value < alpha
            
            st.markdown("**Results:**")
            st.metric("t-statistic", f"{t_stat:.4f}")
            st.metric("p-value", f"{p_value:.6f}")
            st.metric("α (significance)", f"{alpha:.3f}")
            
            if reject:
                st.error("""
                **REJECT H₀**
                
                Statistically significant result.
                Evidence against null hypothesis.
                """)
            else:
                st.success("""
                **FAIL TO REJECT H₀**
                
                Not statistically significant.
                Insufficient evidence against null.
                """)
        
        with col2:
            # Visualization
            x = np.linspace(-4, 4, 1000)
            y = stats.t.pdf(x, df)
            
            fig = go.Figure()
            
            # Full distribution
            fig.add_trace(go.Scatter(
                x=x, y=y,
                fill='tozeroy',
                name='t-distribution',
                line_color='#4fc3f7',
                fillcolor='rgba(79, 195, 247, 0.2)'
            ))
            
            # Rejection region(s)
            if "Two-tailed" in test_type:
                x_reject_left = x[x <= t_crit_low]
                y_reject_left = stats.t.pdf(x_reject_left, df)
                x_reject_right = x[x >= t_crit_high]
                y_reject_right = stats.t.pdf(x_reject_right, df)
                
                fig.add_trace(go.Scatter(
                    x=x_reject_left, y=y_reject_left,
                    fill='tozeroy', name='Rejection Region',
                    line_color='red', fillcolor='rgba(255, 0, 0, 0.3)',
                    showlegend=True
                ))
                fig.add_trace(go.Scatter(
                    x=x_reject_right, y=y_reject_right,
                    fill='tozeroy',
                    line_color='red', fillcolor='rgba(255, 0, 0, 0.3)',
                    showlegend=False
                ))
                
                fig.add_vline(x=t_crit_low, line_dash="dash", line_color="red")
                fig.add_vline(x=t_crit_high, line_dash="dash", line_color="red")
                
            elif "Right-tailed" in test_type:
                x_reject = x[x >= t_crit_high]
                y_reject = stats.t.pdf(x_reject, df)
                
                fig.add_trace(go.Scatter(
                    x=x_reject, y=y_reject,
                    fill='tozeroy', name='Rejection Region',
                    line_color='red', fillcolor='rgba(255, 0, 0, 0.3)'
                ))
                
                fig.add_vline(x=t_crit_high, line_dash="dash", line_color="red",
                             annotation_text=f"Critical: {t_crit_high:.3f}")
            
            else:  # Left-tailed
                x_reject = x[x <= t_crit_low]
                y_reject = stats.t.pdf(x_reject, df)
                
                fig.add_trace(go.Scatter(
                    x=x_reject, y=y_reject,
                    fill='tozeroy', name='Rejection Region',
                    line_color='red', fillcolor='rgba(255, 0, 0, 0.3)'
                ))
                
                fig.add_vline(x=t_crit_low, line_dash="dash", line_color="red",
                             annotation_text=f"Critical: {t_crit_low:.3f}")
            
            # Test statistic
            fig.add_vline(x=t_stat, line_dash="solid", line_color="yellow",
                         annotation_text=f"t={t_stat:.3f}")
            
            fig.update_layout(
                title=f"{test_type} - α={alpha}",
                xaxis_title="t-value",
                yaxis_title="Density",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif exercise == "Sample Size Calculator":
        st.subheader("📏 Sample Size Calculator")
        
        st.markdown("""
        Calculate required sample size for desired margin of error and confidence level.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Input Parameters:**")
            
            pop_std = st.number_input("Population Std Dev (σ):", min_value=0.1, value=10.0)
            margin_error = st.number_input("Desired Margin of Error:", min_value=0.1, value=2.0)
            conf_level = st.slider("Confidence Level (%):", 80, 99, 95)
            
            # Calculate required sample size
            alpha = (100 - conf_level) / 100
            z_crit = stats.norm.ppf(1 - alpha/2)
            
            # n = (z * σ / E)²
            n_required = ((z_crit * pop_std) / margin_error) ** 2
            n_required = int(np.ceil(n_required))
            
            st.markdown("**Results:**")
            st.metric("z-critical", f"{z_crit:.4f}")
            st.metric("Required Sample Size", f"{n_required}")
            
            st.info(f"""
            **Interpretation:**
            
            You need at least **{n_required}** observations to achieve 
            a margin of error of **{margin_error}** with 
            **{conf_level}%** confidence.
            """)
            
            # Formula
            st.markdown("**Formula:**")
            st.latex(r"n = \left(\frac{z_{\alpha/2} \times \sigma}{E}\right)^2")
            
        with col2:
            # Show relationship between ME and sample size
            st.markdown("**Margin of Error vs Sample Size:**")
            
            sizes = np.arange(10, 500, 10)
            margins = z_crit * pop_std / np.sqrt(sizes)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=sizes, y=margins,
                mode='lines',
                line_color='#4fc3f7',
                fill='tozeroy',
                fillcolor='rgba(79, 195, 247, 0.3)'
            ))
            
            fig.add_hline(y=margin_error, line_dash="dash", line_color="red",
                         annotation_text=f"Target ME: {margin_error}")
            fig.add_vline(x=n_required, line_dash="dash", line_color="green",
                         annotation_text=f"n={n_required}")
            
            fig.update_layout(
                title="Margin of Error Decreases with Sample Size",
                xaxis_title="Sample Size",
                yaxis_title="Margin of Error",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Cost-benefit table
            st.markdown("**Sample Size Options:**")
            
            sample_options = [50, 100, 200, 300, 500]
            me_options = [z_crit * pop_std / np.sqrt(n) for n in sample_options]
            
            df_options = pd.DataFrame({
                'Sample Size': sample_options,
                'Margin of Error': [f"{me:.3f}" for me in me_options],
                'Meets Target?': ['✅' if me <= margin_error else '❌' for me in me_options]
            })
            st.table(df_options)
    
    elif exercise == "Power Analysis":
        st.subheader("⚡ Statistical Power Analysis")
        
        st.markdown("""
        Explore the relationship between sample size, effect size, and statistical power.
        
        **Power = P(Reject H₀ | H₀ is false)**
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Parameters:**")
            
            true_mean = st.number_input("True Mean (μ₁):", value=5.0)
            null_mean = st.number_input("Null Mean (μ₀):", value=0.0)
            pop_std = st.number_input("Population Std Dev:", min_value=0.1, value=10.0)
            sample_size = st.slider("Sample Size:", 10, 500, 50)
            alpha = st.slider("Significance Level:", 0.01, 0.10, 0.05, 0.01)
            
            # Calculate effect size
            effect_size = (true_mean - null_mean) / pop_std
            
            # Calculate power
            se = pop_std / np.sqrt(sample_size)
            z_crit = stats.norm.ppf(1 - alpha/2)  # two-tailed
            
            # Critical values in terms of sample mean
            crit_upper = null_mean + z_crit * se
            crit_lower = null_mean - z_crit * se
            
            # Power: probability of rejecting when true mean is μ₁
            power = (1 - stats.norm.cdf(crit_upper, true_mean, se) + 
                    stats.norm.cdf(crit_lower, true_mean, se))
            
            beta = 1 - power
            
            st.markdown("**Results:**")
            st.metric("Effect Size (Cohen's d)", f"{effect_size:.3f}")
            st.metric("Statistical Power", f"{power:.3f}")
            st.metric("Type II Error (β)", f"{beta:.3f}")
            
            if power < 0.80:
                st.warning("⚠️ Power < 0.80: Increase sample size!")
            else:
                st.success("✅ Good power (≥ 0.80)")
            
            st.info("""
            **Rule of Thumb:**
            - Power ≥ 0.80 is desirable
            - Power ≥ 0.90 is excellent
            - Higher power = Less likely to miss true effect
            """)
        
        with col2:
            # Visualization
            x = np.linspace(null_mean - 4*se, true_mean + 4*se, 1000)
            y_null = stats.norm.pdf(x, null_mean, se)
            y_true = stats.norm.pdf(x, true_mean, se)
            
            fig = go.Figure()
            
            # Null distribution
            fig.add_trace(go.Scatter(
                x=x, y=y_null,
                fill='tozeroy',
                name='H₀: μ=μ₀',
                line_color='#4fc3f7',
                fillcolor='rgba(79, 195, 247, 0.2)'
            ))
            
            # True distribution
            fig.add_trace(go.Scatter(
                x=x, y=y_true,
                fill='tozeroy',
                name='True: μ=μ₁',
                line_color='green',
                fillcolor='rgba(0, 255, 0, 0.2)'
            ))
            
            # Critical values
            fig.add_vline(x=crit_upper, line_dash="dash", line_color="red",
                         annotation_text="Critical value")
            
            # Power region
            x_power = x[x >= crit_upper]
            y_power = stats.norm.pdf(x_power, true_mean, se)
            fig.add_trace(go.Scatter(
                x=x_power, y=y_power,
                fill='tozeroy',
                name=f'Power={power:.2f}',
                line_color='yellow',
                fillcolor='rgba(255, 255, 0, 0.4)'
            ))
            
            fig.update_layout(
                title=f"Power Analysis (n={sample_size}, α={alpha})",
                xaxis_title="Sample Mean",
                yaxis_title="Density",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Power curve
            st.markdown("**Power Curve:**")
            
            sizes = np.arange(10, 300, 10)
            powers = []
            for n in sizes:
                se_n = pop_std / np.sqrt(n)
                crit_n = null_mean + stats.norm.ppf(1 - alpha/2) * se_n
                pow_n = 1 - stats.norm.cdf(crit_n, true_mean, se_n)
                powers.append(pow_n)
            
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=sizes, y=powers,
                mode='lines',
                line_color='#4fc3f7'
            ))
            fig2.add_hline(y=0.80, line_dash="dash", line_color="green",
                          annotation_text="Target: 0.80")
            fig2.add_vline(x=sample_size, line_dash="dash", line_color="yellow")
            
            fig2.update_layout(
                title="Power vs Sample Size",
                xaxis_title="Sample Size",
                yaxis_title="Power",
                template="plotly_dark",
                height=300
            )
            st.plotly_chart(fig2, use_container_width=True)

# ======================
# CALCULATOR PAGE  
# ======================
elif page == "🧮 Calculator":
    st.header("Statistical Inference Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["Confidence Interval", "One-Sample t-Test", "Two-Sample t-Test", 
         "Chi-Square Test", "Sample Size"]
    )
    
    if calc_type == "Confidence Interval":
        st.subheader("Confidence Interval Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            known_sigma = st.radio("Population Std Dev Known?", ["No (use t)", "Yes (use z)"])
            
            x_bar = st.number_input("Sample Mean:", value=10.0)
            
            if known_sigma == "Yes (use z)":
                sigma = st.number_input("Population Std Dev (σ):", min_value=0.01, value=2.0)
            else:
                s = st.number_input("Sample Std Dev (s):", min_value=0.01, value=2.0)
            
            n = st.number_input("Sample Size:", min_value=2, value=30)
            conf = st.slider("Confidence Level (%):", 80, 99, 95)
            
            if st.button("Calculate CI"):
                alpha = (100 - conf) / 100
                
                if known_sigma == "Yes (use z)":
                    crit_val = stats.norm.ppf(1 - alpha/2)
                    se = sigma / np.sqrt(n)
                    dist_name = "z"
                else:
                    df = n - 1
                    crit_val = stats.t.ppf(1 - alpha/2, df)
                    se = s / np.sqrt(n)
                    dist_name = "t"
                
                me = crit_val * se
                ci_low = x_bar - me
                ci_high = x_bar + me
                
                st.markdown("**Results:**")
                st.metric(f"{dist_name}-critical", f"{crit_val:.4f}")
                st.metric("Standard Error", f"{se:.4f}")
                st.metric("Margin of Error", f"{me:.4f}")
                st.metric("Lower Bound", f"{ci_low:.4f}")
                st.metric("Upper Bound", f"{ci_high:.4f}")
                
                st.success(f"""
                **{conf}% Confidence Interval:**
                
                [{ci_low:.4f}, {ci_high:.4f}]
                
                We are {conf}% confident the true mean 
                lies within this interval.
                """)
        
        with col2:
            st.markdown("**Formulas:**")
            
            if known_sigma == "Yes (use z)":
                st.latex(r"\bar{x} \pm z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}")
            else:
                st.latex(r"\bar{x} \pm t_{\alpha/2, n-1} \times \frac{s}{\sqrt{n}}")
            
            st.markdown("**When to Use:**")
            st.info("""
            **Use z-distribution when:**
            - Population σ is known
            - Large sample (n ≥ 30)
            
            **Use t-distribution when:**
            - Population σ is unknown
            - Small sample (n < 30)
            - Most real-world cases
            """)
    
    elif calc_type == "One-Sample t-Test":
        st.subheader("One-Sample t-Test Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            test_type = st.radio("Alternative Hypothesis:",
                                ["Two-tailed (≠)", "Right-tailed (>)", "Left-tailed (<)"])
            
            x_bar = st.number_input("Sample Mean:", value=5.0)
            mu_0 = st.number_input("Hypothesized Mean (μ₀):", value=0.0)
            s = st.number_input("Sample Std Dev:", min_value=0.01, value=3.0)
            n = st.number_input("Sample Size:", min_value=2, value=30)
            alpha = st.slider("Significance Level (α):", 0.01, 0.20, 0.05, 0.01)
            
            if st.button("Run t-Test"):
                # Calculate t-statistic
                t_stat = (x_bar - mu_0) / (s / np.sqrt(n))
                df = n - 1
                
                # Calculate p-value
                if "Two-tailed" in test_type:
                    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
                    t_crit = stats.t.ppf(1 - alpha/2, df)
                    crit_text = f"±{t_crit:.4f}"
                elif "Right-tailed" in test_type:
                    p_value = 1 - stats.t.cdf(t_stat, df)
                    t_crit = stats.t.ppf(1 - alpha, df)
                    crit_text = f">{t_crit:.4f}"
                else:  # Left-tailed
                    p_value = stats.t.cdf(t_stat, df)
                    t_crit = stats.t.ppf(alpha, df)
                    crit_text = f"<{t_crit:.4f}"
                
                # Decision
                reject = p_value < alpha
                
                st.markdown("**Results:**")
                st.metric("t-statistic", f"{t_stat:.4f}")
                st.metric("p-value", f"{p_value:.6f}")
                st.metric("Critical Value", crit_text)
                st.metric("Degrees of Freedom", df)
                
                if reject:
                    st.error(f"""
                    **REJECT H₀** (p = {p_value:.6f} < α = {alpha})
                    
                    Statistically significant result.
                    """)
                else:
                    st.success(f"""
                    **FAIL TO REJECT H₀** (p = {p_value:.6f} ≥ α = {alpha})
                    
                    Not statistically significant.
                    """)
        
        with col2:
            st.markdown("**Hypotheses:**")
            
            if "Two-tailed" in test_type:
                st.latex(r"H_0: \mu = \mu_0")
                st.latex(r"H_1: \mu \neq \mu_0")
            elif "Right-tailed" in test_type:
                st.latex(r"H_0: \mu \leq \mu_0")
                st.latex(r"H_1: \mu > \mu_0")
            else:
                st.latex(r"H_0: \mu \geq \mu_0")
                st.latex(r"H_1: \mu < \mu_0")
            
            st.markdown("**Formula:**")
            st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}")
            
            st.markdown("**Applications:**")
            st.info("""
            - Test if mean return differs from benchmark
            - Verify if strategy beats market
            - Quality control testing
            - A/B testing results
            """)
    
    elif calc_type == "Two-Sample t-Test":
        st.subheader("Two-Sample t-Test Calculator")
        
        st.markdown("**Enter data for two groups:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Group 1:**")
            mean1 = st.number_input("Mean (x̄₁):", value=10.0, key="mean1")
            std1 = st.number_input("Std Dev (s₁):", min_value=0.01, value=2.0, key="std1")
            n1 = st.number_input("Sample Size (n₁):", min_value=2, value=30, key="n1")
        
        with col2:
            st.markdown("**Group 2:**")
            mean2 = st.number_input("Mean (x̄₂):", value=12.0, key="mean2")
            std2 = st.number_input("Std Dev (s₂):", min_value=0.01, value=2.5, key="std2")
            n2 = st.number_input("Sample Size (n₂):", min_value=2, value=30, key="n2")
        
        alpha = st.slider("Significance Level:", 0.01, 0.20, 0.05, 0.01)
        
        if st.button("Run Two-Sample t-Test"):
            # Welch's t-test (doesn't assume equal variances)
            se = np.sqrt((std1**2 / n1) + (std2**2 / n2))
            t_stat = (mean1 - mean2) / se
            
            # Welch-Satterthwaite degrees of freedom
            df = ((std1**2/n1 + std2**2/n2)**2) / ((std1**2/n1)**2/(n1-1) + (std2**2/n2)**2/(n2-1))
            
            # Two-tailed test
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
            t_crit = stats.t.ppf(1 - alpha/2, df)
            
            # Decision
            reject = p_value < alpha
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Results:**")
                st.metric("Mean Difference", f"{mean1 - mean2:.4f}")
                st.metric("t-statistic", f"{t_stat:.4f}")
                st.metric("p-value", f"{p_value:.6f}")
                st.metric("df (Welch)", f"{df:.2f}")
                st.metric("Critical Value", f"±{t_crit:.4f}")
            
            with col2:
                if reject:
                    st.error(f"""
                    **REJECT H₀**
                    
                    p-value ({p_value:.6f}) < α ({alpha})
                    
                    Significant difference between groups.
                    """)
                else:
                    st.success(f"""
                    **FAIL TO REJECT H₀**
                    
                    p-value ({p_value:.6f}) ≥ α ({alpha})
                    
                    No significant difference between groups.
                    """)
            
            st.markdown("**Hypotheses:**")
            st.latex(r"H_0: \mu_1 = \mu_2")
            st.latex(r"H_1: \mu_1 \neq \mu_2")
    
    elif calc_type == "Chi-Square Test":
        st.subheader("Chi-Square Goodness of Fit Test")
        
        st.markdown("""
        Test if observed frequencies match expected frequencies.
        """)
        
        n_categories = st.number_input("Number of Categories:", min_value=2, max_value=10, value=4)
        
        col1, col2 = st.columns(2)
        
        observed = []
        expected = []
        
        with col1:
            st.markdown("**Observed Frequencies:**")
            for i in range(n_categories):
                obs = st.number_input(f"Category {i+1}:", min_value=0, value=25, key=f"obs{i}")
                observed.append(obs)
        
        with col2:
            st.markdown("**Expected Frequencies:**")
            for i in range(n_categories):
                exp = st.number_input(f"Category {i+1}:", min_value=0.01, value=25.0, key=f"exp{i}")
                expected.append(exp)
        
        alpha = st.slider("Significance Level:", 0.01, 0.20, 0.05, 0.01)
        
        if st.button("Run Chi-Square Test"):
            observed = np.array(observed)
            expected = np.array(expected)
            
            # Calculate chi-square statistic
            chi2_stat = np.sum((observed - expected)**2 / expected)
            df = len(observed) - 1
            
            # p-value
            p_value = 1 - stats.chi2.cdf(chi2_stat, df)
            chi2_crit = stats.chi2.ppf(1 - alpha, df)
            
            # Decision
            reject = p_value < alpha
            
            # Results
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Results:**")
                st.metric("χ² statistic", f"{chi2_stat:.4f}")
                st.metric("p-value", f"{p_value:.6f}")
                st.metric("df", df)
                st.metric("Critical Value", f"{chi2_crit:.4f}")
                
                if reject:
                    st.error("""
                    **REJECT H₀**
                    
                    Observed frequencies significantly 
                    differ from expected.
                    """)
                else:
                    st.success("""
                    **FAIL TO REJECT H₀**
                    
                    Observed frequencies consistent 
                    with expected.
                    """)
            
            with col2:
                # Comparison table
                df_comp = pd.DataFrame({
                    'Category': [f"Cat {i+1}" for i in range(len(observed))],
                    'Observed': observed,
                    'Expected': expected,
                    'Difference': observed - expected,
                    'Contribution': (observed - expected)**2 / expected
                })
                st.dataframe(df_comp, use_container_width=True)
                
                st.markdown("**Formula:**")
                st.latex(r"\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}")
    
    elif calc_type == "Sample Size":
        st.subheader("Sample Size Calculator")
        
        calc_purpose = st.radio("Purpose:",
                               ["Estimate Mean", "Hypothesis Test"])
        
        if calc_purpose == "Estimate Mean":
            col1, col2 = st.columns(2)
            
            with col1:
                sigma = st.number_input("Population Std Dev (σ):", min_value=0.01, value=10.0)
                margin_error = st.number_input("Desired Margin of Error:", min_value=0.01, value=2.0)
                conf_level = st.slider("Confidence Level (%):", 80, 99, 95)
                
                if st.button("Calculate Sample Size"):
                    alpha = (100 - conf_level) / 100
                    z_crit = stats.norm.ppf(1 - alpha/2)
                    
                    n = ((z_crit * sigma) / margin_error) ** 2
                    n = int(np.ceil(n))
                    
                    st.markdown("**Results:**")
                    st.metric("Required Sample Size", n)
                    
                    st.success(f"""
                    Need at least **{n}** observations to achieve 
                    margin of error of **{margin_error}** with 
                    **{conf_level}%** confidence.
                    """)
            
            with col2:
                st.markdown("**Formula:**")
                st.latex(r"n = \left(\frac{z_{\alpha/2} \times \sigma}{E}\right)^2")
                
                st.markdown("**Example Uses:**")
                st.info("""
                - Survey sample size
                - Portfolio analysis
                - Quality control
                - Market research
                """)

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 3 Quiz: Statistical Inference")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'The correct interpretation of a 95% confidence interval is:',
            'options': [
                'There is a 95% probability the true parameter is in the interval',
                '95% of sample data falls in the interval',
                'If we repeated sampling 100 times, about 95 intervals would contain the true parameter',
                'The sample mean is 95% accurate'
            ],
            'correct': 'If we repeated sampling 100 times, about 95 intervals would contain the true parameter',
            'explanation': 'A confidence interval is about the process of interval construction, not the probability of a single interval.'
        },
        {
            'id': 2,
            'question': 'Type I error occurs when:',
            'options': [
                'We reject a true null hypothesis',
                'We fail to reject a false null hypothesis',
                'We accept a false null hypothesis',
                'Our sample is too small'
            ],
            'correct': 'We reject a true null hypothesis',
            'explanation': 'Type I error (α) is rejecting H₀ when it is actually true (false positive).'
        },
        {
            'id': 3,
            'question': 'A p-value of 0.03 means:',
            'options': [
                'There is a 3% chance H₀ is true',
                'There is a 3% chance of observing data this extreme if H₀ is true',
                'The null hypothesis has 97% support',
                'Our confidence level is 97%'
            ],
            'correct': 'There is a 3% chance of observing data this extreme if H₀ is true',
            'explanation': 'p-value is the probability of observing data as or more extreme than what we got, assuming H₀ is true.'
        },
        {
            'id': 4,
            'question': 'When population standard deviation is unknown, we should use:',
            'options': [
                'z-distribution',
                't-distribution',
                'Normal distribution',
                'Chi-square distribution'
            ],
            'correct': 't-distribution',
            'explanation': 'When σ is unknown and we use sample s, the t-distribution accounts for the extra uncertainty.'
        },
        {
            'id': 5,
            'question': 'To halve the margin of error in a confidence interval, the sample size must be:',
            'options': [
                'Doubled',
                'Quadrupled',
                'Halved',
                'Squared'
            ],
            'correct': 'Quadrupled',
            'explanation': 'ME = z × σ/√n. To cut ME in half, need √n to double, so n must be 4× larger.'
        },
        {
            'id': 6,
            'question': 'Statistical power is:',
            'options': [
                'P(Reject H₀ | H₀ is true)',
                'P(Reject H₀ | H₀ is false)',
                'P(Fail to reject H₀ | H₀ is false)',
                '1 - α'
            ],
            'correct': 'P(Reject H₀ | H₀ is false)',
            'explanation': 'Power = 1 - β = probability of correctly rejecting a false null hypothesis.'
        },
        {
            'id': 7,
            'question': 'In a two-tailed test with α = 0.05, the critical z-values are approximately:',
            'options': [
                '±1.645',
                '±1.96',
                '±2.576',
                '±1.28'
            ],
            'correct': '±1.96',
            'explanation': 'For α = 0.05 (two-tailed), we split α into 0.025 in each tail, giving z = ±1.96.'
        },
        {
            'id': 8,
            'question': 'The standard error measures:',
            'options': [
                'Variability in the population',
                'Variability in the sample',
                'Variability of the sample mean',
                'Error in our calculations'
            ],
            'correct': 'Variability of the sample mean',
            'explanation': 'SE = σ/√n measures how much sample means vary from sample to sample.'
        },
        {
            'id': 9,
            'question': 'Which statement is TRUE about hypothesis testing?',
            'options': [
                'We prove the null hypothesis',
                'We accept the alternative hypothesis',
                'We reject or fail to reject the null hypothesis',
                'We always need α = 0.05'
            ],
            'correct': 'We reject or fail to reject the null hypothesis',
            'explanation': 'We never "accept" or "prove" hypotheses; we only reject or fail to reject H₀ based on evidence.'
        },
        {
            'id': 10,
            'question': 'Bessel\'s correction (using n-1) is used when calculating:',
            'options': [
                'Population variance',
                'Sample variance',
                'Population mean',
                'Sample mean'
            ],
            'correct': 'Sample variance',
            'explanation': 'We divide by n-1 (not n) when calculating sample variance to get an unbiased estimator.'
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
    st.header("Module 3 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Sampling & Estimation**
        - Sample mean estimates population mean
        - Standard error = σ/√n
        - Confidence intervals provide range estimates
        - Larger samples → More precise estimates
        """)
        
        st.success("""
        **Hypothesis Testing**
        - H₀: Null hypothesis (status quo)
        - H₁: Alternative hypothesis
        - p-value: Evidence against H₀
        - Reject H₀ if p < α
        """)
    
    with col2:
        st.warning("""
        **Errors**
        - Type I (α): Reject true H₀
        - Type II (β): Fail to reject false H₀
        - Power = 1 - β
        - Trade-off between Type I and Type II
        """)
        
        st.info("""
        **Practical Significance**
        - Statistical ≠ Practical significance
        - Large samples can find tiny differences
        - Consider effect size, not just p-value
        - Business impact matters most
        """)
    
    st.markdown("---")
    st.subheader("📐 Essential Formulas")
    
    formulas_df = pd.DataFrame({
        'Concept': ['Confidence Interval (σ known)', 'Confidence Interval (σ unknown)', 
                   't-statistic', 'Standard Error', 'Sample Size', 'Chi-Square'],
        'Formula': [
            'x̄ ± z_(α/2) × σ/√n',
            'x̄ ± t_(α/2,df) × s/√n',
            't = (x̄ - μ₀) / (s/√n)',
            'SE = σ/√n or s/√n',
            'n = (z × σ / E)²',
            'χ² = Σ(O - E)²/E'
        ]
    })
    st.table(formulas_df)
    
    st.markdown("---")
    st.subheader("💼 Financial Applications")
    
    tab1, tab2, tab3 = st.tabs(["Portfolio Analysis", "Strategy Testing", "Risk Assessment"])
    
    with tab1:
        st.markdown("""
        **Confidence Intervals in Portfolio Analysis:**
        
        1. **Return Estimation:** Estimate mean return with confidence
        2. **Risk Metrics:** CI for volatility, Sharpe ratio
        3. **Performance:** Compare portfolio to benchmark
        4. **Forecasting:** Prediction intervals for future returns
        
        **Example:** "We are 95% confident the annual return will be between 8% and 12%"
        """)
    
    with tab2:
        st.markdown("""
        **Hypothesis Testing for Trading Strategies:**
        
        1. **Backtest Validation:** Does strategy beat random?
        2. **Alpha Testing:** H₀: α = 0 vs H₁: α > 0
        3. **Risk-Adjusted Performance:** Test Sharpe ratio significance
        4. **Regime Changes:** Test for structural breaks
        
        **Caution:** Beware of data mining and multiple testing
        """)
    
    with tab3:
        st.markdown("""
        **Statistical Inference in Risk Management:**
        
        1. **VaR Backtesting:** Test if VaR model is accurate
        2. **Stress Testing:** Confidence intervals for extreme scenarios
        3. **Model Validation:** Test model assumptions
        4. **Regulatory Compliance:** Statistical evidence for capital requirements
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 4?**
    
    Module 4: Regression Analysis covers:
    - Simple and multiple regression
    - Interpreting coefficients
    - Model diagnostics
    - Financial applications (CAPM, factor models)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #b3e5fc; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 3 of 12: Statistical Inference</p>
</div>
""", unsafe_allow_html=True)