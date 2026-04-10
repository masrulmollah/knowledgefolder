import streamlit as st

# FIX: Wrapped in try-except for multipage flexibility
try:
    st.set_page_config(page_title="Finance Series · Home", page_icon="⚖️", layout="wide")
except st.errors.StreamlitAPIException:
    pass

# Custom CSS for the Home Page
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.main-hero {
    background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
    border-radius: 20px;
    padding: 60px 40px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.main-hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    margin-bottom: 15px;
}

.main-hero p {
    font-size: 18px;
    color: #cbd5e0;
    max-width: 800px;
    margin: 0 auto;
}

.module-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
}

.module-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 25px;
    transition: transform 0.2s, box-shadow 0.2s;
}

.module-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 20px rgba(0,0,0,0.05);
    border-color: #cbd5e0;
}

.module-number {
    color: #718096;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.module-card h3 {
    font-family: 'Playfair Display', serif;
    color: #1a202c;
    font-size: 20px;
    margin-bottom: 12px;
}

.module-card p {
    color: #4a5568;
    font-size: 14px;
    line-height: 1.6;
}

.footer {
    text-align: center;
    padding: 40px 0;
    color: #a0aec0;
    font-size: 14px;
    border-top: 1px solid #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="main-hero">
    <h1>Corporate Finance Masterclass</h1>
    <p>A comprehensive 12-module journey from the foundations of accounting to the complexities of international risk management and professional ethics.</p>
</div>
""", unsafe_allow_html=True)

# Syllabus Data
modules = [
    ("Foundations of Finance", "Introduction to financial goals, the time value of money (TVM), and the core principles of value creation."),
    ("Financial Statements", "Mastering the Balance Sheet, Income Statement, and Cash Flow Statement alongside ratio analysis."),
    ("Planning & Forecasting", "Building financial models, revenue projections, and performing sensitivity/scenario analysis."),
    ("Capital Budgeting", "Techniques for investment appraisal: NPV, IRR, Payback Period, and Profitability Index."),
    ("Cost of Capital", "Understanding WACC, the Cost of Equity (CAPM), Cost of Debt, and optimal capital structure."),
    ("Working Capital", "Managing short-term assets and liabilities: Inventory, Receivables, Payables, and the Cash Conversion Cycle."),
    ("Corporate Valuation", "Determining business value through DCF analysis and relative valuation multiples (P/E, EV/EBITDA)."),
    ("Financial Markets", "The structure of global equity, debt, and derivative markets and how instruments are traded."),
    ("Risk Management", "Identifying and mitigating Market, Credit, and Operational risks using hedging and VaR metrics."),
    ("Corporate Strategy", "M&A mechanics, dividend policy, share buybacks, and corporate restructuring strategies."),
    ("International Finance", "Managing global treasury functions, foreign exchange (FX) risk, and international capital budgeting."),
    ("Ethics & Standards", "The framework of professional integrity, duty of care, and the ethical standards of the finance industry.")
]

# Display Modules in a responsive grid
cols = st.columns(3)
for i, (title, desc) in enumerate(modules):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="module-card">
            <div class="module-number">Module {i+1}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Progress Insight
st.markdown("---")
st.markdown("### 🗺️ Learning Path Visualization")


st.markdown("""
<div class="insight">
    <p><strong>How to use this series:</strong> This curriculum is designed to be sequential. Each module builds upon the quantitative and theoretical foundations established in the previous sections. We recommend starting with <strong>Foundations</strong> and <strong>Financial Statements</strong> before moving into <strong>Valuation</strong> and <strong>Strategy</strong>.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    © 2026 Finance Knowledge Folder Series • Built with Streamlit • Module 1 - 12
</div>
""", unsafe_allow_html=True)