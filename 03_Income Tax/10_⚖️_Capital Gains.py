import streamlit as st

def show_capital_gains_page():
    # --- STANDARD WEB HEADERS ---
    st.markdown("### 💰 Capital Gains Summary")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.header("Navigation")
    section = st.sidebar.radio("Select Section:", 
                               ["Scope & Assets", "Calculation Method", "Exemptions", "Gain Calculator"])

    if section == "Scope & Assets":
        st.markdown("##### **What is a Capital Asset? (Section 56)**")
        st.write("Capital gain is any profit arising from the transfer of a capital asset. This includes:")
        st.write("- **Real Estate:** Land, buildings, and apartments.")
        st.write("- **Financial Assets:** Shares, stocks, bonds, and debentures.")
        st.write("- **Intangibles:** Goodwill, patents, and trademarks.")
        
        st.warning("**Exclusions:** Does not include stock-in-trade, raw materials, or movable personal items (furniture/clothing) used by the taxpayer.")

    elif section == "Calculation Method":
        st.markdown("##### **Computing the Gain (Section 57)**")
        st.write("The taxable gain is determined using the following logic:")
        
        st.success("**Gain = Consideration Received - (Cost of Acquisition + Cost of Improvement + Transfer Expenses)**")
        
        st.markdown("**Key Terms:**")
        st.write("- **Consideration:** The sale price or fair market value of the asset.")
        st.write("- **Cost of Acquisition:** The price paid to purchase the asset.")
        st.write("- **Transfer Expenses:** Brokerage, legal fees, or stamp duties paid during the sale.")

    elif section == "Exemptions":
        st.markdown("##### **Common Exemptions (Section 60)**")
        st.write("Certain gains are not taxable or qualify for relief:")
        st.write("- **Government Bonds:** Gains from specific government-backed securities.")
        st.write("- **Residential Property:** Relief may apply if gains are reinvested in another residential property (subject to time limits).")
        st.write("- **Listed Shares:** Specific tax rates usually apply to gains from the stock market.")

    elif section == "Gain Calculator":
        st.markdown("##### **Capital Gains Calculator**")
        
        col1, col2 = st.columns(2)
        with col1:
            consideration = st.number_input("Full Value of Consideration (Sale Price):", min_value=0.0, step=50000.0, value=2000000.0)
            acquisition_cost = st.number_input("Original Cost of Acquisition:", min_value=0.0, step=50000.0, value=1500000.0)
        
        with col2:
            improvement_cost = st.number_input("Cost of Improvements:", min_value=0.0, step=10000.0, value=0.0)
            transfer_fees = st.number_input("Expenditure for Transfer (Legal/Brokerage):", min_value=0.0, step=5000.0, value=20000.0)
        
        # Calculation logic
        total_cost = acquisition_cost + improvement_cost + transfer_fees
        capital_gain = consideration - total_cost

        st.divider()
        st.metric("Total Cost Base", f"Tk. {total_cost:,.0f}")
        
        if capital_gain > 0:
            st.subheader(f"Taxable Capital Gain: Tk. {capital_gain:,.0f}")
            st.info("Note: Apply the applicable tax rate (e.g., 15% for individuals on certain assets) to this amount.")
        else:
            st.error(f"Capital Loss: Tk. {abs(capital_gain):,.0f}")
            st.write("Note: Capital losses can generally be carried forward to set off against future capital gains.")

    st.write("")
    st.divider()

# Execution logic for multi-page structure
if __name__ == "__main__":
    show_capital_gains_page()
else:
    show_capital_gains_page()