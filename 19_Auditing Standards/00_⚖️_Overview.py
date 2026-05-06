import streamlit as st

# Custom Styling for the Overview Hub
st.markdown("""
    <style>
    .hub-title { color: #1c2833; font-size: 36px; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .hub-subtitle { color: #566573; font-size: 18px; text-align: center; margin-bottom: 30px; }
    .phase-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #d5dbdb;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        height: 250px;
    }
    .phase-header { color: #2e86c1; font-weight: bold; font-size: 20px; margin-bottom: 10px; }
    .stat-box {
        background-color: #1c2833;
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="hub-title">International Standards on Auditing (ISA)</p>', unsafe_allow_html=True)
st.markdown('<p class="hub-subtitle">A Complete Roadmap to the Global Audit Framework</p>', unsafe_allow_html=True)

# Top Stats/Summary
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.markdown('<div class="stat-box"><strong>6 Modules</strong><br>Full Syllabus</div>', unsafe_allow_html=True)
with col_s2:
    st.markdown('<div class="stat-box"><strong>36+ Standards</strong><br>Global Compliance</div>', unsafe_allow_html=True)
with col_s3:
    st.markdown('<div class="stat-box"><strong>Mastery Level</strong><br>Professional Grade</div>', unsafe_allow_html=True)

st.divider()

# The Audit Lifecycle Grid
st.subheader("🚀 The Audit Journey")
st.write("The ISAs are designed to follow the chronological flow of a professional audit engagement.")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""<div class="phase-card">
        <div class="phase-header">1. Foundations</div>
        <strong>ISA 200–299</strong><br><br>
        Setting ethics, engagement terms, and quality control. This is where the auditor's mindset is built.
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""<div class="phase-card">
        <div class="phase-header">2. Strategy & Risk</div>
        <strong>ISA 300–499</strong><br><br>
        Planning the attack. Identifying where the money might be missing and setting materiality.
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""<div class="phase-card">
        <div class="phase-header">3. Fieldwork</div>
        <strong>ISA 500–599</strong><br><br>
        Gathering the proof. Sampling, bank confirms, and checking management's estimates.
    </div>""", unsafe_allow_html=True)

st.write("") # Spacer

c4, c5, c6 = st.columns(3)

with c4:
    st.markdown("""<div class="phase-card">
        <div class="phase-header">4. Support</div>
        <strong>ISA 600–699</strong><br><br>
        Leveraging others. Using the work of experts, internal auditors, or component firms.
    </div>""", unsafe_allow_html=True)

with c5:
    st.markdown("""<div class="phase-card">
        <div class="phase-header">5. Finalization</div>
        <strong>ISA 700–799</strong><br><br>
        Forming the opinion. Writing the report that the shareholders will actually read.
    </div>""", unsafe_allow_html=True)

with c6:
    st.markdown("""<div class="phase-card">
        <div class="phase-header">6. Special Cases</div>
        <strong>ISA 800–899</strong><br><br>
        Auditing specific elements, single statements, or summary financial reports.
    </div>""", unsafe_allow_html=True)

st.divider()

# Final Methodology Summary
with st.expander("📝 How to use this Knowledge Folder"):
    st.write("""
    1. **Sequential Learning:** Start from Module 1 to understand the 'rules of the game' before moving to risk assessment.
    2. **Interactive Testing:** Use the Quiz section in each module to validate your understanding.
    3. **Scenario Focus:** Pay close attention to the 'Practical Scenarios'—these represent the real-world challenges faced by Factory Finance Leads and Auditors alike.
    4. **Reference Guide:** Use this as a quick look-up tool during audit season to ensure compliance with specific documentation or reporting standards.
    """)

st.success("Select a specific module from the sidebar to begin your deep dive into the standards.")