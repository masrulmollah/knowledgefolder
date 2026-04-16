import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
.hero-banner { background: linear-gradient(135deg, #0a2e1a 0%, #1a5c38 50%, #2d8653 100%); padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem; border-left: 6px solid #4ade80; }
.hero-title { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 0 0 0.4rem 0; }
.hero-subtitle { font-size: 1.05rem; color: #bbf7d0; margin: 0; }
.hero-badge { display: inline-block; background: #4ade80; color: #0a2e1a; font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.7rem; border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase; }
.progress-container { background: #e9ecef; border-radius: 20px; height: 10px; margin: 0.3rem 0 0.5rem 0; }
.progress-bar { background: linear-gradient(90deg, #4ade80, #1a5c38); height: 10px; border-radius: 20px; width: 62.5%; }
.progress-label { font-size: 0.78rem; color: #6c757d; margin-bottom: 0.2rem; }
.stat-card { background: white; border: 1px solid #dee2e6; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.stat-number { font-size: 1.8rem; font-weight: 800; color: #1a5c38; }
.stat-label { font-size: 0.78rem; color: #6c757d; margin-top: 0.2rem; }
.finance-lens { background: linear-gradient(135deg, #fff3cd, #fff8e1); border: 1px solid #ffc107; border-left: 5px solid #f5a623; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.5rem 0; }
.finance-lens-title { font-size: 0.85rem; font-weight: 700; color: #856404; text-transform: uppercase; margin-bottom: 0.4rem; }
.finance-lens-body { font-size: 0.88rem; color: #5a4200; line-height: 1.6; }
.section-heading { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #4ade80; padding-bottom: 0.3rem; margin: 1.5rem 0 1rem 0; }
.app-card { background: white; border: 1px solid #e9ecef; border-left: 4px solid #1a5c38; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
.tool-badge { display: inline-block; background: #dcfce7; color: #1a5c38; border: 1px solid #86efac; border-radius: 12px; padding: 0.15rem 0.6rem; font-size: 0.75rem; font-weight: 600; margin: 0.15rem; }
.quiz-box { background: #f0fff4; border: 1px solid #86efac; border-radius: 12px; padding: 1.2rem 1.4rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">💚 Module 5 of 8 &nbsp;|&nbsp; AI Series</div>
  <div class="hero-title">AI Applications in Finance & Accounting</div>
  <div class="hero-subtitle">The applied centrepiece — explore how AI is transforming auditing,
  FP&A, tax, treasury, compliance, and reporting with real tools being used by top firms today.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-label">Series progress — Module 5 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="stat-card"><div class="stat-number">8</div><div class="stat-label">Finance Functions</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-card"><div class="stat-number">30+</div><div class="stat-label">Real AI Tools</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-card"><div class="stat-number">~40</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Quiz Questions</div></div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [("1","Foundations of AI",False),("2","Machine Learning Essentials",False),("3","Deep Learning & Neural Networks",False),("4","Generative AI & LLMs",False),("5","AI in Finance & Accounting",True),("6","Building AI Models",False),("7","AI Ethics, Risk & Governance",False),("8","Future of AI & Career Readiness",False)]
    for num, name, active in modules:
        st.markdown(f"**▶ M{num} — {name}** ✅" if active else f"M{num} — {name}")
    st.markdown("---")
    st.info("💡 This is the most practical module — map each application to your own role.")

# Function explorer
st.markdown('<div class="section-heading">🗺️ AI Across the Finance Function</div>', unsafe_allow_html=True)

finance_functions = {
    "📊 FP&A & Forecasting": {
        "intro": "AI is transforming Financial Planning & Analysis from backward-looking reporting to forward-looking intelligence.",
        "applications": [
            ("Driver-based forecasting", "ML models identify which business drivers (headcount, pipeline, macro indicators) best predict revenue and costs — replacing static budget templates.", "Workday Adaptive Planning, Anaplan, Oracle EPM"),
            ("Automated variance commentary", "LLMs read the numbers and generate plain-English explanations of actual vs budget variances for management reports.", "Microsoft Copilot, Pigment AI"),
            ("Scenario analysis at scale", "AI can run thousands of scenarios simultaneously — stress-testing P&L, balance sheet, and cash flow under different assumptions.", "Vena Solutions, Jedox"),
            ("Rolling forecast automation", "Models continuously update forecasts as new data arrives — replacing manual monthly replanning cycles.", "Anaplan, Board"),
        ],
        "tools": ["Anaplan", "Workday Adaptive", "Oracle EPM", "Pigment", "Vena", "Microsoft Copilot"],
    },
    "🔍 Audit & Assurance": {
        "intro": "AI is enabling auditors to move from sampling-based testing to continuous, population-wide analysis.",
        "applications": [
            ("Journal entry testing (100% population)", "ML models analyse the entire journal entry population — not just a sample — flagging entries with unusual characteristics (weekend postings, round amounts, unusual accounts).", "MindBridge AI Auditor, Galvanize"),
            ("Anomaly detection in AP/AR", "Unsupervised learning identifies outliers in payables and receivables — duplicate payments, ghost vendors, unusual approval patterns.", "AppZen, Oversight Systems"),
            ("Contract analysis", "LLMs extract key terms, obligations, and risk clauses from thousands of contracts in hours rather than weeks.", "Kira, Luminance, Harvey"),
            ("Continuous monitoring", "AI monitors financial data in real-time and alerts auditors when risk indicators exceed thresholds — enabling continuous auditing.", "ACL/Galvanize, CaseWare"),
        ],
        "tools": ["MindBridge", "AppZen", "Kira", "Luminance", "ACL/Galvanize", "CaseWare"],
    },
    "💳 Accounts Payable & Receivable": {
        "intro": "End-to-end automation of transactional finance processes — from invoice receipt to cash collection.",
        "applications": [
            ("Invoice processing automation", "CNN-based OCR reads invoices (any format, any layout), extracts fields, matches to POs, and routes for approval — with no manual data entry.", "ABBYY, Rossum, Hypatos, Kofax"),
            ("3-way match automation", "AI matches invoices to purchase orders and goods receipts automatically — flagging exceptions for human review only.", "SAP Intelligent RPA, Basware"),
            ("Predictive DSO management", "ML models predict which invoices will be paid late, enabling proactive collections. Models consider customer history, invoice age, amount, and economic conditions.", "Tesorio, HighRadius, Sidetrade"),
            ("Cash application", "AI auto-applies incoming payments to open receivables — even when remittances are ambiguous or incomplete.", "HighRadius, YayPay, Esker"),
        ],
        "tools": ["ABBYY", "Rossum", "HighRadius", "Tesorio", "SAP Intelligent RPA", "Esker"],
    },
    "💰 Treasury & Cash Management": {
        "intro": "AI enhances cash visibility, liquidity forecasting, and FX risk management across global treasuries.",
        "applications": [
            ("Cash flow forecasting", "LSTM-based models forecast daily/weekly cash positions across entities and currencies — far more accurate than spreadsheet extrapolations.", "Kyriba, GTreasury, Salmon"),
            ("FX exposure detection", "NLP models read contracts, purchase orders, and invoices to identify and quantify FX exposures before they appear on the balance sheet.", "FiREapps (now part of Kyriba)"),
            ("Liquidity stress testing", "AI simulates extreme scenarios (bank runs, supply chain shocks, currency crises) to test treasury resilience.", "Finastra, Murex"),
            ("Bank connectivity & reconciliation", "AI matches bank statement transactions to ledger entries at scale, handling complex formats across multiple banks and currencies.", "Kyriba, TreasuryXpress"),
        ],
        "tools": ["Kyriba", "GTreasury", "Salmon", "Finastra", "Murex"],
    },
    "🧾 Tax": {
        "intro": "AI is accelerating tax compliance, research, and planning — while managing the complexity of multi-jurisdiction requirements.",
        "applications": [
            ("Tax document classification", "ML models classify and extract data from thousands of tax documents (W-2s, 1099s, invoices) for automated data entry into tax returns.", "Thomson Reuters ONESOURCE, Avalara"),
            ("Transfer pricing benchmarking", "AI searches global databases of comparable transactions to identify arm's length pricing benchmarks — automating months of manual research.", "TP Catalyst (Bureau van Dijk), Duff & Phelps"),
            ("Tax research and interpretation", "LLMs assist tax professionals in researching complex tax questions across jurisdictions, summarising legislation and case law.", "Thomson Reuters CoCounsel, Bloomberg Tax"),
            ("Indirect tax compliance", "AI automates VAT/GST calculation, filing, and reconciliation across multiple jurisdictions with frequently changing rates and rules.", "Avalara, Vertex, Sovos"),
        ],
        "tools": ["ONESOURCE", "Avalara", "Vertex", "Bloomberg Tax", "Thomson Reuters CoCounsel"],
    },
    "🏦 Risk & Compliance": {
        "intro": "AI strengthens financial crime detection, regulatory compliance, and enterprise risk management.",
        "applications": [
            ("Anti-Money Laundering (AML)", "ML models analyse transaction patterns across accounts to detect structuring, layering, and other money laundering typologies with far fewer false positives than rule-based systems.", "NICE Actimize, Feedzai, ComplyAdvantage"),
            ("KYC document verification", "Computer vision verifies identity documents (passports, driving licences) and detects forgeries in seconds — dramatically speeding up customer onboarding.", "Jumio, Onfido, Trulioo"),
            ("Regulatory reporting automation", "AI extracts and transforms data from source systems into regulatory report formats (COREP, FINREP, MAS 610) — reducing manual effort and error risk.", "Axiom, Wolters Kluwer OneSumX"),
            ("Credit risk scoring", "Gradient boosting models provide real-time credit decisions, incorporating bureau data, transactional history, and alternative data sources.", "FICO, Experian, Zest AI"),
        ],
        "tools": ["NICE Actimize", "Feedzai", "Jumio", "FICO", "Zest AI", "Wolters Kluwer"],
    },
    "📈 Investment Management": {
        "intro": "AI is reshaping investment research, portfolio management, and trade execution across asset classes.",
        "applications": [
            ("NLP-driven research", "LLMs summarise earnings calls, analyse sentiment in news and filings, and extract forward guidance — processing thousands of documents daily.", "Kensho (S&P), Bloomberg AI, AlphaSense"),
            ("Alternative data analysis", "ML processes satellite imagery (retail car park occupancy, shipping container movements), web scraping, and credit card data to generate unique investment signals.", "Orbital Insight, YipitData, Eagle Alpha"),
            ("Algorithmic trading", "Reinforcement learning agents and ML models execute trades at optimal prices, minimising market impact and slippage.", "Two Sigma, Renaissance Technologies, Citadel"),
            ("ESG data scoring", "NLP models extract ESG metrics from sustainability reports, news, and regulatory filings to generate standardised ESG scores.", "MSCI ESG, Sustainalytics, Arabesque S-Ray"),
        ],
        "tools": ["Bloomberg AI", "AlphaSense", "Kensho", "MSCI ESG", "Orbital Insight"],
    },
    "📋 Financial Reporting": {
        "intro": "AI is streamlining the financial close, reporting, and disclosure process.",
        "applications": [
            ("Close process automation", "AI orchestrates the financial close — automatically running reconciliations, journal entries, and eliminations in sequence.", "BlackLine, Trintech Cadency, SAP Financial Close"),
            ("Disclosure drafting", "LLMs draft MD&A sections, notes to accounts, and regulatory disclosures from structured financial data — significantly reducing drafting time.", "Workiva AI, Diligent"),
            ("XBRL tagging", "AI automates the tagging of financial statements with XBRL taxonomy codes for regulatory filing — a time-consuming manual task.", "Workiva, Novasoft"),
            ("Report summarisation", "LLMs condense lengthy annual reports, board packs, and management accounts into executive summaries with key metrics highlighted.", "Microsoft Copilot, Claude, Gemini"),
        ],
        "tools": ["BlackLine", "Workiva", "SAP Financial Close", "Trintech", "Microsoft Copilot"],
    },
}

selected_function = st.selectbox("🔍 Explore AI applications by finance function:", list(finance_functions.keys()))
func_data = finance_functions[selected_function]
st.markdown(f"*{func_data['intro']}*")
st.markdown("**Key Tools:**")
st.markdown(" ".join([f'<span class="tool-badge">{t}</span>' for t in func_data["tools"]]), unsafe_allow_html=True)
st.markdown("")
for app_name, desc, tools in func_data["applications"]:
    st.markdown(f"""
    <div class="app-card">
    <b>{app_name}</b><br>
    <span style="font-size:0.87rem">{desc}</span><br>
    <span style="font-size:0.78rem;color:#1a5c38">🛠️ Tools: {tools}</span>
    </div>
    """, unsafe_allow_html=True)

# AI Impact by role
st.markdown('<div class="section-heading">👥 AI Impact by Finance Role</div>', unsafe_allow_html=True)
with st.expander("📊 Which Roles Are Most Affected?"):
    import pandas as pd
    df = pd.DataFrame({
        "Role": ["Financial Accountant", "Management Accountant", "FP&A Analyst", "Internal Auditor", "Tax Specialist", "Treasury Analyst", "CFO", "Finance Director"],
        "Tasks AI Automates": ["Reconciliations, journal entries, report generation", "Variance analysis drafting, standard cost updates", "Budget consolidation, scenario modelling", "Control testing, sampling, documentation", "Document classification, data entry, research", "Cash forecasting, bank reconciliation", "Board report preparation, data aggregation", "Financial close monitoring, reporting"],
        "Tasks AI Enhances": ["Anomaly detection, trend analysis", "Business partnering with AI-generated insights", "Driver analysis, rolling forecasts", "100% population testing, pattern recognition", "Multi-jurisdiction compliance, planning", "FX exposure management, liquidity optimisation", "Real-time performance dashboards", "Risk monitoring, strategic planning support"],
        "AI Impact Level": ["High", "High", "High", "Very High", "Medium-High", "Medium-High", "Medium", "Medium"],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — The Right Perspective</div>
      <div class="finance-lens-body">
        AI automates tasks, not roles. A financial accountant who uses AI reconciliation tools doesn't lose
        their job — they gain time for analysis, business partnering, and advisory work. The risk is not
        "AI takes my job" but rather "a finance professional using AI becomes more valuable than one who doesn't."
      </div>
    </div>
    """, unsafe_allow_html=True)

# Tool Landscape
st.markdown('<div class="section-heading">🛠️ The Finance AI Tool Landscape</div>', unsafe_allow_html=True)
with st.expander("📦 Platform Tools vs Specialist AI Tools"):
    tab1, tab2 = st.tabs(["🏢 Platform / Integrated", "🔬 Specialist AI Tools"])
    with tab1:
        tools = [("Microsoft 365 Copilot", "AI across Excel, Word, Teams, Outlook, PowerPoint.", "Drafting board papers, analysing data in Excel, summarising emails."),("SAP Joule", "AI assistant embedded in SAP ERP, S/4HANA, and SuccessFactors.", "Natural language queries to SAP data, workflow automation."),("Oracle AI", "AI features across Oracle ERP Cloud, EPM, and Analytics.", "Intelligent process automation, anomaly detection in financials."),("Workday AI", "AI in Workday Financial Management and HCM.", "Expense anomaly detection, financial forecasting."),("Xero Analytics Plus", "AI-driven cash flow insights for SME accounting.", "Short-term cash flow forecasting, payment timing prediction."),]
        for name, desc, use in tools:
            st.markdown(f"**{name}** — {desc}")
            st.caption(f"💼 Finance use: {use}")
            st.divider()
    with tab2:
        tools2 = [("MindBridge AI Auditor", "AI risk scoring for 100% of journal entries and transactions.", "Journal entry testing, continuous auditing."),("AppZen", "AI for expense report auditing and AP compliance.", "Real-time expense policy compliance checking."),("HighRadius", "AI for order-to-cash and treasury management.", "Cash application, collections, cash forecasting."),("Kyriba", "Treasury management with AI cash flow forecasting.", "Multi-currency cash management, FX risk."),("Alteryx", "Data prep and ML without heavy coding.", "Financial data automation, self-service analytics."),("Workiva", "AI-powered connected reporting and compliance.", "Financial reporting, XBRL, ESG reporting."),]
        for name, desc, use in tools2:
            st.markdown(f"**{name}** — {desc}")
            st.caption(f"💼 Finance use: {use}")
            st.divider()

# Case Study
st.markdown('<div class="section-heading">📖 Case Study: AI-Powered Financial Close</div>', unsafe_allow_html=True)
with st.expander("🏭 From 10-Day Close to 3-Day Close with AI"):
    st.markdown("""
    **Scenario:** A multinational manufacturing company with 40 subsidiaries, closing in 5 currencies.

    **Before AI (Traditional Close — 10 days):**
    - Day 1–3: Collect data from subsidiaries manually via spreadsheet templates
    - Day 4–5: Consolidate and reconcile intercompany balances (manual matching)
    - Day 6–7: Run eliminations, adjustments, foreign currency translation (manual)
    - Day 8–9: Prepare management accounts and variance commentary (manual writing)
    - Day 10: CFO review and sign-off

    **After AI Implementation (3-Day Close):**

    | Step | AI Solution | Time Saving |
    |------|------------|-------------|
    | Data collection | SAP S/4HANA automates sub-ledger to GL posting | Saves 3 days |
    | Intercompany matching | BlackLine AI automatically matches IC balances, flags exceptions | Saves 1.5 days |
    | FX translation | Automated in ERP with real-time rates | Saves 0.5 days |
    | Variance commentary | Microsoft Copilot drafts initial commentary from data | Saves 0.5 days |
    | Board report | AI-assembled from live data with executive summary | Saves 0.5 days |

    **Result:** Finance team redirected from data processing to business partnering, scenario analysis,
    and forward-looking insight generation. CFO gets preliminary results on Day 2 instead of Day 8.
    """)
    st.success("💡 **Key lesson:** AI doesn't eliminate the close — it eliminates the manual data handling that dominated it. Human judgment remains essential for exceptions, adjustments, and interpretation.")

# Quiz
st.markdown('<div class="section-heading">🧩 Knowledge Check</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {"q": "An internal audit team uses AI to analyse 100% of journal entries rather than a 5% sample. This is an example of:", "options": ["Predictive modelling", "Continuous auditing enabled by ML anomaly detection", "Reinforcement learning", "Generative AI for audit reports"], "answer": "Continuous auditing enabled by ML anomaly detection", "explanation": "ML models can process millions of journal entries to flag anomalies — enabling full population testing rather than sampling. Tools like MindBridge AI Auditor use this approach."},
    {"q": "A treasury team wants to predict which customers will pay their invoices late. The MOST appropriate AI approach is:", "options": ["Unsupervised clustering", "Supervised classification using historical payment data", "Reinforcement learning agent", "Autoencoder anomaly detection"], "answer": "Supervised classification using historical payment data", "explanation": "Predicting late payment (paid late vs not) is a binary classification problem. Supervised learning trains on historical invoices with known outcomes to predict new invoices."},
    {"q": "Which of the following AI tools is specifically designed for AP invoice processing automation?", "options": ["MindBridge", "ABBYY / Rossum", "Kyriba", "AlphaSense"], "answer": "ABBYY / Rossum", "explanation": "ABBYY and Rossum are specialist AI tools for invoice data capture and extraction — using computer vision and NLP to read invoices in any format."},
    {"q": "An AML compliance team replaces its rule-based transaction monitoring with an ML model. The main expected benefit is:", "options": ["The model requires no ongoing maintenance", "Fewer false positives while detecting more complex money laundering patterns", "Regulators prefer ML to rule-based systems", "The model can replace human compliance officers entirely"], "answer": "Fewer false positives while detecting more complex money laundering patterns", "explanation": "ML-based AML models learn complex typologies that rules miss, and produce significantly fewer false positives than rule-based systems — reducing alert fatigue for compliance teams."},
    {"q": "A CFO asks whether AI can fully automate the financial close process. The most accurate response is:", "options": ["Yes — AI can fully automate the entire close with no human involvement", "No — AI has no role in the close process", "AI automates the data processing and routine tasks; human judgment remains essential for exceptions and interpretation", "AI can only help with the board report, not the close itself"], "answer": "AI automates the data processing and routine tasks; human judgment remains essential for exceptions and interpretation", "explanation": "AI dramatically accelerates data collection, matching, and report generation — but human judgment is essential for unusual items, policy decisions, and board-level communication."},
]

for key in ["m5_q_index","m5_score","m5_answered","m5_selected","m5_quiz_done"]:
    if key not in st.session_state: st.session_state[key] = 0 if "index" in key or "score" in key else False

if not st.session_state.m5_quiz_done:
    q_data = questions[st.session_state.m5_q_index]
    st.markdown(f"**Question {st.session_state.m5_q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")
    choice = st.radio("Select your answer:", q_data["options"], key=f"m5_q_{st.session_state.m5_q_index}")
    col_s, col_n = st.columns(2)
    with col_s:
        if st.button("✅ Submit", key=f"m5_sub_{st.session_state.m5_q_index}"):
            st.session_state.m5_answered = True; st.session_state.m5_selected = choice
            if choice == q_data["answer"]: st.session_state.m5_score += 1
    if st.session_state.m5_answered:
        if st.session_state.m5_selected == q_data["answer"]: st.success(f"✅ Correct! {q_data['explanation']}")
        else: st.error(f"❌ Answer: **{q_data['answer']}** — {q_data['explanation']}")
        with col_n:
            if st.session_state.m5_q_index < len(questions)-1:
                if st.button("Next ➡️", key=f"m5_next_{st.session_state.m5_q_index}"):
                    st.session_state.m5_q_index += 1; st.session_state.m5_answered = False; st.rerun()
            else:
                if st.button("🏁 Results"): st.session_state.m5_quiz_done = True; st.rerun()
else:
    s,t = st.session_state.m5_score, len(questions); pct = int((s/t)*100)
    st.markdown(f"### {'🏆' if pct>=80 else '👍' if pct>=60 else '📚'} Score: {s}/{t} ({pct}%)")
    st.progress(pct/100)
    st.info("Excellent!" if pct>=80 else "Good — review the application areas." if pct>=60 else "Revisit the finance function applications.")
    if st.button("🔄 Retry"):
        for k,v in [("m5_q_index",0),("m5_score",0),("m5_answered",False),("m5_selected",None),("m5_quiz_done",False)]: st.session_state[k]=v
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">💡 Key Takeaways</div>', unsafe_allow_html=True)
for i,t in enumerate(["AI is already embedded in major finance platforms — SAP Joule, Oracle AI, Workday AI, Microsoft Copilot — finance professionals don't need to build from scratch.","**Audit** sees the biggest transformation — 100% population testing replaces sampling; AI fraud detection catches patterns humans miss.","**AP/AR automation** delivers rapid, measurable ROI — invoice processing AI eliminates manual data entry and accelerates cash cycles.","**FP&A** shifts from backward-looking reporting to real-time, AI-driven forecasting and scenario analysis.","**AML and KYC** AI reduces false positives dramatically — enabling compliance teams to focus on genuine risk rather than alert fatigue.","AI automates **tasks within roles**, not roles themselves — finance professionals who adopt AI become significantly more valuable."],1):
    st.markdown(f"**{i}.** {t}")

st.markdown("---")
col1,col2,col3 = st.columns(3)
with col1:
    if st.button("⬅️ M4: Generative AI", use_container_width=True): st.info("Navigate to Module 4 from the sidebar.")
with col2: st.markdown("<div style='text-align:center;padding-top:0.4rem'>💚 Module 5 of 8</div>", unsafe_allow_html=True)
with col3:
    if st.button("M6: Building AI Models ➡️", use_container_width=True): st.info("Navigate to Module 6 from the sidebar.")
st.caption("Knowledge Folder · AI Series · Module 5 — AI in Finance & Accounting · © 2025")