import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 7 · Corporate Valuation", page_icon="🏢", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+3:wght@300;400;600&display=swap');
html, body, [class*="css"] { font-family: 'Source Sans 3', sans-serif; }
.hero { background: linear-gradient(135deg, #1a202c 0%, #2d3748 50%, #4a5568 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '🏢'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.15); color: #e2e8f0; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Playfair Display', serif; color: #fff; font-size: 42px; margin: 0 0 12px 0; }
.hero p { color: #e2e8f0; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #2d3748; }
.card h3 { font-family: 'Playfair Display', serif; color: #1a202c; font-size: 18px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }
.formula-box { background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; font-family: 'Courier New', monospace; font-size: 14px; color: #2d3748; margin: 10px 0; font-weight: 600; }
.insight { background: #edf2f7; border-left: 4px solid #4a5568; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #2d3748; font-size: 14px; margin: 0; line-height: 1.6; }
.sh { font-family: 'Playfair Display', serif; color: #1a202c; font-size: 24px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #e2e8f0; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#1a202c,#4a5568); border-radius: 10px; height: 6px; width: 58.3%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 7 of 12</div>
<h1>Corporate Valuation</h1>
<p>Master the art and science of determining what a business is worth using DCF analysis, relative valuation, and transaction multiples.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#4a5568;margin-bottom:4px;"><span>Course progress</span><span>Module 7 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Core Concepts", "📉 DCF Framework", "📊 Relative Valuation", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">Valuation Foundations</div>', unsafe_allow_html=True)
    concepts = [
        ("Enterprise Value (EV)", "The total value of a business, regardless of its capital structure. EV = Market Cap + Total Debt + Minority Interest + Preferred Stock − Cash & Equivalents. It represents the 'takeover price' of the whole entity."),
        ("Equity Value", "The value of the business available only to shareholders. Equity Value = Enterprise Value − Debt + Cash. In public markets, this is equivalent to Market Capitalisation."),
        ("Intrinsic Valuation (DCF)", "Valuing a company based on the present value of its future free cash flows. It is considered the most theoretically sound method but is highly sensitive to assumptions about growth and discount rates."),
        ("Relative Valuation", "Valuing a company by comparing it to similar businesses ('Comps') using multiples like P/E, EV/EBITDA, or EV/Sales. It reflects current market sentiment but may be misleading if the whole sector is over/undervalued."),
        ("Free Cash Flow to Firm (FCFF)", "The cash available to all capital providers (debt and equity) after taxes and reinvestment needs. FCFF = EBIT × (1 − Tax) + D&A − Capex − ΔWorking Capital."),
        ("Terminal Value", "The value of a business beyond the explicit forecast period (usually 5-10 years). It often accounts for 60-80% of total DCF value. Calculated using the Perpetuity Growth Method or Exit Multiple Method."),
        ("Weighted Average Cost of Capital (WACC)", "The discount rate used in DCF to convert future FCFF into present value. It reflects the risk and required return of the firm's capital components."),
    ]
    for t, b in concepts:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">The DCF Workflow</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="formula-box">Value = Σ [FCFFₜ / (1 + WACC)ᵗ] + [Terminal Value / (1 + WACC)ⁿ]</div>
    <div class="formula-box">Terminal Value = FCFFₙ₊₁ / (WACC − g)</div>
    """, unsafe_allow_html=True)
    
    st.markdown("##### 🧪 DCF Sensitivity Simulator")
    col1, col2, col3 = st.columns(3)
    with col1:
        base_fcf = st.number_input("Year 1 Free Cash Flow (₹ Cr)", value=100.0)
        growth = st.slider("Growth Rate for 5 yrs (%)", 2, 30, 10)
    with col2:
        wacc = st.slider("Discount Rate (WACC) (%)", 6, 20, 10)
        t_growth = st.slider("Terminal Growth Rate (%)", 1, 5, 3)
    with col3:
        net_debt = st.number_input("Net Debt (Debt - Cash) (₹ Cr)", value=200.0)
        shares = st.number_input("Shares Outstanding (Cr)", value=10.0)
    
    # Simple 5-year DCF calculation
    fcf_list = []
    pv_list = []
    for i in range(1, 6):
        fcf = base_fcf * (1 + growth/100)**(i-1)
        pv = fcf / (1 + wacc/100)**i
        fcf_list.append(fcf)
        pv_list.append(pv)
    
    terminal_fcf = fcf_list[-1] * (1 + t_growth/100)
    terminal_val = terminal_fcf / (wacc/100 - t_growth/100)
    pv_terminal = terminal_val / (1 + wacc/100)**5
    
    ev = sum(pv_list) + pv_terminal
    equity_val = ev - net_debt
    per_share = equity_val / shares
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Enterprise Value", f"₹{ev:,.1f} Cr")
    c2.metric("Equity Value", f"₹{equity_val:,.1f} Cr")
    c3.metric("Intrinsic Price / Share", f"₹{per_share:,.2f}")
    
    st.markdown(f'<div class="insight"><p><strong>Warning:</strong> Terminal Value represents <strong>{pv_terminal/ev*100:.1f}%</strong> of your total valuation. High terminal value concentration indicates that the valuation is heavily dependent on long-term stability assumptions.</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="sh">Relative Valuation (Multiples)</div>', unsafe_allow_html=True)
    st.write("Compare the target company against peer averages.")
    
    peer_data = pd.DataFrame({
        "Peer Company": ["Peer A", "Peer B", "Peer C", "Peer D"],
        "EV/EBITDA": [12.5, 14.2, 11.8, 13.5],
        "P/E Ratio": [22.0, 25.4, 20.1, 23.5],
        "Revenue Growth": ["12%", "15%", "8%", "11%"]
    })
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("**Target Financials**")
        target_ebitda = st.number_input("Target EBITDA (₹ Cr)", value=150.0)
        target_pat = st.number_input("Target Net Profit (₹ Cr)", value=80.0)
    with col2:
        st.write("**Peer Comparison Table**")
        st.dataframe(peer_data, use_container_width=True, hide_index=True)
        avg_ebitda_mult = peer_data["EV/EBITDA"].mean()
        avg_pe_mult = peer_data["P/E Ratio"].mean()
    
    val_ebitda = target_ebitda * avg_ebitda_mult
    val_pe = target_pat * avg_pe_mult
    
    st.info(f"Valuation based on Peer Avg EV/EBITDA ({avg_ebitda_mult:.1f}x): **₹{val_ebitda:,.1f} Cr (Enterprise Value)**")
    st.info(f"Valuation based on Peer Avg P/E ({avg_pe_mult:.1f}x): **₹{val_pe:,.1f} Cr (Equity Value)**")

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 7</div>', unsafe_allow_html=True)
    qs = [
        {"q": "Which valuation method is considered 'intrinsic' because it relies on the company's specific cash flow generation rather than market sentiment?",
         "options": ["Comparable Company Analysis", "Precedent Transactions", "Discounted Cash Flow (DCF)", "Liquidation Valuation"],
         "answer": "Discounted Cash Flow (DCF)",
         "exp": "DCF is an intrinsic method as it values the business based on the present value of its future cash flows. The other two are 'relative' methods based on market pricing of other companies."},
        {"q": "What is the difference between Enterprise Value (EV) and Equity Value?",
         "options": ["EV includes debt and minority interest; Equity Value is just the value to shareholders", "Equity Value is always higher than EV", "EV is only for private companies", "There is no difference"],
         "answer": "EV includes debt and minority interest; Equity Value is just the value to shareholders",
         "exp": "EV represents the total value of the business (to all capital providers). Equity Value = EV − Net Debt (Value available only to shareholders)."},
        {"q": "Transaction multiples (from M&A deals) are typically HIGHER than comparable company trading multiples because:",
         "options": [
             "They use trailing earnings instead of forward estimates",
             "Acquirers pay a control premium over the public market price",
             "Private companies are more efficient than public ones",
             "Transaction multiples ignore EBITDA adjustments"
         ], "answer": "Acquirers pay a control premium over the public market price",
         "exp": "Acquirers pay a premium (typically 15-30%) over the standalone public market price to gain control of the company, synergies, and strategic benefits. This control premium is the key reason deal multiples exceed trading multiples."}
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q7_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 7 of 12 &nbsp;|&nbsp; Next: <strong>Module 8 — Financial Markets & Instruments</strong></div>', unsafe_allow_html=True)