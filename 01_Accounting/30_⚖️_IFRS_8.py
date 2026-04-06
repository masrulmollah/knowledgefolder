import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 8: Operating Segments")
st.write("This standard requires an entity to report financial and descriptive information about its reportable segments, which are components of an entity about which separate financial information is available.")

# --- THE CORE PRINCIPLE ---
st.info("**The Management Approach:** Segments are identified on the basis of internal reports that are regularly reviewed by the entity's Chief Operating Decision Maker (CODM) to allocate resources and assess performance.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Identifying Segments", "Aggregation & Thresholds", "Disclosures"])

with tab1:
    st.markdown("#### 1. Definition of an Operating Segment")
    st.write("An operating segment is a component of an entity:")
    
    st.success("""
    1. That engages in **business activities** from which it may earn revenues and incur expenses.
    2. Whose **operating results** are regularly reviewed by the CODM.
    3. For which **discrete financial information** is available.
    """)
    
    st.divider()
    st.markdown("**Who is the CODM?**")
    st.write("It is not necessarily a single person; it is a **function** (e.g., the CEO or a Board of Directors) that allocates resources to and assesses the performance of the segments.")

with tab2:
    st.markdown("#### 2. Quantitative Thresholds")
    st.write("An entity must report separate information about an operating segment that meets **ANY** of the following 10% thresholds:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.error("**Revenue**")
        st.write("Reported revenue (internal & external) is **10% or more** of the combined revenue of all operating segments.")
    with col2:
        st.error("**Profit or Loss**")
        st.write("The absolute amount of its profit/loss is **10% or more** of the greater of combined profit or combined loss.")
    with col3:
        st.error("**Assets**")
        st.write("Its assets are **10% or more** of the combined assets of all operating segments.")

    

    with st.expander("📝 The 75% Rule"):
        st.write("If the total external revenue reported by operating segments constitutes less than **75%** of the entity's total revenue, additional operating segments must be identified as reportable segments until at least 75% of the entity's revenue is included.")

with tab3:
    st.markdown("#### 3. Required Disclosures")
    st.write("For each reportable segment, the entity must disclose:")
    
    st.markdown("""
    * **General Information:** Factors used to identify segments and types of products/services.
    * **Profit or Loss:** Measure of profit/loss and specific income/expense items (e.g., interest, depreciation, tax).
    * **Assets and Liabilities:** Only if these are regularly provided to the CODM.
    * **Reconciliations:** Total segment revenues/profits must be reconciled to the entity's consolidated financial statements.
    """)

    st.divider()
    st.warning("**Entity-Wide Disclosures**")
    st.markdown("""
    Even if an entity has only one reportable segment, it must disclose:
    1. Information about **products and services**.
    2. Information about **geographical areas** (Domestic vs. Foreign).
    3. Information about **major customers** (if any single customer provides 10% or more of total revenue).
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 8")