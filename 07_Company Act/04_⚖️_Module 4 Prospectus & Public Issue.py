import streamlit as st
import sys, os

# 1. MUST BE THE ABSOLUTE FIRST STREAMLIT COMMAND
try:
    st.set_page_config(page_title="Module 4 – Prospectus & Public Issue | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # Catch error if config is already set by the Homepage/Main script
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply styles and sidebar
apply_base_styles()
sidebar_nav()

# ── Hero Section ──────────────────────────────────────────────────────
hero("4", "Prospectus & Public Issue",
     "Understand the rules governing prospectus, public share issuance, allotment of shares, and liability for misstatements — essential for capital market professionals.",
     "📣")

metric_row([
    ("Part IV", "Act Coverage"),
    ("120 days", "Prospectus Validity"),
    ("5%", "Min. Application Money"),
    ("3 years", "Director Liability Period"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── What is a Prospectus ──────────────────────────────────────────────
section_heading("What is a Prospectus?")

tip_box("Definition",
        "A Prospectus is any document described or issued as a prospectus, and includes any notice, circular, advertisement or other document inviting deposits from the public or inviting offers from the public for the subscription or purchase of any shares or debentures of a company.")

law_box("Key Rule: Only a PUBLIC company can issue a prospectus to invite the public. A PRIVATE company is prohibited from issuing a prospectus or inviting the public to subscribe for its shares.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🎯 Purpose of a Prospectus</div>
        <div class="info-card-body">
        • Invites the public to subscribe for shares/debentures<br>
        • Provides complete information for informed investment decisions<br>
        • Establishes civil and criminal liability for misstatements<br>
        • Must be filed with the Registrar before publication
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">⏳ Registration Requirement</div>
        <div class="info-card-body">
        A prospectus must be:<br>
        ✔ <strong>Dated</strong> — the date of publication<br>
        ✔ <strong>Registered</strong> with the Registrar on/before publication<br>
        ✔ <strong>Valid for 90 days</strong> from the date of registration<br>
        ✔ <strong>Signed</strong> by every named director
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Mandatory Contents ────────────────────────────────────────────────
section_heading("Mandatory Contents of a Prospectus")



contents = [
    ("📋", "Company Information", "Name, registered office address, objects of the company"),
    ("👥", "Directors & Promoters", "Names, addresses, and qualifications of directors"),
    ("💰", "Financial Information", "Share capital structure and minimum subscription amount"),
    ("📊", "Financial Statements", "Audited accounts and profit/loss history"),
    ("🎯", "Use of Proceeds", "How the funds raised will be utilised"),
    ("⚖️", "Litigation", "Details of any pending legal proceedings"),
]

cols = st.columns(2)
for i, (icon, title, desc) in enumerate(contents):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card" style="padding:14px 18px; margin-bottom:8px;">
            <div class="info-card-title" style="font-size:0.95rem;">{icon} {title}</div>
            <div class="info-card-body" style="font-size:0.88rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Allotment of Shares ───────────────────────────────────────────────
section_heading("Allotment of Shares")

law_box("Section 151 — No allotment shall be made unless the minimum subscription has been subscribed and the application money received.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📐 Minimum Subscription Rule</div>
        <div class="info-card-body">
        ✔ Must be stated in the prospectus<br>
        ✔ Application money must be at least 5% of nominal value<br>
        ✔ If not received within <strong>120 days</strong> → all money must be refunded<br>
        ✔ If not refunded within 130 days → directors become personally liable for interest.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">⚠️ Irregular Allotment</div>
        <div class="info-card-body">
        An allotment is <strong>irregular (voidable)</strong> if made before minimum subscription or application money is received. The applicant can avoid the allotment within 2 months.
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Liability for Misstatements ───────────────────────────────────────
section_heading("Liability for Misstatements in Prospectus")

tab1, tab2 = st.tabs(["⚖️ Civil Liability", "🚔 Criminal Liability"])

with tab1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">💼 Civil Liability — Compensation</div>
        <div class="info-card-body">
        Subscribers can claim <strong>compensation</strong> from directors, promoters, and experts for misleading statements. 
        <strong>Defences:</strong> Withdrawal of consent before issue or reasonable belief in truth.
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🚔 Criminal Liability</div>
        <div class="info-card-body">
        Wilfully untrue statements or fraudulent concealment can lead to:<br>
        🔴 <strong>Imprisonment</strong> up to 2 years<br>
        🔴 <strong>Fine</strong><br>
        🔴 <strong>Both</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Issue at Premium / Discount ────────────────────────────────────────
section_heading("Shares Issued at Premium or Discount")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card" style="background:#f0f8ee;">
        <div class="info-card-title">📈 Issue at Premium</div>
        <div class="info-card-body">
        Premium must go to a <strong>Share Premium Account</strong>. Usable for: Bonus shares, writing off preliminary expenses, or redemption premiums.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card" style="background:#fff5f5;">
        <div class="info-card-title">📉 Issue at Discount</div>
        <div class="info-card-body">
        Generally <strong>not permitted</strong> except with court approval and strict conditions (max 10% discount).
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Interactive ───────────────────────────────────────────────────────
gold_divider()
section_heading("🛠️ Interactive: Public Issue Scenario")

face_val = st.number_input("Face value per share (Tk.)", min_value=1, value=10)
issue_price = st.number_input("Issue price per share (Tk.)", min_value=1, value=25)
num_shares = st.number_input("Total shares to be issued", min_value=1000, value=1000000)

premium = issue_price - face_val
total_issue_size = issue_price * num_shares

if premium > 0:
    st.success(f"Issue at Premium! Share Premium Account Credit: Tk. {premium * num_shares:,.0f}")
elif premium < 0:
    st.error("Issue at Discount — Requires Court Approval.")
else:
    st.info(f"Issue at Par. Total Size: Tk. {total_issue_size:,.0f}")

# ── Quiz ──────────────────────────────────────────────────────────────
gold_divider()
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Which company can issue a prospectus?", ["Private Limited", "Public Limited"], index=None)
if q1 == "Public Limited":
    st.success("Correct!")

# ── Recap ──────────────────────────────────────────────────────────────
recap_box([
    "Only Public Companies can issue a prospectus.",
    "Prospectus must be registered with RJSC and is valid for 90 days.",
    "Minimum subscription must be met within 120 days, or money is refunded.",
    "Misstatements carry both civil compensation and criminal penalties.",
    "Share premiums must be kept in a specific Share Premium Account."
])