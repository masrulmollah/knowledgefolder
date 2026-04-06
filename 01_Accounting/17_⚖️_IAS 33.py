import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 33: Earnings Per Share")
st.write("This standard prescribes principles for the determination and presentation of earnings per share (EPS) to improve performance comparisons between different entities in the same reporting period and between different reporting periods for the same entity.")

# --- THE SCOPE ---
st.info("**Scope:** IAS 33 applies to entities whose ordinary shares or potential ordinary shares are publicly traded, or that are in the process of issuing such shares in public markets.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Basic EPS", "Diluted EPS", "Presentation & Disclosures"])

with tab1:
    st.markdown("#### 1. Basic Earnings Per Share")
    st.write("Basic EPS is calculated by dividing profit or loss attributable to ordinary equity holders by the weighted average number of ordinary shares outstanding.")
    
    st.latex(r"Basic\ EPS = \frac{Net\ Profit\ (Attributable\ to\ Ordinary\ Shareholders)}{Weighted\ Average\ Number\ of\ Ordinary\ Shares}")

    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Numerator (Earnings)**")
        st.markdown("""
        * Start with Net Profit or Loss.
        * **Subtract:** Post-tax preference dividends.
        * **Adjust:** For any differences arising from the settlement of preference shares.
        """)
        
    with col2:
        st.info("**Denominator (Shares)**")
        st.markdown("""
        * **Weighted Average:** Shares are weighted by the time they are outstanding.
        * **Bonus Issue:** Adjusted retrospectively (as if it happened at the start of the earliest period).
        * **Rights Issue:** Includes a 'bonus element' calculation.
        """)

with tab2:
    st.markdown("#### 2. Diluted Earnings Per Share")
    st.write("Diluted EPS adjusts Basic EPS to include the impact of all 'dilutive' potential ordinary shares (e.g., convertible bonds, options).")

    

    st.warning("**The Dilution Test**")
    st.write("Potential ordinary shares are only included if their conversion would **decrease** earnings per share or **increase** loss per share from continuing operations.")
    
    with st.expander("📝 Common Dilutive Instruments"):
        st.markdown("""
        * **Convertible Bonds:** Interest (net of tax) is added back to the numerator; shares are added to the denominator.
        * **Share Options/Warrants:** Only the 'bonus' element (shares issued for no consideration) is added to the denominator.
        * **Contingently Issuable Shares:** Included if the conditions are met at the reporting date.
        """)

with tab3:
    st.markdown("#### 3. Presentation & Retrospective Adjustments")
    
    st.error("**Presentation Rule**")
    st.write("An entity shall present Basic and Diluted EPS in the **Statement of Comprehensive Income**, even if the amounts are negative (a loss per share).")
    
    st.divider()
    
    with st.expander("🔄 Retrospective Adjustments"):
        st.write("""
        If the number of ordinary or potential ordinary shares outstanding increases as a result of a **capitalization, bonus issue, or share split**, the calculation of basic and diluted EPS for all periods presented shall be adjusted retrospectively.
        """)
    
    st.markdown("**Required Disclosures:**")
    st.markdown("""
    1. The **amounts** used as the numerators in calculating basic and diluted EPS.
    2. The **weighted average number** of ordinary shares used as the denominator.
    3. Instruments that could potentially dilute basic EPS in the future but were **not included** because they were anti-dilutive.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 33")