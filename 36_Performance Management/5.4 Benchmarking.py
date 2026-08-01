"""
Performance Management — Applied Learning Series
Module 5.4 · Benchmarking
------------------------------------------------------------
Learning by comparison — measuring performance against a reference
point to find and close gaps:
  • Types: internal, competitive, functional, best-in-class/generic
  • The gap analysis (our performance vs. benchmark)
  • The benchmarking cycle (plan -> analyse -> integrate -> act)

Run with:  streamlit run 5.4_Benchmarking.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="5.4 · Benchmarking",
    page_icon="📏",
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
st.markdown('<p class="big-title">5.4 · Benchmarking</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: use <b>benchmarking</b> to compare performance against a reference '
    'point — internal, competitive, functional or best-in-class — quantify the <b>gap</b>, and drive '
    'improvement through the benchmarking cycle.</p>',
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
**Benchmarking** is the process of comparing your performance, processes or practices against
a **reference point** — and then learning from the difference to improve. A measure means
little in isolation (Module 4.3); benchmarking supplies the **context** that turns a number
into a judgement.

**The main types of benchmarking:**

- **Internal** — compare against another division, site or team *within* the same organisation
  (e.g. one factory vs. another). Easy data access; limited by your own best being the ceiling.
- **Competitive** — compare against **direct competitors**. Highly relevant, but data is hard
  to obtain and often estimated.
- **Functional (process)** — compare a *function or process* against organisations in
  **different industries** who do it well (e.g. benchmark warehousing against a leading
  retailer). Fresh ideas, but adaptation needed.
- **Best-in-class / generic** — compare against the acknowledged **world's best**, regardless
  of sector. The most ambitious and transformative.

**Gap analysis** is the core tool: **Gap = Our performance − Benchmark**. A negative gap
(worse than benchmark) is an improvement opportunity; a positive gap is a competitive strength
to protect.

**The benchmarking cycle** — a continuous loop:

1. **Plan** — choose what to benchmark and against whom.
2. **Analyse** — gather data and quantify the gaps.
3. **Integrate** — set targets and communicate findings.
4. **Act** — implement, monitor and re-benchmark.

Benchmarking is powerful but must be used with care: **context matters** (different scale,
market or strategy can make a comparison misleading), and copying practices blindly rarely works.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Benchmarking is how you know whether a 16% ROCE or a 5-day cash cycle is *good*. It converts "
        "internal metrics into competitive intelligence, exposes where the business is leaving value "
        "on the table, and grounds stretch targets in what others have actually achieved — not "
        "guesswork.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Benchmark Gap Analyser
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Benchmark Gap Analyser</p>',
            unsafe_allow_html=True)
st.caption("Enter your performance and a chosen benchmark for each metric; the engine quantifies and ranks the gaps.")

bench_type = st.selectbox(
    "Benchmark type in use",
    ["Internal (sister site)", "Competitive (rival)", "Functional (other industry)",
     "Best-in-class (world's best)"],
)

default = pd.DataFrame({
    "Metric": ["Overall equipment effectiveness (%)", "First-pass yield (%)",
               "On-time delivery (%)", "Cost per unit (BDT)",
               "Order lead time (days)", "Staff turnover (%)"],
    "Our performance": [72.0, 96.0, 92.0, 54.0, 6.0, 11.0],
    "Benchmark": [85.0, 98.5, 97.0, 48.0, 4.0, 7.0],
    "Lower is better": [False, False, False, True, True, True],
})
data = st.data_editor(
    default, num_rows="dynamic", use_container_width=True, hide_index=True,
    column_config={
        "Our performance": st.column_config.NumberColumn(format="%.1f"),
        "Benchmark": st.column_config.NumberColumn(format="%.1f"),
        "Lower is better": st.column_config.CheckboxColumn(
            help="Tick for metrics where lower is better, e.g. cost, lead time, turnover."),
    },
)

df = data.copy()
df = df[(df["Our performance"].notna()) & (df["Benchmark"].notna())].reset_index(drop=True)

# Gap %: positive = we are BETTER than benchmark, negative = behind
def gap_pct(row):
    ours, bench, lower = row["Our performance"], row["Benchmark"], row["Lower is better"]
    if bench == 0:
        return 0.0
    if lower:
        return round((bench - ours) / bench * 100, 1)   # lower ours => positive (better)
    else:
        return round((ours - bench) / bench * 100, 1)   # higher ours => positive (better)

df["Gap %"] = df.apply(gap_pct, axis=1)
df["Status"] = np.where(df["Gap %"] >= 0, "✅ Ahead", "🔴 Behind")

left, right = st.columns([1.1, 1])
with left:
    st.markdown("#### 📊 Gap Analysis")
    show = df[["Metric", "Our performance", "Benchmark", "Gap %", "Status"]]
    st.dataframe(
        show.style.format({"Our performance": "{:,.1f}", "Benchmark": "{:,.1f}", "Gap %": "{:+.1f}%"}),
        use_container_width=True, hide_index=True,
    )
    ahead = (df["Gap %"] >= 0).sum()
    behind = (df["Gap %"] < 0).sum()
    avg_gap = df["Gap %"].mean() if len(df) else 0
    m1, m2, m3 = st.columns(3)
    m1.metric("Metrics ahead", f"{ahead}")
    m2.metric("Metrics behind", f"{behind}")
    m3.metric("Average gap", f"{avg_gap:+.1f}%",
              "net ahead" if avg_gap >= 0 else "net behind",
              delta_color="normal" if avg_gap >= 0 else "inverse")

with right:
    st.markdown("#### 📉 Gap by Metric")
    colors = ["#1e8449" if g >= 0 else "#c0392b" for g in df["Gap %"]]
    fig = go.Figure(go.Bar(
        x=df["Gap %"], y=df["Metric"], orientation="h",
        marker_color=colors, text=[f"{g:+.1f}%" for g in df["Gap %"]],
        textposition="outside",
    ))
    fig.add_vline(x=0, line=dict(color="#5c6b7a", width=1.5))
    fig.update_layout(height=340, margin=dict(t=20, b=10),
                      xaxis_title="Gap vs. benchmark (%)  ·  negative = behind",
                      plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

# Radar: ours vs benchmark (normalised so higher = better on every axis)
st.markdown("#### 🕸️ Performance vs. Benchmark (normalised — outer is better)")
def norm(row, col):
    ours, bench, lower = row["Our performance"], row["Benchmark"], row["Lower is better"]
    ref = bench if bench else 1
    if lower:
        return (ref / row[col]) * 100 if row[col] else 0
    else:
        return (row[col] / ref) * 100
radar = go.Figure()
ours_norm = [norm(r, "Our performance") for _, r in df.iterrows()]
bench_norm = [100 for _ in range(len(df))]
cats = list(df["Metric"])
if len(df) >= 3:
    radar.add_trace(go.Scatterpolar(r=ours_norm + [ours_norm[0]], theta=cats + [cats[0]],
                                    fill="toself", name="Us",
                                    line=dict(color="#2e86de", width=2),
                                    fillcolor="rgba(46,134,222,0.20)"))
    radar.add_trace(go.Scatterpolar(r=bench_norm + [bench_norm[0]], theta=cats + [cats[0]],
                                    name="Benchmark (100)",
                                    line=dict(color="#e67e22", width=1, dash="dash")))
    radar.update_layout(height=380, margin=dict(t=30, b=10),
                        polar=dict(radialaxis=dict(visible=True)),
                        legend=dict(orientation="h", y=1.12))
    st.plotly_chart(radar, use_container_width=True)
else:
    st.caption("Add at least three metrics to see the radar comparison.")

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

if len(df):
    biggest_gap = df.loc[df["Gap %"].idxmin()]
    biggest_lead = df.loc[df["Gap %"].idxmax()]

    st.markdown(
        f"""
- 🎯 **Biggest gap to close:** **{biggest_gap['Metric']}** at **{biggest_gap['Gap %']:+.1f}%** vs the
  benchmark — the priority improvement target. Study *how* the benchmark achieves it, then adapt.
- 🏆 **Biggest strength:** **{biggest_lead['Metric']}** at **{biggest_lead['Gap %']:+.1f}%** — a
  competitive advantage to protect and, ideally, to learn *from* internally.
- 📊 **Overall position:** on average you are **{avg_gap:+.1f}%** versus this **{bench_type}** benchmark,
  ahead on **{ahead}** of {len(df)} metrics and behind on **{behind}**.
        """
    )

    # Type-specific caution
    cautions = {
        "Internal (sister site)": "Internal benchmarking is easy but your best site is your ceiling — pair it with an external benchmark to avoid complacency.",
        "Competitive (rival)": "Competitive data is often estimated — validate sources before setting hard targets on it.",
        "Functional (other industry)": "Functional benchmarks bring fresh ideas but need adaptation — a practice that works elsewhere may not transfer directly.",
        "Best-in-class (world's best)": "Best-in-class targets are transformative but can demotivate if the gap feels unreachable — stage the journey with interim milestones.",
    }
    st.info(f"📌 **Using {bench_type}:** {cautions[bench_type]}", icon="📌")

    if avg_gap >= 0:
        st.success("**Net ahead of this benchmark.** Strong position — but benchmarking is continuous; "
                   "raise the reference point (e.g. move from internal to best-in-class) to keep improving.",
                   icon="✅")
    else:
        st.warning("**Net behind this benchmark.** Prioritise the largest, most strategically important "
                   "gaps, understand the root-cause practices behind them, and re-benchmark after acting.",
                   icon="⚠️")

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
        - [ ] Benchmarking gives a metric its **context** — good vs. what?
        - [ ] Know the type: **internal, competitive, functional, best-in-class**.
        - [ ] **Gap = Our performance − Benchmark**; prioritise the biggest strategic gaps.
        - [ ] Learn the **practices behind** the numbers, don't just copy targets.
        - [ ] Run the **cycle**: plan → analyse → integrate → act → re-benchmark.
        """
    )
with a2:
    with st.expander("📘 Types of benchmarking"):
        st.markdown(
            """
            | Type | Compare against | Trade-off |
            |---|---|---|
            | **Internal** | Own sites/teams | Easy data; limited ambition |
            | **Competitive** | Direct rivals | Relevant; hard data |
            | **Functional** | Other industries | Fresh ideas; needs adaptation |
            | **Best-in-class** | The world's best | Transformative; ambitious |
            """
        )
    with st.expander("🧭 The benchmarking cycle & cautions"):
        st.markdown(
            """
            **Cycle:** Plan → Analyse → Integrate → Act → (re-benchmark).

            **Cautions:** context differences (scale, market, strategy) can mislead;
            data may be unreliable; copying practices blindly rarely works; and
            benchmarking shows *what* others achieve, not always *how* — the real value
            is understanding the underlying practices.
            """
        )

# Downloadable gap analysis
export = df[["Metric", "Our performance", "Benchmark", "Gap %", "Status"]].copy()
st.download_button(
    "⬇️ Download the benchmark gap analysis (CSV)",
    data=export.to_csv(index=False).encode("utf-8"),
    file_name="benchmarking_gap_analysis.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 5.3 · Non-Financial Performance Indicators", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 6.1 · Performance Dashboards & Reporting ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 5.4")
