import streamlit as st

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #f8f9fa;
    color: #1a1a2e;
}

/* Hero Banner - Blue Gradient for Macro */
.hero {
    background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 60%, #3b82f6 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "Σ";
    position: absolute;
    right: 40px;
    top: -10px;
    font-size: 200px;
    color: rgba(255,255,255,0.05);
    font-family: 'Playfair Display', serif;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    color: #ffffff;
    margin: 0 0 8px 0;
}
.hero p {
    color: #bfdbfe;
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
    border-left: 4px solid #1e3a8a;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #1e3a8a;
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
    background: #eff6ff;
    color: #1e3a8a;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid #bfdbfe;
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
.takeaway strong { color: #b8860b; }

/* Section Divider */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: #1a1a2e;
    margin: 32px 0 16px 0;
    padding-bottom: 8px;
    border-bottom: 2px solid #dbeafe;
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
    background: linear-gradient(90deg, #1e3a8a, #3b82f6);
    height: 100%;
    width: 37.5%;
}
.progress-label {
    font-size: 0.78rem;
    color: #6b7280;
    margin-bottom: 6px;
    letter-spacing: 0.5px;
}

/* Sidebar styling */
section[data-testid="stSidebar"] { background-color: #1e3a8a; }
section[data-testid="stSidebar"] * { color: #dbeafe !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📘 Module 3 of 8</div>
    <h1>Macroeconomics</h1>
    <p>Analyze the economy as a whole. Understand national income, inflation mechanics, and the strategic implications of the business cycle.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label">SYLLABUS PROGRESS — MODULE 3 / 8</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📘 Module 3 Topics")
    st.markdown("""
- 3.1 National Income (GDP)
- 3.2 Business Cycles
- 3.3 Inflation
- 3.4 Unemployment
- 3.5 AD-AS Model
- 3.6 Savings & Investment
- 3.7 Multiplier Effect
""")
    st.markdown("---")
    st.markdown("### 📚 All Modules")
    st.markdown("- ✅ Module 1 – Foundations\n- ✅ Module 2 – Microeconomics\n- ✅ **Module 3** – Macroeconomics\n- ⬜ Module 4 – Money & Banking\n- ⬜ Module 5 – Monetary & Fiscal Policy")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📖 Topic Summaries</div>', unsafe_allow_html=True)

# 3.1 National Income
with st.expander("📌 3.1 — National Income: GDP & GNP", expanded=True):
    st.markdown("""
    <div class="topic-card">
        <h3>Measuring Economic Output</h3>
        <p><b>GDP</b> measures the total market value of all final goods and services produced within a country's borders. <b>Real GDP</b> adjusts for price changes, providing a more accurate picture of volume growth.</p>
        <div class="key-terms">
            <span class="term-pill">GDP</span> <span class="term-pill">GNP</span> <span class="term-pill">Real vs Nominal</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Sustained GDP growth indicates an environment of increasing demand, essential for planning factory capacity and volume growth.</div>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"GDP = C + I + G + (X - M)")

# 3.2 Business Cycles
with st.expander("📌 3.2 — Business Cycles", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Expansion and Contraction</h3>
        <p>Economies move through recurring phases: <b>Expansion, Peak, Recession,</b> and <b>Trough</b>. Understanding where an economy sits in this cycle helps in timing major capital expenditures (CAPEX).</p>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> During a recession (contraction), finance priority shifts from aggressive expansion to cash flow preservation and cost efficiency.</div>
    </div>
    """, unsafe_allow_html=True)

# 3.3 Inflation
with st.expander("📌 3.3 — Inflation & Measurement", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>The Cost of Living</h3>
        <p>Inflation is the sustained increase in the general price level. The <b>Consumer Price Index (CPI)</b> tracks the cost of a basket of goods, while the <b>GDP Deflator</b> reflects the prices of all domestic output.</p>
        <div class="key-terms">
            <span class="term-pill">CPI</span> <span class="term-pill">WPI</span> <span class="term-pill">Core Inflation</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> High inflation erodes purchasing power and increases conversion costs. It necessitates frequent price reviews to protect margins.</div>
    </div>
    """, unsafe_allow_html=True)

# 3.4 Unemployment
with st.expander("📌 3.4 — Unemployment Types", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>The Labour Market</h3>
        <p>Unemployment can be <b>Frictional</b> (transitioning), <b>Structural</b> (mismatch of skills), or <b>Cyclical</b> (linked to the business cycle). <b>Full Employment</b> occurs when cyclical unemployment is zero.</p>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> A tight labour market (low unemployment) leads to wage-push inflation, increasing the labor cost component in manufacturing operations.</div>
    </div>
    """, unsafe_allow_html=True)

# 3.5 AD-AS Model
with st.expander("📌 3.5 — Aggregate Demand & Supply", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Macroeconomic Equilibrium</h3>
        <p>The <b>Aggregate Demand (AD)</b> and <b>Aggregate Supply (AS)</b> model determines the economy's price level and total output. Shifts in AD or AS cause changes in growth and inflation rates.</p>
        <div class="key-terms">
            <span class="term-pill">Demand Shock</span> <span class="term-pill">Supply Shock</span> <span class="term-pill">Stagflation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3.6 Savings & Investment
with st.expander("📌 3.6 — Savings and Investment", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Capital Formation</h3>
        <p>In the long run, national savings fund the investments required for economic growth. This relationship is critical for determining the real interest rate in an economy.</p>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Higher national savings rates often translate to a lower cost of borrowing for corporate investments and factory upgrades.</div>
    </div>
    """, unsafe_allow_html=True)

# 3.7 Multiplier Effect
with st.expander("📌 3.7 — The Multiplier Effect", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>Magnifying Economic Activity</h3>
        <p>The <b>Multiplier</b> explains how an initial injection of spending (like government expenditure) leads to a much larger final increase in national income through rounds of respending.</p>
        <div class="key-terms">
            <span class="term-pill">MPC</span> <span class="term-pill">Marginal Propensity to Consume</span> <span class="term-pill">Fiscal Stimulus</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"Multiplier = \frac{1}{1 - MPC}")

# ─── Interactive: GDP Calculator ─────────────────────────────────────────────
st.markdown('<div class="section-title">📊 Interactive: Expenditure GDP Calculator</div>', unsafe_allow_html=True)
st.markdown("Calculate the GDP based on the standard Expenditure Method (all values in billions):")

col_a, col_b = st.columns(2)
with col_a:
    c_val = st.slider("Consumption (C)", 0, 1000, 600)
    i_val = st.slider("Investment (I)", 0, 500, 150)
with col_b:
    g_val = st.slider("Govt Spending (G)", 0, 500, 200)
    nx_val = st.slider("Net Exports (X-M)", -200, 200, -50)

total_gdp = c_val + i_val + g_val + nx_val
st.metric("Total Estimated GDP", f"${total_gdp} Billion")

# ─── Knowledge Check ─────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🧠 Module 3 Knowledge Check</div>', unsafe_allow_html=True)

q1 = st.radio(
    "1. Which phase of the business cycle is characterized by falling Real GDP and rising unemployment?",
    ["Expansion", "Peak", "Recession", "Trough"],
    index=None, key="m3q1"
)
if q1 == "Recession":
    st.success("✅ Correct! A recession is typically defined as two consecutive quarters of negative growth.")
elif q1:
    st.error("❌ That's not right. A recession is the phase where economic activity slows down significantly.")

q2 = st.radio(
    "2. If an economy is facing rising inflation and falling GDP simultaneously, the condition is known as:",
    ["Deflation", "Disinflation", "Stagflation", "Hyperinflation"],
    index=None, key="m3q2"
)
if q2 == "Stagflation":
    st.success("✅ Correct! Stagflation is a challenging mix of 'stagnant' growth and high 'inflation'.")
elif q2:
    st.error("❌ Incorrect. The combination of stagnation and inflation is called Stagflation.")

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1:
    st.markdown("⬅️ **Previous: Module 2**")
with nav_col2:
    st.markdown("<div style='text-align:center; color:#888; font-size:0.85rem;'>Module 3 of 8</div>", unsafe_allow_html=True)
with nav_col3:
    st.markdown("➡️ **Next: Module 4**")