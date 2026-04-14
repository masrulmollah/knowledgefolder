"""
Machine Learning for Finance & Accounts
Module 8 – Building Your First ML Model

USAGE: import ml_module_08; ml_module_08.show()
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#1E3A5F"; SECONDARY="#3B82F6"; SUCCESS="#10B981"; WARNING="#F59E0B"; DANGER="#EF4444"


def _css():
    st.markdown("""
    <style>
    .main { background:#F0F9FF; }
    .hero-banner { background:linear-gradient(135deg,#1E3A5F 0%,#1D4ED8 60%,#7C3AED 100%);
        border-radius:16px; padding:2.4rem 2.8rem; color:white; margin-bottom:1.6rem; }
    .hero-banner h1 { font-size:2.1rem; margin:0 0 .4rem; font-weight:700; }
    .hero-banner p  { font-size:1.05rem; margin:0; opacity:.9; }
    .hero-badge { display:inline-block; background:rgba(255,255,255,.2);
        border:1px solid rgba(255,255,255,.35); border-radius:20px;
        padding:.18rem .8rem; font-size:.8rem; margin-bottom:.7rem; }
    .section-title { font-size:1.35rem; font-weight:700; color:#1E293B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #1E3A5F; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .info-card .card-icon { font-size:1.7rem; margin-bottom:.4rem; }
    .info-card h4 { font-size:1rem; font-weight:700; color:#1E293B; margin:0 0 .3rem; }
    .info-card p  { font-size:.88rem; color:#475569; margin:0; line-height:1.55; }
    .definition-box { background:#DBEAFE; border-left:5px solid #1E3A5F;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    .definition-box p { margin:0; color:#1E293B; font-size:.96rem; line-height:1.65; }
    .code-block { background:#1E293B; color:#E2E8F0; border-radius:10px;
        padding:1.2rem 1.5rem; font-family:"Courier New",monospace; font-size:.85rem;
        line-height:1.7; overflow-x:auto; margin:1rem 0; }
    .code-comment { color:#64748B; }
    .code-keyword { color:#93C5FD; }
    .code-string { color:#86EFAC; }
    .code-function { color:#FCD34D; }
    .step-badge { display:inline-flex; align-items:center; justify-content:center;
        width:32px; height:32px; border-radius:50%; background:#1E3A5F;
        color:white; font-weight:700; font-size:.9rem; margin-right:.5rem; }
    .quiz-box { background:white; border-radius:12px; padding:1.4rem 1.6rem;
        box-shadow:0 2px 10px rgba(0,0,0,.08); margin-top:1rem; }
    .quiz-q { font-weight:700; color:#1E293B; font-size:1rem; margin-bottom:.8rem; }
    </style>""", unsafe_allow_html=True)


def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 8 — Building Your First ML Model</h1>
      <p>Step-by-step: build a late payment prediction model for accounts receivable
         using Python, pandas, and scikit-learn. No prior coding experience required.</p>
    </div>""", unsafe_allow_html=True)
    for col,(icon,label,val) in zip(st.columns(4),[
        ("🛠️","Level","Hands-on / Practical"),("⏱️","Read time","~45 minutes"),
        ("💻","Tools","Python, pandas, sklearn"),("🏆","Outcome","Build & run an ML model"),
    ]):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""", unsafe_allow_html=True)


def _section_tools():
    st.markdown('<div class="section-title">🛠️ 1. Your ML Toolkit</div>', unsafe_allow_html=True)

    tools = [
        ("🐍","Python","The language of ML. Free, beginner-friendly. Think of it as a more powerful Excel macro language."),
        ("🐼","pandas","The spreadsheet library. Manipulate data tables in Python — like Excel formulas but far more powerful."),
        ("🔢","NumPy","Mathematical operations on arrays and matrices — the backbone of all ML calculations."),
        ("🤖","scikit-learn","The ML library. Contains ready-made algorithms: Random Forest, XGBoost, Linear Regression — just a few lines of code."),
        ("📊","Matplotlib/Plotly","Visualisation. Create charts, model diagnostics, and dashboards."),
        ("☁️","No-Code Options","Excel ML add-ins, Google AutoML, Microsoft Azure ML Studio — for finance pros who prefer no coding."),
    ]
    cols = st.columns(3)
    for i, (icon, name, desc) in enumerate(tools):
        with cols[i%3]:
            st.markdown(f"""<div class="info-card" style="margin-bottom:1rem">
              <div class="card-icon">{icon}</div>
              <h4>{name}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    st.markdown("#### 📦 Install everything you need — one command")
    st.code("pip install pandas numpy scikit-learn plotly streamlit xgboost", language="bash")


def _section_problem_definition():
    st.markdown('<div class="section-title">🎯 2. Step 1 — Define the Problem</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Our project:</strong> Build a model that predicts whether an invoice will be
      paid late — <em>before</em> the due date — so the collections team can act proactively.
      This is a <strong>binary classification</strong> problem: "Late" or "On Time".</p>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **Input features (what we know at invoice creation):**
        - Customer's historical average payment delay (days)
        - Invoice amount
        - Payment terms (Net 30, Net 60, etc.)
        - Customer industry
        - Month of invoice (seasonality)
        - Number of previous late payments
        - Customer credit score

        **Target variable (what we want to predict):**
        - `is_late` = 1 if payment came after due date, 0 otherwise
        """)
    with c2:
        st.markdown("""
        **Success metrics we'll use:**
        | Metric | What it measures |
        |--------|-----------------|
        | Accuracy | % of all predictions correct |
        | Precision | Of predicted 'late', how many were really late? |
        | Recall | Of actual 'late' invoices, how many did we catch? |
        | AUC-ROC | Overall model discrimination ability |
        | F1 Score | Balance of precision and recall |

        > **Finance tip:** In collections, **recall** matters most — you'd rather
        flag some false alarms than miss a real late payer.
        """)


def _section_generate_data():
    st.markdown('<div class="section-title">📊 3. Step 2 — Create & Explore the Dataset</div>', unsafe_allow_html=True)
    st.markdown("In practice you'd load real data from your ERP/accounting system. Here we generate realistic synthetic data:")

    st.code("""import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

# Generate realistic invoice dataset
df = pd.DataFrame({
    'customer_avg_delay': np.random.gamma(3, 5, n),        # past avg days late
    'invoice_amount':     np.random.lognormal(8, 1.2, n),  # invoice value
    'payment_terms':      np.random.choice([30, 60, 90], n, p=[0.6, 0.3, 0.1]),
    'industry':           np.random.choice(['Retail','Manufacturing','Services','Tech'], n),
    'invoice_month':      np.random.randint(1, 13, n),
    'prior_late_count':   np.random.poisson(1.5, n),
    'credit_score':       np.random.normal(650, 80, n).clip(300, 850),
})

# Create target: late payment (1) or on time (0)
df['is_late'] = ((df['customer_avg_delay'] > 10) |
                 (df['invoice_amount'] > 50000) |
                 (df['prior_late_count'] > 3)).astype(int)

print(df.head())
print(f"Late rate: {df['is_late'].mean():.1%}")""", language="python")

    # Actually generate the data for display
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        'customer_avg_delay': np.random.gamma(3, 5, n),
        'invoice_amount': np.random.lognormal(8, 1.2, n),
        'payment_terms': np.random.choice([30, 60, 90], n, p=[0.6, 0.3, 0.1]),
        'industry': np.random.choice(['Retail','Manufacturing','Services','Tech'], n),
        'invoice_month': np.random.randint(1, 13, n),
        'prior_late_count': np.random.poisson(1.5, n),
        'credit_score': np.random.normal(650, 80, n).clip(300, 850),
    })
    df['is_late'] = ((df['customer_avg_delay'] > 10) |
                     (df['invoice_amount'] > 50000) |
                     (df['prior_late_count'] > 3)).astype(int)

    st.markdown("**Preview of generated dataset:**")
    st.dataframe(df.head(10).round(2), use_container_width=True, hide_index=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total invoices", f"{len(df):,}")
    col2.metric("Late payments", f"{df['is_late'].sum():,} ({df['is_late'].mean():.0%})")
    col3.metric("Features", f"{len(df.columns)-1}")
    return df


def _section_train_model(df):
    st.markdown('<div class="section-title">🤖 4. Step 3–4 — Preprocess, Train & Evaluate</div>', unsafe_allow_html=True)

    st.code("""from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, roc_auc_score

# Step 3a: Encode categorical features
df['industry_code'] = LabelEncoder().fit_transform(df['industry'])

# Step 3b: Define features and target
features = ['customer_avg_delay','invoice_amount','payment_terms',
            'industry_code','invoice_month','prior_late_count','credit_score']
X = df[features]
y = df['is_late']

# Step 3c: Split into train/test (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Step 4: Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]
print(classification_report(y_test, y_pred))
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob):.3f}")""", language="python")

    # Simulate results
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder
    from sklearn.metrics import roc_auc_score, confusion_matrix

    df2 = df.copy()
    df2['industry_code'] = LabelEncoder().fit_transform(df2['industry'])
    features = ['customer_avg_delay','invoice_amount','payment_terms',
                'industry_code','invoice_month','prior_late_count','credit_score']
    X = df2[features]; y = df2['is_late']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)
    cm = confusion_matrix(y_test, y_pred)
    accuracy = (cm[0,0]+cm[1,1]) / cm.sum()
    precision = cm[1,1] / (cm[1,1]+cm[0,1]) if (cm[1,1]+cm[0,1]) > 0 else 0
    recall = cm[1,1] / (cm[1,1]+cm[1,0]) if (cm[1,1]+cm[1,0]) > 0 else 0

    st.markdown("#### 📊 Model results")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Accuracy", f"{accuracy:.1%}")
    m2.metric("Precision", f"{precision:.1%}")
    m3.metric("Recall", f"{recall:.1%}")
    m4.metric("AUC-ROC", f"{auc:.3f}")

    col1, col2 = st.columns(2)
    with col1:
        fig_cm = go.Figure(go.Heatmap(
            z=cm, x=["Predicted: On Time","Predicted: Late"],
            y=["Actual: On Time","Actual: Late"],
            colorscale=[[0,"#ECFDF5"],[1,"#065F46"]],
            text=cm, texttemplate="%{text}", textfont={"size":18},
        ))
        fig_cm.update_layout(title="Confusion Matrix", height=260,
                              paper_bgcolor="rgba(0,0,0,0)", margin=dict(t=35,b=10,l=10,r=10))
        st.plotly_chart(fig_cm, use_container_width=True)

    with col2:
        importances = model.feature_importances_
        fig_fi = px.bar(x=importances, y=features, orientation="h",
                        title="Feature Importance",
                        color=importances, color_continuous_scale=["#DBEAFE","#1E3A5F"])
        fig_fi.update_layout(height=260, paper_bgcolor="rgba(0,0,0,0)",
                              plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=35,b=10,l=10,r=10),
                              coloraxis_showscale=False)
        st.plotly_chart(fig_fi, use_container_width=True)

    return model, X_test, y_test, y_prob


def _section_predict(model, X_test, y_test, y_prob):
    st.markdown('<div class="section-title">🔮 5. Step 5 — Make Predictions on New Invoices</div>', unsafe_allow_html=True)

    st.code("""# Predict on a new invoice
new_invoice = pd.DataFrame([{
    'customer_avg_delay': 18,      # customer usually pays 18 days late
    'invoice_amount': 85000,       # large invoice
    'payment_terms': 30,
    'industry_code': 2,            # Services
    'invoice_month': 12,           # December (busy month)
    'prior_late_count': 4,         # 4 previous late payments
    'credit_score': 580,           # below-average credit
}])

probability_late = model.predict_proba(new_invoice)[0][1]
print(f"Probability of late payment: {probability_late:.1%}")
# Output: Probability of late payment: 94.3%""", language="python")

    st.markdown("#### 🎛️ Try it yourself — configure a new invoice")
    col1, col2, col3 = st.columns(3)
    with col1:
        avg_delay = st.slider("Customer avg past delay (days)", 0, 60, 18)
        amount = st.number_input("Invoice amount ($)", 1000, 500000, 85000, 1000)
    with col2:
        prior_late = st.slider("Prior late payments", 0, 10, 4)
        credit = st.slider("Customer credit score", 300, 850, 580)
    with col3:
        terms = st.selectbox("Payment terms", [30, 60, 90])
        month = st.selectbox("Invoice month", list(range(1,13)),
                             format_func=lambda m: ["Jan","Feb","Mar","Apr","May","Jun",
                                                    "Jul","Aug","Sep","Oct","Nov","Dec"][m-1])

    if model is not None:
        lenc = LabelEncoder()
        lenc.classes_ = np.array(['Manufacturing','Retail','Services','Tech'])
        new_inv = pd.DataFrame([{
            'customer_avg_delay': avg_delay, 'invoice_amount': amount,
            'payment_terms': terms, 'industry_code': 2,
            'invoice_month': month, 'prior_late_count': prior_late, 'credit_score': credit,
        }])
        prob = model.predict_proba(new_inv[['customer_avg_delay','invoice_amount','payment_terms',
                                            'industry_code','invoice_month','prior_late_count','credit_score']])[0][1]
        if prob > 0.7: action, colour = "🚨 HIGH RISK — Call customer immediately", DANGER
        elif prob > 0.4: action, colour = "⚠️ MEDIUM RISK — Send proactive reminder", WARNING
        else: action, colour = "✅ LOW RISK — No action needed", SUCCESS

        st.markdown(f"""
        <div style="background:{colour}22;border:2px solid {colour};border-radius:12px;
             padding:1.2rem 1.5rem;margin-top:1rem;text-align:center">
          <h2 style="color:{colour};margin:0">{prob:.1%}</h2>
          <p style="color:{colour};font-weight:700;margin:.3rem 0">{action}</p>
        </div>""", unsafe_allow_html=True)


def _section_no_code():
    st.markdown('<div class="section-title">☁️ 6. No-Code ML Options for Finance Professionals</div>', unsafe_allow_html=True)
    tools = [
        ("📊","Excel + Azure ML Add-in","Upload data, choose algorithm, get predictions — no code. Best for: existing Excel workflows.","Beginner"),
        ("🔵","Microsoft Power BI","Built-in AutoML for forecasting and classification. Integrates with your existing BI setup.","Beginner"),
        ("🤖","Google AutoML / Vertex AI","Enterprise-grade AutoML. Upload CSV, it trains, evaluates and deploys automatically.","Intermediate"),
        ("🟠","AWS SageMaker Canvas","Drag-and-drop ML model builder. Very powerful, point-and-click interface.","Intermediate"),
        ("📗","DataRobot","Purpose-built AutoML platform used by many banks and insurers. Includes explainability.","Intermediate"),
        ("🐍","Streamlit (this app!)","Build your own interactive ML apps with minimal Python code. Great for sharing models.","Intermediate"),
    ]
    for i in range(0, len(tools), 3):
        cols = st.columns(3)
        for col,(icon,name,desc,level) in zip(cols, tools[i:i+3]):
            lc = SUCCESS if level=="Beginner" else WARNING
            col.markdown(f"""<div class="info-card" style="margin-bottom:1rem">
              <div class="card-icon">{icon}</div>
              <h4>{name}</h4><p>{desc}</p>
              <p style="font-size:.78rem;background:{lc}22;color:{lc};
                 border-radius:4px;padding:.1rem .4rem;display:inline-block;
                 margin-top:.4rem">Level: {level}</p></div>""", unsafe_allow_html=True)


def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 8 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q":"Q1. In scikit-learn, which function splits your dataset into training and test sets?",
         "opts":["model.fit()","train_test_split()","predict_proba()","LabelEncoder()"],
         "ans":"train_test_split()",
         "exp":"✅ Correct! `train_test_split()` from sklearn.model_selection splits data into train and test portions."},
        {"q":"Q2. A model has 95% accuracy on training data but only 62% on test data. What is this called?",
         "opts":["Underfitting","Overfitting","Class imbalance","Data leakage"],
         "ans":"Overfitting",
         "exp":"✅ Correct! When a model performs much better on training data than test data, it has memorised the training set — this is overfitting."},
        {"q":"Q3. For a collections team, which metric is most important when evaluating a late payment prediction model?",
         "opts":["Accuracy","Precision","Recall","Processing speed"],
         "ans":"Recall",
         "exp":"✅ Correct! Recall measures how many actual late payments we caught. Missing a late payer (false negative) is more costly than a false alarm in collections."},
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("", q["opts"], key=f"mod8_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"❌ Correct answer: **{q['ans']}**\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True); st.markdown("")


def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 ML for Finance & Accounts** · Module 8 of 10")
    c2.markdown("<div style='text-align:center'><a href='?module=7' style='color:#1E3A5F'>◀ Module 7</a>"
                " &nbsp;|&nbsp; <a href='?module=9' style='color:#1E3A5F'>Module 9 ▶</a></div>",
                unsafe_allow_html=True)
    c3.markdown("<div style='text-align:right;color:#64748B;font-size:.85rem'>Knowledge Folder</div>",
                unsafe_allow_html=True)


def show():
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 8 — Sections")
        st.markdown("1. ML Toolkit\n2. Define the Problem\n3. Generate & Explore Data\n"
                    "4. Train & Evaluate\n5. Make Predictions\n6. No-Code Options\n---\n🧩 Quiz")
        st.progress(80, text="Module 8 / 10")
    _section_tools(); st.markdown("")
    _section_problem_definition(); st.markdown("")
    df = _section_generate_data(); st.markdown("")
    model, X_test, y_test, y_prob = _section_train_model(df); st.markdown("")
    _section_predict(model, X_test, y_test, y_prob); st.markdown("")
    _section_no_code(); st.markdown("")
    _knowledge_check(); _footer()


if __name__ == "__main__":
    st.set_page_config(page_title="Module 8 – Building Your First ML Model | Knowledge Folder",
                       page_icon="🛠️", layout="wide")
    show()