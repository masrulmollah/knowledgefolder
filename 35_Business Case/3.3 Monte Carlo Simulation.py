# ============================================================================
#  BUSINESS CASE — Section
#  Page 3.3 · Monte Carlo Simulation
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
    page_title="3.3 · Monte Carlo Simulation",
    page_icon="🎲",
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
        <h1>3.3 · Monte Carlo Simulation</h1>
        <p>Beyond a few scenarios — assign probability distributions to your assumptions,
        run thousands of trials, and see the full distribution of possible NPVs.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Understand how Monte Carlo works, interpret an NPV distribution, and "
           "read probability-of-loss and P10/P50/P90 outputs.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def npv_from_drivers(units, price, var_cost, fixed_cost, invest, rate, life, tax):
    """Vectorised-friendly project NPV from operating drivers (arrays or scalars)."""
    dep = invest / life
    ebit = units * price - units * var_cost - fixed_cost - dep
    taxamt = np.where(ebit > 0, ebit * tax, 0.0)
    ocf = (ebit - taxamt) + dep
    annuity_factor = sum(1 / (1 + rate) ** t for t in range(1, life + 1))
    return ocf * annuity_factor - invest


def run_simulation(n_trials, base, spreads, rate, life, tax, invest, fixed_cost, seed=42):
    rng = np.random.default_rng(seed)
    units = rng.triangular(base["units"] * (1 - spreads["units"]),
                           base["units"],
                           base["units"] * (1 + spreads["units"]), n_trials)
    price = rng.triangular(base["price"] * (1 - spreads["price"]),
                           base["price"],
                           base["price"] * (1 + spreads["price"]), n_trials)
    var_cost = rng.triangular(base["var_cost"] * (1 - spreads["var_cost"]),
                              base["var_cost"],
                              base["var_cost"] * (1 + spreads["var_cost"]), n_trials)
    npvs = npv_from_drivers(units, price, var_cost, fixed_cost, invest, rate, life, tax)
    return npvs


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
        <b>Monte Carlo Simulation</b> models risk by assigning a <b>probability distribution</b> to each
        uncertain input, then randomly sampling from those distributions <b>thousands of times</b>.
        Each trial produces one NPV; together they form a <b>full distribution of possible outcomes</b> —
        far richer than the three discrete cases of scenario analysis.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · Where It Fits in the Risk Toolkit")
    prog = pd.DataFrame(
        {
            "Method": ["Sensitivity (3.1)", "Scenario (3.2)", "Monte Carlo (3.3)"],
            "Variables changed": ["One at a time", "A few, together", "All, simultaneously & randomly"],
            "Outcomes produced": ["Impact per variable", "3–5 discrete cases", "Thousands → a distribution"],
            "Gives probabilities?": ["No", "Subjective per case", "Yes — full probability profile"],
        }
    )
    st.table(prog)

    st.subheader("3 · How It Works — Five Steps")
    for t, b in [
        ("1️⃣ Build the model",
         "Define the NPV formula linking inputs (volume, price, cost…) to the output."),
        ("2️⃣ Assign distributions",
         "Give each uncertain input a distribution — e.g. triangular (min/most-likely/max), normal "
         "(mean/σ), or uniform."),
        ("3️⃣ Sample randomly",
         "Draw one random value from each input's distribution to form a single trial."),
        ("4️⃣ Recompute & repeat",
         "Calculate NPV for that trial, then repeat thousands of times to build the output distribution."),
        ("5️⃣ Analyse the distribution",
         "Read the mean, spread, percentiles (P10/P50/P90) and the probability that NPV < 0."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("4 · Common Input Distributions")
    c1, c2, c3 = st.columns(3)
    c1.markdown(
        """
        <div class="bc-card"><h4>🔺 Triangular</h4>
        Min, most-likely, max. Intuitive when experts can estimate a range and a best guess.
        Great default for business cases.</div>
        """, unsafe_allow_html=True)
    c2.markdown(
        """
        <div class="bc-card"><h4>🔔 Normal</h4>
        Mean and standard deviation. Good for symmetric uncertainty around a central estimate.</div>
        """, unsafe_allow_html=True)
    c3.markdown(
        """
        <div class="bc-card"><h4>▭ Uniform</h4>
        Any value in a range equally likely. Use when you only know the bounds.</div>
        """, unsafe_allow_html=True)

    st.subheader("5 · Reading the Output")
    st.markdown(
        """
        - **Mean / Expected NPV** — the average across all trials.
        - **Probability of loss** — the % of trials where NPV < 0 (the headline risk metric).
        - **Percentiles** — P10 (pessimistic), P50 (median), P90 (optimistic) give a value range.
        - **Distribution shape** — spread and skew reveal how risky and asymmetric the project is.
        """
    )
    st.latex(r"P(\text{loss}) = \frac{\text{number of trials with } NPV < 0}{\text{total trials}}")

    st.subheader("6 · Strengths & Limitations")
    d1, d2 = st.columns(2)
    with d1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👍 Strengths</h4>
            <ul>
              <li>Produces a <b>full probability distribution</b>, not point estimates</li>
              <li>Quantifies the <b>probability of loss</b> directly</li>
              <li>Can capture <b>many variables and correlations</b></li>
              <li>Powerful for communicating <b>risk</b> to decision-makers</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )
    with d2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👎 Limitations</h4>
            <ul>
              <li><b>Garbage in, garbage out</b> — only as good as the input distributions</li>
              <li>Can create a <b>false sense of precision</b></li>
              <li>Needs <b>software</b> and more effort than other methods</li>
              <li>Correlations between inputs are <b>hard to estimate</b></li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - Monte Carlo assigns **distributions** to inputs and runs **thousands** of trials.
            - The output is a **full NPV distribution**, not a single number.
            - Key metrics: **mean NPV**, **P(loss)**, and **P10/P50/P90** percentiles.
            - It's the most complete risk tool — but only as reliable as its **input assumptions**.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 A 10,000-Trial Simulation")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> The same €800k project. We treat three inputs as <b>triangular</b> distributions
        around their base case: <b>units</b> (±20%), <b>price</b> (±10%) and <b>variable cost</b> (±10%).
        Fixed cost, tax (30%), rate (10%) and life (5 yrs) are held constant. We run <b>10,000 trials</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    base = dict(units=10_000, price=100.0, var_cost=60.0)
    spreads = dict(units=0.20, price=0.10, var_cost=0.10)
    npvs = run_simulation(10_000, base, spreads, rate=0.10, life=5, tax=0.30,
                          invest=800_000, fixed_cost=150_000, seed=42)

    mean_npv = npvs.mean()
    p_loss = (npvs < 0).mean() * 100
    p10, p50, p90 = np.percentile(npvs, [10, 50, 90])

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Mean NPV", f"€{mean_npv:,.0f}")
    m2.metric("P(NPV < 0)", f"{p_loss:.1f}%")
    m3.metric("Median (P50)", f"€{p50:,.0f}")
    m4.metric("P10 – P90", f"€{p10:,.0f} → €{p90:,.0f}")

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=npvs, nbinsx=60, marker_color="#1565C0", opacity=0.85,
                               name="NPV outcomes"))
    fig.add_vline(x=0, line_dash="dash", line_color="#C62828",
                  annotation_text="Break-even", annotation_position="top")
    fig.add_vline(x=mean_npv, line_dash="dot", line_color="#F9A825",
                  annotation_text=f"Mean €{mean_npv:,.0f}", annotation_position="top left")
    fig.update_layout(title="Distribution of NPV across 10,000 trials",
                      xaxis_title="NPV (€)", yaxis_title="Frequency", height=440,
                      margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    if p_loss < 20:
        st.success(f"✅ Across 10,000 trials the **mean NPV is €{mean_npv:,.0f}** with only a "
                   f"**{p_loss:.1f}% chance of a loss**. The median outcome is €{p50:,.0f}, and 80% of "
                   f"outcomes fall between €{p10:,.0f} and €{p90:,.0f} — a fairly robust case.")
    else:
        st.warning(f"🟠 Mean NPV is €{mean_npv:,.0f}, but there's a **{p_loss:.1f}% probability of loss** — "
                   f"a meaningful downside. P10 is €{p10:,.0f}. Weigh this against your risk appetite.")

    st.info("👉 Notice how thousands of trials reveal the *shape* of risk — the spread and the chance "
            "of loss — which three fixed scenarios simply cannot show.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Monte Carlo Engine")
    st.markdown("Set your base case, the uncertainty (± spread) on each driver, and the number of "
                "trials. Then run the simulation to see the full NPV distribution.")

    st.markdown("##### Base-case & fixed assumptions")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        units = st.number_input("Base units", min_value=1, value=10_000, step=500)
        price = st.number_input("Base price (€)", min_value=0.0, value=100.0, step=5.0)
    with c2:
        var_cost = st.number_input("Base var cost/unit (€)", min_value=0.0, value=60.0, step=5.0)
        fixed_cost = st.number_input("Fixed cost/yr (€)", min_value=0, value=150_000, step=10_000)
    with c3:
        invest = st.number_input("Investment (€)", min_value=1, value=800_000, step=25_000)
        life = st.slider("Life (years)", 1, 15, 5)
    with c4:
        rate = st.slider("Discount rate (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
        tax = st.slider("Tax rate (%)", 0.0, 50.0, 30.0, 1.0) / 100.0

    st.markdown("##### Uncertainty (± spread as % of base, triangular distribution)")
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        sp_units = st.slider("Units ± %", 0, 60, 20, 5)
    with s2:
        sp_price = st.slider("Price ± %", 0, 60, 10, 5)
    with s3:
        sp_var = st.slider("Var cost ± %", 0, 60, 10, 5)
    with s4:
        n_trials = st.select_slider("Trials", options=[1_000, 5_000, 10_000, 25_000, 50_000],
                                    value=10_000)

    seed = st.number_input("Random seed (for reproducibility)", min_value=0, value=42, step=1)
    run = st.button("🎲 Run simulation", type="primary")

    if run:
        base = dict(units=units, price=price, var_cost=var_cost)
        spreads = dict(units=sp_units / 100, price=sp_price / 100, var_cost=sp_var / 100)
        npvs = run_simulation(n_trials, base, spreads, rate=rate, life=life, tax=tax,
                              invest=invest, fixed_cost=fixed_cost, seed=int(seed))

        mean_npv = npvs.mean()
        std_npv = npvs.std()
        p_loss = (npvs < 0).mean() * 100
        p5, p10, p50, p90, p95 = np.percentile(npvs, [5, 10, 50, 90, 95])

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Mean NPV", f"€{mean_npv:,.0f}")
        m2.metric("Std deviation", f"€{std_npv:,.0f}")
        m3.metric("P(NPV < 0)", f"{p_loss:.1f}%")
        m4.metric("Median (P50)", f"€{p50:,.0f}")

        n1, n2, n3 = st.columns(3)
        n1.metric("P5 (worst 5%)", f"€{p5:,.0f}")
        n2.metric("P10 – P90 range", f"€{p10:,.0f} → €{p90:,.0f}")
        n3.metric("P95 (best 5%)", f"€{p95:,.0f}")

        fig = go.Figure()
        fig.add_trace(go.Histogram(x=npvs, nbinsx=60, marker_color="#1565C0", opacity=0.85))
        fig.add_vline(x=0, line_dash="dash", line_color="#C62828",
                      annotation_text="Break-even", annotation_position="top")
        fig.add_vline(x=mean_npv, line_dash="dot", line_color="#F9A825",
                      annotation_text=f"Mean €{mean_npv:,.0f}", annotation_position="top left")
        fig.update_layout(title=f"NPV distribution — {n_trials:,} trials",
                          xaxis_title="NPV (€)", yaxis_title="Frequency", height=440,
                          margin=dict(t=70, b=40))
        st.plotly_chart(fig, use_container_width=True)

        # cumulative probability (S-curve)
        sorted_npv = np.sort(npvs)
        cum_p = np.arange(1, len(sorted_npv) + 1) / len(sorted_npv) * 100
        figc = go.Figure(go.Scatter(x=sorted_npv, y=cum_p, mode="lines",
                                    line=dict(color="#0B3D91", width=3)))
        figc.add_vline(x=0, line_dash="dash", line_color="#C62828",
                       annotation_text=f"P(loss) = {p_loss:.1f}%", annotation_position="top left")
        figc.update_layout(title="Cumulative probability (S-curve)",
                           xaxis_title="NPV (€)", yaxis_title="Cumulative probability (%)",
                           height=380, margin=dict(t=60, b=40))
        st.plotly_chart(figc, use_container_width=True)

        if p_loss < 10:
            st.success(f"✅ Only a **{p_loss:.1f}% chance of loss** with mean NPV €{mean_npv:,.0f}. "
                       f"A robust, low-risk investment on these assumptions.")
        elif p_loss < 30:
            st.warning(f"🟠 A **{p_loss:.1f}% chance of loss** with mean NPV €{mean_npv:,.0f}. "
                       f"Moderate risk — check whether the P10 outcome (€{p10:,.0f}) is acceptable.")
        else:
            st.error(f"❌ A high **{p_loss:.1f}% chance of loss** despite a mean NPV of €{mean_npv:,.0f}. "
                     f"The downside is significant — reconsider or de-risk before proceeding.")
    else:
        st.info("👆 Set your inputs and click **Run simulation** to generate the NPV distribution.")

    st.caption("Reminder: results are only as good as the input distributions — 'garbage in, garbage "
               "out'. Use realistic ranges informed by data and expert judgement.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. Monte Carlo simulation models risk by…",
            "options": [
                "Changing one variable at a time",
                "Assigning distributions to inputs and running many random trials",
                "Using only three fixed scenarios",
                "Ignoring uncertainty altogether",
            ],
            "answer": 1,
            "why": "It samples input distributions thousands of times to build a full output distribution.",
        },
        {
            "q": "2. The main output of a Monte Carlo simulation is…",
            "options": [
                "A single point estimate of NPV",
                "A full probability distribution of outcomes",
                "The payback period",
                "The accounting rate of return",
            ],
            "answer": 1,
            "why": "The output is a distribution of possible NPVs, not a single number.",
        },
        {
            "q": "3. A triangular distribution is defined by…",
            "options": [
                "Mean and standard deviation",
                "Minimum, most-likely, and maximum",
                "Only an upper bound",
                "A single fixed value",
            ],
            "answer": 1,
            "why": "Triangular distributions use a min, a most-likely (mode), and a max — intuitive for experts.",
        },
        {
            "q": "4. The probability of loss is measured as…",
            "options": [
                "The mean NPV divided by the investment",
                "The proportion of trials where NPV < 0",
                "The highest NPV observed",
                "The discount rate",
            ],
            "answer": 1,
            "why": "P(loss) = fraction of trials with a negative NPV — the headline risk metric.",
        },
        {
            "q": "5. P10, P50 and P90 refer to…",
            "options": [
                "Three discount rates",
                "Percentiles of the NPV distribution (pessimistic, median, optimistic)",
                "Payback periods in years",
                "Probabilities that always sum to 100%",
            ],
            "answer": 1,
            "why": "They are percentiles: P10 pessimistic, P50 median, P90 optimistic outcomes.",
        },
        {
            "q": "6. A key limitation of Monte Carlo is that…",
            "options": [
                "It cannot handle more than one variable",
                "Its results are only as good as the input distributions",
                "It ignores the time value of money",
                "It always produces a negative NPV",
            ],
            "answer": 1,
            "why": "'Garbage in, garbage out' — unrealistic input assumptions produce misleading results.",
        },
    ]

    with st.form("quiz_3_3"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q33_{i}")
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
            st.success("🏆 Perfect! You can now quantify risk with the most powerful tool in the kit.")
        elif pct >= 60:
            st.info("👍 Strong work — continue to **3.4 · Real Options & EVA**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on distributions, P(loss) and percentiles.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `3.2 · Scenario Analysis`")
with cnext:
    st.markdown("**Next:** `3.4 · Real Options & EVA` ➡️")
st.caption("Business Case section · Page 3.3 · Built with Streamlit")
