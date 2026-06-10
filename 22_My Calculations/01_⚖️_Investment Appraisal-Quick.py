import streamlit as st
import numpy_financial as npf
import pandas as pd

# --- Page Layout & Headers ---
# Note: Layout configurations are cleanly inherited from your main 1_🤓_Homepage.py file
st.title("📊 Investment Appraisal Exercise")
st.markdown("""
Evaluate the financial viability of your project. Enter your initial outlay, 
expected discount rate (cost of capital), and the projected cash flows for each year.
""")

st.sidebar.header("🔧 Project Parameters")

# Step 1: Inputs for initial parameters
initial_investment = st.sidebar.number_input(
    "Initial Investment ($)", 
    min_value=0.0, 
    value=100000.0, 
    step=5000.0
)
discount_rate_pct = st.sidebar.slider(
    "Discount Rate / Cost of Capital (%)", 
    min_value=0.0, 
    max_value=30.0, 
    value=10.0, 
    step=0.5
)
discount_rate = discount_rate_pct / 100.0
years = st.sidebar.slider("Project Horizon (Years)", min_value=1, max_value=10, value=5)

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Annual Cash Inflows")

# Step 2: Dynamic generation of cash flow inputs based on chosen years
cash_flows = [-initial_investment]
for i in range(1, years + 1):
    flow = st.sidebar.number_input(f"Year {i} Cash Flow ($)", min_value=0.0, value=30000.0, step=1000.0)
    cash_flows.append(flow)

# --- Financial Calculations ---

# 1. Net Present Value (NPV)
npv = npf.npv(discount_rate, cash_flows)

# 2. Internal Rate of Return (IRR)
try:
    irr = npf.irr(cash_flows)
except Exception:
    irr = None

# 3. Payback Period & Cumulative Cash Flows
cumulative_cf = []
current_sum = 0
payback_period = None

for idx, cf in enumerate(cash_flows):
    current_sum += cf
    cumulative_cf.append(current_sum)
    if current_sum >= 0 and payback_period is None and idx > 0:
        # Simple linear interpolation for exact payback year fraction
        prev_sum = cumulative_cf[idx-1]
        payback_period = (idx - 1) + (abs(prev_sum) / cf)

# --- UI Layout & Results Presentation ---

col1, col2, col3 = st.columns(3)

with col1:
    if npv > 0:
        st.metric("Net Present Value (NPV)", f"${npv:,.2f}", delta="Viable Project")
    else:
        st.metric("Net Present Value (NPV)", f"${npv:,.2f}", delta="Not Viable", delta_color="inverse")

with col2:
    if irr is not None:
        st.metric("Internal Rate of Return (IRR)", f"{irr * 100:.2f}%")
    else:
        st.metric("Internal Rate of Return (IRR)", "N/A (No return generated)")

with col3:
    if payback_period is not None:
        st.metric("Payback Period", f"{payback_period:.2f} Years")
    else:
        st.metric("Payback Period", "Never Recouped")

st.markdown("---")

# Data Table & Chart Construction
years_axis = [f"Year {i}" if i > 0 else "Initial" for i in range(years + 1)]
df_metrics = pd.DataFrame({
    "Period": years_axis,
    "Net Cash Flow ($)": cash_flows,
    "Cumulative Cash Flow ($)": cumulative_cf
})

col_chart, col_table = st.columns([2, 1])

with col_chart:
    st.subheader("📈 Cumulative Cash Flow Trajectory")
    st.line_chart(df_metrics.set_index("Period")["Cumulative Cash Flow ($)"])

with col_table:
    st.subheader("📋 Cash Flow Table")
    st.dataframe(df_metrics, hide_index=True)

# Investment Verdict / Summary
st.subheader("💡 Financial Verdict")
if npv > 0:
    st.success(
        f"**Accept the project.** The NPV is positive (${npv:,.2f}), meaning the project yields "
        f"returns greater than your {discount_rate_pct}% cost of capital. Your initial investment "
        f"is expected to be fully recovered in {payback_period:.2f} years."
    )
else:
    st.error(
        f"**Reject the project.** The NPV is negative (${npv:,.2f}). This project does not generate "
        f"enough cash flow to cover the {discount_rate_pct}% required rate of return or the initial risk."
    )