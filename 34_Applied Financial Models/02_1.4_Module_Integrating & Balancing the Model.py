"""
================================================================================
APPLIED FINANCIAL MODELS
Module 1.4 — INTEGRATING & BALANCING THE MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to LINK the income statement, balance sheet and cash flow statement into one
integrated three-statement model — including the "plug", circularity, balance
checks and iterative calculation.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a fully integrated 3-statement model, live)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_1_4_Integrating_and_Balancing_the_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="1.4 Integrating & Balancing the Model — Applied Financial Models",
    layout="wide",
    page_icon="🏛️",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def build_integrated_model(
    revenue, cogs_pct, sga, dep, interest_rate, tax_rate,
    dso, dio, dpo, capex, open_ppe,
    open_cash, open_receivables, open_inventory, open_payables,
    open_debt, share_capital, open_retained, dividend_payout_pct,
):
    """
    Build a single-period integrated 3-statement model.
    Returns dicts for income statement, cash flow, and balance sheet + checks.
    """
    # ---------------- INCOME STATEMENT ----------------
    cogs = revenue * cogs_pct / 100
    gross = revenue - cogs
    ebitda = gross - sga
    ebit = ebitda - dep
    interest = open_debt * interest_rate / 100
    pbt = ebit - interest
    tax = max(pbt, 0) * tax_rate / 100
    net_income = pbt - tax

    # ---------------- BALANCE SHEET DRIVERS ----------------
    receivables = dso / 365 * revenue
    inventory = dio / 365 * cogs
    payables = dpo / 365 * cogs
    close_ppe = open_ppe + capex - dep

    # working capital changes (affect cash)
    d_receivables = receivables - open_receivables
    d_inventory = inventory - open_inventory
    d_payables = payables - open_payables

    # dividends & retained earnings
    dividends = max(net_income, 0) * dividend_payout_pct / 100
    close_retained = open_retained + net_income - dividends

    # ---------------- CASH FLOW STATEMENT ----------------
    cfo = net_income + dep - d_receivables - d_inventory + d_payables
    cfi = -capex
    cff = -dividends  # (no new debt/equity in this simple version)
    net_change_cash = cfo + cfi + cff
    close_cash = open_cash + net_change_cash

    # ---------------- BALANCE SHEET ----------------
    total_assets = close_cash + receivables + inventory + close_ppe
    total_liab_equity = payables + open_debt + share_capital + close_retained
    balance_check = total_assets - total_liab_equity

    income = {
        "Revenue": revenue, "COGS": -cogs, "Gross Profit": gross,
        "SG&A": -sga, "EBITDA": ebitda, "Depreciation": -dep, "EBIT": ebit,
        "Interest": -interest, "Profit Before Tax": pbt, "Tax": -tax, "Net Income": net_income,
    }
    cashflow = {
        "Net Income": net_income, "+ Depreciation": dep,
        "− Δ Receivables": -d_receivables, "− Δ Inventory": -d_inventory, "+ Δ Payables": d_payables,
        "= CFO": cfo, "− Capex (CFI)": -capex, "− Dividends (CFF)": -dividends,
        "Net Change in Cash": net_change_cash, "Opening Cash": open_cash, "= Closing Cash": close_cash,
    }
    balance = {
        "Cash": close_cash, "Receivables": receivables, "Inventory": inventory, "PP&E": close_ppe,
        "TOTAL ASSETS": total_assets,
        "Payables": payables, "Debt": open_debt, "Share Capital": share_capital,
        "Retained Earnings": close_retained, "TOTAL LIAB + EQUITY": total_liab_equity,
        "BALANCE CHECK": balance_check,
    }
    return income, cashflow, balance, balance_check


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 1 · The Three-Statement Model")
st.sidebar.markdown(
    """
**Module 1.4 — Integrating & Balancing the Model**

🟡 *Intermediate*

**You will learn to:**
- Link the P&L, balance sheet & cash flow
- Understand the cash "plug"
- Handle circularity & iterative calculation
- Use the balance check to prove it ties out
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for a fully **integrated** "
    "3-statement model — change one driver and watch all three statements move."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏛️ 1.4 · Integrating & Balancing the Model")
st.markdown(
    """
This is where Part 1 comes together. Individually, the income statement (1.1), balance sheet (1.2) and
cash flow statement (1.3) each tell part of the story. **Integrated**, they become a single, living
model where changing *one* assumption flows correctly through *all three* statements — and the balance
sheet still balances.

The magic linkage: **net income** flows to retained earnings *and* into cash flow; **cash flow**
calculates the closing cash that lands back on the balance sheet — which then balances automatically.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "1.4")
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
### The linkages that integrate the three statements
An integrated model is defined by its **links**. Get these right and the model self-balances.
"""
    )

    links = pd.DataFrame(
        {
            "Link": [
                "Net income → Retained earnings",
                "Net income → Cash flow (CFO)",
                "Depreciation → PP&E & CFO",
                "Working capital → CFO",
                "Capex → PP&E & CFI",
                "Closing cash → Balance sheet",
            ],
            "From statement": [
                "Income statement", "Income statement", "Income statement",
                "Balance sheet", "Cash flow / capex plan", "Cash flow statement",
            ],
            "To statement": [
                "Balance sheet (equity)", "Cash flow (top line)", "Balance sheet & cash flow",
                "Cash flow statement", "Balance sheet & cash flow", "Balance sheet (assets)",
            ],
        }
    )
    st.table(links)

    st.markdown(
        """
### The flow of an integrated model
"""
    )
    st.markdown(
        """
```
   INCOME STATEMENT           CASH FLOW STATEMENT            BALANCE SHEET
   ────────────────           ───────────────────           ─────────────
   Revenue                    Net income  ◄─────────────┐    Cash  ◄──────────┐
   − Costs                    + Depreciation             │    Receivables      │
   = Net income ──────────►   ± Working capital          │    Inventory        │
        │                     = CFO                      │    PP&E             │
        │                     − Capex (CFI)              │    ─────────        │
        │                     − Dividends (CFF)          │    Payables         │
        │                     = Net change in cash       │    Debt             │
        │                     + Opening cash             │    Share capital    │
        │                     = Closing cash ────────────┘    Retained earnings│
        └──────────────────────────────────────────────────► (via retained) ──┘
                                                              TOTAL must balance
```
"""
    )

    with st.expander("🔑 Concept 1 — The 'plug' (what makes it balance)"):
        st.markdown(
            """
In an integrated model, **one line is the balancing figure** — usually **cash** (or a revolving credit
facility). You don't hard-code closing cash; you *calculate* it from the cash flow statement, and it
lands on the balance sheet. Because every movement is captured, **Assets automatically equal Liabilities
+ Equity**. If they don't, a link is broken.
"""
        )

    with st.expander("🔑 Concept 2 — Circularity (and why it happens)"):
        st.markdown(
            """
Circularity arises when a calculation depends on itself in a loop. The classic case:

> Interest depends on debt → debt depends on cash → cash depends on net income → net income depends on
> interest. 🔁

Excel resolves this with **iterative calculation** (it loops until the numbers settle). It's powerful
but fragile — a single error can cause the model to spiral. Many modelers use a **circularity switch**
to turn it off and debug.
"""
        )

    with st.expander("🔑 Concept 3 — The balance check (your proof of integrity)"):
        st.markdown(
            """
The single most important cell in an integrated model:

$$\\text{Balance Check} = \\text{Total Assets} - (\\text{Total Liabilities} + \\text{Equity}) = 0$$

If it's ever non-zero, **stop** — a link is broken. Wire it to conditional formatting so it turns red
instantly. A model that doesn't balance cannot be trusted for a single decision.
"""
        )

    with st.expander("🔑 Concept 4 — Common reasons a model won't balance"):
        st.markdown(
            """
- Net income not flowing to **retained earnings**.
- Depreciation deducted from PP&E but not added back in **CFO**.
- A working-capital change hitting the balance sheet but **not the cash flow** (or vice-versa).
- Capex reducing cash but not increasing **PP&E** (or double-counted).
- Dividends reducing cash but not **retained earnings**.

**Debug tip:** check each link in isolation — the balance error usually equals a specific missing item.
"""
        )

    st.success(
        "**Takeaway:** Integration is all about *links*. Net income and cash are the connective tissue; "
        "the balance check is the proof. When it reads zero, every statement is telling a consistent story."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Watching one change flow through all three statements")
    st.markdown(
        "The power of integration is seeing a *single* change ripple correctly everywhere. Let's trace "
        "**+€120,000 of depreciation**."
    )

    st.markdown("#### The ripple effect of depreciation")
    st.markdown(
        """
| Statement | What happens | Effect |
|---|---|---|
| **Income statement** | Depreciation is an expense | EBIT ↓ by €120k → Net income ↓ (by €84k after 30% tax) |
| **Cash flow** | Depreciation is non-cash → **added back** in CFO | CFO only ↓ by the €36k tax effect, *not* the full €120k |
| **Balance sheet (assets)** | PP&E ↓ by €120k; cash ↑ vs. if it were a cash cost | Assets net position adjusts |
| **Balance sheet (equity)** | Lower net income → retained earnings ↓ by €84k | Equity ↓ |
| **Balance check** | Both sides move consistently | **Still €0 ✅** |
"""
    )

    st.info(
        "**Key insight:** Depreciation *reduces profit* but *protects cash* (it's added back, and it "
        "reduces tax). In a non-integrated model you'd miss this — in an integrated model it flows "
        "automatically and the balance check confirms nothing is lost."
    )

    st.markdown("#### The order you build an integrated model")
    st.markdown(
        """
1. **Income statement** — down to net income.
2. **Supporting schedules** — working capital, PP&E, debt (Module 1.5).
3. **Cash flow statement** — pull net income + non-cash + working-capital + capex + financing.
4. **Balance sheet** — pull closing cash, WC balances, PP&E, retained earnings.
5. **Balance check** — confirm Assets = Liabilities + Equity = 0 difference.
6. **Only then** add circularity (e.g. interest on average debt) with a switch.
"""
    )

    st.markdown("#### A fully balanced single period (CleanSoap)")
    st.markdown(
        """
| Income Statement | € | | Cash Flow | € | | Balance Sheet | € |
|---|---|---|---|---|---|---|---|
| Revenue | 2,000,000 | | Net income | 231,000 | | Cash | 295,795 |
| Net income | 231,000 | | + Depreciation | 120,000 | | Receivables | 246,575 |
| | | | ± Working capital | (55,205) | | Inventory | 197,260 |
| | | | = CFO | 295,795 | | PP&E | 1,080,000 |
| | | | − Capex | (200,000) | | **Assets** | **1,819,630** |
| | | | − Dividends | (50,000) | | Payables | 98,630 |
| | | | Net change | 45,795 | | Debt | 700,000 |
| | | | Closing cash | 295,795 | | Equity | 1,021,000 |
| | | | | | | **L + E** | **1,819,630** |

**Balance check = 1,819,630 − 1,819,630 = €0 ✅**
"""
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — A Fully Integrated 3-Statement Model")
    st.markdown(
        "This is the real thing: change **any** driver and watch it flow through the **income statement, "
        "cash flow statement and balance sheet** simultaneously — with a live **balance check** proving "
        "the model always ties out."
    )

    left, right = st.columns([0.30, 0.70])

    with left:
        st.markdown("##### 🧾 P&L drivers")
        revenue = st.number_input("Revenue (€)", 100_000, 20_000_000, 2_000_000, 50_000)
        cogs_pct = st.slider("COGS (% of revenue)", 30.0, 85.0, 60.0, 0.5)
        sga = st.number_input("SG&A (€)", 0, 5_000_000, 300_000, 25_000)
        dep = st.number_input("Depreciation (€)", 0, 5_000_000, 120_000, 10_000)
        interest_rate = st.slider("Interest rate on debt (%)", 0.0, 20.0, 7.14, 0.5)
        tax_rate = st.slider("Tax rate (%)", 0.0, 45.0, 30.0, 1.0)

        st.markdown("##### 💧 Working capital (days)")
        dso = st.slider("DSO (receivable days)", 0, 120, 45, 1)
        dio = st.slider("DIO (inventory days)", 0, 180, 60, 1)
        dpo = st.slider("DPO (payable days)", 0, 120, 30, 1)

        st.markdown("##### 🏭 Investing & payout")
        capex = st.number_input("Capex (€)", 0, 5_000_000, 200_000, 25_000)
        payout = st.slider("Dividend payout (% of net income)", 0, 100, 22, 1)

        with st.expander("🏁 Opening balances (advanced)"):
            open_cash = st.number_input("Opening cash", -1_000_000, 10_000_000, 150_000, 10_000)
            open_ppe = st.number_input("Opening PP&E", 0, 20_000_000, 1_000_000, 50_000)
            open_receivables = st.number_input("Opening receivables", 0, 5_000_000, 200_000, 10_000)
            open_inventory = st.number_input("Opening inventory", 0, 5_000_000, 170_000, 10_000)
            open_payables = st.number_input("Opening payables", 0, 5_000_000, 80_000, 10_000)
            open_debt = st.number_input("Debt", 0, 20_000_000, 700_000, 50_000)
            share_capital = st.number_input("Share capital", 0, 20_000_000, 500_000, 50_000)
            open_retained = st.number_input("Opening retained earnings", -5_000_000, 20_000_000, 240_000, 10_000)
            st.caption("⚠️ If you edit opening balances, the *opening* sheet must balance too "
                       "(Assets = L + E), or the closing balance check won't be zero.")

    with right:
        income, cashflow, balance, balance_check = build_integrated_model(
            revenue, cogs_pct, sga, dep, interest_rate, tax_rate,
            dso, dio, dpo, capex, open_ppe,
            open_cash, open_receivables, open_inventory, open_payables,
            open_debt, share_capital, open_retained, payout,
        )

        balanced = abs(balance_check) < 1
        b1, b2, b3 = st.columns(3)
        b1.metric("Net Income", money(income["Net Income"]))
        b2.metric("Closing Cash", money(balance["Cash"]))
        b3.metric("Balance Check", money(balance_check),
                  "✅ Balanced" if balanced else "❌ Off",
                  delta_color="normal" if balanced else "inverse")

        if balanced:
            st.success("✅ **The model balances.** All three statements are telling a consistent story.")
        else:
            st.error(f"❌ Balance check = {money(balance_check)} — a linkage is broken.")

        if balance["Cash"] < 0:
            st.warning(
                f"🔎 Closing cash is negative ({money(balance['Cash'])}). Mathematically it still balances, "
                "but the business has a **funding gap** — it would need debt or equity to plug it."
            )

        col_is, col_cf, col_bs = st.columns(3)

        with col_is:
            st.markdown("**📄 Income Statement**")
            df_is = pd.DataFrame({"€": income}).reset_index()
            df_is.columns = ["Line", "€"]
            df_is["€"] = df_is["€"].map(money)
            st.dataframe(df_is, use_container_width=True, hide_index=True)

        with col_cf:
            st.markdown("**💵 Cash Flow**")
            df_cf = pd.DataFrame({"€": cashflow}).reset_index()
            df_cf.columns = ["Line", "€"]
            df_cf["€"] = df_cf["€"].map(money)
            st.dataframe(df_cf, use_container_width=True, hide_index=True)

        with col_bs:
            st.markdown("**🏛️ Balance Sheet**")
            df_bs = pd.DataFrame({"€": balance}).reset_index()
            df_bs.columns = ["Line", "€"]
            df_bs["€"] = df_bs["€"].map(money)
            st.dataframe(df_bs, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges (watch the balance check stay at €0)")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Depreciation ripple:** Raise depreciation to €500k. Net income falls, but closing cash barely moves
   (it's added back) — and the model *still balances*.
2. **Working-capital squeeze:** Push DSO to 90 days. Watch receivables rise, CFO fall, and cash drop —
   all three statements move together.
"""
        )
    with e2:
        st.markdown(
            """
3. **Capex funding gap:** Set capex to €1,500,000. Does cash go negative? The balance check stays €0,
   but the funding-gap warning fires.
4. **Payout policy:** Raise dividend payout to 100%. See retained earnings and cash both fall by the
   dividend — equity and assets move in lock-step.
"""
        )

    # Download combined model
    combined = pd.concat([
        pd.DataFrame({"Statement": "Income", "Line": list(income.keys()), "€": list(income.values())}),
        pd.DataFrame({"Statement": "Cash Flow", "Line": list(cashflow.keys()), "€": list(cashflow.values())}),
        pd.DataFrame({"Statement": "Balance Sheet", "Line": list(balance.keys()), "€": list(balance.values())}),
    ])
    st.download_button(
        "⬇️ Download the full integrated model (CSV)",
        combined.to_csv(index=False).encode("utf-8"),
        "integrated_3_statement_model.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The model that wouldn't balance by €84k", expanded=True):
        st.markdown(
            """
**Situation:** An analyst's three-statement model was off by exactly €84,000 and the deadline was looming.

**How integration thinking solved it:** €84k = the after-tax effect of the €120k depreciation. The clue:
depreciation was reducing PP&E and net income, but net income wasn't fully flowing to **retained
earnings**. Fixing that single link brought the balance check to zero.

**Why it matters:** In an integrated model, the *size* of the balance error often points directly to the
broken link.

**Lesson:** Don't hunt randomly — the balance-check number is a diagnostic that names the missing item.
"""
        )

    with st.expander("Case B — The circularity spiral (interest on debt)"):
        st.markdown(
            """
**Situation:** A model added interest calculated on *average* debt, and suddenly threw `#REF!`/`circular`
errors and unstable numbers.

**What happened:** Interest → net income → cash → debt (revolver) → interest… a **circular loop**.

**The fix:** Enable **iterative calculation**, and add a **circularity switch** (a cell that forces
interest to zero) so the model can be turned 'straight' for debugging, then switched back on.

**Lesson:** Circularity is normal in advanced models — but always build a switch so you can break the
loop when hunting errors.
"""
        )

    with st.expander("Case C — One model, every decision (the board pack)"):
        st.markdown(
            """
**Situation:** A factory needed a business case covering profitability, funding, and cash for the board.

**How the integrated model delivered:** A single linked model produced the **P&L** (is it profitable?),
the **cash flow** (can we fund it?), and the **balance sheet** (what's the resulting leverage?) — all
from one consistent set of assumptions. Changing a driver updated every board metric instantly.

**Why it matters:** Integration means one source of truth — no contradictory spreadsheets circulating.

**Lesson:** An integrated model is not just tidy — it's what lets you answer *any* board question
consistently and fast.
"""
        )

    st.info(
        "🔗 **Pattern:** Integration turns three separate reports into one decision engine. The balance "
        "check keeps it honest; the links make it powerful; the single source of truth makes it trusted."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_14"):
        q1 = st.radio(
            "**1.** In an integrated model, which line typically acts as the balancing 'plug'?",
            [
                "Revenue",
                "Cash (calculated from the cash flow statement)",
                "Depreciation",
                "Share capital",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** Net income links the income statement to the balance sheet via:",
            [
                "Accounts payable",
                "Retained earnings",
                "Inventory",
                "Capex",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The balance check should always equal:",
            [
                "Net income",
                "Zero (Assets − Liabilities − Equity = 0)",
                "Closing cash",
                "Total revenue",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Circularity in a model most commonly arises from:",
            [
                "Depreciation being a non-cash item",
                "Interest depending on debt, which depends on cash, which depends on net income (which includes interest)",
                "Adding a dividend line",
                "Using days ratios for working capital",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** If a model won't balance, the FIRST thing to check is:",
            [
                "Whether the font colours are correct",
                "That each link is intact — e.g. net income → retained earnings, capex → PP&E, closing cash → balance sheet",
                "The page margins",
                "Whether revenue is high enough",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Cash (calculated from the cash flow statement)"),
            "2": (q2, "Retained earnings"),
            "3": (q3, "Zero (Assets − Liabilities − Equity = 0)"),
            "4": (q4, "Interest depending on debt, which depends on cash, which depends on net income (which includes interest)"),
            "5": (q5, "That each link is intact — e.g. net income → retained earnings, capex → PP&E, closing cash → balance sheet"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you can now integrate a full three-statement model! On to Module 1.5. 🎉")
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
    f"Applied Financial Models · Module 1.4 Integrating & Balancing the Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
