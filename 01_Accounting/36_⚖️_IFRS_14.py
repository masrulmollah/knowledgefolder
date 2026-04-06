import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 14: Regulatory Deferral Accounts")
st.write("This standard permits an entity which is a first-time adopter of IFRS to continue to account, with some limited changes, for 'regulatory deferral account balances' in accordance with its previous GAAP.")

# --- THE CORE OBJECTIVE ---
st.info("**Objective:** To allow entities that are rate-regulated to adopt IFRS without making major changes to their accounting for regulatory deferral accounts until a more comprehensive standard is developed.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Scope & Eligibility", "Recognition & Measurement", "Presentation"])

with tab1:
    st.markdown("#### 1. Scope and Eligibility")
    st.write("IFRS 14 is NOT available to all entities. It is strictly limited to those that:")
    
    st.success("""
    1. Conduct **rate-regulated activities** (where a regulator sets prices for goods/services).
    2. Recognized **regulatory deferral account balances** in their financial statements under previous GAAP.
    3. Are **first-time adopters** of IFRS.
    """)
    
    st.divider()
    st.markdown("**What is a Regulatory Deferral Account Balance?**")
    st.write("A balance that would not otherwise be recognized as an asset or liability under other IFRS standards, but which is deferred because it is expected to be recovered from, or refunded to, customers through future rate adjustments.")

with tab2:
    st.markdown("#### 2. Recognition and Measurement")
    st.write("IFRS 14 is a 'grandfathering' standard, meaning it allows the continuation of previous accounting policies with very few restrictions.")

    st.warning("**Policy Continuity**")
    st.markdown("""
    * An entity shall apply its **previous GAAP** accounting policies for the recognition, measurement, and impairment of regulatory deferral account balances.
    * Changes to these policies are only permitted if they make the financial statements **more relevant** and no less reliable.
    """)

    with st.expander("📝 Interaction with other IFRSs"):
        st.write("""
        Regulatory deferral account balances are excluded from the scope of several other standards (like IAS 36 for impairment), but IFRS 14 requires specific 'impairment-like' assessments based on the probability of recovery through future rates.
        """)

with tab3:
    st.markdown("#### 3. Presentation Requirements")
    st.write("Because these balances are unique, IFRS 14 requires them to be presented separately from all other assets, liabilities, income, and expenses.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("**Statement of Financial Position**")
        st.markdown("""
        * **Total Regulatory Deferral Debit Balances:** Presented as a separate line item after all other assets.
        * **Total Regulatory Deferral Credit Balances:** Presented as a separate line item after all other liabilities.
        """)
    with col2:
        st.error("**Statement of P&L and OCI**")
        st.markdown("""
        * The net movement in these balances must be presented as a **separate line item** in the P&L and OCI, below all other items but before the final profit/loss.
        """)

    st.divider()
    st.markdown("#### Disclosure Requirements")
    st.write("Entities must disclose the **nature of the rate regulation** and the basis on which the carrying amounts of the balances are expected to be recovered or reversed.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 14")