import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 12: Disclosure of Interests in Other Entities")
st.write("This standard requires an entity to disclose information that enables users of its financial statements to evaluate the nature of, and risks associated with, its interests in other entities and the effects of those interests on its financial position, financial performance, and cash flows.")

# --- THE CORE OBJECTIVE ---
st.info("**Objective:** To provide transparency regarding an entity's involvement with subsidiaries, joint arrangements, associates, and structured entities.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Significant Judgments", "Subsidiaries & NCI", "Joint Interests & Associates"])

with tab1:
    st.markdown("#### 1. Significant Judgments and Assumptions")
    st.write("An entity must disclose the judgments and assumptions made in determining:")
    
    st.success("""
    * Whether it has **control** of another entity (per IFRS 10).
    * Whether it has **joint control** or **significant influence**.
    * The type of joint arrangement (Joint Operation vs. Joint Venture).
    """)
    
    with st.expander("📝 Why is this critical?"):
        st.write("""
        If Unilever holds 48% of a local distributor but claims it 'controls' the entity, IFRS 12 requires management to explain the specific facts (e.g., contractual rights or board composition) that lead to this conclusion.
        """)

with tab2:
    st.markdown("#### 2. Interests in Subsidiaries")
    st.write("An entity shall disclose information that enables users to understand the composition of the group and the interest that non-controlling interests (NCI) have in the group's activities.")

    st.error("**Key Disclosures for Subsidiaries:**")
    st.markdown("""
    * **Composition of the group:** Names and details of significant subsidiaries.
    * **NCI Interests:** For each subsidiary with material NCI, disclose the profit/loss allocated to NCI and the accumulated NCI balance.
    * **Significant Restrictions:** Any legal or contractual restrictions on the ability to access or use assets (e.g., central bank restrictions on moving cash out of a specific country).
    """)

    

with tab3:
    st.markdown("#### 3. Joint Arrangements and Associates")
    st.write("For material joint ventures and associates, an entity must provide summarized financial information to help users understand the scale of these operations.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Summarized Financials**")
        st.markdown("""
        * Current & Non-current assets.
        * Current & Non-current liabilities.
        * Revenue and Net Profit/Loss.
        * Dividends received from the entity.
        """)
    with col2:
        st.warning("**Risks & Commitments**")
        st.markdown("""
        * Capital commitments relating to the joint venture.
        * Contingent liabilities incurred in relation to associates.
        """)

    st.divider()
    st.markdown("#### Structured Entities (The 'Shadow' Entities)")
    st.write("""
    A structured entity is designed so that voting rights are not the dominant factor in deciding who controls it (e.g., a securitization vehicle). IFRS 12 requires disclosure of the **nature and extent** of your involvement and any support provided to these entities, even if you do not consolidate them.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 12")