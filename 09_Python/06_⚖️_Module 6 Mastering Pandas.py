import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 6: Pandas",
        page_icon="🐼",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("🐼 Module 6: Mastering Pandas")
st.markdown("""
**Pandas** is the "Gold Standard" for data manipulation. In finance, we use it to merge ERP exports, clean messy bank statements, and perform multi-dimensional analysis that would crash a standard Excel file.
""")

st.divider()

# --- SECTION 1: THE DATAFRAME ---
st.header("1. From Spreadsheet to DataFrame")
st.write("A **DataFrame** is a 2D table with labeled axes (rows and columns).")

# Creating dummy financial data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Cost Center': ['Production', 'Logistics', 'Admin', 'Production', 'Logistics'],
    'Budget': [12000, 8000, 5000, 15000, 7500],
    'Actual': [12500, 7800, 5200, 14000, 9000]
}
df = pd.DataFrame(data)

col1, col2 = st.columns([1, 1])

with col1:
    st.write("### The DataView")
    st.dataframe(df, use_container_width=True)

with col2:
    st.write("### Quick Pandas Code")
    st.code("""
import pandas as pd

# Creating a DataFrame
df = pd.DataFrame(data)

# Calculating a new column instantly
df['Variance'] = df['Actual'] - df['Budget']
    """, language="python")
    
    # Execution
    df['Variance'] = df['Actual'] - df['Budget']
    st.write("### Calculated Result")
    st.dataframe(df[['Cost Center', 'Variance']], use_container_width=True)

st.divider()

# --- SECTION 2: DATA CLEANING SIMULATION ---
st.header("2. The 'Cleaning' Engine")
st.write("Messy data is the enemy of Finance. Pandas can handle missing values and formatting in one click.")

# Create messy data
messy_data = pd.DataFrame({
    'Invoice_ID': [101, 102, 103, 104],
    'Amount': ["$1,200", "$4,500", None, "$3,200"],
    'Status': [' Paid ', 'unpaid', 'PAID', ' Unpaid']
})

st.write("### Original 'Messy' Data (String amounts and inconsistent casing)")
st.table(messy_data)

if st.button("✨ Clean My Data"):
    # 1. Handle Missing Values
    messy_data['Amount'] = messy_data['Amount'].fillna("$0")
    
    # 2. Clean Strings and Convert to Numbers
    messy_data['Amount'] = messy_data['Amount'].str.replace('$', '').str.replace(',', '').astype(float)
    
    # 3. Standardize Casing
    messy_data['Status'] = messy_data['Status'].str.strip().str.upper()
    
    st.success("Data Cleaned Successfully!")
    st.table(messy_data)
    
    st.code("""
# The 'Clean' Script:
df['Amount'] = df['Amount'].str.replace('$', '').astype(float)
df['Status'] = df['Status'].str.strip().str.upper()
df.fillna(0, inplace=True)
    """, language="python")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 6 Quiz")
st.write("Test your understanding of Pandas capabilities.")

q_pandas = st.radio(
    "If you have a CSV file with 1 million rows, which Pandas function would you use to bring it into Python?",
    ["pd.read_excel()", "pd.read_csv()", "pd.to_sql()"]
)

if st.button("Submit Answer"):
    if q_pandas == "pd.read_csv()":
        st.balloons()
        st.success("Correct! `pd.read_csv()` is incredibly fast and memory-efficient for large text-based datasets.")
    else:
        st.error("Not quite. While Excel is common, CSV files are the standard for large-scale data imports.")

st.markdown("---")
st.caption("Knowledge Folder | Module 6: Mastering Pandas")