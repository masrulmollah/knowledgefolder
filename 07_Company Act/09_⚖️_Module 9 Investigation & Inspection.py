import streamlit as st
import sys, os

# 1. MUST BE THE ABSOLUTE FIRST STREAMLIT COMMAND
# Wrapped in try-except to handle multipage app inheritance
try:
    st.set_page_config(page_title="Module 9 – Investigation & Inspection | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This catches the error if the config was already set by Homepage.py
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply styles and sidebar
apply_base_styles()
sidebar_nav()

# ── Hero Section ──────────────────────────────────────────────────────
hero("9", "Investigation & Inspection",
     "Understand the powers of the Government, Courts, and Registrar to investigate and inspect company affairs — and the rights and protections of minority shareholders.",
     "🔍")

metric_row([
    ("Part IV", "Act Coverage"),
    ("Section 196", "Registrar Powers"),
    ("Section 200", "Court Investigation"),
    ("Section 233", "Minority Protection"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Overview ──────────────────────────────────────────────────────────
section_heading("Overview — Why Investigation Exists")
tip_box("Purpose of Investigation Provisions",
        "The investigation and inspection provisions protect shareholders (especially minorities), creditors, and the public from fraud, mismanagement, and abuse of corporate power.")

gold_divider()

# ── Registrar Powers ──────────────────────────────────────────────────
section_heading("Inspection of Books by Registrar — Section 196")
law_box("Section 196 — The Registrar may, at any time, inspect the books and papers of any company. On inspection, the Registrar may take copies of any book, paper or document.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🔍 Registrar's Inspection Powers</div>
        <div class="info-card-body">
        ✔ Can inspect books and papers at any time<br>
        ✔ Can direct the company to produce books<br>
        ✔ Can call for any explanation from officers/employees<br>
        ✔ Can take copies of any documents
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">⚡ Seizure of Books — Section 199</div>
        <div class="info-card-body">
        Requires a Magistrate's Order. Authorized if:<br>
        ✔ Fraud is suspected<br>
        ✔ Risk of document destruction/falsification<br>
        <strong>Timeline:</strong> Must return books within 30 days.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Court Investigation ───────────────────────────────────────────────
section_heading("Investigation by Court-Appointed Inspectors — Section 200")

law_box("Section 200 — The Court may appoint inspectors to investigate the affairs of a company if: (a) not less than 200 members or members holding ≥1/10 of shares apply, or (b) the company by Special Resolution so resolves.")

investigation_grounds = [
    ("👥", "Member Application", "200+ members, OR holders of 1/10 voting power"),
    ("🗳️", "Special Resolution", "Company resolves via Special Resolution to be investigated"),
    ("🏛️", "Court's Own Motion", "Ordered when necessary in the public interest"),
    ("🏦", "Government Direction", "Government directs Registrar to petition for investigation"),
]

cols = st.columns(2)
for i, (icon, title, desc) in enumerate(investigation_grounds):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card" style="margin-bottom:10px;">
            <div class="info-card-title">{icon} {title}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Minority Protection ───────────────────────────────────────────────
section_heading("Protection of Minority Shareholders — Section 233")

law_box("Section 233 — Any member who complains that company affairs are being conducted in a manner oppressive to any member(s) may apply to the Court for relief.")

st.markdown("""
<div class="info-card">
    <div class="info-card-title">⚖️ Minority Shareholder Remedies</div>
    <div class="info-card-body">
    If the majority is found to be <strong>oppressive</strong>, the Court may:<br><br>
    ✔ Regulate the conduct of future affairs<br>
    ✔ Require the company to refrain from certain acts<br>
    ✔ Order the <strong>purchase of shares</strong> of minority members by the majority<br>
    ✔ Authorize legal proceedings in the company's name
    </div>
</div>
""", unsafe_allow_html=True)

gold_divider()

# ── Quiz ──────────────────────────────────────────────────────────────
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. How many members minimum can apply to Court for an investigation under Section 200?",
              ["100 members", "200 members", "500 members"], index=None)
if q1 == "200 members":
    success_box("Correct! Section 200 requires 200 members or 1/10th of shares.")

q2 = st.radio("2. Seized books must be returned by the Registrar within how many days?",
              ["14 days", "30 days", "60 days"], index=None)
if q2 == "30 days":
    success_box("Correct! The return deadline is 30 days under Section 199.")

# ── Recap ─────────────────────────────────────────────────────────────
recap_box([
    "Registrar can inspect books without notice at any time.",
    "Court investigation requires an application by 200 members or 1/10th of shareholders.",
    "Inspectors have the power to examine officers on oath.",
    "Section 233 provides protection against 'Oppression and Mismanagement'.",
    "Investigation reports are admissible as evidence in legal proceedings."
])