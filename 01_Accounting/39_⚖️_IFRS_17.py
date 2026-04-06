import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 17: Insurance Contracts")
st.write("This standard establishes principles for the recognition, measurement, presentation, and disclosure of insurance contracts within the scope of the standard.")

# --- THE CORE PHILOSOPHY ---
st.info("**The General Measurement Model (GMM):** IFRS 17 moves away from historical cost to a 'Current Value' approach, measuring insurance contracts using updated estimates and assumptions that reflect the timing, amount, and uncertainty of future cash flows.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The Three Building Blocks", "Measurement Models", "Presentation"])

with tab1:
    st.markdown("#### 1. The Four Components of Liability")
    st.write("The measurement of a group of insurance contracts includes:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**1. Estimates of Future Cash Flows**")
        st.write("Probability-weighted estimates of all cash inflows (premiums) and outflows (claims, expenses).")
        
        st.warning("**2. Discount Rate**")
        st.write("Reflects the time value of money, the characteristics of the cash flows, and liquidity.")
    with col2:
        st.error("**3. Risk Adjustment**")
        st.write("The compensation the entity requires for bearing the uncertainty about the amount and timing of the cash flows.")
        
        st.info("**4. Contractual Service Margin (CSM)**")
        st.write("Represents the unearned profit the entity will recognize as it provides services in the future.")

    

with tab2:
    st.markdown("#### 2. Three Measurement Approaches")
    st.write("IFRS 17 provides different models depending on the nature of the contract:")

    st.markdown("**1. General Measurement Model (GMM)**")
    st.caption("The default model for all insurance contracts (especially long-term life insurance).")

    st.markdown("**2. Premium Allocation Approach (PAA)**")
    st.caption("A simplified model for short-term contracts (typically 12 months or less). Very similar to the old 'unearned premium' logic.")

    st.markdown("**3. Variable Fee Approach (VFA)**")
    st.caption("For 'direct participation' contracts where the policyholder shares in the returns of a pool of underlying items.")

    with st.expander("📝 Onerous Contracts (Loss-making)"):
        st.write("If a group of contracts is expected to be loss-making at inception, the loss must be recognized in **Profit or Loss immediately**. You cannot defer losses over the contract term.")

with tab3:
    st.markdown("#### 3. New P&L Presentation")
    st.write("IFRS 17 fundamentally changes how 'Revenue' is reported for insurers.")
    
    st.warning("**Insurance Service Result**")
    st.markdown("""
    * **Insurance Service Revenue:** Reflects the provision of services (not just premiums collected). 
    * **Insurance Service Expenses:** Incurred claims and other expenses.
    * **Exclusion:** Investment components (amounts repaid to policyholders even if no insured event occurs) are **NOT** included in revenue or expenses.
    """)

    

    st.divider()
    st.markdown("#### Key Disclosure: The Reconciliation")
    st.write("Entities must provide a detailed reconciliation showing how the carrying amount of insurance contracts changed from the beginning to the end of the period, broken down by the four building blocks.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 17")