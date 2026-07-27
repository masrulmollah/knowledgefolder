"""
================================================================================
APPLIED FINANCIAL MODELS
Module 3.3 — PRECEDENT TRANSACTIONS
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to value a business using precedent M&A transactions: deal multiples,
control premiums, and how acquisition value differs from standalone trading value.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live deal-comps + control-premium engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_3_3_Precedent_Transactions.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="3.3 Precedent Transactions — Applied Financial Models",
    layout="wide",
    page_icon="💰",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def median(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return 0
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 3 · Valuation Models")
st.sidebar.markdown(
    """
**Module 3.3 — Precedent Transactions**

🔴 *Advanced*

**You will learn to:**
- Value using past M&A deal multiples
- Understand the control premium
- Distinguish deal value from trading value
- Choose relevant precedent transactions
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to value an acquisition target "
    "from deal multiples and see the control premium in action."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("💰 3.3 · Precedent Transactions")
st.markdown(
    """
**Precedent transaction analysis** values a business by looking at the multiples **actually paid** in
comparable past M&A deals. If similar companies were recently acquired at 10× EBITDA, that's strong
evidence of what an acquirer might pay for a similar target today.

The key difference from trading comps (3.2): deal prices include a **control premium** — the extra an
acquirer pays to own and control the whole business — so precedent-transaction multiples are typically
**higher** than trading multiples.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "3.3")
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
Precedent transactions (also called "deal comps" or "transaction comps") value a target using multiples
paid in **completed acquisitions** of similar companies. The logic mirrors trading comps, but the data
comes from **actual deals**, not current share prices.
"""
    )
    st.latex(r"\text{Value of Target} = \text{Median Deal Multiple} \times \text{Target's Metric}")

    st.markdown("### Trading comps vs. precedent transactions")
    comparison = pd.DataFrame(
        {
            "Aspect": ["Data source", "Reflects", "Includes control premium?", "Includes synergies?", "Typical level"],
            "Trading Comps (3.2)": [
                "Current public share prices", "Standalone / minority market value",
                "No", "No", "Lower",
            ],
            "Precedent Transactions (3.3)": [
                "Prices paid in past M&A deals", "Full acquisition (control) value",
                "Yes", "Often (paid for by acquirer)", "Higher",
            ],
        }
    )
    st.table(comparison)

    with st.expander("🔑 Concept 1 — The control premium"):
        st.markdown(
            """
A **control premium** is the amount an acquirer pays *above* the standalone trading price to gain control
of a company — typically **20–40%**.

$$\\text{Offer Price} = \\text{Unaffected Share Price} \\times (1 + \\text{Control Premium})$$

Why pay it? Control lets the buyer set strategy, appoint management, redirect cash flows, and capture
**synergies**. Precedent-transaction multiples already *embed* this premium — which is why they exceed
trading multiples.
"""
        )

    with st.expander("🔑 Concept 2 — Why deal multiples run higher"):
        st.markdown(
            """
Precedent multiples are usually higher than trading multiples for two reasons:
1. **Control premium** — the buyer pays for control.
2. **Synergies** — the buyer expects cost/revenue benefits and may share some of that value with the seller.

So precedent transactions answer *"what would someone pay to buy this whole business?"* — the right lens
for an **acquisition**, but an overstatement of standalone value.
"""
        )

    with st.expander("🔑 Concept 3 — Choosing relevant transactions"):
        st.markdown(
            """
Good precedent deals are:
- **Similar target** — same industry, size, business model.
- **Recent** — market conditions change; old deals may reflect a different environment.
- **Comparable deal type** — strategic vs. financial buyer, full vs. partial acquisition.

Beware: deal data can be **stale** or **scarce**, and reported multiples sometimes exclude undisclosed
earn-outs or assumed debt. Fewer, high-quality precedents beat many loose ones.
"""
        )

    with st.expander("🔑 Concept 4 — Strengths & weaknesses"):
        st.markdown(
            """
- ✅ **Strengths:** based on real prices actually paid; naturally reflects what acquirers will pay;
  ideal for M&A and control situations.
- ⚠️ **Weaknesses:** deals can be old (stale market conditions); each deal has unique circumstances
  (competitive auction, distressed seller); data is often incomplete or hard to source.

Use precedent transactions **alongside** trading comps and a DCF — never in isolation.
"""
        )

    st.success(
        "**Takeaway:** Precedent transactions value a business at *acquisition* (control) value using "
        "multiples actually paid in past deals. They embed a control premium and synergies, so they sit "
        "above trading comps — the right tool when someone is buying the whole company."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Valuing an acquisition target")
    st.markdown("Valuing a target with **€10,000,000 EBITDA** for a potential acquisition.")

    st.markdown("#### Step 1 — Gather precedent deal multiples")
    st.markdown(
        """
| Deal | Target | Deal EV | Target EBITDA | EV/EBITDA paid |
|---|---|---|---|---|
| Deal 1 | Company P | €108m | €12m | 9.0× |
| Deal 2 | Company Q | €150m | €15m | 10.0× |
| Deal 3 | Company R | €95m | €10m | 9.5× |
| Deal 4 | Company S | €210m | €20m | 10.5× |
"""
    )

    st.markdown("#### Step 2 — Use the median deal multiple")
    st.markdown(
        """
Sorted: 9.0×, 9.5×, 10.0×, 10.5× → **Median = 9.75×**

*(Compare with trading comps from Module 3.2, which sat around 8.5× — the ~1.25× uplift reflects the
control premium and synergies embedded in deal prices.)*
"""
    )

    st.markdown("#### Step 3 — Apply to the target")
    st.markdown(
        """
$$\\text{Deal Enterprise Value} = 9.75\\times \\times €10{,}000{,}000 = \\mathbf{€97{,}500{,}000}$$

Bridge to equity (target has €15m net debt):
$$\\text{Equity Value} = €97.5m - €15m = \\mathbf{€82{,}500{,}000}$$
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Median deal multiple", "9.75×")
    e2.metric("Deal Enterprise Value", "€97,500,000")
    e3.metric("Deal Equity Value", "€82,500,000", help="EV − €15m net debt")

    st.markdown("#### Step 4 — Compare the three lenses")
    st.markdown(
        """
| Method | EV/EBITDA | Enterprise Value | What it represents |
|---|---|---|---|
| Trading Comps (3.2) | 8.5× | €85.0m | Standalone market value |
| **Precedent Transactions (3.3)** | **9.75×** | **€97.5m** | **Acquisition (control) value** |
| Control premium implied | +14.7% | +€12.5m | What a buyer pays for control + synergies |
"""
    )

    st.info(
        "**Insight:** Precedent transactions value the target ~15% higher than trading comps — that gap is "
        "the **control premium**. For an *acquisition*, the €97.5m figure is the relevant benchmark; for a "
        "*standalone* valuation, the €85m trading value is more appropriate. **Match the method to the question.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Value a Target from Deal Comps")
    st.markdown(
        "Select which precedent deals to include, then value the acquisition target from the median deal "
        "multiple."
    )

    deals = pd.DataFrame(
        {
            "Deal": ["Deal 1 · Company P", "Deal 2 · Company Q", "Deal 3 · Company R",
                     "Deal 4 · Company S", "Deal 5 · Company T (distressed)"],
            "Deal EV (€m)": [108.0, 150.0, 95.0, 210.0, 60.0],
            "EBITDA (€m)": [12.0, 15.0, 10.0, 20.0, 10.0],
        }
    )
    deals["EV/EBITDA"] = deals["Deal EV (€m)"] / deals["EBITDA (€m)"]

    left, right = st.columns([0.42, 0.58])
    with left:
        st.markdown("##### 🤝 Select precedent deals")
        included = []
        for i, row in deals.iterrows():
            default = "distressed" not in row["Deal"]
            if st.checkbox(f"{row['Deal']}  ·  {row['EV/EBITDA']:.2f}×", value=default, key=f"deal_{i}"):
                included.append(i)

        st.markdown("##### 🎯 Target")
        target_ebitda = st.number_input("Target EBITDA (€m)", 0.1, 1000.0, 10.0, 0.5)
        target_net_debt = st.number_input("Target net debt (€m)", -500.0, 1000.0, 15.0, 1.0)
        trading_multiple = st.number_input("Trading-comp multiple (× for comparison)", 1.0, 50.0, 8.5, 0.25)

    with right:
        if not included:
            st.warning("Select at least one precedent deal.")
        else:
            sel = deals.loc[included]
            show = sel[["Deal", "Deal EV (€m)", "EBITDA (€m)", "EV/EBITDA"]].copy()
            show["EV/EBITDA"] = show["EV/EBITDA"].map(lambda v: f"{v:.2f}×")
            st.markdown("##### 📊 Precedent Transactions Table")
            st.dataframe(show, use_container_width=True, hide_index=True)

            med_deal = median(list(sel["EV/EBITDA"]))
            deal_ev = med_deal * target_ebitda
            deal_equity = deal_ev - target_net_debt

            trading_ev = trading_multiple * target_ebitda
            premium_pct = (med_deal / trading_multiple - 1) * 100 if trading_multiple else 0

            k1, k2, k3 = st.columns(3)
            k1.metric("Median deal multiple", f"{med_deal:.2f}×")
            k2.metric("Deal Enterprise Value", money(deal_ev, dp=1) + "m")
            k3.metric("Deal Equity Value", money(deal_equity, dp=1) + "m")

            k4, k5 = st.columns(2)
            k4.metric("Implied control premium", f"{premium_pct:,.1f}%",
                      help="Deal multiple vs. the trading multiple")
            k5.metric("Uplift vs. trading value", money(deal_ev - trading_ev, dp=1) + "m")

            if premium_pct < 0:
                st.warning(
                    "⚠️ Your deal multiple is **below** the trading multiple — unusual. A distressed deal in "
                    "the set may be dragging it down. Check whether that precedent is truly comparable."
                )
            elif premium_pct > 50:
                st.warning(
                    f"⚠️ Implied control premium of **{premium_pct:.0f}%** is very high (typical range 20–40%). "
                    "A competitive auction or synergy-rich deal may be inflating the precedents."
                )
            else:
                st.success(
                    f"✅ Implied control premium of **{premium_pct:.0f}%** — within the typical 20–40% range "
                    "for acquisitions."
                )

            comp = pd.DataFrame(
                {"Enterprise Value (€m)": [trading_ev, deal_ev]},
                index=["Trading comps (standalone)", "Precedent deals (control)"],
            )
            st.markdown("##### 📈 Standalone vs. acquisition value")
            st.bar_chart(comp)

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Control Premium Calculator")
    st.markdown("See how a control premium turns an unaffected share price into an offer price.")

    c1, c2, c3 = st.columns(3)
    with c1:
        unaffected = st.number_input("Unaffected share price (€)", 0.10, 1000.0, 20.00, 0.50)
        shares_m = st.number_input("Shares outstanding (m)", 0.1, 10_000.0, 10.0, 0.1)
    with c2:
        premium = st.slider("Control premium (%)", 0, 80, 30, 1)
    with c3:
        st.markdown("&nbsp;")

    offer_price = unaffected * (1 + premium / 100)
    market_cap = unaffected * shares_m
    offer_equity = offer_price * shares_m
    premium_paid = offer_equity - market_cap

    m1, m2, m3 = st.columns(3)
    m1.metric("Offer price per share", money(offer_price, dp=2))
    m2.metric("Offer equity value", money(offer_equity, dp=1) + "m")
    m3.metric("Premium paid (total)", money(premium_paid, dp=1) + "m",
              f"+{premium}% over market")

    st.caption(
        f"🧠 At a {premium}% premium, the acquirer pays **{money(offer_price, dp=2)}** per share vs. the "
        f"**{money(unaffected, dp=2)}** market price — a total premium of **{money(premium_paid, dp=1)}m** "
        "that must be justified by control and synergies."
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Setting the offer price for an acquisition", expanded=True):
        st.markdown(
            """
**Situation:** A strategic buyer wanted to acquire a competitor and needed to know a credible offer price.

**How precedent transactions helped:** Recent deals in the sector had been done at ~10× EBITDA — well
above the ~8× trading multiple. That told the buyer the market 'going rate' for **control** was around
10×, framing a realistic opening offer.

**Why it matters:** Bidding at the trading multiple would have been rejected instantly; precedent deals
revealed the true price of control.

**Lesson:** For an acquisition, precedent transactions — not trading comps — set the realistic price bar.
"""
        )

    with st.expander("Case B — The stale-precedent trap"):
        st.markdown(
            """
**Situation:** An analyst valued a target using deal multiples from a boom five years earlier, when
acquirers paid richly.

**What went wrong:** Market conditions had since cooled; those old multiples massively overstated what
buyers would now pay. The valuation was unrealistic.

**The fix:** Refresh the precedent set with **recent** deals reflecting current conditions.

**Lesson:** Precedent transactions are only as good as they are *recent* — market appetite changes.
"""
        )

    with st.expander("Case C — Justifying the control premium to the board"):
        st.markdown(
            """
**Situation:** A board questioned why management proposed paying a 35% premium over the target's share price.

**How the analysis helped:** By showing precedent deals routinely done at 25–40% premiums — and mapping
the premium to identified, quantified **synergies** — management demonstrated the premium was both
market-consistent and value-creating.

**Why it matters:** A premium is only justified if control + synergies exceed it; precedent data provides
the market benchmark.

**Lesson:** Use precedent premiums to benchmark your offer, but always back it with a real synergy case.
"""
        )

    st.info(
        "🔗 **Pattern:** Precedent transactions answer 'what do acquirers actually pay?'. They embed the "
        "control premium and synergies — invaluable for M&A pricing, but sensitive to deal recency and "
        "each deal's unique circumstances."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_33"):
        q1 = st.radio(
            "**1.** Precedent transaction analysis values a business using:",
            [
                "The company's own discounted cash flows",
                "Multiples actually paid in comparable past M&A deals",
                "The current book value of assets",
                "Only the dividend yield",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** Compared with trading comps, precedent-transaction multiples are typically:",
            [
                "Lower, because deals are distressed",
                "Higher, because they include a control premium (and often synergies)",
                "Exactly the same",
                "Always zero",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** A control premium is:",
            [
                "A discount for buying a minority stake",
                "The extra an acquirer pays above the standalone price to gain control (often 20–40%)",
                "The interest rate on acquisition debt",
                "A tax on mergers",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** A key risk when using precedent transactions is that:",
            [
                "They can only be used for loss-making firms",
                "Deals may be stale, reflecting different (often richer) market conditions",
                "They never include a control premium",
                "They ignore the target's industry",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** For valuing a business in a potential ACQUISITION, the most relevant method is:",
            [
                "Trading comps only",
                "Precedent transactions (they reflect control value actually paid)",
                "Book value",
                "The dividend discount model",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Multiples actually paid in comparable past M&A deals"),
            "2": (q2, "Higher, because they include a control premium (and often synergies)"),
            "3": (q3, "The extra an acquirer pays above the standalone price to gain control (often 20–40%)"),
            "4": (q4, "Deals may be stale, reflecting different (often richer) market conditions"),
            "5": (q5, "Precedent transactions (they reflect control value actually paid)"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered precedent transactions! On to Module 3.4 (Dividend Discount Model). 🎉")
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
    f"Applied Financial Models · Module 3.3 Precedent Transactions · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
