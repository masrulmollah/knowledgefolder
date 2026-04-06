import streamlit as st

# --- SUBPAGE HEADER ---
st.header("Income Tax Act: Tax Rate Summary (2025-2027)")
st.write("A quick reference guide for Individual and Corporate tax rates, including specific rules for Dividends and Capital Gains.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Individual Slabs", "Corporate Rates", "Dividends & Capital Gains"])

with tab1:
    st.markdown("### 1. Individual Income Tax Slabs (Resident)")
    st.info("**Note:** For AY 2026-27, the tax-free threshold is proposed to increase to BDT 375,000.")
    
    # Using a table for scannability
    st.markdown("#### Tax Slabs for AY 2025-26")
    st.table({
        "Income Slab (BDT)": [
            "First 350,000*", "Next 100,000", "Next 400,000", 
            "Next 500,000", "Next 500,000", "Next 2,000,000", "On Balance"
        ],
        "Rate": ["0%", "5%", "10%", "15%", "20%", "25%", "30%"]
    })
    st.caption("*Thresholds: Women/Seniors (65+): 400k | Disabled: 475k | Freedom Fighters: 500k")

    with st.expander("🌍 Non-Resident Individuals"):
        st.write("Non-resident individuals (except Non-Resident Bangladeshis) are taxed at a **flat rate of 30%** on their total taxable income in Bangladesh.")

with tab2:
    st.markdown("### 2. Corporate Tax Rates")
    st.write("Rates vary based on listing status and adherence to 'Cashless' conditions (banking channel transactions).")
    
    st.table({
        "Company Type": [
            "Non-Listed Company", "Publicly Traded (>10% IPO)", 
            "Publicly Traded (<=10% IPO)", "One Person Company (OPC)", 
            "Bank/Insurance/FI (Non-Listed)", "Tobacco Manufacturers"
        ],
        "Standard Rate": ["27.5%", "22.5%", "25.0%", "22.5%", "40.0%", "45% + 2.5% Surcharge"],
        "Reduced Rate (If Cashless*)": ["25.0%", "20.0%", "22.5%", "20.0%", "N/A", "N/A"]
    })
    st.caption("*To qualify for reduced rates, all receipts/investments and expenses >5 Lakh per transaction must be through bank transfer.")

with tab3:
    st.markdown("### 3. Dividends & Capital Gains")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dividends (WHT)")
        st.write("**Resident Recipient:**")
        st.markdown("- **Individual:** 10% (15% if no e-TIN)")
        st.markdown("- **Company:** 20%")
        st.write("**Non-Resident Recipient:**")
        st.markdown("- **Individual:** 30%")
        st.markdown("- **Company/Fund:** 20%")
        
    with col2:
        st.subheader("Capital Gains")
        st.write("**For Companies:**")
        st.markdown("- **Flat Rate:** 15% (General Assets/Shares)")
        st.write("**For Individuals:**")
        st.markdown("- **Listed Shares:** 15%")
        st.markdown("- **Other Assets (held >5 yrs):** 15%")
        st.markdown("- **Other Assets (held <=5 yrs):** Regular Slab Rates")

    st.divider()
    st.warning("**Real Estate Capital Gain:**")
    st.write("Tax on land transfer is often based on location-specific rates (e.g., 4% of deed value in major cities like Dhaka/Chattogram) or per-katha rates, whichever is higher.")

# --- SIDEBAR ---
st.sidebar.caption("Reference: Finance Act 2024/2025 & ITA 2023")
st.sidebar.markdown("---")
st.sidebar.write("💡 **Audit Alert:** Ensure your 'Dividend' payments to the parent company are backed by proof of 20% WHT deposit to avoid disallowance of the expense.")