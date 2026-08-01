"""
Performance Management — Applied Learning Series
Module 3.2 · Overhead Variances
------------------------------------------------------------
The trickiest variances, made clear:
  • Variable overhead → expenditure + efficiency
  • Fixed overhead   → expenditure + volume
                       (volume further split into capacity + efficiency)
All reconciled back to the total under absorption costing.

Run with:  streamlit run 3.2_Overhead_Variances.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="3.2 · Overhead Variances",
    page_icon="🏗️",
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
st.markdown('<p class="pill">MODULE 3 · VARIANCE ANALYSIS</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">3.2 · Overhead Variances</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: split <b>variable overhead</b> into expenditure and efficiency, and '
    '<b>fixed overhead</b> into expenditure and volume (with volume further split into <b>capacity</b> and '
    '<b>efficiency</b>) — and reconcile them under absorption costing.</p>',
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
Overhead variances are trickier than material/labour because overheads are **absorbed**
using a predetermined rate, and fixed overheads behave differently from variable ones.

**Variable overhead** (varies with activity, usually labour hours):

- **Expenditure variance** = (Std VOH rate × Actual hours) − Actual VOH cost
  *→ did we spend more/less per hour than expected?*
- **Efficiency variance** = (Std hours for output − Actual hours) × Std VOH rate
  *→ mirrors labour efficiency: did we work faster/slower?*

**Fixed overhead** (does not change with activity in the short run):

- **Expenditure variance** = Budgeted fixed OH − Actual fixed OH
  *→ did total fixed spend differ from budget?*
- **Volume variance** = (Actual output − Budgeted output) × Std fixed OH rate per unit
  *→ under absorption costing, did we over/under-absorb fixed OH by producing more/less
  than planned?*

The **fixed overhead volume variance** can be split further:

- **Capacity variance** = (Actual hours − Budgeted hours) × Std OAR per hour
  *→ did we work more/fewer hours than budgeted (used our capacity)?*
- **Efficiency variance** = (Std hours for output − Actual hours) × Std OAR per hour
  *→ were those hours productive?*

**Reconciliation:** Expenditure + Volume = Total fixed OH variance, and
Capacity + Efficiency = Volume variance. **F** = over-absorbed / underspent; **A** =
under-absorbed / overspent.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "The fixed overhead **volume variance** is unique to absorption costing — it measures "
        "over/under-absorption, not cash. Splitting it into capacity and efficiency tells you "
        "whether an under-absorption was caused by *idle capacity* or by *working slowly* — two "
        "very different management problems.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Overhead Variance Engine</p>',
            unsafe_allow_html=True)

def fav_adv(v):
    """Return (word, icon) for a COST variance where positive = Favourable."""
    if abs(v) < 1e-9:
        return "—", "🟡"
    return ("Favourable", "🟢") if v > 0 else ("Adverse", "🔴")

tab_voh, tab_foh = st.tabs(["⚡ Variable Overhead", "🏛️ Fixed Overhead"])

# ==================================================================
# TAB 1 — VARIABLE OVERHEAD
# ==================================================================
with tab_voh:
    st.caption("Split variable overhead into expenditure and efficiency variances.")

    vl, vr = st.columns([1, 1.5])
    with vl:
        st.markdown("#### 🎛️ Inputs")
        v_output   = st.number_input("Actual output (units)", 1, 5_000_000, 10000, step=500, key="voh_out")
        v_std_hpu  = st.number_input("Standard hours per unit", 0.0, 10000.0, 0.5, step=0.05, key="voh_hpu")
        v_std_rate = st.number_input("Standard VOH rate per hour (BDT)", 0.0, 100000.0, 20.0, step=1.0, key="voh_rate")
        v_act_hrs  = st.number_input("Actual hours worked", 0.0, 100_000_000.0, 5300.0, step=50.0, key="voh_hrs")
        v_act_cost = st.number_input("Actual variable OH cost (BDT)", 0.0, 1_000_000_000.0, 100_700.0, step=1000.0, key="voh_cost")

    v_std_hrs = v_output * v_std_hpu

    voh_exp = (v_std_rate * v_act_hrs) - v_act_cost           # expenditure
    voh_eff = (v_std_hrs - v_act_hrs) * v_std_rate            # efficiency
    voh_total = voh_exp + voh_eff

    e_word, e_icon = fav_adv(voh_exp)
    f_word, f_icon = fav_adv(voh_eff)
    t_word, t_icon = fav_adv(voh_total)

    with vr:
        st.markdown("#### 📊 Variable Overhead Result")
        a, b, c = st.columns(3)
        a.metric("Expenditure", f"{abs(voh_exp):,.0f} BDT", f"{e_icon} {e_word}", delta_color="off")
        b.metric("Efficiency", f"{abs(voh_eff):,.0f} BDT", f"{f_icon} {f_word}", delta_color="off")
        c.metric("Total VOH", f"{abs(voh_total):,.0f} BDT", f"{t_icon} {t_word}", delta_color="off")

        proof = pd.DataFrame({
            "Cost column": ["① Std hrs × Std rate (flexed)",
                            "② Actual hrs × Std rate",
                            "③ Actual VOH cost"],
            "BDT": [v_std_hrs * v_std_rate, v_act_hrs * v_std_rate, v_act_cost],
        })
        st.dataframe(proof.style.format({"BDT": "{:,.0f}"}), use_container_width=True, hide_index=True)
        st.caption("Efficiency = ① − ②  •  Expenditure = ② − ③  •  Total = ① − ③")

    st.markdown(
        f"""
**Interpretation:** {e_icon} **Expenditure {abs(voh_exp):,.0f} BDT ({e_word})** — actual VOH spend vs the
{v_act_hrs:,.0f} hrs × {v_std_rate:,.1f} standard allowance. {f_icon} **Efficiency {abs(voh_eff):,.0f} BDT
({f_word})** — {v_act_hrs:,.0f} hrs worked vs {v_std_hrs:,.0f} hrs allowed for {v_output:,} units (mirrors
labour efficiency).
        """
    )

# ==================================================================
# TAB 2 — FIXED OVERHEAD
# ==================================================================
with tab_foh:
    st.caption("Split fixed overhead into expenditure and volume — then volume into capacity and efficiency.")

    fl, fr = st.columns([1, 1.5])
    with fl:
        st.markdown("#### 🎛️ Inputs")
        f_bud_oh   = st.number_input("Budgeted fixed OH (BDT)", 0.0, 1_000_000_000.0, 300_000.0, step=10_000.0, key="foh_bud")
        f_bud_out  = st.number_input("Budgeted output (units)", 1, 5_000_000, 10000, step=500, key="foh_bout")
        f_std_hpu  = st.number_input("Standard hours per unit", 0.0, 10000.0, 0.5, step=0.05, key="foh_hpu")
        f_act_out  = st.number_input("Actual output (units)", 1, 5_000_000, 9200, step=500, key="foh_aout")
        f_act_hrs  = st.number_input("Actual hours worked", 0.0, 100_000_000.0, 4750.0, step=50.0, key="foh_hrs")
        f_act_oh   = st.number_input("Actual fixed OH (BDT)", 0.0, 1_000_000_000.0, 312_000.0, step=5_000.0, key="foh_act")

    # Standard rates
    bud_hrs      = f_bud_out * f_std_hpu
    oar_per_unit = f_bud_oh / f_bud_out if f_bud_out else 0
    oar_per_hr   = f_bud_oh / bud_hrs if bud_hrs else 0
    std_hrs_out  = f_act_out * f_std_hpu
    absorbed     = f_act_out * oar_per_unit

    # Variances (positive = favourable / over-absorbed / underspent)
    foh_exp    = f_bud_oh - f_act_oh                                  # expenditure
    foh_vol    = (f_act_out - f_bud_out) * oar_per_unit               # volume
    foh_total  = foh_exp + foh_vol
    foh_cap    = (f_act_hrs - bud_hrs) * oar_per_hr                   # capacity
    foh_effy   = (std_hrs_out - f_act_hrs) * oar_per_hr               # efficiency

    ex_w, ex_i = fav_adv(foh_exp)
    vo_w, vo_i = fav_adv(foh_vol)
    to_w, to_i = fav_adv(foh_total)
    ca_w, ca_i = fav_adv(foh_cap)
    ey_w, ey_i = fav_adv(foh_effy)

    with fr:
        st.markdown("#### 📊 Fixed Overhead Result")
        a, b, c = st.columns(3)
        a.metric("Expenditure", f"{abs(foh_exp):,.0f} BDT", f"{ex_i} {ex_w}", delta_color="off")
        b.metric("Volume", f"{abs(foh_vol):,.0f} BDT", f"{vo_i} {vo_w}", delta_color="off")
        c.metric("Total FOH", f"{abs(foh_total):,.0f} BDT", f"{to_i} {to_w}", delta_color="off")

        d, e = st.columns(2)
        d.metric("↳ Capacity", f"{abs(foh_cap):,.0f} BDT", f"{ca_i} {ca_w}", delta_color="off")
        e.metric("↳ Efficiency", f"{abs(foh_effy):,.0f} BDT", f"{ey_i} {ey_w}", delta_color="off")

        st.caption(f"OAR: **{oar_per_unit:,.2f} BDT/unit**  •  **{oar_per_hr:,.2f} BDT/hr**  •  "
                   f"Absorbed: **{absorbed:,.0f} BDT**")

    # Volume -> capacity + efficiency bridge
    bridge = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "relative", "total"],
        x=["Budgeted FOH", "Expenditure", "Volume", "≈ Absorbed"],
        y=[f_bud_oh, -foh_exp, foh_vol, absorbed],
        text=[f"{f_bud_oh:,.0f}", f"{-foh_exp:+,.0f}", f"{foh_vol:+,.0f}", f"{absorbed:,.0f}"],
        textposition="outside",
        connector={"line": {"color": "#b0b7bf"}},
        increasing={"marker": {"color": "#1e8449"}},
        decreasing={"marker": {"color": "#e67e22"}},
        totals={"marker": {"color": "#2e86de"}},
    ))
    bridge.update_layout(height=340, margin=dict(t=40, b=10), yaxis_title="BDT",
                         title="Budgeted → Absorbed fixed overhead", plot_bgcolor="white")
    st.plotly_chart(bridge, use_container_width=True)

    st.markdown(
        f"""
**Interpretation:** {ex_i} **Expenditure {abs(foh_exp):,.0f} BDT ({ex_w})** — actual fixed spend
{f_act_oh:,.0f} vs budget {f_bud_oh:,.0f}. {vo_i} **Volume {abs(foh_vol):,.0f} BDT ({vo_w})** —
{'over' if foh_vol > 0 else 'under'}-absorbed because actual output ({f_act_out:,}) was
{'above' if f_act_out > f_bud_out else 'below'} budget ({f_bud_out:,}). This volume effect breaks into
{ca_i} **capacity ({ca_w})** — hours worked {f_act_hrs:,.0f} vs budgeted {bud_hrs:,.0f} — and
{ey_i} **efficiency ({ey_w})** — {f_act_hrs:,.0f} hrs vs {std_hrs_out:,.0f} allowed for output.
        """
    )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — capacity vs. efficiency, and what it means</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 🏭 **The volume variance is about absorption, not cash.** An adverse fixed OH volume variance
  means output fell short of plan, so budgeted overhead was **under-absorbed** — a costing effect,
  not extra spending.
- 🔍 **Capacity vs. efficiency answers *why*.** Under-absorption from an **adverse capacity**
  variance means the plant ran fewer hours (idle time, breakdowns, low demand). From **adverse
  efficiency**, it means the hours worked were unproductive. Different problems, different owners.
- ⚡ **Variable OH efficiency mirrors labour efficiency.** Because VOH is driven by hours, whatever
  causes an adverse labour-efficiency variance usually causes an adverse VOH-efficiency variance too.
- 🔁 **Feed it back.** Persistent volume variances often signal that the **budgeted activity level**
  (and therefore the absorption rate) needs revisiting.
    """
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
        - [ ] **Variable OH** splits like labour: **expenditure + efficiency**.
        - [ ] **Fixed OH** splits into **expenditure + volume** (absorption costing only).
        - [ ] **Volume** further splits into **capacity + efficiency**.
        - [ ] Volume variance measures **over/under-absorption**, not cash spent.
        - [ ] **F** = over-absorbed / underspent; **A** = under-absorbed / overspent.
        """
    )
with a2:
    with st.expander("📘 Key formulas in this module"):
        st.markdown(
            """
            **Variable OH**
            - Expenditure = (Std rate × Actual hrs) − Actual VOH
            - Efficiency = (Std hrs for output − Actual hrs) × Std rate

            **Fixed OH**
            - Expenditure = Budgeted FOH − Actual FOH
            - Volume = (Actual − Budgeted output) × Std OAR/unit
            - Capacity = (Actual hrs − Budgeted hrs) × Std OAR/hr
            - Efficiency = (Std hrs for output − Actual hrs) × Std OAR/hr
            """
        )
    with st.expander("🧭 Marginal vs. absorption costing note"):
        st.markdown(
            """
            The **fixed overhead volume variance (and its capacity/efficiency split) exists only
            under absorption costing**, where fixed OH is absorbed into units. Under **marginal
            costing**, fixed OH is a period cost, so only the **expenditure** variance arises.
            """
        )

# Downloadable combined result
template = pd.DataFrame({
    "Variance": ["VOH expenditure", "VOH efficiency", "VOH total",
                 "FOH expenditure", "FOH volume", "FOH total",
                 "↳ FOH capacity", "↳ FOH efficiency"],
    "Amount (BDT)": [voh_exp, voh_eff, voh_total,
                     foh_exp, foh_vol, foh_total, foh_cap, foh_effy],
    "F/A": [fav_adv(voh_exp)[0], fav_adv(voh_eff)[0], fav_adv(voh_total)[0],
            fav_adv(foh_exp)[0], fav_adv(foh_vol)[0], fav_adv(foh_total)[0],
            fav_adv(foh_cap)[0], fav_adv(foh_effy)[0]],
})
st.download_button(
    "⬇️ Download the overhead variance summary (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="overhead_variances.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 3.1 · Material & Labour Variances", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 3.3 · Sales Variances ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 3.2")
