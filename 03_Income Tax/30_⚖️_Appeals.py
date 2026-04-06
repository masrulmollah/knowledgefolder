import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### ⚖️ Appeal, Tribunal, & ADR ")
st.markdown("#### Provisions under (Sections 284–306) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Litigation Guide")
menu = st.sidebar.radio("Go to:", 
    ["First Appeal", "Appellate Tribunal", "High Court & Revision", "ADR (Fast Track)"])

if menu == "First Appeal":
    st.markdown("##### **Appeal to Commissioner (Appeals)**")
    st.write("If you disagree with the DCT's assessment, your first stop is the Commissioner (Appeals).")
    
    st.info("**Key Requirements:**")
    st.write("- **Deadline:** Must be filed within **60 days** of the notice of demand.")
    st.write("- **Payment:** You must pay 10% of the tax on the 'disputed income' (or as prescribed) before filing.")
    st.write("- **Form:** Must be submitted in the prescribed 'Form of Appeal'.")
    
    st.warning("The Commissioner (Appeals) can confirm, reduce, enhance, or annul the assessment.")

elif menu == "Appellate Tribunal":
    st.markdown("##### **Taxes Appellate Tribunal (Section 293)**")
    st.write("This is the second and highest 'fact-finding' authority.")
    
    st.success("**Who can Appeal?**")
    st.write("- The Taxpayer (if unhappy with the first appeal).")
    st.write("- The Commissioner (if they believe the first appeal order was too lenient).")
    
    st.markdown("**Timeline:**")
    st.write("- Must be filed within **60 days** of the first appeal order.")
    st.write("- Fees: Tk. 5,000 for taxpayers (Company/Individual).")

elif menu == "High Court & Revision":
    st.markdown("##### **Legal Interpretations & Revisions**")
    
    tab1, tab2 = st.tabs(["Reference to High Court", "Revision by Commissioner"])
    
    with tab1:
        st.write("**Reference (Section 302):**")
        st.write("This is NOT for facts, but for **Questions of Law**.")
        st.write("Must be filed within 90 days of the Tribunal's order.")
        
    with tab2:
        st.write("**Revision (Section 305):**")
        st.write("The Commissioner can 'Suo Motu' (on their own) or on application, revise any order passed by a subordinate officer if it is found to be incorrect.")

elif menu == "ADR (Fast Track)":
    st.markdown("##### **Alternative Dispute Resolution (ADR)**")
    st.write("ADR is a mechanism to resolve disputes outside the traditional court system.")
    
    st.success("**Why choose ADR?**")
    st.write("- **Speed:** Disputes are often settled within months rather than years.")
    st.write("- **Finality:** The agreement reached in ADR is generally binding and cannot be appealed further.")
    st.write("- **Confidentiality:** The proceedings are private.")
    
    st.info("💡 **Finance Lead Note:** For factory-level disputes (like disallowed depreciation or utility costs), ADR is often the most cost-effective way to clean up the company's tax ledger without multi-year legal fees.")

st.divider()