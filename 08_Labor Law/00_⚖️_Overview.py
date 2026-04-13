import streamlit as st

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>📋 Subject Overview: Labor of Bangladesh</h1>", unsafe_allow_html=True)
st.write("---")

st.markdown("""
### Welcome to the Professional Labor Law Refresher
This comprehensive guide is curated specifically for **Finance, Accounts, and HR Professionals** in Bangladesh. 
Use this dashboard to navigate through the 7 core pillars of the **Bangladesh Labour Act 2006** and **Labour Rules 2015**.
""")

# --- MODULE ROADMAP (Grid Layout) ---
st.header("📌 The 7 Pillars of Compliance")

col1, col2 = st.columns(2)

with col1:
    with st.expander("🔹 Module 1: Legal Framework", expanded=True):
        st.write("""
        - Hierarchy of Laws (Act vs. Rules)
        - Classification of Workers
        - Essential definitions for Financial Provisioning.
        """)
    
    with st.expander("🔹 Module 2: Payroll & OT"):
        st.write("""
        - Calculation of Hourly OT Rate
        - Minimum Wage Gazettes
        - Statutory Bonus and Deductions.
        """)

    with st.expander("🔹 Module 3: Leave & Maternity"):
        st.write("""
        - Earned Leave (1:14 vs 1:18)
        - **120 Days** Maternity Benefit rules
        - Leave Encashment logic.
        """)

    with st.expander("🔹 Module 4: WPPF & Funds"):
        st.write("""
        - 5% Profit Sharing (WPPF)
        - Gratuity Tiers (30/45 days)
        - Recognized Provident Funds.
        """)

with col2:
    with st.expander("🔹 Module 5: Final Settlement"):
        st.write("""
        - Resignation vs. Termination
        - Notice Pay requirements
        - Compensation Calculation.
        """)

    with st.expander("🔹 Module 6: Safety & Welfare"):
        st.write("""
        - Mandatory facilities (Canteen, Creche)
        - Group Insurance requirements
        - Accident Compensation.
        """)

    with st.expander("🔹 Module 7: Audits & Disputes"):
        st.write("""
        - DIFE Inspection Checklist
        - Grievance Handling
        - Labor Court & Appeal procedures.
        """)

st.divider()

# --- QUICK COMPLIANCE SUMMARY TABLE ---
st.header("🚀 Quick Reference Guide")
st.write("Key statutory figures at a glance (Current for 2025/2026):")

summary_data = {
    "Subject": ["Maternity Leave", "WPPF Rate", "OT Rate", "Earned Leave Carry-forward", "Gratuity Eligibility"],
    "Standard Requirement": ["120 Days (Paid)", "5% of Net Profit", "2 x Basic Hourly Rate", "Up to 40-60 Days", "5 Years of Service"]
}
st.table(summary_data)

# --- CALL TO ACTION ---
st.success("👈 **Select a Module from the sidebar to begin your deep-dive refresher!**")

# --- FOOTER ---
st.info("""
**Note for Accountants:** Always ensure your actuarial valuations for Gratuity and provisioning for Earned Leave are updated based on the calculations provided in Modules 3 and 4.
""")