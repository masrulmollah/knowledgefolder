import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 32: Financial Instruments: Presentation")
st.write("This standard establishes principles for presenting financial instruments as liabilities or equity and for offsetting financial assets and financial liabilities.")

# --- THE FUNDAMENTAL PRINCIPLE ---
st.info("**Core Rule:** The issuer of a financial instrument shall classify the instrument, or its component parts, on initial recognition as a financial liability, a financial asset, or an equity instrument in accordance with the **substance of the contractual arrangement**.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Liability vs. Equity", "Compound Instruments", "Offsetting & Treasury Shares"])

with tab1:
    st.markdown("#### 1. Classification: Liability vs. Equity")
    st.write("Classification depends on whether the issuer has a contractual obligation to deliver cash or another financial asset.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("**Financial Liability**")
        st.markdown("""
        * **Obligation:** A contractual obligation to deliver cash (e.g., loans, trade payables).
        * **Redeemable Preference Shares:** If the issuer is required to redeem them at a fixed date, they are **liabilities**, not equity.
        """)
        
    with col2:
        st.success("**Equity Instrument**")
        st.markdown("""
        * **No Obligation:** The instrument includes no contractual obligation to deliver cash (e.g., ordinary shares).
        * **Residual Interest:** Represents a residual interest in the assets of an entity after deducting all of its liabilities.
        """)

    

with tab2:
    st.markdown("#### 2. Compound Financial Instruments")
    st.write("Some instruments contain both a liability and an equity component (e.g., **Convertible Bonds**).")
    
    st.warning("**Split Accounting**")
    st.write("The issuer must identify the components separately at the time of issuance.")
    
    with st.expander("📝 How to Calculate Split Accounting"):
        st.markdown("""
        1. **Liability Component:** Determine the fair value of a similar liability that does not have an associated equity component (discounted cash flows).
        2. **Equity Component:** This is the **residual amount** (Total proceeds minus the Liability component).
        """)
    
    st.caption("Once classified, the equity component is not subsequently remeasured.")

with tab3:
    st.markdown("#### 3. Treasury Shares & Offsetting")
    
    st.info("**Treasury Shares**")
    st.write("If an entity reacquires its own equity instruments, those 'treasury shares' shall be **deducted from equity**. No gain or loss is recognized in profit or loss on the purchase, sale, issue, or cancellation of an entity’s own equity instruments.")
    
    st.divider()
    
    st.markdown("**Offsetting (Netting)**")
    st.write("A financial asset and a financial liability shall be offset (presented as a net amount) **ONLY** when the entity:")
    st.markdown("""
    1. Currently has a **legally enforceable right** to set off the recognized amounts.
    2. Intends either to **settle on a net basis**, or to realize the asset and settle the liability simultaneously.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 32")