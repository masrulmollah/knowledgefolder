import streamlit as st

def show_agri_income_page():
    # --- STANDARD HEADERS ---
    st.markdown("### 🌾 Income from Agriculture Summary")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # --- NAVIGATION ---
    st.sidebar.header("Sections")
    menu = st.sidebar.radio("Go to:", ["Scope", "Deductions", "Tax Calculator"])

    if menu == "Scope":
        st.markdown("##### **Scope of Agricultural Income (Section 64)**")
        st.write("This includes income derived from land in Bangladesh used for agriculture:")
        st.write("- **Rent or Revenue:** From leasing agricultural land.")
        st.write("- **Cultivation:** From the sale of crops, flowers, or seeds.")
        st.write("- **Processing:** Making produce fit for market (e.g., threshing, winnowing).")
        st.write("- **Buildings:** Income from farmhouses used for agricultural operations.")
        st.info("Note: Specialist farming like Fisheries or Poultry often follows separate SRO rates.")

    elif menu == "Deductions":
        st.markdown("##### **Admissible Deductions (Section 65)**")
        st.write("The following expenses can be subtracted from the gross income:")
        
        # Highlighting the important 60% rule
        st.success("**The 60% Production Cost Rule**")
        st.write("If you do not maintain formal books of accounts, a flat **60%** of the market value of the produce is allowed as a deduction for production costs.")
        
        st.markdown("**Other Admissible Expenses:**")
        st.write("- **Taxes:** Land development tax and local government rates.")
        st.write("- **Interest:** On loans taken for land improvement or operations.")
        st.write("- **Maintenance:** Costs for irrigation, embankments, and protective works.")
        st.write("- **Insurance:** Premiums for crops or livestock.")

    elif menu == "Tax Calculator":
        st.markdown("##### **Agricultural Income Estimator**")
        
        col1, col2 = st.columns(2)
        with col1:
            gross_val = st.number_input("Market Value of Produce (Tk.):", min_value=0.0, step=1000.0, value=100000.0)
            has_books = st.checkbox("I maintain formal books of accounts")
        
        # Calculation logic
        if not has_books:
            prod_cost = gross_val * 0.60
            st.write(f"Statutory Deduction (60%): **Tk. {prod_cost:,.0f}**")
        else:
            prod_cost = st.number_input("Enter Actual Production Cost (Tk.):", min_value=0.0)

        with col2:
            land_tax = st.number_input("Land Tax/Local Rates Paid:", min_value=0.0)
            loan_int = st.number_input("Interest on Agri Loans:", min_value=0.0)

        total_deductions = prod_cost + land_tax + loan_int
        net_income = gross_val - total_deductions

        st.divider()
        st.markdown(f"**Net Taxable Agricultural Income: Tk. {max(0.0, net_income):,.0f}**")
        
        if net_income <= 200000:
            st.caption("Note: Up to Tk. 200,000 may be non-assessable for certain individuals.")

    st.divider()

# Logic to run within your main app structure
if __name__ == "__main__":
    show_agri_income_page()
else:
    show_agri_income_page()