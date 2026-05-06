import streamlit as st
import pandas as pd

# --- STYLING & CUSTOM CSS ---
st.markdown("""
    <style>
    .main-header {
        color: #111827;
        font-size: 32px;
        font-weight: bold;
        border-bottom: 2px solid #111827;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .strategy-card {
        background-color: #F9FAFB;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #111827;
        margin-bottom: 15px;
    }
    .quiz-box {
        background-color: #EFF6FF;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #DBEAFE;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">Module 6: Advanced Strategic Finance</div>', unsafe_allow_html=True)

# --- TABS FOR ORGANIZATION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🤝 M&A Strategy", 
    "⚖️ Governance", 
    "🌐 International", 
    "📝 Quiz", 
    "📋 Summary"
])

# --- TAB 1: MERGERS & ACQUISITIONS (M&A) ---
with tab1:
    st.subheader("Inorganic Growth & Valuation")
    st.write("""
    M&A is a powerful tool for rapid expansion, but most deals fail due to poor integration or overvaluation. 
    The CFO's job is to ensure the math behind the 'Synergy' is real.
    """)
    
    st.markdown("### 💰 M&A Valuation Calculator")
    col1, col2 = st.columns(2)
    
    with col1:
        target_ebitda = st.number_input("Target Company EBITDA ($)", value=1000000, step=100000)
        industry_multiple = st.slider("Industry Multiple (EV/EBITDA)", 1.0, 25.0, 8.0)
        expected_synergies = st.number_input("Annual Synergies (Cost Savings) ($)", value=200000)
    
    with col2:
        enterprise_value = target_ebitda * industry_multiple
        post_synergy_value = (target_ebitda + expected_synergies) * industry_multiple
        value_created = post_synergy_value - enterprise_value
        
        st.metric("Estimated Purchase Price", f"${enterprise_value:,.0f}")
        st.metric("Value with Synergies", f"${post_synergy_value:,.0f}", delta=f"${value_created:,.0f}")
    
    st.info("**Due Diligence Tip:** Always look for 'Off-Balance Sheet' liabilities and culture fit during the investigation phase.")

# --- TAB 2: CORPORATE GOVERNANCE & ESG ---
with tab2:
    st.subheader("Integrity and Stewardship")
    st.write("A CFO is the conscience of the company. Governance ensures transparency and protects minority shareholders.")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown('<div class="strategy-card"><strong>Board Reporting</strong><br>Providing the Audit Committee with accurate, timely, and unbiased financial data.</div>', unsafe_allow_html=True)
    with col_g2:
        st.markdown('<div class="strategy-card"><strong>ESG Integration</strong><br>Measuring and reporting on Environmental, Social, and Governance impacts to attract modern capital.</div>', unsafe_allow_html=True)

    st.write("**Key Frameworks:** Master the COSO Internal Control Framework and the Sarbanes-Oxley (SOX) compliance standards.")

# --- TAB 3: INTERNATIONAL FINANCE ---
with tab3:
    st.subheader("The Global CFO")
    st.write("Managing finances across borders involves complex tax laws, repatriation strategies, and transfer pricing.")
    
    st.markdown("### 🗺️ Strategic Global Concerns")
    concerns = {
        "Topic": ["Transfer Pricing", "Repatriation", "Tax Jurisdictions"],
        "Focus": [
            "Setting prices for transactions between subsidiaries to optimize global tax.",
            "Moving profits from high-growth foreign markets back to the headquarters.",
            "Navigating different corporate tax rates and treaty benefits."
        ]
    }
    st.table(pd.DataFrame(concerns))

# --- TAB 4: QUIZ ---
with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Strategic Leadership Quiz")
    
    m6_q1 = st.radio("1. In M&A, what are 'Synergies'?", 
                  ["The cost of hiring consultants", "The combined value being greater than the sum of parts", "A type of tax penalty"], key="m6_q1")
    
    m6_q2 = st.radio("2. What is the primary goal of Corporate Governance?", 
                  ["To increase marketing spend", "To ensure accountability and transparency", "To hire more employees"], key="m6_q2")
    
    if st.button("Submit Module 6 Quiz", key="m6_quiz_btn"):
        score = 0
        if m6_q1 == "The combined value being greater than the sum of parts": score += 1
        if m6_q2 == "To ensure accountability and transparency": score += 1
        
        st.write(f"Your Score: {score}/2")
        if score == 2: st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: SUMMARY ---
with tab5:
    st.markdown("""
    ### 📌 Module 6 Recap
    *   **M&A:** Valuation is only half the battle; integration and synergies are where value is actually won.
    *   **Governance:** Act as the ultimate guardian of the company’s ethics and reporting standards.
    *   **International:** Think globally about tax and cash movement to avoid double taxation.
    
    **Final CFO Perspective:** You are now at the intersection of Finance and Strategy. Use your technical mastery to drive the company’s vision forward while keeping its foundation rock-solid.
    """)
    
    st.success("🏁 You have completed all 6 Modules of the CFO Excellence Series!")