# ============================================================================
#  BUSINESS CASE — Section
#  Page 3.1 · Sensitivity Analysis
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
    page_title="3.1 · Sensitivity Analysis",
    page_icon="🌪️",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Parts 0–2)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .bc-hero {
            background: linear-gradient(120deg, #0B3D91 0%, #1565C0 55%, #1E88E5 100%);
            padding: 34px 40px; border-radius: 18px; color: #ffffff;
            box-shadow: 0 10px 28px rgba(11,61,145,0.28); margin-bottom: 10px;
        }
        .bc-hero h1 { color:#ffffff; margin:0; font-size:2.05rem; font-weight:800; }
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
        .bc-step {
            background:#ffffff; border:1px solid #E3E8EF; border-radius:12px;
            padding:14px 18px; margin:8px 0; box-shadow:0 2px 6px rgba(0,0,0,0.04);
        }
        .bc-step b { color:#1565C0; }
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
        <span class="bc-tag">PART 3 · ADVANCED EVALUATION &amp; RISK</span>
        <h1>3.1 · Sensitivity Analysis</h1>
        <p>Stress-test the business case — which single assumption, if wrong,
        does the most damage to your NPV? Find the critical variables before the board does.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Run one-variable-at-a-time sensitivity, read a tornado chart, and find "
           "the break-even value of each key assumption.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def project_npv(units, price, var_cost, fixed_cost, invest, rate, life, tax, dep=None):
    """Simple annuity-style project NPV from operating drivers."""
    if dep is None:
        dep = invest / life if life else 0
    revenue = units * price
    var = units * var_cost
    ebit = revenue - var - fixed_cost - dep
    taxamt = max(ebit, 0) * tax
    ocf = (ebit - taxamt) + dep
    pv = sum(ocf / (1 + rate) ** t for t in range(1, life + 1))
    return pv - invest, ocf


# ----------------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------------
tab_theory, tab_example, tab_lab, tab_quiz = st.tabs(
    ["📘  Theory", "🧮  Worked Example", "🎛️  Interactive Lab", "✅  Quiz"]
)

# ============================================================================
# TAB 1 — THEORY
# ============================================================================
with tab_theory:
    st.subheader("1 · Definition")
    st.markdown(
        """
        <div class="bc-key">
        <b>Sensitivity Analysis</b> asks a simple but powerful question: <i>“What happens to my result
        (usually NPV) if one input changes while everything else stays the same?”</i> By flexing each
        assumption one at a time, you discover which variables the decision is <b>most sensitive</b> to —
        the ones that deserve the most scrutiny and risk management.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · Why It Matters")
    st.markdown(
        """
        Every business case is built on **estimates** — sales volume, price, costs, the discount rate.
        Some are far more critical than others. Sensitivity analysis:
        - Identifies the **critical few** variables that drive the outcome
        - Shows how much "room for error" each assumption has before the decision flips
        - Directs **management attention and data-gathering** to what matters most
        - Strengthens the **credibility** of the business case with decision-makers
        """
    )

    st.subheader("3 · The One-Variable-at-a-Time Method")
    for t, b in [
        ("1️⃣ Establish the base case",
         "Compute the NPV using your best-estimate ('most likely') inputs."),
        ("2️⃣ Flex one variable",
         "Change a single input by a set amount (e.g. ±10%) while holding all others constant."),
        ("3️⃣ Recompute the result",
         "Record the new NPV and the change from the base case."),
        ("4️⃣ Repeat for each variable",
         "Do the same for every key assumption to build a complete picture."),
        ("5️⃣ Rank by impact",
         "Order variables by how much they move the NPV — visualise with a tornado chart."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("4 · The Tornado Chart")
    st.markdown(
        """
        A **tornado chart** is a horizontal bar chart that ranks variables by their impact on NPV —
        the widest bar (most impactful) at the top, narrowing downward like a tornado. It's the single
        most effective way to communicate *what matters most* to a decision-maker at a glance.
        """
    )

    st.subheader("5 · Break-Even (Switching) Values")
    st.markdown(
        """
        The **break-even** or **switching value** of a variable is the level at which **NPV = 0** —
        the point where the decision flips from accept to reject. The closer a variable's break-even is
        to its base case, the **riskier** that assumption:
        """
    )
    st.latex(r"\text{Sensitivity margin} = \frac{\text{Break-even value} - \text{Base value}}{\text{Base value}}")
    st.markdown(
        "<span class='muted'>A small margin (e.g. sales can only fall 5% before NPV turns negative) is "
        "a red flag; a large margin means the case is robust to that variable.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("6 · Strengths & Limitations")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👍 Strengths</h4>
            <ul>
              <li>Simple, transparent, and easy to communicate</li>
              <li>Pinpoints the <b>critical variables</b></li>
              <li>Highlights where <b>more research</b> is worthwhile</li>
              <li>Reveals the <b>margin of safety</b> in each assumption</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👎 Limitations</h4>
            <ul>
              <li>Changes <b>one variable at a time</b> — ignores interactions</li>
              <li>Doesn't assign <b>probabilities</b> to outcomes</li>
              <li>Variables often move <b>together</b> in reality (correlation)</li>
              <li>For combined effects use <b>scenario</b> (3.2) or <b>Monte Carlo</b> (3.3)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - Sensitivity analysis flexes **one input at a time** to see its impact on NPV.
            - The **tornado chart** ranks variables by impact — widest (most critical) on top.
            - The **break-even / switching value** is where NPV = 0; small margins = high risk.
            - It ignores interactions & probabilities — extend with **scenario** and **Monte Carlo**.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Sensitivity of a Project's NPV to ±10% Swings")
    st.markdown(
        """
        <div class="bc-key">
        <b>Base case.</b> A project sells <b>10,000 units</b> at <b>€100</b>, with variable cost
        <b>€60</b>/unit and fixed cost <b>€150,000</b>/yr. It needs <b>€800,000</b> of investment,
        runs <b>5 years</b>, tax <b>30%</b>, discount rate <b>10%</b>. We'll flex each driver ±10%.
        </div>
        """,
        unsafe_allow_html=True,
    )

    base = dict(units=10_000, price=100.0, var_cost=60.0, fixed_cost=150_000,
                invest=800_000, rate=0.10, life=5, tax=0.30)
    base_npv, base_ocf = project_npv(**base)

    st.metric("Base-case NPV", f"€{base_npv:,.0f}", help=f"Annual operating cash flow ≈ €{base_ocf:,.0f}")

    # Flex each variable ±10%
    variables = {
        "Sales volume (units)": "units",
        "Selling price": "price",
        "Variable cost/unit": "var_cost",
        "Fixed cost": "fixed_cost",
        "Initial investment": "invest",
        "Discount rate": "rate",
    }
    rows = []
    for label, key in variables.items():
        low_args = dict(base); high_args = dict(base)
        low_args[key] = base[key] * 0.90
        high_args[key] = base[key] * 1.10
        npv_low = project_npv(**low_args)[0]
        npv_high = project_npv(**high_args)[0]
        rows.append({
            "Variable": label,
            "NPV @ −10% (€)": npv_low,
            "NPV @ +10% (€)": npv_high,
            "Swing (€)": abs(npv_high - npv_low),
        })
    sens = pd.DataFrame(rows).sort_values("Swing (€)", ascending=False).reset_index(drop=True)

    st.dataframe(
        sens.style.format({"NPV @ −10% (€)": "{:,.0f}", "NPV @ +10% (€)": "{:,.0f}",
                           "Swing (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    st.markdown("#### Tornado chart — impact of a ±10% change on NPV")
    sens_sorted = sens.sort_values("Swing (€)", ascending=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=sens_sorted["Variable"], x=sens_sorted["NPV @ −10% (€)"] - base_npv,
        base=base_npv, orientation="h", name="−10%", marker_color="#EF9A9A",
    ))
    fig.add_trace(go.Bar(
        y=sens_sorted["Variable"], x=sens_sorted["NPV @ +10% (€)"] - base_npv,
        base=base_npv, orientation="h", name="+10%", marker_color="#1565C0",
    ))
    fig.add_vline(x=base_npv, line_dash="dash", line_color="#0B3D91",
                  annotation_text=f"Base NPV €{base_npv:,.0f}", annotation_position="top")
    fig.add_vline(x=0, line_dash="dot", line_color="#C62828")
    fig.update_layout(title="Tornado chart — NPV sensitivity to ±10% changes",
                      barmode="overlay", xaxis_title="NPV (€)", height=430,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    top_var = sens.iloc[0]["Variable"]
    st.success(f"✅ **{top_var}** has the biggest impact on NPV — a ±10% move swings NPV by "
               f"€{sens.iloc[0]['Swing (€)']:,.0f}. This is the assumption to validate most carefully "
               f"and manage most closely.")
    st.info("👉 Notice how price and volume typically dominate — small percentage errors there move "
            "NPV far more than an equivalent error in fixed cost.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Sensitivity Engine")
    st.markdown("Set your base case, choose the swing size, and generate a live tornado chart plus "
                "break-even analysis for the variable you care about.")

    st.markdown("##### Base-case inputs")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        units = st.number_input("Sales volume (units)", min_value=0, value=10_000, step=500)
        price = st.number_input("Selling price (€)", min_value=0.0, value=100.0, step=5.0)
    with c2:
        var_cost = st.number_input("Variable cost/unit (€)", min_value=0.0, value=60.0, step=5.0)
        fixed_cost = st.number_input("Fixed cost/yr (€)", min_value=0, value=150_000, step=10_000)
    with c3:
        invest = st.number_input("Initial investment (€)", min_value=1, value=800_000, step=25_000)
        life = st.slider("Project life (years)", 1, 15, 5)
    with c4:
        rate = st.slider("Discount rate (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
        tax = st.slider("Tax rate (%)", 0.0, 50.0, 30.0, 1.0) / 100.0

    swing = st.slider("Swing size for sensitivity (± %)", 5, 50, 10, 5)
    s = swing / 100.0

    base = dict(units=units, price=price, var_cost=var_cost, fixed_cost=fixed_cost,
                invest=invest, rate=rate, life=life, tax=tax)
    base_npv, base_ocf = project_npv(**base)

    m1, m2 = st.columns(2)
    m1.metric("Base-case NPV", f"€{base_npv:,.0f}")
    m2.metric("Annual operating CF", f"€{base_ocf:,.0f}")

    variables = {
        "Sales volume": "units",
        "Selling price": "price",
        "Variable cost/unit": "var_cost",
        "Fixed cost": "fixed_cost",
        "Initial investment": "invest",
        "Discount rate": "rate",
    }
    rows = []
    for label, key in variables.items():
        low_args = dict(base); high_args = dict(base)
        low_args[key] = base[key] * (1 - s)
        high_args[key] = base[key] * (1 + s)
        npv_low = project_npv(**low_args)[0]
        npv_high = project_npv(**high_args)[0]
        rows.append({"Variable": label, "NPV low (€)": npv_low, "NPV high (€)": npv_high,
                     "Swing (€)": abs(npv_high - npv_low)})
    sens = pd.DataFrame(rows).sort_values("Swing (€)", ascending=False).reset_index(drop=True)

    st.dataframe(
        sens.style.format({"NPV low (€)": "{:,.0f}", "NPV high (€)": "{:,.0f}", "Swing (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    sens_sorted = sens.sort_values("Swing (€)", ascending=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(y=sens_sorted["Variable"], x=sens_sorted["NPV low (€)"] - base_npv,
                         base=base_npv, orientation="h", name=f"−{swing}%", marker_color="#EF9A9A"))
    fig.add_trace(go.Bar(y=sens_sorted["Variable"], x=sens_sorted["NPV high (€)"] - base_npv,
                         base=base_npv, orientation="h", name=f"+{swing}%", marker_color="#1565C0"))
    fig.add_vline(x=base_npv, line_dash="dash", line_color="#0B3D91")
    fig.add_vline(x=0, line_dash="dot", line_color="#C62828")
    fig.update_layout(title=f"Tornado chart — NPV sensitivity to ±{swing}%",
                      barmode="overlay", xaxis_title="NPV (€)", height=430,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("🎯 Break-Even (Switching) Value Finder")
    st.markdown("Pick a variable and see how far it can move before NPV hits zero.")

    target = st.selectbox("Variable to break-even test",
                          ["Sales volume", "Selling price", "Variable cost/unit", "Fixed cost"])
    key_map = {"Sales volume": "units", "Selling price": "price",
               "Variable cost/unit": "var_cost", "Fixed cost": "fixed_cost"}
    key = key_map[target]

    # sweep the variable to find NPV = 0 crossing
    base_val = base[key]
    if key in ("var_cost", "fixed_cost"):
        sweep = np.linspace(base_val * 0.5, base_val * 2.0, 200)
    else:
        sweep = np.linspace(base_val * 0.3, base_val * 1.7, 200)
    npv_curve = []
    for v in sweep:
        args = dict(base); args[key] = v
        npv_curve.append(project_npv(**args)[0])

    breakeven = None
    for i in range(1, len(npv_curve)):
        if (npv_curve[i - 1] > 0 >= npv_curve[i]) or (npv_curve[i - 1] < 0 <= npv_curve[i]):
            x0, x1, y0, y1 = sweep[i - 1], sweep[i], npv_curve[i - 1], npv_curve[i]
            breakeven = x0 + (x1 - x0) * (0 - y0) / (y1 - y0)
            break

    figb = go.Figure(go.Scatter(x=sweep, y=npv_curve, mode="lines",
                                line=dict(color="#0B3D91", width=3), name="NPV"))
    figb.add_hline(y=0, line_dash="dash", line_color="#C62828")
    figb.add_vline(x=base_val, line_dash="dot", line_color="#1B7F3B",
                   annotation_text=f"Base {base_val:,.0f}", annotation_position="top")
    if breakeven is not None:
        figb.add_vline(x=breakeven, line_dash="dot", line_color="#F9A825",
                       annotation_text=f"Break-even {breakeven:,.0f}", annotation_position="bottom")
    figb.update_layout(title=f"NPV vs {target}", xaxis_title=target, yaxis_title="NPV (€)",
                       height=400, margin=dict(t=60, b=40))
    st.plotly_chart(figb, use_container_width=True)

    if breakeven is not None:
        margin = (breakeven - base_val) / base_val * 100
        st.success(f"🎯 **Break-even {target.lower()} ≈ {breakeven:,.0f}** vs base {base_val:,.0f} — "
                   f"a margin of **{margin:+.1f}%** before NPV turns negative. "
                   + ("⚠️ Thin margin — high-risk assumption!" if abs(margin) < 15
                      else "A reasonable cushion on this variable."))
    else:
        st.info("No NPV = 0 crossing found in the tested range — the decision is robust to this "
                "variable across a wide band.")

    st.caption("Reminder: this flexes one variable at a time. Use Scenario (3.2) and Monte Carlo "
               "(3.3) for combined and probabilistic effects.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 5 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. Sensitivity analysis examines what happens to the result when…",
            "options": [
                "All variables change together randomly",
                "One variable changes while others are held constant",
                "The discount rate is ignored",
                "Only cash flows after payback change",
            ],
            "answer": 1,
            "why": "It is a one-variable-at-a-time technique: flex one input, hold the rest constant.",
        },
        {
            "q": "2. A tornado chart ranks variables by…",
            "options": [
                "Alphabetical order",
                "Their impact on the result (widest/most impactful on top)",
                "Their cost",
                "The year they occur",
            ],
            "answer": 1,
            "why": "Tornado charts order variables by impact, widest bar (most critical) at the top.",
        },
        {
            "q": "3. The break-even (switching) value of a variable is the level at which…",
            "options": ["NPV is maximised", "NPV equals zero",
                        "IRR equals zero", "Payback equals the cutoff"],
            "answer": 1,
            "why": "The switching value is where NPV = 0 — the point the decision flips.",
        },
        {
            "q": "4. A variable whose break-even value is very close to its base case is…",
            "options": ["Low risk", "High risk", "Irrelevant", "Always fixed"],
            "answer": 1,
            "why": "A small margin before NPV turns negative signals a high-risk, critical assumption.",
        },
        {
            "q": "5. A key limitation of sensitivity analysis is that it…",
            "options": [
                "Requires probabilities for every input",
                "Ignores interactions between variables that move together",
                "Cannot handle NPV",
                "Only works for payback",
            ],
            "answer": 1,
            "why": "Changing one variable at a time ignores correlations; use scenario or Monte Carlo for combined effects.",
        },
    ]

    with st.form("quiz_3_1"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q31_{i}")
            responses.append(choice)
            st.markdown("<hr style='margin:6px 0;'>", unsafe_allow_html=True)
        submitted = st.form_submit_button("📊 Submit answers")

    if submitted:
        score = 0
        for i, item in enumerate(questions):
            chosen = responses[i]
            correct_text = item["options"][item["answer"]]
            if chosen == correct_text:
                score += 1
                st.success(f"**Q{i+1}: Correct ✅** — {item['why']}")
            else:
                st.error(f"**Q{i+1}: Not quite ❌** — Correct answer: *{correct_text}*.\n\n{item['why']}")
        pct = score / len(questions) * 100
        st.markdown("---")
        st.metric("Your score", f"{score} / {len(questions)}", f"{pct:.0f}%")
        if pct == 100:
            st.balloons()
            st.success("🏆 Perfect! You can now stress-test any business case with confidence.")
        elif pct >= 60:
            st.info("👍 Good work — continue to **3.2 · Scenario Analysis**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on tornado charts and switching values.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `2.4 · Profitability Index (PI)`")
with cnext:
    st.markdown("**Next:** `3.2 · Scenario Analysis` ➡️")
st.caption("Business Case section · Page 3.1 · Built with Streamlit")
