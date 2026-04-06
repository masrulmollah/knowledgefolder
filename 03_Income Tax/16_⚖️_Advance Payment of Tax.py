import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 💰 Advance Payment of Tax")
st.markdown("#### Provisions under (Sections 153–158) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("AIT Navigation")
menu = st.sidebar.radio("Go to:", ["Liability & Threshold", "Installment Dates", "Calculation Logic", "AIT Calculator"])

if menu == "Liability & Threshold":
    st.markdown("##### **Who must pay Advance Tax? (Section 153)**")
    st.write("An assessee is required to pay advance tax if their latest assessed income exceeds a specific threshold.")
    
    st.success("**The Threshold:** Total Income > **Tk. 600,000** (excluding Capital Gains and non-recurring income).")
    
    st.markdown("**Key Conditions:**")
    st.write("- Mandatory if you meet the threshold in the previous assessment year.")
    st.write("- Mandatory for new taxpayers who estimate their current income will exceed the threshold.")
    st.write("- Advance tax is essentially 'Pay As You Earn' to avoid a heavy tax burden at the end of the year.")

elif menu == "Installment Dates":
    st.markdown("##### **Payment Schedule (Section 155)**")
    st.write("Advance tax is payable in four equal installments throughout the financial year.")
    
    # Visualizing the schedule
    st.info("**1st Installment:** On or before **September 15**")
    st.info("**2nd Installment:** On or before **December 15**")
    st.info("**3rd Installment:** On or before **March 15**")
    st.info("**4th Installment:** On or before **June 15**")
    
    st.warning("Late payment or missing an installment may trigger simple interest penalties during the final assessment.")

elif menu == "Calculation Logic":
    st.markdown("##### **How to Compute Advance Tax (Section 154)**")
    st.write("The amount of advance tax payable is the tax on the latest assessed income (or estimated income) minus any tax deducted at source (TDS).")
    
    st.markdown("**Formula:**")
    st.latex(r"Installment = \frac{(Total Estimated Tax - TDS)}{4}")
    
    st.markdown("**Estimation Adjustment:**")
    st.write("If you estimate that your income will be lower than the previous year, you can submit a revised estimate to the Deputy Commissioner of Taxes (DCT) and pay a reduced amount.")

elif menu == "AIT Calculator":
    st.markdown("##### **Quarterly Advance Tax Estimator**")
    st.write("Determine the amount you should pay in each installment.")
    
    col1, col2 = st.columns(2)
    with col1:
        total_tax_est = st.number_input("Estimated Total Tax for the Year (Tk.):", min_value=0.0, value=100000.0, step=5000.0)
        tds_already_paid = st.number_input("Estimated TDS for the Year (Tk.):", min_value=0.0, value=20000.0, step=5000.0)
    
    # Calculation
    net_ait_payable = max(0.0, total_tax_est - tds_already_paid)
    quarterly_installment = net_ait_payable / 4
    
    with col2:
        st.metric("Net Advance Tax Due", f"Tk. {net_ait_payable:,.0f}")
        st.metric("Per Quarter Installment", f"Tk. {quarterly_installment:,.0f}")
    
    st.divider()
    st.caption("Note: Ensure your total advance tax + TDS covers at least 75% of your final tax liability to avoid interest under Section 158.")

st.divider()