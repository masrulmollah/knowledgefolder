"""
================================================================================
APPLIED FINANCIAL MODELS
Module 6.1 — LBO (LEVERAGED BUYOUT) MODEL
================================================================================

A single-page, interactive Streamlit module that teaches finance professionals
how a leveraged buyout creates equity returns: entry (sources & uses), debt
paydown from cash flow, exit valuation, and the resulting IRR and MOIC.

The page follows the standard 5-tab structure used across the site:
    1. Theory & Concepts
    2. Worked Examples
    3. Interactive Exercises   (a live LBO returns engine)
    4. Real-Life Practical Cases
    5. Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Module_6_1_LBO_Model.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="6.1 LBO Model — Applied Financial Models",
    layout="wide",
    page_icon="🚀",
)

# --------------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------------
def money(x, symbol="€", dp=0):
    sign = "-" if x < 0 else ""
    return f"{sign}{symbol}{abs(x):,.{dp}f}"


def run_lbo(entry_ebitda, entry_multiple, debt_pct, ebitda_growth,
            cash_sweep_pct, interest_rate, exit_multiple, hold_years):
    """
    Run a simple LBO model.
    Returns a per-year schedule DataFrame plus summary (entry equity, exit equity,
    MOIC, IRR).
    """
    entry_ev = entry_ebitda * entry_multiple
    entry_debt = entry_ev * debt_pct / 100
    entry_equity = entry_ev - entry_debt

    rows = []
    ebitda = entry_ebitda
    debt = entry_debt
    for y in range(1, hold_years + 1):
        ebitda = ebitda * (1 + ebitda_growth / 100)
        interest = debt * interest_rate / 100
        # cash available to repay debt = (EBITDA - interest) * sweep %
        cash_for_debt = max(ebitda - interest, 0) * cash_sweep_pct / 100
        repay = min(cash_for_debt, debt)
        debt_end = debt - repay
        rows.append({
            "Year": y, "EBITDA": ebitda, "Interest": interest,
            "Debt repaid": repay, "Debt (end)": debt_end,
        })
        debt = debt_end

    exit_ebitda = ebitda
    exit_ev = exit_ebitda * exit_multiple
    exit_debt = debt
    exit_equity = exit_ev - exit_debt

    moic = exit_equity / entry_equity if entry_equity > 0 else 0
    irr = (moic ** (1 / hold_years) - 1) * 100 if (entry_equity > 0 and moic > 0) else None

    schedule = pd.DataFrame(rows)
    summary = {
        "entry_ev": entry_ev, "entry_debt": entry_debt, "entry_equity": entry_equity,
        "exit_ebitda": exit_ebitda, "exit_ev": exit_ev, "exit_debt": exit_debt,
        "exit_equity": exit_equity, "moic": moic, "irr": irr,
    }
    return schedule, summary


# --------------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Module Control Panel")
st.sidebar.caption("Part 6 · Specialised & Advanced Models")
st.sidebar.markdown(
    """
**Module 6.1 — LBO (Leveraged Buyout) Model**

🔴 *Advanced*

**You will learn to:**
- Structure an LBO's sources & uses
- Model debt paydown from cash flow
- Value the exit and compute returns
- Understand IRR, MOIC & the role of leverage
"""
)
st.sidebar.markdown("---")
st.sidebar.info(
    "💡 Head to the **Interactive Exercises** tab to run a live LBO — set the "
    "leverage and exit, and see the equity IRR and MOIC."
)
st.sidebar.markdown("---")
st.sidebar.caption("Applied Financial Models · Understand → Build → Interpret → Decide")

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("🚀 6.1 · LBO (Leveraged Buyout) Model")
st.markdown(
    """
A **leveraged buyout (LBO)** is the acquisition of a company using a large amount of **borrowed money
(debt)**, with a relatively small slice of **equity** from the investor (typically a private-equity firm).
The company's own cash flows then repay the debt over time.

The magic — and the risk — is **leverage**: because equity is a small part of the purchase, even a modest
rise in the company's value can produce a very large **return on equity**. This flagship Part 6 module
builds an LBO from entry to exit and shows exactly how the equity return is created.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Module", "6.1")
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
### What is an LBO?
In an LBO, an investor buys a company mostly with **debt** (often 50–70% of the price), contributing only
a small **equity** cheque. The acquired company's **cash flows service and repay the debt**. After a few
years, the investor sells ('exits') — and because the debt has been paid down, most of the sale proceeds
go to equity.
"""
    )

    st.markdown("### The three sources of LBO equity returns")
    sources = pd.DataFrame(
        {
            "Value driver": ["1. Debt paydown", "2. EBITDA growth", "3. Multiple expansion"],
            "How it creates equity value": [
                "Company cash flow repays debt → equity's share of enterprise value grows",
                "Growing EBITDA raises enterprise value at any given multiple",
                "Selling at a higher multiple than the purchase multiple",
            ],
            "Who controls it": [
                "Cash generation & discipline", "Operational improvement", "Market timing / value creation",
            ],
        }
    )
    st.table(sources)

    with st.expander("🔑 Concept 1 — Sources & uses (the entry)"):
        st.markdown(
            """
Every LBO starts with a **sources & uses** table:
- **Uses:** what you're buying — the enterprise value (Entry EBITDA × entry multiple), plus fees.
- **Sources:** how you pay — **debt** (the bulk) + **equity** (the investor's cheque).

$$\\text{Equity} = \\text{Enterprise Value} - \\text{Debt}$$

The higher the debt %, the smaller the equity cheque — and the greater the potential return (and risk).
"""
        )

    with st.expander("🔑 Concept 2 — Debt paydown from cash flow"):
        st.markdown(
            """
The acquired company's operating cash flow (roughly EBITDA − interest − tax − capex) is used to **repay
debt**, often via a **cash sweep** (a set % of surplus cash goes to debt each year). As debt falls:
- Interest costs fall (freeing more cash).
- **Equity's share of enterprise value rises** — even if the company's value doesn't change at all.

Debt paydown alone can create substantial equity returns.
"""
        )

    with st.expander("🔑 Concept 3 — The exit & returns (IRR and MOIC)"):
        st.markdown(
            """
At exit (typically 3–7 years), the company is sold at an **exit multiple** × exit EBITDA. Equity proceeds
= exit enterprise value − remaining debt. Two return metrics:

- **MOIC (Multiple of Invested Capital)** = Exit equity ÷ Entry equity (e.g. 2.5× your money back).
- **IRR (Internal Rate of Return)** = the annualised return: $IRR = MOIC^{1/n} - 1$.

A 2.5× MOIC over 5 years ≈ a **20% IRR** — a typical private-equity target.
"""
        )

    with st.expander("🔑 Concept 4 — Why leverage magnifies returns (and risk)"):
        st.markdown(
            """
Leverage is a double-edged sword:
- **Upside:** with only a small equity slice, a given increase in enterprise value produces a *much* larger
  % return on that equity.
- **Downside:** debt must be serviced regardless of performance. If cash flow disappoints, interest can
  overwhelm the company — the same leverage that magnifies gains magnifies losses, and can lead to distress.

This is why LBOs target **stable, cash-generative** businesses that can safely carry debt.
"""
        )

    with st.expander("🔑 Concept 5 — What makes a good LBO candidate"):
        st.markdown(
            """
Ideal LBO targets have:
- **Strong, predictable cash flows** (to service debt reliably).
- **Low existing debt** and modest capex needs.
- **Operational improvement potential** (cost cuts, growth).
- A **credible exit** (buyers or an IPO in a few years).

Volatile, capital-hungry, or highly cyclical businesses make risky LBOs.
"""
        )

    st.success(
        "**Takeaway:** An LBO buys a company mostly with debt, uses its cash flow to repay that debt, then "
        "sells at exit. Equity returns come from debt paydown, EBITDA growth and multiple expansion — "
        "magnified by leverage, which raises both the reward and the risk."
    )

# ================================================================================
# TAB 2 — WORKED EXAMPLES
# ================================================================================
with tabs[1]:
    st.subheader("Worked Example — A simple LBO from entry to exit")
    st.markdown("A private-equity firm buys a business generating **€10m EBITDA**.")

    st.markdown("#### Step 1 — Entry (sources & uses)")
    st.markdown(
        """
| Item | Value |
|---|---|
| Entry EBITDA | €10m |
| Entry multiple | 8.0× |
| **Enterprise value (purchase price)** | **€80m** |
| Debt (60%) | €48m |
| **Equity cheque (40%)** | **€32m** |
"""
    )

    st.markdown("#### Step 2 — Hold period (5 years)")
    st.markdown(
        """
- EBITDA grows ~5%/year → **€12.8m** by Year 5.
- Cash flow sweeps down the debt from €48m to about **€20m** over the 5 years.
"""
    )

    st.markdown("#### Step 3 — Exit (Year 5)")
    st.markdown(
        """
| Item | Value |
|---|---|
| Exit EBITDA | €12.8m |
| Exit multiple | 8.5× |
| **Exit enterprise value** | **€108.8m** |
| Less: remaining debt | (€20m) |
| **Exit equity value** | **€88.8m** |
"""
    )

    st.markdown("#### Step 4 — Returns")
    st.markdown(
        """
$$\\text{MOIC} = \\frac{€88.8m}{€32m} = \\mathbf{2.78\\times}$$
$$\\text{IRR} = 2.78^{1/5} - 1 = \\mathbf{\\approx 22.7\\%}$$
"""
    )

    e1, e2, e3 = st.columns(3)
    e1.metric("Entry equity", "€32m")
    e2.metric("Exit equity", "€88.8m")
    e3.metric("Return", "2.78× / ~22.7% IRR")

    st.info(
        "**Insight:** The €32m equity nearly **triples to €88.8m** in five years. Notice all three value "
        "drivers at work: **debt paydown** (€48m → €20m shifts value to equity), **EBITDA growth** "
        "(€10m → €12.8m), and modest **multiple expansion** (8.0× → 8.5×). Debt paydown alone — with no "
        "growth or multiple change — would still have delivered a strong return. **That's the power of leverage.**"
    )

# ================================================================================
# TAB 3 — INTERACTIVE EXERCISES
# ================================================================================
with tabs[2]:
    st.subheader("✏️ Interactive Exercise — Live LBO Returns Engine")
    st.markdown(
        "Set the entry, leverage, cash sweep and exit assumptions. The model repays debt from cash flow and "
        "computes the equity **MOIC** and **IRR**."
    )

    left, right = st.columns([0.34, 0.66])

    with left:
        st.markdown("##### 🛒 Entry")
        entry_ebitda = st.number_input("Entry EBITDA (€m)", 1.0, 5000.0, 10.0, 0.5)
        entry_multiple = st.number_input("Entry multiple (×)", 1.0, 30.0, 8.0, 0.5)
        debt_pct = st.slider("Debt % of purchase price", 0, 90, 60, 5)

        st.markdown("##### 📈 Hold period")
        ebitda_growth = st.slider("EBITDA growth (%/yr)", -10.0, 25.0, 5.0, 0.5)
        interest_rate = st.slider("Interest rate on debt (%)", 0.0, 20.0, 7.0, 0.5)
        cash_sweep = st.slider("Cash sweep (% of surplus to debt)", 0, 100, 70, 5)
        hold_years = st.slider("Hold period (years)", 1, 10, 5, 1)

        st.markdown("##### 🚪 Exit")
        exit_multiple = st.number_input("Exit multiple (×)", 1.0, 30.0, 8.5, 0.5)

    with right:
        schedule, s = run_lbo(
            entry_ebitda, entry_multiple, debt_pct, ebitda_growth,
            cash_sweep, interest_rate, exit_multiple, hold_years,
        )

        k1, k2, k3 = st.columns(3)
        k1.metric("Entry equity", money(s["entry_equity"], dp=1) + "m")
        k2.metric("Exit equity", money(s["exit_equity"], dp=1) + "m")
        k3.metric("MOIC", f"{s['moic']:.2f}×",
                  "Money multiple", delta_color="normal" if s["moic"] >= 1 else "inverse")

        k4, k5, k6 = st.columns(3)
        k4.metric("Equity IRR", f"{s['irr']:.1f}%" if s["irr"] is not None else "n/a",
                  "Strong ✅" if (s["irr"] is not None and s["irr"] >= 20)
                  else "Weak" if (s["irr"] is not None and s["irr"] < 15) else None,
                  delta_color="normal" if (s["irr"] is not None and s["irr"] >= 15) else "inverse")
        k5.metric("Entry EV", money(s["entry_ev"], dp=1) + "m", f"{debt_pct}% debt")
        k6.metric("Exit EV", money(s["exit_ev"], dp=1) + "m")

        if s["irr"] is not None and s["irr"] >= 20:
            st.success(
                f"✅ **Attractive LBO:** ~{s['irr']:.0f}% IRR and {s['moic']:.2f}× MOIC — meets a typical "
                "private-equity target (≥20% IRR / ~2–3× MOIC)."
            )
        elif s["irr"] is not None and s["irr"] >= 15:
            st.info(
                f"🔎 **Marginal:** ~{s['irr']:.0f}% IRR ({s['moic']:.2f}× MOIC) — below the usual 20% PE "
                "target. More leverage, growth, or multiple expansion would be needed."
            )
        else:
            st.warning(
                f"⚠️ **Weak return:** ~{s['irr']:.0f}% IRR ({s['moic']:.2f}× MOIC). As configured this deal "
                "doesn't clear a private-equity hurdle."
            )

        st.markdown("##### 📄 Debt Paydown Schedule")
        disp = schedule.copy()
        for col in ["EBITDA", "Interest", "Debt repaid", "Debt (end)"]:
            disp[col] = disp[col].map(lambda v: money(v, dp=2) + "m")
        st.dataframe(disp, use_container_width=True, hide_index=True)

        st.markdown("##### 📉 Debt reduction over the hold period")
        debt_chart = pd.concat([
            pd.DataFrame({"Debt (€m)": [s["entry_debt"]]}, index=["Entry"]),
            schedule.set_index("Year")[["Debt (end)"]].rename(columns={"Debt (end)": "Debt (€m)"}),
        ])
        st.bar_chart(debt_chart)

    st.markdown("---")
    st.markdown("##### 🧪 Try these challenges")
    e1, e2 = st.columns(2)
    with e1:
        st.markdown(
            """
1. **Leverage effect:** Raise debt from 60% → 80%. Watch the equity cheque shrink and the IRR jump — but
   note the higher risk.
2. **No multiple expansion:** Set the exit multiple equal to the entry multiple. Is the return still good
   from debt paydown + growth alone?
"""
        )
    with e2:
        st.markdown(
            """
3. **Growth matters:** Push EBITDA growth to 12%. How much does exit equity rise?
4. **The danger of over-leverage:** Set debt to 90% and growth to −5%. Watch how thin cash flow and heavy
   interest crush the return.
"""
        )

    st.download_button(
        "⬇️ Download the LBO schedule (CSV)",
        schedule.to_csv(index=False).encode("utf-8"),
        "lbo_schedule.csv",
        "text/csv",
    )

# ================================================================================
# TAB 4 — REAL-LIFE PRACTICAL CASES
# ================================================================================
with tabs[3]:
    st.subheader("🏭 Real-Life Practical Cases")

    with st.expander("Case A — Debt paydown drives the return", expanded=True):
        st.markdown(
            """
**Situation:** A private-equity firm buys a stable, cash-generative business at 8× EBITDA with 60% debt.

**How the LBO creates value:** Even with **no growth and no multiple change**, the company's steady cash
flow pays down a large chunk of debt over five years. Because equity = enterprise value − debt, shrinking
the debt **transfers value to equity** — producing a solid IRR from deleveraging alone.

**Why it matters:** It shows the most reliable LBO value driver isn't heroic growth — it's disciplined
**debt paydown** from dependable cash flow.

**Lesson:** Stable cash generators make great LBOs because debt paydown is a near-certain source of return.
"""
        )

    with st.expander("Case B — Over-leverage and financial distress"):
        st.markdown(
            """
**Situation:** A buyer used very aggressive leverage (85%+) on a business whose earnings then dipped.

**What went wrong:** Interest payments consumed nearly all the cash flow; there was nothing left to repay
debt or absorb the downturn. The company breached covenants and slid toward distress.

**Why it matters:** The same leverage that magnifies returns magnifies losses. Too much debt leaves no
margin for error.

**Lesson:** Leverage must match the stability of the cash flows — over-leveraging a cyclical or fragile
business is dangerous.
"""
        )

    with st.expander("Case C — Multiple expansion (buy low, sell high)"):
        st.markdown(
            """
**Situation:** A firm bought a business at 7× EBITDA and, after improving it, sold it at 10× to a
strategic buyer.

**How the LBO creates value:** On top of debt paydown and growth, the **3-turn multiple expansion**
massively boosted the exit equity value — the investor benefited from both a bigger EBITDA *and* a higher
multiple applied to it.

**Why it matters:** Multiple expansion can be the largest single value driver — but it depends on market
conditions and genuinely improving the business, so it's the least certain to rely on.

**Lesson:** Multiple expansion is powerful but not guaranteed; prudent LBOs don't *assume* it in the base case.
"""
        )

    st.info(
        "🔗 **Pattern:** LBO returns come from debt paydown, EBITDA growth and multiple expansion — amplified "
        "by leverage. The safest deals lean on reliable cash flow and debt paydown; the riskiest bet on "
        "aggressive leverage and hoped-for multiple expansion."
    )

# ================================================================================
# TAB 5 — KNOWLEDGE TEST / QUIZ
# ================================================================================
with tabs[4]:
    st.subheader("✅ Knowledge Test")
    st.markdown("Answer the questions below and click **Submit** for instant scoring and feedback.")

    with st.form("quiz_61"):
        q1 = st.radio(
            "**1.** A leveraged buyout (LBO) acquires a company primarily using:",
            [
                "Only the investor's own cash (equity)",
                "A large amount of debt plus a small slice of equity",
                "Government grants",
                "Retained earnings only",
            ],
            index=None,
        )
        q2 = st.radio(
            "**2.** In an LBO, the acquired company's cash flow is mainly used to:",
            [
                "Pay dividends immediately",
                "Repay the acquisition debt",
                "Buy back shares",
                "Increase the purchase price",
            ],
            index=None,
        )
        q3 = st.radio(
            "**3.** Which is NOT one of the three main sources of LBO equity returns?",
            [
                "Debt paydown",
                "EBITDA growth",
                "Multiple expansion",
                "Issuing new equity to the public",
            ],
            index=None,
        )
        q4 = st.radio(
            "**4.** MOIC (Multiple of Invested Capital) is:",
            [
                "Exit equity value ÷ entry equity value",
                "Entry equity ÷ exit equity",
                "Debt ÷ equity",
                "EBITDA × multiple",
            ],
            index=None,
        )
        q5 = st.radio(
            "**5.** Why does higher leverage magnify BOTH returns and risk?",
            [
                "Because it removes all debt",
                "A small equity base means value changes translate into large % swings on equity, while debt must be serviced regardless of performance",
                "Because interest is tax-free",
                "Because it guarantees multiple expansion",
            ],
            index=None,
        )

        submitted = st.form_submit_button("Submit answers")

    if submitted:
        answers = {
            "1": (q1, "A large amount of debt plus a small slice of equity"),
            "2": (q2, "Repay the acquisition debt"),
            "3": (q3, "Issuing new equity to the public"),
            "4": (q4, "Exit equity value ÷ entry equity value"),
            "5": (q5, "A small equity base means value changes translate into large % swings on equity, while debt must be serviced regardless of performance"),
        }
        score = sum(1 for _, (given, correct) in answers.items() if given == correct)

        st.markdown(f"### Your score: **{score} / 5**")
        if score == 5:
            st.balloons()
            st.success("Excellent — you've mastered the LBO model! On to Module 6.2 (M&A / Accretion-Dilution). 🎉")
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
    f"Applied Financial Models · Module 6.1 LBO (Leveraged Buyout) Model · "
    f"Generated {datetime.now().strftime('%Y-%m-%d')} · "
    "Understand → Build → Interpret → Decide."
)
