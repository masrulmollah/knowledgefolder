"""
================================================================================
APPLIED FINANCIAL MODELS
Module 0.1 — WHAT IS A FINANCIAL MODEL?
================================================================================

A single-page, interactive Streamlit module that introduces finance
professionals to the very idea of a financial model: what it is, what it is for,
the main types, and when a model adds value versus when it misleads.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live "inputs -> engine -> outputs" playground)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_0_1_What_is_a_Financial_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="0.1 What is a Financial Model? — Applied Financial Models",
    layout="wide",
    page_icon="🧭",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    return f"{symbol}{x:,.{dp}f}"


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 0 · Orientation & Foundations")
st.sidebar.markdown(
    """
**Module 0.1 — What is a Financial Model?**

🟢 *Foundational*

**You will learn to:**
- Define what a financial model is (and isn't)
- Understand the purpose of modeling
- Recognise the main model types
- Judge when a model adds value vs. misleads
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 This is the **first module** of the course. Head to the **Interactive "
    "Exercises** tab to see a model turn assumptions into decisions in real time."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🧭 0.1 · What is a Financial Model?")
st.markdown(
    """
Before building anything, you need to know *what* you're building and *why*. A **financial model**
is a structured, quantitative representation of a real-world business situation — a tool that turns
**assumptions** into **outputs** so you can answer a question and **make a better decision**.

This opening module builds the mental framework for the entire course: what a model is, what it's for,
the main types you'll meet, and — crucially — when a model genuinely adds value versus when it quietly misleads.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "0.1")
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
### A working definition
> A **financial model** is a tool — usually built in a spreadsheet or code — that uses a set of
> **assumptions (inputs)** and **logic (calculations)** to produce **outputs** that describe the
> financial future or worth of a business, project, or decision.

The whole point is captured in one simple flow:
"""
    )

    flow = pd.DataFrame(
        {
            "Stage": ["① INPUTS", "② CALCULATIONS", "③ OUTPUTS", "④ DECISION"],
            "What it is": [
                "The assumptions you can change (e.g. volume, price, growth, cost %)",
                "The logic/engine that links inputs together (formulas)",
                "The results you read (revenue, profit, NPV, cash, ratios)",
                "The action the outputs support (invest? price? hire? borrow?)",
            ],
        }
    )
    st.table(flow)

    st.markdown(
        """
### Why do we model? (the purpose)
Models exist to **support decisions under uncertainty**. Specifically they let you:
- **Forecast** — see the likely financial future before it happens.
- **Test** — ask "what if?" and flex assumptions safely, without real-world consequences.
- **Value** — put a number on a business, project, or asset.
- **Communicate** — give decision-makers a clear, evidence-based basis for action.
"""
    )

    st.markdown("### The main types of financial model")
    types = pd.DataFrame(
        {
            "Model type": [
                "Three-Statement Model", "Forecasting / Budget Model", "Valuation Model (DCF, Comps)",
                "Investment Appraisal (NPV/IRR)", "Scenario & Sensitivity Model",
                "Specialised (LBO, M&A, Project Finance)",
            ],
            "Answers the question…": [
                "How will the whole company's financials evolve?",
                "What are next year's / quarter's numbers likely to be?",
                "What is this business or share worth?",
                "Should we invest in this project or asset?",
                "What happens if our assumptions are wrong?",
                "Deal-specific: returns, financing, structuring",
            ],
        }
    )
    st.table(types)

    with st.expander("🔑 Key concept 1 — A model is not a crystal ball"):
        st.markdown(
            """
A model does **not** predict the future with certainty. It produces a *conditional* answer:
*"IF these assumptions hold, THEN this is the outcome."* Its value lies in making assumptions
**explicit and testable**, not in being "right." Garbage in → garbage out.
"""
        )

    with st.expander("🔑 Key concept 2 — Good model vs. bad model"):
        st.markdown(
            """
| A model **adds value** when… | A model **misleads** when… |
|---|---|
| Assumptions are explicit and sourced | Numbers are hard-coded and untraceable |
| Inputs are separated from calculations | Inputs are buried inside formulas |
| It's transparent and auditable | It's a "black box" nobody can follow |
| It's flexed with scenarios | It shows a single false-precision answer |
| It supports a clear decision | It exists just to justify a decision already made |
"""
        )

    with st.expander("🔑 Key concept 3 — Precision vs. accuracy"):
        st.markdown(
            """
A model outputting *"NPV = €4,382,911"* looks precise, but precision ≠ accuracy. The honest read is
a **range** driven by uncertain assumptions. Beware **false precision** — decimals don't make an
assumption true. Always pair an output with the assumptions and sensitivities behind it.
"""
        )

    st.success(
        "**Takeaway:** A financial model is a decision tool, not a fortune-teller. Its job is to turn "
        "explicit assumptions into outputs you can trust, challenge, and act on."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — From a static number to a real model")
    st.markdown(
        "Let's see *why* a model beats a single hard-coded number, using a simple question: "
        "**'How much profit will we make selling soap next year?'**"
    )

    st.markdown("#### ❌ The non-model (a hard-coded guess)")
    st.markdown(
        """
> *"We'll make about **€200,000** profit next year."*

**Problems:** Where did it come from? What drives it? What if volume drops 10%? Nobody can tell —
it's a black box. You can't test it, challenge it, or learn from it.
"""
    )

    st.markdown("#### ✅ The model (assumptions → logic → output)")
    st.markdown(
        """
| # | Assumption (INPUT) | Value |
|---|---|---|
| 1 | Units sold | 1,000,000 |
| 2 | Price per unit | €2.00 |
| 3 | Cost per unit | €1.60 |
| 4 | Fixed overheads | €200,000 |

**The logic (CALCULATION):**
- Revenue = 1,000,000 × €2.00 = **€2,000,000**
- Total variable cost = 1,000,000 × €1.60 = **€1,600,000**
- Gross profit = €2,000,000 − €1,600,000 = **€400,000**
- Profit = €400,000 − €200,000 fixed = **€200,000** (OUTPUT)
"""
    )

    st.info(
        "**Same €200,000 — but now it's a model.** Because the inputs are explicit, you can immediately "
        "ask: *what if price rises to €2.10? what if volume falls to 900k?* The answer updates and you "
        "**learn what actually drives the profit**. That is the difference between a number and a model."
    )

    st.markdown("#### The decision it supports")
    st.markdown(
        """
With the model you can now see that **each €0.05 change in price ≈ €50,000 of profit** (1m units).
That single insight — impossible from the static guess — could drive a pricing decision worth far
more than the modeling effort itself.
"""
    )

    st.caption("👉 Open the **Interactive Exercises** tab to flex exactly these assumptions yourself.")

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — See a Model Come Alive")
    st.markdown(
        "This is the essence of *every* financial model: **change the inputs on the left, and watch the "
        "outputs and the decision update instantly.** Notice how you immediately learn what drives the result."
    )

    left, right = st.columns([0.35, 0.65])

    with left:
        st.markdown("##### ① INPUTS (assumptions)")
        units = st.slider("Units sold", 100_000, 2_000_000, 1_000_000, 50_000)
        price = st.slider("Price per unit (€)", 0.50, 5.00, 2.00, 0.05)
        cost = st.slider("Cost per unit (€)", 0.20, 4.00, 1.60, 0.05)
        fixed = st.slider("Fixed overheads (€)", 0, 1_000_000, 200_000, 25_000)

    with right:
        # ② CALCULATIONS (the engine)
        revenue = units * price
        var_cost = units * cost
        gross = revenue - var_cost
        profit = gross - fixed
        margin = (profit / revenue * 100) if revenue else 0
        contribution = price - cost
        breakeven_units = (fixed / contribution) if contribution > 0 else float("inf")

        st.markdown("##### ③ OUTPUTS (results)")
        k1, k2, k3 = st.columns(3)
        k1.metric("Revenue", money(revenue))
        k2.metric("Profit", money(profit))
        k3.metric("Net Margin", f"{margin:,.1f}%")

        out_df = pd.DataFrame(
            {
                "Line item": ["Revenue", "Variable cost", "Gross profit", "Fixed overheads", "Profit"],
                "Amount (€)": [revenue, -var_cost, gross, -fixed, profit],
            }
        )
        out_df["Amount (€)"] = out_df["Amount (€)"].map(lambda v: f"€{v:,.0f}")
        st.table(out_df)

        st.markdown("##### ④ DECISION support")
        if contribution <= 0:
            st.error(
                "⚠️ Price is at or below cost per unit — every unit sold **loses** money. "
                "No volume can make this profitable. Fix pricing or cost first."
            )
        elif profit > 0:
            st.success(
                f"✅ **Profitable.** You break even at **{breakeven_units:,.0f} units** "
                f"({breakeven_units/units*100:,.0f}% of current volume). "
                f"Each €0.05 price change ≈ **{money(units*0.05)}** of profit."
            )
        else:
            st.warning(
                f"🔎 **Loss-making at this volume.** You'd need **{breakeven_units:,.0f} units** to break even "
                f"(vs. {units:,.0f} now). Raise price, cut cost, or grow volume."
            )

    st.markdown("---")
    st.markdown("##### 🧪 Experiments to try")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Pricing power:** Nudge price from €2.00 → €2.10. How much does profit jump? (This is the insight
   the static guess could never give you.)
2. **Volume risk:** Drop units to 900,000. Are you still profitable?
"""
        )
    with e2:
        st.markdown(
            """
3. **Cost squeeze:** Push cost per unit to €1.90. Watch the break-even point rise sharply.
4. **Find the edge:** Can you set inputs so the model flips from profit to loss with a *single* small change?
"""
        )

    st.info(
        "🧠 **The big idea:** You didn't just get a number — you *learned the relationships*. That is what "
        "a financial model gives you that a static figure never can."
    )

    st.download_button(
        "⬇️ Download this mini-model (CSV)",
        pd.DataFrame(
            {
                "Input": ["Units", "Price", "Cost/unit", "Fixed"],
                "Value": [units, price, cost, fixed],
            }
        ).to_csv(index=False).encode("utf-8"),
        "what_is_a_model_inputs.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The €6m Capex decision (model adds value)", expanded=True):
        st.markdown(
            """
**Situation:** A factory is considering a €6m investment in automation to cut labour cost.

**Why a model matters:** Management can't just "feel" whether it's worth it. A model links the
**inputs** (investment, annual savings, life, discount rate) to **outputs** (NPV, IRR, payback), and
lets them **test** downside scenarios (savings 20% lower? project delayed a year?).

**Value delivered:** The model turns a €6m gut-feel into an evidence-based, stress-tested decision —
and shows exactly which assumption (savings level) the decision hinges on.
"""
        )

    with st.expander("Case B — The over-engineered 'black box' (model misleads)"):
        st.markdown(
            """
**Situation:** An analyst presents a 20-tab spreadsheet with hard-coded numbers scattered through
formulas. It outputs a valuation of *"€47,281,904"*.

**The problem:** No one — including the analyst — can explain where key numbers come from or flex them.
The **false precision** (down to the euro) hides deep uncertainty. It looks authoritative but supports
*no* real challenge or learning.

**Lesson:** Complexity and decimals are not the same as reliability. A transparent, simpler model that
people can audit beats an impressive black box every time.
"""
        )

    with st.expander("Case C — Budgeting for the year ahead (everyday modeling)"):
        st.markdown(
            """
**Situation:** A finance team builds next year's budget from volume, price and cost assumptions.

**Why it's a model:** It's driver-based, so when the sales team revises the volume forecast, the whole
budget updates — revenue, costs, and profit — in seconds. Leadership can see the P&L impact of the
change immediately.

**Value delivered:** The model becomes a **living decision tool**, not a once-a-year static document —
enabling rolling forecasts and fast "what-if" conversations.
"""
        )

    st.info(
        "🔗 **Pattern across all cases:** The model's worth comes from **transparency + testability**, "
        "not size or sophistication. A model earns trust when anyone can trace and challenge its numbers."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_01"):
        q1 = st.radio(
            "**1.** A financial model is best described as:",
            [
                "A guaranteed prediction of the future",
                "A tool that turns explicit assumptions into outputs to support a decision",
                "A single hard-coded number stored in a spreadsheet",
                "A legal accounting statement",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The core flow of any financial model is:",
            [
                "Outputs → Inputs → Decision",
                "Inputs → Calculations → Outputs → Decision",
                "Decision → Outputs → Inputs",
                "Calculations → Decision → Inputs",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Which of these signals a model that MISLEADS rather than adds value?",
            [
                "Inputs are clearly separated from calculations",
                "Assumptions are explicit and sourced",
                "Numbers are hard-coded and buried inside formulas (a 'black box')",
                "It is stress-tested with scenarios",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** 'False precision' means:",
            [
                "The model is deliberately wrong",
                "An output shown to the exact euro implies more certainty than the assumptions justify",
                "The model uses too few decimal places",
                "The tax rate is incorrect",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The main purpose of building a financial model is to:",
            [
                "Make the analysis look sophisticated",
                "Support better decisions under uncertainty by making assumptions testable",
                "Avoid using a spreadsheet",
                "Guarantee a profit",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "A tool that turns explicit assumptions into outputs to support a decision"),
            "2": (q2, "Inputs → Calculations → Outputs → Decision"),
            "3": (q3, "Numbers are hard-coded and buried inside formulas (a 'black box')"),
            "4": (q4, "An output shown to the exact euro implies more certainty than the assumptions justify"),
            "5": (q5, "Support better decisions under uncertainty by making assumptions testable"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've got the foundational mindset. On to Module 0.2! 🎉")
        elif score >= 3:
            st.info("Good start — review the feedback below to sharpen your understanding.")
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
    f"Applied Financial Models · Module 0.1 What is a Financial Model? · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
