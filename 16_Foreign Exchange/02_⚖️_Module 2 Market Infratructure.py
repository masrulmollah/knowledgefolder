import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import datetime

def show():
    st.title("🏦 Module 2: FX Market Infrastructure")
    st.markdown("*Master trading sessions, T+2 settlement, SWIFT messaging, nostro/vostro accounts, and order types*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Global Trading Sessions")
        st.markdown("""
        FX markets operate **24 hours a day, 5 days a week** across overlapping geographic sessions.
        Understanding session timing is critical for knowing when spreads are tightest and liquidity is highest.
        """)
        sessions_data = {
            "Session": ["Sydney", "Tokyo", "London", "New York"],
            "Open (GMT)": ["10:00 PM Sun", "12:00 AM Mon", "7:00 AM", "12:00 PM (Noon)"],
            "Close (GMT)": ["7:00 AM", "9:00 AM", "4:00 PM", "9:00 PM"],
            "Most Active Pairs": ["AUD, NZD", "JPY, AUD, NZD", "EUR, GBP, CHF", "USD, CAD, MXN"],
            "Approx. Volume": ["~4%", "~6%", "~38%", "~19%"],
            "Key Feature": ["Opens week; thin liquidity", "BoJ influence on JPY", "Largest session; tightest spreads", "USD dominates; London-NY overlap is peak"]
        }
        st.dataframe(pd.DataFrame(sessions_data), use_container_width=True, hide_index=True)
        st.markdown("""
        **London–New York Overlap (12:00–16:00 GMT):** This 4-hour window accounts for the highest daily
        volume and tightest spreads. Most major economic data releases are scheduled during this window.
        """)

        st.subheader("2. FX Settlement — T+2")
        st.markdown("""
        **Standard spot FX** settles on **T+2** — two business days after the trade date.

        | Convention | Pairs | Why |
        |-----------|-------|-----|
        | **T+2** | EUR/USD, GBP/USD, EUR/JPY, most pairs | Standard global convention |
        | **T+1** | USD/CAD, USD/TRY, USD/RUB | North American / regional convention |
        | **T+0 (Same day)** | Any pair (at premium) | Special "cash" settlement, wider spread |

        ```
        Example: Trade executed Monday 14 April
        T+1 = Tuesday 15 April
        T+2 = Wednesday 16 April  ← Settlement Date (Value Date)

        If trade date is Thursday: T+2 skips weekend → settles Tuesday
        ```

        **Settlement Risk (Herstatt Risk):** The risk that one counterparty pays its leg but the other
        defaults before paying the opposite leg. Named after Bankhaus Herstatt (1974 collapse).
        Eliminated by **CLS Bank** through Payment-vs-Payment (PvP) settlement.
        """)

        st.subheader("3. Nostro & Vostro Accounts")
        st.markdown("""
        FX settlement requires **pre-funded accounts** at correspondent banks in each currency:

        | Term | Meaning | Example |
        |------|---------|---------|
        | **Nostro** | "Our account at YOUR bank" | HSBC London holds a USD account at Citi New York |
        | **Vostro** | "YOUR account at our bank" | Citi's view of that same HSBC account |

        **How settlement works:**
        1. Bank A buys EUR / sells USD from Bank B
        2. Bank A's EUR nostro account at a Frankfurt bank is credited with EUR
        3. Bank A's USD nostro account at a New York bank is debited with USD
        4. Bank B's accounts are credited/debited in reverse

        Treasury teams **monitor nostro balances daily** to ensure sufficient funds to meet settlement
        obligations — shortfalls cause failed trades and regulatory penalties.
        """)

        st.subheader("4. SWIFT Messaging")
        st.markdown("""
        **SWIFT** (Society for Worldwide Interbank Financial Telecommunication) is the **messaging network**
        used to instruct cross-border payments and confirm FX trades. SWIFT moves *instructions*, not funds.

        | Message Type | Purpose |
        |-------------|---------|
        | **MT300** | FX trade confirmation between counterparties |
        | **MT103** | Single customer credit transfer (payment instruction) |
        | **MT202** | Bank-to-bank fund transfer instruction |
        | **MT940** | Account statement (nostro reconciliation) |

        Banks are migrating to **ISO 20022** (SWIFT gpi) — richer data, faster tracking,
        and real-time payment status updates replacing legacy MT messages.
        """)

        st.subheader("5. Order Types in FX")
        order_data = {
            "Order Type": ["Market Order", "Limit Order", "Stop Order", "Stop-Limit Order", "OCO (One-Cancels-Other)", "Good Till Cancelled (GTC)"],
            "How It Works": [
                "Executes immediately at best available price",
                "Executes only at your specified price or better",
                "Becomes a market order when trigger price is reached",
                "Becomes a limit order (not market) at the trigger price",
                "Two orders — when one fills, the other cancels automatically",
                "Remains active until filled or manually cancelled"
            ],
            "Best Used For": [
                "Urgency — guaranteed fill, price uncertainty",
                "Buying dips or selling rallies at target price",
                "Stop-loss (limit losses) or breakout entry",
                "Breakout entry with price control; risk of non-fill",
                "Bracket trading: profit target + stop loss together",
                "Setting-and-forgetting orders around key levels"
            ]
        }
        st.dataframe(pd.DataFrame(order_data), use_container_width=True, hide_index=True)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Calculating the Settlement Value Date")
        st.markdown("""
        **Scenario:** A EUR/USD trade is executed on **Wednesday, 9 April 2025**.

        ```
        Trade Date:      Wednesday 9 April 2025
        T+1:             Thursday 10 April 2025
        T+2 (Value Date): Friday 11 April 2025

        If 10 April is a public holiday in the US or Eurozone:
        T+1 = Friday 11 April
        T+2 = Monday 14 April  (skip weekend)
        ```
        Key rule: Skip **weekends** and **bank holidays** in BOTH currency countries.
        """)

        st.subheader("Example 2: Nostro Account Daily Management")
        st.markdown("""
        **Scenario:** HSBC Singapore's USD nostro account at Citi New York

        ```
        Opening balance (Monday morning):    USD 45,000,000

        Inflows today:
          + Client USD payment received:      +12,500,000
          + USD FX swap near leg:             + 8,000,000

        Outflows today:
          − USD FX spot settlement:          −18,000,000
          − USD commercial payment sent:     − 5,750,000
          − USD bond coupon payment:         − 3,200,000
        ────────────────────────────────────────────────
        Projected closing balance:           USD 38,550,000

        Required minimum buffer:             USD 10,000,000
        Status: ✅ Adequate
        ```
        If projected balance < minimum, treasury must arrange **intraday repo** or **borrow from
        parent** to pre-fund the shortfall before settlement cut-off (typically 5:00 PM NY time).
        """)

        st.subheader("Example 3: Herstatt Risk and CLS Solution")
        st.markdown("""
        **The Herstatt Problem (1974):**
        ```
        Step 1: Deutsche Bank pays DEM 10M to Bankhaus Herstatt at 10:30 AM Frankfurt time
        Step 2: Herstatt should pay USD to Deutsche Bank at 2:30 PM New York time
        Step 3: German regulators close Herstatt at 3:30 PM Frankfurt = 9:30 AM New York
        Step 4: Herstatt received DEM but Deutsche Bank never received USD
        Result: Deutsche Bank lost its full DEM 10M — pure settlement risk
        ```

        **CLS Bank Solution (launched 2002):**
        ```
        Both payment legs are linked — CLS only releases payment A when it confirms
        payment B is also available. If either party cannot pay, NEITHER payment settles.
        Result: Principal (settlement) risk is completely eliminated.

        CLS settles ~$6.5 trillion per day across 18+ currencies.
        ```
        """)

        st.subheader("Example 4: SWIFT MT300 FX Confirmation")
        st.markdown("""
        After every FX trade, both counterparties exchange an **MT300** confirmation:

        ```
        Field 30T: Trade Date         20250409
        Field 30V: Value Date         20250411
        Field 36:  Exchange Rate      1.08500
        Field 32B: Currency/Amount Sold   USD  5,425,000.00
        Field 33B: Currency/Amount Bought EUR  5,000,000.00
        Field 57A: Counterparty Bank  //CITIGB2LXXX  CITIBANK LONDON

        Both counterparties must match fields — mismatches → failed settlement
        ```
        """)

    with tab3:
        st.header("Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "📅 Settlement Date Calculator",
            "💼 Nostro Balance Manager",
            "⏰ Trading Session Finder",
            "📋 Order Cost Estimator"
        ])
        st.markdown("---")

        if calc_choice == "📅 Settlement Date Calculator":
            st.subheader("FX Settlement Value Date Calculator")
            col1, col2 = st.columns(2)
            with col1:
                trade_date = st.date_input("Trade Date", value=datetime.date.today())
                pair_type = st.selectbox("Currency Pair", [
                    "EUR/USD (T+2)", "GBP/USD (T+2)", "USD/JPY (T+2)",
                    "EUR/JPY (T+2)", "USD/CAD (T+1)", "USD/TRY (T+1)"
                ])
            with col2:
                holiday1 = st.date_input("Holiday 1 (optional — enter same date to skip)", value=trade_date)
                holiday2 = st.date_input("Holiday 2 (optional — enter same date to skip)", value=trade_date)

            settlement_days = 1 if "T+1" in pair_type else 2
            holidays = set()
            if holiday1 != trade_date:
                holidays.add(holiday1)
            if holiday2 != trade_date:
                holidays.add(holiday2)

            val_date = trade_date
            added = 0
            while added < settlement_days:
                val_date += datetime.timedelta(days=1)
                if val_date.weekday() < 5 and val_date not in holidays:
                    added += 1

            st.markdown("---")
            st.markdown(f"""
            **Settlement Calculation:**
            ```
            Trade Date:       {trade_date.strftime('%A, %d %B %Y')}
            Convention:       {pair_type.split('(')[1].replace(')', '')}
            Holidays Applied: {len(holidays)}
            ───────────────────────────────────────────────
            Value Date:       {val_date.strftime('%A, %d %B %Y')}
            Days from trade:  {(val_date - trade_date).days} calendar days
            ```
            """)
            col1, col2 = st.columns(2)
            col1.metric("Trade Date", trade_date.strftime('%d %b %Y'))
            col2.metric("Value Date (Settlement)", val_date.strftime('%d %b %Y'))

        elif calc_choice == "💼 Nostro Balance Manager":
            st.subheader("Nostro Account Intraday Balance Manager")
            opening = st.number_input("Opening Nostro Balance (USD)", value=50000000.0, step=1000000.0)
            min_buffer = st.number_input("Minimum Required Buffer (USD)", value=10000000.0, step=1000000.0)
            st.markdown("**Enter today's expected flows:**")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Inflows (+)**")
                inflow1 = st.number_input("Client USD receipts", value=12500000.0, step=500000.0)
                inflow2 = st.number_input("FX swap near leg inflow", value=8000000.0, step=500000.0)
                inflow3 = st.number_input("Other inflows", value=0.0, step=500000.0)
            with col2:
                st.markdown("**Outflows (−)**")
                outflow1 = st.number_input("FX spot settlements", value=18000000.0, step=500000.0)
                outflow2 = st.number_input("Commercial payments", value=5750000.0, step=500000.0)
                outflow3 = st.number_input("Other outflows", value=3200000.0, step=500000.0)

            total_in = inflow1 + inflow2 + inflow3
            total_out = outflow1 + outflow2 + outflow3
            closing = opening + total_in - total_out
            net_flow = total_in - total_out
            buffer_gap = closing - min_buffer

            st.markdown("---")
            st.markdown(f"""
            **Nostro Position Summary:**
            ```
            Opening Balance:      ${opening:>15,.2f}
            Total Inflows:       +${total_in:>15,.2f}
            Total Outflows:      −${total_out:>15,.2f}
            ──────────────────────────────────────────
            Projected Closing:    ${closing:>15,.2f}
            Minimum Buffer:       ${min_buffer:>15,.2f}
            Buffer Gap:          {'+' if buffer_gap >= 0 else ''} ${buffer_gap:>14,.2f}
            ```
            """)
            col1, col2, col3 = st.columns(3)
            col1.metric("Projected Closing", f"${closing:,.0f}", f"${net_flow:+,.0f}")
            col2.metric("Min Buffer", f"${min_buffer:,.0f}")
            col3.metric("Buffer Surplus/Deficit", f"${buffer_gap:+,.0f}")
            if closing < 0:
                st.error("🚨 OVERDRAFT! Arrange emergency intraday credit immediately.")
            elif closing < min_buffer:
                st.warning(f"⚠️ Below minimum buffer by ${abs(buffer_gap):,.0f}. Pre-position funds before cut-off.")
            else:
                st.success(f"✅ Adequate liquidity. Buffer surplus: ${buffer_gap:,.0f}")

        elif calc_choice == "⏰ Trading Session Finder":
            st.subheader("Current Trading Session Finder")
            st.markdown("Enter a GMT time to see which sessions are active and typical spread conditions.")
            gmt_hour = st.slider("GMT Hour (0–23)", 0, 23, 12)
            gmt_min = st.slider("GMT Minute", 0, 59, 0)
            gmt_time = gmt_hour + gmt_min / 60

            sessions_active = []
            if 22 <= gmt_time or gmt_time < 7:
                sessions_active.append("🇦🇺 Sydney (thin liquidity, AUD/NZD most active)")
            if 0 <= gmt_time < 9:
                sessions_active.append("🇯🇵 Tokyo (JPY most active, ~6% of volume)")
            if 7 <= gmt_time < 16:
                sessions_active.append("🇬🇧 London (EUR/GBP most active, ~38% of volume, TIGHTEST spreads)")
            if 12 <= gmt_time < 21:
                sessions_active.append("🇺🇸 New York (USD most active, ~19% of volume)")

            overlap = 12 <= gmt_time < 16
            st.markdown("---")
            if sessions_active:
                st.markdown(f"**Active sessions at {gmt_hour:02d}:{gmt_min:02d} GMT:**")
                for s in sessions_active:
                    st.markdown(f"  ✅ {s}")
                if overlap:
                    st.success("🔥 London–New York OVERLAP — Peak liquidity! Tightest spreads of the day.")
                elif "London" in " ".join(sessions_active):
                    st.info("📊 London session active — high liquidity, competitive spreads.")
                else:
                    st.warning("💤 Low liquidity period — expect wider spreads and thinner order books.")
            else:
                st.error("🔴 All major sessions closed — weekend hours.")

        elif calc_choice == "📋 Order Cost Estimator":
            st.subheader("Order Type & Execution Cost Estimator")
            col1, col2 = st.columns(2)
            with col1:
                order_size = st.number_input("Order Size (base currency units)", value=1000000.0, step=100000.0)
                order_type = st.selectbox("Order Type", ["Market Order", "Limit Order", "Stop Order"])
                session = st.selectbox("Trading Session", ["London (peak)", "London-NY Overlap (peak)", "New York", "Tokyo", "Sydney (off-hours)"])
            with col2:
                pair = st.selectbox("Currency Pair", ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/MXN"])
                rate = st.number_input("Current Market Rate", value=1.0850, format="%.4f")

            spread_map = {
                "EUR/USD": {"London (peak)": 0.5, "London-NY Overlap (peak)": 0.4, "New York": 0.7, "Tokyo": 1.2, "Sydney (off-hours)": 2.0},
                "GBP/USD": {"London (peak)": 0.8, "London-NY Overlap (peak)": 0.7, "New York": 1.0, "Tokyo": 2.0, "Sydney (off-hours)": 3.0},
                "USD/JPY": {"London (peak)": 0.6, "London-NY Overlap (peak)": 0.5, "New York": 0.8, "Tokyo": 0.5, "Sydney (off-hours)": 1.5},
                "AUD/USD": {"London (peak)": 1.0, "London-NY Overlap (peak)": 0.9, "New York": 1.2, "Tokyo": 1.0, "Sydney (off-hours)": 1.5},
                "USD/MXN": {"London (peak)": 20.0, "London-NY Overlap (peak)": 18.0, "New York": 22.0, "Tokyo": 35.0, "Sydney (off-hours)": 50.0},
            }
            slip_map = {"Market Order": 0.5, "Limit Order": 0.0, "Stop Order": 1.0}

            spread = spread_map[pair][session]
            slippage = slip_map[order_type]
            total_cost_pips = spread + slippage
            total_cost_usd = (total_cost_pips * 0.0001) * order_size

            st.markdown("---")
            st.markdown(f"""
            **Execution Cost Estimate:**
            ```
            Pair:           {pair}
            Session:        {session}
            Order Type:     {order_type}
            Order Size:     {order_size:,.0f} base units
            ─────────────────────────────────────────
            Spread:         {spread:.1f} pips
            Slippage est.:  {slippage:.1f} pips
            Total Cost:     {total_cost_pips:.1f} pips = {total_cost_usd:,.2f} quote currency
            ```
            """)
            col1, col2, col3 = st.columns(3)
            col1.metric("Spread", f"{spread:.1f} pips")
            col2.metric("Est. Slippage", f"{slippage:.1f} pips")
            col3.metric("Total Cost", f"{total_cost_usd:,.2f}")

    with tab4:
        st.header("Visualizations")

        st.subheader("FX Market Volume by Financial Centre")
        centres = ['London', 'New York', 'Singapore', 'Hong Kong', 'Tokyo', 'Zurich', 'Frankfurt', 'Other']
        vols = [38.1, 19.4, 9.6, 7.6, 4.5, 4.0, 3.0, 13.8]
        fig_bar = go.Figure(go.Bar(
            x=centres, y=vols,
            marker_color=['#2E86C1', '#E74C3C', '#27AE60', '#E67E22', '#8E44AD', '#1ABC9C', '#F39C12', '#95A5A6'],
            text=[f'{v}%' for v in vols], textposition='outside'
        ))
        fig_bar.update_layout(title='FX Volume by Financial Centre (% of Global Daily Volume)',
                              xaxis_title='Centre', yaxis_title='Share (%)')
        st.plotly_chart(fig_bar, use_container_width=True)

        st.subheader("Daily Volume by Instrument")
        instruments = ['FX Swaps', 'Spot', 'Outright Forwards', 'Currency Swaps', 'Options & Other']
        vol_instr = [3.8, 2.1, 1.1, 0.9, 0.3]
        fig_inst = go.Figure(go.Pie(labels=instruments, values=vol_instr, hole=0.35,
                                   marker=dict(colors=px.colors.qualitative.Pastel)))
        fig_inst.update_layout(title='FX Instruments Share of Daily Turnover ($T)')
        st.plotly_chart(fig_inst, use_container_width=True)

        st.subheader("Trading Session Overlap Timeline")
        fig_sess = go.Figure()
        session_data = [
            ("Sydney", 22, 7, "#AED6F1"),
            ("Tokyo", 24, 33, "#85C1E9"),
            ("London", 31, 40, "#2E86C1"),
            ("New York", 36, 45, "#1A5276"),
        ]
        for sess, start, end, color in session_data:
            x_vals = [s % 24 for s in range(start, end + 1)]
            fig_sess.add_trace(go.Scatter(
                x=x_vals, y=[sess] * len(x_vals),
                mode='lines', line=dict(color=color, width=20),
                name=sess
            ))
        fig_sess.update_layout(
            title='FX Trading Sessions — 24-Hour Timeline (GMT)',
            xaxis=dict(title='GMT Hour', tickvals=list(range(0, 24, 2)),
                       ticktext=[f'{h:02d}:00' for h in range(0, 24, 2)]),
            yaxis_title='Session', height=280
        )
        st.plotly_chart(fig_sess, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding of FX Market Infrastructure")

        st.markdown("**1. Standard spot FX settlement is:**")
        q1 = st.radio("Select:", ["T+1", "T+2", "T+3", "Same day"], key="fx2q1")
        if st.button("Check Answer", key="fx2c1"):
            if q1 == "T+2":
                st.success("✅ Correct! Most FX pairs settle T+2. Exceptions: USD/CAD and USD/TRY settle T+1.")
            else:
                st.error("❌ Incorrect. Standard spot FX settlement is T+2 (two business days after trade date).")
        st.markdown("---")

        st.markdown("**2. Herstatt Risk refers to:**")
        q2 = st.radio("Select:", [
            "Currency mismatch risk in a portfolio",
            "The risk one party pays its leg but the counterparty defaults before paying",
            "Central bank intervention risk",
            "The risk of wide spreads during off-hours"
        ], key="fx2q2")
        if st.button("Check Answer", key="fx2c2"):
            if "counterparty defaults" in q2:
                st.success("✅ Correct! Herstatt risk is settlement/principal risk from time-zone gaps between payment legs.")
            else:
                st.error("❌ Incorrect. Herstatt risk: one party pays first, counterparty defaults before paying the other leg.")
        st.markdown("---")

        st.markdown("**3. A Nostro account is:**")
        q3 = st.radio("Select:", [
            "Our account held at a foreign correspondent bank",
            "A foreign bank's account held at our bank",
            "A settlement account at CLS Bank",
            "An escrow account for disputed trades"
        ], key="fx2q3")
        if st.button("Check Answer", key="fx2c3"):
            if "foreign correspondent bank" in q3:
                st.success("✅ Correct! Nostro = 'our money at your bank' — our account held at a foreign bank.")
            else:
                st.error("❌ Incorrect. Nostro = our account at a foreign bank in the foreign currency.")
        st.markdown("---")

        st.markdown("**4. The SWIFT MT300 message is used for:**")
        q4 = st.radio("Select:", [
            "Customer credit transfers",
            "Bank-to-bank fund transfers",
            "FX trade confirmations",
            "Account statements"
        ], key="fx2q4")
        if st.button("Check Answer", key="fx2c4"):
            if "FX trade confirmations" in q4:
                st.success("✅ Correct! MT300 is the SWIFT message type for confirming FX transactions between counterparties.")
            else:
                st.error("❌ Incorrect. MT300 = FX trade confirmation. MT103 = customer payment. MT940 = account statement.")
        st.markdown("---")

        st.markdown("**5. The London–New York session overlap occurs approximately:**")
        q5 = st.radio("Select:", [
            "7:00 AM – 10:00 AM GMT",
            "12:00 PM – 4:00 PM GMT",
            "4:00 PM – 9:00 PM GMT",
            "10:00 PM – 2:00 AM GMT"
        ], key="fx2q5")
        if st.button("Check Answer", key="fx2c5"):
            if "12:00 PM – 4:00 PM" in q5:
                st.success("✅ Correct! London opens 7AM, New York opens 12PM. Overlap is 12PM–4PM GMT — peak global FX liquidity.")
            else:
                st.error("❌ Incorrect. London (7AM–4PM GMT) and New York (12PM–9PM GMT) overlap from 12PM–4PM GMT.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")

        st.markdown("""
        ### 1. Trading Sessions
        - FX trades 24/5 across Sydney → Tokyo → London → New York
        - **London (~38%)** is the largest session — tightest spreads
        - **London–NY overlap (12–16:00 GMT)** = peak liquidity and price discovery

        ### 2. T+2 Settlement
        - Most FX pairs settle **two business days** after trade date
        - USD/CAD and USD/TRY settle **T+1**
        - Skip weekends AND bank holidays in both countries
        - Pre-fund nostro accounts before settlement cut-off to avoid failed trades

        ### 3. Nostro / Vostro
        - **Nostro** = our account at a foreign bank (in foreign currency)
        - **Vostro** = their account at our bank
        - Treasury monitors nostro positions daily — shortfalls cause failed settlements

        ### 4. SWIFT Messaging
        - SWIFT sends **instructions**, not funds
        - **MT300** = FX confirmation | **MT103** = customer payment | **MT202** = bank transfer
        - Migrating to ISO 20022 (SWIFT gpi) for richer data

        ### 5. Herstatt Risk & CLS
        - Herstatt risk: time-zone gap allows default between payment legs
        - **CLS Bank** eliminates it via **Payment-vs-Payment (PvP)**
        - ~$6.5 trillion settled via CLS daily across 18+ currencies

        ### 6. Order Types
        ```
        Market Order    = immediate fill, no price guarantee
        Limit Order     = fill at target price or better
        Stop Order      = trigger at price, then market fill
        OCO             = profit target + stop loss combined
        ```

        ### Key Formula
        ```
        Settlement Date = Trade Date + 2 business days (T+2)
                         (exclude weekends + holidays in both countries)
        ```
        """)

        st.subheader("📌 Quick Reference")
        ref = {
            "Topic": ["Settlement (most pairs)", "Settlement (USD/CAD)", "London session volume", "SWIFT FX confirmation", "CLS protects against"],
            "Answer": ["T+2", "T+1", "~38% of global volume", "MT300", "Herstatt / settlement risk"],
            "Key Rule": ["Skip weekends + holidays", "North American convention", "Tightest spreads here", "Both parties must match", "PvP — both legs or neither"]
        }
        st.dataframe(pd.DataFrame(ref), use_container_width=True, hide_index=True)

        st.success("🎓 **You've completed Module 2!** You understand FX settlement mechanics, nostro management, SWIFT messaging, and trading session dynamics.")
        st.info("💡 **Next Steps**: Proceed to Module 3 — Exchange Rate Theories to learn PPP, Interest Rate Parity, and the Fisher Effect.")

if __name__ == "__main__":
    show()