import streamlit as st

# --- SUBPAGE HEADER ---
st.header("Income Tax Act 2023: Tax Administration & Tribunal")
st.write("A summary of the administrative hierarchy and the judicial process for tax appeals in Bangladesh.")

# --- THE ADMINISTRATIVE HIERARCHY ---
st.info("**Core Principle:** The National Board of Revenue (NBR) is the apex body. Under the new 2023 Act, the administration is designed to be increasingly digital and taxpayer-friendly.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Administrative Hierarchy", "Taxes Tribunal", "Powers & Procedures"])

with tab1:
    st.markdown("### 1. Tax Authorities in Bangladesh")
    st.write("The hierarchy of tax authorities as per the Income Tax Act is as follows:")

    

    st.markdown("""
    1. **National Board of Revenue (NBR):** The supreme executive authority.
    2. **Chief Commissioner of Taxes (CCT):** A new high-level administrative role.
    3. **Commissioner of Taxes (CT):** Heads a specific Tax Zone (e.g., Large Taxpayers Unit or LTU).
    4. **Additional/Joint Commissioner of Taxes (ACT/JCT):** Supervisory roles within a range.
    5. **Deputy Commissioner of Taxes (DCT):** The primary assessing officer (the first point of contact for your company's filings).
    6. **Assistant Commissioner (AC) / Extra Assistant Commissioner (EAC):** Junior assessing officers.
    7. **Inspectors:** Assist the DCT in field inquiries and data collection.
    """)

with tab2:
    st.markdown("### 2. Taxes Appellate Tribunal")
    st.write("When a taxpayer is aggrieved by an order from the Commissioner (Appeals), the next step is the **Taxes Appellate Tribunal**.")

    col1, col2 = st.columns(2)
    with col1:
        st.success("**Composition**")
        st.write("The Tribunal consists of Judicial members (Judges/Advocates) and Accountant members (typically FCAs or senior tax officials).")
    with col2:
        st.error("**Finality of Fact**")
        st.write("The Tribunal is the **final authority on facts**. Appeals to the High Court Division can only be made on **points of law**.")

    st.warning("**The Appeal Path:**")
    st.markdown("""
    * **Step 1:** Assessment Order by DCT.
    * **Step 2:** Appeal to Commissioner (Appeals) — *Within 60 days.*
    * **Step 3:** Appeal to Taxes Appellate Tribunal — *Within 60 days of the Appeal Order.*
    * **Step 4:** Reference to High Court Division — *Only on questions of Law.*
    """)

with tab3:
    st.markdown("### 3. Powers and Key Procedures")
    
    with st.expander("🔍 Powers of Tax Officers"):
        st.write("Under the Act, tax authorities have powers similar to a Civil Court, including:")
        st.markdown("""
        * Discovery and inspection of accounts.
        * Enforcing the attendance of any person (Summons).
        * Compelling the production of books and documents.
        * Issuing commissions for examination of witnesses.
        """)

    st.divider()
    st.markdown("### Alternative Dispute Resolution (ADR)")
    st.write("To reduce the burden on the Tribunal, the ITA 2023 encourages **ADR**. It is a simplified process where a taxpayer and the NBR can reach a settlement through a neutral Facilitator.")
    
    st.info("**Why choose ADR?** It is faster, non-adversarial, and once a deal is signed, it cannot be challenged in any court, providing finality to your tax liability.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: Income Tax Act 2023 (Bangladesh)")
st.sidebar.markdown("---")
st.sidebar.write("💡 **Finance Lead Note:** Ensure all factory-related 'Capital Expenditure' documentation is ready for DCT inspection to avoid unnecessary additions to income during assessment.")