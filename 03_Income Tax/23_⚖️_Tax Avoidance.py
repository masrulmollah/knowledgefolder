import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 🛡️ Tax Avoidance")
st.markdown("#### Provisions under (Sections 214–222) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Anti-Avoidance Guide")
menu = st.sidebar.radio("Go to:", 
    ["General Anti-Avoidance", "Non-Resident Transactions", "Asset Transfers", "Securities & Bond Washing"])

if menu == "General Anti-Avoidance":
    st.markdown("##### **Impermissible Tax Avoidance (GAAR)**")
    st.write("The tax authorities can look through the legal form of a transaction to its economic substance.")
    
    st.info("**What is an Impermissible Arrangement?**")
    st.write("- It is created with the main purpose of obtaining a tax benefit.")
    st.write("- It lacks commercial substance.")
    st.write("- It creates rights or obligations which would not normally be created between persons acting at arm's length.")
    
    st.error("Consequence: The tax office can re-characterize the arrangement to negate the tax benefit.")

elif menu == "Non-Resident Transactions":
    st.markdown("##### **Transactions with Non-Residents (Section 214)**")
    st.write("This section prevents profit-shifting to foreign entities.")
    
    st.markdown("**The 'Fair Profit' Rule:**")
    st.write("If a resident entity transacts with a non-resident (like a foreign parent or sister company) and the resident shows 'zero' or 'lower than normal' profits, the DCT has the power to:")
    st.write("1. Disregard the reported figures.")
    st.write("2. Estimate the profit that would have been made in a standard market scenario.")
    
    st.info("💡 **Finance Lead Note:** Ensure all inter-company cross-border charges (Management fees, Royalty, or Raw Material transfers) are backed by a Transfer Pricing study to avoid Section 214 challenges.")

elif menu == "Asset Transfers":
    st.markdown("##### **Transfer of Assets Abroad (Section 215)**")
    st.write("This is designed to prevent 'Income Splitting' using foreign accounts.")
    
    st.write("- **The Scenario:** An individual transfers assets so that the income is received by a person resident outside Bangladesh.")
    st.write("- **The Catch:** If the individual still has the 'power to enjoy' that income (directly or indirectly), it is taxed as their own income in Bangladesh.")
    
    st.warning("This applies even if the transfer was legal, provided the primary goal was tax reduction.")

elif menu == "Securities & Bond Washing":
    st.markdown("##### **Transactions in Securities (Section 216)**")
    st.write("Prevents temporary transfers of securities to avoid tax on interest or dividends.")
    
    st.markdown("**Bond Washing:**")
    st.write("Selling a bond just before interest is due and buying it back after interest is paid. The Act treats that interest as the original owner's income.")
    
    st.markdown("**Dividend Stripping:**")
    st.write("Buying shares just before a dividend and selling them immediately after to claim a capital loss. The Act may disallow such losses if the period of ownership is too short.")

st.divider()