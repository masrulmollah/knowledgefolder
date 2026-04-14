"""
Machine Learning for Finance & Accounts
Module 4 – Unsupervised Learning for Finance

USAGE: import ml_module_04; ml_module_04.show()
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#7C3AED"; SUCCESS="#10B981"; WARNING="#F59E0B"; DANGER="#EF4444"; ACCENT="#06B6D4"


def _css():
    st.markdown("""
    <style>
    .main { background:#F5F3FF; }
    .hero-banner { background:linear-gradient(135deg,#7C3AED 0%,#A855F7 60%,#EC4899 100%);
        border-radius:16px; padding:2.4rem 2.8rem; color:white; margin-bottom:1.6rem; }
    .hero-banner h1 { font-size:2.1rem; margin:0 0 .4rem; font-weight:700; }
    .hero-banner p  { font-size:1.05rem; margin:0; opacity:.9; }
    .hero-badge { display:inline-block; background:rgba(255,255,255,.2);
        border:1px solid rgba(255,255,255,.35); border-radius:20px;
        padding:.18rem .8rem; font-size:.8rem; margin-bottom:.7rem; }
    .section-title { font-size:1.35rem; font-weight:700; color:#1E293B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #7C3AED; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .info-card .card-icon { font-size:1.7rem; margin-bottom:.4rem; }
    .info-card h4 { font-size:1rem; font-weight:700; color:#1E293B; margin:0 0 .3rem; }
    .info-card p  { font-size:.88rem; color:#475569; margin:0; line-height:1.55; }
    .definition-box { background:#EDE9FE; border-left:5px solid #7C3AED;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    .definition-box p { margin:0; color:#1E293B; font-size:.96rem; line-height:1.65; }
    .quiz-box { background:white; border-radius:12px; padding:1.4rem 1.6rem;
        box-shadow:0 2px 10px rgba(0,0,0,.08); margin-top:1rem; }
    .quiz-q { font-weight:700; color:#1E293B; font-size:1rem; margin-bottom:.8rem; }
    </style>""", unsafe_allow_html=True)


def _hero():
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-badge">📚 Machine Learning for Finance &amp; Accounts</div>
      <h1>Module 4 — Unsupervised Learning for Finance</h1>
      <p>Discover hidden patterns, segment customers, detect anomalies in transactions,
         and reduce complexity — all without needing labelled data.</p>
    </div>""", unsafe_allow_html=True)
    for col,(icon,label,val) in zip(st.columns(4),[
        ("🔍","Level","Intermediate"),("⏱️","Read time","~30 minutes"),
        ("📋","Techniques","3 covered"),("🏆","Outcome","Pattern discovery skills"),
    ]):
        col.markdown(f"""<div class="info-card" style="text-align:center">
          <div class="card-icon">{icon}</div>
          <p style="font-size:.75rem;color:#94A3B8;margin:0 0 .15rem;
             text-transform:uppercase;letter-spacing:.06em">{label}</p>
          <h4 style="font-size:.95rem;margin:0">{val}</h4></div>""", unsafe_allow_html=True)


def _section_intro():
    st.markdown('<div class="section-title">🔍 1. What is Unsupervised Learning?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Unsupervised Learning</strong> finds patterns and structure in data that has
      <em>no labels</em>. The algorithm discovers groups, anomalies, or compressed
      representations entirely on its own — without being told what to look for.</p>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        **When do you use unsupervised learning in finance?**

        - You have transaction data but **no fraud labels**
        - You want to **segment customers** without knowing the segments in advance
        - You want to find **unusual journal entries** in a general ledger
        - You want to **compress** hundreds of financial ratios into a few key dimensions
        - You want to find **natural groupings** of vendors, products or accounts
        """)
    with c2:
        st.markdown("""
        **Three main techniques:**

        | Technique | Goal | Finance use |
        |-----------|------|-------------|
        | **Clustering** | Group similar records | Customer segments |
        | **Anomaly Detection** | Find the unusual | Fraud, audit |
        | **Dimensionality Reduction** | Compress features | Risk dashboard |
        """)


def _section_clustering():
    st.markdown('<div class="section-title">👥 2. Clustering — K-Means in Finance</div>', unsafe_allow_html=True)
    st.markdown("""
    **K-Means clustering** divides data into K groups where records within each group
    are as similar as possible and as different as possible from other groups.
    """)

    st.markdown("#### 🎛️ Interactive Customer Segmentation")
    k = st.slider("Number of customer segments (K)", 2, 5, 3)

    np.random.seed(42)
    centres = [(2,2), (7,7), (2,8), (8,2), (5,5)][:k]
    data_x, data_y, cluster_labels = [], [], []
    for i, (cx, cy) in enumerate(centres):
        n = np.random.randint(40, 70)
        data_x.extend(np.random.normal(cx, .9, n))
        data_y.extend(np.random.normal(cy, .9, n))
        cluster_labels.extend([f"Segment {i+1}"] * n)

    names = {
        2: ["High-Value Clients", "Occasional Clients"],
        3: ["High-Value Loyal", "SME Regulars", "At-Risk Clients"],
        4: ["Premium Loyal", "SME Regulars", "Occasional Buyers", "Dormant Clients"],
        5: ["Premium Loyal", "Corporate Clients", "SME Regulars", "Occasional", "Dormant"],
    }
    seg_names = names.get(k, [f"Segment {i+1}" for i in range(k)])
    colours = [PRIMARY, SUCCESS, WARNING, DANGER, ACCENT][:k]
    df_c = pd.DataFrame({"x": data_x, "y": data_y, "Segment": cluster_labels})
    df_c["Segment Name"] = df_c["Segment"].map(
        {f"Segment {i+1}": seg_names[i] for i in range(k)})

    fig = px.scatter(df_c, x="x", y="y", color="Segment Name",
                     color_discrete_sequence=colours,
                     labels={"x":"Avg monthly spend ($K)","y":"Transaction frequency"},
                     title=f"K-Means clustering: {k} customer segments")
    for i, (cx, cy) in enumerate(centres):
        fig.add_trace(go.Scatter(x=[cx], y=[cy], mode="markers",
                                 marker=dict(symbol="star", size=16, color=colours[i],
                                             line=dict(color="white", width=1.5)),
                                 name=f"Centre {i+1}", showlegend=False))
    fig.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)", margin=dict(t=35,b=10,l=10,r=10),
                      xaxis=dict(gridcolor="#E2E8F0"), yaxis=dict(gridcolor="#E2E8F0"))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### 💼 How to use segments in finance practice")
    segment_actions = pd.DataFrame({
        "Segment": seg_names,
        "Avg Spend": ["$45K/mo","$12K/mo","$3K/mo","$800/mo","$200/mo"][:k],
        "Recommended action": [
            "Premium service, dedicated account manager",
            "Volume discounts, quarterly reviews",
            "Self-service portal, automated invoicing",
            "Re-engagement campaign, payment plan offer",
            "Cost-to-serve analysis, consider offboarding",
        ][:k],
    })
    st.dataframe(segment_actions, use_container_width=True, hide_index=True)


def _section_anomaly():
    st.markdown('<div class="section-title">🚨 3. Anomaly Detection — Find the Unusual</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="definition-box">
      <p><strong>Anomaly detection</strong> identifies data points that are significantly
      different from the majority. In finance, anomalies often represent fraud,
      errors, or important signals requiring investigation.</p>
    </div>""", unsafe_allow_html=True)

    np.random.seed(9)
    n = 200
    normal_amounts = np.random.lognormal(mean=7, sigma=1, size=n)
    anomaly_amounts = np.array([250000, 180000, 320000, 15, 8, 2])
    all_amounts = np.concatenate([normal_amounts, anomaly_amounts])
    is_anomaly = ["Normal"] * n + ["⚠️ Anomaly"] * len(anomaly_amounts)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(n)), y=normal_amounts,
        mode="markers", name="Normal transactions",
        marker=dict(color=SUCCESS, size=5, opacity=.6)
    ))
    for i, (val, idx) in enumerate(zip(anomaly_amounts, range(n, n+len(anomaly_amounts)))):
        fig.add_trace(go.Scatter(
            x=[idx], y=[val], mode="markers",
            name="Anomaly" if i == 0 else None,
            showlegend=(i==0),
            marker=dict(color=DANGER, size=12, symbol="x", line=dict(width=2, color=DANGER))
        ))
    fig.update_layout(
        title="Transaction anomaly detection — flagged outliers marked in red",
        height=300, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=35,b=10,l=10,r=10),
        xaxis=dict(gridcolor="#E2E8F0", title="Transaction index"),
        yaxis=dict(gridcolor="#E2E8F0", title="Transaction amount ($)", type="log")
    )
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Common anomaly detection algorithms:**
        - **Isolation Forest** — isolates anomalies by random partitioning
        - **Local Outlier Factor (LOF)** — compares density to neighbours
        - **Z-score / IQR** — statistical thresholds
        - **Autoencoders** — deep learning reconstruction error
        """)
    with col2:
        st.markdown("""
        **Finance use cases:**
        - 🔍 Unusual journal entries before month-end close
        - 💳 Fraudulent credit card transactions
        - 📊 Expense claims significantly above peer average
        - 🏦 Money laundering transaction patterns
        - 📋 Vendor invoice amounts spiking unexpectedly
        """)


def _section_pca():
    st.markdown('<div class="section-title">📉 4. Dimensionality Reduction (PCA)</div>', unsafe_allow_html=True)
    st.markdown("""
    **Principal Component Analysis (PCA)** compresses many features into fewer
    dimensions while retaining as much information as possible.

    **Finance example:** Instead of tracking 50 financial ratios, PCA might find
    that 3 "principal components" capture 85% of the variation — making dashboards
    and models much simpler.
    """)

    ratios = ["Current Ratio","Quick Ratio","Debt/Equity","Interest Coverage",
              "ROE","ROA","EBITDA Margin","Net Margin","Asset Turnover",
              "Inventory Days"]
    np.random.seed(3)
    variance_explained = [32, 21, 14, 9, 7, 5, 4, 3, 3, 2]
    cumulative = np.cumsum(variance_explained)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=ratios, y=variance_explained, name="Individual variance",
                         marker_color=PRIMARY))
    fig.add_trace(go.Scatter(x=ratios, y=cumulative, mode="lines+markers",
                             name="Cumulative %", yaxis="y2",
                             line=dict(color=DANGER, width=2),
                             marker=dict(size=7)))
    fig.add_shape(type="line", x0=-0.5, x1=9.5, y0=80, y1=80,
                  line=dict(color=SUCCESS, width=1.5, dash="dash"), yref="y2")
    fig.add_annotation(x=7, y=82, text="80% threshold", showarrow=False,
                       font=dict(color=SUCCESS, size=11), yref="y2")
    fig.update_layout(
        title="PCA: How much variance each financial ratio component explains",
        height=320, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=35,b=80,l=10,r=10),
        yaxis=dict(title="Variance explained (%)", gridcolor="#E2E8F0"),
        yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0,110]),
        legend=dict(x=0.6, y=.3), xaxis=dict(tickangle=45)
    )
    st.plotly_chart(fig, use_container_width=True)
    st.info("💡 The first 4 ratios (components) explain ~76% of variance. "
            "You can build accurate models using just 4 numbers instead of 50!")


def _section_use_cases():
    st.markdown('<div class="section-title">💼 5. Finance Use Cases Summary</div>', unsafe_allow_html=True)
    cases = [
        ("👥","Customer Segmentation","Clustering (K-Means)",
         "Group clients by payment behaviour, transaction volume, and risk level for tailored service."),
        ("🚨","Fraud & Anomaly Detection","Isolation Forest / LOF",
         "Flag unusual journal entries, suspicious transactions, or outlier expense claims."),
        ("📋","Vendor Grouping","Clustering (Hierarchical)",
         "Group vendors by invoice patterns to streamline AP processes and contract negotiations."),
        ("📊","Risk Dashboard","PCA",
         "Reduce 30 risk metrics to 3–5 key dimensions for executive reporting."),
        ("💱","Money Laundering Detection","Anomaly + Network Analysis",
         "Identify unusual patterns of fund movements across accounts."),
        ("📄","Document Categorisation","Clustering (Text)",
         "Group similar contracts, audit notes, or financial reports automatically."),
    ]
    for i in range(0, len(cases), 3):
        cols = st.columns(3)
        for col,(icon,title,algo,desc) in zip(cols, cases[i:i+3]):
            col.markdown(f"""<div class="info-card" style="margin-bottom:1rem">
              <div class="card-icon">{icon}</div>
              <h4>{title}</h4>
              <p style="font-size:.77rem;background:#EDE9FE;color:#4C1D95;
                 border-radius:4px;padding:.1rem .4rem;display:inline-block;
                 margin-bottom:.4rem">{algo}</p>
              <p>{desc}</p></div>""", unsafe_allow_html=True)


def _knowledge_check():
    st.markdown('<div class="section-title">🧩 Knowledge Check — Module 4 Quiz</div>', unsafe_allow_html=True)
    questions = [
        {"q":"Q1. Your company wants to segment 100,000 customers into groups based on payment behaviour, with no predefined categories. Which technique is most appropriate?",
         "opts":["Supervised classification","K-Means Clustering","Linear Regression","Logistic Regression"],
         "ans":"K-Means Clustering",
         "exp":"✅ Correct! K-Means clustering groups data without labels — perfect when you don't know the segments in advance."},
        {"q":"Q2. An ML model flags 6 journal entries out of 50,000 as 'unusual'. What technique is being used?",
         "opts":["Regression","Classification","Anomaly Detection","PCA"],
         "ans":"Anomaly Detection",
         "exp":"✅ Correct! Finding the few unusual records among many normal ones is anomaly detection."},
        {"q":"Q3. You have 80 financial ratios and want to simplify them to 5 key dimensions for a risk dashboard. Which technique should you use?",
         "opts":["K-Means Clustering","Logistic Regression","PCA (Dimensionality Reduction)","Random Forest"],
         "ans":"PCA (Dimensionality Reduction)",
         "exp":"✅ Correct! PCA compresses many features into fewer dimensions while retaining maximum information."},
    ]
    for i, q in enumerate(questions):
        st.markdown(f'<div class="quiz-box"><div class="quiz-q">{q["q"]}</div>', unsafe_allow_html=True)
        choice = st.radio("", q["opts"], key=f"mod4_q{i}", index=None, label_visibility="collapsed")
        if choice:
            if choice == q["ans"]: st.success(q["exp"])
            else: st.error(f"❌ Correct answer: **{q['ans']}**\n\n{q['exp']}")
        st.markdown("</div>", unsafe_allow_html=True); st.markdown("")


def _footer():
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**📚 ML for Finance & Accounts** · Module 4 of 10")
    c2.markdown("<div style='text-align:center'><a href='?module=3' style='color:#7C3AED'>◀ Module 3</a>"
                " &nbsp;|&nbsp; <a href='?module=5' style='color:#7C3AED'>Module 5 ▶</a></div>",
                unsafe_allow_html=True)
    c3.markdown("<div style='text-align:right;color:#64748B;font-size:.85rem'>Knowledge Folder</div>",
                unsafe_allow_html=True)


def show():
    _css(); _hero()
    with st.sidebar:
        st.markdown("### 📑 Module 4 — Sections")
        st.markdown("1. What is Unsupervised Learning?\n2. Clustering (K-Means)\n"
                    "3. Anomaly Detection\n4. PCA\n5. Finance Use Cases\n---\n🧩 Quiz")
        st.progress(40, text="Module 4 / 10")
    _section_intro(); st.markdown("")
    _section_clustering(); st.markdown("")
    _section_anomaly(); st.markdown("")
    _section_pca(); st.markdown("")
    _section_use_cases(); st.markdown("")
    _knowledge_check(); _footer()


if __name__ == "__main__":
    st.set_page_config(page_title="Module 4 – Unsupervised Learning | Knowledge Folder",
                       page_icon="🔍", layout="wide")
    show()