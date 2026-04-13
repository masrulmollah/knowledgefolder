import streamlit as st

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚪 Module 5: Termination & Final Settlement</h1>", unsafe_allow_html=True)
st.write("---")

st.info("""
**Finance Objective:** Calculate the "Full & Final Settlement" (F&F) accurately to prevent Labor Court litigation.
Notice periods and compensation rates vary significantly by the *method* of exit.
""")

# --- SECTION 1: EXIT CALCULATOR ---
st.header("1. ⚖️ Termination vs. Resignation Calculator")
st.write("Select the exit type to see the financial obligations.")

exit_type = st.selectbox("Reason for Exit:", 
                        ["Resignation (by Worker)", 
                         "Termination (by Employer - Without Cause)", 
                         "Retrenchment (Redundancy)", 
                         "Dismissal (Misconduct)"])

monthly_basic = st.number_input("Last Drawn Basic Salary (BDT)", value=20000)
years_service = st.number_input("Years of Continuous Service", min_value=0, value=5)

st.subheader("Financial Breakdown")

if exit_type == "Resignation (by Worker)":
    notice_period = "60 Days"
    st.write(f"**Notice Required:** {notice_period}")
    st.write("**Gratuity/Compensation:**")
    if years_service >= 10:
        comp = (monthly_basic * years_service) # 30 days per year
        st.success(f"Payable: {comp:,.2f} BDT (30 days per year)")
    elif years_service >= 5:
        comp = (monthly_basic / 30 * 14) * years_service # 14 days per year
        st.warning(f"Payable: {comp:,.2f} BDT (14 days per year for <10 yrs)")
    else:
        st.error("No statutory compensation/gratuity for less than 5 years service.")

elif exit_type == "Termination (by Employer - Without Cause)":
    st.write("**Notice Required:** 120 Days (for monthly rated permanent worker)")
    st.write("**Pay in Lieu of Notice:** 4 months of basic wages if no notice given.")
    comp = (monthly_basic * years_service) # 30 days per year
    st.success(f"Compensation: {comp:,.2f} BDT (or Gratuity, whichever is higher)")

elif exit_type == "Retrenchment (Redundancy)":
    st.write("**Notice Required:** 1 Month")
    comp = (monthly_basic * years_service) # 30 days per year
    st.success(f"Retrenchment Compensation: {comp:,.2f} BDT")

elif exit_type == "Dismissal (Misconduct)":
    st.error("No Notice Pay Required. No Compensation (except PF) if dismissed for misconduct.")

st.divider()

# --- SECTION 2: FINAL SETTLEMENT CHECKLIST ---
st.header("2. 📋 F&F Checklist for Accounts")
st.checkbox("Arrears Salary (Calculated up to the last working day)")
st.checkbox("Notice Pay (if applicable)")
st.checkbox("Earned Leave Encashment (Max 40-60 days depending on policy)")
st.checkbox("Gratuity / Termination Compensation")
st.checkbox("Provident Fund (Employee + Employer Contribution)")
st.checkbox("WPPF (Pro-rata share of the current year's profit)")

# --- QUIZ ---
st.header("3. 🧠 Exit Logic Quiz")
q_exit = st.radio("What is the notice period for a permanent monthly-rated worker to RESIGN?", ["30 Days", "60 Days", "90 Days"])

if st.button("Submit"):
    if q_exit == "60 Days":
        st.success("Correct! Under the Act, a permanent worker must give 60 days notice to resign.")
    else:
        st.error("Incorrect. It is 60 days for permanent workers.")