"""
================================================================================
APPLIED FINANCIAL MODELS
Module 4.5 — REPLACEMENT & MAKE-vs-BUY DECISIONS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to make replacement ("keep old vs. buy new") and make-vs-buy ("in-house vs.
outsource") decisions using incremental cash flows and opportunity cost.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a replacement analyzer + make-vs-buy comparator)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_4_5_Replacement_and_Make_vs_Buy.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="4.5 Replacement & Make-vs-Buy — Applied Financial Models",
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


def annuity_pv(payment, rate_pct, years):
    r = rate_pct / 100
    if r == 0:
        return payment * years
    return payment * (1 - (1 + r) ** (-years)) / r


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 4 · Investment Appraisal & Capital Budgeting")
st.sidebar.markdown(
    """
**Module 4.5 — Replacement & Make-vs-Buy**

🟡 *Intermediate*

**You will learn to:**
- Analyse "keep old vs. buy new" decisions
- Analyse "make in-house vs. outsource"
- Use incremental cash flows correctly
- Apply opportunity cost & ignore sunk costs
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for a replacement analyzer and "
    "a make-vs-buy comparator."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🏗️ 4.5 · Replacement & Make-vs-Buy Decisions")
st.markdown(
    """
Two of the most common real-world decisions are **replacement** ("should we keep the old machine or buy a
new one?") and **make-vs-buy** ("should we produce this in-house or outsource it?"). Both are appraised
with the same discipline: compare the alternatives using **incremental cash flows**, respect **opportunity
cost**, and **ignore sunk costs**.

This module — the finale of Part 4 — sharpens the incremental-analysis mindset that underpins every good
investment decision.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "4.5")
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
### The golden rule: think incrementally
Both decisions come down to the same question: *what cash flows are DIFFERENT between the two options?*
Value only the **differences** — the cash flows that change depending on which choice you make.
"""
    )
    st.latex(r"\text{Decide on: } \Delta CF = CF_{\text{Option A}} - CF_{\text{Option B}}")

    st.markdown("### Three cost concepts you must get right")
    concepts = pd.DataFrame(
        {
            "Concept": ["Sunk cost", "Opportunity cost", "Incremental cost"],
            "Definition": [
                "Money already spent — cannot be recovered",
                "The value of the next-best alternative given up",
                "The extra cost caused by choosing one option",
            ],
            "How to treat it": [
                "IGNORE — irrelevant to the decision",
                "INCLUDE — it's a real economic cost",
                "INCLUDE — this is the basis of the decision",
            ],
        }
    )
    st.table(concepts)

    with st.expander("🔑 Concept 1 — Replacement decisions (keep vs. replace)"):
        st.markdown(
            """
Compare the cash flows of **keeping the old asset** vs. **buying the new one**:
- **New machine:** purchase cost (out), *minus* proceeds from selling the old machine (in), plus running-
  cost savings and any productivity/quality benefits, plus differences in maintenance and depreciation
  tax shields.
- **The old machine's original cost is SUNK** — ignore it. What matters is its *current* resale value
  (an opportunity cost of keeping it) and the *future* running costs of each option.

Decision: replace if the NPV of the incremental savings exceeds the net cost of switching.
"""
        )

    with st.expander("🔑 Concept 2 — Make-vs-buy decisions (in-house vs. outsource)"):
        st.markdown(
            """
Compare the total relevant cost of **making** vs. **buying**:
- **Make (in-house):** direct materials + direct labour + *incremental* overhead + any capex needed.
- **Buy (outsource):** the supplier price × volume, plus any transition/quality/logistics costs.

Include **opportunity cost**: if making in-house ties up capacity that could earn money elsewhere, that
lost contribution is a real cost of "make". Exclude **unavoidable fixed overheads** that continue either way.
"""
        )

    with st.expander("🔑 Concept 3 — Opportunity cost (the cost of the road not taken)"):
        st.markdown(
            """
Opportunity cost is easy to forget because no cash changes hands — but it's real. Examples:
- Keeping the old machine means **forgoing its resale value** → that cash is an opportunity cost of "keep".
- Using in-house capacity to "make" means **forgoing** whatever else that capacity could produce/earn.

A decision that looks cheap can be expensive once opportunity costs are included.
"""
        )

    with st.expander("🔑 Concept 4 — Sunk costs: the trap"):
        st.markdown(
            """
"But we already spent €2m on the old line!" — irrelevant. **Sunk costs cannot be changed by any future
decision**, so they must be excluded. Including them leads to the *sunk-cost fallacy*: throwing good money
after bad to "justify" past spending. Only **future, incremental** cash flows matter.
"""
        )

    with st.expander("🔑 Concept 5 — Beyond the numbers (qualitative factors)"):
        st.markdown(
            """
Make-vs-buy and replacement decisions also carry **strategic** considerations the pure NPV may not
capture:
- **Quality & control** (in-house often gives more control).
- **Supplier reliability & dependency** (outsourcing creates reliance).
- **Confidentiality / IP**, flexibility, and speed.

Quantify what you can; flag the rest for the decision-makers alongside the financial answer.
"""
        )

    st.success(
        "**Takeaway:** Replacement and make-vs-buy decisions hinge on **incremental** cash flows. Include "
        "opportunity costs, ignore sunk costs, and layer in strategic factors. Choose the option with the "
        "lower cost (higher NPV) of the *differences*."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Examples")

    st.markdown("#### Example 1 — Replacement: keep the old machine or buy new?")
    st.markdown(
        """
| Item | Detail |
|---|---|
| New machine cost | €500,000 |
| Old machine resale value now | €80,000 |
| Annual running-cost saving (new vs. old) | €120,000 |
| Remaining life | 6 years |
| Discount rate | 10% |
"""
    )
    st.markdown(
        """
**Net cost to switch** = €500,000 − €80,000 (old resale) = **€420,000**

**PV of savings** = €120,000 × annuity factor(10%, 6yr = 4.3553) = **€522,600**

$$NPV_{\\text{replace}} = -420{,}000 + 522{,}600 = \\mathbf{+€102{,}600}$$

✅ **Replace** — the incremental savings outweigh the net cost of switching. (Note: the old machine's
*original* purchase price is **sunk** and correctly ignored; only its current resale value matters.)
"""
    )
    r1, r2, r3 = st.columns(3)
    r1.metric("Net cost to switch", "€420,000")
    r2.metric("PV of savings", "€522,600")
    r3.metric("NPV of replacing", "+€102,600", "Replace ✅")

    st.markdown("---")
    st.markdown("#### Example 2 — Make-vs-Buy: produce in-house or outsource?")
    st.markdown(
        """
Annual requirement: **100,000 units**.

| | Make (in-house) | Buy (outsource) |
|---|---|---|
| Direct materials | €4.00 / unit | — |
| Direct labour | €3.00 / unit | — |
| Incremental overhead | €1.00 / unit | — |
| Supplier price | — | €9.00 / unit |
| **Unit cost** | **€8.00** | **€9.00** |
| **Annual cost (×100k)** | **€800,000** | **€900,000** |
"""
    )
    st.markdown(
        """
On these numbers, **make** is €100,000/yr cheaper. **But** — if making in-house uses capacity that could
otherwise earn €150,000/yr of contribution, that **opportunity cost** flips the decision:

- Make (incl. opportunity cost): €800,000 + €150,000 = **€950,000**
- Buy: **€900,000** → now **buy** is €50,000 cheaper.
"""
    )
    m1, m2, m3 = st.columns(3)
    m1.metric("Make (direct)", "€800,000")
    m2.metric("Buy", "€900,000")
    m3.metric("Make + opportunity cost", "€950,000", "Buy wins", delta_color="inverse")

    st.info(
        "**Insight:** Example 2 shows why **opportunity cost is decisive**. On direct costs alone, making "
        "looks €100k cheaper — but once you account for the €150k of contribution the capacity could earn "
        "elsewhere, **outsourcing becomes the better economic choice.** The numbers that *change* the "
        "decision are the ones that matter."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Replacement Analyzer")
    st.markdown("Should you keep the old asset or buy a new one? Enter the incremental figures.")

    left, right = st.columns([0.38, 0.62])
    with left:
        new_cost = st.number_input("New machine cost (€)", 0, 50_000_000, 500_000, 25_000)
        old_resale = st.number_input("Old machine resale value now (€)", 0, 50_000_000, 80_000, 10_000)
        annual_saving = st.number_input("Annual running-cost saving (€)", 0, 10_000_000, 120_000, 10_000)
        rep_life = st.slider("Remaining life (years)", 1, 20, 6, 1)
        rep_rate = st.slider("Discount rate (%)", 0.0, 25.0, 10.0, 0.5)
        salvage_new = st.number_input("New machine salvage at end (€)", 0, 20_000_000, 0, 10_000)

    with right:
        net_switch = new_cost - old_resale
        pv_savings = annuity_pv(annual_saving, rep_rate, rep_life)
        pv_salvage = salvage_new / ((1 + rep_rate / 100) ** rep_life)
        rep_npv = -net_switch + pv_savings + pv_salvage

        k1, k2, k3 = st.columns(3)
        k1.metric("Net cost to switch", money(net_switch))
        k2.metric("PV of savings", money(pv_savings))
        k3.metric("NPV of replacing", money(rep_npv),
                  "Replace ✅" if rep_npv > 0 else "Keep old ❌",
                  delta_color="normal" if rep_npv > 0 else "inverse")

        if rep_npv > 0:
            st.success(
                f"✅ **REPLACE.** Buying new has a positive incremental NPV of {money(rep_npv)} — the savings "
                "(and any salvage) outweigh the net cost of switching."
            )
        else:
            st.error(
                f"❌ **KEEP THE OLD ASSET.** Replacing has a negative NPV of {money(rep_npv)} — the savings "
                "don't justify the switching cost."
            )
        st.caption("🧠 The old machine's *original* purchase price is a **sunk cost** — correctly excluded. "
                   "Only its current resale value (an opportunity cost of keeping it) is relevant.")

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Make-vs-Buy Comparator")
    st.markdown("Compare producing in-house vs. outsourcing — including opportunity cost.")

    l2, r2 = st.columns([0.38, 0.62])
    with l2:
        volume = st.number_input("Annual volume (units)", 1_000, 50_000_000, 100_000, 10_000)
        st.markdown("**Make (in-house) — per unit**")
        mat = st.number_input("Direct materials (€/unit)", 0.0, 1000.0, 4.00, 0.25)
        lab = st.number_input("Direct labour (€/unit)", 0.0, 1000.0, 3.00, 0.25)
        oh = st.number_input("Incremental overhead (€/unit)", 0.0, 1000.0, 1.00, 0.25)
        opp_cost = st.number_input("Opportunity cost of capacity (€/yr)", 0, 50_000_000, 150_000, 10_000,
                                   help="Contribution the capacity could earn elsewhere")
        st.markdown("**Buy (outsource)**")
        supplier = st.number_input("Supplier price (€/unit)", 0.0, 2000.0, 9.00, 0.25)
        transition = st.number_input("Extra buy costs — logistics/quality (€/yr)", 0, 20_000_000, 0, 10_000)

    with r2:
        make_unit = mat + lab + oh
        make_direct = make_unit * volume
        make_total = make_direct + opp_cost
        buy_total = supplier * volume + transition

        k1, k2, k3 = st.columns(3)
        k1.metric("Make — direct cost", money(make_direct))
        k2.metric("Make + opportunity cost", money(make_total))
        k3.metric("Buy — total cost", money(buy_total))

        diff = buy_total - make_total
        if abs(diff) < 1:
            st.info("The two options cost essentially the same — decide on qualitative/strategic factors.")
        elif make_total < buy_total:
            st.success(
                f"✅ **MAKE in-house.** It's {money(buy_total - make_total)}/yr cheaper (including "
                f"opportunity cost of {money(opp_cost)})."
            )
        else:
            st.warning(
                f"⚠️ **BUY (outsource).** Making in-house is {money(make_total - buy_total)}/yr more expensive "
                f"once the {money(opp_cost)} opportunity cost is included — even if direct cost looks lower."
            )

        comp = pd.DataFrame(
            {"Annual cost (€)": [make_direct, opp_cost, make_total, buy_total]},
            index=["Make (direct)", "Opportunity cost", "Make (total)", "Buy (total)"],
        )
        st.markdown("##### 📊 Cost comparison")
        st.bar_chart(comp)

        st.caption(
            f"Direct-cost comparison: Make €{make_unit:.2f}/unit vs. Buy €{supplier:.2f}/unit. "
            "Opportunity cost can flip a decision that looks obvious on direct costs alone."
        )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Sunk-cost test:** In the replacement tool, notice there's *no input* for the old machine's original
   cost — because it's sunk and irrelevant. Only resale value matters.
2. **Opportunity flip:** In make-vs-buy, raise the opportunity cost until 'make' loses to 'buy'.
"""
        )
    with e2:
        st.markdown(
            """
3. **Salvage kicker:** Add a new-machine salvage value. How much does it improve the replacement NPV?
4. **Volume effect:** In make-vs-buy, double the volume. Does the per-unit advantage scale as expected?
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Replacing ageing factory equipment", expanded=True):
        st.markdown(
            """
**Situation:** A plant runs an old machine with rising maintenance and energy costs. A new machine would
be far more efficient.

**How incremental analysis works:** Compare the **net cost to switch** (new cost less the old machine's
resale value) against the **PV of the running-cost savings** over the new machine's life. The old
machine's original price is **sunk** and excluded.

**Why it matters:** Managers often resist replacing "because the old one still works" — but if the
incremental savings beat the switching cost, replacing creates value.

**Lesson:** Replace when the NPV of incremental savings exceeds the net switching cost — ignore what the
old asset originally cost.
"""
        )

    with st.expander("Case B — Make-vs-buy for a component"):
        st.markdown(
            """
**Situation:** A manufacturer can produce a component in-house for €8/unit or buy it for €9/unit.

**What incremental analysis revealed:** On direct cost, making saves €1/unit. **But** in-house production
occupied a line that could otherwise produce a higher-margin product worth €150k/year — an **opportunity
cost** that made outsourcing cheaper overall.

**Why it matters:** The obvious "make is cheaper" conclusion was wrong once opportunity cost was included.

**Lesson:** In make-vs-buy, always ask what the in-house capacity could earn if freed up.
"""
        )

    with st.expander("Case C — The sunk-cost fallacy trap"):
        st.markdown(
            """
**Situation:** A company hesitated to scrap a €2m production line installed only two years earlier, feeling
it would "waste" the investment.

**What incremental analysis revealed:** The €2m was **sunk** — unrecoverable regardless of the decision.
The only relevant question was whether *future* cash flows favoured keeping or replacing it. On that basis,
replacing was clearly better.

**Why it matters:** Emotional attachment to past spending (the sunk-cost fallacy) leads to value-destroying
decisions.

**Lesson:** Never let sunk costs influence a forward-looking decision — only future incremental cash flows count.
"""
        )

    st.info(
        "🔗 **Pattern:** Replacement and make-vs-buy decisions are won or lost on *incremental* thinking — "
        "include opportunity costs, exclude sunk costs, and remember the qualitative/strategic factors the "
        "numbers can't fully capture."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_45"):
        q1 = st.radio(
            "**1.** Replacement and make-vs-buy decisions should be based on:",
            [
                "Total company cash flows",
                "Incremental cash flows — those that differ between the options",
                "Accounting profit only",
                "The original cost of existing assets",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** A sunk cost should be:",
            [
                "Included as a cost of the new option",
                "Ignored — it cannot be changed by the decision",
                "Added to the opportunity cost",
                "Treated as revenue",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** In a replacement decision, the old machine's ORIGINAL purchase price is:",
            [
                "A relevant incremental cost",
                "A sunk cost that should be ignored",
                "An opportunity cost",
                "Added to the new machine's cost",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Opportunity cost is:",
            [
                "Cash already spent in the past",
                "The value of the next-best alternative given up",
                "A type of depreciation",
                "Always zero",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** In a make-vs-buy decision, if in-house production ties up capacity that could earn money elsewhere, that lost contribution is:",
            [
                "Irrelevant",
                "An opportunity cost that must be added to the 'make' option",
                "A sunk cost to ignore",
                "A benefit of making in-house",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Incremental cash flows — those that differ between the options"),
            "2": (q2, "Ignored — it cannot be changed by the decision"),
            "3": (q3, "A sunk cost that should be ignored"),
            "4": (q4, "The value of the next-best alternative given up"),
            "5": (q5, "An opportunity cost that must be added to the 'make' option"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've completed Part 4 (Investment Appraisal)! On to Part 5 (Scenario, Sensitivity & Risk). 🎉")
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
    f"Applied Financial Models · Module 4.5 Replacement & Make-vs-Buy Decisions · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
