import streamlit as st
import sys, os

# 1. MUST BE THE ABSOLUTE FIRST STREAMLIT COMMAND
# Wrapped in try-except to handle multipage app inheritance
try:
    st.set_page_config(page_title="Module 6 – Directors & Officers | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This catches the error if the config was already set by Homepage.py
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply styles and sidebar
apply_base_styles()
sidebar_nav()

hero("6", "Directors & Company Officers",
     "Master the appointment, duties, powers, liabilities, and restrictions on directors and key officers — a critical area for governance and compliance professionals.",
     "👔")

metric_row([
    ("2", "Min. Directors (Pvt.)"),
    ("3", "Min. Directors (Public)"),
    ("5 years", "Max Director Tenure"),
    ("Section 95", "Key Director Section"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Who is a Director ─────────────────────────────────────────────────
section_heading("Who is a Director?")

law_box("Section 2(f) — 'Director includes any person occupying the position of director by whatever name called.' The title does not matter — substance determines whether someone is a director.")

tip_box("Shadow Directors",
        "A person who is not formally appointed as a director but whose instructions the Board habitually follows may be treated as a 'shadow director' and can be held liable as if they were a director.")

gold_divider()

# ── Appointment ───────────────────────────────────────────────────────
section_heading("Appointment of Directors")

appoint_methods = [
    ("📜", "Named in Articles/Prospectus", "First directors can be named in the AoA or prospectus. They hold office from incorporation."),
    ("🗳️", "Elected by Shareholders", "In a General Meeting by ordinary resolution — this is the normal method for subsequent directors."),
    ("🏛️", "Board Appointment", "Board may appoint directors to fill casual vacancies or as additional directors, subject to AoA."),
    ("⚖️", "Court Order", "Courts may appoint directors in specific circumstances (e.g., investigation proceedings)."),
]

cols = st.columns(2)
for i, (icon, method, desc) in enumerate(appoint_methods):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card" style="margin-bottom:10px;">
            <div class="info-card-title">{icon} {method}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Qualifications & Disqualifications ───────────────────────────────
section_heading("Qualifications & Disqualifications")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card" style="background:#f0f8ee;">
        <div class="info-card-title">✅ General Qualifications</div>
        <div class="info-card-body">
        • Must be a natural person (individual, not a company)<br>
        • Must hold 'qualification shares' if required by AoA<br>
        • Must be at least 18 years of age<br>
        • Must be of sound mind<br>
        • Must consent to act as director (Form IX)
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card" style="background:#fff5f5;">
        <div class="info-card-title">❌ Disqualifications (Section 99-102)</div>
        <div class="info-card-body">
        A person CANNOT be a director if they:<br>
        • Are an <strong>undischarged insolvent</strong><br>
        • Have been <strong>convicted of fraud</strong> within 5 years<br>
        • Have failed to pay calls on their shares<br>
        • Are a <strong>body corporate</strong> (only individuals)
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Duties of Directors ───────────────────────────────────────────────
section_heading("Duties & Responsibilities of Directors")

duties = [
    ("🎯", "Fiduciary Duty", "Directors must act in good faith and in the best interests of the company, not for personal gain."),
    ("🧠", "Duty of Care & Skill", "Must exercise reasonable care and diligence expected of a prudent person."),
    ("🚫", "Duty to Avoid Conflicts", "Must disclose interests in contracts (Section 103) and avoid personal interest conflicts."),
    ("📊", "Duty to Maintain Accounts", "Responsible for ensuring proper books of account are maintained (Section 181)."),
]

for icon, duty, desc in duties:
    with st.expander(f"{icon} {duty}"):
        st.markdown(f'<div class="law-section-box">{desc}</div>', unsafe_allow_html=True)

gold_divider()

# ── Managing Director ─────────────────────────────────────────────────
section_heading("Managing Director")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">👔 Role & Appointment</div>
        <div class="info-card-body">
        A Managing Director (MD) is entrusted with <strong>substantial powers of management</strong>.<br><br>
        <strong>Tenure:</strong> Max 5 years per appointment.<br>
        <strong>Control:</strong> Subject to Board superintendence.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🚫 MD Cannot (Without Board)</div>
        <div class="info-card-body">
        • Make calls on shares<br>
        • Issue debentures<br>
        • Sell or lease the substantial part of the undertaking
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Quiz ──────────────────────────────────────────────────────────────
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. What is the minimum number of directors required for a Public Limited Company?",
              ["2", "3", "5", "7"], index=None)
if q1 == "3":
    success_box("Correct! A Public Limited Company must have at least 3 directors.")
elif q1:
    warning_box("Incorrect. A Public Company requires 3; a Private Company requires 2.")

q2 = st.radio("2. A Managing Director's tenure per appointment cannot exceed:",
              ["3 years", "4 years", "5 years", "10 years"], index=None)
if q2 == "5 years":
    success_box("Correct! Maximum tenure per appointment is 5 years.")
elif q2:
    warning_box("Incorrect. It is 5 years.")

recap_box([
    "Minimum 2 directors for private; 3 for public company.",
    "Directors must be natural persons of sound mind.",
    "MD tenure is capped at 5 years per appointment.",
    "Directors have a fiduciary duty to act in the company's best interest.",
    "Loans to directors are strictly restricted under Section 103A."
])