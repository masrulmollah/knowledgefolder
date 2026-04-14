"""
Machine Learning for Finance & Accounts
Module 1 – What is Machine Learning?

USAGE IN YOUR MULTI-PAGE APP
──────────────────────────────
This file must NOT call st.set_page_config().
Your homepage (or pages/ entry-point) should call it once, then:

    import ml_module_01
    ml_module_01.show()

Or if you use Streamlit's native pages/ folder, just place this file
there – Streamlit calls show() automatically if you define it, but
set_page_config() is still only allowed in the homepage.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# ── colour palette (matches a professional finance feel) ──────────────────────
PRIMARY   = "#4F46E5"   # indigo
SECONDARY = "#7C3AED"   # violet
ACCENT    = "#06B6D4"   # cyan
SUCCESS   = "#10B981"   # emerald
WARNING   = "#F59E0B"   # amber
DANGER    = "#EF4444"   # red
BG_CARD   = "#F8FAFC"


# ─────────────────────────────────────────────────────────────────────────────
def _css():
    st.markdown("""
    <style>
    /* ---------- page chrome ---------- */
    .main { background: #F1F5F9; }

    /* ---------- hero banner ---------- */
    .hero-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 60%, #06B6D4 100%);
        border-radius: 16px;
        padding: 2.4rem 2.8rem;
        color: white;
        margin-bottom: 1.6rem;
    }
    .hero-banner h1  { font-size: 2.1rem; margin: 0 0 .4rem; font-weight: 700; }
    .hero-banner p   { font-size: 1.05rem; margin: 0; opacity: .9; }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,.2);
        border: 1px solid rgba(255,255,255,.35);
        border-radius: 20px;
        padding: .18rem .8rem;
        font-size: .8rem;
        margin-bottom: .7rem;
        letter-spacing: .04em;
    }

    /* ---------- section headings ---------- */
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #1E293B;
        margin: 1.6rem 0 .6rem;
        padding-left: .6rem;
        border-left: 4px solid #4F46E5;
    }

    /* ---------- info / highlight cards ---------- */
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 1.1rem 1.3rem;
        box-shadow: 0 1px 6px rgba(0,0,0,.07);
        height: 100%;
    }
    .info-card .card-icon { font-size: 1.7rem; margin-bottom: .4rem; }
    .info-card h4 { font-size: 1rem; font-weight: 700; color: #1E293B; margin: 0 0 .3rem; }
    .info-card p  { font-size: .88rem; color: #475569; margin: 0; line-height: 1.55; }

    /* ---------- definition box ---------- */
    .definition-box {
        background: #EEF2FF;
        border-left: 5px solid #4F46E5;
        border-radius: 0 10px 10px 0;
        padding: 1rem 1.4rem;
        margin: 1rem 0;
    }
    .definition-box p { margin: 0; color: #1E293B; font-size: .96rem; line-height: 1.65; }

    /* ---------- comparison table header ---------- */
    .compare-head {
        background: #4F46E5;
        color: white;
        border-radius: 10px 10px 0 0;
        padding: .6rem 1.1rem;
        font-weight: 700;
        font-size: .95rem;
    }

    /* ---------- quiz styling ---------- */
    .quiz-box {
        background: white;
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        box-shadow: 0 2px 10px rgba(0,0,0,.08);
        margin-top: 1rem;
    }
    .quiz-q { font-weight: 700; color: #1E293B; font-size: 1rem; margin-bottom: .8rem; }

    /* ---------- progress pill ---------- */
    .progress-pill {
        display: inline-flex;
        align-items: center;
        gap: .4rem;
        background: #DCFCE7;
        color: #166534;
        border-radius: 20px;
        padding: .22rem .9rem;
        font-size: .82rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* ---------- key-term chip ---------- */
    .term-chip {
        display: inline-block;
        background: #EEF2FF;
        color: #4338CA;
        border: 1px solid #C7D2FE;
        border-radius: 6px;
        padding: .18rem .65rem;
        font-size: .82rem;
        margin: .18rem .18rem .18rem 0;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 1 — What is Machine Learning?</h1>
      <p>Build your conceptual foundation: understand what ML is, how it differs from
         traditional programming, and why it matters deeply for finance professionals.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    pills = [
        ("🎯", "Level",       "Beginner"),
        ("⏱️", "Read time",   "~25 minutes"),
        ("📋", "Topics",      "6 sections"),
        ("🏆", "Outcome",     "Core ML concepts"),
    ]
    for col, (icon, label, val) in zip([c1, c2, c3, c4], pills):
        col.markdown(f"""
        <div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;text-transform:uppercase;
             letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4>
        </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
def _section_what_is_ml():
    st.markdown('<div class="section-title">🤖 1. What Exactly is Machine Learning?</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="definition-box">
      <p><strong>Machine Learning (ML)</strong> is a branch of artificial intelligence where
      computer systems <em>learn from data</em> to make decisions or predictions —
      without being explicitly programmed with fixed rules. Instead of a programmer writing
      every rule, the algorithm finds patterns in historical data and uses those patterns
      on new data.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 💡 The simplest analogy for a finance professional")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
          <div class="card-icon">📜</div>
          <h4>Traditional Accounting Rule</h4>
          <p>
            "IF transaction amount &gt; $10,000 AND country is on watchlist
            THEN flag as suspicious."<br><br>
            A human expert wrote every condition.
            Works well — until fraudsters learn the rule.
          </p>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
          <div class="card-icon">🧠</div>
          <h4>Machine Learning Approach</h4>
          <p>
            Show the system 10 million past transactions, labelled
            "fraud" or "legitimate". It discovers <em>hundreds</em> of
            subtle patterns — time of day, device, merchant category,
            velocity — that no human could hand-code.
          </p>
        </div>""", unsafe_allow_html=True)

    st.markdown("#### 🔑 Key terms you will see throughout this course")
    terms = ["Algorithm", "Model", "Training data", "Features",
             "Labels / Target", "Prediction", "Accuracy", "Overfitting",
             "Deployment", "Inference"]
    chips = "".join(f'<span class="term-chip">{t}</span>' for t in terms)
    st.markdown(chips, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
def _section_traditional_vs_ml():
    st.markdown('<div class="section-title">⚖️ 2. Traditional Programming vs. Machine Learning</div>',
                unsafe_allow_html=True)

    data = {
        "Aspect": [
            "How rules are created",
            "Who creates the rules",
            "Handles new patterns?",
            "Scales with more data?",
            "Example in finance",
        ],
        "Traditional Programming": [
            "Manually written by developers",
            "Human expert + programmer",
            "❌  Must rewrite rules",
            "❌  Same rules regardless",
            "IF overdue > 90 days THEN bad debt",
        ],
        "Machine Learning": [
            "Learned automatically from data",
            "Data + ML algorithm",
            "✅  Retrains on new data",
            "✅  Gets smarter with more data",
            "Predict bad debt probability (0–100%)",
        ],
    }
    df = pd.DataFrame(data)
    st.dataframe(
        df.style
          .set_properties(subset=["Traditional Programming"],
                          **{"background-color": "#FFF7ED", "color": "#1E293B"})
          .set_properties(subset=["Machine Learning"],
                          **{"background-color": "#F0FDF4", "color": "#1E293B"})
          .set_table_styles([{
              "selector": "th",
              "props": [("background-color", "#4F46E5"),
                        ("color", "white"), ("font-weight", "700"),
                        ("font-size", "0.9rem")]
          }]),
        use_container_width=True, hide_index=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
def _section_types_of_ml():
    st.markdown('<div class="section-title">🗂️ 3. The Three Types of Machine Learning</div>',
                unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(
        ["🏷️ Supervised Learning", "🔍 Unsupervised Learning", "🎮 Reinforcement Learning"]
    )

    with tab1:
        c1, c2 = st.columns([1.4, 1])
        with c1:
            st.markdown("""
            **What it is:** The algorithm learns from *labelled* examples —
            data where the correct answer is already known.

            **Analogy:** Like a student studying past exam papers with answer keys.

            **In finance:**
            - 🏦 Credit scoring — labelled "default" / "no default"
            - 💳 Fraud detection — labelled "fraud" / "legitimate"
            - 📈 Revenue forecasting — past revenue figures as labels
            - 📊 Expense classification — GL codes as labels
            """)
        with c2:
            fig = go.Figure(go.Indicator(
                mode="gauge+number", value=72,
                title={"text": "Sample Credit Score", "font": {"size": 14}},
                gauge={
                    "axis": {"range": [300, 900]},
                    "bar": {"color": PRIMARY},
                    "steps": [
                        {"range": [300, 580], "color": "#FEE2E2"},
                        {"range": [580, 720], "color": "#FEF3C7"},
                        {"range": [720, 900], "color": "#D1FAE5"},
                    ],
                },
                number={"suffix": "%", "font": {"size": 24}},
            ))
            fig.update_layout(height=230, margin=dict(t=30, b=10, l=20, r=20),
                              paper_bgcolor="rgba(0,0,0,0)", font_color="#1E293B")
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        c1, c2 = st.columns([1.4, 1])
        with c1:
            st.markdown("""
            **What it is:** The algorithm finds hidden patterns in data that has
            *no labels* — it groups or organises data on its own.

            **Analogy:** Like sorting a pile of receipts into categories without
            being told the categories first.

            **In finance:**
            - 👥 Customer segmentation by spending behaviour
            - 🔎 Detecting unusual journal entries (anomaly detection)
            - 📑 Grouping similar vendors or suppliers
            - 🗺️ Mapping related accounts automatically
            """)
        with c2:
            # simple scatter simulating clusters
            import numpy as np
            np.random.seed(42)
            x1, y1 = np.random.normal(2, .5, 30), np.random.normal(3, .5, 30)
            x2, y2 = np.random.normal(5, .5, 30), np.random.normal(1.5, .4, 30)
            x3, y3 = np.random.normal(4, .4, 20), np.random.normal(5, .4, 20)
            fig2 = go.Figure()
            for x, y, name, color in [
                (x1, y1, "High-value clients", PRIMARY),
                (x2, y2, "SME clients",        SUCCESS),
                (x3, y3, "At-risk clients",    WARNING),
            ]:
                fig2.add_trace(go.Scatter(
                    x=x, y=y, mode="markers", name=name,
                    marker=dict(color=color, size=7, opacity=.75)
                ))
            fig2.update_layout(
                title="Customer clusters (unsupervised)",
                title_font_size=12,
                height=230, margin=dict(t=34, b=10, l=10, r=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="#1E293B",
                legend=dict(font_size=10),
                xaxis=dict(showgrid=True, gridcolor="#E2E8F0", title="Avg transaction value"),
                yaxis=dict(showgrid=True, gridcolor="#E2E8F0", title="Transaction frequency"),
            )
            st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        st.markdown("""
        **What it is:** An agent learns by *trial and error*, receiving rewards for
        good decisions and penalties for bad ones — like training a dog.

        **In finance (emerging uses):**
        - 🤖 Algorithmic trading strategies
        - 💹 Dynamic portfolio rebalancing
        - 🎯 Optimising loan offer pricing in real time

        > **Note for finance professionals:** Reinforcement learning is more common
        in fintech and investment banks. Modules 1–9 focus on supervised and
        unsupervised learning, which are most directly applicable to accounting
        and corporate finance.
        """)
        st.info("📌 This module focuses mainly on supervised and unsupervised learning "
                "as these are most relevant to day-to-day finance and accounting work.")


# ─────────────────────────────────────────────────────────────────────────────
def _section_ml_workflow():
    st.markdown('<div class="section-title">🔄 4. The Machine Learning Workflow</div>',
                unsafe_allow_html=True)
    st.markdown("Every ML project — regardless of industry — follows the same six steps:")

    steps = [
        ("1️⃣", "Define the Problem",
         "What do you want to predict or discover?\n\nExample: *Predict which invoices will be paid late.*"),
        ("2️⃣", "Collect & Prepare Data",
         "Gather historical data. Clean it. Handle missing values.\n\nExample: *3 years of invoice records with payment dates.*"),
        ("3️⃣", "Choose & Train a Model",
         "Select an algorithm and feed it the training data.\n\nExample: *Train a Random Forest on 80% of invoices.*"),
        ("4️⃣", "Evaluate the Model",
         "Test it on unseen data. Measure accuracy.\n\nExample: *Does it correctly flag 85% of late payments?*"),
        ("5️⃣", "Improve & Tune",
         "Adjust the model, add features, try other algorithms.\n\nExample: *Add 'customer industry' as a feature — accuracy rises to 91%.*"),
        ("6️⃣", "Deploy & Monitor",
         "Put the model into production. Monitor for drift.\n\nExample: *Integrate into accounts receivable system.*"),
    ]

    col_pairs = [st.columns(3), st.columns(3)]
    for i, (num, title, desc) in enumerate(steps):
        row, col = divmod(i, 3)
        with col_pairs[row][col]:
            st.markdown(f"""
            <div class="info-card">
              <div class="card-icon">{num}</div>
              <h4>{title}</h4>
              <p>{desc.replace(chr(10), '<br>')}</p>
            </div>""", unsafe_allow_html=True)
            st.markdown("")  # spacing


# ─────────────────────────────────────────────────────────────────────────────
def _section_finance_applications():
    st.markdown('<div class="section-title">💼 5. ML Applications — Finance & Accounts at a Glance</div>',
                unsafe_allow_html=True)

    data = {
        "Finance / Accounts Task": [
            "Fraud & anomaly detection",
            "Credit risk scoring",
            "Cash flow forecasting",
            "Invoice / expense classification",
            "Accounts receivable prediction",
            "Audit analytics",
            "Financial statement analysis",
            "Regulatory compliance monitoring",
        ],
        "ML Type": [
            "Unsupervised + Supervised",
            "Supervised",
            "Supervised (Time Series)",
            "Supervised",
            "Supervised",
            "Unsupervised + Supervised",
            "NLP + Supervised",
            "Supervised + NLP",
        ],
        "Benefit": [
            "Catches fraud missed by rule-based systems",
            "Faster, more accurate lending decisions",
            "More accurate budgets and liquidity planning",
            "Automates manual GL coding",
            "Prioritise collections — improve DSO",
            "Identify risky journal entries automatically",
            "Flag unusual ratios, detect earnings management",
            "Monitor transactions against regulations 24/7",
        ],
        "Module covered": [4, 3, 5, 3, 3, 7, 6, 7],
    }
    df = pd.DataFrame(data)

    def colour_type(val):
        m = {"Supervised": "background-color:#DBEAFE;color:#1E3A5F",
             "Unsupervised": "background-color:#D1FAE5;color:#064E3B",
             "NLP": "background-color:#EDE9FE;color:#2E1065"}
        for k, v in m.items():
            if k in val:
                return v
        return ""

    st.dataframe(
        df.style.applymap(colour_type, subset=["ML Type"])
          .set_table_styles([{
              "selector": "th",
              "props": [("background-color", "#4F46E5"), ("color", "white"),
                        ("font-weight", "700"), ("font-size", "0.88rem")]
          }])
          .format({"Module covered": "Module {}"}),
        use_container_width=True, hide_index=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
def _section_ai_ml_landscape():
    st.markdown('<div class="section-title">🗺️ 6. Where Does ML Sit? AI Landscape Overview</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.3])
    with col1:
        st.markdown("""
        Understanding the vocabulary prevents confusion when reading industry reports
        or talking to data teams.

        | Term | Meaning |
        |------|---------|
        | **Artificial Intelligence (AI)** | Broad field — machines mimicking human intelligence |
        | **Machine Learning (ML)** | AI subset — learning from data |
        | **Deep Learning (DL)** | ML subset — neural networks with many layers |
        | **Generative AI** | DL subset — creates text, images, code (GPT, etc.) |
        | **Data Science** | Overlapping discipline using statistics + ML |

        > 🔖 All ChatGPT-style tools are **Generative AI → Deep Learning → ML → AI**.
        When a bank says "AI credit scoring" they usually mean **supervised ML**.
        """)
    with col2:
        labels = ["AI", "Machine Learning", "Deep Learning", "Generative AI"]
        parents = ["", "AI", "Machine Learning", "Deep Learning"]
        values = [100, 60, 30, 12]
        colors = [PRIMARY, SECONDARY, ACCENT, SUCCESS]
        fig = go.Figure(go.Treemap(
            labels=labels, parents=parents, values=values,
            marker=dict(colors=colors),
            textinfo="label",
            textfont=dict(size=14, color="white"),
        ))
        fig.update_layout(
            height=280, margin=dict(t=10, b=10, l=10, r=10),
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 1 Quiz</div>',
                unsafe_allow_html=True)
    st.markdown("Test your understanding before moving to Module 2.")

    questions = [
        {
            "q": "Q1. A bank uses historical loan data (labelled 'default' / 'no default') "
                 "to build a model that predicts whether a new applicant will default. "
                 "What type of ML is this?",
            "opts": ["Unsupervised Learning", "Supervised Learning",
                     "Reinforcement Learning", "Deep Learning"],
            "ans": "Supervised Learning",
            "exp": "✅ Correct! Because the training data has labels (default / no default), "
                   "the algorithm is supervised.",
        },
        {
            "q": "Q2. Your company wants to group 50,000 customers into segments "
                 "based on payment behaviour — with no pre-defined categories. "
                 "Which type of ML is most appropriate?",
            "opts": ["Supervised Learning", "Reinforcement Learning",
                     "Unsupervised Learning", "None — this requires rules-based logic"],
            "ans": "Unsupervised Learning",
            "exp": "✅ Correct! No labels exist, so an unsupervised clustering algorithm "
                   "(like K-Means) would discover the segments.",
        },
        {
            "q": "Q3. Which step in the ML workflow comes BEFORE training a model?",
            "opts": ["Deploy & Monitor", "Evaluate the model",
                     "Collect & Prepare Data", "Improve & Tune"],
            "ans": "Collect & Prepare Data",
            "exp": "✅ Correct! Data must be collected, cleaned and prepared before "
                   "any model can be trained.",
        },
    ]

    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"""<div class="quiz-box">
          <div class="quiz-q">{q['q']}</div>""", unsafe_allow_html=True)
        choice = st.radio("Select your answer:", q["opts"],
                          key=f"mod1_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]:
                st.success(q["exp"])
                score += 1
            else:
                st.error(f"❌ Not quite. The correct answer is **{q['ans']}**.\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("")

    answered = sum(
        1 for i in range(len(questions))
        if st.session_state.get(f"mod1_q{i}") is not None
    )
    if answered == len(questions):
        pct = int(score / len(questions) * 100)
        if pct == 100:
            st.balloons()
            st.success(f"🏆 Perfect score — {score}/{len(questions)}! "
                       "You're ready for Module 2.")
        elif pct >= 67:
            st.info(f"👍 Good effort — {score}/{len(questions)}. "
                    "Review the sections above before moving on.")
        else:
            st.warning(f"📖 Score: {score}/{len(questions)}. "
                       "We recommend re-reading sections 1–3 before continuing.")


# ─────────────────────────────────────────────────────────────────────────────
def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 Machine Learning for Finance & Accounts**  \nModule 1 of 10")
    c2.markdown(
        "<div style='text-align:center'>"
        "<span style='background:#EEF2FF;color:#4338CA;border-radius:6px;"
        "padding:.2rem .7rem;font-weight:600'>Module 1</span>"
        " → "
        "<a href='?module=2' style='text-decoration:none;color:#4F46E5'>Module 2 ▶</a>"
        "</div>",
        unsafe_allow_html=True,
    )
    c3.markdown(
        "<div style='text-align:right;color:#64748B;font-size:.85rem'>"
        "Knowledge Folder · Finance & Accounts Series</div>",
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
def show():
    """
    Entry point.  Call this from your homepage or pages/ file.
    Do NOT call st.set_page_config() here.
    """
    _css()
    _hero()

    st.markdown('<div class="progress-pill">✅ Foundation Level · Start here</div>',
                unsafe_allow_html=True)

    # ── Sidebar navigation ────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("### 📑 Module 1 — Sections")
        st.markdown("""
        1. What is Machine Learning?
        2. Traditional vs. ML
        3. Three types of ML
        4. ML Workflow
        5. Finance Applications
        6. AI Landscape
        ---
        🧩 Knowledge Check
        """)
        st.markdown("---")
        st.markdown("**Your progress**")
        st.progress(10, text="Module 1 / 10")

    # ── Main content ──────────────────────────────────────────────────────────
    _section_what_is_ml()
    st.markdown("")
    _section_traditional_vs_ml()
    st.markdown("")
    _section_types_of_ml()
    st.markdown("")
    _section_ml_workflow()
    st.markdown("")
    _section_finance_applications()
    st.markdown("")
    _section_ai_ml_landscape()
    st.markdown("")
    _knowledge_check()
    _footer()


# ── Allow running this file directly for local testing ────────────────────────
if __name__ == "__main__":
    st.set_page_config(
        page_title="Module 1 – What is Machine Learning? | Knowledge Folder",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    show()