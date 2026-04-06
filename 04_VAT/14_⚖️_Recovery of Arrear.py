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
    
    .recovery-card {
        background-color: #fff5f5;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #c53030;
        margin-bottom: 12px;
    }
    .step-number {
        font-weight: bold;
        color: #c53030;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Recovery Protocol")
st.sidebar.warning("Section 95: Arrear tax recovery is a priority for NBR.")

# --- HEADER ---
st.title("Recovery of Arrear Tax")
st.markdown("#### Section 95 | VAT & SD Act, 2012")
st.divider()

# --- 1. THE RECOVERY PROCESS ---
st.subheader("How Arrears are Recovered")
st.markdown("""
If a registered person fails to pay tax, interest, or penalties within the 
prescribed time, the following recovery methods are deployed:
""")

# --- 2. RECOVERY METHODS ---
st.markdown("""
<div class="recovery-card">
    <span class="step-number">01.</span> <b>Adjustment from Refunds:</b> Any pending VAT refund under Section 48 is automatically adjusted against the liability.
</div>
<div class="recovery-card">
    <span class="step-number">02.</span> <b>Bank Garnishment:</b> Direct orders to banks to freeze and transfer funds from company accounts to the Treasury.
</div>
<div class="recovery-card">
    <span class="step-number">03.</span> <b>Import/Export Blockade:</b> Customs authorities are notified to stop the clearance of all shipments belonging to the BIN holder.
</div>
<div class="recovery-card">
    <span class="step-number">04.</span> <b>Third-Party Debt Recovery:</b> Any person who owes money to the taxpayer can be legally compelled to pay the NBR directly.
</div>
<div class="recovery-card">
    <span class="step-number">05.</span> <b>Distress and Sale:</b> Seizure of movable property (inventory/vehicles) and immovable property (land/buildings) for public auction.
</div>
""", unsafe_allow_html=True)

# --- 3. LEGAL STATUS ---
st.subheader("⚖️ Legal Finality")
st.info("""
Recovery actions are typically initiated once an assessment order becomes 
**'Final and Conclusive'**. This happens if the taxpayer does not file an 
appeal within the statutory time limit or if the Appellate Authority rules 
against the taxpayer.
""")

# --- 4. PREVENTATIVE MEASURES ---
with st.expander("How to stay recovery?"):
    st.write("""
    * **Payment of 10-20%:** Filing an appeal with the Commissioner (Appeals) or the Appellate Tribunal usually requires a mandatory deposit of the disputed amount, which may temporarily stay recovery of the balance.
    * **Stay Order:** Obtaining a specific stay order from the High Court Division or the Appellate Authority.
    """)

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For a large manufacturing entity, the biggest risk 
during an arrear dispute is **Bank Garnishment** and **Customs Blockade**. 
These can halt production instantly. Always ensure that 'Demand Notices' 
are handled by the legal/tax team immediately—missing a deadline to respond 
can lead to an 'Ex-Parte' recovery order, which is difficult to reverse.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Arrear Recovery Module © 2026</center>", unsafe_allow_html=True)