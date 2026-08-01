"""
Performance Management — Applied Learning Series
Module 2.4 · Behavioural Aspects of Budgeting
------------------------------------------------------------
The human side of budgeting: participation vs. imposed budgets,
budget slack & gaming, target difficulty and motivation, and the
dysfunctional behaviours a badly designed budget can trigger.

Run with:  streamlit run 2.4_Behavioural_Aspects_of_Budgeting.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="2.4 · Behavioural Aspects of Budgeting",
    page_icon="🧠",
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
st.markdown('<p class="pill">MODULE 2 · BUDGETING & CONTROL</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">2.4 · Behavioural Aspects of Budgeting</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand the <b>human side</b> of budgeting — participation vs. '
    'imposed styles, <b>budget slack</b> and gaming, how <b>target difficulty</b> drives motivation, '
    'and the dysfunctional behaviours a poorly designed budget can trigger.</p>',
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
A budget is not just a set of numbers — it is a **behavioural tool** that shapes how
people act. Even a technically perfect budget will fail if it demotivates or invites
gaming.

**Budget styles — who sets the target?**

- **Top-down (imposed)** — senior management sets the budget and hands it down. Fast and
  goal-congruent, but can feel unfair and reduce commitment.
- **Bottom-up (participative)** — managers help set their own targets. Builds ownership,
  realism and morale — *but* opens the door to **budget slack**.

**Budget slack (padding)** — the deliberate under-estimation of revenue or over-estimation
of cost so the target is **easy to beat**. It makes managers look good but wastes resources
and distorts planning.

**Target difficulty and motivation.** Research (the aspiration-level effect) shows
performance is highest when a target is **challenging but achievable**. Too easy → little
effort; too hard → managers give up. The best *motivational* target is often tougher than
the best *planning/forecast* target — a genuine tension finance must manage.

**Dysfunctional behaviours** a bad budget can trigger:

- **Gaming / manipulation** — massaging numbers to hit the target.
- **Spending to budget** — "use it or lose it" spending near year-end.
- **Short-termism** — cutting value-adding spend (R&D, maintenance) to hit this year.
- **Blame culture** — treating every adverse variance as a fault rather than information.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "You can build a flawless master budget and still get poor results if managers pad it, "
        "game it, or disengage. Understanding the behavioural levers — participation, fair "
        "targets, how variances are used — is what turns a budget from a threat into a driver "
        "of performance.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — three tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

tab_style, tab_slack, tab_motiv = st.tabs(
    ["🎚️ Budget-Style Diagnostic", "🕵️ Budget-Slack Detector", "📈 Target Difficulty & Motivation"]
)

# ==================================================================
# TAB 1 — BUDGET STYLE DIAGNOSTIC
# ==================================================================
with tab_style:
    st.caption("Rate how your budgeting process actually works, and see where it sits on the imposed↔participative spectrum.")

    sl, sr = st.columns([1, 1.3])
    with sl:
        st.markdown("#### 🎛️ Rate your process (1 = not at all, 5 = fully)")
        q1 = st.slider("Managers help set their own targets", 1, 5, 3)
        q2 = st.slider("Targets feel fair and achievable", 1, 5, 3)
        q3 = st.slider("Two-way discussion before targets are fixed", 1, 5, 3)
        q4 = st.slider("Variances are used to learn, not to blame", 1, 5, 3)
        q5 = st.slider("Managers feel ownership of the budget", 1, 5, 3)

    participation = q1 + q2 + q3 + q4 + q5  # 5..25
    pct = (participation - 5) / 20 * 100

    with sr:
        st.markdown("#### 📊 Where you sit")
        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pct,
            number={"suffix": "%"},
            title={"text": "Participative index"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2e86de"},
                "steps": [
                    {"range": [0, 33], "color": "#f5b7b1"},
                    {"range": [33, 66], "color": "#fdebd0"},
                    {"range": [66, 100], "color": "#abebc6"},
                ],
            },
        ))
        gauge.update_layout(height=300, margin=dict(t=40, b=10))
        st.plotly_chart(gauge, use_container_width=True)

    if pct < 33:
        st.warning(
            "**Strongly imposed / top-down.** Targets are handed down with little dialogue. "
            "Expect fast goal-setting but weak ownership and possible resentment. Introduce some "
            "participation to lift commitment — without losing strategic control.",
            icon="⚠️",
        )
    elif pct < 66:
        st.info(
            "**Mixed / negotiated.** A blend of top-down direction and bottom-up input — often the "
            "healthiest balance. Keep watching for slack creeping in through participation.",
            icon="⚖️",
        )
    else:
        st.success(
            "**Strongly participative.** High ownership and morale. Guard against **budget slack** — "
            "the main risk of participation — by benchmarking and reviewing padded assumptions.",
            icon="✅",
        )

# ==================================================================
# TAB 2 — BUDGET SLACK DETECTOR
# ==================================================================
with tab_slack:
    st.caption("Compare a manager's submitted budget with a realistic benchmark to quantify hidden slack.")

    kl, kr = st.columns([1, 1.3])
    with kl:
        st.markdown("#### 🎛️ Inputs")
        bench_rev  = st.number_input("Realistic (benchmark) revenue (BDT)", 0, 1_000_000_000,
                                     10_000_000, step=100_000)
        sub_rev    = st.number_input("Manager's submitted revenue (BDT)", 0, 1_000_000_000,
                                     9_000_000, step=100_000)
        bench_cost = st.number_input("Realistic (benchmark) cost (BDT)", 0, 1_000_000_000,
                                     7_000_000, step=100_000)
        sub_cost   = st.number_input("Manager's submitted cost (BDT)", 0, 1_000_000_000,
                                     7_800_000, step=100_000)

    rev_slack  = bench_rev - sub_rev     # revenue understated => positive slack
    cost_slack = sub_cost - bench_cost   # cost overstated => positive slack
    total_slack = rev_slack + cost_slack

    bench_profit = bench_rev - bench_cost
    sub_profit   = sub_rev - sub_cost
    slack_pct = (total_slack / bench_profit * 100) if bench_profit else 0

    with kr:
        st.markdown("#### 📊 Slack analysis")
        m1, m2, m3 = st.columns(3)
        m1.metric("Revenue slack", f"{rev_slack:,.0f} BDT",
                  "understated" if rev_slack > 0 else "stretch")
        m2.metric("Cost slack", f"{cost_slack:,.0f} BDT",
                  "padded" if cost_slack > 0 else "tight")
        m3.metric("Total slack", f"{total_slack:,.0f} BDT",
                  f"{slack_pct:.0f}% of real profit")

        fig = go.Figure()
        fig.add_bar(name="Benchmark", x=["Revenue", "Cost", "Profit"],
                    y=[bench_rev, bench_cost, bench_profit], marker_color="#2e86de")
        fig.add_bar(name="Submitted", x=["Revenue", "Cost", "Profit"],
                    y=[sub_rev, sub_cost, sub_profit], marker_color="#e67e22")
        fig.update_layout(barmode="group", height=280, margin=dict(t=30, b=10),
                          legend=dict(orientation="h", y=1.2), yaxis_title="BDT",
                          plot_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

    if total_slack > 0:
        st.warning(
            f"**Slack detected: {total_slack:,.0f} BDT** ({slack_pct:.0f}% of realistic profit). "
            f"The submitted budget understates revenue and/or overstates cost, making the target "
            f"easy to beat. Challenge the padded assumptions, benchmark externally, and reward "
            f"**accuracy of forecasting**, not just beating a soft target.",
            icon="🕵️",
        )
    elif total_slack < 0:
        st.error(
            f"**Negative slack (over-stretch) of {abs(total_slack):,.0f} BDT.** The submitted target "
            f"is *tougher* than realistic — motivating in the short run, but risks demotivation and "
            f"gaming if managers conclude it is unachievable.",
            icon="🔴",
        )
    else:
        st.success("No slack — the submitted budget matches the realistic benchmark.", icon="✅")

# ==================================================================
# TAB 3 — TARGET DIFFICULTY & MOTIVATION
# ==================================================================
with tab_motiv:
    st.caption("Explore how target difficulty affects effort and actual performance — the aspiration-level effect.")

    ml, mr = st.columns([1, 1.4])
    with ml:
        st.markdown("#### 🎛️ Inputs")
        difficulty = st.slider("Target difficulty (0 = trivial, 100 = near-impossible)",
                               0, 100, 65)
        st.caption("Move the slider to see where your target lands on the motivation curve.")

    # Inverted-U aspiration curve: performance peaks at 'challenging but achievable'
    x = np.linspace(0, 100, 200)
    peak = 70  # motivational optimum
    performance = 100 * np.exp(-((x - peak) ** 2) / (2 * 22 ** 2))
    user_perf = 100 * np.exp(-((difficulty - peak) ** 2) / (2 * 22 ** 2))

    with mr:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=performance, name="Expected performance",
                                 line=dict(color="#2e86de", width=3)))
        fig.add_vline(x=peak, line=dict(color="#1e8449", dash="dash"),
                      annotation_text="motivational optimum", annotation_position="top")
        fig.add_trace(go.Scatter(x=[difficulty], y=[user_perf], mode="markers+text",
                                 text=[f"{user_perf:.0f}%"], textposition="top center",
                                 marker=dict(color="#e67e22", size=14),
                                 name="Your target"))
        fig.update_layout(height=360, margin=dict(t=30, b=10),
                          xaxis_title="Target difficulty", yaxis_title="Expected performance (%)",
                          legend=dict(orientation="h", y=1.15), plot_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

    if difficulty < 45:
        st.info(
            "**Target too easy.** Little effort is required, so performance sits well below "
            "potential and slack is likely. Raise the bar to stretch the team.",
            icon="🟡",
        )
    elif difficulty <= 80:
        st.success(
            "**Challenging but achievable — the motivational sweet spot.** This is where effort and "
            "performance peak. Use this level as the *motivational* target, even if the *planning* "
            "forecast is slightly softer.",
            icon="✅",
        )
    else:
        st.error(
            "**Target too hard.** Managers may conclude it is unachievable, give up, or resort to "
            "gaming. Bring it back toward the achievable zone to protect motivation.",
            icon="🔴",
        )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — designing a behaviourally smart budget</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 🤝 **Blend the styles:** combine top-down strategic direction with genuine bottom-up
  participation to win ownership *without* surrendering control.
- 🕵️ **Manage slack actively:** participation invites padding — counter it with benchmarking,
  challenge sessions, and by **rewarding forecast accuracy**, not just beating the target.
- 🎯 **Set challenging-but-achievable targets:** performance peaks in the sweet spot; recognise
  that the best *motivational* target may be tougher than the best *planning* forecast.
- 🧭 **Use variances to learn, not blame:** treat adverse variances as information for action
  (the loop from Module 0), which keeps managers honest and engaged.
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
        - [ ] A budget is a **behavioural** tool, not just a financial one.
        - [ ] **Participation** builds ownership but invites **budget slack**.
        - [ ] Best performance comes from **challenging-but-achievable** targets.
        - [ ] Separate the **motivational** target from the **planning** forecast.
        - [ ] Use variances to **learn**, not to blame — protect engagement.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Imposed (top-down) budget** — set by senior management.
            - **Participative (bottom-up) budget** — managers help set targets.
            - **Budget slack** — deliberate padding to make targets easy to beat.
            - **Goal congruence** — alignment of manager and organisation goals.
            - **Aspiration level** — the target difficulty that maximises effort.
            - **Dysfunctional behaviour** — gaming, spend-to-budget, short-termism.
            """
        )
    with st.expander("🎯 Motivational vs. planning targets"):
        st.markdown(
            """
            Organisations often run **two** versions of a target:
            - a **motivational** target (tougher, to drive effort), and
            - a **planning/forecast** target (realistic, for resourcing and cash).

            Keeping them distinct avoids padding the plan while still stretching the team.
            """
        )

# Downloadable checklist template
template = pd.DataFrame({
    "Behavioural lever": ["Budget style (imposed↔participative)", "Budget slack review",
                          "Target difficulty", "Motivational vs planning target",
                          "Use of variances", "Reward for forecast accuracy"],
    "Design question": [
        "Are managers meaningfully involved in setting their targets?",
        "Have submitted assumptions been benchmarked for padding?",
        "Is the target challenging but achievable?",
        "Are motivational and planning targets kept separate?",
        "Are variances used to learn rather than to blame?",
        "Do we reward accurate forecasting, not just beating soft targets?",
    ],
    "Status (Y/N)": ["", "", "", "", "", ""],
})
st.download_button(
    "⬇️ Download the behavioural budgeting design checklist (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="behavioural_budgeting_checklist.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 2.3 · Zero-Based & Rolling Budgets", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 3.1 · Material & Labour Variances ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 2.4")
