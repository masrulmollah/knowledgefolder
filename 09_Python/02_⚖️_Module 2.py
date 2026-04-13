import streamlit as st

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 2: Financial Logic",
        page_icon="📈",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. STYLING ---
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stMetric { border: 1px solid #e6e9ef; padding: 10px; border-radius: 5px; background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER ---
st.title("📈 Module 2: Foundations & Financial Logic")
st.markdown("""
In this module, we transition from simple variables to **Financial Logic**. 
We will explore how Python handles mathematical formulas and how to organize complex accounting data using Lists and Dictionaries.
""")

st.divider()

# --- SECTION 1: CALCULATION SIMULATION ---
st.header("🧮 Calculation Simulation: CAGR")
st.write("The Compound Annual Growth Rate (CAGR) is a perfect example of Python's mathematical precision.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Parameters")
    beg_val = st.number_input("Beginning Value (e.g., Revenue 2020)", value=100000.0, step=1000.0)
    end_val = st.number_input("Ending Value (e.g., Revenue 2025)", value=161051.0, step=1000.0)
    periods = st.slider("Number of Years", 1, 10, 5)

with col2:
    # Logic: ((Ending/Beginning)**(1/n)) - 1
    cagr_result = ((end_val / beg_val) ** (1 / periods)) - 1
    
    st.subheader("Resulting Metric")
    st.metric(label="Calculated CAGR", value=f"{cagr_result:.2%}")
    
    st.write("### The Python Formula")
    st.code(f"cagr = (({end_val} / {beg_val}) ** (1 / {periods})) - 1", language="python")

st.divider()

# --- SECTION 2: DATA STRUCTURES ---
st.header("📂 Organizing Accounts: Lists & Dictionaries")
st.write("In Excel, you use rows and columns. In Python, we use **Lists** (for sequences) and **Dictionaries** (for mappings).")

tab1, tab2 = st.tabs(["Lists (Sequence)", "Dictionaries (Mappings)"])

with tab1:
    st.subheader("Python Lists")
    st.write("Useful for time series like months or quarters.")
    st.code("""
# A list of months
quarters = ["Q1", "Q2", "Q3", "Q4"]
print(quarters[0]) # Output: Q1
    """, language="python")
    st.info("💡 Note: Python is **Zero-Indexed**. The first item is always position `0`.")

with tab2:
    st.subheader("Python Dictionaries")
    st.write("Perfect for Chart of Accounts (COA) or mapping Cost Centers to Names.")
    st.code("""
# Key-Value Pairs
coa_mapping = {
    "1001": "Cash in Hand",
    "1002": "Cash at Bank",
    "2001": "Accounts Payable"
}
print(coa_mapping["1001"]) # Output: Cash in Hand
    """, language="python")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 2 Quiz")
st.write("Test your understanding of Python data structures.")

q_structure = st.radio(
    "If you want to map a 'Department ID' to a 'Department Name', which structure is best?",
    ["A List", "A Dictionary", "A Float"]
)

if st.button("Check Logic"):
    if q_structure == "A Dictionary":
        st.balloons()
        st.success("Correct! Dictionaries allow you to use a 'Key' (ID) to find a 'Value' (Name).")
    else:
        st.error("Try again! Remember, Lists are for ordering items, while Dictionaries are for mapping them.")

st.markdown("---")
st.caption("Knowledge Folder | Module 2: Foundations & Financial Logic")