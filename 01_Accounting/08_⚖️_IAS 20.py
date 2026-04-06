import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 20: Accounting for Government Grants")
st.write("This standard prescribes the accounting treatment and disclosure of government grants and other forms of government assistance.")

# --- THE CAPITAL VS INCOME DEBATE ---
st.info("**Core Principle:** Government grants shall be recognized in profit or loss on a systematic basis over the periods in which the entity recognizes as expenses the related costs for which the grants are intended to compensate.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Recognition & Types", "Accounting Treatment", "Repayment & Disclosure"])

with tab1:
    st.markdown("#### 1. Recognition Criteria")
    st.write("Government grants shall not be recognized until there is reasonable assurance that:")
    st.markdown("""
    1. The entity will **comply with the conditions** attaching to them.
    2. The grants will be **received**.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Grants Related to Assets**")
        st.write("Government grants whose primary condition is that an entity should purchase, construct, or otherwise acquire long-term assets.")
        
    with col2:
        st.success("**Grants Related to Income**")
        st.write("Government grants other than those related to assets (e.g., wage subsidies or export incentives).")

with tab2:
    st.markdown("#### 2. Presentation in Financial Statements")
    st.write("IAS 20 allows two alternative methods for presenting grants.")

    

    c1, c2 = st.columns(2)
    
    with c1:
        st.warning("**Method A: Deferred Income**")
        st.write("The grant is recognized as deferred income and released to profit or loss over the useful life of the asset.")
        st.caption("Common for asset-related grants.")

    with c2:
        st.warning("**Method B: Deduction from Asset**")
        st.write("The grant is deducted from the carrying amount of the asset to arrive at the net cost. Depreciation is then calculated on the net amount.")

    st.divider()
    st.markdown("**Grants Related to Income**")
    st.write("These can be presented as 'Other Income' or deducted from the related expense in the Statement of Profit or Loss.")

with tab3:
    st.markdown("#### 3. Repayment of Grants")
    st.error("**Accounting for Repayments**")
    st.write("A government grant that becomes repayable shall be accounted for as a **change in accounting estimate** (Prospective).")
    st.markdown("""
    * **If deducted from asset:** Increase the carrying amount of the asset.
    * **If deferred income:** Apply first against any unamortized deferred credit.
    """)
    
    st.divider()
    st.markdown("#### 4. Required Disclosures")
    st.markdown("""
    1. The **accounting policy** adopted for government grants.
    2. The **nature and extent** of government grants recognized.
    3. An indication of **other forms of assistance** (e.g., free technical advice, guarantees).
    4. Unfulfilled conditions and other contingencies.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 20")