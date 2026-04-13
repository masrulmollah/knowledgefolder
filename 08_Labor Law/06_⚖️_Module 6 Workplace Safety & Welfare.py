import streamlit as st

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🏥 Module 6: Workplace Safety & Welfare</h1>", unsafe_allow_html=True)
st.write("---")

st.info("""
**Finance Objective:** Budgeting for mandatory welfare facilities. 
Non-compliance here can lead to heavy fines and "Blacklisting" by international buyers.
""")

# --- SECTION 1: MANDATORY WELFARE FACILITIES ---
st.header("1. Facilities Based on Workforce Size")
st.write("Does your establishment meet these statutory requirements?")

staff_count = st.number_input("Total Number of Workers", value=100)
female_count = st.number_input("Number of Female Workers", value=50)

st.subheader("Your Statutory Requirements:")

if staff_count >= 10:
    st.write("✅ **First Aid Box:** Mandatory (1 per 150 workers).")
if staff_count >= 50:
    st.write("✅ **Safety Committee:** Must be formed with worker representatives.")
if staff_count >= 100:
    st.error("🚨 **Group Insurance:** Mandatory for 100+ permanent workers.")
if staff_count >= 250:
    st.write("✅ **Canteen:** Mandatory for establishments with 250+ workers.")
if female_count >= 40:
    st.write("✅ **Rooms for Children (Creche):** Mandatory for 40+ female workers.")

st.divider()

# --- SECTION 2: SAFETY & ACCIDENTS ---
st.header("2. 🩹 Accident Compensation")
st.write("If an injury occurs during work, the employer is liable for compensation.")

with st.expander("Compensation Tiers (General Guide)"):
    st.markdown("""
    * **Death:** Compensation to be deposited to Labor Court (approx. BDT 2-4 Lakhs depending on sector/amendments).
    * **Permanent Total Disablement:** Compensation based on loss of earning capacity.
    * **Temporary Disablement:** Full wages for first 2 months, then partial.
    """)

# --- SECTION 3: GROUP INSURANCE ---
st.header("3. 🛡️ Group Insurance (Section 99)")
st.warning("If you have 100+ permanent workers, you must have a Group Insurance policy.")
st.write("""
**Accounting Note:** The premiums are a business expense. Ensure the 'Death Benefit' is 
clearly defined in the policy to match or exceed Labor Act requirements.
""")

# --- QUIZ ---
st.header("4. 🧠 Welfare Quiz")
q_welfare = st.radio("At what number of female workers is a 'Children's Room' (Creche) mandatory?", [20, 30, 40])

if st.button("Check Answer"):
    if q_welfare == 40:
        st.success("Correct! Section 94 mandates a room for children under the age of 6 if 40+ women are employed.")
        st.balloons()
    else:
        st.error("Incorrect. The threshold is 40 female workers.")