import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 📋 Return of Income")
st.markdown("#### Provisions under (Sections 166–184) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Return Filing Guide")
menu = st.sidebar.radio("Go to:", ["Filing Eligibility", "Tax Day & Deadlines", "Universal Self-Assessment", "Penalty for Delay"])

if menu == "Filing Eligibility":
    st.markdown("##### **Who Must File a Return? (Section 166)**")
    st.write("Filing is mandatory if you meet any of the following criteria:")
    st.write("- **Income Threshold:** Total income exceeds the tax-exempt limit (General: Tk. 3,50,000).")
    st.write("- **Asset Ownership:** Ownership of a motor vehicle or a house/apartment in a city corporation.")
    st.write("- **Professional Status:** Holding a trade license, being a member of a professional body (ICAB, ICMAB, etc.), or running for public office.")
    st.write("- **Business Status:** Being a director of a company or a partner in a firm.")
    st.info("Note: All Company taxpayers must file a return regardless of income or loss.")

elif menu == "Tax Day & Deadlines":
    st.markdown("##### **The Concept of 'Tax Day'**")
    st.write("Tax Day is the final deadline for filing your income tax return without needing an extension.")
    
    st.success("**For Individual Taxpayers:** **November 30th** (following the end of the June income year).")
    st.success("**For Companies:** Usually **January 15th** or 6 months after the end of the income year.")
    
    st.markdown("**Extensions:**")
    st.write("Taxpayers can apply for an extension to the Deputy Commissioner of Taxes (DCT) before Tax Day if there is a valid reason for delay.")

elif menu == "Universal Self-Assessment":
    st.markdown("##### **Universal Self-Assessment (Section 167)**")
    st.write("This is the standard filing method under the 2023 Act.")
    st.write("- **Process:** The taxpayer calculates income, applies rebates, deducts TDS/Advance Tax, and pays the balance before filing.")
    st.write("- **Acknowledgment:** The receipt provided by the tax office acts as proof of assessment.")
    st.warning("Ensure all calculations are accurate; the tax department may select returns for 'Audit' to verify the information provided.")

elif menu == "Penalty for Delay":
    st.markdown("##### **Consequences of Late Filing**")
    st.write("Filing after Tax Day without an approved extension triggers several penalties:")
    
    st.error("**1. Financial Penalty:** 10% of the tax payable (Minimum Tk. 1,000).")
    st.error("**2. Delay Interest:** 2% per month interest on the unpaid tax amount.")
    st.error("**3. Loss of Benefits:** Late filers may lose certain investment rebates or the ability to carry forward losses.")
    
    st.write("")
    st.info("💡 **Finance Lead Note:** Always aim to file by November 30th to maintain a clean compliance record for the company and personal records.")

st.divider()