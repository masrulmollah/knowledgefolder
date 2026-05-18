import streamlit as st

# --- 1. CRITICAL: THIS MUST BE LINE 1 OF EXECUTED STREAMLIT CODE ---
# Note: If this is part of a multipage app, ensure the main entry script 
# hasn't already called a display command before importing this file.
try:
    st.set_page_config(
        page_title="Python Module 1: Setup",
        page_icon="⚖️",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    # This avoids the error if the config was already set by the Homepage
    pass

# --- 2. STYLING ---
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTENT ---
st.title("🐍 Module 1: Python Setup for Finance")
st.info("Goal: Transition from spreadsheet thinking to automated scripting.")

# --- SECTION 1: THE WORKBENCH ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("1. Your Digital Workbench")
        st.write("""
        For a finance professional, stability is everything. We use:
        * **Anaconda:** To manage libraries like Pandas (Data Manipulation) and Openpyxl (Excel interface).
        * **VS Code:** The editor where you will write your logic.
        """)
    with col2:
        st.write("### Quick Setup Stats")
        st.metric(label="Typical Install Time", value="15 Mins")
        st.metric(label="Disk Space Needed", value="~3 GB")

st.divider()

# --- SECTION 2: INTERACTIVE SIMULATION ---
st.header("💻 Coding Simulation: Financial Variables")
st.write("In Python, we don't need 'Cells'. We use **Variables** to store account data.")

# Input Area
c1, c2, c3 = st.columns(3)
with c1:
    acc_name = st.text_input("Account Name", value="Accounts Receivable")
with c2:
    acc_code = st.text_input("GL Code (Int)", value="1200")
with c3:
    acc_balance = st.number_input("Balance (Float)", value=45000.75)

# Code Display
st.subheader("Generated Python Logic")
st.code(f"""
# Variables assignment
account = "{acc_name}"
gl_code = {acc_code}
balance = {acc_balance}

# Check data types
print(type(account))  # <class 'str'>
print(type(gl_code))  # <class 'int'>
print(type(balance))  # <class 'float'>
""", language='python')

if st.button("Execute Simulation"):
    st.success(f"✅ Variable '{acc_name}' stored as Float with value: ${acc_balance:,.2f}")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Knowledge Check")
st.write("Identify the correct data type for a 'Trial Balance' amount.")

choice = st.radio(
    "Which Python data type is most appropriate for $1,250.50?",
    ["String (str)", "Integer (int)", "Floating Point (float)"],
    index=0
)

if st.button("Check Answer"):
    if "float" in choice.lower():
        st.balloons()
        st.success("Correct! 'Floats' are used for numbers with decimal points.")
    else:
        st.error("Try again! Integers are for whole numbers, and Strings are for text.")

st.markdown("---")
st.caption("Knowledge Folder | Finance & Accounts Professional Refresher")