import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
.hero-banner {
    background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 50%, #415a77 100%);
    padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;
    border-left: 6px solid #778da9;
}
.hero-title { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 0 0 0.4rem 0; }
.hero-subtitle { font-size: 1.05rem; color: #a8b2d8; margin: 0; }
.hero-badge {
    display: inline-block; background: #778da9; color: white;
    font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.7rem;
    border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase;
}
.progress-container { background: #e9ecef; border-radius: 20px; height: 10px; margin: 0.3rem 0 0.5rem 0; }
.progress-bar { background: linear-gradient(90deg, #778da9, #415a77); height: 10px; border-radius: 20px; width: 25%; }
.progress-label { font-size: 0.78rem; color: #6c757d; margin-bottom: 0.2rem; }
.stat-card { background: white; border: 1px solid #dee2e6; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.stat-number { font-size: 1.8rem; font-weight: 800; color: #415a77; }
.stat-label { font-size: 0.78rem; color: #6c757d; margin-top: 0.2rem; }
.topic-card { background: #f8f9fa; border: 1px solid #e9ecef; border-left: 4px solid #415a77; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
.topic-card-title { font-size: 0.95rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.3rem; }
.finance-lens { background: linear-gradient(135deg, #fff3cd, #fff8e1); border: 1px solid #ffc107; border-left: 5px solid #f5a623; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.5rem 0; }
.finance-lens-title { font-size: 0.85rem; font-weight: 700; color: #856404; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; }
.finance-lens-body { font-size: 0.88rem; color: #5a4200; line-height: 1.6; }
.section-heading { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #415a77; padding-bottom: 0.3rem; margin: 1.5rem 0 1rem 0; }
.algo-card { background: #eef2ff; border: 1px solid #c5d0f5; border-radius: 10px; padding: 1rem; margin-bottom: 0.6rem; }
.quiz-box { background: #f0f4ff; border: 1px solid #c5d0f5; border-radius: 12px; padding: 1.2rem 1.4rem; }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">📗 Module 2 of 8 &nbsp;|&nbsp; AI Series</div>
  <div class="hero-title">Machine Learning Essentials</div>
  <div class="hero-subtitle">Understand how machines learn from data — supervised, unsupervised,
  and reinforcement learning — and how these power the financial models you work with every day.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-label">Series progress — Module 2 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown('<div class="stat-card"><div class="stat-number">3</div><div class="stat-label">Learning Types</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-card"><div class="stat-number">8+</div><div class="stat-label">Key Algorithms</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-card"><div class="stat-number">~30</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Quiz Questions</div></div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [("1","Foundations of AI",False),("2","Machine Learning Essentials",True),("3","Deep Learning & Neural Networks",False),("4","Generative AI & LLMs",False),("5","AI in Finance & Accounting",False),("6","Building AI Models",False),("7","AI Ethics, Risk & Governance",False),("8","Future of AI & Career Readiness",False)]
    for num, name, active in modules:
        st.markdown(f"**▶ M{num} — {name}** ✅" if active else f"M{num} — {name}")
    st.markdown("---")
    st.info("💡 Complete M1 first for best understanding.")

# Topic 1
st.markdown('<div class="section-heading">🤖 What is Machine Learning?</div>', unsafe_allow_html=True)
with st.expander("📖 Definition & Core Concept", expanded=True):
    st.markdown("""
    **Machine Learning (ML)** is a subset of AI where systems **learn from data** to make predictions
    or decisions — without being explicitly programmed for each scenario.

    The classic ML loop:
    1. **Feed data** → historical examples with known outcomes
    2. **Algorithm learns** → finds patterns linking inputs to outputs
    3. **Model is built** → a mathematical function capturing those patterns
    4. **Model predicts** → applies learned patterns to new, unseen data
    5. **Feedback loop** → model improves as more data arrives

    > *"A computer program is said to learn from experience E with respect to task T and performance
    measure P, if its performance at T improves with experience E."* — Tom Mitchell, 1997
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        A credit scoring model is trained on thousands of historical loan applications (inputs: income,
        debt, payment history) with known outcomes (repaid vs defaulted). It learns the pattern linking
        applicant characteristics to repayment probability — then applies it to new applicants instantly.
      </div>
    </div>
    """, unsafe_allow_html=True)

# Topic 2
st.markdown('<div class="section-heading">🗂️ The Three Types of Machine Learning</div>', unsafe_allow_html=True)
with st.expander("1️⃣ Supervised Learning — Learning with Labels"):
    st.markdown("""
    The most widely used form of ML. The algorithm is trained on **labelled data** — examples where
    the correct answer is already known.

    **How it works:** Input features (X) + Known output/label (Y) → Model learns the mapping X → Y

    **Two main tasks:**
    - **Regression** → Predict a continuous number (e.g. next quarter's revenue)
    - **Classification** → Predict a category (e.g. fraud vs not fraud, creditworthy vs not)

    **Common algorithms:** Linear Regression, Logistic Regression, Decision Trees,
    Random Forest, Gradient Boosting (XGBoost), Support Vector Machines, Neural Networks
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Supervised Learning Use Cases</div>
      <div class="finance-lens-body">
        <b>Credit scoring</b> (classification) · <b>Fraud detection</b> (classification) ·
        <b>Revenue forecasting</b> (regression) · <b>Churn prediction</b> (classification) ·
        <b>Loan default probability</b> (regression) · <b>Expense anomaly detection</b> (classification)
      </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("2️⃣ Unsupervised Learning — Finding Hidden Patterns"):
    st.markdown("""
    The algorithm is trained on **unlabelled data** — no correct answers are provided.
    The model discovers hidden structure, groupings, or patterns on its own.

    **Main tasks:**
    - **Clustering** → Group similar data points together (e.g. customer segmentation)
    - **Dimensionality Reduction** → Compress data while preserving key patterns (e.g. PCA)
    - **Anomaly Detection** → Identify data points that don't fit any cluster

    **Common algorithms:** K-Means Clustering, DBSCAN, Principal Component Analysis (PCA),
    Autoencoders, Isolation Forest
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Unsupervised Learning Use Cases</div>
      <div class="finance-lens-body">
        <b>Customer segmentation</b> for targeted products · <b>Journal entry anomaly detection</b>
        in audit (no label needed — outliers stand out) · <b>Market regime detection</b> in investment
        management · <b>Expense pattern clustering</b> to identify cost optimisation opportunities
      </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("3️⃣ Reinforcement Learning — Learning by Trial and Error"):
    st.markdown("""
    The algorithm (called an **agent**) learns by interacting with an environment. It takes actions,
    receives **rewards** (for good outcomes) or **penalties** (for bad outcomes), and gradually
    learns the optimal strategy to maximise cumulative reward.

    **Key components:**
    - **Agent** → the model making decisions
    - **Environment** → the system the agent interacts with
    - **State** → current situation
    - **Action** → what the agent does
    - **Reward** → feedback signal (+ve or -ve)

    **Famous examples:** AlphaGo (board games), self-driving car steering, ChatGPT fine-tuning (RLHF)
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Reinforcement Learning Use Cases</div>
      <div class="finance-lens-body">
        <b>Algorithmic trading</b> — agent learns optimal buy/sell timing ·
        <b>Portfolio optimisation</b> — agent maximises risk-adjusted return ·
        <b>Dynamic pricing</b> — agent learns optimal pricing strategy ·
        <b>Order execution</b> — minimising market impact of large trades
      </div>
    </div>
    """, unsafe_allow_html=True)

# Topic 3 - Comparison
st.markdown('<div class="section-heading">📊 Comparison: Three ML Types</div>', unsafe_allow_html=True)
with st.expander("🔄 Side-by-Side Comparison"):
    import pandas as pd
    df = pd.DataFrame({
        "Aspect": ["Training Data", "Goal", "Output", "Finance Example", "Complexity"],
        "Supervised": ["Labelled (X + Y)", "Predict known output", "Number or category", "Credit score", "Medium"],
        "Unsupervised": ["Unlabelled (X only)", "Find hidden structure", "Clusters or patterns", "Customer segments", "Medium–High"],
        "Reinforcement": ["Rewards/penalties", "Maximise cumulative reward", "Policy/strategy", "Trading algorithm", "High"],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# Topic 4 - Key Algorithms
st.markdown('<div class="section-heading">⚙️ Key ML Algorithms Explained Simply</div>', unsafe_allow_html=True)
with st.expander("🔧 Algorithm Reference Guide"):
    algo_tab1, algo_tab2, algo_tab3 = st.tabs(["📉 Regression & Classification", "🌲 Tree-Based", "🔵 Clustering"])
    with algo_tab1:
        st.markdown("""
        **Linear Regression**
        Fits a straight line through data to predict a continuous output.
        *Finance use:* Predicting revenue based on headcount, advertising spend, or economic indicators.

        ---
        **Logistic Regression**
        Despite the name, used for classification. Estimates the probability an observation belongs to a class.
        *Finance use:* Probability of loan default — output is a probability between 0 and 1.

        ---
        **Support Vector Machine (SVM)**
        Finds the optimal boundary (hyperplane) separating two classes.
        *Finance use:* Classifying transactions as fraudulent or legitimate.
        """)
    with algo_tab2:
        st.markdown("""
        **Decision Tree**
        Splits data into branches based on feature values, like a flowchart of yes/no questions.
        *Finance use:* Credit approval rules — very interpretable and auditable.

        ---
        **Random Forest**
        An ensemble of many decision trees — each tree votes, majority wins.
        *Finance use:* More robust fraud detection than a single tree; reduces overfitting.

        ---
        **Gradient Boosting (XGBoost, LightGBM)**
        Builds trees sequentially — each tree corrects the errors of the previous one.
        *Finance use:* Industry standard for credit risk and fraud models. Wins most Kaggle finance competitions.
        """)
    with algo_tab3:
        st.markdown("""
        **K-Means Clustering**
        Groups data into K clusters by minimising distance from each point to its cluster centre.
        *Finance use:* Segmenting customers by spending behaviour, risk profile, or product usage.

        ---
        **Isolation Forest**
        Isolates anomalies by building random trees — outliers are isolated faster than normal points.
        *Finance use:* Journal entry anomaly detection in audit — no labels needed.

        ---
        **Principal Component Analysis (PCA)**
        Reduces many correlated variables into fewer uncorrelated components, preserving variance.
        *Finance use:* Risk factor analysis — reducing 100 market variables to key risk drivers.
        """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Which Algorithm When?</div>
      <div class="finance-lens-body">
        <b>Need to predict a number?</b> → Linear Regression / Gradient Boosting &nbsp;|&nbsp;
        <b>Need to classify?</b> → Logistic Regression / Random Forest / XGBoost &nbsp;|&nbsp;
        <b>Need to find groups?</b> → K-Means &nbsp;|&nbsp;
        <b>Need to find outliers without labels?</b> → Isolation Forest &nbsp;|&nbsp;
        <b>Need an explainable model for regulators?</b> → Decision Tree / Logistic Regression
      </div>
    </div>
    """, unsafe_allow_html=True)

# Topic 5 - ML Pipeline
st.markdown('<div class="section-heading">🔄 The Machine Learning Pipeline</div>', unsafe_allow_html=True)
with st.expander("🛠️ From Raw Data to Deployed Model"):
    steps = [
        ("1️⃣", "Problem Definition", "What are we predicting? What is success? What data do we need?", "Predict which invoices will be paid late (>30 days overdue)."),
        ("2️⃣", "Data Collection", "Gather historical data with known outcomes.", "5 years of invoice data: amount, customer, payment terms, actual days to pay."),
        ("3️⃣", "Data Cleaning", "Handle missing values, remove duplicates, fix errors.", "Fill missing payment terms, remove test invoices, standardise currency."),
        ("4️⃣", "Feature Engineering", "Create informative input variables for the model.", "Create: customer average DSO, invoice size bucket, days since last late payment."),
        ("5️⃣", "Model Training", "Algorithm learns patterns from training data.", "Train XGBoost classifier on 80% of data."),
        ("6️⃣", "Model Evaluation", "Test on held-out data. Measure accuracy, precision, recall.", "Test on remaining 20%. Achieve 87% accuracy, review confusion matrix."),
        ("7️⃣", "Deployment", "Integrate model into production systems.", "Connect to ERP — model scores new invoices daily."),
        ("8️⃣", "Monitoring", "Track model performance over time. Retrain when needed.", "Alert if accuracy drops below 80% — may indicate shift in customer behaviour."),
    ]
    for icon, step, desc, finance_ex in steps:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"**{icon} {step}**")
        with col2:
            st.markdown(desc)
            st.caption(f"💼 Finance example: {finance_ex}")
        st.divider()

# Topic 6 - Overfitting
st.markdown('<div class="section-heading">⚠️ Overfitting & Underfitting</div>', unsafe_allow_html=True)
with st.expander("🎯 A Critical Concept for Financial Model Governance"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="topic-card" style="border-left-color:#28a745">
        <div class="topic-card-title">✅ Good Fit</div>
        Model captures the true underlying pattern. Performs well on both training and new data.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="topic-card" style="border-left-color:#dc3545">
        <div class="topic-card-title">❌ Overfitting</div>
        Model memorises training data including noise. Performs great on training data but poorly on new data. Major risk in finance!
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="topic-card" style="border-left-color:#ffc107">
        <div class="topic-card-title">⚠️ Underfitting</div>
        Model is too simple to capture the pattern. Performs poorly even on training data.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    **How to detect:** Compare training accuracy vs test/validation accuracy.
    If training accuracy >> test accuracy → overfitting.

    **How to fix overfitting:** Cross-validation · Regularisation (L1/L2) ·
    Reduce model complexity · Add more training data · Dropout (for neural nets)
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Why This Matters for Model Risk</div>
      <div class="finance-lens-body">
        An overfitted credit model may look excellent in backtesting but fail badly on live applications.
        Regulatory model risk frameworks (SR 11-7 in the US, MAS TRM in Singapore) explicitly require
        out-of-sample testing and ongoing performance monitoring for this reason. Always ask your
        data science team: "What is the out-of-sample performance?"
      </div>
    </div>
    """, unsafe_allow_html=True)

# Topic 7 - Evaluation Metrics
st.markdown('<div class="section-heading">📏 Model Evaluation Metrics</div>', unsafe_allow_html=True)
with st.expander("📊 How to Measure If Your ML Model Is Any Good"):
    tab1, tab2 = st.tabs(["Classification Metrics", "Regression Metrics"])
    with tab1:
        st.markdown("""
        | Metric | What It Measures | Finance Use |
        |--------|-----------------|-------------|
        | **Accuracy** | % predictions correct overall | General baseline — misleading with imbalanced data |
        | **Precision** | Of predicted positives, how many are truly positive | Fraud: avoid too many false alarms |
        | **Recall (Sensitivity)** | Of actual positives, how many did we catch | Fraud: avoid missing real fraud cases |
        | **F1 Score** | Harmonic mean of precision and recall | Balanced metric for fraud models |
        | **AUC-ROC** | Model's ability to distinguish classes at all thresholds | Standard for credit risk models |
        | **Confusion Matrix** | Table of TP, TN, FP, FN counts | Full picture of classification errors |
        """)
        st.info("💡 **Finance tip:** For fraud detection, **Recall** matters more than Precision — missing a fraud is worse than a false alarm. For credit approval, **Precision** may matter more — you don't want to reject good customers.")
    with tab2:
        st.markdown("""
        | Metric | What It Measures | Finance Use |
        |--------|-----------------|-------------|
        | **MAE** (Mean Absolute Error) | Average absolute difference from actual | Revenue forecast: average miss in dollars |
        | **RMSE** (Root Mean Squared Error) | Like MAE but penalises large errors more | Cash flow forecast: penalises big misses |
        | **MAPE** (Mean Absolute % Error) | Error as a percentage of actual value | Forecast accuracy as a % — comparable across scales |
        | **R² (R-squared)** | Proportion of variance explained by the model | How much of revenue variation does the model explain? |
        """)

# Quiz
st.markdown('<div class="section-heading">🧩 Knowledge Check</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {"q": "A fraud detection model is trained on historical transactions labelled 'fraud' or 'not fraud'. This is an example of:", "options": ["Unsupervised Learning", "Reinforcement Learning", "Supervised Learning", "Deep Learning"], "answer": "Supervised Learning", "explanation": "Supervised learning uses labelled data — here, each transaction has a known label (fraud/not fraud) used to train the model."},
    {"q": "A bank wants to group its 500,000 customers into segments based on spending behaviour, with no predefined categories. Which ML approach is most appropriate?", "options": ["Supervised Learning", "Reinforcement Learning", "Unsupervised Clustering", "Linear Regression"], "answer": "Unsupervised Clustering", "explanation": "With no predefined labels, unsupervised clustering (e.g. K-Means) finds natural groupings in the data."},
    {"q": "An ML model achieves 99% accuracy on training data but only 62% on new test data. This is a sign of:", "options": ["Underfitting", "Overfitting", "Good generalisation", "Data leakage only"], "answer": "Overfitting", "explanation": "When training accuracy far exceeds test accuracy, the model has memorised training data rather than learned general patterns — this is overfitting."},
    {"q": "For a credit default prediction model, which metric is most important to regulators reviewing model risk?", "options": ["Training accuracy only", "AUC-ROC on out-of-sample data", "Number of features used", "Model file size"], "answer": "AUC-ROC on out-of-sample data", "explanation": "Regulators (SR 11-7, MAS TRM) require out-of-sample performance testing. AUC-ROC measures discrimination ability across all thresholds — the standard for credit risk models."},
    {"q": "XGBoost, Random Forest, and Gradient Boosting are all examples of:", "options": ["Clustering algorithms", "Reinforcement learning agents", "Ensemble tree-based algorithms", "Dimensionality reduction techniques"], "answer": "Ensemble tree-based algorithms", "explanation": "All three combine multiple decision trees. Random Forest uses parallel trees; Gradient Boosting and XGBoost build trees sequentially, each correcting the previous."},
]

for key in ["m2_q_index","m2_score","m2_answered","m2_selected","m2_quiz_done"]:
    if key not in st.session_state:
        st.session_state[key] = 0 if "index" in key or "score" in key else False

if not st.session_state.m2_quiz_done:
    q_data = questions[st.session_state.m2_q_index]
    st.markdown(f"**Question {st.session_state.m2_q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")
    choice = st.radio("Select your answer:", q_data["options"], key=f"m2_q_{st.session_state.m2_q_index}")
    col_s, col_n = st.columns(2)
    with col_s:
        if st.button("✅ Submit", key=f"m2_sub_{st.session_state.m2_q_index}"):
            st.session_state.m2_answered = True
            st.session_state.m2_selected = choice
            if choice == q_data["answer"]: st.session_state.m2_score += 1
    if st.session_state.m2_answered:
        if st.session_state.m2_selected == q_data["answer"]: st.success(f"✅ Correct! {q_data['explanation']}")
        else: st.error(f"❌ Answer: **{q_data['answer']}** — {q_data['explanation']}")
        with col_n:
            if st.session_state.m2_q_index < len(questions)-1:
                if st.button("Next ➡️", key=f"m2_next_{st.session_state.m2_q_index}"):
                    st.session_state.m2_q_index += 1; st.session_state.m2_answered = False; st.rerun()
            else:
                if st.button("🏁 Results"):
                    st.session_state.m2_quiz_done = True; st.rerun()
else:
    s,t = st.session_state.m2_score, len(questions)
    pct = int((s/t)*100)
    st.markdown(f"### {'🏆' if pct>=80 else '👍' if pct>=60 else '📚'} Score: {s}/{t} ({pct}%)")
    st.progress(pct/100)
    st.info("Excellent grasp of ML!" if pct>=80 else "Good effort — review the algorithm section." if pct>=60 else "Revisit the three ML types and re-attempt.")
    if st.button("🔄 Retry"):
        for k,v in [("m2_q_index",0),("m2_score",0),("m2_answered",False),("m2_selected",None),("m2_quiz_done",False)]:
            st.session_state[k]=v
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Takeaways
st.markdown('<div class="section-heading">💡 Key Takeaways</div>', unsafe_allow_html=True)
for i,t in enumerate([
    "ML learns rules from data; the three types are **Supervised**, **Unsupervised**, and **Reinforcement Learning**.",
    "**Supervised learning** (with labels) is the most common in finance — credit scoring, fraud detection, forecasting.",
    "**Unsupervised learning** finds hidden patterns without labels — ideal for customer segmentation and audit anomaly detection.",
    "**Gradient Boosting (XGBoost)** is the industry standard for tabular financial data classification and regression.",
    "**Overfitting** is the #1 model risk — always demand out-of-sample test results before trusting any financial ML model.",
    "Choosing the right **evaluation metric** matters — for fraud, Recall > Precision; for credit, AUC-ROC is the standard.",
],1):
    st.markdown(f"**{i}.** {t}")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ M1: Foundations", use_container_width=True): st.info("Navigate to Module 1 from the sidebar.")
with col2: st.markdown("<div style='text-align:center;padding-top:0.4rem'>📗 Module 2 of 8</div>", unsafe_allow_html=True)
with col3:
    if st.button("M3: Deep Learning ➡️", use_container_width=True): st.info("Navigate to Module 3 from the sidebar.")
st.caption("Knowledge Folder · AI Series · Module 2 — Machine Learning Essentials · © 2025")