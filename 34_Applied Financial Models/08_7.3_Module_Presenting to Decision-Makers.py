"""
================================================================================
APPLIED FINANCIAL MODELS
Module 7.3 — PRESENTING TO DECISION-MAKERS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to present model results to decision-makers: dashboards, one-page summaries,
KPI selection, and board-ready outputs.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live one-page board dashboard builder)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_7_3_Presenting_to_Decision_Makers.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="7.3 Presenting to Decision-Makers — Applied Financial Models",
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
**Module 7.3 — Presenting to Decision-Makers**

🟡 *Intermediate*

**You will learn to:**
- Design a one-page board summary
- Choose the right KPIs to show
- Build a clean decision dashboard
- Anticipate the questions you'll get
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live one-page board "
    "dashboard from your model outputs."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🎯 7.3 · Presenting to Decision-Makers")
st.markdown(
    """
You've built the model (Parts 0–6), extracted the insight (7.1), and shaped the story (7.2). Now you have
to **present** it — usually to busy, senior people who will decide in minutes. The format matters as much
as the content: a cluttered pack loses the room; a crisp **one-pager** or **dashboard** wins the decision.

This module covers the practical craft of **board-ready presentation**: the one-page summary, KPI
selection, dashboard design, and handling the tough questions.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "7.3")
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
### The one-page principle
If a decision-maker can only read **one page**, what must it contain? A great one-pager forces you to
distil everything to what truly matters — and it's often all a busy executive will actually read.
"""
    )

    st.markdown("### Anatomy of a board-ready one-pager")
    anatomy = pd.DataFrame(
        {
            "Section": ["1. Recommendation banner", "2. Key metrics (KPIs)", "3. One chart",
                        "4. Key risks & mitigations", "5. The ask"],
            "What it contains": [
                "The decision, up front, in one line (BLUF)",
                "3–5 headline numbers (e.g. NPV, IRR, payback)",
                "A single visual that carries the message (range/bridge/tornado)",
                "The top 2–3 risks and how each is managed",
                "Exactly what you need the board to approve",
            ],
        }
    )
    st.table(anatomy)

    with st.expander("🔑 Concept 1 — Choosing the right KPIs"):
        st.markdown(
            """
Show **3–5 KPIs**, no more. Pick the ones that answer the decision:
- **Investment decision:** NPV, IRR, payback, and the key risk metric.
- **Performance review:** revenue vs. budget, margin, cash, a variance.
- **Financing:** leverage, DSCR/interest cover, headroom.

Every KPI must earn its place — if it doesn't inform the decision, cut it. A wall of 20 metrics hides the
3 that matter.
"""
        )

    with st.expander("🔑 Concept 2 — Dashboards done right"):
        st.markdown(
            """
A good decision dashboard is **glanceable**:
- **Headline KPIs at the top**, big and clear.
- **Traffic-light / colour cues** (green = good, red = attention) for instant status.
- **One primary chart**, not five competing ones.
- **Consistent, uncluttered layout** — whitespace is your friend.

The test: can a director grasp the status in **10 seconds**? (This ties back to your Power BI dashboard
work — the same principles apply.)
"""
        )

    with st.expander("🔑 Concept 3 — Detail on tap (the appendix)"):
        st.markdown(
            """
Board members vary: some want the headline, others will probe the assumptions. Serve both:
- **Front page:** the recommendation and headline KPIs.
- **Appendix:** the full model, sensitivities, and assumption logs — ready if asked, but not cluttering
  the main message.

*"Simple on the surface, deep underneath."*
"""
        )

    with st.expander("🔑 Concept 4 — Anticipating the questions"):
        st.markdown(
            """
Great presenters pre-empt the obvious challenges:
- *"What if volume/price is lower?"* → have the sensitivity ready.
- *"How does this compare to alternatives / doing nothing?"* → show the comparison.
- *"What's the downside / worst case?"* → lead with it before they ask.
- *"What are you assuming?"* → key assumptions on a slide.

Anticipating questions signals rigour and builds trust — and stops the meeting derailing.
"""
        )

    with st.expander("🔑 Concept 5 — Common presentation mistakes"):
        st.markdown(
            """
- **Burying the recommendation** on slide 20 (lead with it).
- **Too many numbers / tiny fonts** (cut ruthlessly).
- **Five charts on one slide** (one message per visual).
- **No clear 'ask'** (state exactly what you need approved).
- **Defensiveness under challenge** (welcome questions; you've done the work).
"""
        )

    st.success(
        "**Takeaway:** Decision-makers decide fast, so present for the glance: a one-page summary with a "
        "clear recommendation, 3–5 KPIs, one chart, the key risks/mitigations, and a specific ask — with "
        "full detail available on tap in the appendix."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — A board one-pager")
    st.markdown("Turning the €6m automation model into a single, decision-ready page.")

    st.markdown("#### The one-page layout")
    st.markdown(
        """
> ## 🟢 RECOMMENDATION: Approve the €6m automation investment (conditional on the X supply contract)
>
> | NPV | IRR | Payback | Worst case |
> |---|---|---|---|
> | **+€400k** | **12%** (hurdle 10%) | **5.0 yrs** | **−€1.2m** |
>
> **[ Chart: scenario range — Worst −€1.2m · Base +€0.4m · Best +€2.4m ]**
>
> **Key risks & mitigations**
> - ⚠️ *Volume/price sensitivity* → secure the X supply contract (protects the base-case volume).
> - ⚠️ *Margin decline over time* → procurement programme to offset input-cost inflation.
>
> **The ask:** Approve €6m capex, conditional on signing the X contract by Q3.
"""
    )

    st.markdown("#### Why it works")
    st.markdown(
        """
- **Recommendation first** — the board knows the answer immediately.
- **4 KPIs**, not 40 — the numbers that decide it.
- **One chart** — the scenario range shows upside *and* survivable downside at a glance.
- **Risks paired with mitigations** — shows rigour and control.
- **A specific ask** — the board knows exactly what to approve.
"""
    )

    st.info(
        "**Insight:** Everything a director needs to decide fits on **one page** and can be absorbed in "
        "under a minute. The full 20-tab model still exists — in the **appendix**, ready for anyone who "
        "wants to probe. **Simple on the surface, deep underneath.** That's board-ready presentation."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — One-Page Board Dashboard Builder")
    st.markdown(
        "Enter your model outputs and watch a clean, board-ready one-pager assemble — recommendation "
        "banner, KPIs, scenario chart, and the ask."
    )

    left, right = st.columns([0.36, 0.64])
    with left:
        project = st.text_input("Decision", "€6m automation investment")
        npv = st.number_input("NPV (€)", -100_000_000, 100_000_000, 400_000, 50_000)
        irr = st.number_input("IRR (%)", -50.0, 100.0, 12.0, 0.5)
        hurdle = st.number_input("Hurdle rate (%)", 0.0, 50.0, 10.0, 0.5)
        payback = st.number_input("Payback (years)", 0.0, 30.0, 5.0, 0.5)
        worst = st.number_input("Worst-case NPV (€)", -500_000_000, 100_000_000, -1_200_000, 50_000)
        best = st.number_input("Best-case NPV (€)", -100_000_000, 500_000_000, 2_400_000, 50_000)
        risk1 = st.text_input("Key risk #1", "Volume/price sensitivity")
        mit1 = st.text_input("Mitigation #1", "secure the X supply contract")
        the_ask = st.text_input("The ask", "Approve €6m capex, conditional on the X contract")

    with right:
        approve = npv > 0 and irr > hurdle
        st.markdown("##### 📄 Board One-Pager (preview)")

        # Recommendation banner
        if approve:
            st.success(f"### 🟢 RECOMMENDATION: APPROVE — {project}")
        elif npv > 0:
            st.info(f"### 🟡 RECOMMENDATION: CONSIDER — {project}")
        else:
            st.error(f"### 🔴 RECOMMENDATION: DECLINE — {project}")

        # KPIs
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("NPV", money(npv))
        k2.metric("IRR", f"{irr:.0f}%", f"hurdle {hurdle:.0f}%",
                  delta_color="normal" if irr > hurdle else "inverse")
        k3.metric("Payback", f"{payback:.1f} yrs")
        k4.metric("Worst case", money(worst), delta_color="inverse")

        # Scenario chart
        st.markdown("**Scenario range (NPV)**")
        scen = pd.DataFrame(
            {"NPV (€)": [worst, npv, best]},
            index=["Worst", "Base", "Best"],
        )
        st.bar_chart(scen)

        # Risks & ask
        st.markdown(f"**Key risk & mitigation:** ⚠️ {risk1} → 🛡️ {mit1}")
        st.markdown(f"**The ask:** {the_ask}")

        # 10-second test flag
        st.caption("✅ 10-second test: recommendation, 4 KPIs, one chart, one risk+mitigation, and the ask — "
                   "all on a single glanceable page.")

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Flip the banner:** Set NPV negative — watch the recommendation banner turn red ('Decline').
2. **KPI discipline:** You have 4 KPIs. Which single one would you keep if allowed only one? Why?
"""
        )
    with e2:
        st.markdown(
            """
3. **Survivable downside:** Raise the worst case above zero. Does the story become easier to sell?
4. **The ask test:** Rewrite 'the ask' so it's specific, time-bound, and unambiguous.
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — The one-pager that got the decision", expanded=True):
        st.markdown(
            """
**Situation:** A well-built investment case kept stalling because the board pack ran to 30 dense slides.

**What presentation fixed:** Condensing to a **single one-pager** — recommendation banner, four KPIs, one
scenario chart, risks/mitigations, and the ask — let the board decide in one meeting. The 30 slides became
an appendix.

**Why it matters:** The analysis was always sound; the *format* was blocking the decision.

**Lesson:** A crisp one-pager often succeeds where a thick deck fails.
"""
        )

    with st.expander("Case B — The dashboard that passed the 10-second test"):
        st.markdown(
            """
**Situation:** A monthly performance pack overwhelmed executives with dozens of metrics.

**What presentation fixed:** A redesigned **dashboard** put 5 headline KPIs at the top with traffic-light
colours and a single trend chart. Executives could read the status in seconds and focus discussion on the
red items.

**Why it matters:** Attention is scarce; a glanceable dashboard directs it to what needs action. (The same
Power BI design principles you use apply here.)

**Lesson:** Design for the glance — headline KPIs, colour cues, one chart, lots of whitespace.
"""
        )

    with st.expander("Case C — Winning the room by anticipating questions"):
        st.markdown(
            """
**Situation:** A presenter expected a grilling on the downside of a risky project.

**What presentation fixed:** They **pre-empted** it — opening with the worst-case scenario and the
mitigation *before* being asked. The board's confidence rose sharply; the tough question never became a trap.

**Why it matters:** Anticipating challenges signals rigour and control, and keeps the meeting on track.

**Lesson:** Lead with the downside and the answer to the obvious questions — don't wait to be cornered.
"""
        )

    st.info(
        "🔗 **Pattern:** Getting a decision across the line is a presentation skill: distil to one page, "
        "choose KPIs that decide, design for the glance, keep detail on tap, and pre-empt the tough questions."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_73"):
        q1 = st.radio(
            "**1.** A board-ready one-pager should lead with:",
            [
                "The detailed assumptions",
                "The recommendation (up front)",
                "The full model",
                "An apology for the complexity",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** How many headline KPIs should a decision one-pager typically show?",
            [
                "As many as possible (20+)",
                "About 3–5 that directly inform the decision",
                "Exactly one",
                "None — just narrative",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Where should the full model and detailed sensitivities live?",
            [
                "On the front page, in full",
                "In an appendix — available on tap if asked",
                "Deleted after the meeting",
                "Only in the presenter's head",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** The '10-second test' for a dashboard means:",
            [
                "It takes 10 seconds to build",
                "A decision-maker can grasp the status at a glance in ~10 seconds",
                "It refreshes every 10 seconds",
                "It has 10 charts",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Anticipating likely questions (e.g. the worst case) before being asked:",
            [
                "Wastes the board's time",
                "Signals rigour and builds trust, keeping the meeting on track",
                "Should be avoided",
                "Is only for junior staff",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The recommendation (up front)"),
            "2": (q2, "About 3–5 that directly inform the decision"),
            "3": (q3, "In an appendix — available on tap if asked"),
            "4": (q4, "A decision-maker can grasp the status at a glance in ~10 seconds"),
            "5": (q5, "Signals rigour and builds trust, keeping the meeting on track"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you can present for a decision! On to Module 7.4 (Common Pitfalls & Model Auditing). 🎉")
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
    f"Applied Financial Models · Module 7.3 Presenting to Decision-Makers · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
