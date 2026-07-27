"""
================================================================================
APPLIED FINANCIAL MODELS
Module 1.5 — SUPPORTING SCHEDULES
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to build the supporting schedules that power a three-statement model:
depreciation, debt & interest, working capital, and tax schedules.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (live multi-year roll-forward schedules)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_1_5_Supporting_Schedules.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="1.5 Supporting Schedules — Applied Financial Models",
    layout="wide",
    page_icon="🏛️",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def depreciation_schedule(open_ppe, capex_per_yr, useful_life, years):
    """Straight-line depreciation roll-forward."""
    rows = {"Opening PP&E": [], "+ Capex": [], "− Depreciation": [], "= Closing PP&E": []}
    ppe = open_ppe
    for _ in range(years):
        opening = ppe
        capex = capex_per_yr
        # simple approach: depreciate (opening + capex) over remaining useful life
        dep = (opening + capex) / useful_life if useful_life > 0 else 0
        closing = opening + capex - dep
        rows["Opening PP&E"].append(opening)
        rows["+ Capex"].append(capex)
        rows["− Depreciation"].append(-dep)
        rows["= Closing PP&E"].append(closing)
        ppe = closing
    return rows


def debt_schedule(open_debt, annual_repay, interest_rate, years):
    """Debt roll-forward with interest on opening balance."""
    rows = {"Opening Debt": [], "− Repayment": [], "= Closing Debt": [], "Interest expense": []}
    debt = open_debt
    for _ in range(years):
        opening = debt
        repay = min(annual_repay, opening)
        interest = opening * interest_rate / 100
        closing = opening - repay
        rows["Opening Debt"].append(opening)
        rows["− Repayment"].append(-repay)
        rows["= Closing Debt"].append(closing)
        rows["Interest expense"].append(interest)
        debt = closing
    return rows


def working_capital_schedule(revenue0, growth, cogs_pct, dso, dio, dpo, years):
    """Working capital balances and cash impact of the change each year."""
    rows = {"Revenue": [], "Receivables": [], "Inventory": [], "Payables": [],
            "Net WC": [], "Δ Net WC (cash impact)": []}
    prev_nwc = None
    rev = revenue0
    for y in range(years):
        if y > 0:
            rev *= (1 + growth / 100)
        cogs = rev * cogs_pct / 100
        rec = dso / 365 * rev
        inv = dio / 365 * cogs
        pay = dpo / 365 * cogs
        nwc = rec + inv - pay
        d_nwc = 0 if prev_nwc is None else -(nwc - prev_nwc)  # increase in NWC uses cash
        rows["Revenue"].append(rev)
        rows["Receivables"].append(rec)
        rows["Inventory"].append(inv)
        rows["Payables"].append(pay)
        rows["Net WC"].append(nwc)
        rows["Δ Net WC (cash impact)"].append(d_nwc)
        prev_nwc = nwc
    return rows


def tax_schedule(ebit0, growth, interest_list, tax_rate, opening_losses, years):
    """Tax schedule with loss carry-forward."""
    rows = {"EBIT": [], "− Interest": [], "Taxable profit": [], "Loss offset": [],
            "Tax charge": [], "Loss c/f": []}
    losses = opening_losses
    ebit = ebit0
    for y in range(years):
        if y > 0:
            ebit *= (1 + growth / 100)
        interest = interest_list[y] if y < len(interest_list) else 0
        taxable = ebit - interest
        if taxable > 0:
            offset = min(losses, taxable)
            taxed = taxable - offset
            losses -= offset
        else:
            offset = 0
            taxed = 0
            losses += -taxable
        tax = taxed * tax_rate / 100
        rows["EBIT"].append(ebit)
        rows["− Interest"].append(-interest)
        rows["Taxable profit"].append(taxable)
        rows["Loss offset"].append(-offset)
        rows["Tax charge"].append(tax)
        rows["Loss c/f"].append(losses)
    return rows


def to_display(rows, years):
    df = pd.DataFrame(rows, index=[f"Year {y+1}" for y in range(years)]).T
    return df.apply(lambda col: col.map(money))


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 1 · The Three-Statement Model")
st.sidebar.markdown(
    """
**Module 1.5 — Supporting Schedules**

🟡 *Intermediate*

**You will learn to build:**
- Depreciation (PP&E) schedules
- Debt & interest schedules
- Working capital schedules
- Tax schedules (with loss carry-forward)
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build live multi-year "
    "roll-forward schedules — the engine room of any model."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏛️ 1.5 · Supporting Schedules")
st.markdown(
    """
Behind every clean three-statement model sits an **engine room** of supporting schedules. These are the
detailed mini-models that calculate individual line items — **depreciation, debt & interest, working
capital, and tax** — and feed them into the main statements.

Good schedules keep the core statements simple and readable, make assumptions transparent, and are what
turn a static model into a genuinely dynamic, multi-year one. This module completes Part 1.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "1.5")
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
### What is a supporting schedule?
A **supporting schedule** is a dedicated calculation block that works out one item in detail, then
feeds a single clean number into the P&L, balance sheet, or cash flow. It keeps the main statements
uncluttered while making the underlying logic fully transparent.

Almost every schedule follows the same **roll-forward** pattern:
"""
    )
    st.latex(r"\text{Closing balance} = \text{Opening balance} + \text{Additions} - \text{Reductions}")

    st.markdown("### The four core schedules")
    sched = pd.DataFrame(
        {
            "Schedule": ["Depreciation (PP&E)", "Debt & Interest", "Working Capital", "Tax"],
            "Roll-forward logic": [
                "Opening PP&E + Capex − Depreciation = Closing PP&E",
                "Opening Debt + Draws − Repayments = Closing Debt; Interest = rate × balance",
                "Receivables + Inventory − Payables = Net WC; Δ feeds cash flow",
                "Taxable profit × rate, adjusted for loss carry-forwards",
            ],
            "Feeds into": [
                "P&L (depreciation), BS (PP&E), CF (add-back & capex)",
                "P&L (interest), BS (debt), CF (financing)",
                "BS (WC balances), CF (Δ working capital)",
                "P&L (tax), BS (tax payable), CF (tax paid)",
            ],
        }
    )
    st.table(sched)

    with st.expander("🔑 Schedule 1 — Depreciation (straight-line vs. reducing balance)"):
        st.markdown(
            """
- **Straight-line:** same charge each year = Cost ÷ Useful life. Simple and most common in models.
- **Reducing balance:** a fixed % of the *remaining* book value each year — higher early charges.

The schedule tracks opening PP&E, adds **capex**, subtracts **depreciation**, giving closing PP&E. The
depreciation figure feeds the P&L (expense) and is **added back** in the cash flow (non-cash).
"""
        )

    with st.expander("🔑 Schedule 2 — Debt & interest"):
        st.markdown(
            """
The debt schedule rolls the balance forward: **Opening + Draws − Repayments = Closing**. Interest is
then calculated on the balance:

- **On opening balance** — simplest, avoids circularity.
- **On average balance** — more accurate, but *creates circularity* (interest → net income → cash →
  debt → interest). Use iterative calculation + a switch (Module 1.4).

Interest feeds the P&L; the balance feeds the balance sheet; draws/repayments feed financing cash flow.
"""
        )

    with st.expander("🔑 Schedule 3 — Working capital"):
        st.markdown(
            """
Working capital balances are driven by **days ratios** (DSO, DIO, DPO) linked to revenue and COGS. The
schedule computes each balance, then the **change** in net working capital feeds the cash flow:

$$\\Delta \\text{Net WC} = \\text{NWC}_{\\text{this year}} - \\text{NWC}_{\\text{last year}}$$

An **increase** in net working capital **consumes** cash; a **decrease** releases it.
"""
        )

    with st.expander("🔑 Schedule 4 — Tax (and loss carry-forwards)"):
        st.markdown(
            """
The tax schedule turns accounting profit into a tax charge:
- Start from **taxable profit** (≈ EBIT − interest).
- Apply **loss carry-forwards**: if the company made losses before, those offset current taxable profit
  (so tax is often €0 until past losses are used up).
- Apply the **tax rate** to the remaining taxable profit.

Modeling this properly matters — ignoring losses overstates tax and understates value.
"""
        )

    st.success(
        "**Takeaway:** Supporting schedules are the engine room. Each follows the roll-forward pattern, "
        "keeps the main statements clean, and feeds one transparent number into each. Master these and "
        "your models become dynamic, multi-year, and audit-ready."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Examples — Building each schedule")

    st.markdown("#### Example 1 — Depreciation schedule (straight-line)")
    st.markdown(
        """
Opening PP&E €1,000,000; annual capex €200,000; useful life 10 years.

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Opening PP&E | 1,000,000 | 1,080,000 | 1,152,000 |
| + Capex | 200,000 | 200,000 | 200,000 |
| − Depreciation | (120,000) | (128,000) | (135,200) |
| **= Closing PP&E** | **1,080,000** | **1,152,000** | **1,216,800** |

*(Depreciation = (Opening + Capex) ÷ 10)*
"""
    )

    st.markdown("#### Example 2 — Debt & interest schedule")
    st.markdown(
        """
Opening debt €700,000; repayment €100,000/yr; interest 7% on opening balance.

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Opening debt | 700,000 | 600,000 | 500,000 |
| − Repayment | (100,000) | (100,000) | (100,000) |
| **= Closing debt** | **600,000** | **500,000** | **400,000** |
| Interest (7% × opening) | 49,000 | 42,000 | 35,000 |
"""
    )

    st.markdown("#### Example 3 — Working capital schedule")
    st.markdown(
        """
Revenue €2,000,000 growing 5%; COGS 60%; DSO 45, DIO 60, DPO 30.

| | Year 1 | Year 2 |
|---|---|---|
| Receivables | 246,575 | 258,904 |
| Inventory | 197,260 | 207,123 |
| Payables | (98,630) | (103,562) |
| **Net WC** | **345,205** | **362,465** |
| Δ Net WC (uses cash) | — | (17,260) |
"""
    )

    st.markdown("#### Example 4 — Tax schedule with loss carry-forward")
    st.markdown(
        """
Taxable profit €330,000; tax rate 30%; but €200,000 of losses carried forward.

| Line | € |
|---|---|
| Taxable profit | 330,000 |
| − Loss offset | (200,000) |
| = Taxed profit | 130,000 |
| **Tax charge (30%)** | **39,000** |
| Losses remaining | 0 |

**Insight:** Without modeling the loss, tax would appear as €99,000 — the carry-forward saves €60,000.
"""
    )

    st.info(
        "👉 Now open the **Interactive Exercises** tab and build all four schedules yourself across "
        "multiple years — change any driver and watch them roll forward."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Schedules")
    st.markdown("Pick a schedule, set the drivers, and watch it roll forward year by year.")

    years = st.slider("Number of years to project", 3, 10, 5, 1)
    which = st.radio(
        "Choose a schedule to build:",
        ["🏭 Depreciation (PP&E)", "🏦 Debt & Interest", "💧 Working Capital", "🧾 Tax (with losses)"],
        horizontal=True,
    )
    st.markdown("---")

    # -------- Depreciation --------
    if which == "🏭 Depreciation (PP&E)":
        left, right = st.columns([0.32, 0.68])
        with left:
            open_ppe = st.number_input("Opening PP&E (€)", 0, 50_000_000, 1_000_000, 50_000)
            capex_yr = st.number_input("Capex per year (€)", 0, 10_000_000, 200_000, 25_000)
            life = st.slider("Useful life (years)", 2, 30, 10, 1)
        with right:
            rows = depreciation_schedule(open_ppe, capex_yr, life, years)
            st.markdown("##### 📄 Depreciation / PP&E Roll-Forward")
            st.dataframe(to_display(rows, years), use_container_width=True)
            chart = pd.DataFrame({"Closing PP&E": rows["= Closing PP&E"]},
                                 index=[f"Y{y+1}" for y in range(years)])
            st.line_chart(chart)
            st.caption(f"Year 1 depreciation: **{money(-rows['− Depreciation'][0])}** — feeds the P&L and is added back in cash flow.")

    # -------- Debt --------
    elif which == "🏦 Debt & Interest":
        left, right = st.columns([0.32, 0.68])
        with left:
            open_debt = st.number_input("Opening debt (€)", 0, 50_000_000, 700_000, 50_000)
            repay = st.number_input("Repayment per year (€)", 0, 10_000_000, 100_000, 25_000)
            rate = st.slider("Interest rate (%)", 0.0, 20.0, 7.0, 0.5)
        with right:
            rows = debt_schedule(open_debt, repay, rate, years)
            st.markdown("##### 📄 Debt & Interest Schedule")
            st.dataframe(to_display(rows, years), use_container_width=True)
            chart = pd.DataFrame({"Closing Debt": rows["= Closing Debt"],
                                  "Interest expense": rows["Interest expense"]},
                                 index=[f"Y{y+1}" for y in range(years)])
            st.line_chart(chart)
            total_int = sum(rows["Interest expense"])
            st.caption(f"Total interest over {years} years: **{money(total_int)}** — feeds the P&L each year.")

    # -------- Working capital --------
    elif which == "💧 Working Capital":
        left, right = st.columns([0.32, 0.68])
        with left:
            rev0 = st.number_input("Year 1 revenue (€)", 100_000, 50_000_000, 2_000_000, 50_000)
            growth = st.slider("Revenue growth (%)", -10.0, 25.0, 5.0, 0.5)
            cogs_pct = st.slider("COGS (% of revenue)", 30.0, 85.0, 60.0, 0.5)
            dso = st.slider("DSO (days)", 0, 120, 45, 1)
            dio = st.slider("DIO (days)", 0, 180, 60, 1)
            dpo = st.slider("DPO (days)", 0, 120, 30, 1)
        with right:
            rows = working_capital_schedule(rev0, growth, cogs_pct, dso, dio, dpo, years)
            st.markdown("##### 📄 Working Capital Schedule")
            st.dataframe(to_display(rows, years), use_container_width=True)
            chart = pd.DataFrame({"Net WC": rows["Net WC"]},
                                 index=[f"Y{y+1}" for y in range(years)])
            st.line_chart(chart)
            total_cash = sum(rows["Δ Net WC (cash impact)"])
            st.caption(
                f"Cumulative cash impact of working-capital change: **{money(total_cash)}** "
                "(negative = cash consumed by growth)."
            )

    # -------- Tax --------
    else:
        left, right = st.columns([0.32, 0.68])
        with left:
            ebit0 = st.number_input("Year 1 EBIT (€)", -1_000_000, 10_000_000, 380_000, 10_000)
            growth = st.slider("EBIT growth (%)", -10.0, 25.0, 5.0, 0.5)
            interest_flat = st.number_input("Interest per year (€)", 0, 5_000_000, 50_000, 5_000)
            tax_rate = st.slider("Tax rate (%)", 0.0, 45.0, 30.0, 1.0)
            losses = st.number_input("Opening losses carried forward (€)", 0, 10_000_000, 200_000, 25_000)
        with right:
            rows = tax_schedule(ebit0, growth, [interest_flat] * years, tax_rate, losses, years)
            st.markdown("##### 📄 Tax Schedule (with loss carry-forward)")
            st.dataframe(to_display(rows, years), use_container_width=True)
            chart = pd.DataFrame({"Tax charge": rows["Tax charge"], "Loss c/f": rows["Loss c/f"]},
                                 index=[f"Y{y+1}" for y in range(years)])
            st.line_chart(chart)
            st.caption(
                f"Year 1 tax: **{money(rows['Tax charge'][0])}**. Notice how losses reduce tax to zero "
                "until they're used up."
            )

    st.markdown("---")
    st.info(
        "🧠 **Each schedule feeds the main model:** depreciation & interest → P&L; PP&E, debt & WC "
        "balances → balance sheet; depreciation add-back, Δ working capital, capex & repayments → cash flow. "
        "This is exactly how the integrated model in 1.4 gets its numbers."
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The €6m Capex depreciation schedule", expanded=True):
        st.markdown(
            """
**Situation:** A factory invests €6m in automation with a 10-year life. The board needs to see the P&L
impact over time.

**How the schedule helps:** A depreciation schedule spreads the €6m as ~€600k/year of non-cash expense,
feeding the P&L (lower EBIT) while being added back in cash flow. It also rolls PP&E forward on the
balance sheet.

**Why it matters:** Without the schedule, you can't show the multi-year earnings drag *or* prove the
cash impact is far smaller than the accounting charge.

**Lesson:** Big Capex decisions need a depreciation schedule to separate the *accounting* hit from the
*cash* reality.
"""
        )

    with st.expander("Case B — Loss carry-forwards that unlocked value"):
        st.markdown(
            """
**Situation:** A turnaround business had €2m of accumulated tax losses. A naïve model applied full tax
from Year 1, making the recovery look unattractive.

**How the schedule helps:** A proper **tax schedule with loss carry-forwards** showed the company would
pay **little or no tax** for the first few profitable years — materially improving forecast cash flows
and the valuation.

**Why it matters:** Tax is often a company's largest single cash outflow; modeling losses correctly can
swing an investment decision.

**Lesson:** Never apply a flat tax rate blindly — model the tax schedule, including losses.
"""
        )

    with st.expander("Case C — The debt schedule that reassured lenders"):
        st.markdown(
            """
**Situation:** A company sought financing for expansion and lenders wanted to see debt serviceability.

**How the schedule helps:** A debt & interest schedule showed opening/closing balances, scheduled
repayments, and interest each year — and (combined with the P&L) an **interest-cover ratio** that stayed
comfortably above covenant thresholds.

**Why it matters:** Lenders lend against a credible repayment and interest schedule, not a single number.

**Lesson:** A transparent debt schedule turns a financing conversation from hopeful to bankable.
"""
        )

    st.info(
        "🔗 **Pattern:** Schedules are where the *detail* lives. They keep the headline statements clean "
        "while giving decision-makers (and lenders, boards, auditors) the depth they need to trust the model."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_15"):
        q1 = st.radio(
            "**1.** Almost every supporting schedule follows which pattern?",
            [
                "Revenue − Costs = Profit",
                "Opening balance + Additions − Reductions = Closing balance",
                "Assets = Liabilities + Equity",
                "Price × Volume",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** In a depreciation schedule, the closing PP&E equals:",
            [
                "Opening PP&E + Depreciation − Capex",
                "Opening PP&E + Capex − Depreciation",
                "Opening PP&E × (1 + growth)",
                "Capex ÷ useful life",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Calculating interest on the AVERAGE debt balance can cause:",
            [
                "The balance sheet to grow faster",
                "Circularity (interest → net income → cash → debt → interest)",
                "Depreciation to increase",
                "Working capital to fall",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** In a working capital schedule, an INCREASE in net working capital:",
            [
                "Releases cash (a source of cash)",
                "Consumes cash (a use of cash)",
                "Has no effect on cash",
                "Increases net income",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Why model loss carry-forwards in a tax schedule?",
            [
                "They increase the tax charge",
                "Past losses offset current taxable profit, so tax can be zero until losses are used up",
                "They are required for depreciation",
                "They change the interest rate",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Opening balance + Additions − Reductions = Closing balance"),
            "2": (q2, "Opening PP&E + Capex − Depreciation"),
            "3": (q3, "Circularity (interest → net income → cash → debt → interest)"),
            "4": (q4, "Consumes cash (a use of cash)"),
            "5": (q5, "Past losses offset current taxable profit, so tax can be zero until losses are used up"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've completed Part 1! You can now build a full three-statement model with schedules. 🎉")
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
    f"Applied Financial Models · Module 1.5 Supporting Schedules · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
