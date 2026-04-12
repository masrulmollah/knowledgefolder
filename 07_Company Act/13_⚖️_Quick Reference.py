import streamlit as st
import sys, os

# 1. MUST BE THE ABSOLUTE FIRST STREAMLIT COMMAND
# Wrap in try-except to handle multipage app inheritance gracefully
try:
    st.set_page_config(page_title="Supplementary – Quick Reference & Tools | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This prevents the crash if the config was already set by Homepage.py
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply styles and sidebar
apply_base_styles()
sidebar_nav()

hero("SR", "Quick Reference & Professional Tools",
     "Your all-in-one reference hub — key sections at a glance, compliance checklists, comparison tables, glossary, and RJSC forms guide.",
     "🛠️")

st.markdown("<br>", unsafe_allow_html=True)

tabs = st.tabs([
    "📋 Key Sections",
    "📅 Compliance Calendar",
    "⚖️ Pvt vs Public",
    "📝 Glossary",
    "🗂️ RJSC Forms",
    "🔗 Related Laws",
])

# ── Tab 1: Key Sections ───────────────────────────────────────────────
with tabs[0]:
    section_heading("Important Sections — Quick Reference")
    
    tip_box("How to Use This", "Use this table for quick look-up. Sections marked ⭐ are the most frequently referenced.")

    sections = [
        ("2", "⭐", "Definitions — all key terms"),
        ("27", "⭐", "Certificate of Incorporation"),
        ("59", "⭐", "Reduction of Share Capital"),
        ("77", "⭐", "Registered Office Notification"),
        ("85", "⭐", "Annual General Meeting (AGM)"),
        ("103", "⭐", "Director's interest in contracts"),
        ("107", "⭐", "Registration of Charges"),
        ("181", "⭐", "Books of Account"),
        ("233", "⭐", "Minority Protection — Oppression"),
        ("241", "⭐", "Grounds for Compulsory Winding Up"),
    ]

    search = st.text_input("🔍 Search sections...", placeholder="e.g. '181'")

    st.markdown("<table><tr><th>Section</th><th>★</th><th>Subject</th></tr>", unsafe_allow_html=True)
    filtered = [(s, star, sub) for s, star, sub in sections if not search or search.lower() in s.lower() or search.lower() in sub.lower()]
    rows = "".join(f"<tr><td><strong>{s}</strong></td><td>{star}</td><td>{sub}</td></tr>" for s, star, sub in filtered)
    st.markdown(rows + "</table>", unsafe_allow_html=True)

# ── Tab 2: Compliance Calendar ────────────────────────────────────────
with tabs[1]:
    section_heading("Annual Compliance Calendar")

    calendar = [
        ("Ongoing", "🟢", "Maintain statutory registers and books of account"),
        ("Within 30 days", "🟡", "Notify RJSC of changes in Directors or Registered Office"),
        ("Within 21 days", "🟡", "Register a Charge/Mortgage (Form XVIII)"),
        ("Annual", "🔴", "Hold AGM within 6 months of year-end"),
        ("Annual", "🔴", "File Annual Return within 21 days of AGM"),
    ]

    for deadline, colour, action in calendar:
        st.markdown(f"""
        <div class="info-card" style="padding:10px 18px; margin-bottom:6px; display:flex; gap:14px;">
            <div style="min-width:180px; font-weight:600;">{colour} {deadline}</div>
            <div class="info-card-body">{action}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Tab 3: Private vs Public ──────────────────────────────────────────
with tabs[2]:
    section_heading("Comparison: Private vs Public Company")

    st.markdown("""
    <table>
    <tr><th>Aspect</th><th>Private Company</th><th>Public Company</th></tr>
    <tr><td>Min Members</td><td>2</td><td>7</td></tr>
    <tr><td>Max Members</td><td>50</td><td>Unlimited</td></tr>
    <tr><td>Min Directors</td><td>2</td><td>3</td></tr>
    <tr><td>Share Transfer</td><td>Restricted</td><td>Free</td></tr>
    <tr><td>Prospectus</td><td>Not required</td><td>Required</td></tr>
    </table>
    """, unsafe_allow_html=True)

# ── Tab 5: RJSC Forms ─────────────────────────────────────────────────
with tabs[4]:
    section_heading("Key RJSC Forms")

    forms = [
        ("Form VI", "Change of Registered Office"),
        ("Form XII", "Particulars of Directors/Managers"),
        ("Form XIII", "Return of Allotments"),
        ("Form XVIII", "Particulars of Charge"),
        ("Form XXX", "Annual Return"),
    ]

    st.markdown("<table><tr><th>Form No.</th><th>Purpose</th></tr>" + 
                "".join(f"<tr><td><strong>{f}</strong></td><td>{p}</td></tr>" for f, p in forms) + 
                "</table>", unsafe_allow_html=True)

# ── Final Recap ──────────────────────────────────────────────────────
gold_divider()
recap_box([
    "This hub is a live reference—keep it open during compliance checks.",
    "Form XII and Form XXX are the most common filings for active companies.",
    "Missing the 21-day AGM filing window (Form XXX) leads to daily fines.",
    "Always check the BSEC Corporate Governance Code if your company is listed."
])