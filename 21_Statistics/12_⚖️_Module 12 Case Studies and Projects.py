import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1b5e20 0%, #388e3c 50%, #4caf50 100%);
    }
    h1 {
        color: #c8e6c9;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #a5d6a7;
        border-left: 6px solid #c8e6c9;
        padding-left: 15px;
    }
    h3 {
        color: #dcedc8;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>🎯 Module 12: Case Studies and Projects</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #dcedc8;'>Real-World Applications & Portfolio Projects</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Case Studies", "🎮 Projects", "🧮 Portfolio Builder", "📝 Final Assessment", "📋 Course Conclusion"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 12 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("12.1 Approaching Real-World Problems")
    
    st.subheader("The Analytics Project Lifecycle")
    
    st.warning("""
    **End-to-End Analytics Project:**
    
    Moving from theory to practice requires a structured approach.
    Real-world projects are messy, data is imperfect, and stakeholders have competing priorities.
    """)
    
    lifecycle = pd.DataFrame({
        'Phase': ['1. Problem Definition', '2. Data Collection', '3. Data Preparation', 
                 '4. Exploratory Analysis', '5. Modeling', '6. Validation', 
                 '7. Communication', '8. Deployment'],
        'Key Activities': [
            'Define objectives, success metrics, stakeholders',
            'Identify data sources, APIs, databases, files',
            'Clean, transform, handle missing values, outliers',
            'Visualize, summarize, find patterns, anomalies',
            'Build models, feature engineering, tuning',
            'Test on holdout data, backtesting, stress test',
            'Create visualizations, reports, presentations',
            'Production deployment, monitoring, maintenance'
        ],
        'Common Challenges': [
            'Vague requirements, shifting goals',
            'Data access issues, privacy concerns',
            'Messy data, 80% of project time here',
            'Finding signal in noise, bias',
            'Overfitting, wrong model choice',
            'Not testing properly, data leakage',
            'Technical jargon, executive buy-in',
            'Model drift, scaling issues'
        ],
        'Deliverables': [
            'Project charter, requirements doc',
            'Data dictionary, source documentation',
            'Clean dataset, transformation code',
            'EDA report, visualizations',
            'Trained model, performance metrics',
            'Validation report, test results',
            'Presentation, dashboard, report',
            'Production code, monitoring plan'
        ]
    })
    
    st.dataframe(lifecycle)
    
    st.markdown("---")
    
    st.subheader("Best Practices for Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Do's:**
        
        **1. Start with the Business Question**
        - What decision needs to be made?
        - What's the impact of being wrong?
        - Who will use the results?
        
        **2. Understand Your Data**
        - Where does it come from?
        - What do the fields mean?
        - What are the limitations?
        
        **3. Document Everything**
        - Assumptions made
        - Data transformations
        - Model parameters
        - Code comments
        
        **4. Validate Thoroughly**
        - Out-of-sample testing
        - Cross-validation
        - Sensitivity analysis
        - Sanity checks
        """)
    
    with col2:
        st.warning("""
        **Don'ts:**
        
        **1. Don't Skip EDA**
        - Never model without exploring first
        - Visualize your data
        - Check distributions
        - Look for anomalies
        
        **2. Don't Overfit**
        - Simpler is often better
        - Test on unseen data
        - Use regularization
        - Monitor performance
        
        **3. Don't Ignore Context**
        - Business logic matters
        - Domain expertise is critical
        - Models aren't truth
        - Results must make sense
        
        **4. Don't Overcomplicate**
        - Start simple, add complexity if needed
        - Explain to non-technical audience
        - Actionable insights > fancy models
        """)
    
    st.markdown("---")
    
    # Communication
    st.header("12.2 Communicating Results")
    
    st.subheader("Storytelling with Data")
    
    st.success("""
    **Effective Communication Principles:**
    
    1. **Know Your Audience**
       - Executives: High-level, business impact
       - Analysts: Methodology, details
       - Technical teams: Code, implementation
    
    2. **Structure Your Story**
       - Context: Why does this matter?
       - Conflict: What's the problem?
       - Resolution: What did we find?
       - Call to Action: What should we do?
    
    3. **Visual > Text**
       - One chart worth 1,000 words
       - Clear, labeled visualizations
       - Remove chartjunk
       - Highlight key findings
    
    4. **Make it Actionable**
       - So what? Now what?
       - Clear recommendations
       - Next steps
       - Expected outcomes
    """)
    
    st.markdown("---")
    
    st.subheader("Common Deliverables")
    
    deliverables = pd.DataFrame({
        'Deliverable': ['Executive Summary', 'Technical Report', 'Dashboard', 'Presentation', 'Code Repository'],
        'Audience': [
            'C-suite, senior management',
            'Data science team, analysts',
            'Business users, managers',
            'Stakeholders, decision makers',
            'Developers, future analysts'
        ],
        'Key Elements': [
            '1-2 pages, key findings, recommendations',
            'Methodology, results, validation, appendix',
            'KPIs, trends, filters, drill-downs',
            '10-15 slides, visualizations, story arc',
            'Clean code, documentation, README'
        ],
        'Tools': [
            'Word, PowerPoint, email',
            'Jupyter, R Markdown, LaTeX',
            'Tableau, Power BI, Streamlit',
            'PowerPoint, Google Slides',
            'GitHub, GitLab, Bitbucket'
        ]
    })
    
    st.table(deliverables)
    
    st.markdown("---")
    
    # Ethics
    st.header("12.3 Ethics and Responsible Analytics")
    
    st.subheader("Ethical Considerations")
    
    st.error("""
    **Critical Ethical Issues:**
    
    **1. Data Privacy**
    - GDPR, CCPA compliance
    - Personally identifiable information (PII)
    - Consent and transparency
    - Data anonymization
    
    **2. Bias and Fairness**
    - Sampling bias
    - Historical bias in data
    - Algorithmic discrimination
    - Protected characteristics
    
    **3. Transparency**
    - Model explainability
    - Black box concerns
    - Stakeholder understanding
    - Documentation
    
    **4. Misuse of Results**
    - Cherry-picking findings
    - P-hacking
    - Misleading visualizations
    - Ignoring limitations
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Red Flags to Watch:**
        
        - Data seems "too perfect"
        - Results align exactly with expectations
        - Can't reproduce findings
        - No discussion of limitations
        - Pressure to manipulate results
        - Ignoring negative results
        - Using data without permission
        - Models affecting people's lives without validation
        """)
    
    with col2:
        st.success("""
        **Best Practices:**
        
        - Document all assumptions
        - Test for bias explicitly
        - Validate with multiple methods
        - Peer review findings
        - Disclose limitations
        - Consider second-order effects
        - Regular model audits
        - Ethics review for high-stakes applications
        """)
    
    st.markdown("---")
    
    # Building Portfolio
    st.header("12.4 Building Your Analytics Portfolio")
    
    st.subheader("Why a Portfolio Matters")
    
    st.warning("""
    **Portfolio Benefits:**
    
    - **Demonstrate Skills:** Show, don't just tell
    - **Stand Out:** Differentiate from other candidates
    - **Learning:** Best way to solidify knowledge
    - **Conversations:** Talking points in interviews
    - **Professional Brand:** Online presence
    """)
    
    st.markdown("---")
    
    st.subheader("Portfolio Project Guidelines")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Good Portfolio Projects:**
        
        **Characteristics:**
        - Real or realistic data
        - Business question driven
        - End-to-end (data → insights)
        - Well documented
        - Reproducible
        - Professional presentation
        
        **Examples:**
        - Credit risk modeling
        - Stock portfolio optimization
        - Customer churn prediction
        - Sales forecasting
        - A/B test analysis
        - Fraud detection system
        """)
    
    with col2:
        st.success("""
        **Portfolio Structure:**
        
        **Each Project Should Have:**
        1. Clear title and description
        2. Business problem statement
        3. Data source and description
        4. Methodology explanation
        5. Key visualizations
        6. Results and insights
        7. Recommendations
        8. Code (clean and commented)
        9. Limitations discussed
        
        **Where to Host:**
        - GitHub (code + README)
        - Personal website/blog
        - Medium articles
        - Kaggle notebooks
        - LinkedIn posts
        """)
    
    st.markdown("---")
    
    # Project Ideas
    st.header("12.5 Project Ideas by Domain")
    
    project_ideas = pd.DataFrame({
        'Domain': [
            'Portfolio Management',
            'Risk Analytics',
            'Corporate Finance',
            'Retail Banking',
            'Investment Banking',
            'Insurance',
            'Fintech',
            'Trading'
        ],
        'Beginner Projects': [
            'Portfolio return calculation, basic Sharpe ratio',
            'Historical VaR calculator',
            'DCF valuation model',
            'Customer segmentation (simple)',
            'M&A deal analysis',
            'Claims frequency analysis',
            'Payment default prediction',
            'Moving average crossover backtest'
        ],
        'Intermediate Projects': [
            'Efficient frontier optimizer, factor analysis',
            'Monte Carlo VaR, stress testing',
            'Sensitivity analysis, scenario modeling',
            'CLV prediction, churn modeling',
            'Comparable company analysis automation',
            'Loss severity modeling',
            'Fraud detection system',
            'Multi-factor trading strategy'
        ],
        'Advanced Projects': [
            'Black-Litterman allocation, ML for returns',
            'CVaR optimization, tail risk hedging',
            'Full LBO model with ML forecasts',
            'Real-time recommendation engine',
            'Deal outcome prediction ML model',
            'Catastrophe modeling, reserving optimization',
            'Credit scoring with alternative data',
            'HFT signal generation, execution optimization'
        ]
    })
    
    st.dataframe(project_ideas, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Capstone Project Recommendations")
    
    st.success("""
    **Ideal Capstone Project:**
    
    Combines multiple techniques from the course:
    
    **Example: "Algorithmic Portfolio Management System"**
    
    1. **Data Collection** (Module 11)
       - API integration for market data
       - Fundamental data scraping
       
    2. **Time Series Analysis** (Module 5)
       - Returns forecasting
       - Volatility modeling (GARCH)
       
    3. **Statistical Methods** (Modules 3-4)
       - Factor analysis
       - Regression for returns
       
    4. **Machine Learning** (Module 9)
       - Regime detection
       - Feature engineering
       
    5. **Portfolio Optimization** (Module 6)
       - Efficient frontier
       - Risk budgeting
       
    6. **Risk Management** (Module 7)
       - VaR calculation
       - Stress testing
       
    7. **Visualization** (Module 11)
       - Interactive dashboard
       - Performance reports
       
    **Deliverables:**
    - Code repository (GitHub)
    - Technical documentation
    - Interactive dashboard
    - Performance backtest report
    - Presentation deck
    """)

# ======================
# CASE STUDIES PAGE
# ======================
elif page == "💡 Case Studies":
    st.header("Real-World Case Studies")
    
    case_study = st.selectbox(
        "Select Case Study:",
        ["Credit Risk Assessment", "Portfolio Rebalancing Strategy", 
         "Customer Churn Analysis", "Sales Forecasting Model"]
    )
    
    if case_study == "Credit Risk Assessment":
        st.subheader("Case Study 1: Credit Risk Assessment")
        
        st.markdown("""
        **Business Context:**
        
        A regional bank wants to improve its loan approval process by building 
        a data-driven credit risk model to predict loan defaults.
        
        **Current Situation:**
        - Manual review process
        - Inconsistent decisions
        - 15% default rate (industry avg: 8-10%)
        - Lost opportunities (good applicants rejected)
        
        **Objective:**
        Build a model to predict probability of default and recommend approval decisions.
        """)
        
        st.markdown("---")
        
        # Generate sample data
        np.random.seed(42)
        n_samples = 1000
        
        # Features
        credit_score = np.random.normal(650, 100, n_samples).clip(300, 850)
        debt_to_income = np.random.uniform(0.1, 0.8, n_samples)
        loan_amount = np.random.uniform(5000, 50000, n_samples)
        employment_length = np.random.randint(0, 30, n_samples)
        
        # Target (influenced by features)
        default_prob = (
            -0.005 * credit_score +
            2.0 * debt_to_income +
            0.00005 * loan_amount -
            0.02 * employment_length +
            3.5
        )
        default_prob = 1 / (1 + np.exp(-default_prob))
        default = (np.random.random(n_samples) < default_prob).astype(int)
        
        df_credit = pd.DataFrame({
            'Credit_Score': credit_score,
            'Debt_to_Income': debt_to_income,
            'Loan_Amount': loan_amount,
            'Employment_Length': employment_length,
            'Default': default
        })
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**Data Overview:**")
            st.dataframe(df_credit.head(10))
            
            st.markdown("**Summary Statistics:**")
            st.dataframe(df_credit.describe().round(2))
            
            default_rate = df_credit['Default'].mean()
            st.metric("Overall Default Rate", f"{default_rate:.1%}")
        
        with col2:
            # Visualizations
            fig1 = px.histogram(
                df_credit,
                x='Credit_Score',
                color='Default',
                title='Credit Score Distribution by Default Status',
                barmode='overlay',
                labels={'Default': 'Defaulted'}
            )
            fig1.update_layout(template="plotly_dark", height=300)
            st.plotly_chart(fig1, use_container_width=True)
            
            fig2 = px.box(
                df_credit,
                x='Default',
                y='Debt_to_Income',
                title='Debt-to-Income by Default Status',
                labels={'Default': 'Defaulted'}
            )
            fig2.update_layout(template="plotly_dark", height=250)
            st.plotly_chart(fig2, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("**Analysis Approach:**")
        
        tabs = st.tabs(["1. EDA", "2. Modeling", "3. Results", "4. Recommendations"])
        
        with tabs[0]:
            st.markdown("""
            **Exploratory Data Analysis:**
            
            **Key Findings:**
            1. Credit Score: Strong negative correlation with default
            2. Debt-to-Income: Positive correlation with default
            3. Employment Length: Slight protective factor
            4. Loan Amount: Weak positive correlation
            
            **Data Quality:**
            - No missing values
            - No obvious outliers
            - Distributions appear reasonable
            - Some class imbalance (85% no default)
            """)
            
            # Correlation matrix
            corr_matrix = df_credit.corr()
            
            fig = px.imshow(
                corr_matrix,
                title='Correlation Matrix',
                color_continuous_scale='RdBu',
                aspect='auto'
            )
            fig.update_layout(template="plotly_dark", height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with tabs[1]:
            st.markdown("""
            **Modeling Approach:**
            
            **Model Selection:** Logistic Regression
            - Interpretable (coefficients)
            - Probability outputs
            - Well-suited for binary classification
            - Regulatory acceptable (explainable)
            
            **Features Used:**
            - Credit Score (standardized)
            - Debt-to-Income Ratio
            - Log(Loan Amount)
            - Employment Length
            
            **Train-Test Split:** 70-30
            **Validation:** 5-fold cross-validation
            """)
            
            st.code("""
# Pseudocode
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Prepare data
X = df[['Credit_Score', 'Debt_to_Income', 
        'Loan_Amount', 'Employment_Length']]
y = df['Default']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y
)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
            """, language='python')
        
        with tabs[2]:
            st.markdown("**Model Performance:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                metrics = pd.DataFrame({
                    'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC-AUC'],
                    'Value': [0.82, 0.65, 0.58, 0.61, 0.78]
                })
                st.table(metrics)
                
                st.success("""
                **Model achieves:**
                - 82% overall accuracy
                - 78% ROC-AUC (good discrimination)
                - Identifies 58% of actual defaults
                - 65% of predicted defaults are correct
                """)
            
            with col2:
                # Feature importance (coefficients)
                importance = pd.DataFrame({
                    'Feature': ['Credit Score', 'Debt-to-Income', 'Loan Amount', 'Employment'],
                    'Coefficient': [-0.82, 1.45, 0.23, -0.15]
                })
                
                fig = px.bar(
                    importance,
                    x='Coefficient',
                    y='Feature',
                    orientation='h',
                    title='Feature Importance (Coefficients)'
                )
                fig.update_layout(template="plotly_dark", height=300)
                st.plotly_chart(fig, use_container_width=True)
        
        with tabs[3]:
            st.markdown("**Business Recommendations:**")
            
            st.success("""
            **1. Implement Risk-Based Pricing**
            - Use predicted probability for interest rates
            - High risk (>20% default prob) → Higher rates or reject
            - Medium risk (10-20%) → Standard rates
            - Low risk (<10%) → Competitive rates
            
            **2. Automated Pre-Screening**
            - Auto-approve low risk applications
            - Auto-reject very high risk
            - Manual review for borderline cases
            
            **3. Expected Impact**
            - Reduce defaults from 15% to ~10%
            - Approve 20% more good applicants
            - Save $500K annually in default costs
            - Increase revenue $200K from better pricing
            
            **4. Implementation Plan**
            - Phase 1: Parallel testing (3 months)
            - Phase 2: Gradual rollout (6 months)
            - Phase 3: Full deployment with monitoring
            
            **5. Ongoing Monitoring**
            - Monthly model performance review
            - Quarterly retraining
            - Annual model validation
            - Bias testing (demographic fairness)
            """)
    
    elif case_study == "Portfolio Rebalancing Strategy":
        st.subheader("Case Study 2: Systematic Portfolio Rebalancing")
        
        st.markdown("""
        **Business Context:**
        
        Investment firm manages $500M across multiple client portfolios.
        Current rebalancing is ad-hoc and inconsistent.
        
        **Challenge:**
        Develop systematic rebalancing strategy that:
        1. Maintains target allocations
        2. Minimizes transaction costs
        3. Considers tax implications
        4. Scales across all accounts
        """)
        
        # Implementation shown in interactive demo
        st.info("See the 'Projects' tab for interactive portfolio rebalancing tool")
    
    elif case_study == "Customer Churn Analysis":
        st.subheader("Case Study 3: SaaS Customer Churn Reduction")
        
        st.markdown("""
        **Business Context:**
        
        B2B SaaS company with $50M ARR facing 25% annual churn.
        
        **Problem:**
        - High customer acquisition cost ($5,000)
        - Losing customers after 12-18 months
        - No early warning system
        - Reactive retention efforts
        
        **Goal:**
        Predict churn 90 days in advance to enable proactive retention.
        """)
        
        st.markdown("---")
        
        # Generate churn data
        np.random.seed(42)
        n = 500
        
        login_freq = np.random.randint(1, 50, n)
        feature_usage = np.random.uniform(0, 1, n)
        support_tickets = np.random.randint(0, 15, n)
        contract_value = np.random.uniform(1000, 50000, n)
        tenure_months = np.random.randint(1, 60, n)
        
        # Churn probability
        churn_score = (
            -0.05 * login_freq +
            -2.0 * feature_usage +
            0.15 * support_tickets +
            -0.00002 * contract_value +
            -0.03 * tenure_months +
            2.0
        )
        churn_prob = 1 / (1 + np.exp(-churn_score))
        churned = (np.random.random(n) < churn_prob).astype(int)
        
        df_churn = pd.DataFrame({
            'Monthly_Logins': login_freq,
            'Feature_Usage_Score': feature_usage,
            'Support_Tickets': support_tickets,
            'Contract_Value': contract_value,
            'Tenure_Months': tenure_months,
            'Churned': churned
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Customer Data:**")
            st.dataframe(df_churn.head(10))
            
            churn_rate = df_churn['Churned'].mean()
            st.metric("Churn Rate", f"{churn_rate:.1%}")
            
            # Churn by tenure
            tenure_groups = pd.cut(df_churn['Tenure_Months'], 
                                  bins=[0, 12, 24, 36, 60],
                                  labels=['0-12m', '12-24m', '24-36m', '36-60m'])
            churn_by_tenure = df_churn.groupby(tenure_groups)['Churned'].mean()
            
            st.markdown("**Churn by Tenure:**")
            st.dataframe(churn_by_tenure.to_frame('Churn Rate').style.format('{:.1%}'))
        
        with col2:
            # Visualizations
            fig = px.scatter(
                df_churn,
                x='Monthly_Logins',
                y='Feature_Usage_Score',
                color='Churned',
                title='Engagement Patterns',
                labels={'Churned': 'Churned?'}
            )
            fig.update_layout(template="plotly_dark", height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("**Solution Summary:**")
        
        st.success("""
        **Model Results:**
        - Random Forest classifier
        - 85% accuracy, 0.82 AUC
        - Top predictors: Login frequency, Feature usage, Support tickets
        
        **Intervention Strategy:**
        
        **High Risk (>70% churn probability):**
        - Immediate account manager outreach
        - Custom success plan
        - Executive sponsorship
        - Special pricing consideration
        
        **Medium Risk (40-70%):**
        - Automated email sequence
        - Feature adoption webinar invitation
        - Quarterly business review
        
        **Impact After 6 Months:**
        - Churn reduced from 25% to 18%
        - $3.5M ARR saved
        - 140 customers retained
        - ROI: 8x on retention program costs
        """)

# ======================
# PROJECTS PAGE
# ======================
elif page == "🎮 Projects":
    st.header("Interactive Projects")
    
    project = st.selectbox(
        "Select Project:",
        ["Portfolio Optimizer", "Financial Dashboard", "Risk Calculator", "Forecast Model"]
    )
    
    if project == "Portfolio Optimizer":
        st.subheader("📊 Portfolio Optimization Tool")
        
        st.markdown("""
        Build an optimal portfolio using Modern Portfolio Theory.
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Portfolio Parameters:**")
            
            n_assets = st.slider("Number of assets:", 3, 8, 4)
            
            # Generate random returns and risks
            np.random.seed(42)
            exp_returns = np.random.uniform(0.05, 0.20, n_assets)
            volatilities = np.random.uniform(0.10, 0.35, n_assets)
            
            asset_names = [f"Asset {i+1}" for i in range(n_assets)]
            
            # Display asset characteristics
            st.markdown("**Asset Characteristics:**")
            asset_df = pd.DataFrame({
                'Asset': asset_names,
                'Expected Return': exp_returns,
                'Volatility': volatilities
            })
            st.dataframe(asset_df.style.format({
                'Expected Return': '{:.1%}',
                'Volatility': '{:.1%}'
            }))
            
            target_return = st.slider(
                "Target Return:",
                float(exp_returns.min()),
                float(exp_returns.max()),
                float(exp_returns.mean()),
                0.01
            )
            
            if st.button("Optimize Portfolio"):
                # Create correlation matrix
                corr = np.random.uniform(0.3, 0.7, (n_assets, n_assets))
                np.fill_diagonal(corr, 1.0)
                corr = (corr + corr.T) / 2  # Make symmetric
                
                # Covariance matrix
                cov = np.outer(volatilities, volatilities) * corr
                
                # Optimization
                from scipy.optimize import minimize
                
                def portfolio_variance(weights):
                    return np.dot(weights, np.dot(cov, weights))
                
                def portfolio_return(weights):
                    return np.dot(weights, exp_returns)
                
                constraints = [
                    {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
                    {'type': 'eq', 'fun': lambda w: portfolio_return(w) - target_return}
                ]
                
                bounds = [(0, 1) for _ in range(n_assets)]
                initial = np.array([1/n_assets] * n_assets)
                
                result = minimize(
                    portfolio_variance,
                    initial,
                    method='SLSQP',
                    bounds=bounds,
                    constraints=constraints
                )
                
                if result.success:
                    optimal_weights = result.x
                    optimal_risk = np.sqrt(result.fun)
                    optimal_return = portfolio_return(optimal_weights)
                    
                    st.session_state['portfolio_result'] = {
                        'weights': optimal_weights,
                        'return': optimal_return,
                        'risk': optimal_risk,
                        'assets': asset_names
                    }
        
        with col2:
            if 'portfolio_result' in st.session_state:
                res = st.session_state['portfolio_result']
                
                # Metrics
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Portfolio Return", f"{res['return']:.2%}")
                with col_b:
                    st.metric("Portfolio Risk", f"{res['risk']:.2%}")
                
                # Pie chart
                fig1 = go.Figure(data=[go.Pie(
                    labels=res['assets'],
                    values=res['weights'] * 100,
                    hole=0.3
                )])
                fig1.update_layout(
                    title="Optimal Portfolio Allocation",
                    template="plotly_dark",
                    height=400
                )
                st.plotly_chart(fig1, use_container_width=True)
                
                # Weights table
                weights_df = pd.DataFrame({
                    'Asset': res['assets'],
                    'Weight': res['weights'] * 100
                })
                weights_df = weights_df[weights_df['Weight'] > 0.1]  # Filter small weights
                
                st.markdown("**Allocation Details:**")
                st.dataframe(weights_df.style.format({'Weight': '{:.1f}%'}))
    
    elif project == "Financial Dashboard":
        st.subheader("📈 Interactive Financial Dashboard")
        
        st.markdown("Real-time financial metrics dashboard")
        
        # Generate sample data
        np.random.seed(42)
        dates = pd.date_range('2024-01-01', periods=90, freq='D')
        
        revenue = np.random.normal(100000, 15000, 90).cumsum()
        expenses = np.random.normal(70000, 10000, 90).cumsum()
        profit = revenue - expenses
        
        df_financial = pd.DataFrame({
            'Date': dates,
            'Revenue': revenue,
            'Expenses': expenses,
            'Profit': profit
        })
        
        # KPIs
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Revenue", f"${revenue[-1]/1e6:.2f}M")
        with col2:
            st.metric("Total Expenses", f"${expenses[-1]/1e6:.2f}M")
        with col3:
            st.metric("Net Profit", f"${profit[-1]/1e6:.2f}M")
        with col4:
            margin = (profit[-1] / revenue[-1]) * 100
            st.metric("Profit Margin", f"{margin:.1f}%")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=dates, y=revenue, name='Revenue', line=dict(color='#4caf50')))
            fig1.add_trace(go.Scatter(x=dates, y=expenses, name='Expenses', line=dict(color='#f44336')))
            fig1.update_layout(title="Revenue vs Expenses", template="plotly_dark", height=400)
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=dates, y=profit, name='Profit', 
                                     fill='tozeroy', line=dict(color='#2196f3')))
            fig2.update_layout(title="Net Profit Over Time", template="plotly_dark", height=400)
            st.plotly_chart(fig2, use_container_width=True)
    
    elif project == "Risk Calculator":
        st.subheader("⚠️ Portfolio Risk Calculator")
        
        st.markdown("Calculate VaR and risk metrics for your portfolio")
        
        col1, col2 = st.columns(2)
        
        with col1:
            portfolio_value = st.number_input("Portfolio Value ($):", value=1000000, step=100000)
            expected_return = st.slider("Expected Annual Return (%):", -10, 30, 8) / 100
            volatility = st.slider("Annual Volatility (%):", 5, 50, 20) / 100
            confidence = st.slider("Confidence Level (%):", 90, 99, 95)
            time_horizon = st.selectbox("Time Horizon:", [1, 5, 10, 20])
            
            if st.button("Calculate Risk"):
                # Scale for time horizon
                mu_scaled = expected_return * (time_horizon / 252)
                sigma_scaled = volatility * np.sqrt(time_horizon / 252)
                
                # VaR
                z = stats.norm.ppf(confidence / 100)
                var_pct = -(mu_scaled - z * sigma_scaled)
                var_dollar = var_pct * portfolio_value
                
                # CVaR approximation
                pdf_at_var = stats.norm.pdf(z)
                cvar_pct = sigma_scaled * pdf_at_var / (1 - confidence/100)
                cvar_dollar = cvar_pct * portfolio_value
                
                st.session_state['risk_results'] = {
                    'var_pct': var_pct,
                    'var_dollar': var_dollar,
                    'cvar_dollar': cvar_dollar,
                    'confidence': confidence,
                    'horizon': time_horizon
                }
        
        with col2:
            if 'risk_results' in st.session_state:
                res = st.session_state['risk_results']
                
                st.markdown("**Risk Metrics:**")
                st.metric(f"{res['horizon']}-day {res['confidence']}% VaR", 
                         f"${res['var_dollar']:,.0f}")
                st.metric(f"{res['horizon']}-day {res['confidence']}% CVaR", 
                         f"${res['cvar_dollar']:,.0f}")
                
                st.info(f"""
                **Interpretation:**
                
                {res['confidence']}% of the time, losses over {res['horizon']} day(s) 
                will be less than ${res['var_dollar']:,.0f}.
                
                In worst {100-res['confidence']}% of cases, average loss 
                is ${res['cvar_dollar']:,.0f}.
                """)

# ======================
# PORTFOLIO BUILDER PAGE
# ======================
elif page == "🧮 Portfolio Builder":
    st.header("Build Your Analytics Portfolio")
    
    st.markdown("""
    Use this guide to create professional portfolio projects.
    """)
    
    project_template = st.selectbox(
        "Choose Project Template:",
        ["Financial Analysis", "Predictive Model", "Dashboard", "Research Report"]
    )
    
    if project_template == "Financial Analysis":
        st.subheader("📊 Financial Analysis Project Template")
        
        st.markdown("""
        **Project Structure:**
        
        1. **Title & Overview**
           - Clear, descriptive title
           - One-paragraph summary
           - Business question addressed
        
        2. **Data**
           - Source and description
           - Time period covered
           - Variables included
           - Data cleaning steps
        
        3. **Methodology**
           - Analytical approach
           - Tools used
           - Key assumptions
        
        4. **Analysis**
           - Exploratory data analysis
           - Statistical tests
           - Visualizations
        
        5. **Results**
           - Key findings
           - Tables and charts
           - Statistical significance
        
        6. **Recommendations**
           - Actionable insights
           - Business implications
           - Next steps
        
        7. **Code**
           - Clean, commented code
           - Reproducible
           - GitHub repository
        """)
        
        st.code("""
# Example README.md structure

# Stock Portfolio Performance Analysis

## Overview
Analysis of a diversified stock portfolio's performance over 5 years,
comparing against S&P 500 benchmark and evaluating risk-adjusted returns.

## Data
- Source: Yahoo Finance API
- Period: 2019-2024
- Stocks: 10 large-cap US equities
- Frequency: Daily closing prices

## Methodology
- Portfolio construction: Equal-weighted
- Metrics: Sharpe ratio, max drawdown, beta
- Tools: Python (pandas, numpy, matplotlib)

## Key Findings
1. Portfolio Sharpe ratio: 0.85 (vs S&P 500: 0.72)
2. Beta: 0.92 (lower market sensitivity)
3. Max drawdown: -28% (vs S&P 500: -34%)

## Files
- `analysis.ipynb`: Main analysis
- `data/`: Raw price data
- `results/`: Charts and tables
- `requirements.txt`: Dependencies

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook analysis.ipynb
```
        """, language='markdown')
    
    elif project_template == "Predictive Model":
        st.subheader("🤖 Predictive Model Project Template")
        
        st.markdown("""
        **ML Project Structure:**
        
        **1. Problem Definition**
        - Business objective
        - Success metrics
        - Stakeholders
        
        **2. Data Exploration**
        - Data sources
        - Sample size
        - Feature distribution
        - Missing values
        - Outliers
        
        **3. Feature Engineering**
        - New features created
        - Transformations applied
        - Feature selection
        
        **4. Model Development**
        - Models tested
        - Hyperparameter tuning
        - Cross-validation strategy
        
        **5. Evaluation**
        - Performance metrics
        - Confusion matrix
        - Feature importance
        - Error analysis
        
        **6. Deployment Considerations**
        - Model serving approach
        - Monitoring strategy
        - Retraining schedule
        """)
        
        st.success("""
        **Portfolio Tips:**
        
        ✅ **Do:**
        - Compare multiple models
        - Show validation process
        - Discuss limitations
        - Include visualizations
        - Explain business impact
        
        ❌ **Avoid:**
        - Only showing best results
        - Ignoring class imbalance
        - No test set
        - Overly complex models without justification
        - Missing business context
        """)

# ======================
# FINAL ASSESSMENT PAGE
# ======================
elif page == "📝 Final Assessment":
    st.header("Final Course Assessment")
    
    st.markdown("""
    Test your knowledge across all 12 modules with this comprehensive assessment.
    """)
    
    if 'final_quiz_submitted' not in st.session_state:
        st.session_state.final_quiz_submitted = False
        st.session_state.final_answers = {}
    
    questions = [
        {
            'id': 1,
            'module': 'Module 1',
            'question': 'The standard deviation measures:',
            'options': ['Central tendency', 'Dispersion', 'Skewness', 'Outliers'],
            'correct': 'Dispersion'
        },
        {
            'id': 2,
            'module': 'Module 2',
            'question': 'A probability of 0.5 means:',
            'options': ['Impossible', 'Unlikely', 'Equally likely', 'Certain'],
            'correct': 'Equally likely'
        },
        {
            'id': 3,
            'module': 'Module 3',
            'question': 'Type I error is:',
            'options': [
                'Failing to reject a true null',
                'Rejecting a true null hypothesis',
                'Accepting false null',
                'Correct decision'
            ],
            'correct': 'Rejecting a true null hypothesis'
        },
        {
            'id': 4,
            'module': 'Module 4',
            'question': 'R-squared measures:',
            'options': [
                'Correlation',
                'Variance explained',
                'Slope',
                'Residuals'
            ],
            'correct': 'Variance explained'
        },
        {
            'id': 5,
            'module': 'Module 5',
            'question': 'ARIMA models are used for:',
            'options': [
                'Classification',
                'Time series forecasting',
                'Clustering',
                'Dimensionality reduction'
            ],
            'correct': 'Time series forecasting'
        },
        {
            'id': 6,
            'module': 'Module 6',
            'question': 'Portfolio diversification reduces:',
            'options': [
                'Systematic risk',
                'Unsystematic risk',
                'All risk',
                'Return'
            ],
            'correct': 'Unsystematic risk'
        },
        {
            'id': 7,
            'module': 'Module 7',
            'question': 'VaR is:',
            'options': [
                'Average loss',
                'Maximum possible loss',
                'Loss threshold at confidence level',
                'Standard deviation'
            ],
            'correct': 'Loss threshold at confidence level'
        },
        {
            'id': 8,
            'module': 'Module 8',
            'question': 'PCA is used for:',
            'options': [
                'Classification',
                'Dimensionality reduction',
                'Regression',
                'Clustering'
            ],
            'correct': 'Dimensionality reduction'
        },
        {
            'id': 9,
            'module': 'Module 9',
            'question': 'Overfitting occurs when:',
            'options': [
                'Model is too simple',
                'Train accuracy >> Test accuracy',
                'Both accuracies are low',
                'Data is too clean'
            ],
            'correct': 'Train accuracy >> Test accuracy'
        },
        {
            'id': 10,
            'module': 'Module 10',
            'question': 'CLV stands for:',
            'options': [
                'Customer Lifetime Value',
                'Current Loss Value',
                'Calculated Linear Variable',
                'Cumulative Loan Value'
            ],
            'correct': 'Customer Lifetime Value'
        },
        {
            'id': 11,
            'module': 'Module 11',
            'question': 'SQL is primarily used for:',
            'options': [
                'Visualization',
                'Database queries',
                'Machine learning',
                'Report formatting'
            ],
            'correct': 'Database queries'
        },
        {
            'id': 12,
            'module': 'Module 12',
            'question': 'A good analytics project should:',
            'options': [
                'Use the most complex model',
                'Address a business question',
                'Avoid documentation',
                'Only show successful results'
            ],
            'correct': 'Address a business question'
        }
    ]
    
    for q in questions:
        st.subheader(f"Question {q['id']} ({q['module']})")
        st.markdown(f"**{q['question']}**")
        
        answer = st.radio(
            "Select answer:",
            q['options'],
            key=f"fq{q['id']}",
            disabled=st.session_state.final_quiz_submitted
        )
        
        st.session_state.final_answers[q['id']] = answer
        
        if st.session_state.final_quiz_submitted:
            if answer == q['correct']:
                st.success(f"✅ Correct!")
            else:
                st.error(f"❌ Incorrect. Answer: **{q['correct']}**")
        
        st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if not st.session_state.final_quiz_submitted:
            if st.button("Submit Final Assessment", type="primary"):
                st.session_state.final_quiz_submitted = True
                st.rerun()
    
    with col2:
        if st.session_state.final_quiz_submitted:
            if st.button("Retake Assessment"):
                st.session_state.final_quiz_submitted = False
                st.session_state.final_answers = {}
                st.rerun()
    
    if st.session_state.final_quiz_submitted:
        correct = sum(1 for q in questions 
                     if st.session_state.final_answers.get(q['id']) == q['correct'])
        percentage = (correct / len(questions)) * 100
        
        st.markdown("---")
        st.subheader("📊 Final Assessment Results")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Score", f"{correct}/{len(questions)}")
        with col2:
            st.metric("Percentage", f"{percentage:.0f}%")
        with col3:
            if percentage >= 80:
                grade = "🎓 Excellent - Course Completed!"
            elif percentage >= 60:
                grade = "👍 Good - Review weak areas"
            else:
                grade = "📚 Review material"
            st.metric("Grade", grade)
        
        if percentage >= 80:
            st.balloons()
            st.success("""
            🎉 **Congratulations on completing the course!**
            
            You've mastered statistics for finance and are ready to apply
            these skills in real-world scenarios.
            
            **Next Steps:**
            1. Build portfolio projects
            2. Apply techniques at work
            3. Continue learning advanced topics
            4. Share your knowledge with others
            """)

# ======================
# COURSE CONCLUSION PAGE
# ======================
elif page == "📋 Course Conclusion":
    st.header("Course Conclusion")
    
    st.markdown("""
    # 🎓 Congratulations!
    
    You've completed **Statistics for Finance Professionals** - a comprehensive 
    12-module course covering everything from basic statistics to advanced 
    machine learning applications in finance.
    """)
    
    st.markdown("---")
    
    st.subheader("📚 What You've Learned")
    
    modules_summary = pd.DataFrame({
        'Module': [
            '1. Foundations',
            '2. Probability',
            '3. Inference',
            '4. Regression',
            '5. Time Series',
            '6. Portfolio Stats',
            '7. Risk Analytics',
            '8. Advanced Methods',
            '9. Machine Learning',
            '10. Business Analytics',
            '11. Tools',
            '12. Projects'
        ],
        'Key Topics': [
            'Descriptive statistics, distributions',
            'Probability rules, Bayes, distributions',
            'Hypothesis testing, confidence intervals',
            'Linear regression, CAPM, diagnostics',
            'ARIMA, GARCH, stationarity',
            'Portfolio optimization, Sharpe ratio',
            'VaR, CVaR, stress testing',
            'PCA, non-parametric, bootstrap',
            'Classification, regression, ML models',
            'CLV, churn, A/B testing, forecasting',
            'Excel, Python, SQL, Tableau',
            'Case studies, real-world applications'
        ],
        'Skills Gained': [
            'Data summarization, visualization',
            'Risk modeling, probability calculations',
            'Statistical testing, decision making',
            'Predictive modeling, relationships',
            'Forecasting, trend analysis',
            'Portfolio construction, optimization',
            'Risk measurement, management',
            'Advanced statistical techniques',
            'Predictive analytics, automation',
            'Business problem solving',
            'Technical tool proficiency',
            'End-to-end project execution'
        ]
    })
    
    st.dataframe(modules_summary, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🎯 Your Journey Forward")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Immediate Actions:**
        
        1. **Build Your Portfolio**
           - 3-5 projects showcasing skills
           - GitHub repositories
           - Blog posts explaining work
        
        2. **Apply at Work**
           - Identify opportunities
           - Start with small projects
           - Demonstrate value
        
        3. **Continue Learning**
           - Deep dive into specializations
           - Advanced courses (ML, quant)
           - Industry certifications
        
        4. **Network**
           - LinkedIn presence
           - Industry meetups
           - Online communities
        """)
    
    with col2:
        st.success("""
        **Career Paths:**
        
        **Financial Analyst:**
        - Focus: Excel, financial modeling
        - Tools: Excel, Power BI, SQL
        - Skills: Valuation, forecasting
        
        **Data Analyst:**
        - Focus: Data analysis, visualization
        - Tools: Python, SQL, Tableau
        - Skills: SQL, statistical analysis
        
        **Quantitative Analyst:**
        - Focus: Mathematical models
        - Tools: Python, R, MATLAB
        - Skills: Advanced statistics, ML
        
        **Risk Manager:**
        - Focus: Risk measurement
        - Tools: Python, Excel, risk systems
        - Skills: VaR, stress testing
        """)
    
    st.markdown("---")
    
    st.subheader("📖 Recommended Resources")
    
    resources = pd.DataFrame({
        'Category': ['Books', 'Online Courses', 'Websites', 'Communities'],
        'Resources': [
            'The Intelligent Investor, Options/Futures (Hull), Python for Finance',
            'Coursera Financial Engineering, edX Data Science, DataCamp',
            'Investopedia, QuantStart, Kaggle, Towards Data Science',
            'r/datascience, r/finance, LinkedIn groups, Local meetups'
        ]
    })
    
    st.table(resources)
    
    st.markdown("---")
    
    st.subheader("💼 Building Your Portfolio")
    
    st.warning("""
    **Portfolio Project Ideas:**
    
    **Beginner:**
    1. Stock portfolio analysis with Sharpe ratio
    2. Credit card default prediction
    3. Sales forecasting dashboard
    4. A/B test analysis
    
    **Intermediate:**
    1. Multi-factor portfolio optimization
    2. Customer churn prediction with ML
    3. VaR calculator with Monte Carlo
    4. Time series forecasting (ARIMA/GARCH)
    
    **Advanced:**
    1. Algorithmic trading system with backtesting
    2. Credit risk model with alternative data
    3. Real-time fraud detection
    4. Portfolio risk attribution system
    
    **Showcase Tips:**
    - Clear README with business context
    - Visualizations and insights
    - Clean, documented code
    - Results and recommendations
    - Deploy as web app (Streamlit/Dash)
    """)
    
    st.markdown("---")
    
    st.subheader("🏆 Final Thoughts")
    
    st.success("""
    **Remember:**
    
    📊 **Statistics is a tool, not the goal**
    - Always start with the business question
    - Simple often beats complex
    - Interpretation matters more than technique
    
    💡 **Learning never stops**
    - Field evolves constantly
    - New techniques emerge
    - Stay curious and keep practicing
    
    🤝 **Share your knowledge**
    - Teach others
    - Write blog posts
    - Contribute to open source
    
    🎯 **Focus on impact**
    - Solve real problems
    - Create business value
    - Make data-driven decisions accessible
    
    ---
    
    **You now have the knowledge and tools to:**
    - Analyze financial data rigorously
    - Build predictive models
    - Manage and measure risk
    - Communicate insights effectively
    - Make data-driven decisions
    
    **The rest is up to you. Good luck! 🚀**
    """)
    
    st.balloons()
    
    st.markdown("---")
    
    st.markdown("""
    <div style='text-align: center; padding: 30px;'>
        <h2 style='color: #4caf50;'>Thank you for completing</h2>
        <h1 style='color: #c8e6c9;'>Statistics for Finance Professionals</h1>
        <p style='color: #a5d6a7; font-size: 1.2rem;'>A 12-Module Comprehensive Course</p>
        <br>
        <p style='color: #dcedc8;'>Created with ❤️ for aspiring finance professionals</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #dcedc8; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 12 of 12: Case Studies and Projects</p>
    <p>🎓 Course Complete!</p>
</div>
""", unsafe_allow_html=True)