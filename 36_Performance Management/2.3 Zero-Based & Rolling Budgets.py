"""
Performance Management — Applied Learning Series
Module 2.3 · Zero-Based & Rolling Budgets
------------------------------------------------------------
Two modern budgeting approaches, side by side:
  • Zero-Based Budgeting (ZBB) — justify every cost from zero,
    build decision packages, rank them, fund down a priority list.
  • Rolling (continuous) Budgets — re-forecast each period and roll
    the horizon forward so a full budget always stretches ahead.

Run with:  streamlit run 2.3_Zero_Based_and_Rolling_Budgets.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="2.3 · Zero-Based & Rolling Budgets",
    page_icon="🔄",
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
st.markdown('<p class="big-title">2.3 · Zero-Based & Rolling Budgets</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: learn two modern alternatives to the traditional incremental '
    'budget — <b>Zero-Based Budgeting</b> (justify every cost from scratch) and <b>Rolling Budgets</b> '
    '(continuously re-forecast and extend the horizon) — and when each adds most value.</p>',
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
Traditional **incremental budgeting** takes last year's figures and adds a percentage.
It is quick, but it carries forward past inefficiencies and rarely challenges *why* a
cost exists. Two approaches tackle this:

**Zero-Based Budgeting (ZBB)** starts every budget from a **zero base**. No cost is
assumed — each activity must justify its funding from scratch. The steps are:

1. Break the organisation into **decision packages** (discrete activities).
2. For each package, describe its purpose, cost, and benefit — and the consequence of
   *not* funding it.
3. **Rank** the packages by value/priority.
4. **Allocate** the available funds down the ranked list until the budget is exhausted.

*Strengths:* eliminates waste, forces justification, focuses resources on value.
*Weaknesses:* time-consuming and costly to prepare; best applied periodically or to
discretionary/support costs.

**Rolling (continuous) Budgets** keep a budget continuously up to date. As each period
(e.g. a month or quarter) ends, it is dropped and a **new period is added at the far
end**, so a full budget horizon always stretches ahead. The remaining periods are
**re-forecast** using the latest information.

*Strengths:* always relevant, reduces forecast error, better for volatile conditions.
*Weaknesses:* more effort to maintain; can demotivate if targets change too often.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "ZBB is a powerful cost-transformation lever — exactly the discipline behind major "
        "savings programmes. Rolling budgets keep planning honest in fast-moving markets where "
        "an annual fixed budget goes stale within months. Knowing *when* to deploy each is a "
        "core finance-leadership skill.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

tab_zbb, tab_roll = st.tabs(["🧱 ZBB · Decision-Package Ranker", "🔄 Rolling-Budget Simulator"])

# ==================================================================
# TAB 1 — ZERO-BASED BUDGETING
# ==================================================================
with tab_zbb:
    st.caption("Score each activity, set a funding cap, and watch ZBB fund packages down the priority ranking.")

    zl, zr = st.columns([1, 1.4])

    with zl:
        st.markdown("#### 🎛️ Funding")
        fund_cap = st.number_input("Total funds available (BDT)", 0, 100_000_000,
                                   1_200_000, step=50_000)
        st.markdown("**Decision packages** — edit cost & value below")

    # Default decision packages (editable)
    default_pkgs = pd.DataFrame({
        "Decision package": ["Preventive maintenance", "Quality lab & testing",
                             "Staff training", "Line automation upgrade",
                             "Marketing samples", "Sustainability / waste reduction",
                             "Discretionary travel"],
        "Cost (BDT)":  [300000, 250000, 180000, 400000, 220000, 150000, 120000],
        "Value score (1-10)": [9, 8, 7, 8, 5, 6, 3],
    })

    with zr:
        st.markdown("#### 📝 Edit packages")
        pkgs = st.data_editor(
            default_pkgs, num_rows="dynamic", use_container_width=True, hide_index=True,
            column_config={
                "Cost (BDT)": st.column_config.NumberColumn(format="%d", min_value=0),
                "Value score (1-10)": st.column_config.NumberColumn(min_value=0, max_value=10),
            },
        )

    # ---- ZBB allocation logic ----
    work = pkgs.copy()
    work = work[work["Cost (BDT)"] > 0].reset_index(drop=True)
    # value per BDT drives ranking (benefit per unit of cost)
    work["Value / BDT"] = work["Value score (1-10)"] / work["Cost (BDT)"].replace(0, np.nan)
    work = work.sort_values(["Value / BDT", "Value score (1-10)"], ascending=False).reset_index(drop=True)

    remaining = fund_cap
    decisions, cum = [], 0
    for _, row in work.iterrows():
        if row["Cost (BDT)"] <= remaining:
            decisions.append("✅ Funded")
            remaining -= row["Cost (BDT)"]
            cum += row["Cost (BDT)"]
        else:
            decisions.append("❌ Not funded")
    work["Decision"] = decisions
    work["Rank"] = range(1, len(work) + 1)

    funded = work[work["Decision"] == "✅ Funded"]
    total_funded_cost = funded["Cost (BDT)"].sum()
    total_funded_value = funded["Value score (1-10)"].sum()
    total_value_all = work["Value score (1-10)"].sum()

    st.markdown("#### 📊 ZBB Allocation Result")
    zm1, zm2, zm3 = st.columns(3)
    zm1.metric("Packages funded", f"{len(funded)} of {len(work)}")
    zm2.metric("Funds committed", f"{total_funded_cost:,.0f} BDT",
               f"{fund_cap - total_funded_cost:,.0f} left")
    zm3.metric("Value captured", f"{total_funded_value:.0f} of {total_value_all:.0f}",
               f"{(total_funded_value/total_value_all*100 if total_value_all else 0):.0f}%")

    show = work[["Rank", "Decision package", "Cost (BDT)", "Value score (1-10)",
                 "Value / BDT", "Decision"]]
    st.dataframe(
        show.style.format({"Cost (BDT)": "{:,.0f}", "Value / BDT": "{:.5f}"}),
        use_container_width=True, hide_index=True,
    )

    if len(funded) < len(work):
        cutoff = work[work["Decision"] == "❌ Not funded"].iloc[0]
        st.warning(
            f"**Funding line drawn.** '{cutoff['Decision package']}' and lower-ranked packages "
            f"fall below the cut-off — under ZBB they must be justified anew or dropped. This is "
            f"the discipline ZBB forces: money follows **value per BDT**, not history.",
            icon="⚠️",
        )
    else:
        st.success("All packages fit within the funding cap — every activity earned its place.",
                   icon="✅")

# ==================================================================
# TAB 2 — ROLLING BUDGETS
# ==================================================================
with tab_roll:
    st.caption("Set a starting run-rate and watch the budget re-forecast and roll its 12-month horizon forward.")

    rl, rr = st.columns([1, 1.4])
    with rl:
        st.markdown("#### 🎛️ Inputs")
        base_month = st.number_input("Base monthly cost/revenue (BDT)", 0, 100_000_000,
                                     500_000, step=25_000)
        growth = st.slider("Expected monthly growth (%)", -10.0, 10.0, 2.0, step=0.5)
        elapsed = st.slider("Months already elapsed", 0, 11, 3,
                            help="How many months of the original budget are now actual.")
        actual_var = st.slider("Actual vs. plan so far (%)", -20.0, 20.0, 4.0, step=1.0,
                               help="How actual results have deviated, triggering a re-forecast.")

    # Build original 12-month budget
    months = [f"M{i}" for i in range(1, 13)]
    original = [base_month * ((1 + growth/100) ** i) for i in range(12)]

    # Actuals for elapsed months (original nudged by actual variance)
    actuals = [original[i] * (1 + actual_var/100) for i in range(elapsed)]

    # Rolling re-forecast: for remaining + newly added months, grow from latest actual run-rate
    if elapsed > 0:
        latest_runrate = actuals[-1]
    else:
        latest_runrate = base_month
    # Rolling budget always shows 12 months ahead from the current point
    rolling = []
    for k in range(12):
        rolling.append(latest_runrate * ((1 + growth/100) ** (k + 1)))
    rolling_months = [f"M{elapsed + i + 1}" for i in range(12)]

    with rr:
        st.markdown("#### 📈 Original Budget vs. Rolling Re-Forecast")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=original, name="Original 12-month budget",
                                 line=dict(color="#95a5a6", width=2, dash="dash")))
        if elapsed > 0:
            fig.add_trace(go.Scatter(x=months[:elapsed], y=actuals, name="Actuals to date",
                                     line=dict(color="#1e8449", width=3),
                                     mode="lines+markers"))
        fig.add_trace(go.Scatter(x=rolling_months, y=rolling, name="Rolling re-forecast",
                                 line=dict(color="#2e86de", width=3), mode="lines+markers"))
        fig.add_vrect(x0=-0.5, x1=elapsed - 0.5, fillcolor="#1e8449", opacity=0.06,
                      line_width=0, annotation_text="elapsed", annotation_position="top left")
        fig.update_layout(height=380, margin=dict(t=30, b=10), yaxis_title="BDT",
                          legend=dict(orientation="h", y=1.15), plot_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

    orig_year = sum(original)
    rolling_year = sum(rolling)
    reforecast_delta = rolling_year - orig_year

    rm1, rm2, rm3 = st.columns(3)
    rm1.metric("Original 12-mo total", f"{orig_year:,.0f} BDT")
    rm2.metric("Rolling 12-mo total", f"{rolling_year:,.0f} BDT",
               f"{reforecast_delta:+,.0f} vs original")
    rm3.metric("Horizon always ahead", "12 months",
               f"rolled +{elapsed} mo" if elapsed else "not yet rolled")

    st.info(
        f"After **{elapsed} month(s)**, those periods are dropped and **{elapsed} new month(s)** are "
        f"added at the far end — the budget still stretches a full 12 months ahead. The remaining "
        f"periods are **re-forecast** from the latest run-rate "
        f"({latest_runrate:,.0f} BDT), so the plan reflects reality rather than a stale annual number.",
        icon="🔄",
    )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — Which approach, when?</p>', unsafe_allow_html=True)

st.markdown(
    """
- 🧱 **Use ZBB when** costs are **discretionary or support-function** (marketing, training, IT,
  admin), when you suspect budget padding, or when running a **cost-transformation** programme.
  It reallocates money to the highest **value-per-BDT** activities and strips out legacy waste.
- 🔄 **Use rolling budgets when** the environment is **volatile or fast-changing**, when the
  annual budget goes stale quickly, or when management needs a **continuously current** view for
  decisions. It cuts forecast error at the cost of extra maintenance effort.
- ⚖️ **They are not mutually exclusive:** many organisations run a **rolling forecast** for
  agility *and* apply **ZBB periodically** (e.g. every few years) to reset the cost base.
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
        - [ ] **Incremental** budgeting carries forward yesterday's inefficiencies.
        - [ ] **ZBB** justifies every cost from zero and funds by **value per BDT**.
        - [ ] Build, describe and **rank decision packages**, then fund down the list.
        - [ ] **Rolling budgets** drop the old period and add a new one — always 12 ahead.
        - [ ] Re-forecast rolling periods from the **latest run-rate**, not the stale plan.
        """
    )
with a2:
    with st.expander("📘 Key terms in this module"):
        st.markdown(
            """
            - **Incremental budget** — last year ± a percentage.
            - **Zero-based budget (ZBB)** — every cost justified from a zero base.
            - **Decision package** — a discrete activity costed and ranked in ZBB.
            - **Rolling / continuous budget** — continuously extended and re-forecast.
            - **Run-rate** — the current period's result annualised/projected forward.
            - **Value per BDT** — benefit score ÷ cost; the ZBB ranking driver.
            """
        )
    with st.expander("⚖️ ZBB vs. Rolling — quick compare"):
        st.markdown(
            """
            | | **ZBB** | **Rolling** |
            |---|---|---|
            | Fixes | Cost waste / padding | Stale forecasts |
            | Effort | Very high (periodic) | Moderate (continuous) |
            | Best for | Discretionary costs | Volatile conditions |
            """
        )

# Downloadable ZBB result
zbb_csv = work[["Rank", "Decision package", "Cost (BDT)",
                "Value score (1-10)", "Value / BDT", "Decision"]].copy()
st.download_button(
    "⬇️ Download the ZBB ranking & funding decisions (CSV)",
    data=zbb_csv.to_csv(index=False).encode("utf-8"),
    file_name="zbb_decision_packages.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 2.2 · Flexible Budgets", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 2.4 · Behavioural Aspects of Budgeting ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 2.3")
