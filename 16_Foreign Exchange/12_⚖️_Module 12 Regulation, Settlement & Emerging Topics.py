import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("26 Module 12: Regulation, Settlement & Emerging Topics")
    st.markdown("*Master the FX Global Code, CLS settlement, MiFID II best execution, Dodd-Frank, algorithmic FX, and CBDCs*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. FX Global Code of Conduct")
        st.markdown("""
        The **FX Global Code** is a set of global principles for professional and ethical
        conduct by participants in the foreign exchange market.

        | Feature | Detail |
        |---------|--------|
        | **Published by** | Global Foreign Exchange Committee (GFXC), supported by central banks |
        | **First published** | May 2017 (revised May 2021) |
        | **Legal status** | Voluntary — not legally binding regulation |
        | **Enforcement** | Market access norms; non-compliance leads to reputational damage |
        | **Statement of Commitment** | Firms sign to declare adherence publicly |

        **Six Pillars of the FX Global Code:**
        ```
        1. Ethics            — Integrity, fair dealing, and professional standards
        2. Governance        — Clear accountability and oversight structures
        3. Execution         — Transparent and fair order handling
        4. Information Sharing — Confidentiality and appropriate use of market info
        5. Risk Management   — Effective identification and management of FX risks
        6. Confirmation & Settlement — Robust settlement and confirmation processes
        ```

        **Key Execution Principles:**
        - **Pre-hedging:** Permitted only when acting as principal and disclosed to clients
        - **Last look:** Must be applied consistently and symmetrically (not only against clients)
        - **Mark-up:** Must be transparent and fair; excessive mark-ups are a Code violation
        - **Information barriers:** Confidential client information must not be misused
        """)

        st.subheader("2. CLS Bank & Payment-vs-Payment Settlement")
        st.markdown("""
        **CLS (Continuous Linked Settlement)** Bank is the primary mechanism for eliminating
        Herstatt (principal/settlement) risk in the global FX market.

        **How CLS works step by step:**
        ```
        Step 1: Both counterparties submit trade instructions to CLS
        Step 2: CLS calculates net positions for each member in each currency
        Step 3: Members fund their net short positions (funding window: 7–9 AM ET)
        Step 4: CLS releases payments simultaneously (Payment-vs-Payment)
        Step 5: If a party cannot fund → NEITHER payment settles (no principal loss)
        ```

        | CLS Statistic | Value |
        |---------------|-------|
        | Daily volume | ~$6.5 trillion |
        | Settlement currencies | 18 major currencies |
        | Settlement members | ~70 major global banks |
        | Risk eliminated | Principal (Herstatt) risk |
        | Average netting efficiency | 96–98% of gross obligations |

        **Trades outside CLS:**
        Exotic EM currencies, very short-dated trades, and non-member bank trades still
        carry settlement risk — managed via bilateral credit limits and ISDA Master Agreements.
        """)

        st.subheader("3. MiFID II & Best Execution in FX")
        st.markdown("""
        **MiFID II** (Markets in Financial Instruments Directive II, effective January 2018)
        imposes best execution obligations for FX transactions within the European Union.

        **Best Execution — Multi-Factor Test (NOT just best price):**
        ```
        Factors considered for best execution:
        1. Price (including all costs — spread, mark-up, commissions)
        2. Speed of execution
        3. Likelihood of full execution and settlement
        4. Size and nature of the order
        5. Market impact of the order
        6. Any other relevant considerations
        ```

        | MiFID II Requirement | Detail |
        |---------------------|--------|
        | EMIR reporting | All OTC FX derivatives reported to a trade repository |
        | RTS 27/28 reports | Annual best execution quality reports published |
        | Transaction reporting | All trades reported to regulators within T+1 |
        | Pre-trade transparency | Quote disclosure for systematic internalisers |
        | Post-trade transparency | Trade data published after execution |

        **Transaction Cost Analysis (TCA):**
        TCA benchmarks execution quality against VWAP, arrival price, and mid-market.
        MiFID II has driven widespread TCA adoption across all major FX dealing rooms.
        """)

        st.subheader("4. Dodd-Frank & US FX Regulation")
        st.markdown("""
        The **Dodd-Frank Wall Street Reform Act (2010)** introduced major FX derivatives
        regulation in the US following the 2008 financial crisis.

        | Requirement | Detail |
        |------------|--------|
        | Swap Dealer Registration | Firms with FX derivative activity > $8B/year must register with CFTC |
        | Central Clearing | Standardised FX swaps must be cleared via CCPs |
        | Trade Reporting | All FX swap/forward trades reported to Swap Data Repositories |
        | Margin Requirements | Initial and variation margin for uncleared OTC FX derivatives |
        | Business Conduct | Suitability, disclosure, and fair dealing obligations |

        **Spot FX exemption:** Pure spot FX (T+2 settlement) is generally exempt from
        Dodd-Frank swap regulations. Deliverable forwards are also largely exempt.

        **Global fragmentation:**
        MiFID II (EU), Dodd-Frank (US), and various Asian regimes create some market
        fragmentation — driving demand for cross-border regulatory harmonisation.
        """)

        st.subheader("5. Algorithmic & Electronic FX Trading")
        st.markdown("""
        Electronic execution platforms have transformed FX markets since the late 1990s.

        **Key Electronic Platforms:**
        | Platform | Type | Primary Use |
        |---------|------|------------|
        | EBS Market/Direct | Interbank ECN | EUR/USD, USD/JPY primary venue |
        | Reuters Matching | Interbank ECN | GBP and commodity currency venue |
        | Hotspot / LMAX | Institutional ECN | Multi-dealer platform |
        | Single-dealer (e.g. Citi Velocity) | Bilateral | Large bank proprietary platform |
        | Aggregators (e.g. 360T, FXall) | Smart order routing | Multi-bank competition |

        **Common FX Execution Algorithms:**
        ```
        TWAP (Time-Weighted Average Price):
          Splits order into equal time slices
          Best for: orders that must finish by a specific time

        VWAP (Volume-Weighted Average Price):
          Participates in proportion to historical volume patterns
          Best for: large orders benchmarked against the day's VWAP

        Implementation Shortfall (IS):
          Minimises total cost vs the decision price
          Trades faster when market moves favourably
          Best for: alpha-sensitive strategies

        Participation Rate:
          Trades as a fixed percentage of market volume
          Best for: very large, illiquid orders
        ```
        """)

        st.subheader("6. CBDCs & The Future of FX")
        st.markdown("""
        **Central Bank Digital Currencies (CBDCs)** are digital forms of central bank money
        with the potential to fundamentally reshape cross-border FX settlement.

        | Feature | Current System | CBDC Vision |
        |---------|---------------|------------|
        | Settlement time | T+2 (spot) | Near-instant (seconds) |
        | Settlement risk | Herstatt risk (mitigated by CLS) | Eliminated by design (built-in PvP) |
        | Correspondent banks | Multi-layer chain | Potentially bypassed |
        | Cost | Multiple intermediary fees | Substantially lower |
        | Programmability | Very limited | Smart contracts possible |

        **mBridge Project (BIS + China, UAE, Thailand, Hong Kong):**
        ```
        Multi-CBDC platform for cross-border FX settlement
        Minimum viable product launched 2024 — live transactions piloted
        Settlement: seconds vs days
        No correspondent banking chain required
        Built-in PvP: atomic exchange eliminates settlement risk
        Potential impact: most significant FX infrastructure change in 50 years
        ```

        **Other key CBDC projects:**
        - Project Jura (Swiss National Bank + Banque de France): wholesale CBDC FX
        - Project Dunbar (MAS + RBA + BNM + SARB): multi-CBDC settlement
        - ECB Digital Euro: retail CBDC consultation underway, potential 2027 launch
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: CLS Netting Efficiency")
        st.markdown("""
        **Bank ABC has 5 EUR/USD trades to settle today:**

        | Trade | Direction | EUR (M) | USD (M) |
        |-------|-----------|---------|---------|
        | T1 | Buy EUR | +100 | -108.5 |
        | T2 | Sell EUR | -75 | +81.4 |
        | T3 | Buy EUR | +50 | -54.3 |
        | T4 | Sell EUR | -120 | +130.2 |
        | T5 | Buy EUR | +80 | -86.8 |

        ```
        Gross Settlement Obligations:
          EUR gross: 100+75+50+120+80 = EUR 425M total
          USD gross: 108.5+81.4+54.3+130.2+86.8 = USD 461.2M total

        Net Position after CLS netting:
          EUR net: +100-75+50-120+80 = +EUR 35M (net long EUR)
          USD net: -108.5+81.4-54.3+130.2-86.8 = -USD 38.0M (net short USD)

        Netting Efficiency:
          EUR: (1 - 35/425) x 100 = 91.8% netted
          USD: (1 - 38/461.2) x 100 = 91.8% netted

        Bank ABC funds only EUR 35M and USD 38M — NOT 425M and 461M.
        Capital and liquidity benefit: enormous for a bank with thousands of trades per day.
        ```
        """)

        st.subheader("Example 2: VWAP Execution — Large EUR/USD Order")
        st.markdown("""
        **Asset manager buys EUR 100M in EUR/USD using a VWAP algorithm over one day:**

        | Slice | Time | Exec Price | Size (M) | Weighted Price |
        |-------|------|-----------|----------|---------------|
        | 1 | 08:00 | 1.0845 | 5 | 0.054225 |
        | 2 | 09:00 | 1.0852 | 8 | 0.086816 |
        | 3 | 10:00 | 1.0859 | 12 | 0.130308 |
        | 4 | 11:00 | 1.0850 | 10 | 0.108500 |
        | 5 | 12:00 | 1.0863 | 15 | 0.162945 |
        | 6 | 13:00 | 1.0856 | 18 | 0.195408 |
        | 7 | 14:00 | 1.0849 | 14 | 0.151886 |
        | 8 | 15:00 | 1.0862 | 18 | 0.195516 |

        ```
        Execution VWAP:
        = Sum(Price x Size) / Sum(Size)
        = (5x1.0845 + 8x1.0852 + 12x1.0859 + 10x1.0850 +
           15x1.0863 + 18x1.0856 + 14x1.0849 + 18x1.0862) / 100
        = 108.5596 / 100
        = 1.08560

        Market VWAP Benchmark = average of all prices = 1.08545

        Implementation Shortfall (vs arrival price 1.0845):
        IS = (1.08560 - 1.08450) / 1.08450 x 10,000 = 10.1 bps

        Execution vs benchmark: 1.08560 - 1.08545 = +1.5 bps slippage vs VWAP
        Within acceptable tolerance for EUR 100M order.
        ```
        """)

        st.subheader("Example 3: MiFID II Best Execution Assessment")
        st.markdown("""
        **Trade: Client buys EUR 5M at EUR/USD 1.08520. Mid-market = 1.08500.**

        ```
        Best Execution Multi-Factor Assessment:

        Factor 1 — Price:
          Spread = 1.08520 - 1.08500 = 2 pips
          Typical EUR/USD market spread = 0.5-1.5 pips (institutional)
          Assessment: Slightly wide but acceptable for EUR 5M ✅

        Factor 2 — Total Cost:
          Spread cost = 2 pips x EUR 5M = USD 1,000
          Cost as bps = 1,000 / 5,000,000 x 10,000 = 2 bps
          Assessment: Within normal range for EUR 5M ✅

        Factor 3 — Speed:
          Execution time = 42 milliseconds after order receipt
          Assessment: Excellent ✅

        Factor 4 — Likelihood of Execution:
          Fill rate = 100% (EUR/USD fully liquid)
          Assessment: Perfect ✅

        Factor 5 — Market Impact:
          EUR 5M in EUR/USD = negligible market impact
          Assessment: None ✅

        BEST EXECUTION VERDICT: Achieved
        Firm must document this assessment and retain records for 5 years.
        ```
        """)

        st.subheader("Example 4: Dodd-Frank Swap Dealer Registration")
        st.markdown("""
        **Does Firm X need to register as a CFTC Swap Dealer?**

        ```
        12-Month Rolling FX Derivatives Activity:
          FX Options:           $3.2B notional
          Cross-currency swaps: $2.8B notional
          FX forwards (spec.):  $1.5B notional
          FX swaps (< 7 days):  $1.2B notional
          ─────────────────────────────────────
          Total:                $8.7B notional

        Dodd-Frank threshold:   $8.0B

        $8.7B > $8.0B → REGISTRATION REQUIRED

        Registration obligations:
          - Daily trade reporting to CFTC-registered SDR
          - Initial margin: 10% of notional (IM schedule)
          - Variation margin: daily mark-to-market exchange
          - Capital requirements: net capital rules apply
          - Business conduct: suitability and disclosure requirements

        If total were $7.5B → De minimis exemption → No registration needed
        ```
        """)

        st.subheader("Example 5: mBridge vs Correspondent Banking")
        st.markdown("""
        **Payment: Singapore company pays Chinese supplier CNY 10,000,000**

        **Current system (correspondent banking):**
        ```
        Day 1, 10:00 AM SGT:
          SGD bank sends SWIFT MT103 to US correspondent bank
          US correspondent debits SGD bank nostro (USD equivalent)
          US correspondent sends SWIFT instruction to China correspondent

        Day 1–2 (processing delays):
          China correspondent credits CNY account in China
          Supplier receives CNY 10M

        Timeline:      1–3 business days
        Total fees:    ~0.8% of transaction = ~$11,000 (USD equiv.)
        Transparency:  Limited — no real-time tracking
        Settlement risk: Herstatt risk in each correspondent link
        ```

        **mBridge CBDC (future vision):**
        ```
        T+0, Real time:
          SGD CBDC locked in mBridge multi-CBDC platform
          Atomic swap: SGD CBDC <-> CNY CBDC simultaneously
          CNY CBDC delivered to supplier's digital wallet

        Timeline:      ~10 seconds
        Total fees:    Near zero (no correspondent chain)
        Transparency:  Full real-time visibility on distributed ledger
        Settlement risk: Zero (PvP atomic settlement built in)
        ```

        Estimated global savings from CBDC cross-border payments:
        ~$120 billion annually (McKinsey Global Institute estimate).
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "🔄 CLS Netting Calculator",
            "📊 VWAP Execution Quality Analyser",
            "⚖️ MiFID II Best Execution Checker",
            "🤖 Algo Order Execution Scheduler",
            "🏛️ CBDC vs Correspondent Banking Cost Comparator"
        ])

        st.markdown("---")

        # ── CLS NETTING ───────────────────────────────────────────────
        if calc_choice == "🔄 CLS Netting Calculator":
            st.subheader("CLS Netting Efficiency Calculator")
            st.info("Enter your FX trades to calculate gross vs net settlement obligations and CLS netting efficiency.")

            col1, col2 = st.columns(2)
            with col1:
                ccy_a = st.text_input("Currency A", value="EUR")
                ccy_b = st.text_input("Currency B", value="USD")
            with col2:
                num_trades = st.number_input("Number of Trades", min_value=2, max_value=10, value=5)

            default_a  = [100.0, -75.0, 50.0, -120.0, 80.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            default_b  = [-108.5, 81.4, -54.3, 130.2, -86.8, 0.0, 0.0, 0.0, 0.0, 0.0]

            trades = []
            for i in range(int(num_trades)):
                col1, col2, col3 = st.columns(3)
                tid = col1.text_input(f"Trade {i+1}", value=f"T{i+1}", key=f"cls_t_{i}")
                a_amt = col2.number_input(f"{ccy_a} (M)", value=default_a[i], step=5.0, key=f"cls_a_{i}")
                b_amt = col3.number_input(f"{ccy_b} (M)", value=default_b[i], step=5.0, key=f"cls_b_{i}")
                trades.append({"id": tid, "a": a_amt, "b": b_amt})

            if st.button("Calculate CLS Netting", type="primary"):
                net_a   = sum(t["a"] for t in trades)
                net_b   = sum(t["b"] for t in trades)
                gross_a = sum(abs(t["a"]) for t in trades)
                gross_b = sum(abs(t["b"]) for t in trades)
                eff_a   = (1 - abs(net_a) / gross_a) * 100 if gross_a > 0 else 0
                eff_b   = (1 - abs(net_b) / gross_b) * 100 if gross_b > 0 else 0

                rows = []
                for t in trades:
                    rows.append({
                        "Trade": t["id"],
                        f"{ccy_a} (M)": f"{t['a']:+.1f}",
                        f"{ccy_b} (M)": f"{t['b']:+.1f}",
                        f"{ccy_a} Flow": "Buy" if t["a"] > 0 else "Sell",
                        f"{ccy_b} Flow": "Receive" if t["b"] > 0 else "Pay"
                    })
                rows.append({"Trade": "GROSS TOTAL",
                             f"{ccy_a} (M)": f"{gross_a:.1f}",
                             f"{ccy_b} (M)": f"{gross_b:.1f}",
                             f"{ccy_a} Flow": "Sum of abs",
                             f"{ccy_b} Flow": "Sum of abs"})
                rows.append({"Trade": "NET (CLS)",
                             f"{ccy_a} (M)": f"{net_a:+.1f}",
                             f"{ccy_b} (M)": f"{net_b:+.1f}",
                             f"{ccy_a} Flow": "Net obligation",
                             f"{ccy_b} Flow": "Net obligation"})
                st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

                c1, c2, c3, c4 = st.columns(4)
                c1.metric(f"Net {ccy_a}", f"{net_a:+.1f}M")
                c2.metric(f"Net {ccy_b}", f"{net_b:+.1f}M")
                c3.metric(f"{ccy_a} Netting Eff.", f"{eff_a:.1f}%")
                c4.metric(f"{ccy_b} Netting Eff.", f"{eff_b:.1f}%")

                fig = go.Figure(go.Bar(
                    x=["Gross Settlement\n(no netting)", "Net Settlement\n(CLS netting)"],
                    y=[gross_a, abs(net_a)],
                    marker_color=["#E74C3C", "#27AE60"],
                    text=[f"{gross_a:.1f}M", f"{abs(net_a):.1f}M"],
                    textposition="outside"
                ))
                fig.update_layout(
                    title=f"{ccy_a} Settlement Obligation — Gross vs Net",
                    yaxis_title=f"{ccy_a} Amount (M)",
                    yaxis=dict(range=[0, gross_a * 1.3])
                )
                st.plotly_chart(fig, use_container_width=True)

                saving = gross_a - abs(net_a)
                st.success(f"✅ CLS netting saves {eff_a:.1f}% — you fund only {abs(net_a):.1f}M {ccy_a} instead of {gross_a:.1f}M. Capital saving: {saving:.1f}M {ccy_a}.")

        # ── VWAP ANALYSER ─────────────────────────────────────────────
        elif calc_choice == "📊 VWAP Execution Quality Analyser":
            st.subheader("VWAP & Implementation Shortfall Calculator")
            col1, col2 = st.columns(2)
            with col1:
                total_order   = st.number_input("Total Order Size (M base currency)", value=100.0, step=10.0)
                arrival_price = st.number_input("Arrival Price (at order decision)", value=1.0850, format="%.4f")
                pair_v        = st.text_input("Currency Pair", value="EUR/USD", key="vwap_pair")
            with col2:
                num_slices = st.number_input("Number of Execution Slices", min_value=2, max_value=10, value=6)

            st.markdown("**Enter each execution slice (price and size):**")
            default_px = [1.0845, 1.0852, 1.0858, 1.0855, 1.0849, 1.0862, 1.0857, 1.0860, 1.0854, 1.0848]
            default_sz = [10.0, 15.0, 20.0, 18.0, 15.0, 22.0, 12.0, 10.0, 8.0, 5.0]
            slices = []
            for i in range(int(num_slices)):
                col1, col2 = st.columns(2)
                px_i = col1.number_input(f"Slice {i+1} — Price", value=default_px[i], format="%.4f", step=0.0001, key=f"vwap_px_{i}")
                sz_i = col2.number_input(f"Slice {i+1} — Size (M)", value=default_sz[i], step=1.0, key=f"vwap_sz_{i}")
                slices.append({"px": px_i, "sz": sz_i})

            if st.button("Analyse Execution Quality", type="primary"):
                total_exec  = sum(s["sz"] for s in slices)
                exec_vwap   = sum(s["px"] * s["sz"] for s in slices) / total_exec if total_exec > 0 else 0
                mkt_vwap    = sum(s["px"] for s in slices) / len(slices)
                is_bps      = (exec_vwap - arrival_price) / arrival_price * 10000
                vs_mkt_bps  = (exec_vwap - mkt_vwap) / mkt_vwap * 10000
                total_cost  = abs(exec_vwap - arrival_price) * total_exec * 1_000_000

                st.markdown("---")
                st.markdown(f"""
                **Execution Quality Summary:**
                ```
                Total Executed:           {total_exec:.1f}M of {total_order:.1f}M ordered
                Arrival Price:            {arrival_price:.4f}
                Execution VWAP:           {exec_vwap:.5f}
                Market VWAP (benchmark):  {mkt_vwap:.5f}

                Implementation Shortfall: {is_bps:+.2f} bps vs arrival price
                vs Market VWAP:           {vs_mkt_bps:+.2f} bps
                Total Execution Cost:     ${total_cost:,.0f}
                ```
                """)
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Execution VWAP", f"{exec_vwap:.4f}")
                c2.metric("Market VWAP", f"{mkt_vwap:.4f}")
                c3.metric("Impl. Shortfall", f"{is_bps:+.1f} bps")
                c4.metric("Total Cost", f"${total_cost:,.0f}")

                slice_df = pd.DataFrame([{
                    "Slice": i+1,
                    "Exec Price": f"{s['px']:.4f}",
                    "Size (M)": f"{s['sz']:.1f}",
                    "Weight": f"{s['sz']/total_exec*100:.1f}%"
                } for i, s in enumerate(slices)])
                st.dataframe(slice_df, use_container_width=True, hide_index=True)

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=[f"S{i+1}" for i in range(len(slices))],
                    y=[s["px"] for s in slices],
                    mode="lines+markers", name="Execution Price",
                    line=dict(color="#E74C3C", width=2.5)
                ))
                fig.add_hline(y=exec_vwap, line_dash="dash", line_color="#27AE60",
                              annotation_text=f"Exec VWAP {exec_vwap:.4f}")
                fig.add_hline(y=arrival_price, line_dash="dot", line_color="gray",
                              annotation_text=f"Arrival {arrival_price:.4f}")
                fig.update_layout(
                    title=f"{pair_v} VWAP Execution — Slice by Slice",
                    xaxis_title="Execution Slice", yaxis_title="Price"
                )
                st.plotly_chart(fig, use_container_width=True)

                if abs(is_bps) < 5:
                    st.success(f"✅ Excellent execution — IS of {is_bps:+.1f} bps is within best-in-class range.")
                elif abs(is_bps) < 15:
                    st.info(f"ℹ️ Good execution — IS of {is_bps:+.1f} bps is acceptable for this order size.")
                else:
                    st.warning(f"⚠️ High IS of {is_bps:+.1f} bps — review algo settings or split the order further.")

        # ── BEST EXECUTION CHECKER ────────────────────────────────────
        elif calc_choice == "⚖️ MiFID II Best Execution Checker":
            st.subheader("MiFID II Best Execution Assessment Tool")
            st.info("Evaluate whether an FX trade meets MiFID II best execution requirements.")
            col1, col2 = st.columns(2)
            with col1:
                mid_rate    = st.number_input("Mid-market rate at order time", value=1.08500, format="%.5f")
                exec_rate   = st.number_input("Client execution rate", value=1.08520, format="%.5f")
                order_size  = st.number_input("Order notional (M base currency)", value=5.0, step=1.0)
                pair_be     = st.text_input("Currency Pair", value="EUR/USD", key="be_pair")
            with col2:
                exec_ms     = st.number_input("Execution time (milliseconds)", value=45, min_value=1)
                fill_pct    = st.number_input("Fill rate %", value=100.0, step=1.0, min_value=0.0, max_value=100.0)
                mkt_spread  = st.number_input("Typical institutional spread (pips)", value=1.0, step=0.1)
                extra_comm  = st.number_input("Additional commissions (USD)", value=0.0, step=50.0)

            if st.button("Check Best Execution", type="primary"):
                spread_pips = (exec_rate - mid_rate) * 10000
                max_spread  = mkt_spread * 3.0
                total_cost  = (exec_rate - mid_rate) * order_size * 1_000_000 + extra_comm
                cost_bps    = total_cost / (order_size * 1_000_000) * 10000

                factors = [
                    ("1. Price — Spread within norms",
                     spread_pips <= max_spread,
                     f"Spread charged: {spread_pips:.1f} pips | Market norm: {mkt_spread:.1f} pips | Max acceptable: {max_spread:.1f} pips"),
                    ("2. Total Cost (< 10 bps)",
                     cost_bps < 10,
                     f"Total cost: {cost_bps:.2f} bps = ${total_cost:,.0f} on {order_size:.0f}M"),
                    ("3. Speed (< 500ms)",
                     exec_ms < 500,
                     f"Execution time: {exec_ms}ms {'— Excellent' if exec_ms < 100 else '— Acceptable' if exec_ms < 500 else '— Slow'}"),
                    ("4. Fill Rate (>= 95%)",
                     fill_pct >= 95,
                     f"Fill rate: {fill_pct:.1f}%"),
                    ("5. Pair Liquidity",
                     True,
                     f"{pair_be} is liquid — full execution straightforward"),
                ]

                results = [{"Factor": f, "Status": "✅ Pass" if ok else "❌ Fail", "Detail": d}
                           for f, ok, d in factors]
                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

                passes = sum(1 for _, ok, _ in factors if ok)
                c1, c2, c3 = st.columns(3)
                c1.metric("Checks Passed", f"{passes}/{len(factors)}")
                c2.metric("Spread Charged", f"{spread_pips:.1f} pips")
                c3.metric("Total Cost", f"${total_cost:,.0f} ({cost_bps:.2f} bps)")

                if passes == len(factors):
                    st.success("✅ BEST EXECUTION ACHIEVED — All MiFID II factors satisfied. Document in your best execution log.")
                elif passes >= len(factors) - 1:
                    st.warning("⚠️ NEAR BEST EXECUTION — One factor flagged. Document rationale for any deviation from the norm.")
                else:
                    st.error("❌ BEST EXECUTION CONCERN — Multiple factors fail. Review execution process and consider corrective action.")

        # ── ALGO SCHEDULER ────────────────────────────────────────────
        elif calc_choice == "🤖 Algo Order Execution Scheduler":
            st.subheader("Algorithmic FX Order Execution Scheduler")
            st.info("Design a TWAP or VWAP execution schedule for a large FX order.")
            col1, col2 = st.columns(2)
            with col1:
                total_algo  = st.number_input("Total Order Size (M base currency)", value=500.0, step=50.0)
                algo_type   = st.selectbox("Algorithm", ["TWAP (Equal time slices)", "VWAP (Volume-weighted slices)", "Front-loaded (IS — urgent)"])
                start_h     = st.number_input("Start Hour (GMT)", value=8, min_value=0, max_value=23)
                end_h       = st.number_input("End Hour (GMT)", value=16, min_value=1, max_value=24)
            with col2:
                daily_vol   = st.number_input("Estimated Daily Volume (EUR B)", value=800.0, step=50.0)
                slices_n    = st.slider("Number of Slices", 4, 16, 8)
                pair_algo   = st.text_input("Currency Pair", value="EUR/USD", key="algo_p")
                base_price  = st.number_input("Current Price", value=1.0850, format="%.4f")

            if st.button("Generate Execution Schedule", type="primary"):
                duration = max(end_h - start_h, 1)
                hours    = np.linspace(start_h, end_h, slices_n + 1)[:-1]

                if "TWAP" in algo_type:
                    raw_weights = np.ones(slices_n)
                elif "VWAP" in algo_type:
                    raw_weights = np.array([0.8, 1.0, 1.2, 1.5, 1.4, 1.2, 1.1, 1.0,
                                            1.0, 1.2, 1.4, 1.6, 1.5, 1.3, 1.1, 0.9][:slices_n])
                else:
                    raw_weights = np.array([2.0, 1.8, 1.5, 1.2, 1.0, 0.9, 0.8, 0.7,
                                            0.6, 0.6, 0.6, 0.6, 0.5, 0.5, 0.5, 0.5][:slices_n])

                weights        = raw_weights / raw_weights.sum()
                slice_sizes    = weights * total_algo
                cum_sizes      = np.cumsum(slice_sizes)
                participation  = slice_sizes / (daily_vol * 1000 / 8 / slices_n * duration) * 100

                schedule_df = pd.DataFrame({
                    "Slice": list(range(1, slices_n + 1)),
                    "Time (GMT)": [f"{int(h):02d}:{int((h%1)*60):02d}" for h in hours],
                    "Slice Size (M)": [f"{s:.1f}" for s in slice_sizes],
                    "Cumulative (M)": [f"{c:.1f}" for c in cum_sizes],
                    "% of Total": [f"{w*100:.1f}%" for w in weights],
                    "Participation Rate": [f"{p:.2f}%" for p in participation]
                })
                st.dataframe(schedule_df, use_container_width=True, hide_index=True)

                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=[f"{int(h):02d}:{int((h%1)*60):02d}" for h in hours],
                    y=slice_sizes,
                    name="Slice Size (M)", marker_color="#2E86C1"
                ))
                fig.add_trace(go.Scatter(
                    x=[f"{int(h):02d}:{int((h%1)*60):02d}" for h in hours],
                    y=cum_sizes,
                    name="Cumulative (M)", line=dict(color="#E74C3C", width=2.5),
                    yaxis="y2"
                ))
                fig.update_layout(
                    title=f"{pair_algo} — {algo_type} Execution Schedule ({total_algo:.0f}M total)",
                    xaxis_title="Time (GMT)",
                    yaxis=dict(title="Slice Size (M)"),
                    yaxis2=dict(title="Cumulative (M)", overlaying="y", side="right"),
                    legend=dict(x=0.01, y=0.99)
                )
                st.plotly_chart(fig, use_container_width=True)

                avg_part = np.mean(participation)
                st.metric("Average Participation Rate", f"{avg_part:.2f}%")
                if avg_part > 10:
                    st.warning(f"⚠️ High participation rate ({avg_part:.1f}%). Consider extending the execution window to reduce market impact.")
                else:
                    st.success(f"✅ Participation rate of {avg_part:.1f}% is within market impact guidelines (target < 10%).")

        # ── CBDC COMPARATOR ───────────────────────────────────────────
        elif calc_choice == "🏛️ CBDC vs Correspondent Banking Cost Comparator":
            st.subheader("CBDC vs Correspondent Banking — Cost & Speed Comparator")
            st.info("Compare the cost and settlement speed of a cross-border FX payment under current correspondent banking vs CBDC vision.")
            col1, col2 = st.columns(2)
            with col1:
                payment_usd   = st.number_input("Payment Amount (USD equivalent)", value=1000000.0, step=100000.0)
                num_payments  = st.number_input("Number of Payments per Year", value=500, step=50)
                from_country  = st.text_input("Sending Country", value="Singapore")
                to_country    = st.text_input("Receiving Country", value="China")
            with col2:
                st.markdown("**Current Correspondent Banking Costs:**")
                sending_bank_fee  = st.number_input("Sending bank fee (USD)", value=25.0, step=5.0)
                correspondent_fee = st.number_input("Correspondent bank fee (bps)", value=8.0, step=1.0)
                fx_spread_bps     = st.number_input("FX spread cost (bps)", value=15.0, step=1.0)
                settlement_days   = st.number_input("Settlement time (business days)", value=2, min_value=1)

            st.markdown("**CBDC Vision Costs:**")
            col3, col4 = st.columns(2)
            cbdc_fixed    = col3.number_input("CBDC platform fee (USD per txn)", value=2.0, step=0.5)
            cbdc_bps      = col4.number_input("CBDC FX spread (bps)", value=3.0, step=0.5)
            cbdc_seconds  = col3.number_input("CBDC settlement time (seconds)", value=10, min_value=1)

            if st.button("Compare Settlement Methods", type="primary"):
                corr_variable  = (correspondent_fee + fx_spread_bps) / 10000 * payment_usd
                corr_total     = sending_bank_fee + corr_variable
                corr_pct       = corr_total / payment_usd * 100

                cbdc_variable  = cbdc_bps / 10000 * payment_usd
                cbdc_total     = cbdc_fixed + cbdc_variable
                cbdc_pct       = cbdc_total / payment_usd * 100

                saving_per_txn = corr_total - cbdc_total
                saving_annual  = saving_per_txn * num_payments
                saving_pct     = (saving_per_txn / corr_total) * 100

                comparison_df = pd.DataFrame({
                    "Metric": [
                        "Settlement Time",
                        "Fixed Fee",
                        "Variable Cost (FX + intermediary)",
                        "Total Cost per Transaction",
                        "Cost as % of Payment",
                        "Annual Cost (all payments)",
                        "Settlement Risk",
                        "Transparency"
                    ],
                    "Correspondent Banking": [
                        f"{settlement_days} business days",
                        f"${sending_bank_fee:.0f}",
                        f"${corr_variable:,.0f} ({correspondent_fee+fx_spread_bps:.0f} bps)",
                        f"${corr_total:,.2f}",
                        f"{corr_pct:.3f}%",
                        f"${corr_total * num_payments:,.0f}",
                        "Herstatt risk (mitigated by CLS for majors)",
                        "Limited — SWIFT tracking only"
                    ],
                    "CBDC (mBridge Vision)": [
                        f"~{cbdc_seconds} seconds",
                        f"${cbdc_fixed:.0f}",
                        f"${cbdc_variable:,.0f} ({cbdc_bps:.0f} bps)",
                        f"${cbdc_total:,.2f}",
                        f"{cbdc_pct:.3f}%",
                        f"${cbdc_total * num_payments:,.0f}",
                        "Zero (atomic PvP built-in)",
                        "Full real-time (distributed ledger)"
                    ]
                })
                st.dataframe(comparison_df, use_container_width=True, hide_index=True)

                st.markdown("---")
                c1, c2, c3 = st.columns(3)
                c1.metric("Saving per Transaction", f"${saving_per_txn:,.2f}")
                c2.metric("Annual Savings", f"${saving_annual:,.0f}")
                c3.metric("Cost Reduction", f"{saving_pct:.1f}%")

                fig = go.Figure(go.Bar(
                    x=["Correspondent\nBanking", "CBDC\n(mBridge Vision)"],
                    y=[corr_total, cbdc_total],
                    marker_color=["#E74C3C", "#27AE60"],
                    text=[f"${corr_total:,.2f}\n({corr_pct:.2f}%)", f"${cbdc_total:,.2f}\n({cbdc_pct:.2f}%)"],
                    textposition="outside"
                ))
                fig.update_layout(
                    title=f"Cost per ${payment_usd:,.0f} Cross-Border Payment",
                    yaxis_title="Total Cost (USD)",
                    yaxis=dict(range=[0, corr_total * 1.4])
                )
                st.plotly_chart(fig, use_container_width=True)
                st.info(f"💡 CBDC could save {from_country} companies ${saving_annual:,.0f}/year on {num_payments} annual payments to {to_country} — a {saving_pct:.1f}% cost reduction. This is before accounting for the value of faster settlement and eliminated settlement risk.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("CLS Netting Efficiency — Daily Settlement Volume")
        categories = ["Gross Obligations\n(pre-netting)", "After Bilateral\nNetting", "After CLS\nMultilateral Netting"]
        values     = [6500, 900, 250]
        colors     = ["#E74C3C", "#F39C12", "#27AE60"]
        fig1 = go.Figure(go.Bar(
            x=categories, y=values,
            marker_color=colors,
            text=[f"${v}B" for v in values],
            textposition="outside"
        ))
        fig1.add_hline(y=250, line_dash="dash", line_color="#2E86C1",
                       annotation_text="CLS net settlement ~$250B of $6.5T gross")
        fig1.update_layout(
            title="CLS Netting Effect — Daily FX Settlement ($B, illustrative)",
            yaxis_title="Daily Settlement Amount ($B)",
            yaxis=dict(range=[0, 7500])
        )
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Electronic FX Trading Growth — Market Share by Execution Method")
        years_e = [2005, 2008, 2011, 2013, 2016, 2019, 2022]
        voice   = [60, 50, 40, 30, 20, 15, 10]
        single  = [15, 20, 25, 30, 32, 30, 28]
        multi   = [10, 15, 20, 25, 30, 35, 40]
        algo_e  = [5,  8, 10, 12, 15, 18, 22]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=years_e, y=voice,  name="Voice/Phone", line=dict(color="#E74C3C", width=2.5)))
        fig2.add_trace(go.Scatter(x=years_e, y=single, name="Single-dealer Platform", line=dict(color="#2E86C1", width=2.5)))
        fig2.add_trace(go.Scatter(x=years_e, y=multi,  name="Multi-dealer/ECN", line=dict(color="#27AE60", width=2.5)))
        fig2.add_trace(go.Scatter(x=years_e, y=algo_e, name="Algorithmic", line=dict(color="#F39C12", width=2.5)))
        fig2.update_layout(
            title="FX Execution Method Market Share % (2005-2022)",
            xaxis_title="Year", yaxis_title="Market Share %",
            legend=dict(x=0.01, y=0.99)
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("CBDC Cross-Border Pilot Projects Worldwide")
        projects = ["mBridge\n(BIS/CN/AE/TH/HK)", "Project Jura\n(SNB + BdF)", "Project Dunbar\n(MAS+RBA+BNM+SARB)", "Project Nexus\n(BIS/MAS/BoT)", "Digital Euro\n(ECB — Retail)"]
        stages   = [4, 3, 3, 2, 2]
        stage_labels = ["1=Concept", "2=Research", "3=Pilot", "4=MVP Live", "5=Full Launch"]
        fig3 = go.Figure(go.Bar(
            y=projects, x=stages,
            orientation="h",
            marker_color=["#27AE60" if s >= 4 else "#F39C12" if s == 3 else "#E74C3C" for s in stages],
            text=[f"Stage {s}: {stage_labels[s-1].split('=')[1]}" for s in stages],
            textposition="outside"
        ))
        fig3.update_layout(
            title="CBDC Cross-Border Projects — Development Stage (2024)",
            xaxis_title="Stage (1=Concept → 5=Full Launch)",
            xaxis=dict(range=[0, 6])
        )
        st.plotly_chart(fig3, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — Regulation, Settlement & Emerging Topics")

        st.markdown("**Q1. The FX Global Code of Conduct is:**")
        q1 = st.radio("", [
            "A legally binding regulation enforced by the BIS",
            "A voluntary set of principles endorsed by central banks; non-compliance damages market reputation",
            "Mandatory only for banks with assets over $100 billion",
            "A product of the MiFID II regulatory framework in the EU"
        ], key="fx12q1")
        if st.button("Check Q1", key="fx12c1"):
            if "voluntary" in q1 and "central banks" in q1:
                st.success("✅ Correct! The FX Global Code is voluntary but carries significant weight — non-compliance risks loss of market access and counterparty relationships.")
            else:
                st.error("❌ Incorrect. The FX Global Code is VOLUNTARY — not legally binding. Central banks endorse it and participants sign a Statement of Commitment.")
        st.markdown("---")

        st.markdown("**Q2. CLS Bank eliminates Herstatt risk through:**")
        q2 = st.radio("", [
            "Netting all trades to zero before settlement",
            "Payment-vs-Payment (PvP) — both legs settle simultaneously or neither settles",
            "Requiring same-day settlement for all FX trades",
            "Using only USD as the settlement currency for all pairs"
        ], key="fx12q2")
        if st.button("Check Q2", key="fx12c2"):
            if "Payment-vs-Payment" in q2:
                st.success("✅ Correct! CLS PvP: both payment legs settle at the same moment. If one party cannot deliver, NEITHER leg settles — principal risk is completely eliminated.")
            else:
                st.error("❌ Incorrect. CLS eliminates Herstatt risk via Payment-vs-Payment (PvP). Both legs of the trade settle simultaneously — no exposure to one party paying without receiving.")
        st.markdown("---")

        st.markdown("**Q3. Under MiFID II, best execution for FX considers:**")
        q3 = st.radio("", [
            "Only the tightest bid-ask spread available at the time",
            "Price, total costs, speed, likelihood of execution — not just best price",
            "Only electronically traded execution venues",
            "The client's historical trading patterns only"
        ], key="fx12q3")
        if st.button("Check Q3", key="fx12c3"):
            if "Price, total costs, speed" in q3:
                st.success("✅ Correct! MiFID II best execution is a multi-factor test: total consideration (price + all costs), speed, likelihood of execution and settlement, and other relevant factors.")
            else:
                st.error("❌ Incorrect. MiFID II best execution considers MULTIPLE factors: price, costs, speed, likelihood of execution and settlement, size/nature of order, and market impact.")
        st.markdown("---")

        st.markdown("**Q4. Under Dodd-Frank, a firm must register as a Swap Dealer if its annual FX derivative notional exceeds:**")
        q4 = st.radio("", [
            "$1 billion",
            "$8 billion",
            "$50 billion",
            "$100 billion"
        ], key="fx12q4")
        if st.button("Check Q4", key="fx12c4"):
            if "$8 billion" in q4:
                st.success("✅ Correct! The Dodd-Frank de minimis threshold for Swap Dealer registration is $8 billion in FX derivatives notional over a rolling 12-month period (as of 2024).")
            else:
                st.error("❌ Incorrect. Dodd-Frank Swap Dealer registration threshold = $8 billion in annual FX derivative notional. Below this = de minimis exemption applies.")
        st.markdown("---")

        st.markdown("**Q5. The mBridge CBDC project primarily aims to:**")
        q5 = st.radio("", [
            "Create a single global digital currency to replace all national currencies",
            "Enable direct multi-CBDC cross-border FX settlement in seconds, bypassing correspondent banking",
            "Replace SWIFT entirely by the end of 2025",
            "Create a gold-backed stablecoin for emerging markets"
        ], key="fx12q5")
        if st.button("Check Q5", key="fx12c5"):
            if "multi-CBDC cross-border FX settlement" in q5:
                st.success("✅ Correct! mBridge (BIS + China, UAE, Thailand, HK) enables direct multi-CBDC payments settled atomically in seconds — bypassing the correspondent banking chain entirely.")
            else:
                st.error("❌ Incorrect. mBridge = multi-CBDC platform for direct cross-border FX settlement. It settles transactions in seconds via atomic PvP exchange, bypassing correspondent banks.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Regulatory Frameworks — Quick Reference")
        reg_df = pd.DataFrame({
            "Framework": ["FX Global Code", "CLS Settlement", "MiFID II", "Dodd-Frank", "EMIR"],
            "Jurisdiction": ["Global (voluntary)", "Global", "European Union", "United States", "European Union"],
            "Key Requirement": [
                "Ethics, governance, execution fairness, information barriers",
                "PvP settlement eliminates Herstatt risk for 18 currencies",
                "Best execution (multi-factor), trade reporting, TCA",
                "Swap dealer registration > $8B, central clearing, margin",
                "OTC derivative reporting to trade repositories"
            ],
            "Who It Applies To": [
                "All FX market participants (voluntary sign-up)",
                "~70 settlement member banks globally",
                "EU investment firms dealing FX for clients",
                "US persons and swap dealers above threshold",
                "EU counterparties to OTC FX derivatives"
            ]
        })
        st.dataframe(reg_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Execution Formulas & Benchmarks")
        formulas_df = pd.DataFrame({
            "Metric": [
                "VWAP",
                "Implementation Shortfall",
                "Best Execution Spread Check",
                "CLS Netting Efficiency",
                "Dodd-Frank Threshold",
                "IFRS 9 Effectiveness"
            ],
            "Formula": [
                "Sum(Price_i x Size_i) / Sum(Size_i)",
                "(Execution Price - Arrival Price) / Arrival Price x 10,000 bps",
                "Spread charged <= 3x typical market spread",
                "(1 - Net Obligation / Gross Obligation) x 100%",
                "FX derivative notional > $8B/year = Swap Dealer registration",
                "80% to 125% band required (Module 8)"
            ],
            "Target / Benchmark": [
                "Execution VWAP <= market VWAP (for buy orders)",
                "< 10 bps for liquid pairs; < 25 bps for less liquid",
                "Must document rationale if > 3x market spread",
                "CLS typically achieves 96-98% netting efficiency",
                "Below $8B = de minimis exemption",
                "Outside band = hedge accounting disqualified"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔮 Future of FX — Emerging Topics Summary")
        future_df = pd.DataFrame({
            "Topic": ["CBDCs (Wholesale)", "CBDCs (Retail)", "mBridge", "AI/ML in FX", "DeFi FX", "ISO 20022 (SWIFT gpi)"],
            "Current Status": [
                "Multiple live pilots (mBridge, Jura, Dunbar)",
                "Pilots in China (e-CNY), EU (Digital Euro research)",
                "MVP launched 2024 — live cross-border transactions",
                "Widely deployed for execution algo, risk management",
                "Nascent — crypto FX on decentralised exchanges",
                "Global migration underway — richer payment data"
            ],
            "FX Impact": [
                "Atomic PvP settlement, eliminate Herstatt risk",
                "Faster retail FX; reduce remittance costs",
                "Bypass correspondent banking; reduce T+2 to seconds",
                "Better execution quality, real-time risk monitoring",
                "Crypto/fiat FX gateways; stablecoin FX",
                "Faster reconciliation; reduce failed trades"
            ],
            "Timeline": ["2025-2030", "2027-2032", "2025-2027", "Now (deployed)", "3-10 years", "2023-2025"]
        })
        st.dataframe(future_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Compliance Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Signing FX Global Code without implementing the governance requirements",
                "Relying only on spread for best execution assessment",
                "Missing Dodd-Frank SDR reporting deadlines",
                "Settling large FX trades outside CLS without bilateral credit limits",
                "Using voice execution without post-trade TCA analysis"
            ],
            "Correct Approach": [
                "Statement of Commitment requires actual implementation: governance docs, training, annual review",
                "Best execution = multi-factor under MiFID II: price + speed + fill rate + total cost",
                "SDR reporting is same-day (T+0 for new trades). Late reporting = regulatory penalty",
                "For non-CLS currencies or counterparties: set bilateral credit limits; use ISDA agreements",
                "All execution should be TCA-benchmarked; document quality annually per RTS 27/28"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 12 Complete! You understand FX regulation (Global Code, MiFID II, Dodd-Frank), CLS settlement mechanics, algorithmic execution, and emerging CBDC developments.")

        st.markdown("---")
        st.markdown("## 🏆 Congratulations — FX Curriculum Complete!")
        st.markdown("""
        You have now completed all **12 modules** of the Foreign Exchange Expert Mastery Curriculum.

        | Phase | Modules | Topics Covered |
        |-------|---------|----------------|
        | **Foundation** | M1–M2 | Market structure, spot quotes, settlement, SWIFT |
        | **Core Theory** | M3–M6 | PPP, IRP, forwards, swaps, options foundations |
        | **Advanced** | M7–M9 | Exotic options, risk management, macro drivers |
        | **Professional** | M10–M12 | Technical analysis, capital markets, regulation |

        **You can now confidently:**
        - Price forward contracts, FX options, and cross-currency swaps
        - Measure and manage transaction, translation, and economic FX exposure
        - Apply VaR, hedge ratios, and IFRS 9 hedge accounting
        - Analyse macro drivers including carry trade and central bank policy
        - Read FX charts using RSI, MACD, Fibonacci, and Bollinger Bands
        - Structure cross-border M&A deals with appropriate FX hedges
        - Navigate FX regulation and understand the future impact of CBDCs
        """)
        st.info("💡 **Next Steps**: Apply these frameworks to real market data, build your own FX analytics spreadsheet, and stay current with central bank decisions, CCS basis levels, and CBDC developments.")

if __name__ == "__main__":
    show()