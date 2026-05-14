import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏦 Module 11: FX in Capital Markets & Corporate Finance")
    st.markdown("*Master FX-adjusted DCF, cross-border M&A FX risk, currency-hedged portfolio returns, and currency overlay strategies*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. FX-Adjusted DCF Valuation")
        st.markdown("""
        When valuing a foreign business or project, the FX dimension must be explicitly handled.
        There are two theoretically equivalent approaches:

        **Approach 1 — Discount in Local Currency, Convert NPV:**
        ```
        Step 1: Forecast all cash flows in local (foreign) currency
        Step 2: Discount at the local WACC (reflects local market risks)
        Step 3: Convert NPV to home currency at TODAY's spot rate

        NPV_home = [Sum of CF_local / (1 + WACC_local)^t] x S0
        ```

        **Approach 2 — Convert Cash Flows at Forward Rates, Discount at Home WACC:**
        ```
        Step 1: Forecast cash flows in local currency
        Step 2: Convert each year's cash flow at the CIP forward rate for that year
        Step 3: Discount converted cash flows at home WACC

        NPV_home = Sum of [CF_local x F_t / (1 + WACC_home)^t]
        ```

        **Both approaches give the same result if CIP holds.**
        Approach 2 is more transparent and easier to audit in practice.

        **EM Premium Adjustment:**
        For emerging market projects, add a Country Risk Premium (CRP) to the discount rate:
        ```
        WACC_EM = WACC_base + Country Risk Premium + Political Risk Premium
        CRP typically sourced from Damodaran's country risk database
        ```
        """)

        st.subheader("2. FX Risk in Cross-Border M&A")
        st.markdown("""
        Cross-border M&A transactions face FX risk from **announcement to closing** (which can take 6–18 months)
        and **post-merger** in translation and economic exposure.

        | Stage | FX Risk | Hedging Instrument |
        |-------|---------|-------------------|
        | **Pre-announcement** | Confidential — cannot hedge | None possible |
        | **Announcement to closing** | Deal price fixed in foreign currency — FX moves affect home value | FX option (preferred over forward) |
        | **Post-closing** | Translation exposure from foreign subsidiary | Cross-currency swaps, balance sheet matching |

        **Why options, not forwards, for deal hedging:**
        ```
        If the deal FAILS (regulatory block, shareholder rejection):
          Forward: You still OWE the forward trade → naked FX position → potential large loss
          Option:  Simply expires — you lose only the premium paid

        → FX options are the preferred instrument for contingent M&A exposure
        ```

        **Deal break-even analysis:**
        ```
        Break-even rate = Agreed acquisition price (foreign) / Acquisition value (home)
        If spot moves beyond break-even before closing → deal may need renegotiation
        ```
        """)

        st.subheader("3. Currency-Hedged Portfolio Returns")
        st.markdown("""
        For international investment portfolios, currency risk can be a significant source
        of return volatility. The total return equation is:

        ```
        Total Unhedged Return = Local Asset Return + Currency Return

        Total Hedged Return  = Local Asset Return + Hedge Return
        Hedge Return         ≈ Domestic Rate - Foreign Rate  (by CIP)

        Therefore:
        Fully Hedged Return ≈ Local Asset Return + (r_domestic - r_foreign)
        ```

        **Key insight (by CIP):**
        A fully currency-hedged foreign bond returns approximately the **domestic risk-free rate**.
        This is why hedged foreign bonds are used as alternatives to domestic bonds —
        they provide credit diversification without currency risk.

        **Partial hedging:**
        ```
        Hedge Ratio h (0 to 1):
        Hedged Return = Local Return + h x (r_d - r_f) + (1-h) x Actual FX Return
        ```
        """)

        st.subheader("4. Currency Overlay")
        st.markdown("""
        **Currency overlay** separates the currency decision from the underlying asset management decision.
        A specialist overlay manager runs FX positions independently of the asset manager.

        | Overlay Type | Purpose | Strategy |
        |-------------|---------|---------|
        | **Passive (defensive)** | Reduce currency risk to near zero | Systematic hedging of all foreign currency exposures |
        | **Active** | Generate alpha from currency views | Tactical tilts vs benchmark hedge ratio |
        | **Dynamic** | Adjust hedge ratio based on market signals | Momentum, carry, valuation signals |

        **Overlay benchmark:**
        The benchmark hedge ratio (typically 0%, 50%, or 100%) is set by the investment committee.
        Active overlay adds value (or loses it) relative to this benchmark.

        **Who uses currency overlay:**
        - Large pension funds (e.g. ABP Netherlands, CalPERS)
        - Sovereign wealth funds (e.g. GIC Singapore, Norges Bank)
        - Insurance companies with global fixed income portfolios
        """)

        st.subheader("5. Foreign Currency Debt & CCBS Hedging")
        st.markdown("""
        Companies frequently issue debt in foreign currencies to:
        - Access deeper or cheaper capital markets
        - Create a natural hedge (USD revenues, USD debt)
        - Diversify the investor base

        **Swapping foreign debt to home currency:**
        ```
        Step 1: Issue USD bond at USD coupon rate (e.g. SOFR + 80 bps)
        Step 2: Enter cross-currency basis swap:
                Pay USD SOFR + basis, Receive EUR €STR
        Step 3: Effective EUR funding = EUR bond equivalent cost

        All-in EUR cost = EUR bond spread + CCS basis (negative = cheaper)
        ```

        **CCBS advantage:**
        When EUR/USD CCS basis is negative (USD at a premium), a US company
        issuing EUR bonds and swapping to USD can achieve cheaper USD funding
        than direct USD issuance.
        """)

        st.subheader("6. EM Currency Risk in International Investment")
        st.markdown("""
        Emerging market currencies carry additional risks beyond standard FX volatility:

        | Risk Factor | Description | Impact |
        |------------|-------------|--------|
        | **Higher volatility** | EM FX vol 3-5x developed market | Wider bid-ask, higher hedging cost |
        | **Capital controls** | Government restrictions on currency flows | NDFs required (Module 4) |
        | **Political risk** | Policy changes, nationalisation, sanctions | Risk premium in discount rate |
        | **Liquidity risk** | Thin markets, large bid-ask spreads | Higher transaction costs |
        | **Convertibility risk** | Currency may become non-convertible | Structural hedge via NDF or operational hedge |

        **EM WACC adjustment:**
        ```
        WACC_EM = WACC_base + CRP + Illiquidity Premium

        Example: Brazil project
          Base WACC:           10.0%
          Brazil CRP:          +4.5% (Damodaran estimate)
          Illiquidity:         +1.0%
          EM WACC:             15.5%
        ```
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: FX-Adjusted DCF — German Subsidiary Acquisition")
        st.markdown("""
        **US company acquires a German business. Forecast EUR cash flows over 5 years.**

        **Inputs:**
        ```
        EUR/USD spot:     1.0850
        US WACC:          10.0%
        German WACC:       8.0%
        US rate:           5.25%
        EU rate:           3.75%

        Year  EUR Cash Flow    CIP Forward    USD Cash Flow
          1    €2,000,000       1.1007          $2,201,400
          2    €2,200,000       1.1167          $2,456,740
          3    €2,420,000       1.1330          $2,741,860
          4    €2,662,000       1.1496          $3,060,179
          5    €2,928,200       1.1665          $3,415,773
        ```

        **Approach 1 (Discount at German WACC, convert at spot):**
        ```
        PV(EUR) = 2M/1.08 + 2.2M/1.08² + 2.42M/1.08³ + 2.662M/1.08⁴ + 2.928M/1.08⁵
                = 1.852M + 1.886M + 1.922M + 1.957M + 1.993M
                = €9,610,000
        NPV_USD = €9.61M × 1.0850 = $10,427,000
        ```

        **Approach 2 (Convert at forwards, discount at US WACC):**
        ```
        PV_USD = 2.201M/1.10 + 2.457M/1.10² + 2.742M/1.10³ + 3.060M/1.10⁴ + 3.416M/1.10⁵
               = $2.001M + $2.031M + $2.060M + $2.089M + $2.120M
               = $10,301,000
        ```
        Small difference due to compounding. Both approaches confirm value ~$10.3–10.4M.
        """)

        st.subheader("Example 2: M&A Deal FX Hedge — Option vs Forward")
        st.markdown("""
        **US company announces acquisition of UK target for GBP 500M.**
        **GBP/USD at announcement: 1.2700. Expected closing in 9 months.**

        | Hedge | Structure | Cost | Risk if Deal Fails |
        |-------|-----------|------|-------------------|
        | No hedge | Do nothing | Zero | Full FX exposure — if GBP/USD falls to 1.20, save $35M. If rises to 1.35, lose $40M |
        | Forward | Buy GBP 500M 9M forward at 1.2675 | Zero premium | If deal fails, naked short USD 633.75M position |
        | Option | Buy GBP 500M call at 1.2700, 9M | ~$12M (1.9% of deal) | Option lapses — lose only $12M premium |

        ```
        Option Hedge Analysis:
        Deal closes at GBP/USD 1.3000 (GBP strengthened):
          Without option: Acquisition costs USD 650M (vs $635M locked by forward)
          With option:    Exercise at 1.2700 → USD 635M + $12M premium = $647M total

        Deal fails (regulatory block) at GBP/USD 1.2400:
          Without option: No problem — just don't buy GBP
          With forward:   Must sell GBP 500M at 1.2675, then buy back at 1.2400 → GAIN $13.75M
                          BUT... if GBP/USD was at 1.3000: LOSE $16.25M!
          With option:    Option expires worthless. Loss = $12M premium only.

        Conclusion: Option preferred for contingent deal exposure despite premium cost.
        ```
        """)

        st.subheader("Example 3: Currency-Hedged Bond Return")
        st.markdown("""
        **US investor buys German Bund (EUR-denominated) and hedges EUR/USD exposure.**

        ```
        German Bund yield:    3.75% p.a.
        USD/EUR forward rate: USD rate 5.25% - EUR rate 3.75% = +1.50% USD premium
        EUR/USD hedge return: = +1.50% (receive 1.50% p.a. from the forward hedge)

        Total Hedged Return = 3.75% (Bund yield) + 1.50% (hedge return)
                            = 5.25%

        US Treasury yield:    5.25%

        Result: Hedged German Bund ≈ US Treasury yield — confirmed by CIP!
        ```

        **Practical implication:**
        ```
        Hedged EUR Bund:         5.25% with German credit quality
        US Treasury:             5.25% with US government credit quality

        If German Bund has +50 bps credit spread (government bonds are the same, but
        for corporate bonds the spread is the value):
        Hedged EUR Corporate:    5.25% + 0.50% = 5.75%  ← Extra yield for same risk

        This is WHY international bond investors buy hedged foreign bonds:
        to capture credit spreads without taking on currency risk.
        ```
        """)

        st.subheader("Example 4: Currency Overlay — Active Performance Attribution")
        st.markdown("""
        **Pension fund with 40% international equity allocation. Benchmark: 50% hedged.**

        | Portfolio | Hedge Ratio | Currency Return | Alpha vs Benchmark |
        |-----------|------------|----------------|-------------------|
        | Benchmark | 50% | +0.80% | — |
        | Active Overlay A | 75% (overweight hedge) | +0.50% | −0.30% (underperformed) |
        | Active Overlay B | 25% (underweight hedge) | +1.40% | +0.60% (outperformed) |
        | Active Overlay C | 100% (fully hedged) | +0.20% | −0.60% (underperformed) |

        ```
        Active Overlay B Analysis:
          Decision: Reduce hedge from 50% to 25% (go more unhedged)
          Reason: Manager forecasted USD weakness vs EUR/GBP
          Result: USD weakened → unhedged portion benefited → +1.40% currency return
          Alpha: +0.60% vs 50% benchmark

          Attribution:
          Active decision: 25% hedge vs 50% benchmark
          = 25% additional foreign currency exposure
          Currency gain: 25% x FX return = 25% x 2.4% = +0.60% alpha
        ```
        """)

        st.subheader("Example 5: EM Investment — Brazil Project WACC")
        st.markdown("""
        **US company evaluating a 5-year manufacturing project in Brazil.**

        ```
        Base US WACC:               10.0%
        Brazil country risk (CRP):  +4.5%  (sovereign spread + equity risk adj.)
        BRL illiquidity premium:    +1.0%
        Political risk premium:     +0.5%
        ─────────────────────────────────────
        Brazil Project WACC:        16.0%

        Year 1 BRL cash flows: BRL 50M
        USD/BRL spot:          5.00
        1Y CIP Forward:        5.00 x (1.10/1.065) ≈ 5.165 (approx, using rate differential)

        USD Year 1 CF:         BRL 50M / 5.165 = USD 9.68M
        PV (Year 1):           USD 9.68M / 1.16 = USD 8.34M

        The 16% discount rate correctly reflects:
        - The time value of money (US 10%)
        - Country risk (default, expropriation: 4.5%)
        - Liquidity and political risk premiums (1.5%)
        ```
        Compare to a similar US project discounted at 10% — the hurdle is much higher
        for Brazil, requiring substantially higher cash flows to justify investment.
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "🏗️ FX-Adjusted DCF Valuation",
            "🤝 M&A Deal FX Hedge Analyser",
            "📈 Hedged Bond Return Calculator",
            "🌐 Currency Overlay Performance",
            "🌍 EM Project WACC Builder"
        ])

        st.markdown("---")

        # ── FX-ADJUSTED DCF ───────────────────────────────────────────
        if calc_choice == "🏗️ FX-Adjusted DCF Valuation":
            st.subheader("FX-Adjusted DCF — Cross-Border Project / Acquisition Valuation")
            st.info("Value a foreign project using two equivalent approaches.")
            col1, col2 = st.columns(2)
            with col1:
                spot_dcf   = st.number_input("Current Spot Rate (home/foreign)", value=1.0850, format="%.4f")
                wacc_local = st.number_input("Local (Foreign) WACC %", value=8.0, step=0.5)
                wacc_home  = st.number_input("Home WACC %", value=10.0, step=0.5)
            with col2:
                r_home     = st.number_input("Home Interest Rate %", value=5.25, step=0.05)
                r_foreign  = st.number_input("Foreign Interest Rate %", value=3.75, step=0.05)
                num_years  = st.number_input("Number of Years", value=5, min_value=1, max_value=20)
                terminal_g = st.number_input("Terminal Growth Rate %", value=2.0, step=0.5)

            st.markdown("**Annual Cash Flows (in local/foreign currency):**")
            cf_inputs = []
            cols_cf = st.columns(min(int(num_years), 5))
            for i in range(int(num_years)):
                default_cf = 2000000.0 * (1.1 ** i)
                cf = cols_cf[i % 5].number_input(f"Year {i+1}", value=round(default_cf, 0),
                                                  step=100000.0, key=f"cf_{i}")
                cf_inputs.append(cf)

            if st.button("🏗️ Calculate FX-Adjusted NPV", type="primary"):
                fwd_rates = [spot_dcf * ((1 + r_home/100) / (1 + r_foreign/100)) ** t
                             for t in range(1, int(num_years) + 1)]
                terminal_value_local = cf_inputs[-1] * (1 + terminal_g/100) / (wacc_local/100 - terminal_g/100)
                terminal_value_home  = terminal_value_local * fwd_rates[-1] / (1 + wacc_home/100) ** int(num_years)

                pv_local_list = [cf / (1 + wacc_local/100) ** (i+1) for i, cf in enumerate(cf_inputs)]
                pv_home_list  = [cf * fwd_rates[i] / (1 + wacc_home/100) ** (i+1) for i, cf in enumerate(cf_inputs)]
                tv_local      = terminal_value_local / (1 + wacc_local/100) ** int(num_years)

                npv_approach1 = (sum(pv_local_list) + tv_local) * spot_dcf
                npv_approach2 = sum(pv_home_list) + terminal_value_home

                st.markdown("---")
                rows_dcf = []
                for i in range(int(num_years)):
                    rows_dcf.append({
                        "Year": i+1,
                        "CF (local)": f"{cf_inputs[i]:,.0f}",
                        "CIP Forward": f"{fwd_rates[i]:.4f}",
                        "CF (home)": f"{cf_inputs[i]*fwd_rates[i]:,.0f}",
                        "PV App.1 (local)": f"{pv_local_list[i]:,.0f}",
                        "PV App.2 (home)": f"{pv_home_list[i]:,.0f}"
                    })
                st.dataframe(pd.DataFrame(rows_dcf), use_container_width=True, hide_index=True)

                c1, c2, c3 = st.columns(3)
                c1.metric("NPV — Approach 1", f"{npv_approach1:,.0f} home")
                c2.metric("NPV — Approach 2", f"{npv_approach2:,.0f} home")
                c3.metric("Difference", f"{abs(npv_approach1-npv_approach2):,.0f}",
                          "Should be ~zero if CIP holds")

                if abs(npv_approach1 - npv_approach2) / max(npv_approach1, 1) < 0.02:
                    st.success("✅ Both approaches consistent (< 2% difference) — CIP approximately holds.")
                else:
                    st.warning("⚠️ Approaches differ > 2%. Check that WACC rates are consistent with interest rate assumptions.")

                fig = go.Figure()
                fig.add_trace(go.Bar(x=[f"Y{i+1}" for i in range(int(num_years))], y=pv_home_list,
                    name="PV of CFs", marker_color="#2E86C1"))
                fig.add_hline(y=0, line_color="black")
                fig.update_layout(title="Present Value of Foreign Cash Flows (Approach 2 — Home Currency)",
                                  xaxis_title="Year", yaxis_title="PV (home currency)")
                st.plotly_chart(fig, use_container_width=True)

        # ── M&A HEDGE ANALYSER ────────────────────────────────────────
        elif calc_choice == "🤝 M&A Deal FX Hedge Analyser":
            st.subheader("Cross-Border M&A Deal FX Hedge Analyser")
            col1, col2 = st.columns(2)
            with col1:
                deal_size_foreign = st.number_input("Acquisition Price (foreign currency)", value=500000000.0, step=10000000.0)
                spot_ma           = st.number_input("Spot Rate at Announcement (home/foreign)", value=1.2700, format="%.4f")
                deal_months       = st.slider("Expected Months to Closing", 3, 24, 9)
                r_home_ma         = st.number_input("Home Rate % p.a.", value=5.25, step=0.05, key="ma_rh")
                r_for_ma          = st.number_input("Foreign Rate % p.a.", value=3.75, step=0.05, key="ma_rf")
            with col2:
                option_premium_pct = st.number_input("Call Option Premium (% of notional)", value=1.9, step=0.1)
                deal_success_prob  = st.slider("Deal Completion Probability %", 10, 100, 80)

            if st.button("🤝 Analyse M&A Hedge", type="primary"):
                fwd_rate   = spot_ma * (1 + r_home_ma/100 * deal_months/12) / (1 + r_for_ma/100 * deal_months/12)
                option_cost = deal_size_foreign * option_premium_pct / 100 * spot_ma
                deal_home  = deal_size_foreign * spot_ma

                scenario_rates = [spot_ma * (1 + m/100) for m in [-15, -10, -5, 0, 5, 10, 15]]
                scenario_labels = [f"{m:+d}%" for m in [-15, -10, -5, 0, 5, 10, 15]]

                results = []
                for rate, label in zip(scenario_rates, scenario_labels):
                    unhedged = deal_size_foreign * rate
                    fwd_cost = deal_size_foreign * fwd_rate
                    opt_cost = max(deal_size_foreign * rate, deal_size_foreign * spot_ma) + option_cost
                    results.append({
                        "FX Move": label,
                        "Spot at Close": f"{rate:.4f}",
                        "Unhedged Cost": f"{unhedged:,.0f}",
                        "Forward Hedge": f"{fwd_cost:,.0f}",
                        "Option Hedge": f"{opt_cost:,.0f}",
                        "Option vs Unhedged": f"{opt_cost-unhedged:+,.0f}"
                    })
                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

                c1, c2, c3 = st.columns(3)
                c1.metric("Deal Size (home currency)", f"{deal_home:,.0f}")
                c2.metric("CIP Forward Rate", f"{fwd_rate:.4f}")
                c3.metric("Option Premium Cost", f"{option_cost:,.0f}")

                fig = go.Figure()
                unhedged_costs = [deal_size_foreign * r for r in scenario_rates]
                fwd_costs      = [deal_size_foreign * fwd_rate] * len(scenario_rates)
                opt_costs      = [max(deal_size_foreign * r, deal_size_foreign * spot_ma) + option_cost for r in scenario_rates]
                fig.add_trace(go.Scatter(x=scenario_labels, y=unhedged_costs, name="Unhedged",
                    line=dict(color="#E74C3C", width=2, dash="dot"), mode="lines+markers"))
                fig.add_trace(go.Scatter(x=scenario_labels, y=fwd_costs, name="Forward Hedge",
                    line=dict(color="#27AE60", width=2.5), mode="lines+markers"))
                fig.add_trace(go.Scatter(x=scenario_labels, y=opt_costs, name="Option Hedge",
                    line=dict(color="#F39C12", width=2, dash="dash"), mode="lines+markers"))
                fig.update_layout(title="M&A Acquisition Cost — Hedge Strategy Comparison",
                                  xaxis_title="FX Move from Announcement", yaxis_title="Total Acquisition Cost (home)")
                st.plotly_chart(fig, use_container_width=True)
                st.info(f"💡 If deal fails ({100-deal_success_prob}% probability): Forward leaves a naked position. Option loses only {option_cost:,.0f} in premium. For contingent M&A exposure, options are preferred.")

        # ── HEDGED BOND RETURN ────────────────────────────────────────
        elif calc_choice == "📈 Hedged Bond Return Calculator":
            st.subheader("Currency-Hedged Foreign Bond Return Calculator")
            st.info("Calculate the all-in return of a foreign bond with full currency hedging (CIP-based).")
            col1, col2 = st.columns(2)
            with col1:
                foreign_yield  = st.number_input("Foreign Bond Yield % p.a.", value=3.75, step=0.05)
                credit_spread  = st.number_input("Credit Spread above sovereign (bps)", value=0.0, step=10.0)
                r_domestic_hb  = st.number_input("Domestic Risk-Free Rate % p.a.", value=5.25, step=0.05, key="hb_rd")
                r_foreign_hb   = st.number_input("Foreign Risk-Free Rate % p.a.", value=3.75, step=0.05, key="hb_rf")
            with col2:
                ccs_basis_hb   = st.number_input("CCS Basis (bps, negative = USD premium)", value=-25.0, step=5.0)
                tenor_hb       = st.number_input("Investment Horizon (years)", value=5, min_value=1)
                invest_amt_hb  = st.number_input("Investment Amount (home currency)", value=10000000.0, step=1000000.0)

            if st.button("📈 Calculate Hedged Return", type="primary"):
                hedge_return    = r_domestic_hb - r_foreign_hb
                cip_hedged      = foreign_yield + credit_spread/100 + hedge_return
                ccbs_adj_hedged = foreign_yield + credit_spread/100 + hedge_return + ccs_basis_hb/100
                unhedged_total  = foreign_yield + credit_spread/100
                domestic_rf     = r_domestic_hb

                total_income_cip  = invest_amt_hb * cip_hedged / 100 * tenor_hb
                total_income_ccbs = invest_amt_hb * ccbs_adj_hedged / 100 * tenor_hb

                st.markdown("---")
                st.markdown(f"""
                **Currency-Hedged Bond Return Breakdown:**
                ```
                Foreign Bond Yield:      {foreign_yield:.2f}%
                Credit Spread:           {credit_spread:.0f} bps
                Total Foreign Yield:     {foreign_yield + credit_spread/100:.2f}%

                Hedge Return (by CIP):   r_domestic - r_foreign
                                       = {r_domestic_hb:.2f}% - {r_foreign_hb:.2f}%
                                       = {hedge_return:+.2f}%

                CCS Basis Adjustment:   {ccs_basis_hb:+.0f} bps

                ─────────────────────────────────────────────────────
                Fully Hedged Return (CIP):    {cip_hedged:.2f}%
                Hedged Return (incl. basis):  {ccbs_adj_hedged:.2f}%
                Domestic Risk-Free Rate:      {domestic_rf:.2f}%
                Unhedged Return:              {unhedged_total:.2f}%
                ```
                """)
                returns_df = pd.DataFrame({
                    "Strategy": ["Domestic Risk-Free", "Fully Hedged (CIP)", "Hedged incl. CCS Basis", "Unhedged Foreign Bond"],
                    "Annual Return %": [f"{domestic_rf:.2f}%", f"{cip_hedged:.2f}%",
                                        f"{ccbs_adj_hedged:.2f}%", f"{unhedged_total:.2f}%"],
                    f"{tenor_hb}Y Total Income": [
                        f"{invest_amt_hb * domestic_rf/100 * tenor_hb:,.0f}",
                        f"{total_income_cip:,.0f}",
                        f"{total_income_ccbs:,.0f}",
                        f"{invest_amt_hb * unhedged_total/100 * tenor_hb:,.0f}"
                    ],
                    "Currency Risk": ["None", "None", "None", "Full FX exposure"]
                })
                st.dataframe(returns_df, use_container_width=True, hide_index=True)

                fig = go.Figure(go.Bar(
                    x=["Domestic RF", "Hedged (CIP)", "Hedged (basis adj.)", "Unhedged"],
                    y=[domestic_rf, cip_hedged, ccbs_adj_hedged, unhedged_total],
                    marker_color=["#95A5A6", "#27AE60", "#2E86C1", "#E74C3C"],
                    text=[f"{r:.2f}%" for r in [domestic_rf, cip_hedged, ccbs_adj_hedged, unhedged_total]],
                    textposition="outside"
                ))
                fig.update_layout(title="Annual Return Comparison — Bond Investment Strategies",
                                  yaxis_title="Return % p.a.",
                                  yaxis=dict(range=[0, max(domestic_rf, cip_hedged, ccbs_adj_hedged, unhedged_total) * 1.3]))
                st.plotly_chart(fig, use_container_width=True)
                st.info(f"💡 CIP insight: Fully hedged foreign bond return ({cip_hedged:.2f}%) ≈ domestic rate ({domestic_rf:.2f}%). The CCS basis ({ccs_basis_hb:.0f} bps) adjusts the return slightly.")

        # ── CURRENCY OVERLAY ──────────────────────────────────────────
        elif calc_choice == "🌐 Currency Overlay Performance":
            st.subheader("Currency Overlay — Attribution & Performance Analysis")
            col1, col2 = st.columns(2)
            with col1:
                benchmark_hedge = st.number_input("Benchmark Hedge Ratio %", value=50.0, step=5.0)
                portfolio_value = st.number_input("Portfolio Value (home currency)", value=100000000.0, step=5000000.0)
                num_currencies  = st.number_input("Number of Foreign Currencies", value=4, min_value=1, max_value=8)
            with col2:
                st.markdown("**Enter currency returns and overlay positions:**")

            currencies_ov = ["EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "SGD", "HKD"]
            default_weights = [0.30, 0.20, 0.25, 0.15, 0.10, 0.0, 0.0, 0.0]
            default_fx_returns = [2.5, -1.5, -3.0, 4.0, 1.5, 0.5, 0.0, 0.0]
            default_overlay_hedge = [30.0, 80.0, 90.0, 20.0, 50.0, 50.0, 50.0, 50.0]

            ov_rows = []
            for i in range(int(num_currencies)):
                col1, col2, col3 = st.columns(3)
                ccy     = col1.text_input(f"Currency {i+1}", value=currencies_ov[i], key=f"ov_ccy_{i}")
                weight  = col2.number_input(f"Portfolio weight %", value=default_weights[i]*100 if i < 8 else 10.0, step=1.0, key=f"ov_w_{i}")
                fx_ret  = col1.number_input(f"FX return % (+ = foreign appreciates)", value=default_fx_returns[i] if i < 8 else 0.0, step=0.5, key=f"ov_fx_{i}")
                hedge   = col3.number_input(f"Overlay hedge ratio %", value=default_overlay_hedge[i] if i < 8 else 50.0, step=5.0, key=f"ov_h_{i}")
                ov_rows.append({"ccy": ccy, "weight": weight/100, "fx_ret": fx_ret/100, "hedge": hedge/100})

            if st.button("🌐 Analyse Currency Overlay", type="primary"):
                results_ov = []
                total_alpha = 0
                for row in ov_rows:
                    benchmark_return = row["fx_ret"] * (1 - benchmark_hedge/100) * row["weight"]
                    actual_return    = row["fx_ret"] * (1 - row["hedge"]) * row["weight"]
                    alpha            = actual_return - benchmark_return
                    total_alpha     += alpha
                    results_ov.append({
                        "Currency": row["ccy"],
                        "Weight": f"{row['weight']*100:.1f}%",
                        "FX Return": f"{row['fx_ret']*100:+.2f}%",
                        "Benchmark Hedge": f"{benchmark_hedge:.0f}%",
                        "Overlay Hedge": f"{row['hedge']*100:.0f}%",
                        "Benchmark Return": f"{benchmark_return*100:+.3f}%",
                        "Actual Return": f"{actual_return*100:+.3f}%",
                        "Alpha": f"{alpha*100:+.3f}%"
                    })
                st.dataframe(pd.DataFrame(results_ov), use_container_width=True, hide_index=True)
                total_dollar_alpha = total_alpha * portfolio_value
                c1, c2, c3 = st.columns(3)
                c1.metric("Total Currency Alpha", f"{total_alpha*100:+.3f}%")
                c2.metric("Dollar Alpha", f"{total_dollar_alpha:+,.0f}")
                c3.metric("Benchmark Hedge", f"{benchmark_hedge:.0f}%")
                if total_alpha > 0:
                    st.success(f"✅ Overlay outperformed benchmark by {total_alpha*100:+.3f}% (${total_dollar_alpha:+,.0f})")
                else:
                    st.error(f"❌ Overlay underperformed benchmark by {abs(total_alpha)*100:.3f}% (${abs(total_dollar_alpha):,.0f})")

        # ── EM WACC BUILDER ───────────────────────────────────────────
        elif calc_choice == "🌍 EM Project WACC Builder":
            st.subheader("Emerging Market Project WACC Builder")
            col1, col2 = st.columns(2)
            with col1:
                base_wacc      = st.number_input("Base WACC (home market) %", value=10.0, step=0.5)
                country        = st.selectbox("Country", ["Brazil", "India", "China", "Mexico", "Indonesia", "Turkey", "South Africa", "Nigeria", "Custom"])
                crp_presets    = {"Brazil": 4.5, "India": 3.0, "China": 2.5, "Mexico": 3.5, "Indonesia": 4.0, "Turkey": 7.5, "South Africa": 5.0, "Nigeria": 8.0, "Custom": 3.0}
                crp            = st.number_input("Country Risk Premium (CRP) %", value=crp_presets[country], step=0.5)
            with col2:
                illiquidity    = st.number_input("Illiquidity Premium %", value=1.0, step=0.25)
                political_risk = st.number_input("Political Risk Premium %", value=0.5, step=0.25)
                currency_risk  = st.number_input("Currency/Convertibility Risk %", value=0.5, step=0.25)
                project_cf     = st.number_input("Year 1 Cash Flow (local currency millions)", value=50.0, step=5.0)
                spot_em        = st.number_input("Spot Rate (local/USD)", value=5.00, step=0.01)

            if st.button("🌍 Build EM WACC", type="primary"):
                em_wacc = base_wacc + crp + illiquidity + political_risk + currency_risk
                components_df = pd.DataFrame({
                    "Component": ["Base WACC", "Country Risk Premium (CRP)", "Illiquidity Premium",
                                  "Political Risk Premium", "Currency/Convertibility Risk", "Total EM WACC"],
                    "Rate %": [f"{base_wacc:.2f}%", f"{crp:.2f}%", f"{illiquidity:.2f}%",
                               f"{political_risk:.2f}%", f"{currency_risk:.2f}%", f"{em_wacc:.2f}%"],
                    "Source": ["CAPM + capital structure", "Damodaran sovereign spread adj.",
                               "Market depth & bid-ask costs", "Expropriation, regulatory risk",
                               "Capital controls, devaluation risk", "Sum of all components"]
                })
                st.dataframe(components_df, use_container_width=True, hide_index=True)

                yr1_usd  = project_cf / spot_em
                pv_yr1   = yr1_usd / (1 + em_wacc/100)
                pv_yr1_base = yr1_usd / (1 + base_wacc/100)
                diff     = pv_yr1_base - pv_yr1

                c1, c2, c3 = st.columns(3)
                c1.metric("EM WACC", f"{em_wacc:.2f}%")
                c2.metric("Year 1 PV (EM WACC)", f"${pv_yr1:.2f}M")
                c3.metric("vs Base WACC PV", f"-${diff:.2f}M",
                          help="How much lower the PV is due to the EM risk premiums")

                fig = go.Figure(go.Waterfall(
                    orientation="v", measure=["relative","relative","relative","relative","relative","total"],
                    x=["Base WACC", "CRP", "Illiquidity", "Political", "Currency", "EM Total"],
                    y=[base_wacc, crp, illiquidity, political_risk, currency_risk, 0],
                    connector={"line": {"color": "rgb(63,63,63)"}},
                    increasing={"marker": {"color": "#E74C3C"}},
                    totals={"marker": {"color": "#2E86C1"}}
                ))
                fig.update_layout(title=f"EM WACC Components — {country} Project",
                                  yaxis_title="Rate %")
                st.plotly_chart(fig, use_container_width=True)
                st.warning(f"⚠️ The EM risk premiums add {crp+illiquidity+political_risk+currency_risk:.1f}% to the hurdle rate. Year 1 PV is ${diff:.2f}M lower vs applying base WACC only. Projects must generate significantly higher cash flows to justify EM investment.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("NPV Sensitivity to Exchange Rate — Cross-Border Acquisition")
        spot_range_v = np.linspace(0.90, 1.25, 50)
        base_spot = 1.0850; wacc_l = 8.0; annual_cf = 2000000; years_v = 5
        npv_vals = []
        for s in spot_range_v:
            pv_local = sum(annual_cf * 1.05**i / (1 + wacc_l/100)**(i+1) for i in range(years_v))
            npv_vals.append(pv_local * s)

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=spot_range_v, y=npv_vals, mode="lines",
            line=dict(color="#2E86C1", width=2.5), name="NPV (home currency)"))
        fig1.add_vline(x=base_spot, line_dash="dash", line_color="gray",
                      annotation_text=f"Current Spot {base_spot}")
        fig1.update_layout(title="NPV Sensitivity to Exchange Rate (EUR/USD)",
                           xaxis_title="EUR/USD Rate", yaxis_title="NPV (USD)")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Hedged vs Unhedged International Bond Returns — 5-Year Simulation")
        np.random.seed(42)
        years_sim = list(range(2020, 2025))
        fx_returns = [2.5, -5.0, 8.0, -3.0, 1.5]
        bond_yield = 3.75; hedge_return = 1.50
        unhedged = [bond_yield + fx for fx in fx_returns]
        hedged   = [bond_yield + hedge_return] * len(years_sim)
        domestic = [5.25] * len(years_sim)

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=years_sim, y=unhedged, name="Unhedged Foreign Bond",
            marker_color=["#27AE60" if u > 0 else "#E74C3C" for u in unhedged]))
        fig2.add_trace(go.Scatter(x=years_sim, y=hedged, name="Hedged Foreign Bond",
            line=dict(color="#2E86C1", width=2.5), mode="lines+markers"))
        fig2.add_trace(go.Scatter(x=years_sim, y=domestic, name="Domestic Bond",
            line=dict(color="#F39C12", width=2, dash="dash"), mode="lines"))
        fig2.add_hline(y=0, line_color="black")
        fig2.update_layout(title="Hedged vs Unhedged Bond Return Comparison (Simulated)",
                           barmode="overlay", xaxis_title="Year", yaxis_title="Total Return %",
                           legend=dict(x=0.01, y=0.99))
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("EM WACC Components — Selected Countries")
        em_countries = ["Brazil", "India", "China", "Mexico", "Indonesia", "Turkey"]
        base_waccs   = [10, 10, 10, 10, 10, 10]
        crps         = [4.5, 3.0, 2.5, 3.5, 4.0, 7.5]
        other_prems  = [2.0, 1.5, 1.5, 2.0, 2.0, 3.0]
        total_em     = [b + c + o for b, c, o in zip(base_waccs, crps, other_prems)]
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(name="Base WACC", x=em_countries, y=base_waccs, marker_color="#2E86C1"))
        fig3.add_trace(go.Bar(name="Country Risk Premium", x=em_countries, y=crps, marker_color="#E74C3C"))
        fig3.add_trace(go.Bar(name="Other Premiums", x=em_countries, y=other_prems, marker_color="#F39C12"))
        fig3.update_layout(title="EM Project WACC Components by Country",
                           barmode="stack", xaxis_title="Country", yaxis_title="WACC %",
                           legend=dict(x=0.01, y=0.99))
        st.plotly_chart(fig3, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — FX in Capital Markets")

        st.markdown("**Q1. When valuing a foreign business using Approach 1 (discount at local WACC, convert at spot), the NPV is:**")
        q1 = st.radio("", [
            "Always higher than Approach 2",
            "Theoretically equivalent to Approach 2 if CIP holds",
            "Always more accurate because it uses the local market's risk assessment",
            "Only valid for developed market acquisitions"
        ], key="fx11q1")
        if st.button("Check Q1", key="fx11c1"):
            if "equivalent to Approach 2 if CIP holds" in q1:
                st.success("✅ Correct! Both approaches give the same result when CIP holds — they are mathematically equivalent. Approach 2 (convert at forwards) is often preferred for transparency.")
            else:
                st.error("❌ Incorrect. Both approaches are theoretically equivalent under CIP. Neither is systematically more accurate — they should produce the same answer.")
        st.markdown("---")

        st.markdown("**Q2. For M&A deal FX hedging, options are preferred over forwards because:**")
        q2 = st.radio("", [
            "Options are always cheaper than forwards",
            "If the deal fails, the option simply lapses — forwards leave a naked FX position",
            "Options do not require counterparty credit assessment",
            "Forwards cannot be used for deal periods longer than 3 months"
        ], key="fx11q2")
        if st.button("Check Q2", key="fx11c2"):
            if "deal fails" in q2 and "lapses" in q2:
                st.success("✅ Correct! M&A exposure is contingent — if the deal fails, a forward leaves you with a naked FX position. An option simply expires, losing only the premium.")
            else:
                st.error("❌ Incorrect. Options are preferred for contingent M&A exposure because they lapse if the deal fails. A forward would leave a dangerous naked position.")
        st.markdown("---")

        st.markdown("**Q3. A fully currency-hedged foreign bond returns approximately:**")
        q3 = st.radio("", [
            "The foreign bond yield without any adjustment",
            "Zero — the currency hedge eliminates all return",
            "The domestic risk-free rate (by CIP relationship)",
            "The average of the foreign yield and domestic yield"
        ], key="fx11q3")
        if st.button("Check Q3", key="fx11c3"):
            if "domestic risk-free rate (by CIP)" in q3:
                st.success("✅ Correct! By CIP: Hedged return = Foreign yield + (Domestic rate - Foreign rate) = Domestic rate. Hedged foreign bonds converge to the domestic risk-free rate plus any credit spread.")
            else:
                st.error("❌ Incorrect. CIP: Hedged return = Foreign bond yield + hedge return (r_domestic - r_foreign) ≈ Domestic risk-free rate. The credit spread above sovereign is the true excess return.")
        st.markdown("---")

        st.markdown("**Q4. Currency overlay separates currency management from asset management because:**")
        q4 = st.radio("", [
            "It reduces the total number of trades required",
            "Specialist overlay managers can focus on FX views independently, generating potential currency alpha",
            "It eliminates all currency risk from the portfolio",
            "It is required by accounting standards for pension funds"
        ], key="fx11q4")
        if st.button("Check Q4", key="fx11c4"):
            if "specialist overlay managers" in q4 or "currency alpha" in q4:
                st.success("✅ Correct! Overlay separates asset allocation from currency management — specialist overlay managers focus purely on FX, potentially adding alpha without changing the underlying portfolio.")
            else:
                st.error("❌ Incorrect. Currency overlay allows specialist FX managers to manage currency exposure independently, potentially generating alpha through active FX positioning vs a benchmark hedge ratio.")
        st.markdown("---")

        st.markdown("**Q5. When adding a Country Risk Premium to the WACC for an EM project:**")
        q5 = st.radio("", [
            "It only applies to the equity component of WACC",
            "It reflects sovereign default risk, political risk, illiquidity and currency convertibility risk",
            "It is always exactly 5% for all emerging markets",
            "It makes the NPV higher by reducing the discount rate"
        ], key="fx11q5")
        if st.button("Check Q5", key="fx11c5"):
            if "sovereign default risk, political risk" in q5:
                st.success("✅ Correct! The EM WACC premium captures: sovereign/country risk (CRP from spreads), political risk (expropriation, regulatory changes), illiquidity, and currency convertibility risk.")
            else:
                st.error("❌ Incorrect. EM WACC premium covers multiple risks: country default risk, political risk, illiquidity, and currency convertibility risk. It INCREASES the discount rate, REDUCING the NPV.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 FX in Capital Markets — Key Frameworks")
        frameworks_df = pd.DataFrame({
            "Framework": [
                "FX-Adjusted DCF (Approach 1)",
                "FX-Adjusted DCF (Approach 2)",
                "M&A Deal Hedge — Option",
                "Hedged Bond Return (CIP)",
                "Currency Overlay — Active",
                "EM Project WACC"
            ],
            "Formula / Method": [
                "NPV = [Sum CF_local / (1+WACC_local)^t] × S0",
                "NPV = Sum [CF_local × F_t / (1+WACC_home)^t]",
                "Buy FX call — lapses if deal fails (lose premium only)",
                "Hedged Return = Foreign Yield + (r_d - r_f) ≈ Domestic Rate",
                "Alpha = Actual currency return - Benchmark hedge return",
                "WACC_EM = Base WACC + CRP + Illiquidity + Political + FX risk"
            ],
            "Key Insight": [
                "Both approaches equivalent under CIP",
                "More transparent; each year's CF uses its own forward rate",
                "Options preferred vs forwards for contingent deal exposure",
                "Credit spread above sovereign is the real value-add of hedged foreign bonds",
                "Specialist overlay can generate FX alpha without changing assets",
                "EM risk premiums can add 5-15% to the discount rate vs developed markets"
            ]
        })
        st.dataframe(frameworks_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "FX-Adjusted NPV (Approach 2)",
                "CIP Forward Rate (year t)",
                "Hedged Bond Return",
                "EM WACC",
                "Deal Break-even Rate",
                "Currency Alpha"
            ],
            "Expression": [
                "NPV = Sum [CF_local_t × F_t / (1+WACC_home)^t]",
                "F_t = S0 × [(1+r_d)/(1+r_f)]^t",
                "Hedged Return = Foreign Yield + (r_domestic - r_foreign)",
                "WACC_EM = Base_WACC + CRP + Illiquidity + Political + FX_risk",
                "Break-even = Deal Price (foreign) / Deal Value (home)",
                "Alpha = Actual_hedge_ratio_return - Benchmark_hedge_ratio_return"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Cross-Border Transaction FX Checklist")
        checklist_df = pd.DataFrame({
            "Step": list(range(1, 9)),
            "Action": [
                "Identify all foreign currency cash flows (revenues, costs, dividends)",
                "Determine net FX exposure by currency after natural hedges",
                "Choose valuation approach (Approach 1 or 2 — both should agree)",
                "Calculate CIP forward rates for each year using current rates",
                "Add country risk premium for EM projects (Damodaran's database)",
                "For M&A: use options (not forwards) for contingent deal exposure",
                "Post-close: establish hedging policy for ongoing translation exposure",
                "Monitor effectiveness quarterly; adjust hedge ratios if needed"
            ],
            "Key Formula / Tool": [
                "Net = Inflows - Outflows per currency",
                "h* = rho × sigma_S/sigma_F (Module 8)",
                "NPV_Approach1 ≈ NPV_Approach2 if CIP holds",
                "F_t = S0 × [(1+r_d)/(1+r_f)]^t",
                "WACC_EM = Base + CRP + premiums",
                "FX Option — premium = cost of deal uncertainty insurance",
                "CCBS for long-term foreign currency debt (Module 5)",
                "IFRS 9: effectiveness 80-125% (Module 8)"
            ]
        })
        st.dataframe(checklist_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Using spot rate to convert ALL future foreign cash flows",
                "Hedging deal FX with a forward contract",
                "Ignoring the CCS basis when computing hedged bond returns",
                "Applying developed-market WACC to EM projects",
                "Treating currency overlay alpha as purely additive to asset returns"
            ],
            "Correct Approach": [
                "Use CIP forward rates for each year (or discount at local WACC first)",
                "Use FX options for contingent M&A exposure — forward creates a naked position if deal fails",
                "Hedged return = Foreign yield + (r_d - r_f) + CCS basis. Basis can meaningfully change the all-in cost",
                "Add CRP, illiquidity, and political risk premiums to the base WACC for EM projects",
                "Overlay alpha is net of its own costs (bid-ask, carry). Evaluate on a net basis vs benchmark"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 11 Complete! You can perform FX-adjusted DCF, analyse M&A FX hedging, compute hedged bond returns, and structure EM project WACC.")
        st.info("💡 Next: Module 12 — FX Regulation, Settlement & Emerging Topics (FX Global Code, CLS, MiFID II, CBDCs)")

if __name__ == "__main__":
    show()