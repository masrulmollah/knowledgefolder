import streamlit as st

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 4: Functions",
        page_icon="📦",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("📦 Module 4: Functions & Modular Code")
st.markdown("""
Think of a **Function** as a specialized "Calculation Engine." You give it inputs (data), it performs a specific task (logic), and it returns a result. This is how we build scalable, error-free financial systems.
""")

st.divider()

# --- SECTION 1: BUILDING A CUSTOM FORMULA ---
st.header("1. Creating Your Own 'Financial Engine'")
st.write("Let's build a function that calculates **Net Pay** after a fixed tax rate and a flat deduction.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Values")
    gross_salary = st.number_input("Gross Monthly Salary", value=5000.0)
    tax_rate = st.slider("Tax Rate (%)", 0, 40, 20) / 100
    pension = st.number_input("Fixed Pension Deduction", value=200.0)

with col2:
    # Defining the Function Logic
    def calculate_net_pay(gross, tax, ded):
        tax_amount = gross * tax
        net = gross - tax_amount - ded
        return net, tax_amount

    # Calling the Function
    net_salary, total_tax = calculate_net_pay(gross_salary, tax_rate, pension)
    
    st.subheader("The Output")
    st.metric("Final Net Pay", f"${net_salary:,.2f}")
    st.write(f"Total Tax Withheld: **${total_tax:,.2f}**")

# Showing the modular code
st.subheader("The Python Definition")
st.code(f"""
def calculate_net_pay(gross, tax, ded):
    tax_amount = gross * tax
    net = gross - tax_amount - ded
    return net

# Usage:
result = calculate_net_pay({gross_salary}, {tax_rate}, {pension})
""", language="python")

st.divider()

# --- SECTION 2: WHY USE FUNCTIONS? ---
st.header("2. Benefits for Accountants")
c1, c2, c3 = st.columns(3)

with c1:
    st.write("### 🛠️ Reusability")
    st.write("Write the 'Lease Accounting' logic once and use it across 100 different contracts.")
with c2:
    st.write("### 🔍 Accuracy")
    st.write("Updating the formula in one place updates it everywhere, reducing 'copy-paste' errors.")
with c3:
    st.write("### 📁 Readability")
    st.write("Your main script becomes cleaner: `tax = calculate_vat(total_sales)` is easy to read.")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 4 Quiz")
st.write("Understand the mechanics of a function.")

q_func = st.radio(
    "In a function, what do you call the values you 'pass into' the function (like the Gross Salary)?",
    ["Returns", "Arguments (or Parameters)", "Variables"]
)

if st.button("Check Answer"):
    if "Arguments" in q_func:
        st.balloons()
        st.success("Correct! Arguments are the inputs the function needs to perform its job.")
    else:
        st.error("Try again! Returns are what comes *out* of a function, not what goes *in*.")

st.markdown("---")
st.caption("Knowledge Folder | Module 4: Functions & Modular Code")