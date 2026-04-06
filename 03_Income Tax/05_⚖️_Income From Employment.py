import streamlit as st
import pandas as pd

def show_employment_income_page():
    # --- STANDARD WEB HEADERS ---
    st.markdown("### 💼 Income from Employment")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.header("Navigation")
    section = st.sidebar.radio("Select Section:", 
                               ["Quick Summary", "Salary Components Search", "Detailed Rules", "Taxable Income Calculator"])

    # --- DATA PREPARATION FOR SEARCH TABLE ---
    salary_items = {
        "Description": [
            "1. Basic salary", "2. Dearness allowance", "3. Bonus", "4. Commission and fees", 
            "5. Advance salary", "6. Arrear salary", "7. Leave encashment", "8. Approved Pension", 
            "9. Approved Gratuity", "10. Annuity", "11. Profit in lieu of salary", "12. Profit in addition to salary", 
            "13. Education allowance for children", "14. Employer's contribution to RPF", 
            "15. Employer's contribution to employee's life insurance policy", "16. Entertainment allowance", 
            "17. Medical allowance", "18. Traveling allowance", "19. Special allowance", 
            "20. House rent allowance", "21. Rent free accommodation", "22. Accommodation at concessional rate", 
            "23. Conveyance allowance", "24. Transport / conveyance facility", "26. Free tea, coffee or beverage", 
            "27. Free dress, telephone, power, gas in office", "28. Servant allowance", "29. Compensation", 
            "30. Charge allowance", "31. Overtime", "32. Residence utility/club bills reimbursed", 
            "33. Group insurance premium paid by employer"
        ],
        "Tax Treatment": [
            "Full", "Full", "Full", "Full", "Full", 
            "Full (if not taxed in earlier years)", "Full", "Nothing (Fully tax free)", 
            "Amount exceeding Tk. 2.5 Crore", "Full", "Full", "Full", "Full", "Full", "Full", "Full", 
            "Full (Except specific surgery/cancer treatments)", "Unspent amount", "Nothing (if spent for official purpose)", 
            "Full", "Annual value", "Difference between annual value and amount paid by employee", 
            "Full", "Tiered by CC (Tk. 15k to 50k per month)", "Nothing", "Full", "Full", "Full", 
            "Fully tax free (if spent for office)", "Full", "Full", "Nothing"
        ]
    }
    df = pd.DataFrame(salary_items)

    if section == "Quick Summary":
        st.markdown("##### **Scope & Key Principles**")
        st.write("Income under this head includes any remuneration due or received from an employer.")
        st.info("**The Universal Exemption Rule:** The taxable amount is the total gross income minus the **lower** of: 1/3rd of total income OR Tk. 4,50,000.")
        
        st.markdown("##### **Core Components**")
        st.write("- **Fixed Pay:** Basic, Bonus, and Allowances.")
        st.write("- **Perquisites:** Non-cash benefits like housing or cars.")
        st.write("- **Retirement:** Gratuity, Pension, and Provident Fund contributions.")

    elif section == "Salary Components Search":
        st.markdown("##### **Searchable Tax Treatment Table**")
        st.write("Use the search box below to check the taxability of specific salary items.")
        
        search_query = st.text_input("🔍 Search component (e.g. 'Rent', 'Pension', 'Medical'):")
        
        if search_query:
            display_df = df[df['Description'].str.contains(search_query, case=False)]
        else:
            display_df = df
            
        st.table(display_df)

    elif section == "Detailed Rules":
        st.markdown("##### **Specific Valuation Rules**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🚗 Transport Facility (Item 24)**")
            st.write("Monthly additions based on Engine Capacity:")
            transport_data = {
                "Engine Capacity": ["Up to 1500cc", "1501-2000cc", "2001-2500cc", "Above 2500cc"],
                "Monthly Addition (Tk.)": ["15,000", "20,000", "30,000", "50,000"]
            }
            st.dataframe(transport_data, hide_index=True)

        with col2:
            st.markdown("**🏥 Medical Exemptions (Item 17)**")
            st.write("Medical allowance is taxable EXCEPT for:")
            st.success("""
            * Heart, Kidney, Eye, Liver, and Brain Operations.
            * Replacement of artificial body parts.
            * Cancer treatment.
            """)
        
        st.divider()
        st.markdown("**🏠 Housing Facility (Items 21 & 22)**")
        st.write("- **Rent-Free:** The annual rental value is added to income.")
        st.write("- **Concessional Rate:** The difference between the annual value and the amount paid by the employee is added.")

    elif section == "Taxable Income Calculator":
        st.markdown("##### **Income Estimator**")
        col1, col2 = st.columns(2)
        with col1:
            basic = st.number_input("Annual Basic Salary:", min_value=0.0, step=10000.0, value=600000.0)
            other_taxable = st.number_input("Other Taxable Allowances/Bonus:", min_value=0.0, step=10000.0, value=300000.0)
        
        total_gross = basic + other_taxable
        exemption = min((total_gross / 3), 450000)
        taxable_total = total_gross - exemption
        
        with col2:
            st.metric("Total Gross Income", f"Tk. {total_gross:,.0f}")
            st.metric("Standard Exemption", f"Tk. {exemption:,.0f}")
        
        st.divider()
        st.markdown(f"**Final Taxable Income: Tk. {taxable_total:,.0f}**")

    st.write("")
    st.divider()

# Execution
if __name__ == "__main__":
    show_employment_income_page()
else:
    show_employment_income_page()