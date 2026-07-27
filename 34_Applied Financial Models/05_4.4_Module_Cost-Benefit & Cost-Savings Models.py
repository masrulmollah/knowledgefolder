"""
================================================================================
APPLIED FINANCIAL MODELS
Module 4.4 — COST-BENEFIT & COST-SAVINGS MODELS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to appraise efficiency / automation projects using cost-benefit and
cost-savings analysis: quantifying benefits, incremental "before vs after"
analysis, and the benefit-cost ratio.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a before-vs-after cost-savings engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_4_4_Cost_Benefit_and_Cost_Savings_Models.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="4.4 Cost-Benefit & Cost-Savings Models — Applied Financial Models",
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
            hi = mid
        else:
            lo, flo = mid, fmid
    return (lo + hi) / 2 * 100


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 4 · Investment Appraisal & Capital Budgeting")
st.sidebar.markdown(
    """
**Module 4.4 — Cost-Benefit & Cost-Savings Models**

🟡 *Intermediate*

**You will learn to:**
- Quantify benefits of efficiency projects
- Do "before vs. after" incremental analysis
- Calculate the benefit-cost ratio (BCR)
- Appraise automation & savings initiatives
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to model a before-vs-after "
    "cost-savings case and see the payback and BCR."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏗️ 4.4 · Cost-Benefit & Cost-Savings Models")
st.markdown(
    """
Not every investment generates new revenue — many create value by **saving cost** or **improving
efficiency**: automation, process improvement, energy reduction, digitalisation. **Cost-benefit analysis**
appraises these by comparing the **total benefits** (often cost savings) against the **total costs** of the
initiative.

The core technique is **incremental "before vs. after" analysis**: measure the *change* the project
creates, not the absolute numbers. This module shows how to quantify savings credibly and turn them into
a sound investment decision.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "4.4")
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
### Cost-benefit analysis (CBA)
CBA weighs everything a project **gives** against everything it **costs**. For efficiency projects, the
main "benefit" is usually **cost savings** — money you no longer spend. A saving is worth exactly as much
as an equivalent amount of new profit.
"""
    )
    st.latex(r"\text{Net Benefit} = \text{Total Benefits (savings)} - \text{Total Costs}")

    st.markdown("### Incremental 'before vs. after' analysis")
    st.markdown(
        """
The heart of a cost-savings model is comparing two states:
"""
    )
    ba = pd.DataFrame(
        {
            "": ["Labour", "Energy", "Waste", "Maintenance", "Total annual cost"],
            "BEFORE (current)": ["€800k", "€300k", "€150k", "€100k", "€1,350k"],
            "AFTER (with project)": ["€500k", "€250k", "€60k", "€120k", "€930k"],
            "Annual saving": ["€300k", "€50k", "€90k", "(€20k)", "€420k"],
        }
    )
    st.table(ba)
    st.caption("The **annual saving (€420k)** is the incremental benefit — note maintenance can *rise*, "
               "which must be captured honestly.")

    st.markdown("### The benefit-cost ratio (BCR)")
    st.latex(r"BCR = \frac{\text{PV of Benefits}}{\text{PV of Costs}}")
    st.markdown(
        """
- **BCR > 1** → benefits exceed costs → worthwhile.
- **BCR = 1** → break-even.
- **BCR < 1** → costs exceed benefits → reject.

BCR is useful for **ranking** projects competing for a limited budget (value per euro spent).
"""
    )

    with st.expander("🔑 Concept 1 — A saving is as good as a profit"):
        st.markdown(
            """
€1 of cost saved flows to the bottom line exactly like €1 of new gross profit — often *better*, because
savings are usually **more certain** than new sales. This is why cost-savings projects (automation,
efficiency) are frequently the most attractive investments a company can make.
"""
        )

    with st.expander("🔑 Concept 2 — Count ALL incremental effects (including negatives)"):
        st.markdown(
            """
Honest CBA captures **every** change, not just the headline saving:
- ➕ Labour, energy, waste, scrap, rework reductions.
- ➖ New costs: maintenance, software licences, training, extra power for new equipment.
- ➕ Intangibles where quantifiable: quality, safety, throughput, lead-time.

Ignoring the *negative* increments (a common temptation) overstates the case. Net them all.
"""
        )

    with st.expander("🔑 Concept 3 — Quantifying 'soft' benefits"):
        st.markdown(
            """
Some benefits are real but hard to measure (better quality, morale, flexibility). Best practice:
- **Quantify** what you credibly can (e.g. fewer defects → €X of avoided scrap).
- **List** the rest as qualitative support, but don't inflate the numbers with unsupported estimates.

Boards trust a conservative, well-evidenced case far more than an optimistic one padded with soft benefits.
"""
        )

    with st.expander("🔑 Concept 4 — CBA still uses NPV"):
        st.markdown(
            """
A cost-savings project is appraised **exactly like any investment** (Modules 4.1–4.3): the annual net
savings are the cash inflows, discounted against the upfront cost to get **NPV, IRR and payback**. CBA is
not a separate method — it's about correctly **quantifying the savings** that then feed the standard
appraisal.
"""
        )

    st.success(
        "**Takeaway:** Cost-benefit analysis appraises efficiency/automation projects by comparing benefits "
        "(mostly cost savings) with costs, using incremental 'before vs. after' analysis. A saving is as "
        "valuable as a profit — just be honest about the negative increments and feed the net savings into NPV."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Appraising an efficiency project")
    st.markdown("A **€1,200,000** process-improvement project. Let's quantify the savings and appraise it.")

    st.markdown("#### Step 1 — Before vs. after (annual costs)")
    st.markdown(
        """
| Cost line | Before | After | Annual saving |
|---|---|---|---|
| Labour | €800,000 | €500,000 | €300,000 |
| Energy | €300,000 | €250,000 | €50,000 |
| Waste / scrap | €150,000 | €60,000 | €90,000 |
| Maintenance (rises) | €100,000 | €120,000 | (€20,000) |
| **Total** | **€1,350,000** | **€930,000** | **€420,000** |
"""
    )

    st.markdown("#### Step 2 — Net annual benefit")
    st.markdown(
        """
Net annual saving = **€420,000** (note the €20k maintenance *increase* is correctly netted off).
"""
    )

    st.markdown("#### Step 3 — Appraise like any investment (5-year life, 10% discount)")
    st.markdown(
        """
$$PV \\text{ of savings} = 420{,}000 \\times \\frac{1-(1.10)^{-5}}{0.10} = 420{,}000 \\times 3.7908 = €1{,}592{,}100$$
$$NPV = -1{,}200{,}000 + 1{,}592{,}100 = \\mathbf{+€392{,}100}$$
"""
    )

    e1, e2, e3, e4 = st.columns(4)
    e1.metric("Net annual saving", "€420,000")
    e2.metric("NPV @ 10%", "+€392,100", "Accept ✅")
    e3.metric("Payback", "≈ 2.9 yrs", help="€1.2m ÷ €420k")
    e4.metric("BCR", "1.33", help="€1,592k ÷ €1,200k")

    st.info(
        "**Insight:** The project saves **€420k/year** net, giving a **positive NPV (+€392k)**, a fast "
        "**~2.9-year payback**, and a **benefit-cost ratio of 1.33** (€1.33 of value per €1 spent). Notice "
        "we honestly netted off the €20k rise in maintenance — inflating the case by ignoring it would have "
        "overstated the return. **Recommendation: approve** — strong, low-risk savings."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Before-vs-After Cost-Savings Engine")
    st.markdown(
        "Enter current ('before') and projected ('after') annual costs for each line. The model computes "
        "the net annual saving, then appraises the investment (NPV, IRR, payback, BCR)."
    )

    left, right = st.columns([0.40, 0.60])

    with left:
        st.markdown("##### 💰 Investment & appraisal settings")
        investment = st.number_input("Upfront cost (€)", 10_000, 100_000_000, 1_200_000, 50_000)
        life = st.slider("Benefit life (years)", 1, 20, 5, 1)
        discount = st.slider("Discount rate (%)", 0.0, 25.0, 10.0, 0.5)
        savings_growth = st.slider("Annual growth in savings (%)", -10.0, 15.0, 0.0, 0.5)

        st.markdown("##### 📊 Annual costs — Before vs. After")
        st.caption("Enter current cost and expected cost with the project.")
        lines = ["Labour", "Energy", "Waste / scrap", "Maintenance", "Other"]
        defaults_before = [800_000, 300_000, 150_000, 100_000, 0]
        defaults_after = [500_000, 250_000, 60_000, 120_000, 0]
        before_vals, after_vals = [], []
        for i, ln in enumerate(lines):
            cc1, cc2 = st.columns(2)
            b = cc1.number_input(f"{ln} — before", 0, 50_000_000, defaults_before[i], 10_000, key=f"b_{i}")
            a = cc2.number_input(f"{ln} — after", 0, 50_000_000, defaults_after[i], 10_000, key=f"a_{i}")
            before_vals.append(b)
            after_vals.append(a)

    with right:
        savings = [b - a for b, a in zip(before_vals, after_vals)]
        total_before = sum(before_vals)
        total_after = sum(after_vals)
        net_saving = total_before - total_after

        # build cash flows
        cfs = [-float(investment)]
        s = net_saving
        for y in range(1, life + 1):
            if y > 1:
                s *= (1 + savings_growth / 100)
            cfs.append(s)

        project_npv = npv(discount, cfs)
        project_irr = irr(cfs)
        pv_benefits = project_npv + investment  # since NPV = -inv + PV(benefits)
        bcr = pv_benefits / investment if investment else 0
        pb = investment / net_saving if net_saving > 0 else None

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Net annual saving", money(net_saving))
        k2.metric("NPV", money(project_npv),
                  "Accept ✅" if project_npv > 0 else "Reject ❌",
                  delta_color="normal" if project_npv > 0 else "inverse")
        k3.metric("Payback", f"{pb:.1f} yrs" if pb else "Never")
        k4.metric("BCR", f"{bcr:.2f}", help="PV of benefits ÷ cost")

        # before/after table
        tbl = pd.DataFrame(
            {
                "Cost line": lines + ["TOTAL"],
                "Before": before_vals + [total_before],
                "After": after_vals + [total_after],
                "Annual saving": savings + [net_saving],
            }
        )
        for c in ["Before", "After", "Annual saving"]:
            tbl[c] = tbl[c].map(money)
        st.markdown("##### 📄 Before vs. After")
        st.dataframe(tbl, use_container_width=True, hide_index=True)

        if net_saving <= 0:
            st.error(
                "❌ The 'after' costs are **not lower** than 'before' — there's no net saving, so the project "
                "destroys value. Re-examine the benefits."
            )
        elif project_npv > 0:
            st.success(
                f"✅ **APPROVE.** Net saving {money(net_saving)}/yr → NPV {money(project_npv)}, "
                f"BCR {bcr:.2f} (€{bcr:.2f} of value per €1 spent)."
                + (f" IRR {project_irr:.1f}%." if project_irr is not None else "")
            )
        else:
            st.warning(
                f"⚠️ Positive savings, but at a {discount:.1f}% discount over {life} years the NPV is "
                f"{money(project_npv)} — the upfront cost is too high for the savings. Reject as configured."
            )

        # savings composition
        pos = {ln: s for ln, s in zip(lines, savings) if s != 0}
        if pos:
            st.markdown("##### 📊 Saving by cost line")
            st.bar_chart(pd.DataFrame({"Annual saving (€)": list(pos.values())}, index=list(pos.keys())))

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Honest negatives:** Raise 'Maintenance — after' above its 'before'. Watch the net saving (and NPV) fall.
2. **Break-even cost:** Raise the upfront cost until NPV hits €0 — that's the most you should pay.
"""
        )
    with e2:
        st.markdown(
            """
3. **BCR ranking:** Aim for a BCR above 1.5 — a strong value-per-euro project worth prioritising.
4. **Discount bite:** Push the discount rate to 20%. Does the fast payback still translate into positive NPV?
"""
        )

    st.download_button(
        "⬇️ Download this cost-benefit analysis (CSV)",
        tbl.to_csv(index=False).encode("utf-8"),
        "cost_benefit_analysis.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The automation savings case", expanded=True):
        st.markdown(
            """
**Situation:** A factory evaluates automating a manual packing line to cut labour cost.

**How the cost-savings model works:** A **before vs. after** comparison quantifies the labour reduction
(the main saving), nets off new maintenance and power costs, and appraises the net annual saving against
the equipment cost via NPV/payback.

**Why it matters:** Automation cases are pure cost-savings investments — the saving *is* the return, and
it's usually more certain than a revenue forecast.

**Lesson:** Treat cost savings as the benefit and appraise automation exactly like any Capex project.
"""
        )

    with st.expander("Case B — The case that ignored the negatives"):
        st.markdown(
            """
**Situation:** A digitalisation proposal claimed €500k of annual savings and looked like an easy yes.

**What was missing:** It ignored new **software licences, training, and support costs** of ~€150k a year.
The *net* saving was only €350k — still positive, but materially lower, and it changed the payback and NPV.

**Why it matters:** Counting only the gross saving overstates the case; boards lose trust when hidden
costs surface later.

**Lesson:** Always net off the new costs a project introduces — the *incremental* benefit is what counts.
"""
        )

    with st.expander("Case C — Ranking projects with the benefit-cost ratio"):
        st.markdown(
            """
**Situation:** A company had a limited capital budget and five worthwhile efficiency projects competing
for funding.

**How BCR helped:** Ranking by **benefit-cost ratio** (value per euro spent) let management fund the
highest-BCR projects first, maximising total value from the constrained budget — better than ranking by
raw NPV when capital is scarce.

**Why it matters:** With limited capital, *efficiency of spend* (BCR) can matter more than absolute NPV.

**Lesson:** Use BCR to prioritise when the budget — not the ideas — is the binding constraint.
"""
        )

    st.info(
        "🔗 **Pattern:** Cost-benefit analysis is about quantifying savings **honestly** — before vs. after, "
        "net of new costs — then appraising with NPV/payback/BCR. Savings are often the safest, highest-"
        "return investments a company can make."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_44"):
        q1 = st.radio(
            "**1.** In a cost-savings project, the main 'benefit' is usually:",
            [
                "New revenue from customers",
                "The reduction in costs (money no longer spent)",
                "An increase in depreciation",
                "A higher tax charge",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** 'Before vs. after' (incremental) analysis means:",
            [
                "Comparing this year to last year's accounts",
                "Measuring the change in costs the project causes, not the absolute totals",
                "Only looking at costs after the project",
                "Ignoring the current situation",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** If a project introduces new maintenance costs, you should:",
            [
                "Ignore them — only savings matter",
                "Net them off against the savings to get the true incremental benefit",
                "Add them to the savings",
                "Treat them as revenue",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** The benefit-cost ratio (BCR) is:",
            [
                "PV of costs ÷ PV of benefits",
                "PV of benefits ÷ PV of costs",
                "NPV × IRR",
                "Payback ÷ project life",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** A €1 cost saving is generally:",
            [
                "Worth less than €1 of new profit",
                "Worth about the same as €1 of new profit (often more certain)",
                "Irrelevant to valuation",
                "Only relevant for tax",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The reduction in costs (money no longer spent)"),
            "2": (q2, "Measuring the change in costs the project causes, not the absolute totals"),
            "3": (q3, "Net them off against the savings to get the true incremental benefit"),
            "4": (q4, "PV of benefits ÷ PV of costs"),
            "5": (q5, "Worth about the same as €1 of new profit (often more certain)"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered cost-benefit analysis! On to Module 4.5 (Replacement & Make-vs-Buy). 🎉")
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
    f"Applied Financial Models · Module 4.4 Cost-Benefit & Cost-Savings Models · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
