"""
================================================================================
APPLIED FINANCIAL MODELS
Module 4.3 — CAPEX BUSINESS CASE MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to build a full Capex investment business case: benefits (revenue/savings),
operating costs, depreciation, tax, working capital, terminal value, and the
resulting free cash flow, NPV, IRR and payback.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a full board-ready Capex model)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_4_3_Capex_Business_Case_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="4.3 Capex Business Case Model — Applied Financial Models",
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
    r = rate_pct / 100
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cashflows))


def irr(cashflows, lo=-0.99, hi=10.0, tol=1e-7, max_iter=300):
    def f(r):
        return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cashflows))
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        fmid = f(mid)
        if abs(fmid) < tol:
            return mid * 100
        if flo * fmid < 0:
            hi, fhi = mid, fmid
        else:
            lo, flo = mid, fmid
    return (lo + hi) / 2 * 100


def payback(cashflows):
    cum = 0.0
    for t, cf in enumerate(cashflows):
        prev = cum
        cum += cf
        if t > 0 and cum >= 0:
            return (t - 1) + (-prev / cf) if cf else float(t)
    return None


def build_capex_case(
    capex, life, annual_benefit, benefit_growth, opex, opex_growth,
    dep_years, tax_rate, wc_pct, discount_rate, terminal_pct,
):
    """
    Build a full Capex business case. Returns a per-year DataFrame + the FCF list.
    Free cash flow = (Benefit - Opex - Depreciation) * (1-tax) + Depreciation
                     - Capex(t0) - ΔWorking capital + Terminal value(final).
    """
    dep = capex / dep_years if dep_years > 0 else 0
    rows = []
    fcfs = [-float(capex)]  # t0 outflow

    # t0 row
    rows.append({
        "Year": 0, "Benefit": 0, "Opex": 0, "Depreciation": 0, "EBIT": 0,
        "Tax": 0, "NOPAT": 0, "Add back Dep": 0, "Capex": -capex,
        "Δ Working capital": 0, "Terminal value": 0, "Free cash flow": -float(capex),
    })

    benefit = annual_benefit
    op = opex
    prev_wc = 0.0
    for y in range(1, life + 1):
        if y > 1:
            benefit *= (1 + benefit_growth / 100)
            op *= (1 + opex_growth / 100)
        depreciation = dep if y <= dep_years else 0
        ebit = benefit - op - depreciation
        tax = max(ebit, 0) * tax_rate / 100
        nopat = ebit - tax
        # working capital tied to benefit level
        wc = benefit * wc_pct / 100
        d_wc = wc - prev_wc
        prev_wc = wc
        terminal = 0.0
        if y == life:
            terminal = benefit * terminal_pct / 100 + wc  # release WC + terminal proxy
        fcf = nopat + depreciation - d_wc + terminal
        fcfs.append(fcf)
        rows.append({
            "Year": y, "Benefit": benefit, "Opex": -op, "Depreciation": -depreciation,
            "EBIT": ebit, "Tax": -tax, "NOPAT": nopat, "Add back Dep": depreciation,
            "Capex": 0, "Δ Working capital": -d_wc, "Terminal value": terminal,
            "Free cash flow": fcf,
        })

    df = pd.DataFrame(rows)
    project_npv = npv(discount_rate, fcfs)
    project_irr = irr(fcfs)
    pb = payback(fcfs)
    return df, fcfs, project_npv, project_irr, pb


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 4 · Investment Appraisal & Capital Budgeting")
st.sidebar.markdown(
    """
**Module 4.3 — Capex Business Case Model**

🔴 *Advanced*

**You will learn to:**
- Build a full investment business case
- Model benefits, opex, depreciation & tax
- Include working capital & terminal value
- Reach a board-ready NPV / IRR / payback
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a complete, board-ready "
    "Capex business case and get an instant investment verdict."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏗️ 4.3 · Capex Business Case Model")
st.markdown(
    """
This is where investment appraisal becomes a **complete, board-ready business case**. Where 4.1 (NPV/IRR)
and 4.2 (payback) covered the *tools*, this module assembles them into a **full Capex model** — the kind
used to justify a major factory investment to senior management.

It brings together everything so far: benefits (extra revenue or cost savings), operating costs,
**depreciation**, **tax**, **working capital**, and a **terminal value** — all flowing into free cash
flow, then NPV, IRR and payback.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "4.3")
c2.metric("Part", "4 — Appraisal")
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

# ================================================================================
# TAB 1 — THEORY & CONCEPTS
# ================================================================================
with tabs[0]:
    st.subheader("Theory & Concepts")

    st.markdown(
        """
### From tools to a full business case
A Capex business case answers: *"If we invest this money, will the future cash flows create enough value
to justify it?"* — using **incremental free cash flow**: only the cash flows that change *because of* the
investment.
"""
    )
    st.latex(r"FCF = (\text{Benefit} - \text{Opex} - \text{Dep}) \times (1-\text{tax}) + \text{Dep} - \text{Capex} - \Delta\text{WC}")

    st.markdown("### The components of a Capex business case")
    comp = pd.DataFrame(
        {
            "Component": ["Capex (t0)", "Benefits", "Operating costs", "Depreciation",
                          "Tax", "Working capital", "Terminal value"],
            "What it is": [
                "The upfront investment (cash out today)",
                "Incremental revenue OR cost savings the project delivers",
                "Extra running costs the project incurs",
                "Non-cash charge that creates a tax shield",
                "Tax on incremental operating profit",
                "Cash tied up as the project scales (a use of cash)",
                "Residual value at the end of the forecast",
            ],
            "Cash effect": [
                "Large outflow at t0", "Inflow each year", "Outflow each year",
                "Non-cash (added back), but reduces tax", "Outflow",
                "Outflow when rising, released at the end", "Inflow in final year",
            ],
        }
    )
    st.table(comp)

    with st.expander("🔑 Concept 1 — Incremental cash flows only"):
        st.markdown(
            """
A business case must use **incremental** cash flows — the difference between *with* the project and
*without* it. Include:
- ✅ New revenue/savings, new costs, capex, incremental working capital, tax effects.

Exclude:
- ❌ **Sunk costs** (already spent — irrelevant), and unaffected overheads.

The golden test: *"Does this cash flow change because of the decision?"* If not, leave it out.
"""
        )

    with st.expander("🔑 Concept 2 — The depreciation tax shield"):
        st.markdown(
            """
Depreciation is **non-cash**, so it's added back in the cash flow — but it still matters because it
**reduces taxable profit**, saving tax:

$$\\text{Tax shield} = \\text{Depreciation} \\times \\text{Tax rate}$$

So a €600k annual depreciation at 30% tax saves €180k of tax each year. Capex-heavy projects get real
value from this shield — which is why we model depreciation explicitly even though it isn't cash.
"""
        )

    with st.expander("🔑 Concept 3 — Working capital in a business case"):
        st.markdown(
            """
Growth usually requires more working capital (receivables, inventory) — a **use of cash** as the project
scales. Model the *change* in working capital each year as a cash outflow, and typically **release** it
at the end of the project (it comes back as a cash inflow). Forgetting working capital is a common way to
overstate a project's returns.
"""
        )

    with st.expander("🔑 Concept 4 — Terminal value & project life"):
        st.markdown(
            """
At the end of the explicit forecast, the asset may still have value — a **terminal (or residual)
value**: salvage/resale of equipment, or the ongoing value of continued cash flows. It's an inflow in
the final year. For long-life assets, a poorly-estimated terminal value can dominate the NPV, so treat it
carefully (as in the DCF, Module 3.1).
"""
        )

    with st.expander("🔑 Concept 5 — Presenting to the board"):
        st.markdown(
            """
A board-ready business case leads with the **decision metrics** — NPV, IRR, payback — then shows the
**key assumptions** and a **sensitivity** on the riskiest ones (benefit level, discount rate). Boards
approve investments on a clear, stress-tested story, not a wall of numbers. (Sensitivity is covered fully
in Part 5.)
"""
        )

    st.success(
        "**Takeaway:** A Capex business case assembles incremental benefits, costs, depreciation, tax, "
        "working capital and terminal value into free cash flow — then NPV/IRR/payback deliver the verdict. "
        "Use incremental cash flows, respect the tax shield, and don't forget working capital."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — A full automation business case")
    st.markdown("A **€6,000,000** automation project delivering **€1,800,000/yr** of cost savings over 8 years.")

    st.markdown("#### Assumptions")
    st.markdown(
        """
| Assumption | Value |
|---|---|
| Capex (t0) | €6,000,000 |
| Annual savings (benefit) | €1,800,000 |
| Extra operating cost | €300,000 / yr |
| Project life | 8 years |
| Depreciation | Straight-line over 8 yrs = €750,000/yr |
| Tax rate | 30% |
| Discount rate (WACC) | 10% |
"""
    )

    st.markdown("#### One representative year (steady state)")
    st.markdown(
        """
| Line | € |
|---|---|
| Benefit (savings) | 1,800,000 |
| − Operating cost | (300,000) |
| − Depreciation | (750,000) |
| = EBIT | 750,000 |
| − Tax @30% | (225,000) |
| = NOPAT | 525,000 |
| + Add back depreciation | 750,000 |
| **= Free cash flow** | **€1,275,000** |
"""
    )

    st.markdown("#### The verdict")
    st.markdown(
        """
Discounting €1,275,000/yr for 8 years at 10% (annuity factor 5.335):
$$PV = 1{,}275{,}000 \\times 5.335 = €6{,}802{,}000$$
$$NPV = -6{,}000{,}000 + 6{,}802{,}000 = \\mathbf{+€802{,}000}$$
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Annual free cash flow", "€1,275,000")
    e2.metric("NPV @ 10%", "+€802,000", "Accept ✅")
    e3.metric("IRR", "≈ 13.6%", "> 10% hurdle")

    st.info(
        "**Insight:** Note the **depreciation tax shield** at work — depreciation isn't cash, but by "
        "cutting taxable profit it saves €225k of tax that boosts free cash flow to €1,275k. The project "
        "delivers a **positive NPV (+€802k)** and an **IRR (~13.6%) comfortably above the 10% hurdle**. "
        "**Recommendation: approve** — subject to sensitivity-testing the savings assumption (Part 5)."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Build a Board-Ready Capex Business Case")
    st.markdown(
        "Set every assumption and get a complete free-cash-flow model with NPV, IRR, payback and an "
        "investment verdict — the kind you'd take to a board."
    )

    left, right = st.columns([0.32, 0.68])

    with left:
        st.markdown("##### 💸 Investment")
        capex = st.number_input("Capex at t=0 (€)", 100_000, 200_000_000, 6_000_000, 100_000)
        life = st.slider("Project life (years)", 1, 20, 8, 1)
        dep_years = st.slider("Depreciation period (years)", 1, 20, 8, 1)

        st.markdown("##### 📈 Benefits & costs")
        benefit = st.number_input("Annual benefit / savings (€)", 0, 100_000_000, 1_800_000, 50_000)
        benefit_growth = st.slider("Benefit growth (%)", -10.0, 15.0, 0.0, 0.5)
        opex = st.number_input("Annual operating cost (€)", 0, 50_000_000, 300_000, 25_000)
        opex_growth = st.slider("Opex growth (%)", -10.0, 15.0, 0.0, 0.5)

        st.markdown("##### ⚙️ Financial assumptions")
        tax_rate = st.slider("Tax rate (%)", 0.0, 45.0, 30.0, 1.0)
        wc_pct = st.slider("Working capital (% of benefit)", 0.0, 40.0, 0.0, 1.0)
        terminal_pct = st.slider("Terminal value (% of final benefit)", 0.0, 200.0, 0.0, 5.0)
        discount_rate = st.slider("Discount rate / hurdle (%)", 1.0, 25.0, 10.0, 0.5)

    with right:
        df, fcfs, project_npv, project_irr, pb = build_capex_case(
            capex, life, benefit, benefit_growth, opex, opex_growth,
            dep_years, tax_rate, wc_pct, discount_rate, terminal_pct,
        )

        k1, k2, k3 = st.columns(3)
        k1.metric("NPV", money(project_npv),
                  "Accept ✅" if project_npv > 0 else "Reject ❌",
                  delta_color="normal" if project_npv > 0 else "inverse")
        k2.metric("IRR", f"{project_irr:.1f}%" if project_irr is not None else "n/a",
                  (f"> {discount_rate:.1f}% ✅" if (project_irr is not None and project_irr > discount_rate)
                   else f"< {discount_rate:.1f}% ❌" if project_irr is not None else None),
                  delta_color="normal" if (project_irr is not None and project_irr > discount_rate) else "inverse")
        k3.metric("Payback", f"{pb:.1f} yrs" if pb is not None else "Never")

        if project_npv > 0 and project_irr is not None and project_irr > discount_rate:
            st.success(
                f"✅ **APPROVE.** NPV +{money(project_npv)} and IRR {project_irr:.1f}% beats the "
                f"{discount_rate:.1f}% hurdle. The business case creates value."
            )
        elif project_npv > 0:
            st.success(f"✅ **APPROVE.** Positive NPV of {money(project_npv)} — the case creates value.")
        else:
            st.error(
                f"❌ **REJECT.** NPV is {money(project_npv)} at a {discount_rate:.1f}% hurdle — the case "
                "destroys value as configured."
            )

        # FCF summary table
        show = df.copy()
        for col in ["Benefit", "Opex", "Depreciation", "EBIT", "Tax", "NOPAT",
                    "Add back Dep", "Capex", "Δ Working capital", "Terminal value", "Free cash flow"]:
            show[col] = show[col].map(money)
        st.markdown("##### 📄 Free Cash Flow Build-Up")
        st.dataframe(
            show[["Year", "Benefit", "Opex", "Depreciation", "EBIT", "Tax",
                  "NOPAT", "Add back Dep", "Capex", "Δ Working capital", "Terminal value", "Free cash flow"]],
            use_container_width=True, hide_index=True,
        )

        st.markdown("##### 📈 Free cash flow by year")
        chart = df.set_index("Year")[["Free cash flow"]]
        st.bar_chart(chart)

        # mini sensitivity on discount rate
        st.markdown("##### 🎯 NPV sensitivity to discount rate")
        rates = [discount_rate - 4 + i for i in range(9) if (discount_rate - 4 + i) >= 1]
        sens = pd.DataFrame({"NPV (€)": [npv(r, fcfs) for r in rates]},
                            index=[f"{r:.0f}%" for r in rates])
        st.line_chart(sens)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Tax shield:** Set depreciation period to match project life, then to half. Watch the tax shield timing
   change the NPV.
2. **Working capital drag:** Set working capital to 20% of benefit. See how much it reduces the NPV.
"""
        )
    with e2:
        st.markdown(
            """
3. **Terminal boost:** Add a terminal value of 100% of final benefit (equipment resale). How much does NPV rise?
4. **Break-even benefit:** Lower the annual benefit until NPV hits €0 — that's your minimum required benefit.
"""
        )

    st.download_button(
        "⬇️ Download this business case (CSV)",
        df.to_csv(index=False).encode("utf-8"),
        "capex_business_case.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The automation / productivity investment", expanded=True):
        st.markdown(
            """
**Situation:** A factory proposes a major automation investment to cut manpower cost and improve
productivity (a transformation-style project).

**How the business case works:** Model the **savings** as the benefit, the new running costs as opex,
**depreciation** of the equipment (with its tax shield), and the upfront capex. The resulting NPV/IRR tell
the board whether the productivity gains justify the spend.

**Why it matters:** Big transformation projects live or die on a rigorous, discounted business case — not
on headline savings figures.

**Lesson:** Frame cost-saving projects exactly like revenue projects — the savings *are* the benefit.
"""
        )

    with st.expander("Case B — The depreciation tax shield that swung the case"):
        st.markdown(
            """
**Situation:** A marginal project looked like it barely cleared the hurdle on pre-tax cash alone.

**What the model revealed:** Modelling **depreciation** properly showed a meaningful annual **tax shield**
(depreciation × tax rate) that boosted after-tax cash flow enough to make the NPV comfortably positive.

**Why it matters:** Ignoring the tax shield understates a capex-heavy project's true returns.

**Lesson:** Always model depreciation and tax explicitly — the shield can be the difference between
approve and reject.
"""
        )

    with st.expander("Case C — Working capital that quietly killed the returns"):
        st.markdown(
            """
**Situation:** A growth project's headline NPV looked strong, but the plan ignored the extra inventory and
receivables growth would require.

**What the model revealed:** Adding the **incremental working capital** as a cash outflow each year cut the
NPV sharply — the project consumed cash faster than the simple model implied.

**Why it matters:** Working capital is a real, often large, cash cost of growth that a naïve business case
omits.

**Lesson:** Never leave working capital out of a growth business case — it can turn a 'yes' into a 'no'.
"""
        )

    st.info(
        "🔗 **Pattern:** A credible Capex business case captures *all* incremental cash effects — benefits, "
        "costs, tax shield, working capital and terminal value — then lets NPV/IRR/payback deliver a "
        "stress-tested verdict the board can trust."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_43"):
        q1 = st.radio(
            "**1.** A Capex business case should be built using:",
            [
                "Total company cash flows",
                "Incremental cash flows — those that change because of the investment",
                "Only accounting profit",
                "Sunk costs already spent",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The depreciation tax shield equals:",
            [
                "Depreciation × (1 − tax rate)",
                "Depreciation × tax rate",
                "Capex ÷ tax rate",
                "EBIT × tax rate",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** In a free cash flow build-up, depreciation is:",
            [
                "Ignored entirely",
                "Subtracted to get EBIT (for tax), then added back because it is non-cash",
                "Treated as a cash outflow",
                "Added to capex",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** An increase in working capital as a project grows is:",
            [
                "A source of cash (inflow)",
                "A use of cash (outflow) that reduces free cash flow",
                "Irrelevant to the business case",
                "The same as depreciation",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Which cost should be EXCLUDED from a business case?",
            [
                "Incremental operating costs",
                "The upfront capex",
                "A sunk cost already spent regardless of the decision",
                "Incremental working capital",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Incremental cash flows — those that change because of the investment"),
            "2": (q2, "Depreciation × tax rate"),
            "3": (q3, "Subtracted to get EBIT (for tax), then added back because it is non-cash"),
            "4": (q4, "A use of cash (outflow) that reduces free cash flow"),
            "5": (q5, "A sunk cost already spent regardless of the decision"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you can build a full Capex business case! On to Module 4.4 (Cost-Benefit & Cost-Savings). 🎉")
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
    f"Applied Financial Models · Module 4.3 Capex Business Case Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
