import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 1: First-time Adoption of IFRS")
st.write("This standard sets out the procedures that an entity must follow when it adopts IFRS for the first time as the basis for preparing its general-purpose financial statements.")

# --- THE CORE OBJECTIVE ---
st.info("**Objective:** To ensure that an entity’s first IFRS financial statements provide a suitable starting point for accounting under IFRS and can be generated at a cost that does not exceed the benefits.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The Opening Balance Sheet", "Mandatory Exceptions", "Optional Exemptions"])

with tab1:
    st.markdown("#### 1. The Opening IFRS Statement of Financial Position")
    st.write("An entity shall prepare and present an **opening IFRS Statement of Financial Position** at the **date of transition** to IFRS.")
    
    st.success("**Key Steps for Transition:**")
    st.markdown("""
    1. **Recognize** all assets and liabilities required by IFRS.
    2. **Derecognize** items as assets or liabilities if IFRS does not permit such recognition.
    3. **Reclassify** items that it recognized under previous GAAP as one type of asset, liability, or component of equity, but are a different type under IFRS.
    4. **Measure** all recognized assets and liabilities according to IFRS.
    """)
    
    st.warning("**Accounting Policy Note:** An entity must use the same accounting policies in its opening IFRS SFP and throughout all periods presented in its first IFRS financial statements.")

with tab2:
    st.markdown("#### 2. Mandatory Exceptions")
    st.write("IFRS 1 prohibits retrospective application of some aspects of IFRS. These mandatory exceptions include:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("**Estimates**")
        st.write("Estimates at the date of transition to IFRS shall be consistent with estimates made for the same date under previous GAAP (unless there is objective evidence of error).")
    with col2:
        st.error("**Derecognition**")
        st.write("Financial assets and liabilities derecognized under previous GAAP before the transition date are not re-recognized under IFRS.")

    with st.expander("🔍 Other Mandatory Exceptions"):
        st.markdown("""
        * **Hedge Accounting:** Only those hedging relationships that qualified for hedge accounting under previous GAAP shall be reflected as hedges in IFRS.
        * **Non-controlling Interests:** Certain requirements of IFRS 10 are applied prospectively.
        * **Classification and Measurement of Financial Assets:** Assessment is made based on facts and circumstances existing at the date of transition.
        """)

with tab3:
    st.markdown("#### 3. Optional Exemptions")
    st.write("To reduce the cost of transition, IFRS 1 provides several optional exemptions that an entity may elect to use.")
    
    st.info("**Common Optional Exemptions:**")
    st.markdown("""
    * **Deemed Cost:** An entity may elect to measure an item of PPE at its fair value at the date of transition and use that fair value as its 'deemed cost'.
    * **Business Combinations:** An entity may elect not to apply IFRS 3 retrospectively to past business combinations.
    * **Leases:** A first-time adopter may assess whether a contract existing at the transition date contains a lease based on facts at that date.
    * **Cumulative Translation Differences:** May be deemed to be zero at the date of transition.
    """)

    st.divider()
    st.markdown("#### Required Reconciliations")
    st.write("An entity's first IFRS financial statements shall include reconciliations of:")
    st.markdown("- **Equity** reported under previous GAAP to its equity under IFRS.")
    st.markdown("- **Total Comprehensive Income** under previous GAAP to its TCI under IFRS.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 1")