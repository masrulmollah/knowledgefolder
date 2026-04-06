import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 📥 Recovery of Tax Summary")
st.markdown("#### Provisions under (Sections 214–222) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Recovery Mechanisms")
menu = st.sidebar.radio("Go to:", 
    ["Assessee in Default", "Garnishee Orders", "Tax Recovery Officer (TRO)", "Stay & Installments"])

if menu == "Assessee in Default":
    st.markdown("##### **Notice of Demand (Section 214)**")
    st.write("When any tax, interest, or penalty is due, the DCT serves a 'Notice of Demand' specifying the amount and the time limit for payment (usually 15 to 30 days).")
    
    st.error("**Definition:** If payment is not made within the time limit, the taxpayer is legally classified as an **'Assessee in Default'**.")
    
    st.markdown("**Key Consequences:**")
    st.write("1. Immediate initiation of recovery proceedings.")
    st.write("2. Potential freezing of bank accounts.")
    st.write("3. Possible restrictions on traveling abroad.")

elif menu == "Garnishee Orders":
    st.markdown("##### **Recovery from Third Parties (Section 221)**")
    st.write("This is one of the most effective tools for tax collection. The DCT can bypass the taxpayer and collect directly from those who owe the taxpayer money.")
    
    st.info("**Who can receive a Garnishee Notice?**")
    st.write("- **Banks:** To freeze and remit funds from the taxpayer's account.")
    column1, column2 = st.columns(2)
    with column1:
        st.write("- **Employers:** To deduct arrears from monthly salary.")
    with column2:
        st.write("- **Debtors:** Any person owing money to the assessee.")
    
    st.warning("Compliance is mandatory. If the third party fails to comply, they become personally liable for the tax amount.")

elif menu == "Tax Recovery Officer (TRO)":
    st.markdown("##### **Powers of the Tax Recovery Officer (Section 215)**")
    st.write("When simple notices fail, the case is referred to a TRO who acts with judicial powers.")
    
    st.markdown("**Methods of Recovery:**")
    st.write("1. **Attachment:** Legally seizing movable property (vehicles, stock) or immovable property (land, buildings).")
    st.write("2. **Auction:** Selling attached property to recover the dues.")
    st.write("3. **Arrest:** In extreme cases of willful default, the TRO can order the civil imprisonment of the taxpayer.")
    st.write("4. **Receivership:** Appointing a manager to run the taxpayer's business to generate funds for tax payment.")

elif menu == "Stay & Installments":
    st.markdown("##### **Relief and Stay of Recovery**")
    st.write("The Act provides some room for negotiation if the taxpayer is facing genuine hardship.")
    
    st.success("**Installment Facility:**")
    st.write("The DCT may allow the tax to be paid in several installments upon a formal written request.")
    
    st.markdown("**Stay of Demand:**")
    st.write("If an appeal is filed before the Taxes Appellate Tribunal or High Court, the recovery may be 'stayed' (paused) until the case is decided, often conditional on paying a portion of the tax (e.g., 10% or 25%).")

    st.info("💡 **Finance Lead Note:** For a factory, a Garnishee order on a primary operations account can halt production. Always respond to 'Notice of Demand' letters immediately to avoid escalation to the TRO.")

st.divider()