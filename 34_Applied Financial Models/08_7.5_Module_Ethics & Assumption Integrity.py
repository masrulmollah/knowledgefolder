"""
================================================================================
APPLIED FINANCIAL MODELS
Module 7.5 — ETHICS & ASSUMPTION INTEGRITY
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
the ethics of modelling: recognising bias and over-optimism, maintaining
assumption integrity, and being transparent with stakeholders.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a bias / integrity self-assessment + red-flag scanner)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_7_5_Ethics_and_Assumption_Integrity.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="7.5 Ethics & Assumption Integrity — Applied Financial Models",
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
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Control Panel")
st.sidebar.caption("Part 7 · From Model to Decision")
st.sidebar.markdown(
    """
**Module 7.5 — Ethics & Assumption Integrity**

🟢 *Foundational*

**You will learn to:**
- Recognise bias & over-optimism
- Maintain assumption integrity
- Be transparent with stakeholders
- Model honestly under pressure
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for an integrity self-assessment "
    "and an ethical red-flag scanner."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎯 7.5 · Ethics & Assumption Integrity")
st.markdown(
    """
A financial model is a tool of **influence** — it shapes decisions worth millions and affects jobs,
investors and communities. That power carries a duty: to model **honestly**. The most dangerous modelling
errors aren't formula mistakes — they're **biased assumptions** dressed up as objective analysis.

This final module of the course covers the ethics of modelling: recognising **bias and over-optimism**,
protecting **assumption integrity**, and being **transparent** with the people who rely on your work.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "7.5")
c2.metric("Part", "7 — Decision")
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
### Why ethics matters in modelling
Models look objective — rows of numbers and formulas — but every model embeds **human choices** about
assumptions. Those choices can be honest, or they can be (consciously or not) **bent** to produce a
desired answer. Because decision-makers trust the apparent objectivity, biased models are especially dangerous.
"""
    )

    st.markdown("### Common biases that corrupt models")
    biases = pd.DataFrame(
        {
            "Bias": ["Optimism / over-confidence", "Confirmation bias", "Anchoring",
                     "Advocacy bias", "Survivorship bias"],
            "How it shows up in a model": [
                "Best-case assumptions treated as base case; risks understated",
                "Only evidence supporting the desired answer is included",
                "Assumptions cling to an initial number or last year's figure",
                "The model is 'reverse-engineered' to justify a decision already made",
                "Only successes are used as comparables; failures ignored",
            ],
        }
    )
    st.table(biases)

    with st.expander("🔑 Concept 1 — Over-optimism (the most common sin)"):
        st.markdown(
            """
The single most frequent integrity failure is **over-optimistic assumptions**: hockey-stick growth,
best-case margins, understated costs, ignored risks. It's often unintentional — people who want a project
to happen naturally lean optimistic. The defence is **discipline**: base cases built on evidence, explicit
worst cases, and independent challenge.
"""
        )

    with st.expander("🔑 Concept 2 — Reverse-engineering (advocacy bias)"):
        st.markdown(
            """
The gravest ethical breach: **deciding the answer first, then building a model to justify it** — tweaking
assumptions until the NPV turns positive. This isn't analysis; it's advocacy disguised as objectivity. A
model exists to *inform* a decision, not to *rubber-stamp* one. If you catch yourself adjusting inputs to
'get to yes', stop.
"""
        )

    with st.expander("🔑 Concept 3 — Transparency with stakeholders"):
        st.markdown(
            """
Integrity means the people relying on your model can **see and challenge** what's inside it:
- **Disclose key assumptions** and their basis (an assumption log).
- **Show the range**, not just a single point — including the downside.
- **Flag the uncertainties** and what could go wrong.
- **Don't hide** inconvenient results or bury caveats in footnotes.

Transparency lets decision-makers weigh the analysis properly — and protects you if things don't go to plan.
"""
        )

    with st.expander("🔑 Concept 4 — Avoiding false precision"):
        st.markdown(
            """
Presenting *"NPV = €4,382,911"* implies a certainty the assumptions can't support — an ethical issue, not
just a stylistic one, because it **misleads** the reader about how reliable the number is. Present a
**range** and be honest about the confidence level. Precision should reflect genuine certainty, not
manufacture it.
"""
        )

    with st.expander("🔑 Concept 5 — Modelling under pressure"):
        st.markdown(
            """
Pressure to deliver a 'good' answer — from a boss, a sponsor, a deadline — is where integrity is tested.
Protect yourself and the decision:
- Keep the **base case honest**, whatever the pressure.
- Show the sponsor's optimistic view *as a scenario*, clearly labelled — not as the base.
- **Document** your assumptions and their sources.
- Raise concerns professionally; your job is to inform, not to please.

Your long-term credibility is worth more than any single approval.
"""
        )

    st.success(
        "**Takeaway:** Models embed human choices, so integrity matters. Guard against over-optimism and "
        "reverse-engineering, be transparent about assumptions and ranges, avoid false precision, and keep "
        "the base case honest under pressure. Model to inform, never to mislead."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Honest vs. biased modelling")
    st.markdown("The same project modelled two ways — one with integrity, one 'reverse-engineered' to a 'yes'.")

    st.markdown("#### ❌ The biased version (built to justify approval)")
    st.markdown(
        """
| Assumption | Value | Problem |
|---|---|---|
| Revenue growth | 25%/yr | Hockey-stick, no evidence |
| Margins | Best-ever, held forever | Ignores competition & inflation |
| Costs | Understated | Omits contingency & overruns |
| Risks / worst case | Not shown | Downside hidden |
| Presentation | "NPV = €3,150,000" | False precision, single point |

*Result: a confident €3.15m NPV — engineered, not analysed.*
"""
    )

    st.markdown("#### ✅ The honest version (built to inform)")
    st.markdown(
        """
| Assumption | Value | Why |
|---|---|---|
| Revenue growth | 8%/yr (base), sourced to market data | Evidence-based |
| Margins | Realistic, gently eroding | Reflects competition/inflation |
| Costs | Include contingency | Prudent |
| Risks / worst case | **Shown: −€1.2m worst case** | Transparent downside |
| Presentation | "NPV ≈ €0.4m (range −€1.2m to +€2.4m)" | Honest range |
"""
    )

    e1, e2 = st.columns(2)
    e1.metric("Biased 'NPV'", "€3,150,000", "engineered", delta_color="inverse")
    e2.metric("Honest NPV", "≈ €400,000", "with −€1.2m downside shown")

    st.info(
        "**Insight:** The biased model wasn't *wrong* in its arithmetic — it was **dishonest in its "
        "assumptions**, producing an NPV ~8× the credible figure and hiding a serious downside. The honest "
        "version still supports the project (positive base case), but lets the board decide with **eyes "
        "open** to the risk. **Integrity doesn't mean pessimism — it means truthfulness, including about the "
        "downside.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Modelling Integrity Self-Assessment")
    st.markdown("Tick the integrity practices your analysis follows. The meter rates how honest & transparent it is.")

    practices = [
        ("Base case is built on evidence, not best-case hopes", 18),
        ("Assumptions are documented with their sources (assumption log)", 16),
        ("The downside / worst case is shown, not hidden", 18),
        ("Results are presented as a range, not false-precision single points", 12),
        ("The model informs the decision (not reverse-engineered to a 'yes')", 20),
        ("Caveats & uncertainties are stated clearly, not buried", 16),
    ]

    left, right = st.columns([0.55, 0.45])
    states = []
    with left:
        st.markdown("##### ✅ Integrity checklist")
        for i, (label, w) in enumerate(practices):
            states.append(st.checkbox(f"{label}  _(+{w})_", value=(i < 2), key=f"int_{i}"))

    with right:
        score = sum(w for (l, w), s in zip(practices, states) if s)
        st.markdown("##### 🧭 Integrity meter")
        st.progress(score / 100)
        st.metric("Integrity score", f"{score} / 100")

        if score >= 90:
            grade, box = "A — High integrity", st.success
            msg = "An honest, transparent analysis a stakeholder can trust."
        elif score >= 70:
            grade, box = "B — Mostly sound", st.info
            msg = "Good, but close the gaps to be fully transparent."
        elif score >= 50:
            grade, box = "C — At risk", st.warning
            msg = "Integrity gaps could mislead decision-makers — address them."
        else:
            grade, box = "D — Not trustworthy", st.error
            msg = "This analysis risks misleading stakeholders. Rebuild with integrity."
        box(f"**Grade: {grade}** — {msg}")

    missing = [l for (l, w), s in zip(practices, states) if not s]
    st.markdown("##### 🔍 Integrity gaps to close")
    if missing:
        for m in missing:
            st.markdown(f"- ❌ {m}")
    else:
        st.markdown("- ✅ All integrity practices in place — an honest, transparent model.")

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Ethical Red-Flag Scanner")
    st.markdown("Describe a modelling situation and see whether it raises an ethical red flag.")

    situation = st.selectbox(
        "Which best describes your situation?",
        [
            "— Select —",
            "My sponsor asked me to 'adjust the assumptions until the NPV is positive'.",
            "I built a base case on market data and showed the worst case too.",
            "I used only the successful competitors as comparables.",
            "I presented the result as a range with the key assumptions listed.",
            "I left the downside scenario out because it 'might worry the board'.",
            "I labelled the optimistic sponsor view clearly as a separate scenario.",
        ],
    )

    verdicts = {
        "My sponsor asked me to 'adjust the assumptions until the NPV is positive'.":
            ("error", "🚩 **Red flag — reverse-engineering.** This is advocacy, not analysis. Keep the base "
                      "case honest; show the sponsor's view as a clearly-labelled optimistic scenario instead."),
        "I built a base case on market data and showed the worst case too.":
            ("success", "✅ **Good practice.** Evidence-based base case + visible downside = integrity."),
        "I used only the successful competitors as comparables.":
            ("error", "🚩 **Red flag — survivorship bias.** Ignoring failed comparables flatters the analysis. "
                      "Include the full, representative peer set."),
        "I presented the result as a range with the key assumptions listed.":
            ("success", "✅ **Good practice.** A range plus disclosed assumptions is honest and transparent."),
        "I left the downside scenario out because it 'might worry the board'.":
            ("error", "🚩 **Red flag — hiding inconvenient results.** The board needs the downside to decide "
                      "properly. Never omit it; that's a transparency breach."),
        "I labelled the optimistic sponsor view clearly as a separate scenario.":
            ("success", "✅ **Good practice.** Showing an optimistic case *as a labelled scenario* (not the "
                        "base) is transparent and honest."),
    }

    if situation != "— Select —":
        kind, msg = verdicts[situation]
        (st.success if kind == "success" else st.error)(msg)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Score yourself:** Tick only the practices you *genuinely* follow on your last real model. Honest score?
2. **Fix a gap:** Pick one unticked item and write down how you'd address it next time.
"""
        )
    with e2:
        st.markdown(
            """
3. **Scan the situations:** Which red-flag scenarios have you seen at work? How were they handled?
4. **Pressure test:** How would you respond if asked to 'get to yes'? Draft a professional reply.
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The reverse-engineered business case", expanded=True):
        st.markdown(
            """
**Situation:** A sponsor, determined to win approval, pushed the analyst to keep 'adjusting' assumptions
until the NPV turned positive.

**The ethical response:** The analyst kept the **base case honest** (evidence-based), and presented the
sponsor's optimistic view as a **clearly-labelled scenario** — not the base. The board saw both and could
weigh them properly.

**Why it matters:** Reverse-engineering a model to a predetermined answer betrays the decision-makers who
trust it — and destroys the analyst's credibility when reality diverges.

**Lesson:** Never bend the base case to 'get to yes'. Show optimism as a labelled scenario, honestly.
"""
        )

    with st.expander("Case B — Over-optimism that came home to roost"):
        st.markdown(
            """
**Situation:** A project was approved on a hockey-stick forecast (25% growth) that everyone quietly knew
was a stretch.

**What happened:** Growth came in near the market rate (~8%); the project badly missed its case, capital
was misallocated, and trust in the finance team's forecasts suffered for years.

**Why it matters:** Over-optimism isn't harmless — it leads to real capital being wasted on projects that
were never going to deliver.

**Lesson:** An honest, lower forecast that proves right beats an optimistic one that fails — every time.
"""
        )

    with st.expander("Case C — Transparency that built lasting trust"):
        st.markdown(
            """
**Situation:** An analyst consistently presented ranges, disclosed assumptions, and flagged the downside —
even when it made cases look less exciting.

**What happened:** Over time, the board came to **trust that analyst's numbers implicitly**, because they
were never blindsided. That credibility became the analyst's most valuable professional asset.

**Why it matters:** Integrity compounds. Being trusted to tell the truth — good or bad — is the foundation
of a finance professional's influence and career.

**Lesson:** Transparency may cost you a 'win' occasionally, but it builds the trust that makes you
genuinely influential.
"""
        )

    st.info(
        "🔗 **Pattern:** Ethical modelling protects both the decision *and* the modeller. Honesty about "
        "assumptions, downside and uncertainty is not weakness — it's the source of durable credibility."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_75"):
        q1 = st.radio(
            "**1.** The most dangerous modelling errors are usually:",
            [
                "Small formula typos",
                "Biased assumptions dressed up as objective analysis",
                "Formatting inconsistencies",
                "Using too few decimal places",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** 'Reverse-engineering' a model means:",
            [
                "Building it from the outputs backwards for efficiency",
                "Deciding the answer first, then tweaking assumptions to justify it",
                "Auditing the formulas",
                "Stress-testing the inputs",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The most common integrity failure in modelling is:",
            [
                "Over-pessimism",
                "Over-optimism (hockey-stick growth, understated risks)",
                "Too many error checks",
                "Excessive transparency",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Transparency with stakeholders means:",
            [
                "Hiding the downside so they aren't worried",
                "Disclosing key assumptions, showing the range, and flagging uncertainties",
                "Presenting a single precise number only",
                "Only sharing the best-case scenario",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** If a sponsor pressures you to 'adjust assumptions until the NPV is positive', you should:",
            [
                "Comply to keep them happy",
                "Keep the base case honest and present their optimistic view as a clearly-labelled scenario",
                "Delete the worst case",
                "Add false precision to look confident",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Biased assumptions dressed up as objective analysis"),
            "2": (q2, "Deciding the answer first, then tweaking assumptions to justify it"),
            "3": (q3, "Over-optimism (hockey-stick growth, understated risks)"),
            "4": (q4, "Disclosing key assumptions, showing the range, and flagging uncertainties"),
            "5": (q5, "Keep the base case honest and present their optimistic view as a clearly-labelled scenario"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Outstanding — you've completed the ENTIRE Applied Financial Models course! 🎓🎉")
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

        if score >= 3:
            st.markdown("---")
            st.markdown(
                "### 🎓 Congratulations!\n"
                "You've reached the final module of **Applied Financial Models**. You can now **understand, "
                "build, interpret and ethically communicate** financial models — from the three statements "
                "and forecasting, through valuation, investment appraisal, risk and specialised models, all "
                "the way to turning analysis into trusted decisions. **Well done!**"
            )

st.markdown("---")
st.caption(
    f"Applied Financial Models · Module 7.5 Ethics & Assumption Integrity · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
