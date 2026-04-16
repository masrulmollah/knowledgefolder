import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
.hero-banner { background: linear-gradient(135deg, #1a0a0a 0%, #4a1010 50%, #8b1a1a 100%); padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem; border-left: 6px solid #f87171; }
.hero-title { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 0 0 0.4rem 0; }
.hero-subtitle { font-size: 1.05rem; color: #fecaca; margin: 0; }
.hero-badge { display: inline-block; background: #f87171; color: #1a0a0a; font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.7rem; border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase; }
.progress-container { background: #e9ecef; border-radius: 20px; height: 10px; margin: 0.3rem 0 0.5rem 0; }
.progress-bar { background: linear-gradient(90deg, #f87171, #8b1a1a); height: 10px; border-radius: 20px; width: 87.5%; }
.progress-label { font-size: 0.78rem; color: #6c757d; margin-bottom: 0.2rem; }
.stat-card { background: white; border: 1px solid #dee2e6; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.stat-number { font-size: 1.8rem; font-weight: 800; color: #8b1a1a; }
.stat-label { font-size: 0.78rem; color: #6c757d; margin-top: 0.2rem; }
.finance-lens { background: linear-gradient(135deg, #fff3cd, #fff8e1); border: 1px solid #ffc107; border-left: 5px solid #f5a623; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.5rem 0; }
.finance-lens-title { font-size: 0.85rem; font-weight: 700; color: #856404; text-transform: uppercase; margin-bottom: 0.4rem; }
.finance-lens-body { font-size: 0.88rem; color: #5a4200; line-height: 1.6; }
.section-heading { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #f87171; padding-bottom: 0.3rem; margin: 1.5rem 0 1rem 0; }
.risk-card { background: white; border: 1px solid #fecaca; border-left: 5px solid #f87171; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
.risk-high { border-left-color: #dc2626; }
.risk-med { border-left-color: #f59e0b; }
.risk-low { border-left-color: #16a34a; }
.reg-card { background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.6rem; }
.quiz-box { background: #fff5f5; border: 1px solid #fecaca; border-radius: 12px; padding: 1.2rem 1.4rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">🔴 Module 7 of 8 &nbsp;|&nbsp; AI Series</div>
  <div class="hero-title">AI Ethics, Risk & Governance</div>
  <div class="hero-subtitle">The responsible use of AI in finance — understand bias, hallucinations,
  explainability, model risk, data privacy, and the regulatory frameworks shaping AI in financial services.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-label">Series progress — Module 7 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="stat-card"><div class="stat-number">7</div><div class="stat-label">Risk Dimensions</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-card"><div class="stat-number">5+</div><div class="stat-label">Regulatory Frameworks</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-card"><div class="stat-number">~35</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Quiz Questions</div></div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [("1","Foundations of AI",False),("2","Machine Learning Essentials",False),("3","Deep Learning & Neural Networks",False),("4","Generative AI & LLMs",False),("5","AI in Finance & Accounting",False),("6","Building AI Models",False),("7","AI Ethics, Risk & Governance",True),("8","Future of AI & Career Readiness",False)]
    for num, name, active in modules:
        st.markdown(f"**▶ M{num} — {name}** ✅" if active else f"M{num} — {name}")
    st.markdown("---")
    st.info("💡 This module is critical for finance professionals in governance and compliance roles.")

st.markdown('<div class="section-heading">⚠️ Why AI Ethics Matters in Finance</div>', unsafe_allow_html=True)
with st.expander("📖 The Stakes of AI in Financial Decision-Making", expanded=True):
    st.markdown("""
    AI in finance makes decisions that directly affect people's financial lives — whether they get
    a loan, how their insurance is priced, whether their transaction is flagged as fraud.
    Unlike a spreadsheet error that a human reviews, AI decisions can be made at massive scale,
    at speed, without human review of each case.

    **Why ethics governance is non-negotiable in finance:**
    - **Scale:** A biased credit model affects thousands of applicants per day — not just one
    - **Asymmetry:** The person denied credit rarely knows an AI made the decision
    - **Accountability:** Regulators hold institutions — not algorithms — responsible for outcomes
    - **Complexity:** AI failures can be subtle and only visible in aggregate across populations
    - **Irreversibility:** A wrongful credit denial, loan default, or AML false positive has real consequences
    """)
    st.warning("⚠️ **Key principle:** AI does not eliminate human responsibility. The organisation that deploys an AI model is fully responsible for its outcomes — including discriminatory, inaccurate, or harmful decisions.")

st.markdown('<div class="section-heading">🎯 AI Bias — Types, Causes, and Finance Impact</div>', unsafe_allow_html=True)
with st.expander("⚖️ Understanding Bias in Financial AI Models"):
    st.markdown("""
    **What is AI bias?**
    AI bias occurs when a model systematically produces unfair or inaccurate outputs for certain
    groups or in certain conditions. Crucially, bias can occur **even without any malicious intent**
    — it emerges from data and design choices.
    """)
    bias_types = [
        ("Historical Bias", "Training data reflects past human decisions that were themselves discriminatory.", "A credit model trained on historical loan approvals will learn that certain demographics were approved at lower rates — not because they are worse credit risks, but because they were historically discriminated against. The model perpetuates this.", "High"),
        ("Representation Bias", "Certain groups are underrepresented in training data — the model has learned less about them.", "A fraud detection model trained mostly on Western transaction patterns may falsely flag transactions by customers from other regions as fraudulent.", "High"),
        ("Measurement Bias", "The features used as proxies may correlate with protected characteristics.", "Using postcode as a feature in insurance pricing correlates with race and ethnicity — perpetuating geographic redlining in a new form.", "High"),
        ("Feedback Loop Bias", "Model decisions change future data, which reinforces the original bias.", "A model that denies credit to a group generates less repayment data for that group, making future models even less confident about them — a self-reinforcing cycle.", "Medium"),
        ("Automation Bias", "Humans over-trust AI recommendations and stop exercising independent judgment.", "A credit officer rubber-stamps all AI rejections without review — the AI's biases operate without any human check.", "Medium"),
    ]
    for name, desc, finance_ex, level in bias_types:
        color = "#dc2626" if level=="High" else "#f59e0b"
        st.markdown(f"""
        <div class="risk-card">
        <b style="color:{color}">{name}</b> <span style="font-size:0.75rem;background:{color};color:white;padding:0.1rem 0.5rem;border-radius:10px">{level} Risk</span><br>
        <span style="font-size:0.87rem">{desc}</span><br>
        <span style="font-size:0.82rem;color:#5a4200">💼 Finance impact: {finance_ex}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    **How to detect and mitigate bias:**
    - **Disaggregated testing** — evaluate model performance separately for each demographic group (gender, age, ethnicity, geography)
    - **Fairness metrics** — measure equal opportunity, demographic parity, calibration across groups
    - **Diverse training data** — actively ensure training data represents all customer segments
    - **Pre-processing** — reweigh or resample training data to address imbalance
    - **Post-processing** — adjust thresholds per group to achieve fairer outcomes
    - **Human review** — always have human review for high-stakes decisions (credit denial, AML)
    """)

st.markdown('<div class="section-heading">🔮 Hallucination Risk in Financial AI</div>', unsafe_allow_html=True)
with st.expander("🚨 Managing Generative AI's Accuracy Risk"):
    st.markdown("""
    **Hallucination** is when an LLM generates plausible-sounding but factually incorrect information
    with apparent confidence. This is distinct from "being wrong" — the model doesn't know it is
    hallucinating.

    **Why hallucination occurs:**
    LLMs predict statistically likely token sequences. When they lack sufficient training signal
    for a specific fact, they generate text that fits the pattern — which may be wrong.

    **Hallucination risk assessment for finance tasks:**
    """)

    tasks = [("Drafting variance commentary from numbers you provide", "Low", "You provide all the facts; LLM only structures the language."),("Summarising a document you paste into the prompt", "Low-Medium", "Mostly summarising provided content, but may miss nuances or misrepresent details."),("Explaining accounting concepts", "Medium", "Generally reliable for well-known concepts; less so for edge cases."),("Citing specific IFRS or GAAP paragraph numbers", "High", "LLMs frequently hallucinate specific standard references. Always verify."),("Stating specific tax rates, thresholds, or deadlines", "Very High", "Tax specifics change frequently and vary by jurisdiction. Never trust without verification."),("Generating financial figures from memory", "Very High", "Do not ask LLMs to recall specific figures — they will hallucinate confidently."),("Legal or regulatory interpretation", "Very High", "Hallucinated legal citations are a serious professional risk."),]

    risk_colors = {"Low":"#16a34a","Low-Medium":"#65a30d","Medium":"#f59e0b","High":"#dc2626","Very High":"#991b1b"}
    for task, risk, note in tasks:
        color = risk_colors.get(risk,"#888")
        st.markdown(f"""
        <div style="display:flex;align-items:flex-start;gap:0.8rem;padding:0.6rem 0;border-bottom:1px solid #fee2e2">
        <span style="min-width:80px;background:{color};color:white;border-radius:8px;padding:0.15rem 0.5rem;font-size:0.75rem;font-weight:600;text-align:center">{risk}</span>
        <div><b style="font-size:0.87rem">{task}</b><br><span style="font-size:0.8rem;color:#6c757d">{note}</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    **Mitigation strategies:**
    - **Grounding** — always provide source documents; use RAG for document-based queries
    - **Verification workflow** — treat LLM output as a draft, not final; verify against primary sources
    - **Confidence indicators** — ask the model to flag when it is uncertain
    - **Source citation** — instruct the model to cite its sources; check them
    - **Human-in-the-loop** — no LLM output should go into financial records without human review
    """)
    st.error("⛔ **Non-negotiable rule:** LLM-generated financial figures, tax rates, regulatory citations, and legal interpretations must ALWAYS be verified against authoritative primary sources before use.")

st.markdown('<div class="section-heading">🔍 Explainability (XAI) in Finance</div>', unsafe_allow_html=True)
with st.expander("💡 The Right to Explanation and Model Interpretability"):
    st.markdown("""
    **Why explainability matters in finance:**
    - **Regulatory:** GDPR Article 22, Fair Credit Reporting Act, Equal Credit Opportunity Act
      require that individuals receive explanations for automated decisions affecting them
    - **Business:** Credit analysts, risk officers, and auditors need to understand why a model
      made a decision — not just what it decided
    - **Trust:** Models that cannot be explained cannot be audited, challenged, or improved

    **Explainability approaches:**
    """)
    tab1, tab2, tab3 = st.tabs(["📊 Inherently Interpretable", "🔍 Post-Hoc Local", "🌐 Post-Hoc Global"])
    with tab1:
        st.markdown("""
        **Logistic Regression**
        Each feature has a coefficient that directly states its contribution.
        *"A customer_late_rate_12m of 0.4 increases the log-odds of late payment by 0.8"*

        **Decision Tree**
        The entire decision path is visible: "IF amount > $50K AND payment_terms > 60 days THEN High Risk"

        **Scorecard Models**
        Points-based systems derived from logistic regression — interpretable by non-technical users.
        Standard in retail credit.

        **Trade-off:** Interpretable models are typically less accurate than complex ones.
        In regulated financial decisions (credit, insurance), this trade-off often favours interpretability.
        """)
    with tab2:
        st.markdown("""
        **SHAP (SHapley Additive exPlanations)**
        Explains any model's prediction by calculating each feature's contribution to that specific prediction.

        *For invoice #INV-2847 predicted as High Risk (probability 0.84):*
        - customer_late_rate_12m = 0.65 → +0.31 (strongest driver)
        - invoice_amount = $120K → +0.18
        - payment_terms_days = 90 → +0.14
        - has_po_number = False → +0.09
        - customer_relationship_years = 1 → +0.07

        *"This invoice is flagged as high risk primarily because this customer has been late 65% of the time in the past 12 months, and the invoice is large with extended payment terms."*

        **LIME (Local Interpretable Model-agnostic Explanations)**
        Fits a simple linear model locally around a specific prediction to approximate the complex model's behaviour.
        """)
    with tab3:
        st.markdown("""
        **Feature Importance Plots**
        Which features matter most across the entire model — not just one prediction.

        **Partial Dependence Plots (PDP)**
        How model predictions change as one feature varies — holding all others constant.
        *"Show me how predicted late payment probability changes as invoice amount increases"*

        **These are essential for:**
        - Model validation — does the model use features in the expected direction?
        - Regulatory review — demonstrating the model is not using prohibited variables
        - Bias detection — identifying if protected characteristics are driving decisions
        """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — The SR 11-7 / MAS TRM Standard</div>
      <div class="finance-lens-body">
        US Federal Reserve SR 11-7 and MAS Technology Risk Management guidelines require financial
        institutions to maintain comprehensive model documentation including: model purpose, methodology,
        limitations, validation results, and ongoing monitoring. Explainability is a prerequisite for
        model sign-off. Any AI model used for credit, pricing, or risk decisions must have a documented
        explanation methodology.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">🔒 Data Privacy in Financial AI</div>', unsafe_allow_html=True)
with st.expander("🛡️ PDPA, GDPR, and Data Governance for AI"):
    st.markdown("""
    AI models in finance often process sensitive personal and financial data. Key data privacy
    obligations vary by jurisdiction but share common principles:
    """)
    regs = [
        ("🇸🇬 Singapore PDPA", "Personal Data Protection Act", "Requires consent for collection and use of personal data. AI systems must not use personal data beyond the notified purpose. Data Protection Impact Assessments (DPIA) recommended for high-risk AI."),
        ("🇪🇺 GDPR (EU)", "General Data Protection Regulation", "Article 22: Right to explanation for automated decisions with significant effects. Prohibits automated decisions based solely on profiling without human review. Data minimisation principle."),
        ("🇺🇸 FCRA / ECOA (US)", "Fair Credit Reporting Act / Equal Credit Opportunity Act", "Credit decisions must be explainable. Adverse action notices required. Prohibition on discrimination based on protected characteristics."),
        ("🌐 EU AI Act", "European Union AI Act (2024)", "Classifies credit scoring, biometric systems, and employment AI as 'high-risk'. Requires conformity assessment, transparency, human oversight, and accuracy requirements before deployment."),
        ("🏦 Basel IV / BCBS 239", "Bank for International Settlements", "Data lineage, data quality, and risk data aggregation requirements applicable to AI inputs in risk models."),
    ]
    for flag_name, full_name, desc in regs:
        st.markdown(f"""
        <div class="reg-card">
        <b>{flag_name}</b> <span style="font-size:0.8rem;color:#6c757d">{full_name}</span><br>
        <span style="font-size:0.87rem">{desc}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    **Practical data privacy checklist for finance AI projects:**
    - ✅ Is consent documented for using this personal data to train AI?
    - ✅ Does the model use any sensitive data (race, gender, religion) — directly or as a proxy?
    - ✅ Has a Data Protection Impact Assessment been conducted?
    - ✅ Can individuals receive an explanation of AI decisions affecting them?
    - ✅ Is there a human review process for high-stakes AI decisions?
    - ✅ Is model training data stored securely with access controls?
    - ✅ Are data retention policies applied to training datasets?
    """)

st.markdown('<div class="section-heading">📋 Model Risk Management Framework</div>', unsafe_allow_html=True)
with st.expander("🏗️ Governing AI Models in Financial Institutions"):
    st.markdown("""
    **Model Risk Management (MRM)** is the formal governance framework for managing the risk that
    an AI/ML model may produce incorrect outputs that lead to adverse financial, regulatory, or
    reputational consequences.

    **The 3 lines of defence for AI model risk:**
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **1st Line — Model Owners**
        - Build and maintain models
        - Document methodology and assumptions
        - Monitor ongoing performance
        - Report metrics to governance
        """)
    with col2:
        st.markdown("""
        **2nd Line — Model Validation**
        - Independent review of model methodology
        - Challenger model testing
        - Bias and fairness assessment
        - Sign-off before production deployment
        """)
    with col3:
        st.markdown("""
        **3rd Line — Internal Audit**
        - Periodic audit of MRM framework
        - Verify validation is independent
        - Check regulatory compliance
        - Escalate findings to board
        """)

    st.markdown("""
    **Model inventory and documentation requirements:**

    | Document | Contents |
    |----------|---------|
    | **Model Concept Document** | Business purpose, methodology justification, data sources |
    | **Model Development Document** | Full technical specification, training data, feature engineering, results |
    | **Validation Report** | Independent testing, challenger model, sensitivity analysis, approval |
    | **Ongoing Monitoring Report** | Monthly/quarterly performance metrics, drift detection, alerts |
    | **Model Retirement Record** | When and why the model was decommissioned |
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Practical Governance for Finance Teams</div>
      <div class="finance-lens-body">
        Even a simple Excel-based ML model or AI automation script should have: (1) a document
        explaining what it does and why, (2) tested outputs, (3) a named owner responsible for
        monitoring, and (4) a defined review cycle. "Shadow AI" — models deployed informally
        without governance — is a material operational and regulatory risk.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">🌐 Regulatory Landscape — AI in Financial Services</div>', unsafe_allow_html=True)
with st.expander("📜 What Regulators Are Saying About AI"):
    st.markdown("""
    **Key regulatory developments (as at 2024–2025):**

    **EU AI Act (2024)**
    The world's first comprehensive AI regulation. Classifies AI systems by risk level:
    - *Prohibited* — social scoring, real-time facial recognition
    - *High-risk* — credit scoring, employment, education (requires conformity assessment, transparency)
    - *Limited risk* — chatbots (transparency disclosure)
    - *Minimal risk* — spam filters, AI in video games

    **US Federal Guidance**
    - SR 11-7 (Federal Reserve) — Model risk management framework, applies to ML models
    - Executive Order on AI (Oct 2023) — Directs federal agencies to issue AI guidance for financial sector
    - CFPB guidance — AI credit decisions must be explainable; adverse action notices required

    **Singapore MAS**
    - Fairness, Ethics, Accountability, Transparency (FEAT) principles for financial AI
    - Veritas initiative — toolkit for assessing fairness in credit scoring and financial AI
    - TRM Guidelines — Technology Risk Management includes AI model risk

    **UK FCA / PRA**
    - DP5/22 — Discussion paper on AI and ML in financial services
    - Principles: safe, ethical, accountable AI

    **IOSCO / FSB**
    - International regulatory coordination on AI risks in capital markets
    - Focus on algorithmic trading, model risk, systemic risk from correlated AI models
    """)
    st.info("💡 **Regulatory trend:** Global regulators are converging on the same requirements: transparency, explainability, fairness, human oversight, and model risk management. Finance professionals need to embed these into AI projects from day one.")

# Interactive Risk Assessment Tool
st.markdown('<div class="section-heading">🔧 Interactive: AI Project Risk Checker</div>', unsafe_allow_html=True)
with st.expander("✅ Assess the Risk Level of Your AI Project"):
    st.markdown("Answer these questions to get a quick risk assessment of an AI project:")
    q1 = st.selectbox("1. Does this AI make or influence decisions about individuals (credit, hiring, pricing)?", ["No — purely internal operations", "Yes — affects individual customers or employees"])
    q2 = st.selectbox("2. Does the model use personal data (name, address, transaction history, demographics)?", ["No personal data used", "Yes — personal financial data", "Yes — including sensitive data (demographics, health)"])
    q3 = st.selectbox("3. How interpretable is the output?", ["Fully interpretable (scorecard, logistic regression)", "Partially interpretable (tree, SHAP available)", "Black box (deep neural network, no XAI)"])
    q4 = st.selectbox("4. Is there human review before the decision takes effect?", ["Yes — always, every decision", "Yes — for flagged cases only", "No — fully automated, no human review"])
    q5 = st.selectbox("5. Is there ongoing monitoring and a retraining protocol?", ["Yes — formal process in place", "Informal monitoring only", "No monitoring"])

    if st.button("🔍 Assess Risk Level"):
        score = 0
        if "Yes — affects individual" in q1: score += 3
        if "personal financial data" in q2: score += 2
        if "sensitive data" in q2: score += 3
        if "Black box" in q3: score += 3
        if "Partially" in q3: score += 1
        if "flagged cases only" in q4: score += 2
        if "No — fully automated" in q4: score += 4
        if "Informal" in q5: score += 1
        if "No monitoring" in q5: score += 2

        if score <= 3:
            st.success("🟢 **Low Risk** — Good governance practices appear to be in place. Maintain documentation and monitor regularly.")
        elif score <= 8:
            st.warning("🟡 **Medium Risk** — Some governance gaps identified. Consider strengthening explainability, adding human review for high-stakes cases, and formalising monitoring.")
        else:
            st.error("🔴 **High Risk** — Significant governance concerns. This project may require formal model validation, legal/compliance review, and possibly a Data Protection Impact Assessment before deployment.")
        st.caption("Note: This is a simplified educational tool, not a substitute for formal risk assessment.")

# Quiz
st.markdown('<div class="section-heading">🧩 Knowledge Check</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {"q": "A bank's credit scoring model trained on 10 years of historical loan data consistently approves fewer applicants from a specific ethnic group. Despite no explicit ethnicity variable in the model, this is an example of:", "options": ["Automation bias", "Historical bias — the model has learned past discriminatory lending patterns", "Measurement error in the training data", "Overfitting to the training set"], "answer": "Historical bias — the model has learned past discriminatory lending patterns", "explanation": "Historical bias occurs when training data reflects past human decisions that were discriminatory. Even without an explicit ethnicity variable, correlated features (postcode, education, employment history) can encode the same patterns."},
    {"q": "Under GDPR Article 22, individuals subject to automated decisions with significant legal effects have:", "options": ["No specific rights — automated decisions are treated the same as human decisions", "The right to human review, explanation, and to contest the decision", "The right to see the model's source code", "Only the right to be informed that AI was used"], "answer": "The right to human review, explanation, and to contest the decision", "explanation": "GDPR Article 22 grants individuals the right not to be subject to solely automated decisions with significant effects, and where such decisions occur, the right to obtain human intervention, express their point of view, and contest the decision."},
    {"q": "SHAP (SHapley Additive exPlanations) is used in AI model governance primarily to:", "options": ["Speed up model training", "Explain why a model made a specific prediction by quantifying each feature's contribution", "Replace the need for model validation", "Detect overfitting during training"], "answer": "Explain why a model made a specific prediction by quantifying each feature's contribution", "explanation": "SHAP provides local explanations — for any individual prediction, it quantifies how much each feature contributed to pushing the prediction above or below the baseline. Essential for explaining credit decisions."},
    {"q": "An AI chatbot used by a bank's customer service team gives a customer a confidently-stated but incorrect tax rate on savings interest. This is an example of:", "options": ["Bias", "Hallucination", "Distribution shift", "Overfitting"], "answer": "Hallucination", "explanation": "Hallucination is when an LLM generates factually incorrect information with apparent confidence. This is a critical risk in financial services — incorrect tax or regulatory information given to customers has serious professional and compliance consequences."},
    {"q": "Under the EU AI Act, AI systems used for credit scoring are classified as:", "options": ["Minimal risk — no special requirements", "Limited risk — transparency disclosure only", "High-risk — requiring conformity assessment, transparency, and human oversight", "Prohibited — not permitted in the EU"], "answer": "High-risk — requiring conformity assessment, transparency, and human oversight", "explanation": "The EU AI Act classifies credit scoring as a high-risk AI application due to its significant impact on individuals' financial lives. High-risk applications require conformity assessment, technical documentation, transparency to affected individuals, and meaningful human oversight."},
]

for key in ["m7_q_index","m7_score","m7_answered","m7_selected","m7_quiz_done"]:
    if key not in st.session_state: st.session_state[key] = 0 if "index" in key or "score" in key else False

if not st.session_state.m7_quiz_done:
    q_data = questions[st.session_state.m7_q_index]
    st.markdown(f"**Question {st.session_state.m7_q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")
    choice = st.radio("Select your answer:", q_data["options"], key=f"m7_q_{st.session_state.m7_q_index}")
    col_s, col_n = st.columns(2)
    with col_s:
        if st.button("✅ Submit", key=f"m7_sub_{st.session_state.m7_q_index}"):
            st.session_state.m7_answered = True; st.session_state.m7_selected = choice
            if choice == q_data["answer"]: st.session_state.m7_score += 1
    if st.session_state.m7_answered:
        if st.session_state.m7_selected == q_data["answer"]: st.success(f"✅ Correct! {q_data['explanation']}")
        else: st.error(f"❌ Answer: **{q_data['answer']}** — {q_data['explanation']}")
        with col_n:
            if st.session_state.m7_q_index < len(questions)-1:
                if st.button("Next ➡️", key=f"m7_next_{st.session_state.m7_q_index}"):
                    st.session_state.m7_q_index += 1; st.session_state.m7_answered = False; st.rerun()
            else:
                if st.button("🏁 Results"): st.session_state.m7_quiz_done = True; st.rerun()
else:
    s,t = st.session_state.m7_score, len(questions); pct = int((s/t)*100)
    st.markdown(f"### {'🏆' if pct>=80 else '👍' if pct>=60 else '📚'} Score: {s}/{t} ({pct}%)")
    st.progress(pct/100)
    st.info("Excellent!" if pct>=80 else "Good — review the regulatory frameworks." if pct>=60 else "Revisit the bias and explainability sections.")
    if st.button("🔄 Retry"):
        for k,v in [("m7_q_index",0),("m7_score",0),("m7_answered",False),("m7_selected",None),("m7_quiz_done",False)]: st.session_state[k]=v
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">💡 Key Takeaways</div>', unsafe_allow_html=True)
for i,t in enumerate(["**AI bias** can emerge without any malicious intent — from historical data, proxy variables, and feedback loops. Disaggregated testing by demographic group is essential.","**Hallucination** in LLMs is a systemic issue — never use AI-generated financial figures, tax rates, or regulatory citations without verification against primary sources.","**Explainability** (SHAP, LIME, scorecards) is a regulatory requirement for credit, insurance, and employment AI decisions — not optional.","**Model Risk Management** requires documentation, independent validation, ongoing monitoring, and defined ownership for every AI model in production.","The **EU AI Act** classifies credit scoring as high-risk, requiring conformity assessment and human oversight. Singapore's MAS FEAT principles and Veritas toolkit provide the regional framework.","**Data privacy** (PDPA, GDPR) requires consent, purpose limitation, and data minimisation for personal data used in AI training — compliance must be built in from the start."],1):
    st.markdown(f"**{i}.** {t}")

st.markdown("---")
col1,col2,col3 = st.columns(3)
with col1:
    if st.button("⬅️ M6: Building Models", use_container_width=True): st.info("Navigate to Module 6 from the sidebar.")
with col2: st.markdown("<div style='text-align:center;padding-top:0.4rem'>🔴 Module 7 of 8</div>", unsafe_allow_html=True)
with col3:
    if st.button("M8: Future of AI ➡️", use_container_width=True): st.info("Navigate to Module 8 from the sidebar.")
st.caption("Knowledge Folder · AI Series · Module 7 — AI Ethics, Risk & Governance · © 2025")