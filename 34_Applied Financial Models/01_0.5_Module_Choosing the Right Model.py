"""
================================================================================
APPLIED FINANCIAL MODELS
Module 0.5 — CHOOSING THE RIGHT MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to match a business question to the RIGHT type of financial model — the
capstone skill of Part 0 (Orientation & Foundations).

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a decision-tree wizard + model selector)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_0_5_Choosing_the_Right_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="0.5 Choosing the Right Model — Applied Financial Models",
    layout="wide",
    page_icon="🧭",
)

# --------------------------------------------------------------------------------
# MODEL REFERENCE DATA
# --------------------------------------------------------------------------------
MODELS = [
    {
        "name": "Three-Statement Model",
        "module": "Part 1 (1.1–1.5)",
        "question": "How will the whole company's financials evolve over time?",
        "use_when": "You need an integrated view of P&L, balance sheet and cash flow.",
        "outputs": "Projected income statement, balance sheet, cash flow",
    },
    {
        "name": "Forecasting / Budget Model",
        "module": "Part 2 (2.1–2.4)",
        "question": "What are next year's / quarter's numbers likely to be?",
        "use_when": "You're planning, budgeting, or building a rolling forecast.",
        "outputs": "Revenue/cost forecast, budget vs. actual, variance bridges",
    },
    {
        "name": "Valuation Model (DCF / Comps)",
        "module": "Part 3 (3.1–3.5)",
        "question": "What is this business, share, or asset worth?",
        "use_when": "You're valuing a company for investment, sale, or fundraising.",
        "outputs": "Enterprise/equity value, share price, valuation range",
    },
    {
        "name": "Investment Appraisal (NPV / IRR)",
        "module": "Part 4 (4.1–4.5)",
        "question": "Should we invest in this project, asset, or Capex?",
        "use_when": "You're deciding whether a specific investment is worthwhile.",
        "outputs": "NPV, IRR, payback period, accept/reject decision",
    },
    {
        "name": "Scenario & Sensitivity Model",
        "module": "Part 5 (5.1–5.4)",
        "question": "What happens if our assumptions are wrong?",
        "use_when": "You need to understand risk, ranges, and key drivers.",
        "outputs": "Scenario outcomes, tornado charts, break-even, risk range",
    },
    {
        "name": "Specialised Model (LBO / M&A / Project Finance)",
        "module": "Part 6 (6.1–6.5)",
        "question": "Deal-specific: returns, financing structure, or synergies?",
        "use_when": "You're structuring a buyout, merger, or financed project.",
        "outputs": "Equity returns, accretion/dilution, debt schedules, DSCR",
    },
]

# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 0 · Orientation & Foundations")
st.sidebar.markdown(
    """
**Module 0.5 — Choosing the Right Model**

🟢 *Foundational*

**You will learn to:**
- Match a business question to a model type
- Use a decision tree to select a model
- Avoid using the wrong tool for the job
- Know what each model can (and can't) answer
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to run the **decision-tree "
    "wizard** — answer a few questions and get your recommended model."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🧭 0.5 · Choosing the Right Model")
st.markdown(
    """
The most common — and costly — modeling mistake isn't a broken formula. It's building the **wrong type
of model** for the question you're trying to answer. A brilliant DCF is useless if what you actually
needed was a break-even analysis.

This capstone module of Part 0 gives you a **decision framework**: start from the *business question*,
and let it point you to the right model. Get this right and every downstream module makes sense.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "0.5")
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
### Start with the question, not the model
Amateurs pick a model they know and force the problem into it. Professionals start with a crisp
**business question** and let it dictate the tool. The golden principle:

> **The question determines the model — never the other way around.**
"""
    )

    st.markdown("### The model-selection map")
    map_df = pd.DataFrame(
        [
            {"If the question is about…": m["question"],
             "…use this model": m["name"],
             "Where to learn it": m["module"]}
            for m in MODELS
        ]
    )
    st.table(map_df)

    st.markdown(
        """
### The four questions that narrow it down
Ask these in order and you'll almost always land on the right model:

1. **Am I looking at the *whole company* or a *single project/decision*?**
   - Whole company → three-statement, forecast, or valuation.
   - Single project → investment appraisal (NPV/IRR).
2. **Do I need a *value* (what it's worth) or a *decision* (yes/no) or a *plan* (the numbers)?**
   - Value → valuation model. Decision → appraisal. Plan → forecast/budget.
3. **Is *uncertainty / risk* the main thing I'm worried about?**
   - Yes → scenario & sensitivity model (layered on top of the base model).
4. **Is this a *special structure* (buyout, merger, financed project)?**
   - Yes → specialised model (LBO / M&A / project finance).
"""
    )

    with st.expander("🔑 Concept — Models are layered, not mutually exclusive"):
        st.markdown(
            """
Real analysis often **combines** models. A typical investment case:
1. Build a **three-statement / forecast** for the base numbers.
2. Run an **NPV/IRR appraisal** on the project cash flows.
3. Add **scenario & sensitivity** analysis to test the risks.

Choosing "the right model" often means choosing the right **primary** model — then layering others on top.
"""
        )

    with st.expander("🔑 Concept — Match the effort to the decision"):
        st.markdown(
            """
Don't build a 20-tab LBO model to decide on a €5k purchase. **Model complexity should match the size
and reversibility of the decision.** A quick back-of-envelope (payback, break-even) is often the
*right* model for small or urgent decisions — the FAST principle "Appropriate" from Module 0.2.
"""
        )

    with st.expander("🔑 Concept — The cost of the wrong model"):
        st.markdown(
            """
Using the wrong model doesn't just waste time — it produces **confident but irrelevant answers**.
Examples:
- Using a P&L forecast to make an investment decision (ignores the time value of money → overstates returns).
- Using a single-point valuation when the real issue is risk (hides the range that actually matters).

The wrong model can be more dangerous than no model, because it *looks* authoritative.
"""
        )

    st.success(
        "**Takeaway:** Choosing the right model is a skill in itself. Start from the question, use the "
        "four narrowing questions, match effort to the decision, and layer models when needed."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Examples — Matching questions to models")
    st.markdown("Four real business questions, each walked through to the right model choice.")

    with st.container():
        st.markdown("#### Example 1 — *'Should we buy this €6m automation line?'*")
        st.markdown(
            """
- **Whole company or single project?** → Single project.
- **Value, decision, or plan?** → A **decision** (invest or not).
- **Time value of money matters?** → Yes — savings arrive over 8 years.

✅ **Right model: Investment Appraisal (NPV / IRR)** — Module 4.1/4.3. Discount the future savings and
compare to the €6m today.
"""
        )

    with st.container():
        st.markdown("#### Example 2 — *'What should next year's factory budget be?'*")
        st.markdown(
            """
- **Whole company or single project?** → Whole operation.
- **Value, decision, or plan?** → A **plan** (the numbers themselves).

✅ **Right model: Forecasting / Budget Model** — Module 2.x. Driver-based volume × price and cost build-up.
"""
        )

    with st.container():
        st.markdown("#### Example 3 — *'What is our business worth if we sell it?'*")
        st.markdown(
            """
- **Whole company or single project?** → Whole company.
- **Value, decision, or plan?** → A **value**.

✅ **Right model: Valuation (DCF + Comps)** — Module 3.1/3.2. Discount future free cash flows and
cross-check with market multiples.
"""
        )

    with st.container():
        st.markdown("#### Example 4 — *'How risky is our profit if raw material prices spike?'*")
        st.markdown(
            """
- Is **uncertainty** the main concern? → Yes.

✅ **Right model: Scenario & Sensitivity** — Module 5.1/5.2, layered on the existing P&L. Flex the COGS
assumption and read the profit range.
"""
        )

    st.info(
        "**Notice the pattern:** in every case we answered the *narrowing questions* first, and the model "
        "chose itself. That discipline is the whole skill of this module."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — The Model-Selector Wizard")
    st.markdown(
        "Answer the questions below and the wizard will recommend your **primary model** — just like the "
        "decision tree in the Theory tab."
    )

    scope = st.radio(
        "**Q1 — What are you analysing?**",
        ["— Select —",
         "The whole company / operation",
         "A single project, asset, or one-off decision",
         "A special deal (buyout, merger, financed project)"],
    )

    recommendation = None
    reason = None

    if scope == "A special deal (buyout, merger, financed project)":
        recommendation = "Specialised Model (LBO / M&A / Project Finance)"
        reason = "Special structures need bespoke models for financing, returns, and synergies."

    elif scope == "A single project, asset, or one-off decision":
        goal = st.radio(
            "**Q2 — What do you need to decide?**",
            ["— Select —",
             "Whether the investment is worth it (yes/no)",
             "How risky the outcome is / what if assumptions change"],
        )
        if goal == "Whether the investment is worth it (yes/no)":
            recommendation = "Investment Appraisal (NPV / IRR)"
            reason = "A single invest/don't-invest decision with cash flows over time → discount them and test NPV/IRR."
        elif goal == "How risky the outcome is / what if assumptions change":
            recommendation = "Scenario & Sensitivity Model"
            reason = "When uncertainty is the main concern, layer scenario/sensitivity analysis on the base case."

    elif scope == "The whole company / operation":
        need = st.radio(
            "**Q2 — What do you need?**",
            ["— Select —",
             "A value — what the business is worth",
             "A plan — next period's projected numbers",
             "An integrated view of P&L, balance sheet & cash flow"],
        )
        if need == "A value — what the business is worth":
            recommendation = "Valuation Model (DCF / Comps)"
            reason = "Valuing a whole company → discount its future free cash flows and cross-check with multiples."
        elif need == "A plan — next period's projected numbers":
            recommendation = "Forecasting / Budget Model"
            reason = "Planning the numbers themselves → a driver-based forecast/budget model."
        elif need == "An integrated view of P&L, balance sheet & cash flow":
            recommendation = "Three-Statement Model"
            reason = "A complete financial picture that ties all three statements together."

    if recommendation:
        model = next((m for m in MODELS if m["name"] == recommendation), None)
        st.success(f"### 👉 Recommended model: **{recommendation}**")
        st.markdown(f"**Why:** {reason}")
        if model:
            colA, colB = st.columns(2)
            colA.markdown(f"**📘 Where to learn it:** {model['module']}")
            colB.markdown(f"**📊 Typical outputs:** {model['outputs']}")
            st.markdown(f"**✅ Use it when:** {model['use_when']}")
    elif scope != "— Select —":
        st.info("👆 Answer the follow-up question above to get your recommendation.")
    else:
        st.info("Start by selecting what you're analysing in Q1.")

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Model Reference Explorer")
    st.markdown("Filter the full library of models by the kind of question you're asking.")

    keyword = st.text_input("🔍 Describe your question or keyword (e.g. 'worth', 'invest', 'risk', 'budget')", "").strip().lower()

    filtered = MODELS
    if keyword:
        filtered = [
            m for m in MODELS
            if keyword in m["question"].lower()
            or keyword in m["use_when"].lower()
            or keyword in m["name"].lower()
            or keyword in m["outputs"].lower()
        ]

    if filtered:
        ref_df = pd.DataFrame(
            [
                {"Model": m["name"], "Answers": m["question"],
                 "Use when": m["use_when"], "Outputs": m["outputs"], "Module": m["module"]}
                for m in filtered
            ]
        )
        st.dataframe(ref_df, use_container_width=True, hide_index=True)
    else:
        st.warning("No models match that keyword. Try 'value', 'invest', 'risk', 'plan', or 'deal'.")

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The wrong model chosen (a cautionary tale)", expanded=True):
        st.markdown(
            """
**Situation:** A team needed to decide whether to invest €6m in new equipment. They built a detailed
5-year **P&L forecast**, saw rising profits, and recommended "yes".

**What went wrong:** A P&L forecast ignores the **time value of money** and the upfront cash outlay
timing. It showed accounting profit but never answered *"does this create value versus the €6m spent
today?"* — that needs an **NPV/IRR appraisal**.

**Right model:** Investment Appraisal (Module 4). When re-run properly, the discounted return was far
thinner than the P&L implied.

**Lesson:** The right model for an *investment decision* is an appraisal — not a profit forecast.
"""
        )

    with st.expander("Case B — Layering models for a full investment case"):
        st.markdown(
            """
**Situation:** A factory transformation (like a major Capex + productivity project) required a robust
business case for the board.

**How the right models combined:**
1. **Forecast model** — projected the new cost base and savings.
2. **NPV/IRR appraisal** — tested whether the investment created value.
3. **Scenario & sensitivity** — stress-tested savings, timing, and inflation.

**Result:** A layered, credible case that survived tough board questions because each question had the
*right* model behind it.

**Lesson:** Big decisions rarely use one model — they use the right *combination*, chosen deliberately.
"""
        )

    with st.expander("Case C — Matching effort to the decision (the quick model)"):
        st.markdown(
            """
**Situation:** An urgent decision on a €15k tooling spend, needed the same afternoon.

**The right choice:** Not a full three-statement model — a quick **payback / break-even** calculation.
It answered the question in minutes and was entirely *appropriate* to the decision's size.

**Lesson:** Choosing the right model also means choosing the right *level of effort*. Over-modeling a
small decision is itself a mistake.
"""
        )

    st.info(
        "🔗 **Pattern:** The right-model skill shows up as *speed and credibility* — the analysis answers "
        "exactly the question asked, at the right depth, and stands up to scrutiny."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_05"):
        q1 = st.radio(
            "**1.** The golden principle of model selection is:",
            [
                "Always use the most sophisticated model available",
                "The business question determines the model, not the other way around",
                "Pick the model you know best and adapt the question to it",
                "Always start with a full three-statement model",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** You must decide whether to invest €6m in a machine that saves cash over 8 years. The right model is:",
            [
                "A P&L forecast only",
                "Investment Appraisal (NPV / IRR)",
                "A comparable-company valuation",
                "An LBO model",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The question 'What is our company worth if we sell it?' calls for a:",
            [
                "Budget model",
                "Break-even analysis",
                "Valuation model (DCF / Comps)",
                "Sensitivity table",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** When *uncertainty and risk* are your main concern, you should:",
            [
                "Ignore it — models can't handle risk",
                "Layer a scenario & sensitivity model on top of your base case",
                "Switch to a valuation model",
                "Use a bigger discount rate and stop there",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** 'Match the effort to the decision' means:",
            [
                "Always build the most detailed model possible",
                "Model complexity should match the size and reversibility of the decision",
                "Only senior staff may build models",
                "Small decisions never need any analysis",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The business question determines the model, not the other way around"),
            "2": (q2, "Investment Appraisal (NPV / IRR)"),
            "3": (q3, "Valuation model (DCF / Comps)"),
            "4": (q4, "Layer a scenario & sensitivity model on top of your base case"),
            "5": (q5, "Model complexity should match the size and reversibility of the decision"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've completed Part 0! You're ready to start building models in Part 1. 🎉")
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
    f"Applied Financial Models · Module 0.5 Choosing the Right Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
