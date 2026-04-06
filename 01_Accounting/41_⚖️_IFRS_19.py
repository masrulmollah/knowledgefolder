import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 19: Subsidiaries without Public Accountability: Disclosures")
st.write("Issued in May 2024, this standard permits eligible subsidiaries to apply IFRS Accounting Standards with reduced disclosure requirements in their consolidated, separate, or individual financial statements.")

# --- THE CORE OBJECTIVE ---
st.info("**Objective:** To reduce the costs of preparing financial statements for subsidiaries that do not have public accountability, while still providing high-quality information to users.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Eligibility Criteria", "The 'Reduced' Logic", "Practical Benefits"])

with tab1:
    st.markdown("#### 1. Who Can Use IFRS 19?")
    st.write("An entity is eligible to apply IFRS 19 only if it meets **ALL** of the following criteria at the end of the reporting period:")
    
    st.success("**Criterion 1: It is a Subsidiary**")
    st.write("It must be an entity that is controlled by a parent that prepares consolidated financial statements available for public use that comply with IFRS.")
    
    st.warning("**Criterion 2: No Public Accountability**")
    st.write("It must not have its debt or equity instruments traded in a public market and must not hold assets in a fiduciary capacity for a broad group of outsiders (like a bank).")
    
    st.error("**Criterion 3: Use of Full IFRS**")
    st.write("The subsidiary must apply the recognition and measurement requirements of all other IFRS Accounting Standards (e.g., IFRS 9, IFRS 15, IFRS 16).")

    

with tab2:
    st.markdown("#### 2. The Disclosure Framework")
    st.write("IFRS 19 acts as a 'pick and choose' list. Instead of looking for disclosure requirements in each individual standard (like IFRS 7 or IAS 19), the subsidiary looks directly at IFRS 19.")

    st.markdown("**How it works:**")
    st.markdown("""
    * **Recognition & Measurement:** Use Full IFRS (No shortcuts here).
    * **Disclosures:** Use only the reduced set specified in IFRS 19.
    * **Omitted Disclosures:** Many complex disclosures from standards like **IFRS 7** (Financial Instruments) and **IAS 19** (Employee Benefits) are significantly simplified or removed.
    """)
    
    with st.expander("📝 Interaction with other Standards"):
        st.write("""
        If a subsidiary applies IFRS 19, it is exempt from the disclosure requirements in other IFRS Accounting Standards, except for a few specific instances where IFRS 19 explicitly refers back to them.
        """)

with tab3:
    st.markdown("#### 3. Strategic Benefits for Multinational Groups")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Efficiency**")
        st.write("Reduces the 'disclosure gap' between the subsidiary's local reporting and the data needed for the parent's consolidation.")
    with col2:
        st.info("**Cost Savings**")
        st.write("Lower audit and preparation costs by removing dozens of pages of complex notes that are often irrelevant to local lenders or tax authorities.")

    st.divider()
    st.markdown("#### Effective Date")
    st.warning("IFRS 19 is effective for annual reporting periods beginning on or after **1 January 2027**, with early application permitted. This aligns perfectly with the rollout of IFRS 18.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 19")