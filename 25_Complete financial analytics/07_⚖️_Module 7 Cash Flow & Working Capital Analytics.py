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
    st.title("🏦 Module 7: Cash Flow & Working Capital Analytics")
    st.caption("Track where cash is generated, consumed, and trapped — and how to free it")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Cash Flow Builder", "📊 Working Capital Simulator", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Cash Flow Statement Analysis", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Three Sections of the Cash Flow Statement:**

| Section | What It Covers | Healthy Signal |
|---------|---------------|----------------|
| Operating CF | Cash from core business | Positive & growing |
| Investing CF | Capex, acquisitions, disposals | Negative (growing business) |
| Financing CF | Debt, equity, dividends | Context-dependent |

**Free Cash Flow (FCF):**
```
FCF = Operating Cash Flow − Capital Expenditure
```
FCF is the purest measure of cash a business generates after maintaining
and growing its asset base. It is the basis for DCF valuation.

**Cash Conversion:**
```
Cash Conversion = FCF / EBITDA × 100%
```
- > 80% = excellent cash conversion
- 60–80% = acceptable
- < 60% = investigate working capital or capex intensity

**EBITDA vs. Cash — Why They Differ:**
- Working capital build (AR up, inventory up) consumes cash
- Capex is cash but not in EBITDA
- Non-cash charges (D&A, provisions) are in EBITDA but not cash
            """)
        with c2:
            st.markdown("""
**Cash Burn & Runway:**
```
Monthly Burn Rate = (Cash Start − Cash End) / Months
Runway (months)  = Current Cash / Monthly Burn Rate
```
Critical for early-stage companies, distressed businesses, or
any entity managing a restructuring.

**13-Week Cash Flow Forecast:**
The gold standard for near-term liquidity management.
- Weekly granularity for the next 13 weeks
- Direct method: actual cash receipts and payments
- Reviewed weekly by CFO/Treasury
- Triggers action when runway falls below threshold

**Operating vs. Structural Cash:**
| Type | Source | Sustainability |
|------|--------|---------------|
| Operating CF | Trading profit + WC improvement | Recurring |
| Asset disposal | One-off sale | Non-recurring |
| Debt drawdown | Borrowing | Temporary |
| Equity raise | New capital | One-off |

Always distinguish: is the company generating real trading cash,
or is it papering over weak operations with financing?
            """)

        _sec("Working Capital Analytics", "⚙️")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**The Working Capital Cycle:**
```
Cash → Raw Materials (Inventory) → Production → Finished Goods
     → Receivables (Sales on Credit) → Cash Collection → Cash
```
**Cash Conversion Cycle (CCC):**
```
CCC = DIO + DSO − DPO
```
- **DIO** (Days Inventory Outstanding) = Inventory / COGS × 365
- **DSO** (Days Sales Outstanding)     = Receivables / Revenue × 365
- **DPO** (Days Payable Outstanding)   = Payables / COGS × 365

Lower CCC = faster cash cycle = less working capital funding needed.
Negative CCC (Amazon, Zara) = customers pay before suppliers → structural advantage.

**Cash Released per Day of Improvement:**
```
1-day DSO improvement = Daily Revenue
1-day DIO improvement = Daily COGS
1-day DPO extension   = Daily COGS (cash preserved)
```
            """)
        with c2:
            st.markdown("""
**Receivables Aging Analysis (AR Buckets):**
| Bucket | Days Overdue | Risk Level | Action |
|--------|-------------|------------|--------|
| Current | 0–30 days | Low | Monitor |
| Overdue 1 | 31–60 days | Medium | Reminder |
| Overdue 2 | 61–90 days | High | Escalate |
| Overdue 3 | 91–120 days | Very High | Collections |
| Bad debt | > 120 days | Critical | Provision/Write-off |

**Inventory Aging:**
Fast-moving vs. slow-moving vs. obsolete.
Obsolete inventory ties up cash and often has hidden disposal costs.

**Working Capital Levers:**
- Reduce DSO: tighter credit terms, early payment discounts, invoice factoring
- Reduce DIO: lean inventory, demand-driven replenishment, SKU rationalisation
- Extend DPO: negotiate longer supplier terms, supply chain finance
- Net effect: fund operations with suppliers' money, not the bank's
            """)
        st.info("💡 A $500M revenue business improving DSO by just 5 days releases approximately **$6.8M in cash** immediately — with no impact on P&L.")

    # ── CASH FLOW BUILDER ─────────────────────────────────────────────────────
    with tab2:
        _sec("Indirect Method Cash Flow Builder", "🧮")
        st.markdown("Build a full cash flow statement from P&L and balance sheet movements:")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**P&L Inputs ($M)**")
            ebitda_cf   = st.number_input("EBITDA",          value=120.0, step=5.0, key="cf_ebitda")
            da_cf       = st.number_input("D&A",             value=28.0,  step=1.0, key="cf_da")
            interest_cf = st.number_input("Cash Interest",   value=12.0,  step=1.0, key="cf_int")
            tax_cf      = st.number_input("Cash Tax",        value=22.0,  step=1.0, key="cf_tax")
        with c2:
            st.markdown("**Working Capital Changes ($M)**")
            d_recv  = st.number_input("Δ Receivables (+build/-release)", value=8.0,  step=1.0, key="cf_recv",
                                      help="Positive = AR increased (uses cash)")
            d_inv   = st.number_input("Δ Inventory (+build/-release)",   value=5.0,  step=1.0, key="cf_inv",
                                      help="Positive = Inventory increased (uses cash)")
            d_pay   = st.number_input("Δ Payables (+increase/-decrease)",value=3.0,  step=1.0, key="cf_pay",
                                      help="Positive = Payables increased (generates cash)")
        with c3:
            st.markdown("**Investing & Financing ($M)**")
            capex_cf  = st.number_input("Capex (maintenance)",    value=18.0, step=1.0, key="cf_capex_m")
            capex_g   = st.number_input("Capex (growth)",         value=12.0, step=1.0, key="cf_capex_g")
            debt_net  = st.number_input("Net Debt Repayment",     value=10.0, step=1.0, key="cf_debt",
                                        help="Positive = repaid debt (uses cash)")
            dividends = st.number_input("Dividends Paid",         value=15.0, step=1.0, key="cf_div")

        ebit      = ebitda_cf - da_cf
        wc_change = -(d_recv + d_inv - d_pay)
        op_cf     = ebit + da_cf - interest_cf - tax_cf + wc_change
        inv_cf    = -(capex_cf + capex_g)
        fin_cf    = -(debt_net + dividends)
        net_cf    = op_cf + inv_cf + fin_cf
        fcf       = op_cf - capex_cf - capex_g
        conv_rate = fcf / ebitda_cf * 100 if ebitda_cf > 0 else 0

        cf_items = [
            ("EBITDA",                    ebitda_cf,           "Operating"),
            ("Less: D&A (add back)",      da_cf,               "Operating"),
            ("Less: Interest",            -interest_cf,        "Operating"),
            ("Less: Tax",                 -tax_cf,             "Operating"),
            ("Δ Working Capital",         wc_change,           "Operating"),
            ("Operating Cash Flow",       op_cf,               "SUBTOTAL"),
            ("Capex — Maintenance",       -capex_cf,           "Investing"),
            ("Capex — Growth",            -capex_g,            "Investing"),
            ("Investing Cash Flow",       inv_cf,              "SUBTOTAL"),
            ("Debt Repayment",            -debt_net,           "Financing"),
            ("Dividends",                 -dividends,          "Financing"),
            ("Financing Cash Flow",       fin_cf,              "SUBTOTAL"),
            ("NET CHANGE IN CASH",        net_cf,              "TOTAL"),
        ]
        cf_df = pd.DataFrame(cf_items, columns=["Line Item", "Amount ($M)", "Category"])
        st.dataframe(cf_df, use_container_width=True, hide_index=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Operating CF",        f"${op_cf:.1f}M",  delta="✅ Positive" if op_cf > 0 else "🔴 Negative")
        c2.metric("Free Cash Flow",      f"${fcf:.1f}M",    delta="✅ Positive" if fcf > 0 else "🔴 Negative")
        c3.metric("Net Cash Change",     f"${net_cf:.1f}M")
        c4.metric("Cash Conversion",     f"{conv_rate:.0f}%", delta="✅ Strong" if conv_rate > 75 else "⚠️ Weak")

        fig = go.Figure(go.Waterfall(
            orientation="v",
            measure=["relative","relative","relative","relative","relative","total",
                     "relative","relative","total",
                     "relative","relative","total","total"],
            x=[i[0] for i in cf_items],
            y=[i[1] for i in cf_items],
            text=[f"${i[1]:+.1f}M" for i in cf_items],
            textposition="outside",
            connector={"line": {"color": "#888"}},
            increasing={"marker": {"color": "#1D9E75"}},
            decreasing={"marker": {"color": "#E24B4A"}},
            totals={"marker":    {"color": "#185FA5"}}
        ))
        fig.update_layout(title="Cash Flow Waterfall — Indirect Method ($M)",
                          template="plotly_white", height=440,
                          xaxis=dict(tickangle=35), yaxis_title="$M")
        st.plotly_chart(fig, use_container_width=True)

    # ── WORKING CAPITAL SIMULATOR ─────────────────────────────────────────────
    with tab3:
        _sec("Working Capital Optimisation Simulator", "📊")
        st.markdown("Model the cash impact of improving DSO, DIO, and DPO:")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Current State**")
            rev_wc   = st.number_input("Annual Revenue ($M)",  value=500.0, step=10.0, key="wc_rev")
            cogs_wc  = st.number_input("Annual COGS ($M)",     value=300.0, step=10.0, key="wc_cogs")
            dso_curr = st.number_input("Current DSO (days)",   value=52.0,  step=1.0,  key="wc_dso")
            dio_curr = st.number_input("Current DIO (days)",   value=48.0,  step=1.0,  key="wc_dio")
            dpo_curr = st.number_input("Current DPO (days)",   value=38.0,  step=1.0,  key="wc_dpo")
        with c2:
            st.markdown("**Target State**")
            dso_tgt  = st.number_input("Target DSO (days)",    value=42.0,  step=1.0,  key="wc_dso_t")
            dio_tgt  = st.number_input("Target DIO (days)",    value=40.0,  step=1.0,  key="wc_dio_t")
            dpo_tgt  = st.number_input("Target DPO (days)",    value=45.0,  step=1.0,  key="wc_dpo_t")

        daily_rev  = rev_wc / 365
        daily_cogs = cogs_wc / 365

        ccc_curr = dso_curr + dio_curr - dpo_curr
        ccc_tgt  = dso_tgt  + dio_tgt  - dpo_tgt

        cash_dso = (dso_curr - dso_tgt) * daily_rev
        cash_dio = (dio_curr - dio_tgt) * daily_cogs
        cash_dpo = (dpo_tgt  - dpo_curr) * daily_cogs
        total_cash_release = cash_dso + cash_dio + cash_dpo

        wc_rows = pd.DataFrame({
            "Metric":        ["DSO", "DIO", "DPO", "CCC"],
            "Current (days)":[dso_curr, dio_curr, dpo_curr, ccc_curr],
            "Target (days)": [dso_tgt,  dio_tgt,  dpo_tgt,  ccc_tgt],
            "Change (days)": [dso_curr-dso_tgt, dio_curr-dio_tgt, dpo_tgt-dpo_curr, ccc_curr-ccc_tgt],
            "Cash Impact ($M)":[round(cash_dso,1), round(cash_dio,1), round(cash_dpo,1), round(total_cash_release,1)],
        })
        st.dataframe(wc_rows, use_container_width=True, hide_index=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Current CCC",        f"{ccc_curr:.0f} days")
        c2.metric("Target CCC",         f"{ccc_tgt:.0f} days", delta=f"{ccc_curr-ccc_tgt:+.0f} days improvement")
        c3.metric("Total Cash Released", f"${total_cash_release:.1f}M",
                  delta="✅ Cash In" if total_cash_release > 0 else "🔴 Cash Out")
        c4.metric("As % of Revenue",    f"{total_cash_release/rev_wc*100:.1f}%")

        fig = go.Figure(go.Bar(
            x=["DSO Improvement", "DIO Improvement", "DPO Extension", "Total"],
            y=[cash_dso, cash_dio, cash_dpo, total_cash_release],
            marker_color=["#185FA5","#1D9E75","#BA7517","#2A4858"],
            text=[f"${v:.1f}M" for v in [cash_dso, cash_dio, cash_dpo, total_cash_release]],
            textposition="outside"
        ))
        fig.update_layout(title="Working Capital Cash Release by Lever ($M)",
                          template="plotly_white", height=380, yaxis_title="Cash Released ($M)")
        st.plotly_chart(fig, use_container_width=True)

        # AR Aging heatmap simulator
        st.markdown("**Receivables Aging Buckets (Current vs. Target)**")
        aging_curr = [45, 28, 15, 8, 4]
        aging_tgt  = [58, 26, 10, 4, 2]
        buckets    = ["0–30 days", "31–60 days", "61–90 days", "91–120 days", "> 120 days (bad debt risk)"]
        aging_df   = pd.DataFrame({
            "Bucket": buckets,
            "Current % of AR": aging_curr,
            "Target % of AR":  aging_tgt,
            "Movement":        [f"{t-c:+}pp" for c, t in zip(aging_curr, aging_tgt)],
        })
        st.dataframe(aging_df, use_container_width=True, hide_index=True)

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: 13-Week Cash Flow Forecast — Retail Group in Liquidity Stress", "🧪")
        st.markdown("""
**Situation:** You are the Group Treasurer. The CFO has just been informed that the company's
revolving credit facility (RCF) has a covenant breach risk in 9 weeks. She needs a 13-week
cash flow forecast by end of day to assess liquidity headroom and identify action levers.
        """)

        np.random.seed(7)
        weeks = [f"Wk {i}" for i in range(1, 14)]

        # Collections vary with seasonality
        collections = [18.5, 16.2, 22.4, 19.8, 15.1, 21.3, 18.9,
                        23.5, 17.2, 19.1, 14.8, 20.4, 22.1]
        # Payments: payroll Wk 1 & 7, rent Wk 1, large supplier Wk 4 & 10
        supplier = [8.2, 7.5, 8.8, 15.4, 7.9, 8.1, 7.6,
                    8.5, 7.8, 16.2, 7.4, 8.0, 8.3]
        payroll  = [4.5, 0, 0, 0, 0, 0, 4.5, 0, 0, 0, 0, 0, 4.5]
        overheads= [2.1, 1.8, 2.0, 1.9, 2.2, 1.8, 2.0,
                    2.1, 1.9, 2.0, 1.8, 2.1, 1.9]
        rent     = [3.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.5]
        capex    = [0, 0, 1.2, 0, 0, 2.5, 0, 0, 1.2, 0, 0, 0, 0]

        total_in  = collections
        total_out = [s+p+o+r+c for s,p,o,r,c in zip(supplier, payroll, overheads, rent, capex)]
        net_weekly= [ti - to for ti, to in zip(total_in, total_out)]

        opening_cash = 12.0
        closing = []
        for nw in net_weekly:
            opening_cash += nw
            closing.append(round(opening_cash, 1))

        rfc_limit = 5.0  # covenant: cash must stay above $5M

        df_13w = pd.DataFrame({
            "Week":           weeks,
            "Collections ($M)": [round(v,1) for v in collections],
            "Supplier Pay ($M)": [round(v,1) for v in supplier],
            "Payroll ($M)":      payroll,
            "Overheads ($M)":    [round(v,1) for v in overheads],
            "Rent ($M)":         rent,
            "Capex ($M)":        capex,
            "Net Cash ($M)":     [round(v,1) for v in net_weekly],
            "Closing Cash ($M)": closing,
            "Covenant OK?":      ["✅" if c >= rfc_limit else "🔴 BREACH RISK" for c in closing],
        })
        st.dataframe(df_13w, use_container_width=True, hide_index=True)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=weeks, y=net_weekly,
                             marker_color=["#1D9E75" if v >= 0 else "#E24B4A" for v in net_weekly],
                             name="Weekly Net Cash ($M)"))
        fig.add_trace(go.Scatter(x=weeks, y=closing, name="Closing Cash Balance",
                                 mode="lines+markers", line=dict(color="#185FA5", width=2.5),
                                 marker=dict(size=8)))
        fig.add_hline(y=rfc_limit, line_dash="dash", line_color="red",
                      annotation_text=f"Covenant Floor: ${rfc_limit}M")
        fig.update_layout(title="13-Week Cash Flow Forecast — Closing Cash vs. Covenant Floor",
                          template="plotly_white", height=420,
                          yaxis_title="$M", legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)

        breach_weeks = [w for w, c in zip(weeks, closing) if c < rfc_limit]
        min_cash_wk  = weeks[closing.index(min(closing))]

        if breach_weeks:
            st.error(f"🚨 COVENANT BREACH RISK: Cash falls below ${rfc_limit}M floor in {', '.join(breach_weeks)}. Minimum cash point: ${min(closing):.1f}M in {min_cash_wk}.")
        else:
            st.success(f"✅ No covenant breach in 13-week window. Minimum cash: ${min(closing):.1f}M ({min_cash_wk}).")

        st.success("""
**CFO Action Plan — Liquidity Management:**

| Action | Timing | Estimated Cash Impact |
|--------|--------|----------------------|
| Accelerate key customer collections (top 5 accounts) | Weeks 1–3 | +$4.5M |
| Defer non-critical Capex (Wk 6 spend) | Week 6 | +$2.5M |
| Negotiate 2-week extension on Wk 10 supplier payment | Week 10 | +$3.0M |
| Draw $5M on RCF as liquidity buffer | Week 2 | +$5.0M |
| **Total headroom created** | | **+$15.0M** |

With these actions, minimum closing cash improves to ~$9M — comfortably above covenant floor.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 7 Quiz", "❓")
        _quiz("1. Free Cash Flow (FCF) is best defined as:",
              ["EBITDA minus interest and tax",
               "Operating Cash Flow minus Capital Expenditure",
               "Net Profit plus Depreciation",
               "Revenue minus all operating costs"],
              "Operating Cash Flow minus Capital Expenditure", "fa_m7q1")
        st.divider()
        _quiz("2. A company has DSO=60, DIO=45, DPO=30. The CCC is:",
              ["135 days", "15 days", "75 days", "45 days"], "75 days", "fa_m7q2")
        st.divider()
        _quiz("3. If annual revenue is $730M and DSO improves by 5 days, the cash released is approximately:",
              ["$1M", "$5M", "$10M", "$20M"], "$10M", "fa_m7q3")
        st.divider()
        _quiz("4. A cash conversion rate of 45% (FCF/EBITDA) signals:",
              ["Excellent cash generation",
               "Working capital build or high capex is consuming a large share of EBITDA",
               "The company has negative EBITDA",
               "Interest payments are too low"],
              "Working capital build or high capex is consuming a large share of EBITDA", "fa_m7q4")
        st.divider()
        _quiz("5. Receivables aging analysis is most useful for:",
              ["Calculating depreciation charges",
               "Identifying overdue invoices and quantifying bad debt risk before it crystallises",
               "Benchmarking product margins",
               "Forecasting revenue growth"],
              "Identifying overdue invoices and quantifying bad debt risk before it crystallises", "fa_m7q5")
        st.divider()
        _quiz("6. A 13-week cash flow forecast uses the direct method, which means:",
              ["It is derived from the P&L using accrual adjustments",
               "It tracks actual cash receipts and payments week by week",
               "It is produced once a year",
               "It focuses on investing activities only"],
              "It tracks actual cash receipts and payments week by week", "fa_m7q6")