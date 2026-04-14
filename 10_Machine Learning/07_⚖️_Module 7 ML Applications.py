import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

PRIMARY="#065F46"; SUCCESS="#10B981"; WARNING="#F59E0B"; DANGER="#EF4444"; ACCENT="#6366F1"

def _css():
    st.markdown("""
    <style>
    .main { background:#ECFDF5; }
    .hero-banner { background:linear-gradient(135deg,#065F46 0%,#059669 60%,#0891B2 100%);
        border-radius:16px; padding:2.4rem 2.8rem; color:white; margin-bottom:1.6rem; }
    .hero-banner h1 { font-size:2.1rem; margin:0 0 .4rem; font-weight:700; color: white !important; }
    .hero-banner p  { font-size:1.05rem; margin:0; opacity:.9; color: white !important; }
    .section-title { font-size:1.35rem; font-weight:700; color:#064E3B;
        margin:1.6rem 0 .6rem; padding-left:.6rem; border-left:4px solid #065F46; }
    .info-card { background:white; border-radius:12px; padding:1.1rem 1.3rem;
        box-shadow:0 1px 6px rgba(0,0,0,.07); height:100%; }
    .definition-box { background:#D1FAE5; border-left:5px solid #065F46;
        border-radius:0 10px 10px 0; padding:1rem 1.4rem; margin:1rem 0; }
    </style>
    """, unsafe_allow_html=True)

def _hero():
    st.markdown("""
    <div class="hero-banner">
      <h1>Module 7 — ML Applications in Finance</h1>
      <p>Moving from theory to practice: How Machine Learning transforms Fraud, Audit, AP, and Credit Risk.</p>
    </div>""", unsafe_allow_html=True)

def _section_fraud():
    st.markdown('<div class="section-title">🕵️ 1. Fraud Detection & Anti-Money Laundering</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Anomaly Detection (Unsupervised)**
        The model learns 'normal' behavior and flags anything that deviates significantly.
        - *Benefit:* Catches 'Unknown Unknowns'—fraud types you haven't seen before.
        """)
    # FIXED SYNTAX ERROR HERE
    with col2:
        st.markdown("""
        **Pattern Recognition (Supervised)**
        The model is trained on historical fraud cases to recognize known red flags.
        - *Benefit:* Extremely high accuracy for known fraud schemes.
        """)

def _section_audit():
    st.markdown('<div class="section-title">📊 2. Smart Audit & Continuous Monitoring</div>', unsafe_allow_html=True)
    st.info("Traditional audit samples 5-10% of data. ML allows for **100% population testing**.")
    
    data = {
        "Audit Task": ["Duplicate Invoices", "Ghost Vendors", "Benford's Law Analysis", "Risk-Based Sampling"],
        "ML Approach": ["Fuzzy Matching", "Clustering", "Statistical Modeling", "Classification"],
        "Impact": ["Cash recovery", "Loss prevention", "Regulatory compliance", "Efficiency"]
    }
    # FIXED: applymap replaced with map for modern pandas compatibility
    st.table(pd.DataFrame(data))

def show():
    """Main entry point called by Homepage.py"""
    _css()
    _hero()
    
    with st.sidebar:
        st.markdown("### 📑 Module 7 Sections")
        st.progress(70, text="Module 7 / 10")
        st.write("- Fraud Detection\n- Audit Analytics\n- AP Automation\n- Credit Risk")

    _section_fraud()
    _section_audit()
    
    st.markdown("---")
    st.caption("Knowledge Folder · Machine Learning for Finance & Accounts")

# CRITICAL: Removed st.set_page_config and the __main__ block 
# to ensure it integrates with your Homepage without crashing.