import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
.hero-banner { background: linear-gradient(135deg, #0c0c1e 0%, #1a1a3e 40%, #2d2d6b 70%, #4040a0 100%); padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem; border-left: 6px solid #a78bfa; }
.hero-title { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 0 0 0.4rem 0; }
.hero-subtitle { font-size: 1.05rem; color: #ddd6fe; margin: 0; }
.hero-badge { display: inline-block; background: #a78bfa; color: #0c0c1e; font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.7rem; border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase; }
.progress-container { background: #e9ecef; border-radius: 20px; height: 10px; margin: 0.3rem 0 0.5rem 0; }
.progress-bar { background: linear-gradient(90deg, #a78bfa, #4040a0); height: 10px; border-radius: 20px; width: 100%; }
.progress-label { font-size: 0.78rem; color: #6c757d; margin-bottom: 0.2rem; }
.stat-card { background: white; border: 1px solid #dee2e6; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.stat-number { font-size: 1.8rem; font-weight: 800; color: #4040a0; }
.stat-label { font-size: 0.78rem; color: #6c757d; margin-top: 0.2rem; }
.finance-lens { background: linear-gradient(135deg, #fff3cd, #fff8e1); border: 1px solid #ffc107; border-left: 5px solid #f5a623; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.5rem 0; }
.finance-lens-title { font-size: 0.85rem; font-weight: 700; color: #856404; text-transform: uppercase; margin-bottom: 0.4rem; }
.finance-lens-body { font-size: 0.88rem; color: #5a4200; line-height: 1.6; }
.section-heading { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #a78bfa; padding-bottom: 0.3rem; margin: 1.5rem 0 1rem 0; }
.trend-card { background: white; border: 1px solid #ede9fe; border-left: 5px solid #a78bfa; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
.career-card { background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.6rem; }
.skill-pill { display: inline-block; background: #ede9fe; color: #4040a0; border: 1px solid #c4b5fd; border-radius: 20px; padding: 0.2rem 0.75rem; font-size: 0.8rem; font-weight: 600; margin: 0.2rem; }
.quiz-box { background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 12px; padding: 1.2rem 1.4rem; }
.complete-banner { background: linear-gradient(135deg, #1a3a1a, #2d6a2d); border: 2px solid #4ade80; border-radius: 16px; padding: 1.5rem 2rem; text-align: center; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">🏆 Module 8 of 8 &nbsp;|&nbsp; Final Module — AI Series</div>
  <div class="hero-title">The Future of AI & Career Readiness</div>
  <div class="hero-subtitle">Look ahead at emerging AI trends reshaping finance — agentic AI,
  multimodal models, AI + blockchain — and build your personal roadmap for staying relevant in an AI-driven profession.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-label">Series progress — Module 8 of 8 — Final Module! 🎉</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="stat-card"><div class="stat-number">8</div><div class="stat-label">Emerging Trends</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-card"><div class="stat-number">3</div><div class="stat-label">Career Pathways</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-card"><div class="stat-number">~35</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-card"><div class="stat-number">✅</div><div class="stat-label">Series Complete</div></div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [("1","Foundations of AI",False),("2","Machine Learning Essentials",False),("3","Deep Learning & Neural Networks",False),("4","Generative AI & LLMs",False),("5","AI in Finance & Accounting",False),("6","Building AI Models",False),("7","AI Ethics, Risk & Governance",False),("8","Future of AI & Career Readiness",True)]
    for num, name, active in modules:
        st.markdown(f"**▶ M{num} — {name}** ✅" if active else f"M{num} — {name} ✅")
    st.markdown("---")
    st.success("🎉 You've reached the final module!")

st.markdown('<div class="section-heading">🚀 Emerging AI Trends in Finance</div>', unsafe_allow_html=True)
with st.expander("🔮 The Next Wave — 8 Trends Shaping Finance AI", expanded=True):
    trends = [
        ("1. Agentic AI", "🤖", "AI that can autonomously plan and execute multi-step tasks — not just answer questions.", "An AI agent given the task 'prepare the monthly management accounts' can: pull data from ERP, run reconciliations, generate variance commentary, format the report, and email it to reviewers — with minimal human instruction.", "2024–2026 — Early enterprise deployments underway"),
        ("2. Multimodal AI", "👁️", "AI that processes and generates text, images, audio, and video together.", "Reading a board presentation (slides + narrative), analysing financial charts visually, processing audio from earnings calls alongside transcripts — unified understanding of multiple data types.", "2024 — GPT-4V, Gemini Ultra already deployed"),
        ("3. AI + Blockchain / DLT", "🔗", "Combining AI's analytical power with blockchain's immutable audit trail.", "Smart contracts that automatically trigger payments when AI confirms delivery conditions are met. AI auditing of DeFi protocols. Automated regulatory reporting with cryptographic proof of data integrity.", "2025–2027 — Experimental, growing in trade finance"),
        ("4. Quantum AI", "⚛️", "Quantum computing accelerating AI training and optimisation problems.", "Portfolio optimisation across thousands of assets simultaneously. Monte Carlo simulations running orders of magnitude faster. Breaking current encryption (requiring post-quantum cryptography in finance).", "2028–2035 — Longer horizon, but planning now"),
        ("5. Federated Learning", "🔒", "Training AI models across distributed data sources without centralising sensitive data.", "Multiple banks collaborating to train a shared AML model without sharing customer transaction data with each other. Privacy-preserving consortium AI.", "2024–2026 — MAS and global regulators actively exploring"),
        ("6. AI-Native Finance Platforms", "🏗️", "Finance tools built from the ground up with AI as the core architecture, not a feature add-on.", "Platforms where forecasting, reporting, and analysis are AI-generated by default — the human role shifts to reviewing, challenging, and directing AI outputs.", "2025–2028 — Next-gen vendors emerging"),
        ("7. Autonomous AI CFO Tools", "📊", "AI systems that handle entire finance workflows with human approval at key checkpoints only.", "AI that manages the complete order-to-cash cycle, flags exceptions, and proposes strategies — the finance professional becomes a supervisor of AI workflows rather than executor.", "2026–2030 — Depends on trust and governance maturity"),
        ("8. AI + ESG & Sustainability Reporting", "🌱", "AI extracting, verifying, and reporting sustainability data with the same rigour as financial data.", "Automated ESG data collection from supply chains, AI-verified sustainability KPIs, real-time carbon accounting integrated with the financial close.", "2024–2026 — Driven by ISSB and CSRD requirements"),
    ]
    tab_labels = [t[0] for t in trends]
    tabs = st.tabs([t[:20] + "..." if len(t) > 20 else t for t in tab_labels])
    for i, (name, icon, desc, finance_ex, timeline) in enumerate(trends):
        with tabs[i]:
            st.markdown(f"### {icon} {name}")
            st.markdown(f"**{desc}**")
            st.markdown(f"""
            <div class="finance-lens">
              <div class="finance-lens-title">💼 Finance Application</div>
              <div class="finance-lens-body">{finance_ex}</div>
            </div>
            """, unsafe_allow_html=True)
            st.caption(f"⏱️ Timeline: {timeline}")

st.markdown('<div class="section-heading">🔮 Agentic AI — A Deeper Dive</div>', unsafe_allow_html=True)
with st.expander("🤖 Why Agentic AI is the Biggest Near-Term Shift for Finance"):
    st.markdown("""
    **What makes AI "agentic"?**
    Current AI tools respond to one query at a time — they are reactive. **Agentic AI** can:
    - Decompose a complex goal into subtasks
    - Plan a sequence of actions to achieve the goal
    - Execute those actions using tools (web browsing, code execution, API calls)
    - Monitor progress and adapt the plan when things change
    - Complete multi-step tasks with minimal human involvement

    **The finance agent stack:**
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Today's Finance AI:**
        - *"Summarise this document"* → AI responds
        - *"Write a formula"* → AI responds
        - *"Explain this variance"* → AI responds
        - Human does all the orchestration between steps
        """)
    with col2:
        st.markdown("""
        **Agentic Finance AI:**
        - *"Prepare the monthly close pack"*
        - Agent pulls data, runs reconciliations, generates commentary, formats report, sends for review
        - Human reviews and approves the final output
        """)
    st.markdown("""
    **Agentic AI finance use cases emerging now:**

    | Task | What the Agent Does | Human Role |
    |------|--------------------|----|
    | Month-end close | Pull data, post journals, reconcile, draft commentary | Review and approve |
    | Expense audit | Review all expenses, flag policy violations, draft findings | Approve findings |
    | Tax compliance | Collect data, calculate liability, draft returns | Review and sign |
    | FX hedging | Monitor exposure, propose hedge ratio, execute trades | Approve strategy |
    | Investor reporting | Pull metrics, generate narrative, format presentation | Review and present |

    **Current limitations of agentic AI:**
    - Hallucination risk multiplies across long task chains
    - Difficult to audit — hard to trace which step introduced an error
    - Security risks — agents with tool access can cause unintended actions
    - Regulatory acceptance still developing
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — The Governance Imperative</div>
      <div class="finance-lens-body">
        Agentic AI raises the governance stakes significantly. When an AI agent executes a payment,
        posts a journal entry, or files a return — who is responsible for errors? Finance teams
        adopting agentic AI need clear accountability frameworks, approval workflows, and audit
        trails before deployment. The CFO remains responsible regardless of which AI made the action.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">👔 The Finance Professional in an AI World</div>', unsafe_allow_html=True)
with st.expander("📊 Which Roles Are Enhanced, Which Are At Risk?"):
    st.markdown("""
    The most common question: *"Will AI take my job?"*
    The honest answer: AI will significantly change most finance roles — but elimination is far less
    likely than transformation. The risk is not replacement; it is **skill obsolescence**.
    """)
    import pandas as pd
    df = pd.DataFrame({
        "Finance Activity": [
            "Manual data entry and reconciliation",
            "Standard report generation",
            "Variance calculation",
            "Compliance checklist processing",
            "Journal entry preparation (routine)",
            "Business partnering and insight generation",
            "Strategic financial advice",
            "Stakeholder relationships",
            "Complex technical accounting judgments",
            "AI model governance and oversight",
            "Cross-functional project leadership",
            "Ethics and professional accountability",
        ],
        "AI Impact": [
            "🔴 High automation — largely replaced by AI",
            "🔴 High automation — AI generates reports faster",
            "🔴 High automation — AI calculates instantly",
            "🟠 Significant automation — AI handles routine checks",
            "🟠 Significant automation — AI posts standard entries",
            "🟡 Enhanced by AI — more time available, AI provides data",
            "🟢 Enhanced — AI provides analysis, human provides wisdom",
            "🟢 Not automated — human relationships are irreplaceable",
            "🟢 Enhanced but not replaced — judgment still required",
            "🟢 New demand — finance professionals govern AI",
            "🟢 Not automated — requires human coordination",
            "🟢 Essential — AI is not accountable, humans are",
        ],
        "Action": [
            "Minimise time here — automate with AI tools",
            "Use AI tools; focus on quality review",
            "Automate; focus on explaining variances",
            "Automate; focus on exceptions",
            "Automate; focus on complex journals",
            "Invest heavily here — this is your future value",
            "Build this skill — it's increasingly premium",
            "Invest — not replicable by AI",
            "Maintain deep technical knowledge",
            "Build AI governance skills — new demand",
            "Develop leadership skills",
            "Maintain high professional standards",
        ]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.warning("⚠️ **The real risk:** A finance professional who continues to spend 60% of their time on data entry and report generation will be displaced. One who uses AI to handle those tasks and spends that time on analysis, business partnering, and AI oversight will be significantly more valuable.")

st.markdown('<div class="section-heading">🎯 Skills Finance Professionals Need for the AI Era</div>', unsafe_allow_html=True)
with st.expander("📚 Your AI Skills Roadmap"):
    tab1, tab2, tab3 = st.tabs(["🟢 AI Literacy (Everyone)", "🔵 AI Application (Senior)", "🟣 AI Leadership (Finance Leaders)"])
    with tab1:
        st.markdown("#### For Every Finance Professional")
        st.markdown("These skills are now baseline requirements — equivalent to Excel competency a decade ago.")
        skills = [
            ("AI Concepts & Vocabulary", "Understand what ML, LLMs, RAG, hallucination, and bias mean — well enough to participate in AI project discussions."),
            ("Prompt Engineering", "Craft effective prompts for ChatGPT, Claude, and Copilot to get high-quality outputs for financial tasks."),
            ("AI Tool Proficiency", "Use Microsoft Copilot in Excel and Word, your ERP's AI features, and relevant specialist tools."),
            ("AI Output Verification", "Know when to trust AI and when to verify. Understand hallucination risk by task type."),
            ("Data Literacy", "Read and interpret data outputs, understand distributions, and evaluate ML model outputs."),
            ("AI Ethics Awareness", "Understand bias, fairness, and governance principles sufficient to raise concerns when needed."),
        ]
        for skill, desc in skills:
            st.markdown(f"**{skill}**")
            st.markdown(f"> {desc}")
        st.markdown("**Recommended resources:**")
        resources = ["Microsoft Learn — Copilot for Finance (free)","Coursera — AI For Everyone (Andrew Ng, free audit)","ACCA/CIMA AI for Finance (CPD modules)","Anthropic — Prompt Engineering Guide (free)","Kaggle — Intro to Machine Learning (free)"]
        for r in resources: st.markdown(f"  - {r}")

    with tab2:
        st.markdown("#### For Senior Finance Professionals and Specialists")
        skills = [
            ("AI Project Specification", "Define AI use cases, success metrics, data requirements, and governance needs for finance projects."),
            ("ML Model Evaluation", "Read and challenge ML model documentation — understand AUC, precision/recall, confusion matrices."),
            ("Data Analysis with Python/SQL", "Basic Python (pandas, visualisation) and SQL for data extraction and analysis."),
            ("RAG Implementation Basics", "Understand how to connect LLMs to internal financial document repositories."),
            ("AI Vendor Assessment", "Evaluate AI tool vendors — assess data privacy, model risk, integration capabilities."),
            ("Model Risk Oversight", "Apply Model Risk Management principles to AI models in your function."),
        ]
        for skill, desc in skills:
            st.markdown(f"**{skill}**")
            st.markdown(f"> {desc}")
        st.markdown("**Recommended resources:**")
        resources = ["Coursera — Machine Learning Specialization (Andrew Ng)","DataCamp — Data Analyst with Python track","Google Cloud — Professional Data Analyst certification","GARP — Financial Risk Manager (FRM) covers model risk"]
        for r in resources: st.markdown(f"  - {r}")

    with tab3:
        st.markdown("#### For CFOs, Finance Directors, and Heads of Finance")
        skills = [
            ("AI Strategy and Roadmapping", "Develop a function-wide AI adoption roadmap aligned to business strategy."),
            ("AI Governance Framework Design", "Establish model risk management, AI ethics, and data governance frameworks."),
            ("Change Management for AI", "Lead organisational change as AI transforms finance team structures and workflows."),
            ("AI Investment Evaluation", "Build business cases for AI investments — TCO, ROI, risk-adjusted return."),
            ("Regulatory Engagement", "Understand emerging AI regulations and represent finance in regulatory discussions."),
            ("Board-level AI Communication", "Communicate AI risk, opportunity, and governance to boards and audit committees."),
        ]
        for skill, desc in skills:
            st.markdown(f"**{skill}**")
            st.markdown(f"> {desc}")
        st.markdown("**Recommended resources:**")
        resources = ["MIT Sloan — AI Strategy for Business (online)","INSEAD — Leading Digital Transformation","Deloitte AI Institute — CFO Perspectives (free reports)","WEF — Future of Jobs in Financial Services (free)"]
        for r in resources: st.markdown(f"  - {r}")

st.markdown('<div class="section-heading">📅 Staying Current — Continuous Learning Strategy</div>', unsafe_allow_html=True)
with st.expander("🔄 How to Keep Up with AI in Finance"):
    st.markdown("""
    AI is evolving faster than any previous technology. A structured approach to continuous
    learning is essential — ad-hoc reading is insufficient.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Daily (10 minutes):**
        - Scan AI headlines: The Rundown, AI Breakfast, Morning Brew AI
        - Follow on LinkedIn: key AI in finance voices, vendor blogs

        **Weekly (30 minutes):**
        - Try a new AI prompt in your workflow
        - Read one AI in finance research piece (Deloitte, McKinsey, PwC AI Institutes)
        - Experiment with new tool features (Copilot updates, LLM new capabilities)

        **Monthly (2–4 hours):**
        - Complete one CPD module on AI (ACCA, CIMA, or LinkedIn Learning)
        - Attend one webinar or online event on AI in finance
        - Review performance of any AI tools you are using
        """)
    with col2:
        st.markdown("""
        **Quarterly:**
        - Map new AI capabilities to your specific role — what can I automate or improve?
        - Update your team's AI usage inventory
        - Review regulatory updates (EU AI Act implementation, MAS circulars, SEC guidance)

        **Annually:**
        - Complete a formal AI certification or course
        - Update your personal AI skills roadmap
        - Review your function's AI strategy and tool landscape

        **Key publications to follow:**
        - McKinsey Global Institute — AI in Finance
        - Deloitte AI Institute
        - ACCA / ICAEW AI research
        - MAS Technology Bulletins
        - MIT Technology Review — Finance AI
        """)

# Personal Action Plan Builder
st.markdown('<div class="section-heading">🗺️ Build Your Personal AI Action Plan</div>', unsafe_allow_html=True)
with st.expander("✅ Interactive: Your 90-Day AI Adoption Plan"):
    st.markdown("Answer these questions to get a personalised starting point:")

    role_level = st.selectbox("Your current role level:", ["Graduate / Early career (0–3 years)", "Mid-level analyst / accountant (3–8 years)", "Senior / Manager (8–15 years)", "Director / CFO (15+ years)"])
    current_tools = st.multiselect("Which AI tools do you currently use?", ["Microsoft Copilot", "ChatGPT / Claude / Gemini", "Xero / MYOB AI features", "SAP / Oracle AI", "Alteryx", "Power BI AI features", "None yet"])
    priority_area = st.selectbox("Which area do you most want to develop?", ["Using AI for everyday finance tasks", "Understanding ML models for risk/audit work", "Building AI business cases", "AI governance and ethics", "AI strategy and leadership"])
    time_available = st.selectbox("Hours per week available for AI learning:", ["< 1 hour", "1–3 hours", "3–5 hours", "5+ hours"])

    if st.button("🎯 Generate My 90-Day Plan"):
        st.markdown("### 📋 Your Personalised 90-Day AI Action Plan")
        if "None yet" in current_tools or not current_tools:
            st.markdown("**Month 1 — Foundation:**")
            st.markdown("- Install and activate Microsoft Copilot in your Microsoft 365 suite\n- Complete Microsoft's 'Copilot for Finance' free learning path (4 hours)\n- Use Copilot for one task each day: email drafting, Excel formulas, meeting summaries\n- Read: 'AI For Everyone' by Andrew Ng (Coursera — free audit, 6 hours)")
        else:
            st.markdown("**Month 1 — Deepen Existing Tool Usage:**")
            st.markdown("- Identify your top 3 repetitive finance tasks and build AI prompts for each\n- Share your best prompts with your team\n- Complete one advanced module on your most-used tool")
        if "Using AI for everyday" in priority_area:
            st.markdown("**Month 2 — Applied Automation:**")
            st.markdown("- Build a prompt library of 10 finance-specific prompts for your role\n- Automate your most time-consuming report using AI + Copilot\n- Set up a RAG experiment: try AI Q&A on your own procedure documents\n- Measure time saved: document hours recovered per week")
        elif "ML models" in priority_area:
            st.markdown("**Month 2 — ML Model Literacy:**")
            st.markdown("- Complete Module 2 (ML Essentials) from this series in depth\n- Read your firm's model risk policy — map to what you've learned\n- Ask your data science or IT team to walk you through a model in production\n- Study: 'Interpretable Machine Learning' (Molnar, free online)")
        elif "governance" in priority_area or "ethics" in priority_area:
            st.markdown("**Month 2 — Governance Deep Dive:**")
            st.markdown("- Review EU AI Act summary for financial services\n- Read MAS FEAT principles and Veritas toolkit documentation\n- Map your firm's current AI deployments to governance requirements\n- Propose an AI model inventory template to your manager")
        st.markdown("**Month 3 — Build and Share:**")
        st.markdown(f"- Deliver a 15-minute lunch-and-learn on AI for your finance team\n- Identify one AI project to sponsor or champion in your function\n- Achieve one certification: Microsoft AI-900, Google AI Essentials, or ACCA AI CPD module\n- Schedule your first quarterly review of AI strategy for your role")
        if "< 1" in time_available:
            st.info("💡 With less than 1 hour per week: focus on the daily habit — use AI for one task per day. Small, consistent practice compounds rapidly.")
        elif "5+" in time_available:
            st.success("🚀 With 5+ hours per week: you can move through this series, complete a formal certification, and be in a position to lead AI initiatives within 6 months.")

# Job market
st.markdown('<div class="section-heading">💼 The AI-Transformed Finance Job Market</div>', unsafe_allow_html=True)
with st.expander("📈 New Roles, Enhanced Roles, and Evolving Expectations"):
    st.markdown("""
    **New roles emerging in finance driven by AI:**
    """)
    new_roles = [
        ("Finance AI Lead / CFO of AI", "Owns the AI transformation roadmap for the finance function. Bridges finance domain expertise and AI capabilities. Reports to CFO."),
        ("AI Model Risk Analyst (Finance)", "Validates and monitors ML models used in financial decisions. Combines quantitative skills with model governance."),
        ("Finance Data Scientist", "Builds predictive models for FP&A, credit, fraud, and treasury. Requires Python/R + finance domain knowledge."),
        ("AI-Augmented FP&A Analyst", "Uses AI tools to run advanced scenario modelling, automated forecasting, and AI-generated commentary. The 'new' management accountant."),
        ("Prompt Engineer (Finance)", "Designs and maintains prompt libraries, RAG systems, and AI workflows for finance-specific applications."),
        ("AI Compliance / Ethics Officer (Finance)", "Ensures AI tools in finance comply with regulations — GDPR, EU AI Act, MAS FEAT. Growing rapidly."),
    ]
    for role, desc in new_roles:
        st.markdown(f"""
        <div class="career-card">
        <b>{role}</b><br>
        <span style="font-size:0.87rem">{desc}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    **Skills employers are now adding to finance job descriptions:**
    """)
    skills_list = ["AI / ML literacy","Prompt engineering","Python or R","Power BI / Tableau","SQL","Data storytelling","Copilot proficiency","Model risk awareness","AI governance","Digital transformation leadership"]
    st.markdown(" ".join([f'<span class="skill-pill">{s}</span>' for s in skills_list]), unsafe_allow_html=True)

# Quiz
st.markdown('<div class="section-heading">🧩 Final Knowledge Check — Series Capstone</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {"q": "Agentic AI differs from current AI tools primarily because:", "options": ["It uses more computing power", "It can plan and execute multi-step tasks autonomously, not just respond to individual queries", "It is only available to large enterprises", "It doesn't require training data"], "answer": "It can plan and execute multi-step tasks autonomously, not just respond to individual queries", "explanation": "Agentic AI can decompose complex goals into subtasks, plan sequences of actions, use tools (APIs, code execution), and execute multi-step workflows with minimal human intervention — a fundamental shift from reactive to proactive AI."},
    {"q": "Which AI trend allows multiple banks to train a shared fraud model without sharing each other's customer transaction data?", "options": ["Quantum AI", "Federated Learning", "Multimodal AI", "Agentic AI"], "answer": "Federated Learning", "explanation": "Federated Learning trains models across distributed data sources — each bank trains locally on its own data and shares only model updates (gradients), not raw data. Ideal for privacy-sensitive financial data collaboration."},
    {"q": "A CFO is asked by the board: 'An AI system posted a journal entry incorrectly. Who is responsible?' The correct answer is:", "options": ["The AI system itself is responsible", "The data scientist who built the model", "The CFO and the organisation that deployed the AI — human accountability cannot be delegated to AI", "The software vendor who sold the tool"], "answer": "The CFO and the organisation that deployed the AI — human accountability cannot be delegated to AI", "explanation": "AI does not hold professional or legal accountability. The organisation that deploys AI is responsible for its outputs. Finance leaders must maintain oversight and governance structures that preserve human accountability."},
    {"q": "Which of the following finance activities is LEAST likely to be automated by AI in the next 5–10 years?", "options": ["Standard report generation", "Manual data entry and reconciliation", "Strategic financial advice and stakeholder relationships", "Routine journal entry preparation"], "answer": "Strategic financial advice and stakeholder relationships", "explanation": "AI excels at pattern recognition, processing, and generation of structured outputs. Strategic advice requires contextual judgment, relationship trust, ethical accountability, and understanding of complex organisational dynamics — capabilities that remain distinctly human."},
    {"q": "A finance professional wants to stay current with AI developments. Which approach is MOST effective for long-term AI literacy?", "options": ["Read one comprehensive AI book each year", "Complete one online course and consider the topic covered", "Daily habit of brief AI exposure + monthly structured learning + quarterly skills application", "Wait for employers to provide mandatory AI training"], "answer": "Daily habit of brief AI exposure + monthly structured learning + quarterly skills application", "explanation": "AI is evolving at a pace that makes one-time learning obsolete quickly. A consistent multi-cadence approach — daily exposure, monthly structured learning, quarterly application and reflection — builds durable, adaptive AI literacy."},
]

for key in ["m8_q_index","m8_score","m8_answered","m8_selected","m8_quiz_done"]:
    if key not in st.session_state: st.session_state[key] = 0 if "index" in key or "score" in key else False

if not st.session_state.m8_quiz_done:
    q_data = questions[st.session_state.m8_q_index]
    st.markdown(f"**Question {st.session_state.m8_q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")
    choice = st.radio("Select your answer:", q_data["options"], key=f"m8_q_{st.session_state.m8_q_index}")
    col_s, col_n = st.columns(2)
    with col_s:
        if st.button("✅ Submit", key=f"m8_sub_{st.session_state.m8_q_index}"):
            st.session_state.m8_answered = True; st.session_state.m8_selected = choice
            if choice == q_data["answer"]: st.session_state.m8_score += 1
    if st.session_state.m8_answered:
        if st.session_state.m8_selected == q_data["answer"]: st.success(f"✅ Correct! {q_data['explanation']}")
        else: st.error(f"❌ Answer: **{q_data['answer']}** — {q_data['explanation']}")
        with col_n:
            if st.session_state.m8_q_index < len(questions)-1:
                if st.button("Next ➡️", key=f"m8_next_{st.session_state.m8_q_index}"):
                    st.session_state.m8_q_index += 1; st.session_state.m8_answered = False; st.rerun()
            else:
                if st.button("🏁 Final Results"): st.session_state.m8_quiz_done = True; st.rerun()
else:
    s,t = st.session_state.m8_score, len(questions); pct = int((s/t)*100)
    st.markdown(f"### {'🏆' if pct>=80 else '👍' if pct>=60 else '📚'} Score: {s}/{t} ({pct}%)")
    st.progress(pct/100)
    st.info("Outstanding — you're well prepared for the AI era!" if pct>=80 else "Good — review the agentic AI and career sections." if pct>=60 else "Revisit the emerging trends and revisit earlier modules for reinforcement.")
    if st.button("🔄 Retry"):
        for k,v in [("m8_q_index",0),("m8_score",0),("m8_answered",False),("m8_selected",None),("m8_quiz_done",False)]: st.session_state[k]=v
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">💡 Key Takeaways — Module 8 & Series</div>', unsafe_allow_html=True)
for i,t in enumerate(["**Agentic AI** — multi-step, autonomous AI — is the most significant near-term shift for finance operations: from reactive AI tools to proactive AI workflows.","**Federated learning** enables AI collaboration on sensitive financial data without data sharing — a key enabler for industry-wide AML and fraud models.","**Human accountability** for AI decisions is non-negotiable — the CFO and their organisation remain responsible regardless of which AI made a decision.","Finance activities **enhanced** by AI (strategy, relationships, judgment) become more valuable; those **replaced** (data entry, standard reports) must be automated, not defended.","**Continuous, structured learning** is the only sustainable response to AI's pace of change — a daily habit + monthly structured learning + quarterly application.","The finance professional of the future is an **AI-augmented strategic advisor** — using AI to handle the processing, freeing human expertise for judgment, relationships, and accountability."],1):
    st.markdown(f"**{i}.** {t}")

# Series Complete Banner
st.markdown("""
<div class="complete-banner">
  <h2 style="color:#4ade80;margin:0 0 0.5rem 0">🎉 AI Series Complete!</h2>
  <p style="color:#bbf7d0;margin:0 0 1rem 0;font-size:1rem">
    You have completed all 8 modules of the Knowledge Folder AI Series.<br>
    You now have a comprehensive foundation in AI for finance and accounting professionals.
  </p>
  <p style="color:#86efac;font-size:0.88rem;margin:0">
    Modules covered: Foundations · Machine Learning · Deep Learning · Generative AI ·
    AI in Finance · Building Models · Ethics & Governance · Future of AI
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
col1,col2,col3 = st.columns(3)
with col1:
    if st.button("⬅️ M7: Ethics & Governance", use_container_width=True): st.info("Navigate to Module 7 from the sidebar.")
with col2: st.markdown("<div style='text-align:center;padding-top:0.4rem'>🏆 Module 8 of 8 — Complete!</div>", unsafe_allow_html=True)
with col3:
    if st.button("🏠 Back to Homepage", use_container_width=True): st.info("Navigate to the Homepage from the sidebar.")
st.caption("Knowledge Folder · AI Series · Module 8 — Future of AI & Career Readiness · © 2025")