# -*- coding: utf-8 -*-
"""
Machine Learning for Finance & Accounts - Executive Portal & Comprehensive Overview
Architecture Entry-Point & Synthesis Hub
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Consistent UI Color Palette
PRIMARY = "#1E3A5F"     # Deep Slate Navy
SECONDARY = "#0F766E"   # Deep Teal
ACCENT = "#6366F1"      # Indigo Spark
SUCCESS = "#10B981"     # Emerald
WARNING = "#F59E0B"     # Amber
DANGER = "#EF4444"      # Crimson
MUTED = "#64748B"       # Slate Gray
BG_CARD = "#F8FAFC"     # Off-White

def _css():
    st.markdown("""
    <style>
    .main { background: #F1F5F9; }
    .portal-banner {
        background: linear-gradient(135deg, #1E3A5F 0%, #0F766E 50%, #4F46E5 100%);
        border-radius: 16px;
        padding: 3rem 3.5rem;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(30, 58, 95, 0.15);
    }
    .portal-banner h1 { font-size: 2.6rem; margin: 0 0 .5rem; font-weight: 800; color: white !important; }
    .portal-banner p { font-size: 1.2rem; margin: 0; opacity: .95; color: white !important; font-weight: 300; }
    .portal-badge {
        display: inline-block;
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.35);
        border-radius: 30px;
        padding: .25rem 1rem;
        font-size: .85rem;
        margin-bottom: 1rem;
        font-weight: 600;
        letter-spacing: .05em;
        text-transform: uppercase;
    }
    .grid-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1E293B;
        margin: 2rem 0 1rem;
        padding-left: .75rem;
        border-left: 5px solid #1E3A5F;
    }
    .module-card {
        background: white;
        border-radius: 14px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        border: 1px solid #E2E8F0;
        height: 100%;
    }
    .module-num {
        font-size: 0.8rem;
        font-weight: 700;
        color: #6366F1;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.25rem;
    }
    .module-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #0F172A;
        margin: 0 0 0.5rem 0;
    }
    .module-desc {
        font-size: 0.9rem;
        color: #475569;
        line-height: 1.5;
        margin-bottom: 1rem;
    }
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        margin-bottom: 1rem;
    }
    .pill-tag {
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.15rem 0.5rem;
        border-radius: 6px;
        background: #F1F5F9;
        color: #475569;
    }
    .pill-tag-tech { background: #E0E7FF; color: #4338CA; }
    .pill-tag-type { background: #CCFBF1; color: #0F766E; }
    
    .metric-box {
        background: white;
        padding: 1.25rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        text-align: center;
        border-top: 4px solid #1E3A5F;
    }
    .synthesis-container {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

def _hero():
    st.markdown("""
    <div class="portal-banner">
      <div class="portal-badge">Executive Knowledge Hub</div>
      <h1>Machine Learning for Finance &amp; Accounts</h1>
      <p>A comprehensive 10-module strategic framework designed to bridge the gap between advanced data science and practical corporate finance application.</p>
    </div>
    """, unsafe_allow_html=True)

def get_module_data():
    return [
        {"id": 1, "title": "Module 1: What is Machine Learning?", "desc": "Foundational paradigm shift comparing rules-based systems vs. automated pattern discovery from high-volume corporate transactions.", "type": "Core Theory", "tech": "Conceptual", "icon": "🤖"},
        {"id": 2, "title": "Module 2: Data Fundamentals for Finance", "desc": "Deep dive into structural corporate data dimensions. Overcoming data distribution risks like extreme class imbalances and missing strings.", "type": "Data Engineering", "tech": "Pandas / SQL", "icon": "📊"},
        {"id": 3, "title": "Module 3: Supervised Learning for Finance", "desc": "Implementation of predictable models using labelled historic targets. Compares classic linear regression with ensemble tree boosting methods.", "type": "Predictive ML", "tech": "Scikit-Learn / XGBoost", "icon": "📈"},
        {"id": 4, "title": "Module 4: Unsupervised Learning for Finance", "desc": "Pattern tracking techniques operating without predefined labels. Excellent for capturing unseen transaction fraud signatures.", "type": "Pattern Discovery", "tech": "K-Means / Isolation Forest", "icon": "🔍"},
        {"id": 5, "title": "Module 5: Time Series & Forecasting", "desc": "Advanced multi-period forecasting methods mapping seasonality, trendlines, and residuals directly onto business planning matrices.", "type": "Forecasting", "tech": "ARIMA / SARIMA", "icon": "📅"},
        {"id": 6, "title": "Module 6: NLP for Finance Documents", "desc": "Deploying intelligent text parsing algorithms across massive bodies of unorganized documents, financial statements, and invoice records.", "type": "Text Analytics", "tech": "NER / Sentiment Models", "icon": "📝"},
        {"id": 7, "title": "Module 7: ML Applications in Finance", "desc": "Moving directly from technical theories into operational continuous tracking systems, smart audits, and accounts payable automations.", "type": "Operational ML", "tech": "Fuzzy Match / Clustering", "icon": "⚖️"},
        {"id": 8, "title": "Module 8: Building Your First ML Model", "desc": "Practical framework constructing an end-to-end classification dashboard designed to predict credit risks and vendor payment delay pipelines.", "type": "Practical Dev", "tech": "Python Dev Tools", "icon": "🛠️"},
        {"id": 9, "title": "Module 9: Model Evaluation & Ethics", "desc": "Rigorous performance diagnostics combined with transparent algorithmic explainability tools (SHAP values) and bias checking frameworks.", "type": "Governance / Risk", "tech": "SHAP / ROC Curves", "icon": "🛡️"},
        {"id": 10, "title": "Module 10: Advanced ML & Future of Finance", "desc": "Strategic roadmap analyzing deep multi-layered neural networks, generative corporate assistants, large language models, and evolving workflows.", "type": "Strategic Innovation", "tech": "Deep Learning / GenAI", "icon": "🚀"}
    ]

def _render_overview_tab():
    st.markdown('<div class="grid-title">🎓 The 10-Module Knowledge Architecture</div>', unsafe_allow_html=True)
    modules = get_module_data()
    
    for i in range(0, len(modules), 2):
        col1, col2 = st.columns(2)
        with col1:
            m = modules[i]
            st.markdown(f"""
            <div class="module-card">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{m['icon']}</div>
                <div class="module-num">Step 0{m['id']} · {m['type']}</div>
                <h3 class="module-title">{m['title']}</h3>
                <p class="module-desc">{m['desc']}</p>
                <div class="tag-container">
                    <span class="pill-tag pill-tag-type">{m['type']}</span>
                    <span class="pill-tag pill-tag-tech">{m['tech']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if i + 1 < len(modules):
                m = modules[i+1]
                st.markdown(f"""
                <div class="module-card">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{m['icon']}</div>
                    <div class="module-num">Step {m['id'] if m['id'] >= 10 else f'0{m["id"]}'} · {m['type']}</div>
                    <h3 class="module-title">{m['title']}</h3>
                    <p class="module-desc">{m['desc']}</p>
                    <div class="tag-container">
                        <span class="pill-tag pill-tag-type">{m['type']}</span>
                        <span class="pill-tag pill-tag-tech">{m['tech']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        st.write("")

def _render_synthesis_tab():
    st.markdown('<div class="grid-title">📊 Cross-Module Technical Synthesis</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="synthesis-container">
        <h3>🔄 End-to-End Financial Pipeline Flow</h3>
        <p>This dynamic synthesis matrix establishes how data moves throughout corporate pipelines, showing how different module competencies connect into production ecosystems.</p>
    </div>
    """, unsafe_allow_html=True)
    
    pipeline_data = {
        "Data Pipeline Stage": ["1. Harvesting & Data Prep", "2. Model Architecture Execution", "3. Diagnostics & Explainability", "4. Production Continuous Audit"],
        "Core Objectives": ["Clean ledger inputs; fix highly skewed arrays.", "Run regressions or classification matrices.", "Isolate true error costs and check features.", "Perform automated population tracking."],
        "Relevant Modules": ["Modules 2 & 6", "Modules 3, 4, 5 & 10", "Module 9", "Modules 7 & 10"]
    }
    st.table(pd.DataFrame(pipeline_data))

    # Dynamic Analytical Metrics Chart
    st.write("")
    tasks = ['Credit Delinquency', 'Invoice G/L Coding', 'Fraud Discovery', 'Cash Variances']
    legacy_rules = [72, 65, 50, 78]
    ml_models = [94, 92, 96, 93]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=tasks, y=legacy_rules, name='Legacy Rules Base', marker_color='#94A3B8'))
    fig.add_trace(go.Bar(x=tasks, y=ml_models, name='ML Architectures', marker_color='#0F766E'))
    fig.update_layout(barmode='group', title='Accuracy Gains Scale (%)', plot_bgcolor='white', height=300)
    st.plotly_chart(fig, use_container_width=True)

def _render_interactive_portal():
    st.markdown('<div class="grid-title">🧭 Enterprise Roadmap Matcher</div>', unsafe_allow_html=True)
    selected = st.selectbox("Select Target Business Objective:", [
        "Select Objective...",
        "Optimize Accounts Receivable Collection Pipelines",
        "Automate Unstructured Document Invoice Ledger Coding"
    ])
    
    if selected != "Select Objective...":
        st.markdown('<div style="background: white; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: 12px;">', unsafe_allow_html=True)
        if "Accounts Receivable" in selected:
            st.markdown("<h4>🎯 Target Vector: AR Collections Optimization</h4><p>Requires Supervised Binary Classification. Focus heavily on <strong>Module 2</strong> data scaling, <strong>Module 3</strong> modeling implementations, and <strong>Module 8</strong> practical builds.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<h4>📝 Target Vector: Automated Invoice String Matching</h4><p>Requires NLP Entity Extraction. Focus heavily on <strong>Module 2</strong> text transforms and <strong>Module 6</strong> Named Entity Recognition frameworks.</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def _footer():
    st.markdown("""
    <hr style="border:0; height:1px; background:#E2E8F0; margin-top:3rem;">
    <div style="display:flex; justify-content:between; font-size:0.8rem; color:#94A3B8; padding-bottom:1rem;">
        <div>📚 Machine Learning for Finance &amp; Accounts · Complete Portfolio Portal</div>
        <div style="margin-left:auto;">Knowledge Folder Platform</div>
    </div>
    """, unsafe_allow_html=True)

# ── MANDATORY SHOW FUNCTION CALLED BY THE MULTI-PAGE APPLICATION FRAMEWORK ──
def show():
    """Main execution path that structures the layout components cleanly."""
    _css()
    _hero()
    
    # 4 High-Level Summary Cards
    m1, m2, m3, m4 = st.columns(4)
    m1.markdown('<div class="metric-box"><h4>Depth</h4><h2>10 Modules</h2></div>', unsafe_allow_html=True)
    m2.markdown('<div class="metric-box" style="border-top-color:#0F766E;"><h4>Scope</h4><h2>12+ Models</h2></div>', unsafe_allow_html=True)
    m3.markdown('<div class="metric-box" style="border-top-color:#6366F1;"><h4>Focus</h4><h2>Enterprise ROI</h2></div>', unsafe_allow_html=True)
    m4.markdown('<div class="metric-box" style="border-top-color:#10B981;"><h4>Status</h4><h2>Production Ready</h2></div>', unsafe_allow_html=True)
    
    st.write("")
    
    tab_overview, tab_synthesis, tab_portal = st.tabs([
        "📋 Executive Module Index", 
        "🔄 Cross-Discipline Synthesis", 
        "🧭 Dynamic Scenario Matrix"
    ])
    
    with tab_overview:
        _render_overview_tab()
    with tab_synthesis:
        _render_synthesis_tab()
    with tab_portal:
        _render_interactive_portal()
        
    _footer()

# Local Execution Engine Fallback
if __name__ == '__main__':
    st.set_page_config(page_title="Executive Hub | ML for Finance", page_icon="⚖️", layout="wide")
    show()