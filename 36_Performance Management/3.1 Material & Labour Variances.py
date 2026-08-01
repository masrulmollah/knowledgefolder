"""
Performance Management — Applied Learning Series
Module 3.1 · Material & Labour Variances
------------------------------------------------------------
The core of variance analysis: decomposing the total cost variance
for direct materials and direct labour into their price/usage and
rate/efficiency components, and reconciling them back to the total.

Run with:  streamlit run 3.1_Material_and_Labour_Variances.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="3.1 · Material & Labour Variances",
    page_icon="🧮",
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
st.markdown('<p class="big-title">3.1 · Material & Labour Variances</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: decompose the total <b>direct material</b> and <b>direct labour</b> '
    'cost variances into their <b>price/rate</b> and <b>usage/efficiency</b> components, and prove they '
    'reconcile back to the total.</p>',
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
A **cost variance** is the difference between the *standard* (flexed to actual output) and
the *actual* cost. For direct materials and direct labour, the total variance splits into
two questions: **did we pay the expected price?** and **did we use the expected quantity?**

**Direct material variances**

- **Total material variance** = (Std qty for actual output × Std price) − (Actual qty × Actual price)
- **Price variance** = (Std price − Actual price) × Actual quantity
  *→ were materials cheaper/dearer than standard?*
- **Usage variance** = (Std qty for actual output − Actual qty) × Std price
  *→ did we use more/less material than the standard allowed?*

**Direct labour variances**

- **Total labour variance** = (Std hours for actual output × Std rate) − (Actual hours × Actual rate)
- **Rate variance** = (Std rate − Actual rate) × Actual hours
  *→ did we pay a higher/lower wage rate than standard?*
- **Efficiency variance** = (Std hours for actual output − Actual hours) × Std rate
  *→ did we work faster/slower than the standard time?*

**The golden reconciliation:** Price/Rate variance **+** Usage/Efficiency variance **=**
Total variance. If they don't add up, the arithmetic is wrong.

**Sign convention:** a variance is **Favourable (F)** when actual cost is *below* standard,
and **Adverse (A)** when actual cost is *above* standard.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Price and usage variances point to *different owners*: price/rate usually sits with "
        "procurement or HR, while usage/efficiency sits with the production line. Splitting the "
        "total tells you **where** to investigate and **who** can act — the essence of "
        "responsibility accounting on the factory floor.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Variance Engine</p>',
            unsafe_allow_html=True)

tab_mat, tab_lab = st.tabs(["🧱 Material Variances", "👷 Labour Variances"])

def fav_adv(v):
    """Return (word, icon) for a COST variance where positive = Favourable."""
    if abs(v) < 1e-9:
        return "—", "🟡"
    return ("Favourable", "🟢") if v > 0 else ("Adverse", "🔴")

# ==================================================================
# TAB 1 — MATERIAL VARIANCES
# ==================================================================
with tab_mat:
    st.caption("Enter the standard and actual data; the engine splits the total into price and usage variances.")

    ml, mr = st.columns([1, 1.5])
    with ml:
        st.markdown("#### 🎛️ Inputs")
        output_units = st.number_input("Actual output (units)", 1, 5_000_000, 10000, step=500,
                                       key="mat_out")
        std_qty_pu   = st.number_input("Standard material per unit (kg)", 0.0, 10000.0, 2.0, step=0.1,
                                       key="mat_stdqty")
        std_price    = st.number_input("Standard price per kg (BDT)", 0.0, 100000.0, 50.0, step=1.0,
                                       key="mat_stdprice")
        actual_qty   = st.number_input("Actual material used (kg)", 0.0, 100_000_000.0, 21000.0,
                                       step=100.0, key="mat_actqty")
        actual_price = st.number_input("Actual price per kg (BDT)", 0.0, 100000.0, 52.0, step=1.0,
                                       key="mat_actprice")

    # Standard quantity flexed to actual output
    std_qty_flexed = output_units * std_qty_pu

    # Variances (positive = favourable)
    price_var = (std_price - actual_price) * actual_qty
    usage_var = (std_qty_flexed - actual_qty) * std_price
    total_var = price_var + usage_var

    # Proof via cost columns
    std_cost_flexed = std_qty_flexed * std_price
    actual_cost     = actual_qty * actual_price

    p_word, p_icon = fav_adv(price_var)
    u_word, u_icon = fav_adv(usage_var)
    t_word, t_icon = fav_adv(total_var)

    with mr:
        st.markdown("#### 📊 Material Variance Result")
        a, b, c = st.columns(3)
        a.metric("Price variance", f"{abs(price_var):,.0f} BDT", f"{p_icon} {p_word}", delta_color="off")
        b.metric("Usage variance", f"{abs(usage_var):,.0f} BDT", f"{u_icon} {u_word}", delta_color="off")
        c.metric("Total variance", f"{abs(total_var):,.0f} BDT", f"{t_icon} {t_word}", delta_color="off")

        proof = pd.DataFrame({
            "Cost column": ["① Std qty × Std price (flexed)",
                            "② Actual qty × Std price",
                            "③ Actual qty × Actual price"],
            "BDT": [std_cost_flexed, actual_qty * std_price, actual_cost],
        })
        st.dataframe(proof.style.format({"BDT": "{:,.0f}"}), use_container_width=True, hide_index=True)
        st.caption("Usage = ① − ②  •  Price = ② − ③  •  Total = ① − ③")

    # Bridge chart
    bridge = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "relative", "total"],
        x=["Std cost (flexed)", "Usage var.", "Price var.", "Actual cost"],
        y=[std_cost_flexed, -usage_var, -price_var, actual_cost],
        text=[f"{std_cost_flexed:,.0f}", f"{-usage_var:+,.0f}",
              f"{-price_var:+,.0f}", f"{actual_cost:,.0f}"],
        textposition="outside",
        connector={"line": {"color": "#b0b7bf"}},
        increasing={"marker": {"color": "#e67e22"}},
        decreasing={"marker": {"color": "#1e8449"}},
        totals={"marker": {"color": "#2e86de"}},
    ))
    bridge.update_layout(height=340, margin=dict(t=40, b=10), yaxis_title="BDT",
                         title="Standard → Actual cost bridge", plot_bgcolor="white")
    st.plotly_chart(bridge, use_container_width=True)

    st.markdown(
        f"""
**Interpretation:** Against a flexed standard cost of **{std_cost_flexed:,.0f} BDT**, actual spend was
**{actual_cost:,.0f} BDT**.
- {p_icon} **Price variance {abs(price_var):,.0f} BDT ({p_word})** — actual price was
  {actual_price:,.1f} vs standard {std_price:,.1f} per kg (owner: *procurement*).
- {u_icon} **Usage variance {abs(usage_var):,.0f} BDT ({u_word})** — used {actual_qty:,.0f} kg vs the
  {std_qty_flexed:,.0f} kg the standard allowed for {output_units:,} units (owner: *production*).
        """
    )

# ==================================================================
# TAB 2 — LABOUR VARIANCES
# ==================================================================
with tab_lab:
    st.caption("Enter the standard and actual data; the engine splits the total into rate and efficiency variances.")

    ll, lr = st.columns([1, 1.5])
    with ll:
        st.markdown("#### 🎛️ Inputs")
        l_output   = st.number_input("Actual output (units)", 1, 5_000_000, 10000, step=500,
                                     key="lab_out")
        std_hr_pu  = st.number_input("Standard hours per unit", 0.0, 10000.0, 0.5, step=0.05,
                                     key="lab_stdhr")
        std_rate   = st.number_input("Standard rate per hour (BDT)", 0.0, 100000.0, 120.0, step=5.0,
                                     key="lab_stdrate")
        actual_hrs = st.number_input("Actual hours worked", 0.0, 100_000_000.0, 5300.0, step=50.0,
                                     key="lab_acthr")
        actual_rate = st.number_input("Actual rate per hour (BDT)", 0.0, 100000.0, 118.0, step=5.0,
                                      key="lab_actrate")

    std_hrs_flexed = l_output * std_hr_pu

    rate_var = (std_rate - actual_rate) * actual_hrs
    eff_var  = (std_hrs_flexed - actual_hrs) * std_rate
    l_total  = rate_var + eff_var

    std_labour_flexed = std_hrs_flexed * std_rate
    actual_labour     = actual_hrs * actual_rate

    r_word, r_icon = fav_adv(rate_var)
    e_word, e_icon = fav_adv(eff_var)
    lt_word, lt_icon = fav_adv(l_total)

    with lr:
        st.markdown("#### 📊 Labour Variance Result")
        a, b, c = st.columns(3)
        a.metric("Rate variance", f"{abs(rate_var):,.0f} BDT", f"{r_icon} {r_word}", delta_color="off")
        b.metric("Efficiency variance", f"{abs(eff_var):,.0f} BDT", f"{e_icon} {e_word}", delta_color="off")
        c.metric("Total variance", f"{abs(l_total):,.0f} BDT", f"{lt_icon} {lt_word}", delta_color="off")

        proof = pd.DataFrame({
            "Cost column": ["① Std hrs × Std rate (flexed)",
                            "② Actual hrs × Std rate",
                            "③ Actual hrs × Actual rate"],
            "BDT": [std_labour_flexed, actual_hrs * std_rate, actual_labour],
        })
        st.dataframe(proof.style.format({"BDT": "{:,.0f}"}), use_container_width=True, hide_index=True)
        st.caption("Efficiency = ① − ②  •  Rate = ② − ③  •  Total = ① − ③")

    bridge = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "relative", "total"],
        x=["Std cost (flexed)", "Efficiency var.", "Rate var.", "Actual cost"],
        y=[std_labour_flexed, -eff_var, -rate_var, actual_labour],
        text=[f"{std_labour_flexed:,.0f}", f"{-eff_var:+,.0f}",
              f"{-rate_var:+,.0f}", f"{actual_labour:,.0f}"],
        textposition="outside",
        connector={"line": {"color": "#b0b7bf"}},
        increasing={"marker": {"color": "#e67e22"}},
        decreasing={"marker": {"color": "#1e8449"}},
        totals={"marker": {"color": "#2e86de"}},
    ))
    bridge.update_layout(height=340, margin=dict(t=40, b=10), yaxis_title="BDT",
                         title="Standard → Actual cost bridge", plot_bgcolor="white")
    st.plotly_chart(bridge, use_container_width=True)

    st.markdown(
        f"""
**Interpretation:** Against a flexed standard labour cost of **{std_labour_flexed:,.0f} BDT**, actual
labour cost was **{actual_labour:,.0f} BDT**.
- {r_icon} **Rate variance {abs(rate_var):,.0f} BDT ({r_word})** — actual rate {actual_rate:,.1f} vs
  standard {std_rate:,.1f} per hour (owner: *HR / payroll*).
- {e_icon} **Efficiency variance {abs(eff_var):,.0f} BDT ({e_word})** — took {actual_hrs:,.0f} hrs vs the
  {std_hrs_flexed:,.0f} hrs allowed for {l_output:,} units (owner: *production supervision*).
        """
    )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — linked causes
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — reading the story behind the numbers</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 🔗 **Variances interact — never read them in isolation.** A *favourable material price*
  variance from buying cheap, low-grade material often causes an *adverse material usage*
  variance (more waste) and even *adverse labour efficiency* (slower to work with).
- 🧭 **Trace to a root cause and an owner.** Price/rate variances usually sit with procurement
  or HR; usage/efficiency with the production line. That is why we split them.
- ⚖️ **Judge materiality, not just sign.** Investigate variances that are large in value or
  percentage — small adverse variances may not be worth the cost of investigation.
- 🔁 **Close the loop.** Feed the causes back into revised standards and the next plan — the
  Plan → Measure → Evaluate → Act cycle from Module 0.
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
        - [ ] Always **flex the standard** to actual output before comparing.
        - [ ] **Price/Rate** = based on *actual quantity/hours*; **Usage/Efficiency** = valued at *standard price/rate*.
        - [ ] Price/Rate **+** Usage/Efficiency **must equal** the total variance.
        - [ ] **F** = actual below standard; **A** = actual above standard.
        - [ ] Link interacting variances to a **root cause** and a **responsible owner**.
        """
    )
with a2:
    with st.expander("📘 Key formulas in this module"):
        st.markdown(
            """
            **Materials**
            - Price = (Std price − Actual price) × Actual qty
            - Usage = (Std qty for output − Actual qty) × Std price

            **Labour**
            - Rate = (Std rate − Actual rate) × Actual hours
            - Efficiency = (Std hrs for output − Actual hrs) × Std rate

            **Both:** Price/Rate + Usage/Efficiency = Total variance
            """
        )
    with st.expander("🔗 Classic interacting-variance example"):
        st.markdown(
            """
            Buying **cheaper material** → *favourable price* variance, but if it is lower
            quality it causes **more waste** (*adverse usage*) and is **slower to process**
            (*adverse labour efficiency*). The favourable price may be more than offset — which
            is why variances must be read together.
            """
        )

# Downloadable combined result
template = pd.DataFrame({
    "Variance": ["Material price", "Material usage", "Material total",
                 "Labour rate", "Labour efficiency", "Labour total"],
    "Amount (BDT)": [price_var, usage_var, total_var, rate_var, eff_var, l_total],
    "F/A": [fav_adv(price_var)[0], fav_adv(usage_var)[0], fav_adv(total_var)[0],
            fav_adv(rate_var)[0], fav_adv(eff_var)[0], fav_adv(l_total)[0]],
})
st.download_button(
    "⬇️ Download the material & labour variance summary (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="material_labour_variances.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 2.4 · Behavioural Aspects of Budgeting", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 3.2 · Overhead Variances ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 3.1")
