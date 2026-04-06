import streamlit as st

# --- SUBPAGE HEADER ---
st.header("Income Tax Act 2023: Fundamental Pillars")
st.write("A deep dive into the five most critical definitions that determine tax liability and timing in Bangladesh.")

# --- THE 5 PILLARS ---
st.info("**Finance Lead Perspective:** You cannot calculate a company's tax liability without first confirming the 'Resident' status and identifying the correct 'Assessment Year'.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Assessee", "Assessment Year", "Company", "Income", "Resident"
])

with tab1:
    st.markdown("### 1. Assessee (Section 2, Clause 22)")
    st.write("An 'Assessee' is more than just a taxpayer. It includes any person:")
    st.success("""
    * By whom any tax or other sum of money (fine, interest, penalty) is payable.
    * Against whom any proceeding under this Act has been taken.
    * Who is deemed to be an assessee (e.g., a representative of a non-resident).
    * Who is an 'Assessee in Default' for failing to pay or deduct tax at source.
    """)

with tab2:
    st.markdown("### 2. Assessment Year (Section 2, Clause 9)")
    st.write("The period in which the tax of the previous year is processed.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning("**Income Year**")
        st.write("The 12-month period from **July 1 to June 30** in which income is earned.")
        st.caption("*Banks and Financial Institutions follow January to December.")
    with col2:
        st.error("**Assessment Year**")
        st.write("The 12-month period starting from **July 1** immediately following the Income Year.")

    

with tab3:
    st.markdown("### 3. Company (Section 2, Clause 31)")
    st.write("The 2023 Act has significantly expanded this definition. A 'Company' includes:")
    st.markdown("""
    * Any body corporate formed under the **Companies Act, 1994**.
    * A foreign association or body corporate.
    * A **Permanent Establishment** of a foreign company.
    * Any Statutory Government Authority, Local Authority, or Autonomous Body.
    * **Note:** Trust and Funds are specifically excluded and treated as separate taxable entities.
    """)

with tab4:
    st.markdown("### 4. Income (Section 2, Clause 34)")
    st.write("Income is a broad concept under the Act, covering both actual and deemed receipts.")
    st.info("**Scope includes:**")
    st.markdown("""
    * Any amount chargeable to tax under any provision of the Act.
    * Any amount subject to **Tax Deducted at Source (TDS)**.
    * Any loss of income.
    * **Deemed Income:** Benefits like car usage, free housing, or unexplained cash credits.
    * Profits or gains from business, insurance, or capital assets.
    """)

with tab5:
    st.markdown("### 5. Resident (Section 2, Clause 55)")
    st.write("Residential status determines whether you are taxed on 'Worldwide Income' or only 'Bangladesh-sourced Income'.")

    st.markdown("**For Individuals:**")
    st.code("""
If (Days_in_BD >= 183):
    Status = "Resident"
elif (Days_in_BD >= 90 AND Total_Days_Last_4_Years >= 365):
    Status = "Resident"
else:
    Status = "Non-Resident"
    """, language="python")

    st.markdown("**For Companies:**")
    st.write("A company is resident if it is a **Bangladeshi Company** or its **Control and Management** is situated wholly in Bangladesh.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: Income Tax Act 2023 (Bangladesh)")
st.sidebar.markdown("---")
st.sidebar.write("📅 **Current Context:** As of April 2026, the current Assessment Year for most taxpayers is **2025-2026** (based on income earned from July 2024 to June 2025).")