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

hero("5","Management & Administration","Learn the operational and administrative requirements every company must comply with — registered office, statutory registers, annual returns, and document management.","🏢")
metrics([("Part IV","Act Coverage"),("28 days","Change of Office Notice"),("18 months","First Annual Return"),("21 days","Post-AGM Filing")])
st.markdown("<br>",unsafe_allow_html=True)

sh("Registered Office Requirements — Section 77")
law("Section 77 — A company shall at all times have a registered office within Bangladesh to which all communications and notices may be addressed.")
c1,c2=st.columns(2)
with c1: card("🏠 Requirements","✔ Must be established within <strong>28 days</strong> of incorporation<br>✔ Must be in Bangladesh<br>✔ Address must be registered with RJSC (Form VI)<br>✔ Changes must be notified to RJSC within <strong>28 days</strong><br>✔ All official communications go here")
with c2: card("📋 Documents Kept at Registered Office","• Register of Members<br>• Register of Directors<br>• Register of Charges<br>• Minutes of General Meetings<br>• Copies of MoA and AoA<br>• Annual Returns<br>• Books of Account")

divider()
sh("Company Name Rules")
name_rules=[("✅","Must end with","'Limited' for private companies; 'PLC' or 'Public Limited Company' for public companies"),
            ("🚫","Cannot use","Names identical or too similar to an existing registered company"),
            ("🚫","Prohibited words","'Bank', 'Insurance', 'Trust', 'Royal', 'Government' require special permission"),
            ("📋","Display requirement","Company name must be displayed outside every office and on all business correspondence"),
            ("🔄","Change of name","Permitted by Special Resolution + approval of Registrar"),
            ("⚠️","Misleading names","Registrar can direct a company to change its name if misleading")]
for icon,label,rule in name_rules:
    st.markdown(f'<div class="card" style="padding:10px 16px;margin-bottom:8px;"><strong style="color:#1a3a5c;">{icon} {label}:</strong> <span style="font-size:0.92rem;color:#4a4a4a;"> {rule}</span></div>',unsafe_allow_html=True)

divider()
sh("Statutory Registers & Books to be Maintained")
tip("Why Statutory Registers Matter","These are legal obligations — failure to maintain them properly attracts penalties. Finance and accounts professionals are often responsible for ensuring these are up to date.")
registers=[("📋","Register of Members","Names, addresses, shareholding details of all members. Must be updated within 2 months of any change.","Section 36"),
           ("👥","Register of Directors","Names, addresses, nationalities, other directorships of all directors.","Section 109"),
           ("⚡","Register of Charges","Details of all charges/mortgages created by the company on its assets.","Section 107"),
           ("📊","Minutes Books","Minutes of all General Meetings and Board Meetings, signed by Chairman.","Section 92"),
           ("📁","Books of Account","Cash book, sales book, purchase book, ledger, stock records.","Section 181"),
           ("📜","Register of Contracts","Contracts in which directors have personal interest.","Section 103")]
cols=st.columns(2)
for i,(icon,name,desc,sec) in enumerate(registers):
    cols[i%2].markdown(f'<div class="card" style="margin-bottom:10px;"><div class="card-title">{icon} {name} <span style="background:#c8922a20;color:#8a6010;font-family:monospace;font-size:0.75rem;padding:2px 8px;border-radius:10px;">{sec}</span></div><div class="card-body">{desc}</div></div>',unsafe_allow_html=True)

divider()
sh("Annual Return — Section 190")
law("Section 190 — Every company must file an Annual Return with the Registrar. First Annual Return within 18 months of incorporation; thereafter within 21 days of each AGM.")
c1,c2=st.columns(2)
with c1: card("📅 Filing Timeline","<strong>First Annual Return:</strong> Within 18 months of incorporation<br><br><strong>Subsequent Returns:</strong> Within 21 days after each AGM<br><br><strong>Filed with:</strong> RJSC<br><br><strong>Signed by:</strong> Director and Secretary")
with c2: card("📋 Contents of Annual Return","✔ Registered office address<br>✔ Summary of share capital and debentures<br>✔ List of members (names, addresses, shares held)<br>✔ Transfers of shares during the year<br>✔ Particulars of directors, managers, secretaries<br>✔ Copy of latest audited financial statements")
warn("Failure to file the Annual Return on time attracts a penalty of Tk. 500 per day for every day of default. Directors and the company are jointly and severally liable.")

divider()
sh("Books of Account — Section 181")
law("Section 181 — Every company shall keep at its registered office proper books of account giving a true and fair view of the state of affairs and explaining its transactions.")
st.markdown("""<table><tr><th>Book/Record</th><th>Contents</th><th>Retention Period</th></tr>
<tr><td>Cash Book</td><td>All cash receipts and payments</td><td>Minimum 8 years</td></tr>
<tr><td>Sales/Revenue Records</td><td>All sales and services rendered</td><td>Minimum 8 years</td></tr>
<tr><td>Purchase Records</td><td>All goods and services purchased</td><td>Minimum 8 years</td></tr>
<tr><td>General Ledger</td><td>All account balances</td><td>Minimum 8 years</td></tr>
<tr><td>Stock Records</td><td>Inventory at beginning/end of financial year</td><td>Minimum 8 years</td></tr>
<tr><td>Minutes Books</td><td>Minutes of all meetings</td><td>Permanently</td></tr>
<tr><td>Statutory Registers</td><td>Members, Directors, Charges etc.</td><td>Permanently</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("🗓️ Annual Compliance Calendar — Key Deadlines")
calendar=[("Within 28 days of incorporation","Establish registered office and notify RJSC"),
          ("Within 1 month of incorporation","Appoint first auditors (Board decision)"),
          ("Within 18 months of incorporation","File FIRST Annual Return with RJSC"),
          ("Within 21 days of charge creation","Register every charge with RJSC"),
          ("Within 28 days of any change","Notify RJSC of change in directors, registered office, etc."),
          ("Within 6 months of financial year end","Hold Annual General Meeting (AGM)"),
          ("Within 21 days of AGM","File Annual Return with RJSC"),
          ("Within 42 days of dividend declaration","Pay declared dividend to shareholders"),
          ("Within 30 days of meeting","Enter minutes in Minutes Book")]
for deadline,action in calendar:
    st.markdown(f'<div class="card" style="padding:10px 16px;margin-bottom:6px;display:flex;gap:16px;"><div style="min-width:260px;color:#c8922a;font-weight:600;font-size:0.85rem;">⏰ {deadline}</div><div class="card-body" style="font-size:0.9rem;">{action}</div></div>',unsafe_allow_html=True)

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. Within how many days must a change in registered office be notified to the Registrar?",["14 days","21 days","28 days","30 days"],index=None,key="m5q1")
if q1=="28 days": ok("Correct! Under Section 77, any change in registered office must be communicated to the RJSC within 28 days.")
elif q1: warn("Incorrect. The deadline for notifying change in registered office is 28 days.")

q2=st.radio("2. The Annual Return must be filed within how many days after the AGM?",["14 days","21 days","28 days","42 days"],index=None,key="m5q2")
if q2=="21 days": ok("Correct! Section 190 requires the Annual Return to be filed with RJSC within 21 days of the Annual General Meeting.")
elif q2: warn("Incorrect. The Annual Return must be filed within 21 days after the AGM (Section 190).")

q3=st.radio("3. Books of account must be retained for at least how many years?",["5 years","6 years","8 years","10 years"],index=None,key="m5q3")
if q3=="8 years": ok("Correct! Books of account must be maintained for a minimum of 8 years from the end of the relevant financial year.")
elif q3: warn("Incorrect. The minimum retention period for books of account is 8 years.")

recap(["Registered office must be established within 28 days — all official documents go here",
       "Statutory registers must be maintained — failure attracts penalties",
       "Annual Return must be filed with RJSC within 21 days of each AGM",
       "First Annual Return is due within 18 months of incorporation",
       "Books of account must be kept for at least 8 years; statutory registers permanently",
       "Company name + registration details must appear on all business correspondence",
       "Penalty for late Annual Return filing: Tk. 500 per day"])