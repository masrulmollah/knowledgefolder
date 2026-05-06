import streamlit as st
import pandas as pd
import numpy as np

# --- STYLING & CUSTOM CSS ---
# Fixed the TypeError by using the correct argument: unsafe_allow_html=True
st.markdown("""
    <style>
    .main-header {
        color: #1E3A8A;
        font-size: 32px;
        font-weight: bold;
        border-bottom: 2px solid #1E3A8A;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .concept-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 15px;
    }
    .quiz-box {
        background-color: #fff4e6;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ffd8a8;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">Module 1: Corporate Finance Foundations</div>', unsafe_allow_html=True)

# --- TABS FOR ORGANIZATION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Time Value", 
    "🏗️ Capital Budgeting", 
    "💰 Cost of Capital", 
    "📝 Quiz", 
    "📋 Summary"
])

# --- TAB 1: TIME VALUE OF MONEY ---
with tab1:
    st.subheader("Time Value of Money (TVM)")
    st.write("""
    The core principle: **A dollar today is worth more than a dollar tomorrow.** 
    This is due to inflation, risk, and the opportunity cost of interest.
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Calculator**")
        pv_val = st.number_input("Present Value (PV)", value=1000.0, step=100.0, key="mod1_pv")
        r_val = st.slider("Annual Interest Rate (%)", 0.0, 20.0, 8.0, key="mod1_r") / 100
        t_val = st.number_input("Years (t)", value=5, step=1, key="mod1_t")
        
        fv_val = pv_val * (1 + r_val)**t_val
        st.metric("Future Value (FV)", f"${fv_val:,.2f}")

    with col2:
        st.markdown("**Core Formulas**")
        st.latex(r"FV = PV \times (1 + r)^t")
        st.latex(r"PV = \frac{FV}{(1 + r)^t}")
        st.info("The Compounding Effect: Interest earned on interest is what drives long-term wealth creation.")

# --- TAB 2: CAPITAL BUDGETING ---
with tab2:
    st.subheader("Capital Budgeting & Project Selection")
    st.write("How a CFO decides which projects to fund. We prioritize **NPV** because it measures absolute value creation.")

    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        cost_val = st.number_input("Initial Investment ($)", value=10000.0, step=1000.0, key="mod1_cost")
        wacc_input = st.slider("Discount Rate (WACC %)", 5.0, 20.0, 10.0, key="mod1_wacc_slider") / 100
        
        # Cash Flow Table
        cf_data = {"Year": [1, 2, 3, 4, 5], "Cash Flow": [3000, 3500, 4000, 4000, 4500]}
        df_cf = pd.DataFrame(cf_data)
        df_cf["Discounted CF"] = df_cf["Cash Flow"] / (1 + wacc_input)**df_cf["Year"]
        
        st.dataframe(df_cf.style.format({"Cash Flow": "${:,.0f}", "Discounted CF": "${:,.2f}"}), use_container_width=True)

    with col_b:
        npv_val = df_cf["Discounted CF"].sum() - cost_val
        st.metric("Project NPV", f"${npv_val:,.2f}")
        
        if npv_val > 0:
            st.success("✅ Accept: Project creates shareholder value.")
        else:
            st.error("❌ Reject: Project destroys value.")

# --- TAB 3: COST OF CAPITAL ---
with tab3:
    st.subheader("Weighted Average Cost of Capital (WACC)")
    st.write("The hurdle rate. If your project return is lower than WACC, you are losing money for your investors.")
    
    c1, c2 = st.columns(2)
    with c1:
        e_val = st.number_input("Equity Value", value=700000, key="mod1_equity")
        d_val = st.number_input("Debt Value", value=300000, key="mod1_debt")
        re_val = st.number_input("Cost of Equity %", value=12.0, key="mod1_re") / 100
    with c2:
        rd_val = st.number_input("Cost of Debt %", value=7.0, key="mod1_rd") / 100
        tax_val = st.number_input("Corporate Tax %", value=25.0, key="mod1_tax") / 100
        
        total_v_val = e_val + d_val
        wacc_val = ((e_val/total_v_val) * re_val) + ((d_val/total_v_val) * rd_val * (1 - tax_val))
        st.metric("Final WACC", f"{wacc_val*100:.2f}%")

# --- TAB 4: QUIZ ---
with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Test Your Knowledge")
    
    q1_ans = st.radio("1. Which method is considered the 'Gold Standard' for project evaluation?", 
                  ["Payback Period", "Net Present Value (NPV)", "Internal Rate of Return (IRR)"], key="q1")
    
    q2_ans = st.radio("2. Why is the cost of debt usually cheaper than the cost of equity?", 
                  ["Debt is less risky", "Interest is tax-deductible", "Both of the above"], key="q2")
    
    if st.button("Submit Answers", key="quiz_btn"):
        current_score = 0
        if q1_ans == "Net Present Value (NPV)": current_score += 1
        if q2_ans == "Both of the above": current_score += 1
        
        st.write(f"Your Score: {current_score}/2")
        if current_score == 2: st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: SUMMARY ---
with tab5:
    st.markdown("""
    ### 📌 Module 1 Recap
    *   **TVM:** Money has a time value; always discount future cash flows.
    *   **NPV:** The most reliable tool for decision-making. Accept if > 0.
    *   **WACC:** The cost of the money you are using. It is the 'hurdle' projects must clear.
    
    **Next Steps:** Move to Module 2 to explore how we choose between Debt and Equity (Capital Structure).
    """)
    
    st.info("Tip: Use the calculators in the previous tabs to simulate different business scenarios!")