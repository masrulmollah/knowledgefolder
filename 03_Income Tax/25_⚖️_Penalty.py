import streamlit as st
import pandas as pd

# --- STANDARD WEB HEADERS ---
st.markdown("### ⚠️ Summary of Penalties")
st.markdown("#### Provisions under (Sections 266–283) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Compliance Monitor")
menu = st.sidebar.radio("Go to:", 
    ["Filing & Payment Defaults", "Concealment & Evasion", "Documentation Defaults", "Penalty Estimator"])

if menu == "Filing & Payment Defaults":
    st.markdown("##### **Delay in Return Filing (Section 266)**")
    st.write("Missing the 'Tax Day' deadline triggers immediate financial consequences.")
    
    st.error("**The Penalty Structure:**")
    st.write("- **Primary Penalty:** 10% of the tax payable on the last assessed income.")
    st.write("- **Minimum Amount:** Tk. 1,000.")
    st.write("- **Continuing Default:** Tk. 50 for every day the delay continues.")
    
    st.info("**Payment Default:** Failure to pay tax due with the return (Section 173) can lead to a penalty of 10% of the unpaid amount.")

elif menu == "Concealment & Evasion":
    st.markdown("##### **Concealment of Income (Section 269)**")
    st.write("Deliberate attempts to hide income or claim fraudulent expenses carry heavy surcharges.")
    
    st.warning("**Standard Penalty:** 15% of the tax sought to be evaded.")
    st.write("- This applies to 'unexplained' investments, cash, or assets found during an audit.")
    st.write("- In extreme cases, this can lead to criminal prosecution (Chapter 25).")
    
    st.markdown("##### **Default in Advance Tax (Section 271)**")
    st.write("If total Advance Tax + TDS is less than 75% of the final tax, simple interest is charged at the prescribed rate (usually 10% per annum) on the shortfall.")

elif menu == "Documentation Defaults":
    st.markdown("##### **Non-Compliance with Records**")
    
    # Data for standard penalties
    data = {
        "Nature of Default": [
            "Failure to keep/maintain accounts", 
            "Non-compliance with Summons/Notice", 
            "Failure to verify DVS (Companies)",
            "Failure to use Banking Channel"
        ],
        "Max Penalty Limit": [
            "Tk. 20,000", 
            "Tk. 5,000", 
            "Tk. 50,000", 
            "Disallowance of Expense"
        ],
        "Section": ["Sec 275", "Sec 267", "Sec 280", "Sec 55"]
    }
    st.table(pd.DataFrame(data))
    
    st.info("💡 **Finance Lead Note:** For factory accounts, ensuring that the 'Document Verification System (DVS)' code is correctly generated for the audit report is now a high-priority compliance item.")

elif menu == "Penalty Estimator":
    st.markdown("##### **Late Filing Penalty Estimator**")
    st.write("Calculate the estimated penalty for missing the Tax Day deadline.")
    
    col1, col2 = st.columns(2)
    with col1:
        last_tax = st.number_input("Tax Paid in Last Assessment (Tk.):", min_value=0.0, value=50000.0)
        days_late = st.number_input("Number of Days Late:", min_value=0, step=1)
    
    # Calculation
    base_penalty = max(1000.0, last_tax * 0.10)
    daily_fine = days_late * 50
    total_penalty = base_penalty + daily_fine
    
    with col2:
        st.metric("Base Penalty (10%)", f"Tk. {base_penalty:,.0f}")
        st.metric("Daily Accumulation (Tk. 50/day)", f"Tk. {daily_fine:,.0f}")
    
    st.divider()
    st.subheader(f"Estimated Total Penalty: Tk. {total_penalty:,.0f}")
    st.caption("Note: This is an estimation. The DCT has the final authority to determine the penalty based on the circumstances.")

st.divider()