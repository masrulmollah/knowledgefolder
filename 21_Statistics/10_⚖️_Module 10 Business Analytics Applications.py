import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e65100 0%, #f57c00 50%, #ff9800 100%);
    }
    h1 {
        color: #fff3e0;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #ffe0b2;
        border-left: 6px solid #fff3e0;
        padding-left: 15px;
    }
    h3 {
        color: #ffecb3;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>📊 Module 10: Business Analytics Applications</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffecb3;'>Practical Analytics for Business Decisions</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 10 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("10.1 Customer Analytics")
    
    st.subheader("Customer Segmentation")
    
    st.warning("""
    **Customer Segmentation:**
    
    Dividing customers into groups based on common characteristics to target them more effectively.
    
    **Why It Matters:**
    - Personalized marketing
    - Better resource allocation
    - Improved customer satisfaction
    - Higher conversion rates
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Segmentation Methods:**
        
        **1. Demographic Segmentation**
        - Age, gender, income
        - Location, education
        - Easy to obtain
        - Limited predictive power
        
        **2. Behavioral Segmentation**
        - Purchase history
        - Product usage
        - Engagement level
        - More predictive
        
        **3. RFM Analysis**
        - Recency: Last purchase
        - Frequency: How often
        - Monetary: How much spent
        - Simple but powerful
        """)
    
    with col2:
        st.success("""
        **K-Means Clustering:**
        
        **Algorithm:**
        1. Choose k clusters
        2. Initialize k centroids randomly
        3. Assign each point to nearest centroid
        4. Update centroids (mean of assigned points)
        5. Repeat 3-4 until convergence
        
        **Choosing k:**
        - Elbow method
        - Silhouette score
        - Business judgment
        
        **Applications:**
        - Customer segmentation
        - Market basket analysis
        - Portfolio grouping
        """)
    
    st.markdown("---")
    
    st.subheader("Customer Lifetime Value (CLV)")
    
    st.latex(r"CLV = \sum_{t=1}^{T} \frac{R_t - C_t}{(1+d)^t}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Components:**
        - R_t: Revenue at time t
        - C_t: Cost at time t
        - d: Discount rate
        - T: Customer lifetime
        
        **Simplified Formula:**
        """)
        
        st.latex(r"CLV = \frac{\text{Avg Purchase Value} \times \text{Purchase Frequency} \times \text{Customer Lifespan}}{\text{Churn Rate}}")
        
        st.markdown("""
        **Key Metrics:**
        - Average order value
        - Purchase frequency
        - Customer retention rate
        - Churn rate
        """)
    
    with col2:
        st.success("""
        **Why Calculate CLV:**
        
        **1. Customer Acquisition**
        - Maximum affordable CAC
        - CLV should be 3x CAC
        - ROI on marketing
        
        **2. Retention Strategy**
        - Focus on high CLV customers
        - Proactive retention
        - Personalized offers
        
        **3. Business Valuation**
        - Total customer base value
        - Growth projections
        - Investor presentations
        
        **Example:**
        - Avg order: $100
        - Frequency: 4x/year
        - Lifespan: 5 years
        - CLV = $100 × 4 × 5 = $2,000
        """)
    
    st.markdown("---")
    
    st.subheader("Churn Prediction")
    
    st.warning("""
    **Customer Churn:**
    
    Predicting which customers are likely to leave/stop using your product.
    
    **Why It Matters:**
    - Acquiring new customers is 5-25x more expensive than retaining
    - Proactive retention saves costs
    - Improves customer satisfaction
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Churn Indicators:**
        
        **Usage Patterns:**
        - Decreasing engagement
        - Reduced login frequency
        - Fewer transactions
        
        **Customer Service:**
        - Increased support tickets
        - Complaints
        - Negative feedback
        
        **Financial:**
        - Late payments
        - Downgraded plans
        - Reduced spending
        """)
    
    with col2:
        st.success("""
        **Predictive Approach:**
        
        **1. Data Collection**
        - Usage metrics
        - Demographics
        - Transaction history
        - Support interactions
        
        **2. Feature Engineering**
        - Days since last purchase
        - Trend in engagement
        - Payment delays
        
        **3. Model Building**
        - Classification (will churn yes/no)
        - Random Forest, Logistic Regression
        - Predict churn probability
        
        **4. Action**
        - Target high-risk customers
        - Retention offers
        - Personalized outreach
        """)
    
    st.markdown("---")
    
    # Forecasting
    st.header("10.2 Business Forecasting")
    
    st.subheader("Sales Forecasting Methods")
    
    methods_comparison = pd.DataFrame({
        'Method': [
            'Moving Average',
            'Exponential Smoothing',
            'Linear Regression',
            'ARIMA',
            'Machine Learning'
        ],
        'Best For': [
            'Simple, stable trends',
            'Recent data more important',
            'Clear linear trend',
            'Complex time series',
            'Multiple predictors'
        ],
        'Complexity': [
            'Low',
            'Low',
            'Medium',
            'High',
            'High'
        ],
        'Data Needs': [
            'Time series only',
            'Time series only',
            'Additional features helpful',
            'Long time series',
            'Many features'
        ]
    })
    
    st.table(methods_comparison)
    
    st.markdown("---")
    
    st.subheader("Demand Forecasting")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Components of Demand:**
        
        **1. Base Demand**
        - Regular, predictable sales
        - Core customer purchases
        
        **2. Trend**
        - Long-term growth/decline
        - Market expansion
        
        **3. Seasonality**
        - Predictable patterns
        - Holiday effects
        - Monthly/quarterly cycles
        
        **4. Events/Promotions**
        - Marketing campaigns
        - Price changes
        - Competitor actions
        """)
    
    with col2:
        st.success("""
        **Forecasting Process:**
        
        **Step 1: Collect Data**
        - Historical sales
        - Marketing spend
        - Economic indicators
        - Competitor data
        
        **Step 2: Clean & Prepare**
        - Handle missing values
        - Remove outliers
        - Create features
        
        **Step 3: Build Model**
        - Choose method
        - Train on historical data
        - Validate accuracy
        
        **Step 4: Generate Forecast**
        - Point forecast
        - Confidence intervals
        - Scenarios (best/worst/likely)
        
        **Step 5: Monitor & Update**
        - Track actual vs forecast
        - Adjust model
        - Continuous improvement
        """)
    
    st.markdown("---")
    
    # A/B Testing
    st.header("10.3 A/B Testing")
    
    st.subheader("Experimental Design")
    
    st.warning("""
    **A/B Testing:**
    
    Comparing two versions (A and B) to determine which performs better.
    
    **Common Applications:**
    - Website design
    - Email campaigns
    - Product features
    - Pricing strategies
    - Marketing messages
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **A/B Test Process:**
        
        **1. Define Objective**
        - What are we testing?
        - What's success metric?
        - Conversion rate, revenue, engagement
        
        **2. Create Hypothesis**
        - "Button color change will increase clicks by 10%"
        - Testable and specific
        
        **3. Design Test**
        - Control (A): Current version
        - Treatment (B): New version
        - Random assignment
        
        **4. Determine Sample Size**
        - Power analysis
        - Significance level (α = 0.05)
        - Expected effect size
        """)
    
    with col2:
        st.success("""
        **5. Run Test**
        - Equal traffic split
        - Sufficient duration
        - Avoid external events
        
        **6. Analyze Results**
        - Statistical significance
        - Practical significance
        - Confidence intervals
        
        **7. Make Decision**
        - Implement winner
        - Run longer if inconclusive
        - Consider secondary metrics
        
        **Common Pitfalls:**
        - Stopping too early
        - Multiple testing (p-hacking)
        - Ignoring seasonality
        - Not accounting for novelty effect
        """)
    
    st.markdown("---")
    
    st.subheader("Statistical Testing for A/B")
    
    st.markdown("**For Conversion Rates (Binary Outcome):**")
    
    st.latex(r"z = \frac{p_B - p_A}{\sqrt{\bar{p}(1-\bar{p})(\frac{1}{n_A} + \frac{1}{n_B})}}")
    
    st.info("""
    **Where:**
    - p_A, p_B: Conversion rates for A and B
    - p̄: Pooled conversion rate
    - n_A, n_B: Sample sizes
    
    **Decision Rule:**
    - Calculate z-statistic
    - Compare to critical value (1.96 for 95% confidence)
    - If |z| > 1.96, difference is significant
    """)
    
    st.markdown("---")
    
    # Marketing Analytics
    st.header("10.4 Marketing Analytics")
    
    st.subheader("Marketing Mix Modeling (MMM)")
    
    st.success("""
    **Marketing Mix Model:**
    
    Regression-based approach to measure impact of marketing activities on sales.
    """)
    
    st.latex(r"Sales = \beta_0 + \beta_1 TV + \beta_2 Digital + \beta_3 Print + \beta_4 Price + \epsilon")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Components:**
        
        **Dependent Variable:**
        - Sales, revenue, or market share
        
        **Independent Variables:**
        - Marketing spend by channel
        - Price
        - Promotions
        - Seasonality
        - Competitor activity
        
        **Outputs:**
        - ROI by channel
        - Optimal budget allocation
        - Incrementality (lift from marketing)
        """)
    
    with col2:
        st.warning("""
        **Challenges:**
        
        **1. Attribution**
        - Multiple touchpoints
        - Time lag effects
        - Synergies between channels
        
        **2. Data Quality**
        - Consistent measurement
        - External factors
        - Historical data needed
        
        **3. Model Assumptions**
        - Linearity
        - Constant effects
        - No omitted variables
        
        **Solutions:**
        - Adstock transformations
        - Diminishing returns curves
        - Interaction terms
        """)
    
    st.markdown("---")
    
    st.subheader("Customer Acquisition Cost (CAC)")
    
    st.latex(r"CAC = \frac{\text{Total Marketing Spend}}{\text{Number of New Customers}}")
    
    st.info("""
    **Key Metrics:**
    
    **CAC by Channel:**
    - Social media: $50
    - Search ads: $75
    - Email: $20
    - Referral: $30
    
    **CAC Payback Period:**
    - Time to recover acquisition cost
    - CAC / (Monthly Revenue per Customer)
    - Target: < 12 months
    
    **LTV/CAC Ratio:**
    - Lifetime Value / Customer Acquisition Cost
    - Target: > 3.0
    - 3.0 means customer generates 3x their acquisition cost
    """)
    
    st.markdown("---")
    
    # Operational Analytics
    st.header("10.5 Operational Analytics")
    
    st.subheader("Inventory Optimization")
    
    st.warning("""
    **Economic Order Quantity (EOQ):**
    
    Optimal order quantity that minimizes total inventory costs.
    """)
    
    st.latex(r"EOQ = \sqrt{\frac{2DS}{H}}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Parameters:**
        - D: Annual demand
        - S: Order cost per order
        - H: Holding cost per unit per year
        
        **Example:**
        - D = 10,000 units/year
        - S = $100/order
        - H = $5/unit/year
        
        **Calculation:**
        - EOQ = √(2 × 10,000 × 100 / 5)
        - EOQ = √400,000
        - EOQ = 632 units
        
        **Interpretation:**
        Order 632 units at a time to minimize costs
        """)
    
    with col2:
        st.success("""
        **Total Cost Components:**
        
        **1. Ordering Cost**
        - Cost to place orders
        - (D/Q) × S
        - More frequent orders → Higher cost
        
        **2. Holding Cost**
        - Cost to store inventory
        - (Q/2) × H
        - More inventory → Higher cost
        
        **3. Purchase Cost**
        - D × Unit price
        - Usually constant
        
        **Optimal Point:**
        - Where ordering cost = holding cost
        - EOQ minimizes total
        """)
    
    st.markdown("---")
    
    st.subheader("Process Optimization")
    
    st.info("""
    **Six Sigma Approach:**
    
    Data-driven methodology to reduce defects and variation.
    
    **DMAIC Framework:**
    
    **Define:**
    - Problem statement
    - Goals and objectives
    - Customer requirements
    
    **Measure:**
    - Current performance
    - Data collection
    - Baseline metrics
    
    **Analyze:**
    - Root cause analysis
    - Statistical analysis
    - Identify improvement opportunities
    
    **Improve:**
    - Develop solutions
    - Test changes
    - Implement improvements
    
    **Control:**
    - Monitor performance
    - Sustain gains
    - Documentation
    """)
    
    st.markdown("---")
    
    # Pricing Analytics
    st.header("10.6 Pricing Analytics")
    
    st.subheader("Price Elasticity")
    
    st.latex(r"\text{Price Elasticity} = \frac{\% \Delta \text{Quantity}}{\% \Delta \text{Price}}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Interpretation:**
        
        **Elastic (|E| > 1):**
        - Demand sensitive to price
        - Price increase → Revenue decrease
        - Examples: Luxury goods, substitutes
        
        **Inelastic (|E| < 1):**
        - Demand insensitive to price
        - Price increase → Revenue increase
        - Examples: Necessities, addictive products
        
        **Unit Elastic (|E| = 1):**
        - Revenue unchanged with price change
        - Rare in practice
        """)
    
    with col2:
        st.success("""
        **Example:**
        
        **Initial:**
        - Price: $100
        - Quantity: 1,000 units
        - Revenue: $100,000
        
        **After 10% price increase:**
        - Price: $110
        - Quantity: 900 units
        - Revenue: $99,000
        
        **Elasticity:**
        - % ΔQ = -10%
        - % ΔP = +10%
        - E = -10% / 10% = -1.0
        
        **Result: Unit elastic**
        """)
    
    st.markdown("---")
    
    st.subheader("Dynamic Pricing")
    
    st.warning("""
    **Dynamic Pricing:**
    
    Adjusting prices in real-time based on demand, competition, and other factors.
    
    **Applications:**
    - Airlines: Seat pricing
    - Rideshare: Surge pricing
    - Hotels: Room rates
    - E-commerce: Personalized pricing
    - Retail: Markdown optimization
    
    **Factors Considered:**
    - Time to event
    - Inventory levels
    - Competitor prices
    - Customer segment
    - Market demand
    - Weather, events
    """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Business Analytics Examples")
    
    # Example 1: Customer Segmentation
    st.subheader("Example 1: Customer Segmentation with K-Means")
    
    st.markdown("""
    **Scenario:** Segment customers based on purchase behavior.
    
    **Features:** Annual spending, Purchase frequency
    """)
    
    # Generate sample data
    np.random.seed(42)
    
    # Three customer segments
    # Segment 1: Low spenders, low frequency
    seg1_spend = np.random.normal(1000, 200, 50)
    seg1_freq = np.random.normal(2, 0.5, 50)
    
    # Segment 2: Medium spenders, medium frequency
    seg2_spend = np.random.normal(3000, 400, 50)
    seg2_freq = np.random.normal(6, 1, 50)
    
    # Segment 3: High spenders, high frequency
    seg3_spend = np.random.normal(6000, 800, 50)
    seg3_freq = np.random.normal(12, 2, 50)
    
    spending = np.concatenate([seg1_spend, seg2_spend, seg3_spend])
    frequency = np.concatenate([seg1_freq, seg2_freq, seg3_freq])
    
    df_customers = pd.DataFrame({
        'Annual_Spending': spending,
        'Purchase_Frequency': frequency
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Sample Data:**")
        st.dataframe(df_customers.head(10))
        
        # Standardize features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(df_customers)
        
        # K-means clustering
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(X_scaled)
        
        df_customers['Cluster'] = clusters
        
        # Calculate cluster statistics
        cluster_stats = df_customers.groupby('Cluster').agg({
            'Annual_Spending': ['mean', 'count'],
            'Purchase_Frequency': 'mean'
        }).round(2)
        
        cluster_stats.columns = ['Avg Spending', 'Count', 'Avg Frequency']
        
        st.markdown("**Cluster Summary:**")
        st.dataframe(cluster_stats)
        
        # Assign labels
        cluster_labels = {
            cluster_stats['Avg Spending'].idxmin(): 'Low Value',
            cluster_stats['Avg Spending'].idxmax(): 'High Value'
        }
        # Find medium
        for idx in cluster_stats.index:
            if idx not in cluster_labels:
                cluster_labels[idx] = 'Medium Value'
        
        df_customers['Segment'] = df_customers['Cluster'].map(cluster_labels)
        
        st.success("""
        **Identified Segments:**
        - Low Value: Low spending, low frequency
        - Medium Value: Moderate engagement
        - High Value: VIP customers
        
        **Action:**
        - Target marketing by segment
        - Different retention strategies
        - Personalized offers
        """)
    
    with col2:
        # Scatter plot with clusters
        fig = px.scatter(
            df_customers,
            x='Annual_Spending',
            y='Purchase_Frequency',
            color='Segment',
            title='Customer Segments',
            labels={
                'Annual_Spending': 'Annual Spending ($)',
                'Purchase_Frequency': 'Purchase Frequency (times/year)'
            },
            color_discrete_map={
                'Low Value': '#ff6b6b',
                'Medium Value': '#ffd93d',
                'High Value': '#6bcf7f'
            }
        )
        
        fig.update_layout(template="plotly_dark", height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 2: A/B Test
    st.subheader("Example 2: A/B Test Analysis")
    
    st.markdown("""
    **Scenario:** Test if new website design increases conversion rate.
    
    **Control (A):** Current design
    **Treatment (B):** New design
    """)
    
    # Simulate A/B test data
    np.random.seed(42)
    
    n_A = 1000
    n_B = 1000
    
    p_A = 0.10  # 10% conversion rate for A
    p_B = 0.12  # 12% conversion rate for B (20% lift)
    
    conversions_A = np.random.binomial(1, p_A, n_A)
    conversions_B = np.random.binomial(1, p_B, n_B)
    
    conv_rate_A = conversions_A.mean()
    conv_rate_B = conversions_B.mean()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Test Results:**")
        
        results_df = pd.DataFrame({
            'Variant': ['A (Control)', 'B (Treatment)'],
            'Visitors': [n_A, n_B],
            'Conversions': [conversions_A.sum(), conversions_B.sum()],
            'Conversion Rate': [conv_rate_A, conv_rate_B]
        })
        
        st.table(results_df.style.format({
            'Conversion Rate': '{:.2%}'
        }))
        
        # Statistical test
        p_pooled = (conversions_A.sum() + conversions_B.sum()) / (n_A + n_B)
        se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n_A + 1/n_B))
        z_stat = (conv_rate_B - conv_rate_A) / se
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        lift = (conv_rate_B - conv_rate_A) / conv_rate_A * 100
        
        st.markdown("**Statistical Analysis:**")
        
        st.code(f"""
z-statistic: {z_stat:.3f}
p-value: {p_value:.4f}
Significance level: 0.05

Conversion lift: {lift:.1f}%
        """)
        
        if p_value < 0.05:
            st.success(f"""
            ✅ **Statistically Significant!**
            
            Treatment B has {lift:.1f}% higher conversion rate.
            
            **Recommendation:** Implement new design.
            
            **Expected Impact:**
            - {lift:.1f}% more conversions
            - With 10,000 visitors: {int(10000 * lift / 100)} extra conversions
            """)
        else:
            st.info("""
            ❌ **Not Statistically Significant**
            
            Cannot conclusively say B is better than A.
            
            Options:
            - Run test longer
            - Increase sample size
            - Try a different variation
            """)
    
    with col2:
        # Visualization
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=['Control (A)', 'Treatment (B)'],
            y=[conv_rate_A, conv_rate_B],
            text=[f'{conv_rate_A:.2%}', f'{conv_rate_B:.2%}'],
            textposition='auto',
            marker_color=['#ff6b6b', '#6bcf7f']
        ))
        
        fig.update_layout(
            title="Conversion Rate Comparison",
            yaxis_title="Conversion Rate",
            yaxis_tickformat='.0%',
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Confidence intervals
        ci_A = 1.96 * np.sqrt(conv_rate_A * (1 - conv_rate_A) / n_A)
        ci_B = 1.96 * np.sqrt(conv_rate_B * (1 - conv_rate_B) / n_B)
        
        fig2 = go.Figure()
        
        variants = ['Control (A)', 'Treatment (B)']
        rates = [conv_rate_A, conv_rate_B]
        errors = [ci_A, ci_B]
        
        fig2.add_trace(go.Scatter(
            x=variants,
            y=rates,
            error_y=dict(type='data', array=errors, visible=True),
            mode='markers',
            marker=dict(size=15, color=['#ff6b6b', '#6bcf7f']),
            name='95% CI'
        ))
        
        fig2.update_layout(
            title="Conversion Rate with 95% Confidence Intervals",
            yaxis_title="Conversion Rate",
            yaxis_tickformat='.0%',
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Example 3: Sales Forecasting
    st.subheader("Example 3: Sales Forecasting")
    
    st.markdown("""
    **Scenario:** Forecast next quarter's sales using historical data.
    """)
    
    # Generate sample sales data
    np.random.seed(42)
    n_months = 24
    
    # Trend + seasonality + noise
    trend = np.linspace(100, 150, n_months)
    seasonality = 20 * np.sin(np.arange(n_months) * 2 * np.pi / 12)
    noise = np.random.normal(0, 5, n_months)
    
    sales = trend + seasonality + noise
    
    months = pd.date_range(start='2022-01', periods=n_months, freq='M')
    
    df_sales = pd.DataFrame({
        'Month': months,
        'Sales': sales
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Historical Sales:**")
        st.dataframe(df_sales.tail(12))
        
        # Simple forecast using moving average
        window = 3
        forecast_horizon = 3
        
        ma = df_sales['Sales'].rolling(window=window).mean().iloc[-1]
        
        # Add trend
        recent_trend = (df_sales['Sales'].iloc[-1] - df_sales['Sales'].iloc[-6]) / 6
        
        forecasts = []
        for i in range(1, forecast_horizon + 1):
            forecast = ma + recent_trend * i
            forecasts.append(forecast)
        
        forecast_months = pd.date_range(start=months[-1] + pd.DateOffset(months=1), 
                                       periods=forecast_horizon, freq='M')
        
        st.markdown("**Forecast (Next 3 Months):**")
        
        forecast_df = pd.DataFrame({
            'Month': forecast_months,
            'Forecast': forecasts
        })
        
        st.table(forecast_df.style.format({'Forecast': '{:.1f}'}))
        
        st.info(f"""
        **Method:** Trend-adjusted moving average
        
        **Assumptions:**
        - Recent trend continues
        - Seasonal pattern holds
        - No major disruptions
        
        **Forecast Total:** ${sum(forecasts):.0f}k
        """)
    
    with col2:
        # Plot
        fig = go.Figure()
        
        # Historical
        fig.add_trace(go.Scatter(
            x=df_sales['Month'],
            y=df_sales['Sales'],
            mode='lines+markers',
            name='Historical',
            line=dict(color='#fff3e0', width=2)
        ))
        
        # Forecast
        fig.add_trace(go.Scatter(
            x=forecast_months,
            y=forecasts,
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#ff9800', width=2, dash='dash'),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Sales Forecast",
            xaxis_title="Month",
            yaxis_title="Sales ($k)",
            template="plotly_dark",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Business Analytics")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["Customer Segmentation Tool", "A/B Test Calculator", 
         "CLV Calculator", "Price Elasticity Simulator"]
    )
    
    if exercise == "Customer Segmentation Tool":
        st.subheader("👥 Customer Segmentation Tool")
        
        st.markdown("Upload or generate customer data to segment.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            data_source = st.radio("Data source:", ["Generate Sample", "Manual Input"])
            
            if data_source == "Generate Sample":
                n_customers = st.slider("Number of customers:", 100, 1000, 300)
                n_clusters = st.slider("Number of segments:", 2, 5, 3)
                
                if st.button("Generate & Segment"):
                    np.random.seed(42)
                    
                    # Generate data
                    spending = np.random.lognormal(8, 1, n_customers)
                    frequency = np.random.poisson(6, n_customers)
                    recency = np.random.uniform(1, 365, n_customers)
                    
                    df = pd.DataFrame({
                        'Spending': spending,
                        'Frequency': frequency,
                        'Recency_Days': recency
                    })
                    
                    # Standardize
                    scaler = StandardScaler()
                    X_scaled = scaler.fit_transform(df)
                    
                    # K-means
                    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
                    df['Segment'] = kmeans.fit_predict(X_scaled)
                    
                    st.session_state['segment_data'] = df
        
        with col2:
            if 'segment_data' in st.session_state:
                df = st.session_state['segment_data']
                
                # 3D scatter
                fig = px.scatter_3d(
                    df,
                    x='Spending',
                    y='Frequency',
                    z='Recency_Days',
                    color='Segment',
                    title='Customer Segments (3D View)',
                    labels={
                        'Spending': 'Annual Spending ($)',
                        'Frequency': 'Purchase Frequency',
                        'Recency_Days': 'Days Since Last Purchase'
                    }
                )
                
                fig.update_layout(template="plotly_dark", height=500)
                st.plotly_chart(fig, use_container_width=True)
                
                # Segment profiles
                st.markdown("**Segment Profiles:**")
                
                profile = df.groupby('Segment').agg({
                    'Spending': 'mean',
                    'Frequency': 'mean',
                    'Recency_Days': 'mean'
                }).round(2)
                
                profile['Count'] = df.groupby('Segment').size()
                profile['Pct'] = (profile['Count'] / len(df) * 100).round(1)
                
                st.dataframe(profile)
    
    elif exercise == "A/B Test Calculator":
        st.subheader("🧪 A/B Test Calculator")
        
        st.markdown("Calculate if your A/B test results are significant.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Variant A (Control):**")
            visitors_A = st.number_input("Visitors A:", min_value=1, value=1000)
            conversions_A = st.number_input("Conversions A:", min_value=0, value=100)
            
            st.markdown("**Variant B (Treatment):**")
            visitors_B = st.number_input("Visitors B:", min_value=1, value=1000)
            conversions_B = st.number_input("Conversions B:", min_value=0, value=120)
            
            alpha = st.slider("Significance level:", 0.01, 0.10, 0.05, 0.01)
        
        with col2:
            if st.button("Calculate Results"):
                # Conversion rates
                cr_A = conversions_A / visitors_A
                cr_B = conversions_B / visitors_B
                
                # Statistical test
                p_pooled = (conversions_A + conversions_B) / (visitors_A + visitors_B)
                se = np.sqrt(p_pooled * (1 - p_pooled) * (1/visitors_A + 1/visitors_B))
                z = (cr_B - cr_A) / se
                p_value = 2 * (1 - stats.norm.cdf(abs(z)))
                
                # Lift
                lift = (cr_B - cr_A) / cr_A * 100
                
                st.markdown("**Results:**")
                st.metric("Control Rate", f"{cr_A:.2%}")
                st.metric("Treatment Rate", f"{cr_B:.2%}")
                st.metric("Lift", f"{lift:+.1f}%")
                st.metric("p-value", f"{p_value:.4f}")
                
                if p_value < alpha:
                    st.success(f"""
                    ✅ **Statistically Significant!**
                    
                    p-value ({p_value:.4f}) < α ({alpha})
                    
                    Treatment is {lift:+.1f}% {'better' if lift > 0 else 'worse'} than control.
                    """)
                else:
                    st.info(f"""
                    ❌ **Not Significant**
                    
                    p-value ({p_value:.4f}) ≥ α ({alpha})
                    
                    Cannot conclude B is different from A.
                    Need more data or larger effect size.
                    """)
    
    elif exercise == "CLV Calculator":
        st.subheader("💰 Customer Lifetime Value Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Input Parameters:**")
            
            avg_purchase = st.number_input("Average Purchase Value ($):", value=100.0)
            frequency = st.number_input("Purchase Frequency (per year):", value=4.0)
            retention_rate = st.slider("Customer Retention Rate (%):", 0, 100, 70) / 100
            margin = st.slider("Profit Margin (%):", 0, 100, 30) / 100
            discount_rate = st.slider("Discount Rate (%):", 0, 20, 10) / 100
            
            if st.button("Calculate CLV"):
                # Annual revenue per customer
                annual_revenue = avg_purchase * frequency
                annual_profit = annual_revenue * margin
                
                # CLV calculation (infinite horizon)
                if retention_rate < 1:
                    churn_rate = 1 - retention_rate
                    clv = annual_profit / (churn_rate + discount_rate - (retention_rate * discount_rate))
                else:
                    clv = annual_profit / discount_rate
                
                # 5-year CLV
                clv_5year = 0
                for t in range(1, 6):
                    clv_5year += annual_profit * (retention_rate ** t) / ((1 + discount_rate) ** t)
                
                st.session_state['clv_results'] = {
                    'clv': clv,
                    'clv_5year': clv_5year,
                    'annual_revenue': annual_revenue,
                    'annual_profit': annual_profit
                }
        
        with col2:
            if 'clv_results' in st.session_state:
                results = st.session_state['clv_results']
                
                st.markdown("**Results:**")
                
                st.metric("Customer Lifetime Value", f"${results['clv']:.2f}")
                st.metric("5-Year CLV", f"${results['clv_5year']:.2f}")
                st.metric("Annual Revenue/Customer", f"${results['annual_revenue']:.2f}")
                st.metric("Annual Profit/Customer", f"${results['annual_profit']:.2f}")
                
                # CAC comparison
                st.markdown("**Max Customer Acquisition Cost (3:1 rule):**")
                max_cac = results['clv'] / 3
                st.metric("Max CAC", f"${max_cac:.2f}")
                
                st.success(f"""
                **Insights:**
                
                - Each customer is worth ${results['clv']:.2f} lifetime
                - Can afford up to ${max_cac:.2f} for acquisition
                - Annual profit: ${results['annual_profit']:.2f}
                """)
    
    elif exercise == "Price Elasticity Simulator":
        st.subheader("💵 Price Elasticity Simulator")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Current State:**")
            
            current_price = st.number_input("Current Price ($):", value=100.0)
            current_quantity = st.number_input("Current Quantity:", value=1000)
            
            st.markdown("**Scenario:**")
            
            new_price = st.number_input("New Price ($):", value=110.0)
            elasticity = st.slider("Price Elasticity:", -3.0, -0.1, -1.5, 0.1)
            
            # Calculate new quantity
            pct_price_change = (new_price - current_price) / current_price
            pct_qty_change = elasticity * pct_price_change
            new_quantity = current_quantity * (1 + pct_qty_change)
            
            # Revenue
            current_revenue = current_price * current_quantity
            new_revenue = new_price * new_quantity
            revenue_change = new_revenue - current_revenue
            
            st.markdown("**Results:**")
            st.metric("New Quantity", f"{new_quantity:.0f}")
            st.metric("Revenue Change", f"${revenue_change:,.2f}",
                     delta=f"{revenue_change/current_revenue*100:+.1f}%")
        
        with col2:
            # Create price-revenue curve
            prices = np.linspace(current_price * 0.5, current_price * 1.5, 50)
            quantities = []
            revenues = []
            
            for p in prices:
                pct_change = (p - current_price) / current_price
                q = current_quantity * (1 + elasticity * pct_change)
                quantities.append(q)
                revenues.append(p * q)
            
            fig = go.Figure()
            
            # Revenue curve
            fig.add_trace(go.Scatter(
                x=prices,
                y=revenues,
                mode='lines',
                name='Revenue',
                line=dict(color='#fff3e0', width=3)
            ))
            
            # Current point
            fig.add_trace(go.Scatter(
                x=[current_price],
                y=[current_revenue],
                mode='markers',
                name='Current',
                marker=dict(size=15, color='#6bcf7f')
            ))
            
            # New point
            fig.add_trace(go.Scatter(
                x=[new_price],
                y=[new_revenue],
                mode='markers',
                name='New',
                marker=dict(size=15, color='#ff9800')
            ))
            
            fig.update_layout(
                title="Price-Revenue Curve",
                xaxis_title="Price ($)",
                yaxis_title="Revenue ($)",
                template="plotly_dark",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            if revenue_change > 0:
                st.success(f"✅ Revenue increases by ${revenue_change:,.2f}")
            else:
                st.error(f"❌ Revenue decreases by ${abs(revenue_change):,.2f}")

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Business Analytics Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["CLV Calculator", "Break-Even Analysis", "EOQ Calculator", "ROI Calculator"]
    )
    
    if calc_type == "CLV Calculator":
        st.subheader("Customer Lifetime Value Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            avg_purchase = st.number_input("Average Purchase Value ($):", value=100.0)
            frequency = st.number_input("Annual Purchase Frequency:", value=4.0)
            margin = st.slider("Profit Margin (%):", 0, 100, 25) / 100
            retention = st.slider("Annual Retention Rate (%):", 0, 100, 80) / 100
            
            if st.button("Calculate"):
                annual_value = avg_purchase * frequency * margin
                churn_rate = 1 - retention
                clv = annual_value / churn_rate if churn_rate > 0 else annual_value * 20
                
                st.metric("Customer Lifetime Value", f"${clv:.2f}")
                st.metric("Annual Value", f"${annual_value:.2f}")
                st.metric("Average Lifespan", f"{1/churn_rate if churn_rate > 0 else 'High'} years")
        
        with col2:
            st.info("""
            **Formula:**
            
            CLV = (Avg Purchase × Frequency × Margin) / Churn Rate
            
            **Where:**
            - Churn Rate = 1 - Retention Rate
            
            **Use:**
            - Marketing budget allocation
            - Customer acquisition decisions
            - Segment prioritization
            """)

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 10 Quiz: Business Analytics Applications")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'Customer Lifetime Value (CLV) represents:',
            'options': [
                'Total revenue from all customers',
                'Present value of future profits from a customer',
                'Customer acquisition cost',
                'Average order value'
            ],
            'correct': 'Present value of future profits from a customer',
            'explanation': 'CLV is the total profit expected from a customer over their entire relationship with the company.'
        },
        {
            'id': 2,
            'question': 'In A/B testing, statistical significance means:',
            'options': [
                'The result is guaranteed',
                'The difference is likely not due to chance',
                'Version B is always better',
                'You should stop the test immediately'
            ],
            'correct': 'The difference is likely not due to chance',
            'explanation': 'Statistical significance (typically p < 0.05) means we can reject the null hypothesis that the difference is due to chance alone.'
        },
        {
            'id': 3,
            'question': 'K-means clustering is used for:',
            'options': [
                'Supervised classification',
                'Regression analysis',
                'Unsupervised customer segmentation',
                'Time series forecasting'
            ],
            'correct': 'Unsupervised customer segmentation',
            'explanation': 'K-means is an unsupervised learning method that groups similar customers together based on their characteristics.'
        },
        {
            'id': 4,
            'question': 'Price elasticity of -1.5 means:',
            'options': [
                'Demand is inelastic',
                'Demand is elastic',
                'Price has no effect',
                'Revenue always increases with price'
            ],
            'correct': 'Demand is elastic',
            'explanation': '|Elasticity| > 1 means elastic demand - quantity changes more than proportionally to price changes.'
        },
        {
            'id': 5,
            'question': 'The ideal LTV/CAC ratio is:',
            'options': [
                '1:1',
                '3:1',
                '1:3',
                '10:1'
            ],
            'correct': '3:1',
            'explanation': 'A healthy business should have CLV at least 3x the Customer Acquisition Cost to be profitable and sustainable.'
        },
        {
            'id': 6,
            'question': 'Churn prediction is an example of:',
            'options': [
                'Regression',
                'Clustering',
                'Classification',
                'Dimensionality reduction'
            ],
            'correct': 'Classification',
            'explanation': 'Churn prediction classifies customers into binary outcomes: will churn or won\'t churn.'
        },
        {
            'id': 7,
            'question': 'Economic Order Quantity (EOQ) minimizes:',
            'options': [
                'Only ordering costs',
                'Only holding costs',
                'Total inventory costs',
                'Purchase costs'
            ],
            'correct': 'Total inventory costs',
            'explanation': 'EOQ finds the optimal order quantity that minimizes the sum of ordering and holding costs.'
        },
        {
            'id': 8,
            'question': 'In RFM analysis, "M" stands for:',
            'options': [
                'Marketing',
                'Monetary value',
                'Monthly frequency',
                'Margin'
            ],
            'correct': 'Monetary value',
            'explanation': 'RFM = Recency, Frequency, Monetary value - measures how recently, often, and much a customer purchases.'
        },
        {
            'id': 9,
            'question': 'A/B test sample size should be determined:',
            'options': [
                'After running the test',
                'Before starting the test',
                'When you see a winner',
                'Randomly'
            ],
            'correct': 'Before starting the test',
            'explanation': 'Sample size should be calculated beforehand using power analysis to ensure the test can detect meaningful differences.'
        },
        {
            'id': 10,
            'question': 'Marketing Mix Modeling (MMM) uses:',
            'options': [
                'A/B testing',
                'Cluster analysis',
                'Regression analysis',
                'Decision trees'
            ],
            'correct': 'Regression analysis',
            'explanation': 'MMM uses regression to quantify the impact of different marketing channels on sales or other KPIs.'
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
    st.header("Module 10 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Customer Analytics**
        - Segmentation (K-means)
        - CLV calculation
        - Churn prediction
        - RFM analysis
        """)
        
        st.success("""
        **Marketing Analytics**
        - A/B testing
        - Marketing mix modeling
        - CAC and LTV/CAC ratio
        - Attribution analysis
        """)
    
    with col2:
        st.warning("""
        **Operational Analytics**
        - Inventory optimization (EOQ)
        - Process improvement
        - Six Sigma / DMAIC
        - Supply chain analytics
        """)
        
        st.info("""
        **Pricing Analytics**
        - Price elasticity
        - Dynamic pricing
        - Revenue optimization
        - Break-even analysis
        """)
    
    st.markdown("---")
    st.subheader("📐 Key Formulas")
    
    formulas_df = pd.DataFrame({
        'Metric': ['CLV', 'CAC', 'Price Elasticity', 'EOQ', 'LTV/CAC'],
        'Formula': [
            'Annual Profit / Churn Rate',
            'Marketing Spend / New Customers',
            '%ΔQuantity / %ΔPrice',
            '√(2DS/H)',
            'CLV / CAC'
        ],
        'Target': [
            'Maximize',
            'Minimize',
            'Understand demand',
            'Optimize inventory',
            '> 3.0'
        ]
    })
    st.table(formulas_df)
    
    st.markdown("---")
    st.subheader("💼 Practical Applications")
    
    tab1, tab2, tab3 = st.tabs(["E-commerce", "SaaS", "Retail"])
    
    with tab1:
        st.markdown("""
        **E-commerce Analytics:**
        
        1. **Customer Segmentation**
           - High-value vs low-value customers
           - Behavioral cohorts
           - Personalized recommendations
        
        2. **A/B Testing**
           - Product page design
           - Checkout flow
           - Pricing strategies
        
        3. **Forecasting**
           - Demand prediction
           - Inventory planning
           - Seasonal trends
        
        4. **Marketing**
           - Channel attribution
           - Campaign ROI
           - Customer acquisition efficiency
        """)
    
    with tab2:
        st.markdown("""
        **SaaS Analytics:**
        
        1. **Subscription Metrics**
           - MRR/ARR tracking
           - Churn analysis
           - Cohort retention
        
        2. **Customer Success**
           - Usage analytics
           - Feature adoption
           - Health scores
        
        3. **Growth**
           - Viral coefficient
           - CAC payback period
           - Net revenue retention
        
        4. **Product Analytics**
           - Feature usage
           - User journey mapping
           - A/B testing features
        """)
    
    with tab3:
        st.markdown("""
        **Retail Analytics:**
        
        1. **Inventory Management**
           - EOQ optimization
           - Stock-out prevention
           - Markdown optimization
        
        2. **Store Performance**
           - Sales per square foot
           - Foot traffic analysis
           - Conversion rates
        
        3. **Pricing**
           - Competitive pricing
           - Dynamic pricing
           - Promotional effectiveness
        
        4. **Customer**
           - Loyalty programs
           - Basket analysis
           - Customer traffic patterns
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 11?**
    
    Module 11: Tools and Software covers:
    - Excel for analytics
    - Python and R
    - SQL for data
    - BI tools (Tableau, Power BI)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #ffecb3; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 10 of 12: Business Analytics Applications</p>
</div>
""", unsafe_allow_html=True)