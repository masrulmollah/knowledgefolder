"""
================================================================================
APPLIED FINANCIAL MODELS
Module 5.1 — SENSITIVITY ANALYSIS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to test how sensitive a model's output is to its inputs: one-way and two-way
data tables and tornado charts.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (one-way table, two-way table, tornado chart)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_5_1_Sensitivity_Analysis.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="5.1 Sensitivity Analysis — Applied Financial Models",
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
    """
    Simple project NPV: annual operating cash flow discounted over `life`,
    less the upfront capex. Used as the base model for sensitivity analysis.
    """
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
**Module 5.1 — Sensitivity Analysis**

🟡 *Intermediate*

**You will learn to:**
- Flex one input and read the impact
- Build one-way & two-way data tables
- Rank drivers with a tornado chart
- Find the value-critical assumptions
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build one-way and two-way "
    "sensitivity tables and a tornado chart."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎲 5.1 · Sensitivity Analysis")
st.markdown(
    """
Every model rests on **assumptions** — and every assumption could be wrong. **Sensitivity analysis** asks
the vital question: *"How much does my answer change if an input changes?"* It flexes **one input at a
time** to reveal which assumptions the result is most **sensitive** to — the ones worth worrying about.

This opens Part 5 (risk & uncertainty). Master it and you'll never again present a single-point answer as
if it were certain — you'll show *what drives it* and *how robust it is*.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "5.1")
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
### What is sensitivity analysis?
Sensitivity analysis measures how an **output** (e.g. NPV, profit) responds when you change **one input**
while holding everything else constant. It answers *"which assumptions matter most?"* and *"how wrong can
I be before the decision changes?"*
"""
    )

    st.markdown("### The three main tools")
    tools = pd.DataFrame(
        {
            "Tool": ["One-way data table", "Two-way data table", "Tornado chart"],
            "What it does": [
                "Varies ONE input across a range; shows the output at each level",
                "Varies TWO inputs simultaneously in a grid",
                "Ranks inputs by their impact on the output (biggest at the top)",
            ],
            "Best for": [
                "Seeing how one driver moves the result",
                "Seeing the interaction of two key drivers",
                "Spotting the highest-impact drivers at a glance",
            ],
        }
    )
    st.table(tools)

    with st.expander("🔑 Concept 1 — One-way sensitivity (one input at a time)"):
        st.markdown(
            """
Pick one input (say, the discount rate), vary it across a range (e.g. 6% → 14%), and record the output
(NPV) at each level. This shows **how steeply** the result responds to that one driver. A steep response =
high sensitivity = an assumption you must get right.
"""
        )

    with st.expander("🔑 Concept 2 — Two-way data tables"):
        st.markdown(
            """
Real outcomes depend on several drivers at once. A **two-way table** varies **two** inputs in a grid — for
example, NPV at every combination of *sales volume* (rows) and *discount rate* (columns). It reveals
**interactions** and lets you see the combinations where the project turns from value-creating to
value-destroying.
"""
        )

    with st.expander("🔑 Concept 3 — Tornado charts (ranking the drivers)"):
        st.markdown(
            """
A **tornado chart** flexes each input by the same amount (e.g. ±10%) and plots the resulting swing in the
output as a horizontal bar. Bars are sorted **longest at the top**, so the chart looks like a tornado. The
top bars are the drivers your result is **most sensitive** to — where you should focus data-gathering and
risk-management effort.
"""
        )

    with st.expander("🔑 Concept 4 — Sensitivity vs. scenario vs. simulation"):
        st.markdown(
            """
- **Sensitivity (this module):** change **one** input at a time — isolates each driver's impact.
- **Scenario analysis (5.2):** change a **coherent set** of inputs together (e.g. a 'recession' case).
- **Monte Carlo (5.3):** vary **many** inputs randomly across probability distributions to get a full
  range of outcomes.

Start with sensitivity to find what matters, then use scenarios and simulation to explore combined risk.
"""
        )

    with st.expander("🔑 Concept 5 — Why it matters"):
        st.markdown(
            """
Sensitivity analysis turns a single, fragile number into a **robust, defensible** analysis. It:
- Identifies the **value-critical** assumptions (focus effort there).
- Reveals **break-even** points (how far can an input move before the decision flips?).
- Builds **credibility** with decision-makers who (rightly) distrust single-point forecasts.
"""
        )

    st.success(
        "**Takeaway:** Sensitivity analysis flexes one input at a time to show which assumptions your answer "
        "depends on most. One-way tables show a single driver, two-way tables show interactions, and tornado "
        "charts rank them — so you can focus on what really moves the result."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Sensitivity of a project's NPV")
    st.markdown(
        "Base case: 100,000 units, price €20, variable cost €12, fixed cost €300k, capex €1.5m, 5-year "
        "life, 10% discount. **Base NPV ≈ €394k.**"
    )

    st.markdown("#### One-way sensitivity — discount rate")
    st.markdown(
        """
| Discount rate | NPV |
|---|---|
| 6% | €606,000 |
| 8% | €496,000 |
| **10% (base)** | **€394,000** |
| 12% | €301,000 |
| 14% | €215,000 |

*As the discount rate rises, NPV falls — but the project stays positive across this range (robust to rate).*
"""
    )

    st.markdown("#### One-way sensitivity — sales price")
    st.markdown(
        """
| Price | NPV |
|---|---|
| €18 (−10%) | (€364,000) |
| €19 (−5%) | €15,000 |
| **€20 (base)** | **€394,000** |
| €21 (+5%) | €773,000 |
| €22 (+10%) | €1,152,000 |

*A 10% price fall turns the NPV **negative** — the project is highly sensitive to price.*
"""
    )

    st.markdown("#### The tornado chart (±10% on each driver)")
    st.markdown(
        """
| Driver | NPV swing (±10%) | Rank |
|---|---|---|
| **Price** | ±€758,000 | 1 (most sensitive) |
| **Variable cost** | ∓€455,000 | 2 |
| **Volume** | ±€303,000 | 3 |
| Fixed cost | ∓€114,000 | 4 |
| Discount rate | ±€90,000 | 5 (least) |
"""
    )

    st.info(
        "**Insight:** The tornado chart makes the priority obvious — **price is the value-critical driver** "
        "(a ±10% move swings NPV by ~€758k and can flip the decision), followed by variable cost. The "
        "discount rate, often over-debated, matters least here. **Focus effort on nailing the price "
        "assumption and protecting margins** — that's where the risk really lives."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Sensitivity Lab")
    st.markdown("Set the base case, then explore one-way tables, a two-way table, and a tornado chart.")

    st.markdown("##### 🎯 Base-case assumptions")
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        volume = st.number_input("Volume (units)", 1_000, 10_000_000, 100_000, 5_000)
        capex = st.number_input("Capex (€)", 0, 100_000_000, 1_500_000, 50_000)
    with b2:
        price = st.number_input("Price (€/unit)", 0.1, 1000.0, 20.0, 0.5)
        life = st.slider("Life (years)", 1, 20, 5, 1)
    with b3:
        var_cost = st.number_input("Variable cost (€/unit)", 0.0, 1000.0, 12.0, 0.5)
        discount = st.slider("Discount rate (%)", 1.0, 25.0, 10.0, 0.5)
    with b4:
        fixed_cost = st.number_input("Fixed cost (€)", 0, 50_000_000, 300_000, 25_000)

    base = project_npv(volume, price, var_cost, fixed_cost, capex, life, discount)
    st.metric("Base-case NPV", money(base),
              "Value +" if base > 0 else "Value −",
              delta_color="normal" if base > 0 else "inverse")

    st.markdown("---")

    # ---- One-way ----
    st.markdown("##### 1️⃣ One-Way Sensitivity")
    driver = st.selectbox(
        "Vary one driver:",
        ["Price", "Variable cost", "Volume", "Fixed cost", "Discount rate"],
    )
    pct_range = st.slider("Range (± %)", 5, 50, 20, 5)

    steps = [-pct_range, -pct_range / 2, 0, pct_range / 2, pct_range]
    rows = []
    for p in steps:
        f = 1 + p / 100
        if driver == "Price":
            npv_v = project_npv(volume, price * f, var_cost, fixed_cost, capex, life, discount)
            label = money(price * f, dp=2)
        elif driver == "Variable cost":
            npv_v = project_npv(volume, price, var_cost * f, fixed_cost, capex, life, discount)
            label = money(var_cost * f, dp=2)
        elif driver == "Volume":
            npv_v = project_npv(volume * f, price, var_cost, fixed_cost, capex, life, discount)
            label = f"{volume * f:,.0f}"
        elif driver == "Fixed cost":
            npv_v = project_npv(volume, price, var_cost, fixed_cost * f, capex, life, discount)
            label = money(fixed_cost * f)
        else:  # discount rate — additive in points
            dr = discount + p / 100 * discount
            npv_v = project_npv(volume, price, var_cost, fixed_cost, capex, life, dr)
            label = f"{dr:.1f}%"
        rows.append({"Change": f"{p:+.0f}%", f"{driver} value": label, "NPV": npv_v})
    one_way = pd.DataFrame(rows)
    show = one_way.copy()
    show["NPV"] = show["NPV"].map(money)
    c_tbl, c_chart = st.columns([0.5, 0.5])
    with c_tbl:
        st.dataframe(show, use_container_width=True, hide_index=True)
    with c_chart:
        chart_df = one_way.set_index("Change")[["NPV"]]
        st.line_chart(chart_df)

    st.markdown("---")

    # ---- Two-way ----
    st.markdown("##### 2️⃣ Two-Way Data Table — Volume × Price")
    st.caption("NPV at every combination of volume (rows) and price (columns). Green-ish = positive.")
    vol_steps = [volume * (1 + p / 100) for p in [-20, -10, 0, 10, 20]]
    price_steps = [price * (1 + p / 100) for p in [-10, -5, 0, 5, 10]]
    grid = []
    for v in vol_steps:
        row = {}
        row["Volume"] = f"{v:,.0f}"
        for pr in price_steps:
            row[money(pr, dp=2)] = project_npv(v, pr, var_cost, fixed_cost, capex, life, discount)
        grid.append(row)
    two_way = pd.DataFrame(grid).set_index("Volume")
    two_way_disp = two_way.apply(lambda col: col.map(money))
    st.dataframe(two_way_disp, use_container_width=True)

    st.markdown("---")

    # ---- Tornado ----
    st.markdown("##### 3️⃣ Tornado Chart — driver impact (± chosen %)")
    swing_pct = st.slider("Flex each driver by ± (%)", 5, 30, 10, 5, key="tornado_pct")
    f = swing_pct / 100
    drivers = {
        "Price": (project_npv(volume, price * (1 + f), var_cost, fixed_cost, capex, life, discount),
                  project_npv(volume, price * (1 - f), var_cost, fixed_cost, capex, life, discount)),
        "Variable cost": (project_npv(volume, price, var_cost * (1 - f), fixed_cost, capex, life, discount),
                          project_npv(volume, price, var_cost * (1 + f), fixed_cost, capex, life, discount)),
        "Volume": (project_npv(volume * (1 + f), price, var_cost, fixed_cost, capex, life, discount),
                   project_npv(volume * (1 - f), price, var_cost, fixed_cost, capex, life, discount)),
        "Fixed cost": (project_npv(volume, price, var_cost, fixed_cost * (1 - f), capex, life, discount),
                       project_npv(volume, price, var_cost, fixed_cost * (1 + f), capex, life, discount)),
        "Discount rate": (project_npv(volume, price, var_cost, fixed_cost, capex, life, discount * (1 - f)),
                          project_npv(volume, price, var_cost, fixed_cost, capex, life, discount * (1 + f))),
    }
    swings = {k: abs(hi - lo) for k, (hi, lo) in drivers.items()}
    tor = pd.DataFrame({"NPV swing (€)": swings.values()}, index=list(swings.keys()))
    tor = tor.sort_values("NPV swing (€)", ascending=True)  # smallest first so chart reads top=biggest
    st.bar_chart(tor)

    top_driver = max(swings, key=swings.get)
    st.info(
        f"🎯 **Most sensitive driver: {top_driver}** — a ±{swing_pct}% move swings NPV by "
        f"**{money(swings[top_driver])}**. Focus your data-gathering and risk management here."
    )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Find the break-even:** In the one-way table for Price, find the % fall that makes NPV zero.
2. **Danger cell:** In the two-way table, find the volume/price combination where NPV turns negative.
"""
        )
    with e2:
        st.markdown(
            """
3. **Re-rank the tornado:** Raise fixed cost to €2m. Does it climb the tornado ranking?
4. **Robustness check:** Which driver could move ±20% and still leave NPV positive?
"""
        )

    st.download_button(
        "⬇️ Download one-way sensitivity (CSV)",
        one_way.to_csv(index=False).encode("utf-8"),
        "sensitivity_one_way.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Stress-testing a Capex business case", expanded=True):
        st.markdown(
            """
**Situation:** A €6m automation case showed a positive NPV, but the board wanted to know how robust it was.

**How sensitivity analysis helped:** A tornado chart flexing each assumption ±10% revealed the NPV was
most sensitive to the **savings level** and the **discount rate**. A one-way table then showed the savings
could fall ~15% before the NPV turned negative — the project's break-even margin of safety.

**Why it matters:** It transformed "the NPV is €402k" into "the NPV is €402k, and it stays positive unless
savings fall more than 15%" — a far more useful, honest statement for a decision.

**Lesson:** Always pair a headline NPV with a sensitivity analysis showing how much room for error exists.
"""
        )

    with st.expander("Case B — The tornado chart that refocused the team"):
        st.markdown(
            """
**Situation:** A project team was spending weeks refining the discount-rate assumption.

**What the tornado chart revealed:** The result was far more sensitive to **sales price** and **volume**
than to the discount rate. The team had been polishing the least important input.

**Why it matters:** Analyst time is scarce; a tornado chart directs it to the assumptions that actually
move the answer.

**Lesson:** Use a tornado chart *early* to prioritise where to spend your analytical effort.
"""
        )

    with st.expander("Case C — The two-way table that framed a pricing decision"):
        st.markdown(
            """
**Situation:** Management debated a price cut to win volume, unsure of the net effect on value.

**How the two-way table helped:** A grid of NPV across combinations of **price** and **volume** showed
exactly how much extra volume was needed to offset each price cut — and which combinations still created
value.

**Why it matters:** It turned a heated qualitative debate into a clear, data-driven trade-off map.

**Lesson:** Two-way tables are powerful for decisions where two drivers move together (like price and volume).
"""
        )

    st.info(
        "🔗 **Pattern:** Sensitivity analysis converts a fragile single number into a robust, risk-aware "
        "decision. It shows what matters (tornado), how much room for error exists (one-way), and how "
        "drivers interact (two-way)."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_51"):
        q1 = st.radio(
            "**1.** Sensitivity analysis measures how an output changes when you:",
            [
                "Change all inputs randomly at once",
                "Change one input at a time, holding others constant",
                "Ignore the assumptions",
                "Only change the tax rate",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** A one-way data table:",
            [
                "Varies two inputs in a grid",
                "Varies one input across a range and shows the output at each level",
                "Ranks all inputs by impact",
                "Removes the discount rate",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** A tornado chart is used to:",
            [
                "Show cash flows over time",
                "Rank inputs by their impact on the output (biggest at the top)",
                "Calculate depreciation",
                "Display the balance sheet",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A two-way data table is most useful for:",
            [
                "Seeing how ONE driver affects the result",
                "Seeing how TWO drivers interact to affect the result",
                "Ranking every input",
                "Replacing the NPV calculation",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The main value of sensitivity analysis is that it:",
            [
                "Guarantees the forecast is correct",
                "Identifies which assumptions the result depends on most, and how much room for error exists",
                "Eliminates all risk",
                "Replaces the need for a discount rate",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Change one input at a time, holding others constant"),
            "2": (q2, "Varies one input across a range and shows the output at each level"),
            "3": (q3, "Rank inputs by their impact on the output (biggest at the top)"),
            "4": (q4, "Seeing how TWO drivers interact to affect the result"),
            "5": (q5, "Identifies which assumptions the result depends on most, and how much room for error exists"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered sensitivity analysis! On to Module 5.2 (Scenario Analysis). 🎉")
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
    f"Applied Financial Models · Module 5.1 Sensitivity Analysis · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
