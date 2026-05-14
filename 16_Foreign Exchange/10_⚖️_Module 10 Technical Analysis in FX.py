import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📈 Module 10: Technical Analysis in FX")
    st.markdown("*Master chart patterns, trend analysis, RSI, MACD, Fibonacci retracement, Bollinger Bands, and Elliott Wave*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Support & Resistance")
        st.markdown("""
        **Support** is a price level where buying interest consistently prevents further decline.
        **Resistance** is a price level where selling pressure consistently caps advances.

        | Concept | Definition | Practical Use |
        |---------|-----------|--------------|
        | **Support** | Floor — buyers step in to defend this level | Place buy orders above support; stop-loss below |
        | **Resistance** | Ceiling — sellers emerge at this level | Place sell orders below resistance; stop-loss above |
        | **Role Reversal** | Broken resistance becomes support (and vice versa) | One of the most reliable technical principles |
        | **Round Numbers** | 1.1000, 1.2000 etc. act as psychological S&R | Major central bank levels often coincide |

        ```
        Strength of S&R increases when:
        - Level has been tested multiple times
        - High volume occurred at that level historically
        - Coincides with a Fibonacci level or moving average
        - Long time since the level was last tested
        ```
        """)

        st.subheader("2. Moving Averages")
        st.markdown("""
        Moving averages **smooth price data** to identify trend direction.

        | Type | Calculation | Sensitivity | Best Used For |
        |------|------------|-------------|---------------|
        | **SMA (Simple)** | Average of last N closes | Slow | Identifying major trend direction |
        | **EMA (Exponential)** | Weighted — recent prices count more | Fast | Shorter-term trend following |
        | **WMA (Weighted)** | Linear weighting | Medium | Balanced trend signals |

        **Key Signals:**
        ```
        Golden Cross:   50-day MA crosses ABOVE 200-day MA  → Bullish long-term signal
        Death Cross:    50-day MA crosses BELOW 200-day MA  → Bearish long-term signal
        Price > 200MA:  Long-term uptrend confirmed
        Price < 200MA:  Long-term downtrend confirmed
        ```

        **MAs are LAGGING indicators** — they confirm trends after they have started.
        Use them for trend confirmation, not entry timing.
        """)

        st.subheader("3. RSI — Relative Strength Index")
        st.markdown("""
        **RSI** is a momentum oscillator (range 0–100) measuring the speed and change of price moves.

        ```
        RSI = 100 - [100 / (1 + RS)]
        RS  = Average Gain over N periods / Average Loss over N periods
        Standard period: N = 14
        ```

        | RSI Level | Signal | Interpretation |
        |-----------|--------|----------------|
        | **> 70** | Overbought | Potential reversal lower — consider taking profits |
        | **50–70** | Bullish momentum | Trend continuing upward |
        | **30–50** | Bearish momentum | Trend continuing downward |
        | **< 30** | Oversold | Potential reversal higher — consider buying |

        **RSI Divergence (most powerful signal):**
        - **Bearish divergence:** Price makes new HIGH but RSI makes LOWER high → weakness warning
        - **Bullish divergence:** Price makes new LOW but RSI makes HIGHER low → strength building
        """)

        st.subheader("4. MACD — Moving Average Convergence Divergence")
        st.markdown("""
        **MACD** is a trend-following momentum indicator showing the relationship between two EMAs.

        ```
        MACD Line    = EMA(12) - EMA(26)
        Signal Line  = EMA(9) of MACD Line
        Histogram    = MACD Line - Signal Line
        ```

        | Signal | Condition | Action |
        |--------|-----------|--------|
        | **Bullish crossover** | MACD crosses ABOVE Signal Line | Buy signal |
        | **Bearish crossover** | MACD crosses BELOW Signal Line | Sell signal |
        | **Zero line cross (bullish)** | MACD crosses ABOVE zero | Trend turning positive |
        | **Zero line cross (bearish)** | MACD crosses BELOW zero | Trend turning negative |
        | **Histogram expanding** | Bar getting taller | Momentum increasing |
        | **Histogram shrinking** | Bar getting shorter | Momentum fading — potential reversal |
        """)

        st.subheader("5. Fibonacci Retracement")
        st.markdown("""
        **Fibonacci retracement** uses the mathematical Fibonacci sequence ratios to identify
        potential support and resistance levels after a significant price move.

        ```
        Key Fibonacci Retracement Levels:
        23.6%  — Shallow retracement (strong trend)
        38.2%  — Moderate retracement
        50.0%  — Psychological level (not true Fibonacci but widely watched)
        61.8%  — The Golden Ratio (1/phi = 0.618) — MOST significant level
        78.6%  — Deep retracement (trend in doubt)

        Formula:
        Retracement Level = High - (High - Low) x Fibonacci Ratio
        ```

        The **61.8% Golden Ratio** is the most significant because it appears throughout
        nature and financial markets. A bounce from 61.8% confirms the trend is intact.
        A break below 78.6% suggests the original move may be fully reversed.
        """)

        st.subheader("6. Bollinger Bands")
        st.markdown("""
        **Bollinger Bands** consist of a middle band (SMA) and two outer bands at
        a set number of standard deviations above and below the SMA.

        ```
        Middle Band  = SMA(20)
        Upper Band   = SMA(20) + 2 x Standard Deviation
        Lower Band   = SMA(20) - 2 x Standard Deviation
        ```

        | Signal | Condition | Interpretation |
        |--------|-----------|----------------|
        | **Squeeze** | Bands narrowing | Low volatility — breakout likely soon |
        | **Expansion** | Bands widening | High volatility — strong trend in motion |
        | **Touch upper band** | Price at upper band | Overbought warning in ranging market |
        | **Touch lower band** | Price at lower band | Oversold warning in ranging market |
        | **Riding upper band** | Price consistently near upper band | Strong uptrend — not a sell signal |

        In FX, Bollinger Band squeezes often precede major moves — especially ahead of
        economic data releases (NFP, CPI, central bank decisions).
        """)

        st.subheader("7. Candlestick Patterns")
        st.markdown("""
        Each candlestick shows Open, High, Low, and Close for a period.

        | Pattern | Shape | Signal |
        |---------|-------|--------|
        | **Doji** | Open ≈ Close, long wicks | Indecision — potential reversal |
        | **Hammer** | Small body, long lower wick | Bullish reversal after downtrend |
        | **Shooting Star** | Small body, long upper wick | Bearish reversal after uptrend |
        | **Bullish Engulfing** | Large green candle engulfs prior red | Strong bullish reversal |
        | **Bearish Engulfing** | Large red candle engulfs prior green | Strong bearish reversal |
        | **Morning Star** | 3-candle pattern — down, doji, up | Bullish reversal |
        | **Evening Star** | 3-candle pattern — up, doji, down | Bearish reversal |
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: RSI Calculation Step by Step")
        st.markdown("""
        **EUR/USD 14-period RSI calculation:**

        ```
        Last 14 daily closes (price changes):
        Up days:   +0.35%, +0.42%, +0.18%, +0.51%, +0.29%, +0.38%, +0.22%  (7 days)
        Down days: -0.28%, -0.15%, -0.41%, -0.19%, -0.33%, -0.25%, -0.12% (7 days)

        Step 1: Average Gain = (0.35+0.42+0.18+0.51+0.29+0.38+0.22) / 14
                             = 2.35 / 14 = 0.1679%

        Step 2: Average Loss = (0.28+0.15+0.41+0.19+0.33+0.25+0.12) / 14
                             = 1.73 / 14 = 0.1236%

        Step 3: RS = Average Gain / Average Loss = 0.1679 / 0.1236 = 1.358

        Step 4: RSI = 100 - [100 / (1 + 1.358)]
                    = 100 - [100 / 2.358]
                    = 100 - 42.41
                    = 57.59

        Interpretation: RSI = 57.6 — bullish momentum, not overbought.
        Room to run higher before approaching the 70 threshold.
        ```
        """)

        st.subheader("Example 2: Fibonacci Retracement — EUR/USD")
        st.markdown("""
        **EUR/USD rallies from 1.0500 (swing low) to 1.1000 (swing high)**

        ```
        Range = 1.1000 - 1.0500 = 500 pips

        Fibonacci Retracement Levels:
        23.6% → 1.1000 - 500 x 0.236 = 1.0882  (shallow — strong bull trend)
        38.2% → 1.1000 - 500 x 0.382 = 1.0809  (first major support)
        50.0% → 1.1000 - 500 x 0.500 = 1.0750  (widely watched, psychological)
        61.8% → 1.1000 - 500 x 0.618 = 1.0691  (Golden Ratio — strongest support)
        78.6% → 1.1000 - 500 x 0.786 = 1.0607  (deep — trend in serious doubt)

        Trading Strategy:
        - Look for bullish candlestick patterns at 61.8% (1.0691)
        - Place buy order with stop below 78.6% (1.0607)
        - Target: retest of swing high 1.1000 (61.8% risk/reward ≈ 1:3)
        ```
        """)

        st.subheader("Example 3: Golden Cross Trading Signal — GBP/USD")
        st.markdown("""
        **GBP/USD 50/200 Moving Average Golden Cross:**

        | Date | GBP/USD | 50-Day MA | 200-Day MA | Signal |
        |------|---------|-----------|------------|--------|
        | Jan 2024 | 1.2400 | 1.2350 | 1.2500 | Death Cross — bearish |
        | Mar 2024 | 1.2600 | 1.2520 | 1.2530 | Converging — watch |
        | Apr 2024 | 1.2700 | 1.2600 | 1.2580 | **GOLDEN CROSS!** |
        | Jun 2024 | 1.2900 | 1.2780 | 1.2650 | Uptrend confirmed |

        ```
        Golden Cross at 1.2700:
        Entry:     1.2700 (on close above 200MA after cross)
        Stop-loss: 1.2500 (below 200MA — invalidates signal)
        Target:    1.3000 (previous resistance)

        Risk:   200 pips (1.2700 - 1.2500)
        Reward: 300 pips (1.3000 - 1.2700)
        R:R     1:1.5 — acceptable

        Note: Golden crosses work best in trending markets, not ranging markets.
        Confirm with rising RSI > 50 and MACD above zero.
        ```
        """)

        st.subheader("Example 4: Bollinger Band Squeeze — USD/JPY Pre-NFP")
        st.markdown("""
        **USD/JPY Bollinger Band Squeeze before US Non-Farm Payrolls:**

        ```
        Situation:
          Current USD/JPY:      149.50
          20-day SMA:           149.30
          Upper Band:           149.70  (only +20 pips from middle!)
          Lower Band:           148.90  (only -40 pips from middle!)
          Band Width:           80 pips (vs normal 200-250 pips)

        BB Squeeze detected → Low volatility → Major breakout imminent

        NFP Result: +350k jobs (much stronger than 200k expected)
        USD/JPY reaction: Spikes to 151.20 (+170 pips in minutes)
        Upper band penetrated → Riding the upper band

        Trade Management:
          Initial long entry:  149.60 (on break above upper band at 149.70)
          Stop-loss:           149.00 (below lower band)
          Target:              151.00 (measured move = band width added to breakout)
          R:R:                 1:2.3
        ```
        """)

        st.subheader("Example 5: Multi-Indicator Confluence Trade Setup")
        st.markdown("""
        **AUD/USD — Full Technical Analysis Checklist:**

        ```
        Timeframe: Daily chart
        Current Price: 0.6500

        TREND ANALYSIS:
          Price above 200-day MA (0.6400)     ✅ Bullish
          50-day MA (0.6480) > 200-day MA     ✅ Golden Cross in place
          Recent higher highs and higher lows  ✅ Uptrend structure

        MOMENTUM:
          RSI(14) = 58                         ✅ Bullish momentum, not overbought
          MACD Line above Signal Line           ✅ Bullish crossover 3 days ago
          MACD Histogram expanding              ✅ Momentum increasing

        LEVELS:
          Fibonacci 61.8% at 0.6450           ✅ Just bounced off this level
          Support confluence at 0.6450         ✅ Previous resistance (role reversal)
          Bollinger mid-band at 0.6480         ✅ Price above mid-band

        CONFLUENCE SCORE: 8/8 bullish signals

        TRADE PLAN:
          Entry:     0.6510 (breakout above recent high)
          Stop:      0.6430 (below 61.8% Fib and 50-day MA)
          Target:    0.6700 (previous swing high / resistance)
          R:R:       1:2.5 ✅
        ```
        The more indicators that align in the same direction, the higher
        the probability trade. Never rely on a single indicator alone.
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "📐 RSI Calculator",
            "🌀 Fibonacci Retracement Calculator",
            "📊 Moving Average Crossover Analyser",
            "📉 Bollinger Bands Calculator",
            "🎯 Support & Resistance Finder"
        ])

        st.markdown("---")

        # ── RSI CALCULATOR ────────────────────────────────────────────
        if calc_choice == "📐 RSI Calculator":
            st.subheader("RSI (Relative Strength Index) Calculator")
            st.info("Enter the last 14 price changes (as % or pips) to calculate RSI.")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Price Changes (+ = up day, - = down day):**")
                changes = []
                default_vals = [0.35, -0.28, 0.42, -0.15, 0.18, -0.41, 0.51, -0.19, 0.29, -0.33, 0.38, -0.25, 0.22, -0.12]
                for i in range(14):
                    val = st.number_input(f"Day {i+1}", value=default_vals[i], step=0.01, format="%.2f", key=f"rsi_d{i}")
                    changes.append(val)
            with col2:
                period = st.number_input("RSI Period", value=14, min_value=2, max_value=14)
                current_price = st.number_input("Current Price (for display)", value=1.0850, format="%.4f")
                overbought = st.number_input("Overbought Threshold", value=70, min_value=50, max_value=90)
                oversold   = st.number_input("Oversold Threshold", value=30, min_value=10, max_value=50)

            if st.button("Calculate RSI", type="primary"):
                gains = [c for c in changes if c > 0]
                losses = [abs(c) for c in changes if c < 0]
                avg_gain = sum(gains) / period if gains else 0
                avg_loss = sum(losses) / period if losses else 0.0001
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))

                st.markdown("---")
                st.markdown(f"""
                **RSI Calculation:**
                ```
                Up days:      {len(gains)}  |  Down days: {len(losses)}
                Average Gain: {avg_gain:.4f}%
                Average Loss: {avg_loss:.4f}%
                RS:           {rs:.4f}
                RSI(14):      {rsi:.2f}

                Formula: RSI = 100 - [100 / (1 + RS)]
                             = 100 - [100 / (1 + {rs:.4f})]
                             = {rsi:.2f}
                ```
                """)

                col1, col2, col3 = st.columns(3)
                col1.metric("RSI Value", f"{rsi:.2f}")
                col2.metric("Avg Gain", f"{avg_gain:.4f}%")
                col3.metric("Avg Loss", f"{avg_loss:.4f}%")

                if rsi > overbought:
                    st.error(f"🔴 OVERBOUGHT (RSI = {rsi:.1f} > {overbought}). Potential reversal lower. Look for bearish candlestick patterns to confirm.")
                elif rsi < oversold:
                    st.success(f"🟢 OVERSOLD (RSI = {rsi:.1f} < {oversold}). Potential reversal higher. Look for bullish candlestick patterns to confirm.")
                elif rsi > 50:
                    st.info(f"📈 Bullish momentum (RSI = {rsi:.1f}). Trend is positive. Above 50 = buyers in control.")
                else:
                    st.warning(f"📉 Bearish momentum (RSI = {rsi:.1f}). Trend is negative. Below 50 = sellers in control.")

                fig = go.Figure()
                fig.add_shape(type="rect", x0=0, x1=1, y0=overbought, y1=100,
                              fillcolor="rgba(231,76,60,0.15)", line_width=0)
                fig.add_shape(type="rect", x0=0, x1=1, y0=0, y1=oversold,
                              fillcolor="rgba(39,174,96,0.15)", line_width=0)
                fig.add_hline(y=rsi, line_color="#2E86C1", line_width=3,
                              annotation_text=f"RSI = {rsi:.1f}")
                fig.add_hline(y=overbought, line_dash="dash", line_color="#E74C3C",
                              annotation_text=f"Overbought {overbought}")
                fig.add_hline(y=oversold, line_dash="dash", line_color="#27AE60",
                              annotation_text=f"Oversold {oversold}")
                fig.update_layout(title=f"RSI Level — {rsi:.1f}",
                                  yaxis=dict(range=[0, 100], title="RSI"),
                                  xaxis=dict(showticklabels=False),
                                  height=300)
                st.plotly_chart(fig, use_container_width=True)

        # ── FIBONACCI ─────────────────────────────────────────────────
        elif calc_choice == "🌀 Fibonacci Retracement Calculator":
            st.subheader("Fibonacci Retracement Level Calculator")
            col1, col2 = st.columns(2)
            with col1:
                swing_high = st.number_input("Swing High", value=1.1000, format="%.4f", step=0.0001)
                swing_low  = st.number_input("Swing Low",  value=1.0500, format="%.4f", step=0.0001)
                direction  = st.radio("Trend Direction", ["Uptrend (retracement going down)", "Downtrend (retracement going up)"])
            with col2:
                current_p  = st.number_input("Current Price", value=1.0750, format="%.4f", step=0.0001)
                pair_name  = st.text_input("Currency Pair", value="EUR/USD")

            if st.button("Calculate Fibonacci Levels", type="primary"):
                fib_ratios  = [0.0, 0.236, 0.382, 0.500, 0.618, 0.786, 1.0]
                fib_names   = ["0% (Swing High)", "23.6%", "38.2%", "50.0%", "61.8% (Golden Ratio)", "78.6%", "100% (Swing Low)"]
                price_range = swing_high - swing_low

                if "Uptrend" in direction:
                    fib_levels = [swing_high - price_range * r for r in fib_ratios]
                else:
                    fib_levels = [swing_low + price_range * r for r in fib_ratios]

                rows = []
                for name, level, ratio in zip(fib_names, fib_levels, fib_ratios):
                    dist_pips = abs(current_p - level) * 10000
                    above_below = "ABOVE ↑" if current_p > level else "BELOW ↓"
                    nearest = "◄ CURRENT LEVEL" if dist_pips < 30 else ""
                    rows.append({
                        "Level": name,
                        "Price": f"{level:.4f}",
                        "Distance (pips)": f"{dist_pips:.0f}",
                        "vs Current Price": above_below,
                        "Notes": "🟡 Most significant" if ratio == 0.618 else ("⚠️ Deep retracement" if ratio == 0.786 else nearest)
                    })

                st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Swing High", f"{swing_high:.4f}")
                col2.metric("Swing Low",  f"{swing_low:.4f}")
                col3.metric("Range", f"{price_range*10000:.0f} pips")

                fig = go.Figure()
                colors_fib = ["#95A5A6", "#3498DB", "#27AE60", "#F39C12", "#E74C3C", "#8E44AD", "#95A5A6"]
                for level, name, color in zip(fib_levels, fib_names, colors_fib):
                    fig.add_hline(y=level, line_color=color, line_dash="dot" if "23.6" in name or "78.6" in name else "dash",
                                  annotation_text=f"{name}: {level:.4f}", annotation_position="right")
                fig.add_hline(y=current_p, line_color="#2E86C1", line_width=3,
                              annotation_text=f"Current: {current_p:.4f}")
                fig.update_layout(title=f"{pair_name} — Fibonacci Retracement Levels",
                                  yaxis_title="Price", yaxis=dict(range=[min(fib_levels)*0.999, max(fib_levels)*1.001]),
                                  xaxis=dict(showticklabels=False), height=400)
                st.plotly_chart(fig, use_container_width=True)

        # ── MA CROSSOVER ──────────────────────────────────────────────
        elif calc_choice == "📊 Moving Average Crossover Analyser":
            st.subheader("Moving Average Crossover Signal Analyser")
            st.info("Generate simulated price data and analyse MA crossover signals.")
            col1, col2 = st.columns(2)
            with col1:
                start_price = st.number_input("Starting Price", value=1.0500, format="%.4f")
                num_periods = st.slider("Number of Periods (days)", 50, 300, 200)
                trend_pct   = st.number_input("Trend Strength (% per year, + = uptrend)", value=5.0, step=0.5)
                volatility  = st.number_input("Daily Volatility %", value=0.6, step=0.1)
            with col2:
                fast_period = st.number_input("Fast MA Period", value=50, min_value=5, max_value=100)
                slow_period = st.number_input("Slow MA Period", value=200, min_value=20, max_value=300)
                pair_ma     = st.text_input("Currency Pair", value="EUR/USD", key="ma_pair")

            if st.button("Generate & Analyse", type="primary"):
                np.random.seed(42)
                daily_trend = trend_pct / 100 / 252
                daily_vol   = volatility / 100
                returns = np.random.normal(daily_trend, daily_vol, num_periods)
                prices  = [start_price]
                for r in returns:
                    prices.append(prices[-1] * (1 + r))
                prices = prices[1:]
                dates  = list(range(1, num_periods + 1))

                fast_ma = pd.Series(prices).rolling(int(fast_period)).mean().tolist()
                slow_ma = pd.Series(prices).rolling(int(slow_period)).mean().tolist()

                signals = []
                prev_above = None
                for i in range(num_periods):
                    if fast_ma[i] and slow_ma[i]:
                        above = fast_ma[i] > slow_ma[i]
                        if prev_above is not None and above != prev_above:
                            signals.append({"Day": i, "Price": prices[i],
                                            "Signal": "GOLDEN CROSS ✅" if above else "DEATH CROSS ❌",
                                            "Type": "Buy" if above else "Sell"})
                        prev_above = above

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=dates, y=prices, name=pair_ma,
                    line=dict(color="#2E86C1", width=1.5), mode="lines"))
                fig.add_trace(go.Scatter(x=dates, y=fast_ma, name=f"{int(fast_period)}-day MA",
                    line=dict(color="#F39C12", width=2), mode="lines"))
                fig.add_trace(go.Scatter(x=dates, y=slow_ma, name=f"{int(slow_period)}-day MA",
                    line=dict(color="#E74C3C", width=2), mode="lines"))
                for sig in signals:
                    fig.add_vline(x=sig["Day"], line_dash="dot",
                                  line_color="#27AE60" if sig["Type"] == "Buy" else "#E74C3C",
                                  annotation_text=sig["Signal"].split(" ")[0])
                fig.update_layout(title=f"{pair_ma} — Moving Average Crossover Analysis",
                                  xaxis_title="Day", yaxis_title="Price",
                                  legend=dict(x=0.01, y=0.99))
                st.plotly_chart(fig, use_container_width=True)

                if signals:
                    st.dataframe(pd.DataFrame(signals), use_container_width=True, hide_index=True)
                    st.metric("Total Crossover Signals", len(signals))
                else:
                    st.info("No crossover signals in this period. Try increasing the number of periods or adjusting the trend.")

        # ── BOLLINGER BANDS ───────────────────────────────────────────
        elif calc_choice == "📉 Bollinger Bands Calculator":
            st.subheader("Bollinger Bands Calculator & Squeeze Detector")
            st.info("Enter recent closing prices to calculate Bollinger Bands and detect squeezes.")
            col1, col2 = st.columns(2)
            with col1:
                bb_period = st.number_input("BB Period (SMA)", value=20, min_value=5, max_value=50)
                bb_std    = st.number_input("Standard Deviations", value=2.0, step=0.5, min_value=1.0)
                pair_bb   = st.text_input("Currency Pair", value="USD/JPY", key="bb_pair")
            with col2:
                st.markdown("**Enter last 20 closing prices (most recent last):**")
                default_prices = [148.2, 148.5, 149.1, 149.3, 148.8, 149.0, 149.5, 149.8, 150.1, 149.9,
                                  149.6, 149.8, 150.0, 149.7, 149.9, 150.2, 150.0, 149.8, 149.9, 150.1]
                bb_prices = []
                for i in range(int(bb_period)):
                    p = st.number_input(f"Close {i+1}", value=default_prices[i] if i < 20 else 149.5,
                                        format="%.2f", step=0.01, key=f"bb_p{i}")
                    bb_prices.append(p)

            if st.button("Calculate Bollinger Bands", type="primary"):
                sma_bb   = np.mean(bb_prices)
                std_bb   = np.std(bb_prices, ddof=1)
                upper_bb = sma_bb + bb_std * std_bb
                lower_bb = sma_bb - bb_std * std_bb
                bw       = (upper_bb - lower_bb) / sma_bb * 100
                current_bb = bb_prices[-1]
                b_pct    = (current_bb - lower_bb) / (upper_bb - lower_bb) * 100 if upper_bb != lower_bb else 50

                st.markdown("---")
                st.markdown(f"""
                **Bollinger Bands Calculation:**
                ```
                SMA({int(bb_period)}):       {sma_bb:.4f}
                Std Dev:          {std_bb:.4f}
                Upper Band:       {upper_bb:.4f}  ({sma_bb:.4f} + {bb_std}x{std_bb:.4f})
                Middle Band:      {sma_bb:.4f}
                Lower Band:       {lower_bb:.4f}  ({sma_bb:.4f} - {bb_std}x{std_bb:.4f})
                Band Width:       {bw:.2f}%
                Current Price:    {current_bb:.4f}
                %B:               {b_pct:.1f}%  (0% = at lower, 100% = at upper band)
                ```
                """)
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Upper Band", f"{upper_bb:.4f}")
                c2.metric("Middle (SMA)", f"{sma_bb:.4f}")
                c3.metric("Lower Band", f"{lower_bb:.4f}")
                c4.metric("Band Width %", f"{bw:.2f}%")

                if bw < 1.5:
                    st.warning(f"🔔 BOLLINGER SQUEEZE detected (BW = {bw:.2f}%). Very low volatility — expect a major breakout soon!")
                elif current_bb > upper_bb:
                    st.error(f"🔴 Price ({current_bb:.4f}) ABOVE upper band ({upper_bb:.4f}). Overbought in ranging market.")
                elif current_bb < lower_bb:
                    st.success(f"🟢 Price ({current_bb:.4f}) BELOW lower band ({lower_bb:.4f}). Oversold in ranging market.")
                else:
                    st.info(f"ℹ️ Price within bands. %B = {b_pct:.1f}%. {'Above midline — bullish' if b_pct > 50 else 'Below midline — bearish'}.")

                fig = go.Figure()
                x_range = list(range(1, len(bb_prices)+1))
                fig.add_trace(go.Scatter(x=x_range, y=[upper_bb]*len(bb_prices), name="Upper Band",
                    line=dict(color="#E74C3C", width=1.5, dash="dash")))
                fig.add_trace(go.Scatter(x=x_range, y=[sma_bb]*len(bb_prices), name="Middle (SMA)",
                    line=dict(color="#F39C12", width=2)))
                fig.add_trace(go.Scatter(x=x_range, y=[lower_bb]*len(bb_prices), name="Lower Band",
                    line=dict(color="#27AE60", width=1.5, dash="dash"),
                    fill="tonexty", fillcolor="rgba(39,174,96,0.05)"))
                fig.add_trace(go.Scatter(x=x_range, y=bb_prices, name=pair_bb,
                    line=dict(color="#2E86C1", width=2.5), mode="lines+markers",
                    marker=dict(size=5)))
                fig.update_layout(title=f"{pair_bb} — Bollinger Bands ({int(bb_period)}-period, {bb_std}σ)",
                                  xaxis_title="Period", yaxis_title="Price",
                                  legend=dict(x=0.01, y=0.99))
                st.plotly_chart(fig, use_container_width=True)

        # ── S&R FINDER ────────────────────────────────────────────────
        elif calc_choice == "🎯 Support & Resistance Finder":
            st.subheader("Key S&R Levels — Pivot Point Calculator")
            st.info("Calculate daily, weekly, or monthly pivot points and S&R levels from OHLC data.")
            col1, col2 = st.columns(2)
            with col1:
                prev_high  = st.number_input("Previous Period High",  value=1.0920, format="%.4f", step=0.0001)
                prev_low   = st.number_input("Previous Period Low",   value=1.0780, format="%.4f", step=0.0001)
                prev_close = st.number_input("Previous Period Close", value=1.0850, format="%.4f", step=0.0001)
            with col2:
                current_p_sr = st.number_input("Current Price", value=1.0870, format="%.4f", step=0.0001)
                pivot_type   = st.selectbox("Pivot Type", ["Classic", "Fibonacci", "Camarilla"])
                pair_sr      = st.text_input("Currency Pair", value="EUR/USD", key="sr_pair")

            if st.button("Calculate S&R Levels", type="primary"):
                PP = (prev_high + prev_low + prev_close) / 3

                if pivot_type == "Classic":
                    R1 = 2*PP - prev_low
                    R2 = PP + (prev_high - prev_low)
                    R3 = prev_high + 2*(PP - prev_low)
                    S1 = 2*PP - prev_high
                    S2 = PP - (prev_high - prev_low)
                    S3 = prev_low - 2*(prev_high - PP)
                elif pivot_type == "Fibonacci":
                    rng = prev_high - prev_low
                    R1 = PP + 0.382*rng; R2 = PP + 0.618*rng; R3 = PP + 1.000*rng
                    S1 = PP - 0.382*rng; S2 = PP - 0.618*rng; S3 = PP - 1.000*rng
                else:  # Camarilla
                    rng = prev_high - prev_low
                    R1 = prev_close + 1.1*rng/12; R2 = prev_close + 1.1*rng/6
                    R3 = prev_close + 1.1*rng/4
                    S1 = prev_close - 1.1*rng/12; S2 = prev_close - 1.1*rng/6
                    S3 = prev_close - 1.1*rng/4

                levels_df = pd.DataFrame({
                    "Level": ["R3 (Strong Resistance)", "R2 (Resistance 2)", "R1 (Resistance 1)",
                              "PP (Pivot Point)", "S1 (Support 1)", "S2 (Support 2)", "S3 (Strong Support)"],
                    "Price":  [f"{R3:.4f}", f"{R2:.4f}", f"{R1:.4f}", f"{PP:.4f}", f"{S1:.4f}", f"{S2:.4f}", f"{S3:.4f}"],
                    "vs Current": [f"{(R3-current_p_sr)*10000:+.0f} pips", f"{(R2-current_p_sr)*10000:+.0f} pips",
                                   f"{(R1-current_p_sr)*10000:+.0f} pips", f"{(PP-current_p_sr)*10000:+.0f} pips",
                                   f"{(S1-current_p_sr)*10000:+.0f} pips", f"{(S2-current_p_sr)*10000:+.0f} pips",
                                   f"{(S3-current_p_sr)*10000:+.0f} pips"],
                    "Type": ["Resistance", "Resistance", "Resistance", "Pivot", "Support", "Support", "Support"]
                })
                st.dataframe(levels_df, use_container_width=True, hide_index=True)
                st.metric("Pivot Point (PP)", f"{PP:.4f}")
                pos = "ABOVE Pivot (bullish bias)" if current_p_sr > PP else "BELOW Pivot (bearish bias)"
                st.info(f"Current price {current_p_sr:.4f} is {pos}. Nearest resistance: {R1:.4f} ({(R1-current_p_sr)*10000:.0f} pips). Nearest support: {S1:.4f} ({(current_p_sr-S1)*10000:.0f} pips).")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("Simulated EUR/USD with Technical Indicators")
        np.random.seed(101)
        n = 200
        prices_v = [1.0500]
        for _ in range(n - 1):
            prices_v.append(prices_v[-1] * (1 + np.random.normal(0.0002, 0.006)))
        prices_s = pd.Series(prices_v)
        sma50  = prices_s.rolling(50).mean()
        sma200 = prices_s.rolling(200).mean()
        bb_m   = prices_s.rolling(20).mean()
        bb_u   = bb_m + 2 * prices_s.rolling(20).std()
        bb_l   = bb_m - 2 * prices_s.rolling(20).std()

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=list(range(n)), y=prices_v, name="EUR/USD",
            line=dict(color="#2E86C1", width=1.5)))
        fig1.add_trace(go.Scatter(x=list(range(n)), y=sma50.tolist(), name="50-day MA",
            line=dict(color="#F39C12", width=2)))
        fig1.add_trace(go.Scatter(x=list(range(n)), y=sma200.tolist(), name="200-day MA",
            line=dict(color="#E74C3C", width=2)))
        fig1.add_trace(go.Scatter(x=list(range(n)), y=bb_u.tolist(), name="BB Upper",
            line=dict(color="#8E44AD", width=1, dash="dot")))
        fig1.add_trace(go.Scatter(x=list(range(n)), y=bb_l.tolist(), name="BB Lower",
            line=dict(color="#8E44AD", width=1, dash="dot"),
            fill="tonexty", fillcolor="rgba(142,68,173,0.05)"))
        fig1.update_layout(title="EUR/USD — Price with 50/200 MA and Bollinger Bands",
                           xaxis_title="Day", yaxis_title="Price",
                           legend=dict(x=0.01, y=0.99))
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("RSI Oscillator")
        changes_v = [prices_v[i] - prices_v[i-1] for i in range(1, len(prices_v))]
        gains_v   = [max(c, 0) for c in changes_v]
        losses_v  = [abs(min(c, 0)) for c in changes_v]
        rsi_vals  = []
        for i in range(13, len(gains_v)):
            avg_g = np.mean(gains_v[i-13:i+1])
            avg_l = np.mean(losses_v[i-13:i+1])
            rs_v  = avg_g / avg_l if avg_l > 0 else 100
            rsi_vals.append(100 - 100 / (1 + rs_v))
        rsi_x = list(range(14, n))

        fig2 = go.Figure()
        fig2.add_shape(type="rect", x0=0, x1=n, y0=70, y1=100, fillcolor="rgba(231,76,60,0.1)", line_width=0)
        fig2.add_shape(type="rect", x0=0, x1=n, y0=0, y1=30, fillcolor="rgba(39,174,96,0.1)", line_width=0)
        fig2.add_trace(go.Scatter(x=rsi_x, y=rsi_vals, name="RSI(14)",
            line=dict(color="#2E86C1", width=2)))
        fig2.add_hline(y=70, line_dash="dash", line_color="#E74C3C", annotation_text="Overbought 70")
        fig2.add_hline(y=30, line_dash="dash", line_color="#27AE60", annotation_text="Oversold 30")
        fig2.add_hline(y=50, line_dash="dot", line_color="gray", annotation_text="Neutral 50")
        fig2.update_layout(title="RSI(14) Oscillator", xaxis_title="Day",
                           yaxis=dict(range=[0, 100], title="RSI"), height=250)
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Fibonacci Retracement — Illustrative")
        high_f = 1.1000; low_f = 1.0500
        fib_r  = [0.0, 0.236, 0.382, 0.500, 0.618, 0.786, 1.0]
        fib_p  = [high_f - (high_f - low_f) * r for r in fib_r]
        fib_l  = ["0% (High)", "23.6%", "38.2%", "50.0%", "61.8% (Golden)", "78.6%", "100% (Low)"]
        clrs_f = ["#2ECC71", "#3498DB", "#27AE60", "#F39C12", "#E74C3C", "#8E44AD", "#E74C3C"]
        fig3 = go.Figure()
        for level, name, col in zip(fib_p, fib_l, clrs_f):
            lw = 2.5 if "61.8" in name else 1.5
            fig3.add_hline(y=level, line_color=col, line_dash="dash" if "61.8" not in name else "solid",
                           line_width=lw, annotation_text=f"{name}: {level:.4f}")
        fig3.add_hline(y=1.0750, line_color="#2E86C1", line_width=3,
                       annotation_text="Current Price: 1.0750")
        fig3.update_layout(title="EUR/USD Fibonacci Retracement (1.0500 → 1.1000)",
                           yaxis=dict(range=[1.0450, 1.1050], title="Price"),
                           xaxis=dict(showticklabels=False), height=400)
        st.plotly_chart(fig3, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — Technical Analysis")

        st.markdown("**Q1. A 'Golden Cross' in technical analysis occurs when:**")
        q1 = st.radio("", [
            "Price crosses above the 61.8% Fibonacci retracement level",
            "The 50-day moving average crosses ABOVE the 200-day moving average",
            "RSI crosses above the 70 overbought threshold",
            "MACD crosses above the zero line"
        ], key="fx10q1")
        if st.button("Check Q1", key="fx10c1"):
            if "50-day moving average crosses ABOVE the 200-day" in q1:
                st.success("✅ Correct! Golden Cross = 50-day MA crosses above 200-day MA. It is a major long-term bullish signal, especially when accompanied by rising volume.")
            else:
                st.error("❌ Incorrect. Golden Cross = 50-day MA crosses ABOVE 200-day MA. The opposite (50 crosses below 200) is the Death Cross.")
        st.markdown("---")

        st.markdown("**Q2. An RSI reading of 75 suggests:**")
        q2 = st.radio("", [
            "The currency is in a strong downtrend",
            "The currency is oversold and a buy signal is triggered",
            "The currency is overbought — potential reversal or pullback warning",
            "The currency is at its 200-day moving average"
        ], key="fx10q2")
        if st.button("Check Q2", key="fx10c2"):
            if "overbought" in q2:
                st.success("✅ Correct! RSI > 70 = overbought. Not an automatic sell signal, but a warning that the move may be overextended. Look for bearish confirmation candles.")
            else:
                st.error("❌ Incorrect. RSI > 70 = overbought (potential reversal). RSI < 30 = oversold (potential bounce).")
        st.markdown("---")

        st.markdown("**Q3. The Fibonacci 61.8% level is significant because:**")
        q3 = st.radio("", [
            "It was invented by technical analysts in the 1980s",
            "It represents the Golden Ratio (1/phi) and appears throughout nature and markets",
            "It is the 50% midpoint of any price move",
            "It is always the strongest support level regardless of context"
        ], key="fx10q3")
        if st.button("Check Q3", key="fx10c3"):
            if "Golden Ratio" in q3:
                st.success("✅ Correct! 61.8% = the Golden Ratio (1/φ ≈ 0.618). It appears throughout nature and financial markets and is the most-watched Fibonacci retracement level.")
            else:
                st.error("❌ Incorrect. 61.8% = the Golden Ratio (1/phi). The 50% level is a psychological midpoint — not a true Fibonacci ratio.")
        st.markdown("---")

        st.markdown("**Q4. A Bollinger Band squeeze indicates:**")
        q4 = st.radio("", [
            "The currency pair is trending strongly upward",
            "Volatility is very low and a significant breakout is likely imminent",
            "The currency is overbought at the upper band",
            "The moving average is about to cross"
        ], key="fx10q4")
        if st.button("Check Q4", key="fx10c4"):
            if "Volatility is very low" in q4:
                st.success("✅ Correct! BB squeeze = bands narrow together = low volatility period. Low volatility tends to precede high volatility — a major breakout (up or down) is coming.")
            else:
                st.error("❌ Incorrect. A BB squeeze means bands are narrowing = low volatility = breakout imminent. The direction is unknown until the price breaks out.")
        st.markdown("---")

        st.markdown("**Q5. RSI bearish divergence occurs when:**")
        q5 = st.radio("", [
            "RSI is above 70 and price falls",
            "Price makes a new HIGH but RSI makes a LOWER high — momentum weakening",
            "RSI crosses below the 50 level",
            "Price and RSI both decline together"
        ], key="fx10q5")
        if st.button("Check Q5", key="fx10c5"):
            if "Price makes a new HIGH but RSI makes a LOWER high" in q5:
                st.success("✅ Correct! Bearish divergence = price new high + RSI lower high. Momentum is weakening despite price rising — a warning of potential reversal.")
            else:
                st.error("❌ Incorrect. Bearish divergence: price makes new high but RSI makes a lower high. This shows momentum is fading — a powerful warning signal.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Technical Indicators — Quick Reference")
        indicators_df = pd.DataFrame({
            "Indicator": ["SMA / EMA", "Golden/Death Cross", "RSI(14)", "MACD", "Bollinger Bands", "Fibonacci 61.8%", "Pivot Points"],
            "Type": ["Trend", "Trend", "Momentum Oscillator", "Trend + Momentum", "Volatility", "S&R Level", "S&R Level"],
            "Key Signal": [
                "Price above MA = uptrend; below = downtrend",
                "50-day crossing 200-day = major trend change",
                ">70 overbought; <30 oversold; divergence = reversal warning",
                "MACD above signal = bullish; below = bearish; histogram = momentum",
                "Squeeze = breakout coming; touch upper/lower = extreme",
                "Bounce from 61.8% = trend intact; break = reversal",
                "PP = bias; R1/S1 = first targets; R3/S3 = extreme levels"
            ],
            "Lagging?": ["Yes", "Yes (significant lag)", "Leading/coincident", "Slightly lagging", "Coincident", "Forward-looking", "Forward-looking"]
        })
        st.dataframe(indicators_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "RSI",
                "RS (for RSI)",
                "MACD Line",
                "Signal Line",
                "Bollinger Upper Band",
                "Bollinger Lower Band",
                "Fibonacci Level (uptrend retracement)"
            ],
            "Expression": [
                "100 - [100 / (1 + RS)]",
                "Average Gain (N periods) / Average Loss (N periods)",
                "EMA(12) - EMA(26)",
                "EMA(9) of MACD Line",
                "SMA(20) + 2 × Standard Deviation(20)",
                "SMA(20) - 2 × Standard Deviation(20)",
                "High - (High - Low) × Fibonacci Ratio (e.g. 0.618)"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Candlestick Pattern Reference")
        candles_df = pd.DataFrame({
            "Pattern": ["Hammer", "Shooting Star", "Doji", "Bullish Engulfing", "Bearish Engulfing", "Morning Star", "Evening Star"],
            "Signal": ["Bullish reversal", "Bearish reversal", "Indecision", "Strong bullish reversal", "Strong bearish reversal", "Bullish reversal (3 candles)", "Bearish reversal (3 candles)"],
            "Where Valid": ["After downtrend", "After uptrend", "After any trend", "After downtrend", "After uptrend", "After downtrend", "After uptrend"],
            "Confirmation Needed": ["Yes — next candle close above hammer", "Yes — next candle closes lower", "Yes — follow-up direction candle", "Strong — usually reliable", "Strong — usually reliable", "Yes — above star", "Yes — below star"]
        })
        st.dataframe(candles_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Using a single indicator in isolation",
                "Trading every RSI overbought/oversold signal",
                "Placing stops too tight near support levels",
                "Ignoring the major trend when trading short-term signals",
                "Forcing Fibonacci levels that do not align with actual price action"
            ],
            "Correct Approach": [
                "Use confluence — at least 3 indicators agreeing before entering",
                "In strong trends, RSI can stay overbought/oversold for extended periods",
                "Allow for normal price noise; use ATR to set appropriate stop distances",
                "Always trade with the higher timeframe trend; counter-trend trades have lower success",
                "Fibonacci works best when levels coincide with prior S&R and moving averages"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 10 Complete! You can apply RSI, MACD, Fibonacci retracements, Bollinger Bands, and moving average crossovers to real FX charts.")
        st.info("💡 Next: Module 11 — FX in Capital Markets & Corporate Finance (FX-adjusted DCF, M&A, currency overlay)")

if __name__ == "__main__":
    show()