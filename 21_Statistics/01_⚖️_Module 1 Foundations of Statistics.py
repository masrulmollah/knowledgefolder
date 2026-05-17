import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0a1628 0%, #1a2942 50%, #2a3f5f 100%);
    }
    .stTab {
        background-color: rgba(26, 41, 66, 0.6);
        border-radius: 10px;
        padding: 20px;
    }
    h1 {
        color: #d4af37;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #d4af37 0%, #f4e5b8 50%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    h2 {
        color: #f4e5b8;
        border-left: 6px solid #d4af37;
        padding-left: 15px;
    }
    h3 {
        color: #a8c5dd;
    }
    .stAlert {
        background-color: rgba(212, 175, 55, 0.1);
        border: 2px solid #d4af37;
        border-radius: 10px;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>📊 Module 1: Foundations of Statistics</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #a8c5dd;'>Building Blocks for Financial Analysis</h3>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 1 of 12**\n\nStatistics for Finance Professionals")

# Helper functions
def calculate_descriptive_stats(data):
    """Calculate comprehensive descriptive statistics"""
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': stats.mode(data, keepdims=True)[0][0] if len(data) > 0 else 0,
        'std': np.std(data, ddof=0),
        'variance': np.var(data, ddof=0),
        'min': np.min(data),
        'max': np.max(data),
        'range': np.max(data) - np.min(data),
        'q1': np.percentile(data, 25),
        'q3': np.percentile(data, 75),
        'iqr': np.percentile(data, 75) - np.percentile(data, 25),
        'skewness': stats.skew(data),
        'kurtosis': stats.kurtosis(data)
    }

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("1.1 Data Types and Collection")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Quantitative Data")
        st.info("""
        **Numerical data that can be measured and expressed mathematically**
        
        Examples in Finance:
        - Stock prices: $150.23, $148.90
        - Returns: 2.5%, -1.3%
        - Trading volume: 1,234,567 shares
        - Revenue: $2.5M
        - P/E ratios: 15.2, 22.8
        """)
        
    with col2:
        st.subheader("📝 Qualitative Data")
        st.info("""
        **Categorical data describing characteristics or qualities**
        
        Examples in Finance:
        - Credit ratings: AAA, BB+, CCC
        - Industry sector: Technology, Finance
        - Market sentiment: Bullish, Bearish
        - Risk level: Low, Medium, High
        - Bond grade: Investment, Speculative
        """)
    
    st.markdown("---")
    
    st.header("Data Structures in Finance")
    
    st.subheader("🕒 Time Series Data")
    st.success("""
    **Definition:** Observations collected over time at regular intervals.
    
    **Applications:** 
    - Tracking stock price movements
    - Analyzing returns over time
    - Economic indicator trends
    - Revenue growth patterns
    
    **Example:** Daily closing prices of AAPL stock from 2020-2025
    """)
    
    st.subheader("📊 Cross-Sectional Data")
    st.warning("""
    **Definition:** Observations across different entities at a single point in time.
    
    **Applications:** 
    - Comparing company valuations
    - Industry peer analysis
    - Portfolio composition analysis
    - Market cap rankings
    
    **Example:** P/E ratios of all S&P 500 companies on December 31, 2025
    """)
    
    st.subheader("🎯 Panel Data")
    st.info("""
    **Definition:** Combines both time series and cross-sectional dimensions.
    
    **Applications:** 
    - Multi-company financial analysis
    - Longitudinal performance studies
    - Economic policy impact studies
    
    **Example:** Quarterly earnings of 100 companies from 2020-2025
    """)
    
    st.markdown("---")
    
    st.header("1.2 Descriptive Statistics")
    
    st.subheader("📍 Measures of Central Tendency")
    
    # Mean
    with st.expander("**Mean (Average)** - Click to expand", expanded=True):
        st.latex(r"\mu = \frac{\sum_{i=1}^{n} x_i}{n}")
        st.markdown("""
        **Where:**
        - μ (mu) = population mean
        - xᵢ = individual values
        - n = number of observations
        
        **Financial Application:** Average portfolio return over time
        
        **Key Point:** Sensitive to outliers - one extreme value can significantly affect the mean
        """)
    
    # Median
    with st.expander("**Median** - Click to expand"):
        st.markdown("""
        **Definition:** The middle value when data is ordered from smallest to largest.
        
        **Calculation:**
        - If n is odd: median is the middle value
        - If n is even: median is the average of the two middle values
        
        **Financial Application:** Median home prices in real estate analysis
        
        **Key Point:** Robust to outliers - not affected by extreme values
        """)
    
    # Mode
    with st.expander("**Mode** - Click to expand"):
        st.markdown("""
        **Definition:** The most frequently occurring value in a dataset.
        
        **Note:** A dataset can have:
        - No mode (all values unique)
        - One mode (unimodal)
        - Multiple modes (bimodal, multimodal)
        
        **Financial Application:** Most common transaction amount in payment processing
        """)
    
    st.markdown("---")
    
    st.subheader("📏 Measures of Dispersion")
    
    # Variance
    with st.expander("**Variance (σ²)** - Click to expand", expanded=True):
        st.latex(r"\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}")
        st.markdown("""
        **Definition:** Average of squared deviations from the mean
        
        **Units:** Square of the original data units
        
        **Financial Application:** Portfolio risk measurement (though standard deviation is more commonly used)
        """)
    
    # Standard Deviation
    with st.expander("**Standard Deviation (σ)** - Click to expand", expanded=True):
        st.latex(r"\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}}")
        st.markdown("""
        **Definition:** Square root of variance, in same units as original data
        
        **Interpretation:**
        - Higher σ = More spread out data = Higher risk
        - Lower σ = Data clustered around mean = Lower risk
        
        **Financial Application:** 
        - **VOLATILITY** in financial markets
        - Risk measurement for investments
        - Portfolio variance calculation
        
        **Critical for Finance:** Standard Deviation = Volatility = Risk
        """)
    
    # Range and IQR
    with st.expander("**Range & Interquartile Range (IQR)** - Click to expand"):
        st.markdown("""
        **Range:**
        """)
        st.latex(r"\text{Range} = \text{Maximum} - \text{Minimum}")
        
        st.markdown("""
        **Interquartile Range (IQR):**
        """)
        st.latex(r"\text{IQR} = Q_3 - Q_1")
        
        st.markdown("""
        **Where:**
        - Q₁ = 25th percentile (1st quartile)
        - Q₃ = 75th percentile (3rd quartile)
        
        **Interpretation:** IQR represents the spread of the middle 50% of data
        
        **Financial Application:** Identifying outliers in trading data
        """)
    
    # Skewness and Kurtosis
    with st.expander("**Skewness & Kurtosis** - Click to expand"):
        st.markdown("""
        **Skewness:**
        - Measures asymmetry of the distribution
        - Positive skew: right tail is longer (mean > median)
        - Negative skew: left tail is longer (mean < median)
        - Zero skew: symmetric distribution
        
        **Kurtosis:**
        - Measures "tailedness" of the distribution
        - High kurtosis: heavy tails, more outliers
        - Low kurtosis: light tails, fewer outliers
        
        **Financial Application:** 
        - Return distributions often exhibit skewness
        - Risk analysis for extreme events (tail risk)
        """)
    
    st.markdown("---")
    
    st.success("""
    ### 💡 Key Insight for Finance
    
    In financial analysis:
    - **Standard Deviation = Volatility = Risk**
    - **Mean = Expected Return**
    - **Sharpe Ratio = (Return - Risk-Free Rate) / Standard Deviation**
    
    The relationship between return and risk is fundamental to all investment decisions.
    """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Real-World Financial Examples")
    
    # Example 1: Stock Returns
    st.subheader("Example 1: Analyzing Stock Returns")
    
    st.markdown("""
    **Scenario:** You're analyzing daily returns of a tech stock over 10 trading days.
    """)
    
    returns_data = [2.3, -1.2, 0.8, 3.1, -0.5, 1.7, 2.8, -2.1, 1.5, 0.9]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.code(f"Returns (%): {returns_data}", language="python")
        
        # Calculate statistics
        stats_results = calculate_descriptive_stats(returns_data)
        
        st.markdown("**Calculations:**")
        st.metric("Mean Return", f"{stats_results['mean']:.2f}%")
        st.metric("Standard Deviation (Volatility)", f"{stats_results['std']:.2f}%")
        st.metric("Min Return", f"{stats_results['min']:.2f}%")
        st.metric("Max Return", f"{stats_results['max']:.2f}%")
        
        st.markdown(f"""
        **Interpretation:**
        - Average daily return: **{stats_results['mean']:.2f}%**
        - Daily volatility (risk): **{stats_results['std']:.2f}%**
        - The stock shows moderate volatility with positive average returns
        """)
    
    with col2:
        # Create visualization
        df_returns = pd.DataFrame({
            'Day': list(range(1, 11)),
            'Return': returns_data
        })
        
        fig = px.line(df_returns, x='Day', y='Return', 
                     title='Daily Stock Returns',
                     markers=True)
        fig.update_traces(line_color='#d4af37', marker=dict(size=10))
        fig.update_layout(template="plotly_dark", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 2: Portfolio Volatility
    st.subheader("Example 2: Portfolio Volatility Calculation")
    
    st.markdown("""
    **Problem:** Calculate the annual volatility of a portfolio with monthly returns.
    """)
    
    monthly_returns = [2.1, -0.5, 1.8, 3.2, -1.1, 2.5, 1.9, 0.7, -0.3, 2.8, 1.4, 0.6]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code(f"Monthly Returns (%): {monthly_returns}", language="python")
        
        # Calculate statistics
        monthly_mean = np.mean(monthly_returns)
        monthly_std = np.std(monthly_returns, ddof=0)
        annual_std = monthly_std * np.sqrt(12)
        
        st.markdown("**Step-by-Step Solution:**")
        st.markdown(f"1. **Mean monthly return:** {monthly_mean:.2f}%")
        st.markdown(f"2. **Monthly standard deviation:** {monthly_std:.2f}%")
        st.markdown(f"3. **Annualization factor:** √12 = {np.sqrt(12):.2f}")
        st.markdown(f"4. **Annual volatility:** {monthly_std:.2f}% × {np.sqrt(12):.2f} = **{annual_std:.2f}%**")
        
    with col2:
        # Visualization
        df_monthly = pd.DataFrame({
            'Month': range(1, 13),
            'Return': monthly_returns
        })
        
        fig = px.bar(df_monthly, x='Month', y='Return', 
                     title='Monthly Portfolio Returns',
                     color='Return',
                     color_continuous_scale=['red', 'yellow', 'green'])
        fig.update_layout(template="plotly_dark", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.success(f"""
    **Result:** The portfolio has an annualized volatility of **{annual_std:.2f}%**, 
    indicating moderate risk.
    """)
    
    st.markdown("---")
    
    # Example 3: Comparing Investments
    st.subheader("Example 3: Comparing Two Investment Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Investment A: Stable Bond Fund**")
        bond_returns = [0.5, 0.6, 0.4, 0.5, 0.6, 0.5, 0.4, 0.5, 0.6, 0.5]
        bond_stats = calculate_descriptive_stats(bond_returns)
        
        st.metric("Mean Return", f"{bond_stats['mean']:.2f}%")
        st.metric("Volatility (Std Dev)", f"{bond_stats['std']:.2f}%")
        st.metric("Sharpe Ratio*", f"{(bond_stats['mean'] - 0.3) / bond_stats['std']:.2f}")
        
        st.caption("*Assuming risk-free rate = 0.3%")
        
    with col2:
        st.markdown("**Investment B: Growth Stock**")
        stock_returns = [3.2, -1.5, 4.1, -2.3, 5.2, 1.8, -0.9, 3.7, 2.1, -1.4]
        stock_stats = calculate_descriptive_stats(stock_returns)
        
        st.metric("Mean Return", f"{stock_stats['mean']:.2f}%")
        st.metric("Volatility (Std Dev)", f"{stock_stats['std']:.2f}%")
        st.metric("Sharpe Ratio*", f"{(stock_stats['mean'] - 0.3) / stock_stats['std']:.2f}")
        
        st.caption("*Assuming risk-free rate = 0.3%")
    
    # Comparison
    comparison_df = pd.DataFrame({
        'Metric': ['Mean Return (%)', 'Std Dev (%)', 'Sharpe Ratio'],
        'Bond Fund': [f"{bond_stats['mean']:.2f}", f"{bond_stats['std']:.2f}", 
                      f"{(bond_stats['mean'] - 0.3) / bond_stats['std']:.2f}"],
        'Growth Stock': [f"{stock_stats['mean']:.2f}", f"{stock_stats['std']:.2f}",
                        f"{(stock_stats['mean'] - 0.3) / stock_stats['std']:.2f}"]
    })
    
    st.table(comparison_df)
    
    st.info("""
    **Analysis:**
    - **Bond Fund:** Low return, low risk, moderate risk-adjusted return
    - **Growth Stock:** Higher return, higher risk, better risk-adjusted return (higher Sharpe ratio)
    
    The Growth Stock offers better compensation for the risk taken.
    """)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Statistical Analysis")
    
    st.markdown("""
    Modify the dataset below and observe how descriptive statistics change in real-time.
    This helps you understand the relationship between data and its statistical measures.
    """)
    
    # Input method selection
    input_method = st.radio("Choose input method:", 
                           ["Manual Entry", "Upload CSV", "Generate Random Data"])
    
    if input_method == "Manual Entry":
        default_data = "85, 92, 78, 95, 88, 76, 90, 82, 91, 87"
        user_input = st.text_area(
            "Enter your data (comma-separated):",
            value=default_data,
            height=100
        )
        
        try:
            data = [float(x.strip()) for x in user_input.split(',') if x.strip()]
        except:
            st.error("Please enter valid numbers separated by commas")
            data = [85, 92, 78, 95, 88, 76, 90, 82, 91, 87]
    
    elif input_method == "Upload CSV":
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            col = st.selectbox("Select column:", df.columns)
            data = df[col].dropna().tolist()
        else:
            st.info("Please upload a CSV file")
            data = [85, 92, 78, 95, 88, 76, 90, 82, 91, 87]
    
    else:  # Generate Random Data
        col1, col2, col3 = st.columns(3)
        with col1:
            n_points = st.slider("Number of points:", 10, 100, 50)
        with col2:
            mean_val = st.slider("Mean:", 0.0, 100.0, 50.0)
        with col3:
            std_val = st.slider("Std Dev:", 1.0, 30.0, 10.0)
        
        data = np.random.normal(mean_val, std_val, n_points).tolist()
    
    # Calculate statistics
    if len(data) > 0:
        stats_dict = calculate_descriptive_stats(data)
        
        st.markdown("---")
        st.subheader("📊 Calculated Statistics")
        
        # Display metrics in columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Mean", f"{stats_dict['mean']:.2f}")
            st.metric("Median", f"{stats_dict['median']:.2f}")
        
        with col2:
            st.metric("Std Dev", f"{stats_dict['std']:.2f}")
            st.metric("Variance", f"{stats_dict['variance']:.2f}")
        
        with col3:
            st.metric("Min", f"{stats_dict['min']:.2f}")
            st.metric("Max", f"{stats_dict['max']:.2f}")
        
        with col4:
            st.metric("Range", f"{stats_dict['range']:.2f}")
            st.metric("IQR", f"{stats_dict['iqr']:.2f}")
        
        # Additional statistics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Skewness", f"{stats_dict['skewness']:.3f}")
        with col2:
            st.metric("Kurtosis", f"{stats_dict['kurtosis']:.3f}")
        
        st.markdown("---")
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # Histogram
            fig1 = go.Figure()
            fig1.add_trace(go.Histogram(
                x=data,
                nbinsx=20,
                marker_color='#d4af37',
                opacity=0.7,
                name='Frequency'
            ))
            fig1.add_vline(x=stats_dict['mean'], line_dash="dash", 
                          line_color="red", annotation_text="Mean")
            fig1.add_vline(x=stats_dict['median'], line_dash="dash", 
                          line_color="green", annotation_text="Median")
            fig1.update_layout(
                title="Distribution Histogram",
                xaxis_title="Value",
                yaxis_title="Frequency",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Box plot
            fig2 = go.Figure()
            fig2.add_trace(go.Box(
                y=data,
                marker_color='#d4af37',
                name='Data'
            ))
            fig2.update_layout(
                title="Box Plot (Shows Quartiles and Outliers)",
                yaxis_title="Value",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        # Summary statistics table
        st.subheader("📋 Summary Statistics Table")
        summary_df = pd.DataFrame({
            'Statistic': ['Count', 'Mean', 'Median', 'Mode', 'Std Dev', 'Variance', 
                         'Min', 'Q1', 'Q2 (Median)', 'Q3', 'Max', 'Range', 'IQR', 
                         'Skewness', 'Kurtosis'],
            'Value': [
                len(data),
                f"{stats_dict['mean']:.4f}",
                f"{stats_dict['median']:.4f}",
                f"{stats_dict['mode']:.4f}",
                f"{stats_dict['std']:.4f}",
                f"{stats_dict['variance']:.4f}",
                f"{stats_dict['min']:.4f}",
                f"{stats_dict['q1']:.4f}",
                f"{stats_dict['median']:.4f}",
                f"{stats_dict['q3']:.4f}",
                f"{stats_dict['max']:.4f}",
                f"{stats_dict['range']:.4f}",
                f"{stats_dict['iqr']:.4f}",
                f"{stats_dict['skewness']:.4f}",
                f"{stats_dict['kurtosis']:.4f}"
            ]
        })
        st.dataframe(summary_df, use_container_width=True)
        
        # Practice exercises
        st.markdown("---")
        st.subheader("🎯 Try These Exercises:")
        
        st.info("""
        1. **Outlier Effect:** Add an extreme value (e.g., 500) and observe how it affects mean vs median
        2. **Low Variance:** Create data with values close together (e.g., 50, 51, 49, 52, 50)
        3. **High Variance:** Create data with values spread far apart (e.g., 10, 90, 20, 80, 30, 70)
        4. **Uniform Distribution:** Make all values equal and see what happens to standard deviation
        5. **Skewness:** Create right-skewed data (many small values, few large ones)
        """)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Descriptive Statistics Calculator")
    
    st.markdown("""
    Enter your financial data to calculate comprehensive descriptive statistics instantly.
    Perfect for quick portfolio analysis, risk assessment, or data exploration.
    """)
    
    # Calculator tabs
    calc_tab1, calc_tab2 = st.tabs(["📊 Single Dataset", "⚖️ Compare Two Datasets"])
    
    with calc_tab1:
        st.subheader("Single Dataset Analysis")
        
        data_input = st.text_area(
            "Enter data (comma-separated):",
            placeholder="Example: 100, 105, 98, 110, 102, 95, 108, 103, 99, 106",
            height=100
        )
        
        if st.button("Calculate Statistics", key="calc1"):
            try:
                data = [float(x.strip()) for x in data_input.split(',') if x.strip()]
                
                if len(data) == 0:
                    st.error("Please enter valid numerical data")
                else:
                    stats_dict = calculate_descriptive_stats(data)
                    
                    st.success("✅ Calculations Complete!")
                    
                    # Create metrics display
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("### Central Tendency")
                        st.metric("Mean (μ)", f"{stats_dict['mean']:.4f}")
                        st.metric("Median", f"{stats_dict['median']:.4f}")
                        st.metric("Mode", f"{stats_dict['mode']:.4f}")
                    
                    with col2:
                        st.markdown("### Dispersion")
                        st.metric("Std Dev (σ)", f"{stats_dict['std']:.4f}")
                        st.metric("Variance (σ²)", f"{stats_dict['variance']:.4f}")
                        st.metric("Range", f"{stats_dict['range']:.4f}")
                    
                    with col3:
                        st.markdown("### Position")
                        st.metric("Minimum", f"{stats_dict['min']:.4f}")
                        st.metric("Maximum", f"{stats_dict['max']:.4f}")
                        st.metric("IQR", f"{stats_dict['iqr']:.4f}")
                    
                    # Quartiles
                    st.markdown("### Quartiles")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Q1 (25th)", f"{stats_dict['q1']:.4f}")
                    with col2:
                        st.metric("Q2 (50th)", f"{stats_dict['median']:.4f}")
                    with col3:
                        st.metric("Q3 (75th)", f"{stats_dict['q3']:.4f}")
                    
                    # Shape
                    st.markdown("### Distribution Shape")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Skewness", f"{stats_dict['skewness']:.4f}")
                        if stats_dict['skewness'] > 0:
                            st.caption("Positive skew: Right tail longer")
                        elif stats_dict['skewness'] < 0:
                            st.caption("Negative skew: Left tail longer")
                        else:
                            st.caption("Symmetric distribution")
                    
                    with col2:
                        st.metric("Kurtosis", f"{stats_dict['kurtosis']:.4f}")
                        if stats_dict['kurtosis'] > 0:
                            st.caption("Heavy tails: More outliers")
                        else:
                            st.caption("Light tails: Fewer outliers")
                    
                    # Formulas used
                    with st.expander("📐 Formulas Used"):
                        st.latex(r"\text{Mean: } \mu = \frac{\sum x_i}{n}")
                        st.latex(r"\text{Variance: } \sigma^2 = \frac{\sum (x_i - \mu)^2}{n}")
                        st.latex(r"\text{Std Dev: } \sigma = \sqrt{\sigma^2}")
                        st.latex(r"\text{IQR: } Q_3 - Q_1")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}\nPlease enter valid numbers separated by commas")
    
    with calc_tab2:
        st.subheader("Compare Two Datasets")
        
        col1, col2 = st.columns(2)
        
        with col1:
            data1_input = st.text_area(
                "Dataset 1:",
                placeholder="Example: Stock A returns",
                height=100,
                key="data1"
            )
        
        with col2:
            data2_input = st.text_area(
                "Dataset 2:",
                placeholder="Example: Stock B returns",
                height=100,
                key="data2"
            )
        
        if st.button("Compare Datasets", key="calc2"):
            try:
                data1 = [float(x.strip()) for x in data1_input.split(',') if x.strip()]
                data2 = [float(x.strip()) for x in data2_input.split(',') if x.strip()]
                
                if len(data1) == 0 or len(data2) == 0:
                    st.error("Please enter valid data for both datasets")
                else:
                    stats1 = calculate_descriptive_stats(data1)
                    stats2 = calculate_descriptive_stats(data2)
                    
                    # Comparison table
                    comparison = pd.DataFrame({
                        'Metric': ['Count', 'Mean', 'Median', 'Std Dev', 'Variance', 
                                  'Min', 'Max', 'Range', 'IQR', 'Skewness', 'Kurtosis'],
                        'Dataset 1': [
                            len(data1),
                            f"{stats1['mean']:.4f}",
                            f"{stats1['median']:.4f}",
                            f"{stats1['std']:.4f}",
                            f"{stats1['variance']:.4f}",
                            f"{stats1['min']:.4f}",
                            f"{stats1['max']:.4f}",
                            f"{stats1['range']:.4f}",
                            f"{stats1['iqr']:.4f}",
                            f"{stats1['skewness']:.4f}",
                            f"{stats1['kurtosis']:.4f}"
                        ],
                        'Dataset 2': [
                            len(data2),
                            f"{stats2['mean']:.4f}",
                            f"{stats2['median']:.4f}",
                            f"{stats2['std']:.4f}",
                            f"{stats2['variance']:.4f}",
                            f"{stats2['min']:.4f}",
                            f"{stats2['max']:.4f}",
                            f"{stats2['range']:.4f}",
                            f"{stats2['iqr']:.4f}",
                            f"{stats2['skewness']:.4f}",
                            f"{stats2['kurtosis']:.4f}"
                        ]
                    })
                    
                    st.dataframe(comparison, use_container_width=True)
                    
                    # Visual comparison
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Histogram comparison
                        fig = go.Figure()
                        fig.add_trace(go.Histogram(x=data1, name='Dataset 1', 
                                                  opacity=0.6, marker_color='#d4af37'))
                        fig.add_trace(go.Histogram(x=data2, name='Dataset 2', 
                                                  opacity=0.6, marker_color='#a8c5dd'))
                        fig.update_layout(
                            title="Distribution Comparison",
                            barmode='overlay',
                            template="plotly_dark",
                            height=400
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        # Box plot comparison
                        fig = go.Figure()
                        fig.add_trace(go.Box(y=data1, name='Dataset 1', 
                                           marker_color='#d4af37'))
                        fig.add_trace(go.Box(y=data2, name='Dataset 2', 
                                           marker_color='#a8c5dd'))
                        fig.update_layout(
                            title="Box Plot Comparison",
                            template="plotly_dark",
                            height=400
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    # Key insights
                    st.subheader("📊 Key Insights")
                    
                    if stats1['mean'] > stats2['mean']:
                        st.info(f"Dataset 1 has a higher mean ({stats1['mean']:.2f} vs {stats2['mean']:.2f})")
                    else:
                        st.info(f"Dataset 2 has a higher mean ({stats2['mean']:.2f} vs {stats1['mean']:.2f})")
                    
                    if stats1['std'] > stats2['std']:
                        st.warning(f"Dataset 1 is more volatile (Std Dev: {stats1['std']:.2f} vs {stats2['std']:.2f})")
                    else:
                        st.warning(f"Dataset 2 is more volatile (Std Dev: {stats2['std']:.2f} vs {stats1['std']:.2f})")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}\nPlease check your input data")

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Knowledge Check Quiz")
    
    st.markdown("""
    Test your understanding of Module 1: Foundations of Statistics.
    Select the best answer for each question.
    """)
    
    # Initialize session state for quiz
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    # Quiz questions
    questions = [
        {
            'id': 1,
            'question': 'Which measure of central tendency is most affected by outliers?',
            'options': ['Mean', 'Median', 'Mode', 'Range'],
            'correct': 'Mean',
            'explanation': 'The mean is calculated using all values, so extreme outliers significantly affect it. The median only depends on the middle value(s) and is robust to outliers.'
        },
        {
            'id': 2,
            'question': 'What type of data is stock prices over time?',
            'options': ['Cross-sectional', 'Time series', 'Qualitative', 'Categorical'],
            'correct': 'Time series',
            'explanation': 'Stock prices collected over time at regular intervals form a time series dataset.'
        },
        {
            'id': 3,
            'question': 'Standard deviation is the square root of:',
            'options': ['Mean', 'Median', 'Variance', 'Range'],
            'correct': 'Variance',
            'explanation': 'Standard deviation (σ) = √(Variance). This puts the measure of spread in the same units as the original data.'
        },
        {
            'id': 4,
            'question': 'Which measure represents the spread of the middle 50% of data?',
            'options': ['Standard deviation', 'Range', 'Interquartile range', 'Variance'],
            'correct': 'Interquartile range',
            'explanation': 'IQR = Q3 - Q1 represents the range containing the middle 50% of the data (from 25th to 75th percentile).'
        },
        {
            'id': 5,
            'question': 'In finance, what does volatility typically measure?',
            'options': ['Mean return', 'Risk/uncertainty', 'Maximum return', 'Median return'],
            'correct': 'Risk/uncertainty',
            'explanation': 'Volatility, measured by standard deviation, quantifies the risk or uncertainty in investment returns.'
        },
        {
            'id': 6,
            'question': 'If a dataset has positive skewness, the mean is:',
            'options': ['Less than the median', 'Equal to the median', 'Greater than the median', 'Unrelated to the median'],
            'correct': 'Greater than the median',
            'explanation': 'Positive skewness means the right tail is longer. The mean gets pulled toward the tail and is greater than the median.'
        },
        {
            'id': 7,
            'question': 'Which is NOT a measure of dispersion?',
            'options': ['Variance', 'Standard deviation', 'Median', 'Range'],
            'correct': 'Median',
            'explanation': 'Median is a measure of central tendency, not dispersion. Variance, standard deviation, and range all measure spread.'
        },
        {
            'id': 8,
            'question': 'To annualize monthly volatility, you multiply by:',
            'options': ['12', '√12', '12²', '√252'],
            'correct': '√12',
            'explanation': 'Volatility scales with the square root of time. Annual volatility = Monthly volatility × √12.'
        },
        {
            'id': 9,
            'question': 'Panel data combines which two types of data?',
            'options': ['Qualitative and quantitative', 'Time series and cross-sectional', 'Primary and secondary', 'Discrete and continuous'],
            'correct': 'Time series and cross-sectional',
            'explanation': 'Panel data tracks multiple entities (cross-sectional) over multiple time periods (time series).'
        },
        {
            'id': 10,
            'question': 'The Sharpe ratio measures:',
            'options': ['Absolute return', 'Risk-adjusted return', 'Maximum drawdown', 'Total risk'],
            'correct': 'Risk-adjusted return',
            'explanation': 'Sharpe ratio = (Return - Risk-free rate) / Standard deviation, measuring return per unit of risk.'
        }
    ]
    
    # Display questions
    for q in questions:
        st.subheader(f"Question {q['id']}")
        st.markdown(f"**{q['question']}**")
        
        answer = st.radio(
            f"Select your answer for Question {q['id']}:",
            q['options'],
            key=f"q{q['id']}",
            disabled=st.session_state.quiz_submitted
        )
        
        st.session_state.quiz_answers[q['id']] = answer
        
        # Show result if submitted
        if st.session_state.quiz_submitted:
            if answer == q['correct']:
                st.success(f"✅ Correct! {q['explanation']}")
            else:
                st.error(f"❌ Incorrect. The correct answer is: **{q['correct']}**")
                st.info(q['explanation'])
        
        st.markdown("---")
    
    # Submit button
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if not st.session_state.quiz_submitted:
            if st.button("Submit Quiz", type="primary", use_container_width=True):
                st.session_state.quiz_submitted = True
                st.rerun()
    
    with col2:
        if st.session_state.quiz_submitted:
            if st.button("Retake Quiz", use_container_width=True):
                st.session_state.quiz_submitted = False
                st.session_state.quiz_answers = {}
                st.rerun()
    
    # Show score if submitted
    if st.session_state.quiz_submitted:
        correct_count = sum(1 for q in questions 
                          if st.session_state.quiz_answers.get(q['id']) == q['correct'])
        total_questions = len(questions)
        percentage = (correct_count / total_questions) * 100
        
        st.markdown("---")
        st.subheader("📊 Quiz Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Correct Answers", f"{correct_count}/{total_questions}")
        with col2:
            st.metric("Score", f"{percentage:.0f}%")
        with col3:
            if percentage >= 80:
                st.metric("Grade", "🌟 Excellent")
            elif percentage >= 60:
                st.metric("Grade", "👍 Good")
            else:
                st.metric("Grade", "📚 Review Needed")
        
        # Performance feedback
        if percentage == 100:
            st.balloons()
            st.success("🎉 Perfect score! You have mastered Module 1!")
        elif percentage >= 80:
            st.success("🌟 Excellent work! You have a strong understanding of the material.")
        elif percentage >= 60:
            st.info("👍 Good job! Review the topics you missed for better understanding.")
        else:
            st.warning("📚 Keep studying! Go through the theory and examples again.")

# ======================
# SUMMARY PAGE
# ======================
elif page == "📋 Summary":
    st.header("Module 1 Summary")
    
    st.markdown("""
    A comprehensive review of key concepts, formulas, and applications from Module 1.
    """)
    
    # Key Takeaways
    st.subheader("🎯 Key Takeaways")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **1️⃣ Data Types Matter**
        
        Understanding whether you're working with:
        - **Time series:** observations over time
        - **Cross-sectional:** snapshot at one time
        - **Panel data:** both dimensions combined
        
        This shapes your entire analytical approach.
        """)
        
        st.success("""
        **3️⃣ Dispersion Measures Risk**
        
        In finance:
        - **Standard Deviation = Volatility = Risk**
        - Higher σ → Higher risk
        - Lower σ → Lower risk
        
        Always pair return measures with risk measures!
        """)
    
    with col2:
        st.warning("""
        **2️⃣ Central Tendency Shows the Center**
        
        - **Mean:** Sensitive to outliers (use for symmetric data)
        - **Median:** Robust to outliers (use for skewed data)
        - **Mode:** Most frequent value
        
        Choose the right measure for your data distribution.
        """)
        
        st.info("""
        **4️⃣ Always Visualize First**
        
        Before calculating statistics:
        1. Plot your data
        2. Check for outliers
        3. Assess distribution shape
        4. Identify patterns
        
        A chart reveals what numbers might hide.
        """)
    
    st.markdown("---")
    
    # Essential Formulas
    st.subheader("📐 Essential Formulas to Remember")
    
    formulas_df = pd.DataFrame({
        'Measure': ['Mean (μ)', 'Variance (σ²)', 'Standard Deviation (σ)', 
                   'Range', 'IQR', 'Coefficient of Variation'],
        'Formula': [
            'Σxᵢ / n',
            'Σ(xᵢ - μ)² / n',
            '√(σ²)',
            'Max - Min',
            'Q₃ - Q₁',
            '(σ / μ) × 100%'
        ],
        'Financial Use': [
            'Expected return',
            'Risk measure',
            'Volatility measure',
            'Price range',
            'Outlier detection',
            'Risk comparison'
        ]
    })
    
    st.table(formulas_df)
    
    # Mathematical notation
    with st.expander("📊 View Detailed Mathematical Formulas"):
        st.markdown("**Population Mean:**")
        st.latex(r"\mu = \frac{1}{n}\sum_{i=1}^{n} x_i")
        
        st.markdown("**Population Variance:**")
        st.latex(r"\sigma^2 = \frac{1}{n}\sum_{i=1}^{n} (x_i - \mu)^2")
        
        st.markdown("**Population Standard Deviation:**")
        st.latex(r"\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n} (x_i - \mu)^2}")
        
        st.markdown("**Sample Variance (Bessel's correction):**")
        st.latex(r"s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2")
        
        st.markdown("**Coefficient of Variation:**")
        st.latex(r"CV = \frac{\sigma}{\mu} \times 100\%")
    
    st.markdown("---")
    
    # Quick Reference Table
    st.subheader("📋 Quick Reference: When to Use What")
    
    reference_df = pd.DataFrame({
        'Situation': [
            'Data has outliers',
            'Symmetric distribution',
            'Skewed distribution',
            'Comparing risk of two investments',
            'Measuring portfolio volatility',
            'Finding extreme values',
            'Detecting outliers'
        ],
        'Use This': [
            'Median instead of Mean',
            'Mean',
            'Median',
            'Standard Deviation (or CV)',
            'Standard Deviation',
            'Min and Max',
            'IQR method (Q1 - 1.5×IQR, Q3 + 1.5×IQR)'
        ]
    })
    
    st.table(reference_df)
    
    st.markdown("---")
    
    # Financial Applications Summary
    st.subheader("💼 Financial Applications Summary")
    
    tab1, tab2, tab3 = st.tabs(["Portfolio Analysis", "Risk Management", "Performance Evaluation"])
    
    with tab1:
        st.markdown("""
        **Portfolio Analysis:**
        
        1. **Calculate expected return** using mean of historical returns
        2. **Measure portfolio risk** using standard deviation
        3. **Identify diversification benefits** by comparing individual vs portfolio volatility
        4. **Detect anomalies** using IQR and outlier detection
        
        **Example:**
        - Portfolio Mean Return: 8.5% annually
        - Portfolio Std Dev: 12.3%
        - Interpretation: Moderate risk-return profile
        """)
    
    with tab2:
        st.markdown("""
        **Risk Management:**
        
        1. **Volatility measurement:** Standard deviation of returns
        2. **Value at Risk (VaR):** Use percentiles for worst-case scenarios
        3. **Stress testing:** Analyze extreme values (min/max)
        4. **Risk-adjusted returns:** Sharpe Ratio, Sortino Ratio
        
        **Key Metrics:**
        - Volatility (σ) = Risk
        - Higher σ = Higher uncertainty
        - Use for position sizing and risk limits
        """)
    
    with tab3:
        st.markdown("""
        **Performance Evaluation:**
        
        1. **Sharpe Ratio:** (Return - Risk-free rate) / Std Dev
        2. **Consistency:** Low variance indicates stable returns
        3. **Benchmark comparison:** Compare mean and std dev vs index
        4. **Distribution analysis:** Check skewness and kurtosis
        
        **Decision Framework:**
        - High return + Low volatility = Best
        - High return + High volatility = Evaluate risk tolerance
        - Low return + Low volatility = Safe but low reward
        - Low return + High volatility = Avoid
        """)
    
    st.markdown("---")
    
    # Practice Recommendations
    st.subheader("🎯 Next Steps & Practice Recommendations")
    
    st.success("""
    **To Master This Module:**
    
    1. **Practice Daily:**
       - Calculate statistics for your portfolio
       - Analyze stock returns from Yahoo Finance
       - Compare different investments
    
    2. **Build Intuition:**
       - Use the interactive calculator regularly
       - Modify datasets and observe changes
       - Create visualizations of your own data
    
    3. **Apply to Real Scenarios:**
       - Analyze your company's revenue data
       - Evaluate investment opportunities
       - Assess risk in your projects
    
    4. **Prepare for Module 2:**
       - Review probability concepts
       - Understand random variables
       - Get comfortable with distributions
    """)
    
    # Module Progress
    st.markdown("---")
    st.subheader("📈 Your Learning Progress")
    
    progress_col1, progress_col2 = st.columns([3, 1])
    
    with progress_col1:
        st.progress(100, text="Module 1: Complete ✅")
    
    with progress_col2:
        st.metric("Modules Completed", "1 / 12")
    
    st.info("""
    **Ready for the next module?**
    
    Module 2: Probability Theory will build on these foundations to help you:
    - Understand uncertainty in financial markets
    - Work with probability distributions
    - Apply Bayes' theorem to investment decisions
    - Model random events in finance
    """)
    
    # Download Summary
    st.markdown("---")
    
    if st.button("📥 Download Module Summary (Coming Soon)", disabled=True):
        st.info("Summary download feature will be available soon!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #a8c5dd; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 1 of 12: Foundations of Statistics</p>
    <p style='font-size: 0.9em; opacity: 0.7;'>Master the foundations to build advanced analytical skills</p>
</div>
""", unsafe_allow_html=True)