import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🌍 Module 9: Macro Drivers of Exchange Rates")
    st.markdown("*Master carry trade, central bank policy, Taylor Rule, risk-on/off dynamics, BEER/FEER, and FX reserves analysis*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Interest Rate Differentials & Carry Trade")
        st.markdown("""
        **Interest rate differentials** are among the most powerful short-to-medium term FX drivers.

        ```
        Carry Trade Mechanics:
        1. Borrow in low-yield currency (e.g. JPY at 0.1%)
        2. Convert to high-yield currency (e.g. AUD at 4.35%)
        3. Invest at higher rate
        4. Gross carry = i_high - i_low = 4.35% - 0.1% = 4.25% p.a.
        5. Net carry = gross carry - actual spot depreciation of HY currency
        ```

        | Carry Trade Driver | Effect on FX |
        |-------------------|-------------|
        | Rising rate differential | HY currency tends to APPRECIATE (capital inflows) |
        | Falling rate differential | HY currency tends to DEPRECIATE (capital outflows) |
        | Risk-off event (VIX spike) | Sudden carry UNWIND — HY currencies crash, JPY/CHF spike |

        **The paradox:** UIP says carry should = 0. But empirically, HY currencies often appreciate
        rather than depreciate — the famous "forward premium puzzle."
        """)

        st.subheader("2. Central Bank Policy & FX Transmission")
        st.markdown("""
        Central bank decisions are the single most important short-term FX driver.

        #### How Rate Decisions Transmit to FX:
        ```
        Rate HIKE → Higher yields → Capital inflows → Currency APPRECIATES
        Rate CUT  → Lower yields → Capital outflows → Currency DEPRECIATES

        BUT: Expectations matter more than actual decisions!
        "Buy the rumour, sell the fact" — FX often peaks on the actual hike
        if the market had already priced it in fully.
        ```

        #### Central Bank Communication Channels:
        | Channel | FX Impact |
        |---------|----------|
        | Surprise rate hike | Immediate sharp appreciation |
        | Hawkish forward guidance | Gradual appreciation |
        | Dovish pivot (unexpected) | Sharp depreciation |
        | QE expansion | Currency depreciation (money supply up) |
        | FX intervention (buy domestic) | Direct short-term appreciation |
        """)

        st.subheader("3. Taylor Rule")
        st.markdown("""
        The **Taylor Rule** estimates the appropriate policy rate based on macroeconomic fundamentals.
        Used by FX analysts to assess whether a central bank will hike or cut, and thus forecast currency direction.

        ```
        Taylor Rule:
        i = r* + pi + alpha x (pi - pi*) + beta x (y - y*)

        Where:
          i    = recommended nominal policy rate
          r*   = neutral real interest rate (typically ~1%)
          pi   = current inflation rate
          pi*  = inflation target (typically 2%)
          y-y* = output gap (actual GDP vs potential GDP)
          alpha, beta = policy weights (typically 0.5 each)
        ```

        **Using Taylor Rule for FX:**
        If Taylor Rule rate > Actual rate: Central bank is BEHIND THE CURVE → expect hikes → bullish currency
        If Taylor Rule rate < Actual rate: Central bank is AHEAD OF THE CURVE → expect cuts → bearish currency
        """)

        st.subheader("4. Risk-On / Risk-Off Dynamics")
        st.markdown("""
        Global risk sentiment is a major FX driver, particularly for EM and commodity currencies.

        | Environment | Indicator | Safe Havens (BUY) | Risk Currencies (SELL) |
        |------------|-----------|------------------|----------------------|
        | **Risk-ON** | VIX < 20, equities rising | — | AUD, NZD, EM, CAD |
        | **Risk-OFF** | VIX > 25, equities falling | JPY, CHF, USD | AUD, NZD, EM, ZAR |

        **Key risk-on/off indicators:**
        - VIX index (equity fear gauge)
        - Credit spreads (high-yield bond spreads)
        - S&P 500 direction
        - Oil price (commodity currency proxy)
        - EM capital flows data

        **Correlation rule of thumb:**
        AUD/USD and S&P 500 correlation ≈ +0.65 (risk-on currency)
        USD/JPY and S&P 500 correlation ≈ -0.40 (JPY = safe haven)
        """)

        st.subheader("5. BEER & FEER Models")
        st.markdown("""
        Medium-term FX valuation models used by central banks, IMF, and macro analysts:

        | Model | Full Name | Methodology |
        |-------|-----------|-------------|
        | **BEER** | Behavioural Equilibrium Exchange Rate | Regression of real FX rate on macro fundamentals (ToT, NFA, productivity, fiscal) |
        | **FEER** | Fundamental Equilibrium Exchange Rate | Rate consistent with both internal balance (full employment) and external balance (sustainable current account) |

        **BEER inputs typically include:**
        - Terms of Trade (export/import price ratio)
        - Net Foreign Assets (NFA) as % of GDP
        - Productivity differentials (Balassa-Samuelson)
        - Government fiscal position
        - Commodity prices (for commodity exporters)

        These models give **medium-term fair value** — currencies can deviate from BEER/FEER for years
        but tend to revert over 3-5 year horizons.
        """)

        st.subheader("6. FX Reserves & Currency Crisis Framework")
        st.markdown("""
        **FX Reserves** provide the firepower for central banks to defend their currency.

        #### Adequacy Metrics:
        ```
        1. Import Cover:     Reserves / Monthly Imports (target: > 3 months)
        2. Debt Coverage:    Reserves / Short-term External Debt (target: > 100%)
        3. M2 Coverage:      Reserves / Broad Money Supply (target: > 20%)
        4. Composite (IMF):  Weighted blend of all above (ARA metric)
        ```

        #### Speculative Attack Vulnerability Indicators:
        ```
        High Risk:  < 3 months import cover + current account deficit + overvalued REER
        Moderate:   3-6 months import cover + moderate deficit
        Low Risk:   > 6 months import cover + current account surplus
        ```
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Carry Trade Return Analysis")
        st.markdown("""
        **Classic AUD/JPY carry trade:**

        | Metric | Value |
        |--------|-------|
        | RBA Cash Rate (AUD) | 4.35% |
        | BoJ Policy Rate (JPY) | 0.10% |
        | Gross Carry | 4.25% p.a. |
        | Funding cost (bid-ask, etc.) | ~0.25% |
        | Net Carry | ~4.00% p.a. |

        **Scenario Analysis:**
        ```
        Scenario A: AUD/JPY unchanged over 12 months
          Return = +4.00% carry (no FX impact)

        Scenario B: AUD/JPY rises 5% (AUD strengthens — contra UIP)
          Return = +4.00% carry + 5.00% FX gain = +9.00%!

        Scenario C: AUD/JPY falls 3% (UIP partially holds)
          Return = +4.00% carry - 3.00% FX loss = +1.00% (still positive!)

        Scenario D: Risk-off shock — AUD/JPY falls 15% (2008-style)
          Return = +4.00% carry - 15.00% FX loss = -11.00% ← Carry unwind!
        ```
        The carry trade Sharpe ratio is positive in calm markets but experiences extreme
        negative skewness during risk-off events — "picking up pennies in front of a steamroller."
        """)

        st.subheader("Example 2: Taylor Rule Analysis — Federal Reserve")
        st.markdown("""
        **US Taylor Rule Calculation (2024):**

        ```
        Inputs:
          r* (neutral real rate)  = 0.5%  (post-GFC estimate)
          pi (current CPI)        = 3.5%
          pi* (inflation target)  = 2.0%
          y-y* (output gap)       = +0.5% (economy above potential)
          alpha = beta            = 0.5

        Taylor Rate:
        i = r* + pi + alpha(pi - pi*) + beta(y-y*)
          = 0.5% + 3.5% + 0.5(3.5% - 2.0%) + 0.5(0.5%)
          = 0.5% + 3.5% + 0.75% + 0.25%
          = 5.00%

        Actual Fed Funds Rate: 5.25%

        Interpretation: Fed is SLIGHTLY above Taylor rate (by 25 bps)
        → Fed may be close to peak; potential cuts signal
        → Slightly bearish USD at the margin
        ```
        """)

        st.subheader("Example 3: Risk-Off Event — COVID-19 March 2020")
        fx_covid = pd.DataFrame({
            "Currency Pair": ["AUD/USD", "NZD/USD", "USD/JPY", "USD/CHF", "USD/ZAR", "USD/BRL"],
            "Move (2 weeks)": ["-14.5%", "-13.2%", "-7.8% (JPY↑)", "-3.5% (CHF↑)", "+25.0% (ZAR↓)", "+30.0% (BRL↓)"],
            "Classification": ["Risk-off SELL", "Risk-off SELL", "Safe Haven BUY", "Safe Haven BUY", "EM SELL", "EM SELL"],
            "Carry Position": ["Long (4.35% carry)", "Long (3.50% carry)", "Short (funded)", "Short (funded)", "Long (7.0% carry)", "Long (4.5% carry)"]
        })
        st.dataframe(fx_covid, use_container_width=True, hide_index=True)
        st.markdown("""
        **Key observations:**
        - Safe haven currencies (JPY, CHF) appreciated sharply despite near-zero yields
        - Carry trade currencies (AUD, NZD, EM) fell dramatically — years of carry wiped out in days
        - The speed of the move prevented orderly unwinding — massive losses for carry traders
        - EUR/USD CCS basis hit -120 bps — acute dollar funding shortage
        """)

        st.subheader("Example 4: BEER Valuation — Case Study")
        beer_df = pd.DataFrame({
            "Currency": ["AUD/USD", "EUR/USD", "GBP/USD", "USD/JPY", "USD/BRL"],
            "Actual Rate": ["0.6450", "1.0850", "1.2700", "149.50", "4.97"],
            "BEER Fair Value": ["0.6800", "1.0500", "1.3200", "135.00", "5.20"],
            "Over/Undervalued": ["-5.1% (undervalued)", "+3.3% (overvalued)", "-3.8% (undervalued)", "+10.7% (JPY undervalued)", "-4.4% (BRL undervalued)"],
            "Key Driver": ["Commodities/China exposure", "Rate differential (USD higher)", "Brexit uncertainty premium", "BoJ yield curve control", "Political risk premium"]
        })
        st.dataframe(beer_df, use_container_width=True, hide_index=True)
        st.markdown("""
        **Important caveat:** BEER/FEER deviations can persist for 2-5 years.
        Being right on valuation but wrong on timing destroys more capital than being wrong on both.
        """)

        st.subheader("Example 5: FX Reserves Adequacy — Emerging Market")
        st.markdown("""
        **Country X FX Reserves Assessment:**

        ```
        FX Reserves:                 USD 42 billion
        Monthly Imports:             USD 7.5 billion
        Short-term External Debt:    USD 35 billion
        Broad Money (M2):            USD 180 billion

        Adequacy Metrics:
        Import Cover:     42 / 7.5   = 5.6 months  ✅ (target: >3 months)
        Debt Coverage:    42 / 35    = 120%         ✅ (target: >100%)
        M2 Coverage:      42 / 180   = 23.3%        ✅ (target: >20%)

        Current Account Balance:  -2.5% of GDP     ⚠️ (moderate deficit)
        REER:                     8% above BEER     ⚠️ (slightly overvalued)

        Overall Assessment: ADEQUATE but monitor current account.
        If CA deficit widens to >4% GDP, reserve drawdown risk increases.
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Calculator:", [
            "💹 Carry Trade Return Calculator",
            "📐 Taylor Rule Policy Rate Calculator",
            "🌡️ Risk-On/Off Scenario Analyser",
            "📊 BEER Valuation Calculator",
            "🏦 FX Reserves Adequacy Checker"
        ])

        st.markdown("---")

        if calc_choice == "💹 Carry Trade Return Calculator":
            st.subheader("Carry Trade Return & Risk Calculator")
            col1, col2 = st.columns(2)
            with col1:
                i_high     = st.number_input("High-yield currency rate % (invest)", value=4.35, step=0.05)
                i_low      = st.number_input("Funding currency rate % (borrow)",   value=0.10, step=0.05)
                fund_cost  = st.number_input("Transaction & funding costs % p.a.", value=0.25, step=0.05)
            with col2:
                invest_amt = st.number_input("Investment Amount", value=1000000.0, step=100000.0)
                horizon    = st.slider("Investment Horizon (months)", 1, 24, 12)
            st.markdown("**Spot Scenarios (% change over horizon, + = HY depreciates):**")
            scenarios_input = {
                "Bull (HY appreciates 5%)": -5.0,
                "Base (No change)": 0.0,
                "Mild carry unwind (-5%)": 5.0,
                "Severe carry unwind (-15%)": 15.0,
                "GFC-style crash (-25%)": 25.0
            }

            if st.button("🧮 Analyse Carry Trade", type="primary"):
                gross_carry = i_high - i_low
                net_carry   = gross_carry - fund_cost
                period_carry = net_carry * horizon / 12
                results = []
                for scen, fx_move in scenarios_input.items():
                    total_return = period_carry - fx_move
                    dollar_pnl   = invest_amt * total_return / 100
                    results.append({"Scenario": scen, "Carry %": f"{period_carry:.2f}%",
                                    "FX Move %": f"{-fx_move:+.1f}%", "Total Return %": f"{total_return:+.2f}%",
                                    "Dollar P&L": f"${dollar_pnl:+,.0f}",
                                    "Result": "✅ Profit" if dollar_pnl > 0 else "❌ Loss"})
                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)
                c1, c2, c3 = st.columns(3)
                c1.metric("Gross Carry", f"{gross_carry:.2f}% p.a.")
                c2.metric("Net Carry", f"{net_carry:.2f}% p.a.")
                c3.metric(f"{horizon}M Period Carry", f"{period_carry:.2f}%")
                break_even = period_carry
                st.info(f"📊 Break-even spot move: {break_even:.2f}% depreciation of HY currency wipes out all carry over {horizon} months.")
                fx_range = np.linspace(-20, 30, 100)
                returns_v = [period_carry - f for f in fx_range]
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=fx_range, y=returns_v, mode="lines",
                    line=dict(color="#2E86C1", width=2.5)))
                fig.add_hline(y=0, line_color="red", line_dash="dash", annotation_text="Break-even")
                fig.update_layout(title=f"Carry Trade Return vs HY Currency Move ({horizon}M)",
                                  xaxis_title="HY Currency Depreciation %", yaxis_title="Total Return %")
                st.plotly_chart(fig, use_container_width=True)

        elif calc_choice == "📐 Taylor Rule Policy Rate Calculator":
            st.subheader("Taylor Rule Policy Rate Calculator")
            col1, col2 = st.columns(2)
            with col1:
                r_star   = st.number_input("Neutral Real Rate r* %", value=0.5, step=0.1)
                pi_curr  = st.number_input("Current Inflation % (pi)", value=3.5, step=0.1)
                pi_star  = st.number_input("Inflation Target % (pi*)", value=2.0, step=0.1)
            with col2:
                output_gap = st.number_input("Output Gap % (y - y*, +ve = above potential)", value=0.5, step=0.1)
                alpha      = st.number_input("Inflation Weight (alpha)", value=0.5, step=0.1)
                beta       = st.number_input("Output Gap Weight (beta)", value=0.5, step=0.1)
                actual_rate = st.number_input("Actual Policy Rate %", value=5.25, step=0.05)
                country = st.text_input("Country / Central Bank", value="USA / Federal Reserve")

            if st.button("🧮 Calculate Taylor Rate", type="primary"):
                taylor_rate = r_star + pi_curr + alpha*(pi_curr - pi_star) + beta*output_gap
                deviation   = actual_rate - taylor_rate
                st.markdown("---")
                st.markdown(f"""
                **Taylor Rule Calculation — {country}:**
                ```
                i = r* + pi + alpha × (pi - pi*) + beta × (y - y*)
                  = {r_star:.1f}% + {pi_curr:.1f}% + {alpha:.1f}×({pi_curr:.1f}% - {pi_star:.1f}%) + {beta:.1f}×({output_gap:.1f}%)
                  = {r_star:.1f}% + {pi_curr:.1f}% + {alpha*(pi_curr-pi_star):.2f}% + {beta*output_gap:.2f}%
                  = {taylor_rate:.2f}%

                Actual Policy Rate:   {actual_rate:.2f}%
                Taylor Rate:          {taylor_rate:.2f}%
                Deviation:            {deviation:+.2f}% (actual vs Taylor)
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("Taylor Rule Rate", f"{taylor_rate:.2f}%")
                c2.metric("Actual Rate", f"{actual_rate:.2f}%")
                c3.metric("Deviation", f"{deviation:+.2f}%")
                if deviation > 0.5:
                    st.warning(f"⚠️ Actual rate is {deviation:.2f}% ABOVE Taylor rate → Central bank ahead of curve → potential CUTS ahead → slightly bearish for {country.split('/')[0].strip()} currency.")
                elif deviation < -0.5:
                    st.warning(f"⚠️ Actual rate is {abs(deviation):.2f}% BELOW Taylor rate → Central bank behind curve → potential HIKES ahead → slightly bullish for {country.split('/')[0].strip()} currency.")
                else:
                    st.success(f"✅ Policy rate approximately consistent with Taylor Rule ({deviation:+.2f}% deviation). No strong directional signal.")
                components = ["r* (Neutral)", "pi (Inflation)", "Inflation Gap", "Output Gap", "Taylor Total"]
                values_c   = [r_star, pi_curr, alpha*(pi_curr-pi_star), beta*output_gap, taylor_rate]
                fig = go.Figure(go.Waterfall(orientation="v", measure=["relative","relative","relative","relative","total"],
                    x=components, y=values_c,
                    connector={"line": {"color": "rgb(63,63,63)"}},
                    increasing={"marker": {"color": "#27AE60"}},
                    decreasing={"marker": {"color": "#E74C3C"}},
                    totals={"marker": {"color": "#2E86C1"}}))
                fig.add_hline(y=actual_rate, line_dash="dash", line_color="orange",
                             annotation_text=f"Actual Rate {actual_rate:.2f}%")
                fig.update_layout(title=f"Taylor Rule Components — {country}", yaxis_title="Rate %")
                st.plotly_chart(fig, use_container_width=True)

        elif calc_choice == "🌡️ Risk-On/Off Scenario Analyser":
            st.subheader("Risk-On / Risk-Off Scenario Impact Analyser")
            col1, col2 = st.columns(2)
            with col1:
                vix_level  = st.slider("VIX Level", 10, 80, 18)
                scenario_type = st.selectbox("Market Event", [
                    "Central bank surprise hike",
                    "Geopolitical shock / war escalation",
                    "US recession announcement",
                    "Strong US jobs report",
                    "EM debt crisis",
                    "Global equity meltdown (-10% in a week)"
                ])
            with col2:
                aud_pos = st.number_input("AUD/USD position (+ = long, - = short)", value=1000000.0, step=100000.0)
                jpy_pos = st.number_input("USD/JPY position (+ = long USD, - = short USD)", value=-500000.0, step=100000.0)
                em_pos  = st.number_input("EM currency position", value=500000.0, step=100000.0)

            if st.button("🌡️ Run Risk Scenario", type="primary"):
                impact_map = {
                    "Central bank surprise hike":   {"AUD/USD": +2.0, "USD/JPY": +1.5, "EM": +1.0, "risk": "ON"},
                    "Geopolitical shock / war escalation": {"AUD/USD": -4.0, "USD/JPY": -5.0, "EM": -6.0, "risk": "OFF"},
                    "US recession announcement":    {"AUD/USD": -6.0, "USD/JPY": -8.0, "EM": -10.0, "risk": "OFF"},
                    "Strong US jobs report":         {"AUD/USD": +1.5, "USD/JPY": +2.0, "EM": +0.5, "risk": "ON"},
                    "EM debt crisis":                {"AUD/USD": -5.0, "USD/JPY": -6.0, "EM": -15.0, "risk": "OFF"},
                    "Global equity meltdown (-10% in a week)": {"AUD/USD": -8.0, "USD/JPY": -10.0, "EM": -12.0, "risk": "OFF"}
                }
                impacts = impact_map[scenario_type]
                aud_pnl = aud_pos * impacts["AUD/USD"] / 100
                jpy_pnl = jpy_pos * impacts["USD/JPY"] / 100
                em_pnl  = em_pos  * impacts["EM"] / 100
                total_pnl = aud_pnl + jpy_pnl + em_pnl
                risk_env = impacts["risk"]

                st.markdown("---")
                results = pd.DataFrame({
                    "Position": ["AUD/USD", "USD/JPY", "EM Currency"],
                    "Exposure": [f"{aud_pos:+,.0f}", f"{jpy_pos:+,.0f}", f"{em_pos:+,.0f}"],
                    "Estimated Move": [f"{impacts['AUD/USD']:+.1f}%", f"{impacts['USD/JPY']:+.1f}%", f"{impacts['EM']:+.1f}%"],
                    "P&L Impact": [f"{aud_pnl:+,.0f}", f"{jpy_pnl:+,.0f}", f"{em_pnl:+,.0f}"]
                })
                st.dataframe(results, use_container_width=True, hide_index=True)
                c1, c2, c3 = st.columns(3)
                c1.metric("Risk Environment", f"{'🟢 Risk-ON' if risk_env == 'ON' else '🔴 Risk-OFF'}")
                c2.metric("VIX Level", f"{vix_level}", "Elevated" if vix_level > 25 else "Normal")
                c3.metric("Total P&L Impact", f"{total_pnl:+,.0f}", delta_color="normal" if total_pnl >= 0 else "inverse")
                if total_pnl < 0 and risk_env == "OFF":
                    st.error(f"🚨 Risk-OFF event causes {abs(total_pnl):,.0f} loss. Consider adding JPY/CHF longs as portfolio hedges.")
                elif total_pnl > 0:
                    st.success(f"✅ Portfolio gains {total_pnl:,.0f} under this scenario.")

        elif calc_choice == "📊 BEER Valuation Calculator":
            st.subheader("BEER Exchange Rate Valuation Tool")
            st.info("Input macro variables to estimate BEER fair value and currency misalignment.")
            col1, col2 = st.columns(2)
            with col1:
                actual_rate_b = st.number_input("Actual Exchange Rate", value=0.6450, format="%.4f")
                terms_of_trade = st.number_input("Terms of Trade Index (100 = neutral)", value=105.0, step=1.0)
                nfa_gdp = st.number_input("Net Foreign Assets (% of GDP)", value=-50.0, step=1.0)
            with col2:
                productivity = st.number_input("Productivity Differential vs trading partners (% diff)", value=0.5, step=0.1)
                commodity_idx = st.number_input("Commodity Price Index (100 = neutral)", value=110.0, step=1.0)
                govt_balance = st.number_input("Government Balance (% of GDP, + = surplus)", value=-3.0, step=0.5)

            if st.button("🧮 Estimate BEER Fair Value", type="primary"):
                beer_adj  = (terms_of_trade - 100) * 0.003
                beer_adj += nfa_gdp * 0.002
                beer_adj += productivity * 0.005
                beer_adj += (commodity_idx - 100) * 0.002
                beer_adj += govt_balance * 0.001
                beer_value = actual_rate_b * (1 + beer_adj)
                misalignment = (actual_rate_b - beer_value) / beer_value * 100

                st.markdown("---")
                st.markdown(f"""
                **BEER Valuation:**
                ```
                Actual Rate:        {actual_rate_b:.4f}
                BEER Adjustment:    {beer_adj*100:+.2f}%
                BEER Fair Value:    {beer_value:.4f}
                Misalignment:       {misalignment:+.2f}%
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("Actual Rate", f"{actual_rate_b:.4f}")
                c2.metric("BEER Fair Value", f"{beer_value:.4f}")
                c3.metric("Misalignment", f"{misalignment:+.2f}%")
                if misalignment > 5:
                    st.warning(f"⚠️ Currency OVERVALUED by {misalignment:.1f}% vs BEER. Long-run depreciation pressure.")
                elif misalignment < -5:
                    st.info(f"📈 Currency UNDERVALUED by {abs(misalignment):.1f}% vs BEER. Long-run appreciation potential.")
                else:
                    st.success(f"✅ Currency approximately fairly valued vs BEER ({misalignment:+.1f}%).")

        elif calc_choice == "🏦 FX Reserves Adequacy Checker":
            st.subheader("FX Reserves Adequacy Assessment")
            col1, col2 = st.columns(2)
            with col1:
                reserves = st.number_input("FX Reserves (USD billions)", value=42.0, step=1.0)
                monthly_imports = st.number_input("Monthly Imports (USD billions)", value=7.5, step=0.5)
                st_debt = st.number_input("Short-term External Debt (USD billions)", value=35.0, step=1.0)
            with col2:
                m2 = st.number_input("Broad Money M2 (USD billions equivalent)", value=180.0, step=5.0)
                ca_balance = st.number_input("Current Account Balance (% of GDP)", value=-2.5, step=0.1)
                country_name = st.text_input("Country Name", value="Country X")

            if st.button("🏦 Assess FX Reserves Adequacy", type="primary"):
                import_cover = reserves / monthly_imports
                debt_cover   = reserves / st_debt * 100 if st_debt > 0 else 0
                m2_cover     = reserves / m2 * 100 if m2 > 0 else 0

                metrics = pd.DataFrame({
                    "Metric": ["Import Cover", "Short-term Debt Coverage", "M2 Coverage", "Current Account Balance"],
                    "Value": [f"{import_cover:.1f} months", f"{debt_cover:.0f}%", f"{m2_cover:.1f}%", f"{ca_balance:.1f}% of GDP"],
                    "Target": [">3 months", ">100%", ">20%", "Manageable (<4%)"],
                    "Status": [
                        "✅ Adequate" if import_cover > 3 else ("⚠️ Borderline" if import_cover > 2 else "❌ Insufficient"),
                        "✅ Adequate" if debt_cover > 100 else ("⚠️ Borderline" if debt_cover > 75 else "❌ Insufficient"),
                        "✅ Adequate" if m2_cover > 20 else ("⚠️ Borderline" if m2_cover > 10 else "❌ Insufficient"),
                        "✅ Surplus" if ca_balance > 0 else ("✅ Manageable" if ca_balance > -3 else ("⚠️ Elevated" if ca_balance > -5 else "❌ High Risk"))
                    ]
                })
                st.dataframe(metrics, use_container_width=True, hide_index=True)
                pass_count = sum(1 for _, row in metrics.iterrows() if "✅" in row["Status"])
                st.metric(f"{country_name} — Overall Reserves Assessment",
                          "Adequate" if pass_count >= 3 else "Borderline" if pass_count >= 2 else "Vulnerable")
                fig = go.Figure(go.Bar(
                    x=["Import Cover\n(target=3)", "Debt Coverage\n(target=100%)", "M2 Coverage\n(target=20%)"],
                    y=[import_cover/3*100, debt_cover, m2_cover],
                    marker_color=["#27AE60" if x > 100 else "#E74C3C" for x in [import_cover/3*100, debt_cover, m2_cover]],
                    text=[f"{import_cover:.1f} months", f"{debt_cover:.0f}%", f"{m2_cover:.1f}%"],
                    textposition="outside"
                ))
                fig.add_hline(y=100, line_dash="dash", annotation_text="Target Level")
                fig.update_layout(title=f"{country_name} — FX Reserves Adequacy vs Targets",
                                  yaxis_title="% of Target Met")
                st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.header("Visualizations")

        st.subheader("US Policy Rate vs EUR/USD (2015-2024)")
        years = list(range(2015, 2025))
        us_rates = [0.25, 0.50, 1.25, 2.25, 2.50, 0.25, 0.25, 0.75, 4.50, 5.25]
        eu_rates = [0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 3.50, 4.00]
        eurusd   = [1.09, 1.05, 1.05, 1.20, 1.14, 1.18, 1.22, 1.07, 1.07, 1.09]
        differentials = [u - e for u, e in zip(us_rates, eu_rates)]
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=years, y=differentials, name="Rate Differential (US-EU)",
            marker_color=["#27AE60" if d > 0 else "#E74C3C" for d in differentials], opacity=0.6, yaxis="y"))
        fig1.add_trace(go.Scatter(x=years, y=eurusd, name="EUR/USD",
            line=dict(color="#2E86C1", width=2.5), yaxis="y2"))
        fig1.update_layout(title="US-EU Rate Differential vs EUR/USD",
            yaxis=dict(title="Rate Differential (pp)"),
            yaxis2=dict(title="EUR/USD", overlaying="y", side="right"),
            legend=dict(x=0.01, y=0.99))
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Carry Trade Return Distribution — AUD/JPY")
        np.random.seed(42)
        normal_returns = np.random.normal(4.5, 6, 500)
        crash_returns  = np.random.normal(-18, 5, 50)
        all_returns    = np.concatenate([normal_returns, crash_returns])
        fig2 = go.Figure()
        fig2.add_trace(go.Histogram(x=all_returns, nbinsx=50, name="Annual Returns",
            marker_color="#2E86C1", opacity=0.75))
        fig2.add_vline(x=np.mean(all_returns), line_dash="dash", line_color="orange",
                      annotation_text=f"Mean={np.mean(all_returns):.1f}%")
        fig2.add_vline(x=np.percentile(all_returns, 5), line_dash="dot", line_color="#E74C3C",
                      annotation_text=f"5th pct={np.percentile(all_returns, 5):.1f}%")
        fig2.update_layout(title="Carry Trade Return Distribution — Left Tail (Crash) Risk",
                           xaxis_title="Annual Return %", yaxis_title="Frequency")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Risk-On vs Risk-Off Currency Performance")
        currencies = ["AUD/USD", "NZD/USD", "USD/JPY", "USD/CHF", "USD/ZAR", "EUR/USD"]
        risk_on    = [3.5, 3.0, 2.5, 1.5, 4.0, 1.5]
        risk_off   = [-8.0, -7.5, -9.0, -4.0, -15.0, -3.0]
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(name="Risk-ON (typical)", x=currencies, y=risk_on, marker_color="#27AE60"))
        fig3.add_trace(go.Bar(name="Risk-OFF (stress)", x=currencies, y=risk_off, marker_color="#E74C3C"))
        fig3.add_hline(y=0, line_color="black")
        fig3.update_layout(title="Typical FX Response to Risk-On vs Risk-Off Events (%)",
                           barmode="group", xaxis_title="Currency Pair", yaxis_title="Typical Move %")
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — Macro Drivers")

        st.markdown("**Q1. The carry trade borrows in low-yield currencies and invests in high-yield currencies. Its main risk is:**")
        q1 = st.radio("", [
            "The interest rate differential disappears gradually",
            "Sudden risk-off events causing violent carry unwinds that wipe out months of carry in days",
            "Central bank intervention targeting the funding currency",
            "Inflation eroding the real return"
        ], key="fx9q1")
        if st.button("Check Q1", key="fx9c1"):
            if "sudden risk-off" in q1.lower() or "violent carry unwinds" in q1.lower():
                st.success("✅ Correct! The carry trade has positive average returns but extreme negative skewness — sudden risk-off events can wipe out years of carry quickly.")
            else:
                st.error("❌ Incorrect. The main carry trade risk is sudden risk-off events (VIX spikes, crises) causing violent unwinds where HY currencies crash rapidly.")
        st.markdown("---")

        st.markdown("**Q2. If the Taylor Rule implies a rate of 5.5% but the central bank holds at 4.0%, FX analysts would expect:**")
        q2 = st.radio("", [
            "The currency to depreciate immediately",
            "The central bank is behind the curve — likely future hikes — bullish for the currency",
            "The central bank is ahead of the curve — likely future cuts — bearish for the currency",
            "No FX impact — Taylor Rule is only for academic use"
        ], key="fx9q2")
        if st.button("Check Q2", key="fx9c2"):
            if "behind the curve" in q2 and "bullish" in q2:
                st.success("✅ Correct! CB is below Taylor rate (behind curve) → market expects future hikes → capital inflows → currency appreciates.")
            else:
                st.error("❌ Incorrect. Taylor Rate (5.5%) > Actual (4.0%): CB is behind the curve → hikes expected → currency should appreciate as rate expectations are priced in.")
        st.markdown("---")

        st.markdown("**Q3. In a risk-off environment, which currencies typically strengthen?**")
        q3 = st.radio("", [
            "AUD, NZD and commodity currencies",
            "JPY, CHF and USD (safe havens)",
            "EM currencies with high yields",
            "EUR and GBP specifically"
        ], key="fx9q3")
        if st.button("Check Q3", key="fx9c3"):
            if "JPY, CHF and USD" in q3:
                st.success("✅ Correct! Risk-off: investors flee to safety → JPY, CHF, USD appreciate. AUD, NZD, EM currencies fall as carry trades are unwound.")
            else:
                st.error("❌ Incorrect. Risk-off safe havens: JPY (near-zero rates but historically safe), CHF (Swiss stability), USD (global reserve currency).")
        st.markdown("---")

        st.markdown("**Q4. BEER (Behavioural Equilibrium Exchange Rate) estimates:**")
        q4 = st.radio("", [
            "The next 24-hour FX move based on order flow",
            "Medium-term FX fair value based on macro fundamentals like ToT, NFA, and productivity",
            "The exact rate a central bank will target for intervention",
            "The forward rate implied by interest rate differentials"
        ], key="fx9q4")
        if st.button("Check Q4", key="fx9c4"):
            if "macro fundamentals" in q4 and "medium-term" in q4.lower():
                st.success("✅ Correct! BEER uses macro variables (Terms of Trade, Net Foreign Assets, productivity differentials) to estimate medium-term fair value.")
            else:
                st.error("❌ Incorrect. BEER = Behavioural Equilibrium Exchange Rate. Uses macro fundamentals to estimate medium-term FX fair value. Not for short-term forecasting.")
        st.markdown("---")

        st.markdown("**Q5. The standard FX reserves adequacy benchmark for import cover is:**")
        q5 = st.radio("", [
            "1 month of imports",
            "3 months of imports",
            "6 months of imports",
            "12 months of imports"
        ], key="fx9q5")
        if st.button("Check Q5", key="fx9c5"):
            if q5 == "3 months of imports":
                st.success("✅ Correct! The IMF standard is at least 3 months of import cover. Below 3 months signals vulnerability to speculative attacks and currency crises.")
            else:
                st.error("❌ Incorrect. The standard IMF benchmark is 3 months of import cover. Also check: short-term debt coverage > 100% and M2 coverage > 20%.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Macro FX Drivers — Quick Reference")
        drivers_df = pd.DataFrame({
            "Driver": ["Interest Rate Differential", "Central Bank Surprise", "Risk-Off Event", "Current Account Surplus", "BEER Undervaluation", "Reserve Depletion"],
            "Effect on Domestic Currency": ["Higher i_d relative to i_f → Appreciates", "Surprise hike → Immediate sharp appreciation", "Global risk-off → Depreciates (unless safe haven)", "Exports > Imports → Appreciates over time", "Undervalued by BEER → Long-run appreciation potential", "Depleting reserves → Weakens, signals vulnerability"],
            "Timeframe": ["Short-medium term", "Immediate (minutes)", "Hours to weeks", "Medium-long term", "3-5 years", "Medium term"],
            "Key Formula": ["Carry = i_high - i_low", "Taylor Rate deviation", "VIX correlation", "CA balance / GDP", "BEER misalignment %", "Import cover months"]
        })
        st.dataframe(drivers_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "Carry Trade Gross Return",
                "Carry Trade Net Return",
                "Taylor Rule Rate",
                "Import Cover",
                "Debt Coverage",
                "BEER Misalignment"
            ],
            "Expression": [
                "i_high - i_low",
                "i_high - i_low - transaction costs - actual FX depreciation",
                "i = r* + pi + alpha(pi - pi*) + beta(y - y*)",
                "FX Reserves / Monthly Imports  (target: > 3 months)",
                "FX Reserves / Short-term External Debt × 100%  (target: > 100%)",
                "(Actual Rate - BEER Fair Value) / BEER Fair Value × 100%"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Risk-On vs Risk-Off — Currency Cheat Sheet")
        roro_df = pd.DataFrame({
            "Currency": ["JPY", "CHF", "USD", "AUD", "NZD", "EM currencies", "CAD"],
            "Risk-ON": ["Weakens (safe haven sold)", "Weakens slightly", "Mixed (depends on risk appetite)", "Strengthens", "Strengthens", "Strengthens", "Strengthens (oil)"],
            "Risk-OFF": ["Strengthens sharply", "Strengthens", "Strengthens (reserve currency)", "Weakens sharply", "Weakens sharply", "Weakens significantly", "Weakens (oil falls)"],
            "Key Driver": ["Safe haven, low yield", "Swiss stability", "Global reserve currency", "Commodities, China", "Commodities, risk proxy", "Carry, growth", "Oil price"]
        })
        st.dataframe(roro_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Running carry trades without stop-losses",
                "Reacting only to actual rate decisions (not forward guidance)",
                "Ignoring VIX when running risk currencies long",
                "Treating BEER/FEER deviations as near-term trade signals",
                "Assessing reserves only by import cover (missing debt angle)"
            ],
            "Correct Approach": [
                "Size carry appropriately; use tight stops given fat-tail risk in risk-off",
                "FX prices the expected path 6-12 months ahead; track forward guidance obsessively",
                "VIX > 25 = reduce risk-on positions; VIX > 35 = aggressive risk reduction",
                "BEER/FEER = structural backdrop only; need a catalyst for mean reversion",
                "Use all three metrics: import cover + debt coverage + M2 coverage (IMF ARA composite)"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 9 Complete! You can analyse macro FX drivers, calculate carry trade returns, apply the Taylor Rule, and assess reserves adequacy.")
        st.info("💡 Next: Module 10 — Technical Analysis in FX (RSI, MACD, Fibonacci, chart patterns)")

if __name__ == "__main__":
    show()