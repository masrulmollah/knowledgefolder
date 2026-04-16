import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
.hero-banner { background: linear-gradient(135deg, #1a1200 0%, #3d2c00 50%, #7a5500 100%); padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem; border-left: 6px solid #fbbf24; }
.hero-title { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 0 0 0.4rem 0; }
.hero-subtitle { font-size: 1.05rem; color: #fde68a; margin: 0; }
.hero-badge { display: inline-block; background: #fbbf24; color: #1a1200; font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.7rem; border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase; }
.progress-container { background: #e9ecef; border-radius: 20px; height: 10px; margin: 0.3rem 0 0.5rem 0; }
.progress-bar { background: linear-gradient(90deg, #fbbf24, #7a5500); height: 10px; border-radius: 20px; width: 75%; }
.progress-label { font-size: 0.78rem; color: #6c757d; margin-bottom: 0.2rem; }
.stat-card { background: white; border: 1px solid #dee2e6; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.stat-number { font-size: 1.8rem; font-weight: 800; color: #7a5500; }
.stat-label { font-size: 0.78rem; color: #6c757d; margin-top: 0.2rem; }
.finance-lens { background: linear-gradient(135deg, #fff3cd, #fff8e1); border: 1px solid #ffc107; border-left: 5px solid #f5a623; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.5rem 0; }
.finance-lens-title { font-size: 0.85rem; font-weight: 700; color: #856404; text-transform: uppercase; margin-bottom: 0.4rem; }
.finance-lens-body { font-size: 0.88rem; color: #5a4200; line-height: 1.6; }
.section-heading { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #fbbf24; padding-bottom: 0.3rem; margin: 1.5rem 0 1rem 0; }
.step-card { background: white; border: 1px solid #fde68a; border-left: 5px solid #fbbf24; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
.code-note { background: #1e1e1e; color: #d4d4d4; border-radius: 8px; padding: 1rem; font-family: monospace; font-size: 0.82rem; margin: 0.5rem 0; }
.quiz-box { background: #fffbeb; border: 1px solid #fde68a; border-radius: 12px; padding: 1.2rem 1.4rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">🟡 Module 6 of 8 &nbsp;|&nbsp; AI Series</div>
  <div class="hero-title">Building AI Models — A Practical Primer</div>
  <div class="hero-subtitle">Walk through the full ML pipeline step by step — from raw financial data
  to a deployed prediction model — using a cash flow forecasting example you can follow yourself.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-label">Series progress — Module 6 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="stat-card"><div class="stat-number">8</div><div class="stat-label">Pipeline Steps</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-card"><div class="stat-number">Python</div><div class="stat-label">Code Examples</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-card"><div class="stat-number">~40</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Quiz Questions</div></div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [("1","Foundations of AI",False),("2","Machine Learning Essentials",False),("3","Deep Learning & Neural Networks",False),("4","Generative AI & LLMs",False),("5","AI in Finance & Accounting",False),("6","Building AI Models",True),("7","AI Ethics, Risk & Governance",False),("8","Future of AI & Career Readiness",False)]
    for num, name, active in modules:
        st.markdown(f"**▶ M{num} — {name}** ✅" if active else f"M{num} — {name}")
    st.markdown("---")
    st.info("💡 M2 (Machine Learning) is essential background for this module.")

st.markdown('<div class="section-heading">🗺️ The ML Pipeline Overview</div>', unsafe_allow_html=True)
st.markdown("""
Building an ML model is a structured, iterative process — not a single step. Think of it as an
8-stage pipeline, each stage feeding into the next. We will walk through each stage using a
**working finance example: predicting which invoices will be paid late.**
""")
with st.expander("📋 The 8-Stage ML Pipeline at a Glance"):
    pipeline_steps = [
        ("1", "Problem Definition", "🎯", "Define what you are predicting, the success metric, and data requirements."),
        ("2", "Data Collection", "📦", "Gather historical data with known outcomes from source systems."),
        ("3", "Exploratory Data Analysis", "🔍", "Understand distributions, correlations, and data quality."),
        ("4", "Data Preprocessing", "🧹", "Clean missing values, encode categories, handle outliers."),
        ("5", "Feature Engineering", "⚙️", "Create informative input variables that help the model."),
        ("6", "Model Training & Selection", "🏋️", "Train multiple algorithms and compare performance."),
        ("7", "Model Evaluation", "📊", "Test on held-out data. Measure business-relevant metrics."),
        ("8", "Deployment & Monitoring", "🚀", "Integrate into production systems. Monitor performance over time."),
    ]
    for num, step, icon, desc in pipeline_steps:
        col1, col2 = st.columns([1, 4])
        with col1: st.markdown(f"**Step {num}** {icon}")
        with col2: st.markdown(f"**{step}** — {desc}")

# Step 1
st.markdown('<div class="section-heading">Step 1 — Problem Definition</div>', unsafe_allow_html=True)
with st.expander("🎯 Define the Problem Before Touching Data"):
    st.markdown("""
    The most important step — and the most commonly rushed. Poor problem definition leads to
    building a technically correct model that solves the wrong problem.

    **Questions to answer before starting:**

    | Question | Invoice Late Payment Example |
    |----------|------------------------------|
    | **What are we predicting?** | Whether an invoice will be paid more than 30 days after due date |
    | **What type of ML problem?** | Binary classification (late: yes/no) |
    | **What is the success metric?** | Recall ≥ 80% (catching 80%+ of actually late invoices) |
    | **What data do we need?** | Historical invoices with actual payment dates |
    | **Who uses the output?** | Collections team — to prioritise follow-up calls |
    | **What action does the output drive?** | Proactive outreach to high-risk invoices 2 weeks before due |
    | **What is the business value?** | Reduce DSO by 5 days = ~$2M freed cash for $150M revenue company |
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — The Right Success Metric</div>
      <div class="finance-lens-body">
        For a late payment model, <b>Recall</b> matters more than Accuracy. It is worse to miss a
        genuinely late invoice (false negative = cash not collected) than to flag a few that turn out
        to pay on time (false positive = an unnecessary call). Define this upfront with the business.
      </div>
    </div>
    """, unsafe_allow_html=True)

# Step 2
st.markdown('<div class="section-heading">Step 2 — Data Collection</div>', unsafe_allow_html=True)
with st.expander("📦 What Data Do You Need and Where to Get It"):
    st.markdown("""
    For our invoice late payment model, we need data from multiple finance systems:

    **Data sources:**
    - **ERP / Accounting System** (SAP, Oracle, Xero) → Invoice master data, customer master
    - **Accounts Receivable ledger** → Invoice amount, due date, actual payment date (our label)
    - **CRM** → Customer industry, relationship age, account manager
    - **External credit data** → Customer credit score, Dun & Bradstreet rating (optional)

    **Minimum viable dataset:**
    - At least 2–3 years of historical invoices
    - Both paid invoices (with actual payment dates) and currently open invoices
    - Target: 10,000+ records for reliable ML (more is better)
    - Balance: Aim for no worse than 80:20 on-time vs late (address imbalance if needed)

    **Data governance checklist:**
    - ✅ Do we have permission to use this data for ML?
    - ✅ Does it contain personal data requiring PDPA / GDPR compliance?
    - ✅ Is it stored securely? Should it leave the corporate environment?
    - ✅ Can we explain the model's use to customers if asked?
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Data Extraction</div>
      <div class="finance-lens-body">
        Most finance teams extract training data using SQL queries from their data warehouse or
        direct ERP extraction. Tools like Alteryx, Power Query, or Python (pandas + SQL connector)
        are commonly used to consolidate data from multiple source systems into a single model-ready dataset.
      </div>
    </div>
    """, unsafe_allow_html=True)

# Step 3
st.markdown('<div class="section-heading">Step 3 — Exploratory Data Analysis (EDA)</div>', unsafe_allow_html=True)
with st.expander("🔍 Understanding Your Data Before Modelling"):
    st.markdown("""
    Before modelling, explore your data to understand its structure, quality, and patterns.
    This often reveals data quality issues and feature ideas.

    **Key EDA steps:**
    - **Shape check** — How many rows and columns?
    - **Missing values** — Which columns have nulls? How many?
    - **Distribution** — Are numeric variables skewed? Any extreme outliers?
    - **Target variable balance** — What % are late invoices? (10%? 40%?)
    - **Correlations** — Which features correlate most with late payment?
    - **Time patterns** — Is late payment seasonal? Industry-specific?
    """)
    st.code("""
import pandas as pd
import matplotlib.pyplot as plt

# Load invoice data
df = pd.read_csv('invoices.csv')

# Basic checks
print(f"Rows: {len(df):,}, Columns: {df.shape[1]}")
print(df.dtypes)
print(df.isnull().sum())

# Target balance
print(df['is_late'].value_counts(normalize=True))
# Output: False 0.73 (73% paid on time), True 0.27 (27% late)

# Distribution of invoice amounts
df['invoice_amount'].hist(bins=50)
plt.title('Invoice Amount Distribution')
plt.show()

# Correlation with target
print(df.corr()['is_late'].sort_values(ascending=False))
""", language="python")
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — What EDA Often Reveals</div>
      <div class="finance-lens-body">
        Common findings in invoice data EDA: (1) Large invoices >$100K are paid later on average —
        customers delay large payments. (2) Certain industries (construction, government) have
        systematically longer payment cycles. (3) Invoices without PO numbers have higher late rates.
        (4) Month-end invoices are paid faster. These become features in Step 5.
      </div>
    </div>
    """, unsafe_allow_html=True)

# Step 4
st.markdown('<div class="section-heading">Step 4 — Data Preprocessing</div>', unsafe_allow_html=True)
with st.expander("🧹 Cleaning Data for Machine Learning"):
    st.markdown("""
    Raw financial data is rarely model-ready. Common preprocessing steps:

    **Missing values:**
    - Numerical: Fill with median (robust to outliers) or mean
    - Categorical: Fill with mode or create an 'Unknown' category
    - Flag missingness: Create binary column `payment_terms_missing` — missingness itself may predict late payment

    **Categorical encoding:**
    - Binary categories: 0/1 encoding (paid: 0, late: 1)
    - Multi-category (industry, country): One-Hot Encoding or Target Encoding

    **Outlier handling:**
    - Cap extreme values at 99th percentile (winsorization)
    - Or log-transform highly skewed amounts (invoice_amount → log_invoice_amount)

    **Feature scaling:**
    - Tree-based models (XGBoost, Random Forest) don't need scaling
    - Linear models and neural networks do: StandardScaler or MinMaxScaler
    """)
    st.code("""
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import numpy as np

# Handle missing values
df['payment_terms'].fillna('Unknown', inplace=True)
df['credit_limit'].fillna(df['credit_limit'].median(), inplace=True)

# Flag missingness
df['credit_score_missing'] = df['credit_score'].isna().astype(int)
df['credit_score'].fillna(df['credit_score'].median(), inplace=True)

# Log transform skewed amount
df['log_invoice_amount'] = np.log1p(df['invoice_amount'])

# One-hot encode industry
df = pd.get_dummies(df, columns=['customer_industry'], drop_first=True)

# Winsorise at 99th percentile
cap = df['days_outstanding'].quantile(0.99)
df['days_outstanding'] = df['days_outstanding'].clip(upper=cap)
""", language="python")

# Step 5
st.markdown('<div class="section-heading">Step 5 — Feature Engineering</div>', unsafe_allow_html=True)
with st.expander("⚙️ Creating Informative Input Variables"):
    st.markdown("""
    Feature engineering is often the difference between a mediocre and an excellent model.
    Domain knowledge — your finance expertise — drives the best features.

    **Types of features for invoice late payment model:**
    """)
    features = [
        ("📊 Invoice-level features", ["invoice_amount — larger invoices paid later on average", "invoice_age_at_due — days invoice outstanding at due date", "payment_terms_days — contractual payment terms (30/60/90)", "has_po_number — invoices without PO numbers pay later", "is_disputed — dispute flag on invoice", "invoice_month, invoice_quarter — seasonality"]),
        ("👤 Customer-level features", ["customer_avg_dso_12m — customer's average Days Sales Outstanding over past 12 months", "customer_late_rate_12m — % of their invoices paid late in last 12 months", "customer_credit_score — external credit bureau score", "customer_relationship_years — longer relationships pay more reliably", "customer_revenue_tier — bucketed annual spend with company"]),
        ("📈 Trend features", ["customer_dso_trend — is their DSO getting better or worse?", "industry_avg_dso — benchmark for their industry", "days_since_last_late — recency of last late payment", "consecutive_late_count — how many in a row have been late"]),
        ("🌍 Macro features (optional)", ["gdp_growth_rate — economic health at invoice date", "industry_pmi — purchasing managers index for customer industry", "interest_rate — cost of capital affecting payment behaviour"]),
    ]
    for category, items in features:
        st.markdown(f"**{category}**")
        for item in items: st.markdown(f"  - `{item}`")
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Your Domain Knowledge is an Asset</div>
      <div class="finance-lens-body">
        A finance professional building this model has a significant advantage over a pure data
        scientist: you know that government customers always pay slowly, that disputed invoices
        almost always pay late, and that month-end invoices get prioritised. These insights create
        features that dramatically improve model accuracy.
      </div>
    </div>
    """, unsafe_allow_html=True)

# Step 6
st.markdown('<div class="section-heading">Step 6 — Model Training & Selection</div>', unsafe_allow_html=True)
with st.expander("🏋️ Training and Comparing Models"):
    st.markdown("""
    **Train-test split:** Reserve 20–30% of data as a held-out test set. The model never sees this
    during training — it simulates predicting future invoices.

    **Cross-validation:** Split training data into K folds. Train on K-1 folds, validate on 1 fold.
    Repeat K times. Average performance gives a reliable estimate and detects overfitting.

    **Start simple, then iterate:**
    1. **Baseline** — Logistic Regression (simple, interpretable, establishes baseline)
    2. **Improved** — Random Forest (non-linear, handles interactions)
    3. **Best** — XGBoost (usually wins on tabular financial data)
    4. **Optional** — Neural Network (if >100K rows and complex patterns)
    """)
    st.code("""
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, classification_report

# Features and target
features = ['log_invoice_amount', 'payment_terms_days', 'customer_avg_dso_12m',
            'customer_late_rate_12m', 'has_po_number', 'customer_credit_score',
            'days_since_last_late', 'invoice_month']
X = df[features]
y = df['is_late']

# Train-test split (time-based for financial data!)
# Sort by invoice date first, then split — never random split on time series
df_sorted = df.sort_values('invoice_date')
split_idx = int(len(df_sorted) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

# Train and compare models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'XGBoost': XGBClassifier(n_estimators=100, random_state=42, eval_metric='logloss'),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred_proba)
    print(f"{name}: AUC = {auc:.3f}")

# Output example:
# Logistic Regression: AUC = 0.741
# Random Forest:       AUC = 0.813
# XGBoost:             AUC = 0.847  ← winner
""", language="python")
    st.warning("⚠️ **Critical for finance:** Always use a **time-based split** for financial data — train on older invoices, test on recent ones. Random splitting leaks future data into training, producing overly optimistic results.")

# Step 7
st.markdown('<div class="section-heading">Step 7 — Model Evaluation</div>', unsafe_allow_html=True)
with st.expander("📊 Measuring Business Value, Not Just Accuracy"):
    st.markdown("""
    **Evaluation metrics for the late payment classifier:**
    """)
    st.code("""
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import shap

# Best model: XGBoost
best_model = models['XGBoost']
y_pred = best_model.predict(X_test)
y_pred_proba = best_model.predict_proba(X_test)[:, 1]

# Classification report
print(classification_report(y_test, y_pred, target_names=['On-Time', 'Late']))
# Output:
#               precision    recall  f1-score
# On-Time           0.91      0.88      0.89
# Late              0.74      0.81      0.77  ← Recall 0.81 > our target of 0.80 ✅
# AUC-ROC: 0.847

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
# [[True Negatives, False Positives],
#  [False Negatives, True Positives]]

# Feature importance (what drives late payment?)
importance = pd.Series(best_model.feature_importances_, index=features)
importance.sort_values().plot(kind='barh', title='Feature Importance')

# SHAP values for explainability
explainer = shap.TreeExplainer(best_model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
""", language="python")
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Translate to Business Impact</div>
      <div class="finance-lens-body">
        <b>Recall of 0.81</b> means the model correctly identifies 81% of invoices that will be late.
        For a company with 500 late invoices per month averaging $15K each: catching 81% = 405 invoices
        flagged early = potential ~$6M in accelerated collections per month. <b>This is how you
        justify AI investment to the CFO.</b>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Step 8
st.markdown('<div class="section-heading">Step 8 — Deployment & Monitoring</div>', unsafe_allow_html=True)
with st.expander("🚀 Taking Your Model to Production"):
    st.markdown("""
    Building a good model is only half the work — deploying and maintaining it is the other half.

    **Deployment options for finance teams:**
    """)
    tab1, tab2, tab3 = st.tabs(["🐍 Python Script / Batch", "🔌 API / Integration", "📊 No-Code / AutoML"])
    with tab1:
        st.markdown("""
        **Simplest option — daily batch scoring**
        - Extract new invoices from ERP each morning
        - Run prediction script → assign risk score to each invoice
        - Write scores back to ERP or export to Excel/CSV
        - Collections team reviews high-risk invoices daily
        """)
        st.code("""
import joblib
import pandas as pd

# Save trained model
joblib.dump(best_model, 'invoice_late_model.pkl')

# Daily scoring script
def score_new_invoices(new_invoices_df):
    model = joblib.load('invoice_late_model.pkl')
    features = ['log_invoice_amount', 'payment_terms_days', ...]
    scores = model.predict_proba(new_invoices_df[features])[:, 1]
    new_invoices_df['late_payment_risk'] = scores
    new_invoices_df['risk_tier'] = pd.cut(scores,
        bins=[0, 0.3, 0.6, 1.0],
        labels=['Low', 'Medium', 'High'])
    return new_invoices_df
""", language="python")
    with tab2:
        st.markdown("""
        **For real-time integration with ERP / collections tools**
        - Wrap model in a FastAPI or Flask REST API
        - ERP calls API with new invoice data
        - API returns risk score in real-time (< 100ms)
        - Score displayed in ERP for collectors
        """)
        st.code("""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib, numpy as np

app = FastAPI()
model = joblib.load('invoice_late_model.pkl')

class Invoice(BaseModel):
    invoice_amount: float
    payment_terms_days: int
    customer_avg_dso_12m: float
    customer_late_rate_12m: float
    has_po_number: int

@app.post("/score")
def score_invoice(invoice: Invoice):
    features = [[
        np.log1p(invoice.invoice_amount),
        invoice.payment_terms_days,
        invoice.customer_avg_dso_12m,
        invoice.customer_late_rate_12m,
        invoice.has_po_number,
    ]]
    prob = model.predict_proba(features)[0][1]
    tier = "High" if prob > 0.6 else "Medium" if prob > 0.3 else "Low"
    return {"late_payment_probability": round(prob, 3), "risk_tier": tier}
""", language="python")
    with tab3:
        st.markdown("""
        **No-Code and Low-Code AutoML options — no Python required**

        | Tool | Best for | Finance accessibility |
        |------|----------|----------------------|
        | **Microsoft Azure AutoML** | Enterprise, Azure cloud | Medium — needs IT |
        | **Google AutoML Tables** | Tabular finance data | Medium — needs GCP |
        | **Alteryx Auto Insights** | Finance analysts | High — drag and drop |
        | **DataRobot** | Enterprise ML at scale | Medium — needs setup |
        | **KNIME** | Open source, visual workflow | High — no coding |
        | **H2O AutoML** | Fast model comparison | Medium — needs setup |

        These tools handle preprocessing, feature selection, model comparison, and deployment
        automatically — ideal for finance teams without dedicated data science resources.
        """)

    st.markdown("""
    **Monitoring — the ongoing responsibility:**
    - 📉 **Performance drift** — check monthly: is AUC/Recall still meeting target?
    - 📊 **Data drift** — are input feature distributions changing? (new customer types, new markets)
    - ⚠️ **Model retraining trigger** — if AUC drops below 0.80, retrain on recent data
    - 📋 **Model governance log** — document version, training date, test results, sign-off
    """)

# Quiz
st.markdown('<div class="section-heading">🧩 Knowledge Check</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {"q": "When building an ML model to predict invoice late payments using 3 years of historical data, what is the MOST appropriate way to split data for training and testing?", "options": ["Random 80/20 split", "Use first year for test, remaining for training", "Train on older invoices, test on the most recent data (time-based split)", "Use all data for training to maximise model accuracy"], "answer": "Train on older invoices, test on the most recent data (time-based split)", "explanation": "Financial data is time-series — a random split would leak future data into training, creating unrealistically good results. Time-based splits simulate real-world deployment where you predict future from past."},
    {"q": "A finance analyst notices that in the training data, only 8% of invoices are late. This could cause:", "options": ["Overfitting to the majority class — the model may simply predict 'on-time' for everything", "Underfitting due to too little data", "The model to require more features", "No issues — 8% is ideal for ML"], "answer": "Overfitting to the majority class — the model may simply predict 'on-time' for everything", "explanation": "Class imbalance is common in fraud and late payment data. A model predicting 'on-time' for everything achieves 92% accuracy but has 0% recall on the minority class — useless. Techniques like SMOTE, class weighting, or threshold adjustment address this."},
    {"q": "Which of the following is an example of feature engineering using finance domain knowledge?", "options": ["Splitting data into train and test sets", "Creating a 'customer_late_rate_12m' variable from historical payment records", "Choosing XGBoost over Logistic Regression", "Setting the learning rate to 0.01"], "answer": "Creating a 'customer_late_rate_12m' variable from historical payment records", "explanation": "Feature engineering transforms raw data into informative inputs. 'Customer 12-month late rate' is a domain-knowledge-driven feature that directly encodes payment behaviour history — a powerful predictor."},
    {"q": "After deployment, the invoice late payment model's AUC drops from 0.847 to 0.71 over 6 months. The MOST likely cause is:", "options": ["The model was deleted from the server", "Distribution shift — customer or economic conditions have changed", "The model was always wrong", "XGBoost is not suitable for finance"], "answer": "Distribution shift — customer or economic conditions have changed", "explanation": "Model performance degrades over time as the real world changes — new customer segments, economic cycles, business model changes. This is 'distribution shift' and requires monitoring and periodic retraining."},
    {"q": "A finance manager wants to deploy an ML model but cannot code in Python. Which is the MOST appropriate no-code option?", "options": ["Writing the model in Excel VLOOKUP formulas", "Using Alteryx or KNIME for a visual, drag-and-drop ML workflow", "Hiring a team of data scientists", "Using only rule-based systems instead"], "answer": "Using Alteryx or KNIME for a visual, drag-and-drop ML workflow", "explanation": "Tools like Alteryx, KNIME, and Azure AutoML provide visual, no-code interfaces for the full ML pipeline — accessible to finance analysts without Python expertise."},
]

for key in ["m6_q_index","m6_score","m6_answered","m6_selected","m6_quiz_done"]:
    if key not in st.session_state: st.session_state[key] = 0 if "index" in key or "score" in key else False

if not st.session_state.m6_quiz_done:
    q_data = questions[st.session_state.m6_q_index]
    st.markdown(f"**Question {st.session_state.m6_q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")
    choice = st.radio("Select your answer:", q_data["options"], key=f"m6_q_{st.session_state.m6_q_index}")
    col_s, col_n = st.columns(2)
    with col_s:
        if st.button("✅ Submit", key=f"m6_sub_{st.session_state.m6_q_index}"):
            st.session_state.m6_answered = True; st.session_state.m6_selected = choice
            if choice == q_data["answer"]: st.session_state.m6_score += 1
    if st.session_state.m6_answered:
        if st.session_state.m6_selected == q_data["answer"]: st.success(f"✅ Correct! {q_data['explanation']}")
        else: st.error(f"❌ Answer: **{q_data['answer']}** — {q_data['explanation']}")
        with col_n:
            if st.session_state.m6_q_index < len(questions)-1:
                if st.button("Next ➡️", key=f"m6_next_{st.session_state.m6_q_index}"):
                    st.session_state.m6_q_index += 1; st.session_state.m6_answered = False; st.rerun()
            else:
                if st.button("🏁 Results"): st.session_state.m6_quiz_done = True; st.rerun()
else:
    s,t = st.session_state.m6_score, len(questions); pct = int((s/t)*100)
    st.markdown(f"### {'🏆' if pct>=80 else '👍' if pct>=60 else '📚'} Score: {s}/{t} ({pct}%)")
    st.progress(pct/100)
    st.info("Excellent!" if pct>=80 else "Good — review the pipeline steps." if pct>=60 else "Revisit the ML pipeline and re-attempt.")
    if st.button("🔄 Retry"):
        for k,v in [("m6_q_index",0),("m6_score",0),("m6_answered",False),("m6_selected",None),("m6_quiz_done",False)]: st.session_state[k]=v
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">💡 Key Takeaways</div>', unsafe_allow_html=True)
for i,t in enumerate(["The ML pipeline has 8 stages: problem definition, data collection, EDA, preprocessing, feature engineering, training, evaluation, deployment & monitoring.","**Always use time-based splits** for financial data — random splits leak future data and produce unrealistically optimistic results.","**Feature engineering** using finance domain knowledge often provides more value than choosing a fancier algorithm — your expertise is an asset.","**XGBoost** is the industry standard for tabular financial data — it consistently outperforms alternatives on structured finance datasets.","**Monitoring and retraining** are ongoing responsibilities — models degrade as conditions change and must be maintained like any financial system.","**No-code tools** (Alteryx, KNIME, Azure AutoML) make the ML pipeline accessible to finance analysts without Python expertise."],1):
    st.markdown(f"**{i}.** {t}")

st.markdown("---")
col1,col2,col3 = st.columns(3)
with col1:
    if st.button("⬅️ M5: AI in Finance", use_container_width=True): st.info("Navigate to Module 5 from the sidebar.")
with col2: st.markdown("<div style='text-align:center;padding-top:0.4rem'>🟡 Module 6 of 8</div>", unsafe_allow_html=True)
with col3:
    if st.button("M7: Ethics & Governance ➡️", use_container_width=True): st.info("Navigate to Module 7 from the sidebar.")
st.caption("Knowledge Folder · AI Series · Module 6 — Building AI Models · © 2025")