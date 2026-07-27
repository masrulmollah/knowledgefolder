"""
================================================================================
APPLIED FINANCIAL MODELS
Module 6.2 — M&A / ACCRETION-DILUTION MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to assess whether an acquisition increases (accretive) or decreases
(dilutive) the acquirer's EPS: deal structuring (cash vs. stock), financing,
synergies, and the pro-forma EPS bridge.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live accretion/dilution engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_6_2_MA_Accretion_Dilution_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="6.2 M&A Accretion-Dilution — Applied Financial Models",
    layout="wide",
    page_icon="🚀",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def run_accretion_dilution(
    acq_ni, acq_shares, acq_price,
    target_ni, offer_equity_value,
    pct_stock, synergies, interest_rate, tax_rate,
):
    """
    Compute pro-forma EPS and accretion/dilution.
    - Stock portion: new shares issued at acquirer's price.
    - Cash portion: assumed debt-funded, incurring after-tax interest.
    Returns a dict of results.
    """
    acq_eps = acq_ni / acq_shares if acq_shares else 0

    stock_consideration = offer_equity_value * pct_stock / 100
    cash_consideration = offer_equity_value - stock_consideration

    new_shares = stock_consideration / acq_price if acq_price else 0
    after_tax_interest = cash_consideration * interest_rate / 100 * (1 - tax_rate / 100)
    after_tax_synergies = synergies * (1 - tax_rate / 100)

    combined_ni = acq_ni + target_ni + after_tax_synergies - after_tax_interest
    combined_shares = acq_shares + new_shares
    pro_forma_eps = combined_ni / combined_shares if combined_shares else 0

    accretion = pro_forma_eps - acq_eps
    accretion_pct = (accretion / acq_eps * 100) if acq_eps else 0

    return {
        "acq_eps": acq_eps, "stock_consideration": stock_consideration,
        "cash_consideration": cash_consideration, "new_shares": new_shares,
        "after_tax_interest": after_tax_interest, "after_tax_synergies": after_tax_synergies,
        "combined_ni": combined_ni, "combined_shares": combined_shares,
        "pro_forma_eps": pro_forma_eps, "accretion": accretion, "accretion_pct": accretion_pct,
    }


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 6 · Specialised & Advanced Models")
st.sidebar.markdown(
    """
**Module 6.2 — M&A / Accretion-Dilution**

🔴 *Advanced*

**You will learn to:**
- Test if a deal is accretive or dilutive
- Structure cash vs. stock consideration
- Fold in synergies & financing cost
- Build a pro-forma EPS bridge
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to run a live accretion/dilution "
    "test — change the cash/stock mix and synergies and watch EPS move."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🚀 6.2 · M&A / Accretion-Dilution Model")
st.markdown(
    """
When one company acquires another, the first question the market asks is: *"Will this deal increase or
decrease the acquirer's earnings per share (EPS)?"* If EPS rises, the deal is **accretive**; if it falls,
it's **dilutive**. Accretion-dilution analysis is the quick, powerful test that shapes almost every M&A
decision.

This module builds the model: combining the two companies' earnings, accounting for how the deal is paid
for (**cash vs. stock**), adding **synergies**, and computing the **pro-forma EPS**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "6.2")
c2.metric("Part", "6 — Specialised")
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
### The core question: accretive or dilutive?
"""
    )
    st.latex(r"\text{Pro-forma EPS} = \frac{\text{Combined Net Income (incl. synergies, less financing cost)}}{\text{Combined Share Count}}")
    st.markdown(
        """
- If **Pro-forma EPS > Acquirer's standalone EPS** → the deal is **accretive** (good for EPS).
- If **Pro-forma EPS < Acquirer's standalone EPS** → the deal is **dilutive** (bad for EPS).
"""
    )

    st.markdown("### The building blocks of pro-forma net income")
    blocks = pd.DataFrame(
        {
            "Component": ["Acquirer net income", "+ Target net income", "+ After-tax synergies",
                          "− After-tax interest on new debt", "= Combined net income"],
            "Effect on EPS": [
                "Base earnings", "Adds the target's earnings", "Boosts earnings (cost/revenue gains)",
                "Reduces earnings (cost of cash-funding)", "The numerator of pro-forma EPS",
            ],
        }
    )
    st.table(blocks)

    with st.expander("🔑 Concept 1 — Cash vs. stock consideration"):
        st.markdown(
            """
How the acquirer pays changes everything:
- **Cash deal** (often debt-funded): **no new shares** issued, but the acquirer incurs **after-tax
  interest** on the debt. No change to share count.
- **Stock deal:** the acquirer **issues new shares** to pay the seller — **increasing the share count**
  (the denominator), which dilutes EPS unless the target adds enough earnings.

Most deals are a **mix** of cash and stock, blending both effects.
"""
        )

    with st.expander("🔑 Concept 2 — The quick accretion/dilution rule (P/E test)"):
        st.markdown(
            """
A famous shortcut for **all-stock** deals:
- If the acquirer's **P/E > target's P/E** (acquirer is 'more expensive'), the deal is generally
  **accretive**.
- If the acquirer's **P/E < target's P/E**, it's generally **dilutive**.

Intuition: a high-P/E acquirer issues relatively few shares to buy a given amount of the target's
earnings, so EPS rises. This rule guides deal structuring before any detailed modelling.
"""
        )

    with st.expander("🔑 Concept 3 — Synergies (the value justification)"):
        st.markdown(
            """
**Synergies** are the extra value from combining the two firms:
- **Cost synergies** — eliminating duplicate functions, procurement scale, plant consolidation (most
  reliable).
- **Revenue synergies** — cross-selling, wider distribution (harder to realise).

Synergies are added (after tax) to combined net income and can turn a dilutive deal accretive. But
acquirers routinely **over-estimate** them — so they must be scrutinised, not assumed.
"""
        )

    with st.expander("🔑 Concept 4 — Why accretion isn't everything"):
        st.markdown(
            """
Accretion/dilution is a fast EPS screen, **not** a full value test:
- A deal can be **accretive but value-destroying** (e.g. overpaying, funded with cheap debt that flatters
  EPS while adding risk).
- A deal can be **dilutive but value-creating** (e.g. buying a high-growth business whose earnings will
  compound).

Always pair the EPS test with a proper **valuation** (DCF/Comps) and a look at the **control premium**
paid (Module 3.3).
"""
        )

    with st.expander("🔑 Concept 5 — The pro-forma bridge"):
        st.markdown(
            """
A clean way to present the analysis is an **EPS bridge**: start from the acquirer's standalone EPS, then
show each effect — target earnings (+), synergies (+), new-share dilution (−), financing interest (−) —
arriving at pro-forma EPS. It makes crystal clear *why* the deal is accretive or dilutive.
"""
        )

    st.success(
        "**Takeaway:** Accretion-dilution tests whether a deal raises or lowers the acquirer's EPS. Cash "
        "deals add interest cost; stock deals add shares; synergies help. It's a vital quick screen — but "
        "always confirm with a full valuation, because accretion ≠ value creation."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Is the deal accretive or dilutive?")
    st.markdown("Acquirer 'BigCo' plans to buy 'SmallCo'.")

    st.markdown("#### The players")
    st.markdown(
        """
| | BigCo (acquirer) | SmallCo (target) |
|---|---|---|
| Net income | €100m | €20m |
| Shares | 50m | — |
| Share price | €40 | — |
| **EPS** | **€2.00** | — |
| Offer (equity value) | — | €300m |
"""
    )

    st.markdown("#### Scenario A — 100% stock deal")
    st.markdown(
        """
- New shares issued = €300m ÷ €40 = **7.5m shares**
- Combined net income = €100m + €20m = **€120m**
- Combined shares = 50m + 7.5m = **57.5m**
- Pro-forma EPS = €120m ÷ 57.5m = **€2.087**

$$\\text{Accretion} = \\frac{2.087 - 2.00}{2.00} = \\mathbf{+4.3\\% \\text{ (accretive)}}$$
"""
    )

    st.markdown("#### Scenario B — 100% cash deal (debt at 6%, tax 30%)")
    st.markdown(
        """
- No new shares. After-tax interest = €300m × 6% × (1 − 30%) = **€12.6m**
- Combined net income = €100m + €20m − €12.6m = **€107.4m**
- Shares = 50m
- Pro-forma EPS = €107.4m ÷ 50m = **€2.148**

$$\\text{Accretion} = \\frac{2.148 - 2.00}{2.00} = \\mathbf{+7.4\\% \\text{ (accretive)}}$$
"""
    )

    a1, a2, a3 = st.columns(3)
    a1.metric("Standalone EPS", "€2.00")
    a2.metric("All-stock EPS", "€2.087", "+4.3% ✅")
    a3.metric("All-cash EPS", "€2.148", "+7.4% ✅")

    st.info(
        "**Insight:** Both structures are **accretive**, but the **cash deal is more accretive** here "
        "(+7.4% vs. +4.3%) because cheap debt (4.2% after tax) is 'cheaper' than issuing new equity. "
        "That's often true when interest rates are low — but the cash deal adds **debt and risk** to the "
        "balance sheet, which the EPS number alone doesn't show. **Structure matters as much as price.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Live Accretion/Dilution Engine")
    st.markdown(
        "Set the two companies, the offer, and the cash/stock mix. The model computes pro-forma EPS and "
        "tells you whether the deal is accretive or dilutive."
    )

    left, right = st.columns([0.36, 0.64])

    with left:
        st.markdown("##### 🏢 Acquirer")
        acq_ni = st.number_input("Acquirer net income (€m)", 1.0, 100_000.0, 100.0, 5.0)
        acq_shares = st.number_input("Acquirer shares (m)", 1.0, 100_000.0, 50.0, 1.0)
        acq_price = st.number_input("Acquirer share price (€)", 0.1, 10_000.0, 40.0, 1.0)

        st.markdown("##### 🎯 Target & offer")
        target_ni = st.number_input("Target net income (€m)", 0.0, 100_000.0, 20.0, 1.0)
        offer_equity = st.number_input("Offer / equity value (€m)", 1.0, 1_000_000.0, 300.0, 10.0)

        st.markdown("##### 🧩 Deal structure")
        pct_stock = st.slider("% funded by stock", 0, 100, 100, 5)
        synergies = st.number_input("Pre-tax annual synergies (€m)", 0.0, 100_000.0, 0.0, 1.0)
        interest_rate = st.slider("Interest rate on cash/debt (%)", 0.0, 20.0, 6.0, 0.5)
        tax_rate = st.slider("Tax rate (%)", 0.0, 45.0, 30.0, 1.0)

    with right:
        r = run_accretion_dilution(
            acq_ni, acq_shares, acq_price, target_ni, offer_equity,
            pct_stock, synergies, interest_rate, tax_rate,
        )

        k1, k2, k3 = st.columns(3)
        k1.metric("Acquirer standalone EPS", money(r["acq_eps"], dp=3))
        k2.metric("Pro-forma EPS", money(r["pro_forma_eps"], dp=3))
        k3.metric("Accretion / (Dilution)", f"{r['accretion_pct']:+.1f}%",
                  "Accretive ✅" if r["accretion"] >= 0 else "Dilutive ❌",
                  delta_color="normal" if r["accretion"] >= 0 else "inverse")

        if r["accretion"] >= 0:
            st.success(
                f"✅ **ACCRETIVE.** Pro-forma EPS of {money(r['pro_forma_eps'], dp=3)} is "
                f"{r['accretion_pct']:+.1f}% above the standalone {money(r['acq_eps'], dp=3)} — the deal "
                "increases EPS as structured."
            )
        else:
            st.error(
                f"❌ **DILUTIVE.** Pro-forma EPS of {money(r['pro_forma_eps'], dp=3)} is "
                f"{r['accretion_pct']:.1f}% below the standalone {money(r['acq_eps'], dp=3)} — the deal "
                "reduces EPS. Consider more cash funding, higher synergies, or a lower price."
            )

        # EPS bridge table
        bridge = pd.DataFrame(
            {
                "Component": [
                    "Acquirer net income", "+ Target net income", "+ After-tax synergies",
                    "− After-tax interest (cash portion)", "= Combined net income",
                    "Combined shares (m)", "Pro-forma EPS",
                ],
                "Value": [
                    money(acq_ni, dp=1) + "m", money(target_ni, dp=1) + "m",
                    money(r["after_tax_synergies"], dp=1) + "m",
                    money(-r["after_tax_interest"], dp=1) + "m",
                    money(r["combined_ni"], dp=1) + "m",
                    f"{r['combined_shares']:,.2f}m", money(r["pro_forma_eps"], dp=3),
                ],
            }
        )
        st.markdown("##### 📄 Pro-Forma EPS Bridge")
        st.dataframe(bridge, use_container_width=True, hide_index=True)

        d1, d2, d3 = st.columns(3)
        d1.metric("Stock consideration", money(r["stock_consideration"], dp=1) + "m")
        d2.metric("Cash consideration", money(r["cash_consideration"], dp=1) + "m")
        d3.metric("New shares issued", f"{r['new_shares']:,.2f}m")

        eps_chart = pd.DataFrame(
            {"EPS (€)": [r["acq_eps"], r["pro_forma_eps"]]},
            index=["Standalone", "Pro-forma"],
        )
        st.markdown("##### 📊 Standalone vs. Pro-forma EPS")
        st.bar_chart(eps_chart)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Cash vs. stock:** Slide '% funded by stock' from 100% to 0%. Does the deal get more or less accretive?
2. **Synergy rescue:** Set the offer high enough to make the deal dilutive, then add synergies until it
   flips back to accretive.
"""
        )
    with e2:
        st.markdown(
            """
3. **Overpaying:** Raise the offer value sharply. Watch a stock deal turn dilutive as more shares are issued.
4. **P/E rule check:** Note the acquirer's P/E vs. the implied target P/E — does the accretive/dilutive
   result match the quick rule?
"""
        )

    st.download_button(
        "⬇️ Download the EPS bridge (CSV)",
        bridge.to_csv(index=False).encode("utf-8"),
        "accretion_dilution_bridge.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Cash vs. stock changes the answer", expanded=True):
        st.markdown(
            """
**Situation:** An acquirer weighed paying for a target in cash (debt-funded) vs. its own shares.

**What the model revealed:** With low interest rates, the **cash deal was more accretive** (cheap debt
cost less than issuing equity), while the **all-stock deal** diluted EPS more by adding shares.

**Why it matters:** The *same* target at the *same* price can be accretive or dilutive purely based on how
it's financed — structure is a real lever.

**Lesson:** Always test multiple financing structures; the cash/stock mix can flip the EPS outcome.
"""
        )

    with st.expander("Case B — Synergies turning a dilutive deal accretive"):
        st.markdown(
            """
**Situation:** A proposed acquisition looked **dilutive** on a standalone basis — the target's earnings
weren't enough to offset the new shares issued.

**What the model revealed:** Credible **cost synergies** (plant consolidation, procurement scale) added
enough to combined net income to flip the deal to **accretive**.

**Why it matters:** Synergies are often the justification for a deal — but the model showed *exactly how
much* synergy was needed, creating a clear accountability target.

**Lesson:** Use the model to quantify the synergies required — then hold the deal team to delivering them.
"""
        )

    with st.expander("Case C — Accretive but value-destroying"):
        st.markdown(
            """
**Situation:** A deal was heavily promoted as 'EPS accretive' and won board approval on that basis.

**What was missed:** It was accretive only because it was funded with cheap debt — but the acquirer
**overpaid** far above the target's intrinsic value (DCF). EPS rose, yet shareholder *value* was destroyed,
and the added leverage raised risk.

**Why it matters:** Accretion is an accounting-EPS effect, not a value test. A deal can boost EPS while
still being a bad investment.

**Lesson:** Never approve a deal on accretion alone — always confirm with a valuation and the price paid.
"""
        )

    st.info(
        "🔗 **Pattern:** Accretion-dilution is the fast first screen every M&A team runs — but structure "
        "(cash vs. stock), synergies, and *especially* the price paid determine whether an accretive deal is "
        "also a *good* deal."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_62"):
        q1 = st.radio(
            "**1.** A deal is 'accretive' when:",
            [
                "The acquirer's pro-forma EPS is higher than its standalone EPS",
                "The acquirer's pro-forma EPS is lower than its standalone EPS",
                "The target is larger than the acquirer",
                "No synergies exist",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** In an all-STOCK deal, the acquirer's EPS is affected mainly because:",
            [
                "It pays after-tax interest on new debt",
                "It issues new shares, increasing the share count",
                "It pays no premium",
                "The tax rate changes",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** In an all-CASH (debt-funded) deal, the main EPS drag is:",
            [
                "New shares issued",
                "The after-tax interest cost on the debt",
                "A higher dividend",
                "Lower target earnings",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** By the quick P/E rule, an all-stock deal is generally accretive when:",
            [
                "The acquirer's P/E is lower than the target's P/E",
                "The acquirer's P/E is higher than the target's P/E",
                "Both have the same P/E",
                "Neither company has earnings",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Why is accretion/dilution NOT a complete test of a deal?",
            [
                "It always overstates synergies",
                "A deal can be accretive yet value-destroying (e.g. overpaying), so it must be paired with a valuation",
                "It cannot be calculated for cash deals",
                "It ignores the target's net income",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The acquirer's pro-forma EPS is higher than its standalone EPS"),
            "2": (q2, "It issues new shares, increasing the share count"),
            "3": (q3, "The after-tax interest cost on the debt"),
            "4": (q4, "The acquirer's P/E is higher than the target's P/E"),
            "5": (q5, "A deal can be accretive yet value-destroying (e.g. overpaying), so it must be paired with a valuation"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered accretion/dilution analysis! On to Module 6.3 (Project Finance). 🎉")
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
    f"Applied Financial Models · Module 6.2 M&A / Accretion-Dilution Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
