"""
================================================================================
APPLIED FINANCIAL MODELS
Module 5.2 — SCENARIO ANALYSIS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to run scenario analysis: Base / Best / Worst cases, scenario managers, and
probability-weighted expected outcomes.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live scenario manager comparing cases)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_5_2_Scenario_Analysis.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="5.2 Scenario Analysis — Applied Financial Models",
    layout="wide",
    page_icon="🎲",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def project_npv(volume, price, var_cost, fixed_cost, capex, life, discount_rate):
    """Simple project NPV used as the base model across all scenarios."""
    annual_cf = volume * (price - var_cost) - fixed_cost
    r = discount_rate / 100
    pv = sum(annual_cf / ((1 + r) ** t) for t in range(1, life + 1))
    return pv - capex


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 5 · Scenario, Sensitivity & Risk Models")
st.sidebar.markdown(
    """
**Module 5.2 — Scenario Analysis**

🟡 *Intermediate*

**You will learn to:**
- Build Base / Best / Worst cases
- Change a coherent SET of assumptions together
- Use a scenario manager
- Compute a probability-weighted expected value
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a scenario manager and "
    "compare Base / Best / Worst outcomes side by side."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎲 5.2 · Scenario Analysis")
st.markdown(
    """
Where **sensitivity analysis** (5.1) flexes *one input at a time*, **scenario analysis** changes a
**coherent set of assumptions together** to represent a plausible future — a *"recession"*, a
*"boom"*, a *"supply-chain crisis"*. Because real-world events move many drivers at once (a downturn cuts
volume **and** price **and** raises costs), scenarios give a more realistic picture of risk.

This module covers the classic **Base / Best / Worst** framework, scenario managers, and how to weight
scenarios by probability to get an **expected value**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "5.2")
c2.metric("Part", "5 — Risk")
c3.metric("Level", "Intermediate")
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
### What is scenario analysis?
A **scenario** is an internally-consistent story about the future, expressed as a **set** of assumption
values that move *together*. Scenario analysis runs the model under several such stories to see the range
of outcomes — a far more realistic view of risk than flexing one input in isolation.
"""
    )

    st.markdown("### The classic Base / Best / Worst framework")
    framework = pd.DataFrame(
        {
            "Scenario": ["Best case", "Base case", "Worst case"],
            "Represents": [
                "Everything goes well (optimistic but plausible)",
                "The most likely outcome — your central forecast",
                "Things go wrong together (pessimistic but plausible)",
            ],
            "Typical assumptions move…": [
                "Volume ↑, price ↑, costs ↓",
                "Central estimates for every driver",
                "Volume ↓, price ↓, costs ↑",
            ],
        }
    )
    st.table(framework)

    with st.expander("🔑 Concept 1 — Scenario vs. sensitivity (the key difference)"):
        st.markdown(
            """
- **Sensitivity (5.1):** change **one** input, hold the rest constant → *"how sensitive is the result to
  price?"*
- **Scenario (this module):** change a **coherent set** of inputs together → *"what happens in a
  recession, where price, volume AND costs all move?"*

Scenarios are more realistic because drivers are **correlated** in the real world — they rarely move
independently.
"""
        )

    with st.expander("🔑 Concept 2 — Building internally-consistent scenarios"):
        st.markdown(
            """
Each scenario must tell a **coherent story**. In a 'recession' scenario, it wouldn't make sense to assume
falling volume *and* rising prices *and* falling costs. Good scenarios:
- Move drivers in **directions that fit the narrative**.
- Are **plausible** (not doomsday or fantasy).
- Are **distinct** enough to bracket the realistic range of outcomes.
"""
        )

    with st.expander("🔑 Concept 3 — The scenario manager"):
        st.markdown(
            """
A **scenario manager** stores several complete sets of inputs and lets you switch between them to compare
outputs instantly. In Excel this is the *Scenario Manager* tool; in a model it's usually a **switch cell**
that selects which column of assumptions feeds the calculations. It keeps all scenarios in one place and
makes comparison clean and auditable.
"""
        )

    with st.expander("🔑 Concept 4 — Probability-weighted expected value"):
        st.markdown(
            """
If you assign a **probability** to each scenario, you can compute an **expected value**:

$$E[\\text{NPV}] = \\sum_i p_i \\times \\text{NPV}_i \\quad \\text{where } \\sum_i p_i = 1$$

For example: 25% best (€1,000k) + 50% base (€400k) + 25% worst (−€200k) = **€400k expected NPV**. This
blends the scenarios into a single risk-adjusted figure — useful, but always show the *range* too, not
just the average.
"""
        )

    with st.expander("🔑 Concept 5 — Reading the results"):
        st.markdown(
            """
The most important questions scenario analysis answers:
- **How bad is the downside?** If the worst case is survivable, the risk may be acceptable.
- **Is the worst case a 'deal-breaker'?** A negative worst-case NPV that would threaten the business is a
  red flag even if the base case looks great.
- **How wide is the range?** A huge spread signals high uncertainty and the need for risk mitigation.
"""
        )

    st.success(
        "**Takeaway:** Scenario analysis changes a coherent set of assumptions together to model realistic "
        "futures (Base/Best/Worst). It shows the *range* of outcomes and the downside risk — and, weighted "
        "by probability, an expected value. Always look at the range, not just the average."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Base / Best / Worst for a project")
    st.markdown(
        "Base case: 100,000 units, price €20, variable cost €12, fixed €300k, capex €1.5m, 5-yr life, "
        "10% discount."
    )

    st.markdown("#### Step 1 — Define coherent scenarios (a set of assumptions each)")
    st.markdown(
        """
| Assumption | Worst | Base | Best |
|---|---|---|---|
| Volume | 80,000 | 100,000 | 120,000 |
| Price | €18 | €20 | €22 |
| Variable cost | €13 | €12 | €11 |
| Fixed cost | €330k | €300k | €280k |
"""
    )

    st.markdown("#### Step 2 — Run the model for each scenario")
    st.markdown(
        """
| Scenario | Annual cash flow | NPV @10% |
|---|---|---|
| **Worst** | 80,000 × (18−13) − 330,000 = €70,000 | **(€1,235,000)** |
| **Base** | 100,000 × (20−12) − 300,000 = €500,000 | **€395,000** |
| **Best** | 120,000 × (22−11) − 280,000 = €1,040,000 | **€2,442,000** |
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Worst-case NPV", "−€1,235,000", "Loss", delta_color="inverse")
    e2.metric("Base-case NPV", "+€395,000", "Value +")
    e3.metric("Best-case NPV", "+€2,442,000", "Strong +")

    st.markdown("#### Step 3 — Probability-weight (25% / 50% / 25%)")
    st.markdown(
        """
$$E[\\text{NPV}] = 0.25(-1{,}235) + 0.50(395) + 0.25(2{,}442) = \\mathbf{€499{,}000}$$
"""
    )

    st.info(
        "**Insight:** The base case looks healthy (+€395k), but scenario analysis reveals a **large "
        "downside**: in the worst case the project **loses €1.24m**. The expected NPV (~€499k) is positive, "
        "but the wide range (−€1.24m to +€2.44m) signals real uncertainty. **Recommendation: proceed only "
        "if the business can absorb the worst case** — and consider mitigations (e.g. price protection, "
        "flexible costs) to narrow the downside."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Scenario Manager")
    st.markdown(
        "Define the assumptions for each scenario, set probabilities, and compare NPVs side by side — plus "
        "a probability-weighted expected value."
    )

    st.markdown("##### 🔧 Fixed project parameters")
    f1, f2, f3 = st.columns(3)
    with f1:
        capex = st.number_input("Capex (€)", 0, 100_000_000, 1_500_000, 50_000)
    with f2:
        life = st.slider("Life (years)", 1, 20, 5, 1)
    with f3:
        discount = st.slider("Discount rate (%)", 1.0, 25.0, 10.0, 0.5)

    st.markdown("##### 📋 Scenario assumptions")
    st.caption("Enter a coherent set of assumptions for each scenario.")

    header = st.columns([0.24, 0.19, 0.19, 0.19, 0.19])
    header[0].markdown("**Driver**")
    header[1].markdown("**Worst**")
    header[2].markdown("**Base**")
    header[3].markdown("**Best**")
    header[4].markdown("**Your case**")

    def scenario_row(label, key, default_w, default_b, default_ba, default_y, fmt_step, mn, mx):
        cols = st.columns([0.24, 0.19, 0.19, 0.19, 0.19])
        cols[0].markdown(f"{label}")
        w = cols[1].number_input("w" + key, mn, mx, default_w, fmt_step, key="w" + key, label_visibility="collapsed")
        b = cols[2].number_input("b" + key, mn, mx, default_b, fmt_step, key="b" + key, label_visibility="collapsed")
        ba = cols[3].number_input("ba" + key, mn, mx, default_ba, fmt_step, key="ba" + key, label_visibility="collapsed")
        y = cols[4].number_input("y" + key, mn, mx, default_y, fmt_step, key="y" + key, label_visibility="collapsed")
        return w, b, ba, y

    vol_w, vol_b, vol_ba, vol_y = scenario_row("Volume (units)", "vol", 80_000, 100_000, 120_000, 100_000, 5_000, 0, 10_000_000)
    pr_w, pr_b, pr_ba, pr_y = scenario_row("Price (€)", "pr", 18.0, 20.0, 22.0, 20.0, 0.5, 0.0, 1000.0)
    vc_w, vc_b, vc_ba, vc_y = scenario_row("Variable cost (€)", "vc", 13.0, 12.0, 11.0, 12.0, 0.5, 0.0, 1000.0)
    fc_w, fc_b, fc_ba, fc_y = scenario_row("Fixed cost (€)", "fc", 330_000, 300_000, 280_000, 300_000, 10_000, 0, 50_000_000)

    st.markdown("##### 🎲 Scenario probabilities (should sum to 100%)")
    p1, p2, p3, p4 = st.columns(4)
    prob_w = p1.slider("Worst %", 0, 100, 25, 5)
    prob_b = p2.slider("Base %", 0, 100, 50, 5)
    prob_ba = p3.slider("Best %", 0, 100, 25, 5)
    prob_sum = prob_w + prob_b + prob_ba
    p4.metric("Sum", f"{prob_sum}%", "OK ✅" if prob_sum == 100 else "≠100% ⚠️",
              delta_color="normal" if prob_sum == 100 else "inverse")

    # compute NPVs
    npv_w = project_npv(vol_w, pr_w, vc_w, fc_w, capex, life, discount)
    npv_b = project_npv(vol_b, pr_b, vc_b, fc_b, capex, life, discount)
    npv_ba = project_npv(vol_ba, pr_ba, vc_ba, fc_ba, capex, life, discount)
    npv_y = project_npv(vol_y, pr_y, vc_y, fc_y, capex, life, discount)

    st.markdown("---")
    st.markdown("##### 📊 Results")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Worst NPV", money(npv_w), delta_color="inverse")
    k2.metric("Base NPV", money(npv_b))
    k3.metric("Best NPV", money(npv_ba))
    k4.metric("Your case NPV", money(npv_y))

    if prob_sum == 100:
        expected = (prob_w * npv_w + prob_b * npv_b + prob_ba * npv_ba) / 100
        st.metric("🎯 Probability-weighted Expected NPV", money(expected),
                  "Value +" if expected > 0 else "Value −",
                  delta_color="normal" if expected > 0 else "inverse")
    else:
        st.warning("⚠️ Probabilities don't sum to 100% — adjust them to compute an expected value.")
        expected = None

    # downside flag
    if npv_w < 0:
        st.error(
            f"🔻 **Downside risk:** the worst case loses {money(npv_w)}. Confirm the business could absorb "
            "this before proceeding — a negative worst case is a key risk signal."
        )
    else:
        st.success("✅ Even the worst case has a non-negative NPV — a robust, low-risk project.")

    chart = pd.DataFrame(
        {"NPV (€)": [npv_w, npv_b, npv_ba]},
        index=["Worst", "Base", "Best"],
    )
    st.markdown("##### 📈 Scenario comparison")
    st.bar_chart(chart)

    spread = npv_ba - npv_w
    st.caption(f"Range (Best − Worst) = **{money(spread)}** — the wider this is, the greater the uncertainty.")

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Survivable downside?** Adjust the worst case until its NPV is just break-even — how much protection
   would that require?
2. **Probability shift:** Raise the worst-case probability to 50%. What happens to the expected NPV?
"""
        )
    with e2:
        st.markdown(
            """
3. **Narrow the range:** Make the scenarios closer together (less extreme). Notice how the range shrinks.
4. **Your own case:** Use the 'Your case' column to model a specific mitigation (e.g. lock in price).
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Board-ready Base / Best / Worst on a Capex case", expanded=True):
        st.markdown(
            """
**Situation:** A board wouldn't approve a major investment on a single-point NPV alone.

**How scenario analysis helped:** Presenting **Base / Best / Worst** NPVs — with a coherent story behind
each — showed the board the full range of outcomes and, crucially, that the **worst case was survivable**.
That gave them the confidence to approve.

**Why it matters:** Boards approve *risk-aware* cases. A range with a bounded downside is far more
convincing than a single optimistic number.

**Lesson:** Always present investment cases as scenarios, not a single figure — and highlight the downside.
"""
        )

    with st.expander("Case B — The worst case that killed a deal"):
        st.markdown(
            """
**Situation:** A project had an attractive base-case NPV, so it looked like an easy approval.

**What scenario analysis revealed:** In a plausible **worst case** (demand slump + cost inflation
together), the project generated large losses that could have threatened the division's viability.

**Why it matters:** The correlated downside — invisible in a base case or one-at-a-time sensitivity — was
a genuine deal-breaker.

**Lesson:** A healthy base case isn't enough; a catastrophic, plausible worst case can (and should) stop a project.
"""
        )

    with st.expander("Case C — Probability-weighting competing projects"):
        st.markdown(
            """
**Situation:** Two projects had similar base-case NPVs but very different risk profiles.

**How scenario analysis helped:** Assigning probabilities to each project's scenarios produced
**expected NPVs** and revealed that one project had a much tighter, safer range while the other was a
high-variance gamble.

**Why it matters:** Expected value plus range let management choose based on **risk appetite**, not just
the headline base case.

**Lesson:** Probability-weighted scenarios help compare projects on a risk-adjusted basis.
"""
        )

    st.info(
        "🔗 **Pattern:** Scenario analysis reframes a decision from 'what's the number?' to 'what's the "
        "*range*, how bad is the downside, and can we live with it?' — the questions that actually drive "
        "good risk decisions."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_52"):
        q1 = st.radio(
            "**1.** Scenario analysis differs from sensitivity analysis because it:",
            [
                "Changes only one input at a time",
                "Changes a coherent SET of inputs together to represent a plausible future",
                "Ignores all assumptions",
                "Only varies the discount rate",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** In a 'worst case' scenario for a typical project, you would usually assume:",
            [
                "Higher volume, higher price, lower costs",
                "Lower volume, lower price, higher costs",
                "No change from the base case",
                "Only a change in the tax rate",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** A scenario must be:",
            [
                "As extreme as possible",
                "Internally consistent — the assumptions should fit a coherent story",
                "Identical to the base case",
                "Based on a single input",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** The probability-weighted expected NPV is calculated by:",
            [
                "Averaging the inputs",
                "Summing each scenario's NPV × its probability (probabilities summing to 100%)",
                "Taking the highest scenario NPV",
                "Ignoring probabilities",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The most important thing scenario analysis reveals is:",
            [
                "The exact future outcome",
                "The range of outcomes and how bad the downside could be",
                "The company's tax rate",
                "The depreciation method",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Changes a coherent SET of inputs together to represent a plausible future"),
            "2": (q2, "Lower volume, lower price, higher costs"),
            "3": (q3, "Internally consistent — the assumptions should fit a coherent story"),
            "4": (q4, "Summing each scenario's NPV × its probability (probabilities summing to 100%)"),
            "5": (q5, "The range of outcomes and how bad the downside could be"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered scenario analysis! On to Module 5.3 (Monte Carlo Simulation). 🎉")
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
    f"Applied Financial Models · Module 5.2 Scenario Analysis · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
