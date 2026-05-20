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
        background: linear-gradient(135deg, #1a237e 0%, #283593 50%, #3949ab 100%);
    }
    h1 {
        color: #c5cae9;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #9fa8da;
        border-left: 6px solid #c5cae9;
        padding-left: 15px;
    }
    h3 {
        color: #e8eaf6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>🛠️ Module 11: Tools and Software</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #e8eaf6;'>Essential Analytics Tools for Finance Professionals</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 11 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("11.1 Excel for Analytics")
    
    st.subheader("Why Excel?")
    
    st.warning("""
    **Excel's Continued Dominance:**
    
    Despite newer tools, Excel remains the most widely used analytics tool in finance because:
    - Universal availability
    - Familiar interface
    - Flexible and quick
    - Integrates with other systems
    - No coding required (but supports VBA)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Essential Excel Skills:**
        
        **1. Formulas & Functions**
        - VLOOKUP / XLOOKUP
        - INDEX-MATCH
        - SUMIFS, COUNTIFS, AVERAGEIFS
        - IF, IFS, nested logic
        - IFERROR, IFNA
        
        **2. Data Analysis**
        - PivotTables
        - PivotCharts
        - Slicers and filters
        - Power Query (Get & Transform)
        
        **3. Financial Functions**
        - NPV, IRR, XIRR
        - PMT, PV, FV
        - RATE, NPER
        """)
    
    with col2:
        st.success("""
        **Advanced Features:**
        
        **4. Statistical Functions**
        - AVERAGE, STDEV, VAR
        - CORREL, COVARIANCE
        - FORECAST, TREND
        - LINEST (regression)
        
        **5. Data Visualization**
        - Charts (line, bar, scatter)
        - Conditional formatting
        - Sparklines
        - Custom dashboards
        
        **6. Automation**
        - Macros (VBA)
        - Power Pivot
        - Dynamic arrays (FILTER, SORT, UNIQUE)
        """)
    
    st.markdown("---")
    
    st.subheader("Excel Best Practices")
    
    best_practices = pd.DataFrame({
        'Category': ['Structure', 'Formulas', 'Data', 'Formatting', 'Documentation'],
        'Do': [
            'One table per sheet, headers in row 1',
            'Use named ranges, avoid hardcoding values',
            'Keep raw data separate from analysis',
            'Use consistent number formats',
            'Add comments, document assumptions'
        ],
        'Don\'t': [
            'Merge cells, use multiple tables on one sheet',
            'Reference cells by address only, use complex nested formulas',
            'Mix data entry and calculations',
            'Use color as the only indicator',
            'Leave formulas unexplained'
        ]
    })
    
    st.table(best_practices)
    
    st.markdown("---")
    
    # Python & R
    st.header("11.2 Python for Finance")
    
    st.subheader("Why Python?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Advantages of Python:**
        
        **1. Versatility**
        - Data analysis
        - Machine learning
        - Web scraping
        - API integration
        - Automation
        
        **2. Rich Ecosystem**
        - pandas: Data manipulation
        - numpy: Numerical computing
        - matplotlib/seaborn: Visualization
        - scikit-learn: Machine learning
        - statsmodels: Statistics
        
        **3. Community & Resources**
        - Large user base
        - Extensive documentation
        - Free and open source
        - Active development
        """)
    
    with col2:
        st.success("""
        **Key Libraries for Finance:**
        
        **Data & Analysis:**
        - pandas: DataFrames, time series
        - numpy: Arrays, math operations
        - scipy: Statistical functions
        
        **Visualization:**
        - matplotlib: Static plots
        - seaborn: Statistical graphics
        - plotly: Interactive charts
        
        **Finance-Specific:**
        - yfinance: Market data
        - pandas_datareader: Financial data
        - QuantLib: Derivatives pricing
        - zipline: Backtesting
        
        **Machine Learning:**
        - scikit-learn: ML algorithms
        - tensorflow/pytorch: Deep learning
        """)
    
    st.markdown("---")
    
    st.subheader("Python Code Examples")
    
    st.markdown("**Example 1: Load and Analyze Data**")
    
    st.code("""
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('stock_prices.csv')

# Basic analysis
print(df.describe())
print(df.head())

# Calculate returns
df['returns'] = df['close'].pct_change()

# Statistics
mean_return = df['returns'].mean()
volatility = df['returns'].std()

print(f"Mean return: {mean_return:.2%}")
print(f"Volatility: {volatility:.2%}")
    """, language='python')
    
    st.markdown("---")
    
    st.markdown("**Example 2: Portfolio Optimization**")
    
    st.code("""
import numpy as np
from scipy.optimize import minimize

# Expected returns and covariance
returns = np.array([0.12, 0.10, 0.08])
cov_matrix = np.array([
    [0.04, 0.01, 0.02],
    [0.01, 0.03, 0.01],
    [0.02, 0.01, 0.02]
])

# Portfolio variance function
def portfolio_variance(weights):
    return weights.T @ cov_matrix @ weights

# Constraints: weights sum to 1
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = [(0, 1)] * 3

# Minimize
result = minimize(
    portfolio_variance,
    x0=[1/3, 1/3, 1/3],
    constraints=constraints,
    bounds=bounds
)

print("Optimal weights:", result.x)
    """, language='python')
    
    st.markdown("---")
    
    # R Programming
    st.subheader("R for Statistics")
    
    st.warning("""
    **R Programming Language:**
    
    Designed specifically for statistical computing and graphics.
    
    **When to Use R:**
    - Academic research
    - Advanced statistics
    - Publication-quality graphics
    - Time series analysis
    - Econometrics
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Key R Packages:**
        
        **Data Manipulation:**
        - dplyr: Data transformation
        - tidyr: Data tidying
        - data.table: Fast operations
        
        **Visualization:**
        - ggplot2: Grammar of graphics
        - plotly: Interactive plots
        
        **Statistics:**
        - stats: Base statistics
        - forecast: Time series
        - quantmod: Financial data
        """)
    
    with col2:
        st.success("""
        **R Code Example:**
        
        ```r
        # Load libraries
        library(dplyr)
        library(ggplot2)
        
        # Load data
        df <- read.csv('data.csv')
        
        # Data manipulation
        summary_df <- df %>%
          group_by(sector) %>%
          summarise(
            mean_return = mean(return),
            sd_return = sd(return)
          )
        
        # Visualization
        ggplot(summary_df, 
               aes(x=sector, y=mean_return)) +
          geom_bar(stat='identity') +
          theme_minimal()
        ```
        """)
    
    st.markdown("---")
    
    # SQL
    st.header("11.3 SQL for Data")
    
    st.subheader("Why SQL?")
    
    st.info("""
    **Structured Query Language (SQL):**
    
    The standard language for working with relational databases.
    
    **Essential for:**
    - Querying large datasets
    - Data warehousing
    - Business intelligence
    - Data engineering
    - Financial reporting systems
    
    **SQL is a must-have skill for data-driven roles.**
    """)
    
    st.markdown("---")
    
    st.subheader("Core SQL Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Basic Queries:**")
        
        st.code("""
-- SELECT: Retrieve data
SELECT 
    customer_id,
    SUM(amount) as total_spent
FROM transactions
WHERE date >= '2024-01-01'
GROUP BY customer_id
HAVING SUM(amount) > 1000
ORDER BY total_spent DESC
LIMIT 10;
        """, language='sql')
        
        st.markdown("**Key Clauses:**")
        st.markdown("""
        - **SELECT**: Columns to retrieve
        - **FROM**: Table name
        - **WHERE**: Filter rows
        - **GROUP BY**: Aggregate data
        - **HAVING**: Filter groups
        - **ORDER BY**: Sort results
        - **LIMIT**: Number of rows
        """)
    
    with col2:
        st.markdown("**JOINs:**")
        
        st.code("""
-- INNER JOIN: Matching rows only
SELECT 
    c.customer_name,
    o.order_id,
    o.amount
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.date >= '2024-01-01';

-- LEFT JOIN: All from left table
SELECT 
    c.customer_name,
    COUNT(o.order_id) as num_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;
        """, language='sql')
    
    st.markdown("---")
    
    st.subheader("Advanced SQL")
    
    st.success("""
    **Window Functions:**
    """)
    
    st.code("""
-- Running total
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM transactions;

-- Ranking
SELECT 
    customer_id,
    amount,
    RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) as rank
FROM transactions;

-- Moving average
SELECT 
    date,
    price,
    AVG(price) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as ma_7d
FROM stock_prices;
    """, language='sql')
    
    st.markdown("---")
    
    # Business Intelligence Tools
    st.header("11.4 Business Intelligence Tools")
    
    st.subheader("Tableau")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Tableau:**
        
        Leading data visualization and BI platform.
        
        **Strengths:**
        - Intuitive drag-and-drop
        - Beautiful visualizations
        - Interactive dashboards
        - Fast performance
        - Large user community
        
        **Use Cases:**
        - Executive dashboards
        - Sales analytics
        - Financial reporting
        - Marketing analysis
        - Ad-hoc exploration
        """)
    
    with col2:
        st.success("""
        **Key Features:**
        
        **Visualization Types:**
        - Line, bar, scatter plots
        - Heatmaps, treemaps
        - Geographic maps
        - Custom calculations
        
        **Interactivity:**
        - Filters and parameters
        - Actions (filter, highlight, URL)
        - Drill-down capabilities
        
        **Sharing:**
        - Tableau Server
        - Tableau Online
        - Embedded dashboards
        
        **Learning:** Tableau Public (free)
        """)
    
    st.markdown("---")
    
    st.subheader("Power BI")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Microsoft Power BI:**
        
        Microsoft's BI and analytics platform.
        
        **Strengths:**
        - Deep Excel integration
        - Microsoft ecosystem
        - DAX language (powerful)
        - Cost-effective
        - Growing adoption
        
        **Components:**
        - Power Query: Data prep
        - Power Pivot: Data modeling
        - Power BI Desktop: Development
        - Power BI Service: Sharing
        """)
    
    with col2:
        st.info("""
        **When to Choose Power BI:**
        
        **Best For:**
        - Microsoft-heavy organizations
        - Excel power users
        - Cost-conscious teams
        - Enterprise reporting
        
        **DAX Example:**
        ```
        Total Sales = SUM(Sales[Amount])
        
        Sales YTD = 
        CALCULATE(
            [Total Sales],
            DATESYTD(Calendar[Date])
        )
        
        Sales vs LY = 
        [Total Sales] - 
        CALCULATE(
            [Total Sales],
            SAMEPERIODLASTYEAR(Calendar[Date])
        )
        ```
        """)
    
    st.markdown("---")
    
    st.subheader("Tool Comparison")
    
    comparison_df = pd.DataFrame({
        'Tool': ['Excel', 'Python', 'R', 'SQL', 'Tableau', 'Power BI'],
        'Best For': [
            'Quick analysis, financial modeling',
            'Automation, ML, complex analysis',
            'Statistical research, econometrics',
            'Data extraction, database queries',
            'Interactive dashboards, exploration',
            'Enterprise BI, Microsoft integration'
        ],
        'Learning Curve': [
            'Easy',
            'Medium',
            'Medium',
            'Medium',
            'Easy-Medium',
            'Easy-Medium'
        ],
        'Cost': [
            'License required',
            'Free',
            'Free',
            'Depends on DB',
            '$70/month',
            '$10/month'
        ],
        'Use in Finance': [
            'Universal',
            'Growing rapidly',
            'Academic/Quant',
            'Data teams',
            'Reporting/Dashboards',
            'Enterprise BI'
        ]
    })
    
    st.table(comparison_df)
    
    st.markdown("---")
    
    # Modern Tools
    st.header("11.5 Modern Analytics Stack")
    
    st.subheader("Cloud Platforms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Cloud Data Warehouses:**
        
        **Snowflake:**
        - Cloud-native data warehouse
        - Separation of storage and compute
        - Supports structured and semi-structured data
        - SQL-based interface
        
        **Google BigQuery:**
        - Serverless data warehouse
        - Petabyte scale
        - Machine learning integration
        - Pay per query
        
        **Amazon Redshift:**
        - AWS data warehouse
        - Columnar storage
        - Integration with AWS services
        """)
    
    with col2:
        st.success("""
        **Data Pipeline Tools:**
        
        **ETL/ELT:**
        - Fivetran: Automated data pipelines
        - Airbyte: Open-source connectors
        - dbt: Data transformation
        
        **Orchestration:**
        - Apache Airflow: Workflow management
        - Prefect: Modern data workflows
        
        **Notebooks:**
        - Jupyter: Interactive Python
        - Google Colab: Cloud notebooks
        - Databricks: Unified analytics
        """)
    
    st.markdown("---")
    
    st.subheader("Recommended Learning Path")
    
    learning_path = pd.DataFrame({
        'Stage': ['Beginner', 'Intermediate', 'Advanced', 'Expert'],
        'Excel': [
            'Formulas, PivotTables',
            'VLOOKUP, charts, basic VBA',
            'Power Query, Power Pivot',
            'Advanced VBA, add-ins'
        ],
        'Programming': [
            'Python basics, pandas',
            'numpy, matplotlib, SQL basics',
            'scikit-learn, advanced SQL',
            'ML frameworks, optimization'
        ],
        'BI Tools': [
            'Tableau/Power BI basics',
            'Dashboards, filters, calculations',
            'Advanced calculations, parameters',
            'Admin, performance tuning'
        ]
    })
    
    st.table(learning_path)
    
    st.info("""
    **Recommended Focus for Finance Professionals:**
    
    1. **Must Have:** Excel (advanced), SQL (intermediate)
    2. **Highly Valuable:** Python or R, Tableau or Power BI
    3. **Nice to Have:** Cloud platforms, advanced ML
    
    **Time Investment:**
    - Excel: 2-3 months to proficiency
    - Python: 3-6 months to productivity
    - SQL: 1-2 months for basics
    - Tableau/Power BI: 1-2 months
    """)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Tool Examples & Use Cases")
    
    # Example 1: Excel Analysis
    st.subheader("Example 1: Financial Analysis in Excel")
    
    st.markdown("""
    **Scenario:** Quarterly revenue analysis with YoY comparison.
    
    **Excel Functions Used:**
    - SUMIFS for conditional sums
    - Percentage growth formulas
    - Conditional formatting
    - PivotTable for summary
    """)
    
    # Create sample data
    np.random.seed(42)
    
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    years = [2023, 2024]
    regions = ['North', 'South', 'East', 'West']
    
    data = []
    for year in years:
        for quarter in quarters:
            for region in regions:
                base = 100000 if year == 2023 else 110000
                revenue = base + np.random.randint(-10000, 20000)
                data.append({
                    'Year': year,
                    'Quarter': quarter,
                    'Region': region,
                    'Revenue': revenue
                })
    
    df_revenue = pd.DataFrame(data)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Raw Data Sample:**")
        st.dataframe(df_revenue.head(10))
        
        # Pivot analysis
        pivot = df_revenue.pivot_table(
            values='Revenue',
            index='Region',
            columns=['Year', 'Quarter'],
            aggfunc='sum'
        )
        
        st.markdown("**PivotTable Summary:**")
        st.dataframe(pivot.style.format("${:,.0f}"))
        
        # YoY Growth
        yoy = df_revenue.groupby(['Quarter', 'Year'])['Revenue'].sum().unstack()
        yoy['Growth'] = ((yoy[2024] - yoy[2023]) / yoy[2023] * 100).round(1)
        
        st.markdown("**YoY Growth by Quarter:**")
        st.dataframe(yoy.style.format({
            2023: '${:,.0f}',
            2024: '${:,.0f}',
            'Growth': '{:+.1f}%'
        }))
    
    with col2:
        # Visualization
        fig = px.bar(
            df_revenue.groupby(['Year', 'Quarter'])['Revenue'].sum().reset_index(),
            x='Quarter',
            y='Revenue',
            color='Year',
            barmode='group',
            title='Quarterly Revenue Comparison',
            labels={'Revenue': 'Revenue ($)'},
            color_discrete_map={2023: '#9fa8da', 2024: '#5c6bc0'}
        )
        
        fig.update_layout(template="plotly_dark", height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Regional breakdown
        fig2 = px.pie(
            df_revenue[df_revenue['Year'] == 2024],
            values='Revenue',
            names='Region',
            title='2024 Revenue by Region'
        )
        
        fig2.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Example 2: Python Analysis
    st.subheader("Example 2: Python for Portfolio Analysis")
    
    st.markdown("""
    **Scenario:** Calculate portfolio statistics and visualize risk-return.
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Python Code:**")
        
        st.code("""
import pandas as pd
import numpy as np

# Portfolio data
assets = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Returns (annualized)
returns = np.array([0.15, 0.12, 0.18, 0.14])

# Correlation matrix
corr = np.array([
    [1.00, 0.60, 0.55, 0.50],
    [0.60, 1.00, 0.58, 0.52],
    [0.55, 0.58, 1.00, 0.48],
    [0.50, 0.52, 0.48, 1.00]
])

# Volatilities
vols = np.array([0.25, 0.20, 0.28, 0.30])

# Covariance matrix
cov = np.outer(vols, vols) * corr

# Portfolio stats
port_return = np.dot(weights, returns)
port_vol = np.sqrt(np.dot(weights, 
                   np.dot(cov, weights)))

print(f"Return: {port_return:.2%}")
print(f"Risk: {port_vol:.2%}")
print(f"Sharpe (rf=3%): {(port_return-0.03)/port_vol:.2f}")
        """, language='python')
    
    with col2:
        # Execute the analysis
        assets = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
        weights = np.array([0.25, 0.25, 0.25, 0.25])
        returns = np.array([0.15, 0.12, 0.18, 0.14])
        vols = np.array([0.25, 0.20, 0.28, 0.30])
        
        corr = np.array([
            [1.00, 0.60, 0.55, 0.50],
            [0.60, 1.00, 0.58, 0.52],
            [0.55, 0.58, 1.00, 0.48],
            [0.50, 0.52, 0.48, 1.00]
        ])
        
        cov = np.outer(vols, vols) * corr
        
        port_return = np.dot(weights, returns)
        port_vol = np.sqrt(np.dot(weights, np.dot(cov, weights)))
        sharpe = (port_return - 0.03) / port_vol
        
        st.markdown("**Output:**")
        
        st.metric("Portfolio Return", f"{port_return:.2%}")
        st.metric("Portfolio Risk", f"{port_vol:.2%}")
        st.metric("Sharpe Ratio", f"{sharpe:.2f}")
        
        # Risk-Return plot
        fig = go.Figure()
        
        # Individual assets
        fig.add_trace(go.Scatter(
            x=vols * 100,
            y=returns * 100,
            mode='markers+text',
            text=assets,
            textposition='top center',
            marker=dict(size=15, color='#9fa8da'),
            name='Individual Assets'
        ))
        
        # Portfolio
        fig.add_trace(go.Scatter(
            x=[port_vol * 100],
            y=[port_return * 100],
            mode='markers+text',
            text=['Portfolio'],
            textposition='top center',
            marker=dict(size=20, color='#5c6bc0', symbol='star'),
            name='Portfolio'
        ))
        
        fig.update_layout(
            title="Risk-Return Profile",
            xaxis_title="Risk (Volatility %)",
            yaxis_title="Return (%)",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Example 3: SQL Query
    st.subheader("Example 3: SQL for Customer Analysis")
    
    st.markdown("""
    **Scenario:** Analyze customer purchase patterns from database.
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**SQL Query:**")
        
        st.code("""
-- Customer Lifetime Value Analysis
SELECT 
    c.customer_id,
    c.customer_name,
    COUNT(DISTINCT o.order_id) as num_orders,
    SUM(o.amount) as total_spent,
    AVG(o.amount) as avg_order_value,
    MIN(o.order_date) as first_order,
    MAX(o.order_date) as last_order,
    DATEDIFF(day, MIN(o.order_date), 
             MAX(o.order_date)) as customer_tenure_days
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
WHERE o.order_date >= '2023-01-01'
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.amount) > 1000
ORDER BY total_spent DESC
LIMIT 20;
        """, language='sql')
        
        st.info("""
        **Query Breakdown:**
        
        1. **JOIN** customers and orders
        2. **FILTER** orders from 2023
        3. **AGGREGATE** by customer
        4. **CALCULATE** metrics
        5. **FILTER** high-value customers
        6. **SORT** by total spent
        7. **LIMIT** to top 20
        """)
    
    with col2:
        st.markdown("**Sample Results:**")
        
        # Simulate results
        np.random.seed(42)
        
        results = pd.DataFrame({
            'customer_id': range(1, 21),
            'customer_name': [f'Customer {i}' for i in range(1, 21)],
            'num_orders': np.random.randint(5, 30, 20),
            'total_spent': np.random.randint(1000, 10000, 20),
            'avg_order_value': np.random.randint(200, 800, 20),
            'customer_tenure_days': np.random.randint(100, 700, 20)
        })
        
        results = results.sort_values('total_spent', ascending=False)
        
        st.dataframe(results.head(10).style.format({
            'total_spent': '${:,.0f}',
            'avg_order_value': '${:,.0f}'
        }))
        
        st.success("""
        **Insights:**
        - Top 20 customers represent high value
        - Average order value varies widely
        - Tenure impacts total spending
        
        **Next Steps:**
        - Segment customers by behavior
        - Create retention strategies
        - Identify upsell opportunities
        """)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive Tool Exercises")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["Excel Function Builder", "Python Code Generator", 
         "SQL Query Builder", "BI Dashboard Demo"]
    )
    
    if exercise == "Excel Function Builder":
        st.subheader("📊 Excel Function Builder")
        
        st.markdown("Build common Excel formulas visually.")
        
        function_type = st.selectbox(
            "Select function:",
            ["VLOOKUP", "SUMIFS", "IF Statement", "INDEX-MATCH"]
        )
        
        if function_type == "VLOOKUP":
            st.markdown("**VLOOKUP Builder:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                lookup_value = st.text_input("Lookup value (cell):", value="A2")
                table_array = st.text_input("Table array:", value="D2:F100")
                col_index = st.number_input("Column index:", min_value=1, value=2)
                exact_match = st.checkbox("Exact match", value=True)
            
            with col2:
                match_type = "FALSE" if exact_match else "TRUE"
                formula = f"=VLOOKUP({lookup_value},{table_array},{col_index},{match_type})"
                
                st.markdown("**Generated Formula:**")
                st.code(formula, language='excel')
                
                st.info("""
                **Explanation:**
                - Lookup value in first column of table
                - Return value from specified column
                - FALSE = exact match
                """)
        
        elif function_type == "SUMIFS":
            st.markdown("**SUMIFS Builder:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                sum_range = st.text_input("Sum range:", value="C2:C100")
                criteria_range1 = st.text_input("Criteria range 1:", value="A2:A100")
                criteria1 = st.text_input("Criteria 1:", value='"North"')
                
                add_criteria = st.checkbox("Add second criteria")
                if add_criteria:
                    criteria_range2 = st.text_input("Criteria range 2:", value="B2:B100")
                    criteria2 = st.text_input("Criteria 2:", value='">1000"')
            
            with col2:
                if add_criteria:
                    formula = f"=SUMIFS({sum_range},{criteria_range1},{criteria1},{criteria_range2},{criteria2})"
                else:
                    formula = f"=SUMIFS({sum_range},{criteria_range1},{criteria1})"
                
                st.markdown("**Generated Formula:**")
                st.code(formula, language='excel')
                
                st.success("""
                **Use Case:**
                Sum values where multiple conditions are met.
                
                Example: Total sales in North region 
                with value > $1000
                """)
    
    elif exercise == "Python Code Generator":
        st.subheader("🐍 Python Code Generator")
        
        st.markdown("Generate Python code for common tasks.")
        
        task = st.selectbox(
            "Select task:",
            ["Load CSV", "Calculate Statistics", "Create Plot", "Filter Data"]
        )
        
        if task == "Load CSV":
            filename = st.text_input("Filename:", value="data.csv")
            
            code = f"""
import pandas as pd

# Load data
df = pd.read_csv('{filename}')

# Display info
print(df.head())
print(df.info())
print(df.describe())
            """
            
            st.code(code, language='python')
        
        elif task == "Calculate Statistics":
            column = st.text_input("Column name:", value="returns")
            
            code = f"""
import pandas as pd
import numpy as np

# Calculate statistics
mean = df['{column}'].mean()
median = df['{column}'].median()
std = df['{column}'].std()
min_val = df['{column}'].min()
max_val = df['{column}'].max()

print(f"Mean: {{mean:.4f}}")
print(f"Median: {{median:.4f}}")
print(f"Std Dev: {{std:.4f}}")
print(f"Range: [{{min_val:.4f}}, {{max_val:.4f}}]")
            """
            
            st.code(code, language='python')
        
        elif task == "Create Plot":
            plot_type = st.selectbox("Plot type:", ["Line", "Scatter", "Histogram"])
            x_col = st.text_input("X column:", value="date")
            y_col = st.text_input("Y column:", value="price")
            
            if plot_type == "Line":
                code = f"""
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df['{x_col}'], df['{y_col}'])
plt.xlabel('{x_col}')
plt.ylabel('{y_col}')
plt.title('{y_col} over {x_col}')
plt.grid(True)
plt.show()
                """
            elif plot_type == "Scatter":
                code = f"""
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(df['{x_col}'], df['{y_col}'], alpha=0.5)
plt.xlabel('{x_col}')
plt.ylabel('{y_col}')
plt.title('{y_col} vs {x_col}')
plt.grid(True)
plt.show()
                """
            else:
                code = f"""
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df['{y_col}'], bins=30, edgecolor='black')
plt.xlabel('{y_col}')
plt.ylabel('Frequency')
plt.title('Distribution of {y_col}')
plt.grid(True)
plt.show()
                """
            
            st.code(code, language='python')
    
    elif exercise == "SQL Query Builder":
        st.subheader("💾 SQL Query Builder")
        
        st.markdown("Build SQL queries visually.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            table = st.text_input("Table name:", value="sales")
            columns = st.text_input("Columns (comma-separated):", value="customer_id, amount, date")
            
            where_clause = st.text_input("WHERE condition (optional):", value="amount > 100")
            
            group_by = st.text_input("GROUP BY (optional):", value="customer_id")
            
            order_by = st.text_input("ORDER BY (optional):", value="amount DESC")
            
            limit = st.number_input("LIMIT (optional, 0=none):", min_value=0, value=10)
        
        with col2:
            # Build query
            query = f"SELECT {columns}\nFROM {table}"
            
            if where_clause:
                query += f"\nWHERE {where_clause}"
            
            if group_by:
                query += f"\nGROUP BY {group_by}"
            
            if order_by:
                query += f"\nORDER BY {order_by}"
            
            if limit > 0:
                query += f"\nLIMIT {limit}"
            
            query += ";"
            
            st.markdown("**Generated Query:**")
            st.code(query, language='sql')
            
            st.info("""
            **Query Structure:**
            1. SELECT: Columns to retrieve
            2. FROM: Source table
            3. WHERE: Filter conditions
            4. GROUP BY: Aggregation
            5. ORDER BY: Sorting
            6. LIMIT: Number of rows
            """)
    
    elif exercise == "BI Dashboard Demo":
        st.subheader("📊 BI Dashboard Demo")
        
        st.markdown("Interactive dashboard example with filters.")
        
        # Generate sample data
        np.random.seed(42)
        
        dates = pd.date_range('2024-01-01', periods=90, freq='D')
        regions = ['North', 'South', 'East', 'West']
        products = ['Product A', 'Product B', 'Product C']
        
        data = []
        for date in dates:
            for region in regions:
                for product in products:
                    sales = np.random.randint(1000, 5000)
                    data.append({
                        'Date': date,
                        'Region': region,
                        'Product': product,
                        'Sales': sales
                    })
        
        df_dashboard = pd.DataFrame(data)
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            selected_region = st.multiselect(
                "Region:",
                options=regions,
                default=regions
            )
        
        with col2:
            selected_product = st.multiselect(
                "Product:",
                options=products,
                default=products
            )
        
        with col3:
            date_range = st.date_input(
                "Date range:",
                value=(dates[0], dates[-1])
            )
        
        # Filter data
        mask = (
            (df_dashboard['Region'].isin(selected_region)) &
            (df_dashboard['Product'].isin(selected_product)) &
            (df_dashboard['Date'] >= pd.to_datetime(date_range[0])) &
            (df_dashboard['Date'] <= pd.to_datetime(date_range[1]))
        )
        
        filtered_df = df_dashboard[mask]
        
        # KPIs
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
        
        with col2:
            st.metric("Avg Daily Sales", f"${filtered_df['Sales'].mean():,.0f}")
        
        with col3:
            st.metric("Number of Days", len(filtered_df['Date'].unique()))
        
        with col4:
            st.metric("Max Daily Sales", f"${filtered_df['Sales'].max():,.0f}")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Time series
            daily_sales = filtered_df.groupby('Date')['Sales'].sum().reset_index()
            
            fig1 = px.line(
                daily_sales,
                x='Date',
                y='Sales',
                title='Daily Sales Trend'
            )
            fig1.update_layout(template="plotly_dark", height=300)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # By region
            region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
            
            fig2 = px.bar(
                region_sales,
                x='Region',
                y='Sales',
                title='Sales by Region'
            )
            fig2.update_layout(template="plotly_dark", height=300)
            st.plotly_chart(fig2, use_container_width=True)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("Tool Recommendation Calculator")
    
    st.markdown("""
    Answer a few questions to get tool recommendations for your needs.
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        role = st.selectbox(
            "Your role:",
            ["Financial Analyst", "Data Analyst", "Business Analyst", 
             "Portfolio Manager", "Risk Manager", "Executive/Manager"]
        )
        
        data_size = st.selectbox(
            "Typical data size:",
            ["Small (< 100K rows)", "Medium (100K - 1M rows)", 
             "Large (1M - 100M rows)", "Very Large (> 100M rows)"]
        )
        
        tasks = st.multiselect(
            "Primary tasks:",
            ["Reporting", "Financial Modeling", "Data Analysis", 
             "Visualization", "Machine Learning", "Database Queries",
             "Automation", "Dashboards"]
        )
        
        coding = st.select_slider(
            "Coding comfort level:",
            options=["None", "Basic", "Intermediate", "Advanced", "Expert"]
        )
    
    with col2:
        if st.button("Get Recommendations"):
            recommendations = []
            
            # Excel
            if coding in ["None", "Basic"] or "Financial Modeling" in tasks:
                recommendations.append({
                    'Tool': 'Excel',
                    'Priority': 'Essential',
                    'Reason': 'Universal tool for finance, great for modeling'
                })
            
            # Python
            if coding in ["Intermediate", "Advanced", "Expert"] or "Machine Learning" in tasks:
                recommendations.append({
                    'Tool': 'Python',
                    'Priority': 'High',
                    'Reason': 'Powerful for automation and ML'
                })
            
            # SQL
            if data_size in ["Medium (100K - 1M rows)", "Large (1M - 100M rows)", "Very Large (> 100M rows)"]:
                recommendations.append({
                    'Tool': 'SQL',
                    'Priority': 'Essential',
                    'Reason': 'Critical for working with databases'
                })
            
            # Tableau/Power BI
            if "Visualization" in tasks or "Dashboards" in tasks:
                recommendations.append({
                    'Tool': 'Tableau or Power BI',
                    'Priority': 'High',
                    'Reason': 'Best for interactive dashboards'
                })
            
            # R
            if role in ["Portfolio Manager", "Risk Manager"] and coding in ["Advanced", "Expert"]:
                recommendations.append({
                    'Tool': 'R',
                    'Priority': 'Medium',
                    'Reason': 'Excellent for statistical analysis'
                })
            
            df_rec = pd.DataFrame(recommendations)
            
            st.markdown("**Recommended Tools:**")
            st.table(df_rec)
            
            st.success("""
            **Learning Path:**
            
            1. Start with Essential tools
            2. Add High priority as needed
            3. Consider Medium based on specific needs
            
            **Time Investment:**
            - Essential tools: 2-4 weeks each
            - High priority: 1-3 months each
            - Medium: As needed for specialization
            """)

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 11 Quiz: Tools and Software")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'Which Excel function is best for lookups in large tables?',
            'options': [
                'VLOOKUP',
                'INDEX-MATCH',
                'LOOKUP',
                'FIND'
            ],
            'correct': 'INDEX-MATCH',
            'explanation': 'INDEX-MATCH is more flexible and faster than VLOOKUP, especially for large datasets.'
        },
        {
            'id': 2,
            'question': 'Python\'s pandas library is primarily used for:',
            'options': [
                'Web scraping',
                'Data manipulation and analysis',
                'Machine learning',
                'Visualization'
            ],
            'correct': 'Data manipulation and analysis',
            'explanation': 'pandas is the core Python library for working with structured data (DataFrames).'
        },
        {
            'id': 3,
            'question': 'SQL SELECT statement returns:',
            'options': [
                'One row always',
                'Modified data',
                'Query results (rows and columns)',
                'Database schema'
            ],
            'correct': 'Query results (rows and columns)',
            'explanation': 'SELECT retrieves data from tables and returns matching rows and specified columns.'
        },
        {
            'id': 4,
            'question': 'Tableau is best described as:',
            'options': [
                'Programming language',
                'Database system',
                'Data visualization and BI tool',
                'Statistical software'
            ],
            'correct': 'Data visualization and BI tool',
            'explanation': 'Tableau specializes in interactive data visualization and business intelligence dashboards.'
        },
        {
            'id': 5,
            'question': 'Power Query in Excel is used for:',
            'options': [
                'Creating charts',
                'Data cleaning and transformation',
                'Writing VBA code',
                'Financial calculations'
            ],
            'correct': 'Data cleaning and transformation',
            'explanation': 'Power Query (Get & Transform) is Excel\'s ETL tool for preparing data.'
        },
        {
            'id': 6,
            'question': 'Which is NOT a Python data visualization library?',
            'options': [
                'matplotlib',
                'seaborn',
                'plotly',
                'django'
            ],
            'correct': 'django',
            'explanation': 'django is a web framework, not a visualization library. The others are all for creating charts and graphs.'
        },
        {
            'id': 7,
            'question': 'SQL JOIN is used to:',
            'options': [
                'Combine data from multiple tables',
                'Sort data',
                'Filter rows',
                'Calculate totals'
            ],
            'correct': 'Combine data from multiple tables',
            'explanation': 'JOIN operations combine rows from two or more tables based on related columns.'
        },
        {
            'id': 8,
            'question': 'R is particularly strong in:',
            'options': [
                'Web development',
                'Statistical analysis',
                'Mobile apps',
                'Database administration'
            ],
            'correct': 'Statistical analysis',
            'explanation': 'R was designed specifically for statistical computing and is widely used in research and quantitative finance.'
        },
        {
            'id': 9,
            'question': 'Power BI\'s DAX language is used for:',
            'options': [
                'Database queries',
                'Calculations and measures',
                'Web scraping',
                'Report formatting'
            ],
            'correct': 'Calculations and measures',
            'explanation': 'DAX (Data Analysis Expressions) creates custom calculations and measures in Power BI.'
        },
        {
            'id': 10,
            'question': 'For working with 10+ million rows, you should use:',
            'options': [
                'Excel only',
                'SQL database with Python/R',
                'Word documents',
                'PowerPoint'
            ],
            'correct': 'SQL database with Python/R',
            'explanation': 'Large datasets require databases (SQL) combined with programming tools (Python/R) for efficient processing.'
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
    st.header("Module 11 Summary")
    
    st.subheader("🎯 Essential Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Must-Have Skills:**
        - **Excel:** Universal, essential for finance
        - **SQL:** Working with databases
        - **Python or R:** Advanced analysis
        - **BI Tool:** Tableau or Power BI
        """)
        
        st.success("""
        **Excel Mastery:**
        - Formulas: VLOOKUP, SUMIFS, INDEX-MATCH
        - PivotTables for analysis
        - Power Query for ETL
        - Financial functions (NPV, IRR)
        - VBA for automation
        """)
    
    with col2:
        st.warning("""
        **Python Key Libraries:**
        - pandas: Data manipulation
        - numpy: Numerical computing
        - matplotlib/plotly: Visualization
        - scikit-learn: Machine learning
        - statsmodels: Statistics
        """)
        
        st.info("""
        **SQL Essentials:**
        - SELECT, FROM, WHERE
        - JOIN operations
        - GROUP BY aggregations
        - Window functions
        - Subqueries
        """)
    
    st.markdown("---")
    st.subheader("📊 Tool Selection Guide")
    
    selection_guide = pd.DataFrame({
        'Use Case': [
            'Quick analysis',
            'Financial modeling',
            'Large datasets (1M+ rows)',
            'Machine learning',
            'Interactive dashboards',
            'Statistical research',
            'Automation',
            'Reporting'
        ],
        'Best Tool': [
            'Excel',
            'Excel',
            'SQL + Python',
            'Python',
            'Tableau/Power BI',
            'R',
            'Python',
            'Power BI/Tableau'
        ],
        'Alternative': [
            'Python',
            'Python',
            'R + SQL',
            'R',
            'Python (Dash)',
            'Python',
            'VBA',
            'Excel'
        ]
    })
    
    st.table(selection_guide)
    
    st.markdown("---")
    st.subheader("💼 Career Path Recommendations")
    
    tab1, tab2, tab3 = st.tabs(["Financial Analyst", "Data Analyst", "Quant/Risk"])
    
    with tab1:
        st.markdown("""
        **Financial Analyst Tool Stack:**
        
        **Essential (Priority 1):**
        - Excel (Advanced): Financial modeling, valuation
        - Power BI or Tableau: Dashboards and reporting
        - SQL (Basic-Intermediate): Query financial data
        
        **Highly Valuable (Priority 2):**
        - Python (Intermediate): Automation, data analysis
        - Bloomberg Terminal: Market data
        - ERP systems: SAP, Oracle
        
        **Nice to Have (Priority 3):**
        - VBA: Excel automation
        - R: Statistical analysis
        - Cloud platforms: AWS, Azure
        
        **Time Investment:**
        - Months 1-3: Excel mastery
        - Months 4-6: SQL + BI tool
        - Months 7+: Python for automation
        """)
    
    with tab2:
        st.markdown("""
        **Data Analyst Tool Stack:**
        
        **Essential (Priority 1):**
        - SQL (Advanced): Primary data access
        - Python (Intermediate-Advanced): pandas, numpy
        - Tableau or Power BI (Advanced): Visualizations
        
        **Highly Valuable (Priority 2):**
        - Excel (Intermediate): Quick analysis
        - Git: Version control
        - Cloud data warehouses: Snowflake, BigQuery
        
        **Nice to Have (Priority 3):**
        - R: Statistical methods
        - Apache Airflow: Orchestration
        - dbt: Data transformation
        
        **Time Investment:**
        - Months 1-4: SQL + Python
        - Months 5-7: BI tool mastery
        - Months 8+: Cloud platforms
        """)
    
    with tab3:
        st.markdown("""
        **Quant/Risk Analyst Tool Stack:**
        
        **Essential (Priority 1):**
        - Python (Advanced): ML, optimization
        - R (Advanced): Statistical modeling
        - SQL (Intermediate): Data access
        
        **Highly Valuable (Priority 2):**
        - MATLAB: Numerical computing
        - C++: Performance-critical code
        - QuantLib: Derivatives pricing
        
        **Nice to Have (Priority 3):**
        - Excel: Prototyping
        - Tableau: Result visualization
        - Hadoop/Spark: Big data
        
        **Time Investment:**
        - Months 1-6: Python + R mastery
        - Months 7-12: Advanced statistics
        - Year 2+: Domain specialization
        """)
    
    st.markdown("---")
    
    st.subheader("🎓 Learning Resources")
    
    resources = pd.DataFrame({
        'Tool': ['Excel', 'Python', 'SQL', 'Tableau', 'Power BI', 'R'],
        'Free Resources': [
            'Excel Jet, ExcelIsFun YouTube',
            'Python.org docs, Real Python',
            'SQLZoo, Mode Analytics tutorials',
            'Tableau Public',
            'Microsoft Learn',
            'R for Data Science (book)'
        ],
        'Paid/Certification': [
            'Wall Street Prep, Udemy',
            'DataCamp, Coursera',
            'DataCamp, Udacity',
            'Tableau Desktop Specialist',
            'Microsoft PL-300',
            'Coursera specializations'
        ],
        'Practice': [
            'Financial modeling templates',
            'Kaggle, LeetCode',
            'HackerRank, LeetCode',
            'Makeover Monday',
            'Power BI community',
            'R exercises, Tidy Tuesday'
        ]
    })
    
    st.table(resources)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 12?**
    
    Module 12: Case Studies and Projects covers:
    - Real-world applications
    - End-to-end projects
    - Portfolio pieces
    - Capstone exercises
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #e8eaf6; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 11 of 12: Tools and Software</p>
</div>
""", unsafe_allow_html=True)