import streamlit as st
import sys, os

# 1. ABSOLUTELY FIRST: Handle page config safely for multipage app environments
try:
    st.set_page_config(page_title="Module 8 – Accounts, Audit & Reporting | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This prevents the error if the config was already set by the main script
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply custom styles and sidebar
apply_base_styles()
sidebar_nav()

# ── Hero Section ──────────────────────────────────────────────────────
hero("8", "Accounts, Audit & Financial Reporting",
     "The most critical module for finance and accounts professionals — covering statutory obligations for maintaining accounts, financial reporting, appointment of auditors, and audit requirements under the Act.",
     "📊")

metric_row([
    ("Section 181", "Books of Account"),
    ("Section 183", "P&L / Balance Sheet"),
    ("Section 210", "Auditor Appointment"),
    ("8 Years", "Record Retention"),
])
st.markdown("<br>", unsafe_allow_html=True)

tip_box("Why This Module is Critical",
        "Finance and accounts professionals are directly responsible for compliance with these provisions. Failure to maintain proper accounts or facilitate audits exposes both the company and its officers to serious legal liability.")

# ── Books of Account ──────────────────────────────────────────────────
section_heading("Obligation to Maintain Books of Account — Section 181")

law_box("Section 181(1) — Every company shall keep at its registered office proper books of account with respect to: sums received/expended, sales/purchases, and assets/liabilities.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📚 What Books Must Be Kept</div>
        <div class="info-card-body">
        ✔ <strong>Cash Book</strong> & Sales/Purchase Records<br>
        ✔ <strong>General Ledger</strong> & Stock Records<br>
        ✔ <strong>Fixed Asset Register</strong><br>
        ✔ Debtors/Creditors Ledgers
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📍 Location & Retention</div>
        <div class="info-card-body">
        <strong>Location:</strong> Registered office.<br><br>
        <strong>Retention Period:</strong> Minimum <strong>8 years</strong>.<br><br>
        <strong>Inspection:</strong> Directors have right to inspect at any time.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Audit Section ─────────────────────────────────────────────────────
section_heading("Statutory Audit Requirements")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">✅ Auditor Qualification — Sec 212</div>
        <div class="info-card-body">
        An auditor must be a <strong>Chartered Accountant</strong> (ICAB Member).<br><br>
        <strong>Disqualifications:</strong><br>
        ❌ Company employee/officer<br>
        ❌ Indebted to company > Tk. 1,000<br>
        ❌ Body Corporate
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📅 Appointment — Section 210</div>
        <div class="info-card-body">
        <strong>First Auditor:</strong> Appointed by Board within 1 month of incorporation.<br><br>
        <strong>Subsequent:</strong> Appointed by members at each AGM.<br><br>
        <strong>Remuneration:</strong> Fixed by the appointing authority (Members or Board).
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Dividend Rules ────────────────────────────────────────────────────
section_heading("Dividend — Key Rules")

law_box("General Rule: Dividends can ONLY be paid out of PROFITS — not out of capital.")

dividend_rules = [
    ("📢", "Declaration", "Declared by members at AGM. Directors can declare INTERIM dividends."),
    ("⏰", "Payment", "Must be paid within 42 days of declaration."),
    ("📊", "Source", "From current year or accumulated profits. Never from capital."),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(dividend_rules):
    with cols[i]:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">{icon} {title}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Quiz ──────────────────────────────────────────────────────────────
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Who appoints the FIRST auditor of a company?",
              ["Members at AGM", "Board of Directors within 1 month", "RJSC"], index=None)
if q1 == "Board of Directors within 1 month":
    success_box("Correct! Section 210 gives this power to the Board initially.")

q2 = st.radio("2. Books of account must be retained for a minimum of how many years?",
              ["5 years", "8 years", "12 years"], index=None)
if q2 == "8 years":
    success_box("Correct! Section 181 requires 8 years of record retention.")

recap_box([
    "Proper books must be kept at the registered office for 8 years.",
    "First auditor is appointed by the Board; subsequent auditors by members.",
    "Only ICAB Chartered Accountants can be statutory auditors.",
    "Dividends can only be paid from profits; never from capital.",
    "Auditors have a right of access to all books and vouchers at all times."
])