"""
Performance Management — Applied Learning Series
Module 2.2 · Flexible Budgets
------------------------------------------------------------
An interactive study of flexible budgeting: why a fixed budget is an
unfair yardstick, how to "flex" a budget to the actual activity level,
and how the flexed budget isolates a fair volume vs. expenditure split.

Run with:  streamlit run 2.2_Flexible_Budgets.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="2.2 · Flexible Budgets",
    page_icon="🪗",
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
st.markdown('<p class="big-title">2.2 · Flexible Budgets</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand why a <b>fixed budget</b> is an unfair yardstick when '
    'activity changes, and learn to <b>flex</b> a budget to the actual volume so you can split total '
    'variance into a fair <b>volume</b> effect and a controllable <b>expenditure</b> effect.</p>',
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
A **fixed budget** is set for a single planned level of activity and is *not* changed
afterwards. It is fine for planning, but it is a **poor control tool**: if actual volume
differs from plan, comparing actual costs against the original budget mixes two very
different things together — the effect of *doing more/less* and the effect of *spending
more/less per unit*.

A **flexible (flexed) budget** solves this. It **re-states the budget at the actual
activity level**, using the original cost behaviour:

- **Variable costs** are flexed in proportion to actual volume.
- **Fixed costs** stay the same (they don't move with activity).

This lets us split the **total variance** into two fair pieces:

1. **Volume variance** = Flexed budget − Original fixed budget
   *(the effect of operating at a different activity level — often not the manager's fault)*
2. **Expenditure variance** = Actual − Flexed budget
   *(the truly controllable effect — spending more or less than expected for the volume achieved)*

**The golden rule of control:** always compare **actual results to the flexed budget**,
never to the original fixed budget.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Flexing the budget is what makes variance analysis *fair*. Without it, a manager who "
        "produced more than planned looks 'over budget' on cost even when perfectly efficient. "
        "Flexed budgets separate volume noise from real cost control — vital in a factory where "
        "output rarely lands exactly on plan.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Budget Flexing Engine
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Budget Flexing Engine</p>',
            unsafe_allow_html=True)
st.caption("Set the original budget and the actual results, then watch the budget flex and split the variance.")

left, right = st.columns([1, 1.5])

with left:
    st.markdown("#### 🎛️ Inputs")
    st.markdown("**Original (fixed) budget**")
    budget_units = st.number_input("Budgeted output (units)", 1, 5_000_000, 10000, step=500)
    var_cost_pu  = st.number_input("Budgeted variable cost per unit (BDT)", 0.0, 100000.0, 60.0, step=1.0)
    fixed_cost   = st.number_input("Budgeted fixed cost (BDT)", 0.0, 100_000_000.0, 300_000.0, step=10_000.0)

    st.markdown("**Actual results**")
    actual_units = st.number_input("Actual output (units)", 1, 5_000_000, 11500, step=500)
    actual_var   = st.number_input("Actual variable cost (BDT)", 0.0, 1_000_000_000.0, 736_000.0, step=10_000.0)
    actual_fixed = st.number_input("Actual fixed cost (BDT)", 0.0, 100_000_000.0, 310_000.0, step=5_000.0)

# ---- Calculations ----
# Original fixed budget
orig_var   = budget_units * var_cost_pu
orig_total = orig_var + fixed_cost

# Flexed budget (variable flexed to ACTUAL units, fixed unchanged)
flex_var   = actual_units * var_cost_pu
flex_total = flex_var + fixed_cost

# Actual
actual_total = actual_var + actual_fixed

# Variance split (for costs: Adverse when actual > budget)
total_variance       = actual_total - orig_total          # vs fixed budget (misleading if used alone)
volume_variance      = flex_total - orig_total            # effect of volume change
expenditure_variance = actual_total - flex_total          # controllable spend effect

# Break expenditure into variable & fixed
var_exp_variance   = actual_var - flex_var
fixed_exp_variance = actual_fixed - fixed_cost

def av(x):  # label helper for COST variances (positive = adverse spend)
    if abs(x) < 1e-9:
        return "—", "🟡"
    return ("Adverse", "🔴") if x > 0 else ("Favourable", "🟢")

with right:
    st.markdown("#### 📊 Flexed Budget Comparison")

    comp = pd.DataFrame({
        "": ["Output (units)", "Variable cost (BDT)", "Fixed cost (BDT)", "Total cost (BDT)"],
        "Original budget": [budget_units, orig_var, fixed_cost, orig_total],
        "Flexed budget":   [actual_units, flex_var, fixed_cost, flex_total],
        "Actual":          [actual_units, actual_var, actual_fixed, actual_total],
    })
    st.dataframe(
        comp.style.format({"Original budget": "{:,.0f}",
                           "Flexed budget": "{:,.0f}",
                           "Actual": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    vol_word, vol_icon = av(volume_variance)
    exp_word, exp_icon = av(expenditure_variance)
    m1, m2 = st.columns(2)
    m1.metric("Volume variance", f"{abs(volume_variance):,.0f} BDT", f"{vol_icon} {vol_word}",
              delta_color="off")
    m2.metric("Expenditure variance", f"{abs(expenditure_variance):,.0f} BDT",
              f"{exp_icon} {exp_word}", delta_color="off")

# ---- Bridge chart: original -> volume -> expenditure -> actual ----
st.markdown("#### 💧 Variance Bridge (Original Budget → Actual)")
bridge = go.Figure(go.Waterfall(
    orientation="v",
    measure=["absolute", "relative", "relative", "total"],
    x=["Original budget", "Volume variance", "Expenditure variance", "Actual cost"],
    y=[orig_total, volume_variance, expenditure_variance, actual_total],
    text=[f"{orig_total:,.0f}", f"{volume_variance:+,.0f}",
          f"{expenditure_variance:+,.0f}", f"{actual_total:,.0f}"],
    textposition="outside",
    connector={"line": {"color": "#b0b7bf"}},
    increasing={"marker": {"color": "#e67e22"}},   # cost up = adverse
    decreasing={"marker": {"color": "#1e8449"}},   # cost down = favourable
    totals={"marker": {"color": "#2e86de"}},
))
bridge.update_layout(height=380, margin=dict(t=40, b=10), yaxis_title="BDT",
                     plot_bgcolor="white")
st.plotly_chart(bridge, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic commentary
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

vol_dir = "above" if actual_units > budget_units else ("below" if actual_units < budget_units else "equal to")
unit_diff = actual_units - budget_units
var_word, var_icon = av(var_exp_variance)
fix_word, fix_icon = av(fixed_exp_variance)

st.markdown(
    f"""
- 🪗 **Flexing:** actual output of **{actual_units:,} units** is **{abs(unit_diff):,} units {vol_dir}** budget,
  so the variable budget flexes from **{orig_var:,.0f}** to **{flex_var:,.0f} BDT** (fixed cost stays at **{fixed_cost:,.0f}**).
- 📦 **Volume variance = {abs(volume_variance):,.0f} BDT ({vol_word}).** This is purely the effect of
  operating at a different activity level — generally **not** a measure of cost control.
- 🎯 **Expenditure variance = {abs(expenditure_variance):,.0f} BDT ({exp_word}).** This is the
  **controllable** part: spending vs. what the flexed budget allowed for the volume achieved.
    - {var_icon} Variable spend: **{abs(var_exp_variance):,.0f} BDT {var_word}**
    - {fix_icon} Fixed spend: **{abs(fixed_exp_variance):,.0f} BDT {fix_word}**
    """
)

if expenditure_variance > 0:
    st.warning(
        f"**ACT →** The controllable expenditure variance is **adverse ({expenditure_variance:,.0f} BDT)**. "
        f"Even after allowing for the volume change, actual spend exceeded the flexed budget. "
        f"Investigate the variable and fixed drivers before judging performance — this is exactly "
        f"the split that Module 3 (Variance Analysis) drills into.",
        icon="⚠️",
    )
elif expenditure_variance < 0:
    st.success(
        f"**Well controlled.** The flexed comparison shows a **favourable expenditure variance "
        f"({abs(expenditure_variance):,.0f} BDT)** — real cost efficiency, not just a volume effect. "
        f"This is the fair verdict a fixed-budget comparison would have hidden.",
        icon="✅",
    )
else:
    st.info("Actual spend exactly matches the flexed budget — no controllable variance.", icon="🟡")

st.caption(
    f"⚠️ Note: comparing actual ({actual_total:,.0f}) to the *original* budget "
    f"({orig_total:,.0f}) gives a total variance of {abs(total_variance):,.0f} BDT — but that "
    f"mixes volume and spend together, which is why we flex first."
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
        - [ ] Never judge performance against a **fixed budget** when volume has moved.
        - [ ] **Flex** variable costs to actual volume; keep **fixed** costs unchanged.
        - [ ] Split total variance into **volume** (uncontrollable) and **expenditure** (controllable).
        - [ ] Compare **actual to the flexed budget** — the golden rule of control.
        - [ ] The flexed budget is the launch-pad for detailed **variance analysis** (Module 3).
        """
    )
with a2:
    with st.expander("📘 Key terms & formulas in this module"):
        st.markdown(
            """
            - **Fixed budget** — set for one activity level, not changed.
            - **Flexible budget** — restated at the actual activity level.
            - **Flexed variable cost** = Actual units × budgeted variable cost/unit.
            - **Volume variance** = Flexed budget − Original fixed budget.
            - **Expenditure variance** = Actual − Flexed budget.
            - **Favourable (F)** — actual cost below allowance; **Adverse (A)** — above.
            """
        )
    with st.expander("🧭 How to flex a budget in 3 steps"):
        st.markdown(
            """
            1. Split every cost into **fixed** and **variable**.
            2. Recalculate **variable** costs at the **actual** activity level.
            3. Leave **fixed** costs unchanged, then compare **actual vs. flexed**.
            """
        )

# Downloadable template
template = pd.DataFrame({
    "Line item": ["Budgeted output (u)", "Actual output (u)",
                  "Budget variable cost/unit", "Budgeted fixed cost",
                  "Original budget – variable", "Original budget – total",
                  "Flexed budget – variable", "Flexed budget – total",
                  "Actual variable cost", "Actual fixed cost", "Actual total cost",
                  "Volume variance", "Expenditure variance",
                  "  of which variable-spend", "  of which fixed-spend"],
    "Value": [budget_units, actual_units, var_cost_pu, fixed_cost,
              orig_var, orig_total, flex_var, flex_total,
              actual_var, actual_fixed, actual_total,
              volume_variance, expenditure_variance,
              var_exp_variance, fixed_exp_variance],
})
st.download_button(
    "⬇️ Download this flexed budget as a CSV template",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="flexible_budget_template.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 2.1 · Budget Preparation", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 2.3 · Zero-Based & Rolling Budgets ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 2.2")
