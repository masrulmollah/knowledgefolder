import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from styles import *

st.set_page_config(page_title="Module 12 – Offences & Penalties | Company Act BD", layout="wide", page_icon="📘")
apply_base_styles()
sidebar_nav()

hero("12", "Offences, Penalties & Legal Proceedings",
     "A comprehensive reference of offences, penalties, and legal proceedings under the Companies Act, 1994 — critical for compliance risk management.",
     "⚖️")

metric_row([
    ("Part XI", "Act Coverage"),
    ("Section 396", "Cognisance"),
    ("2 Years", "Max Imprisonment"),
    ("Section 404", "Final Section"),
])
st.markdown("<br>", unsafe_allow_html=True)

tip_box("Practical Importance",
        "Understanding the offences and penalties under the Act is essential for risk management. Directors and officers can face both corporate fines AND personal imprisonment for many violations.")

section_heading("Key Offences & Penalties Reference Table")

offences = [
    ("Misstatement in Prospectus (wilful)", "Director, Promoter, any authorised person", "Imprisonment up to 2 years and/or fine"),
    ("Failure to keep proper Books of Account", "Every officer in default", "Imprisonment up to 6 months and/or fine"),
    ("Failure to hold AGM", "Every officer in default", "Fine up to Tk. 5,000 + Tk. 250/day continuing"),
    ("Failure to file Annual Return", "Company and every officer", "Fine Tk. 500/day for every day of default"),
    ("Failure to register a Charge", "Company and every officer in default", "Fine up to Tk. 500/day"),
    ("False Declaration of Solvency", "Directors making declaration", "Imprisonment up to 6 months and/or fine"),
    ("Fraudulent Trading", "Officers who carried on business fraudulently", "Personal liability for all debts + criminal prosecution"),
    ("Carrying on business with fewer than minimum members", "Every officer knowingly party", "Personal liability for all debts incurred"),
    ("Unauthorised use of 'Limited' in company name", "Any person", "Fine up to Tk. 1,000"),
    ("Failure to display company name at office", "Company and every officer in default", "Fine"),
    ("Failure to give notice of change of directors", "Company and every officer in default", "Fine"),
    ("Non-compliance with Registrar's inspection direction", "Company and officers", "Fine and/or imprisonment"),
    ("Fraudulent preference payment before winding up", "Directors/officers responsible", "Transaction voidable; personal liability"),
    ("Wrongful withholding of company property", "Person withholding", "Fine and court order to return"),
    ("Failure to file return after final meeting (winding up)", "Liquidator", "Fine up to Tk. 500/day"),
]

st.markdown("""
<table>
<tr><th>Offence</th><th>Person Liable</th><th>Penalty</th></tr>
""" + "".join(f"<tr><td>{o}</td><td>{p}</td><td style='color:#b33a3a;'><strong>{pen}</strong></td></tr>" for o, p, pen in offences) + """
</table>
""", unsafe_allow_html=True)

gold_divider()

section_heading("'Officer in Default' — Who is Liable?")

law_box("Under the Act, 'officer in default' means any officer of the company who is knowingly and wilfully authorised or permitted the default, contravention, or failure.")

st.markdown("""
<div class="info-card">
    <div class="info-card-title">👤 Who Can Be an 'Officer in Default'?</div>
    <div class="info-card-body">
    The following can be held liable as 'officer in default':<br><br>
    ✔ <strong>Managing Director</strong> — if specifically responsible for the area of default<br>
    ✔ <strong>Directors</strong> — who knowingly permitted or authorised the default<br>
    ✔ <strong>Company Secretary</strong> — for filing and procedural defaults<br>
    ✔ <strong>Manager</strong> — for defaults in their area of responsibility<br>
    ✔ <strong>Any other officer</strong> who participated in or authorised the default<br><br>
    <em>Note: Not every director is automatically liable for every default — only those who knowingly permitted it.</em>
    </div>
</div>
""", unsafe_allow_html=True)

gold_divider()
section_heading("Cognisance of Offences — Section 396")

law_box("Section 396 — No Court shall take cognisance of any offence under this Act except upon complaint made by, or with the sanction of, the Registrar or the Government.")

warning_box("This is an important procedural requirement. A private party cannot directly file a criminal complaint under the Companies Act without the Registrar's complaint or sanction. However, civil remedies are separately available.")

gold_divider()
section_heading("Compounding of Offences")

info_card("🤝 Compounding (Settlement)",
          "Certain offences under the Act may be 'compounded' (settled) by paying a fine without going through full criminal proceedings. The Registrar or Government has power to compound offences on payment of a sum not exceeding the maximum fine specified. This is a practical option for technical/procedural defaults.")

gold_divider()
section_heading("Limitation of Prosecutions")

st.markdown("""
<div class="info-card">
    <div class="info-card-title">⏰ Time Limits for Prosecution</div>
    <div class="info-card-body">
    For offences under the Companies Act, the general limitation period for prosecution is governed by the Code of Criminal Procedure. For continuing offences (where penalty accrues per day), each day constitutes a separate offence — so limitation runs from the date the default is remedied.
    </div>
</div>
""", unsafe_allow_html=True)

gold_divider()
section_heading("Power to Require Security for Costs")

info_card("🏦 Security for Costs",
          "The Court may require a limited company which is plaintiff in any civil proceedings to provide security for the defendant's costs, where it appears there is reason to believe the company will be unable to pay costs if unsuccessful. This prevents shell companies from bringing frivolous litigation.")

gold_divider()
section_heading("Key Case Law Notes")

cases = [
    ("Solomon v Solomon & Co. [1897]", "Foundation case on separate legal entity — company is distinct from its shareholders even if one person holds virtually all shares. Applicable principle under Bangladesh Act."),
    ("Foss v Harbottle [1843]", "Majority rule — wrong done to company should be remedied by company itself. Basis for limits on minority shareholder suits. Modified by Section 233 (oppression remedy)."),
    ("Re City Equitable Fire Insurance [1925]", "Standard of care for directors — not expected to give continuous attention to business; can delegate and rely on properly qualified officers."),
    ("Saloman Doctrine in Bangladesh", "Bangladesh courts follow the separate legal entity principle. Piercing the corporate veil is exceptional — fraud or sham must be proved."),
]

for case, desc in cases:
    with st.expander(f"📚 {case}"):
        st.markdown(f'<div class="law-section-box">{desc}</div>', unsafe_allow_html=True)

gold_divider()
section_heading("🧠 Test Your Knowledge")

q1 = st.radio("1. Who must sanction a criminal complaint under the Companies Act before a Court can take cognisance?",
              ["Any shareholder", "The Registrar or Government", "A director of the company", "Any creditor"], index=None)
if q1 == "The Registrar or Government":
    success_box("Correct! Under Section 396, a Court can only take cognisance of an offence under the Act upon complaint by, or with sanction of, the Registrar or the Government.")
elif q1:
    warning_box("Incorrect. Only the Registrar's complaint or Government sanction allows a Court to take cognisance (Section 396).")

q2 = st.radio("2. What is the maximum imprisonment for wilful misstatement in a Prospectus?",
              ["6 months", "1 year", "2 years", "5 years"], index=None)
if q2 == "2 years":
    success_box("Correct! Wilful misstatement in a prospectus carries a maximum imprisonment of 2 years and/or fine.")
elif q2:
    warning_box("Incorrect. The maximum imprisonment for wilful misstatement in prospectus is 2 years.")

recap_box([
    "Officers 'in default' are personally liable — not just the company as an entity",
    "False Declaration of Solvency carries imprisonment up to 6 months",
    "Failure to file Annual Return attracts Tk. 500/day penalty",
    "Courts cannot take cognisance of offences without Registrar's complaint or Government sanction",
    "Compounding allows settlement of technical offences by payment of fine",
    "Fraudulent trading can result in directors being personally liable for ALL company debts",
    "Separate legal entity is the foundation of company law — veil pierced only for fraud",
])