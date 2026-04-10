import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 8 · Financial Markets & Instruments", page_icon="📈", layout="wide")
except st.errors.StreamlitAPIException:
    pass

STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.hero { background: linear-gradient(135deg, #003049 0%, #006494 50%, #0496ff 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '📈'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.15); color: #90e0ef; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'DM Serif Display', serif; color: #fff; font-size: 42px; margin: 0 0 12px 0; }
.hero p { color: #90e0ef; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #caf0f8; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #006494; }
.card h3 { font-family: 'DM Serif Display', serif; color: #003049; font-size: 17px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }
.formula-box { background: #e0f7fa; border-radius: 8px; padding: 14px 18px; font-family: 'Courier New', monospace; font-size: 14px; color: #003049; margin: 10px 0; font-weight: 600; }
.insight { background: #e0f7fa; border-left: 4px solid #006494; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #003049; font-size: 14px; margin: 0; line-height: 1.6; }
.sh { font-family: 'DM Serif Display', serif; color: #003049; font-size: 24px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #caf0f8; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #caf0f8; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#003049,#0496ff); border-radius: 10px; height: 6px; width: 66%; }
</style>
"""
st.markdown(STYLE, unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 8 of 12</div>
<h1>Financial Markets & Instruments</h1>
<p>Understand the architecture of global financial markets, how capital flows between participants, and the instruments that enable that flow.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#006494;margin-bottom:4px;"><span>Course progress</span><span>Module 8 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Market Structure", "📜 Instruments", "📉 Yield Curves", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">Financial Market Structure</div>', unsafe_allow_html=True)
    markets = [
        ("Money Markets", "Short-term debt instruments with maturity ≤ 1 year. Highly liquid and low-risk. Instruments: Treasury Bills, Commercial Paper, Certificates of Deposit, Repo agreements. Used for short-term funding and liquidity management."),
        ("Capital Markets", "Long-term financing — equity and debt with maturity > 1 year. Divided into: Primary markets (new issuances — IPO, FPO, bond issuance) and Secondary markets (trading of existing securities — NSE, BSE, NYSE)."),
        ("Equity Markets", "Markets where company ownership (shares) is traded. Equity holders are residual claimants — they receive returns after all obligations are met. Key metrics: P/E, P/BV, dividend yield, market capitalisation."),
        ("Debt Markets (Bond Markets)", "Markets for fixed-income securities. Issuers: governments (G-Secs, T-Bills), corporations (corporate bonds, debentures). Bond price and yield move inversely. Duration measures interest rate sensitivity."),
        ("Derivatives Markets", "Markets for contracts whose value derives from an underlying asset. Types: Futures, Options, Forwards, Swaps. Used for hedging, speculation, and arbitrage. Notional value of global derivatives market exceeds $1 quadrillion."),
        ("Foreign Exchange (FX) Markets", "Largest and most liquid market in the world (~$7.5 trillion/day). Operates 24/5 globally. Key rate types: spot, forward, swap. Central banks intervene to manage exchange rate volatility."),
        ("Commodity Markets", "Physical and derivative markets for raw materials (oil, metals, agricultural products). Important for corporates to hedge input cost risk."),
    ]
    for t, b in markets:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">Key Financial Instruments</div>', unsafe_allow_html=True)
    
    categories = {
        "Equity Instruments": [
            ("Ordinary Shares (Common Stock)", "Ownership stake. Voting rights. Residual claim on profits (dividend) and assets (on liquidation). Highest risk, highest potential return."),
            ("Preference Shares", "Fixed dividend (priority over ordinary shares). Usually no voting rights. Hybrid — characteristics of both debt and equity."),
            ("Warrants", "Right (not obligation) to buy shares at a fixed price before expiry. Like long-dated call options issued by the company itself."),
        ],
        "Debt Instruments": [
            ("Bonds / Debentures", "Fixed coupon paid periodically. Principal returned at maturity. Bond price = PV of coupons + PV of face value. Price moves inversely with yield."),
            ("Zero Coupon Bonds", "No interim payments. Issued at a deep discount; redeemed at face value. Return = capital appreciation."),
            ("Floating Rate Notes (FRNs)", "Coupon resets periodically based on a benchmark rate (LIBOR, SOFR, MIBOR). Protects investor from rising rates."),
        ],
        "Derivatives": [
            ("Futures", "Standardised contract to buy/sell an asset at a fixed price on a future date. Exchange-traded. Marked to market daily. Used for hedging and speculation."),
            ("Options", "Right (not obligation) to buy (call) or sell (put) at a fixed strike price. Buyer pays premium. Used for hedging asymmetric risk."),
            ("Interest Rate Swaps", "Exchange of fixed interest payments for floating rate payments (or vice versa). Most common OTC derivative. Used by corporates to manage interest rate exposure."),
            ("Currency Forwards", "Agreement to exchange currencies at a fixed rate on a future date. Used by exporters and importers to lock in exchange rates."),
        ],
    }
    
    for category, instruments in categories.items():
        st.markdown(f"#### {category}")
        for name, desc in instruments:
            st.markdown(f'<div class="card"><h3>{name}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="sh">Yield Curve Analysis</div>', unsafe_allow_html=True)
    st.markdown("The yield curve plots interest rates vs. maturity. Its shape signals economic conditions.")
        
    yield_type = st.selectbox("Select Yield Curve Shape:", ["Normal (Upward sloping)", "Inverted (Downward sloping)", "Flat", "Humped"])
    
    maturities = [0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30]
    
    curves = {
        "Normal (Upward sloping)": [4.5, 4.8, 5.2, 5.8, 6.2, 6.8, 7.2, 7.5, 7.8, 8.0],
        "Inverted (Downward sloping)": [7.5, 7.3, 7.0, 6.5, 6.2, 5.8, 5.5, 5.3, 5.1, 5.0],
        "Flat": [6.0, 6.1, 6.0, 6.1, 6.0, 6.1, 6.0, 6.1, 6.0, 6.1],
        "Humped": [5.0, 5.5, 6.5, 7.2, 7.5, 7.2, 6.8, 6.5, 6.3, 6.0],
    }
    
    yields = curves[yield_type]
    df = pd.DataFrame({"Maturity (Years)": maturities, "Yield (%)": yields})
    st.line_chart(df.set_index("Maturity (Years)"))
    
    interpretations = {
        "Normal (Upward sloping)": "Long-term rates > short-term rates. Normal in a healthy economy. Reflects time preference and inflation expectations. Positive carry for banks (borrow short, lend long).",
        "Inverted (Downward sloping)": "Short-term rates > long-term rates. Strong predictor of recession. Signals tight monetary policy or flight to quality.",
        "Flat": "Short and long-term rates are similar. Transitional phase — economy moving between expansion and contraction.",
        "Humped": "Medium-term rates highest. Rare. Occurs during monetary policy transitions or periods of unusual uncertainty.",
    }
    
    st.markdown(f'<div class="insight"><p><strong>{yield_type}:</strong> {interpretations[yield_type]}</p></div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 8</div>', unsafe_allow_html=True)
    qs = [
        {"q": "An inverted yield curve (short-term rates > long-term rates) historically signals:",
         "options": ["Strong economic growth ahead", "An impending recession", "Rising inflation", "A booming stock market"],
         "answer": "An impending recession",
         "exp": "An inverted yield curve signals that investors expect future economic weakness and rate cuts, driving long-term yields below short-term ones."},
        {"q": "A call option gives the holder the right to:",
         "options": ["Sell the underlying asset at the strike price", "Buy the underlying asset at the strike price", "Receive fixed interest payments", "Sell the option at market price"],
         "answer": "Buy the underlying asset at the strike price",
         "exp": "A call option gives the right (not obligation) to BUY the underlying asset at the strike price."},
        {"q": "Bond prices and bond yields have what relationship?",
         "options": ["Direct (move together)", "Inverse (move opposite)", "No relationship", "They converge at maturity only"],
         "answer": "Inverse (move opposite)",
         "exp": "When yields rise, the discount rate increases, reducing PV → price falls."},
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q8_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 8 of 12 &nbsp;|&nbsp; Next: <strong>Module 9 — Risk Management</strong></div>', unsafe_allow_html=True)