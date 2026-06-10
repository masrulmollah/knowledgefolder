import streamlit as st
import pandas as pd

# --- Standard Text Sizing Injection ---
st.markdown(
    """
    <style>
    [data-testid="stMetricValue"] {
        font-size: 22px !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Page Header ---
st.markdown("### Integrated Financial Statements & Ratio Model")
st.markdown("""
Modify standard financial parameters in the left sidebar. The system will instantly regenerate your statements.
The **Ratio Analysis Matrix** at the bottom automatically evaluates performance against standard benchmark parameters using color alerts.
""")
st.markdown("---")

# ==========================================
# --- SIDEBAR: STANDARD FINANCIAL INPUTS ---
# ==========================================
st.sidebar.markdown("### 📋 Income Statement Parameters")
s_revenue = st.sidebar.number_input("Gross Revenue ($)", min_value=0.0, value=500000.0, step=10000.0, key="ifm_rev")
s_cogs = st.sidebar.number_input("Cost of Goods Sold (COGS) ($)", min_value=0.0, value=250000.0, step=10000.0, key="ifm_cogs")
s_opex = st.sidebar.number_input("Operating Expenses (SGA) ($)", min_value=0.0, value=120000.0, step=5000.0, key="ifm_opex")
s_depr = st.sidebar.number_input("Depreciation & Amortization ($)", min_value=0.0, value=20000.0, step=1000.0, key="ifm_depr")
s_interest = st.sidebar.number_input("Interest Expense ($)", min_value=0.0, value=10000.0, step=500.0, key="ifm_int")
s_tax_rate = st.sidebar.slider("Tax Rate (%)", min_value=0, max_value=50, value=25, key="ifm_tax")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏛️ Balance Sheet Parameters")
s_cash_init = st.sidebar.number_input("Beginning Cash Balance ($)", min_value=0.0, value=40000.0, step=2000.0, key="ifm_cash_i")
s_ar = st.sidebar.number_input("Accounts Receivable ($)", min_value=0.0, value=55000.0, step=2000.0, key="ifm_ar")
s_inventory = st.sidebar.number_input("Inventory ($)", min_value=0.0, value=65000.0, step=2000.0, key="ifm_inv")
s_ppe_gross = st.sidebar.number_input("Gross Property, Plant & Equip ($)", min_value=0.0, value=300000.0, step=10000.0, key="ifm_ppe")

s_ap = st.sidebar.number_input("Accounts Payable ($)", min_value=0.0, value=35000.0, step=2000.0, key="ifm_ap")
s_st_debt = st.sidebar.number_input("Short-Term Debt ($)", min_value=0.0, value=150000.0, step=5000.0, key="ifm_st_debt")
s_lt_debt = st.sidebar.number_input("Long-Term Debt ($)", min_value=0.0, value=100000.0, step=5000.0, key="ifm_lt_debt")

s_common_stock = st.sidebar.number_input("Common Stock ($)", min_value=0.0, value=100000.0, step=5000.0, key="ifm_stock")
s_re_begin = st.sidebar.number_input("Beginning Retained Earnings ($)", min_value=0.0, value=60000.0, step=5000.0, key="ifm_re_beg")
s_dividends = st.sidebar.number_input("Dividends Declared ($)", min_value=0.0, value=15000.0, step=1000.0, key="ifm_div")

# ==========================================
# --- FINANCIAL STATEMENTS COMPUTATION ---
# ==========================================

# 1. INCOME STATEMENT Calculations
gross_profit = s_revenue - s_cogs
ebitda = gross_profit - s_opex
ebit = ebitda - s_depr
ebt = ebit - s_interest
tax_expense = max(0.0, ebt * (s_tax_rate / 100.0))
net_income = ebt - tax_expense

# 2. RETAINED EARNINGS Statement Calculations
ending_retained_earnings = s_re_begin + net_income - s_dividends

# 3. BALANCE SHEET Calculations
total_current_assets_pre_cash = s_ar + s_inventory
net_ppe = s_ppe_gross - s_depr

# Total Current Liabilities
total_current_liabilities = s_ap + s_st_debt

# Total Liabilities & Equity calculation
total_liabilities = total_current_liabilities + s_lt_debt
total_equity = s_common_stock + ending_retained_earnings
total_liab_and_equity = total_liabilities + total_equity

# Cash identity check
computed_cash = total_liab_and_equity - total_current_assets_pre_cash - net_ppe
total_current_assets = computed_cash + total_current_assets_pre_cash
total_assets = total_current_assets + net_ppe

# 4. CASH FLOW STATEMENT Calculations (Indirect Method)
cash_from_operations = net_income + s_depr - (s_ar * 0.05) - (s_inventory * 0.02) + (s_ap * 0.03) 
cash_from_investing = -(s_ppe_gross * 0.05) 
cash_from_financing = (s_st_debt * 0.02) + (s_lt_debt * 0.01) - s_dividends
net_change_in_cash = cash_from_operations + cash_from_investing + cash_from_financing
final_cash_flow_balance = s_cash_init + net_change_in_cash

# ==========================================
# --- RENDERING THE FOUR CORE STATEMENTS ---
# ==========================================
tab_is, tab_bs, tab_re, tab_cf, tab_ratios = st.tabs([
    "🧾 1. Income Statement", 
    "🏛️ 2. Balance Sheet", 
    "📈 3. Retained Earnings",
    "💧 4. Cash Flow Statement",
    "📊 5. Financial Ratio Analysis"
])

with tab_is:
    st.markdown("#### Income Statement")
    is_data = {
        "Line Item Component": ["Gross Sales / Revenue", "Cost of Goods Sold (COGS)", "Gross Profit", "Operating Expenses (SG&A)", "EBITDA", "Depreciation & Amortization", "Operating Profit (EBIT)", "Interest Expense", "Earnings Before Tax (EBT)", "Income Tax Expense", "Net Profit / Income"],
        "Value ($)": [s_revenue, -s_cogs, gross_profit, -s_opex, ebitda, -s_depr, ebit, -s_interest, ebt, -tax_expense, net_income]
    }
    st.dataframe(pd.DataFrame(is_data).style.format({"Value ($)": "${:,.2f}"}), hide_index=True, use_container_width=True)

with tab_bs:
    st.markdown("#### Balance Sheet")
    col_as, col_li = st.columns(2)
    
    with col_as:
        st.markdown("**ASSETS**")
        assets_data = {
            "Asset Description": ["Cash & Equivalents (Balanced)", "Accounts Receivable", "Inventory Items", "Total Current Assets", "Net Property, Plant & Equip", "TOTAL ASSETS"],
            "Valuation ($)": [computed_cash, s_ar, s_inventory, total_current_assets, net_ppe, total_assets]
        }
        st.dataframe(pd.DataFrame(assets_data).style.format({"Valuation ($)": "${:,.2f}"}), hide_index=True, use_container_width=True)
        
    with col_li:
        st.markdown("**LIABILITIES & SHAREHOLDERS EQUITY**")
        liab_data = {
            "Obligation / Capital Component": ["Accounts Payable", "Short-Term Debt Obligations", "Total Current Liabilities", "Long-Term Corporate Debt", "Total Liabilities", "Common Capital Stock", "Ending Retained Earnings", "Total Shareholders Equity", "TOTAL LIABILITIES & EQUITY"],
            "Valuation ($)": [s_ap, s_st_debt, total_current_liabilities, s_lt_debt, total_liabilities, s_common_stock, ending_retained_earnings, total_equity, total_liab_and_equity]
        }
        st.dataframe(pd.DataFrame(liab_data).style.format({"Valuation ($)": "${:,.2f}"}), hide_index=True, use_container_width=True)

with tab_re:
    st.markdown("#### Statement of Retained Earnings")
    re_data = {
        "Retained Earnings Ledger Block": ["Beginning Retained Earnings Balance", "Add: Net Profit / Income Contribution", "Less: Dividends Declared/Distributed", "Ending Retained Earnings Balance"],
        "Value ($)": [s_re_begin, net_income, -s_dividends, ending_retained_earnings]
    }
    st.dataframe(pd.DataFrame(re_data).style.format({"Value ($)": "${:,.2f}"}), hide_index=True, use_container_width=True)

with tab_cf:
    st.markdown("#### Statement of Cash Flows (Indirect Layout Model)")
    cf_data = {
        "Cash Flow Statement Section": ["Net Profit / Income Base", "Adjust: Depreciation Non-Cash Addition", "Changes in Operations Working Capital", "Net Cash from Operating Activities", "Net Cash from Investing Activities", "Net Cash from Financing Activities", "Net Change in Cash Pool", "Beginning Cash Balance", "Ending Cash Balance Balance Line"],
        "Value ($)": [net_income, s_depr, (cash_from_operations - net_income - s_depr), cash_from_operations, cash_from_investing, cash_from_financing, net_change_in_cash, s_cash_init, final_cash_flow_balance]
    }
    st.dataframe(pd.DataFrame(cf_data).style.format({"Value ($)": "${:,.2f}"}), hide_index=True, use_container_width=True)

# ==========================================
# --- RATIO ANALYSIS ENGINE WITH COLOR ---
# ==========================================
with tab_ratios:
    st.markdown("#### Comprehensive Corporate Financial Ratios Matrix")
    
    # Pre-calculate Ratios safely
    c_ratio = (total_current_assets / total_current_liabilities) if total_current_liabilities > 0 else 0.0
    q_ratio = ((total_current_assets - s_inventory) / total_current_liabilities) if total_current_liabilities > 0 else 0.0
    
    gp_margin = (gross_profit / s_revenue * 100.0) if s_revenue > 0 else 0.0
    np_margin = (net_income / s_revenue * 100.0) if s_revenue > 0 else 0.0
    roa_pct = (net_income / total_assets * 100.0) if total_assets > 0 else 0.0
    roe_pct = (net_income / total_equity * 100.0) if total_equity > 0 else 0.0
    
    de_ratio = (total_liabilities / total_equity) if total_equity > 0 else 0.0
    da_ratio = (total_liabilities / total_assets) if total_assets > 0 else 0.0
    int_coverage = (ebit / s_interest) if s_interest > 0 else 0.0
    
    inv_turn = (s_cogs / s_inventory) if s_inventory > 0 else 0.0
    asset_turn = (s_revenue / total_assets) if total_assets > 0 else 0.0

    # Top Metrics Bar
    rm1, rm2, rm3, rm4 = st.columns(4)
    with rm1: st.metric("Current Ratio", f"{c_ratio:.2f}")
    with rm2: st.metric("Net Profit Margin", f"{np_margin:.1f}%")
    with rm3: st.metric("Debt-to-Equity", f"{de_ratio:.2f}")
    with rm4: st.metric("Asset Turnover", f"{asset_turn:.2f}x")
    
    st.markdown("---")

    # Raw Matrix Dictionary Array
    ratio_data_raw = [
        # LIQUIDITY BLOCK
        {"Block Category": "1. Liquidity Block", "Ratio KPI Name": "Current Ratio", "Standard Formula Rule": "Total Current Assets / Total Current Liabilities", "Standard Parameter": ">= 1.50", "Computed Value": c_ratio, "Display Value": f"{c_ratio:.2f}", "Status": ""},
        {"Block Category": "1. Liquidity Block", "Ratio KPI Name": "Quick Ratio (Acid-Test)", "Standard Formula Rule": "(Current Assets - Inventory) / Total Current Liabilities", "Standard Parameter": ">= 1.00", "Computed Value": q_ratio, "Display Value": f"{q_ratio:.2f}", "Status": ""},
        
        # PROFITABILITY BLOCK
        {"Block Category": "2. Profitability Block", "Ratio KPI Name": "Gross Profit Margin", "Standard Formula Rule": "(Gross Profit / Gross Revenue) * 100", "Standard Parameter": ">= 40.0%", "Computed Value": gp_margin, "Display Value": f"{gp_margin:.1f}%", "Status": ""},
        {"Block Category": "2. Profitability Block", "Ratio KPI Name": "Net Profit Margin", "Standard Formula Rule": "(Net Income / Gross Revenue) * 100", "Standard Parameter": ">= 10.0%", "Computed Value": np_margin, "Display Value": f"{np_margin:.1f}%", "Status": ""},
        {"Block Category": "2. Profitability Block", "Ratio KPI Name": "Return on Assets (ROA)", "Standard Formula Rule": "(Net Income / Total Assets) * 100", "Standard Parameter": ">= 5.0%", "Computed Value": roa_pct, "Display Value": f"{roa_pct:.1f}%", "Status": ""},
        {"Block Category": "2. Profitability Block", "Ratio KPI Name": "Return on Equity (ROE)", "Standard Formula Rule": "(Net Income / Total Shareholders Equity) * 100", "Standard Parameter": ">= 12.0%", "Computed Value": roe_pct, "Display Value": f"{roe_pct:.1f}%", "Status": ""},
        
        # LEVERAGE / SOLVENCY BLOCK
        {"Block Category": "3. Solvency & Leverage Block", "Ratio KPI Name": "Debt-to-Equity Ratio", "Standard Formula Rule": "Total Liabilities / Total Shareholders Equity", "Standard Parameter": "<= 1.50", "Computed Value": de_ratio, "Display Value": f"{de_ratio:.2f}", "Status": ""},
        {"Block Category": "3. Solvency & Leverage Block", "Ratio KPI Name": "Debt-to-Assets Ratio", "Standard Formula Rule": "Total Liabilities / Total Assets", "Standard Parameter": "<= 0.50", "Computed Value": da_ratio, "Display Value": f"{da_ratio:.2f}", "Status": ""},
        {"Block Category": "3. Solvency & Leverage Block", "Ratio KPI Name": "Interest Coverage Ratio", "Standard Formula Rule": "Operating Profit (EBIT) / Interest Expense", "Standard Parameter": ">= 3.00x", "Computed Value": int_coverage, "Display Value": f"{int_coverage:.2f}x", "Status": ""},
        
        # EFFICIENCY BLOCK
        {"Block Category": "4. Operational Efficiency Block", "Ratio KPI Name": "Inventory Turnover Ratio", "Standard Formula Rule": "Cost of Goods Sold (COGS) / Closing Inventory Value", "Standard Parameter": ">= 4.00x", "Computed Value": inv_turn, "Display Value": f"{inv_turn:.2f}x", "Status": ""},
        {"Block Category": "4. Operational Efficiency Block", "Ratio KPI Name": "Total Asset Turnover Ratio", "Standard Formula Rule": "Gross Revenue / Total Comprehensive Assets", "Standard Parameter": ">= 1.00x", "Computed Value": asset_turn, "Display Value": f"{asset_turn:.2f}x", "Status": ""}
    ]

    # Assign internal categorical states (Green, Amber, Red) based on explicit rules
    for r in ratio_data_raw:
        name = r["Ratio KPI Name"]
        val = r["Computed Value"]
        
        if name == "Current Ratio":
            r["Status"] = "🟢 Optimal" if val >= 1.5 else ("🟡 Warning" if val >= 1.0 else "🔴 Critical Risk")
        elif name == "Quick Ratio (Acid-Test)":
            r["Status"] = "🟢 Optimal" if val >= 1.0 else ("🟡 Warning" if val >= 0.7 else "🔴 Critical Risk")
        elif name == "Gross Profit Margin":
            r["Status"] = "🟢 Optimal" if val >= 40.0 else ("🟡 Warning" if val >= 25.0 else "🔴 Critical Risk")
        elif name == "Net Profit Margin":
            r["Status"] = "🟢 Optimal" if val >= 10.0 else ("🟡 Warning" if val >= 5.0 else "🔴 Critical Risk")
        elif name == "Return on Assets (ROA)":
            r["Status"] = "🟢 Optimal" if val >= 5.0 else ("🟡 Warning" if val >= 2.0 else "🔴 Critical Risk")
        elif name == "Return on Equity (ROE)":
            r["Status"] = "🟢 Optimal" if val >= 12.0 else ("🟡 Warning" if val >= 6.0 else "🔴 Critical Risk")
        elif name == "Debt-to-Equity Ratio":
            r["Status"] = "🟢 Optimal" if val <= 1.5 else ("🟡 Warning" if val <= 2.5 else "🔴 Critical Risk")
        elif name == "Debt-to-Assets Ratio":
            r["Status"] = "🟢 Optimal" if val <= 0.5 else ("🟡 Warning" if val <= 0.7 else "🔴 Critical Risk")
        elif name == "Interest Coverage Ratio":
            r["Status"] = "🟢 Optimal" if val >= 3.0 else ("🟡 Warning" if val >= 1.5 else "🔴 Critical Risk")
        elif name == "Inventory Turnover Ratio":
            r["Status"] = "🟢 Optimal" if val >= 4.0 else ("🟡 Warning" if val >= 2.0 else "🔴 Critical Risk")
        elif name == "Total Asset Turnover Ratio":
            r["Status"] = "🟢 Optimal" if val >= 1.0 else ("🟡 Warning" if val >= 0.5 else "🔴 Critical Risk")

    # Convert to Dataframe and prune evaluation columns out of visual render
    df_styled = pd.DataFrame(ratio_data_raw)
    df_visual = df_styled[["Block Category", "Ratio KPI Name", "Standard Formula Rule", "Standard Parameter", "Display Value", "Status"]].copy()
    df_visual.rename(columns={"Display Value": "Computed Value"}, inplace=True)

    # --- PANDAS DYNAMIC HIGHLIGHT ENGINE ---
    def apply_row_metrics_color(row):
        status = row["Status"]
        # Default fallback values for standard typography readability
        bg_color = "transparent"
        text_color = "inherit"
        
        if "🟢" in status:
            bg_color = "#d4edda"  # Soft corporate green
            text_color = "#155724"
        elif "🟡" in status:
            bg_color = "#fff3cd"  # Soft corporate yellow/amber
            text_color = "#856404"
        elif "🔴" in status:
            bg_color = "#f8d7da"  # Soft corporate red
            text_color = "#721c24"
            
        return [f"background-color: {bg_color}; color: {text_color}; font-weight: 500;"] * len(row)

    # Render Styled Table Matrix
    st.dataframe(
        df_visual.style.apply(apply_row_metrics_color, axis=1), 
        hide_index=True, 
        use_container_width=True
    )