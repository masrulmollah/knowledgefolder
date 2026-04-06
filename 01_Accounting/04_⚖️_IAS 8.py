import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 8: Accounting Policies, Changes in Estimates and Errors")
st.write("This standard enhances the relevance and reliability of an entity's financial statements and their comparability over time and with other entities.")

# --- THE GOLDEN RULE ---
st.info("**Objective:** To prescribe the criteria for selecting and changing accounting policies, along with the accounting treatment and disclosure of changes in policies, estimates, and corrections of errors.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Accounting Policies", "Accounting Estimates", "Prior Period Errors"])

with tab1:
    st.markdown("#### 1. Selection and Change in Accounting Policies")
    st.write("Accounting policies are the specific principles, bases, conventions, rules, and practices applied by an entity in preparing financial statements.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**When to Change?**")
        st.markdown("""
        Only if the change:
        * Is required by an **IFRS**.
        * Results in **more reliable and relevant** information.
        """)
        
    with col2:
        st.error("**Accounting Treatment**")
        st.markdown("""
        * **Retrospective Application:** Apply the new policy as if it had always been in place.
        * **Adjustment:** Adjust the opening balance of each affected component of equity for the earliest prior period presented.
        """)

with tab2:
    st.markdown("#### 2. Changes in Accounting Estimates")
    st.write("Estimates are necessary due to inherent uncertainties in business (e.g., bad debt provisions, useful lives of PPE).")

    

    st.warning("**Accounting Treatment: Prospective**")
    st.write("""
    Changes in estimates are recognized in the period of change (and future periods if affected). 
    **Do NOT restate prior periods.**
    """)
    
    with st.expander("📝 Examples of Estimates"):
        st.write("""
        * Changing the **useful life** or residual value of a factory machine.
        * Adjusting the **provision** for obsolete inventory.
        * Revising the **allowance** for doubtful accounts.
        """)

with tab3:
    st.markdown("#### 3. Prior Period Errors")
    st.write("Errors can arise from mathematical mistakes, mistakes in applying policies, oversights, or fraud.")
    
    st.error("**Accounting Treatment: Retrospective**")
    st.write("""
    Material prior period errors must be corrected **retrospectively** in the first set of financial statements authorized for issue after their discovery.
    """)
    
    with st.expander("🔍 Correction Method"):
        st.write("""
        1. **Restate** the comparative amounts for the prior period(s) presented in which the error occurred.
        2. If the error occurred before the earliest prior period presented, **restate the opening balances** of assets, liabilities, and equity for the earliest prior period presented.
        """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 8")