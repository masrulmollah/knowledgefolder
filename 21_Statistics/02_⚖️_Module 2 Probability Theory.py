import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from scipy.special import comb
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1a0f2e 0%, #2a1f3e 50%, #3a2f5e 100%);
    }
    h1 {
        color: #9d7bd8;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #c9a7eb;
        border-left: 6px solid #9d7bd8;
        padding-left: 15px;
    }
    h3 {
        color: #b8a3d6;
    }
    .stAlert {
        background-color: rgba(157, 123, 216, 0.1);
        border: 2px solid #9d7bd8;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>🎲 Module 2: Probability Theory</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #b8a3d6;'>Understanding Uncertainty in Finance</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 2 of 12**\n\nStatistics for Finance Professionals")

# Helper Functions
def binomial_probability(n, k, p):
    """Calculate binomial probability"""
    return comb(n, k, exact=True) * (p**k) * ((1-p)**(n-k))

def poisson_probability(k, lambda_val):
    """Calculate Poisson probability"""
    return (np.exp(-lambda_val) * (lambda_val**k)) / np.math.factorial(k)

def normal_probability(x, mu, sigma):
    """Calculate normal probability density"""
    return (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/sigma)**2)

def bayes_theorem(p_b_given_a, p_a, p_b):
    """Calculate P(A|B) using Bayes' theorem"""
    return (p_b_given_a * p_a) / p_b

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("2.1 Basic Probability Concepts")
    
    # Sample Space and Events
    st.subheader("Sample Space and Events")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Sample Space (S):**
        The set of all possible outcomes
        
        **Example:** Rolling a die
        - S = {1, 2, 3, 4, 5, 6}
        
        **Financial Example:** Stock movement
        - S = {Up, Down, Unchanged}
        """)
    
    with col2:
        st.success("""
        **Event (E):**
        A subset of the sample space
        
        **Example:** Getting an even number
        - E = {2, 4, 6}
        
        **Financial Example:** Profitable trade
        - E = {Returns > 0}
        """)
    
    # Probability Rules
    st.markdown("---")
    st.subheader("Fundamental Probability Rules")
    
    with st.expander("**Rule 1: Probability Range** - Click to expand", expanded=True):
        st.latex(r"0 \leq P(E) \leq 1")
        st.markdown("""
        - Probability of any event is between 0 and 1
        - P(E) = 0 means impossible event
        - P(E) = 1 means certain event
        - P(E) = 0.5 means equally likely
        """)
    
    with st.expander("**Rule 2: Complementary Events**"):
        st.latex(r"P(E) + P(E^c) = 1")
        st.markdown("""
        - P(E^c) is the probability of "not E"
        - If P(profit) = 0.6, then P(loss) = 0.4
        
        **Financial Application:**
        - If P(default) = 0.03, then P(no default) = 0.97
        """)
    
    with st.expander("**Rule 3: Addition Rule**"):
        st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")
        st.markdown("""
        - For mutually exclusive events: P(A ∪ B) = P(A) + P(B)
        - Events cannot happen simultaneously
        
        **Financial Application:**
        - P(Tech stock OR Energy stock) when mutually exclusive
        """)
    
    with st.expander("**Rule 4: Multiplication Rule**"):
        st.latex(r"P(A \cap B) = P(A) \times P(B|A)")
        st.markdown("""
        - For independent events: P(A ∩ B) = P(A) × P(B)
        - P(B|A) is conditional probability
        
        **Financial Application:**
        - P(Two profitable trades in a row)
        """)
    
    # Conditional Probability
    st.markdown("---")
    st.subheader("Conditional Probability")
    
    st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}")
    
    st.info("""
    **Interpretation:** Probability of A given that B has occurred
    
    **Financial Example:**
    - P(Default | Poor Credit Score)
    - P(Stock Up | Market Up)
    - P(Bankruptcy | Negative Earnings)
    """)
    
    # Independence
    st.markdown("---")
    st.subheader("Independence")
    
    st.warning("""
    **Independent Events:** A and B are independent if:
    """)
    
    st.latex(r"P(A|B) = P(A) \quad \text{or} \quad P(A \cap B) = P(A) \times P(B)")
    
    st.markdown("""
    **Financial Examples:**
    - Coin flips are independent
    - Stock returns on different days (approximately)
    - Different companies in different industries (may be independent)
    
    **Not Independent:**
    - Stock returns within same sector
    - Economic indicators
    - Related company stocks
    """)
    
    # Bayes' Theorem
    st.markdown("---")
    st.subheader("Bayes' Theorem")
    
    st.latex(r"P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}")
    
    st.success("""
    **Components:**
    - **P(A|B):** Posterior probability (what we want)
    - **P(B|A):** Likelihood
    - **P(A):** Prior probability
    - **P(B):** Marginal probability
    
    **Financial Application:** Credit Risk Assessment
    - Update probability of default given new information
    - Revise investment thesis based on earnings
    """)
    
    # Probability Distributions
    st.markdown("---")
    st.header("2.2 Probability Distributions")
    
    st.subheader("📊 Discrete Distributions")
    
    # Binomial Distribution
    with st.expander("**Binomial Distribution** - Click to expand", expanded=True):
        st.latex(r"P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}")
        
        st.markdown("""
        **Used for:** Fixed number of independent trials, each with two outcomes
        
        **Parameters:**
        - n: number of trials
        - p: probability of success
        - k: number of successes
        
        **Financial Applications:**
        - Number of profitable trades out of 10
        - Number of defaults in a bond portfolio
        - Win/loss streaks in trading
        
        **Example:** If you make 10 trades with 60% success rate, 
        what's the probability of exactly 7 wins?
        """)
        
        # Visual example
        n, p = 10, 0.6
        k_values = range(0, n+1)
        probs = [binomial_probability(n, k, p) for k in k_values]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=list(k_values), y=probs, marker_color='#9d7bd8'))
        fig.update_layout(
            title=f"Binomial Distribution (n={n}, p={p})",
            xaxis_title="Number of Successes",
            yaxis_title="Probability",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Poisson Distribution
    with st.expander("**Poisson Distribution**"):
        st.latex(r"P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}")
        
        st.markdown("""
        **Used for:** Number of events in a fixed interval
        
        **Parameter:**
        - λ (lambda): average rate of occurrence
        
        **Financial Applications:**
        - Number of trades per day
        - Number of defaults per year
        - Number of market crashes per decade
        - Fraud occurrences
        
        **Example:** If a trading desk averages 5 trades per hour,
        what's the probability of exactly 3 trades in the next hour?
        """)
    
    st.markdown("---")
    st.subheader("📈 Continuous Distributions")
    
    # Normal Distribution
    with st.expander("**Normal (Gaussian) Distribution** - Click to expand", expanded=True):
        st.latex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}")
        
        st.markdown("""
        **The most important distribution in finance!**
        
        **Parameters:**
        - μ (mu): mean
        - σ (sigma): standard deviation
        
        **Properties:**
        - Symmetric, bell-shaped
        - Mean = Median = Mode
        - 68% within 1σ, 95% within 2σ, 99.7% within 3σ
        
        **Financial Applications:**
        - Stock returns (approximately)
        - Asset price changes
        - Measurement errors
        - Risk modeling
        
        **Key Assumption:** Many models assume normal distribution
        - Black-Scholes model
        - Modern Portfolio Theory
        - Value at Risk (VaR)
        """)
        
        # Visual
        x = np.linspace(-4, 4, 100)
        y = stats.norm.pdf(x, 0, 1)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', 
                                line_color='#9d7bd8'))
        fig.update_layout(
            title="Standard Normal Distribution (μ=0, σ=1)",
            xaxis_title="Standard Deviations from Mean",
            yaxis_title="Probability Density",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Lognormal Distribution
    with st.expander("**Lognormal Distribution**"):
        st.markdown("""
        **Definition:** If log(X) is normally distributed, then X is lognormal
        
        **Why Important in Finance:**
        - Stock PRICES follow lognormal (not normal)
        - Prices cannot be negative
        - Returns are normal, prices are lognormal
        
        **Applications:**
        - Stock price modeling
        - Option pricing
        - Asset valuations
        
        **Relationship:**
        - If returns ~ Normal(μ, σ)
        - Then prices ~ Lognormal
        """)
    
    # Student's t-Distribution
    with st.expander("**Student's t-Distribution**"):
        st.markdown("""
        **Used when:** Sample size is small or population std dev unknown
        
        **Parameter:**
        - ν (nu): degrees of freedom
        
        **Properties:**
        - Similar to normal but heavier tails
        - Approaches normal as ν → ∞
        - More conservative for small samples
        
        **Financial Applications:**
        - Small sample testing
        - Hypothesis tests with limited data
        - More realistic for extreme events
        """)
    
    st.markdown("---")
    st.success("""
    ### 💡 Key Insights for Finance
    
    1. **Normal distribution** is the foundation of many financial models
    2. **Binomial** for discrete win/loss scenarios
    3. **Poisson** for rare events (defaults, crashes)
    4. **Lognormal** for asset prices
    5. **Real markets** often have fatter tails than normal distribution suggests
    """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Real-World Financial Examples")
    
    # Example 1: Binomial - Trading Success
    st.subheader("Example 1: Trading Success Probability (Binomial)")
    
    st.markdown("""
    **Scenario:** You're a day trader with a 55% success rate. You plan to make 20 trades today.
    What's the probability of winning at least 12 trades?
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        n, p = 20, 0.55
        
        st.code(f"""
Parameters:
- Number of trades (n): {n}
- Win probability (p): {p}
- Target: At least 12 wins
        """, language="text")
        
        # Calculate P(X >= 12)
        prob_at_least_12 = sum([binomial_probability(n, k, p) for k in range(12, n+1)])
        
        st.markdown("**Solution:**")
        st.latex(r"P(X \geq 12) = \sum_{k=12}^{20} \binom{20}{k} (0.55)^k (0.45)^{20-k}")
        
        st.metric("Probability of ≥12 wins", f"{prob_at_least_12:.2%}")
        
        st.markdown(f"""
        **Interpretation:**
        - There's a **{prob_at_least_12:.1%} chance** of having at least 12 winning trades
        - Expected wins: {n*p:.1f} trades
        - This helps set realistic expectations
        """)
    
    with col2:
        # Visualization
        k_values = range(0, n+1)
        probs = [binomial_probability(n, k, p) for k in k_values]
        colors = ['#9d7bd8' if k >= 12 else '#4a4a4a' for k in k_values]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=list(k_values), y=probs, marker_color=colors))
        fig.add_vline(x=12, line_dash="dash", line_color="red", 
                     annotation_text="Target: 12 wins")
        fig.update_layout(
            title="Probability Distribution of Wins",
            xaxis_title="Number of Winning Trades",
            yaxis_title="Probability",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 2: Bayes' Theorem - Credit Risk
    st.subheader("Example 2: Credit Risk Assessment (Bayes' Theorem)")
    
    st.markdown("""
    **Scenario:** A bank uses credit scores to assess loan default risk.
    
    **Given Information:**
    - 5% of all borrowers default on loans
    - 80% of defaulters had poor credit scores
    - 30% of non-defaulters had poor credit scores
    
    **Question:** If a borrower has a poor credit score, what's the probability they will default?
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Define probabilities
        p_default = 0.05  # P(D)
        p_poor_given_default = 0.80  # P(Poor|D)
        p_poor_given_no_default = 0.30  # P(Poor|No D)
        p_no_default = 1 - p_default  # P(No D)
        
        # Calculate P(Poor) using law of total probability
        p_poor = (p_poor_given_default * p_default + 
                  p_poor_given_no_default * p_no_default)
        
        # Apply Bayes' Theorem
        p_default_given_poor = (p_poor_given_default * p_default) / p_poor
        
        st.markdown("**Step-by-Step Solution:**")
        
        st.markdown(f"""
        1. **Given:**
           - P(Default) = {p_default:.2%}
           - P(Poor Score | Default) = {p_poor_given_default:.0%}
           - P(Poor Score | No Default) = {p_poor_given_no_default:.0%}
        
        2. **Find P(Poor Score):**
        """)
        
        st.latex(r"P(\text{Poor}) = P(\text{Poor}|D) \times P(D) + P(\text{Poor}|\neg D) \times P(\neg D)")
        
        st.markdown(f"""
           P(Poor) = {p_poor_given_default} × {p_default} + {p_poor_given_no_default} × {p_no_default}
           P(Poor) = {p_poor:.3f}
        
        3. **Apply Bayes' Theorem:**
        """)
        
        st.latex(r"P(D|\text{Poor}) = \frac{P(\text{Poor}|D) \times P(D)}{P(\text{Poor})}")
        
        st.markdown(f"""
           P(Default | Poor) = ({p_poor_given_default} × {p_default}) / {p_poor:.3f}
        """)
        
        st.metric("P(Default | Poor Credit)", f"{p_default_given_poor:.2%}")
        
    with col2:
        # Visualization
        categories = ['Prior\nP(Default)', 'Posterior\nP(Default|Poor)']
        probabilities = [p_default, p_default_given_poor]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=categories,
            y=probabilities,
            marker_color=['#4a4a4a', '#9d7bd8'],
            text=[f"{p:.1%}" for p in probabilities],
            textposition='auto'
        ))
        fig.update_layout(
            title="Prior vs Posterior Probability",
            yaxis_title="Probability",
            yaxis_tickformat='.0%',
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"""
        **Conclusion:**
        - Prior probability of default: **{p_default:.1%}**
        - Posterior (given poor score): **{p_default_given_poor:.1%}**
        - The poor credit score increased default probability by **{p_default_given_poor/p_default:.1f}x**
        """)
    
    st.markdown("---")
    
    # Example 3: Normal Distribution - VaR
    st.subheader("Example 3: Value at Risk using Normal Distribution")
    
    st.markdown("""
    **Scenario:** A portfolio has:
    - Expected daily return: 0.05%
    - Daily volatility (std dev): 1.2%
    
    **Question:** What's the 95% Value at Risk (VaR)? 
    i.e., What's the maximum loss expected 95% of the time?
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        mu = 0.05  # mean return %
        sigma = 1.2  # std dev %
        
        # 95% VaR corresponds to 5th percentile (left tail)
        z_score_5pct = stats.norm.ppf(0.05)  # -1.645 for 95% confidence
        var_95 = mu + z_score_5pct * sigma
        
        st.markdown("**Solution:**")
        
        st.markdown(f"""
        **Given:**
        - μ (mean return) = {mu}%
        - σ (std dev) = {sigma}%
        - Confidence level = 95%
        
        **For 95% VaR, we need the 5th percentile:**
        """)
        
        st.latex(r"\text{VaR}_{95\%} = \mu + z_{0.05} \times \sigma")
        
        st.markdown(f"""
        - z-score for 5th percentile = {z_score_5pct:.3f}
        - VaR₉₅ = {mu} + ({z_score_5pct:.3f}) × {sigma}
        - VaR₉₅ = **{var_95:.2f}%**
        """)
        
        st.metric("95% Value at Risk", f"{abs(var_95):.2f}%", 
                 delta="Maximum expected loss", delta_color="inverse")
        
        st.info("""
        **Interpretation:**
        On 95% of days, losses won't exceed 1.92%.
        On 5% of days (1 in 20), losses could be worse.
        """)
        
    with col2:
        # Visualization
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
        y = stats.norm.pdf(x, mu, sigma)
        
        fig = go.Figure()
        
        # Full distribution
        fig.add_trace(go.Scatter(
            x=x, y=y,
            fill='tozeroy',
            name='Distribution',
            line_color='#9d7bd8',
            fillcolor='rgba(157, 123, 216, 0.3)'
        ))
        
        # VaR region
        x_var = x[x <= var_95]
        y_var = stats.norm.pdf(x_var, mu, sigma)
        fig.add_trace(go.Scatter(
            x=x_var, y=y_var,
            fill='tozeroy',
            name='5% Tail (VaR)',
            line_color='red',
            fillcolor='rgba(255, 0, 0, 0.3)'
        ))
        
        fig.add_vline(x=var_95, line_dash="dash", line_color="red",
                     annotation_text=f"VaR: {var_95:.2f}%")
        
        fig.update_layout(
            title="Portfolio Return Distribution & VaR",
            xaxis_title="Daily Return (%)",
            yaxis_title="Probability Density",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 4: Poisson - Rare Events
    st.subheader("Example 4: Modeling Rare Events (Poisson)")
    
    st.markdown("""
    **Scenario:** Based on historical data, major market crashes (>20% drop) occur 
    on average once every 10 years.
    
    **Question:** What's the probability of experiencing at least one crash in the next 5 years?
    """)
    
    lambda_10y = 1  # 1 crash per 10 years
    lambda_5y = 0.5  # 0.5 crashes per 5 years
    
    # P(X >= 1) = 1 - P(X = 0)
    p_no_crash = poisson_probability(0, lambda_5y)
    p_at_least_one = 1 - p_no_crash
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Solution:**")
        
        st.markdown(f"""
        **Given:**
        - Average rate: 1 crash per 10 years
        - Time period: 5 years
        - λ (lambda) = {lambda_5y} crashes per 5 years
        
        **Calculate P(at least 1 crash):**
        """)
        
        st.latex(r"P(X \geq 1) = 1 - P(X = 0)")
        st.latex(r"P(X = 0) = \frac{e^{-\lambda} \lambda^0}{0!} = e^{-\lambda}")
        
        st.markdown(f"""
        - P(X = 0) = e^(-{lambda_5y}) = {p_no_crash:.4f}
        - P(X ≥ 1) = 1 - {p_no_crash:.4f} = **{p_at_least_one:.2%}**
        """)
        
        st.metric("Probability of ≥1 crash in 5 years", f"{p_at_least_one:.1%}")
        
    with col2:
        # Visualization
        k_values = range(0, 6)
        probs = [poisson_probability(k, lambda_5y) for k in k_values]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=list(k_values),
            y=probs,
            marker_color=['red'] + ['#9d7bd8']*5,
            text=[f"{p:.1%}" for p in probs],
            textposition='auto'
        ))
        fig.update_layout(
            title=f"Poisson Distribution (λ={lambda_5y})",
            xaxis_title="Number of Crashes",
            yaxis_title="Probability",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Probability Simulations")
    
    exercise_type = st.selectbox(
        "Choose an exercise:",
        ["Binomial Distribution", "Normal Distribution", "Bayes' Theorem Simulator", 
         "Monte Carlo Simulation"]
    )
    
    if exercise_type == "Binomial Distribution":
        st.subheader("🎯 Binomial Distribution Explorer")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            n = st.slider("Number of trials (n):", 1, 100, 20)
            p = st.slider("Success probability (p):", 0.0, 1.0, 0.5, 0.01)
            k_target = st.slider("Target successes (k):", 0, n, n//2)
            
            # Calculate probabilities
            p_exact = binomial_probability(n, k_target, p)
            p_at_most = sum([binomial_probability(n, k, p) for k in range(k_target+1)])
            p_at_least = sum([binomial_probability(n, k, p) for k in range(k_target, n+1)])
            
            expected_value = n * p
            variance = n * p * (1-p)
            std_dev = np.sqrt(variance)
            
            st.markdown("**Results:**")
            st.metric("P(X = k)", f"{p_exact:.4f}")
            st.metric("P(X ≤ k)", f"{p_at_most:.4f}")
            st.metric("P(X ≥ k)", f"{p_at_least:.4f}")
            
            st.markdown("**Distribution Statistics:**")
            st.metric("Expected Value E(X)", f"{expected_value:.2f}")
            st.metric("Std Dev σ", f"{std_dev:.2f}")
        
        with col2:
            # Visualization
            k_values = range(0, n+1)
            probs = [binomial_probability(n, k, p) for k in k_values]
            colors = ['#9d7bd8' if k == k_target else '#4a4a4a' for k in k_values]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=list(k_values), y=probs, marker_color=colors))
            fig.add_vline(x=expected_value, line_dash="dash", line_color="yellow",
                         annotation_text=f"E(X)={expected_value:.1f}")
            fig.update_layout(
                title=f"Binomial Distribution (n={n}, p={p})",
                xaxis_title="Number of Successes",
                yaxis_title="Probability",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif exercise_type == "Normal Distribution":
        st.subheader("📊 Normal Distribution Explorer")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            mu = st.slider("Mean (μ):", -10.0, 10.0, 0.0, 0.1)
            sigma = st.slider("Std Dev (σ):", 0.1, 5.0, 1.0, 0.1)
            
            x_val = st.slider("Calculate P(X ≤ x):", mu-4*sigma, mu+4*sigma, mu, 0.1)
            
            # Calculate probabilities
            z_score = (x_val - mu) / sigma
            p_less_than = stats.norm.cdf(x_val, mu, sigma)
            p_greater_than = 1 - p_less_than
            
            st.markdown("**Results:**")
            st.metric("z-score", f"{z_score:.3f}")
            st.metric("P(X ≤ x)", f"{p_less_than:.4f}")
            st.metric("P(X > x)", f"{p_greater_than:.4f}")
            
            # Percentiles
            st.markdown("**Key Percentiles:**")
            p5 = stats.norm.ppf(0.05, mu, sigma)
            p50 = stats.norm.ppf(0.50, mu, sigma)
            p95 = stats.norm.ppf(0.95, mu, sigma)
            
            st.write(f"5th percentile: {p5:.2f}")
            st.write(f"50th percentile: {p50:.2f}")
            st.write(f"95th percentile: {p95:.2f}")
        
        with col2:
            # Visualization
            x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
            y = stats.norm.pdf(x, mu, sigma)
            
            fig = go.Figure()
            
            # Full distribution
            fig.add_trace(go.Scatter(
                x=x, y=y,
                fill='tozeroy',
                name='Distribution',
                line_color='#9d7bd8',
                fillcolor='rgba(157, 123, 216, 0.3)'
            ))
            
            # Shaded region
            x_shaded = x[x <= x_val]
            y_shaded = stats.norm.pdf(x_shaded, mu, sigma)
            fig.add_trace(go.Scatter(
                x=x_shaded, y=y_shaded,
                fill='tozeroy',
                name=f'P(X ≤ {x_val:.1f})',
                line_color='purple',
                fillcolor='rgba(157, 123, 216, 0.7)'
            ))
            
            fig.add_vline(x=mu, line_dash="dash", line_color="yellow",
                         annotation_text=f"μ={mu}")
            fig.add_vline(x=x_val, line_dash="dash", line_color="red",
                         annotation_text=f"x={x_val:.1f}")
            
            fig.update_layout(
                title=f"Normal Distribution (μ={mu}, σ={sigma})",
                xaxis_title="Value",
                yaxis_title="Probability Density",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif exercise_type == "Bayes' Theorem Simulator":
        st.subheader("🔄 Bayes' Theorem Calculator")
        
        st.markdown("""
        **Scenario:** Medical Test Accuracy
        
        Calculate the probability of having a disease given a positive test result.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Input Parameters:**")
            
            p_disease = st.slider("P(Disease) - Base rate:", 0.001, 0.5, 0.01, 0.001,
                                 format="%.3f")
            sensitivity = st.slider("P(Positive | Disease) - Sensitivity:", 0.5, 1.0, 0.95, 0.01)
            specificity = st.slider("P(Negative | No Disease) - Specificity:", 0.5, 1.0, 0.90, 0.01)
            
            # Calculate
            p_no_disease = 1 - p_disease
            p_pos_given_disease = sensitivity
            p_pos_given_no_disease = 1 - specificity
            
            # P(Positive)
            p_positive = (p_pos_given_disease * p_disease + 
                         p_pos_given_no_disease * p_no_disease)
            
            # P(Disease | Positive) - Bayes' Theorem
            p_disease_given_pos = (p_pos_given_disease * p_disease) / p_positive
            
        with col2:
            st.markdown("**Results:**")
            
            st.metric("P(Positive Test)", f"{p_positive:.4f}")
            st.metric("P(Disease | Positive)", f"{p_disease_given_pos:.4f}")
            
            st.markdown("**Comparison:**")
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Before Test", f"{p_disease:.2%}")
            with col_b:
                st.metric("After Positive", f"{p_disease_given_pos:.2%}")
            
            multiplier = p_disease_given_pos / p_disease
            st.info(f"The positive test increased disease probability by **{multiplier:.1f}x**")
        
        # Visualization
        categories = ['Prior\nP(Disease)', 'Posterior\nP(Disease|Pos)']
        probabilities = [p_disease, p_disease_given_pos]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=categories,
            y=probabilities,
            marker_color=['#4a4a4a', '#9d7bd8'],
            text=[f"{p:.2%}" for p in probabilities],
            textposition='auto'
        ))
        fig.update_layout(
            title="Bayesian Update",
            yaxis_title="Probability",
            yaxis_tickformat='.0%',
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif exercise_type == "Monte Carlo Simulation":
        st.subheader("🎲 Monte Carlo Simulation - Portfolio Returns")
        
        st.markdown("""
        Simulate future portfolio values using random sampling.
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            initial_value = st.number_input("Initial Portfolio Value:", 
                                          value=100000, step=10000)
            annual_return = st.slider("Expected Annual Return (%):", 
                                     -10.0, 30.0, 8.0, 0.5)
            annual_volatility = st.slider("Annual Volatility (%):", 
                                         1.0, 50.0, 15.0, 1.0)
            years = st.slider("Time Horizon (years):", 1, 30, 10)
            n_simulations = st.slider("Number of Simulations:", 
                                     100, 10000, 1000, 100)
            
            if st.button("Run Simulation"):
                # Convert to daily
                daily_return = annual_return / 252
                daily_vol = annual_volatility / np.sqrt(252)
                n_days = years * 252
                
                # Run simulations
                np.random.seed(42)
                simulations = np.zeros((n_simulations, n_days + 1))
                simulations[:, 0] = initial_value
                
                for i in range(n_simulations):
                    for day in range(1, n_days + 1):
                        daily_change = np.random.normal(daily_return/100, daily_vol/100)
                        simulations[i, day] = simulations[i, day-1] * (1 + daily_change)
                
                # Statistics
                final_values = simulations[:, -1]
                
                st.markdown("**Results:**")
                st.metric("Mean Final Value", f"${np.mean(final_values):,.0f}")
                st.metric("Median Final Value", f"${np.median(final_values):,.0f}")
                st.metric("5th Percentile (95% VaR)", f"${np.percentile(final_values, 5):,.0f}")
                st.metric("95th Percentile", f"${np.percentile(final_values, 95):,.0f}")
                
                # Store in session state
                st.session_state['simulations'] = simulations
                st.session_state['years'] = years
        
        with col2:
            if 'simulations' in st.session_state:
                simulations = st.session_state['simulations']
                years_sim = st.session_state['years']
                
                # Plot
                fig = go.Figure()
                
                # Plot first 100 paths
                days = np.linspace(0, years_sim, simulations.shape[1])
                for i in range(min(100, simulations.shape[0])):
                    fig.add_trace(go.Scatter(
                        x=days,
                        y=simulations[i],
                        mode='lines',
                        line=dict(width=0.5),
                        opacity=0.3,
                        showlegend=False,
                        hoverinfo='skip'
                    ))
                
                # Add median
                median_path = np.median(simulations, axis=0)
                fig.add_trace(go.Scatter(
                    x=days,
                    y=median_path,
                    mode='lines',
                    line=dict(color='yellow', width=3),
                    name='Median'
                ))
                
                fig.update_layout(
                    title="Monte Carlo Simulation - Portfolio Value",
                    xaxis_title="Years",
                    yaxis_title="Portfolio Value ($)",
                    template="plotly_dark",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Probability Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["Binomial Probability", "Normal Distribution", "Bayes' Theorem", 
         "Expected Value & Variance"]
    )
    
    if calc_type == "Binomial Probability":
        st.subheader("Binomial Probability Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            n = st.number_input("Number of trials (n):", min_value=1, value=10)
            p = st.number_input("Success probability (p):", 
                              min_value=0.0, max_value=1.0, value=0.5, step=0.01)
            k = st.number_input("Number of successes (k):", 
                              min_value=0, max_value=int(n), value=5)
            
            if st.button("Calculate"):
                p_exact = binomial_probability(n, k, p)
                p_at_most = sum([binomial_probability(n, i, p) for i in range(k+1)])
                p_at_least = sum([binomial_probability(n, i, p) for i in range(k, n+1)])
                
                expected = n * p
                variance = n * p * (1-p)
                
                st.markdown("**Results:**")
                st.metric("P(X = k)", f"{p_exact:.6f}")
                st.metric("P(X ≤ k)", f"{p_at_most:.6f}")
                st.metric("P(X ≥ k)", f"{p_at_least:.6f}")
                
                st.markdown("**Distribution Stats:**")
                st.metric("Expected Value", f"{expected:.4f}")
                st.metric("Variance", f"{variance:.4f}")
                st.metric("Std Dev", f"{np.sqrt(variance):.4f}")
        
        with col2:
            st.markdown("**Formula:**")
            st.latex(r"P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}")
            
            st.markdown("**Example Use Cases:**")
            st.info("""
            - Number of winning trades
            - Number of loan defaults
            - Success rate in sales calls
            - Quality control pass/fail
            """)
    
    elif calc_type == "Normal Distribution":
        st.subheader("Normal Distribution Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            mu = st.number_input("Mean (μ):", value=0.0)
            sigma = st.number_input("Std Dev (σ):", min_value=0.1, value=1.0)
            x = st.number_input("Value (x):", value=0.0)
            
            if st.button("Calculate"):
                # Probabilities
                z = (x - mu) / sigma
                p_less = stats.norm.cdf(x, mu, sigma)
                p_greater = 1 - p_less
                pdf = stats.norm.pdf(x, mu, sigma)
                
                # Percentiles
                p68_lower = mu - sigma
                p68_upper = mu + sigma
                p95_lower = mu - 1.96*sigma
                p95_upper = mu + 1.96*sigma
                
                st.markdown("**Results:**")
                st.metric("Z-score", f"{z:.4f}")
                st.metric("P(X ≤ x)", f"{p_less:.6f}")
                st.metric("P(X > x)", f"{p_greater:.6f}")
                st.metric("Density f(x)", f"{pdf:.6f}")
                
                st.markdown("**Confidence Intervals:**")
                st.write(f"68% CI: [{p68_lower:.2f}, {p68_upper:.2f}]")
                st.write(f"95% CI: [{p95_lower:.2f}, {p95_upper:.2f}]")
        
        with col2:
            st.markdown("**Formula:**")
            st.latex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}")
            
            st.markdown("**Z-score:**")
            st.latex(r"z = \frac{x - \mu}{\sigma}")
            
            st.markdown("**Applications:**")
            st.info("""
            - Stock return analysis
            - Value at Risk (VaR)
            - Hypothesis testing
            - Quality control limits
            """)
    
    elif calc_type == "Bayes' Theorem":
        st.subheader("Bayes' Theorem Calculator")
        
        st.markdown("""
        Calculate P(A|B) given P(B|A), P(A), and P(B)
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            p_a = st.number_input("P(A) - Prior probability:", 
                                 min_value=0.0, max_value=1.0, value=0.1, step=0.01)
            p_b_given_a = st.number_input("P(B|A) - Likelihood:", 
                                         min_value=0.0, max_value=1.0, value=0.8, step=0.01)
            p_b_given_not_a = st.number_input("P(B|not A):", 
                                             min_value=0.0, max_value=1.0, value=0.2, step=0.01)
            
            if st.button("Calculate"):
                # Calculate P(B) using law of total probability
                p_not_a = 1 - p_a
                p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a
                
                # Bayes' Theorem
                p_a_given_b = (p_b_given_a * p_a) / p_b
                
                st.markdown("**Results:**")
                st.metric("P(B)", f"{p_b:.6f}")
                st.metric("P(A|B) - Posterior", f"{p_a_given_b:.6f}")
                
                # Comparison
                st.markdown("**Bayesian Update:**")
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Prior P(A)", f"{p_a:.4f}")
                with col_b:
                    st.metric("Posterior P(A|B)", f"{p_a_given_b:.4f}")
                
                multiplier = p_a_given_b / p_a
                st.info(f"Evidence multiplied probability by **{multiplier:.2f}x**")
        
        with col2:
            st.markdown("**Formula:**")
            st.latex(r"P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}")
            
            st.markdown("**Where:**")
            st.latex(r"P(B) = P(B|A) \times P(A) + P(B|\neg A) \times P(\neg A)")
            
            st.markdown("**Applications:**")
            st.info("""
            - Credit risk assessment
            - Fraud detection
            - Medical diagnosis
            - Investment signals
            - Updating forecasts
            """)
    
    elif calc_type == "Expected Value & Variance":
        st.subheader("Expected Value & Variance Calculator")
        
        st.markdown("""
        Enter outcomes and their probabilities to calculate expected value and variance.
        """)
        
        # Number of outcomes
        n_outcomes = st.number_input("Number of outcomes:", 
                                    min_value=2, max_value=10, value=3)
        
        # Input table
        data = []
        for i in range(n_outcomes):
            col1, col2 = st.columns(2)
            with col1:
                outcome = st.number_input(f"Outcome {i+1}:", value=float(i), key=f"outcome_{i}")
            with col2:
                prob = st.number_input(f"Probability {i+1}:", 
                                      min_value=0.0, max_value=1.0, value=1.0/n_outcomes,
                                      step=0.01, key=f"prob_{i}")
            data.append((outcome, prob))
        
        if st.button("Calculate"):
            outcomes = [d[0] for d in data]
            probs = [d[1] for d in data]
            
            # Validate probabilities
            total_prob = sum(probs)
            
            if abs(total_prob - 1.0) > 0.01:
                st.error(f"Probabilities must sum to 1.0 (current sum: {total_prob:.4f})")
            else:
                # Calculate expected value
                expected_value = sum(o * p for o, p in zip(outcomes, probs))
                
                # Calculate variance
                variance = sum(p * (o - expected_value)**2 
                             for o, p in zip(outcomes, probs))
                std_dev = np.sqrt(variance)
                
                # Display results
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Expected Value E(X)", f"{expected_value:.4f}")
                    st.metric("Variance Var(X)", f"{variance:.4f}")
                    st.metric("Std Dev σ", f"{std_dev:.4f}")
                
                with col2:
                    # Create distribution table
                    df = pd.DataFrame({
                        'Outcome': outcomes,
                        'Probability': probs,
                        'Weighted Value': [o*p for o, p in zip(outcomes, probs)]
                    })
                    st.dataframe(df, use_container_width=True)
                
                # Visualization
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=outcomes,
                    y=probs,
                    marker_color='#9d7bd8',
                    text=[f"{p:.3f}" for p in probs],
                    textposition='auto'
                ))
                fig.add_vline(x=expected_value, line_dash="dash", line_color="yellow",
                             annotation_text=f"E(X)={expected_value:.2f}")
                fig.update_layout(
                    title="Probability Distribution",
                    xaxis_title="Outcome",
                    yaxis_title="Probability",
                    template="plotly_dark",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.markdown("**Formulas:**")
                st.latex(r"E(X) = \sum x_i \cdot P(x_i)")
                st.latex(r"Var(X) = \sum P(x_i) \cdot (x_i - E(X))^2")

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 2 Quiz: Probability Theory")
    
    # Initialize session state
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'The probability of any event must be:',
            'options': ['Between -1 and 1', 'Between 0 and 1', 'Between 0 and 100', 'Any real number'],
            'correct': 'Between 0 and 1',
            'explanation': 'Probability is always between 0 (impossible) and 1 (certain).'
        },
        {
            'id': 2,
            'question': 'If two events A and B are independent, then P(A ∩ B) equals:',
            'options': ['P(A) + P(B)', 'P(A) × P(B)', 'P(A) - P(B)', 'P(A) / P(B)'],
            'correct': 'P(A) × P(B)',
            'explanation': 'For independent events, the probability of both occurring is the product of their individual probabilities.'
        },
        {
            'id': 3,
            'question': 'Bayes\' theorem is used to:',
            'options': ['Calculate expected value', 'Update probabilities based on new evidence', 
                       'Find variance', 'Calculate correlation'],
            'correct': 'Update probabilities based on new evidence',
            'explanation': 'Bayes\' theorem allows us to revise prior probabilities when new information becomes available.'
        },
        {
            'id': 4,
            'question': 'Which distribution is most appropriate for modeling stock prices?',
            'options': ['Normal', 'Lognormal', 'Binomial', 'Poisson'],
            'correct': 'Lognormal',
            'explanation': 'Lognormal distribution is used for stock prices because prices cannot be negative and returns are approximately normal.'
        },
        {
            'id': 5,
            'question': 'A binomial distribution requires:',
            'options': ['Continuous outcomes', 'Fixed number of trials with two outcomes', 
                       'Infinite trials', 'Normal distribution of outcomes'],
            'correct': 'Fixed number of trials with two outcomes',
            'explanation': 'Binomial distribution models n independent trials, each with success or failure.'
        },
        {
            'id': 6,
            'question': 'In a standard normal distribution, what percentage of data falls within 2 standard deviations?',
            'options': ['68%', '95%', '99.7%', '50%'],
            'correct': '95%',
            'explanation': 'Approximately 95% of data in a normal distribution falls within ±2 standard deviations of the mean.'
        },
        {
            'id': 7,
            'question': 'The Poisson distribution is best used for:',
            'options': ['Continuous random variables', 'Rare events in a fixed interval', 
                       'Binary outcomes', 'Normally distributed data'],
            'correct': 'Rare events in a fixed interval',
            'explanation': 'Poisson distribution models the number of rare events occurring in a fixed time or space interval.'
        },
        {
            'id': 8,
            'question': 'Expected value is calculated as:',
            'options': ['Sum of all outcomes', 'Sum of outcomes times their probabilities', 
                       'Average of outcomes', 'Median of outcomes'],
            'correct': 'Sum of outcomes times their probabilities',
            'explanation': 'E(X) = Σ xᵢ × P(xᵢ) - each outcome weighted by its probability.'
        },
        {
            'id': 9,
            'question': 'If P(A) = 0.3 and P(B) = 0.4 and A and B are mutually exclusive, then P(A ∪ B) is:',
            'options': ['0.12', '0.70', '0.10', '1.00'],
            'correct': '0.70',
            'explanation': 'For mutually exclusive events, P(A ∪ B) = P(A) + P(B) = 0.3 + 0.4 = 0.7'
        },
        {
            'id': 10,
            'question': 'Value at Risk (VaR) at 95% confidence represents:',
            'options': ['Average loss', 'Maximum loss 95% of the time', 
                       'Loss exceeded only 5% of the time', 'Expected profit'],
            'correct': 'Loss exceeded only 5% of the time',
            'explanation': 'VaR at 95% is the threshold below which losses will fall 95% of the time (exceeded only 5% of the time).'
        }
    ]
    
    # Display questions
    for q in questions:
        st.subheader(f"Question {q['id']}")
        st.markdown(f"**{q['question']}**")
        
        answer = st.radio(
            f"Select your answer:",
            q['options'],
            key=f"q{q['id']}",
            disabled=st.session_state.quiz_submitted
        )
        
        st.session_state.quiz_answers[q['id']] = answer
        
        if st.session_state.quiz_submitted:
            if answer == q['correct']:
                st.success(f"✅ Correct! {q['explanation']}")
            else:
                st.error(f"❌ Incorrect. Correct answer: **{q['correct']}**")
                st.info(q['explanation'])
        
        st.markdown("---")
    
    # Buttons
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
    
    # Score
    if st.session_state.quiz_submitted:
        correct = sum(1 for q in questions 
                     if st.session_state.quiz_answers.get(q['id']) == q['correct'])
        percentage = (correct / len(questions)) * 100
        
        st.markdown("---")
        st.subheader("📊 Quiz Results")
        
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
    st.header("Module 2 Summary: Probability Theory")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **1. Probability Rules**
        - 0 ≤ P(E) ≤ 1
        - P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
        - P(A ∩ B) = P(A) × P(B) for independent events
        - P(A|B) = P(A ∩ B) / P(B) for conditional probability
        """)
        
        st.success("""
        **3. Discrete Distributions**
        - **Binomial:** Fixed trials, two outcomes
        - **Poisson:** Rare events in interval
        - Use for counting events
        - Success/failure scenarios
        """)
    
    with col2:
        st.warning("""
        **2. Bayes' Theorem**
        - Updates probabilities with new evidence
        - P(A|B) = P(B|A) × P(A) / P(B)
        - Critical for risk assessment
        - Used in credit scoring, fraud detection
        """)
        
        st.info("""
        **4. Continuous Distributions**
        - **Normal:** Most important in finance
        - **Lognormal:** For stock prices
        - **t-Distribution:** Small samples
        - Foundation for risk models
        """)
    
    st.markdown("---")
    st.subheader("📐 Essential Formulas")
    
    formulas_df = pd.DataFrame({
        'Concept': ['Binomial', 'Poisson', 'Normal PDF', 'Bayes\'', 'Expected Value', 'Variance'],
        'Formula': [
            'P(X=k) = C(n,k) × p^k × (1-p)^(n-k)',
            'P(X=k) = (e^(-λ) × λ^k) / k!',
            'f(x) = (1/σ√(2π)) × e^(-½((x-μ)/σ)²)',
            'P(A|B) = P(B|A) × P(A) / P(B)',
            'E(X) = Σ xᵢ × P(xᵢ)',
            'Var(X) = Σ P(xᵢ) × (xᵢ - E(X))²'
        ]
    })
    st.table(formulas_df)
    
    st.markdown("---")
    st.subheader("💼 Financial Applications")
    
    tab1, tab2, tab3 = st.tabs(["Risk Modeling", "Credit Analysis", "Portfolio Management"])
    
    with tab1:
        st.markdown("""
        **Probability in Risk Modeling:**
        
        1. **VaR Calculation:** Use normal distribution to estimate maximum loss
        2. **Stress Testing:** Model probability of extreme events (Poisson)
        3. **Monte Carlo:** Simulate thousands of scenarios using probability distributions
        4. **Confidence Intervals:** Estimate range of possible outcomes
        """)
    
    with tab2:
        st.markdown("""
        **Bayes' Theorem in Credit:**
        
        1. **Prior:** Historical default rate (e.g., 3%)
        2. **Likelihood:** P(Poor Score | Default) = 80%
        3. **Evidence:** Borrower has poor score
        4. **Posterior:** Updated default probability (e.g., 11%)
        
        This allows dynamic risk assessment as new information arrives.
        """)
    
    with tab3:
        st.markdown("""
        **Portfolio Applications:**
        
        1. **Expected Return:** E(R) = Σ wᵢ × rᵢ
        2. **Portfolio Risk:** Uses covariance and correlation
        3. **Diversification:** Probability of joint losses
        4. **Scenario Analysis:** Assign probabilities to outcomes
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 3?**
    
    Module 3: Statistical Inference will teach you:
    - Sampling and estimation
    - Hypothesis testing
    - Confidence intervals
    - Making decisions from data
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #b8a3d6; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 2 of 12: Probability Theory</p>
</div>
""", unsafe_allow_html=True)