import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 2: Share-based Payment")
st.write("This standard requires an entity to reflect in its profit or loss and financial position the effects of share-based payment transactions, including expenses associated with transactions in which share options are granted to employees.")

# --- THE CORE PRINCIPLE ---
st.info("**Core Rule:** An entity shall recognize the goods or services received or acquired in a share-based payment transaction when it obtains the goods or as the services are received.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Types of Transactions", "Equity-Settled", "Cash-Settled"])

with tab1:
    st.markdown("#### 1. Scope of IFRS 2")
    st.write("There are three main types of share-based payment transactions:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("**Equity-Settled**")
        st.write("The entity receives goods/services as consideration for its own equity instruments (e.g., shares or options).")
    with col2:
        st.info("**Cash-Settled**")
        st.write("The entity acquires goods/services by incurring a liability to transfer cash based on the price of the shares.")
    with col3:
        st.warning("**Choice of Settlement**")
        st.write("Transactions where either the entity or the supplier has a choice of settlement (cash or equity).")

    

with tab2:
    st.markdown("#### 2. Equity-Settled Transactions")
    st.write("For transactions with employees, the entity measures the fair value of the services received by reference to the **Fair Value of the equity instruments granted** at the **Grant Date**.")

    st.markdown("**Accounting Treatment:**")
    st.code("Dr. Expense (P&L) \nCr. Equity (Retained Earnings/Other Reserve)", language="text")

    with st.expander("⏳ Vesting Conditions"):
        st.write("If the equity instruments vest immediately, the expense is recognized in full. If they vest over a period (e.g., 3 years of service), the expense is spread over that **Vesting Period**.")
        st.markdown("""
        * **Service Conditions:** Require the employee to complete a period of service.
        * **Performance Conditions:** Require specific performance targets to be met (e.g., EPS growth).
        """)
    
    st.error("**Note:** For equity-settled transactions, the Fair Value is measured at **Grant Date** and is **NOT** subsequently remeasured.")

with tab3:
    st.markdown("#### 3. Cash-Settled Transactions")
    st.write("Commonly known as **Share Appreciation Rights (SARs)**. The entity acquires services by incurring a liability to pay cash based on the share price.")

    st.markdown("**Accounting Treatment:**")
    st.code("Dr. Expense (P&L) \nCr. Liability", language="text")

    st.warning("**The Remeasurement Rule**")
    st.write("Unlike equity-settled plans, the liability for cash-settled plans must be **remeasured at each reporting date** and at the date of settlement. Any changes in fair value are recognized in **Profit or Loss**.")

    st.divider()
    st.markdown("#### Disclosure Requirements")
    st.markdown("""
    1. **Nature and extent** of share-based payment arrangements.
    2. **How the fair value** was determined (e.g., use of Black-Scholes or Binomial models).
    3. **The effect** of the transactions on the entity's profit or loss and financial position.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 2")