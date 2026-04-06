import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 15: Revenue from Contracts with Customers")
st.write("This standard establishes a single comprehensive model for entities to use in accounting for revenue arising from contracts with customers.")

# --- THE CORE PRINCIPLE ---
st.info("**Core Rule:** Recognize revenue to depict the transfer of promised goods or services to customers in an amount that reflects the consideration to which the entity expects to be entitled.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The 5-Step Model", "Recognition (Point vs Time)", "Contract Costs"])

with tab1:
    st.markdown("#### 1. The Five-Step Framework")
    st.write("An entity applies these five steps to every contract with a customer:")
    
    st.success("**Step 1: Identify the Contract**")
    st.caption("Agreement between two or more parties that creates enforceable rights and obligations.")
    
    st.success("**Step 2: Identify Performance Obligations (PO)**")
    st.caption("Promises in a contract to transfer a distinct good or service to the customer.")
    
    st.success("**Step 3: Determine the Transaction Price**")
    st.caption("The amount of consideration (e.g., fixed price, variable discounts, rebates) an entity expects to be entitled to.")
    
    st.success("**Step 4: Allocate Transaction Price**")
    st.caption("Allocate the price to each PO based on relative stand-alone selling prices.")
    
    st.success("**Step 5: Recognize Revenue**")
    st.caption("Recognize revenue when (or as) the entity satisfies a performance obligation.")

    

with tab2:
    st.markdown("#### 2. Satisfaction of Performance Obligations")
    st.write("Revenue is recognized when control of the good or service is transferred to the customer.")

    col1, col2 = st.columns(2)
    with col1:
        st.warning("**At a Point in Time**")
        st.markdown("""
        * Typical for **goods** (e.g., FMCG products).
        * Indicators of control:
            * Physical possession.
            * Legal title.
            * Significant risks and rewards of ownership.
            * Customer has accepted the asset.
        """)
    with col2:
        st.warning("**Over Time**")
        st.markdown("""
        * Typical for **services** or customized assets.
        * Criteria (Must meet one):
            * Customer receives and consumes benefits as the entity performs.
            * Entity's performance creates/enhances an asset the customer controls.
            * Asset has no alternative use and entity has right to payment for work done.
        """)

    with st.expander("📝 Variable Consideration"):
        st.write("Includes discounts, rebates, refunds, and performance bonuses. An entity should only include variable consideration in the transaction price to the extent that it is **highly probable** that a significant reversal will not occur.")

with tab3:
    st.markdown("#### 3. Contract Costs & Presentation")
    
    st.info("**Incremental Costs of Obtaining a Contract**")
    st.write("Costs that an entity incurs to obtain a contract with a customer that it would not have incurred if the contract had not been obtained (e.g., sales commissions) are **capitalized** if they are expected to be recovered.")
    
    st.divider()
    
    st.markdown("**Contract Assets vs. Receivables**")
    st.markdown("""
    * **Receivable:** An unconditional right to consideration (only the passage of time is required).
    * **Contract Asset:** Right to consideration in exchange for goods/services transferred (e.g., dependent on satisfying another PO).
    * **Contract Liability:** An entity’s obligation to transfer goods/services for which it has received consideration (Unearned Revenue).
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 15")