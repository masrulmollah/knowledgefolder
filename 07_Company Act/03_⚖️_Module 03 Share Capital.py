import streamlit as st

def apply_styles():
    st.markdown("""<style>
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
    </style>""",unsafe_allow_html=True)

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

apply_styles()
hero("3","Share Capital & Debentures","Understand the types of share capital, share transfers, reduction of capital, debentures, and charge registration — core knowledge for every finance professional.","💰")
metrics([("Part III","Act Coverage"),("2","Main Share Types"),("4","Types of Capital"),("21 days","Charge Reg. Deadline")])
st.markdown("<br>",unsafe_allow_html=True)

sh("Types of Share Capital")
tip("Why Capital Structure Matters","Understanding the different layers of share capital is fundamental to reading a balance sheet and understanding a company's financial position.")
cols=st.columns(2)
cap=[("📊","Authorised Capital","The MAXIMUM amount of share capital a company is authorised to issue by its MoA. Represents the ceiling.","#e8f4fd"),
     ("📋","Issued Capital","That part of the authorised capital which has been offered to the public or shareholders for subscription.","#f0f8ee"),
     ("✅","Subscribed Capital","That part of the issued capital which has been applied for and accepted (subscribed) by shareholders.","#fdf4e8"),
     ("💵","Paid-up Capital","That part of subscribed capital which shareholders have actually paid. Remaining unpaid = 'calls in arrears'.","#fdf0f8")]
for i,(icon,name,desc,bg) in enumerate(cap):
    cols[i%2].markdown(f'<div class="card" style="background:{bg};"><div class="card-title">{icon} {name}</div><div class="card-body">{desc}</div></div>',unsafe_allow_html=True)
law("Hierarchy: Authorised Capital ≥ Issued Capital ≥ Subscribed Capital ≥ Called-up Capital ≥ Paid-up Capital")

divider()
sh("Types of Shares")
tab1,tab2=st.tabs(["📗 Ordinary (Equity) Shares","📘 Preference Shares"])
with tab1:
    c1,c2=st.columns(2)
    with c1: card("📗 Ordinary (Equity) Shares","• Residual owners of the company<br>• Voting rights: One share = One vote<br>• Dividend: Variable — depends on profits<br>• Capital repayment: Last priority on winding up<br>• No fixed return — upside is unlimited<br>• Right to attend and vote at General Meetings")
    with c2: card("💡 Key Characteristics","Equity shareholders bear the most risk but also get the most reward. They are the true owners of the company. Their return is not fixed — it depends entirely on company performance.")
with tab2:
    c1,c2=st.columns(2)
    with c1: card("📘 Preference Shares","• Fixed dividend rate — paid before ordinary dividend<br>• Priority in repayment of capital on winding up<br>• Usually carry no/restricted voting rights<br>• Can be: Cumulative / Non-Cumulative<br>• Can be: Participating / Non-Participating<br>• Can be: Redeemable / Irredeemable<br>• Can be: Convertible (to equity)")
    with c2:
        for t,d in [("Cumulative","Unpaid dividends accumulate and must be paid in future profitable years before equity dividend."),
                    ("Non-Cumulative","If dividend not paid in a year, it lapses — no right to recover it later."),
                    ("Participating","Get fixed dividend PLUS share in surplus profits after equity dividend."),
                    ("Redeemable","Company can buy back/redeem these shares after a specified period.")]:
            st.markdown(f'<div class="card" style="padding:10px 14px;margin-bottom:6px;"><div class="card-title" style="font-size:0.9rem;">{t}</div><div class="card-body" style="font-size:0.85rem;">{d}</div></div>',unsafe_allow_html=True)

divider()
sh("Transfer & Transmission of Shares")
c1,c2=st.columns(2)
with c1: card("🔄 Transfer of Shares","A <strong>voluntary act</strong> by the shareholder to pass ownership to another person.<br><br><strong>Process:</strong><br>✔ Execute a Share Transfer Form<br>✔ Submit to company with share certificate<br>✔ Company registers in Register of Members<br>✔ Issue new share certificate to transferee<br><br><strong>Private Company Restriction:</strong> Directors may refuse transfer without giving reasons. Notice of refusal must be sent within 2 months.")
with c2: card("⚖️ Transmission of Shares","An <strong>operation of law</strong> — shares pass to another party due to death, insolvency, or lunacy of the shareholder.<br><br><strong>On Death:</strong> Shares vest in legal heir/executor<br><br><strong>On Insolvency:</strong> Shares vest in the Official Receiver<br><br><strong>Key Difference:</strong> Transfer requires a stamp duty-paid instrument; Transmission does not require an instrument of transfer.")
warn("In a private company, a refusal to register a transfer must be communicated within 2 months, otherwise the company may be compelled by court to register the transfer.")

divider()
sh("Reduction of Share Capital — Section 59")
law("Section 59 — A company limited by shares may, if authorised by its AoA, by Special Resolution reduce its share capital in any way, subject to confirmation by the Court.")
st.markdown("""<table><tr><th>Step</th><th>Action Required</th></tr>
<tr><td>1</td><td>Check AoA authorises capital reduction</td></tr>
<tr><td>2</td><td>Pass Special Resolution in General Meeting</td></tr>
<tr><td>3</td><td>Apply to Court for confirmation</td></tr>
<tr><td>4</td><td>Court gives notice to creditors and settles list of objectors</td></tr>
<tr><td>5</td><td>Court may require adequate provisions for creditors' claims</td></tr>
<tr><td>6</td><td>Court confirms reduction by Order</td></tr>
<tr><td>7</td><td>File certified copy of Order + altered MoA with Registrar within 90 days</td></tr>
<tr><td>8</td><td>Registrar registers — Certificate of Registration issued</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("Debentures")
tip("Definition","Under Section 2(e): 'Debenture includes debenture stock, bonds and any other securities of a company, whether constituting a charge on the assets of the company or not.'")
cols=st.columns(2)
debs=[("🔒","Secured Debentures","Backed by a charge on company assets. Debenture holders have priority on those assets in case of default."),
      ("🔓","Unsecured Debentures","No charge on assets. Debenture holders are treated as unsecured creditors — higher risk, usually higher interest."),
      ("💱","Convertible Debentures","Can be converted into equity shares after a specified period."),
      ("🔁","Redeemable Debentures","Repaid by the company on or before a specified date."),
      ("📋","Registered Debentures","Name of holder recorded in company's register. Transfer requires execution of a deed."),
      ("📜","Bearer Debentures","Transferred by mere delivery — no formal transfer process.")]
for i,(icon,name,desc) in enumerate(debs):
    cols[i%2].markdown(f'<div class="card" style="margin-bottom:10px;"><div class="card-title">{icon} {name}</div><div class="card-body">{desc}</div></div>',unsafe_allow_html=True)

divider()
sh("Registration of Charges — Section 107")
law("Section 107 — Every charge created by a company must be registered with the Registrar within 21 days of its creation. Failure makes the charge VOID against liquidators and creditors.")
c1,c2=st.columns(2)
with c1: card("⚡ Fixed Charge vs Floating Charge","<strong>Fixed Charge:</strong><br>• Attached to specific identified assets (land, building, machinery)<br>• Company cannot freely deal with the charged asset<br>• Priority over floating charge holders<br><br><strong>Floating Charge:</strong><br>• Hovers over a class of assets (stock-in-trade, debtors)<br>• Company can deal freely with assets until 'crystallisation'<br>• Crystallises on default, winding up, or appointment of receiver")
with c2: card("⏰ 21-Day Registration Rule","Timeline: Charge must be registered within <strong>21 days</strong> of creation<br><br><strong>Effect of Non-Registration:</strong><br>• Charge is void against liquidators and creditors<br>• Money secured becomes immediately payable<br>• BUT the charge is still valid between the company and charge holder<br><br>Registrar's Register of Charges is a <strong>public document</strong> — anyone can inspect it.")
warn("Failing to register a charge within 21 days makes it void against creditors and liquidators — serious implications in insolvency situations.")

divider()
sh("Shares vs Debentures — Comparison")
st.markdown("""<table><tr><th>Aspect</th><th>Shares</th><th>Debentures</th></tr>
<tr><td>Nature</td><td>Ownership instrument</td><td>Debt instrument</td></tr>
<tr><td>Return</td><td>Dividend — variable</td><td>Interest — fixed</td></tr>
<tr><td>Voting Rights</td><td>Yes (equity shares)</td><td>No</td></tr>
<tr><td>Priority on Winding Up</td><td>Last — after all creditors</td><td>Before shareholders</td></tr>
<tr><td>Risk</td><td>Higher risk, higher potential reward</td><td>Lower risk, fixed return</td></tr>
<tr><td>Tax Treatment</td><td>Dividend from after-tax profits</td><td>Interest is tax-deductible for company</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. What is the maximum share capital a company can issue?",["Subscribed Capital","Paid-up Capital","Authorised Capital","Issued Capital"],index=None,key="m3q1")
if q1=="Authorised Capital": ok("Correct! Authorised Capital is the ceiling — the maximum that can be issued under the MoA.")
elif q1: warn("Incorrect. Authorised Capital (also called Registered/Nominal Capital) is the ceiling.")

q2=st.radio("2. A charge must be registered with the Registrar within how many days of creation?",["7 days","14 days","21 days","30 days"],index=None,key="m3q2")
if q2=="21 days": ok("Correct! Under Section 107, every charge must be registered within 21 days, failing which it is void against liquidators and creditors.")
elif q2: warn("Incorrect. Under Section 107, the deadline is 21 days from the date of creation of the charge.")

q3=st.radio("3. Which type of preference share allows unpaid dividends to accumulate?",["Non-cumulative","Cumulative","Participating","Redeemable"],index=None,key="m3q3")
if q3=="Cumulative": ok("Correct! Cumulative preference shares accumulate unpaid dividends for recovery from future profits.")
elif q3: warn("Incorrect. It is the Cumulative Preference Share that accumulates unpaid dividends.")

recap(["4 types of capital: Authorised ≥ Issued ≥ Subscribed ≥ Paid-up",
       "Ordinary shares carry voting rights; preference shares have priority on dividend & capital",
       "Transfer is voluntary; Transmission is by operation of law (death, insolvency)",
       "Reduction of share capital requires Special Resolution + Court confirmation",
       "Debenture holders are creditors; shareholders are owners",
       "Every charge must be registered within 21 days — failure makes charge void against creditors",
       "Fixed charge is on specific assets; Floating charge is on a class of assets"])
