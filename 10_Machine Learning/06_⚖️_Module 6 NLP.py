"""
Machine Learning for Finance & Accounts
Module 6 – NLP for Finance Documents

USAGE: import ml_module_06; ml_module_06.show()
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#0E7490"; SECONDARY="#06B6D4"; SUCCESS="#10B981"; WARNING="#F59E0B"; DANGER="#EF4444"


def _css():
    st.markdown("""
    <style>
    .main { background:#ECFEFF; }
    .hero-banner { background:linear-gradient(135deg,#0E7490 0%,#0891B2 60%,#6366F1 100%);
        border-radius:16px; padding:2.4rem 2.8rem; color:white; margin-bottom:1.6rem; }
    .hero-banner h1 { font-size:2.1rem; margin:0 0 .4rem; font-weight:700; }
    .hero-banner p  { font-size:1.05rem; margin:0; opacity:.9; }
    .hero-badge { display:inline-block; background:rgba(255,255,255,.2);
        border:1px solid rgba(255,255,255,.35); border-radius:20px;
        padding:.18rem .8rem; font-size:.8rem; margin-bottom:.7rem; }
    .section-title { font-size:1.35rem; font-weight:700; color:#1E293B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #0E7490; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .info-card .card-icon { font-size:1.7rem; margin-bottom:.4rem; }
    .info-card h4 { font-size:1rem; font-weight:700; color:#1E293B; margin:0 0 .3rem; }
    .info-card p  { font-size:.88rem; color:#475569; margin:0; line-height:1.55; }
    .definition-box { background:#CFFAFE; border-left:5px solid #0E7490;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    .definition-box p { margin:0; color:#1E293B; font-size:.96rem; line-height:1.65; }
    .text-sample { background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px;
        padding:1rem 1.2rem; font-family:Georgia,serif; font-size:.92rem;
        line-height:1.7; color:#334155; }
    .quiz-box { background:white; border-radius:12px; padding:1.4rem 1.6rem;
        box-shadow:0 2px 10px rgba(0,0,0,.08); margin-top:1rem; }
    .quiz-q { font-weight:700; color:#1E293B; font-size:1rem; margin-bottom:.8rem; }
    .sentiment-pos { background:#D1FAE5; color:#065F46; border-radius:6px;
        padding:.15rem .5rem; font-weight:700; font-size:.85rem; }
    .sentiment-neg { background:#FEE2E2; color:#991B1B; border-radius:6px;
        padding:.15rem .5rem; font-weight:700; font-size:.85rem; }
    .sentiment-neu { background:#F1F5F9; color:#475569; border-radius:6px;
        padding:.15rem .5rem; font-weight:700; font-size:.85rem; }
    </style>""", unsafe_allow_html=True)


def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 6 — NLP for Finance Documents</h1>
      <p>Learn how ML reads and understands text: analyse earnings calls,
         classify contracts, extract financial data from reports, and gauge market sentiment.</p>
    </div>""", unsafe_allow_html=True)
    for col,(icon,label,val) in zip(st.columns(4),[
        ("📝","Level","Intermediate"),("⏱️","Read time","~30 minutes"),
        ("📋","Topics","5 NLP techniques"),("🏆","Outcome","Process finance text with ML"),
    ]):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""", unsafe_allow_html=True)


def _section_what_is_nlp():
    st.markdown('<div class="section-title">📖 1. What is NLP and Why Does Finance Need It?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Natural Language Processing (NLP)</strong> is the branch of ML that
      enables computers to read, understand, and generate human language. Finance
      generates enormous volumes of text — most of it unread by any model or system.</p>
    </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **How much text does finance generate?**
        - 📋 Annual reports: 50–300 pages each
        - 📞 Earnings calls: 60–90 min transcripts per quarter
        - 📄 Contracts: thousands per company per year
        - 📧 Internal communications: millions of messages
        - 📰 News & analyst reports: thousands per day

        **Without NLP:** Human analysts must read everything manually — slow, expensive, inconsistent.

        **With NLP:** ML reads and classifies all of it in seconds.
        """)
    with col2:
        tasks = ["Sentiment Analysis","Text Classification","Named Entity Recognition",
                 "Topic Modelling","Text Summarisation","Question Answering"]
        finance_use = ["Earnings call tone","Invoice GL coding","Extract company names from contracts",
                       "Find themes in audit notes","Summarise annual reports","Query financial documents"]
        for task, use in zip(tasks, finance_use):
            st.markdown(f"**{task}** → _{use}_")


def _section_sentiment():
    st.markdown('<div class="section-title">😊 2. Sentiment Analysis — Reading the Tone of Finance</div>', unsafe_allow_html=True)
    st.markdown("Sentiment analysis classifies text as **positive**, **negative**, or **neutral**.")

    earnings_samples = [
        ("We delivered exceptional revenue growth of 28% this quarter, exceeding all guidance.",
         "Positive", 0.91, "#D1FAE5", "#065F46"),
        ("Results were broadly in line with expectations, though headwinds remain in EMEA.",
         "Neutral", 0.12, "#F1F5F9", "#475569"),
        ("We are deeply concerned about margin compression and rising cost of capital.",
         "Negative", -0.78, "#FEE2E2", "#991B1B"),
        ("Our restructuring programme is progressing as planned with expected savings of $40M.",
         "Neutral", 0.22, "#F1F5F9", "#475569"),
        ("We see strong pipeline momentum and are confident in our full-year outlook.",
         "Positive", 0.76, "#D1FAE5", "#065F46"),
    ]
    st.markdown("#### 🎤 Earnings call sentiment analysis — live demo")
    user_text = st.text_area("Paste any earnings call or financial statement sentence:",
                             value="We are pleased to report strong growth across all segments, with EBITDA margins expanding by 150 basis points year on year.",
                             height=80)

    keywords_pos = ["strong","growth","exceeded","pleased","confident","exceptional","improved","expansion","momentum"]
    keywords_neg = ["concern","headwind","decline","difficult","compression","risk","challenging","missed","weak"]
    words = user_text.lower().split()
    pos_count = sum(1 for w in words if any(k in w for k in keywords_pos))
    neg_count = sum(1 for w in words if any(k in w for k in keywords_neg))
    score = (pos_count - neg_count) / max(len(words) * 0.1, 1)
    score = max(-1, min(1, score))
    if score > 0.15: sentiment, color = "Positive 😊", SUCCESS
    elif score < -0.15: sentiment, color = "Negative 😟", DANGER
    else: sentiment, color = "Neutral 😐", WARNING

    col1, col2, col3 = st.columns(3)
    col1.metric("Sentiment", sentiment)
    col2.metric("Positive keywords", pos_count)
    col3.metric("Negative keywords", neg_count)

    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=score,
        title={"text":"Sentiment Score"},
        gauge={"axis":{"range":[-1,1]},
               "bar":{"color":color},
               "steps":[{"range":[-1,-0.15],"color":"#FEE2E2"},
                        {"range":[-0.15,0.15],"color":"#F1F5F9"},
                        {"range":[0.15,1],"color":"#D1FAE5"}]},
    ))
    fig.update_layout(height=220, paper_bgcolor="rgba(0,0,0,0)",
                      margin=dict(t=20,b=10,l=30,r=30))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### 📊 Historical earnings call sentiment vs stock returns")
    quarters = ["Q1 2022","Q2 2022","Q3 2022","Q4 2022","Q1 2023","Q2 2023","Q3 2023","Q4 2023"]
    sentiment_scores = [0.72, 0.61, -0.48, -0.62, 0.15, 0.44, 0.68, 0.79]
    stock_return = [3.2, 1.8, -4.1, -5.3, 0.4, 2.1, 3.8, 4.6]
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=quarters, y=sentiment_scores, name="Sentiment score",
                          marker_color=[SUCCESS if s>0 else DANGER for s in sentiment_scores]))
    fig2.add_trace(go.Scatter(x=quarters, y=stock_return, mode="lines+markers",
                              name="Stock return (%)", yaxis="y2",
                              line=dict(color=PRIMARY, width=2.5), marker=dict(size=8)))
    fig2.update_layout(height=280, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       margin=dict(t=20,b=10,l=10,r=10), barmode="group",
                       yaxis=dict(title="Sentiment", gridcolor="#E2E8F0"),
                       yaxis2=dict(title="Return %", overlaying="y", side="right"),
                       legend=dict(x=0,y=1))
    st.plotly_chart(fig2, use_container_width=True)


def _section_text_classification():
    st.markdown('<div class="section-title">🏷️ 3. Text Classification — Auto-Coding Invoices & Expenses</div>', unsafe_allow_html=True)
    st.markdown("""
    Text classification assigns categories to text. In accounting, the most common use
    is **automatic GL (General Ledger) coding** — reading an invoice description and
    assigning the correct account code.
    """)

    invoice_data = [
        ("Microsoft Azure - Cloud compute charges Oct 2024", "IT Infrastructure", "6210", "✅ High confidence"),
        ("Monthly office cleaning service - City Clean Ltd", "Facilities", "7110", "✅ High confidence"),
        ("Business travel - London to New York - J.Smith", "Travel & Entertainment", "8310", "✅ High confidence"),
        ("Strategic consulting services Q4 2024 - McKinsey", "Professional Fees", "7510", "✅ High confidence"),
        ("Mixed supplies and services - various invoices", "⚠️ Needs Review", "???", "⚠️ Low confidence"),
    ]
    df = pd.DataFrame(invoice_data, columns=["Invoice Description","GL Category","GL Code","Confidence"])
    st.dataframe(
        df.style.applymap(
            lambda v: "background-color:#D1FAE5;color:#065F46" if "✅" in str(v)
            else "background-color:#FEF3C7;color:#92400E" if "⚠️" in str(v) else "",
            subset=["Confidence"]
        ),
        use_container_width=True, hide_index=True
    )
    st.info("💡 A well-trained classification model can auto-code 85–95% of invoices with "
            "high confidence, flagging only the ambiguous ones for human review.")


def _section_ner():
    st.markdown('<div class="section-title">🔎 4. Named Entity Recognition (NER) — Extracting Key Information</div>', unsafe_allow_html=True)
    st.markdown("""
    **NER** automatically identifies and extracts key entities from text —
    like company names, dates, monetary amounts, and percentages.
    This is crucial for processing contracts, annual reports, and regulatory filings.
    """)

    sample_text = """Acme Corporation reported net revenue of $2.4 billion for the fiscal year
    ended December 31, 2024, representing a 14.2% increase year-over-year.
    Chief Executive John Smith noted that the EMEA region contributed $680 million,
    while negotiations with Beta Holdings Ltd regarding the proposed $450 million
    acquisition remain ongoing."""

    st.markdown('<div class="text-sample">' + sample_text + '</div>', unsafe_allow_html=True)
    st.markdown("#### 🏷️ Entities extracted by NER:")

    entities = [
        ("Acme Corporation", "ORGANISATION", "#DBEAFE", "#1E3A5F"),
        ("$2.4 billion", "MONEY", "#D1FAE5", "#065F46"),
        ("December 31, 2024", "DATE", "#FEF3C7", "#92400E"),
        ("14.2%", "PERCENTAGE", "#EDE9FE", "#3730A3"),
        ("John Smith", "PERSON", "#FCE7F3", "#831843"),
        ("EMEA", "LOCATION/REGION", "#CFFAFE", "#164E63"),
        ("$680 million", "MONEY", "#D1FAE5", "#065F46"),
        ("Beta Holdings Ltd", "ORGANISATION", "#DBEAFE", "#1E3A5F"),
        ("$450 million", "MONEY", "#D1FAE5", "#065F46"),
    ]

    chips = " ".join([
        f'<span style="background:{bg};color:{tc};border-radius:6px;'
        f'padding:.2rem .6rem;font-size:.83rem;font-weight:600;'
        f'margin:.2rem;display:inline-block">{text} <span style="opacity:.7;'
        f'font-size:.7rem">({label})</span></span>'
        for text, label, bg, tc in entities
    ])
    st.markdown(chips, unsafe_allow_html=True)

    st.markdown("""
    **Finance applications of NER:**
    - Extract all monetary amounts from contracts automatically
    - Build a database of counterparty relationships from agreement text
    - Pull key dates (payment terms, expiry dates) from vendor agreements
    - Monitor news for mentions of your portfolio companies
    """)


def _section_topic_modelling():
    st.markdown('<div class="section-title">📊 5. Topic Modelling & Document Summarisation</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🗂️ Topic Modelling", "📝 Summarisation"])
    with tab1:
        st.markdown("""
        **Topic modelling** (LDA, NMF) discovers recurring themes across a collection
        of documents without being told what themes to look for.
        """)
        topics = {
            "Topic 1 — Liquidity Risk": ["cash","liquidity","facility","covenant","refinancing","maturity","revolving"],
            "Topic 2 — Regulatory Compliance": ["IFRS","disclosure","audit","compliance","regulator","provision","restatement"],
            "Topic 3 — Growth Strategy": ["acquisition","synergy","market","expansion","investment","pipeline","partnership"],
            "Topic 4 — Cost Management": ["efficiency","restructuring","headcount","margin","overhead","savings","optimisation"],
        }
        colours = [PRIMARY, SUCCESS, WARNING, "#7C3AED"]
        cols = st.columns(2)
        for i, (topic, words) in enumerate(topics.items()):
            with cols[i % 2]:
                chips = " ".join([f'<span style="background:{colours[i]}22;color:{colours[i]};'
                                  f'border:1px solid {colours[i]}44;border-radius:4px;'
                                  f'padding:.15rem .5rem;font-size:.8rem;margin:.1rem;'
                                  f'display:inline-block">{w}</span>' for w in words])
                st.markdown(f"**{topic}**")
                st.markdown(chips, unsafe_allow_html=True)
                st.markdown("")

    with tab2:
        st.markdown("""
        **Automatic summarisation** condenses long documents into key points.
        Critical for finance professionals dealing with lengthy reports.

        **Use cases:**
        - Summarise 200-page annual reports to 1-page executive briefs
        - Generate meeting summaries from earnings call transcripts
        - Create vendor risk summaries from supplier contracts
        - Daily news digests covering your sector and portfolio
        """)
        st.markdown("**Example:** Annual report section → Auto-summary")
        st.markdown('<div class="text-sample" style="border-left:3px solid #0E7490">'
                    '<strong>Original (180 words):</strong> The Group\'s liquidity position '
                    'remained robust throughout the year, supported by strong operating cash '
                    'generation and an undrawn revolving credit facility of £300 million maturing '
                    'in 2027. Net debt decreased to £480 million from £620 million, representing '
                    'a net debt to EBITDA ratio of 1.8x, well within our target range of below 2.5x. '
                    'The Board continues to monitor covenants closely and is satisfied that there is '
                    'significant headroom...</div>', unsafe_allow_html=True)
        st.markdown("")
        st.success("**🤖 AI Summary (25 words):** Liquidity is strong. Net debt fell to £480M "
                   "(1.8x EBITDA, target <2.5x). £300M undrawn credit facility. Covenant headroom is comfortable.")


def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 6 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q":"Q1. You want to automatically assign GL codes to thousands of invoices based on their description text. Which NLP technique should you use?",
         "opts":["Sentiment Analysis","Text Classification","Named Entity Recognition","Topic Modelling"],
         "ans":"Text Classification",
         "exp":"✅ Correct! Assigning categories (GL codes) to text is a text classification task."},
        {"q":"Q2. An NLP model reads: 'Revenue grew to $4.2B in Q3 2024'. It extracts '$4.2B' and 'Q3 2024' as key entities. What technique is this?",
         "opts":["Sentiment Analysis","Topic Modelling","Named Entity Recognition (NER)","Text Summarisation"],
         "ans":"Named Entity Recognition (NER)",
         "exp":"✅ Correct! NER identifies and extracts specific entities like money amounts, dates, and organisations from text."},
        {"q":"Q3. An analyst uses ML to detect that an earnings call sounds significantly more negative than the previous quarter. What technique is this?",
         "opts":["Text Classification","Topic Modelling","Sentiment Analysis","Named Entity Recognition"],
         "ans":"Sentiment Analysis",
         "exp":"✅ Correct! Measuring the tone (positive/negative/neutral) of text is sentiment analysis."},
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("", q["opts"], key=f"mod6_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"❌ Correct answer: **{q['ans']}**\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True); st.markdown("")


def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 ML for Finance & Accounts** · Module 6 of 10")
    c2.markdown("<div style='text-align:center'><a href='?module=5' style='color:#0E7490'>◀ Module 5</a>"
                " &nbsp;|&nbsp; <a href='?module=7' style='color:#0E7490'>Module 7 ▶</a></div>",
                unsafe_allow_html=True)
    c3.markdown("<div style='text-align:right;color:#64748B;font-size:.85rem'>Knowledge Folder</div>",
                unsafe_allow_html=True)


def show():
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 6 — Sections")
        st.markdown("1. What is NLP?\n2. Sentiment Analysis\n3. Text Classification\n"
                    "4. Named Entity Recognition\n5. Topic Modelling & Summarisation\n---\n🧩 Quiz")
        st.progress(60, text="Module 6 / 10")
    _section_what_is_nlp(); st.markdown("")
    _section_sentiment(); st.markdown("")
    _section_text_classification(); st.markdown("")
    _section_ner(); st.markdown("")
    _section_topic_modelling(); st.markdown("")
    _knowledge_check(); _footer()


if __name__ == "__main__":
    st.set_page_config(page_title="Module 6 – NLP for Finance | Knowledge Folder",
                       page_icon="📝", layout="wide")
    show()