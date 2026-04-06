import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 16: Property, Plant and Equipment")
st.write("This standard prescribes the accounting treatment for property, plant and equipment so that users of the financial statements can discern information about an entity's investment in its PPE.")

# --- CORE DEFINITION ---
st.info("**Definition:** PPE are tangible items that are held for use in the production or supply of goods or services, for rental to others, or for administrative purposes; and are expected to be used during more than one period.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["Recognition & Initial Cost", "Subsequent Measurement", "Depreciation", "Derecognition"])

with tab1:
    st.markdown("#### 1. Recognition Criteria")
    st.write("An item of PPE shall be recognized as an asset if, and only if:")
    st.markdown("""
    1. It is probable that **future economic benefits** associated with the item will flow to the entity.
    2. The **cost** of the item can be measured reliably.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Elements of Cost**")
        st.markdown("""
        * **Purchase Price:** Including import duties and non-refundable taxes.
        * **Directly Attributable Costs:** Site preparation, delivery, installation, assembly, and professional fees.
        * **Dismantling Costs:** Initial estimate of removing the asset and restoring the site.
        """)
        
    with col2:
        st.warning("**Costs to Expense**")
        st.markdown("""
        * Costs of opening a new facility.
        * Costs of introducing a new product or service (marketing).
        * Administration and general overheads.
        * Costs incurred while an item capable of operating is not yet brought into use.
        """)

with tab2:
    st.markdown("#### 2. Measurement After Recognition")
    st.write("An entity shall choose either the **Cost Model** or the **Revaluation Model** as its accounting policy.")

    

    c1, c2 = st.columns(2)
    
    with c1:
        st.info("**Cost Model**")
        st.markdown("""
        **Carrying Amount =** Cost  
        (-) Accumulated Depreciation  
        (-) Accumulated Impairment Losses
        """)

    with c2:
        st.info("**Revaluation Model**")
        st.markdown("""
        **Carrying Amount =** Fair Value at date of revaluation  
        (-) Subsequent Acc. Depreciation  
        (-) Subsequent Acc. Impairment
        """)
        st.caption("Revaluations must be made with sufficient regularity.")

with tab3:
    st.markdown("#### 3. Depreciation")
    st.write("The depreciation method used shall reflect the pattern in which the asset’s future economic benefits are expected to be consumed by the entity.")
    
    st.markdown("""
    * **Straight-line:** Constant charge over the useful life.
    * **Diminishing balance:** Decreasing charge over the useful life.
    * **Units of production:** Charge based on expected use or output.
    """)
    
    st.error("**⚠️ Review Rule:** The residual value and the useful life of an asset shall be reviewed at least at each financial year-end.")

with tab4:
    st.markdown("#### 4. Derecognition")
    st.write("The carrying amount of an item of PPE shall be derecognized:")
    st.markdown("""
    * On **disposal** (sale, lease, donation).
    * When **no future economic benefits** are expected from its use or disposal.
    """)
    
    st.success("**Gains and Losses**")
    st.write("The gain or loss arising from derecognition is the difference between the net disposal proceeds and the carrying amount. It must be recognized in Profit or Loss.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 16")