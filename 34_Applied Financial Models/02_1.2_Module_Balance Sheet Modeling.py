"""
================================================================================
APPLIED FINANCIAL MODELS
Module 1.2 — BALANCE SHEET MODELING
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to model a balance sheet: working capital, fixed assets, debt & equity
schedules, and the all-important balance check (Assets = Liabilities + Equity).

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live balance-sheet builder + balance check)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_1_2_Balance_Sheet_Modeling.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="1.2 Balance Sheet Modeling — Applied Financial Models",
    layout="wide",
    page_icon="🏛️",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    return f"{symbol}{x:,.{dp}f}"


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 1 · The Three-Statement Model")
st.sidebar.markdown(
    """
**Module 1.2 — Balance Sheet Modeling**

🟡 *Intermediate*

**You will learn to:**
- Structure assets, liabilities & equity
- Model working capital (receivables, inventory, payables)
- Build fixed asset & debt/equity schedules
- Make the balance sheet actually **balance**
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live balance sheet "
    "and watch the balance check turn green (or red!)."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏛️ 1.2 · Balance Sheet Modeling")
st.markdown(
    """
If the income statement shows *performance over a period*, the **balance sheet** is a *snapshot at a
point in time* — what the company **owns** (assets), what it **owes** (liabilities), and what belongs
to **shareholders** (equity).

The defining feature of balance-sheet modeling is the **fundamental accounting equation**, which must
*always* hold:
"""
)

st.latex(r"\textbf{Assets} = \textbf{Liabilities} + \textbf{Equity}")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "1.2")
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
### The structure of a balance sheet
A balance sheet has two sides that must always be equal. It's organised from most to least liquid.
"""
    )

    structure = pd.DataFrame(
        {
            "ASSETS (what you own)": [
                "Cash & equivalents",
                "Accounts receivable",
                "Inventory",
                "— (current assets subtotal) —",
                "Property, plant & equipment (PP&E)",
                "Intangibles / goodwill",
                "= TOTAL ASSETS",
            ],
            "LIABILITIES & EQUITY (how it's financed)": [
                "Accounts payable",
                "Short-term debt",
                "— (current liabilities subtotal) —",
                "Long-term debt",
                "Share capital",
                "Retained earnings",
                "= TOTAL LIABILITIES + EQUITY",
            ],
        }
    )
    st.table(structure)

    st.markdown(
        """
### The three engines of a balance sheet model
Most balance-sheet lines are driven by **schedules** — supporting mini-models that feed the balance sheet:
"""
    )

    engines = pd.DataFrame(
        {
            "Schedule": ["Working Capital", "Fixed Assets (PP&E)", "Debt & Equity"],
            "Drives these lines": [
                "Receivables, inventory, payables",
                "PP&E, depreciation, capex",
                "Debt balances, interest, share capital, retained earnings",
            ],
            "Key driver / logic": [
                "Days ratios (DSO, DIO, DPO) linked to revenue/COGS",
                "Opening PP&E + capex − depreciation = closing PP&E",
                "Opening debt + draw − repay; RE + net income − dividends",
            ],
        }
    )
    st.table(engines)

    with st.expander("🔑 Concept 1 — Working capital (the operational squeeze)"):
        st.markdown(
            """
Working capital ties up cash in day-to-day operations. Model it with **days ratios**:

- **DSO** (Days Sales Outstanding) → Receivables = DSO ÷ 365 × Revenue
- **DIO** (Days Inventory Outstanding) → Inventory = DIO ÷ 365 × COGS
- **DPO** (Days Payables Outstanding) → Payables = DPO ÷ 365 × COGS

$$\\text{Net Working Capital} = \\text{Receivables} + \\text{Inventory} - \\text{Payables}$$

Rising working capital *consumes* cash even when profits look healthy — a classic trap.
"""
        )

    with st.expander("🔑 Concept 2 — The fixed asset (PP&E) roll-forward"):
        st.markdown(
            """
PP&E is modelled as a **roll-forward** from one period to the next:

$$\\text{Closing PP\\&E} = \\text{Opening PP\\&E} + \\text{Capex} - \\text{Depreciation}$$

- **Capex** adds new assets (a cash outflow).
- **Depreciation** reduces book value (a non-cash charge that links to the income statement).

This same roll-forward pattern (opening → movements → closing) applies to debt, equity, and provisions.
"""
        )

    with st.expander("🔑 Concept 3 — Debt & equity schedules"):
        st.markdown(
            """
- **Debt:** Closing = Opening + new draw − repayments. Interest links to the income statement.
- **Retained earnings:** Closing = Opening + Net Income − Dividends. This is the crucial link that
  connects the **income statement to the balance sheet**.

These schedules are what make the three statements *integrate* (covered fully in Module 1.4).
"""
        )

    with st.expander("🔑 Concept 4 — Why it must balance (and the 'plug')"):
        st.markdown(
            """
If Assets ≠ Liabilities + Equity, the model has an error. In an integrated model, **cash** is usually
the balancing figure (the "plug") — it flows in from the cash flow statement. If the balance check
fails, something upstream is wrong. A visible **balance check** (should equal zero) is non-negotiable.
"""
        )

    st.success(
        "**Takeaway:** A balance sheet model is a set of roll-forward schedules (working capital, PP&E, "
        "debt, equity) that must always satisfy Assets = Liabilities + Equity. The balance check is your safety net."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Building a balance sheet step by step")
    st.markdown("Let's construct a simple balance sheet for our fictional company **'CleanSoap'**.")

    st.markdown("#### Step 1 — Model working capital from days ratios")
    st.markdown(
        """
Assume **Revenue = €2,000,000**, **COGS = €1,200,000**.

| Item | Days | Calculation | Result |
|---|---|---|---|
| Receivables | DSO 45 | 45 ÷ 365 × 2,000,000 | **€246,575** |
| Inventory | DIO 60 | 60 ÷ 365 × 1,200,000 | **€197,260** |
| Payables | DPO 30 | 30 ÷ 365 × 1,200,000 | **€98,630** |

**Net working capital** = 246,575 + 197,260 − 98,630 = **€345,205**
"""
    )

    st.markdown("#### Step 2 — Roll forward fixed assets")
    st.markdown(
        """
| Item | Value |
|---|---|
| Opening PP&E | €1,000,000 |
| + Capex | €200,000 |
| − Depreciation | (€120,000) |
| **= Closing PP&E** | **€1,080,000** |
"""
    )

    st.markdown("#### Step 3 — Assemble the balance sheet")
    st.markdown(
        """
| ASSETS | € | | LIABILITIES & EQUITY | € |
|---|---|---|---|---|
| Cash | 150,000 | | Accounts payable | 98,630 |
| Accounts receivable | 246,575 | | Short-term debt | 100,000 |
| Inventory | 197,260 | | Long-term debt | 600,000 |
| PP&E | 1,080,000 | | Share capital | 500,000 |
| | | | Retained earnings | 375,205 |
| **TOTAL ASSETS** | **1,673,835** | | **TOTAL L + E** | **1,673,835** |
"""
    )

    st.markdown("#### Step 4 — Run the balance check")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Assets", "€1,673,835")
    col2.metric("Total Liab + Equity", "€1,673,835")
    col3.metric("Balance Check", "€0 ✅", help="Assets − (Liabilities + Equity) = 0")

    st.info(
        "**Insight:** With €345k tied up in net working capital, tightening DSO from 45 → 35 days would "
        "release ~€55k of cash — money currently locked in customer credit. **Recommendation:** review "
        "credit terms before seeking external financing."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Build a Balance Sheet & Make It Balance")
    st.markdown(
        "Change the drivers on the left. The balance sheet rebuilds live, and the **balance check** tells "
        "you instantly whether Assets = Liabilities + Equity. Cash acts as the balancing plug."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        st.markdown("##### 🎚️ Operating drivers")
        revenue = st.number_input("Revenue (€)", 100_000, 20_000_000, 2_000_000, 50_000)
        cogs = st.number_input("COGS (€)", 50_000, 15_000_000, 1_200_000, 50_000)
        dso = st.slider("DSO — receivable days", 0, 120, 45, 1)
        dio = st.slider("DIO — inventory days", 0, 180, 60, 1)
        dpo = st.slider("DPO — payable days", 0, 120, 30, 1)

        st.markdown("##### 🏭 Fixed assets")
        open_ppe = st.number_input("Opening PP&E (€)", 0, 20_000_000, 1_000_000, 50_000)
        capex = st.number_input("Capex (€)", 0, 5_000_000, 200_000, 25_000)
        dep = st.number_input("Depreciation (€)", 0, 5_000_000, 120_000, 10_000)

        st.markdown("##### 🏦 Financing")
        st_debt = st.number_input("Short-term debt (€)", 0, 10_000_000, 100_000, 25_000)
        lt_debt = st.number_input("Long-term debt (€)", 0, 20_000_000, 600_000, 50_000)
        share_cap = st.number_input("Share capital (€)", 0, 20_000_000, 500_000, 50_000)
        retained = st.number_input("Retained earnings (€)", -5_000_000, 20_000_000, 375_205, 25_000)

    with right:
        # Working capital
        receivables = dso / 365 * revenue
        inventory = dio / 365 * cogs
        payables = dpo / 365 * cogs
        nwc = receivables + inventory - payables

        # Fixed assets
        close_ppe = open_ppe + capex - dep

        # Liabilities + equity (excluding the balancing cash)
        total_liab_equity = st_debt + lt_debt + share_cap + retained + payables

        # Non-cash assets
        non_cash_assets = receivables + inventory + close_ppe

        # Cash is the plug so the sheet balances
        cash = total_liab_equity - non_cash_assets
        total_assets = cash + non_cash_assets

        balance_check = total_assets - total_liab_equity

        k1, k2, k3 = st.columns(3)
        k1.metric("Total Assets", money(total_assets))
        k2.metric("Total Liab + Equity", money(total_liab_equity))
        k3.metric("Balance Check", money(balance_check),
                  "✅ Balanced" if abs(balance_check) < 1 else "❌ Off",
                  delta_color="normal" if abs(balance_check) < 1 else "inverse")

        if cash < 0:
            st.error(
                f"⚠️ **Cash is negative ({money(cash)}).** The business can't fund its assets from current "
                "financing — it needs more debt/equity or must release working capital. (The sheet still "
                "balances mathematically, but negative cash signals a funding gap.)"
            )
        else:
            st.success(f"✅ Balanced with **{money(cash)}** of cash as the plug.")

        bs = pd.DataFrame(
            {
                "ASSETS": ["Cash", "Accounts receivable", "Inventory", "PP&E (closing)", "TOTAL ASSETS"],
                "€ (A)": [cash, receivables, inventory, close_ppe, total_assets],
                "LIABILITIES & EQUITY": ["Accounts payable", "Short-term debt", "Long-term debt",
                                          "Share capital + Retained earnings", "TOTAL LIAB + EQUITY"],
                "€ (L+E)": [payables, st_debt, lt_debt, share_cap + retained, total_liab_equity],
            }
        )
        for c in ["€ (A)", "€ (L+E)"]:
            bs[c] = bs[c].map(lambda v: f"€{v:,.0f}")
        st.markdown("##### 📄 Balance Sheet")
        st.dataframe(bs, use_container_width=True, hide_index=True)

        st.markdown("##### 💧 Net Working Capital")
        w1, w2, w3, w4 = st.columns(4)
        w1.metric("Receivables", money(receivables))
        w2.metric("Inventory", money(inventory))
        w3.metric("Payables", money(payables))
        w4.metric("Net WC", money(nwc))

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Cash squeeze:** Raise DSO from 45 → 90 days. Watch receivables balloon and cash shrink.
2. **Release cash:** Cut DIO from 60 → 30 days. How much cash is freed from inventory?
"""
        )
    with e2:
        st.markdown(
            """
3. **Funding gap:** Lower long-term debt to €0. Does cash go negative (a funding gap)?
4. **Capex impact:** Push capex to €1,000,000. See PP&E rise but cash fall by the same amount.
"""
        )

    st.download_button(
        "⬇️ Download this balance sheet (CSV)",
        bs.to_csv(index=False).encode("utf-8"),
        "balance_sheet.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Profitable but out of cash (the working-capital trap)", expanded=True):
        st.markdown(
            """
**Situation:** A fast-growing manufacturer reported record profits, yet kept running short of cash.

**What the balance sheet revealed:** As sales grew, **receivables and inventory ballooned** (long DSO
and DIO), tying up cash faster than profit generated it. Growth was *consuming* cash.

**The fix:** Tighten credit terms (lower DSO) and improve inventory turns (lower DIO) to release cash
locked in working capital — often faster and cheaper than raising external finance.

**Lesson:** Profit ≠ cash. The balance sheet (via working capital) explains where the cash actually went.
"""
        )

    with st.expander("Case B — Funding a €6m Capex (asset & financing schedules)"):
        st.markdown(
            """
**Situation:** A factory plans a €6m automation investment and needs to show how it will be financed.

**How the balance sheet models it:** The **PP&E roll-forward** adds €6m capex; the **debt schedule**
shows new borrowing to fund it; **depreciation** then reduces PP&E and links to the P&L over the asset's life.

**Why it matters:** The balance sheet proves the investment is **fundable** and shows the resulting
leverage (debt-to-equity) — critical for lender and board approval.

**Lesson:** Big Capex decisions live or die on the balance sheet's asset and financing schedules.
"""
        )

    with st.expander("Case C — The balance sheet that wouldn't balance (debugging)"):
        st.markdown(
            """
**Situation:** An analyst's model showed Assets €50k higher than Liabilities + Equity.

**How the balance check helped:** The visible **check row** (Assets − L − E) flagged the €50k gap
immediately. Tracing it back revealed depreciation was deducted from PP&E but never linked to retained
earnings via the P&L — a broken integration.

**The fix:** Re-link net income (after depreciation) to retained earnings so both sides move together.

**Lesson:** A balance check doesn't just confirm correctness — it's your fastest debugging tool.
"""
        )

    st.info(
        "🔗 **Pattern:** The balance sheet is where *profitability meets funding*. Working capital explains "
        "cash, asset schedules explain investment, and the balance check keeps you honest."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_12"):
        q1 = st.radio(
            "**1.** The fundamental accounting equation is:",
            [
                "Assets = Revenue − Costs",
                "Assets = Liabilities + Equity",
                "Equity = Assets + Liabilities",
                "Cash = Profit",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** Receivables are typically modelled using:",
            [
                "DPO (Days Payables Outstanding) × Revenue",
                "DSO (Days Sales Outstanding) ÷ 365 × Revenue",
                "Depreciation ÷ Capex",
                "Debt ÷ Equity",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The PP&E roll-forward is:",
            [
                "Opening PP&E + Depreciation − Capex",
                "Opening PP&E + Capex − Depreciation",
                "Opening PP&E × (1 + growth)",
                "Revenue − COGS",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Which line links the income statement to the balance sheet?",
            [
                "Accounts payable",
                "Retained earnings (Opening + Net Income − Dividends)",
                "Inventory",
                "Short-term debt",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** A company is highly profitable but keeps running out of cash. The most likely balance-sheet cause is:",
            [
                "Too much share capital",
                "Rising working capital (receivables & inventory) consuming cash",
                "Depreciation being too high",
                "Having no long-term debt",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Assets = Liabilities + Equity"),
            "2": (q2, "DSO (Days Sales Outstanding) ÷ 365 × Revenue"),
            "3": (q3, "Opening PP&E + Capex − Depreciation"),
            "4": (q4, "Retained earnings (Opening + Net Income − Dividends)"),
            "5": (q5, "Rising working capital (receivables & inventory) consuming cash"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered balance sheet modeling! On to Module 1.3 (Cash Flow). 🎉")
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
    f"Applied Financial Models · Module 1.2 Balance Sheet Modeling · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
