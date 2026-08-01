"""
Performance Management — Applied Learning Series
Module 5.3 · Non-Financial Performance Indicators (NFPIs)
------------------------------------------------------------
Measuring what financials miss — the leading indicators of future
financial performance:
  • Quality (and the cost-of-quality model: prevention/appraisal/failure)
  • Delivery & operations (OTIF, cycle time, throughput)
  • People (engagement, retention, safety)
  • Sustainability / ESG
Shows how non-financial signals predict financial outcomes.

Run with:  streamlit run 5.3_Non_Financial_Performance_Indicators.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="5.3 · Non-Financial Performance Indicators",
    page_icon="🌱",
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
st.markdown('<p class="big-title">5.3 · Non-Financial Performance Indicators</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: measure the <b>quality, delivery, people and sustainability</b> '
    'dimensions that financials miss, understand the <b>cost-of-quality</b> model, and see how these '
    '<b>leading</b> signals predict future financial performance.</p>',
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
**Non-Financial Performance Indicators (NFPIs)** measure aspects of performance that money
figures alone cannot capture — quality, speed, customer loyalty, employee engagement,
environmental impact. They are usually **leading** indicators: they move *before* the
financial results do, giving early warning and time to act.

**The main NFPI families:**

- **Quality** — defect/reject rate, first-pass yield, customer complaints, returns, warranty
  claims. Quality is often analysed through the **cost-of-quality** model:
    - **Prevention costs** — spent to *stop* defects (training, better design, maintenance).
    - **Appraisal costs** — spent to *find* defects (inspection, testing).
    - **Internal failure** — defects caught *before* dispatch (scrap, rework).
    - **External failure** — defects reaching the *customer* (returns, warranty, lost goodwill).
  Spending more on **prevention** typically slashes the far more expensive **failure** costs.
- **Delivery & operations** — on-time-in-full (OTIF), cycle/lead time, throughput, capacity
  utilisation, schedule adherence.
- **People** — employee engagement, retention/turnover, absenteeism, safety (lost-time
  incidents), training hours.
- **Sustainability / ESG** — energy and water use, waste and emissions, recycling rate,
  community and governance measures.

**Why they matter:** financials are **lagging** and can be short-term-gamed (cut training,
defer maintenance) to flatter this period while damaging the future. NFPIs expose those
trade-offs and measure the **drivers** of sustainable financial performance.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "A factory can hit its cost target this quarter by skimping on maintenance or quality — and "
        "pay for it later in breakdowns, scrap and lost customers. NFPIs let finance see those "
        "trade-offs *before* they hit the P&L, making them essential partners to the numbers rather "
        "than a replacement for them.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

tab_coq, tab_dash = st.tabs(["🔧 Cost-of-Quality Model", "🌱 NFPI Dashboard (Quality · Delivery · People · ESG)"])

# ==================================================================
# TAB 1 — COST OF QUALITY
# ==================================================================
with tab_coq:
    st.caption("Shift spend toward prevention and watch how failure costs — the expensive kind — respond.")

    ql, qr = st.columns([1, 1.4])
    with ql:
        st.markdown("#### 🎛️ Quality spend (BDT)")
        prevention = st.number_input("Prevention costs", 0, 100_000_000, 200_000, step=10_000)
        appraisal  = st.number_input("Appraisal costs", 0, 100_000_000, 150_000, step=10_000)
        st.markdown("#### 🎛️ Failure costs (BDT)")
        st.caption("Tip: higher prevention usually drives these down in practice.")
        internal_fail = st.number_input("Internal failure (scrap, rework)", 0, 100_000_000, 300_000, step=10_000)
        external_fail = st.number_input("External failure (returns, warranty)", 0, 100_000_000, 450_000, step=10_000)

    conformance = prevention + appraisal           # cost of good quality
    non_conformance = internal_fail + external_fail # cost of poor quality
    total_coq = conformance + non_conformance

    with qr:
        st.markdown("#### 📊 Cost-of-Quality Breakdown")
        a, b, c = st.columns(3)
        a.metric("Conformance", f"{conformance:,.0f} BDT",
                 f"{conformance/total_coq*100 if total_coq else 0:.0f}%")
        b.metric("Non-conformance", f"{non_conformance:,.0f} BDT",
                 f"{non_conformance/total_coq*100 if total_coq else 0:.0f}%")
        c.metric("Total CoQ", f"{total_coq:,.0f} BDT")

        fig = go.Figure(go.Bar(
            x=["Prevention", "Appraisal", "Internal failure", "External failure"],
            y=[prevention, appraisal, internal_fail, external_fail],
            marker_color=["#1e8449", "#16a085", "#e67e22", "#c0392b"],
            text=[f"{prevention:,.0f}", f"{appraisal:,.0f}",
                  f"{internal_fail:,.0f}", f"{external_fail:,.0f}"],
            textposition="outside",
        ))
        fig.update_layout(height=300, margin=dict(t=30, b=10), plot_bgcolor="white",
                          yaxis_title="BDT", title="The four quality-cost categories")
        st.plotly_chart(fig, use_container_width=True)

    ratio = non_conformance / conformance if conformance else float("inf")
    if ratio > 1.5:
        st.warning(
            f"**Failure costs dominate (non-conformance is {ratio:.1f}× conformance).** You are paying "
            f"far more to *fix* defects than to *prevent* them — and external failure "
            f"({external_fail:,.0f} BDT) is the most damaging of all. Shifting spend toward "
            f"**prevention** typically reduces total cost of quality.",
            icon="⚠️",
        )
    elif ratio < 0.7:
        st.success(
            f"**Prevention-led quality.** Conformance spend outweighs failure costs — a sign of a "
            f"mature quality system where defects are designed out rather than inspected out.",
            icon="✅",
        )
    else:
        st.info(f"**Balanced quality spend** (non-conformance {ratio:.1f}× conformance). Watch the trend — "
                f"the goal is to move spend *upstream* into prevention over time.", icon="🟡")

# ==================================================================
# TAB 2 — NFPI DASHBOARD
# ==================================================================
with tab_dash:
    st.caption("Enter actuals vs. targets across the four NFPI families; the engine scores each and flags leading risks.")

    default = pd.DataFrame({
        "Family": ["Quality", "Quality", "Delivery", "Delivery",
                   "People", "People", "Sustainability", "Sustainability"],
        "Indicator": ["First-pass yield (%)", "Customer complaints (per 1000)",
                      "OTIF delivery (%)", "Order lead time (days)",
                      "Staff engagement (%)", "Staff turnover (%)",
                      "Waste recycled (%)", "Energy per unit (kWh)"],
        "Target": [98.0, 5.0, 95.0, 4.0, 80.0, 8.0, 90.0, 1.2],
        "Actual": [96.0, 7.0, 92.0, 5.0, 76.0, 11.0, 85.0, 1.4],
        "Lower is better": [False, True, False, True, False, True, False, True],
    })
    data = st.data_editor(
        default, num_rows="dynamic", use_container_width=True, hide_index=True,
        column_config={
            "Family": st.column_config.SelectboxColumn(
                options=["Quality", "Delivery", "People", "Sustainability"]),
            "Target": st.column_config.NumberColumn(format="%.1f"),
            "Actual": st.column_config.NumberColumn(format="%.1f"),
            "Lower is better": st.column_config.CheckboxColumn(),
        },
    )

    df = data.copy()
    df = df[(df["Target"].notna()) & (df["Actual"].notna())].reset_index(drop=True)

    def achievement(row):
        t, a, lower = row["Target"], row["Actual"], row["Lower is better"]
        if t == 0 or a == 0:
            return 0.0
        val = (t / a) if lower else (a / t)
        return round(min(val * 100, 150), 1)

    df["Achievement %"] = df.apply(achievement, axis=1)

    fam_order = ["Quality", "Delivery", "People", "Sustainability"]
    fam_scores = df.groupby("Family")["Achievement %"].mean().reindex(fam_order).fillna(0)

    dl, dr = st.columns([1.1, 1])
    with dl:
        st.markdown("#### 📊 Indicator Detail")
        show = df[["Family", "Indicator", "Target", "Actual", "Achievement %"]]
        st.dataframe(
            show.style.format({"Target": "{:,.1f}", "Actual": "{:,.1f}", "Achievement %": "{:.0f}%"}),
            use_container_width=True, hide_index=True,
        )
    with dr:
        st.markdown("#### 🕸️ NFPI Balance")
        radar = go.Figure()
        radar.add_trace(go.Scatterpolar(
            r=list(fam_scores.values) + [fam_scores.values[0]],
            theta=fam_order + [fam_order[0]], fill="toself",
            line=dict(color="#16a085", width=2), fillcolor="rgba(22,160,133,0.25)"))
        radar.add_trace(go.Scatterpolar(
            r=[100] * (len(fam_order) + 1), theta=fam_order + [fam_order[0]],
            line=dict(color="#1e8449", width=1, dash="dash"), name="Target"))
        radar.update_layout(height=320, margin=dict(t=30, b=10),
                            polar=dict(radialaxis=dict(visible=True, range=[0, 130])),
                            showlegend=False)
        st.plotly_chart(radar, use_container_width=True)

    f1, f2, f3, f4 = st.columns(4)
    for col, name in zip([f1, f2, f3, f4], fam_order):
        s = fam_scores[name]
        col.metric(name, f"{s:.0f}%", "on track" if s >= 95 else "below target",
                   delta_color="normal" if s >= 95 else "inverse")

    weakest = fam_scores.idxmin()
    st.warning(
        f"**Leading-risk signal: {weakest} is weakest at {fam_scores[weakest]:.0f}%.** Because NFPIs "
        f"lead the financials, a shortfall here is an early warning — {'poor quality/delivery erodes customers and drives failure costs' if weakest in ['Quality','Delivery'] else 'weak people/sustainability metrics undermine capability and licence to operate'} — "
        f"act now, before it reaches the P&L.",
        icon="⚠️",
    ) if fam_scores.min() < 95 else st.success(
        "**All NFPI families on track.** Strong leading indicators point to healthy future financials.",
        icon="✅")

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — non-financial signals, financial consequences</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 🔧 **Quality: prevention beats cure.** External failure is the costliest category (rework *plus*
  lost goodwill). Spending upstream on prevention and appraisal is almost always cheaper than
  paying for failure downstream.
- ⏱️ **Delivery drives loyalty.** OTIF and lead time are leading indicators of customer retention —
  slipping service today predicts lost revenue tomorrow.
- 👥 **People underpin everything.** Engagement, safety and retention are the deepest leading
  indicators; neglect them and quality, delivery and cost all deteriorate later.
- 🌱 **Sustainability is now performance, not PR.** ESG measures affect cost (energy, waste),
  risk (regulation) and reputation — increasingly material to financial results.
- ⚖️ **Balance, don't replace.** NFPIs complement financials; used together they reveal whether
  today's profit was earned sustainably or borrowed from the future.
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
        - [ ] NFPIs are mostly **leading** — they move before the financials do.
        - [ ] Cover **quality, delivery, people, sustainability**.
        - [ ] Use the **cost-of-quality** model: prevention + appraisal vs. failure.
        - [ ] Shift quality spend **upstream** into prevention.
        - [ ] **Complement**, don't replace, financial measures.
        """
    )
with a2:
    with st.expander("📘 Cost-of-quality categories"):
        st.markdown(
            """
            - **Prevention** — stop defects arising (training, design, maintenance).
            - **Appraisal** — detect defects (inspection, testing).
            - **Internal failure** — caught before dispatch (scrap, rework).
            - **External failure** — reach the customer (returns, warranty, goodwill).

            *Conformance = Prevention + Appraisal. Non-conformance = Internal + External failure.*
            """
        )
    with st.expander("🧭 Example NFPIs by family"):
        st.markdown(
            """
            | Family | Example indicators |
            |---|---|
            | **Quality** | Defect rate, first-pass yield, complaints |
            | **Delivery** | OTIF, lead time, throughput |
            | **People** | Engagement, turnover, safety (LTI) |
            | **Sustainability** | Energy/unit, waste %, emissions |
            """
        )

# Downloadable NFPI dashboard
export = df[["Family", "Indicator", "Target", "Actual", "Achievement %"]].copy()
st.download_button(
    "⬇️ Download the NFPI dashboard (CSV)",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="non_financial_indicators.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 5.2 · KPIs & Critical Success Factors", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 5.4 · Benchmarking ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 5.3")
