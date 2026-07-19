import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Module 9 — Capstone Project", page_icon="🏆", layout="wide")

st.title("🏆 Module 9: Capstone Project — End-to-End Case Study")
st.caption("Learning goal: apply the full process, on one integrated case, from question to recommendation.")

st.markdown(
    """
### 📂 The Case: Meridian Distributors Inc.

You are the finance manager at Meridian, a mid-size B2B distributor. **Gross margin has fallen
from 41% to 36% over the last two quarters**, and the CFO wants your recommendation before
next week's board meeting. Work through the tabs below in order — each mirrors a step from
Module 2's process, using the techniques from Modules 3–7.
"""
)

tabs = st.tabs([
    "1️⃣ Define & Classify",
    "2️⃣ Explore the Data",
    "3️⃣ Diagnose the Cause",
    "4️⃣ Forecast Forward",
    "5️⃣ Decide & Recommend",
    "6️⃣ Summary Report",
])

# ----------------------------------------------------------------------------
# TAB 1 — DEFINE & CLASSIFY
# ----------------------------------------------------------------------------
with tabs[0]:
    st.markdown("### Step 1 — Define the objective & classify the analytics type")
    st.markdown(
        "**Objective:** *Why did gross margin fall from 41% to 36%, is it likely to persist, "
        "and what should Meridian do about it?*"
    )
    q1 = st.multiselect(
        "Which types of analytics will this question require? (select all that apply)",
        ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
    )
    if q1:
        correct = {"Descriptive", "Diagnostic", "Predictive", "Prescriptive"}
        if set(q1) == correct:
            st.success("Correct — this realistic question actually needs **all four**: confirm the "
                       "drop (Descriptive), find the cause (Diagnostic), see if it persists (Predictive), "
                       "and decide what to do (Prescriptive).")
        else:
            st.info("Keep thinking — a full board-level answer to this question typically draws on "
                    "more than one type of analytics. Try selecting all four.")

# ----------------------------------------------------------------------------
# TAB 2 — EXPLORE
# ----------------------------------------------------------------------------
with tabs[1]:
    st.markdown("### Step 2 — Explore: margin by product line")
    st.markdown("Here is quarterly gross margin by product line. Adjust nothing — just explore and identify the outlier.")

    product_lines = ["Industrial Parts", "Electrical Supplies", "Safety Equipment", "Tools"]
    q_labels = ["Q1", "Q2", "Q3", "Q4"]
    margins = np.array([
        [42, 41, 40, 39],   # Industrial Parts
        [40, 41, 40, 41],   # Electrical Supplies
        [43, 42, 22, 15],   # Safety Equipment -- collapsed
        [41, 40, 41, 40],   # Tools
    ])
    df_margin = pd.DataFrame(margins, index=product_lines, columns=q_labels)
    st.dataframe(df_margin.style.format("{:.0f}%").background_gradient(cmap="RdYlGn", axis=None, vmin=10, vmax=45),
                 use_container_width=True)

    fig = go.Figure()
    for i, pl in enumerate(product_lines):
        fig.add_trace(go.Scatter(x=q_labels, y=margins[i], mode="lines+markers", name=pl))
    fig.update_layout(title="Gross Margin % by Product Line", height=420, yaxis_title="Gross Margin (%)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("**Which product line is driving the overall margin collapse?**")
    guess = st.radio("Select:", product_lines, key="guess_line")
    if guess == "Safety Equipment":
        st.success("Correct! Safety Equipment collapsed from 43% to 15% — every other line is stable. "
                   "This tells us the issue is **specific and structural**, not a company-wide pricing problem.")
    else:
        st.error("Look again at the table — one line drops sharply in Q3-Q4 while the others stay flat.")

# ----------------------------------------------------------------------------
# TAB 3 — DIAGNOSE
# ----------------------------------------------------------------------------
with tabs[2]:
    st.markdown("### Step 3 — Diagnose: what happened to Safety Equipment?")
    st.markdown(
        "Investigation reveals a key supplier raised input costs by 18% in Q3, but Meridian's "
        "sales team did not adjust customer pricing. Use the sliders to test the variance bridge."
    )
    supplier_increase = st.slider("Supplier cost increase (%)", 0, 40, 18)
    price_passthrough = st.slider("% of cost increase passed on to customers so far", 0, 100, 0)

    base_cost = 100
    base_price = 175  # gives ~43% margin at baseline
    new_cost = base_cost * (1 + supplier_increase / 100)
    new_price = base_price * (1 + (supplier_increase / 100) * (price_passthrough / 100))
    new_margin = (new_price - new_cost) / new_price * 100
    old_margin = (base_price - base_cost) / base_price * 100

    c1, c2 = st.columns(2)
    c1.metric("Margin before cost increase", f"{old_margin:.1f}%")
    c2.metric("Margin after cost increase & pass-through", f"{new_margin:.1f}%",
              delta=f"{new_margin - old_margin:.1f}pp")

    if price_passthrough < 50:
        st.warning(
            "With low pass-through, margin stays badly compressed. This confirms the root cause: "
            "**an unpassed supplier cost increase**, not a demand or volume problem — a Diagnostic finding."
        )
    else:
        st.success("Raising pass-through recovers much of the lost margin — useful evidence for Step 5's recommendation.")

# ----------------------------------------------------------------------------
# TAB 4 — FORECAST
# ----------------------------------------------------------------------------
with tabs[3]:
    st.markdown("### Step 4 — Forecast: will this persist into next quarter?")
    st.markdown("Assuming no pricing action is taken, project Safety Equipment margin forward using a simple trend.")

    hist_margin = [43, 42, 22, 15]
    x = np.arange(len(hist_margin))
    coeffs = np.polyfit(x, hist_margin, 1)
    future_x = np.arange(len(hist_margin), len(hist_margin) + 2)
    forecast_margin = np.polyval(coeffs, future_x)
    forecast_margin = np.clip(forecast_margin, 0, 100)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=["Q1", "Q2", "Q3", "Q4"], y=hist_margin, mode="lines+markers", name="Actual"))
    fig2.add_trace(go.Scatter(x=["Q5 (fcst)", "Q6 (fcst)"], y=forecast_margin, mode="lines+markers",
                               name="Forecast (no action)", line=dict(dash="dot", color="red")))
    fig2.update_layout(title="Safety Equipment Margin Forecast if No Action Taken", height=400)
    st.plotly_chart(fig2, use_container_width=True)

    st.error(
        f"Without action, the trend suggests margin could fall to roughly **{forecast_margin[0]:.0f}%** next "
        "quarter — reinforcing that this is urgent and won't self-correct."
    )

# ----------------------------------------------------------------------------
# TAB 5 — DECIDE
# ----------------------------------------------------------------------------
with tabs[4]:
    st.markdown("### Step 5 — Decide: compare two options with expected value")
    st.markdown("Two options are on the table. Adjust probabilities/payoffs if you disagree with the estimates.")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Option A: Reprice Safety Equipment (+15%)**")
        p_a_success = st.slider("Probability customers accept price increase", 0.0, 1.0, 0.7, key="pa")
        payoff_a_success = st.number_input("Payoff if accepted ($'000 margin recovered/yr)", value=900, key="pas")
        payoff_a_fail = st.number_input("Payoff if customers churn instead ($'000, negative)", value=-300, key="paf")
        ev_a = p_a_success * payoff_a_success + (1 - p_a_success) * payoff_a_fail
        st.metric("Expected Value — Option A", f"${ev_a:,.0f}k")
    with c2:
        st.markdown("**Option B: Renegotiate with Supplier**")
        p_b_success = st.slider("Probability supplier grants partial relief", 0.0, 1.0, 0.4, key="pb")
        payoff_b_success = st.number_input("Payoff if relief granted ($'000/yr)", value=500, key="pbs")
        payoff_b_fail = st.number_input("Payoff if no relief ($'000/yr)", value=0, key="pbf")
        ev_b = p_b_success * payoff_b_success + (1 - p_b_success) * payoff_b_fail
        st.metric("Expected Value — Option B", f"${ev_b:,.0f}k")

    if ev_a > ev_b:
        st.success(f"**Recommendation: Option A** (reprice) has the higher expected value: ${ev_a:,.0f}k vs ${ev_b:,.0f}k.")
    else:
        st.success(f"**Recommendation: Option B** (renegotiate) has the higher expected value: ${ev_b:,.0f}k vs ${ev_a:,.0f}k.")
    st.caption("Combining both options (reprice AND renegotiate) is often the real-world answer — expected value "
               "analysis just tells you where the bigger lever is.")

# ----------------------------------------------------------------------------
# TAB 6 — SUMMARY REPORT
# ----------------------------------------------------------------------------
with tabs[5]:
    st.markdown("### Step 6 — Generate a one-page management summary")
    if st.button("📝 Generate Summary Report"):
        recommended = "Reprice Safety Equipment" if ev_a > ev_b else "Renegotiate with Supplier"
        report = f"""
**MERIDIAN DISTRIBUTORS — GROSS MARGIN REVIEW**

**Finding (Descriptive):** Company gross margin fell from 41% to 36% over two quarters.

**Root Cause (Diagnostic):** The decline is isolated to Safety Equipment, where margin
collapsed from 43% to 15% after an 18% supplier cost increase was not passed through to customers.
All other product lines remain stable.

**Outlook (Predictive):** Without intervention, Safety Equipment margin is projected to fall
further next quarter, continuing to drag down company-wide profitability.

**Recommendation (Prescriptive):** {recommended}, based on expected-value analysis of the
available options (Option A EV = ${ev_a:,.0f}k/yr, Option B EV = ${ev_b:,.0f}k/yr).

**Next step:** Implement the recommended action and monitor Safety Equipment margin monthly
to confirm recovery (Step 9 — Monitor).
"""
        st.markdown(report)
        st.success("This is exactly the structure — Finding → Cause → Outlook → Recommendation → Monitor — "
                   "you should use for any real analytics deliverable to a CFO or board.")

st.divider()
st.balloons()
st.markdown(
    """
## 🎓 Congratulations!
You've completed the **Applied Data Analytics** curriculum — from recognizing the type of
analytics a question needs, through the full process, to descriptive, diagnostic, predictive
and prescriptive techniques, ending with a real management recommendation.

Go back to the **Overview** page any time to revisit a module or check off your progress.
"""
)
