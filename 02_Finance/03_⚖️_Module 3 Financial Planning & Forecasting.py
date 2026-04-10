import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 3 · Financial Planning & Forecasting", page_icon="📅", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=IBM+Plex+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

.hero { background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 50%, #40916c 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '📅'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.15); color: #b7e4c7; font-size: 12px;
    letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px;
    display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Libre Baskerville', serif; color: #fff; font-size: 40px; margin: 0 0 12px 0; }
.hero p { color: #b7e4c7; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }

.concept-card { background: #fff; border: 1px solid #d8f3dc; border-radius: 12px;
    padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #40916c; }
.concept-card h3 { font-family: 'Libre Baskerville', serif; color: #1b4332; font-size: 17px; margin: 0 0 8px; }
.concept-card p { color: #495057; font-size: 14px; line-height: 1.7; margin: 0; }

.formula-box { background: #d8f3dc; border-radius: 8px; padding: 14px 18px;
    font-family: 'Courier New', monospace; font-size: 14px; color: #1b4332; margin: 10px 0; font-weight: 600; }

.insight-box { background: #f0fff4; border-left: 4px solid #38a169;
    border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight-box p { color: #276749; font-size: 14px; margin: 0; line-height: 1.6; }

.section-header { font-family: 'Libre Baskerville', serif; color: #1b4332; font-size: 24px;
    margin: 32px 0 16px; padding-bottom: 8px; border-bottom: 2px solid #d8f3dc; }
.quiz-ok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px;
    padding: 14px; color: #276749; font-weight: 500; margin-top: 8px; }
.quiz-err { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px;
    padding: 14px; color: #9b2c2c; font-weight: 500; margin-top: 8px; }
.progress-bar-outer { background: #d8f3dc; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.progress-bar-inner { background: linear-gradient(90deg,#1b4332,#40916c); border-radius: 10px; height: 6px; width: 25%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-tag">Module 3 of 12</div>
    <h1>Financial Planning & Forecasting</h1>
    <p>Master budgeting, pro-forma statements, break-even analysis, and scenario planning — the tools that translate strategy into numbers.</p>
</div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#52796f;margin-bottom:4px;"><span>Course progress</span><span>Module 3 / 12</span></div>
<div class="progress-bar-outer"><div class="progress-bar-inner"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📖 Core Concepts", "📋 Budgeting Methods", "📉 Break-Even Analysis", "🔮 Scenario Planning", "✅ Quiz"])

with tab1:
    st.markdown('<div class="section-header">Core Concepts in Financial Planning</div>', unsafe_allow_html=True)
    
    concepts = [
        ("Financial Planning", "The process of setting objectives, evaluating available resources, estimating future financial needs, and deciding how to achieve the goals. It spans short-term operational budgets to long-term strategic plans."),
        ("Pro-Forma Financial Statements", "Forward-looking financial statements based on assumptions about future revenues, costs, and capital requirements. Companies prepare pro-forma Income Statements, Balance Sheets, and Cash Flow Statements to plan and attract investors."),
        ("Budgeting", "A budget is a quantitative plan of action for a future period. It coordinates plans of different departments, sets targets, controls performance, and enables variance analysis. Types include operating, capital, and cash budgets."),
        ("Variance Analysis", "Comparing actual results against budgeted figures to understand deviations. Favourable variances (actual better than budget) and adverse variances (actual worse than budget) are investigated for corrective action."),
        ("Rolling Forecasts", "Unlike a static annual budget, a rolling forecast is continuously updated — e.g., always projecting 12 months forward. More responsive to business changes and market dynamics."),
        ("Sensitivity Analysis", "Testing how sensitive the output (e.g., profit, NPV) is to changes in individual input variables. Identifies the most critical drivers of financial performance."),
        ("Scenario Analysis", "Building complete alternative scenarios (Base, Bull, Bear) by changing multiple assumptions simultaneously. More realistic than sensitivity analysis as it captures correlated risks."),
    ]
    
    for title, body in concepts:
        st.markdown(f"""
        <div class="concept-card"><h3>{title}</h3><p>{body}</p></div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-header">Budgeting Methods Compared</div>', unsafe_allow_html=True)
    
    methods = [
        ("Incremental Budgeting", "Start from the prior year's budget and add/subtract a percentage. Simple and fast but perpetuates past inefficiencies. Most common in practice.", "🟡 Common"),
        ("Zero-Based Budgeting (ZBB)", "Every expense must be justified from scratch each year, regardless of past spending. Eliminates waste but is very time-intensive. Used in cost-restructuring exercises.", "🟠 Rigorous"),
        ("Activity-Based Budgeting (ABB)", "Budget is built based on the activities required to achieve output targets. Links costs to specific activities and cost drivers. More accurate than incremental.", "🔵 Advanced"),
        ("Flexible Budgeting", "Budget that adjusts automatically with volume/output changes. Separates fixed and variable costs to produce realistic targets across different activity levels.", "🟢 Adaptive"),
        ("Rolling / Continuous Budgeting", "Always maintains a 12-month forward budget by adding a new period as the most recent one concludes. More responsive to market dynamics.", "🟣 Dynamic"),
        ("Top-Down Budgeting", "Senior management sets overall targets which are cascaded down. Fast alignment but may demotivate operating managers if targets feel imposed.", "⚪ Strategic"),
        ("Bottom-Up Budgeting", "Department managers build their own budgets which are aggregated upward. More ownership at the ground level but can lead to budget padding.", "⚪ Participative"),
    ]
    
    for name, desc, badge in methods:
        st.markdown(f"""
        <div style="background:#fff;border:1px solid #d8f3dc;border-radius:10px;padding:16px 20px;margin-bottom:12px;display:flex;gap:16px;align-items:flex-start;">
            <div style="flex:1;">
                <div style="font-weight:600;color:#1b4332;font-size:15px;margin-bottom:6px;">{name} <span style="font-size:12px;background:#d8f3dc;color:#2d6a4f;border-radius:12px;padding:2px 10px;margin-left:8px;">{badge}</span></div>
                <div style="color:#495057;font-size:14px;line-height:1.6;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="section-header">Break-Even Analysis</div>', unsafe_allow_html=True)
    st.markdown("The break-even point is where **Total Revenue = Total Costs** — no profit, no loss.")
    
    st.markdown("""
    <div class="formula-box">BEP (Units) = Fixed Costs / (Selling Price per Unit − Variable Cost per Unit)</div>
    <div class="formula-box">BEP (Revenue) = Fixed Costs / Contribution Margin Ratio</div>
    <div class="formula-box">Contribution Margin = Selling Price − Variable Cost per Unit</div>
    <div class="formula-box">Margin of Safety = (Actual Sales − BEP Sales) / Actual Sales × 100</div>
    """, unsafe_allow_html=True)
    
    st.markdown("##### 📐 Break-Even Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        fc = st.number_input("Fixed Costs (₹)", value=500000.0, step=10000.0)
    with col2:
        sp = st.number_input("Selling Price per Unit (₹)", value=500.0, step=10.0)
    with col3:
        vc = st.number_input("Variable Cost per Unit (₹)", value=300.0, step=10.0)
    
    actual_sales = st.number_input("Actual / Projected Units Sold", value=3500.0, step=100.0)
    
    if sp > vc:
        cm = sp - vc
        cmr = cm / sp
        bep_units = fc / cm
        bep_rev = fc / cmr
        mos_units = actual_sales - bep_units
        mos_pct = (mos_units / actual_sales * 100) if actual_sales > 0 else 0
        actual_profit = (actual_sales * cm) - fc
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Contribution Margin / Unit", f"₹{cm:,.0f}")
        with col2:
            st.metric("Break-Even (Units)", f"{bep_units:,.0f}")
        with col3:
            st.metric("Break-Even (Revenue)", f"₹{bep_rev:,.0f}")
        with col4:
            st.metric("Margin of Safety", f"{mos_pct:.1f}%")
        
        st.metric("Projected Profit / (Loss)", f"₹{actual_profit:,.0f}", 
                  delta="Profitable ✅" if actual_profit > 0 else "Loss ❌")
        
        # Simple table for BEP visualisation
        unit_range = [int(bep_units * i / 5) for i in range(1, 11)]
        data = []
        for u in unit_range:
            rev = u * sp
            tc = fc + u * vc
            profit = rev - tc
            data.append({"Units": f"{u:,}", "Revenue (₹)": f"₹{rev:,.0f}", "Total Cost (₹)": f"₹{tc:,.0f}", "Profit/(Loss) (₹)": f"₹{profit:,.0f}"})
        st.markdown("##### Revenue vs Cost Table")
        st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
    else:
        st.error("Selling price must be greater than variable cost.")

with tab4:
    st.markdown('<div class="section-header">Scenario & Sensitivity Analysis</div>', unsafe_allow_html=True)
    st.markdown("Build three scenarios (Base, Bull, Bear) for your P&L instantly.")
    
    with st.expander("⚙️ Base Case Assumptions", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            base_rev = st.number_input("Base Revenue (₹ Cr)", value=100.0)
            gm_pct = st.slider("Gross Margin (%)", 10, 80, 40)
            opex_pct = st.slider("Opex as % of Revenue", 5, 50, 20)
        with col2:
            bull_rev_growth = st.slider("Bull Case: Revenue Growth (%)", 5, 100, 30)
            bear_rev_growth = st.slider("Bear Case: Revenue Decline (%)", -50, -1, -20)
            tax = st.slider("Tax Rate (%)", 10, 40, 25)
    
    scenarios = {
        "🐻 Bear Case": base_rev * (1 + bear_rev_growth/100),
        "📊 Base Case": base_rev,
        "🐂 Bull Case": base_rev * (1 + bull_rev_growth/100),
    }
    
    rows = []
    for name, rev in scenarios.items():
        gp = rev * gm_pct / 100
        opex = rev * opex_pct / 100
        ebit = gp - opex
        pbt = ebit * 0.9
        pat = pbt * (1 - tax/100)
        rows.append({
            "Scenario": name,
            "Revenue": f"₹{rev:.1f} Cr",
            "Gross Profit": f"₹{gp:.1f} Cr",
            "EBIT": f"₹{ebit:.1f} Cr",
            "Net Profit": f"₹{pat:.1f} Cr",
            "Net Margin": f"{pat/rev*100:.1f}%",
        })
    
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box"><p><strong>Best Practice:</strong> Always present at least three scenarios to the board. The Bear Case tests financial resilience (can we service debt?), the Base Case drives the operating plan, and the Bull Case informs upside capacity planning. Scenario assumptions should be documented and regularly revisited.</p></div>
    """, unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="section-header">Knowledge Check — Module 3</div>', unsafe_allow_html=True)
    
    questions = [
        {
            "q": "A company has Fixed Costs of ₹10,00,000, Selling Price of ₹200/unit, and Variable Cost of ₹120/unit. What is the break-even point in units?",
            "options": ["5,000 units", "8,333 units", "12,500 units", "6,667 units"],
            "answer": "12,500 units",
            "explanation": "Contribution Margin = ₹200 − ₹120 = ₹80. BEP = ₹10,00,000 / ₹80 = 12,500 units."
        },
        {
            "q": "Which budgeting method requires every expense to be justified from scratch each period?",
            "options": ["Incremental Budgeting", "Flexible Budgeting", "Zero-Based Budgeting", "Rolling Budgeting"],
            "answer": "Zero-Based Budgeting",
            "explanation": "Zero-Based Budgeting (ZBB) starts from a zero base and every cost must be justified anew. It eliminates historical inefficiencies but is time-intensive."
        },
        {
            "q": "Scenario analysis differs from sensitivity analysis because it:",
            "options": [
                "Only changes one variable at a time",
                "Changes multiple correlated variables simultaneously",
                "Only applies to revenue projections",
                "Is used only in capital budgeting"
            ],
            "answer": "Changes multiple correlated variables simultaneously",
            "explanation": "Sensitivity analysis tests one variable at a time (holding others constant). Scenario analysis changes a whole set of related assumptions together, creating coherent alternative futures (e.g., a recession scenario changes revenue, margins, and interest rates together)."
        },
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q3_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                score += 1
                st.markdown(f'<div class="quiz-ok">✅ Correct! {q["explanation"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="quiz-err">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["explanation"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">
    📚 Knowledge Folder · Finance Series · Module 3 of 12 &nbsp;|&nbsp; Next: <strong>Module 4 — Capital Budgeting & Investment Decisions</strong>
</div>
""", unsafe_allow_html=True)