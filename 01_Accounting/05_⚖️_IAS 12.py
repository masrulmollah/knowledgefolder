import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 12: Income Taxes")
st.write("This standard prescribes the accounting treatment for income taxes, focusing on accounting for the current and future tax consequences of transactions and other events.")

# --- THE GOLDEN RULE ---
st.info("**Core Principle:** Deferred tax must be recognized for temporary differences between the carrying amount of assets and liabilities in the financial statements and their tax base.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Current Tax", "Deferred Tax", "Tax Bases & Temporary Differences"])

with tab1:
    st.markdown("#### 1. Current Tax")
    st.write("Current tax is the amount of income taxes payable (or recoverable) in respect of the taxable profit (or tax loss) for a period.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Measurement**")
        st.markdown("""
        * Measured using the **tax rates and tax laws** that have been enacted or substantively enacted by the end of the reporting period.
        """)
        
    with col2:
        st.error("**Accounting Treatment**")
        st.markdown("""
        * Unpaid current tax is recognized as a **liability** (Current Tax Payable).
        * If the amount paid exceeds the amount due, the excess is recognized as an **asset**.
        """)

with tab2:
    st.markdown("#### 2. Deferred Tax Liabilities & Assets")
    st.write("Deferred tax is the tax expected to be paid or recovered in future periods due to current differences between accounting and tax treatments.")

    c1, c2 = st.columns(2)

    with c1:
        st.error("**Deferred Tax Liabilities (DTL)**")
        st.markdown("""
        * Arise from **Taxable Temporary Differences**.
        * Situations where accounting profits are recognized *before* tax profits.
        * **Rule:** Must be recognized for almost all taxable temporary differences.
        """)
        
    with c2:
        st.success("**Deferred Tax Assets (DTA)**")
        st.markdown("""
        * Arise from **Deductible Temporary Differences** (and unused tax losses/credits).
        * **Rule:** Only recognized to the extent that it is **probable** that future taxable profits will be available.
        """)
    
    with st.expander("📝 Presentation & Measurement"):
        st.write("""
        * **No Discounting:** Deferred tax assets and liabilities must **not** be discounted to present value.
        * **Classification:** DTA and DTL are always classified as **non-current** assets or liabilities on the statement of financial position.
        """)

with tab3:
    st.markdown("#### 3. Tax Bases & Temporary Differences")
    st.write("Temporary differences are the differences between the carrying amount of an asset or liability and its tax base.")
    
    st.warning("**Definitions**")
    st.write("""
    * **Carrying Amount:** The value of the asset or liability reported on the balance sheet.
    * **Tax Base:** The amount attributed to that asset or liability for tax purposes by the tax authorities.
    """)
    
    with st.expander("🔍 Quick Formula Matrix"):
        st.write("""
        Use this quick rule of thumb to determine what to recognize:
        
        * **For Assets:**
          * If Carrying Amount **>** Tax Base $\\rightarrow$ **Taxable** Temporary Difference (**DTL**)
          * If Carrying Amount **<** Tax Base $\\rightarrow$ **Deductible** Temporary Difference (**DTA**)
          
        * **For Liabilities:**
          * If Carrying Amount **>** Tax Base $\\rightarrow$ **Deductible** Temporary Difference (**DTA**)
          * If Carrying Amount **<** Tax Base $\\rightarrow$ **Taxable** Temporary Difference (**DTL**)
        """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 12")