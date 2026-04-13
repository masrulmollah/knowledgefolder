import streamlit as st

# We do NOT use 'def' or 'if __name__' here to ensure it runs immediately
# We also avoid st.set_page_config to prevent the error you had earlier

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>📘 Module 1: Legal Framework</h1>", unsafe_allow_html=True)
st.write("---")

st.info("""
**Audience:** Finance & Accounts Professionals  
**Objective:** Refresh knowledge on the legal structure of Labor Laws in Bangladesh.
""")

# --- SECTION 1: HIERARCHY ---
st.header("1. The Legal Hierarchy")
col1, col2 = st.columns(2)

with col1:
    st.subheader("The Foundations")
    st.markdown("""
    * **Bangladesh Labour Act, 2006:** The main law.
    * **Bangladesh Labour Rules, 2015:** The 'Manual' for calculations.
    """)

with col2:
    st.subheader("Key Updates")
    st.markdown("""
    * **2023 Amendment:** 120 days Maternity Leave.
    * **EPZ Labor Act:** Different rules for EPZ areas.
    """)

# --- SECTION 2: INTERACTIVE DEFINITIONS ---
st.header("2. Knowledge Refresher")
topic = st.selectbox("Select a term to define:", ["Worker", "Wages", "Employer"])

if topic == "Worker":
    st.success("**Definition:** Any person employed to do manual, technical, or clerical work.")
    st.warning("**Finance Note:** This defines who gets Overtime and WPPF.")
elif topic == "Wages":
    st.success("**Definition:** Includes Basic, House Rent, Medical, and Bonuses.")
    st.warning("**Finance Note:** Excludes PF and Gratuity.")
else:
    st.success("**Definition:** Person/Company that employs workers.")

# --- SECTION 3: QUIZ ---
st.divider()
st.header("3. Quick Quiz")
choice = st.radio("Is a Manager always considered a 'Worker'?", ["Yes", "No"])

if st.button("Submit Answer"):
    if choice == "No":
        st.balloons()
        st.success("Correct! Managerial roles are usually excluded from 'Worker' benefits.")
    else:
        st.error("Incorrect. Managers are generally classified as 'Employers' under the Act.")