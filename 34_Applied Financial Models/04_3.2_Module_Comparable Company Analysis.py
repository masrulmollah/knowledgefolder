"""
================================================================================
APPLIED FINANCIAL MODELS
Module 3.2 — COMPARABLE COMPANY ANALYSIS ("COMPS")
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to value a business using trading multiples: EV/EBITDA, P/E, EV/Sales, peer
selection, and applying the peer multiple to a target.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live comps table + valuation engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_3_2_Comparable_Company_Analysis.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="3.2 Comparable Company Analysis — Applied Financial Models",
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
**Module 3.2 — Comparable Company Analysis**

🔴 *Advanced*

**You will learn to:**
- Select a credible peer group
- Calculate trading multiples (EV/EBITDA, P/E)
- Apply peer multiples to value a target
- Triangulate Comps with a DCF
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to build a live comps table, "
    "pick your peers, and value a target company from their multiples."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("💰 3.2 · Comparable Company Analysis (\"Comps\")")
st.markdown(
    """
Where the DCF (3.1) values a business from its own fundamentals, **Comps** values it *relative to the
market* — the logic being that **similar companies should trade at similar multiples**. If comparable
firms trade at 8× EBITDA, a similar business is probably worth roughly 8× its EBITDA too.

Comps are fast, market-based, and a vital **cross-check** on any DCF. This module covers peer selection,
the key multiples, and how to apply them to value a target.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "3.2")
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
### The core idea: relative valuation
Comps rest on the **law of one price** — assets with similar risk and cash flows should sell for similar
prices. We express "price" as a **multiple** of a financial metric, so businesses of different sizes can
be compared on a like-for-like basis.
"""
    )
    st.latex(r"\text{Value of Target} = \text{Peer Multiple} \times \text{Target's Metric}")

    st.markdown("### The key trading multiples")
    mult = pd.DataFrame(
        {
            "Multiple": ["EV / EBITDA", "EV / Sales", "P / E", "EV / EBIT"],
            "Formula": [
                "Enterprise Value ÷ EBITDA",
                "Enterprise Value ÷ Revenue",
                "Share Price ÷ Earnings per Share (or Equity Value ÷ Net Income)",
                "Enterprise Value ÷ EBIT",
            ],
            "Best for / notes": [
                "The workhorse — capital-structure neutral, ignores D&A policy",
                "Loss-making / early-stage firms with no earnings yet",
                "Equity investors' favourite, but distorted by leverage & tax",
                "Like EV/EBITDA but after depreciation (capital-intensity matters)",
            ],
        }
    )
    st.table(mult)

    with st.expander("🔑 Concept 1 — Enterprise value vs. equity multiples"):
        st.markdown(
            """
- **EV multiples** (EV/EBITDA, EV/Sales) value the *whole firm* — independent of how it's financed.
  Pair them with **pre-financing** metrics (EBITDA, sales, EBIT).
- **Equity multiples** (P/E) value only the *shareholders' stake*. Pair them with **post-financing**
  metrics (net income, EPS).

**Golden rule:** never mix them — an EV multiple must sit on an EV-level metric, an equity multiple on an
equity-level metric. Mixing is a classic error.
"""
        )

    with st.expander("🔑 Concept 2 — Choosing the peer group (the hard part)"):
        st.markdown(
            """
Comps live or die on peer selection. Good comparables share:
- **Industry / business model** (same sector, similar products)
- **Size** (revenue/market cap in a similar range)
- **Growth & margins** (similar profitability profile)
- **Geography & risk** (similar markets and regulation)

A weak peer group produces a misleading multiple — *"comparable"* is doing a lot of work in the name.
Always disclose and justify your peer set.
"""
        )

    with st.expander("🔑 Concept 3 — Mean vs. median (use the median)"):
        st.markdown(
            """
Peer multiples often contain **outliers** (a firm in a takeover, or a temporary earnings dip). The
**median** is more robust than the mean because it isn't dragged around by extremes. Most practitioners
apply the **median** (or an interquartile range) of the peer multiples to the target.
"""
        )

    with st.expander("🔑 Concept 4 — Trading comps vs. transaction comps"):
        st.markdown(
            """
- **Trading comps** (this module): multiples of *publicly traded* peers right now — reflect standalone
  market value.
- **Transaction comps** (Module 3.3): multiples paid in *actual M&A deals* — include a **control premium**
  and expected synergies, so they're usually higher.

Use trading comps for standalone value; transaction comps when valuing for an acquisition.
"""
        )

    with st.expander("🔑 Concept 5 — Comps vs. DCF: triangulate"):
        st.markdown(
            """
- **DCF** = intrinsic, fundamentals-based, forward-looking (but assumption-sensitive).
- **Comps** = market-based, fast, reality-checked by real prices (but inherits market sentiment and
  depends on peer quality).

Best practice: run **both** and present a **valuation range** where they overlap. If they diverge widely,
investigate why — one set of assumptions needs revisiting.
"""
        )

    st.success(
        "**Takeaway:** Comps value a business relative to similar companies using multiples. Match EV "
        "multiples to EV metrics, choose peers carefully, use the median, and always triangulate with a DCF."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — Valuing a target with EV/EBITDA")
    st.markdown("Valuing a target company with **€10,000,000 EBITDA** using a peer group.")

    st.markdown("#### Step 1 — Gather the peer group's multiples")
    st.markdown(
        """
| Peer | Enterprise Value | EBITDA | EV/EBITDA |
|---|---|---|---|
| Peer A | €80m | €10m | 8.0× |
| Peer B | €126m | €18m | 7.0× |
| Peer C | €90m | €10m | 9.0× |
| Peer D | €170m | €20m | 8.5× |
| Peer E (outlier — in a takeover) | €150m | €10m | 15.0× |
"""
    )

    st.markdown("#### Step 2 — Choose the representative multiple (use the median)")
    st.markdown(
        """
Sorted multiples: 7.0×, 8.0×, **8.5×**, 9.0×, 15.0×

- **Mean** = 9.5× (dragged up by the 15.0× outlier — misleading)
- **Median** = **8.5×** (robust to the outlier — use this)
"""
    )

    st.markdown("#### Step 3 — Apply to the target")
    st.markdown(
        """
$$\\text{Enterprise Value} = \\text{Median EV/EBITDA} \\times \\text{Target EBITDA}$$
$$= 8.5\\times \\times €10{,}000{,}000 = \\mathbf{€85{,}000{,}000}$$

Then bridge to equity (if the target has €15m net debt):
$$\\text{Equity Value} = €85m - €15m = \\mathbf{€70{,}000{,}000}$$
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Median EV/EBITDA", "8.5×")
    e2.metric("Enterprise Value", "€85,000,000")
    e3.metric("Equity Value", "€70,000,000", help="EV − €15m net debt")

    st.info(
        "**Insight:** Using the **mean (9.5×)** would have valued the target at €95m — €10m too high — "
        "because one peer in a takeover distorted the average. The **median (8.5×)** gives a more defensible "
        "€85m. This is why practitioners lean on the median. Cross-check against a DCF before concluding."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Build a Comps Table & Value a Target")
    st.markdown(
        "Select which peers to include, choose the multiple, and value the target. Watch how including or "
        "excluding an outlier changes the answer."
    )

    # Preset peer data
    peers = pd.DataFrame(
        {
            "Peer": ["Peer A", "Peer B", "Peer C", "Peer D", "Peer E (takeover)"],
            "EV (€m)": [80.0, 126.0, 90.0, 170.0, 150.0],
            "EBITDA (€m)": [10.0, 18.0, 10.0, 20.0, 10.0],
            "Net Income (€m)": [5.0, 9.0, 5.5, 11.0, 4.0],
            "Equity Value (€m)": [65.0, 100.0, 72.0, 140.0, 130.0],
        }
    )
    peers["EV/EBITDA"] = peers["EV (€m)"] / peers["EBITDA (€m)"]
    peers["P/E"] = peers["Equity Value (€m)"] / peers["Net Income (€m)"]

    left, right = st.columns([0.42, 0.58])

    with left:
        st.markdown("##### 🏢 Select peers to include")
        included = []
        for i, row in peers.iterrows():
            default = row["Peer"] != "Peer E (takeover)"  # exclude outlier by default
            if st.checkbox(
                f"{row['Peer']}  ·  EV/EBITDA {row['EV/EBITDA']:.1f}×  ·  P/E {row['P/E']:.1f}×",
                value=default, key=f"peer_{i}",
            ):
                included.append(i)

        st.markdown("##### ⚙️ Valuation settings")
        multiple_choice = st.radio("Multiple to use", ["EV/EBITDA", "P/E"], horizontal=True)
        stat = st.radio("Central statistic", ["Median (recommended)", "Mean"], horizontal=True)

        st.markdown("##### 🎯 Target company")
        target_ebitda = st.number_input("Target EBITDA (€m)", 0.1, 1000.0, 10.0, 0.5)
        target_ni = st.number_input("Target Net Income (€m)", 0.1, 1000.0, 5.5, 0.5)
        target_net_debt = st.number_input("Target Net Debt (€m)", -500.0, 1000.0, 15.0, 1.0)

    with right:
        if not included:
            st.warning("Select at least one peer to build the comps table.")
        else:
            sel = peers.loc[included]
            st.markdown("##### 📊 Comps Table (selected peers)")
            show = sel[["Peer", "EV (€m)", "EBITDA (€m)", "EV/EBITDA", "P/E"]].copy()
            show["EV/EBITDA"] = show["EV/EBITDA"].map(lambda v: f"{v:.1f}×")
            show["P/E"] = show["P/E"].map(lambda v: f"{v:.1f}×")
            st.dataframe(show, use_container_width=True, hide_index=True)

            mult_vals = list(sel[multiple_choice])
            chosen = median(mult_vals) if stat.startswith("Median") else sum(mult_vals) / len(mult_vals)

            # Apply multiple
            if multiple_choice == "EV/EBITDA":
                ev = chosen * target_ebitda
                equity = ev - target_net_debt
            else:  # P/E → equity value directly
                equity = chosen * target_ni
                ev = equity + target_net_debt

            k1, k2, k3 = st.columns(3)
            k1.metric(f"{stat.split()[0]} {multiple_choice}", f"{chosen:.1f}×")
            k2.metric("Implied Enterprise Value", money(ev, dp=1) + "m")
            k3.metric("Implied Equity Value", money(equity, dp=1) + "m")

            # median vs mean comparison
            med = median(mult_vals)
            mean = sum(mult_vals) / len(mult_vals)
            if abs(mean - med) / med > 0.10 if med else False:
                st.warning(
                    f"⚠️ Mean ({mean:.1f}×) and median ({med:.1f}×) differ by >10% — an **outlier** is "
                    "likely distorting the mean. The median is the safer choice."
                )
            else:
                st.success(
                    f"✅ Mean ({mean:.1f}×) and median ({med:.1f}×) are close — the peer set looks consistent."
                )

            # range chart
            rng = pd.DataFrame(
                {"Multiple (×)": mult_vals}, index=list(sel["Peer"])
            )
            st.markdown("##### 📈 Peer multiple spread")
            st.bar_chart(rng)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Outlier effect:** Tick 'Peer E (takeover)' to include it. Watch the mean jump — and the warning fire.
   Compare the valuation with and without it.
2. **Multiple choice:** Switch between EV/EBITDA and P/E. Do they give a similar equity value?
"""
        )
    with e2:
        st.markdown(
            """
3. **Peer quality:** Include only Peers A & C (both ~8–9×). How tight is the valuation range now?
4. **Debt bridge:** Raise target net debt to €40m. EV stays put, but equity value falls — see the bridge.
"""
        )

    st.caption("🧠 Comps give a *range*, not a single truth. Present the spread and triangulate with the "
               "DCF from Module 3.1.")

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Sanity-checking a DCF", expanded=True):
        st.markdown(
            """
**Situation:** A DCF valued a business at €120m, but management were unsure if it was realistic.

**How Comps helped:** Peers traded at a median 8× EBITDA. With €12m EBITDA, Comps implied ~€96m — well
below the DCF. The gap traced to an over-optimistic terminal growth rate in the DCF.

**Why it matters:** Comps provided a market reality check that exposed an aggressive DCF assumption.

**Lesson:** Always triangulate — when DCF and Comps diverge, investigate *why* before trusting either.
"""
        )

    with st.expander("Case B — The peer group that wasn't comparable"):
        st.markdown(
            """
**Situation:** An analyst valued a small, slow-growth manufacturer using high-growth tech peers trading
at 20× EBITDA — producing an absurdly high value.

**What went wrong:** The 'peers' shared neither growth, margins, nor risk. The multiple reflected a
completely different business profile.

**The fix:** Rebuild the peer set with genuinely similar manufacturers (~7× EBITDA), giving a credible value.

**Lesson:** A multiple is only as good as the peer group behind it — comparability is everything.
"""
        )

    with st.expander("Case C — Valuing a loss-making company (EV/Sales)"):
        st.markdown(
            """
**Situation:** A fast-growing but currently loss-making company had negative EBITDA and no earnings, so
EV/EBITDA and P/E were meaningless.

**How Comps helped:** Analysts used **EV/Sales** from comparable growth companies to establish a value
based on revenue scale until profitability arrived.

**Why it matters:** The right multiple depends on the company's stage — no single multiple fits all.

**Lesson:** Match the multiple to the situation; use EV/Sales when earnings-based multiples break down.
"""
        )

    st.info(
        "🔗 **Pattern:** Comps are fast and market-grounded, but only as reliable as the peer group and the "
        "matching of multiple to metric. Their greatest value is as a cross-check that keeps a DCF honest."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_32"):
        q1 = st.radio(
            "**1.** Comparable company analysis values a business by:",
            [
                "Discounting its own future cash flows",
                "Applying multiples from similar companies to the target's metrics",
                "Adding up the book value of its assets",
                "Using only its dividend history",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The EV/EBITDA multiple is popular mainly because it:",
            [
                "Depends heavily on the company's tax rate",
                "Is capital-structure neutral and ignores D&A policy differences",
                "Only works for loss-making firms",
                "Requires no peer group",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Which pairing is CORRECT?",
            [
                "EV multiple applied to net income",
                "P/E multiple applied to EBITDA",
                "EV/EBITDA applied to EBITDA (both enterprise-level)",
                "P/E applied to enterprise value",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** Why do practitioners usually use the MEDIAN of peer multiples rather than the mean?",
            [
                "The median is always higher",
                "The median is more robust to outliers (e.g. a peer in a takeover)",
                "The mean cannot be calculated",
                "Tax rules require the median",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** The best practice when valuing a business is to:",
            [
                "Rely only on a DCF",
                "Rely only on Comps",
                "Use both DCF and Comps and triangulate to a valuation range",
                "Use the highest number available",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "Applying multiples from similar companies to the target's metrics"),
            "2": (q2, "Is capital-structure neutral and ignores D&A policy differences"),
            "3": (q3, "EV/EBITDA applied to EBITDA (both enterprise-level)"),
            "4": (q4, "The median is more robust to outliers (e.g. a peer in a takeover)"),
            "5": (q5, "Use both DCF and Comps and triangulate to a valuation range"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered Comps! On to Module 3.3 (Precedent Transactions). 🎉")
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
    f"Applied Financial Models · Module 3.2 Comparable Company Analysis · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
