import streamlit as st

# Styling for the Collaboration Module
st.markdown("""
    <style>
    .collab-title { color: #512e5f; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .collab-card { 
        background-color: #f4ecf7; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 5px solid #8e44ad;
        margin-bottom: 15px;
    }
    .responsibility-box {
        background-color: #fdf2f9;
        border: 2px dashed #c0392b;
        padding: 15px;
        color: #922b21;
        font-weight: bold;
        text-align: center;
    }
    .quiz-box { background-color: #f5eef8; padding: 20px; border-radius: 10px; border: 1px solid #8e44ad; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="collab-title">ISA 600–699: Using the Work of Others</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 The Collaboration Library", "⚖️ The Responsibility Rule", "💡 Practical Scenarios", "🧠 Quiz"])

with tab1:
    st.info("These standards define how the principal auditor interacts with other parties to gain assurance.")
    
    isa_600_data = [
        {
            "id": "ISA 600 (Revised)", 
            "title": "Group Audits", 
            "desc": "Special considerations for audits of group financial statements (subsidiaries, branches). Focuses on the 'Group Engagement Team' vs 'Component Auditors'."
        },
        {
            "id": "ISA 610 (Revised)", 
            "title": "Using the Work of Internal Auditors", 
            "desc": "How the external auditor can use the work of the internal audit function or get direct assistance from them. Requires assessing their 'Objectivity' and 'Competence'."
        },
        {
            "id": "ISA 620", 
            "title": "Using the Work of an Auditor’s Expert", 
            "desc": "Used when expertise in a field other than accounting/auditing is needed (e.g., a surveyor for property valuation or an actuary for pension liabilities)."
        }
    ]

    for isa in isa_600_data:
        with st.expander(f"{isa['id']}: {isa['title']}"):
            st.write(isa['desc'])

with tab2:
    st.subheader("The 'Sole Responsibility' Principle")
    st.markdown("""
    <div class="responsibility-box">
        The auditor has sole responsibility for the audit opinion expressed. 
        That responsibility is not reduced by the auditor’s use of the work of others.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("### When using others, you must evaluate:")
    cols = st.columns(3)
    with cols[0]:
        st.write("**1. Competence**")
        st.caption("Do they have the skills and professional qualifications?")
    with cols[1]:
        st.write("**2. Objectivity**")
        st.caption("Are they free from bias or conflict of interest?")
    with cols[2]:
        st.write("**3. Adequacy**")
        st.caption("Is their work sufficient for the auditor's purposes?")

with tab3:
    st.subheader("Mastery Scenarios")
    
    st.write("### 🏢 Scenario: The Foreign Subsidiary (ISA 600)")
    st.info("Your client has a branch in Brazil audited by a local firm. **Action:** You must evaluate the component auditor's ethics and competence. You may need to review their working papers or perform additional tests on the 'group' consolidation.")

    st.write("### 🏗️ Scenario: The Property Valuation (ISA 620)")
    st.info("The client's land is valued at $500M by an independent surveyor. **Action:** You must evaluate the surveyor's expertise, the assumptions they used (e.g., market rates), and the source data to ensure the valuation isn't overstated.")

with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Collaboration Mastery Quiz")
    
    q1 = st.radio("1. When using an internal auditor (ISA 610), what is the most critical factor to assess?", 
                  ["Their salary", "Their objectivity and technical competence", "The number of people in their team"])
    
    q2 = st.radio("2. If an Auditor's Expert (ISA 620) makes a mistake, who is ultimately responsible for the audit opinion?", 
                  ["The Expert", "The Client", "The Auditor"])
    
    q3 = st.selectbox("3. ISA 600 applies specifically to:", 
                      ["", "Individual small audits", "Group financial statements and subsidiaries", "Only government audits"])

    if st.button("Check Collaboration Knowledge"):
        score = 0
        if q1 == "Their objectivity and technical competence": score += 1
        if q2 == "The Auditor": score += 1
        if q3 == "Group financial statements and subsidiaries": score += 1
        
        if score == 3:
            st.success("Mastery Achieved! You understand how to maintain control while using external help.")
        else:
            st.warning(f"Score: {score}/3. Review the 'Sole Responsibility' principle again.")
    st.markdown('</div>', unsafe_allow_html=True)