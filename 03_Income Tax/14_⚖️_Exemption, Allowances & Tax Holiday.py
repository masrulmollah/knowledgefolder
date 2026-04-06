import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 🛡️ Exemption and Allowances")
st.markdown("#### Tax Holidays & Special Concessions")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Exemption Explorer")
menu = st.sidebar.radio("Go to:", 
                        ["Tax Holiday Info", "Exempted Income", "Investment Rebates", "Special Concessions"])

if menu == "Tax Holiday Info":
    st.markdown("##### **Newly Established Industrial Undertakings**")
    st.write("The Government provides tax holidays to encourage industrialization in specific sectors.")
    st.info("**Key Sectors:** Automobiles, Active Pharmaceutical Ingredients (API), Renewable Energy, and ICT.")
    
    st.markdown("**Compliance Checklist:**")
    st.write("- Must be a Company incorporated in Bangladesh.")
    st.write("- Registration with BIDA or relevant authority is mandatory.")
    st.write("- Must maintain books of accounts as per Section 73.")
    st.warning("Violation of any condition can lead to the withdrawal of the holiday status by the tax authorities.")

elif menu == "Exempted Income":
    st.markdown("##### **Exclusions from Total Income (Sixth Schedule)**")
    st.write("Certain incomes are excluded from 'Total Income' for tax purposes:")
    st.write("- **Agriculture:** Income up to Tk. 200,000 for specific individual farmers.")
    st.write("- **Remittance:** Foreign remittances sent through legal banking channels.")
    st.write("- **Pensions:** Income from government-approved pension funds.")
    st.write("- **IT Services:** Income from IT-enabled services (subject to SRO conditions).")

elif menu == "Investment Rebates":
    st.markdown("##### **Tax Credit on Investments (Section 78)**")
    st.write("Resident individuals can reduce tax liability through eligible investments.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Eligible Investments:**")
        st.write("- Life Insurance Premiums")
        st.write("- DPS (up to Tk. 60,000)")
        st.write("- Govt Savings Certificates")
        st.write("- Benevolent Fund/Group Insurance")
    
    with col2:
        st.markdown("**Calculation Logic:**")
        st.write("Rebate is generally the **lower** of:")
        st.write("1. 3% of Total Taxable Income")
        st.write("2. 15% of Actual Investment")
        st.write("3. Tk. 1,000,000 (Statutory Cap)")

elif menu == "Special Concessions":
    st.markdown("##### **Export & Economic Zones**")
    st.write("- **Export Income:** 50% of income from export is typically exempted for certain entities.")
    st.write("- **Economic Zones:** Expatriate employees in EZs may enjoy a 50% tax exemption for the first 3 years.")
    st.write("- **Grants:** Capital grants for asset acquisition are treated specifically under depreciation rules.")

# Bottom Spacing
st.write("")
st.divider()