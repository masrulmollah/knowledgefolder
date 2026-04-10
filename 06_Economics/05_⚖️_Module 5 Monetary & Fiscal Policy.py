import streamlit as st

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #fdfafb;
    color: #1a1a2e;
}

/* Hero Banner - Purple/Crimson Gradient for Policy */
.hero {
    background: linear-gradient(135deg, #4c1d95 0%, #831843 60%, #9f1239 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "⚖️";
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
    color: #fce7f3;
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
    border-left: 4px solid #831843;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #4c1d95;
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
    background: #fdf2f8;
    color: #9f1239;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid #fce7f3;
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
    background: linear-gradient(90deg, #831843, #db2777);
    height: 100%;
    width: 62.5%;
}

/* Sidebar styling */
section[data-testid="stSidebar"] { background-color: #4c1d95; }
section[data-testid="stSidebar"] * { color: #fce7f3 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📘 Module 5 of 8</div>
    <h1>Monetary & Fiscal Policy</h1>
    <p>Master the levers of economic control. Understand how governments and central banks manage growth, inflation, and public debt through strategic policy interventions.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label" style="font-size: 0.78rem; color: #6b7280; margin-bottom: 6px;">SYLLABUS PROGRESS — MODULE 5 / 8</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📘 Module 5 Topics")
    st.markdown("""
- 5.1 Monetary Policy Tools
- 5.2 Interest Rates & Inflation
- 5.3 Fiscal Policy (Expansionary/Contractionary)
- 5.4 Taxation & Public Spending
- 5.5 Debt & Deficits
""")
    st.markdown("---")
    st.markdown("### 📚 All Modules")
    st.markdown("- ✅ Module 1 – Foundations\n- ✅ Module 2 – Micro\n- ✅ Module 3 – Macro\n- ✅ Module 4 – Money & Banking\n- ✅ **Module 5** – Policy\n- ⬜ Module 6 – International")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #fce7f3; padding-bottom: 8px;">📖 Topic Summaries</h2>', unsafe_allow_html=True)

# ── 5.1 & 5.2 Monetary Policy
with st.expander("📌 5.1 & 5.2 — Monetary Policy & Interest Rates", expanded=True):
    st.markdown("""
    <div class="topic-card">
        <h3>Central Bank Interventions</h3>
        <p>Monetary policy involves managing the money supply and interest rates. Central banks use <b>Repo Rates</b> and <b>Open Market Operations (OMO)</b> to control inflation and encourage or cool economic growth.</p>
        <div class="key-terms">
            <span class="term-pill">Repo Rate</span> <span class="term-pill">CRR / SLR</span> <span class="term-pill">Quantitative Easing</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── 5.3 Fiscal Policy
with st.expander("📌 5.3 — Fiscal Policy Framework", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Government Spending & Revenue</h3>
        <p>Fiscal policy is the use of government spending and tax policy to influence economic conditions. 
        It is typically divided into two types:</p>
        <ul>
            <li><b>Expansionary:</b> Increasing spending or cutting taxes to fight unemployment and recession.</li>
            <li><b>Contractionary:</b> Decreasing spending or raising taxes to combat inflation and reduce debt.</li>
        </ul>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Large government infrastructure projects (Expansionary Fiscal Policy) directly increase the demand for industrial products and manufacturing services.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 5.4 Taxation & Public Spending
with st.expander("📌 5.4 — Taxation & Public Expenditure", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Funding the State</h3>
        <p>Governments collect revenue through <b>Direct Taxes</b> (Income/Corporate tax) and <b>Indirect Taxes</b> (VAT/GST/Customs). Spending is directed toward public goods, social security, and development.</p>
        <div class="key-terms">
            <span class="term-pill">Progressive Tax</span> <span class="term-pill">Regressive Tax</span> <span class="term-pill">VAT</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Changes in Corporate Tax rates or VAT regulations directly impact the bottom-line profitability and cash flow forecasting of manufacturing plants.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 5.5 Debt & Deficits
with st.expander("📌 5.5 — Public Debt & Deficits", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>The National Balance Sheet</h3>
        <p>When spending exceeds revenue, a <b>Budget Deficit</b> occurs, which is financed through borrowing, leading to <b>Public Debt</b>. Managing the debt-to-GDP ratio is critical for long-term fiscal sustainability.</p>
    </div>
    """, unsafe_allow_html=True)

# ─── Interactive: Policy Impact Simulator ────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #fce7f3; padding-bottom: 8px;">🎮 Interactive: Policy Lever Simulator</h2>', unsafe_allow_html=True)
st.markdown("Choose a policy action to see its typical effect on the economy:")

policy_action = st.selectbox(
    "Select a Government/Central Bank Action:",
    ["Increase Interest Rates", "Decrease Interest Rates", "Increase Infrastructure Spending", "Increase Corporate Tax"],
    index=None
)

if policy_action == "Increase Interest Rates":
    st.info("📉 **Likely Outcome:** Borrowing becomes expensive. Inflation usually drops, but economic growth and investment may slow down.")
elif policy_action == "Decrease Interest Rates":
    st.success("📈 **Likely Outcome:** Cheaper credit encourages expansion and spending. GDP growth likely increases, but inflation risk rises.")
elif policy_action == "Increase Infrastructure Spending":
    st.success("🏗️ **Likely Outcome:** Direct boost to Aggregate Demand and job creation. Increases long-term productivity but expands the budget deficit.")
elif policy_action == "Increase Corporate Tax":
    st.error("💰 **Likely Outcome:** Government revenue increases, but corporate retained earnings for reinvestment decrease, potentially slowing CAPEX.")

# ─── Knowledge Check ─────────────────────────────────────────────────────────
st.markdown('<h2 style="font-family: \'Playfair Display\', serif; font-size: 1.5rem; border-bottom: 2px solid #fce7f3; padding-bottom: 8px;">🧠 Module 5 Knowledge Check</h2>', unsafe_allow_html=True)

q1 = st.radio(
    "1. Which policy is primarily managed by the Central Bank to control the money supply?",
    ["Fiscal Policy", "Monetary Policy", "Industrial Policy"],
    index=None, key="m5q1"
)
if q1 == "Monetary Policy":
    st.success("✅ Correct! Central banks use Monetary Policy tools to manage liquidity and interest rates.")

q2 = st.radio(
    "2. If a government reduces taxes and increases spending during a recession, it is practicing:",
    ["Contractionary Fiscal Policy", "Expansionary Fiscal Policy", "Supply-side Policy"],
    index=None, key="m5q2"
)
if q2 == "Expansionary Fiscal Policy":
    st.success("✅ Correct! Expansionary policy 'expands' the economy by putting more money in the hands of consumers and firms.")

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1:
    st.markdown("⬅️ **Previous: Module 4**")
with nav_col2:
    st.markdown("<div style='text-align:center; color:#888; font-size:0.85rem;'>Module 5 of 8</div>", unsafe_allow_html=True)
with nav_col3:
    st.markdown("➡️ **Next: Module 6**")