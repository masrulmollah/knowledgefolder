"""
Machine Learning for Finance & Accounts
Module 9 – Model Evaluation & Ethics

USAGE: import ml_module_09; ml_module_09.show()
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#991B1B"; SECONDARY="#EF4444"; SUCCESS="#10B981"; WARNING="#F59E0B"; ACCENT="#6366F1"


def _css():
    st.markdown("""
    <style>
    .main { background:#FFF1F2; }
    .hero-banner { background:linear-gradient(135deg,#991B1B 0%,#DC2626 60%,#EA580C 100%);
        border-radius:16px; padding:2.4rem 2.8rem; color:white; margin-bottom:1.6rem; }
    .hero-banner h1 { font-size:2.1rem; margin:0 0 .4rem; font-weight:700; }
    .hero-banner p  { font-size:1.05rem; margin:0; opacity:.9; }
    .hero-badge { display:inline-block; background:rgba(255,255,255,.2);
        border:1px solid rgba(255,255,255,.35); border-radius:20px;
        padding:.18rem .8rem; font-size:.8rem; margin-bottom:.7rem; }
    .section-title { font-size:1.35rem; font-weight:700; color:#1E293B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #991B1B; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .info-card .card-icon { font-size:1.7rem; margin-bottom:.4rem; }
    .info-card h4 { font-size:1rem; font-weight:700; color:#1E293B; margin:0 0 .3rem; }
    .info-card p  { font-size:.88rem; color:#475569; margin:0; line-height:1.55; }
    .definition-box { background:#FEE2E2; border-left:5px solid #991B1B;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    .definition-box p { margin:0; color:#1E293B; font-size:.96rem; line-height:1.65; }
    .quiz-box { background:white; border-radius:12px; padding:1.4rem 1.6rem;
        box-shadow:0 2px 10px rgba(0,0,0,.08); margin-top:1rem; }
    .quiz-q { font-weight:700; color:#1E293B; font-size:1rem; margin-bottom:.8rem; }
    .ethics-card { background:white; border-radius:12px; padding:1.2rem 1.5rem;
        border-left:5px solid #DC2626; box-shadow:0 2px 8px rgba(0,0,0,.07); margin-bottom:1rem; }
    </style>""", unsafe_allow_html=True)


def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 9 — Model Evaluation &amp; Ethics</h1>
      <p>Learn to rigorously evaluate ML models, understand bias and fairness,
         ensure explainability for regulators, and govern AI responsibly in finance.</p>
    </div>""", unsafe_allow_html=True)
    for col,(icon,label,val) in zip(st.columns(4),[
        ("⚖️","Level","Advanced / Critical"),("⏱️","Read time","~35 minutes"),
        ("📋","Topics","Metrics, bias, SHAP, compliance"),("🏆","Outcome","Responsible ML deployment"),
    ]):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""", unsafe_allow_html=True)


def _section_metrics():
    st.markdown('<div class="section-title">📊 1. Evaluation Metrics — Choosing the Right One</div>', unsafe_allow_html=True)
    st.markdown("""
    Not all metrics are created equal. In finance, **the cost of errors varies** —
    a missed fraud costs far more than a false fraud alert.
    """)

    tab1, tab2, tab3 = st.tabs(["📋 Classification Metrics","📈 Regression Metrics","⚖️ When to Use Which"])
    with tab1:
        st.markdown("""
        #### The Confusion Matrix — foundation of all classification metrics
        """)
        fig = go.Figure(go.Heatmap(
            z=[[850, 30],[45, 75]],
            x=["Predicted: On Time","Predicted: Late"],
            y=["Actual: On Time","Actual: Late"],
            text=[[850, 30],[45, 75]],
            texttemplate="%{text}",
            textfont={"size":22},
            colorscale=[[0,"#ECFDF5"],[1,"#065F46"]],
        ))
        fig.update_layout(height=240, paper_bgcolor="rgba(0,0,0,0)", margin=dict(t=10,b=10,l=10,r=10))
        st.plotly_chart(fig, use_container_width=True)

        tn, fp, fn, tp = 850, 30, 45, 75
        accuracy = (tp+tn)/(tp+tn+fp+fn)
        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        f1 = 2*precision*recall/(precision+recall)

        metrics_df = pd.DataFrame({
            "Metric": ["Accuracy","Precision","Recall (Sensitivity)","Specificity","F1 Score"],
            "Formula": ["(TP+TN)/Total","TP/(TP+FP)","TP/(TP+FN)","TN/(TN+FP)","2×P×R/(P+R)"],
            "Value": [f"{accuracy:.1%}",f"{precision:.1%}",f"{recall:.1%}",f"{tn/(tn+fp):.1%}",f"{f1:.1%}"],
            "Finance meaning": [
                "Overall prediction correctness",
                "Of predicted 'late' invoices, how many were truly late?",
                "Of all actual late invoices, how many did we catch?",
                "Of on-time invoices, how many did we correctly label?",
                "Balance of precision and recall",
            ]
        })
        st.dataframe(metrics_df, use_container_width=True, hide_index=True)

    with tab2:
        st.markdown("""
        For regression models (predicting numbers like revenue or cash flow):

        | Metric | Formula | Finance meaning |
        |--------|---------|-----------------|
        | **MAE** | Mean Absolute Error | Average dollar error in predictions |
        | **RMSE** | Root Mean Squared Error | Penalises large errors more heavily |
        | **MAPE** | Mean Absolute % Error | Error as % of actual — useful for budgets |
        | **R²** | R-squared | How much variance the model explains (0–1) |

        > **Finance example:** A revenue forecasting model with MAPE of 5% means
        forecasts are off by 5% on average — suitable for most planning purposes.
        """)

    with tab3:
        decision_data = {
            "Scenario": ["Fraud detection","Credit approval","Revenue forecasting",
                         "Expense classification","Customer churn"],
            "Primary metric": ["Recall","Precision + AUC","MAPE / RMSE","Accuracy","Recall + F1"],
            "Why": ["Missing real fraud is very costly",
                    "Both false approvals and rejections are costly",
                    "% error matters for budget accuracy",
                    "Label accuracy is the main goal",
                    "Missing churners more costly than false alarms"],
        }
        st.dataframe(pd.DataFrame(decision_data), use_container_width=True, hide_index=True)


def _section_overfitting():
    st.markdown('<div class="section-title">⚠️ 2. Overfitting vs Underfitting</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Overfitting:</strong> The model memorises training data instead of learning
      general patterns. It performs brilliantly on training data but fails on new data —
      like a student who memorises past exam answers but can't solve new questions.</p>
    </div>""", unsafe_allow_html=True)

    depth = st.slider("Model complexity (tree depth)", 1, 20, 5)
    np.random.seed(42)
    train_acc = min(0.99, 0.65 + depth * 0.04 - depth * 0.001)
    test_acc = max(0.55, 0.88 - (max(0, depth - 6) ** 1.5) * 0.012)

    depths = list(range(1, 21))
    train_accs = [min(0.99, 0.65 + d*0.04 - d*0.001) for d in depths]
    test_accs = [max(0.55, 0.88 - (max(0, d-6)**1.5)*0.012) for d in depths]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=depths, y=train_accs, mode="lines", name="Training accuracy",
                             line=dict(color=SECONDARY, width=2)))
    fig.add_trace(go.Scatter(x=depths, y=test_accs, mode="lines", name="Test accuracy",
                             line=dict(color=SUCCESS, width=2)))
    fig.add_vline(x=depth, line_dash="dot", line_color=WARNING,
                  annotation_text=f"Current: depth {depth}")
    fig.add_vrect(x0=10, x1=20, fillcolor=SECONDARY, opacity=0.1,
                  annotation_text="Overfit zone", annotation_position="top right")
    fig.update_layout(title="Training vs test accuracy by model complexity",
                      height=280, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=10),
                      yaxis=dict(gridcolor="#E2E8F0", title="Accuracy", range=[0.5,1.02]),
                      xaxis=dict(gridcolor="#E2E8F0", title="Tree depth"),
                      legend=dict(x=0,y=0))
    st.plotly_chart(fig, use_container_width=True)

    if depth <= 4: st.warning("⚠️ Underfitting: model is too simple — both training and test accuracy are low.")
    elif depth <= 8: st.success("✅ Good fit: model generalises well.")
    else: st.error(f"🚨 Overfitting: training accuracy {train_acc:.1%} >> test accuracy {test_acc:.1%}.")


def _section_roc_curve():
    st.markdown('<div class="section-title">📈 3. ROC Curve & AUC — The Gold Standard</div>', unsafe_allow_html=True)
    st.markdown("""
    The **ROC curve** plots True Positive Rate (Recall) against False Positive Rate
    at every possible decision threshold. **AUC** (Area Under Curve) summarises it
    as a single number: 1.0 = perfect, 0.5 = random guessing.
    """)

    np.random.seed(7)
    n = 1000
    threshold = st.slider("Decision threshold", 0.1, 0.9, 0.5, 0.05)

    tp_rates = np.array([0,0.05,0.12,0.28,0.45,0.61,0.74,0.84,0.92,0.97,1.0])
    fp_rates = np.array([0,0.01,0.03,0.06,0.10,0.16,0.24,0.35,0.50,0.70,1.0])
    idx = int(threshold * 10)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fp_rates, y=tp_rates, mode="lines", name="Our model (AUC=0.92)",
                             line=dict(color=PRIMARY, width=2.5)))
    fig.add_trace(go.Scatter(x=[0,1], y=[0,1], mode="lines", name="Random (AUC=0.50)",
                             line=dict(color="gray", width=1.5, dash="dash")))
    fig.add_trace(go.Scatter(x=[fp_rates[idx]], y=[tp_rates[idx]], mode="markers",
                             name=f"Threshold={threshold:.2f}",
                             marker=dict(color=DANGER, size=12)))
    fig.update_layout(title="ROC Curve — fraud detection model",
                      height=300, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=10),
                      xaxis=dict(gridcolor="#E2E8F0", title="False Positive Rate", range=[0,1]),
                      yaxis=dict(gridcolor="#E2E8F0", title="True Positive Rate (Recall)", range=[0,1.02]),
                      legend=dict(x=0.4,y=0.15))
    st.plotly_chart(fig, use_container_width=True)
    st.info(f"At threshold **{threshold:.2f}**: TPR = {tp_rates[idx]:.0%}, FPR = {fp_rates[idx]:.0%}. "
            f"{'Catching more fraud but also more false alarms.' if threshold < 0.5 else 'Fewer false alarms but potentially missing some fraud.'}")


def _section_explainability():
    st.markdown('<div class="section-title">🔎 4. Explainability — SHAP Values</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Black box problem:</strong> Complex models (Random Forest, XGBoost) can be
      highly accurate but hard to explain. Regulators, auditors, and customers demand to know
      <em>why</em> a model made a decision. <strong>SHAP values</strong> quantify each
      feature's contribution to every individual prediction.</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("#### SHAP explanation for a single credit decision — 'DECLINED'")
    features_shap = ["Customer avg delay","Prior late count","Invoice amount",
                     "Credit score","Payment terms","Invoice month"]
    shap_values = [+0.35, +0.22, +0.18, -0.12, +0.05, -0.03]
    colours = [DANGER if v > 0 else SUCCESS for v in shap_values]
    labels = [f"+{v:.2f} (increases risk)" if v > 0 else f"{v:.2f} (decreases risk)" for v in shap_values]

    fig = go.Figure(go.Bar(
        x=shap_values, y=features_shap, orientation="h",
        marker_color=colours, text=labels, textposition="outside",
        textfont=dict(size=11),
    ))
    fig.add_vline(x=0, line_color="gray", line_width=1)
    fig.update_layout(title="Why was this invoice flagged as HIGH RISK?",
                      height=280, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=80),
                      xaxis=dict(gridcolor="#E2E8F0", title="SHAP value (impact on risk)"),
                      yaxis=dict(gridcolor="#E2E8F0"))
    st.plotly_chart(fig, use_container_width=True)
    st.success("""
    **Human-readable explanation:** This invoice was flagged as high risk primarily because
    the customer has a history of paying 18 days late on average (biggest driver),
    combined with 4 prior late payments. The large invoice amount also increases risk.
    The good credit score partially offsets this.
    """)


def _section_bias_fairness():
    st.markdown('<div class="section-title">⚖️ 5. Bias, Fairness & Ethics in Finance ML</div>', unsafe_allow_html=True)

    ethics_issues = [
        ("🎭","Proxy Discrimination",
         "A credit model may not use 'race' as a feature but might use 'postcode' or 'education level' — which correlate with race. This is proxy discrimination and is illegal in many jurisdictions.",
         "Audit model features for proxy variables. Use fairness-aware training."),
        ("📊","Historical Bias Amplification",
         "If past lending decisions were biased, training on that data amplifies the bias. The model learns 'this group never got loans' and perpetuates it.",
         "Analyse approval rates across protected groups. Use re-sampling or adversarial training."),
        ("🌍","Geographic Discrimination",
         "Using postcode or regional data in credit scoring can systematically disadvantage residents of certain areas.",
         "Test model outcomes by geography. Consider removing or transforming geographic features."),
        ("💼","Model Risk (SR 11-7)",
         "US banks under SR 11-7 guidance must document, validate, and monitor all models. Similar frameworks exist in the UK (PRA/FCA) and EU (EBA).",
         "Maintain model inventory. Conduct independent model validation annually."),
    ]
    for icon, title, problem, solution in ethics_issues:
        st.markdown(f"""<div class="ethics-card">
          <h4>{icon} {title}</h4>
          <p style="color:#475569;margin:.3rem 0"><strong>Problem:</strong> {problem}</p>
          <p style="color:#065F46;margin:0"><strong>Mitigation:</strong> {solution}</p>
          </div>""", unsafe_allow_html=True)


def _section_governance():
    st.markdown('<div class="section-title">🏛️ 6. ML Governance in Finance</div>', unsafe_allow_html=True)
    st.markdown("""
    Responsible deployment of ML in finance requires formal governance. Here is a
    best-practice framework:
    """)

    stages = [
        ("📋","Model Inventory","Document every ML model in production: purpose, owner, training date, data sources, known limitations."),
        ("✅","Independent Validation","A team separate from model developers tests and challenges the model before deployment."),
        ("📊","Performance Monitoring","Track model accuracy monthly. Alert if it drops below acceptable thresholds (model drift)."),
        ("🔄","Periodic Retraining","Retrain models on fresh data at least annually, or when performance degrades significantly."),
        ("📝","Explainability Reports","Maintain documentation that explains model decisions to regulators and auditors on demand."),
        ("🚪","Model Retirement","Clear criteria for when to retire a model and how to transition to the replacement."),
    ]
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(stages):
        with cols[i%3]:
            st.markdown(f"""<div class="info-card" style="margin-bottom:1rem;border-top:4px solid #991B1B">
              <div class="card-icon">{icon}</div>
              <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)


def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 9 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q":"Q1. A fraud detection model has 99% accuracy but catches only 30% of actual frauds. What metric should have been prioritised?",
         "opts":["Accuracy","Precision","Recall","R-squared"],
         "ans":"Recall",
         "exp":"✅ Correct! With 99% accuracy the model is predicting 'not fraud' for almost everything (class imbalance). Recall measures how many actual frauds we catch — the critical metric here."},
        {"q":"Q2. SHAP values show that 'postcode' is the second most important feature in a credit scoring model. What concern should this raise?",
         "opts":["The model is overfitting","Potential proxy discrimination against certain geographic areas","The model needs more features","The training data is too small"],
         "ans":"Potential proxy discrimination against certain geographic areas",
         "exp":"✅ Correct! Postcode can serve as a proxy for race or socioeconomic background, raising fairness and legal compliance concerns."},
        {"q":"Q3. A bank's credit model performed excellently when deployed in 2022, but accuracy has been declining since mid-2024. What is the likely cause?",
         "opts":["The model was overfit","Model drift — the real world has changed since training","The training data was too large","The wrong algorithm was chosen"],
         "ans":"Model drift — the real world has changed since training",
         "exp":"✅ Correct! Model drift occurs when the statistical relationship between features and outcomes changes over time (e.g., due to economic changes), making the original model less accurate."},
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("", q["opts"], key=f"mod9_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"❌ Correct answer: **{q['ans']}**\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True); st.markdown("")


def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 ML for Finance & Accounts** · Module 9 of 10")
    c2.markdown("<div style='text-align:center'><a href='?module=8' style='color:#991B1B'>◀ Module 8</a>"
                " &nbsp;|&nbsp; <a href='?module=10' style='color:#991B1B'>Module 10 ▶</a></div>",
                unsafe_allow_html=True)
    c3.markdown("<div style='text-align:right;color:#64748B;font-size:.85rem'>Knowledge Folder</div>",
                unsafe_allow_html=True)


def show():
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 9 — Sections")
        st.markdown("1. Evaluation Metrics\n2. Overfitting vs Underfitting\n3. ROC Curve & AUC\n"
                    "4. Explainability (SHAP)\n5. Bias & Ethics\n6. Governance\n---\n🧩 Quiz")
        st.progress(90, text="Module 9 / 10")
    _section_metrics(); st.markdown("")
    _section_overfitting(); st.markdown("")
    _section_roc_curve(); st.markdown("")
    _section_explainability(); st.markdown("")
    _section_bias_fairness(); st.markdown("")
    _section_governance(); st.markdown("")
    _knowledge_check(); _footer()


if __name__ == "__main__":
    st.set_page_config(page_title="Module 9 – Model Evaluation & Ethics | Knowledge Folder",
                       page_icon="⚖️", layout="wide")
    show()