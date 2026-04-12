import streamlit as st
import sys, os

# --- Page Config ---
try:
    st.set_page_config(page_title="Overview | Company Act BD", layout="wide", page_icon="🏛️")
except st.errors.StreamlitAPIException:
    pass

# --- Setup Paths and Imports ---
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

apply_base_styles()
sidebar_nav()

# Custom Hero for Overview
st.markdown(f"""
<div class="hero-banner">
    <div style="font-family:'Fira Mono',monospace; font-size:12px; color:#c8922a; letter-spacing:3px; text-transform:uppercase; margin-bottom:12px;">
        Interactive Learning Guide
    </div>
    <div class="hero-title">🏛️ The Companies Act, 1994</div>
    <div class="hero-subtitle">
        A complete statutory guide to Corporate Law in Bangladesh. Explore all 12 modules below to master 
        incorporation, management, compliance, and winding up procedures.
    </div>
</div>
""", unsafe_allow_html=True)

section_heading("Curriculum Roadmap")

# --- Grid of Modules ---
# We define the data for all 12 modules
module_data = [
    ("01", "Introduction", "History, evolution, and legal framework of company law in BD."),
    ("02", "Incorporation", "MOA, AOA, and the process of forming Private & Public companies."),
    ("03", "Share Capital", "Equity, preference shares, debentures, and capital alteration."),
    ("04", "Prospectus", "Public offerings, listing requirements, and liability for misstatements."),
    ("05", "Management", "Registered office, statutory registers, and administrative compliance."),
    ("06", "Directors", "Appointment, legal status, powers, duties, and qualifications."),
    ("07", "Meetings", "AGM, EGM, statutory meetings, notices, and voting resolutions."),
    ("08", "Audit & Accounts", "Financial reporting, books of account, and auditor appointment."),
    ("09", "Investigation", "Registrar's powers, government inspection, and court inquiries."),
    ("10", "Winding Up", "Compulsory, voluntary, and court-supervised liquidation processes."),
    ("11", "Foreign Co.", "Registration of foreign entities, branches, and liaison offices."),
    ("12", "Penalties", "Offences, default officer liability, and legal proceedings."),
]

# Display in 3 columns
cols = st.columns(3)
for i, (m_id, title, desc) in enumerate(module_data):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="info-card" style="min-height: 180px;">
            <div style="font-family:'Fira Mono',monospace; color:#c8922a; font-weight:700; font-size:0.8rem;">MODULE {m_id}</div>
            <div class="info-card-title">{title}</div>
            <div class="info-card-body" style="font-size:0.88rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# --- Practical Reference Section ---
col_left, col_right = st.columns(2)

with col_left:
    section_heading("Key Regulatory Bodies")
    st.markdown("""
    * **RJSC:** Registrar of Joint Stock Companies & Firms (Primary Regulator).
    * **BSEC:** Bangladesh Securities and Exchange Commission (For Listed Companies).
    * **FRC:** Financial Reporting Council (Audit oversight).
    * **High Court Division:** Jurisdiction over company matters.
    """)

with col_right:
    section_heading("Compliance Quick-Links")
    st.markdown("""
    * [Search RJSC Entity](https://www.roc.gov.bd)
    * [BSEC Rules & Regulations](https://www.sec.gov.bd)
    * [ICAB Auditing Standards](https://www.icab.org.bd)
    """)

recap_box([
    "The Act consists of 404 Sections and 12 Schedules.",
    "Most company filings are now handled through the RJSC online portal.",
    "Section 2 is the most vital for understanding legal definitions.",
    "The 'Officer in Default' principle makes directors personally liable for compliance gaps."
])