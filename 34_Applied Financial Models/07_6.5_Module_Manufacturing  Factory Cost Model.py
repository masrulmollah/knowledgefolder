"""
================================================================================
APPLIED FINANCIAL MODELS
Module 6.5 — MANUFACTURING / FACTORY COST MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to model manufacturing cost: absorption costing, overhead absorption rates,
wastage/yield analytics, and the full cost-per-unit build-up.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live cost-per-unit + wastage engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_6_5_Manufacturing_Factory_Cost_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="6.5 Manufacturing / Factory Cost Model — Applied Financial Models",
    layout="wide",
    page_icon="🚀",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=2):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def build_cost_per_unit(materials, labour, var_oh,
                        fixed_oh_total, good_units, yield_pct):
    """
    Build absorption cost per unit including a wastage adjustment.
    - Direct costs (materials, labour, variable OH) are per GOOD unit but
      grossed up for wastage (you pay for inputs on units that fail yield).
    - Fixed overhead is absorbed over good units.
    Returns a breakdown dict.
    """
    yld = yield_pct / 100 if yield_pct > 0 else 1
    # inputs must be started for every good unit, adjusted for yield loss
    materials_eff = materials / yld
    labour_eff = labour / yld
    var_oh_eff = var_oh / yld
    wastage_cost = (materials_eff + labour_eff + var_oh_eff) - (materials + labour + var_oh)

    fixed_oh_per_unit = fixed_oh_total / good_units if good_units else 0

    prime_cost = materials_eff + labour_eff
    variable_cost = prime_cost + var_oh_eff
    total_cost = variable_cost + fixed_oh_per_unit

    return {
        "materials_eff": materials_eff, "labour_eff": labour_eff, "var_oh_eff": var_oh_eff,
        "wastage_cost": wastage_cost, "fixed_oh_per_unit": fixed_oh_per_unit,
        "prime_cost": prime_cost, "variable_cost": variable_cost, "total_cost": total_cost,
    }


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 6 · Specialised & Advanced Models")
st.sidebar.markdown(
    """
**Module 6.5 — Manufacturing / Factory Cost Model**

🟡 *Intermediate*

**You will learn to:**
- Build a full cost-per-unit
- Apply absorption costing & OH rates
- Quantify the cost of wastage / low yield
- Turn cost analytics into savings
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a cost-per-unit and see "
    "exactly what wastage is costing you."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🚀 6.5 · Manufacturing / Factory Cost Model")
st.markdown(
    """
For any manufacturer, the most important number is often the **cost per unit** — it drives pricing,
margins, make-vs-buy decisions, and cost-saving priorities. Building it properly means understanding
**absorption costing** (how fixed factory overhead is spread across units) and the real, often hidden,
**cost of wastage** (every unit that fails the yield still consumed materials, labour and energy).

This module — the finale of Part 6 — is tailored to industrial finance: cost-per-unit build-up, overhead
absorption, and wastage analytics that turn directly into savings.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "6.5")
c2.metric("Part", "6 — Specialised")
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
### The cost-per-unit build-up
A product's full (absorption) cost is built up layer by layer:
"""
    )
    build = pd.DataFrame(
        {
            "Layer": ["Direct materials", "+ Direct labour", "= Prime cost",
                      "+ Variable overhead", "+ Fixed overhead (absorbed)", "= Total (absorption) cost"],
            "What it is": [
                "Raw materials & packaging per unit",
                "Production wages per unit",
                "The direct cost of making one unit",
                "Power, consumables that vary with output",
                "Rent, depreciation, salaries — spread over units",
                "The fully-loaded cost of one unit",
            ],
        }
    )
    st.table(build)

    st.markdown("### Absorption costing — spreading fixed overhead")
    st.latex(r"\text{Overhead Absorption Rate} = \frac{\text{Total Fixed Overhead}}{\text{Total Units (or Labour hrs / Machine hrs)}}")
    st.markdown(
        """
Fixed factory overhead doesn't belong to any single unit, so we **absorb** it across output using a rate.
Crucially, the more units you make, the **lower** the fixed overhead per unit (it's spread wider) — a key
reason **volume matters so much** to unit cost.
"""
    )

    st.markdown("### The cost of wastage / yield")
    st.latex(r"\text{Effective input cost per good unit} = \frac{\text{Input cost per unit}}{\text{Yield \%}}")
    st.markdown(
        """
If yield is 90%, you must **start** ~1.11 units of input for every good unit that passes — so the *good*
unit effectively carries the cost of the 0.11 units that were wasted. Low yield silently inflates unit cost.
"""
    )

    with st.expander("🔑 Concept 1 — Absorption vs. marginal (variable) costing"):
        st.markdown(
            """
- **Absorption costing:** includes a share of **fixed** overhead in each unit — the 'fully-loaded' cost,
  required for financial reporting (inventory valuation) and long-run pricing.
- **Marginal (variable) costing:** counts only **variable** costs per unit — the right basis for
  short-run decisions (e.g. accept a one-off order at a price above variable cost).

Use the right one for the question: absorption for reporting & long-run pricing; marginal for short-run
incremental decisions.
"""
        )

    with st.expander("🔑 Concept 2 — Why fixed cost per unit falls with volume"):
        st.markdown(
            """
Fixed overhead is a *fixed pot* of money. Spread it over more units and the per-unit share drops:

$$\\text{Fixed OH per unit} = \\frac{\\text{Fixed Overhead}}{\\text{Units produced}}$$

This is **operating leverage** (Module 2.2) seen through the cost lens — and why running a factory at high
utilisation is so important to competitive unit cost.
"""
        )

    with st.expander("🔑 Concept 3 — Wastage & yield (the hidden cost)"):
        st.markdown(
            """
Every unit that fails quality still consumed **materials, labour and energy**. So the *good* units must
absorb the cost of the wasted ones. Improving yield from, say, 90% → 95% directly lowers the effective
cost per good unit — often one of the highest-return savings a factory can pursue (and a natural target
for wastage analytics / Power BI dashboards).
"""
        )

    with st.expander("🔑 Concept 4 — Over/under-absorption of overhead"):
        st.markdown(
            """
Absorption rates are set on **budgeted** volume. If actual volume differs:
- Produce **more** than budget → overhead is **over-absorbed** (you 'recovered' more than the actual pot).
- Produce **less** → overhead is **under-absorbed** (a shortfall charged to the P&L).

This variance is why cost accountants track absorption carefully — it can distort reported unit cost and profit.
"""
        )

    with st.expander("🔑 Concept 5 — From cost model to savings"):
        st.markdown(
            """
The unit-cost model is a **savings roadmap**. Break cost into its drivers (materials %, labour, OH,
wastage) and you can see exactly where the biggest opportunities lie — usually **materials** (procurement)
and **wastage/yield** for a typical manufacturer. This is the analytical backbone of any factory
cost-transformation programme.
"""
        )

    st.success(
        "**Takeaway:** A factory cost model builds up the fully-loaded cost per unit — direct materials & "
        "labour, plus absorbed overhead — and reveals the hidden cost of wastage. Volume lowers fixed cost "
        "per unit; better yield lowers effective cost per good unit. It's the roadmap for cost savings."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Cost per unit with absorption & wastage")
    st.markdown("A factory makes **1,000,000 good units/year**. Fixed overhead €500,000. Yield 90%.")

    st.markdown("#### Step 1 — Direct costs per good unit (grossed up for yield)")
    st.markdown(
        """
Per-unit input costs (before wastage): materials €0.80, labour €0.30, variable OH €0.10.

At **90% yield**, you must start 1 ÷ 0.90 = **1.111 units** of input per good unit, so:

| Item | Base | ÷ Yield (90%) | Effective |
|---|---|---|---|
| Materials | €0.80 | ÷ 0.90 | €0.889 |
| Labour | €0.30 | ÷ 0.90 | €0.333 |
| Variable OH | €0.10 | ÷ 0.90 | €0.111 |
| **Variable cost / good unit** | €1.20 | | **€1.333** |

The **wastage cost = €1.333 − €1.20 = €0.133 per unit** — the hidden cost of the 10% that fails.
"""
    )

    st.markdown("#### Step 2 — Absorb fixed overhead")
    st.markdown(
        """
$$\\text{Fixed OH per unit} = \\frac{€500{,}000}{1{,}000{,}000} = €0.50$$
"""
    )

    st.markdown("#### Step 3 — Total absorption cost per unit")
    st.markdown(
        """
$$\\text{Total cost} = €1.333 \\text{ (variable, incl. wastage)} + €0.50 \\text{ (fixed OH)} = \\mathbf{€1.833}$$
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Variable cost/unit", "€1.333", "incl. €0.133 wastage")
    e2.metric("Fixed OH/unit", "€0.500")
    e3.metric("Total cost/unit", "€1.833")

    st.info(
        "**Insight:** Wastage adds **€0.133 to every good unit** — that's **€133,000/year** on 1m units, "
        "purely from the 10% yield loss. Lifting yield from 90% → 95% would cut the effective variable cost "
        "to ~€1.263, saving ~€70k/year. Meanwhile, fixed OH per unit (€0.50) would fall if volume rose. "
        "**The two biggest cost-saving levers here are clearly yield improvement and higher utilisation.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Factory Cost-per-Unit Engine")
    st.markdown(
        "Build the fully-loaded cost per unit. Flex the yield to see the cost of wastage, and change volume "
        "to watch fixed overhead per unit move."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        st.markdown("##### 🧱 Direct costs (per good unit, before wastage)")
        materials = st.number_input("Direct materials (€/unit)", 0.0, 1000.0, 0.80, 0.05)
        labour = st.number_input("Direct labour (€/unit)", 0.0, 1000.0, 0.30, 0.05)
        var_oh = st.number_input("Variable overhead (€/unit)", 0.0, 1000.0, 0.10, 0.05)

        st.markdown("##### 🏭 Overhead & volume")
        fixed_oh_total = st.number_input("Total fixed overhead (€)", 0, 500_000_000, 500_000, 25_000)
        good_units = st.number_input("Good units produced / yr", 1_000, 500_000_000, 1_000_000, 50_000)

        st.markdown("##### ♻️ Yield")
        yield_pct = st.slider("Yield — good units (%)", 50.0, 100.0, 90.0, 0.5)

        st.markdown("##### 💰 Pricing (optional)")
        price = st.number_input("Selling price (€/unit)", 0.0, 5000.0, 2.50, 0.05)

    with right:
        r = build_cost_per_unit(materials, labour, var_oh, fixed_oh_total, good_units, yield_pct)

        total_cost = r["total_cost"]
        margin = price - total_cost
        margin_pct = (margin / price * 100) if price else 0
        annual_wastage = r["wastage_cost"] * good_units

        k1, k2, k3 = st.columns(3)
        k1.metric("Total cost / unit", money(total_cost, dp=3))
        k2.metric("Wastage cost / unit", money(r["wastage_cost"], dp=3),
                  f"{money(annual_wastage, dp=0)}/yr", delta_color="inverse")
        k3.metric("Fixed OH / unit", money(r["fixed_oh_per_unit"], dp=3))

        if price > 0:
            k4, k5, k6 = st.columns(3)
            k4.metric("Selling price", money(price, dp=2))
            k5.metric("Margin / unit", money(margin, dp=3),
                      "Profit +" if margin > 0 else "Loss −",
                      delta_color="normal" if margin > 0 else "inverse")
            k6.metric("Margin %", f"{margin_pct:.1f}%")

            if margin <= 0:
                st.error(
                    f"❌ At {money(price,dp=2)} the unit **loses {money(-margin,dp=3)}** — the price is below "
                    "fully-loaded cost. Raise price, cut cost, or improve yield/volume."
                )
            else:
                st.success(
                    f"✅ Each unit earns {money(margin,dp=3)} ({margin_pct:.1f}% margin). "
                    f"Wastage is costing {money(annual_wastage,dp=0)}/yr — the top savings target."
                )

        # cost breakdown table
        breakdown = pd.DataFrame(
            {
                "Cost component": ["Materials (eff.)", "Labour (eff.)", "Variable OH (eff.)",
                                   "  of which: wastage", "Fixed OH (absorbed)", "TOTAL cost / unit"],
                "€ per unit": [
                    r["materials_eff"], r["labour_eff"], r["var_oh_eff"],
                    r["wastage_cost"], r["fixed_oh_per_unit"], total_cost,
                ],
            }
        )
        breakdown["€ per unit"] = breakdown["€ per unit"].map(lambda v: money(v, dp=3))
        st.markdown("##### 📄 Cost-per-Unit Build-Up")
        st.dataframe(breakdown, use_container_width=True, hide_index=True)

        # composition chart
        comp = pd.DataFrame(
            {"€ per unit": [r["materials_eff"], r["labour_eff"], r["var_oh_eff"], r["fixed_oh_per_unit"]]},
            index=["Materials", "Labour", "Variable OH", "Fixed OH"],
        )
        st.markdown("##### 📊 Cost composition")
        st.bar_chart(comp)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Yield is money:** Raise yield 90% → 95%. Watch the wastage cost/unit and the annual wastage bill drop.
2. **Volume dilutes fixed cost:** Double the good units. See fixed OH per unit halve — the power of utilisation.
"""
        )
    with e2:
        st.markdown(
            """
3. **Procurement lever:** Cut materials by 10%. For most factories, materials is the biggest cost component.
4. **Break-even price:** Lower the selling price until the margin hits zero — that's your minimum viable price.
"""
        )

    st.download_button(
        "⬇️ Download the cost build-up (CSV)",
        breakdown.to_csv(index=False).encode("utf-8"),
        "factory_cost_per_unit.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Wastage analytics that unlocked savings", expanded=True):
        st.markdown(
            """
**Situation:** A factory suspected wastage was hurting margins but couldn't quantify it by SKU or line.

**How the cost model helped:** By building the **effective cost per good unit** (grossing inputs up for
yield), finance quantified exactly what each percentage point of wastage cost — often €100k+ per year on a
high-volume line. A **Power BI dashboard** then tracked wastage by machine and SKU for targeted action.

**Why it matters:** You can't manage what you can't measure; the model turned a vague concern into a hard,
prioritised savings number.

**Lesson:** Wastage/yield is a top-tier savings lever — quantify it per good unit and track it relentlessly.
"""
        )

    with st.expander("Case B — Volume, absorption and unit cost"):
        st.markdown(
            """
**Situation:** A plant's unit cost jumped in a low-demand quarter, alarming management.

**What the model revealed:** With fewer units produced, the **fixed overhead was spread over less volume**,
so fixed OH per unit rose (and overhead was **under-absorbed**). The variable cost hadn't changed at all —
the spike was purely an absorption/volume effect.

**Why it matters:** Misreading an absorption-driven cost rise as an efficiency problem leads to the wrong
actions.

**Lesson:** Always separate volume/absorption effects from genuine cost-efficiency changes.
"""
        )

    with st.expander("Case C — Absorption vs. marginal for a special order"):
        st.markdown(
            """
**Situation:** A customer offered to buy a large one-off batch at a price **below** the fully-loaded
(absorption) cost. The instinct was to refuse.

**What the model revealed:** The offer price was **above the marginal (variable) cost**, and the factory
had spare capacity, so the order made a **positive contribution** to already-committed fixed costs —
accepting it improved profit.

**Why it matters:** Using absorption cost for a short-run incremental decision would have wrongly rejected
a profitable order.

**Lesson:** Use **marginal** cost for short-run incremental orders (with spare capacity), absorption cost
for long-run pricing and reporting.
"""
        )

    st.info(
        "🔗 **Pattern:** A factory cost model is both a *pricing* tool and a *savings roadmap*. Absorption "
        "gives the fully-loaded cost; marginal guides short-run decisions; and wastage/yield analytics point "
        "straight at the biggest savings."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_65"):
        q1 = st.radio(
            "**1.** Absorption costing includes, in each unit's cost:",
            [
                "Only direct materials",
                "Direct costs PLUS a share of fixed factory overhead",
                "Only variable costs",
                "Only fixed overhead",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** As production volume rises, the FIXED overhead per unit:",
            [
                "Rises",
                "Falls (the fixed pot is spread over more units)",
                "Stays exactly the same",
                "Becomes a variable cost",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** If yield is 90%, the effective input cost per GOOD unit is:",
            [
                "Input cost × 0.90",
                "Input cost ÷ 0.90 (grossed up for the wasted units)",
                "Input cost − 0.90",
                "Unchanged by yield",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** For a short-run decision to accept a one-off order with spare capacity, you should compare the price to:",
            [
                "The fully-loaded absorption cost",
                "The marginal (variable) cost per unit",
                "The fixed overhead only",
                "Last year's price",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** For a typical manufacturer, the biggest cost-saving levers are usually:",
            [
                "The tax rate and depreciation",
                "Materials (procurement) and wastage/yield",
                "The discount rate",
                "Share count",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Direct costs PLUS a share of fixed factory overhead"),
            "2": (q2, "Falls (the fixed pot is spread over more units)"),
            "3": (q3, "Input cost ÷ 0.90 (grossed up for the wasted units)"),
            "4": (q4, "The marginal (variable) cost per unit"),
            "5": (q5, "Materials (procurement) and wastage/yield"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've completed Part 6 (Specialised Models)! On to Part 7 (From Model to Decision). 🎉")
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
    f"Applied Financial Models · Module 6.5 Manufacturing / Factory Cost Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
