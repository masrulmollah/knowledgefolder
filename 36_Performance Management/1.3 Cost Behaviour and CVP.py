"""
Performance Management — Applied Learning Series
Module 1.3 · Cost Behaviour & Cost-Volume-Profit (CVP)
------------------------------------------------------------
An interactive study of how costs behave with activity and how
Cost-Volume-Profit analysis drives break-even, contribution and
target-profit decisions.

Run with:  streamlit run 1.3_Cost_Behaviour_and_CVP.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="1.3 · Cost Behaviour & CVP",
    page_icon="📈",
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
st.markdown('<p class="pill">MODULE 1 · COSTING FOUNDATIONS FOR PERFORMANCE</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">1.3 · Cost Behaviour & Cost-Volume-Profit (CVP)</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand how <b>fixed, variable and semi-variable</b> costs '
    'behave with activity, and use <b>CVP analysis</b> to find break-even, contribution margin, '
    'target-profit volume and margin of safety.</p>',
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
**Cost behaviour** describes how a cost changes as activity (volume) changes:

- **Fixed costs** — stay constant in total regardless of volume (e.g. factory rent,
  supervisor salaries). *Per unit*, they **fall** as volume rises.
- **Variable costs** — change in direct proportion to volume (e.g. raw material,
  direct labour per unit). *Per unit*, they stay **constant**.
- **Semi-variable (mixed) costs** — contain both a fixed and a variable element
  (e.g. electricity: a standing charge plus a usage charge). These are commonly split
  using the **high-low method**.

**Cost-Volume-Profit (CVP) analysis** builds on this to answer the questions every
finance manager faces:

- How many units must we sell to **break even**?
- How much does each unit contribute toward fixed costs and profit — the
  **contribution margin**?
- What volume achieves a **target profit**?
- How much can sales fall before we make a loss — the **margin of safety**?

Core relationships:

- **Contribution per unit** = Selling price − Variable cost per unit
- **Break-even (units)** = Fixed costs ÷ Contribution per unit
- **Target-profit (units)** = (Fixed costs + Target profit) ÷ Contribution per unit
- **Margin of safety** = (Actual − Break-even) ÷ Actual
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "CVP is the fastest lens for pricing, volume and cost decisions. Before any "
        "budget or investment case, it tells you the minimum activity to stay viable and "
        "how sensitive profit is to a swing in volume — essential for factory and "
        "commercial planning.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — CVP Simulator
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The CVP Simulator</p>',
            unsafe_allow_html=True)
st.caption("Set your price and cost structure, then watch break-even, contribution and profit respond live.")

left, right = st.columns([1, 1.5])

with left:
    st.markdown("#### 🎛️ Inputs")
    selling_price = st.number_input("Selling price per unit (BDT)", 1.0, 10000.0, 100.0, step=5.0)
    var_cost      = st.number_input("Variable cost per unit (BDT)", 0.0, 10000.0, 60.0, step=5.0)
    fixed_cost    = st.number_input("Total fixed costs (BDT)", 0.0, 100_000_000.0, 300_000.0, step=10_000.0)
    target_profit = st.number_input("Target profit (BDT)", 0.0, 100_000_000.0, 150_000.0, step=10_000.0)
    actual_units  = st.number_input("Expected / actual sales (units)", 0, 1_000_000, 12000, step=500)

# ---- Calculations ----
contribution = selling_price - var_cost
cm_ratio = (contribution / selling_price) if selling_price else 0

if contribution > 0:
    be_units = fixed_cost / contribution
    be_revenue = be_units * selling_price
    tp_units = (fixed_cost + target_profit) / contribution
else:
    be_units = tp_units = be_revenue = float("inf")

profit_at_actual = actual_units * contribution - fixed_cost
mos_units = actual_units - be_units if np.isfinite(be_units) else float("nan")
mos_pct = (mos_units / actual_units * 100) if actual_units and np.isfinite(be_units) else float("nan")

with right:
    st.markdown("#### 📊 Results")
    m1, m2, m3 = st.columns(3)
    m1.metric("Contribution / unit", f"{contribution:,.1f} BDT", f"CM ratio {cm_ratio*100:.1f}%")
    m2.metric("Break-even", f"{be_units:,.0f} u" if np.isfinite(be_units) else "—",
              f"{be_revenue:,.0f} BDT" if np.isfinite(be_revenue) else "n/a")
    m3.metric("Profit at expected sales", f"{profit_at_actual:,.0f} BDT",
              f"{'profit' if profit_at_actual>=0 else 'loss'}",
              delta_color="normal" if profit_at_actual >= 0 else "inverse")

    m4, m5 = st.columns(2)
    m4.metric("Units for target profit", f"{tp_units:,.0f} u" if np.isfinite(tp_units) else "—")
    m5.metric("Margin of safety", f"{mos_pct:,.1f}%" if np.isfinite(mos_pct) else "—",
              f"{mos_units:,.0f} u" if np.isfinite(mos_units) else "n/a",
              delta_color="normal" if (np.isfinite(mos_pct) and mos_pct >= 0) else "inverse")

# ---- Break-even chart ----
st.markdown("#### 📉 Break-Even Chart")
max_units = int(max(actual_units, be_units if np.isfinite(be_units) else actual_units, 1) * 1.6) + 1
x = np.linspace(0, max_units, 100)
total_cost_line = fixed_cost + var_cost * x
revenue_line = selling_price * x
fixed_line = np.full_like(x, fixed_cost)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=revenue_line, name="Total revenue",
                         line=dict(color="#2e86de", width=3)))
fig.add_trace(go.Scatter(x=x, y=total_cost_line, name="Total cost",
                         line=dict(color="#e67e22", width=3)))
fig.add_trace(go.Scatter(x=x, y=fixed_line, name="Fixed cost",
                         line=dict(color="#95a5a6", width=1.5, dash="dash")))

if np.isfinite(be_units) and be_units <= max_units:
    fig.add_trace(go.Scatter(x=[be_units], y=[be_revenue], mode="markers+text",
                             name="Break-even", text=["BEP"], textposition="top center",
                             marker=dict(color="#c0392b", size=12, symbol="x")))
    fig.add_vline(x=be_units, line=dict(color="#c0392b", width=1, dash="dot"))

# shade profit / loss zones lightly via markers of actual point
fig.add_trace(go.Scatter(x=[actual_units], y=[selling_price*actual_units],
                         mode="markers+text", name="Expected sales",
                         text=["Expected"], textposition="bottom center",
                         marker=dict(color="#1e8449", size=11, symbol="circle")))

fig.update_layout(height=430, margin=dict(t=30, b=10),
                  xaxis_title="Units", yaxis_title="BDT",
                  legend=dict(orientation="h", y=1.12),
                  plot_bgcolor="white")
st.plotly_chart(fig, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic commentary
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

if contribution <= 0:
    st.error(
        "**Contribution is zero or negative.** Each unit sold fails to cover its own "
        "variable cost, so there is *no* break-even point — the business loses more the "
        "more it sells. Raise the selling price or cut variable cost before anything else.",
        icon="🔴",
    )
else:
    st.markdown(
        f"""
- 🟢 **Contribution:** each unit contributes **{contribution:,.1f} BDT** ({cm_ratio*100:.1f}% of price) toward fixed costs and profit.
- 🎯 **Break-even:** you must sell **{be_units:,.0f} units** ({be_revenue:,.0f} BDT of revenue) just to avoid a loss.
- 💰 **Target profit:** reaching **{target_profit:,.0f} BDT** profit requires **{tp_units:,.0f} units**.
- 📈 **At expected sales of {actual_units:,.0f} units**, profit is **{profit_at_actual:,.0f} BDT**.
        """
    )

    if np.isfinite(mos_pct):
        if mos_pct >= 25:
            st.success(
                f"**Margin of safety = {mos_pct:.1f}%.** Expected sales sit comfortably "
                f"**{mos_units:,.0f} units above** break-even. The plan is resilient — sales could "
                f"fall materially before a loss occurs.",
                icon="✅",
            )
        elif mos_pct >= 0:
            st.warning(
                f"**Margin of safety = {mos_pct:.1f}%.** Expected sales are only "
                f"**{mos_units:,.0f} units above** break-even. Profit is fragile — a small "
                f"volume shortfall could wipe it out. Consider a price rise, cost reduction, "
                f"or demand cushion.",
                icon="⚠️",
            )
        else:
            st.error(
                f"**Below break-even.** Expected sales are **{abs(mos_units):,.0f} units short** "
                f"of break-even, producing a loss of **{abs(profit_at_actual):,.0f} BDT**. "
                f"Increase volume, lift price, or cut fixed/variable costs to restore viability.",
                icon="🔴",
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
        - [ ] Separate every cost into **fixed**, **variable** or **semi-variable**.
        - [ ] Contribution — not gross profit — drives short-term CVP decisions.
        - [ ] **Break-even = Fixed ÷ Contribution per unit.** Memorise it.
        - [ ] A high **CM ratio** means profit is very sensitive to volume (operating gearing).
        - [ ] Always check the **margin of safety** before committing to a plan.
        """
    )
with a2:
    with st.expander("📘 Key terms & formulas in this module"):
        st.markdown(
            """
            - **Fixed cost** — constant in total, falls per unit as volume rises.
            - **Variable cost** — constant per unit, rises in total with volume.
            - **Semi-variable cost** — mix of both; split via the high-low method.
            - **Contribution/unit** = Price − Variable cost.
            - **CM ratio** = Contribution ÷ Selling price.
            - **Break-even units** = Fixed cost ÷ Contribution per unit.
            - **Target-profit units** = (Fixed + Target profit) ÷ Contribution per unit.
            - **Margin of safety** = (Actual − Break-even) ÷ Actual.
            """
        )

    with st.expander("🧮 High-low method (splitting a mixed cost)"):
        st.markdown(
            """
            Given the highest and lowest activity observations:

            **Variable cost/unit** = (Cost at high − Cost at low) ÷ (Units high − Units low)

            **Fixed cost** = Total cost at high − (Variable cost/unit × Units high)
            """
        )

# Downloadable template
template = pd.DataFrame({
    "Metric": ["Selling price/unit", "Variable cost/unit", "Contribution/unit",
               "CM ratio (%)", "Fixed costs", "Break-even units", "Break-even revenue",
               "Target profit", "Units for target profit", "Expected units",
               "Profit at expected", "Margin of safety (units)", "Margin of safety (%)"],
    "Value": [selling_price, var_cost, contribution, round(cm_ratio*100, 1), fixed_cost,
              round(be_units, 0) if np.isfinite(be_units) else "n/a",
              round(be_revenue, 0) if np.isfinite(be_revenue) else "n/a",
              target_profit,
              round(tp_units, 0) if np.isfinite(tp_units) else "n/a",
              actual_units, round(profit_at_actual, 0),
              round(mos_units, 0) if np.isfinite(mos_units) else "n/a",
              round(mos_pct, 1) if np.isfinite(mos_pct) else "n/a"],
})
st.download_button(
    "⬇️ Download this CVP analysis as a CSV template",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="cvp_analysis_template.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 1.2 · Activity-Based Costing", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 2.1 · Budget Preparation ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 1.3")
