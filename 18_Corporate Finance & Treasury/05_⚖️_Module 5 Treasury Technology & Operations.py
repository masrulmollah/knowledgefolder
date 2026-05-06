import streamlit as st
import pandas as pd

# --- STYLING & CUSTOM CSS ---
st.markdown("""
    <style>
    .main-header {
        color: #0F172A;
        font-size: 32px;
        font-weight: bold;
        border-bottom: 2px solid #0F172A;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .tech-card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #334155;
        margin-bottom: 15px;
    }
    .quiz-box {
        background-color: #ECFDF5;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #D1FAE5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">Module 5: Treasury Technology & Operations</div>', unsafe_allow_html=True)

# --- TABS FOR ORGANIZATION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💻 TMS & Systems", 
    "🏦 Banking Ops", 
    "🛡️ Fraud & Security", 
    "📝 Quiz", 
    "📋 Summary"
])

# --- TAB 1: TREASURY MANAGEMENT SYSTEMS (TMS) ---
with tab1:
    st.subheader("The Digital Ecosystem")
    st.write("""
    A TMS is the central nervous system for a modern treasury department. It automates bank statement processing, 
    debt management, and hedge accounting.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Core Capabilities of a TMS:**")
        st.markdown("- **Bank Connectivity:** Real-time visibility of global balances via SWIFT or API.")
        st.markdown("- **Automated Reconciliation:** Matching bank transactions to ERP records automatically.")
        st.markdown("- **Compliance:** Automated reporting for IFRS 9 / ASC 815 (Hedge Accounting).")
    
    with col2:
        st.info("**Key Players:** Systems like Kyriba, Reval, ION Treasury, or SAP Treasury module are industry standards.")
        st.write("Does your organization still use Excel for cash positioning? If so, you are likely losing 20-30% of your team's time to manual data entry.")

# --- TAB 2: BANK RELATIONSHIP MANAGEMENT ---
with tab2:
    st.subheader("Managing Your Financial Partners")
    st.write("A CFO must manage banks not just as lenders, but as service providers. This involves tracking 'Wallet Share' and service fees.")
    
    st.markdown("### 📊 Bank Fee Analysis Simulator")
    bank_name = st.text_input("Bank Name", "Global Partner Bank")
    monthly_trans = st.number_input("Monthly Transactions", value=5000)
    fee_per_trans = st.number_input("Fee per Transaction ($)", value=0.50)
    maintenance_fee = st.number_input("Monthly Maintenance Fee ($)", value=1000)
    
    total_monthly = (monthly_trans * fee_per_trans) + maintenance_fee
    st.metric(f"Estimated Monthly Cost ({bank_name})", f"${total_monthly:,.2f}")
    
    st.markdown("""
    **CFO Tip:** Conduct an annual 'Bank Scorecard' review. Evaluate them on:
    1. Pricing competitiveness.
    2. Quality of customer service.
    3. Technical stability of their online portal.
    """)

# --- TAB 3: FRAUD PREVENTION & SECURITY ---
with tab3:
    st.subheader("Protecting the Vault")
    st.write("Treasury is a prime target for cybercriminals. Security is not just an IT issue; it's a financial internal control.")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown('<div class="tech-card"><strong>Dual Control</strong><br>Ensuring no single individual can both initiate and approve a payment (Segregation of Duties).</div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown('<div class="tech-card"><strong>Whitelist Management</strong><br>Only allowing payments to pre-approved vendor bank accounts.</div>', unsafe_allow_html=True)

    st.error("🚨 **Business Email Compromise (BEC):** The most common fraud where hackers spoof an executive's email to request an urgent wire. Always verify 'out-of-band' (phone call) before sending funds.")

# --- TAB 4: QUIZ ---
with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Operations Mastery Quiz")
    
    m5_q1 = st.radio("1. What is the primary benefit of a TMS over Excel?", 
                  ["It has better fonts", "Real-time bank visibility and automation", "It is cheaper"], key="m5_q1")
    
    m5_q2 = st.radio("2. Which protocol is the global standard for secure financial messaging between banks?", 
                  ["HTTP", "SWIFT", "FTP"], key="m5_q2")
    
    if st.button("Submit Module 5 Quiz", key="m5_quiz_btn"):
        score = 0
        if m5_q1 == "Real-time bank visibility and automation": score += 1
        if m5_q2 == "SWIFT": score += 1
        
        st.write(f"Your Score: {score}/2")
        if score == 2: st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: SUMMARY ---
with tab5:
    st.markdown("""
    ### 📌 Module 5 Recap
    *   **TMS:** Move from manual tracking to automated systems to reduce risk and increase speed.
    *   **Bank Relationships:** Track your fees and treat banks as strategic service providers.
    *   **Controls:** Implement Dual Control and Whitelisting to prevent multi-million dollar fraud losses.
    
    **CFO Perspective:** Technology is the great multiplier. A CFO who masters the tech stack can manage 10x more complexity with the same headcount.
    """)