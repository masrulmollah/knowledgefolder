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

hero("9","Investigation & Inspection","Understand the powers of the Government, Courts, and Registrar to investigate and inspect company affairs — and the rights and protections of minority shareholders.","🔍")
metrics([("Part IV","Act Coverage"),("Section 196","Registrar Powers"),("200","Min Members to Apply"),("Section 233","Minority Protection")])
st.markdown("<br>",unsafe_allow_html=True)

sh("Overview — Why Investigation Exists")
tip("Purpose","The investigation and inspection provisions protect shareholders, creditors, and the public from fraud, mismanagement, and abuse of corporate power. They provide oversight mechanisms beyond the normal audit process.")

divider()
sh("Inspection of Books by Registrar — Section 196")
law("Section 196 — The Registrar may, at any time, inspect the books and papers of any company. On inspection, the Registrar may take copies of any book, paper or document.")
c1,c2=st.columns(2)
with c1: card("🔍 Registrar's Inspection Powers","✔ Can inspect books and papers of any company at any time<br>✔ Can direct the company to produce books for inspection<br>✔ Can take copies of books, papers, and documents<br>✔ Can call for explanations from officers/employees<br>✔ Can seize books and documents if fraud is suspected<br>✔ Must return seized documents within 30 days (extendable)")
with c2: card("⚡ Seizure of Books — Section 199","The Registrar may, after obtaining a Magistrate's Order, seize books and documents if:<br><br>✔ There is reason to believe the company is committing fraud<br>✔ The books are likely to be destroyed, mutilated, or falsified<br>✔ The company has failed to produce books as directed<br><br><strong>Timeline:</strong> Seized books must be returned within 30 days (extendable by Court)")

divider()
sh("Investigation by Court-Appointed Inspectors — Section 200")
law("Section 200 — The Court may appoint inspectors to investigate the affairs of a company if: (a) not less than 200 members or members holding ≥1/10 of shares apply, or (b) the company by Special Resolution so resolves.")
grounds=[("👥","Member Application","200 or more members, OR members holding not less than 1/10 of issued shares, may apply to Court"),
         ("🗳️","Special Resolution","The company itself passes a Special Resolution requesting Court investigation"),
         ("🏛️","Court's Own Motion","Court may order investigation when it considers it necessary in the public interest"),
         ("🏦","Government Direction","The Government may direct the Registrar to present a petition to Court for investigation"),
         ("📋","On Winding Up","In the course of winding up proceedings, Court may direct investigation into affairs")]
cols=st.columns(2)
for i,(icon,t,d) in enumerate(grounds):
    cols[i%2].markdown(f'<div class="card" style="margin-bottom:10px;"><div class="card-title">{icon} {t}</div><div class="card-body">{d}</div></div>',unsafe_allow_html=True)

divider()
sh("Powers of Inspectors")
for p in ["Examine all books, papers, and documents of the company and related companies",
          "Examine on oath any present or past officer, agent, banker, or employee of the company",
          "Require production of books, documents, and explanations from any person dealing with the company",
          "Extend investigation to related companies — subsidiary, holding, or associated companies",
          "Report findings to the Court — report is admissible as evidence in legal proceedings"]:
    st.markdown(f'<div class="ok-box" style="margin-bottom:6px;padding:9px 14px;">🔍 {p}</div>',unsafe_allow_html=True)

divider()
sh("Protection of Minority Shareholders — Section 233")
law("Section 233 — Any member of a company who complains that the affairs of the company are being conducted in a manner oppressive to any member(s) may apply to the Court for relief.")
card("⚖️ Minority Shareholder Remedies","When majority shareholders or directors conduct company affairs in a manner <strong>oppressive</strong> to minority shareholders, a minority shareholder can apply to Court. The Court may:<br><br>✔ Regulate the conduct of the company's affairs in future<br>✔ Require the company to refrain from doing acts complained of<br>✔ Authorise civil proceedings in the company's name<br>✔ Provide for the <strong>purchase of shares</strong> of any member by other members or by the company<br>✔ Make such other order as Court thinks fit")
warn("Minority protection applies when the majority abuses its power. However, mere 'commercial unfairness' is not enough — there must be actual oppression or breach of legal rights.")

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. How many members minimum can apply to Court for an investigation under Section 200?",["100 members","200 members","500 members","Any number with Court approval"],index=None,key="m9q1")
if q1=="200 members": ok("Correct! Under Section 200, at least 200 members (or holders of ≥1/10 of issued shares) can apply to the Court for appointment of inspectors.")
elif q1: warn("Incorrect. The minimum is 200 members or holders of ≥1/10 of issued share capital.")

q2=st.radio("2. Seized books and documents must be returned by the Registrar within how many days?",["14 days","21 days","30 days","60 days"],index=None,key="m9q2")
if q2=="30 days": ok("Correct! The Registrar must return seized books and documents within 30 days (extendable by Court order).")
elif q2: warn("Incorrect. The return deadline is 30 days under Section 199.")

recap(["Registrar can inspect books of any company at any time without prior notice",
       "Court can appoint inspectors on application by 200+ members or holders of ≥1/10 shares",
       "Inspectors can examine officers on oath and extend investigation to related companies",
       "Minority shareholders can seek Court relief under Section 233 for oppressive conduct",
       "The investigation report is admissible as evidence in legal proceedings",
       "Seized documents must be returned within 30 days (extendable by Court)"])