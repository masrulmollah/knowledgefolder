import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 34: Interim Financial Reporting")
st.write("This standard defines the minimum content of an interim financial report and the principles for recognition and measurement in complete or condensed financial statements for an interim period.")

# --- THE CORE CONCEPT ---
st.info("**Interim Period:** A financial reporting period shorter than a full financial year (e.g., Quarterly or Semi-annual reports).")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Content & Structure", "Recognition & Measurement", "Periods to Present"])

with tab1:
    st.markdown("#### 1. Minimum Content of an Interim Report")
    st.write("An entity may provide a 'Complete' set of financial statements (per IAS 1) or a 'Condensed' set.")
    
    st.success("**Condensed Components**")
    st.markdown("""
    * Condensed Statement of Financial Position.
    * Condensed Statement of Profit or Loss and OCI.
    * Condensed Statement of Changes in Equity.
    * Condensed Statement of Cash Flows.
    * **Selected Explanatory Notes:** Focus on events significant to an understanding of the changes since the last annual report.
    """)
    
    with st.expander("📝 Significant Events for Disclosure"):
        st.markdown("""
        * Write-down of inventories to NRV.
        * Recognition/Reversal of impairment losses.
        * Litigation settlements.
        * Corrections of prior period errors.
        * Changes in the business or economic circumstances affecting fair value.
        """)

with tab2:
    st.markdown("#### 2. Recognition and Measurement")
    st.write("The same accounting policies must be applied in the interim report as are applied in the annual financial statements.")

    

    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("**Seasonality**")
        st.write("Revenues received seasonally or occasionally within a financial year should **not** be anticipated or deferred at an interim date if such treatment is inappropriate at year-end.")
        
    with col2:
        st.info("**Income Tax Expense**")
        st.write("Recognized in each interim period based on the best estimate of the **weighted average annual income tax rate** expected for the full financial year.")

    st.divider()
    st.error("**Discrete vs. Integral View**")
    st.write("IAS 34 follows the 'Discrete View' – the interim period is a distinct reporting period, but the frequency of reporting should not affect the measurement of the annual results.")

with tab3:
    st.markdown("#### 3. Periods Required to be Presented")
    st.write("For an entity reporting quarterly (e.g., Q3), the following comparatives are required:")
    
    st.markdown("""
    1. **SFP:** End of current interim period vs. End of **immediately preceding financial year**.
    2. **P&L:** Current interim period (Q3) and Year-to-date (YTD) vs. Comparable periods of the **preceding financial year**.
    3. **Equity:** YTD vs. Comparable YTD of the **preceding financial year**.
    4. **Cash Flows:** YTD vs. Comparable YTD of the **preceding financial year**.
    """)
    
    st.divider()
    st.markdown("**Materiality**")
    st.write("In deciding how to recognize, measure, or disclose an item for interim reporting purposes, materiality shall be assessed in relation to the **interim period financial data**.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 34")