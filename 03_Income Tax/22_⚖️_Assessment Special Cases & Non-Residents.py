import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 🌐 Assessment Special Cases & Non-Residents")
st.markdown("#### Provisions under (Sections 189–202) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Special Cases Guide")
menu = st.sidebar.radio("Go to:", 
    ["Representative Assessees", "Non-Resident Agents", "Deceased & Departing Persons", "Discontinued Business"])

if menu == "Representative Assessees":
    st.markdown("##### **Who is a Representative Assessee? (Section 189)**")
    st.write("A representative is someone legally responsible for the tax affairs of another person.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**For Minors/Lunatics:** Guardians or Managers.")
        st.info("**For Trusts:** The Trustees.")
    with col2:
        st.info("**For Court of Wards:** The Administrator.")
        st.info("**For Non-Residents:** Their Agents in Bangladesh.")
    
    st.warning("Critical Rule: The tax liability of the representative is exactly the same as that of the principal.")

elif menu == "Non-Resident Agents":
    st.markdown("##### **Agents of Non-Residents (Section 190)**")
    st.write("The DCT may treat any of the following as an 'Agent' of a non-resident:")
    st.write("1. Anyone in Bangladesh employed by or on behalf of the non-resident.")
    st.write("2. Anyone through whom the non-resident is in receipt of any income.")
    st.write("3. Anyone who has a business connection with the non-resident.")
    
    st.markdown("**Right to Retain:**")
    st.write("An agent who pays tax for a non-resident has the legal right to retain the amount from the non-resident's money in their possession.")

elif menu == "Deceased & Departing Persons":
    st.markdown("##### **Special Timing & Liabilities**")
    
    st.markdown("**1. Deceased Persons (Section 191)**")
    st.write("- The legal heir/representative must file the return and pay the tax.")
    st.write("- Liability is limited to the extent to which the estate is capable of meeting the charge.")

    st.markdown("**2. Persons Leaving Bangladesh (Section 192)**")
    st.error("Accelerated Assessment:")
    st.write("If someone is leaving Bangladesh for good, the DCT can demand a return and tax payment immediately for the current financial year up to the date of departure.")

elif menu == "Discontinued Business":
    st.markdown("##### **Closing a Business (Section 193)**")
    st.write("If you discontinue your business or profession:")
    st.write("- You must inform the DCT within **15 days** of the discontinuance.")
    st.write("- You must file a separate return for the period from the start of the year to the date of closing.")
    
    st.info("💡 **Finance Lead Note:** For factory operations, ensuring a 'Tax Clearance Certificate' is obtained during any formal winding up or asset disposal is vital to protect the directors from personal liability.")

st.divider()