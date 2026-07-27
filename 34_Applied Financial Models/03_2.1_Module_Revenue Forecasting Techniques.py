"""
================================================================================
APPLIED FINANCIAL MODELS
Module 2.1 — REVENUE FORECASTING TECHNIQUES
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
the main ways to forecast revenue: top-down, bottom-up, volume x price, and
market-share methods — and when to use each.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (three forecasting methods, side by side)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_2_1_Revenue_Forecasting_Techniques.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="2.1 Revenue Forecasting Techniques — Applied Financial Models",
    layout="wide",
    page_icon="📊",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def project(base, growth_pct, years):
    """Return a list of values growing at growth_pct for `years` periods (year 1 = base)."""
    out = []
    val = base
    for y in range(years):
        if y > 0:
            val *= (1 + growth_pct / 100)
        out.append(val)
    return out


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 2 · Forecasting & Budgeting Models")
st.sidebar.markdown(
    """
**Module 2.1 — Revenue Forecasting Techniques**

🟡 *Intermediate*

**You will learn to:**
- Forecast revenue top-down vs. bottom-up
- Use the volume × price method
- Apply the market-share approach
- Choose the right technique for the situation
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to forecast revenue three "
    "different ways and compare the results side by side."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("📊 2.1 · Revenue Forecasting Techniques")
st.markdown(
    """
Revenue is the **top line** — and the single most important (and most uncertain) number in almost every
model. Get it wrong and everything below it is wrong too. This module opens Part 2 by covering the main
techniques professionals use to forecast revenue credibly.

The golden rule from Module 1.1 still applies: **never hard-code a single revenue number** — build it
from drivers so it can be understood, challenged, and flexed.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "2.1")
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
### The two directions of forecasting
Every revenue forecast is built in one of two directions — and the best analysts often do **both** and
reconcile them.
"""
    )

    directions = pd.DataFrame(
        {
            "Approach": ["Top-Down", "Bottom-Up"],
            "Starts from": [
                "The total market, then your share of it",
                "Individual units/customers, then adds them up",
            ],
            "Best for": [
                "New markets, strategy, sanity-checking, quick estimates",
                "Detailed budgets, operational plans, mature businesses",
            ],
            "Risk": [
                "Can be optimistic / detached from operational reality",
                "Can miss the big picture; time-consuming",
            ],
        }
    )
    st.table(directions)

    st.markdown("### The core methods")
    methods = pd.DataFrame(
        {
            "Method": ["Volume × Price", "Market Share", "Growth-Rate (trend)"],
            "Formula / logic": [
                "Revenue = Units sold × Price per unit",
                "Revenue = Total market size × Your market share %",
                "Revenue = Last period × (1 + growth rate)",
            ],
            "When to use": [
                "You know units and pricing (most operational forecasts)",
                "New products / markets where share is the key lever",
                "Stable, mature businesses with a reliable trend",
            ],
        }
    )
    st.table(methods)

    with st.expander("🔑 Method 1 — Volume × Price (bottom-up workhorse)"):
        st.markdown(
            """
The most widely used operational method:

$$\\text{Revenue} = \\text{Volume} \\times \\text{Price}$$

Model **volume growth** (capacity, demand, market expansion) and **price growth** (inflation,
premiumisation) *separately* — they behave differently. For multi-product businesses, do this per
product line or category and sum up.
"""
        )

    with st.expander("🔑 Method 2 — Market share (top-down)"):
        st.markdown(
            """
$$\\text{Revenue} = \\text{Total Addressable Market (TAM)} \\times \\text{Market Share \\%}$$

Start with the size of the whole market, then estimate the slice you can win. Powerful for new products
or entering new markets, but only as good as your market-size and share assumptions — always sanity-check
the implied units against capacity.
"""
        )

    with st.expander("🔑 Method 3 — Growth-rate / trend"):
        st.markdown(
            """
$$\\text{Revenue}_{t} = \\text{Revenue}_{t-1} \\times (1 + g)$$

Simple and quick — extend a historical trend or CAGR forward. Fine for **stable, mature** businesses,
but dangerous when the future differs from the past (new competition, market shifts, one-off events).
"""
        )

    with st.expander("🔑 Best practice — Triangulate and reconcile"):
        st.markdown(
            """
Professionals rarely trust a single method. A strong forecast:
1. Builds **bottom-up** (volume × price) for operational credibility.
2. Builds **top-down** (market share) as an independent cross-check.
3. **Reconciles** the two — if they diverge widely, an assumption needs revisiting.

Where the two approaches meet, you have a forecast you can defend.
"""
        )

    st.success(
        "**Takeaway:** Build revenue from drivers, not a single guess. Use volume × price for operational "
        "detail, market share for the big picture, and reconcile top-down with bottom-up to build confidence."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Examples — The same business, three methods")
    st.markdown("Forecasting Year-1 revenue for our fictional product **'CleanSoap'** three different ways.")

    st.markdown("#### Method 1 — Volume × Price (bottom-up)")
    st.markdown(
        """
- Units sold: **1,000,000**
- Price per unit: **€2.00**

$$\\text{Revenue} = 1{,}000{,}000 \\times €2.00 = \\mathbf{€2{,}000{,}000}$$
"""
    )

    st.markdown("#### Method 2 — Market share (top-down)")
    st.markdown(
        """
- Total soap market: **€40,000,000**
- Our market share: **5%**

$$\\text{Revenue} = €40{,}000{,}000 \\times 5\\% = \\mathbf{€2{,}000{,}000}$$
"""
    )

    st.markdown("#### Method 3 — Growth-rate (trend)")
    st.markdown(
        """
- Last year's revenue: **€1,900,000**
- Expected growth: **5.3%**

$$\\text{Revenue} = €1{,}900{,}000 \\times (1 + 5.3\\%) = \\mathbf{€2{,}000{,}000}$$
"""
    )

    st.markdown("#### The reconciliation")
    recon = pd.DataFrame(
        {
            "Method": ["Volume × Price", "Market Share", "Growth-Rate"],
            "Year-1 Revenue": ["€2,000,000", "€2,000,000", "€2,000,000"],
            "Implied cross-check": [
                "Implies 5% share of a €40m market ✓",
                "Implies 1m units at €2.00 ✓",
                "Consistent with both above ✓",
            ],
        }
    )
    st.table(recon)

    st.info(
        "**Insight:** All three methods converge on €2.0m — that's a *reconciled* forecast you can defend. "
        "If the market-share method had implied, say, 2m units but the factory can only make 1.2m, you'd "
        "know an assumption was unrealistic. **Convergence builds confidence; divergence flags risk.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Forecast Revenue Three Ways")
    st.markdown(
        "Set the drivers for each method and compare the multi-year forecasts side by side. Watch how the "
        "three approaches converge — or diverge."
    )

    years = st.slider("Forecast horizon (years)", 3, 10, 5, 1)

    st.markdown("---")
    colA, colB, colC = st.columns(3)

    with colA:
        st.markdown("##### 🔢 Volume × Price")
        units = st.number_input("Year-1 units", 10_000, 50_000_000, 1_000_000, 50_000)
        price = st.number_input("Year-1 price (€)", 0.10, 100.0, 2.0, 0.10)
        vol_g = st.slider("Volume growth (%)", -10.0, 25.0, 5.0, 0.5)
        price_g = st.slider("Price growth (%)", -5.0, 15.0, 3.0, 0.5)

    with colB:
        st.markdown("##### 🥧 Market Share")
        tam = st.number_input("Year-1 market size (€)", 1_000_000, 5_000_000_000, 40_000_000, 1_000_000)
        share = st.slider("Market share (%)", 0.1, 100.0, 5.0, 0.1)
        tam_g = st.slider("Market growth (%)", -10.0, 25.0, 4.0, 0.5)
        share_g = st.slider("Share gain per year (pp)", -2.0, 5.0, 0.3, 0.1,
                            help="Percentage points of share gained each year")

    with colC:
        st.markdown("##### 📈 Growth-Rate (trend)")
        last_rev = st.number_input("Last year's revenue (€)", 100_000, 5_000_000_000, 1_900_000, 50_000)
        trend_g = st.slider("Trend growth (%)", -10.0, 25.0, 5.3, 0.1)

    # Build the three forecasts
    vp_units = project(units, vol_g, years)
    vp_price = project(price, price_g, years)
    vp_rev = [u * p for u, p in zip(vp_units, vp_price)]

    ms_tam = project(tam, tam_g, years)
    ms_rev = []
    sh = share
    for y in range(years):
        if y > 0:
            sh += share_g
        sh = max(0.0, min(sh, 100.0))
        ms_rev.append(ms_tam[y] * sh / 100)

    gr_rev = []
    val = last_rev * (1 + trend_g / 100)  # year 1 already grown from last year
    for y in range(years):
        if y > 0:
            val *= (1 + trend_g / 100)
        gr_rev.append(val)

    idx = [f"Year {y+1}" for y in range(years)]
    compare = pd.DataFrame(
        {"Volume × Price": vp_rev, "Market Share": ms_rev, "Growth-Rate": gr_rev}, index=idx
    )

    st.markdown("##### 📊 Forecast comparison")
    k1, k2, k3 = st.columns(3)
    k1.metric("Vol × Price — Yr " + str(years), money(vp_rev[-1]))
    k2.metric("Market Share — Yr " + str(years), money(ms_rev[-1]))
    k3.metric("Growth-Rate — Yr " + str(years), money(gr_rev[-1]))

    spread = max(vp_rev[-1], ms_rev[-1], gr_rev[-1]) - min(vp_rev[-1], ms_rev[-1], gr_rev[-1])
    avg = (vp_rev[-1] + ms_rev[-1] + gr_rev[-1]) / 3
    spread_pct = (spread / avg * 100) if avg else 0

    if spread_pct < 5:
        st.success(
            f"✅ **Strong convergence** — the three methods are within {spread_pct:.1f}% of each other in "
            f"Year {years}. This is a well-reconciled, defensible forecast."
        )
    elif spread_pct < 15:
        st.info(
            f"🔎 **Moderate spread** ({spread_pct:.1f}% in Year {years}). Worth understanding what's driving "
            "the difference before finalising."
        )
    else:
        st.warning(
            f"⚠️ **Wide divergence** ({spread_pct:.1f}% in Year {years}). At least one method's assumptions "
            "need revisiting — the methods disagree materially."
        )

    st.line_chart(compare)

    disp = compare.apply(lambda col: col.map(money))
    st.dataframe(disp, use_container_width=True)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Reconcile them:** Adjust the drivers so all three methods land within 5% (green convergence).
2. **Capacity check:** In Vol × Price, note the Year-5 units. Could your factory actually produce them?
"""
        )
    with e2:
        st.markdown(
            """
3. **Optimism trap:** Push 'share gain per year' to 5pp. Does the market-share method run away from reality?
4. **Trend break:** Set trend growth to 20% — is extrapolating the past still credible?
"""
        )

    st.download_button(
        "⬇️ Download the three forecasts (CSV)",
        compare.to_csv().encode("utf-8"),
        "revenue_forecasts_comparison.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The bottom-up factory budget", expanded=True):
        st.markdown(
            """
**Situation:** A manufacturer with 200+ SKUs needs next year's revenue budget.

**Method used:** **Bottom-up, volume × price** per SKU category. Volumes come from the sales team and
capacity plan; prices reflect agreed lists and expected inflation.

**Why it fits:** A mature, operational business needs a granular, defensible budget the operations team
can be held accountable to.

**Lesson:** For operational budgets in established businesses, bottom-up volume × price is the workhorse.
"""
        )

    with st.expander("Case B — The new-product launch (top-down)"):
        st.markdown(
            """
**Situation:** A company launches a new product with no sales history.

**Method used:** **Top-down, market share.** Estimate the total addressable market, then a realistic
share ramp (e.g. 1% → 3% → 5% over three years), cross-checked against capacity and marketing spend.

**Why it fits:** With no history, bottom-up units are guesswork — the market-size lens is more credible,
provided the share assumptions are sanity-checked.

**Lesson:** For new products/markets, start top-down — then validate the implied units bottom-up.
"""
        )

    with st.expander("Case C — When the methods disagreed (and it mattered)"):
        st.markdown(
            """
**Situation:** A board forecast built top-down implied 40% growth; the bottom-up sales pipeline supported
only 15%.

**What happened:** The **divergence itself was the insight.** The top-down number assumed share gains the
sales team had no plan to deliver. Reconciling the two led to a credible ~18% forecast — and a realistic
resourcing plan to hit it.

**Why it matters:** A single method would have hidden the gap; triangulation exposed it.

**Lesson:** When top-down and bottom-up disagree, don't average blindly — investigate *why*, and fix the
weak assumption.
"""
        )

    st.info(
        "🔗 **Pattern:** The right technique depends on context — bottom-up for operational detail, "
        "top-down for new/strategic questions — and the greatest insight often comes from *reconciling both*."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_21"):
        q1 = st.radio(
            "**1.** A top-down revenue forecast starts from:",
            [
                "Individual units sold, added up",
                "The total market size, then your share of it",
                "Last year's net income",
                "The depreciation schedule",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The volume × price method calculates revenue as:",
            [
                "Market size × share %",
                "Units sold × price per unit",
                "Last period × (1 + growth)",
                "EBIT × tax rate",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The market-share method is MOST appropriate when:",
            [
                "Forecasting a mature product with a long sales history",
                "Launching a new product / entering a new market",
                "Calculating depreciation",
                "Building a debt schedule",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Why is it best practice to build both top-down and bottom-up forecasts?",
            [
                "To make the model larger",
                "So the two can be reconciled — convergence builds confidence, divergence flags risk",
                "Because tax rules require it",
                "To avoid using volume × price",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The biggest risk of a simple growth-rate (trend) forecast is that:",
            [
                "It is always too low",
                "It assumes the future behaves like the past, which may not hold",
                "It cannot be put in a spreadsheet",
                "It ignores the tax rate",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The total market size, then your share of it"),
            "2": (q2, "Units sold × price per unit"),
            "3": (q3, "Launching a new product / entering a new market"),
            "4": (q4, "So the two can be reconciled — convergence builds confidence, divergence flags risk"),
            "5": (q5, "It assumes the future behaves like the past, which may not hold"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered revenue forecasting! On to Module 2.2 (Cost & OPEX Forecasting). 🎉")
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
    f"Applied Financial Models · Module 2.1 Revenue Forecasting Techniques · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
