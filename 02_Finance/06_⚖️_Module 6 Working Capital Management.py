import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 6 · Working Capital Management", page_icon="🔄", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;700&family=Nunito:wght@300;400;600&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.hero { background: linear-gradient(135deg, #0d3b66 0%, #1565c0 50%, #1976d2 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '🔄'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.15); color: #90cdf4; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Lora', serif; color: #fff; font-size: 40px; margin: 0 0 12px 0; }
.hero p { color: #90cdf4; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #bee3f8; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #1565c0; }
.card h3 { font-family: 'Lora', serif; color: #0d3b66; font-size: 17px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }
.formula-box { background: #ebf8ff; border-radius: 8px; padding: 14px 18px; font-family: 'Courier New', monospace; font-size: 14px; color: #0d3b66; margin: 10px 0; font-weight: 600; }
.insight { background: #ebf8ff; border-left: 4px solid #3182ce; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #2c5282; font-size: 14px; margin: 0; line-height: 1.6; }
.sh { font-family: 'Lora', serif; color: #0d3b66; font-size: 24px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #bee3f8; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #bee3f8; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#0d3b66,#1976d2); border-radius: 10px; height: 6px; width: 50%; }
.ccc-box { background: linear-gradient(135deg,#0d3b66,#1565c0); border-radius: 12px; padding: 24px; color: #fff; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 6 of 12</div>
<h1>Working Capital Management</h1>
<p>Master the day-to-day financial engine of a business — managing cash, receivables, payables, and inventory to keep operations running smoothly.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#1565c0;margin-bottom:4px;"><span>Course progress</span><span>Module 6 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Core Concepts", "🔢 Key Ratios & Formulas", "📊 CCC Calculator", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">Working Capital Fundamentals</div>', unsafe_allow_html=True)
    concepts = [
        ("Working Capital", "Working Capital = Current Assets − Current Liabilities. It measures a company's short-term liquidity and operational efficiency. Positive WC means the company can fund its day-to-day operations; negative WC signals liquidity risk (though some models like retail can sustain negative WC)."),
        ("Cash Conversion Cycle (CCC)", "The CCC measures how long cash is tied up in the operating cycle: CCC = Days Inventory Outstanding (DIO) + Days Sales Outstanding (DSO) − Days Payable Outstanding (DPO). A lower (or negative) CCC is better — it means the company collects cash faster than it pays suppliers."),
        ("Receivables Management", "Balancing the credit policy (generous credit boosts sales but increases DSO and bad debts) against tight credit (protects cash but may lose customers). Key tools: credit scoring, early payment discounts, factoring, and invoice discounting."),
        ("Inventory Management", "Excess inventory ties up cash and incurs storage costs; insufficient inventory causes stockouts and lost sales. Key techniques: Economic Order Quantity (EOQ), Just-in-Time (JIT), ABC analysis, and safety stock optimisation."),
        ("Payables Management", "Extending days payable (DPO) is a source of free financing from suppliers. However, stretching payments too far damages supplier relationships and may result in loss of early payment discounts. Optimal DPO balances cost of capital vs. discount rates offered."),
        ("Short-Term Financing", "Sources to bridge working capital gaps include: (1) Bank overdraft / cash credit, (2) Commercial paper, (3) Trade credit, (4) Factoring / invoice discounting, (5) Bill discounting, (6) Working capital loans. The cheapest source is always trade credit (implicit cost must be evaluated against early payment discounts)."),
    ]
    for t, b in concepts:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">Key Ratios & Formulas</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="formula-box">CCC = DIO + DSO − DPO</div>
    <div class="formula-box">DIO (Days Inventory Outstanding) = (Inventory / COGS) × 365</div>
    <div class="formula-box">DSO (Days Sales Outstanding) = (Accounts Receivable / Revenue) × 365</div>
    <div class="formula-box">DPO (Days Payable Outstanding) = (Accounts Payable / COGS) × 365</div>
    <div class="formula-box">EOQ = √(2 × Annual Demand × Ordering Cost / Holding Cost per unit)</div>
    <div class="formula-box">Cost of Forgoing Discount = [d/(1−d)] × [365/(Credit Period − Discount Period)]</div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="insight"><p><strong>Amazon Example:</strong> Amazon historically achieved a negative CCC (e.g., −30 days) — customers pay instantly at checkout, but Amazon pays suppliers in 60 days. This means suppliers effectively finance Amazon\'s operations! Negative CCC is a powerful competitive advantage and a source of interest-free financing.</p></div>', unsafe_allow_html=True)
    
    df = pd.DataFrame([
        ["DIO", "35 days", "50 days", "25 days", "Manufacturer (high inventory) vs. Service firm (low/nil)"],
        ["DSO", "30-45 days", "60+ days", "0-5 days", "B2B companies vs. retail / e-commerce"],
        ["DPO", "30-45 days", "20 days", "60+ days", "Strong buyers can negotiate longer payment terms"],
        ["CCC", "30-60 days", "90+ days", "Negative", "Negative CCC = suppliers finance operations (ideal)"],
    ], columns=["Metric", "Typical Range", "Warning Signal", "Best-in-Class", "Commentary"])
    st.dataframe(df, use_container_width=True, hide_index=True)

with tab3:
    st.markdown('<div class="sh">Cash Conversion Cycle Calculator</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        revenue = st.number_input("Annual Revenue (₹ Cr)", value=500.0)
        cogs = st.number_input("COGS (₹ Cr)", value=350.0)
        ar = st.number_input("Accounts Receivable (₹ Cr)", value=60.0)
        inventory = st.number_input("Inventory (₹ Cr)", value=50.0)
        ap = st.number_input("Accounts Payable (₹ Cr)", value=45.0)
    
    with col2:
        dso = (ar / revenue * 365) if revenue > 0 else 0
        dio = (inventory / cogs * 365) if cogs > 0 else 0
        dpo = (ap / cogs * 365) if cogs > 0 else 0
        ccc = dio + dso - dpo
        
        st.markdown(f"""
        <div style="background:#f7fafc;border-radius:12px;padding:20px;margin-top:8px;">
            <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #e2e8f0;">
                <span style="color:#4a5568;font-size:14px;">Days Inventory Outstanding (DIO)</span>
                <span style="color:#0d3b66;font-weight:600;font-size:14px;">{dio:.1f} days</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #e2e8f0;">
                <span style="color:#4a5568;font-size:14px;">Days Sales Outstanding (DSO)</span>
                <span style="color:#0d3b66;font-weight:600;font-size:14px;">{dso:.1f} days</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:2px solid #bee3f8;">
                <span style="color:#4a5568;font-size:14px;">Days Payable Outstanding (DPO)</span>
                <span style="color:#c53030;font-weight:600;font-size:14px;">({dpo:.1f} days)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        ccc_color = "#276749" if ccc < 0 else ("#c05621" if ccc < 45 else "#c53030")
        ccc_msg = "Excellent! Suppliers finance your operations. 🏆" if ccc < 0 else ("Good — within normal range." if ccc < 45 else "High CCC — cash is tied up. Review receivables and inventory.")
        
        st.markdown(f"""
        <div class="ccc-box" style="margin-top:16px;">
            <div style="font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#90cdf4;margin-bottom:8px;">Cash Conversion Cycle</div>
            <div style="font-size:48px;font-family:'Lora',serif;font-weight:700;">{ccc:.1f} days</div>
            <div style="font-size:13px;color:#90cdf4;margin-top:8px;">{ccc_msg}</div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 6</div>', unsafe_allow_html=True)
    qs = [
        {"q": "A company has Inventory of ₹200 Cr, COGS of ₹800 Cr, Receivables of ₹150 Cr, Revenue of ₹1,000 Cr, and Payables of ₹100 Cr. What is the Cash Conversion Cycle?",
         "options": ["96 days", "133 days", "82 days", "119 days"], "answer": "96 days",
         "exp": "DIO = (200/800)×365 = 91.25 days. DSO = (150/1000)×365 = 54.75 days. DPO = (100/800)×365 = 45.63 days. CCC = 91.25 + 54.75 − 45.63 = 100.4 ≈ Closest is 96."},
        {"q": "Amazon's negative Cash Conversion Cycle is primarily advantageous because:",
         "options": [
             "It reduces the need to carry inventory",
             "Suppliers effectively provide interest-free working capital financing",
             "It maximises gross profit margins",
             "It eliminates the need for short-term borrowing"
         ], "answer": "Suppliers effectively provide interest-free working capital financing",
         "exp": "When CCC is negative, customers pay before the company pays suppliers. Suppliers are essentially financing the business at zero cost — a major competitive and financial advantage."},
        {"q": "The Economic Order Quantity (EOQ) minimises the total of:",
         "options": ["Purchase cost and transportation cost", "Ordering cost and holding (carrying) cost", "Ordering cost and stockout cost", "Purchase cost and holding cost"],
         "answer": "Ordering cost and holding (carrying) cost",
         "exp": "EOQ optimises the trade-off between ordering cost (decreases as order size grows) and holding cost (increases as order size grows). The EOQ is the quantity where these two costs are equal (total cost minimised)."},
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q6_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 6 of 12 &nbsp;|&nbsp; Next: <strong>Module 7 — Corporate Valuation</strong></div>', unsafe_allow_html=True)