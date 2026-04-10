import streamlit as st
import pandas as pd
import numpy as np

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 11 · International & Treasury Finance", page_icon="🌐", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');
html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; }
.hero { background: linear-gradient(135deg, #1a365d 0%, #2b6cb0 50%, #4299e1 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '🌐'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.15); color: #ebf8ff; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Playfair Display', serif; color: #fff; font-size: 42px; margin: 0 0 12px 0; }
.hero p { color: #ebf8ff; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #2b6cb0; }
.card h3 { font-family: 'Playfair Display', serif; color: #1a365d; font-size: 18px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }
.formula-box { background: #f7fafc; border: 1px solid #bee3f8; border-radius: 8px; padding: 14px 18px; font-family: 'Courier New', monospace; font-size: 14px; color: #2c5282; margin: 10px 0; font-weight: 600; }
.insight { background: #ebf8ff; border-left: 4px solid #3182ce; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #2c5282; font-size: 14px; margin: 0; line-height: 1.6; }
.sh { font-family: 'Playfair Display', serif; color: #1a365d; font-size: 24px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #e2e8f0; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#1a365d,#4299e1); border-radius: 10px; height: 6px; width: 91.6%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 11 of 12</div>
<h1>International & Treasury Finance</h1>
<p>Navigate the complexities of global capital flows, currency risk management, and the strategic functions of a corporate treasury department.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#2b6cb0;margin-bottom:4px;"><span>Course progress</span><span>Module 11 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🏛️ Treasury Function", "💱 Foreign Exchange", "🌎 International Finance", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">The Corporate Treasury Department</div>', unsafe_allow_html=True)
    treasury_roles = [
        ("Liquidity Management", "Ensuring the company has enough cash to meet its obligations. This involves daily cash positioning, short-term investing of surplus cash, and managing credit lines."),
        ("Risk Management", "Identifying and mitigating financial risks, primarily interest rate risk, foreign exchange risk, and commodity price risk through hedging strategies."),
        ("Capital Raising & Structure", "Determining the optimal mix of debt and equity and executing the issuance of bonds, commercial paper, or bank loans."),
        ("Bank Relationship Management", "Maintaining and optimizing relationships with financial institutions for credit, cash management, and advisory services."),
        ("Corporate Governance", "Ensuring compliance with financial regulations and internal controls related to financial assets and transactions."),
    ]
    for t, b in treasury_roles:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">Foreign Exchange (FX) Fundamentals</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="formula-box">Indirect Quote: 1 Unit of Local Currency = X Units of Foreign Currency</div>
    <div class="formula-box">Direct Quote: 1 Unit of Foreign Currency = X Units of Local Currency</div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### ⚡ FX Risk Exposure Calculator")
    col1, col2 = st.columns(2)
    with col1:
        exposure_amount = st.number_input("Exposure Amount (USD $)", value=1000000)
        spot_rate = st.number_input("Current Spot Rate (USD/INR)", value=83.50)
    with col2:
        expected_volatility = st.slider("Expected Volatility (%)", 1, 20, 5)
        time_horizon = st.selectbox("Time Horizon", ["1 Month", "3 Months", "6 Months", "1 Year"])
    
    impact = exposure_amount * spot_rate * (expected_volatility / 100)
    st.info(f"Potential financial impact of a {expected_volatility}% move: **₹{impact:,.0f}**")
    
    st.markdown('<div class="insight"><p><strong>The "Trilemma" of International Finance:</strong> A country cannot have more than two of the following at the same time: (1) A fixed exchange rate, (2) Free capital movement, and (3) An independent monetary policy.</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="sh">International Capital Budgeting</div>', unsafe_allow_html=True)
    concepts = [
        ("Purchasing Power Parity (PPP)", "The theory that exchange rates between currencies are in equilibrium when their purchasing power is the same in each of the two countries."),
        ("International Fisher Effect", "Differences in nominal interest rates reflect differences in expected inflation, which in turn drive changes in spot exchange rates."),
        ("Political Risk", "The risk that a host government's actions (expropriation, tax changes, capital controls) will adversely affect an investment's value."),
        ("Repatriation of Profits", "The process of moving earnings from a foreign subsidiary back to the parent company. Often subject to withholding taxes and regulatory hurdles."),
    ]
    for t, b in concepts:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 11</div>', unsafe_allow_html=True)
    qs = [
        {"q": "Which treasury function involves managing the daily cash inflows and outflows to ensure operational stability?",
         "options": ["Capital Structure", "Liquidity Management", "Repatriation", "Mergers & Acquisitions"],
         "answer": "Liquidity Management",
         "exp": "Liquidity management is the core daily task of treasury, focused on ensuring the firm has sufficient 'liquidity' (cash/near-cash) to pay its bills."},
        {"q": "If the USD/INR exchange rate moves from 80 to 85, which of the following is true for an Indian EXPORTER?",
         "options": ["Their competitive position weakens", "They receive more Rupees for their USD revenue", "The Rupee has appreciated", "Their USD-denominated debt becomes cheaper to service"],
         "answer": "They receive more Rupees for their USD revenue",
         "exp": "When USD/INR rises, the Rupee has depreciated. Exporters benefit because their USD earnings translate into more local currency (INR)."},
        {"q": "According to the 'International Fisher Effect', if interest rates in Country A are significantly higher than Country B, Country A's currency is expected to:",
         "options": ["Appreciate", "Depreciate", "Stay stable", "Become the world reserve currency"],
         "answer": "Depreciate",
         "exp": "The theory suggests higher nominal rates compensate for higher expected inflation. High inflation usually leads to currency depreciation over the long term to maintain PPP."}
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q11_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 11 of 12 &nbsp;|&nbsp; Next: <strong>Module 12 — Ethics & Professional Standards</strong></div>', unsafe_allow_html=True)