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

hero("8","Accounts, Audit & Financial Reporting","The most critical module for finance and accounts professionals — covering statutory obligations for maintaining accounts, financial reporting, appointment of auditors, and audit requirements under the Act.","📊")
metrics([("Section 181","Books of Account"),("Section 183","P&L / Balance Sheet"),("Section 210","Auditor Appointment"),("8 Years","Record Retention")])
st.markdown("<br>",unsafe_allow_html=True)

tip("Why This Module is Critical","Finance and accounts professionals are directly responsible for these provisions. Failure to maintain proper accounts, prepare financial statements, or facilitate audits exposes both the company and its officers to serious legal liability.")

sh("Obligation to Maintain Books of Account — Section 181")
law("Section 181(1) — Every company shall keep at its registered office proper books of account with respect to: (a) all sums of money received and expended; (b) all sales and purchases of goods; (c) the assets and liabilities of the company.")
c1,c2=st.columns(2)
with c1: card("📚 What Books Must Be Kept","✔ <strong>Cash Book</strong> — all receipts and payments<br>✔ <strong>Sales Records</strong> — all sales of goods and services<br>✔ <strong>Purchase Records</strong> — all goods/services purchased<br>✔ <strong>General Ledger</strong> — all accounts and balances<br>✔ <strong>Stock Records</strong> — inventory at year beginning and end<br>✔ <strong>Work-in-Progress</strong> — for manufacturing companies<br>✔ <strong>Fixed Asset Register</strong>")
with c2: card("📍 Where Kept & Retention","<strong>Location:</strong> Registered office<br><strong>Retention Period:</strong> Minimum <strong>8 years</strong> from end of financial year<br><br><strong>Inspection:</strong> Directors have right to inspect books at any time. Members generally do NOT have right to inspect books (only statutory registers).")
warn("Failure to keep proper books of account is an offence. Every officer in default is liable to imprisonment up to 6 months or fine or both.")

divider()
sh("Financial Statements — Section 183 & 184")
law("Section 183 — The directors shall at every AGM lay before the company a Balance Sheet and Profit & Loss Account for the period since the last such accounts.")
st.markdown("""<table><tr><th>Statement</th><th>Contents</th><th>Requirement</th></tr>
<tr><td><strong>Balance Sheet</strong></td><td>Assets, liabilities, equity/capital; must give true and fair view at year end</td><td>Must comply with Schedule XI format; signed by directors</td></tr>
<tr><td><strong>Profit & Loss Account</strong></td><td>Revenue, expenses, profit/loss for the financial year</td><td>Must give true and fair view; signed by directors</td></tr>
<tr><td><strong>Cash Flow Statement</strong></td><td>Cash inflows/outflows from operating, investing, financing activities</td><td>Required for listed companies under BSEC rules</td></tr>
<tr><td><strong>Notes to Accounts</strong></td><td>Accounting policies, explanations, disclosures</td><td>Integral part of financial statements</td></tr>
<tr><td><strong>Directors' Report</strong></td><td>State of affairs, dividend, future plans, material changes</td><td>Must accompany financial statements at AGM</td></tr>
<tr><td><strong>Auditors' Report</strong></td><td>Opinion on truth and fairness of financial statements</td><td>Must be read at AGM and sent to all members</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("Appointment of Auditors — Section 210")
c1,c2=st.columns(2)
with c1: card("✅ Auditor Qualification — Section 212","An auditor must be a <strong>Chartered Accountant</strong> within the meaning of the Bangladesh Chartered Accountants Order, 1973 (i.e., a member of ICAB).<br><br><strong>Disqualifications — Section 213:</strong><br>❌ Officer or employee of the company<br>❌ Partner/employee of an officer of the company<br>❌ Person indebted to the company > Tk. 1,000<br>❌ Body corporate (only individuals can be auditors)<br>❌ Person who has guaranteed any debt of the company")
with c2: card("📅 Appointment Timeline","<strong>First Auditors:</strong> Appointed by the <strong>Board</strong> within 1 month of incorporation. Hold office until conclusion of first AGM.<br><br><strong>Subsequent Auditors:</strong> Appointed by <strong>members at each AGM</strong>. Hold office from that AGM to the next.<br><br><strong>Casual Vacancy:</strong> Filled by the Board. Appointee holds office until next AGM.<br><br><strong>Remuneration:</strong> Fixed by the members at AGM (or Board if Board appointed)")

divider()
sh("Powers & Duties of Auditors — Section 213-215")
tab1,tab2=st.tabs(["💪 Powers","📋 Duties"])
with tab1:
    for p in ["Access at all times to the books, accounts, and vouchers of the company",
              "Require from officers/employees such information and explanations as necessary",
              "Attend any General Meeting of the company",
              "Receive all notices and communications relating to General Meetings",
              "Be heard at General Meetings on matters concerning the auditors"]:
        st.markdown(f'<div class="ok-box" style="margin-bottom:6px;padding:9px 14px;">💪 {p}</div>',unsafe_allow_html=True)
with tab2:
    for t,d in [("Report to Members","Auditor must make a report to the members on the accounts examined and on every Balance Sheet and P&L Account"),
                ("True & Fair View","Report must state whether, in their opinion, the financial statements give a true and fair view"),
                ("Proper Books","Report must state whether proper books of account have been kept"),
                ("Balance Sheet Agreement","Report must state whether the Balance Sheet agrees with the books of account"),
                ("Qualifications","Must clearly state any qualifications, reservations, or adverse opinions")]:
        with st.expander(f"📋 {t}"):
            st.markdown(f'<div class="law-box">{d}</div>',unsafe_allow_html=True)

divider()
sh("Types of Audit Opinions")
opinions=[("✅","Unqualified (Clean) Opinion","Financial statements give a true and fair view in all material respects. No issues found.","#f0f8ee"),
          ("⚠️","Qualified Opinion","Except for a specific matter, the statements give a true and fair view. Disagreement on specific issue.","#fff8e8"),
          ("❌","Adverse Opinion","Financial statements do NOT give a true and fair view. Serious disagreement with management.","#fff0f0"),
          ("🚫","Disclaimer of Opinion","Auditor is unable to express an opinion due to significant limitation of scope.","#f5f5f5"),
          ("📝","Emphasis of Matter","Opinion is unqualified but auditor highlights a matter of importance (e.g., going concern doubt).","#f0f4fd")]
cols=st.columns(2)
for i,(icon,name,desc,bg) in enumerate(opinions):
    cols[i%2].markdown(f'<div class="card" style="background:{bg};margin-bottom:10px;"><div class="card-title">{icon} {name}</div><div class="card-body">{desc}</div></div>',unsafe_allow_html=True)

divider()
sh("Dividend — Key Rules")
law("General Rule: Dividends can only be paid out of PROFITS — not out of capital. Payment of dividend out of capital is unlawful and directors are personally liable to restore the capital.")
div_rules=[("📢","Declaration","Dividend is declared by members at AGM. Directors can declare INTERIM dividend between AGMs."),
           ("💡","Recommendation","Directors RECOMMEND the amount; members can reduce it but CANNOT increase it beyond directors' recommendation."),
           ("⏰","Payment Timeline","Dividend must be paid within 42 days of declaration."),
           ("🚫","Unclaimed Dividends","If dividend remains unclaimed for 3 years → transferred to a separate Unclaimed Dividend Account."),
           ("⚠️","Source","From current year profits OR accumulated profits. Cannot be paid from capital.")]
cols=st.columns(2)
for i,(icon,t,d) in enumerate(div_rules):
    cols[i%2].markdown(f'<div class="card" style="margin-bottom:10px;"><div class="card-title">{icon} {t}</div><div class="card-body">{d}</div></div>',unsafe_allow_html=True)

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. Who appoints the FIRST auditor of a newly incorporated company?",["Members at first AGM","Board of Directors within 1 month of incorporation","Registrar of Joint Stock Companies","Government"],index=None,key="m8q1")
if q1=="Board of Directors within 1 month of incorporation": ok("Correct! Under Section 210, the Board of Directors appoints the first auditor within 1 month of incorporation.")
elif q1: warn("Incorrect. The first auditors are appointed by the Board within 1 month of incorporation (Section 210).")

q2=st.radio("2. Which type of professional must serve as a company auditor in Bangladesh?",["Cost and Management Accountant","Chartered Accountant (ICAB member)","Chartered Secretary","Any qualified accountant"],index=None,key="m8q2")
if q2=="Chartered Accountant (ICAB member)": ok("Correct! Only an ICAB Chartered Accountant under Section 212 can serve as a statutory auditor.")
elif q2: warn("Incorrect. Only an ICAB Chartered Accountant (Section 212) can serve as statutory auditor.")

q3=st.radio("3. Dividends can be paid out of:",["Capital profits only","Capital reserves","Current or accumulated profits","Any reserves including capital"],index=None,key="m8q3")
if q3=="Current or accumulated profits": ok("Correct! Dividends can only be paid from profits — current year profits or accumulated (retained) profits. Payment from capital is unlawful.")
elif q3: warn("Incorrect. Dividends can only be paid out of profits (current or accumulated) — NEVER from capital.")

recap(["Every company must maintain proper books of account at registered office for minimum 8 years",
       "Financial statements must give a 'true and fair view' — this is the primary standard",
       "First auditor appointed by Board within 1 month; subsequent auditors by members at AGM",
       "Auditors must be ICAB Chartered Accountants — no body corporate can be auditor",
       "Auditor has unrestricted access to all books, accounts, vouchers, and explanations",
       "Four types of audit opinions: Unqualified, Qualified, Adverse, Disclaimer",
       "Dividends must come from profits — payment from capital is illegal",
       "Dividend declared at AGM must be paid within 42 days"])