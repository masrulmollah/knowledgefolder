import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 18: Presentation and Disclosure in Financial Statements")
st.write("Issued in April 2024 to replace IAS 1, this standard improves how companies communicate their financial performance, focusing on the Statement of Profit or Loss.")

# --- THE CORE OBJECTIVE ---
st.info("**Objective:** To reduce diversity in how companies report 'Operating Profit' and to provide a more consistent structure for the Income Statement.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The 3 New Categories", "MPMs (Non-GAAP)", "Aggregation Logic"])

with tab1:
    st.markdown("#### 1. The Structured Income Statement")
    st.write("IFRS 18 requires all income and expenses to be classified into **three distinct categories**:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**Operating**")
        st.write("The default category. Includes all income/expenses not in other categories. It now provides a mandatory **Operating Profit** subtotal.")
    with col2:
        st.warning("**Investing**")
        st.write("Returns from investments in associates, joint ventures, and un-consolidated subsidiaries (e.g., share of profit).")
    with col3:
        st.error("**Financing**")
        st.write("Income/expenses from cash/cash equivalents and the raising of finance (e.g., interest on bank loans/leases).")

    

    st.divider()
    st.markdown("#### New Mandatory Subtotals")
    st.write("Companies must now report:")
    st.markdown("1. **Operating Profit**")
    st.markdown("2. **Operating Profit and income/expenses from integral associates and JVs**")
    st.markdown("3. **Profit before financing and income tax**")

with tab2:
    st.markdown("#### 2. Management Performance Measures (MPMs)")
    st.write("Many companies use 'Non-GAAP' measures like 'Adjusted EBITDA'. IFRS 18 brings these into the **audited** financial statements.")

    st.error("**The MPM Disclosure Rule**")
    st.write("If management uses a subtotal of income/expenses that is not defined by IFRS to communicate performance, they must:")
    st.markdown("""
    * Explain **why** the measure provides useful information.
    * Explain **how** it is calculated.
    * Provide a **reconciliation** between the MPM and the most directly comparable IFRS subtotal.
    * Disclose the **income tax effect** and NCI effect for each adjustment.
    """)
    
    with st.expander("📝 Why this matters?"):
        st.write("This stops companies from 'cherry-picking' adjustments to make profits look better without transparently explaining the math in the notes.")

with tab3:
    st.markdown("#### 3. Grouping of Information")
    st.write("IFRS 18 provides clearer guidance on whether information should be in the primary financial statements or hidden in the notes.")
    
    st.info("**Aggregation and Disaggregation**")
    st.markdown("""
    * Items must be grouped based on **shared characteristics**.
    * If an item is material, it **cannot** be obscured by aggregating it with dissimilar items.
    * Use of the label **'Other'** is restricted; if a large amount is labeled 'Other', the entity must disclose more detail about what is inside that bucket.
    """)

    st.divider()
    st.markdown("#### Effective Date")
    st.warning("IFRS 18 is effective for annual reporting periods beginning on or after **1 January 2027**, with early application permitted. For your 2026 reporting, you should be preparing for this transition.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 18 (Replaces IAS 1)")