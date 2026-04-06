import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 16: Leases")
st.write("This standard sets out the principles for the recognition, measurement, presentation, and disclosure of leases. The objective is to ensure that lessees and lessors provide relevant information in a manner that faithfully represents those transactions.")

# --- THE CORE PRINCIPLE ---
st.info("**Core Rule:** For lessees, IFRS 16 removes the classification of leases as either operating leases or finance leases. Instead, it introduces a single lessee accounting model where a lessee recognizes a Right-of-Use (ROU) asset and a Lease Liability.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The Lessee Model", "Identifying a Lease", "Lessor Accounting"])

with tab1:
    st.markdown("#### 1. The Lessee Accounting Model")
    st.write("At the commencement date, a lessee shall recognize:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Right-of-Use (ROU) Asset**")
        st.markdown("""
        * **Initial:** Measured at cost (Lease liability + initial direct costs + prepayments).
        * **Subsequent:** Depreciated over the shorter of the lease term or useful life.
        """)
    with col2:
        st.error("**Lease Liability**")
        st.markdown("""
        * **Initial:** Present value of lease payments that are not paid at that date.
        * **Subsequent:** Increased by interest expense and reduced by lease payments made.
        """)

    

    with st.expander("📝 Exemptions (Optional)"):
        st.write("A lessee may elect not to apply the requirements above to:")
        st.markdown("""
        1. **Short-term leases:** Leases with a term of 12 months or less.
        2. **Low-value assets:** Leases where the underlying asset has a low value when new (e.g., personal computers, office furniture).
        * *Treatment:* Recognize lease payments as an expense on a straight-line basis.
        """)

with tab2:
    st.markdown("#### 2. Identifying a Lease")
    st.write("A contract is, or contains, a lease if the contract conveys the **right to control the use of an identified asset** for a period of time in exchange for consideration.")

    st.warning("**The Control Test**")
    st.markdown("""
    1. **Identified Asset:** Is there a specific asset (e.g., a specific warehouse bay)?
    2. **Economic Benefits:** Does the customer have the right to obtain substantially all economic benefits from use?
    3. **Direction of Use:** Does the customer have the right to direct how and for what purpose the asset is used?
    """)

    

with tab3:
    st.markdown("#### 3. Lessor Accounting")
    st.write("Unlike lessees, lessor accounting remains substantially unchanged from the old standard (IAS 17).")
    
    st.info("**Two Classifications for Lessors:**")
    st.markdown("""
    * **Finance Lease:** A lease that transfers substantially all the risks and rewards incidental to ownership of an underlying asset.
    * **Operating Lease:** A lease that does not transfer substantially all the risks and rewards incidental to ownership.
    """)

    st.divider()
    st.markdown("#### Presentation in Financial Statements")
    st.markdown("""
    * **Statement of Financial Position:** ROU assets and Lease liabilities must be presented separately (or disclosed in the notes).
    * **Statement of P&L:** Depreciation (on ROU) and Interest (on Liability) are presented separately.
    * **Statement of Cash Flows:** Principal payments are Financing activities; interest can be Operating or Financing.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 16")