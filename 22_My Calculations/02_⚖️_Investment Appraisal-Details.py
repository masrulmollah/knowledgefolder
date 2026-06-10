"""
Investment Appraisal Web App — Streamlit
Covers: NPV, IRR, MIRR, Payback, Discounted Payback, PI, ARR, Sensitivity Analysis, Monte Carlo
Run with:  streamlit run investment_appraisal.py
"""

import streamlit as st
import numpy as np
import numpy_financial as npf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# NOTE: set_page_config() is intentionally omitted here.
# This file is a sub-page inside a multi-page Streamlit app.
# set_page_config() must only be called once, in your main
# homepage file (e.g. 1_🤓_Homepage.py).
# If you want wide layout for this page, set it there:
#   st.set_page_config(layout="wide")
# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    .main-title  { font-size:2.4rem; font-weight:800; color:#1a1a2e; text-align:center; margin-bottom:4px; }
    .sub-title   { font-size:1.05rem; color:#555; text-align:center; margin-bottom:20px; }

    /* Signal badges */
    .badge-accept  { background:#d4edda; color:#155724; border:1px solid #c3e6cb;
                     border-radius:8px; padding:10px 16px; font-weight:700; font-size:1rem; }
    .badge-reject  { background:#f8d7da; color:#721c24; border:1px solid #f5c6cb;
                     border-radius:8px; padding:10px 16px; font-weight:700; font-size:1rem; }
    .badge-caution { background:#fff3cd; color:#856404; border:1px solid #ffc107;
                     border-radius:8px; padding:10px 16px; font-weight:700; font-size:1rem; }

    /* Metric cards */
    .metric-card { background:#f8f9fa; border-radius:10px; padding:16px 20px;
                   border-left:5px solid #0d6efd; margin-bottom:10px; }
    .metric-card.green  { border-left-color:#198754; }
    .metric-card.red    { border-left-color:#dc3545; }
    .metric-card.amber  { border-left-color:#ffc107; }
    .metric-card.purple { border-left-color:#6f42c1; }

    .verdict-box { border-radius:12px; padding:18px 24px; font-size:1.1rem;
                   font-weight:700; margin-top:8px; }
    .verdict-accept { background:#d4edda; color:#155724; border:2px solid #28a745; }
    .verdict-reject { background:#f8d7da; color:#721c24; border:2px solid #dc3545; }
    .verdict-caution{ background:#fff3cd; color:#856404; border:2px solid #ffc107; }

    .section-header { font-size:1.3rem; font-weight:700; color:#1a1a2e;
                      border-bottom:3px solid #0d6efd; padding-bottom:6px; margin-top:24px; }
    .info-box  { background:#e7f3ff; border-radius:8px; padding:12px 16px;
                 color:#0d47a1; font-size:0.9rem; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def signal(condition_accept, condition_reject=None):
    """Return colored badge HTML."""
    if condition_accept:
        return '<span class="badge-accept">✅ ACCEPT</span>'
    elif condition_reject is None or condition_reject:
        return '<span class="badge-reject">❌ REJECT</span>'
    else:
        return '<span class="badge-caution">⚠️ BORDERLINE</span>'

def verdict_box(accept: bool, text: str):
    cls = "verdict-accept" if accept else "verdict-reject"
    icon = "✅" if accept else "❌"
    return f'<div class="verdict-box {cls}">{icon} {text}</div>'

def fmt(val, prefix="", suffix="", decimals=2):
    return f"{prefix}{val:,.{decimals}f}{suffix}"

def compute_npv(rate, cashflows):
    return npf.npv(rate, cashflows)

def compute_irr(cashflows):
    try:
        return npf.irr(cashflows)
    except Exception:
        return None

def compute_mirr(cashflows, finance_rate, reinvest_rate):
    try:
        return npf.mirr(cashflows, finance_rate, reinvest_rate)
    except Exception:
        return None

def payback_period(cashflows):
    """Returns (years, months) or None."""
    cumulative = 0
    for i, cf in enumerate(cashflows):
        cumulative += cf
        if cumulative >= 0:
            if i == 0:
                return 0, 0
            prev = cumulative - cf
            frac = -prev / cf
            full_years = i - 1
            months = round(frac * 12)
            return full_years, months
    return None, None

def discounted_payback(cashflows, rate):
    pv_cfs = [cf / (1 + rate) ** i for i, cf in enumerate(cashflows)]
    cumulative = 0
    for i, pv in enumerate(pv_cfs):
        cumulative += pv
        if cumulative >= 0:
            if i == 0:
                return 0, 0
            prev = cumulative - pv
            frac = -prev / pv
            full_years = i - 1
            months = round(frac * 12)
            return full_years, months
    return None, None

def profitability_index(npv, initial_investment):
    return 1 + npv / abs(initial_investment)

def arr(avg_annual_profit, initial_investment):
    return avg_annual_profit / abs(initial_investment) * 100

def sensitivity_npv(base_cashflows, rate, vary_param, variation_pct):
    """Vary a single parameter by ±variation_pct and return NPV."""
    results = []
    for pct in variation_pct:
        cfs = base_cashflows.copy()
        if vary_param == "Discount Rate":
            new_rate = rate * (1 + pct / 100)
            results.append(compute_npv(new_rate, cfs))
        elif vary_param == "Initial Investment":
            cfs[0] = cfs[0] * (1 + pct / 100)
            results.append(compute_npv(rate, cfs))
        elif vary_param == "Annual Cash Inflows":
            cfs[1:] = [c * (1 + pct / 100) for c in cfs[1:]]
            results.append(compute_npv(rate, cfs))
    return results

def monte_carlo_npv(initial_inv, mean_cf, std_cf, rate, years, n=5000):
    npvs = []
    for _ in range(n):
        cfs = [-abs(initial_inv)] + list(np.random.normal(mean_cf, std_cf, years))
        npvs.append(compute_npv(rate, cfs))
    return np.array(npvs)

# ─────────────────────────────────────────────
# SIDEBAR — INPUTS
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Project Inputs")
    st.markdown("---")

    project_name = st.text_input("📌 Project Name", value="Project Alpha")

    st.markdown("### 💰 Investment & Timing")
    initial_investment = st.number_input(
        "Initial Investment ($)", min_value=1_000, max_value=100_000_000,
        value=500_000, step=10_000, format="%d"
    )
    project_life = st.slider("Project Life (Years)", 2, 30, 10)

    st.markdown("### 📈 Cash Flow Inputs")
    cf_mode = st.radio("Cash Flow Mode", ["Uniform Annual CFs", "Custom Year-by-Year"])

    if cf_mode == "Uniform Annual CFs":
        annual_cf = st.number_input(
            "Annual Cash Inflow ($)", min_value=0, max_value=100_000_000,
            value=120_000, step=5_000, format="%d"
        )
        cf_growth = st.slider("Annual CF Growth Rate (%)", -10.0, 20.0, 0.0, 0.5)
        annual_cashflows = [annual_cf * ((1 + cf_growth / 100) ** i) for i in range(project_life)]
    else:
        st.markdown("Enter cash inflow for each year:")
        annual_cashflows = []
        cols_per_row = 2
        for i in range(project_life):
            val = st.number_input(f"Year {i+1} ($)", min_value=-10_000_000, max_value=100_000_000,
                                  value=120_000, step=5_000, key=f"cf_{i}", format="%d")
            annual_cashflows.append(val)

    salvage_value = st.number_input(
        "Salvage / Terminal Value ($)", min_value=0, max_value=50_000_000,
        value=50_000, step=5_000, format="%d"
    )

    st.markdown("### 🎯 Rate Inputs")
    discount_rate = st.slider("Required Rate of Return / WACC (%)", 1.0, 40.0, 10.0, 0.5)
    finance_rate  = st.slider("Finance Rate for MIRR (%)", 1.0, 30.0, 8.0, 0.5)
    reinvest_rate = st.slider("Reinvestment Rate for MIRR (%)", 1.0, 30.0, 10.0, 0.5)
    target_pb     = st.slider("Target Payback Period (Years)", 1, 20, 5)

    st.markdown("### 📊 ARR")
    annual_depreciation = st.number_input(
        "Annual Depreciation ($)", min_value=0, max_value=10_000_000,
        value=int(initial_investment / project_life), step=5_000, format="%d"
    )

    st.markdown("### 🎲 Monte Carlo")
    mc_simulations = st.select_slider("Simulations", [1000, 2000, 5000, 10000], value=5000)
    cf_std_pct = st.slider("CF Std Dev (% of Mean CF)", 5, 60, 20)

    st.markdown("---")
    run_analysis = st.button("🚀 Run Full Analysis", type="primary", use_container_width=True)

# ─────────────────────────────────────────────
# MAIN TITLE
# ─────────────────────────────────────────────
st.markdown('<div class="main-title">📊 Investment Appraisal Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Comprehensive Capital Budgeting & Project Evaluation Dashboard</div>', unsafe_allow_html=True)

if not run_analysis:
    st.info("👈 Configure your project inputs in the sidebar, then click **Run Full Analysis**.")
    st.stop()

# ─────────────────────────────────────────────
# BUILD CASHFLOW ARRAY
# ─────────────────────────────────────────────
rate = discount_rate / 100
fin_rate = finance_rate / 100
reinv_rate = reinvest_rate / 100

# Add salvage to final year
cashflows_ops = annual_cashflows.copy()
cashflows_ops[-1] += salvage_value
all_cashflows = [-initial_investment] + cashflows_ops

# ─────────────────────────────────────────────
# CALCULATIONS
# ─────────────────────────────────────────────
npv_val      = compute_npv(rate, all_cashflows)
irr_val      = compute_irr(all_cashflows)
mirr_val     = compute_mirr(all_cashflows, fin_rate, reinv_rate)
pi_val       = profitability_index(npv_val, initial_investment)
pb_y, pb_m   = payback_period(all_cashflows)
dpb_y, dpb_m = discounted_payback(all_cashflows, rate)

avg_annual_profit = np.mean([cf - annual_depreciation for cf in annual_cashflows])
arr_val      = arr(avg_annual_profit, initial_investment)

# Cumulative cashflows
cum_cfs    = np.cumsum(all_cashflows)
disc_cfs   = [cf / (1 + rate) ** i for i, cf in enumerate(all_cashflows)]
cum_disc   = np.cumsum(disc_cfs)

# ─────────────────────────────────────────────
# SCORECARD — TOP ROW
# ─────────────────────────────────────────────
st.markdown(f"## 📋 Appraisal Results — *{project_name}*")

k1, k2, k3, k4, k5 = st.columns(5)

def kpi(col, label, value, color="blue"):
    color_map = {"green": "#198754", "red": "#dc3545", "amber": "#ffc107",
                 "blue": "#0d6efd", "purple": "#6f42c1"}
    c = color_map.get(color, "#0d6efd")
    col.markdown(
        f"""<div style="background:#f8f9fa;border-radius:10px;padding:14px 12px;
        border-top:5px solid {c};text-align:center;">
        <div style="font-size:0.78rem;color:#666;font-weight:600;letter-spacing:.5px">{label}</div>
        <div style="font-size:1.45rem;font-weight:800;color:{c};margin-top:4px">{value}</div>
        </div>""", unsafe_allow_html=True
    )

npv_color  = "green" if npv_val > 0 else "red"
irr_color  = "green" if irr_val and irr_val > rate else "red"
pi_color   = "green" if pi_val >= 1 else "red"
pb_color   = "green" if pb_y is not None and (pb_y + (pb_m or 0) / 12) <= target_pb else "red"
arr_color  = "green" if arr_val >= discount_rate else "red"

kpi(k1, "NPV", fmt(npv_val, "$"), npv_color)
kpi(k2, "IRR", f"{irr_val*100:.2f}%" if irr_val else "N/A", irr_color)
kpi(k3, "PI",  fmt(pi_val, decimals=3), pi_color)
kpi(k4, "Payback", f"{pb_y}y {pb_m}m" if pb_y is not None else "Never", pb_color)
kpi(k5, "ARR",  fmt(arr_val, suffix="%"), arr_color)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tabs = st.tabs([
    "📐 NPV & DCF",
    "🔄 IRR & MIRR",
    "⏱️ Payback",
    "📊 PI & ARR",
    "🔍 Sensitivity",
    "🎲 Monte Carlo",
    "📋 Full Cash Flow Table",
    "🏆 Decision Summary"
])

# ══════════════════════════════════════════════
# TAB 1 — NPV & DCF
# ══════════════════════════════════════════════
with tabs[0]:
    st.markdown('<div class="section-header">Net Present Value (NPV) Analysis</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
        <div class="metric-card {'green' if npv_val > 0 else 'red'}">
            <strong>NPV = {fmt(npv_val, '$')}</strong><br>
            <small>Discount Rate: {discount_rate}% &nbsp;|&nbsp; Project Life: {project_life} years</small>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(signal(npv_val > 0), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="info-box">
        📌 <strong>What NPV tells you:</strong><br>
        NPV measures the value added to the firm in today's dollars.<br>
        • <strong>NPV &gt; 0</strong> → Project creates wealth; <strong>ACCEPT</strong><br>
        • <strong>NPV = 0</strong> → Project breaks even at the required rate<br>
        • <strong>NPV &lt; 0</strong> → Project destroys value; <strong>REJECT</strong><br><br>
        This project's NPV of <strong>{fmt(npv_val, '$')}</strong>
        {"adds value above the required return. ✅" if npv_val > 0 else "fails to cover the cost of capital. ❌"}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # NPV Profile chart (NPV vs discount rate)
        rates_range = np.linspace(0.001, 0.50, 100)
        npvs_range  = [compute_npv(r, all_cashflows) for r in rates_range]

        fig_npv = go.Figure()
        fig_npv.add_trace(go.Scatter(
            x=rates_range * 100, y=npvs_range,
            mode='lines', line=dict(color='#0d6efd', width=3), name="NPV Profile"
        ))
        fig_npv.add_hline(y=0, line_dash="dash", line_color="black", line_width=1.5)
        fig_npv.add_vline(x=discount_rate, line_dash="dot", line_color="#dc3545",
                          annotation_text=f"WACC {discount_rate}%", line_width=2)
        if irr_val:
            fig_npv.add_vline(x=irr_val * 100, line_dash="dot", line_color="#198754",
                              annotation_text=f"IRR {irr_val*100:.1f}%", line_width=2)
        fig_npv.add_scatter(x=[discount_rate], y=[npv_val],
                            mode='markers', marker=dict(size=12, color='#dc3545'),
                            name=f"NPV @ WACC = {fmt(npv_val, '$')}")
        fig_npv.update_layout(
            title="NPV Profile — Value vs Discount Rate",
            xaxis_title="Discount Rate (%)", yaxis_title="NPV ($)",
            height=380, template="plotly_white",
            legend=dict(orientation="h", y=-0.2)
        )
        st.plotly_chart(fig_npv, use_container_width=True)

    # DCF Waterfall
    st.markdown('<div class="section-header">Discounted Cash Flow Waterfall</div>', unsafe_allow_html=True)
    labels = [f"Year {i}" if i > 0 else "Year 0\n(Investment)" for i in range(len(all_cashflows))]
    colors = ["#dc3545" if v < 0 else "#198754" for v in disc_cfs]

    fig_wf = go.Figure(go.Bar(
        x=labels, y=disc_cfs,
        marker_color=colors,
        text=[fmt(v, "$", decimals=0) for v in disc_cfs],
        textposition="outside"
    ))
    fig_wf.add_scatter(x=labels, y=cum_disc, mode='lines+markers',
                       line=dict(color='#6f42c1', width=2.5),
                       marker=dict(size=8), name="Cumulative Discounted CF")
    fig_wf.add_hline(y=0, line_color="black", line_width=1)
    fig_wf.update_layout(
        title="Present Value of Each Year's Cash Flow",
        yaxis_title="PV ($)", height=420, template="plotly_white",
        showlegend=True
    )
    st.plotly_chart(fig_wf, use_container_width=True)

# ══════════════════════════════════════════════
# TAB 2 — IRR & MIRR
# ══════════════════════════════════════════════
with tabs[1]:
    st.markdown('<div class="section-header">Internal Rate of Return (IRR)</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        irr_pct  = irr_val * 100 if irr_val else None
        hurdle   = discount_rate
        spread   = (irr_pct - hurdle) if irr_pct else None

        st.markdown(f"""
        <div class="metric-card {'green' if irr_pct and irr_pct > hurdle else 'red'}">
            <strong>IRR = {f'{irr_pct:.2f}%' if irr_pct else 'Cannot be computed'}</strong><br>
            <small>Hurdle Rate: {hurdle}% &nbsp;|&nbsp;
            Spread: {f'{spread:+.2f}%' if spread else 'N/A'}</small>
        </div>
        """, unsafe_allow_html=True)

        if irr_pct:
            st.markdown(signal(irr_pct > hurdle), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="info-box">
        📌 <strong>What IRR tells you:</strong><br>
        IRR is the discount rate that makes NPV = 0.<br>
        • <strong>IRR &gt; Hurdle Rate</strong> → Project earns more than required; <strong>ACCEPT</strong><br>
        • <strong>IRR &lt; Hurdle Rate</strong> → Project under-performs; <strong>REJECT</strong><br><br>
        ⚠️ <em>Limitation:</em> IRR assumes reinvestment at the IRR rate itself, which may be unrealistic.
        Use MIRR for a more conservative estimate.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        mirr_pct = mirr_val * 100 if mirr_val else None
        st.markdown(f"""
        <div class="metric-card purple {'green' if mirr_pct and mirr_pct > hurdle else 'red'}">
            <strong>MIRR = {f'{mirr_pct:.2f}%' if mirr_pct else 'N/A'}</strong><br>
            <small>Finance Rate: {finance_rate}% &nbsp;|&nbsp; Reinvestment Rate: {reinvest_rate}%</small>
        </div>
        """, unsafe_allow_html=True)

        if mirr_pct:
            st.markdown(signal(mirr_pct > hurdle), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="info-box">
        📌 <strong>What MIRR tells you:</strong><br>
        MIRR corrects IRR's reinvestment assumption by using:<br>
        • A <strong>finance rate</strong> for negative flows (cost of capital)<br>
        • A <strong>reinvestment rate</strong> for positive flows (returns on reinvested cash)<br><br>
        MIRR is generally more conservative and realistic than IRR.<br>
        {"✅ MIRR > Hurdle Rate — project is still attractive." if mirr_pct and mirr_pct > hurdle else "❌ MIRR < Hurdle Rate — reconsider the project."}
        </div>
        """, unsafe_allow_html=True)

    # Comparison bar
    fig_irr = go.Figure()
    metrics = ["Hurdle Rate", "IRR", "MIRR"]
    values  = [hurdle, irr_pct or 0, mirr_pct or 0]
    colors_bar = ["#6c757d",
                  "#198754" if irr_pct and irr_pct > hurdle else "#dc3545",
                  "#0d6efd" if mirr_pct and mirr_pct > hurdle else "#dc3545"]
    fig_irr.add_trace(go.Bar(x=metrics, y=values, marker_color=colors_bar,
                             text=[f"{v:.2f}%" for v in values], textposition="outside"))
    fig_irr.update_layout(
        title="Rate Comparison: Hurdle vs IRR vs MIRR",
        yaxis_title="Rate (%)", height=380, template="plotly_white",
        showlegend=False
    )
    st.plotly_chart(fig_irr, use_container_width=True)

# ══════════════════════════════════════════════
# TAB 3 — PAYBACK PERIOD
# ══════════════════════════════════════════════
with tabs[2]:
    st.markdown('<div class="section-header">Payback Period & Discounted Payback Period</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        pb_val = pb_y + (pb_m or 0) / 12 if pb_y is not None else None
        pb_ok  = pb_val is not None and pb_val <= target_pb
        st.markdown(f"""
        <div class="metric-card {'green' if pb_ok else 'red'}">
            <strong>Simple Payback = {f'{pb_y}y {pb_m}m' if pb_y is not None else 'Never recovered'}</strong><br>
            <small>Target: ≤ {target_pb} years</small>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(signal(pb_ok, not pb_ok), unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
        📌 <strong>Payback Period:</strong> How long until cumulative cash inflows recover the initial outlay.<br>
        • Simple and widely used — but <em>ignores time value of money</em> and cash flows after payback.<br>
        • Good as a liquidity/risk measure alongside NPV.
        </div>""", unsafe_allow_html=True)

    with col2:
        dpb_val = dpb_y + (dpb_m or 0) / 12 if dpb_y is not None else None
        dpb_ok  = dpb_val is not None and dpb_val <= target_pb
        st.markdown(f"""
        <div class="metric-card {'green' if dpb_ok else 'red'}">
            <strong>Discounted Payback = {f'{dpb_y}y {dpb_m}m' if dpb_y is not None else 'Never recovered'}</strong><br>
            <small>Target: ≤ {target_pb} years</small>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(signal(dpb_ok, not dpb_ok), unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
        📌 <strong>Discounted Payback:</strong> Same as payback but using discounted (PV) cash flows.<br>
        • Always longer than simple payback. Accounts for TVM.<br>
        • If project never recovers in discounted terms, NPV is negative.
        </div>""", unsafe_allow_html=True)

    # Cumulative CF chart
    years_axis = list(range(len(all_cashflows)))
    fig_pb = go.Figure()
    fig_pb.add_trace(go.Scatter(
        x=years_axis, y=cum_cfs,
        mode='lines+markers', name='Cumulative CF (Undiscounted)',
        line=dict(color='#0d6efd', width=3), marker=dict(size=8)
    ))
    fig_pb.add_trace(go.Scatter(
        x=years_axis, y=cum_disc,
        mode='lines+markers', name='Cumulative CF (Discounted)',
        line=dict(color='#6f42c1', width=3, dash='dash'), marker=dict(size=8)
    ))
    fig_pb.add_hline(y=0, line_color="red", line_width=2, line_dash="solid",
                     annotation_text="Break-even line")

    # Shade zones
    fig_pb.add_vrect(x0=0, x1=target_pb, fillcolor="rgba(255,193,7,0.1)",
                     layer="below", line_width=0,
                     annotation_text=f"Target window ({target_pb}y)", annotation_position="top left")

    fig_pb.update_layout(
        title="Cumulative Cash Flow Over Project Life",
        xaxis_title="Year", yaxis_title="Cumulative CF ($)",
        height=420, template="plotly_white",
        legend=dict(orientation="h", y=-0.2)
    )
    st.plotly_chart(fig_pb, use_container_width=True)

# ══════════════════════════════════════════════
# TAB 4 — PI & ARR
# ══════════════════════════════════════════════
with tabs[3]:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-header">Profitability Index (PI)</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="metric-card {'green' if pi_val >= 1 else 'red'}">
            <strong>PI = {pi_val:.4f}</strong><br>
            <small>PI = 1 + NPV / |Initial Investment|</small>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(signal(pi_val >= 1), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="info-box">
        📌 <strong>Profitability Index:</strong> PV of future cash flows per dollar invested.<br>
        • <strong>PI &gt; 1.0</strong> → Generates more than $1 of PV per $1 invested → <strong>ACCEPT</strong><br>
        • <strong>PI &lt; 1.0</strong> → Destroys value → <strong>REJECT</strong><br>
        • Very useful for <strong>capital rationing</strong> — rank projects by PI when budget is limited.<br><br>
        This project generates <strong>{fmt(pi_val, decimals=4)}x</strong> in PV for every $1 invested.
        </div>
        """, unsafe_allow_html=True)

        # Gauge chart for PI
        fig_pi = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pi_val,
            title={'text': "Profitability Index"},
            gauge={
                'axis': {'range': [0, max(2.5, pi_val + 0.3)]},
                'bar': {'color': "#198754" if pi_val >= 1 else "#dc3545"},
                'steps': [
                    {'range': [0, 1], 'color': '#f8d7da'},
                    {'range': [1, 1.5], 'color': '#d4edda'},
                    {'range': [1.5, 3], 'color': '#a8d5b5'},
                ],
                'threshold': {'line': {'color': "black", 'width': 4}, 'value': 1}
            }
        ))
        fig_pi.update_layout(height=300)
        st.plotly_chart(fig_pi, use_container_width=True)

    with col2:
        st.markdown('<div class="section-header">Accounting Rate of Return (ARR)</div>',
                    unsafe_allow_html=True)
        st.markdown(f"""
        <div class="metric-card {'green' if arr_val >= discount_rate else 'red'}">
            <strong>ARR = {fmt(arr_val, suffix='%')}</strong><br>
            <small>Avg Annual Profit: {fmt(avg_annual_profit, '$')} &nbsp;|&nbsp;
            Target: ≥ {discount_rate}%</small>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(signal(arr_val >= discount_rate), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="info-box">
        📌 <strong>ARR (Accounting Rate of Return):</strong> Average accounting profit as % of investment.<br>
        • Based on <em>accounting profit</em> (after depreciation), NOT cash flows<br>
        • <strong>ARR &gt; Required Rate</strong> → <strong>ACCEPT</strong><br>
        • Does <em>not</em> account for time value of money<br>
        • Used mainly as a secondary check alongside NPV/IRR<br><br>
        Annual Depreciation used: <strong>{fmt(annual_depreciation, '$')}</strong>
        </div>
        """, unsafe_allow_html=True)

        annual_profits = [cf - annual_depreciation for cf in annual_cashflows]
        fig_arr = go.Figure()
        fig_arr.add_trace(go.Bar(
            x=[f"Yr {i+1}" for i in range(len(annual_profits))],
            y=annual_profits,
            marker_color=["#198754" if p > 0 else "#dc3545" for p in annual_profits],
            name="Annual Accounting Profit"
        ))
        fig_arr.add_hline(y=avg_annual_profit, line_dash="dash", line_color="#0d6efd",
                          annotation_text=f"Avg: {fmt(avg_annual_profit, '$')}")
        fig_arr.update_layout(title="Annual Accounting Profit (CF − Depreciation)",
                              height=300, template="plotly_white")
        st.plotly_chart(fig_arr, use_container_width=True)

# ══════════════════════════════════════════════
# TAB 5 — SENSITIVITY ANALYSIS
# ══════════════════════════════════════════════
with tabs[4]:
    st.markdown('<div class="section-header">Sensitivity Analysis (Tornado & Spider)</div>',
                unsafe_allow_html=True)

    variation_range = np.arange(-40, 45, 5)
    params = ["Discount Rate", "Initial Investment", "Annual Cash Inflows"]
    results_dict = {}
    for param in params:
        results_dict[param] = sensitivity_npv(all_cashflows, rate, param, variation_range)

    # Spider chart
    fig_sp = go.Figure()
    colors_sp = ["#0d6efd", "#dc3545", "#198754"]
    for (param, vals), col in zip(results_dict.items(), colors_sp):
        fig_sp.add_trace(go.Scatter(
            x=list(variation_range), y=vals,
            mode='lines+markers', name=param,
            line=dict(color=col, width=2.5)
        ))
    fig_sp.add_hline(y=0, line_dash="dash", line_color="black")
    fig_sp.add_vline(x=0, line_dash="dot", line_color="grey")
    fig_sp.update_layout(
        title="Spider Diagram — NPV Sensitivity to Input Changes",
        xaxis_title="Change in Parameter (%)",
        yaxis_title="Resulting NPV ($)",
        height=420, template="plotly_white",
        legend=dict(orientation="h", y=-0.2)
    )
    st.plotly_chart(fig_sp, use_container_width=True)

    # Tornado chart (impact at ±20%)
    st.markdown("#### Tornado Chart — Impact of ±20% Change on NPV")
    base_npv = npv_val
    tornado_data = []
    for param in params:
        idx_low  = list(variation_range).index(-20)
        idx_high = list(variation_range).index(20)
        low_npv  = results_dict[param][idx_low]
        high_npv = results_dict[param][idx_high]
        tornado_data.append({"Parameter": param, "NPV_Low": low_npv, "NPV_High": high_npv,
                             "Range": abs(high_npv - low_npv)})

    tornado_df = pd.DataFrame(tornado_data).sort_values("Range")
    fig_tor = go.Figure()
    for _, row in tornado_df.iterrows():
        fig_tor.add_trace(go.Bar(
            y=[row["Parameter"]], x=[row["NPV_High"] - base_npv],
            base=base_npv, orientation='h',
            marker_color="#198754", showlegend=False
        ))
        fig_tor.add_trace(go.Bar(
            y=[row["Parameter"]], x=[row["NPV_Low"] - base_npv],
            base=base_npv, orientation='h',
            marker_color="#dc3545", showlegend=False
        ))
    fig_tor.add_vline(x=base_npv, line_dash="solid", line_color="black", line_width=2,
                      annotation_text="Base NPV")
    fig_tor.update_layout(
        title="Tornado Diagram — Sensitivity at ±20% Change",
        barmode='overlay', height=360, template="plotly_white",
        xaxis_title="NPV ($)"
    )
    st.plotly_chart(fig_tor, use_container_width=True)

    st.markdown("""
    <div class="info-box">
    📌 <strong>Reading Sensitivity Analysis:</strong><br>
    • The <strong>Spider Diagram</strong> shows how NPV changes as each input varies ±40%.<br>
    • Steeper lines = more sensitive to that variable = higher risk.<br>
    • The <strong>Tornado Chart</strong> ranks variables by their impact — the widest bar is the biggest risk driver.<br>
    • Focus risk management on the factors at the top of the tornado.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 6 — MONTE CARLO
# ══════════════════════════════════════════════
with tabs[5]:
    st.markdown('<div class="section-header">Monte Carlo Simulation — Risk Analysis</div>',
                unsafe_allow_html=True)

    mean_cf  = np.mean(annual_cashflows)
    std_cf   = mean_cf * (cf_std_pct / 100)
    mc_npvs  = monte_carlo_npv(initial_investment, mean_cf, std_cf, rate, project_life, mc_simulations)

    prob_positive = (mc_npvs > 0).mean() * 100
    mc_mean  = mc_npvs.mean()
    mc_p5    = np.percentile(mc_npvs, 5)
    mc_p95   = np.percentile(mc_npvs, 95)

    col1, col2, col3, col4 = st.columns(4)
    def mc_kpi(col, label, val, color):
        col.markdown(f"""
        <div style="background:#f8f9fa;border-radius:10px;padding:12px;
        border-top:5px solid {color};text-align:center">
        <div style="font-size:0.75rem;color:#666;font-weight:600">{label}</div>
        <div style="font-size:1.3rem;font-weight:800;color:{color}">{val}</div>
        </div>""", unsafe_allow_html=True)

    mc_kpi(col1, "P(NPV > 0)", f"{prob_positive:.1f}%",
           "#198754" if prob_positive > 70 else "#ffc107" if prob_positive > 50 else "#dc3545")
    mc_kpi(col2, "Mean NPV", fmt(mc_mean, "$"), "#0d6efd")
    mc_kpi(col3, "P5 NPV (Worst 5%)", fmt(mc_p5, "$"), "#dc3545")
    mc_kpi(col4, "P95 NPV (Best 5%)", fmt(mc_p95, "$"), "#198754")

    st.markdown("<br>", unsafe_allow_html=True)

    fig_mc = go.Figure()
    fig_mc.add_trace(go.Histogram(
        x=mc_npvs, nbinsx=80,
        marker_color=np.where(mc_npvs > 0, '#198754', '#dc3545').tolist(),
        opacity=0.8, name="Simulated NPVs"
    ))
    # Actually plotly doesn't support per-bar colors in histogram easily; use a workaround
    fig_mc = go.Figure()
    pos_npvs = mc_npvs[mc_npvs >= 0]
    neg_npvs = mc_npvs[mc_npvs < 0]
    fig_mc.add_trace(go.Histogram(x=pos_npvs, nbinsx=50, name="NPV ≥ 0 (Positive)",
                                  marker_color="#198754", opacity=0.75))
    fig_mc.add_trace(go.Histogram(x=neg_npvs, nbinsx=30, name="NPV < 0 (Negative)",
                                  marker_color="#dc3545", opacity=0.75))
    fig_mc.add_vline(x=0,       line_dash="solid", line_color="black",  line_width=2)
    fig_mc.add_vline(x=mc_mean, line_dash="dash",  line_color="#0d6efd", line_width=2,
                     annotation_text=f"Mean: {fmt(mc_mean, '$')}")
    fig_mc.add_vline(x=mc_p5,   line_dash="dot",   line_color="#dc3545", line_width=1.5,
                     annotation_text=f"P5: {fmt(mc_p5, '$')}")
    fig_mc.add_vline(x=mc_p95,  line_dash="dot",   line_color="#198754", line_width=1.5,
                     annotation_text=f"P95: {fmt(mc_p95, '$')}")
    fig_mc.update_layout(
        title=f"Monte Carlo NPV Distribution ({mc_simulations:,} Simulations)",
        barmode='overlay', xaxis_title="NPV ($)", yaxis_title="Frequency",
        height=440, template="plotly_white",
        legend=dict(orientation="h", y=-0.2)
    )
    st.plotly_chart(fig_mc, use_container_width=True)

    mc_signal = ("#198754" if prob_positive > 70
                 else "#ffc107" if prob_positive > 50 else "#dc3545")
    mc_label  = ("High confidence — project likely creates value ✅" if prob_positive > 70
                 else "Moderate risk — significant chance of loss ⚠️" if prob_positive > 50
                 else "High risk — more likely to destroy value ❌")
    st.markdown(f"""
    <div style="background:#f8f9fa;border-radius:10px;padding:16px;border-left:6px solid {mc_signal}">
    <strong>Monte Carlo Verdict:</strong> Probability of positive NPV = <strong>{prob_positive:.1f}%</strong><br>
    {mc_label}<br><br>
    <em>CF Std Dev assumed: {cf_std_pct}% of mean annual CF (${std_cf:,.0f})</em>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 7 — FULL CASH FLOW TABLE
# ══════════════════════════════════════════════
with tabs[6]:
    st.markdown('<div class="section-header">Detailed Cash Flow & DCF Schedule</div>',
                unsafe_allow_html=True)

    pv_factors = [1 / (1 + rate) ** i for i in range(len(all_cashflows))]
    table_data = {
        "Year":            list(range(len(all_cashflows))),
        "Gross CF ($)":    [f"{v:,.0f}" for v in all_cashflows],
        "PV Factor":       [f"{f:.6f}" for f in pv_factors],
        "Discounted CF ($)": [f"{v:,.0f}" for v in disc_cfs],
        "Cum. CF ($)":     [f"{v:,.0f}" for v in cum_cfs],
        "Cum. Disc CF ($)":[f"{v:,.0f}" for v in cum_disc],
    }
    df_table = pd.DataFrame(table_data)

    def highlight_rows(row):
        cum = float(row["Cum. CF ($)"].replace(",", ""))
        cum_d = float(row["Cum. Disc CF ($)"].replace(",", ""))
        style = []
        for col in row.index:
            if col == "Cum. CF ($)":
                style.append("background-color: #d4edda; color:#155724" if cum >= 0
                              else "background-color: #f8d7da; color:#721c24")
            elif col == "Cum. Disc CF ($)":
                style.append("background-color: #d1ecf1; color:#0c5460" if cum_d >= 0
                              else "background-color: #fff3cd; color:#856404")
            else:
                style.append("")
        return style

    st.dataframe(df_table.style.apply(highlight_rows, axis=1), use_container_width=True, height=420)

    st.markdown("""
    <div class="info-box">
    🟢 Green = cumulative CF has turned positive (simple payback reached)<br>
    🔵 Blue = cumulative discounted CF turned positive (discounted payback reached)<br>
    🟡 Yellow = discounted CF still negative
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 8 — DECISION SUMMARY
# ══════════════════════════════════════════════
with tabs[7]:
    st.markdown('<div class="section-header">🏆 Investment Decision Summary</div>',
                unsafe_allow_html=True)

    # Collect verdicts
    verdicts = {
        "NPV":     {"val": fmt(npv_val, "$"),   "accept": npv_val > 0,
                    "rule": "NPV > 0"},
        "IRR":     {"val": f"{irr_val*100:.2f}%" if irr_val else "N/A",
                    "accept": bool(irr_val and irr_val > rate),
                    "rule": f"IRR > Hurdle ({discount_rate}%)"},
        "MIRR":    {"val": f"{mirr_val*100:.2f}%" if mirr_val else "N/A",
                    "accept": bool(mirr_val and mirr_val > rate),
                    "rule": f"MIRR > Hurdle ({discount_rate}%)"},
        "PI":      {"val": f"{pi_val:.4f}",      "accept": pi_val >= 1,
                    "rule": "PI ≥ 1.0"},
        "Payback": {"val": f"{pb_y}y {pb_m}m" if pb_y is not None else "Never",
                    "accept": pb_val is not None and pb_val <= target_pb,
                    "rule": f"Payback ≤ {target_pb}y"},
        "Disc. PB":{"val": f"{dpb_y}y {dpb_m}m" if dpb_y is not None else "Never",
                    "accept": dpb_val is not None and dpb_val <= target_pb,
                    "rule": f"Disc. Payback ≤ {target_pb}y"},
        "ARR":     {"val": f"{arr_val:.2f}%",    "accept": arr_val >= discount_rate,
                    "rule": f"ARR ≥ {discount_rate}%"},
        "Monte Carlo": {"val": f"P(NPV>0) = {prob_positive:.1f}%",
                        "accept": prob_positive >= 60,
                        "rule": "Probability ≥ 60%"},
    }

    accepts = sum(1 for v in verdicts.values() if v["accept"])
    rejects = len(verdicts) - accepts

    # Scorecard table
    col_hdr = st.columns([2, 2, 1, 2])
    col_hdr[0].markdown("**Technique**")
    col_hdr[1].markdown("**Result**")
    col_hdr[2].markdown("**Signal**")
    col_hdr[3].markdown("**Decision Rule**")
    st.markdown("---")

    for name, info in verdicts.items():
        c0, c1, c2, c3 = st.columns([2, 2, 1, 2])
        c0.markdown(f"**{name}**")
        c1.markdown(info["val"])
        badge = "✅ Accept" if info["accept"] else "❌ Reject"
        bg    = "#d4edda" if info["accept"] else "#f8d7da"
        fg    = "#155724" if info["accept"] else "#721c24"
        c2.markdown(
            f'<span style="background:{bg};color:{fg};border-radius:6px;'
            f'padding:4px 10px;font-weight:700;font-size:0.85rem">{badge}</span>',
            unsafe_allow_html=True
        )
        c3.markdown(f"<small>{info['rule']}</small>", unsafe_allow_html=True)

    st.markdown("---")

    # Overall verdict
    weight_score = accepts / len(verdicts)
    if weight_score >= 0.75:
        overall = "STRONG ACCEPT"
        ov_cls  = "verdict-accept"
        ov_icon = "✅✅"
        ov_comment = (f"{accepts}/{len(verdicts)} techniques signal ACCEPT. "
                      "The project demonstrates strong financial viability. "
                      "Recommend proceeding with investment.")
    elif weight_score >= 0.5:
        overall = "CONDITIONAL ACCEPT"
        ov_cls  = "verdict-caution"
        ov_icon = "⚠️"
        ov_comment = (f"{accepts}/{len(verdicts)} techniques signal ACCEPT. "
                      "The project has merit but some metrics raise concerns. "
                      "Review risk factors and sensitivity analysis before proceeding.")
    else:
        overall = "REJECT"
        ov_cls  = "verdict-reject"
        ov_icon = "❌"
        ov_comment = (f"Only {accepts}/{len(verdicts)} techniques signal ACCEPT. "
                      "The project does not meet the required financial thresholds. "
                      "Recommend rejecting or redesigning the project.")

    st.markdown(f"""
    <div class="verdict-box {ov_cls}">
    {ov_icon} Overall Decision: <strong>{overall}</strong><br>
    <span style="font-weight:400;font-size:0.95rem">{ov_comment}</span>
    </div>
    """, unsafe_allow_html=True)

    # Radar chart summary
    st.markdown("<br>", unsafe_allow_html=True)
    radar_labels = list(verdicts.keys())
    radar_scores = [1 if v["accept"] else 0 for v in verdicts.values()]
    radar_scores.append(radar_scores[0])
    radar_labels_loop = radar_labels + [radar_labels[0]]

    fig_rad = go.Figure()
    fig_rad.add_trace(go.Scatterpolar(
        r=radar_scores, theta=radar_labels_loop,
        fill='toself', name='Accept=1, Reject=0',
        line_color='#0d6efd', fillcolor='rgba(13,110,253,0.2)'
    ))
    fig_rad.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        title="Appraisal Radar — Coverage of Acceptance Criteria",
        height=450, template="plotly_white"
    )
    st.plotly_chart(fig_rad, use_container_width=True)

    # Key parameters recap
    st.markdown('<div class="section-header">📌 Key Parameters Summary</div>', unsafe_allow_html=True)
    summary_df = pd.DataFrame({
        "Parameter": ["Initial Investment", "Project Life", "Discount Rate / WACC",
                      "NPV", "IRR", "MIRR", "Profitability Index",
                      "Simple Payback", "Discounted Payback", "ARR",
                      "MC P(NPV > 0)", "MC Mean NPV"],
        "Value": [
            fmt(initial_investment, "$"), f"{project_life} years", f"{discount_rate}%",
            fmt(npv_val, "$"),
            f"{irr_val*100:.2f}%" if irr_val else "N/A",
            f"{mirr_val*100:.2f}%" if mirr_val else "N/A",
            f"{pi_val:.4f}",
            f"{pb_y}y {pb_m}m" if pb_y is not None else "Never",
            f"{dpb_y}y {dpb_m}m" if dpb_y is not None else "Never",
            f"{arr_val:.2f}%",
            f"{prob_positive:.1f}%",
            fmt(mc_mean, "$")
        ]
    })
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<center><small>Investment Appraisal Suite &nbsp;|&nbsp; "
    "Techniques: NPV · IRR · MIRR · Payback · Discounted Payback · PI · ARR · "
    "Sensitivity Analysis · Monte Carlo &nbsp;|&nbsp; "
    "For educational and professional use</small></center>",
    unsafe_allow_html=True
)