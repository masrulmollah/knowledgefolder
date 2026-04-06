import streamlit as st

# --- PAGE CONFIG & HEADER ---
st.markdown("### 👤 Assessment of Individual")
st.markdown("#### Detailed Summary | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Individual Tax Guide")
menu = st.sidebar.radio("Go to:", 
    ["Thresholds & Slabs", "Salary Exemptions", "Investment Rebate", "Surcharge & Min Tax", "Tax Calculator"])

if menu == "Thresholds & Slabs":
    st.markdown("##### **1. Tax-Free Income Limits (AY 2025-26)**")
    col1, col2 = st.columns(2)
    with col1:
        st.write("- **General:** Tk. 350,000")
        st.write("- **Women/Seniors (65+):** Tk. 400,000")
    with col2:
        st.write("- **Physically Challenged:** Tk. 475,000")
        st.write("- **Freedom Fighters:** Tk. 500,000")

    st.markdown("##### **2. Progressive Tax Slabs**")
    slabs = {
        "Income Slab": ["First Slab (Tax-Free)", "Next 100,000", "Next 400,000", "Next 500,000", "Next 500,000", "Balance"],
        "Rate": ["0%", "5%", "10%", "15%", "20%", "25% - 30%"]
    }
    st.table(slabs)

elif menu == "Salary Exemptions":
    st.markdown("##### **Consolidated Salary Exemption**")
    st.write("The 2023 Act simplified perquisites. House rent, medical, and conveyance allowances are no longer separately exempt.")
    st.info("**Current Rule:** Exemption = Lower of (1/3rd of Total Salary) OR (Tk. 450,000).")
    st.write("Everything else—including bonuses and performance pay—is added to the taxable base.")

elif menu == "Investment Rebate":
    st.markdown("##### **Tax Rebate on Investment (Section 78)**")
    st.write("To qualify for a rebate, you must invest in approved sectors (DPS, Savings Certificates, Life Insurance, Listed Shares).")
    
    st.markdown("**Your Rebate is the LOWER of:**")
    st.success("1. **3%** of Total Taxable Income")
    st.success("2. **15%** of Actual Investment")
    st.success("3. **Tk. 1,000,000** (Maximum Limit)")

elif menu == "Surcharge & Min Tax":
    st.markdown("##### **Surcharge on Net Wealth**")
    st.write("Surcharge is calculated on the total tax payable if your net wealth exceeds Tk. 4 Crore.")
    
    surcharge_data = {
        "Net Wealth Range": ["Up to 4 Crore", "4 Crore to 10 Crore", "10 Crore to 20 Crore", "Above 50 Crore"],
        "Surcharge Rate": ["Nil", "10%", "20%", "35%"]
    }
    st.table(surcharge_data)

    st.markdown("##### **Minimum Tax (By Location)**")
    st.write("- **Dhaka & Chattogram City Corp:** Tk. 5,000")
    st.write("- **Other City Corporations:** Tk. 4,000")
    st.write("- **Outside City Corporations:** Tk. 3,000")

elif menu == "Tax Calculator":
    st.markdown("##### **Individual Tax Estimator**")
    
    salary = st.number_input("Annual Gross Salary (Tk.):", min_value=0.0, value=1200000.0, step=50000.0)
    investment = st.number_input("Total Eligible Investment (Tk.):", min_value=0.0, value=200000.0, step=10000.0)
    
    # Logic: Exemption
    exemption = min(salary / 3, 450000)
    taxable_income = max(0.0, salary - exemption)
    
    # Simplified Rebate Logic
    rebate = min(taxable_income * 0.03, investment * 0.15, 1000000)
    
    st.divider()
    st.write(f"**Estimated Taxable Income:** Tk. {taxable_income:,.0f}")
    st.write(f"**Estimated Investment Rebate:** Tk. {rebate:,.0f}")
    st.caption("Note: This estimator uses simplified logic. Final tax depends on slab-wise calculations and minimum tax rules.")

st.divider()