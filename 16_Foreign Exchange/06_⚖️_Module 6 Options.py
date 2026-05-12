import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from scipy.stats import norm

# ── Garman-Kohlhagen pricing engine ─────────────────────────────────────────
def gk_price(S, K, r_d, r_f, T, sigma, opt_type="call"):
    if T <= 0 or sigma <= 0 or S <= 0 or K <= 0:
        return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    d1 = (np.log(S / K) + (r_d - r_f + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if opt_type == "call":
        price = S * np.exp(-r_f * T) * norm.cdf(d1) - K * np.exp(-r_d * T) * norm.cdf(d2)
        delta = np.exp(-r_f * T) * norm.cdf(d1)
    else:
        price = K * np.exp(-r_d * T) * norm.cdf(-d2) - S * np.exp(-r_f * T) * norm.cdf(-d1)
        delta = -np.exp(-r_f * T) * norm.cdf(-d1)
    gamma = np.exp(-r_f * T) * norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega  = S * np.exp(-r_f * T) * norm.pdf(d1) * np.sqrt(T) / 100
    theta = (-(S * np.exp(-r_f * T) * norm.pdf(d1) * sigma / (2 * np.sqrt(T)))
             - r_d * K * np.exp(-r_d * T) * norm.cdf(d2 if opt_type == "call" else -d2)
             + r_f * S * np.exp(-r_f * T) * norm.cdf(d1 if opt_type == "call" else -d1)) / 365
    rho = K * T * np.exp(-r_d * T) * norm.cdf(d2 if opt_type == "call" else -d2) / 100
    return round(price, 6), round(delta, 4), round(gamma, 6), round(vega, 4), round(theta, 6), round(rho, 4)

def show():
    st.title("📊 Module 6: FX Options — Foundations")
    st.markdown("*Master the Garman-Kohlhagen model, option Greeks, put-call parity, and basic FX hedging strategies*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. FX Options — What Are They?")
        st.markdown("""
        An **FX option** gives the buyer the **right, but not the obligation**, to exchange
        a specified amount of currency at a predetermined rate (the **strike**) on or before
        the expiry date. The buyer pays a **premium** upfront.

        | Feature | Call Option | Put Option |
        |---------|------------|-----------|
        | **Right** | Buy base currency at strike K | Sell base currency at strike K |
        | **Exercise when** | Spot > Strike (ITM) | Spot < Strike (ITM) |
        | **Max loss (buyer)** | Premium paid | Premium paid |
        | **Max gain (buyer)** | Unlimited | Strike − Premium |
        | **Obligation (seller)** | Must sell at K if exercised | Must buy at K if exercised |

        **Option vs Forward:**
        - Forward: obligatory, zero premium, no upside
        - Option: optional, premium cost, retains upside if rates move favourably
        """)

        st.subheader("2. Moneyness")
        st.markdown("""
        | Moneyness | Call | Put | Intrinsic Value |
        |-----------|------|-----|----------------|
        | **In-the-Money (ITM)** | Spot > Strike | Spot < Strike | Positive |
        | **At-the-Money (ATM)** | Spot ≈ Strike | Spot ≈ Strike | Zero |
        | **Out-of-the-Money (OTM)** | Spot < Strike | Spot > Strike | Zero |

        ```
        Option Premium = Intrinsic Value + Time Value

        Intrinsic Value (call) = max(Spot - Strike, 0)
        Intrinsic Value (put)  = max(Strike - Spot, 0)
        Time Value             = Premium - Intrinsic Value
        ```
        ATM options have the **highest time value** and the highest sensitivity to volatility.
        """)

        st.subheader("3. Garman-Kohlhagen (GK) Model")
        st.markdown("""
        The **Garman-Kohlhagen** model is the FX extension of Black-Scholes. The key difference:
        the foreign interest rate is treated as a **continuous dividend yield** (since holding
        foreign currency earns the foreign risk-free rate).

        ```
        d1 = [ln(S/K) + (r_d - r_f + sigma^2/2) x T] / (sigma x sqrt(T))
        d2 = d1 - sigma x sqrt(T)

        Call = S x e^(-r_f x T) x N(d1) - K x e^(-r_d x T) x N(d2)
        Put  = K x e^(-r_d x T) x N(-d2) - S x e^(-r_f x T) x N(-d1)
        ```

        | Input | Symbol | Description |
        |-------|--------|-------------|
        | Spot rate | S | Current exchange rate |
        | Strike rate | K | Agreed exchange rate |
        | Domestic rate | r_d | Quote currency risk-free rate |
        | Foreign rate | r_f | Base currency risk-free rate |
        | Time to expiry | T | In years (e.g., 90 days = 0.25Y) |
        | Volatility | sigma | Implied volatility (annualised) |
        """)

        st.subheader("4. The Option Greeks")
        st.markdown("""
        The **Greeks** measure how the option price changes with each input:

        | Greek | Symbol | Measures | Call Value | ATM Approx |
        |-------|--------|---------|------------|-----------|
        | **Delta** | Delta | Price change per 1 unit spot move | 0 to 1 | ~0.50 |
        | **Gamma** | Gamma | Delta change per 1 unit spot move | Always + | Highest at ATM |
        | **Vega** | Vega | Price change per 1% vol move | Always + | Highest at ATM |
        | **Theta** | Theta | Price change per 1 day passing | Always - | Accelerates near expiry |
        | **Rho** | Rho | Price change per 1% rate move | + for calls | Smaller effect in FX |

        **Key relationships:**
        - Long options: positive vega (benefit from rising vol), negative theta (decay hurts)
        - Delta + |Put delta| ≈ 1 (for options with same strike/expiry)
        - Delta ≈ probability of expiring ITM (approximate)
        """)

        st.subheader("5. Put-Call Parity in FX")
        st.markdown("""
        **Put-Call Parity** links call and put prices with the same strike and expiry:
        ```
        C - P = S x e^(-r_f x T) - K x e^(-r_d x T)

        Rearranged:
        P = C - S x e^(-r_f x T) + K x e^(-r_d x T)
        C = P + S x e^(-r_f x T) - K x e^(-r_d x T)
        ```
        Any violation = arbitrage opportunity. Traders enforce this continuously.
        """)

        st.subheader("6. Basic FX Hedging Strategies")
        st.markdown("""
        | Strategy | Structure | Best For |
        |---------|-----------|---------|
        | **Protective Put** | Buy put option | Exporter hedging against USD weakness |
        | **Covered Call** | Buy forward + sell OTM call | Importer reducing hedge cost |
        | **Zero-Cost Collar** | Buy put + sell call (same premium) | Full protection, no net premium |
        | **Risk Reversal** | Buy OTM call + sell OTM put | Directional view with limited cost |

        **Zero-Cost Collar example:**
        - Exporter buys USD put at 1.25 (protection floor)
        - Simultaneously sells USD call at 1.30 (cap on upside)
        - Net premium = zero (put premium = call premium received)
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: GK Call Option Pricing — Step by Step")
        st.markdown("""
        **Given:** EUR/USD S=1.0850, K=1.0900, r_d=5.25%, r_f=3.75%, T=0.25Y (90 days), sigma=8%

        **Step 1: Calculate d1 and d2**
        ```
        d1 = [ln(1.0850/1.0900) + (0.0525 - 0.0375 + 0.5 x 0.08^2) x 0.25]
              / (0.08 x sqrt(0.25))

           = [ln(0.99541) + (0.0150 + 0.0032) x 0.25] / (0.08 x 0.5)

           = [-0.004604 + 0.004550] / 0.04

           = -0.000054 / 0.04 = -0.0014

        d2 = -0.0014 - 0.08 x sqrt(0.25) = -0.0014 - 0.04 = -0.0414
        ```

        **Step 2: Look up N(d1) and N(d2)**
        ```
        N(d1) = N(-0.0014) = 0.4994
        N(d2) = N(-0.0414) = 0.4835
        ```

        **Step 3: Calculate Call Price**
        ```
        Call = 1.0850 x e^(-0.0375 x 0.25) x 0.4994
               - 1.0900 x e^(-0.0525 x 0.25) x 0.4835

             = 1.0850 x 0.9907 x 0.4994
               - 1.0900 x 0.9870 x 0.4835

             = 0.5359 - 0.5200

             = 0.0159 = 159 pips (approx 1.47% of spot)
        ```

        **Interpretation:** The 90-day EUR/USD call with strike 1.0900 costs approximately 159 pips.
        For EUR 1,000,000 notional: premium = $15,900.
        """)

        st.subheader("Example 2: Delta Hedging")
        st.markdown("""
        **Scenario:** Market maker sells EUR/USD call, delta = 0.50, notional EUR 1,000,000

        ```
        Delta Hedge Required:
        The market maker is SHORT the call (negative delta).
        To be delta-neutral: BUY EUR 1,000,000 x 0.50 = EUR 500,000 in spot market.

        If EUR/USD rises from 1.0850 to 1.0950 (+100 pips):
          Option delta increases to 0.58 (gamma effect)
          New hedge: EUR 1,000,000 x 0.58 = EUR 580,000
          → Must BUY additional EUR 80,000 in spot

        Cost of daily rebalancing = gamma x (spot move)^2 / 2
        This is why option sellers collect premium — they need it to cover rebalancing costs.
        ```
        """)

        st.subheader("Example 3: Put-Call Parity Check")
        st.markdown("""
        **Given:** EUR/USD S=1.0850, K=1.0900, r_d=5.25%, r_f=3.75%, T=0.25Y
        Call price = 0.0159

        **Calculate fair put price using put-call parity:**
        ```
        P = C - S x e^(-r_f x T) + K x e^(-r_d x T)
          = 0.0159 - 1.0850 x e^(-0.0094) + 1.0900 x e^(-0.0131)
          = 0.0159 - 1.0850 x 0.9906 + 1.0900 x 0.9870
          = 0.0159 - 1.0748 + 1.0759
          = 0.0170

        Put price = 0.0170 = 170 pips
        ```

        If market put = 0.0200 (overpriced by 30 pips):
        Arbitrage: Buy call + Sell put + Sell spot + Invest PV(K) → Riskless profit of 30 pips.
        """)

        st.subheader("Example 4: Exporter Using a Protective Put")
        st.markdown("""
        **Scenario:** Singapore exporter expects USD 5,000,000 in 90 days.
        Current GBP/USD = 1.2700. Buys USD put (right to sell USD) at strike 1.2700.
        Put premium = 100 pips = 0.0100 (cost: 0.0100 x USD 5M = USD 50,000)

        | Market Rate at Expiry | Without Hedge | With Put Hedge | Net Result |
        |----------------------|--------------|----------------|-----------|
        | 1.3000 | GBP 3,846,154 | GBP 3,794,644 | Let put expire, keep gain |
        | 1.2700 | GBP 3,937,008 | GBP 3,897,638 | ATM — pay only premium |
        | 1.2400 | GBP 4,032,258 | GBP 3,897,638 | Exercise put at 1.2700 |
        | 1.2000 | GBP 4,166,667 | GBP 3,897,638 | Exercise put — saved loss |
        | 1.1700 | GBP 4,273,504 | GBP 3,897,638 | Exercise put — large save |

        The put provides a **floor** at 1.2700 while keeping upside if USD strengthens.
        Cost of insurance = GBP equivalent of USD 50,000 premium.
        """)

        st.subheader("Example 5: Zero-Cost Collar")
        st.markdown("""
        **Scenario:** UK exporter, 6-month horizon, GBP/USD spot = 1.2700

        **Structure:**
        ```
        Buy USD put (downside protection):
          Strike = 1.2500 (floor)
          Premium paid = 90 pips

        Sell USD call (cap on upside):
          Strike = 1.3000 (ceiling)
          Premium received = 90 pips

        Net premium = 90 - 90 = ZERO (zero-cost collar)

        Outcome range:
          GBP/USD < 1.2500 → Exercise put, effective rate = 1.2500
          GBP/USD 1.2500-1.3000 → No exercise, convert at market rate
          GBP/USD > 1.3000 → Call exercised against you, effective rate = 1.3000
        ```

        The exporter is protected below 1.2500 and participates up to 1.3000.
        Above 1.3000, gains are capped because the sold call is exercised by the buyer.
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "🧮 Garman-Kohlhagen Option Pricer",
            "📐 Greeks Calculator",
            "⚖️ Put-Call Parity Checker",
            "🛡️ Hedge Strategy Payoff Builder",
            "💰 Option P&L at Expiry"
        ])

        st.markdown("---")

        if calc_choice == "🧮 Garman-Kohlhagen Option Pricer":
            st.subheader("Garman-Kohlhagen FX Option Pricing Model")
            col1, col2 = st.columns(2)
            with col1:
                S_gk = st.number_input("Spot Rate (S)", value=1.0850, format="%.4f", step=0.0001)
                K_gk = st.number_input("Strike Rate (K)", value=1.0900, format="%.4f", step=0.0001)
                rd_gk = st.number_input("Domestic Rate % (r_d, quote ccy)", value=5.25, step=0.05)
                rf_gk = st.number_input("Foreign Rate % (r_f, base ccy)", value=3.75, step=0.05)
            with col2:
                T_days = st.number_input("Days to Expiry", value=90, step=1, min_value=1)
                sig_gk = st.number_input("Implied Volatility %", value=8.0, step=0.5, min_value=0.1)
                opt_gk = st.radio("Option Type", ["Call", "Put"])
                notl_gk = st.number_input("Notional (base currency)", value=1000000.0, step=100000.0)

            if st.button("Price Option", type="primary"):
                T_gk = T_days / 365
                price, delta, gamma, vega, theta, rho = gk_price(
                    S_gk, K_gk, rd_gk/100, rf_gk/100, T_gk, sig_gk/100, opt_gk.lower())

                d1_v = (np.log(S_gk/K_gk) + (rd_gk/100 - rf_gk/100 + 0.5*(sig_gk/100)**2)*T_gk) / (sig_gk/100*np.sqrt(T_gk))
                d2_v = d1_v - sig_gk/100*np.sqrt(T_gk)
                intrinsic = max(S_gk - K_gk, 0) if opt_gk == "Call" else max(K_gk - S_gk, 0)
                time_val = price - intrinsic
                total_prem = price * notl_gk

                st.markdown("---")
                st.markdown(f"""
                **GK Option Price Breakdown:**
                ```
                d1 = {d1_v:.4f}   N(d1) = {norm.cdf(d1_v):.4f}
                d2 = {d2_v:.4f}   N(d2) = {norm.cdf(d2_v):.4f}

                Option Price:     {price:.4f} ({price*10000:.1f} pips)
                Intrinsic Value:  {intrinsic:.4f}
                Time Value:       {time_val:.4f}
                Total Premium:    {total_prem:,.2f} quote currency
                As % of Spot:     {price/S_gk*100:.3f}%
                ```
                """)
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Option Price", f"{price:.4f}")
                c2.metric("Pips", f"{price*10000:.1f}")
                c3.metric("Intrinsic", f"{intrinsic:.4f}")
                c4.metric("Total Premium", f"{total_prem:,.0f}")

                st.markdown("---")
                st.markdown("**Option Greeks:**")
                g1, g2, g3, g4, g5 = st.columns(5)
                g1.metric("Delta (Δ)", f"{delta:.4f}", help="Price change per 1 unit spot move")
                g2.metric("Gamma (Γ)", f"{gamma:.6f}", help="Delta change per 1 unit spot move")
                g3.metric("Vega (ν)", f"{vega:.4f}", help="Price change per 1% vol move")
                g4.metric("Theta (Θ)", f"{theta:.6f}", help="Price change per 1 day passing")
                g5.metric("Rho (ρ)", f"{rho:.4f}", help="Price change per 1% rate move")

                st.info(f"Delta hedge: {'Sell' if opt_gk == 'Call' else 'Buy'} {abs(delta) * notl_gk:,.0f} units of base currency to be delta-neutral.")

        elif calc_choice == "📐 Greeks Calculator":
            st.subheader("Option Greeks Sensitivity Analysis")
            col1, col2 = st.columns(2)
            with col1:
                S_gr = st.number_input("Spot Rate", value=1.0850, format="%.4f", key="gr_s")
                K_gr = st.number_input("Strike Rate", value=1.0900, format="%.4f", key="gr_k")
                rd_gr = st.number_input("Domestic Rate %", value=5.25, key="gr_rd")
                rf_gr = st.number_input("Foreign Rate %", value=3.75, key="gr_rf")
            with col2:
                T_gr = st.number_input("Days to Expiry", value=90, step=1, key="gr_t")
                sig_gr = st.number_input("Implied Vol %", value=8.0, step=0.5, key="gr_sig")

            if st.button("Calculate Greeks Sensitivity", type="primary"):
                spot_range = np.linspace(S_gr * 0.95, S_gr * 1.05, 50)
                call_prices = [gk_price(s, K_gr, rd_gr/100, rf_gr/100, T_gr/365, sig_gr/100, "call")[0] for s in spot_range]
                deltas_c = [gk_price(s, K_gr, rd_gr/100, rf_gr/100, T_gr/365, sig_gr/100, "call")[1] for s in spot_range]
                put_prices = [gk_price(s, K_gr, rd_gr/100, rf_gr/100, T_gr/365, sig_gr/100, "put")[0] for s in spot_range]
                deltas_p = [gk_price(s, K_gr, rd_gr/100, rf_gr/100, T_gr/365, sig_gr/100, "put")[1] for s in spot_range]

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=spot_range, y=call_prices, name="Call Price",
                    line=dict(color="#27AE60", width=2.5)))
                fig.add_trace(go.Scatter(x=spot_range, y=put_prices, name="Put Price",
                    line=dict(color="#E74C3C", width=2.5)))
                fig.add_vline(x=K_gr, line_dash="dash", annotation_text=f"Strike {K_gr:.4f}")
                fig.add_vline(x=S_gr, line_dash="dot", line_color="gray", annotation_text=f"Spot {S_gr:.4f}")
                fig.update_layout(title="Option Price vs Spot Rate", xaxis_title="Spot Rate", yaxis_title="Option Price")
                st.plotly_chart(fig, use_container_width=True)

                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(x=spot_range, y=deltas_c, name="Call Delta",
                    line=dict(color="#27AE60", width=2.5)))
                fig2.add_trace(go.Scatter(x=spot_range, y=deltas_p, name="Put Delta",
                    line=dict(color="#E74C3C", width=2.5)))
                fig2.add_hline(y=0, line_color="black", line_dash="dash")
                fig2.add_vline(x=K_gr, line_dash="dash", annotation_text=f"Strike {K_gr:.4f}")
                fig2.update_layout(title="Delta vs Spot Rate", xaxis_title="Spot Rate", yaxis_title="Delta")
                st.plotly_chart(fig2, use_container_width=True)

        elif calc_choice == "⚖️ Put-Call Parity Checker":
            st.subheader("Put-Call Parity Arbitrage Checker")
            col1, col2 = st.columns(2)
            with col1:
                S_pcp = st.number_input("Spot Rate (S)", value=1.0850, format="%.4f", key="pcp_s")
                K_pcp = st.number_input("Strike Rate (K)", value=1.0900, format="%.4f", key="pcp_k")
                rd_pcp = st.number_input("Domestic Rate % (r_d)", value=5.25, key="pcp_rd")
                rf_pcp = st.number_input("Foreign Rate % (r_f)", value=3.75, key="pcp_rf")
            with col2:
                T_pcp = st.number_input("Days to Expiry", value=90, step=1, key="pcp_t")
                call_mkt = st.number_input("Market Call Price", value=0.0159, format="%.4f", key="pcp_c")
                put_mkt = st.number_input("Market Put Price", value=0.0200, format="%.4f", key="pcp_p")

            if st.button("Check Put-Call Parity", type="primary"):
                T_y = T_pcp / 365
                lhs = call_mkt - put_mkt
                rhs = S_pcp * np.exp(-rf_pcp/100 * T_y) - K_pcp * np.exp(-rd_pcp/100 * T_y)
                parity_gap = (lhs - rhs) * 10000
                fair_put = call_mkt - rhs
                fair_call = put_mkt + rhs

                st.markdown("---")
                st.markdown(f"""
                **Put-Call Parity Check:**
                ```
                Formula: C - P = S x e^(-r_f x T) - K x e^(-r_d x T)

                LHS (C - P):    {call_mkt:.4f} - {put_mkt:.4f} = {lhs:.4f}
                RHS calculation: {S_pcp:.4f} x e^(-{rf_pcp:.2f}% x {T_pcp/365:.3f})
                                 - {K_pcp:.4f} x e^(-{rd_pcp:.2f}% x {T_pcp/365:.3f})
                               = {rhs:.4f}

                Parity Gap:      {parity_gap:+.1f} pips
                Fair Put price:  {fair_put:.4f}
                Fair Call price: {fair_call:.4f}
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("Parity Gap", f"{parity_gap:+.1f} pips")
                c2.metric("Fair Put", f"{fair_put:.4f}")
                c3.metric("Fair Call", f"{fair_call:.4f}")

                if abs(parity_gap) < 2:
                    st.success(f"✅ Put-call parity holds — gap = {parity_gap:.1f} pips (within bid-ask spread).")
                elif parity_gap > 0:
                    st.warning(f"⚠️ Call overpriced / Put underpriced by {parity_gap:.1f} pips. Arbitrage: Sell call, buy put, buy spot, borrow PV(K).")
                else:
                    st.warning(f"⚠️ Put overpriced / Call underpriced by {abs(parity_gap):.1f} pips. Arbitrage: Buy call, sell put, sell spot, invest PV(K).")

        elif calc_choice == "🛡️ Hedge Strategy Payoff Builder":
            st.subheader("FX Option Hedge Strategy Payoff Diagram")
            col1, col2 = st.columns(2)
            with col1:
                strategy = st.selectbox("Strategy", [
                    "Long Call (Importer protection)",
                    "Long Put (Exporter protection)",
                    "Zero-Cost Collar (Exporter)",
                    "Bull Spread (Directional call)"
                ])
                spot_curr = st.number_input("Current Spot", value=1.2700, format="%.4f", key="hpb_s")
                notional_h = st.number_input("Notional (base currency)", value=1000000.0, step=100000.0)
            with col2:
                k1 = st.number_input("Strike 1 (K1)", value=1.2700, format="%.4f", key="hpb_k1")
                prem1 = st.number_input("Premium 1 (pips)", value=100.0, step=5.0)
                if "Collar" in strategy or "Spread" in strategy:
                    k2 = st.number_input("Strike 2 (K2)", value=1.3200, format="%.4f", key="hpb_k2")
                    prem2 = st.number_input("Premium 2 received (pips)", value=100.0, step=5.0)
                else:
                    k2, prem2 = k1, 0.0

            if st.button("Build Payoff Diagram", type="primary"):
                spots = np.linspace(spot_curr * 0.90, spot_curr * 1.10, 200)
                net_prem1 = prem1 * 0.0001
                net_prem2 = prem2 * 0.0001

                if "Long Call" in strategy:
                    payoff = [max(s - k1, 0) - net_prem1 for s in spots]
                    title_str = f"Long Call — Strike {k1:.4f}, Premium {prem1:.0f} pips"
                elif "Long Put" in strategy:
                    payoff = [max(k1 - s, 0) - net_prem1 for s in spots]
                    title_str = f"Long Put — Strike {k1:.4f}, Premium {prem1:.0f} pips"
                elif "Zero-Cost Collar" in strategy:
                    payoff = [max(k1 - s, 0) - net_prem1 - max(s - k2, 0) + net_prem2 for s in spots]
                    title_str = f"Zero-Cost Collar — Put {k1:.4f} / Call {k2:.4f}"
                else:
                    payoff = [max(s - k1, 0) - net_prem1 - max(s - k2, 0) + net_prem2 for s in spots]
                    title_str = f"Bull Spread — K1 {k1:.4f} / K2 {k2:.4f}"

                payoff_dollar = [p * notional_h for p in payoff]
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=spots, y=payoff_dollar, mode="lines",
                    line=dict(color="#2E86C1", width=2.5), name="P&L"))
                fig.add_hline(y=0, line_color="black", line_dash="dash")
                fig.add_vline(x=spot_curr, line_dash="dot", line_color="gray",
                             annotation_text=f"Spot {spot_curr:.4f}")
                fig.update_layout(title=title_str + f" — Notional {notional_h:,.0f}",
                                  xaxis_title="Spot Rate at Expiry", yaxis_title="P&L (quote currency)")
                st.plotly_chart(fig, use_container_width=True)

        elif calc_choice == "💰 Option P&L at Expiry":
            st.subheader("Option P&L at Expiry Calculator")
            col1, col2 = st.columns(2)
            with col1:
                opt_type_pl = st.radio("Option Type", ["Call (bought)", "Put (bought)", "Call (sold)", "Put (sold)"])
                strike_pl = st.number_input("Strike Rate", value=1.0900, format="%.4f", key="pl_k")
                premium_pl = st.number_input("Premium Paid/Received (pips)", value=159.0, step=1.0)
            with col2:
                expiry_spot = st.number_input("Spot Rate at Expiry", value=1.0950, format="%.4f", key="pl_exp")
                notional_pl = st.number_input("Notional (base currency)", value=1000000.0, step=100000.0)

            if st.button("Calculate P&L at Expiry", type="primary"):
                prem_rate = premium_pl * 0.0001
                if "Call (bought)" in opt_type_pl:
                    intrinsic = max(expiry_spot - strike_pl, 0)
                    pnl_rate = intrinsic - prem_rate
                    exercised = expiry_spot > strike_pl
                elif "Put (bought)" in opt_type_pl:
                    intrinsic = max(strike_pl - expiry_spot, 0)
                    pnl_rate = intrinsic - prem_rate
                    exercised = expiry_spot < strike_pl
                elif "Call (sold)" in opt_type_pl:
                    intrinsic = max(expiry_spot - strike_pl, 0)
                    pnl_rate = prem_rate - intrinsic
                    exercised = expiry_spot > strike_pl
                else:
                    intrinsic = max(strike_pl - expiry_spot, 0)
                    pnl_rate = prem_rate - intrinsic
                    exercised = expiry_spot < strike_pl

                pnl_dollar = pnl_rate * notional_pl

                st.markdown("---")
                st.markdown(f"""
                **P&L at Expiry:**
                ```
                Spot at Expiry:     {expiry_spot:.4f}
                Strike:             {strike_pl:.4f}
                Intrinsic Value:    {intrinsic:.4f} ({intrinsic*10000:.1f} pips)
                Premium:            {prem_rate:.4f} ({premium_pl:.1f} pips)
                Net P&L per unit:   {pnl_rate:+.4f} ({pnl_rate*10000:+.1f} pips)
                Total P&L:          {pnl_dollar:+,.2f} quote currency
                Exercised?          {'Yes' if exercised else 'No — option expires worthless'}
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("P&L (pips)", f"{pnl_rate*10000:+.1f}")
                c2.metric("Total P&L", f"{pnl_dollar:+,.0f}")
                c3.metric("Exercised", "Yes" if exercised else "No")
                if pnl_dollar > 0:
                    st.success(f"✅ Profitable! Net gain: {pnl_dollar:+,.2f} quote currency.")
                elif pnl_dollar < 0:
                    st.error(f"❌ Net loss: {pnl_dollar:+,.2f} quote currency.")
                else:
                    st.info("Break-even.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("Option Payoff Diagrams — Call vs Put")
        K_vis = 1.0900
        prem_vis = 0.0159
        spots_vis = np.linspace(1.04, 1.14, 200)

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=spots_vis, y=[max(s - K_vis, 0) - prem_vis for s in spots_vis],
            name="Long Call", line=dict(color="#27AE60", width=2.5)))
        fig1.add_trace(go.Scatter(x=spots_vis, y=[-(max(s - K_vis, 0) - prem_vis) for s in spots_vis],
            name="Short Call", line=dict(color="#E74C3C", width=2, dash="dot")))
        fig1.add_hline(y=0, line_color="black", line_dash="dash")
        fig1.add_vline(x=K_vis, line_dash="dot", annotation_text=f"Strike {K_vis}")
        fig1.update_layout(title=f"EUR/USD Call Option Payoff (K={K_vis}, Prem={prem_vis:.4f})",
                           xaxis_title="Spot at Expiry", yaxis_title="P&L per unit")
        st.plotly_chart(fig1, use_container_width=True)

        prem_put = 0.0170
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=spots_vis, y=[max(K_vis - s, 0) - prem_put for s in spots_vis],
            name="Long Put", line=dict(color="#8E44AD", width=2.5)))
        fig2.add_trace(go.Scatter(x=spots_vis, y=[-(max(K_vis - s, 0) - prem_put) for s in spots_vis],
            name="Short Put", line=dict(color="#F39C12", width=2, dash="dot")))
        fig2.add_hline(y=0, line_color="black", line_dash="dash")
        fig2.add_vline(x=K_vis, line_dash="dot", annotation_text=f"Strike {K_vis}")
        fig2.update_layout(title=f"EUR/USD Put Option Payoff (K={K_vis}, Prem={prem_put:.4f})",
                           xaxis_title="Spot at Expiry", yaxis_title="P&L per unit")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Option Premium vs Implied Volatility")
        vols_range = np.linspace(2, 25, 100)
        prices_atm = [gk_price(1.0850, 1.0850, 0.0525, 0.0375, 0.25, v/100, "call")[0] for v in vols_range]
        prices_otm = [gk_price(1.0850, 1.1000, 0.0525, 0.0375, 0.25, v/100, "call")[0] for v in vols_range]
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=vols_range, y=prices_atm, name="ATM Call (K=1.0850)",
            line=dict(color="#2E86C1", width=2.5)))
        fig3.add_trace(go.Scatter(x=vols_range, y=prices_otm, name="OTM Call (K=1.1000)",
            line=dict(color="#E74C3C", width=2.5)))
        fig3.update_layout(title="Option Price vs Implied Volatility (Vega Effect)",
                           xaxis_title="Implied Volatility %", yaxis_title="Option Price (pips × 10,000)")
        st.plotly_chart(fig3, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — FX Options Foundations")

        st.markdown("**Q1. In the Garman-Kohlhagen model, the foreign interest rate is treated as:**")
        q1 = st.radio("", [
            "A discount rate for future cash flows",
            "A continuous dividend yield on the base currency",
            "An inflation proxy",
            "A penalty rate for early exercise"
        ], key="fx6q1")
        if st.button("Check Q1", key="fx6c1"):
            if "continuous dividend yield" in q1:
                st.success("✅ Correct! Holding foreign currency earns r_f — analogous to a dividend. GK adjusts Black-Scholes by treating r_f as a continuous dividend yield.")
            else:
                st.error("❌ Incorrect. GK treats r_f (foreign rate) as a continuous dividend yield because holding foreign currency earns that rate.")
        st.markdown("---")

        st.markdown("**Q2. An ATM EUR/USD call option has delta of approximately:**")
        q2 = st.radio("", ["0.00", "0.50", "1.00", "-0.50"], key="fx6q2")
        if st.button("Check Q2", key="fx6c2"):
            if q2 == "0.50":
                st.success("✅ Correct! ATM call delta ≈ 0.50. This means the option price rises ~0.50 pips for every 1-pip rise in spot.")
            else:
                st.error("❌ Incorrect. ATM call delta ≈ 0.50. Delta ranges from 0 (deep OTM) to 1 (deep ITM) for calls.")
        st.markdown("---")

        st.markdown("**Q3. Vega measures:**")
        q3 = st.radio("", [
            "Price change per 1 day passing",
            "Price change per 1% change in implied volatility",
            "Delta change per 1 unit spot move",
            "Price change per 1% change in interest rates"
        ], key="fx6q3")
        if st.button("Check Q3", key="fx6c3"):
            if "1% change in implied volatility" in q3:
                st.success("✅ Correct! Vega = sensitivity to implied volatility. Long options have positive vega — they gain value when vol rises.")
            else:
                st.error("❌ Incorrect. Vega = option price change per 1% change in implied volatility. Theta = time decay. Gamma = delta change.")
        st.markdown("---")

        st.markdown("**Q4. Put-Call Parity states: C - P = ?**")
        q4 = st.radio("", [
            "K x e^(-rd x T) - S x e^(-rf x T)",
            "S x e^(-rf x T) - K x e^(-rd x T)",
            "S - K (intrinsic value)",
            "Forward rate - Spot rate"
        ], key="fx6q4")
        if st.button("Check Q4", key="fx6c4"):
            if "S x e^(-rf x T) - K x e^(-rd x T)" in q4:
                st.success("✅ Correct! C - P = S x e^(-rf x T) - K x e^(-rd x T). This is the FX put-call parity relationship.")
            else:
                st.error("❌ Incorrect. Put-call parity: C - P = S x e^(-rf x T) - K x e^(-rd x T).")
        st.markdown("---")

        st.markdown("**Q5. A UK exporter wanting protection against GBP strengthening (USD weakening) should:**")
        q5 = st.radio("", [
            "Buy a USD call option",
            "Buy a USD put option (right to sell USD at strike)",
            "Sell a USD call option",
            "Buy a GBP put option"
        ], key="fx6q5")
        if st.button("Check Q5", key="fx6c5"):
            if "Buy a USD put option" in q5:
                st.success("✅ Correct! Exporter fears USD weakening (lower GBP/USD). Buy USD put = right to sell USD at strike. If USD falls below strike, exercise the put.")
            else:
                st.error("❌ Incorrect. The exporter has USD receipts and fears USD weakness. Buying a USD put gives the right to sell USD at the strike rate — the protection floor.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Garman-Kohlhagen Pricing Summary")
        gk_df = pd.DataFrame({
            "Component": ["d1", "d2", "Call Price", "Put Price", "Put-Call Parity"],
            "Formula": [
                "[ln(S/K) + (r_d - r_f + sigma^2/2) x T] / (sigma x sqrt(T))",
                "d1 - sigma x sqrt(T)",
                "S x e^(-rf x T) x N(d1) - K x e^(-rd x T) x N(d2)",
                "K x e^(-rd x T) x N(-d2) - S x e^(-rf x T) x N(-d1)",
                "C - P = S x e^(-rf x T) - K x e^(-rd x T)"
            ]
        })
        st.dataframe(gk_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Option Greeks Reference")
        greeks_df = pd.DataFrame({
            "Greek": ["Delta (Δ)", "Gamma (Γ)", "Vega (ν)", "Theta (Θ)", "Rho (ρ)"],
            "Measures": [
                "Price change per 1 unit spot move",
                "Delta change per 1 unit spot move",
                "Price change per 1% vol change",
                "Price change per 1 day passing",
                "Price change per 1% rate change"
            ],
            "Call Range": ["0 to +1", "Always positive", "Always positive", "Always negative", "Positive"],
            "Highest At": ["Deep ITM", "ATM", "ATM", "Near expiry, ATM", "Long dated, ITM"],
            "Long Option": ["+ exposure", "Benefits buyer", "Positive (vega long)", "Negative (decay)", "Small effect FX"]
        })
        st.dataframe(greeks_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Hedging Strategy Comparison")
        hedge_df = pd.DataFrame({
            "Strategy": ["Forward Hedge", "Long Put (Exporter)", "Long Call (Importer)", "Zero-Cost Collar"],
            "Premium": ["Zero", "Pay premium", "Pay premium", "Zero (net)"],
            "Downside Protection": ["Full (locked rate)", "Full below strike", "Full above strike", "Full below put strike"],
            "Upside Participation": ["None", "Full above strike", "Full below strike", "Limited (to call strike)"],
            "Best When": ["Certainty needed", "Want protection + upside", "Want protection + upside", "Cost-sensitive, accept cap"]
        })
        st.dataframe(hedge_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Confusing r_d and r_f in GK formula",
                "Forgetting time is in YEARS (not days) in GK",
                "Delta = probability of profit (incorrect)",
                "Ignoring theta cost of long option positions",
                "Using Black-Scholes (no r_f) for FX options"
            ],
            "Correct Approach": [
                "r_d = quote currency (domestic) rate; r_f = base currency (foreign) rate",
                "T = days/365 or days/360 (convention varies). 90 days = 0.2466Y",
                "Delta approximates ITM probability at expiry, not profit probability",
                "Long options decay daily — theta is the cost of holding optionality",
                "Always use GK for FX — both r_d and r_f must be included"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 6 Complete! You can price FX vanilla options using GK, interpret the Greeks, verify put-call parity, and design basic FX hedges.")
        st.info("💡 Next: Module 7 — FX Options Advanced Structures (barriers, digitals, vol surface, exotic products)")

if __name__ == "__main__":
    show()