import streamlit as st
import pandas as pd

def show_business_income_page():
    # --- STANDARD WEB HEADERS ---
    st.markdown("### 🏭 Income from Business")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.header("Navigation")
    section = st.sidebar.radio("Select Section:", 
                               ["Scope & Principles", "Allowable Expenses", "Inadmissible Expenses", "Profit Calculator"])

    if section == "Scope & Principles":
        st.markdown("##### **Scope of Business Income (Section 45)**")
        st.write("Income under this head includes profits and gains from any business, profession, or vocation. Key components include:")
        st.write("- **Trading Profits:** Gains from the sale of goods or services.")
        st.write("- **Business Benefits:** The value of any perquisite or benefit derived from the business.")
        st.write("- **Incentives:** Cash subsidies or export incentives received from the government.")
        st.write("- **Management Fees:** Income from managing agencies or professional services.")

    elif section == "Allowable Expenses":
        st.markdown("##### **Admissible Deductions (Section 46)**")
        st.write("Expenses must be incurred **wholly and exclusively** for business purposes to be deductible.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Operational Costs**")
            st.write("- Rent and local rates for premises.")
            st.write("- Repairs and insurance for assets.")
            st.write("- Salaries and wages for staff.")
        with col2:
            st.markdown("**Financial & Technical**")
            st.write("- Interest on business loans.")
            st.write("- Bad debts written off.")
            st.write("- Scientific research expenses.")
        
        st.info("**Depreciation:** Allowance for wear and tear of machinery, buildings, and vehicles is calculated based on the Third Schedule rates.")

    elif section == "Inadmissible Expenses":
        st.markdown("##### **Non-Deductible Expenses (Section 55)**")
        st.write("The following cannot be deducted from business income:")
        st.error("- **Personal Expenses:** Any private or personal spending.")
        st.error("- **Capital Expenditure:** Costs for acquiring long-term assets.")
        st.error("- **Non-Banking Payments:** Payments exceeding statutory limits made in cash.")
        st.error("- **Taxes:** Any income tax or tax on profits.")
        st.error("- **Provisions:** General reserves or provisions (except specific bad debts).")

    elif section == "Profit Calculator":
        st.markdown("##### **Business Profit Estimator**")
        
        col1, col2 = st.columns(2)
        with col1:
            gross_profit = st.number_input("Gross Profit (Tk.):", min_value=0.0, step=10000.0, value=1000000.0)
            other_income = st.number_input("Other Business Income (Tk.):", min_value=0.0, value=0.0)
        
        total_revenue = gross_profit + other_income
        
        with col2:
            oper_exp = st.number_input("Total Operating Expenses:", min_value=0.0, value=400000.0)
            depreciation = st.number_input("Depreciation Allowance:", min_value=0.0, value=50000.0)
        
        # Calculate Net Business Income
        net_business_income = total_revenue - (oper_exp + depreciation)

        st.divider()
        st.metric("Total Revenue", f"Tk. {total_revenue:,.0f}")
        st.metric("Total Deductions", f"Tk. {oper_exp + depreciation:,.0f}")
        
        st.divider()
        st.markdown(f"**Net Taxable Business Income: Tk. {max(0.0, net_business_income):,.0f}**")

    st.write("")
    st.divider()

# Execution logic for multi-page structure
if __name__ == "__main__":
    show_business_income_page()
else:
    show_business_income_page()