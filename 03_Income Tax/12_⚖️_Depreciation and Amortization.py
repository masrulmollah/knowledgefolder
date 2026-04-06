import streamlit as st

def show_depreciation_page():
    # --- STANDARD HEADERS ---
    st.markdown("### 📉 Depreciation & Amortization Summary")
    st.markdown("#### According to the Income Tax Act, 2023")
    st.divider()

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.header("Chapter 11 Explorer")
    menu = st.sidebar.radio("Navigate to:", 
                            ["General Principles", "Depreciation Rates", "Amortization rules", "WDV Calculator"])

    if menu == "General Principles":
        st.markdown("##### **Core Rules for Depreciation (Section 71)**")
        st.write("1. **Ownership:** The asset must be owned by the taxpayer.")
        st.write("2. **Usage:** The asset must be used for business/professional purposes.")
        st.write("3. **Timing:** Full year depreciation is allowed in the year of acquisition; zero in the year of sale.")
        st.write("4. **The Capping Rule:** Passenger motor vehicles (not for hire) are capped at a cost of Tk. 3,000,000 for depreciation purposes.")
        st.info("Note: Accounting depreciation is added back, and Tax depreciation is deducted during tax assessment.")

    elif menu == "Depreciation Rates":
        st.markdown("##### **Common Tax Depreciation Rates (Third Schedule)**")
        rates = {
            "Building (General)": "10%",
            "Factory Building": "20%",
            "Furniture & Fittings": "10%",
            "Machinery & Plant (General)": "20%",
            "Computer & IT Equipment": "30%",
            "Motor Vehicles (Non-commercial)": "20%",
            "Books": "30%"
        }
        st.table({"Asset Type": rates.keys(), "Standard Rate": rates.values()})
        st.write("*Rates may vary for specific industries like shipping or specialized machinery.*")

    elif menu == "Amortization rules":
        st.markdown("##### **Amortization (Section 72)**")
        st.write("- **Intangibles:** Patents, Trademarks, and Licenses are amortized over their useful life.")
        st.write("- **Pre-commencement Expenses:** Expenses incurred before business start-up are typically amortized over **10 years** (10% annually).")
        st.write("- **Software:** Specialized software is usually amortized at 20-30% depending on the nature of the application.")

    elif menu == "WDV Calculator":
        st.markdown("##### **Written Down Value (WDV) & Depreciation Calculator**")
        
        col1, col2 = st.columns(2)
        with col1:
            asset_type = st.selectbox("Select Asset Type", ["General Building", "Factory", "Machinery", "Computer", "Furniture"])
            cost = st.number_input("Original Cost (Tk.):", min_value=0.0, value=100000.0, step=10000.0)
            
        with col2:
            rate_map = {"General Building": 0.10, "Factory": 0.20, "Machinery": 0.20, "Computer": 0.30, "Furniture": 0.10}
            rate = rate_map[asset_type]
            st.write(f"**Applicable Rate:** {rate*100:.0f}%")
            years = st.slider("Years of usage:", 1, 10, 1)

        # Calculation
        current_wdv = cost
        for i in range(years):
            dep = current_wdv * rate
            current_wdv -= dep

        st.divider()
        st.metric(f"WDV after {years} year(s)", f"Tk. {current_wdv:,.2f}")
        st.write(f"Total Depreciation Claimed: Tk. {(cost - current_wdv):,.2f}")

    st.divider()

# Execution logic
if __name__ == "__main__":
    show_depreciation_page()
else:
    show_depreciation_page()