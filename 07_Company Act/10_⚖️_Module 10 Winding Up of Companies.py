import streamlit as st
import sys, os

# 1. ABSOLUTELY FIRST: Handle page config safely for multipage app inheritance
try:
    st.set_page_config(page_title="Module 10 – Winding Up | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This catches the error if the config was already set by 1_🤓_Homepage.py
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply styles and sidebar
apply_base_styles()
sidebar_nav()

# ── Hero Section ──────────────────────────────────────────────────────
hero("10", "Winding Up of Companies",
     "Understand how a company ceases to exist — the modes of winding up, role of liquidators, priority of creditors, and the final dissolution of a company under the Companies Act, 1994.",
     "🏚️")

metric_row([
    ("Part V", "Act Coverage"),
    ("3", "Modes of Winding Up"),
    ("Section 241", "Compulsory W/U"),
    ("Section 304", "Voluntary W/U"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Definition ────────────────────────────────────────────────────────
section_heading("What is Winding Up?")
tip_box("Definition",
        "Winding up is the legal process by which a company's life is brought to an end. Its assets are realized, debts paid, and surplus distributed, leading to formal dissolution.")

gold_divider()

# ── Modes of Winding Up ───────────────────────────────────────────────
section_heading("Modes of Winding Up")

modes = [
    ("⚖️", "Compulsory Winding Up (by Court)", "The Court orders winding up, usually due to insolvency or 'just and equitable' grounds.", "#fff5f5"),
    ("🤝", "Voluntary Winding Up", "Initiated by members (if solvent) or creditors (if insolvent).", "#f0f8ee"),
    ("🏛️", "Subject to Court Supervision", "A voluntary process where the Court retains oversight of the liquidator.", "#f0f4fd"),
]

for icon, name, desc, bg in modes:
    st.markdown(f"""
    <div class="info-card" style="background:{bg}; margin-bottom:12px;">
        <div class="info-card-title">{icon} {name}</div>
        <div class="info-card-body">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Voluntary Winding Up ──────────────────────────────────────────────
section_heading("Voluntary Winding Up Details")

tab1, tab2 = st.tabs(["👥 Members' (Solvent)", "🏦 Creditors' (Insolvent)"])

with tab1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">👥 Members' Voluntary Winding Up</div>
        <div class="info-card-body">
        ✔ Requires a <strong>Declaration of Solvency</strong> from directors.<br>
        ✔ Directors state company can pay debts within 12 months.<br>
        ✔ Members appoint the liquidator.
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🏦 Creditors' Voluntary Winding Up</div>
        <div class="info-card-body">
        ✔ No declaration of solvency is possible.<br>
        ✔ Creditors have the primary say in appointing the liquidator.<br>
        ✔ A Meeting of Creditors must be held.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Priority of Claims ───────────────────────────────────────────────
section_heading("Priority of Claims (Order of Payment)")


st.markdown("""
<div class="info-card">
    <div class="info-card-body">
    1. <strong>Secured Creditors</strong> (up to security value)<br>
    2. <strong>Winding up costs</strong> (Liquidator fees, legal costs)<br>
    3. <strong>Preferential Creditors</strong> (Employee wages, government taxes)<br>
    4. <strong>Unsecured Creditors</strong> (Trade suppliers, etc.)<br>
    5. <strong>Shareholders</strong> (Preference first, then Ordinary)
    </div>
</div>
""", unsafe_allow_html=True)

gold_divider()

# ── Quiz ──────────────────────────────────────────────────────────────
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. In Members' Voluntary Winding Up, what must directors declare?",
              ["Declaration of insolvency", "Declaration of solvency"], index=None)
if q1 == "Declaration of solvency":
    success_box("Correct! They must declare the ability to pay debts within 12 months.")

q2 = st.radio("2. Who is paid FIRST in the order of priority?",
              ["Secured creditors", "Unsecured creditors", "Shareholders"], index=None)
if q2 == "Secured creditors":
    success_box("Correct! Secured creditors hold the highest priority on their collateral.")

# ── Recap ─────────────────────────────────────────────────────────────
recap_box([
    "Winding up is the process; Dissolution is the end result.",
    "Compulsory winding up is ordered by the Court (e.g., Section 241).",
    "Solvency declarations are essential for Members' Voluntary Winding Up.",
    "Creditors take control if the company is insolvent.",
    "Fraudulent preferences made within 6 months of winding up can be set aside."
])