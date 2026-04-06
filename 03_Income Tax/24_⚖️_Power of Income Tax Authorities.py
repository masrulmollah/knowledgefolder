import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 🔍 Powers of Income Tax Authorities")
st.markdown("#### Search and Seizure| Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Enforcement Guide")
menu = st.sidebar.radio("Go to:", 
    ["Civil Court Powers", "Inspection & Entry", "Search and Seizure", "Retention Rules"])

if menu == "Civil Court Powers":
    st.markdown("##### **Judicial Powers (Section 204)**")
    st.write("Income tax authorities (DCT, Joint Commissioner, etc.) are granted powers similar to a Civil Court under the Code of Civil Procedure.")
    
    st.info("**Core Powers:**")
    st.write("- **Summoning:** Compelling a person to appear and give evidence.")
    st.write("- **Discovery:** Compelling the production of any book of account or document.")
    st.write("- **Oaths:** Examining any person under a formal oath.")
    
    st.warning("Failure to comply with a summons can lead to a fine or prosecution under the Penal Code.")

elif menu == "Inspection & Entry":
    st.markdown("##### **Power of Survey (Section 205)**")
    st.write("An income tax authority may enter any place of business or profession within their jurisdiction.")
    
    st.markdown("**What can they do during a Survey?**")
    st.write("1. Inspect books of account and documents.")
    st.write("2. Verify cash, stock, or other valuable articles found on the premises.")
    st.write("3. Record statements of any person present.")
    st.write("4. Place identification marks on records or take copies.")
    
    st.info("💡 **Finance Lead Note:** Ensure that the 'Cash Book' and 'Stock Register' are updated daily at the factory, as these are the primary targets during a surprise inspection.")

elif menu == "Search and Seizure":
    st.markdown("##### **The Power to Search (Section 209)**")
    st.write("If the Director General or Commissioner has 'Reason to Believe' that tax evasion is occurring, they may authorize a search.")
    
    st.error("**Authorized Actions:**")
    st.write("- Enter and search any building, vessel, or vehicle.")
    st.write("- Break open doors, windows, or safes if access is denied.")
    st.write("- Seize any books of account, money, or valuables representing undisclosed income.")
    st.write("- Search any person leaving the premises.")
    
    st.markdown("**Presumption of Ownership:**")
    st.write("Anything found in the possession of a person during a search is presumed to belong to that person unless proven otherwise.")

elif menu == "Retention Rules":
    st.markdown("##### **Retention of Seized Material (Section 210)**")
    st.write("Authorities cannot keep seized items indefinitely.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Books of Accounts**")
        st.write("- Can be kept for **180 days**.")
        st.write("- Requires written approval from the Commissioner for longer retention.")
        
    with col2:
        st.markdown("**Money & Assets**")
        st.write("- Assets are used to satisfy the tax and penalty determined in the assessment.")
        st.write("- Surplus must be returned to the owner.")

st.divider()