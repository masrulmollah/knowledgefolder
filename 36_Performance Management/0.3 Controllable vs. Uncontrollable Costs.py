"""
Performance Management — Applied Learning Series
Module 0.3 · Controllable vs. Uncontrollable Costs
------------------------------------------------------------
The accountability principle in action: separate the costs a manager
can influence from those they cannot, and judge performance only on
the controllable portion.

Run with:  streamlit run 0.3_Controllable_vs_Uncontrollable_Costs.py
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
    page_title="0.3 · Controllable vs. Uncontrollable Costs",
    page_icon="⚖️",
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
                      background:#fafcff;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# ① HEADER ZONE
# ------------------------------------------------------------------
st.markdown('<p class="pill">MODULE 0 · FOUNDATIONS</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">0.3 · Controllable vs. Uncontrollable Costs</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: apply the <b>accountability principle</b> — separate costs a '
    'manager <b>can</b> influence from those they <b>cannot</b>, and evaluate performance on the '
    '<b>controllable</b> portion only.</p>',
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
A **controllable cost** is one a manager can significantly influence within a given time frame.
An **uncontrollable cost** is imposed from outside their authority — allocated head-office
overhead, group insurance, depreciation on assets they didn't choose, centrally-set prices.

The **accountability principle** states:

> **Hold managers responsible only for costs they can control.**

Three things shift a cost between the two buckets:

1. **Level of authority** — a plant manager controls line labour; the CFO controls group insurance.
2. **Time horizon** — almost everything is controllable in the long run; far less in a single month.
3. **Traceability** — apportioned/allocated costs are usually *uncontrollable* at the local level.

Mixing the two on a performance report is the single most common cause of **demotivation and
gaming** — managers stop trusting a scorecard that penalises them for things they can't change.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "A good responsibility report shows a **controllable profit** subtotal *before* charging "
        "allocated overhead. Managers are appraised on that line; the business is still assessed "
        "on the full picture below it. Both truths coexist — cleanly separated.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — Cost Classifier & Fair-Evaluation Report</p>',
            unsafe_allow_html=True)
st.caption("Toggle each cost line between controllable and uncontrollable, and watch the manager's "
           "fair scorecard separate from the full business result.")

# Default cost lines (factory-flavoured, editable)
default_rows = [
    {"Cost line": "Direct material",          "Amount": 1200, "Controllable": True},
    {"Cost line": "Direct labour",            "Amount": 800,  "Controllable": True},
    {"Cost line": "Line supervision",         "Amount": 300,  "Controllable": True},
    {"Cost line": "Utilities (metered)",      "Amount": 250,  "Controllable": True},
    {"Cost line": "Maintenance (local)",      "Amount": 180,  "Controllable": True},
    {"Cost line": "Allocated head-office OH", "Amount": 600,  "Controllable": False},
    {"Cost line": "Group insurance",          "Amount": 150,  "Controllable": False},
    {"Cost line": "Depreciation (central)",   "Amount": 400,  "Controllable": False},
]

left, right = st.columns([1.05, 1.35])

with left:
    st.markdown("#### 🎛️ Cost lines (editable)")
    df_in = pd.DataFrame(default_rows)
    edited = st.data_editor(
        df_in,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Cost line": st.column_config.TextColumn("Cost line"),
            "Amount": st.column_config.NumberColumn("Amount (BDT '000)", min_value=0, step=10),
            "Controllable": st.column_config.CheckboxColumn("Controllable?"),
        },
        key="cost_editor",
    )
    revenue = st.number_input("Division revenue (BDT '000)", 0, 1_000_000, 4000, step=100)

# ---- Calculations ----
edited = edited.fillna({"Amount": 0, "Controllable": False})
controllable   = edited.loc[edited["Controllable"] == True, "Amount"].sum()
uncontrollable = edited.loc[edited["Controllable"] == False, "Amount"].sum()
total_cost     = controllable + uncontrollable

controllable_profit = revenue - controllable          # manager is judged here
net_profit          = revenue - total_cost            # business is judged here
ctrl_share          = (controllable / total_cost * 100) if total_cost else 0

with right:
    st.markdown("#### 📊 Two subtotals, two audiences")
    m1, m2, m3 = st.columns(3)
    m1.metric("Controllable cost", f"{controllable:,.0f}", f"{ctrl_share:.0f}% of total")
    m2.metric("Controllable profit", f"{controllable_profit:,.0f}", "manager judged on this")
    m3.metric("Net profit", f"{net_profit:,.0f}", "business judged on this",
              delta_color="off")

    # Split bar: controllable vs uncontrollable
    split = go.Figure()
    split.add_bar(name="Controllable", x=["Costs"], y=[controllable], marker_color="#2e86de")
    split.add_bar(name="Uncontrollable", x=["Costs"], y=[uncontrollable], marker_color="#95a5a6")
    split.update_layout(barmode="stack", height=250, margin=dict(t=30, b=10),
                        legend=dict(orientation="h", y=1.2),
                        title="Cost split by controllability")
    st.plotly_chart(split, use_container_width=True)

# ---- Responsibility report waterfall ----
st.markdown("#### 🧾 Responsibility Report (the fair way to present it)")
wf = go.Figure(go.Waterfall(
    orientation="v",
    measure=["absolute", "relative", "total", "relative", "total"],
    x=["Revenue", "− Controllable cost", "Controllable profit",
       "− Uncontrollable cost", "Net profit"],
    y=[revenue, -controllable, None, -uncontrollable, None],
    connector={"line": {"color": "#b2bec3"}},
    decreasing={"marker": {"color": "#e67e22"}},
    increasing={"marker": {"color": "#2e86de"}},
    totals={"marker": {"color": "#8e44ad"}},
))
wf.update_layout(height=350, margin=dict(t=20, b=10),
                 title="Revenue → Controllable Profit → Net Profit")
st.plotly_chart(wf, use_container_width=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

cp_icon = "🟢" if controllable_profit >= 0 else "🔴"
np_icon = "🟢" if net_profit >= 0 else "🔴"

st.markdown(
    f"""
- {cp_icon} **Manager's scorecard (controllable profit):** **{controllable_profit:,.0f}** — this is what the manager should be appraised on, since it excludes the **{uncontrollable:,.0f}** of costs imposed from outside.
- {np_icon} **Business scorecard (net profit):** **{net_profit:,.0f}** — the full economic result of the division, including allocated costs.
- ⚖️ **Controllable costs are {ctrl_share:.0f}%** of the total cost base; the remaining **{100-ctrl_share:.0f}%** is outside the manager's authority.
    """
)

gap = controllable_profit - net_profit
if uncontrollable == 0:
    st.success(
        "**Verdict →** Every cost line is controllable, so the manager's scorecard equals the "
        "business result. Appraisal is straightforward here.",
        icon="✅",
    )
elif controllable_profit >= 0 and net_profit < 0:
    st.warning(
        f"**Verdict →** The manager delivers a **positive controllable profit ({controllable_profit:,.0f})**, "
        f"yet the division shows a **net loss ({net_profit:,.0f})** purely because of **{uncontrollable:,.0f}** "
        f"in uncontrollable allocations. Penalising the manager for this loss would be *unfair* and "
        f"demotivating — appraise on the controllable line, escalate the allocation issue separately.",
        icon="⚠️",
    )
else:
    st.info(
        f"**Verdict →** Uncontrollable allocations reduce the reported result by **{gap:,.0f}**. "
        f"Keep them *below* the controllable-profit line so the manager's performance is judged "
        f"cleanly, while the business still sees the full picture.",
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
        - [ ] Split every cost line into **controllable** vs **uncontrollable**.
        - [ ] Report a **controllable profit** subtotal *before* allocated overhead.
        - [ ] Appraise the manager on the **controllable line only**.
        - [ ] Remember: authority, **time horizon**, and traceability decide the bucket.
        - [ ] Keep allocations transparent — never hide them, just position them correctly.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Controllable cost** — significantly influenced by the manager in the period.
            - **Uncontrollable cost** — imposed externally (allocations, group charges).
            - **Accountability principle** — judge only on controllable items.
            - **Controllable profit** — revenue less controllable costs (the appraisal line).
            - **Apportioned / allocated cost** — shared cost split across units by a rule.
            - **Responsibility report** — a report structured around who controls what.
            """
        )

# Downloadable template — reflects current edits
out = edited.copy()
out["Bucket"] = np.where(out["Controllable"] == True, "Controllable", "Uncontrollable")
summary = pd.DataFrame({
    "Line": ["Revenue", "Controllable cost", "Controllable profit",
             "Uncontrollable cost", "Net profit"],
    "Amount (BDT '000)": [revenue, controllable, controllable_profit,
                          uncontrollable, net_profit],
})
csv_bytes = ("RESPONSIBILITY REPORT\n" + summary.to_csv(index=False) +
             "\nDETAIL\n" + out[["Cost line", "Amount", "Bucket"]].to_csv(index=False))
st.download_button(
    "⬇️ Download this responsibility report (CSV)",
    data=csv_bytes.encode("utf-8"),
    file_name="responsibility_report.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 0.2 · Responsibility Centres", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 1.1 · Absorption vs. Marginal Costing ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 0.3")
