import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Module 3 — Descriptive Analytics", page_icon="📊", layout="wide")

st.title("📊 Module 3: Descriptive Analytics — Ratios & Trend Analysis")
st.caption("Learning goal: answer 'what happened?' using financial ratios, KPIs, and trend charts.")

st.markdown(
    "Descriptive analytics summarizes historical performance. Adjust the inputs below "
    "(one year of financials) and watch the ratios, KPI cards and 3-year trend update instantly."
)

st.divider()
st.markdown("## 🎛️ Inputs — Current Year Financials ($ '000)")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**Income Statement**")
    revenue = st.slider("Revenue", 1000, 50000, 20000, step=500)
    cogs = st.slider("Cost of Goods Sold (COGS)", 500, 40000, 12000, step=500)
    opex = st.slider("Operating Expenses", 500, 20000, 5000, step=250)
with c2:
    st.markdown("**Balance Sheet**")
    current_assets = st.slider("Current Assets", 500, 30000, 9000, step=250)
    inventory = st.slider("Inventory (part of current assets)", 0, 15000, 3000, step=250)
    current_liabilities = st.slider("Current Liabilities", 500, 20000, 6000, step=250)
with c3:
    st.markdown("**Capital Structure**")
    total_debt = st.slider("Total Debt", 0, 30000, 8000, step=250)
    total_equity = st.slider("Total Equity", 500, 30000, 12000, step=250)
    total_assets = st.slider("Total Assets", 1000, 60000, 25000, step=500)

# --- calculations ---
gross_profit = revenue - cogs
operating_profit = gross_profit - opex
gross_margin = gross_profit / revenue * 100
operating_margin = operating_profit / revenue * 100
net_margin = operating_profit * 0.75 / revenue * 100  # assume 25% tax as illustrative net proxy

current_ratio = current_assets / current_liabilities
quick_ratio = (current_assets - inventory) / current_liabilities

debt_to_equity = total_debt / total_equity
roe = (operating_profit * 0.75) / total_equity * 100
roa = (operating_profit * 0.75) / total_assets * 100
asset_turnover = revenue / total_assets

st.divider()
st.markdown("## 📌 KPI Dashboard")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Gross Margin", f"{gross_margin:.1f}%")
k2.metric("Operating Margin", f"{operating_margin:.1f}%")
k3.metric("Net Margin (est.)", f"{net_margin:.1f}%")
k4.metric("Return on Equity (ROE)", f"{roe:.1f}%")

k5, k6, k7, k8 = st.columns(4)
k5.metric("Current Ratio", f"{current_ratio:.2f}")
k6.metric("Quick Ratio", f"{quick_ratio:.2f}")
k7.metric("Debt-to-Equity", f"{debt_to_equity:.2f}")
k8.metric("Asset Turnover", f"{asset_turnover:.2f}x")

# --- automatic insight flags ---
st.markdown("### 💡 Automatic Insight Flags")
flags = []
if current_ratio < 1:
    flags.append("🔴 **Liquidity risk**: current ratio below 1.0 — current liabilities exceed current assets.")
elif current_ratio < 1.5:
    flags.append("🟠 **Watch liquidity**: current ratio is on the low side (below 1.5).")
else:
    flags.append("🟢 Liquidity looks healthy (current ratio ≥ 1.5).")

if debt_to_equity > 2:
    flags.append("🔴 **High leverage**: debt-to-equity above 2.0 — the company relies heavily on debt.")
elif debt_to_equity > 1:
    flags.append("🟠 Leverage is moderate-to-high (debt-to-equity between 1 and 2).")
else:
    flags.append("🟢 Leverage looks conservative (debt-to-equity below 1.0).")

if gross_margin < 20:
    flags.append("🔴 **Thin gross margin** (below 20%) — cost structure or pricing may need review.")
else:
    flags.append("🟢 Gross margin is at a reasonable level (20%+).")

for f in flags:
    st.markdown(f)

st.divider()

# ----------------------------------------------------------------------------
# 3-YEAR TREND (synthetic prior years scaled off current-year inputs)
# ----------------------------------------------------------------------------
st.markdown("## 📈 3-Year Trend (Year 3 = your inputs above)")

years = ["Year 1", "Year 2", "Year 3 (current)"]
rev_series = [revenue * 0.85, revenue * 0.93, revenue]
gm_series = [gross_margin - 3, gross_margin - 1.2, gross_margin]
cr_series = [current_ratio * 0.9, current_ratio * 0.97, current_ratio]

fig = go.Figure()
fig.add_trace(go.Bar(x=years, y=rev_series, name="Revenue ($'000)", yaxis="y1", marker_color="#5B8FF9"))
fig.add_trace(go.Scatter(x=years, y=gm_series, name="Gross Margin (%)", yaxis="y2",
                          mode="lines+markers", line=dict(color="#E8684A", width=3)))
fig.add_trace(go.Scatter(x=years, y=cr_series, name="Current Ratio", yaxis="y2",
                          mode="lines+markers", line=dict(color="#5AD8A6", width=3, dash="dot")))

fig.update_layout(
    yaxis=dict(title="Revenue ($'000)"),
    yaxis2=dict(title="Ratio / %", overlaying="y", side="right"),
    legend=dict(orientation="h", y=-0.2),
    height=450,
    margin=dict(t=30),
)
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    "Try lowering **Revenue** while keeping **COGS** fixed — watch Gross Margin fall and see how the "
    "insight flags react. This is the descriptive foundation you'll build on in Module 4 (diagnosing *why*)."
)

st.divider()
st.info("➡️ Next: **Module 4 — Diagnostic Analytics**, to understand *why* the numbers moved.")
