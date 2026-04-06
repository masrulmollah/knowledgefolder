import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 7: Statement of Cash Flows")
st.write("This standard requires the presentation of information about the historical changes in cash and cash equivalents of an entity by means of a statement of cash flows.")

# --- DEFINITIONS ---
st.info("**Cash equivalents** are short-term, highly liquid investments that are readily convertible to known amounts of cash and which are subject to an insignificant risk of changes in value.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Classification", "Reporting Methods", "Special Items"])

with tab1:
    st.markdown("#### Classification of Cash Flows")
    st.write("Cash flows during the period must be classified into three distinct categories:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("**Operating**")
        st.write("Principal revenue-producing activities (e.g., cash from sales, payments to suppliers/employees).")
        
    with col2:
        st.info("**Investing**")
        st.write("Acquisition and disposal of long-term assets (e.g., buying PPE, selling shares in other entities).")
        
    with col3:
        st.warning("**Financing**")
        st.write("Activities that result in changes in the size and composition of equity and borrowings.")

with tab2:
    st.markdown("#### Methods of Reporting Operating Cash Flows")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("**Direct Method**")
        st.write("Major classes of gross cash receipts and gross cash payments are disclosed (e.g., 'Cash received from customers').")
        st.caption("IAS 7 encourages the use of the Direct Method.")
        
    with c2:
        st.markdown("**Indirect Method**")
        st.write("Profit or loss is adjusted for the effects of non-cash transactions and deferrals/accruals (e.g., 'Profit + Depreciation - Increase in Receivables').")

    

with tab3:
    st.markdown("#### Special Items & Disclosures")
    
    with st.expander("📌 Interest and Dividends"):
        st.write("""
        * **Interest Paid:** Can be Operating or Financing.
        * **Interest/Dividends Received:** Can be Operating or Investing.
        * **Dividends Paid:** Can be Operating or Financing.
        * *Consistency is key: once a classification is chosen, it must be used consistently.*
        """)
        
    with st.expander("🏢 Taxes on Income"):
        st.write("Cash flows arising from taxes on income shall be classified as **Operating** unless they can be specifically identified with financing and investing activities.")

    with st.expander("🚫 Non-Cash Transactions"):
        st.error("**Rule:** Investing and financing transactions that do not require the use of cash shall be **excluded** from the statement of cash flows.")
        st.write("Example: Acquisition of assets by assuming directly related liabilities or by means of a finance lease.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 7")