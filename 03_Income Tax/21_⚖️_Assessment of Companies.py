import streamlit as st
import pandas as pd

# --- STANDARD WEB HEADERS ---
st.markdown("### 🏢 Assessment of Companies")
st.markdown("#### Provisions under | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Corporate Tax Guide")
menu = st.sidebar.radio("Go to:", 
    ["Tax Rates", "Compliance Requirements", "CSR Tax Rebate", "Minimum Tax (Sec 163)", "Corporate Tax Calculator"])

if menu == "Tax Rates":
    st.markdown("##### **Corporate Income Tax Slabs (AY 2025-26)**")
    st.write("Tax rates vary based on the listing status and compliance with cashless transaction rules.")
    
    rates_data = {
        "Type of Company": ["Publicly Traded", "Non-Publicly Traded", "One Person Company (OPC)", "Bank/Insurance/FI", "Tobacco Manufacturers"],
        "Base Rate": ["22.5%", "27.5%", "22.5%", "37.5%", "45.0%"],
        "Reduced Rate*": ["20.0%", "25.0%", "20.0%", "N/A", "N/A"]
    }
    st.table(pd.DataFrame(rates_data))
    st.caption("*Reduced rates apply if all income/receipts and expenditures over Tk. 5 Lakh are handled via bank transfers.")

elif menu == "Compliance Requirements":
    st.markdown("##### **Mandatory Filing & Audits**")
    st.write("- **Audit Report:** Companies MUST submit audited financial statements verified via the Document Verification System (DVS).")
    st.write("- **Return Deadline:** Usually **January 15th** or 6 months from the end of the income year.")
    st.write("- **TDS Compliance:** Companies are 'Responsible Persons' for withholding tax. Non-compliance leads to disallowance of expenses.")
    st.info("💡 **Finance Lead Note:** Ensure all utility payments and contractor bills are paid via banking channels to qualify for the 2.5% tax rate reduction.")

elif menu == "CSR Tax Rebate":
    st.markdown("##### **Corporate Social Responsibility (Section 79)**")
    st.write("Companies can claim a tax credit for spending on approved social causes.")
    
    st.success("**Rebate Amount:** 10% of the actual CSR expenditure.")
    
    st.markdown("**Investment Limits (The Lower of):**")
    st.write("1. **20%** of the company's total income.")
    st.write("2. **Tk. 12 Crore** (Statutory Cap).")
    
    st.markdown("**Approved CSR Sectors:**")
    st.write("- Education & Healthcare for the underprivileged.")
    st.write("- Climate change and environmental protection.")
    st.write("- Disaster relief and Prime Minister's Relief Fund.")
    st.write("- Digital Bangladesh and ICT training.")
    
    st.warning("Note: Contribution must be made through banking channels, and the company must not be a tax defaulter.")

elif menu == "Minimum Tax (Sec 163)":
    st.markdown("##### **Minimum Tax on Gross Receipts**")
    st.write("Even if a company incurs a loss, it may be liable for Minimum Tax.")
    
    min_tax_data = {
        "Category": ["General Company", "Manufacturer of Cigarettes", "Mobile Phone Operators", "New Industrial Units (first 3 years)"],
        "Rate on Gross Receipts": ["0.60%", "1.00%", "2.00%", "0.10%"]
    }
    st.table(pd.DataFrame(min_tax_data))
    st.warning("The actual tax liability is the HIGHER of the 'Regular Tax' or the 'Minimum Tax'.")

elif menu == "Corporate Tax Calculator":
    st.markdown("##### **Corporate Tax Estimator**")
    
    col1, col2 = st.columns(2)
    with col1:
        net_profit = st.number_input("Net Profit before Tax (Tk.):", min_value=0.0, value=10000000.0, step=100000.0)
        csr_spent = st.number_input("CSR Expenditure (Tk.):", min_value=0.0, value=500000.0)
    
    with col2:
        gross_receipts = st.number_input("Total Gross Receipts (Tk.):", min_value=0.0, value=50000000.0)
        comp_type = st.selectbox("Company Status", ["Non-Publicly Traded", "Publicly Traded", "OPC"])

    # Basic Calculation Logic
    base_rate = 0.275 if comp_type == "Non-Publicly Traded" else 0.225
    tax_before_rebate = net_profit * base_rate
    
    # CSR Rebate calculation
    eligible_csr = min(csr_spent, net_profit * 0.20, 120000000)
    csr_rebate = eligible_csr * 0.10
    
    regular_tax = tax_before_rebate - csr_rebate
    min_tax = gross_receipts * 0.006
    final_tax = max(regular_tax, min_tax)

    st.divider()
    st.metric("Total Tax before Rebate", f"Tk. {tax_before_rebate:,.0f}")
    st.metric("CSR Tax Rebate (10%)", f"Tk. {csr_rebate:,.0f}")
    
    st.subheader(f"Final Tax Liability: Tk. {final_tax:,.0f}")
    st.caption(f"Calculation based on a {base_rate*100:.1f}% base rate and 0.6% Minimum Tax.")

st.divider()