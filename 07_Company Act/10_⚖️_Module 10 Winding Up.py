import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

st.set_page_config(page_title="Module 10 – Winding Up | Company Act BD", layout="wide", page_icon="📘")
apply_base_styles()
sidebar_nav()

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

section_heading("What is Winding Up?")
tip_box("Definition",
        "Winding up (also called liquidation) is the process by which a company's life is brought to an end. The company's assets are collected and realised, its debts and liabilities are paid off, and any surplus is distributed among members. After winding up, the company is formally dissolved.")

gold_divider()

section_heading("Modes of Winding Up")

modes = [
    ("⚖️", "Compulsory Winding Up (by Court)", "The Court orders the company to be wound up. Usually initiated by creditors, members, or the Government. Sections 241–303.", "#fff5f5"),
    ("🤝", "Voluntary Winding Up", "Initiated by the company itself — either by members (solvent) or by creditors (insolvent). Sections 304–354.", "#f0f8ee"),
    ("🏛️", "Winding Up Subject to Court Supervision", "Company voluntarily passes resolution to wind up but Court exercises supervision over the process. Sections 355–358.", "#f0f4fd"),
]

for icon, name, desc, bg in modes:
    st.markdown(f"""
    <div class="info-card" style="background:{bg}; margin-bottom:12px;">
        <div class="info-card-title">{icon} {name}</div>
        <div class="info-card-body">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

section_heading("Compulsory Winding Up — Grounds (Section 241)")

law_box("Section 241 — A company may be wound up by the Court on the following grounds:")

grounds = [
    ("1", "Special Resolution", "The company has by Special Resolution resolved that it be wound up by the Court"),
    ("2", "Failure to Commence Business", "Company has not commenced business within 1 year from incorporation, or suspended business for a whole year"),
    ("3", "Member Numbers Below Minimum", "Number of members has fallen below 2 (private) or 7 (public)"),
    ("4", "Unable to Pay Debts", "Company is unable to pay its debts (most common ground used by creditors)"),
    ("5", "Just & Equitable", "Court considers it just and equitable to wind up the company (catch-all provision — deadlock, loss of substratum, fraud, etc.)"),
    ("6", "Default in Filing", "Company defaults in filing statutory report, holding statutory meeting (public companies)"),
]

st.markdown("""
<table>
<tr><th>#</th><th>Ground</th><th>Details</th></tr>
""" + "".join(f"<tr><td>{n}</td><td><strong>{g}</strong></td><td>{d}</td></tr>" for n, g, d in grounds) + """
</table>
""", unsafe_allow_html=True)

gold_divider()

section_heading("Unable to Pay Debts — Section 243")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">💸 When is a Company 'Unable to Pay Debts'?</div>
        <div class="info-card-body">
        A company is deemed unable to pay its debts if:<br><br>
        ✔ A creditor owed >Tk.500 serves a demand, and the company fails to pay within <strong>3 weeks</strong><br>
        ✔ Execution or legal process issued against the company is unsatisfied<br>
        ✔ The Court is satisfied that the company <strong>cannot pay its debts</strong> after considering all contingent liabilities
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">👤 Who Can Petition for Compulsory W/U?</div>
        <div class="info-card-body">
        • The <strong>company itself</strong><br>
        • Any <strong>creditor(s)</strong> (including contingent/prospective creditors)<br>
        • Any <strong>contributory</strong> (present or past member)<br>
        • The <strong>Official Liquidator</strong><br>
        • The <strong>Registrar</strong> (for certain defaults)<br>
        • The <strong>Government</strong> (in public interest)
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

section_heading("Voluntary Winding Up")

tab1, tab2 = st.tabs(["👥 Members' Voluntary W/U", "🏦 Creditors' Voluntary W/U"])

with tab1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">👥 Members' Voluntary Winding Up (Solvent Company)</div>
        <div class="info-card-body">
        Used when the company is <strong>SOLVENT</strong> — able to pay all its debts in full within 12 months.<br><br>
        <strong>Key Requirement — Declaration of Solvency:</strong><br>
        ✔ Majority of directors must make a <strong>statutory declaration of solvency</strong><br>
        ✔ Declaration states company can pay all debts within 12 months of commencement of winding up<br>
        ✔ Must be filed with RJSC before the winding up resolution<br>
        ✔ Directors making false declaration are liable (imprisonment up to 6 months and/or fine)<br><br>
        <strong>Process:</strong><br>
        1. Board passes resolution and makes declaration of solvency<br>
        2. Members pass Special Resolution for voluntary winding up<br>
        3. Liquidator appointed by members<br>
        4. Company ceases normal business (only for winding up purposes)
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🏦 Creditors' Voluntary Winding Up (Insolvent Company)</div>
        <div class="info-card-body">
        Used when the company is <strong>INSOLVENT</strong> — cannot pay all debts within 12 months.<br><br>
        <strong>Key Features:</strong><br>
        ✔ No declaration of solvency is made<br>
        ✔ Creditors have significant control over the process<br>
        ✔ Company calls a <strong>Creditors' Meeting</strong> within 14 days of members' resolution<br>
        ✔ Directors present a full statement of affairs to creditors<br>
        ✔ <strong>Creditors' nominated liquidator</strong> takes precedence over members' nominee<br>
        ✔ Creditors may appoint a Committee of Inspection (max 5 members)<br>
        ✔ Liquidator must report to creditors at regular intervals
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

section_heading("Role & Powers of Liquidator")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🏛️ Official Liquidator (Compulsory W/U)</div>
        <div class="info-card-body">
        Appointed by the Court from a panel of official liquidators.<br><br>
        <strong>Key Powers & Duties:</strong><br>
        ✔ Collect and realise assets of the company<br>
        ✔ Sue and be sued in the company's name<br>
        ✔ Carry on business only for beneficial winding up<br>
        ✔ Pay dividends to creditors<br>
        ✔ Settle list of contributories<br>
        ✔ Investigate conduct of directors and officers<br>
        ✔ Apply to Court for directions<br>
        ✔ Submit final account to Court before dissolution
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">📊 Priority of Claims in Winding Up</div>
        <div class="info-card-body">
        Assets distributed in this strict order:<br><br>
        <strong>1st:</strong> Secured creditors (up to value of security)<br>
        <strong>2nd:</strong> Winding up costs and expenses<br>
        <strong>3rd:</strong> Preferential creditors (employee wages, tax arrears)<br>
        <strong>4th:</strong> Unsecured creditors (trade creditors, debenture holders without security)<br>
        <strong>5th:</strong> Members — preference shareholders<br>
        <strong>6th:</strong> Members — ordinary/equity shareholders<br><br>
        <em>If assets insufficient → creditors of same rank paid pari passu (proportionately)</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

section_heading("Fraudulent Preference & Void Transactions")

warning_box("Transactions made by an insolvent company to 'prefer' certain creditors over others before winding up may be set aside by the Court as 'fraudulent preferences'.")

prefs = [
    ("⚠️", "Fraudulent Preference", "A payment or transfer made to a specific creditor within 6 months before winding up, with intent to prefer that creditor, can be set aside by Court. The creditor must return what was received."),
    ("🚫", "Void Dispositions", "Any disposition of property, transfer of shares, or alteration in members' register after commencement of winding up is void unless Court orders otherwise."),
    ("⚖️", "Fraudulent Trading", "If any business was carried on with intent to defraud creditors, the Court may declare directors/officers personally liable for all or part of the company's debts."),
]
for icon, title, desc in prefs:
    info_card(f"{icon} {title}", desc)

gold_divider()

section_heading("Dissolution — End of Company Life")

success_box("Dissolution is the formal legal death of the company. After dissolution, the company no longer exists as a legal person. All proceedings against it cease, and remaining assets vest in the Government.")

dissolution_steps = [
    "Liquidator completes realisation of all assets",
    "All creditors paid (or settlement reached)",
    "Surplus distributed among members (if any)",
    "Final accounts prepared and audited",
    "Final meeting of members/creditors held",
    "Return of Final Meeting filed with RJSC",
    "Registrar registers the return and company is dissolved after 3 months",
    "Company struck off the Register — ceases to exist",
]
for i, step in enumerate(dissolution_steps, 1):
    st.markdown(f"""
    <div class="info-card" style="padding:10px 18px; margin-bottom:6px; display:flex; gap:14px; align-items:center;">
        <div style="background:#1a3a5c; color:#c8922a; font-family:'Fira Mono',monospace; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0;">{i}</div>
        <div class="info-card-body">{step}</div>
    </div>
    """, unsafe_allow_html=True)

gold_divider()

section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. In Members' Voluntary Winding Up, what must directors declare?",
              ["Declaration of insolvency", "Declaration of solvency", "Declaration of assets", "Declaration of debts"], index=None)
if q1 == "Declaration of solvency":
    success_box("Correct! Directors must make a statutory Declaration of Solvency stating the company can pay all debts within 12 months.")
elif q1:
    warning_box("Incorrect. Directors must make a Declaration of Solvency — stating ability to pay all debts within 12 months.")

q2 = st.radio("2. Which ground for compulsory winding up is most commonly used by creditors?",
              ["Just and equitable", "Failure to commence business", "Unable to pay debts", "Special Resolution"], index=None)
if q2 == "Unable to pay debts":
    success_box("Correct! Inability to pay debts (Section 243) is the most commonly used ground when creditors petition for winding up.")
elif q2:
    warning_box("Incorrect. 'Unable to pay debts' under Section 243 is the most common ground for creditor-initiated winding up.")

q3 = st.radio("3. In the priority of payment in winding up, who is paid FIRST?",
              ["Unsecured creditors", "Ordinary shareholders", "Secured creditors", "Preference shareholders"], index=None)
if q3 == "Secured creditors":
    success_box("Correct! Secured creditors are paid first (up to the value of their security), followed by winding up costs, preferential creditors, unsecured creditors, then shareholders.")
elif q3:
    warning_box("Incorrect. Secured creditors have the highest priority, followed by winding up costs, preferential creditors, unsecured creditors, then shareholders.")

recap_box([
    "Three modes of winding up: Compulsory (by Court), Voluntary (by company), Subject to Court Supervision",
    "Compulsory winding up: 6 grounds including inability to pay debts and just & equitable",
    "Members' Voluntary W/U requires Declaration of Solvency from directors",
    "Creditors' Voluntary W/U: creditors' nominated liquidator takes precedence",
    "Priority order: Secured → Winding up costs → Preferential → Unsecured → Preference shareholders → Equity shareholders",
    "Fraudulent preferences made within 6 months before winding up can be set aside by Court",
    "After dissolution, company ceases to be a legal person — it no longer exists",
])