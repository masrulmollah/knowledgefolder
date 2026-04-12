import streamlit as st
import sys, os

# 1. ABSOLUTELY FIRST: Handle page config safely
try:
    st.set_page_config(page_title="Module 7 – Meetings & Resolutions | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # If already set by the main/homepage script, we ignore the error and proceed
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply custom styles and sidebar
apply_base_styles()
sidebar_nav()

# ── Hero Section ──────────────────────────────────────────────────────
hero("7", "Meetings & Resolutions",
     "Understand the types of company meetings, notice requirements, quorum rules, voting procedures, and the different categories of resolutions under the Act.",
     "🗳️")

metric_row([
    ("21 days", "AGM Notice Period"),
    ("6 months", "AGM Deadline"),
    ("14 days", "EGM Notice Period"),
    ("3/4 Majority", "Special Resolution"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Types of Meetings ─────────────────────────────────────────────────
section_heading("Types of Company Meetings")

meetings = [
    ("🏛️", "Statutory Meeting", "Public companies only. Held once between 1-6 months from commencement. Statutory Report must be sent 21 days before.", "Section 83"),
    ("📅", "Annual General Meeting (AGM)", "Held each calendar year. Subsequent AGMs within 6 months of financial year end.", "Section 85"),
    ("⚡", "Extraordinary General Meeting (EGM)", "Any general meeting other than AGM. Called by directors or requisitioned by 1/10th of shareholders.", "Section 86"),
    ("🏢", "Board Meeting", "Meeting of Directors. Held at least once every 3 months; minimum 4 times a year.", "Section 95"),
]

for icon, name, desc, sec in meetings:
    with st.expander(f"{icon} {name}  〈{sec}〉"):
        st.markdown(f'<div class="law-section-box">{desc}</div>', unsafe_allow_html=True)

gold_divider()

# ── AGM in Detail ─────────────────────────────────────────────────────
section_heading("Annual General Meeting (AGM) — Key Rules")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📋 Notice Requirements</div>
        <div class="info-card-body">
        ✔ Minimum <strong>21 days' written notice</strong> to all members<br>
        ✔ Short notice valid if <strong>95% of members</strong> consent<br>
        ✔ Notice must be sent to all directors, auditors, and members
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">👥 Quorum Requirements</div>
        <div class="info-card-body">
        <strong>Private Company:</strong> 2 members present<br>
        <strong>Public Company:</strong> 5 members present<br><br>
        If no quorum in 30 mins: Adjourned to same day/time next week.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Types of Resolutions ──────────────────────────────────────────────
section_heading("Types of Resolutions")

res_types = [
    ("📗", "Ordinary Resolution",
     "Simple majority (>50%) of votes cast. Used for: Appointment of directors, adoption of accounts, dividends."),
    ("📘", "Special Resolution",
     "At least 75% (3/4) of votes cast. Used for: Altering MoA/AoA, name change, capital reduction."),
]

for icon, name, desc in res_types:
    st.markdown(f"""
    <div class="info-card" style="margin-bottom:12px;">
        <div class="info-card-title">{icon} {name}</div>
        <div class="info-card-body">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Voting & Proxies ──────────────────────────────────────────────────
section_heading("Voting & Proxies")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🗳️ Methods of Voting</div>
        <div class="info-card-body">
        <strong>1. Show of Hands:</strong> One member = One vote.<br><br>
        <strong>2. Poll:</strong> Each share carries proportionate votes. Demanded by Chairman or 5 members (or 1/10th voting rights).
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📝 Proxies</div>
        <div class="info-card-body">
        A person authorised to vote on behalf of a member.<br><br>
        ✔ Appointed in writing.<br>
        ✔ Form deposited ≥48 hours before meeting.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Quiz ──────────────────────────────────────────────────────────────
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. What is the minimum notice period for an Annual General Meeting?",
              ["7 days", "14 days", "21 days", "28 days"], index=None)
if q1 == "21 days":
    st.success("Correct!")

q2 = st.radio("2. A Special Resolution requires what majority of votes cast?",
              ["Simple majority", "Three-fourths majority (75%)"], index=None)
if q2 == "Three-fourths majority (75%)":
    st.success("Correct!")

# ── Recap ──────────────────────────────────────────────────────────────
recap_box([
    "AGM requires 21 days' written notice.",
    "Special Resolutions require a 75% majority.",
    "Quorum for Public Companies is 5 members; Private is 2.",
    "Minutes must be recorded within 30 days and signed by the Chairman.",
    "Shareholders holding 10% voting power can requisition an EGM."
])