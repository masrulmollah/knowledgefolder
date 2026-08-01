"""
Performance Management — Applied Learning Series
Module 3.4 · Operating Statement & Reconciliation
------------------------------------------------------------
The capstone of variance analysis: assemble every variance (sales,
material, labour, variable & fixed overhead) into a formal operating
statement that reconciles BUDGETED profit to ACTUAL profit, and prove
the bridge ties out.

Run with:  streamlit run 3.4_Operating_Statement_and_Reconciliation.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="3.4 · Operating Statement & Reconciliation",
    page_icon="📑",
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
st.markdown('<p class="big-title">3.4 · Operating Statement & Reconciliation</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: bring <b>every variance together</b> into a formal operating statement '
    'that reconciles <b>budgeted profit to actual profit</b>, and prove that favourable and adverse '
    'variances bridge the two figures exactly.</p>',
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
An **operating statement** is the formal report that reconciles the **budgeted profit** to
the **actual profit** by listing every variance in between. It is the culmination of
variance analysis — the single page a manager reads to understand *why* profit differed
from plan.

**The structure (marginal costing basis):**

1. Start with **budgeted profit** (or budgeted contribution).
2. Add the **sales variances** (price, and volume valued at standard contribution) to get
   to the *actual sales, standard cost* contribution.
3. Deduct/add the **cost variances**:
   - Material — price and usage
   - Labour — rate and efficiency
   - Variable overhead — expenditure and efficiency
   - Fixed overhead — expenditure (and, under absorption, volume)
4. Arrive at **actual profit**.

**The golden rule:** Budgeted profit **+ Σ Favourable − Σ Adverse = Actual profit.**
If it doesn't tie out, a variance is missing or has the wrong sign.

Favourable variances **increase** profit above budget; adverse variances **reduce** it.
The operating statement makes the whole story auditable on one page.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "This is the report that goes to the factory leadership team. It converts a mass of "
        "individual variances into one clear narrative — how much of the profit gap came from "
        "selling, from buying, from producing — so management knows exactly where to act. "
        "Mastering it is the payoff of the whole variance module.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Operating Statement Builder
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Operating Statement Builder</p>',
            unsafe_allow_html=True)
st.caption("Enter budgeted & actual profit and each variance (positive = Favourable, negative = Adverse). "
           "The engine builds the operating statement and checks it reconciles.")

left, right = st.columns([1, 1.5])

with left:
    st.markdown("#### 🎛️ Anchor figures")
    budgeted_profit = st.number_input("Budgeted profit (BDT)", -1_000_000_000, 1_000_000_000,
                                      400_000, step=10_000)
    actual_profit   = st.number_input("Actual profit (BDT)", -1_000_000_000, 1_000_000_000,
                                      372_000, step=10_000)

    st.markdown("#### 🎛️ Variances  \n*(+ Favourable / − Adverse)*")
    sales_price = st.number_input("Sales price variance", -10_000_000, 10_000_000, -32_400, step=1000)
    sales_vol   = st.number_input("Sales volume variance", -10_000_000, 10_000_000, 32_000, step=1000)
    mat_price   = st.number_input("Material price variance", -10_000_000, 10_000_000, -42_000, step=1000)
    mat_usage   = st.number_input("Material usage variance", -10_000_000, 10_000_000, -50_000, step=1000)
    lab_rate    = st.number_input("Labour rate variance", -10_000_000, 10_000_000, 10_600, step=1000)
    lab_eff     = st.number_input("Labour efficiency variance", -10_000_000, 10_000_000, -36_000, step=1000)
    voh_exp     = st.number_input("Var. OH expenditure variance", -10_000_000, 10_000_000, 5_300, step=500)
    voh_eff     = st.number_input("Var. OH efficiency variance", -10_000_000, 10_000_000, -6_000, step=500)
    foh_exp     = st.number_input("Fixed OH expenditure variance", -10_000_000, 10_000_000, -12_000, step=1000)
    foh_vol     = st.number_input("Fixed OH volume variance", -10_000_000, 10_000_000, 0, step=1000)

# ---- Assemble ----
variances = [
    ("Sales price", sales_price),
    ("Sales volume", sales_vol),
    ("Material price", mat_price),
    ("Material usage", mat_usage),
    ("Labour rate", lab_rate),
    ("Labour efficiency", lab_eff),
    ("Variable OH expenditure", voh_exp),
    ("Variable OH efficiency", voh_eff),
    ("Fixed OH expenditure", foh_exp),
    ("Fixed OH volume", foh_vol),
]

total_variance = sum(v for _, v in variances)
reconciled_profit = budgeted_profit + total_variance
gap = actual_profit - reconciled_profit
total_fav = sum(v for _, v in variances if v > 0)
total_adv = sum(v for _, v in variances if v < 0)

def fa(v):
    if abs(v) < 1e-9:
        return "—"
    return "Favourable" if v > 0 else "Adverse"

with right:
    st.markdown("#### 📑 Operating Statement (Budget → Actual Profit)")

    rows = [{"Line": "Budgeted profit", "Favourable": "", "Adverse": "",
             "Running profit": budgeted_profit}]
    running = budgeted_profit
    for name, v in variances:
        running += v
        rows.append({
            "Line": name,
            "Favourable": f"{v:,.0f}" if v > 0 else "",
            "Adverse": f"{abs(v):,.0f}" if v < 0 else "",
            "Running profit": running,
        })
    rows.append({"Line": "= Actual profit (reconciled)", "Favourable": "", "Adverse": "",
                 "Running profit": reconciled_profit})
    stmt = pd.DataFrame(rows)
    st.dataframe(
        stmt.style.format({"Running profit": "{:,.0f}"}),
        use_container_width=True, hide_index=True, height=460,
    )

    s1, s2, s3 = st.columns(3)
    s1.metric("Σ Favourable", f"{total_fav:,.0f} BDT")
    s2.metric("Σ Adverse", f"{abs(total_adv):,.0f} BDT")
    s3.metric("Net variance", f"{total_variance:,.0f} BDT",
              "Favourable" if total_variance >= 0 else "Adverse",
              delta_color="normal" if total_variance >= 0 else "inverse")

st.divider()

# ---- Reconciliation waterfall ----
st.markdown("#### 💧 Profit Reconciliation Bridge")
wf_x = ["Budgeted profit"] + [n for n, _ in variances] + ["Actual profit"]
wf_y = [budgeted_profit] + [v for _, v in variances] + [reconciled_profit]
wf_measure = ["absolute"] + ["relative"] * len(variances) + ["total"]

wf = go.Figure(go.Waterfall(
    orientation="v",
    measure=wf_measure,
    x=wf_x,
    y=wf_y,
    text=[f"{budgeted_profit:,.0f}"] + [f"{v:+,.0f}" for _, v in variances] +
         [f"{reconciled_profit:,.0f}"],
    textposition="outside",
    connector={"line": {"color": "#b0b7bf"}},
    increasing={"marker": {"color": "#1e8449"}},   # favourable = green
    decreasing={"marker": {"color": "#e67e22"}},   # adverse = orange
    totals={"marker": {"color": "#2e86de"}},
))
wf.update_layout(height=440, margin=dict(t=30, b=90), yaxis_title="BDT",
                 xaxis_tickangle=-40, plot_bgcolor="white")
st.plotly_chart(wf, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

# Reconciliation check
if abs(gap) < 1e-6:
    st.success(
        f"**Reconciled exactly.** Budgeted profit {budgeted_profit:,.0f} + net variance "
        f"{total_variance:,.0f} = actual profit {reconciled_profit:,.0f}. The operating statement "
        f"ties out — every variance is accounted for.",
        icon="✅",
    )
else:
    st.error(
        f"**Does not reconcile — gap of {gap:,.0f} BDT.** Your entered actual profit "
        f"({actual_profit:,.0f}) differs from the reconciled figure ({reconciled_profit:,.0f}). "
        f"A variance is missing, double-counted, or has the wrong sign. Adjust until the gap is zero.",
        icon="🔴",
    )

# Biggest drivers
sorted_v = sorted(variances, key=lambda kv: kv[1])
worst = sorted_v[0]
best = sorted_v[-1]

st.markdown(
    f"""
- 📉 **Largest adverse driver:** **{worst[0]}** at **{abs(worst[1]):,.0f} BDT ({fa(worst[1])})** —
  the first place to investigate.
- 📈 **Largest favourable driver:** **{best[0]}** at **{abs(best[1]):,.0f} BDT ({fa(best[1])})** —
  understand it so it can be repeated.
- ⚖️ **Net effect:** profit moved **{total_variance:+,.0f} BDT** from budget, a
  **{(total_variance/budgeted_profit*100 if budgeted_profit else 0):+.1f}%** swing.
    """
)

# Interacting-variance nudge
if mat_price > 0 and mat_usage < 0:
    st.warning(
        "🔗 **Interacting variances spotted:** a favourable material *price* alongside an adverse "
        "material *usage* often means cheaper, lower-grade material caused extra waste. Read them "
        "together before judging procurement.",
        icon="🔗",
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
        - [ ] Start from **budgeted profit**, finish at **actual profit**.
        - [ ] **+ Favourable − Adverse** must bridge the two exactly.
        - [ ] Group variances logically: **sales → material → labour → overheads**.
        - [ ] A statement that doesn't reconcile has a **missing or mis-signed** variance.
        - [ ] Focus management attention on the **largest, most controllable** variances.
        """
    )
with a2:
    with st.expander("📘 The reconciliation identity"):
        st.markdown(
            """
            **Budgeted profit + Σ Favourable − Σ Adverse = Actual profit**

            Equivalently: Actual profit − Budgeted profit = Net variance.

            Under **marginal costing** the sales volume variance is valued at standard
            **contribution** and there is **no fixed OH volume variance**. Under **absorption
            costing**, volume is valued at standard **margin** and the fixed OH **volume**
            variance appears (as included above).
            """
        )
    with st.expander("🧭 How to present it to management"):
        st.markdown(
            """
            - Lead with the **headline**: budget vs. actual profit and the net gap.
            - Highlight the **two or three biggest drivers**, not all ten.
            - Pair each with a **cause and an owner**.
            - End with the **action** and the effect on the next plan (close the loop).
            """
        )

# Downloadable operating statement
export = pd.DataFrame(rows)[["Line", "Favourable", "Adverse", "Running profit"]]
st.download_button(
    "⬇️ Download the operating statement (CSV)",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="operating_statement_reconciliation.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 3.3 · Sales Variances", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 3.5 · Advanced Variances ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 3.4")
