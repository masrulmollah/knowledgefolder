import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💱 Module 1: Foundations of Foreign Exchange")
    st.markdown("*Understand the FX market structure, spot quotes, bid-ask spreads, cross rates, and pip arithmetic*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. What is the Foreign Exchange Market?")
        st.markdown("""
        The **Foreign Exchange (FX / Forex) market** is a global, decentralised, over-the-counter (OTC)
        marketplace where currencies are bought and sold. It is the **largest and most liquid financial
        market in the world** with approximately **$7.5 trillion** in daily turnover (BIS 2022).

        #### Key Features:
        - **OTC market** — no central exchange; trades happen directly between participants
        - **24/5 operation** — open Sunday 10 PM GMT (Sydney) to Friday 9 PM GMT (New York close)
        - **Decentralised** — prices set by competition among thousands of dealers
        - **No single regulator** — governed by local regulations in each jurisdiction
        """)

        st.subheader("2. Key Market Participants")
        participants = {
            "Participant": ["Central Banks", "Commercial Banks", "Corporations", "Hedge Funds / Asset Managers", "Retail Traders"],
            "Role": [
                "Manage foreign reserves, implement monetary policy, intervene to stabilise exchange rates",
                "Facilitate client FX transactions, provide liquidity, proprietary trading",
                "Hedge trade receivables/payables, convert foreign revenues, fund overseas investments",
                "Speculative trading, carry trades, currency overlay for international portfolios",
                "Smallest segment — trade via online brokers; mainly speculative"
            ],
            "Approx. Share": ["~5%", "~38%", "~18%", "~30%", "~9%"]
        }
        st.dataframe(pd.DataFrame(participants), use_container_width=True, hide_index=True)

        st.subheader("3. Currency Pair Conventions")
        st.markdown("""
        Currencies are always quoted in **pairs**, written as **BASE / QUOTE**:

        | Term | Definition | Example (EUR/USD = 1.0850) |
        |------|-----------|---------------------------|
        | **Base Currency** | The currency being bought or sold (always 1 unit) | EUR |
        | **Quote Currency** | The price expressed in this currency | USD |
        | **Exchange Rate** | How many quote units buy 1 base unit | 1.0850 USD per EUR |

        #### Direct vs Indirect Quotation:
        - **Direct quote** (from USD perspective): EUR/USD = 1.0850 → 1 EUR costs $1.0850
        - **Indirect quote** (from USD perspective): USD/EUR = 0.9217 → 1 USD buys €0.9217
        - **Rule:** Direct × Indirect = 1 (they are exact reciprocals)
        """)

        st.subheader("4. Bid, Ask, and Spread")
        st.markdown("""
        Every FX quote has **two prices**:

        | Price | Definition | Who it applies to |
        |-------|-----------|-------------------|
        | **Bid** | Price the market maker will BUY the base currency | You SELL at the bid |
        | **Ask (Offer)** | Price the market maker will SELL the base currency | You BUY at the ask |
        | **Spread** | Ask minus Bid — the dealer's profit margin | Always paid by the client |

        **Example:** EUR/USD quoted as **1.08500 / 1.08520**
        - Bid = 1.08500 | Ask = 1.08520 | Spread = 0.00020 = **2 pips**

        #### Factors affecting spread width:
        - **Liquidity** — major pairs (EUR/USD) have tighter spreads than exotic pairs
        - **Volatility** — spreads widen during news events and market stress
        - **Time of day** — widest during low-liquidity periods (e.g., Sydney session for EUR/USD)
        - **Credit relationship** — institutional clients get tighter spreads than retail
        """)

        st.subheader("5. Pips and Pip Value")
        st.markdown("""
        A **pip** (percentage in point) is the smallest standardised price move in FX:

        | Pair Type | 1 Pip = | Example |
        |-----------|---------|---------|
        | Most pairs (EUR/USD, GBP/USD, etc.) | 0.0001 (4th decimal) | 1.0850 → 1.0851 |
        | JPY pairs (USD/JPY, EUR/JPY) | 0.01 (2nd decimal) | 149.50 → 149.51 |

        ```
        Pip Value = (Pip Size / Exchange Rate) × Lot Size

        Standard Lot  = 100,000 units of base currency
        Mini Lot      = 10,000 units
        Micro Lot     = 1,000 units
        ```

        **Example:** EUR/USD = 1.0850, Standard Lot
        Pip Value = (0.0001 / 1.0850) × 100,000 = **$9.22 per pip**
        """)

        st.subheader("6. Cross Rates")
        st.markdown("""
        A **cross rate** is an exchange rate between two currencies, **neither of which is USD**,
        derived from their individual USD rates.

        ```
        Cross Rate (A/C) = Rate (A/B) × Rate (B/C)

        Example:
        EUR/USD = 1.0850  and  USD/JPY = 149.50
        EUR/JPY = 1.0850 × 149.50 = 162.21
        ```

        If EUR/JPY trades at 163.00 in the market but the cross rate implies 162.21,
        a **triangular arbitrage** opportunity exists — traders will exploit it until prices align.
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Reading FX Quotes")
        st.markdown("""
        **Scenario:** You are a Singapore-based importer who needs to buy USD to pay a US supplier.
        Your bank quotes EUR/USD at **1.0845 / 1.0847** and USD/SGD at **1.3450 / 1.3455**.

        **Q: How many SGD do you need to buy USD 500,000?**
        """)
        quote_data = {
            "Step": ["1", "2", "3"],
            "Action": [
                "You BUY USD — so you pay the ASK rate for USD/SGD",
                "SGD needed = USD 500,000 × Ask rate",
                "SGD needed = 500,000 × 1.3455"
            ],
            "Result": ["USD/SGD Ask = 1.3455", "SGD = USD × 1.3455", "SGD 672,750"]
        }
        st.dataframe(pd.DataFrame(quote_data), use_container_width=True, hide_index=True)

        st.subheader("Example 2: Cross Rate Calculation")
        st.markdown("""
        **Given:** EUR/USD = 1.0850 and USD/CHF = 0.9050
        **Find:** EUR/CHF cross rate

        ```
        EUR/CHF = EUR/USD × USD/CHF
                = 1.0850 × 0.9050
                = 0.9820

        Verify: 1 EUR should cost CHF 0.9820
        ```
        **Check for arbitrage:** If EUR/CHF market rate = 0.9900, you could:
        1. Buy EUR with USD at 1.0850 → Buy CHF with EUR at 0.9900 → Sell CHF for USD
        2. Net profit per million euros = significant riskless gain
        3. Arbitrage activity quickly closes the gap
        """)

        st.subheader("Example 3: Spread Cost on a Large Transaction")
        st.markdown("""
        **Scenario:** A multinational converts EUR 10,000,000 to USD.
        EUR/USD quoted: Bid 1.08490 / Ask 1.08510

        ```
        If you SELL EUR (buy USD): you receive Bid rate = 1.08490
        If mid-market rate       = 1.08500

        Spread cost = (Mid − Bid) × Notional
                    = (1.08500 − 1.08490) × 10,000,000
                    = 0.00010 × 10,000,000
                    = USD 1,000 transaction cost

        Annual impact: 500 such transactions = USD 500,000 in spread costs
        → Why treasury teams negotiate tight spreads with relationship banks
        ```
        """)

        st.subheader("Example 4: Pip Value Calculation")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **EUR/USD Standard Lot:**
            ```
            Pip Value = (0.0001 / 1.0850) × 100,000
                      = 0.09216 × 100
                      = $9.22 per pip
            ```
            If EUR/USD moves from 1.0850 to 1.0900 (+50 pips):
            P&L = 50 × $9.22 = **$461 profit**
            """)
        with col2:
            st.markdown("""
            **USD/JPY Standard Lot:**
            ```
            Pip Value = (0.01 / 149.50) × 100,000
                      = 0.0000669 × 100,000
                      = $6.69 per pip
            ```
            Note: JPY pairs use 0.01 as pip size, not 0.0001.
            Always check the pair convention!
            """)

        st.subheader("Example 5: Trade P&L Calculation")
        st.markdown("""
        **Long EUR/USD:** Buy 2 standard lots at 1.0850, close at 1.0920 (+70 pips)
        ```
        P&L = (Exit − Entry) × Lot Size × Number of Lots
            = (1.0920 − 1.0850) × 100,000 × 2
            = 0.0070 × 200,000
            = USD 1,400 profit
        ```

        **Short GBP/USD:** Sell 1 standard lot at 1.2700, close at 1.2640 (+60 pips profit)
        ```
        P&L = (Entry − Exit) × Lot Size   [reversed for short]
            = (1.2700 − 1.2640) × 100,000
            = 0.0060 × 100,000
            = USD 600 profit
        ```
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "📐 Spread Calculator",
            "🔢 Cross Rate Calculator",
            "💰 Pip Value Calculator",
            "📈 Trade P&L Calculator",
            "🔄 Currency Converter"
        ])

        st.markdown("---")

        if calc_choice == "📐 Spread Calculator":
            st.subheader("Spread & Transaction Cost Calculator")
            col1, col2 = st.columns(2)
            with col1:
                bid = st.number_input("Bid Rate", value=1.08500, format="%.5f", step=0.00001)
                ask = st.number_input("Ask Rate", value=1.08520, format="%.5f", step=0.00001)
            with col2:
                notional = st.number_input("Notional (base currency)", value=1000000.0, step=100000.0)
                is_jpy = st.checkbox("JPY pair? (pip = 0.01)")

            if ask > bid:
                pip_size = 0.01 if is_jpy else 0.0001
                spread_pips = (ask - bid) / pip_size
                spread_pct = (ask - bid) / ask * 100
                spread_cost = (ask - bid) * notional
                mid = (bid + ask) / 2

                st.markdown("---")
                st.markdown(f"""
                **Spread Analysis:**
                ```
                Bid:            {bid:.5f}
                Ask:            {ask:.5f}
                Mid-market:     {mid:.5f}
                ─────────────────────────────
                Spread:         {spread_pips:.1f} pips
                Spread (%):     {spread_pct:.4f}%
                Transaction Cost (notional {notional:,.0f}): {spread_cost:,.2f} quote currency
                ```
                """)
                col1, col2, col3 = st.columns(3)
                col1.metric("Spread", f"{spread_pips:.1f} pips")
                col2.metric("Spread %", f"{spread_pct:.4f}%")
                col3.metric("Transaction Cost", f"{spread_cost:,.2f}")
            else:
                st.error("❌ Ask rate must be greater than Bid rate.")

        elif calc_choice == "🔢 Cross Rate Calculator":
            st.subheader("Cross Rate Calculator (via USD)")
            col1, col2 = st.columns(2)
            with col1:
                ccy_a = st.text_input("Currency A (e.g. EUR)", value="EUR")
                rate_a_usd = st.number_input(f"{ccy_a}/USD rate", value=1.0850, format="%.4f", step=0.0001)
            with col2:
                ccy_b = st.text_input("Currency B (e.g. GBP)", value="GBP")
                rate_b_usd = st.number_input(f"{ccy_b}/USD rate", value=1.2700, format="%.4f", step=0.0001)

            if rate_b_usd > 0 and rate_a_usd > 0:
                cross = rate_a_usd / rate_b_usd
                st.markdown("---")
                st.markdown(f"""
                **Cross Rate Calculation:**
                ```
                {ccy_a}/USD = {rate_a_usd:.4f}
                {ccy_b}/USD = {rate_b_usd:.4f}

                {ccy_a}/{ccy_b} = {ccy_a}/USD ÷ {ccy_b}/USD
                          = {rate_a_usd:.4f} ÷ {rate_b_usd:.4f}
                          = {cross:.4f}

                Meaning: 1 {ccy_a} = {cross:.4f} {ccy_b}
                ```
                """)
                st.metric(f"{ccy_a}/{ccy_b} Cross Rate", f"{cross:.4f}")

        elif calc_choice == "💰 Pip Value Calculator":
            st.subheader("Pip Value Calculator")
            col1, col2, col3 = st.columns(3)
            with col1:
                rate = st.number_input("Exchange Rate", value=1.0850, format="%.4f")
            with col2:
                lot_type = st.selectbox("Lot Size", ["Standard (100,000)", "Mini (10,000)", "Micro (1,000)"])
            with col3:
                is_jpy_pv = st.checkbox("JPY pair?", key="jpy_pv")

            lot_map = {"Standard (100,000)": 100000, "Mini (10,000)": 10000, "Micro (1,000)": 1000}
            lot_size = lot_map[lot_type]
            pip_size = 0.01 if is_jpy_pv else 0.0001
            pip_val = (pip_size / rate) * lot_size

            st.markdown("---")
            st.markdown(f"""
            **Pip Value Calculation:**
            ```
            Pip Size:  {pip_size}
            Rate:      {rate:.4f}
            Lot Size:  {lot_size:,}

            Pip Value = ({pip_size} / {rate:.4f}) × {lot_size:,}
                      = {pip_size/rate:.8f} × {lot_size:,}
                      = {pip_val:.2f} quote currency per pip
            ```
            """)
            col1, col2 = st.columns(2)
            col1.metric("Pip Value", f"{pip_val:.2f} per pip")
            col2.metric("10-pip move P&L", f"{pip_val * 10:.2f}")

        elif calc_choice == "📈 Trade P&L Calculator":
            st.subheader("Trade Profit & Loss Calculator")
            col1, col2 = st.columns(2)
            with col1:
                direction = st.radio("Trade Direction", ["Long (BUY)", "Short (SELL)"])
                entry = st.number_input("Entry Rate", value=1.0850, format="%.4f", step=0.0001)
                exit_r = st.number_input("Exit Rate", value=1.0920, format="%.4f", step=0.0001)
            with col2:
                lots = st.number_input("Number of Lots", value=1.0, step=0.5, min_value=0.01)
                lot_sz = st.selectbox("Lot Type", ["Standard (100,000)", "Mini (10,000)", "Micro (1,000)"], key="pnl_lot")
                pip_size_pnl = 0.0001

            lot_map2 = {"Standard (100,000)": 100000, "Mini (10,000)": 10000, "Micro (1,000)": 1000}
            lot_units = lot_map2[lot_sz] * lots
            mult = 1 if "Long" in direction else -1
            pnl = (exit_r - entry) * lot_units * mult
            pips = (exit_r - entry) / pip_size_pnl * mult

            st.markdown("---")
            st.markdown(f"""
            **P&L Calculation:**
            ```
            Direction:   {direction}
            Entry:       {entry:.4f}
            Exit:        {exit_r:.4f}
            Move:        {pips:+.1f} pips
            Lot Size:    {lot_units:,.0f} units

            P&L = (Exit − Entry) × Units × Direction
                = ({exit_r:.4f} − {entry:.4f}) × {lot_units:,.0f} × {mult}
                = {pnl:,.2f} quote currency
            ```
            """)
            col1, col2, col3 = st.columns(3)
            col1.metric("P&L", f"{pnl:,.2f}")
            col2.metric("Pips", f"{pips:+.1f}")
            col3.metric("Result", "✅ Profit" if pnl > 0 else "❌ Loss")

        elif calc_choice == "🔄 Currency Converter":
            st.subheader("Currency Converter")
            col1, col2, col3 = st.columns(3)
            with col1:
                amount = st.number_input("Amount to Convert", value=10000.0, step=1000.0)
                from_ccy = st.text_input("From Currency", value="EUR")
            with col2:
                to_ccy = st.text_input("To Currency", value="USD")
                rate_conv = st.number_input(f"{from_ccy}/{to_ccy} rate", value=1.0850, format="%.4f")
            with col3:
                spread_conv = st.number_input("Spread (pips)", value=2.0, step=0.5)

            pip_size_conv = 0.0001
            mid_rate = rate_conv
            bid_rate = rate_conv - (spread_conv / 2) * pip_size_conv
            ask_rate = rate_conv + (spread_conv / 2) * pip_size_conv
            converted_bid = amount * bid_rate
            converted_ask = amount * ask_rate
            cost = (ask_rate - bid_rate) * amount

            st.markdown("---")
            st.markdown(f"""
            **Conversion Result:**
            ```
            Amount:     {amount:,.2f} {from_ccy}
            Mid Rate:   {mid_rate:.4f}
            Bid:        {bid_rate:.5f}  |  Ask: {ask_rate:.5f}

            If you SELL {from_ccy}: {converted_bid:,.2f} {to_ccy} (at bid)
            If you BUY  {from_ccy}: {converted_ask:,.2f} {to_ccy} (at ask)
            Spread Cost: {cost:,.2f} {to_ccy}
            ```
            """)
            col1, col2 = st.columns(2)
            col1.metric(f"Sell {from_ccy} → Receive {to_ccy}", f"{converted_bid:,.2f}")
            col2.metric(f"Buy {from_ccy} → Pay {to_ccy}", f"{converted_ask:,.2f}")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("FX Market Share by Currency Pair")
        pairs = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'USD/CAD', 'USD/CHF', 'USD/CNY', 'Other']
        shares = [23.0, 13.5, 9.6, 5.4, 5.0, 4.7, 3.8, 35.0]
        fig_pie = go.Figure(go.Pie(
            labels=pairs, values=shares, hole=0.4,
            marker=dict(colors=px.colors.qualitative.Set2),
            textinfo='label+percent'
        ))
        fig_pie.update_layout(title='Global FX Market Share by Currency Pair (BIS 2022)')
        st.plotly_chart(fig_pie, use_container_width=True)

        st.subheader("Typical Bid-Ask Spreads by Pair")
        spread_pairs = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'AUD/USD', 'EUR/GBP', 'USD/MXN', 'USD/ZAR', 'USD/TRY']
        spread_vals = [0.5, 0.8, 0.6, 1.0, 1.2, 20.0, 45.0, 35.0]
        colors_spread = ['#2ECC71' if s < 5 else '#E67E22' if s < 20 else '#E74C3C' for s in spread_vals]
        fig_spread = go.Figure(go.Bar(
            x=spread_pairs, y=spread_vals, marker_color=colors_spread,
            text=[f'{s} pips' for s in spread_vals], textposition='outside'
        ))
        fig_spread.update_layout(
            title='Typical Retail Bid-Ask Spreads (pips)',
            xaxis_title='Currency Pair', yaxis_title='Spread (pips)',
            yaxis_type='log'
        )
        st.plotly_chart(fig_spread, use_container_width=True)

        st.subheader("Trading Session Liquidity")
        sessions = ['Sydney\n(10PM-7AM GMT)', 'Tokyo\n(12AM-9AM GMT)', 'London\n(7AM-4PM GMT)', 'New York\n(12PM-9PM GMT)']
        volumes = [4, 6, 38, 19]
        overlap = ['No', 'No', 'Peak overlap\n12-4PM GMT', 'Peak overlap\n12-4PM GMT']
        fig_sess = go.Figure(go.Bar(
            x=sessions, y=volumes,
            marker_color=['#AED6F1', '#85C1E9', '#2E86C1', '#1A5276'],
            text=[f'{v}%' for v in volumes], textposition='outside'
        ))
        fig_sess.update_layout(
            title='FX Volume by Trading Session (% of daily volume)',
            xaxis_title='Trading Session', yaxis_title='% of Daily Volume'
        )
        st.plotly_chart(fig_sess, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding of FX Foundations")

        st.markdown("**1. EUR/USD is quoted as 1.0845 / 1.0847. What is the spread in pips?**")
        q1 = st.radio("Select your answer:", ["1 pip", "2 pips", "3 pips", "0.5 pips"], key="fx1q1")
        if st.button("Check Answer", key="fx1c1"):
            if q1 == "2 pips":
                st.success("✅ Correct! Spread = Ask − Bid = 1.0847 − 1.0845 = 0.0002 = 2 pips.")
            else:
                st.error("❌ Incorrect. Spread = 1.0847 − 1.0845 = 0.0002. Divide by 0.0001 per pip = 2 pips.")
        st.markdown("---")

        st.markdown("**2. USD/JPY = 149.50 and USD/CHF = 0.9050. What is the CHF/JPY cross rate?**")
        q2 = st.radio("Select your answer:", ["135.25", "165.19", "0.00605", "170.10"], key="fx1q2")
        if st.button("Check Answer", key="fx1c2"):
            if q2 == "165.19":
                st.success("✅ Correct! CHF/JPY = USD/JPY ÷ USD/CHF = 149.50 / 0.9050 = 165.19")
            else:
                st.error("❌ Incorrect. CHF/JPY = USD/JPY ÷ USD/CHF = 149.50 / 0.9050 = 165.19")
        st.markdown("---")

        st.markdown("**3. You BUY EUR/USD at 1.0850 and close at 1.0900. Standard lot. What is your P&L?**")
        q3 = st.radio("Select your answer:", ["$500 profit", "$500 loss", "$50 profit", "$5,000 profit"], key="fx1q3")
        if st.button("Check Answer", key="fx1c3"):
            if q3 == "$500 profit":
                st.success("✅ Correct! P&L = (1.0900 − 1.0850) × 100,000 = 0.005 × 100,000 = $500 profit.")
            else:
                st.error("❌ Incorrect. P&L = (1.0900 − 1.0850) × 100,000 = $500 profit.")
        st.markdown("---")

        st.markdown("**4. Which is the BASE currency in GBP/USD?**")
        q4 = st.radio("Select your answer:", ["USD", "GBP", "Both", "Neither"], key="fx1q4")
        if st.button("Check Answer", key="fx1c4"):
            if q4 == "GBP":
                st.success("✅ Correct! In BASE/QUOTE notation, the first currency is always the base. GBP is the base.")
            else:
                st.error("❌ Incorrect. In BASE/QUOTE (GBP/USD), GBP is the base currency.")
        st.markdown("---")

        st.markdown("**5. EUR/USD pip value on a standard lot at rate 1.0850 is approximately:**")
        q5 = st.radio("Select your answer:", ["$9.22", "$10.00", "$0.92", "$92.20"], key="fx1q5")
        if st.button("Check Answer", key="fx1c5"):
            if q5 == "$9.22":
                st.success("✅ Correct! Pip Value = (0.0001 / 1.0850) × 100,000 = $9.22 per pip.")
            else:
                st.error("❌ Incorrect. Pip Value = (0.0001 / 1.0850) × 100,000 = $9.22 per pip.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")

        st.markdown("""
        ### 1. The FX Market
        - Largest financial market: ~$7.5 trillion daily turnover
        - OTC, decentralised, operates 24 hours/5 days per week
        - Key participants: Central banks, commercial banks, corporations, hedge funds, retail traders

        ### 2. Currency Pair Conventions
        - Written as **BASE/QUOTE** — e.g. EUR/USD = 1.0850 means 1 EUR costs 1.0850 USD
        - **Direct quote**: price of 1 foreign unit in domestic currency
        - **Indirect quote**: its exact reciprocal
        - Direct × Indirect = 1

        ### 3. Bid, Ask, and Spread
        - **Bid**: market maker buys base (you sell at bid)
        - **Ask**: market maker sells base (you buy at ask)
        - **Spread** = Ask − Bid = dealer's margin
        - Spreads are tighter for liquid pairs (EUR/USD ~0.5 pip) vs EM pairs (USD/ZAR ~45 pips)

        ### 4. Pip Arithmetic
        ```
        1 pip = 0.0001 for most pairs | 0.01 for JPY pairs
        Pip Value = (Pip Size / Rate) × Lot Size
        Standard Lot = 100,000 units
        ```

        ### 5. Cross Rates
        ```
        Cross Rate (A/C) = Rate(A/B) × Rate(B/C)
        EUR/JPY = EUR/USD × USD/JPY = 1.0850 × 149.50 = 162.21
        ```

        ### 6. Key Formulas
        ```
        Spread (pips)  = (Ask − Bid) / Pip Size
        Spread (%)     = (Ask − Bid) / Ask × 100
        Pip Value      = (Pip Size / Rate) × Lot Size
        P&L (Long)     = (Exit − Entry) × Lot Size
        P&L (Short)    = (Entry − Exit) × Lot Size
        Cross Rate     = Rate(A/B) × Rate(B/C)
        ```
        """)

        st.subheader("📌 Quick Reference")
        ref = {
            "Concept": ["Major pair spread", "JPY pip size", "Standard lot", "Cross rate formula", "Direct × Indirect"],
            "Value / Formula": ["0.5–2 pips", "0.01 (2nd decimal)", "100,000 base units", "A/C = A/B × B/C", "= 1 (always)"],
            "Example": ["EUR/USD 0.5 pip", "USD/JPY 149.50 → 149.51", "EUR/USD 100,000 EUR", "EUR/JPY = 1.0850 × 149.50", "1.0850 × 0.9217 ≈ 1"]
        }
        st.dataframe(pd.DataFrame(ref), use_container_width=True, hide_index=True)

        st.success("🎓 **You've completed Module 1!** You now understand the structure of the FX market and can read any FX quote, calculate spreads, pip values, cross rates, and trade P&L.")
        st.info("💡 **Next Steps**: Proceed to Module 2 — FX Market Infrastructure to learn about trading sessions, settlement, SWIFT, and nostro/vostro accounts.")

if __name__ == "__main__":
    show()