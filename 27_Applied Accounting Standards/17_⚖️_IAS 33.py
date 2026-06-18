import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show():
    st.title("📊 IAS 33: Earnings Per Share")
    st.markdown("*Master basic and diluted EPS calculations for listed entities*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Scope and Objective")
        st.markdown("""
IAS 33 applies to entities whose **ordinary shares are publicly traded** (listed companies). It prescribes how to calculate and present **earnings per share (EPS)** to enable meaningful comparisons.

EPS is one of the most widely used performance metrics for equity investors.
        """)
        st.subheader("2. Basic EPS")
        st.markdown("""
```
Basic EPS = Earnings attributable to ordinary equity holders
            ─────────────────────────────────────────────────
            Weighted Average Number of Ordinary Shares (WANOS)
```

**Earnings (numerator):**
- Profit or loss attributable to ordinary shareholders
- Deduct preference dividends (cumulative: deduct whether declared or not; non-cumulative: only if declared)

**WANOS (denominator):**
- Weight shares by the fraction of the period they were outstanding
- Bonus issues / stock splits / share consolidations → adjust **retrospectively** as if they always existed
- Rights issues at below market price → contains a bonus element → adjust for the bonus element
        """)
        st.subheader("3. Diluted EPS")
        st.markdown("""
Diluted EPS shows the impact of **all potential ordinary shares** that could dilute EPS if exercised/converted.

**Potential ordinary shares include:**
- Stock options and warrants
- Convertible bonds
- Convertible preference shares
- Contingently issuable shares

**Treasury stock method (for options/warrants):**
- Assume options exercised → proceeds used to buy back shares at average market price
- Net dilutive shares = options outstanding − shares bought back with proceeds

**Diluted EPS formula:**
```
Diluted EPS = Adjusted Earnings
              ─────────────────────────────────────────────────────
              WANOS + Weighted Average Dilutive Potential Shares
```

**Anti-dilutive instruments** (those that INCREASE EPS if included) are **EXCLUDED** from diluted EPS.

Diluted EPS ≤ Basic EPS (always — unless there are anti-dilutive shares excluded).
        """)
        st.subheader("4. Adjustments for Share Changes")
        st.markdown("""
| Event | Adjustment |
|---|---|
| New shares issued for cash at fair value | Weight from date of issue |
| Bonus issue (stock dividend) | Retroactively adjust — as if always outstanding |
| Share split | Retroactively adjust |
| Share consolidation (reverse split) | Retroactively adjust |
| Rights issue at below-market price | Retroactively adjust bonus element; weight cash element from issue date |
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Basic EPS with Mid-Year Issue")
        st.markdown("""
- Opening shares: 10,000,000
- 1 April: Issued 2,000,000 new shares for cash at market price
- Earnings attributable to ordinary shareholders: $4,500,000

**WANOS:**
| Period | Shares | Fraction | Weighted |
|---|---|---|---|
| 1 Jan–31 Mar | 10,000,000 | 3/12 | 2,500,000 |
| 1 Apr–31 Dec | 12,000,000 | 9/12 | 9,000,000 |
| **WANOS** | | | **11,500,000** |

**Basic EPS = $4,500,000 / 11,500,000 = $0.391**
        """)
        st.subheader("Example 2: Diluted EPS — Share Options")
        st.markdown("""
- Basic EPS: $0.391; WANOS: 11,500,000
- Outstanding options: 1,000,000 @ $3.00 exercise price
- Average market price: $5.00

**Treasury stock method:**
- Proceeds = 1,000,000 × $3.00 = $3,000,000
- Shares repurchased at market = $3,000,000 / $5.00 = 600,000
- Net dilutive shares = 1,000,000 − 600,000 = **400,000**

**Diluted WANOS = 11,500,000 + 400,000 = 11,900,000**
**Diluted EPS = $4,500,000 / 11,900,000 = $0.378**
        """)
        st.subheader("Example 3: Bonus Issue — Retrospective Adjustment")
        st.markdown("""
- Shares at 1 Jan: 8,000,000
- 1 July: 1-for-4 bonus issue → 2,000,000 new shares
- Earnings: $3,200,000

**WANOS (bonus element treated as always outstanding):**
All 10,000,000 shares treated as outstanding for full year
- Pre-bonus period: 8,000,000 × adjustment factor (10/8) × 6/12 = 5,000,000
- Post-bonus: 10,000,000 × 6/12 = 5,000,000
- **WANOS = 10,000,000**

**Basic EPS = $3,200,000 / 10,000,000 = $0.32**

Prior period EPS is also restated using the 10/8 adjustment factor.
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Basic EPS Calculator with WANOS")
        earnings = st.number_input("Earnings attributable to ordinary shareholders ($)", value=4500000)
        pref_divs = st.number_input("Preference dividends to deduct ($)", value=0)
        st.markdown("**Share movements during the year:**")
        opening_shares = st.number_input("Opening shares (1 Jan)", value=10000000)
        issue_shares = st.number_input("Shares issued during year", value=2000000)
        issue_month = st.number_input("Month of issue (1=Jan, 4=Apr)", value=4, min_value=1, max_value=12)
        bonus = st.number_input("Bonus shares issued (0 if none)", value=0)

        if st.button("Calculate Basic EPS"):
            adj_earnings = earnings - pref_divs
            w1 = opening_shares * (issue_month - 1) / 12
            w2 = (opening_shares + issue_shares) * (13 - issue_month) / 12
            wanos = w1 + w2
            if bonus > 0:
                adj_factor = (opening_shares + issue_shares + bonus) / (opening_shares + issue_shares)
                wanos = wanos * adj_factor
            basic_eps = adj_earnings / wanos
            st.markdown(f"""
| Item | Value |
|---|---|
| Adjusted earnings | ${adj_earnings:,.0f} |
| WANOS | {wanos:,.0f} |
| **Basic EPS** | **${basic_eps:.4f}** |
""")

        st.markdown("---")
        st.subheader("🔧 Diluted EPS — Treasury Stock Method for Options")
        col1, col2 = st.columns(2)
        with col1:
            basic_eps_d = st.number_input("Basic EPS ($)", value=0.391)
            wanos_d = st.number_input("Basic WANOS", value=11500000)
            earn_d = st.number_input("Earnings ($)", value=4500000)
        with col2:
            options = st.number_input("Options outstanding", value=1000000)
            exercise_price = st.number_input("Exercise price ($)", value=3.0)
            avg_price = st.number_input("Average market price ($)", value=5.0)
        if st.button("Calculate Diluted EPS"):
            if exercise_price < avg_price:
                proceeds = options * exercise_price
                buyback = proceeds / avg_price
                net_dilutive = options - buyback
                diluted_wanos = wanos_d + net_dilutive
                diluted_eps = earn_d / diluted_wanos
                st.success(f"""
Net dilutive shares: {net_dilutive:,.0f}
Diluted WANOS: {diluted_wanos:,.0f}
**Diluted EPS: ${diluted_eps:.4f}** (vs Basic ${basic_eps_d:.4f})
""")
            else:
                st.info("Options are ANTI-DILUTIVE (exercise price ≥ market price) → EXCLUDED from diluted EPS. Diluted EPS = Basic EPS.")

    with tab4:
        st.header("Visualizations")
        years = ["2020","2021","2022","2023","2024"]
        basic = [0.28, 0.32, 0.35, 0.37, 0.39]
        diluted = [0.25, 0.29, 0.32, 0.35, 0.38]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=basic, name="Basic EPS", line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig.add_trace(go.Scatter(x=years, y=diluted, name="Diluted EPS", line=dict(color="#F59E0B", width=2, dash="dash"), mode="lines+markers"))
        fig.update_layout(title="EPS Trend — Basic vs Diluted", yaxis_title="EPS ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. Basic EPS denominator is:**")
        q1 = st.radio("", ["Total shares at year-end","Weighted average ordinary shares outstanding","Total authorized shares","Shares less treasury shares at year-end"], key="ias33q1")
        if st.button("Check", key="c33_1"):
            if q1 == "Weighted average ordinary shares outstanding":
                st.success("✅ Correct! The denominator for basic EPS is the WANOS — shares weighted by the fraction of the period they were outstanding.")
            else:
                st.error("❌ Basic EPS uses WEIGHTED AVERAGE ordinary shares — not year-end shares.")
        st.markdown("---")
        st.markdown("**2. A bonus issue that occurs during the year affects WANOS:**")
        q2 = st.radio("", ["From the date of issue only","Retroactively — as if the shares were always outstanding","Not at all","Only for the diluted EPS calculation"], key="ias33q2")
        if st.button("Check", key="c33_2"):
            if q2 == "Retroactively — as if the shares were always outstanding":
                st.success("✅ Correct! Bonus issues are treated as if they always existed — adjust WANOS retrospectively for all periods presented.")
            else:
                st.error("❌ Bonus issues → retrospective adjustment. Treat as if always outstanding. Prior period EPS is also restated.")
        st.markdown("---")
        st.markdown("**3. Anti-dilutive potential shares are:**")
        q3 = st.radio("", ["Included in diluted EPS","Excluded from diluted EPS","Included in basic EPS only","Disclosed but not included in any EPS"], key="ias33q3")
        if st.button("Check", key="c33_3"):
            if q3 == "Excluded from diluted EPS":
                st.success("✅ Correct! Anti-dilutive instruments (those that INCREASE EPS if included) are excluded from the diluted EPS calculation.")
            else:
                st.error("❌ Anti-dilutive instruments are EXCLUDED from diluted EPS. Only dilutive instruments are included.")
        st.markdown("---")
        st.markdown("**4. Cumulative preference dividends are deducted from earnings for basic EPS:**")
        q4 = st.radio("", ["Only if declared","Whether declared or not","Only in the year they are paid","Only if non-participating"], key="ias33q4")
        if st.button("Check", key="c33_4"):
            if q4 == "Whether declared or not":
                st.success("✅ Correct! Cumulative preference dividends are deducted whether declared or not (they accrue regardless). Non-cumulative preference dividends are deducted only if declared.")
            else:
                st.error("❌ Cumulative preference dividends → deduct whether declared or not. Non-cumulative → only if declared.")
        st.markdown("---")
        st.markdown("**5. Under the treasury stock method for options, net dilutive shares =**")
        q5 = st.radio("", ["Total options outstanding","Options × exercise price / market price","Options outstanding minus shares repurchased with proceeds","Options × market price / exercise price"], key="ias33q5")
        if st.button("Check", key="c33_5"):
            if q5 == "Options outstanding minus shares repurchased with proceeds":
                st.success("✅ Correct! Treasury stock method: net dilutive shares = options − (exercise price × options / avg market price) = options minus shares repurchased with proceeds.")
            else:
                st.error("❌ Treasury method: assume options exercised → use proceeds to buy back shares at market price. Net dilutive = options − buyback shares.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 33 Key Formulas

```
Basic EPS = (Earnings − Preference Dividends) / WANOS

Diluted EPS = Adjusted Earnings / (WANOS + Dilutive Potential Shares)

Treasury Stock Method (options):
Net Dilutive Shares = Options − (Options × Exercise Price / Avg Market Price)
```

**WANOS Adjustments:**
- Cash issue → weight from date of issue
- Bonus issue / split → retroactive (treat as always outstanding)
- Rights issue at below market → separate bonus element (retroactive) + cash element (from date)

**Diluted EPS Rules:**
- Include ALL dilutive potential shares
- Exclude anti-dilutive instruments
- Diluted EPS ≤ Basic EPS

**Numerator adjustments for diluted EPS:**
- Add back after-tax interest on convertible bonds
- Add back preferred dividends on convertible preference shares

**Disclosure required:**
- Basic and diluted EPS on face of P&L
- Amounts used as numerator and denominator (reconciliation)
        """)
        st.success("🎓 IAS 33 Complete!")
        st.info("💡 Next: IAS 36 — Impairment of Assets")

if __name__ == "__main__":
    show()