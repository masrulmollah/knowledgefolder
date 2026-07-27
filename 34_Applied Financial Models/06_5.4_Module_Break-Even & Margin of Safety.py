"""
================================================================================
APPLIED FINANCIAL MODELS
Module 5.4 — BREAK-EVEN & MARGIN OF SAFETY
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
cost-volume-profit (CVP) analysis: the break-even point, contribution margin,
margin of safety, target-profit volumes, and operating leverage.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live CVP / break-even engine + chart)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_5_4_Break_Even_and_Margin_of_Safety.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="5.4 Break-Even & Margin of Safety — Applied Financial Models",
    layout="wide",
    page_icon="🎲",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 5 · Scenario, Sensitivity & Risk Models")
st.sidebar.markdown(
    """
**Module 5.4 — Break-Even & Margin of Safety**

🟢 *Foundational*

**You will learn to:**
- Calculate the break-even point
- Use contribution margin
- Measure the margin of safety
- Understand operating leverage
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live CVP model and "
    "see exactly where revenue crosses total cost."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎲 5.4 · Break-Even & Margin of Safety")
st.markdown(
    """
How many units must you sell just to *not lose money*? That's the **break-even point** — one of the most
practical questions in business. **Cost-Volume-Profit (CVP)** analysis answers it, and goes further:
how much sales can fall before you hit break-even (the **margin of safety**), and how sharply profit
swings with volume (**operating leverage**).

This module rounds out Part 5 with the tools managers use every day to understand the relationship between
**costs, volume and profit**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "5.4")
c2.metric("Part", "5 — Risk")
c3.metric("Level", "Foundational")
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
### Contribution margin — the building block
The **contribution margin** is what each unit contributes towards covering fixed costs (and then profit),
after paying its own variable cost:
"""
    )
    st.latex(r"\text{Contribution per unit} = \text{Price} - \text{Variable cost per unit}")
    st.latex(r"\text{Contribution margin ratio} = \frac{\text{Price} - \text{Variable cost}}{\text{Price}}")

    st.markdown("### The break-even point")
    st.markdown("Break-even is where **total contribution exactly covers fixed costs** — profit is zero.")
    st.latex(r"\text{Break-even (units)} = \frac{\text{Fixed Costs}}{\text{Contribution per unit}}")
    st.latex(r"\text{Break-even (revenue)} = \frac{\text{Fixed Costs}}{\text{Contribution margin ratio}}")

    st.markdown("### The key CVP measures")
    measures = pd.DataFrame(
        {
            "Measure": ["Break-even point", "Margin of safety", "Target-profit volume", "Operating leverage"],
            "Formula": [
                "Fixed cost ÷ contribution per unit",
                "(Actual sales − Break-even sales) ÷ Actual sales",
                "(Fixed cost + Target profit) ÷ contribution per unit",
                "Contribution ÷ Operating profit",
            ],
            "Tells you": [
                "Volume needed to avoid a loss",
                "How far sales can fall before a loss (a risk cushion)",
                "Volume needed to hit a profit goal",
                "How sharply profit reacts to a change in sales",
            ],
        }
    )
    st.table(measures)

    with st.expander("🔑 Concept 1 — Why contribution margin matters"):
        st.markdown(
            """
Every unit sold first has to 'pay for itself' (its variable cost); what's left — the **contribution** —
goes towards fixed costs. Once fixed costs are fully covered, every additional unit's contribution drops
straight to profit. This is why contribution margin is the engine of CVP analysis.
"""
        )

    with st.expander("🔑 Concept 2 — The margin of safety (your risk cushion)"):
        st.markdown(
            """
The **margin of safety** measures how much sales can decline before you reach break-even:

$$\\text{Margin of Safety \\%} = \\frac{\\text{Actual Sales} - \\text{Break-even Sales}}{\\text{Actual Sales}}$$

A **high** margin of safety (say 40%) means sales could fall 40% before you make a loss — a comfortable
cushion. A **low** margin (say 5%) means you're operating close to the edge — risky. It's a direct,
intuitive measure of downside risk.
"""
        )

    with st.expander("🔑 Concept 3 — Target-profit analysis"):
        st.markdown(
            """
CVP isn't just about avoiding losses — it tells you the volume needed to hit a **profit goal**:

$$\\text{Units for target profit} = \\frac{\\text{Fixed Costs} + \\text{Target Profit}}{\\text{Contribution per unit}}$$

Just treat the target profit like an extra 'fixed cost' to be covered. This turns a profit *goal* into a
concrete sales *target*.
"""
        )

    with st.expander("🔑 Concept 4 — Operating leverage"):
        st.markdown(
            """
**Operating leverage** measures how sensitive profit is to changes in sales:

$$\\text{Degree of Operating Leverage} = \\frac{\\text{Total Contribution}}{\\text{Operating Profit}}$$

- **High fixed costs → high operating leverage:** a small % change in sales causes a *large* % change in
  profit (great on the way up, brutal on the way down).
- **Low fixed costs → low leverage:** profit tracks sales more gently.

A DOL of 3 means a 10% rise in sales produces a **30%** rise in profit (and vice-versa).
"""
        )

    with st.expander("🔑 Concept 5 — The CVP chart"):
        st.markdown(
            """
The classic **break-even chart** plots, against volume:
- **Total revenue** (a line rising from the origin), and
- **Total cost** (fixed cost + variable cost, starting at the fixed-cost level).

The point where the two lines **cross** is the break-even volume. Left of it = loss; right of it = profit.
The widening gap to the right is profit; the gap between actual sales and break-even is the margin of safety.
"""
        )

    st.success(
        "**Takeaway:** CVP analysis links cost, volume and profit. Break-even = fixed cost ÷ contribution "
        "per unit; the margin of safety shows how much sales can fall before a loss; and operating leverage "
        "shows how sharply profit swings with volume. Simple tools, huge practical value."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — CVP for a product line")
    st.markdown("Price €20/unit, variable cost €12/unit, fixed costs €300,000, current sales 60,000 units.")

    st.markdown("#### Step 1 — Contribution margin")
    st.markdown(
        """
$$\\text{Contribution per unit} = €20 - €12 = \\mathbf{€8}$$
$$\\text{Contribution margin ratio} = \\frac{8}{20} = \\mathbf{40\\%}$$
"""
    )

    st.markdown("#### Step 2 — Break-even point")
    st.markdown(
        """
$$\\text{Break-even (units)} = \\frac{€300{,}000}{€8} = \\mathbf{37{,}500 \\text{ units}}$$
$$\\text{Break-even (revenue)} = 37{,}500 \\times €20 = \\mathbf{€750{,}000}$$
"""
    )

    st.markdown("#### Step 3 — Margin of safety")
    st.markdown(
        """
Current sales = 60,000 units (€1,200,000).
$$\\text{Margin of Safety} = \\frac{60{,}000 - 37{,}500}{60{,}000} = \\mathbf{37.5\\%}$$

Sales could fall 37.5% before the product makes a loss — a healthy cushion.
"""
    )

    st.markdown("#### Step 4 — Current profit & operating leverage")
    st.markdown(
        """
- Total contribution = 60,000 × €8 = €480,000
- Operating profit = €480,000 − €300,000 = **€180,000**
- Degree of operating leverage = €480,000 ÷ €180,000 = **2.67×**

*A 10% rise in sales would lift profit by ~26.7%.*
"""
    )

    e1, e2, e3, e4 = st.columns(4)
    e1.metric("Break-even", "37,500 units")
    e2.metric("Margin of safety", "37.5%")
    e3.metric("Operating profit", "€180,000")
    e4.metric("Operating leverage", "2.67×")

    st.info(
        "**Insight:** The product breaks even at 37,500 units and currently sells 60,000 — a comfortable "
        "**37.5% margin of safety**. But note the **operating leverage of 2.67×**: profit is nearly 3× as "
        "volatile as sales. That's great while volumes grow, but a 20% sales drop would cut profit by "
        "~53%. **Recommendation: healthy now, but monitor volume closely given the leverage.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — CVP / Break-Even Engine")
    st.markdown(
        "Set price, costs and volume. The model computes break-even, margin of safety, profit and operating "
        "leverage — and plots the classic break-even chart."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        price = st.number_input("Price per unit (€)", 0.1, 1000.0, 20.0, 0.5)
        var_cost = st.number_input("Variable cost per unit (€)", 0.0, 1000.0, 12.0, 0.5)
        fixed_cost = st.number_input("Fixed costs (€)", 0, 50_000_000, 300_000, 25_000)
        current_units = st.number_input("Current sales (units)", 0, 10_000_000, 60_000, 5_000)
        target_profit = st.number_input("Target profit (€)", 0, 50_000_000, 200_000, 25_000)

    with right:
        contribution = price - var_cost
        cm_ratio = (contribution / price * 100) if price else 0

        if contribution <= 0:
            st.error(
                "⚠️ **Contribution is zero or negative** (price ≤ variable cost). Every unit loses money, so "
                "there is **no break-even** — the product cannot be profitable at this price. Fix pricing or cost."
            )
        else:
            be_units = fixed_cost / contribution
            be_revenue = be_units * price
            total_contribution = current_units * contribution
            op_profit = total_contribution - fixed_cost
            current_revenue = current_units * price
            mos_pct = ((current_revenue - be_revenue) / current_revenue * 100) if current_revenue else 0
            target_units = (fixed_cost + target_profit) / contribution
            dol = (total_contribution / op_profit) if op_profit != 0 else float("inf")

            k1, k2, k3 = st.columns(3)
            k1.metric("Contribution / unit", money(contribution, dp=2), f"{cm_ratio:.0f}% margin")
            k2.metric("Break-even", f"{be_units:,.0f} units", money(be_revenue) + " revenue")
            k3.metric("Operating profit", money(op_profit),
                      "Profit +" if op_profit > 0 else "Loss −",
                      delta_color="normal" if op_profit > 0 else "inverse")

            k4, k5, k6 = st.columns(3)
            k4.metric("Margin of safety", f"{mos_pct:,.1f}%",
                      "Cushion" if mos_pct > 0 else "Below break-even!",
                      delta_color="normal" if mos_pct > 0 else "inverse")
            k5.metric("Units for target profit", f"{target_units:,.0f}")
            k6.metric("Operating leverage", f"{dol:,.2f}×" if dol != float('inf') else "n/a",
                      help="Total contribution ÷ operating profit")

            # verdict on margin of safety
            if op_profit <= 0:
                st.error(
                    f"❌ At {current_units:,.0f} units you're **below break-even** ({be_units:,.0f} units) — "
                    f"making a loss of {money(-op_profit)}. You need {be_units - current_units:,.0f} more units."
                )
            elif mos_pct < 15:
                st.warning(
                    f"⚠️ Margin of safety is only **{mos_pct:.0f}%** — you're operating close to break-even. "
                    "A small sales drop would tip you into a loss."
                )
            else:
                st.success(
                    f"✅ Healthy: **{mos_pct:.0f}% margin of safety** — sales could fall {mos_pct:.0f}% before "
                    f"a loss. Operating leverage of {dol:.2f}× means profit moves ~{dol:.1f}× as fast as sales."
                )

            # Break-even chart
            st.markdown("##### 📈 Break-Even Chart")
            max_units = int(max(current_units, be_units) * 1.6) or 100
            pts = 12
            step = max(max_units // pts, 1)
            xs = list(range(0, max_units + step, step))
            chart_df = pd.DataFrame({
                "Total revenue": [u * price for u in xs],
                "Total cost": [fixed_cost + u * var_cost for u in xs],
            }, index=xs)
            chart_df.index.name = "Units"
            st.line_chart(chart_df)
            st.caption(
                f"The lines cross at the **break-even point ({be_units:,.0f} units)**. Left of it = loss; "
                f"right of it = profit. Your current sales ({current_units:,.0f}) sit "
                f"{'above ✅' if current_units > be_units else 'below ❌'} break-even."
            )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Squeeze the margin:** Raise variable cost to €18. Watch break-even soar and the margin of safety shrink.
2. **Fixed-cost effect:** Double fixed costs to €600k. How many more units must you sell to break even?
"""
        )
    with e2:
        st.markdown(
            """
3. **Hit the target:** Note the 'units for target profit'. How much is that above break-even?
4. **Leverage risk:** Push fixed costs up and variable cost down. Watch operating leverage climb — higher
   reward *and* higher risk.
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Pricing a new product launch", expanded=True):
        st.markdown(
            """
**Situation:** A company launching a new product needed to know how many units it must sell to justify the
launch.

**How CVP helped:** With price, variable cost and the fixed launch costs known, the **break-even volume**
told management the minimum sales required — which they could compare against a realistic demand forecast.

**Why it matters:** If break-even sits above credible demand, the launch is a non-starter before a euro is spent.

**Lesson:** Break-even analysis is a fast, powerful go/no-go screen for new products.
"""
        )

    with st.expander("Case B — The thin margin of safety warning"):
        st.markdown(
            """
**Situation:** A business line looked profitable, but management wanted to understand its risk.

**What CVP revealed:** The **margin of safety was only 8%** — sales could fall just 8% before the line
made a loss. Despite current profitability, it was operating dangerously close to the edge.

**Why it matters:** A profitable-but-fragile line needs active volume protection; the margin of safety
made that fragility visible.

**Lesson:** Always check the margin of safety — profitability alone doesn't reveal how much cushion you have.
"""
        )

    with st.expander("Case C — Operating leverage in a downturn"):
        st.markdown(
            """
**Situation:** A high-fixed-cost manufacturer faced a demand slump.

**What CVP revealed:** With a **degree of operating leverage of ~3×**, a 20% fall in sales translated into
a ~60% collapse in operating profit — far worse than management expected.

**Why it matters:** High operating leverage amplifies downturns. Understanding it helps a business prepare
(e.g. flex costs, protect volume) before a slump hits.

**Lesson:** Know your operating leverage — it tells you how exposed your profit is to a fall in sales.
"""
        )

    st.info(
        "🔗 **Pattern:** CVP analysis turns the cost/volume/profit relationship into practical decisions — "
        "minimum viable volumes (break-even), risk cushions (margin of safety), and profit volatility "
        "(operating leverage). Simple maths, everyday value."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_54"):
        q1 = st.radio(
            "**1.** The contribution per unit is:",
            [
                "Price + variable cost per unit",
                "Price − variable cost per unit",
                "Fixed cost ÷ units",
                "Price − fixed cost",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The break-even point (in units) equals:",
            [
                "Fixed costs ÷ contribution per unit",
                "Contribution per unit ÷ fixed costs",
                "Fixed costs × price",
                "Variable cost ÷ price",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The margin of safety measures:",
            [
                "How much fixed costs can rise",
                "How far sales can fall before reaching break-even",
                "The tax rate on profit",
                "The depreciation charge",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A high degree of operating leverage means:",
            [
                "Profit is barely affected by sales changes",
                "A small % change in sales causes a large % change in profit",
                "There are no fixed costs",
                "The break-even point is zero",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** On a break-even chart, the break-even point is where:",
            [
                "Total cost is zero",
                "The total revenue and total cost lines cross",
                "Fixed cost equals variable cost",
                "Profit is at its maximum",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Price − variable cost per unit"),
            "2": (q2, "Fixed costs ÷ contribution per unit"),
            "3": (q3, "How far sales can fall before reaching break-even"),
            "4": (q4, "A small % change in sales causes a large % change in profit"),
            "5": (q5, "The total revenue and total cost lines cross"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've completed Part 5 (Risk & Uncertainty)! On to Part 6 (Specialised Models). 🎉")
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
    f"Applied Financial Models · Module 5.4 Break-Even & Margin of Safety · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
