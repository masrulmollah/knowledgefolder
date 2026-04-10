import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 5 · Cost of Capital & Capital Structure", page_icon="⚖️", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Spectral:wght@400;700&family=Plus+Jakarta+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.hero { background: linear-gradient(135deg, #7b2d00 0%, #c05621 50%, #dd6b20 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '⚖️'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.08; }
.hero-tag { background: rgba(255,255,255,0.15); color: #fbd38d; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Spectral', serif; color: #fff; font-size: 42px; margin: 0 0 12px 0; }
.hero p { color: #feebc8; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #feebc8; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #c05621; }
.card h3 { font-family: 'Spectral', serif; color: #7b2d00; font-size: 19px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }
.formula-box { background: #fffaf0; border: 1px solid #feebc8; border-radius: 8px; padding: 14px 18px; font-family: 'Courier New', monospace; font-size: 14px; color: #7b2d00; margin: 10px 0; font-weight: 600; }
.sh { font-family: 'Spectral', serif; color: #7b2d00; font-size: 24px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #feebc8; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #feebc8; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#7b2d00,#dd6b20); border-radius: 10px; height: 6px; width: 41%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 5 of 12</div>
<h1>Cost of Capital & Capital Structure</h1>
<p>Understand the 'hurdle rate' for investments and the strategic mix of debt and equity that minimises costs while maximising firm value.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#9c4221;margin-bottom:4px;"><span>Course progress</span><span>Module 5 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Core Concepts", "📐 WACC Formula", "📊 WACC Calculator", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">Foundations of Capital Structure</div>', unsafe_allow_html=True)
    concepts = [
        ("Cost of Capital", "The minimum rate of return a company must earn on its investments to satisfy its investors (debt holders and equity holders). It acts as the 'hurdle rate' or discount rate for NPV calculations."),
        ("Cost of Debt (Kd)", "The effective rate a company pays on its borrowed funds. Because interest is tax-deductible, the 'after-tax' cost of debt is used: Kd × (1 - Tax Rate). Debt is generally cheaper than equity because it is lower risk and tax-advantaged."),
        ("Cost of Equity (Ke)", "The return required by shareholders. Unlike debt, there is no contractual payment. It is usually estimated using the Capital Asset Pricing Model (CAPM). Equity is more expensive than debt because shareholders take the most risk."),
        ("CAPM", "Formula: Ke = Rf + β(Rm - Rf). It links the cost of equity to the risk-free rate (Rf), the stock's sensitivity to the market (Beta), and the market risk premium (Rm - Rf)."),
        ("WACC", "The Weighted Average Cost of Capital. It is the average rate of return a company is expected to pay to all its security holders to finance its assets. A firm aims to find the 'Optimal Capital Structure' that minimises WACC."),
        ("Operating vs Financial Leverage", "Operating leverage relates to fixed costs in production. Financial leverage relates to the use of debt in the capital structure. High leverage increases potential returns but also increases the risk of insolvency."),
        ("Modigliani-Miller Theorem", "A theory suggesting that in a perfect market (no taxes, no bankruptcy costs), the value of a firm is independent of its capital structure. In the real world, taxes make debt financing attractive until the risk of 'financial distress' outweighs the tax benefits."),
    ]
    for t, b in concepts:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">The WACC Framework</div>', unsafe_allow_html=True)
    st.markdown("""
    The Weighted Average Cost of Capital (WACC) is calculated by multiplying the cost of each capital component by its proportional weight.
    """)
    st.markdown("""
    <div class="formula-box" style="text-align:center; font-size:18px; padding:25px;">
        WACC = (E/V × Ke) + (D/V × Kd × [1 - T])
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Variables:**")
        st.write("- **E**: Market Value of Equity")
        st.write("- **D**: Market Value of Debt")
        st.write("- **V**: Total Value (E + D)")
    with col2:
        st.markdown("**Rates:**")
        st.write("- **Ke**: Cost of Equity (from CAPM)")
        st.write("- **Kd**: Pre-tax Cost of Debt")
        st.write("- **T**: Marginal Corporate Tax Rate")
    
    st.info("**Note on Weights:** Always use **Market Values** of debt and equity rather than Book Values when calculating WACC, as market values reflect the current cost of raising capital.")

with tab3:
    st.markdown('<div class="sh">Interactive WACC Calculator</div>', unsafe_allow_html=True)
    
    with st.expander("🛠️ Step 1: Calculate Cost of Equity (CAPM)", expanded=True):
        c1, c2, c3 = st.columns(3)
        rf = c1.number_input("Risk-Free Rate (%)", value=7.0, help="Yield on 10-year Govt Bonds")
        beta = c2.number_input("Equity Beta (β)", value=1.1, help="Sensitivity to market movements")
        mrp = c3.number_input("Market Risk Premium (%)", value=6.0, help="Expected market return minus risk-free rate")
        ke = rf + (beta * mrp)
        st.success(f"Estimated Cost of Equity (Ke): **{ke:.2f}%**")

    with st.expander("🛠️ Step 2: Capital Structure & Tax", expanded=True):
        c1, c2, c3 = st.columns(3)
        mkt_cap = c1.number_input("Market Cap (₹ Cr)", value=7000.0)
        total_debt = c2.number_input("Total Debt (₹ Cr)", value=3000.0)
        tax_rate = c3.slider("Tax Rate (%)", 10, 40, 25)
        
        pre_tax_kd = st.number_input("Pre-tax Cost of Debt (%)", value=9.0)
        after_tax_kd = pre_tax_kd * (1 - tax_rate/100)
        
        total_val = mkt_cap + total_debt
        w_equity = mkt_cap / total_val
        w_debt = total_debt / total_val
    
    wacc_final = (w_equity * ke/100) + (w_debt * after_tax_kd/100)
    
    st.markdown("### Final WACC Result")
    col1, col2, col3 = st.columns(3)
    col1.metric("Weight of Equity", f"{w_equity*100:.1f}%")
    col2.metric("After-tax Cost of Debt", f"{after_tax_kd:.2f}%")
    col3.metric("Final WACC", f"{wacc_final*100:.2f}%", delta_color="inverse")

    st.markdown("---")
    st.write("**Summary Table**")
    summary_df = pd.DataFrame({
        "Component": ["Equity", "Debt (After-tax)"],
        "Market Value (₹ Cr)": [mkt_cap, total_debt],
        "Weight (%)": [f"{w_equity*100:.1f}%", f"{w_debt*100:.1f}%"],
        "Cost (%)": [f"{ke:.2f}%", f"{after_tax_kd:.2f}%"]
    })
    st.table(summary_df)

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 5</div>', unsafe_allow_html=True)
    qs = [
        {"q": "Using CAPM, if the Risk-free rate is 5%, Beta is 1.2, and Market Risk Premium is 6%, what is the Cost of Equity?",
         "options": ["11.0%", "12.2%", "7.2%", "13.2%"], "answer": "12.2%",
         "exp": "Ke = Rf + β(MRP) = 5% + 1.2(6%) = 5% + 7.2% = 12.2%."},
        {"q": "A firm has a 10% pre-tax cost of debt and a 30% tax rate. What is the after-tax cost of debt?",
         "options": ["10%", "13%", "7%", "3%"], "answer": "7%",
         "exp": "After-tax Kd = Pre-tax Kd × (1 - T) = 10% × (1 - 0.30) = 7%."},
        {"q": "If a company's stock price increases (Market Cap rises) while debt stays constant, how does this typically affect the WACC calculation?",
         "options": [
             "WACC will decrease",
             "WACC will increase (as equity, which is more expensive, now has a higher weight)",
             "WACC will stay exactly the same",
             "Debt becomes more expensive"
         ], "answer": "WACC will increase (as equity, which is more expensive, now has a higher weight)",
         "exp": "Equity is always more expensive than debt. If the weight of equity in the total value increases, the weighted average cost will be pulled closer to the higher cost of equity, thus increasing WACC."},
        {"q": "Why is after-tax cost of debt typically lower than the cost of equity?",
         "options": [
             "Debt holders take more risk than equity holders",
             "Interest is tax-deductible and debt holders have lower risk (prior claim)",
             "Equity dividends are tax-deductible",
             "Debt has no maturity"
         ], "answer": "Interest is tax-deductible and debt holders have lower risk (prior claim)",
         "exp": "Debt is cheaper because: (1) Creditors have priority over equity holders → lower risk → lower required return; (2) Interest payments reduce taxable income, creating a tax shield (government effectively subsidises debt financing)."}
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q5_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 5 of 12 &nbsp;|&nbsp; Next: <strong>Module 6 — Working Capital Management</strong></div>', unsafe_allow_html=True)