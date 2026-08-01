# ============================================================================
#  BUSINESS CASE — Section
#  Page 2.2 · Internal Rate of Return (IRR & MIRR)
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
    page_title="2.2 · Internal Rate of Return (IRR & MIRR)",
    page_icon="🔄",
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
        <span class="bc-tag">PART 2 · DISCOUNTED (CORE) METHODS</span>
        <h1>2.2 · Internal Rate of Return (IRR &amp; MIRR)</h1>
        <p>The project's own rate of return — the discount rate that makes NPV zero.
        Intuitive as a %, but with traps that the Modified IRR is designed to fix.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Compute and interpret IRR, understand its reinvestment and multiple-IRR "
           "pitfalls, and use MIRR to overcome them.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr_bisection(cashflows, low=-0.9, high=1.0, tol=1e-6, max_iter=200):
    """Robust IRR via bisection on the first sign-change bracket. Returns None if not found."""
    # scan for a sign change across a fine grid
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


def mirr(cashflows, finance_rate, reinvest_rate):
    """Modified IRR. cashflows[0] is Year 0."""
    n = len(cashflows) - 1
    pv_neg = sum(cf / (1 + finance_rate) ** t
                 for t, cf in enumerate(cashflows) if cf < 0)
    fv_pos = sum(cf * (1 + reinvest_rate) ** (n - t)
                 for t, cf in enumerate(cashflows) if cf > 0)
    if pv_neg == 0 or fv_pos <= 0:
        return None
    return (fv_pos / -pv_neg) ** (1 / n) - 1


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
        The <b>Internal Rate of Return (IRR)</b> is the discount rate at which a project's
        <b>NPV equals zero</b>. It represents the project's own <b>effective annual rate of return</b> —
        the break-even cost of capital. If a project's IRR beats the required return, it adds value.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · The Defining Equation")
    st.latex(r"NPV = \sum_{t=0}^{n} \frac{CF_t}{(1 + IRR)^{t}} = 0")
    st.markdown(
        "There's no neat algebraic solution for most projects — IRR is found **iteratively** "
        "(trial and error, interpolation, or a numerical solver), which is exactly what the lab does."
    )

    st.subheader("3 · The Decision Rule")
    st.markdown(
        """
        <div class="bc-card">
        <h4>📏 Accept / Reject</h4>
        <ul>
          <li><span class="good">IRR &gt; required return (hurdle / WACC)</span> → <b>Accept.</b></li>
          <li><span class="bad">IRR &lt; required return</span> → <b>Reject.</b></li>
          <li><b>IRR = hurdle rate</b> → break-even; indifferent.</li>
        </ul>
        For a single conventional project, the IRR and NPV rules <b>always agree</b> on accept/reject.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("4 · IRR and the NPV Profile")
    st.markdown(
        """
        On the **NPV profile** (from page 2.1), the IRR is simply the point where the downward-sloping
        curve **crosses the zero line**. To the left of the IRR, NPV is positive (accept); to the right,
        NPV is negative (reject).
        """
    )

    st.subheader("5 · Linear Interpolation Shortcut")
    st.markdown("A quick manual estimate using one positive and one negative NPV:")
    st.latex(r"IRR \approx r_L + \frac{NPV_L}{NPV_L - NPV_H}\,(r_H - r_L)")
    st.markdown(
        "<span class='muted'>Where $r_L$ gives a positive NPV ($NPV_L$) and $r_H$ a negative one "
        "($NPV_H$). It's an approximation — the true curve is not perfectly linear.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("6 · The Three IRR Traps")
    for t, b in [
        ("🔁 Unrealistic reinvestment assumption",
         "IRR implicitly assumes interim cash flows are reinvested at the IRR itself — often too "
         "optimistic. NPV assumes reinvestment at the cost of capital, which is more realistic."),
        ("🔀 Multiple IRRs",
         "Projects with non-conventional cash flows (sign changes more than once, e.g. a big "
         "clean-up cost at the end) can have several IRRs — or none. NPV has no such problem."),
        ("⚖️ Ranking conflicts",
         "For mutually exclusive projects of different size or timing, IRR can rank them differently "
         "from NPV. When they conflict, <b>trust NPV</b> — it measures value directly."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("7 · MIRR — The Modified IRR Fix")
    st.markdown(
        """
        The **Modified IRR (MIRR)** repairs the two biggest flaws: it assumes interim inflows are
        reinvested at a realistic **reinvestment rate** (usually the cost of capital), and it produces
        a **single, unique** value.
        """
    )
    st.latex(r"MIRR = \left(\frac{FV_{\text{inflows at reinvest rate}}}{-PV_{\text{outflows at finance rate}}}\right)^{\frac{1}{n}} - 1")
    st.markdown(
        """
        - **Discount** all outflows to Year 0 at the *finance rate*.
        - **Compound** all inflows to Year *n* at the *reinvestment rate*.
        - MIRR is the rate linking those two figures over *n* years.
        """
    )

    st.subheader("8 · IRR vs NPV — When They Disagree")
    cmp = pd.DataFrame(
        {
            "Aspect": ["Output", "Reinvestment assumption", "Multiple values possible?",
                       "Ranking mutually exclusive projects", "Best for"],
            "NPV": ["Absolute € value", "Cost of capital (realistic)", "No",
                    "Reliable", "The final decision"],
            "IRR": ["% return", "The IRR itself (often unrealistic)", "Yes (non-conventional flows)",
                    "Can mislead", "Communicating return intuitively"],
        }
    )
    st.table(cmp)

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - IRR = the discount rate where **NPV = 0** — the project's own return.
            - Decision rule: **accept if IRR > hurdle rate**.
            - Traps: unrealistic **reinvestment**, **multiple IRRs**, and **ranking conflicts**.
            - **MIRR** fixes reinvestment & uniqueness by using a separate reinvestment rate.
            - When IRR and NPV disagree, **follow NPV**.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Finding IRR by Interpolation, then MIRR")
    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> A project costs <b>€500,000</b> and returns <b>€160,000</b> per year for
        <b>5 years</b>. The cost of capital is <b>10%</b>. We'll estimate the IRR by interpolation,
        confirm it, then compute the MIRR.
        </div>
        """,
        unsafe_allow_html=True,
    )

    cfs = [-500_000, 160_000, 160_000, 160_000, 160_000, 160_000]

    st.markdown("#### Step 1 · Compute NPV at two trial rates")
    r_low, r_high = 0.15, 0.20
    npv_low, npv_high = npv(r_low, cfs), npv(r_high, cfs)
    trial = pd.DataFrame(
        {"Trial rate": [f"{r_low*100:.0f}%", f"{r_high*100:.0f}%"],
         "NPV (€)": [npv_low, npv_high]}
    )
    st.dataframe(trial.style.format({"NPV (€)": "{:,.0f}"}),
                 use_container_width=True, hide_index=True)

    st.markdown("#### Step 2 · Interpolate")
    irr_interp = r_low + (npv_low / (npv_low - npv_high)) * (r_high - r_low)
    st.latex(rf"IRR \approx {r_low*100:.0f}\% + \frac{{{npv_low:,.0f}}}{{{npv_low:,.0f} - ({npv_high:,.0f})}}"
             rf"\times({r_high*100:.0f}\% - {r_low*100:.0f}\%) = {irr_interp*100:.1f}\%")

    irr_true = irr_bisection(cfs)
    st.success(f"✅ Interpolated IRR ≈ **{irr_interp*100:.1f}%**; precise solver gives "
               f"**{irr_true*100:.2f}%**. Since IRR > 10% cost of capital → **ACCEPT**.")

    st.markdown("#### Step 3 · Compute MIRR (reinvest at 10%)")
    m = mirr(cfs, finance_rate=0.10, reinvest_rate=0.10)
    st.latex(r"MIRR = \left(\frac{FV_{inflows@10\%}}{-PV_{outflow}}\right)^{1/5} - 1")
    st.info(f"With reinvestment at the 10% cost of capital, **MIRR ≈ {m*100:.2f}%** — lower than the "
            f"IRR of {irr_true*100:.2f}%, because IRR over-optimistically assumed reinvestment at "
            f"{irr_true*100:.1f}%. MIRR is the more realistic return.")

    st.markdown("#### The NPV profile — IRR is the zero crossing")
    rates = np.linspace(0, 0.35, 36)
    npvs = [npv(rr, cfs) for rr in rates]
    fig = go.Figure(go.Scatter(x=rates * 100, y=npvs, mode="lines",
                               line=dict(color="#0B3D91", width=3), name="NPV"))
    fig.add_hline(y=0, line_dash="dash", line_color="#C62828")
    fig.add_vline(x=irr_true * 100, line_dash="dot", line_color="#F9A825",
                  annotation_text=f"IRR ≈ {irr_true*100:.1f}%", annotation_position="top")
    fig.add_vline(x=10, line_dash="dot", line_color="#1B7F3B",
                  annotation_text="Hurdle 10%", annotation_position="bottom")
    fig.update_layout(title="NPV profile — IRR crossing",
                      xaxis_title="Discount rate (%)", yaxis_title="NPV (€)",
                      height=420, margin=dict(t=60, b=40))
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ IRR & MIRR Solver")
    st.markdown("Edit the cash flows, set the hurdle and reinvestment rates, and see IRR, MIRR and the "
                "NPV profile update live.")

    c1, c2, c3 = st.columns(3)
    with c1:
        invest = st.number_input("Initial investment (€, Year 0)", min_value=0, value=500_000, step=25_000)
        n_years = st.slider("Number of years", 1, 12, 5)
    with c2:
        hurdle = st.slider("Hurdle rate / WACC (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
        reinvest = st.slider("Reinvestment rate for MIRR (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
    with c3:
        finance = st.slider("Finance rate for MIRR (%)", 0.0, 30.0, 10.0, 0.5) / 100.0

    pattern = st.radio("Inflow pattern", ["Even (constant)", "Uneven (edit table)"], horizontal=True)
    if pattern.startswith("Even"):
        annual = st.number_input("Annual inflow (€)", min_value=0, value=160_000, step=10_000)
        inflows = [annual] * n_years
    else:
        default = pd.DataFrame({"Year": list(range(1, n_years + 1)),
                                "Cash Flow (€)": [140000, 150000, 160000, 170000, 180000][:n_years]
                                + [160000] * max(0, n_years - 5)})
        edited = st.data_editor(default, use_container_width=True, hide_index=True,
                                num_rows="fixed", key="irr_editor")
        inflows = edited["Cash Flow (€)"].tolist()

    cfs = [-invest] + inflows

    irr_val = irr_bisection(cfs)
    mirr_val = mirr(cfs, finance_rate=finance, reinvest_rate=reinvest)
    npv_at_hurdle = npv(hurdle, cfs)

    m1, m2, m3 = st.columns(3)
    m1.metric("IRR", f"{irr_val*100:.2f}%" if irr_val is not None else "No real IRR")
    m2.metric("MIRR", f"{mirr_val*100:.2f}%" if mirr_val is not None else "n/a")
    m3.metric(f"NPV @ {hurdle*100:.1f}%", f"€{npv_at_hurdle:,.0f}")

    rates = np.linspace(0, 0.5, 51)
    npvs = [npv(rr, cfs) for rr in rates]
    fig = go.Figure(go.Scatter(x=rates * 100, y=npvs, mode="lines",
                               line=dict(color="#0B3D91", width=3), name="NPV"))
    fig.add_hline(y=0, line_dash="dash", line_color="#C62828")
    fig.add_vline(x=hurdle * 100, line_dash="dot", line_color="#1B7F3B",
                  annotation_text=f"Hurdle {hurdle*100:.1f}%", annotation_position="bottom")
    if irr_val is not None:
        fig.add_vline(x=irr_val * 100, line_dash="dot", line_color="#F9A825",
                      annotation_text=f"IRR {irr_val*100:.1f}%", annotation_position="top")
    fig.update_layout(title="NPV profile", xaxis_title="Discount rate (%)",
                      yaxis_title="NPV (€)", height=420, margin=dict(t=60, b=40))
    st.plotly_chart(fig, use_container_width=True)

    if irr_val is None:
        st.warning("⚠️ No single real IRR found — the cash flows may be non-conventional "
                   "(multiple sign changes). This is exactly why **MIRR / NPV** are safer here.")
    elif irr_val > hurdle:
        st.success(f"✅ **IRR {irr_val*100:.2f}% > hurdle {hurdle*100:.1f}% → ACCEPT.** "
                   + (f"MIRR is {mirr_val*100:.2f}% (more realistic). " if mirr_val else "")
                   + f"NPV at the hurdle is €{npv_at_hurdle:,.0f}.")
    else:
        st.error(f"❌ **IRR {irr_val*100:.2f}% < hurdle {hurdle*100:.1f}% → REJECT.** "
                 f"NPV at the hurdle is €{npv_at_hurdle:,.0f}.")

    st.caption("Tip: if IRR and NPV ever disagree on ranking, trust NPV — it measures value in €.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. The IRR is defined as the discount rate at which…",
            "options": ["NPV is maximised", "NPV equals zero",
                        "Payback equals the cutoff", "ARR equals the target"],
            "answer": 1,
            "why": "IRR is the rate that makes a project's NPV exactly zero.",
        },
        {
            "q": "2. Under the IRR decision rule, accept a project when…",
            "options": [
                "IRR is below the hurdle rate",
                "IRR equals zero",
                "IRR exceeds the required return / hurdle rate",
                "IRR is negative",
            ],
            "answer": 2,
            "why": "Accept when IRR is greater than the required return (WACC / hurdle rate).",
        },
        {
            "q": "3. A key unrealistic assumption of the standard IRR is that interim cash flows are reinvested at…",
            "options": ["The inflation rate", "The IRR itself",
                        "The risk-free rate", "Zero percent"],
            "answer": 1,
            "why": "IRR assumes reinvestment at the IRR — often too optimistic; NPV/MIRR use the cost of capital.",
        },
        {
            "q": "4. Multiple IRRs can arise when a project has…",
            "options": [
                "Only one sign change in its cash flows",
                "Non-conventional cash flows with more than one sign change",
                "A constant annual inflow",
                "No initial investment",
            ],
            "answer": 1,
            "why": "More than one sign change (e.g. large end-of-life costs) can produce several IRRs.",
        },
        {
            "q": "5. MIRR improves on IRR primarily by…",
            "options": [
                "Ignoring the time value of money",
                "Assuming a realistic reinvestment rate and giving a unique value",
                "Removing the need for cash-flow forecasts",
                "Always producing a higher return",
            ],
            "answer": 1,
            "why": "MIRR reinvests inflows at a realistic rate and yields a single, unique figure.",
        },
        {
            "q": "6. When IRR and NPV rank mutually exclusive projects differently, you should…",
            "options": ["Follow IRR", "Follow NPV",
                        "Follow payback", "Average the two rankings"],
            "answer": 1,
            "why": "NPV measures absolute value creation, so it is the reliable tie-breaker.",
        },
    ]

    with st.form("quiz_2_2"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q22_{i}")
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
            st.success("🏆 Perfect! You've mastered IRR, its traps, and the MIRR fix.")
        elif pct >= 60:
            st.info("👍 Strong work — continue to **2.3 · Discounted Payback Period**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — especially the reinvestment and multiple-IRR traps.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `2.1 · Net Present Value (NPV)`")
with cnext:
    st.markdown("**Next:** `2.3 · Discounted Payback Period` ➡️")
st.caption("Business Case section · Page 2.2 · Built with Streamlit")
