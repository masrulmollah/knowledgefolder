import streamlit as st

# Custom Styling for Professional Look
st.markdown("""
    <style>
    .main-title { color: #1a5276; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .isa-card { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 5px solid #2980b9;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .example-text { color: #515a5a; font-style: italic; background-color: #f8f9f9; padding: 10px; border-radius: 5px; }
    .quiz-area { background-color: #f4fcf0; padding: 20px; border-radius: 10px; border: 1px solid #27ae60; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">ISA 200–299: General Principles & Responsibilities</p>', unsafe_allow_html=True)

# Tabs for Organization
tab1, tab2, tab3 = st.tabs(["📚 Full Standards Library", "💡 Practical Scenarios", "🧠 Mastery Quiz"])

with tab1:
    st.info("The 200 series governs the auditor's ethical and professional behavior.")
    
    # List of all ISAs in the 200 series
    isa_data = [
        {
            "id": "ISA 200",
            "title": "Overall Objectives & Professional Skepticism",
            "summary": "The foundation of all audits. It requires auditors to obtain 'Reasonable Assurance' and maintain 'Professional Skepticism'.",
            "details": "Auditors must recognize that inherent limitations exist (sampling, internal control gaps) which prevent 'Absolute Assurance'."
        },
        {
            "id": "ISA 210",
            "title": "Agreeing the Terms of Audit Engagements",
            "summary": "Ensures management and the auditor are on the same page before work starts.",
            "details": "Requires an Engagement Letter. If the client imposes a scope limitation that would result in a disclaimer of opinion, the auditor should not accept it."
        },
        {
            "id": "ISA 220",
            "title": "Quality Management for an Audit",
            "summary": "Focuses on the Engagement Partner's responsibility for quality.",
            "details": "Requires a system of quality management, including direction, supervision, and review of the audit team's work."
        },
        {
            "id": "ISA 230",
            "title": "Audit Documentation",
            "summary": "The 'if it isn't written, it wasn't done' rule.",
            "details": "Audit files must be assembled within 60 days of the report date and kept for at least 5 years (depending on local law)."
        },
        {
            "id": "ISA 240",
            "title": "The Auditor’s Responsibilities Relating to Fraud",
            "summary": "Identifying risks of material misstatement due to fraud.",
            "details": "Focuses on two types of fraud: Fraudulent Financial Reporting and Misappropriation of Assets. Requires 'Journal Entry Testing'."
        },
        {
            "id": "ISA 250",
            "title": "Consideration of Laws & Regulations",
            "summary": "Distinguishes between laws with direct vs. indirect effects.",
            "details": "Direct effect: Tax/Pension laws. Indirect effect: Environmental/Labor laws. Auditor must inquire about non-compliance."
        },
        {
            "id": "ISA 260",
            "title": "Communication with TCWG",
            "summary": "How to talk to those at the top (Board of Directors/Audit Committee).",
            "details": "Must communicate audit scope, timing, and significant findings (e.g., disagreements with management)."
        },
        {
            "id": "ISA 265",
            "title": "Communicating Deficiencies in Internal Control",
            "summary": "Reporting weaknesses found during the audit.",
            "details": "Significant deficiencies must be reported in writing to Those Charged with Governance (TCWG)."
        }
    ]

    for isa in isa_data:
        with st.expander(f"{isa['id']}: {isa['title']}"):
            st.markdown(f"**Core Objective:** {isa['summary']}")
            st.write(isa['details'])

with tab2:
    st.subheader("Real-World Audit Challenges")
    
    st.write("### 🏢 Scenario: The Scope Limitation (ISA 210)")
    st.markdown("""
    A new client tells you that you are not allowed to observe the year-end inventory count. 
    **Auditor's Action:** Under ISA 210, you must determine if this is a scope limitation. If you can't get sufficient evidence, you may need to decline the engagement before it starts.
    """)
    
    st.write("### 📝 Scenario: The Missing Signature (ISA 230)")
    st.markdown("""
    An audit junior performed a bank reconciliation but didn't document who reviewed it. 
    **Impact:** During a quality review, this is a failure of ISA 230 and ISA 220. The 'Audit Trail' is broken.
    """)
    
    st.write("### ⚖️ Scenario: Environmental Violation (ISA 250)")
    st.markdown("""
    You find out the factory is dumping waste illegally. 
    **Action:** This is an 'Indirect Effect' law. You must report this to management and TCWG. If they do nothing, you may have to report it to regulators or resign.
    """)

with tab3:
    st.markdown('<div class="quiz-area">', unsafe_allow_html=True)
    st.subheader("Final Mastery Check")
    
    score = 0
    q1 = st.selectbox("1. Which ISA requires a written report on internal control weaknesses?", ["", "ISA 230", "ISA 265", "ISA 200"])
    q2 = st.radio("2. What is the standard 'Assembly Period' for audit files under ISA 230?", ["30 days", "60 days", "90 days"])
    q3 = st.radio("3. True or False: ISA 240 says management is primarily responsible for preventing fraud.", ["True", "False"])

    if st.button("Submit Quiz"):
        if q1 == "ISA 265": score += 1
        if q2 == "60 days": score += 1
        if q3 == "True": score += 1
        
        st.write(f"### Your Score: {score}/3")
        if score == 3:
            st.success("Mastery Achieved! You have a solid grasp of the General Principles.")
        else:
            st.warning("Review the 'Full Library' tab to brush up on the specifics.")
    st.markdown('</div>', unsafe_allow_html=True)

# Summary for Website
st.divider()
st.markdown("""
### 📌 Module Summary for 'Knowledge Folder'
*   **ISA 200:** The foundation (Skepticism & Assurance).
*   **ISA 210/220:** Setting up the engagement and quality.
*   **ISA 230:** The evidence trail.
*   **ISA 240/250:** Dealing with the 'bad stuff' (Fraud & Illegal acts).
*   **ISA 260/265:** Effective communication with leadership.
""")