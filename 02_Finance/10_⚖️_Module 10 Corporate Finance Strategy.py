import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 10 · Corporate Finance Strategy", page_icon="♟️", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Crimson+Pro:wght@300;400;600&display=swap');
html, body, [class*=\"css\"] { font-family: 'Crimson Pro', serif; }
.hero { background: linear-gradient(135deg, #0a0a0a 0%, #1a3a1a 50%, #2d6a2d 100%); border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '♟️'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.12); color: #9ae6b4; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Cinzel', serif; color: #fff; font-size: 38px; margin: 0 0 12px 0; line-height: 1.2; }
.hero p { color: #9ae6b4; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #c6f6d5; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #2d6a2d; }
.card h3 { font-family: 'Cinzel', serif; color: #0a3d0a; font-size: 15px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 15px; line-height: 1.7; margin: 0; }
.insight { background: #f0fff4; border-left: 4px solid #38a169; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #276749; font-size: 15px; margin: 0; line-height: 1.6; }
.sh { font-family: 'Cinzel', serif; color: #0a3d0a; font-size: 22px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #c6f6d5; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #c6f6d5; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#0a3d0a,#38a169); border-radius: 10px; height: 6px; width: 83%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 10 of 12</div>
<h1>Corporate Finance Strategy</h1>
<p>The high-level financial decisions that shape a company's destiny — M&A, dividend policy, buybacks, going public, and restructuring.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#2d6a2d;margin-bottom:4px;"><span>Course progress</span><span>Module 10 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🤝 M&A", "💰 Dividends & Buybacks", "🚀 IPO & Funding", "🔧 Restructuring", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">Mergers & Acquisitions</div>', unsafe_allow_html=True)
    topics = [
        ("Types of M&A", "Merger: two companies combine into one. Acquisition: one company buys another. Types by direction: Horizontal (same industry — scale benefits), Vertical (up/downstream — supply chain control), Conglomerate (unrelated industries — diversification)."),
        ("Synergies", "The key justification for paying a premium. Revenue synergies (cross-selling, market share) + Cost synergies (redundancy elimination, procurement leverage) = Total synergy value. Must exceed the premium paid for value creation."),
        ("Accretion / Dilution Analysis", "In a stock-for-stock merger: if the acquirer's P/E > target's P/E (adjusted for exchange ratio), the deal is EPS-accretive. If acquirer P/E < target P/E, EPS dilution occurs. Management targets accretive deals but dilutive deals can still create value if synergies materialise."),
        ("Deal Structures", "Cash deal: simple but acquirer bears all risk. Stock deal: target shareholders share in future upside/risk. Mixed consideration common. Earnouts (contingent payments) used when future performance is uncertain."),
        ("Due Diligence", "Comprehensive investigation before deal close. Financial DD (audit quality, EBITDA adjustments), Legal DD (contracts, litigation), Commercial DD (market position, customer concentration), Tax DD, and HR DD."),
        ("Hostile Takeovers & Defences", "Hostile bid: approach directly to target shareholders without board approval. Target defences: poison pill (dilutive share issuance rights), staggered board, golden parachutes, white knight (friendly acquirer), Pac-Man defence."),
    ]
    for t, b in topics:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">Dividend Policy</div>', unsafe_allow_html=True)
    div_theories = [
        ("Dividend Irrelevance Theory (M&M)", "In perfect markets, dividend policy is irrelevant — investors can create their own dividends by selling shares (homemade dividends). Firm value depends only on investment decisions, not payout decisions."),
        ("Bird-in-the-Hand Theory", "Investors prefer current dividends (certain) over capital gains (uncertain), so higher dividends reduce required return and increase value. Counter to M&M."),
        ("Tax Preference Theory", "If capital gains are taxed at lower rates than dividends, investors prefer retained earnings (lower effective tax). Firm should pay less dividends."),
        ("Signalling Hypothesis", "Dividends signal management's confidence in future earnings. Dividend cuts are seen very negatively by the market. Initiating or increasing dividends sends a positive signal."),
        ("Residual Dividend Policy", "Dividends = Earnings − Equity retained for positive NPV projects. Maximises shareholder value from investment perspective but results in volatile dividends."),
    ]
    for t, b in div_theories:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sh">Share Buybacks</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Why Companies Prefer Buybacks Over Dividends</h3>
        <p>Share buybacks (share repurchases) have several advantages: (1) Tax efficiency — capital gains taxed lower than dividends in many jurisdictions; (2) Flexibility — unlike dividends, buybacks can be done opportunistically without creating an "expectation" that must be maintained; (3) EPS accretion — fewer shares → higher EPS, supporting share price; (4) Signal of undervaluation — management buying back shares signals confidence; (5) Capital structure optimisation — can increase leverage to WACC-optimal level.</p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="sh">Company Funding Lifecycle & IPO</div>', unsafe_allow_html=True)
    
    stages = [
        ("Seed Stage", "Friends & family, angel investors. ₹10L − ₹2Cr. Proof of concept. Very high risk. Valuation highly subjective."),
        ("Series A", "Early-stage VC. ₹5Cr − ₹50Cr. Product-market fit demonstrated. Revenue model visible."),
        ("Series B & C", "Growth-stage VC / PE. ₹50Cr − ₹500Cr. Scaling operations. Market leadership being established."),
        ("Pre-IPO / Late Stage", "PE funds, sovereign wealth funds. ₹500Cr+. Preparing for liquidity event. Revenue / EBITDA positive."),
        ("IPO (Initial Public Offering)", "Company lists on stock exchange. Public raises capital. Existing investors achieve liquidity. Requires SEBI (India) / SEC (US) compliance."),
        ("Post-IPO Growth", "Ongoing access to capital markets — FPOs (Follow-on Public Offers), QIPs, bonds. Enhanced brand and credibility."),
    ]
    
    for stage, desc in stages:
        st.markdown(f"""
        <div style="background:#fff;border:1px solid #c6f6d5;border-radius:10px;padding:14px 18px;margin-bottom:10px;display:flex;gap:14px;align-items:flex-start;">
            <div style="background:#2d6a2d;color:#fff;border-radius:6px;padding:4px 12px;font-size:12px;font-weight:600;flex-shrink:0;white-space:nowrap;">{stage}</div>
            <div style="color:#4a5568;font-size:14px;line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="insight"><p><strong>IPO Pricing:</strong> Determined by book building (institutional orders) or fixed price method. Underwriters (investment banks) set the price band, build the book, and stabilise post-listing. IPO underpricing (first-day pop) is common globally, averaging 15-20%, benefiting institutional investors at the expense of the issuing company.</p></div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="sh">Corporate Restructuring</div>', unsafe_allow_html=True)
    restructuring = [
        ("Financial Restructuring", "Changing the capital structure — debt renegotiation, debt-for-equity swaps, rights issues to reduce leverage, refinancing at lower rates. Done when the company is financially distressed."),
        ("Operational Restructuring", "Cost-cutting, workforce reductions, plant closures, supply chain optimisation. Aimed at improving margins and cash flow."),
        ("Portfolio Restructuring", "Divesting non-core businesses to focus on core competencies. Spin-offs (separate company), carve-outs (partial IPO), and asset sales all unlock hidden value."),
        ("Turnaround Management", "Comprehensive restructuring of a distressed company combining financial, operational, and strategic initiatives. Requires strong leadership and creditor support."),
        ("Insolvency & Bankruptcy", "IBC (Insolvency and Bankruptcy Code) in India: 180-day resolution period. CIRP (Corporate Insolvency Resolution Process). Committee of Creditors (CoC) approves resolution plans. Liquidation is the last resort."),
    ]
    for t, b in restructuring:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="sh">Knowledge Check — Module 10</div>', unsafe_allow_html=True)
    qs = [
        {"q": "A company's EPS is ₹10 and it trades at P/E of 20×. It acquires a target at P/E of 15× using stock. The deal is:",
         "options": ["Dilutive to EPS", "Accretive to EPS", "EPS-neutral", "Cannot be determined"],
         "answer": "Accretive to EPS",
         "exp": "In a stock-for-stock deal, if the acquirer's P/E (20×) > target's P/E (15×), the deal is EPS-accretive. The acquirer exchanges high-P/E stock for lower-P/E earnings, increasing combined EPS. If acquirer P/E < target P/E, the deal is dilutive."},
        {"q": "The 'signalling hypothesis' of dividend policy suggests that:",
         "options": [
             "Higher dividends always increase firm value",
             "Dividend changes convey management's expectations about future earnings",
             "Dividends should only be paid from residual earnings",
             "Tax treatment of dividends is the primary driver of payout policy"
         ], "answer": "Dividend changes convey management's expectations about future earnings",
         "exp": "The signalling hypothesis (Bhattacharya, 1979) argues that dividends convey private information from management to investors. A dividend increase signals management's confidence in future earnings, while a cut signals deterioration — markets react strongly to dividend changes."},
        {"q": "In the IBC (Insolvency and Bankruptcy Code) process in India, the maximum time allowed for the CIRP is:",
         "options": ["90 days", "270 days", "365 days", "180 days"],
         "answer": "270 days",
         "exp": "The CIRP under IBC allows 180 days initially, extendable by 90 days with CoC approval, totalling 270 days. If no resolution plan is approved within this period, the NCLT orders liquidation of the company."},
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q10_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 10 of 12 &nbsp;|&nbsp; Next: <strong>Module 11 — International & Treasury Finance</strong></div>', unsafe_allow_html=True)