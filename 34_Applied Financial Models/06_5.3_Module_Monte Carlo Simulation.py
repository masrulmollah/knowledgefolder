"""
================================================================================
APPLIED FINANCIAL MODELS
Module 5.3 — MONTE CARLO SIMULATION
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to quantify risk with Monte Carlo simulation: modelling uncertain inputs as
probability distributions, running thousands of random trials, and reading the
resulting distribution of outcomes.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live Monte Carlo NPV simulator)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas numpy
    streamlit run Module_5_3_Monte_Carlo_Simulation.py
================================================================================
"""

from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="5.3 Monte Carlo Simulation — Applied Financial Models",
    layout="wide",
    page_icon="🎲",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def run_monte_carlo(n_trials, capex, life, discount_rate,
                    vol_mean, vol_sd, price_mean, price_sd,
                    vc_mean, vc_sd, fixed_mean, fixed_sd, seed=42):
    """
    Run a Monte Carlo simulation of project NPV.
    Each uncertain input is drawn from a normal distribution.
    Returns an array of NPVs (one per trial).
    """
    rng = np.random.default_rng(seed)
    vol = rng.normal(vol_mean, vol_sd, n_trials)
    price = rng.normal(price_mean, price_sd, n_trials)
    vc = rng.normal(vc_mean, vc_sd, n_trials)
    fixed = rng.normal(fixed_mean, fixed_sd, n_trials)

    # clip to sensible non-negative ranges
    vol = np.clip(vol, 0, None)
    price = np.clip(price, 0, None)
    vc = np.clip(vc, 0, None)
    fixed = np.clip(fixed, 0, None)

    annual_cf = vol * (price - vc) - fixed
    r = discount_rate / 100
    annuity_factor = sum(1 / ((1 + r) ** t) for t in range(1, life + 1))
    npvs = annual_cf * annuity_factor - capex
    return npvs


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 5 · Scenario, Sensitivity & Risk Models")
st.sidebar.markdown(
    """
**Module 5.3 — Monte Carlo Simulation**

🔴 *Advanced*

**You will learn to:**
- Model inputs as probability distributions
- Run thousands of random trials
- Read the distribution of outcomes
- Estimate the probability of a positive NPV
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to run a live Monte Carlo "
    "simulation and see the full distribution of possible NPVs."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎲 5.3 · Monte Carlo Simulation")
st.markdown(
    """
Sensitivity analysis (5.1) flexes one input; scenario analysis (5.2) tests a handful of coherent cases.
**Monte Carlo simulation** goes further: it treats each uncertain input as a **probability distribution**
and runs the model **thousands of times** with random draws — producing the *full distribution* of
possible outcomes, not just three points.

The payoff is a powerful, probabilistic answer: instead of "the NPV is €400k", you can say *"there's an
82% chance the NPV is positive, and here's the range."* This is the most sophisticated risk tool in Part 5.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "5.3")
c2.metric("Part", "5 — Risk")
c3.metric("Level", "Advanced")
c4.metric("Learning Tabs", "5")

tab_labels = [
    "📚 Theory & Concepts",
    "🔢 Worked Examples",
    "✏️ Interactive Exercises",
    "🏭 Real-Life Practical Cases",
    "✅ Knowledge Test / Quiz",
]
tabs = st.tabs(tab_labels)

# ================================================================================
# TAB 1 — THEORY & CONCEPTS
# ================================================================================
with tabs[0]:
    st.subheader("Theory & Concepts")

    st.markdown(
        """
### What is Monte Carlo simulation?
Named after the casino, Monte Carlo simulation uses **repeated random sampling** to model uncertainty.
Instead of single point-estimates for inputs, you specify a **probability distribution** for each, then
let the computer run the model thousands of times — each trial drawing a random value for every input.
The result is a **distribution of outcomes** you can analyse statistically.
"""
    )

    st.markdown("### The four steps")
    steps = pd.DataFrame(
        {
            "Step": ["1. Model inputs as distributions", "2. Random sampling", "3. Run many trials", "4. Analyse the output distribution"],
            "What you do": [
                "Assign each uncertain input a distribution (e.g. Normal with a mean & standard deviation)",
                "Each trial draws one random value from every input's distribution",
                "Repeat thousands of times (e.g. 10,000 trials), computing the output each time",
                "Summarise: mean, range, percentiles, and probability of success",
            ],
        }
    )
    st.table(steps)

    with st.expander("🔑 Concept 1 — Inputs as distributions, not point estimates"):
        st.markdown(
            """
The key shift: instead of *"volume = 100,000"*, you say *"volume is Normally distributed with a mean of
100,000 and a standard deviation of 10,000."* Common distributions:
- **Normal** — symmetric uncertainty around a mean (most common).
- **Triangular** — min / most-likely / max (good when you only have three estimates).
- **Uniform** — equally likely anywhere in a range.

The distribution captures *how uncertain* each input is, not just its central value.
"""
        )

    with st.expander("🔑 Concept 2 — The law of large numbers"):
        st.markdown(
            """
With enough trials, the simulated distribution converges on the 'true' distribution of outcomes. A few
hundred trials is noisy; **10,000+** gives a stable, reliable picture. More trials = more precision, at
the cost of computation time.
"""
        )

    with st.expander("🔑 Concept 3 — Reading the output distribution"):
        st.markdown(
            """
The simulation produces a **histogram** of outcomes. Key statistics:
- **Mean / median** — the central expected outcome.
- **Range & standard deviation** — how spread out (risky) the outcomes are.
- **Percentiles** — e.g. the 5th percentile (P5) is a 'value at risk' downside; the 95th (P95) an upside.
- **Probability of success** — the % of trials where NPV > 0. *This* is Monte Carlo's headline output.
"""
        )

    with st.expander("🔑 Concept 4 — Monte Carlo vs. sensitivity vs. scenario"):
        st.markdown(
            """
| Method | Inputs changed | Output |
|---|---|---|
| Sensitivity (5.1) | One at a time | How each driver moves the result |
| Scenario (5.2) | A few coherent sets | A handful of discrete outcomes |
| **Monte Carlo (5.3)** | **All, randomly, thousands of times** | **Full probability distribution** |

Monte Carlo is the most complete — but also the most data-hungry (you need to justify every distribution).
"""
        )

    with st.expander("🔑 Concept 5 — Strengths & limitations"):
        st.markdown(
            """
- ✅ **Strengths:** captures the full range and probability of outcomes; handles many uncertain inputs at
  once; gives a probability of success — powerful for decision-making under uncertainty.
- ⚠️ **Limitations:** only as good as the input distributions (garbage-in-garbage-out); assumes you know
  the distributions and correlations; can create false confidence with precise-looking probabilities built
  on shaky assumptions.

Use it to *understand* risk, not to manufacture certainty.
"""
        )

    st.success(
        "**Takeaway:** Monte Carlo simulation models inputs as distributions and runs thousands of random "
        "trials to produce the full distribution of outcomes — including the crucial probability of a "
        "positive result. It's the most complete risk tool, but only as reliable as its input assumptions."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Simulating a project's NPV")
    st.markdown(
        "Take the project from earlier modules, but now treat the key inputs as **uncertain distributions** "
        "rather than fixed numbers."
    )

    st.markdown("#### Step 1 — Define input distributions")
    st.markdown(
        """
| Input | Distribution | Mean | Std. dev. |
|---|---|---|---|
| Volume | Normal | 100,000 | 6,000 |
| Price | Normal | €20 | €0.80 |
| Variable cost | Normal | €12 | €0.60 |
| Fixed cost | Normal | €300,000 | €12,000 |

Fixed: capex €1.5m, 5-year life, 10% discount rate.
"""
    )

    st.markdown("#### Step 2 — Run 10,000 trials")
    st.markdown(
        """
Each trial draws a random value for every input, computes the annual cash flow, discounts it, and records
the NPV. After 10,000 trials we have 10,000 NPVs to analyse.
"""
    )

    st.markdown("#### Step 3 — Read the output distribution (illustrative)")
    st.markdown(
        """
| Statistic | Value |
|---|---|
| Mean NPV | ≈ €397,000 |
| Standard deviation | ≈ €430,000 |
| 5th percentile (P5) | ≈ (€277,000) |
| 95th percentile (P95) | ≈ €1,121,000 |
| **Probability NPV > 0** | **≈ 82%** |
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Mean NPV", "≈ €397,000")
    e2.metric("P(NPV > 0)", "≈ 82%")
    e3.metric("Downside (P5)", "≈ −€277,000", delta_color="inverse")

    st.info(
        "**Insight:** The **mean NPV (~€395k)** matches the single-point base case — but Monte Carlo adds "
        "the vital risk dimension: there's an **~82% chance of a positive NPV**, a plausible downside (P5) "
        "of about −€310k, and meaningful upside (P95 ~€1.1m). Instead of a fragile single number, the board "
        "gets a **probability of success** and a full risk profile. **Recommendation: an 82% success "
        "probability with a survivable downside supports proceeding.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Live Monte Carlo NPV Simulator")
    st.markdown(
        "Set each input's mean and uncertainty (standard deviation), choose the number of trials, and run "
        "the simulation to see the full distribution of possible NPVs."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        st.markdown("##### 🔧 Fixed parameters")
        capex = st.number_input("Capex (€)", 0, 100_000_000, 1_500_000, 50_000)
        life = st.slider("Life (years)", 1, 20, 5, 1)
        discount = st.slider("Discount rate (%)", 1.0, 25.0, 10.0, 0.5)
        n_trials = st.select_slider("Number of trials", [1_000, 5_000, 10_000, 50_000], value=10_000)

        st.markdown("##### 🎲 Uncertain inputs (mean ± std dev)")
        vol_mean = st.number_input("Volume — mean", 1_000, 10_000_000, 100_000, 5_000)
        vol_sd = st.number_input("Volume — std dev", 0, 5_000_000, 6_000, 1_000)
        price_mean = st.number_input("Price — mean (€)", 0.1, 1000.0, 20.0, 0.5)
        price_sd = st.number_input("Price — std dev (€)", 0.0, 500.0, 0.8, 0.1)
        vc_mean = st.number_input("Variable cost — mean (€)", 0.0, 1000.0, 12.0, 0.5)
        vc_sd = st.number_input("Variable cost — std dev (€)", 0.0, 500.0, 0.6, 0.1)
        fixed_mean = st.number_input("Fixed cost — mean (€)", 0, 50_000_000, 300_000, 25_000)
        fixed_sd = st.number_input("Fixed cost — std dev (€)", 0, 10_000_000, 12_000, 1_000)

    with right:
        npvs = run_monte_carlo(
            n_trials, capex, life, discount,
            vol_mean, vol_sd, price_mean, price_sd,
            vc_mean, vc_sd, fixed_mean, fixed_sd,
        )

        mean_npv = float(np.mean(npvs))
        median_npv = float(np.median(npvs))
        sd_npv = float(np.std(npvs))
        p5 = float(np.percentile(npvs, 5))
        p95 = float(np.percentile(npvs, 95))
        prob_positive = float(np.mean(npvs > 0) * 100)

        k1, k2, k3 = st.columns(3)
        k1.metric("Mean NPV", money(mean_npv))
        k2.metric("Probability NPV > 0", f"{prob_positive:.1f}%",
                  "Likely +" if prob_positive >= 50 else "Likely −",
                  delta_color="normal" if prob_positive >= 50 else "inverse")
        k3.metric("Std deviation", money(sd_npv), help="Spread / risk")

        k4, k5, k6 = st.columns(3)
        k4.metric("Downside P5", money(p5), delta_color="inverse")
        k5.metric("Median NPV", money(median_npv))
        k6.metric("Upside P95", money(p95))

        # verdict
        if prob_positive >= 80:
            st.success(
                f"✅ **Strong case:** {prob_positive:.0f}% probability of a positive NPV. The odds clearly "
                "favour proceeding — confirm the downside (P5) is survivable."
            )
        elif prob_positive >= 50:
            st.info(
                f"🔎 **Marginal:** {prob_positive:.0f}% chance of a positive NPV. Better than a coin-flip, "
                "but the downside is material — consider risk mitigation before committing."
            )
        else:
            st.warning(
                f"⚠️ **Risky:** only {prob_positive:.0f}% chance of a positive NPV. More likely to destroy "
                "value than create it as configured."
            )

        # histogram
        st.markdown("##### 📊 Distribution of simulated NPVs")
        counts, edges = np.histogram(npvs, bins=40)
        centers = [(edges[i] + edges[i + 1]) / 2 for i in range(len(edges) - 1)]
        hist_df = pd.DataFrame({"NPV (€)": centers, "Frequency": counts}).set_index("NPV (€)")
        st.bar_chart(hist_df)
        st.caption(
            f"Across {n_trials:,} trials: mean {money(mean_npv)}, ranging from a P5 of {money(p5)} to a "
            f"P95 of {money(p95)}. The share of bars right of €0 is the {prob_positive:.0f}% success probability."
        )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **More certainty:** Cut every std dev in half. Watch the distribution narrow and the success
   probability sharpen.
2. **High uncertainty:** Triple the price std dev. See the range widen and P(NPV>0) change.
"""
        )
    with e2:
        st.markdown(
            """
3. **Trials & stability:** Run 1,000 vs. 50,000 trials. Notice the results steady as trials increase
   (law of large numbers).
4. **Break the case:** Lower the mean price until the success probability drops below 50%.
"""
        )

    st.download_button(
        "⬇️ Download simulation summary (CSV)",
        pd.DataFrame({
            "Statistic": ["Mean", "Median", "Std dev", "P5", "P95", "P(NPV>0) %", "Trials"],
            "Value": [mean_npv, median_npv, sd_npv, p5, p95, prob_positive, n_trials],
        }).to_csv(index=False).encode("utf-8"),
        "monte_carlo_summary.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Giving the board a probability of success", expanded=True):
        st.markdown(
            """
**Situation:** A board was uncomfortable approving a large investment on a single-point NPV.

**How Monte Carlo helped:** By modelling volume, price and costs as distributions and running 10,000
trials, the team could state: *"There's an 82% probability of a positive NPV, with a worst-case (P5) loss
of ~€310k."* This reframed the decision in terms the board could weigh against its risk appetite.

**Why it matters:** A probability of success is far more decision-useful than a deterministic number that
hides all the uncertainty.

**Lesson:** Monte Carlo turns "the NPV is €400k" into "here's the *chance* it pays off, and the range" —
exactly what risk-aware boards want.
"""
        )

    with st.expander("Case B — Comparing two projects on risk, not just return"):
        st.markdown(
            """
**Situation:** Two projects had similar mean NPVs, so they looked equally attractive.

**What Monte Carlo revealed:** Their **distributions** were very different — one had a tight spread and a
90% success probability; the other was high-variance with only a 60% chance of a positive NPV and a large
potential loss.

**Why it matters:** Equal expected returns can mask very different risk. The distribution — not the mean —
told the real story.

**Lesson:** Use the full distribution (spread, percentiles, P(success)) to compare projects on a
risk-adjusted basis.
"""
        )

    with st.expander("Case C — The danger of shaky input distributions"):
        st.markdown(
            """
**Situation:** A slick Monte Carlo model reported a precise "87.3% chance of success", impressing everyone.

**What went wrong:** The input distributions were **guesses** with no data behind them. The
precise-looking probability created **false confidence** in assumptions that were essentially made up.

**Why it matters:** Monte Carlo's sophistication can lend unwarranted credibility to weak inputs
(garbage-in-garbage-out, dressed up in statistics).

**Lesson:** A Monte Carlo result is only as good as its input distributions — justify them with data, and
be honest about their uncertainty.
"""
        )

    st.info(
        "🔗 **Pattern:** Monte Carlo is the most powerful risk tool — it quantifies the probability and range "
        "of outcomes across all uncertain inputs at once. But it demands credible input distributions; "
        "sophistication is no substitute for sound assumptions."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_53"):
        q1 = st.radio(
            "**1.** Monte Carlo simulation models uncertainty by:",
            [
                "Changing one input at a time",
                "Treating inputs as probability distributions and running many random trials",
                "Using only the base case",
                "Ignoring the discount rate",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** In a Monte Carlo model, an uncertain input is represented as:",
            [
                "A single fixed number",
                "A probability distribution (e.g. Normal with a mean and standard deviation)",
                "The tax rate",
                "A sunk cost",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The headline output of a Monte Carlo NPV simulation is usually:",
            [
                "A single guaranteed NPV",
                "The probability of a positive NPV (and the distribution of outcomes)",
                "The depreciation schedule",
                "The payback period only",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Running more trials (e.g. 10,000+) is important because:",
            [
                "It changes the input assumptions",
                "The results converge and stabilise (law of large numbers)",
                "It removes all risk",
                "It lowers the discount rate",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The main limitation of Monte Carlo simulation is that:",
            [
                "It can only handle one input",
                "It is only as reliable as the input distributions (garbage-in, garbage-out)",
                "It cannot produce a probability",
                "It ignores the time value of money",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Treating inputs as probability distributions and running many random trials"),
            "2": (q2, "A probability distribution (e.g. Normal with a mean and standard deviation)"),
            "3": (q3, "The probability of a positive NPV (and the distribution of outcomes)"),
            "4": (q4, "The results converge and stabilise (law of large numbers)"),
            "5": (q5, "It is only as reliable as the input distributions (garbage-in, garbage-out)"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered Monte Carlo simulation! On to Module 5.4 (Break-Even & Margin of Safety). 🎉")
        elif score >= 3:
            st.info("Good work — review the feedback below to close the gaps.")
        else:
            st.warning("Worth another pass — revisit the Theory tab, then retry.")

        st.markdown("#### Feedback")
        for qn, (given, correct) in answers.items():
            if given == correct:
                st.markdown(f"- **Q{qn}: ✅ Correct**")
            elif given is None:
                st.markdown(f"- **Q{qn}: ⚠️ Not answered.** Correct answer: _{correct}_")
            else:
                st.markdown(f"- **Q{qn}: ❌ Incorrect.** Correct answer: _{correct}_")

st.markdown("---")
st.caption(
    f"Applied Financial Models · Module 5.3 Monte Carlo Simulation · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
