"""
Performance Management — Applied Learning Series
Module 6.1 · Performance Dashboards & Reporting
------------------------------------------------------------
From measuring performance to COMMUNICATING it:
  • Dashboard design principles (audience, hierarchy, clarity)
  • RAG (Red-Amber-Green) status logic
  • Exception reporting & management by exception
  • A live management-dashboard mock-up

Run with:  streamlit run 6.1_Performance_Dashboards_and_Reporting.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="6.1 · Performance Dashboards & Reporting",
    page_icon="📊",
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
        .tile        {border-radius:12px; padding:14px 16px; color:white; margin-bottom:6px;}
        .tile h3     {margin:0; font-size:0.85rem; font-weight:600; opacity:0.95;}
        .tile .v     {font-size:1.6rem; font-weight:800; margin:2px 0;}
        .tile .s     {font-size:0.8rem; opacity:0.95;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# ① HEADER ZONE
# ------------------------------------------------------------------
st.markdown('<p class="pill">MODULE 6 · REPORTING, GOVERNANCE & APPLICATION</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">6.1 · Performance Dashboards & Reporting</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: turn measurement into <b>communication</b> — design clear performance '
    'dashboards, apply <b>RAG status</b> and <b>exception reporting</b>, and tailor reports to the '
    'audience so insight drives action.</p>',
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
Measuring performance is worthless if the message doesn't reach decision-makers clearly.
**Reporting and dashboards** are how measurement becomes **action**.

**Know your audience (the reporting hierarchy):**

- **Strategic (board/exec)** — highly summarised, a handful of headline KPIs, trends and
  outlook. *"Are we winning?"*
- **Tactical (senior/middle management)** — departmental performance vs. budget, variances,
  drill-down. *"Where do we act?"*
- **Operational (front line)** — detailed, frequent, real-time metrics. *"What's happening now?"*

**Dashboard design principles:**

- **One screen, one story** — the most important message visible at a glance.
- **Hierarchy** — headline KPIs first; detail on drill-down, not all at once.
- **Right visual for the data** — trends as lines, comparisons as bars, status as RAG.
- **Context always** — every figure vs. a target, prior period or benchmark.
- **Declutter** — remove chart-junk; maximise the data-to-ink ratio.

**RAG status (Red–Amber–Green)** gives instant visual triage:

- 🟢 **Green** — on or above target.
- 🟡 **Amber** — within tolerance but needs watching.
- 🔴 **Red** — outside tolerance; action required.

**Management by exception / exception reporting** focuses attention on the items that are
*off track*, rather than drowning managers in everything that is fine — the reporting
embodiment of the control loop from Module 0.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Finance produces the numbers *and* the story. A cluttered, undifferentiated report buries "
        "the signal; a well-designed dashboard with RAG and exceptions puts the two or three things "
        "that matter in front of the right person at the right time — turning data into decisions.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Live Dashboard Mock-up
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — Build a Management Dashboard</p>',
            unsafe_allow_html=True)
st.caption("Edit the KPI data and tolerances; the engine applies RAG status and produces a live dashboard with exceptions.")

cfg1, cfg2, cfg3 = st.columns(3)
with cfg1:
    audience = st.selectbox("Report audience", ["Strategic (board)", "Tactical (management)", "Operational (front line)"])
with cfg2:
    amber_tol = st.slider("Amber tolerance (%)", 1, 20, 5,
                          help="Within this % of target = Amber; beyond = Red.")
with cfg3:
    exceptions_only = st.checkbox("Exception reporting (show only Amber/Red)", value=False)

default = pd.DataFrame({
    "KPI": ["Revenue (BDT '000)", "Operating margin (%)", "ROCE (%)",
            "On-time delivery (%)", "First-pass yield (%)", "Cost per unit (BDT)",
            "Safety incidents", "Staff engagement (%)"],
    "Actual": [9200.0, 14.0, 16.5, 92.0, 96.0, 54.0, 3.0, 76.0],
    "Target": [10000.0, 15.0, 18.0, 95.0, 98.0, 50.0, 0.0, 80.0],
    "Lower is better": [False, False, False, False, False, True, True, False],
})
data = st.data_editor(
    default, num_rows="dynamic", use_container_width=True, hide_index=True,
    column_config={
        "Actual": st.column_config.NumberColumn(format="%.1f"),
        "Target": st.column_config.NumberColumn(format="%.1f"),
        "Lower is better": st.column_config.CheckboxColumn(),
    },
)

df = data.copy()
df = df[(df["Actual"].notna()) & (df["Target"].notna())].reset_index(drop=True)

def rag(row):
    a, t, lower = row["Actual"], row["Target"], row["Lower is better"]
    if t == 0:
        # target of zero (e.g. safety incidents): green only if actual <= 0 for lower-is-better
        if lower:
            return "🟢 Green" if a <= 0 else ("🟡 Amber" if a <= 1 else "🔴 Red")
        else:
            return "🟢 Green" if a >= 0 else "🔴 Red"
    # performance ratio where 1.0 = at target
    perf = (t / a) if lower else (a / t)
    if perf >= 1.0:
        return "🟢 Green"
    elif perf >= 1 - amber_tol / 100:
        return "🟡 Amber"
    else:
        return "🔴 Red"

df["RAG"] = df.apply(rag, axis=1)
df["Var %"] = df.apply(
    lambda r: round(((r["Target"] - r["Actual"]) / r["Target"] * 100) if (r["Lower is better"] and r["Target"]) else
                    ((r["Actual"] - r["Target"]) / r["Target"] * 100 if r["Target"] else 0), 1), axis=1)

# Counts
n_green = df["RAG"].str.contains("Green").sum()
n_amber = df["RAG"].str.contains("Amber").sum()
n_red = df["RAG"].str.contains("Red").sum()

# ---- KPI tiles ----
st.markdown("#### 🧭 Dashboard")
display_df = df[~df["RAG"].str.contains("Green")] if exceptions_only else df

color_map = {"🟢 Green": "#1e8449", "🟡 Amber": "#e67e22", "🔴 Red": "#c0392b"}
if len(display_df) == 0:
    st.success("No exceptions — every KPI is Green. 🎉", icon="✅")
else:
    tiles = st.columns(4)
    for i, (_, r) in enumerate(display_df.iterrows()):
        c = tiles[i % 4]
        bg = color_map[r["RAG"]]
        with c:
            st.markdown(
                f"""
                <div class="tile" style="background:{bg};">
                    <h3>{r['KPI']}</h3>
                    <div class="v">{r['Actual']:,.1f}</div>
                    <div class="s">Target {r['Target']:,.1f} · {r['Var %']:+.1f}% · {r['RAG'].split()[1]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ---- RAG summary + variance chart ----
s1, s2 = st.columns([1, 1.4])
with s1:
    st.markdown("#### 🚦 RAG Summary")
    donut = go.Figure(go.Pie(
        labels=["Green", "Amber", "Red"], values=[n_green, n_amber, n_red],
        marker=dict(colors=["#1e8449", "#e67e22", "#c0392b"]), hole=0.55,
        textinfo="value",
    ))
    donut.update_layout(height=260, margin=dict(t=10, b=10),
                        legend=dict(orientation="h", y=-0.1))
    st.plotly_chart(donut, use_container_width=True)

with s2:
    st.markdown("#### 📊 Variance vs. Target")
    colors = [color_map[r] for r in df["RAG"]]
    fig = go.Figure(go.Bar(
        x=df["Var %"], y=df["KPI"], orientation="h",
        marker_color=colors, text=[f"{v:+.1f}%" for v in df["Var %"]],
        textposition="outside",
    ))
    fig.add_vline(x=0, line=dict(color="#5c6b7a", width=1.5))
    fig.update_layout(height=300, margin=dict(t=10, b=10),
                      xaxis_title="Variance vs. target (%)", plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

audience_advice = {
    "Strategic (board)": "Keep this to the **5–7 headline KPIs** only, emphasise **trend and outlook**, "
                         "and lead with the exceptions — the board wants *'are we winning and what needs a decision?'*, not detail.",
    "Tactical (management)": "Show **performance vs. budget with drill-down** so managers can locate and act on "
                             "variances. RAG plus variance % is ideal at this level.",
    "Operational (front line)": "Provide **frequent, detailed, real-time** metrics with clear thresholds so the "
                                "team can self-correct during the shift, not after it.",
}

st.markdown(
    f"""
- 🚦 **Status:** **{n_green} Green · {n_amber} Amber · {n_red} Red** across {len(df)} KPIs.
  {'Attention needed — ' + str(n_red) + ' KPI(s) are Red and outside tolerance.' if n_red else 'No Red items — performance is broadly under control.'}
- 👥 **For a {audience} report:** {audience_advice[audience]}
- 🎯 **Management by exception:** toggling *exception reporting* strips out the Green items so managers
  see only what needs action — the reporting form of the control loop (Module 0).
    """
)

if n_red:
    reds = ", ".join(df[df["RAG"].str.contains("Red")]["KPI"].tolist())
    st.error(f"**Red exceptions requiring action:** {reds}. Pair each with a cause, an owner and a "
             f"corrective action in the commentary — numbers alone don't drive decisions.", icon="🔴")
else:
    st.success("**No Red exceptions.** Keep the dashboard focused on trend and early-warning Ambers so "
               "small issues are caught before they turn Red.", icon="✅")

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
        - [ ] Tailor the report to the **audience** (strategic / tactical / operational).
        - [ ] **One screen, one story** — headline first, detail on drill-down.
        - [ ] Give every number **context** (target, prior period, benchmark).
        - [ ] Use **RAG** for instant triage and **exception reporting** to focus attention.
        - [ ] Pair every Red with a **cause, owner and action** — not just a number.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Dashboard** — a single-view summary of key performance measures.
            - **RAG status** — Red/Amber/Green visual triage against tolerance.
            - **Exception reporting** — reporting only items outside tolerance.
            - **Management by exception** — focusing attention on the off-track few.
            - **Data-to-ink ratio** — maximise information, minimise clutter.
            - **Drill-down** — moving from summary to underlying detail on demand.
            """
        )
    with st.expander("🧭 Reporting hierarchy at a glance"):
        st.markdown(
            """
            | Level | Focus | Frequency | Detail |
            |---|---|---|---|
            | **Strategic** | Are we winning? | Monthly/Quarterly | Very high summary |
            | **Tactical** | Where to act? | Weekly/Monthly | Medium, vs. budget |
            | **Operational** | What's happening now? | Daily/Real-time | High detail |
            """
        )

# Downloadable dashboard
export = df[["KPI", "Actual", "Target", "Var %", "RAG"]].copy()
st.download_button(
    "⬇️ Download the dashboard status (CSV)",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="performance_dashboard.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 5.4 · Benchmarking", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 6.2 · Beyond Budgeting & Modern Frameworks ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 6.1")
