# ============================================================================
#  BUSINESS CASE — Section
#  Page 0.3 · Time Value of Money & Discount Rate
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="0.3 · Time Value of Money & Discount Rate",
    page_icon="⏳",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with 0.1 / 0.2)
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
        <span class="bc-tag">PART 0 · FOUNDATIONS</span>
        <h1>0.3 · Time Value of Money &amp; Discount Rate</h1>
        <p>Why €1 today is worth more than €1 tomorrow — and how to choose the rate
        that converts every future cash flow into today's money.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Master present & future value, discount factors, and how to build a "
           "WACC / hurdle rate — the engine behind NPV, IRR and every discounted method.")

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
    st.subheader("1 · The Core Idea")
    st.markdown(
        """
        <div class="bc-key">
        The <b>Time Value of Money (TVM)</b> says a euro received <b>today</b> is worth more than a
        euro received in the future — because today's euro can be <b>invested to earn a return</b>,
        it carries <b>less risk</b>, and it isn't eroded by <b>inflation</b>. Every discounted
        business-case method rests on this single principle.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · Future Value — Compounding Forward")
    st.markdown("Grow a present amount forward at rate *r* for *n* periods:")
    st.latex(r"FV = PV \times (1 + r)^{n}")
    st.markdown(
        "<span class='muted'>Example: €1,000 at 10% for 3 years → €1,000 × 1.1³ = "
        "<b>€1,331</b>.</span>", unsafe_allow_html=True,
    )

    st.subheader("3 · Present Value — Discounting Back")
    st.markdown("Bring a future amount back to today — the operation we use constantly in a business case:")
    st.latex(r"PV = \frac{FV}{(1 + r)^{n}}")
    st.markdown(
        "<span class='muted'>Example: €1,331 in 3 years at 10% → €1,331 ÷ 1.1³ = "
        "<b>€1,000</b>. Discounting is simply compounding in reverse.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("4 · The Discount Factor")
    st.markdown("The multiplier that converts any future €1 into today's value:")
    st.latex(r"DF_n = \frac{1}{(1 + r)^{n}}")
    st.markdown(
        "Multiply each year's cash flow by its discount factor to get its present value. "
        "The **sum** of discounted cash flows is the foundation of **NPV**."
    )

    st.subheader("5 · Present Value of an Annuity")
    st.markdown("For a *constant* cash flow *C* each year for *n* years:")
    st.latex(r"PV_{\text{annuity}} = C \times \frac{1 - (1 + r)^{-n}}{r}")
    st.markdown("And for a **perpetuity** (a level cash flow forever):")
    st.latex(r"PV_{\text{perpetuity}} = \frac{C}{r}")

    st.subheader("6 · Choosing the Discount Rate")
    st.markdown(
        "The discount rate reflects the **opportunity cost of capital** and the project's **risk**. "
        "Three common reference points:"
    )
    rate_cards = [
        ("💼 Cost of Capital (WACC)",
         "The blended after-tax cost of the firm's debt and equity — the default rate for "
         "average-risk projects."),
        ("🎯 Hurdle Rate",
         "The minimum return management demands. Often set at or above WACC, sometimes with a "
         "risk premium added for uncertain projects."),
        ("⚖️ Risk-Adjusted Rate",
         "WACC plus (or minus) a premium reflecting how the project's risk differs from the "
         "company's average."),
    ]
    for t, b in rate_cards:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("7 · WACC — Weighted Average Cost of Capital")
    st.latex(r"WACC = \frac{E}{V}\,r_e \; + \; \frac{D}{V}\,r_d\,(1 - t)")
    st.markdown(
        """
        Where:
        - $E$ = market value of **equity**, $D$ = market value of **debt**, $V = E + D$
        - $r_e$ = cost of **equity** (often from CAPM: $r_e = r_f + \\beta (r_m - r_f)$)
        - $r_d$ = cost of **debt**, and $t$ = tax rate (debt interest is tax-deductible → the $(1-t)$ shield)
        """
    )

    st.subheader("8 · Why the Rate Matters So Much")
    st.markdown(
        """
        - A **higher** discount rate → future cash flows shrink faster → **lower** NPV → harder to justify.
        - A **lower** rate flatters long-dated projects and can make weak ideas look attractive.
        - Small changes in *r* can flip a decision — which is why we **sensitivity-test** it (Part 3).
        """
    )

    with st.expander("🔑 Quick reference — TVM formulas"):
        st.markdown(
            """
            | Concept | Formula |
            |---------|---------|
            | Future value | $FV = PV(1+r)^n$ |
            | Present value | $PV = FV / (1+r)^n$ |
            | Discount factor | $DF = 1/(1+r)^n$ |
            | PV of annuity | $C \\times [1-(1+r)^{-n}]/r$ |
            | PV of perpetuity | $C / r$ |
            | WACC | $(E/V)r_e + (D/V)r_d(1-t)$ |
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Discounting a Stream of Cash Flows")

    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> A project returns <b>€160,000</b> per year for <b>5 years</b>. The company's
        discount rate is <b>10%</b>. What are these future cash flows worth <b>today</b>? We'll build
        the discount factors and present values year by year.
        </div>
        """,
        unsafe_allow_html=True,
    )

    r = 0.10
    cash = 160_000
    years = [1, 2, 3, 4, 5]
    dfs = [1 / (1 + r) ** n for n in years]
    pvs = [cash * d for d in dfs]
    total_pv = sum(pvs)

    df = pd.DataFrame(
        {
            "Year": years,
            "Cash Flow (€)": [cash] * 5,
            "Discount Factor @10%": [round(d, 4) for d in dfs],
            "Present Value (€)": pvs,
        }
    )
    st.dataframe(
        df.style.format({"Cash Flow (€)": "{:,.0f}", "Present Value (€)": "{:,.0f}",
                         "Discount Factor @10%": "{:.4f}"}),
        use_container_width=True, hide_index=True,
    )

    st.latex(rf"PV_{{total}} = \sum_{{n=1}}^{{5}} \frac{{160{{,}}000}}{{(1.10)^n}} = €{total_pv:,.0f}")

    st.markdown(
        f"""
        - **Undiscounted** total = €{cash*5:,.0f}
        - **Discounted** total (present value) = **€{total_pv:,.0f}**
        - The **€{cash*5-total_pv:,.0f}** difference is the *time value* lost by waiting.
        """
    )

    # Cross-check with the annuity formula
    annuity_pv = cash * (1 - (1 + r) ** (-5)) / r
    st.info(f"✅ Cross-check with the **annuity formula**: "
            f"160,000 × [1 − 1.10⁻⁵] / 0.10 = **€{annuity_pv:,.0f}** — matches the year-by-year sum.")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=[cash] * 5, name="Nominal cash flow",
                         marker_color="#BBD3F2"))
    fig.add_trace(go.Bar(x=years, y=pvs, name="Present value",
                         marker_color="#1565C0"))
    fig.update_layout(title="Nominal vs discounted cash flows @10%",
                      barmode="overlay", xaxis_title="Year", yaxis_title="€",
                      height=420, legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    fig.update_traces(opacity=0.85)
    st.plotly_chart(fig, use_container_width=True)

    st.success("Notice how each later year's bar shrinks — the further out the cash flow, the less "
               "it's worth today. This is exactly the mechanism behind **NPV** in Part 2.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Lab A · PV / FV Calculator")
    st.markdown("Explore how a single cash flow moves through time.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        mode = st.radio("Calculate", ["Present Value (discount)", "Future Value (compound)"])
    with c2:
        amount = st.number_input("Amount (€)", min_value=0.0, value=100000.0, step=5000.0)
    with c3:
        rate = st.slider("Rate r (%)", 0.0, 25.0, 10.0, 0.5) / 100.0
    with c4:
        periods = st.slider("Periods n (years)", 1, 30, 5)

    if mode.startswith("Present"):
        result = amount / (1 + rate) ** periods
        st.metric(f"PV of €{amount:,.0f} received in {periods} yrs @ {rate*100:.1f}%",
                  f"€{result:,.0f}")
        st.latex(rf"PV = \frac{{{amount:,.0f}}}{{(1+{rate:.3f})^{{{periods}}}}} = €{result:,.0f}")
    else:
        result = amount * (1 + rate) ** periods
        st.metric(f"FV of €{amount:,.0f} in {periods} yrs @ {rate*100:.1f}%", f"€{result:,.0f}")
        st.latex(rf"FV = {amount:,.0f}\times(1+{rate:.3f})^{{{periods}}} = €{result:,.0f}")

    # growth/decay curve
    xs = list(range(0, periods + 1))
    if mode.startswith("Present"):
        ys = [amount / (1 + rate) ** n for n in xs]
        title = "How today's value of a fixed future amount falls with time"
    else:
        ys = [amount * (1 + rate) ** n for n in xs]
        title = "How a present amount grows with compounding"
    figa = go.Figure(go.Scatter(x=xs, y=ys, mode="lines+markers",
                                line=dict(color="#0B3D91", width=3)))
    figa.update_layout(title=title, xaxis_title="Years", yaxis_title="€", height=360,
                       margin=dict(t=60, b=40))
    st.plotly_chart(figa, use_container_width=True)

    st.markdown("---")
    st.subheader("🎛️ Lab B · Discount a Cash-Flow Stream")
    st.markdown("Enter/edit yearly cash flows and a rate to see each present value and the total PV.")

    cc1, cc2 = st.columns([1, 3])
    with cc1:
        disc = st.slider("Discount rate (%)", 0.0, 25.0, 10.0, 0.5, key="stream_rate") / 100.0
        n_years = st.slider("Number of years", 1, 10, 5, key="stream_years")
    default = pd.DataFrame({"Year": list(range(1, n_years + 1)),
                            "Cash Flow (€)": [160000] * n_years})
    with cc2:
        edited = st.data_editor(default, use_container_width=True, hide_index=True,
                                num_rows="fixed", key="stream_editor")

    edited = edited.copy()
    edited["Discount Factor"] = edited["Year"].apply(lambda n: 1 / (1 + disc) ** n)
    edited["Present Value (€)"] = edited["Cash Flow (€)"] * edited["Discount Factor"]
    total_pv = edited["Present Value (€)"].sum()
    total_nominal = edited["Cash Flow (€)"].sum()

    st.dataframe(
        edited.style.format({"Cash Flow (€)": "{:,.0f}", "Discount Factor": "{:.4f}",
                             "Present Value (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )
    m1, m2, m3 = st.columns(3)
    m1.metric("Nominal total", f"€{total_nominal:,.0f}")
    m2.metric("Present value (total)", f"€{total_pv:,.0f}")
    m3.metric("Time value lost", f"€{total_nominal-total_pv:,.0f}")

    st.markdown("---")
    st.subheader("🎛️ Lab C · Build a WACC")
    st.markdown("Set your capital structure and costs to compute a weighted average cost of capital.")

    w1, w2, w3 = st.columns(3)
    with w1:
        equity = st.number_input("Equity value E (€m)", min_value=0.0, value=70.0, step=5.0)
        debt = st.number_input("Debt value D (€m)", min_value=0.0, value=30.0, step=5.0)
    with w2:
        re = st.slider("Cost of equity rₑ (%)", 0.0, 30.0, 12.0, 0.5) / 100.0
        rd = st.slider("Cost of debt r_d (%)", 0.0, 20.0, 6.0, 0.5) / 100.0
    with w3:
        tax = st.slider("Tax rate t (%)", 0.0, 50.0, 30.0, 1.0) / 100.0

    V = equity + debt
    if V > 0:
        we, wd = equity / V, debt / V
        wacc = we * re + wd * rd * (1 - tax)
        st.latex(rf"WACC = {we:.2f}\times{re*100:.1f}\% + {wd:.2f}\times{rd*100:.1f}\%\times(1-{tax:.2f})"
                 rf" = {wacc*100:.2f}\%")
        k1, k2, k3 = st.columns(3)
        k1.metric("Equity weight E/V", f"{we*100:.1f}%")
        k2.metric("Debt weight D/V", f"{wd*100:.1f}%")
        k3.metric("WACC (use as discount rate)", f"{wacc*100:.2f}%")

        figw = go.Figure(go.Pie(labels=["Equity", "Debt"], values=[equity, debt],
                                marker=dict(colors=["#1565C0", "#90CAF9"]), hole=0.5))
        figw.update_layout(title="Capital structure", height=320, margin=dict(t=50, b=20))
        st.plotly_chart(figw, use_container_width=True)
        st.success(f"👉 Use **{wacc*100:.2f}%** as the discount rate for an average-risk project. "
                   f"Add a premium for riskier ones.")
    else:
        st.warning("Enter a non-zero capital structure to compute WACC.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. The time value of money says that €1 today is…",
            "options": ["Worth less than €1 next year", "Worth the same as €1 next year",
                        "Worth more than €1 next year", "Irrelevant to investment decisions"],
            "answer": 2,
            "why": "Today's euro can be invested to earn a return, carries less risk, and avoids inflation — so it's worth more.",
        },
        {
            "q": "2. Which formula gives the present value of a future amount?",
            "options": ["PV = FV × (1+r)ⁿ", "PV = FV / (1+r)ⁿ",
                        "PV = FV × r × n", "PV = FV / (r × n)"],
            "answer": 1,
            "why": "Discounting divides the future value by (1+r)ⁿ to bring it back to today.",
        },
        {
            "q": "3. As the discount rate increases, the present value of a future cash flow…",
            "options": ["Increases", "Decreases", "Stays the same", "Becomes negative"],
            "answer": 1,
            "why": "A higher rate discounts future cash more heavily, so its present value falls.",
        },
        {
            "q": "4. In the WACC formula, why is the cost of debt multiplied by (1 − t)?",
            "options": [
                "Because debt is riskier than equity",
                "Because interest is tax-deductible, creating a tax shield",
                "Because debt has no cost",
                "To convert it to a monthly rate",
            ],
            "answer": 1,
            "why": "Interest is tax-deductible, so the effective (after-tax) cost of debt is r_d × (1 − t).",
        },
        {
            "q": "5. The discount factor for year n at rate r is…",
            "options": ["(1+r)ⁿ", "1 / (1+r)ⁿ", "r × n", "1 + r×n"],
            "answer": 1,
            "why": "The discount factor is 1/(1+r)ⁿ — multiply a cash flow by it to get its present value.",
        },
        {
            "q": "6. A hurdle rate is best described as…",
            "options": [
                "The maximum return a project can earn",
                "The minimum acceptable return for a project to be approved",
                "The rate of inflation",
                "The company's revenue growth rate",
            ],
            "answer": 1,
            "why": "The hurdle rate is the minimum return management requires — often set at or above WACC.",
        },
    ]

    with st.form("quiz_0_3"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q03_{i}")
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
            st.success("🏆 Outstanding! You've mastered the engine behind every discounted method.")
        elif pct >= 60:
            st.info("👍 Nice work — review the misses, then move on to Part 1 & 2 where we apply "
                    "discounting in **NPV, IRR and PI**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — discounting is the heart of the whole section.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `0.2 · Cash Flows: Inflows & Outflows`")
with cnext:
    st.markdown("**Next:** `1.1 · Payback Period` ➡️")
st.caption("Business Case section · Page 0.3 · Built with Streamlit")
