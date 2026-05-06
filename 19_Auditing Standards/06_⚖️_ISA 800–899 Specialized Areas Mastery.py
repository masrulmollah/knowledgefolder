import streamlit as st

# Styling for the Specialized Module
st.markdown("""
    <style>
    .special-title { color: #283747; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .special-card { 
        background-color: #f2f3f4; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 5px solid #283747;
        margin-bottom: 15px;
    }
    .warning-box {
        background-color: #fdf2f2;
        border: 1px solid #ec7063;
        padding: 15px;
        color: #943126;
        border-radius: 5px;
        font-size: 0.9em;
    }
    .quiz-container { background-color: #ebf5fb; padding: 20px; border-radius: 10px; border: 1px solid #2e86c1; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="special-title">ISA 800–899: Specialized Areas Mastery</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Specialized Library", "⚖️ Framework Types", "💡 Practical Scenarios", "🧠 Quiz"])

with tab1:
    st.info("These standards cover audits of financial statements prepared in accordance with special purpose frameworks.")
    
    isa_800_data = [
        {
            "id": "ISA 800 (Revised)", 
            "title": "Special Purpose Frameworks", 
            "desc": "Used when auditing statements prepared for specific users. Examples: Tax basis, Cash basis, or financial reporting requirements of a regulator."
        },
        {
            "id": "ISA 805 (Revised)", 
            "title": "Single Financial Statements / Specific Elements", 
            "desc": "Applied when you are asked to audit ONLY a Balance Sheet, or ONLY an Accounts Receivable schedule, rather than a full set of accounts."
        },
        {
            "id": "ISA 810 (Revised)", 
            "title": "Engagements to Report on Summary Financial Statements", 
            "desc": "Procedures for when an auditor is asked to report on 'condensed' or summary financial statements derived from a full audited set."
        }
    ]

    for isa in isa_800_data:
        with st.expander(f"{isa['id']}: {isa['title']}"):
            st.write(isa['desc'])

with tab2:
    st.subheader("General vs. Special Purpose")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### General Purpose")
        st.write("- Designed for a wide range of users.")
        st.write("- Examples: IFRS, GAAP.")
        st.write("- **ISA 700 series applies.**")
    
    with col2:
        st.write("### Special Purpose")
        st.write("- Designed for specific users (e.g., Lenders, Tax Authorities).")
        st.write("- **ISA 800 series applies.**")
        st.markdown('<div class="warning-box">Must include an "Emphasis of Matter" to alert users that the FS are prepared for a specific purpose.</div>', unsafe_allow_html=True)

with tab3:
    st.subheader("Mastery Scenarios")
    
    st.write("### 🏦 Scenario: The Bank Loan (ISA 805)")
    st.info("A bank requires an audit of just the 'Inventory' and 'Accounts Receivable' of a company to secure a loan. **Action:** You apply ISA 805. You must ensure that the audit of these specific elements provides enough evidence despite not auditing the whole company.")

    st.write("### 📄 Scenario: The Annual Highlights (ISA 810)")
    st.info("The client wants to publish a 2-page 'Summary Financial Statement' in their marketing brochure. **Action:** You must compare the summary to the full audited accounts and ensure it is not misleading and is consistent with the full version.")

with tab4:
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("Specialized Areas Mastery Quiz")
    
    q1 = st.radio("1. Which standard applies if you are auditing a 'Cash Basis' set of accounts for a regulator?", 
                  ["ISA 700", "ISA 800", "ISA 810"])
    
    q2 = st.radio("2. Can an auditor audit a single financial statement (like just the Income Statement)?", 
                  ["Yes, under ISA 805", "No, ISAs require a full set", "Only for government entities"])
    
    q3 = st.selectbox("3. In an ISA 800 report, the auditor MUST include:", 
                      ["", "A disclaimer of opinion", "An Emphasis of Matter paragraph", "The names of all shareholders"])

    if st.button("Check Specialized Knowledge"):
        score = 0
        if q1 == "ISA 800": score += 1
        if q2 == "Yes, under ISA 805": score += 1
        if q3 == "An Emphasis of Matter paragraph": score += 1
        
        if score == 3:
            st.success("Mastery Achieved! You have completed the entire ISA framework.")
        else:
            st.warning(f"Score: {score}/3. Remember: ISA 800 reports always need an alert to the reader (EoM).")
    st.markdown('</div>', unsafe_allow_html=True)

# Final Completion Summary
st.divider()
st.balloons()
st.subheader("🏁 Congratulations!")
st.write("""
You have now built a complete **ISA Knowledge Repository**. 
From General Principles (200) to Specialized Areas (800), your website is now a powerful resource for professional audit guidance.
""")