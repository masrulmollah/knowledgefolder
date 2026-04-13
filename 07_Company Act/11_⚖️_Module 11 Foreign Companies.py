import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

st.set_page_config(page_title="Module 11 – Foreign Companies | Company Act BD", layout="wide", page_icon="📘")
apply_base_styles()
sidebar_nav()

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

section_heading("What is a Foreign Company?")
tip_box("Definition",
        "A Foreign Company is any company incorporated outside Bangladesh that has established (or intends to establish) a place of business in Bangladesh. This includes branch offices, liaison offices, representative offices, and project offices.")

law_box("Section 378 — Every foreign company which establishes a place of business within Bangladesh shall, within 30 days of such establishment, deliver to the Registrar the prescribed documents.")

gold_divider()
section_heading("Registration Requirements — Section 378")

docs = [
    ("📜", "Certified copy of Charter/MoA/AoA or equivalent constitutional document"),
    ("📋", "List of directors and secretary of the foreign company"),
    ("📍", "Address of registered/principal office in the country of incorporation"),
    ("🏢", "Address of principal place of business in Bangladesh"),
    ("👤", "Names and addresses of persons resident in Bangladesh authorised to accept notices on behalf of the company"),
    ("📊", "Latest audited financial statements of the foreign company"),
]

for icon, doc in docs:
    st.markdown(f'<div class="success-box" style="margin-bottom:6px; padding:10px 16px;">{icon} {doc}</div>', unsafe_allow_html=True)

gold_divider()
section_heading("Ongoing Compliance Obligations")

compliance = [
    ("📅", "Annual Filing", "Must file copies of annual balance sheet and accounts with RJSC within the same period as required in its home country (or as prescribed by the Registrar)"),
    ("🏢", "Office Display", "Must display the company name and country of incorporation prominently outside every place of business in Bangladesh"),
    ("📝", "Document Disclosure", "All business correspondence, letterheads, and official documents in Bangladesh must state the company name, country of incorporation, and liability status"),
    ("🔄", "Change Notification", "Any change in charter/MoA/AoA, directors, secretary, or registered agent must be notified to RJSC within 30 days"),
    ("📊", "Audit Compliance", "Accounts maintained in Bangladesh must be audited by a qualified auditor acceptable to the Registrar"),
    ("⚠️", "Tax Compliance", "Foreign companies with permanent establishment in Bangladesh are subject to Bangladesh income tax on Bangladesh-sourced income"),
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
section_heading("Restrictions on Share Offers")

warning_box("Section 388 — Foreign companies are prohibited from offering or advertising shares or debentures for sale or subscription in Bangladesh unless the company is incorporated in Bangladesh or has complied with the conditions prescribed by the Government.")

gold_divider()
section_heading("Closure of Foreign Company in Bangladesh")

closure_steps = [
    "Board resolution in home country to close Bangladesh operations",
    "Give adequate notice to all Bangladesh creditors and employees",
    "Settle all outstanding liabilities in Bangladesh",
    "File notice of closure with RJSC",
    "Deregister with RJSC",
    "Obtain No Objection from Bangladesh Bank (for remittance of funds)",
    "File final tax returns and obtain tax clearance",
    "Return all relevant Bangladesh-authority registrations and licences",
]
for i, step in enumerate(closure_steps, 1):
    st.markdown(f"""
    <div class="info-card" style="padding:10px 18px; margin-bottom:6px; display:flex; gap:14px; align-items:center;">
        <div style="background:#1a3a5c; color:#c8922a; font-family:'Fira Mono',monospace; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0;">{i}</div>
        <div class="info-card-body">{step}</div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Within how many days of establishing a place of business in Bangladesh must a foreign company register with RJSC?",
              ["7 days", "14 days", "21 days", "30 days"], index=None)
if q1 == "30 days":
    success_box("Correct! Under Section 378, a foreign company must register with the Registrar within 30 days of establishing a place of business in Bangladesh.")
elif q1:
    warning_box("Incorrect. The deadline is 30 days from establishing a place of business in Bangladesh.")

recap_box([
    "Foreign company = incorporated outside Bangladesh but has a place of business in Bangladesh",
    "Must register with RJSC within 30 days of establishment",
    "Must file annual accounts, list of directors, and notify changes within 30 days",
    "Cannot offer shares to the public in Bangladesh without special Government approval",
    "All Bangladesh correspondence must clearly state country of incorporation",
    "Closure requires notification to RJSC, settlement of all liabilities, and tax clearance",
])

# ══════════════════════════════════════════════════════════════════════
# MODULE 12
# ══════════════════════════════════════════════════════════════════════