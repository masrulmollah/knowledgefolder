import streamlit as st
CSS="""<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&family=Fira+Mono:wght@400;500&display=swap');
.hero{background:linear-gradient(135deg,#1a3a5c,#0d2340);border-radius:14px;padding:40px 36px;margin-bottom:28px;}
.hero-tag{font-family:'Fira Mono',monospace;font-size:11px;color:#c8922a;letter-spacing:3px;text-transform:uppercase;margin-bottom:10px;}
.hero-title{font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:700;color:#fff;margin-bottom:12px;line-height:1.2;}
.hero-sub{font-size:1rem;color:rgba(255,255,255,0.72);line-height:1.7;}
.sec-head{font-family:'Playfair Display',serif;font-size:1.35rem;font-weight:600;color:#1a3a5c;border-left:4px solid #c8922a;padding-left:12px;margin:26px 0 14px 0;}
.card{background:#fff;border-radius:10px;padding:20px 22px;margin-bottom:14px;border:1px solid #e8e0d0;box-shadow:0 2px 8px rgba(26,58,92,0.06);}
.card-title{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:600;color:#1a3a5c;margin-bottom:7px;}
.card-body{font-size:0.93rem;color:#4a4a4a;line-height:1.7;}
.law-box{background:linear-gradient(135deg,#1a3a5c08,#c8922a10);border:1px solid #c8922a40;border-left:4px solid #c8922a;border-radius:8px;padding:14px 18px;margin:10px 0;font-family:'Fira Mono',monospace;font-size:0.86rem;color:#1a3a5c;}
.tip-box{background:linear-gradient(135deg,#fff8ec,#fff3e0);border:1px solid #f0c060;border-radius:10px;padding:16px 20px;margin:14px 0;}
.tip-title{font-family:'Playfair Display',serif;font-size:0.92rem;font-weight:700;color:#b07a10;margin-bottom:5px;}
.tip-body{font-size:0.9rem;color:#5a4a20;line-height:1.6;}
.warn-box{background:#fff5f5;border:1px solid #f0a0a0;border-left:4px solid #b33a3a;border-radius:8px;padding:14px 18px;margin:10px 0;font-size:0.9rem;color:#7a2020;line-height:1.6;}
.ok-box{background:#f0faf4;border:1px solid #90d0a8;border-left:4px solid #2d7a4f;border-radius:8px;padding:14px 18px;margin:10px 0;font-size:0.9rem;color:#1a4a30;line-height:1.6;}
.recap{background:linear-gradient(135deg,#1a3a5c,#0d2340);border-radius:12px;padding:26px 30px;margin:26px 0 8px 0;}
.recap h4{font-family:'Playfair Display',serif;font-size:1.15rem;color:#c8922a;margin-bottom:12px;}
.recap ul{padding-left:18px;line-height:1.9;font-size:0.93rem;color:rgba(255,255,255,0.85);}
.metric-box{background:#fff;border-radius:10px;padding:16px;text-align:center;border:1px solid #e8e0d0;}
.metric-num{font-family:'Playfair Display',serif;font-size:1.9rem;font-weight:700;color:#1a3a5c;}
.metric-lbl{font-size:0.78rem;color:#999;text-transform:uppercase;letter-spacing:1px;}
.gold-line{border:none;height:2px;background:linear-gradient(to right,#c8922a,transparent);margin:22px 0;}
table{width:100%;border-collapse:collapse;font-size:0.91rem;margin:10px 0;}
th{background:#1a3a5c;color:#fff;padding:9px 13px;text-align:left;font-weight:600;}
td{padding:8px 13px;border-bottom:1px solid #e8e0d0;vertical-align:top;}
tr:nth-child(even) td{background:#f9f6f0;}
</style>"""
st.markdown(CSS,unsafe_allow_html=True)
def hero(mod,title,subtitle,icon="📘"):
    st.markdown(f'<div class="hero"><div class="hero-tag">📚 Company Act of Bangladesh &nbsp;|&nbsp; Module {mod}</div><div class="hero-title">{icon} {title}</div><div class="hero-sub">{subtitle}</div></div>',unsafe_allow_html=True)
def sh(t): st.markdown(f'<div class="sec-head">{t}</div>',unsafe_allow_html=True)
def card(title,body): st.markdown(f'<div class="card"><div class="card-title">{title}</div><div class="card-body">{body}</div></div>',unsafe_allow_html=True)
def law(t): st.markdown(f'<div class="law-box">⚖️ &nbsp;{t}</div>',unsafe_allow_html=True)
def tip(title,body): st.markdown(f'<div class="tip-box"><div class="tip-title">💡 {title}</div><div class="tip-body">{body}</div></div>',unsafe_allow_html=True)
def warn(t): st.markdown(f'<div class="warn-box">⚠️ &nbsp;{t}</div>',unsafe_allow_html=True)
def ok(t): st.markdown(f'<div class="ok-box">✅ &nbsp;{t}</div>',unsafe_allow_html=True)
def divider(): st.markdown('<hr class="gold-line">',unsafe_allow_html=True)
def metrics(items):
    cols=st.columns(len(items))
    for col,(num,lbl) in zip(cols,items):
        col.markdown(f'<div class="metric-box"><div class="metric-num">{num}</div><div class="metric-lbl">{lbl}</div></div>',unsafe_allow_html=True)
def recap(points):
    li="".join(f"<li>{p}</li>" for p in points)
    st.markdown(f'<div class="recap"><h4>🔁 Quick Recap</h4><ul>{li}</ul></div>',unsafe_allow_html=True)

hero("SR","Quick Reference & Professional Tools","Your all-in-one reference hub — key sections at a glance, compliance checklists, comparison tables, glossary, and RJSC forms guide.","🛠️")
st.markdown("<br>",unsafe_allow_html=True)

tabs=st.tabs(["📋 Key Sections","📅 Compliance Calendar","⚖️ Pvt vs Public","📝 Glossary","🗂️ RJSC Forms","🔗 Related Laws"])

with tabs[0]:
    sh("Important Sections — Quick Reference")
    tip("How to Use","Use this table for quick look-up during exams, professional work, or compliance review. ⭐ marks the most frequently tested sections.")
    sections=[("2","⭐","Definitions — all key terms used in the Act"),
              ("13-16","","Alteration of Memorandum of Association"),
              ("27","⭐","Certificate of Incorporation — conclusive evidence"),
              ("28","","Companies not for profit — licence to omit 'Limited'"),
              ("59","⭐","Reduction of Share Capital — Special Resolution + Court"),
              ("77","⭐","Registered Office — 28 days to establish and notify changes"),
              ("83","","Statutory Meeting — public companies, 1–6 months from commencement"),
              ("85","⭐","Annual General Meeting — 6 months from year end, 21 days notice"),
              ("86","⭐","Extraordinary General Meeting — 10% shareholders can requisition"),
              ("92","⭐","Minutes of Meetings — 30 days to enter, signed by Chairman"),
              ("95","⭐","Board Meetings — 4 times per year minimum"),
              ("99","⭐","Undischarged insolvent cannot be director"),
              ("103","⭐","Director must declare interest in contracts"),
              ("103A","⭐","Loans to directors — generally prohibited"),
              ("107","⭐","Registration of Charges — 21 days"),
              ("148","","Prospectus — registration with RJSC required"),
              ("151","⭐","Minimum Subscription — must be received before allotment"),
              ("181","⭐","Books of Account — must be kept, 8-year retention"),
              ("183","⭐","Balance Sheet and P&L to be laid before AGM"),
              ("184","⭐","Directors' Report — mandatory contents"),
              ("190","⭐","Annual Return — 21 days after AGM"),
              ("196","","Registrar's power to inspect books"),
              ("200","","Court investigation — 200+ members can apply"),
              ("210","⭐","Appointment of Auditors"),
              ("212","⭐","Auditor must be Chartered Accountant (ICAB)"),
              ("213","⭐","Disqualifications for auditors"),
              ("233","⭐","Minority shareholder protection — oppression remedy"),
              ("241","⭐","Grounds for compulsory winding up"),
              ("243","⭐","Unable to pay debts — deemed insolvency"),
              ("378","⭐","Foreign companies — registration within 30 days"),
              ("396","⭐","Cognisance of offences — Registrar/Government sanction required")]
    search=st.text_input("🔍 Search sections...",placeholder="e.g. 'dividend' or '181'",key="sr_search")
    st.markdown("<table><tr><th>Section(s)</th><th>★</th><th>Subject</th></tr>" + "".join(f"<tr><td><strong>{s}</strong></td><td>{star}</td><td>{sub}</td></tr>" for s,star,sub in sections if not search or search.lower() in s.lower() or search.lower() in sub.lower()) + "</table>",unsafe_allow_html=True)

with tabs[1]:
    sh("Annual Compliance Calendar for Companies")
    tip("Usage","Use this as a monthly compliance tracker. Finance/accounts teams should review this at the start of each month.")
    for col,(deadline,colour,action) in zip([None]*20,[
        ("Ongoing","🟢","Maintain all statutory registers (Members, Directors, Charges, etc.)"),
        ("Ongoing","🟢","Maintain proper books of account"),
        ("Within 28 days of incorporation","🔵","Establish registered office; file Form VI with RJSC"),
        ("Within 1 month of incorporation","🔵","Appoint first auditors (Board decision)"),
        ("Within 18 months of incorporation","🔵","File FIRST Annual Return with RJSC"),
        ("Within 21 days of charge creation","🟡","Register every charge with RJSC (Form XVIII/XIX)"),
        ("Within 28 days of any change","🟡","Notify RJSC of change in directors, registered office, etc."),
        ("Within 6 months of financial year end","🔴","Hold Annual General Meeting (AGM)"),
        ("Within 21 days of AGM","🔴","File Annual Return with RJSC"),
        ("Within 42 days of dividend declaration","🟡","Pay declared dividend to shareholders"),
        ("Within 30 days of AGM/Board Meeting","🟡","Enter minutes in Minutes Book"),
        ("Quarterly (4 times per year)","🔵","Hold Board Meetings"),
        ("At least 21 days before AGM","🔴","Send AGM notice + Annual Report to all members"),
        ("Before publication","🔵","Register prospectus with RJSC (if public offer)"),
        ("Within 90 days of Court Order","🟡","File confirmed capital reduction order with RJSC")]):
        st.markdown(f'<div class="card" style="padding:10px 16px;margin-bottom:6px;display:flex;gap:14px;"><div style="min-width:240px;color:#1a3a5c;font-weight:600;font-size:0.83rem;">{colour} {deadline}</div><div class="card-body" style="font-size:0.9rem;">{action}</div></div>',unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.8rem;color:#888;margin-top:8px;'>🟢 Ongoing &nbsp;|&nbsp; 🔵 One-time events &nbsp;|&nbsp; 🟡 Event-triggered &nbsp;|&nbsp; 🔴 Annual recurring</div>",unsafe_allow_html=True)

with tabs[2]:
    sh("Private Company vs Public Company — Comprehensive Comparison")
    st.markdown("""<table><tr><th>Aspect</th><th>Private Company</th><th>Public Company</th></tr>
<tr><td>Minimum Members</td><td>2</td><td>7</td></tr>
<tr><td>Maximum Members</td><td>50 (excl. employees)</td><td>Unlimited</td></tr>
<tr><td>Minimum Directors</td><td>2</td><td>3</td></tr>
<tr><td>Share Transfer</td><td>Restricted by AoA</td><td>Freely transferable</td></tr>
<tr><td>Public Subscription</td><td>Prohibited</td><td>Permitted</td></tr>
<tr><td>Prospectus</td><td>Not required</td><td>Required for public issue</td></tr>
<tr><td>Statutory Meeting</td><td>Not required</td><td>Required (1–6 months after commencement)</td></tr>
<tr><td>AGM Notice Period</td><td>21 days</td><td>21 days</td></tr>
<tr><td>Quorum at General Meeting</td><td>2 members</td><td>5 members</td></tr>
<tr><td>BSEC Regulations</td><td>Generally not applicable</td><td>Listed companies fully regulated by BSEC</td></tr>
<tr><td>Listing on Stock Exchange</td><td>Cannot list shares</td><td>Can list on DSE/CSE</td></tr>
<tr><td>Regulatory Burden</td><td>Lower</td><td>Higher (especially if listed)</td></tr>
<tr><td>Name Suffix</td><td>'Limited' or 'Ltd.'</td><td>'Public Limited' or 'PLC'</td></tr></table>""",unsafe_allow_html=True)

with tabs[3]:
    sh("Glossary of Key Terms")
    glossary={"AGM":"Annual General Meeting — the yearly meeting of shareholders to adopt accounts, declare dividend, appoint directors and auditors.",
              "AoA":"Articles of Association — internal rulebook governing company management.",
              "Authorised Capital":"Maximum share capital a company is permitted to issue under its MoA.",
              "Contributory":"A person liable to contribute to the assets of a company in the event of winding up.",
              "Debenture":"Instrument of debt — includes bonds, debenture stock, and other securities (secured or unsecured).",
              "Declaration of Solvency":"Statutory declaration by directors in Members' Voluntary Winding Up that the company can pay all debts within 12 months.",
              "EGM":"Extraordinary General Meeting — any general meeting other than the AGM.",
              "Fixed Charge":"Charge attached to a specific identified asset; company cannot freely deal with that asset.",
              "Floating Charge":"Charge over a class of changing assets; crystallises on default or winding up.",
              "Fraudulent Preference":"Payment to a specific creditor within 6 months before winding up to prefer them over others — voidable by Court.",
              "Liquidator":"Person appointed to wind up a company's affairs — realise assets, pay debts, distribute surplus.",
              "MoA":"Memorandum of Association — the supreme/constitutional document of a company.",
              "Officer in Default":"Officer who knowingly permitted or authorised a statutory default; liable for penalties.",
              "Ordinary Resolution":"Resolution passed by simple majority (>50%) of votes cast.",
              "Paid-up Capital":"The portion of subscribed capital that shareholders have actually paid to the company.",
              "Perpetual Succession":"A company continues to exist regardless of changes in its membership.",
              "Proxy":"Person authorised by a member to attend and vote at a meeting on their behalf.",
              "RJSC":"Registrar of Joint Stock Companies and Firms — the regulatory body for company registration in Bangladesh.",
              "Separate Legal Entity":"The principle that a company is a legal person distinct from its shareholders.",
              "Special Resolution":"Resolution passed by at least 75% majority of votes cast.",
              "Share Premium":"Amount received over the face/nominal value of shares — must be credited to Share Premium Account.",
              "Statutory Audit":"Mandatory annual audit of company accounts by a qualified Chartered Accountant (ICAB member).",
              "Transfer (Shares)":"Voluntary act of passing ownership of shares from one person to another.",
              "Transmission (Shares)":"Transfer of shares by operation of law (death, insolvency) — not by voluntary act.",
              "Ultra Vires":"Acts beyond the company's objects as stated in the MoA — legally void.",
              "Winding Up":"The process of bringing a company's existence to an end by realising assets and paying liabilities."}
    search_g=st.text_input("🔍 Search glossary...",placeholder="Type a term...",key="gloss_search")
    for term,defn in sorted(glossary.items()):
        if not search_g or search_g.lower() in term.lower() or search_g.lower() in defn.lower():
            with st.expander(f"📌 {term}"):
                st.markdown(f'<div class="law-box">{defn}</div>',unsafe_allow_html=True)

with tabs[4]:
    sh("Key RJSC Forms and Their Purposes")
    forms=[("Form I","Declaration of compliance with requirements of the Act on application for registration"),
           ("Form VI","Notice of situation of registered office / change of registered office"),
           ("Form IX","Consent of director to act — signed by each proposed director"),
           ("Form X","List of persons who have consented to act as first directors"),
           ("Form XII","Particulars of directors, managers, managing agents, secretaries"),
           ("Form XIII","Return of allotments (shares allotted)"),
           ("Form XVIII","Particulars of a charge / mortgage created by a company"),
           ("Form XIX","Particulars of a charge subject to which property acquired"),
           ("Form XXIV","Satisfaction of a charge — memorandum of satisfaction"),
           ("Form XXX","Annual Return for companies having share capital"),
           ("Form XXXIV","Statement to be filed by a foreign company"),
           ("Form XLVII","Declaration of solvency (Members' Voluntary Winding Up)")]
    st.markdown("<table><tr><th>Form No.</th><th>Purpose</th></tr>" + "".join(f"<tr><td><strong>{f}</strong></td><td>{p}</td></tr>" for f,p in forms) + "</table>",unsafe_allow_html=True)
    tip("Pro Tip","Keep a master register of all RJSC forms filed by your company — with filing dates and acknowledgement receipts. This is invaluable during audits, regulatory inspections, or due diligence.")

with tabs[5]:
    sh("Related Laws & Regulations")
    for icon,name,desc in [("📜","Bangladesh Securities and Exchange Commission Act, 1993","Regulates securities market; listed companies must comply with BSEC rules in addition to Companies Act."),
                           ("📊","BSEC Corporate Governance Code","Mandatory corporate governance requirements for listed companies — independent directors, audit committee, etc."),
                           ("💰","Income Tax Ordinance, 1984","Tax obligations of companies — corporate tax, withholding tax, advance tax, minimum tax."),
                           ("🏦","Bank Company Act, 1991","Special provisions for banking companies — capital adequacy, provisioning, governance."),
                           ("📈","Financial Institutions Act, 1993","Governs non-banking financial institutions (NBFIs, leasing companies)."),
                           ("🤝","Contract Act, 1872","Foundation of all contracts — applicable to all company contracts."),
                           ("📑","Stamp Act, 1899","Stamp duty on company documents — share transfer forms, debenture trust deeds, etc."),
                           ("📊","Financial Reporting Act, 2015","Establishes Financial Reporting Council (FRC) — oversight of auditing and accounting standards in Bangladesh.")]:
        st.markdown(f'<div class="card" style="margin-bottom:10px;"><div class="card-title">{icon} {name}</div><div class="card-body">{desc}</div></div>',unsafe_allow_html=True)

divider()
recap(["This supplementary module is your daily go-to reference — bookmark it!",
       "Key sections to memorise: 2, 27, 59, 77, 85, 92, 103, 107, 151, 181, 183, 190, 210, 233, 241, 378, 396",
       "Compliance calendar helps prevent penalties — set calendar reminders for recurring deadlines",
       "RJSC forms should be filed promptly — delays attract per-day fines",
       "Always cross-reference with BSEC Corporate Governance Code for listed companies",
       "The Financial Reporting Act, 2015 adds FRC oversight on top of Companies Act audit requirements"])