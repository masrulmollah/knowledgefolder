"""
Performance Management — Applied Learning Series
0.0 · Section Overview & Landing Page
------------------------------------------------------------
The single front door to the whole Performance Management section:
  • What the section covers and who it's for
  • The end-to-end learning journey (the closed loop)
  • All 26 modules across 7 modules, with progress tracking
  • Suggested learning paths and quick navigation

Run with:  streamlit run 0.0_Performance_Management_Overview.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Performance Management · Overview",
    page_icon="🎯",
    layout="wide",
)

# ------------------------------------------------------------------
# LIGHT THEME / STYLING (consistent with the site)
# ------------------------------------------------------------------
st.markdown(
    """
    <style>
        .hero-title  {font-size:2.6rem; font-weight:800; color:#1f3b57; margin-bottom:0;}
        .hero-sub    {color:#5c6b7a; font-size:1.15rem; margin-top:4px;}
        .big-title   {font-size:2.1rem; font-weight:800; color:#1f3b57; margin-bottom:0;}
        .subtle      {color:#5c6b7a; font-size:1.02rem;}
        .zone-header {font-size:1.4rem; font-weight:700; color:#1f3b57;
                      border-left:5px solid #2e86de; padding-left:10px; margin-top:8px;}
        .pill        {display:inline-block; padding:4px 12px; border-radius:14px;
                      background:#eaf2fb; color:#2e86de; font-weight:600; font-size:0.8rem;}
        .modcard     {border:1px solid #e3e8ee; border-radius:12px; padding:16px 18px;
                      background:#fbfcfe; height:100%;}
        .modcard h3  {margin:0 0 6px 0; font-size:1.05rem; color:#1f3b57;}
        .modcard p   {margin:0; color:#5c6b7a; font-size:0.9rem;}
        .done        {color:#1e8449; font-weight:700;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# HERO
# ------------------------------------------------------------------
st.markdown('<p class="pill">APPLIED LEARNING SERIES · FOR FINANCE PROFESSIONALS</p>',
            unsafe_allow_html=True)
st.markdown('<p class="hero-title">🎯 Performance Management</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-sub">From setting a budget to running a full factory performance review — '
    'learn the complete, end-to-end discipline of performance management through 26 hands-on, '
    'interactive modules.</p>',
    unsafe_allow_html=True,
)
st.divider()

# ------------------------------------------------------------------
# CURRICULUM DATA
# ------------------------------------------------------------------
curriculum = {
    "0 · Foundations": [
        ("0.1", "What is Performance Management", "The closed-loop cycle: plan → measure → evaluate → act", True),
        ("0.2", "Responsibility Centres", "Cost, revenue, profit and investment centres", True),
        ("0.3", "Controllable vs. Uncontrollable Costs", "The accountability principle", True),
    ],
    "1 · Costing Foundations": [
        ("1.1", "Absorption vs. Marginal Costing", "Profit impact and reconciliation", True),
        ("1.2", "Activity-Based Costing (ABC)", "Cost drivers and overhead allocation", True),
        ("1.3", "Cost Behaviour & CVP", "Break-even, contribution and margin of safety", True),
    ],
    "2 · Budgeting & Control": [
        ("2.1", "Budget Preparation", "Functional budgets into a master budget", True),
        ("2.2", "Flexible Budgets", "Flexing to actual activity; volume vs. expenditure", True),
        ("2.3", "Zero-Based & Rolling Budgets", "Modern budgeting approaches", True),
        ("2.4", "Behavioural Aspects of Budgeting", "Participation, slack, motivation", True),
    ],
    "3 · Variance Analysis": [
        ("3.1", "Material & Labour Variances", "Price/usage and rate/efficiency", True),
        ("3.2", "Overhead Variances", "Fixed & variable; capacity & efficiency", True),
        ("3.3", "Sales Variances", "Price, volume, mix and quantity", True),
        ("3.4", "Operating Statement & Reconciliation", "Budget-to-actual profit bridge", True),
        ("3.5", "Advanced Variances", "Planning vs. operational; mix & yield", True),
    ],
    "4 · Financial Performance": [
        ("4.1", "ROI & Residual Income", "Divisional return and the ROI–RI conflict", True),
        ("4.2", "Economic Value Added (EVA)", "NOPAT, WACC and shareholder value", True),
        ("4.3", "Ratio Analysis for Performance", "Profitability, efficiency, liquidity, gearing", True),
        ("4.4", "Transfer Pricing", "The negotiable range and goal congruence", True),
    ],
    "5 · Strategic & Non-Financial": [
        ("5.1", "The Balanced Scorecard", "Four perspectives and the strategy map", True),
        ("5.2", "KPIs & Critical Success Factors", "The CSF→KPI cascade and SMART test", True),
        ("5.3", "Non-Financial Performance Indicators", "Quality, delivery, people, sustainability", True),
        ("5.4", "Benchmarking", "Internal, competitive and best-in-class", True),
    ],
    "6 · Reporting, Governance & Application": [
        ("6.1", "Performance Dashboards & Reporting", "RAG status and exception reporting", True),
        ("6.2", "Beyond Budgeting & Modern Frameworks", "Adaptive planning and OKRs", True),
        ("6.3", "End-to-End Case Study", "A full factory performance review (capstone)", True),
    ],
}

# Progress numbers
all_modules = [m for mods in curriculum.values() for m in mods]
total = len(all_modules)
done = sum(1 for *_, d in all_modules if d)
pct = done / total * 100

# ------------------------------------------------------------------
# AT A GLANCE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">📌 At a Glance</p>', unsafe_allow_html=True)
g1, g2, g3, g4 = st.columns(4)
g1.metric("Modules", f"{len(curriculum)}")
g2.metric("Interactive lessons", f"{total}")
g3.metric("Completed", f"{done} / {total}")
g4.metric("Progress", f"{pct:.0f}%")

st.progress(pct / 100, text=f"Section progress · {done} of {total} lessons built")

c1, c2 = st.columns([1.35, 1])
with c1:
    st.markdown(
        """
**Who this is for.** Finance professionals — analysts, business partners, factory and
commercial finance managers — who want to master performance management *and apply it* on
the job, not just read the theory.

**What makes it different.** Every lesson is **hands-on**: you change real inputs and watch
break-even points, variances, ROI, scorecards and dashboards respond live. Concepts are
grounded in a **manufacturing / commercial finance** context, so the skills transfer straight
into practice.

**What you'll be able to do by the end.** Build and flex a budget, decompose any variance,
reconcile budget to actual profit, judge a division with ROI/RI/EVA, design a balanced
scorecard, set the right KPIs, benchmark performance, and report it all on a management
dashboard — then feed the insight back into the next plan.
        """
    )
with c2:
    st.info(
        "**How to use this section**\n\n"
        "Work through the modules **in order** for a complete learning journey, or jump to any "
        "lesson using the map below. Each lesson stands alone with its own concept, interactive "
        "model, interpretation and downloadable template.",
        icon="🧭",
    )

st.divider()

# ------------------------------------------------------------------
# THE LEARNING JOURNEY (closed loop)
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">🔄 The Learning Journey</p>', unsafe_allow_html=True)
st.caption("The whole section follows the performance-management loop — every module is one part of this cycle.")

jl, jr = st.columns([1, 1.1])
with jl:
    st.markdown(
        """
        The section is built around the **closed-loop cycle** introduced in Module 0.1:

        - **① Plan** — foundations, costing and budgeting *(Modules 0–2)*
        - **② Measure** — capturing actual results *(the bridge into Module 3)*
        - **③ Evaluate** — variances, divisional return, scorecards, benchmarking *(Modules 3–5)*
        - **④ Act** — reporting, decisions and modern frameworks *(Module 6)*, feeding the next plan

        Follow the loop and each module clicks into the next — culminating in the **6.3 capstone**,
        where all six stages run together on one factory.
        """
    )
with jr:
    loop = go.Figure()
    stages = ["① PLAN<br>(M0–2)", "② MEASURE<br>(→M3)", "③ EVALUATE<br>(M3–5)", "④ ACT<br>(M6)"]
    xs = [0, 1, 1, 0]
    ys = [1, 1, 0, 0]
    colors = ["#2e86de", "#16a085", "#8e44ad", "#e67e22"]
    order = [0, 1, 2, 3]
    for i in order:
        loop.add_trace(go.Scatter(
            x=[xs[i]], y=[ys[i]], mode="markers+text", text=[stages[i]],
            textposition="middle center", textfont=dict(color="white", size=12),
            marker=dict(size=120, color=colors[i]), showlegend=False))
    seq = [0, 1, 2, 3, 0]
    for i in range(4):
        a, b = seq[i], seq[i + 1]
        loop.add_annotation(x=xs[b], y=ys[b], ax=xs[a], ay=ys[a],
                            xref="x", yref="y", axref="x", ayref="y",
                            showarrow=True, arrowhead=3, arrowsize=1.4,
                            arrowwidth=2, arrowcolor="#95a5a6",
                            standoff=42, startstandoff=42)
    loop.update_layout(height=340, margin=dict(t=20, b=20, l=20, r=20),
                       xaxis=dict(visible=False, range=[-0.5, 1.5]),
                       yaxis=dict(visible=False, range=[-0.5, 1.5]),
                       plot_bgcolor="white")
    st.plotly_chart(loop, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# CURRICULUM MAP
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">🗺️ The Full Curriculum — 26 Interactive Lessons</p>',
            unsafe_allow_html=True)

module_icons = {
    "0 · Foundations": "🧱",
    "1 · Costing Foundations": "📊",
    "2 · Budgeting & Control": "🧾",
    "3 · Variance Analysis": "🧮",
    "4 · Financial Performance": "🏦",
    "5 · Strategic & Non-Financial": "🧭",
    "6 · Reporting, Governance & Application": "📑",
}

for mod, lessons in curriculum.items():
    icon = module_icons.get(mod, "📁")
    mod_done = sum(1 for *_, d in lessons if d)
    with st.expander(f"{icon}  Module {mod}   ·   {mod_done}/{len(lessons)} lessons ✅", expanded=True):
        cols = st.columns(2)
        for i, (num, title, desc, d) in enumerate(lessons):
            with cols[i % 2]:
                tick = "✅" if d else "⬜"
                st.markdown(
                    f"""
                    <div class="modcard">
                        <h3>{tick} {num} · {title}</h3>
                        <p>{desc}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.write("")

st.divider()

# ------------------------------------------------------------------
# SUGGESTED LEARNING PATHS
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">🧭 Suggested Learning Paths</p>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)
with p1:
    st.markdown("#### 🎓 Complete journey")
    st.markdown(
        """
        Work through **0.1 → 6.3** in order. The most thorough route — each module builds on
        the last and the capstone ties everything together.

        *Best for: building mastery from the ground up.*
        """
    )
with p2:
    st.markdown("#### ⚡ Variance fast-track")
    st.markdown(
        """
        **2.1 → 2.2 → 3.1 → 3.2 → 3.3 → 3.4**. Straight to budgeting and the variance engine,
        ending in the operating statement.

        *Best for: month-end reporting and cost control.*
        """
    )
with p3:
    st.markdown("#### 📈 Strategy & measurement")
    st.markdown(
        """
        **4.1 → 4.2 → 5.1 → 5.2 → 5.3 → 6.1**. Divisional return, scorecards and dashboards
        for the bigger picture.

        *Best for: business partnering and board reporting.*
        """
    )

st.divider()

# ------------------------------------------------------------------
# WHAT EACH LESSON CONTAINS
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">🧩 What Every Lesson Contains</p>', unsafe_allow_html=True)
st.markdown(
    """
    Each of the 26 lessons follows the same consistent **five-zone layout**, so you always know
    where to look:

    1. **① Header** — the module number, title and a one-line objective.
    2. **② Concept** — a clear explanation plus a *"why it matters in finance"* callout.
    3. **③ Interactive Model** — change the inputs and watch results, charts and status update live.
    4. **④ Interpretation** — dynamic commentary that reads the numbers and tells the story.
    5. **⑤ Apply It** — a takeaway checklist, key formulas, and a downloadable template for real work.
    """
)

st.divider()

# ------------------------------------------------------------------
# DOWNLOADABLE CURRICULUM MAP
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">⬇️ Take the Curriculum With You</p>', unsafe_allow_html=True)

rows = []
for mod, lessons in curriculum.items():
    for num, title, desc, d in lessons:
        rows.append({"Module": mod, "Lesson": num, "Title": title,
                     "Focus": desc, "Status": "Built" if d else "Planned"})
cur_df = pd.DataFrame(rows)
st.download_button(
    "⬇️ Download the full curriculum map (CSV)",
    data=cur_df.to_csv(index=False).encode("utf-8"),
    file_name="performance_management_curriculum.csv",
    mime="text/csv",
)

st.divider()
st.caption("Performance Management · Applied Learning Series · Section Overview (0.0)  ·  "
           f"{done} of {total} interactive lessons")
