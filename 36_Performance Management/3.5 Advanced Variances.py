"""
Performance Management — Applied Learning Series
Module 3.5 · Advanced Variances
------------------------------------------------------------
Two advanced topics that sharpen variance analysis:
  • Planning vs. Operational variances — separating an out-of-date
    standard (planning) from genuine performance (operational).
  • Materials Mix & Yield — splitting the usage variance when inputs
    are substitutable (process industries).

Run with:  streamlit run 3.5_Advanced_Variances.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="3.5 · Advanced Variances",
    page_icon="🔬",
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
st.markdown('<p class="big-title">3.5 · Advanced Variances</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: separate an out-of-date standard from genuine performance using '
    '<b>planning vs. operational</b> variances, and split the materials usage variance into '
    '<b>mix</b> and <b>yield</b> when inputs are substitutable.</p>',
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
Basic variances assume the **original standard was correct**. Advanced variance analysis
challenges that assumption and digs deeper.

**Planning vs. operational variances**

Sometimes a variance arises not because a manager performed poorly, but because the
*original standard was unrealistic* (e.g. a market price shifted after the budget was set).
We separate the two:

- **Planning variance** = (Original standard − Revised/realistic standard) × Actual quantity
  *→ the part caused by a flawed standard — uncontrollable by the operational manager.*
- **Operational variance** = (Revised standard − Actual) × Actual quantity
  *→ the genuinely controllable performance against a fair, up-to-date standard.*

This is fairer: managers are judged only on the **operational** variance, against a
**revised ex-post standard** that reflects conditions they actually faced.

**Materials mix & yield**

Where inputs are **substitutable** (chemicals, food, animal feed), the materials **usage**
variance splits into:

- **Mix variance** = (Actual quantity in actual mix − Actual quantity in standard mix)
  × Standard price
  *→ did we use a cheaper/dearer blend of inputs than the standard recipe?*
- **Yield variance** = (Standard input for actual output − Actual total input)
  × Standard cost per unit of input
  *→ did the total input produce more/less output than the standard recipe expected?*

**Reconciliation:** Planning + Operational = Total variance; Mix + Yield = Usage variance.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Planning/operational analysis protects managers from being blamed for market shocks and "
        "keeps standards honest. Mix & yield is decisive in process industries — a cheaper input "
        "blend (favourable mix) that ruins the yield (adverse yield) can destroy margin. Both "
        "sharpen accountability where basic variances mislead.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

def fav_adv(v):
    """Return (word, icon) for a COST variance where positive = Favourable."""
    if abs(v) < 1e-9:
        return "—", "🟡"
    return ("Favourable", "🟢") if v > 0 else ("Adverse", "🔴")

tab_po, tab_my = st.tabs(["🎯 Planning vs. Operational", "🧪 Materials Mix & Yield"])

# ==================================================================
# TAB 1 — PLANNING vs OPERATIONAL
# ==================================================================
with tab_po:
    st.caption("Split a total variance into the part caused by a flawed standard (planning) vs. genuine performance (operational).")

    pl, pr = st.columns([1, 1.4])
    with pl:
        st.markdown("#### 🎛️ Inputs (material price example)")
        act_qty   = st.number_input("Actual quantity used (kg)", 0.0, 100_000_000.0, 21000.0, step=100.0, key="po_qty")
        orig_std  = st.number_input("Original standard price (BDT/kg)", 0.0, 100000.0, 50.0, step=1.0, key="po_orig")
        rev_std   = st.number_input("Revised (realistic) standard price (BDT/kg)", 0.0, 100000.0, 54.0, step=1.0, key="po_rev")
        act_price = st.number_input("Actual price paid (BDT/kg)", 0.0, 100000.0, 52.0, step=1.0, key="po_act")

    planning_var    = (orig_std - rev_std) * act_qty      # flawed standard
    operational_var = (rev_std - act_price) * act_qty     # genuine performance
    total_var       = (orig_std - act_price) * act_qty

    pl_w, pl_i = fav_adv(planning_var)
    op_w, op_i = fav_adv(operational_var)
    to_w, to_i = fav_adv(total_var)

    with pr:
        st.markdown("#### 📊 Result")
        a, b, c = st.columns(3)
        a.metric("Planning variance", f"{abs(planning_var):,.0f} BDT", f"{pl_i} {pl_w}", delta_color="off")
        b.metric("Operational variance", f"{abs(operational_var):,.0f} BDT", f"{op_i} {op_w}", delta_color="off")
        c.metric("Total variance", f"{abs(total_var):,.0f} BDT", f"{to_i} {to_w}", delta_color="off")

        proof = pd.DataFrame({
            "Price basis (BDT/kg)": ["① Original standard", "② Revised standard", "③ Actual"],
            "Value": [orig_std, rev_std, act_price],
        })
        st.dataframe(proof.style.format({"Value": "{:,.1f}"}), use_container_width=True, hide_index=True)
        st.caption("Planning = (① − ②) × qty  •  Operational = (② − ③) × qty  •  Total = (① − ③) × qty")

    bridge = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "relative", "total"],
        x=["Std cost @ orig", "Planning var.", "Operational var.", "Actual cost"],
        y=[orig_std * act_qty, -planning_var, -operational_var, act_price * act_qty],
        text=[f"{orig_std*act_qty:,.0f}", f"{-planning_var:+,.0f}",
              f"{-operational_var:+,.0f}", f"{act_price*act_qty:,.0f}"],
        textposition="outside",
        connector={"line": {"color": "#b0b7bf"}},
        increasing={"marker": {"color": "#e67e22"}},
        decreasing={"marker": {"color": "#1e8449"}},
        totals={"marker": {"color": "#2e86de"}},
    ))
    bridge.update_layout(height=320, margin=dict(t=40, b=10), yaxis_title="BDT",
                         title="Original standard → Actual cost", plot_bgcolor="white")
    st.plotly_chart(bridge, use_container_width=True)

    st.markdown(
        f"""
**Interpretation:** {pl_i} **Planning {abs(planning_var):,.0f} BDT ({pl_w})** — caused by the standard
moving from {orig_std:,.1f} to a realistic {rev_std:,.1f}; this is **uncontrollable** and should not be
charged to the operational manager. {op_i} **Operational {abs(operational_var):,.0f} BDT ({op_w})** —
genuine performance: {act_price:,.1f} paid vs the fair revised standard {rev_std:,.1f}. **Judge the
manager on this figure only.**
        """
    )

# ==================================================================
# TAB 2 — MATERIALS MIX & YIELD
# ==================================================================
with tab_my:
    st.caption("Split the usage variance into mix and yield when inputs are substitutable. Edit the recipe below.")

    default = pd.DataFrame({
        "Input": ["Material A", "Material B", "Material C"],
        "Std mix %": [50.0, 30.0, 20.0],
        "Std price (BDT/kg)": [40.0, 60.0, 25.0],
        "Actual input (kg)": [10500.0, 5500.0, 4200.0],
    })
    data = st.data_editor(
        default, num_rows="dynamic", use_container_width=True, hide_index=True,
        column_config={
            "Std mix %": st.column_config.NumberColumn(format="%.1f", min_value=0.0),
            "Std price (BDT/kg)": st.column_config.NumberColumn(format="%.1f", min_value=0.0),
            "Actual input (kg)": st.column_config.NumberColumn(format="%.0f", min_value=0.0),
        },
    )

    std_output_input = st.number_input(
        "Standard total input for actual output (kg)",
        0.0, 100_000_000.0, 20000.0, step=100.0,
        help="The total quantity of input the standard recipe says should be needed for the actual output achieved.",
    )

    df = data.copy()
    df = df[df["Actual input (kg)"] >= 0].reset_index(drop=True)
    total_actual_input = df["Actual input (kg)"].sum()
    mix_frac = df["Std mix %"] / df["Std mix %"].sum() if df["Std mix %"].sum() else 0

    # Actual total input in STANDARD mix
    df["Actual @ std mix"] = mix_frac * total_actual_input
    # Standard input for output in standard mix
    df["Std input @ std mix"] = mix_frac * std_output_input

    # Mix variance: (actual@std mix - actual input) x std price  (positive = favourable)
    df["Mix variance"] = (df["Actual @ std mix"] - df["Actual input (kg)"]) * df["Std price (BDT/kg)"]
    # Yield variance: (std input@std mix - actual@std mix) x std price
    df["Yield variance"] = (df["Std input @ std mix"] - df["Actual @ std mix"]) * df["Std price (BDT/kg)"]
    # Usage check: (std input@std mix - actual input) x std price
    df["Usage variance"] = (df["Std input @ std mix"] - df["Actual input (kg)"]) * df["Std price (BDT/kg)"]

    mix_total = df["Mix variance"].sum()
    yield_total = df["Yield variance"].sum()
    usage_total = df["Usage variance"].sum()

    m_w, m_i = fav_adv(mix_total)
    y_w, y_i = fav_adv(yield_total)
    u_w, u_i = fav_adv(usage_total)

    st.markdown("#### 📊 Mix & Yield Result")
    a, b, c = st.columns(3)
    a.metric("Mix variance", f"{abs(mix_total):,.0f} BDT", f"{m_i} {m_w}", delta_color="off")
    b.metric("Yield variance", f"{abs(yield_total):,.0f} BDT", f"{y_i} {y_w}", delta_color="off")
    c.metric("= Usage variance", f"{abs(usage_total):,.0f} BDT", f"{u_i} {u_w}", delta_color="off")

    show = df[["Input", "Actual input (kg)", "Actual @ std mix", "Std input @ std mix",
               "Std price (BDT/kg)", "Mix variance", "Yield variance"]]
    st.dataframe(
        show.style.format({"Actual input (kg)": "{:,.0f}", "Actual @ std mix": "{:,.0f}",
                           "Std input @ std mix": "{:,.0f}", "Std price (BDT/kg)": "{:,.1f}",
                           "Mix variance": "{:,.0f}", "Yield variance": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )
    st.caption("Mix + Yield = Usage variance. Mix = blend effect; Yield = total-input productivity effect.")

    fig = go.Figure()
    fig.add_bar(name="Mix variance", x=df["Input"], y=df["Mix variance"], marker_color="#8e44ad")
    fig.add_bar(name="Yield variance", x=df["Input"], y=df["Yield variance"], marker_color="#16a085")
    fig.update_layout(barmode="group", height=320, margin=dict(t=30, b=10),
                      yaxis_title="BDT", legend=dict(orientation="h", y=1.2), plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

    if mix_total > 0 and yield_total < 0:
        st.warning(
            f"🔗 **Classic trade-off:** a **favourable mix ({mix_total:,.0f} BDT)** — a cheaper input "
            f"blend — coincides with an **adverse yield ({abs(yield_total):,.0f} BDT)**. The cheaper "
            f"recipe may be producing less output per kg of input. Check whether the mix saving is "
            f"real once the yield loss is netted off.",
            icon="⚠️",
        )
    elif yield_total > 0:
        st.success(
            f"**Favourable yield ({yield_total:,.0f} BDT).** The process converted input into output "
            f"more efficiently than the standard recipe expected.",
            icon="✅",
        )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — using advanced variances well</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 🎯 **Judge managers on operational variances only.** The planning variance reflects a flawed
  standard or a market shift — hold it separately so accountability stays fair.
- 🧪 **Never read mix without yield.** A favourable mix (cheaper blend) that causes an adverse
  yield (less output per input) can be a false economy — always net them together.
- ⚠️ **Beware manipulation.** Managers may argue an adverse result was a "planning" problem to
  escape blame. Revised standards must be **objective and evidence-based**, agreed independently.
- 🔁 **Update the standards.** A recurring planning variance is a signal to **rebase the standard**
  — feeding back into the next plan (the loop from Module 0).
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
        - [ ] **Planning** variance = flawed standard (uncontrollable); **Operational** = performance.
        - [ ] Judge the manager only on the **operational** variance vs. a **revised** standard.
        - [ ] Split usage into **mix + yield** when inputs are **substitutable**.
        - [ ] **Mix** = blend effect; **Yield** = output-per-input effect.
        - [ ] Always net **mix against yield** before celebrating a cheaper recipe.
        """
    )
with a2:
    with st.expander("📘 Key formulas in this module"):
        st.markdown(
            """
            **Planning / Operational**
            - Planning = (Original std − Revised std) × Actual qty
            - Operational = (Revised std − Actual) × Actual qty

            **Mix / Yield**
            - Mix = (Actual qty in std mix − Actual qty in actual mix) × Std price
            - Yield = (Std input for output − Actual total input, in std mix) × Std price
            - **Check:** Mix + Yield = Usage variance
            """
        )
    with st.expander("🧭 When to use each"):
        st.markdown(
            """
            - Use **planning/operational** when the original standard is genuinely out of date
              (market price shocks, revised methods) — not as a routine excuse.
            - Use **mix & yield** in **process industries** where inputs can be substituted
              (chemicals, food, feed, blended products).
            """
        )

# Downloadable combined summary
template = pd.DataFrame({
    "Variance": ["Planning", "Operational", "Total (planning+operational)",
                 "Materials mix", "Materials yield", "Usage (mix+yield)"],
    "Amount (BDT)": [planning_var, operational_var, total_var,
                     mix_total, yield_total, usage_total],
    "F/A": [fav_adv(planning_var)[0], fav_adv(operational_var)[0], fav_adv(total_var)[0],
            fav_adv(mix_total)[0], fav_adv(yield_total)[0], fav_adv(usage_total)[0]],
})
st.download_button(
    "⬇️ Download the advanced variance summary (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="advanced_variances.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 3.4 · Operating Statement & Reconciliation", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 4.1 · ROI & Residual Income ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 3.5")
