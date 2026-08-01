# ============================================================================
#  BUSINESS CASE — Section
#  Page 3.4 · Real Options & EVA
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
    page_title="3.4 · Real Options & EVA",
    page_icon="🌱",
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
        <span class="bc-tag">PART 3 · ADVANCED EVALUATION &amp; RISK</span>
        <h1>3.4 · Real Options &amp; EVA</h1>
        <p>Two ideas static NPV misses — the value of <b>managerial flexibility</b>
        (options to expand, defer or abandon) and <b>Economic Value Added</b>, the true
        economic profit after charging for capital.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Understand why flexibility has value beyond NPV, value simple real "
           "options, and compute EVA as a capital-charged measure of economic profit.")

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
    st.subheader("PART A · Real Options")
    st.markdown(
        """
        <div class="bc-key">
        <b>Real options</b> apply financial-option thinking to real investments. Standard NPV assumes
        a project is a <b>now-or-never, fixed</b> commitment. In reality, managers can <b>react</b> to
        how the future unfolds — expanding a winner, deferring until uncertainty clears, or abandoning
        a loser. That <b>flexibility has value</b> that static NPV ignores.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("1 · The Core Insight")
    st.latex(r"\text{Expanded (strategic) NPV} = \text{Static NPV} + \text{Value of Options}")
    st.markdown(
        "A project with a slightly negative static NPV can still be worth doing if it creates valuable "
        "**options** (e.g. a foothold in a new market you could later scale up)."
    )

    st.subheader("2 · The Main Types of Real Option")
    for t, b in [
        ("📈 Option to Expand (Growth)",
         "The right to scale up if things go well — like a call option. Common in phased rollouts, "
         "pilot plants, and new-market entries."),
        ("⏸️ Option to Defer (Timing)",
         "The right to wait before committing, letting uncertainty (price, demand, regulation) resolve "
         "before you invest."),
        ("🛑 Option to Abandon",
         "The right to exit and recover salvage value if the project underperforms — like a put option. "
         "It limits the downside."),
        ("🔀 Option to Switch",
         "Flexibility to change inputs, outputs, or processes (e.g. dual-fuel equipment, flexible "
         "production lines)."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("3 · What Drives Option Value?")
    st.markdown(
        """
        - **Uncertainty** — more uncertainty means *more* option value (flexibility is worth more when
          the future is unclear). This is the opposite of how uncertainty affects a fixed NPV.
        - **Time** — the longer you can wait/react, the more valuable the option.
        - **Irreversibility** — the more sunk and irreversible the cost, the more valuable the ability
          to defer or abandon.
        """
    )
    st.info("👉 Key mindset shift: in a real-options world, **uncertainty can be an asset**, not just "
            "a threat — provided you have the flexibility to respond to it.")

    st.subheader("4 · A Simple Decision-Tree Valuation")
    st.markdown(
        """
        You don't always need Black-Scholes. Many real options can be valued with a **decision tree**:
        map the possible future states, their probabilities, and the *optimal action* in each state,
        then take the probability-weighted, discounted value. The lab does exactly this for an
        **abandonment option**.
        """
    )

    st.markdown("---")
    st.subheader("PART B · Economic Value Added (EVA)")
    st.markdown(
        """
        <div class="bc-key">
        <b>Economic Value Added (EVA)</b> measures the <b>true economic profit</b> a business or project
        generates <i>after</i> charging for the cost of <b>all</b> capital employed — both debt and
        equity. Accounting profit ignores the cost of equity; EVA does not.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("5 · The EVA Formula")
    st.latex(r"EVA = NOPAT - (\text{Capital Employed} \times WACC)")
    st.markdown(
        """
        Where:
        - **NOPAT** = Net Operating Profit After Tax = $EBIT \\times (1 - t)$
        - **Capital Employed** = the invested capital (debt + equity) tied up in the business/project
        - **WACC** = the weighted average cost of capital (the capital charge rate — see page 0.3)
        """
    )
    st.markdown("An equivalent, insight-rich form:")
    st.latex(r"EVA = (ROIC - WACC) \times \text{Capital Employed}")
    st.markdown(
        "<span class='muted'>Where ROIC = NOPAT ÷ Capital Employed. This shows EVA is positive only "
        "when the return on invested capital <b>beats</b> the cost of that capital.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("6 · The Decision Rule & Link to NPV")
    st.markdown(
        """
        <div class="bc-card">
        <h4>📏 Interpretation</h4>
        <ul>
          <li><span class="good">EVA &gt; 0</span> → the business/project earns more than its cost of
          capital and <b>creates value</b>.</li>
          <li><span class="bad">EVA &lt; 0</span> → it earns less than the capital charge and
          <b>destroys value</b>, even if accounting profit is positive.</li>
        </ul>
        <span class="muted">The present value of a project's future EVAs equals its NPV — EVA is NPV
        expressed as an annual, performance-manageable figure.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("7 · Why EVA Matters in a Business Case")
    st.markdown(
        """
        - Turns "did we beat the cost of capital?" into a **single annual number**
        - Great for **performance management** and **incentive** design (managers charged for capital)
        - Discourages **empire-building** — growth only helps if ROIC > WACC
        - Complements NPV: NPV for the go/no-go decision, EVA for **tracking value delivery** afterwards
        """
    )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - **Real options** capture the value of *flexibility* that static NPV ignores:
              Expanded NPV = Static NPV + Option value.
            - Option types: **expand, defer, abandon, switch**; value rises with **uncertainty**.
            - **EVA = NOPAT − (Capital × WACC)** = economic profit after a capital charge.
            - EVA > 0 means **ROIC > WACC** → value created; the PV of future EVAs equals NPV.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Example A · Valuing an Abandonment Option")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> A project's future value is uncertain. After Year 1 it will be either a
        <b>success</b> (PV of remaining cash flows = <b>€1,200,000</b>, 60% likely) or a
        <b>failure</b> (PV = <b>€300,000</b>, 40% likely). If it fails, you can <b>abandon</b> and
        recover a salvage value of <b>€500,000</b>. Discount rate 10%. What is the abandonment option worth?
        </div>
        """,
        unsafe_allow_html=True,
    )

    p_success, p_fail = 0.60, 0.40
    v_success, v_fail = 1_200_000, 300_000
    salvage = 500_000
    r = 0.10

    # Without option: you're stuck with the outcome
    ev_no_option = p_success * v_success + p_fail * v_fail
    # With option: in the failure state you take max(continue, abandon)
    fail_value_with_option = max(v_fail, salvage)
    ev_with_option = p_success * v_success + p_fail * fail_value_with_option

    pv_no_option = ev_no_option / (1 + r)
    pv_with_option = ev_with_option / (1 + r)
    option_value = pv_with_option - pv_no_option

    tbl = pd.DataFrame(
        {
            "State": ["Success (60%)", "Failure (40%)"],
            "Continue value (€)": [v_success, v_fail],
            "Abandon (salvage) (€)": ["—", salvage],
            "Optimal action": ["Continue", "Abandon" if salvage > v_fail else "Continue"],
            "Value taken (€)": [v_success, fail_value_with_option],
        }
    )
    st.dataframe(
        tbl.style.format({"Continue value (€)": "{:,.0f}", "Value taken (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("PV without option", f"€{pv_no_option:,.0f}")
    m2.metric("PV with abandon option", f"€{pv_with_option:,.0f}")
    m3.metric("Value of the option", f"€{option_value:,.0f}")

    st.latex(rf"\text{{Option value}} = \frac{{0.6(1{{,}}200{{,}}000) + 0.4({fail_value_with_option:,.0f})}}{{1.10}}"
             rf" - \frac{{0.6(1{{,}}200{{,}}000) + 0.4(300{{,}}000)}}{{1.10}} = €{option_value:,.0f}")

    st.success(f"✅ The ability to abandon and recover €{salvage:,.0f} instead of being stuck with the "
               f"€{v_fail:,.0f} failure value is worth **€{option_value:,.0f}** in present-value terms. "
               f"This flexibility should be *added* to the static NPV.")

    fig = go.Figure(go.Bar(
        x=["PV without option", "PV with abandon option"],
        y=[pv_no_option, pv_with_option],
        marker_color=["#90CAF9", "#1565C0"],
        text=[f"€{pv_no_option:,.0f}", f"€{pv_with_option:,.0f}"], textposition="outside",
    ))
    fig.update_layout(title="Value added by the abandonment option",
                      yaxis_title="Present value (€)", height=400, margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("🧮 Example B · Computing EVA")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> A business unit generates <b>EBIT of €500,000</b>, pays tax at <b>30%</b>, and
        employs <b>€2,500,000</b> of capital at a <b>WACC of 10%</b>. Is it creating economic value?
        </div>
        """,
        unsafe_allow_html=True,
    )

    ebit = 500_000
    tax_rate = 0.30
    capital = 2_500_000
    wacc = 0.10

    nopat = ebit * (1 - tax_rate)
    capital_charge = capital * wacc
    eva = nopat - capital_charge
    roic = nopat / capital

    st.latex(rf"NOPAT = 500{{,}}000 \times (1 - 0.30) = €{nopat:,.0f}")
    st.latex(rf"\text{{Capital charge}} = 2{{,}}500{{,}}000 \times 0.10 = €{capital_charge:,.0f}")
    st.latex(rf"EVA = {nopat:,.0f} - {capital_charge:,.0f} = €{eva:,.0f}")

    m1, m2, m3 = st.columns(3)
    m1.metric("NOPAT", f"€{nopat:,.0f}")
    m2.metric("Capital charge", f"€{capital_charge:,.0f}")
    m3.metric("EVA", f"€{eva:,.0f}", f"ROIC {roic*100:.1f}% vs WACC {wacc*100:.1f}%")

    if eva > 0:
        st.success(f"✅ **EVA = €{eva:,.0f} > 0.** With ROIC of {roic*100:.1f}% beating the "
                   f"{wacc*100:.1f}% WACC, the unit creates economic value — even after fully charging "
                   f"for the capital it uses.")
    else:
        st.error(f"❌ **EVA = €{eva:,.0f} < 0.** Despite a positive accounting profit, ROIC "
                 f"({roic*100:.1f}%) is below the {wacc*100:.1f}% cost of capital — value is destroyed.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Lab A · Abandonment Option Valuer")
    st.markdown("Model a two-state future and see how much the option to abandon (and recover salvage) "
                "is worth.")

    c1, c2, c3 = st.columns(3)
    with c1:
        p_success = st.slider("Probability of success (%)", 0, 100, 60) / 100.0
        r = st.slider("Discount rate (%)", 0.0, 25.0, 10.0, 0.5) / 100.0
    with c2:
        v_success = st.number_input("Success continue value (€)", min_value=0, value=1_200_000, step=50_000)
        v_fail = st.number_input("Failure continue value (€)", min_value=0, value=300_000, step=25_000)
    with c3:
        salvage = st.number_input("Salvage if abandoned (€)", min_value=0, value=500_000, step=25_000)

    p_fail = 1 - p_success
    ev_no_option = p_success * v_success + p_fail * v_fail
    fail_value = max(v_fail, salvage)
    ev_with_option = p_success * v_success + p_fail * fail_value
    pv_no = ev_no_option / (1 + r)
    pv_with = ev_with_option / (1 + r)
    option_value = pv_with - pv_no

    m1, m2, m3 = st.columns(3)
    m1.metric("PV without option", f"€{pv_no:,.0f}")
    m2.metric("PV with option", f"€{pv_with:,.0f}")
    m3.metric("Option value", f"€{option_value:,.0f}")

    fig = go.Figure(go.Bar(
        x=["Without option", "With abandon option"], y=[pv_no, pv_with],
        marker_color=["#90CAF9", "#1565C0"],
        text=[f"€{pv_no:,.0f}", f"€{pv_with:,.0f}"], textposition="outside",
    ))
    fig.update_layout(title="Abandonment option value", yaxis_title="PV (€)",
                      height=380, margin=dict(t=60, b=40))
    st.plotly_chart(fig, use_container_width=True)

    if salvage > v_fail:
        st.success(f"✅ In the failure state you'd abandon (salvage €{salvage:,.0f} > continue "
                   f"€{v_fail:,.0f}). The option adds **€{option_value:,.0f}** of value.")
    else:
        st.info(f"ℹ️ Here salvage (€{salvage:,.0f}) ≤ failure continue value (€{v_fail:,.0f}), so you'd "
                f"keep going even in failure — the abandonment option adds no value at these inputs.")

    st.markdown("---")
    st.subheader("🎛️ Lab B · EVA Calculator")
    st.markdown("Enter operating profit, tax, capital and WACC to compute EVA and ROIC.")

    d1, d2, d3, d4 = st.columns(4)
    with d1:
        ebit = st.number_input("EBIT (€)", min_value=-10_000_000, value=500_000, step=25_000)
    with d2:
        tax_rate = st.slider("Tax rate (%)", 0.0, 50.0, 30.0, 1.0) / 100.0
    with d3:
        capital = st.number_input("Capital employed (€)", min_value=1, value=2_500_000, step=100_000)
    with d4:
        wacc = st.slider("WACC (%)", 0.0, 25.0, 10.0, 0.5) / 100.0

    nopat = ebit * (1 - tax_rate)
    capital_charge = capital * wacc
    eva = nopat - capital_charge
    roic = nopat / capital if capital else 0

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("NOPAT", f"€{nopat:,.0f}")
    k2.metric("Capital charge", f"€{capital_charge:,.0f}")
    k3.metric("EVA", f"€{eva:,.0f}")
    k4.metric("ROIC vs WACC", f"{roic*100:.1f}% / {wacc*100:.1f}%")

    figw = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute", "relative", "total"],
        x=["NOPAT", "− Capital charge", "EVA"],
        y=[nopat, -capital_charge, eva],
        text=[f"€{nopat:,.0f}", f"−€{capital_charge:,.0f}", f"€{eva:,.0f}"],
        connector={"line": {"color": "#90CAF9"}},
        decreasing={"marker": {"color": "#C62828"}},
        increasing={"marker": {"color": "#1B7F3B"}},
        totals={"marker": {"color": "#1565C0"}},
    ))
    figw.update_layout(title="EVA bridge: NOPAT − capital charge",
                       yaxis_title="€", height=400, margin=dict(t=60, b=40))
    st.plotly_chart(figw, use_container_width=True)

    if eva > 0:
        st.success(f"✅ **EVA = €{eva:,.0f} > 0** — ROIC {roic*100:.1f}% beats WACC {wacc*100:.1f}%, "
                   f"so economic value is created.")
    elif eva < 0:
        st.error(f"❌ **EVA = €{eva:,.0f} < 0** — ROIC {roic*100:.1f}% is below WACC {wacc*100:.1f}%; "
                 f"value is destroyed despite any accounting profit.")
    else:
        st.info("EVA = 0 — the business exactly earns its cost of capital.")

    st.caption("Reminder: EVA charges for ALL capital (including equity), unlike accounting profit.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. Real options capture the value of…",
            "options": [
                "Accounting profit",
                "Managerial flexibility to react to future events",
                "Sunk costs",
                "The initial investment only",
            ],
            "answer": 1,
            "why": "Real options value the flexibility to expand, defer, abandon or switch as the future unfolds.",
        },
        {
            "q": "2. Expanded (strategic) NPV equals…",
            "options": [
                "Static NPV − option value",
                "Static NPV + value of options",
                "Option value − static NPV",
                "IRR × static NPV",
            ],
            "answer": 1,
            "why": "Strategic NPV = static NPV plus the value of the embedded real options.",
        },
        {
            "q": "3. Unlike a fixed NPV, the value of a real option generally increases with…",
            "options": ["Lower uncertainty", "Higher uncertainty",
                        "A shorter time horizon", "Fully reversible costs"],
            "answer": 1,
            "why": "More uncertainty makes flexibility more valuable — the opposite of its effect on a static NPV.",
        },
        {
            "q": "4. The option to abandon a project for its salvage value is most like a…",
            "options": ["Call option", "Put option", "Forward contract", "Bond"],
            "answer": 1,
            "why": "Abandonment resembles a put option — the right to 'sell' the project for salvage, limiting downside.",
        },
        {
            "q": "5. EVA is calculated as…",
            "options": [
                "NOPAT − (Capital employed × WACC)",
                "EBIT + depreciation",
                "Revenue − variable cost",
                "NPV ÷ investment",
            ],
            "answer": 0,
            "why": "EVA = NOPAT minus a capital charge (capital employed × WACC).",
        },
        {
            "q": "6. A business with positive accounting profit can still have negative EVA when…",
            "options": [
                "It pays no tax",
                "Its ROIC is below its WACC",
                "It has no debt",
                "Depreciation is zero",
            ],
            "answer": 1,
            "why": "If the return on invested capital is below the cost of capital, the capital charge exceeds NOPAT → negative EVA.",
        },
    ]

    with st.form("quiz_3_4"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q34_{i}")
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
            st.success("🏆 Perfect! You've mastered advanced value concepts — and completed Part 3!")
        elif pct >= 60:
            st.info("👍 Strong work — next is Part 4, starting with **4.1 · Decision Rules & Method Comparison**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on option types and the EVA formula.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `3.3 · Monte Carlo Simulation`")
with cnext:
    st.markdown("**Next:** `4.1 · Decision Rules & Method Comparison` ➡️")
st.caption("Business Case section · Page 3.4 · Built with Streamlit")
