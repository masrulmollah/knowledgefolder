"""
Performance Management — Applied Learning Series
Module 4.3 · Ratio Analysis for Performance
------------------------------------------------------------
A full performance-ratio dashboard across the four families:
  • Profitability   (ROCE, margins, ROI link)
  • Efficiency      (asset turnover, working-capital days)
  • Liquidity       (current, quick)
  • Gearing         (gearing %, interest cover)
Enter one set of statement figures; the engine computes and
interprets every ratio and shows the ROCE pyramid.

Run with:  streamlit run 4.3_Ratio_Analysis_for_Performance.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="4.3 · Ratio Analysis for Performance",
    page_icon="📐",
    layout="wide",
)

# ------------------------------------------------------------------
# LIGHT THEME / STYLING (consistent with the site)
# ------------------------------------------------------------------
st.markdown(
    """
    <style>
        .big-title   {font-size:2.1rem; font-weight:800; color:#1f3b57; margin-bottom:0;}
        .subtle      {color:#5c6b7a; font-size:1.02rem;}
        .zone-header {font-size:1.35rem; font-weight:700; color:#1f3b57;
                      border-left:5px solid #2e86de; padding-left:10px; margin-top:8px;}
        .pill        {display:inline-block; padding:4px 12px; border-radius:14px;
                      background:#eaf2fb; color:#2e86de; font-weight:600; font-size:0.8rem;}
        .good        {color:#1e8449; font-weight:700;}
        .bad         {color:#c0392b; font-weight:700;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# ① HEADER ZONE
# ------------------------------------------------------------------
st.markdown('<p class="pill">MODULE 4 · PERFORMANCE MEASUREMENT — FINANCIAL</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">4.3 · Ratio Analysis for Performance</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: assess performance across the four ratio families — '
    '<b>profitability, efficiency, liquidity and gearing</b> — from one set of financial statements, '
    'and link them together through the <b>ROCE pyramid</b>.</p>',
    unsafe_allow_html=True,
)
st.divider()

# ------------------------------------------------------------------
# ② CONCEPT ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">② The Concept</p>', unsafe_allow_html=True)

c1, c2 = st.columns([1.35, 1])
with c1:
    st.markdown(
        """
**Ratio analysis** interprets financial statements by relating figures to one another,
turning raw numbers into a performance story. Ratios matter most when **compared** — over
time (trend), against **budget**, or against **competitors/industry**.

The ratios group into four families:

- **Profitability** — how well the business generates profit from sales and capital:
  **ROCE**, gross/operating/net margins. *ROCE = Operating profit ÷ Capital employed* is the
  primary measure and links straight to ROI from Module 4.1.
- **Efficiency (activity)** — how hard the assets and working capital work:
  **asset turnover**, **inventory days**, **receivables days**, **payables days**, and the
  resulting **cash cycle**.
- **Liquidity** — the ability to meet short-term obligations:
  **current ratio** and **quick (acid-test) ratio**.
- **Gearing (solvency)** — reliance on debt and the ability to service it:
  **gearing %** and **interest cover**.

**The ROCE pyramid** ties it together:

- **ROCE = Operating margin × Asset turnover**
  = (Operating profit ÷ Sales) × (Sales ÷ Capital employed)

This DuPont-style split shows whether returns are driven by **margins** (pricing/cost) or
by **asset utilisation** (volume/efficiency) — the diagnostic backbone of performance review.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Ratios are the common language of performance review. A single ratio says little; the "
        "skill is reading them **together and in context** — a high margin with poor asset turnover "
        "tells a very different story from the reverse. This is how finance turns statements into "
        "management action.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Ratio Dashboard
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Ratio Dashboard</p>', unsafe_allow_html=True)
st.caption("Enter the key financial-statement figures once; every ratio computes and interprets live.")

with st.expander("🎛️ Enter financial statement figures", expanded=True):
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown("**Income statement**")
        revenue   = st.number_input("Revenue (BDT)", 0, 100_000_000_000, 10_000_000, step=100_000)
        cogs      = st.number_input("Cost of sales (BDT)", 0, 100_000_000_000, 6_500_000, step=100_000)
        op_profit = st.number_input("Operating profit (PBIT) (BDT)", -1_000_000_000, 1_000_000_000, 1_500_000, step=50_000)
        interest  = st.number_input("Interest expense (BDT)", 0, 1_000_000_000, 300_000, step=10_000)
    with g2:
        st.markdown("**Balance sheet — assets**")
        inventory   = st.number_input("Inventory (BDT)", 0, 100_000_000_000, 1_300_000, step=50_000)
        receivables = st.number_input("Trade receivables (BDT)", 0, 100_000_000_000, 1_600_000, step=50_000)
        cash        = st.number_input("Cash (BDT)", 0, 100_000_000_000, 400_000, step=50_000)
        cur_assets  = st.number_input("Total current assets (BDT)", 0, 100_000_000_000, 3_300_000, step=50_000)
    with g3:
        st.markdown("**Balance sheet — liabilities & capital**")
        payables    = st.number_input("Trade payables (BDT)", 0, 100_000_000_000, 1_100_000, step=50_000)
        cur_liab    = st.number_input("Total current liabilities (BDT)", 0, 100_000_000_000, 1_800_000, step=50_000)
        debt        = st.number_input("Long-term debt (BDT)", 0, 100_000_000_000, 3_000_000, step=100_000)
        equity      = st.number_input("Equity (BDT)", 1, 100_000_000_000, 5_000_000, step=100_000)

# ---- Derived figures ----
gross_profit   = revenue - cogs
capital_emp    = equity + debt
net_profit     = op_profit - interest

# Profitability
roce          = op_profit / capital_emp * 100 if capital_emp else 0
gross_margin  = gross_profit / revenue * 100 if revenue else 0
op_margin     = op_profit / revenue * 100 if revenue else 0
net_margin    = net_profit / revenue * 100 if revenue else 0
asset_turn    = revenue / capital_emp if capital_emp else 0

# Efficiency (working capital days)
inv_days = inventory / cogs * 365 if cogs else 0
rec_days = receivables / revenue * 365 if revenue else 0
pay_days = payables / cogs * 365 if cogs else 0
cash_cycle = inv_days + rec_days - pay_days

# Liquidity
current_ratio = cur_assets / cur_liab if cur_liab else 0
quick_ratio   = (cur_assets - inventory) / cur_liab if cur_liab else 0

# Gearing
gearing = debt / (debt + equity) * 100 if (debt + equity) else 0
int_cover = op_profit / interest if interest else float("inf")

# ---- Display: four families ----
st.markdown("#### 📊 Performance Ratios by Family")
f1, f2 = st.columns(2)

with f1:
    st.markdown("**🟣 Profitability**")
    p1, p2, p3 = st.columns(3)
    p1.metric("ROCE", f"{roce:.1f}%")
    p2.metric("Operating margin", f"{op_margin:.1f}%")
    p3.metric("Asset turnover", f"{asset_turn:.2f}×")
    p4, p5, p6 = st.columns(3)
    p4.metric("Gross margin", f"{gross_margin:.1f}%")
    p5.metric("Net margin", f"{net_margin:.1f}%")
    p6.metric("Capital employed", f"{capital_emp:,.0f}")

    st.markdown("**🟢 Liquidity**")
    l1, l2 = st.columns(2)
    l1.metric("Current ratio", f"{current_ratio:.2f}",
              "healthy" if current_ratio >= 1.5 else "watch",
              delta_color="normal" if current_ratio >= 1.5 else "inverse")
    l2.metric("Quick ratio", f"{quick_ratio:.2f}",
              "healthy" if quick_ratio >= 1.0 else "watch",
              delta_color="normal" if quick_ratio >= 1.0 else "inverse")

with f2:
    st.markdown("**🟠 Efficiency (working capital)**")
    e1, e2, e3 = st.columns(3)
    e1.metric("Inventory days", f"{inv_days:.0f}")
    e2.metric("Receivable days", f"{rec_days:.0f}")
    e3.metric("Payable days", f"{pay_days:.0f}")
    st.metric("Cash operating cycle", f"{cash_cycle:.0f} days",
              "shorter is better", delta_color="off")

    st.markdown("**🔴 Gearing (solvency)**")
    gg1, gg2 = st.columns(2)
    gg1.metric("Gearing", f"{gearing:.1f}%",
               "high" if gearing >= 50 else "moderate",
               delta_color="inverse" if gearing >= 50 else "normal")
    gg2.metric("Interest cover", f"{int_cover:.1f}×" if np.isfinite(int_cover) else "∞",
               "safe" if (np.isfinite(int_cover) and int_cover >= 3) else "risky",
               delta_color="normal" if (np.isfinite(int_cover) and int_cover >= 3) else "inverse")

st.divider()

# ---- ROCE pyramid ----
st.markdown("#### 🔺 The ROCE Pyramid (DuPont link to Module 4.1)")
pyr = go.Figure(go.Bar(
    x=["Operating margin (%)", "Asset turnover (×)", "= ROCE (%)"],
    y=[op_margin, asset_turn, roce],
    marker_color=["#8e44ad", "#16a085", "#2e86de"],
    text=[f"{op_margin:.1f}%", f"{asset_turn:.2f}×", f"{roce:.1f}%"],
    textposition="outside",
))
pyr.update_layout(height=300, margin=dict(t=30, b=10), plot_bgcolor="white",
                  title="ROCE = Operating margin × Asset turnover")
st.plotly_chart(pyr, use_container_width=True)

# Cash cycle visual
st.markdown("#### 💧 Cash Operating Cycle")
cyc = go.Figure(go.Waterfall(
    orientation="v",
    measure=["relative", "relative", "relative", "total"],
    x=["Inventory days", "Receivable days", "Less payable days", "Cash cycle"],
    y=[inv_days, rec_days, -pay_days, cash_cycle],
    text=[f"{inv_days:.0f}", f"{rec_days:.0f}", f"{-pay_days:.0f}", f"{cash_cycle:.0f}"],
    textposition="outside",
    connector={"line": {"color": "#b0b7bf"}},
    increasing={"marker": {"color": "#e67e22"}},
    decreasing={"marker": {"color": "#1e8449"}},
    totals={"marker": {"color": "#2e86de"}},
))
cyc.update_layout(height=300, margin=dict(t=30, b=10), yaxis_title="Days", plot_bgcolor="white")
st.plotly_chart(cyc, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

# Profitability driver
if asset_turn > 0 and op_margin > 0:
    if op_margin >= 15 and asset_turn < 1:
        driver = ("a **high-margin, low-turnover** model — returns come from pricing/product, "
                  "not asset intensity (typical of premium or capital-heavy operations).")
    elif op_margin < 10 and asset_turn >= 1.5:
        driver = ("a **low-margin, high-turnover** model — returns come from **volume and asset "
                  "efficiency** rather than margin (typical of fast-moving, competitive markets).")
    else:
        driver = "a **balanced** mix of margin and asset utilisation."
else:
    driver = "an unusual profile — check the inputs."

st.markdown(
    f"""
- 🟣 **Profitability:** ROCE of **{roce:.1f}%** is built from an operating margin of **{op_margin:.1f}%**
  and asset turnover of **{asset_turn:.2f}×** — {driver}
- 🟠 **Efficiency:** the cash operating cycle is **{cash_cycle:.0f} days**
  (inventory {inv_days:.0f} + receivables {rec_days:.0f} − payables {pay_days:.0f}). The longer it is,
  the more working capital is tied up.
- 🟢 **Liquidity:** current ratio **{current_ratio:.2f}** / quick ratio **{quick_ratio:.2f}** —
  {"comfortable short-term cover." if quick_ratio >= 1 else "thin cover once inventory is excluded — monitor closely."}
- 🔴 **Gearing:** **{gearing:.1f}%** geared with interest cover of
  **{(f'{int_cover:.1f}×' if np.isfinite(int_cover) else '∞')}** —
  {"a prudent structure." if (np.isfinite(int_cover) and int_cover >= 3 and gearing < 50) else "elevated financial risk; watch debt-servicing capacity."}
    """
)

st.info(
    "📌 **Golden rule:** a ratio in isolation means little. Always compare against **prior periods, "
    "budget, or industry benchmarks**, and read the four families **together** — they tell one "
    "connected story about performance.",
    icon="📌",
)

st.divider()

# ------------------------------------------------------------------
# ⑤ APPLY IT ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">⑤ Apply It</p>', unsafe_allow_html=True)

a1, a2 = st.columns([1, 1])
with a1:
    st.markdown("**Takeaway checklist**")
    st.markdown(
        """
        - [ ] Group ratios into **profitability, efficiency, liquidity, gearing**.
        - [ ] **ROCE = Operating margin × Asset turnover** — always decompose it.
        - [ ] Read the **cash cycle**: inventory + receivable − payable days.
        - [ ] Ratios mean nothing alone — compare to **trend, budget, industry**.
        - [ ] Interpret the four families **together**, not in isolation.
        """
    )
with a2:
    with st.expander("📘 Key formulas in this module"):
        st.markdown(
            """
            **Profitability**
            - ROCE = Operating profit ÷ Capital employed
            - Margins = Gross/Operating/Net profit ÷ Revenue
            - Asset turnover = Revenue ÷ Capital employed

            **Efficiency**
            - Inventory days = Inventory ÷ COGS × 365
            - Receivable days = Receivables ÷ Revenue × 365
            - Payable days = Payables ÷ COGS × 365

            **Liquidity**
            - Current = Current assets ÷ Current liabilities
            - Quick = (Current assets − Inventory) ÷ Current liabilities

            **Gearing**
            - Gearing = Debt ÷ (Debt + Equity)
            - Interest cover = Operating profit ÷ Interest
            """
        )
    with st.expander("🧭 Rules of thumb (context-dependent!)"):
        st.markdown(
            """
            - Current ratio ≈ **1.5–2.0**, quick ratio ≈ **1.0** are often seen as comfortable.
            - Interest cover **> 3×** is usually considered safe.
            - Gearing **> 50%** signals higher financial risk.

            These are **guides, not rules** — always judge against the industry and the trend.
            """
        )

# Downloadable summary
template = pd.DataFrame({
    "Ratio": ["ROCE (%)", "Gross margin (%)", "Operating margin (%)", "Net margin (%)",
              "Asset turnover (x)", "Inventory days", "Receivable days", "Payable days",
              "Cash cycle (days)", "Current ratio", "Quick ratio",
              "Gearing (%)", "Interest cover (x)"],
    "Value": [round(roce, 1), round(gross_margin, 1), round(op_margin, 1), round(net_margin, 1),
              round(asset_turn, 2), round(inv_days, 0), round(rec_days, 0), round(pay_days, 0),
              round(cash_cycle, 0), round(current_ratio, 2), round(quick_ratio, 2),
              round(gearing, 1), round(int_cover, 1) if np.isfinite(int_cover) else "inf"],
})
st.download_button(
    "⬇️ Download the ratio dashboard (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="ratio_analysis_performance.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 4.2 · Economic Value Added (EVA)", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 4.4 · Transfer Pricing ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 4.3")
