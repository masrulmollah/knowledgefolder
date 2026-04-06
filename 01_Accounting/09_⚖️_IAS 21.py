import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 21: The Effects of Changes in Foreign Exchange Rates")
st.write("This standard prescribes how to include foreign currency transactions and foreign operations in the financial statements of an entity and how to translate financial statements into a presentation currency.")

# --- THE CORE CONCEPTS ---
st.info("**Functional Currency:** The currency of the primary economic environment in which the entity operates.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Functional Currency", "Foreign Transactions", "Translation of Operations"])

with tab1:
    st.markdown("#### 1. Determining Functional Currency")
    st.write("An entity considers the following primary indicators:")
    st.markdown("""
    * The currency that mainly influences **sales prices** for goods and services.
    * The currency of the country whose competitive forces and regulations mainly determine sales prices.
    * The currency that mainly influences **labor, material, and other costs** of providing goods or services.
    """)
    
    st.warning("**Presentation Currency:** The currency in which the financial statements are presented (can be different from the functional currency).")

with tab2:
    st.markdown("#### 2. Reporting Foreign Currency Transactions")
    st.write("A foreign currency transaction is recorded, on initial recognition, using the **spot exchange rate** at the date of the transaction.")

    

    st.markdown("**Reporting at Subsequent End Dates:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Monetary Items**")
        st.write("Units of currency held and assets/liabilities to be received/paid in fixed units of currency (e.g., Cash, Receivables, Payables).")
        st.markdown("- **Rate:** Use the **Closing Rate**.")
        st.markdown("- **Gain/Loss:** Recognize in **Profit or Loss**.")
        
    with col2:
        st.info("**Non-Monetary Items**")
        st.write("Items that do not result in a right to receive or an obligation to deliver fixed units of currency (e.g., Inventory, PPE, Goodwill).")
        st.markdown("- **Rate:** Use the **Historical Rate** at the date of transaction.")
        st.markdown("- **Gain/Loss:** Usually no exchange difference arises.")

with tab3:
    st.markdown("#### 3. Translation to Presentation Currency")
    st.write("When an entity translates its results and financial position from a functional currency to a different presentation currency:")

    st.markdown("""
    1. **Assets and Liabilities:** Translate at the **closing rate** at the date of the statement of financial position.
    2. **Income and Expenses:** Translate at the **exchange rates at the dates of the transactions** (average rates are often used for practicality).
    3. **Exchange Differences:** Recognized in **Other Comprehensive Income (OCI)** and accumulated in a separate component of equity.
    """)
    
    st.error("**⚠️ Note:** If the functional currency is that of a hyperinflationary economy, the financial statements are restated in accordance with IAS 29 before translation.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 21")