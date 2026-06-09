import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

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
    st.title("📊 Module 1: Descriptive & Historical Analytics")
    st.caption("Summarise what happened — trend, structure, ratios and health metrics")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Trend Calculator", "📊 Ratio Analyser", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Horizontal & Trend Analytics", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Year-on-Year (YoY) & Period-on-Period (PoP)**
| Technique | Formula | Use Case |
|-----------|---------|----------|
| YoY Growth | (Current − Prior) / Prior | Revenue, EBITDA annual change |
| MoM Growth | (This Month − Last Month) / Last Month | Short-cycle operational KPIs |
| QoQ Growth | (This Q − Last Q) / Last Q | Quarterly earnings reporting |

**Base-Year Indexation**
```
Index = (Current Year Value / Base Year Value) × 100
```
Sets a fixed starting point (= 100) to compare compounding growth paths across multiple metrics simultaneously.

**CAGR (Compound Annual Growth Rate)**
```
CAGR = (End Value / Start Value)^(1/n) − 1
```
Smooths annual volatility to reveal the steady geometric growth rate over n years.
            """)
        with c2:
            st.markdown("""
**Vertical & Structural Analytics**

**Common-Size Income Statement** (% of Revenue):
- Gross Margin % = Gross Profit / Revenue
- EBITDA Margin % = EBITDA / Revenue
- Net Margin % = Net Profit / Revenue

Reveals cost structure and margin profiles across periods and peers.

**Common-Size Balance Sheet** (% of Total Assets):
- Shows capital allocation and leverage structure

**Per-Unit / Operational Metrics:**
| Metric | Calculation |
|--------|-------------|
| Revenue per Employee | Revenue / Headcount |
| Cost per Unit | Total COGS / Units Produced |
| Logistics Cost / km | Total Logistics Cost / km Shipped |
| Revenue per SKU | Segment Revenue / Number of SKUs |
            """)

        _sec("Key Financial Ratios", "📋")
        st.dataframe(pd.DataFrame({
            "Category":  ["Liquidity","Liquidity","Solvency","Solvency",
                          "Efficiency","Efficiency","Efficiency","Efficiency",
                          "Profitability","Profitability","Profitability","Profitability"],
            "Ratio":     ["Current Ratio","Quick Ratio","Debt-to-Equity","Interest Coverage",
                          "Asset Turnover","Days Inventory (DIO)","Days Receivable (DSO)","Days Payable (DPO)",
                          "Gross Margin","EBITDA Margin","ROE","ROCE"],
            "Formula":   ["Current Assets / Current Liabilities",
                          "(Current Assets − Inventory) / Current Liabilities",
                          "Total Debt / Shareholders' Equity",
                          "EBIT / Interest Expense",
                          "Revenue / Average Total Assets",
                          "Inventory / COGS × 365",
                          "Receivables / Revenue × 365",
                          "Payables / COGS × 365",
                          "Gross Profit / Revenue",
                          "EBITDA / Revenue",
                          "Net Profit / Average Equity",
                          "EBIT / (Total Assets − Current Liabilities)"],
            "Benchmark": ["> 1.5×","≥ 1.0×","< 2.0×","> 3.0×",
                          "Industry specific","30–60 days","30–45 days","30–60 days",
                          "> 40% (mfg)","15–25%","15–20%+","10–15%+"],
        }), use_container_width=True, hide_index=True)

        _sec("DuPont Analysis — ROE Decomposition", "🔬")
        st.markdown("""
```
ROE = Net Profit Margin  ×  Asset Turnover  ×  Financial Leverage
    = (Net Profit/Revenue) × (Revenue/Assets) × (Assets/Equity)
```
**Why it matters:** Two companies can have the same ROE for very different reasons — one via fat margins, 
another via aggressive leverage. DuPont exposes which lever is driving returns, and which is at risk.

**Cash Conversion Cycle (CCC):**
```
CCC = DIO + DSO − DPO
```
Lower CCC = faster cash generation from operations. Negative CCC (e.g. Amazon, Zara) = customers pay 
before suppliers are paid — a structural working capital advantage.
        """)
        st.warning("⚠️ Ratios are only meaningful in context — compare against prior periods, peers, and industry benchmarks simultaneously. A single ratio in isolation can mislead.")

    # ── TREND CALCULATOR ──────────────────────────────────────────────────────
    with tab2:
        _sec("YoY / CAGR / Index Calculator", "🧮")
        st.markdown("Enter up to 6 years of annual revenue data:")
        cols = st.columns(6)
        years_range = list(range(2019, 2025))
        defaults = [410.0, 445.0, 398.0, 487.0, 532.0, 578.0]
        values = []
        for i, col in enumerate(cols):
            with col:
                v = st.number_input(str(years_range[i]), value=defaults[i], step=1.0, key=f"tr_{i}")
                values.append(v)

        base_yr = st.selectbox("Base year for indexation:", years_range, index=0)
        base_idx = years_range.index(base_yr)
        base_val = values[base_idx]

        rows = []
        for i, (yr, val) in enumerate(zip(years_range, values)):
            yoy = (val / values[i-1] - 1) * 100 if i > 0 else None
            idx = val / base_val * 100
            n = i - base_idx
            cagr = ((val / base_val) ** (1 / n) - 1) * 100 if n > 0 else None
            rows.append({
                "Year": yr,
                "Revenue ($M)": val,
                "YoY Growth": f"{yoy:+.1f}%" if yoy is not None else "Base",
                "Index": f"{idx:.1f}",
                "CAGR from Base": f"{cagr:.1f}%" if cagr is not None else "Base",
            })
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=years_range, y=values, name="Revenue ($M)",
                             marker_color="#185FA5", opacity=0.7))
        yoy_vals = [None] + [(values[i]/values[i-1]-1)*100 for i in range(1, len(values))]
        fig.add_trace(go.Scatter(x=years_range, y=yoy_vals, name="YoY Growth (%)",
                                 mode="lines+markers", yaxis="y2",
                                 line=dict(color="#E24B4A", width=2)))
        fig.update_layout(
            title="Revenue Trend with YoY Growth Rate",
            template="plotly_white", height=400,
            yaxis=dict(title="Revenue ($M)"),
            yaxis2=dict(title="YoY Growth (%)", overlaying="y", side="right", ticksuffix="%"),
            legend=dict(orientation="h", y=1.02)
        )
        st.plotly_chart(fig, use_container_width=True)

        # Index chart
        idx_vals = [v / base_val * 100 for v in values]
        fig2 = go.Figure(go.Scatter(x=years_range, y=idx_vals, mode="lines+markers",
                                    line=dict(color="#1D9E75", width=2.5),
                                    marker=dict(size=8)))
        fig2.add_hline(y=100, line_dash="dash", line_color="gray", annotation_text=f"Base Year ({base_yr}) = 100")
        fig2.update_layout(title=f"Revenue Growth Index (Base Year = {base_yr})",
                           yaxis_title="Index (Base = 100)",
                           template="plotly_white", height=340)
        st.plotly_chart(fig2, use_container_width=True)

        overall_cagr = ((values[-1] / values[0]) ** (1/(len(values)-1)) - 1) * 100
        st.info(f"📌 **6-Year CAGR (2019–2024): {overall_cagr:.1f}%** — Revenue has grown from ${values[0]:.0f}M to ${values[-1]:.0f}M over 5 years.")

    # ── RATIO ANALYSER ────────────────────────────────────────────────────────
    with tab3:
        _sec("Financial Ratio Dashboard", "📊")
        st.markdown("Input P&L and Balance Sheet data to generate a full ratio profile:")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Income Statement ($M)**")
            revenue   = st.number_input("Revenue", value=500.0, step=10.0, key="r_rev")
            cogs      = st.number_input("COGS", value=220.0, step=5.0, key="r_cogs")
            sga       = st.number_input("SG&A", value=80.0, step=5.0, key="r_sga")
            da        = st.number_input("D&A", value=25.0, step=1.0, key="r_da")
            interest  = st.number_input("Interest Expense", value=12.0, step=1.0, key="r_int")
            tax_rate  = st.number_input("Tax Rate (%)", value=25.0, step=1.0, key="r_tax") / 100
        with c2:
            st.markdown("**Balance Sheet ($M)**")
            curr_assets  = st.number_input("Current Assets", value=180.0, step=5.0, key="r_ca")
            inventory    = st.number_input("  of which: Inventory", value=65.0, step=5.0, key="r_inv")
            receivables  = st.number_input("  of which: Receivables", value=70.0, step=5.0, key="r_rec")
            total_assets = st.number_input("Total Assets", value=620.0, step=10.0, key="r_ta")
            curr_liab    = st.number_input("Current Liabilities", value=110.0, step=5.0, key="r_cl")
            payables     = st.number_input("  of which: Payables", value=55.0, step=5.0, key="r_pay")
        with c3:
            st.markdown("**Capital Structure ($M)**")
            total_debt   = st.number_input("Total Debt", value=200.0, step=10.0, key="r_debt")
            equity       = st.number_input("Shareholders' Equity", value=280.0, step=10.0, key="r_eq")

        gross_profit = revenue - cogs
        ebitda = gross_profit - sga
        ebit = ebitda - da
        ebt = ebit - interest
        net_profit = ebt * (1 - tax_rate)

        ratios = {
            "Gross Margin %":        gross_profit / revenue * 100,
            "EBITDA Margin %":       ebitda / revenue * 100,
            "EBIT Margin %":         ebit / revenue * 100,
            "Net Margin %":          net_profit / revenue * 100,
            "Current Ratio":         curr_assets / curr_liab,
            "Quick Ratio":           (curr_assets - inventory) / curr_liab,
            "Debt-to-Equity":        total_debt / equity,
            "Interest Coverage":     ebit / interest,
            "Asset Turnover":        revenue / total_assets,
            "DIO (days)":            inventory / cogs * 365,
            "DSO (days)":            receivables / revenue * 365,
            "DPO (days)":            payables / cogs * 365,
            "ROE %":                 net_profit / equity * 100,
            "ROCE %":                ebit / (total_assets - curr_liab) * 100,
        }
        ccc = ratios["DIO (days)"] + ratios["DSO (days)"] - ratios["DPO (days)"]

        benchmarks = {
            "Gross Margin %":    (35, 55),  "EBITDA Margin %":   (12, 25),
            "EBIT Margin %":     (8, 18),   "Net Margin %":      (5, 15),
            "Current Ratio":     (1.5, 3.0),"Quick Ratio":       (1.0, 2.0),
            "Debt-to-Equity":    (0.5, 2.0),"Interest Coverage": (3.0, 8.0),
            "Asset Turnover":    (0.6, 1.2),"DIO (days)":        (30, 60),
            "DSO (days)":        (30, 50),  "DPO (days)":        (30, 60),
            "ROE %":             (12, 22),  "ROCE %":            (10, 18),
        }

        ratio_rows = []
        for name, val in ratios.items():
            lo, hi = benchmarks.get(name, (None, None))
            if lo is not None:
                if val >= lo and val <= hi: sig = "✅ On-track"
                elif val < lo:             sig = "🔴 Below benchmark"
                else:                      sig = "🟢 Above benchmark"
            else: sig = "—"
            ratio_rows.append({"Ratio": name, "Value": round(val, 2), "Status": sig,
                                "Benchmark Range": f"{lo} – {hi}"})

        st.markdown("**Computed Ratio Dashboard:**")
        st.dataframe(pd.DataFrame(ratio_rows), use_container_width=True, hide_index=True)

        c1, c2, c3 = st.columns(3)
        c1.metric("Cash Conversion Cycle", f"{ccc:.0f} days",
                  delta="lower is better", delta_color="off")
        c2.metric("EBITDA ($M)", f"${ebitda:.1f}M")
        c3.metric("Net Profit ($M)", f"${net_profit:.1f}M")

        # DuPont
        st.markdown("**DuPont ROE Decomposition:**")
        npm = net_profit / revenue
        at  = revenue / total_assets
        fl  = total_assets / equity
        d1, d2, d3, d4 = st.columns(4)
        d1.metric("Net Profit Margin", f"{npm*100:.1f}%")
        d2.metric("Asset Turnover",    f"{at:.2f}×")
        d3.metric("Financial Leverage",f"{fl:.2f}×")
        d4.metric("ROE (DuPont)",       f"{npm*at*fl*100:.1f}%")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: 5-Year Descriptive Analysis — Apex Manufacturing Ltd", "🧪")
        st.markdown("""
**Business Situation:** You are the Group FP&A Director at Apex Manufacturing.
The Board has requested a complete historical performance review covering 2020–2024.
Your task: deliver a full descriptive analytics narrative covering trend, structure, ratios, and health.
        """)

        years = [2020, 2021, 2022, 2023, 2024]
        rev   = [380, 415, 442, 498, 545]
        cogs_ = [228, 241, 262, 289, 312]
        sga_  = [76,   83,  88,  100, 109]
        da_   = [22,   24,  25,   27,  29]
        int_  = [14,   13,  12,   11,  10]

        gp_   = [r-c for r,c in zip(rev, cogs_)]
        ebitda_  = [g-s for g,s in zip(gp_, sga_)]
        ebit_ = [e-d for e,d in zip(ebitda_, da_)]
        ni_   = [(e-i)*0.75 for e,i in zip(ebit_, int_)]

        pnl = pd.DataFrame({
            "Year": years,
            "Revenue": rev, "COGS": cogs_, "Gross Profit": gp_,
            "SG&A": sga_, "EBITDA": ebitda_, "EBIT": ebit_, "Net Income": [round(n,1) for n in ni_],
        })

        st.markdown("**Step 1 — 5-Year P&L Summary ($M)**")
        st.dataframe(pnl, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — Common-Size Analysis (% of Revenue)**")
        cs = pd.DataFrame({"Year": years})
        for col in ["COGS","Gross Profit","SG&A","EBITDA","Net Income"]:
            cs[col+" %"] = [round(pnl[col][i]/pnl["Revenue"][i]*100, 1) for i in range(5)]
        st.dataframe(cs, use_container_width=True, hide_index=True)

        st.markdown("**Step 3 — Revenue Trend vs. Margin Profile**")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=years, y=rev, name="Revenue ($M)", marker_color="#B5D4F4"))
        fig.add_trace(go.Scatter(x=years, y=[e/r*100 for e,r in zip(ebitda_,rev)],
                                 name="EBITDA Margin %", yaxis="y2", mode="lines+markers",
                                 line=dict(color="#1D9E75", width=2.5)))
        fig.add_trace(go.Scatter(x=years, y=[n/r*100 for n,r in zip(ni_,rev)],
                                 name="Net Margin %", yaxis="y2", mode="lines+markers",
                                 line=dict(color="#E24B4A", width=2, dash="dash")))
        fig.update_layout(title="Revenue Growth vs. Margin Trend (2020–2024)",
                          template="plotly_white", height=400,
                          yaxis=dict(title="Revenue ($M)"),
                          yaxis2=dict(title="Margin %", overlaying="y", side="right"),
                          legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 4 — CAGR & Growth Summary**")
        cagr_rev   = (rev[-1]/rev[0])**(1/4) - 1
        cagr_ebitda = (ebitda_[-1]/ebitda_[0])**(1/4) - 1
        cagr_ni    = (ni_[-1]/ni_[0])**(1/4) - 1
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Revenue CAGR (4yr)",  f"{cagr_rev*100:.1f}%")
        c2.metric("EBITDA CAGR (4yr)",   f"{cagr_ebitda*100:.1f}%")
        c3.metric("Net Income CAGR",     f"{cagr_ni*100:.1f}%")
        c4.metric("2024 EBITDA Margin",  f"{ebitda_[-1]/rev[-1]*100:.1f}%")

        idx_rev = [r/rev[0]*100 for r in rev]
        idx_ebitda = [e/ebitda_[0]*100 for e in ebitda_]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=years, y=idx_rev, name="Revenue Index",
                                  mode="lines+markers", line=dict(color="#185FA5", width=2.5)))
        fig2.add_trace(go.Scatter(x=years, y=idx_ebitda, name="EBITDA Index",
                                  mode="lines+markers", line=dict(color="#1D9E75", width=2.5)))
        fig2.add_hline(y=100, line_dash="dash", line_color="gray", annotation_text="Base = 100 (2020)")
        fig2.update_layout(title="Revenue & EBITDA Growth Index (Base 2020 = 100)",
                           yaxis_title="Index", template="plotly_white", height=340)
        st.plotly_chart(fig2, use_container_width=True)

        st.success("""
**Board Summary — Apex Manufacturing 2020–2024**

| KPI | 2020 | 2024 | CAGR | Trend |
|-----|------|------|------|-------|
| Revenue ($M) | $380M | $545M | +9.4% | ✅ Consistent growth |
| EBITDA Margin | 20.0% | 22.8% | +2.8pp | ✅ Margin expansion |
| Net Margin | 9.7% | 11.4% | +1.7pp | ✅ Improving profitability |
| COGS % Rev | 60.0% | 57.2% | −2.8pp | ✅ Efficiency gains |
| SG&A % Rev | 20.0% | 20.0% | Flat | ⚠️ Not leveraging scale |

**Key Insight:** Revenue and EBITDA are both growing, but EBITDA is growing faster (CAGR +11.2% vs +9.4%) — indicating genuine margin expansion, not just top-line scale. SG&A has not been leveraged; an SG&A efficiency programme should be a 2025 priority.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 1 Quiz", "❓")
        _quiz("1. Revenue grew from $400M to $600M over 4 years. What is the CAGR?",
              ["10.7%", "12.5%", "50.0%", "10.0%"], "10.7%", "fa_m1q1")
        st.divider()
        _quiz("2. A company has DIO=45, DSO=40, DPO=50. What is the Cash Conversion Cycle?",
              ["135 days", "35 days", "50 days", "95 days"], "35 days", "fa_m1q2")
        st.divider()
        _quiz("3. Common-size income statement expresses all items as % of:",
              ["Total Assets", "Total Equity", "Revenue", "EBITDA"], "Revenue", "fa_m1q3")
        st.divider()
        _quiz("4. DuPont analysis decomposes ROE into which three components?",
              ["Gross margin × EBITDA margin × Net margin",
               "Net profit margin × Asset turnover × Financial leverage",
               "Revenue growth × Margin expansion × Leverage",
               "ROIC × WACC × Capital turns"],
              "Net profit margin × Asset turnover × Financial leverage", "fa_m1q4")
        st.divider()
        _quiz("5. Interest Coverage Ratio of 1.8× means:",
              ["Company earns 1.8× its revenue in interest",
               "EBIT barely covers interest — elevated financial risk",
               "Debt is 1.8× equity",
               "Company has 1.8 months of cash"],
              "EBIT barely covers interest — elevated financial risk", "fa_m1q5")
        st.divider()
        _quiz("6. Base-year indexation is most useful for:",
              ["Calculating tax liabilities",
               "Comparing growth paths of metrics with different absolute scales",
               "Measuring daily price volatility",
               "Identifying duplicate journal entries"],
              "Comparing growth paths of metrics with different absolute scales", "fa_m1q6")