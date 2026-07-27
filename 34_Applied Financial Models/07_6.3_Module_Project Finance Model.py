"""
================================================================================
APPLIED FINANCIAL MODELS
Module 6.3 — PROJECT FINANCE MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how project finance works: cash flow available for debt service (CFADS), the
debt service coverage ratio (DSCR), debt sculpting, and covenant testing.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live CFADS / DSCR / covenant engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_6_3_Project_Finance_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="6.3 Project Finance Model — Applied Financial Models",
    layout="wide",
    page_icon="🚀",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def run_project_finance(cfads0, cfads_growth, opening_debt, interest_rate,
                        tenor, sculpt, target_dscr, covenant_dscr):
    """
    Build a project finance debt schedule.
    - CFADS grows each year.
    - If sculpt=True, principal repayment is sized so DSCR = target each year
      (subject to repaying within tenor); else equal (annuity-like) principal.
    Returns schedule DataFrame + summary.
    """
    rows = []
    debt = opening_debt
    cfads = cfads0
    min_dscr = None
    breaches = 0

    # For equal-principal mode
    equal_principal = opening_debt / tenor if tenor else opening_debt

    for y in range(1, tenor + 1):
        if y > 1:
            cfads *= (1 + cfads_growth / 100)
        interest = debt * interest_rate / 100

        if sculpt:
            # principal sized so debt service = CFADS / target_dscr
            target_ds = cfads / target_dscr if target_dscr else 0
            principal = max(target_ds - interest, 0)
            principal = min(principal, debt)  # can't repay more than outstanding
        else:
            principal = min(equal_principal, debt)

        debt_service = interest + principal
        dscr = cfads / debt_service if debt_service > 0 else float("inf")
        debt_end = debt - principal

        breach = dscr < covenant_dscr
        if breach:
            breaches += 1
        if min_dscr is None or dscr < min_dscr:
            min_dscr = dscr

        rows.append({
            "Year": y, "CFADS": cfads, "Interest": interest, "Principal": principal,
            "Debt service": debt_service, "DSCR": dscr, "Debt (end)": debt_end,
            "Covenant OK": "✅" if not breach else "❌",
        })
        debt = debt_end

    schedule = pd.DataFrame(rows)
    fully_repaid = debt <= 1
    summary = {
        "min_dscr": min_dscr, "breaches": breaches, "ending_debt": debt,
        "fully_repaid": fully_repaid,
    }
    return schedule, summary


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 6 · Specialised & Advanced Models")
st.sidebar.markdown(
    """
**Module 6.3 — Project Finance Model**

🔴 *Advanced*

**You will learn to:**
- Calculate CFADS & the DSCR
- Understand debt sculpting
- Test debt-service covenants
- See how lenders size project debt
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a debt schedule with "
    "sculpting and watch the DSCR and covenant tests update."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🚀 6.3 · Project Finance Model")
st.markdown(
    """
**Project finance** is how large, long-life assets — power plants, toll roads, factories, infrastructure —
get funded. The key feature: lenders are repaid **only from the project's own cash flows**, not the
sponsor's balance sheet (it's *non-recourse* or *limited-recourse*). Because the cash flows *are* the
security, lenders focus intensely on one question: *"will the project generate enough cash to service its
debt, with a safety margin?"*

This module builds the tools they use: **CFADS**, the **DSCR**, **debt sculpting**, and **covenant testing**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "6.3")
c2.metric("Part", "6 — Specialised")
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
### CFADS — Cash Flow Available for Debt Service
The foundation of project finance. CFADS is the cash the project generates that can be used to pay debt,
*before* any financing:
"""
    )
    st.latex(r"\text{CFADS} = \text{Operating Cash Flow} - \text{Taxes} - \text{Capex} \; (\pm \Delta \text{Reserves})")

    st.markdown("### DSCR — Debt Service Coverage Ratio")
    st.markdown("The single most important ratio in project finance — the lender's safety margin:")
    st.latex(r"\text{DSCR} = \frac{\text{CFADS}}{\text{Debt Service (Interest + Principal)}}")
    st.markdown(
        """
- **DSCR = 1.0×** → cash *exactly* covers debt service (no cushion — dangerous).
- **DSCR = 1.5×** → cash is 1.5× the debt service (a comfortable 50% cushion).
- Lenders require a **minimum DSCR** (a covenant), typically **1.2×–1.5×** depending on risk.
"""
    )

    st.markdown("### The key concepts")
    tbl = pd.DataFrame(
        {
            "Term": ["CFADS", "DSCR", "Debt sculpting", "Covenant", "Tenor"],
            "Meaning": [
                "Cash available to service debt (the numerator of DSCR)",
                "CFADS ÷ debt service — the coverage / safety margin",
                "Shaping repayments so DSCR stays at a target each year",
                "A lender rule (e.g. DSCR must stay above 1.3×)",
                "The debt's repayment period (life of the loan)",
            ],
        }
    )
    st.table(tbl)

    with st.expander("🔑 Concept 1 — Why lenders live and die by the DSCR"):
        st.markdown(
            """
In project finance the loan is repaid *only* from project cash flow, so the DSCR **is** the lender's
security. A DSCR of 1.4× means that even if cash flow falls 28%, the project could still service its
debt — that cushion is what makes the loan safe. Lenders set a **minimum DSCR covenant**; breaching it can
trigger a default even if payments are still being made.
"""
        )

    with st.expander("🔑 Concept 2 — Debt sculpting (shaping repayments to cash flow)"):
        st.markdown(
            """
Unlike a normal loan with fixed repayments, project debt is often **sculpted**: principal repayments are
sized each period so the **DSCR stays at a constant target** (e.g. exactly 1.5× every year).

- In **high-cash years**, the project repays **more** principal.
- In **low-cash years**, it repays **less**.

Sculpting matches debt service to the project's actual cash generation — maximising the debt the project
can safely carry while keeping the covenant satisfied throughout.
"""
        )

    with st.expander("🔑 Concept 3 — Sizing the debt (how much can the project borrow?)"):
        st.markdown(
            """
Lenders work *backwards* from cash flow: given the forecast CFADS and a target DSCR, they calculate the
**maximum debt** the project can support:

$$\\text{Max annual debt service} = \\frac{\\text{CFADS}}{\\text{Target DSCR}}$$

The present value of those affordable debt-service amounts (at the loan rate) gives the **debt capacity**.
The rest of the project cost must be funded by **equity**. This 'cash-flow-first' sizing is the opposite
of corporate lending, which looks at the balance sheet.
"""
        )

    with st.expander("🔑 Concept 4 — Covenants & reserve accounts"):
        st.markdown(
            """
Lenders protect themselves with:
- **DSCR covenant** — a minimum ratio that must be maintained (breach = default event).
- **Debt Service Reserve Account (DSRA)** — cash set aside (often 6 months of debt service) as a buffer.
- **Cash sweeps / distribution locks** — if DSCR falls near the covenant, cash to equity is trapped and
  used to pay down debt first.

These mechanisms make the debt safer and are standard in any project finance deal.
"""
        )

    with st.expander("🔑 Concept 5 — DSCR vs. LLCR"):
        st.markdown(
            """
- **DSCR** — a *period-by-period* coverage ratio (this year's CFADS vs. this year's debt service).
- **LLCR** (Loan Life Coverage Ratio) — a *whole-of-life* ratio: the PV of all future CFADS over the loan
  life ÷ outstanding debt. It measures overall robustness, not just one year.

Lenders watch **both**: DSCR for short-term coverage, LLCR for lifetime resilience.
"""
        )

    st.success(
        "**Takeaway:** Project finance repays debt only from project cash flow, so the **DSCR** (CFADS ÷ "
        "debt service) is everything. Debt is **sculpted** to keep DSCR at a target, sized from a **target "
        "DSCR**, and protected by **covenants** and reserves."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — DSCR and debt sculpting")
    st.markdown("A project generates CFADS starting at **€15m**, growing ~3%/year. Debt €60m at 6%, 10-year tenor.")

    st.markdown("#### Step 1 — DSCR with equal principal repayment")
    st.markdown(
        """
Year 1: equal principal = €60m ÷ 10 = €6m; interest = €60m × 6% = €3.6m.
- Debt service = €6m + €3.6m = **€9.6m**
- $$\\text{DSCR} = \\frac{15.0}{9.6} = \\mathbf{1.56\\times}$$

The DSCR of 1.56× comfortably exceeds a typical 1.30× covenant — the project can service its debt with
room to spare.
"""
    )

    st.markdown("#### Step 2 — Debt sculpting to a target 1.50× DSCR")
    st.markdown(
        """
Instead of fixed principal, size the debt service so DSCR = 1.50× exactly:
- Target debt service = CFADS ÷ 1.50 = €15.0m ÷ 1.50 = **€10.0m**
- Interest = €3.6m → principal = €10.0m − €3.6m = **€6.4m**

By repaying €6.4m (more than the €6m equal amount) in this high-cash year, the project keeps DSCR at
exactly 1.50× and pays debt down faster. In leaner years it would repay less, holding DSCR steady.
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("CFADS (Year 1)", "€15.0m")
    e2.metric("DSCR (equal principal)", "1.56×", "> 1.30× covenant ✅")
    e3.metric("Sculpted debt service", "€10.0m", "→ DSCR 1.50×")

    st.info(
        "**Insight:** With a **1.56× DSCR**, the project has a comfortable cushion — cash flow could fall "
        "~36% before it couldn't service its debt. **Sculpting** the repayments to a target 1.50× lets the "
        "project safely carry (and repay) as much debt as its cash flow allows, year by year. Lenders love "
        "this because the covenant is respected in *every* period, not just on average."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Project Finance Debt Engine")
    st.markdown(
        "Set the project's cash flow and debt terms, choose equal-principal or **sculpted** repayment, and "
        "watch the DSCR and covenant tests update year by year."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        st.markdown("##### 💵 Project cash flow")
        cfads0 = st.number_input("Year-1 CFADS (€m)", 0.1, 10_000.0, 15.0, 0.5)
        cfads_growth = st.slider("CFADS growth (%/yr)", -10.0, 15.0, 3.0, 0.5)

        st.markdown("##### 🏦 Debt terms")
        opening_debt = st.number_input("Debt drawn (€m)", 1.0, 100_000.0, 60.0, 1.0)
        interest_rate = st.slider("Interest rate (%)", 0.0, 20.0, 6.0, 0.5)
        tenor = st.slider("Loan tenor (years)", 2, 25, 10, 1)

        st.markdown("##### 📏 Structure & covenant")
        sculpt = st.toggle("Sculpt debt to a target DSCR", value=True)
        target_dscr = st.slider("Target DSCR (for sculpting)", 1.0, 3.0, 1.5, 0.05)
        covenant_dscr = st.slider("Minimum DSCR covenant", 1.0, 2.5, 1.3, 0.05)

    with right:
        schedule, s = run_project_finance(
            cfads0, cfads_growth, opening_debt, interest_rate,
            tenor, sculpt, target_dscr, covenant_dscr,
        )

        k1, k2, k3 = st.columns(3)
        k1.metric("Minimum DSCR", f"{s['min_dscr']:.2f}×",
                  "Above covenant ✅" if s["min_dscr"] >= covenant_dscr else "Breach ❌",
                  delta_color="normal" if s["min_dscr"] >= covenant_dscr else "inverse")
        k2.metric("Covenant breaches", f"{s['breaches']} yr(s)",
                  "None ✅" if s["breaches"] == 0 else "Breached ❌",
                  delta_color="normal" if s["breaches"] == 0 else "inverse")
        k3.metric("Debt fully repaid?", "Yes ✅" if s["fully_repaid"] else f"No — {money(s['ending_debt'],dp=1)}m left",
                  delta_color="normal" if s["fully_repaid"] else "inverse")

        if s["breaches"] == 0 and s["fully_repaid"]:
            st.success(
                f"✅ **Bankable structure:** DSCR stays above the {covenant_dscr:.2f}× covenant in every "
                "year (minimum "
                f"{s['min_dscr']:.2f}×) and the debt is fully repaid within the tenor. Lenders would be comfortable."
            )
        elif s["breaches"] > 0:
            st.error(
                f"❌ **Covenant breach in {s['breaches']} year(s)** — DSCR falls below {covenant_dscr:.2f}×. "
                "The project can't safely carry this much debt. Reduce debt, extend tenor, or lower the interest rate."
            )
        else:
            st.warning(
                f"⚠️ Covenant holds, but **{money(s['ending_debt'],dp=1)}m of debt remains** unpaid at the end "
                "of the tenor. Extend the tenor or increase repayments."
            )

        disp = schedule.copy()
        for col in ["CFADS", "Interest", "Principal", "Debt service", "Debt (end)"]:
            disp[col] = disp[col].map(lambda v: money(v, dp=2) + "m")
        disp["DSCR"] = schedule["DSCR"].map(lambda v: f"{v:.2f}×")
        st.markdown("##### 📄 Debt Schedule")
        st.dataframe(disp, use_container_width=True, hide_index=True)

        st.markdown("##### 📊 DSCR by year (vs. covenant)")
        dscr_chart = schedule.set_index("Year")[["DSCR"]].copy()
        dscr_chart["Covenant"] = covenant_dscr
        st.line_chart(dscr_chart)
        st.caption(
            f"As long as the DSCR line stays **above** the {covenant_dscr:.2f}× covenant, the project is "
            "compliant. Sculpting holds the DSCR flat at the target; equal principal lets it drift."
        )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Over-gearing:** Raise debt to €90m. Watch the DSCR fall and covenant breaches appear.
2. **Sculpt vs. equal:** Toggle sculpting off. See how equal-principal lets the DSCR drift over time.
"""
        )
    with e2:
        st.markdown(
            """
3. **Debt capacity:** With sculpting on, find the maximum debt that keeps min DSCR at the 1.30× covenant.
4. **Rate shock:** Raise the interest rate to 12%. Does the project still service its debt safely?
"""
        )

    st.download_button(
        "⬇️ Download the debt schedule (CSV)",
        schedule.to_csv(index=False).encode("utf-8"),
        "project_finance_schedule.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Financing a power plant / infrastructure asset", expanded=True):
        st.markdown(
            """
**Situation:** A developer builds a power plant with long-term, contracted revenues and seeks non-recourse
debt.

**How project finance works:** Lenders forecast **CFADS** from the contracted revenues, apply a **target
DSCR** (say 1.4×), and size the debt to what those cash flows can safely service. The rest is equity.

**Why it matters:** Because repayment relies solely on the plant's cash flows, the DSCR cushion is what
makes the loan financeable — the sponsor's other assets aren't on the hook.

**Lesson:** In infrastructure, stable contracted cash flows + a healthy DSCR = bankable project debt.
"""
        )

    with st.expander("Case B — Debt sculpting for a seasonal / ramping project"):
        st.markdown(
            """
**Situation:** A project's cash flows start low and ramp up over several years.

**How sculpting helps:** Fixed (equal) repayments would breach the DSCR covenant in the early low-cash
years. **Sculpting** the repayments — small in early years, larger as cash flow ramps — keeps the DSCR at
the target throughout, avoiding covenant breaches.

**Why it matters:** Sculpting matches debt service to actual cash generation, maximising affordable debt
while protecting the covenant every period.

**Lesson:** For projects with uneven cash flows, sculpting is essential to keep the DSCR compliant.
"""
        )

    with st.expander("Case C — A covenant breach and the reserve account"):
        st.markdown(
            """
**Situation:** An operating project hit a bad year and its DSCR dropped toward the covenant floor.

**What the structure did:** The **Debt Service Reserve Account (DSRA)** — pre-funded with ~6 months of
debt service — covered the shortfall, and a **cash sweep** trapped distributions to equity until coverage
recovered. A technical breach was avoided.

**Why it matters:** Project finance builds in these safety mechanisms precisely because cash flows can
disappoint; they protect lenders without forcing an immediate default.

**Lesson:** Reserve accounts and cash sweeps are the shock absorbers that make DSCR covenants workable in
the real world.
"""
        )

    st.info(
        "🔗 **Pattern:** Project finance is 'cash-flow-first' lending — the DSCR is the security, debt is "
        "sized and sculpted to the cash flows, and covenants plus reserves protect the lender against a bad year."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_63"):
        q1 = st.radio(
            "**1.** In project finance, lenders are typically repaid from:",
            [
                "The sponsor's entire balance sheet",
                "The project's own cash flows (non-recourse / limited-recourse)",
                "Government guarantees only",
                "New equity issuance each year",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The Debt Service Coverage Ratio (DSCR) is:",
            [
                "Debt service ÷ CFADS",
                "CFADS ÷ Debt service (interest + principal)",
                "Debt ÷ Equity",
                "EBITDA × multiple",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** A DSCR of 1.5× means:",
            [
                "The project can only just cover its debt service",
                "Cash flow is 1.5× the debt service — a 50% cushion",
                "The project is in default",
                "Debt is 1.5× equity",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Debt sculpting means:",
            [
                "Repaying the same fixed principal every year",
                "Sizing principal repayments so the DSCR stays at a target each period",
                "Never repaying principal",
                "Converting debt to equity",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** A DSCR covenant is:",
            [
                "A tax on project debt",
                "A minimum coverage ratio the project must maintain (a breach can trigger default)",
                "The interest rate on the loan",
                "The project's depreciation policy",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The project's own cash flows (non-recourse / limited-recourse)"),
            "2": (q2, "CFADS ÷ Debt service (interest + principal)"),
            "3": (q3, "Cash flow is 1.5× the debt service — a 50% cushion"),
            "4": (q4, "Sizing principal repayments so the DSCR stays at a target each period"),
            "5": (q5, "A minimum coverage ratio the project must maintain (a breach can trigger default)"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered project finance! On to Module 6.4 (Working Capital Optimization). 🎉")
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
    f"Applied Financial Models · Module 6.3 Project Finance Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
