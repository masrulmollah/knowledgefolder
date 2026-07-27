# ==============================================================================
# APPLIED FINANCIAL MODELS
# Module 3.1 - DISCOUNTED CASH FLOW (DCF)
# ==============================================================================
#
# A single-page, interactive Streamlit module that teaches finance professionals
# how to value a business using a DCF: free cash flow, WACC, terminal value, and
# the bridge from enterprise value to equity value (and share price).
#
# The page follows the standard 5-tab structure used across the site:
#     1. Theory & Concepts
#     2. Worked Examples
#     3. Interactive Exercises   (a full live DCF engine)
#     4. Real-Life Practical Cases
#     5. Knowledge Test / Quiz
#
# ------------------------------------------------------------------------------
# HOW TO RUN
# ------------------------------------------------------------------------------
#     pip install streamlit pandas
#     streamlit run Module_3_1_Discounted_Cash_Flow_DCF.py
# ==============================================================================

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="3.1 Discounted Cash Flow (DCF) - Applied Financial Models",
    layout="wide",
    page_icon="💰",
)

# ------------------------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def run_dcf(fcf0, growth_pct, wacc_pct, terminal_g_pct, years,
            net_debt, shares):
    """Run a DCF. Returns a dict with the year-by-year schedule and summary values."""
    wacc = wacc_pct / 100
    g = growth_pct / 100
    tg = terminal_g_pct / 100

    fcfs, discount_factors, pv_fcfs = [], [], []
    fcf = fcf0
    for y in range(1, years + 1):
        fcf = fcf * (1 + g)
        df = 1 / ((1 + wacc) ** y)
        pv = fcf * df
        fcfs.append(fcf)
        discount_factors.append(df)
        pv_fcfs.append(pv)

    sum_pv_fcf = sum(pv_fcfs)

    final_fcf = fcfs[-1]
    if wacc > tg:
        terminal_value = final_fcf * (1 + tg) / (wacc - tg)
    else:
        terminal_value = float("inf")
    pv_terminal = terminal_value * discount_factors[-1] if terminal_value != float("inf") else float("inf")

    enterprise_value = sum_pv_fcf + pv_terminal
    equity_value = enterprise_value - net_debt
    share_price = equity_value / shares if shares > 0 else 0

    tv_pct = (pv_terminal / enterprise_value * 100) if enterprise_value not in (0, float("inf")) else 0

    return {
        "fcfs": fcfs, "discount_factors": discount_factors, "pv_fcfs": pv_fcfs,
        "sum_pv_fcf": sum_pv_fcf, "terminal_value": terminal_value, "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value, "equity_value": equity_value,
        "share_price": share_price, "tv_pct": tv_pct,
    }


# ------------------------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 3 · Valuation Models")
st.sidebar.markdown(
    """
**Module 3.1 — Discounted Cash Flow (DCF)**

🔴 *Advanced*

**You will learn to:**
- Project free cash flow (FCF)
- Discount using WACC
- Calculate terminal value
- Bridge enterprise value → equity value → share price
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for a full live **DCF engine** "
    "- set FCF, WACC and terminal growth, and value a business in real time."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# ------------------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------------------
st.title("💰 3.1 · Discounted Cash Flow (DCF)")
st.markdown(
    """
The **DCF** is the cornerstone of valuation. Its logic is simple but powerful: a business is worth the
**present value of all the cash it will generate in the future**. Because a euro tomorrow is worth less
than a euro today (Module 0.4), we *discount* those future cash flows back to today using a rate that
reflects their risk - the **WACC**.

This flagship module builds the full DCF: projecting free cash flow, discounting it, adding a terminal
value, and bridging from **enterprise value** to **equity value** and a **share price**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "3.1")
c2.metric("Part", "3 - Valuation")
c3.metric("Level", "Advanced")
c4.metric("Learning Tabs", "5")

tab_labels = [
    "📚 Theory & Concepts",
    "🔢 Worked Examples",
    "✏️ Interactive Exercises",
    "🏭 Real-Life Practical Cases",
    "✅ Knowledge Test / Quiz",
]
tabs = st.tabs(tab_labels)

# ==============================================================================
# TAB 1 - THEORY & CONCEPTS
# ==============================================================================
with tabs[0]:
    st.subheader("Theory & Concepts")

    st.markdown(
        """
### The core idea
A DCF values a business as the sum of two parts:
1. The **present value of explicit forecast free cash flows** (usually 5-10 years).
2. The **present value of the terminal value** - everything beyond the forecast horizon.
"""
    )
    st.latex(r"\text{Enterprise Value} = \sum_{t=1}^{n} \frac{FCF_t}{(1+WACC)^t} + \frac{TV}{(1+WACC)^n}")

    st.markdown("### The building blocks")
    blocks = pd.DataFrame(
        {
            "Component": ["Free Cash Flow (FCF)", "WACC", "Terminal Value (TV)", "Net Debt", "Equity Value"],
            "What it is": [
                "Cash a business generates after reinvestment, available to all investors",
                "Weighted Average Cost of Capital - the blended required return (the discount rate)",
                "The value of all cash flows beyond the explicit forecast period",
                "Total debt minus cash",
                "What belongs to shareholders = Enterprise Value - Net Debt",
            ],
        }
    )
    st.table(blocks)

    with st.expander("🔑 Concept 1 - Free Cash Flow (what we discount)"):
        st.markdown(
            """
Unlevered **Free Cash Flow to the Firm (FCFF)** is the cash available to *all* investors (debt + equity):

$$FCF = EBIT \\times (1 - \\text{tax}) + \\text{Depreciation} - \\text{Capex} - \\Delta \\text{Working Capital}$$

It starts from operating profit (not net income) because we want the cash the *business* generates
before financing effects - those are captured in the WACC instead.
"""
        )

    with st.expander("🔑 Concept 2 - WACC (the discount rate)"):
        st.markdown(
            """
The **Weighted Average Cost of Capital** blends the required returns of debt and equity by their weights:

$$WACC = \\frac{E}{V} \\times K_e + \\frac{D}{V} \\times K_d \\times (1 - \\text{tax})$$

- $K_e$ = cost of equity (often via CAPM), $K_d$ = cost of debt.
- Debt is after-tax because interest is tax-deductible.
- **Higher WACC leads to lower valuation** (future cash is discounted harder). The valuation is *highly*
  sensitive to WACC - always sensitise it.
"""
        )

    with st.expander("🔑 Concept 3 - Terminal Value (usually the biggest piece)"):
        st.markdown(
            """
Since we can't forecast forever, the **terminal value** captures everything beyond the forecast horizon.
The **Gordon Growth (perpetuity) method**:

$$TV = \\frac{FCF_{n} \\times (1 + g)}{WACC - g}$$

where $g$ is the perpetual growth rate (must be **below** WACC, and typically <= long-run GDP growth).
The TV is then discounted back to today. It often represents **60-80% of total value** - so its
assumptions deserve real scrutiny.
"""
        )

    with st.expander("🔑 Concept 4 - Enterprise value to equity value to share price"):
        st.markdown(
            """
The DCF gives **Enterprise Value (EV)** - the value of the whole business (to debt + equity holders).
To get to what shareholders own:

$$\\text{Equity Value} = \\text{Enterprise Value} - \\text{Net Debt}$$
$$\\text{Share Price} = \\frac{\\text{Equity Value}}{\\text{Shares Outstanding}}$$

Net debt = total debt - cash. This **EV-to-equity bridge** is a step candidates often forget.
"""
        )

    with st.expander("🔑 Concept 5 - Strengths & weaknesses"):
        st.markdown(
            """
- ✅ **Strengths:** grounded in cash and fundamentals; intrinsic (not market-sentiment driven); forces
  explicit assumptions.
- ⚠️ **Weaknesses:** *highly* sensitive to WACC and terminal growth (small changes lead to big swings);
  garbage-in-garbage-out; terminal value dominates. Always **triangulate** with Comps (Module 3.2).
"""
        )

    st.success(
        "**Takeaway:** A DCF values a business as the present value of its future free cash flows plus a "
        "terminal value, discounted at WACC. Mind the sensitivity to WACC and terminal growth - and always "
        "cross-check with market multiples."
    )

# ==============================================================================
# TAB 2 - WORKED EXAMPLES
# ==============================================================================
with tabs[1]:
    st.subheader("Worked Example - Valuing a business with a 5-year DCF")
    st.markdown("A simplified DCF for a company generating **€1,000,000** of free cash flow this year.")

    st.markdown("#### Assumptions")
    st.markdown(
        """
| Assumption | Value |
|---|---|
| Base free cash flow (Year 0) | €1,000,000 |
| FCF growth (explicit period) | 8% p.a. |
| Forecast horizon | 5 years |
| WACC (discount rate) | 10% |
| Terminal growth (g) | 2.5% |
| Net debt | €2,000,000 |
| Shares outstanding | 1,000,000 |
"""
    )

    st.markdown("#### Step 1 - Project & discount the free cash flows")
    st.markdown(
        """
| Year | FCF (8% growth) | Discount factor @10% | PV of FCF |
|---|---|---|---|
| 1 | 1,080,000 | 0.9091 | 981,818 |
| 2 | 1,166,400 | 0.8264 | 963,967 |
| 3 | 1,259,712 | 0.7513 | 946,436 |
| 4 | 1,360,489 | 0.6830 | 929,215 |
| 5 | 1,469,328 | 0.6209 | 912,313 |
| **Sum of PV of FCF** | | | **€4,733,749** |
"""
    )

    st.markdown("#### Step 2 - Terminal value (Gordon growth)")
    st.markdown(
        """
$$TV = \\frac{FCF_5 \\times (1 + g)}{WACC - g} = \\frac{1{,}469{,}328 \\times 1.025}{0.10 - 0.025} = €20{,}081{,}150$$

Discount back to today: €20,081,150 × 0.6209 = **€12,468,406**
"""
    )

    st.markdown("#### Step 3 - Enterprise to equity to share price")
    e1, e2, e3 = st.columns(3)
    e1.metric("Enterprise Value", "€17,202,155", help="PV of FCF + PV of TV")
    e2.metric("Equity Value", "€15,202,155", help="EV - €2.0m net debt")
    e3.metric("Value per share", "€15.20", help="Equity / 1,000,000 shares")

    st.info(
        "**Insight:** Note that the terminal value's present value (€12.5m) is **~72% of the €17.2m "
        "enterprise value** - typical for a DCF. That's why the terminal growth rate and WACC deserve the "
        "most scrutiny: a 0.5% change in either moves the valuation by hundreds of thousands."
    )

# ==============================================================================
# TAB 3 - INTERACTIVE EXERCISES
# ==============================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise - A Full Live DCF Engine")
    st.markdown(
        "Set the assumptions on the left and watch the entire valuation build - year-by-year discounting, "
        "terminal value, and the bridge from enterprise value to a per-share price."
    )

    left, right = st.columns([0.32, 0.68])

    with left:
        st.markdown("##### 💵 Cash flow")
        fcf0 = st.number_input("Base free cash flow (€)", 100_000, 500_000_000, 1_000_000, 50_000)
        growth = st.slider("FCF growth - explicit period (%)", -10.0, 30.0, 8.0, 0.5)
        years = st.slider("Forecast horizon (years)", 3, 10, 5, 1)

        st.markdown("##### 🎯 Discounting")
        wacc = st.slider("WACC (%)", 4.0, 20.0, 10.0, 0.25)
        terminal_g = st.slider("Terminal growth g (%)", 0.0, 6.0, 2.5, 0.25)

        st.markdown("##### 🏦 Equity bridge")
        net_debt = st.number_input("Net debt (€)", -100_000_000, 500_000_000, 2_000_000, 100_000)
        shares = st.number_input("Shares outstanding", 1_000, 1_000_000_000, 1_000_000, 10_000)

    with right:
        if wacc / 100 <= terminal_g / 100:
            st.error(
                "⚠️ **WACC must be greater than terminal growth (g).** Otherwise the terminal value is "
                "infinite/meaningless. Lower g or raise WACC."
            )
        else:
            r = run_dcf(fcf0, growth, wacc, terminal_g, years, net_debt, shares)

            k1, k2, k3 = st.columns(3)
            k1.metric("Enterprise Value", money(r["enterprise_value"]))
            k2.metric("Equity Value", money(r["equity_value"]))
            k3.metric("Value per share", money(r["share_price"], dp=2))

            k4, k5, k6 = st.columns(3)
            k4.metric("PV of explicit FCF", money(r["sum_pv_fcf"]))
            k5.metric("PV of terminal value", money(r["pv_terminal"]))
            k6.metric("TV as % of EV", f"{r['tv_pct']:,.0f}%",
                      help="How much of the value comes from beyond the forecast")

            if r["tv_pct"] > 80:
                st.warning(
                    f"⚠️ Terminal value is **{r['tv_pct']:.0f}%** of enterprise value - the valuation rests "
                    "heavily on long-run assumptions. Scrutinise g and WACC carefully."
                )
            else:
                st.success(
                    f"✅ Enterprise value **{money(r['enterprise_value'])}**. Terminal value is "
                    f"{r['tv_pct']:.0f}% of the total - within a typical range."
                )

            sched = pd.DataFrame(
                {
                    "Year": list(range(1, years + 1)),
                    "FCF": r["fcfs"],
                    "Discount factor": r["discount_factors"],
                    "PV of FCF": r["pv_fcfs"],
                }
            )
            sched_disp = sched.copy()
            sched_disp["FCF"] = sched_disp["FCF"].map(money)
            sched_disp["Discount factor"] = sched_disp["Discount factor"].map(lambda v: f"{v:.4f}")
            sched_disp["PV of FCF"] = sched_disp["PV of FCF"].map(money)
            st.markdown("##### 📄 DCF Schedule")
            st.dataframe(sched_disp, use_container_width=True, hide_index=True)

            st.markdown("##### 📊 Value build-up")
            build = pd.DataFrame(
                {"€": [r["sum_pv_fcf"], r["pv_terminal"], r["enterprise_value"],
                       -net_debt, r["equity_value"]]},
                index=["PV of FCF", "PV of TV", "Enterprise Value", "- Net Debt", "Equity Value"],
            )
            st.bar_chart(build)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **WACC sensitivity:** Move WACC from 10% to 11%. Watch how much the valuation drops from a 1% change.
2. **Terminal dominance:** Set terminal growth to 4%. See TV's share of value balloon - is that credible?
"""
        )
    with e2:
        st.markdown(
            """
3. **The danger zone:** Set g just below WACC (e.g. WACC 8%, g 7.5%). Watch the valuation explode - a
   classic DCF pitfall.
4. **Equity bridge:** Raise net debt to €10m. See enterprise value unchanged but equity value fall.
"""
        )

    st.caption("🧠 Notice how *small* changes in WACC and terminal growth cause *large* swings - this "
               "sensitivity is the DCF's greatest weakness, and why you always sensitise these two inputs.")

# ==============================================================================
# TAB 4 - REAL-LIFE PRACTICAL CASES
# ==============================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A - Valuing an acquisition target", expanded=True):
        st.markdown(
            """
**Situation:** A company is considering acquiring a competitor and needs a defensible valuation.

**How the DCF helps:** By projecting the target's free cash flows and discounting at an appropriate WACC,
the acquirer gets an **intrinsic value** independent of current market noise - a basis for the offer price
and for identifying how much synergy would be needed to justify a premium.

**Why it matters:** Paying more than the DCF value (plus achievable synergies) destroys shareholder value.

**Lesson:** A DCF anchors deal pricing in fundamentals, not hope.
"""
        )

    with st.expander("Case B - The terminal-value reality check"):
        st.markdown(
            """
**Situation:** An analyst's DCF produced an eye-watering valuation that didn't feel right.

**What the model revealed:** The **terminal value was 90%+ of enterprise value**, driven by a 4.5%
perpetual growth rate - implying the company would eventually outgrow the whole economy. Trimming g to a
realistic 2% cut the valuation dramatically.

**Why it matters:** Terminal value usually dominates, so an unrealistic g quietly inflates the whole answer.

**Lesson:** Always check TV as a % of EV and keep perpetual growth at or below long-run GDP growth.
"""
        )

    with st.expander("Case C - WACC sensitivity swings the decision"):
        st.markdown(
            """
**Situation:** An investment committee debated whether a project cleared the bar; the DCF was marginal.

**What the model revealed:** A **sensitivity table** on WACC (9% / 10% / 11%) swung the valuation by tens
of percent. The 'answer' depended entirely on a discount rate that itself was an assumption.

**Why it matters:** Presenting a single-point DCF as 'the value' is misleading - the honest output is a
*range* driven by WACC and g.

**Lesson:** Never present a DCF as one number; show a sensitivity range and triangulate with Comps (3.2).
"""
        )

    st.info(
        "🔗 **Pattern:** A DCF is only as good as its assumptions. Its power is intrinsic, cash-based "
        "valuation; its danger is false precision. Sensitise WACC and g, sanity-check terminal value, and "
        "cross-check with market multiples."
    )

# ==============================================================================
# TAB 5 - KNOWLEDGE TEST / QUIZ
# ==============================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_31"):
        q1 = st.radio(
            "**1.** A DCF values a business as:",
            [
                "The book value of its assets",
                "The present value of its expected future free cash flows",
                "Last year's net income x 10",
                "Total revenue minus total costs",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** In a DCF, the discount rate used is typically the:",
            [
                "Inflation rate",
                "WACC (Weighted Average Cost of Capital)",
                "Corporate tax rate",
                "Dividend yield",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** All else equal, a HIGHER WACC results in:",
            [
                "A higher valuation",
                "A lower valuation (future cash is discounted more heavily)",
                "No change to valuation",
                "A higher terminal growth rate",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** The Gordon Growth terminal value formula requires that:",
            [
                "Terminal growth g is greater than WACC",
                "Terminal growth g is less than WACC",
                "WACC equals zero",
                "There is no net debt",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** To get from Enterprise Value to Equity Value you:",
            [
                "Add net debt",
                "Subtract net debt",
                "Multiply by the tax rate",
                "Divide by WACC",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The present value of its expected future free cash flows"),
            "2": (q2, "WACC (Weighted Average Cost of Capital)"),
            "3": (q3, "A lower valuation (future cash is discounted more heavily)"),
            "4": (q4, "Terminal growth g is less than WACC"),
            "5": (q5, "Subtract net debt"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent - you've mastered the DCF! On to Module 3.2 (Comparable Company Analysis). 🎉")
        elif score >= 3:
            st.info("Good work - review the feedback below to close the gaps.")
        else:
            st.warning("Worth another pass - revisit the Theory tab, then retry.")

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
    f"Applied Financial Models · Module 3.1 Discounted Cash Flow (DCF) · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
