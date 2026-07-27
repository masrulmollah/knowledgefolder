"""
================================================================================
APPLIED FINANCIAL MODELS
Module 0.4 — CORE BUILDING BLOCKS
================================================================================

A single-page, interactive Streamlit module covering the mathematical foundations
every financial model relies on: time value of money, compounding, discounting,
growth rates (CAGR) and key financial ratios.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (live TVM / CAGR calculators with charts)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_0_4_Core_Building_Blocks.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="0.4 Core Building Blocks — Applied Financial Models",
    layout="wide",
    page_icon="🧭",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    return f"{symbol}{x:,.{dp}f}"


def future_value(pv, rate_pct, years):
    return pv * (1 + rate_pct / 100) ** years


def present_value(fv, rate_pct, years):
    return fv / (1 + rate_pct / 100) ** years


def cagr(begin, end, years):
    if begin <= 0 or years <= 0:
        return 0.0
    return ((end / begin) ** (1 / years) - 1) * 100


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 0 · Orientation & Foundations")
st.sidebar.markdown(
    """
**Module 0.4 — Core Building Blocks**

🟢 *Foundational*

**You will learn to:**
- Apply the time value of money (TVM)
- Compound a value forward & discount it back
- Calculate growth rates and CAGR
- Use key financial ratios to read performance
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for live calculators — "
    "compound money forward, discount it back, and compute CAGR."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🧭 0.4 · Core Building Blocks")
st.markdown(
    """
Before building any model, you need the **mathematical toolkit** that underpins them all. Almost every
financial model — from a simple forecast to a full valuation — rests on a handful of core concepts:
the **time value of money**, **compounding**, **discounting**, **growth rates**, and **ratios**.

Master these five building blocks and the rest of the course becomes far easier — because you'll
recognise them appearing again and again.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "0.4")
c2.metric("Part", "0 — Foundations")
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
### 1. The Time Value of Money (TVM)
> **A euro today is worth more than a euro tomorrow.**

Why? Because a euro today can be invested to earn a return, it's certain (no risk of not receiving it),
and inflation erodes future purchasing power. TVM is the single most important idea in finance — it's
why we *compound* and *discount*.
"""
    )

    st.markdown(
        """
### 2. Compounding — growing a value forward
Compounding answers: *"If I invest an amount today, what will it be worth in the future?"*

$$FV = PV \\times (1 + r)^{n}$$

- **FV** = future value  •  **PV** = present value  •  **r** = rate per period  •  **n** = number of periods
- The magic is **interest on interest** — growth accelerates over time.
"""
    )

    st.markdown(
        """
### 3. Discounting — bringing a value back to today
Discounting is the reverse: *"What is a future amount worth in today's money?"* It's the engine behind
NPV and DCF valuation (Parts 3 & 4).

$$PV = \\frac{FV}{(1 + r)^{n}}$$

- **r** here is the **discount rate** — it reflects risk and opportunity cost.
- The further away the cash flow (larger **n**), the more it is discounted.
"""
    )

    st.markdown(
        """
### 4. Growth rates & CAGR
A single-period growth rate is simple: $(\\text{new} - \\text{old}) / \\text{old}$. But over multiple
periods we use the **Compound Annual Growth Rate (CAGR)** — the smooth annual rate that connects a
starting and ending value:

$$CAGR = \\left(\\frac{\\text{End Value}}{\\text{Begin Value}}\\right)^{\\frac{1}{n}} - 1$$

CAGR strips out year-to-year noise and tells you the *average* compounded growth.
"""
    )

    st.markdown("### 5. Key financial ratios")
    ratios = pd.DataFrame(
        {
            "Ratio": [
                "Gross / EBITDA / Net Margin", "Return on Investment (ROI)",
                "Current Ratio", "Debt-to-Equity", "Interest Cover",
            ],
            "Formula": [
                "Profit line ÷ Revenue", "Gain ÷ Investment",
                "Current Assets ÷ Current Liabilities", "Total Debt ÷ Equity",
                "EBIT ÷ Interest",
            ],
            "Tells you": [
                "Profitability at each level of the P&L",
                "Efficiency of an investment",
                "Short-term liquidity / ability to pay bills",
                "Leverage / financial risk",
                "Ability to service debt from operating profit",
            ],
        }
    )
    st.table(ratios)

    with st.expander("🔑 Deep dive — Why compounding is so powerful (the 'Rule of 72')"):
        st.markdown(
            """
A quick mental shortcut: divide **72** by the annual rate to estimate how many years it takes money to
**double**.

- At 6% → 72 ÷ 6 = **12 years** to double.
- At 9% → 72 ÷ 9 = **8 years** to double.

Small differences in rate compound into huge differences over time — the core reason early investment
and cost of capital matter so much.
"""
        )

    with st.expander("🔑 Deep dive — The discount rate is an assumption, not a fact"):
        st.markdown(
            """
The discount rate (**r**) captures risk and opportunity cost. A higher rate = future cash is worth less
today. Because valuations are **highly sensitive** to this single number, it must always be justified
and stress-tested (you'll do exactly this in the DCF and NPV modules).
"""
        )

    with st.expander("🔑 Deep dive — Nominal vs. real (watch out for inflation)"):
        st.markdown(
            """
- **Nominal** values/rates include inflation.
- **Real** values/rates strip inflation out.

Golden rule: **be consistent** — discount nominal cash flows at a nominal rate, and real cash flows at
a real rate. Mixing them is a common and costly modeling error.
"""
        )

    st.success(
        "**Takeaway:** Compounding grows money forward; discounting brings it back; CAGR smooths growth; "
        "ratios read performance. These five tools reappear in almost every model you'll ever build."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Examples — The core formulas in action")

    st.markdown("#### Example 1 — Compounding (future value)")
    st.markdown(
        """
*You invest **€100,000** at **8%** per year for **5 years**. What is it worth at the end?*

$$FV = 100{,}000 \\times (1 + 0.08)^{5} = 100{,}000 \\times 1.4693 = \\mathbf{€146{,}933}$$

**Insight:** You earned €46,933 — and roughly €6,900 of that is *interest on interest* (compounding),
not just simple interest.
"""
    )

    st.markdown("#### Example 2 — Discounting (present value)")
    st.markdown(
        """
*A project will pay you **€146,933** in **5 years**. If your discount rate is **8%**, what is it worth today?*

$$PV = \\frac{146{,}933}{(1 + 0.08)^{5}} = \\frac{146{,}933}{1.4693} = \\mathbf{€100{,}000}$$

**Insight:** Discounting is the exact mirror of compounding — it unwinds the growth back to today's money.
This is the foundation of every NPV and DCF valuation.
"""
    )

    st.markdown("#### Example 3 — CAGR (compound annual growth rate)")
    st.markdown(
        """
*Revenue grew from **€400m** to **€550m** over **4 years**. What was the CAGR?*

$$CAGR = \\left(\\frac{550}{400}\\right)^{\\frac{1}{4}} - 1 = (1.375)^{0.25} - 1 = \\mathbf{8.3\\%}$$

**Insight:** Even though total growth was 37.5%, the *smoothed annual* rate is 8.3% — the number you'd
use to compare against other businesses or forecast forward.
"""
    )

    st.markdown("#### Example 4 — A quick ratio read")
    st.markdown(
        """
*A company has EBIT of **€380k** and interest expense of **€50k**.*

$$\\text{Interest Cover} = \\frac{380}{50} = \\mathbf{7.6\\times}$$

**Insight:** Operating profit covers interest 7.6 times over — comfortable. Lenders typically want this
above ~3×, so this business has healthy debt-servicing capacity.
"""
    )

    st.info(
        "👉 Now open the **Interactive Exercises** tab and run these calculations yourself with any numbers "
        "you like — watch the compounding curve and discounting decay in real time."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Calculators")
    st.markdown("Three live tools. Change any input and watch the result — and the chart — update instantly.")

    calc = st.radio(
        "Choose a calculator:",
        ["📈 Compounding (Future Value)", "📉 Discounting (Present Value)", "🚀 CAGR (Growth Rate)"],
        horizontal=True,
    )

    st.markdown("---")

    # -------- Compounding --------
    if calc == "📈 Compounding (Future Value)":
        left, right = st.columns([0.35, 0.65])
        with left:
            pv = st.number_input("Present value today (€)", 1_000, 10_000_000, 100_000, 1_000)
            rate = st.slider("Annual rate (%)", 0.0, 25.0, 8.0, 0.5)
            years = st.slider("Number of years", 1, 40, 5, 1)
        with right:
            fv = future_value(pv, rate, years)
            simple = pv + pv * (rate / 100) * years
            k1, k2, k3 = st.columns(3)
            k1.metric("Future value", money(fv))
            k2.metric("Total gain", money(fv - pv))
            k3.metric("Compounding bonus", money(fv - simple),
                      help="Extra vs. simple interest = interest-on-interest")

            series = {f"Year {y}": future_value(pv, rate, y) for y in range(0, years + 1)}
            chart_df = pd.DataFrame({"Value (€)": list(series.values())},
                                    index=list(series.keys()))
            st.line_chart(chart_df)
            doubling = 72 / rate if rate > 0 else float("inf")
            st.caption(f"🧮 Rule of 72: at {rate:.1f}%, money doubles in ~**{doubling:,.1f} years**.")

    # -------- Discounting --------
    elif calc == "📉 Discounting (Present Value)":
        left, right = st.columns([0.35, 0.65])
        with left:
            fv = st.number_input("Future amount to receive (€)", 1_000, 10_000_000, 146_933, 1_000)
            rate = st.slider("Discount rate (%)", 0.0, 25.0, 8.0, 0.5)
            years = st.slider("Years until received", 1, 40, 5, 1)
        with right:
            pv = present_value(fv, rate, years)
            k1, k2 = st.columns(2)
            k1.metric("Present value (today)", money(pv))
            k2.metric("Value lost to discounting", money(fv - pv),
                      help="How much the delay + risk costs you")

            series = {f"Year {y}": present_value(fv, rate, y) for y in range(0, years + 1)}
            chart_df = pd.DataFrame({"Present value (€)": list(series.values())},
                                    index=list(series.keys()))
            st.line_chart(chart_df)
            st.caption(
                f"📉 €{fv:,.0f} received in {years} years is worth only **{money(pv)}** today at {rate:.1f}%. "
                "The further out (and higher the rate), the less it's worth now."
            )

    # -------- CAGR --------
    else:
        left, right = st.columns([0.35, 0.65])
        with left:
            begin = st.number_input("Beginning value (€)", 1_000, 10_000_000, 400_000_000, 1_000_000)
            end = st.number_input("Ending value (€)", 1_000, 100_000_000_000, 550_000_000, 1_000_000)
            years = st.slider("Number of years", 1, 40, 4, 1)
        with right:
            g = cagr(begin, end, years)
            total_growth = (end / begin - 1) * 100 if begin else 0
            k1, k2, k3 = st.columns(3)
            k1.metric("CAGR", f"{g:,.2f}%")
            k2.metric("Total growth", f"{total_growth:,.1f}%")
            k3.metric("Growth multiple", f"{end/begin:,.2f}×" if begin else "—")

            series = {f"Year {y}": begin * (1 + g / 100) ** y for y in range(0, years + 1)}
            chart_df = pd.DataFrame({"Smoothed value (€)": list(series.values())},
                                    index=list(series.keys()))
            st.line_chart(chart_df)
            st.caption(
                f"🚀 A CAGR of **{g:,.2f}%** is the smooth annual rate connecting {money(begin)} to "
                f"{money(end)} over {years} years."
            )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Rule of 72:** In the compounding tool, set the rate to 9%. Does the value roughly double in 8 years?
2. **Time kills value:** In discounting, push 'years until received' from 5 to 20. Watch today's value collapse.
"""
        )
    with e2:
        st.markdown(
            """
3. **Rate sensitivity:** In discounting, hold years fixed and raise the rate from 5% to 20%. How much value is lost?
4. **CAGR vs. total:** In CAGR, set begin €100, end €200, years 10. Note CAGR ≈ 7.2% (Rule of 72 in reverse!).
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The €6m Capex decision (discounting in action)", expanded=True):
        st.markdown(
            """
**Situation:** A factory expects €1.5m of annual savings for 8 years from a €6m automation project.

**Where the building blocks apply:** You can't just add up €1.5m × 8 = €12m and call it a €6m profit —
those future savings are worth **less in today's money**. Each year's saving must be **discounted** back
at the company's cost of capital before comparing to the €6m spent today.

**Why it matters:** TVM/discounting is precisely what turns a naïve "€12m > €6m, easy yes" into a
rigorous NPV decision (built fully in Module 4.1).

**Lesson:** Never compare cash flows from different points in time without discounting first.
"""
        )

    with st.expander("Case B — Comparing two growth stories (CAGR)"):
        st.markdown(
            """
**Situation:** Business A grew revenue from €100m to €160m in 5 years; Business B from €50m to €90m in
3 years. Which grew faster?

**Where the building blocks apply:** Totals mislead (A: +60%, B: +80%). **CAGR** normalises for time:
A ≈ 9.9%/yr, B ≈ 21.6%/yr. B is growing far faster on a like-for-like annual basis.

**Why it matters:** CAGR lets you compare growth across different time horizons fairly — essential for
benchmarking and forecasting.

**Lesson:** Always compare growth on a CAGR basis, not raw totals.
"""
        )

    with st.expander("Case C — Reading a company's health in 30 seconds (ratios)"):
        st.markdown(
            """
**Situation:** Before a supplier negotiation, you glance at their accounts: Interest Cover 1.8×,
Debt-to-Equity 3.5×, Current Ratio 0.9.

**Where the building blocks apply:** These **ratios** instantly signal a highly-leveraged, cash-tight
business — interest is barely covered and short-term liabilities exceed liquid assets.

**Why it matters:** A 30-second ratio read shapes your negotiation stance (e.g. don't over-rely on this
supplier; watch payment terms).

**Lesson:** Ratios turn raw numbers into fast, actionable insight — the analyst's quick diagnostic.
"""
        )

    st.info(
        "🔗 **Pattern:** These aren't abstract maths — TVM drives every investment decision, CAGR drives "
        "every growth comparison, and ratios drive every quick health check. They're the vocabulary of finance."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_04"):
        q1 = st.radio(
            "**1.** The time value of money principle states that:",
            [
                "A euro tomorrow is worth more than a euro today",
                "A euro today is worth more than a euro tomorrow",
                "Money has no value over time",
                "Inflation increases the value of future money",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** Which formula gives the FUTURE value of money?",
            [
                "PV = FV / (1+r)^n",
                "FV = PV × (1+r)^n",
                "FV = PV × r × n",
                "CAGR = (End/Begin)^(1/n) − 1",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Discounting is used to:",
            [
                "Grow a present amount into the future",
                "Convert a future cash flow into its value today",
                "Remove all risk from a project",
                "Calculate gross margin",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Revenue grows from €100m to €200m over 10 years. Using the Rule of 72, the CAGR is approximately:",
            ["3.6%", "7.2%", "10%", "20%"],
            index=None,
        )
        q5 = st.radio(
            "**5.** A higher discount rate applied to a future cash flow will make its present value:",
            [
                "Higher",
                "Lower",
                "Unchanged",
                "Equal to the future value",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "A euro today is worth more than a euro tomorrow"),
            "2": (q2, "FV = PV × (1+r)^n"),
            "3": (q3, "Convert a future cash flow into its value today"),
            "4": (q4, "7.2%"),
            "5": (q5, "Lower"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered the core building blocks! On to Module 0.5. 🎉")
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

        st.caption("Q4 note: Rule of 72 → to double (×2) in 10 years, rate ≈ 72 ÷ 10 = 7.2%.")

st.markdown("---")
st.caption(
    f"Applied Financial Models · Module 0.4 Core Building Blocks · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
