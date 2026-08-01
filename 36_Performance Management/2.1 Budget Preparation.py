"""
Performance Management — Applied Learning Series
Module 2.1 · Budget Preparation
------------------------------------------------------------
An interactive walk-through of how functional budgets connect into
a master budget: Sales -> Production -> Materials / Labour / Overhead
-> Cost of production -> Operating profit -> Cash.

Run with:  streamlit run 2.1_Budget_Preparation.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="2.1 · Budget Preparation",
    page_icon="🧾",
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
st.markdown('<p class="pill">MODULE 2 · BUDGETING & CONTROL</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">2.1 · Budget Preparation</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: learn how the <b>functional budgets</b> — sales, production, '
    'materials, labour and overhead — link together into a <b>master budget</b>, and how the '
    'sales forecast cascades all the way through to profit and cash.</p>',
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
A **budget** is a quantified financial plan for a future period. **Budget preparation**
is the process of building a set of coordinated functional budgets that roll up into a
**master budget** (a budgeted income statement, balance sheet and cash flow).

**The budgeting sequence** usually starts from the *principal budget factor* — the
constraint that limits activity (normally sales demand):

1. **Sales budget** — units to sell × selling price = budgeted revenue.
2. **Production budget** — sales units, adjusted for opening and closing finished-goods
   inventory, gives units to produce.
3. **Materials budget** — production units × material per unit × price, adjusted for
   raw-material inventory, gives purchases.
4. **Labour budget** — production units × hours per unit × rate.
5. **Overhead budget** — variable overhead (per unit) plus fixed overhead.
6. **Master budget** — everything consolidates into budgeted profit and a cash budget.

**Key inventory relationship (production budget):**

- *Units to produce* = Sales units + Closing inventory − Opening inventory
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Budget preparation is where strategy becomes numbers. A well-built master budget "
        "coordinates every department, sets the yardstick for later variance analysis, and "
        "reveals cash pinch-points *before* they happen — essential for factory and "
        "commercial planning.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Master Budget Builder
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Master Budget Builder</p>',
            unsafe_allow_html=True)
st.caption("Set your sales plan and cost structure, and watch the functional budgets cascade into a master budget.")

left, right = st.columns([1, 1.5])

with left:
    st.markdown("#### 🎛️ Inputs")
    st.markdown("**Sales budget**")
    sales_units   = st.number_input("Budgeted sales (units)", 0, 5_000_000, 10000, step=500)
    selling_price = st.number_input("Selling price per unit (BDT)", 0.0, 100000.0, 100.0, step=5.0)

    st.markdown("**Inventory policy (finished goods)**")
    open_fg  = st.number_input("Opening finished-goods (units)", 0, 1_000_000, 800, step=100)
    close_fg = st.number_input("Closing finished-goods (units)", 0, 1_000_000, 1200, step=100)

    st.markdown("**Cost structure (per unit produced)**")
    mat_per_unit = st.number_input("Material cost per unit (BDT)", 0.0, 100000.0, 35.0, step=1.0)
    lab_per_unit = st.number_input("Labour cost per unit (BDT)", 0.0, 100000.0, 18.0, step=1.0)
    voh_per_unit = st.number_input("Variable overhead per unit (BDT)", 0.0, 100000.0, 7.0, step=1.0)
    fixed_oh     = st.number_input("Total fixed overhead (BDT)", 0.0, 100_000_000.0, 120_000.0, step=10_000.0)

# ---- Calculations ----
# Production budget
units_to_produce = sales_units + close_fg - open_fg
units_to_produce = max(units_to_produce, 0)

# Functional cost budgets (based on production)
material_budget = units_to_produce * mat_per_unit
labour_budget   = units_to_produce * lab_per_unit
voh_budget      = units_to_produce * voh_per_unit
total_prod_cost = material_budget + labour_budget + voh_budget + fixed_oh

# Revenue & profit
revenue = sales_units * selling_price
unit_var_cost = mat_per_unit + lab_per_unit + voh_per_unit
# cost of goods SOLD approximated on sales units for variable + full fixed OH
cogs_variable = sales_units * unit_var_cost
budgeted_cost_of_sales = cogs_variable + fixed_oh
operating_profit = revenue - budgeted_cost_of_sales
op_margin = (operating_profit / revenue * 100) if revenue else 0

with right:
    st.markdown("#### 📊 Master Budget Summary")
    m1, m2, m3 = st.columns(3)
    m1.metric("Units to produce", f"{units_to_produce:,.0f} u",
              f"{units_to_produce - sales_units:+,.0f} vs sales")
    m2.metric("Budgeted revenue", f"{revenue:,.0f} BDT")
    m3.metric("Operating profit", f"{operating_profit:,.0f} BDT", f"{op_margin:.1f}% margin",
              delta_color="normal" if operating_profit >= 0 else "inverse")

    # Functional budget table
    budget_tbl = pd.DataFrame({
        "Functional budget": ["Sales revenue", "Materials", "Labour",
                              "Variable overhead", "Fixed overhead", "Total production cost"],
        "Basis": [f"{sales_units:,} u sold", f"{units_to_produce:,} u produced",
                  f"{units_to_produce:,} u produced", f"{units_to_produce:,} u produced",
                  "period cost", "sum of above"],
        "Amount (BDT)": [revenue, material_budget, labour_budget,
                         voh_budget, fixed_oh, total_prod_cost],
    })
    st.dataframe(
        budget_tbl.style.format({"Amount (BDT)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

# ---- Waterfall: revenue -> costs -> profit ----
st.markdown("#### 💧 Revenue-to-Profit Waterfall")
wf = go.Figure(go.Waterfall(
    orientation="v",
    measure=["absolute", "relative", "relative", "relative", "relative", "total"],
    x=["Revenue", "Materials", "Labour", "Var. overhead", "Fixed overhead", "Operating profit"],
    y=[revenue, -cogs_variable * (mat_per_unit/unit_var_cost if unit_var_cost else 0),
       -cogs_variable * (lab_per_unit/unit_var_cost if unit_var_cost else 0),
       -cogs_variable * (voh_per_unit/unit_var_cost if unit_var_cost else 0),
       -fixed_oh, operating_profit],
    connector={"line": {"color": "#b0b7bf"}},
    increasing={"marker": {"color": "#2e86de"}},
    decreasing={"marker": {"color": "#e67e22"}},
    totals={"marker": {"color": "#1e8449"}},
))
wf.update_layout(height=380, margin=dict(t=30, b=10), yaxis_title="BDT", plot_bgcolor="white")
st.plotly_chart(wf, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic commentary
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

inv_change = close_fg - open_fg
if inv_change > 0:
    inv_note = (f"You plan to **build inventory by {inv_change:,} units**, so production "
                f"({units_to_produce:,}) exceeds sales ({sales_units:,}).")
elif inv_change < 0:
    inv_note = (f"You plan to **run down inventory by {abs(inv_change):,} units**, so production "
                f"({units_to_produce:,}) is below sales ({sales_units:,}).")
else:
    inv_note = f"Inventory is held flat, so production equals sales ({sales_units:,} units)."

st.markdown(
    f"""
- 🏭 **Production budget:** {inv_note}
- 🧱 **Cost build-up:** each unit produced carries **{unit_var_cost:,.1f} BDT** of variable cost
  (materials {mat_per_unit:,.0f} + labour {lab_per_unit:,.0f} + var. OH {voh_per_unit:,.0f}),
  on top of **{fixed_oh:,.0f} BDT** fixed overhead for the period.
- 💵 **Profitability:** budgeted revenue of **{revenue:,.0f} BDT** yields an operating profit of
  **{operating_profit:,.0f} BDT** ({op_margin:.1f}% margin).
    """
)

if operating_profit < 0:
    st.error(
        "**The budget shows a loss.** Revenue does not cover budgeted costs. Revisit price, "
        "volume, or the cost structure before finalising the master budget.",
        icon="🔴",
    )
elif op_margin < 10:
    st.warning(
        f"**Thin margin ({op_margin:.1f}%).** The budget is profitable but leaves little "
        f"cushion. Small adverse variances later could erase it — build in contingency and "
        f"watch the cost budgets closely.",
        icon="⚠️",
    )
else:
    st.success(
        f"**Healthy budgeted margin ({op_margin:.1f}%).** The functional budgets consolidate "
        f"into a robust master budget. Use this as the control benchmark for later variance "
        f"analysis (Module 3).",
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
        - [ ] Identify the **principal budget factor** first (usually sales demand).
        - [ ] Budget in sequence: **sales → production → materials/labour/overhead**.
        - [ ] Never forget the **inventory adjustment** in the production budget.
        - [ ] All functional budgets must **reconcile** into the master budget.
        - [ ] The master budget becomes the **benchmark** for variance analysis.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Budget** — a quantified financial plan for a future period.
            - **Functional budget** — a plan for one function (sales, production, etc.).
            - **Master budget** — the consolidated budgeted P&L, balance sheet and cash flow.
            - **Principal budget factor** — the constraint that limits activity.
            - **Production budget** = Sales + Closing inventory − Opening inventory.
            - **Cash budget** — the timing of receipts and payments (liquidity view).
            """
        )
    with st.expander("🔁 The budgeting sequence at a glance"):
        st.markdown(
            """
            Sales budget → Production budget → Materials + Labour + Overhead budgets →
            Cost of production → Budgeted income statement → **Cash budget** →
            Budgeted balance sheet.
            """
        )

# Downloadable template
template = pd.DataFrame({
    "Line item": ["Budgeted sales (units)", "Selling price/unit", "Budgeted revenue",
                  "Opening finished goods", "Closing finished goods", "Units to produce",
                  "Material budget", "Labour budget", "Variable overhead budget",
                  "Fixed overhead", "Total production cost",
                  "Variable cost of sales", "Operating profit", "Operating margin (%)"],
    "Value": [sales_units, selling_price, revenue, open_fg, close_fg, units_to_produce,
              material_budget, labour_budget, voh_budget, fixed_oh, total_prod_cost,
              cogs_variable, operating_profit, round(op_margin, 1)],
})
st.download_button(
    "⬇️ Download this master budget as a CSV template",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="master_budget_template.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 1.3 · Cost Behaviour & CVP", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 2.2 · Flexible Budgets ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 2.1")
