"""
Performance Management — Applied Learning Series
Module 0.1 · What is Performance Management
------------------------------------------------------------
An interactive introduction to the performance-management cycle:
Plan -> Measure -> Evaluate -> Act (the closed loop).

Run with:  streamlit run 0.1_What_is_Performance_Management.py
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
    page_title="0.1 · What is Performance Management",
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
st.markdown('<p class="pill">MODULE 0 · FOUNDATIONS</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">0.1 · What is Performance Management</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: understand performance management as a continuous, '
    'closed-loop process — <b>Plan → Measure → Evaluate → Act</b> — and see how each '
    'stage drives the next in a real finance setting.</p>',
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
**Performance management** is the continuous process of setting objectives, measuring
results against those objectives, evaluating the gap, and taking corrective action —
then feeding what you learn back into the next plan.

It is **not a one-off report**. It is a *loop* that keeps an organisation aligned with
its strategy. In finance, this is the engine behind budgeting, variance analysis, KPIs,
and management reporting.

**The four stages of the closed loop:**

1. **Plan** — set targets, budgets and standards (what *should* happen).
2. **Measure** — capture actual results (what *did* happen).
3. **Evaluate** — analyse the variance between plan and actual (the *gap*).
4. **Act** — take decisions to close the gap, then refine the next plan.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Every core finance activity — budgeting, standard costing, variance analysis, "
        "ROI, the Balanced Scorecard — is just one stage of this loop. Master the loop "
        "and every later module clicks into place.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — The Closed-Loop Simulator
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Closed-Loop Simulator</p>',
            unsafe_allow_html=True)
st.caption("Adjust the plan and the actual outcome, and watch the performance loop respond in real time.")

left, right = st.columns([1, 1.4])

with left:
    st.markdown("#### 🎛️ Inputs")
    st.markdown("**① PLAN — set your target**")
    target_output = st.number_input("Planned output (units)", 500, 100000, 10000, step=500)
    target_cost   = st.number_input("Planned cost per unit (BDT)", 1.0, 5000.0, 50.0, step=1.0)

    st.markdown("**② MEASURE — record the actual**")
    actual_output = st.number_input("Actual output (units)", 500, 100000, 9200, step=500)
    actual_cost   = st.number_input("Actual cost per unit (BDT)", 1.0, 5000.0, 54.0, step=1.0)

    tolerance = st.slider("Acceptable variance tolerance (%)", 1, 20, 5,
                          help="Variances within this band are treated as 'on track'.")

# ---- Calculations ----
planned_total = target_output * target_cost
actual_total  = actual_output * actual_cost

output_var    = actual_output - target_output
output_var_pct = (output_var / target_output) * 100 if target_output else 0

cost_var      = actual_cost - target_cost
cost_var_pct  = (cost_var / target_cost) * 100 if target_cost else 0

total_var     = actual_total - planned_total
total_var_pct = (total_var / planned_total) * 100 if planned_total else 0

with right:
    st.markdown("#### 📊 Results")
    m1, m2, m3 = st.columns(3)
    m1.metric("Output variance", f"{output_var:+,} u", f"{output_var_pct:+.1f}%",
              delta_color="normal")
    m2.metric("Unit-cost variance", f"{cost_var:+.1f}", f"{cost_var_pct:+.1f}%",
              delta_color="inverse")
    m3.metric("Total-cost variance", f"{total_var:+,.0f}", f"{total_var_pct:+.1f}%",
              delta_color="inverse")

    # Plan vs Actual bar
    fig = go.Figure()
    fig.add_bar(name="Plan", x=["Output (u)", "Total cost (BDT)"],
                x0=0, y=[target_output, planned_total], marker_color="#2e86de")
    fig.add_bar(name="Actual", x=["Output (u)", "Total cost (BDT)"],
                y=[actual_output, actual_total], marker_color="#e67e22")
    fig.update_layout(barmode="group", height=300, margin=dict(t=30, b=10),
                      legend=dict(orientation="h", y=1.15), title="Plan vs. Actual")
    st.plotly_chart(fig, use_container_width=True)

# ---- The Loop diagram ----
st.markdown("#### 🔄 The Performance-Management Loop")
loop = go.Figure()
stages = ["1 · PLAN", "2 · MEASURE", "3 · EVALUATE", "4 · ACT"]
angles = np.linspace(90, 90 - 360, len(stages) + 1)[:-1]
xs = np.cos(np.radians(angles))
ys = np.sin(np.radians(angles))
colors = ["#2e86de", "#16a085", "#8e44ad", "#e67e22"]
for i, s in enumerate(stages):
    loop.add_trace(go.Scatter(
        x=[xs[i]], y=[ys[i]], mode="markers+text", text=[s],
        textposition="middle center", textfont=dict(color="white", size=13),
        marker=dict(size=90, color=colors[i]), showlegend=False))
# arrows between nodes
for i in range(len(stages)):
    j = (i + 1) % len(stages)
    loop.add_annotation(x=xs[j]*0.78, y=ys[j]*0.78, ax=xs[i]*0.78, ay=ys[i]*0.78,
                        xref="x", yref="y", axref="x", ayref="y",
                        showarrow=True, arrowhead=3, arrowsize=1.5,
                        arrowwidth=2, arrowcolor="#95a5a6")
loop.update_layout(height=380, margin=dict(t=10, b=10, l=10, r=10),
                   xaxis=dict(visible=False, range=[-1.6, 1.6]),
                   yaxis=dict(visible=False, range=[-1.6, 1.6]),
                   plot_bgcolor="white")
st.plotly_chart(loop, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic commentary
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

def verdict(pct, favourable_when_negative=True):
    within = abs(pct) <= tolerance
    if within:
        return "on track", "🟢"
    if favourable_when_negative:
        return ("favourable", "🟢") if pct < 0 else ("adverse", "🔴")
    else:
        return ("favourable", "🟢") if pct > 0 else ("adverse", "🔴")

out_word, out_icon = verdict(output_var_pct, favourable_when_negative=False)
cost_word, cost_icon = verdict(cost_var_pct, favourable_when_negative=True)
tot_word, tot_icon = verdict(total_var_pct, favourable_when_negative=True)

st.markdown(
    f"""
- {out_icon} **Output:** actual output is **{output_var:+,} units ({output_var_pct:+.1f}%)** vs plan → *{out_word}*.
- {cost_icon} **Unit cost:** actual cost per unit is **{cost_var:+.1f} BDT ({cost_var_pct:+.1f}%)** vs plan → *{cost_word}*.
- {tot_icon} **Total cost:** overall spend is **{total_var:+,.0f} BDT ({total_var_pct:+.1f}%)** vs plan → *{tot_word}*.
    """
)

if abs(total_var_pct) <= tolerance:
    st.success(
        "**ACT →** Total variance is within tolerance. The plan is under control — "
        "continue monitoring and feed these results into the next planning cycle.",
        icon="✅",
    )
else:
    driver = "higher unit cost" if cost_var > 0 else "lower unit cost"
    vol = "lower volume" if output_var < 0 else "higher volume"
    st.warning(
        f"**ACT →** Total variance ({total_var_pct:+.1f}%) breaches the ±{tolerance}% tolerance. "
        f"The main drivers are **{driver}** and **{vol}**. Investigate root causes "
        f"(price, efficiency, demand), take corrective action, and revise the next plan. "
        f"This is the loop closing — *evaluate* leads directly to *act*.",
        icon="⚠️",
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
        - [ ] Every performance system is a **loop**, not a single report.
        - [ ] A target is meaningless without a **measurement** to compare it against.
        - [ ] The **variance** (gap) is where finance adds value — it points to action.
        - [ ] **Act** is the stage most organisations skip — don't.
        - [ ] Each cycle should **improve the next plan** (continuous improvement).
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Target/Standard** — the planned level of performance.
            - **Actual** — what really happened.
            - **Variance** — the difference between actual and plan.
            - **Favourable / Adverse** — variance that helps / hurts profit.
            - **Tolerance** — the acceptable variance band before action is triggered.
            - **Closed loop** — feeding results back into the next plan.
            """
        )

# Downloadable template
template = pd.DataFrame({
    "Metric":        ["Output (units)", "Cost per unit (BDT)", "Total cost (BDT)"],
    "Plan":          [target_output, target_cost, planned_total],
    "Actual":        [actual_output, actual_cost, actual_total],
    "Variance":      [output_var, cost_var, total_var],
    "Variance %":    [round(output_var_pct, 1), round(cost_var_pct, 1), round(total_var_pct, 1)],
})
st.download_button(
    "⬇️ Download this performance loop as a CSV template",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="performance_loop_template.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Section Home", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 0.2 · Responsibility Centres ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 0.1")
