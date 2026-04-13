import streamlit as st

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>💸 Module 2: Payroll & Compensation</h1>", unsafe_allow_html=True)
st.write("---")

st.info("""
**Focus:** Accuracy in Wage calculation, Overtime, and statutory deductions. 
Errors in this module lead to Labor Court disputes and financial penalties.
""")

# --- SECTION 1: OVERTIME CALCULATOR ---
st.header("1. 🧮 Interactive Overtime (OT) Calculator")
st.write("According to BLA 2006, OT must be **double the ordinary rate** of basic wages.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Data")
    monthly_basic = st.number_input("Monthly Basic Salary (BDT)", min_value=0, value=10000, step=500)
    ot_hours = st.number_input("Total OT Hours worked", min_value=0, value=10, step=1)
    
    # Standard formula for Bangladesh: (Basic / 26 / 8) * 2 * OT Hours
    # 26 working days, 8 hours per day
    hourly_rate = (monthly_basic / 26) / 8
    ot_payment = hourly_rate * 2 * ot_hours

with col2:
    st.subheader("Calculation Result")
    st.metric(label="Single Hourly Rate", value=f"{round(hourly_rate, 2)} BDT")
    st.metric(label="Total OT Payable", value=f"{round(ot_payment, 2)} BDT", delta="Double Rate Applied")
    
    with st.expander("Show Formula"):
        st.latex(r"OT = \left( \frac{Basic}{26 \times 8} \right) \times 2 \times Hours")

st.divider()

# --- SECTION 2: WAGE COMPONENTS ---
st.header("2. Wage Structure & Deductions")
st.write("Finance teams must distinguish between what is legally allowed to be deducted and what is not.")

tab1, tab2 = st.tabs(["Allowed Deductions", "Festival Bonuses"])

with tab1:
    st.markdown("""
    **Legally Permissible Deductions:**
    * Absence from duty.
    * Damage or loss of goods expressly entrusted to the worker.
    * House-accommodation provided by the employer.
    * Recovery of advances or adjustment of over-payments.
    * Income Tax payable by the worker.
    """)
    st.error("⚠️ **Warning:** Total deductions cannot usually exceed 50% of the wages.")

with tab2:
    st.markdown("""
    **Festival Bonus Rules:**
    * Every worker who has completed **1 year of service** is entitled to two festival bonuses per year.
    * Each bonus should not exceed the basic wage.
    * For non-permanent workers, it is often calculated based on continuous service length.
    """)

# --- SECTION 3: PAYROLL QUIZ ---
st.header("3. 🧠 Payroll Compliance Quiz")

q_pay = st.radio(
    "What is the divisor used to find the daily basic rate for OT in a standard month?",
    ["30 days", "26 days", "22 days"]
)

if st.button("Verify Answer"):
    if q_pay == "26 days":
        st.success("Correct! Under the Labour Rules, 26 is the standard divisor used for converting monthly basic to daily basic for OT calculations.")
        st.balloons()
    else:
        st.error("Incorrect. While a month has 30 days, 26 is the standard divisor used for OT logic in Bangladesh.")

# --- SIDEBAR PROGRESS ---
st.sidebar.markdown("### Module 2 Progress")
st.sidebar.progress(100)
st.sidebar.write("✅ OT Calculator Ready")
st.sidebar.write("✅ Deduction Rules Covered")