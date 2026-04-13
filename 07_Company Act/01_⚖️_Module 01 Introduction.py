import streamlit as st

# ── Shared CSS ────────────────────────────────────────────────────────
def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&family=Fira+Mono:wght@400;500&display=swap');
    .hero { background: linear-gradient(135deg,#1a3a5c,#0d2340); border-radius:14px; padding:40px 36px; margin-bottom:28px; }
    .hero-tag { font-family:'Fira Mono',monospace; font-size:11px; color:#c8922a; letter-spacing:3px; text-transform:uppercase; margin-bottom:10px; }
    .hero-title { font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:700; color:#fff; margin-bottom:12px; line-height:1.2; }
    .hero-sub { font-size:1rem; color:rgba(255,255,255,0.72); line-height:1.7; }
    .sec-head { font-family:'Playfair Display',serif; font-size:1.35rem; font-weight:600; color:#1a3a5c; border-left:4px solid #c8922a; padding-left:12px; margin:26px 0 14px 0; }
    .card { background:#fff; border-radius:10px; padding:20px 22px; margin-bottom:14px; border:1px solid #e8e0d0; box-shadow:0 2px 8px rgba(26,58,92,0.06); }
    .card-title { font-family:'Playfair Display',serif; font-size:1.05rem; font-weight:600; color:#1a3a5c; margin-bottom:7px; }
    .card-body { font-size:0.93rem; color:#4a4a4a; line-height:1.7; }
    .law-box { background:linear-gradient(135deg,#1a3a5c08,#c8922a10); border:1px solid #c8922a40; border-left:4px solid #c8922a; border-radius:8px; padding:14px 18px; margin:10px 0; font-family:'Fira Mono',monospace; font-size:0.86rem; color:#1a3a5c; }
    .tip-box { background:linear-gradient(135deg,#fff8ec,#fff3e0); border:1px solid #f0c060; border-radius:10px; padding:16px 20px; margin:14px 0; }
    .tip-title { font-family:'Playfair Display',serif; font-size:0.92rem; font-weight:700; color:#b07a10; margin-bottom:5px; }
    .tip-body { font-size:0.9rem; color:#5a4a20; line-height:1.6; }
    .warn-box { background:#fff5f5; border:1px solid #f0a0a0; border-left:4px solid #b33a3a; border-radius:8px; padding:14px 18px; margin:10px 0; font-size:0.9rem; color:#7a2020; line-height:1.6; }
    .ok-box { background:#f0faf4; border:1px solid #90d0a8; border-left:4px solid #2d7a4f; border-radius:8px; padding:14px 18px; margin:10px 0; font-size:0.9rem; color:#1a4a30; line-height:1.6; }
    .recap { background:linear-gradient(135deg,#1a3a5c,#0d2340); border-radius:12px; padding:26px 30px; margin:26px 0 8px 0; }
    .recap h4 { font-family:'Playfair Display',serif; font-size:1.15rem; color:#c8922a; margin-bottom:12px; }
    .recap ul { padding-left:18px; line-height:1.9; font-size:0.93rem; color:rgba(255,255,255,0.85); }
    .metric-box { background:#fff; border-radius:10px; padding:16px; text-align:center; border:1px solid #e8e0d0; }
    .metric-num { font-family:'Playfair Display',serif; font-size:1.9rem; font-weight:700; color:#1a3a5c; }
    .metric-lbl { font-size:0.78rem; color:#999; text-transform:uppercase; letter-spacing:1px; }
    .gold-line { border:none; height:2px; background:linear-gradient(to right,#c8922a,transparent); margin:22px 0; }
    table { width:100%; border-collapse:collapse; font-size:0.91rem; margin:10px 0; }
    th { background:#1a3a5c; color:#fff; padding:9px 13px; text-align:left; font-weight:600; }
    td { padding:8px 13px; border-bottom:1px solid #e8e0d0; vertical-align:top; }
    tr:nth-child(even) td { background:#f9f6f0; }
    </style>
    """, unsafe_allow_html=True)

def hero(mod, title, subtitle, icon="📘"):
    st.markdown(f"""
    <div class="hero">
        <div class="hero-tag">📚 Company Act of Bangladesh &nbsp;|&nbsp; Module {mod}</div>
        <div class="hero-title">{icon} {title}</div>
        <div class="hero-sub">{subtitle}</div>
    </div>""", unsafe_allow_html=True)

def sh(text): st.markdown(f'<div class="sec-head">{text}</div>', unsafe_allow_html=True)
def card(title, body): st.markdown(f'<div class="card"><div class="card-title">{title}</div><div class="card-body">{body}</div></div>', unsafe_allow_html=True)
def law(text): st.markdown(f'<div class="law-box">⚖️ &nbsp;{text}</div>', unsafe_allow_html=True)
def tip(title, body): st.markdown(f'<div class="tip-box"><div class="tip-title">💡 {title}</div><div class="tip-body">{body}</div></div>', unsafe_allow_html=True)
def warn(text): st.markdown(f'<div class="warn-box">⚠️ &nbsp;{text}</div>', unsafe_allow_html=True)
def ok(text): st.markdown(f'<div class="ok-box">✅ &nbsp;{text}</div>', unsafe_allow_html=True)
def divider(): st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
def metrics(items):
    cols = st.columns(len(items))
    for col,(num,lbl) in zip(cols,items):
        col.markdown(f'<div class="metric-box"><div class="metric-num">{num}</div><div class="metric-lbl">{lbl}</div></div>', unsafe_allow_html=True)
def recap(points):
    li = "".join(f"<li>{p}</li>" for p in points)
    st.markdown(f'<div class="recap"><h4>🔁 Quick Recap</h4><ul>{li}</ul></div>', unsafe_allow_html=True)

# ── PAGE ──────────────────────────────────────────────────────────────
apply_styles()
hero("1","Introduction & Background",
     "Understand the origins, purpose, and structure of the Companies Act, 1994 — the foundational law governing all companies in Bangladesh.","🏛️")

metrics([("1994","Year Enacted"),("11","Parts in Act"),("404","Total Sections"),("1913","Previous Act")])
st.markdown("<br>",unsafe_allow_html=True)

sh("Historical Background")
c1,c2=st.columns([3,2])
with c1:
    card("🕰️ Evolution of Company Law",
         "Company law in the subcontinent traces back to the <strong>British Companies Act 1844</strong>, leading to the <em>Joint Stock Companies Act 1850</em> — the first company law for the region, based on unlimited liability. In 1857, <strong>limited liability</strong> was introduced.<br><br>After Bangladesh's independence, the <strong>Companies Act 1913</strong> remained in force until replaced by the comprehensive <strong>Companies Act, 1994 (Act No. 18 of 1994)</strong>, which received Presidential assent on <strong>11 September 1994</strong>.")
with c2:
    card("📅 Key Milestones",
         "<strong>1844</strong> — British Companies Act<br><strong>1850</strong> — Joint Stock Companies Act<br><strong>1857</strong> — Limited Liability introduced<br><strong>1913</strong> — Companies Act for subcontinent<br><strong>1984</strong> — Last amendment to 1913 Act<br><strong>1994</strong> — Companies Act 1994 enacted<br><strong>1995</strong> — Came into force (SRO 177-law)")

divider()
sh("Objectives & Purpose of the Act")
law("Preamble: 'An Act to consolidate and amend the law relating to companies and certain other associations.' — Companies Act, 1994")

cols=st.columns(3)
objectives=[("🎯","Consolidation","To bring all provisions under a single modern law replacing the outdated 1913 Act."),
            ("🏢","Regulation","To provide a complete legal framework for formation, management, and dissolution of companies."),
            ("🛡️","Protection","To protect rights of shareholders, creditors, and the public dealing with companies."),
            ("📊","Transparency","To ensure proper maintenance of accounts, auditing, and financial disclosure."),
            ("⚖️","Accountability","To define duties and liabilities of directors, officers, and auditors.")]
for i,(icon,t,d) in enumerate(objectives):
    cols[i%3].markdown(f'<div class="card"><div class="card-title">{icon} {t}</div><div class="card-body">{d}</div></div>',unsafe_allow_html=True)

divider()
sh("Structure of the Act — 11 Parts")
st.markdown("""<table><tr><th>Part</th><th>Subject</th><th>Key Topics</th></tr>
<tr><td><strong>Part I</strong></td><td>Preliminary</td><td>Definitions, short title, commencement</td></tr>
<tr><td><strong>Part II</strong></td><td>Incorporation & Formation</td><td>MoA, AoA, registration, associations not for profit</td></tr>
<tr><td><strong>Part III</strong></td><td>Share Capital</td><td>Share capital rules, reduction, limited liability of directors</td></tr>
<tr><td><strong>Part IV</strong></td><td>Management & Administration</td><td>Registered office, meetings, directors, prospectus, auditors</td></tr>
<tr><td><strong>Part V</strong></td><td>Winding Up</td><td>Modes of winding up, liquidators, settlement of debts</td></tr>
<tr><td><strong>Part VI</strong></td><td>Companies Limited by Guarantee</td><td>Special provisions for guarantee companies</td></tr>
<tr><td><strong>Part VII</strong></td><td>Guarantee + Share Capital</td><td>Hybrid company provisions</td></tr>
<tr><td><strong>Part VIII</strong></td><td>Unlimited Companies</td><td>Re-registration, special provisions</td></tr>
<tr><td><strong>Part IX</strong></td><td>Unregistered Companies</td><td>Winding up of unregistered companies</td></tr>
<tr><td><strong>Part X</strong></td><td>Foreign Companies</td><td>Establishment, accounts, closure of foreign companies</td></tr>
<tr><td><strong>Part XI</strong></td><td>Supplemental</td><td>Legal proceedings, offences, penalties</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("Important Definitions (Section 2)")
tip("Why Definitions Matter","The definitions in Section 2 are the building blocks of the entire Act. Every term used throughout the Act draws its meaning from this section.")

definitions={
    "Company":"A company formed and registered under this Act or an existing company.",
    "Private Company":"A company which by its articles: (i) restricts right to transfer shares, (ii) prohibits public invitation to subscribe shares/debentures, (iii) limits members to 50 (excluding employees).",
    "Public Company":"A company incorporated under this Act (or any earlier law) that is NOT a private company.",
    "Director":"Includes any person occupying the position of director, by whatever name called.",
    "Officer":"Includes a director, managing agent, manager, secretary or any other officer of a company.",
    "Debenture":"Includes debenture stock, bonds and any other securities of a company, whether constituting a charge on assets or not.",
    "Share":"A share in the capital of a company, and includes stock except where a distinction is expressed or implied.",
    "Memorandum":"The memorandum of association as originally framed or as altered.",
    "Articles":"The articles of association of a company including regulations in Schedule I of the Act.",
    "Secretary":"Any individual with prescribed qualifications appointed to perform secretarial and administrative duties.",
    "Registrar":"The Registrar of Joint Stock Companies (RJSC) performing registration duties under the Act.",
    "Financial Year":"The period for which any profit & loss account of the company is made up and laid before AGM.",
    "Subsidiary":"A company in which another company controls the composition of its Board of Directors.",
    "The Court":"The court having jurisdiction under the Act (generally the High Court Division).",
}

search_term=st.text_input("🔍 Search definitions...",placeholder="Type a term e.g. 'private company'")
for term,defn in definitions.items():
    if not search_term or search_term.lower() in term.lower() or search_term.lower() in defn.lower():
        with st.expander(f"📌 {term}"):
            st.markdown(f'<div class="law-box">{defn}</div>',unsafe_allow_html=True)

divider()
sh("Types of Companies Under the Act")
cols=st.columns(2)
types=[("🏦","Company Limited by Shares","Liability of members limited to unpaid amount on shares. Most common type.","#e8f4fd"),
       ("🤝","Company Limited by Guarantee","Liability limited to amount members undertake to contribute on winding up. Common for clubs, NGOs.","#f0f8ee"),
       ("♾️","Unlimited Company","No limit on members' liability. Rare in practice.","#fdf4e8"),
       ("🔒","Private Limited Company","Max 50 members, no public share subscription, restricted transfers. Suffix: 'Ltd.'","#fdf0f0"),
       ("🌐","Public Limited Company","Unlimited members, can invite public to subscribe shares. Suffix: 'PLC' or 'Ltd.'","#f0f4fd"),
       ("🌍","Foreign Company","Company incorporated outside Bangladesh with a place of business in Bangladesh.","#f8f0fd")]
for i,(icon,name,desc,bg) in enumerate(types):
    cols[i%2].markdown(f'<div class="card" style="background:{bg};"><div class="card-title">{icon} {name}</div><div class="card-body">{desc}</div></div>',unsafe_allow_html=True)

divider()
sh("Quick Comparison: Private vs Public Company")
st.markdown("""<table><tr><th>Feature</th><th>Private Company</th><th>Public Company</th></tr>
<tr><td>Minimum Members</td><td>2</td><td>7</td></tr>
<tr><td>Maximum Members</td><td>50 (excl. employees)</td><td>Unlimited</td></tr>
<tr><td>Share Transfer</td><td>Restricted by Articles</td><td>Freely transferable</td></tr>
<tr><td>Public Invitation</td><td>Prohibited</td><td>Permitted</td></tr>
<tr><td>Prospectus</td><td>Not required</td><td>Required for public issue</td></tr>
<tr><td>Minimum Directors</td><td>2</td><td>3</td></tr>
<tr><td>Statutory Meeting</td><td>Not required</td><td>Required</td></tr>
<tr><td>Name Suffix</td><td>'Limited' or 'Ltd.'</td><td>'Public Limited' or 'PLC'</td></tr></table>""",unsafe_allow_html=True)
warn("A private company that contravenes any of the three conditions loses its status as a private company and becomes a public company.")

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. In which year did the Companies Act, 1994 actually come into force?",["1993","1994","1995","1996"],index=None,key="m1q1")
if q1=="1995": ok("Correct! The Act was enacted in 1994 but came into force in 1995 via Notification SRO 177-law dated 1-10-95.")
elif q1: warn("Not quite. The Act received Presidential assent in 1994 but came into force in 1995.")

q2=st.radio("2. What is the maximum number of members allowed in a Private Company?",["20","50","100","Unlimited"],index=None,key="m1q2")
if q2=="50": ok("Correct! A private company limits its members to 50, excluding persons in the company's employment.")
elif q2: warn("Incorrect. Section 2(q) limits private company membership to 50 (excluding employees).")

q3=st.radio("3. Which part of the Companies Act 1994 deals with Winding Up?",["Part III","Part IV","Part V","Part VI"],index=None,key="m1q3")
if q3=="Part V": ok("Correct! Part V of the Companies Act, 1994 covers winding up of companies.")
elif q3: warn("Incorrect. Winding Up is covered under Part V.")

recap(["Companies Act, 1994 (Act No. 18 of 1994) replaced the old Companies Act 1913",
       "The Act received Presidential assent on 11 September 1994 and came into force in 1995",
       "The Act has 11 Parts and 404 Sections covering all aspects of company law",
       "Key company types: Private Limited, Public Limited, Limited by Guarantee, Unlimited, Foreign",
       "A Private Company restricts transfers, prohibits public subscription, and limits members to 50",
       "All key terms are defined under Section 2 — the starting point for interpreting the Act"])
