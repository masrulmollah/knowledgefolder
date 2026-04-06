import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 5: Non-current Assets Held for Sale and Discontinued Operations")
st.write("This standard specifies the accounting for assets held for sale and the presentation and disclosure of discontinued operations.")

# --- THE CORE PRINCIPLE ---
st.info("**Core Rule:** Assets that meet the criteria to be classified as 'held for sale' should be measured at the lower of carrying amount and fair value less costs to sell, and depreciation on such assets should cease.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Classification Criteria", "Measurement Rules", "Discontinued Operations"])

with tab1:
    st.markdown("#### 1. Classification as Held for Sale")
    st.write("An entity shall classify a non-current asset (or disposal group) as held for sale if its carrying amount will be recovered principally through a **sale transaction** rather than through continuing use.")
    
    st.success("**The Strict Criteria:**")
    st.markdown("""
    1. The asset must be **available for immediate sale** in its present condition.
    2. The sale must be **highly probable**.
    3. Management must be committed to a plan to sell.
    4. An active program to locate a buyer must have been initiated.
    5. The asset must be actively marketed at a price that is **reasonable** in relation to its current fair value.
    6. The sale is expected to qualify for recognition as a completed sale within **one year**.
    """)

    

with tab2:
    st.markdown("#### 2. Measurement of Assets Held for Sale")
    st.write("Immediately before the initial classification, the carrying amounts of the assets shall be measured in accordance with applicable IFRSs (e.g., IAS 16, IAS 38).")

    st.error("**Subsequent Measurement**")
    st.markdown("""
    * Measure at the **Lower of**: 
        * Carrying Amount.
        * Fair Value less Costs to Sell (FVLCTS).
    * **Cease Depreciation:** Non-current assets classified as held for sale shall NOT be depreciated.
    """)
    
    with st.expander("📝 Recognition of Impairment"):
        st.write("Any write-down to FVLCTS is recognized as an impairment loss in Profit or Loss. Subsequent increases in FVLCTS can be recognized as a gain, but only up to the amount of cumulative impairment losses previously recognized.")

with tab3:
    st.markdown("#### 3. Discontinued Operations")
    st.write("A discontinued operation is a component of an entity that either has been disposed of or is classified as held for sale.")
    
    st.warning("**Presentation Requirements**")
    st.markdown("""
    * **Statement of Comprehensive Income:** A single amount on the face of the P&L representing the post-tax profit/loss of the discontinued operation and the post-tax gain/loss on the measurement/disposal.
    * **Statement of Financial Position:** Assets and liabilities of a disposal group must be presented **separately** from other assets and liabilities (no offsetting).
    """)

    

    st.divider()
    st.markdown("#### Cash Flow Disclosure")
    st.write("The net cash flows attributable to the operating, investing, and financing activities of discontinued operations shall be separately presented or disclosed in the notes.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 5")