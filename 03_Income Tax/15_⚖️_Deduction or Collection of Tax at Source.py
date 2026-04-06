import streamlit as st
import pandas as pd

# --- STANDARD WEB HEADERS ---
st.markdown("### 📝 Deduction & Collection of Tax at Source")
st.markdown("#### Provisions under (Sections 86–145) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("TDS Explorer")
menu = st.sidebar.radio("Go to:", ["General Principles", "Common TDS Rates", "Compliance & Returns", "TDS Calculator"])

if menu == "General Principles":
    st.markdown("##### **Fundamentals of Withholding Tax**")
    st.write("Withholding tax is a mechanism where the payer deducts a portion of the payment and remits it directly to the government on behalf of the payee.")
    
    st.markdown("**Key Responsibilities:**")
    st.write("- **Who must deduct:** Companies, firms, NGOs, and government agencies (Defined as 'Responsible Persons').")
    st.write("- **When to deduct:** At the time of making the payment or at the time of credit to the account, whichever is earlier.")
    st.error("**Risk of Non-Compliance:** Failure to deduct or deposit tax results in the related expense being disallowed for the deductor under Section 55.")

elif menu == "Common TDS Rates":
    st.markdown("##### **Major TDS Rates at a Glance**")
    
    # Data for the table
    tds_data = {
        "Nature of Payment": ["Salaries", "Suppliers (General)", "Professional Fees", "House Property Rent", "Bank Interest (with e-TIN)", "Dividends (Individual)"],
        "Section": ["Sec 86", "Sec 89", "Sec 90", "Sec 93", "Sec 102", "Sec 116"],
        "Standard Rate": ["Average Rate", "2% - 7%", "10% - 15%", "5%", "10%", "10% - 15%"]
    }
    df = pd.DataFrame(tds_data)
    st.table(df)
    st.caption("Rates may vary based on thresholds and specific SROs. Non-E-TIN holders often face 50% higher rates.")

elif menu == "Compliance & Returns":
    st.markdown("##### **Reporting & Deposit Deadlines**")
    st.write("The 2023 Act has simplified the filing process for withholding entities.")
    
    st.info("**Monthly TDS Return:** All deductors are required to file a monthly statement/return of tax deducted at source.")
    
    st.markdown("**Deposit Timeline:**")
    st.write("- Generally, tax must be deposited via Automated Challan (A-Challan) within **7 days** of the end of the month in which deduction was made.")
    st.write("- During the month of June, the timeline is tighter (usually within 24 hours of deduction).")
    
    st.markdown("**Certificate of Deduction:**")
    st.write("The deductor must issue a TDS Certificate to the payee within 15 days of the following month to allow the payee to claim tax credit.")

elif menu == "TDS Calculator":
    st.markdown("##### **Simple TDS Estimator**")
    
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Select Payment Category", 
                                ["Professional/Technical Fee", "Supplier Payment", "Rent", "Contractor"])
        bill_amount = st.number_input("Gross Bill Amount (Tk.):", min_value=0.0, value=100000.0, step=10000.0)
    
    # Simple logic mapping
    rates_map = {"Professional/Technical Fee": 0.10, "Supplier Payment": 0.03, "Rent": 0.05, "Contractor": 0.05}
    selected_rate = rates_map[category]
    
    tds_amount = bill_amount * selected_rate
    net_payable = bill_amount - tds_amount
    
    with col2:
        st.metric("TDS Amount", f"Tk. {tds_amount:,.0f}")
        st.metric("Net Payable to Party", f"Tk. {net_payable:,.0f}")
    
    st.divider()
    st.warning(f"Note: This is an estimate based on a {selected_rate*100:.1f}% rate. Actual rates depend on cumulative payment thresholds.")

st.divider()