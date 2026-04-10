import streamlit as st
import time

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #f4f7f6;
    color: #1a1a2e;
}

/* Hero Banner - Emerald/Slate Gradient */
.hero {
    background: linear-gradient(135deg, #064e3b 0%, #065f46 60%, #334155 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    border-bottom: 4px solid #10b981;
}
.hero::before {
    content: "⌬";
    position: absolute;
    right: 40px;
    top: -10px;
    font-size: 180px;
    color: rgba(16, 185, 129, 0.08);
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    color: #ecfdf5;
    margin: 0 0 8px 0;
}
.hero p {
    color: #d1fae5;
    font-size: 1.05rem;
    margin: 0;
    font-weight: 300;
}
.hero .badge {
    display: inline-block;
    background: rgba(16, 185, 129, 0.2);
    color: #34d399;
    border: 1px solid rgba(52, 211, 153, 0.4);
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
    border-left: 4px solid #10b981;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #064e3b;
    margin: 0 0 10px 0;
}
.topic-card p {
    font-size: 0.96rem;
    line-height: 1.8;
    color: #334155;
    margin: 0;
}

/* Celebration Card */
.cert-card {
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
    border: 2px solid #10b981;
    border-radius: 15px;
    padding: 40px;
    text-align: center;
    margin-top: 40px;
    box-shadow: 0 10px 25px rgba(16, 185, 129, 0.1);
}
.cert-card h2 {
    font-family: 'Playfair Display', serif;
    color: #064e3b;
    font-size: 2rem;
    margin-bottom: 10px;
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
    background: linear-gradient(90deg, #10b981, #34d399);
    height: 100%;
    width: 100%;
}

/* Sidebar styling */
section[data-testid="stSidebar"] { background-color: #064e3b; }
section[data-testid="stSidebar"] * { color: #d1fae5 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📘 Module 8 of 8</div>
    <h1>Contemporary Issues</h1>
    <p>Analyze the forces shaping the 21st-century economy, from sustainable development and climate change to the AI-driven digital revolution.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label" style="font-size: 0.78rem; color: #6b7280; margin-bottom: 6px;">SYLLABUS PROGRESS — MODULE 8 / 8 (COMPLETE)</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📘 Module 8 Topics")
    st.markdown("""
- 8.1 Sustainable Development
- 8.2 Economics of Climate Change
- 8.3 The Digital Economy & AI
- 8.4 Globalization 4.0
- 8.5 Income Inequality
""")
    st.markdown("---")
    st.success("🎉 Final Module Reached!")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px;">📖 Topic Summaries</h2>', unsafe_allow_html=True)

# ── 8.1 Sustainable Development
with st.expander("📌 8.1 — Sustainable Development Goals (SDGs)", expanded=True):
    st.markdown("""
    <div class="topic-card">
        <h3>ESG & The Future</h3>
        <p>Sustainable development balances economic growth with social inclusion and environmental protection. It is often guided by the UN's 17 SDGs and corporate ESG frameworks.</p>
    </div>
    """, unsafe_allow_html=True)

# ── 8.2 Economics of Climate Change
with st.expander("📌 8.2 — Economics of Climate Change", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Correcting Market Failure</h3>
        <p>Climate change is the ultimate global externality. Economics focuses on carbon pricing and incentivizing green energy transitions to internalize these environmental costs.</p>
    </div>
    """, unsafe_allow_html=True)

# ── 8.3 Digital Economy & AI
with st.expander("📌 8.3 — The Digital Economy & AI", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Production in the Age of Data</h3>
        <p>AI and big data are redefining productivity. This topic analyzes "Platform Economics," network effects, and how automation shifts the production possibility frontier.</p>
    </div>
    """, unsafe_allow_html=True)

# ── 8.4 Globalization 4.0
with st.expander("📌 8.4 — Globalization 4.0 & Supply Chains", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Supply Chain Resilience</h3>
        <p>Modern trade is shifting toward digital services and resilient, regionalized supply chains. The strategy is moving from "Just-in-Time" to "Just-in-Case" logistics.</p>
    </div>
    """, unsafe_allow_html=True)

# ── 8.5 Income Inequality
with st.expander("📌 8.5 — Income & Wealth Inequality", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>The Gini Coefficient</h3>
        <p>Measuring wealth distribution using the Lorenz Curve and Gini Coefficient helps policy makers address economic mobility and social stability.</p>
    </div>
    """, unsafe_allow_html=True)

# ─── Completion Celebration ──────────────────────────────────────────────────
st.markdown("---")
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; text-align: center;">🎓 Course Graduation</h2>', unsafe_allow_html=True)

if st.button("CLICK HERE TO CELEBRATE COMPLETION"):
    st.balloons()
    st.snow()
    time.sleep(1)
    st.markdown("""
    <div class="cert-card">
        <p style="text-transform: uppercase; letter-spacing: 2px; color: #10b981; font-weight: 600; margin-bottom: 0;">Congratulations</p>
        <h2>Course Completed!</h2>
        <p style="color: #475569; font-size: 1.1rem;">You have successfully navigated through all 8 modules of <b>Economics for Professionals</b>. You have mastered the foundational and contemporary tools of economic analysis.</p>
        <div style="margin-top: 20px; font-style: italic; color: #94a3b8;">"The engine of the economy is human ingenuity."</div>
    </div>
    """, unsafe_allow_html=True)

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1:
    st.markdown("⬅️ **Previous: Module 7**")
with nav_col2:
    st.markdown("<div style='text-align:center; color:#10b981; font-weight:600;'>Course Completed 🎓</div>", unsafe_allow_html=True)
with nav_col3:
    st.markdown("🏠 **Home: Module 1**")