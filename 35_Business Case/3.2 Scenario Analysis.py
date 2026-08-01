# ============================================================================
#  BUSINESS CASE — Section
#  Page 3.2 · Scenario Analysis
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
    page_title="3.2 · Scenario Analysis",
    page_icon="🎭",
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
        <h1>3.2 · Scenario Analysis</h1>
        <p>From one variable to whole worlds — bundle assumptions into coherent
        Base, Best and Worst cases, then weight them by probability to see the expected outcome.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Build coherent scenarios, compute probability-weighted expected NPV, "
           "and read the risk profile of an investment.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def project_npv(units, price, var_cost, fixed_cost, invest, rate, life, tax):
    dep = invest / life if life else 0
    ebit = units * price - units * var_cost - fixed_cost - dep
    taxamt = max(ebit, 0) * tax
    ocf = (ebit - taxamt) + dep
    pv = sum(ocf / (1 + rate) ** t for t in range(1, life + 1))
    return pv - invest


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
        <b>Scenario Analysis</b> evaluates the business case under a small number of <b>internally
        consistent “states of the world”</b> — typically <b>Base</b>, <b>Best</b> and <b>Worst</b> cases.
        Unlike sensitivity analysis (one variable at a time), scenarios change <b>several variables
        together</b> in a way that reflects how they would realistically move as a bundle.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · Sensitivity vs Scenario — The Key Difference")
    diff = pd.DataFrame(
        {
            "Aspect": ["Variables changed", "Captures correlations?", "Output", "Best for"],
            "Sensitivity (3.1)": ["One at a time", "No", "Impact of each variable",
                                  "Finding the critical variable"],
            "Scenario (3.2)": ["Several together, coherently", "Yes (by design)",
                               "A few complete outcomes", "Seeing plausible combined outcomes"],
        }
    )
    st.table(diff)

    st.subheader("3 · The Three Classic Scenarios")
    for t, b in [
        ("🟢 Best case (optimistic)",
         "All key drivers move favourably together — higher volume & price, lower costs. The upside "
         "potential."),
        ("🔵 Base case (most likely)",
         "Your central, best-estimate assumptions — the scenario the business case is built around."),
        ("🔴 Worst case (pessimistic)",
         "Key drivers move adversely together — lower volume & price, higher costs. The downside "
         "exposure and a test of survivability."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("4 · Probability-Weighted Expected NPV")
    st.markdown(
        "Assign each scenario a probability (summing to 100%) and compute the **Expected NPV** — "
        "the probability-weighted average outcome:"
    )
    st.latex(r"E[NPV] = \sum_{i} p_i \times NPV_i")
    st.markdown(
        "Where $p_i$ is the probability of scenario $i$ and $NPV_i$ its NPV. This single figure blends "
        "upside and downside into an expected value for decision-making."
    )

    st.subheader("5 · Measuring the Risk — Spread & Downside")
    st.markdown(
        """
        Scenarios reveal not just the *expected* result but its **spread**:
        - **Range** = Best-case NPV − Worst-case NPV (the total swing)
        - **Downside** = is the worst case survivable? Does NPV stay above a floor?
        - **Standard deviation** across scenarios = a simple measure of risk/volatility
        """
    )
    st.latex(r"\sigma = \sqrt{\sum_i p_i \,(NPV_i - E[NPV])^2}")
    st.markdown(
        "<span class='muted'>A high expected NPV with a catastrophic, likely worst case may be "
        "rejected in favour of a lower but safer alternative — risk appetite matters.</span>",
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
              <li>Captures <b>realistic combinations</b> of assumptions</li>
              <li>Respects how variables <b>move together</b></li>
              <li>Produces an <b>expected value</b> and a risk range</li>
              <li>Intuitive for boards — tells a <b>story</b> per scenario</li>
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
              <li>Only a <b>handful of outcomes</b> — reality is continuous</li>
              <li>Probabilities are often <b>subjective</b></li>
              <li>Can lull you into thinking 3 cases <b>cover all risk</b></li>
              <li>For a full distribution, use <b>Monte Carlo</b> (3.3)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - Scenario analysis changes **several variables together** into coherent worlds.
            - Standard trio: **Best / Base / Worst** case.
            - **Expected NPV** = Σ (probability × scenario NPV).
            - Also look at the **range and worst-case survivability**, not just the average.
            - For a continuous distribution of outcomes, extend to **Monte Carlo** (3.3).
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Base / Best / Worst — and Expected NPV")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> The same project as page 3.1 (€800k investment, 5-year life, 30% tax, 10% rate).
        We define three coherent scenarios by bundling volume, price and variable-cost assumptions,
        then weight them by probability.
        </div>
        """,
        unsafe_allow_html=True,
    )

    common = dict(fixed_cost=150_000, invest=800_000, rate=0.10, life=5, tax=0.30)
    scenarios = {
        "Worst":  dict(units=8_000,  price=90.0,  var_cost=66.0, prob=0.25),
        "Base":   dict(units=10_000, price=100.0, var_cost=60.0, prob=0.50),
        "Best":   dict(units=12_000, price=110.0, var_cost=55.0, prob=0.25),
    }

    rows = []
    for name, sc in scenarios.items():
        npv = project_npv(units=sc["units"], price=sc["price"], var_cost=sc["var_cost"], **common)
        rows.append({"Scenario": name, "Units": sc["units"], "Price (€)": sc["price"],
                     "Var cost (€)": sc["var_cost"], "Probability": sc["prob"], "NPV (€)": npv})
    dfres = pd.DataFrame(rows)

    st.dataframe(
        dfres.style.format({"Units": "{:,.0f}", "Price (€)": "{:,.0f}", "Var cost (€)": "{:,.0f}",
                            "Probability": "{:.0%}", "NPV (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    exp_npv = (dfres["Probability"] * dfres["NPV (€)"]).sum()
    variance = (dfres["Probability"] * (dfres["NPV (€)"] - exp_npv) ** 2).sum()
    std = variance ** 0.5
    rng = dfres["NPV (€)"].max() - dfres["NPV (€)"].min()

    st.latex(rf"E[NPV] = 0.25({dfres.iloc[0]['NPV (€)']:,.0f}) + 0.50({dfres.iloc[1]['NPV (€)']:,.0f})"
             rf" + 0.25({dfres.iloc[2]['NPV (€)']:,.0f}) = €{exp_npv:,.0f}")

    m1, m2, m3 = st.columns(3)
    m1.metric("Expected NPV", f"€{exp_npv:,.0f}")
    m2.metric("Std deviation (risk)", f"€{std:,.0f}")
    m3.metric("Range (Best − Worst)", f"€{rng:,.0f}")

    colors = {"Worst": "#C62828", "Base": "#1565C0", "Best": "#1B7F3B"}
    fig = go.Figure(go.Bar(
        x=dfres["Scenario"], y=dfres["NPV (€)"],
        marker_color=[colors[s] for s in dfres["Scenario"]],
        text=[f"€{v:,.0f}" for v in dfres["NPV (€)"]], textposition="outside",
    ))
    fig.add_hline(y=exp_npv, line_dash="dash", line_color="#F9A825",
                  annotation_text=f"E[NPV] €{exp_npv:,.0f}", annotation_position="top left")
    fig.add_hline(y=0, line_dash="dot", line_color="grey")
    fig.update_layout(title="NPV by scenario, with expected value",
                      yaxis_title="NPV (€)", height=430, margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    worst_npv = dfres.iloc[0]["NPV (€)"]
    if worst_npv < 0:
        st.warning(f"⚠️ The **worst case NPV is €{worst_npv:,.0f} (negative)** with a 25% probability — "
                   f"even though Expected NPV is positive at €{exp_npv:,.0f}. Judge whether the downside "
                   f"is survivable and acceptable given your risk appetite.")
    else:
        st.success(f"✅ Even the worst case stays positive (€{worst_npv:,.0f}), and Expected NPV is "
                   f"€{exp_npv:,.0f} — a robust, low-risk investment on these scenarios.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Scenario Builder")
    st.markdown("Define three scenarios and their probabilities. The tool computes each NPV, the "
                "expected NPV, and the risk profile. Probabilities should sum to 100%.")

    st.markdown("##### Shared (fixed) assumptions")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        fixed_cost = st.number_input("Fixed cost/yr (€)", min_value=0, value=150_000, step=10_000)
    with c2:
        invest = st.number_input("Initial investment (€)", min_value=1, value=800_000, step=25_000)
    with c3:
        life = st.slider("Project life (years)", 1, 15, 5)
    with c4:
        rate = st.slider("Discount rate (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
    tax = st.slider("Tax rate (%)", 0.0, 50.0, 30.0, 1.0) / 100.0
    common = dict(fixed_cost=fixed_cost, invest=invest, rate=rate, life=life, tax=tax)

    st.markdown("##### Scenario assumptions")
    editable = pd.DataFrame(
        {
            "Scenario": ["Worst", "Base", "Best"],
            "Units": [8_000, 10_000, 12_000],
            "Price (€)": [90.0, 100.0, 110.0],
            "Var cost/unit (€)": [66.0, 60.0, 55.0],
            "Probability (%)": [25.0, 50.0, 25.0],
        }
    )
    sc = st.data_editor(editable, use_container_width=True, hide_index=True,
                        num_rows="dynamic", key="scenario_editor")

    sc = sc.copy()
    sc = sc[sc["Units"].notna()]
    sc["NPV (€)"] = sc.apply(
        lambda r: project_npv(units=r["Units"], price=r["Price (€)"],
                              var_cost=r["Var cost/unit (€)"], **common), axis=1)
    prob_sum = sc["Probability (%)"].sum()

    if abs(prob_sum - 100) > 0.01:
        st.warning(f"⚠️ Probabilities sum to **{prob_sum:.0f}%** — they should total 100%. "
                   f"Expected NPV below is normalised to your weights.")
    weights = sc["Probability (%)"] / prob_sum if prob_sum else sc["Probability (%)"] * 0
    exp_npv = (weights * sc["NPV (€)"]).sum()
    variance = (weights * (sc["NPV (€)"] - exp_npv) ** 2).sum()
    std = variance ** 0.5
    rng = sc["NPV (€)"].max() - sc["NPV (€)"].min()

    st.dataframe(
        sc.style.format({"Units": "{:,.0f}", "Price (€)": "{:,.0f}", "Var cost/unit (€)": "{:,.0f}",
                         "Probability (%)": "{:.0f}%", "NPV (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("Expected NPV", f"€{exp_npv:,.0f}")
    m2.metric("Std deviation (risk)", f"€{std:,.0f}")
    m3.metric("Range", f"€{rng:,.0f}")

    palette = ["#C62828", "#1565C0", "#1B7F3B", "#F9A825", "#6A1B9A", "#00838F"]
    fig = go.Figure(go.Bar(
        x=sc["Scenario"], y=sc["NPV (€)"],
        marker_color=[palette[i % len(palette)] for i in range(len(sc))],
        text=[f"€{v:,.0f}" for v in sc["NPV (€)"]], textposition="outside",
    ))
    fig.add_hline(y=exp_npv, line_dash="dash", line_color="#F9A825",
                  annotation_text=f"E[NPV] €{exp_npv:,.0f}", annotation_position="top left")
    fig.add_hline(y=0, line_dash="dot", line_color="grey")
    fig.update_layout(title="NPV by scenario", yaxis_title="NPV (€)", height=430,
                      margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    worst_npv = sc["NPV (€)"].min()
    if exp_npv > 0 and worst_npv >= 0:
        st.success(f"✅ Expected NPV €{exp_npv:,.0f} and even the worst outcome is non-negative "
                   f"(€{worst_npv:,.0f}) → a robust case.")
    elif exp_npv > 0 and worst_npv < 0:
        st.warning(f"🟠 Positive Expected NPV (€{exp_npv:,.0f}) but a negative worst case "
                   f"(€{worst_npv:,.0f}). Accept only if the downside is survivable and acceptable.")
    else:
        st.error(f"❌ Expected NPV is €{exp_npv:,.0f} — the probability-weighted outcome destroys value.")

    st.caption("Reminder: three scenarios sketch the risk; for a full continuous distribution of "
               "outcomes, use Monte Carlo simulation (page 3.3).")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 5 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. How does scenario analysis differ from sensitivity analysis?",
            "options": [
                "It changes only one variable at a time",
                "It changes several variables together in coherent combinations",
                "It ignores the time value of money",
                "It requires no assumptions",
            ],
            "answer": 1,
            "why": "Scenario analysis flexes multiple variables together as internally consistent bundles.",
        },
        {
            "q": "2. The three classic scenarios are…",
            "options": [
                "Short, medium, long",
                "Best, base, worst",
                "Debt, equity, hybrid",
                "Fixed, variable, semi-variable",
            ],
            "answer": 1,
            "why": "The standard trio is optimistic (best), most-likely (base), and pessimistic (worst).",
        },
        {
            "q": "3. Expected NPV is calculated as…",
            "options": [
                "The average of the best and worst NPVs",
                "The sum of each scenario's probability × its NPV",
                "The highest scenario NPV",
                "NPV divided by the number of scenarios",
            ],
            "answer": 1,
            "why": "Expected NPV = Σ (probability × scenario NPV) — a probability-weighted average.",
        },
        {
            "q": "4. Even with a positive expected NPV, a project may be rejected if…",
            "options": [
                "The best case is too high",
                "The worst case is a catastrophic, non-survivable loss",
                "There are only three scenarios",
                "The discount rate is positive",
            ],
            "answer": 1,
            "why": "A severe, likely downside can outweigh a positive average, depending on risk appetite.",
        },
        {
            "q": "5. A key limitation of scenario analysis is that it…",
            "options": [
                "Considers only a handful of discrete outcomes, not a full distribution",
                "Cannot change more than one variable",
                "Ignores probabilities entirely",
                "Always understates risk to zero",
            ],
            "answer": 0,
            "why": "It looks at only a few discrete states; Monte Carlo provides the full continuous distribution.",
        },
    ]

    with st.form("quiz_3_2"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q32_{i}")
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
            st.success("🏆 Perfect! You can now frame and weight scenarios like a pro.")
        elif pct >= 60:
            st.info("👍 Good work — continue to **3.3 · Monte Carlo Simulation**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on expected NPV and downside risk.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `3.1 · Sensitivity Analysis`")
with cnext:
    st.markdown("**Next:** `3.3 · Monte Carlo Simulation` ➡️")
st.caption("Business Case section · Page 3.2 · Built with Streamlit")
