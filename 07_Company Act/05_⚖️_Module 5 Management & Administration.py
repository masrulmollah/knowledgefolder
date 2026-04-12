import streamlit as st
import sys, os

# 1. ABSOLUTELY FIRST: Handle page config safely for multipage apps
try:
    st.set_page_config(page_title="Module 5 – Management & Administration | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # If already set by the main script, ignore and move on
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply custom styles and sidebar
apply_base_styles()
sidebar_nav()

hero("5", "Management & Administration",
     "Learn the operational and administrative requirements every company must comply with — registered office, statutory registers, annual returns, and document management.",
     "🏢")

metric_row([
    ("Part IV", "Act Coverage"),
    ("28 days", "Change of Office Notice"),
    ("18 months", "First Annual Return"),
    ("21 days", "Notice for AGM"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Registered Office ─────────────────────────────────────────────────
section_heading("Registered Office Requirements")

law_box("Section 77 — A company shall at all times have a registered office within Bangladesh to which all communications and notices may be addressed.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🏠 Requirements</div>
        <div class="info-card-body">
        ✔ Established within <strong>28 days</strong> of incorporation<br>
        ✔ Address must be registered with RJSC (Form VI)<br>
        ✔ Changes must be notified to RJSC within <strong>28 days</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📋 Documents Kept at Office</div>
        <div class="info-card-body">
        • Register of Members & Directors<br>
        • Register of Charges<br>
        • Minutes of Meetings<br>
        • Books of Account & Annual Returns
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Company Name ──────────────────────────────────────────────────────
section_heading("Company Name Rules")

name_rules = [
    ("✅", "Must end with", "'Limited' (Pvt) or 'PLC' (Public)"),
    ("🚫", "Prohibited words", "'Bank', 'Insurance', 'Royal' require special permission"),
    ("📋", "Display requirement", "Must be displayed outside every place of business"),
    ("🔄", "Change of name", "Special Resolution + RJSC approval needed"),
]

for icon, label, rule in name_rules:
    st.markdown(f"""
    <div class="info-card" style="padding:12px 18px; margin-bottom:8px; display:flex; gap:12px;">
        <span style="font-size:1.2rem;">{icon}</span>
        <div>
            <strong style="color:#1a3a5c;">{label}:</strong>
            <span class="info-card-body"> {rule}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Statutory Registers ───────────────────────────────────────────────
section_heading("Statutory Registers to be Maintained")

registers = [
    ("📋", "Register of Members", "Shareholding details; update within 2 months of change.", "Section 36"),
    ("👥", "Register of Directors", "Names, nationalities, other directorships.", "Section 109"),
    ("⚡", "Register of Charges", "Details of mortgages created on assets.", "Section 107"),
    ("📊", "Minutes Books", "Records of GM and Board meetings; keep permanently.", "Section 92"),
]

cols = st.columns(2)
for i, (icon, name, desc, sec) in enumerate(registers):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card" style="margin-bottom:10px;">
            <div class="info-card-title">{icon} {name} <span class="section-pill">{sec}</span></div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Annual Return ─────────────────────────────────────────────────────
section_heading("Annual Return — Section 190")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📅 Filing Timeline</div>
        <div class="info-card-body">
        <strong>First Return:</strong> Within 18 months of incorporation<br><br>
        <strong>Subsequent:</strong> Within 21 days after each AGM<br><br>
        <strong>Penalty:</strong> Tk. 500 per day for default.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📋 Contents</div>
        <div class="info-card-body">
        ✔ Summary of share capital<br>
        ✔ List of current members & transfers<br>
        ✔ Particulars of directors & charges<br>
        ✔ Copy of audited financials
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Books of Account ──────────────────────────────────────────────────
section_heading("Books of Account — Section 181")

st.markdown("""
<table>
<tr><th>Book/Record</th><th>Retention Period</th></tr>
<tr><td>Cash, Sales, and Purchase Books</td><td>Min. 8 years</td></tr>
<tr><td>Fixed Asset Register</td><td>Life of asset + 8 years</td></tr>
<tr><td>Minutes Books</td><td>Permanently</td></tr>
<tr><td>Statutory Registers</td><td>Permanently (while active)</td></tr>
</table>
""", unsafe_allow_html=True)

gold_divider()

# ── Compliance Calendar ────────────────────────────────────────────────
section_heading("🗓️ Annual Compliance Calendar")

calendar = [
    ("📅 Within 28 days of incorporation", "Establish registered office"),
    ("📅 Within 18 months of incorporation", "File first Annual Return"),
    ("📅 Within 21 days of each AGM", "File Annual Return"),
    ("📅 Within 28 days of change", "Notify RJSC of change in directors/office"),
]

for deadline, action in calendar:
    st.markdown(f"""
    <div class="info-card" style="padding:12px 18px; margin-bottom:8px; display:flex; gap:16px;">
        <div style="min-width:250px; color:#c8922a; font-weight:600;">{deadline}</div>
        <div class="info-card-body">{action}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Quiz ──────────────────────────────────────────────────────────────
gold_divider()
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Within how many days must a change in registered office be notified?",
              ["14 days", "21 days", "28 days"], index=None)
if q1 == "28 days":
    success_box("Correct!")

q2 = st.radio("2. The Annual Return must be filed within how many days after the AGM?",
              ["14 days", "21 days", "42 days"], index=None)
if q2 == "21 days":
    success_box("Correct!")

recap_box([
    "Registered office must be established and address notified within 28 days.",
    "Annual Return is due within 21 days of the AGM.",
    "First Annual Return is due within 18 months of incorporation.",
    "Books of account must be retained for at least 8 years.",
    "Company name must be displayed outside all places of business."
])