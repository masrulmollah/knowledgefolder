"""
Performance Management — Applied Learning Series
Module 6.2 · Beyond Budgeting & Modern Frameworks
------------------------------------------------------------
The critique of the traditional annual budget and the modern
alternatives:
  • Why the annual fixed budget struggles in volatile conditions
  • Beyond Budgeting (Hope & Fraser) principles
  • Modern tools: rolling forecasts, driver-based planning, OKRs, agile
  • A traditional-vs-adaptive diagnostic and readiness self-assessment

Run with:  streamlit run 6.2_Beyond_Budgeting_and_Modern_Frameworks.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="6.2 · Beyond Budgeting & Modern Frameworks",
    page_icon="🚀",
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
st.markdown('<p class="pill">MODULE 6 · REPORTING, GOVERNANCE & APPLICATION</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">6.2 · Beyond Budgeting & Modern Frameworks</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand the <b>critique of the traditional annual budget</b> and the '
    'modern alternatives — <b>Beyond Budgeting, rolling forecasts, driver-based planning and OKRs</b> — '
    'and assess how adaptive your own planning is.</p>',
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
The traditional **annual fixed budget** has been the backbone of control for a century — but
in fast-moving markets it is increasingly criticised.

**The critique of traditional budgeting:**

- **Time-consuming and costly** — months of effort for a plan that can be stale on arrival.
- **Quickly out of date** — a fixed annual target ignores changing conditions.
- **Encourages dysfunctional behaviour** — budget slack, "use it or lose it" spending, and
  gaming (from Module 2.4).
- **Backward-looking and rigid** — anchors on last year and discourages agility.
- **Weak strategic link** — annual cost control can crowd out longer-term value creation.

**Beyond Budgeting (Hope & Fraser)** proposes managing *without* traditional fixed budgets,
built on two sets of principles:

- **Leadership principles** — devolve decisions, trust teams, set relative goals, foster
  transparency and purpose.
- **Process principles** — use **rolling forecasts**, **relative targets** (vs. peers or the
  market rather than a fixed number), **resources on demand**, and reward **relative
  performance** rather than beating a negotiated budget.

**Modern planning tools** that support this:

- **Rolling forecasts** — continuously updated horizon (from Module 2.3).
- **Driver-based planning** — model outputs from the few key business *drivers* (volume,
  price, rates) rather than line-by-line, so re-forecasting is fast.
- **OKRs (Objectives & Key Results)** — ambitious objectives with measurable key results,
  reviewed quarterly; popular in tech and agile organisations.
- **Beyond Budgeting / adaptive management** — separating **target-setting, forecasting and
  resource allocation** (traditional budgets fuse all three, causing conflict).

**The key idea:** separate the three jobs a budget tries to do at once — **set a target,
predict the future, and allocate resources** — because bundling them creates bias (you lowball
the forecast to get an easy target, or pad resources to be safe).
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Finance leaders increasingly question whether the annual budget earns its cost. Knowing the "
        "alternatives — and being able to diagnose which fits your volatility and culture — is a "
        "modern finance-leadership skill. It's not 'no planning'; it's *smarter, more adaptive* "
        "planning.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

tab_diag, tab_ready = st.tabs(["⚖️ Traditional vs. Adaptive Diagnostic", "🚀 Beyond Budgeting Readiness"])

# ==================================================================
# TAB 1 — DIAGNOSTIC
# ==================================================================
with tab_diag:
    st.caption("Rate where your organisation sits on each dimension (0 = fully traditional, 100 = fully adaptive).")

    dims = {
        "Target setting": ("Fixed annual target", "Relative / rolling target"),
        "Forecasting": ("Annual, static", "Continuous rolling forecast"),
        "Resource allocation": ("Pre-allocated in budget", "On demand, as needed"),
        "Decision-making": ("Centralised, top-down", "Devolved to front line"),
        "Rewards": ("Beat the fixed budget", "Relative performance"),
        "Planning granularity": ("Line-by-line", "Driver-based"),
    }

    scores = {}
    dl, dr = st.columns([1, 1.3])
    with dl:
        st.markdown("#### 🎛️ Rate each dimension")
        for dim, (trad, adap) in dims.items():
            scores[dim] = st.slider(f"{dim}", 0, 100, 35, step=5,
                                    help=f"0 = {trad}  •  100 = {adap}")

    avg = np.mean(list(scores.values()))

    with dr:
        st.markdown("#### 🕸️ Traditional ↔ Adaptive Profile")
        cats = list(scores.keys())
        vals = list(scores.values())
        radar = go.Figure()
        radar.add_trace(go.Scatterpolar(r=vals + [vals[0]], theta=cats + [cats[0]],
                                        fill="toself", line=dict(color="#2e86de", width=2),
                                        fillcolor="rgba(46,134,222,0.25)", name="You"))
        radar.update_layout(height=360, margin=dict(t=30, b=10),
                            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                            showlegend=False)
        st.plotly_chart(radar, use_container_width=True)
        st.metric("Adaptiveness index", f"{avg:.0f}/100",
                  "adaptive" if avg >= 60 else ("transitional" if avg >= 40 else "traditional"),
                  delta_color="normal" if avg >= 60 else "off")

    if avg < 40:
        st.info(
            "**Predominantly traditional.** A fixed annual budget still anchors your planning. This can "
            "work in **stable** conditions, but if your market is volatile you're likely reacting late. "
            "Consider introducing **rolling forecasts** as a first step.",
            icon="🏛️",
        )
    elif avg < 60:
        st.warning(
            "**In transition.** You've adopted some adaptive practices but retain traditional anchors. "
            "The risk is running *both* systems at once (double effort). Decide which elements to fully "
            "commit to — often **rolling forecasts + relative targets** first.",
            icon="🔄",
        )
    else:
        st.success(
            "**Strongly adaptive.** Your planning is devolved, continuous and driver-based — well suited "
            "to volatile conditions. Keep guarding against the main risk: **loss of central control**, "
            "managed through transparency and clear boundaries.",
            icon="🚀",
        )

# ==================================================================
# TAB 2 — READINESS
# ==================================================================
with tab_ready:
    st.caption("Answer honestly — how ready is your organisation to move beyond the traditional budget?")

    qs = [
        "Our market/demand is volatile and hard to predict a year ahead",
        "Managers are trusted to make decisions without central sign-off",
        "We already produce rolling forecasts (or could easily)",
        "We have good data systems for fast re-forecasting",
        "Leadership is open to changing the planning model",
        "We can set targets relative to peers/market, not just a fixed number",
    ]
    answers = []
    for q in qs:
        answers.append(st.select_slider(q, options=["Strongly disagree", "Disagree", "Neutral",
                                                     "Agree", "Strongly agree"], value="Neutral"))
    scale = {"Strongly disagree": 0, "Disagree": 25, "Neutral": 50, "Agree": 75, "Strongly agree": 100}
    readiness = np.mean([scale[a] for a in answers])

    st.markdown("#### 📊 Readiness Score")
    gauge = go.Figure(go.Indicator(
        mode="gauge+number", value=readiness, number={"suffix": "%"},
        title={"text": "Beyond Budgeting readiness"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#2e86de"},
               "steps": [{"range": [0, 40], "color": "#f5b7b1"},
                         {"range": [40, 70], "color": "#fdebd0"},
                         {"range": [70, 100], "color": "#abebc6"}]}))
    gauge.update_layout(height=300, margin=dict(t=40, b=10))
    st.plotly_chart(gauge, use_container_width=True)

    if readiness < 40:
        st.info("**Low readiness.** Culture, data or volatility conditions aren't yet aligned for a full "
                "move. Start small: pilot a **rolling forecast** alongside the existing budget.", icon="🌱")
    elif readiness < 70:
        st.warning("**Moderate readiness.** Foundations exist. Prioritise the weakest enablers — often "
                   "**data systems** or **leadership trust** — before scaling up adaptive practices.", icon="⚙️")
    else:
        st.success("**High readiness.** Volatility, culture and systems favour an adaptive model. You could "
                   "move decisively to **rolling forecasts + relative targets + devolved decisions**.", icon="🚀")

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — adopting modern frameworks wisely</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 🎯 **Separate the three jobs.** Most budget dysfunction comes from fusing **target-setting,
  forecasting and resource allocation**. Splitting them removes the incentive to bias the forecast
  to win an easy target.
- 🔄 **Adopt incrementally.** Few organisations abandon budgets overnight. **Rolling forecasts** are
  usually the first, highest-value step; relative targets and devolution follow as trust grows.
- 🧭 **Fit to context.** Beyond Budgeting shines in **volatile, knowledge-based** settings; a stable,
  regulated operation may still value the discipline of a traditional budget. Match the tool to the
  environment (echoing the benchmarking caution in 5.4).
- ⚖️ **Mind the trade-off.** Greater agility can mean **less central control and comparability**.
  Manage this with transparency, clear boundaries and strong information systems.
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
        - [ ] Know the **critique** of the annual budget (slow, stale, gamed, rigid).
        - [ ] **Beyond Budgeting** = leadership + process principles, no fixed budget.
        - [ ] Separate **target-setting, forecasting and resource allocation**.
        - [ ] Start with **rolling forecasts**; add relative targets and devolution.
        - [ ] Match the model to your **volatility and culture**; mind the control trade-off.
        """
    )
with a2:
    with st.expander("📘 Key concepts in this module"):
        st.markdown(
            """
            - **Beyond Budgeting** — managing without traditional fixed budgets (Hope & Fraser).
            - **Rolling forecast** — continuously updated forward horizon.
            - **Driver-based planning** — model outputs from key business drivers.
            - **Relative targets** — measured vs. peers/market, not a fixed number.
            - **OKRs** — Objectives & Key Results, reviewed quarterly.
            - **The three jobs** — target-setting, forecasting, resource allocation (separate them!).
            """
        )
    with st.expander("🧭 Traditional vs. Beyond Budgeting"):
        st.markdown(
            """
            | | **Traditional** | **Beyond Budgeting** |
            |---|---|---|
            | Target | Fixed annual | Relative / stretch |
            | Forecast | Annual, static | Rolling, continuous |
            | Resources | Pre-allocated | On demand |
            | Decisions | Centralised | Devolved |
            | Rewards | Beat the budget | Relative performance |
            """
        )

# Downloadable diagnostic
export = pd.DataFrame({
    "Dimension": list(scores.keys()) + ["Adaptiveness index", "Readiness score"],
    "Score (0-100)": [round(v, 0) for v in scores.values()] + [round(avg, 0), round(readiness, 0)],
})
st.download_button(
    "⬇️ Download the planning-maturity diagnostic (CSV)",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="beyond_budgeting_diagnostic.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 6.1 · Performance Dashboards & Reporting", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 6.3 · End-to-End Case Study ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 6.2")
