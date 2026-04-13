import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
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
    </style>""", unsafe_allow_html=True)

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

# ── PAGE ──────────────────────────────────────────────────────────────
apply_styles()
hero("2","Incorporation & Formation of a Company",
     "Master the process of forming a company — from drafting the Memorandum and Articles of Association to obtaining the Certificate of Incorporation.","🏗️")
metrics([("Part II","Act Coverage"),("2","Min. Members (Pvt.)"),("7","Min. Members (Public)"),("6","Clauses in MoA")])
st.markdown("<br>",unsafe_allow_html=True)

sh("Overview of Company Formation Process")
steps=[("1️⃣","Draft MoA & AoA","Prepare Memorandum and Articles of Association as per Act requirements"),
       ("2️⃣","Name Clearance","Obtain name clearance from the Registrar of Joint Stock Companies (RJSC)"),
       ("3️⃣","Sign & Witness","Subscribers sign MoA & AoA in presence of at least 2 witnesses"),
       ("4️⃣","File with RJSC","Submit MoA, AoA, and required forms/fees to the RJSC"),
       ("5️⃣","Certificate Issued","RJSC reviews and issues the Certificate of Incorporation"),
       ("6️⃣","Legal Existence","From the date on certificate, company becomes a legal person")]
cols=st.columns(3)
for i,(num,t,d) in enumerate(steps):
    cols[i%3].markdown(f'<div class="card"><div class="card-title">{num} {t}</div><div class="card-body">{d}</div></div>',unsafe_allow_html=True)

divider()
sh("Memorandum of Association (MoA)")
tip("What is MoA?","The MoA is the 'constitution' of the company — the fundamental document that defines the company's relationship with the outside world. A company cannot act beyond what the MoA allows.")

st.markdown('<div class="sec-head" style="font-size:1.05rem;">The Six Mandatory Clauses of the MoA</div>',unsafe_allow_html=True)
clauses=[("📛","1. Name Clause","States the name of the company. Private company must end with 'Limited' or 'Ltd.' and public company with 'Public Limited Company' or 'PLC'."),
         ("📍","2. Registered Office Clause","States the name of the division/district in Bangladesh where the registered office will be situated."),
         ("🎯","3. Objects Clause","States the objects/purpose for which the company is formed. Company cannot act beyond these objects (ultra vires doctrine)."),
         ("🛡️","4. Liability Clause","States whether the liability of members is limited (by shares or by guarantee) or unlimited."),
         ("💰","5. Capital Clause","States the amount of authorised (registered) share capital and its division into shares of fixed value."),
         ("✍️","6. Subscription Clause","Names and addresses of subscribers who agree to take at least one share each, signed before witnesses.")]
for icon,t,b in clauses:
    with st.expander(f"{icon} {t}"):
        st.markdown(f'<div class="law-box">{b}</div>',unsafe_allow_html=True)

law("Section 13 — Alteration of MoA: A company cannot alter MoA conditions EXCEPT as provided in the Act.")
warn("The Objects Clause is critical — any transaction beyond stated objects is 'ultra vires' and void, even if approved by all shareholders.")

divider()
sh("Articles of Association (AoA)")
c1,c2=st.columns(2)
with c1: card("📋 What is AoA?","The AoA is the internal rulebook of the company — it governs internal management, rights of shareholders, conduct of meetings, powers of directors, dividend policy, and more.<br><br>If a company does not register its own AoA, <strong>Schedule I (Table A)</strong> of the Act applies automatically as default regulations.")
with c2: card("🔧 Alteration of AoA","AoA can be altered by a <strong>Special Resolution</strong> passed at a general meeting, subject to:<br>• Must not conflict with the MoA or the Act<br>• Must not be illegal or fraudulent<br>• Must be for the benefit of the company as a whole<br>• Must not deprive minority shareholders of fundamental rights")

divider()
sh("MoA vs AoA — Key Differences")
st.markdown("""<table><tr><th>Aspect</th><th>Memorandum of Association</th><th>Articles of Association</th></tr>
<tr><td><strong>Nature</strong></td><td>Supreme/fundamental document</td><td>Subordinate to MoA</td></tr>
<tr><td><strong>Purpose</strong></td><td>Defines relationship with outside world</td><td>Governs internal management</td></tr>
<tr><td><strong>Alteration</strong></td><td>Very restricted — only as provided in Act</td><td>Can be altered by Special Resolution</td></tr>
<tr><td><strong>Binding on</strong></td><td>Company and outsiders dealing with it</td><td>Company and its members (internal only)</td></tr>
<tr><td><strong>Compulsory?</strong></td><td>Yes — must be filed</td><td>Optional (Schedule I applies if not filed)</td></tr>
<tr><td><strong>Ultra Vires</strong></td><td>Acts beyond MoA are void</td><td>Acts beyond AoA may be ratified</td></tr></table>""",unsafe_allow_html=True)

divider()
sh("Certificate of Incorporation")
law("Section 27 — On registration, the Registrar shall certify under his hand that the company is incorporated. The Certificate is CONCLUSIVE EVIDENCE of incorporation.")
c1,c2=st.columns(2)
with c1: card("📁 Documents Required for Registration","✔ Signed Memorandum of Association<br>✔ Signed Articles of Association<br>✔ Form I (Declaration of compliance)<br>✔ Form VI (Registered office)<br>✔ Form IX (Consent of directors)<br>✔ Form X (List of directors)<br>✔ Form XII (Particulars of directors)<br>✔ Registration fees<br>✔ Name clearance certificate")
with c2: card("✅ Effect of Incorporation","Once incorporated, the company:<br><br>🏢 Becomes a <strong>separate legal entity</strong><br>♾️ Has <strong>perpetual succession</strong><br>📜 Can <strong>sue and be sued</strong> in its own name<br>🏦 Can own property, enter contracts<br>🔒 Members have <strong>limited liability</strong><br>📋 Certificate is <strong>conclusive evidence</strong>")
tip("Conclusive Evidence Rule","Even if there were procedural errors in the registration process, the Certificate of Incorporation cannot be challenged by third parties.")

divider()
sh("🛠️ Interactive: Private or Public Company Checker")
q_members=st.slider("How many members/shareholders will your company have?",2,200,5)
q_public=st.selectbox("Will you invite the general public to subscribe for shares?",["No","Yes"])
q_transfer=st.selectbox("Will share transfers be restricted?",["Yes – restricted","No – freely transferable"])
if q_members<=50 and q_public=="No" and q_transfer=="Yes – restricted":
    ok(f"Based on your answers ({q_members} members, no public subscription, restricted transfers), this qualifies as a <strong>PRIVATE LIMITED COMPANY</strong>. Minimum 2 directors required.")
else:
    warn("Based on your answers, this will be a <strong>PUBLIC LIMITED COMPANY</strong>. Requirements: Minimum 7 subscribers, 3 directors, prospectus required for public share issue.")

divider()
sh("🧠 Test Your Knowledge")
q1=st.radio("1. Which document is considered the 'constitution' or supreme document of a company?",["Articles of Association","Memorandum of Association","Certificate of Incorporation","Prospectus"],index=None,key="m2q1")
if q1=="Memorandum of Association": ok("Correct! The MoA is the supreme/fundamental document defining the company's relationship with the outside world.")
elif q1: warn("Incorrect. The Memorandum of Association (MoA) is the supreme charter of the company.")

q2=st.radio("2. If a company does not register its Articles of Association, what applies?",["Company cannot be registered","MoA provisions apply instead","Schedule I (Table A) of the Act applies automatically","Company must adopt a standard AoA"],index=None,key="m2q2")
if q2=="Schedule I (Table A) of the Act applies automatically": ok("Correct! Schedule I (Table A) automatically applies as the default regulations if a company does not file its own AoA.")
elif q2: warn("Incorrect. Schedule I of the Act applies as default regulations when AoA is not registered.")

q3=st.radio("3. The Certificate of Incorporation is:",["Prima facie evidence of incorporation","Conclusive evidence of incorporation","Subject to challenge by creditors","Valid only for 5 years"],index=None,key="m2q3")
if q3=="Conclusive evidence of incorporation": ok("Correct! Under Section 27, the Certificate of Incorporation is conclusive evidence — it cannot be challenged even if procedural errors occurred.")
elif q3: warn("Incorrect. The Certificate is conclusive evidence under Section 27.")

recap(["The MoA has 6 mandatory clauses: Name, Registered Office, Objects, Liability, Capital, Subscription",
       "AoA governs internal management and can be altered by Special Resolution",
       "If no AoA is filed, Schedule I (Table A) automatically applies",
       "MoA is supreme — acts beyond MoA are ultra vires and void",
       "The Certificate of Incorporation is conclusive evidence of legal existence",
       "On incorporation, a company becomes a separate legal entity with perpetual succession"])
