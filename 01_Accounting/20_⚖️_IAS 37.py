import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 37: Provisions, Contingent Liabilities and Contingent Assets")
st.write("This standard ensures that appropriate recognition criteria and measurement bases are applied to provisions, contingent liabilities, and contingent assets.")

# --- THE THREE PILLARS ---
st.info("**Core Objective:** To ensure that only genuine obligations are recognized in the financial statements. Future operating losses and 'general' provisions are strictly prohibited.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Provisions", "Contingent Items", "Specific Applications"])

with tab1:
    st.markdown("#### 1. Recognition of a Provision")
    st.write("A provision shall be recognized when:")
    st.success("""
    1. An entity has a **present obligation** (legal or constructive) as a result of a past event.
    2. It is **probable** (more likely than not) that an outflow of resources will be required to settle it.
    3. A **reliable estimate** can be made of the amount of the obligation.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Legal Obligation**")
        st.caption("Derives from a contract, legislation, or other operation of law.")
    with col2:
        st.markdown("**Constructive Obligation**")
        st.caption("Derives from an entity's actions where it has indicated to other parties that it will accept certain responsibilities (e.g., a published policy).")

    

    st.markdown("#### Measurement")
    st.write("The amount recognized should be the **best estimate** of the expenditure required to settle the present obligation. If the effect of the time value of money is material, the provision should be **discounted**.")

with tab2:
    st.markdown("#### 2. Contingent Liabilities & Assets")
    
    c1, c2 = st.columns(2)
    with c1:
        st.error("**Contingent Liability**")
        st.markdown("""
        * **Nature:** A possible obligation (uncertain) or a present obligation where outflow is NOT probable.
        * **Treatment:** Do NOT recognize. **Disclose** in notes unless the possibility of outflow is remote.
        """)
    with c2:
        st.info("**Contingent Asset**")
        st.markdown("""
        * **Nature:** A possible asset that arises from past events and whose existence will be confirmed only by future events.
        * **Treatment:** Do NOT recognize. **Disclose** only when an inflow of economic benefits is probable.
        """)

    st.warning("**Virtually Certain:** If an inflow of economic benefits is virtually certain, the asset is no longer contingent and should be recognized.")

with tab3:
    st.markdown("#### 3. Specific Applications")
    
    with st.expander("🛠️ Restructuring Costs"):
        st.write("A provision for restructuring is recognized only when the general recognition criteria are met. A constructive obligation exists only when there is a **detailed formal plan** and a **valid expectation** has been raised in those affected.")
        st.caption("Includes: Redundancy costs. Excludes: Retraining, marketing, or investment in new systems.")
        
    with st.expander("📉 Onerous Contracts"):
        st.write("A contract in which the unavoidable costs of meeting the obligations exceed the economic benefits expected to be received. The present obligation under the contract shall be recognized and measured as a provision.")
        
    with st.expander("🌱 Decommissioning/Restoration"):
        st.write("If a factory lease or law requires the site to be restored at the end of use, a provision is recognized when the plant is installed, with a corresponding increase in the cost of the asset (IAS 16).")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 37")