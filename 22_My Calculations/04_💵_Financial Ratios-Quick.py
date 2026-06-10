import streamlit as st
import pandas as pd

# --- Standard Text Sizing Injection ---
st.markdown(
    """
    <style>
    [data-testid="stMetricValue"] {
        font-size: 24px !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Page Layout & Headers ---
st.markdown("### Financial Ratios Workspace Calculator")
st.markdown("""
Analyze core corporate wellness indicators across Liquidity, Profitability, Leverage, and Efficiency blocks.
Provide numbers from your Balance Sheet and Income Statement in the sidebar to generate performance cards.
""")

st.markdown("---")

# --- SIDEBAR INPUT PANEL ---
st.sidebar.markdown("### 📋 Income Statement Elements")
revenue = st.sidebar.number_input("Total Sales / Revenue ($)", min_value=0.0, value=500000.0, step=10000.0, key="fr_revenue")
cogs = st.sidebar.number_input("Cost of Goods Sold (COGS) ($)", min_value=0.0, value=300000.0, step=10000.0, key="fr_cogs")
ebit = st.sidebar.number_input("Earnings Before Interest & Taxes (EBIT) ($)", min_value=0.0, value=85000.0, step=5000.0, key="fr_ebit")
interest_expense = st.sidebar.number_input("Annual Interest Expense ($)", min_value=0.0, value=10000.0, step=500.0, key="fr_interest")
net_income = st.sidebar.number_input("Net Corporate Profit ($)", min_value=0.0, value=55000.0, step=2500.0, key="fr_net_income")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏛️ Balance Sheet Elements")
current_assets = st.sidebar.number_input("Total Current Assets ($)", min_value=0.0, value=150000.0, step=5000.0, key="fr_curr_assets")
inventory = st.sidebar.number_input("Closing Inventory Asset ($)", min_value=0.0, value=45000.0, step=2500.0, key="fr_inventory")
total_assets = st.sidebar.number_input("Total Comprehensive Assets ($)", min_value=0.0, value=400000.0, step=10000.0, key="fr_total_assets")
current_liabilities = st.sidebar.number_input("Total Current Liabilities ($)", min_value=0.0, value=80000.0, step=5000.0, key="fr_curr_liab")
total_liabilities = st.sidebar.number_input("Total Long & Short Term Debt ($)", min_value=0.0, value=180000.0, step=5000.0, key="fr_total_liab")
equity = st.sidebar.number_input("Shareholder's Net Equity ($)", min_value=0.0, value=220000.0, step=10000.0, key="fr_equity")


# --- FINANCIAL LOGIC ENGINE ---
ratio_records = []

# Block 1: Liquidity calculations (Short-term debt coverage metrics)
current_ratio = (current_assets / current_liabilities) if current_liabilities > 0 else 0.0
quick_ratio = ((current_assets - inventory) / current_liabilities) if current_liabilities > 0 else 0.0

ratio_records.extend([
    {"Category": "Liquidity", "Ratio Name": "Current Ratio", "Value": f"{current_ratio:.2f}", "Benchmark Target": "> 1.50", "Assessment": "Healthy Working Cap" if current_ratio >= 1.5 else "Tight Short-term Cover"},
    {"Category": "Liquidity", "Ratio Name": "Quick Ratio (Acid-Test)", "Value": f"{quick_ratio:.2f}", "Benchmark Target": "> 1.00", "Assessment": "Excellent Immediate Cash" if quick_ratio >= 1.0 else "Dependent on Inventory Speed"}
])

# Block 2: Profitability calculations (Margin conversions and asset return yields)
gross_profit_margin = ((revenue - cogs) / revenue * 100.0) if revenue > 0 else 0.0
net_profit_margin = (net_income / revenue * 100.0) if revenue > 0 else 0.0
roa = (net_income / total_assets * 100.0) if total_assets > 0 else 0.0
roe = (net_income / equity * 100.0) if equity > 0 else 0.0

ratio_records.extend([
    {"Category": "Profitability", "Ratio Name": "Gross Profit Margin", "Value": f"{gross_profit_margin:.2f}%", "Benchmark Target": "Varies by Sector", "Assessment": "Production Spread Capture"},
    {"Category": "Profitability", "Ratio Name": "Net Profit Margin", "Value": f"{net_profit_margin:.2f}%", "Benchmark Target": "> 10.00%", "Assessment": "Strong Expense Optimization" if net_profit_margin >= 10 else "Compressed Returns"},
    {"Category": "Profitability", "Ratio Name": "Return on Assets (ROA)", "Value": f"{roa:.2f}%", "Benchmark Target": "> 5.00%", "Assessment": "Efficient Capital Deploy" if roa >= 5 else "Underutilized Infrastructure Assets"},
    {"Category": "Profitability", "Ratio Name": "Return on Equity (ROE)", "Value": f"{roe:.2f}%", "Benchmark Target": "> 15.00%", "Assessment": "Great Value Generation" if roe >= 15 else "Low Shareholder Value Generation"}
])

# Block 3: Solvency & Leverage calculations (Capital structure boundaries)
debt_to_equity = (total_liabilities / equity) if equity > 0 else 0.0
equity_ratio = (equity / total_assets) if total_assets > 0 else 0.0
interest_coverage = (ebit / interest_expense) if interest_expense > 0 else 0.0

ratio_records.extend([
    {"Category": "Solvency / Leverage", "Ratio Name": "Debt-to-Equity Ratio", "Value": f"{debt_to_equity:.2f}", "Benchmark Target": "< 2.00", "Assessment": "Safe Leverage Exposure" if debt_to_equity <= 2 else "High Creditor Risk Exposure"},
    {"Category": "Solvency / Leverage", "Ratio Name": "Equity Financing Ratio", "Value": f"{equity_ratio:.2f}", "Benchmark Target": "> 0.50", "Assessment": "Asset Stability Funded" if equity_ratio >= 0.5 else "Aggressive External Leverage"},
    {"Category": "Solvency / Leverage", "Ratio Name": "Interest Coverage Ratio", "Value": f"{interest_coverage:.2f}x", "Benchmark Target": "> 3.00x", "Assessment": "Safe Servicing Spread" if interest_coverage >= 3 else "High Default Structural Risk"}
])

# Block 4: Efficiency calculations (Asset turnover operational velocities)
inventory_turnover = (cogs / inventory) if inventory > 0 else 0.0
asset_turnover = (revenue / total_assets) if total_assets > 0 else 0.0

ratio_records.extend([
    {"Category": "Efficiency / Activity", "Ratio Name": "Inventory Turnover", "Value": f"{inventory_turnover:.2f}x", "Benchmark Target": "4.0x - 8.0x", "Assessment": "Active Operations Velocity" if inventory_turnover >= 4 else "Slow Moving Warehouse Idle Capital"},
    {"Category": "Efficiency / Activity", "Ratio Name": "Total Asset Turnover", "Value": f"{asset_turnover:.2f}x", "Benchmark Target": "> 1.00x", "Assessment": "Excellent Asset Revenue Optimization" if asset_turnover >= 1 else "Low Utilization Velocity"}
])


# --- MAIN INTERACTIVE DISPLAY BLOCKS ---

# Block A: Liquidity Presentation Row
st.markdown("#### 💧 1. Short-Term Liquidity Performance")
col_l1, col_l2 = st.columns(2)
with col_l1:
    st.metric("Current Ratio (CA / CL)", f"{current_ratio:.2f}", help="Measures capacity to handle obligations maturing within 12 months.")
with col_l2:
    st.metric("Quick Ratio (Cash + AR / CL)", f"{quick_ratio:.2f}", help="Stricter index removing warehouse inventory values.")

st.markdown("---")

# Block B: Profitability Presentation Row
st.markdown("#### 💰 2. Profitability Margin Yields")
col_p1, col_p2, col_p3, col_p4 = st.columns(4)
with col_p1:
    st.metric("Gross Profit Margin", f"{gross_profit_margin:.1f}%")
with col_p2:
    st.metric("Net Profit Margin", f"{net_profit_margin:.1f}%")
with col_p3:
    st.metric("Return on Assets (ROA)", f"{roa:.1f}%")
with col_p4:
    st.metric("Return on Equity (ROE)", f"{roe:.1f}%")

st.markdown("---")

# Block C: Solvency & Leverage Presentation Row
st.markdown("#### 🛡️ 3. Solvency & Structural Leverage")
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.metric("Debt-to-Equity (D / E)", f"{debt_to_equity:.2f}")
with col_s2:
    st.metric("Equity Asset Ratio", f"{equity_ratio:.2f}")
with col_s3:
    st.metric("Interest Coverage Metric", f"{interest_coverage:.1f}x")

st.markdown("---")

# Block D: Operational Efficiency Presentation Row
st.markdown("#### ⚙️ 4. Asset Efficiency Operations")
col_e1, col_e2 = st.columns(2)
with col_e1:
    st.metric("Inventory Turnover Frequency", f"{inventory_turnover:.2f}x")
with col_e2:
    st.metric("Total Asset Turnover Velocity", f"{asset_turnover:.2f}x")

st.markdown("---")

# Comprehensive Performance Ledger Table View
st.markdown("### 📊 Consolidated Corporate Ratio Ledger")
df_ratios = pd.DataFrame(ratio_records)
st.dataframe(df_ratios, hide_index=True, use_container_width=True)