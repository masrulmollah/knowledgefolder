import streamlit as st

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #fdfdfd;
    color: #1a1a2e;
}

/* Hero Banner - Charcoal/Gold Gradient for Financial Economics */
.hero {
    background: linear-gradient(135deg, #1a1a1a 0%, #262626 60%, #404040 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    border-bottom: 4px solid #d4af37;
}
.hero::before {
    content: "$";
    position: absolute;
    right: 40px;
    top: -10px;
    font-size: 180px;
    color: rgba(212, 175, 55, 0.1);
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    color: #d4af37;
    margin: 0 0 8px 0;
}
.hero p {
    color: #e5e5e5;
    font-size: 1.05rem;
    margin: 0;
    font-weight: 300;
}
.hero .badge {
    display: inline-block;
    background: rgba(212, 175, 55, 0.2);
    color: #d4af37;
    border: 1px solid rgba(212, 175, 55, 0.4);
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
    border-left: 4px solid #d4af37;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #1a1a1a;
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
    background: #fffcf0;
    color: #b8860b;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid #f5d78e;
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
    background: linear-gradient(90deg, #d4af37, #f1c40f);
    height: 100%;
    width: 87.5%;
}

/* Sidebar styling */
section[data-testid="stSidebar"] { background-color: #1a1a1a; }
section[data-testid="stSidebar"] * { color: #d4af37 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📘 Module 7 of 8</div>
    <h1>Financial Economics</h1>
    <p>Understand the intersection of economic theory and financial markets. Analyze how assets are priced, how capital is raised, and how risk is managed globally.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label" style="font-size: 0.78rem; color: #6b7280; margin-bottom: 6px;">SYLLABUS PROGRESS — MODULE 7 / 8</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📘 Module 7 Topics")
    st.markdown("""
- 7.1 Time Value of Money
- 7.2 Bonds & Fixed Income
- 7.3 Equity & Capital Markets
- 7.4 Derivatives & Hedging
- 7.5 Risk & Portfolio Management
""")
    st.markdown("---")
    st.markdown("### 📚 All Modules")
    st.markdown("- ✅ Module 1-6 Complete\n- ✅ **Module 7** – Financial\n- ⬜ Module 8 – Contemporary")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #f5d78e; padding-bottom: 8px;">📖 Topic Summaries</h2>', unsafe_allow_html=True)

# ── 7.1 Time Value of Money (TVM)
with st.expander("📌 7.1 — Time Value of Money", expanded=True):
    st.markdown("""
    <div class="topic-card">
        <h3>The Core of Finance</h3>
        <p>A dollar today is worth more than a dollar tomorrow due to its potential earning capacity. TVM is the foundation for NPV, IRR, and all corporate investment appraisals.</p>
        <div class="key-terms">
            <span class="term-pill">Discounting</span> <span class="term-pill">Compounding</span> <span class="term-pill">Annuity</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 7.2 Bonds & Fixed Income
with st.expander("📌 7.2 — Bond Markets", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Debt Financing</h3>
        <p>Bonds are debt instruments used by governments and corporations to raise capital. Prices move inversely to interest rates—a critical concept for managing corporate treasury.</p>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Rising interest rates increase the yield required by investors, making new corporate debt issuances more expensive.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 7.3 Equity & Capital Markets
with st.expander("📌 7.3 — Equity & Capital Markets", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Ownership & Valuation</h3>
        <p>Equity represents ownership in a corporation. This topic explores <b>IPOs</b>, secondary market trading, and the valuation of firms using multiples (P/E) or DCF models.</p>
        <div class="key-terms">
            <span class="term-pill">IPO</span> <span class="term-pill">Market Cap</span> <span class="term-pill">Dividends</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Understanding market valuation multiples helps finance leaders communicate company performance to shareholders and investors.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 7.4 Derivatives & Hedging
with st.expander("📌 7.4 — Derivatives", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Managing Volatility</h3>
        <p>Derivatives (Forwards, Futures, Options) are contracts that derive value from an underlying asset. They are essential for <b>Hedging</b> against commodity price or FX fluctuations.</p>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Factories use derivatives to lock in prices for raw materials (like fuel or chemicals), protecting conversion costs from market volatility.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 7.5 Risk & Portfolio Management
with st.expander("📌 7.5 — Risk & Portfolio Management", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Diversification</h3>
        <p>Risk is measured through variance and standard deviation. Portfolio management focuses on <b>Diversification</b> to eliminate unsystematic risk and maximize returns for a given level of risk.</p>
        <div class="key-terms">
            <span class="term-pill">Beta</span> <span class="term-pill">CAPM</span> <span class="term-pill">Sharpe Ratio</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── Interactive: NPV Calculator ─────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #f5d78e; padding-bottom: 8px;">📊 Interactive: Project Appraisal (NPV)</h2>', unsafe_allow_html=True)

initial_inv = st.number_input("Initial Investment ($)", value=10000, step=1000)
cash_flow = st.number_input("Expected Annual Cash Flow ($)", value=3000, step=500)
rate = st.slider("Discount Rate (%)", 1, 20, 10) / 100
years = st.slider("Project Life (Years)", 1, 10, 5)

npv = sum([cash_flow / (1 + rate)**t for t in range(1, years + 1)]) - initial_inv
st.metric("Project Net Present Value (NPV)", f"${npv:,.2f}")
if npv > 0: st.success("✅ Positive NPV: This project adds value!")
else: st.error("❌ Negative NPV: This project may destroy value.")

# ─── Knowledge Check ─────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #f5d78e; padding-bottom: 8px;">🧠 Module 7 Knowledge Check</h2>', unsafe_allow_html=True)

q1 = st.radio(
    "1. Which financial instrument is specifically designed to hedge against future price changes of a commodity?",
    ["Common Stock", "Government Bond", "Futures Contract"],
    index=None, key="m7q1"
)
if q1 == "Futures Contract":
    st.success("✅ Correct! Futures allow you to lock in a price today for a transaction in the future.")

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1:
    st.markdown("⬅️ **Previous: Module 6**")
with nav_col2:
    st.markdown("<div style='text-align:center; color:#888; font-size:0.85rem;'>Module 7 of 8</div>", unsafe_allow_html=True)
with nav_col3:
    st.markdown("➡️ **Next: Module 8**")