import streamlit as st

# --- SUBPAGE HEADER ---
st.header("Income Tax Act 2023: Surcharge & Minimum Tax")
st.write("A summary of the wealth-based Surcharge for individuals and the 'Gross Receipts' Minimum Tax for companies in Bangladesh.")

# --- THE CORE CONCEPTS ---
st.info("**Strategic Insight:** Minimum Tax is calculated on 'Gross Receipts,' meaning even if your factory makes a loss, you may still owe tax to the NBR.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Surcharge (Individual)", "Minimum Tax (Corporate)", "TDS as Minimum Tax"])

with tab1:
    st.markdown("### 1. Surcharge on Wealth (Individual)")
    st.write("Surcharge is not a tax on income, but a tax on the **Total Tax Payable** based on the net wealth declared in the 'Asset & Liability' statement.")
    
    st.table({
        "Net Wealth Threshold (BDT)": [
            "Up to 4 Crore", 
            "4 Crore to 10 Crore", 
            "10 Crore to 20 Crore", 
            "20 Crore to 50 Crore", 
            "Above 50 Crore"
        ],
        "Surcharge Rate (% of Tax Payable)": ["0%", "10%", "20%", "30%", "35%"]
    })
    
    st.warning("**Mandatory Surcharge:** If an individual owns more than one car or a house property exceeding 8,000 sq. ft. in a City Corporation, a minimum 10% surcharge applies regardless of wealth threshold.")

with tab2:
    st.markdown("### 2. Minimum Tax (Section 163)")
    st.write("Every company and certain individuals (with gross receipts > BDT 30 Lakh) must pay a minimum tax based on their turnover.")
    
    st.markdown("#### Minimum Tax Rates on Gross Receipts")
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**General Rates**")
        st.markdown("""
        * **General Company:** 0.60% 
        * **Publicly Traded Company:** 0.60%
        * **Individual (Non-Company):** 0.25%
        """)
        
    with col2:
        st.error("**Special Sector Rates**")
        st.markdown("""
        * **Tobacco Manufacturers:** 1.00%
        * **Mobile Phone Operators:** 2.00%
        * **Carbonated Beverage:** 3.00% - 5.00%
        """)

    with st.expander("📝 Definition of 'Gross Receipts'"):
        st.write("""
        Includes all receipts from sale of goods, services, rental income, 
        and any other incidental income before deducting any expenses.
        """)

with tab3:
    st.markdown("### 3. TDS as Minimum Tax")
    st.write("Under the 2023 Act, Tax Deducted at Source (TDS) on certain transactions is treated as the **Final Discharge of Tax Liability** (Minimum Tax).")
    
    st.markdown("**Common Sources treated as Minimum Tax:**")
    st.markdown("""
    1. **Section 89:** Supply of goods or execution of contracts (TDS on invoices).
    2. **Section 102:** Interest on bank deposits/savings.
    3. **Section 105:** Cash incentives for exports.
    4. **Section 124:** Income from property (Rent).
    """)

    st.divider()
    st.markdown("#### The Comparison Rule")
    st.error("**The Rule of 'Higher of Three'**")
    st.write("A company's final tax liability is the **HIGHEST** of:")
    st.markdown("""
    1. Regular Tax (e.g., 27.5% of Net Profit).
    2. Minimum Tax on Gross Receipts (e.g., 0.60% of Turnover).
    3. Total TDS deducted from the company's income during the year.
    """)

# --- SIDEBAR ---
st.sidebar.caption("Reference: Section 163, ITA 2023")
st.sidebar.markdown("---")
st.sidebar.write("💡 **Finance Lead Note:** If your factory margin is thin (e.g., < 2.5%), your 0.60% Minimum Tax on Turnover might actually exceed your 27.5% Tax on Profit.")