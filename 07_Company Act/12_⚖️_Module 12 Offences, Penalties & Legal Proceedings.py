import streamlit as st
import sys, os

# --- ABSOLUTELY FIRST STREAMLIT COMMAND ---
# Wrap in try-except to prevent crash in multipage app environments
try:
    st.set_page_config(page_title="Module 12 – Offences & Penalties | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # Page config already set by the main entry point (Homepage.py)
    pass

# --- Setup Paths and Imports ---
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

apply_base_styles()
sidebar_nav()

hero("12", "Offences, Penalties & Legal Proceedings",
     "A comprehensive reference of offences, penalties, and legal proceedings under the Companies Act, 1994 — critical for compliance risk management.",
     "⚖️")

metric_row([
    ("Part XI", "Act Coverage"),
    ("Section 396", "Cognisance"),
    ("2 Years", "Max Imprisonment"),
    ("Section 404", "Final Section"),
])
st.markdown("<br>", unsafe_allow_html=True)

tip_box("Practical Importance",
        "Understanding the offences and penalties under the Act is essential for risk management. Directors and officers can face both corporate fines AND personal imprisonment for many violations.")

# --- Offences Table ---
section_heading("Key Offences & Penalties Reference Table")

offences = [
    ("Misstatement in Prospectus (wilful)", "Director, Promoter, authorized person", "Imprisonment up to 2 years and/or fine"),
    ("Failure to keep proper Books of Account", "Every officer in default", "Imprisonment up to 6 months and/or fine"),
    ("Failure to hold AGM", "Every officer in default", "Fine up to Tk. 5,000 + Tk. 250/day continuing"),
    ("Failure to file Annual Return", "Company and every officer", "Fine Tk. 500/day for every day of default"),
    ("False Declaration of Solvency", "Directors making declaration", "Imprisonment up to 6 months and/or fine"),
    ("Fraudulent Trading", "Responsible officers", "Personal liability for all debts + prosecution"),
]

st.markdown("""
<table>
<tr><th>Offence</th><th>Person Liable</th><th>Penalty</th></tr>
""" + "".join(f"<tr><td>{o}</td><td>{p}</td><td style='color:#b33a3a;'><strong>{pen}</strong></td></tr>" for o, p, pen in offences) + """
</table>
""", unsafe_allow_html=True)

gold_divider()

# --- Officer in Default ---
section_heading("'Officer in Default' — Who is Liable?")

law_box("Under the Act, 'officer in default' means any officer of the company who knowingly and wilfully authorized or permitted the default, contravention, or failure.")

st.markdown("""
<div class="info-card">
    <div class="info-card-title">👤 Who Can Be an 'Officer in Default'?</div>
    <div class="info-card-body">
    ✔ <strong>Managing Director</strong> — for general oversight.<br>
    ✔ <strong>Directors</strong> — who knowingly permitted the default.<br>
    ✔ <strong>Company Secretary</strong> — for filing/procedural defaults.<br>
    ✔ <strong>Manager</strong> — for defaults in their specific area.<br>
    </div>
</div>
""", unsafe_allow_html=True)

gold_divider()

# --- Cognisance & Compounding ---
section_heading("Cognisance & Settlement")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">⚖️ Cognisance (Section 396)</div>
        <div class="info-card-body">
        Courts <strong>cannot</strong> take cognisance of an offence unless a complaint is made by (or sanctioned by) the <strong>Registrar or the Government</strong>.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🤝 Compounding</div>
        <div class="info-card-body">
        Technical or procedural defaults can often be 'compounded' (settled) by paying a fine to the Registrar/Government without a full criminal trial.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# --- Case Law ---
section_heading("Key Case Law Notes")

cases = [
    ("Solomon v Solomon & Co. [1897]", "The foundation of 'Separate Legal Entity'—the company is a distinct person from its owners."),
    ("Foss v Harbottle [1843]", "The 'Majority Rule'—wrong done to a company should be remedied by the company itself."),
    ("Saloman Doctrine in BD", "Bangladesh courts strictly follow the separate entity principle; the 'veil' is pierced only in cases of clear fraud."),
]

for case, desc in cases:
    with st.expander(f"📚 {case}"):
        st.markdown(f'<div class="law-section-box">{desc}</div>', unsafe_allow_html=True)

gold_divider()

# --- Quiz ---
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Who must sanction a criminal complaint under the Companies Act?",
              ["Any shareholder", "The Registrar or Government", "The Board of Directors"], index=None)
if q1 == "The Registrar or Government":
    success_box("Correct! Section 396 requires sanction from the Registrar or Gov.")

q2 = st.radio("2. What is the foundation principle of the Solomon v Solomon case?",
              ["Ultra Vires", "Separate Legal Entity", "Constructive Notice"], index=None)
if q2 == "Separate Legal Entity":
    success_box("Correct! It established that a company is a separate legal person.")

recap_box([
    "Officers 'in default' are personally liable for penalties.",
    "Section 396 requires Registrar/Gov sanction for criminal prosecutions.",
    "The maximum imprisonment under the Act is generally 2 years (e.g., Prospectus fraud).",
    "Separate legal entity remains the core principle of Bangladesh Company Law.",
    "Compounding is a practical way to resolve procedural defaults without trial."
])