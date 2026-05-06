import streamlit as st

# Custom Styling for the Risk Module
st.markdown("""
    <style>
    .risk-title { color: #d35400; font-size: 32px; font-weight: bold; margin-bottom: 20px; }
    .standard-box { 
        background-color: #fef9e7; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 5px solid #f39c12;
        margin-bottom: 15px;
    }
    .formula-box {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    .quiz-container { background-color: #f2f4f4; padding: 20px; border-radius: 10px; border-top: 5px solid #d35400; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="risk-title">ISA 300–499: Risk Assessment & Response</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Standards Library", "🧮 Materiality & Risk", "💡 Scenarios", "🧠 Quiz"])

with tab1:
    st.info("These standards cover how we plan the audit and react to what we find.")
    
    isa_300_data = [
        {"id": "ISA 300", "title": "Planning an Audit", "desc": "Establishes the audit strategy and plan. Planning is an iterative process, not a discrete phase."},
        {"id": "ISA 315 (Revised)", "title": "Identifying & Assessing Risks", "desc": "The most important standard in this series. Requires understanding the entity's IT environment and 'Spectrum of Inherent Risk'."},
        {"id": "ISA 320", "title": "Materiality", "desc": "Setting thresholds for what matters. Includes Overall Materiality, Performance Materiality, and Threshold for Trivial Misstatements."},
        {"id": "ISA 330", "title": "The Auditor’s Responses", "desc": "How we respond to risks through 'Tests of Controls' and 'Substantive Procedures'."},
        {"id": "ISA 402", "title": "Service Organizations", "desc": "Used when the client outsources functions (like payroll or cloud accounting). Requires 'Type 1' or 'Type 2' reports."},
        {"id": "ISA 450", "title": "Evaluation of Misstatements", "desc": "How to handle errors found. Auditors must accumulate all misstatements except those that are clearly trivial."}
    ]

    for isa in isa_300_data:
        with st.expander(f"{isa['id']}: {isa['title']}"):
            st.write(isa['desc'])

with tab2:
    st.subheader("The Audit Risk Model")
    st.markdown('<div class="formula-box">Audit Risk = Inherent Risk × Control Risk × Detection Risk</div>', unsafe_allow_html=True)
    st.write("")
    st.write("""
    - **Inherent Risk (IR):** Susceptibility of an assertion to misstatement (e.g., complex derivatives have high IR).
    - **Control Risk (CR):** Risk that internal controls won't prevent or detect a misstatement.
    - **Detection Risk (DR):** The only component the auditor controls. We lower DR by doing more work.
    """)
    
    st.divider()
    st.subheader("Materiality (ISA 320)")
    st.write("**Performance Materiality:** Usually 50% to 75% of overall materiality. It provides a 'buffer' to catch aggregated small errors that could become material.")

with tab3:
    st.subheader("Practical Mastery Scenarios")
    
    with st.container():
        st.write("### 🏢 Scenario: The Complex IT System (ISA 315)")
        st.info("The client implemented a new SAP system mid-year. **Action:** You must evaluate General IT Controls (GITCs). If GITCs are weak, you cannot rely on automated reports and must do heavy substantive testing.")
        
        st.write("### 💰 Scenario: Adjusting Materiality (ISA 320)")
        st.info("Mid-audit, you find that the company’s actual profit is 40% lower than the forecast used to set materiality. **Action:** You must revise materiality downward and likely increase your sample sizes.")

with tab4:
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("Mastery Check: Risk & Response")
    
    q1 = st.selectbox("1. If Inherent Risk and Control Risk are both HIGH, what must the auditor do to Detection Risk?", 
                      ["", "Keep it the same", "Lower it (increase work)", "Raise it (decrease work)"])
    
    q2 = st.radio("2. Which ISA requires the testing of 'Significant Risks' specifically?", 
                  ["ISA 300", "ISA 315", "ISA 330"])

    if st.button("Submit Mastery Test"):
        if q1 == "Lower it (increase work)" and q2 == "ISA 330":
            st.success("Perfect! You understand the relationship between risk assessment and the audit response.")
        else:
            st.error("Not quite. Remember: To keep Audit Risk low, if IR/CR are high, you MUST lower Detection Risk by working harder.")
    st.markdown('</div>', unsafe_allow_html=True)