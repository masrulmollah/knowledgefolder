"""
================================================================================
APPLIED FINANCIAL MODELS
Module 7.1 — EXTRACTING INSIGHTS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to READ a model's outputs: spotting value drivers, red flags, trends and the
"so what?" that turns numbers into insight.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live insight / red-flag scanner)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_7_1_Extracting_Insights.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="7.1 Extracting Insights — Applied Financial Models",
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
**Module 7.1 — Extracting Insights**

🟡 *Intermediate*

**You will learn to:**
- Read model outputs like an analyst
- Identify the true value drivers
- Spot red flags and warning signs
- Turn numbers into the "so what?"
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to run an insight scanner — "
    "enter model outputs and see the drivers and red flags it surfaces."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎯 7.1 · Extracting Insights")
st.markdown(
    """
Parts 0–6 were about **building** models. Part 7 is about the skill that actually creates value: turning a
finished model into **insight and action**. A model full of correct numbers is worthless if nobody can
say what it *means*.

This module teaches you to **read** outputs like a seasoned analyst — finding the **value drivers** (what
really moves the result), spotting the **red flags** (what should worry you), and articulating the
**"so what?"** that leads to a decision.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "7.1")
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
### From numbers to insight
An **output** is a number the model produces (NPV = €400k). An **insight** is what that number *means for
a decision* ("the project creates value, but only if margins hold — and they're the biggest risk"). The
job of Part 7 is to bridge that gap.
"""
    )

    st.markdown("### The analyst's reading framework")
    framework = pd.DataFrame(
        {
            "Question": [
                "What are the value drivers?",
                "What are the red flags?",
                "What's the trend?",
                "How does it compare?",
                "So what?",
            ],
            "What you're looking for": [
                "Which few inputs move the result most (from sensitivity/tornado)",
                "Warning signs: negative cash, thin margins, high leverage, fragile assumptions",
                "Direction over time — improving or deteriorating?",
                "vs. budget, prior year, peers, or a hurdle rate",
                "The single decision or action the numbers point to",
            ],
        }
    )
    st.table(framework)

    with st.expander("🔑 Concept 1 — Value drivers: the 80/20 of any model"):
        st.markdown(
            """
In almost every model, a **handful of drivers** explain most of the result (recall the tornado chart,
5.1). Extracting insight starts with identifying them: *"NPV is overwhelmingly driven by price and
volume; the discount rate barely matters."* Once you know the drivers, you know **where the risk and the
opportunity really are** — and where to focus attention.
"""
        )

    with st.expander("🔑 Concept 2 — Red flags to scan for"):
        st.markdown(
            """
Train yourself to spot warning signs in any set of outputs:
- **Negative or thin operating cash flow** (profit ≠ cash).
- **Margins deteriorating** over the forecast.
- **High leverage / low interest cover** (DSCR or interest cover near covenant).
- **Terminal value >80% of a DCF** (over-reliant on distant assumptions).
- **A negative worst-case scenario** the business couldn't survive.
- **Break-even close to forecast volume** (thin margin of safety).

Any one of these should prompt a *"why?"* and a deeper look.
"""
        )

    with st.expander("🔑 Concept 3 — Trends & comparisons give meaning"):
        st.markdown(
            """
A single number rarely tells a story — **context** does:
- **Trend:** is the margin rising or falling over the five years?
- **Benchmark:** how does the return compare to the hurdle rate, to last year, to peers?
- **Composition:** what's *inside* the number (e.g. is growth from volume or price)?

Insight lives in the *change* and the *comparison*, not the absolute figure.
"""
        )

    with st.expander("🔑 Concept 4 — The 'so what?' test"):
        st.markdown(
            """
Every output should survive the **"so what?"** test. If you state a number and can't finish the sentence
*"…therefore we should…"*, you haven't extracted the insight yet.

- ❌ *"The NPV is €400k."*  →  So what?
- ✅ *"The NPV is €400k and stays positive unless margins fall >15% — so we should proceed, but lock in
  supplier prices to protect the margin."*

The 'so what?' is where analysis becomes advice.
"""
        )

    with st.expander("🔑 Concept 5 — Avoiding analysis traps"):
        st.markdown(
            """
- **False precision:** don't over-trust decimals built on rough assumptions (2.9).
- **Confirmation bias:** don't cherry-pick the outputs that support a pre-formed view.
- **Missing the wood for the trees:** a huge model can bury the one number that matters — always step back
  to the headline drivers.
"""
        )

    st.success(
        "**Takeaway:** Extracting insight means reading a model with a framework — identify the value "
        "drivers, scan for red flags, add trend and benchmark context, and always finish with the "
        "'so what?'. Numbers inform; insight decides."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Reading a project's outputs")
    st.markdown("A completed model produces the outputs below. Let's extract the insight.")

    st.markdown("#### The raw outputs")
    st.markdown(
        """
| Output | Value |
|---|---|
| NPV | +€400,000 |
| IRR | 13% (hurdle 10%) |
| Operating margin — Year 1 → Year 5 | 20% → 14% (declining) |
| Worst-case NPV (scenario) | −€1,200,000 |
| Tornado — top driver | Sales price (±10% → ±€760k NPV) |
| Terminal value as % of DCF | 55% |
"""
    )

    st.markdown("#### Step 1 — Value drivers")
    st.markdown(
        "The tornado shows **price** dominates (±€760k swing). Volume matters; the discount rate barely does. "
        "→ *The result lives or dies on price.*"
    )

    st.markdown("#### Step 2 — Red flags")
    st.markdown(
        """
- 🚩 **Margins decline** 20% → 14% over the forecast — why? (cost inflation? discounting?).
- 🚩 **Worst-case NPV is −€1.2m** — a large, potentially unsurvivable downside.
- ✅ Terminal value at 55% of DCF is within a normal range (not a flag).
"""
    )

    st.markdown("#### Step 3 — Trend & comparison")
    st.markdown(
        "IRR (13%) beats the hurdle (10%) ✅, but the **deteriorating margin trend** undercuts the headline "
        "NPV — the project looks weaker each year, not stronger."
    )

    st.markdown("#### Step 4 — The 'so what?'")
    st.info(
        "**Insight & recommendation:** *The project is value-creating at the base case (NPV +€400k, IRR 13% "
        "> 10% hurdle), but it is **highly exposed to price** and shows a **worrying margin decline** and a "
        "**severe worst-case (−€1.2m)**. Recommendation: proceed only if we can (a) protect pricing (e.g. "
        "contracts/indexation) and (b) confirm the business can absorb the worst case. Otherwise, defer or "
        "de-risk first.*"
    )
    st.caption("Notice how the raw numbers became a clear, caveated recommendation — that's insight extraction.")

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Insight & Red-Flag Scanner")
    st.markdown(
        "Enter a project's key outputs. The scanner surfaces the likely **value driver**, flags **warning "
        "signs**, and drafts a **'so what?'** recommendation — the way an analyst would read it."
    )

    left, right = st.columns([0.40, 0.60])

    with left:
        st.markdown("##### 📊 Model outputs")
        npv = st.number_input("NPV (€)", -100_000_000, 100_000_000, 400_000, 50_000)
        irr = st.number_input("IRR (%)", -50.0, 100.0, 13.0, 0.5)
        hurdle = st.number_input("Hurdle rate (%)", 0.0, 50.0, 10.0, 0.5)
        margin_start = st.number_input("Operating margin — Year 1 (%)", -50.0, 100.0, 20.0, 0.5)
        margin_end = st.number_input("Operating margin — final year (%)", -50.0, 100.0, 14.0, 0.5)
        worst_npv = st.number_input("Worst-case NPV (€)", -500_000_000, 100_000_000, -1_200_000, 50_000)
        tv_pct = st.slider("Terminal value as % of DCF", 0, 100, 55, 1)
        top_driver = st.selectbox("Tornado — top driver",
                                  ["Price", "Volume", "Variable cost", "Fixed cost", "Discount rate"])
        mos = st.slider("Margin of safety (%)", -20, 80, 30, 1)

    with right:
        st.markdown("##### 🔎 Scanner results")

        # Headline verdict
        if npv > 0 and irr > hurdle:
            st.success(f"✅ **Value-creating base case:** NPV {money(npv)}, IRR {irr:.0f}% beats the {hurdle:.0f}% hurdle.")
        elif npv > 0:
            st.info(f"🔎 Positive NPV ({money(npv)}), but IRR ({irr:.0f}%) vs. hurdle ({hurdle:.0f}%) is worth checking.")
        else:
            st.error(f"❌ **Value-destroying base case:** NPV is {money(npv)}.")

        # Value driver
        st.markdown(f"**🎯 Primary value driver:** `{top_driver}` — focus risk management and data quality here.")

        # Red-flag scan
        flags = []
        if margin_end < margin_start - 1:
            flags.append(f"📉 **Margin declining** ({margin_start:.0f}% → {margin_end:.0f}%) — investigate the cause (cost inflation? pricing?).")
        if worst_npv < 0:
            flags.append(f"🔻 **Negative worst-case NPV** ({money(worst_npv)}) — confirm the business can survive the downside.")
        if tv_pct > 80:
            flags.append(f"⏳ **Terminal value is {tv_pct}% of DCF** — the valuation leans heavily on distant assumptions.")
        if mos < 15:
            flags.append(f"⚠️ **Thin margin of safety ({mos}%)** — little room before break-even.")
        if irr <= hurdle:
            flags.append(f"🚧 **IRR ({irr:.0f}%) at/below the hurdle ({hurdle:.0f}%)** — return may not justify the risk.")

        st.markdown("**🚩 Red flags:**")
        if flags:
            for f in flags:
                st.markdown(f"- {f}")
        else:
            st.markdown("- ✅ No major red flags detected in these outputs.")

        # So-what recommendation
        st.markdown("**🧭 Draft 'so what?' recommendation:**")
        if npv > 0 and not flags:
            rec = (f"Proceed. The project creates value ({money(npv)} NPV, {irr:.0f}% IRR) with no major red "
                   f"flags. Monitor **{top_driver.lower()}** as the key driver.")
            st.success(rec)
        elif npv > 0 and flags:
            rec = (f"Proceed **with conditions**. The base case is positive ({money(npv)} NPV), but address "
                   f"the red flags above — especially protecting **{top_driver.lower()}** and stress-testing "
                   "the downside — before committing.")
            st.info(rec)
        else:
            rec = ("Do not proceed as configured. The base case destroys value; revisit the assumptions "
                   f"around **{top_driver.lower()}** or restructure the project before reconsidering.")
            st.error(rec)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Flip the margin trend:** Set the final-year margin *above* Year 1. Watch that red flag disappear.
2. **Survivable downside:** Raise the worst-case NPV above zero. How does the recommendation change?
"""
        )
    with e2:
        st.markdown(
            """
3. **TV over-reliance:** Push terminal value to 90%. See the scanner flag an over-reliance on distant assumptions.
4. **Thin safety:** Drop the margin of safety below 15% and note the new warning.
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The headline that hid the story", expanded=True):
        st.markdown(
            """
**Situation:** A project was presented with a strong headline NPV and approved quickly.

**What insight extraction would have caught:** The outputs also showed a **declining margin trend** and a
**severe negative worst-case** — both buried beneath the positive headline. Reading the full output set
(not just the NPV) would have surfaced these risks *before* approval.

**Why it matters:** A single output can flatter a project; the insight is in the *pattern* of outputs.

**Lesson:** Never stop at the headline number — scan margins, downside, drivers and trends.
"""
        )

    with st.expander("Case B — Finding the one driver that mattered"):
        st.markdown(
            """
**Situation:** A team debated dozens of assumptions in a complex model, unsure where the value really came from.

**What insight extraction revealed:** The tornado made it obvious that **price** drove ~70% of the NPV
swing. Suddenly the whole debate refocused on securing pricing — the single lever that mattered.

**Why it matters:** Extracting the dominant driver cut through the noise and directed effort where it
created the most value.

**Lesson:** Identify the value drivers first — they tell you what to worry about and what to ignore.
"""
        )

    with st.expander("Case C — The 'so what?' that changed the decision"):
        st.markdown(
            """
**Situation:** An analyst delivered a technically flawless model but just presented the numbers.

**What was missing:** The **'so what?'**. When pushed to translate the outputs into a recommendation, the
analyst realised the project only worked if a fragile assumption held — leading the board to **defer**
pending more evidence.

**Why it matters:** The insight (and the better decision) came from interpreting the numbers, not just
reporting them.

**Lesson:** Your job isn't to present numbers — it's to say what they *mean* and what to *do*.
"""
        )

    st.info(
        "🔗 **Pattern:** Extracting insight is the difference between a *reporter* and an *advisor*. Read the "
        "full output set, find the drivers and red flags, add context, and always land the 'so what?'."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_71"):
        q1 = st.radio(
            "**1.** The difference between an output and an insight is that an insight:",
            [
                "Is always a bigger number",
                "Explains what the number means for a decision",
                "Ignores the model",
                "Is only about the discount rate",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** 'Value drivers' are:",
            [
                "The few inputs that move the result the most",
                "The least important assumptions",
                "Only the fixed costs",
                "The model's formatting",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Which of these is a RED FLAG when reading model outputs?",
            [
                "A comfortable margin of safety",
                "A negative worst-case NPV the business couldn't survive",
                "IRR well above the hurdle rate",
                "Stable margins over the forecast",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** The 'so what?' test checks whether you can:",
            [
                "Make the model larger",
                "Translate an output into a recommended action ('…therefore we should…')",
                "Remove the assumptions",
                "Avoid using a discount rate",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** A single number usually gains meaning from:",
            [
                "Being shown to more decimal places",
                "Trend and comparison (vs. prior year, budget, peers, or a hurdle)",
                "Ignoring the context",
                "Hiding the assumptions",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Explains what the number means for a decision"),
            "2": (q2, "The few inputs that move the result the most"),
            "3": (q3, "A negative worst-case NPV the business couldn't survive"),
            "4": (q4, "Translate an output into a recommended action ('…therefore we should…')"),
            "5": (q5, "Trend and comparison (vs. prior year, budget, peers, or a hurdle)"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you can turn outputs into insight! On to Module 7.2 (Storytelling with Models). 🎉")
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
    f"Applied Financial Models · Module 7.1 Extracting Insights · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
