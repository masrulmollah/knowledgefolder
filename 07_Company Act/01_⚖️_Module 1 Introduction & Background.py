import streamlit as st
import sys
import os

# 1. MUST BE FIRST: Set page config before any other st. commands
# NOTE: If this page is part of a multipage app and you get an error, 
# ensure the main script (Homepage) is the only one calling this.
try:
    st.set_page_config(page_title="Module 1 – Introduction & Background | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This catches the error if it was already set by the main page
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply styles and content
apply_base_styles()
sidebar_nav()

hero("1", "Introduction & Background",
     "Understand the origins, purpose, and structure of the Companies Act, 1994 — the foundational law governing all companies in Bangladesh.",
     "🏛️")

metric_row([
    ("1994", "Year Enacted"),
    ("11", "Parts in the Act"),
    ("404", "Total Sections"),
    ("1913", "Previous Act Replaced"),
])

st.markdown("<br>", unsafe_allow_html=True)

# ── Historical Background ──────────────────────────────────────────────
section_heading("Historical Background")

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🕰️ Evolution of Company Law in Bangladesh</div>
        <div class="info-card-body">
        Company law in the subcontinent traces back to the <strong>British Companies Act 1844</strong>, 
        which led to the <em>Joint Stock Companies Act 1850</em> — the first company law for the region, 
        based on unlimited liability. In 1857, limited liability was introduced, and the law evolved 
        through multiple amendments over the decades.<br><br>
        After Bangladesh's independence, the <strong>Companies Act 1913</strong> (with amendments through 1984) 
        remained in force until it was replaced by the comprehensive <strong>Companies Act, 1994 (Act No. 18 of 1994)</strong>, 
        which received Presidential assent on <strong>11 September 1994</strong>.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📅 Key Milestones</div>
        <div class="info-card-body">
        <strong>1844</strong> — British Companies Act<br>
        <strong>1850</strong> — Joint Stock Companies Act (subcontinent)<br>
        <strong>1857</strong> — Limited Liability introduced<br>
        <strong>1913</strong> — Companies Act for India/Pakistan/BD<br>
        <strong>1984</strong> — Last amendment to 1913 Act<br>
        <strong>1994</strong> — Companies Act, 1994 enacted<br>
        <strong>1995</strong> — Came into force (SRO 177-law, 1-10-95)
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Why the Act was enacted ───────────────────────────────────────────
section_heading("Objectives & Purpose of the Act")

law_box("Preamble: 'An Act to consolidate and amend the law relating to companies and certain other associations.' — Companies Act, 1994")

objectives = [
    ("🎯", "Consolidation", "To bring all provisions relating to companies under a single, modern law replacing the outdated 1913 Act."),
    ("🏢", "Regulation", "To provide a complete legal framework for the formation, management, and dissolution of companies in Bangladesh."),
    ("🛡️", "Protection", "To protect the rights of shareholders, creditors, and the general public dealing with companies."),
    ("📊", "Transparency", "To ensure proper maintenance of accounts, auditing, and disclosure of financial information."),
    ("⚖️", "Accountability", "To define duties and liabilities of directors, officers, and auditors of companies."),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(objectives):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="info-card" style="min-height:140px;">
            <div class="info-card-title">{icon} {title}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Structure of the Act ───────────────────────────────────────────────
section_heading("Structure of the Act — 11 Parts at a Glance")

parts_data = [
    ("Part I", "Preliminary", "Definitions, short title, commencement, extent"),
    ("Part II", "Incorporation & Formation", "MoA, AoA, registration, associations not for profit"),
    ("Part III", "Share Capital", "Share capital rules, reduction, limited liability of directors"),
    ("Part IV", "Management & Administration", "Registered office, books, meetings, directors, prospectus, auditors"),
    ("Part V", "Winding Up", "Modes of winding up, liquidators, settlement of debts"),
    ("Part VI", "Companies Limited by Guarantee", "Special provisions for guarantee companies"),
    ("Part VII", "Companies Limited by Guarantee & Having Share Capital", "Hybrid company provisions"),
    ("Part VIII", "Unlimited Companies", "Re-registration, special provisions"),
    ("Part IX", "Unregistered Companies", "Winding up of unregistered companies"),
    ("Part X", "Foreign Companies", "Establishment, accounts, closure of foreign companies in BD"),
    ("Part XI", "Supplemental", "Legal proceedings, offences, penalties, fines"),
]

table_html = """
<table>
<tr><th>Part</th><th>Subject</th><th>Key Topics</th></tr>
""" + "".join(f"<tr><td><strong>{p}</strong></td><td>{s}</td><td>{k}</td></tr>" for p, s, k in parts_data) + "</table>"

st.markdown(table_html, unsafe_allow_html=True)

gold_divider()

# ── Key Definitions ───────────────────────────────────────────────────
section_heading("Important Definitions (Section 2)")

tip_box("Why Definitions Matter",
        "The definitions in Section 2 are the building blocks of the entire Act. Every term used throughout the Act draws its meaning from this section.")

definitions = {
    "Company": "A company formed and registered under this Act or an existing company.",
    "Private Company": "A company which by its articles: (i) restricts right to transfer shares, (ii) prohibits public invitation to subscribe shares/debentures, (iii) limits members to 50.",
    "Public Company": "A company incorporated under this Act that is NOT a private company.",
    "Director": "Includes any person occupying the position of director, by whatever name called.",
    "Officer": "Includes a director, managing agent, manager, secretary or any other officer.",
    "Share": "A share in the capital of a company, and includes stock.",
    "Registrar": "The Registrar of Joint Stock Companies (RJSC) performing registration duties.",
}

search_term = st.text_input("🔍 Search definitions...", placeholder="Type a term e.g. 'private company'")

for term, defn in definitions.items():
    if not search_term or search_term.lower() in term.lower() or search_term.lower() in defn.lower():
        with st.expander(f"📌 {term}"):
            st.markdown(f'<div class="law-section-box">{defn}</div>', unsafe_allow_html=True)

gold_divider()

# ── Types of Companies ─────────────────────────────────────────────────
section_heading("Types of Companies Under the Act")

type_data = [
    ("🏦", "Company Limited by Shares", "Liability limited to unpaid amount on shares.", "#e8f4fd"),
    ("🤝", "Company Limited by Guarantee", "Liability limited to amount members undertake to contribute.", "#f0f8ee"),
    ("🔒", "Private Limited Company", "Max 50 members, restricted transfers.", "#fdf0f0"),
    ("🌐", "Public Limited Company", "Unlimited members, can invite public to subscribe.", "#f0f4fd"),
]

cols = st.columns(2)
for i, (icon, name, desc, bg) in enumerate(type_data):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card" style="background:{bg};">
            <div class="info-card-title">{icon} {name}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Quiz ──────────────────────────────────────────────────────────────
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. In which year did the Companies Act, 1994 come into force?",
              ["1993", "1994", "1995", "1996"], index=None)
if q1 == "1995":
    success_box("Correct! Enacted in 1994, effective from 1-10-95.")

# ── Recap ──────────────────────────────────────────────────────────────
recap_box([
    "Companies Act, 1994 replaced the 1913 Act.",
    "The Act has 11 Parts and 404 Sections.",
    "Key types: Private Limited, Public Limited, Guarantee, Unlimited.",
])