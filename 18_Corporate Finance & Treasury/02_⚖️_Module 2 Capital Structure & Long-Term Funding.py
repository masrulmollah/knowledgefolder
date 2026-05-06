import streamlit as st
import pandas as pd
import numpy as np

# --- STYLING & CUSTOM CSS ---
st.markdown("""
    <style>
    .main-header {
        color: #065F46;
        font-size: 32px;
        font-weight: bold;
        border-bottom: 2px solid #065F46;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .theory-card {
        background-color: #ecfdf5;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #059669;
        margin-bottom: 15px;
    }
    .quiz-box {
        background-color: #f0f9ff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #bae6fd;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">Module 2: Capital Structure & Long-Term Funding</div>', unsafe_allow_html=True)

# --- TABS FOR ORGANIZATION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "⚖️ Debt vs Equity", 
    "📈 Modigliani-Miller", 
    "💸 Dividend Policy", 
    "📝 Quiz", 
    "📋 Summary"
])

# --- TAB 1: DEBT VS EQUITY ---
with tab1:
    st.subheader("The Financing Decision")
    st.write("""
    A CFO must decide the optimal mix of funds. **Debt** offers tax shields but increases bankruptcy risk. 
    **Equity** is flexible but more expensive and dilutes ownership.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="theory-card"><strong>Debt Financing</strong><br>• Lower cost (Tax Shield)<br>• Fixed obligations<br>• Higher risk during downturns</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="theory-card"><strong>Equity Financing</strong><br>• Higher cost (Risk Premium)<br>• No fixed repayment<br>• Dilutes control & earnings</div>', unsafe_allow_html=True)

# --- TAB 2: MODIGLIANI-MILLER (MM) THEORY ---
with tab2:
    st.subheader("Capital Structure Theory")
    st.write("Does capital structure even matter? MM Theory provides the framework.")
    
    st.info("**MM Proposition I (With Taxes):** Firm value increases with debt because interest is tax-deductible.")
    
    # Simple Tax Shield Calculator
    st.markdown("### 🛡️ Interest Tax Shield Calculator")
    col_tax1, col_tax2 = st.columns(2)
    
    with col_tax1:
        debt_amt = st.number_input("Total Debt ($)", value=1000000, step=50000, key="m2_debt")
        int_rate = st.slider("Interest Rate (%)", 1.0, 15.0, 6.0, key="m2_int") / 100
        tax_rate = st.slider("Tax Rate (%)", 0.0, 40.0, 25.0, key="m2_tax") / 100
    
    with col_tax2:
        annual_interest = debt_amt * int_rate
        tax_shield = annual_interest * tax_rate
        st.metric("Annual Tax Savings", f"${tax_shield:,.0f}")
        st.write(f"By using debt, the company saves **${tax_shield:,.0f}** in taxes every year.")

# --- TAB 3: DIVIDEND & PAYOUT POLICY ---
with tab3:
    st.subheader("Returning Wealth to Shareholders")
    st.write("How should we pay out excess cash? Dividends or Share Buybacks?")
    
    method = st.selectbox("Select Payout Strategy", ["Cash Dividends", "Share Buybacks"])
    
    if method == "Cash Dividends":
        st.write("**Impact:** Provides immediate income to shareholders. Usually seen as a sign of stability.")
    else:
        st.write("**Impact:** Reduces shares outstanding, increasing Earnings Per Share (EPS). Often tax-efficient.")

    # Visualization of Payout Impact
    st.markdown("### EPS Impact Simulator")
    earnings = st.number_input("Net Income ($)", value=500000, key="m2_earn")
    shares = st.number_input("Shares Outstanding", value=100000, key="m2_shares")
    buyback_amt = st.slider("Amount to spend on Buyback ($)", 0, 100000, 50000, step=5000)
    share_price = st.number_input("Current Share Price ($)", value=50)
    
    shares_retired = buyback_amt / share_price
    new_shares = shares - shares_retired
    old_eps = earnings / shares
    new_eps = earnings / new_shares
    
    st.metric("New EPS after Buyback", f"${new_eps:.2f}", delta=f"{((new_eps/old_eps)-1)*100:.2f}% improvement")

# --- TAB 4: QUIZ ---
with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Module 2 Knowledge Check")
    
    m2_q1 = st.radio("1. What is the 'Tax Shield' in Corporate Finance?", 
                  ["Government grants", "The tax savings from interest payments", "A way to hide assets"], key="m2_q1")
    
    m2_q2 = st.radio("2. If a company buys back its own shares, what usually happens to EPS?", 
                  ["It decreases", "It stays the same", "It increases"], key="m2_q2")
    
    if st.button("Submit Module 2 Quiz", key="m2_quiz_btn"):
        score = 0
        if m2_q1 == "The tax savings from interest payments": score += 1
        if m2_q2 == "It increases": score += 1
        
        st.write(f"Your Score: {score}/2")
        if score == 2: st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: SUMMARY ---
with tab5:
    st.markdown("""
    ### 📌 Module 2 Recap
    *   **Capital Mix:** Finding the balance between the 'cheaper' debt and 'safer' equity.
    *   **Tax Shield:** Debt is subsidized by the government via interest deductibility.
    *   **Payouts:** Companies must decide between dividends (income) and buybacks (growth).
    
    **CFO Perspective:** Your goal is to find the **Optimal Capital Structure** that minimizes WACC and maximizes firm value.
    """)