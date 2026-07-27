"""
================================================================================
APPLIED FINANCIAL MODELS
Module 4.1 — NPV & IRR MODELS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to appraise an investment using Net Present Value (NPV) and Internal Rate of
Return (IRR): cash flow timelines, hurdle rates, and the accept/reject rules.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live NPV/IRR engine + NPV profile)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_4_1_NPV_and_IRR_Models.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="4.1 NPV & IRR Models — Applied Financial Models",
    layout="wide",
    page_icon="🏗️",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def npv(rate_pct, cashflows):
    """NPV where cashflows[0] is at t=0 (today)."""
    r = rate_pct / 100
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cashflows))


def irr(cashflows, lo=-0.99, hi=10.0, tol=1e-6, max_iter=200):
    """Find IRR via bisection. Returns None if no sign change / not found."""
    def f(r):
        return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cashflows))

    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        # try to widen / detect no root
        return None
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        fmid = f(mid)
        if abs(fmid) < tol:
            return mid * 100
        if flo * fmid < 0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid
    return (lo + hi) / 2 * 100


def payback_period(cashflows):
    """Simple payback: years until cumulative cash flow turns non-negative."""
    cum = 0.0
    for t, cf in enumerate(cashflows):
        prev = cum
        cum += cf
        if cum >= 0 and t > 0:
            # interpolate within the year
            if cf != 0:
                frac = -prev / cf
                return (t - 1) + frac
            return float(t)
    return None


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 4 · Investment Appraisal & Capital Budgeting")
st.sidebar.markdown(
    """
**Module 4.1 — NPV & IRR Models**

🟡 *Intermediate*

**You will learn to:**
- Build an investment cash flow timeline
- Calculate NPV and IRR
- Apply the hurdle rate & decision rules
- Compare projects and spot pitfalls
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for a live NPV/IRR engine — "
    "edit the cash flows and get an instant accept/reject decision."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏗️ 4.1 · NPV & IRR Models")
st.markdown(
    """
Should we make this investment? That's the question **investment appraisal** answers — and **NPV** and
**IRR** are its two most important tools. Both apply the time value of money (Module 0.4) to a project's
cash flows: **NPV** tells you how much *value* an investment creates in today's money, while **IRR** tells
you the *return* it earns.

This module — the heart of Capex decision-making — builds both from the ground up, with clear decision rules.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "4.1")
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
### Net Present Value (NPV)
NPV is the **sum of all a project's cash flows, discounted to today**. If it's positive, the project
creates value; if negative, it destroys value.
"""
    )
    st.latex(r"NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t} = -\text{Investment} + \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t}")
    st.markdown(
        """
- $CF_t$ = cash flow in year $t$ (the initial investment at $t=0$ is negative)
- $r$ = the **discount rate / hurdle rate** (often the WACC)
"""
    )

    st.markdown("### The decision rules")
    rules = pd.DataFrame(
        {
            "Measure": ["NPV", "IRR", "Payback"],
            "Accept if…": [
                "NPV > 0 (creates value)",
                "IRR > hurdle rate (return beats the required return)",
                "Payback within the target period",
            ],
            "Interpretation": [
                "Value added in today's money (€)",
                "The project's effective annual return (%)",
                "How quickly the initial outlay is recovered",
            ],
        }
    )
    st.table(rules)

    with st.expander("🔑 Concept 1 — NPV: the gold standard"):
        st.markdown(
            """
NPV is the **theoretically correct** appraisal measure because it directly answers *"how much value does
this create?"* in absolute euros, using the time value of money.

- **NPV > 0** → accept (the return exceeds the hurdle rate → value created).
- **NPV < 0** → reject (destroys value).
- **NPV = 0** → indifferent (earns exactly the hurdle rate).

Because it's an absolute number, NPV correctly reflects the *scale* of value created — a key advantage
over IRR.
"""
        )

    with st.expander("🔑 Concept 2 — IRR: the return the project earns"):
        st.markdown(
            """
The **Internal Rate of Return** is the discount rate at which **NPV = 0** — i.e. the project's own
effective return.

$$0 = \\sum_{t=0}^{n} \\frac{CF_t}{(1+IRR)^t}$$

- **Accept if IRR > hurdle rate** (the return beats what you require).
- Intuitive for managers ("this earns 18%"), but has pitfalls (below).
"""
        )

    with st.expander("🔑 Concept 3 — The hurdle rate"):
        st.markdown(
            """
The **hurdle rate** is the minimum acceptable return — the discount rate in the NPV, and the benchmark
for IRR. It usually reflects the **WACC** (Module 3.1), sometimes plus a risk margin for uncertain projects.

A higher hurdle rate makes projects harder to justify (future cash discounted more heavily → lower NPV).
Setting it correctly is critical: too low and you accept value-destroying projects; too high and you
reject good ones.
"""
        )

    with st.expander("🔑 Concept 4 — NPV vs. IRR (when they disagree)"):
        st.markdown(
            """
Usually NPV and IRR agree, but they can conflict:
- **Scale:** IRR ignores project size. A small project can have a high IRR but small NPV; a large project
  with a lower IRR may create far more value. **When they conflict, follow NPV.**
- **Multiple IRRs:** projects with unconventional cash flows (sign changes) can have several IRRs — NPV
  stays reliable.
- **Reinvestment assumption:** IRR implicitly assumes cash is reinvested at the IRR (often unrealistic);
  NPV assumes reinvestment at the hurdle rate (more realistic).

**Rule of thumb:** when in doubt, trust NPV.
"""
        )

    with st.expander("🔑 Concept 5 — Payback (quick but flawed)"):
        st.markdown(
            """
**Payback** = how long until the initial investment is recovered. It's simple and popular for a quick
liquidity read, but it **ignores the time value of money** and **anything after the payback point**. Use
it only as a supplement to NPV/IRR, never as the primary decision rule. (Discounted payback fixes the
first flaw — see Module 4.2.)
"""
        )

    st.success(
        "**Takeaway:** NPV measures value created (€) and is the gold standard; IRR measures the return (%) "
        "and is intuitive but has pitfalls. Accept when NPV > 0 / IRR > hurdle rate — and when they "
        "disagree, follow NPV."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Appraising a €6m automation project")
    st.markdown("A factory invests **€6,000,000** today for cash savings over 8 years. Hurdle rate **10%**.")

    st.markdown("#### Step 1 — Lay out the cash flow timeline")
    st.markdown(
        """
| Year | Cash flow |
|---|---|
| 0 (today) | −€6,000,000 (investment) |
| 1–8 | +€1,200,000 per year (savings) |
"""
    )

    st.markdown("#### Step 2 — Discount each year at 10% and sum")
    st.markdown(
        """
The present value of €1,200,000 per year for 8 years at 10% (an annuity):

$$PV = 1{,}200{,}000 \\times \\frac{1 - (1.10)^{-8}}{0.10} = 1{,}200{,}000 \\times 5.3349 = €6{,}401{,}900$$

$$NPV = -6{,}000{,}000 + 6{,}401{,}900 = \\mathbf{+€401{,}900}$$
"""
    )

    st.markdown("#### Step 3 — Calculate IRR & payback")
    st.markdown(
        """
- **IRR** ≈ **11.8%** (the rate where NPV = 0) — above the 10% hurdle.
- **Simple payback** = €6.0m ÷ €1.2m = **5.0 years**.
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("NPV @ 10%", "+€401,900", "Accept ✅")
    e2.metric("IRR", "11.8%", "> 10% hurdle")
    e3.metric("Payback", "5.0 years")

    st.info(
        "**Insight & recommendation:** The project has a **positive NPV (+€402k)** and an **IRR (11.8%) "
        "above the 10% hurdle** — both say *accept*. It creates ~€402k of value in today's money. The 5-year "
        "payback is reasonable for an 8-year-life asset. **Recommendation: proceed**, but stress-test the "
        "savings assumption (see the sensitivity work in Part 5)."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Live NPV / IRR Engine")
    st.markdown(
        "Set the investment, annual cash flows and hurdle rate. The model computes NPV, IRR and payback, "
        "gives an accept/reject verdict, and plots the **NPV profile**."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        st.markdown("##### 💸 Investment & returns")
        investment = st.number_input("Initial investment at t=0 (€)", 10_000, 100_000_000, 6_000_000, 100_000)
        annual_cf = st.number_input("Annual cash inflow (€)", 0, 50_000_000, 1_200_000, 50_000)
        years = st.slider("Project life (years)", 1, 20, 8, 1)
        cf_growth = st.slider("Annual growth in cash flow (%)", -10.0, 15.0, 0.0, 0.5)
        hurdle = st.slider("Hurdle rate / discount rate (%)", 1.0, 25.0, 10.0, 0.5)
        terminal = st.number_input("Terminal / salvage value at end (€)", 0, 50_000_000, 0, 50_000)

    with right:
        # Build cash flow list
        cfs = [-float(investment)]
        cf = annual_cf
        for y in range(1, years + 1):
            if y > 1:
                cf *= (1 + cf_growth / 100)
            flow = cf
            if y == years:
                flow += terminal
            cfs.append(flow)

        project_npv = npv(hurdle, cfs)
        project_irr = irr(cfs)
        pb = payback_period(cfs)

        k1, k2, k3 = st.columns(3)
        k1.metric("NPV", money(project_npv),
                  "Accept ✅" if project_npv > 0 else "Reject ❌",
                  delta_color="normal" if project_npv > 0 else "inverse")
        k2.metric("IRR", f"{project_irr:.1f}%" if project_irr is not None else "n/a",
                  (f"> {hurdle:.1f}% ✅" if (project_irr is not None and project_irr > hurdle)
                   else f"< {hurdle:.1f}% ❌" if project_irr is not None else None),
                  delta_color="normal" if (project_irr is not None and project_irr > hurdle) else "inverse")
        k3.metric("Payback", f"{pb:.1f} yrs" if pb is not None else "Never")

        # Verdict
        if project_npv > 0:
            st.success(
                f"✅ **ACCEPT.** NPV is positive ({money(project_npv)}) and IRR "
                f"({project_irr:.1f}%) exceeds the {hurdle:.1f}% hurdle — the project creates value."
                if project_irr is not None else
                f"✅ **ACCEPT.** NPV is positive ({money(project_npv)}) — the project creates value."
            )
        else:
            st.error(
                f"❌ **REJECT.** NPV is negative ({money(project_npv)}) — at a {hurdle:.1f}% hurdle rate the "
                "project destroys value."
            )

        # Cash flow + discounting table
        rows = []
        for t, c in enumerate(cfs):
            df = 1 / ((1 + hurdle / 100) ** t)
            rows.append({"Year": t, "Cash flow": c, "Discount factor": df, "PV": c * df})
        cf_df = pd.DataFrame(rows)
        cf_df["Cumulative PV"] = cf_df["PV"].cumsum()
        disp = cf_df.copy()
        disp["Cash flow"] = disp["Cash flow"].map(money)
        disp["Discount factor"] = disp["Discount factor"].map(lambda v: f"{v:.4f}")
        disp["PV"] = disp["PV"].map(money)
        disp["Cumulative PV"] = disp["Cumulative PV"].map(money)
        st.markdown("##### 📄 Cash Flow & Discounting")
        st.dataframe(disp, use_container_width=True, hide_index=True)

        # NPV profile
        st.markdown("##### 📈 NPV Profile (NPV at different discount rates)")
        rates = list(range(1, 26))
        profile = pd.DataFrame(
            {"NPV (€)": [npv(r, cfs) for r in rates]},
            index=[f"{r}%" for r in rates],
        )
        st.line_chart(profile)
        st.caption(
            "The NPV profile crosses zero at the **IRR** — where the line hits the x-axis. "
            "To the left of the IRR the project is value-creating; to the right, value-destroying."
        )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Find the break-even hurdle:** Raise the hurdle rate until NPV hits €0 — that rate equals the IRR.
2. **Savings shortfall:** Cut the annual cash flow to €1,000,000. Does the project still clear the hurdle?
"""
        )
    with e2:
        st.markdown(
            """
3. **Salvage value:** Add a €1,000,000 terminal value. How much does NPV improve?
4. **Growth kicker:** Set cash-flow growth to 5%. Watch NPV and IRR rise as later years get bigger.
"""
        )

    st.download_button(
        "⬇️ Download this appraisal (CSV)",
        cf_df.to_csv(index=False).encode("utf-8"),
        "npv_irr_appraisal.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The Capex investment decision", expanded=True):
        st.markdown(
            """
**Situation:** A factory must decide whether to invest €6m in automation that will cut costs for years.

**How NPV/IRR help:** Rather than a naïve "€1.2m savings × 8 years = €9.6m, so yes", the appraisal
**discounts** those future savings. The NPV (+€402k) confirms real value creation, and the IRR (11.8%)
shows the return beats the 10% cost of capital.

**Why it matters:** Ignoring the time value of money overstates returns — discounting reveals the true,
much thinner, economic gain.

**Lesson:** Always appraise Capex with NPV/IRR, never with undiscounted totals.
"""
        )

    with st.expander("Case B — When NPV and IRR disagree (scale)"):
        st.markdown(
            """
**Situation:** Two mutually exclusive projects — a small one with a 30% IRR (NPV €50k) and a large one
with a 15% IRR (NPV €800k).

**What the analysis revealed:** IRR favours the small project, but the large project creates **16× more
value**. Since only one can be chosen, **NPV is the correct tie-breaker**.

**Why it matters:** Chasing the highest IRR can leave enormous value on the table when project sizes differ.

**Lesson:** For mutually exclusive projects, choose the higher **NPV**, not the higher IRR.
"""
        )

    with st.expander("Case C — Setting the right hurdle rate"):
        st.markdown(
            """
**Situation:** A company used a single 8% hurdle for all projects, regardless of risk.

**What went wrong:** Risky, uncertain projects were being accepted on the same bar as safe ones — some
later destroyed value because the hurdle didn't reflect their risk.

**The fix:** Use a **risk-adjusted hurdle rate** — the WACC as a base, plus a premium for riskier
projects.

**Why it matters:** The hurdle rate is the single biggest lever in an appraisal; a wrong rate leads to
systematically wrong decisions.

**Lesson:** Match the hurdle rate to project risk — one size does not fit all.
"""
        )

    st.info(
        "🔗 **Pattern:** NPV/IRR turn a gut-feel 'should we invest?' into a rigorous, discounted decision. "
        "NPV measures value, IRR measures return — and the hurdle rate ties both to the cost of capital."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_41"):
        q1 = st.radio(
            "**1.** Net Present Value (NPV) is:",
            [
                "The undiscounted sum of a project's cash flows",
                "The sum of a project's cash flows discounted to today at the hurdle rate",
                "The project's payback period",
                "Revenue minus costs in year 1",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** You should ACCEPT a project when:",
            [
                "NPV < 0",
                "NPV > 0 (and IRR > hurdle rate)",
                "Payback is longer than the project life",
                "IRR is below the hurdle rate",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The IRR is defined as the discount rate at which:",
            [
                "NPV is maximised",
                "NPV equals zero",
                "Payback equals one year",
                "Revenue equals costs",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** When NPV and IRR disagree for mutually exclusive projects, you should:",
            [
                "Always pick the higher IRR",
                "Follow NPV, because it correctly reflects the scale of value created",
                "Pick the shorter payback",
                "Reject both projects",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The main weakness of the simple payback method is that it:",
            [
                "Is too difficult to calculate",
                "Ignores the time value of money and cash flows after the payback point",
                "Always rejects good projects",
                "Requires an IRR first",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The sum of a project's cash flows discounted to today at the hurdle rate"),
            "2": (q2, "NPV > 0 (and IRR > hurdle rate)"),
            "3": (q3, "NPV equals zero"),
            "4": (q4, "Follow NPV, because it correctly reflects the scale of value created"),
            "5": (q5, "Ignores the time value of money and cash flows after the payback point"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered NPV & IRR! On to Module 4.2 (Payback & Discounted Payback). 🎉")
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
    f"Applied Financial Models · Module 4.1 NPV & IRR Models · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
