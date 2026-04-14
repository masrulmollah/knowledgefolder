"""
Machine Learning for Finance & Accounts
Module 3 – Supervised Learning for Finance

USAGE: import ml_module_03; ml_module_03.show()
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#1D4ED8"; SECONDARY="#3B82F6"; SUCCESS="#10B981"; WARNING="#F59E0B"; DANGER="#EF4444"


def _css():
    st.markdown("""
    <style>
    .main { background: #EFF6FF; }
    .hero-banner {
        background: linear-gradient(135deg, #1D4ED8 0%, #3B82F6 60%, #06B6D4 100%);
        border-radius: 16px; padding: 2.4rem 2.8rem; color: white; margin-bottom: 1.6rem;
    }
    .hero-banner h1 { font-size: 2.1rem; margin: 0 0 .4rem; font-weight: 700; }
    .hero-banner p  { font-size: 1.05rem; margin: 0; opacity: .9; }
    .hero-badge { display:inline-block; background:rgba(255,255,255,.2);
        border:1px solid rgba(255,255,255,.35); border-radius:20px;
        padding:.18rem .8rem; font-size:.8rem; margin-bottom:.7rem; }
    .section-title { font-size:1.35rem; font-weight:700; color:#1E293B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #1D4ED8; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .info-card .card-icon { font-size:1.7rem; margin-bottom:.4rem; }
    .info-card h4 { font-size:1rem; font-weight:700; color:#1E293B; margin:0 0 .3rem; }
    .info-card p  { font-size:.88rem; color:#475569; margin:0; line-height:1.55; }
    .definition-box { background:#DBEAFE; border-left:5px solid #1D4ED8;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    .definition-box p { margin:0; color:#1E293B; font-size:.96rem; line-height:1.65; }
    .algo-card { background:white; border-radius:12px; padding:1.2rem 1.4rem;
        border-top:4px solid #1D4ED8; box-shadow:0 2px 8px rgba(0,0,0,.07); margin-bottom:1rem; }
    .quiz-box { background:white; border-radius:12px; padding:1.4rem 1.6rem;
        box-shadow:0 2px 10px rgba(0,0,0,.08); margin-top:1rem; }
    .quiz-q { font-weight:700; color:#1E293B; font-size:1rem; margin-bottom:.8rem; }
    </style>""", unsafe_allow_html=True)


def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 3 — Supervised Learning for Finance</h1>
      <p>Learn the most widely used ML family: from simple linear regression to
         powerful ensemble methods — all applied to real finance problems.</p>
    </div>""", unsafe_allow_html=True)
    for col,(icon,label,val) in zip(st.columns(4),[
        ("🎯","Level","Intermediate"),("⏱️","Read time","~35 minutes"),
        ("📋","Algorithms","5 covered"),("🏆","Outcome","Build predictive models"),
    ]):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""", unsafe_allow_html=True)


def _section_what_is_supervised():
    st.markdown('<div class="section-title">🏷️ 1. What is Supervised Learning?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Supervised Learning</strong> trains a model on labelled data — each record
      has a known correct answer (the <em>label</em> or <em>target</em>). The model learns
      the relationship between input features and the target, then applies that relationship
      to predict outcomes on new, unseen data.</p>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **Two flavours of supervised learning:**

        | Task | Target type | Finance example |
        |------|-------------|-----------------|
        | **Regression** | Continuous number | Predict invoice amount, forecast revenue |
        | **Classification** | Category / class | Default or not, fraud or legitimate |
        """)
    with c2:
        fig = go.Figure()
        np.random.seed(1)
        x = np.linspace(1, 10, 50)
        y = 2.5 * x + np.random.randn(50) * 3
        fig.add_trace(go.Scatter(x=x, y=y, mode="markers", name="Data points",
                                 marker=dict(color=SECONDARY, size=7)))
        fig.add_trace(go.Scatter(x=x, y=2.5*x, mode="lines", name="Regression line",
                                 line=dict(color=DANGER, width=2)))
        fig.update_layout(title="Regression: predict a number",
                          height=220, paper_bgcolor="rgba(0,0,0,0)",
                          plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=35,b=10,l=10,r=10),
                          xaxis=dict(gridcolor="#E2E8F0", title="Days overdue"),
                          yaxis=dict(gridcolor="#E2E8F0", title="Amount at risk ($K)"))
        st.plotly_chart(fig, use_container_width=True)


def _section_linear_regression():
    st.markdown('<div class="section-title">📈 2. Linear Regression — Predict Numbers</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="algo-card">
    <strong>How it works:</strong> Finds the best straight line through data points.
    Equation: <code>Y = a + b₁X₁ + b₂X₂ + ...</code> where Y is what you predict
    and X values are your features.<br><br>
    <strong>Finance use cases:</strong> Revenue forecasting · Budget estimation ·
    Predicting collection amounts · Property valuation
    </div>""", unsafe_allow_html=True)

    st.markdown("#### 🎛️ Interactive: See linear regression in action")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        intercept = st.slider("Base revenue (intercept $M)", 10, 100, 50)
        slope = st.slider("Effect per sales rep hired", 0.5, 5.0, 2.0, 0.1)
        noise = st.slider("Data noise level", 1, 20, 8)

    with col2:
        np.random.seed(42)
        reps = np.arange(5, 55)
        revenue = intercept + slope * reps + np.random.randn(50) * noise
        predicted = intercept + slope * reps
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=reps, y=revenue, mode="markers", name="Actual",
                                 marker=dict(color=SECONDARY, size=6, opacity=.7)))
        fig.add_trace(go.Scatter(x=reps, y=predicted, mode="lines", name="Model prediction",
                                 line=dict(color=DANGER, width=2.5)))
        fig.update_layout(height=260, paper_bgcolor="rgba(0,0,0,0)",
                          plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=15,b=10,l=10,r=10),
                          xaxis=dict(gridcolor="#E2E8F0", title="Number of sales reps"),
                          yaxis=dict(gridcolor="#E2E8F0", title="Revenue ($M)"),
                          legend=dict(x=0, y=1))
        st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**Model equation:** Revenue = {intercept} + {slope} × (Sales Reps)")


def _section_logistic_regression():
    st.markdown('<div class="section-title">🔀 3. Logistic Regression — Predict Yes/No</div>', unsafe_allow_html=True)
    st.markdown("""
    Despite the name, logistic regression is a **classification** algorithm.
    It predicts a probability (0–1) that a record belongs to a class.

    **Finance use cases:** Invoice late payment prediction · Credit default · Fraud flag
    """)
    np.random.seed(5)
    days = np.sort(np.random.uniform(0, 90, 200))
    prob_late = 1 / (1 + np.exp(-(days - 45) / 10))
    colour = ["#EF4444" if p > 0.5 else "#10B981" for p in prob_late]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=days, y=prob_late, mode="lines",
                             line=dict(color=PRIMARY, width=2.5), name="P(Late payment)"))
    fig.add_shape(type="line", x0=0, x1=90, y0=0.5, y1=0.5,
                  line=dict(color=WARNING, width=1.5, dash="dash"))
    fig.add_annotation(x=80, y=0.52, text="Decision threshold (0.5)", showarrow=False,
                       font=dict(color=WARNING, size=11))
    fig.update_layout(title="Logistic regression: probability of late payment vs days outstanding",
                      height=260, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=10),
                      xaxis=dict(gridcolor="#E2E8F0", title="Days outstanding"),
                      yaxis=dict(gridcolor="#E2E8F0", title="Probability of late payment", range=[0,1]))
    st.plotly_chart(fig, use_container_width=True)
    st.info("💡 At 45 days outstanding, there is a 50% probability of late payment. "
            "Below 45 days = likely on time (green). Above 45 days = likely late (red).")


def _section_decision_trees():
    st.markdown('<div class="section-title">🌳 4. Decision Trees & Random Forests</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🌱 Decision Trees", "🌲 Random Forests"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            **How it works:** Splits data by asking yes/no questions about features,
            building a tree of decisions. Very intuitive — mimics how an auditor or
            credit analyst thinks.

            **Strengths:**
            - Easy to explain to management
            - Handles both numbers and categories
            - No need to scale features

            **Weakness:**
            - Tends to overfit (memorise training data)
            - A single tree can be unstable
            """)
        with c2:
            st.markdown("""
            **Finance credit decision tree example:**
            ```
            Is credit score > 700?
            ├── YES → Is debt-to-income < 40%?
            │         ├── YES → ✅ APPROVE
            │         └── NO  → ⚠️ REVIEW
            └── NO  → Is employment > 2 years?
                      ├── YES → ⚠️ REVIEW
                      └── NO  → ❌ DECLINE
            ```
            """)
    with tab2:
        st.markdown("""
        **Random Forest = hundreds of decision trees, combined.**

        Each tree is trained on a random subset of data and features.
        The final prediction is the **majority vote** (classification) or
        **average** (regression) across all trees.

        **Why it's better:**
        - Overfitting is drastically reduced
        - More stable and accurate
        - Still provides feature importance rankings
        """)
        features = ["Credit score","Debt-to-income","Employment length",
                    "Loan amount","Payment history","Number of accounts"]
        importance = [0.31, 0.24, 0.18, 0.13, 0.09, 0.05]
        fig = px.bar(x=importance, y=features, orientation="h",
                     title="Random Forest: Feature Importance for Credit Default",
                     labels={"x":"Importance","y":"Feature"},
                     color=importance, color_continuous_scale=["#DBEAFE","#1D4ED8"])
        fig.update_layout(height=280, paper_bgcolor="rgba(0,0,0,0)",
                          plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=35,b=10,l=10,r=10),
                          coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)


def _section_gradient_boosting():
    st.markdown('<div class="section-title">🚀 5. Gradient Boosting (XGBoost / LightGBM)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Gradient Boosting</strong> builds trees <em>sequentially</em> — each new
      tree corrects the errors of the previous one. XGBoost and LightGBM are the most
      popular implementations. They consistently win data science competitions and are
      widely used in finance for credit scoring and fraud detection.</p>
    </div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    for col, (title, color, text) in zip([col1,col2,col3],[
        ("Decision Tree","#DBEAFE","A single tree makes a rough prediction with many errors."),
        ("+ Correction Tree","#BFDBFE","A second tree learns from the first tree's errors."),
        ("Final: Ensemble","#1D4ED8","Hundreds of correction trees = highly accurate model."),
    ]):
        col.markdown(f"""<div class="info-card" style="border-top:4px solid {color}">
          <h4>{title}</h4><p>{text}</p></div>""", unsafe_allow_html=True)

    st.markdown("#### 📊 Algorithm comparison for a fraud detection task")
    algos = ["Logistic Regression","Decision Tree","Random Forest","XGBoost (Gradient Boosting)"]
    accuracy = [78, 82, 91, 95]
    auc = [0.81, 0.79, 0.94, 0.97]
    df = pd.DataFrame({"Algorithm":algos, "Accuracy (%)":accuracy, "AUC-ROC":auc})
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Accuracy (%)", x=algos, y=accuracy, marker_color=SECONDARY))
    fig.add_trace(go.Scatter(name="AUC-ROC ×100", x=algos, y=[v*100 for v in auc],
                             mode="lines+markers", yaxis="y2",
                             line=dict(color=DANGER, width=2),
                             marker=dict(size=8)))
    fig.update_layout(
        height=300, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=20,b=10,l=10,r=10), barmode="group",
        yaxis=dict(title="Accuracy (%)", gridcolor="#E2E8F0"),
        yaxis2=dict(title="AUC-ROC ×100", overlaying="y", side="right"),
        legend=dict(x=0, y=1),
    )
    st.plotly_chart(fig, use_container_width=True)


def _section_use_cases():
    st.markdown('<div class="section-title">💼 6. Finance Use Cases — Supervised Learning</div>', unsafe_allow_html=True)
    cases = [
        ("🏦","Credit Scoring","Supervised (Classification)",
         "Predict probability of loan default. Features: income, debt ratio, credit history, employment."),
        ("💳","Fraud Detection","Supervised (Classification)",
         "Flag fraudulent transactions. Features: amount, merchant, location, time, velocity."),
        ("📊","Revenue Forecasting","Supervised (Regression)",
         "Predict next quarter revenue. Features: pipeline value, seasonal trends, macro indicators."),
        ("📄","Invoice Classification","Supervised (Classification)",
         "Auto-assign GL codes to invoices. Features: vendor name, description, amount, department."),
        ("⏰","Late Payment Prediction","Supervised (Classification)",
         "Predict which invoices will be paid late. Features: customer history, amount, payment terms."),
        ("📉","Churn Prediction","Supervised (Classification)",
         "Predict which customers will churn. Features: transaction frequency, product usage, complaints."),
    ]
    for i in range(0, len(cases), 3):
        cols = st.columns(3)
        for col, (icon, title, algo, desc) in zip(cols, cases[i:i+3]):
            col.markdown(f"""<div class="info-card" style="margin-bottom:1rem">
              <div class="card-icon">{icon}</div>
              <h4>{title}</h4>
              <p style="font-size:.77rem;background:#DBEAFE;color:#1E3A5F;
                 border-radius:4px;padding:.1rem .4rem;display:inline-block;
                 margin-bottom:.4rem">{algo}</p>
              <p>{desc}</p></div>""", unsafe_allow_html=True)


def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 3 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q":"Q1. You want to predict the exact dollar amount a customer will spend next month. Which type of supervised learning should you use?",
         "opts":["Classification","Clustering","Regression","Reinforcement Learning"],
         "ans":"Regression","exp":"✅ Correct! Regression predicts a continuous number — like a dollar amount."},
        {"q":"Q2. A Random Forest combines many decision trees. What is the main benefit?",
         "opts":["It trains faster","It reduces overfitting and improves accuracy",
                 "It requires less data","It works only for regression"],
         "ans":"It reduces overfitting and improves accuracy",
         "exp":"✅ Correct! Averaging hundreds of trees cancels out individual errors, dramatically reducing overfitting."},
        {"q":"Q3. Which algorithm is generally considered the most accurate for structured financial data?",
         "opts":["Linear Regression","Decision Tree","Gradient Boosting (XGBoost)",
                 "Logistic Regression"],
         "ans":"Gradient Boosting (XGBoost)",
         "exp":"✅ Correct! XGBoost/LightGBM consistently achieves the best performance on structured tabular data — the type most common in finance."},
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("", q["opts"], key=f"mod3_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"❌ Correct answer: **{q['ans']}**\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True); st.markdown("")


def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 ML for Finance & Accounts** · Module 3 of 10")
    c2.markdown("<div style='text-align:center'><a href='?module=2' style='color:#1D4ED8'>◀ Module 2</a>"
                " &nbsp;|&nbsp; <a href='?module=4' style='color:#1D4ED8'>Module 4 ▶</a></div>",
                unsafe_allow_html=True)
    c3.markdown("<div style='text-align:right;color:#64748B;font-size:.85rem'>Knowledge Folder</div>",
                unsafe_allow_html=True)


def show():
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 3 — Sections")
        st.markdown("1. What is Supervised Learning?\n2. Linear Regression\n3. Logistic Regression\n"
                    "4. Decision Trees & Random Forests\n5. Gradient Boosting\n6. Finance Use Cases\n---\n🧩 Quiz")
        st.progress(30, text="Module 3 / 10")
    _section_what_is_supervised(); st.markdown("")
    _section_linear_regression(); st.markdown("")
    _section_logistic_regression(); st.markdown("")
    _section_decision_trees(); st.markdown("")
    _section_gradient_boosting(); st.markdown("")
    _section_use_cases(); st.markdown("")
    _knowledge_check(); _footer()


if __name__ == "__main__":
    st.set_page_config(page_title="Module 3 – Supervised Learning | Knowledge Folder",
                       page_icon="📈", layout="wide")
    show()