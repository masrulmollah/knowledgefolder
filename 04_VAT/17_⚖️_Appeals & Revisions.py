import streamlit as st

# --- DO NOT CALL set_page_config HERE (Handled by Homepage) ---

# --- STANDARD WEBPAGE STYLING ---
st.markdown("""
    <style>
    html, body, [class*="st-"] {
        font-size: 16px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1 { font-size: 2.1rem !important; color: #1E3A8A !important; }
    h2 { font-size: 1.6rem !important; color: #1E40AF !important; margin-top: 1.5rem !important; }
    h3 { font-size: 1.25rem !important; color: #1E40AF !important; }
    p, li { font-size: 1rem !important; line-height: 1.6; color: #374151; }
    
    .appeal-step {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 12px;
    }
    .deposit-warning {
        background-color: #fffbeb;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #f59e0b;
        color: #92400e;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Litigation Management")
st.sidebar.info("Sections 121-135: Challenging Tax Demands.")

# --- HEADER ---
st.title("Appeals, Revisions & ADR")
st.markdown("#### Sections 121-135 | VAT & SD Act, 2012")
st.divider()

# --- 1. APPEAL HIERARCHY ---
st.subheader("🏛️ The Appellate Hierarchy")

st.markdown("""
<div class="appeal-step">
    <b>Level 1: Commissioner (Appeals)</b><br>
    Time Limit: 90 Days | Form: Mushak-12.1
</div>
<div class="appeal-step">
    <b>Level 2: Appellate Tribunal</b><br>
    Time Limit: 90 Days | Requires 10% Additional Deposit
</div>
<div class="appeal-step">
    <b>Level 3: High Court Division (Revision)</b><br>
    Time Limit: 90 Days | Applicable only on points of law.
</div>
""", unsafe_allow_html=True)

# --- 2. MANDATORY DEPOSITS ---
st.subheader("💰 Mandatory Pre-deposits")
st.markdown("""
To discourage frivolous litigation, the law requires a 'skin in the game' 
before an appeal is heard:
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="deposit-warning">Appeal to Commissioner:<br>10% of Disputed Tax</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="deposit-warning">Appeal to Tribunal:<br>10% of Disputed Tax</div>', unsafe_allow_html=True)

# --- 3. ALTERNATIVE DISPUTE RESOLUTION (ADR) ---
st.subheader("🤝 Alternative Dispute Resolution (ADR)")
st.write("""
ADR is a mechanism to resolve disputes outside the formal court system through 
mutually appointed facilitators.
""")
with st.expander("Why choose ADR?"):
    st.write("""
    * **Speed:** Faster resolution compared to the Tribunal or High Court.
    * **Finality:** Once an agreement is signed in ADR, it is binding and cannot be appealed further.
    * **Cost:** Avoids lengthy legal fees and 2% monthly interest accumulation during the trial.
    """)

# --- 4. MISCELLANEOUS PROVISIONS ---
st.subheader("📝 Miscellaneous")
st.markdown("""
* **Section 121 (Revision):** The Commissioner can revise any order passed by a subordinate officer if it is found incorrect.
* **Condonation of Delay:** The appellate authority may accept an appeal after 90 days if 'sufficient cause' for the delay is shown.
* **Service of Notice:** Notices are considered served if sent to the registered email or the physical address in the IVAS system.
""")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For a factory, tax litigation can freeze huge amounts 
of cash in 'Mandatory Deposits'. Before filing an appeal, conduct a 
**Cost-Benefit Analysis**. If the chance of winning is low, **ADR** is often 
the better route to settle and avoid the 2% monthly interest that continues 
to accrue while the case is pending in the Tribunal.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Appeals & Litigation Module © 2026</center>", unsafe_allow_html=True)