import streamlit as st
import sys, os

# 1. ABSOLUTELY FIRST: Handle page config safely for multipage apps
try:
    st.set_page_config(page_title="Module 2 – Incorporation & Formation | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # If already set by Homepage.py, ignore and move on
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply custom styles and sidebar
apply_base_styles()
sidebar_nav()

# ── Hero Section ──────────────────────────────────────────────────────
hero("2", "Incorporation & Formation of a Company",
     "Master the process of forming a company — from drafting the Memorandum and Articles of Association to obtaining the Certificate of Incorporation.",
     "🏗️")

metric_row([
    ("Part II", "Act Coverage"),
    ("2", "Min. Members (Pvt.)"),
    ("7", "Min. Members (Public)"),
    ("6", "Clauses in MoA"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Overview ──────────────────────────────────────────────────────────
section_heading("Overview of Company Formation Process")

steps = [
    ("1️⃣", "Draft MoA & AoA", "Prepare Memorandum and Articles of Association as per Act requirements"),
    ("2️⃣", "Name Clearance", "Obtain name clearance from the Registrar of Joint Stock Companies (RJSC)"),
    ("3️⃣", "Sign & Witness", "Subscribers sign MoA & AoA in the presence of at least 2 witnesses"),
    ("4️⃣", "File with RJSC", "Submit MoA, AoA, and required forms/fees to the RJSC"),
    ("5️⃣", "Certificate Issued", "RJSC reviews and issues the Certificate of Incorporation"),
    ("6️⃣", "Legal Existence", "From the date on the certificate, the company becomes a legal person"),
]
cols = st.columns(3)
for i, (num, title, desc) in enumerate(steps):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="info-card" style="min-height:130px;">
            <div class="info-card-title">{num} {title}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── MoA ───────────────────────────────────────────────────────────────
section_heading("Memorandum of Association (MoA)")

tip_box("What is MoA?",
        "The MoA is the 'constitution' of the company — the fundamental document that defines the company's relationship with the outside world. It is the charter of the company. A company cannot act beyond what the MoA allows.")

st.markdown("<div class='section-heading' style='font-size:1.1rem;'>The Six Mandatory Clauses of the MoA</div>", unsafe_allow_html=True)

clauses = [
    ("📛", "1. Name Clause", "States the name of the company. A private company must end with 'Limited' or 'Ltd.' and a public company with 'Public Limited Company' or 'PLC'."),
    ("📍", "2. Registered Office Clause", "States the name of the division/district in Bangladesh where the registered office will be situated."),
    ("🎯", "3. Objects Clause", "States the objects/purpose for which the company is formed. The company cannot act beyond these objects (ultra vires doctrine)."),
    ("🛡️", "4. Liability Clause", "States whether the liability of members is limited (by shares or by guarantee) or unlimited."),
    ("💰", "5. Capital Clause", "States the amount of authorised (registered) share capital and its division into shares of fixed value."),
    ("✍️", "6. Subscription Clause", "Names and addresses of subscribers who agree to take at least one share each, signed before witnesses."),
]

for icon, title, body in clauses:
    with st.expander(f"{icon} {title}"):
        st.markdown(f'<div class="law-section-box">{body}</div>', unsafe_allow_html=True)

law_box("Section 13 — Alteration of MoA: A company cannot alter MoA conditions EXCEPT as provided in the Act.")

warning_box("The Objects Clause is critical — any transaction beyond the stated objects is 'ultra vires' and void, even if approved by all shareholders.")

gold_divider()

# ── AoA ───────────────────────────────────────────────────────────────
section_heading("Articles of Association (AoA)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📋 What is AoA?</div>
        <div class="info-card-body">
        The AoA is the internal rulebook of the company — it governs the internal management. If a company does not register its own AoA, <strong>Schedule I of the Act</strong> applies automatically.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🔧 Alteration of AoA</div>
        <div class="info-card-body">
        The AoA can be altered by a <strong>Special Resolution</strong> passed at a general meeting, provided it doesn't conflict with the MoA or the Act.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── MoA vs AoA ────────────────────────────────────────────────────────
section_heading("MoA vs AoA — Key Differences")

st.markdown("""
<table>
<tr><th>Aspect</th><th>Memorandum of Association</th><th>Articles of Association</th></tr>
<tr><td><strong>Nature</strong></td><td>Supreme/fundamental document</td><td>Subordinate to MoA</td></tr>
<tr><td><strong>Purpose</strong></td><td>Defines relationship with outside world</td><td>Governs internal management</td></tr>
<tr><td><strong>Alteration</strong></td><td>Very restricted</td><td>By Special Resolution</td></tr>
<tr><td><strong>Ultra Vires</strong></td><td>Acts beyond MoA are void</td><td>Acts beyond AoA may be ratified</td></tr>
</table>
""", unsafe_allow_html=True)

gold_divider()

# ── Registration Process ─────────────────────────────────────────────
section_heading("Registration Process with RJSC")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📁 Documents Required</div>
        <div class="info-card-body">
        ✔ Signed MoA & AoA<br>
        ✔ Form I (Compliance Declaration)<br>
        ✔ Form VI (Registered Office)<br>
        ✔ Form IX, X, XII (Director Details)<br>
        ✔ Registration Fees & Name Clearance
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">✅ Effect of Certificate</div>
        <div class="info-card-body">
        Once incorporated, the company becomes a <strong>separate legal entity</strong> with <strong>perpetual succession</strong>. It can sue, be sued, and own property in its own name.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Interactive ──────────────────────────────────────────────────────
section_heading("🛠️ Interactive: Company Type Checklist")

q_members = st.slider("How many members will your company have?", 2, 200, 5)
q_public = st.selectbox("Will you invite the general public to subscribe?", ["No", "Yes"])
q_transfer = st.selectbox("Will share transfers be restricted?", ["Yes – restricted", "No – freely transferable"])

if q_members <= 50 and q_public == "No" and q_transfer == "Yes – restricted":
    success_box(f"✅ Qualifies as a **PRIVATE LIMITED COMPANY** (Section 2). Min 2 directors.")
else:
    warning_box("⚠️ Qualifies as a **PUBLIC LIMITED COMPANY**. Requires min 7 members and 3 directors.")

# ── Quiz ──────────────────────────────────────────────────────────────
gold_divider()
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Which document is the 'constitution' of a company?",
              ["Articles of Association", "Memorandum of Association", "Prospectus"], index=None)
if q1 == "Memorandum of Association":
    success_box("Correct!")

# ── Recap ──────────────────────────────────────────────────────────────
recap_box([
    "MoA is the supreme charter with 6 mandatory clauses.",
    "AoA governs internal rules; Schedule I applies if AoA is missing.",
    "The Certificate of Incorporation is conclusive evidence of legal existence.",
    "Incorporation creates a separate legal entity and perpetual succession."
])