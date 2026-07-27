"""
================================================================================
APPLIED FINANCIAL MODELS
Module 2.3 — BUDGET vs. ACTUAL (VARIANCE) MODELS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to compare budget with actual results, decompose the variance into price and
volume effects (the variance bridge), classify favourable/adverse variances, and
build a rolling forecast.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live variance bridge + rolling forecast)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_2_3_Budget_vs_Actual_Variance_Models.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="2.3 Budget vs. Actual (Variance) Models — Applied Financial Models",
    layout="wide",
    page_icon="📊",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def variance_label(actual, budget, cost=False):
    """Return F (favourable) or A (adverse). For costs, lower actual is favourable."""
    diff = actual - budget
    if abs(diff) < 1e-9:
        return "—", 0.0
    if cost:
        return ("F" if diff < 0 else "A"), diff
    return ("F" if diff > 0 else "A"), diff


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 2 · Forecasting & Budgeting Models")
st.sidebar.markdown(
    """
**Module 2.3 — Budget vs. Actual (Variance) Models**

🟡 *Intermediate*

**You will learn to:**
- Compare budget vs. actual results
- Decompose variance into price & volume
- Classify favourable vs. adverse variances
- Build a rolling forecast
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live **variance "
    "bridge** — split any gap into price and volume effects."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("📊 2.3 · Budget vs. Actual (Variance) Models")
st.markdown(
    """
A forecast is only useful if you later check it against reality. **Variance analysis** compares what you
**budgeted** with what **actually happened**, and — crucially — explains *why* they differ. Was revenue
up because you sold more (volume) or charged more (price)? Did costs rise from inflation or inefficiency?

This module covers variance analysis, the **price/volume bridge**, favourable vs. adverse classification,
and how variances feed a **rolling forecast**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "2.3")
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
### What is variance analysis?
**Variance = Actual − Budget.** But the number alone isn't enough — the skill is *explaining* it so
management can act. A €100k revenue shortfall from losing customers needs a very different response than
one from a deliberate price cut that won market share.
"""
    )

    st.markdown("### Favourable vs. adverse")
    fa = pd.DataFrame(
        {
            "Item": ["Revenue / Profit", "Costs"],
            "Favourable (F) when…": ["Actual > Budget (more is good)", "Actual < Budget (less is good)"],
            "Adverse (A) when…": ["Actual < Budget", "Actual > Budget"],
        }
    )
    st.table(fa)

    st.markdown(
        """
### The price/volume bridge (the heart of this module)
A revenue variance almost always has two causes: you sold a different **quantity** (volume) and/or at a
different **price**. The bridge splits the total variance into these two effects:
"""
    )
    st.latex(r"\text{Volume Variance} = (\text{Actual Volume} - \text{Budget Volume}) \times \text{Budget Price}")
    st.latex(r"\text{Price Variance} = (\text{Actual Price} - \text{Budget Price}) \times \text{Actual Volume}")
    st.markdown(
        r"""
$$\text{Total Variance} = \text{Volume Variance} + \text{Price Variance}$$
"""
    )

    with st.expander("🔑 Concept 1 — Why decompose price vs. volume?"):
        st.markdown(
            """
The *same* revenue miss can mean opposite things:
- **Volume-driven miss** → a demand or market-share problem (fix sales/marketing).
- **Price-driven miss** → a pricing or discounting problem (fix commercial policy).

Decomposing the variance tells management **which lever to pull**. A single "revenue down €100k" number
hides the diagnosis; the bridge reveals it.
"""
        )

    with st.expander("🔑 Concept 2 — The variance bridge (waterfall)"):
        st.markdown(
            """
A **bridge** (or waterfall) visually walks from budget to actual, one effect at a time:

```
Budget Revenue ──► + Volume effect ──► + Price effect ──► Actual Revenue
   2,000,000          +100,000            −50,000           2,050,000
```

Each bar shows a driver's contribution. Bridges are the standard way to present variances to
management because they answer "what moved, and by how much?" at a glance.
"""
        )

    with st.expander("🔑 Concept 3 — Cost variances (rate vs. usage)"):
        st.markdown(
            """
Costs decompose similarly:
- **Usage/efficiency variance** = (Actual quantity − Budget quantity) × Budget rate — did we use more
  input than planned?
- **Rate/price variance** = (Actual rate − Budget rate) × Actual quantity — did the input cost more?

This separates *operational* efficiency from *market* price movements — a key management distinction.
"""
        )

    with st.expander("🔑 Concept 4 — Rolling forecasts"):
        st.markdown(
            """
A **rolling forecast** continually updates the outlook as actuals come in — always projecting, say, the
next 12 months. Rather than a static annual budget that goes stale, you replace budgeted months with
actuals and re-forecast the remainder.

Variances feed this directly: if Q1 volume ran 5% ahead, you might raise the full-year outlook. Rolling
forecasts keep decisions based on the *latest* reality.
"""
        )

    st.success(
        "**Takeaway:** Variance analysis isn't about blame — it's about *explanation*. Decompose the gap "
        "into price and volume (and rate vs. usage for costs), present it as a bridge, and feed it into a "
        "rolling forecast so decisions stay current."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Decomposing a revenue variance")
    st.markdown("CleanSoap budgeted vs. actual results for the quarter.")

    st.markdown("#### The numbers")
    st.markdown(
        """
| | Budget | Actual |
|---|---|---|
| Volume (units) | 1,000,000 | 1,050,000 |
| Price per unit | €2.00 | €1.95 |
| **Revenue** | **€2,000,000** | **€2,047,500** |

Total revenue variance = 2,047,500 − 2,000,000 = **+€47,500 (Favourable)**
"""
    )

    st.markdown("#### Step 1 — Volume variance")
    st.markdown(
        """
$$(\\text{Actual Vol} - \\text{Budget Vol}) \\times \\text{Budget Price}$$
$$(1{,}050{,}000 - 1{,}000{,}000) \\times €2.00 = \\mathbf{+€100{,}000 \\text{ (F)}}$$

We sold 50,000 more units — worth €100k at the budgeted price.
"""
    )

    st.markdown("#### Step 2 — Price variance")
    st.markdown(
        """
$$(\\text{Actual Price} - \\text{Budget Price}) \\times \\text{Actual Vol}$$
$$(€1.95 - €2.00) \\times 1{,}050{,}000 = \\mathbf{-€52{,}500 \\text{ (A)}}$$

We charged €0.05 less per unit across all 1,050,000 units sold — costing €52.5k.
"""
    )

    st.markdown("#### Step 3 — The bridge")
    st.markdown(
        """
| Step | € | Type |
|---|---|---|
| Budget revenue | 2,000,000 | — |
| + Volume variance | +100,000 | Favourable |
| + Price variance | −52,500 | Adverse |
| **= Actual revenue** | **2,047,500** | **+47,500 net F** |
"""
    )

    st.info(
        "**Insight:** The headline (+€47.5k favourable) hides two opposing stories: **strong volume** "
        "(+€100k) partly given back by **discounting** (−€52.5k). The management action is clear — the "
        "extra volume is great, but investigate *why* price slipped. A single number would have missed this entirely."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Build a Price/Volume Bridge")
    st.markdown(
        "Enter your budget and actual figures. The model decomposes the revenue variance into **volume** "
        "and **price** effects — and reconciles them back to the total."
    )

    left, right = st.columns([0.35, 0.65])
    with left:
        st.markdown("##### 📋 Budget")
        bud_vol = st.number_input("Budget volume (units)", 1_000, 50_000_000, 1_000_000, 10_000)
        bud_price = st.number_input("Budget price (€)", 0.10, 1000.0, 2.00, 0.05)
        st.markdown("##### 📊 Actual")
        act_vol = st.number_input("Actual volume (units)", 1_000, 50_000_000, 1_050_000, 10_000)
        act_price = st.number_input("Actual price (€)", 0.10, 1000.0, 1.95, 0.05)

    with right:
        bud_rev = bud_vol * bud_price
        act_rev = act_vol * act_price
        total_var = act_rev - bud_rev
        vol_var = (act_vol - bud_vol) * bud_price
        price_var = (act_price - bud_price) * act_vol

        k1, k2, k3 = st.columns(3)
        k1.metric("Budget revenue", money(bud_rev))
        k2.metric("Actual revenue", money(act_rev))
        k3.metric("Total variance", money(total_var),
                  "Favourable" if total_var >= 0 else "Adverse",
                  delta_color="normal" if total_var >= 0 else "inverse")

        k4, k5 = st.columns(2)
        k4.metric("Volume variance", money(vol_var), "F" if vol_var >= 0 else "A",
                  delta_color="normal" if vol_var >= 0 else "inverse")
        k5.metric("Price variance", money(price_var), "F" if price_var >= 0 else "A",
                  delta_color="normal" if price_var >= 0 else "inverse")

        # reconciliation check
        recon_ok = abs((vol_var + price_var) - total_var) < 1
        if recon_ok:
            st.success(f"✅ Bridge reconciles: Volume ({money(vol_var)}) + Price ({money(price_var)}) = Total ({money(total_var)}).")
        else:
            st.error("❌ Reconciliation error.")

        # bridge as a table + chart
        bridge = pd.DataFrame(
            {
                "Step": ["Budget", "Volume effect", "Price effect", "Actual"],
                "€": [bud_rev, vol_var, price_var, act_rev],
            }
        )
        st.markdown("##### 🌉 Variance Bridge")
        disp = bridge.copy()
        disp["€"] = disp["€"].map(money)
        st.table(disp)

        # simple cumulative waterfall for the chart
        waterfall = pd.DataFrame(
            {"Cumulative revenue (€)": [bud_rev, bud_rev + vol_var, bud_rev + vol_var + price_var]},
            index=["Budget", "+ Volume", "+ Price (= Actual)"],
        )
        st.bar_chart(waterfall)

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Rolling Forecast Updater")
    st.markdown(
        "You budgeted a full year. Some months are now **actuals**. See how the full-year outlook updates "
        "when you re-forecast the remaining months based on the trend so far."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        annual_budget = st.number_input("Full-year budget (€)", 100_000, 5_000_000_000, 24_000_000, 500_000)
        months_actual = st.slider("Months of actuals so far", 1, 11, 3, 1)
    with c2:
        ytd_performance = st.slider("Actuals vs. budget so far (%)", 70, 130, 108, 1,
                                    help="e.g. 108 = running 8% ahead of budget")
    with c3:
        rest_of_year = st.slider("Expected performance for rest of year (%)", 70, 130, 103, 1,
                                 help="Your re-forecast for the remaining months")

    monthly_budget = annual_budget / 12
    actual_ytd = monthly_budget * months_actual * (ytd_performance / 100)
    remaining_months = 12 - months_actual
    forecast_rest = monthly_budget * remaining_months * (rest_of_year / 100)
    new_full_year = actual_ytd + forecast_rest
    fy_variance = new_full_year - annual_budget

    m1, m2, m3 = st.columns(3)
    m1.metric("Actual YTD", money(actual_ytd))
    m2.metric("Re-forecast (rest)", money(forecast_rest))
    m3.metric("New full-year outlook", money(new_full_year),
              f"{money(fy_variance)} vs budget",
              delta_color="normal" if fy_variance >= 0 else "inverse")

    if fy_variance > 0:
        st.success(f"✅ On current trends, you're tracking **{money(fy_variance)} ahead** of the annual budget.")
    elif fy_variance < 0:
        st.warning(f"⚠️ On current trends, you're tracking **{money(-fy_variance)} behind** the annual budget.")
    else:
        st.info("On track to hit the annual budget exactly.")

    st.caption(
        "🧠 A rolling forecast replaces budgeted months with actuals and re-forecasts the rest — keeping "
        "the outlook based on the latest reality rather than a stale annual plan."
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The favourable variance that hid a problem", expanded=True):
        st.markdown(
            """
**Situation:** A business unit reported revenue slightly *ahead* of budget and celebrated.

**What the bridge revealed:** The favourable total masked a **large adverse price variance** offset by
an even larger favourable volume variance driven by deep discounting. They were "buying" revenue by
sacrificing margin.

**Why it matters:** The headline looked fine; the *composition* was alarming. Profit was actually down
despite revenue being up.

**Lesson:** Never judge performance on the net variance alone — always decompose it.
"""
        )

    with st.expander("Case B — Rate vs. usage in the factory"):
        st.markdown(
            """
**Situation:** Raw-material costs came in €200k over budget.

**What the bridge revealed:** Splitting into **rate** vs. **usage**: €150k was a **rate** variance
(commodity prices rose — outside the plant's control) and only €50k was a **usage** variance (efficiency).

**Why it matters:** Holding the plant accountable for the full €200k would be unfair and misdirect effort.
The usage portion is the controllable, actionable part.

**Lesson:** Separating rate from usage tells you what's *controllable* versus *market-driven*.
"""
        )

    with st.expander("Case C — Rolling forecast beats the annual budget"):
        st.markdown(
            """
**Situation:** A company's static annual budget was obsolete by Q2 after a major market shift.

**How rolling forecasting helped:** By replacing actual months and re-forecasting the remainder each
month, leadership always had a realistic 12-month outlook — and could adjust spending and hiring in time
rather than discovering the miss at year-end.

**Why it matters:** Static budgets assume the year plays out as planned; rolling forecasts adapt to reality.

**Lesson:** In volatile environments, a rolling forecast is far more decision-useful than a fixed annual budget.
"""
        )

    st.info(
        "🔗 **Pattern:** Variance analysis converts 'what happened' into 'why it happened' and 'what to do "
        "next'. Decomposition reveals the story; rolling forecasts keep it current."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_23"):
        q1 = st.radio(
            "**1.** A variance is defined as:",
            [
                "Budget − Last year",
                "Actual − Budget",
                "Revenue − Costs",
                "Price × Volume",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** For a REVENUE line, a favourable (F) variance occurs when:",
            [
                "Actual is less than budget",
                "Actual is greater than budget",
                "Actual equals last year",
                "Costs fall",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The volume variance is calculated as:",
            [
                "(Actual price − Budget price) × Actual volume",
                "(Actual volume − Budget volume) × Budget price",
                "Actual revenue − Budget revenue",
                "Budget volume × Actual price",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Why decompose a revenue variance into price and volume effects?",
            [
                "To make the report longer",
                "Because each points to a different management action (pricing vs. demand)",
                "Because tax rules require it",
                "To avoid calculating total revenue",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** A rolling forecast is best described as:",
            [
                "A budget that never changes all year",
                "An outlook continually updated with actuals, always projecting a set period ahead",
                "A one-off valuation",
                "A depreciation schedule",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Actual − Budget"),
            "2": (q2, "Actual is greater than budget"),
            "3": (q3, "(Actual volume − Budget volume) × Budget price"),
            "4": (q4, "Because each points to a different management action (pricing vs. demand)"),
            "5": (q5, "An outlook continually updated with actuals, always projecting a set period ahead"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered variance analysis! On to Module 2.4 (Driver-Based Planning). 🎉")
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
    f"Applied Financial Models · Module 2.3 Budget vs. Actual (Variance) Models · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
