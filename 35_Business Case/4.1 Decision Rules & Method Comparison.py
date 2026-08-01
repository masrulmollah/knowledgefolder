# ============================================================================
#  BUSINESS CASE — Section
#  Page 4.1 · Decision Rules & Method Comparison
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
    page_title="4.1 · Decision Rules & Method Comparison",
    page_icon="⚖️",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Parts 0–3)
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
        <span class="bc-tag">PART 4 · DECISION-MAKING FRAMEWORK</span>
        <h1>4.1 · Decision Rules &amp; Method Comparison</h1>
        <p>Every method in one place — the accept/reject rules side by side,
        why NPV and IRR sometimes disagree, and how to pick the right tool for the decision.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Master the decision rule for every method, understand NPV–IRR conflicts, "
           "and know which method to trust in each situation.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr_bisection(cashflows, low=-0.9, high=1.0, tol=1e-6, max_iter=200):
    grid = np.linspace(low, high, 200)
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


def simple_payback(cashflows):
    cum = np.cumsum(cashflows)
    for i in range(1, len(cum)):
        if cum[i - 1] < 0 <= cum[i]:
            denom = cashflows[i] if cashflows[i] != 0 else 1
            return (i - 1) + (-cum[i - 1] / denom)
    return None


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
    st.subheader("1 · The Decision Rules — All in One Place")
    st.markdown(
        """
        <div class="bc-key">
        Each appraisal method has its own <b>accept/reject rule</b>. In a well-behaved single project
        they usually agree — but knowing each rule, and what each method really measures, is what lets
        you build a defensible recommendation.
        </div>
        """,
        unsafe_allow_html=True,
    )

    rules = pd.DataFrame(
        {
            "Method": ["Payback Period", "Discounted Payback", "ARR",
                       "NPV", "IRR", "MIRR", "Profitability Index"],
            "Measures": ["Time to recover outlay", "Time to recover (discounted)",
                         "Avg profit ÷ investment", "Value added today (€)",
                         "Project's own return (%)", "IRR with realistic reinvestment",
                         "PV inflows per € invested"],
            "Accept if": ["< target period", "< target period", "> target rate",
                          "> 0", "> hurdle rate", "> hurdle rate", "> 1"],
            "Time value?": ["No", "Yes", "No", "Yes", "Yes", "Yes", "Yes"],
        }
    )
    st.table(rules)

    st.subheader("2 · What Each Method Is Best For")
    for t, b in [
        ("💎 NPV — the decision-maker",
         "The primary rule for the go/no-go decision and for choosing between mutually exclusive "
         "projects. Measures absolute value creation."),
        ("🔄 IRR / MIRR — the communicator",
         "An intuitive % return for stakeholders. Use MIRR to avoid the reinvestment and multiple-IRR "
         "traps. Confirm against NPV."),
        ("📊 PI — the rationer",
         "Best for ranking projects when capital is limited — value per euro invested."),
        ("⏱️ Payback — the risk screen",
         "A fast liquidity/risk filter. Never the sole basis for a decision, but useful early."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("3 · When NPV and IRR Disagree")
    st.markdown(
        """
        For a **single conventional** project, NPV and IRR always agree on accept/reject. Conflicts
        arise when **ranking mutually exclusive** projects, due to:
        """
    )
    for t, b in [
        ("📏 Scale (size) differences",
         "IRR is a %, so it can favour a small, high-% project over a larger one that creates more "
         "total value. NPV captures the absolute € and wins."),
        ("⏳ Timing differences",
         "Projects with very different cash-flow timing can cross over — their NPV profiles intersect "
         "at a 'crossover rate'. Below it, one ranks higher; above it, the other."),
        ("🔁 Reinvestment assumption",
         "IRR assumes reinvestment at the IRR; NPV assumes the cost of capital. When this matters, "
         "MIRR or NPV is more realistic."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.info("👉 **Golden rule:** when NPV and IRR conflict for mutually exclusive projects, **follow "
            "NPV** — it directly measures the value added to the business.")

    st.subheader("4 · The Crossover Rate")
    st.markdown(
        """
        The **crossover rate** is the discount rate at which two projects have the **same NPV**. It is
        found by computing the IRR of the **differential cash flows** (Project A − Project B). Compare
        it to your cost of capital to see which project the NPV rule favours.
        """
    )

    st.subheader("5 · A Practical Decision Hierarchy")
    st.markdown(
        """
        1. **Screen** with payback / discounted payback for obvious liquidity or risk issues.
        2. **Decide** with **NPV** — the primary value rule.
        3. **Cross-check** with IRR/MIRR for an intuitive return, and PI if capital is rationed.
        4. **Stress-test** with sensitivity, scenario and Monte Carlo (Part 3).
        5. **Overlay** qualitative and strategic factors (page 4.3) before finalising.
        """
    )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - Know the **accept/reject rule** for every method (NPV > 0, IRR > hurdle, PI > 1…).
            - **NPV is the primary decision rule**; others support or communicate it.
            - NPV–IRR conflicts arise from **scale, timing and reinvestment** — follow **NPV**.
            - The **crossover rate** = IRR of the differential cash flows.
            - Combine quantitative rules with **risk analysis and qualitative judgement**.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Two Projects, One Budget — an NPV vs IRR Conflict")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> Two <b>mutually exclusive</b> projects, each costing <b>€500,000</b>, discount
        rate <b>10%</b>. <b>Project S</b> ("small & fast") returns cash early; <b>Project L</b>
        ("large & late") returns more overall but later. Which should we choose?
        </div>
        """,
        unsafe_allow_html=True,
    )

    r = 0.10
    proj_s = [-500_000, 300_000, 250_000, 150_000, 80_000, 40_000]
    proj_l = [-500_000, 80_000, 140_000, 220_000, 320_000, 380_000]

    npv_s, npv_l = npv(r, proj_s), npv(r, proj_l)
    irr_s, irr_l = irr_bisection(proj_s), irr_bisection(proj_l)
    pb_s, pb_l = simple_payback(proj_s), simple_payback(proj_l)

    comp = pd.DataFrame(
        {
            "Metric": ["NPV @ 10% (€)", "IRR (%)", "Payback (yrs)"],
            "Project S (early)": [f"{npv_s:,.0f}", f"{irr_s*100:.1f}%", f"{pb_s:.2f}"],
            "Project L (late)": [f"{npv_l:,.0f}", f"{irr_l*100:.1f}%", f"{pb_l:.2f}"],
        }
    )
    st.dataframe(comp, use_container_width=True, hide_index=True)

    conflict = (irr_s > irr_l) != (npv_s > npv_l)
    if conflict:
        st.warning("🟠 **Conflict!** IRR and payback favour **Project S**, but NPV favours "
                   f"**Project L** (€{npv_l:,.0f} vs €{npv_s:,.0f}). The methods disagree because of "
                   "timing and scale of cash flows.")
    st.success(f"✅ **Decision: follow NPV → choose Project {'L' if npv_l > npv_s else 'S'}.** "
               f"It adds the most value (€{max(npv_l, npv_s):,.0f}) at the 10% cost of capital, even "
               f"though Project S has the quicker payback and higher IRR.")

    # NPV profiles + crossover
    rates = np.linspace(0, 0.35, 71)
    npvs_s = [npv(rr, proj_s) for rr in rates]
    npvs_l = [npv(rr, proj_l) for rr in rates]
    diff = [a - b for a, b in zip(proj_s, proj_l)]
    crossover = irr_bisection(diff)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rates * 100, y=npvs_s, mode="lines", name="Project S",
                             line=dict(color="#1E88E5", width=3)))
    fig.add_trace(go.Scatter(x=rates * 100, y=npvs_l, mode="lines", name="Project L",
                             line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dot", line_color="grey")
    fig.add_vline(x=10, line_dash="dash", line_color="#1B7F3B",
                  annotation_text="Cost of capital 10%", annotation_position="top")
    if crossover is not None and 0 < crossover < 0.35:
        fig.add_vline(x=crossover * 100, line_dash="dot", line_color="#F9A825",
                      annotation_text=f"Crossover {crossover*100:.1f}%", annotation_position="bottom")
    fig.update_layout(title="NPV profiles — the crossover rate explains the conflict",
                      xaxis_title="Discount rate (%)", yaxis_title="NPV (€)",
                      height=450, legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    if crossover is not None:
        st.info(f"👉 The projects' NPV profiles cross at the **crossover rate ≈ {crossover*100:.1f}%**. "
                f"Because our 10% cost of capital is **below** the crossover, the later-cash project (L) "
                f"has the higher NPV. Above the crossover, the ranking would flip.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Method Comparison Engine")
    st.markdown("Edit two competing projects and the discount rate. The tool computes every metric, "
                "flags any NPV–IRR conflict, finds the crossover rate, and gives the NPV-based verdict.")

    c1, c2, c3 = st.columns(3)
    with c1:
        rate = st.slider("Discount rate / hurdle (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
    with c2:
        n_years = st.slider("Number of years", 2, 10, 5)
    with c3:
        pb_target = st.number_input("Payback target (yrs)", min_value=0.0, value=3.0, step=0.5)

    st.markdown("##### Edit the two projects' cash flows (Year 0 = investment, negative)")
    default = pd.DataFrame(
        {
            "Year": list(range(0, n_years + 1)),
            "Project A (€)": [-500_000, 300_000, 250_000, 150_000, 80_000, 40_000][:n_years + 1],
            "Project B (€)": [-500_000, 80_000, 140_000, 220_000, 320_000, 380_000][:n_years + 1],
        }
    )
    edited = st.data_editor(default, use_container_width=True, hide_index=True,
                            num_rows="fixed", key="compare_editor")

    cf_a = edited["Project A (€)"].tolist()
    cf_b = edited["Project B (€)"].tolist()

    npv_a, npv_b = npv(rate, cf_a), npv(rate, cf_b)
    irr_a, irr_b = irr_bisection(cf_a), irr_bisection(cf_b)
    pb_a, pb_b = simple_payback(cf_a), simple_payback(cf_b)
    pi_a = (npv_a + (-cf_a[0])) / (-cf_a[0]) if cf_a[0] < 0 else np.nan
    pi_b = (npv_b + (-cf_b[0])) / (-cf_b[0]) if cf_b[0] < 0 else np.nan

    results = pd.DataFrame(
        {
            "Metric": ["NPV (€)", "IRR (%)", "PI", "Payback (yrs)"],
            "Project A": [
                f"{npv_a:,.0f}",
                f"{irr_a*100:.1f}%" if irr_a is not None else "n/a",
                f"{pi_a:.3f}",
                f"{pb_a:.2f}" if pb_a is not None else "Never",
            ],
            "Project B": [
                f"{npv_b:,.0f}",
                f"{irr_b*100:.1f}%" if irr_b is not None else "n/a",
                f"{pi_b:.3f}",
                f"{pb_b:.2f}" if pb_b is not None else "Never",
            ],
        }
    )
    st.dataframe(results, use_container_width=True, hide_index=True)

    # conflict detection
    npv_pick = "A" if npv_a > npv_b else "B"
    irr_pick = None
    if irr_a is not None and irr_b is not None:
        irr_pick = "A" if irr_a > irr_b else "B"
    conflict = irr_pick is not None and irr_pick != npv_pick

    m1, m2, m3 = st.columns(3)
    m1.metric("NPV favours", f"Project {npv_pick}", f"€{max(npv_a, npv_b):,.0f}")
    m2.metric("IRR favours", f"Project {irr_pick}" if irr_pick else "n/a")
    m3.metric("Conflict?", "Yes ⚠️" if conflict else "No ✅")

    # NPV profiles + crossover
    rates = np.linspace(0, 0.4, 81)
    npvs_a = [npv(rr, cf_a) for rr in rates]
    npvs_b = [npv(rr, cf_b) for rr in rates]
    diff = [a - b for a, b in zip(cf_a, cf_b)]
    crossover = irr_bisection(diff)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rates * 100, y=npvs_a, mode="lines", name="Project A",
                             line=dict(color="#1E88E5", width=3)))
    fig.add_trace(go.Scatter(x=rates * 100, y=npvs_b, mode="lines", name="Project B",
                             line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dot", line_color="grey")
    fig.add_vline(x=rate * 100, line_dash="dash", line_color="#1B7F3B",
                  annotation_text=f"r = {rate*100:.1f}%", annotation_position="top")
    if crossover is not None and 0 < crossover < 0.4:
        fig.add_vline(x=crossover * 100, line_dash="dot", line_color="#F9A825",
                      annotation_text=f"Crossover {crossover*100:.1f}%", annotation_position="bottom")
    fig.update_layout(title="NPV profiles of the two projects",
                      xaxis_title="Discount rate (%)", yaxis_title="NPV (€)",
                      height=440, legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    if conflict:
        st.warning(f"🟠 **NPV–IRR conflict detected.** IRR favours Project {irr_pick}, but NPV favours "
                   f"Project {npv_pick}. This is driven by differences in scale and/or cash-flow timing"
                   + (f" (crossover ≈ {crossover*100:.1f}%)." if crossover else ".") )
    st.success(f"✅ **Recommendation: choose Project {npv_pick}** — the higher NPV (€{max(npv_a, npv_b):,.0f}) "
               f"means it adds the most value at your {rate*100:.1f}% cost of capital. NPV is the tie-breaker.")

    st.caption("Reminder: NPV is the primary rule. Use IRR/PI/payback to communicate and screen, "
               "not to override NPV for mutually exclusive projects.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. The accept rule for the Profitability Index is…",
            "options": ["PI < 1", "PI > 1", "PI = 0", "PI > hurdle rate"],
            "answer": 1,
            "why": "Accept when PI > 1, which is equivalent to a positive NPV.",
        },
        {
            "q": "2. For mutually exclusive projects, when NPV and IRR conflict you should follow…",
            "options": ["IRR", "NPV", "Payback", "ARR"],
            "answer": 1,
            "why": "NPV measures absolute value creation and is the reliable rule when methods disagree.",
        },
        {
            "q": "3. NPV–IRR ranking conflicts are mainly caused by differences in…",
            "options": [
                "Tax rates only",
                "Project scale and cash-flow timing",
                "The number of decimal places",
                "Depreciation method",
            ],
            "answer": 1,
            "why": "Scale (size) and timing differences make IRR and NPV rank mutually exclusive projects differently.",
        },
        {
            "q": "4. The crossover rate is found by…",
            "options": [
                "Averaging the two IRRs",
                "Computing the IRR of the differential (A − B) cash flows",
                "Adding the two NPVs",
                "Taking the higher hurdle rate",
            ],
            "answer": 1,
            "why": "The crossover rate is the IRR of the incremental cash flows between the two projects.",
        },
        {
            "q": "5. Which method does NOT account for the time value of money?",
            "options": ["NPV", "Discounted payback", "Simple payback", "IRR"],
            "answer": 2,
            "why": "Simple payback (and ARR) ignore the time value of money; the discounted methods do not.",
        },
        {
            "q": "6. The best role for the simple payback method is as…",
            "options": [
                "The primary decision rule",
                "A quick liquidity/risk screen alongside NPV",
                "A replacement for NPV",
                "A measure of total value created",
            ],
            "answer": 1,
            "why": "Payback is a fast screening tool for liquidity/risk — not a standalone decision rule.",
        },
    ]

    with st.form("quiz_4_1"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q41_{i}")
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
            st.success("🏆 Perfect! You can now navigate any method conflict with confidence.")
        elif pct >= 60:
            st.info("👍 Strong work — continue to **4.2 · Mutually Exclusive Projects & Capital Rationing**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on the NPV–IRR conflict and the crossover rate.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `3.4 · Real Options & EVA`")
with cnext:
    st.markdown("**Next:** `4.2 · Mutually Exclusive Projects & Capital Rationing` ➡️")
st.caption("Business Case section · Page 4.1 · Built with Streamlit")
