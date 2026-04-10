import streamlit as st

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 1 · Foundations of Finance", page_icon="💡", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.hero {
    background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 32px; position: relative; overflow: hidden;
}
.hero::before {
    content: '💡'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.08;
}
.hero-tag { background: rgba(255,255,255,0.15); color: #a8d8ea; font-size: 12px;
    letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px;
    display: inline-block; margin-bottom: 16px; font-family: 'DM Sans', sans-serif; }
.hero h1 { font-family: 'Playfair Display', serif; color: #ffffff; font-size: 42px;
    margin: 0 0 12px 0; line-height: 1.2; }
.hero p { color: #b0c4d8; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }

.concept-card {
    background: #ffffff; border: 1px solid #e8ecf0; border-radius: 12px;
    padding: 24px; margin-bottom: 16px; border-left: 4px solid #2c5364;
    transition: box-shadow 0.2s;
}
.concept-card:hover { box-shadow: 0 4px 20px rgba(44,83,100,0.12); }
.concept-card h3 { font-family: 'Playfair Display', serif; color: #1a2332; margin: 0 0 10px 0; font-size: 18px; }
.concept-card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }

.formula-box {
    background: #f0f7ff; border: 1px solid #bee3f8; border-radius: 10px;
    padding: 20px 24px; margin: 12px 0; font-family: 'Courier New', monospace;
    font-size: 15px; color: #2a4a6b; font-weight: 500;
}
.formula-label { font-size: 11px; color: #718096; letter-spacing: 2px;
    text-transform: uppercase; font-family: 'DM Sans', sans-serif; margin-bottom: 8px; }

.insight-box {
    background: linear-gradient(135deg, #667eea15, #764ba215);
    border: 1px solid #667eea40; border-radius: 12px; padding: 20px 24px; margin: 20px 0;
}
.insight-box h4 { color: #553c9a; margin: 0 0 8px 0; font-size: 14px;
    letter-spacing: 1px; text-transform: uppercase; }
.insight-box p { color: #4a3f6b; font-size: 14px; margin: 0; line-height: 1.6; }

.section-header {
    font-family: 'Playfair Display', serif; color: #1a2332; font-size: 26px;
    margin: 36px 0 20px 0; padding-bottom: 10px;
    border-bottom: 2px solid #e8ecf0;
}
.pill {
    display: inline-block; background: #edf2f7; color: #4a5568;
    border-radius: 20px; padding: 4px 14px; font-size: 12px;
    margin: 4px; font-weight: 500;
}
.quiz-result-correct { background: #f0fff4; border: 1px solid #9ae6b4;
    border-radius: 10px; padding: 16px; color: #276749; font-weight: 500; }
.quiz-result-wrong { background: #fff5f5; border: 1px solid #feb2b2;
    border-radius: 10px; padding: 16px; color: #9b2c2c; font-weight: 500; }
.progress-bar-outer { background: #e2e8f0; border-radius: 10px; height: 6px; margin-top: 8px; }
.progress-bar-inner { background: linear-gradient(90deg, #2c5364, #0f9b8e);
    border-radius: 10px; height: 6px; width: 8%; }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-tag">Module 1 of 12</div>
    <h1>Foundations of Finance</h1>
    <p>Master the core principles that underpin every financial decision — from the time value of money to the purpose of a firm in the modern economy.</p>
</div>
""", unsafe_allow_html=True)

# Progress Tracker
st.markdown("""
<div style="margin-bottom:28px;">
    <div style="display:flex;justify-content:space-between;font-size:12px;color:#718096;margin-bottom:4px;">
        <span>Course progress</span><span>Module 1 / 12</span>
    </div>
    <div class="progress-bar-outer"><div class="progress-bar-inner"></div></div>
</div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Core Concepts", "🔢 Key Formulas", "📊 Interactive Tools", "💡 Insights", "✅ Quiz"])

with tab1:
    st.markdown('<div class="section-header">Core Concepts</div>', unsafe_allow_html=True)
    
    concepts = [
        ("Time Value of Money (TVM)", "A rupee today is worth more than a rupee tomorrow. Money has the ability to earn interest over time, making present value always greater than the same future amount. This is the single most important concept in all of finance.", ["Present Value", "Future Value", "Discounting", "Compounding"]),
        ("Financial System", "The interconnected network of markets, institutions, instruments, and regulations that facilitate the flow of funds between savers and borrowers. It includes banks, capital markets, insurance companies, and regulatory bodies.", ["Banks", "Capital Markets", "Regulators", "Instruments"]),
        ("Goals of a Firm", "The primary financial goal is to maximise shareholder wealth (maximise stock price), not merely maximise profits. Modern finance also recognises stakeholder value, ESG considerations, and long-term sustainability.", ["Shareholder Wealth", "Stakeholder Theory", "ESG", "Sustainability"]),
        ("Agency Problem", "Conflict of interest between principals (shareholders) and agents (managers). Managers may act in their own self-interest rather than shareholders' interests. Solved through incentive alignment (ESOPs, bonuses) and governance mechanisms.", ["Principal-Agent", "ESOPs", "Governance", "Incentive Alignment"]),
        ("Role of the Finance Function", "Finance provides three core services: (1) Investment decisions — where to allocate capital; (2) Financing decisions — how to raise capital; (3) Dividend decisions — how to return value to shareholders.", ["Capital Allocation", "Fundraising", "Dividend Policy", "CFO Role"]),
    ]
    
    for title, desc, tags in concepts:
        tag_html = "".join(f'<span class="pill">{t}</span>' for t in tags)
        st.markdown(f"""
        <div class="concept-card">
            <h3>{title}</h3>
            <p>{desc}</p>
            <div style="margin-top:12px;">{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-header">Key Formulas</div>', unsafe_allow_html=True)
    
    formulas = [
        ("Future Value (Single Sum)", "FV = PV × (1 + r)ⁿ", "PV = Present Value | r = Interest rate per period | n = Number of periods"),
        ("Present Value (Single Sum)", "PV = FV / (1 + r)ⁿ", "FV = Future Value | r = Discount rate | n = Number of periods"),
        ("Future Value of Annuity", "FVA = PMT × [(1 + r)ⁿ - 1] / r", "PMT = Periodic payment | r = Rate per period | n = Number of payments"),
        ("Present Value of Annuity", "PVA = PMT × [1 - (1 + r)⁻ⁿ] / r", "PMT = Periodic payment | r = Discount rate | n = Number of periods"),
        ("Present Value of Perpetuity", "PV = C / r", "C = Constant annual cash flow | r = Discount rate (required return)"),
        ("Effective Annual Rate", "EAR = (1 + r/m)ᵐ - 1", "r = Nominal annual rate | m = Number of compounding periods per year"),
    ]
    
    for label, formula, note in formulas:
        st.markdown(f"""
        <div style="margin-bottom:20px;">
            <div class="formula-label">{label}</div>
            <div class="formula-box">{formula}</div>
            <div style="font-size:13px;color:#718096;padding:4px 8px;">📝 {note}</div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="section-header">TVM Calculator</div>', unsafe_allow_html=True)
    st.markdown("Use this tool to calculate Future Value or Present Value interactively.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Future Value Calculator")
        pv = st.number_input("Present Value (₹)", min_value=0.0, value=100000.0, step=1000.0, key="pv_fv")
        rate = st.slider("Annual Interest Rate (%)", 1, 25, 8, key="rate_fv")
        years = st.slider("Number of Years", 1, 40, 10, key="yr_fv")
        compound = st.selectbox("Compounding", ["Annually", "Semi-annually", "Quarterly", "Monthly"], key="comp_fv")
        
        m_map = {"Annually": 1, "Semi-annually": 2, "Quarterly": 4, "Monthly": 12}
        m = m_map[compound]
        fv_calc = pv * (1 + (rate/100)/m) ** (m * years)
        gain = fv_calc - pv
        
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#0f2027,#2c5364);border-radius:12px;padding:24px;margin-top:16px;">
            <div style="color:#a8d8ea;font-size:12px;letter-spacing:2px;text-transform:uppercase;">Future Value</div>
            <div style="color:#ffffff;font-size:36px;font-family:'Playfair Display',serif;margin:8px 0;">₹{fv_calc:,.0f}</div>
            <div style="color:#68d391;font-size:14px;">+₹{gain:,.0f} gain ({(gain/pv*100):.1f}% total return)</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("##### Present Value Calculator")
        fv_in = st.number_input("Future Value (₹)", min_value=0.0, value=500000.0, step=1000.0, key="fv_in")
        rate2 = st.slider("Discount Rate (%)", 1, 25, 10, key="rate_pv")
        years2 = st.slider("Number of Years", 1, 40, 10, key="yr_pv")
        
        pv_calc = fv_in / (1 + rate2/100) ** years2
        discount = fv_in - pv_calc
        
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#1a1a2e,#16213e);border-radius:12px;padding:24px;margin-top:16px;">
            <div style="color:#a8d8ea;font-size:12px;letter-spacing:2px;text-transform:uppercase;">Present Value</div>
            <div style="color:#ffffff;font-size:36px;font-family:'Playfair Display',serif;margin:8px 0;">₹{pv_calc:,.0f}</div>
            <div style="color:#fc8181;font-size:14px;">₹{discount:,.0f} discounted away over {years2} years</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("##### Compounding Frequency Comparison")
    base = st.number_input("Principal (₹)", value=100000.0, step=5000.0)
    r_comp = st.slider("Rate (%)", 1, 20, 10, key="r_comp")
    y_comp = st.slider("Years", 1, 30, 10, key="y_comp")
    
    rows = []
    for freq, m_val in [("Annually",1),("Semi-annually",2),("Quarterly",4),("Monthly",12),("Daily",365)]:
        fv_c = base * (1 + (r_comp/100)/m_val)**(m_val*y_comp)
        rows.append({"Compounding": freq, "Future Value (₹)": f"₹{fv_c:,.0f}", "Total Return (%)": f"{(fv_c-base)/base*100:.2f}%"})
    
    import pandas as pd
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

with tab4:
    st.markdown('<div class="section-header">Key Insights & Real-World Applications</div>', unsafe_allow_html=True)
    
    insights = [
        ("Rule of 72", "Divide 72 by the annual interest rate to find how many years it takes to double your money. At 8% per year, money doubles in 72/8 = 9 years. A quick mental math tool used by seasoned finance professionals."),
        ("Inflation Erodes Value", "Real return = Nominal return − Inflation. A 10% return in a 6% inflation environment yields only a 4% real return. Finance always distinguishes between nominal and real rates."),
        ("Sunk Cost Fallacy", "Money already spent is irrelevant to future decisions. Only incremental (marginal) cash flows matter in capital allocation. One of the most common errors in corporate decision-making."),
        ("Opportunity Cost", "The return foregone from the next best alternative. If you invest in Project A, the cost is not just the cash outlay — it also includes whatever Project B would have returned. All financial decisions must account for this."),
        ("Fisher Effect", "Nominal interest rate = Real interest rate + Expected inflation. This links monetary policy, inflation expectations, and the discount rates used in valuation."),
    ]
    
    for title, text in insights:
        st.markdown(f"""
        <div class="insight-box">
            <h4>💡 {title}</h4>
            <p>{text}</p>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="section-header">Quick Knowledge Check</div>', unsafe_allow_html=True)
    st.markdown("Test your understanding of Module 1 fundamentals.")
    
    questions = [
        {
            "q": "Which of the following BEST describes the primary financial goal of a firm?",
            "options": ["Maximise net profit", "Maximise shareholder wealth", "Minimise costs", "Maximise revenue"],
            "answer": "Maximise shareholder wealth",
            "explanation": "The primary financial objective is to maximise shareholder wealth (maximise the stock price / market value of equity). Maximising profit ignores timing, risk, and the time value of money."
        },
        {
            "q": "₹50,000 is invested at 12% per annum compounded quarterly for 3 years. What is the effective annual rate (EAR)?",
            "options": ["12.00%", "12.36%", "12.55%", "13.20%"],
            "answer": "12.55%",
            "explanation": "EAR = (1 + 0.12/4)⁴ − 1 = (1.03)⁴ − 1 = 1.1255 − 1 = 12.55%. Quarterly compounding is more effective than annual compounding at the same nominal rate."
        },
        {
            "q": "The agency problem in finance refers to:",
            "options": [
                "Conflict between equity and debt holders",
                "Conflict between shareholders and managers",
                "Conflict between regulators and firms",
                "Conflict between domestic and foreign investors"
            ],
            "answer": "Conflict between shareholders and managers",
            "explanation": "The agency problem (principal-agent problem) arises because managers (agents) may not always act in the best interests of shareholders (principals). ESOPs and governance mechanisms are used to align interests."
        },
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("Select your answer:", q["options"], key=f"q1_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                score += 1
                st.markdown(f'<div class="quiz-result-correct">✅ Correct! {q["explanation"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="quiz-result-wrong">❌ Incorrect. The correct answer is: <strong>{q["answer"]}</strong><br>{q["explanation"]}</div>', unsafe_allow_html=True)
        st.markdown("---")
    
    answered = sum(1 for i in range(len(questions)) if st.session_state.get(f"q1_{i}"))
    if answered == len(questions):
        pct = score / len(questions) * 100
        color = "#276749" if pct >= 67 else "#c05621"
        st.markdown(f"""
        <div style="background:#f8fafc;border:2px solid {'#9ae6b4' if pct>=67 else '#fbd38d'};border-radius:12px;padding:24px;text-align:center;">
            <div style="font-size:42px;font-family:'Playfair Display',serif;color:{color};">{score}/{len(questions)}</div>
            <div style="color:#718096;margin-top:4px;">{'Great work! Module 1 mastered. 🎉' if pct>=67 else 'Review the concepts above and try again.'}</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">
    📚 Knowledge Folder · Finance Series · Module 1 of 12 &nbsp;|&nbsp; Next: <strong>Module 2 — Financial Statements & Analysis</strong>
</div>
""", unsafe_allow_html=True)