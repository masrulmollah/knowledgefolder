import streamlit as st
import pandas as pd

# --- STANDARD WEB HEADERS ---
st.markdown("### 🤝 Assessment of Partnership Firms")
st.markdown("#### Provisions under | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Partnership Guide")
menu = st.sidebar.radio("Go to:", ["Legal Status", "Taxation Principles", "Disallowed Expenses", "Firm Tax Calculator"])

if menu == "Legal Status":
    st.markdown("##### **Definition and Registration**")
    st.write("Under the Income Tax Act, 2023, a firm is treated as a separate taxable entity.")
    
    st.markdown("**Key Classifications:**")
    st.write("- **Registered Firm:** A firm registered with the Registrar of Joint Stock Companies and Firms (RJSC).")
    st.write("- **Unregistered Firm:** Treated as an Association of Persons (AOP) for tax purposes.")
    
    st.info("💡 **Finance Tip:** Registration is highly recommended as it provides clarity on the legal standing of the entity and ease of assessment.")

elif menu == "Taxation Principles":
    st.markdown("##### **How Firms are Taxed**")
    st.write("The 2023 Act significantly streamlined the taxation of firms to prevent double taxation.")
    
    st.markdown("**Current Rules:**")
    st.write("1. **Firm Level:** The firm pays tax on its total income at the prevailing corporate rate (typically 27.5% for non-publicly traded entities).")
    st.write("2. **Partner Level:** The share of profit received by a partner from a taxed firm is generally excluded from the partner's individual taxable income.")
    st.write("3. **Losses:** Losses stay within the firm. They cannot be passed on to partners to offset their personal income (Section 70).")

elif menu == "Disallowed Expenses":
    st.markdown("##### **Inadmissible Deductions (Section 55)**")
    st.write("When calculating the 'Business Income' of a firm, the following payments to partners are **added back** to the profit:")
    
    # Data for the table
    disallowed = {
        "Payment Type": ["Salary / Remuneration", "Bonus", "Commission", "Interest on Capital"],
        "Tax Treatment": ["Disallowed (Add back)", "Disallowed (Add back)", "Disallowed (Add back)", "Disallowed (Add back)"]
    }
    st.table(pd.DataFrame(disallowed))
    
    st.warning("These payments are treated as a distribution of profit rather than a business expense.")

elif menu == "Firm Tax Calculator":
    st.markdown("##### **Firm Tax Estimator**")
    
    col1, col2 = st.columns(2)
    with col1:
        net_profit_accounts = st.number_input("Net Profit as per Accounts (Tk.):", min_value=0.0, value=1000000.0, step=50000.0)
        partner_salaries = st.number_input("Salaries paid to Partners (Tk.):", min_value=0.0, value=200000.0, step=10000.0)
    
    with col2:
        partner_interest = st.number_input("Interest paid on Partner Capital:", min_value=0.0, value=50000.0)
        tax_rate = st.slider("Applicable Tax Rate (%)", 20.0, 30.0, 27.5)

    # Calculation
    taxable_income = net_profit_accounts + partner_salaries + partner_interest
    estimated_tax = taxable_income * (tax_rate / 100)

    st.divider()
    st.metric("Total Taxable Income of Firm", f"Tk. {taxable_income:,.0f}")
    st.metric("Estimated Tax Payable", f"Tk. {estimated_tax:,.0f}")
    
    st.caption("Note: This calculation assumes no other adjustments (like depreciation differences or inadmissible cash payments).")

st.divider()