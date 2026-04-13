import streamlit as st

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>💰 Module 4: Statutory Funds & WPPF</h1>", unsafe_allow_html=True)
st.write("---")

st.info("""
**Finance Core:** This module covers the 5% Profit Sharing (WPPF) and long-term employee benefits (Gratuity/PF).
""")

# --- SECTION 1: WPPF CALCULATOR ---
st.header("1. 📈 WPPF Distribution (5% Rule)")
st.write("Applicable if Paid-up Capital > BDT 10M or Fixed Assets > BDT 20M.")

net_profit = st.number_input("Annual Net Profit Before Tax (BDT)", min_value=0, value=10000000, step=1000000)

wppf_total = net_profit * 0.05

st.subheader("Distribution Breakdown")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Participation Fund (80%)", f"{(wppf_total * 0.8):,.2f}")
    st.caption("Distributed to workers")

with col2:
    st.metric("Welfare Fund (10%)", f"{(wppf_total * 0.1):,.2f}")
    st.caption("Internal worker welfare")

with col3:
    st.metric("Govt Foundation (10%)", f"{(wppf_total * 0.1):,.2f}")
    st.caption("Paid to Govt Fund")

st.divider()

# --- SECTION 2: GRATUITY RULES ---
st.header("2. 📜 Gratuity Calculation (AS PER 2025/2026 STANDARDS)")
st.write("Workers are eligible after **5 years** of continuous service.")

with st.expander("See Calculation Tiers"):
    st.markdown("""
    * **5 to 10 years:** 30 days' basic wages for every completed year.
    * **Over 10 years:** 45 days' basic wages for every completed year.
    * **Resignation (New Tier):** Permanent workers with 3+ years service now get partial compensation even upon resignation.
    """)

# --- SECTION 3: PROVIDENT FUND (PF) ---
st.header("3. Provident Fund Compliance")
st.write("PF is mandatory if 75% of workers demand it in an establishment with 10+ workers.")

st.warning("""
**Tax Note for Accountants:** - Employer's contribution is a deductible expense.
- The PF Trust must be 'Recognized' by the NBR for tax benefits.
""")

# --- QUIZ ---
st.divider()
st.header("4. 🧠 WPPF Knowledge Check")
q_wppf = st.radio("What percentage of net profit must be allocated to WPPF?", ["2%", "5%", "10%"])

if st.button("Check WPPF Answer"):
    if q_wppf == "5%":
        st.success("Correct! 5% of Net Profit before tax must be distributed among the three funds.")
        st.balloons()
    else:
        st.error("Incorrect. The statutory requirement is 5%.")