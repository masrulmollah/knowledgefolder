import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
/* ── Hero ── */
.hero-banner {
    background: linear-gradient(135deg, #0a0a1a 0%, #12123a 35%, #1e1e6e 65%, #2d2d9e 100%);
    padding: 3rem 2.5rem; border-radius: 20px; margin-bottom: 1.5rem;
    border-left: 6px solid #818cf8; position: relative; overflow: hidden;
}
.hero-title { font-size: 2.3rem; font-weight: 900; color: #ffffff; margin: 0 0 0.5rem 0; line-height: 1.2; }
.hero-subtitle { font-size: 1.05rem; color: #c7d2fe; margin: 0 0 1.2rem 0; line-height: 1.7; }
.hero-badge {
    display: inline-block; background: #818cf8; color: #0a0a1a;
    font-size: 0.75rem; font-weight: 800; padding: 0.25rem 0.9rem;
    border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase; letter-spacing: 0.06em;
}
.hero-tag {
    display: inline-block; background: rgba(129,140,248,0.15); color: #a5b4fc;
    border: 1px solid rgba(129,140,248,0.4); font-size: 0.78rem; font-weight: 600;
    padding: 0.2rem 0.7rem; border-radius: 20px; margin: 0.15rem;
}

/* ── Stat cards ── */
.stat-card {
    background: white; border: 1px solid #e5e7eb; border-radius: 14px;
    padding: 1.3rem 1rem; text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06); transition: transform 0.2s;
}
.stat-number { font-size: 2rem; font-weight: 900; color: #4338ca; }
.stat-label { font-size: 0.78rem; color: #6b7280; margin-top: 0.2rem; font-weight: 500; }

/* ── Section heading ── */
.section-heading {
    font-size: 1.2rem; font-weight: 800; color: #1e1b4b;
    border-bottom: 3px solid #818cf8; padding-bottom: 0.4rem;
    margin: 2rem 0 1.2rem 0; display: flex; align-items: center; gap: 0.5rem;
}

/* ── AI Definition box ── */
.definition-box {
    background: linear-gradient(135deg, #eef2ff, #f0fdf4);
    border: 1px solid #c7d2fe; border-left: 5px solid #4338ca;
    border-radius: 14px; padding: 1.4rem 1.6rem; margin: 1rem 0;
}
.definition-title { font-size: 1rem; font-weight: 800; color: #312e81; margin-bottom: 0.5rem; }
.definition-body { font-size: 0.92rem; color: #374151; line-height: 1.8; }

/* ── Module card ── */
.module-card {
    background: white; border: 1px solid #e5e7eb; border-radius: 14px;
    padding: 1.2rem 1.4rem; margin-bottom: 0.9rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    border-left: 5px solid #818cf8;
    transition: box-shadow 0.2s;
}
.module-number {
    display: inline-block; width: 28px; height: 28px; border-radius: 50%;
    text-align: center; line-height: 28px; font-size: 0.78rem;
    font-weight: 800; margin-right: 0.5rem; flex-shrink: 0;
}
.module-title { font-size: 1rem; font-weight: 700; color: #1e1b4b; margin-bottom: 0.3rem; }
.module-desc { font-size: 0.85rem; color: #4b5563; line-height: 1.6; margin-bottom: 0.5rem; }
.module-topics { font-size: 0.8rem; color: #6366f1; font-weight: 600; }

/* ── Finance lens ── */
.finance-lens {
    background: linear-gradient(135deg, #fffbeb, #fefce8);
    border: 1px solid #fcd34d; border-left: 5px solid #f59e0b;
    border-radius: 12px; padding: 1rem 1.4rem; margin: 0.6rem 0;
}
.finance-lens-title {
    font-size: 0.82rem; font-weight: 800; color: #92400e;
    text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem;
}
.finance-lens-body { font-size: 0.87rem; color: #78350f; line-height: 1.7; }

/* ── Nested sub-field diagram ── */
.nest-container {
    background: linear-gradient(135deg, #eef2ff 0%, #f0f9ff 100%);
    border: 2px solid #c7d2fe; border-radius: 16px; padding: 1.5rem;
    text-align: center; margin: 0.8rem 0;
}
.nest-label { font-size: 0.82rem; font-weight: 700; letter-spacing: 0.03em; }

/* ── Skill pill ── */
.skill-pill {
    display: inline-block; background: #ede9fe; color: #4338ca;
    border: 1px solid #c4b5fd; border-radius: 20px;
    padding: 0.2rem 0.75rem; font-size: 0.78rem; font-weight: 600; margin: 0.2rem;
}

/* ── Why card ── */
.why-card {
    background: white; border: 1px solid #e5e7eb; border-radius: 12px;
    padding: 1rem 1.2rem; margin-bottom: 0.7rem;
    border-top: 4px solid #818cf8;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.why-icon { font-size: 1.4rem; margin-bottom: 0.3rem; }
.why-title { font-size: 0.92rem; font-weight: 700; color: #1e1b4b; margin-bottom: 0.3rem; }
.why-body { font-size: 0.83rem; color: #4b5563; line-height: 1.6; }

/* ── Timeline ── */
.timeline-item {
    display: flex; gap: 1rem; margin-bottom: 0.8rem; align-items: flex-start;
}
.timeline-dot {
    min-width: 36px; height: 36px; border-radius: 50%;
    background: #4338ca; color: white; display: flex;
    align-items: center; justify-content: center; font-size: 0.72rem; font-weight: 800;
    flex-shrink: 0;
}
.timeline-content { font-size: 0.87rem; color: #374151; padding-top: 0.3rem; line-height: 1.6; }

/* ── Application table ── */
.app-row {
    display: flex; gap: 0.8rem; padding: 0.7rem 0;
    border-bottom: 1px solid #f3f4f6; align-items: flex-start;
}
.app-function {
    min-width: 140px; font-size: 0.82rem; font-weight: 700; color: #4338ca;
}
.app-uses { font-size: 0.82rem; color: #374151; line-height: 1.6; }

/* ── CTA card ── */
.cta-card {
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
    border-radius: 16px; padding: 2rem 2.5rem; text-align: center; margin-top: 1.5rem;
    color: white;
}
.cta-title { font-size: 1.4rem; font-weight: 800; margin-bottom: 0.5rem; }
.cta-body { font-size: 0.92rem; color: #c7d2fe; margin-bottom: 1.2rem; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)


# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">🤖 AI Series — Overview &amp; Guide</div>
  <div class="hero-title">Artificial Intelligence (AI)<br>for Finance Professionals</div>
  <div class="hero-subtitle">
    A complete, structured guide to understanding, applying, and governing AI —
    written specifically for finance and accounting professionals.<br>
    From foundations to future trends, mapped to your career and your work.
  </div>
  <div>
    <span class="hero-tag">8 Modules</span>
    <span class="hero-tag">Finance-first lens</span>
    <span class="hero-tag">Interactive quizzes</span>
    <span class="hero-tag">Real tools &amp; use cases</span>
    <span class="hero-tag">Practical code examples</span>
    <span class="hero-tag">Career roadmap</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ── QUICK STATS ───────────────────────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)
stats = [
    ("8", "Modules"),
    ("40+", "Topics Covered"),
    ("40+", "Quiz Questions"),
    ("30+", "AI Tools Referenced"),
    ("~4 hrs", "Total Read Time"),
]
for col, (num, label) in zip([c1,c2,c3,c4,c5], stats):
    with col:
        st.markdown(f'<div class="stat-card"><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

st.markdown("")


# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    for num, name in [("OV","Overview (This Page)"),("1","Foundations of AI"),("2","Machine Learning Essentials"),("3","Deep Learning & Neural Networks"),("4","Generative AI & LLMs"),("5","AI in Finance & Accounting"),("6","Building AI Models"),("7","AI Ethics, Risk & Governance"),("8","Future of AI & Career Readiness")]:
        prefix = "**▶" if num == "OV" else " "
        suffix = "** 🗺️" if num == "OV" else ""
        st.markdown(f"{prefix} M{num} — {name}{suffix}")
    st.markdown("---")
    st.info("💡 Start here if you are new to the AI series, then navigate to individual modules.")


# ── WHAT IS AI ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🧠 What is Artificial Intelligence?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="definition-box">
  <div class="definition-title">Definition</div>
  <div class="definition-body">
    <b>Artificial Intelligence (AI)</b> is the field of computer science focused on building systems
    that can perform tasks that would normally require human intelligence — such as understanding
    language, recognising patterns, making predictions, generating content, and learning from experience.
    <br><br>
    Unlike traditional software, which follows explicit rules written by programmers, an AI system
    <b>learns its own rules from data</b>. Given enough examples of inputs and their correct outputs,
    an AI model discovers the underlying patterns and can apply them to new, unseen situations.
    <br><br>
    The term was coined at the <b>Dartmouth Conference in 1956</b>. Practical, large-scale AI became
    possible in the 2010s as three forces converged: <b>massive datasets</b> (the internet),
    <b>powerful computing</b> (GPUs), and <b>algorithmic breakthroughs</b> (deep learning).
    The 2020s introduced Generative AI — tools that can create new text, images, and code — bringing
    AI directly into every professional's workflow.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="finance-lens">
  <div class="finance-lens-title">💼 The Finance Professional's One-Line Summary</div>
  <div class="finance-lens-body">
    AI is software that learns from your financial data to predict, detect, generate, and automate —
    replacing manual pattern-matching with scale, speed, and consistency that no human team can match.
    It is already inside your ERP, your audit tools, your bank, and your Excel.
    The question is not whether to engage with AI — it is how to do so effectively and responsibly.
  </div>
</div>
""", unsafe_allow_html=True)


# ── AI LANDSCAPE MAP ─────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🗺️ The AI Landscape — How the Sub-fields Relate</div>', unsafe_allow_html=True)

col_left, col_right = st.columns([2, 3])
with col_left:
    st.markdown("""
    <div class="nest-container">
      <div style="background:#e0e7ff;border:2px solid #818cf8;border-radius:14px;padding:1.2rem 1rem;">
        <div class="nest-label" style="color:#3730a3">🌐 ARTIFICIAL INTELLIGENCE</div>
        <div style="font-size:0.75rem;color:#6366f1;margin:0.2rem 0 0.7rem">Any system mimicking human intelligence</div>
        <div style="background:#dbeafe;border:2px solid #60a5fa;border-radius:10px;padding:0.9rem 0.8rem;">
          <div class="nest-label" style="color:#1d4ed8">📊 MACHINE LEARNING</div>
          <div style="font-size:0.72rem;color:#3b82f6;margin:0.2rem 0 0.6rem">Systems that learn from data</div>
          <div style="background:#dcfce7;border:2px solid #4ade80;border-radius:7px;padding:0.7rem 0.6rem;">
            <div class="nest-label" style="color:#15803d">🧠 DEEP LEARNING</div>
            <div style="font-size:0.7rem;color:#16a34a;margin:0.15rem 0 0.5rem">Multi-layer neural networks</div>
            <div style="background:#fef9c3;border:2px solid #fbbf24;border-radius:5px;padding:0.5rem 0.5rem;">
              <div class="nest-label" style="color:#92400e">✨ GENERATIVE AI</div>
              <div style="font-size:0.68rem;color:#b45309">Creates new text, images, code</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    | Layer | What it is | Finance examples |
    |-------|-----------|-----------------|
    | **AI** | Broad field — any machine mimicking intelligence | Fraud rules, chatbots, robotic process automation |
    | **ML** | Learns rules from data without explicit programming | Credit scoring, revenue forecasting, churn prediction |
    | **Deep Learning** | Neural networks with many layers | Document OCR, contract analysis, time-series forecasting |
    | **Generative AI** | Creates new content from learned patterns | ChatGPT, Claude, Copilot — drafting, summarising, coding |
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Why This Matters</div>
      <div class="finance-lens-body">
        When a colleague says "we're using AI" — ask which layer. A credit scoring model (ML) has very
        different capabilities, risks, and governance requirements than a document summarisation tool
        (Generative AI). Knowing the sub-field makes you a more effective participant in AI projects.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── TYPES OF AI ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📐 Three Types of AI You Need to Know</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)
with t1:
    st.markdown("""
    <div class="module-card" style="border-left-color:#4338ca">
      <div class="module-title">🎯 Narrow AI (ANI)</div>
      <div class="module-desc">
        Designed for one specific task. Excellent within its domain; cannot generalise beyond it.
        <b>All AI tools that exist today are Narrow AI.</b>
      </div>
      <div class="module-topics">
        Examples: ChatGPT, fraud detection, credit scoring, invoice OCR, voice assistants
      </div>
    </div>
    """, unsafe_allow_html=True)
with t2:
    st.markdown("""
    <div class="module-card" style="border-left-color:#0891b2">
      <div class="module-title">🧩 General AI (AGI)</div>
      <div class="module-desc">
        Hypothetical AI that can perform any intellectual task a human can. Does not exist yet.
        Active research area — estimated 10–50 years away (highly debated).
      </div>
      <div class="module-topics">Status: Research phase only — no practical finance implication today</div>
    </div>
    """, unsafe_allow_html=True)
with t3:
    st.markdown("""
    <div class="module-card" style="border-left-color:#dc2626">
      <div class="module-title">⚡ Super AI (ASI)</div>
      <div class="module-desc">
        Purely theoretical — AI surpassing all human intelligence across all domains.
        Subject of philosophical debate, not practical planning.
      </div>
      <div class="module-topics">Status: Theoretical concept only</div>
    </div>
    """, unsafe_allow_html=True)


# ── BRIEF HISTORY ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📅 AI in 60 Seconds — A Brief History</div>', unsafe_allow_html=True)

with st.expander("🕰️ From 1956 to the Generative AI Era"):
    timeline_items = [
        ("1950s", "Alan Turing proposes the Turing Test. Dartmouth Conference (1956) formally names 'Artificial Intelligence'. Early programs play chess and prove theorems."),
        ("1970–80s", "Expert systems: rule-based AI used in medicine and finance. First 'AI Winter' — overpromising leads to funding cuts. Second wave: machine learning approaches emerge."),
        ("1990s", "Statistical ML replaces hand-coded rules. IBM Deep Blue beats chess world champion Kasparov (1997). Internet creates the data foundation AI needs."),
        ("2010s", "Deep learning revolution: neural networks achieve superhuman performance on image and speech tasks. AlphaGo beats world Go champion. GPU computing makes training practical."),
        ("2017", "Transformer architecture introduced ('Attention Is All You Need'). The architecture that powers GPT-4, Claude, and Gemini is born."),
        ("2020–22", "GPT-3, then ChatGPT (Nov 2022) — generative AI enters mainstream. 1 million users in 5 days. Finance professionals begin using AI daily."),
        ("2023–25", "Claude, GPT-4, Gemini, Copilot become standard tools. Agentic AI emerges. EU AI Act passes. Finance function transformation accelerates."),
    ]
    for era, desc in timeline_items:
        st.markdown(f"""
        <div class="timeline-item">
          <div class="timeline-dot">{era[:4]}</div>
          <div class="timeline-content"><b>{era}</b> — {desc}</div>
        </div>
        """, unsafe_allow_html=True)


# ── WHY AI MATTERS FOR FINANCE ────────────────────────────────────────────────
st.markdown('<div class="section-heading">💼 Why AI Matters for Finance & Accounting Professionals</div>', unsafe_allow_html=True)

why_items = [
    ("⏱️", "Automation of High-Volume Tasks", "Reconciliations, journal entries, invoice processing, report generation — AI handles these faster and more accurately than manual effort, freeing you for analysis and advisory work."),
    ("🎯", "Prediction at Scale", "ML models predict cash flow, credit defaults, late payments, and revenue with accuracy that manual judgement and spreadsheet extrapolation cannot match."),
    ("🔍", "Anomaly Detection", "AI analyses 100% of transactions — not a sample — flagging unusual patterns in journal entries, expenses, and payables that would take human auditors weeks to find."),
    ("📝", "Language at Speed", "LLMs draft variance commentary, summarise board packs, analyse contracts, and answer tax queries in seconds — compressing hours of professional writing into minutes of review."),
    ("⚖️", "Governance Imperative", "Finance professionals govern AI models in their organisations. Understanding bias, hallucination, explainability, and model risk is now a core professional competency — not optional."),
    ("🚀", "Career Differentiation", "Finance professionals who use AI to produce better analysis faster become significantly more valuable. Those who don't risk displacement — not by AI, but by colleagues using AI."),
]

cols = st.columns(2)
for i, (icon, title, body) in enumerate(why_items):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="why-card">
          <div class="why-icon">{icon}</div>
          <div class="why-title">{title}</div>
          <div class="why-body">{body}</div>
        </div>
        """, unsafe_allow_html=True)


# ── AI ACROSS FINANCE FUNCTION ────────────────────────────────────────────────
st.markdown('<div class="section-heading">🏦 AI Across the Finance Function — At a Glance</div>', unsafe_allow_html=True)

with st.expander("📋 Finance Function → Key AI Applications → Tools", expanded=False):
    applications = [
        ("📊 FP&A", "Driver-based ML forecasting, automated variance commentary, rolling forecast automation, scenario modelling at scale", "Anaplan, Workday Adaptive, Pigment, Microsoft Copilot"),
        ("🔍 Audit", "100% journal entry testing, expense anomaly detection, contract analysis, continuous monitoring", "MindBridge, AppZen, Kira, ACL/Galvanize"),
        ("💳 AP / AR", "Invoice OCR & processing, 3-way match automation, predictive DSO, cash application", "ABBYY, Rossum, HighRadius, Tesorio, Esker"),
        ("💰 Treasury", "Cash flow forecasting (LSTM), FX exposure detection, liquidity stress testing", "Kyriba, GTreasury, Salmon"),
        ("🧾 Tax", "Document classification, transfer pricing benchmarking, tax research, VAT automation", "ONESOURCE, Avalara, Bloomberg Tax"),
        ("🏦 Risk & Compliance", "AML transaction monitoring, KYC identity verification, credit risk scoring", "NICE Actimize, Feedzai, Jumio, FICO, Zest AI"),
        ("📈 Investment", "NLP earnings call analysis, alternative data, algorithmic trading, ESG scoring", "Bloomberg AI, AlphaSense, Kensho, MSCI ESG"),
        ("📋 Reporting", "Financial close automation, disclosure drafting, XBRL tagging, report summarisation", "BlackLine, Workiva, SAP Financial Close"),
    ]
    for func, uses, tools in applications:
        st.markdown(f"""
        <div class="app-row">
          <div class="app-function">{func}</div>
          <div class="app-uses">
            {uses}<br>
            <span style="font-size:0.76rem;color:#6366f1">🛠 {tools}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)


# ── 8 MODULE OVERVIEW ─────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📚 The 8 Modules — What You Will Learn</div>', unsafe_allow_html=True)

modules = [
    {
        "num": "1", "color": "#e94560", "bg": "#fff0f3",
        "icon": "🧠", "title": "Foundations of AI",
        "summary": "Build your conceptual base. Understand what AI is, how it differs from traditional software, the nested sub-field landscape (AI → ML → Deep Learning → Gen AI), and the 6 core AI capabilities.",
        "topics": "Definition · History · Narrow vs General AI · AI vs Traditional Software · AI Capabilities Map · Glossary",
        "finance": "Why every finance professional needs AI literacy now. AI already inside SAP, Oracle, Xero, Bloomberg, and Microsoft 365.",
        "outcome": "Confidently explain AI concepts in board and project discussions.",
    },
    {
        "num": "2", "color": "#415a77", "bg": "#f0f4f8",
        "icon": "📊", "title": "Machine Learning Essentials",
        "summary": "The engine behind most finance AI. Understand supervised, unsupervised, and reinforcement learning. Know when to use regression, classification, and clustering — and which algorithm to choose.",
        "topics": "Supervised · Unsupervised · Reinforcement Learning · Key Algorithms · ML Pipeline · Overfitting · Evaluation Metrics",
        "finance": "Credit scoring, fraud detection, revenue forecasting, customer segmentation, journal entry anomaly detection.",
        "outcome": "Intelligently evaluate ML model proposals and challenge data science teams.",
    },
    {
        "num": "3", "color": "#2d4a8a", "bg": "#f0f4ff",
        "icon": "🔵", "title": "Deep Learning & Neural Networks",
        "summary": "Demystify the black box. Understand how neural networks learn, what backpropagation does, and how CNNs, LSTMs, and Transformers work — including the architecture behind ChatGPT and Claude.",
        "topics": "Neural Network Structure · Backpropagation · Activation Functions · CNN · LSTM · Transformer · Embeddings · Attention",
        "finance": "Invoice OCR (CNN), cash flow forecasting (LSTM), document understanding and LLMs (Transformer).",
        "outcome": "Understand what the AI tools you use are actually doing under the hood.",
    },
    {
        "num": "4", "color": "#6a1f9e", "bg": "#f9f0ff",
        "icon": "✨", "title": "Generative AI & Large Language Models",
        "summary": "Master the tools reshaping finance workflows. Understand how LLMs are trained, how to prompt engineer effectively, what RAG is, and how to manage hallucination risk in financial contexts.",
        "topics": "What is Gen AI · How LLMs Work · RLHF · Major Models · Prompt Engineering · RAG · Fine-tuning · Hallucination Risk",
        "finance": "Drafting reports, contract analysis, tax research, variance commentary, Excel formula generation.",
        "outcome": "Use AI tools productively and safely for finance-specific tasks.",
    },
    {
        "num": "5", "color": "#1a5c38", "bg": "#f0fff4",
        "icon": "🏦", "title": "AI Applications in Finance & Accounting",
        "summary": "The applied centrepiece. Explore real AI implementations across FP&A, audit, AP/AR, treasury, tax, risk, investment management, and financial reporting — with the tools driving transformation today.",
        "topics": "FP&A · Audit · AP/AR · Treasury · Tax · AML/KYC · Investment Management · Financial Reporting · Real Tools",
        "finance": "30+ real AI tools mapped to finance functions. Case study: 10-day close to 3-day close with AI.",
        "outcome": "Map AI opportunities to your specific finance role and organisation.",
    },
    {
        "num": "6", "color": "#7a5500", "bg": "#fffbeb",
        "icon": "🛠️", "title": "Building AI Models — A Practical Primer",
        "summary": "Walk through the complete 8-stage ML pipeline using a finance example: predicting late invoice payments. Includes Python code you can adapt, plus no-code AutoML options for non-developers.",
        "topics": "Problem Definition · Data Collection · EDA · Preprocessing · Feature Engineering · Model Training · Evaluation · Deployment · Monitoring",
        "finance": "Full worked example: invoice late payment classifier. Python + XGBoost. Time-based split. SHAP explainability.",
        "outcome": "Participate meaningfully in AI model development projects. Ask the right questions.",
    },
    {
        "num": "7", "color": "#8b1a1a", "bg": "#fff5f5",
        "icon": "⚖️", "title": "AI Ethics, Risk & Governance",
        "summary": "The responsible use of AI in finance. Understand bias types, hallucination risks, explainability requirements, model risk management frameworks, data privacy obligations, and the regulatory landscape.",
        "topics": "Bias Types · Hallucination Risk · Explainability (SHAP/LIME) · Model Risk Management · Data Privacy · EU AI Act · MAS FEAT · SR 11-7",
        "finance": "AI governance for credit models, AML, and automated decisions. PDPA/GDPR for AI training data. Interactive risk checker tool.",
        "outcome": "Lead or contribute to AI governance initiatives in your organisation.",
    },
    {
        "num": "8", "color": "#4040a0", "bg": "#f5f3ff",
        "icon": "🚀", "title": "Future of AI & Career Readiness",
        "summary": "Look ahead at 8 emerging trends — agentic AI, multimodal, federated learning, quantum AI — and build your personal AI skills roadmap. Understand which finance activities AI enhances versus replaces.",
        "topics": "Agentic AI · Multimodal · Federated Learning · AI + Blockchain · Role Impact Analysis · Skills Roadmap · 90-Day Action Plan",
        "finance": "Personal 90-day action plan builder. Finance job market evolution. New roles: Finance AI Lead, AI Model Risk Analyst.",
        "outcome": "Build a concrete plan for staying ahead in an AI-transformed profession.",
    },
]

for m in modules:
    with st.expander(f"Module {m['num']} — {m['icon']} {m['title']}"):
        col_a, col_b = st.columns([3, 2])
        with col_a:
            st.markdown(f"**{m['summary']}**")
            st.markdown(f"<span style='font-size:0.8rem;color:{m['color']};font-weight:600'>📋 Topics: {m['topics']}</span>", unsafe_allow_html=True)
        with col_b:
            st.markdown(f"""
            <div class="finance-lens" style="border-left-color:{m['color']}">
              <div class="finance-lens-title">💼 Finance Application</div>
              <div class="finance-lens-body">{m['finance']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"**✅ Learning outcome:** {m['outcome']}")


# ── KEY CONCEPTS REFERENCE ────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🔑 Essential AI Concepts — Quick Reference</div>', unsafe_allow_html=True)

with st.expander("📖 The 20 Most Important AI Terms for Finance Professionals"):
    search = st.text_input("🔍 Search concepts", placeholder="Type any term...")
    glossary = {
        "Algorithm": "A set of rules or instructions a computer follows to solve a problem. In ML, the algorithm learns its own rules from data.",
        "Machine Learning (ML)": "A subset of AI where systems learn from data to make predictions or decisions without being explicitly programmed.",
        "Training Data": "The historical dataset used to teach an ML model. Quality and volume directly determine model performance.",
        "Model": "The mathematical output of training — a function that maps inputs to predictions. E.g., a credit scoring model.",
        "Supervised Learning": "ML with labelled data (known correct answers). Used for classification (fraud yes/no) and regression (revenue forecast).",
        "Unsupervised Learning": "ML without labels — discovers hidden patterns such as customer clusters or journal entry anomalies.",
        "Overfitting": "When a model memorises training data and performs poorly on new data. A major model risk management concern.",
        "Neural Network": "A computational model of interconnected nodes (neurons) in layers. The foundation of Deep Learning.",
        "Transformer": "The architecture behind ChatGPT, Claude, and Gemini. Uses self-attention to process entire text sequences in parallel.",
        "Large Language Model (LLM)": "A transformer trained on massive text data. Can generate, summarise, and reason about text — the core of generative AI tools.",
        "Hallucination": "When an LLM generates plausible but factually incorrect output. Critical risk for financial figures and regulatory citations.",
        "Prompt Engineering": "The craft of writing effective instructions for LLMs to produce high-quality, accurate outputs.",
        "RAG (Retrieval-Augmented Generation)": "Connecting an LLM to your own documents — the model retrieves relevant content before answering. Essential for financial document Q&A.",
        "Embedding": "A numerical vector representation of text that captures semantic meaning. Similar concepts have similar vectors.",
        "Feature": "An individual input variable used by an ML model (e.g. invoice amount, customer DSO, payment terms).",
        "AUC-ROC": "Area Under the Receiver Operating Characteristic Curve. Standard performance metric for credit and fraud classification models.",
        "SHAP": "SHapley Additive exPlanations — explains why a model made a specific prediction. Required for model explainability in regulated finance.",
        "Bias": "Systematic unfairness in AI output caused by flawed training data or model design. Critical in credit, insurance, and employment AI.",
        "Model Risk Management": "Framework for governing AI models in financial institutions — documentation, validation, monitoring, and accountability.",
        "Agentic AI": "AI that can plan and execute multi-step tasks autonomously — the next frontier in finance workflow automation.",
    }
    for term, definition in glossary.items():
        if search.lower() in term.lower() or search.lower() in definition.lower() or not search:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{term}**")
            with col2:
                st.markdown(definition)
            st.divider()


# ── AI SKILLS OVERVIEW ────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🎯 AI Skills Every Finance Professional Needs</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🟢 Baseline (All Levels)", "🔵 Advanced (Senior)", "🟣 Leadership (CFO / FD)"])
with tab1:
    st.markdown("These skills are now **baseline requirements** — the new Excel proficiency.")
    baseline = ["AI concepts & vocabulary","Prompt engineering","Microsoft Copilot (Excel/Word)","AI output verification & hallucination awareness","Basic data literacy","AI ethics awareness"]
    st.markdown(" ".join([f'<span class="skill-pill">{s}</span>' for s in baseline]), unsafe_allow_html=True)
    st.markdown("\n**Start with:** Microsoft Learn Copilot for Finance (free) · AI For Everyone — Andrew Ng (Coursera, free audit)")

with tab2:
    st.markdown("These skills differentiate **senior finance professionals** in AI-augmented organisations.")
    advanced = ["ML model evaluation","Python / SQL basics","RAG implementation concepts","AI vendor assessment","Feature engineering","Model risk oversight","AI project specification"]
    st.markdown(" ".join([f'<span class="skill-pill">{s}</span>' for s in advanced]), unsafe_allow_html=True)
    st.markdown("\n**Start with:** Machine Learning Specialisation — Andrew Ng (Coursera) · DataCamp Python for Finance")

with tab3:
    st.markdown("These skills define the **AI-ready finance leader**.")
    leadership = ["AI strategy & roadmapping","AI governance framework design","Change management for AI","AI investment evaluation","Regulatory engagement","Board-level AI communication"]
    st.markdown(" ".join([f'<span class="skill-pill">{s}</span>' for s in leadership]), unsafe_allow_html=True)
    st.markdown("\n**Start with:** MIT Sloan AI Strategy · Deloitte AI Institute CFO Perspectives (free reports)")


# ── HOW TO USE THIS SERIES ────────────────────────────────────────────────────
st.markdown('<div class="section-heading">🧭 How to Use This Series</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Suggested learning paths:**

    **📘 Complete Beginner (no AI background)**
    Start at Module 1 → work through all 8 in order.
    Each module builds on the previous. Allow 25–40 min per module.

    **📗 Intermediate (uses AI tools daily)**
    Skim Module 1 → focus on Modules 4, 5, 7, 8.
    Use Module 6 if you want to build models yourself.

    **📙 Senior Professional / Manager**
    Focus on Modules 5, 7, 8 first (applications, governance, future).
    Then deepen with Modules 2, 3 for technical credibility.

    **📕 CFO / Finance Director**
    Start with Module 8 (future & career) → Module 7 (governance) →
    Module 5 (applications) → return to others as needed.
    """)
with col2:
    st.markdown("""
    **Each module includes:**

    - 📖 **Expandable topic sections** with full explanations
    - 💼 **Finance lens callouts** linking theory to your work
    - 🔑 **Key term highlights** and concept explanations
    - 🛠️ **Real tools** referenced for each application area
    - 🧩 **5-question interactive quiz** with instant feedback
    - 💡 **Key takeaways** — the 6 things to remember
    - 🔗 **Module navigation** to move through the series

    **Interactive features in specific modules:**
    - 🧪 Prompt builder (Module 4)
    - 🔧 AI project risk checker (Module 7)
    - 📋 Personal 90-day action plan (Module 8)
    - 💻 Python code examples (Module 6)
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Best Practice Tip</div>
      <div class="finance-lens-body">
        After each module, spend 15 minutes applying one concept to your current work.
        The finance professional who reads <i>and applies</i> advances fastest.
        AI literacy compounds — each module makes the next one clearer.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── SUBJECT SUMMARY ───────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📋 AI for Finance — Complete Subject Summary</div>', unsafe_allow_html=True)

with st.expander("📄 Read the Full Summary (Suitable for CPD Notes)", expanded=False):
    st.markdown("""
    ### Artificial Intelligence (AI) — Subject Summary for Finance & Accounting Professionals

    **1. What AI Is**
    Artificial Intelligence is the field of computer science building systems that perform
    tasks requiring human intelligence. Modern AI — specifically Machine Learning — learns
    rules from data rather than following rules programmed by humans. All current AI tools
    (ChatGPT, Copilot, fraud detection systems, credit scorecards) are Narrow AI: highly
    capable within their specific domain, unable to generalise outside it.

    **2. The Sub-field Hierarchy**
    AI contains Machine Learning as a subset; ML contains Deep Learning; Deep Learning
    contains Generative AI. Each layer adds specificity. A credit scoring model is ML. An
    invoice OCR system is Deep Learning (CNN). ChatGPT is Generative AI (transformer-based LLM).
    Knowing the layer helps finance professionals understand capabilities, limitations, and
    governance requirements.

    **3. How Machine Learning Works**
    Supervised learning (the most common finance use case) trains on labelled historical data
    to predict outputs on new data. Classification models predict categories (fraud vs not fraud);
    regression models predict continuous values (next quarter's revenue). Key algorithms include
    Logistic Regression (interpretable, regulatory-friendly), Random Forest (robust, handles
    complex interactions), and XGBoost (typically highest accuracy on tabular financial data).
    Model evaluation requires out-of-sample testing — training accuracy alone is meaningless.
    Overfitting is the primary model risk: a model that memorises training data fails on
    live data.

    **4. Deep Learning and Neural Networks**
    Neural networks learn by adjusting millions of numerical weights through backpropagation —
    iteratively reducing prediction error. CNNs process spatial data (invoice documents, scanned
    receipts). LSTMs handle sequential data (cash flow time series, transaction histories).
    Transformers — introduced in 2017 — process entire text sequences in parallel using
    self-attention, enabling the LLM revolution. The Transformer architecture underlies all
    major generative AI tools: GPT-4, Claude, Gemini, Copilot.

    **5. Generative AI and LLMs**
    Large Language Models are trained on hundreds of billions of text tokens, then fine-tuned
    using RLHF (Reinforcement Learning from Human Feedback) to follow instructions helpfully.
    Prompt engineering — writing effective instructions — is the most immediately valuable
    skill: specificity, role assignment, chain-of-thought reasoning, and output format
    instructions dramatically improve results. RAG (Retrieval-Augmented Generation) connects
    LLMs to proprietary documents, enabling financial document Q&A, contract analysis, and
    policy compliance checking grounded in actual source material. Hallucination — confident
    generation of factually incorrect content — is the primary risk: financial figures, tax
    rates, and regulatory citations must always be verified against primary sources.

    **6. AI Applications in Finance**
    AI is transforming every finance function. FP&A uses ML forecasting and AI-generated
    commentary. Audit uses population-wide anomaly detection replacing sampling. AP/AR
    automation uses computer vision for invoice processing and ML for collections prioritisation.
    Treasury uses LSTM-based cash forecasting and AI FX exposure detection. Tax uses document
    classification and LLM-assisted research. Compliance uses ML for AML transaction monitoring
    and computer vision for KYC. Investment management uses NLP for earnings analysis and
    alternative data processing. The 10-day financial close is becoming a 3-day close through
    AI orchestration of the close process.

    **7. Building AI Models**
    The ML pipeline has eight stages: problem definition, data collection, exploratory analysis,
    preprocessing, feature engineering, model training, evaluation, and deployment with ongoing
    monitoring. Finance domain knowledge is the most valuable input to feature engineering —
    understanding that disputed invoices almost always pay late, that government customers have
    longer payment cycles, and that month-end invoices are prioritised drives better features
    than algorithmic feature selection. Time-based train/test splits are mandatory for financial
    data — random splits leak future data into training, producing unrealistically optimistic
    results. XGBoost consistently outperforms alternatives on tabular financial data. SHAP
    values provide the post-hoc explainability required for model governance.

    **8. Ethics, Risk, and Governance**
    AI bias — systematic unfairness in model outputs — can emerge from historical data,
    proxy variables, and feedback loops without any malicious intent. Finance professionals
    must demand disaggregated testing across demographic groups for any model affecting
    individual financial decisions. Model Risk Management (SR 11-7, MAS TRM) requires
    documentation, independent validation, and ongoing monitoring. The EU AI Act classifies
    credit scoring as high-risk, requiring conformity assessment and human oversight. GDPR
    and Singapore PDPA impose consent, explainability, and data minimisation obligations on
    AI using personal data. Human accountability is non-delegable: the organisation deploying
    AI is fully responsible for its outcomes.

    **9. The Future and Career Implications**
    Agentic AI — capable of planning and executing multi-step finance workflows — represents
    the most significant near-term transformation: from reactive AI tools to proactive AI
    assistants managing entire processes. Federated learning enables privacy-preserving
    collaboration on financial data. Multimodal models process text, images, and audio
    together. AI does not eliminate finance roles — it eliminates the processing tasks within
    them. Finance professionals who adopt AI tools to handle data processing gain time for
    analysis, business partnering, governance, and strategic advisory — the activities that
    compound professional value. AI literacy is now a baseline professional competency,
    equivalent to Excel proficiency a decade ago.
    """)
    st.download_button(
        label="📥 Download Summary as Text",
        data="""Artificial Intelligence (AI) — Subject Summary for Finance & Accounting Professionals\n\nSee full content in Knowledge Folder AI Series Overview page.""",
        file_name="AI_Subject_Summary_Finance.txt",
        mime="text/plain"
    )


# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-card">
  <div class="cta-title">🚀 Ready to Begin?</div>
  <div class="cta-body">
    Start with Module 1 — Foundations of AI — and work through the series at your own pace.<br>
    Each module builds your understanding. Each quiz tests your retention.<br>
    Each finance lens connects the theory to your daily work.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("▶ Start with Module 1 — Foundations of AI", use_container_width=True):
        st.info("Navigate to **Module 1 — Foundations of AI** from the sidebar to begin.")

st.markdown("---")
st.caption("Knowledge Folder · AI Series · Overview Page · All 8 modules available in the sidebar · © 2025")