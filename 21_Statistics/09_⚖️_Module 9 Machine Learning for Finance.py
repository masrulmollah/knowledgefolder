import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, roc_curve, auc, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #004d40 0%, #00695c 50%, #00796b 100%);
    }
    h1 {
        color: #a7ffeb;
        font-size: 3rem;
        text-align: center;
        padding: 20px;
    }
    h2 {
        color: #64ffda;
        border-left: 6px solid #a7ffeb;
        padding-left: 15px;
    }
    h3 {
        color: #b2dfdb;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1>🤖 Module 9: Machine Learning for Finance</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #b2dfdb;'>Predictive Analytics & Classification</h3>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    ["🎓 Theory", "💡 Examples", "🎮 Interactive Exercise", "🧮 Calculator", "📝 Quiz", "📋 Summary"]
)

st.sidebar.markdown("---")
st.sidebar.info("**Module 9 of 12**\n\nStatistics for Finance Professionals")

# ======================
# THEORY PAGE
# ======================
if page == "🎓 Theory":
    st.header("9.1 Introduction to Machine Learning")
    
    st.subheader("What is Machine Learning?")
    
    st.warning("""
    **Machine Learning:**
    
    Algorithms that learn patterns from data to make predictions or decisions 
    without being explicitly programmed.
    
    **Key Idea:**
    Use historical data to predict future outcomes or classify new observations.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Types of Machine Learning:**
        
        **1. Supervised Learning**
        - Learn from labeled data
        - Predict known outputs
        - Examples: Classification, Regression
        
        **2. Unsupervised Learning**
        - Learn from unlabeled data
        - Find hidden patterns
        - Examples: Clustering, PCA
        
        **3. Reinforcement Learning**
        - Learn through trial and error
        - Maximize rewards
        - Examples: Trading bots, game AI
        """)
    
    with col2:
        st.success("""
        **ML vs Traditional Statistics:**
        
        **Traditional Statistics:**
        - Focus on inference
        - Hypothesis testing
        - Interpretability
        - Small to medium data
        
        **Machine Learning:**
        - Focus on prediction
        - Pattern recognition
        - Often "black box"
        - Large data (big data)
        
        **In Finance:**
        - Both approaches complement each other
        - Statistics for understanding
        - ML for prediction
        """)
    
    st.markdown("---")
    
    st.subheader("Machine Learning Workflow")
    
    workflow = pd.DataFrame({
        'Step': ['1. Problem Definition', '2. Data Collection', '3. Data Preparation', 
                '4. Feature Engineering', '5. Model Selection', '6. Training', 
                '7. Evaluation', '8. Deployment'],
        'Description': [
            'Define objective: Predict, classify, cluster?',
            'Gather relevant data: prices, fundamentals, sentiment',
            'Clean, handle missing values, outliers',
            'Create meaningful features from raw data',
            'Choose algorithm(s): logistic, tree, neural net',
            'Fit model on training data',
            'Test on holdout data: accuracy, precision, etc.',
            'Put into production, monitor performance'
        ],
        'Finance Example': [
            'Predict loan default (binary classification)',
            'Credit history, income, debt ratios',
            'Remove duplicates, impute missing income',
            'Debt-to-income ratio, payment history score',
            'Logistic regression, random forest',
            'Train on 2018-2022 data',
            'Test on 2023 data: 85% accuracy',
            'Score new loan applications in real-time'
        ]
    })
    
    st.table(workflow)
    
    st.markdown("---")
    
    # Classification
    st.header("9.2 Classification Methods")
    
    st.subheader("Binary Classification")
    
    st.info("""
    **Binary Classification:**
    
    Predict one of two outcomes (Yes/No, 0/1, True/False)
    
    **Financial Applications:**
    - Credit default: Default or No Default
    - Stock movement: Up or Down
    - Fraud detection: Fraud or Legitimate
    - Customer churn: Leave or Stay
    - M&A success: Success or Failure
    """)
    
    st.markdown("---")
    
    st.markdown("### 1. Logistic Regression")
    
    st.latex(r"P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + ... + \beta_p X_p)}}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Logistic Regression:**
        
        **What it does:**
        - Predicts probability of binary outcome
        - S-shaped (sigmoid) curve
        - Output between 0 and 1
        
        **How it works:**
        - Linear combination of features
        - Transform through sigmoid function
        - Threshold at 0.5 (typically)
        
        **Advantages:**
        - Simple and interpretable
        - Provides probabilities
        - Fast training
        - Works well for linearly separable data
        """)
    
    with col2:
        st.warning("""
        **Interpretation:**
        
        **Coefficients (β):**
        - Positive β: Increases probability
        - Negative β: Decreases probability
        - Magnitude shows strength of effect
        
        **Odds Ratio:**
        - exp(β) = Odds ratio
        - OR > 1: Increases odds
        - OR < 1: Decreases odds
        
        **Example:**
        - β_debt_ratio = 2.5
        - OR = e^2.5 ≈ 12.2
        - 1-unit increase in debt ratio multiplies 
          odds of default by 12.2
        """)
    
    st.markdown("---")
    
    st.markdown("### 2. Decision Trees")
    
    st.success("""
    **Decision Trees:**
    
    **Structure:**
    - Tree-like model of decisions
    - Root node → Internal nodes → Leaf nodes
    - Each node = decision rule
    - Each leaf = prediction
    
    **Example for Credit Scoring:**
    ```
    Root: Debt-to-Income > 0.4?
    ├─ Yes: Payment History > 2 late payments?
    │  ├─ Yes: HIGH RISK (Default)
    │  └─ No: MEDIUM RISK
    └─ No: Income > $50k?
       ├─ Yes: LOW RISK (No Default)
       └─ No: MEDIUM RISK
    ```
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Advantages:**
        - Very interpretable
        - Handles non-linear relationships
        - No feature scaling needed
        - Can handle missing values
        - Shows feature importance
        
        **Applications:**
        - Credit scoring
        - Customer segmentation
        - Risk classification
        - Rule-based systems
        """)
    
    with col2:
        st.warning("""
        **Disadvantages:**
        - Prone to overfitting
        - Unstable (small data changes → big tree changes)
        - Not great for extrapolation
        - Biased to dominant classes
        
        **Solutions:**
        - Pruning (limit depth)
        - Ensemble methods (Random Forest)
        - Cross-validation
        - Minimum samples per leaf
        """)
    
    st.markdown("---")
    
    st.markdown("### 3. Random Forest")
    
    st.success("""
    **Random Forest:**
    
    Ensemble of many decision trees trained on random subsets of data and features.
    
    **How it works:**
    1. Create many decision trees (e.g., 100 trees)
    2. Each tree trained on random subset of data (bootstrap)
    3. Each split considers random subset of features
    4. Final prediction = majority vote (classification) or average (regression)
    
    **Why it's powerful:**
    - Reduces overfitting (compared to single tree)
    - More stable and robust
    - Handles non-linearity well
    - Provides feature importance
    - Generally excellent performance
    """)
    
    st.markdown("---")
    
    # Model Evaluation
    st.header("9.3 Model Evaluation")
    
    st.subheader("Classification Metrics")
    
    st.markdown("### Confusion Matrix")
    
    confusion_df = pd.DataFrame({
        '': ['Actual Positive', 'Actual Negative'],
        'Predicted Positive': ['True Positive (TP)', 'False Positive (FP)'],
        'Predicted Negative': ['False Negative (FN)', 'True Negative (TN)']
    })
    
    st.table(confusion_df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Accuracy:**")
        st.latex(r"\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}")
        
        st.info("""
        - Overall correctness
        - Can be misleading with imbalanced data
        - Example: 95% accuracy on 95% negative class
        """)
        
        st.markdown("**Precision:**")
        st.latex(r"\text{Precision} = \frac{TP}{TP + FP}")
        
        st.info("""
        - Of predicted positives, how many are correct?
        - Important when False Positives are costly
        - Example: Fraud detection (don't annoy customers)
        """)
    
    with col2:
        st.markdown("**Recall (Sensitivity):**")
        st.latex(r"\text{Recall} = \frac{TP}{TP + FN}")
        
        st.info("""
        - Of actual positives, how many did we catch?
        - Important when False Negatives are costly
        - Example: Disease detection (don't miss cases)
        """)
        
        st.markdown("**F1 Score:**")
        st.latex(r"F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}")
        
        st.info("""
        - Harmonic mean of precision and recall
        - Balances both metrics
        - Good for imbalanced data
        """)
    
    st.markdown("---")
    
    st.markdown("### ROC Curve and AUC")
    
    st.warning("""
    **ROC Curve:**
    
    Receiver Operating Characteristic curve plots:
    - True Positive Rate (Recall) vs False Positive Rate
    - Shows tradeoff at different thresholds
    
    **AUC (Area Under Curve):**
    - Single number summary (0 to 1)
    - 1.0 = Perfect classifier
    - 0.5 = Random guessing
    - 0.7-0.8 = Good
    - 0.8-0.9 = Excellent
    - 0.9+ = Outstanding
    
    **When to use:**
    - Comparing models
    - Threshold-independent evaluation
    - Imbalanced datasets
    """)
    
    st.markdown("---")
    
    # Regression
    st.header("9.4 Regression for Prediction")
    
    st.subheader("Regression Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Mean Squared Error (MSE):**")
        st.latex(r"MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2")
        
        st.info("""
        - Average squared error
        - Penalizes large errors heavily
        - Same units as y² (hard to interpret)
        """)
        
        st.markdown("**Root MSE (RMSE):**")
        st.latex(r"RMSE = \sqrt{MSE}")
        
        st.info("""
        - Square root of MSE
        - Same units as y
        - More interpretable than MSE
        - Common choice for evaluation
        """)
    
    with col2:
        st.markdown("**Mean Absolute Error (MAE):**")
        st.latex(r"MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|")
        
        st.info("""
        - Average absolute error
        - More robust to outliers than MSE
        - Same units as y
        - Linear penalty (vs squared)
        """)
        
        st.markdown("**R-squared (R²):**")
        st.latex(r"R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}")
        
        st.info("""
        - Proportion of variance explained
        - Range: -∞ to 1 (typically 0 to 1)
        - 0 = No better than mean
        - 1 = Perfect prediction
        """)
    
    st.markdown("---")
    
    # Overfitting
    st.header("9.5 Overfitting and Regularization")
    
    st.subheader("The Bias-Variance Tradeoff")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Overfitting:**
        
        Model learns noise in training data, 
        not true patterns
        
        **Signs:**
        - High training accuracy
        - Low test accuracy
        - Model too complex
        - Memorizes rather than generalizes
        
        **Example:**
        - Training accuracy: 99%
        - Test accuracy: 65%
        - Model has overfit!
        """)
    
    with col2:
        st.info("""
        **Underfitting:**
        
        Model too simple to capture patterns
        
        **Signs:**
        - Low training accuracy
        - Low test accuracy
        - Model too simple
        - Doesn't learn patterns
        
        **Example:**
        - Training accuracy: 60%
        - Test accuracy: 58%
        - Model is underfitting
        """)
    
    st.markdown("---")
    
    st.subheader("Regularization Techniques")
    
    st.success("""
    **Regularization:**
    Add penalty to model complexity to prevent overfitting
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Ridge Regression (L2):**")
        st.latex(r"\min \sum(y_i - \hat{y}_i)^2 + \lambda\sum\beta_j^2")
        
        st.info("""
        - Penalizes sum of squared coefficients
        - Shrinks coefficients toward zero
        - Keeps all features
        - Good when all features are relevant
        """)
    
    with col2:
        st.markdown("**Lasso Regression (L1):**")
        st.latex(r"\min \sum(y_i - \hat{y}_i)^2 + \lambda\sum|\beta_j|")
        
        st.info("""
        - Penalizes sum of absolute coefficients
        - Can set coefficients to exactly zero
        - Performs feature selection
        - Good when many irrelevant features
        """)
    
    st.markdown("---")
    
    st.subheader("Cross-Validation")
    
    st.warning("""
    **k-Fold Cross-Validation:**
    
    **Process:**
    1. Split data into k folds (e.g., k=5)
    2. Train on k-1 folds, test on 1 fold
    3. Repeat k times (each fold as test once)
    4. Average performance across all folds
    
    **Benefits:**
    - Better use of limited data
    - More reliable performance estimate
    - Reduces variance in evaluation
    - Helps detect overfitting
    
    **Typical k values:**
    - k = 5: Common choice, fast
    - k = 10: More thorough, slower
    - k = n: Leave-one-out (LOO)
    """)
    
    st.markdown("---")
    
    # Feature Engineering
    st.header("9.6 Feature Engineering")
    
    st.subheader("Creating Better Features")
    
    st.info("""
    **Feature Engineering:**
    The process of creating new features from existing data to improve model performance.
    
    **Often more important than algorithm choice!**
    """)
    
    techniques = pd.DataFrame({
        'Technique': [
            'Domain Features',
            'Interaction Terms',
            'Polynomial Features',
            'Binning/Discretization',
            'Lag Features',
            'Rolling Statistics',
            'One-Hot Encoding',
            'Feature Scaling'
        ],
        'Description': [
            'Domain knowledge → new features',
            'Multiply features together',
            'x, x², x³ for non-linearity',
            'Continuous → categorical',
            'Previous time period values',
            'Moving average, rolling std',
            'Categorical → binary columns',
            'Standardize or normalize'
        ],
        'Finance Example': [
            'Debt-to-income ratio, P/E ratio',
            'Age × Income, Sector × Size',
            'Returns, Returns², Returns³',
            'Income brackets, risk buckets',
            'Yesterday\'s return, last week returns',
            '50-day MA, 20-day volatility',
            'Industry dummy variables',
            'Z-score normalization of returns'
        ]
    })
    
    st.table(techniques)

# ======================
# EXAMPLES PAGE
# ======================
elif page == "💡 Examples":
    st.header("Machine Learning Examples")
    
    # Example 1: Logistic Regression
    st.subheader("Example 1: Credit Default Prediction (Logistic Regression)")
    
    st.markdown("""
    **Scenario:** Predict whether a borrower will default on a loan.
    
    **Features:** Debt-to-income ratio, Credit score, Loan amount
    **Target:** Default (1) or No Default (0)
    """)
    
    # Generate synthetic data
    np.random.seed(42)
    n_samples = 200
    
    # Features
    debt_to_income = np.random.uniform(0.1, 0.8, n_samples)
    credit_score = np.random.uniform(300, 850, n_samples)
    loan_amount = np.random.uniform(5000, 50000, n_samples)
    
    # Target (influenced by features)
    default_prob = (0.5 * debt_to_income - 0.0015 * credit_score + 0.00001 * loan_amount + 0.5)
    default_prob = 1 / (1 + np.exp(-5 * (default_prob - 0.5)))
    default = (np.random.random(n_samples) < default_prob).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Debt_to_Income': debt_to_income,
        'Credit_Score': credit_score,
        'Loan_Amount': loan_amount,
        'Default': default
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Sample Data:**")
        st.dataframe(df.head(10))
        
        # Train-test split
        X = df[['Debt_to_Income', 'Credit_Score', 'Loan_Amount']]
        y = df['Default']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # Train logistic regression
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        log_reg = LogisticRegression(random_state=42)
        log_reg.fit(X_train_scaled, y_train)
        
        # Predictions
        y_pred = log_reg.predict(X_test_scaled)
        y_pred_proba = log_reg.predict_proba(X_test_scaled)[:, 1]
        
        # Metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        st.markdown("**Model Performance:**")
        
        metrics_df = pd.DataFrame({
            'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score'],
            'Value': [accuracy, precision, recall, f1]
        })
        st.table(metrics_df.style.format({'Value': '{:.3f}'}))
        
        st.markdown("**Coefficients:**")
        coef_df = pd.DataFrame({
            'Feature': X.columns,
            'Coefficient': log_reg.coef_[0]
        })
        st.table(coef_df.style.format({'Coefficient': '{:.4f}'}))
        
        st.success(f"""
        **Interpretation:**
        
        - Positive Debt_to_Income coefficient: Higher debt ratio increases default risk
        - Negative Credit_Score coefficient: Higher score decreases default risk
        - Model achieves {accuracy:.1%} accuracy on test data
        """)
    
    with col2:
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        
        fig1 = go.Figure(data=go.Heatmap(
            z=cm,
            x=['Predicted No Default', 'Predicted Default'],
            y=['Actual No Default', 'Actual Default'],
            colorscale='Blues',
            text=cm,
            texttemplate='%{text}',
            textfont={"size": 20}
        ))
        
        fig1.update_layout(
            title="Confusion Matrix",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # ROC Curve
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)
        
        fig2 = go.Figure()
        
        fig2.add_trace(go.Scatter(
            x=fpr, y=tpr,
            mode='lines',
            name=f'ROC (AUC = {roc_auc:.3f})',
            line=dict(color='#a7ffeb', width=3)
        ))
        
        fig2.add_trace(go.Scatter(
            x=[0, 1], y=[0, 1],
            mode='lines',
            name='Random',
            line=dict(color='red', dash='dash')
        ))
        
        fig2.update_layout(
            title="ROC Curve",
            xaxis_title="False Positive Rate",
            yaxis_title="True Positive Rate",
            template="plotly_dark",
            height=300
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        st.info(f"""
        **ROC-AUC: {roc_auc:.3f}**
        
        {'Excellent' if roc_auc > 0.8 else 'Good' if roc_auc > 0.7 else 'Fair'} discrimination ability
        """)
    
    st.markdown("---")
    
    # Example 2: Random Forest
    st.subheader("Example 2: Stock Movement Prediction (Random Forest)")
    
    st.markdown("""
    **Scenario:** Predict if stock price will go up next day.
    
    **Features:** Previous returns, volume, volatility
    """)
    
    # Generate synthetic stock data
    np.random.seed(42)
    n_days = 300
    
    returns_1d = np.random.normal(0.05, 1.5, n_days)
    returns_5d = np.random.normal(0.1, 3, n_days)
    volume = np.random.uniform(1000000, 5000000, n_days)
    volatility = np.random.uniform(0.5, 3, n_days)
    
    # Target: 1 if next day return > 0
    next_return = np.random.normal(0.05, 1.5, n_days)
    direction = (next_return > 0).astype(int)
    
    df_stock = pd.DataFrame({
        'Return_1D': returns_1d,
        'Return_5D': returns_5d,
        'Volume': volume,
        'Volatility': volatility,
        'Direction': direction
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Data Sample:**")
        st.dataframe(df_stock.head(10))
        
        # Train-test split
        X = df_stock[['Return_1D', 'Return_5D', 'Volume', 'Volatility']]
        y = df_stock['Direction']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # Train Random Forest
        rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
        rf.fit(X_train, y_train)
        
        # Predictions
        y_pred = rf.predict(X_test)
        
        # Metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        
        st.markdown("**Performance:**")
        st.metric("Accuracy", f"{accuracy:.1%}")
        st.metric("Precision", f"{precision:.1%}")
        st.metric("Recall", f"{recall:.1%}")
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'Feature': X.columns,
            'Importance': rf.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        st.markdown("**Feature Importance:**")
        st.table(feature_importance.style.format({'Importance': '{:.4f}'}))
    
    with col2:
        # Feature importance plot
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=feature_importance['Importance'],
            y=feature_importance['Feature'],
            orientation='h',
            marker_color='#a7ffeb'
        ))
        
        fig.update_layout(
            title="Feature Importance",
            xaxis_title="Importance",
            yaxis_title="Feature",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Random Forest Advantages:**
        - Handles non-linear relationships
        - Robust to outliers
        - Provides feature importance
        - Less prone to overfitting than single tree
        
        **Note:**
        Stock direction prediction is inherently difficult 
        due to market efficiency!
        """)
    
    st.markdown("---")
    
    # Example 3: Regression
    st.subheader("Example 3: Return Prediction (Regression)")
    
    st.markdown("""
    **Scenario:** Predict actual stock returns (not just direction).
    """)
    
    # Generate data
    np.random.seed(42)
    n = 200
    
    market_return = np.random.normal(0.5, 2, n)
    sector_return = np.random.normal(0.3, 1.5, n)
    momentum = np.random.normal(0.1, 1, n)
    
    # Target
    stock_return = (0.8 * market_return + 0.5 * sector_return + 
                   0.3 * momentum + np.random.normal(0, 0.5, n))
    
    df_reg = pd.DataFrame({
        'Market_Return': market_return,
        'Sector_Return': sector_return,
        'Momentum': momentum,
        'Stock_Return': stock_return
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        X = df_reg[['Market_Return', 'Sector_Return', 'Momentum']]
        y = df_reg['Stock_Return']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        # Train models
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        
        ridge = Ridge(alpha=1.0)
        ridge.fit(X_train, y_train)
        
        # Predictions
        y_pred_lr = lr.predict(X_test)
        y_pred_ridge = ridge.predict(X_test)
        
        # Metrics
        rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
        r2_lr = r2_score(y_test, y_pred_lr)
        
        rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
        r2_ridge = r2_score(y_test, y_pred_ridge)
        
        st.markdown("**Model Comparison:**")
        
        comparison = pd.DataFrame({
            'Model': ['Linear Regression', 'Ridge Regression'],
            'RMSE': [rmse_lr, rmse_ridge],
            'R²': [r2_lr, r2_ridge]
        })
        st.table(comparison.style.format({'RMSE': '{:.4f}', 'R²': '{:.4f}'}))
    
    with col2:
        # Actual vs Predicted
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=y_test,
            y=y_pred_lr,
            mode='markers',
            name='Linear Regression',
            marker=dict(size=8, color='#a7ffeb', opacity=0.6)
        ))
        
        # 45-degree line
        min_val = min(y_test.min(), y_pred_lr.min())
        max_val = max(y_test.max(), y_pred_lr.max())
        
        fig.add_trace(go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            name='Perfect Prediction',
            line=dict(color='yellow', dash='dash')
        ))
        
        fig.update_layout(
            title="Actual vs Predicted Returns",
            xaxis_title="Actual Return (%)",
            yaxis_title="Predicted Return (%)",
            template="plotly_dark",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ======================
# INTERACTIVE EXERCISE PAGE
# ======================
elif page == "🎮 Interactive Exercise":
    st.header("Interactive ML Exercises")
    
    exercise = st.selectbox(
        "Choose Exercise:",
        ["Classification Builder", "Model Comparison", "Feature Importance Explorer", "Overfitting Demo"]
    )
    
    if exercise == "Classification Builder":
        st.subheader("🎯 Build Your Own Classifier")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Generate Data:**")
            
            n_samples = st.slider("Number of samples:", 100, 1000, 300)
            noise_level = st.slider("Noise level:", 0.1, 2.0, 0.5, 0.1)
            
            model_type = st.selectbox("Model:", 
                                     ["Logistic Regression", "Decision Tree", "Random Forest"])
            
            if st.button("Train Model"):
                # Generate data
                np.random.seed(42)
                
                X1 = np.random.randn(n_samples)
                X2 = np.random.randn(n_samples)
                
                # Create non-linear decision boundary
                y = ((X1**2 + X2**2) > 1.5).astype(int)
                
                # Add noise
                noise_idx = np.random.choice(n_samples, int(noise_level * n_samples / 2), replace=False)
                y[noise_idx] = 1 - y[noise_idx]
                
                X = np.column_stack([X1, X2])
                
                # Split
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                
                # Train
                if model_type == "Logistic Regression":
                    model = LogisticRegression()
                elif model_type == "Decision Tree":
                    model = DecisionTreeClassifier(max_depth=5)
                else:
                    model = RandomForestClassifier(n_estimators=100, max_depth=5)
                
                model.fit(X_train, y_train)
                
                # Evaluate
                train_acc = model.score(X_train, y_train)
                test_acc = model.score(X_test, y_test)
                
                st.session_state['model_data'] = {
                    'X': X,
                    'y': y,
                    'X_test': X_test,
                    'y_test': y_test,
                    'model': model,
                    'train_acc': train_acc,
                    'test_acc': test_acc
                }
        
        with col2:
            if 'model_data' in st.session_state:
                data = st.session_state['model_data']
                
                # Decision boundary
                fig = go.Figure()
                
                # Create mesh
                h = 0.1
                x_min, x_max = data['X'][:, 0].min() - 1, data['X'][:, 0].max() + 1
                y_min, y_max = data['X'][:, 1].min() - 1, data['X'][:, 1].max() + 1
                xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                                    np.arange(y_min, y_max, h))
                
                Z = data['model'].predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                
                # Plot decision boundary
                fig.add_trace(go.Contour(
                    x=xx[0],
                    y=yy[:, 0],
                    z=Z,
                    colorscale=[[0, '#004d40'], [1, '#a7ffeb']],
                    showscale=False,
                    opacity=0.3
                ))
                
                # Plot points
                colors = ['#ff6b6b' if label == 0 else '#4ecdc4' for label in data['y']]
                
                fig.add_trace(go.Scatter(
                    x=data['X'][:, 0],
                    y=data['X'][:, 1],
                    mode='markers',
                    marker=dict(size=8, color=colors, opacity=0.6),
                    name='Data Points'
                ))
                
                fig.update_layout(
                    title=f"{model_type} Decision Boundary",
                    xaxis_title="Feature 1",
                    yaxis_title="Feature 2",
                    template="plotly_dark",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Metrics
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Train Accuracy", f"{data['train_acc']:.1%}")
                with col_b:
                    st.metric("Test Accuracy", f"{data['test_acc']:.1%}")
                
                if data['train_acc'] - data['test_acc'] > 0.1:
                    st.warning("⚠️ Model may be overfitting (train >> test)")
                elif data['test_acc'] < 0.65:
                    st.info("Model may be underfitting (low accuracy)")
                else:
                    st.success("✅ Model looks good!")
    
    elif exercise == "Model Comparison":
        st.subheader("📊 Compare ML Models")
        
        if st.button("Generate Data & Train All Models"):
            # Generate data
            np.random.seed(42)
            n = 400
            
            X1 = np.random.randn(n)
            X2 = np.random.randn(n)
            y = ((X1**2 + X2**2) > 1.5).astype(int)
            
            X = np.column_stack([X1, X2])
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            
            # Train multiple models
            models = {
                'Logistic Regression': LogisticRegression(),
                'Decision Tree (depth=3)': DecisionTreeClassifier(max_depth=3),
                'Decision Tree (depth=10)': DecisionTreeClassifier(max_depth=10),
                'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=5)
            }
            
            results = []
            for name, model in models.items():
                model.fit(X_train, y_train)
                
                train_acc = model.score(X_train, y_train)
                test_acc = model.score(X_test, y_test)
                
                y_pred = model.predict(X_test)
                precision = precision_score(y_test, y_pred)
                recall = recall_score(y_test, y_pred)
                
                results.append({
                    'Model': name,
                    'Train Acc': train_acc,
                    'Test Acc': test_acc,
                    'Precision': precision,
                    'Recall': recall
                })
            
            df_results = pd.DataFrame(results)
            
            st.markdown("**Model Performance Comparison:**")
            st.dataframe(df_results.style.format({
                'Train Acc': '{:.3f}',
                'Test Acc': '{:.3f}',
                'Precision': '{:.3f}',
                'Recall': '{:.3f}'
            }))
            
            # Bar chart
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                name='Train Accuracy',
                x=df_results['Model'],
                y=df_results['Train Acc'],
                marker_color='#a7ffeb'
            ))
            
            fig.add_trace(go.Bar(
                name='Test Accuracy',
                x=df_results['Model'],
                y=df_results['Test Acc'],
                marker_color='#64ffda'
            ))
            
            fig.update_layout(
                title="Model Accuracy Comparison",
                xaxis_title="Model",
                yaxis_title="Accuracy",
                barmode='group',
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.info("""
            **Observations:**
            - Decision Tree (depth=10) has highest train but lower test → overfitting
            - Random Forest balances train and test well
            - Logistic Regression underfits non-linear boundary
            """)
    
    elif exercise == "Feature Importance Explorer":
        st.subheader("🔍 Feature Importance Analysis")
        
        if st.button("Train Random Forest & Show Importance"):
            # Generate data with different feature importances
            np.random.seed(42)
            n = 500
            
            important_feature = np.random.randn(n)
            medium_feature = np.random.randn(n)
            noise_feature1 = np.random.randn(n)
            noise_feature2 = np.random.randn(n)
            
            y = (2 * important_feature + 0.5 * medium_feature + 
                np.random.randn(n) * 0.5 > 0).astype(int)
            
            X = np.column_stack([important_feature, medium_feature, 
                                noise_feature1, noise_feature2])
            
            feature_names = ['Important Feature', 'Medium Feature', 
                           'Noise Feature 1', 'Noise Feature 2']
            
            # Train
            rf = RandomForestClassifier(n_estimators=100, random_state=42)
            rf.fit(X, y)
            
            # Feature importance
            importance = pd.DataFrame({
                'Feature': feature_names,
                'Importance': rf.feature_importances_
            }).sort_values('Importance', ascending=False)
            
            # Plot
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=importance['Importance'],
                y=importance['Feature'],
                orientation='h',
                marker_color='#a7ffeb',
                text=importance['Importance'].round(3),
                textposition='auto'
            ))
            
            fig.update_layout(
                title="Feature Importance from Random Forest",
                xaxis_title="Importance",
                yaxis_title="Feature",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.success("""
            **Correctly Identified:**
            - Important Feature has highest importance
            - Medium Feature has moderate importance
            - Noise Features have low importance
            
            **Use Cases:**
            - Feature selection
            - Understanding drivers
            - Model simplification
            """)
    
    elif exercise == "Overfitting Demo":
        st.subheader("⚠️ Overfitting Demonstration")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            max_depth = st.slider("Tree Max Depth:", 1, 20, 3)
            
            if st.button("Train Decision Tree"):
                # Generate simple data
                np.random.seed(42)
                n = 100
                
                X = np.random.randn(n, 2)
                y = (X[:, 0] > 0).astype(int)
                
                # Add noise
                noise_idx = np.random.choice(n, 15, replace=False)
                y[noise_idx] = 1 - y[noise_idx]
                
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.3, random_state=42
                )
                
                # Train with specified depth
                tree = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
                tree.fit(X_train, y_train)
                
                train_acc = tree.score(X_train, y_train)
                test_acc = tree.score(X_test, y_test)
                
                st.session_state['overfit_demo'] = {
                    'train_acc': train_acc,
                    'test_acc': test_acc,
                    'depth': max_depth
                }
        
        with col2:
            if 'overfit_demo' in st.session_state:
                data = st.session_state['overfit_demo']
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Train Accuracy", f"{data['train_acc']:.1%}")
                with col_b:
                    st.metric("Test Accuracy", f"{data['test_acc']:.1%}")
                
                gap = data['train_acc'] - data['test_acc']
                
                if gap > 0.2:
                    st.error(f"""
                    🚨 **OVERFITTING!**
                    
                    Train accuracy ({data['train_acc']:.1%}) >> Test accuracy ({data['test_acc']:.1%})
                    
                    Gap: {gap:.1%}
                    
                    Tree depth {data['depth']} is too high!
                    Try reducing max_depth.
                    """)
                elif data['train_acc'] < 0.7:
                    st.warning("""
                    **UNDERFITTING**
                    
                    Both accuracies are low.
                    Try increasing max_depth.
                    """)
                else:
                    st.success("""
                    ✅ **GOOD FIT**
                    
                    Model generalizes well to test data.
                    """)

# ======================
# CALCULATOR PAGE
# ======================
elif page == "🧮 Calculator":
    st.header("ML Calculators")
    
    calc_type = st.selectbox(
        "Select Calculator:",
        ["Classification Metrics", "Regression Metrics", "Confusion Matrix Analyzer"]
    )
    
    if calc_type == "Classification Metrics":
        st.subheader("Classification Metrics Calculator")
        
        st.markdown("**Enter confusion matrix values:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tp = st.number_input("True Positives (TP):", min_value=0, value=85)
            fn = st.number_input("False Negatives (FN):", min_value=0, value=15)
        
        with col2:
            fp = st.number_input("False Positives (FP):", min_value=0, value=10)
            tn = st.number_input("True Negatives (TN):", min_value=0, value=90)
        
        if st.button("Calculate Metrics"):
            total = tp + tn + fp + fn
            
            accuracy = (tp + tn) / total
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Accuracy", f"{accuracy:.3f}")
                st.metric("Precision", f"{precision:.3f}")
            
            with col2:
                st.metric("Recall", f"{recall:.3f}")
                st.metric("F1 Score", f"{f1:.3f}")
            
            # Confusion matrix visualization
            cm_data = [[tn, fp], [fn, tp]]
            
            fig = go.Figure(data=go.Heatmap(
                z=cm_data,
                x=['Predicted Negative', 'Predicted Positive'],
                y=['Actual Negative', 'Actual Positive'],
                colorscale='Blues',
                text=cm_data,
                texttemplate='%{text}',
                textfont={"size": 20}
            ))
            
            fig.update_layout(
                title="Confusion Matrix",
                template="plotly_dark",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

# ======================
# QUIZ PAGE
# ======================
elif page == "📝 Quiz":
    st.header("Module 9 Quiz: Machine Learning for Finance")
    
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
    
    questions = [
        {
            'id': 1,
            'question': 'Supervised learning requires:',
            'options': [
                'Only input features',
                'Labeled data with inputs and outputs',
                'No data at all',
                'Unsupervised preprocessing'
            ],
            'correct': 'Labeled data with inputs and outputs',
            'explanation': 'Supervised learning needs labeled examples (X, y) to learn the mapping from inputs to outputs.'
        },
        {
            'id': 2,
            'question': 'Logistic regression outputs:',
            'options': [
                'Continuous values',
                'Probabilities between 0 and 1',
                'Binary 0 or 1 directly',
                'Categories only'
            ],
            'correct': 'Probabilities between 0 and 1',
            'explanation': 'Logistic regression uses sigmoid function to output probabilities, which are then thresholded for classification.'
        },
        {
            'id': 3,
            'question': 'Precision measures:',
            'options': [
                'Of predicted positives, how many are correct',
                'Of actual positives, how many we caught',
                'Overall accuracy',
                'Total correct predictions'
            ],
            'correct': 'Of predicted positives, how many are correct',
            'explanation': 'Precision = TP/(TP+FP) - among predictions of positive class, what fraction are correct.'
        },
        {
            'id': 4,
            'question': 'Recall is important when:',
            'options': [
                'False positives are costly',
                'False negatives are costly',
                'Accuracy is all that matters',
                'Speed is critical'
            ],
            'correct': 'False negatives are costly',
            'explanation': 'Recall measures how many actual positives we catch. High recall means few false negatives (missed cases).'
        },
        {
            'id': 5,
            'question': 'ROC-AUC of 0.5 means:',
            'options': [
                'Perfect classifier',
                'Random guessing',
                'Excellent performance',
                'Model is broken'
            ],
            'correct': 'Random guessing',
            'explanation': 'AUC = 0.5 means the model performs no better than random chance. AUC = 1.0 is perfect.'
        },
        {
            'id': 6,
            'question': 'Overfitting occurs when:',
            'options': [
                'Train and test accuracy are both high',
                'Train accuracy >> test accuracy',
                'Both accuracies are low',
                'Model is too simple'
            ],
            'correct': 'Train accuracy >> test accuracy',
            'explanation': 'Overfitting: model memorizes training data but fails to generalize, leading to high train but low test performance.'
        },
        {
            'id': 7,
            'question': 'Random Forest is:',
            'options': [
                'Single decision tree',
                'Ensemble of decision trees',
                'Type of neural network',
                'Linear model'
            ],
            'correct': 'Ensemble of decision trees',
            'explanation': 'Random Forest combines many decision trees trained on random subsets to reduce overfitting and improve accuracy.'
        },
        {
            'id': 8,
            'question': 'Cross-validation helps to:',
            'options': [
                'Train model faster',
                'Estimate performance more reliably',
                'Increase training data',
                'Remove outliers'
            ],
            'correct': 'Estimate performance more reliably',
            'explanation': 'k-fold CV tests model on multiple train/test splits, giving more robust performance estimates.'
        },
        {
            'id': 9,
            'question': 'Feature engineering is:',
            'options': [
                'Creating new features from existing data',
                'Removing all features',
                'Always automatic',
                'Not important for ML'
            ],
            'correct': 'Creating new features from existing data',
            'explanation': 'Feature engineering transforms raw data into meaningful features that improve model performance.'
        },
        {
            'id': 10,
            'question': 'In finance, ML is most commonly used for:',
            'options': [
                'Replacing all human decisions',
                'Prediction and pattern recognition',
                'Generating random numbers',
                'Eliminating all risk'
            ],
            'correct': 'Prediction and pattern recognition',
            'explanation': 'ML excels at finding patterns and making predictions from data, complementing human expertise in finance.'
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
    st.header("Module 9 Summary")
    
    st.subheader("🎯 Key Concepts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Supervised Learning**
        - Classification: Predict categories
        - Regression: Predict continuous values
        - Requires labeled data
        - Train → Test → Deploy
        """)
        
        st.success("""
        **Classification Models**
        - Logistic Regression: Simple, interpretable
        - Decision Trees: Non-linear, visual
        - Random Forest: Robust, accurate
        - Each has tradeoffs
        """)
    
    with col2:
        st.warning("""
        **Model Evaluation**
        - Accuracy: Overall correctness
        - Precision: Correct positives
        - Recall: Catch all positives
        - F1: Balance precision/recall
        - ROC-AUC: Threshold-independent
        """)
        
        st.info("""
        **Best Practices**
        - Train/test split (80/20)
        - Cross-validation
        - Feature engineering
        - Regularization to prevent overfitting
        - Monitor performance over time
        """)
    
    st.markdown("---")
    st.subheader("📐 Key Formulas")
    
    formulas_df = pd.DataFrame({
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'RMSE'],
        'Formula': [
            '(TP + TN) / Total',
            'TP / (TP + FP)',
            'TP / (TP + FN)',
            '2 × (Prec × Rec) / (Prec + Rec)',
            '√(Σ(y - ŷ)² / n)'
        ]
    })
    st.table(formulas_df)
    
    st.markdown("---")
    st.subheader("💼 Financial Applications")
    
    tab1, tab2, tab3 = st.tabs(["Credit Risk", "Trading", "Fraud Detection"])
    
    with tab1:
        st.markdown("""
        **Credit Risk Modeling:**
        
        1. **Default Prediction**
           - Binary classification: Default/No Default
           - Features: Credit history, income, debt ratio
           - Model: Logistic Regression or Random Forest
           - Metric: Recall (catch defaults) + Precision
        
        2. **Credit Scoring**
           - Multi-class: Low/Medium/High risk
           - Probability of default (PD)
           - Expected loss calculation
           - Regulatory requirements (Basel)
        
        3. **Feature Importance**
           - Identify key risk drivers
           - Payment history most important
           - Income stability
           - Debt-to-income ratio
        
        4. **Model Monitoring**
           - Performance over time
           - Population drift
           - Regulatory compliance
           - Fairness considerations
        """)
    
    with tab2:
        st.markdown("""
        **Algorithmic Trading:**
        
        1. **Direction Prediction**
           - Up/Down classification
           - Features: Technical indicators, momentum
           - Challenge: Market efficiency
           - Success rate: 51-55% can be profitable
        
        2. **Return Forecasting**
           - Regression on returns
           - Factor models enhanced with ML
           - Ensemble methods
           - Combine with risk management
        
        3. **Regime Detection**
           - Classify market regimes
           - Bull/Bear/Sideways
           - Volatility regimes
           - Adapt strategy to regime
        
        4. **Feature Engineering**
           - Technical indicators
           - Sentiment scores
           - Order flow features
           - Alternative data integration
        """)
    
    with tab3:
        st.markdown("""
        **Fraud Detection:**
        
        1. **Transaction Classification**
           - Binary: Fraud or Legitimate
           - Real-time scoring
           - High precision needed (avoid false alarms)
           - High recall needed (catch fraud)
        
        2. **Anomaly Detection**
           - Unsupervised learning
           - Identify unusual patterns
           - Behavioral anomalies
           - Network analysis
        
        3. **Imbalanced Data**
           - Fraud is rare (< 1%)
           - Oversampling techniques
           - Cost-sensitive learning
           - Precision-Recall tradeoff
        
        4. **Continuous Learning**
           - Fraud patterns evolve
           - Model retraining
           - A/B testing
           - Feedback loops
        """)
    
    st.markdown("---")
    st.success("""
    **Ready for Module 10?**
    
    Module 10: Business Analytics Applications covers:
    - Customer analytics
    - Marketing analytics
    - Operational analytics
    - Business forecasting
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #b2dfdb; padding: 20px;'>
    <p><strong>Statistics for Finance Professionals</strong></p>
    <p>Module 9 of 12: Machine Learning for Finance</p>
</div>
""", unsafe_allow_html=True)