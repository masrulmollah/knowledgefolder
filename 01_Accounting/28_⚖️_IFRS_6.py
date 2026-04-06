import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 6: Exploration for and Evaluation of Mineral Resources")
st.write("This standard specifies the financial reporting for the exploration for and evaluation of mineral resources. It allows an entity to develop an accounting policy for exploration and evaluation assets without specifically considering the requirements of IAS 8.")

# --- THE CORE PRINCIPLE ---
st.info("**Scope:** Applies only to expenditures incurred in the exploration and evaluation of mineral resources (e.g., minerals, oil, natural gas) before the technical feasibility and commercial viability of extracting them are demonstrable.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Recognition & Measurement", "Impairment Testing", "Presentation"])

with tab1:
    st.markdown("#### 1. Recognition and Measurement")
    st.write("An entity is permitted to develop its own accounting policy for recognizing exploration and evaluation (E&E) assets.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**E&E Assets Examples**")
        st.markdown("""
        * Acquisition of rights to explore.
        * Topographical and geological studies.
        * Exploratory drilling and trenching.
        * Sampling and activities in relation to evaluating technical feasibility.
        """)
    with col2:
        st.warning("**Measurement at Recognition**")
        st.write("Exploration and evaluation assets shall be measured at **cost** at the time of initial recognition.")

    st.divider()
    st.markdown("**Subsequent Measurement:**")
    st.write("After recognition, an entity shall apply either the **Cost Model** or the **Revaluation Model** (per IAS 16 or IAS 38) to the E&E assets.")

with tab2:
    st.markdown("#### 2. Impairment: The Trigger Points")
    st.write("Unlike other assets under IAS 36, E&E assets are only tested for impairment when facts and circumstances suggest that the carrying amount may exceed the recoverable amount.")

    

    st.error("**Indications of Impairment:**")
    st.markdown("""
    1. The period for which the entity has the right to explore has **expired** or will expire soon and is not expected to be renewed.
    2. Substantive expenditure on further exploration is **neither budgeted nor planned**.
    3. Exploration has not led to the discovery of commercially viable quantities and the entity has decided to **discontinue** activities.
    4. Data exists suggesting that the carrying amount is unlikely to be recovered in full from successful development or by sale.
    """)

with tab3:
    st.markdown("#### 3. Classification and Reclassification")
    
    with st.expander("📂 Classification of E&E Assets"):
        st.write("An entity shall classify E&E assets as **tangible** (e.g., vehicles and drilling rigs) or **intangible** (e.g., drilling rights) according to the nature of the assets acquired.")
        
    st.divider()
    st.warning("**Reclassification Rule**")
    st.write("""
    An E&E asset shall no longer be classified as such when the **technical feasibility and commercial viability** of extracting a mineral resource are demonstrable. 
    \n**Action:** Test for impairment BEFORE reclassifying to PPE (IAS 16) or Intangible Assets (IAS 38).
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 6")