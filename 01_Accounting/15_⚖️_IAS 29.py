import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 29: Financial Reporting in Hyperinflationary Economies")
st.write("This standard is applied to the individual financial statements, as well as the consolidated financial statements, of any entity whose functional currency is the currency of a hyperinflationary economy.")

# --- THE TRIGGER CONDITION ---
st.error("**Core Rule:** In a hyperinflationary economy, financial statements must be stated in terms of the **measuring unit current at the end of the reporting period.**")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Identifying Hyperinflation", "The Restatement Process", "Disclosures"])

with tab1:
    st.markdown("#### 1. When is an Economy Hyperinflationary?")
    st.write("IAS 29 does not establish an absolute rate, but it identifies indicators of hyperinflation:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Economic Indicators**")
        st.markdown("""
        * The general population prefers to keep wealth in **non-monetary assets** or stable foreign currencies.
        * Prices are quoted in a stable **foreign currency**.
        * Sales and purchases on credit take place at prices that compensate for the expected loss of purchasing power.
        """)
        
    with col2:
        st.warning("**The Numerical Benchmark**")
        st.markdown("""
        * Interest rates, wages, and prices are linked to a **price index**.
        * The cumulative inflation rate over three years is approaching, or exceeds, **100%**.
        """)

with tab2:
    st.markdown("#### 2. How to Restate the Accounts")
    st.write("All amounts in the statement of financial position not already expressed in terms of the measuring unit current at the end of the reporting period must be restated.")

    

    c1, c2 = st.columns(2)
    
    with c1:
        st.info("**Monetary Items**")
        st.write("Money held and items to be received or paid in money (e.g., Cash, Receivables, Loans).")
        st.markdown("- **Action:** Do NOT restate (they are already expressed in current units).")
        
    with c2:
        st.info("**Non-Monetary Items**")
        st.write("Items not expressed in current units (e.g., PPE, Inventory, Equity).")
        st.markdown("- **Action:** Restate by applying a **General Price Index** from the date of acquisition to the reporting date.")

    st.divider()
    st.error("**Gain or Loss on Net Monetary Position**")
    st.write("The gain or loss on the net monetary position is recognized in **Profit or Loss** and disclosed separately. This reflects the impact of inflation on the entity's monetary assets and liabilities.")

with tab3:
    st.markdown("#### 3. Reporting & Disclosures")
    st.write("When an economy ceases to be hyperinflationary, the entity discontinues the preparation of financial statements in accordance with IAS 29.")
    
    st.markdown("**Required Disclosures:**")
    st.markdown("""
    1. The **fact** that the financial statements have been restated for changes in the general purchasing power of the functional currency.
    2. Whether the financial statements are based on a **historical cost** approach or a current cost approach.
    3. The **identity and level of the price index** at the end of the reporting period and the movement in the index during the current and previous periods.
    """)
    
    with st.expander("📝 Impact on Statement of Cash Flows"):
        st.write("All items in the statement of cash flows are expressed in terms of the measuring unit current at the end of the reporting period.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 29")