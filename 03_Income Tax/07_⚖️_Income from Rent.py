import streamlit as st
import pandas as pd

def show_rent_income_page():
    # --- STANDARD WEB HEADERS ---
    st.markdown("### 🏠 Income from Rent")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.header("Navigation")
    section = st.sidebar.radio("Select Section:", 
                               ["General Provisions", "Admissible Deductions", "Taxable Rent Calculator"])

    if section == "General Provisions":
        st.markdown("##### **Annual Value (Section 66)**")
        st.write("The basis of calculation is the **Annual Value**, which is defined as the higher of:")
        st.write("1. **Actual Rent:** The total amount received or receivable from the tenant.")
        st.write("2. **Reasonable Rent:** The amount the property would typically fetch in the market (Municipal Value).")
        
        st.info("**Note:** If the owner provides utilities (water, electricity, lift, etc.), the cost of these services should be deducted from the total rent received before determining the Annual Value.")

    elif section == "Admissible Deductions":
        st.markdown("##### **Statutory Deductions (Section 68)**")
        st.write("The following amounts can be deducted from the Annual Value to arrive at the taxable income:")
        
        st.markdown("**1. Repair and Maintenance (Statutory)**")
        st.write("- **25%** of Annual Value for Residential properties.")
        st.write("- **30%** of Annual Value for Commercial/Business properties.")
        
        st.markdown("**2. Other Expenses (On Actual Basis)**")
        st.write("- **Municipal Taxes:** Land development tax and city corporation taxes.")
        st.write("- **Insurance:** Premiums paid to insure the property.")
        st.write("- **Loan Interest:** Interest on capital borrowed for construction or acquisition.")
        st.write("- **Vacancy Allowance:** Deduction for periods where the property was vacant.")

    elif section == "Taxable Rent Calculator":
        st.markdown("##### **Income from Rent Calculator**")
        
        col1, col2 = st.columns(2)
        with col1:
            actual_rent = st.number_input("Annual Actual Rent Received (Tk.):", min_value=0.0, step=10000.0, value=500000.0)
            municipal_val = st.number_input("Annual Municipal Value (Tk.):", min_value=0.0, step=10000.0, value=450000.0)
            prop_type = st.selectbox("Property Category:", ["Residential", "Commercial"])
        
        # Calculate Annual Value
        annual_value = max(actual_rent, municipal_val)
        
        # Calculate Statutory Deduction (Repair/Maintenance)
        repair_rate = 0.25 if prop_type == "Residential" else 0.30
        repair_deduction = annual_value * repair_rate
        
        with col2:
            st.metric("Determined Annual Value", f"Tk. {annual_value:,.0f}")
            st.metric(f"Repair Allowance ({int(repair_rate*100)}%)", f"Tk. {repair_deduction:,.0f}")

        st.divider()
        
        # Additional Deductions
        st.write("**Additional Admissible Expenses:**")
        col3, col4 = st.columns(2)
        with col3:
            muni_tax = st.number_input("Municipal/Land Tax Paid:", min_value=0.0, step=1000.0)
            loan_int = st.number_input("Interest on House Building Loan:", min_value=0.0, step=1000.0)
        with col4:
            ins_prem = st.number_input("Insurance Premium Paid:", min_value=0.0, step=1000.0)
            vacancy = st.number_input("Vacancy Allowance (if any):", min_value=0.0, step=1000.0)

        total_deductions = repair_deduction + muni_tax + loan_int + ins_prem + vacancy
        net_taxable_rent = annual_value - total_deductions

        st.divider()
        st.markdown(f"**Net Taxable Income from Rent: Tk. {max(0, net_taxable_rent):,.0f}**")

    st.write("")
    st.divider()

# Execution
if __name__ == "__main__":
    show_rent_income_page()
else:
    show_rent_income_page()