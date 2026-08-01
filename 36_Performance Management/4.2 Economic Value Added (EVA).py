"""
Performance Management — Applied Learning Series
Module 4.2 · Economic Value Added (EVA)
------------------------------------------------------------
EVA refines Residual Income into a shareholder-value measure:
  EVA = NOPAT - (Invested capital x WACC)
where NOPAT and capital are ADJUSTED to remove accounting distortions.
Includes a WACC builder and the standard EVA adjustments made explicit.

Run with:  streamlit run 4.2_Economic_Value_Added.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="4.2 · Economic Value Added (EVA)",
    page_icon="💎",
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
st.markdown('<p class="big-title">4.2 · Economic Value Added (EVA)</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: measure true economic profit with <b>EVA = NOPAT − (Invested capital '
    '× WACC)</b>, build up the <b>WACC</b>, and apply the standard <b>accounting adjustments</b> that '
    'separate EVA from ordinary Residual Income.</p>',
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
**Economic Value Added (EVA®)** is a refined version of Residual Income developed by Stern
Stewart. It measures the value created **above the cost of *all* the capital** — debt and
equity — after correcting the accounting numbers to better reflect economic reality.

**The core formula:**

- **EVA = NOPAT − (Invested capital × WACC)**

where:

- **NOPAT** = Net Operating Profit After Tax — operating profit, taxed, and **adjusted**.
- **WACC** = Weighted Average Cost of Capital — the blended cost of debt and equity.
- **Invested capital** = the adjusted economic capital tied up in the business.

**Why adjust? (EVA vs. RI)** RI uses accounting profit as reported. EVA argues accounting
rules understate economic performance, so it makes adjustments such as:

- **Add back non-cash / value-building spend** treated as expenses but really investments —
  e.g. **R&D, marketing, training** — and capitalise/amortise them.
- **Add back accounting provisions** (e.g. doubtful debts, deferred tax movements) that
  don't reflect cash economics.
- **Use replacement/economic values** rather than historic net book value where possible.
- **Interest** is excluded from NOPAT because its cost is captured in the WACC charge.

**WACC:**

- **WACC = (E/V × Ke) + (D/V × Kd × (1 − tax))**

**Decision rule:** **positive EVA** = the business earned more than the cost of its capital
and created shareholder value; **negative EVA** = value destroyed.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "EVA links divisional performance directly to **shareholder value creation**. By capitalising "
        "value-building spend like R&D and marketing, it stops managers from boosting short-term "
        "profit by slashing long-term investment — exactly the short-termism a well-designed metric "
        "should prevent.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — two tabs
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model</p>', unsafe_allow_html=True)

tab_eva, tab_wacc = st.tabs(["💎 EVA Builder", "⚖️ WACC Calculator"])

# ==================================================================
# TAB 2 first computed values needed? We'll compute WACC in its tab and
# allow EVA tab to use its own WACC input for independence.
# ==================================================================

# ------------------------- WACC TAB -------------------------------
with tab_wacc:
    st.caption("Build the Weighted Average Cost of Capital from the debt/equity mix and their costs.")

    wl, wr = st.columns([1, 1.4])
    with wl:
        st.markdown("#### 🎛️ Inputs")
        equity = st.number_input("Market value of equity, E (BDT)", 0, 100_000_000_000,
                                 6_000_000, step=100_000, key="w_e")
        debt   = st.number_input("Market value of debt, D (BDT)", 0, 100_000_000_000,
                                 4_000_000, step=100_000, key="w_d")
        ke     = st.slider("Cost of equity, Ke (%)", 0.0, 40.0, 16.0, step=0.5, key="w_ke")
        kd     = st.slider("Cost of debt, Kd pre-tax (%)", 0.0, 30.0, 10.0, step=0.5, key="w_kd")
        tax    = st.slider("Tax rate (%)", 0.0, 50.0, 25.0, step=1.0, key="w_tax")

    V = equity + debt
    we = equity / V if V else 0
    wd = debt / V if V else 0
    kd_at = kd * (1 - tax / 100)
    wacc = we * ke + wd * kd_at

    with wr:
        st.markdown("#### 📊 WACC Result")
        a, b, c = st.columns(3)
        a.metric("Equity weight", f"{we*100:.1f}%", f"{equity:,.0f} BDT")
        b.metric("Debt weight", f"{wd*100:.1f}%", f"{debt:,.0f} BDT")
        c.metric("WACC", f"{wacc:.2f}%", f"after-tax Kd {kd_at:.2f}%")

        fig = go.Figure(go.Bar(
            x=["Ke contribution", "Kd (after-tax) contribution", "WACC"],
            y=[we*ke, wd*kd_at, wacc],
            marker_color=["#8e44ad", "#16a085", "#2e86de"],
            text=[f"{we*ke:.2f}%", f"{wd*kd_at:.2f}%", f"{wacc:.2f}%"],
            textposition="outside",
        ))
        fig.update_layout(height=300, margin=dict(t=30, b=10), plot_bgcolor="white",
                          title="WACC build-up", yaxis_title="%")
        st.plotly_chart(fig, use_container_width=True)

    st.caption(f"**WACC = (E/V × Ke) + (D/V × Kd × (1−t))** = "
               f"({we:.2f} × {ke:.1f}%) + ({wd:.2f} × {kd:.1f}% × {1-tax/100:.2f}) = **{wacc:.2f}%**")
    st.info("Use this WACC figure in the **EVA Builder** tab as the capital charge rate.", icon="↩️")

# ------------------------- EVA TAB --------------------------------
with tab_eva:
    st.caption("Walk from accounting operating profit to NOPAT, then charge the capital to arrive at EVA.")

    el, er = st.columns([1, 1.5])
    with el:
        st.markdown("#### 🎛️ Profit inputs")
        op_profit = st.number_input("Operating profit (PBIT) (BDT)", -1_000_000_000, 1_000_000_000,
                                    1_200_000, step=10_000, key="e_op")
        tax_e     = st.slider("Tax rate (%)", 0.0, 50.0, 25.0, step=1.0, key="e_tax")

        st.markdown("#### 🎛️ EVA adjustments (add back to NOPAT)")
        rnd    = st.number_input("R&D expensed this year (BDT)", 0, 1_000_000_000, 120_000, step=10_000, key="e_rnd")
        mktg   = st.number_input("Non-routine marketing/brand build (BDT)", 0, 1_000_000_000, 80_000, step=10_000, key="e_mkt")
        provs  = st.number_input("Non-cash provisions increase (BDT)", 0, 1_000_000_000, 30_000, step=5_000, key="e_prov")

        st.markdown("#### 🎛️ Capital & charge")
        capital = st.number_input("Invested capital (adjusted) (BDT)", 1, 100_000_000_000,
                                  8_000_000, step=100_000, key="e_cap")
        wacc_in = st.slider("WACC (%) — from the other tab", 0.0, 40.0, 13.60, step=0.05, key="e_wacc")

    # NOPAT build-up
    nopat_base = op_profit * (1 - tax_e / 100)
    adjustments = rnd + mktg + provs
    nopat = nopat_base + adjustments

    capital_charge = capital * wacc_in / 100
    eva = nopat - capital_charge

    with er:
        st.markdown("#### 📊 EVA Result")
        a, b, c = st.columns(3)
        a.metric("NOPAT", f"{nopat:,.0f} BDT", f"incl. {adjustments:,.0f} adj.")
        b.metric("Capital charge", f"{capital_charge:,.0f} BDT", f"{wacc_in:.2f}% × capital")
        c.metric("EVA", f"{eva:,.0f} BDT",
                 "value created" if eva >= 0 else "value destroyed",
                 delta_color="normal" if eva >= 0 else "inverse")

        # NOPAT build-up table
        build = pd.DataFrame({
            "NOPAT build-up": ["Operating profit (PBIT)", f"Less tax @ {tax_e:.0f}%",
                               "= After-tax operating profit",
                               "Add back: R&D", "Add back: Marketing/brand",
                               "Add back: Non-cash provisions", "= NOPAT (adjusted)"],
            "BDT": [op_profit, -(op_profit * tax_e / 100), nopat_base,
                    rnd, mktg, provs, nopat],
        })
        st.dataframe(build.style.format({"BDT": "{:,.0f}"}),
                     use_container_width=True, hide_index=True)

    # EVA bridge
    bridge = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "relative", "total"],
        x=["After-tax profit", "EVA adjustments", "Capital charge", "EVA"],
        y=[nopat_base, adjustments, -capital_charge, eva],
        text=[f"{nopat_base:,.0f}", f"{adjustments:+,.0f}", f"{-capital_charge:+,.0f}", f"{eva:,.0f}"],
        textposition="outside",
        connector={"line": {"color": "#b0b7bf"}},
        increasing={"marker": {"color": "#1e8449"}},
        decreasing={"marker": {"color": "#e67e22"}},
        totals={"marker": {"color": "#2e86de"}},
    ))
    bridge.update_layout(height=340, margin=dict(t=40, b=10), yaxis_title="BDT",
                         title="After-tax profit → EVA", plot_bgcolor="white")
    st.plotly_chart(bridge, use_container_width=True)

    if eva >= 0:
        st.success(
            f"**Positive EVA of {eva:,.0f} BDT — value created.** NOPAT ({nopat:,.0f}) exceeds the "
            f"capital charge ({capital_charge:,.0f}), so the business earned more than the cost of all "
            f"its capital. Note how capitalising R&D and marketing ({adjustments:,.0f}) rewards "
            f"long-term investment rather than penalising it.",
            icon="✅",
        )
    else:
        st.warning(
            f"**Negative EVA of {eva:,.0f} BDT — value destroyed.** The capital charge "
            f"({capital_charge:,.0f}) exceeds NOPAT ({nopat:,.0f}). The business is not covering the "
            f"cost of its capital — improve NOPAT, release capital, or lower the WACC.",
            icon="⚠️",
        )

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation — EVA vs. RI, and what it drives</p>',
            unsafe_allow_html=True)

st.markdown(
    """
- 💎 **EVA is RI, refined.** Both charge for capital, but EVA replaces accounting profit with
  **adjusted NOPAT** and the simple cost of capital with **WACC** — a truer economic picture.
- 🌱 **It protects long-term investment.** By capitalising **R&D, marketing and training**, EVA
  stops managers boosting this year's profit by cutting the very spend that builds future value.
- 🏦 **It charges for *all* capital.** Because interest is captured in WACC, NOPAT excludes it —
  avoiding double-counting the cost of debt.
- ⚖️ **Judgement is required.** The adjustments are subjective and can be manipulated; keep them
  **consistent, documented, and independently reviewed**, just like revised standards in 3.5.
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
        - [ ] **EVA = NOPAT − (Invested capital × WACC)**.
        - [ ] Build **NOPAT** from PBIT: tax it, then **add back** value-building spend.
        - [ ] **Capitalise R&D, marketing, training**; exclude interest (it's in WACC).
        - [ ] **WACC = (E/V × Ke) + (D/V × Kd × (1−t))**.
        - [ ] **Positive EVA = value created**; keep adjustments consistent and documented.
        """
    )
with a2:
    with st.expander("📘 Key formulas in this module"):
        st.markdown(
            """
            - **EVA** = NOPAT − (Invested capital × WACC)
            - **NOPAT** = PBIT × (1 − tax) + value-building add-backs
            - **WACC** = (E/V × Ke) + (D/V × Kd × (1 − t))
            - **Capital charge** = Invested capital × WACC
            """
        )
    with st.expander("🧭 EVA vs. RI — quick compare"):
        st.markdown(
            """
            | | **RI** | **EVA** |
            |---|---|---|
            | Profit base | Accounting profit | Adjusted **NOPAT** |
            | Capital charge | Cost of capital | **WACC** |
            | Adjustments | None | R&D, marketing, provisions… |
            | Focus | Divisional control | **Shareholder value** |
            """
        )

# Downloadable summary
template = pd.DataFrame({
    "Metric": ["Operating profit (PBIT)", "Tax rate (%)", "After-tax operating profit",
               "EVA adjustments (add-backs)", "NOPAT", "Invested capital", "WACC (%)",
               "Capital charge", "EVA"],
    "Value": [op_profit, tax_e, round(nopat_base, 0), adjustments, round(nopat, 0),
              capital, wacc_in, round(capital_charge, 0), round(eva, 0)],
})
st.download_button(
    "⬇️ Download the EVA summary (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="economic_value_added.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 4.1 · ROI & Residual Income", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 4.3 · Ratio Analysis for Performance ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 4.2")
