import streamlit as st

# --- SUBPAGE HEADER (Reduced Size) ---
st.subheader("IAS 10: Events After the Reporting Period")
st.write("This standard dictates when an entity should adjust its financial statements for events that occur after the reporting period.")

# --- KEY TIMELINE VISUAL ---
st.info("**Timeline:** Reporting Date ➡ Events Occurring ➡ Authorization Date")

# --- MAIN CONTENT TABS ---
# Standardized labels for a clean look
tab1, tab2, tab3 = st.tabs(["Classification", "Examples", "Disclosure & Going Concern"])

with tab1:
    # Using H4 for a professional, medium-sized header
    st.markdown("#### Adjusting vs. Non-Adjusting")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Adjusting Events**")
        st.write("Evidence of conditions that **existed** at the end of the reporting period.")
        st.markdown("""
        * **Action:** Update financial statements.
        * **Impact:** Adjust carrying amounts of assets/liabilities.
        """)
        
    with col2:
        st.warning("**Non-Adjusting Events**")
        st.write("Indicative of conditions that **arose after** the reporting period.")
        st.markdown("""
        * **Action:** Do NOT update numbers.
        * **Impact:** Disclose in notes if material.
        """)

with tab2:
    st.markdown("#### Common Scenarios")
    
    # Expanders keep the page compact and readable
    with st.expander("✅ Adjusting Event Examples"):
        st.write("""
        * **Court Cases:** Settlement confirming a year-end obligation.
        * **Asset Impairment:** Bankruptcy of a customer after year-end.
        * **Inventory:** Sale of inventory providing evidence of Net Realizable Value (NRV).
        * **Errors:** Discovery of fraud showing the accounts were incorrect.
        """)
        
    with st.expander("❌ Non-Adjusting Event Examples"):
        st.write("""
        * **Market Value:** Significant decline in investment value after year-end.
        * **Dividends:** Declared after the reporting period.
        * **Disasters:** A fire or flood destroying a production plant after year-end.
        * **Forex:** Major changes in foreign exchange rates.
        """)

with tab3:
    st.markdown("#### Special Considerations")
    
    # Red box for critical 'Going Concern' rule
    st.error("**⚠️ Going Concern**")
    st.write("""
    If management determines after the reporting date that it intends to liquidate 
    or cease trading, the financial statements **cannot** be prepared on a going concern basis. 
    **This is always an adjusting event.**
    """)
    
    st.divider()
    
    st.markdown("**Required Disclosures**")
    st.write("1. The date the financial statements were **authorized for issue**.")
    st.write("2. The **nature** and **financial effect** of material non-adjusting events.")

# --- SIDEBAR CAPTION ---
# This will appear in your sidebar only when this page is active
st.sidebar.caption("Reference: International Accounting Standard 10")