import streamlit as st
import pandas as pd

# --- DO NOT CALL set_page_config HERE (Handled by Homepage) ---

# --- STANDARD WEBPAGE STYLING ---
st.markdown("""
    <style>
    html, body, [class*="st-"] {
        font-size: 16px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1 { font-size: 2.1rem !important; color: #991b1b !important; }
    h2 { font-size: 1.6rem !important; color: #b91c1c !important; margin-top: 1.5rem !important; }
    h3 { font-size: 1.25rem !important; color: #b91c1c !important; }
    p, li { font-size: 1rem !important; line-height: 1.6; color: #374151; }
    
    .penalty-card {
        background-color: #fef2f2;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #dc2626;
        margin-bottom: 12px;
    }
    .warning-label {
        font-weight: bold;
        color: #991b1b;
        text-transform: uppercase;
        font-size: 0.85rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Risk Management")
st.sidebar.error("Compliance is non-negotiable. Interest at 2% per month is mandatory.")

# --- HEADER ---
st.title("Consequences of Non-Compliance")
st.markdown("#### Sections 111-127 | VAT & SD Act, 2012")
st.divider()

# --- 1. MONETARY PENALTIES ---
st.subheader("⚖️ Common Monetary Penalties")
st.markdown("Under Section 121, the following fixed penalties apply for procedural lapses:")

penalty_data = {
    "Nature of Irregularity": [
        "Failure to apply for Registration/Enlistment",
        "Failure to submit VAT Return (Mushak-9.1) on time",
        "Failure to display Registration Certificate",
        "Failure to notify changes in business info",
        "Failure to issue Tax Invoice (Mushak-6.3)",
        "Failure to maintain mandatory Books/Registers"
    ],
    "Penalty Amount": [
        "Tk. 10,000",
        "Tk. 10,000",
        "Tk. 10,000",
        "Tk. 10,000",
        "Tk. 50,000 or 100% of Tax",
        "Tk. 50,000"
    ]
}
st.table(pd.DataFrame(penalty_data))

# --- 2. INTEREST & BIN SUSPENSION ---
st.subheader("⚡ Operational Impacts")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="penalty-card">
        <span class="warning-label">Mandatory Interest</span>
        <p><b>2% Simple Interest</b> is charged per month on any unpaid tax. This is calculated daily and cannot be waived by any VAT authority.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="penalty-card">
        <span class="warning-label">BIN Suspension</span>
        <p>Non-filing for <b>2 consecutive months</b> triggers an automatic system lock. This halts all Import/Export clearances and Port activities.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. OFFENCES & PROSECUTION ---
st.subheader("🏢 Criminal Offences & Prosecution")

with st.expander("Tax Evasion & Forgery (Section 111)"):
    st.write("""
    Knowingly making false statements, forging Mushak-6.3 invoices, or using 
    fake BINs to evade tax is a criminal offence.
    * **Punishment:** Imprisonment for up to 1 year, OR a fine equal to the tax amount, OR both.
    """)

with st.expander("Obstruction of Duty (Section 113)"):
    st.write("""
    Preventing or obstructing a VAT officer from entering the factory or 
    inspecting records is punishable by a fine of up to Tk. 50,000 or 6 months imprisonment.
    """)

# --- 4. AUDIT & RECOVERY ---
st.subheader("🔍 Recovery Powers")
st.markdown("""
If tax remains unpaid, the Commissioner has the power to:
1. **Garnish Bank Accounts:** Direct banks to freeze and transfer funds to the Treasury.
2. **Seal Business Premises:** Physically lock the factory or warehouse.
3. **Stop Sale:** Order the cessation of all sales until dues are cleared.
""")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** In a multinational environment, 'Reputational Risk' 
outweighs the monetary penalty. A BIN suspension for even 24 hours can 
disrupt the entire supply chain. Ensure your **Tax Calendar** is automated with 
reminders 5 days before the **15th of the month** to ensure 100% on-time filing.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | VAT Compliance Risk Module © 2026</center>", unsafe_allow_html=True)