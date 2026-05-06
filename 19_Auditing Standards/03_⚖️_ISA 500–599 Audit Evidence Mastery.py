import streamlit as st

# Professional styling for Audit Evidence
st.markdown("""
    <style>
    .evidence-title { color: #0b5345; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .evidence-card { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 5px solid #117a65;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .concept-tag {
        background-color: #e8f8f5;
        color: #117a65;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.85em;
        font-weight: bold;
        margin-right: 5px;
    }
    .quiz-box { background-color: #f4fbf9; padding: 20px; border-radius: 10px; border: 1px solid #117a65; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="evidence-title">ISA 500–599: Audit Evidence Mastery</p>', unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 The Evidence Library", "🔍 Evidence Types", "💡 Case Studies", "🧠 Quiz"])

with tab1:
    st.info("Evidence is the information used by the auditor in arriving at the conclusions on which the auditor’s opinion is based.")
    
    # Complete list of ISAs in the 500 series
    isa_500_data = [
        {"id": "ISA 500", "title": "Audit Evidence", "desc": "Defines what constitutes audit evidence and the requirement to obtain sufficient appropriate evidence."},
        {"id": "ISA 501", "title": "Specific Considerations", "desc": "Focuses on Inventory (attendance at counts), Litigation/Claims, and Segment Information."},
        {"id": "ISA 505", "title": "External Confirmations", "desc": "Direct written responses from third parties (e.g., Banks, Debtors). Positive vs. Negative confirmations."},
        {"id": "ISA 510", "title": "Initial Engagements", "desc": "Focuses on opening balances and ensuring they don't contain material misstatements."},
        {"id": "ISA 520", "title": "Analytical Procedures", "desc": "Using ratios and trends to find anomalies. Mandatory during planning and final review."},
        {"id": "ISA 530", "title": "Audit Sampling", "desc": "Using statistical or non-statistical sampling to provide a basis for conclusions about a population."},
        {"id": "ISA 540", "title": "Auditing Accounting Estimates", "desc": "Focuses on 'Estimation Uncertainty' (e.g., Fair value, Provisions, Depreciation)."},
        {"id": "ISA 550", "title": "Related Parties", "desc": "Ensures all related party relationships and transactions are identified and disclosed."},
        {"id": "ISA 560", "title": "Subsequent Events", "desc": "Responsibilities for events occurring between the date of financial statements and the auditor's report."},
        {"id": "ISA 570", "title": "Going Concern", "desc": "Evaluating management's assessment of the entity's ability to continue for at least 12 months."},
        {"id": "ISA 580", "title": "Written Representations", "desc": "Management's formal letter confirming they have fulfilled their responsibilities."}
    ]

    for isa in isa_500_data:
        with st.expander(f"{isa['id']}: {isa['title']}"):
            st.write(isa['desc'])

with tab2:
    st.subheader("The Quality of Evidence")
    st.markdown('<span class="concept-tag">Sufficient = Quantity</span> <span class="concept-tag">Appropriate = Quality</span>', unsafe_allow_html=True)
    st.write("")
    
    cols = st.columns(2)
    with cols[0]:
        st.write("### Methods of Collection")
        st.write("- **Inspection:** Examining records or assets.")
        st.write("- **Observation:** Watching a process (e.g., inventory count).")
        st.write("- **Inquiry:** Seeking information from people inside/outside.")
        st.write("- **Recalculation:** Checking mathematical accuracy.")
    
    with cols[1]:
        st.write("### Reliability Rules")
        st.write("✅ **External** is more reliable than Internal.")
        st.write("✅ **Directly obtained** is better than Indirectly.")
        st.write("✅ **Documentary** is better than Oral.")
        st.write("✅ **Originals** are better than Photocopies.")

with tab3:
    st.subheader("Mastery Case Studies")
    
    st.write("### 🏦 Scenario: Bank Confirmation (ISA 505)")
    st.info("The client says they don't want you to send a confirmation to a specific bank because the relationship is 'sensitive.' **Action:** This is a scope limitation. You must evaluate management's reasons and consider the impact on your opinion.")

    st.write("### 🏭 Scenario: Inventory Count (ISA 501)")
    st.info("The inventory is held at a remote location you cannot visit. **Action:** You must perform alternative procedures, like inspecting documentation of subsequent sale of those items, or hire another auditor to attend on your behalf.")

with tab4:
    st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
    st.subheader("Audit Evidence Mastery Quiz")
    
    q1 = st.radio("1. Which ISA deals with 'Subsequent Events'?", 
                  ["ISA 550", "ISA 560", "ISA 570"])
    
    q2 = st.selectbox("2. If an auditor uses a trend analysis to identify an anomaly, they are performing:", 
                      ["", "Analytical Procedures", "Recalculation", "Inquiry"])
    
    q3 = st.radio("3. Written Representations (ISA 580) can be used as a substitute for other evidence.", 
                  ["True", "False"])

    if st.button("Submit Evidence Test"):
        score = 0
        if q1 == "ISA 560": score += 1
        if q2 == "Analytical Procedures": score += 1
        if q3 == "False": score += 1
        
        if score == 3:
            st.success("Mastery Confirmed! You understand how to build a strong audit case.")
        else:
            st.warning(f"Score: {score}/3. Remember: ISA 580 (Representations) is NOT a substitute for other evidence.")
    st.markdown('</div>', unsafe_allow_html=True)