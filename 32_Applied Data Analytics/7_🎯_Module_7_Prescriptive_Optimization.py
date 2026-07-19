import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from itertools import product

st.set_page_config(page_title="Module 7 — Prescriptive Optimization", page_icon="🎯", layout="wide")

st.title("🎯 Module 7: Prescriptive Analytics — Optimization & Decisions")
st.caption("Learning goal: answer 'what should we do?' using optimization and expected-value analysis.")

st.markdown(
    "Prescriptive analytics goes one step beyond prediction — it recommends the **best action** "
    "given your constraints. Two common finance tools: **budget allocation optimization** and "
    "**expected-value decision analysis**."
)

st.divider()

# ----------------------------------------------------------------------------
# BUDGET ALLOCATION OPTIMIZER (diminishing returns)
# ----------------------------------------------------------------------------
st.markdown("## 💰 Budget Allocation Optimizer")
st.markdown(
    "Each channel has **diminishing returns**: the first dollar spent returns more than the "
    "thousandth. Set the total budget and each channel's efficiency, and we'll search for the "
    "split that maximizes total return."
)

total_budget = st.slider("Total marketing budget ($'000)", 100, 5000, 1000, step=50)

st.markdown("**Channel efficiency (higher = more return per dollar before diminishing returns kick in):**")
c1, c2, c3 = st.columns(3)
eff_digital = c1.slider("Digital Ads efficiency", 0.5, 3.0, 2.0, step=0.1)
eff_tv = c2.slider("TV/Radio efficiency", 0.5, 3.0, 1.2, step=0.1)
eff_events = c3.slider("Events/Sponsorship efficiency", 0.5, 3.0, 1.5, step=0.1)

def channel_return(spend, efficiency):
    # diminishing returns via square-root response curve
    return efficiency * np.sqrt(spend) * 10

# grid search over allocation splits (simple, transparent approach for teaching purposes)
step = max(total_budget // 40, 1)
best_alloc, best_return = None, -1
grid = np.arange(0, total_budget + step, step)
for d in grid:
    for t in grid:
        e = total_budget - d - t
        if e < 0:
            continue
        r = channel_return(d, eff_digital) + channel_return(t, eff_tv) + channel_return(e, eff_events)
        if r > best_return:
            best_return = r
            best_alloc = (d, t, e)

# compare to an equal-split baseline
equal = total_budget / 3
equal_return = (channel_return(equal, eff_digital) + channel_return(equal, eff_tv) + channel_return(equal, eff_events))

colA, colB = st.columns(2)
with colA:
    st.markdown("### 🔻 Equal-Split Allocation (naive baseline)")
    st.write(pd.DataFrame({
        "Channel": ["Digital", "TV/Radio", "Events"],
        "Spend ($'000)": [equal, equal, equal],
    }).style.format({"Spend ($'000)": "{:.0f}"}))
    st.metric("Total Return (index)", f"{equal_return:,.0f}")

with colB:
    st.markdown("### ✅ Optimized Allocation")
    st.write(pd.DataFrame({
        "Channel": ["Digital", "TV/Radio", "Events"],
        "Spend ($'000)": list(best_alloc),
    }).style.format({"Spend ($'000)": "{:.0f}"}))
    st.metric("Total Return (index)", f"{best_return:,.0f}",
              delta=f"+{best_return - equal_return:,.0f} vs equal split")

fig = go.Figure(data=[
    go.Bar(name="Equal Split", x=["Digital", "TV/Radio", "Events"], y=[equal, equal, equal]),
    go.Bar(name="Optimized", x=["Digital", "TV/Radio", "Events"], y=list(best_alloc)),
])
fig.update_layout(barmode="group", title="Allocation Comparison", height=400)
st.plotly_chart(fig, use_container_width=True)

st.success(
    f"The optimizer shifts more budget toward **higher-efficiency channels**, but not all of it — "
    "because diminishing returns mean spreading spend across channels still beats piling everything into one."
)

st.divider()

# ----------------------------------------------------------------------------
# EXPECTED VALUE DECISION CALCULATOR
# ----------------------------------------------------------------------------
st.markdown("## 🌳 Expected Value Decision Calculator")
st.markdown(
    "Compare two strategic options under uncertainty. For each, define possible scenarios, "
    "their probability, and payoff — the tool computes the expected value of each option."
)

def scenario_editor(label, defaults):
    st.markdown(f"**{label}**")
    rows = []
    for i, (name, prob, payoff) in enumerate(defaults):
        c1, c2, c3 = st.columns([2, 1, 1])
        n = c1.text_input(f"Scenario name", value=name, key=f"{label}_name_{i}")
        p = c2.number_input("Probability", 0.0, 1.0, prob, step=0.05, key=f"{label}_prob_{i}")
        v = c3.number_input("Payoff ($'000)", value=payoff, step=50, key=f"{label}_val_{i}")
        rows.append((n, p, v))
    return rows

colX, colY = st.columns(2)
with colX:
    rows_a = scenario_editor("Option A: Launch New Product", [
        ("Strong demand", 0.3, 4000),
        ("Moderate demand", 0.5, 1200),
        ("Weak demand", 0.2, -1500),
    ])
with colY:
    rows_b = scenario_editor("Option B: Expand Existing Line", [
        ("Strong demand", 0.4, 2200),
        ("Moderate demand", 0.4, 900),
        ("Weak demand", 0.2, -200),
    ])

ev_a = sum(p * v for _, p, v in rows_a)
ev_b = sum(p * v for _, p, v in rows_b)
prob_sum_a = sum(p for _, p, v in rows_a)
prob_sum_b = sum(p for _, p, v in rows_b)

st.divider()
m1, m2 = st.columns(2)
m1.metric("Option A — Expected Value", f"${ev_a:,.0f}k",
          help="Sum of (probability × payoff) across scenarios")
m2.metric("Option B — Expected Value", f"${ev_b:,.0f}k")

if abs(prob_sum_a - 1) > 0.01 or abs(prob_sum_b - 1) > 0.01:
    st.warning("⚠️ Probabilities for one or both options don't sum to 1.0 — adjust them for a valid expected value.")

if ev_a > ev_b:
    st.success(f"**Recommendation: Option A** has the higher expected value (${ev_a:,.0f}k vs ${ev_b:,.0f}k). "
               "But also consider Option A's downside risk — check the worst-case scenario, not just the average.")
elif ev_b > ev_a:
    st.success(f"**Recommendation: Option B** has the higher expected value (${ev_b:,.0f}k vs ${ev_a:,.0f}k). "
               "Also weigh strategic factors expected value doesn't capture (e.g. brand risk, competitive response).")
else:
    st.info("Both options currently have equal expected value — the tie-breaker should be risk tolerance or strategic fit.")

st.divider()
st.info("➡️ Next: **Module 8 — Data Visualization & Dashboards**, to communicate these findings effectively.")
