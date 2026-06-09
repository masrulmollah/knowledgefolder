import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def _sec(title, icon=""):
    st.markdown(f"### {icon} {title}")
    st.markdown("---")

def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans: st.success("✅ Correct!")
        else: st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def show():
    st.title("💰 Module 6: Commercial, Customer & Value Analytics")
    st.caption("Understand where value is created and lost — customers, pricing, capital, and investment decisions")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 CLV & CAC", "📊 DCF Calculator", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Customer & Channel Profitability", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Customer Lifetime Value (CLV):**
```
CLV = (Average Annual Revenue × Gross Margin %) / Churn Rate
```
Measures the total net value a customer delivers over their lifetime.

**Customer Acquisition Cost (CAC):**
```
CAC = Total Sales & Marketing Spend / New Customers Acquired
```
**CAC Payback Period:**
```
CAC Payback = CAC / (Annual Revenue per Customer × GM%)
```
Industry benchmarks:
- SaaS / subscription: CAC payback < 12 months = excellent
- B2B enterprise: < 24 months acceptable
- LTV:CAC ratio > 3× considered healthy

**Cost-to-Serve (Hidden Loss-Makers):**
Standard margin reporting shows gross profit per customer.
Cost-to-Serve adds: logistics, customised packaging, returns,
credit terms cost, account management time.

Result: A customer with 30% gross margin and high cost-to-serve
may be a NET NEGATIVE contributor once fully loaded.
            """)
        with c2:
            st.markdown("""
**Pricing & Revenue Analytics:**
| Technique | What It Measures |
|-----------|-----------------|
| Price Realization | Actual price achieved vs. list price |
| Pocket Margin | Revenue minus all discounts and cost-to-serve |
| Discount Waterfall | Step-by-step margin erosion from list to net |
| Price Elasticity | % volume change per 1% price change |
| Mix-Adjusted Pricing | Price trend after removing product mix changes |

**Price Elasticity:**
```
Elasticity = % Change in Volume / % Change in Price
```
- |e| < 1: Inelastic (necessities, premium goods)
- |e| > 1: Elastic (commodities, substitutable goods)

If price elasticity = −2.0, a 5% price increase will reduce 
volume by 10% — potentially reducing total revenue.

**Discount Waterfall Example:**
```
List Price:          $100.00
Trade discount:       −$8.00 (8%)
Volume rebate:        −$5.00 (5%)
Payment discount:     −$2.00 (2%)
Logistics surcharge:  −$3.00 (3%)
Net Pocket Price:     $82.00 (18% erosion)
```
            """)

        _sec("Capital Allocation & Investment Analytics", "💼")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**NPV (Net Present Value):**
```
NPV = Σ [CF_t / (1 + r)^t] − Initial Investment
```
Decision rule: Accept if NPV > 0. Higher NPV = more value created.

**IRR (Internal Rate of Return):**
The discount rate at which NPV = 0. The effective annual return of the investment.
Accept if IRR > cost of capital (WACC).

**Payback Period:**
```
Payback = Initial Investment / Annual Cash Flow
```
Ignores time value of money. Use as a liquidity/risk check, not a primary criterion.

**EVA (Economic Value Added):**
```
EVA = NOPAT − (WACC × Invested Capital)
```
Measures whether a business earns more than its cost of capital.
Positive EVA = value creation. Negative EVA = value destruction.
            """)
        with c2:
            st.markdown("""
**WACC (Weighted Average Cost of Capital):**
```
WACC = (E/V × Ke) + (D/V × Kd × (1 − Tax Rate))

Where:
  E = Market value of equity
  D = Market value of debt
  V = E + D
  Ke = Cost of equity (CAPM: Rf + β × Market Risk Premium)
  Kd = Cost of debt (interest rate)
```
WACC is the hurdle rate — minimum acceptable return for any investment.

**Working Capital Optimization:**
```
Cash Released = Reduction in DSO × Daily Revenue
              + Reduction in DIO × Daily COGS
              − Reduction in DPO × Daily COGS
```
Even a 5-day improvement in DSO can release millions in cash
for a business with $500M+ in receivables.
            """)

    # ── CLV & CAC CALCULATOR ──────────────────────────────────────────────────
    with tab2:
        _sec("CLV, CAC & Customer Segment Profitability", "🧮")
        st.markdown("**Segment Input Parameters**")
        segments = ["Enterprise", "Mid-Market", "SMB", "E-commerce"]
        defaults = {
            "Annual Revenue ($K)":    [250, 80, 20, 8],
            "Gross Margin %":         [55, 48, 42, 35],
            "Churn Rate %":           [8, 15, 28, 45],
            "CAC ($K)":               [45, 18, 5, 1.5],
            "Cost-to-Serve ($K)":     [25, 10, 4, 1],
        }

        input_seg = {}
        for metric, defs in defaults.items():
            st.markdown(f"**{metric}**")
            cols_s = st.columns(4)
            row = []
            for i, (seg, d) in enumerate(zip(segments, defs)):
                with cols_s[i]:
                    v = st.number_input(seg, value=float(d), key=f"seg_{metric}_{i}",
                                        label_visibility="visible")
                    row.append(v)
            input_seg[metric] = row

        results = []
        for i, seg in enumerate(segments):
            rev    = input_seg["Annual Revenue ($K)"][i]
            gm     = input_seg["Gross Margin %"][i] / 100
            churn  = input_seg["Churn Rate %"][i] / 100
            cac    = input_seg["CAC ($K)"][i]
            cts    = input_seg["Cost-to-Serve ($K)"][i]
            clv    = (rev * gm) / churn
            ltv_cac = clv / cac if cac > 0 else float("inf")
            payback = cac / (rev * gm) if rev * gm > 0 else float("inf")
            net_clv = clv - cac - (cts / churn)
            results.append({
                "Segment": seg,
                "CLV ($K)": round(clv, 1),
                "CAC ($K)": round(cac, 1),
                "LTV:CAC": f"{ltv_cac:.1f}×",
                "CAC Payback (yrs)": round(payback, 1),
                "Cost-to-Serve ($K/yr)": cts,
                "Net CLV ($K)": round(net_clv, 1),
                "Verdict": "⭐ Highly Profitable" if ltv_cac >= 4 and net_clv > 50
                           else "✅ Profitable" if ltv_cac >= 2.5 and net_clv > 0
                           else "⚠️ Marginal" if net_clv > 0
                           else "🔴 Loss-Making",
            })

        df_seg = pd.DataFrame(results)
        st.markdown("**Customer Segment Profitability Summary:**")
        st.dataframe(df_seg, use_container_width=True, hide_index=True)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=segments, y=[r["CLV ($K)"] for r in results],
                             name="CLV ($K)", marker_color="#185FA5"))
        fig.add_trace(go.Bar(x=segments, y=[r["CAC ($K)"] for r in results],
                             name="CAC ($K)", marker_color="#E24B4A"))
        fig.add_trace(go.Bar(x=segments, y=[r["Net CLV ($K)"] for r in results],
                             name="Net CLV ($K)", marker_color="#1D9E75"))
        fig.update_layout(title="CLV vs. CAC vs. Net CLV by Segment ($K)",
                          barmode="group", template="plotly_white", height=380,
                          yaxis_title="$K", legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)

    # ── DCF CALCULATOR ────────────────────────────────────────────────────────
    with tab3:
        _sec("Investment Appraisal — NPV / IRR / Payback", "📊")
        c1, c2, c3 = st.columns(3)
        with c1:
            initial_inv = st.number_input("Initial Investment ($M)", value=50.0, step=1.0, key="dcf_inv")
            wacc        = st.number_input("Discount Rate / WACC (%)", value=10.0, step=0.5, key="dcf_wacc") / 100
            horizon     = st.slider("Project Horizon (years)", 3, 10, 5)
        with c2:
            growth_yr1  = st.number_input("Year 1 Cash Flow ($M)", value=8.0, step=0.5, key="dcf_cf1")
            cf_growth   = st.number_input("Annual CF Growth Rate (%)", value=8.0, step=0.5, key="dcf_cfg") / 100
        with c3:
            terminal_g  = st.number_input("Terminal Growth Rate (%)", value=2.5, step=0.5, key="dcf_tg") / 100
            use_terminal = st.checkbox("Include Terminal Value", value=True)

        cash_flows = [growth_yr1 * (1 + cf_growth) ** i for i in range(horizon)]
        terminal_val = (cash_flows[-1] * (1 + terminal_g)) / (wacc - terminal_g) if use_terminal and wacc > terminal_g else 0
        pv_cfs  = [cf / (1 + wacc)**(i+1) for i, cf in enumerate(cash_flows)]
        pv_tv   = terminal_val / (1 + wacc)**horizon
        npv     = sum(pv_cfs) + pv_tv - initial_inv

        # IRR via bisection
        def calc_npv(rate, cfs, inv):
            return sum(cf / (1+rate)**(i+1) for i, cf in enumerate(cfs)) + (
                (cfs[-1]*(1+terminal_g)/(rate-terminal_g)/(1+rate)**len(cfs)) if use_terminal and rate > terminal_g else 0
            ) - inv
        try:
            from scipy.optimize import brentq
            irr = brentq(lambda r: calc_npv(r, cash_flows, initial_inv), 0.001, 5.0)
        except Exception:
            irr = None

        cumcf = 0
        payback_yr = None
        for i, cf in enumerate(cash_flows):
            cumcf += cf
            if cumcf >= initial_inv and payback_yr is None:
                payback_yr = i + 1

        years_lbl = [f"Year {i+1}" for i in range(horizon)]
        cf_table = pd.DataFrame({
            "Year": years_lbl,
            "Cash Flow ($M)": [round(cf, 2) for cf in cash_flows],
            "PV Factor":      [round(1/(1+wacc)**(i+1), 4) for i in range(horizon)],
            "PV of CF ($M)":  [round(pv, 2) for pv in pv_cfs],
        })
        if use_terminal and wacc > terminal_g:
            tv_row = pd.DataFrame([{"Year": f"Terminal (at Yr {horizon})",
                                     "Cash Flow ($M)": round(terminal_val, 1),
                                     "PV Factor": round(1/(1+wacc)**horizon, 4),
                                     "PV of CF ($M)": round(pv_tv, 2)}])
            cf_table = pd.concat([cf_table, tv_row], ignore_index=True)
        st.dataframe(cf_table, use_container_width=True, hide_index=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("NPV", f"${npv:.2f}M", delta="Value Creating" if npv > 0 else "Value Destroying")
        c2.metric("IRR", f"{irr*100:.1f}%" if irr else "N/A",
                  delta=f"{'Above' if irr and irr > wacc else 'Below'} WACC ({wacc*100:.1f}%)")
        c3.metric("Payback Period", f"{payback_yr} years" if payback_yr else ">project life")
        c4.metric("PI (Profitability Index)", f"{(sum(pv_cfs)+pv_tv)/initial_inv:.2f}×",
                  delta="Accept if > 1.0×")

        if npv > 0 and irr and irr > wacc:
            st.success(f"✅ **INVEST:** NPV = ${npv:.2f}M (positive) and IRR ({irr*100:.1f}%) exceeds WACC ({wacc*100:.1f}%). This project creates shareholder value.")
        else:
            st.error(f"🔴 **DO NOT INVEST:** NPV = ${npv:.2f}M. Project destroys value at this discount rate. Re-examine cost structure or cash flow assumptions.")

        fig_dcf = go.Figure()
        fig_dcf.add_trace(go.Bar(x=years_lbl, y=[round(cf,2) for cf in cash_flows],
                                  name="Nominal CF ($M)", marker_color="#B5D4F4"))
        fig_dcf.add_trace(go.Bar(x=years_lbl, y=[round(pv,2) for pv in pv_cfs],
                                  name="PV of CF ($M)", marker_color="#185FA5"))
        fig_dcf.update_layout(title="Cash Flows — Nominal vs. Present Value",
                              barmode="group", template="plotly_white", height=360)
        st.plotly_chart(fig_dcf, use_container_width=True)

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Uncovering Hidden Loss-Making Customers — Distribution Company", "🧪")
        st.markdown("""
**Situation:** The Sales Director insists all top-20 customers are profitable because they all have positive gross margins.
The CFO has asked you to build a full cost-to-serve model to test this claim.
        """)

        np.random.seed(42)
        n_cust = 20
        customers = [f"Customer {i:02d}" for i in range(1, n_cust+1)]
        revenue   = np.random.pareto(1.3, n_cust) * 800 + 50
        gm_pct    = np.random.uniform(22, 45, n_cust)
        gross_profit = revenue * gm_pct / 100

        logistics     = revenue * np.random.uniform(0.04, 0.18, n_cust)
        custom_pack   = revenue * np.random.uniform(0.00, 0.08, n_cust)
        credit_cost   = revenue * np.random.uniform(0.01, 0.06, n_cust)
        account_mgmt  = np.random.uniform(5, 40, n_cust)

        total_cts   = logistics + custom_pack + credit_cost + account_mgmt
        net_margin  = gross_profit - total_cts
        net_margin_pct = net_margin / revenue * 100

        df_c = pd.DataFrame({
            "Customer":         customers,
            "Revenue ($K)":     revenue.round(1),
            "GM %":             gm_pct.round(1),
            "Gross Profit ($K)":gross_profit.round(1),
            "Logistics ($K)":   logistics.round(1),
            "Custom Pack ($K)": custom_pack.round(1),
            "Credit Cost ($K)": credit_cost.round(1),
            "Acct Mgmt ($K)":   account_mgmt.round(1),
            "Total CTS ($K)":   total_cts.round(1),
            "Net Margin ($K)":  net_margin.round(1),
            "Net Margin %":     net_margin_pct.round(1),
        })
        df_c = df_c.sort_values("Net Margin ($K)", ascending=False).reset_index(drop=True)
        df_c["Verdict"] = df_c["Net Margin %"].apply(
            lambda v: "✅ Profitable" if v > 5 else "⚠️ Marginal" if v > 0 else "🔴 Loss-Making")

        st.markdown("**Full Cost-to-Serve Profitability by Customer:**")
        st.dataframe(df_c, use_container_width=True, hide_index=True)

        loss_makers = df_c[df_c["Net Margin ($K)"] < 0]
        n_loss = len(loss_makers)
        total_loss = loss_makers["Net Margin ($K)"].sum()

        st.markdown("**Loss-Making Customers (positive GM but negative net margin):**")
        if n_loss > 0:
            st.dataframe(loss_makers[["Customer","Revenue ($K)","GM %","Total CTS ($K)","Net Margin ($K)","Verdict"]],
                         use_container_width=True, hide_index=True)
            st.error(f"⚠️ {n_loss} customers appear profitable on gross margin but are LOSS-MAKING after cost-to-serve. Combined value destruction: ${abs(total_loss):,.0f}K annually.")

        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_c["Customer"], y=df_c["Gross Profit ($K)"],
                             name="Gross Profit", marker_color="#B5D4F4"))
        fig.add_trace(go.Bar(x=df_c["Customer"], y=df_c["Net Margin ($K)"],
                             name="Net Margin (post CTS)",
                             marker_color=["#1D9E75" if v >= 0 else "#E24B4A" for v in df_c["Net Margin ($K)"]]))
        fig.add_hline(y=0, line_color="black", line_width=1)
        fig.update_layout(title="Customer Gross Profit vs. Net Margin after Cost-to-Serve",
                          barmode="group", template="plotly_white", height=400,
                          xaxis=dict(tickangle=45), yaxis_title="$K",
                          legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)

        st.success(f"""
**CFO Briefing — Cost-to-Serve Findings:**

- The Sales Director was correct that all 20 customers have **positive gross margins** (range: {gm_pct.min():.0f}%–{gm_pct.max():.0f}%).
- However, once logistics, custom packaging, credit costs, and account management are fully loaded, **{n_loss} customers are NET LOSS-MAKING**.
- Annual value destruction from these customers: **${abs(total_loss):,.0f}K**.
- **Recommended actions:**
  1. Renegotiate logistics terms or apply surcharges for high-complexity delivery requirements.
  2. Review custom packaging — standardise where possible.
  3. Tighten credit terms for loss-making accounts.
  4. Consider minimum order value thresholds to cover fixed account management costs.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 6 Quiz", "❓")
        _quiz("1. CLV = $90K and CAC = $20K. The LTV:CAC ratio is:",
              ["1.5×", "3.5×", "4.5×", "9.0×"], "4.5×", "fa_m6q1")
        st.divider()
        _quiz("2. A project has NPV = +$15M and IRR = 14% vs. WACC of 10%. You should:",
              ["Reject — IRR is too low",
               "Accept — NPV is positive and IRR exceeds WACC, project creates value",
               "Reject — payback period was not mentioned",
               "Accept only if payback < 2 years"],
              "Accept — NPV is positive and IRR exceeds WACC, project creates value", "fa_m6q2")
        st.divider()
        _quiz("3. A customer has 30% gross margin but is loss-making after cost-to-serve. This means:",
              ["The gross margin calculation is wrong",
               "Logistics, credit terms, or service complexity erase the gross profit",
               "The customer should be the company's top priority",
               "The company's fixed costs are too high"],
              "Logistics, credit terms, or service complexity erase the gross profit", "fa_m6q3")
        st.divider()
        _quiz("4. Price elasticity of −3.0 means:",
              ["A 1% price increase leads to a 3% volume decrease",
               "Revenue always falls with price increases",
               "Demand is perfectly inelastic",
               "A 1% price increase leads to a 0.3% volume decrease"],
              "A 1% price increase leads to a 3% volume decrease", "fa_m6q4")
        st.divider()
        _quiz("5. EVA (Economic Value Added) is positive when:",
              ["Revenue exceeds costs",
               "NOPAT exceeds the cost of all capital employed (WACC × Invested Capital)",
               "EBITDA margin exceeds 15%",
               "The company pays no tax"],
              "NOPAT exceeds the cost of all capital employed (WACC × Invested Capital)", "fa_m6q5")