import streamlit as st

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #f9fafb;
    color: #1a1a2e;
}

/* Hero Banner - Indigo/Violet Gradient */
.hero {
    background: linear-gradient(135deg, #312e81 0%, #4338ca 60%, #5b21b6 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "₿";
    position: absolute;
    right: 40px;
    top: -10px;
    font-size: 180px;
    color: rgba(255,255,255,0.05);
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    color: #ffffff;
    margin: 0 0 8px 0;
}
.hero p {
    color: #e0e7ff;
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
    border-left: 4px solid #4338ca;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #312e81;
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
    background: #eef2ff;
    color: #4338ca;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid #e0e7ff;
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
    background: linear-gradient(90deg, #4338ca, #6366f1);
    height: 100%;
    width: 50%;
}

/* Sidebar styling */
section[data-testid="stSidebar"] { background-color: #312e81; }
section[data-testid="stSidebar"] * { color: #e0e7ff !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📘 Module 4 of 8</div>
    <h1>Money & Banking</h1>
    <p>Explore the architecture of financial systems. Understand the evolution of money, the role of commercial banks, and the rise of digital assets.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label" style="font-size: 0.78rem; color: #6b7280; margin-bottom: 6px;">SYLLABUS PROGRESS — MODULE 4 / 8</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📘 Module 4 Topics")
    st.markdown("""
- 4.1 Functions of Money
- 4.2 Commercial Banks
- 4.3 Central Banking
- 4.4 Money Supply (M1, M2)
- 4.5 The Credit Multiplier
- 4.6 Digital Money & Crypto
""")
    st.markdown("---")
    st.markdown("### 📚 All Modules")
    st.markdown("- ✅ Module 1 – Foundations\n- ✅ Module 2 – Microeconomics\n- ✅ Module 3 – Macroeconomics\n- ✅ **Module 4** – Money & Banking\n- ⬜ Module 5 – Monetary & Fiscal Policy")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #e0e7ff; padding-bottom: 8px;">📖 Topic Summaries</h2>', unsafe_allow_html=True)

# ── 4.1 Functions of Money
with st.expander("📌 4.1 — Functions and Types of Money", expanded=True):
    st.markdown("""
    <div class="topic-card">
        <h3>The Triple Role of Money</h3>
        <p>Money is a tool that facilitates economic activity through three functions: <b>Medium of Exchange</b> (buying/selling), <b>Unit of Account</b> (pricing), and <b>Store of Value</b> (saving).</p>
        <div class="key-terms">
            <span class="term-pill">Fiat Money</span> <span class="term-pill">Liquidity</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 4.2 Commercial Banking
with st.expander("📌 4.2 — Role of Commercial Banks", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Financial Intermediation</h3>
        <p>Banks pool deposits from savers and provide credit to borrowers. This process is essential for capital formation and the efficient allocation of resources within an economy.</p>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Commercial banks are the primary source of credit lines for industrial working capital and trade finance.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 4.3 Central Banking
with st.expander("📌 4.3 — Central Banking", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Monetary Authority</h3>
        <p>The Central Bank oversees the banking system, manages interest rates, and serves as the lender of last resort during financial crises to maintain systemic stability.</p>
    </div>
    """, unsafe_allow_html=True)

# ── 4.4 Money Supply
with st.expander("📌 4.4 — Money Supply Aggregates", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>M1 and M2</h3>
        <p>Economists track different levels of money. <b>M1</b> includes the most liquid assets (cash and checking accounts), while <b>M2</b> adds "near money" like savings deposits and time deposits.</p>
    </div>
    """, unsafe_allow_html=True)

# ── 4.5 Credit Multiplier
with st.expander("📌 4.5 — The Credit Multiplier", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>How Banks Create Money</h3>
        <p>Through fractional reserve banking, banks lend out deposits, which are then re-deposited and lent again. This creates a ripple effect that expands the total money supply.</p>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"Credit Multiplier = \frac{1}{Reserve Ratio}")

# ── 4.6 Digital Money & Crypto
with st.expander("📌 4.6 — Digital Money & Cryptocurrencies", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>The Future of Assets</h3>
        <p>This topic explores the shift from physical to digital value. It covers <b>Cryptocurrencies</b> (decentralized assets like Bitcoin) and <b>CBDCs</b> (Central Bank Digital Currencies), which are digital forms of a country's sovereign currency.</p>
        <div class="key-terms">
            <span class="term-pill">Blockchain</span> <span class="term-pill">CBDC</span> <span class="term-pill">Stablecoins</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Digital currencies could significantly reduce cross-border transaction times and costs for multinational treasury operations.</div>
    </div>
    """, unsafe_allow_html=True)

# ─── Interactive: Credit Multiplier Calculator ───────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #e0e7ff; padding-bottom: 8px;">🔢 Interactive: Money Creation Simulator</h2>', unsafe_allow_html=True)
initial_dep = st.number_input("Initial Deposit ($)", value=1000, step=100)
reserve_req = st.slider("Required Reserve Ratio (%)", 1, 50, 10) / 100
total_money = initial_dep * (1 / reserve_req)
st.metric("Total Money Created", f"${total_money:,.2f}")

# ─── Knowledge Check ─────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #e0e7ff; padding-bottom: 8px;">🧠 Module 4 Knowledge Check</h2>', unsafe_allow_html=True)
q1 = st.radio(
    "1. Which type of asset is a digital version of a country's fiat currency issued by the Central Bank?",
    ["Bitcoin", "CBDC", "Stablecoin"],
    index=None, key="m4q1"
)
if q1 == "CBDC":
    st.success("✅ Correct! CBDCs are sovereign digital currencies issued directly by a central bank.")

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1: st.markdown("⬅️ **Previous: Module 3**")
with nav_col2: st.markdown("<div style='text-align:center; color:#888; font-size:0.85rem;'>Module 4 of 8</div>", unsafe_allow_html=True)
with nav_col3: st.markdown("➡️ **Next: Module 5**")