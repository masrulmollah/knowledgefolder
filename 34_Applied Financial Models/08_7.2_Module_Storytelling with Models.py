"""
================================================================================
APPLIED FINANCIAL MODELS
Module 7.2 — STORYTELLING WITH MODELS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to translate model outputs into a compelling executive narrative: structure,
the "so what?", plain language, and audience-appropriate framing.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live narrative / executive-summary builder)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_7_2_Storytelling_with_Models.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="7.2 Storytelling with Models — Applied Financial Models",
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
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 7 · From Model to Decision")
st.sidebar.markdown(
    """
**Module 7.2 — Storytelling with Models**

🟡 *Intermediate*

**You will learn to:**
- Structure a persuasive financial narrative
- Lead with the recommendation (BLUF)
- Translate jargon into plain language
- Tailor the story to the audience
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build an executive summary "
    "from your model outputs — and translate the jargon."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎯 7.2 · Storytelling with Models")
st.markdown(
    """
A brilliant model that nobody understands changes nothing. **Storytelling** is how you turn analysis into
**action** — translating the numbers into a clear, persuasive narrative that decision-makers can grasp in
minutes and act on with confidence.

This module covers the structure of a compelling financial story, the discipline of **leading with the
recommendation**, translating **jargon into plain language**, and tailoring the message to your **audience**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "7.2")
c2.metric("Part", "7 — Decision")
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
### Why storytelling matters
Executives don't have time to trace a 20-tab model. They need the **story**: what you found, why it
matters, and what to do. Your analytical credibility only creates value if it's **communicated** in a way
that drives a decision.
"""
    )

    st.markdown("### The classic narrative structure (SCR)")
    scr = pd.DataFrame(
        {
            "Element": ["Situation", "Complication / Analysis", "Resolution / Recommendation"],
            "What it covers": [
                "The context — why we're looking at this",
                "What the model shows — the key findings, drivers and risks",
                "The recommended action and what it delivers",
            ],
            "Example": [
                "\"We're deciding whether to invest €6m in automation.\"",
                "\"The model shows an NPV of +€400k, driven by labour savings, but it's sensitive to volume.\"",
                "\"Recommend we proceed, subject to protecting volume with the X contract.\"",
            ],
        }
    )
    st.table(scr)

    with st.expander("🔑 Concept 1 — Lead with the answer (BLUF)"):
        st.markdown(
            """
**BLUF = Bottom Line Up Front.** Don't build suspense — executives want the conclusion *first*, then the
support. Open with the recommendation:

> *"We recommend approving the €6m investment: it creates ~€400k of value with an acceptable, survivable
> downside."*

…then provide the evidence. Leading with the answer respects the reader's time and frames everything that
follows.
"""
        )

    with st.expander("🔑 Concept 2 — One message, three supports"):
        st.markdown(
            """
A strong financial story has **one central message** supported by **~three** key points — no more (people
don't retain more). For an investment:
1. **It creates value** (NPV/IRR).
2. **Here's the main risk** (the key driver / downside).
3. **Here's how we manage it** (the mitigation).

Ruthlessly cut everything that doesn't support the central message.
"""
        )

    with st.expander("🔑 Concept 3 — Translate jargon into plain language"):
        st.markdown(
            """
Finance jargon alienates non-specialists. Translate:
- *"Positive NPV"* → *"creates value / worth more than it costs"*
- *"IRR exceeds WACC"* → *"the return beats our cost of money"*
- *"High operating leverage"* → *"profits swing sharply with sales"*
- *"Accretive"* → *"increases earnings per share"*

Keep the precise term available for those who want it, but **lead with the plain-English meaning**.
"""
        )

    with st.expander("🔑 Concept 4 — Know your audience"):
        st.markdown(
            """
Tailor the story to who's listening:
- **Board / CEO:** value, strategic fit, risk, one number. Minimal detail.
- **CFO / finance:** the drivers, assumptions, sensitivities.
- **Operations:** what it means for volumes, capacity, jobs.

Same model, different story. Match the depth, language and emphasis to the audience's needs and decision.
"""
        )

    with st.expander("🔑 Concept 5 — Show, don't drown (visuals)"):
        st.markdown(
            """
A single well-chosen chart beats a table of 200 numbers:
- A **bridge/waterfall** to explain a change.
- A **tornado** to show what drives the result.
- A **scenario range** to show the downside.

Use visuals to make the message *instant*; put the detailed numbers in an appendix for those who ask.
"""
        )

    st.success(
        "**Takeaway:** Storytelling turns analysis into action. Lead with the recommendation (BLUF), build "
        "one message on ~three supports, translate jargon into plain language, tailor to the audience, and "
        "let a clear visual carry the message."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — From model to executive summary")
    st.markdown("Turning the same raw outputs into a story an executive can act on.")

    st.markdown("#### ❌ The 'data dump' (what NOT to do)")
    st.markdown(
        """
> *"The DCF produces an NPV of €402,311 at a 10% WACC with a terminal growth of 2.5%. The IRR is 11.8%.
> Sensitivity analysis shows a ±10% price move swings NPV by €758k. The worst-case scenario NPV is
> −€1.2m. Operating margin declines from 20% to 14%. Payback is 5.0 years, discounted payback 7.3 years…"*

**Problem:** All true, all precise — and almost **useless** to a busy executive. No recommendation, no
priority, no 'so what?'. They can't act on it.
"""
    )

    st.markdown("#### ✅ The executive story (BLUF + SCR)")
    st.markdown(
        """
> **Recommendation: Approve the €6m automation investment — with one condition.**
>
> **Situation:** We can invest €6m to automate the packing line and cut labour cost.
>
> **What the analysis shows:**
> - ✅ **It creates value** — about €400k in today's money, earning ~12% vs. our 10% cost of capital.
> - ⚠️ **The main risk is volume/price** — if sales fall materially, the return disappears (worst case: a
>   €1.2m loss).
> - 🛡️ **We can manage it** — securing the X supply contract protects the volumes the case depends on.
>
> **Recommendation:** Proceed, conditional on signing the X contract first. Payback is ~5 years, within
> our threshold.
"""
    )

    st.info(
        "**Insight:** Both versions use the *same numbers*. The first **reports**; the second **advises** — "
        "it leads with the decision, carries one clear message (create value, manage the volume risk), "
        "translates the jargon, and tells the executive exactly what to do. **That's storytelling with models.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Executive Summary Builder")
    st.markdown(
        "Enter your model's outputs and the app drafts a **BLUF + SCR** executive summary you can adapt."
    )

    left, right = st.columns([0.42, 0.58])
    with left:
        project = st.text_input("Project / decision", "€6m automation of the packing line")
        npv = st.number_input("NPV (€)", -100_000_000, 100_000_000, 400_000, 50_000)
        irr = st.number_input("IRR (%)", -50.0, 100.0, 12.0, 0.5)
        hurdle = st.number_input("Hurdle rate (%)", 0.0, 50.0, 10.0, 0.5)
        payback = st.number_input("Payback (years)", 0.0, 30.0, 5.0, 0.5)
        key_driver = st.selectbox("Main risk / driver",
                                  ["volume", "price", "input costs", "execution", "demand"])
        worst_case = st.number_input("Worst-case outcome (€)", -500_000_000, 100_000_000, -1_200_000, 50_000)
        mitigation = st.text_input("Proposed mitigation", "securing the X supply contract")

    with right:
        verb = "Approve" if npv > 0 else "Do not approve"
        value_phrase = (f"creates about {money(npv)} of value" if npv > 0
                        else f"destroys about {money(-npv)} of value")
        beats = "beats" if irr > hurdle else "falls short of"

        summary = f"""**Recommendation: {verb} {project}.**

**Situation.** We are deciding whether to proceed with {project}.

**What the analysis shows.**
- {'✅' if npv > 0 else '❌'} **It {value_phrase}** — an IRR of ~{irr:.0f}% that {beats} our {hurdle:.0f}% cost of capital.
- ⚠️ **The main risk is {key_driver}** — if it moves against us, the return weakens (worst case: {money(worst_case)}).
- 🛡️ **We can manage it** by {mitigation}.

**Recommendation.** {'Proceed' if npv > 0 else 'Hold'}{' , conditional on ' + mitigation if npv > 0 else ''}. \
Payback is about {payback:.1f} years."""

        st.markdown("##### 📝 Draft executive summary")
        st.markdown(summary)
        st.download_button(
            "⬇️ Download the summary (Markdown)",
            summary.encode("utf-8"),
            "executive_summary.md",
            "text/markdown",
        )

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Jargon Translator")
    st.markdown("Pick a piece of finance jargon and see how to say it in plain, executive-friendly language.")

    jargon = {
        "Positive NPV": "It creates value — it's worth more than it costs in today's money.",
        "IRR exceeds WACC": "The return beats our cost of money, so it's worth doing.",
        "High operating leverage": "Profits swing sharply with sales — great on the way up, painful on the way down.",
        "EPS accretive": "It increases our earnings per share.",
        "Terminal value dominates the DCF": "Most of the value depends on assumptions far in the future, so it's less certain.",
        "Thin margin of safety": "We're operating close to break-even — little room for error.",
        "DSCR above covenant": "The project generates comfortably more than enough cash to cover its debt payments.",
        "Working capital release": "We free up cash that's currently tied up in stock and unpaid invoices.",
    }
    pick = st.selectbox("Finance term", list(jargon.keys()))
    st.success(f"**Plain English:** {jargon[pick]}")
    st.caption("🧠 Keep the technical term for the specialists, but always lead with the plain-English meaning.")

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Flip the verdict:** Set NPV negative. Watch the summary switch from 'Approve/Proceed' to 'Hold'.
2. **Audience test:** Rewrite the generated summary in one sentence for a CEO with 30 seconds.
"""
        )
    with e2:
        st.markdown(
            """
3. **Change the risk:** Switch the main driver and see how the story's emphasis changes.
4. **De-jargon a report:** Take a real sentence from a finance report and translate it to plain English.
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The BLUF that won approval", expanded=True):
        st.markdown(
            """
**Situation:** A strong investment case kept getting deferred because presentations buried the conclusion
under detail.

**What storytelling fixed:** Re-opening with a one-line **BLUF** — *"Recommend approving; it creates €400k
of value with a manageable, contract-protected downside"* — gave the board the answer immediately. The
detail then *supported* a decision rather than delaying it. It was approved.

**Why it matters:** The analysis hadn't changed — only the *delivery*. Leading with the answer unlocked
the decision.

**Lesson:** Put the recommendation first; detail second.
"""
        )

    with st.expander("Case B — Plain language across the boardroom"):
        st.markdown(
            """
**Situation:** A finance team presented an M&A case full of 'accretion', 'WACC' and 'synergies' to a
board that included non-finance directors.

**What storytelling fixed:** Translating to plain language — *"the deal increases our earnings per share
and the return beats our cost of money"* — got everyone on the same page. Engagement and the quality of
questions improved dramatically.

**Why it matters:** Jargon excludes; plain language includes. A decision needs the *whole* room to understand.

**Lesson:** Translate jargon — lead with meaning, keep the technical term for those who want it.
"""
        )

    with st.expander("Case C — One chart that told the whole story"):
        st.markdown(
            """
**Situation:** A risk analysis spanned dozens of scenarios in a dense table nobody could read.

**What storytelling fixed:** A single **scenario-range chart** (worst / base / best NPV) instantly showed
the decision-makers the upside, the base case, and — crucially — the survivable downside. The table moved
to an appendix.

**Why it matters:** A well-chosen visual makes the message *instant*; a raw table hides it.

**Lesson:** Show, don't drown — let one clear chart carry the headline, and keep the detail on tap.
"""
        )

    st.info(
        "🔗 **Pattern:** The best analysts are translators. They lead with the recommendation, build one "
        "clear message, speak plain language, tailor to the audience, and let a single visual make the point."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_72"):
        q1 = st.radio(
            "**1.** 'BLUF' in financial storytelling means:",
            [
                "Build Long Under-explained Forecasts",
                "Bottom Line Up Front — lead with the recommendation",
                "Basic Ledger Under Finance",
                "Bury Learnings Until Final",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** A good financial narrative typically has:",
            [
                "One central message supported by ~three key points",
                "As many points as possible",
                "No recommendation",
                "Only raw data tables",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The SCR structure stands for:",
            [
                "Sales, Costs, Returns",
                "Situation, Complication/analysis, Resolution/recommendation",
                "Summary, Chart, References",
                "Scenario, Cash, Ratio",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Translating 'positive NPV' into plain language, you'd say:",
            [
                "It has a high internal rate of return",
                "It creates value — it's worth more than it costs",
                "It is EPS accretive",
                "It reduces the discount rate",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Why tailor the same model's story to different audiences?",
            [
                "To make the model bigger",
                "Because a board, the CFO, and operations each need different depth, language and emphasis",
                "To hide the assumptions",
                "It is required by accounting standards",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Bottom Line Up Front — lead with the recommendation"),
            "2": (q2, "One central message supported by ~three key points"),
            "3": (q3, "Situation, Complication/analysis, Resolution/recommendation"),
            "4": (q4, "It creates value — it's worth more than it costs"),
            "5": (q5, "Because a board, the CFO, and operations each need different depth, language and emphasis"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you can tell a story with a model! On to Module 7.3 (Presenting to Decision-Makers). 🎉")
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
    f"Applied Financial Models · Module 7.2 Storytelling with Models · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
