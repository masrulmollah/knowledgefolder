import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY = "#0F766E"; SECONDARY = "#14B8A6"; ACCENT = "#6366F1"
SUCCESS = "#10B981"; WARNING = "#F59E0B"; DANGER = "#EF4444"

def _css():
    st.markdown("""
    <style>
    .main { background: #F0FDFA; }
    .hero-banner {
        background: linear-gradient(135deg, #0F766E 0%, #0D9488 60%, #6366F1 100%);
        border-radius: 16px; padding: 2.4rem 2.8rem; color: white; margin-bottom: 1.6rem;
    }
    .hero-banner h1 { font-size: 2.1rem; margin: 0 0 .4rem; font-weight: 700; }
    .hero-banner p  { font-size: 1.05rem; margin: 0; opacity: .9; }
    .hero-badge {
        display: inline-block; background: rgba(255,255,255,.2);
        border: 1px solid rgba(255,255,255,.35); border-radius: 20px;
        padding: .18rem .8rem; font-size: .8rem; margin-bottom: .7rem;
    }
    .section-title {
        font-size: 1.35rem; font-weight: 700; color: #1E293B;
        margin: 1.6rem 0 .6rem; padding-left: .6rem;
        border-left: 4px solid #0F766E;
    }
    .info-card {
        background: white; border-radius: 12px; padding: 1.1rem 1.3rem;
        box-shadow: 0 1px 6px rgba(0,0,0,.07); height: 100%;
    }
    .info-card .card-icon { font-size: 1.7rem; margin-bottom: .4rem; }
    .info-card h4 { font-size: 1rem; font-weight: 700; color: #1E293B; margin: 0 0 .3rem; }
    .info-card p  { font-size: .88rem; color: #475569; margin: 0; line-height: 1.55; }
    .definition-box {
        background: #CCFBF1; border-left: 5px solid #0F766E;
        border-radius: 0 10px 10px 0; padding: 1rem 1.4rem; margin: 1rem 0;
    }
    .definition-box p { margin: 0; color: #1E293B; font-size: .96rem; line-height: 1.65; }
    .quiz-box { background: white; border-radius: 12px; padding: 1.4rem 1.6rem;
        box-shadow: 0 2px 10px rgba(0,0,0,.08); margin-top: 1rem; }
    .quiz-q { font-weight: 700; color: #1E293B; font-size: 1rem; margin-bottom: .8rem; }
    </style>
    """, unsafe_allow_html=True)

def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 2 — Data Fundamentals for Finance</h1>
      <p>Understand financial data types, quality issues, feature engineering,
         and how to prepare data so ML models can learn from it effectively.</p>
    </div>""", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    pills = [("📊","Level","Beginner–Intermediate"),("⏱️","Read time","~30 minutes"),
             ("📋","Topics","7 sections"),("🏆","Outcome","Data-ready mindset")]
    for col, (icon, label, val) in zip([c1, c2, c3, c4], pills):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""",
          unsafe_allow_html=True)

def _section_data_types():
    st.markdown('<div class="section-title">📂 1. Types of Financial Data</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p>In ML, data is the fuel. The quality and type of data you feed a model
      directly determines how well it performs. Finance professionals are surrounded
      by rich data — the challenge is knowing how to use it.</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📋 Structured Data", "📄 Unstructured Data", "⏱️ Time-Series Data"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            **Structured data** is organised in rows and columns — like a spreadsheet or database table.
            It is the most common type in ML and the easiest to work with.

            **Finance examples:**
            - General ledger entries
            - Invoice records (vendor, amount, date, GL code)
            - Bank transaction data
            - Customer master data
            - Budget vs actual tables
            """)
        with c2:
            df = pd.DataFrame({
                "Invoice ID": ["INV-001","INV-002","INV-003","INV-004"],
                "Vendor": ["Acme Ltd","Beta Corp","Acme Ltd","Gamma Inc"],
                "Amount ($)": [12500, 3400, 15600, 890],
                "Due Date": ["2024-03-15","2024-03-20","2024-03-18","2024-03-25"],
                "Status": ["Paid","Overdue","Paid","Pending"],
            })
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.caption("Example: structured invoice table — ideal for ML")

    with tab2:
        st.markdown("""
        **Unstructured data** has no fixed format. It requires special ML techniques
        (Natural Language Processing — covered in Module 6) to process.

        **Finance examples:**
        - Audit notes and management letters
        - Earnings call transcripts
        - Vendor contracts and agreements
        - Customer complaint emails
        - News articles affecting valuations
        """)
        st.info("💡 Unstructured data is the fastest-growing data type in finance. "
                "Modern ML can extract structured insights from it automatically.")

    with tab3:
        st.markdown("""
        **Time-series data** is structured data where the **order and timing** of records matters.
        Finance is naturally time-series: every transaction has a timestamp.

        **Finance examples:**
        - Monthly revenue figures
        - Daily stock prices
        - Weekly cash balances
        - Quarterly earnings
        """)
        dates = pd.date_range("2022-01-01", periods=24, freq="ME") # Updated from 'M' to 'ME'
        np.random.seed(7)
        revenue = 100 + np.cumsum(np.random.randn(24) * 3 + 2)
        fig = px.line(x=dates, y=revenue, labels={"x":"Month","y":"Revenue ($M)"},
                      title="Monthly Revenue Time Series")
        fig.update_traces(line_color=PRIMARY, line_width=2.5)
        fig.update_layout(height=250, paper_bgcolor="rgba(0,0,0,0)",
                          plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=35,b=10,l=10,r=10),
                          xaxis=dict(gridcolor="#E2E8F0"), yaxis=dict(gridcolor="#E2E8F0"))
        st.plotly_chart(fig, use_container_width=True)

def _section_data_quality():
    st.markdown('<div class="section-title">🔍 2. Data Quality — The #1 Challenge in ML</div>', unsafe_allow_html=True)
    # FIXED SYNTAX ERROR HERE: Used single quotes around the double quoted phrase
    st.markdown('> **"Garbage in, garbage out."** — The most important rule in Machine Learning.')

    issues = [
        ("🕳️","Missing Values","Invoices with no GL code, customers with no credit score.",
         "Fill with mean/median, use 'Unknown' category, or remove rows."),
        ("👯","Duplicate Records","Same transaction recorded twice — common after system migrations.",
         "Deduplicate by key fields (invoice number, date, amount)."),
        ("📊","Outliers","A single $50M transaction in a dataset of $1K–$10K invoices.",
         "Investigate: is it real? Cap, transform, or treat separately."),
        ("🔀","Inconsistent Formats","Dates as '01/03/2024' vs '2024-03-01' vs 'March 1, 2024'.",
         "Standardise to ISO format (YYYY-MM-DD) in preprocessing."),
        ("🏷️","Wrong Labels","Invoice marked 'Paid' but still outstanding in the ledger.",
         "Cross-validate against multiple source systems."),
        ("📉","Imbalanced Classes","999 legitimate vs 1 fraudulent transaction — model learns to ignore fraud.",
         "Use oversampling (SMOTE), undersampling, or weighted loss functions."),
    ]

    cols = st.columns(3)
    for i, (icon, title, prob, sol) in enumerate(issues):
        with cols[i % 3]:
            st.markdown(f"""<div class="info-card" style="margin-bottom:1rem">
              <div class="card-icon">{icon}</div>
              <h4>{title}</h4>
              <p><strong>Problem:</strong> {prob}<br><br>
              <strong>Solution:</strong> {sol}</p></div>""", unsafe_allow_html=True)

    st.markdown("#### 🧪 Interactive: Spot the data quality issues")
    df_dirty = pd.DataFrame({
        "Invoice ID": ["INV-001","INV-002","INV-001","INV-003","INV-004","INV-005"],
        "Vendor":     ["Acme Ltd","Beta Corp","Acme Ltd","","Gamma Inc","Delta LLC"],
        "Amount":     [12500, 3400, 12500, 890, 9999999, 1200],
        "GL Code":    ["5001","5002","5001",None,"5003","5001"],
        "Issue":      ["✅ Clean","✅ Clean","⚠️ Duplicate","❌ Missing vendor",
                       "⚠️ Outlier?","✅ Clean"],
    })
    # FIXED: applymap replaced with map for modern pandas
    st.dataframe(df_dirty.style.map(
        lambda v: "background-color:#FEF2F2;color:#991B1B" if "❌" in str(v)
        else ("background-color:#FFFBEB;color:#92400E" if "⚠️" in str(v)
        else "background-color:#F0FDF4;color:#166534") if "✅" in str(v) else "",
        subset=["Issue"]
    ), use_container_width=True, hide_index=True)

def _section_features():
    st.markdown('<div class="section-title">🔧 3. Features & Feature Engineering</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Features</strong> are the input variables (columns) you give to the ML model.
      <strong>Feature engineering</strong> is the process of creating new, more informative
      features from raw data — often the most impactful step in improving model performance.</p>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Raw features:**")
        raw = pd.DataFrame({
            "Raw Column": ["invoice_date","due_date","amount","customer_id","payment_date"],
            "Type": ["Date","Date","Numeric","Categorical","Date"],
        })
        st.dataframe(raw, use_container_width=True, hide_index=True)
    with c2:
        st.markdown("**Engineered features:**")
        eng = pd.DataFrame({
            "New Feature": ["days_to_due","is_month_end","customer_avg_delay","amount_log"],
            "How derived": ["due_date - invoice_date","invoice_date.day > 25","avg of past delays","log(amount)"],
        })
        st.dataframe(eng, use_container_width=True, hide_index=True)

def _section_preprocessing():
    st.markdown('<div class="section-title">⚙️ 4. Data Preprocessing Steps</div>', unsafe_allow_html=True)
    steps = [
        ("1. Handle missing values", "numerical → fill with median; categorical → fill with mode"),
        ("2. Remove duplicates", "Drop exact duplicate rows; keep most recent for near-duplicates"),
        ("3. Encode categories", "Convert text categories to numbers: One-Hot Encoding"),
        ("4. Scale/normalise numbers", "Bring all numbers to the same scale (0-1)"),
    ]
    for step, detail in steps:
        with st.expander(f"✅ {step}"):
            st.markdown(f"**{step}**\n\n{detail}")

def _section_train_test():
    st.markdown('<div class="section-title">✂️ 5. Train / Validation / Test Split</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    splits = [
        ("70%","Training Set","#4F46E5","Model learns from this."),
        ("15%","Validation Set","#0F766E","Used to tune the model."),
        ("15%","Test Set","#F59E0B","Final honest evaluation."),
    ]
    for col, (pct, name, color, desc) in zip([col1,col2,col3], splits):
        col.markdown(f"""<div class="info-card" style="border-top:4px solid {color}">
          <h4 style="color:{color};font-size:1.5rem">{pct}</h4>
          <h4>{name}</h4><p>{desc}</p></div>""", unsafe_allow_html=True)

def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 2 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q": "Q1. 10,000 invoices: 9,950 legitimate, 50 fraudulent. What is this?",
         "opts": ["Data leakage","Class imbalance","Feature engineering"],
         "ans": "Class imbalance",
         "exp": "Correct! One class vastly outnumbers the other."},
        {"q": "Q2. Creating 'days_to_due' from dates is what?",
         "opts": ["Data cleaning","Feature engineering","Data leakage"],
         "ans": "Feature engineering",
         "exp": "Correct! Creating new informative columns is feature engineering."}
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("Select answer:", q["opts"], key=f"mod2_q{i}", index=None)
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"Incorrect. Answer is {q['ans']}")

def _footer():
    st.markdown("---")
    st.markdown("<div style='text-align:center;color:#64748B'>Knowledge Folder · Module 2 of 10</div>", unsafe_allow_html=True)

def show():
    """Main function called by Homepage.py"""
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 2 — Sections")
        st.progress(20, text="Module 2 / 10")
    _section_data_types()
    _section_data_quality()
    _section_features()
    _section_preprocessing()
    _section_train_test()
    _knowledge_check()
    _footer()