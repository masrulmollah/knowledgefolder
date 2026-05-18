import streamlit as st
import numpy as np

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 5: NumPy",
        page_icon="🔢",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("🔢 Module 5: Powering Through Data with NumPy")
st.markdown("""
NumPy is the foundation of data science in Python. It allows us to handle large blocks of numbers (Arrays) and perform calculations on them simultaneously. This is essential for **Risk Modeling, Portfolio Analysis, and Statistical Auditing.**
""")

st.divider()

# --- SECTION 1: ARRAYS VS LISTS ---
st.header("1. The Power of Vectorization")
st.write("In standard Python, doubling 5 numbers requires a loop. In NumPy, you simply multiply the whole 'Array' by 2.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("The Scenario")
    st.write("Imagine we have a list of 5 investment amounts and we want to apply a 10% growth factor.")
    investments = [1000, 2500, 5000, 7500, 10000]
    st.write(f"Original Investments: `{investments}`")

with col2:
    # NumPy logic
    np_investments = np.array(investments)
    growth = np_investments * 1.10
    
    st.subheader("The NumPy Result")
    st.write(f"Grown Portfolio: `{growth.tolist()}`")
    st.code("""
import numpy as np
arr = np.array([1000, 2500, 5000])
result = arr * 1.10 # Vectorized operation
    """, language="python")

st.divider()

# --- SECTION 2: STATISTICAL ANALYSIS ---
st.header("2. Statistical Insights for Audit")
st.write("NumPy provides instant statistical functions to analyze transaction populations for anomalies.")

# Generate some random "Transaction Data"
data_size = st.select_slider("Select Transaction Sample Size", options=[100, 500, 1000, 5000])
# Creating a normal distribution of transaction amounts
np.random.seed(42)
transactions = np.random.normal(loc=500, scale=150, size=data_size)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Mean Spend", f"${np.mean(transactions):,.2f}")
with c2:
    st.metric("Median Spend", f"${np.median(transactions):,.2f}")
with c3:
    st.metric("Std Deviation", f"${np.std(transactions):,.2f}")
with c4:
    st.metric("Total Value", f"${np.sum(transactions):,.0f}")

st.info("💡 **Finance Tip:** A high Standard Deviation relative to the Mean can flag inconsistent spending patterns or potential data entry errors in financial records.")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 5 Quiz")
st.write("Understanding the efficiency of NumPy.")

q_numpy = st.radio(
    "What is the main advantage of using a NumPy Array over a standard Python List for 1 million transactions?",
    [
        "Arrays can store text and numbers together.",
        "Arrays are much faster and use less memory for mathematical operations.",
        "Arrays are easier to print on the screen."
    ]
)

if st.button("Submit Assessment"):
    if "faster" in q_numpy:
        st.balloons()
        st.success("🎯 **Correct!** NumPy is optimized at the hardware level for lightning-fast math.")
    else:
        st.error("❌ Not quite. While lists are flexible, Arrays are specialized for high-performance numerical work.")

st.markdown("---")
st.caption("Knowledge Folder | Module 5: Powering Through Data with NumPy")