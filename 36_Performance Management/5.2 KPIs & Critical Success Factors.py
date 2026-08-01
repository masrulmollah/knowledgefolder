"""
Performance Management — Applied Learning Series
Module 5.2 · KPIs & Critical Success Factors
------------------------------------------------------------
Choosing the RIGHT measures:
  • CSF -> KPI cascade (what must go right -> how we measure it)
  • Leading vs. lagging indicators
  • The SMART quality test for a KPI
  • Pitfalls: too many KPIs, gaming, vanity metrics, tunnel vision

Run with:  streamlit run 5.2_KPIs_and_Critical_Success_Factors.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="5.2 · KPIs & Critical Success Factors",
    page_icon="🎯",
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
st.markdown('<p class="pill">MODULE 5 · PERFORMANCE MEASUREMENT — STRATEGIC & NON-FINANCIAL</p>',
            unsafe_allow_html=True)
st.markdown('<p class="big-title">5.2 · KPIs & Critical Success Factors</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: cascade <b>Critical Success Factors (CSFs)</b> into <b>Key Performance '
    'Indicators (KPIs)</b>, distinguish <b>leading vs. lagging</b> measures, and test each KPI against the '
    '<b>SMART</b> quality criteria — while avoiding the classic measurement pitfalls.</p>',
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
Strategy only becomes manageable when it is measured — but *what* you measure decides *how*
people behave. This module is about choosing the **right** measures.

**Critical Success Factors (CSFs)** are the **few things that must go right** for the
organisation to achieve its strategy — e.g. *"reliable on-time delivery"* or *"consistent
product quality"*. They are qualitative statements of what matters most.

**Key Performance Indicators (KPIs)** are the **quantifiable measures** that tell you whether
a CSF is being achieved — e.g. the CSF *"reliable delivery"* is measured by the KPI *"% orders
delivered on time"*. The relationship is a **cascade**:

> **Objective → CSF (what must go right) → KPI (how we measure it) → Target → Initiative**

**Leading vs. lagging indicators:**

- **Lagging** — measure past outcomes (profit, revenue). Accurate but too late to act on.
- **Leading** — measure the *drivers* of future outcomes (pipeline, training, defect rate).
  Predictive but less certain. A good set **balances both**.

**What makes a good KPI — the SMART test:** Specific, Measurable, Achievable, Relevant,
Time-bound. A KPI failing any of these will mislead or demotivate.

**The pitfalls** (what to guard against):

- **Too many KPIs** — dilutes focus; keep to the *vital few*.
- **Gaming / tunnel vision** — people optimise the measure, not the goal ("what gets measured
  gets manipulated").
- **Vanity metrics** — impressive-looking numbers that don't drive decisions.
- **Measuring only what's easy**, not what matters.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Finance is often custodian of the KPI framework. Pick the wrong measures and you steer the "
        "business off course — rewarding volume over margin, or output over quality. Getting the "
        "CSF→KPI cascade right, with a balance of leading and lagging measures, is how finance turns "
        "strategy into steerable performance.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

tab_cascade, tab_smart = st.tabs(["🔗 CSF → KPI Cascade", "✅ SMART KPI Tester"])

# ==================================================================
# TAB 1 — CSF -> KPI CASCADE
# ==================================================================
with tab_cascade:
    st.caption("Map each Critical Success Factor to its KPI, target, and indicator type. Keep to the vital few.")

    default = pd.DataFrame({
        "Critical Success Factor": ["Reliable on-time delivery", "Consistent product quality",
                                    "Motivated, skilled workforce", "Cost competitiveness",
                                    "Strong customer relationships"],
        "KPI": ["% orders delivered on time", "First-pass quality yield (%)",
                "Training days per employee", "Unit cost vs. benchmark (%)",
                "Customer retention rate (%)"],
        "Target": ["≥ 95%", "≥ 98%", "6 days", "≤ 100%", "≥ 90%"],
        "Type": ["Lagging", "Lagging", "Leading", "Lagging", "Lagging"],
    })
    data = st.data_editor(
        default, num_rows="dynamic", use_container_width=True, hide_index=True,
        column_config={
            "Type": st.column_config.SelectboxColumn(options=["Leading", "Lagging"]),
        },
    )

    df = data.copy()
    df = df[df["KPI"].astype(str).str.strip() != ""].reset_index(drop=True)
    n_kpi = len(df)
    n_lead = (df["Type"] == "Leading").sum()
    n_lag = (df["Type"] == "Lagging").sum()
    lead_pct = n_lead / n_kpi * 100 if n_kpi else 0

    m1, m2, m3 = st.columns(3)
    m1.metric("Total KPIs", f"{n_kpi}", "vital few" if n_kpi <= 7 else "too many?",
              delta_color="normal" if n_kpi <= 7 else "inverse")
    m2.metric("Leading", f"{n_lead}", f"{lead_pct:.0f}% of set")
    m3.metric("Lagging", f"{n_lag}", f"{100-lead_pct:.0f}% of set")

    # Leading vs lagging balance chart
    fig = go.Figure(go.Bar(
        x=["Leading", "Lagging"], y=[n_lead, n_lag],
        marker_color=["#8e44ad", "#2e86de"],
        text=[n_lead, n_lag], textposition="outside",
    ))
    fig.update_layout(height=260, margin=dict(t=30, b=10), plot_bgcolor="white",
                      title="Leading vs. lagging balance", yaxis_title="# KPIs")
    st.plotly_chart(fig, use_container_width=True)

    if n_kpi > 7:
        st.warning(
            f"**{n_kpi} KPIs may be too many.** Beyond ~5–7 the *vital few* get lost and focus dilutes. "
            f"Prune to the measures that genuinely drive the strategy.",
            icon="⚠️",
        )
    if n_lead == 0 and n_kpi > 0:
        st.warning(
            "**No leading indicators.** Your set is entirely lagging — you'll only know performance "
            "*after* it's too late to act. Add predictive, driver-based measures.",
            icon="⚠️",
        )
    elif n_lag == 0 and n_kpi > 0:
        st.info("**All leading, no lagging.** Predictive, but you lack confirmed outcome measures — "
                "add a few lagging KPIs to verify results.", icon="🟡")
    elif n_kpi > 0:
        st.success("**Balanced set.** A healthy mix of leading drivers and lagging outcomes.", icon="✅")

# ==================================================================
# TAB 2 — SMART TESTER
# ==================================================================
with tab_smart:
    st.caption("Score a single KPI against the five SMART criteria to judge whether it's fit for purpose.")

    sl, sr = st.columns([1, 1.3])
    with sl:
        st.markdown("#### 🎛️ KPI under review")
        kpi_name = st.text_input("KPI name", "% orders delivered on time")
        st.markdown("**Rate each criterion (1 = weak, 5 = strong)**")
        specific   = st.slider("Specific — clearly defined, unambiguous", 1, 5, 4)
        measurable = st.slider("Measurable — reliably quantifiable", 1, 5, 5)
        achievable = st.slider("Achievable — realistic to influence", 1, 5, 4)
        relevant   = st.slider("Relevant — linked to a CSF/strategy", 1, 5, 5)
        timebound  = st.slider("Time-bound — has a period/deadline", 1, 5, 3)

    scores = {"Specific": specific, "Measurable": measurable, "Achievable": achievable,
              "Relevant": relevant, "Time-bound": timebound}
    total = sum(scores.values())
    pct = total / 25 * 100

    with sr:
        st.markdown("#### 📊 SMART Profile")
        radar = go.Figure()
        cats = list(scores.keys())
        vals = list(scores.values())
        radar.add_trace(go.Scatterpolar(
            r=vals + [vals[0]], theta=cats + [cats[0]], fill="toself",
            line=dict(color="#2e86de", width=2), fillcolor="rgba(46,134,222,0.25)",
            name=kpi_name))
        radar.update_layout(height=320, margin=dict(t=30, b=10),
                            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                            showlegend=False)
        st.plotly_chart(radar, use_container_width=True)
        st.metric("Overall SMART score", f"{total}/25", f"{pct:.0f}%",
                  delta_color="normal" if pct >= 80 else "inverse")

    weakest = min(scores, key=scores.get)
    if pct >= 80:
        st.success(
            f"**Strong KPI ({pct:.0f}%).** '{kpi_name}' meets the SMART criteria well and is fit for "
            f"purpose. Keep the weakest dimension — **{weakest} ({scores[weakest]}/5)** — under review.",
            icon="✅",
        )
    elif pct >= 60:
        st.warning(
            f"**Usable but improvable ({pct:.0f}%).** The weakest criterion is **{weakest} "
            f"({scores[weakest]}/5)**. Tighten it before relying on this KPI for decisions or rewards.",
            icon="⚠️",
        )
    else:
        st.error(
            f"**Weak KPI ({pct:.0f}%).** '{kpi_name}' fails the SMART test, especially on **{weakest}**. "
            f"A poorly-defined KPI misleads and demotivates — redefine it before use.",
            icon="🔴",
        )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — designing a measurement set that works</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 🔗 **Start from strategy, not data.** Derive KPIs *from* CSFs, which come *from* objectives —
  never bolt measures on just because the data is available.
- ⚖️ **Balance leading and lagging.** Lagging measures confirm results; leading measures let you
  act in time. A set that is all-lagging is a rear-view mirror.
- 🎯 **Fewer, better KPIs.** The *vital few* focus attention; a sprawling dashboard hides what
  matters and invites box-ticking.
- 🛡️ **Design against gaming.** Whatever you measure and reward, people will optimise — so pair
  measures (e.g. speed *and* quality) to prevent tunnel vision, and revisit KPIs as behaviour adapts.
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
        - [ ] Cascade **Objective → CSF → KPI → Target → Initiative**.
        - [ ] Every KPI must trace back to a **CSF** and the strategy.
        - [ ] Balance **leading** (predictive) and **lagging** (confirming) measures.
        - [ ] Test each KPI against **SMART**; fix the weakest criterion.
        - [ ] Keep the **vital few**; pair measures to prevent **gaming**.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **CSF** — the few things that must go right to deliver strategy.
            - **KPI** — a quantifiable measure of whether a CSF is achieved.
            - **Leading indicator** — measures a driver of future performance.
            - **Lagging indicator** — measures a past outcome.
            - **SMART** — Specific, Measurable, Achievable, Relevant, Time-bound.
            - **Gaming / tunnel vision** — optimising the measure, not the goal.
            """
        )
    with st.expander("🧭 CSF → KPI examples"):
        st.markdown(
            """
            | CSF | KPI |
            |---|---|
            | Reliable delivery | % on-time delivery |
            | Product quality | First-pass yield %, defect rate |
            | Skilled workforce | Training days, retention % |
            | Cost competitiveness | Unit cost vs. benchmark |
            | Customer loyalty | Retention %, NPS |
            """
        )

# Downloadable cascade
export = df[["Critical Success Factor", "KPI", "Target", "Type"]].copy()
st.download_button(
    "⬇️ Download the CSF → KPI cascade (CSV)",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="csf_kpi_cascade.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 5.1 · The Balanced Scorecard", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 5.3 · Non-Financial Performance Indicators ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 5.2")
