import streamlit as st

# --- SUBPAGE HEADER ---
st.header("Income Tax Act 2023: Salary Income Computation")
st.write("A streamlined guide to calculating taxable income from employment, reflecting the unified exemption rules of the new Act.")

# --- THE CORE RULE ---
st.info("**The Unified Exemption Rule:** Instead of multiple separate limits, the 2023 Act provides a single exemption on the total salary received.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The Calculation Formula", "Perquisites & Benefits", "Exemptions & Limits"])

with tab1:
    st.markdown("### 1. Step-by-Step Computation")
    st.write("To reach the 'Net Taxable Salary', follow this sequence:")
    
    st.success("**Step A: Gross Salary**")
    st.write("Sum of Basic + House Rent + Medical + Conveyance + Bonus + Leave Encashment + Any other allowance.")
    
    st.warning("**Step B: Apply Unified Exemption**")
    st.markdown("""
    Subtract the **Lesser** of:
    1. **One-third (1/3rd)** of the Total Salary, OR
    2. **BDT 450,000**
    """)
    
    st.error("**Step C: Net Taxable Salary**")
    st.write("Gross Salary minus the Unified Exemption calculated in Step B.")

    

with tab2:
    st.markdown("### 2. Valuation of Perquisites")
    st.write("When an employer provides non-cash benefits, their 'deemed value' is added to your salary.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🚗 Motor Vehicle Facility**")
        st.write("If a car is provided for both personal and office use, the following monthly amounts are added to income:")
        st.table({
            "Engine Capacity": ["Up to 2500cc", "Above 2500cc"],
            "Monthly Addition": ["BDT 10,000", "BDT 25,000"]
        })
    with col2:
        st.markdown("**🏠 Accommodation**")
        st.write("If rent-free accommodation is provided:")
        st.write("- The **Annual Rental Value** is added to the total salary.")
        st.caption("Note: If the employee pays partial rent, only the difference is added.")

    with st.expander("📝 Employee Share Schemes"):
        st.write("""
        If shares are received under an ESOP, the taxable benefit is:
        **Fair Market Value (at date of receipt) - Cost paid by employee.**
        """)

with tab3:
    st.markdown("### 3. Specific Exclusions (Fully Tax-Free)")
    st.write("The following items are NOT included in 'Total Salary' before the 1/3rd exemption is applied:")
    
    st.markdown("""
    * **Medical Expenses:** Reimbursement for surgery (Heart, Kidney, Eye, Liver, Cancer) of a non-shareholder employee.
    * **Group Insurance:** Premiums paid by the employer for the employee.
    * **Government Pension:** Any pension received from the government.
    * **Travel Allowance:** Amounts incurred wholly and necessarily for office duties.
    """)

    st.divider()
    st.markdown("#### The Final Tax Result")
    st.info("Once you have the 'Net Taxable Salary', add your income from other heads (like Bank Interest) and apply the **Tax Slabs** (0% to 30%) to find the Gross Tax Payable.")

# --- SIDEBAR ---
st.sidebar.caption("Reference: Section 32, ITA 2023")
st.sidebar.markdown("---")
st.sidebar.write("💡 **Finance Lead Note:** Ensure your HR payroll system is configured to cap the 1/3rd exemption at BDT 450,000 to avoid under-deducting TDS from employee salaries.")