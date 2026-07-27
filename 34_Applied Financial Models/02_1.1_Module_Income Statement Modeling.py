"""
================================================================================
APPLIED FINANCIAL MODELS
Module 1.1 — INCOME STATEMENT MODELING
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to UNDERSTAND, BUILD, INTERPRET and ACT ON an income statement model.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live, driver-based P&L builder)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_1_1_Income_Statement_Modeling.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="1.1 Income Statement Modeling — Applied Financial Models",
    layout="wide",
    page_icon="🏛️",
)

# --------------------------------------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    """Format a number as currency."""
    return f"{symbol}{x:,.{dp}f}"


def build_income_statement(
    units_y1, price_y1, vol_growth, price_growth,
    cogs_pct, sga_fixed, sga_growth, dep, interest,
    tax_rate, years=5,
):
    """
    Build a simple driver-based income statement projection.
    Returns a DataFrame (line items as rows, years as columns).
    """
    rows = [
        "Volume (units)", "Price per unit", "Revenue",
        "COGS", "Gross Profit", "Gross Margin %",
        "SG&A (fixed base)", "EBITDA", "EBITDA Margin %",
        "Depreciation", "EBIT", "Interest",
        "Profit Before Tax", "Tax", "Net Income", "Net Margin %",
    ]
    data = {r: [] for r in rows}

    units = units_y1
    price = price_y1
    sga = sga_fixed

    for y in range(years):
        if y > 0:
            units *= (1 + vol_growth / 100)
            price *= (1 + price_growth / 100)
            sga *= (1 + sga_growth / 100)

        revenue = units * price
        cogs = revenue * cogs_pct / 100
        gross = revenue - cogs
        gross_m = gross / revenue * 100 if revenue else 0
        ebitda = gross - sga
        ebitda_m = ebitda / revenue * 100 if revenue else 0
        ebit = ebitda - dep
        pbt = ebit - interest
        tax = max(pbt, 0) * tax_rate / 100
        net = pbt - tax
        net_m = net / revenue * 100 if revenue else 0

        data["Volume (units)"].append(units)
        data["Price per unit"].append(price)
        data["Revenue"].append(revenue)
        data["COGS"].append(-cogs)
        data["Gross Profit"].append(gross)
        data["Gross Margin %"].append(gross_m)
        data["SG&A (fixed base)"].append(-sga)
        data["EBITDA"].append(ebitda)
        data["EBITDA Margin %"].append(ebitda_m)
        data["Depreciation"].append(-dep)
        data["EBIT"].append(ebit)
        data["Interest"].append(-interest)
        data["Profit Before Tax"].append(pbt)
        data["Tax"].append(-tax)
        data["Net Income"].append(net)
        data["Net Margin %"].append(net_m)

    cols = [f"Year {y+1}" for y in range(years)]
    df = pd.DataFrame(data, index=cols).T
    return df


# --------------------------------------------------------------------------------
# SESSION STATE
# --------------------------------------------------------------------------------
if "quiz_submitted_11" not in st.session_state:
    st.session_state.quiz_submitted_11 = False

# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 1 · The Three-Statement Model")
st.sidebar.markdown(
    """
**Module 1.1 — Income Statement Modeling**

🟡 *Intermediate*

**You will learn to:**
- Identify revenue & cost drivers
- Build a driver-based P&L
- Read margins & profitability
- Turn the model into a recommendation
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live income "
    "statement — change the drivers and watch every line update."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏛️ 1.1 · Income Statement Modeling")
st.markdown(
    """
The **income statement** (or Profit & Loss / P&L) is where every financial model begins.
It answers the fundamental question: *is the business making a profit, and why?*

In this module you'll learn to build a **driver-based** income statement — one where revenue and
costs flow from real business assumptions (volume, price, cost ratios) rather than hard-coded numbers.
This is the foundation of the full three-statement model.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "1.1")
c2.metric("Part", "1 — 3-Statement")
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
### What is an income statement model?
An income statement model projects a company's **revenues, costs and profits** over a forecast
period (typically 3–5 years). A good model is **driver-based**: outputs are calculated from a small
set of clearly-stated assumptions, so you can change one driver and instantly see the impact.
"""
    )

    st.markdown("### The structure of a P&L (top to bottom)")
    structure = pd.DataFrame(
        {
            "Line Item": [
                "Revenue (Sales)", "− COGS", "= Gross Profit",
                "− SG&A / Operating Expenses", "= EBITDA",
                "− Depreciation & Amortisation", "= EBIT (Operating Profit)",
                "− Interest", "= Profit Before Tax (PBT)",
                "− Tax", "= Net Income (Bottom Line)",
            ],
            "What it tells you": [
                "Volume × price — the top line, driven by the market",
                "Direct cost of producing the goods/services sold",
                "Profit after direct costs — pricing & production efficiency",
                "Overheads: sales, admin, marketing (often semi-fixed)",
                "Cash operating profit before capital & financing effects",
                "Non-cash allocation of past capital spend",
                "Operating profitability after all operating costs",
                "Cost of debt financing",
                "Profit before the taxman",
                "Corporate income tax",
                "Profit attributable to shareholders",
            ],
        }
    )
    st.table(structure)

    with st.expander("🔑 Key concept 1 — Revenue drivers: Volume × Price"):
        st.markdown(
            """
Revenue should almost never be a single hard-coded number. Break it into **volume × price**:

$$\\text{Revenue} = \\text{Units Sold} \\times \\text{Price per Unit}$$

This lets you model **volume growth** (market expansion, capacity) separately from **price growth**
(inflation, premiumisation) — the two behave very differently and are driven by different forces.
"""
        )

    with st.expander("🔑 Key concept 2 — Cost behaviour: fixed vs. variable"):
        st.markdown(
            """
- **Variable costs** (e.g. COGS) move with volume — best modelled as a **% of revenue** or a cost-per-unit.
- **Fixed costs** (e.g. rent, core salaries) stay broadly flat — model them as an absolute amount that
  grows only with inflation.
- **Step costs** jump at capacity thresholds (e.g. a new production line).

Getting this split right is what makes a model react realistically when you flex the drivers.
"""
        )

    with st.expander("🔑 Key concept 3 — The margin ladder"):
        st.markdown(
            """
Margins are the quickest read on profitability and comparability:

$$\\text{Gross Margin} = \\frac{\\text{Gross Profit}}{\\text{Revenue}} \\qquad
\\text{EBITDA Margin} = \\frac{\\text{EBITDA}}{\\text{Revenue}} \\qquad
\\text{Net Margin} = \\frac{\\text{Net Income}}{\\text{Revenue}}$$

Track how each margin trends over the forecast — **rising margins** signal operating leverage or
efficiency; **falling margins** signal cost pressure or discounting.
"""
        )

    with st.expander("🔑 Key concept 4 — EBITDA vs. EBIT vs. Net Income"):
        st.markdown(
            """
- **EBITDA** — cash operating profit; useful for comparing operating performance across firms.
- **EBIT** — after depreciation; reflects the cost of using capital assets.
- **Net Income** — the true bottom line, after financing and tax.

Different audiences care about different lines — operators watch EBITDA, lenders watch EBIT/interest
cover, shareholders watch Net Income and EPS.
"""
        )

    st.success(
        "**Takeaway:** A strong income statement model is transparent and driver-based — anyone should be "
        "able to trace every number back to a stated assumption and flex it with confidence."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Building a P&L from scratch")
    st.markdown(
        "Let's build a one-year income statement for a fictional FMCG product, **'CleanSoap'**, "
        "step by step from its drivers."
    )

    st.markdown("#### Step 1 — State the assumptions")
    assumptions = pd.DataFrame(
        {
            "Driver": [
                "Volume (units)", "Price per unit", "COGS (% of revenue)",
                "SG&A (fixed)", "Depreciation", "Interest", "Tax rate",
            ],
            "Value": ["1,000,000", "€2.00", "60%", "€300,000", "€120,000", "€50,000", "30%"],
        }
    )
    st.table(assumptions)

    st.markdown("#### Step 2 — Calculate line by line")
    st.markdown(
        """
| Line Item | Calculation | Result |
|---|---|---|
| **Revenue** | 1,000,000 × €2.00 | **€2,000,000** |
| − COGS | 60% × €2,000,000 | (€1,200,000) |
| **= Gross Profit** | €2,000,000 − €1,200,000 | **€800,000** |
| − SG&A | fixed | (€300,000) |
| **= EBITDA** | €800,000 − €300,000 | **€500,000** |
| − Depreciation | fixed | (€120,000) |
| **= EBIT** | €500,000 − €120,000 | **€380,000** |
| − Interest | fixed | (€50,000) |
| **= Profit Before Tax** | €380,000 − €50,000 | **€330,000** |
| − Tax | 30% × €330,000 | (€99,000) |
| **= Net Income** | €330,000 − €99,000 | **€231,000** |
"""
    )

    st.markdown("#### Step 3 — Read the margins")
    m1, m2, m3 = st.columns(3)
    m1.metric("Gross Margin", "40.0%", help="€800k / €2,000k")
    m2.metric("EBITDA Margin", "25.0%", help="€500k / €2,000k")
    m3.metric("Net Margin", "11.6%", help="€231k / €2,000k")

    st.markdown("#### Step 4 — Interpret & recommend")
    st.info(
        "**Insight:** COGS at 60% of revenue is the single biggest lever. A 2-point reduction in COGS "
        "(60% → 58%) would add €40k of gross profit — roughly a **17% uplift to Net Income** — without "
        "selling a single extra unit. **Recommendation:** prioritise procurement/efficiency initiatives "
        "on COGS before chasing volume."
    )

    st.caption(
        "👉 Now open the **Interactive Exercises** tab and rebuild this P&L yourself — try dropping "
        "COGS to 58% and watch Net Income jump."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Build & Flex a 5-Year P&L")
    st.markdown(
        "Change the drivers on the left and watch the **full income statement** rebuild instantly. "
        "This is exactly how a driver-based model behaves in practice."
    )

    left, right = st.columns([0.32, 0.68])

    with left:
        st.markdown("##### 🎚️ Drivers")
        units_y1 = st.number_input("Year 1 volume (units)", 100_000, 5_000_000, 1_000_000, 50_000)
        price_y1 = st.number_input("Year 1 price per unit (€)", 0.5, 20.0, 2.0, 0.1)
        vol_growth = st.slider("Annual volume growth (%)", -10.0, 20.0, 5.0, 0.5)
        price_growth = st.slider("Annual price growth (%)", -5.0, 15.0, 3.0, 0.5)
        cogs_pct = st.slider("COGS (% of revenue)", 30.0, 85.0, 60.0, 0.5)
        sga_fixed = st.number_input("SG&A base (€)", 0, 2_000_000, 300_000, 25_000)
        sga_growth = st.slider("SG&A growth (%)", 0.0, 15.0, 4.0, 0.5)
        dep = st.number_input("Depreciation p.a. (€)", 0, 1_000_000, 120_000, 10_000)
        interest = st.number_input("Interest p.a. (€)", 0, 1_000_000, 50_000, 10_000)
        tax_rate = st.slider("Tax rate (%)", 0.0, 45.0, 30.0, 1.0)

    with right:
        df_is = build_income_statement(
            units_y1, price_y1, vol_growth, price_growth,
            cogs_pct, sga_fixed, sga_growth, dep, interest, tax_rate,
        )

        # KPI cards for Year 1 vs Year 5
        rev1, rev5 = df_is.loc["Revenue", "Year 1"], df_is.loc["Revenue", "Year 5"]
        ni1, ni5 = df_is.loc["Net Income", "Year 1"], df_is.loc["Net Income", "Year 5"]
        nm5 = df_is.loc["Net Margin %", "Year 5"]

        k1, k2, k3 = st.columns(3)
        k1.metric("Year 5 Revenue", money(rev5), f"{(rev5/rev1-1)*100:,.1f}% vs Y1")
        k2.metric("Year 5 Net Income", money(ni5), f"{(ni5/ni1-1)*100:,.1f}% vs Y1" if ni1 else None)
        k3.metric("Year 5 Net Margin", f"{nm5:,.1f}%")

        st.markdown("##### 📄 Projected Income Statement")

        # Format for display
        pct_rows = ["Gross Margin %", "EBITDA Margin %", "Net Margin %"]
        unit_rows = ["Volume (units)", "Price per unit"]

        def fmt_row(row):
            if row.name in pct_rows:
                return row.map(lambda v: f"{v:,.1f}%")
            if row.name == "Price per unit":
                return row.map(lambda v: f"€{v:,.2f}")
            if row.name == "Volume (units)":
                return row.map(lambda v: f"{v:,.0f}")
            return row.map(lambda v: f"€{v:,.0f}")

        disp = df_is.apply(fmt_row, axis=1)
        st.dataframe(disp, use_container_width=True)

        st.markdown("##### 📈 Revenue vs. Net Income trajectory")
        chart_df = df_is.loc[["Revenue", "EBITDA", "Net Income"]].T
        st.line_chart(chart_df)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    ch1, ch2 = st.columns(2)
    with ch1:
        st.markdown(
            """
1. **Operating leverage:** Set volume growth to 10% but keep SG&A growth at 4%. Watch how
   Net Margin *expands* over time — costs grow slower than revenue.
2. **Margin squeeze:** Push COGS to 75%. How many extra units would you need to hold Net Income flat?
"""
        )
    with ch2:
        st.markdown(
            """
3. **Pricing power:** Set volume growth to 0% and price growth to 6%. Can price alone drive
   profit growth?
4. **Break-even stress:** Lower price to €1.20. At what COGS % does Net Income turn negative?
"""
        )

    # Download the model output
    st.download_button(
        "⬇️ Download this income statement (CSV)",
        df_is.to_csv().encode("utf-8"),
        "income_statement_projection.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — FMCG manufacturer: the COGS lever", expanded=True):
        st.markdown(
            """
**Situation:** A consumer-goods factory produces 200+ SKUs. COGS runs at ~62% of revenue, dominated
by raw materials and packaging. Volume growth is modest (~3%) in a mature market.

**Modeling approach:**
- Split revenue by **volume × price** per SKU category.
- Model raw material cost as **% of revenue**, sensitised to commodity price swings.
- Treat factory overheads as **semi-fixed** — flat until a capacity step-change.

**Insight the model reveals:** With low volume growth, **cost efficiency (COGS %) and price realisation
matter far more than volume**. A 1-point COGS improvement often beats a full year of volume growth.

**Recommendation:** Direct management attention to procurement, wastage reduction and premium pricing
rather than chasing volume in a saturated market.
"""
        )

    with st.expander("Case B — SaaS / subscription business: the growth-vs-margin trade-off"):
        st.markdown(
            """
**Situation:** A software company grows subscribers at 30%+ but spends heavily on sales & marketing.

**Modeling approach:**
- Revenue = **subscribers × ARPU** (average revenue per user), with churn built in.
- COGS is low (hosting, support) → high gross margins (~80%).
- SG&A (esp. sales & marketing) is the swing factor and often grows *with* revenue.

**Insight the model reveals:** The business can be **gross-margin rich but net-loss making** because
S&M is front-loaded to acquire customers. The model shows *when* the business crosses into profit.

**Recommendation:** Track the path to profitability; test how much S&M can be trimmed before growth stalls.
"""
        )

    with st.expander("Case C — Capex-heavy manufacturer: depreciation drag"):
        st.markdown(
            """
**Situation:** A firm invests €6m in new automated lines. EBITDA looks strong, but a big new
depreciation charge hits EBIT.

**Modeling approach:**
- Keep **EBITDA** as the operating performance measure (excludes depreciation).
- Model **depreciation** from the capital schedule (a supporting schedule — see Module 1.5).
- Watch the gap between EBITDA and EBIT widen after the investment.

**Insight the model reveals:** A project can be **EBITDA-accretive but EBIT-dilutive** in early years
due to depreciation — important when management is measured on EBIT.

**Recommendation:** Communicate both EBITDA and EBIT effects to stakeholders; align incentives to the
right metric so a good investment isn't rejected on a short-term EBIT dip.
"""
        )

    st.info(
        "🔗 **Connecting the dots:** In every case, the *structure* of the P&L is the same — what changes "
        "is *which driver dominates*. Identifying that dominant driver is the analyst's real job."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_11"):
        q1 = st.radio(
            "**1.** Which formula correctly builds a driver-based revenue line?",
            [
                "Revenue = last year's revenue + a fixed € amount",
                "Revenue = Units Sold × Price per Unit",
                "Revenue = EBITDA − Depreciation",
                "Revenue = Gross Profit + COGS − Tax",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** COGS is best modelled as which type of cost?",
            [
                "Purely fixed — a flat € amount every year",
                "Variable — typically a % of revenue or cost-per-unit",
                "A step cost that never changes",
                "Equal to depreciation",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** EBITDA differs from EBIT because EBITDA:",
            [
                "Is calculated after tax",
                "Excludes depreciation & amortisation",
                "Includes interest expense",
                "Is always larger than revenue",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A company has Revenue €2,000k and Gross Profit €800k. Its gross margin is:",
            ["25%", "40%", "60%", "160%"],
            index=None,
        )
        q5 = st.radio(
            "**5.** 'Operating leverage' in a P&L model means:",
            [
                "Revenue grows faster than variable-only costs, so margins expand as fixed costs are spread wider",
                "Interest expense rises with debt",
                "Tax rate falls as profit rises",
                "Depreciation equals capital expenditure",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Revenue = Units Sold × Price per Unit"),
            "2": (q2, "Variable — typically a % of revenue or cost-per-unit"),
            "3": (q3, "Excludes depreciation & amortisation"),
            "4": (q4, "40%"),
            "5": (q5, "Revenue grows faster than variable-only costs, so margins expand as fixed costs are spread wider"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Outstanding — you've mastered the fundamentals of income statement modeling! 🎉")
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

        st.caption(
            "Calculation check for Q4: Gross Margin = Gross Profit / Revenue = 800 / 2,000 = 40%."
        )

st.markdown("---")
st.caption(
    f"Applied Financial Models · Module 1.1 Income Statement Modeling · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
