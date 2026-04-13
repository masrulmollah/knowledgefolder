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

hero("7","Meetings & Resolutions","Understand the types of company meetings, notice requirements, quorum rules, voting procedures, and the different categories of resolutions under the Act.","🗳️")
metrics([("21 days","AGM Notice Period"),("6 months","AGM Deadline"),("14 days","EGM Notice Period"),("75%","Special Resolution")])
st.markdown("<br>",unsafe_allow_html=True)

sh("Types of Company Meetings")
meetings=[("🏛️","Statutory Meeting","Public companies only. Held once — between 1 and 6 months from the date of commencement of business. Directors must send a Statutory Report to all members at least 21 days before.","Section 83"),
          ("📅","Annual General Meeting (AGM)","Every company must hold an AGM each calendar year. First AGM within 18 months of incorporation; subsequent AGMs within 6 months of financial year end. Not more than 15 months between two AGMs.","Section 85"),
          ("⚡","Extraordinary General Meeting (EGM)","Any general meeting other than the AGM. Called by directors on their own motion, or requisitioned by shareholders holding ≥1/10 of paid-up voting capital.","Section 86"),
          ("🏢","Board Meeting","Must be held at least 4 times a year (once every 3 months). Quorum: one-third of total directors or 2 directors, whichever is higher.","Section 95")]
for icon,name,desc,sec in meetings:
    with st.expander(f"{icon} {name}  〈{sec}〉"):
        st.markdown(f'<div class="law-box">{desc}</div>',unsafe_allow_html=True)

divider()
sh("Annual General Meeting (AGM) — Key Rules")
c1,c2=st.columns(2)
with c1: card("📋 Notice Requirements","✔ Minimum <strong>21 days' written notice</strong> to all members<br>✔ Short notice permitted if <strong>95% of members</strong> consent<br>✔ Notice must state: date, time, place, and agenda<br>✔ Notice must accompany Annual Report and Financial Statements<br>✔ Notice must be sent to all directors, auditors, and members")
with c2: card("👥 Quorum Requirements","<strong>Private Company:</strong> 2 members personally present<br><strong>Public Company:</strong> 5 members personally present<br><br>If quorum is not present within <strong>30 minutes</strong> of scheduled time:<br>• If called by requisition → meeting is dissolved<br>• Otherwise → adjourned to same day next week, same time and place<br>• At adjourned meeting → members present form quorum")

st.markdown("""<table><tr><th>Business at AGM</th><th>Ordinary Business</th><th>Special Business</th></tr>
<tr><td>Definition</td><td>Standard agenda items at every AGM</td><td>Any business other than ordinary</td></tr>
<tr><td>Examples</td><td>Adoption of accounts, declaration of dividend, appointment of directors, appointment of auditors</td><td>Alteration of AoA, reduction of capital, issue of new shares, approval of major transactions</td></tr>
<tr><td>Resolution Type</td><td>Usually Ordinary Resolution</td><td>Usually Special Resolution</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("Types of Resolutions")
tip("Why Resolution Types Matter","The type of resolution required determines the majority needed. Always check whether a matter requires an ordinary or special resolution before proceeding.")
res_types=[("📗","Ordinary Resolution","Passed by a simple majority (more than 50%) of votes cast by members present and voting.","Appointment of directors, declaration of dividend, adoption of accounts, appointment of auditors"),
           ("📘","Special Resolution","Passed by at least 75% (three-fourths) of votes cast. 21 days' notice required specifying the intent.","Alteration of MoA/AoA, change of company name, reduction of capital, voluntary winding up"),
           ("📙","Resolution Requiring Special Notice","Requires 28 days' notice to the company. Company must give 21 days' notice to members.","Removal of a director before expiry of tenure; appointment of auditor other than retiring auditor")]
for icon,name,desc,examples in res_types:
    c1,c2=st.columns([2,3])
    with c1: st.markdown(f'<div class="card"><div class="card-title">{icon} {name}</div><div class="card-body">{desc}</div></div>',unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="card" style="background:#f9f6f0;"><div class="card-title" style="font-size:0.88rem;color:#888;">📋 Used For</div><div class="card-body">{examples}</div></div>',unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

divider()
sh("Voting & Proxies")
c1,c2=st.columns(2)
with c1: card("🗳️ Methods of Voting","<strong>1. Show of Hands (default):</strong> Each member present has ONE vote regardless of shares held<br><br><strong>2. Poll (on demand):</strong> Each share carries proportionate votes. Demanded by:<br>• Chairman, OR<br>• At least 5 members present in person, OR<br>• Members holding ≥1/10 of total voting rights<br><br><strong>Poll result overrides</strong> the show of hands result.")
with c2: card("📝 Proxies","A <strong>proxy</strong> is a person authorised to attend and vote at a meeting on behalf of a member who cannot attend in person.<br><br>✔ Must be appointed in writing (proxy form)<br>✔ Proxy form deposited at company ≥48 hours before meeting<br>✔ Every member has right to appoint proxy<br>✔ A company can be a proxy for another company (corporate representative)")

divider()
sh("Minutes of Meetings — Section 92")
law("Section 92 — Every company shall cause minutes of all proceedings of General Meetings and Board Meetings to be entered within 30 days in books kept for that purpose. Minutes signed by the Chairman shall be evidence of the proceedings.")
ok("Minutes signed by the Chairman are prima facie evidence of the proceedings. They are presumed correct unless proved otherwise.")
for rule in ["Must be recorded within 30 days of the meeting",
             "Minutes book must be kept at the registered office",
             "Must be signed by the Chairman of the same meeting or the next meeting",
             "Members may inspect General Meeting minutes during business hours",
             "Minutes cannot be altered after they are signed — only corrections with Chairman's initials permitted"]:
    st.markdown(f'<div class="ok-box" style="margin-bottom:6px;padding:9px 14px;">📋 {rule}</div>',unsafe_allow_html=True)

divider()
sh("EGM by Shareholder Requisition")
card("⚡ When Can Shareholders Demand an EGM?","Members holding <strong>not less than 1/10th of paid-up voting capital</strong> can requisition the directors to call an EGM by depositing a signed requisition at the registered office.<br><br><strong>Timeline:</strong><br>✔ Directors must call the meeting within <strong>21 days</strong> of receiving the requisition<br>✔ Meeting must be held within <strong>45 days</strong> of the requisition<br>✔ If directors fail → the requisitionists themselves may call it within 3 months<br>✔ Reasonable expenses incurred by requisitionists must be repaid by the company")

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. What is the minimum notice period for an Annual General Meeting?",["7 days","14 days","21 days","28 days"],index=None,key="m7q1")
if q1=="21 days": ok("Correct! Under Section 85, an AGM requires at least 21 days' written notice to all members.")
elif q1: warn("Incorrect. The minimum notice period for an AGM is 21 days.")

q2=st.radio("2. A Special Resolution requires what majority of votes cast?",["Simple majority (>50%)","Two-thirds majority (>66%)","Three-fourths majority (≥75%)","Unanimous consent"],index=None,key="m7q2")
if q2=="Three-fourths majority (≥75%)": ok("Correct! A Special Resolution requires at least 75% (three-fourths) majority of votes cast.")
elif q2: warn("Incorrect. A Special Resolution requires a three-fourths (75%) majority.")

q3=st.radio("3. If a quorum is not present at an AGM within 30 minutes (not called by requisition), what happens?",["Meeting is dissolved","Meeting continues with those present","Meeting is adjourned to same day next week","Directors must call fresh meeting"],index=None,key="m7q3")
if q3=="Meeting is adjourned to same day next week": ok("Correct! If quorum is not present within 30 minutes and the meeting was not called by requisition, the meeting is adjourned to the same day the following week.")
elif q3: warn("Incorrect. The meeting is adjourned to same day next week at same time and place (unless called by requisition, in which case it is dissolved).")

recap(["AGM must be held within 6 months of financial year end; not more than 15 months between AGMs",
       "AGM requires 21 days' notice; short notice valid with consent of 95% of members",
       "Quorum: 2 members (private); 5 members (public)",
       "Ordinary Resolution = simple majority (>50%); Special Resolution = 75% majority",
       "Minutes must be entered within 30 days and signed by Chairman",
       "Shareholders holding ≥10% paid-up capital can requisition an EGM",
       "Poll overrides show of hands — each share has proportionate votes on poll"])