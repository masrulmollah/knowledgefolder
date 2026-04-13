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

hero("6","Directors & Company Officers","Master the appointment, duties, powers, liabilities, and restrictions on directors and key officers — critical for governance and compliance professionals.","👔")
metrics([("2","Min Directors (Pvt.)"),("3","Min Directors (Public)"),("5 years","Max MD Tenure"),("Section 103","Declare Interest")])
st.markdown("<br>",unsafe_allow_html=True)

sh("Who is a Director?")
law("Section 2(f) — 'Director includes any person occupying the position of director by whatever name called.' The title does not matter — substance determines whether someone is a director.")

divider()
sh("Appointment of Directors")
methods=[("📜","Named in Articles/Prospectus","First directors can be named in the AoA or prospectus. They hold office from incorporation."),
         ("🗳️","Elected by Shareholders","In a General Meeting by ordinary resolution — normal method for subsequent directors."),
         ("🏛️","Board Appointment","Board may appoint directors to fill casual vacancies or as additional directors, subject to AoA."),
         ("🏛️","Government Nomination","In certain public interest companies, Government may appoint nominee directors."),
         ("⚖️","Court Order","Courts may appoint directors in specific circumstances.")]
cols=st.columns(2)
for i,(icon,m,d) in enumerate(methods):
    cols[i%2].markdown(f'<div class="card" style="margin-bottom:10px;"><div class="card-title">{icon} {m}</div><div class="card-body">{d}</div></div>',unsafe_allow_html=True)

divider()
sh("Qualifications & Disqualifications")
c1,c2=st.columns(2)
with c1: card("✅ General Qualifications","• Must be a natural person (individual, not a company)<br>• Must hold 'qualification shares' if required by AoA<br>• Must be at least 18 years of age<br>• Must not be an undischarged insolvent<br>• Must be of sound mind<br>• Must consent to act as director (Form IX)")
with c2: card("❌ Disqualifications (Section 99-102)","A person CANNOT be a director if they:<br>• Are an <strong>undischarged insolvent</strong> (bankrupt)<br>• Have been <strong>convicted of fraud/dishonesty</strong> within 5 years<br>• Have failed to pay calls on their shares<br>• Are of <strong>unsound mind</strong> (declared by court)<br>• Are a <strong>body corporate</strong> (only individuals qualify)")

divider()
sh("Duties & Responsibilities of Directors")
duties=[("🎯","Fiduciary Duty","Must act in good faith, in the best interests of the company. Must not use position for personal gain."),
        ("🧠","Duty of Care & Skill","Must exercise reasonable care and diligence expected of a reasonably prudent person."),
        ("🚫","Duty to Avoid Conflicts","Must not place themselves in a position where personal interests conflict with company interests."),
        ("📋","Duty to Act Within Powers","Must act within the limits of the Act, MoA, AoA, and resolutions of the company."),
        ("📊","Duty to Maintain Accounts","Responsible for ensuring proper books of account are maintained (Section 181)."),
        ("📅","Duty to File Returns","Responsible for timely filing of Annual Returns, charge registrations, etc. with RJSC."),
        ("🔍","Duty of Disclosure","Must disclose interests in contracts, shareholdings, related party transactions."),
        ("🤝","Duty to Creditors","When company is in financial difficulty, duty extends to protecting creditors' interests.")]
for icon,duty,desc in duties:
    with st.expander(f"{icon} {duty}"):
        st.markdown(f'<div class="law-box">{desc}</div>',unsafe_allow_html=True)

divider()
sh("Restrictions on Loans to Directors — Section 103A")
warn("A company (other than a banking company) SHALL NOT directly or indirectly make any loan to, or give any guarantee in connection with any loan made to, any director or any firm in which the director is a partner.")
card("⚠️ Exceptions to the Loan Prohibition","✔ Loans to <strong>managing directors</strong> as part of their service conditions<br>✔ Loans by <strong>holding companies to subsidiaries</strong><br>✔ Loans where <strong>Central Government approves</strong><br>✔ Companies whose <strong>ordinary business includes lending money</strong> (e.g., NBFIs)")

divider()
sh("Managing Director")
c1,c2=st.columns(2)
with c1: card("👔 Role & Appointment","A Managing Director (MD) is a director to whom <strong>substantial powers of management</strong> are entrusted.<br><br><strong>Appointment:</strong> By the Board, subject to AoA and shareholder approval<br><strong>Tenure:</strong> Maximum <strong>5 years</strong> at a time (re-appointment permitted)<br><strong>Powers:</strong> Subject to superintendence, control and direction of the Board<br><strong>Remuneration:</strong> Must be approved by shareholders")
with c2: card("🚫 MD Cannot (without Board/Shareholder approval)","• Make calls on shareholders for unpaid share capital<br>• Issue debentures<br>• Borrow money beyond Board delegation<br>• Invest the company's funds<br>• Make loans to others<br>• Sell, lease, or dispose of whole/substantial part of the undertaking")

divider()
sh("Declaration of Director's Interest — Section 103")
law("Section 103 — Every director who is directly or indirectly interested in a contract or arrangement with the company shall declare the nature of his interest at the Board meeting at which the question is first considered.")
st.markdown("""<table><tr><th>Situation</th><th>When to Disclose</th><th>Method</th></tr>
<tr><td>Existing contract where director has interest</td><td>At first Board meeting after becoming interested</td><td>Written notice to Board</td></tr>
<tr><td>Proposed new contract</td><td>At the Board meeting where contract is first considered</td><td>Oral declaration recorded in minutes</td></tr>
<tr><td>Director becomes interested after contract</td><td>At next Board meeting</td><td>Written notice to Board</td></tr></table>""",unsafe_allow_html=True)
warn("Failure to disclose interest does NOT automatically void the contract, but the director can be held personally liable and may be required to account for any profit made.")

divider()
sh("Liability of Directors")
tab1,tab2,tab3=st.tabs(["⚖️ Civil Liability","🚔 Criminal Liability","🛡️ Protection"])
with tab1: card("💼 Civil Liability","Directors may be personally liable for:<br>✔ Breach of fiduciary duty<br>✔ Negligence in management<br>✔ Ultra vires transactions causing loss<br>✔ Fraudulent or wrongful trading<br>✔ Misstatements in prospectus<br>✔ Failure to file returns — penalties under the Act<br>✔ Unlawful payment of dividends out of capital")
with tab2: card("🚔 Criminal Liability","Directors may face criminal prosecution for:<br>✔ Wilful misstatement in prospectus (imprisonment up to 2 years)<br>✔ Fraudulent trading (deceiving creditors/members)<br>✔ Fraudulent preference payments before winding up<br>✔ Misfeasance — misapplication of company money<br>✔ Making unauthorised loans to directors")
with tab3: card("🛡️ Directors' Protection","Directors are NOT personally liable when:<br>✔ They acted <strong>honestly and reasonably</strong> in all circumstances<br>✔ They relied on information/advice from qualified experts in good faith<br>✔ They properly delegated duties to appropriate officers<br>✔ They had their <strong>dissent recorded in minutes</strong>")

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. What is the minimum number of directors required for a Public Limited Company?",["2","3","5","7"],index=None,key="m6q1")
if q1=="3": ok("Correct! A Public Limited Company must have at least 3 directors.")
elif q1: warn("Incorrect. A Public Company requires a minimum of 3 directors; Private Company requires 2.")

q2=st.radio("2. A Managing Director's tenure per appointment cannot exceed:",["3 years","4 years","5 years","10 years"],index=None,key="m6q2")
if q2=="5 years": ok("Correct! Under the Act, a Managing Director can be appointed for a maximum of 5 years at a time.")
elif q2: warn("Incorrect. Maximum tenure per appointment for a Managing Director is 5 years.")

q3=st.radio("3. An undischarged insolvent:",["Can be a director with shareholder approval","Cannot be a director under any circumstances","Can be a director in private companies only","Can be a director with court approval"],index=None,key="m6q3")
if q3=="Cannot be a director under any circumstances": ok("Correct! Under Section 99, an undischarged insolvent is absolutely disqualified from being a director.")
elif q3: warn("Incorrect. An undischarged insolvent is absolutely disqualified under Section 99.")

recap(["Minimum 2 directors for private company; 3 for public company",
       "Directors must not be undischarged insolvents, convicted fraudsters, or of unsound mind",
       "Directors owe fiduciary duty, duty of care, and duty to act within powers",
       "Loans to directors are generally prohibited (with narrow exceptions)",
       "MD tenure is max 5 years per appointment; powers subject to Board superintendence",
       "Directors must declare interests in contracts at the relevant Board meeting",
       "Criminal liability for wilful misstatement in prospectus — up to 2 years imprisonment"])