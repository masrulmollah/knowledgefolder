import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from scipy.stats import norm

def gk(S, K, rd, rf, T, sig, otype="call"):
    if T <= 0 or sig <= 0: return 0.0, 0.0
    d1 = (np.log(S/K) + (rd - rf + 0.5*sig**2)*T) / (sig*np.sqrt(T))
    d2 = d1 - sig*np.sqrt(T)
    if otype == "call":
        p = S*np.exp(-rf*T)*norm.cdf(d1) - K*np.exp(-rd*T)*norm.cdf(d2)
        delta = np.exp(-rf*T)*norm.cdf(d1)
    else:
        p = K*np.exp(-rd*T)*norm.cdf(-d2) - S*np.exp(-rf*T)*norm.cdf(-d1)
        delta = -np.exp(-rf*T)*norm.cdf(-d1)
    return round(p, 6), round(delta, 4)

def show():
    st.title("🔮 Module 7: FX Options — Advanced Structures")
    st.markdown("*Master barrier options, digital options, Asian options, the volatility surface, and structured FX products*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Barrier Options")
        st.markdown("""
        **Barrier options** are path-dependent — they activate or extinguish if the spot rate
        reaches a pre-set barrier level during the option's life.

        | Type | How It Works | Premium vs Vanilla |
        |------|-------------|-------------------|
        | **Knock-In (KI)** | Option ACTIVATES if spot hits the barrier | Cheaper — may never activate |
        | **Knock-Out (KO)** | Option EXTINGUISHES if spot hits the barrier | Cheaper — protection can disappear |
        | **Up-and-In** | KI with barrier ABOVE current spot | Rare for hedging |
        | **Down-and-Out** | KO with barrier BELOW current spot | Common corporate hedge |
        | **Reverse KO** | KO where barrier is in-the-money | Most dangerous — protection disappears when needed |

        **Key Risk — Pin Risk:** Near expiry, if spot hovers near the barrier, gamma and delta
        become very large. Market makers struggle to hedge; bid-ask spreads widen dramatically.
        """)

        st.subheader("2. Digital (Binary) Options")
        st.markdown("""
        A **digital option** pays a fixed, predetermined cash amount if spot is above
        (call) or below (put) the strike at expiry. All-or-nothing payoff.

        ```
        Digital Call payoff: $1 if S_T > K, else $0
        Digital Put payoff:  $1 if S_T < K, else $0

        Pricing (GK approximation):
        Digital Call = e^(-r_d x T) x N(d2)
        Digital Put  = e^(-r_d x T) x N(-d2)
        ```

        The digital call price approximates the **risk-neutral probability** of the spot
        finishing above the strike at expiry. Used in structured products and as probability tools.
        """)

        st.subheader("3. Asian (Average Rate) Options")
        st.markdown("""
        The payoff depends on the **average spot rate** over the option's life, not the final spot.

        ```
        Asian Call payoff = max(S_avg - K, 0)
        Asian Put payoff  = max(K - S_avg, 0)

        Where S_avg = arithmetic or geometric average of spot rates over the period
        ```

        | Feature | Asian Option | Vanilla Option |
        |---------|-------------|----------------|
        | Payoff based on | Average spot | Final spot |
        | Premium | Lower (20-30% cheaper typical) | Higher |
        | Why cheaper | Averaging reduces effective volatility | Full volatility priced |
        | Best for | Corporates with recurring FX flows | One-off exposures |

        **Finance use:** A company that converts USD revenues monthly benefits from an Asian
        option — the average rate over the year is more relevant than a single-date spot rate.
        """)

        st.subheader("4. Volatility Smile and Skew")
        st.markdown("""
        Black-Scholes/GK assume **constant volatility** across all strikes. In reality,
        implied volatility varies by strike and forms a characteristic shape:

        | Shape | Description | Common In |
        |-------|-------------|----------|
        | **Smile** | IV higher for OTM calls AND puts | FX, interest rates |
        | **Skew (smirk)** | IV higher for OTM puts than OTM calls | Equity markets |
        | **Forward skew** | IV higher for OTM calls | Commodities |

        **Risk Reversal (RR):** Measures the skew — difference between OTM call and OTM put vol.
        ```
        RR = IV(25-delta call) - IV(25-delta put)
        Negative RR: downside feared more than upside (put IV > call IV)
        Positive RR: upside feared more than downside
        ```

        **Butterfly (BF):** Measures the "fatness" of tails vs ATM.
        ```
        BF = [IV(25D call) + IV(25D put)] / 2 - IV(ATM)
        Positive BF: fat tails — large moves priced richer vs ATM
        ```
        """)

        st.subheader("5. Volatility Surface")
        st.markdown("""
        The **volatility surface** is a 3D matrix of implied volatility across all strikes
        and tenors. It is the market's complete view of option pricing.

        **Standard FX vol surface quotes:**
        ```
        ATM vol    = implied vol for at-the-money forward option
        25D RR     = IV(25D call) - IV(25D put)  [skew]
        25D BF     = [IV(25D call) + IV(25D put)]/2 - ATM  [kurtosis]
        10D RR     = IV(10D call) - IV(10D put)  [tail skew]
        10D BF     = [IV(10D call) + IV(10D put)]/2 - ATM  [extreme tails]
        ```

        From just 5 market quotes (ATM, 25D RR, 25D BF, 10D RR, 10D BF) per tenor,
        traders can reconstruct the full volatility smile using interpolation models.
        """)

        st.subheader("6. Structured FX Products")
        st.markdown("""
        | Product | Structure | Risk |
        |---------|-----------|------|
        | **TARF** (Target Accrual Redemption Forward) | Series of enhanced forwards that knock out when cumulative gain hits target | Unlimited loss if market moves adversely |
        | **PRDC** (Power Reverse Dual Currency Bond) | Bond with coupons linked to JPY/USD movements | Complex interest rate + FX exposure |
        | **Participating Forward** | Forward + long OTM option: fixed rate on 50%, market rate on 50% | Premium embedded in the forward rate |
        | **Seagull** | Buy call, sell OTM call, sell OTM put — three legs | Protection with premium funding |

        ⚠️ **Warning:** Structured products can have complex, asymmetric risk profiles.
        The 2008 GFC saw many Asian corporates suffer large losses from mis-sold TARFs.
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Knock-Out Forward vs Vanilla Option")
        st.markdown("""
        **Scenario:** UK importer needs to buy USD 1M in 6 months. EUR/USD spot = 1.0850.

        | Structure | Strike | Barrier | Premium | Risk |
        |-----------|--------|---------|---------|------|
        | Vanilla Call | 1.0900 | None | 300 pips | Protection guaranteed |
        | Knock-Out Call | 1.0900 | 1.0600 (KO) | 180 pips | Cheaper; protection lost if EUR/USD falls to 1.0600 |
        | Knock-In Call | 1.0900 | 1.1200 (KI) | 120 pips | Cheapest; only activates if EUR/USD rises to 1.1200 |

        **Analysis:**
        ```
        Vanilla: Always protected above 1.0900. Pay 300 pips.
        KO:      Protected above 1.0900, UNLESS EUR/USD drops to 1.0600 first.
                 Saves 120 pips vs vanilla. Used when importer believes EUR won't drop to 1.0600.
        KI:      Only has protection IF EUR/USD rises to 1.1200 first.
                 If EUR/USD never touches 1.1200, the option never exists.
                 Used when importer believes EUR will rise to 1.1200 (option activates when needed most).
        ```
        """)

        st.subheader("Example 2: Digital Option Pricing")
        st.markdown("""
        **Price a digital call:** EUR/USD S=1.0850, K=1.0900, r_d=5.25%, r_f=3.75%, T=0.25Y, sigma=8%

        ```
        From Module 6: d2 = -0.0414

        Digital Call = e^(-r_d x T) x N(d2)
                     = e^(-0.0525 x 0.25) x N(-0.0414)
                     = e^(-0.013125) x 0.4835
                     = 0.9870 x 0.4835
                     = 0.4772

        Interpretation: For every $1 payout, the digital call costs $0.4772.
        Probability of EUR/USD finishing above 1.0900 in 90 days = ~47.7%

        For a $1M digital payout: Premium = $1,000,000 x 0.4772 = $477,200
        ```
        """)

        st.subheader("Example 3: Asian Option — Corporate Use Case")
        st.markdown("""
        **Scenario:** US exporter receives JPY 100M per month (JPY 1.2B per year).
        USD/JPY spot = 149.50. The company wants to hedge its annual average rate.

        ```
        Asian Call (right to sell JPY at average rate):
          Strike:  150.00 JPY/USD
          Tenor:   12 months
          Average: Geometric average of 12 monthly fixings
          Premium: ~65% of equivalent vanilla option premium

        If monthly rates are: 145, 148, 152, 149, 151, 147, 153, 150, 148, 152, 149, 151
          Average = 149.58 JPY/USD
          Intrinsic = max(149.58 - 150.00, 0) = 0 (option expires worthless)
          The company converts at the 149.58 average — below strike

        Compare to vanilla: If final spot = 145.00
          Vanilla profits significantly (149.58 final spot would have been different)
          Asian: paid less premium, appropriate for averaging business
        ```
        """)

        st.subheader("Example 4: Reading a Volatility Smile")
        vol_df = pd.DataFrame({
            "Strike (Delta)": ["10D Put", "25D Put", "ATM", "25D Call", "10D Call"],
            "Delta": ["-0.10", "-0.25", "0.50", "+0.25", "+0.10"],
            "Implied Vol %": ["9.50", "8.80", "8.00", "8.40", "9.20"],
            "vs ATM": ["+1.50%", "+0.80%", "0", "+0.40%", "+1.20%"]
        })
        st.dataframe(vol_df, use_container_width=True, hide_index=True)
        st.markdown("""
        **Observations from this vol surface slice:**
        ```
        25D Risk Reversal = IV(25D Call) - IV(25D Put) = 8.40% - 8.80% = -0.40%
        Negative RR: OTM puts more expensive → market fears downside more than upside

        25D Butterfly = [IV(25D Call) + IV(25D Put)]/2 - ATM
                      = [8.40% + 8.80%]/2 - 8.00%
                      = 8.60% - 8.00% = +0.60%
        Positive BF: Fat tails — extreme moves in either direction priced richly vs ATM
        ```
        """)

        st.subheader("Example 5: TARF Mechanics")
        st.markdown("""
        **Target Accrual Redemption Forward (TARF):**
        A common structured product for Asian corporate hedgers.

        ```
        Terms:
          Notional:     USD 1M per settlement
          Settlements:  12 monthly
          Forward Rate: 1.0950 (enhanced vs spot 1.0850)
          Target:       USD 600,000 cumulative gain
          Leverage:     2x on losses

        How it works:
          Each month, if EUR/USD < 1.0950 (favourable for USD buyer):
            Company buys USD 1M at 1.0950 (better than spot)
            Gain = (1.0950 - market rate) x 1M

          If EUR/USD > 1.0950 (unfavourable):
            Company MUST buy USD 2M at 1.0950 (2x leverage on losses!)
            Loss = (market rate - 1.0950) x 2M

          When cumulative gains reach USD 600,000:
            Contract terminates (target reached)

        Risk: If EUR/USD rises sharply (USD weakens), the 2x leverage causes
        losses that can far exceed the enhanced forward benefit.
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose a Calculator:", [
            "🚧 Barrier Option Analyser",
            "💻 Digital Option Pricer",
            "📊 Volatility Smile Builder",
            "🌊 Asian Option Approximator",
            "⚠️ TARF Scenario Analyser"
        ])

        st.markdown("---")

        if calc_choice == "🚧 Barrier Option Analyser":
            st.subheader("Barrier Option vs Vanilla Comparison")
            col1, col2 = st.columns(2)
            with col1:
                S_b = st.number_input("Spot Rate (S)", value=1.0850, format="%.4f", key="bar_s")
                K_b = st.number_input("Strike Rate (K)", value=1.0900, format="%.4f", key="bar_k")
                rd_b = st.number_input("Domestic Rate %", value=5.25, key="bar_rd")
                rf_b = st.number_input("Foreign Rate %", value=3.75, key="bar_rf")
            with col2:
                T_b = st.number_input("Days to Expiry", value=180, key="bar_t")
                sig_b = st.number_input("Implied Vol %", value=8.0, step=0.5, key="bar_sig")
                barrier = st.number_input("Barrier Level", value=1.0600, format="%.4f", key="bar_barrier")
                btype = st.selectbox("Barrier Type", ["Down-and-Out Call", "Up-and-In Call", "Down-and-In Put", "Up-and-Out Put"])
                notional_b = st.number_input("Notional (base)", value=1000000.0, step=100000.0, key="bar_n")

            if st.button("Analyse Barrier Option", type="primary"):
                vanilla_price, vanilla_delta = gk(S_b, K_b, rd_b/100, rf_b/100, T_b/365, sig_b/100, "call")
                ko_discount = 0.45 if "Out" in btype else 0.35
                barrier_price = vanilla_price * ko_discount
                saving_pips = (vanilla_price - barrier_price) * 10000
                saving_dollar = (vanilla_price - barrier_price) * notional_b

                st.markdown("---")
                st.markdown(f"""
                **Barrier Option Analysis:**
                ```
                Vanilla Call Price:    {vanilla_price:.4f} ({vanilla_price*10000:.1f} pips)
                Barrier ({btype}):     {barrier_price:.4f} ({barrier_price*10000:.1f} pips)
                Premium Saving:        {saving_pips:.1f} pips = {saving_dollar:,.0f} quote currency
                Discount vs Vanilla:   {ko_discount*100:.0f}% cheaper

                Barrier Level:         {barrier:.4f}
                Current Spot:          {S_b:.4f}
                Distance to Barrier:   {abs(S_b - barrier)*10000:.0f} pips ({abs(S_b-barrier)/S_b*100:.2f}% move)
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("Vanilla Price", f"{vanilla_price*10000:.1f} pips")
                c2.metric("Barrier Price", f"{barrier_price*10000:.1f} pips")
                c3.metric("Premium Saving", f"{saving_dollar:,.0f}")

                if abs(S_b - barrier) / S_b < 0.03:
                    st.warning("⚠️ Barrier is CLOSE to spot (< 3% away). High risk of barrier being hit — consider wider barrier or vanilla option.")
                elif abs(S_b - barrier) / S_b < 0.05:
                    st.info("ℹ️ Moderate distance to barrier. Monitor closely — if spot approaches barrier, the hedge may extinguish.")
                else:
                    st.success(f"✅ Barrier is {abs(S_b-barrier)/S_b*100:.1f}% away from spot. Reasonable distance for a barrier hedge.")

        elif calc_choice == "💻 Digital Option Pricer":
            st.subheader("Digital (Binary) Option Pricer")
            col1, col2 = st.columns(2)
            with col1:
                S_d = st.number_input("Spot Rate (S)", value=1.0850, format="%.4f", key="dig_s")
                K_d = st.number_input("Strike Rate (K)", value=1.0900, format="%.4f", key="dig_k")
                rd_d = st.number_input("Domestic Rate %", value=5.25, key="dig_rd")
                rf_d = st.number_input("Foreign Rate %", value=3.75, key="dig_rf")
            with col2:
                T_d = st.number_input("Days to Expiry", value=90, key="dig_t")
                sig_d = st.number_input("Implied Vol %", value=8.0, step=0.5, key="dig_sig")
                payout = st.number_input("Digital Payout Amount (USD)", value=1000000.0, step=100000.0)
                dtype = st.radio("Digital Type", ["Call (pays if S > K at expiry)", "Put (pays if S < K at expiry)"])

            if st.button("Price Digital Option", type="primary"):
                T_y = T_d / 365
                d2_d = (np.log(S_d/K_d) + (rd_d/100 - rf_d/100 - 0.5*(sig_d/100)**2)*T_y) / (sig_d/100*np.sqrt(T_y))
                disc = np.exp(-rd_d/100 * T_y)
                if "Call" in dtype:
                    prob = norm.cdf(d2_d)
                    dig_price = disc * norm.cdf(d2_d)
                else:
                    prob = norm.cdf(-d2_d)
                    dig_price = disc * norm.cdf(-d2_d)

                total_premium = dig_price * payout

                st.markdown("---")
                st.markdown(f"""
                **Digital Option Pricing:**
                ```
                d2 = {d2_d:.4f}
                N(d2) = {norm.cdf(d2_d):.4f} | N(-d2) = {norm.cdf(-d2_d):.4f}
                Discount factor = e^(-{rd_d:.2f}% x {T_d}d) = {disc:.4f}

                Digital Price = {disc:.4f} x {prob:.4f} = {dig_price:.4f}
                Implied ITM probability = {prob*100:.2f}%
                Total premium for ${payout:,.0f} payout = ${total_premium:,.2f}
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("Digital Price", f"{dig_price:.4f}")
                c2.metric("ITM Probability", f"{prob*100:.2f}%")
                c3.metric("Total Premium", f"${total_premium:,.0f}")
                st.info(f"This {dtype.split('(')[0].strip()} option has a {prob*100:.1f}% probability of paying out ${payout:,.0f} at expiry.")

        elif calc_choice == "📊 Volatility Smile Builder":
            st.subheader("FX Volatility Surface — Smile Builder")
            col1, col2, col3 = st.columns(3)
            with col1:
                atm_vol = st.number_input("ATM Vol %", value=8.0, step=0.1)
                rr_25 = st.number_input("25D Risk Reversal (bps)", value=-40.0, step=5.0)
            with col2:
                bf_25 = st.number_input("25D Butterfly (bps)", value=60.0, step=5.0)
                rr_10 = st.number_input("10D Risk Reversal (bps)", value=-120.0, step=5.0)
            with col3:
                bf_10 = st.number_input("10D Butterfly (bps)", value=200.0, step=10.0)
                spot_vs = st.number_input("Spot Rate", value=1.0850, format="%.4f", key="vs_s")

            if st.button("Build Volatility Smile", type="primary"):
                call_25_vol = atm_vol + rr_25/100/2 + bf_25/100
                put_25_vol  = atm_vol - rr_25/100/2 + bf_25/100
                call_10_vol = atm_vol + rr_10/100/2 + bf_10/100
                put_10_vol  = atm_vol - rr_10/100/2 + bf_10/100

                smile_df = pd.DataFrame({
                    "Strike (Delta)": ["10D Put", "25D Put", "ATM", "25D Call", "10D Call"],
                    "Delta": ["-0.10", "-0.25", "~0.50", "+0.25", "+0.10"],
                    "Implied Vol %": [f"{put_10_vol:.2f}", f"{put_25_vol:.2f}", f"{atm_vol:.2f}",
                                       f"{call_25_vol:.2f}", f"{call_10_vol:.2f}"],
                    "vs ATM (bps)": [f"{(put_10_vol-atm_vol)*100:+.0f}", f"{(put_25_vol-atm_vol)*100:+.0f}",
                                     "0", f"{(call_25_vol-atm_vol)*100:+.0f}", f"{(call_10_vol-atm_vol)*100:+.0f}"]
                })
                st.dataframe(smile_df, use_container_width=True, hide_index=True)

                deltas_v = [-0.10, -0.25, 0.50, 0.75, 0.90]
                vols_v   = [put_10_vol, put_25_vol, atm_vol, call_25_vol, call_10_vol]
                labels_v = ["10D Put", "25D Put", "ATM", "25D Call", "10D Call"]
                fig = go.Figure(go.Scatter(x=deltas_v, y=vols_v, mode="lines+markers+text",
                    line=dict(color="#2E86C1", width=2.5), marker=dict(size=10),
                    text=labels_v, textposition="top center"))
                fig.add_hline(y=atm_vol, line_dash="dash", annotation_text=f"ATM {atm_vol}%")
                fig.update_layout(title="FX Volatility Smile", xaxis_title="Option Delta",
                                  yaxis_title="Implied Volatility %")
                st.plotly_chart(fig, use_container_width=True)

                c1, c2 = st.columns(2)
                c1.metric("25D Risk Reversal", f"{rr_25:+.0f} bps", "Negative = downside fear")
                c2.metric("25D Butterfly", f"{bf_25:+.0f} bps", "Fat tails priced in" if bf_25 > 0 else "Thin tails")

        elif calc_choice == "🌊 Asian Option Approximator":
            st.subheader("Asian Option Premium Approximator")
            col1, col2 = st.columns(2)
            with col1:
                S_a = st.number_input("Spot Rate (S)", value=149.50, format="%.2f", key="as_s")
                K_a = st.number_input("Strike Rate (K)", value=150.00, format="%.2f", key="as_k")
                rd_a = st.number_input("Domestic Rate %", value=5.25, key="as_rd")
                rf_a = st.number_input("Foreign Rate %", value=0.10, key="as_rf")
            with col2:
                T_a = st.number_input("Tenor (days)", value=365, key="as_t")
                sig_a = st.number_input("Implied Vol %", value=10.0, step=0.5, key="as_sig")
                fixings_a = st.number_input("Number of Fixings", value=12, min_value=1)
                otype_a = st.radio("Option Type", ["Asian Call", "Asian Put"], key="as_type")

            if st.button("Price Asian Option", type="primary"):
                from scipy.stats import norm as sn
                sigma_asian = sig_a / 100 * np.sqrt((2 * fixings_a + 1) / (6 * (fixings_a + 1)))
                T_y = T_a / 365
                vanilla_p, _ = gk(S_a, K_a, rd_a/100, rf_a/100, T_y, sig_a/100, otype_a.split()[1].lower())
                asian_p, _ = gk(S_a, K_a, rd_a/100, rf_a/100, T_y, sigma_asian, otype_a.split()[1].lower())
                discount_pct = (1 - asian_p / vanilla_p) * 100 if vanilla_p > 0 else 0

                st.markdown("---")
                st.markdown(f"""
                **Asian Option Approximation:**
                ```
                Effective sigma (Asian) = sigma x sqrt((2n+1)/(6(n+1)))
                                        = {sig_a:.2f}% x sqrt((2x{fixings_a}+1)/(6x({fixings_a}+1)))
                                        = {sigma_asian*100:.3f}%

                Vanilla Option Price:  {vanilla_p:.4f} ({vanilla_p*10000:.1f} pips)
                Asian Option Price:    {asian_p:.4f} ({asian_p*10000:.1f} pips)
                Premium Discount:      {discount_pct:.1f}% cheaper than vanilla
                ```
                """)
                c1, c2, c3 = st.columns(3)
                c1.metric("Vanilla Price", f"{vanilla_p*10000:.1f} pips")
                c2.metric("Asian Price", f"{asian_p*10000:.1f} pips")
                c3.metric("Discount", f"{discount_pct:.1f}%")
                st.info(f"The Asian option is {discount_pct:.1f}% cheaper because averaging {fixings_a} fixings reduces the effective volatility from {sig_a:.1f}% to {sigma_asian*100:.2f}%.")

        elif calc_choice == "⚠️ TARF Scenario Analyser":
            st.subheader("TARF (Target Accrual Redemption Forward) Scenario Analyser")
            st.warning("⚠️ TARFs are complex products with potentially unlimited downside. This is for educational analysis only.")
            col1, col2 = st.columns(2)
            with col1:
                tarf_fwd = st.number_input("Enhanced Forward Rate", value=1.0950, format="%.4f")
                spot_tarf = st.number_input("Current Spot Rate", value=1.0850, format="%.4f", key="tarf_s")
                monthly_notional = st.number_input("Monthly Notional (base)", value=1000000.0, step=100000.0)
            with col2:
                target = st.number_input("Cumulative Gain Target", value=600000.0, step=50000.0)
                leverage = st.number_input("Loss Leverage (x)", value=2.0, step=0.5, min_value=1.0)
                months = st.number_input("Maximum Months", value=12, min_value=1)

            rate_scenario = st.slider("Set average monthly spot rate (for scenario)", 1.0000, 1.2000, 1.0850, 0.0050)

            if st.button("Run TARF Scenario", type="primary"):
                cumulative_gain = 0.0
                results = []
                for m in range(1, int(months)+1):
                    month_rate = rate_scenario + np.random.normal(0, 0.005)
                    if month_rate < tarf_fwd:
                        gain = (tarf_fwd - month_rate) * monthly_notional
                        action = f"Favourable: buy at {tarf_fwd:.4f} vs market {month_rate:.4f}"
                    else:
                        gain = (tarf_fwd - month_rate) * monthly_notional * leverage
                        action = f"Adverse: buy {leverage:.0f}x at {tarf_fwd:.4f} vs market {month_rate:.4f}"
                    cumulative_gain += gain
                    results.append({"Month": m, "Market Rate": f"{month_rate:.4f}",
                                    "Monthly P&L": f"{gain:+,.0f}", "Cumulative P&L": f"{cumulative_gain:+,.0f}",
                                    "Status": "KNOCKED OUT" if cumulative_gain >= target else "Active", "Action": action})
                    if cumulative_gain >= target:
                        break

                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)
                if cumulative_gain >= target:
                    st.success(f"✅ TARF target reached at month {len(results)}. Total gain: {cumulative_gain:,.0f}")
                else:
                    st.error(f"❌ TARF did not reach target after {months} months. Final P&L: {cumulative_gain:+,.0f}")

    with tab4:
        st.header("Visualizations")

        st.subheader("Barrier Option Payoff vs Vanilla")
        K_v = 1.0900; prem_v = 0.0200; prem_ko = 0.0120; barrier_v = 1.0600
        spots_v = np.linspace(1.04, 1.15, 200)
        vanilla_poff = [max(s - K_v, 0) - prem_v for s in spots_v]
        ko_poff = [max(s - K_v, 0) - prem_ko if s > barrier_v else -prem_ko for s in spots_v]
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=spots_v, y=vanilla_poff, name="Vanilla Call", line=dict(color="#27AE60", width=2.5)))
        fig1.add_trace(go.Scatter(x=spots_v, y=ko_poff, name="KO Call (barrier=1.0600)", line=dict(color="#E74C3C", width=2, dash="dot")))
        fig1.add_hline(y=0, line_color="black", line_dash="dash")
        fig1.add_vline(x=barrier_v, line_color="#E74C3C", line_dash="dash", annotation_text="Barrier 1.0600")
        fig1.update_layout(title="Vanilla Call vs Knock-Out Call Payoff at Expiry",
                           xaxis_title="Spot at Expiry", yaxis_title="P&L per unit")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Volatility Smile — EUR/USD Illustrative")
        deltas_smile = [-0.10, -0.25, 0.50, 0.75, 0.90]
        vols_smile = [9.5, 8.8, 8.0, 8.4, 9.2]
        labels_smile = ["10D Put", "25D Put", "ATM", "25D Call", "10D Call"]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=deltas_smile, y=vols_smile, mode="lines+markers+text",
            line=dict(color="#8E44AD", width=2.5), marker=dict(size=10, color="#8E44AD"),
            text=labels_smile, textposition="top center", name="Vol Smile"))
        fig2.add_hline(y=8.0, line_dash="dash", annotation_text="ATM Vol 8.0%")
        fig2.update_layout(title="EUR/USD Volatility Smile by Delta",
                           xaxis_title="Option Delta", yaxis_title="Implied Volatility %")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Digital vs Vanilla Option Payoff Comparison")
        K_dig = 1.0900; prem_dig = 0.0159; dig_payout = 0.05
        dig_poff = [dig_payout - 0.0478 if s > K_dig else -0.0478 for s in spots_v]
        van_poff = [max(s - K_dig, 0) - prem_dig for s in spots_v]
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=spots_v, y=van_poff, name="Vanilla Call", line=dict(color="#27AE60", width=2.5)))
        fig3.add_trace(go.Scatter(x=spots_v, y=dig_poff, name="Digital Call ($0.05 payout)", line=dict(color="#F39C12", width=2.5)))
        fig3.add_hline(y=0, line_color="black", line_dash="dash")
        fig3.add_vline(x=K_dig, line_dash="dot", annotation_text=f"Strike {K_dig}")
        fig3.update_layout(title="Vanilla vs Digital Call Option Payoff Comparison",
                           xaxis_title="Spot at Expiry", yaxis_title="P&L per unit")
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.subheader("Test Your Understanding — Advanced FX Options")

        st.markdown("**Q1. A knock-out option compared to a vanilla option is:**")
        q1 = st.radio("", [
            "More expensive because of the barrier feature",
            "Cheaper — but protection disappears if the spot rate hits the barrier",
            "Exactly the same price as the vanilla option",
            "Only available for USD/JPY"
        ], key="fx7q1")
        if st.button("Check Q1", key="fx7c1"):
            if "Cheaper" in q1 and "disappears" in q1:
                st.success("✅ Correct! KO options are cheaper because the seller bears less risk — but the buyer's protection extinguishes if the barrier is hit.")
            else:
                st.error("❌ Incorrect. KO options are CHEAPER than vanilla — the protection disappears if spot hits the barrier, reducing the seller's liability.")
        st.markdown("---")

        st.markdown("**Q2. An Asian option is cheaper than a vanilla option because:**")
        q2 = st.radio("", [
            "It can only be exercised on specific dates",
            "The average rate has lower effective volatility than the final spot rate alone",
            "It has no intrinsic value",
            "It is only available for large notional amounts"
        ], key="fx7q2")
        if st.button("Check Q2", key="fx7c2"):
            if "lower effective volatility" in q2:
                st.success("✅ Correct! Averaging multiple fixings reduces the effective volatility of the payoff — lower vol = lower option price. Ideal for recurring cash flows.")
            else:
                st.error("❌ Incorrect. Asian options are cheaper because averaging reduces the effective volatility. Lower sigma → lower option premium.")
        st.markdown("---")

        st.markdown("**Q3. A negative 25-delta Risk Reversal (EUR/USD) means:**")
        q3 = st.radio("", [
            "EUR call IV is higher than EUR put IV",
            "EUR put IV is higher than EUR call IV — market fears EUR downside more",
            "The vol surface is flat with no skew",
            "ATM options are overpriced"
        ], key="fx7q3")
        if st.button("Check Q3", key="fx7c3"):
            if "EUR put IV is higher" in q3:
                st.success("✅ Correct! Negative RR = puts cost more than calls in vol terms → market is pricing in more downside risk for EUR (or USD upside risk).")
            else:
                st.error("❌ Incorrect. RR = IV(25D call) - IV(25D put). Negative RR means puts are more expensive → downside fear dominates.")
        st.markdown("---")

        st.markdown("**Q4. The 25-delta butterfly measures:**")
        q4 = st.radio("", [
            "The skew between calls and puts",
            "The kurtosis — how much fat tails are priced vs ATM (wings richness)",
            "The direction of the next spot move",
            "The time decay of at-the-money options"
        ], key="fx7q4")
        if st.button("Check Q4", key="fx7c4"):
            if "kurtosis" in q4 or "fat tails" in q4:
                st.success("✅ Correct! BF = [IV(25D C) + IV(25D P)]/2 - ATM. Positive BF means both wings are expensive vs ATM — fat tails priced in.")
            else:
                st.error("❌ Incorrect. Butterfly = [IV(25D call) + IV(25D put)]/2 - ATM. It measures the richness of tails vs ATM (kurtosis).")
        st.markdown("---")

        st.markdown("**Q5. The main risk of a TARF (Target Accrual Redemption Forward) is:**")
        q5 = st.radio("", [
            "The contract cannot be cancelled before maturity",
            "Losses are leveraged when spot moves adversely — potential for very large losses",
            "The target profit is too low",
            "It requires a large upfront premium"
        ], key="fx7q5")
        if st.button("Check Q5", key="fx7c5"):
            if "leveraged" in q5 or "large losses" in q5:
                st.success("✅ Correct! TARFs typically apply 2x or more leverage on adverse moves. When spot moves against the embedded forwards, losses are multiplied.")
            else:
                st.error("❌ Incorrect. TARFs embed leverage on the loss side — when spot moves adversely, the client must transact at 2x (or more) notional at the off-market rate.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Exotic Options Comparison")
        exotic_df = pd.DataFrame({
            "Product": ["Knock-Out (KO)", "Knock-In (KI)", "Digital Call", "Asian Call", "Vanilla Call"],
            "Payoff": [
                "Vanilla payoff IF barrier not hit",
                "Vanilla payoff ONLY IF barrier was hit",
                "Fixed amount if S_T > K",
                "max(S_avg - K, 0)",
                "max(S_T - K, 0)"
            ],
            "vs Vanilla Premium": ["30-50% cheaper", "20-40% cheaper", "Varies (fixed payout)", "20-35% cheaper", "Benchmark"],
            "Main Risk": ["Protection lost at barrier", "May never activate", "All-or-nothing", "Can't outperform avg", "Premium cost only"],
            "Best Used When": ["Confident barrier won't be hit", "Expect barrier to be reached", "Probability bet/structured product", "Recurring FX cash flows", "Certainty of protection needed"]
        })
        st.dataframe(exotic_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": [
                "Digital Call Price",
                "Digital Put Price",
                "25D Risk Reversal",
                "25D Butterfly",
                "Asian Effective Sigma",
                "Asian Option Price"
            ],
            "Expression": [
                "e^(-rd x T) x N(d2)",
                "e^(-rd x T) x N(-d2)",
                "IV(25D Call) - IV(25D Put)",
                "[IV(25D Call) + IV(25D Put)] / 2 - IV(ATM)",
                "sigma x sqrt((2n+1) / (6(n+1)))",
                "Use GK with sigma_asian as volatility"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Volatility Surface Interpretation")
        vs_df = pd.DataFrame({
            "Market Quote": ["ATM Vol", "25D RR > 0", "25D RR < 0", "25D BF > 0", "25D BF < 0"],
            "Meaning": [
                "Base implied vol for at-the-money option",
                "OTM calls pricier → market fears upside (e.g. commodity CCY)",
                "OTM puts pricier → market fears downside (most FX pairs)",
                "Fat tails — large moves in either direction priced richly",
                "Thin tails — rare; market pricing tight range"
            ]
        })
        st.dataframe(vs_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Buying KO options without monitoring the barrier",
                "Mispricing Asian options with vanilla GK formula",
                "Treating digital option price as the true probability",
                "Selling TARFs without stress-testing adverse scenarios",
                "Ignoring transaction costs in vol surface construction"
            ],
            "Correct Approach": [
                "Set alerts if spot approaches within 2-3% of barrier; have vanilla backup plan",
                "Use Asian-adjusted sigma = sigma x sqrt((2n+1)/(6(n+1))) in GK",
                "Digital price = risk-neutral probability, not real-world probability",
                "Always run 2-3x adverse stress scenarios before recommending TARFs",
                "Vol surface must be calibrated to observed market prices including bid-ask"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 7 Complete! You can price barrier, digital and Asian options, interpret the volatility surface, and understand structured FX product risks.")
        st.info("💡 Next: Module 8 — FX Risk Management (VaR, hedge ratios, IFRS 9 hedge accounting)")

if __name__ == "__main__":
    show()