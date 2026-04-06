import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### ⚖️ Assessment Procedures Summary")
st.markdown("#### According to the Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
section = st.sidebar.radio("Select Section:", 
                           ["Self-Assessment", "Best Judgment", "Special Assessments", "Time Limits"])

if section == "Self-Assessment":
    st.markdown("##### **Universal Self-Assessment (Section 167)**")
    st.write("This is the default method for most taxpayers in Bangladesh.")
    st.write("- **The Concept:** You calculate your income, pay the tax, and file the return.")
    st.write("- **Deemed Assessment:** The acknowledgment slip provided by the tax office serves as your assessment order.")
    st.info("The tax office can still select your file for an 'Audit' within a specified timeframe to verify accuracy.")

elif section == "Best Judgment":
    st.markdown("##### **Best Judgment Assessment (Section 180)**")
    st.write("The tax officer (DCT) can determine your tax liability based on their 'Best Judgment' if:")
    st.write("1. You **fail to file** a return by the deadline (Tax Day).")
    st.write("2. You fail to respond to a formal notice to provide documents/accounts.")
    st.write("3. Your submitted accounts are found to be **grossly unreliable**.")
    st.error("Warning: Best Judgment assessments often result in higher tax liabilities and penalties.")

elif section == "Special Assessments":
    st.markdown("##### **Provisional & Search-based Assessments**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Provisional (Sec 176)**")
        st.write("Used to secure revenue when a filed return is clearly deficient.")
        
    with col2:
        st.markdown("**Search & Seizure (Sec 181)**")
        st.write("Special assessment following a raid or discovery of hidden assets.")

elif section == "Time Limits":
    st.markdown("##### **Statute of Limitations (Section 182)**")
    st.write("The tax authorities cannot keep your tax file 'open' indefinitely.")
    
    st.success("**The 2-Year Rule:**")
    st.write("Generally, an assessment must be completed within **two years** from the end of the assessment year in which the return was filed.")
    
    st.write("- **Re-opening Cases:** If the DCT finds evidence of 'tax evasion' or 'omission', they may re-open a case within a longer statutory window (usually 6 years).")

# Bottom spacing
st.write("")
st.divider()