import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 9: Financial Instruments")
st.write("This standard establishes principles for the financial reporting of financial assets and financial liabilities that will present relevant and useful information to users of financial statements.")

# --- THE THREE PILLARS ---
st.info("**The Three Pillars of IFRS 9:** Classification & Measurement, Impairment (ECL), and Hedge Accounting.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Classification & Measurement", "Impairment (ECL)", "Hedge Accounting"])

with tab1:
    st.markdown("#### 1. Classification of Financial Assets")
    st.write("Classification is determined by the entity's **Business Model** for managing the assets and the **Contractual Cash Flow Characteristics** (SPPI test).")
    
    
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**Amortised Cost**")
        st.markdown("""
        * **Business Model:** Hold to collect cash flows.
        * **SPPI:** Solely Payments of Principal and Interest.
        * *Example:* Trade Receivables, Loans.
        """)
    with col2:
        st.warning("**FVOCI**")
        st.markdown("""
        * **Business Model:** Hold to collect AND sell.
        * **SPPI:** Yes.
        * *Example:* Debt securities held for liquidity.
        """)
    with col3:
        st.error("**FVTPL**")
        st.markdown("""
        * **Residual Category:** Assets that don't meet the above.
        * *Example:* Derivatives, Equity investments (unless elected for FVOCI).
        """)

    st.divider()
    st.markdown("#### Financial Liabilities")
    st.write("Most financial liabilities are measured at **Amortised Cost**. Those held for trading (derivatives) are measured at **FVTPL**.")

with tab2:
    st.markdown("#### 2. Impairment: The Expected Credit Loss (ECL) Model")
    st.write("Unlike the old 'incurred loss' model, IFRS 9 requires entities to recognize credit losses earlier based on future expectations.")

    st.error("**The Three-Stage Model**")
    st.markdown("""
    1. **Stage 1 (Performing):** Credit risk has not increased significantly. Recognize **12-month ECL**.
    2. **Stage 2 (Underperforming):** Significant Increase in Credit Risk (SICR). Recognize **Lifetime ECL**.
    3. **Stage 3 (Non-performing):** Credit impaired/Default. Recognize **Lifetime ECL**.
    """)

    

    with st.expander("📝 Simplified Approach for Trade Receivables"):
        st.write("For trade receivables without a significant financing component (standard in FMCG), entities can use a 'Provision Matrix' to always recognize **Lifetime ECL**.")

with tab3:
    st.markdown("#### 3. Hedge Accounting")
    st.write("The objective is to represent in the financial statements the effect of an entity’s risk management activities that use financial instruments to manage exposures.")
    
    st.info("**Qualifying Criteria:**")
    st.markdown("""
    * The hedging relationship consists only of eligible hedging instruments and eligible hedged items.
    * Formal designation and documentation at inception.
    * The hedging relationship meets the **effectiveness requirements** (economic relationship, credit risk doesn't dominate, hedge ratio is consistent).
    """)

    st.warning("**Types of Hedges:**")
    st.markdown("""
    * **Fair Value Hedge:** Hedge of exposure to changes in fair value of a recognized asset/liability.
    * **Cash Flow Hedge:** Hedge of exposure to variability in cash flows (e.g., future raw material purchase in USD).
    * **Net Investment Hedge:** Hedge of foreign currency exposure in a foreign operation.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 9")