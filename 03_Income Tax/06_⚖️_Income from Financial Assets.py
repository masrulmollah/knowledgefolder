import streamlit as st

def show_financial_assets_page():
    # Using H3/H4 for titles to keep font sizes within a standard web range
    st.markdown("### ⚖️ Income from Financial Assets Summary")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # Sidebar for Navigation
    st.sidebar.header("Navigation")
    section = st.sidebar.radio("Select Section:", ["Scope", "Deductions", "Exemptions", "Grossing Up Calculator"])

    if section == "Scope":
        st.markdown("##### **Scope of Financial Assets (Section 62)**")
        st.write("Income under this head includes any income received from:")
        st.write("- **Government Securities:** Interest on bonds or treasury bills.")
        st.write("- **Dividends:** Income from shares in companies, mutual funds, or unit funds.")
        st.write("- **Bank Deposits:** Interest from FDRs, DPS, or Savings accounts.")
        st.write("- **Islamic Finance:** Profits from Mudaraba or other Islamic banking products.")
        st.write("- **Savings Certificates:** Interest from Sanchayapatra.")
        st.info("Note: All income from these sources must be reported on a gross basis.")

    elif section == "Deductions":
        st.markdown("##### **Admissible Deductions (Section 64)**")
        st.write("The following expenses are deductible from gross financial income:")
        
        st.write("**1. Bank Charges:** Fees paid to a bank for the collection of interest or dividends.")
        st.write("**2. Interest on Loans:** Interest paid on capital borrowed specifically for making the investment.")

    elif section == "Exemptions":
        st.markdown("##### **Common Exemptions**")
        st.write("Certain financial incomes are excluded from the total taxable income:")
        
        # Using a simple list for cleaner UI than a large table
        st.markdown("""
        * **Wage Earner Development Bond:** Fully Exempt.
        * **Zero-Coupon Bond:** Fully Exempt (for non-corporate taxpayers).
        * **Dividends:** Exempt up to specific thresholds as per the Finance Act.
        """)

    elif section == "Grossing Up Calculator":
        st.markdown("##### **Grossing Up Calculator**")
        st.write("Calculate the gross income to be reported in your tax return.")
        
        # Columns help prevent input fields from being too wide
        col1, col2 = st.columns(2)
        with col1:
            net_income = st.number_input("Net Amount Received (Tk.):", min_value=0.0, step=500.0, value=1000.0)
        with col2:
            tds_rate = st.selectbox("TDS Rate Applied (%):", [5, 10, 15, 20])
        
        if st.button("Calculate"):
            gross_income = net_income / (1 - (tds_rate / 100))
            tax_deducted = gross_income - net_income
            
            st.write(f"**Gross Income to Report:** Tk. {gross_income:,.2f}")
            st.write(f"**Tax Deducted at Source (TDS):** Tk. {tax_deducted:,.2f}")

    # Bottom spacing
    st.write("")
    st.divider()

# Execution logic
if __name__ == "__main__":
    show_financial_assets_page()
else:
    show_financial_assets_page()