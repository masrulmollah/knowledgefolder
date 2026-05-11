import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📐 Module 3: Exchange Rate Theories")
    st.markdown("*Master PPP, Covered & Uncovered Interest Rate Parity, the Fisher Effect, and the International Fisher Effect*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Purchasing Power Parity (PPP)")
        st.markdown("""
        **Absolute PPP:** Exchange rate should equal the ratio of price levels between countries.
        Identical goods should cost the same when expressed in a common currency.
        ```
        S = P_domestic / P_foreign
        ```
        The **Big Mac Index** (The Economist) is the most famous absolute PPP proxy.

        **Relative PPP:** More practical — links exchange rate *changes* to inflation differentials:
        ```
        E(S1) = S0 x (1 + pi_d) / (1 + pi_f)
        Approximation: %Change in S = pi_d - pi_f
        ```
        - US inflation 3.5%, EU inflation 2.0% → USD expected to depreciate ~1.5% vs EUR
        - PPP is a **long-run anchor** — can deviate significantly for years due to capital flows,
          risk sentiment, and productivity differences (Balassa-Samuelson effect)
        """)

        st.subheader("2. Covered Interest Rate Parity (CIP)")
        st.markdown("""
        **CIP** links the spot rate, forward rate, and interest rates. No currency risk — the forward
        contract locks in the return completely.
        ```
        F / S = (1 + i_d) / (1 + i_f)
        F = S x (1 + i_d x T/360) / (1 + i_f x T/360)
        ```

        | Scenario | Forward | Interpretation |
        |----------|---------|----------------|
        | i_d > i_f | F > S | Base currency at forward PREMIUM |
        | i_d < i_f | F < S | Base currency at forward DISCOUNT |
        | i_d = i_f | F = S | No forward adjustment |

        **CIP is arbitrage-enforced.** Any deviation allows borrow-invest-hedge arbitrage with zero risk.
        Post-2008: a persistent "CIP basis" exists due to bank balance sheet constraints.
        """)

        st.subheader("3. Uncovered Interest Rate Parity (UIP)")
        st.markdown("""
        **UIP** states that the *expected* exchange rate change equals the interest differential.
        Unlike CIP, there is no forward hedge — the investor bears full currency risk.
        ```
        E(%Change in S) = i_d - i_f
        ```

        **The Forward Premium Puzzle:**
        UIP fails empirically — high-yield currencies often APPRECIATE rather than depreciate.
        This is the basis of the **carry trade:**
        ```
        Carry Trade: Borrow low-yield currency, invest in high-yield currency
        Gross Carry = i_high - i_low
        Works because UIP fails — HY currencies often do not depreciate as predicted
        Risk: sudden risk-off events cause violent carry unwinds (e.g., 2008, 2020 COVID)
        ```
        """)

        st.subheader("4. Fisher Effect (Domestic)")
        st.markdown("""
        Links nominal interest rates, real interest rates, and inflation:
        ```
        (1 + i_nominal) = (1 + r_real) x (1 + pi_expected)
        Approximation: i_nominal = r_real + pi_expected
        ```
        - A rate hike driven by higher inflation expectations may NOT strengthen the currency
          if **real** interest rates remain unchanged
        - Central banks manage nominal rates; what matters for capital flows is the real rate
        """)

        st.subheader("5. International Fisher Effect (IFE)")
        st.markdown("""
        The **IFE** unifies PPP, CIP, and the Fisher Effect:
        ```
        (1 + i_d) / (1 + i_f) = (1 + pi_d) / (1 + pi_f) = E(S1) / S0
        ```
        If real interest rates are equal across countries (the key assumption):
        - Nominal rate differentials = Expected inflation differentials = Expected FX changes

        | Parity | Links | Currency Risk? |
        |--------|-------|---------------|
        | Absolute PPP | Price levels to spot rate | Yes |
        | Relative PPP | Inflation differential to spot change | Yes |
        | CIP | Interest differential to forward rate | No (hedged) |
        | UIP | Interest differential to expected spot change | Yes |
        | IFE | Combines all above | Yes |
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Relative PPP Calculation")
        st.markdown("""
        **Given:** EUR/USD spot = 1.0850; US inflation = 3.5%; EU inflation = 2.0%
        ```
        E(S1) = 1.0850 x (1.035 / 1.020)
               = 1.0850 x 1.01471
               = 1.1010

        Approximation: %Change = 3.5% - 2.0% = +1.5% USD depreciation
        Exact change: (1.1010 / 1.0850 - 1) x 100 = +1.47%
        ```
        **Finance Application:** A CFO budgeting for USD revenues converted to EUR should
        plan for approximately 1.5% FX headwind if PPP holds over the forecast period.
        """)

        st.subheader("Example 2: CIP Forward Rate Derivation")
        st.markdown("""
        **Given:** EUR/USD spot = 1.0850; US 1Y rate = 5.25%; EU 1Y rate = 3.75%
        ```
        F = 1.0850 x (1.0525 / 1.0375)
          = 1.0850 x 1.01446
          = 1.1007

        Forward Points = (1.1007 - 1.0850) x 10,000 = +157 pips
        EUR at premium because US rates are higher (USD at discount)
        ```
        **Why must it be 1.1007?**
        If F = 1.1050 instead: borrow EUR at 3.75%, convert to USD, invest at 5.25%,
        sell USD forward at 1.1050 → riskless profit. Arbitrage closes the deviation.
        """)

        st.subheader("Example 3: UIP Prediction vs Carry Trade Reality")
        st.markdown("""
        **US rate = 5.25%, Japan rate = 0.1%**
        ```
        UIP predicts: E(%Change USD/JPY) = 0.1% - 5.25% = -5.15%
        (USD expected to DEPRECIATE 5.15% vs JPY — making carry = 0%)

        Carry Trade Reality:
        Gross Carry = 5.25% - 0.1% = +5.15% p.a.

        Scenario A (normal): USD/JPY rises 2% (USD appreciates — opposite of UIP!)
          FX gain: +2.0% + carry +5.15% = +7.15% total return

        Scenario B (risk-off): USD/JPY falls 10% (yen spike)
          FX loss: -10.0% + carry +5.15% = -4.85% total return
        ```
        Key insight: A year of carry can be lost in days during a risk-off event.
        """)

        st.subheader("Example 4: IFE Consistency Check")
        comparison_df = pd.DataFrame({
            "Parity Condition": ["Relative PPP", "CIP Forward", "IFE Prediction"],
            "Formula": [
                "1.0850 x (1.035/1.020)",
                "1.0850 x (1.0525/1.0375)",
                "Converges with PPP and CIP"
            ],
            "Result": ["1.1010", "1.1007", "~1.100"],
            "Consistent?": ["Yes", "Yes", "Yes (within rounding)"]
        })
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)
        st.markdown("""
        All three conditions converge at approximately **1.100** — confirming IFE consistency.
        US real rate ≈ 1.69%, EU real rate ≈ 1.72% — nearly equal, validating the IFE assumption.
        """)

        st.subheader("Example 5: Big Mac PPP Index")
        bm_df = pd.DataFrame({
            "Country": ["USA", "Eurozone", "UK", "Switzerland", "Japan"],
            "Big Mac Price": ["$5.58", "EUR 4.65", "GBP 4.19", "CHF 6.70", "JPY 450"],
            "PPP-implied Rate": ["1.00", "0.834", "0.751", "1.201", "80.6"],
            "Actual Rate (local/USD)": ["1.00", "0.921", "0.787", "0.867", "150.5"],
            "Over/Undervalued": ["Benchmark", "-10% (undervalued)", "-5% (undervalued)", "+38% (overvalued)", "-46% (undervalued)"]
        })
        st.dataframe(bm_df, use_container_width=True, hide_index=True)
        st.info("💡 Big Mac PPP has real limitations — prices reflect local wages, rents, and taxes, not just traded goods prices.")

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "📈 PPP Expected Exchange Rate Calculator",
            "🔗 CIP Forward Rate & Arbitrage Checker",
            "💹 UIP & Carry Trade Return Calculator",
            "🌐 Big Mac PPP Valuation Tool"
        ])

        st.markdown("---")

        if calc_choice == "📈 PPP Expected Exchange Rate Calculator":
            st.subheader("Relative PPP — Expected Future Spot Rate")
            col1, col2, col3 = st.columns(3)
            with col1:
                s0 = st.number_input("Current Spot Rate (S0)", value=1.0850, format="%.4f", step=0.0001)
            with col2:
                pi_d = st.number_input("Domestic Inflation % (pi_d)", value=3.5, step=0.1)
            with col3:
                pi_f = st.number_input("Foreign Inflation % (pi_f)", value=2.0, step=0.1)
            yrs = st.slider("Forecast Horizon (years)", 1, 10, 1)

            s1 = s0 * ((1 + pi_d / 100) / (1 + pi_f / 100)) ** yrs
            chg = (s1 / s0 - 1) * 100
            ann_chg = ((1 + pi_d / 100) / (1 + pi_f / 100) - 1) * 100

            st.markdown("---")
            st.markdown(f"""
            **PPP Calculation:**
            ```
            E(S{yrs}) = {s0:.4f} x [(1 + {pi_d:.1f}%) / (1 + {pi_f:.1f}%)] ^ {yrs}
                     = {s1:.4f}

            Total change over {yrs} year(s): {chg:+.2f}%
            Annual rate of change:           {ann_chg:+.2f}% p.a.
            ```
            """)
            col1, col2, col3 = st.columns(3)
            col1.metric("Spot Rate (S0)", f"{s0:.4f}")
            col2.metric(f"PPP Rate in {yrs}Y", f"{s1:.4f}", f"{chg:+.2f}%")
            col3.metric("Annual Change", f"{ann_chg:+.2f}% p.a.")

            if ann_chg > 0:
                st.info(f"📉 Domestic currency expected to DEPRECIATE {abs(ann_chg):.2f}% p.a. (higher domestic inflation).")
            elif ann_chg < 0:
                st.info(f"📈 Domestic currency expected to APPRECIATE {abs(ann_chg):.2f}% p.a. (lower domestic inflation).")
            else:
                st.success("Equal inflation rates — no PPP-implied exchange rate change.")

            rates_path = [s0 * ((1 + pi_d / 100) / (1 + pi_f / 100)) ** y for y in range(yrs + 1)]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(range(yrs + 1)), y=rates_path,
                mode='lines+markers', line=dict(color='#2E86C1', width=2.5), marker=dict(size=8)))
            fig.add_hline(y=s0, line_dash='dash', line_color='gray', annotation_text=f'Current Spot {s0:.4f}')
            fig.update_layout(title='PPP Projected Exchange Rate Path',
                              xaxis_title='Year', yaxis_title='Exchange Rate')
            st.plotly_chart(fig, use_container_width=True)

        elif calc_choice == "🔗 CIP Forward Rate & Arbitrage Checker":
            st.subheader("CIP Forward Rate Calculator & Arbitrage Checker")
            col1, col2 = st.columns(2)
            with col1:
                spot_c = st.number_input("Spot Rate (S0)", value=1.0850, format="%.4f")
                i_d_c = st.number_input("Domestic Interest Rate % p.a.", value=5.25, step=0.05)
            with col2:
                i_f_c = st.number_input("Foreign Interest Rate % p.a.", value=3.75, step=0.05)
                tenor_c = st.number_input("Tenor (days)", value=365, step=30, min_value=1)

            F_cip = spot_c * (1 + i_d_c / 100 * tenor_c / 360) / (1 + i_f_c / 100 * tenor_c / 360)
            fp = (F_cip - spot_c) * 10000
            prem_pct = (F_cip - spot_c) / spot_c * 100

            st.markdown("---")
            st.markdown(f"""
            **CIP Forward Rate:**
            ```
            F = {spot_c:.4f} x (1 + {i_d_c:.2f}% x {tenor_c:.0f}/360)
                              (1 + {i_f_c:.2f}% x {tenor_c:.0f}/360)
              = {F_cip:.4f}

            Forward Points:    {fp:+.1f} pips
            Premium/Discount:  {prem_pct:+.3f}%
            ```
            """)
            col1, col2, col3 = st.columns(3)
            col1.metric("CIP Fair Forward", f"{F_cip:.4f}")
            col2.metric("Forward Points", f"{fp:+.1f} pips")
            col3.metric("Premium/Discount", f"{prem_pct:+.3f}%")

            st.markdown("---")
            st.subheader("Arbitrage Checker")
            actual_fwd = st.number_input("Enter Actual Market Forward (check for arbitrage)",
                                          value=round(F_cip, 4), format="%.4f")
            invest_amt = st.number_input("Investment Amount (domestic currency)", value=1000000.0, step=100000.0)

            basis_bps = (actual_fwd - F_cip) / F_cip * 10000
            approx_profit = abs(actual_fwd - F_cip) * (invest_amt / spot_c) * (1 + i_f_c / 100 * tenor_c / 360)

            st.markdown(f"""
            ```
            CIP Fair Forward:       {F_cip:.4f}
            Actual Market Forward:  {actual_fwd:.4f}
            Deviation:              {basis_bps:+.2f} bps
            Est. Arbitrage Profit:  {approx_profit:+,.2f} domestic currency
            ```
            """)
            if abs(basis_bps) < 1.0:
                st.success(f"✅ CIP holds — basis = {basis_bps:.2f} bps. No arbitrage opportunity.")
            elif actual_fwd > F_cip:
                st.warning(f"⚠️ Forward OVERPRICED by {basis_bps:.1f} bps. CIA: Borrow domestic, invest foreign, sell forward at actual. Estimated profit: {approx_profit:,.2f}")
            else:
                st.warning(f"⚠️ Forward UNDERPRICED by {abs(basis_bps):.1f} bps. CIA: Borrow foreign, invest domestic, buy forward at actual. Estimated profit: {approx_profit:,.2f}")

        elif calc_choice == "💹 UIP & Carry Trade Return Calculator":
            st.subheader("Carry Trade Return Calculator")
            col1, col2 = st.columns(2)
            with col1:
                i_high = st.number_input("High-yield currency rate % (invest here)", value=5.25, step=0.1)
                i_low = st.number_input("Funding currency rate % (borrow here)", value=0.10, step=0.05)
            with col2:
                actual_spot_move = st.number_input("Actual spot move % (+ve = HY currency depreciates)", value=0.0, step=0.1)
                invest_carry = st.number_input("Investment Amount", value=1000000.0, step=100000.0)

            gross_carry = i_high - i_low
            net_return = gross_carry - actual_spot_move
            dollar_return = invest_carry * net_return / 100

            st.markdown("---")
            st.markdown(f"""
            **Carry Trade Analysis:**
            ```
            UIP predicts HY currency depreciation of: {gross_carry:.2f}% (net return = 0%)

            Gross Carry (i_high - i_low):  {gross_carry:.2f}%
            Actual Spot Move:             {actual_spot_move:+.2f}%
            Net Return:                   {net_return:.2f}%
            Dollar Return on {invest_carry:,.0f}: {dollar_return:,.2f}
            ```
            """)
            col1, col2, col3 = st.columns(3)
            col1.metric("Gross Carry", f"{gross_carry:.2f}%")
            col2.metric("Net Return", f"{net_return:.2f}%", delta_color="normal" if net_return > 0 else "inverse")
            col3.metric("Dollar Return", f"{dollar_return:,.0f}")

            if net_return > 0:
                st.success(f"✅ Profitable carry: {net_return:.2f}%. UIP failed — HY currency did not depreciate enough.")
            elif net_return < -gross_carry:
                st.error(f"❌ Carry unwind! Lost {abs(net_return):.2f}% — spot depreciation swamped the carry.")
            else:
                st.warning(f"⚠️ Partial loss: {net_return:.2f}%. Spot depreciation partially offset the carry.")

            scenarios_range = range(-10, 11)
            net_returns = [gross_carry - s for s in scenarios_range]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(scenarios_range), y=net_returns,
                mode='lines+markers', line=dict(color='#2E86C1', width=2.5), name='Net Return'))
            fig.add_hline(y=0, line_color='red', line_dash='dash', annotation_text='Break-even')
            fig.add_vline(x=actual_spot_move, line_color='orange', line_dash='dot',
                         annotation_text=f'Actual: {actual_spot_move:.1f}%')
            fig.update_layout(title='Carry Trade Return vs Spot Move',
                              xaxis_title='Spot Move % (+ = HY depr.)', yaxis_title='Net Return %')
            st.plotly_chart(fig, use_container_width=True)

        elif calc_choice == "🌐 Big Mac PPP Valuation Tool":
            st.subheader("Big Mac PPP Index Calculator")
            base_price = st.number_input("Big Mac Price in USA (USD)", value=5.58, step=0.01)
            num_countries = st.number_input("Number of countries to compare", 1, 6, 4)

            default_names = ["Eurozone", "UK", "Japan", "Switzerland", "Australia", "Brazil"]
            default_local = [4.65, 4.19, 450.0, 6.70, 7.45, 22.90]
            default_rates = [0.921, 0.787, 150.5, 0.867, 1.532, 4.97]

            country_data = []
            cols_form = st.columns(2)
            for i in range(int(num_countries)):
                with cols_form[i % 2]:
                    cname = st.text_input(f"Country {i+1}", value=default_names[i] if i < 6 else f"Country {i+1}", key=f"bm_n_{i}")
                    local_price = st.number_input(f"Big Mac price (local)", value=default_local[i] if i < 6 else 5.0, step=0.01, key=f"bm_p_{i}")
                    actual_rate = st.number_input(f"Actual rate (local/USD)", value=default_rates[i] if i < 6 else 1.0, step=0.001, key=f"bm_r_{i}")
                    country_data.append({"Country": cname, "Local Price": local_price, "Actual Rate": actual_rate})

            if st.button("Calculate PPP Valuations", type="primary"):
                rows = []
                vals, names = [], []
                for d in country_data:
                    ppp_rate = d["Local Price"] / base_price
                    over_under = (d["Actual Rate"] / ppp_rate - 1) * 100
                    rows.append({
                        "Country": d["Country"],
                        "Local Price": f"{d['Local Price']:.2f}",
                        "PPP Rate": f"{ppp_rate:.4f}",
                        "Actual Rate": f"{d['Actual Rate']:.4f}",
                        "Over/Undervalued": f"{over_under:+.1f}%",
                        "Verdict": "Overvalued vs USD" if over_under > 5 else ("Undervalued vs USD" if over_under < -5 else "Fairly valued")
                    })
                    vals.append((d["Local Price"] / base_price / d["Actual Rate"] - 1) * 100)
                    names.append(d["Country"])
                st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
                fig = go.Figure(go.Bar(x=names, y=vals,
                    marker_color=["#27AE60" if v > 0 else "#E74C3C" for v in vals],
                    text=[f"{v:+.1f}%" for v in vals], textposition='outside'))
                fig.add_hline(y=0, line_color='black', line_dash='dash')
                fig.update_layout(title='Currency Valuation vs USD (PPP-based Big Mac Index)',
                                  xaxis_title='Country', yaxis_title='% Over/Undervalued vs USD')
                st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.header("Visualizations")

        st.subheader("Currency Over/Under-valuation vs PPP Fair Value")
        countries = ['Switzerland', 'UK', 'USA', 'Japan', 'Brazil', 'India', 'Turkey']
        actual_r = [0.91, 1.27, 1.00, 0.0067, 0.19, 0.012, 0.031]
        ppp_r = [0.83, 1.18, 1.00, 0.0079, 0.21, 0.016, 0.048]
        overunder = [(a / p - 1) * 100 for a, p in zip(actual_r, ppp_r)]
        fig1 = go.Figure(go.Bar(
            x=countries, y=overunder,
            marker_color=['#E74C3C' if x > 0 else '#27AE60' for x in overunder],
            text=[f'{x:+.1f}%' for x in overunder], textposition='outside'
        ))
        fig1.add_hline(y=0, line_color='black', line_dash='dash', annotation_text='PPP fair value')
        fig1.update_layout(title='Currency Over/Under-valuation vs PPP (vs USD)',
                           xaxis_title='Country', yaxis_title='% from PPP fair value')
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("US vs EU Rate Differential & EUR/USD Exchange Rate")
        years = list(range(2015, 2025))
        us_rates = [0.25, 0.50, 1.25, 2.25, 2.50, 0.25, 0.25, 0.75, 4.50, 5.25]
        eu_rates = [0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 3.50, 4.00]
        eurusd_hist = [1.09, 1.05, 1.05, 1.20, 1.14, 1.18, 1.22, 1.07, 1.07, 1.09]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=years, y=us_rates, name='US Rate %', line=dict(color='#E74C3C', width=2.5)))
        fig2.add_trace(go.Scatter(x=years, y=eu_rates, name='EU Rate %', line=dict(color='#2E86C1', width=2.5)))
        fig2.add_trace(go.Scatter(x=years, y=eurusd_hist, name='EUR/USD (RHS)',
                                  line=dict(color='#27AE60', width=2, dash='dot'), yaxis='y2'))
        fig2.update_layout(
            title='US vs EU Rate Differential & EUR/USD (2015-2024)',
            yaxis=dict(title='Policy Rate %'), yaxis2=dict(title='EUR/USD', overlaying='y', side='right'),
            legend=dict(x=0.01, y=0.99)
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Empirical Support for Parity Conditions")
        conditions = ['Absolute PPP', 'Relative PPP\n(Long Run)', 'CIP', 'UIP', 'IFE']
        support = [3, 7, 9, 2, 5]
        colors_c = ['#E67E22', '#F39C12', '#27AE60', '#E74C3C', '#8E44AD']
        fig3 = go.Figure(go.Bar(x=conditions, y=support, marker_color=colors_c,
            text=[f'{v}/10' for v in support], textposition='outside'))
        fig3.update_layout(title='Empirical Support for Each Parity Condition (1=Weak, 10=Strong)',
                           xaxis_title='Parity Condition', yaxis_title='Empirical Support',
                           yaxis=dict(range=[0, 11]))
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding of Exchange Rate Theories")

        st.markdown("**1. Relative PPP states the exchange rate change approximately equals:**")
        q1 = st.radio("Select your answer:", [
            "The GDP growth rate differential",
            "The inflation rate differential between the two countries",
            "The current account balance ratio",
            "The interest rate differential"
        ], key="fx3q1")
        if st.button("Check Answer", key="fx3c1"):
            if "inflation rate differential" in q1:
                st.success("✅ Correct! Relative PPP: %ΔS ≈ pi_d − pi_f. Higher-inflation country's currency depreciates proportionally.")
            else:
                st.error("❌ Incorrect. Relative PPP links exchange rate CHANGES to the INFLATION differential, not interest rates or GDP.")
        st.markdown("---")

        st.markdown("**2. CIP is described as 'arbitrage-enforced' because:**")
        q2 = st.radio("Select your answer:", [
            "Central banks enforce it through direct intervention",
            "Any deviation creates a riskless profit that traders immediately eliminate",
            "It is required by IMF and BIS regulations",
            "Markets are always perfectly efficient under CIP"
        ], key="fx3q2")
        if st.button("Check Answer", key="fx3c2"):
            if "riskless profit" in q2:
                st.success("✅ Correct! Any CIP deviation allows riskless borrow-invest-hedge arbitrage. Traders close the gap instantly.")
            else:
                st.error("❌ Incorrect. CIP is self-enforcing: any deviation = riskless profit → traders exploit it → deviation disappears.")
        st.markdown("---")

        st.markdown("**3. EUR/USD spot = 1.0850, US rate = 5%, EU rate = 3%. Approximate 1Y CIP forward:**")
        q3 = st.radio("Select your answer:", ["1.0850", "1.1057", "1.0641", "1.2000"], key="fx3q3")
        if st.button("Check Answer", key="fx3c3"):
            if q3 == "1.1057":
                st.success("✅ Correct! F = 1.0850 × (1.05/1.03) = 1.0850 × 1.01942 ≈ 1.1061 (closest answer = 1.1057).")
            else:
                st.error("❌ Incorrect. F = 1.0850 × (1.05/1.03) = 1.0850 × 1.01942 ≈ 1.1061.")
        st.markdown("---")

        st.markdown("**4. The carry trade exploits:**")
        q4 = st.radio("Select your answer:", [
            "PPP deviations in goods markets",
            "CIP arbitrage in forward markets",
            "UIP violations — high-yield currencies often fail to depreciate as UIP predicts",
            "Central bank intervention patterns"
        ], key="fx3q4")
        if st.button("Check Answer", key="fx3c4"):
            if "UIP violations" in q4:
                st.success("✅ Correct! Carry trade profits from UIP failure. Borrow low-yield, invest high-yield. Dangerous during risk-off events.")
            else:
                st.error("❌ Incorrect. The carry trade exploits UIP violations — high-yield currencies tend to appreciate rather than depreciate.")
        st.markdown("---")

        st.markdown("**5. The International Fisher Effect states nominal rate differentials equal:**")
        q5 = st.radio("Select your answer:", [
            "Real interest rate differentials only",
            "Expected inflation differentials AND expected exchange rate changes",
            "GDP growth rate differentials",
            "Trade balance ratios between countries"
        ], key="fx3q5")
        if st.button("Check Answer", key="fx3c5"):
            if "Expected inflation differentials AND expected exchange rate changes" in q5:
                st.success("✅ Correct! IFE: (1+i_d)/(1+i_f) = (1+pi_d)/(1+pi_f) = E(S1)/S0 — unifying all parity conditions.")
            else:
                st.error("❌ Incorrect. IFE: nominal rate differentials = inflation differentials = expected FX changes.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")

        st.markdown("""
        ### 1. Purchasing Power Parity (PPP)
        - **Absolute PPP**: S = P_d / P_f (Law of One Price)
        - **Relative PPP**: E(S1) = S0 × (1 + pi_d) / (1 + pi_f)
        - PPP is a **long-run anchor** — deviations can persist for years
        - Big Mac Index: imperfect but intuitive absolute PPP measure

        ### 2. Covered Interest Rate Parity (CIP)
        - F = S × (1 + i_d × T/360) / (1 + i_f × T/360)
        - **Arbitrage-enforced** — deviations create riskless profit
        - No currency risk — forward contract locks in the return
        - Post-2008 CIP basis = bank balance sheet constraint, not free profit

        ### 3. Uncovered Interest Rate Parity (UIP)
        - E(%ΔS) ≈ i_d − i_f — but frequently FAILS in practice
        - Failure basis of the carry trade: borrow low-yield, invest high-yield
        - Profitable in calm markets; dangerous during risk-off events

        ### 4. Fisher Effect & International Fisher Effect
        - i_nominal = r_real + pi_expected
        - IFE: (1+i_d)/(1+i_f) = (1+pi_d)/(1+pi_f) = E(S1)/S0
        - When real rates are equal globally, all three parity conditions converge

        ### 5. Key Formulas Summary
        ```
        Relative PPP:    E(S1) = S0 x (1 + pi_d) / (1 + pi_f)
        Approximation:   %Change in S = pi_d - pi_f
        CIP:             F = S x (1 + i_d x T/360) / (1 + i_f x T/360)
        UIP:             E(%Change in S) = i_d - i_f
        Fisher:          i_nominal = r_real + pi_expected
        IFE:             (1+i_d)/(1+i_f) = (1+pi_d)/(1+pi_f) = E(S1)/S0
        Carry Return:    i_high - i_low - actual spot depreciation
        ```
        """)

        st.subheader("📌 Quick Reference — Which Parity to Use?")
        ref_df = pd.DataFrame({
            "Situation": [
                "Pricing a forward contract",
                "Long-run currency valuation for strategic planning",
                "Explaining why a carry trade works",
                "Checking real rate equality across countries",
                "Estimating inflation-adjusted return on foreign bond"
            ],
            "Use This": ["CIP", "Relative PPP", "UIP violation", "IFE", "Fisher + CIP"],
            "Currency Risk?": ["No (hedged)", "Yes", "Yes", "No assumption", "No (hedged forward)"]
        })
        st.dataframe(ref_df, use_container_width=True, hide_index=True)

        st.success("🎓 **You've completed Module 3!** You understand all five major parity conditions and can apply them to FX pricing, valuation, and hedging decisions.")
        st.info("💡 **Next Steps**: Proceed to Module 4 — Forward Markets & Forward Rate Mathematics.")

if __name__ == "__main__":
    show()