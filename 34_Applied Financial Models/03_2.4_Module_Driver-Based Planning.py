"""
================================================================================
APPLIED FINANCIAL MODELS
Module 2.4 — DRIVER-BASED PLANNING
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to build driver-based plans: translating operational KPIs (capacity,
utilisation, yield, headcount, productivity) into financial outputs.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live operational -> financial driver tree)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_2_4_Driver_Based_Planning.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="2.4 Driver-Based Planning — Applied Financial Models",
    layout="wide",
    page_icon="📊",
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
st.sidebar.caption("Part 2 · Forecasting & Budgeting Models")
st.sidebar.markdown(
    """
**Module 2.4 — Driver-Based Planning**

🟡 *Intermediate*

**You will learn to:**
- Link operational KPIs to financial outputs
- Build a driver tree (capacity → revenue → profit)
- Model yield, utilisation & productivity
- Plan using the levers management controls
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live driver tree — "
    "change an operational KPI and watch profit respond."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("📊 2.4 · Driver-Based Planning")
st.markdown(
    """
Most budgets are built in *financial* language — revenue, costs, profit. But managers don't directly
control "revenue"; they control **operational drivers**: machine capacity, utilisation, yield, headcount,
productivity. **Driver-based planning** links those operational KPIs to the financial outputs, so the plan
speaks the language of the people who actually deliver it.

This approach — the culmination of Part 2 — makes plans more accurate, more actionable, and far easier
to flex ("what if utilisation improves 5%?").
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "2.4")
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
### What is driver-based planning?
Instead of forecasting financial lines directly, you model the **operational drivers** that *cause* them,
then let the financials fall out. A driver is any measurable operational input that moves a financial
output — capacity, utilisation, yield, price, headcount, productivity.
"""
    )

    st.markdown("### The operational → financial driver tree")
    st.markdown(
        """
```
   OPERATIONAL DRIVERS                        FINANCIAL OUTPUTS
   ───────────────────                        ─────────────────
   Machine hours available ┐
   × Utilisation %         ├─► Units produced ─► × Price ─────► REVENUE ┐
   × Output per hour       │         │                                  │
   × Yield % (good units)  ┘         │                                  ├─► PROFIT
                                     └─► × Cost per unit ─► COGS ────────┤
   Headcount × cost/head ───────────────────────────────► Labour cost ──┘
```
"""
    )

    st.markdown("### Common operational drivers and what they feed")
    drivers = pd.DataFrame(
        {
            "Operational driver": [
                "Capacity (machine hours)", "Utilisation %", "Yield %",
                "Output per hour / productivity", "Headcount", "Cost per unit",
            ],
            "Feeds into": [
                "Maximum possible output", "Actual output vs. capacity", "Good (sellable) units",
                "Units produced per resource", "Labour cost & capacity", "Variable cost / COGS",
            ],
            "Management lever": [
                "Capex / shifts", "Scheduling, downtime reduction", "Quality / waste reduction",
                "Training, automation, process improvement", "Hiring / restructuring", "Procurement, efficiency",
            ],
        }
    )
    st.table(drivers)

    with st.expander("🔑 Concept 1 — Why drivers beat direct financial forecasting"):
        st.markdown(
            """
- **Accuracy:** operational drivers are grounded in physical reality (a machine can only run so many hours).
- **Actionability:** managers can act on "improve yield 2%" but not on "increase revenue €200k" directly.
- **Flexibility:** one driver change flows through automatically — perfect for scenario analysis.
- **Ownership:** operations teams recognise and commit to plans built in their own KPIs.
"""
        )

    with st.expander("🔑 Concept 2 — Capacity, utilisation & yield (the production chain)"):
        st.markdown(
            """
A classic manufacturing driver chain:

$$\\text{Units produced} = \\text{Capacity (hrs)} \\times \\text{Utilisation \\%} \\times \\text{Output per hr} \\times \\text{Yield \\%}$$

- **Utilisation** = how much of available capacity you actually use.
- **Yield** = the proportion of output that's good (sellable), i.e. net of waste/defects.

Small improvements *compound*: +5% utilisation *and* +3% yield can lift output meaningfully — and because
much cost is fixed, most of that flows to profit (operating leverage from Module 2.2).
"""
        )

    with st.expander("🔑 Concept 3 — Productivity drivers (people & output)"):
        st.markdown(
            """
For labour-intensive or service settings, model:

$$\\text{Output} = \\text{Headcount} \\times \\text{Productivity per head}$$

Productivity improvements (training, automation, process change) let output grow without proportional
headcount growth — the core of most cost-transformation business cases.
"""
        )

    with st.expander("🔑 Concept 4 — Sensitivity: which driver matters most?"):
        st.markdown(
            """
Not all drivers are equal. A driver-based model lets you test the **profit impact of a 1% change** in
each driver, ranking them by leverage. Management should focus effort on the **highest-impact drivers**
(often price and yield) rather than spreading attention thinly.

This ranking is the natural bridge to sensitivity analysis (Part 5).
"""
        )

    st.success(
        "**Takeaway:** Driver-based planning models the *operational causes* of financial results. It's more "
        "accurate, more actionable, and easier to flex — and it makes the plan speak the language of the "
        "people who deliver it."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — From machine hours to profit")
    st.markdown("Building a driver-based plan for a CleanSoap production line.")

    st.markdown("#### Step 1 — Operational drivers → units produced")
    st.markdown(
        """
| Driver | Value |
|---|---|
| Machine hours available (year) | 6,000 |
| Utilisation % | 85% |
| Output per hour (units) | 250 |
| Yield % (good units) | 92% |

$$\\text{Units} = 6{,}000 \\times 85\\% \\times 250 \\times 92\\% = \\mathbf{1{,}173{,}000 \\text{ units}}$$
"""
    )

    st.markdown("#### Step 2 — Units → revenue & cost")
    st.markdown(
        """
| Line | Calculation | € |
|---|---|---|
| Revenue | 1,173,000 × €2.00 | 2,346,000 |
| Variable cost | 1,173,000 × €1.30 | (1,524,900) |
| Fixed cost | | (300,000) |
| **Operating profit** | | **€521,100** |
"""
    )

    st.markdown("#### Step 3 — Test an operational improvement")
    st.markdown(
        """
Suppose a quality initiative lifts **yield from 92% → 95%** (nothing else changes):

$$\\text{Units} = 6{,}000 \\times 85\\% \\times 250 \\times 95\\% = \\mathbf{1{,}211{,}250 \\text{ units}}$$

| Line | € |
|---|---|
| Revenue | 2,422,500 |
| Variable cost | (1,574,625) |
| Fixed cost | (300,000) |
| **Operating profit** | **€547,875** |
"""
    )

    st.info(
        "**Insight:** A 3-percentage-point yield improvement lifted operating profit by **€26,775 (+5%)** — "
        "with no extra machines, hours, or price change. That's the power of driver-based planning: it "
        "pinpoints exactly which *operational* lever creates *financial* value, so improvement effort is targeted."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Operational → Financial Driver Tree")
    st.markdown(
        "Adjust the **operational drivers** on the left and watch them cascade into **units, revenue, cost "
        "and profit** on the right. This is driver-based planning in action."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        st.markdown("##### 🏭 Production drivers")
        machine_hours = st.number_input("Machine hours available / yr", 100, 100_000, 6_000, 100)
        utilisation = st.slider("Utilisation (%)", 0.0, 100.0, 85.0, 1.0)
        output_per_hr = st.number_input("Output per hour (units)", 1, 10_000, 250, 10)
        yield_pct = st.slider("Yield — good units (%)", 50.0, 100.0, 92.0, 0.5)

        st.markdown("##### 💰 Commercial drivers")
        price = st.number_input("Price per unit (€)", 0.10, 100.0, 2.00, 0.05)
        var_cost = st.number_input("Variable cost per unit (€)", 0.01, 90.0, 1.30, 0.05)
        fixed_cost = st.number_input("Fixed cost (€)", 0, 10_000_000, 300_000, 25_000)

    with right:
        capacity_units = machine_hours * output_per_hr
        units_before_yield = capacity_units * utilisation / 100
        units = units_before_yield * yield_pct / 100
        revenue = units * price
        variable = units * var_cost
        op_profit = revenue - variable - fixed_cost
        op_margin = (op_profit / revenue * 100) if revenue else 0
        waste_units = units_before_yield - units

        k1, k2, k3 = st.columns(3)
        k1.metric("Units produced (good)", f"{units:,.0f}")
        k2.metric("Revenue", money(revenue))
        k3.metric("Operating profit", money(op_profit))

        k4, k5, k6 = st.columns(3)
        k4.metric("Capacity (max units)", f"{capacity_units:,.0f}")
        k5.metric("Units lost to waste", f"{waste_units:,.0f}",
                  help="Utilised output that failed the yield %")
        k6.metric("Operating margin", f"{op_margin:,.1f}%")

        # Driver tree table
        tree = pd.DataFrame(
            {
                "Driver / Output": [
                    "Machine hours available", "× Utilisation %", "× Output per hour",
                    "= Utilised output (units)", "× Yield %", "= Good units produced",
                    "× Price", "= Revenue", "− Variable cost", "− Fixed cost", "= Operating profit",
                ],
                "Value": [
                    f"{machine_hours:,.0f}", f"{utilisation:.0f}%", f"{output_per_hr:,.0f}",
                    f"{units_before_yield:,.0f}", f"{yield_pct:.1f}%", f"{units:,.0f}",
                    money(price, dp=2), money(revenue), money(-variable), money(-fixed_cost), money(op_profit),
                ],
            }
        )
        st.markdown("##### 🌳 Driver Tree")
        st.dataframe(tree, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("##### 📊 Driver Sensitivity — profit impact of a +1% improvement in each driver")
    st.caption("Which operational lever creates the most value? (All else held constant.)")

    base_profit = op_profit

    def profit_with(util=utilisation, yld=yield_pct, oph=output_per_hr, pr=price, vc=var_cost):
        u = machine_hours * oph * util / 100 * yld / 100
        return u * pr - u * vc - fixed_cost

    sens = {
        "Utilisation +1%": profit_with(util=min(utilisation + 1, 100)) - base_profit,
        "Yield +1%": profit_with(yld=min(yield_pct + 1, 100)) - base_profit,
        "Output/hour +1%": profit_with(oph=output_per_hr * 1.01) - base_profit,
        "Price +1%": profit_with(pr=price * 1.01) - base_profit,
        "Variable cost −1%": profit_with(vc=var_cost * 0.99) - base_profit,
    }
    sens_df = pd.DataFrame({"Δ Operating profit (€)": sens.values()}, index=list(sens.keys()))
    st.bar_chart(sens_df)

    top_driver = max(sens, key=sens.get)
    st.info(
        f"🎯 **Highest-impact lever right now: {top_driver}** — improving it by 1% adds "
        f"**{money(sens[top_driver])}** to operating profit. Focus improvement effort here first."
    )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Yield vs. utilisation:** Which adds more profit — +5% utilisation or +5% yield? Test both.
2. **Waste hunt:** Lower yield to 80%. How many units (and how much profit) are lost to waste?
"""
        )
    with e2:
        st.markdown(
            """
3. **Capacity ceiling:** Note the max-capacity units. How close is your plan to the ceiling?
4. **Price vs. ops:** Compare a 1% price rise with a 1% cost cut — which is the bigger lever for you?
"""
        )

    st.download_button(
        "⬇️ Download this driver tree (CSV)",
        tree.to_csv(index=False).encode("utf-8"),
        "driver_based_plan.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The yield-improvement business case", expanded=True):
        st.markdown(
            """
**Situation:** A factory wanted to justify investment in quality-control equipment.

**How driver-based planning helped:** By modelling **yield** as an explicit driver, finance showed that
lifting yield from 92% → 95% would add ~€27k of profit per line per year — directly linking the
operational KPI to a financial return the board could evaluate.

**Why it matters:** Operations understood "improve yield 3pp"; finance translated it into euros. The
shared language made approval straightforward.

**Lesson:** Driver-based models turn operational improvements into fundable, quantified business cases.
"""
        )

    with st.expander("Case B — Manpower productivity transformation"):
        st.markdown(
            """
**Situation:** A large manufacturing site ran a transformation to improve manpower productivity
(fewer people, higher output per head).

**How driver-based planning helped:** Modelling **headcount × productivity per head** let finance project
how output could be maintained (or grown) with a reduced workforce — quantifying the savings and the
payback of the change programme.

**Why it matters:** The plan was built in the operational levers management actually controlled, making
targets credible and trackable month by month.

**Lesson:** Big cost-transformation cases are best built bottom-up from productivity drivers.
"""
        )

    with st.expander("Case C — Finding the highest-impact lever"):
        st.markdown(
            """
**Situation:** A management team was spreading improvement effort across a dozen initiatives with little focus.

**How driver-based planning helped:** A **driver-sensitivity** analysis ranked each lever by profit impact
per 1% change. Price and yield dwarfed the others — so effort was refocused on pricing discipline and waste
reduction, and results improved quickly.

**Why it matters:** Not all drivers are equal; a model reveals where a unit of effort earns the most.

**Lesson:** Use driver sensitivity to prioritise — focus on the few levers that move profit the most.
"""
        )

    st.info(
        "🔗 **Pattern:** Driver-based planning connects the shop floor to the P&L. It makes plans credible "
        "(grounded in operations), actionable (built on real levers), and prioritised (via driver sensitivity)."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_24"):
        q1 = st.radio(
            "**1.** Driver-based planning forecasts financial results by:",
            [
                "Hard-coding revenue and profit directly",
                "Modelling the operational drivers (KPIs) that cause the financial outputs",
                "Copying last year's numbers",
                "Using only the tax schedule",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** In a production driver chain, units produced ≈",
            [
                "Capacity × Utilisation × Output per hour × Yield",
                "Revenue ÷ Price",
                "Fixed cost + Variable cost",
                "Headcount ÷ Productivity",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** 'Yield %' in a manufacturing model represents:",
            [
                "The interest rate on debt",
                "The proportion of output that is good / sellable (net of waste)",
                "The tax rate",
                "The price per unit",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A key advantage of driver-based planning is that it is:",
            [
                "Impossible to flex",
                "Actionable — managers can act on operational levers, not abstract financial totals",
                "Always less accurate",
                "Only useful for tax",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Driver sensitivity analysis helps management by:",
            [
                "Hiding which drivers matter",
                "Ranking drivers by their profit impact so effort focuses on the highest-impact levers",
                "Removing the need for a budget",
                "Setting the depreciation method",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Modelling the operational drivers (KPIs) that cause the financial outputs"),
            "2": (q2, "Capacity × Utilisation × Output per hour × Yield"),
            "3": (q3, "The proportion of output that is good / sellable (net of waste)"),
            "4": (q4, "Actionable — managers can act on operational levers, not abstract financial totals"),
            "5": (q5, "Ranking drivers by their profit impact so effort focuses on the highest-impact levers"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've completed Part 2! You can now build forecasting & budgeting models end-to-end. 🎉")
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
    f"Applied Financial Models · Module 2.4 Driver-Based Planning · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
