import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- STYLING & CUSTOM CSS ---
st.markdown("""
    <style>
    .main-header {
        color: #7C3AED;
        font-size: 32px;
        font-weight: bold;
        border-bottom: 2px solid #7C3AED;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .treasury-card {
        background-color: #F5F3FF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #7C3AED;
        margin-bottom: 15px;
    }
    .quiz-box {
        background-color: #FDF2F8;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #FBCFE8;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">Module 3: Strategic Treasury Management</div>', unsafe_allow_html=True)

# --- TABS FOR ORGANIZATION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💧 Liquidity & Cash", 
    "⚙️ Working Capital", 
    "🔮 Forecasting", 
    "📝 Quiz", 
    "📋 Summary"
])

# --- TAB 1: LIQUIDITY & CASH MANAGEMENT ---
with tab1:
    st.subheader("Cash is King")
    st.write("""
    Treasury management ensures the company has enough liquidity to meet its obligations. 
    A CFO must balance 'Idle Cash' (which earns nothing) against 'Liquidity Risk' (not having enough to pay bills).
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="treasury-card"><strong>Cash Pooling</strong><br>Consolidating balances from different subsidiaries to minimize borrowing costs and maximize interest income.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="treasury-card"><strong>Netting</strong><br>Offsetting intra-company payables and receivables to reduce transaction volume and FX costs.</div>', unsafe_allow_html=True)

# --- TAB 2: WORKING CAPITAL OPTIMIZATION ---
with tab2:
    st.subheader("The Cash Conversion Cycle (CCC)")
    st.write("The CCC measures how fast a company converts its investment in inventory back into cash.")
    
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        dio = st.number_input("Days Inventory Outstanding (DIO)", value=45, key="m3_dio")
        dso = st.number_input("Days Sales Outstanding (DSO)", value=30, key="m3_dso")
        dpo = st.number_input("Days Payables Outstanding (DPO)", value=40, key="m3_dpo")
        
        ccc = dio + dso - dpo
        st.metric("Cash Conversion Cycle", f"{ccc} Days")
    
    with col_b:
        st.write("**The Formula:**")
        st.latex(r"CCC = DIO + DSO - DPO")
        if ccc < 30:
            st.success("Efficient: You are turning inventory into cash quickly.")
        else:
            st.warning("Inefficient: Your cash is trapped in the operating cycle.")

# --- TAB 3: CASH FLOW FORECASTING ---
with tab3:
    st.subheader("Predictive Liquidity")
    st.write("A 13-week rolling forecast is the industry standard for short-term liquidity management.")
    
    # Interactive Forecast Chart
    weeks = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"]
    inflows = [100, 120, 80, 150, 90, 110, 130, 140]
    outflows = [90, 100, 110, 95, 100, 85, 90, 105]
    
    df_forecast = pd.DataFrame({
        "Week": weeks,
        "Inflows": inflows,
        "Outflows": outflows
    })
    df_forecast["Net Cash Flow"] = df_forecast["Inflows"] - df_forecast["Outflows"]
    
    fig = px.bar(df_forecast, x="Week", y=["Inflows", "Outflows"], barmode="group",
                 title="8-Week Cash Inflow vs Outflow",
                 color_discrete_sequence=["#10B981", "#EF4444"])
    st.plotly_chart(fig, use_container_width=True)

# --- TAB 4: QUIZ ---
with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Treasury Mastery Test")
    
    m3_q1 = st.radio("1. What happens to the CCC if you pay your suppliers faster?", 
                  ["The CCC decreases", "The CCC increases", "No change"], key="m3_q1")
    
    m3_q2 = st.radio("2. Which tool is used to consolidate cash from various bank accounts?", 
                  ["Cash Pooling", "Dividend Payout", "Capital Budgeting"], key="m3_q2")
    
    if st.button("Submit Module 3 Quiz", key="m3_quiz_btn"):
        score = 0
        if m3_q1 == "The CCC increases": score += 1
        if m3_q2 == "Cash Pooling": score += 1
        
        st.write(f"Your Score: {score}/2")
        if score == 2: st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: SUMMARY ---
with tab5:
    st.markdown("""
    ### 📌 Module 3 Recap
    *   **Liquidity:** Treasury's primary goal is ensuring the company never runs out of cash.
    *   **CCC:** Manage DIO, DSO, and DPO to release 'trapped' cash from the balance sheet.
    *   **Forecasting:** Visibility is key. Use rolling forecasts to anticipate funding gaps.
    
    **CFO Perspective:** A great CFO doesn't just manage profit; they manage **Cash Flow**. Profit is an accounting concept; Cash is a reality.
    """)