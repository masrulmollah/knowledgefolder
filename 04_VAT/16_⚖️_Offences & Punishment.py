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
    h1 { font-size: 2.1rem !important; color: #7f1d1d !important; }
    h2 { font-size: 1.6rem !important; color: #991b1b !important; margin-top: 1.5rem !important; }
    h3 { font-size: 1.25rem !important; color: #b91c1c !important; }
    p, li { font-size: 1rem !important; line-height: 1.6; color: #374151; }
    
    .legal-card {
        background-color: #fef2f2;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #991b1b;
        margin-bottom: 12px;
    }
    .penalty-text {
        font-weight: bold;
        color: #dc2626;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Legal Protocol")
st.sidebar.error("Chapter 16: Criminal liability applies to Directors & Managers.")

# --- HEADER ---
st.title("Offence, Trial & Punishment")
st.markdown("#### Sections 111-120 | VAT & SD Act, 2012")
st.divider()

# --- 1. CLASSIFICATION OF OFFENCES ---
st.subheader("⚠️ Major Criminal Offences")

offence_data = {
    "Section": ["Section 111", "Section 112", "Section 113"],
    "Nature of Offence": [
        "Tax Evasion (Fake Invoices, Fake BIN, Forged Stamps, Wrongful Refunds)",
        "False or Misleading Statements in VAT documents",
        "Obstruction of a VAT Officer's Duty"
    ],
    "Maximum Punishment": [
        "1 Year Jail + Fine (equal to tax)",
        "6 Months Jail + Fine",
        "6 Months Jail + Fine (up to 2 Lac)"
    ]
}
st.table(pd.DataFrame(offence_data))

# --- 2. TRIAL PROCEDURES ---
st.subheader("⚖️ Trial & Jurisdiction")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="legal-card">
        <b>Court Authority</b><br>
        Trials are conducted by a <b>First Class Judicial Magistrate</b> or <b>Metropolitan Magistrate</b>. They have the power to impose any fine amount prescribed.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="legal-card">
        <b>Bail & Arrest</b><br>
        VAT offences are <b>Bailable</b> and <b>Non-Cognizable</b>. A written complaint from an Assistant Commissioner (min rank) is required.
    </div>
    """, unsafe_allow_html=True)

# --- 3. SPECIAL PROVISIONS ---
st.subheader("🔍 Corporate & Management Liability")
st.warning("""
**Section 120:** If a company commits an offence, every **Director, Manager, or Secretary** is deemed guilty unless they can prove the offence was committed without their knowledge or that they exercised due diligence to prevent it.
""")

with st.expander("Compounding of Offences (Section 119)"):
    st.write("""
    The Commissioner can "Compound" an offence. This means the NBR may allow the 
    taxpayer to settle the matter by paying the due tax and a compounding fee 
    to avoid a long criminal trial. Once compounded, no further criminal 
    proceedings can be initiated for that specific offence.
    """)

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** In corporate finance, the 'Section 120' liability is 
a significant risk. Ensure that all **Mushak-6.3** invoices and **Mushak-9.1** returns are signed only after a thorough internal audit. Even if a junior 
clerk commits a forgery, the **Factory Finance Lead** or **Directors** can be 
held legally accountable under the 'vicarious liability' principles of this Act.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Legal & Punishment Module © 2026</center>", unsafe_allow_html=True)