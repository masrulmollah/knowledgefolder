import streamlit as st
import random

# ── NO st.set_page_config() here — already called in Homepage ──────────────

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Hero banner */
.hero-banner {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    padding: 2.5rem 2rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    border-left: 6px solid #e94560;
}
.hero-title {
    font-size: 2rem;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 0.4rem 0;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: #a8b2d8;
    margin: 0;
}
.hero-badge {
    display: inline-block;
    background: #e94560;
    color: white;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.2rem 0.7rem;
    border-radius: 20px;
    margin-bottom: 0.8rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* Progress bar */
.progress-container {
    background: #e9ecef;
    border-radius: 20px;
    height: 10px;
    margin: 0.3rem 0 0.5rem 0;
}
.progress-bar {
    background: linear-gradient(90deg, #e94560, #f5a623);
    height: 10px;
    border-radius: 20px;
    width: 12.5%;
}
.progress-label {
    font-size: 0.78rem;
    color: #6c757d;
    margin-bottom: 0.2rem;
}

/* Topic cards */
.topic-card {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-left: 4px solid #0f3460;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
}
.topic-card-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: #1a1a2e;
    margin-bottom: 0.3rem;
}
.topic-card-body {
    font-size: 0.88rem;
    color: #495057;
    line-height: 1.6;
}

/* Finance lens box */
.finance-lens {
    background: linear-gradient(135deg, #fff3cd, #fff8e1);
    border: 1px solid #ffc107;
    border-left: 5px solid #f5a623;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin: 0.5rem 0;
}
.finance-lens-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: #856404;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.4rem;
}
.finance-lens-body {
    font-size: 0.88rem;
    color: #5a4200;
    line-height: 1.6;
}

/* Key term pill */
.term-pill {
    display: inline-block;
    background: #e8f4f8;
    color: #0f3460;
    border: 1px solid #b8dce8;
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.2rem;
}

/* Stat cards */
.stat-card {
    background: white;
    border: 1px solid #dee2e6;
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
}
.stat-number {
    font-size: 1.8rem;
    font-weight: 800;
    color: #e94560;
}
.stat-label {
    font-size: 0.78rem;
    color: #6c757d;
    margin-top: 0.2rem;
}

/* Quiz */
.quiz-box {
    background: #f0f4ff;
    border: 1px solid #c5d0f5;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
}

/* Section heading */
.section-heading {
    font-size: 1.15rem;
    font-weight: 700;
    color: #1a1a2e;
    border-bottom: 2px solid #e94560;
    padding-bottom: 0.3rem;
    margin: 1.5rem 0 1rem 0;
}

/* Nav footer */
.nav-footer {
    background: #f8f9fa;
    border-top: 2px solid #dee2e6;
    border-radius: 0 0 12px 12px;
    padding: 1rem 1.5rem;
    margin-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)


# ── Hero Banner ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">📘 Module 1 of 8 &nbsp;|&nbsp; AI Series</div>
  <div class="hero-title">Foundations of Artificial Intelligence</div>
  <div class="hero-subtitle">Build a solid conceptual base — understand what AI is, how it evolved,
  and why every finance professional needs to speak this language today.</div>
</div>
""", unsafe_allow_html=True)

# ── Progress ─────────────────────────────────────────────────────────────────
st.markdown('<div class="progress-label">Series progress — Module 1 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

# ── Quick Stats Row ───────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-card"><div class="stat-number">8</div><div class="stat-label">Topics Covered</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><div class="stat-number">~25</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><div class="stat-number">10</div><div class="stat-label">Quiz Questions</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-card"><div class="stat-number">1950s</div><div class="stat-label">AI Origin Year</div></div>', unsafe_allow_html=True)

st.markdown("")

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [
        ("1", "Foundations of AI", True),
        ("2", "Machine Learning Essentials", False),
        ("3", "Deep Learning & Neural Networks", False),
        ("4", "Generative AI & LLMs", False),
        ("5", "AI in Finance & Accounting", False),
        ("6", "Building AI Models", False),
        ("7", "AI Ethics, Risk & Governance", False),
        ("8", "Future of AI & Career Readiness", False),
    ]
    for num, name, active in modules:
        if active:
            st.markdown(f"**▶ M{num} — {name}** ✅")
        else:
            st.markdown(f"M{num} — {name}")
    st.markdown("---")
    st.info("💡 **Tip:** Work through modules in order for the best learning experience.")


# ── TOPIC 1 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🧠 What is Artificial Intelligence?</div>', unsafe_allow_html=True)

with st.expander("📖 Definition & Core Concepts", expanded=True):
    st.markdown("""
    **Artificial Intelligence (AI)** is the branch of computer science that aims to build systems
    capable of performing tasks that would normally require human intelligence — such as
    understanding language, recognising patterns, making decisions, and learning from experience.

    The term was coined by **John McCarthy** in 1956 at the Dartmouth Conference, where AI was
    formally established as an academic discipline.

    At its core, AI works by:
    - **Learning from data** (finding patterns in large datasets)
    - **Reasoning** (applying learned patterns to new situations)
    - **Self-improving** (updating its knowledge as more data arrives)

    Unlike traditional software which follows explicit rules written by programmers, an AI system
    *learns* those rules from examples.
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        When your bank's fraud detection system flags an unusual transaction — that is AI learning
        from millions of past transactions, not a human-written rule. Similarly, when your ERP
        system auto-categorises expense claims or suggests a journal entry — that is AI pattern
        recognition at work.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Key Terms:**")
    terms = ["Algorithm", "Model", "Training", "Inference", "Dataset", "Feature", "Label", "Prediction"]
    st.markdown(" ".join([f'<span class="term-pill">{t}</span>' for t in terms]), unsafe_allow_html=True)


# ── TOPIC 2 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📅 A Brief History of AI</div>', unsafe_allow_html=True)

with st.expander("🕰️ AI Timeline — From 1950 to Today"):
    timeline = {
        "1950s": ("The Birth", "Alan Turing proposes the 'Turing Test'. Dartmouth Conference (1956) coins the term AI. Early programs play chess and prove theorems."),
        "1960s–70s": ("Early Optimism & First Winter", "Expert systems developed. Overpromising leads to funding cuts — the first 'AI Winter'."),
        "1980s": ("Expert Systems Boom", "Rule-based AI systems used in medicine and finance. Second AI Winter follows when systems proved too rigid."),
        "1990s–2000s": ("Machine Learning Rises", "Statistical approaches replace rules. IBM Deep Blue beats chess champion Kasparov (1997). Internet creates big data."),
        "2010s": ("Deep Learning Revolution", "Neural networks with many layers (deep learning) achieve breakthroughs. AlphaGo beats world champion. GPUs accelerate training."),
        "2020s": ("Generative AI Era", "ChatGPT, Claude, Gemini — large language models enter mainstream. AI enters every profession including finance and accounting."),
    }
    for era, (label, desc) in timeline.items():
        col_a, col_b = st.columns([1, 4])
        with col_a:
            st.markdown(f"**{era}**")
            st.caption(label)
        with col_b:
            st.info(desc)

    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        Finance was an early adopter of AI — credit scoring models (FICO) have used statistical
        learning since the 1980s. Algorithmic trading emerged in the 2000s. The 2020s bring
        AI directly into the accountant's desktop via Microsoft Copilot, Xero AI, and SAP Joule.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── TOPIC 3 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🗂️ Types of AI</div>', unsafe_allow_html=True)

with st.expander("🔍 Narrow AI vs General AI vs Super AI"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="topic-card">
        <div class="topic-card-title">🎯 Narrow AI (ANI)</div>
        <div class="topic-card-body">
        Designed for ONE specific task. All AI tools in use today are Narrow AI.<br><br>
        <b>Examples:</b> Spam filter, facial recognition, ChatGPT, fraud detection, voice assistants.
        </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="topic-card" style="border-left-color:#f5a623">
        <div class="topic-card-title">🧠 General AI (AGI)</div>
        <div class="topic-card-body">
        Hypothetical AI that can perform ANY intellectual task a human can. Does NOT exist yet.<br><br>
        <b>Status:</b> Active research area. Estimated 10–50 years away (debated).
        </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="topic-card" style="border-left-color:#e94560">
        <div class="topic-card-title">⚡ Super AI (ASI)</div>
        <div class="topic-card-body">
        Theoretical AI that surpasses all human intelligence. Purely hypothetical today.<br><br>
        <b>Status:</b> Subject of philosophical debate. Not a near-term concern.
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        Every AI tool a finance professional uses today — from anomaly detection in audit software
        to AI-driven FP&A platforms — is Narrow AI. AGI and ASI are important to be aware of
        conceptually, but have no immediate practical implication for your work.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── TOPIC 4 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">⚙️ AI vs Traditional Software</div>', unsafe_allow_html=True)

with st.expander("🔄 What Makes AI Different from Conventional Programming?"):
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### 💻 Traditional Software")
        st.markdown("""
        - Rules are **explicitly written** by programmers
        - Input + Rules → Output
        - Behaviour is **predictable and fixed**
        - Example: *"If amount > $10,000, flag for review"*
        - Cannot handle situations not covered by its rules
        """)
    with col_b:
        st.markdown("#### 🤖 AI / Machine Learning")
        st.markdown("""
        - Rules are **learned from data** automatically
        - Input + Output (examples) → Rules (learned)
        - Behaviour **adapts** as new data arrives
        - Example: *"Learn from 1M transactions what fraud looks like"*
        - Can generalise to new unseen situations
        """)

    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        A traditional ERP system applies fixed rules to classify a transaction. An AI-powered
        accounting system learns from your company's historical coding patterns and suggests
        the right GL account — improving its accuracy over time without manual reprogramming.
        This is the fundamental shift AI brings to finance workflows.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── TOPIC 5 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🗺️ The AI Landscape Map</div>', unsafe_allow_html=True)

with st.expander("🌐 How AI, ML, Deep Learning & Gen AI Relate"):
    st.markdown("""
    A common source of confusion is the relationship between AI and its sub-fields. Think of them
    as **nested circles** from broadest to narrowest:

    ```
    ┌─────────────────────────────────────────────┐
    │  ARTIFICIAL INTELLIGENCE (AI)               │
    │  ┌───────────────────────────────────────┐  │
    │  │  MACHINE LEARNING (ML)                │  │
    │  │  ┌─────────────────────────────────┐  │  │
    │  │  │  DEEP LEARNING (DL)             │  │  │
    │  │  │  ┌───────────────────────────┐  │  │  │
    │  │  │  │  GENERATIVE AI (Gen AI)   │  │  │  │
    │  │  │  └───────────────────────────┘  │  │  │
    │  │  └─────────────────────────────────┘  │  │
    │  └───────────────────────────────────────┘  │
    └─────────────────────────────────────────────┘
    ```

    - **AI** — The broad field: any machine mimicking human intelligence
    - **ML** — A subset of AI: systems that learn from data
    - **Deep Learning** — A subset of ML: multi-layered neural networks
    - **Generative AI** — A subset of Deep Learning: models that create new content (text, images, code)
    """)

    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        <b>Credit scoring</b> → ML. &nbsp;|&nbsp;
        <b>Document OCR &amp; extraction</b> → Deep Learning. &nbsp;|&nbsp;
        <b>ChatGPT / Copilot drafting board reports</b> → Generative AI. &nbsp;|&nbsp;
        All are "AI" — but knowing the sub-type helps you evaluate capabilities and limitations.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── TOPIC 6 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📊 AI Capabilities Spectrum</div>', unsafe_allow_html=True)

with st.expander("🔢 What Can AI Actually Do? — The 6 Core Capabilities"):
    capabilities = [
        ("🔍", "Pattern Recognition",
         "Identifying recurring structures in data.",
         "Fraud detection, anomaly detection in GL, document classification."),
        ("📝", "Natural Language Processing (NLP)",
         "Understanding and generating human language.",
         "Reading contracts, summarising reports, answering finance queries in plain English."),
        ("🔮", "Prediction & Forecasting",
         "Estimating future values from historical data.",
         "Cash flow forecasting, revenue prediction, credit risk scoring."),
        ("🎯", "Recommendation",
         "Suggesting next-best actions based on context.",
         "Recommending journal entries, flagging unusual approvals for review."),
        ("🤖", "Automation & Decision-Making",
         "Executing rule-based and learned decisions at scale.",
         "Invoice matching, expense categorisation, payroll anomaly detection."),
        ("🎨", "Generation",
         "Creating new content — text, images, code, data.",
         "Drafting audit reports, generating variance commentary, coding financial models."),
    ]
    for icon, title, desc, fin in capabilities:
        c1, c2 = st.columns([1, 3])
        with c1:
            st.markdown(f"### {icon}\n**{title}**")
        with c2:
            st.markdown(f"*{desc}*")
            st.markdown(f"💼 **Finance use:** {fin}")
        st.divider()


# ── TOPIC 7 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🏦 Why AI Matters for Finance Professionals</div>', unsafe_allow_html=True)

with st.expander("📈 The Business Case for AI Literacy in Finance"):
    st.markdown("""
    AI is not replacing finance professionals — but finance professionals **who use AI** are
    replacing those who don't. Here is why AI literacy has become a core professional skill:
    """)

    reasons = {
        "⏱️ Efficiency": "AI automates repetitive, rule-based tasks — reconciliations, data entry, report generation — freeing you for higher-value analysis.",
        "🎯 Accuracy": "AI reduces human error in data processing. Automated bank reconciliations and AI-assisted audit sampling are faster and more consistent.",
        "🔍 Insight": "AI can find patterns in financial data that humans would miss — identifying cost drivers, revenue anomalies, or emerging credit risks.",
        "🏆 Competitive Advantage": "Firms using AI in FP&A, audit, and tax are faster, cheaper, and more insightful. AI literacy helps you contribute to these initiatives.",
        "⚖️ Risk & Governance": "Finance professionals need to understand AI's limitations — hallucinations, bias, model risk — to govern its use in financial processes.",
    }
    for icon_title, body in reasons.items():
        st.markdown(f"**{icon_title}**")
        st.markdown(f"> {body}")

    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — AI Tools You May Already Be Using</div>
      <div class="finance-lens-body">
        <b>Microsoft Copilot</b> (Excel, Teams, Word) &nbsp;|&nbsp;
        <b>SAP Joule</b> (ERP AI assistant) &nbsp;|&nbsp;
        <b>Xero Analytics Plus</b> (cash flow AI) &nbsp;|&nbsp;
        <b>Bloomberg AI</b> (research summaries) &nbsp;|&nbsp;
        <b>Alteryx</b> (automated data prep) &nbsp;|&nbsp;
        <b>Workiva</b> (AI-assisted reporting)
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── TOPIC 8 ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📖 Key Terms Glossary</div>', unsafe_allow_html=True)

with st.expander("🔑 Essential AI Vocabulary for Finance Professionals"):
    glossary = {
        "Algorithm": "A set of instructions or rules that a computer follows to solve a problem. In AI, algorithms learn these rules from data.",
        "Model": "The output of training an algorithm on data — a mathematical function that maps inputs to outputs.",
        "Training Data": "The historical dataset used to teach an AI model. Quality and quantity of training data directly impacts model performance.",
        "Inference": "Using a trained model to make predictions on new, unseen data. This is what happens when you use an AI tool.",
        "Feature": "An individual measurable input variable used by a model (e.g. invoice amount, payment days, customer age).",
        "Label": "The known output in supervised learning (e.g. 'fraud' or 'not fraud') used to train the model.",
        "Overfitting": "When a model learns training data too precisely and fails to generalise to new data — a key risk in financial models.",
        "Bias": "Systematic errors in AI output caused by flawed training data or model design. A major governance concern in finance.",
        "Neural Network": "A computational model loosely inspired by the human brain, consisting of layers of interconnected nodes.",
        "Hallucination": "When a generative AI produces plausible-sounding but factually incorrect output. Critical risk in financial contexts.",
    }
    search_term = st.text_input("🔍 Search glossary terms", placeholder="Type a term...")
    for term, definition in glossary.items():
        if search_term.lower() in term.lower() or search_term.lower() in definition.lower() or not search_term:
            st.markdown(f"**{term}**")
            st.caption(definition)
            st.divider()


# ── INTERACTIVE QUIZ ──────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🧩 Knowledge Check — Quick Quiz</div>', unsafe_allow_html=True)

st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {
        "q": "Which of the following BEST describes the difference between traditional software and AI?",
        "options": [
            "Traditional software is faster than AI",
            "Traditional software follows explicit rules; AI learns rules from data",
            "AI cannot make mistakes; traditional software can",
            "Traditional software uses the internet; AI does not",
        ],
        "answer": "Traditional software follows explicit rules; AI learns rules from data",
        "explanation": "The fundamental distinction is that traditional software is programmed with explicit rules, while AI systems learn patterns and rules from data examples."
    },
    {
        "q": "ChatGPT, Claude, and Microsoft Copilot are examples of which type of AI?",
        "options": ["Artificial General Intelligence (AGI)", "Super AI (ASI)", "Narrow AI (ANI)", "Expert Systems"],
        "answer": "Narrow AI (ANI)",
        "explanation": "All current AI tools — including the most advanced LLMs — are Narrow AI. They are very capable within their domain but cannot generalise to arbitrary tasks the way a human can."
    },
    {
        "q": "In the AI landscape, which is the BROADEST category?",
        "options": ["Machine Learning", "Deep Learning", "Generative AI", "Artificial Intelligence"],
        "answer": "Artificial Intelligence",
        "explanation": "AI is the broadest field. ML is a subset of AI, Deep Learning is a subset of ML, and Generative AI is a subset of Deep Learning."
    },
    {
        "q": "When a bank's fraud detection system 'learns' what fraudulent transactions look like from historical data, this is best described as:",
        "options": ["Traditional rule-based programming", "Machine Learning", "Super AI", "Human intelligence"],
        "answer": "Machine Learning",
        "explanation": "Learning patterns from historical data to make predictions on new data is the core definition of Machine Learning."
    },
    {
        "q": "What does 'hallucination' mean in the context of Generative AI?",
        "options": [
            "The AI generates images instead of text",
            "The AI produces plausible-sounding but factually incorrect output",
            "The AI runs too slowly",
            "The AI refuses to answer a question",
        ],
        "answer": "The AI produces plausible-sounding but factually incorrect output",
        "explanation": "Hallucination is a critical risk for finance professionals — AI may confidently state incorrect figures, regulations, or facts. Always verify AI output against authoritative sources."
    },
]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected" not in st.session_state:
    st.session_state.selected = None
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False

if not st.session_state.quiz_done:
    q_data = questions[st.session_state.q_index]
    st.markdown(f"**Question {st.session_state.q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")

    choice = st.radio("Select your answer:", q_data["options"], key=f"q_{st.session_state.q_index}")

    col_submit, col_next = st.columns([1, 1])
    with col_submit:
        if st.button("✅ Submit Answer", key=f"submit_{st.session_state.q_index}"):
            st.session_state.answered = True
            st.session_state.selected = choice
            if choice == q_data["answer"]:
                st.session_state.score += 1

    if st.session_state.answered:
        if st.session_state.selected == q_data["answer"]:
            st.success(f"✅ Correct! — {q_data['explanation']}")
        else:
            st.error(f"❌ Not quite. The answer is: **{q_data['answer']}**\n\n{q_data['explanation']}")

        with col_next:
            if st.session_state.q_index < len(questions) - 1:
                if st.button("Next Question ➡️"):
                    st.session_state.q_index += 1
                    st.session_state.answered = False
                    st.session_state.selected = None
                    st.rerun()
            else:
                if st.button("🏁 See Results"):
                    st.session_state.quiz_done = True
                    st.rerun()
else:
    score = st.session_state.score
    total = len(questions)
    pct = int((score / total) * 100)
    if pct >= 80:
        emoji, msg = "🏆", "Excellent! You have a strong grasp of AI foundations."
    elif pct >= 60:
        emoji, msg = "👍", "Good effort! Review the topics above to strengthen your understanding."
    else:
        emoji, msg = "📚", "Keep going! Re-read the expandable sections and try again."

    st.markdown(f"### {emoji} Your Score: {score}/{total} ({pct}%)")
    st.progress(pct / 100)
    st.info(msg)
    if st.button("🔄 Retake Quiz"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.quiz_done = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)


# ── Key Takeaways ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">💡 Key Takeaways</div>', unsafe_allow_html=True)

takeaways = [
    "AI refers to machines that perform tasks requiring human-like intelligence. All current AI tools are **Narrow AI**.",
    "AI learns rules from data; traditional software is programmed with explicit rules. This is the fundamental difference.",
    "AI, ML, Deep Learning, and Generative AI are **nested fields** — not interchangeable terms.",
    "Finance professionals already interact with AI daily — in ERP systems, fraud detection, forecasting, and reporting tools.",
    "AI literacy is now a **core professional competency** alongside Excel, accounting standards, and financial analysis.",
    "**Hallucinations and bias** are real risks. Always validate AI outputs in financial contexts.",
]
for i, t in enumerate(takeaways, 1):
    st.markdown(f"**{i}.** {t}")


# ── Module Navigation Footer ──────────────────────────────────────────────────
st.markdown("---")
col_prev, col_home, col_next = st.columns([1, 1, 1])
with col_prev:
    st.button("⬅️ Previous", disabled=True, use_container_width=True)
with col_home:
    st.markdown("<div style='text-align:center;padding-top:0.4rem'>📘 Module 1 of 8</div>", unsafe_allow_html=True)
with col_next:
    if st.button("Next Module ➡️", use_container_width=True):
        st.info("Navigate to **Module 2 — Machine Learning Essentials** from the sidebar.")

st.caption("Knowledge Folder · AI Series · Module 1 — Foundations of AI · © 2025")