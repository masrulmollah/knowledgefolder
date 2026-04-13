import streamlit as st

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>📅 Module 3: Leave & Maternity Benefits</h1>", unsafe_allow_html=True)
st.write("---")

st.info("""
**Finance Perspective:** Leave is not just time off; it is a financial liability. 
Unspent 'Earned Leave' must be provisioned in the year-end balance sheet.
""")

# --- SECTION 1: MATERNITY BENEFIT CALCULATOR ---
st.header("1. 🤱 Maternity Benefit (2025/2026 Update)")
st.warning("Update: Maternity leave is now **120 days** (increased from 112 days).")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Payment Calculation")
    avg_wage = st.number_input("Average Daily Wage (Total of last 3 months / total days worked)", min_value=0, value=1000)
    st.caption("Formula: Daily Wage x 120 Days")

with col2:
    total_benefit = avg_wage * 120
    st.metric(label="Total Maternity Payable", value=f"{total_benefit:,.2f} BDT")
    st.write("**Payment Schedule:** Usually paid in two installments (before and after delivery).")

st.divider()

# --- SECTION 2: LEAVE TYPES ---
st.header("2. Types of Statutory Leave")

leave_data = {
    "Leave Type": ["Casual Leave", "Sick Leave", "Festival Holiday", "Earned Leave (Factory)", "Earned Leave (Commercial)"],
    "Days": ["10 Days", "14 Days", "11 Days", "1 per 18 days worked", "1 per 14 days worked"],
    "Encashable?": ["No", "No", "No (Compensatory instead)", "Yes", "Yes"]
}

st.table(leave_data)

# --- SECTION 3: EARNED LEAVE PROVISIONING ---
st.header("3. 🧮 Earned Leave Provisioning Tool")
st.write("Use this to calculate the liability for a worker's unspent leave.")

c1, c2, c3 = st.columns(3)
with c1:
    daily_basic = st.number_input("Daily Basic Rate", value=500)
with c2:
    unspent_days = st.number_input("Unspent Earned Leave Days", value=15)
with c3:
    liability = daily_basic * unspent_days
    st.metric("Provision Amount", f"{liability:,.2f} BDT")

# --- QUIZ ---
st.divider()
st.header("4. 🧠 Leave Compliance Quiz")
choice = st.radio("Can a worker carry forward their Sick Leave to the next year?", ["Yes", "No"])

if st.button("Check Answer"):
    if choice == "No":
        st.success("Correct! Sick leave and Casual leave expire at the end of the year. Only Earned Leave can be carried forward.")
    else:
        st.error("Incorrect. Sick leave is 'use it or lose it' and cannot be carried forward.")