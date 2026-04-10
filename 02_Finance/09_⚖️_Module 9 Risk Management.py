import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 9 · Risk Management", page_icon="🛡️", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.hero { background: linear-gradient(135deg, #1a1a2e 0%, #c62a2a 50%, #e53e3e 100%); border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '🛡️'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.15); color: #fed7d7; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Merriweather', serif; color: #fff; font-size: 40px; margin: 0 0 12px 0; }
.hero p { color: #fed7d7; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #fed7d7; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #e53e3e; }
.card h3 { font-family: 'Merriweather', serif; color: #1a1a2e; font-size: 16px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }
.formula-box { background: #fff5f5; border-radius: 8px; padding: 14px 18px; font-family: 'Courier New', monospace; font-size: 14px; color: #c62a2a; margin: 10px 0; font-weight: 600; }
.insight { background: #fff5f5; border-left: 4px solid #e53e3e; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #c62a2a; font-size: 14px; margin: 0; line-height: 1.6; }
.sh { font-family: 'Merriweather', serif; color: #1a1a2e; font-size: 22px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #fed7d7; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #fed7d7; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#1a1a2e,#e53e3e); border-radius: 10px; height: 6px; width: 75%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 9 of 12</div>
<h1>Risk Management</h1>
<p>Identify, measure, and mitigate the financial risks that every business faces — from market and credit risk to operational and enterprise-wide threats.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#c62a2a;margin-bottom:4px;"><span>Course progress</span><span>Module 9 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Risk Types", "🔢 Risk Metrics", "🛡️ Hedging Strategies", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">Types of Financial Risk</div>', unsafe_allow_html=True)
    risks = [
        ("Market Risk", "Risk of losses from adverse movements in market prices — interest rates, exchange rates, equity prices, commodity prices. Measured by VaR, Duration, Beta, and Greeks (for derivatives)."),
        ("Credit Risk", "Risk that a counterparty fails to meet their financial obligations. Includes default risk, downgrade risk, and concentration risk. Managed through credit scoring, collateral, covenants, and credit derivatives (CDS)."),
        ("Liquidity Risk", "Risk of being unable to meet financial obligations as they fall due, or being unable to sell an asset quickly at fair value. Two forms: funding liquidity risk and market liquidity risk."),
        ("Operational Risk", "Risk of losses from inadequate or failed internal processes, systems, human error, or external events. Includes fraud, IT failures, compliance breaches. Basel II categorises and requires capital for op risk."),
        ("Interest Rate Risk", "Risk that changes in interest rates will adversely affect the firm's financial position (earnings or economic value). Particularly critical for banks and bond portfolios."),
        ("Foreign Exchange (FX) Risk", "Risk of financial loss from adverse movements in exchange rates. Three types: Transaction risk (on specific FX cash flows), Translation risk (consolidating overseas subsidiaries), Economic risk (impact on competitive position)."),
        ("Commodity Risk", "Price risk on raw materials (oil, metals, agricultural). Critical for manufacturers, airlines, and utilities. Managed through commodity futures and options."),
        ("Systemic Risk", "Risk of collapse of an entire financial system, not just individual firms. Cannot be diversified away. Examples: 2008 Global Financial Crisis, COVID-19 market shock."),
    ]
    for t, b in risks:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">Key Risk Measurement Metrics</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="formula-box">Value at Risk (VaR): Maximum loss expected at a given confidence level over a period.</div>
    <div style="font-size:13px;color:#718096;padding:4px 8px 12px;">Example: "95% 1-day VaR = ₹10 Cr" means there is a 5% probability of losing more than ₹10 Cr in a single day.</div>
    <div class="formula-box">Expected Shortfall (CVaR) = Average loss in the worst (1−confidence level)% of scenarios</div>
    <div style="font-size:13px;color:#718096;padding:4px 8px 12px;">CVaR is more informative than VaR as it captures the average of the tail losses, not just the cutoff.</div>
    <div class="formula-box">Duration (Macaulay) = Σ [t × PV(CF_t)] / Bond Price</div>
    <div style="font-size:13px;color:#718096;padding:4px 8px 12px;">Duration measures the weighted average time to receive cash flows. It also approximates the % change in bond price for a 1% change in yield.</div>
    <div class="formula-box">Credit VaR = Unexpected Credit Loss = WCL − EL</div>
    <div style="font-size:13px;color:#718096;padding:4px 8px 12px;">Banks hold capital for unexpected credit losses (CVaR), while expected losses (EL = PD × LGD × EAD) are priced into loan spreads.</div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sh">Enterprise Risk Management (ERM) Framework</div>', unsafe_allow_html=True)
    erm_steps = [
        ("1. Risk Identification", "Systematic identification of all risks using tools like risk registers, SWOT, PESTEL, scenario analysis."),
        ("2. Risk Assessment", "Quantifying each risk by Likelihood × Impact. Plotted on a risk heat map. Risks prioritised for management."),
        ("3. Risk Response", "For each significant risk: Avoid, Reduce (mitigate), Transfer (insurance, derivatives), or Accept (if within risk appetite)."),
        ("4. Risk Monitoring", "Ongoing monitoring using KRIs (Key Risk Indicators), dashboards, and internal audit. Risk appetite and limits set by the board."),
        ("5. Reporting", "Regular risk reporting to the board, audit committee, and regulators. Transparent risk disclosures in annual reports."),
    ]
    for step, desc in erm_steps:
        st.markdown(f"""
        <div style="background:#fff;border:1px solid #fed7d7;border-radius:10px;padding:14px 18px;margin-bottom:10px;display:flex;gap:14px;align-items:flex-start;">
            <div style="background:#e53e3e;color:#fff;border-radius:6px;padding:4px 10px;font-size:13px;font-weight:600;flex-shrink:0;">{step}</div>
            <div style="color:#4a5568;font-size:14px;line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="sh">Hedging Strategies</div>', unsafe_allow_html=True)
    hedges = [
        ("FX Forward Contracts", "An exporter expecting USD 1M in 3 months buys a USD/INR forward contract to lock in the exchange rate today. Eliminates FX transaction risk completely."),
        ("Interest Rate Swaps", "A company with floating rate debt swaps payments with a fixed-rate payer to lock in borrowing costs, protecting against rising rates."),
        ("Commodity Futures", "An airline buys crude oil futures to lock in fuel prices, protecting against price spikes that could devastate margins."),
        ("Options (Protective Put)", "A fund manager buys put options on their equity portfolio to cap downside risk while retaining upside. Insurance-like hedging."),
        ("Natural Hedging", "Matching revenues and costs in the same currency (e.g., a US firm with USD revenues and USD costs has a natural hedge — no derivatives needed)."),
        ("Cross-Currency Swaps", "Used by companies issuing debt in foreign currency to swap both principal and interest payments back into their home currency, eliminating both FX and interest rate risk."),
    ]
    for name, desc in hedges:
        st.markdown(f'<div class="card"><h3>{name}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 9</div>', unsafe_allow_html=True)
    qs = [
        {"q": "A 95% 1-day VaR of ₹50 Cr means:",
         "options": [
             "The company will lose exactly ₹50 Cr tomorrow",
             "There is a 95% probability that the loss will be less than ₹50 Cr tomorrow",
             "There is a 95% probability of losing more than ₹50 Cr",
             "The average loss over 20 days will be ₹50 Cr"
         ], "answer": "There is a 95% probability that the loss will be less than ₹50 Cr tomorrow",
         "exp": "VaR at 95% confidence means there is a 95% chance losses will NOT exceed ₹50 Cr in one day — equivalently, a 5% chance they will exceed ₹50 Cr. VaR is a statistical measure of downside risk, not a certain outcome."},
        {"q": "Which type of FX risk affects the reported consolidated earnings of a multinational company when converting overseas subsidiaries' results?",
         "options": ["Transaction risk", "Translation risk", "Economic risk", "Settlement risk"],
         "answer": "Translation risk",
         "exp": "Translation risk (also called accounting risk) affects the consolidated financial statements when the results of foreign subsidiaries are translated into the parent company's reporting currency at the period-end rate. This can distort reported earnings even if operations are unchanged."},
        {"q": "An airline expects to purchase 10 million litres of jet fuel in 6 months. To hedge rising fuel prices, it should:",
         "options": [
             "Sell crude oil futures today",
             "Buy crude oil futures today",
             "Buy put options on jet fuel today",
             "Sell forward contracts on USD"
         ], "answer": "Buy crude oil futures today",
         "exp": "The airline is a fuel buyer (long physical fuel exposure). To hedge, it takes the opposite position in derivatives: BUY futures today. If prices rise, the futures gain offsets the higher spot purchase cost. Selling futures would increase (not hedge) risk."},
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q9_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 9 of 12 &nbsp;|&nbsp; Next: <strong>Module 10 — Corporate Finance Strategy</strong></div>', unsafe_allow_html=True)