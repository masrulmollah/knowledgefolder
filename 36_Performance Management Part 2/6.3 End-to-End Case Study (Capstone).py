"""
Performance Management — Applied Learning Series
Module 6.3 · End-to-End Case Study  (CAPSTONE)
------------------------------------------------------------
One integrated factory performance review that threads together the
whole section:
  Stage 1 · Budget (Module 2)
  Stage 2 · Variance analysis (Module 3)
  Stage 3 · Operating statement & reconciliation (Module 3.4)
  Stage 4 · Divisional return — ROI / RI / EVA (Module 4)
  Stage 5 · Balanced scorecard & NFPIs (Module 5)
  Stage 6 · Dashboard & the closed loop (Modules 6.1 / 0.1)

Run with:  streamlit run 6.3_End_to_End_Case_Study.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="6.3 · End-to-End Case Study",
    page_icon="🏭",
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
        .stage       {display:inline-block; padding:3px 10px; border-radius:10px;
                      background:#1f3b57; color:white; font-weight:600; font-size:0.8rem;}
        .good        {color:#1e8449; font-weight:700;}
        .bad         {color:#c0392b; font-weight:700;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# ① HEADER ZONE
# ------------------------------------------------------------------
st.markdown('<p class="pill">MODULE 6 · REPORTING, GOVERNANCE & APPLICATION · CAPSTONE</p>',
            unsafe_allow_html=True)
st.markdown('<p class="big-title">6.3 · End-to-End Case Study</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: run a <b>complete factory performance review</b> for a fictional plant '
    '— from budget to variances to divisional return to scorecard to dashboard — seeing how every '
    'module in this section connects into one continuous management cycle.</p>',
    unsafe_allow_html=True,
)
st.divider()

# ------------------------------------------------------------------
# ② CONCEPT / SCENARIO ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">② The Scenario</p>', unsafe_allow_html=True)

c1, c2 = st.columns([1.35, 1])
with c1:
    st.markdown(
        """
**Meet "Riverside Personal Care Factory" (RPC)** — a single-product soap plant operating as an
**investment centre** within a larger group. The board wants a full performance review for the
period just ended.

You are the factory finance manager. Using the live inputs below, you will thread the entire
section together in six connected stages:

1. **Budget** — set the plan (Module 2).
2. **Variances** — compare actual to a flexed standard (Module 3).
3. **Operating statement** — reconcile budgeted to actual profit (Module 3.4).
4. **Divisional return** — judge the plant with ROI, RI and EVA (Module 4).
5. **Scorecard & NFPIs** — check the balance beyond financials (Module 5).
6. **Dashboard & loop** — report it and close the cycle (Modules 6.1 & 0.1).

Every stage **feeds the next** — the actual profit from the operating statement drives the
divisional return; the whole picture lands on the board dashboard. Change an input at the top
and watch it flow all the way through.
        """
    )
with c2:
    st.info(
        "**How to use this capstone**\n\n"
        "Adjust the shared inputs once; each stage recalculates and the story updates end-to-end. "
        "This is exactly how a real performance review works — one set of facts, viewed through "
        "several complementary lenses, ending in a decision and a revised plan.",
        icon="🧭",
    )

st.divider()

# ------------------------------------------------------------------
# SHARED INPUTS
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Shared Case Inputs</p>', unsafe_allow_html=True)
st.caption("Set the facts of the case once — every stage below uses these.")

i1, i2, i3, i4 = st.columns(4)
with i1:
    st.markdown("**Volume & price**")
    bud_units = st.number_input("Budgeted output (units '000)", 1, 100000, 100, step=5)
    act_units = st.number_input("Actual output (units '000)", 1, 100000, 96, step=5)
    std_price = st.number_input("Std selling price (BDT)", 0.0, 100000.0, 100.0, step=1.0)
    act_price = st.number_input("Actual selling price (BDT)", 0.0, 100000.0, 98.0, step=1.0)
with i2:
    st.markdown("**Materials & labour (per unit)**")
    std_mat = st.number_input("Std material cost (BDT)", 0.0, 100000.0, 35.0, step=1.0)
    act_mat = st.number_input("Actual material cost (BDT)", 0.0, 100000.0, 37.0, step=1.0)
    std_lab = st.number_input("Std labour cost (BDT)", 0.0, 100000.0, 18.0, step=1.0)
    act_lab = st.number_input("Actual labour cost (BDT)", 0.0, 100000.0, 18.5, step=1.0)
with i3:
    st.markdown("**Overheads (total '000)**")
    bud_foh = st.number_input("Budgeted fixed OH (BDT '000)", 0, 10_000_000, 2000, step=100)
    act_foh = st.number_input("Actual fixed OH (BDT '000)", 0, 10_000_000, 2080, step=100)
    std_voh = st.number_input("Std variable OH/unit (BDT)", 0.0, 100000.0, 7.0, step=0.5)
    act_voh_tot = st.number_input("Actual variable OH (BDT '000)", 0, 10_000_000, 690, step=10)
with i4:
    st.markdown("**Capital & cost of capital**")
    capital = st.number_input("Capital employed (BDT '000)", 1, 100_000_000, 20000, step=500)
    coc = st.slider("Cost of capital / WACC (%)", 0.0, 30.0, 12.0, step=0.5)
    tax = st.slider("Tax rate (%)", 0.0, 50.0, 25.0, step=1.0)

# ------------------------------------------------------------------
# CALCULATIONS (all in BDT '000 where noted; per-unit in BDT)
# ------------------------------------------------------------------
# Contribution basis
std_var_cost = std_mat + std_lab + std_voh
std_contrib = std_price - std_var_cost

# ---- Stage 1: Budget ----
bud_revenue = bud_units * std_price                      # '000
bud_var_cost = bud_units * std_var_cost
bud_contrib = bud_revenue - bud_var_cost
bud_profit = bud_contrib - bud_foh                       # budgeted profit '000

# ---- Stage 2: Variances (all '000, +F / -A) ----
# Sales
sales_price_var = (act_price - std_price) * act_units
sales_vol_var = (act_units - bud_units) * std_contrib
# Material (flex to actual output)
mat_total_var = (std_mat - act_mat) * act_units
# Labour
lab_total_var = (std_lab - act_lab) * act_units
# Variable OH: std allowance vs actual
voh_flexed = act_units * std_voh
voh_var = voh_flexed - act_voh_tot
# Fixed OH expenditure
foh_exp_var = bud_foh - act_foh
# Fixed OH volume (absorption): (actual - budget units) x std FOH/unit
std_foh_pu = bud_foh / bud_units if bud_units else 0
foh_vol_var = (act_units - bud_units) * std_foh_pu

variances = [
    ("Sales price", sales_price_var),
    ("Sales volume", sales_vol_var),
    ("Material total", mat_total_var),
    ("Labour total", lab_total_var),
    ("Variable OH", voh_var),
    ("Fixed OH expenditure", foh_exp_var),
    ("Fixed OH volume", foh_vol_var),
]
net_var = sum(v for _, v in variances)

# ---- Stage 3: Operating statement ----
actual_profit = bud_profit + net_var
total_fav = sum(v for _, v in variances if v > 0)
total_adv = sum(v for _, v in variances if v < 0)

# ---- Stage 4: Divisional return ----
roi = actual_profit / capital * 100 if capital else 0
ri = actual_profit - capital * coc / 100
# Simple EVA: NOPAT = profit x (1-tax); charge WACC on capital
nopat = actual_profit * (1 - tax / 100)
eva = nopat - capital * coc / 100

# ------------------------------------------------------------------
# STAGE TABS
# ------------------------------------------------------------------
st.divider()
st.markdown('<p class="zone-header">④ The Review — Six Connected Stages</p>', unsafe_allow_html=True)

s1, s2, s3, s4, s5, s6 = st.tabs([
    "1 · Budget", "2 · Variances", "3 · Operating Statement",
    "4 · Divisional Return", "5 · Scorecard & NFPIs", "6 · Dashboard & Loop"])

# ---------- STAGE 1 ----------
with s1:
    st.markdown('<span class="stage">STAGE 1 · MODULE 2 — THE BUDGET</span>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    a.metric("Budgeted revenue", f"{bud_revenue:,.0f}k")
    b.metric("Std contribution/unit", f"{std_contrib:,.1f}")
    c.metric("Budgeted profit", f"{bud_profit:,.0f}k")
    tbl = pd.DataFrame({
        "Line": ["Revenue", "Variable cost", "Contribution", "Fixed overhead", "Budgeted profit"],
        "BDT '000": [bud_revenue, -bud_var_cost, bud_contrib, -bud_foh, bud_profit],
    })
    st.dataframe(tbl.style.format({"BDT '000": "{:,.0f}"}), use_container_width=True, hide_index=True)
    st.caption("This budgeted profit is the anchor the whole review reconciles from.")

# ---------- STAGE 2 ----------
with s2:
    st.markdown('<span class="stage">STAGE 2 · MODULE 3 — VARIANCE ANALYSIS</span>', unsafe_allow_html=True)
    vdf = pd.DataFrame(variances, columns=["Variance", "BDT '000"])
    vdf["F/A"] = np.where(vdf["BDT '000"] >= 0, "Favourable", "Adverse")
    colors = ["#1e8449" if v >= 0 else "#c0392b" for v in vdf["BDT '000"]]
    fig = go.Figure(go.Bar(x=vdf["BDT '000"], y=vdf["Variance"], orientation="h",
                           marker_color=colors, text=[f"{v:+,.0f}" for v in vdf["BDT '000"]],
                           textposition="outside"))
    fig.add_vline(x=0, line=dict(color="#5c6b7a", width=1.5))
    fig.update_layout(height=320, margin=dict(t=20, b=10), xaxis_title="BDT '000  (+F / −A)",
                      plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(vdf.style.format({"BDT '000": "{:+,.0f}"}), use_container_width=True, hide_index=True)
    st.caption(f"Net variance = {net_var:+,.0f}k. Note the interacting story: an adverse material "
               f"variance alongside the volume shortfall — the classic factory pattern from Module 3.1.")

# ---------- STAGE 3 ----------
with s3:
    st.markdown('<span class="stage">STAGE 3 · MODULE 3.4 — OPERATING STATEMENT</span>', unsafe_allow_html=True)
    wf_x = ["Budgeted profit"] + [n for n, _ in variances] + ["Actual profit"]
    wf_y = [bud_profit] + [v for _, v in variances] + [actual_profit]
    wf = go.Figure(go.Waterfall(
        orientation="v", measure=["absolute"] + ["relative"]*len(variances) + ["total"],
        x=wf_x, y=wf_y,
        text=[f"{bud_profit:,.0f}"] + [f"{v:+,.0f}" for _, v in variances] + [f"{actual_profit:,.0f}"],
        textposition="outside", connector={"line": {"color": "#b0b7bf"}},
        increasing={"marker": {"color": "#1e8449"}}, decreasing={"marker": {"color": "#e67e22"}},
        totals={"marker": {"color": "#2e86de"}}))
    wf.update_layout(height=420, margin=dict(t=30, b=90), yaxis_title="BDT '000",
                     xaxis_tickangle=-40, plot_bgcolor="white")
    st.plotly_chart(wf, use_container_width=True)
    a, b, c = st.columns(3)
    a.metric("Budgeted profit", f"{bud_profit:,.0f}k")
    b.metric("Net variance", f"{net_var:+,.0f}k",
             "favourable" if net_var >= 0 else "adverse",
             delta_color="normal" if net_var >= 0 else "inverse")
    c.metric("Actual profit", f"{actual_profit:,.0f}k")
    st.caption("Reconciliation holds: budgeted profit + Σ favourable − Σ adverse = actual profit. "
               "This actual profit now drives Stage 4.")

# ---------- STAGE 4 ----------
with s4:
    st.markdown('<span class="stage">STAGE 4 · MODULE 4 — DIVISIONAL RETURN</span>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    a.metric("ROI", f"{roi:.1f}%", f"vs {coc:.1f}% CoC",
             delta_color="normal" if roi >= coc else "inverse")
    b.metric("Residual Income", f"{ri:,.0f}k",
             "value created" if ri >= 0 else "value destroyed",
             delta_color="normal" if ri >= 0 else "inverse")
    c.metric("EVA", f"{eva:,.0f}k",
             "value created" if eva >= 0 else "value destroyed",
             delta_color="normal" if eva >= 0 else "inverse")
    fig = go.Figure(go.Bar(
        x=["ROI (%)", "Cost of capital (%)"], y=[roi, coc],
        marker_color=["#2e86de", "#95a5a6"], text=[f"{roi:.1f}%", f"{coc:.1f}%"],
        textposition="outside"))
    fig.update_layout(height=280, margin=dict(t=20, b=10), plot_bgcolor="white",
                      title="Return vs. the cost of capital")
    st.plotly_chart(fig, use_container_width=True)
    verdict = ("creates" if ri >= 0 else "destroys")
    st.caption(f"On the actual profit of {actual_profit:,.0f}k against {capital:,.0f}k of capital, the "
               f"plant {verdict} value: ROI {roi:.1f}% vs {coc:.1f}% cost of capital, RI {ri:,.0f}k, EVA {eva:,.0f}k.")

# ---------- STAGE 5 ----------
with s5:
    st.markdown('<span class="stage">STAGE 5 · MODULE 5 — SCORECARD & NFPIs</span>', unsafe_allow_html=True)
    st.caption("Financials alone don't tell the whole story — check the balance across perspectives.")
    # Financial score derived from actual vs budget profit; others are case inputs
    fin_score = min(actual_profit / bud_profit * 100, 130) if bud_profit else 0
    cust = st.slider("Customer — on-time delivery achievement (%)", 0, 130, 96)
    proc = st.slider("Internal process — first-pass yield achievement (%)", 0, 130, 97)
    learn = st.slider("Learning & growth — engagement achievement (%)", 0, 130, 92)
    persp = {"Financial": fin_score, "Customer": cust, "Internal Process": proc, "Learning & Growth": learn}
    cats = list(persp.keys()); vals = list(persp.values())
    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(r=vals + [vals[0]], theta=cats + [cats[0]], fill="toself",
                                    line=dict(color="#16a085", width=2),
                                    fillcolor="rgba(22,160,133,0.25)", name="Achievement"))
    radar.add_trace(go.Scatterpolar(r=[100]*(len(cats)+1), theta=cats + [cats[0]],
                                    line=dict(color="#1e8449", dash="dash"), name="Target"))
    radar.update_layout(height=360, margin=dict(t=30, b=10),
                        polar=dict(radialaxis=dict(visible=True, range=[0, 130])),
                        legend=dict(orientation="h", y=1.12))
    st.plotly_chart(radar, use_container_width=True)
    weakest = min(persp, key=persp.get)
    st.caption(f"Financial achievement is {fin_score:.0f}% of budget, but the weakest perspective is "
               f"**{weakest} ({persp[weakest]:.0f}%)** — a leading-risk signal (Module 5.3) to address "
               f"before it feeds through to future financials.")

# ---------- STAGE 6 ----------
with s6:
    st.markdown('<span class="stage">STAGE 6 · MODULES 6.1 & 0.1 — DASHBOARD & THE LOOP</span>',
                unsafe_allow_html=True)
    # Build a board dashboard with RAG
    dash = pd.DataFrame({
        "KPI": ["Profit vs budget", "ROI vs CoC", "EVA", "On-time delivery", "First-pass yield", "Engagement"],
        "Status value": [actual_profit/bud_profit*100 if bud_profit else 0,
                         roi - coc + 100, 100 + (eva/abs(bud_profit)*100 if bud_profit else 0),
                         cust, proc, learn],
    })
    def rag(v):
        return "🟢 Green" if v >= 100 else ("🟡 Amber" if v >= 95 else "🔴 Red")
    dash["RAG"] = dash["Status value"].apply(rag)
    ng = dash["RAG"].str.contains("Green").sum()
    na = dash["RAG"].str.contains("Amber").sum()
    nr = dash["RAG"].str.contains("Red").sum()
    a, b, c = st.columns(3)
    a.metric("🟢 Green", ng); b.metric("🟡 Amber", na); c.metric("🔴 Red", nr)
    st.dataframe(dash[["KPI", "RAG"]], use_container_width=True, hide_index=True)

    st.markdown("#### 🔄 Closing the loop (Module 0.1)")
    st.markdown(
        f"""
        **Plan → Measure → Evaluate → Act.** The review is complete:
        - **Plan:** budgeted profit was **{bud_profit:,.0f}k**.
        - **Measure:** actual profit came in at **{actual_profit:,.0f}k** ({net_var:+,.0f}k vs plan).
        - **Evaluate:** ROI **{roi:.1f}%** vs **{coc:.1f}%** CoC; EVA **{eva:,.0f}k**; weakest scorecard
          perspective **{min(persp, key=persp.get)}**.
        - **Act:** address the largest adverse variance and the weakest non-financial perspective, then
          **feed both into next period's budget and targets** — restarting the cycle.
        """
    )
    if actual_profit >= bud_profit and ri >= 0:
        st.success("**Overall verdict: a solid period.** Profit near/above plan and value created after "
                   "the capital charge. Protect the strengths and close the non-financial gap.", icon="✅")
    else:
        st.warning("**Overall verdict: action needed.** Either profit fell short of plan or the plant isn't "
                   "covering its cost of capital. Prioritise the biggest drivers and revise the plan.", icon="⚠️")

st.divider()

# ------------------------------------------------------------------
# ⑤ APPLY IT ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">⑤ Apply It — the whole section in one picture</p>', unsafe_allow_html=True)

a1, a2 = st.columns([1, 1])
with a1:
    st.markdown("**What this capstone demonstrates**")
    st.markdown(
        """
        - [ ] The **budget** (M2) sets the benchmark for everything that follows.
        - [ ] **Variances** (M3) explain the gap and reconcile to **actual profit** (M3.4).
        - [ ] That profit drives **ROI / RI / EVA** (M4) — is capital being used well?
        - [ ] The **scorecard & NFPIs** (M5) test whether results are *balanced and sustainable*.
        - [ ] The **dashboard** (M6.1) communicates it, and the **loop** (M0.1) feeds the next plan.
        """
    )
with a2:
    with st.expander("🎓 The performance-management cycle — full recap"):
        st.markdown(
            """
            **Plan** (budgets, standards) → **Measure** (actuals) → **Evaluate**
            (variances, ROI/RI/EVA, scorecard, benchmarking) → **Act** (decisions,
            reporting, revised plan) → back to **Plan**.

            Every module in this section is one part of this single, continuous loop —
            that is the core message of the whole Performance Management course.
            """
        )
    with st.expander("🏭 Extend the case yourself"):
        st.markdown(
            """
            - Push **actual output** well below budget and watch the fixed-OH **volume** variance and
              **ROI** deteriorate together.
            - Raise **material cost** and see the operating statement, EVA and dashboard all turn.
            - Drop a **non-financial** slider and note how the scorecard flags risk *before* the
              financials move — the essence of leading indicators.
            """
        )

# Downloadable executive summary
summary = pd.DataFrame({
    "Metric": ["Budgeted profit (000)", "Net variance (000)", "Actual profit (000)",
               "ROI (%)", "Cost of capital (%)", "Residual income (000)", "EVA (000)"],
    "Value": [round(bud_profit), round(net_var), round(actual_profit),
              round(roi, 1), coc, round(ri), round(eva)],
})
st.download_button(
    "⬇️ Download the executive performance summary (CSV)",
    data=summary.to_csv(index=False).encode("utf-8"),
    file_name="rpc_performance_review_summary.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 6.2 · Beyond Budgeting & Modern Frameworks", use_container_width=True, disabled=True)
with nav3:
    st.button("🎓 Section complete!", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 6.3 · CAPSTONE")
