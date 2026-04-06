import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 27: Separate Financial Statements")
st.write("This standard is applied in accounting for investments in subsidiaries, joint ventures, and associates when an entity elects, or is required by local regulations, to present separate financial statements.")

# --- THE CORE DEFINITION ---
st.info("**Separate Financial Statements:** Those presented by an entity, in which the entity could elect to account for its investments in subsidiaries, joint ventures and associates either at cost, in accordance with IFRS 9, or using the equity method.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Preparation & Methods", "Dividend Income", "Disclosures"])

with tab1:
    st.markdown("#### 1. Preparation of Separate Financial Statements")
    st.write("When an entity prepares separate financial statements, it shall account for investments in subsidiaries, joint ventures, and associates either:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("**At Cost**")
        st.write("The investment is recorded at the original purchase price less any accumulated impairment losses.")
        
    with col2:
        st.info("**IFRS 9 Method**")
        st.write("In accordance with IFRS 9 (Financial Instruments), typically at Fair Value through Profit or Loss (FVTPL) or OCI.")
        
    with col3:
        st.warning("**Equity Method**")
        st.write("As described in IAS 28, where the investment is initially at cost and adjusted for the post-acquisition change in net assets.")

    st.markdown("---")
    st.error("**⚠️ Critical Requirement:** The entity shall apply the same accounting for each category of investments (e.g., all subsidiaries must be treated the same way).")

with tab2:
    st.markdown("#### 2. Treatment of Dividends")
    st.write("An entity shall recognize a dividend from a subsidiary, joint venture, or associate in its separate financial statements when its **right to receive the dividend is established**.")

    

    st.info("**Where to Recognize?**")
    st.write("The dividend is recognized in **Profit or Loss** unless the entity elects to use the equity method, in which case the dividend reduces the carrying amount of the investment.")
    
    with st.expander("📝 Reorganization Note"):
        st.write("If a parent reorganizes the structure of its group by establishing a new parent, specific rules apply to measuring the cost of the new parent’s investment in the original parent.")

with tab3:
    st.markdown("#### 3. Required Disclosures")
    st.write("When a parent elects not to prepare consolidated financial statements (under the IFRS 10 exemption) and prepares only separate statements, it must disclose:")
    
    st.markdown("""
    1. That the financial statements are **separate financial statements**.
    2. A **list of significant investments** in subsidiaries, joint ventures, and associates (including name, country of incorporation, and proportion of ownership).
    3. The **method used** to account for those investments.
    """)
    
    st.divider()
    st.markdown("**Investment Entities**")
    st.write("If a parent is an 'Investment Entity', it is required to measure its investment in subsidiaries at fair value through profit or loss in accordance with IFRS 9.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 27")