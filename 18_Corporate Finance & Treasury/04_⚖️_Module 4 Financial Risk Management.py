import streamlit as st
import pandas as pd
import numpy as np

# --- STYLING & CUSTOM CSS ---
st.markdown("""
    <style>
    .main-header {
        color: #DC2626;
        font-size: 32px;
        font-weight: bold;
        border-bottom: 2px solid #DC2626;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .risk-card {
        background-color: #FEF2F2;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #DC2626;
        margin-bottom: 15px;
    }
    .quiz-box {
        background-color: #FFF7ED;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #FFEDD5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">Module 4: Financial Risk Management</div>', unsafe_allow_html=True)

# --- TABS FOR ORGANIZATION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 FX Risk", 
    "📈 Interest Rate Risk", 
    "🛡️ Hedging Strategies", 
    "📝 Quiz", 
    "📋 Summary"
])

# --- TAB 1: FOREIGN EXCHANGE (FX) RISK ---
with tab1:
    st.subheader("Managing Global Currency Exposure")
    st.write("""
    For global companies, currency fluctuations can wipe out operating profits overnight. 
    A CFO must manage three types of exposure:
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="risk-card"><strong>Transaction</strong><br>Risk that the exchange rate changes between entering a contract and settling it.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="risk-card"><strong>Translation</strong><br>Risk when consolidating financial statements of foreign subsidiaries into the home currency.</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="risk-card"><strong>Economic</strong><br>Long-term risk to the company\'s market value due to currency shifts.</div>', unsafe_allow_html=True)

# --- TAB 2: INTEREST RATE RISK ---
with tab2:
    st.subheader("The Cost of Borrowing")
    st.write("If a company has floating-rate debt, an increase in central bank rates directly increases interest expense.")
    
    st.markdown("### 📉 Floating vs. Fixed Rate Impact")
    loan_amt = st.number_input("Total Floating Rate Debt ($)", value=5000000, step=500000, key="m4_loan")
    current_rate = st.slider("Current Interest Rate (%)", 1.0, 10.0, 5.0, key="m4_curr_rate") / 100
    rate_hike = st.slider("Potential Rate Hike (Basis Points)", 0, 300, 100, key="m4_hike") / 10000
    
    impact = loan_amt * rate_hike
    st.metric("Additional Annual Interest Expense", f"${impact:,.0f}", delta="Increase", delta_color="inverse")
    st.info(f"A {rate_hike*10000:.0f} bps hike increases your cost from ${loan_amt*current_rate:,.0f} to ${(loan_amt*(current_rate+rate_hike)):,.0f}.")

# --- TAB 3: HEDGING STRATEGIES ---
with tab3:
    st.subheader("Derivatives as Insurance")
    st.write("CFOs use derivatives to 'lock in' prices and create certainty.")
    
    strategy = st.selectbox("Select a Hedging Tool", ["Forward Contract", "Currency Option", "Interest Rate Swap"])
    
    if strategy == "Forward Contract":
        st.write("**Definition:** An obligation to buy/sell at a fixed price on a future date. No upfront cost, but no benefit if the market moves in your favor.")
    elif strategy == "Currency Option":
        st.write("**Definition:** The right, but not the obligation, to trade. Requires an upfront premium but allows you to benefit from favorable market moves.")
    else:
        st.write("**Definition:** Exchanging a floating interest rate for a fixed one (or vice-versa) with a counterparty.")

    st.warning("⚠️ **Warning:** Hedging should be used to reduce risk, not for speculation. Over-hedging can be as dangerous as not hedging at all.")

# --- TAB 4: QUIZ ---
with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Risk Management Challenge")
    
    m4_q1 = st.radio("1. Which risk type involves the impact of currency on the balance sheet during consolidation?", 
                  ["Transaction Exposure", "Translation Exposure", "Economic Exposure"], key="m4_q1")
    
    m4_q2 = st.radio("2. If you want to lock in an exchange rate but still want the choice to walk away if the rate improves, which tool do you use?", 
                  ["Forward Contract", "Futures Contract", "Currency Option"], key="m4_q2")
    
    if st.button("Submit Module 4 Quiz", key="m4_quiz_btn"):
        score = 0
        if m4_q1 == "Translation Exposure": score += 1
        if m4_q2 == "Currency Option": score += 1
        
        st.write(f"Your Score: {score}/2")
        if score == 2: st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: SUMMARY ---
with tab5:
    st.markdown("""
    ### 📌 Module 4 Recap
    *   **FX Risk:** Categorize your exposure into Transaction, Translation, and Economic.
    *   **Sensitivity:** Always stress-test your debt against potential interest rate hikes.
    *   **Hedging:** Use Forwards and Options to create budget certainty.
    
    **CFO Perspective:** Your goal is **predictability**. Investors hate surprises; a well-hedged company is a more valuable company because its cash flows are stable.
    """)