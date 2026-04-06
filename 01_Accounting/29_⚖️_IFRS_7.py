import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 7: Financial Instruments: Disclosures")
st.write("This standard requires entities to provide disclosures in their financial statements that enable users to evaluate the significance of financial instruments and the nature and extent of risks arising from them.")

# --- THE CORE OBJECTIVE ---
st.info("**Objective:** To provide information about an entity’s exposure to risks and how those risks are managed. It focuses on both Qualitative and Quantitative disclosures.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Significance of Instruments", "Nature & Extent of Risks", "Hedge Accounting"])

with tab1:
    st.markdown("#### 1. Significance of Financial Instruments")
    st.write("An entity must disclose information that enables users to evaluate the significance of financial instruments for its financial position and performance.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Balance Sheet Disclosures**")
        st.markdown("""
        * Categories of financial assets and liabilities (per IFRS 9).
        * Financial assets/liabilities at **Fair Value through P&L**.
        * Reclassifications of financial assets.
        * **Offsetting** of financial assets and liabilities.
        * Collateral held or pledged.
        """)
    with col2:
        st.warning("**P&L and Equity Disclosures**")
        st.markdown("""
        * Net gains or net losses on each category.
        * Total **interest income** and total **interest expense**.
        * Fee income and expense arising from financial instruments.
        * Impairment losses (Expected Credit Losses).
        """)

with tab2:
    st.markdown("#### 2. Risk Disclosures (Qualitative & Quantitative)")
    st.write("The entity must disclose the nature and extent of risks arising from financial instruments to which the entity is exposed at the end of the reporting period.")

    st.error("**The Three Pillars of Risk**")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**1. Credit Risk**")
        st.caption("The risk that one party to a financial instrument will cause a financial loss for the other party by failing to discharge an obligation.")
    with c2:
        st.markdown("**2. Liquidity Risk**")
        st.caption("The risk that an entity will encounter difficulty in meeting obligations associated with financial liabilities that are settled by delivering cash.")
    with c3:
        st.markdown("**3. Market Risk**")
        st.caption("The risk that the fair value or future cash flows will fluctuate because of changes in market prices (Currency, Interest Rate, Other Price risk).")

    with st.expander("📊 Quantitative Requirements"):
        st.write("For each type of risk, an entity must provide summary quantitative data and a **Sensitivity Analysis** (e.g., how profit would change if interest rates rose by 1%).")

with tab3:
    st.markdown("#### 3. Hedge Accounting Disclosures")
    st.write("If you use derivatives to hedge risks, IFRS 7 requires detailed reporting on your hedging strategy.")
    
    st.info("**What to Disclose?**")
    st.markdown("""
    * The entity's **risk management strategy** and how it is applied.
    * How the entity's hedging activities may affect the **amount, timing, and uncertainty** of future cash flows.
    * The effect that hedge accounting has had on the entity’s Statement of Financial Position and Statement of Comprehensive Income.
    """)

    st.divider()
    st.markdown("#### Fair Value Hierarchy")
    st.write("Financial instruments measured at fair value must be categorized into three levels:")
    st.markdown("- **Level 1:** Quoted prices in active markets.")
    st.markdown("- **Level 2:** Inputs other than quoted prices that are observable (e.g., interest rates).")
    st.markdown("- **Level 3:** Unobservable inputs (Management estimates).")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 7")