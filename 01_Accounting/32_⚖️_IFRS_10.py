import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 10: Consolidated Financial Statements")
st.write("This standard establishes principles for the presentation and preparation of consolidated financial statements when an entity controls one or more other entities.")

# --- THE CORE PRINCIPLE ---
st.info("**Core Rule:** An investor, regardless of the nature of its involvement with an entity, shall determine whether it is a **parent** by assessing whether it **controls** the investee.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The Three Elements of Control", "Consolidation Procedures", "Investment Entities"])

with tab1:
    st.markdown("#### 1. The Definition of Control")
    st.write("An investor controls an investee if and only if the investor has **ALL** of the following:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**1. Power**")
        st.write("Existing rights that give the current ability to direct the **relevant activities** (those that significantly affect returns).")
    with col2:
        st.warning("**2. Exposure/Rights**")
        st.write("Exposure, or rights, to **variable returns** from its involvement with the investee.")
    with col3:
        st.error("**3. Ability to Use Power**")
        st.write("The ability to use its power over the investee to **affect the amount** of the investor's returns.")

    

    with st.expander("📝 De Facto Control"):
        st.write("""
        Control can exist even without a majority of voting rights (e.g., holding 45% when the remaining 55% is widely dispersed among thousands of small shareholders). This is known as 'De Facto' control.
        """)

with tab2:
    st.markdown("#### 2. Consolidation Procedures")
    st.write("Consolidated financial statements combine like items of assets, liabilities, equity, income, expenses, and cash flows of the parent with those of its subsidiaries.")

    st.markdown("**Key Requirements:**")
    st.markdown("""
    * **Uniform Accounting Policies:** Use uniform policies for like transactions in similar circumstances.
    * **Reporting Dates:** If the reporting dates differ, the difference cannot be more than **three months**, and adjustments must be made for significant transactions in that gap.
    * **Intragroup Eliminations:** Eliminate in full all intragroup assets/liabilities, equity, income, expenses, and cash flows (e.g., unrealized profits on inventory sold between Unilever entities).
    """)

    st.divider()
    st.info("**Non-controlling Interests (NCI):**")
    st.write("Present NCI in the consolidated statement of financial position within **equity**, separately from the equity of the owners of the parent.")

with tab3:
    st.markdown("#### 3. Exceptions & Loss of Control")
    
    st.warning("**The Investment Entity Exception**")
    st.write("""
    A parent that is an 'Investment Entity' (like a Private Equity fund) does not consolidate its subsidiaries. Instead, it measures them at **Fair Value Through Profit or Loss (FVTPL)** under IFRS 9.
    """)
    
    st.divider()
    
    st.markdown("**Loss of Control**")
    st.write("If a parent loses control of a subsidiary, it:")
    st.markdown("""
    1. Derecognizes the assets and liabilities of the former subsidiary.
    2. Recognizes any investment retained in the former subsidiary at its **fair value**.
    3. Recognizes the gain or loss associated with the loss of control in **Profit or Loss**.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 10")