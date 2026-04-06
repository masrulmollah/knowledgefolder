import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 28: Investments in Associates and Joint Ventures")
st.write("This standard outlines how to account for investments in associates and sets out the requirements for the application of the equity method when accounting for investments in associates and joint ventures.")

# --- THE CORE CONCEPT ---
st.info("**Significant Influence:** The power to participate in the financial and operating policy decisions of the investee, but not control or joint control over those policies.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Significant Influence", "The Equity Method", "Impairment & Exemptions"])

with tab1:
    st.markdown("#### 1. Identifying Significant Influence")
    st.write("Significant influence is presumed to exist if an entity holds, directly or indirectly, **20% or more** of the voting power of the investee.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Indicators of Influence**")
        st.markdown("""
        * Representation on the **Board of Directors**.
        * Participation in **policy-making** processes.
        * Material transactions between the entities.
        * Interchange of **managerial personnel**.
        * Provision of essential technical information.
        """)
        
    with col2:
        st.warning("**Joint Ventures**")
        st.write("A joint arrangement whereby the parties that have joint control of the arrangement have rights to the **net assets** of the arrangement.")
        st.caption("Joint Ventures MUST also use the Equity Method under IAS 28.")

with tab2:
    st.markdown("#### 2. Mechanics of the Equity Method")
    st.write("The investment is initially recognized at **cost** and adjusted thereafter for the post-acquisition change in the investor’s share of the investee’s net assets.")

    

    st.markdown("**Accounting Entries:**")
    st.info("""
    * **Share of Profit/Loss:** Recognized in the investor's Profit or Loss.
    * **Dividends Received:** These are NOT income; they **reduce** the carrying amount of the investment (as they are a return of capital).
    * **Other Comprehensive Income (OCI):** The investor’s share of the investee’s OCI is recognized in the investor’s OCI.
    """)
    
    with st.expander("📝 Potential Adjustments"):
        st.write("""
        * **Uniform Accounting Policies:** The investee’s financial statements must be adjusted to match the investor’s policies.
        * **Reporting Dates:** If dates differ, the difference should not be more than three months.
        * **Upstream/Downstream Transactions:** Profits and losses resulting from transactions between the entities are eliminated to the extent of the investor’s interest.
        """)

with tab3:
    st.markdown("#### 3. Impairment & Discontinuance")
    
    st.error("**Impairment Testing**")
    st.write("""
    After applying the equity method, the investor applies **IAS 36 (Impairment of Assets)** to determine whether it is necessary to recognize any additional impairment loss with respect to its net investment in the associate or joint venture.
    """)
    
    st.divider()
    
    st.markdown("**When to Stop using the Equity Method?**")
    st.markdown("""
    * If the investment becomes a **subsidiary** (Apply IFRS 10).
    * If the retained interest is a **financial asset** (Apply IFRS 9).
    * If the entity loses significant influence or joint control.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 28")