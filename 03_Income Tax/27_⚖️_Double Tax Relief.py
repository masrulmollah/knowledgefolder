import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 🌍 Double Taxation Relief Summary")
st.markdown("#### Provisions under (Sections 223–232) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Global Tax Guide")
menu = st.sidebar.radio("Go to:", 
    ["DTAA Framework", "Unilateral Relief", "Methods of Relief", "Tax Credit Calculator"])

if menu == "DTAA Framework":
    st.markdown("##### **Avoidance of Double Taxation (Section 223)**")
    st.write("Bangladesh has signed Double Taxation Avoidance Agreements (DTAA) with over 35 countries (including the UK, India, USA, and Singapore).")
    
    st.info("**Objectives of DTAA:**")
    st.write("- **Prevention:** Ensuring income isn't taxed twice.")
    st.write("- **Investment:** Encouraging foreign direct investment (FDI) by providing tax certainty.")
    st.write("- **Information Exchange:** Cooperating with foreign tax powers to stop money laundering and evasion.")
    
    st.markdown("**The Tie-Breaker Rule:**")
    st.write("If an individual is considered a resident in both countries, DTAAs provide 'tie-breaker' rules (Permanent home, Center of vital interests, etc.) to determine the primary taxing country.")

elif menu == "Unilateral Relief":
    st.markdown("##### **Relief in Absence of Agreement (Section 226)**")
    st.write("What if Bangladesh does NOT have a treaty with a country?")
    
    st.success("**The Resident's Protection:**")
    st.write("If a resident of Bangladesh proves they have paid tax in a foreign country on income originating there, they are entitled to relief in Bangladesh.")
    
    st.markdown("**Key Conditions:**")
    st.write("1. The taxpayer must be a Resident of Bangladesh.")
    st.write("2. The income must have been taxed in the foreign country.")
    st.write("3. The relief is limited to the lower of the foreign tax paid or the Bangladesh tax on that specific income.")

elif menu == "Methods of Relief":
    st.markdown("##### **Common Relief Methods**")
    
    tab1, tab2 = st.tabs(["Tax Credit Method", "Exemption Method"])
    
    with tab1:
        st.write("**The Credit Method:**")
        st.write("The foreign tax is treated as a payment toward your total tax liability in Bangladesh.")
        st.write("*Example:* If you owe Tk. 100 in BD but paid Tk. 30 in the UK, you only pay Tk. 70 in BD.")
        
    with tab2:
        st.write("**The Exemption Method:**")
        st.write("Specific income types (e.g., foreign dividends) are completely ignored by one of the countries as per the treaty terms.")

    st.info("💡 **Finance Lead Note:** For multinational operations, always check the specific DTAA for 'Withholding Tax' rates on Royalties and Technical Service Fees, as these are often lower than the standard 15-20% rates in the Income Tax Act.")

elif menu == "Tax Credit Calculator":
    st.markdown("##### **Foreign Tax Credit Estimator**")
    st.write("Calculate how much foreign tax you can offset against your Bangladesh tax.")
    
    col1, col2 = st.columns(2)
    with col1:
        foreign_income = st.number_input("Foreign Income (Tk.):", min_value=0.0, value=500000.0)
        foreign_tax_paid = st.number_input("Tax Paid Abroad (Tk.):", min_value=0.0, value=75000.0)
    
    with col2:
        bd_tax_rate = st.slider("Your Bangladesh Tax Rate (%)", 5.0, 30.0, 25.0)

    # Calculation
    max_allowable_credit = foreign_income * (bd_tax_rate / 100)
    actual_credit = min(foreign_tax_paid, max_allowable_credit)
    
    st.divider()
    st.metric("Max Relief Allowed in BD", f"Tk. {max_allowable_credit:,.0f}")
    st.metric("Actual Tax Credit Claimable", f"Tk. {actual_credit:,.0f}")
    
    if foreign_tax_paid > max_allowable_credit:
        st.warning(f"Note: Tk. {foreign_tax_paid - max_allowable_credit:,.0f} of foreign tax cannot be claimed as credit because it exceeds the Bangladesh tax rate.")

st.divider()