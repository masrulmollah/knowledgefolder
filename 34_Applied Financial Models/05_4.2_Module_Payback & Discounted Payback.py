"""
================================================================================
APPLIED FINANCIAL MODELS
Module 4.2 — PAYBACK & DISCOUNTED PAYBACK
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
the payback period and discounted payback period: how to calculate them, how they
differ, and their limitations versus NPV/IRR.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (simple vs. discounted payback, side by side)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_4_2_Payback_and_Discounted_Payback.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="4.2 Payback & Discounted Payback — Applied Financial Models",
    layout="wide",
    page_icon="🏗️",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def payback_from_cumulative(cum_series):
    """
    Given a list of cumulative balances (index 0 = t0), return the fractional
    period at which cumulative first turns >= 0 (after t0). None if never.
    """
    for t in range(1, len(cum_series)):
        prev = cum_series[t - 1]
        curr = cum_series[t]
        if curr >= 0:
            period_flow = curr - prev
            if period_flow != 0:
                frac = -prev / period_flow
                return (t - 1) + frac
            return float(t)
    return None


def build_paybacks(investment, annual_cf, years, cf_growth, discount_rate):
    """Return a DataFrame with cash flows, discounted flows, and both cumulative balances."""
    r = discount_rate / 100
    rows = []
    cf = annual_cf
    cum = -float(investment)
    dcum = -float(investment)
    rows.append({"Year": 0, "Cash flow": -float(investment), "Discounted CF": -float(investment),
                 "Cumulative CF": cum, "Cumulative Discounted CF": dcum})
    for y in range(1, years + 1):
        if y > 1:
            cf *= (1 + cf_growth / 100)
        dcf = cf / ((1 + r) ** y)
        cum += cf
        dcum += dcf
        rows.append({"Year": y, "Cash flow": cf, "Discounted CF": dcf,
                     "Cumulative CF": cum, "Cumulative Discounted CF": dcum})
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 4 · Investment Appraisal & Capital Budgeting")
st.sidebar.markdown(
    """
**Module 4.2 — Payback & Discounted Payback**

🟡 *Intermediate*

**You will learn to:**
- Calculate the simple payback period
- Calculate the discounted payback period
- See why discounting lengthens payback
- Know payback's uses and limitations
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to compare simple vs. "
    "discounted payback and watch the cumulative cash flow cross zero."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏗️ 4.2 · Payback & Discounted Payback")
st.markdown(
    """
**Payback** answers a simple, intuitive question every manager asks: *"How long until we get our money
back?"* It's the most widely used appraisal metric in practice because it's easy to understand and gives
a quick read on **risk and liquidity**.

This module covers both the **simple payback** and the more rigorous **discounted payback** (which
respects the time value of money) — and, crucially, where payback falls short versus NPV and IRR (4.1).
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "4.2")
c2.metric("Part", "4 — Appraisal")
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
### Simple payback period
The **payback period** is the time it takes for a project's cumulative cash inflows to recover the
initial investment. For even annual cash flows:
"""
    )
    st.latex(r"\text{Payback} = \frac{\text{Initial Investment}}{\text{Annual Cash Flow}}")
    st.markdown(
        """
For uneven cash flows, you accumulate year by year until the cumulative balance turns positive
(interpolating within the final year).
"""
    )

    st.markdown("### Discounted payback period")
    st.markdown(
        """
The simple payback has a major flaw: it treats a euro in Year 5 the same as a euro today. The
**discounted payback** fixes this by first **discounting** each cash flow to today's value, then finding
when the *discounted* cumulative balance turns positive.
"""
    )
    st.latex(r"\text{Discounted CF}_t = \frac{CF_t}{(1+r)^t}")
    st.markdown(
        "Because discounted cash flows are smaller, the **discounted payback is always longer** than the "
        "simple payback."
    )

    st.markdown("### Payback vs. NPV / IRR")
    comp = pd.DataFrame(
        {
            "Aspect": ["Time value of money", "Cash flows after payback", "Measures", "Main use"],
            "Simple Payback": ["Ignored ❌", "Ignored ❌", "Time to recover cash", "Quick risk/liquidity check"],
            "Discounted Payback": ["Included ✅", "Ignored ❌", "Time to recover in PV terms", "Risk check with TVM"],
            "NPV / IRR": ["Included ✅", "Included ✅", "Value created / return", "The primary decision"],
        }
    )
    st.table(comp)

    with st.expander("🔑 Concept 1 — Why managers love payback"):
        st.markdown(
            """
Despite its flaws, payback is hugely popular because it:
- Is **simple** to calculate and explain to non-finance people.
- Gives a quick sense of **risk** — a shorter payback means less time exposed to uncertainty.
- Emphasises **liquidity** — how fast cash comes back, which matters for cash-constrained firms.

It answers "how exposed are we, and for how long?" — a genuinely useful question.
"""
        )

    with st.expander("🔑 Concept 2 — Why discounted payback is better"):
        st.markdown(
            """
Simple payback pretends a euro in five years equals a euro today. **Discounted payback** discounts each
inflow first, so it reflects the real economic recovery time. It's always **longer** than simple payback
(sometimes a project never pays back in discounted terms even though it does in simple terms — a red flag).
"""
        )

    with st.expander("🔑 Concept 3 — The two big limitations (of both)"):
        st.markdown(
            """
Even discounted payback shares one fatal flaw with simple payback:

1. **It ignores everything after the payback point.** A project that pays back in 4 years then earns
   huge cash for 20 more looks identical to one that dies at year 5. Payback can't see the difference.
2. **It has no value measure.** It tells you *when* you break even, not *how much value* is created —
   only NPV does that.

**Therefore:** use payback as a **supplementary** screen, never as the sole decision rule.
"""
        )

    with st.expander("🔑 Concept 4 — How to use payback well"):
        st.markdown(
            """
Best practice: use payback **alongside** NPV/IRR.
- **NPV/IRR** make the *value* decision (accept/reject).
- **Payback** adds a *risk/liquidity* lens (how long is our capital at risk?).
- Many firms set a **maximum acceptable payback** (e.g. "must pay back within 4 years") as a *screening*
  hurdle, then rank surviving projects by NPV.
"""
        )

    st.success(
        "**Takeaway:** Payback measures how fast you recover your investment — simple payback ignores the "
        "time value of money, discounted payback fixes that, but both ignore everything after payback and "
        "neither measures value. Use them to gauge risk, and let NPV make the decision."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Simple vs. discounted payback")
    st.markdown("The €6m automation project from Module 4.1: €1.2m/year for 8 years, discount rate 10%.")

    st.markdown("#### Simple payback")
    st.markdown(
        """
$$\\text{Payback} = \\frac{€6{,}000{,}000}{€1{,}200{,}000 \\text{ / yr}} = \\mathbf{5.0 \\text{ years}}$$

After 5 years the cumulative inflows (€6.0m) exactly recover the €6.0m investment.
"""
    )

    st.markdown("#### Discounted payback (at 10%)")
    st.markdown(
        """
| Year | Cash flow | Discounted CF @10% | Cumulative discounted |
|---|---|---|---|
| 0 | −6,000,000 | −6,000,000 | −6,000,000 |
| 1 | 1,200,000 | 1,090,909 | −4,909,091 |
| 2 | 1,200,000 | 991,736 | −3,917,355 |
| 3 | 1,200,000 | 901,578 | −3,015,776 |
| 4 | 1,200,000 | 819,616 | −2,196,160 |
| 5 | 1,200,000 | 745,105 | −1,451,055 |
| 6 | 1,200,000 | 677,368 | −773,687 |
| 7 | 1,200,000 | 615,789 | −157,898 |
| 8 | 1,200,000 | 559,808 | +401,911 |

The discounted cumulative balance turns positive during **Year 8** → discounted payback ≈ **7.3 years**.
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Simple payback", "5.0 years")
    e2.metric("Discounted payback", "≈ 7.3 years")
    e3.metric("Difference", "+2.3 years", help="The cost of ignoring the time value of money")

    st.info(
        "**Insight:** The simple payback (5.0 yrs) *understates* how long recovery really takes. Once you "
        "account for the time value of money, it's **7.3 years** — cutting it fine against the asset's "
        "8-year life. The final year's positive balance (+€401,911) is exactly the project's NPV from 4.1 — "
        "confirming the link: **discounted payback reaches zero, then keeps going to become the NPV.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Simple vs. Discounted Payback")
    st.markdown(
        "Set the project parameters and compare both payback methods. Watch the cumulative cash flow lines "
        "cross zero at different times."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        investment = st.number_input("Initial investment (€)", 10_000, 100_000_000, 6_000_000, 100_000)
        annual_cf = st.number_input("Annual cash inflow (€)", 1_000, 50_000_000, 1_200_000, 50_000)
        years = st.slider("Project life (years)", 1, 20, 8, 1)
        cf_growth = st.slider("Cash-flow growth (%)", -10.0, 15.0, 0.0, 0.5)
        discount_rate = st.slider("Discount rate (%)", 0.0, 25.0, 10.0, 0.5)
        target_pb = st.slider("Max acceptable payback (years)", 1, 20, 6, 1)

    with right:
        df = build_paybacks(investment, annual_cf, years, cf_growth, discount_rate)

        simple_pb = payback_from_cumulative(list(df["Cumulative CF"]))
        disc_pb = payback_from_cumulative(list(df["Cumulative Discounted CF"]))
        final_npv = df["Cumulative Discounted CF"].iloc[-1]

        k1, k2, k3 = st.columns(3)
        k1.metric("Simple payback",
                  f"{simple_pb:.1f} yrs" if simple_pb is not None else "Never")
        k2.metric("Discounted payback",
                  f"{disc_pb:.1f} yrs" if disc_pb is not None else "Never")
        k3.metric("NPV (final disc. cum.)", money(final_npv),
                  "Value +" if final_npv > 0 else "Value −",
                  delta_color="normal" if final_npv > 0 else "inverse")

        # verdict vs target
        if simple_pb is None:
            st.error("❌ The project **never** recovers its investment (simple basis). Reject.")
        elif disc_pb is None:
            st.warning(
                f"⚠️ Simple payback is {simple_pb:.1f} yrs, but on a **discounted** basis the project "
                "**never** pays back within its life — a red flag despite the simple figure looking OK."
            )
        elif disc_pb <= target_pb:
            st.success(
                f"✅ Discounted payback ({disc_pb:.1f} yrs) is within your {target_pb}-year target — "
                "passes the screen. Confirm the decision with NPV."
            )
        else:
            st.warning(
                f"⚠️ Discounted payback ({disc_pb:.1f} yrs) **exceeds** your {target_pb}-year target — "
                "fails the payback screen even if NPV is positive."
            )

        # table
        disp = df.copy()
        for col in ["Cash flow", "Discounted CF", "Cumulative CF", "Cumulative Discounted CF"]:
            disp[col] = disp[col].map(money)
        st.markdown("##### 📄 Cash Flow & Cumulative Recovery")
        st.dataframe(disp, use_container_width=True, hide_index=True)

        st.markdown("##### 📈 Cumulative recovery (crosses €0 at payback)")
        chart = df.set_index("Year")[["Cumulative CF", "Cumulative Discounted CF"]]
        st.line_chart(chart)
        st.caption(
            "The **simple** line crosses €0 first; the **discounted** line crosses later (or not at all). "
            "The gap between them is the cost of ignoring the time value of money."
        )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Discount bite:** Raise the discount rate from 10% → 20%. Watch the discounted payback stretch out
   (or disappear) while simple payback is unchanged.
2. **Never pays back:** Cut annual cash flow to €700k. Does the discounted line ever cross zero?
"""
        )
    with e2:
        st.markdown(
            """
3. **After-payback blindness:** Set life to 20 years. Payback doesn't change, but think about how much
   value payback is *ignoring* beyond the payback point.
4. **Screen vs. value:** Find a case that fails your payback target but still has a positive NPV.
"""
        )

    st.download_button(
        "⬇️ Download this payback analysis (CSV)",
        df.to_csv(index=False).encode("utf-8"),
        "payback_analysis.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Payback as a fast risk screen", expanded=True):
        st.markdown(
            """
**Situation:** A factory faced dozens of small improvement proposals and couldn't build a full DCF for each.

**How payback helped:** A simple rule — *"must pay back within 3 years"* — quickly screened out the
slow-return projects, leaving a shortlist for proper NPV analysis.

**Why it matters:** Payback is a cheap, fast **first filter** when you have many small decisions and
limited analyst time.

**Lesson:** Use payback as an efficient screening hurdle, then apply NPV to the survivors.
"""
        )

    with st.expander("Case B — When payback hid the better project"):
        st.markdown(
            """
**Situation:** Two projects: Project A paid back in 2 years then stopped; Project B paid back in 4 years
but then generated strong cash for another 10.

**What went wrong:** A payback-only rule picked Project A — yet Project B had a far higher NPV because of
all the cash **after** its payback point, which payback completely ignored.

**The fix:** NPV revealed B as the value-creating choice.

**Lesson:** Payback is blind to everything after break-even — never let it override NPV.
"""
        )

    with st.expander("Case C — Discounted payback caught a bad deal"):
        st.markdown(
            """
**Situation:** A project's simple payback of 4.5 years looked acceptable against a 5-year rule.

**What discounting revealed:** At the company's 12% cost of capital, the **discounted** payback stretched
beyond the asset's life — the project never truly recovered its cost in economic terms, and NPV was negative.

**Why it matters:** Simple payback flattered a value-destroying project; discounting exposed it.

**Lesson:** Prefer discounted payback over simple payback — it respects the time value of money and
catches marginal deals.
"""
        )

    st.info(
        "🔗 **Pattern:** Payback is a useful *risk and liquidity* lens and a great screening tool — but it "
        "measures time, not value. Pair it with NPV/IRR, and prefer the discounted version."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_42"):
        q1 = st.radio(
            "**1.** The payback period measures:",
            [
                "The total value a project creates",
                "The time taken to recover the initial investment",
                "The project's internal rate of return",
                "The project's tax charge",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** For even annual cash flows, simple payback equals:",
            [
                "Annual cash flow ÷ Initial investment",
                "Initial investment ÷ Annual cash flow",
                "Initial investment × discount rate",
                "NPV ÷ IRR",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Compared with simple payback, discounted payback is:",
            [
                "Always shorter",
                "Always longer (because discounted cash flows are smaller)",
                "Always exactly the same",
                "Unrelated to the discount rate",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A key limitation shared by BOTH payback methods is that they:",
            [
                "Are too hard to calculate",
                "Ignore all cash flows after the payback point and don't measure value",
                "Require an IRR first",
                "Always reject profitable projects",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The best way to use payback is:",
            [
                "As the sole decision rule, ignoring NPV",
                "As a supplementary risk/liquidity screen alongside NPV/IRR",
                "To replace the discount rate",
                "To calculate depreciation",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The time taken to recover the initial investment"),
            "2": (q2, "Initial investment ÷ Annual cash flow"),
            "3": (q3, "Always longer (because discounted cash flows are smaller)"),
            "4": (q4, "Ignore all cash flows after the payback point and don't measure value"),
            "5": (q5, "As a supplementary risk/liquidity screen alongside NPV/IRR"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered payback analysis! On to Module 4.3 (Capex Business Case Model). 🎉")
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
    f"Applied Financial Models · Module 4.2 Payback & Discounted Payback · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
