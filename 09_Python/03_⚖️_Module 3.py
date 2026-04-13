import streamlit as st

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 3: Audit Logic",
        page_icon="⚖️",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("⚖️ Module 3: Flow Control & Audit Logic")
st.markdown("""
Real-world finance is full of rules: *"If the variance is > 10%, flag it."* or *"For every cost center, calculate the tax."* This module teaches you how to translate those business rules into Python logic using **Conditionals** and **Loops**.
""")

st.divider()

# --- SECTION 1: CONDITIONALS (The IF-Statement) ---
st.header("1. Automated Variance Flagging")
st.write("Conditionals allow Python to make decisions. Let's build a budget variance checker.")

col1, col2 = st.columns([1, 1])

with col1:
    budget = st.number_input("Budgeted Amount", value=100000)
    actual = st.number_input("Actual Spend", value=115000)
    threshold = st.slider("Threshold for Warning (%)", 0, 20, 10)

with col2:
    variance = (actual - budget) / budget
    st.write(f"### Variance: {variance:.1%}")
    
    # Python Logic
    if variance > (threshold / 100):
        st.error("🚩 ALERT: Significant Overspend Detected!")
        status = "Overspend"
    elif variance < -(threshold / 100):
        st.info("💰 SAVING: Under-budget detected.")
        status = "Under-budget"
    else:
        st.success("✅ WITHIN LIMIT: Spend is acceptable.")
        status = "Normal"

    st.code(f"""
if variance > {threshold/100}:
    print("Alert: Overspend")
elif variance < -{threshold/100}:
    print("Saving detected")
else:
    print("Within limit")
    """, language="python")

st.divider()

# --- SECTION 2: LOOPS (The FOR-Statement) ---
st.header("2. Looping through Transactions")
st.write("Loops are used to perform the same action on a list of items—like applying VAT to a batch of invoices.")

invoice_amounts = [1200, 4500, 800, 3200]
vat_rate = 0.15

st.write(f"Raw Invoice Batch: `{invoice_amounts}`")

if st.button("🚀 Process Batch (Apply 15% VAT)"):
    processed_invoices = []
    
    # Code Simulation
    for amount in invoice_amounts:
        total = amount * (1 + vat_rate)
        processed_invoices.append(total)
        st.write(f"Processed: ${amount:,.2f} ➡️ **${total:,.2f}** (Incl. VAT)")
    
    st.success("Batch Processing Complete!")
    
    st.code("""
# How the loop works
for amount in invoice_amounts:
    total = amount * 1.15
    print(total)
    """, language="python")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 3 Quiz")
st.write("Test your logic on handling exceptions.")

q_logic = st.radio(
    "Which command would you use to iterate through a list of 500 employee salaries to calculate a bonus?",
    ["if-else", "for loop", "variable assignment"]
)

if st.button("Verify Logic"):
    if q_logic == "for loop":
        st.balloons()
        st.success("Correct! Loops are used for repetitive tasks over a collection of data.")
    else:
        st.error("Try again! While 'if' checks a condition, it doesn't repeat the action for multiple items.")

st.markdown("---")
st.caption("Knowledge Folder | Module 3: Flow Control & Audit Logic")