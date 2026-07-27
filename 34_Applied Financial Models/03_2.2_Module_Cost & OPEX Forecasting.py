"""
================================================================================
APPLIED FINANCIAL MODELS
Module 2.2 — COST & OPEX FORECASTING
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to forecast costs: the fixed/variable split, cost inflation, step costs,
and the resulting operating leverage.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live fixed/variable/step cost model)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_2_2_Cost_and_OPEX_Forecasting.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="2.2 Cost & OPEX Forecasting — Applied Financial Models",
    layout="wide",
    page_icon="📊",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def build_cost_forecast(
    units_y1, vol_growth, price, price_growth,
    var_cost_per_unit, var_inflation,
    fixed_cost_y1, fixed_inflation,
    step_threshold, step_cost, years,
):
    """
    Build a multi-year cost & margin forecast with fixed, variable and step costs.
    Returns a DataFrame with line items as rows and years as columns.
    """
    rows = {
        "Volume (units)": [], "Revenue": [],
        "Variable cost": [], "Fixed cost": [], "Step cost": [], "Total cost": [],
        "Operating profit": [], "Operating margin %": [],
    }
    units = units_y1
    p = price
    vcu = var_cost_per_unit
    fixed = fixed_cost_y1

    for y in range(years):
        if y > 0:
            units *= (1 + vol_growth / 100)
            p *= (1 + price_growth / 100)
            vcu *= (1 + var_inflation / 100)
            fixed *= (1 + fixed_inflation / 100)

        revenue = units * p
        var_cost = units * vcu
        # step cost: number of capacity blocks needed
        blocks = 0
        if step_threshold > 0:
            import math
            blocks = math.ceil(units / step_threshold) - 1  # first block included in fixed
            blocks = max(blocks, 0)
        step = blocks * step_cost
        total_cost = var_cost + fixed + step
        op_profit = revenue - total_cost
        op_margin = (op_profit / revenue * 100) if revenue else 0

        rows["Volume (units)"].append(units)
        rows["Revenue"].append(revenue)
        rows["Variable cost"].append(-var_cost)
        rows["Fixed cost"].append(-fixed)
        rows["Step cost"].append(-step)
        rows["Total cost"].append(-total_cost)
        rows["Operating profit"].append(op_profit)
        rows["Operating margin %"].append(op_margin)

    idx = [f"Year {y+1}" for y in range(years)]
    return pd.DataFrame(rows, index=idx).T


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 2 · Forecasting & Budgeting Models")
st.sidebar.markdown(
    """
**Module 2.2 — Cost & OPEX Forecasting**

🟡 *Intermediate*

**You will learn to:**
- Split costs into fixed vs. variable
- Apply cost inflation correctly
- Model step (capacity) costs
- Understand operating leverage
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live cost model and "
    "watch operating leverage in action as volume grows."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("📊 2.2 · Cost & OPEX Forecasting")
st.markdown(
    """
If revenue is the top line, **costs decide how much of it you keep**. Forecasting costs well is what
turns a revenue forecast into a credible profit forecast. The key skill is understanding **how each cost
behaves** — does it move with volume, stay flat, or jump in steps?

This module covers the fixed/variable split, cost inflation, step costs, and the powerful concept of
**operating leverage** — why profits can grow faster than revenue.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "2.2")
c2.metric("Part", "2 — Forecasting")
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
### The three cost behaviours
The foundation of cost forecasting is classifying every cost by *how it behaves* as volume changes.
"""
    )

    behaviours = pd.DataFrame(
        {
            "Cost type": ["Variable", "Fixed", "Step (semi-fixed)"],
            "Behaviour as volume rises": [
                "Rises in direct proportion to volume",
                "Stays flat regardless of volume",
                "Flat within a range, then jumps at a capacity threshold",
            ],
            "How to model it": [
                "Cost per unit × volume (or % of revenue)",
                "Absolute € amount, grown only by inflation",
                "Fixed block that adds another block past each threshold",
            ],
            "Examples": [
                "Raw materials, packaging, sales commission",
                "Rent, core salaries, insurance, software licences",
                "A new production line, extra shift, new warehouse",
            ],
        }
    )
    st.table(behaviours)

    st.markdown(
        """
### The core cost equation
"""
    )
    st.latex(r"\text{Total Cost} = \underbrace{(\text{Cost per unit} \times \text{Volume})}_{\text{variable}} + \underbrace{\text{Fixed Cost}}_{\text{flat}} + \underbrace{\text{Step Cost}}_{\text{capacity jumps}}")

    with st.expander("🔑 Concept 1 — Fixed vs. variable (the most important split)"):
        st.markdown(
            """
- **Variable costs** scale with activity — model as **cost per unit** or **% of revenue**. They stay a
  roughly constant *percentage* as volume changes.
- **Fixed costs** don't move with volume — model as an **absolute €** amount, grown only by inflation.
  As volume rises, fixed cost *per unit* falls (spreading over more units).

Misclassifying a fixed cost as variable (or vice-versa) is one of the most common forecasting errors —
it makes the model react wrongly when you flex volume.
"""
        )

    with st.expander("🔑 Concept 2 — Cost inflation (don't forget it)"):
        st.markdown(
            """
Even flat costs rise over time due to inflation. Apply an inflation rate to each cost line:

$$\\text{Cost}_{t} = \\text{Cost}_{t-1} \\times (1 + \\text{inflation})$$

Different cost lines can have **different inflation rates** — wages, energy, and raw materials often
diverge sharply. Modeling a single blended rate is convenient but can mask real pressure points.
"""
        )

    with st.expander("🔑 Concept 3 — Step costs (the capacity jump)"):
        st.markdown(
            """
Some costs are fixed *within a range* but **jump** when you cross a capacity threshold — a new machine,
an extra shift, another warehouse. These **step costs** matter enormously for growth planning: a small
volume increase can trigger a large cost jump that temporarily crushes margins.

Model them by defining a **capacity per block** and adding another block's cost each time volume crosses
a threshold.
"""
        )

    with st.expander("🔑 Concept 4 — Operating leverage (why profit outpaces revenue)"):
        st.markdown(
            """
Because fixed costs don't rise with volume, each extra unit contributes its full **contribution margin**
(price − variable cost) to profit. This is **operating leverage**:

$$\\text{Contribution per unit} = \\text{Price} - \\text{Variable cost per unit}$$

- **High fixed costs** → high operating leverage → profits swing sharply with volume (great on the way
  up, painful on the way down).
- **Low fixed costs** → profits track revenue more gently.

Understanding your leverage is essential for both growth planning and risk assessment.
"""
        )

    st.success(
        "**Takeaway:** Classify every cost as fixed, variable, or step; grow each by the right inflation; "
        "and understand your operating leverage. That's what turns a revenue forecast into a reliable "
        "profit forecast."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Forecasting CleanSoap's costs")
    st.markdown("Building the cost side of our fictional product, then watching operating leverage appear.")

    st.markdown("#### Step 1 — Classify the costs")
    st.markdown(
        """
| Cost | Type | Amount |
|---|---|---|
| Raw materials & packaging | Variable | €1.20 / unit |
| Sales commission | Variable | €0.10 / unit |
| Factory rent & core salaries | Fixed | €300,000 |
| New production line (if > 1.2m units) | Step | €150,000 per block |
"""
    )

    st.markdown("#### Step 2 — Year 1 at 1,000,000 units")
    st.markdown(
        """
| Line | Calculation | € |
|---|---|---|
| Revenue | 1,000,000 × €2.00 | 2,000,000 |
| Variable cost | 1,000,000 × €1.30 | (1,300,000) |
| Fixed cost | | (300,000) |
| Step cost | below 1.2m threshold | 0 |
| **Operating profit** | | **€400,000** |
| Operating margin | 400k / 2,000k | **20.0%** |
"""
    )

    st.markdown("#### Step 3 — Year 2 at 1,150,000 units (operating leverage)")
    st.markdown(
        """
| Line | Calculation | € |
|---|---|---|
| Revenue | 1,150,000 × €2.00 | 2,300,000 |
| Variable cost | 1,150,000 × €1.30 | (1,495,000) |
| Fixed cost | unchanged | (300,000) |
| **Operating profit** | | **€505,000** |
| Operating margin | 505k / 2,300k | **22.0%** |
"""
    )

    st.info(
        "**Operating leverage in action:** Volume rose 15% but operating profit rose **26%** (€400k → "
        "€505k), and margin expanded from 20% → 22%. Why? The €300k fixed cost was spread over more units. "
        "**This is the payoff of operating leverage** — but note it reverses on the way down."
    )

    st.warning(
        "⚠️ **The step-cost trap:** If Year 2 volume had hit 1,250,000 (crossing the 1.2m threshold), a "
        "€150,000 step cost would kick in — temporarily wiping out much of the leverage benefit until "
        "volume grows into the new capacity."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Build a Cost Model & See Operating Leverage")
    st.markdown(
        "Set the cost structure on the left. Watch total costs, operating profit and margin evolve — and "
        "see step costs kick in as volume crosses capacity thresholds."
    )

    left, right = st.columns([0.32, 0.68])

    with left:
        st.markdown("##### 📈 Volume & price")
        units_y1 = st.number_input("Year-1 volume (units)", 100_000, 20_000_000, 1_000_000, 50_000)
        vol_growth = st.slider("Volume growth (%)", -10.0, 30.0, 12.0, 1.0)
        price = st.number_input("Price per unit (€)", 0.10, 100.0, 2.0, 0.10)
        price_growth = st.slider("Price growth (%)", -5.0, 15.0, 3.0, 0.5)

        st.markdown("##### 🔧 Variable costs")
        vcu = st.number_input("Variable cost per unit (€)", 0.01, 90.0, 1.30, 0.05)
        var_inflation = st.slider("Variable cost inflation (%)", 0.0, 15.0, 4.0, 0.5)

        st.markdown("##### 🏢 Fixed costs")
        fixed = st.number_input("Fixed cost — Year 1 (€)", 0, 10_000_000, 300_000, 25_000)
        fixed_inflation = st.slider("Fixed cost inflation (%)", 0.0, 15.0, 3.0, 0.5)

        st.markdown("##### 🪜 Step cost")
        step_threshold = st.number_input("Capacity per block (units)", 0, 20_000_000, 1_200_000, 50_000,
                                         help="Set 0 to disable step costs")
        step_cost = st.number_input("Cost per extra block (€)", 0, 5_000_000, 150_000, 25_000)

        years = st.slider("Forecast horizon (years)", 3, 10, 5, 1)

    with right:
        df = build_cost_forecast(
            units_y1, vol_growth, price, price_growth,
            vcu, var_inflation, fixed, fixed_inflation,
            step_threshold, step_cost, years,
        )

        op1 = df.loc["Operating profit", "Year 1"]
        opN = df.loc["Operating profit", f"Year {years}"]
        m1 = df.loc["Operating margin %", "Year 1"]
        mN = df.loc["Operating margin %", f"Year {years}"]
        rev1 = df.loc["Revenue", "Year 1"]
        revN = df.loc["Revenue", f"Year {years}"]

        rev_growth = (revN / rev1 - 1) * 100 if rev1 else 0
        profit_growth = (opN / op1 - 1) * 100 if op1 else 0

        k1, k2, k3 = st.columns(3)
        k1.metric(f"Revenue (Yr {years})", money(revN), f"{rev_growth:,.0f}% vs Y1")
        k2.metric(f"Operating profit (Yr {years})", money(opN),
                  f"{profit_growth:,.0f}% vs Y1" if op1 else None)
        k3.metric(f"Operating margin (Yr {years})", f"{mN:,.1f}%", f"{mN - m1:+.1f} pp vs Y1")

        # operating leverage insight
        if op1 and profit_growth > rev_growth + 1:
            st.success(
                f"✅ **Operating leverage is working:** profit grew {profit_growth:,.0f}% vs. revenue "
                f"{rev_growth:,.0f}% — margin expanded because fixed costs were spread over more volume."
            )
        elif op1 and profit_growth < rev_growth - 1:
            st.warning(
                f"⚠️ **Margins compressed:** profit grew only {profit_growth:,.0f}% vs. revenue "
                f"{rev_growth:,.0f}%. Check cost inflation or a step-cost jump eating the leverage benefit."
            )

        # detect step cost jumps
        step_row = df.loc["Step cost"]
        if (step_row < 0).any():
            first_step_year = next((i + 1 for i, v in enumerate(step_row) if v < 0), None)
            st.info(
                f"🪜 **Step cost triggered in Year {first_step_year}** — volume crossed a capacity block, "
                f"adding {money(step_cost)}. Notice the temporary margin dip that year."
            )

        st.markdown("##### 📄 Cost & Profit Forecast")

        def fmt(row):
            if row.name == "Operating margin %":
                return row.map(lambda v: f"{v:,.1f}%")
            if row.name == "Volume (units)":
                return row.map(lambda v: f"{v:,.0f}")
            return row.map(money)

        st.dataframe(df.apply(fmt, axis=1), use_container_width=True)

        st.markdown("##### 📈 Revenue vs. Total Cost vs. Operating Profit")
        chart_df = df.loc[["Revenue", "Total cost", "Operating profit"]].T
        # total cost stored negative — flip for chart readability
        chart_df["Total cost"] = -chart_df["Total cost"]
        st.line_chart(chart_df)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Leverage up:** Raise fixed cost to €800k and volume growth to 20%. See profit grow much faster than revenue.
2. **Step shock:** Set capacity per block to 1,100,000. Watch a step cost hit early and dent margins.
"""
        )
    with e2:
        st.markdown(
            """
3. **Inflation squeeze:** Push variable cost inflation to 12% while price growth stays at 3%. Watch margins erode.
4. **De-leverage risk:** Set volume growth to −10%. See how high fixed costs punish profit on the way down.
"""
        )

    st.download_button(
        "⬇️ Download this cost forecast (CSV)",
        df.to_csv().encode("utf-8"),
        "cost_opex_forecast.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The high-fixed-cost factory (operating leverage)", expanded=True):
        st.markdown(
            """
**Situation:** A manufacturer with heavy fixed costs (plant, core workforce) saw volumes rise 10%.

**What the cost model revealed:** Because fixed costs didn't move, that 10% volume gain flowed largely
to profit — operating profit jumped ~20% and margins expanded. The reverse was equally true: a 10% volume
*fall* would have hit profit twice as hard.

**Why it matters:** High operating leverage magnifies both upside and downside — a critical risk to flag
in any forecast.

**Lesson:** In capital-intensive businesses, volume is the master variable — model fixed costs carefully
and stress-test the downside.
"""
        )

    with st.expander("Case B — The step cost that surprised the board"):
        st.markdown(
            """
**Situation:** A growing business forecast smooth margin expansion — until actual results showed a sudden
margin drop in the growth year.

**What the cost model (should have) revealed:** Crossing a capacity threshold triggered a **step cost** —
a new production line and shift — that a simple % -of-revenue cost model had completely missed.

**Why it matters:** Step costs break the assumption that costs scale smoothly. Ignoring them makes
growth-year forecasts look better than reality.

**Lesson:** Always model capacity thresholds explicitly — smooth cost curves lie about growth years.
"""
        )

    with st.expander("Case C — Divergent inflation (wages vs. energy vs. materials)"):
        st.markdown(
            """
**Situation:** A single blended 3% inflation assumption made a forecast look comfortable — but energy
costs were rising 15% and wages 8%.

**What the cost model revealed:** Splitting inflation by cost line exposed a serious margin threat that
the blended rate had hidden. Management could then target the specific pressure points (energy hedging,
efficiency).

**Why it matters:** Costs don't inflate uniformly; a blended rate can mask real risk.

**Lesson:** Where cost lines face very different inflation, model them separately.
"""
        )

    st.info(
        "🔗 **Pattern:** Cost forecasting is about *behaviour*, not just amounts. Get the fixed/variable/step "
        "classification and inflation right, and your profit forecast becomes genuinely decision-useful."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_22"):
        q1 = st.radio(
            "**1.** A variable cost is best modelled as:",
            [
                "A flat € amount every year",
                "Cost per unit × volume (or % of revenue)",
                "A one-off capacity jump",
                "Depreciation ÷ useful life",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** As volume rises, a FIXED cost:",
            [
                "Rises in proportion to volume",
                "Stays flat in total, so falls per unit",
                "Doubles every year",
                "Becomes a variable cost",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** A step cost is one that:",
            [
                "Changes with every single unit",
                "Is flat within a range, then jumps when a capacity threshold is crossed",
                "Never changes under any circumstances",
                "Is always equal to revenue",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Operating leverage explains why:",
            [
                "Taxes fall as profit rises",
                "Profit can grow faster than revenue because fixed costs are spread over more units",
                "Variable costs disappear at high volume",
                "Depreciation is a non-cash cost",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Why model inflation separately for different cost lines?",
            [
                "It makes the model shorter",
                "Because wages, energy and materials often inflate at very different rates, and a blended rate can hide risk",
                "Because tax law requires it",
                "Because fixed costs never inflate",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Cost per unit × volume (or % of revenue)"),
            "2": (q2, "Stays flat in total, so falls per unit"),
            "3": (q3, "Is flat within a range, then jumps when a capacity threshold is crossed"),
            "4": (q4, "Profit can grow faster than revenue because fixed costs are spread over more units"),
            "5": (q5, "Because wages, energy and materials often inflate at very different rates, and a blended rate can hide risk"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered cost & OPEX forecasting! On to Module 2.3 (Budget vs. Actual). 🎉")
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
    f"Applied Financial Models · Module 2.2 Cost & OPEX Forecasting · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
