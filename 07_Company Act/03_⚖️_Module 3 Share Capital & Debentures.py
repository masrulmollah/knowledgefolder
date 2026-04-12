import streamlit as st
import sys, os

# 1. MUST BE FIRST: Safe page config for multipage apps
try:
    st.set_page_config(page_title="Module 3 – Share Capital & Debentures | Company Act BD", layout="wide", page_icon="📘")
except st.errors.StreamlitAPIException:
    # This prevents the error when called from Homepage.py
    pass

# 2. Setup paths and imports
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

# 3. Apply styles and sidebar
apply_base_styles()
sidebar_nav()

hero("3", "Share Capital & Debentures",
     "Understand the types of share capital, share transfers, reduction of capital, debentures, and charge registration — core knowledge for every finance professional.",
     "💰")

metric_row([
    ("Part III", "Act Coverage"),
    ("2", "Main Share Types"),
    ("4", "Types of Capital"),
    ("21 days", "Charge Reg. Timeline"),
])
st.markdown("<br>", unsafe_allow_html=True)

# ── Types of Capital ──────────────────────────────────────────────────
section_heading("Types of Share Capital")



tip_box("Why Capital Structure Matters",
        "Understanding the different layers of share capital is fundamental to reading a balance sheet, understanding a company's financial position, and advising on corporate transactions.")

capital_types = [
    ("📊", "Authorised Capital", "Also called Registered or Nominal Capital. The maximum amount of share capital which a company is authorised to issue by its MoA. Represents the ceiling.", "#e8f4fd"),
    ("📋", "Issued Capital", "That part of the authorised capital which has been offered to the public or shareholders for subscription. Cannot exceed authorised capital.", "#f0f8ee"),
    ("✅", "Subscribed Capital", "That part of the issued capital which has been applied for and accepted (subscribed) by shareholders.", "#fdf4e8"),
    ("💵", "Paid-up Capital", "That part of subscribed capital which shareholders have actually paid. Remaining unpaid amount is 'calls in arrears'.", "#fdf0f8"),
]

cols = st.columns(2)
for i, (icon, name, desc, bg) in enumerate(capital_types):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card" style="background:{bg};">
            <div class="info-card-title">{icon} {name}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="law-section-box">
📐 <strong>Hierarchy:</strong> Authorised Capital ≥ Issued Capital ≥ Subscribed Capital ≥ Called-up Capital ≥ Paid-up Capital
</div>
""", unsafe_allow_html=True)

gold_divider()

# ── Types of Shares ───────────────────────────────────────────────────
section_heading("Types of Shares")

tab1, tab2 = st.tabs(["📗 Ordinary (Equity) Shares", "📘 Preference Shares"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="info-card-title">📗 Ordinary (Equity) Shares</div>
            <div class="info-card-body">
            • Residual owners of the company<br>
            • Voting rights: One share = One vote<br>
            • Dividend: Variable — depends on profits available after preference<br>
            • Capital repayment: Last priority on winding up<br>
            • No fixed return — upside is unlimited<br>
            • Right to attend and vote at General Meetings<br>
            • Right to appoint/remove directors
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.info("**💡 Key Characteristics**: Equity shareholders bear the most risk but also get the most reward. They are the true owners of the company. Their return is not fixed — it depends on company performance.")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="info-card-title">📘 Preference Shares</div>
            <div class="info-card-body">
            • Fixed dividend rate — paid before ordinary dividend<br>
            • Priority in repayment of capital on winding up<br>
            • Usually carry no/restricted voting rights<br>
            • Can be Cumulative or Non-Cumulative<br>
            • Can be Participating or Non-Participating<br>
            • Can be Redeemable or Irredeemable<br>
            • Can be Convertible (to equity)
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        pref_types = [
            ("Cumulative", "Unpaid dividends accumulate and must be paid in future profitable years before equity dividend"),
            ("Non-Cumulative", "If dividend not paid in a year, it lapses — no right to recover it later"),
            ("Participating", "Get fixed dividend PLUS share in surplus profits after equity dividend"),
            ("Redeemable", "Company can buy back/redeem these shares after a specified period"),
        ]
        for t, d in pref_types:
            st.markdown(f"""
            <div class="info-card" style="padding:12px 16px; margin-bottom:8px;">
                <div class="info-card-title" style="font-size:0.95rem;">{t}</div>
                <div class="info-card-body" style="font-size:0.88rem;">{d}</div>
            </div>
            """, unsafe_allow_html=True)

gold_divider()

# ── Transfer & Transmission ───────────────────────────────────────────
section_heading("Transfer & Transmission of Shares")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🔄 Transfer of Shares</div>
        <div class="info-card-body">
        A <strong>voluntary act</strong> by the shareholder to pass ownership to another person.<br><br>
        <strong>Process:</strong><br>
        ✔ Execute a Share Transfer Form<br>
        ✔ Submit to company with share certificate<br>
        ✔ Company registers in the Register of Members<br>
        ✔ Issue new share certificate to transferee
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">⚖️ Transmission of Shares</div>
        <div class="info-card-body">
        An <strong>operation of law</strong> — shares pass to another party due to death, insolvency, or lunacy (not by voluntary act).<br><br>
        <strong>On Death:</strong> Shares vest in legal heir/executor<br><br>
        <strong>On Insolvency:</strong> Shares vest in the Official Receiver<br><br>
        <strong>Difference:</strong> Transmission does not require an instrument of transfer.
        </div>
    </div>
    """, unsafe_allow_html=True)

warning_box("A private company must communicate a refusal to register a transfer within 2 months.")

gold_divider()

# ── Reduction of Share Capital ────────────────────────────────────────
section_heading("Reduction of Share Capital")

law_box("Section 59 — A company limited by shares may, if authorised by its AoA, by Special Resolution reduce its share capital in any way, subject to confirmation by the Court.")

st.markdown("""
<table>
<tr><th>Step</th><th>Action Required</th></tr>
<tr><td>1</td><td>Check AoA authorises capital reduction</td></tr>
<tr><td>2</td><td>Pass Special Resolution in General Meeting</td></tr>
<tr><td>3</td><td>Apply to Court for confirmation</td></tr>
<tr><td>4</td><td>Court confirms reduction by Order</td></tr>
<tr><td>5</td><td>File Order + altered MoA with Registrar within 90 days</td></tr>
</table>
""", unsafe_allow_html=True)

gold_divider()

# ── Debentures ────────────────────────────────────────────────────────
section_heading("Debentures")



tip_box("Definition", "Under Section 2(e): 'Debenture includes debenture stock, bonds and any other securities of a company...'")

deb_types = [
    ("🔒", "Secured Debentures", "Backed by a charge (fixed or floating) on company assets."),
    ("🔓", "Unsecured Debentures", "No charge on assets. Holders are unsecured creditors."),
    ("💱", "Convertible Debentures", "Can be converted into equity shares after a specified period."),
    ("🔁", "Redeemable Debentures", "Repaid by the company on or before a specified date."),
]

cols = st.columns(2)
for i, (icon, name, desc) in enumerate(deb_types):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-title">{icon} {name}</div>
            <div class="info-card-body">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

gold_divider()

# ── Registration of Charges ───────────────────────────────────────────
section_heading("Registration of Charges")

law_box("Section 107 — Every charge created by a company must be registered with the Registrar within 21 days. Failure makes the charge void against liquidators.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">⚡ Fixed Charge vs Floating Charge</div>
        <div class="info-card-body">
        <strong>Fixed Charge:</strong> Attached to specific identified assets (e.g., land).<br><br>
        <strong>Floating Charge:</strong> Hovers over a class of assets (e.g., inventory). Crystallises on default or winding up.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">⏰ 21-Day Registration Rule</div>
        <div class="info-card-body">
        <strong>Effect of Non-Registration:</strong><br>
        • Charge is void against liquidators/creditors<br>
        • Money secured becomes immediately payable
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

# ── Comparison ────────────────────────────────────────────────────────
section_heading("⚖️ Shares vs Debentures")

comparison_data = [
    ("Nature", "Ownership instrument", "Debt instrument"),
    ("Return", "Dividend (Variable)", "Interest (Fixed)"),
    ("Voting", "Yes", "No"),
    ("Tax", "Paid from after-tax profit", "Tax-deductible expense"),
]

st.markdown("""
<table>
<tr><th>Aspect</th><th>Shares</th><th>Debentures</th></tr>
""" + "".join(f"<tr><td><strong>{a}</strong></td><td>{s}</td><td>{d}</td></tr>" for a, s, d in comparison_data) + "</table>", unsafe_allow_html=True)

# ── Quiz ──────────────────────────────────────────────────────────────
gold_divider()
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. What is the maximum share capital a company can issue?",
              ["Subscribed Capital", "Paid-up Capital", "Authorised Capital"], index=None)
if q1 == "Authorised Capital":
    success_box("Correct!")

q2 = st.radio("2. A charge must be registered with the Registrar within how many days?",
              ["7 days", "14 days", "21 days"], index=None)
if q2 == "21 days":
    success_box("Correct!")

# ── Recap ──────────────────────────────────────────────────────────────
recap_box([
    "Authorised Capital is the ceiling for share issuance.",
    "Transfer is voluntary; Transmission is legal (death/insolvency).",
    "Capital reduction requires Court confirmation.",
    "Charges must be registered within 21 days to be valid against creditors."
])