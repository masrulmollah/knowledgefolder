"""
================================================================================
APPLIED FINANCIAL MODELS
Module 7.4 — COMMON PITFALLS & MODEL AUDITING
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to spot errors and audit a model: common pitfalls, garbage-in-garbage-out,
error-checking discipline, and stress-testing assumptions.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a model-audit checklist scorer + error spotter)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_7_4_Common_Pitfalls_and_Model_Auditing.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="7.4 Common Pitfalls & Model Auditing — Applied Financial Models",
    layout="wide",
    page_icon="🎯",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


# --------------------------------------------------------------------------------
# SESSION STATE
# --------------------------------------------------------------------------------
if "audit_answers" not in st.session_state:
    st.session_state.audit_answers = {}

# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Control Panel")
st.sidebar.caption("Part 7 · From Model to Decision")
st.sidebar.markdown(
    """
**Module 7.4 — Common Pitfalls & Model Auditing**

🔴 *Advanced*

**You will learn to:**
- Recognise common modelling errors
- Avoid garbage-in-garbage-out
- Build & run error checks
- Stress-test a model before trusting it
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to score a model with an audit "
    "checklist and play 'spot the error'."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎯 7.4 · Common Pitfalls & Model Auditing")
st.markdown(
    """
A model that looks polished can still be **dangerously wrong**. History is full of costly spreadsheet
errors that led to bad decisions and real losses. **Model auditing** is the quality-control discipline
that catches mistakes *before* they reach a decision-maker — and **stress-testing** confirms the model
behaves sensibly under pressure.

This module covers the most common pitfalls (and how to avoid them), how to build and run **error checks**,
and how to audit and stress-test a model so you can trust it.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "7.4")
c2.metric("Part", "7 — Decision")
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
### Garbage in, garbage out (GIGO)
A model is only as good as its **inputs and logic**. Flawless formulas fed with bad assumptions produce
confident, precise — and wrong — answers. Auditing checks **both** the mechanics (does it calculate
correctly?) and the assumptions (are the inputs credible?).
"""
    )

    st.markdown("### The most common modelling pitfalls")
    pitfalls = pd.DataFrame(
        {
            "Pitfall": [
                "Hard-coded numbers in formulas", "Broken/incorrect references", "Inconsistent formulas across a row",
                "Circular references (unintended)", "Unit / sign errors", "Over-optimistic assumptions",
                "No error checks", "False precision",
            ],
            "How it bites": [
                "Hidden assumptions no one can find or flex",
                "A formula points to the wrong cell → silent error",
                "One rogue cell breaks the whole row",
                "The model spirals or won't calculate",
                "€000s vs. € , or a + that should be a − ",
                "Hockey-stick forecasts that never happen",
                "Mistakes reach the decision undetected",
                "Decimals imply certainty the inputs don't support",
            ],
        }
    )
    st.table(pitfalls)

    with st.expander("🔑 Concept 1 — Build error checks into the model"):
        st.markdown(
            """
A professional model **checks itself**. Standard checks:
- **Balance-sheet check:** Assets − Liabilities − Equity = 0.
- **Cash flow ties** to the balance-sheet cash movement.
- **Sum checks:** parts sum to the total; % between 0–100%.
- **Sense checks:** margins, growth rates within plausible bounds.

Wire each to conditional formatting so it turns **red** on failure. A visible 'checks' row is the single
most valuable audit tool.
"""
        )

    with st.expander("🔑 Concept 2 — Stress-testing (does it behave sensibly?)"):
        st.markdown(
            """
Push inputs to **extremes** and see if the model stays sane:
- Set volume to **zero** — does profit/cash go where you'd expect (not to a bizarre number)?
- Set growth very **high** — does anything break or explode implausibly?
- Flip a key input **negative** — does the model handle it gracefully?

If extreme inputs produce nonsense outputs, there's a logic error hiding. Stress-testing flushes it out.
"""
        )

    with st.expander("🔑 Concept 3 — The audit review process"):
        st.markdown(
            """
A structured audit:
1. **Trace the logic** — follow inputs → calculations → outputs; can you explain every number?
2. **Check the mechanics** — spot hard-codes, broken references, inconsistent rows.
3. **Challenge the assumptions** — are they sourced, reasonable, benchmarked?
4. **Run the checks** — do all error checks pass?
5. **Stress-test** — extreme inputs, sensitivities, worst case.

A fresh pair of eyes catches what the builder can't see.
"""
        )

    with st.expander("🔑 Concept 4 — Challenging assumptions (the GIGO defence)"):
        st.markdown(
            """
The mechanics are often fine — the **assumptions** are where models go wrong. Ask:
- Is each key assumption **sourced** (data, benchmark) or just a guess?
- Is the forecast a credible **trend** or a wishful **hockey stick**?
- What does the model implicitly assume (e.g. that share can be won, prices held)?

An assumption log — stating each key input and its basis — is best practice and makes challenge easy.
"""
        )

    with st.expander("🔑 Concept 5 — Famous spreadsheet disasters"):
        st.markdown(
            """
Real-world errors that reached the headlines show the stakes:
- A **copy-paste / formula error** in a bank's risk model understated risk (contributing to large losses).
- A **spreadsheet omission** dropped assets from a merger analysis, misstating the position.
- Academic and policy analyses have been **reversed** after coding/range errors were found.

The lesson is universal: **audit before you rely**. The cost of a check is trivial next to the cost of a
wrong decision.
"""
        )

    st.success(
        "**Takeaway:** Models fail from bad inputs (GIGO) and hidden mechanical errors. Defend against both: "
        "build self-checking error rows, trace the logic, challenge every assumption, and stress-test with "
        "extreme inputs — *audit before you rely*."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Auditing a flawed model")
    st.markdown("A model reports a confident NPV of **€2.1m**. An audit finds three problems.")

    st.markdown("#### Finding 1 — A hard-coded number")
    st.markdown(
        """
`Revenue = Units * 2.05 * 1.15` — the `1.15` is an undocumented 15% uplift buried in the formula. Nobody
knew it was there, and it inflated revenue. **Fix:** move it to a labelled input (or remove it if it's an error).
"""
    )

    st.markdown("#### Finding 2 — A unit error")
    st.markdown(
        """
Fixed costs were entered as **€300** instead of **€300,000** (a €000s mix-up). The model understated costs
by €299,700, massively overstating profit. **Fix:** consistent units and a sense-check on the cost line.
"""
    )

    st.markdown("#### Finding 3 — A hockey-stick assumption")
    st.markdown(
        """
Revenue was assumed to grow **35%/year for five years** — with no market or capacity evidence. **Fix:**
benchmark against history and market growth; a credible ~8% roughly **halves** the NPV.
"""
    )

    st.markdown("#### The corrected picture")
    e1, e2 = st.columns(2)
    e1.metric("Reported NPV (flawed)", "€2,100,000")
    e2.metric("Audited NPV (corrected)", "≈ €650,000", "−69%", delta_color="inverse")

    st.info(
        "**Insight:** The 'confident' €2.1m NPV was **~3× too high** — a hidden hard-code, a €000s unit "
        "error, and a hockey-stick growth assumption all flattered it. None was visible on the surface; only "
        "an **audit** (tracing logic, sense-checking units, challenging assumptions) revealed the true "
        "~€650k. **This is why you never trust a model you haven't audited.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Model Audit Scorecard")
    st.markdown(
        "Tick the checks your model passes. The scorecard rates how audit-ready (trustworthy) it is."
    )

    checks = [
        ("Inputs are separated and clearly labelled (no hidden hard-codes)", 15),
        ("All references are correct (no broken/mis-pointed formulas)", 15),
        ("One consistent formula per row, copied across", 10),
        ("No unintended circular references", 10),
        ("Units and signs are consistent and sense-checked", 15),
        ("Built-in error checks (balance, cash tie, sums) all pass", 15),
        ("Key assumptions are sourced / benchmarked (not guesses)", 10),
        ("The model has been stress-tested with extreme inputs", 10),
    ]

    left, right = st.columns([0.55, 0.45])
    states = []
    with left:
        st.markdown("##### ✅ Audit checklist")
        for i, (label, w) in enumerate(checks):
            states.append(st.checkbox(f"{label}  _(+{w})_", value=(i < 3), key=f"chk_{i}"))

    with right:
        score = sum(w for (l, w), s in zip(checks, states) if s)
        st.markdown("##### 📊 Audit-readiness score")
        st.progress(score / 100)
        st.metric("Score", f"{score} / 100")

        if score >= 90:
            grade, box = "A — Trustworthy", st.success
            msg = "Audit-ready. You can rely on this model for a decision."
        elif score >= 70:
            grade, box = "B — Minor gaps", st.info
            msg = "Largely sound; close the missing checks before relying on it."
        elif score >= 50:
            grade, box = "C — Risky", st.warning
            msg = "Several gaps — do not present to decision-makers until fixed."
        else:
            grade, box = "D — Do not trust", st.error
            msg = "High error risk. This model must be audited and rebuilt before use."
        box(f"**Grade: {grade}** — {msg}")

    st.markdown("##### 🔍 Outstanding items")
    missing = [l for (l, w), s in zip(checks, states) if not s]
    if missing:
        for m in missing:
            st.markdown(f"- ❌ {m}")
    else:
        st.markdown("- ✅ All audit checks passed — fully audit-ready.")

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Spot the Error")
    st.markdown("Inspect each formula/situation and identify the pitfall.")

    scenarios = [
        {
            "code": "Fixed cost cell:  300   (rest of model in €000s → shown as 300,000 elsewhere)",
            "context": "The fixed-cost input looks tiny next to other lines.",
            "options": ["A unit / €000s inconsistency", "A circular reference", "A missing chart", "Too many decimals"],
            "answer": "A unit / €000s inconsistency",
            "explain": "The cost is in € while the model runs in €000s — a classic unit error that understates cost.",
        },
        {
            "code": "=Revenue * 0.6 * 1.15",
            "context": "A gross-profit formula with two bare numbers in it.",
            "options": ["Hard-coded numbers buried in a formula", "A balance check", "A sensible input cell", "A stress test"],
            "answer": "Hard-coded numbers buried in a formula",
            "explain": "0.6 (COGS%) and 1.15 (an uplift) should be labelled input cells, not hidden in the formula.",
        },
        {
            "code": "Revenue growth = 35% per year for 5 years (no supporting evidence)",
            "context": "A forecast that rockets upward with no basis.",
            "options": ["An over-optimistic 'hockey-stick' assumption", "A unit error", "A broken reference", "A balance check"],
            "answer": "An over-optimistic 'hockey-stick' assumption",
            "explain": "Unsupported steep growth is a GIGO red flag — benchmark it against history and the market.",
        },
    ]

    for i, sc in enumerate(scenarios):
        st.markdown(f"##### Scenario {i+1}")
        st.code(sc["code"], language="text")
        st.caption(sc["context"])
        choice = st.radio("Which pitfall is this?", sc["options"], index=None, key=f"spot_{i}")
        if choice is not None:
            if choice == sc["answer"]:
                st.success(f"✅ Correct! {sc['explain']}")
            else:
                st.error(f"❌ Not quite. **Correct:** {sc['answer']} — {sc['explain']}")
        st.markdown("---")

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The €50k balance error caught by a check", expanded=True):
        st.markdown(
            """
**Situation:** An integrated model was presented as final, but a balance-sheet check quietly showed a
€50k discrepancy.

**How auditing helped:** The visible **balance check** (Assets − Liabilities − Equity) flagged the gap
instantly. Tracing it revealed depreciation wasn't fully linked to retained earnings — a broken link.
Fixing it brought the check to zero.

**Why it matters:** Without the check, the error would have flowed into the decision unnoticed.

**Lesson:** A single self-checking cell can save you from a wrong decision — build checks into every model.
"""
        )

    with st.expander("Case B — The hockey-stick that didn't survive challenge"):
        st.markdown(
            """
**Situation:** A business case assumed 35% annual growth, producing a spectacular NPV.

**What the audit found:** The growth assumption had **no evidence** — no market data, no capacity plan.
Benchmarked against a realistic ~8%, the NPV **more than halved**, changing the recommendation.

**Why it matters:** The mechanics were perfect; the **assumption** was the flaw (GIGO). Auditing the
inputs — not just the formulas — is essential.

**Lesson:** Challenge every key assumption; unsupported growth is the most common way models mislead.
"""
        )

    with st.expander("Case C — Stress-testing exposed a hidden logic error"):
        st.markdown(
            """
**Situation:** A model looked fine at normal inputs, so it was nearly signed off.

**What stress-testing found:** Setting volume to **zero** produced a *positive* profit — impossible. The
audit traced it to a fixed cost wrongly modelled as a negative, which only showed up at the extreme.

**Why it matters:** Normal inputs hid the bug; only pushing to an extreme revealed it.

**Lesson:** Always stress-test with extreme inputs — logic errors often hide until you push the model hard.
"""
        )

    st.info(
        "🔗 **Pattern:** Auditing defends against both flavours of failure — mechanical errors (caught by "
        "checks and tracing) and bad assumptions (caught by challenge and benchmarking) — with "
        "stress-testing as the final safety net."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_74"):
        q1 = st.radio(
            "**1.** 'Garbage in, garbage out' (GIGO) means:",
            [
                "Models always produce garbage",
                "A model with correct formulas can still be wrong if the inputs/assumptions are bad",
                "Only the formulas matter",
                "Auditing is unnecessary",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The single most valuable built-in audit tool is:",
            [
                "A bigger font",
                "A visible error-check row (e.g. balance check = 0) that turns red on failure",
                "More decimal places",
                "A longer model",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Stress-testing a model means:",
            [
                "Running it once with base-case inputs",
                "Pushing inputs to extremes to see if the outputs stay sensible",
                "Deleting the assumptions",
                "Adding more charts",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A revenue forecast of 35%/year for 5 years with no supporting evidence is an example of:",
            [
                "A balance check",
                "An over-optimistic 'hockey-stick' assumption",
                "A unit error",
                "A circular reference",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Which is the best defence against modelling errors reaching a decision?",
            [
                "Trusting a polished-looking model",
                "Auditing: trace the logic, challenge assumptions, run checks, and stress-test before relying on it",
                "Adding more inputs",
                "Presenting faster",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "A model with correct formulas can still be wrong if the inputs/assumptions are bad"),
            "2": (q2, "A visible error-check row (e.g. balance check = 0) that turns red on failure"),
            "3": (q3, "Pushing inputs to extremes to see if the outputs stay sensible"),
            "4": (q4, "An over-optimistic 'hockey-stick' assumption"),
            "5": (q5, "Auditing: trace the logic, challenge assumptions, run checks, and stress-test before relying on it"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you can audit and stress-test a model! On to Module 7.5 (Ethics & Assumption Integrity). 🎉")
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
    f"Applied Financial Models · Module 7.4 Common Pitfalls & Model Auditing · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
