import streamlit as st
import pandas as pd

# --- HEADER ---
st.title("📚 IFRS & IAS Syllabus Overview")
st.write("Welcome to the 2026 Accounting Standards Navigator. Use the categories below to explore the full syllabus.")

# --- DATASET ---
data = {
    "Category": [
        "Foundation", "Foundation", "Assets", "Assets", 
        "Revenue", "Liabilities", "Groups", "Specialized"
    ],
    "Standard": [
        "IAS 1 / IFRS 18", "IAS 7", "IAS 16", "IFRS 16", 
        "IFRS 15", "IAS 37", "IFRS 10", "IFRS 9"
    ],
    "Title": [
        "Presentation of Financial Statements", "Statement of Cash Flows",
        "Property, Plant and Equipment", "Leases",
        "Revenue from Contracts", "Provisions & Contingencies",
        "Consolidated Financial Statements", "Financial Instruments"
    ]
}
df = pd.DataFrame(data)

# --- SEARCH BAR ---
search = st.text_input("🔍 Search Syllabus", placeholder="e.g. IAS 16 or Leases")

if search:
    # Filter the dataframe based on search
    filtered_df = df[df.apply(lambda row: search.lower() in row.astype(str).str.lower().values, axis=1)]
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
else:
    # --- CATEGORIZED VIEW ---
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("🏗️ 1. Foundation & Framework", expanded=True):
            st.write("**IAS 1 / IFRS 18:** Presentation")
            st.write("**IAS 7:** Cash Flows")
            st.write("**IAS 8:** Accounting Policies")
        
        with st.expander("📦 2. Assets & Leases", expanded=True):
            st.write("**IAS 2:** Inventories")
            st.write("**IAS 16:** PPE")
            st.write("**IFRS 16:** Leases")

    with col2:
        with st.expander("💰 3. Revenue & Tax", expanded=True):
            st.write("**IFRS 15:** Revenue Recognition")
            st.write("**IAS 12:** Income Taxes")
            st.write("**IAS 19:** Employee Benefits")

        with st.expander("🏢 4. Group Accounting", expanded=True):
            st.write("**IFRS 3:** Business Combinations")
            st.write("**IFRS 10:** Consolidation")
            st.write("**IAS 28:** Associates")

# --- FOOTER ---
st.divider()
st.caption("Strategic Finance Library | Version 2026.1")