"""
Performance Management — Applied Learning Series
Module 4.1 · ROI & Residual Income
------------------------------------------------------------
Divisional performance measurement:
  • Return on Investment (ROI) = Controllable profit / Capital employed
  • Residual Income (RI)        = Profit - (Capital x Cost of capital)
Plus the classic ROI-vs-RI conflict: why ROI can push a manager to
REJECT a project that RI (and the company) would ACCEPT.

Run with:  streamlit run 4.1_ROI_and_Residual_Income.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="4.1 · ROI & Residual Income",
    page_icon="🏦",
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
st.markdown('<p class="pill">MODULE 4 · PERFORMANCE MEASUREMENT — FINANCIAL</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">4.1 · ROI & Residual Income</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: measure divisional performance with <b>Return on Investment (ROI)</b> '
    'and <b>Residual Income (RI)</b>, and understand the classic <b>conflict</b> where ROI drives a '
    'manager to reject a project the company should accept.</p>',
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
When an organisation is divided into **investment centres**, each manager controls both
profit *and* the capital tied up in their division. We need measures that capture **return
relative to the capital employed**.

**Return on Investment (ROI)** — a percentage:

- **ROI = Controllable (divisional) profit ÷ Capital employed × 100**

It can be decomposed (the DuPont view):

- **ROI = Profit margin × Asset turnover** = (Profit ÷ Sales) × (Sales ÷ Capital)

*Strength:* intuitive, comparable across divisions of different sizes.
*Weakness:* it is a **ratio**, so it can encourage **dysfunctional decisions** — a manager
may reject a good project because it lowers their *average* ROI, even though it earns above
the company's cost of capital.

**Residual Income (RI)** — an absolute money amount:

- **RI = Controllable profit − (Capital employed × Cost of capital %)**

The term *(Capital × cost of capital)* is the **imputed interest charge** — the minimum
return the company requires on the capital. Any RI above zero is value created *after*
covering the cost of capital.

*Strength:* promotes **goal congruence** — a manager accepts any project with positive RI,
which is exactly what benefits the company.
*Weakness:* an absolute figure, so it is **harder to compare** divisions of different sizes.

**The key tension:** ROI (a ratio) and RI (an absolute) can rank the same decision
differently — the heart of this module.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "How you *measure* a division shapes how its manager *behaves*. Reward ROI alone and you "
        "may see managers starve growth to protect a headline percentage. RI aligns the manager's "
        "self-interest with shareholder value — a core lesson in designing performance metrics.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

tab_calc, tab_conflict = st.tabs(["📐 ROI & RI Calculator", "⚔️ The ROI-vs-RI Conflict"])

# ==================================================================
# TAB 1 — CALCULATOR
# ==================================================================
with tab_calc:
    st.caption("Enter divisional profit, capital and the cost of capital to compute ROI and RI together.")

    cl, cr = st.columns([1, 1.5])
    with cl:
        st.markdown("#### 🎛️ Inputs")
        profit  = st.number_input("Controllable divisional profit (BDT)", -1_000_000_000, 1_000_000_000,
                                  900_000, step=10_000)
        capital = st.number_input("Capital employed (BDT)", 1, 10_000_000_000, 5_000_000, step=100_000)
        coc     = st.slider("Cost of capital (%)", 0.0, 30.0, 12.0, step=0.5)
        sales   = st.number_input("Divisional sales (BDT) — for DuPont", 0, 10_000_000_000,
                                  8_000_000, step=100_000)

    roi = profit / capital * 100 if capital else 0
    imputed = capital * coc / 100
    ri = profit - imputed
    margin = profit / sales * 100 if sales else 0
    turnover = sales / capital if capital else 0

    with cr:
        st.markdown("#### 📊 Result")
        a, b, c = st.columns(3)
        a.metric("ROI", f"{roi:.1f}%", f"vs {coc:.1f}% CoC",
                 delta_color="normal" if roi >= coc else "inverse")
        b.metric("Imputed interest", f"{imputed:,.0f} BDT", f"{coc:.1f}% × capital")
        c.metric("Residual Income", f"{ri:,.0f} BDT",
                 "value created" if ri >= 0 else "value destroyed",
                 delta_color="normal" if ri >= 0 else "inverse")

        st.caption(f"**DuPont:** ROI = margin {margin:.1f}% × asset turnover {turnover:.2f} = {margin*turnover/100:.1f}%")

        # DuPont breakdown chart
        fig = go.Figure(go.Bar(
            x=["Profit margin (%)", "Asset turnover (×)", "ROI (%)"],
            y=[margin, turnover, roi],
            marker_color=["#8e44ad", "#16a085", "#2e86de"],
            text=[f"{margin:.1f}%", f"{turnover:.2f}×", f"{roi:.1f}%"],
            textposition="outside",
        ))
        fig.update_layout(height=280, margin=dict(t=30, b=10), plot_bgcolor="white",
                          title="DuPont decomposition")
        st.plotly_chart(fig, use_container_width=True)

    if ri >= 0 and roi >= coc:
        st.success(
            f"**Value-creating division.** ROI ({roi:.1f}%) beats the cost of capital ({coc:.1f}%) and "
            f"RI is positive ({ri:,.0f} BDT) — the division earns more than the required return on its "
            f"capital. Both measures agree.",
            icon="✅",
        )
    else:
        st.warning(
            f"**Below the required return.** ROI ({roi:.1f}%) is under the cost of capital ({coc:.1f}%) and "
            f"RI is negative ({ri:,.0f} BDT) — the division is not covering the cost of the capital tied "
            f"up in it. Investigate margin, asset turnover, or the capital base.",
            icon="⚠️",
        )

# ==================================================================
# TAB 2 — THE CONFLICT
# ==================================================================
with tab_conflict:
    st.caption("See how ROI and RI can disagree on the SAME new project — the classic dysfunctional-decision trap.")

    xl, xr = st.columns([1, 1.4])
    with xl:
        st.markdown("#### 🎛️ Existing division")
        ex_profit  = st.number_input("Existing profit (BDT)", 0, 1_000_000_000, 900_000, step=10_000, key="cf_ep")
        ex_capital = st.number_input("Existing capital (BDT)", 1, 10_000_000_000, 5_000_000, step=100_000, key="cf_ec")
        coc2       = st.slider("Cost of capital (%)", 0.0, 30.0, 12.0, step=0.5, key="cf_coc")

        st.markdown("#### 🎛️ New project under consideration")
        proj_profit  = st.number_input("New project profit (BDT)", 0, 1_000_000_000, 140_000, step=5_000, key="cf_pp")
        proj_capital = st.number_input("New project capital (BDT)", 1, 10_000_000_000, 1_000_000, step=50_000, key="cf_pc")

    # Existing metrics
    ex_roi = ex_profit / ex_capital * 100
    ex_ri = ex_profit - ex_capital * coc2 / 100

    # Project standalone
    proj_roi = proj_profit / proj_capital * 100
    proj_ri = proj_profit - proj_capital * coc2 / 100

    # Combined (if accepted)
    new_profit = ex_profit + proj_profit
    new_capital = ex_capital + proj_capital
    new_roi = new_profit / new_capital * 100
    new_ri = new_profit - new_capital * coc2 / 100

    with xr:
        st.markdown("#### 📊 Decision table")
        tbl = pd.DataFrame({
            "": ["ROI (%)", "Residual Income (BDT)"],
            "Existing": [f"{ex_roi:.1f}%", f"{ex_ri:,.0f}"],
            "Project alone": [f"{proj_roi:.1f}%", f"{proj_ri:,.0f}"],
            "If accepted (combined)": [f"{new_roi:.1f}%", f"{new_ri:,.0f}"],
        })
        st.dataframe(tbl, use_container_width=True, hide_index=True)

        # ROI decision
        roi_decision = "ACCEPT" if new_roi >= ex_roi else "REJECT"
        ri_decision = "ACCEPT" if proj_ri >= 0 else "REJECT"
        company_best = "ACCEPT" if proj_roi >= coc2 else "REJECT"

        d1, d2, d3 = st.columns(3)
        d1.metric("Manager on ROI", roi_decision,
                  "protects avg ROI" if roi_decision == "REJECT" else "raises avg ROI",
                  delta_color="inverse" if roi_decision == "REJECT" else "normal")
        d2.metric("Manager on RI", ri_decision, "value-based",
                  delta_color="normal" if ri_decision == "ACCEPT" else "inverse")
        d3.metric("Company's interest", company_best, f"proj ROI {proj_roi:.1f}% vs CoC {coc2:.1f}%",
                  delta_color="normal" if company_best == "ACCEPT" else "inverse")

    # Diagnosis
    if roi_decision != company_best and ri_decision == company_best:
        st.error(
            f"**Dysfunctional decision exposed.** The project earns **{proj_roi:.1f}%** — above the "
            f"cost of capital ({coc2:.1f}%), so the company **should accept** it. But because "
            f"{proj_roi:.1f}% is **below the division's existing ROI ({ex_roi:.1f}%)**, accepting it "
            f"**drags the average ROI down** ({ex_roi:.1f}% → {new_roi:.1f}%). A manager rewarded on ROI "
            f"would **reject** a good project. **RI gets it right** — the project's RI is "
            f"**{proj_ri:,.0f} BDT (positive)**, so an RI-rewarded manager accepts, aligning with the "
            f"company. *This is the core argument for RI over ROI.*",
            icon="⚔️",
        )
    elif roi_decision == company_best == ri_decision:
        st.success(
            f"**All three agree ({company_best}).** Here ROI and RI happen to align. Try lowering the "
            f"project's profit so its ROI falls **between** the cost of capital and the existing ROI to "
            f"trigger the classic conflict.",
            icon="✅",
        )
    else:
        st.info(
            "Adjust the project profit/capital so its standalone ROI sits **between** the cost of "
            "capital and the existing division ROI — that gap is where ROI and RI disagree.",
            icon="🎛️",
        )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — choosing and reading the measures</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- ⚖️ **ROI is a ratio; RI is an absolute.** ROI compares divisions of different sizes easily,
  but can be gamed by shrinking the asset base. RI rewards **total value added** above the
  capital charge and drives **goal-congruent** decisions.
- 🎯 **The conflict is the exam favourite — and a real one.** Any project earning **above the
  cost of capital but below the division's current ROI** will lift RI yet dilute ROI. Reward
  the wrong metric and managers reject value-adding growth.
- 🧮 **Use the DuPont split to diagnose ROI.** Break ROI into **margin × asset turnover** to see
  whether performance is a pricing/cost story or an asset-utilisation story.
- 🧭 **Watch the definitions.** Be consistent about *controllable* profit and capital, and how
  assets are valued (net book value inflates ROI over time as assets depreciate).
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
        - [ ] **ROI = Profit ÷ Capital employed**; decompose as **margin × asset turnover**.
        - [ ] **RI = Profit − (Capital × cost of capital)**.
        - [ ] Accept any project with **positive RI** / ROI above the **cost of capital**.
        - [ ] ROI can cause managers to **reject good projects** that dilute their average.
        - [ ] Be consistent on **controllable profit** and **asset valuation**.
        """
    )
with a2:
    with st.expander("📘 Key formulas in this module"):
        st.markdown(
            """
            - **ROI** = Controllable profit ÷ Capital employed × 100
            - **DuPont** = (Profit ÷ Sales) × (Sales ÷ Capital)
            - **RI** = Controllable profit − (Capital employed × Cost of capital %)
            - **Imputed interest charge** = Capital employed × Cost of capital %
            """
        )
    with st.expander("🧭 ROI vs. RI — quick compare"):
        st.markdown(
            """
            | | **ROI** | **RI** |
            |---|---|---|
            | Form | Ratio (%) | Absolute (BDT) |
            | Compares sizes | Easily | Poorly |
            | Goal congruence | Can distort | Strong |
            | Decision rule | ROI > CoC | RI > 0 |
            """
        )

# Downloadable summary
template = pd.DataFrame({
    "Metric": ["Controllable profit", "Capital employed", "Cost of capital (%)",
               "ROI (%)", "Imputed interest", "Residual income",
               "Profit margin (%)", "Asset turnover (×)"],
    "Value": [profit, capital, coc, round(roi, 1), round(imputed, 0),
              round(ri, 0), round(margin, 1), round(turnover, 2)],
})
st.download_button(
    "⬇️ Download the ROI & RI summary (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="roi_residual_income.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 3.5 · Advanced Variances", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 4.2 · Economic Value Added (EVA) ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 4.1")
