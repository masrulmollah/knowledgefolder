import streamlit as st
import sys, os

# 1. ABSOLUTELY FIRST: Handle page config safely for multipage apps
try:
    st.set_page_config(page_title="Module 11 – Foreign Companies | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This prevents the error if the config was already set by the main/homepage script
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply custom styles and sidebar
apply_base_styles()
sidebar_nav()

# ── Hero Section ──────────────────────────────────────────────────────
hero("11", "Foreign Companies",
     "Learn the requirements for foreign companies establishing operations in Bangladesh — registration, compliance, accounts, and closure procedures under Part X of the Act.",
     "🌍")

metric_row([
    ("Part X", "Act Coverage"),
    ("30 days", "Registration Deadline"),
    ("Section 378", "Key Section"),
    ("2 copies", "Financial Statements Filed"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Definition ────────────────────────────────────────────────────────
section_heading("What is a Foreign Company?")
tip_box("Definition",
        "A Foreign Company is any company incorporated outside Bangladesh that has established (or intends to establish) a place of business in Bangladesh. This includes branch, liaison, and representative offices.")

law_box("Section 378 — Every foreign company which establishes a place of business within Bangladesh shall, within 30 days of such establishment, deliver to the Registrar the prescribed documents.")

gold_divider()

# ── Registration Requirements ─────────────────────────────────────────
section_heading("Registration Requirements — Section 378")

docs = [
    ("📜", "Certified copy of Charter/MoA/AoA or equivalent"),
    ("📋", "List of directors and secretary of the foreign company"),
    ("📍", "Address of registered office in the country of incorporation"),
    ("🏢", "Address of principal place of business in Bangladesh"),
    ("👤", "Authorized person resident in Bangladesh for service of notices"),
    ("📊", "Latest audited financial statements of the foreign company"),
]

for icon, doc in docs:
    st.markdown(f'<div class="success-box" style="margin-bottom:6px; padding:10px 16px;">{icon} {doc}</div>', unsafe_allow_html=True)

gold_divider()

# ── Ongoing Compliance ────────────────────────────────────────────────
section_heading("Ongoing Compliance Obligations")

compliance = [
    ("📅", "Annual Filing", "File copies of annual balance sheet and accounts with RJSC."),
    ("🏢", "Office Display", "Company name and country must be displayed outside every place of business."),
    ("📝", "Document Disclosure", "Letterheads must state name, country of incorporation, and liability status."),
    ("🔄", "Change Notification", "Notify RJSC of changes in directors or charter within 30 days."),
]

cols = st.columns(2)
for i, (icon, title, desc) in enumerate(compliance):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card" style="margin-bottom:10px;">
            <div class="info-card-title">{icon} {title}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Closure ───────────────────────────────────────────────────────────
section_heading("Closure of Foreign Company in Bangladesh")

closure_steps = [
    "Board resolution in home country to close operations.",
    "Notice to all Bangladesh creditors and employees.",
    "File notice of closure and deregister with RJSC.",
    "Obtain No Objection from Bangladesh Bank for fund remittance.",
    "File final tax returns and obtain tax clearance.",
]

for i, step in enumerate(closure_steps, 1):
    st.markdown(f"""
    <div class="info-card" style="padding:10px 18px; margin-bottom:6px; display:flex; gap:14px; align-items:center;">
        <div style="background:#1a3a5c; color:#c8922a; font-family:'Fira Mono',monospace; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0;">{i}</div>
        <div class="info-card-body">{step}</div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Quiz ──────────────────────────────────────────────────────────────
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Within how many days of establishing a business must a foreign company register?",
              ["14 days", "21 days", "30 days"], index=None)
if q1 == "30 days":
    st.success("Correct! Section 378 requires registration within 30 days.")

# ── Recap ─────────────────────────────────────────────────────────────
recap_box([
    "Foreign companies must register with RJSC within 30 days of setup.",
    "Annual accounts must be filed with the Registrar.",
    "Local correspondence must state the country of incorporation.",
    "Closure requires tax clearance and Bangladesh Bank approval for remittance.",
    "Registration requires a designated local representative for notices."
])