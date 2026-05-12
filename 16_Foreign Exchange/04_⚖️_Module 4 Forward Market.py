import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📅 Module 4: Forward Markets & Forward Rate Mathematics")
    st.markdown("*Price forward contracts, calculate forward points, understand CIA arbitrage, and apply corporate hedging*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. What is a Forward Contract?")
        st.markdown("""
        A **forward contract** is a binding agreement to exchange a specified amount of currency at a
        **specified rate (the forward rate)** on a **specified future date (the value date)**.

        | Feature | Detail |
        |---------|--------|
        | Obligatory | Both parties MUST perform — no choice |
        | OTC instrument | Fully customisable amount and maturity date |
        | Zero upfront cost | No premium paid (unlike options) |
        | Locks in rate | Eliminates FX uncertainty completely |
        | Also locks in upside | Cannot benefit if rates move in your favour |

        **Critical insight:** The forward rate is **NOT a forecast** of future spot rates.
        It is the **arbitrage-free price** derived entirely from today's spot and the interest differential.
        """)

        st.subheader("2. Forward Rate Formula")
        st.markdown("""
        Derived directly from Covered Interest Rate Parity (Module 3):
        ```
        F = S0 x (1 + i_d x T/360) / (1 + i_f x T/360)

        Where:
          F    = forward exchange rate (BASE/QUOTE)
          S0   = current spot rate
          i_d  = domestic (quote currency) interest rate, annualised
          i_f  = foreign (base currency) interest rate, annualised
          T    = number of days to maturity
        ```

        **For annual periods (simplified):**
        ```
        F = S0 x (1 + i_d) / (1 + i_f)
        ```

        **Forward Points** = (F - S0) x 10,000 for most pairs; x 100 for JPY pairs
        - Positive forward points → base currency at forward **PREMIUM** (i_d > i_f)
        - Negative forward points → base currency at forward **DISCOUNT** (i_d < i_f)
        """)

        st.subheader("3. Forward Premium and Discount")
        st.markdown("""
        ```
        Forward Premium/Discount (%) = (F - S0) / S0 x 360/T x 100
        ```

        | Condition | Term | Meaning |
        |-----------|------|---------|
        | F > S0 | Forward Premium | Base currency MORE expensive forward than spot |
        | F < S0 | Forward Discount | Base currency LESS expensive forward than spot |
        | F = S0 | At Par | Interest rates equal in both countries |

        **Example:** EUR/USD spot = 1.0850, 1Y forward = 1.1007
        ```
        Premium = (1.1007 - 1.0850) / 1.0850 x 100 = +1.45%
        EUR is at a 1.45% annual premium (US rates are higher than EU rates)
        ```
        """)

        st.subheader("4. Covered Interest Arbitrage (CIA)")
        st.markdown("""
        If the actual market forward ≠ the CIP fair forward, a **riskless profit** is possible.

        **Steps when F_actual > F_CIP:**
        ```
        Step 1: Borrow domestic currency at i_d for T days
        Step 2: Convert to foreign currency at spot rate S0
        Step 3: Invest at foreign rate i_f for T days
        Step 4: Sell foreign currency forward at F_actual (lock in the profit)
        Step 5: At maturity → collect foreign investment, convert at F_actual, repay domestic loan
        Profit = (F_actual - F_CIP) per unit of base currency (riskless!)
        ```

        Arbitrageurs eliminate deviations rapidly. Post-2008 exception: the **CIP basis** persists
        because bank balance sheet constraints prevent full arbitrage execution.
        """)

        st.subheader("5. Non-Deliverable Forwards (NDFs)")
        st.markdown("""
        **NDFs** are used for currencies where physical delivery is restricted or impossible:

        | Feature | Detail |
        |---------|--------|
        | Common currencies | CNY, INR, BRL, KRW, IDR, PHP, MYR |
        | Settlement | Cash in USD — no local currency changes hands |
        | Fixing | Based on official central bank or ISDA fixing rate |
        | Users | MNCs with EM currency exposure, hedge funds |

        ```
        NDF Settlement = (NDF Rate - Fixing Rate) / Fixing Rate x Notional (USD)

        Example: Sell USD 5M at NDF rate 7.35 CNY/USD
        At maturity, PBoC fixing = 7.28 (CNY appreciated)
        Settlement = (7.35 - 7.28) / 7.28 x $5,000,000 = $48,077 received
        ```
        """)

        st.subheader("6. Corporate Hedging with Forwards")
        st.markdown("""
        | Corporate Exposure | Risk | Hedge Action |
        |-------------------|------|-------------|
        | USD payable in 90 days (importer) | USD rises → pay more domestic | BUY USD forward |
        | USD receivable in 90 days (exporter) | USD falls → receive less domestic | SELL USD forward |
        | Foreign investment in USD assets | USD falls → lower domestic value | SELL USD forward |
        | USD debt service | USD rises → higher domestic cost | BUY USD forward |

        **Key trade-off:**
        - **Forwards** → certainty, no premium, but no upside
        - **Options** → protection + upside, but premium cost (see Module 6)
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Pricing a 90-Day Forward Rate")
        st.markdown("""
        **Given:** EUR/USD spot = 1.0850; US 90-day rate = 5.25% p.a.; EU 90-day rate = 3.75% p.a.

        **Step-by-step calculation:**
        ```
        F = 1.0850 x (1 + 0.0525 x 90/360) / (1 + 0.0375 x 90/360)
          = 1.0850 x (1 + 0.013125) / (1 + 0.009375)
          = 1.0850 x 1.013125 / 1.009375
          = 1.0850 x 1.003712
          = 1.0890

        Forward Points = (1.0890 - 1.0850) x 10,000 = +40 pips
        Forward Premium = (1.0890 - 1.0850) / 1.0850 x 100 = +0.37% for 90 days
                        = +1.47% annualised
        ```
        **Interpretation:** EUR is at a 40-pip forward premium. EUR/USD 90-day forward must be
        1.0890 by CIP or arbitrage will exploit the deviation.
        """)

        st.subheader("Example 2: Covered Interest Arbitrage")
        st.markdown("""
        **Setup:** EUR/USD spot = 1.0850; US rate = 5.25%; EU rate = 3.75%; 1Y
        CIP fair forward = **1.1007**. Suppose actual market forward = **1.1060** (overpriced by 53 pips).

        | Step | Action | Amount |
        |------|--------|--------|
        | 1 | Borrow USD at 5.25% for 1 year | $1,085,000 |
        | 2 | Convert to EUR at spot 1.0850 | EUR 1,000,000 |
        | 3 | Invest EUR at 3.75% for 1 year | EUR 1,037,500 |
        | 4 | Sell EUR 1,037,500 forward at 1.1060 | $1,147,475 |
        | 5 | Repay USD loan: $1,085,000 × 1.0525 | $1,141,963 |
        | **Profit** | **Riskless arbitrage profit** | **$5,512** |

        Arbitrageurs will keep exploiting this until the forward falls back to 1.1007.
        """)

        st.subheader("Example 3: Reading Forward Quotes from a Dealer Screen")
        st.markdown("""
        **EUR/USD dealer forward quote:**

        | Tenor | Spot | Fwd Points (bid/ask) | Outright Forward |
        |-------|------|---------------------|-----------------|
        | 1 Week | 1.0850 | +5 / +7 | 1.0855 / 1.0857 |
        | 1 Month | 1.0850 | +18 / +21 | 1.0868 / 1.0871 |
        | 3 Months | 1.0850 | +38 / +42 | 1.0888 / 1.0892 |
        | 6 Months | 1.0850 | +72 / +77 | 1.0922 / 1.0927 |
        | 1 Year | 1.0850 | +150 / +157 | 1.1000 / 1.1007 |

        **Rules for adding forward points:**
        - If bid fwd pts < ask fwd pts (e.g. +38/+42): ADD to spot (base at premium)
        - If bid fwd pts > ask fwd pts (e.g. -42/-38): SUBTRACT from spot (base at discount)
        """)

        st.subheader("Example 4: Corporate Forward Hedge — UK Exporter")
        st.markdown("""
        **Scenario:** UK exporter expects USD 5,000,000 from US client in 6 months.
        Current GBP/USD = 1.2700. 6M CIP forward = 1.2650 (GBP at premium, USD at discount).

        ```
        Without hedge: Wait 6 months and convert at market rate
          Best case if GBP/USD falls to 1.24:  USD 5M / 1.24 = GBP 4,032,258 (+)
          Base case (spot unchanged, 1.27):     USD 5M / 1.27 = GBP 3,937,008
          Worst case if GBP/USD rises to 1.32:  USD 5M / 1.32 = GBP 3,787,879 (-)

        With forward hedge at 1.2650:
          Locked-in receipt: USD 5M / 1.2650 = GBP 3,952,569 (CERTAIN)
          No matter what GBP/USD does in 6 months, GBP 3,952,569 is guaranteed.
        ```

        **Finance decision:** Treasurer locks in GBP 3,952,569. Budgets and plans with certainty.
        Misses the upside if GBP weakens, but eliminates downside risk entirely.
        """)

        st.subheader("Example 5: NDF Settlement — Hedging CNY Exposure")
        st.markdown("""
        **Scenario:** Singapore company will receive CNY 50,000,000 in 6 months.
        NDF rate (USD/CNY): 7.35. At maturity, PBoC fixing: 7.20 (CNY appreciated).

        ```
        NDF Settlement (company receives CNY, sells NDF):
        Settlement = (NDF Rate - Fixing) / Fixing x Notional
                   = (7.35 - 7.20) / 7.20 x ($50,000,000 / 7.35)
                   = 0.15 / 7.20 x $6,802,721
                   = 0.02083 x $6,802,721
                   = $141,724 received by the company

        Why company profits: CNY appreciated (fewer CNY per USD) vs the NDF hedge rate.
        The NDF compensates for the stronger CNY on the underlying exposure.
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "📅 Forward Rate Calculator",
            "🔍 Covered Interest Arbitrage Checker",
            "🏢 Corporate Hedge Analyser",
            "💱 NDF Settlement Calculator",
            "📊 Forward Curve Builder"
        ])

        st.markdown("---")

        if calc_choice == "📅 Forward Rate Calculator":
            st.subheader("Forward Rate Calculator")
            st.info("Calculate the CIP fair forward rate for any currency pair and tenor.")
            col1, col2 = st.columns(2)
            with col1:
                spot = st.number_input("Spot Rate (S0)", value=1.0850, format="%.4f", step=0.0001)
                i_d = st.number_input("Domestic (Quote) Rate % p.a.", value=5.25, step=0.05)
                i_f = st.number_input("Foreign (Base) Rate % p.a.", value=3.75, step=0.05)
            with col2:
                tenor = st.number_input("Tenor (days)", value=90, step=1, min_value=1, max_value=1825)
                notional = st.number_input("Notional (base currency units)", value=1000000.0, step=100000.0)
                direction = st.radio("Hedge Direction", ["BUY forward (importer)", "SELL forward (exporter)"])

            if st.button("Calculate Forward Rate", type="primary"):
                F = spot * (1 + i_d / 100 * tenor / 360) / (1 + i_f / 100 * tenor / 360)
                fwd_pts = (F - spot) * 10000
                prem_pct = (F - spot) / spot * 100
                ann_prem = prem_pct * 360 / tenor
                quote_notional = notional * F

                st.markdown("---")
                st.markdown(f"""
                **Forward Rate Calculation:**
                ```
                F = {spot:.4f} x (1 + {i_d:.2f}% x {tenor}/360)
                                 (1 + {i_f:.2f}% x {tenor}/360)

                  = {spot:.4f} x {1+i_d/100*tenor/360:.6f}
                                 {1+i_f/100*tenor/360:.6f}

                  = {F:.4f}

                Forward Points:        {fwd_pts:+.1f} pips
                Premium/Discount:      {prem_pct:+.3f}% ({tenor} days)
                Annualised Premium:    {ann_prem:+.3f}% p.a.
                ```
                """)
                col1, col2, col3 = st.columns(3)
                col1.metric("Forward Rate", f"{F:.4f}")
                col2.metric("Forward Points", f"{fwd_pts:+.1f} pips")
                col3.metric("Annualised Premium", f"{ann_prem:+.3f}%")

                st.markdown("---")
                st.markdown(f"### Hedge Details")
                if "BUY" in direction:
                    st.success(f"To BUY {notional:,.0f} base currency forward at {F:.4f}: you will PAY **{quote_notional:,.2f}** quote currency on value date ({tenor} days from today).")
                else:
                    st.success(f"To SELL {notional:,.0f} base currency forward at {F:.4f}: you will RECEIVE **{quote_notional:,.2f}** quote currency on value date ({tenor} days from today).")

        elif calc_choice == "🔍 Covered Interest Arbitrage Checker":
            st.subheader("Covered Interest Arbitrage Checker")
            st.info("Enter the actual market forward to check whether a CIA opportunity exists.")
            col1, col2 = st.columns(2)
            with col1:
                spot_cia = st.number_input("Spot Rate", value=1.0850, format="%.4f", key="cia_spot")
                id_cia = st.number_input("Domestic Rate % p.a.", value=5.25, step=0.05, key="cia_id")
                if_cia = st.number_input("Foreign Rate % p.a.", value=3.75, step=0.05, key="cia_if")
            with col2:
                tenor_cia = st.number_input("Tenor (days)", value=365, step=1, min_value=1, key="cia_t")
                actual_fwd = st.number_input("Actual Market Forward Rate", value=1.1007, format="%.4f", key="cia_act")
                invest_cia = st.number_input("Investment Amount (domestic)", value=1000000.0, step=100000.0, key="cia_inv")

            if st.button("Check for Arbitrage", type="primary"):
                F_cip = spot_cia * (1 + id_cia / 100 * tenor_cia / 360) / (1 + if_cia / 100 * tenor_cia / 360)
                deviation = actual_fwd - F_cip
                deviation_bps = deviation / F_cip * 10000
                foreign_invest = invest_cia / spot_cia
                foreign_maturity = foreign_invest * (1 + if_cia / 100 * tenor_cia / 360)
                converted_back = foreign_maturity * actual_fwd
                loan_repayment = invest_cia * (1 + id_cia / 100 * tenor_cia / 360)
                profit = converted_back - loan_repayment

                st.markdown("---")
                st.markdown(f"""
                **Arbitrage Analysis:**
                ```
                CIP Fair Forward:       {F_cip:.4f}
                Actual Market Forward:  {actual_fwd:.4f}
                Deviation:              {deviation*10000:+.1f} pips ({deviation_bps:+.2f} bps)
                ─────────────────────────────────────────────────
                CIA Steps:
                1. Borrow {invest_cia:,.0f} domestic at {id_cia:.2f}%
                2. Convert to {foreign_invest:,.2f} foreign at {spot_cia:.4f}
                3. Invest {foreign_invest:,.2f} foreign at {if_cia:.2f}% → {foreign_maturity:,.2f}
                4. Sell {foreign_maturity:,.2f} forward at {actual_fwd:.4f} → {converted_back:,.2f}
                5. Repay loan: {loan_repayment:,.2f}
                ─────────────────────────────────────────────────
                Riskless Profit:        {profit:+,.2f} domestic currency
                ```
                """)
                col1, col2, col3 = st.columns(3)
                col1.metric("CIP Fair Forward", f"{F_cip:.4f}")
                col2.metric("Deviation", f"{deviation_bps:+.2f} bps")
                col3.metric("Arbitrage Profit", f"{profit:+,.2f}")

                if abs(deviation_bps) < 2:
                    st.success("✅ CIP holds — no significant arbitrage opportunity (< 2 bps deviation).")
                elif deviation > 0:
                    st.warning(f"⚠️ Forward OVERPRICED by {deviation_bps:.1f} bps. CIA: Borrow domestic → Invest foreign → Sell overpriced forward. Profit: {profit:,.2f}")
                else:
                    st.warning(f"⚠️ Forward UNDERPRICED by {abs(deviation_bps):.1f} bps. CIA: Borrow foreign → Invest domestic → Buy underpriced forward. Profit: {profit:,.2f}")

        elif calc_choice == "🏢 Corporate Hedge Analyser":
            st.subheader("Corporate Forward Hedge Analyser")
            st.info("Compare hedged vs unhedged outcomes across a range of market scenarios.")
            col1, col2 = st.columns(2)
            with col1:
                exposure_type = st.radio("Exposure Type", [
                    "Exporter (will RECEIVE foreign currency)",
                    "Importer (will PAY foreign currency)"
                ])
                notional_h = st.number_input("Notional (foreign currency)", value=1000000.0, step=100000.0)
                spot_h = st.number_input("Current Spot Rate", value=1.2700, format="%.4f")
            with col2:
                fwd_h = st.number_input("Forward Rate Available", value=1.2650, format="%.4f")
                tenor_h = st.number_input("Tenor (days)", value=180, step=1)
                option_cost_pct = st.number_input("Option Hedge Cost (% of notional, for comparison)", value=1.5, step=0.1)

            if st.button("Analyse Hedge", type="primary"):
                scenario_moves = [-8, -6, -4, -2, 0, 2, 4, 6, 8]
                scenario_rates = [spot_h * (1 + m / 100) for m in scenario_moves]
                scenario_labels = [f"{m:+d}%" for m in scenario_moves]

                if "Exporter" in exposure_type:
                    unhedged = [notional_h / r for r in scenario_rates]
                    hedged = [notional_h / fwd_h] * len(scenario_rates)
                    option_hedge = [max(notional_h / r, notional_h / fwd_h) * (1 - option_cost_pct / 100) for r in scenario_rates]
                    ylabel = "Domestic Currency Received"
                    locked = notional_h / fwd_h
                else:
                    unhedged = [notional_h * r for r in scenario_rates]
                    hedged = [notional_h * fwd_h] * len(scenario_rates)
                    option_hedge = [min(notional_h * r, notional_h * fwd_h) * (1 + option_cost_pct / 100) for r in scenario_rates]
                    ylabel = "Domestic Currency Paid"
                    locked = notional_h * fwd_h

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=scenario_labels, y=unhedged, name="Unhedged",
                    line=dict(color='#E74C3C', width=2, dash='dot'), mode='lines+markers'))
                fig.add_trace(go.Scatter(x=scenario_labels, y=hedged, name="Forward Hedge",
                    line=dict(color='#27AE60', width=2.5), mode='lines+markers'))
                fig.add_trace(go.Scatter(x=scenario_labels, y=option_hedge, name="Option Hedge (approx.)",
                    line=dict(color='#F39C12', width=2, dash='dash'), mode='lines+markers'))
                fig.update_layout(title='Hedged vs Unhedged — Scenario Analysis',
                                  xaxis_title='Spot Rate Move from Today',
                                  yaxis_title=ylabel, legend=dict(x=0.01, y=0.99))
                st.plotly_chart(fig, use_container_width=True)

                st.metric("Forward Hedge — Locked-in Amount", f"{locked:,.2f} domestic currency")
                results_df = pd.DataFrame({
                    "Scenario": scenario_labels,
                    "Market Rate": [f"{r:.4f}" for r in scenario_rates],
                    "Unhedged": [f"{v:,.0f}" for v in unhedged],
                    "Forward Hedge": [f"{v:,.0f}" for v in hedged],
                    "vs Unhedged": [f"{h-u:+,.0f}" for h, u in zip(hedged, unhedged)]
                })
                st.dataframe(results_df, use_container_width=True, hide_index=True)

        elif calc_choice == "💱 NDF Settlement Calculator":
            st.subheader("NDF Settlement Calculator")
            st.info("Calculate the USD cash settlement amount for a Non-Deliverable Forward.")
            col1, col2 = st.columns(2)
            with col1:
                ndf_rate = st.number_input("NDF Contracted Rate (local/USD)", value=7.35, format="%.4f", step=0.01)
                notional_usd = st.number_input("Notional Amount (USD)", value=5000000.0, step=100000.0)
                position = st.radio("Your NDF Position", ["BUY USD (you pay USD at NDF rate)", "SELL USD (you receive USD at NDF rate)"])
            with col2:
                fixing_rate = st.number_input("Fixing Rate at Maturity (local/USD)", value=7.28, format="%.4f", step=0.01)
                currency_name = st.text_input("Local Currency Name", value="CNY")

            if st.button("Calculate NDF Settlement", type="primary"):
                settlement_pct = (ndf_rate - fixing_rate) / fixing_rate
                settlement_usd = settlement_pct * notional_usd

                if "SELL USD" in position:
                    net_settlement = settlement_usd
                else:
                    net_settlement = -settlement_usd

                st.markdown("---")
                st.markdown(f"""
                **NDF Settlement Calculation:**
                ```
                NDF Rate:      {ndf_rate:.4f} {currency_name}/USD
                Fixing Rate:   {fixing_rate:.4f} {currency_name}/USD
                Notional:      USD {notional_usd:,.0f}

                Settlement % = (NDF Rate - Fixing Rate) / Fixing Rate
                             = ({ndf_rate:.4f} - {fixing_rate:.4f}) / {fixing_rate:.4f}
                             = {settlement_pct*100:+.4f}%

                Gross Settlement = {settlement_pct*100:+.4f}% x USD {notional_usd:,.0f}
                                 = USD {settlement_usd:+,.2f}

                Your Settlement (as {position.split('(')[0].strip()}):
                             = USD {net_settlement:+,.2f}
                ```
                """)
                col1, col2, col3 = st.columns(3)
                col1.metric("NDF Rate", f"{ndf_rate:.4f}")
                col2.metric("Fixing Rate", f"{fixing_rate:.4f}")
                col3.metric("Your Settlement", f"USD {net_settlement:+,.2f}",
                           delta_color="normal" if net_settlement > 0 else "inverse")

                if net_settlement > 0:
                    st.success(f"✅ You RECEIVE USD {abs(net_settlement):,.2f} — the {currency_name} {'appreciated' if ndf_rate > fixing_rate else 'depreciated'} vs your hedge rate.")
                elif net_settlement < 0:
                    st.error(f"❌ You PAY USD {abs(net_settlement):,.2f} — the {currency_name} {'depreciated' if ndf_rate > fixing_rate else 'appreciated'} vs your hedge rate.")
                else:
                    st.info("Settlement = 0 — NDF rate exactly equals fixing rate.")

        elif calc_choice == "📊 Forward Curve Builder":
            st.subheader("Forward Curve Builder")
            st.info("Build and visualise the full forward curve for any currency pair.")
            col1, col2 = st.columns(2)
            with col1:
                spot_fc = st.number_input("Spot Rate", value=1.0850, format="%.4f", key="fc_spot")
                id_fc = st.number_input("Domestic Rate % p.a.", value=5.25, step=0.05, key="fc_id")
            with col2:
                if_fc = st.number_input("Foreign Rate % p.a.", value=3.75, step=0.05, key="fc_if")
                base_ccy = st.text_input("Pair Label (e.g. EUR/USD)", value="EUR/USD")

            tenors_days = [1, 7, 14, 30, 60, 90, 120, 180, 270, 365, 548, 730]
            tenors_labels = ['O/N', '1W', '2W', '1M', '2M', '3M', '4M', '6M', '9M', '1Y', '18M', '2Y']
            fwd_rates_fc = [spot_fc * (1 + id_fc/100 * t/360) / (1 + if_fc/100 * t/360) for t in tenors_days]
            fwd_pts_fc = [(f - spot_fc) * 10000 for f in fwd_rates_fc]

            fig1 = go.Figure()
            fig1.add_hline(y=spot_fc, line_dash='dash', line_color='gray',
                          annotation_text=f'Spot {spot_fc:.4f}', annotation_position='bottom right')
            fig1.add_trace(go.Scatter(x=tenors_labels, y=fwd_rates_fc,
                mode='lines+markers', line=dict(color='#2E86C1', width=2.5),
                marker=dict(size=8), name='Forward Rate'))
            fig1.update_layout(title=f'{base_ccy} Forward Curve',
                               xaxis_title='Tenor', yaxis_title='Forward Rate')
            st.plotly_chart(fig1, use_container_width=True)

            fig2 = go.Figure(go.Bar(x=tenors_labels, y=fwd_pts_fc,
                marker_color=['#27AE60' if p > 0 else '#E74C3C' for p in fwd_pts_fc],
                text=[f'{p:+.1f}' for p in fwd_pts_fc], textposition='outside'))
            fig2.update_layout(title=f'{base_ccy} Forward Points by Tenor',
                               xaxis_title='Tenor', yaxis_title='Forward Points (pips)')
            st.plotly_chart(fig2, use_container_width=True)

            curve_df = pd.DataFrame({
                "Tenor": tenors_labels, "Days": tenors_days,
                "Forward Rate": [f"{f:.4f}" for f in fwd_rates_fc],
                "Forward Points": [f"{p:+.1f}" for p in fwd_pts_fc],
                "Premium/Discount %": [f"{(f-spot_fc)/spot_fc*100:+.3f}%" for f in fwd_rates_fc]
            })
            st.dataframe(curve_df, use_container_width=True, hide_index=True)

    with tab4:
        st.header("Visualizations")

        st.subheader("EUR/USD Forward Curve — Current Rate Environment")
        spot_vis = 1.0850; id_vis = 5.25; if_vis = 3.75
        tenors_d = [7, 30, 60, 90, 180, 270, 365]
        tenors_l = ['1W', '1M', '2M', '3M', '6M', '9M', '1Y']
        fwd_rates = [spot_vis * (1 + id_vis/100 * t/360) / (1 + if_vis/100 * t/360) for t in tenors_d]
        fwd_pts = [(f - spot_vis) * 10000 for f in fwd_rates]

        col1, col2 = st.columns(2)
        with col1:
            fig1 = go.Figure()
            fig1.add_hline(y=spot_vis, line_dash='dash', annotation_text=f'Spot {spot_vis}')
            fig1.add_trace(go.Scatter(x=tenors_l, y=fwd_rates, mode='lines+markers',
                line=dict(color='#27AE60', width=2.5), marker=dict(size=8)))
            fig1.update_layout(title='EUR/USD Forward Curve', xaxis_title='Tenor', yaxis_title='Rate')
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            fig2 = go.Figure(go.Bar(x=tenors_l, y=fwd_pts,
                marker_color=['#27AE60' if p > 0 else '#E74C3C' for p in fwd_pts],
                text=[f'{p:+.1f}' for p in fwd_pts], textposition='outside'))
            fig2.update_layout(title='Forward Points by Tenor (pips)', xaxis_title='Tenor', yaxis_title='Pips')
            st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Hedged vs Unhedged — Exporter Outcome Comparison")
        fwd_rate_vis = 1.0890
        spot_scenarios = [1.04, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1.12, 1.14]
        unhedged_vis = [1000000 / s for s in spot_scenarios]
        hedged_vis = [1000000 / fwd_rate_vis] * len(spot_scenarios)

        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=spot_scenarios, y=unhedged_vis, name='Unhedged',
            line=dict(color='#E74C3C', width=2, dash='dot'), mode='lines+markers'))
        fig3.add_trace(go.Scatter(x=spot_scenarios, y=hedged_vis, name=f'Forward Hedge @ {fwd_rate_vis}',
            line=dict(color='#27AE60', width=2.5), mode='lines'))
        fig3.update_layout(title='Exporter: EUR Proceeds from USD 1M (Hedged vs Unhedged)',
                           xaxis_title='EUR/USD Market Rate at Maturity', yaxis_title='EUR Proceeds')
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — Forward Markets")

        st.markdown("**1. The forward rate is best described as:**")
        q1 = st.radio("Select your answer:", [
            "A prediction of where the spot rate will be at maturity",
            "The arbitrage-free rate derived from spot and the interest differential (CIP)",
            "The central bank's target exchange rate",
            "A weighted average of past spot rates"
        ], key="fx4q1")
        if st.button("Check Answer", key="fx4c1"):
            if "arbitrage-free" in q1:
                st.success("✅ Correct! The forward rate is entirely determined by spot and the interest differential via CIP. It is NOT a forecast.")
            else:
                st.error("❌ Incorrect. The forward rate is the CIP arbitrage-free price. It tells us nothing about where spot will actually be.")
        st.markdown("---")

        st.markdown("**2. EUR/USD spot = 1.0850, US rate = 5%, EU rate = 3%, 180-day forward. F ≈ ?**")
        q2 = st.radio("Select your answer:", ["1.0850", "1.0957", "1.0741", "1.1200"], key="fx4q2")
        if st.button("Check Answer", key="fx4c2"):
            if q2 == "1.0957":
                st.success("✅ Correct! F = 1.0850 × (1+0.05×0.5)/(1+0.03×0.5) = 1.0850 × 1.025/1.015 = 1.0957.")
            else:
                st.error("❌ Incorrect. F = 1.0850 × (1+0.05×180/360)/(1+0.03×180/360) = 1.0850 × 1.025/1.015 ≈ 1.0957.")
        st.markdown("---")

        st.markdown("**3. Forward points of +150 means the forward rate is:**")
        q3 = st.radio("Select your answer:", [
            "150 pips BELOW the spot rate",
            "150 pips ABOVE the spot rate",
            "Equal to the spot rate",
            "The spread is 150 pips"
        ], key="fx4q3")
        if st.button("Check Answer", key="fx4c3"):
            if "ABOVE" in q3:
                st.success("✅ Correct! Positive forward points ADD to spot. +150 pips means Forward = Spot + 0.0150.")
            else:
                st.error("❌ Incorrect. Positive forward points are added to spot. +150 pips means Forward = Spot + 0.0150.")
        st.markdown("---")

        st.markdown("**4. A UK exporter expecting USD receipts in 3 months should:**")
        q4 = st.radio("Select your answer:", [
            "Buy USD forward to lock in the rate",
            "Sell USD forward to lock in the GBP/USD conversion rate",
            "Do nothing and wait for a better rate",
            "Buy USD put options only"
        ], key="fx4q4")
        if st.button("Check Answer", key="fx4c4"):
            if "Sell USD forward" in q4:
                st.success("✅ Correct! The exporter will RECEIVE USD → SELL USD forward to lock in the GBP/USD rate for conversion.")
            else:
                st.error("❌ Incorrect. Exporter receives USD and wants GBP → SELL USD forward (buy GBP forward) to lock in the rate.")
        st.markdown("---")

        st.markdown("**5. NDFs (Non-Deliverable Forwards) settle in:**")
        q5 = st.radio("Select your answer:", [
            "The local restricted currency only",
            "A convertible currency (usually USD) — no local currency changes hands",
            "Gold or commodities",
            "Both currencies simultaneously via CLS"
        ], key="fx4q5")
        if st.button("Check Answer", key="fx4c5"):
            if "convertible currency" in q5:
                st.success("✅ Correct! NDFs settle in USD (or another convertible currency). Used for CNY, INR, BRL, KRW where physical delivery is restricted.")
            else:
                st.error("❌ Incorrect. NDFs settle in USD — no local currency changes hands. Used for currencies with exchange controls.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")

        st.markdown("""
        ### 1. Forward Contract Fundamentals
        - Binding agreement to exchange currency at a fixed rate on a future date
        - OTC instrument — fully customisable amount and tenor
        - No upfront premium (unlike options) but obligatory
        - The forward rate is the **CIP arbitrage-free price** — NOT a forecast

        ### 2. Forward Rate Formula
        ```
        F = S0 x (1 + i_d x T/360) / (1 + i_f x T/360)

        Forward Points = (F - S0) x 10,000
        Positive points = base currency at PREMIUM (i_d > i_f)
        Negative points = base currency at DISCOUNT (i_d < i_f)
        ```

        ### 3. Forward Premium/Discount
        ```
        Premium/Discount % = (F - S0) / S0 x 360/T x 100
        ```

        ### 4. Covered Interest Arbitrage (CIA)
        - If F_actual ≠ F_CIP → riskless profit opportunity
        - Steps: Borrow domestic → Convert to foreign → Invest → Lock in forward
        - Arbitrageurs close deviations rapidly
        - Post-2008 CIP basis persists due to balance sheet constraints (not free profit)

        ### 5. NDF Settlement
        ```
        Settlement = (NDF Rate - Fixing Rate) / Fixing Rate x Notional (USD)
        Used for: CNY, INR, BRL, KRW, IDR — currencies with capital controls
        ```

        ### 6. Corporate Hedging Rules
        ```
        Importer (will PAY foreign currency)    → BUY forward
        Exporter (will RECEIVE foreign currency) → SELL forward
        ```

        ### Key Formulas Summary
        ```
        Forward Rate:        F = S0 x (1 + i_d x T/360) / (1 + i_f x T/360)
        Forward Points:      (F - S0) x 10,000
        Premium/Discount %:  (F - S0) / S0 x 360/T x 100
        NDF Settlement:      (NDF Rate - Fixing) / Fixing x Notional
        CIA Profit:          (F_actual - F_CIP) x Foreign Maturity Proceeds
        ```
        """)

        st.subheader("📌 Quick Reference")
        ref_df = pd.DataFrame({
            "Scenario": [
                "Price a 90-day EUR/USD forward",
                "Check if CIA opportunity exists",
                "UK company has USD receivable in 6M",
                "Hedge CNY exposure (restricted currency)",
                "EUR/USD fwd pts = +150, spot = 1.0850"
            ],
            "Action": [
                "Use F = S × (1+id×90/360)/(1+if×90/360)",
                "Compare F_actual vs F_CIP. If different → CIA steps",
                "SELL USD forward to lock in GBP/USD rate",
                "Use NDF — cash settled in USD at fixing rate",
                "Outright forward = 1.0850 + 0.0150 = 1.1000"
            ]
        })
        st.dataframe(ref_df, use_container_width=True, hide_index=True)

        st.success("🎓 **You've completed Module 4!** You can price any forward contract, detect CIA opportunities, and apply forward hedging to real corporate exposures.")
        st.info("💡 **Next Steps**: Proceed to Module 5 — FX Swaps & Cross-Currency Swaps.")

if __name__ == "__main__":
    show()