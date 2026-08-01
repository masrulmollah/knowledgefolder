"""
Performance Management — Applied Learning Series
Module 1.1 · Absorption vs. Marginal Costing
------------------------------------------------------------
See why absorption and marginal costing report DIFFERENT profits
when production ≠ sales, and how to reconcile the two — driven by
the fixed overhead carried in (or released from) inventory.

Run with:  streamlit run 1.1_Absorption_vs_Marginal_Costing.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="1.1 · Absorption vs. Marginal Costing",
    page_icon="📦",
    layout="wide",
)

# ------------------------------------------------------------------
# STYLING (consistent with the site)
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
        .card        {border:1px solid #e3e8ee; border-radius:12px; padding:14px 16px;
                      background:#fafcff;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# ① HEADER ZONE
# ------------------------------------------------------------------
st.markdown('<p class="pill">MODULE 1 · COSTING FOUNDATIONS</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">1.1 · Absorption vs. Marginal Costing</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand how <b>marginal</b> and <b>absorption</b> costing treat '
    'fixed production overhead differently, why they report <b>different profits</b> when inventory '
    'changes, and how to <b>reconcile</b> the two.</p>',
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
The two methods differ on **one question: how is fixed production overhead treated?**

- **Marginal (variable) costing** — only *variable* production costs attach to the product.
  Fixed overhead is a **period cost**, expensed in full each period. Profit is driven by **sales**.
- **Absorption costing** — each unit absorbs a share of fixed overhead too (via an
  overhead absorption rate, OAR). Fixed overhead sits **in inventory** until the unit is sold.

**The consequence — profit differs whenever production ≠ sales:**

| Situation | Inventory | Absorption vs. Marginal profit |
|-----------|-----------|-------------------------------|
| Production **>** Sales | Rising | Absorption **higher** (fixed OH deferred in stock) |
| Production **<** Sales | Falling | Absorption **lower** (fixed OH released from stock) |
| Production **=** Sales | Flat | **Equal** |

**The reconciling bridge:**

> Difference in profit = **Change in inventory units × Fixed OH per unit**
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Absorption is required for **external reporting** (IAS 2). Marginal is superior for "
        "**decision-making** (it isolates contribution). Knowing the bridge stops you being "
        "fooled by a profit that rose only because stock was built up.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — Profit Statement & Reconciliation</p>',
            unsafe_allow_html=True)
st.caption("Set production, sales and cost inputs. Watch both profit statements build side by side "
           "and reconcile automatically.")

left, right = st.columns([1, 1.55])

with left:
    st.markdown("#### 🎛️ Inputs")
    price       = st.number_input("Selling price / unit (BDT)", 1.0, 5000.0, 100.0, step=5.0)
    var_prod    = st.number_input("Variable production cost / unit (BDT)", 0.0, 5000.0, 45.0, step=1.0)
    var_sell    = st.number_input("Variable selling cost / unit (BDT)", 0.0, 5000.0, 5.0, step=1.0)
    fixed_prod  = st.number_input("Total fixed production overhead (BDT)", 0, 10_000_000, 300000, step=10000)
    fixed_sell  = st.number_input("Total fixed selling & admin (BDT)", 0, 10_000_000, 80000, step=10000)

    st.markdown("**Volumes**")
    production  = st.number_input("Units produced", 0, 1_000_000, 10000, step=500)
    sales       = st.number_input("Units sold", 0, 1_000_000, 9000, step=500)

    st.markdown("**Fixed OH absorption basis**")
    oar_basis = st.radio("Absorb fixed OH using:", ["Actual production", "Normal/budgeted volume"],
                         horizontal=False)
    if oar_basis == "Normal/budgeted volume":
        normal_vol = st.number_input("Normal/budgeted volume (units)", 1, 1_000_000, 10000, step=500)
    else:
        normal_vol = production if production > 0 else 1

# ---- Guard rails ----
sales = min(sales, production + 0)  # can't sell more than available if no opening stock
closing_inv = production - sales
if closing_inv < 0:
    closing_inv = 0

# ---- Overhead absorption rate ----
oar = fixed_prod / normal_vol if normal_vol else 0        # fixed OH per unit
absorbed = oar * production
under_over = absorbed - fixed_prod                         # +over absorbed / -under absorbed

# ---- MARGINAL COSTING P&L ----
revenue          = price * sales
var_cogs         = var_prod * sales
contribution_prod = revenue - var_cogs
var_selling_total = var_sell * sales
contribution      = contribution_prod - var_selling_total
marginal_profit   = contribution - fixed_prod - fixed_sell

# ---- ABSORPTION COSTING P&L ----
prod_cost_per_unit = var_prod + oar
abs_cogs           = prod_cost_per_unit * sales
gross_profit_abs   = revenue - abs_cogs + under_over       # adjust for under/over absorption
abs_profit         = gross_profit_abs - var_selling_total - fixed_sell

# ---- Reconciliation ----
inv_change_units = closing_inv                             # no opening stock assumed
fixed_oh_in_stock = inv_change_units * oar
recon_check = marginal_profit + fixed_oh_in_stock          # should equal abs_profit (when producing>selling)

with right:
    st.markdown("#### 📊 Two profit statements")
    colM, colA = st.columns(2)

    with colM:
        st.markdown("**Marginal costing**")
        mdf = pd.DataFrame({
            "Line": ["Revenue", "Less: variable COGS", "Less: variable selling",
                     "= Contribution", "Less: fixed production OH",
                     "Less: fixed selling & admin", "= Profit"],
            "BDT": [revenue, -var_cogs, -var_selling_total, contribution,
                    -fixed_prod, -fixed_sell, marginal_profit],
        })
        st.dataframe(mdf, hide_index=True, use_container_width=True)

    with colA:
        st.markdown("**Absorption costing**")
        adf = pd.DataFrame({
            "Line": ["Revenue", "Less: absorption COGS", "(Under)/over absorption",
                     "= Gross profit", "Less: variable selling",
                     "Less: fixed selling & admin", "= Profit"],
            "BDT": [revenue, -abs_cogs, under_over, gross_profit_abs,
                    -var_selling_total, -fixed_sell, abs_profit],
        })
        st.dataframe(adf, hide_index=True, use_container_width=True)

    # Profit comparison bar
    fig = go.Figure()
    fig.add_bar(x=["Marginal", "Absorption"], y=[marginal_profit, abs_profit],
                marker_color=["#16a085", "#2e86de"],
                text=[f"{marginal_profit:,.0f}", f"{abs_profit:,.0f}"],
                textposition="outside")
    fig.update_layout(height=280, margin=dict(t=30, b=10),
                      title="Reported profit by method", yaxis_title="BDT")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — reconciliation + commentary
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation & Reconciliation</p>', unsafe_allow_html=True)

diff = abs_profit - marginal_profit

r1, r2 = st.columns([1.1, 1])
with r1:
    st.markdown("**🔗 Profit reconciliation bridge**")
    bridge = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "total"],
        x=["Marginal profit", "Fixed OH in Δ inventory", "Absorption profit"],
        y=[marginal_profit, diff, None],
        connector={"line": {"color": "#b2bec3"}},
        decreasing={"marker": {"color": "#e67e22"}},
        increasing={"marker": {"color": "#2e86de"}},
        totals={"marker": {"color": "#8e44ad"}},
    ))
    bridge.update_layout(height=300, margin=dict(t=20, b=10))
    st.plotly_chart(bridge, use_container_width=True)

with r2:
    st.metric("Closing inventory", f"{closing_inv:,} u")
    st.metric("Fixed OH / unit (OAR)", f"{oar:,.2f}")
    st.metric("Profit difference (Abs − Marg)", f"{diff:+,.0f}")
    if abs(under_over) > 0.5:
        tag = "over-absorbed" if under_over > 0 else "under-absorbed"
        st.metric("(Under)/over absorption", f"{under_over:+,.0f}", tag)

if closing_inv > 0 and production > sales:
    st.info(
        f"**Production ({production:,}) > Sales ({sales:,})** → inventory rose by **{closing_inv:,} units**. "
        f"Absorption costing defers **{fixed_oh_in_stock:,.0f} BDT** of fixed overhead *inside* that stock, "
        f"so absorption profit is **higher by {diff:,.0f}**. The bridge = {closing_inv:,} u × {oar:,.2f} = {fixed_oh_in_stock:,.0f}.",
        icon="📈",
    )
elif production < sales:
    st.warning(
        f"**Production ({production:,}) < Sales ({sales:,})** → inventory fell. Absorption costing "
        f"releases previously-deferred fixed overhead into cost of sales, so absorption profit is "
        f"**lower by {abs(diff):,.0f}**. Beware: a falling profit here may just be stock run-down, not poor trading.",
        icon="📉",
    )
else:
    st.success(
        "**Production = Sales** → no change in inventory, so both methods report the **same profit**. "
        "This is the only case where the choice of method is profit-neutral.",
        icon="✅",
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
        - [ ] The **only** conceptual difference is the treatment of **fixed production OH**.
        - [ ] Profit differs **only** when production ≠ sales (inventory changes).
        - [ ] Bridge = **Δ inventory units × fixed OH per unit**.
        - [ ] Use **absorption** for external reporting (IAS 2); **marginal** for decisions.
        - [ ] Watch for profit inflated by **building stock** under absorption costing.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Marginal cost** — the variable cost of one more unit.
            - **Contribution** — sales less all variable costs.
            - **OAR** — overhead absorption rate = fixed OH ÷ activity level.
            - **Under/over absorption** — actual OH ≠ absorbed OH (when using a normal rate).
            - **Period cost** — expensed in full in the period (fixed OH under marginal).
            - **Product cost** — attached to units and carried in inventory.
            """
        )

# Downloadable template
summary = pd.DataFrame({
    "Item": ["Selling price/u", "Variable prod cost/u", "Fixed OH/u (OAR)",
             "Units produced", "Units sold", "Closing inventory",
             "Marginal profit", "Absorption profit", "Difference (Abs-Marg)"],
    "Value": [price, var_prod, round(oar, 2), production, sales, closing_inv,
              round(marginal_profit, 0), round(abs_profit, 0), round(diff, 0)],
})
st.download_button(
    "⬇️ Download this costing comparison (CSV)",
    data=summary.to_csv(index=False).encode("utf-8"),
    file_name="absorption_vs_marginal.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 0.3 · Controllable vs. Uncontrollable Costs", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 1.2 · Activity-Based Costing (ABC) ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 1.1")
