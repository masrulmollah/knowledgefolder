import streamlit as st

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #f5f3ee;
    color: #1a1a2e;
}

/* Hero Banner */
.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "§";
    position: absolute;
    right: 40px;
    top: 10px;
    font-size: 180px;
    color: rgba(255,255,255,0.04);
    font-family: 'Playfair Display', serif;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    color: #e2d9c5;
    margin: 0 0 8px 0;
}
.hero p {
    color: #a8b2c8;
    font-size: 1.05rem;
    margin: 0;
    font-weight: 300;
}
.hero .badge {
    display: inline-block;
    background: rgba(226,217,197,0.15);
    color: #e2d9c5;
    border: 1px solid rgba(226,217,197,0.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

/* Topic Cards */
.topic-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 16px;
    border-left: 4px solid #0f3460;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    transition: box-shadow 0.2s;
}
.topic-card:hover {
    box-shadow: 0 6px 24px rgba(0,0,0,0.1);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #0f3460;
    margin: 0 0 10px 0;
}
.topic-card p {
    font-size: 0.96rem;
    line-height: 1.75;
    color: #3a3a4a;
    margin: 0;
}

/* Key Term Pills */
.key-terms {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 12px;
}
.term-pill {
    background: #eef2ff;
    color: #0f3460;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid #c7d2fe;
}

/* Takeaway box */
.takeaway {
    background: linear-gradient(135deg, #fff9ee, #fff3d6);
    border: 1px solid #f5d78e;
    border-radius: 10px;
    padding: 14px 18px;
    margin-top: 12px;
    font-size: 0.9rem;
    color: #5a4000;
}
.takeaway strong {
    color: #b8860b;
}

/* Section Divider */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: #1a1a2e;
    margin: 32px 0 16px 0;
    padding-bottom: 8px;
    border-bottom: 2px solid #e0dbd0;
}

/* Progress indicator */
.progress-bar {
    background: #e0dbd0;
    border-radius: 10px;
    height: 6px;
    margin-bottom: 32px;
    overflow: hidden;
}
.progress-fill {
    background: linear-gradient(90deg, #0f3460, #e94560);
    height: 100%;
    width: 12.5%;
    border-radius: 10px;
}
.progress-label {
    font-size: 0.78rem;
    color: #888;
    margin-bottom: 6px;
    letter-spacing: 0.5px;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #1a1a2e;
}
section[data-testid="stSidebar"] * {
    color: #c8d0e0 !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📘 Module 1 of 8</div>
    <h1>Foundations of Economics</h1>
    <p>Build the bedrock understanding every finance professional needs — scarcity, choice, systems, and the core economic problem.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label">SYLLABUS PROGRESS — MODULE 1 / 8</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📘 Module 1 Topics")
    st.markdown("""
- 1.1 What is Economics?
- 1.2 Micro vs Macro
- 1.3 Economic Systems
- 1.4 The Basic Economic Problem
""")
    st.markdown("---")
    st.markdown("### 📚 All Modules")
    st.markdown("""
- ✅ **Module 1** – Foundations *(current)*
- ⬜ Module 2 – Microeconomics
- ⬜ Module 3 – Macroeconomics
- ⬜ Module 4 – Money & Banking
- ⬜ Module 5 – Monetary & Fiscal Policy
- ⬜ Module 6 – International Economics
- ⬜ Module 7 – Financial Economics
- ⬜ Module 8 – Contemporary Issues
""")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📖 Topic Summaries</div>', unsafe_allow_html=True)

topics = [
    {
        "number": "1.1",
        "title": "What is Economics? — Scarcity, Choice & Opportunity Cost",
        "summary": (
            "Economics is the study of how individuals, businesses, and governments allocate "
            "limited resources to satisfy unlimited wants. At its heart lies the concept of "
            "<b>scarcity</b> — resources like time, money, land, and labour are finite, forcing "
            "us to make choices. Every choice involves a trade-off. The value of the next best "
            "alternative foregone is called the <b>Opportunity Cost</b> — a crucial concept in "
            "finance when evaluating investment decisions, capital allocation, or even career choices."
        ),
        "terms": ["Scarcity", "Opportunity Cost", "Trade-off", "Resource Allocation", "Rationality"],
        "takeaway": "💡 <strong>Finance Lens:</strong> Every capital allocation decision carries an opportunity cost. Choosing to invest in Project A means forgoing returns from Project B — economics formalises this thinking."
    },
    {
        "number": "1.2",
        "title": "Microeconomics vs Macroeconomics",
        "summary": (
            "<b>Microeconomics</b> focuses on individual units — households, firms, and markets. "
            "It explains how prices are set, how consumers decide what to buy, and how firms "
            "determine output. <b>Macroeconomics</b>, on the other hand, looks at the economy as "
            "a whole — national output (GDP), inflation, unemployment, and government policy. "
            "For finance professionals, both matter: micro helps in company valuation and industry "
            "analysis, while macro drives asset allocation, interest rate views, and portfolio strategy."
        ),
        "terms": ["Microeconomics", "Macroeconomics", "Market", "GDP", "Inflation", "Firm Behaviour"],
        "takeaway": "💡 <strong>Finance Lens:</strong> A stock analyst uses microeconomics (firm-level costs, pricing power), while a fund manager uses macroeconomics (rate cycles, GDP trends) for asset allocation."
    },
    {
        "number": "1.3",
        "title": "Economic Systems — Capitalism, Socialism & Mixed Economy",
        "summary": (
            "An <b>economic system</b> defines how a society organises production, distribution, "
            "and consumption. In a <b>Capitalist (Market) Economy</b>, private individuals own "
            "resources and markets determine prices — profit is the motivator. In a "
            "<b>Socialist (Command) Economy</b>, the government owns and plans economic activity. "
            "Most real-world economies are <b>Mixed Economies</b> — combining market forces with "
            "government intervention. The degree of state involvement shapes tax policy, regulatory "
            "environment, and business risk — all critical for cross-border financial analysis."
        ),
        "terms": ["Capitalism", "Socialism", "Mixed Economy", "Command Economy", "Free Market", "Privatisation"],
        "takeaway": "💡 <strong>Finance Lens:</strong> Understanding a country's economic system is essential for sovereign risk analysis, FDI decisions, and assessing regulatory risk in emerging markets."
    },
    {
        "number": "1.4",
        "title": "The Basic Economic Problem — What, How & For Whom to Produce",
        "summary": (
            "Every economy — regardless of its system — must answer three fundamental questions: "
            "<b>What to produce?</b> (Which goods and services, and in what quantity?) "
            "<b>How to produce?</b> (What combination of labour, capital, and technology?) "
            "<b>For whom to produce?</b> (Who gets the output — based on income, need, or merit?) "
            "These questions shape government budgets, corporate strategy, and social policy. "
            "In financial analysis, understanding a government's answer to 'for whom' reveals "
            "spending priorities, welfare commitments, and fiscal sustainability."
        ),
        "terms": ["Production", "Distribution", "Factors of Production", "Resource Utilisation", "Welfare", "Fiscal Policy"],
        "takeaway": "💡 <strong>Finance Lens:</strong> Government spending patterns (healthcare vs infrastructure vs defence) reflect their 'for whom' priorities — directly impacting sectoral investment opportunities."
    },
]

for topic in topics:
    with st.expander(f"📌 {topic['number']} — {topic['title']}", expanded=False):
        st.markdown(f"""
        <div class="topic-card">
            <h3>{topic['number']} {topic['title']}</h3>
            <p>{topic['summary']}</p>
            <div class="key-terms">
                {''.join([f'<span class="term-pill">{t}</span>' for t in topic['terms']])}
            </div>
            <div class="takeaway">{topic['takeaway']}</div>
        </div>
        """, unsafe_allow_html=True)

# ─── Quick Revision Quiz ─────────────────────────────────────────────────────
st.markdown('<div class="section-title">🧠 Quick Revision Check</div>', unsafe_allow_html=True)

q1 = st.radio(
    "1. A company decides to invest ₹10 Cr in Plant A instead of Plant B (which would have returned ₹1.5 Cr). What is the opportunity cost?",
    ["₹10 Cr", "₹1.5 Cr", "The profit from Plant A", "Zero"],
    index=None
)
if q1 == "₹1.5 Cr":
    st.success("✅ Correct! The opportunity cost is the return from the best foregone alternative — Plant B's ₹1.5 Cr.")
elif q1:
    st.error("❌ Not quite. Opportunity cost = value of the next best alternative foregone = ₹1.5 Cr from Plant B.")

q2 = st.radio(
    "2. Which branch of economics would a portfolio manager use when assessing the impact of rising interest rates on bond prices?",
    ["Microeconomics", "Macroeconomics", "Behavioural Economics", "Development Economics"],
    index=None
)
if q2 == "Macroeconomics":
    st.success("✅ Correct! Interest rates are a macroeconomic variable that affects the economy at the aggregate level.")
elif q2:
    st.error("❌ Interest rates are a macroeconomic concept — they affect the entire economy, not just individual markets.")

q3 = st.radio(
    "3. India is best described as which type of economic system?",
    ["Pure Capitalist Economy", "Command Economy", "Mixed Economy", "Socialist Economy"],
    index=None
)
if q3 == "Mixed Economy":
    st.success("✅ Correct! India operates a mixed economy — with both private enterprise and significant government participation.")
elif q3:
    st.error("❌ India combines market forces with government intervention — making it a Mixed Economy.")

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown("⬅️ *No previous module*")
with col2:
    st.markdown("<div style='text-align:center; color:#888; font-size:0.85rem;'>Module 1 of 8 — Foundations of Economics</div>", unsafe_allow_html=True)
with col3:
    st.markdown("➡️ **Next: Module 2 — Microeconomics**")