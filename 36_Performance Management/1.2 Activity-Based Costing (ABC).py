"""
Performance Management — Applied Learning Series
Module 1.2 · Activity-Based Costing (ABC)
------------------------------------------------------------
See how ABC traces overhead through ACTIVITIES and COST DRIVERS,
and how it exposes the cross-subsidisation hidden by a single
volume-based absorption rate.

Run with:  streamlit run 1.2_Activity_Based_Costing.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="1.2 · Activity-Based Costing (ABC)",
    page_icon="🧮",
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
st.markdown('<p class="big-title">1.2 · Activity-Based Costing (ABC)</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand how ABC assigns overhead via <b>activities</b> and '
    '<b>cost drivers</b>, and how it reveals the <b>cross-subsidisation</b> that a single '
    'volume-based rate hides between high- and low-volume products.</p>',
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
Traditional absorption costing spreads **all** overhead using one volume-based rate
(labour hours, machine hours). That is fine when overhead really is driven by volume —
but modern overhead (set-ups, inspections, order handling) often is **not**.

**Activity-Based Costing** works in four steps:

1. **Identify activities** that consume resources (e.g., machine set-ups, quality inspections).
2. **Pool the cost** of each activity (the activity cost pool).
3. **Pick a cost driver** — the factor that *causes* that cost (number of set-ups, inspections).
4. **Charge products** by how much of each driver they actually consume.

**Why it changes the answer:**

> A single volume rate over-costs **high-volume simple** products and under-costs
> **low-volume complex** products. ABC corrects this **cross-subsidy**.

Cost drivers sit at different levels: **unit**, **batch**, **product**, and **facility** —
the *cost hierarchy*. ABC is most powerful for the batch- and product-level costs that
volume-based rates smear indiscriminately.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Get product costs wrong and you misprice, mis-rank profitability, and chase the wrong "
        "mix. In a multi-SKU factory, ABC often reveals that a 'star' high-volume line is less "
        "profitable — and a niche line more profitable — than the volume rate suggested.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — Traditional vs. ABC</p>',
            unsafe_allow_html=True)
st.caption("Two products share the same overhead pools. Compare a single volume-based rate against "
           "driver-based ABC and watch the cross-subsidy appear.")

st.markdown("#### 🎛️ Product & activity inputs")
colP, colA = st.columns([1, 1.25])

with colP:
    st.markdown("**Product volumes & prime cost**")
    prod_df = pd.DataFrame({
        "Product": ["A · High volume", "B · Low volume"],
        "Units": [10000, 2000],
        "Machine hrs/unit": [0.5, 0.5],
        "Prime cost/unit": [30.0, 45.0],
        "Selling price/unit": [60.0, 95.0],
    })
    prod_edit = st.data_editor(
        prod_df, hide_index=True, use_container_width=True,
        column_config={
            "Units": st.column_config.NumberColumn(min_value=0, step=100),
            "Machine hrs/unit": st.column_config.NumberColumn(min_value=0.0, step=0.1, format="%.2f"),
            "Prime cost/unit": st.column_config.NumberColumn(min_value=0.0, step=1.0, format="%.2f"),
            "Selling price/unit": st.column_config.NumberColumn(min_value=0.0, step=1.0, format="%.2f"),
        },
        key="prod_editor",
    )

with colA:
    st.markdown("**Activity cost pools & driver usage**")
    act_df = pd.DataFrame({
        "Activity": ["Machine running", "Machine set-ups", "Quality inspection", "Order handling"],
        "Pool cost": [200000, 120000, 90000, 60000],
        "Driver": ["Machine hours", "Number of set-ups", "Number of inspections", "Number of orders"],
        "A usage": [5000, 20, 40, 50],
        "B usage": [1000, 80, 160, 150],
    })
    act_edit = st.data_editor(
        act_df, hide_index=True, use_container_width=True,
        column_config={
            "Pool cost": st.column_config.NumberColumn(min_value=0, step=1000),
            "A usage": st.column_config.NumberColumn(min_value=0, step=5),
            "B usage": st.column_config.NumberColumn(min_value=0, step=5),
        },
        key="act_editor",
    )

# ---- Clean inputs ----
prod_edit = prod_edit.fillna(0)
act_edit  = act_edit.fillna(0)

units      = prod_edit["Units"].to_numpy(dtype=float)
mhr_unit   = prod_edit["Machine hrs/unit"].to_numpy(dtype=float)
prime      = prod_edit["Prime cost/unit"].to_numpy(dtype=float)
price      = prod_edit["Selling price/unit"].to_numpy(dtype=float)
names      = prod_edit["Product"].tolist()

total_oh   = act_edit["Pool cost"].sum()
total_mhrs = float((units * mhr_unit).sum())

# ---- TRADITIONAL: single machine-hour rate ----
trad_rate  = total_oh / total_mhrs if total_mhrs else 0        # OH per machine hour
trad_oh_unit = mhr_unit * trad_rate                            # per unit, per product
trad_total_cost_unit = prime + trad_oh_unit

# ---- ABC: driver rate per activity, charged by usage ----
a_usage = act_edit["A usage"].to_numpy(dtype=float)
b_usage = act_edit["B usage"].to_numpy(dtype=float)
pool    = act_edit["Pool cost"].to_numpy(dtype=float)
tot_usage = a_usage + b_usage
driver_rate = np.divide(pool, tot_usage, out=np.zeros_like(pool), where=tot_usage != 0)

abc_oh_A = float((driver_rate * a_usage).sum())
abc_oh_B = float((driver_rate * b_usage).sum())
abc_oh_total_unit = np.array([
    abc_oh_A / units[0] if units[0] else 0,
    abc_oh_B / units[1] if units[1] else 0,
])
abc_total_cost_unit = prime + abc_oh_total_unit

# ------------------------------------------------------------------
# Results tables
# ------------------------------------------------------------------
st.markdown("#### 📊 Overhead per unit — Traditional vs. ABC")

res = pd.DataFrame({
    "Product": names,
    "Prime cost/u": prime,
    "OH/u (Traditional)": np.round(trad_oh_unit, 2),
    "OH/u (ABC)": np.round(abc_oh_total_unit, 2),
    "Total cost/u (Trad)": np.round(trad_total_cost_unit, 2),
    "Total cost/u (ABC)": np.round(abc_total_cost_unit, 2),
    "Δ cost/u (ABC−Trad)": np.round(abc_total_cost_unit - trad_total_cost_unit, 2),
})
st.dataframe(res, hide_index=True, use_container_width=True)

colL, colR = st.columns([1.1, 1])
with colL:
    fig = go.Figure()
    fig.add_bar(name="Traditional", x=names, y=np.round(trad_oh_unit, 2), marker_color="#95a5a6")
    fig.add_bar(name="ABC", x=names, y=np.round(abc_oh_total_unit, 2), marker_color="#2e86de")
    fig.update_layout(barmode="group", height=320, margin=dict(t=30, b=10),
                      title="Overhead per unit", yaxis_title="BDT/unit",
                      legend=dict(orientation="h", y=1.2))
    st.plotly_chart(fig, use_container_width=True)

with colR:
    st.markdown("**Driver rates (ABC)**")
    rate_df = pd.DataFrame({
        "Activity": act_edit["Activity"],
        "Driver": act_edit["Driver"],
        "Rate/driver": np.round(driver_rate, 2),
    })
    st.dataframe(rate_df, hide_index=True, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

# Margins under each method
trad_margin = price - trad_total_cost_unit
abc_margin  = price - abc_total_cost_unit

shift_A = abc_total_cost_unit[0] - trad_total_cost_unit[0]
shift_B = abc_total_cost_unit[1] - trad_total_cost_unit[1]

st.markdown(
    f"""
- **{names[0]}:** cost/unit moves **{shift_A:+.2f} BDT** under ABC → margin goes from **{trad_margin[0]:.2f}** to **{abc_margin[0]:.2f}**.
- **{names[1]}:** cost/unit moves **{shift_B:+.2f} BDT** under ABC → margin goes from **{trad_margin[1]:.2f}** to **{abc_margin[1]:.2f}**.
    """
)

if shift_A < -0.01 and shift_B > 0.01:
    st.warning(
        f"**Cross-subsidy exposed →** The single volume rate was **over-costing the high-volume "
        f"product ({names[0]})** and **under-costing the low-volume product ({names[1]})**. ABC "
        f"shifts **{abs(shift_A)*units[0]:,.0f} BDT** of overhead off A and onto B, because B "
        f"consumes disproportionately more set-ups, inspections and orders per unit. Re-check B's "
        f"pricing — it may be far less profitable than the traditional system suggested.",
        icon="⚠️",
    )
elif abs(shift_A) < 0.01 and abs(shift_B) < 0.01:
    st.success(
        "**No cross-subsidy →** Both products consume drivers in the same proportion as machine "
        "hours, so ABC and the volume rate agree. ABC adds little here — its value appears only "
        "when driver consumption diverges from volume.",
        icon="✅",
    )
else:
    st.info(
        "**Costs have been re-routed →** ABC has reallocated overhead based on actual driver "
        "consumption. Compare the new margins before setting prices or product-mix strategy.",
        icon="🧠",
    )

st.info(
    "**Cost hierarchy reminder:** unit-level costs track volume; **batch-level** (set-ups, "
    "inspections) track *number of batches*; **product-level** costs track product existence. "
    "ABC shines wherever costs are driven by anything other than pure volume.",
    icon="🧩",
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
        - [ ] List activities → pool costs → pick the **driver that causes** each cost.
        - [ ] Charge products by **actual driver consumption**, not volume.
        - [ ] Expect **high-volume simple** products to get *cheaper*, **low-volume complex** dearer.
        - [ ] Map costs to the **hierarchy**: unit / batch / product / facility.
        - [ ] Use ABC to fix **pricing, mix and profitability** decisions — not just reporting.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Activity** — a task that consumes resources (e.g., a set-up).
            - **Cost pool** — the total cost gathered for one activity.
            - **Cost driver** — the factor causing the cost (e.g., number of set-ups).
            - **Driver rate** — pool cost ÷ total driver quantity.
            - **Cross-subsidy** — one product's cost wrongly carried by another.
            - **Cost hierarchy** — unit / batch / product / facility-level costs.
            """
        )

# Downloadable template
out = res.copy()
out["Margin/u (Trad)"] = np.round(trad_margin, 2)
out["Margin/u (ABC)"]  = np.round(abc_margin, 2)
st.download_button(
    "⬇️ Download the ABC vs. Traditional comparison (CSV)",
    data=out.to_csv(index=False).encode("utf-8"),
    file_name="abc_vs_traditional.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 1.1 · Absorption vs. Marginal Costing", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 1.3 · Cost Behaviour & CVP ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 1.2")
