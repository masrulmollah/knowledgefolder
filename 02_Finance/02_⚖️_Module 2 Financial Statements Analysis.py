import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 2 · Financial Statements & Analysis", page_icon="📊", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@400;700&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 32px; position: relative; overflow: hidden;
}
.hero::before { content: '📊'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.12); color: #90cdf4; font-size: 12px;
    letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px;
    display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Fraunces', serif; color: #fff; font-size: 42px; margin: 0 0 12px 0; }
.hero p { color: #a0aec0; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }

.stmt-card { background: #fff; border-radius: 12px; border: 1px solid #e2e8f0;
    padding: 0; overflow: hidden; margin-bottom: 20px; }
.stmt-header { padding: 16px 20px; font-family: 'Fraunces', serif; font-size: 17px;
    color: #fff; font-weight: 700; }
.stmt-body { padding: 16px 20px; }
.stmt-row { display: flex; justify-content: space-between; padding: 7px 0;
    border-bottom: 1px solid #f7fafc; font-size: 14px; }
.stmt-row-total { display: flex; justify-content: space-between; padding: 10px 0;
    font-weight: 600; font-size: 15px; border-top: 2px solid #e2e8f0; margin-top: 4px; }
.stmt-label { color: #4a5568; }
.stmt-value { color: #1a202c; font-family: 'Courier New', monospace; }
.stmt-value-pos { color: #276749; font-family: 'Courier New', monospace; font-weight: 600; }
.stmt-value-neg { color: #c53030; font-family: 'Courier New', monospace; font-weight: 600; }

.ratio-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px;
    padding: 18px; text-align: center; }
.ratio-value { font-family: 'Fraunces', serif; font-size: 32px; color: #0f3460; margin: 6px 0; }
.ratio-name { font-size: 12px; color: #718096; text-transform: uppercase; letter-spacing: 1px; }
.ratio-bench { font-size: 12px; color: #a0aec0; margin-top: 4px; }

.insight-box { background: #ebf8ff; border-left: 4px solid #3182ce;
    border-radius: 0 10px 10px 0; padding: 16px 20px; margin: 12px 0; }
.insight-box p { color: #2c5282; font-size: 14px; margin: 0; line-height: 1.6; }

.section-header { font-family: 'Fraunces', serif; color: #1a202c; font-size: 26px;
    margin: 32px 0 18px 0; padding-bottom: 10px; border-bottom: 2px solid #e2e8f0; }
.quiz-result-correct { background: #f0fff4; border: 1px solid #9ae6b4;
    border-radius: 10px; padding: 14px; color: #276749; font-weight: 500; margin-top:8px; }
.quiz-result-wrong { background: #fff5f5; border: 1px solid #feb2b2;
    border-radius: 10px; padding: 14px; color: #9b2c2c; font-weight: 500; margin-top:8px; }
.progress-bar-outer { background: #e2e8f0; border-radius: 10px; height: 6px; margin: 8px 0 24px; }
.progress-bar-inner { background: linear-gradient(90deg, #0f3460, #e94560);
    border-radius: 10px; height: 6px; width: 16%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-tag">Module 2 of 12</div>
    <h1>Financial Statements & Analysis</h1>
    <p>Learn to read, interpret, and analyse the three core financial statements that tell the story of every business — and the ratios that decode them.</p>
</div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#718096;margin-bottom:4px;"><span>Course progress</span><span>Module 2 / 12</span></div>
<div class="progress-bar-outer"><div class="progress-bar-inner"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 The 3 Statements", "📐 Ratio Analysis", "🔬 DuPont Framework", "📊 Interactive Analysis", "✅ Quiz"])

with tab1:
    st.markdown('<div class="section-header">The Three Financial Statements</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="stmt-card">
            <div class="stmt-header" style="background:#0f3460;">Income Statement</div>
            <div class="stmt-body">
                <div style="font-size:12px;color:#718096;margin-bottom:12px;">Measures PROFITABILITY over a period</div>
                <div class="stmt-row"><span class="stmt-label">Revenue</span><span class="stmt-value">10,000</span></div>
                <div class="stmt-row"><span class="stmt-label">Cost of Goods Sold</span><span class="stmt-value-neg">(6,000)</span></div>
                <div class="stmt-row-total"><span>Gross Profit</span><span class="stmt-value-pos">4,000</span></div>
                <div class="stmt-row"><span class="stmt-label">Operating Expenses</span><span class="stmt-value-neg">(1,500)</span></div>
                <div class="stmt-row-total"><span>EBITDA</span><span class="stmt-value-pos">2,500</span></div>
                <div class="stmt-row"><span class="stmt-label">Depreciation</span><span class="stmt-value-neg">(300)</span></div>
                <div class="stmt-row-total"><span>EBIT</span><span class="stmt-value-pos">2,200</span></div>
                <div class="stmt-row"><span class="stmt-label">Interest Expense</span><span class="stmt-value-neg">(200)</span></div>
                <div class="stmt-row-total"><span>PBT</span><span class="stmt-value-pos">2,000</span></div>
                <div class="stmt-row"><span class="stmt-label">Tax (25%)</span><span class="stmt-value-neg">(500)</span></div>
                <div class="stmt-row-total"><span>Net Profit (PAT)</span><span class="stmt-value-pos">1,500</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stmt-card">
            <div class="stmt-header" style="background:#1a365d;">Balance Sheet</div>
            <div class="stmt-body">
                <div style="font-size:12px;color:#718096;margin-bottom:12px;">Snapshot of FINANCIAL POSITION at a date</div>
                <div style="font-weight:600;color:#2d3748;margin-bottom:6px;font-size:13px;">ASSETS</div>
                <div class="stmt-row"><span class="stmt-label">Cash & Equivalents</span><span class="stmt-value">2,000</span></div>
                <div class="stmt-row"><span class="stmt-label">Accounts Receivable</span><span class="stmt-value">1,500</span></div>
                <div class="stmt-row"><span class="stmt-label">Inventory</span><span class="stmt-value">1,200</span></div>
                <div class="stmt-row"><span class="stmt-label">Fixed Assets (Net)</span><span class="stmt-value">5,300</span></div>
                <div class="stmt-row-total"><span>Total Assets</span><span class="stmt-value-pos">10,000</span></div>
                <div style="font-weight:600;color:#2d3748;margin:10px 0 6px;font-size:13px;">LIABILITIES & EQUITY</div>
                <div class="stmt-row"><span class="stmt-label">Accounts Payable</span><span class="stmt-value">800</span></div>
                <div class="stmt-row"><span class="stmt-label">Long-term Debt</span><span class="stmt-value">3,200</span></div>
                <div class="stmt-row"><span class="stmt-label">Share Capital</span><span class="stmt-value">4,000</span></div>
                <div class="stmt-row"><span class="stmt-label">Retained Earnings</span><span class="stmt-value">2,000</span></div>
                <div class="stmt-row-total"><span>Total L + E</span><span class="stmt-value-pos">10,000</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="stmt-card">
            <div class="stmt-header" style="background:#22543d;">Cash Flow Statement</div>
            <div class="stmt-body">
                <div style="font-size:12px;color:#718096;margin-bottom:12px;">Tracks actual CASH MOVEMENTS in a period</div>
                <div style="font-weight:600;color:#2d3748;margin-bottom:6px;font-size:13px;">Operating Activities</div>
                <div class="stmt-row"><span class="stmt-label">Net Profit</span><span class="stmt-value">1,500</span></div>
                <div class="stmt-row"><span class="stmt-label">Add: Depreciation</span><span class="stmt-value">300</span></div>
                <div class="stmt-row"><span class="stmt-label">Working Capital Changes</span><span class="stmt-value-neg">(200)</span></div>
                <div class="stmt-row-total"><span>CFO</span><span class="stmt-value-pos">1,600</span></div>
                <div style="font-weight:600;color:#2d3748;margin:10px 0 6px;font-size:13px;">Investing Activities</div>
                <div class="stmt-row"><span class="stmt-label">Capex</span><span class="stmt-value-neg">(800)</span></div>
                <div class="stmt-row-total"><span>CFI</span><span class="stmt-value-neg">(800)</span></div>
                <div style="font-weight:600;color:#2d3748;margin:10px 0 6px;font-size:13px;">Financing Activities</div>
                <div class="stmt-row"><span class="stmt-label">Debt Raised</span><span class="stmt-value">400</span></div>
                <div class="stmt-row"><span class="stmt-label">Dividends Paid</span><span class="stmt-value-neg">(300)</span></div>
                <div class="stmt-row-total"><span>CFF</span><span class="stmt-value-pos">100</span></div>
                <div class="stmt-row-total"><span>Net Cash Change</span><span class="stmt-value-pos">900</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box"><p><strong>Golden Rule:</strong> Net Profit ≠ Cash Flow. A profitable company can still run out of cash if working capital is mismanaged. The cash flow statement reconciles accounting profit with actual cash. Always analyse all three statements together.</p></div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-header">Financial Ratio Analysis</div>', unsafe_allow_html=True)
    
    ratio_groups = {
        "💧 Liquidity Ratios": [
            ("Current Ratio", "Current Assets / Current Liabilities", "2:1 (ideal)", "Ability to pay short-term obligations"),
            ("Quick Ratio", "(Current Assets − Inventory) / Current Liabilities", "1:1 (ideal)", "Stricter liquidity test, excludes inventory"),
            ("Cash Ratio", "Cash & Equivalents / Current Liabilities", "> 0.5", "Most conservative liquidity measure"),
        ],
        "📈 Profitability Ratios": [
            ("Gross Profit Margin", "Gross Profit / Revenue × 100", "Industry-specific", "Efficiency of production / COGS management"),
            ("Net Profit Margin", "Net Profit / Revenue × 100", "> 10% (good)", "Overall profitability after all expenses"),
            ("Return on Equity (ROE)", "Net Profit / Shareholders' Equity × 100", "> 15%", "Return generated for shareholders"),
            ("Return on Assets (ROA)", "Net Profit / Total Assets × 100", "> 5%", "Efficiency of asset utilisation"),
            ("Return on Capital Employed (ROCE)", "EBIT / Capital Employed × 100", "> WACC", "Operating return on total capital"),
        ],
        "⚙️ Efficiency Ratios": [
            ("Asset Turnover", "Revenue / Total Assets", "> 1.0", "Sales generated per rupee of assets"),
            ("Inventory Turnover", "COGS / Average Inventory", "Higher = better", "How fast inventory is sold"),
            ("Debtor Days", "Accounts Receivable / Revenue × 365", "< 45 days", "Average collection period"),
            ("Creditor Days", "Accounts Payable / COGS × 365", "30−60 days", "Average payment period to suppliers"),
        ],
        "🏦 Leverage Ratios": [
            ("Debt-to-Equity (D/E)", "Total Debt / Shareholders' Equity", "< 2:1 typically", "Financial leverage of the company"),
            ("Interest Coverage", "EBIT / Interest Expense", "> 3x (safe)", "Ability to service debt interest"),
            ("Debt-to-Assets", "Total Debt / Total Assets", "< 0.5 (conservative)", "Proportion of assets financed by debt"),
        ],
    }
    
    for group, ratios in ratio_groups.items():
        st.markdown(f"#### {group}")
        df = pd.DataFrame(ratios, columns=["Ratio", "Formula", "Benchmark", "Interpretation"])
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("")

with tab3:
    st.markdown('<div class="section-header">DuPont Framework</div>', unsafe_allow_html=True)
    st.markdown("""
    The DuPont analysis **decomposes ROE** into three drivers, revealing exactly *why* ROE is high or low.
    """)
    
    st.markdown("""
    <div style="background:#f7fafc;border-radius:12px;padding:24px;margin:16px 0;text-align:center;">
        <div style="font-size:13px;color:#718096;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;">3-Factor DuPont</div>
        <div style="font-size:22px;color:#0f3460;font-family:'Fraunces',serif;line-height:1.8;">
            ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
        </div>
        <div style="font-size:16px;color:#718096;margin-top:8px;">
            ROE = (Net Profit/Revenue) × (Revenue/Assets) × (Assets/Equity)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("##### Interactive DuPont Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        npm = st.number_input("Net Profit Margin (%)", value=10.0, step=0.5)
    with col2:
        at = st.number_input("Asset Turnover (×)", value=1.2, step=0.1)
    with col3:
        em = st.number_input("Equity Multiplier (×)", value=2.0, step=0.1)
    
    roe = (npm/100) * at * em * 100
    
    col1, col2, col3, col4 = st.columns(4)
    for col, label, val, color in [
        (col1, "Net Profit Margin", f"{npm:.1f}%", "#0f3460"),
        (col2, "Asset Turnover", f"{at:.1f}×", "#2c7a7b"),
        (col3, "Equity Multiplier", f"{em:.1f}×", "#7b341e"),
        (col4, "ROE (Result)", f"{roe:.2f}%", "#276749"),
    ]:
        with col:
            st.markdown(f"""
            <div class="ratio-card">
                <div class="ratio-name">{label}</div>
                <div class="ratio-value" style="color:{color};">{val}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box" style="margin-top:20px;">
    <p><strong>DuPont Insight:</strong> A high ROE can be achieved through (1) high margins (premium brands like Apple), (2) high asset turnover (retailers like Walmart), or (3) high financial leverage (banks). Understanding the source of ROE is critical — leverage-driven ROE carries higher risk.</p>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="section-header">Build Your Own Ratio Dashboard</div>', unsafe_allow_html=True)
    st.markdown("Enter your company's financials and instantly compute all key ratios.")
    
    with st.expander("📝 Enter Financial Data", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Income Statement (₹ Cr)**")
            revenue = st.number_input("Revenue", value=10000.0)
            cogs = st.number_input("Cost of Goods Sold", value=6000.0)
            opex = st.number_input("Operating Expenses", value=1500.0)
            depr = st.number_input("Depreciation", value=300.0)
            interest = st.number_input("Interest Expense", value=200.0)
            tax_rate = st.slider("Tax Rate (%)", 10, 40, 25)
        with c2:
            st.markdown("**Balance Sheet (₹ Cr)**")
            cash = st.number_input("Cash", value=2000.0)
            ar = st.number_input("Accounts Receivable", value=1500.0)
            inventory = st.number_input("Inventory", value=1200.0)
            fixed_assets = st.number_input("Fixed Assets (Net)", value=5300.0)
            ap = st.number_input("Accounts Payable", value=800.0)
            total_debt = st.number_input("Total Debt", value=3200.0)
            equity = st.number_input("Shareholders' Equity", value=6000.0)
        with c3:
            st.markdown("**Computed Values**")
            gross_profit = revenue - cogs
            ebitda = gross_profit - opex
            ebit = ebitda - depr
            pbt = ebit - interest
            net_profit = pbt * (1 - tax_rate/100)
            total_assets = cash + ar + inventory + fixed_assets
            current_assets = cash + ar + inventory
            current_liabilities = ap
            
            st.metric("Gross Profit", f"₹{gross_profit:,.0f}")
            st.metric("EBIT", f"₹{ebit:,.0f}")
            st.metric("Net Profit", f"₹{net_profit:,.0f}")
            st.metric("Total Assets", f"₹{total_assets:,.0f}")
    
    st.markdown("##### 📊 Ratio Results")
    ratios_computed = {
        "Current Ratio": f"{current_assets/current_liabilities:.2f}×" if current_liabilities else "N/A",
        "Gross Profit Margin": f"{gross_profit/revenue*100:.1f}%",
        "Net Profit Margin": f"{net_profit/revenue*100:.1f}%",
        "ROE": f"{net_profit/equity*100:.1f}%" if equity else "N/A",
        "ROA": f"{net_profit/total_assets*100:.1f}%",
        "Asset Turnover": f"{revenue/total_assets:.2f}×",
        "D/E Ratio": f"{total_debt/equity:.2f}×" if equity else "N/A",
        "Interest Coverage": f"{ebit/interest:.1f}×" if interest else "N/A",
        "Debtor Days": f"{ar/revenue*365:.0f} days",
        "Inventory Turnover": f"{cogs/inventory:.1f}×" if inventory else "N/A",
    }
    
    cols = st.columns(5)
    for idx, (k, v) in enumerate(ratios_computed.items()):
        with cols[idx % 5]:
            st.markdown(f"""
            <div class="ratio-card" style="margin-bottom:12px;">
                <div class="ratio-name">{k}</div>
                <div class="ratio-value" style="font-size:22px;">{v}</div>
            </div>
            """, unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="section-header">Knowledge Check — Module 2</div>', unsafe_allow_html=True)
    
    questions = [
        {
            "q": "Which financial statement shows a company's financial position at a specific point in time?",
            "options": ["Income Statement", "Cash Flow Statement", "Balance Sheet", "Statement of Changes in Equity"],
            "answer": "Balance Sheet",
            "explanation": "The Balance Sheet (Statement of Financial Position) is a snapshot as at a specific date. It shows Assets = Liabilities + Equity. The Income Statement and Cash Flow Statement cover a period."
        },
        {
            "q": "A company has Current Assets of ₹800 Cr, Inventory of ₹300 Cr, and Current Liabilities of ₹400 Cr. What is the Quick Ratio?",
            "options": ["2.0", "1.25", "0.75", "1.0"],
            "answer": "1.25",
            "explanation": "Quick Ratio = (Current Assets − Inventory) / Current Liabilities = (800 − 300) / 400 = 500 / 400 = 1.25. This is above 1, indicating the company can meet short-term obligations without selling inventory."
        },
        {
            "q": "In DuPont analysis, which driver would a high-volume, low-margin retailer primarily rely on to generate a high ROE?",
            "options": ["High Net Profit Margin", "High Asset Turnover", "High Equity Multiplier", "High EBITDA"],
            "answer": "High Asset Turnover",
            "explanation": "Retailers like Walmart operate on thin margins but generate high volumes, resulting in a very high Asset Turnover ratio (Revenue / Assets). This is the efficiency driver in DuPont analysis."
        },
        {
            "q": "A company reports a net profit of ₹500 Cr but negative cash flow from operations. This MOST likely indicates:",
            "options": [
                "The company is growing rapidly with high capex",
                "Working capital has increased significantly (e.g. receivables rising)",
                "The company has taken on more debt",
                "The tax rate has increased"
            ],
            "answer": "Working capital has increased significantly (e.g. receivables rising)",
            "explanation": "Profit ≠ Cash. If receivables or inventory rise faster than payables, cash is tied up in working capital. This is a common red flag — companies can be profitable yet cash-poor."
        },
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q2_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                score += 1
                st.markdown(f'<div class="quiz-result-correct">✅ Correct! {q["explanation"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="quiz-result-wrong">❌ Incorrect. Correct answer: <strong>{q["answer"]}</strong><br>{q["explanation"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">
    📚 Knowledge Folder · Finance Series · Module 2 of 12 &nbsp;|&nbsp; Next: <strong>Module 3 — Financial Planning & Forecasting</strong>
</div>
""", unsafe_allow_html=True)