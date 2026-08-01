# ============================================================================
#  BUSINESS CASE — Section
#  Page 1.2 · Accounting Rate of Return (ARR)
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="1.2 · Accounting Rate of Return (ARR)",
    page_icon="📐",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Part 0 / 1.1)
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
        <span class="bc-tag">PART 1 · NON-DISCOUNTED METHODS</span>
        <h1>1.2 · Accounting Rate of Return (ARR)</h1>
        <p>A profit-based percentage return that speaks the language of the P&amp;L —
        easy to compute from accounting figures, but blind to cash and timing.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Compute ARR on both investment bases, apply the decision rule, and "
           "understand why it differs from cash-based methods.")

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
        The <b>Accounting Rate of Return (ARR)</b> — also called Return on Investment (ROI) or
        Return on Capital Employed (ROCE) in this context — expresses the <b>average annual
        accounting profit</b> a project generates as a <b>percentage of the investment</b>.
        Unlike payback, it uses <b>profit</b> (after depreciation), not cash.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · The Formula")
    st.latex(r"ARR = \frac{\text{Average Annual Accounting Profit}}{\text{Investment}} \times 100\%")
    st.markdown(
        "The **average annual profit** is the total profit *after depreciation* over the project's "
        "life, divided by the number of years:"
    )
    st.latex(r"\text{Average Profit} = \frac{\text{Total Profit after Depreciation}}{\text{Number of Years}}")

    st.subheader("3 · Two Investment Bases")
    st.markdown("The denominator can be defined two ways — always state which you use:")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>① Initial Investment</h4>
            <p>Uses the full original cost as the base.</p>
            </div>
            """, unsafe_allow_html=True,
        )
        st.latex(r"ARR = \frac{\text{Avg Profit}}{\text{Initial Investment}}")
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>② Average Investment</h4>
            <p>Assumes the asset depreciates evenly to its residual value.</p>
            </div>
            """, unsafe_allow_html=True,
        )
        st.latex(r"\text{Avg Inv} = \frac{\text{Initial} + \text{Residual}}{2}")
    st.info("👉 The **average investment** base gives a **higher** ARR (smaller denominator). "
            "Be consistent and transparent about which base you use when comparing projects.")

    st.subheader("4 · The Decision Rule")
    st.markdown(
        """
        <div class="bc-card">
        <h4>📏 Accept / Reject</h4>
        <ul>
          <li><span class="good">Accept</span> if ARR is <b>greater than</b> the company's target /
          required accounting rate of return.</li>
          <li><span class="bad">Reject</span> if ARR is <b>below</b> the target.</li>
          <li>For competing projects, prefer the one with the <b>higher</b> ARR.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("5 · Profit vs Cash — the Key Distinction")
    st.markdown(
        """
        ARR uses **accounting profit**, which is *after* deducting depreciation. This is the crucial
        difference from cash-based methods:
        """
    )
    st.latex(r"\text{Accounting Profit} = \text{Net Cash Flow} - \text{Depreciation}")
    st.markdown(
        "<span class='muted'>So if a project earns €160k cash and depreciation is €100k, the "
        "accounting profit used in ARR is €60k — not €160k.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("6 · Strengths & Weaknesses")
    c3, c4 = st.columns(2)
    with c3:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👍 Strengths</h4>
            <ul>
              <li>Simple; uses readily available <b>accounting data</b></li>
              <li>Expressed as a familiar <b>% return</b> managers relate to</li>
              <li>Considers <b>profitability over the whole life</b> (unlike payback)</li>
              <li>Links to performance measures like <b>ROCE</b></li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👎 Weaknesses</h4>
            <ul>
              <li><b>Ignores the time value of money</b></li>
              <li>Based on <b>accounting profit</b>, not cash flow</li>
              <li>Sensitive to <b>depreciation policy</b> choices</li>
              <li>The target rate is often <b>arbitrary</b></li>
              <li>Uses averages — <b>ignores the timing</b> of profits</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - ARR = average annual **profit** ÷ investment, as a %.
            - Profit is **after depreciation** — not cash flow.
            - Two bases: **initial** vs **average** investment (average → higher ARR).
            - Decision rule: accept if **ARR > target**; higher is better.
            - Blind spots: **ignores TVM**, depends on **depreciation policy**, uses **averages**.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Computing ARR on Both Bases")
    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> A machine costs <b>€500,000</b> with a <b>€50,000</b> residual value and a
        <b>5-year</b> life. It generates annual <b>net cash flows</b> of €160,000. Depreciation is
        straight-line. The company's target ARR is <b>15%</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    initial = 500_000
    residual = 50_000
    life = 5
    annual_cash = 160_000

    dep = (initial - residual) / life
    annual_profit = annual_cash - dep
    avg_investment = (initial + residual) / 2

    st.markdown("#### Step 1 · Depreciation & annual profit")
    st.latex(rf"\text{{Depreciation}} = \frac{{500{{,}}000 - 50{{,}}000}}{{5}} = €{dep:,.0f}\ \text{{/yr}}")
    st.latex(rf"\text{{Annual Profit}} = 160{{,}}000 - {dep:,.0f} = €{annual_profit:,.0f}")

    st.markdown("#### Step 2 · Apply both bases")
    arr_initial = annual_profit / initial
    arr_average = annual_profit / avg_investment

    tbl = pd.DataFrame(
        {
            "Basis": ["Initial investment", "Average investment"],
            "Denominator (€)": [initial, avg_investment],
            "ARR (%)": [arr_initial * 100, arr_average * 100],
        }
    )
    st.dataframe(
        tbl.style.format({"Denominator (€)": "{:,.0f}", "ARR (%)": "{:.1f}%"}),
        use_container_width=True, hide_index=True,
    )

    st.latex(rf"ARR_{{initial}} = \frac{{{annual_profit:,.0f}}}{{500{{,}}000}} = {arr_initial*100:.1f}\%")
    st.latex(rf"ARR_{{average}} = \frac{{{annual_profit:,.0f}}}{{{avg_investment:,.0f}}} = {arr_average*100:.1f}\%")

    st.markdown("#### Step 3 · Decision")
    if arr_average >= 0.15:
        st.success(f"On the **average-investment** basis ARR = **{arr_average*100:.1f}%** ≥ 15% target "
                   f"→ **ACCEPT** ✅. On the initial basis it is {arr_initial*100:.1f}%. Always state "
                   f"which basis you're using!")
    else:
        st.warning(f"ARR is {arr_average*100:.1f}% (average) / {arr_initial*100:.1f}% (initial) vs a "
                   f"15% target — the decision depends on the basis chosen.")

    fig = go.Figure(go.Bar(
        x=["Initial basis", "Average basis"],
        y=[arr_initial * 100, arr_average * 100],
        marker_color=["#90CAF9", "#1565C0"],
        text=[f"{arr_initial*100:.1f}%", f"{arr_average*100:.1f}%"], textposition="outside",
    ))
    fig.add_hline(y=15, line_dash="dash", line_color="#C62828",
                  annotation_text="Target 15%", annotation_position="top left")
    fig.update_layout(title="ARR by investment basis vs target",
                      yaxis_title="ARR (%)", height=400, margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.info("⚠️ Notice ARR uses **profit of €" + f"{annual_profit:,.0f}" +
            "**, not the €160,000 cash. Depreciation policy directly changes the answer — a cash "
            "method like NPV would not be affected this way.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ ARR Calculator")
    st.markdown("Set the investment and profit drivers, choose your basis, and compare ARR against "
                "your target.")

    c1, c2, c3 = st.columns(3)
    with c1:
        initial = st.number_input("Initial investment (€)", min_value=0, value=500_000, step=25_000)
        residual = st.number_input("Residual / salvage value (€)", min_value=0, value=50_000, step=10_000)
    with c2:
        life = st.slider("Project life (years)", 1, 15, 5)
        target = st.slider("Target ARR (%)", 0.0, 40.0, 15.0, 0.5)
    with c3:
        profit_mode = st.radio("Profit input", ["Enter annual cash flow", "Enter annual profit directly"])

    if profit_mode.startswith("Enter annual cash"):
        annual_cash = st.number_input("Annual net cash flow (€)", min_value=0, value=160_000, step=10_000)
        dep = (initial - residual) / life if life else 0
        annual_profit = annual_cash - dep
        st.caption(f"Straight-line depreciation = €{dep:,.0f}/yr → annual profit = €{annual_profit:,.0f}")
    else:
        annual_profit = st.number_input("Average annual accounting profit (€)",
                                        min_value=-10_000_000, value=70_000, step=5_000)
        dep = (initial - residual) / life if life else 0

    avg_investment = (initial + residual) / 2
    arr_initial = (annual_profit / initial) if initial else 0
    arr_average = (annual_profit / avg_investment) if avg_investment else 0

    basis = st.radio("Reporting basis for the decision",
                     ["Average investment", "Initial investment"], horizontal=True)
    arr_used = arr_average if basis.startswith("Average") else arr_initial

    m1, m2, m3 = st.columns(3)
    m1.metric("ARR (initial basis)", f"{arr_initial*100:.1f}%")
    m2.metric("ARR (average basis)", f"{arr_average*100:.1f}%")
    m3.metric("Annual profit used", f"€{annual_profit:,.0f}")

    fig = go.Figure(go.Bar(
        x=["Initial basis", "Average basis"],
        y=[arr_initial * 100, arr_average * 100],
        marker_color=["#90CAF9", "#1565C0"],
        text=[f"{arr_initial*100:.1f}%", f"{arr_average*100:.1f}%"], textposition="outside",
    ))
    fig.add_hline(y=target, line_dash="dash", line_color="#C62828",
                  annotation_text=f"Target {target:.1f}%", annotation_position="top left")
    fig.update_layout(title="ARR vs target", yaxis_title="ARR (%)", height=400, margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    if arr_used * 100 >= target:
        st.success(f"✅ ARR on the **{basis.lower()}** = **{arr_used*100:.1f}%** ≥ target {target:.1f}% "
                   f"→ **ACCEPT**.")
    else:
        st.warning(f"🟠 ARR on the **{basis.lower()}** = **{arr_used*100:.1f}%** < target {target:.1f}% "
                   f"→ **REJECT** on this measure.")

    st.caption("Reminder: ARR uses accounting profit and ignores the time value of money. "
               "Confirm with NPV/IRR (Part 2) before deciding.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 5 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. ARR expresses a project's return as…",
            "options": [
                "Average annual profit as a % of investment",
                "Total cash inflow divided by years",
                "The discount rate that sets NPV to zero",
                "The time to recover the initial outlay",
            ],
            "answer": 0,
            "why": "ARR = average annual accounting profit ÷ investment, expressed as a percentage.",
        },
        {
            "q": "2. ARR is based on accounting profit, which is…",
            "options": [
                "Net cash flow before depreciation",
                "Net cash flow after deducting depreciation",
                "Only the salvage value",
                "The same as free cash flow",
            ],
            "answer": 1,
            "why": "Accounting profit is net cash flow minus depreciation — that's why ARR differs from cash methods.",
        },
        {
            "q": "3. The average investment base is calculated as…",
            "options": [
                "Initial investment ÷ life",
                "(Initial + Residual) ÷ 2",
                "Initial − Residual",
                "Initial × 2",
            ],
            "answer": 1,
            "why": "Average investment = (Initial cost + Residual value) ÷ 2, assuming even depreciation.",
        },
        {
            "q": "4. Compared with the initial-investment base, the average-investment base gives an ARR that is…",
            "options": ["Lower", "Higher", "Exactly the same", "Always negative"],
            "answer": 1,
            "why": "The average base is a smaller denominator, so it produces a higher ARR percentage.",
        },
        {
            "q": "5. A key weakness of ARR shared with payback is that it…",
            "options": [
                "Requires a discount rate",
                "Ignores the time value of money",
                "Cannot be computed from accounts",
                "Always understates returns",
            ],
            "answer": 1,
            "why": "Like payback, ARR ignores the time value of money — a core limitation of non-discounted methods.",
        },
    ]

    with st.form("quiz_1_2"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q12_{i}")
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
            st.success("🏆 Perfect! You've mastered ARR — and completed Part 1.")
        elif pct >= 60:
            st.info("👍 Good work — now move on to Part 2, starting with **2.1 · Net Present Value (NPV)**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — especially profit vs cash and the two bases.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `1.1 · Payback Period`")
with cnext:
    st.markdown("**Next:** `2.1 · Net Present Value (NPV)` ➡️")
st.caption("Business Case section · Page 1.2 · Built with Streamlit")
