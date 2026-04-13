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

hero("4","Prospectus & Public Issue","Rules governing prospectus, public share issuance, allotment of shares, and liability for misstatements — essential for capital market professionals.","📣")
metrics([("Part IV","Act Coverage"),("120 days","Prospectus Validity"),("5%","Min. Application Money"),("2 Years","Max Imprisonment")])
st.markdown("<br>",unsafe_allow_html=True)

sh("What is a Prospectus?")
tip("Definition","A Prospectus is any document described or issued as a prospectus, and includes any notice, circular, advertisement or other document inviting offers from the public for subscription or purchase of shares or debentures of a company.")
law("Key Rule: Only a PUBLIC company can issue a prospectus to invite the public. A PRIVATE company is PROHIBITED from issuing a prospectus or inviting the public to subscribe.")
c1,c2=st.columns(2)
with c1: card("🎯 Purpose of a Prospectus","• Invites the public to subscribe for shares/debentures<br>• Provides complete information for informed investment decisions<br>• Creates legal obligations on the company and promoters<br>• Establishes civil and criminal liability for misstatements<br>• Must be filed with the Registrar before publication")
with c2: card("⏳ Registration Requirement","A prospectus must be:<br>✔ <strong>Dated</strong> — the date is deemed the date of publication<br>✔ <strong>Registered</strong> with the Registrar before publication<br>✔ <strong>Signed</strong> by every person named as a director or proposed director<br>✔ <strong>Valid for 90 days</strong> from date of registration")

divider()
sh("Mandatory Contents of a Prospectus")
contents=[("📋","Company Information","Name, registered office address, objects of the company"),
          ("👥","Directors & Promoters","Names, addresses, qualifications of directors; promoter details"),
          ("💰","Financial Information","Share capital structure, minimum subscription amount"),
          ("📊","Financial Statements","Audited accounts, profit/loss history, assets/liabilities"),
          ("🏦","Bankers & Auditors","Names of bankers, auditors, legal advisors, and underwriters"),
          ("📅","Time Limits","Opening/closing dates for subscription, estimated issue expenses"),
          ("🏢","Property","Details of property acquired or to be acquired with issue proceeds"),
          ("⚖️","Litigation","Details of any pending legal proceedings"),
          ("🎯","Use of Proceeds","How the funds raised will be utilised"),
          ("📜","Material Contracts","Details of contracts not in ordinary course of business")]
cols=st.columns(2)
for i,(icon,t,d) in enumerate(contents):
    cols[i%2].markdown(f'<div class="card" style="padding:12px 16px;margin-bottom:8px;"><div class="card-title" style="font-size:0.9rem;">{icon} {t}</div><div class="card-body" style="font-size:0.85rem;">{d}</div></div>',unsafe_allow_html=True)

divider()
sh("Statement in Lieu of Prospectus")
card("📝 What is Statement in Lieu of Prospectus?","When a public company does <strong>NOT issue a prospectus</strong> (raises capital through private placement), it must file a <strong>Statement in Lieu of Prospectus</strong> with the Registrar at least <strong>3 days before</strong> allotting any shares or debentures.<br><br>Purpose: To ensure transparency even when no public offer is made.")
st.markdown("""<table><tr><th>Aspect</th><th>Prospectus</th><th>Statement in Lieu of Prospectus</th></tr>
<tr><td>When Used</td><td>When shares offered to general public</td><td>When shares NOT offered to public</td></tr>
<tr><td>Filing</td><td>Before publication/issue</td><td>At least 3 days before first allotment</td></tr>
<tr><td>Nature</td><td>Public document for investors</td><td>Regulatory filing only</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("Allotment of Shares — Minimum Subscription")
law("Section 151 — No allotment shall be made unless the minimum subscription stated in the prospectus has been subscribed and the sum payable on application has been paid to and received by the company.")
c1,c2=st.columns(2)
with c1: card("📐 Minimum Subscription Rule","✔ Must be stated in the prospectus<br>✔ Application money must be at least <strong>5%</strong> of nominal value<br>✔ If minimum subscription not received within <strong>120 days</strong> of prospectus issue → all money must be refunded<br>✔ If not refunded within <strong>130 days</strong> → directors personally liable to pay interest at 6% p.a.")
with c2: card("⚠️ Irregular Allotment","An allotment is <strong>voidable</strong> if made before:<br>• Minimum subscription received<br>• Beginning of 3rd day after prospectus issue<br>• Application money properly received<br><br>The applicant can avoid the allotment within <strong>2 months</strong> of the company's statutory meeting.")

divider()
sh("Liability for Misstatements in Prospectus")
tip("Why This Matters","A prospectus is a legally binding document. False or misleading statements expose promoters, directors, and experts to both civil (compensation) and criminal (imprisonment/fine) liability.")
tab1,tab2=st.tabs(["⚖️ Civil Liability","🚔 Criminal Liability"])
with tab1:
    card("💼 Civil Liability — Compensation","Any person who subscribed based on a misleading/false prospectus can claim <strong>compensation</strong> from every director at time of issue, every promoter, every person who authorised the issue, and every expert who gave a report.<br><br><strong>Defences:</strong> Reasonable belief in truth, reliance on expert statement, withdrawal of consent before issue.")
with tab2:
    card("🚔 Criminal Liability","Any person who authorised the issue of a prospectus with a <strong>wilfully untrue</strong> statement is liable to:<br><br>🔴 <strong>Imprisonment</strong> up to 2 years, OR<br>🔴 <strong>Fine</strong>, OR<br>🔴 <strong>Both</strong> imprisonment and fine")

divider()
sh("Shares Issued at Premium or Discount")
c1,c2=st.columns(2)
with c1: card("📈 Issue at Premium","When shares are issued above their <strong>nominal/face value</strong>.<br><br>Example: Face value Tk. 10, Issue price Tk. 25 → Premium = Tk. 15<br><br><strong>Premium must be credited to Share Premium Account.</strong><br><br>Uses of Share Premium Account:<br>✔ Issue bonus shares<br>✔ Write off preliminary expenses<br>✔ Provide for premium on debenture redemption")
with c2: card("📉 Issue at Discount","Generally, shares <strong>cannot be issued at a discount</strong> except in very limited circumstances:<br><br>✔ Authorised by a resolution in general meeting<br>✔ Confirmed by the Court<br>✔ Maximum discount: 10% of nominal value<br>✔ Shares must be of a class already issued")

divider()
sh("🛠️ Interactive: Public Issue Calculator")
face_val=st.number_input("Face value per share (Tk.)",min_value=1,value=10)
issue_price=st.number_input("Issue price per share (Tk.)",min_value=1,value=25)
num_shares=st.number_input("Total shares to be issued",min_value=1000,value=1000000,step=100000)
premium=issue_price-face_val
total_size=issue_price*num_shares
app_money=0.05*issue_price*num_shares
if premium>0:
    ok(f"📊 <strong>Issue at Premium</strong> (Tk. {premium:,.0f} per share)<br>Total Issue Size: <strong>Tk. {total_size:,.0f}</strong> | Share Premium Account: <strong>Tk. {premium*num_shares:,.0f}</strong> | Min. Application Money (5%): <strong>Tk. {app_money:,.0f}</strong>")
elif premium<0:
    warn(f"Issue at Discount (Tk. {abs(premium):,.0f} per share) — Generally not permitted without court approval.")
else:
    ok(f"Issue at Par. Total Issue Size: Tk. {total_size:,.0f}")

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. Which type of company is allowed to issue a prospectus to the general public?",["Private Limited Company","Public Limited Company","Company Limited by Guarantee","Any registered company"],index=None,key="m4q1")
if q1=="Public Limited Company": ok("Correct! Only a Public Limited Company can issue a prospectus inviting the public to subscribe.")
elif q1: warn("Incorrect. Only Public Limited Companies are permitted to issue a prospectus.")

q2=st.radio("2. If minimum subscription is not received, within how many days must application money be refunded?",["90 days","100 days","120 days","150 days"],index=None,key="m4q2")
if q2=="120 days": ok("Correct! If minimum subscription is not received within 120 days, all application money must be refunded.")
elif q2: warn("Incorrect. The time limit is 120 days from the date of issue of the prospectus.")

q3=st.radio("3. Share premium received must be credited to which account?",["General Reserve","Capital Redemption Reserve","Share Premium Account","Revenue Reserve"],index=None,key="m4q3")
if q3=="Share Premium Account": ok("Correct! Any premium received on issue of shares must be transferred to the Share Premium Account.")
elif q3: warn("Incorrect. Share premium must go to the Share Premium Account.")

recap(["Only Public Companies can issue a prospectus to invite the general public",
       "Prospectus must be registered with RJSC before publication",
       "Minimum subscription: if not met in 120 days, refund all money",
       "Application money must be at least 5% of the nominal value of shares",
       "False statements in a prospectus attract civil and criminal liability (up to 2 years imprisonment)",
       "Share premium must be credited to Share Premium Account",
       "Private companies must file Statement in Lieu of Prospectus (not actual prospectus)"])
