"""
Machine Learning for Finance & Accounts
Module 10 – Advanced ML & Future of Finance

USAGE: import ml_module_10; ml_module_10.show()
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#312E81"; SECONDARY="#6366F1"; SUCCESS="#10B981"; WARNING="#F59E0B"; DANGER="#EF4444"
GOLD="#B45309"; PINK="#DB2777"


def _css():
    st.markdown("""
    <style>
    .main { background:#EEF2FF; }
    .hero-banner { background:linear-gradient(135deg,#312E81 0%,#6366F1 50%,#A855F7 80%,#EC4899 100%);
        border-radius:16px; padding:2.4rem 2.8rem; color:white; margin-bottom:1.6rem; }
    .hero-banner h1 { font-size:2.1rem; margin:0 0 .4rem; font-weight:700; }
    .hero-banner p  { font-size:1.05rem; margin:0; opacity:.9; }
    .hero-badge { display:inline-block; background:rgba(255,255,255,.2);
        border:1px solid rgba(255,255,255,.35); border-radius:20px;
        padding:.18rem .8rem; font-size:.8rem; margin-bottom:.7rem; }
    .section-title { font-size:1.35rem; font-weight:700; color:#1E293B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #312E81; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .info-card .card-icon { font-size:1.7rem; margin-bottom:.4rem; }
    .info-card h4 { font-size:1rem; font-weight:700; color:#1E293B; margin:0 0 .3rem; }
    .info-card p  { font-size:.88rem; color:#475569; margin:0; line-height:1.55; }
    .definition-box { background:#E0E7FF; border-left:5px solid #312E81;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    .definition-box p { margin:0; color:#1E293B; font-size:.96rem; line-height:1.65; }
    .future-card { background:white; border-radius:12px; padding:1.3rem 1.5rem;
        border-top:4px solid; box-shadow:0 2px 8px rgba(0,0,0,.07); margin-bottom:1rem; }
    .roadmap-step { background:white; border-radius:10px; padding:1rem 1.2rem;
        border-left:4px solid #6366F1; margin-bottom:.7rem;
        box-shadow:0 1px 4px rgba(0,0,0,.06); }
    .quiz-box { background:white; border-radius:12px; padding:1.4rem 1.6rem;
        box-shadow:0 2px 10px rgba(0,0,0,.08); margin-top:1rem; }
    .quiz-q { font-weight:700; color:#1E293B; font-size:1rem; margin-bottom:.8rem; }
    .completion-banner { background:linear-gradient(135deg,#065F46,#059669);
        border-radius:16px; padding:2rem 2.5rem; color:white; text-align:center; margin-top:2rem; }
    .completion-banner h2 { font-size:1.8rem; margin:0 0 .5rem; }
    .completion-banner p  { font-size:1rem; margin:0; opacity:.9; }
    </style>""", unsafe_allow_html=True)


def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 10 — Advanced ML &amp; The Future of Finance</h1>
      <p>Deep learning, Generative AI, LLMs in finance, the evolving role of the
         finance professional, and your personalised learning roadmap.</p>
    </div>""", unsafe_allow_html=True)
    for col,(icon,label,val) in zip(st.columns(4),[
        ("🚀","Level","Advanced / Strategic"),("⏱️","Read time","~40 minutes"),
        ("📋","Topics","Deep Learning, GenAI, LLMs, Roadmap"),("🏆","Outcome","Future-proof your career"),
    ]):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""", unsafe_allow_html=True)


def _section_deep_learning():
    st.markdown('<div class="section-title">🧠 1. Deep Learning — Neural Networks Explained</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Deep Learning</strong> uses neural networks with many layers (hence "deep")
      to automatically learn complex patterns. It excels at images, speech, and text —
      and increasingly at complex financial signals like options pricing, document understanding,
      and real-time risk assessment.</p>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("""
        **How a neural network works:**
        1. Input layer receives features (transaction data, text, images)
        2. Hidden layers transform features through weighted connections
        3. Each neuron applies an activation function (non-linearity)
        4. Output layer produces prediction (fraud/no fraud, amount, category)
        5. Training adjusts all weights via backpropagation

        **When does Deep Learning beat traditional ML in finance?**
        - Very large datasets (millions of transactions)
        - Complex sequential data (tick-by-tick market data)
        - Unstructured inputs (document images, audio)
        - Patterns too complex for hand-crafted features
        """)
    with col2:
        # Neural network diagram using plotly
        layers = [
            ("Input\n(Features)", 6, "#3B82F6"),
            ("Hidden\nLayer 1", 8, "#8B5CF6"),
            ("Hidden\nLayer 2", 6, "#A855F7"),
            ("Output\n(Prediction)", 2, "#10B981"),
        ]
        fig = go.Figure()
        positions = {}
        for li, (name, n, color) in enumerate(layers):
            x = li * 2
            ys = np.linspace(0, n-1, n) - (n-1)/2
            for i, y in enumerate(ys):
                positions[(li, i)] = (x, y)
                fig.add_shape(type="circle", x0=x-0.15, y0=y-0.15, x1=x+0.15, y1=y+0.15,
                              fillcolor=color, line_color="white", line_width=1)
            if li > 0:
                prev_n = layers[li-1][1]
                prev_ys = np.linspace(0, prev_n-1, prev_n) - (prev_n-1)/2
                for py in prev_ys[:3]:
                    for cy in ys[:3]:
                        fig.add_shape(type="line",
                                      x0=(li-1)*2+0.15, y0=py, x1=x-0.15, y1=cy,
                                      line=dict(color="rgba(100,100,200,0.15)", width=0.5))
            mid = (ys[0] + ys[-1]) / 2
            fig.add_annotation(x=x, y=mid - n/2 - 0.7, text=name, showarrow=False,
                                font=dict(size=10, color="#475569"), align="center")
        fig.update_layout(height=320, paper_bgcolor="rgba(0,0,0,0)",
                          margin=dict(t=20,b=40,l=20,r=20),
                          xaxis=dict(visible=False, range=[-0.5, 6.5]),
                          yaxis=dict(visible=False, range=[-5, 5]))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### 🏦 Deep Learning in finance — specific applications")
    dl_apps = [
        ("LSTM Networks","Time series","Stock/FX price prediction, fraud velocity detection"),
        ("CNNs","Pattern recognition","Chart pattern recognition, document image classification"),
        ("Transformers","Sequence modelling","Earnings call analysis, contract review"),
        ("Autoencoders","Anomaly detection","Unusual transaction patterns, insider trading signals"),
    ]
    df = pd.DataFrame(dl_apps, columns=["Architecture","Best for","Finance application"])
    st.dataframe(df, use_container_width=True, hide_index=True)


def _section_genai():
    st.markdown('<div class="section-title">🤖 2. Generative AI & LLMs in Finance</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Large Language Models (LLMs)</strong> like GPT-4, Claude, and Gemini are trained
      on vast amounts of text. They can read, summarise, explain, generate, and answer questions
      about financial documents — transforming how finance teams handle unstructured information.</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📋 What LLMs Can Do","💼 Finance Use Cases","⚠️ Risks & Limitations"])
    with tab1:
        capabilities = [
            ("📖","Read & Summarise","Condense 200-page annual reports to executive summaries in seconds."),
            ("❓","Answer Questions","Query financial documents: 'What were the top 3 revenue risks mentioned in the 10-K?'"),
            ("✍️","Draft Content","Generate first drafts of board commentary, variance analysis, and management reports."),
            ("🔄","Transform Data","Convert unstructured text (contracts, emails) into structured data tables."),
            ("💬","Explain Decisions","Translate ML model outputs into plain English for non-technical stakeholders."),
            ("🔍","Extract & Classify","Pull specific data points from thousands of documents simultaneously."),
        ]
        cols = st.columns(3)
        for i, (icon, title, desc) in enumerate(capabilities):
            with cols[i%3]:
                st.markdown(f"""<div class="info-card" style="margin-bottom:1rem">
                  <div class="card-icon">{icon}</div>
                  <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    with tab2:
        use_cases = pd.DataFrame({
            "Finance Function": ["Accounts Payable","Financial Reporting","Audit","Tax","Treasury","Investor Relations"],
            "LLM Application": [
                "Auto-draft vendor responses, explain invoice discrepancies",
                "Generate board commentary, variance explanations, MD&A drafts",
                "Summarise audit findings, generate management letter points",
                "Review tax legislation, flag changes affecting provisions",
                "Analyse FX hedging reports, summarise covenant documentation",
                "Monitor analyst report sentiment, draft Q&A preparation",
            ],
            "Time Saved": ["2–3 hrs/day","5–8 hrs/month","3–4 hrs/audit","4–6 hrs/quarter","2–3 hrs/week","8–10 hrs/quarter"],
        })
        st.dataframe(use_cases, use_container_width=True, hide_index=True)

    with tab3:
        st.error("""
        **Critical limitations of LLMs in finance:**
        - 🚫 **Hallucination:** LLMs can confidently state incorrect numbers or facts — NEVER use for financial calculations without verification
        - 📅 **Knowledge cutoff:** Training data has a cutoff date — LLMs don't know recent events
        - 🔒 **Data privacy:** Never input confidential financial data into public LLMs without checking your firm's policy
        - ⚖️ **Regulatory compliance:** LLM outputs may not meet disclosure or sign-off requirements without human review
        - 📊 **No real-time data:** LLMs don't have live market prices, exchange rates, or current financial statements
        """)
        st.success("✅ **Best practice:** Use LLMs for drafting, summarising, and explaining — not for final numbers or regulatory filings without human review and sign-off.")


def _section_fintech_tools():
    st.markdown('<div class="section-title">🏢 3. ML in Finance Software — Tools You May Already Have</div>', unsafe_allow_html=True)

    tools_data = [
        ("🟢", "SAP S/4HANA", "Built-in ML for cash flow forecasting, payment behaviour prediction, and intelligent G/L account assignment."),
        ("🔵", "Microsoft Dynamics 365", "AI-powered collections, cash flow forecasting, customer churn prediction, and automated invoice processing."),
        ("🟡", "Oracle NetSuite", "Intelligent transaction matching, anomaly detection in expenses, and automated approval workflows."),
        ("💚", "Xero & QuickBooks", "Automated bank reconciliation, expense categorisation, and cash flow predictions for SMEs."),
        ("🟠", "Workday Adaptive", "AI-driven budgeting and forecasting, with automated variance explanations."),
        ("🔴", "SAP Concur", "ML-powered expense audit: flags policy violations, duplicates, and unusual claim patterns automatically."),
    ]
    for i in range(0, len(tools_data), 2):
        cols = st.columns(2)
        for col, (icon, name, desc) in zip(cols, tools_data[i:i+2]):
            col.markdown(f"""<div class="info-card" style="margin-bottom:1rem;border-left:4px solid #6366F1">
              <h4>{icon} {name}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

    st.info("💡 **Key insight for finance professionals:** You likely already have ML available in your existing software. "
            "Start by exploring the AI/ML features already licensed in your current ERP and finance tools before evaluating new platforms.")


def _section_future_roles():
    st.markdown('<div class="section-title">👔 4. The Evolving Role of Finance Professionals</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Tasks ML will automate (reducing time spent):**")
        automating = ["Manual data entry and reconciliation","Routine variance analysis write-ups",
                      "Standard report generation","Invoice processing and GL coding",
                      "Basic compliance checking","Data extraction from documents"]
        for t in automating:
            st.markdown(f"⬇️ {t}")

    with col2:
        st.markdown("**Skills that become MORE valuable:**")
        growing = ["Interpreting and challenging ML model outputs","Defining the right business problems for ML",
                   "Ethical oversight and governance of AI","Stakeholder communication of data-driven insights",
                   "Strategic decision-making from ML-enhanced analysis","Change management for AI adoption"]
        for t in growing:
            st.markdown(f"⬆️ {t}")

    st.markdown("#### 📊 Finance role evolution timeline")
    timeline_data = {
        "Year": ["2020","2022","2024","2026","2028","2030"],
        "Manual work (%)": [70, 60, 45, 30, 20, 12],
        "Analysis & judgement (%)": [20, 28, 38, 48, 55, 58],
        "AI oversight & strategy (%)": [10, 12, 17, 22, 25, 30],
    }
    df_t = pd.DataFrame(timeline_data)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_t["Year"], y=df_t["Manual work (%)"], fill="tozeroy",
                             name="Manual/routine", line=dict(color=DANGER), fillcolor="rgba(239,68,68,0.15)"))
    fig.add_trace(go.Scatter(x=df_t["Year"], y=df_t["Analysis & judgement (%)"], fill="tozeroy",
                             name="Analysis & judgement", line=dict(color=WARNING), fillcolor="rgba(245,158,11,0.15)"))
    fig.add_trace(go.Scatter(x=df_t["Year"], y=df_t["AI oversight & strategy (%)"], fill="tozeroy",
                             name="AI oversight & strategy", line=dict(color=SUCCESS), fillcolor="rgba(16,185,129,0.15)"))
    fig.update_layout(title="Finance professional time allocation — projected shift",
                      height=300, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=35,b=10,l=10,r=10),
                      xaxis=dict(gridcolor="#E2E8F0"),
                      yaxis=dict(gridcolor="#E2E8F0", title="% of working time"),
                      legend=dict(x=0,y=1))
    st.plotly_chart(fig, use_container_width=True)


def _section_roadmap():
    st.markdown('<div class="section-title">🗺️ 5. Your Personal Learning Roadmap</div>', unsafe_allow_html=True)
    st.markdown("Based on your goals, here is a structured path to build your ML capabilities:")

    goal = st.selectbox("What is your primary goal?", [
        "🤔 Just want to understand what ML is (awareness)",
        "💼 Use ML tools in my current finance role",
        "🛠️ Build basic ML models for my team",
        "🚀 Become a Finance Data Scientist",
    ])

    roadmaps = {
        "🤔 Just want to understand what ML is (awareness)": [
            ("✅ Complete","Modules 1–2: Concepts and data fundamentals"),
            ("✅ Complete","Module 7: Real finance applications"),
            ("📌 Recommended","Module 6: NLP (very relevant to daily reading)"),
            ("🔖 Optional","Module 9: Ethics — important for governance roles"),
        ],
        "💼 Use ML tools in my current finance role": [
            ("✅ Complete","Modules 1–7: Full conceptual foundation"),
            ("📌 Recommended","Explore ML features in your ERP (SAP, Oracle, Xero)"),
            ("📌 Recommended","Complete Microsoft Power BI AI features training"),
            ("🔖 Optional","Module 8: Build a simple model in Excel + Azure ML"),
        ],
        "🛠️ Build basic ML models for my team": [
            ("✅ Complete","All 10 modules"),
            ("📌 Next","Learn Python basics: 4-week free course on Coursera"),
            ("📌 Next","Complete scikit-learn official tutorial"),
            ("📌 Next","Build the late payment model from Module 8 on your own data"),
            ("🔖 Advanced","Google Machine Learning Crash Course (free)"),
        ],
        "🚀 Become a Finance Data Scientist": [
            ("✅ Complete","All 10 modules — solid conceptual foundation"),
            ("📌 Next","Python for Data Science (Coursera specialisation)"),
            ("📌 Next","Kaggle: complete 5 tabular data competitions"),
            ("📌 Next","CFA Institute Certificate in ESG Investing or CDMP"),
            ("🔖 Advanced","Deep Learning Specialisation — Andrew Ng (Coursera)"),
            ("🔖 Advanced","MLOps fundamentals — deploying models to production"),
        ],
    }

    steps = roadmaps.get(goal, [])
    for status, step in steps:
        color = "#065F46" if "✅" in status else "#1E3A5F" if "📌" in status else "#6B7280"
        bg = "#D1FAE5" if "✅" in status else "#DBEAFE" if "📌" in status else "#F3F4F6"
        st.markdown(f"""<div class="roadmap-step" style="border-left-color:{color};background:{bg}">
          <span style="font-weight:700;color:{color}">{status}</span>
          <span style="color:#1E293B;margin-left:.5rem">{step}</span></div>""",
          unsafe_allow_html=True)


def _section_stay_current():
    st.markdown('<div class="section-title">📰 6. Staying Current in ML for Finance</div>', unsafe_allow_html=True)
    resources = [
        ("📰","Publications","FT, Bloomberg, The Economist — ML coverage in Finance section"),
        ("🎓","Free Courses","Coursera ML Specialisation, Google ML Crash Course, fast.ai"),
        ("📊","Kaggle","Free datasets + competitions — practice with real data"),
        ("🤝","Communities","AICPA Technology Advisory, IMA Digital Finance, FinTech meetups"),
        ("📚","Books","'Advances in Financial ML' (Lopez de Prado), 'Machine Learning for Asset Managers'"),
        ("🔬","Research","arXiv (cs.LG), SSRN Finance papers, Federal Reserve research"),
    ]
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(resources):
        with cols[i%3]:
            st.markdown(f"""<div class="info-card" style="margin-bottom:1rem">
              <div class="card-icon">{icon}</div>
              <h4>{title}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)


def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 10 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q":"Q1. Which deep learning architecture is best suited for sequential financial data like daily stock prices or monthly revenue?",
         "opts":["Convolutional Neural Network (CNN)","LSTM (Long Short-Term Memory)","Autoencoder","Random Forest"],
         "ans":"LSTM (Long Short-Term Memory)",
         "exp":"✅ Correct! LSTMs are designed for sequential data and excel at capturing long-term dependencies in time series — perfect for financial sequences."},
        {"q":"Q2. A finance team wants to use an LLM to automatically answer questions about their company's annual report. What is the most important risk to manage?",
         "opts":["Model overfitting","LLM hallucination — generating plausible but incorrect figures","Class imbalance","Slow processing speed"],
         "ans":"LLM hallucination — generating plausible but incorrect figures",
         "exp":"✅ Correct! LLMs can confidently state wrong financial figures. All LLM outputs used in financial reporting must be verified against source documents."},
        {"q":"Q3. As ML automates more routine accounting tasks, which skill becomes MORE valuable for finance professionals?",
         "opts":["Manual data entry","Interpreting, challenging and governing ML model outputs","Preparing standard journal entries","Filing paper-based expense reports"],
         "ans":"Interpreting, challenging and governing ML model outputs",
         "exp":"✅ Correct! The finance professional of the future will spend less time on routine tasks and more time applying judgement, overseeing AI, and communicating insights."},
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("", q["opts"], key=f"mod10_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"❌ Correct answer: **{q['ans']}**\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True); st.markdown("")

    answered = sum(1 for i in range(3) if st.session_state.get(f"mod10_q{i}") is not None)
    if answered == 3:
        score = sum(1 for i, q in enumerate(questions)
                    if st.session_state.get(f"mod10_q{i}") == q["ans"])
        if score == 3:
            st.balloons()


def _completion():
    st.markdown("""
    <div class="completion-banner">
      <h2>🎓 Congratulations! You've completed all 10 modules.</h2>
      <p>You now have a comprehensive understanding of Machine Learning for Finance & Accounts —
         from core concepts to advanced AI, from data preparation to model deployment,
         and from practical applications to ethical governance.</p>
      <p style="margin-top:1rem;font-weight:700">
        You understand ML · You can apply ML · You can build ML models · You can govern ML responsibly
      </p>
    </div>""", unsafe_allow_html=True)

    st.markdown("### 📊 Your learning journey — complete")
    modules = [f"M{i}" for i in range(1, 11)]
    completed = [100] * 10
    fig = go.Figure(go.Bar(x=modules, y=completed,
                           marker_color=[f"hsl({i*25},70%,45%)" for i in range(10)],
                           text=["✓"]*10, textposition="inside",
                           textfont=dict(color="white", size=14)))
    fig.update_layout(height=160, paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=10,b=10,l=10,r=10),
                      yaxis=dict(visible=False), xaxis=dict(gridcolor="#E2E8F0"),
                      showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 ML for Finance & Accounts** · Module 10 of 10")
    c2.markdown("<div style='text-align:center'><a href='?module=9' style='color:#312E81'>◀ Module 9</a>"
                " &nbsp;|&nbsp; <span style='color:#059669'>✅ Course Complete!</span></div>",
                unsafe_allow_html=True)
    c3.markdown("<div style='text-align:right;color:#64748B;font-size:.85rem'>Knowledge Folder</div>",
                unsafe_allow_html=True)


def show():
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 10 — Sections")
        st.markdown("1. Deep Learning\n2. Generative AI & LLMs\n3. ML in Finance Software\n"
                    "4. Evolving Finance Roles\n5. Personal Roadmap\n6. Stay Current\n---\n🧩 Quiz")
        st.progress(100, text="Module 10 / 10 ✅")
    _section_deep_learning(); st.markdown("")
    _section_genai(); st.markdown("")
    _section_fintech_tools(); st.markdown("")
    _section_future_roles(); st.markdown("")
    _section_roadmap(); st.markdown("")
    _section_stay_current(); st.markdown("")
    _knowledge_check(); st.markdown("")
    _completion(); _footer()


if __name__ == "__main__":
    st.set_page_config(page_title="Module 10 – Advanced ML & Future | Knowledge Folder",
                       page_icon="🚀", layout="wide")
    show()