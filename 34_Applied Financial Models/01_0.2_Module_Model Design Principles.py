"""
================================================================================
APPLIED FINANCIAL MODELS
Module 0.2 — MODEL DESIGN PRINCIPLES
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
HOW to structure a financial model well: the Inputs -> Calculations -> Outputs
architecture, logical flow, transparency, and the FAST standard.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live "model quality auditor")
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_0_2_Model_Design_Principles.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="0.2 Model Design Principles — Applied Financial Models",
    layout="wide",
    page_icon="🧭",
)

# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 0 · Orientation & Foundations")
st.sidebar.markdown(
    """
**Module 0.2 — Model Design Principles**

🟢 *Foundational*

**You will learn to:**
- Structure a model: Inputs → Calculations → Outputs
- Build a logical left-to-right, top-to-bottom flow
- Make models transparent & auditable
- Apply the **FAST** standard (Flexible, Appropriate, Structured, Transparent)
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to audit a model's design and "
    "watch its quality score update as you fix (or break) it."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🧭 0.2 · Model Design Principles")
st.markdown(
    """
A model can be *numerically correct* and still be *badly designed* — impossible to follow, risky to
change, and untrusted by the people who must act on it. **Design is what makes a model usable.**

This module covers the architecture and discipline behind professional models: how to separate
**inputs, calculations and outputs**, build a clean **flow**, keep everything **transparent**, and
apply the industry-recognised **FAST** standard.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "0.2")
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
### The golden architecture: Inputs → Calculations → Outputs
Every well-designed model separates three distinct zones. Mixing them is the single most common
cause of errors and mistrust.
"""
    )

    arch = pd.DataFrame(
        {
            "Zone": ["① INPUTS", "② CALCULATIONS", "③ OUTPUTS"],
            "Contains": [
                "All assumptions — the only cells a user should change",
                "The engine: formulas that link inputs together",
                "The results: statements, charts, KPIs, decisions",
            ],
            "Design rule": [
                "Hard-code ONLY here; colour-code (e.g. blue) so they're obvious",
                "No hard-coded numbers — formulas reference inputs only",
                "No new logic — outputs simply present calculation results",
            ],
        }
    )
    st.table(arch)

    st.markdown(
        """
### Logical flow: left-to-right, top-to-bottom
A reader should be able to follow a model like a book:
- **Time flows left → right** (Year 1, Year 2, … across the columns).
- **Logic flows top → bottom** (drivers → revenue → costs → profit).
- **One calculation per row**, copied consistently across all periods.
- Avoid formulas that jump around the workbook — dependencies should move forward, not backward.
"""
    )

    st.markdown("### The FAST standard")
    fast = pd.DataFrame(
        {
            "Letter": ["F", "A", "S", "T"],
            "Principle": ["Flexible", "Appropriate", "Structured", "Transparent"],
            "Meaning": [
                "Easy to change and extend without breaking; driver-based",
                "Fit for purpose — not over-engineered; right level of detail",
                "Consistent layout, logical blocks, predictable structure",
                "Simple, clear formulas anyone can follow and audit",
            ],
        }
    )
    st.table(fast)

    with st.expander("🔑 Key principle 1 — Separate inputs from calculations"):
        st.markdown(
            """
The cardinal rule. If assumptions are buried inside formulas (e.g. `=Revenue*0.6`), no one knows
`0.6` is a changeable assumption. Instead, put `60%` in a **labelled input cell** and reference it
(`=Revenue*COGS_pct`). This makes the model **flexible** and **auditable**.
"""
        )

    with st.expander("🔑 Key principle 2 — One formula per row, copied across"):
        st.markdown(
            """
Within a calculation row, the **same formula** should copy cleanly across every period. If a single
cell in the middle of a row is different, that's a red flag — it breaks consistency and hides errors.
Consistency lets a reviewer check one cell and trust the whole row.
"""
        )

    with st.expander("🔑 Key principle 3 — No hard-coding in calculations"):
        st.markdown(
            """
A hard-coded number inside a calculation (a "plug") is invisible and dangerous. Every number should
either be an **input** or the **result of a formula**. If you must include a constant, label it and
move it to the inputs zone.
"""
        )

    with st.expander("🔑 Key principle 4 — Formatting & colour-coding conventions"):
        st.markdown(
            """
Professional models use consistent visual signals so anyone can read them instantly:
- **Blue font** = inputs/assumptions (safe to change)
- **Black font** = formulas/calculations (don't touch)
- **Green font** = links to other sheets
- Consistent units, number formats, and clear labels on every row.
"""
        )

    with st.expander("🔑 Key principle 5 — Build in error checks"):
        st.markdown(
            """
Good models **check themselves**. Examples:
- A balance-sheet check (Assets − Liabilities − Equity = 0).
- Cash-flow ties to the balance sheet.
- Sensible-range flags (e.g. margin between 0–100%).

A visible "checks" row that turns red on error catches mistakes before they reach a decision-maker.
"""
        )

    st.success(
        "**Takeaway:** Correct ≠ well-designed. A professional model is Flexible, Appropriate, "
        "Structured and Transparent — so it can be trusted, changed, and audited with confidence."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Redesigning a messy model")
    st.markdown(
        "Here's the same revenue calculation built two ways. Same answer — very different quality."
    )

    st.markdown("#### ❌ Badly designed (hard-coded, opaque)")
    st.code(
        "Cell B10:  =950000*2.05*0.6      <- what are these numbers?\n"
        "Cell B11:  =950000*2.05          <- 950000 and 2.05 repeated everywhere\n"
        "Cell B12:  =B11-B10",
        language="text",
    )
    st.markdown(
        """
**Problems:**
- Assumptions (volume 950,000; price 2.05; COGS 60%) are **buried in formulas**.
- To test a price change you'd have to edit **every cell** — and you'd probably miss one.
- No labels, no colour-coding — a reviewer can't tell inputs from calculations.
"""
    )

    st.markdown("#### ✅ Well designed (structured, transparent)")
    st.markdown(
        """
| Zone | Label | Cell | Content |
|---|---|---|---|
| **INPUT** | Volume (units) | `C4` | `950,000` *(blue)* |
| **INPUT** | Price per unit | `C5` | `2.05` *(blue)* |
| **INPUT** | COGS % of revenue | `C6` | `60%` *(blue)* |
| **CALC** | Revenue | `C10` | `=C4*C5` |
| **CALC** | COGS | `C11` | `=C10*C6` |
| **CALC** | Gross Profit | `C12` | `=C10-C11` |
| **CHECK** | Margin sensible? | `C13` | `=IF(AND(C12/C10>0,C12/C10<1),"OK","ERROR")` |
"""
    )

    st.info(
        "**Why it's better:** Change price once in `C5` and the whole model updates. Anyone can trace "
        "every number to a labelled input. The **check row** flags nonsense automatically. Same maths — "
        "but now it's Flexible, Structured and Transparent."
    )

    st.markdown("#### The 60-second design checklist")
    st.markdown(
        """
1. ✅ Are **all assumptions** in one clearly-labelled inputs zone?
2. ✅ Do calculations reference inputs (no hard-coded numbers)?
3. ✅ Does time flow **left→right** and logic **top→bottom**?
4. ✅ Is there **one formula per row**, copied consistently?
5. ✅ Are inputs **colour-coded** and every row **labelled**?
6. ✅ Are there **error checks** that flag problems automatically?
"""
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — The Model Quality Auditor")
    st.markdown(
        "Toggle the design choices below to reflect how a model is built. Watch the **FAST quality "
        "score** respond in real time — and see which principles are being followed or violated."
    )

    principles = [
        ("Inputs separated from calculations", 20,
         "Assumptions live in one labelled zone, referenced by formulas.",
         "Assumptions are buried inside formulas — impossible to flex safely."),
        ("No hard-coded numbers in calculations", 20,
         "Every number is an input or a formula result.",
         "Hidden 'plugs' hard-coded inside formulas create silent errors."),
        ("Consistent one-formula-per-row layout", 15,
         "The same formula copies cleanly across every period.",
         "Inconsistent formulas across a row hide mistakes."),
        ("Logical left→right / top→bottom flow", 15,
         "Reads like a book; dependencies move forward.",
         "Formulas jump around; backward references confuse reviewers."),
        ("Colour-coding & clear labels", 10,
         "Blue inputs, black formulas; every row labelled.",
         "No visual signals — can't tell inputs from calculations."),
        ("Built-in error checks", 10,
         "Balance/range checks flag problems automatically.",
         "No self-checks — errors reach the decision-maker unnoticed."),
        ("Appropriate level of detail (not over-engineered)", 10,
         "Right granularity for the decision; not bloated.",
         "Over-engineered or too sparse for the question at hand."),
    ]

    left, right = st.columns([0.5, 0.5])
    states = []
    with left:
        st.markdown("##### 🎛️ Design choices")
        for i, (name, weight, _, _) in enumerate(principles):
            states.append(st.checkbox(f"{name}  _(+{weight})_", value=(i < 2), key=f"p_{i}"))

    with right:
        score = sum(w for (n, w, g, b), s in zip(principles, states) if s)
        st.markdown("##### 📊 FAST Quality Score")
        st.progress(score / 100)
        st.metric("Design score", f"{score} / 100")

        if score >= 90:
            grade, msg, box = "A — Professional", "Excellent, audit-ready design. Trustworthy and flexible.", st.success
        elif score >= 70:
            grade, msg, box = "B — Solid", "Good design with minor gaps. Tighten the missing principles.", st.info
        elif score >= 50:
            grade, msg, box = "C — Risky", "Usable but fragile. Several principles need fixing before others rely on it.", st.warning
        else:
            grade, msg, box = "D — Dangerous", "High error risk and low trust. Redesign before use.", st.error
        box(f"**Grade: {grade}** — {msg}")

    st.markdown("---")
    st.markdown("##### 🔍 Live design review")
    review_rows = []
    for (name, weight, good, bad), s in zip(principles, states):
        review_rows.append({
            "Principle": name,
            "Status": "✅ Followed" if s else "❌ Violated",
            "Impact": good if s else bad,
        })
    st.table(pd.DataFrame(review_rows))

    st.caption(
        "🧠 **Notice:** the two highest-weighted principles — *separating inputs* and *no hard-coding* — "
        "carry 40 of 100 points. Get those two right first; they prevent the most damaging errors."
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The €6m Capex model that couldn't be changed", expanded=True):
        st.markdown(
            """
**Situation:** An investment case for a €6m automation project hard-coded the annual savings figure
into 30+ formulas across the workbook.

**What went wrong:** When the board asked *"what if savings are 15% lower?"*, the analyst had to hunt
and edit dozens of cells live in the meeting — and missed several, giving an inconsistent answer.

**Design fix:** Move savings to a **single labelled input**. One change would have re-flowed the entire
model instantly, enabling a confident, real-time scenario in front of the board.

**Lesson:** *Flexibility* isn't a nicety — it's what lets a model survive tough questions.
"""
        )

    with st.expander("Case B — The 'London Whale': design failure with real losses"):
        st.markdown(
            """
**Situation:** A large bank's risk model contained manual copy-paste steps between spreadsheets and a
formula that divided by a *sum* instead of an *average*.

**What went wrong:** The broken, untransparent design understated risk — contributing to billions in
trading losses. No error checks caught the flaw.

**Design fix:** Automated links (no copy-paste), transparent formulas, and independent **error checks**
would have surfaced the mistake early.

**Lesson:** Poor design isn't just untidy — in the real world it can be catastrophically expensive.
"""
        )

    with st.expander("Case C — The reusable budget template (design done right)"):
        st.markdown(
            """
**Situation:** A finance team rebuilt its annual budget model around FAST principles: a clean inputs
tab, consistent one-formula-per-row calcs, colour-coding, and a checks row.

**Result:** The template became **reusable across sites and years**. New analysts learned it in hours,
scenario analysis took minutes, and errors dropped sharply because the checks row flagged them early.

**Lesson:** Good design compounds — a well-structured model pays back every time it's reused or reviewed.
"""
        )

    st.info(
        "🔗 **Pattern:** Design quality shows up precisely when a model is *stressed* — changed under "
        "pressure, reviewed by others, or reused. That's when Flexible, Structured, Transparent earns its keep."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_02"):
        q1 = st.radio(
            "**1.** The 'golden architecture' of a well-designed model separates it into:",
            [
                "Revenue, Costs, and Profit",
                "Inputs, Calculations, and Outputs",
                "Past, Present, and Future",
                "Assets, Liabilities, and Equity",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** What does the 'F' in the FAST standard stand for?",
            ["Fast", "Financial", "Flexible", "Formatted"],
            index=None,
        )
        q3 = st.radio(
            "**3.** Which practice is a design RED FLAG?",
            [
                "Assumptions in a single labelled inputs zone",
                "A hard-coded number buried inside a calculation formula",
                "One formula per row, copied across all periods",
                "A visible error-check row",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** In a well-structured model, time and logic should flow:",
            [
                "Right-to-left and bottom-to-top",
                "Left-to-right (time) and top-to-bottom (logic)",
                "Randomly, as long as the answer is correct",
                "Only within a single cell",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Why separate inputs from calculations?",
            [
                "It makes the file smaller",
                "So assumptions are visible and can be changed safely, making the model flexible and auditable",
                "It is required by tax law",
                "So the model runs faster",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Inputs, Calculations, and Outputs"),
            "2": (q2, "Flexible"),
            "3": (q3, "A hard-coded number buried inside a calculation formula"),
            "4": (q4, "Left-to-right (time) and top-to-bottom (logic)"),
            "5": (q5, "So assumptions are visible and can be changed safely, making the model flexible and auditable"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered model design principles! On to Module 0.3. 🎉")
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
    f"Applied Financial Models · Module 0.2 Model Design Principles · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
