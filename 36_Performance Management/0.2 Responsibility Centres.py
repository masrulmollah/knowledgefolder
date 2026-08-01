"""
Performance Management — Applied Learning Series
Module 0.2 · Responsibility Centres
------------------------------------------------------------
Understand the four responsibility centres — Cost, Revenue, Profit,
Investment — and how the manager's accountability (and the right
performance measure) changes with each.

Run with:  streamlit run 0.2_Responsibility_Centres.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="0.2 · Responsibility Centres",
    page_icon="🏢",
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
                      background:#fafcff; height:100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# ① HEADER ZONE
# ------------------------------------------------------------------
st.markdown('<p class="pill">MODULE 0 · FOUNDATIONS</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">0.2 · Responsibility Centres</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand the four types of responsibility centre — '
    '<b>Cost, Revenue, Profit, Investment</b> — and match each to the <b>right performance '
    'measure</b> based on what the manager can actually control.</p>',
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
A **responsibility centre** is a unit of an organisation whose manager is held accountable
for a specific set of financial outcomes. The golden rule of performance management is:

> **A manager should only be judged on what they can control.**

The four centres form a ladder of increasing responsibility:

| Centre | Manager controls… | Judged on… | Typical example |
|--------|------------------|-----------|-----------------|
| **Cost** | Costs only | Cost efficiency / variances | Factory production dept. |
| **Revenue** | Revenue only | Sales vs. target | Regional sales team |
| **Profit** | Costs **and** revenue | Profit / margin | A product division |
| **Investment** | Costs, revenue **and** capital | ROI / RI / EVA | A strategic business unit |

As you climb the ladder, the manager controls more levers — so the performance measure
must widen to match that authority.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Choosing the wrong measure creates dysfunctional behaviour. Judge a **cost-centre** "
        "manager on profit they can't influence, and you get frustration and gaming. Match "
        "the measure to the controllable levers and behaviour aligns with strategy.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — Centre Classifier & Divisional Simulator</p>',
            unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🧭 Centre Classifier", "📈 Divisional Performance Simulator"])

# ---------- TAB 1: CLASSIFIER ----------
with tab1:
    st.caption("Tell us what the manager controls, and we'll classify the centre and recommend the right measure.")
    q1, q2, q3 = st.columns(3)
    ctrl_cost    = q1.checkbox("Manager controls **costs**", value=True)
    ctrl_revenue = q2.checkbox("Manager controls **revenue**", value=False)
    ctrl_capital = q3.checkbox("Manager controls **capital / investment**", value=False)

    # Classification logic
    if ctrl_capital and ctrl_cost and ctrl_revenue:
        centre, measure, colour = "Investment Centre", "ROI · Residual Income · EVA", "#8e44ad"
        note = "Full P&L plus the balance sheet — judge on returns generated per unit of capital employed."
    elif ctrl_cost and ctrl_revenue:
        centre, measure, colour = "Profit Centre", "Profit · Contribution margin", "#e67e22"
        note = "Controls both sides of the P&L — judge on the profit generated."
    elif ctrl_revenue and not ctrl_cost:
        centre, measure, colour = "Revenue Centre", "Sales vs. target · Revenue variance", "#16a085"
        note = "Accountable for sales generation, not the cost of producing goods."
    elif ctrl_cost and not ctrl_revenue and not ctrl_capital:
        centre, measure, colour = "Cost Centre", "Cost variances · Cost per unit", "#2e86de"
        note = "Accountable only for keeping costs within standard."
    else:
        centre, measure, colour = "Undefined", "Select at least one lever above", "#95a5a6"
        note = "A responsibility centre must control at least one financial lever."

    st.markdown(
        f"""
        <div class="card" style="border-left:6px solid {colour};">
            <span class="pill" style="background:{colour}22; color:{colour};">CLASSIFICATION</span>
            <h3 style="margin:6px 0; color:{colour};">{centre}</h3>
            <b>Recommended performance measure:</b> {measure}<br>
            <span class="subtle">{note}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- TAB 2: DIVISIONAL SIMULATOR ----------
with tab2:
    st.caption("Enter a division's numbers and compare how each type of measure would judge the same unit.")
    left, right = st.columns([1, 1.4])

    with left:
        st.markdown("#### 🎛️ Division inputs")
        revenue   = st.number_input("Revenue (BDT '000)", 0, 1_000_000, 5000, step=100)
        op_cost   = st.number_input("Controllable operating cost (BDT '000)", 0, 1_000_000, 3800, step=100)
        capital   = st.number_input("Capital employed (BDT '000)", 0, 5_000_000, 8000, step=100)
        coc       = st.slider("Cost of capital (%)", 1, 30, 12) / 100

    profit   = revenue - op_cost
    roi      = (profit / capital * 100) if capital else 0
    ri       = profit - coc * capital          # Residual income
    margin   = (profit / revenue * 100) if revenue else 0

    with right:
        st.markdown("#### 📊 The same division, four lenses")
        m = st.columns(4)
        m[0].metric("Cost lens", f"{op_cost:,.0f}", "controllable cost")
        m[1].metric("Revenue lens", f"{revenue:,.0f}", f"margin {margin:.1f}%")
        m[2].metric("Profit lens", f"{profit:,.0f}", f"{'profit' if profit>=0 else 'loss'}")
        m[3].metric("Investment lens", f"ROI {roi:.1f}%",
                    f"RI {ri:+,.0f}", delta_color="normal")

        # Waterfall from revenue to residual income
        wf = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "total", "relative", "total"],
            x=["Revenue", "− Op cost", "Profit", "− Capital charge", "Residual Income"],
            y=[revenue, -op_cost, None, -coc*capital, None],
            connector={"line": {"color": "#b2bec3"}},
            decreasing={"marker": {"color": "#e67e22"}},
            increasing={"marker": {"color": "#2e86de"}},
            totals={"marker": {"color": "#8e44ad"}},
        ))
        wf.update_layout(height=340, margin=dict(t=30, b=10),
                         title="From Revenue to Residual Income")
        st.plotly_chart(wf, use_container_width=True)

    st.session_state["_roi"] = roi
    st.session_state["_ri"] = ri
    st.session_state["_coc"] = coc
    st.session_state["_profit"] = profit
    st.session_state["_margin"] = margin

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

roi_v    = st.session_state.get("_roi", 0)
ri_v     = st.session_state.get("_ri", 0)
coc_v    = st.session_state.get("_coc", 0.12)
profit_v = st.session_state.get("_profit", 0)
margin_v = st.session_state.get("_margin", 0)

prof_icon = "🟢" if profit_v >= 0 else "🔴"
roi_icon  = "🟢" if roi_v >= coc_v*100 else "🔴"
ri_icon   = "🟢" if ri_v >= 0 else "🔴"

st.markdown(
    f"""
- {prof_icon} **Profit lens:** the division makes a **{'profit' if profit_v>=0 else 'loss'} of {profit_v:,.0f}** (margin {margin_v:.1f}%).
- {roi_icon} **Investment lens (ROI):** ROI is **{roi_v:.1f}%** vs a {coc_v*100:.0f}% cost of capital → {"value-creating" if roi_v>=coc_v*100 else "value-destroying"}.
- {ri_icon} **Investment lens (RI):** residual income is **{ri_v:+,.0f}** → {"positive economic value added" if ri_v>=0 else "the division earns below its capital charge"}.
    """
)

if ri_v >= 0 and roi_v >= coc_v*100:
    st.success(
        "**Verdict →** As an *investment centre*, this division creates value: it earns more than "
        "the cost of the capital it ties up. Judging it on ROI/RI is appropriate and it passes.",
        icon="✅",
    )
else:
    st.warning(
        "**Verdict →** As an *investment centre* the division is under-performing against its capital "
        "charge. Note how it might still look fine on a pure **profit** lens — this is exactly why the "
        "*measure must match the centre type*. Investigate asset utilisation or margin before acting.",
        icon="⚠️",
    )

st.info(
    "**The ROI trap:** ROI can wrongly reject a good project that lowers a star division's average, "
    "while RI (an absolute BDT figure) encourages any project earning above the cost of capital. "
    "This is why many groups pair the two.",
    icon="🧠",
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
        - [ ] Identify **what the manager controls** *before* choosing a measure.
        - [ ] Cost centre → **cost variances**; Revenue centre → **sales vs. target**.
        - [ ] Profit centre → **profit/contribution**; Investment centre → **ROI, RI, EVA**.
        - [ ] Never judge a manager on outcomes **outside their authority**.
        - [ ] Pair **ROI with RI** to avoid the "reject-good-projects" trap.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Responsibility centre** — a unit whose manager is accountable for defined outcomes.
            - **Controllability principle** — judge only on what the manager can influence.
            - **ROI** — profit ÷ capital employed (a %).
            - **Residual Income (RI)** — profit − (cost of capital × capital employed), in BDT.
            - **Capital charge** — the return the group requires on capital tied up.
            - **Cost of capital** — the minimum acceptable rate of return.
            """
        )

# Downloadable template
template = pd.DataFrame({
    "Centre type": ["Cost", "Revenue", "Profit", "Investment"],
    "Manager controls": ["Costs", "Revenue", "Costs + Revenue", "Costs + Revenue + Capital"],
    "Primary measure": ["Cost variance", "Sales vs target", "Profit / margin", "ROI · RI · EVA"],
    "Example": ["Production dept.", "Sales region", "Product division", "Strategic business unit"],
})
st.download_button(
    "⬇️ Download the responsibility-centre reference table (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="responsibility_centres_reference.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 0.1 · What is Performance Management", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 0.3 · Controllable vs. Uncontrollable Costs ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 0.2")
