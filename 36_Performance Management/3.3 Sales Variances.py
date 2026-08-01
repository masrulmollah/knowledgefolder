"""
Performance Management — Applied Learning Series
Module 3.3 · Sales Variances
------------------------------------------------------------
The revenue side of variance analysis:
  • Sales price variance
  • Sales volume variance (valued at standard contribution/margin)
  • For multi-product firms: volume split into MIX + QUANTITY
All reconciled back to the total sales variance.

Run with:  streamlit run 3.3_Sales_Variances.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="3.3 · Sales Variances",
    page_icon="💹",
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
st.markdown('<p class="big-title">3.3 · Sales Variances</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: measure the <b>sales price</b> and <b>sales volume</b> variances, and — '
    'for multi-product businesses — split volume into the <b>mix</b> and <b>quantity</b> components, all '
    'valued at standard contribution or margin.</p>',
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
Sales variances explain why actual sales performance differs from budget. Crucially, the
**volume effect is valued at standard contribution (marginal costing) or standard profit
margin (absorption costing)** — *not* at selling price — because selling one more unit only
adds its contribution, not its full price.

**Sales price variance** = (Actual price − Standard price) × Actual units sold
*→ did we sell at a higher/lower price than budgeted?*

**Sales volume variance** = (Actual units − Budgeted units) × Standard contribution per unit
*→ did we sell more/fewer units than budgeted?*

For a business selling **several products**, the volume variance splits further:

- **Sales mix variance** = (Actual units in actual mix − Actual units in budgeted mix)
  × Standard contribution per unit
  *→ did we sell a richer or poorer blend of products than planned?*
- **Sales quantity variance** = (Actual total units in budget mix − Budgeted units)
  × Standard contribution per unit
  *→ did the total market volume we captured rise or fall?*

**Reconciliation:** Mix + Quantity = Volume variance; Price + Volume = Total sales variance.
**F** = better than budget; **A** = worse than budget.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Sales variances are where commercial and finance meet. Valuing volume at **contribution** "
        "stops a sales team from being credited with 'revenue' that carries no margin, and the "
        "**mix** variance reveals whether the team is pushing high-margin lines or chasing volume "
        "in low-margin ones — a decisive insight for a multi-SKU factory.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Sales Variance Engine</p>',
            unsafe_allow_html=True)

def fav_adv(v):
    """Return (word, icon) for a SALES variance where positive = Favourable."""
    if abs(v) < 1e-9:
        return "—", "🟡"
    return ("Favourable", "🟢") if v > 0 else ("Adverse", "🔴")

tab_basic, tab_mix = st.tabs(["💰 Price & Volume (single product)", "🧩 Mix & Quantity (multi-product)"])

# ==================================================================
# TAB 1 — PRICE & VOLUME
# ==================================================================
with tab_basic:
    st.caption("Split the total sales variance into price and volume, with volume valued at standard contribution.")

    bl, br = st.columns([1, 1.5])
    with bl:
        st.markdown("#### 🎛️ Inputs")
        bud_units  = st.number_input("Budgeted sales (units)", 0, 5_000_000, 10000, step=500, key="b_bud")
        act_units  = st.number_input("Actual sales (units)", 0, 5_000_000, 10800, step=500, key="b_act")
        std_price  = st.number_input("Standard selling price (BDT)", 0.0, 100000.0, 100.0, step=1.0, key="b_sp")
        act_price  = st.number_input("Actual selling price (BDT)", 0.0, 100000.0, 97.0, step=1.0, key="b_ap")
        std_vcost  = st.number_input("Standard variable cost/unit (BDT)", 0.0, 100000.0, 60.0, step=1.0, key="b_vc")

    std_contrib = std_price - std_vcost

    price_var  = (act_price - std_price) * act_units
    volume_var = (act_units - bud_units) * std_contrib
    total_var  = price_var + volume_var

    p_word, p_icon = fav_adv(price_var)
    v_word, v_icon = fav_adv(volume_var)
    t_word, t_icon = fav_adv(total_var)

    with br:
        st.markdown("#### 📊 Sales Variance Result")
        a, b, c = st.columns(3)
        a.metric("Price variance", f"{abs(price_var):,.0f} BDT", f"{p_icon} {p_word}", delta_color="off")
        b.metric("Volume variance", f"{abs(volume_var):,.0f} BDT", f"{v_icon} {v_word}", delta_color="off")
        c.metric("Total sales var.", f"{abs(total_var):,.0f} BDT", f"{t_icon} {t_word}", delta_color="off")

        st.caption(f"Standard contribution per unit: **{std_contrib:,.1f} BDT** "
                   f"(price {std_price:,.1f} − variable cost {std_vcost:,.1f})")

    bridge = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "relative", "total"],
        x=["Budget contribution", "Volume var.", "Price var.", "Actual contribution"],
        y=[bud_units * std_contrib, volume_var, price_var,
           bud_units * std_contrib + volume_var + price_var],
        text=[f"{bud_units*std_contrib:,.0f}", f"{volume_var:+,.0f}",
              f"{price_var:+,.0f}", f"{bud_units*std_contrib+total_var:,.0f}"],
        textposition="outside",
        connector={"line": {"color": "#b0b7bf"}},
        increasing={"marker": {"color": "#1e8449"}},
        decreasing={"marker": {"color": "#e67e22"}},
        totals={"marker": {"color": "#2e86de"}},
    ))
    bridge.update_layout(height=340, margin=dict(t=40, b=10), yaxis_title="BDT",
                         title="Budget → Actual contribution bridge", plot_bgcolor="white")
    st.plotly_chart(bridge, use_container_width=True)

    st.markdown(
        f"""
**Interpretation:** {p_icon} **Price {abs(price_var):,.0f} BDT ({p_word})** — sold at {act_price:,.1f}
vs standard {std_price:,.1f} across {act_units:,} units. {v_icon} **Volume {abs(volume_var):,.0f} BDT
({v_word})** — sold {act_units:,} vs budget {bud_units:,} units, each worth {std_contrib:,.1f} of
standard contribution.
        """
    )

# ==================================================================
# TAB 2 — MIX & QUANTITY
# ==================================================================
with tab_mix:
    st.caption("For multi-product sales, split the volume variance into mix and quantity. Edit the product table below.")

    default = pd.DataFrame({
        "Product": ["Soap", "Shampoo", "Toothpaste"],
        "Budget units": [5000, 3000, 2000],
        "Actual units": [4800, 3600, 2400],
        "Std contribution/unit (BDT)": [30.0, 45.0, 25.0],
    })
    data = st.data_editor(
        default, num_rows="dynamic", use_container_width=True, hide_index=True,
        column_config={
            "Budget units": st.column_config.NumberColumn(format="%d", min_value=0),
            "Actual units": st.column_config.NumberColumn(format="%d", min_value=0),
            "Std contribution/unit (BDT)": st.column_config.NumberColumn(format="%.1f", min_value=0.0),
        },
    )

    df = data.copy()
    df = df[(df["Budget units"] + df["Actual units"]) > 0].reset_index(drop=True)

    bud_total = df["Budget units"].sum()
    act_total = df["Actual units"].sum()

    # Budgeted mix proportions
    df["Budget mix %"] = df["Budget units"] / bud_total if bud_total else 0
    # Actual units restated in budget mix (same total actual units, budgeted proportions)
    df["Actual @ budget mix"] = df["Budget mix %"] * act_total

    # Mix variance: (actual units - actual total in budget mix) x std contribution
    df["Mix variance"] = (df["Actual units"] - df["Actual @ budget mix"]) * df["Std contribution/unit (BDT)"]
    # Quantity variance: (actual total in budget mix - budget units) x std contribution
    df["Quantity variance"] = (df["Actual @ budget mix"] - df["Budget units"]) * df["Std contribution/unit (BDT)"]
    # Volume variance check
    df["Volume variance"] = (df["Actual units"] - df["Budget units"]) * df["Std contribution/unit (BDT)"]

    mix_total = df["Mix variance"].sum()
    qty_total = df["Quantity variance"].sum()
    vol_total = df["Volume variance"].sum()

    m_word, m_icon = fav_adv(mix_total)
    q_word, q_icon = fav_adv(qty_total)
    vt_word, vt_icon = fav_adv(vol_total)

    st.markdown("#### 📊 Mix & Quantity Result")
    a, b, c = st.columns(3)
    a.metric("Sales mix variance", f"{abs(mix_total):,.0f} BDT", f"{m_icon} {m_word}", delta_color="off")
    b.metric("Sales quantity variance", f"{abs(qty_total):,.0f} BDT", f"{q_icon} {q_word}", delta_color="off")
    c.metric("= Volume variance", f"{abs(vol_total):,.0f} BDT", f"{vt_icon} {vt_word}", delta_color="off")

    show = df[["Product", "Budget units", "Actual units", "Actual @ budget mix",
               "Std contribution/unit (BDT)", "Mix variance", "Quantity variance"]]
    st.dataframe(
        show.style.format({"Budget units": "{:,.0f}", "Actual units": "{:,.0f}",
                           "Actual @ budget mix": "{:,.0f}",
                           "Std contribution/unit (BDT)": "{:,.1f}",
                           "Mix variance": "{:,.0f}", "Quantity variance": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )
    st.caption("Mix + Quantity = Volume variance. Mix shows the blend effect; Quantity shows the total-volume effect.")

    # Per-product mix contribution chart
    fig = go.Figure()
    fig.add_bar(name="Mix variance", x=df["Product"], y=df["Mix variance"], marker_color="#8e44ad")
    fig.add_bar(name="Quantity variance", x=df["Product"], y=df["Quantity variance"], marker_color="#16a085")
    fig.update_layout(barmode="group", height=320, margin=dict(t=30, b=10),
                      yaxis_title="BDT", legend=dict(orientation="h", y=1.2), plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

    if mix_total > 0:
        st.success(
            f"**Favourable mix ({mix_total:,.0f} BDT).** The actual sales blend was richer than budgeted "
            f"— more of the higher-contribution products were sold. The team improved profitability "
            f"through product mix, not just volume.",
            icon="✅",
        )
    elif mix_total < 0:
        st.warning(
            f"**Adverse mix ({abs(mix_total):,.0f} BDT).** The actual blend was poorer than budgeted — "
            f"proportionally more low-contribution product was sold. Investigate whether discounting or "
            f"demand shifted the mix toward weaker margins.",
            icon="⚠️",
        )
    else:
        st.info("Neutral mix — the actual blend matched the budgeted proportions.", icon="🟡")

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — reading the commercial story</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 💰 **Price vs. volume is a classic trade-off.** A favourable volume variance driven by an
  adverse price variance may just be **discounting to shift units** — check whether total
  contribution actually improved.
- 🧩 **Mix reveals sales-force behaviour.** A favourable quantity but adverse mix means the team
  sold *more in total* but skewed toward **low-margin** products — volume without value.
- 📉 **Value volume at contribution, never at price.** Crediting sales at full selling price
  overstates the benefit of extra units and hides margin erosion.
- 🔁 **Close the loop.** Feed mix and price findings back into targets, incentives and the next
  sales budget — the Plan → Measure → Evaluate → Act cycle from Module 0.
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
        - [ ] Value the **volume** variance at **standard contribution/margin**, not price.
        - [ ] **Price** variance uses **actual units**; **volume** uses **standard contribution**.
        - [ ] For multi-product firms, split volume into **mix + quantity**.
        - [ ] **Mix** = blend effect; **Quantity** = total-volume effect.
        - [ ] Watch the **price-vs-volume** and **mix-vs-quantity** trade-offs together.
        """
    )
with a2:
    with st.expander("📘 Key formulas in this module"):
        st.markdown(
            """
            - **Price** = (Actual price − Std price) × Actual units
            - **Volume** = (Actual units − Budget units) × Std contribution
            - **Mix** = (Actual units − Actual total in budget mix) × Std contribution
            - **Quantity** = (Actual total in budget mix − Budget units) × Std contribution
            - **Check:** Mix + Quantity = Volume; Price + Volume = Total
            """
        )
    with st.expander("🧭 Marginal vs. absorption note"):
        st.markdown(
            """
            Under **marginal costing**, value the volume variance at **standard contribution**.
            Under **absorption costing**, value it at **standard profit margin** (contribution
            less absorbed fixed overhead per unit). The method changes the *rate*, not the logic.
            """
        )

# Downloadable summary (basic tab result)
template = pd.DataFrame({
    "Variance": ["Sales price", "Sales volume", "Total sales",
                 "Sales mix (multi-product)", "Sales quantity (multi-product)"],
    "Amount (BDT)": [price_var, volume_var, total_var, mix_total, qty_total],
    "F/A": [fav_adv(price_var)[0], fav_adv(volume_var)[0], fav_adv(total_var)[0],
            fav_adv(mix_total)[0], fav_adv(qty_total)[0]],
})
st.download_button(
    "⬇️ Download the sales variance summary (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="sales_variances.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 3.2 · Overhead Variances", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 3.4 · Operating Statement & Reconciliation ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 3.3")
