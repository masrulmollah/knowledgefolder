"""
================================================================================
APPLIED FINANCIAL MODELS
Module 6.4 — WORKING CAPITAL OPTIMIZATION MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to optimise working capital: the cash conversion cycle (CCC), the DSO/DIO/DPO
levers, and how releasing cash from working capital creates value.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live CCC / cash-release engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_6_4_Working_Capital_Optimization.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="6.4 Working Capital Optimization — Applied Financial Models",
    layout="wide",
    page_icon="🚀",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def working_capital(revenue, cogs, dso, dio, dpo):
    """Return receivables, inventory, payables, net WC and CCC."""
    receivables = dso / 365 * revenue
    inventory = dio / 365 * cogs
    payables = dpo / 365 * cogs
    net_wc = receivables + inventory - payables
    ccc = dso + dio - dpo
    return receivables, inventory, payables, net_wc, ccc


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 6 · Specialised & Advanced Models")
st.sidebar.markdown(
    """
**Module 6.4 — Working Capital Optimization**

🟡 *Intermediate*

**You will learn to:**
- Calculate the cash conversion cycle (CCC)
- Use the DSO / DIO / DPO levers
- Quantify cash released from working capital
- Turn WC efficiency into real value
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to flex DSO/DIO/DPO and see how "
    "much cash you can release and how the CCC shortens."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🚀 6.4 · Working Capital Optimization Model")
st.markdown(
    """
Working capital — the cash tied up in **receivables** and **inventory**, less what you owe in **payables**
— is often a company's largest pool of 'trapped' cash. Optimising it releases cash **without** raising
debt, selling equity, or improving profit. For a manufacturer with large inventories and receivables, it's
one of the most powerful (and overlooked) value levers.

This module builds the **cash conversion cycle (CCC)** and shows how flexing the DSO / DIO / DPO levers
frees up cash and creates value.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "6.4")
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
### The three working-capital levers
Working capital is driven by three 'days' ratios — how long cash is tied up at each stage of the operating
cycle.
"""
    )
    levers = pd.DataFrame(
        {
            "Lever": ["DSO — Days Sales Outstanding", "DIO — Days Inventory Outstanding", "DPO — Days Payables Outstanding"],
            "Measures": [
                "How long customers take to pay you",
                "How long inventory sits before it's sold",
                "How long you take to pay suppliers",
            ],
            "To release cash…": [
                "**Lower** it (collect faster)",
                "**Lower** it (hold less stock)",
                "**Raise** it (pay suppliers later)",
            ],
        }
    )
    st.table(levers)

    st.markdown("### The Cash Conversion Cycle (CCC)")
    st.markdown("The CCC is the net number of days cash is tied up in operations:")
    st.latex(r"\text{CCC} = \text{DSO} + \text{DIO} - \text{DPO}")
    st.markdown(
        """
- A **shorter CCC** means cash cycles back to you faster — less working capital needed.
- A **negative CCC** (like some retailers) means you're paid by customers *before* you pay suppliers —
  the business is effectively **funded by its own operations**.
"""
    )

    st.markdown("### Converting days into cash")
    st.latex(r"\text{Receivables} = \frac{\text{DSO}}{365}\times \text{Revenue} \quad "
             r"\text{Inventory} = \frac{\text{DIO}}{365}\times \text{COGS} \quad "
             r"\text{Payables} = \frac{\text{DPO}}{365}\times \text{COGS}")
    st.latex(r"\text{Net Working Capital} = \text{Receivables} + \text{Inventory} - \text{Payables}")

    with st.expander("🔑 Concept 1 — Why working capital is 'trapped cash'"):
        st.markdown(
            """
Every euro sitting in receivables or inventory is cash you've already spent but haven't got back yet. It
earns **nothing** while it's trapped. Releasing it — by collecting faster, holding less stock, or paying
later — hands you **free cash** you can use to pay down debt, invest, or return to shareholders. No profit
improvement required.
"""
        )

    with st.expander("🔑 Concept 2 — The value of releasing cash"):
        st.markdown(
            """
Cash freed from working capital has a real value — you avoid the **cost of financing** it. If your cost of
capital is 10%, releasing €1m of trapped cash saves ~€100k a year in financing cost, *every year*. That's
why working-capital programmes are among the highest-return, lowest-risk initiatives a company can run.

$$\\text{Annual value of released cash} = \\text{Cash released} \\times \\text{Cost of capital}$$
"""
        )

    with st.expander("🔑 Concept 3 — The DSO lever (receivables)"):
        st.markdown(
            """
Lowering **DSO** means collecting from customers faster — via tighter credit terms, better invoicing,
early-payment discounts, or stronger collections. Each day of DSO reduction releases:

$$\\Delta\\text{Cash} = \\frac{1}{365}\\times \\text{Revenue}$$

But beware: pushing customers too hard on payment can hurt sales relationships — there's a commercial
trade-off.
"""
        )

    with st.expander("🔑 Concept 4 — The DIO lever (inventory)"):
        st.markdown(
            """
Lowering **DIO** means holding less stock — via better demand forecasting, leaner production (JIT),
SKU rationalisation, or faster throughput. For a manufacturer with hundreds of SKUs, inventory is often
the **biggest** working-capital lever. But cut too far and you risk **stock-outs** and lost sales — so
optimise, don't just minimise.
"""
        )

    with st.expander("🔑 Concept 5 — The DPO lever (payables)"):
        st.markdown(
            """
Raising **DPO** means taking longer to pay suppliers — effectively using them as a free source of
financing. Levers include renegotiating terms and centralising procurement. The trade-off: pushing
suppliers too hard can damage relationships, forfeit early-payment discounts, or raise prices. Balance is key.
"""
        )

    st.success(
        "**Takeaway:** Working capital is trapped cash. Shorten the cash conversion cycle (lower DSO & DIO, "
        "raise DPO) to release it — creating value equal to the financing cost saved, with no need to "
        "improve profit. But respect the commercial trade-offs with customers and suppliers."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Releasing cash from working capital")
    st.markdown("A manufacturer: **Revenue €2,000,000**, **COGS €1,200,000**. Current DSO 60, DIO 90, DPO 30.")

    st.markdown("#### Step 1 — Current working capital & CCC")
    st.markdown(
        """
| Item | Calculation | Value |
|---|---|---|
| Receivables | 60 ÷ 365 × 2,000,000 | €328,767 |
| Inventory | 90 ÷ 365 × 1,200,000 | €295,890 |
| Payables | 30 ÷ 365 × 1,200,000 | (€98,630) |
| **Net working capital** | | **€526,027** |
| **Cash conversion cycle** | 60 + 90 − 30 | **120 days** |
"""
    )

    st.markdown("#### Step 2 — Optimise: DSO 60→45, DIO 90→60, DPO 30→45")
    st.markdown(
        """
| Item | New calculation | New value |
|---|---|---|
| Receivables | 45 ÷ 365 × 2,000,000 | €246,575 |
| Inventory | 60 ÷ 365 × 1,200,000 | €197,260 |
| Payables | 45 ÷ 365 × 1,200,000 | (€147,945) |
| **Net working capital** | | **€295,890** |
| **Cash conversion cycle** | 45 + 60 − 45 | **60 days** |
"""
    )

    st.markdown("#### Step 3 — Cash released & value created")
    st.markdown(
        """
- **Cash released** = €526,027 − €295,890 = **€230,137**
- **CCC halved** from 120 → 60 days.
- At a 10% cost of capital, the annual value = €230,137 × 10% = **~€23,000/year**, every year.
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Cash released", "€230,137")
    e2.metric("CCC", "120 → 60 days", "−60 days")
    e3.metric("Annual value @10%", "~€23,000")

    st.info(
        "**Insight:** Without selling a single extra unit or improving margin, optimising the three levers "
        "**released €230k of cash** and halved the cash conversion cycle. That cash can repay debt or fund "
        "investment, and the recurring financing saving is ~€23k/year. **This is why working-capital "
        "programmes deliver such high returns for low risk** — but note we kept the changes moderate to "
        "avoid stock-outs or straining customer/supplier relationships."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Working Capital Optimizer")
    st.markdown(
        "Set the current position, then move the DSO / DIO / DPO levers to a target and see the cash "
        "released, the shorter CCC, and the recurring value created."
    )

    left, right = st.columns([0.36, 0.64])

    with left:
        st.markdown("##### 🏭 Business size")
        revenue = st.number_input("Revenue (€)", 100_000, 1_000_000_000, 2_000_000, 50_000)
        cogs = st.number_input("COGS (€)", 50_000, 1_000_000_000, 1_200_000, 50_000)
        cost_of_capital = st.slider("Cost of capital (%)", 1.0, 25.0, 10.0, 0.5)

        st.markdown("##### 📊 Current position (days)")
        dso0 = st.slider("Current DSO", 0, 180, 60, 1)
        dio0 = st.slider("Current DIO", 0, 365, 90, 1)
        dpo0 = st.slider("Current DPO", 0, 180, 30, 1)

        st.markdown("##### 🎯 Target position (days)")
        dso1 = st.slider("Target DSO", 0, 180, 45, 1)
        dio1 = st.slider("Target DIO", 0, 365, 60, 1)
        dpo1 = st.slider("Target DPO", 0, 180, 45, 1)

    with right:
        rec0, inv0, pay0, nwc0, ccc0 = working_capital(revenue, cogs, dso0, dio0, dpo0)
        rec1, inv1, pay1, nwc1, ccc1 = working_capital(revenue, cogs, dso1, dio1, dpo1)

        cash_released = nwc0 - nwc1
        annual_value = cash_released * cost_of_capital / 100

        k1, k2, k3 = st.columns(3)
        k1.metric("Cash released", money(cash_released),
                  "Freed ✅" if cash_released > 0 else "Consumed ❌",
                  delta_color="normal" if cash_released > 0 else "inverse")
        k2.metric("CCC", f"{ccc1:.0f} days", f"{ccc1 - ccc0:+.0f} days vs. current",
                  delta_color="normal" if ccc1 <= ccc0 else "inverse")
        k3.metric("Annual value", money(annual_value),
                  help="Cash released × cost of capital")

        if cash_released > 0:
            st.success(
                f"✅ **{money(cash_released)} of cash released** by shortening the CCC from {ccc0:.0f} to "
                f"{ccc1:.0f} days — worth ~{money(annual_value)}/year in saved financing. No profit "
                "improvement required."
            )
        elif cash_released < 0:
            st.warning(
                f"⚠️ These targets would **consume {money(-cash_released)}** more cash (the CCC lengthens). "
                "Re-check the levers — you want DSO & DIO down and DPO up."
            )
        else:
            st.info("No change in working capital from these targets.")

        # comparison table
        comp = pd.DataFrame(
            {
                "Item": ["Receivables (DSO)", "Inventory (DIO)", "Payables (DPO)", "Net working capital", "Cash conversion cycle"],
                "Current": [money(rec0), money(inv0), money(pay0), money(nwc0), f"{ccc0:.0f} days"],
                "Target": [money(rec1), money(inv1), money(pay1), money(nwc1), f"{ccc1:.0f} days"],
            }
        )
        st.markdown("##### 📄 Current vs. Target")
        st.dataframe(comp, use_container_width=True, hide_index=True)

        # chart
        chart = pd.DataFrame(
            {"Net working capital (€)": [nwc0, nwc1]},
            index=["Current", "Target"],
        )
        st.markdown("##### 📊 Working capital: current vs. target")
        st.bar_chart(chart)

        if ccc1 < 0:
            st.info("💡 Your target CCC is **negative** — customers pay you before you pay suppliers, so the "
                    "business is effectively self-funding its operations. Powerful, if achievable.")

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Inventory is king:** For a manufacturer, cut target DIO hard (e.g. 90→45). Notice it's usually the
   biggest single cash lever.
2. **Negative CCC:** Push DPO up and DSO/DIO down until the CCC goes negative. What does that imply?
"""
        )
    with e2:
        st.markdown(
            """
3. **The value of a day:** Lower target DSO by just 1 day. How much cash is that worth? (≈ Revenue ÷ 365.)
4. **Trade-off check:** Cut DIO to near zero — great for cash, but what's the real-world risk?
"""
        )

    st.download_button(
        "⬇️ Download the working-capital comparison (CSV)",
        comp.to_csv(index=False).encode("utf-8"),
        "working_capital_optimization.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Releasing cash from factory inventory", expanded=True):
        st.markdown(
            """
**Situation:** A manufacturer with 200+ SKUs carried very high inventory (long DIO), tying up millions in cash.

**How optimization helped:** Better demand forecasting, SKU rationalisation and leaner production cut DIO
significantly. Because inventory is the largest working-capital component for a manufacturer, even a
moderate DIO reduction **released a large amount of cash** — used to reduce debt.

**Why it matters:** The cash was freed **without** improving profit or raising finance — pure balance-sheet
efficiency.

**Lesson:** For manufacturers, inventory (DIO) is usually the single biggest working-capital lever.
"""
        )

    with st.expander("Case B — The growth cash trap (why WC discipline matters)"):
        st.markdown(
            """
**Situation:** A fast-growing company was profitable but constantly short of cash.

**What the CCC revealed:** As sales grew, receivables and inventory ballooned faster than cash came in —
a **long CCC** meant growth was *consuming* cash. Shortening the CCC (tighter collections, leaner stock)
freed cash to fund the growth itself.

**Why it matters:** Growth without working-capital discipline can starve a profitable company of cash
(the classic 'over-trading' trap).

**Lesson:** Manage the CCC actively during growth — profit doesn't guarantee cash.
"""
        )

    with st.expander("Case C — The supplier-terms trade-off"):
        st.markdown(
            """
**Situation:** A company tried to boost cash by aggressively extending payment terms (raising DPO).

**What happened:** It released cash short-term, but key suppliers **withdrew early-payment discounts and
raised prices**, and some relationships soured — partly offsetting the benefit.

**Why it matters:** Working-capital levers have **commercial trade-offs**; the cheapest cash isn't always
free once supplier reactions are counted.

**Lesson:** Optimise working capital with an eye on customer and supplier relationships — don't just
minimise the numbers.
"""
        )

    st.info(
        "🔗 **Pattern:** Working-capital optimization releases trapped cash by shortening the cash conversion "
        "cycle — a high-return, low-risk lever. But every lever (DSO, DIO, DPO) carries a commercial "
        "trade-off, so optimise, don't just minimise."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_64"):
        q1 = st.radio(
            "**1.** The cash conversion cycle (CCC) is calculated as:",
            [
                "DSO + DIO + DPO",
                "DSO + DIO − DPO",
                "DPO − DSO − DIO",
                "DSO × DIO ÷ DPO",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** To RELEASE cash from working capital, you generally want to:",
            [
                "Raise DSO and DIO, lower DPO",
                "Lower DSO and DIO, raise DPO",
                "Raise all three ratios",
                "Lower all three ratios",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** A NEGATIVE cash conversion cycle means:",
            [
                "The company is making a loss",
                "Customers pay before the company pays its suppliers (self-funding operations)",
                "The company has no inventory",
                "Debt exceeds equity",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** For a typical manufacturer, the LARGEST working-capital lever is usually:",
            [
                "Payables (DPO)",
                "Inventory (DIO)",
                "The tax rate",
                "Depreciation",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The value of cash released from working capital comes mainly from:",
            [
                "Higher reported profit",
                "Avoiding the financing cost of the trapped cash (cash released × cost of capital)",
                "A lower tax rate",
                "Issuing new shares",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "DSO + DIO − DPO"),
            "2": (q2, "Lower DSO and DIO, raise DPO"),
            "3": (q3, "Customers pay before the company pays its suppliers (self-funding operations)"),
            "4": (q4, "Inventory (DIO)"),
            "5": (q5, "Avoiding the financing cost of the trapped cash (cash released × cost of capital)"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered working capital optimization! On to Module 6.5 (Manufacturing / Factory Cost). 🎉")
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
    f"Applied Financial Models · Module 6.4 Working Capital Optimization Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
