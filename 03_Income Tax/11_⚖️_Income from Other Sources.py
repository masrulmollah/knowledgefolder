import streamlit as st

def show_other_sources_page():
    # --- STANDARD HEADERS ---
    st.markdown("### 🎲 Income from Other Sources Summary")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.header("Explore Chapter 10")
    menu = st.sidebar.radio("Go to:", ["General Scope", "Special Income Types", "Deductions", "Quick Estimator"])

    if menu == "General Scope":
        st.markdown("##### **Scope of Other Sources (Section 66)**")
        st.write("This is the residual head of income. If an income cannot be classified under any other head, it falls here. Examples include:")
        st.write("- **Dividends:** Income received from company shares.")
        st.write("- **Interest:** Earnings from bank deposits or non-govt securities.")
        st.write("- **Royalties:** Payments for the use of intellectual property.")
        st.write("- **Technical Fees:** Fees for managerial or consultancy services.")
        st.info("Note: Any income found 'unexplained' by the DCT is often categorized here as deemed income.")

    elif menu == "Special Income Types":
        st.markdown("##### **Specific Categories (Section 67)**")
        st.write("The Act highlights specific items under this head:")
        st.write("- **Lottery & Prizes:** Winnings from lotteries, crossword puzzles, or card games.")
        st.write("- **Asset Transfers:** Income from transferring natural or taxpayer-created assets.")
        st.write("- **Deemed Income:** Amounts received as a gift or loan that don't meet specific transparency criteria.")
        st.warning("Winnings from lotteries are usually taxed at a flat rate (e.g., 20%) through TDS at the time of payment.")

    elif menu == "Deductions":
        st.markdown("##### **Admissible vs Inadmissible Expenses**")
        
        tab1, tab2 = st.tabs(["✅ Allowable", "❌ Inadmissible"])
        
        with tab1:
            st.write("**Section 68 allows:**")
            st.write("- **Direct Expenses:** Any money spent wholly to earn the income.")
            st.write("- **Interest:** On loans taken to invest in the asset producing the income.")
            st.write("- **Bank Charges:** Commissions paid for collecting dividends or interest.")
            
        with tab2:
            st.write("**Section 69 prohibits:**")
            st.write("- **Personal Spending:** Private or personal expenses.")
            st.write("- **Capital Costs:** Costs to acquire or improve the asset (non-revenue).")
            st.write("- **TDS Violations:** Payments where required tax was not withheld.")

    elif menu == "Quick Estimator":
        st.markdown("##### **Income Estimator**")
        
        col1, col2 = st.columns(2)
        with col1:
            gross_other = st.number_input("Gross Income (Tk.):", min_value=0.0, step=5000.0, value=50000.0)
            st.caption("Includes Dividends, Interest, Royalties, etc.")
        
        with col2:
            exp_other = st.number_input("Direct Expenses (Tk.):", min_value=0.0, step=1000.0)
            st.caption("Expenses incurred solely for this income.")

        net_other = gross_other - exp_other
        
        st.divider()
        st.subheader(f"Net Income from Other Sources: Tk. {max(0.0, net_other):,.0f}")
        st.write("Ensure you keep receipts for all 'Direct Expenses' to justify the deduction during assessment.")

    st.divider()

# Execution logic
if __name__ == "__main__":
    show_other_sources_page()
else:
    show_other_sources_page()