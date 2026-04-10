import streamlit as st

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #f0f9ff;
    color: #1a1a2e;
}

/* Hero Banner - Teal/Azure Gradient for International Economics */
.hero {
    background: linear-gradient(135deg, #0d9488 0%, #0891b2 60%, #0284c7 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "🌐";
    position: absolute;
    right: 40px;
    top: -10px;
    font-size: 150px;
    color: rgba(255,255,255,0.05);
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    color: #ffffff;
    margin: 0 0 8px 0;
}
.hero p {
    color: #ccfbf1;
    font-size: 1.05rem;
    margin: 0;
    font-weight: 300;
}
.hero .badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    color: #ffffff;
    border: 1px solid rgba(255,255,255,0.3);
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
    border-left: 4px solid #0891b2;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #0d4a4e;
    margin: 0 0 10px 0;
}
.topic-card p {
    font-size: 0.96rem;
    line-height: 1.8;
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
    background: #f0fdfa;
    color: #0d9488;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid #ccfbf1;
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

/* Progress indicator */
.progress-bar {
    background: #e5e7eb;
    border-radius: 10px;
    height: 6px;
    margin-bottom: 32px;
    overflow: hidden;
}
.progress-fill {
    background: linear-gradient(90deg, #0d9488, #0ea5e9);
    height: 100%;
    width: 75%;
}

/* Sidebar styling */
section[data-testid="stSidebar"] { background-color: #0d4a4e; }
section[data-testid="stSidebar"] * { color: #ccfbf1 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📘 Module 6 of 8</div>
    <h1>International Economics</h1>
    <p>Navigate the complexities of global markets. Understand the drivers of international trade, currency exchange dynamics, and the architecture of the global financial system.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label" style="font-size: 0.78rem; color: #6b7280; margin-bottom: 6px;">SYLLABUS PROGRESS — MODULE 6 / 8</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📘 Module 6 Topics")
    st.markdown("""
- 6.1 International Trade Theories
- 6.2 Trade Barriers & Protections
- 6.3 Foreign Exchange Markets
- 6.4 Balance of Payments (BoP)
- 6.5 Economic Integration (EU/WTO)
""")
    st.markdown("---")
    st.markdown("### 📚 All Modules")
    st.markdown("- ✅ Module 1-5 Complete\n- ✅ **Module 6** – International\n- ⬜ Module 7 – Financial\n- ⬜ Module 8 – Contemporary")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #ccfbf1; padding-bottom: 8px;">📖 Topic Summaries</h2>', unsafe_allow_html=True)

# ── 6.1 Trade Theories
with st.expander("📌 6.1 — International Trade Theories", expanded=True):
    st.markdown("""
    <div class="topic-card">
        <h3>Comparative Advantage</h3>
        <p>Why do nations trade? David Ricardo's <b>Comparative Advantage</b> theory suggests that countries should specialize in producing goods where they have the lowest opportunity cost, even if they aren't the absolute best at it.</p>
        <div class="key-terms">
            <span class="term-pill">Absolute Advantage</span> <span class="term-pill">Opportunity Cost</span> <span class="term-pill">Specialization</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 6.2 Trade Barriers
with st.expander("📌 6.2 — Trade Barriers & Protectionism", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Tariffs, Quotas & Embargoes</h3>
        <p>Governments often restrict trade to protect domestic industries. Common tools include <b>Tariffs</b> (taxes on imports) and <b>Quotas</b> (physical limits on volume).</p>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> For manufacturing, high tariffs on raw materials increase the "Landing Cost," directly impacting product pricing and competitiveness.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 6.3 Foreign Exchange
with st.expander("📌 6.3 — Foreign Exchange Markets", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Currency Dynamics</h3>
        <p>The <b>Forex</b> market determines the value of one currency against another. Exchange rates are influenced by interest rates, inflation, and trade balances.</p>
        <div class="key-terms">
            <span class="term-pill">Appreciation</span> <span class="term-pill">Depreciation</span> <span class="term-pill">Fixed vs Floating</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Currency depreciation makes exports cheaper but imports more expensive, necessitating robust FX hedging strategies.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 6.4 Balance of Payments
with st.expander("📌 6.4 — Balance of Payments (BoP)", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>The National Ledger</h3>
        <p>The <b>BoP</b> records all economic transactions between residents of a country and the rest of the world. It consists of the <b>Current Account</b> (Trade, Services) and the <b>Capital Account</b> (Investment, Debt).</p>
    </div>
    """, unsafe_allow_html=True)

# ── 6.5 Economic Integration
with st.expander("📌 6.5 — Economic Integration & WTO", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Global Governance</h3>
        <p>International trade is governed by bodies like the <b>World Trade Organization (WTO)</b> and regional blocs like the <b>EU</b> or <b>ASEAN</b>. These entities aim to reduce barriers and standardize trade rules.</p>
        <div class="key-terms">
            <span class="term-pill">Free Trade Agreement</span> <span class="term-pill">WTO</span> <span class="term-pill">Trade Blocs</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── Interactive: Exchange Rate Impact ──────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #ccfbf1; padding-bottom: 8px;">💹 Interactive: FX Margin Calculator</h2>', unsafe_allow_html=True)

base_price = st.number_input("Unit Cost in Local Currency", value=100.0)
fx_rate = st.slider("Exchange Rate (1 USD = X Local)", 50.0, 150.0, 110.0)

usd_cost = base_price / fx_rate
st.metric("Landed Cost in USD", f"${usd_cost:.2f}")

# ─── Knowledge Check ─────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #ccfbf1; padding-bottom: 8px;">🧠 Module 6 Knowledge Check</h2>', unsafe_allow_html=True)

q1 = st.radio(
    "1. If a country's currency appreciates significantly, what is the likely impact on its exports?",
    ["Exports become cheaper and more competitive", "Exports become more expensive for foreign buyers", "No impact"],
    index=None, key="m6q1"
)
if q1 == "Exports become more expensive for foreign buyers":
    st.success("✅ Correct! Appreciation raises the price of domestic goods for international markets.")

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1:
    st.markdown("⬅️ **Previous: Module 5**")
with nav_col2:
    st.markdown("<div style='text-align:center; color:#888; font-size:0.85rem;'>Module 6 of 8</div>", unsafe_allow_html=True)
with nav_col3:
    st.markdown("➡️ **Next: Module 7**")