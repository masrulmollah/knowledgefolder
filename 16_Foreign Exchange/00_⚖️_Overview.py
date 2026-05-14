import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💱 Foreign Exchange — Complete Course Overview")
    st.markdown("*Your comprehensive guide to all 12 modules — summaries, formulas, and interactive review tools*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🗺️ Course Map", "📖 Module Summaries", "🧮 Formula Bank",
        "📊 Visual Dashboard", "✅ Master Quiz", "🎓 Study Planner"
    ])

    # ══════════════════════════════════════════════════════════════════
    modules_info = [
        {"num": 1, "title": "Foundations of Foreign Exchange",
         "icon": "💱", "color": "#2E86C1",
         "topics": ["FX market structure", "Spot quotes & bid-ask", "Pip value & cross rates", "Market participants"],
         "key_skill": "Read any FX quote and calculate spreads, pips, and cross rates",
         "difficulty": "Beginner"},

        {"num": 2, "title": "FX Market Infrastructure",
         "icon": "🏦", "color": "#27AE60",
         "topics": ["Trading sessions", "T+2 settlement", "SWIFT & MT messages", "Nostro/Vostro accounts"],
         "key_skill": "Calculate settlement value dates and manage nostro balances",
         "difficulty": "Beginner"},

        {"num": 3, "title": "Exchange Rate Theories",
         "icon": "📐", "color": "#8E44AD",
         "topics": ["PPP (absolute & relative)", "Covered Interest Parity", "Uncovered IRP", "International Fisher Effect"],
         "key_skill": "Apply all five parity conditions and identify arbitrage opportunities",
         "difficulty": "Intermediate"},

        {"num": 4, "title": "Forward Markets & Forward Rate Mathematics",
         "icon": "📅", "color": "#E67E22",
         "topics": ["Forward rate formula", "Forward points", "Covered Interest Arbitrage", "NDFs"],
         "key_skill": "Price forward contracts and detect CIA arbitrage opportunities",
         "difficulty": "Intermediate"},

        {"num": 5, "title": "FX Swaps & Cross-Currency Swaps",
         "icon": "🔄", "color": "#E74C3C",
         "topics": ["FX swap mechanics", "Swap points pricing", "CCBS structure", "CIP basis"],
         "key_skill": "Price FX swaps and compare CCBS vs direct funding costs",
         "difficulty": "Intermediate"},

        {"num": 6, "title": "FX Options — Foundations",
         "icon": "📊", "color": "#1ABC9C",
         "topics": ["Garman-Kohlhagen model", "d1, d2 & option price", "Greeks (Delta, Gamma, Vega, Theta)", "Put-call parity"],
         "key_skill": "Price vanilla FX options using GK and interpret all five Greeks",
         "difficulty": "Intermediate"},

        {"num": 7, "title": "FX Options — Advanced Structures",
         "icon": "🔮", "color": "#3498DB",
         "topics": ["Barrier options (KI/KO)", "Digital options", "Asian options", "Volatility smile & surface"],
         "key_skill": "Price exotic options and interpret the volatility surface",
         "difficulty": "Advanced"},

        {"num": 8, "title": "FX Risk Management",
         "icon": "🛡️", "color": "#2C3E50",
         "topics": ["Transaction, translation & economic exposure", "Parametric VaR", "Minimum variance hedge ratio", "IFRS 9 hedge accounting"],
         "key_skill": "Measure all FX exposures, calculate VaR, and apply IFRS 9",
         "difficulty": "Advanced"},

        {"num": 9, "title": "Macro Drivers of Exchange Rates",
         "icon": "🌍", "color": "#D35400",
         "topics": ["Carry trade mechanics", "Taylor Rule", "Risk-on/off dynamics", "BEER & FEER models"],
         "key_skill": "Analyse macro FX drivers, calculate carry returns, and assess reserves adequacy",
         "difficulty": "Advanced"},

        {"num": 10, "title": "Technical Analysis in FX",
         "icon": "📈", "color": "#16A085",
         "topics": ["Support & resistance", "RSI & MACD", "Fibonacci retracement", "Bollinger Bands"],
         "key_skill": "Apply RSI, MACD, Fibonacci, and Bollinger Bands to FX charts",
         "difficulty": "Intermediate"},

        {"num": 11, "title": "FX in Capital Markets & Corporate Finance",
         "icon": "🏦", "color": "#8E44AD",
         "topics": ["FX-adjusted DCF", "Cross-border M&A FX risk", "Currency-hedged bond returns", "Currency overlay"],
         "key_skill": "Value foreign projects, structure M&A hedges, and compute hedged bond returns",
         "difficulty": "Advanced"},

        {"num": 12, "title": "Regulation, Settlement & Emerging Topics",
         "icon": "⚖️", "color": "#27AE60",
         "topics": ["FX Global Code", "CLS & PvP settlement", "MiFID II best execution", "CBDCs & mBridge"],
         "key_skill": "Apply FX regulation, analyse VWAP execution, and understand CBDC impact",
         "difficulty": "Advanced"},
    ]

    difficulty_colors = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🟠", "Expert": "🔴"}

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("🗺️ Course Map — 12 Modules at a Glance")

        st.markdown("""
        ### Welcome to the Complete Foreign Exchange Course
        This course transforms you from a beginner to a **professional-grade FX practitioner**.
        Below is your complete learning roadmap across **12 comprehensive modules**.
        """)

        for row_start in range(0, len(modules_info), 3):
            cols = st.columns(3)
            for col_idx, mod in enumerate(modules_info[row_start:row_start + 3]):
                with cols[col_idx]:
                    difficulty_icon = difficulty_colors.get(mod["difficulty"], "⚪")
                    st.markdown(f"""
                    <div style="background-color:{mod['color']}22; border-left:5px solid {mod['color']};
                    padding:12px; border-radius:8px; margin-bottom:8px; min-height:180px;">
                    <h4 style="color:{mod['color']}; margin:0;">{mod['icon']} Module {mod['num']}</h4>
                    <strong>{mod['title']}</strong><br>
                    <small>{difficulty_icon} {mod['difficulty']}</small><br><br>
                    <small>🔑 <em>{mod['key_skill']}</em></small>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("📈 Learning Progression")

        learning_path = pd.DataFrame({
            "Phase": ["Phase 1: Foundations", "Phase 2: Instruments", "Phase 3: Risk & Macro", "Phase 4: Professional Application"],
            "Modules": ["1 – 2", "3 – 6", "7 – 9", "10 – 12"],
            "Focus": ["Market structure, quotes, settlement", "Theories, forwards, swaps, options", "Exotics, risk management, macro", "Technical analysis, capital markets, regulation"],
            "Duration": ["~1 week", "~4 weeks", "~3 weeks", "~3 weeks"]
        })
        st.dataframe(learning_path, use_container_width=True, hide_index=True)

        st.subheader("🎓 Professional Relevance")
        cert_df = pd.DataFrame({
            "Role / Certification": ["Treasury Manager / Treasurer", "CFA (CFA Institute)", "FRM (GARP)", "ACI Dealing Certificate", "Investment Banker / DCM"],
            "Modules Most Relevant": [
                "M1-M5, M8 — spot, forwards, swaps, risk management",
                "M3, M6, M8, M9, M11 — theories, options, risk, macro, capital markets",
                "M6, M7, M8 — options pricing, exotic structures, VaR and IFRS 9",
                "M1-M5, M12 — market mechanics, instruments, settlement, regulation",
                "M5, M11, M12 — CCBS, FX-adjusted DCF, cross-border M&A, regulation"
            ],
            "Coverage": ["~90%", "~75%", "~80%", "~85%", "~70%"]
        })
        st.dataframe(cert_df, use_container_width=True, hide_index=True)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("📖 Module-by-Module Summaries")
        st.markdown("Quick reference summaries for all 12 modules.")

        selected_module = st.selectbox("Select a Module to Review:", [
            f"Module {m['num']}: {m['title']}" for m in modules_info
        ])

        mod_num = int(selected_module.split(":")[0].replace("Module ", ""))
        mod = modules_info[mod_num - 1]

        st.markdown(f"## {mod['icon']} Module {mod['num']}: {mod['title']}")
        st.markdown(f"**Difficulty:** {difficulty_colors.get(mod['difficulty'], '⚪')} {mod['difficulty']} | **Key Skill:** {mod['key_skill']}")

        summaries = {
            1: {
                "overview": "The foundation of all FX knowledge — what the market is, how prices are quoted, who trades, and the arithmetic of pips, spreads, and cross rates.",
                "key_concepts": [
                    "FX is a 24/5 OTC market with ~$7.5 trillion daily turnover — the world's largest financial market",
                    "Currency pairs written as BASE/QUOTE — e.g. EUR/USD = 1.0850 means 1 EUR costs 1.0850 USD",
                    "Bid = market maker buys base (you sell); Ask = market maker sells base (you buy)",
                    "Spread = Ask − Bid = dealer profit margin; tighter for liquid pairs",
                    "1 pip = 0.0001 for most pairs; 0.01 for JPY pairs",
                    "Cross Rate (A/C) = Rate(A/B) × Rate(B/C) — derived via the USD"
                ],
                "key_formulas": {
                    "Spread (pips)": "Ask − Bid  (divide by 0.0001)",
                    "Pip Value": "(Pip Size / Exchange Rate) × Lot Size",
                    "Cross Rate": "Rate(A/B) × Rate(B/C)",
                    "Trade P&L (long)": "(Exit Rate − Entry Rate) × Lot Size",
                    "Spread Cost": "(Ask − Bid) × Notional"
                },
                "exam_tips": [
                    "You always BUY at the ask and SELL at the bid — the spread is always against you",
                    "For JPY pairs: 1 pip = 0.01 (not 0.0001) — a classic calculation error",
                    "Cross rate arbitrage: if market rate ≠ calculated cross rate, a triangular arbitrage exists"
                ]
            },
            2: {
                "overview": "The plumbing behind every FX trade — settlement timing, nostro management, SWIFT messaging, and how the 24-hour market operates across global sessions.",
                "key_concepts": [
                    "FX trades 24/5 across Sydney → Tokyo → London → New York sessions",
                    "Standard spot settlement: T+2 business days (USD/CAD and USD/TRY: T+1)",
                    "Nostro = our account at a foreign bank (in foreign currency); Vostro = their account at our bank",
                    "SWIFT sends instructions, not funds — MT300 confirms FX trades; MT103 moves payments",
                    "CLS Bank eliminates Herstatt (settlement) risk via Payment-vs-Payment (PvP)",
                    "London session (~38% of volume) has the tightest spreads; London-NY overlap is peak liquidity"
                ],
                "key_formulas": {
                    "Value Date": "Trade Date + 2 Business Days (skip weekends & holidays)",
                    "Nostro Balance": "Opening + Inflows − Outflows",
                    "Correspondent Fee": "Fixed fee + Variable fee (bps × notional)"
                },
                "exam_tips": [
                    "T+2 skips weekends AND public holidays in BOTH currency countries",
                    "SWIFT moves instructions only — settlement happens through nostro/correspondent accounts",
                    "CLS: PvP means if one party cannot pay, NEITHER payment settles — no principal loss"
                ]
            },
            3: {
                "overview": "The theoretical underpinnings of exchange rates — five parity conditions that link inflation, interest rates, and FX changes into one unified framework.",
                "key_concepts": [
                    "Relative PPP: exchange rate change ≈ inflation differential (long-run anchor)",
                    "Covered IRP (CIP): F = S × (1+i_d)/(1+i_f) — arbitrage-enforced, no currency risk",
                    "Uncovered IRP (UIP): E(%ΔS) ≈ i_d − i_f — frequently FAILS in practice",
                    "UIP failure = basis of carry trade: borrow low-yield, invest high-yield",
                    "IFE unifies all parity conditions: (1+i_d)/(1+i_f) = (1+π_d)/(1+π_f) = E(S1)/S0",
                    "Post-2008 CIP basis: bank balance sheet constraints prevent full CIP arbitrage"
                ],
                "key_formulas": {
                    "Relative PPP": "E(S1) = S0 × (1 + π_d) / (1 + π_f)",
                    "PPP Approximation": "%ΔS ≈ π_d − π_f",
                    "CIP Forward": "F = S × (1 + i_d × T/360) / (1 + i_f × T/360)",
                    "UIP": "E(%ΔS) ≈ i_d − i_f",
                    "Fisher Effect": "i_nominal ≈ r_real + π_expected",
                    "Carry Return": "i_high − i_low − actual FX depreciation"
                },
                "exam_tips": [
                    "CIP is arbitrage-enforced — any deviation creates a riskless profit (CIA in Module 4)",
                    "UIP FAILS empirically — that failure IS the carry trade (borrow JPY, invest AUD)",
                    "IFE: when real rates are equal globally, all three parity conditions give the same answer"
                ]
            },
            4: {
                "overview": "Forward contracts are the most widely used FX hedging instrument. The forward rate is NOT a forecast — it is the CIP arbitrage-free price derived from spot and interest rates.",
                "key_concepts": [
                    "Forward rate = S × (1+i_d×T/360) / (1+i_f×T/360) — entirely determined by spot and rates",
                    "Forward points = (F − S) × 10,000 — positive means base at premium",
                    "Importers BUY forward (lock in purchase rate); Exporters SELL forward (lock in sale rate)",
                    "CIA: if actual forward ≠ CIP forward, riskless profit is available",
                    "NDFs: cash-settled in USD for restricted currencies (CNY, INR, BRL, KRW)",
                    "NDF settlement = (NDF Rate − Fixing) / Fixing × Notional (USD)"
                ],
                "key_formulas": {
                    "Forward Rate": "F = S0 × (1 + i_d × T/360) / (1 + i_f × T/360)",
                    "Forward Points": "(F − S0) × 10,000",
                    "Forward Premium %": "(F − S0) / S0 × 360/T × 100",
                    "NDF Settlement": "(NDF Rate − Fixing Rate) / Fixing Rate × Notional",
                    "CIA Profit": "(F_actual − F_CIP) × Foreign Maturity Proceeds"
                },
                "exam_tips": [
                    "The forward rate tells you NOTHING about where spot will be — it is purely an arbitrage-free price",
                    "Positive forward points = ADD to spot; negative = SUBTRACT from spot",
                    "For CIA: if F_actual > F_CIP, borrow domestic → invest foreign → sell overpriced forward"
                ]
            },
            5: {
                "overview": "FX swaps are the largest FX instrument by volume. Understanding swap pricing, CCBS structure, and the cross-currency basis is essential for treasury and capital markets professionals.",
                "key_concepts": [
                    "FX swap = near leg (spot) + far leg (forward) in OPPOSITE directions, same notional",
                    "Swap points ≈ S × (i_d − i_f) × T/360 — cost equals the interest differential",
                    "CCBS: exchange floating coupons in two currencies + principal at start and maturity (1–30Y)",
                    "CIP basis = persistent CIP deviation; negative EUR/USD basis = USD at a premium",
                    "Basis widens in stress (GFC: −200 bps; COVID March 2020: −120 bps)",
                    "CCBS used for cross-currency funding: European bank converts EUR bonds → cheaper USD"
                ],
                "key_formulas": {
                    "FX Swap Far Leg": "Far Leg Rate = S × (1+i_d×T/360)/(1+i_f×T/360)",
                    "Swap Points (approx.)": "S × (i_d − i_f) × T/360",
                    "CCBS Effective USD Cost": "Foreign yield + (r_domestic − r_foreign) + CCS Basis",
                    "Annualised Swap Cost": "(F − S) / S × 360/T × 100"
                },
                "exam_tips": [
                    "Sell-Buy swap: SELL base at spot (near leg), BUY base at forward (far leg)",
                    "Negative CCS basis = USD in excess demand — a key market stress indicator",
                    "CCBS vs FX swap: CCBS has coupons and can be years long; FX swaps are typically short-dated"
                ]
            },
            6: {
                "overview": "The Garman-Kohlhagen (GK) model prices FX vanilla options. The five Greeks measure option sensitivities and drive daily risk management on every FX trading desk globally.",
                "key_concepts": [
                    "GK extends Black-Scholes: r_f (foreign rate) treated as a continuous dividend yield",
                    "d1, d2 → N(d1), N(d2) → Call/Put prices via the GK formula",
                    "Delta: price change per 1 unit spot move (ATM call ≈ 0.50)",
                    "Gamma: delta change per 1 unit spot move — highest at ATM",
                    "Vega: price change per 1% vol move — most important Greek for options traders",
                    "Put-call parity: C − P = S·e^(−rf·T) − K·e^(−rd·T)"
                ],
                "key_formulas": {
                    "d1": "[ln(S/K) + (r_d − r_f + σ²/2)×T] / (σ×√T)",
                    "d2": "d1 − σ×√T",
                    "Call Price": "S×e^(−rf×T)×N(d1) − K×e^(−rd×T)×N(d2)",
                    "Put Price": "K×e^(−rd×T)×N(−d2) − S×e^(−rf×T)×N(−d1)",
                    "Put-Call Parity": "C − P = S×e^(−rf×T) − K×e^(−rd×T)",
                    "Delta Hedge": "Sell Delta × Notional units of base currency"
                },
                "exam_tips": [
                    "r_d = QUOTE currency rate; r_f = BASE currency rate — this is the most common GK error",
                    "T must be in YEARS: 90 days = 90/365 = 0.2466Y (not 90/360)",
                    "ATM options have the most time value AND the highest vega AND gamma"
                ]
            },
            7: {
                "overview": "Beyond vanilla options — barrier options, digitals, and Asian options, plus the volatility surface that captures the market's true option pricing across all strikes and tenors.",
                "key_concepts": [
                    "Knock-Out (KO): option dies if spot hits barrier — cheaper, but protection disappears",
                    "Knock-In (KI): option activates only if spot reaches barrier — cheaper, may never exist",
                    "Digital call = fixed payout if S_T > K; price ≈ e^(−rd×T)×N(d2)",
                    "Asian option: payoff based on average rate — 20-35% cheaper than vanilla",
                    "Volatility smile: OTM options are priced at higher IV than ATM in FX markets",
                    "RR = IV(25D call) − IV(25D put); BF = [IV(25D C)+IV(25D P)]/2 − ATM"
                ],
                "key_formulas": {
                    "Digital Call Price": "e^(−r_d×T) × N(d2)",
                    "Digital Put Price": "e^(−r_d×T) × N(−d2)",
                    "25D Risk Reversal": "IV(25D Call) − IV(25D Put)",
                    "25D Butterfly": "[IV(25D Call) + IV(25D Put)] / 2 − IV(ATM)",
                    "Asian Effective Vol": "σ × √[(2n+1) / (6(n+1))]"
                },
                "exam_tips": [
                    "KO options are cheaper but protection disappears when spot hits the barrier — PIN RISK near barrier",
                    "Digital option price = risk-neutral probability of expiring ITM × discount factor",
                    "Negative RR (EUR/USD) = OTM puts > OTM calls = market fears EUR downside"
                ]
            },
            8: {
                "overview": "FX risk management is a core treasury function — measuring all three exposure types, calculating VaR, optimising hedge ratios, and meeting IFRS 9 hedge accounting requirements.",
                "key_concepts": [
                    "Transaction: contracted future foreign cash flows — hedge with forwards/options",
                    "Translation: converting foreign subsidiary accounts — hedge with CCBS/balance sheet matching",
                    "Economic: long-term competitive position — managed operationally",
                    "Parametric VaR = Position × σ_daily × Z × √T (Z: 99%=2.326; 95%=1.645)",
                    "Optimal hedge ratio h* = ρ × (σ_S/σ_F) — minimises residual variance",
                    "IFRS 9 effectiveness test: 80%–125% band required for hedge accounting"
                ],
                "key_formulas": {
                    "Net FX Exposure": "Total Foreign Inflows − Total Foreign Outflows",
                    "Parametric VaR": "Position × σ_daily × Z × √T",
                    "T-Day VaR": "VaR_1d × √T",
                    "Hedge Ratio (h*)": "ρ × (σ_Spot / σ_Hedge)",
                    "Hedge Notional": "h* × Exposure Notional",
                    "IFRS 9 Effectiveness": "|ΔFV_Hedge| / |ΔFV_Item| × 100%"
                },
                "exam_tips": [
                    "Always net inflows vs outflows FIRST — only hedge the residual net exposure",
                    "h* < 1 when hedge instrument is more volatile than spot (σ_F > σ_S)",
                    "IFRS 9 cash flow hedge: gains/losses go to OCI first, reclassified to P&L when hedged item affects income"
                ]
            },
            9: {
                "overview": "Central banks, interest rate differentials, carry trade, and global risk sentiment are the dominant short-to-medium term FX drivers — understanding these is essential for FX forecasting.",
                "key_concepts": [
                    "Carry trade: borrow low-yield (JPY), invest high-yield (AUD) — profits from UIP failure",
                    "Risk-OFF: sell AUD/NZD/EM, buy JPY/CHF/USD (safe havens); Risk-ON: reverse",
                    "Taylor Rule: i = r* + π + α(π−π*) + β(y−y*) — guides CB rate expectations",
                    "BEER: macro-based medium-term fair value estimate (ToT, NFA, productivity)",
                    "FX reserves adequacy: > 3 months import cover and > 100% short-term debt coverage",
                    "Carry unwinds are violent — a year of carry can be lost in hours during stress"
                ],
                "key_formulas": {
                    "Carry Return": "i_high − i_low − actual spot depreciation of HY currency",
                    "Taylor Rule Rate": "r* + π + α(π − π*) + β(y − y*)",
                    "Import Cover": "FX Reserves / Monthly Imports  (target: > 3 months)",
                    "Debt Coverage": "FX Reserves / Short-term External Debt  (target: > 100%)",
                    "BEER Misalignment": "(Actual Rate − BEER Fair Value) / BEER × 100%"
                },
                "exam_tips": [
                    "CB is BEHIND the curve if actual rate < Taylor rate → expect hikes → bullish currency",
                    "Carry trade positive in calm markets; catastrophic in risk-off — always size with stops",
                    "VIX > 25 = risk-off; VIX > 35 = aggressive risk reduction in carry and EM positions"
                ]
            },
            10: {
                "overview": "Technical analysis provides timing signals for FX entries and exits. Combine multiple indicators for confluence — never trade a single signal in isolation.",
                "key_concepts": [
                    "Support = buying interest floor; Resistance = selling pressure ceiling; role reversal on break",
                    "Golden Cross: 50-day MA crosses above 200-day MA = long-term bullish signal",
                    "RSI > 70 = overbought (potential reversal); RSI < 30 = oversold; divergence = powerful warning",
                    "MACD above Signal Line = bullish momentum; histogram expanding = strengthening trend",
                    "Fibonacci 61.8% = Golden Ratio — strongest retracement support/resistance",
                    "Bollinger Band squeeze = low volatility → major breakout imminent"
                ],
                "key_formulas": {
                    "RSI": "100 − [100 / (1 + Avg Gain / Avg Loss)]",
                    "MACD Line": "EMA(12) − EMA(26)",
                    "Signal Line": "EMA(9) of MACD Line",
                    "BB Upper": "SMA(20) + 2 × Standard Deviation",
                    "BB Lower": "SMA(20) − 2 × Standard Deviation",
                    "Fibonacci Level": "High − (High − Low) × Fibonacci Ratio"
                },
                "exam_tips": [
                    "Golden Cross = 50 above 200 MA (bullish); Death Cross = 50 below 200 MA (bearish)",
                    "RSI divergence is more reliable than absolute overbought/oversold levels",
                    "61.8% Fibonacci (Golden Ratio) is the most significant — use it as primary S&R"
                ]
            },
            11: {
                "overview": "FX expertise applied to capital markets — valuing foreign acquisitions, hedging M&A deal risk, computing hedged bond returns, and structuring currency overlay programs.",
                "key_concepts": [
                    "FX-adjusted DCF: discount at local WACC in local currency, convert at spot (Approach 1)",
                    "Or convert each year's CF at CIP forward rate and discount at home WACC (Approach 2 — both equivalent)",
                    "M&A FX: use OPTIONS (not forwards) for contingent deal exposure — if deal fails, option lapses",
                    "Hedged foreign bond return ≈ domestic risk-free rate (by CIP) + any credit spread",
                    "Currency overlay separates FX management from asset management — specialist overlay managers",
                    "EM WACC = Base WACC + Country Risk Premium + Illiquidity + Political risk"
                ],
                "key_formulas": {
                    "FX-Adjusted NPV (App. 2)": "Sum [CF_local × F_t / (1+WACC_home)^t]",
                    "CIP Forward (year t)": "S0 × [(1+r_d)/(1+r_f)]^t",
                    "Hedged Bond Return": "Foreign Yield + (r_domestic − r_foreign)",
                    "EM WACC": "Base WACC + CRP + Illiquidity + Political Risk Premium",
                    "Currency Alpha": "Actual hedge return − Benchmark hedge return"
                },
                "exam_tips": [
                    "Both DCF approaches give the same NPV under CIP — Approach 2 (use forwards) is more transparent",
                    "Options for M&A: if deal fails, forward = naked FX position; option = lapses losing only premium",
                    "Hedged foreign bond ≈ domestic rate — the credit spread above sovereign IS the value-add"
                ]
            },
            12: {
                "overview": "The regulatory and technological framework of FX — from the voluntary FX Global Code to mandatory MiFID II best execution, Dodd-Frank reporting, and the CBDC revolution ahead.",
                "key_concepts": [
                    "FX Global Code: voluntary, 6 pillars, firms sign Statement of Commitment; non-compliance = market exclusion",
                    "CLS Bank: PvP settlement for 18+ currencies, ~$6.5T/day, eliminates Herstatt risk",
                    "MiFID II best execution: multi-factor test — price, speed, costs, fill rate, market impact",
                    "Dodd-Frank: Swap Dealer registration required if FX derivative notional > $8B/year",
                    "VWAP = execution quality benchmark; IS = (Execution − Arrival price) / Arrival × 10,000 bps",
                    "mBridge CBDC (BIS + CN + AE + TH + HK): atomic PvP settlement in seconds, bypasses correspondent banking"
                ],
                "key_formulas": {
                    "VWAP": "Sum(Price_i × Volume_i) / Sum(Volume_i)",
                    "Implementation Shortfall": "(Exec Price − Arrival Price) / Arrival Price × 10,000 bps",
                    "CLS Netting Efficiency": "(1 − Net Obligation / Gross Obligation) × 100%",
                    "Dodd-Frank Threshold": "> $8B FX derivative notional → Swap Dealer registration",
                    "IFRS 9 Effectiveness": "80% to 125% band required"
                },
                "exam_tips": [
                    "FX Global Code is VOLUNTARY — but non-compliance risks market access and counterparty relationships",
                    "CLS PvP: if one party cannot pay, NEITHER payment settles — principal risk is completely eliminated",
                    "MiFID II best execution is NOT just best price — speed, fill rate, and total cost all matter"
                ]
            },
        }

        summary = summaries[mod_num]

        st.markdown(f"### 📋 Overview")
        st.info(summary["overview"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 💡 Key Concepts")
            for concept in summary["key_concepts"]:
                st.markdown(f"• {concept}")
        with col2:
            st.markdown("### 📐 Key Formulas")
            for formula, expression in summary["key_formulas"].items():
                st.markdown(f"**{formula}:**")
                st.code(expression)

        st.markdown("### 🎯 Exam & Application Tips")
        for tip in summary["exam_tips"]:
            st.warning(f"💡 {tip}")

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("🧮 Formula Bank — All 12 Modules")
        st.markdown("Complete formula reference for the entire FX curriculum.")

        formula_category = st.selectbox("Filter by Category:", [
            "All Formulas",
            "Spot & Basic Calculations (M1-M2)",
            "Parity Theories & Rates (M3-M4)",
            "Swaps & Options Pricing (M5-M6)",
            "Advanced Options & Risk (M7-M8)",
            "Macro, Technical & Capital Markets (M9-M11)",
            "Execution & Regulation (M12)"
        ])

        all_formulas = [
            # M1 Foundations
            ("M1", "Spread (pips)", "Ask − Bid  (divide by pip size 0.0001 or 0.01 for JPY)", "Basic FX arithmetic"),
            ("M1", "Spread (%)", "(Ask − Bid) / Ask × 100", "Transaction cost as percentage"),
            ("M1", "Pip Value", "(Pip Size / Exchange Rate) × Lot Size", "P&L per pip move"),
            ("M1", "Cross Rate", "Rate(A/B) × Rate(B/C) = Rate(A/C)", "Deriving non-USD pairs"),
            ("M1", "Trade P&L (Long)", "(Exit − Entry) × Lot Size", "Profit/loss on a long trade"),
            ("M1", "Trade P&L (Short)", "(Entry − Exit) × Lot Size", "Profit/loss on a short trade"),
            # M2 Infrastructure
            ("M2", "Settlement Value Date", "Trade Date + 2 Business Days (skip weekends & holidays)", "T+2 standard"),
            ("M2", "Nostro Closing Balance", "Opening Balance + Total Inflows − Total Outflows", "Daily treasury management"),
            ("M2", "Correspondent Fee", "Fixed Fee + (Variable bps × Notional)", "Payment cost"),
            # M3 Theories
            ("M3", "Relative PPP", "E(S1) = S0 × (1 + π_d) / (1 + π_f)", "Inflation-based FX forecast"),
            ("M3", "PPP Approximation", "%ΔS ≈ π_d − π_f", "Quick PPP estimate"),
            ("M3", "CIP Forward Rate", "F = S × (1 + i_d × T/360) / (1 + i_f × T/360)", "Arbitrage-free forward"),
            ("M3", "UIP Prediction", "E(%ΔS) ≈ i_d − i_f", "Expected spot change"),
            ("M3", "Fisher Effect", "i_nominal ≈ r_real + π_expected", "Nominal rate decomposition"),
            ("M3", "IFE", "(1+i_d)/(1+i_f) = (1+π_d)/(1+π_f) = E(S1)/S0", "Unified parity framework"),
            ("M3", "Carry Trade Return", "i_high − i_low − actual FX depreciation", "Net carry return"),
            # M4 Forwards
            ("M4", "Forward Rate (full)", "F = S0 × (1 + i_d×T/360) / (1 + i_f×T/360)", "CIP forward pricing"),
            ("M4", "Forward Points", "(F − S0) × 10,000", "Dealer quoting convention"),
            ("M4", "Forward Premium %", "(F − S0) / S0 × 360/T × 100", "Annualised premium/discount"),
            ("M4", "NDF Settlement", "(NDF Rate − Fixing Rate) / Fixing Rate × Notional", "EM currency cash settlement"),
            ("M4", "CIA Profit (approx.)", "(F_actual − F_CIP) × Foreign Maturity Proceeds", "Riskless arbitrage"),
            # M5 Swaps
            ("M5", "FX Swap Far Leg", "S × (1 + i_d × T/360) / (1 + i_f × T/360)", "Same as CIP forward"),
            ("M5", "Swap Points (approx.)", "S × (i_d − i_f) × T/360", "Quick swap cost estimate"),
            ("M5", "Swap Annualised Cost", "(Far Leg − Spot) / Spot × 360/T × 100", "≈ interest differential"),
            ("M5", "CCBS Effective USD Cost", "Foreign Yield + (r_domestic − r_foreign) + Basis", "All-in cross-currency cost"),
            # M6 Options
            ("M6", "d1 (GK)", "[ln(S/K) + (r_d−r_f+σ²/2)×T] / (σ×√T)", "GK key input"),
            ("M6", "d2 (GK)", "d1 − σ×√T", "GK key input"),
            ("M6", "Call Price (GK)", "S×e^(−rf×T)×N(d1) − K×e^(−rd×T)×N(d2)", "Vanilla FX call"),
            ("M6", "Put Price (GK)", "K×e^(−rd×T)×N(−d2) − S×e^(−rf×T)×N(−d1)", "Vanilla FX put"),
            ("M6", "Put-Call Parity", "C − P = S×e^(−rf×T) − K×e^(−rd×T)", "Arbitrage-free parity"),
            ("M6", "Delta Hedge", "Delta × Notional = units to trade in spot market", "Hedge the directional exposure"),
            # M7 Exotics
            ("M7", "Digital Call Price", "e^(−r_d×T) × N(d2)", "Risk-neutral ITM probability"),
            ("M7", "Digital Put Price", "e^(−r_d×T) × N(−d2)", "Risk-neutral ITM probability"),
            ("M7", "25D Risk Reversal", "IV(25D Call) − IV(25D Put)", "Skew / directional sentiment"),
            ("M7", "25D Butterfly", "[IV(25D C) + IV(25D P)] / 2 − IV(ATM)", "Tail risk / kurtosis"),
            ("M7", "Asian Effective Sigma", "σ × √[(2n+1) / (6(n+1))]", "Reduced vol for Asian options"),
            # M8 Risk
            ("M8", "Net FX Exposure", "Total Foreign Inflows − Total Foreign Outflows", "Hedge only the net"),
            ("M8", "Parametric VaR (1-day)", "Position Value × σ_daily × Z_confidence", "99%: Z=2.326; 95%: Z=1.645"),
            ("M8", "T-Day VaR", "VaR_1d × √T", "Scale by square root of time"),
            ("M8", "Minimum Variance h*", "ρ × (σ_Spot / σ_Hedge)", "Optimal hedge ratio"),
            ("M8", "IFRS 9 Effectiveness", "|ΔFV_Hedge| / |ΔFV_Item| × 100%", "Must be 80%–125%"),
            # M9 Macro
            ("M9", "Carry Trade Return", "i_high − i_low − actual spot depreciation", "Net carry trade P&L"),
            ("M9", "Taylor Rule", "i = r* + π + α(π−π*) + β(y−y*)", "CB rate guidance"),
            ("M9", "Import Cover", "FX Reserves / Monthly Imports", "Adequacy target: > 3 months"),
            ("M9", "Debt Coverage", "FX Reserves / ST External Debt × 100%", "Adequacy target: > 100%"),
            # M10 Technical
            ("M10", "RSI", "100 − [100 / (1 + Avg Gain / Avg Loss)]", "Momentum oscillator 0–100"),
            ("M10", "MACD Line", "EMA(12) − EMA(26)", "Trend + momentum"),
            ("M10", "Signal Line", "EMA(9) of MACD Line", "MACD crossover trigger"),
            ("M10", "BB Upper Band", "SMA(20) + 2 × Std Dev(20)", "Upper volatility boundary"),
            ("M10", "BB Lower Band", "SMA(20) − 2 × Std Dev(20)", "Lower volatility boundary"),
            ("M10", "Fibonacci Level", "High − (High−Low) × Ratio", "Key: 23.6%, 38.2%, 50%, 61.8%, 78.6%"),
            # M11 Capital Markets
            ("M11", "FX-Adjusted NPV (App.2)", "Sum [CF_local × F_t / (1+WACC_home)^t]", "Convert at CIP forwards"),
            ("M11", "CIP Forward (year t)", "S0 × [(1+r_d)/(1+r_f)]^t", "Multi-year forward rate"),
            ("M11", "Hedged Bond Return", "Foreign Yield + (r_domestic − r_foreign)", "≈ domestic risk-free rate"),
            ("M11", "EM WACC", "Base WACC + CRP + Illiquidity + Political Premium", "Emerging market projects"),
            # M12 Regulation
            ("M12", "VWAP", "Sum(Price_i × Vol_i) / Sum(Vol_i)", "Execution quality benchmark"),
            ("M12", "Implementation Shortfall", "(Exec − Arrival) / Arrival × 10,000", "bps slippage vs decision price"),
            ("M12", "CLS Netting Efficiency", "(1 − Net / Gross) × 100%", "Typically 96–98%"),
        ]

        cat_filter = {
            "All Formulas": list(range(12)),
            "Spot & Basic Calculations (M1-M2)": [1, 2],
            "Parity Theories & Rates (M3-M4)": [3, 4],
            "Swaps & Options Pricing (M5-M6)": [5, 6],
            "Advanced Options & Risk (M7-M8)": [7, 8],
            "Macro, Technical & Capital Markets (M9-M11)": [9, 10, 11],
            "Execution & Regulation (M12)": [12]
        }

        filtered_mods = cat_filter[formula_category]
        filtered_formulas = [(m, n, f, u) for m, n, f, u in all_formulas
                              if int(m.replace("M", "")) in filtered_mods]

        formula_df = pd.DataFrame(filtered_formulas, columns=["Module", "Formula Name", "Expression", "Use / Notes"])
        st.dataframe(formula_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔍 Formula Lookup")
        search_term = st.text_input("Search for a formula (type any keyword):", placeholder="e.g. VaR, forward, RSI, VWAP...")
        if search_term:
            matches = [(m, n, f, u) for m, n, f, u in all_formulas
                        if search_term.lower() in n.lower() or search_term.lower() in f.lower() or search_term.lower() in u.lower()]
            if matches:
                st.dataframe(pd.DataFrame(matches, columns=["Module", "Name", "Expression", "Notes"]),
                             use_container_width=True, hide_index=True)
            else:
                st.warning(f"No formulas found matching '{search_term}'. Try a different keyword.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("📊 Visual Dashboard")

        st.subheader("Difficulty Progression Across 12 Modules")
        difficulty_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3, "Expert": 4}
        diff_values = [difficulty_map[m["difficulty"]] for m in modules_info]
        diff_colors = [m["color"] for m in modules_info]

        fig_diff = go.Figure(go.Scatter(
            x=list(range(1, 13)),
            y=diff_values,
            mode="lines+markers+text",
            line=dict(color="#2E86C1", width=3),
            marker=dict(size=20, color=diff_colors),
            text=[f"M{m['num']}" for m in modules_info],
            textposition="middle center",
            textfont=dict(color="white", size=10)
        ))
        fig_diff.update_layout(
            title="Difficulty Progression Across 12 Modules",
            xaxis_title="Module Number",
            yaxis=dict(tickvals=[1, 2, 3, 4], ticktext=["Beginner", "Intermediate", "Advanced", "Expert"]),
            hovermode="x unified"
        )
        fig_diff.add_hrect(y0=0.5, y1=1.5, fillcolor="green", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=1.5, y1=2.5, fillcolor="yellow", opacity=0.1, line_width=0)
        fig_diff.add_hrect(y0=2.5, y1=3.5, fillcolor="orange", opacity=0.1, line_width=0)
        st.plotly_chart(fig_diff, use_container_width=True)

        st.subheader("Skills Developed — Full FX Curriculum")
        skill_categories = ["Market Mechanics", "Mathematical Pricing", "Risk Management",
                            "Macro Analysis", "Professional Application", "Regulatory Knowledge"]
        skill_scores = [10, 9, 9, 8, 9, 8]
        skill_scores_r = skill_scores + [skill_scores[0]]
        categories_r   = skill_categories + [skill_categories[0]]

        fig_radar = go.Figure(go.Scatterpolar(
            r=skill_scores_r,
            theta=categories_r,
            fill="toself",
            name="Skills Covered",
            line=dict(color="#2E86C1", width=3),
            fillcolor="rgba(46,134,193,0.3)"
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False,
            title="Skills Developed — All 12 FX Modules Combined"
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        st.subheader("Topics per Module")
        fig_topics = go.Figure(go.Bar(
            x=[f"M{m['num']}" for m in modules_info],
            y=[len(m["topics"]) for m in modules_info],
            marker_color=[m["color"] for m in modules_info],
            text=[f"{len(m['topics'])} topics" for m in modules_info],
            textposition="auto"
        ))
        fig_topics.update_layout(
            title="Number of Major Topics per Module",
            xaxis_title="Module", yaxis_title="Number of Major Topics"
        )
        st.plotly_chart(fig_topics, use_container_width=True)

        st.subheader("FX Market — Key Statistics")
        col1, col2 = st.columns(2)
        with col1:
            instruments = ["FX Swaps", "Spot", "Outright Forwards", "Currency Swaps (CCBS)", "FX Options"]
            volumes     = [3.8, 2.1, 1.1, 0.9, 0.3]
            fig_ins = go.Figure(go.Pie(
                labels=instruments, values=volumes, hole=0.35,
                marker=dict(colors=["#2E86C1", "#27AE60", "#E67E22", "#8E44AD", "#E74C3C"])
            ))
            fig_ins.update_layout(title="Global FX Daily Volume by Instrument ($T, BIS 2022)")
            st.plotly_chart(fig_ins, use_container_width=True)
        with col2:
            pairs   = ["EUR/USD", "USD/JPY", "GBP/USD", "AUD/USD", "USD/CAD", "USD/CHF", "Other"]
            shares  = [23.0, 13.5, 9.6, 5.4, 5.0, 4.7, 38.8]
            fig_pairs = go.Figure(go.Pie(
                labels=pairs, values=shares, hole=0.35,
                marker=dict(colors=["#2E86C1", "#E74C3C", "#27AE60", "#F39C12", "#8E44AD", "#1ABC9C", "#95A5A6"])
            ))
            fig_pairs.update_layout(title="FX Market Share by Currency Pair (%)")
            st.plotly_chart(fig_pairs, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("✅ Master Quiz — All 12 Modules")
        st.markdown("Test your knowledge across the entire FX curriculum with this comprehensive quiz!")

        quiz_mode = st.radio("Quiz Mode:", [
            "Quick Fire (5 questions)", "Standard (10 questions)", "Full Exam (12 questions)"
        ], horizontal=True)
        num_q = {"Quick Fire (5 questions)": 5, "Standard (10 questions)": 10, "Full Exam (12 questions)": 12}[quiz_mode]

        all_quiz_questions = [
            {"q": "EUR/USD is quoted as 1.0845 / 1.0847. What is the spread in pips?",
             "opts": ["1 pip", "2 pips", "3 pips", "0.5 pips"],
             "ans": "2 pips", "mod": 1,
             "exp": "Spread = 1.0847 − 1.0845 = 0.0002 = 2 pips. Divide by 0.0001 per pip."},

            {"q": "Standard spot FX settlement for EUR/USD is:",
             "opts": ["Same day", "T+1", "T+2", "T+3"],
             "ans": "T+2", "mod": 2,
             "exp": "Most FX pairs settle T+2 (two business days). USD/CAD and USD/TRY are T+1 exceptions."},

            {"q": "Covered Interest Rate Parity (CIP) ensures that:",
             "opts": ["Spot rates are equal across countries", "Any deviation in the forward rate from CIP creates a riskless arbitrage profit", "Inflation rates are equal globally", "UIP always holds in practice"],
             "ans": "Any deviation in the forward rate from CIP creates a riskless arbitrage profit", "mod": 3,
             "exp": "CIP: F/S = (1+i_d)/(1+i_f). Any deviation allows borrow-invest-hedge arbitrage with zero risk — traders close deviations immediately."},

            {"q": "EUR/USD spot = 1.0850, US rate = 5%, EU rate = 3%, 180-day forward. F ≈ ?",
             "opts": ["1.0850", "1.0957", "1.0741", "1.1200"],
             "ans": "1.0957", "mod": 4,
             "exp": "F = 1.0850 × (1+0.05×0.5) / (1+0.03×0.5) = 1.0850 × 1.025/1.015 ≈ 1.0957."},

            {"q": "A negative EUR/USD cross-currency basis means:",
             "opts": ["EUR is scarce in the market", "USD is in excess demand — borrowers pay above CIP to access USD", "EUR rates are lower than USD rates", "The spot rate is overvalued"],
             "ans": "USD is in excess demand — borrowers pay above CIP to access USD", "mod": 5,
             "exp": "Negative CCS basis = USD at a premium. Non-US borrowers pay extra above CIP to access USD via swaps. Widens during stress (GFC, COVID)."},

            {"q": "In the Garman-Kohlhagen model, the foreign interest rate (r_f) is treated as:",
             "opts": ["A discount rate for future cash flows", "A continuous dividend yield on the base currency", "An inflation proxy", "A penalty rate for early exercise"],
             "ans": "A continuous dividend yield on the base currency", "mod": 6,
             "exp": "Holding foreign currency earns r_f — analogous to a dividend. GK extends Black-Scholes by treating r_f as a continuous dividend yield."},

            {"q": "A knock-out (KO) barrier option compared to a vanilla option is:",
             "opts": ["More expensive due to the barrier", "Cheaper — but protection disappears if spot hits the barrier", "The same price as vanilla", "Only available for USD/JPY"],
             "ans": "Cheaper — but protection disappears if spot hits the barrier", "mod": 7,
             "exp": "KO options are cheaper — the seller bears less risk since the option can cease to exist. However, protection disappears exactly when spot reaches the barrier."},

            {"q": "The minimum variance hedge ratio h* = ρ × (σ_S/σ_F). If σ_F > σ_S, then h* is:",
             "opts": ["Greater than 1 — over-hedge", "Less than 1 — hedge only a fraction", "Equal to 1 — always hedge 100%", "Negative — take opposite position"],
             "ans": "Less than 1 — hedge only a fraction", "mod": 8,
             "exp": "When σ_F > σ_S (hedge more volatile than exposure), σ_S/σ_F < 1, so h* < 1. Hedging less than 100% minimises variance."},

            {"q": "The carry trade exploits:",
             "opts": ["PPP deviations in goods markets", "CIP arbitrage in forward markets", "UIP violations — high-yield currencies often fail to depreciate as theory predicts", "Central bank intervention patterns"],
             "ans": "UIP violations — high-yield currencies often fail to depreciate as theory predicts", "mod": 9,
             "exp": "Carry trade: borrow low-yield, invest high-yield. Works because UIP fails — HY currencies often appreciate. Dangerous during sudden risk-off events."},

            {"q": "A Golden Cross in technical analysis occurs when:",
             "opts": ["Price crosses above the 61.8% Fibonacci level", "The 50-day MA crosses ABOVE the 200-day MA", "RSI crosses above the 70 overbought level", "MACD crosses above zero"],
             "ans": "The 50-day MA crosses ABOVE the 200-day MA", "mod": 10,
             "exp": "Golden Cross = 50-day MA crosses above 200-day MA. Major long-term bullish signal. Opposite = Death Cross (bearish)."},

            {"q": "When using FX options (not forwards) to hedge M&A deal FX risk, the key advantage is:",
             "opts": ["Options are always cheaper than forwards", "If the deal fails, the option lapses — forwards leave a naked FX position", "Options do not require counterparty credit assessment", "Forwards cannot be used beyond 3-month tenors"],
             "ans": "If the deal fails, the option lapses — forwards leave a naked FX position", "mod": 11,
             "exp": "M&A exposure is contingent. If the deal fails, a forward leaves a dangerous naked FX position. An FX option simply expires, losing only the premium paid."},

            {"q": "CLS Bank eliminates Herstatt risk through:",
             "opts": ["Netting all trades to zero", "Payment-vs-Payment (PvP) — both legs settle simultaneously or neither settles", "Requiring same-day settlement for all FX", "Using only USD as the settlement currency"],
             "ans": "Payment-vs-Payment (PvP) — both legs settle simultaneously or neither settles", "mod": 12,
             "exp": "CLS PvP: both payment legs settle at the same moment. If one party cannot deliver, neither leg settles — principal risk is completely eliminated."},
        ]

        selected_questions = all_quiz_questions[:num_q]

        if "fx_quiz_submitted" not in st.session_state:
            st.session_state.fx_quiz_submitted = {}

        for idx, q in enumerate(selected_questions):
            st.markdown("---")
            st.markdown(f"**Q{idx+1}. [Module {q['mod']}] {q['q']}**")
            answer = st.radio("", q["opts"], key=f"fxmq_{idx}")

            if st.button(f"Check Answer Q{idx+1}", key=f"fxmqc_{idx}"):
                if answer == q["ans"]:
                    st.success(f"✅ Correct! {q['exp']}")
                    st.session_state.fx_quiz_submitted[idx] = True
                else:
                    st.error(f"❌ Incorrect. The correct answer is: **{q['ans']}**")
                    st.info(f"💡 Explanation: {q['exp']}")
                    st.session_state.fx_quiz_submitted[idx] = False

        st.markdown("---")
        answered = len(st.session_state.fx_quiz_submitted)
        correct  = sum(1 for v in st.session_state.fx_quiz_submitted.values() if v)
        if answered > 0:
            pct = correct / answered * 100
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Questions Answered", f"{answered}/{num_q}")
            with col2: st.metric("Correct Answers", f"{correct}")
            with col3: st.metric("Score", f"{pct:.0f}%")

            if pct >= 90:
                st.success("🏆 Outstanding! You have expert-level FX knowledge!")
            elif pct >= 75:
                st.info("✅ Great work! Good understanding across the FX curriculum.")
            elif pct >= 60:
                st.warning("⚠️ Good progress! Review the modules where you made mistakes.")
            else:
                st.error("❌ Keep studying! Focus on the modules you found challenging.")

        if st.button("🔄 Reset Quiz"):
            st.session_state.fx_quiz_submitted = {}
            st.rerun()

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("🎓 Study Planner & Progress Tracker")

        st.subheader("📅 Suggested Study Schedule")

        schedule_df = pd.DataFrame({
            "Week": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11"],
            "Modules": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10–11", "12 + Review"],
            "Topics": [
                "FX market structure, spot quotes, bid-ask, pips, cross rates",
                "Trading sessions, T+2 settlement, SWIFT, nostro/vostro, CLS",
                "PPP, CIP, UIP, Fisher Effect, IFE — parity framework",
                "Forward rate formula, CIA, forward points, NDFs, corporate hedging",
                "FX swap mechanics, CCBS, CIP basis, treasury applications",
                "Garman-Kohlhagen model, Greeks (Delta/Gamma/Vega/Theta), put-call parity",
                "Barrier options, digitals, Asian options, volatility surface",
                "FX exposures (transaction/translation/economic), VaR, h*, IFRS 9",
                "Carry trade, Taylor Rule, risk-on/off, BEER/FEER, FX reserves",
                "Technical analysis (RSI, MACD, Fibonacci, BB) + FX capital markets (DCF, M&A, overlay)",
                "Regulation (FX Code, CLS, MiFID II, Dodd-Frank, CBDC) + full review"
            ],
            "Focus Activity": [
                "Quote practice + spread and pip value calculations",
                "Settlement date calculator + nostro balance management",
                "PPP, CIP, carry trade formula drills",
                "Forward rate pricing from scratch + CIA arbitrage detection",
                "FX swap pricing + CCBS all-in cost comparison",
                "Price GK options by hand + interpret Greeks for each input change",
                "Barrier payoff diagrams + vol smile reading",
                "VaR calculations + h* + IFRS 9 effectiveness tests",
                "Taylor Rule analysis + carry scenarios + reserves adequacy",
                "Chart reading + FX-adjusted DCF + M&A hedge comparison",
                "VWAP execution + regulatory quiz + full exam practice"
            ]
        })
        st.dataframe(schedule_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("✅ My Progress Tracker")
        st.markdown("Track your completion of each module:")

        total_completed = 0
        for mod in modules_info:
            col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
            with col1:
                st.markdown(f"**{mod['icon']} Module {mod['num']}: {mod['title']}**")
            with col2:
                completed = st.checkbox("Completed ✅", key=f"fx_prog_done_{mod['num']}")
            with col3:
                practiced = st.checkbox("Practised 🧮", key=f"fx_prog_prac_{mod['num']}")
            with col4:
                confidence = st.select_slider(
                    "Confidence", ["❓", "😰", "😐", "😊", "🌟"],
                    value="😐", key=f"fx_prog_conf_{mod['num']}"
                )
            if completed:
                total_completed += 1

        overall_progress = total_completed / 12 * 100
        st.progress(overall_progress / 100)
        st.metric("Overall Progress", f"{total_completed}/12 modules ({overall_progress:.0f}%)")

        if total_completed == 12:
            st.success("🎉 🏆 Congratulations! You have completed all 12 modules of the Foreign Exchange curriculum! You are ready to apply FX expertise professionally.")
            st.balloons()

        st.markdown("---")
        st.subheader("📌 Quick Reference — Top 12 Rules to Remember")

        rules = [
            ("1",  "The forward rate is NOT a forecast",
             "F = S × (1+i_d)/(1+i_f) — it is the CIP arbitrage-free price, nothing more",
             "M3, M4"),
            ("2",  "CIP is arbitrage-enforced; UIP is not",
             "CIP deviations = riskless profit (CIA). UIP fails = carry trade exists",
             "M3, M4"),
            ("3",  "You buy at the ASK, sell at the BID",
             "The spread is ALWAYS against the client — this is true for every instrument",
             "M1"),
            ("4",  "Settle T+2 — skip BOTH countries' holidays",
             "USD/CAD and USD/TRY are T+1 exceptions. Skip weekends in both currency countries",
             "M2"),
            ("5",  "GK: r_d = quote currency, r_f = base currency",
             "The most common GK exam error — r_f is the BASE (e.g. EUR in EUR/USD), not the domestic",
             "M6"),
            ("6",  "h* = rho × (sigma_S / sigma_F) — not always 1.0",
             "Over-hedging AND under-hedging both increase total variance vs h*",
             "M8"),
            ("7",  "Use OPTIONS for contingent M&A exposure, not forwards",
             "If the deal fails, a forward creates a naked FX position. An option simply lapses",
             "M11"),
            ("8",  "Hedged foreign bond ≈ domestic rate (by CIP)",
             "Foreign yield + (r_d − r_f) = domestic rate. Credit spread above sovereign IS the value-add",
             "M11"),
            ("9",  "Carry trade can lose a year of carry in hours",
             "Size positions with strict stops. Risk-off events (VIX > 35) = exit carry positions immediately",
             "M9"),
            ("10", "IFRS 9 effectiveness must be 80%–125%",
             "Outside this band = hedge accounting disqualified → full P&L volatility on the derivative",
             "M8"),
            ("11", "61.8% Fibonacci = the Golden Ratio — most important S&R level",
             "A bounce from 61.8% confirms trend intact. Break of 78.6% = trend reversal likely",
             "M10"),
            ("12", "FX Global Code is voluntary — but non-compliance costs market access",
             "Sign the Statement of Commitment AND implement governance. Reputation IS enforcement",
             "M12"),
        ]

        rules_df = pd.DataFrame(rules, columns=["#", "Rule", "Why It Matters", "Module(s)"])
        st.dataframe(rules_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔗 Module Connections — How Everything Links Together")
        st.markdown("""
        Understanding how modules connect deepens your mastery:

        | Connection | Link |
        |-----------|------|
        | **M1 → M4** | Spot rate is the foundation for every forward, swap, and option calculation |
        | **M3 → M4** | CIP theory from M3 IS the forward rate formula used in M4 |
        | **M4 → M5** | FX swap far leg pricing = CIP forward rate from M4 |
        | **M3 + M4 → M6** | IRP and forward pricing underpin the GK option model inputs |
        | **M6 → M7** | Vanilla GK formula from M6 is extended to price digital and barrier options in M7 |
        | **M6 + M7 → M8** | Greeks and option structures feed directly into the hedging strategies in M8 |
        | **M3 + M8 → M9** | Parity theory + risk management framework → macro driver analysis |
        | **M4 + M5 → M11** | Forwards and CCBS are the primary instruments for FX-adjusted DCF and M&A hedging |
        | **M8 → M11** | IFRS 9 from M8 applies directly to M&A hedge accounting in M11 |
        | **M2 → M12** | Settlement mechanics from M2 (CLS, Herstatt) are the foundation of M12 regulation |
        | **M10 → M9** | Technical signals complement macro analysis for entry/exit timing |
        | **M11 + M12** | Capital markets application + regulatory compliance = professional FX practitioner |
        """)

        st.success("🎓 Use this overview page as your constant companion throughout the course. Return to it for quick reference, formula lookup, progress tracking, and exam preparation!")

if __name__ == "__main__":
    show()