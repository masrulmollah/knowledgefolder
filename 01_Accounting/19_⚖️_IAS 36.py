import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 36: Impairment of Assets")
st.write("This standard ensures that an entity's assets are carried at no more than their recoverable amount. An asset is impaired when its carrying amount exceeds the amount to be recovered through use or sale.")

# --- THE CORE PRINCIPLE ---
st.error("**Core Rule:** If the Carrying Amount > Recoverable Amount, the asset is impaired and must be written down.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["Scope & Indicators", "Recoverable Amount", "Cash-Generating Units", "Reversals"])

with tab1:
    st.markdown("#### 1. When to Test for Impairment?")
    st.write("Assets should be tested whenever there is an **indication** of impairment. However, some assets must be tested **annually** regardless of indicators:")
    st.info("* Goodwill acquired in a business combination.\n* Intangible assets with an indefinite useful life.\n* Intangible assets not yet available for use.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**External Indicators**")
        st.markdown("""
        * Decline in asset's market value.
        * Significant changes in technology, market, or laws.
        * Increase in market interest rates (increasing the discount rate).
        """)
    with col2:
        st.warning("**Internal Indicators**")
        st.markdown("""
        * Evidence of **obsolescence** or physical damage.
        * Changes in the way the asset is used (e.g., plans to discontinue).
        * Internal reports showing lower-than-expected economic performance.
        """)

with tab2:
    st.markdown("#### 2. Determining Recoverable Amount")
    st.write("The Recoverable Amount is the **higher** of two values:")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Fair Value Less Costs of Disposal (FVLCD)**")
        st.write("The amount obtainable from the sale of an asset in an arm’s length transaction between knowledgeable, willing parties, less the costs of disposal.")
    with c2:
        st.info("**Value in Use (VIU)**")
        st.write("The present value of the **future cash flows** expected to be derived from an asset or cash-generating unit.")

    st.divider()
    st.latex(r"Recoverable\ Amount = max(FVLCD,\ VIU)")

with tab3:
    st.markdown("#### 3. Cash-Generating Units (CGU)")
    st.write("If it is not possible to estimate the recoverable amount of an individual asset, determine the recoverable amount of the **CGU** to which the asset belongs.")
    
    st.success("**Definition:** The smallest identifiable group of assets that generates cash inflows that are largely independent of the cash inflows from other assets or groups of assets.")
    
    with st.expander("📦 Allocation of Impairment Loss"):
        st.write("When a CGU is impaired, the loss is allocated in this order:")
        st.markdown("""
        1.  First, reduce the carrying amount of any **Goodwill** allocated to the CGU.
        2.  Then, to the **other assets** of the unit pro rata on the basis of the carrying amount of each asset.
        """)

with tab4:
    st.markdown("#### 4. Reversal of Impairment")
    st.write("An entity assesses at each reporting date whether there is an indication that an impairment loss recognized in prior periods may no longer exist or may have decreased.")
    
    st.warning("**The Golden Rule of Reversal**")
    st.markdown("""
    * **Goodwill:** Impairment losses recognized for Goodwill can **NEVER** be reversed.
    * **Other Assets:** Reversal is recognized in Profit or Loss (unless the asset is revalued) and is limited to what the carrying amount would have been (net of depreciation) had no impairment occurred.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 36")