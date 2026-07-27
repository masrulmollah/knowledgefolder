"""
================================================================================
APPLIED FINANCIAL MODELS
Module 3.5 — SUM-OF-THE-PARTS (SOTP)
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to value a conglomerate / multi-business-unit company by valuing each
division separately and summing them — including the conglomerate discount.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live multi-division SOTP engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_3_5_Sum_of_the_Parts.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="3.5 Sum-of-the-Parts (SOTP) — Applied Financial Models",
    layout="wide",
    page_icon="💰",
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
st.sidebar.caption("Part 3 · Valuation Models")
st.sidebar.markdown(
    """
**Module 3.5 — Sum-of-the-Parts (SOTP)**

🔴 *Advanced*

**You will learn to:**
- Value each business unit separately
- Apply the right multiple to each division
- Sum the parts to a group value
- Apply a conglomerate discount & equity bridge
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for a live SOTP engine — value "
    "each division, sum them, and bridge to equity value."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("💰 3.5 · Sum-of-the-Parts (SOTP)")
st.markdown(
    """
Some companies aren't one business — they're several very different businesses under one roof (a
**conglomerate** or **multi-BU** group). Valuing such a group with a single multiple is misleading,
because each division has its own growth, margins, and risk.

**Sum-of-the-Parts (SOTP)** values **each business unit separately** — using the most appropriate method
and multiple for each — then adds them up. It's the right lens for diversified groups, spin-off analysis,
and unlocking "hidden" value.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "3.5")
c2.metric("Part", "3 — Valuation")
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
### The core idea
A diversified group is worth the sum of its independently-valued parts. Value each division on its own
merits, add them together, then adjust for group-level items (net debt, central costs, and any
conglomerate discount).
"""
    )
    st.latex(r"\text{Group EV} = \sum_{i=1}^{n} \text{EV}_{\text{division } i}")
    st.latex(r"\text{Equity Value} = \text{Group EV} - \text{Net Debt} - \text{Central Costs} \times (1 - \text{discount adj.})")

    st.markdown("### The SOTP process")
    steps = pd.DataFrame(
        {
            "Step": ["1. Segment", "2. Value each part", "3. Sum", "4. Adjust", "5. Bridge to equity"],
            "What you do": [
                "Split the group into its distinct business units",
                "Value each BU with the most appropriate method / multiple",
                "Add the divisional enterprise values together",
                "Apply any conglomerate discount and deduct central/HQ costs",
                "Subtract net debt to reach equity value (and per-share value)",
            ],
        }
    )
    st.table(steps)

    with st.expander("🔑 Concept 1 — Why one multiple doesn't fit all"):
        st.markdown(
            """
Different businesses trade at different multiples because they have different growth, margins, and risk.
For example a group might contain:
- A stable consumer division → ~10× EBITDA
- A fast-growth digital arm → ~18× EBITDA
- A cyclical industrial unit → ~6× EBITDA

Blending them into one group multiple hides value and misprices the whole. SOTP applies the **right
multiple to each part** — often revealing that the sum is worth more (or less) than the market assumes.
"""
        )

    with st.expander("🔑 Concept 2 — Mix and match methods per division"):
        st.markdown(
            """
SOTP lets you use the **best tool for each division**:
- A mature cash-cow → **DCF** or EV/EBITDA multiple.
- An early-stage unit with no profit → **EV/Sales**.
- A listed minority stake → its **market value** directly.
- A property portfolio → **net asset value**.

This flexibility is SOTP's great strength — you're not forced into one method for the whole group.
"""
        )

    with st.expander("🔑 Concept 3 — The conglomerate discount"):
        st.markdown(
            """
Diversified groups often trade **below** the sum of their parts — the **conglomerate discount**
(commonly ~10–20%). Reasons include:
- Complexity and reduced transparency for investors.
- Inefficient capital allocation across unrelated units.
- Lack of focus / management bandwidth.

$$\\text{Adjusted Group Value} = \\text{Sum of Parts} \\times (1 - \\text{Conglomerate Discount})$$

A large discount is often the trigger for **break-up / spin-off** proposals (see Case studies).
"""
        )

    with st.expander("🔑 Concept 4 — Central costs & the equity bridge"):
        st.markdown(
            """
Two group-level adjustments complete the picture:
1. **Central (HQ) costs** — corporate overheads not attributed to any division reduce group value
   (often capitalised as a negative "stub").
2. **Net debt** — as always, subtract group net debt to move from enterprise value to **equity value**.

$$\\text{Equity Value} = \\text{Sum of Division EVs} - \\text{Central cost value} - \\text{Net Debt}$$
"""
        )

    st.success(
        "**Takeaway:** SOTP values each business unit on its own merits with the most fitting method, sums "
        "them, then adjusts for conglomerate discount, central costs and net debt. It's the right approach "
        "for diversified groups — and often reveals hidden value."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Valuing a three-division group")
    st.markdown("A diversified group **'DiverseCo'** with three very different business units.")

    st.markdown("#### Step 1 — Value each division separately")
    st.markdown(
        """
| Division | Metric (EBITDA) | Multiple | Enterprise Value |
|---|---|---|---|
| Consumer (stable) | €20m | 10.0× | €200m |
| Digital (high-growth) | €8m | 18.0× | €144m |
| Industrial (cyclical) | €15m | 6.0× | €90m |
| **Sum of parts (EV)** | | | **€434m** |
"""
    )

    st.markdown("#### Step 2 — Apply the conglomerate discount")
    st.markdown(
        """
The market applies a **15% conglomerate discount** for complexity:

$$\\text{Adjusted EV} = €434m \\times (1 - 0.15) = \\mathbf{€368.9m}$$
"""
    )

    st.markdown("#### Step 3 — Deduct central costs & net debt")
    st.markdown(
        """
| Item | € |
|---|---|
| Adjusted group EV | 368.9m |
| − Central cost value | (20.0m) |
| = Group Enterprise Value | 348.9m |
| − Net debt | (50.0m) |
| **= Equity Value** | **€298.9m** |
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Sum of parts (EV)", "€434.0m")
    e2.metric("After 15% discount", "€368.9m")
    e3.metric("Equity Value", "€298.9m")

    st.info(
        "**Insight:** The three divisions are worth €434m *individually*, but the market values the group at "
        "~€369m due to the **conglomerate discount** — a €65m gap. If a break-up could realise the full "
        "sum-of-parts, that €65m is the potential **value unlock** — exactly the logic activists use to "
        "push for spin-offs."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Build a Sum-of-the-Parts Valuation")
    st.markdown(
        "Set each division's EBITDA and multiple, apply a conglomerate discount, deduct central costs and "
        "net debt — and watch the group equity value (and the value-unlock gap) build live."
    )

    left, right = st.columns([0.40, 0.60])

    with left:
        st.markdown("##### 🏭 Division 1 — Consumer")
        e1 = st.number_input("EBITDA 1 (€m)", 0.0, 5000.0, 20.0, 1.0)
        m1 = st.number_input("Multiple 1 (×)", 0.0, 50.0, 10.0, 0.5)

        st.markdown("##### 💻 Division 2 — Digital")
        e2 = st.number_input("EBITDA 2 (€m)", 0.0, 5000.0, 8.0, 1.0)
        m2 = st.number_input("Multiple 2 (×)", 0.0, 50.0, 18.0, 0.5)

        st.markdown("##### 🏗️ Division 3 — Industrial")
        e3 = st.number_input("EBITDA 3 (€m)", 0.0, 5000.0, 15.0, 1.0)
        m3 = st.number_input("Multiple 3 (×)", 0.0, 50.0, 6.0, 0.5)

        st.markdown("##### 🏢 Group adjustments")
        cong_disc = st.slider("Conglomerate discount (%)", 0, 40, 15, 1)
        central = st.number_input("Central cost value (€m)", 0.0, 1000.0, 20.0, 1.0)
        net_debt = st.number_input("Net debt (€m)", -1000.0, 5000.0, 50.0, 5.0)
        shares = st.number_input("Shares outstanding (m)", 0.1, 10000.0, 100.0, 1.0)

    with right:
        ev1, ev2, ev3 = e1 * m1, e2 * m2, e3 * m3
        sum_parts = ev1 + ev2 + ev3
        adjusted = sum_parts * (1 - cong_disc / 100)
        group_ev = adjusted - central
        equity = group_ev - net_debt
        per_share = equity / shares if shares else 0
        unlock = sum_parts - adjusted  # value lost to the discount

        k1, k2, k3 = st.columns(3)
        k1.metric("Sum of parts (EV)", money(sum_parts, dp=1) + "m")
        k2.metric(f"After {cong_disc}% discount", money(adjusted, dp=1) + "m")
        k3.metric("Equity value", money(equity, dp=1) + "m")

        k4, k5, k6 = st.columns(3)
        k4.metric("Group EV (after central)", money(group_ev, dp=1) + "m")
        k5.metric("Value per share", money(per_share, dp=2))
        k6.metric("Potential value unlock", money(unlock, dp=1) + "m",
                  help="Gap between sum-of-parts and discounted value")

        # divisional table
        div_df = pd.DataFrame(
            {
                "Division": ["Consumer", "Digital", "Industrial", "Sum of parts"],
                "EBITDA (€m)": [e1, e2, e3, e1 + e2 + e3],
                "Multiple": [f"{m1:.1f}×", f"{m2:.1f}×", f"{m3:.1f}×", "—"],
                "Enterprise Value (€m)": [ev1, ev2, ev3, sum_parts],
            }
        )
        div_df["EBITDA (€m)"] = div_df["EBITDA (€m)"].map(lambda v: f"{v:,.1f}")
        div_df["Enterprise Value (€m)"] = div_df["Enterprise Value (€m)"].map(lambda v: f"{v:,.1f}")
        st.markdown("##### 📄 Divisional Valuation")
        st.dataframe(div_df, use_container_width=True, hide_index=True)

        # contribution chart
        contrib = pd.DataFrame(
            {"Enterprise Value (€m)": [ev1, ev2, ev3]},
            index=["Consumer", "Digital", "Industrial"],
        )
        st.markdown("##### 📊 Value contribution by division")
        st.bar_chart(contrib)

        if cong_disc >= 15:
            st.warning(
                f"⚠️ A **{cong_disc}% conglomerate discount** destroys **{money(unlock, dp=1)}m** of value. "
                "A large gap like this is exactly what triggers break-up / spin-off proposals."
            )
        else:
            st.success(
                f"✅ Group equity value **{money(equity, dp=1)}m** ({money(per_share, dp=2)}/share). "
                f"The conglomerate discount costs {money(unlock, dp=1)}m."
            )

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    ce1, ce2 = st.columns(2)
    with ce1:
        st.markdown(
            """
1. **Hidden gem:** Raise the Digital multiple to 25×. See how a single high-growth unit lifts the whole group.
2. **Break-up case:** Push the conglomerate discount to 30%. How much value could a spin-off unlock?
"""
        )
    with ce2:
        st.markdown(
            """
3. **One multiple myth:** Set all three multiples to 10×. Notice how a blended approach mis-values the mix.
4. **Debt bridge:** Raise net debt to €150m. Watch equity value (and per-share) fall while EV is unchanged.
"""
        )

    st.download_button(
        "⬇️ Download this SOTP valuation (CSV)",
        div_df.to_csv(index=False).encode("utf-8"),
        "sum_of_the_parts_valuation.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Unlocking value in a multi-BU group", expanded=True):
        st.markdown(
            """
**Situation:** A diversified consumer group traded well below what its divisions seemed individually worth.

**How SOTP helped:** Valuing each business unit separately (a premium multiple for the fast-growth arm, a
lower one for the cyclical unit) showed the sum of parts exceeded the market cap by ~20% — a clear
**conglomerate discount**.

**Why it matters:** It quantified the value that could be released by simplifying the portfolio or spinning
off a division.

**Lesson:** SOTP is the standard tool for revealing value trapped inside diversified groups.
"""
        )

    with st.expander("Case B — The spin-off decision"):
        st.markdown(
            """
**Situation:** A board debated whether to spin off a high-growth division that was 'lost' inside a
low-multiple industrial group.

**How SOTP helped:** The analysis showed the digital unit alone, valued at its own peer multiple, was worth
a large fraction of the entire group's market cap. Separately listed, it could command that higher multiple
directly.

**Why it matters:** SOTP turned a strategic hunch into a quantified value case for the spin-off.

**Lesson:** SOTP underpins virtually every break-up, spin-off, and demerger decision.
"""
        )

    with st.expander("Case C — Choosing the right method per division"):
        st.markdown(
            """
**Situation:** A group contained a mature cash cow, a pre-profit start-up, and a minority stake in a
listed company.

**How SOTP helped:** Each got the appropriate method — **DCF** for the cash cow, **EV/Sales** for the
loss-making start-up, and the **market price** for the listed stake. Forcing one multiple on all three
would have badly mispriced the group.

**Why it matters:** SOTP's flexibility to mix methods is precisely what makes it accurate for complex groups.

**Lesson:** Match the valuation method to each division's nature — that's the essence of a good SOTP.
"""
        )

    st.info(
        "🔗 **Pattern:** SOTP shines wherever a business is really several businesses. It reveals hidden "
        "value, quantifies the conglomerate discount, and provides the analytical backbone for break-up and "
        "spin-off decisions."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_35"):
        q1 = st.radio(
            "**1.** Sum-of-the-Parts (SOTP) valuation works by:",
            [
                "Applying a single group multiple to total EBITDA",
                "Valuing each business unit separately and summing them",
                "Only discounting group dividends",
                "Using the group's book value",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** SOTP is MOST appropriate for:",
            [
                "A single-product start-up",
                "A diversified conglomerate with several distinct divisions",
                "A company with no revenue",
                "Valuing a single bond",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Why apply different multiples to different divisions?",
            [
                "To make the model longer",
                "Because divisions differ in growth, margins and risk, so they merit different multiples",
                "Because tax rules require it",
                "To hide the group's debt",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A conglomerate discount means the group trades:",
            [
                "Above the sum of its parts",
                "Below the sum of its parts, due to complexity/inefficiency",
                "Exactly at the sum of its parts",
                "At its book value",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** A large conglomerate discount often motivates:",
            [
                "Issuing more debt",
                "A break-up or spin-off to unlock the trapped value",
                "Cutting the dividend to zero",
                "Switching to a single group multiple",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Valuing each business unit separately and summing them"),
            "2": (q2, "A diversified conglomerate with several distinct divisions"),
            "3": (q3, "Because divisions differ in growth, margins and risk, so they merit different multiples"),
            "4": (q4, "Below the sum of its parts, due to complexity/inefficiency"),
            "5": (q5, "A break-up or spin-off to unlock the trapped value"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've completed Part 3 (Valuation)! On to Part 4 (Investment Appraisal). 🎉")
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
    f"Applied Financial Models · Module 3.5 Sum-of-the-Parts (SOTP) · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
