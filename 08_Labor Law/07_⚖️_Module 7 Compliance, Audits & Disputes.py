import streamlit as st

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>⚖️ Module 7: Compliance, Audits & Disputes</h1>", unsafe_allow_html=True)
st.write("---")

st.info("""
**Executive Summary:** This module focuses on external relations—how to handle Government Inspections, Trade Unions, and the Labor Court. 
For Finance, this represents **Contingent Liabilities** and **Reputational Risk.**
""")

# --- SECTION 1: DIFE INSPECTION CHECKLIST ---
st.header("1. 🔍 Preparing for DIFE Inspection")
st.write("The Department of Inspection for Factories and Establishments (DIFE) conducts regular audits. Ensure these documents are ready:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Records & Registers")
    st.checkbox("Register of Workers (Form 8)")
    st.checkbox("Maternity Benefit Register (Form 11)")
    st.checkbox("Overtime Register (Form 10)")
    st.checkbox("Leave Register (Form 9)")

with col2:
    st.subheader("Financial Proofs")
    st.checkbox("WPPF Payment Receipts/Evidence")
    st.checkbox("Group Insurance Policy Document")
    st.checkbox("Proof of Bonus Payments")
    st.checkbox("Trade License & Factory License")

st.divider()

# --- SECTION 2: LABOR COURT & DISPUTES ---
st.header("2. 🏛️ Dispute Resolution & Labor Court")
st.write("Understanding the path of a grievance helps Finance estimate legal costs.")

with st.expander("The Dispute Workflow"):
    st.markdown("""
    1.  **Grievance Submission:** Worker submits written grievance to Employer within 30 days.
    2.  **Employer Response:** Employer must reply within 15 days.
    3.  **Labor Court:** If no resolution, the worker can file a case in the Labor Court within 30 days.
    4.  **Appeal:** Appeals go to the **Labor Appellate Tribunal**.
    """)

# --- SECTION 3: SOCIAL COMPLIANCE & ESG ---
st.header("3. 🌍 ESG & International Audits")
st.write("For export-oriented businesses, Labor Law is a subset of **ESG (Environmental, Social, and Governance)** reporting.")

audit_type = st.radio("Select Audit Framework for key focus areas:", ["SEDEX/SMETA", "BSCI", "ISO 45001"])

if audit_type == "SEDEX/SMETA":
    st.warning("**Focus:** Forced Labor, Health & Safety, and Fair Wages.")
elif audit_type == "BSCI":
    st.warning("**Focus:** Ethical Business Behavior and No Child Labor.")
else:
    st.warning("**Focus:** Occupational Health and Safety Management Systems.")

# --- SECTION 4: COMPLIANCE STATUS TRACKER ---
st.divider()
st.header("4. 📊 Internal Compliance Health Check")
st.write("Self-assess your department's compliance level:")

compliance_score = 0
if st.checkbox("All workers have Appointment Letters"): compliance_score += 25
if st.checkbox("WPPF is allocated and distributed"): compliance_score += 25
if st.checkbox("No worker works more than 60 hours/week (including OT)"): compliance_score += 25
if st.checkbox("Maternity benefits are paid as per 2023 amendment"): compliance_score += 25

st.progress(compliance_score / 100)
st.write(f"Your Compliance Score: **{compliance_score}%**")

if compliance_score == 100:
    st.balloons()
    st.success("Audit Ready!")
elif compliance_score >= 50:
    st.info("Good progress, but there are critical gaps to fill.")
else:
    st.error("High Risk: Immediate action required to avoid legal penalties.")

# --- QUIZ ---
st.header("5. 🧠 Audit Quiz")
q_audit = st.radio("How many days does an employer have to respond to a worker's grievance?", [7, 15, 30])

if st.button("Submit Answer"):
    if q_audit == 15:
        st.success("Correct! Under Section 33, the employer must communicate the decision within 15 days.")
    else:
        st.error("Incorrect. The legal timeframe for a response is 15 days.")