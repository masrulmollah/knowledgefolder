"""
================================================================================
APPLIED FINANCIAL MODELS
Module 3.4 — DIVIDEND DISCOUNT MODEL (DDM)
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how to value a company (equity) from its dividends: the Gordon Growth model and
multi-stage (two-stage) DDM.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (Gordon growth + two-stage DDM engines)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_3_4_Dividend_Discount_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="3.4 Dividend Discount Model — Applied Financial Models",
    layout="wide",
    page_icon="💰",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=2):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def gordon_growth(d1, ke_pct, g_pct):
    """Gordon growth value = D1 / (Ke - g)."""
    ke = ke_pct / 100
    g = g_pct / 100
    if ke <= g:
        return float("inf")
    return d1 / (ke - g)


def two_stage_ddm(d0, high_g_pct, high_years, terminal_g_pct, ke_pct):
    """
    Two-stage DDM: explicit high-growth dividends discounted, plus a Gordon-growth
    terminal value at the end of the high-growth phase.
    Returns schedule + summary.
    """
    ke = ke_pct / 100
    hg = high_g_pct / 100
    tg = terminal_g_pct / 100

    divs, dfs, pvs = [], [], []
    d = d0
    for y in range(1, high_years + 1):
        d = d * (1 + hg)
        df = 1 / ((1 + ke) ** y)
        pv = d * df
        divs.append(d)
        dfs.append(df)
        pvs.append(pv)

    sum_pv_divs = sum(pvs)

    last_div = divs[-1]
    if ke > tg:
        terminal_value = last_div * (1 + tg) / (ke - tg)
    else:
        terminal_value = float("inf")
    pv_terminal = terminal_value * dfs[-1] if terminal_value != float("inf") else float("inf")

    value = sum_pv_divs + pv_terminal
    tv_pct = (pv_terminal / value * 100) if value not in (0, float("inf")) else 0

    return {
        "divs": divs, "dfs": dfs, "pvs": pvs, "sum_pv_divs": sum_pv_divs,
        "terminal_value": terminal_value, "pv_terminal": pv_terminal,
        "value": value, "tv_pct": tv_pct,
    }


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 3 · Valuation Models")
st.sidebar.markdown(
    """
**Module 3.4 — Dividend Discount Model (DDM)**

🔴 *Advanced*

**You will learn to:**
- Value equity from expected dividends
- Apply the Gordon Growth model
- Build a two-stage (multi-stage) DDM
- Know when the DDM fits (and when it doesn't)
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab for a Gordon growth calculator "
    "and a two-stage DDM engine."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("💰 3.4 · Dividend Discount Model (DDM)")
st.markdown(
    """
The **Dividend Discount Model** values a company's **equity** directly, based on the principle that a
share is worth the **present value of all the dividends it will ever pay**. Where a DCF discounts *free
cash flow to the firm*, the DDM discounts the *cash actually returned to shareholders* — dividends.

It's especially useful for **stable, dividend-paying** businesses (mature industrials, banks, utilities).
This module covers the Gordon Growth model and the more flexible **two-stage DDM**.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "3.4")
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
A share entitles you to a stream of future **dividends**. The DDM says the fair value of the share today
is the **present value of that dividend stream**, discounted at the **cost of equity ($K_e$)** — the
return shareholders require.
"""
    )
    st.latex(r"P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+K_e)^t}")

    st.markdown("### The Gordon Growth Model (constant growth)")
    st.markdown(
        """
If dividends grow at a **constant rate g forever**, the infinite sum simplifies beautifully:
"""
    )
    st.latex(r"P_0 = \frac{D_1}{K_e - g} \qquad \text{where } D_1 = D_0 \times (1+g)")
    st.markdown(
        """
- $D_1$ = next year's expected dividend  •  $K_e$ = cost of equity  •  $g$ = perpetual dividend growth
- **Requirement:** $K_e > g$ (otherwise the value is infinite/meaningless).
"""
    )

    st.markdown("### When to use each variant")
    variants = pd.DataFrame(
        {
            "Model": ["Gordon Growth (single-stage)", "Two-Stage DDM", "Multi-Stage DDM"],
            "Assumes": [
                "One constant growth rate forever",
                "A high-growth phase, then stable perpetual growth",
                "Several distinct growth phases before stabilising",
            ],
            "Best for": [
                "Mature, stable dividend payers",
                "Companies growing fast now, maturing later",
                "Complex growth paths (e.g. early-stage → scale → mature)",
            ],
        }
    )
    st.table(variants)

    with st.expander("🔑 Concept 1 — Cost of equity (Ke) via CAPM"):
        st.markdown(
            """
The discount rate in a DDM is the **cost of equity** — the return shareholders demand. It's often
estimated with the **Capital Asset Pricing Model (CAPM)**:

$$K_e = R_f + \\beta \\times (R_m - R_f)$$

- $R_f$ = risk-free rate  •  $\\beta$ = the stock's sensitivity to the market  •  $(R_m - R_f)$ = equity
  risk premium.

A higher beta (riskier stock) → higher $K_e$ → lower valuation.
"""
        )

    with st.expander("🔑 Concept 2 — The two-stage DDM"):
        st.markdown(
            """
Few companies grow at one rate forever. The **two-stage DDM** handles this:
1. **Stage 1 (explicit):** discount each dividend through a high-growth phase (e.g. 5 years at 10%).
2. **Stage 2 (terminal):** apply Gordon Growth at a *sustainable* rate from then on, and discount that
   terminal value back to today.

$$P_0 = \\sum_{t=1}^{n} \\frac{D_t}{(1+K_e)^t} + \\frac{1}{(1+K_e)^n}\\times\\frac{D_{n+1}}{K_e - g_{stable}}$$

This mirrors the DCF's explicit-plus-terminal structure (Module 3.1) — but with dividends.
"""
        )

    with st.expander("🔑 Concept 3 — DDM vs. DCF"):
        st.markdown(
            """
| | DDM | DCF (FCFF) |
|---|---|---|
| Cash flow discounted | Dividends (to shareholders) | Free cash flow (to the firm) |
| Discount rate | Cost of equity ($K_e$) | WACC |
| Output | **Equity value** directly | **Enterprise value** (bridge to equity) |
| Best for | Stable dividend payers | Most companies, esp. non-dividend payers |

The DDM gives equity value *directly* (no net-debt bridge needed) because dividends already belong to
shareholders.
"""
        )

    with st.expander("🔑 Concept 4 — Strengths & limitations"):
        st.markdown(
            """
- ✅ **Strengths:** simple, transparent, directly values equity; excellent for stable dividend payers
  (utilities, mature banks, consumer staples).
- ⚠️ **Limitations:** useless for companies that **pay no dividends** (many growth/tech firms); very
  sensitive to $K_e$ and $g$; assumes dividends represent true value returned (buybacks are ignored).

For non-dividend payers, use a DCF or Comps instead.
"""
        )

    st.success(
        "**Takeaway:** The DDM values equity as the present value of future dividends. Use Gordon Growth for "
        "stable payers and a two-stage model when growth changes — but never for companies that don't pay dividends."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Examples")

    st.markdown("#### Example 1 — Gordon Growth (a stable dividend payer)")
    st.markdown(
        """
A mature company just paid a dividend of **€2.00** ($D_0$), expected to grow **3%** forever. Shareholders
require **9%** ($K_e$).

**Step 1 — next year's dividend:**
$$D_1 = €2.00 \\times (1 + 0.03) = €2.06$$

**Step 2 — apply Gordon Growth:**
$$P_0 = \\frac{D_1}{K_e - g} = \\frac{€2.06}{0.09 - 0.03} = \\frac{€2.06}{0.06} = \\mathbf{€34.33}$$
"""
    )
    g1, g2, g3 = st.columns(3)
    g1.metric("D₁ (next dividend)", "€2.06")
    g2.metric("Ke − g (spread)", "6.0%")
    g3.metric("Fair value per share", "€34.33")

    st.markdown("#### Example 2 — Two-stage DDM (growth then maturity)")
    st.markdown(
        """
A company pays **€1.00** now ($D_0$), growing **12%** for 4 years, then **3%** forever. $K_e$ = **10%**.

**Stage 1 — explicit dividends (12% growth), discounted at 10%:**

| Year | Dividend | Discount factor | PV |
|---|---|---|---|
| 1 | 1.120 | 0.9091 | 1.018 |
| 2 | 1.254 | 0.8264 | 1.037 |
| 3 | 1.405 | 0.7513 | 1.056 |
| 4 | 1.574 | 0.6830 | 1.075 |
| **Sum of PV (Stage 1)** | | | **€4.186** |
"""
    )
    st.markdown(
        """
**Stage 2 — terminal value at end of Year 4 (Gordon Growth at 3%):**
$$TV_4 = \\frac{D_4 \\times (1+g)}{K_e - g} = \\frac{1.574 \\times 1.03}{0.10 - 0.03} = €23.16$$

Discount back: €23.16 × 0.6830 = **€15.82**

**Total value = €4.19 + €15.82 = €20.01 per share**
"""
    )
    t1, t2, t3 = st.columns(3)
    t1.metric("PV of Stage 1 dividends", "€4.19")
    t2.metric("PV of terminal value", "€15.82")
    t3.metric("Fair value per share", "€20.01")

    st.info(
        "**Insight:** As with the DCF, the **terminal value dominates** (~79% of the €20.01). The two-stage "
        "model captures the high-growth phase explicitly, then reverts to a *sustainable* long-run rate — "
        "avoiding the error of assuming 12% growth lasts forever."
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise 1 — Gordon Growth Calculator")
    st.markdown("Value a stable dividend payer. Watch how sensitive the price is to the $K_e - g$ spread.")

    left, right = st.columns([0.35, 0.65])
    with left:
        d0 = st.number_input("Current dividend D₀ (€)", 0.01, 100.0, 2.00, 0.05)
        g = st.slider("Perpetual growth g (%)", 0.0, 8.0, 3.0, 0.25)
        ke = st.slider("Cost of equity Ke (%)", 2.0, 20.0, 9.0, 0.25)

    with right:
        if ke <= g:
            st.error("⚠️ **Ke must exceed g.** With Ke ≤ g the Gordon model gives an infinite value. Lower g or raise Ke.")
        else:
            d1 = d0 * (1 + g / 100)
            price = gordon_growth(d1, ke, g)
            spread = ke - g

            k1, k2, k3 = st.columns(3)
            k1.metric("D₁ (next dividend)", money(d1))
            k2.metric("Ke − g spread", f"{spread:.2f}%")
            k3.metric("Fair value / share", money(price))

            # sensitivity: value across a range of Ke
            ke_range = [round(ke - 2 + 0.5 * i, 2) for i in range(9) if (ke - 2 + 0.5 * i) > g]
            vals = [gordon_growth(d1, k, g) for k in ke_range]
            sens = pd.DataFrame({"Fair value (€)": vals}, index=[f"{k:.1f}%" for k in ke_range])
            st.markdown("##### 📉 Value vs. Cost of Equity (Ke)")
            st.line_chart(sens)
            st.caption(
                f"Notice the steep curve: as Ke approaches g ({g:.1f}%), the value rises sharply. The "
                "Gordon model is *extremely* sensitive when the spread is small."
            )

    st.markdown("---")
    st.subheader("✏️ Interactive Exercise 2 — Two-Stage DDM Engine")
    st.markdown("Model a high-growth phase that matures into stable perpetual growth.")

    l2, r2 = st.columns([0.35, 0.65])
    with l2:
        d0b = st.number_input("Current dividend D₀ (€)", 0.01, 100.0, 1.00, 0.05, key="d0b")
        high_g = st.slider("Stage-1 high growth (%)", 0.0, 30.0, 12.0, 0.5)
        high_years = st.slider("Stage-1 duration (years)", 1, 10, 4, 1)
        term_g = st.slider("Stage-2 perpetual growth (%)", 0.0, 6.0, 3.0, 0.25)
        keb = st.slider("Cost of equity Ke (%)", 2.0, 20.0, 10.0, 0.25, key="keb")

    with r2:
        if keb <= term_g:
            st.error("⚠️ **Ke must exceed the perpetual growth rate.** Lower Stage-2 growth or raise Ke.")
        else:
            res = two_stage_ddm(d0b, high_g, high_years, term_g, keb)

            k1, k2, k3 = st.columns(3)
            k1.metric("PV of Stage-1 dividends", money(res["sum_pv_divs"]))
            k2.metric("PV of terminal value", money(res["pv_terminal"]))
            k3.metric("Fair value / share", money(res["value"]))

            if res["tv_pct"] > 80:
                st.warning(
                    f"⚠️ Terminal value is **{res['tv_pct']:.0f}%** of the total — the valuation leans heavily "
                    "on the long-run assumption. Scrutinise Stage-2 growth and Ke."
                )
            else:
                st.success(
                    f"✅ Fair value **{money(res['value'])}** per share. Terminal value is "
                    f"{res['tv_pct']:.0f}% of the total."
                )

            sched = pd.DataFrame(
                {
                    "Year": list(range(1, high_years + 1)),
                    "Dividend": res["divs"],
                    "Discount factor": res["dfs"],
                    "PV of dividend": res["pvs"],
                }
            )
            sched_disp = sched.copy()
            sched_disp["Dividend"] = sched_disp["Dividend"].map(money)
            sched_disp["Discount factor"] = sched_disp["Discount factor"].map(lambda v: f"{v:.4f}")
            sched_disp["PV of dividend"] = sched_disp["PV of dividend"].map(money)
            st.markdown("##### 📄 Stage-1 dividend schedule")
            st.dataframe(sched_disp, use_container_width=True, hide_index=True)

            build = pd.DataFrame(
                {"€ per share": [res["sum_pv_divs"], res["pv_terminal"], res["value"]]},
                index=["PV Stage-1 divs", "PV terminal value", "Total value"],
            )
            st.bar_chart(build)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Danger zone:** In Gordon Growth, set g = 8% and Ke = 9%. Watch the value explode as the spread shrinks.
2. **Growth phase:** In the two-stage model, extend Stage-1 to 10 years at 15%. How much does value rise?
"""
        )
    with e2:
        st.markdown(
            """
3. **Ke sensitivity:** Raise Ke from 10% → 12% in either model. See how much value falls.
4. **Terminal dominance:** Lower Stage-1 growth to 3% (= terminal). The two-stage model should collapse
   toward the simple Gordon result.
"""
        )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Valuing a utility (perfect DDM candidate)", expanded=True):
        st.markdown(
            """
**Situation:** An investor wants to value a regulated utility with stable, predictable dividends growing
~2–3% a year.

**Why the DDM fits:** Utilities have steady cash flows and pay out most earnings as dividends. The Gordon
Growth model captures this almost perfectly — value ≈ next dividend ÷ (Ke − g).

**Why it matters:** For such businesses, the DDM is often more direct and reliable than a full DCF.

**Lesson:** The DDM shines for mature, stable, high-payout businesses — utilities, staples, mature banks.
"""
        )

    with st.expander("Case B — When the DDM breaks (a no-dividend growth company)"):
        st.markdown(
            """
**Situation:** An analyst tried to value a fast-growing tech company using the DDM.

**What went wrong:** The company pays **no dividends** — it reinvests everything. The DDM produced a value
of essentially zero, which is obviously wrong.

**The fix:** Switch to a **DCF** (which values *cash generation*, not distributions) or Comps.

**Lesson:** The DDM only works for companies that actually pay (or will predictably pay) dividends. No
dividends → use another method.
"""
        )

    with st.expander("Case C — The two-stage model for a maturing business"):
        st.markdown(
            """
**Situation:** A company was growing dividends 12% a year, but that pace clearly couldn't last forever.

**How the two-stage DDM helped:** It modelled the 12% phase explicitly for several years, then reverted
to a sustainable 3% perpetual rate. A single-stage Gordon model assuming 12% forever would have produced
a wildly inflated (and impossible) value.

**Why it matters:** Assuming high growth is permanent is one of the most common — and most dangerous —
valuation errors.

**Lesson:** When growth will clearly change, use a multi-stage model and revert to a sustainable long-run rate.
"""
        )

    st.info(
        "🔗 **Pattern:** The DDM is elegant and direct for dividend payers, but fragile where dividends are "
        "absent or growth is unstable. Match the model to the company — and always sanity-check g against "
        "what's sustainable."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_34"):
        q1 = st.radio(
            "**1.** The Dividend Discount Model values a share as:",
            [
                "The present value of the company's free cash flow to the firm",
                "The present value of all future dividends the share will pay",
                "The book value of equity per share",
                "Revenue per share × a multiple",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** The Gordon Growth formula is:",
            [
                "P₀ = D₁ × (Ke − g)",
                "P₀ = D₁ / (Ke − g)",
                "P₀ = D₀ / (Ke + g)",
                "P₀ = Ke / (D₁ − g)",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** The discount rate used in a DDM is the:",
            [
                "WACC",
                "Cost of equity (Ke)",
                "Risk-free rate only",
                "Corporate tax rate",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** The Gordon Growth model requires that:",
            [
                "g is greater than Ke",
                "Ke is greater than g",
                "Ke equals g",
                "the company has net debt",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** For which company is the DDM LEAST appropriate?",
            [
                "A mature utility paying steady dividends",
                "A regulated bank with a stable payout",
                "A fast-growing tech firm that pays no dividends",
                "A consumer-staples company with a long dividend history",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "The present value of all future dividends the share will pay"),
            "2": (q2, "P₀ = D₁ / (Ke − g)"),
            "3": (q3, "Cost of equity (Ke)"),
            "4": (q4, "Ke is greater than g"),
            "5": (q5, "A fast-growing tech firm that pays no dividends"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered the DDM! On to Module 3.5 (Sum-of-the-Parts). 🎉")
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
    f"Applied Financial Models · Module 3.4 Dividend Discount Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
