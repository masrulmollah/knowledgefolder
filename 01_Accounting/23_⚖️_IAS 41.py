import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 41: Agriculture")
st.write("This standard prescribes the accounting treatment, financial statement presentation, and disclosures related to agricultural activity.")

# --- THE KEY CONCEPTS ---
st.info("**Agricultural Activity:** The management by an entity of the biological transformation and harvest of biological assets for sale or for conversion into agricultural produce.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Biological Assets", "Recognition & Measurement", "Government Grants"])

with tab1:
    st.markdown("#### 1. Scope and Definitions")
    st.write("IAS 41 applies to the following when they relate to agricultural activity:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**Biological Assets**")
        st.write("Living animals or plants (e.g., Sheep, Dairy Cattle, Trees in a plantation).")
    with col2:
        st.warning("**Agricultural Produce**")
        st.write("The harvested product of the entity's biological assets (e.g., Wool, Milk, Felled Trees).")
    with col3:
        st.error("**Exclusions**")
        st.write("Land (IAS 16/40), Bearer Plants (IAS 16), and intangible assets (IAS 38).")

    

    st.markdown("#### The 'Bearer Plant' Exception")
    st.write("Plants used to grow produce for more than one period (e.g., tea bushes, fruit trees) are accounted for under **IAS 16** (PPE) at cost, but the produce growing *on* them remains under **IAS 41**.")

with tab2:
    st.markdown("#### 2. Recognition and Measurement")
    st.write("An entity recognizes a biological asset or agricultural produce when it controls the asset, future benefits are probable, and the value is measurable.")
    
    st.info("**The Fair Value Rule**")
    st.write("Biological assets are measured on initial recognition and at each reporting date at **Fair Value Less Costs to Sell (FVLCTS)**.")
    
    st.warning("**Gains and Losses**")
    st.write("Gains or losses arising on initial recognition and from changes in FVLCTS are recognized in **Profit or Loss** for the period in which they arise.")
    
    with st.expander("📝 The Cost Exception"):
        st.write("There is a rebuttable presumption that fair value can be measured reliably. Only on initial recognition, if market-determined prices are not available and alternative estimates are unreliable, the asset is measured at **Cost less Depreciation/Impairment**.")

with tab3:
    st.markdown("#### 3. Government Grants & Disclosure")
    
    st.markdown("**Government Grants (Agriculture)**")
    st.write("""
    * **Unconditional Grants:** Recognized in profit or loss when the grant becomes receivable.
    * **Conditional Grants:** Recognized in profit or loss only when the conditions are met.
    """)
    
    st.divider()
    st.markdown("#### Required Disclosures")
    st.markdown("""
    1. **Aggregate Gain/Loss** arising during the current period on initial recognition and from changes in FVLCTS.
    2. **Description** of each group of biological assets (e.g., distinguishing between consumable and bearer assets).
    3. **Reconciliation** of changes in the carrying amount of biological assets between the beginning and the end of the period.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 41")