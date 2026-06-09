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
    st.title("🔍 Module 3: Diagnostic & Variance Analytics")
    st.caption("Diagnose WHY it happened — variance decomposition, cost analysis, and root cause")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 PVM Bridge", "📊 Cost Behaviour", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Price-Volume-Mix Decomposition", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Core Bridge Formula**
```
Revenue Variance = Price Effect + Volume Effect + Mix Effect

Price Effect  = (Actual Price  − Budget Price)  × Actual Volume
Volume Effect = (Actual Volume − Budget Volume) × Budget Price
Mix Effect    = Total Variance − Price Effect − Volume Effect
```
Each effect is isolated so management can act on the correct lever.

**The 5-Why Framework**
| Level | Question | Example |
|-------|----------|---------|
| Why 1 | Why did EBITDA miss? | Revenue below plan |
| Why 2 | Why was revenue low? | Volume down 12% |
| Why 3 | Why was volume down? | 3 accounts churned |
| Why 4 | Why did they churn? | Competitor undercut price |
| Why 5 | Why weren't we aware? | No churn early-warning KRI |

The 5-Why stops at a root cause that has a clear action — not just another symptom.
            """)
        with c2:
            st.markdown("""
**Standard Costing Variances (Manufacturing)**
```
Material Cost Variance
├── Price Variance: (Std Price − Actual Price) × Actual Qty
└── Usage Variance: (Std Qty − Actual Qty) × Std Price

Labour Cost Variance
├── Rate Variance: (Std Rate − Actual Rate) × Actual Hours
└── Efficiency Variance: (Std Hours − Actual Hours) × Std Rate

Overhead Variance
├── Spending Variance: Budgeted OH − Actual OH
└── Volume Variance: Absorbed OH − Budgeted OH
```
**Activity-Based Costing (ABC):**
Traditional overhead allocation distorts true product cost. ABC assigns
indirect costs to activities (machine setup, quality inspection, shipping),
then assigns those activities to products based on actual consumption.

Result: Reveals products that appear profitable under absorption costing
but are actually margin destroyers when true overhead is assigned.
            """)

        _sec("Cost Behaviour Analysis", "📊")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Cost Types:**
| Type | Behaviour | Example |
|------|-----------|---------|
| Fixed | Constant regardless of volume | Rent, insurance, base salaries |
| Variable | Changes proportionally | Raw materials, sales commission |
| Semi-variable | Fixed base + variable element | Utilities, maintenance |
| Step-fixed | Fixed within ranges, jumps at thresholds | Adding a shift, new warehouse |

**High-Low Method:**
```
Variable Cost/Unit = (Highest Cost − Lowest Cost) / (Highest − Lowest Volume)
Fixed Cost = Total Cost at Either Point − (Variable Rate × Volume)
```
            """)
        with c2:
            st.markdown("""
**Cost-Volume-Profit (CVP) Analysis:**
```
Break-Even Volume = Fixed Costs / Contribution Margin per Unit
Contribution Margin = Selling Price − Variable Cost per Unit
Margin of Safety = (Actual Revenue − Break-Even Revenue) / Actual Revenue

Target Profit Volume = (Fixed Costs + Target Profit) / CM per Unit
```
**Operating Leverage:**
```
Operating Leverage = Contribution Margin / EBIT
```
A high operating leverage business (e.g. airlines, manufacturers) sees
EBIT swing dramatically with small revenue changes — much more than
a low-leverage, variable-cost business (e.g. staffing agencies).
            """)

    # ── PVM BRIDGE ────────────────────────────────────────────────────────────
    with tab2:
        _sec("Price-Volume-Mix Revenue Bridge Calculator", "🧮")
        products = ["Product A", "Product B", "Product C", "Product D"]
        db = [(500, 10.0), (300, 15.0), (200, 20.0), (150, 25.0)]
        da = [(480, 11.5), (340, 14.0), (190, 22.0), (170, 24.0)]

        hdr = st.columns([2, 1.5, 1.5, 1.5, 1.5])
        for h, lbl in zip(hdr, ["Product", "Budget Vol", "Budget Price", "Actual Vol", "Actual Price"]):
            h.markdown(f"**{lbl}**")

        bvs, bps, avs, aps = [], [], [], []
        for i, prod in enumerate(products):
            c1, c2, c3, c4, c5 = st.columns([2, 1.5, 1.5, 1.5, 1.5])
            with c1: st.markdown(f"*{prod}*")
            with c2: bv = st.number_input(f"bv{i}", value=float(db[i][0]), key=f"pvm_bv{i}", label_visibility="collapsed")
            with c3: bp = st.number_input(f"bp{i}", value=db[i][1],        key=f"pvm_bp{i}", label_visibility="collapsed")
            with c4: av = st.number_input(f"av{i}", value=float(da[i][0]), key=f"pvm_av{i}", label_visibility="collapsed")
            with c5: ap = st.number_input(f"ap{i}", value=da[i][1],        key=f"pvm_ap{i}", label_visibility="collapsed")
            bvs.append(bv); bps.append(bp); avs.append(av); aps.append(ap)

        rows = []
        tb, ta, tpe, tve, tme = 0, 0, 0, 0, 0
        for i, prod in enumerate(products):
            br = bvs[i] * bps[i]; ar = avs[i] * aps[i]
            pe = (aps[i] - bps[i]) * avs[i]
            ve = (avs[i] - bvs[i]) * bps[i]
            me = (ar - br) - pe - ve
            rows.append({"Product": prod, "Budget": round(br, 1), "Actual": round(ar, 1),
                         "Total Var": round(ar-br, 1), "Price Effect": round(pe, 1),
                         "Volume Effect": round(ve, 1), "Mix Effect": round(me, 1)})
            tb += br; ta += ar; tpe += pe; tve += ve; tme += me

        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        tv = ta - tb
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Total Budget",   f"${tb:,.0f}")
        c2.metric("Total Actual",   f"${ta:,.0f}")
        c3.metric("Price Effect",   f"${tpe:+,.0f}")
        c4.metric("Volume Effect",  f"${tve:+,.0f}")
        c5.metric("Mix Effect",     f"${tme:+,.0f}")

        fig = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "relative", "relative", "total"],
            x=["Budget", "Price Effect", "Volume Effect", "Mix Effect", "Actual"],
            y=[tb, tpe, tve, tme, 0],
            text=[f"${tb:,.0f}", f"${tpe:+,.0f}", f"${tve:+,.0f}", f"${tme:+,.0f}", f"${ta:,.0f}"],
            textposition="outside",
            connector={"line": {"color": "#888"}},
            increasing={"marker": {"color": "#1D9E75"}},
            decreasing={"marker": {"color": "#E24B4A"}},
            totals={"marker": {"color": "#185FA5"}}
        ))
        fig.update_layout(title="Revenue Bridge: Budget to Actual ($)",
                          template="plotly_white", height=400)
        st.plotly_chart(fig, use_container_width=True)

        primary = max([("Price", abs(tpe)), ("Volume", abs(tve)), ("Mix", abs(tme))], key=lambda x: x[1])
        if tv < 0:
            st.error(f"⚠️ Revenue is **${abs(tv):,.0f} below budget**. Primary driver: **{primary[0]} Effect** (${primary[1]:+,.0f}). Investigate this first.")
        else:
            st.success(f"✅ Revenue is **${tv:,.0f} above budget**. Primary driver: **{primary[0]} Effect** (${primary[1]:+,.0f}).")

    # ── COST BEHAVIOUR ────────────────────────────────────────────────────────
    with tab3:
        _sec("Cost-Volume-Profit & Break-Even Analyser", "📊")
        c1, c2, c3 = st.columns(3)
        with c1:
            sp = st.number_input("Selling Price per Unit ($)", value=50.0, step=1.0, key="cvp_sp")
            vc = st.number_input("Variable Cost per Unit ($)", value=30.0, step=1.0, key="cvp_vc")
        with c2:
            fc = st.number_input("Total Fixed Costs ($)", value=100000.0, step=5000.0, key="cvp_fc")
            tp = st.number_input("Target Profit ($)", value=50000.0, step=5000.0, key="cvp_tp")
        with c3:
            av_units = st.number_input("Actual Units Sold", value=8000.0, step=100.0, key="cvp_av")

        cm = sp - vc
        cm_ratio = cm / sp * 100
        be_units = fc / cm
        be_rev   = be_units * sp
        tp_units = (fc + tp) / cm
        mos_units = av_units - be_units
        mos_pct   = mos_units / av_units * 100 if av_units > 0 else 0
        actual_profit = (av_units * cm) - fc
        op_leverage = (av_units * cm) / actual_profit if actual_profit > 0 else float("inf")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Contribution Margin / Unit", f"${cm:.2f}")
        c2.metric("CM Ratio", f"{cm_ratio:.1f}%")
        c3.metric("Break-Even (units)", f"{be_units:,.0f}")
        c4.metric("Break-Even (revenue)", f"${be_rev:,.0f}")
        c5, c6, c7, c8 = st.columns(4)
        c5.metric("Target Profit Volume", f"{tp_units:,.0f} units")
        c6.metric("Margin of Safety", f"{mos_pct:.1f}%")
        c7.metric("Actual Profit", f"${actual_profit:,.0f}")
        c8.metric("Operating Leverage", f"{op_leverage:.1f}×")

        unit_range = np.linspace(0, max(av_units * 1.5, tp_units * 1.2), 200)
        total_rev  = unit_range * sp
        total_cost = fc + unit_range * vc
        profit_line = total_rev - total_cost

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=unit_range, y=total_rev,  name="Total Revenue",  line=dict(color="#185FA5", width=2)))
        fig.add_trace(go.Scatter(x=unit_range, y=total_cost, name="Total Cost",      line=dict(color="#E24B4A", width=2)))
        fig.add_trace(go.Scatter(x=unit_range, y=profit_line,name="Profit / Loss",   line=dict(color="#1D9E75", width=1.5, dash="dot")))
        fig.add_vline(x=be_units, line_dash="dash", line_color="orange",
                      annotation_text=f"Break-Even: {be_units:,.0f} units")
        fig.add_vline(x=av_units, line_dash="dash", line_color="green",
                      annotation_text=f"Actual: {av_units:,.0f} units")
        fig.add_hline(y=0, line_color="black", line_width=0.5)
        fig.update_layout(title="CVP Chart — Revenue, Cost & Profit",
                          xaxis_title="Units Sold", yaxis_title="$ Amount",
                          template="plotly_white", height=420)
        st.plotly_chart(fig, use_container_width=True)

        if op_leverage > 5:
            st.warning(f"⚠️ Operating leverage of {op_leverage:.1f}× is HIGH. A 10% revenue drop would reduce profit by ~{op_leverage*10:.0f}%.")
        else:
            st.info(f"ℹ️ Operating leverage of {op_leverage:.1f}×. A 10% revenue increase would boost profit by ~{op_leverage*10:.0f}%.")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Diagnosing a $38M EBITDA Miss — Consumer Goods Q2 2024", "🧪")
        st.markdown("""
**Situation:** You are the Group FP&A Director. Q2 2024 EBITDA came in at **$82M vs. budget $120M** — a **$38M miss (32%)**.
The Board needs a complete root-cause diagnosis within 24 hours.
        """)

        st.markdown("**Step 1 — P&L Variance Summary**")
        pnl_data = pd.DataFrame({
            "Line Item":     ["Revenue", "COGS", "Gross Profit", "SG&A", "R&D", "EBITDA"],
            "Budget ($M)":   [450, -180, 270, -108, -42, 120],
            "Actual ($M)":   [428, -196, 232, -116, -34, 82],
        })
        pnl_data["Variance ($M)"]  = pnl_data["Actual ($M)"] - pnl_data["Budget ($M)"]
        pnl_data["Variance (%)"]   = (pnl_data["Variance ($M)"] / pnl_data["Budget ($M)"].abs() * 100).round(1)
        pnl_data["Signal"] = pnl_data["Variance ($M)"].apply(lambda v: "🔴 Miss" if v < 0 else "🟢 Beat")
        st.dataframe(pnl_data, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — EBITDA Waterfall Bridge**")
        fig = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "relative", "relative", "relative", "total"],
            x=["Budget EBITDA", "Revenue Miss", "COGS Overshoot", "SG&A Over-run", "R&D Saving", "Actual EBITDA"],
            y=[120, -22, -16, -8, 8, 0],
            text=["$120M", "-$22M", "-$16M", "-$8M", "+$8M", "$82M"],
            textposition="outside",
            connector={"line": {"color": "#888"}},
            increasing={"marker": {"color": "#1D9E75"}},
            decreasing={"marker": {"color": "#E24B4A"}},
            totals={"marker": {"color": "#185FA5"}}
        ))
        fig.update_layout(title="EBITDA Bridge — Budget to Actual Q2 2024 ($M)",
                          template="plotly_white", height=420, yaxis_title="EBITDA ($M)")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 3 — Revenue PVM Decomposition**")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Revenue Miss", "-$22M")
        c2.metric("Price Effect", "+$6M",  delta="Price held firm — positive")
        c3.metric("Volume Effect", "-$24M", delta="Volume shortfall — key driver")
        c4.metric("Mix Effect", "-$4M",    delta="Mix shift to lower-margin SKUs")
        st.info("📌 Revenue miss is 100% volume-driven — price realisation was actually +$6M ahead of plan.")

        st.markdown("**Step 4 — Volume Miss by Region**")
        regions  = ["North America", "Europe", "Asia Pacific", "Latin America", "MEA"]
        var_reg  = [3, -12, -9, -2, -2]
        fig2 = go.Figure(go.Bar(
            x=regions, y=var_reg,
            marker_color=["#1D9E75" if v >= 0 else "#E24B4A" for v in var_reg],
            text=[f"${v:+}M" for v in var_reg], textposition="outside"
        ))
        fig2.add_hline(y=0, line_color="black", line_width=1)
        fig2.update_layout(title="Revenue Variance vs. Budget by Region ($M)",
                           template="plotly_white", height=360, yaxis=dict(range=[-18, 10]))
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Step 5 — COGS Anomaly Detection (Z-Score)**")
        np.random.seed(7)
        unit_costs = np.random.normal(44, 3.5, 80)
        unit_costs[18] = 82; unit_costs[53] = 78
        z_scores = (unit_costs - unit_costs.mean()) / unit_costs.std()
        flagged  = np.abs(z_scores) > 2.5
        anomaly_df = pd.DataFrame({
            "Transaction #": range(1, 81),
            "Unit Cost ($)": unit_costs.round(1),
            "Z-Score":       z_scores.round(2),
            "Flag": ["⚠️ Anomaly" if f else "✅ Normal" for f in flagged]
        })
        st.dataframe(anomaly_df[anomaly_df["Flag"] == "⚠️ Anomaly"][["Transaction #","Unit Cost ($)","Z-Score","Flag"]],
                     use_container_width=True, hide_index=True)
        st.warning("2 anomalous unit-cost transactions identified — both traceable to emergency spot-market raw material purchases in April 2024 due to supplier strike in Vietnam.")

        st.success("""
**Root Cause Summary — $38M EBITDA Miss (Q2 2024)**

| Driver | Impact | Root Cause |
|--------|--------|------------|
| Volume Miss | -$24M | Europe: 2 large retailers deferred orders. Asia Pacific: lost tender to local competitor. |
| COGS Inflation | -$16M | Raw material cost +9% above budget. 2 spot purchases at 86% premium. |
| SG&A Over-run | -$8M | Digital marketing spend brought forward from Q3; 12 new hires ahead of revenue. |
| R&D Under-spend | +$8M | Product Phoenix Phase 2 delayed — shifts to Q3. |

**Recommended Actions:**
1. Re-engage European retail accounts — CFO-approved retention discount up to 8%.
2. Activate secondary supplier in Malaysia to avoid future spot-market purchases.
3. Freeze discretionary SG&A for Q3; review headcount ramp vs. revenue plan.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 3 Quiz", "❓")
        _quiz("1. Revenue variance = −$30M. Volume effect = −$35M, Mix effect = +$5M. Price effect is:",
              ["−$60M", "+$30M", "$0M", "−$5M"], "$0M", "fa_m3q1")
        st.divider()
        _quiz("2. Fixed costs = $200K, selling price = $80, variable cost = $50. Break-even (units)?",
              ["2,500", "4,000", "6,667", "2,000"], "6,667", "fa_m3q2")
        st.divider()
        _quiz("3. Activity-Based Costing (ABC) is most valuable when:",
              ["A company has only one product",
               "Overhead is small relative to direct costs",
               "Products have very different consumption of shared overhead activities",
               "All products use resources in the same proportion"],
              "Products have very different consumption of shared overhead activities", "fa_m3q3")
        st.divider()
        _quiz("4. Operating leverage of 8× means a 5% revenue drop causes profit to fall by approximately:",
              ["5%", "1.6%", "40%", "8%"], "40%", "fa_m3q4")
        st.divider()
        _quiz("5. In standard costing, a favourable material usage variance means:",
              ["Actual material price was below standard",
               "Fewer materials were used than standard specified",
               "More materials were used than standard",
               "Output volume exceeded budget"],
              "Fewer materials were used than standard specified", "fa_m3q5")
        st.divider()
        _quiz("6. The Margin of Safety represents:",
              ["The difference between actual revenue and break-even revenue",
               "The gap between gross margin and EBITDA margin",
               "The maximum allowable cost increase",
               "Fixed costs as a % of revenue"],
              "The difference between actual revenue and break-even revenue", "fa_m3q6")