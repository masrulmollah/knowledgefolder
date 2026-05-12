import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🔄 Module 5: FX Swaps & Cross-Currency Swaps")
    st.markdown("*Master FX swap mechanics, pricing, cross-currency basis, CCBS valuation, and treasury applications*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. What is an FX Swap?")
        st.markdown("""
        An **FX swap** is the simultaneous execution of a **spot transaction and a forward transaction**
        in the opposite direction for the **same notional amount** of base currency.

        | Component | Description |
        |-----------|-------------|
        | Near Leg | Spot transaction (today's settlement, T+2) |
        | Far Leg | Forward transaction in opposite direction |
        | Net FX Risk | Zero — same notional both legs |
        | Economic Effect | Borrow one currency, lend another for the swap period |

        **Two types:**
        - **Buy-Sell:** Buy base currency spot, sell base currency forward
          → Effectively borrowing foreign currency, lending domestic
        - **Sell-Buy:** Sell base currency spot, buy base currency forward
          → Effectively borrowing domestic currency, lending foreign
        """)

        st.subheader("2. Short-Dated Swap Tenors")
        st.markdown("""
        | Tenor | Description | Use Case |
        |-------|-------------|---------|
        | **O/N (Overnight)** | Today → Tomorrow | Intraday liquidity, missed settlements |
        | **T/N (Tom-Next)** | Tomorrow → Spot | Rolling spot positions, fixing value dates |
        | **S/N (Spot-Next)** | Spot → Next day | Extending spot positions one day |
        | **Spot-Week** | Spot → 1 week | Short-term currency funding |
        | **1M, 3M, 6M, 1Y** | Standard forward tenors | Liquidity management, hedging |

        **Swap points** for short-dated swaps follow the same interest differential logic as forward points.
        """)

        st.subheader("3. FX Swap Pricing")
        st.markdown("""
        The swap rate (far leg - near leg) is simply the forward points:
        ```
        Swap Points = F - S
                    = S x (i_d - i_f) x T/360  (approximation)
        ```

        **Exact formula:**
        ```
        Far Leg Rate = S x (1 + i_d x T/360) / (1 + i_f x T/360)
        Swap Points  = Far Leg Rate - Spot Rate
        ```

        The cost of the swap = the interest rate differential for the period.
        A company doing a Sell-Buy EUR/USD swap effectively borrows USD and lends EUR
        for the swap period at the interest differential.
        """)

        st.subheader("4. Cross-Currency Basis Swaps (CCBS)")
        st.markdown("""
        A **Cross-Currency Basis Swap** exchanges **floating rate payments in two currencies**
        plus the **principal at both start and end** of the swap.

        | Feature | FX Swap | Cross-Currency Basis Swap |
        |---------|---------|--------------------------|
        | Tenor | Typically < 1 year | 1 to 30 years |
        | Coupon exchange | No coupons | Floating coupons exchanged |
        | Principal | No re-exchange at market | Exchanged at same rate at start and end |
        | FX risk on principal | None (same rate both legs) | None (same rate both legs) |
        | Use | Short-term liquidity | Long-term currency funding |

        **Standard structure (USD/EUR example):**
        ```
        Party A pays: USD SOFR flat
        Party B pays: EUR €STR + Basis Spread
        Principal:    Exchanged at spot at start; re-exchanged at SAME rate at maturity
        ```
        """)

        st.subheader("5. The Cross-Currency Basis")
        st.markdown("""
        The **CIP basis** (or cross-currency basis) is the spread above/below fair value in the CCBS:
        ```
        Basis = Actual CCBS spread - CIP theoretical spread (which = 0)
        ```

        | Basis | Meaning |
        |-------|---------|
        | Negative (−20 to −80 bps for EUR/USD) | USD is in excess demand — borrowers pay extra for USD |
        | More negative | More dollar stress (e.g. COVID March 2020: −120 bps) |
        | Near zero | Normal market conditions |

        **Why does the basis persist post-2008?**
        - US money market funds withdrew from European bank paper
        - Non-US banks had USD funding shortfalls
        - Bank leverage ratio constraints prevent full arbitrage
        - The basis is now a widely-watched **USD funding stress indicator**
        """)

        st.subheader("6. CCBS Use Cases")
        st.markdown("""
        | User | Purpose |
        |------|---------|
        | European bank | Fund USD assets using EUR bonds → swap EUR to USD via CCBS |
        | US corporate issuing Eurobonds | Convert EUR proceeds to USD for US operations |
        | Japanese insurer | Buy US Treasuries → hedge USD back to JPY via CCBS |
        | Pension fund | Access foreign bonds without currency risk |

        **CCBS all-in cost comparison:**
        ```
        Direct USD funding: USD LIBOR/SOFR + credit spread (e.g. +80 bps)
        Via CCBS:           EUR bond yield + CCS spread + basis (e.g. +60 bps effective)
        → Choose CCBS if all-in cost is lower
        ```
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: FX Swap Pricing")
        st.markdown("""
        **Scenario:** Bank needs to fund a EUR 10M position for 3 months.
        EUR/USD spot = 1.0850; US 3M rate = 5.25%; EU 3M rate = 3.75%

        **Sell-Buy EUR/USD swap (sell EUR spot, buy EUR forward):**
        ```
        Near Leg (Spot):
          Sell EUR 10,000,000 at 1.0850 → Receive USD 10,850,000

        Far Leg (Forward):
          F = 1.0850 x (1 + 0.0525 x 90/360) / (1 + 0.0375 x 90/360)
            = 1.0850 x 1.013125 / 1.009375
            = 1.0890
          Buy EUR 10,000,000 at 1.0890 → Pay USD 10,890,000

        Swap Cost = USD 10,890,000 - USD 10,850,000 = USD 40,000 (= 40 swap points x 1M)
        Annualised Cost = USD 40,000 / USD 10,850,000 x 4 = 1.47% p.a.
        (This equals the interest rate differential: 5.25% - 3.75% = 1.50% approximately)
        ```
        """)

        st.subheader("Example 2: Cross-Currency Basis Swap — European Bank USD Funding")
        st.markdown("""
        **Scenario:** European bank needs USD 500M for 5 years. Two options:

        | Option | Details | All-in USD Cost |
        |--------|---------|----------------|
        | Direct USD issuance | USD 5Y bond at SOFR + 85 bps | **SOFR + 85 bps** |
        | CCBS route | Issue EUR 5Y bond at €STR + 50 bps, enter CCBS | **SOFR + 50 - Basis** |

        **CCBS Analysis (basis = −35 bps):**
        ```
        EUR bond issued:        Pay €STR + 50 bps
        CCBS: Pay €STR + basis  Pay €STR + (−35 bps) → Pay €STR − 35 bps
              Receive SOFR       Receive USD SOFR

        Net USD cost = €STR paid + 50 bps (bond) − €STR − 35 bps (CCBS) paid
                     = SOFR + 50 bps − (−35 bps) = SOFR + 50 + 35 = SOFR + 85 bps

        Wait... basis is NEGATIVE, meaning the bank RECEIVES extra basis:
        Correct calculation: SOFR + 50 bps − 35 bps = SOFR + 15 bps
        vs. Direct: SOFR + 85 bps → Savings: 70 bps x $500M = $3.5M/year!
        ```
        """)

        st.subheader("Example 3: CIP Basis Monitoring")
        st.markdown("""
        **EUR/USD 3-Month CCS Basis — Historical Observations:**

        | Period | Basis (bps) | Interpretation |
        |--------|------------|----------------|
        | Pre-GFC (2007) | ~0 | Normal — CIP held |
        | GFC Peak (Oct 2008) | −200 | Extreme USD shortage |
        | Post-GFC steady state (2012-2019) | −20 to −50 | Structural USD demand from non-US banks |
        | COVID-19 Peak (March 2020) | −120 | Acute dollar funding stress |
        | Post-COVID (2021-2023) | −15 to −30 | Elevated but stable |

        **Trading desk use:** Treasurers monitor basis as a real-time USD stress indicator.
        When basis widens suddenly (becomes more negative), it signals tightening dollar conditions —
        often preceding broader market stress.
        """)

        st.subheader("Example 4: T/N Swap for Position Rolling")
        st.markdown("""
        **Scenario:** FX desk has a EUR/USD spot long from yesterday that must be rolled to tomorrow.
        Spot = 1.0850; O/N interest differential = 1.5 bps per day

        ```
        T/N Swap (Tom-Next):
          Near Leg: SELL EUR spot at 1.0850 (close existing position)
          Far Leg:  BUY EUR tomorrow at 1.0850 + 0.00015 (T/N points = +0.15 pips)

        Cost of rolling: 0.15 pips per day x EUR 10M = USD 150 per day
        Annual carry cost: ~$54,750 (reflects 1.5% interest differential)
        ```
        This is how FX traders "roll" their spot positions overnight — the swap points
        reflect the daily cost or benefit of carrying the position.
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "🔄 FX Swap Pricing Calculator",
            "💼 CCBS All-in Cost Comparator",
            "📊 Swap Cost vs Direct Borrowing",
            "🌡️ CIP Basis Monitor"
        ])

        st.markdown("---")

        if calc_choice == "🔄 FX Swap Pricing Calculator":
            st.subheader("FX Swap Pricing Calculator")
            st.info("Calculate near leg, far leg, swap points, and all-in cost for an FX swap.")
            col1, col2 = st.columns(2)
            with col1:
                spot_sw = st.number_input("Spot Rate (S0)", value=1.0850, format="%.4f", step=0.0001)
                id_sw = st.number_input("Domestic (Quote) Rate % p.a.", value=5.25, step=0.05, key="sw_id")
                if_sw = st.number_input("Foreign (Base) Rate % p.a.", value=3.75, step=0.05, key="sw_if")
            with col2:
                tenor_sw = st.number_input("Swap Tenor (days)", value=90, step=1, min_value=1)
                notional_sw = st.number_input("Notional (base currency)", value=10000000.0, step=1000000.0)
                swap_type = st.radio("Swap Type", ["Buy-Sell (buy near, sell far)", "Sell-Buy (sell near, buy far)"])

            if st.button("Price the FX Swap", type="primary"):
                F_sw = spot_sw * (1 + id_sw / 100 * tenor_sw / 360) / (1 + if_sw / 100 * tenor_sw / 360)
                sw_pts = (F_sw - spot_sw) * 10000
                near_quote = notional_sw * spot_sw
                far_quote = notional_sw * F_sw
                swap_cost = abs(far_quote - near_quote)
                ann_cost_pct = (F_sw - spot_sw) / spot_sw * 360 / tenor_sw * 100

                st.markdown("---")
                if "Buy-Sell" in swap_type:
                    near_action = f"BUY {notional_sw:,.0f} base at {spot_sw:.4f} → PAY {near_quote:,.2f} quote"
                    far_action = f"SELL {notional_sw:,.0f} base at {F_sw:.4f} → RECEIVE {far_quote:,.2f} quote"
                    net = far_quote - near_quote
                else:
                    near_action = f"SELL {notional_sw:,.0f} base at {spot_sw:.4f} → RECEIVE {near_quote:,.2f} quote"
                    far_action = f"BUY {notional_sw:,.0f} base at {F_sw:.4f} → PAY {far_quote:,.2f} quote"
                    net = near_quote - far_quote

                st.markdown(f"""
                **FX Swap Pricing:**
                ```
                Near Leg (Spot, T+2):   {near_action}
                Far Leg (Forward, T+{tenor_sw}d): {far_action}
                ─────────────────────────────────────────────────────────
                Far Leg Rate:        {F_sw:.4f}
                Swap Points:         {sw_pts:+.1f} pips
                Net Quote Cash Flow: {net:+,.2f} quote currency
                Annualised Cost:     {ann_cost_pct:+.3f}% p.a.
                (≈ interest differential: {id_sw:.2f}% - {if_sw:.2f}% = {id_sw-if_sw:.2f}%)
                ```
                """)
                col1, col2, col3 = st.columns(3)
                col1.metric("Swap Points", f"{sw_pts:+.1f} pips")
                col2.metric("Far Leg Rate", f"{F_sw:.4f}")
                col3.metric("Annualised Cost", f"{ann_cost_pct:+.3f}%")

        elif calc_choice == "💼 CCBS All-in Cost Comparator":
            st.subheader("Cross-Currency Basis Swap — All-in Cost Comparator")
            st.info("Compare the all-in cost of direct USD issuance vs CCBS-routed EUR issuance.")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Direct USD Issuance:**")
                sofr = st.number_input("USD SOFR % p.a.", value=5.30, step=0.05)
                direct_spread = st.number_input("Credit Spread over SOFR (bps)", value=85.0, step=5.0)
                st.markdown("**EUR Bond Issuance:**")
                euribor = st.number_input("EUR €STR % p.a.", value=4.00, step=0.05)
                eur_spread = st.number_input("Credit Spread over €STR (bps)", value=50.0, step=5.0)
            with col2:
                st.markdown("**CCBS Terms:**")
                ccbs_basis = st.number_input("EUR/USD CCBS Basis (bps, enter negative)", value=-35.0, step=1.0)
                tenor_ccbs = st.number_input("Tenor (years)", value=5, step=1)
                notional_ccbs = st.number_input("Notional (USD millions)", value=500.0, step=50.0)

            if st.button("Compare Funding Options", type="primary"):
                direct_cost = sofr + direct_spread / 100
                eur_bond_cost_eur = euribor + eur_spread / 100
                ccbs_all_in_usd = sofr + eur_spread / 100 + ccbs_basis / 100
                savings_bps = direct_spread - eur_spread - ccbs_basis
                annual_savings = savings_bps / 10000 * notional_ccbs * 1_000_000
                total_savings = annual_savings * tenor_ccbs

                st.markdown("---")
                st.markdown(f"""
                **All-in Cost Comparison:**
                ```
                Option A — Direct USD Issuance:
                  SOFR {sofr:.2f}% + {direct_spread:.0f} bps = {direct_cost:.2f}% all-in USD cost

                Option B — EUR Bond + CCBS:
                  EUR bond:  €STR {euribor:.2f}% + {eur_spread:.0f} bps = {eur_bond_cost_eur:.2f}% EUR cost
                  CCBS:      Pay €STR + ({ccbs_basis:.0f} bps basis), Receive SOFR
                  Net USD cost = SOFR + {eur_spread:.0f} bps + ({ccbs_basis:.0f} bps basis)
                               = SOFR + {eur_spread + ccbs_basis:.0f} bps
                               = {ccbs_all_in_usd:.2f}% all-in USD cost

                Savings:  {savings_bps:.0f} bps = {savings_bps:.0f} bps/year
                Annual $: ${annual_savings:,.0f}
                Total ({tenor_ccbs}Y): ${total_savings:,.0f}
                ```
                """)
                col1, col2, col3 = st.columns(3)
                col1.metric("Direct USD Cost", f"{direct_cost:.2f}%")
                col2.metric("CCBS All-in USD Cost", f"{ccbs_all_in_usd:.2f}%")
                col3.metric("Savings", f"{savings_bps:.0f} bps", f"${annual_savings:,.0f}/yr")

                if ccbs_all_in_usd < direct_cost:
                    st.success(f"✅ CCBS route is CHEAPER by {savings_bps:.0f} bps. Total saving over {tenor_ccbs}Y: ${total_savings:,.0f}")
                else:
                    st.warning(f"⚠️ Direct USD issuance is cheaper by {-savings_bps:.0f} bps in this scenario.")

                fig = go.Figure(go.Bar(
                    x=["Direct USD Issuance", "CCBS Route (EUR + Swap)"],
                    y=[direct_cost, ccbs_all_in_usd],
                    marker_color=["#E74C3C", "#27AE60"],
                    text=[f"{direct_cost:.2f}%", f"{ccbs_all_in_usd:.2f}%"],
                    textposition='outside'
                ))
                fig.update_layout(title="All-in USD Funding Cost Comparison",
                                  yaxis_title="All-in USD Cost %",
                                  yaxis=dict(range=[0, max(direct_cost, ccbs_all_in_usd) * 1.3]))
                st.plotly_chart(fig, use_container_width=True)

        elif calc_choice == "📊 Swap Cost vs Direct Borrowing":
            st.subheader("FX Swap Cost vs Direct Borrowing Comparison")
            col1, col2 = st.columns(2)
            with col1:
                spot_comp = st.number_input("Spot Rate", value=1.0850, format="%.4f", key="comp_s")
                id_comp = st.number_input("Domestic Rate % p.a.", value=5.25, key="comp_id")
                if_comp = st.number_input("Foreign Rate % p.a.", value=3.75, key="comp_if")
            with col2:
                tenor_comp = st.slider("Tenor (days)", 7, 365, 90, key="comp_t")
                notional_comp = st.number_input("Notional (base)", value=10000000.0, step=1000000.0)

            F_comp = spot_comp * (1 + id_comp / 100 * tenor_comp / 360) / (1 + if_comp / 100 * tenor_comp / 360)
            sw_pts_comp = (F_comp - spot_comp) * 10000
            swap_ann_cost = (F_comp - spot_comp) / spot_comp * 360 / tenor_comp * 100
            direct_borrow_cost = id_comp

            tenors_range = list(range(7, 366, 7))
            swap_costs = [(spot_comp * (1 + id_comp/100 * t/360) / (1 + if_comp/100 * t/360) - spot_comp) / spot_comp * 360 / t * 100 for t in tenors_range]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=tenors_range, y=swap_costs, name='FX Swap Annualised Cost',
                line=dict(color='#2E86C1', width=2)))
            fig.add_hline(y=id_comp, line_dash='dash', line_color='#E74C3C',
                         annotation_text=f'Direct Borrow Rate {id_comp}%')
            fig.add_hline(y=if_comp, line_dash='dot', line_color='#27AE60',
                         annotation_text=f'Foreign Rate {if_comp}%')
            fig.update_layout(title='FX Swap Annualised Cost vs Direct Borrowing by Tenor',
                              xaxis_title='Tenor (days)', yaxis_title='Annualised Cost %')
            st.plotly_chart(fig, use_container_width=True)

            col1, col2, col3 = st.columns(3)
            col1.metric(f"Swap Cost ({tenor_comp}d annualised)", f"{swap_ann_cost:.3f}%")
            col2.metric("Direct Borrow Rate", f"{direct_borrow_cost:.2f}%")
            col3.metric("Swap Points", f"{sw_pts_comp:+.1f} pips")

        elif calc_choice == "🌡️ CIP Basis Monitor":
            st.subheader("CIP Basis Analyser")
            st.info("Input observed swap rates to calculate the implied CIP basis.")
            col1, col2 = st.columns(2)
            with col1:
                spot_b = st.number_input("EUR/USD Spot", value=1.0850, format="%.4f", key="basis_s")
                id_b = st.number_input("USD SOFR % p.a.", value=5.30, step=0.05, key="basis_id")
                if_b = st.number_input("EUR €STR % p.a.", value=4.00, step=0.05, key="basis_if")
            with col2:
                tenor_b = st.number_input("Tenor (days)", value=365, step=30, min_value=1, key="basis_t")
                actual_sw_pts = st.number_input("Observed Swap Points (from market)", value=155.0, step=0.5)

            F_cip_b = spot_b * (1 + id_b / 100 * tenor_b / 360) / (1 + if_b / 100 * tenor_b / 360)
            cip_sw_pts = (F_cip_b - spot_b) * 10000
            actual_fwd_b = spot_b + actual_sw_pts / 10000
            basis = (actual_fwd_b - F_cip_b) / F_cip_b * 10000

            st.markdown("---")
            st.markdown(f"""
            **CIP Basis Calculation:**
            ```
            CIP Fair Forward:       {F_cip_b:.4f}
            CIP Swap Points:        {cip_sw_pts:+.1f} pips
            Observed Swap Points:   {actual_sw_pts:+.1f} pips
            Actual Forward:         {actual_fwd_b:.4f}
            ─────────────────────────────────────────
            CIP Basis:              {basis:+.2f} bps
            ```
            """)
            col1, col2, col3 = st.columns(3)
            col1.metric("CIP Fair Forward", f"{F_cip_b:.4f}")
            col2.metric("Actual Forward", f"{actual_fwd_b:.4f}")
            col3.metric("CIP Basis", f"{basis:+.2f} bps")

            if basis < -50:
                st.error(f"🚨 Very negative basis ({basis:.1f} bps). Acute USD funding stress — similar to GFC or COVID conditions.")
            elif basis < -20:
                st.warning(f"⚠️ Negative basis ({basis:.1f} bps). USD in structural excess demand — watch for potential stress escalation.")
            elif abs(basis) < 5:
                st.success(f"✅ Near-zero basis ({basis:.1f} bps). Normal market conditions. CIP approximately holds.")
            else:
                st.info(f"ℹ️ Basis = {basis:.1f} bps. Monitor for trend.")

    with tab4:
        st.header("Visualizations")

        st.subheader("EUR/USD Cross-Currency Basis — Historical")
        years_v = list(range(2007, 2025))
        basis_hist = [0, -80, -60, -40, -30, -40, -50, -20, -15, -25, -30, -45, -20, -120, -25, -20, -30, -25]
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=years_v, y=basis_hist, fill='tozeroy',
            fillcolor='rgba(231,76,60,0.15)', line=dict(color='#E74C3C', width=2), name='EUR/USD Basis'))
        fig1.add_hline(y=0, line_color='black', line_dash='dash', annotation_text='CIP = 0')
        fig1.add_vrect(x0=2008, x1=2009, fillcolor='rgba(231,76,60,0.1)', line_width=0, annotation_text='GFC')
        fig1.add_vrect(x0=2020, x1=2020.5, fillcolor='rgba(231,76,60,0.1)', line_width=0, annotation_text='COVID')
        fig1.update_layout(title='EUR/USD 1Y Cross-Currency Basis (bps) — 2007 to 2024',
                           xaxis_title='Year', yaxis_title='Basis (bps)')
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("FX Swap vs Outright Forward — Volume Breakdown")
        instruments = ['FX Swaps', 'Spot', 'Outright Forwards', 'Currency Swaps (CCBS)', 'Options']
        vol_t = [3.8, 2.1, 1.1, 0.9, 0.3]
        fig2 = go.Figure(go.Pie(labels=instruments, values=vol_t, hole=0.35,
            marker=dict(colors=['#2E86C1', '#27AE60', '#F39C12', '#8E44AD', '#E74C3C'])))
        fig2.update_layout(title='Global FX Market — Daily Volume by Instrument ($T, BIS 2022)')
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Swap Points by Tenor — EUR/USD")
        spot_t = 1.0850; id_t = 5.25; if_t = 3.75
        tenors_td = [1, 7, 30, 90, 180, 365]
        tenors_tl = ['O/N', '1W', '1M', '3M', '6M', '1Y']
        sw_pts_t = [(spot_t * (1+id_t/100*t/360)/(1+if_t/100*t/360) - spot_t) * 10000 for t in tenors_td]
        fig3 = go.Figure(go.Bar(x=tenors_tl, y=sw_pts_t,
            marker_color='#2E86C1',
            text=[f'{p:+.2f}' for p in sw_pts_t], textposition='outside'))
        fig3.update_layout(title='EUR/USD Swap Points by Tenor (pips)',
                           xaxis_title='Tenor', yaxis_title='Swap Points (pips)')
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — FX Swaps & CCBS")

        st.markdown("**1. An FX swap consists of:**")
        q1 = st.radio("Select your answer:", [
            "Two forward contracts in the same direction",
            "A spot transaction plus a forward transaction in opposite directions for the same notional",
            "A forward contract plus an option",
            "Two spot transactions with different counterparties"
        ], key="fx5q1")
        if st.button("Check Answer", key="fx5c1"):
            if "spot transaction plus a forward" in q1:
                st.success("✅ Correct! FX swap = near leg (spot) + far leg (forward) in opposite directions, same notional. Net FX exposure = zero.")
            else:
                st.error("❌ Incorrect. An FX swap combines a spot deal and a forward deal in opposite directions for the same notional.")
        st.markdown("---")

        st.markdown("**2. A negative EUR/USD cross-currency basis means:**")
        q2 = st.radio("Select your answer:", [
            "The EUR is scarce in the market",
            "USD is in excess demand — borrowers pay more than CIP implies for USD via swaps",
            "EUR rates are lower than USD rates",
            "The EUR/USD spot rate is overvalued"
        ], key="fx5q2")
        if st.button("Check Answer", key="fx5c2"):
            if "USD is in excess demand" in q2:
                st.success("✅ Correct! Negative basis = USD at a premium — non-US borrowers pay extra above CIP to access USD via cross-currency swaps.")
            else:
                st.error("❌ Incorrect. Negative basis = USD in excess demand. Non-US entities pay above CIP to access USD funding via CCBS.")
        st.markdown("---")

        st.markdown("**3. In a Sell-Buy EUR/USD FX swap, the near leg involves:**")
        q3 = st.radio("Select your answer:", [
            "Buying EUR at the spot rate",
            "Selling EUR at the spot rate",
            "Selling USD at the forward rate",
            "There is no near leg in a Sell-Buy swap"
        ], key="fx5q3")
        if st.button("Check Answer", key="fx5c3"):
            if "Selling EUR at the spot rate" in q3:
                st.success("✅ Correct! Sell-Buy: SELL EUR spot (near leg), BUY EUR forward (far leg). Same notional, opposite directions.")
            else:
                st.error("❌ Incorrect. Sell-Buy: SELL base currency at spot (near leg), then BUY base currency at the forward rate (far leg).")
        st.markdown("---")

        st.markdown("**4. CCBS differs from a standard FX swap mainly because:**")
        q4 = st.radio("Select your answer:", [
            "CCBS involves no principal exchange",
            "CCBS exchanges floating interest coupons in two currencies and can be 1 to 30 years",
            "CCBS is exchange-traded on organised exchanges",
            "CCBS is only available for USD/JPY"
        ], key="fx5q4")
        if st.button("Check Answer", key="fx5c4"):
            if "floating interest coupons" in q4:
                st.success("✅ Correct! CCBS exchanges floating coupons in two currencies + principal at start and end. Tenors 1–30 years. FX swaps are typically short-dated.")
            else:
                st.error("❌ Incorrect. CCBS: floating coupon exchange + principal exchange at start and maturity. Can be 1–30 years — much longer than FX swaps.")
        st.markdown("---")

        st.markdown("**5. The FX swap cost of a Sell-Buy EUR/USD swap approximately equals:**")
        q5 = st.radio("Select your answer:", [
            "The EUR/USD spot rate",
            "The interest rate differential between USD and EUR rates",
            "The bid-ask spread only",
            "Zero — swaps are always costless"
        ], key="fx5q5")
        if st.button("Check Answer", key="fx5c5"):
            if "interest rate differential" in q5:
                st.success("✅ Correct! FX swap cost ≈ i_d − i_f for the period. Swap points reflect the interest differential — the cost of borrowing one currency vs the other.")
            else:
                st.error("❌ Incorrect. Swap points ≈ S × (i_d − i_f) × T/360. The cost of the swap equals the interest rate differential for the period.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")

        st.markdown("""
        ### 1. FX Swap Structure
        - Near leg (spot) + Far leg (forward) in **opposite directions**, same notional
        - Net FX exposure = zero (same amount of base currency both legs)
        - **Buy-Sell:** Buy spot, sell forward → borrow foreign, lend domestic
        - **Sell-Buy:** Sell spot, buy forward → borrow domestic, lend foreign

        ### 2. FX Swap Pricing
        ```
        Far Leg Rate = S0 x (1 + i_d x T/360) / (1 + i_f x T/360)
        Swap Points  = Far Leg Rate - Spot Rate
        Approximation: Swap Pts = S x (i_d - i_f) x T/360
        Annualised cost ≈ interest rate differential (i_d - i_f)
        ```

        ### 3. Cross-Currency Basis Swap (CCBS)
        - Tenor: 1 to 30 years (much longer than FX swaps)
        - Exchange floating coupons in two currencies + principal at start and maturity
        - Principal re-exchanged at the **same rate** → no FX risk on principal
        - Used for long-term cross-currency funding

        ### 4. The CIP Basis
        - Basis = deviation from CIP in the swap market
        - Negative basis = USD at a premium (excess USD demand)
        - Key indicator of dollar funding stress
        - EUR/USD basis: typically −15 to −50 bps in normal conditions
        - Spikes to −100 to −200 bps in severe stress (GFC, COVID)

        ### 5. Key Use Cases
        ```
        FX Swap:  Roll spot positions, short-term liquidity management
        CCBS:     Long-term cross-currency funding (EUR → USD, JPY → USD)
        Both:     Eliminate currency mismatch without permanent FX risk
        ```
        """)

        st.subheader("📌 Quick Reference")
        ref_df = pd.DataFrame({
            "Situation": [
                "Roll EUR/USD spot position overnight",
                "European bank needs 5Y USD funding",
                "Company wants 90-day USD from EUR cash",
                "Monitoring USD market stress",
                "EUR/USD swap pts = +40 for 90 days"
            ],
            "Instrument": ["T/N FX Swap", "CCBS (5Y)", "FX Swap (90-day)", "EUR/USD CCS Basis", "FX Swap far leg"],
            "Key Formula/Fact": [
                "Swap pts reflect daily interest differential",
                "Compare all-in USD cost vs direct USD bond",
                "Swap cost ≈ 1.47% p.a. (rate differential)",
                "Basis < −50 bps = elevated stress",
                "Far leg = 1.0850 + 0.0040 = 1.0890"
            ]
        })
        st.dataframe(ref_df, use_container_width=True, hide_index=True)

        st.success("🎓 **You've completed Module 5!** You understand FX swap mechanics, CCBS structure, and how to use them for liquidity management and cross-currency funding.")
        st.info("💡 **Next Steps**: Proceed to Module 6 — FX Options Foundations (Garman-Kohlhagen model and the Greeks).")

if __name__ == "__main__":
    show()