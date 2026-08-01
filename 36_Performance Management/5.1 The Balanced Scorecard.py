"""
Performance Management — Applied Learning Series
Module 5.1 · The Balanced Scorecard
------------------------------------------------------------
Kaplan & Norton's Balanced Scorecard: translating strategy into a
balanced set of measures across four perspectives —
  • Financial
  • Customer
  • Internal Business Process
  • Learning & Growth
Includes an editable scorecard, a radar view, achievement scoring,
and a cause-and-effect strategy map.

Run with:  streamlit run 5.1_The_Balanced_Scorecard.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="5.1 · The Balanced Scorecard",
    page_icon="🧭",
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
st.markdown('<p class="big-title">5.1 · The Balanced Scorecard</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: translate strategy into a <b>balanced set of measures</b> across four '
    'perspectives — <b>Financial, Customer, Internal Process, and Learning &amp; Growth</b> — and see how '
    'they link through cause and effect.</p>',
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
Traditional performance measurement leans heavily on **financial** results — which are
**lagging** indicators that tell you how you *did*, not how you *will do*. Kaplan & Norton's
**Balanced Scorecard (BSC)** complements them with **leading** indicators, translating
strategy into measures across **four perspectives**:

- **Financial** — *"How do we look to shareholders?"* Profit, ROCE, cash, growth.
- **Customer** — *"How do customers see us?"* Satisfaction, retention, market share,
  on-time delivery.
- **Internal Business Process** — *"What must we excel at?"* Quality, cycle time, yield,
  efficiency.
- **Learning & Growth** — *"Can we continue to improve and create value?"* Skills, training,
  innovation, employee engagement, systems.

**The key insight — cause and effect.** The perspectives are not a random list; they form a
**chain**: investment in *Learning & Growth* improves *Internal Processes*, which lifts
*Customer* outcomes, which ultimately drives *Financial* results. The lower perspectives are
the **leading drivers** of the **lagging** financial outcomes.

**For each objective, the scorecard specifies four things:** the **objective**, a **measure
(KPI)**, a **target**, and an **initiative** to achieve it. This forces strategy to be made
concrete and measurable, and keeps the organisation from over-optimising one dimension (e.g.
cutting cost) at the expense of others (e.g. quality or capability).
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Finance owns the numbers, but numbers alone are lagging. The BSC forces the question "
        "*what drives* those numbers — capability, process, customer — so finance can help the "
        "business manage the **causes** of future performance, not just report the past. It is the "
        "bridge from cost control to strategy.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Scorecard Builder
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Scorecard Builder</p>',
            unsafe_allow_html=True)
st.caption("Edit the objectives, targets and actuals below; the engine scores each perspective and plots the balance.")

default = pd.DataFrame({
    "Perspective": ["Financial", "Financial", "Customer", "Customer",
                    "Internal Process", "Internal Process", "Learning & Growth", "Learning & Growth"],
    "Objective (KPI)": ["ROCE (%)", "Revenue growth (%)", "On-time delivery (%)",
                        "Customer satisfaction (%)", "First-pass quality yield (%)",
                        "Order cycle time (days)", "Training days per employee",
                        "Staff engagement (%)"],
    "Target": [18.0, 10.0, 95.0, 90.0, 98.0, 5.0, 6.0, 80.0],
    "Actual": [16.5, 8.0, 92.0, 88.0, 96.0, 6.0, 5.0, 76.0],
    "Lower is better": [False, False, False, False, False, True, False, False],
})

data = st.data_editor(
    default, num_rows="dynamic", use_container_width=True, hide_index=True,
    column_config={
        "Perspective": st.column_config.SelectboxColumn(
            options=["Financial", "Customer", "Internal Process", "Learning & Growth"]),
        "Target": st.column_config.NumberColumn(format="%.1f"),
        "Actual": st.column_config.NumberColumn(format="%.1f"),
        "Lower is better": st.column_config.CheckboxColumn(
            help="Tick for metrics where a lower actual is better, e.g. cycle time."),
    },
)

df = data.copy()
df = df[(df["Target"].notna()) & (df["Actual"].notna())].reset_index(drop=True)

# Achievement %: for higher-is-better = actual/target; lower-is-better = target/actual
def achievement(row):
    t, a, lower = row["Target"], row["Actual"], row["Lower is better"]
    if t == 0 or a == 0:
        return 0.0
    val = (t / a) if lower else (a / t)
    return round(min(val * 100, 150), 1)   # cap at 150% to avoid runaway

df["Achievement %"] = df.apply(achievement, axis=1)

# Perspective scores (average achievement)
persp_order = ["Financial", "Customer", "Internal Process", "Learning & Growth"]
persp_scores = (df.groupby("Perspective")["Achievement %"]
                  .mean().reindex(persp_order).fillna(0))

left, right = st.columns([1.1, 1])

with left:
    st.markdown("#### 📊 Achievement by KPI")
    show = df[["Perspective", "Objective (KPI)", "Target", "Actual", "Achievement %"]]
    st.dataframe(
        show.style.format({"Target": "{:,.1f}", "Actual": "{:,.1f}", "Achievement %": "{:.0f}%"}),
        use_container_width=True, hide_index=True,
    )
    overall = df["Achievement %"].mean() if len(df) else 0
    st.metric("Overall scorecard achievement", f"{overall:.0f}%",
              "balanced" if df.groupby('Perspective')['Achievement %'].mean().min() >= 90 else "imbalanced",
              delta_color="normal" if overall >= 95 else "inverse")

with right:
    st.markdown("#### 🕸️ The Four-Perspective Balance")
    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=list(persp_scores.values) + [persp_scores.values[0]],
        theta=persp_order + [persp_order[0]],
        fill="toself", name="Achievement %",
        line=dict(color="#2e86de", width=2), fillcolor="rgba(46,134,222,0.25)",
    ))
    radar.add_trace(go.Scatterpolar(
        r=[100] * (len(persp_order) + 1),
        theta=persp_order + [persp_order[0]],
        name="Target (100%)", line=dict(color="#1e8449", width=1, dash="dash"),
    ))
    radar.update_layout(height=340, margin=dict(t=30, b=10),
                        polar=dict(radialaxis=dict(visible=True, range=[0, 130])),
                        legend=dict(orientation="h", y=1.15), showlegend=True)
    st.plotly_chart(radar, use_container_width=True)

# Perspective score cards
p1, p2, p3, p4 = st.columns(4)
for col, name in zip([p1, p2, p3, p4], persp_order):
    score = persp_scores[name]
    col.metric(name, f"{score:.0f}%",
               "on track" if score >= 95 else "below target",
               delta_color="normal" if score >= 95 else "inverse")

st.divider()

# ---- Strategy map ----
st.markdown("#### 🧭 The Strategy Map — cause and effect")
sm = go.Figure()
layers = [("Learning & Growth", "#8e44ad", 0),
          ("Internal Process", "#e67e22", 1),
          ("Customer", "#16a085", 2),
          ("Financial", "#2e86de", 3)]
for name, color, y in layers:
    score = persp_scores[name]
    sm.add_trace(go.Scatter(
        x=[0.5], y=[y], mode="markers+text",
        text=[f"{name}<br>{score:.0f}%"], textposition="middle center",
        textfont=dict(color="white", size=12),
        marker=dict(size=120, color=color, symbol="square"), showlegend=False))
for y in range(3):
    sm.add_annotation(x=0.5, y=y + 0.72, ax=0.5, ay=y + 0.28,
                      xref="x", yref="y", axref="x", ayref="y",
                      showarrow=True, arrowhead=3, arrowsize=1.5, arrowwidth=2,
                      arrowcolor="#95a5a6")
sm.add_annotation(x=0.85, y=1.5, text="drives ↑", showarrow=False,
                  font=dict(color="#5c6b7a", size=12))
sm.update_layout(height=430, margin=dict(t=10, b=10),
                 xaxis=dict(visible=False, range=[0, 1]),
                 yaxis=dict(visible=False, range=[-0.6, 3.6]),
                 plot_bgcolor="white")
st.plotly_chart(sm, use_container_width=True)
st.caption("Investment in Learning & Growth → better Internal Processes → improved Customer outcomes → "
           "stronger Financial results. Lower layers are the **leading drivers** of the top layer.")

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

weakest = persp_scores.idxmin()
strongest = persp_scores.idxmax()

st.markdown(
    f"""
- 🕸️ **Balance check:** strongest perspective is **{strongest} ({persp_scores[strongest]:.0f}%)**,
  weakest is **{weakest} ({persp_scores[weakest]:.0f}%)**. A truly *balanced* scorecard needs all four
  near target — a spike in one with a dip in another signals over-optimisation.
- 🧭 **Cause and effect:** because **{weakest}** sits {'low in the chain' if weakest in ['Learning & Growth','Internal Process'] else 'high in the chain'}, {'a weakness here will feed upward and undermine customer and financial results over time — fix the driver early.' if weakest in ['Learning & Growth','Internal Process'] else 'the weakness is a lagging outcome; trace it down to the process and capability drivers beneath it.'}
- 🎯 **Action:** prioritise initiatives that lift **{weakest}** back toward target, and watch whether
  improvement flows upward through the strategy map in later periods.
    """
)

if persp_scores.min() >= 95:
    st.success("**Well-balanced scorecard.** All four perspectives are at or near target — strategy is "
               "executing evenly across leading and lagging measures.", icon="✅")
else:
    st.warning(f"**Imbalance detected.** **{weakest}** is lagging at {persp_scores[weakest]:.0f}%. Because "
               f"the perspectives are causally linked, an untreated weakness low in the chain will erode "
               f"the perspectives above it. Rebalance before it shows up in the financials.", icon="⚠️")

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
        - [ ] Balance **financial (lagging)** with **non-financial (leading)** measures.
        - [ ] Cover all four perspectives: **Financial, Customer, Process, Learning & Growth**.
        - [ ] For each objective set a **measure, target and initiative**.
        - [ ] Respect **cause and effect** — lower perspectives drive the upper ones.
        - [ ] Don't over-optimise one perspective at the expense of another.
        """
    )
with a2:
    with st.expander("📘 The four perspectives & their question"):
        st.markdown(
            """
            - **Financial** — *How do we look to shareholders?*
            - **Customer** — *How do customers see us?*
            - **Internal Process** — *What must we excel at?*
            - **Learning & Growth** — *Can we keep improving and creating value?*
            """
        )
    with st.expander("🧭 Strengths & limitations"):
        st.markdown(
            """
            **Strengths:** links measures to strategy; balances short and long term; combines
            leading and lagging indicators; communicates strategy clearly.

            **Limitations:** choosing the right measures is hard; too many KPIs dilute focus;
            cause-and-effect links can be assumed rather than proven; needs strong data systems.
            """
        )

# Downloadable scorecard
export = df[["Perspective", "Objective (KPI)", "Target", "Actual", "Achievement %"]].copy()
st.download_button(
    "⬇️ Download the balanced scorecard (CSV)",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="balanced_scorecard.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 4.4 · Transfer Pricing", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 5.2 · KPIs & Critical Success Factors ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 5.1")
