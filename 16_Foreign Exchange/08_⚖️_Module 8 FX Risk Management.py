import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from scipy.stats import norm

def show():
    st.title("🛡️ Module 8: FX Risk Management")
    st.markdown("*Master transaction, translation and economic exposure, VaR, hedge ratios, stress testing, and IFRS 9 hedge accounting*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. The Three Types of FX Exposure")
        st.markdown("""
        Every company with international operations faces three distinct categories of FX risk:
        """)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            #### Transaction Exposure
            - Risk on **already-contracted** future foreign currency cash flows
            - Most **immediate and direct** form of FX risk
            - Clearly defined — easy to quantify and hedge
            - **Examples:** Foreign currency invoice receivable in 90 days; USD bond coupon payment
            - **Managed by:** Forwards, options, money market hedges
            """)
        with col2:
            st.markdown("""
            #### Translation Exposure
            - Risk when converting **foreign subsidiary** financials to parent's reporting currency at period end
            - Affects the balance sheet and reported equity
            - Does not directly impact cash flows
            - **Examples:** Revaluing a EUR-denominated subsidiary in USD accounts
            - **Managed by:** Balance sheet matching; cross-currency swaps
            """)
        with col3:
            st.markdown("""
            #### Economic (Operating) Exposure
            - Long-term risk to **competitive position**, future uncontracted cash flows, and firm value
            - Hardest to measure and hedge — affects strategy
            - **Examples:** Toyota building US plants to match USD revenues with USD costs (natural hedge)
            - **Managed by:** Operational decisions, diversification, invoice currency choice
            """)

        st.subheader("2. Natural Hedging")
        st.markdown("""
        **Natural hedging** reduces FX exposure through operational decisions rather than financial instruments:
        ```
        Natural Hedge Examples:
        ├── Match revenue and cost currencies (earn USD, pay USD suppliers)
        ├── Produce in export markets (costs in same currency as revenues)
        ├── Invoice foreign customers in your home currency
        ├── Borrow in the currency of your foreign assets
        └── Diversify across multiple currencies (portfolio effect)

        Net Exposure = Gross Inflows (foreign) - Gross Outflows (foreign)
        Only hedge the NET residual exposure after natural hedges
        ```
        """)

        st.subheader("3. Value at Risk (VaR)")
        st.markdown("""
        **VaR** is the maximum expected loss over a given time horizon at a specified confidence level.

        ```
        Parametric (Variance-Covariance) VaR:
        VaR = Position Value x sigma_daily x Z x sqrt(T)

        Where:
          sigma_daily = daily return standard deviation
          Z           = confidence level z-score (99% = 2.326; 95% = 1.645)
          T           = holding period in days
        ```

        | VaR Method | Approach | Pros | Cons |
        |-----------|---------|------|------|
        | **Parametric** | Normal distribution assumption | Simple, fast | Assumes normality; underestimates tail risk |
        | **Historical** | Uses actual past returns | No distribution assumption | Backward-looking |
        | **Monte Carlo** | Simulates thousands of scenarios | Most flexible | Computationally intensive |

        **Key limitation:** VaR says nothing about losses BEYOND the confidence threshold.
        Use **Expected Shortfall (ES / CVaR)** for tail risk.
        """)

        st.subheader("4. Minimum Variance Hedge Ratio")
        st.markdown("""
        The **optimal hedge ratio** minimises the variance of the hedged position:
        ```
        h* = rho x (sigma_S / sigma_F)

        Where:
          rho     = correlation between spot and hedge instrument returns
          sigma_S = standard deviation of spot position returns
          sigma_F = standard deviation of forward/futures returns

        Hedge Notional = h* x Exposure Notional
        ```
        **Key insight:** h* < 1 when the hedge instrument is more volatile than the spot.
        Over-hedging (h > h*) or under-hedging (h < h*) both increase total risk.
        """)

        st.subheader("5. Hedge Effectiveness")
        st.markdown("""
        **Hedge effectiveness** measures how well the hedge offsets the hedged item's fair value changes.
        Required under IFRS 9 for hedge accounting qualification.

        ```
        Effectiveness = |Change in Fair Value of Hedge| / |Change in Fair Value of Hedged Item|

        IFRS 9 requires: 80% <= Effectiveness <= 125%
        Below 80% or above 125% → Hedge accounting NOT permitted
        ```

        **Three hedge types under IFRS 9:**
        | Type | Hedges | Gain/Loss Treatment |
        |------|--------|-------------------|
        | **Fair Value Hedge** | Fair value of recognised asset/liability | P&L immediately |
        | **Cash Flow Hedge** | Variability in future cash flows | OCI until hedged item affects P&L |
        | **Net Investment Hedge** | Foreign subsidiary net assets | OCI until disposal |
        """)

        st.subheader("6. Stress Testing & Scenario Analysis")
        st.markdown("""
        VaR has limitations (assumes normality, historical window). **Stress testing** complements VaR:
        ```
        Historical Stress Scenarios:
          GFC 2008:     EUR/USD fell 20% in 6 months
          COVID-19:     USD/JPY fell 10% in 2 weeks
          GBP/USD flash crash (Oct 2016): fell 6% in 2 minutes
          Asian crisis 1997: THB/USD fell 50% in months

        Hypothetical Scenarios:
          Disorderly USD appreciation of 15%
          EM currency basket depreciation of 25%
          Simultaneous volatility spike across all pairs
        ```
        Stress testing reveals losses that VaR's normality assumption would massively understate.
        """)

    # ══════════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Identifying and Quantifying Net FX Exposure")
        st.markdown("""
        **Scenario:** UK multinational with USD operations. Annual figures:

        | USD Cash Flow | Amount |
        |--------------|--------|
        | USD revenues from US sales | +USD 25,000,000 |
        | USD raw material costs | -USD 8,000,000 |
        | USD manufacturing overhead (US plant) | -USD 4,500,000 |
        | USD interest payments on USD bond | -USD 1,200,000 |
        | USD dividends received from US subsidiary | +USD 2,000,000 |

        ```
        Gross USD Inflows:   $25M + $2M = $27,000,000
        Gross USD Outflows:  $8M + $4.5M + $1.2M = $13,700,000
        ────────────────────────────────────────────────────────
        Net USD Exposure:    $27M - $13.7M = $13,300,000 (net long USD)

        GBP/USD = 1.2700 → Net GBP exposure at risk = GBP 10,472,441

        If GBP/USD rises 5% (GBP strengthens, USD weakens):
        GBP loss = GBP 10,472,441 x 5% = GBP 523,622
        ```
        Only hedge the NET $13.3M — not the gross flows — to avoid over-hedging.
        """)

        st.subheader("Example 2: Parametric VaR Calculation")
        st.markdown("""
        **Portfolio:** EUR 5,000,000 long EUR/USD position. EUR/USD daily vol = 0.60%.

        ```
        Step 1: Convert to USD base
          Position Value = EUR 5,000,000 x 1.0850 = USD 5,425,000

        Step 2: Calculate 1-day 99% VaR
          VaR = USD 5,425,000 x 0.60% x 2.326 x sqrt(1)
              = USD 5,425,000 x 0.006 x 2.326
              = USD 5,425,000 x 0.013956
              = USD 75,716

        Interpretation: 99% confident that the 1-day loss will NOT exceed USD 75,716.
        1% chance of losing MORE than USD 75,716 in a single day.

        Step 3: Scale to 10-day 99% VaR (Basel minimum)
          VaR_10d = USD 75,716 x sqrt(10) = USD 75,716 x 3.162 = USD 239,366
        ```
        """)

        st.subheader("Example 3: Minimum Variance Hedge Ratio")
        st.markdown("""
        **Scenario:** GBP exporter hedging USD 10M receivable using USD/GBP forwards.

        ```
        Given:
          rho (correlation, USD/GBP spot vs forward) = 0.97
          sigma_S (daily vol of spot)    = 0.65%
          sigma_F (daily vol of forward) = 0.63%

        Optimal Hedge Ratio:
          h* = rho x (sigma_S / sigma_F)
             = 0.97 x (0.65% / 0.63%)
             = 0.97 x 1.0317
             = 1.0008 ≈ 1.00

        Hedge Notional = h* x USD 10,000,000 = USD 10,000,000 (hedge 100%)

        Explanation: When forward closely tracks spot (high rho, similar vol),
        the optimal hedge ratio is close to 1.0 — hedge the full notional.
        ```
        """)

        st.subheader("Example 4: IFRS 9 Cash Flow Hedge — Documentation")
        st.markdown("""
        **Highly Probable Forecast Transaction:** UK company expects to receive USD 5M in 6 months.
        Enters EUR/USD forward to lock in GBP proceeds.

        ```
        Hedge Documentation Required:
        ─────────────────────────────────────────────────────
        Hedging Relationship:     Cash Flow Hedge
        Risk Being Hedged:        FX risk — variability in GBP proceeds
        Hedged Item:              Highly probable forecast USD 5M receipt
        Hedging Instrument:       Forward contract to sell USD 5M at 1.2650
        Hedge Ratio:              1:1 (USD 5M forward / USD 5M exposure)
        Effectiveness Method:     Hypothetical derivative comparison

        At inception: No entry (forward at fair value = zero)

        3 months later: GBP/USD has fallen to 1.2400
        Forward fair value gain: (1.2650 - 1.2400) x 5M / 1.2400 = GBP 100,806

        Accounting entries:
          Dr  Forward Asset              GBP 100,806
          Cr  OCI (Cash Flow Hedge Reserve)  GBP 100,806

        At settlement: Forward gain reclassified from OCI to Revenue P&L
        ```

        **Effectiveness test:**
        Hedge ratio = forward gain / expected spot rate movement = within 80-125% band.
        """)

        st.subheader("Example 5: Stress Testing — GFC Scenario")
        st.markdown("""
        **Portfolio:** EUR 10M receivable, GBP 8M payable, JPY 1.5B receivable (USD-based company)
        **Current rates:** EUR/USD 1.0850; GBP/USD 1.2700; USD/JPY 149.50

        **GFC 2008 stress scenario applied:**
        ```
        EUR/USD fell   15% → New rate: 0.9223 (USD strengthens vs EUR)
        GBP/USD fell   28% → New rate: 0.9144 (GBP flash crash severity)
        USD/JPY fell   12% → New rate: 131.56 (JPY strengthens — safe haven)

        Stress P&L Impact:
          EUR receivable: EUR 10M x (0.9223 - 1.0850) = USD -1,627,000
          GBP payable:    GBP 8M x (1.2700 - 0.9144) = USD +2,844,800  ← gain (paying less)
          JPY receivable: JPY 1.5B x (1/131.56 - 1/149.50) = USD -1,365,000
          ──────────────────────────────────────────────────────────────
          Net Stress Loss:                                  USD -147,200

        Vs Normal 1-day 99% VaR:   USD ~150,000
        → GFC scenario loss ≈ 1x daily VaR (surprisingly contained due to offsets)
        ```
        **Key insight:** Portfolio diversification across currencies reduced stress loss significantly.
        """)

    # ══════════════════════════════════════════════════════════════════════
    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Calculator:", [
            "📊 Net FX Exposure Calculator",
            "📉 VaR Calculator (Parametric)",
            "🎯 Minimum Variance Hedge Ratio",
            "⚖️ IFRS 9 Effectiveness Tester",
            "🔥 Stress Testing Scenario Analyser"
        ])

        st.markdown("---")

        # ── NET EXPOSURE ──────────────────────────────────────────────
        if calc_choice == "📊 Net FX Exposure Calculator":
            st.subheader("Net FX Exposure Calculator")
            st.info("Enter all expected foreign currency cash flows to calculate your net exposure and recommend a hedge notional.")

            currency = st.text_input("Foreign Currency (e.g. USD)", value="USD")
            spot_rate = st.number_input("Current Spot Rate (domestic per foreign)", value=1.2700, format="%.4f")
            num_inflows = st.number_input("Number of Inflow Items", 1, 10, 3)
            num_outflows = st.number_input("Number of Outflow Items", 1, 10, 3)

            st.markdown("**Inflows (+):**")
            inflows = []
            for i in range(int(num_inflows)):
                col1, col2 = st.columns([2, 1])
                desc = col1.text_input(f"Inflow {i+1} description", value=["Export revenues", "Dividends from subsidiary", "Asset sale proceeds"][i] if i < 3 else f"Inflow {i+1}", key=f"inf_d_{i}")
                amt = col2.number_input(f"{currency} amount", value=[5000000.0, 2000000.0, 1000000.0][i] if i < 3 else 1000000.0, step=100000.0, key=f"inf_a_{i}")
                inflows.append((desc, amt))

            st.markdown("**Outflows (-):**")
            outflows = []
            for i in range(int(num_outflows)):
                col1, col2 = st.columns([2, 1])
                desc = col1.text_input(f"Outflow {i+1} description", value=["Import payments", "Foreign supplier costs", "Interest on USD debt"][i] if i < 3 else f"Outflow {i+1}", key=f"out_d_{i}")
                amt = col2.number_input(f"{currency} amount", value=[3000000.0, 1500000.0, 500000.0][i] if i < 3 else 500000.0, step=100000.0, key=f"out_a_{i}")
                outflows.append((desc, amt))

            if st.button("🧮 Calculate Net Exposure", type="primary"):
                total_in  = sum(a for _, a in inflows)
                total_out = sum(a for _, a in outflows)
                net = total_in - total_out
                net_domestic = net * spot_rate

                rows = ([{"Flow": "INFLOW", "Description": d, f"{currency} Amount": f"{a:,.0f}", "Domestic Equiv.": f"{a*spot_rate:,.0f}"} for d, a in inflows] +
                        [{"Flow": "OUTFLOW", "Description": d, f"{currency} Amount": f"-{a:,.0f}", "Domestic Equiv.": f"-{a*spot_rate:,.0f}"} for d, a in outflows] +
                        [{"Flow": "NET", "Description": "Net FX Exposure", f"{currency} Amount": f"{net:+,.0f}", "Domestic Equiv.": f"{net_domestic:+,.0f}"}])
                st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

                c1, c2, c3 = st.columns(3)
                c1.metric(f"Total {currency} Inflows",  f"{total_in:,.0f}")
                c2.metric(f"Total {currency} Outflows", f"{total_out:,.0f}")
                c3.metric("Net Exposure", f"{net:+,.0f} {currency}", f"≈ {net_domestic:+,.0f} domestic")

                direction = "LONG" if net > 0 else "SHORT"
                hedge_action = f"SELL {currency} forward" if net > 0 else f"BUY {currency} forward"
                st.success(f"✅ You are **{direction} {currency} {abs(net):,.0f}**. Recommended hedge: **{hedge_action}** for the net notional.")

                fig = go.Figure(go.Waterfall(
                    orientation="v",
                    measure=["relative"] * len(inflows) + ["relative"] * len(outflows) + ["total"],
                    x=[d for d, _ in inflows] + [d for d, _ in outflows] + ["NET"],
                    y=[a for _, a in inflows] + [-a for _, a in outflows] + [0],
                    connector={"line": {"color": "rgb(63, 63, 63)"}},
                    increasing={"marker": {"color": "#27AE60"}},
                    decreasing={"marker": {"color": "#E74C3C"}},
                    totals={"marker": {"color": "#2E86C1"}}
                ))
                fig.update_layout(title=f"FX Cash Flow Waterfall — {currency}", yaxis_title=f"{currency} Amount")
                st.plotly_chart(fig, use_container_width=True)

        # ── VAR ──────────────────────────────────────────────────────
        elif calc_choice == "📉 VaR Calculator (Parametric)":
            st.subheader("Parametric VaR Calculator — FX Portfolio")
            st.info("Calculate Value at Risk for one or more FX positions using the parametric (variance-covariance) method.")

            col1, col2 = st.columns(2)
            with col1:
                position_val = st.number_input("Position Value (domestic currency)", value=5425000.0, step=100000.0)
                daily_vol    = st.number_input("Daily Volatility % (sigma)", value=0.60, step=0.05, format="%.2f")
            with col2:
                confidence   = st.selectbox("Confidence Level", ["99% (Z = 2.326)", "97.5% (Z = 1.960)", "95% (Z = 1.645)"])
                holding_days = st.slider("Holding Period (days)", 1, 250, 1)

            z_map = {"99% (Z = 2.326)": 2.326, "97.5% (Z = 1.960)": 1.960, "95% (Z = 1.645)": 1.645}
            Z = z_map[confidence]
            conf_pct = confidence.split("%")[0]

            if st.button("🧮 Calculate VaR", type="primary"):
                var_1d = position_val * (daily_vol / 100) * Z
                var_nd = var_1d * np.sqrt(holding_days)
                var_pct = var_nd / position_val * 100
                expected_shortfall = var_1d * norm.pdf(norm.ppf(float(conf_pct)/100)) / (1 - float(conf_pct)/100)

                st.markdown("---")
                st.markdown(f"""
                **VaR Calculation:**
                ```
                VaR = Position × sigma_daily × Z × sqrt(T)
                    = {position_val:,.0f} × {daily_vol:.2f}% × {Z:.3f} × sqrt({holding_days})
                    = {position_val:,.0f} × {daily_vol/100:.4f} × {Z:.3f} × {np.sqrt(holding_days):.4f}
                    = {var_nd:,.2f}
                    = {var_pct:.3f}% of position

                1-day {conf_pct}% VaR:          {var_1d:,.2f}
                {holding_days}-day {conf_pct}% VaR:         {var_nd:,.2f}
                Expected Shortfall (approx.): {expected_shortfall:,.2f}
                ```
                """)
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("1-Day VaR", f"{var_1d:,.0f}")
                c2.metric(f"{holding_days}-Day VaR", f"{var_nd:,.0f}")
                c3.metric("VaR % of Position", f"{var_pct:.3f}%")
                c4.metric("Exp. Shortfall", f"{expected_shortfall:,.0f}")

                if var_pct > 3:
                    st.error(f"🚨 VaR exceeds 3% of position — HIGH risk. Review position sizing or add hedges.")
                elif var_pct > 1.5:
                    st.warning(f"⚠️ VaR is {var_pct:.2f}% of position — ELEVATED. Monitor closely.")
                else:
                    st.success(f"✅ VaR is {var_pct:.2f}% of position — within normal bounds.")

                days_range = list(range(1, 251))
                var_curve = [var_1d * np.sqrt(d) for d in days_range]
                fig = go.Figure(go.Scatter(x=days_range, y=var_curve, mode="lines",
                    line=dict(color="#E74C3C", width=2.5), name=f"{conf_pct}% VaR"))
                fig.add_vline(x=holding_days, line_dash="dash", annotation_text=f"Selected: {holding_days}d")
                fig.update_layout(title=f"VaR Scaling — {conf_pct}% Confidence Level",
                                  xaxis_title="Holding Period (days)", yaxis_title="VaR (domestic currency)")
                st.plotly_chart(fig, use_container_width=True)

        # ── HEDGE RATIO ──────────────────────────────────────────────
        elif calc_choice == "🎯 Minimum Variance Hedge Ratio":
            st.subheader("Minimum Variance Hedge Ratio Calculator")
            col1, col2 = st.columns(2)
            with col1:
                rho     = st.number_input("Correlation (rho) between spot and hedge", value=0.97, min_value=-1.0, max_value=1.0, step=0.01, format="%.3f")
                sigma_s = st.number_input("Spot Volatility % (sigma_S)", value=0.65, step=0.01, format="%.3f")
                sigma_f = st.number_input("Hedge Instrument Volatility % (sigma_F)", value=0.63, step=0.01, format="%.3f")
            with col2:
                exposure = st.number_input("Total Exposure Notional", value=10000000.0, step=500000.0)
                current_hedge = st.number_input("Current Hedge Notional (for comparison)", value=10000000.0, step=500000.0)

            if st.button("🧮 Calculate Optimal Hedge Ratio", type="primary"):
                h_star = rho * (sigma_s / sigma_f) if sigma_f > 0 else 0
                optimal_notional = h_star * exposure
                over_under = ((current_hedge - optimal_notional) / exposure) * 100

                st.markdown("---")
                st.markdown(f"""
                **Minimum Variance Hedge Ratio:**
                ```
                h* = rho × (sigma_S / sigma_F)
                   = {rho:.3f} × ({sigma_s:.3f}% / {sigma_f:.3f}%)
                   = {rho:.3f} × {sigma_s/sigma_f:.4f}
                   = {h_star:.4f}

                Optimal Hedge Notional = {h_star:.4f} × {exposure:,.0f}
                                       = {optimal_notional:,.0f}

                Current Hedge:    {current_hedge:,.0f}
                Optimal Hedge:    {optimal_notional:,.0f}
                Difference:       {current_hedge - optimal_notional:+,.0f} ({over_under:+.2f}% of exposure)
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("Optimal Hedge Ratio (h*)", f"{h_star:.4f}")
                c2.metric("Optimal Hedge Notional", f"{optimal_notional:,.0f}")
                c3.metric("vs Current Hedge", f"{current_hedge - optimal_notional:+,.0f}")

                if abs(over_under) < 2:
                    st.success(f"✅ Current hedge is near-optimal ({over_under:+.2f}% from optimal).")
                elif over_under > 0:
                    st.warning(f"⚠️ OVER-hedged by {abs(current_hedge - optimal_notional):,.0f} ({over_under:+.2f}%). Reduce hedge or you add risk.")
                else:
                    st.warning(f"⚠️ UNDER-hedged by {abs(current_hedge - optimal_notional):,.0f} ({over_under:.2f}%). Increase hedge to minimise variance.")

                rho_range = np.linspace(-1, 1, 100)
                h_range = [r * (sigma_s / sigma_f) for r in rho_range]
                fig = go.Figure(go.Scatter(x=rho_range, y=h_range, mode="lines",
                    line=dict(color="#2E86C1", width=2.5)))
                fig.add_vline(x=rho, line_dash="dash", annotation_text=f"Current rho={rho:.3f}")
                fig.add_hline(y=h_star, line_dash="dot", annotation_text=f"h*={h_star:.4f}")
                fig.update_layout(title="Optimal Hedge Ratio vs Correlation",
                                  xaxis_title="Correlation (rho)", yaxis_title="Optimal Hedge Ratio h*")
                st.plotly_chart(fig, use_container_width=True)

        # ── IFRS 9 EFFECTIVENESS ──────────────────────────────────────
        elif calc_choice == "⚖️ IFRS 9 Effectiveness Tester":
            st.subheader("IFRS 9 Hedge Effectiveness Tester")
            st.info("Test whether your hedge qualifies for IFRS 9 hedge accounting (80-125% effectiveness band).")
            col1, col2 = st.columns(2)
            with col1:
                hedge_type = st.selectbox("Hedge Type", ["Cash Flow Hedge", "Fair Value Hedge", "Net Investment Hedge"])
                num_periods = st.number_input("Number of Test Periods", 2, 12, 6)
            with col2:
                st.markdown("**Enter Fair Value Changes:**")

            rows_eff = []
            for i in range(int(num_periods)):
                col1, col2 = st.columns(2)
                h_change = col1.number_input(f"Period {i+1} — Hedge FV Change", value=[-8000, 12000, -5000, 15000, -10000, 9000][i] if i < 6 else 5000.0, step=100.0, key=f"hc_{i}")
                i_change = col2.number_input(f"Period {i+1} — Hedged Item FV Change", value=[8200, -11500, 5100, -14800, 10200, -8900][i] if i < 6 else -5000.0, step=100.0, key=f"ic_{i}")
                rows_eff.append({"Period": i+1, "Hedge FV Change": h_change, "Hedged Item FV Change": i_change})

            if st.button("🧮 Test Hedge Effectiveness", type="primary"):
                df_eff = pd.DataFrame(rows_eff)
                df_eff["Effectiveness %"] = df_eff.apply(
                    lambda r: abs(r["Hedge FV Change"] / r["Hedged Item FV Change"]) * 100 if r["Hedged Item FV Change"] != 0 else 0, axis=1)
                df_eff["IFRS 9 Status"] = df_eff["Effectiveness %"].apply(
                    lambda e: "✅ Qualifies" if 80 <= e <= 125 else "❌ Fails")
                df_eff["Hedge FV Change"] = df_eff["Hedge FV Change"].apply(lambda x: f"{x:+,.0f}")
                df_eff["Hedged Item FV Change"] = df_eff["Hedged Item FV Change"].apply(lambda x: f"{x:+,.0f}")
                df_eff["Effectiveness %"] = df_eff["Effectiveness %"].apply(lambda x: f"{x:.1f}%")
                st.dataframe(df_eff, use_container_width=True, hide_index=True)
                pass_count = sum(1 for r in rows_eff if 80 <= (abs(r["Hedge FV Change"] / r["Hedged Item FV Change"]) * 100 if r["Hedged Item FV Change"] != 0 else 0) <= 125)
                total_periods = len(rows_eff)
                c1, c2, c3 = st.columns(3)
                c1.metric("Periods Tested", total_periods)
                c2.metric("Periods Qualifying", pass_count)
                c3.metric("Pass Rate", f"{pass_count/total_periods*100:.0f}%")
                if pass_count == total_periods:
                    st.success("✅ All periods within 80-125% band. Hedge accounting QUALIFIES under IFRS 9.")
                else:
                    st.error(f"❌ {total_periods - pass_count} period(s) outside 80-125% band. Hedge accounting may be DISQUALIFIED. Review hedge structure.")

        # ── STRESS TEST ──────────────────────────────────────────────
        elif calc_choice == "🔥 Stress Testing Scenario Analyser":
            st.subheader("FX Stress Testing Scenario Analyser")
            st.markdown("**Define your FX portfolio and run historical or hypothetical stress scenarios.**")

            st.markdown("#### Portfolio Positions:")
            num_pos = st.number_input("Number of FX Positions", 1, 6, 3)
            positions = []
            for i in range(int(num_pos)):
                col1, col2, col3, col4 = st.columns(4)
                pair = col1.text_input("Pair", value=["EUR/USD", "GBP/USD", "USD/JPY"][i] if i < 3 else f"Pair {i+1}", key=f"st_pair_{i}")
                size = col2.number_input("Notional (base)", value=[5000000.0, 3000000.0, -2000000.0][i] if i < 3 else 1000000.0, step=100000.0, key=f"st_size_{i}")
                spot = col3.number_input("Current Spot", value=[1.0850, 1.2700, 149.50][i] if i < 3 else 1.0, format="%.4f", key=f"st_spot_{i}")
                direction = col4.selectbox("Direction", ["Long (buy base)", "Short (sell base)"], key=f"st_dir_{i}")
                positions.append({"pair": pair, "size": size, "spot": spot, "long": "Long" in direction})

            st.markdown("#### Stress Scenario:")
            scenario = st.selectbox("Choose Scenario", [
                "GFC 2008 (USD strengthens 15-25%)",
                "COVID-19 March 2020 (JPY safe-haven spike)",
                "Eurozone crisis 2011 (EUR weakens)",
                "Custom scenario (define your own)"
            ])

            if st.button("🔥 Run Stress Test", type="primary"):
                scenario_shocks = {
                    "GFC 2008 (USD strengthens 15-25%)": {"EUR/USD": -0.20, "GBP/USD": -0.28, "USD/JPY": -0.15},
                    "COVID-19 March 2020 (JPY safe-haven spike)": {"EUR/USD": -0.05, "GBP/USD": -0.10, "USD/JPY": -0.08},
                    "Eurozone crisis 2011 (EUR weakens)": {"EUR/USD": -0.18, "GBP/USD": 0.02, "USD/JPY": 0.05},
                    "Custom scenario (define your own)": {"EUR/USD": -0.10, "GBP/USD": -0.10, "USD/JPY": -0.10}
                }
                shocks = scenario_shocks[scenario]
                results = []
                total_pnl = 0
                for p in positions:
                    pair_key = p["pair"]
                    shock = shocks.get(pair_key, -0.10)
                    new_spot = p["spot"] * (1 + shock)
                    if p["long"]:
                        pnl = (new_spot - p["spot"]) * p["size"]
                    else:
                        pnl = (p["spot"] - new_spot) * p["size"]
                    total_pnl += pnl
                    results.append({
                        "Pair": p["pair"],
                        "Position": f"{'Long' if p['long'] else 'Short'} {p['size']:,.0f}",
                        "Current Spot": f"{p['spot']:.4f}",
                        "Shock Applied": f"{shock*100:+.1f}%",
                        "Stress Spot": f"{new_spot:.4f}",
                        "Stress P&L": f"{pnl:+,.0f}"
                    })
                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)
                st.metric("Total Portfolio Stress P&L", f"{total_pnl:+,.0f}",
                          delta_color="normal" if total_pnl >= 0 else "inverse")
                if total_pnl < 0:
                    st.error(f"🚨 Stress scenario produces a loss of {abs(total_pnl):,.0f}. Consider rebalancing hedges for tail risk protection.")
                else:
                    st.success(f"✅ Portfolio gains {total_pnl:,.0f} under this stress scenario — existing hedges provide protection.")

    # ══════════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("VaR vs Expected Shortfall — Normal Distribution")
        x_range = np.linspace(-4, 4, 400)
        y_norm  = norm.pdf(x_range)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=x_range, y=y_norm, mode="lines",
            line=dict(color="#2E86C1", width=2.5), name="Return Distribution"))
        var_z = -2.326
        x_tail = x_range[x_range <= var_z]
        y_tail = norm.pdf(x_tail)
        fig1.add_trace(go.Scatter(x=np.concatenate([x_tail, [var_z, var_z]]),
            y=np.concatenate([y_tail, [0, 0]]), fill="toself", fillcolor="rgba(231,76,60,0.3)",
            line=dict(color="rgba(231,76,60,0)"), name="1% Tail (VaR exceedance zone)"))
        fig1.add_vline(x=var_z, line_color="#E74C3C", line_dash="dash",
                      annotation_text=f"99% VaR (Z={abs(var_z):.3f})")
        fig1.update_layout(title="VaR Illustrated — 1-Day 99% Confidence Level (Normal Dist.)",
                           xaxis_title="Return (standard deviations)", yaxis_title="Probability Density")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Three Types of FX Exposure — Comparison")
        categories = ["Measurability", "Hedgeability", "Impact on P&L", "Impact on Balance Sheet", "Strategic Importance"]
        transaction = [9, 9, 8, 4, 6]
        translation = [6, 6, 5, 9, 4]
        economic    = [3, 3, 7, 6, 10]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatterpolar(r=transaction+[transaction[0]], theta=categories+[categories[0]],
            fill="toself", fillcolor="rgba(46,134,193,0.2)", line=dict(color="#2E86C1", width=2), name="Transaction"))
        fig2.add_trace(go.Scatterpolar(r=translation+[translation[0]], theta=categories+[categories[0]],
            fill="toself", fillcolor="rgba(39,174,96,0.2)", line=dict(color="#27AE60", width=2), name="Translation"))
        fig2.add_trace(go.Scatterpolar(r=economic+[economic[0]], theta=categories+[categories[0]],
            fill="toself", fillcolor="rgba(231,76,60,0.2)", line=dict(color="#E74C3C", width=2), name="Economic"))
        fig2.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                           title="FX Exposure Types — Characteristic Comparison", height=380)
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("VaR Scaling with Holding Period")
        holding_periods = list(range(1, 252))
        var_base = 75716
        var_scaled = [var_base * np.sqrt(d) for d in holding_periods]
        fig3 = go.Figure(go.Scatter(x=holding_periods, y=var_scaled, mode="lines",
            line=dict(color="#8E44AD", width=2.5), name="VaR (sqrt-T rule)"))
        fig3.add_vline(x=10, line_dash="dash", annotation_text="Basel 10-day")
        fig3.add_vline(x=250, line_dash="dot", annotation_text="1 Year")
        fig3.update_layout(title="VaR Scaling with Holding Period (1-Day VaR × sqrt(T))",
                           xaxis_title="Holding Period (days)", yaxis_title="VaR (USD)")
        st.plotly_chart(fig3, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — FX Risk Management")

        st.markdown("**Q1. A UK company has USD 8M receivable in 90 days. This is:**")
        q1 = st.radio("", [
            "Translation exposure — revaluing a USD subsidiary",
            "Transaction exposure — a contracted future USD cash flow",
            "Economic exposure — long-term competitive risk",
            "Sovereign risk — USD government default risk"
        ], key="fx8q1")
        if st.button("Check Q1", key="fx8c1"):
            if "Transaction exposure" in q1:
                st.success("✅ Correct! Transaction exposure = specifically contracted future foreign currency cash flows. Easy to quantify, hedge with forwards or options.")
            else:
                st.error("❌ Incorrect. The USD receivable is a contracted, specific future cash flow → Transaction exposure. Manage with forwards, options, or money market hedges.")
        st.markdown("---")

        st.markdown("**Q2. The 1-day 99% parametric VaR assumes:**")
        q2 = st.radio("", [
            "Returns follow a fat-tailed distribution",
            "Returns follow a normal (Gaussian) distribution",
            "Returns follow a Poisson distribution",
            "No distributional assumption is required"
        ], key="fx8q2")
        if st.button("Check Q2", key="fx8c2"):
            if "normal (Gaussian)" in q2:
                st.success("✅ Correct! Parametric VaR assumes normally distributed returns. This underestimates tail risk in practice (fat tails / kurtosis).")
            else:
                st.error("❌ Incorrect. Parametric (variance-covariance) VaR assumes normally distributed returns. Historical simulation makes no distributional assumption.")
        st.markdown("---")

        st.markdown("**Q3. The minimum variance hedge ratio h* = rho × (sigma_S / sigma_F). If sigma_F > sigma_S, then h* is:**")
        q3 = st.radio("", [
            "Greater than 1 — over-hedge",
            "Less than 1 — hedge only a fraction of the exposure",
            "Equal to 1 — always hedge 100%",
            "Negative — take an opposite position"
        ], key="fx8q3")
        if st.button("Check Q3", key="fx8c3"):
            if "Less than 1" in q3:
                st.success("✅ Correct! If sigma_F > sigma_S (hedge more volatile than exposure), then sigma_S/sigma_F < 1, so h* < 1. Don't hedge the full notional.")
            else:
                st.error("❌ Incorrect. When sigma_F > sigma_S, sigma_S/sigma_F < 1, so h* < 1. Hedge less than 100% of exposure to minimise variance.")
        st.markdown("---")

        st.markdown("**Q4. Under IFRS 9, a cash flow hedge gain/loss is initially recognised in:**")
        q4 = st.radio("", [
            "P&L immediately when the derivative fair value changes",
            "Other Comprehensive Income (OCI), reclassified to P&L when the hedged item affects income",
            "Retained earnings directly",
            "A separate hedge reserve account outside equity"
        ], key="fx8q4")
        if st.button("Check Q4", key="fx8c4"):
            if "Other Comprehensive Income (OCI)" in q4:
                st.success("✅ Correct! Cash flow hedge: gains/losses go to OCI first, then reclassified to P&L when the hedged transaction affects profit — matching timing.")
            else:
                st.error("❌ Incorrect. Cash flow hedge accounting defers gains/losses to OCI until the hedged item (e.g. the forecast transaction) impacts P&L.")
        st.markdown("---")

        st.markdown("**Q5. If IFRS 9 hedge effectiveness is measured at 72%, the hedge:**")
        q5 = st.radio("", [
            "Qualifies — 72% is acceptable",
            "Does not qualify — below the 80% minimum threshold",
            "Qualifies with a reduced hedge ratio applied",
            "Requires central bank approval to proceed"
        ], key="fx8q5")
        if st.button("Check Q5", key="fx8c5"):
            if "Does not qualify" in q5:
                st.success("✅ Correct! IFRS 9 requires effectiveness between 80% and 125%. At 72%, the hedge does not qualify and full fair value changes hit P&L immediately.")
            else:
                st.error("❌ Incorrect. IFRS 9 effectiveness range: 80% to 125%. Below 80% → hedge accounting disqualified → full P&L volatility on the derivative.")

    # ══════════════════════════════════════════════════════════════════════
    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Three FX Exposure Types — Quick Reference")
        exp_df = pd.DataFrame({
            "Exposure Type": ["Transaction", "Translation", "Economic (Operating)"],
            "Definition": [
                "Risk on contracted future foreign currency cash flows",
                "Risk when converting foreign subsidiary accounts to parent currency",
                "Long-term risk to competitive position and uncontracted cash flows"
            ],
            "Example": [
                "USD invoice receivable in 90 days",
                "EUR subsidiary revalued in USD parent accounts",
                "Competitor gains advantage from currency move"
            ],
            "Hedge Tools": [
                "Forwards, options, money market hedge",
                "Balance sheet matching, cross-currency swaps",
                "Operational decisions, invoice currency, diversification"
            ],
            "Measurability": ["High", "Medium", "Low"]
        })
        st.dataframe(exp_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "Net FX Exposure",
                "Parametric VaR (1-day)",
                "Scaled VaR (T-day)",
                "Minimum Variance Hedge Ratio",
                "Hedge Notional",
                "IFRS 9 Effectiveness"
            ],
            "Expression": [
                "Net = Total Foreign Inflows - Total Foreign Outflows",
                "VaR = Position × sigma_daily × Z",
                "VaR_T = VaR_1d × sqrt(T)",
                "h* = rho × (sigma_S / sigma_F)",
                "Hedge Notional = h* × Exposure Notional",
                "Effectiveness = |ΔFV_hedge| / |ΔFV_hedged item| × 100%"
            ],
            "Notes": [
                "Only hedge the net residual exposure",
                "99% confidence: Z=2.326; 95%: Z=1.645",
                "Basel: use 10-day VaR (× sqrt(10))",
                "rho = correlation; sigma_S/sigma_F = vol ratio",
                "May be < or > 100% of exposure",
                "Must be 80–125% to qualify for IFRS 9 hedge accounting"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 IFRS 9 Hedge Types Comparison")
        ifrs_df = pd.DataFrame({
            "Hedge Type": ["Fair Value Hedge", "Cash Flow Hedge", "Net Investment Hedge"],
            "Hedges Against": [
                "Fair value changes in a recognised asset or liability",
                "Variability in future cash flows (forecast transactions, floating rate debt)",
                "FX risk on net assets of a foreign subsidiary"
            ],
            "Derivative Gains/Losses": [
                "Immediately to P&L — offset by hedged item adjustment",
                "OCI → reclassified to P&L when hedged item affects income",
                "OCI → reclassified to P&L on disposal of subsidiary"
            ],
            "Common Example": [
                "Fixed-rate debt hedged with interest rate swap",
                "Forecast USD sales hedged with USD forward",
                "EUR subsidiary financed with EUR debt"
            ]
        })
        st.dataframe(ifrs_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Hedging gross flows rather than net exposure",
                "Using VaR alone as the only risk measure",
                "Setting h* = 1 always without calculating optimal",
                "Forgetting to test IFRS 9 effectiveness quarterly",
                "Confusing transaction and economic exposure"
            ],
            "Correct Approach": [
                "Net inflows and outflows first; only hedge residual net exposure",
                "Supplement VaR with stress testing and Expected Shortfall for tail risks",
                "Calculate h* = rho × sigma_S/sigma_F; may differ meaningfully from 1.0",
                "Document, test, and report hedge effectiveness every reporting period",
                "Transaction = contracted; Economic = long-term competitive — different tools"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 8 Complete! You can identify and quantify all three FX exposure types, calculate VaR, derive optimal hedge ratios, and apply IFRS 9 hedge accounting.")
        st.info("💡 Next: Module 9 — Macro Drivers of Exchange Rates (carry trade, central bank policy, BEER/FEER)")

if __name__ == "__main__":
    show()