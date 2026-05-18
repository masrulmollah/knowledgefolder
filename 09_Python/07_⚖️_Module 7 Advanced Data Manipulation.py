import streamlit as st
import pandas as pd

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 7: Advanced Pandas",
        page_icon="🧬",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("🧬 Module 7: Advanced Data Manipulation")
st.markdown("""
In this module, we tackle complex data relationships. You will learn how to join separate tables together and summarize millions of transactions into meaningful management reports using **Merge** and **GroupBy**.
""")

st.divider()

# --- SECTION 1: THE VLOOKUP KILLER (MERGING) ---
st.header("1. Merging Datasets (The VLOOKUP Killer)")
st.write("In Finance, we often have one table with 'Transactions' and another with 'Account Names'. Python's `merge` is faster and less prone to errors than VLOOKUP.")

# Creating two sample dataframes
df_transactions = pd.DataFrame({
    'GL_Code': ['101', '102', '101', '103', '102'],
    'Amount': [1500, 2200, 300, 4500, 1100]
})

df_mapping = pd.DataFrame({
    'GL_Code': ['101', '102', '103'],
    'Account_Name': ['Cash at Bank', 'Accounts Receivable', 'Fixed Assets']
})

col1, col2, col3 = st.columns([1, 1, 1.5])

with col1:
    st.write("**Table A: Transactions**")
    st.dataframe(df_transactions, hide_index=True)

with col2:
    st.write("**Table B: Mapping**")
    st.dataframe(df_mapping, hide_index=True)

with col3:
    # Execution of Merge
    df_merged = pd.merge(df_transactions, df_mapping, on='GL_Code', how='left')
    st.write("**Result: Merged Report**")
    st.dataframe(df_merged, hide_index=True)
    
st.code("""
# Merging Table A and Table B on 'GL_Code'
merged_report = pd.merge(df_transactions, df_mapping, on='GL_Code', how='left')
""", language="python")

st.divider()

# --- SECTION 2: PIVOT TABLES & GROUPBY ---
st.header("2. Grouping & Pivoting")
st.write("Summary reports are the backbone of financial analysis. `groupby` allows you to aggregate data by department, region, or category instantly.")

# Sample Data for Grouping
data_summary = pd.DataFrame({
    'Region': ['North', 'South', 'North', 'East', 'South', 'North'],
    'Department': ['Sales', 'HR', 'Sales', 'IT', 'IT', 'Sales'],
    'Expense': [12000, 8500, 15000, 22000, 7000, 9000]
})

st.write("### Raw Expense Data")
st.dataframe(data_summary, use_container_width=True)

# Interactive Pivot Selection
agg_func = st.selectbox("Select Aggregation Method", ["Sum", "Mean", "Count"])

if agg_func == "Sum":
    summary_result = data_summary.groupby('Region')['Expense'].sum().reset_index()
elif agg_func == "Mean":
    summary_result = data_summary.groupby('Region')['Expense'].mean().reset_index()
else:
    summary_result = data_summary.groupby('Region')['Expense'].count().reset_index()

st.write(f"### Expense Summary by Region ({agg_func})")
st.table(summary_result)

st.code(f"""
# Python logic for this summary:
summary = data_summary.groupby('Region')['Expense'].{agg_func.lower()}()
""", language="python")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 7 Quiz")
st.write("Refine your understanding of data consolidation.")

q_merge = st.radio(
    "If you want to keep all records from your Transaction list even if they don't have a match in the Mapping table, which 'how' parameter should you use in a merge?",
    ["how='inner'", "how='left'", "how='right'"]
)

if st.button("Check Accuracy"):
    if q_merge == "how='left'":
        st.balloons()
        st.success("Correct! A 'Left Join' keeps every row from your primary (left) table and adds matching data where available.")
    else:
        st.error("Not quite. 'Inner' only keeps matches. To ensure you don't lose transactions, use 'Left'.")

st.markdown("---")
st.caption("Knowledge Folder | Module 7: Advanced Data Manipulation")