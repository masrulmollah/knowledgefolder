import streamlit as st

CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&family=Fira+Mono:wght@400;500&display=swap');
.hero{background:linear-gradient(135deg,#1a3a5c,#0d2340);border-radius:14px;padding:40px 36px;margin-bottom:28px;}
.hero-tag{font-family:'Fira Mono',monospace;font-size:11px;color:#c8922a;letter-spacing:3px;text-transform:uppercase;margin-bottom:10px;}
.hero-title{font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:700;color:#fff;margin-bottom:12px;line-height:1.2;}
.hero-sub{font-size:1rem;color:rgba(255,255,255,0.72);line-height:1.7;}
.sec-head{font-family:'Playfair Display',serif;font-size:1.35rem;font-weight:600;color:#1a3a5c;border-left:4px solid #c8922a;padding-left:12px;margin:26px 0 14px 0;}
.card{background:#fff;border-radius:10px;padding:20px 22px;margin-bottom:14px;border:1px solid #e8e0d0;box-shadow:0 2px 8px rgba(26,58,92,0.06);}
.card-title{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:600;color:#1a3a5c;margin-bottom:7px;}
.card-body{font-size:0.95rem;color:#4a4a4a;line-height:1.7;}
.law-box{background:linear-gradient(135deg,#1a3a5c08,#c8922a10);border:1px solid #c8922a40;border-left:4px solid #c8922a;border-radius:8px;padding:14px 18px;margin:10px 0;font-family:'Fira Mono',monospace;font-size:0.86rem;color:#1a3a5c;}
.tip-box{background:linear-gradient(135deg,#fff8ec,#fff3e0);border:1px solid #f0c060;border-radius:10px;padding:16px 20px;margin:14px 0;}
.tip-title{font-family:'Playfair Display',serif;font-size:0.92rem;font-weight:700;color:#b07a10;margin-bottom:5px;}
.tip-body{font-size:0.9rem;color:#5a4a20;line-height:1.6;}
.warn-box{background:#fff5f5;border:1px solid #f0a0a0;border-left:4px solid #b33a3a;border-radius:8px;padding:14px 18px;margin:10px 0;font-size:0.9rem;color:#7a2020;line-height:1.6;}
.ok-box{background:#f0faf4;border:1px solid #90d0a8;border-left:4px solid #2d7a4f;border-radius:8px;padding:14px 18px;margin:10px 0;font-size:0.9rem;color:#1a4a30;line-height:1.6;}
.metric-box{background:#fff;border-radius:10px;padding:16px;text-align:center;border:1px solid #e8e0d0;}
.metric-num{font-family:'Playfair Display',serif;font-size:1.9rem;font-weight:700;color:#1a3a5c;}
.metric-lbl{font-size:0.78rem;color:#999;text-transform:uppercase;letter-spacing:1px;}
.gold-line{border:none;height:2px;background:linear-gradient(to right,#c8922a,transparent);margin:22px 0;}
table{width:100%;border-collapse:collapse;font-size:0.91rem;margin:10px 0;}
th{background:#1a3a5c;color:#fff;padding:9px 13px;text-align:left;font-weight:600;}
td{padding:8px 13px;border-bottom:1px solid #e8e0d0;vertical-align:top;}
tr:nth-child(even) td{background:#f9f6f0;}
</style>"""

st.markdown(CSS, unsafe_allow_html=True)

def hero(title, subtitle, icon="📘"):
    st.markdown(f"""
    <div class="hero">
        <div class="hero-tag">📚 Company Act of Bangladesh &nbsp;|&nbsp; Overview</div>
        <div class="hero-title">{icon} {title}</div>
        <div class="hero-sub">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def sh(text):
    st.markdown(f'<div class="sec-head">{text}</div>', unsafe_allow_html=True)


def card(title, body):
    st.markdown(f'<div class="card"><div class="card-title">{title}</div><div class="card-body">{body}</div></div>', unsafe_allow_html=True)


def divider():
    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)


hero(
    "Company Act Syllabus Overview",
    "A complete roadmap for the Company Act section — module structure, key topics, and the practical focus for every company law professional.",
    "🧭",
)

st.markdown("<br>", unsafe_allow_html=True)

cols = st.columns(4)
for col, item in zip(cols, [
    ("12", "Total chapters"),
    ("13", "Modules + Quick Ref"),
    ("194", "Key sections highlighted"),
    ("✅", "Useful for law, audit, and company secretarial teams"),
]):
    col.markdown(f'<div class="metric-box"><div class="metric-num">{item[0]}</div><div class="metric-lbl">{item[1]}</div></div>', unsafe_allow_html=True)

divider()
sh("What this Company Act section covers")
st.markdown(
    "<div class='card-body'>This section gives you a full picture of company law in Bangladesh through 12 dedicated modules, plus a quick reference tool. It covers corporate formation, capital and securities, governance, compliance, audit, enforcement, winding up, and foreign company rules.</div>",
    unsafe_allow_html=True,
)

divider()
sh("Module Roadmap")

modules = [
    ("Module 1: Introduction", "Foundations of the Companies Act, 1994 — history, purpose, structure, and how to read the Act."),
    ("Module 2: Incorporation", "Formation of companies, Memorandum and Articles of Association, registration, certificate of incorporation, and company types."),
    ("Module 3: Share Capital", "Share capital structure, share types, transfers, transmissions, reduction of capital, debentures, and charge registration."),
    ("Module 4: Prospectus", "Public offerings, prospectus requirements, allotment rules, statements in lieu, issue at premium/discount, and liability for misstatements."),
    ("Module 5: Management", "Registered office, company name rules, statutory registers, annual returns, books of account, notice and filing obligations, and compliance timelines."),
    ("Module 6: Directors", "Director appointment, qualifications, duties, disclosures, loans, managing director powers, and director liability."),
    ("Module 7: Meetings", "Statutory meetings, AGMs, EGMs, board meetings, quorum and notice rules, voting, proxies, and minutes."),
    ("Module 8: Accounts & Audit", "Accounting obligations, financial statements, audit appointment and reports, auditor duties, dividend rules, and record retention."),
    ("Module 9: Investigation", "Registrar inspection powers, court investigations, inspectors’ authority, minority oppression remedies, and company oversight."),
    ("Module 10: Winding Up", "Modes of winding up, compulsory and voluntary liquidation, liquidators, creditor priority, and company dissolution."),
    ("Module 11: Foreign Companies", "Requirements for foreign companies in Bangladesh — registration, compliance, reporting, local operations, and closure."),
    ("Module 12: Offences", "Offences, penalties, officer liability, cognisance rules, compounding, limits on prosecution, and legal consequences."),
    ("Quick Reference", "A practical hub for section lookup, compliance checklists, comparison tables, glossary, and RJSC form guidance."),
]

for i in range(0, len(modules), 2):
    c1, c2 = st.columns(2)
    title1, body1 = modules[i]
    c1.markdown(f'<div class="card"><div class="card-title">{title1}</div><div class="card-body">{body1}</div></div>', unsafe_allow_html=True)
    if i + 1 < len(modules):
        title2, body2 = modules[i + 1]
        c2.markdown(f'<div class="card"><div class="card-title">{title2}</div><div class="card-body">{body2}</div></div>', unsafe_allow_html=True)

divider()
sh("How to use this section")
st.markdown(
    "<div class='card-body'>Use the overview as your study map. Start with the Introduction, then follow the sequence from Incorporation to Offences. Use the Quick Reference page to look up important sections, deadlines, and compliance checklists while you study or work.</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<ul style='padding-left:18px;line-height:1.7;font-size:0.95rem;color:#4a4a4a;'>"
    "<li><strong>Step 1:</strong> Read Module 1 to understand the Act’s structure and key definitions.</li>"
    "<li><strong>Step 2:</strong> Learn company formation and constitutional documents in Modules 2 and 3.</li>"
    "<li><strong>Step 3:</strong> Study governance, meetings and management in Modules 5, 6, and 7.</li>"
    "<li><strong>Step 4:</strong> Cover statutory accounts, audit and enforcement in Modules 8, 9 and 12.</li>"
    "<li><strong>Step 5:</strong> Review company closure and foreign company rules in Modules 10 and 11.</li>"
    "<li><strong>Step 6:</strong> Keep the Quick Reference page open as your working checklist.</li>"
    "</ul>",
    unsafe_allow_html=True,
)

divider()
sh("Key learning outcomes")
st.markdown(
    "<div class='card-body'>After completing this section, you should be able to: identify company formation requirements, distinguish between private and public company rules, explain director duties and meeting procedures, maintain statutory compliance, understand audits and financial reporting, recognise inspection and winding-up processes, and apply penalties and foreign company rules.</div>",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="ok-box">✅ Use this overview page as the first page for the Company Act section to get a full syllabus view before diving into each module.</div>',
    unsafe_allow_html=True,
)
