import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 1: Presentation of Financial Statements")
st.write("This standard sets out the overall requirements for the presentation of financial statements, guidelines for their structure, and minimum requirements for their content.")

# --- KEY COMPONENTS VISUAL ---
st.info("**Objective:** To ensure comparability both with the entity's financial statements of previous periods and with the financial statements of other entities.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["General Features", "Financial Statements", "Current vs Non-Current"])

with tab1:
    st.markdown("#### General Features of Financial Statements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Core Principles**")
        st.markdown("""
        * **Fair Presentation:** Compliance with IFRS.
        * **Going Concern:** Entity will continue for the foreseeable future.
        * **Accrual Basis:** Transactions recognized when they occur.
        * **Materiality:** Omissions could influence user decisions.
        """)
        
    with col2:
        st.warning("**Reporting Rules**")
        st.markdown("""
        * **Consistency:** Presentation kept same period to period.
        * **Offsetting:** Assets/Liabilities generally not offset.
        * **Frequency:** At least annually.
        * **Comparative Info:** Previous period data required.
        """)

with tab2:
    st.markdown("#### Complete Set of Financial Statements")
    st.write("A complete set includes:")
    
    with st.expander("📝 1. Statement of Financial Position (Balance Sheet)"):
        st.write("Shows assets, liabilities, and equity at a specific point in time.")
        
    with st.expander("📈 2. Statement of Profit or Loss & Other Comprehensive Income"):
        st.write("Shows financial performance over a period. OCI includes items not recognized in P&L (e.g., revaluation surpluses).")
        
    with st.expander("💰 3. Statement of Changes in Equity"):
        st.write("Reconciles the opening and closing amounts of equity components.")
        
    with st.expander("💧 4. Statement of Cash Flows"):
        st.write("Analyzes cash movements via Operating, Investing, and Financing activities.")
        
    with st.expander("📖 5. Notes to the Accounts"):
        st.write("Significant accounting policies and explanatory information.")

with tab3:
    st.markdown("#### Classification of Assets & Liabilities")
    
    st.write("An entity must present current and non-current items as separate classifications.")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.error("**Current Criteria**")
        st.markdown("""
        * Expected to be realized/settled within **12 months**.
        * Held primarily for **trading**.
        * Expected to be realized in the **normal operating cycle**.
        * Cash or cash equivalents.
        """)

    with col_b:
        st.info("**Non-Current Criteria**")
        st.write("All other assets and liabilities that do not meet the 'Current' definition are classified as Non-Current (e.g., PP&E, Intangibles, Long-term loans).")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 1")