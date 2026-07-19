import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Module 6 — Risk & Simulation", page_icon="🎲", layout="wide")

st.title("🎲 Module 6: Predictive Analytics — Risk & Monte Carlo Simulation")
st.caption("Learning goal: quantify uncertainty in financial projections using simulation.")

st.markdown(
    """
Point forecasts (a single number) hide risk. **Monte Carlo simulation** runs a projection
thousands of times with randomly sampled assumptions, giving you a full *distribution* of
possible outcomes — essential for investment and cash-flow decisions.
"""
)

st.divider()
st.markdown("## 🎛️ Project Assumptions — NPV Simulation")

c1, c2, c3 = st.columns(3)
with c1:
    initial_investment = st.number_input("Initial Investment ($'000)", value=5000, step=100)
    years = st.slider("Project life (years)", 1, 10, 5)
with c2:
    cf_mean = st.number_input("Expected annual cash flow ($'000)", value=1400, step=50)
    cf_std = st.slider("Cash flow volatility (std dev, $'000)", 0, 1000, 250, step=25)
with c3:
    growth_mean = st.slider("Expected annual cash-flow growth (%)", -10.0, 20.0, 3.0, step=0.5)
    discount_rate = st.slider("Discount rate (%)", 1.0, 20.0, 10.0, step=0.5)

n_sims = st.select_slider("Number of simulations", options=[500, 1000, 5000, 10000], value=5000)

st.divider()

# ----------------------------------------------------------------------------
# MONTE CARLO SIMULATION
# ----------------------------------------------------------------------------
np.random.seed(7)
npvs = np.zeros(n_sims)

for s in range(n_sims):
    cf0 = np.random.normal(cf_mean, cf_std)
    growth_draw = np.random.normal(growth_mean, 3.0)  # uncertainty around growth rate itself
    npv = -initial_investment
    cf = cf0
    for y in range(1, years + 1):
        npv += cf / (1 + discount_rate / 100) ** y
        cf *= (1 + growth_draw / 100)
    npvs[s] = npv

results_df = pd.DataFrame({"NPV ($'000)": npvs})

fig = px.histogram(results_df, x="NPV ($'000)", nbins=60, title="Distribution of Simulated NPV Outcomes")
fig.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Break-even (NPV = 0)")
fig.add_vline(x=np.mean(npvs), line_dash="dot", line_color="green", annotation_text="Mean NPV")
fig.update_layout(height=450)
st.plotly_chart(fig, use_container_width=True)

st.markdown("## 📊 Risk Summary")
prob_negative = (npvs < 0).mean() * 100
p10, p50, p90 = np.percentile(npvs, [10, 50, 90])

k1, k2, k3, k4 = st.columns(4)
k1.metric("Mean NPV", f"${np.mean(npvs):,.0f}k")
k2.metric("Probability of Loss (NPV<0)", f"{prob_negative:.1f}%")
k3.metric("10th Percentile (pessimistic)", f"${p10:,.0f}k")
k4.metric("90th Percentile (optimistic)", f"${p90:,.0f}k")

if prob_negative > 40:
    st.error(
        f"**High risk**: there's a {prob_negative:.0f}% chance this project destroys value. "
        "Consider renegotiating terms, reducing initial investment, or requiring a higher expected cash flow before proceeding."
    )
elif prob_negative > 15:
    st.warning(
        f"**Moderate risk**: a {prob_negative:.0f}% chance of a negative NPV. Worth stress-testing "
        "key assumptions (cash-flow volatility, discount rate) before committing."
    )
else:
    st.success(
        f"**Lower risk**: only a {prob_negative:.0f}% chance of a negative NPV under these assumptions. "
        "Still worth checking sensitivity to the discount rate."
    )

st.markdown(
    """
**Why this matters for a finance manager:** a single-point NPV forecast (e.g. "NPV = +$1.2M") can
hide a coin-flip's chance of loss. Simulation turns "is this a good project?" into
"here is the range of outcomes and how likely each is" — a much stronger basis for a decision,
and a natural bridge into **Module 7 (Prescriptive Analytics)**.
"""
)

st.divider()
st.info("➡️ Next: **Module 7 — Prescriptive Analytics: Optimization & Decisions**.")
