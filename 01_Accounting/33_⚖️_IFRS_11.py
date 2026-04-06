import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 11: Joint Arrangements")
st.write("This standard outlines the accounting for arrangements where two or more parties have joint control. The focus is on the rights and obligations of the parties, rather than the legal structure of the arrangement.")

# --- THE CORE PRINCIPLE ---
st.info("**Joint Control:** The contractually agreed sharing of control, which exists only when decisions about the relevant activities require the **unanimous consent** of the parties sharing control.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Classification", "Joint Operations", "Joint Ventures"])

with tab1:
    st.markdown("#### 1. Classifying the Arrangement")
    st.write("IFRS 11 classifies joint arrangements into two types based on the rights and obligations of the parties:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Joint Operation**")
        st.write("Parties have rights to the **assets** and obligations for the **liabilities** relating to the arrangement.")
    with col2:
        st.warning("**Joint Venture**")
        st.write("Parties have rights to the **net assets** of the arrangement.")

    

    with st.expander("📝 The 'Unanimous Consent' Test"):
        st.write("""
        If a company owns 50% and another owns 50%, but the agreement says decisions only need 51% approval, it is **NOT** a joint arrangement under IFRS 11 (it might be a subsidiary under IFRS 10 for whoever has that 1% edge). Joint control requires everyone at the table to agree.
        """)

with tab2:
    st.markdown("#### 2. Accounting for Joint Operations")
    st.write("A joint operator recognizes its interest in a joint operation by accounting for its share of individual assets, liabilities, revenues, and expenses.")

    st.markdown("**The 'Line-by-Line' Approach:**")
    st.code("""
# The operator records in its own financial statements:
1. Its assets, including its share of any assets held jointly.
2. Its liabilities, including its share of any liabilities incurred jointly.
3. Its revenue from the sale of its share of the output.
4. Its expenses, including its share of any expenses incurred jointly.
    """, language="python")

with tab3:
    st.markdown("#### 3. Accounting for Joint Ventures")
    st.write("A joint venturer recognizes its interest in a joint venture as an investment and accounts for that investment using the **Equity Method**.")
    
    st.error("**Proportional Consolidation is Prohibited**")
    st.write("Under the old standards (IAS 31), you could consolidate 50% of the assets and liabilities. IFRS 11 strictly forbids this for Joint Ventures. You must use the Equity Method (IAS 28).")
    
    with st.expander("📊 How the Equity Method Works"):
        st.markdown("""
        * **Initial Recognition:** Recorded at cost.
        * **Subsequent:** The carrying amount is increased or decreased to recognize the venturer's share of the profit or loss of the investee after the date of acquisition.
        * **Dividends:** Received dividends reduce the carrying amount of the investment.
        """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 11")