# ============================================================================
#  BUSINESS CASE — Section
#  Page 5.1 · End-to-End Case Builder  (CAPSTONE)
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="5.1 · End-to-End Case Builder",
    page_icon="🏗️",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Parts 0–4)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .bc-hero {
            background: linear-gradient(120deg, #0B3D91 0%, #1565C0 55%, #1E88E5 100%);
            padding: 34px 40px; border-radius: 18px; color: #ffffff;
            box-shadow: 0 10px 28px rgba(11,61,145,0.28); margin-bottom: 10px;
        }
        .bc-hero h1 { color:#ffffff; margin:0; font-size:2.0rem; font-weight:800; }
        .bc-hero p  { color:#E8F0FE; margin:8px 0 0 0; font-size:1.05rem; }
        .bc-pill {
            display:inline-block; background:rgba(255,255,255,0.18);
            padding:5px 14px; border-radius:30px; font-size:0.8rem;
            margin-top:14px; letter-spacing:.4px;
        }
        .bc-card {
            background:#ffffff; border:1px solid #E3E8EF; border-left:5px solid #1565C0;
            padding:18px 22px; border-radius:12px; margin:12px 0;
            box-shadow:0 3px 10px rgba(0,0,0,0.05);
        }
        .bc-card h4 { margin-top:0; color:#0B3D91; }
        .bc-key {
            background:#F1F7FF; border:1px solid #CFE2FF; border-radius:12px;
            padding:16px 20px; margin:10px 0;
        }
        .verdict-go {
            background:#E7F6EC; border:1px solid #B7E1C4; border-left:6px solid #1B7F3B;
            padding:18px 22px; border-radius:12px; margin:12px 0;
        }
        .verdict-no {
            background:#FDECEC; border:1px solid #F4C0C0; border-left:6px solid #C62828;
            padding:18px 22px; border-radius:12px; margin:12px 0;
        }
        .verdict-caution {
            background:#FFF7E6; border:1px solid #F5D9A0; border-left:6px solid #F9A825;
            padding:18px 22px; border-radius:12px; margin:12px 0;
        }
        .bc-tag {
            display:inline-block; background:#0B3D91; color:#fff; border-radius:6px;
            padding:2px 10px; font-size:.72rem; font-weight:700; margin-right:8px;
        }
        .good { color:#1B7F3B; font-weight:700; }
        .bad  { color:#C62828; font-weight:700; }
        .muted{ color:#5A6472; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="bc-hero">
        <span class="bc-tag">PART 5 · BUILD A REAL BUSINESS CASE</span>
        <h1>🏗️ 5.1 · End-to-End Case Builder</h1>
        <p>The capstone. Enter your investment once and see every method work together —
        cash flows, Payback, Discounted Payback, NPV, IRR, MIRR and PI — ending in a
        board-ready recommendation.</p>
        <div class="bc-pill">🧩 Inputs &nbsp;•&nbsp; 📊 Cash Flows &nbsp;•&nbsp; 🎯 Appraisal Dashboard &nbsp;•&nbsp; 📝 Recommendation</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Integrate everything from Parts 0–4 into a single, coherent investment "
           "appraisal and a defensible recommendation.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr_bisection(cashflows, low=-0.9, high=1.0, tol=1e-6, max_iter=200):
    grid = np.linspace(low, high, 250)
    prev_r, prev_v = grid[0], npv(grid[0], cashflows)
    bracket = None
    for r in grid[1:]:
        v = npv(r, cashflows)
        if prev_v == 0:
            return prev_r
        if prev_v * v < 0:
            bracket = (prev_r, r)
            break
        prev_r, prev_v = r, v
    if bracket is None:
        return None
    a, b = bracket
    fa = npv(a, cashflows)
    for _ in range(max_iter):
        m = (a + b) / 2
        fm = npv(m, cashflows)
        if abs(fm) < tol:
            return m
        if fa * fm < 0:
            b = m
        else:
            a, fa = m, fm
    return (a + b) / 2


def mirr(cashflows, finance_rate, reinvest_rate):
    n = len(cashflows) - 1
    pv_neg = sum(cf / (1 + finance_rate) ** t for t, cf in enumerate(cashflows) if cf < 0)
    fv_pos = sum(cf * (1 + reinvest_rate) ** (n - t) for t, cf in enumerate(cashflows) if cf > 0)
    if pv_neg == 0 or fv_pos <= 0:
        return None
    return (fv_pos / -pv_neg) ** (1 / n) - 1


def payback(cumulative, series):
    for i in range(1, len(cumulative)):
        if cumulative[i - 1] < 0 <= cumulative[i]:
            denom = series[i] if series[i] != 0 else 1
            return (i - 1) + (-cumulative[i - 1] / denom)
    return None


# ----------------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------------
tab_inputs, tab_cf, tab_dash, tab_reco = st.tabs(
    ["🧩  Inputs", "📊  Cash Flows", "🎯  Appraisal Dashboard", "📝  Recommendation"]
)

# ============================================================================
# SHARED STATE — build inputs in tab 1, reuse everywhere
# ============================================================================
if "case" not in st.session_state:
    st.session_state.case = {}

# ============================================================================
# TAB 1 — INPUTS
# ============================================================================
with tab_inputs:
    st.subheader("🧩 Step 1 · Define Your Investment")
    st.markdown("Enter the project details below. Everything else — cash flows, metrics and the "
                "recommendation — updates automatically from these inputs.")

    cA, cB = st.columns(2)
    with cA:
        project_name = st.text_input("Project name", value="Packing Line Automation")
        invest = st.number_input("Initial investment — Capex (€, Year 0)",
                                 min_value=0, value=800_000, step=25_000)
        working_capital = st.number_input("Initial working capital (€, Year 0)",
                                          min_value=0, value=100_000, step=10_000)
        life = st.slider("Project life (years)", 1, 15, 5)
    with cB:
        rate = st.slider("Discount rate / WACC (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
        tax = st.slider("Tax rate (%)", 0.0, 50.0, 30.0, 1.0) / 100.0
        salvage = st.number_input("Salvage value at end (€, pre-tax)",
                                  min_value=0, value=120_000, step=10_000)
        cutoff = st.number_input("Max acceptable payback (years)", min_value=0.0, value=4.0, step=0.5)

    st.markdown("##### Operating drivers")
    cC, cD, cE = st.columns(3)
    with cC:
        units = st.number_input("Annual sales volume (units)", min_value=0, value=10_000, step=500)
    with cD:
        price = st.number_input("Selling price (€/unit)", min_value=0.0, value=100.0, step=5.0)
    with cE:
        var_cost = st.number_input("Variable cost (€/unit)", min_value=0.0, value=60.0, step=5.0)

    cF, cG = st.columns(2)
    with cF:
        fixed_cost = st.number_input("Annual fixed cost (€)", min_value=0, value=150_000, step=10_000)
    with cG:
        growth = st.slider("Annual growth in volume (%)", -20, 30, 0) / 100.0

    recover_wc = st.checkbox("Recover working capital in final year", value=True)

    # Save to state
    st.session_state.case = dict(
        project_name=project_name, invest=invest, working_capital=working_capital, life=life,
        rate=rate, tax=tax, salvage=salvage, cutoff=cutoff, units=units, price=price,
        var_cost=var_cost, fixed_cost=fixed_cost, growth=growth, recover_wc=recover_wc,
    )

    st.success("✅ Inputs saved. Move to the **Cash Flows** tab to see the model build itself.")
    st.info("💡 Tip: This single input set drives all six appraisal methods — change anything here and "
            "every downstream metric and the recommendation update instantly.")

# ============================================================================
# BUILD THE MODEL (from saved state)
# ============================================================================
c = st.session_state.case
dep = (c["invest"]) / c["life"] if c["life"] else 0  # straight-line on capex

years = list(range(0, c["life"] + 1))
capex_row, wc_row, op_row, salv_row, net_row = [], [], [], [], []
salvage_net = c["salvage"] * (1 - c["tax"])

for y in years:
    if y == 0:
        capex_row.append(-c["invest"])
        wc_row.append(-c["working_capital"])
        op_row.append(0.0)
        salv_row.append(0.0)
    else:
        vol = c["units"] * ((1 + c["growth"]) ** (y - 1))
        revenue = vol * c["price"]
        variable = vol * c["var_cost"]
        ebit = revenue - variable - c["fixed_cost"] - dep
        taxamt = max(ebit, 0) * c["tax"]
        ocf = (ebit - taxamt) + dep
        capex_row.append(0.0)
        wc_row.append(c["working_capital"] if (y == c["life"] and c["recover_wc"]) else 0.0)
        op_row.append(ocf)
        salv_row.append(salvage_net if y == c["life"] else 0.0)
    net_row.append(capex_row[-1] + wc_row[-1] + op_row[-1] + salv_row[-1])

cum_simple = pd.Series(net_row).cumsum().tolist()
dfs = [1 / (1 + c["rate"]) ** t for t in years]
pv_row = [n * d for n, d in zip(net_row, dfs)]
cum_disc = pd.Series(pv_row).cumsum().tolist()

# Metrics
project_npv = sum(pv_row)
irr_val = irr_bisection(net_row)
mirr_val = mirr(net_row, c["rate"], c["rate"])
pi = (sum(pv_row[1:]) / -pv_row[0]) if pv_row[0] != 0 else np.nan
pb_simple = payback(cum_simple, net_row)
pb_disc = payback(cum_disc, pv_row)

# ============================================================================
# TAB 2 — CASH FLOWS
# ============================================================================
with tab_cf:
    st.subheader(f"📊 Step 2 · Cash-Flow Model — {c['project_name']}")
    st.markdown("Built automatically from your inputs, using the incremental cash-flow logic from "
                "page 0.2 and discounting from page 0.3.")

    cf_df = pd.DataFrame(
        {
            "Year": years,
            "Capex (€)": capex_row,
            "Working Capital (€)": wc_row,
            "Operating CF (€)": op_row,
            "Salvage net (€)": salv_row,
            "Net Cash Flow (€)": net_row,
            "Discount Factor": [round(d, 4) for d in dfs],
            "Present Value (€)": pv_row,
            "Cumulative PV (€)": cum_disc,
        }
    )
    st.dataframe(
        cf_df.style.format({col: "{:,.0f}" for col in cf_df.columns
                            if col not in ("Year", "Discount Factor")}
                           | {"Discount Factor": "{:.4f}"}),
        use_container_width=True, hide_index=True,
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("Annual depreciation", f"€{dep:,.0f}")
    m2.metric("Total net (undiscounted)", f"€{sum(net_row):,.0f}")
    m3.metric("PV of net cash flows", f"€{project_npv + 0:,.0f}")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=net_row, name="Net cash flow",
                         marker_color=["#C62828"] + ["#1E88E5"] * c["life"]))
    fig.add_trace(go.Scatter(x=years, y=cum_disc, name="Cumulative PV",
                             mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="grey")
    fig.update_layout(title="Cash-flow profile & cumulative present value",
                      xaxis_title="Year", yaxis_title="€", height=440,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# TAB 3 — APPRAISAL DASHBOARD
# ============================================================================
with tab_dash:
    st.subheader("🎯 Step 3 · Appraisal Dashboard — Every Method at a Glance")
    st.markdown("All six techniques from Parts 1–2, computed on the same cash flows.")

    r1c1, r1c2, r1c3 = st.columns(3)
    r1c1.metric("NPV", f"€{project_npv:,.0f}",
                "Accept" if project_npv > 0 else "Reject")
    r1c2.metric("IRR", f"{irr_val*100:.1f}%" if irr_val is not None else "n/a",
                f"vs {c['rate']*100:.1f}% hurdle" if irr_val is not None else "")
    r1c3.metric("MIRR", f"{mirr_val*100:.1f}%" if mirr_val is not None else "n/a")

    r2c1, r2c2, r2c3 = st.columns(3)
    r2c1.metric("Profitability Index", f"{pi:.3f}" if not np.isnan(pi) else "n/a",
                "Accept" if (not np.isnan(pi) and pi > 1) else "Reject")
    r2c2.metric("Payback", f"{pb_simple:.2f} yrs" if pb_simple else "Never",
                f"cutoff {c['cutoff']:.1f}")
    r2c3.metric("Discounted Payback", f"{pb_disc:.2f} yrs" if pb_disc else "Never")

    # Summary decision table
    st.markdown("##### Method-by-method verdict")
    def verdict_npv():
        return "✅ Accept" if project_npv > 0 else "❌ Reject"
    def verdict_irr():
        if irr_val is None:
            return "⚠️ n/a"
        return "✅ Accept" if irr_val > c["rate"] else "❌ Reject"
    def verdict_pi():
        if np.isnan(pi):
            return "⚠️ n/a"
        return "✅ Accept" if pi > 1 else "❌ Reject"
    def verdict_pb():
        if pb_simple is None:
            return "❌ Reject"
        return "✅ Accept" if pb_simple <= c["cutoff"] else "🟠 Marginal"
    def verdict_dpb():
        if pb_disc is None:
            return "❌ Reject"
        return "✅ Accept" if pb_disc <= c["cutoff"] else "🟠 Marginal"

    summary = pd.DataFrame(
        {
            "Method": ["NPV", "IRR", "MIRR", "Profitability Index",
                       "Payback", "Discounted Payback"],
            "Result": [
                f"€{project_npv:,.0f}",
                f"{irr_val*100:.1f}%" if irr_val is not None else "n/a",
                f"{mirr_val*100:.1f}%" if mirr_val is not None else "n/a",
                f"{pi:.3f}" if not np.isnan(pi) else "n/a",
                f"{pb_simple:.2f} yrs" if pb_simple else "Never",
                f"{pb_disc:.2f} yrs" if pb_disc else "Never",
            ],
            "Rule": ["NPV > 0", f"IRR > {c['rate']*100:.1f}%", f"MIRR > {c['rate']*100:.1f}%",
                     "PI > 1", f"≤ {c['cutoff']:.1f} yrs", f"≤ {c['cutoff']:.1f} yrs"],
            "Verdict": [verdict_npv(), verdict_irr(),
                        "✅ Accept" if (mirr_val is not None and mirr_val > c["rate"]) else "⚠️ n/a",
                        verdict_pi(), verdict_pb(), verdict_dpb()],
        }
    )
    st.dataframe(summary, use_container_width=True, hide_index=True)

    # NPV profile
    rates = np.linspace(0, 0.5, 51)
    npvs = [npv(rr, net_row) for rr in rates]
    figp = go.Figure(go.Scatter(x=rates * 100, y=npvs, mode="lines",
                                line=dict(color="#0B3D91", width=3), name="NPV"))
    figp.add_hline(y=0, line_dash="dash", line_color="#C62828")
    figp.add_vline(x=c["rate"] * 100, line_dash="dot", line_color="#1B7F3B",
                   annotation_text=f"WACC {c['rate']*100:.1f}%", annotation_position="bottom")
    if irr_val is not None:
        figp.add_vline(x=irr_val * 100, line_dash="dot", line_color="#F9A825",
                       annotation_text=f"IRR {irr_val*100:.1f}%", annotation_position="top")
    figp.update_layout(title="NPV profile", xaxis_title="Discount rate (%)", yaxis_title="NPV (€)",
                       height=420, margin=dict(t=60, b=40))
    st.plotly_chart(figp, use_container_width=True)

# ============================================================================
# TAB 4 — RECOMMENDATION
# ============================================================================
with tab_reco:
    st.subheader("📝 Step 4 · Recommendation")
    st.markdown("A board-ready synthesis of the analysis — the kind of summary that goes to the top "
                "of a business case.")

    # Count accept signals
    signals = []
    signals.append(project_npv > 0)
    if irr_val is not None:
        signals.append(irr_val > c["rate"])
    if not np.isnan(pi):
        signals.append(pi > 1)
    if pb_disc is not None:
        signals.append(pb_disc <= c["cutoff"])
    accept_count = sum(signals)
    total_signals = len(signals)

    headline = "INVEST" if project_npv > 0 else "DO NOT INVEST"
    if project_npv > 0 and accept_count == total_signals:
        css, icon, tone = "verdict-go", "✅", "strongly supports proceeding"
    elif project_npv > 0:
        css, icon, tone = "verdict-caution", "🟠", "supports proceeding with some caution"
    else:
        css, icon, tone = "verdict-no", "❌", "does not support proceeding"

    irr_txt = f"{irr_val*100:.1f}%" if irr_val is not None else "n/a"
    pi_txt = f"{pi:.2f}" if not np.isnan(pi) else "n/a"
    pb_txt = f"{pb_disc:.2f} years" if pb_disc else "not within life"

    st.markdown(
        f"""
        <div class="{css}">
        <h3 style="margin-top:0;">{icon} Recommendation: <b>{headline}</b> — {c['project_name']}</h3>
        <p>The financial analysis <b>{tone}</b>. The project delivers an <b>NPV of €{project_npv:,.0f}</b>
        at a {c['rate']*100:.1f}% cost of capital, an <b>IRR of {irr_txt}</b>, a
        <b>profitability index of {pi_txt}</b>, and a <b>discounted payback of {pb_txt}</b>
        (against a {c['cutoff']:.1f}-year target). {accept_count} of {total_signals} quantitative
        criteria support acceptance.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Executive summary card
    st.markdown("##### Executive summary")
    exec_df = pd.DataFrame(
        {
            "Item": ["Investment (Capex + WC)", "Project life", "Discount rate (WACC)",
                     "NPV", "IRR", "Profitability Index", "Discounted payback", "Recommendation"],
            "Value": [
                f"€{c['invest'] + c['working_capital']:,.0f}",
                f"{c['life']} years",
                f"{c['rate']*100:.1f}%",
                f"€{project_npv:,.0f}",
                irr_txt if irr_val is None else f"{irr_val*100:.1f}%",
                pi_txt,
                pb_txt,
                headline,
            ],
        }
    )
    st.dataframe(exec_df, use_container_width=True, hide_index=True)

    # Downloadable text summary
    reco_text = f"""BUSINESS CASE — RECOMMENDATION SUMMARY
Project: {c['project_name']}

INVESTMENT
  Initial Capex:            EUR {c['invest']:,.0f}
  Initial working capital:  EUR {c['working_capital']:,.0f}
  Project life:             {c['life']} years
  Discount rate (WACC):     {c['rate']*100:.1f}%
  Tax rate:                 {c['tax']*100:.1f}%

RESULTS
  NPV:                      EUR {project_npv:,.0f}
  IRR:                      {irr_txt}
  MIRR:                     {mirr_val*100:.1f}% {'' if mirr_val is not None else '(n/a)'}
  Profitability Index:      {pi_txt}
  Simple payback:           {f'{pb_simple:.2f} years' if pb_simple else 'Never'}
  Discounted payback:       {pb_txt}
  Criteria supporting:      {accept_count} of {total_signals}

RECOMMENDATION: {headline}

Note: Confirm qualitative factors (strategic fit, ESG, risk, compliance) and
governance/approval authority (see pages 4.2–4.3) before final sign-off.
"""
    st.download_button("⬇️ Download recommendation summary (.txt)", data=reco_text,
                       file_name=f"business_case_{c['project_name'].replace(' ', '_')}.txt",
                       mime="text/plain")

    st.markdown("##### ✅ Before final sign-off — checklist")
    st.markdown(
        """
        - [ ] Cash-flow assumptions validated with data owners (page 0.2)
        - [ ] Discount rate agreed with Finance (page 0.3)
        - [ ] Sensitivity & scenario / Monte Carlo risk analysis run (pages 3.1–3.3)
        - [ ] Qualitative factors & ESG assessed (page 4.3)
        - [ ] Correct approval authority per Delegation of Authority (page 4.3)
        - [ ] Post-investment review scheduled to track benefit delivery
        """
    )

    st.info("💡 This recommendation reflects the **quantitative** case. A complete business case also "
            "documents qualitative factors, risks, assumptions, and the implementation plan.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `4.3 · Qualitative Factors & Governance`")
with cnext:
    st.markdown("**Next:** `6.1 · Master Quiz` ➡️")
st.caption("Business Case section · Page 5.1 (Capstone) · Built with Streamlit")
