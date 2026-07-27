"""
================================================================================
APPLIED FINANCIAL MODELS
Module 0.3 — BEST PRACTICES & GOLDEN RULES
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
the day-to-day discipline of professional modeling: formatting conventions,
colour-coding, one-formula-per-row, no-hardcoding, consistency, and error checks.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live "spot the golden-rule violation" trainer)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_0_3_Best_Practices_Golden_Rules.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="0.3 Best Practices & Golden Rules — Applied Financial Models",
    layout="wide",
    page_icon="🧭",
)

# --------------------------------------------------------------------------------
# SESSION STATE
# --------------------------------------------------------------------------------
if "bp_answered" not in st.session_state:
    st.session_state.bp_answered = {}

# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 0 · Orientation & Foundations")
st.sidebar.markdown(
    """
**Module 0.3 — Best Practices & Golden Rules**

🟢 *Foundational*

**You will learn to:**
- Apply the modeler's "golden rules"
- Use colour-coding & formatting conventions
- Keep one formula per row, copied across
- Eliminate hard-coding and hidden plugs
- Build self-checking, consistent models
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to play *Spot the Violation* — "
    "inspect real formulas and catch which golden rule is broken."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🧭 0.3 · Best Practices & Golden Rules")
st.markdown(
    """
Where Module 0.2 covered the *architecture* of a model, this module is about the **daily habits** that
separate a professional modeler from an amateur. These are the "golden rules" — small disciplines that,
applied consistently, make a model **fast to build, safe to change, easy to audit, and trusted by others**.

Master these and every model you touch — from a quick P&L to a full valuation — becomes cleaner and more reliable.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "0.3")
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
### The 10 Golden Rules of financial modeling
These rules are simple to state and powerful in practice. Together they form a professional standard.
"""
    )

    rules = pd.DataFrame(
        {
            "#": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "Golden Rule": [
                "Separate inputs, calculations & outputs",
                "Never hard-code numbers inside formulas",
                "One formula per row — copy it across consistently",
                "Colour-code: blue = inputs, black = formulas, green = links",
                "Label every row and state the units",
                "Keep formulas short & simple (break up long ones)",
                "Build time left→right, logic top→bottom",
                "Add error checks that flag problems automatically",
                "No hidden cells, circular refs (unless intended) or manual plugs",
                "Document key assumptions and sources",
            ],
            "Why it matters": [
                "Prevents the #1 source of errors and mistrust",
                "Makes every number traceable and changeable",
                "Lets a reviewer check one cell and trust the row",
                "Anyone can instantly read the model",
                "Removes ambiguity (€ vs €000s vs %)",
                "Short formulas are easier to audit and debug",
                "The model reads like a book",
                "Catches mistakes before a decision-maker sees them",
                "Eliminates invisible risk",
                "Others (and future-you) can understand it",
            ],
        }
    )
    st.table(rules)

    st.markdown("### The colour-coding convention (industry standard)")
    colours = pd.DataFrame(
        {
            "Colour": ["🔵 Blue font", "⬛ Black font", "🟢 Green font", "🔴 Red font"],
            "Means": [
                "Input / assumption — safe to change",
                "Formula / calculation — do not overtype",
                "Link to another sheet or workbook",
                "Warning / check that has failed",
            ],
            "Example": ["Growth rate = 5%", "=Revenue*COGS_pct", "='P&L'!B12", 'Balance check = "ERROR"'],
        }
    )
    st.table(colours)

    with st.expander("🔑 Rule in depth — No hard-coding ('the 0.6 problem')"):
        st.markdown(
            """
Writing `=Revenue*0.6` hides an assumption. Six months later, nobody knows what `0.6` is or whether
it's safe to change. **Fix:** put `60%` in a labelled, colour-coded input cell and reference it:
`=Revenue*COGS_pct`. Now the assumption is visible, documented, and flexible.

> **Rule of thumb:** the only place a typed number belongs is the *inputs* zone. If you see a number
> inside a calculation formula, treat it as a bug until proven otherwise.
"""
        )

    with st.expander("🔑 Rule in depth — One formula per row"):
        st.markdown(
            """
Every cell in a calculation row should contain the **same logic**, just shifted one period right.
If cell `D10` differs from `C10` and `E10`, a reviewer can't trust the row. Consistency means you
**check one cell and trust the entire row** — a huge time-saver and error-catcher.
"""
        )

    with st.expander("🔑 Rule in depth — Keep formulas short"):
        st.markdown(
            """
A monster formula like `=(A1*B1-C1)/(D1+E1)*(1+F1)-G1*H1` is impossible to audit. **Break it into
steps** across labelled rows (revenue, then cost, then margin). Short formulas are transparent;
long ones hide errors. If you can't read a formula aloud, it's too long.
"""
        )

    with st.expander("🔑 Rule in depth — Error checks that self-police"):
        st.markdown(
            """
Add a dedicated **checks area** with simple tests, e.g.:
- `Balance check: =IF(Assets-Liabilities-Equity=0,"OK","ERROR")`
- `Cash-flow tie-out`, `sum-of-parts = total`, `% within 0–100%`.

Wire these to conditional formatting so a failure turns **red**. A model that flags its own mistakes
is worth far more than one that silently hides them.
"""
        )

    st.success(
        "**Takeaway:** Golden rules aren't bureaucracy — they're speed. Consistent habits let you build "
        "faster, change safely, and hand a model to anyone with confidence."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Applying the golden rules")
    st.markdown("Watch a single calculation improve as we apply the rules one at a time.")

    st.markdown("#### 🔴 Version 1 — Breaks the rules")
    st.code(
        'B5:  =1000000*2*0.6*1.05          <- hard-coded, one giant formula, no labels',
        language="text",
    )
    st.markdown(
        "*Violations:* hard-coding (4 hidden numbers), one monster formula, no labels, no units."
    )

    st.markdown("#### 🟠 Version 2 — Separate the inputs")
    st.code(
        "Volume     C4:  1,000,000     (blue input)\n"
        "Price      C5:  2.00          (blue input)\n"
        "COGS %     C6:  60%           (blue input)\n"
        "Growth     C7:  5%            (blue input)\n"
        "Result     C10: =C4*C5*C6*(1+C7)   <- still one long formula",
        language="text",
    )
    st.markdown("*Better:* assumptions are visible and changeable — but the formula is still too long.")

    st.markdown("#### 🟢 Version 3 — Golden-rule compliant")
    st.markdown(
        """
| Row | Label | Formula | Note |
|---|---|---|---|
| Volume (units) | `C4` | `1,000,000` | 🔵 input |
| Price (€/unit) | `C5` | `2.00` | 🔵 input |
| COGS % of revenue | `C6` | `60%` | 🔵 input |
| Volume growth | `C7` | `5%` | 🔵 input |
| **Revenue** | `C10` | `=C4*C5` | one step |
| **COGS** | `C11` | `=C10*C6` | one step |
| **Gross Profit** | `C12` | `=C10-C11` | one step |
| **Next-yr Revenue** | `C13` | `=C10*(1+C7)` | one step |
| **Check: margin 0–100%?** | `C14` | `=IF(AND(C12/C10>0,C12/C10<1),"OK","ERROR")` | 🔴 self-check |
"""
    )

    st.info(
        "**Result:** Every number is traceable, each formula is one readable step, rows are labelled with "
        "units, inputs are colour-coded, and a check row self-polices. Same maths — professional quality."
    )

    st.markdown("#### The takeaway in one line")
    st.markdown(
        "> *If you can't point to where every number comes from and change any assumption in one place, "
        "the model isn't finished yet.*"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Spot the Golden-Rule Violation")
    st.markdown(
        "Inspect each formula below and choose which golden rule it breaks. You'll get instant feedback."
    )

    scenarios = [
        {
            "formula": "=B4*B5*0.3",
            "context": "A tax line, where 0.3 is the tax rate typed straight into the formula.",
            "options": [
                "Hard-coding a number inside a formula",
                "Time flowing in the wrong direction",
                "Missing a chart",
                "Using too many colours",
            ],
            "answer": "Hard-coding a number inside a formula",
            "explain": "The 0.3 (tax rate) should be a labelled, colour-coded input cell — e.g. =B4*B5*Tax_rate.",
        },
        {
            "formula": "C10:  =C4*C5      |  D10:  =D4*D5+500  |  E10:  =E4*E5",
            "context": "A revenue row copied across three years — but D10 has an extra +500.",
            "options": [
                "One formula per row is broken (D10 is inconsistent)",
                "The formula is too colourful",
                "Inputs are on the wrong sheet",
                "There is no tax line",
            ],
            "answer": "One formula per row is broken (D10 is inconsistent)",
            "explain": "Every cell in the row must share the same logic. The rogue +500 in D10 is a classic hidden error.",
        },
        {
            "formula": "=(A1*B1-C1)/(D1+E1)*(1+F1)-G1*H1",
            "context": "A single 'bottom-line' cell doing the entire P&L at once.",
            "options": [
                "Formula is far too long — should be broken into labelled steps",
                "Not enough hard-coding",
                "Too many input cells",
                "Missing a header row",
            ],
            "answer": "Formula is far too long — should be broken into labelled steps",
            "explain": "Break it into readable one-step rows (revenue, cost, margin). If you can't read it aloud, it's too long.",
        },
        {
            "formula": "Assets = 1,200 | Liabilities = 700 | Equity = 450  (no check cell)",
            "context": "A balance sheet where 700 + 450 = 1,150 ≠ 1,200 — and nothing flags it.",
            "options": [
                "No error check — the balance sheet doesn't balance and nothing catches it",
                "Too many colours used",
                "The font is too small",
                "Inputs and outputs are the same colour on purpose",
            ],
            "answer": "No error check — the balance sheet doesn't balance and nothing catches it",
            "explain": "A simple check =IF(Assets-Liab-Equity=0,\"OK\",\"ERROR\") would have turned red and caught the €50 gap.",
        },
    ]

    for i, sc in enumerate(scenarios):
        st.markdown(f"##### Scenario {i+1}")
        st.code(sc["formula"], language="text")
        st.caption(sc["context"])
        choice = st.radio(
            "Which golden rule is broken?",
            sc["options"],
            index=None,
            key=f"bp_scenario_{i}",
        )
        if choice is not None:
            if choice == sc["answer"]:
                st.success(f"✅ Correct! {sc['explain']}")
            else:
                st.error(f"❌ Not quite. **Correct answer:** {sc['answer']} — {sc['explain']}")
        st.markdown("---")

    # ---------------------------------------------------------------------------
    st.subheader("✏️ Interactive Exercise 2 — Colour-Coding Demonstrator")
    st.markdown(
        "Pick what a cell *contains* and see the colour convention a professional would apply."
    )

    cell_type = st.selectbox(
        "This cell contains…",
        [
            "— Select —",
            "A typed assumption I want to change (e.g. growth rate 5%)",
            "A formula that calculates a result (e.g. =C4*C5)",
            "A link pulling from another sheet (e.g. ='P&L'!B12)",
            "A check that has failed (balance ≠ 0)",
        ],
    )

    mapping = {
        "A typed assumption I want to change (e.g. growth rate 5%)":
            ("🔵 BLUE font", "Input / assumption — this is the only kind of cell users should overtype.", st.info),
        "A formula that calculates a result (e.g. =C4*C5)":
            ("⬛ BLACK font", "Calculation — never type over it; it derives from inputs.", st.success),
        "A link pulling from another sheet (e.g. ='P&L'!B12)":
            ("🟢 GREEN font", "Cross-sheet link — colour-coded so readers know the value lives elsewhere.", st.success),
        "A check that has failed (balance ≠ 0)":
            ("🔴 RED font / fill", "Failed error check — demands attention before the model is used.", st.error),
    }

    if cell_type != "— Select —":
        colour, meaning, box = mapping[cell_type]
        box(f"**Apply: {colour}** — {meaning}")

    st.caption(
        "🧠 Consistent colour-coding means anyone can open your model and instantly know what's safe to "
        "change (blue), what to leave alone (black), what comes from elsewhere (green), and what's broken (red)."
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The 'fat-finger' hard-code (why Rule 2 exists)", expanded=True):
        st.markdown(
            """
**Situation:** An analyst hard-coded a one-off €2m grant into the revenue formula for the current year,
then copied the row across all five forecast years.

**What went wrong:** The €2m silently repeated in every year, overstating the 5-year plan by ~€8m. No
one spotted it because the number was invisible inside the formula.

**Golden rule breached:** *Never hard-code inside formulas.* A labelled one-off input, applied only to
Year 1, would have prevented it.

**Lesson:** Hidden numbers don't just cause errors — they cause errors that *propagate*.
"""
        )

    with st.expander("Case B — MI-reporting speed-up (colour-coding & consistency)"):
        st.markdown(
            """
**Situation:** A factory finance team standardised all monthly reporting models: blue inputs, black
formulas, one formula per row, and a checks tab.

**Result:** New team members became productive in **days, not weeks**, month-end review time dropped,
and hand-offs during holidays no longer caused errors — anyone could pick up the model and read it.

**Golden rules applied:** colour-coding, consistency, labelling, error checks.

**Lesson:** Best practices aren't overhead — they directly cut cycle time and reliance on any one person.
"""
        )

    with st.expander("Case C — The audit that passed in an hour (transparency pays off)"):
        st.markdown(
            """
**Situation:** A €6m Capex model went to internal audit. Because it followed golden rules — traceable
inputs, short formulas, self-checks — the auditors could follow every number without asking the modeler.

**Result:** The review that usually takes days was signed off in about an hour, and the investment
decision proceeded on schedule.

**Golden rules applied:** no hard-coding, short formulas, documentation, error checks.

**Lesson:** A transparent model isn't just 'nice' — it removes friction from real decisions and approvals.
"""
        )

    st.info(
        "🔗 **Pattern:** Every 'best practice' maps to a real-world failure it prevents. The discipline is "
        "invisible when it works — and painfully visible when it's skipped."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_03"):
        q1 = st.radio(
            "**1.** In the standard colour-coding convention, a BLUE font cell represents:",
            [
                "A formula that must not be changed",
                "An input / assumption that is safe to change",
                "A link to another workbook",
                "A failed error check",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** Writing `=Revenue*0.6` instead of `=Revenue*COGS_pct` breaks which golden rule?",
            [
                "Keep formulas short",
                "Never hard-code numbers inside formulas",
                "Build time left-to-right",
                "Document your sources",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** 'One formula per row' means:",
            [
                "Each row may contain only one number",
                "Every cell in a calculation row shares the same logic, copied across periods",
                "You can only have one row per sheet",
                "Formulas must never reference inputs",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** The main purpose of an error-check row is to:",
            [
                "Make the model look more advanced",
                "Automatically flag mistakes before a decision-maker relies on the model",
                "Increase the file size",
                "Replace the need for inputs",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Which of these is the BEST reason to keep formulas short and broken into steps?",
            [
                "It uses more cells, which looks impressive",
                "Short, single-step formulas are transparent and easy to audit; long ones hide errors",
                "Excel cannot handle long formulas",
                "It is required by accounting standards",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "An input / assumption that is safe to change"),
            "2": (q2, "Never hard-code numbers inside formulas"),
            "3": (q3, "Every cell in a calculation row shares the same logic, copied across periods"),
            "4": (q4, "Automatically flag mistakes before a decision-maker relies on the model"),
            "5": (q5, "Short, single-step formulas are transparent and easy to audit; long ones hide errors"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've internalised the golden rules! On to Module 0.4. 🎉")
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
    f"Applied Financial Models · Module 0.3 Best Practices & Golden Rules · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
