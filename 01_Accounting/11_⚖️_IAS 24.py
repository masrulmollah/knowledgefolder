import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 24: Related Party Disclosures")
st.write("This standard ensures that an entity's financial statements contain the disclosures necessary to draw attention to the possibility that its financial position and profit or loss may have been affected by the existence of related parties.")

# --- THE DISCLOSURE PRINCIPLE ---
st.info("**Core Objective:** Knowledge of an entity’s transactions, outstanding balances, and relationships with related parties may affect the assessments of its operations by users of financial statements.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Identifying Related Parties", "Required Disclosures", "Exemptions"])

with tab1:
    st.markdown("#### 1. Who is a Related Party?")
    st.write("A person or entity is related to the reporting entity if:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Persons**")
        st.markdown("""
        * **Control:** Has control or joint control over the entity.
        * **Influence:** Has significant influence over the entity.
        * **KMP:** Is a member of the **Key Management Personnel** (including directors).
        * **Family:** Close members of the family of the persons above.
        """)
        
    with col2:
        st.info("**Entities**")
        st.markdown("""
        * Members of the **same group** (Parent, Subsidiary, Fellow Subsidiary).
        * **Associates** or Joint Ventures.
        * Post-employment benefit plans for the benefit of employees.
        * Entities controlled by a related person.
        """)

    

with tab2:
    st.markdown("#### 2. What Must Be Disclosed?")
    st.write("Relationships between a **parent and its subsidiaries** must be disclosed irrespective of whether there have been transactions between them.")

    with st.expander("📊 Transaction Disclosures"):
        st.write("If there have been transactions, disclose the nature of the relationship, the amount of transactions, and outstanding balances including:")
        st.markdown("""
        * Purchases or sales of goods/assets.
        * Rendering or receiving of services.
        * Leases and transfers of research and development.
        * Transfers under license agreements.
        * Finance (loans or equity contributions).
        """)
        
    with st.expander("👥 Key Management Personnel (KMP)"):
        st.error("**KMP Compensation**")
        st.write("Disclose total compensation and the breakdown for:")
        st.markdown("""
        1. Short-term employee benefits.
        2. Post-employment benefits.
        3. Other long-term benefits.
        4. Termination benefits.
        5. Share-based payments.
        """)

with tab3:
    st.markdown("#### 3. Special Cases & Exemptions")
    
    st.warning("**Government-Related Entities**")
    st.write("""
    A reporting entity is exempt from the disclosure requirements in relation to related party transactions and outstanding balances with:
    * A government that has control or significant influence over the reporting entity.
    * Another entity that is a related party because the same government has control or significant influence over both.
    """)
    
    st.divider()
    st.markdown("**Arm’s Length Transactions**")
    st.write("Disclosures that related party transactions were made on terms equivalent to those that prevail in arm’s length transactions are made **only if such terms can be substantiated.**")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 24")