import streamlit as st

# Styling for the Reporting Module
st.markdown("""
    <style>
    .report-title { color: #7b241c; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .report-card { 
        background-color: #fdf2e9; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 5px solid #a93226;
        margin-bottom: 15px;
    }
    .opinion-box {
        padding: 15px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin: 10px 0;
    }
    .unmodified { background-color: #d4efdf; color: #1d8348; border: 1px solid #1d8348; }
    .modified { background-color: #fcedec; color: #943126; border: 1px solid #943126; }
    .quiz-container { background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #a93226; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="report-title">ISA 700–799: Audit Conclusions & Reporting</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Reporting Standards", "⚖️ Types of Opinions", "💡 Practical Scenarios", "🧠 Quiz"])

with tab1:
    st.info("These standards dictate the form and content of the auditor’s report.")
    
    isa_700_data = [
        {"id": "ISA 700 (Revised)", "title": "Forming an Opinion", "desc": "Defines the standard 'Unmodified' report structure: Opinion, Basis for Opinion, Going Concern, and Responsibilities."},
        {"id": "ISA 701", "title": "Key Audit Matters (KAMs)", "desc": "Mandatory for listed entities. These are matters that required significant auditor attention (e.g., high-risk areas or major judgments)."},
        {"id": "ISA 705 (Revised)", "title": "Modifications to the Opinion", "desc": "When the auditor cannot issue a clean report. Covers Qualified, Adverse, and Disclaimer of opinion."},
        {"id": "ISA 706 (Revised)", "title": "Emphasis of Matter (EoM)", "desc": "Used to draw attention to a matter already disclosed in the financial statements that is fundamental to the user's understanding."},
        {"id": "ISA 710", "title": "Comparative Information", "desc": "Ensures the prior year's figures (corresponing figures or comparative financial statements) are correctly reported and audited."},
        {"id": "ISA 720 (Revised)", "title": "Other Information", "desc": "Auditor's responsibility regarding information in the Annual Report (e.g., Chairman’s Statement) that is NOT part of the financial statements."}
    ]

    for isa in isa_700_data:
        with st.expander(f"{isa['id']}: {isa['title']}"):
            st.write(isa['desc'])

with tab2:
    st.subheader("The Opinion Decision Tree")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="opinion-box unmodified">Unmodified Opinion</div>', unsafe_allow_html=True)
        st.caption("The 'Clean' Opinion. Financial statements present fairly, in all material respects.")
    
    with col2:
        st.markdown('<div class="opinion-box modified">Modified Opinion</div>', unsafe_allow_html=True)
        st.caption("Includes: Qualified (Except for...), Adverse (Do not present fairly), or Disclaimer (Cannot form opinion).")

    st.write("---")
    st.write("### Comparison Table")
    st.table({
        "Nature of Matter": ["Material but NOT Pervasive", "Material AND Pervasive"],
        "Financial Statements Misstated": ["Qualified Opinion", "Adverse Opinion"],
        "Inability to Obtain Evidence": ["Qualified Opinion", "Disclaimer of Opinion"]
    })

with tab3:
    st.subheader("Reporting Case Studies")
    
    st.write("### 🏢 Scenario: The Litigation (ISA 706)")
    st.info("The company is facing a massive lawsuit that could bankrupt them. It is properly disclosed in Note 15. **Action:** The auditor may add an 'Emphasis of Matter' paragraph to highlight this note without changing the clean opinion.")

    st.write("### 📉 Scenario: Missing Records (ISA 705)")
    st.info("A fire destroyed all purchase invoices for the last 6 months. You cannot verify 40% of the expenses. **Action:** This is an inability to obtain evidence. Since 40% is likely pervasive, you must issue a 'Disclaimer of Opinion'.")

with tab4:
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("Reporting Mastery Quiz")
    
    q1 = st.radio("1. Which ISA introduced Key Audit Matters (KAMs)?", 
                  ["ISA 700", "ISA 701", "ISA 705"])
    
    q2 = st.radio("2. If the financial statements are 'materially misstated' and the effect is 'pervasive', which opinion is used?", 
                  ["Qualified", "Adverse", "Disclaimer"])
    
    q3 = st.selectbox("3. An Emphasis of Matter (EoM) paragraph is used for:", 
                      ["", "Reporting a disagreement with management", "Highlighting a properly disclosed fundamental matter", "Correcting an error in the accounts"])

    if st.button("Submit Report Test"):
        score = 0
        if q1 == "ISA 701": score += 1
        if q2 == "Adverse": score += 1
        if q3 == "Highlighting a properly disclosed fundamental matter": score += 1
        
        if score == 3:
            st.success("Mastery Achieved! You are ready to sign off on the audit.")
        else:
            st.warning(f"Score: {score}/3. Remember: EoM (706) is only for matters *already* in the notes!")
    st.markdown('</div>', unsafe_allow_html=True)