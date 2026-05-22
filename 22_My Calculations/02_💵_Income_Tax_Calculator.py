import streamlit as st
import pandas as pd

# --- Standard Text Sizing Injection ---
# This CSS lowers the default font size of st.metric numbers so they align cleanly
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
st.markdown("### Bangladesh Income Tax Calculator")
st.markdown("""
Calculate individual income tax liability based on the updated provisions of the **Income Tax Act of Bangladesh**.
This workspace fully accounts for automatic statutory employment exemptions, investment rebates, and minimum tax thresholds.
""")

st.markdown("---")

# --- SIDEBAR INPUT PANEL ---
st.sidebar.markdown("### 👤 Taxpayer Profile")
category = st.sidebar.selectbox(
    "Taxpayer Category", 
    options=[
        "General Male Taxpayer", 
        "Female Taxpayer / Senior Citizen (Aged 65+)",
        "Physically Challenged Person / Third Gender", 
        "Gazetted War-Wounded Freedom Fighter"
    ], 
    key="tax_calc_category"
)
has_disabled_dependent = st.sidebar.checkbox(
    "Parent/Guardian of a physically challenged dependent?", 
    key="tax_calc_dependent"
)
location = st.sidebar.selectbox(
    "Residential Location", 
    options=[
        "Dhaka North / Dhaka South / Chattogram City Corporation", 
        "Other City Corporation Areas", 
        "Outside Any City Corporation Area"
    ], 
    key="tax_calc_location"
)
is_new_taxpayer = st.sidebar.checkbox(
    "Is this a first-time/new tax filer?", 
    key="tax_calc_new_filer"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💰 Income & Investments")

# User inputs Gross Income before the 1/3 statutory deduction rule
gross_income = st.sidebar.number_input(
    "Gross Annual Employment Income (BDT)", 
    min_value=0.0, 
    value=600000.0, 
    step=10000.0, 
    key="tax_calc_gross_income"
)

actual_investment = st.sidebar.number_input(
    "Actual Approved Investment (BDT)", 
    min_value=0.0, 
    value=50000.0, 
    step=5000.0, 
    key="tax_calc_investment"
)


# --- MAIN DISPLAY PANEL: FINANCIAL LOGIC & LEDGER ---
st.markdown("### 🔍 Financial Computation Ledger")

# --- STEP 1: Apply Employment Income Exemption Rule ---
# Formula: Lower of (1/3 of Gross Income) OR (BDT 500,000)
calculated_one_third = gross_income / 3.0
statutory_exemption_cap = 500000.0
allowed_exemption = min(calculated_one_third, statutory_exemption_cap)

# Calculate Net Taxable Income used to map progressive slabs
total_income = max(0.0, gross_income - allowed_exemption)

# --- STEP 2: Assign Basic Exemption Threshold ---
if category == "General Male Taxpayer": 
    base_threshold = 350000.0
elif category == "Female Taxpayer / Senior Citizen (Aged 65+)": 
    base_threshold = 400000.0
elif category == "Physically Challenged Person / Third Gender": 
    base_threshold = 475000.0
else: 
    base_threshold = 500000.0

if has_disabled_dependent: 
    base_threshold += 50000.0

# --- STEP 3: Progressive Slab Mapping ---
slabs = [
    {"limit": base_threshold, "rate": 0.0, "label": "Tax-Free Bracket"},
    {"limit": 100000.0, "rate": 0.05, "label": "Next BDT 100,000"},
    {"limit": 400000.0, "rate": 0.10, "label": "Next BDT 400,000"},
    {"limit": 500000.0, "rate": 0.15, "label": "Next BDT 500,000"},
    {"limit": 500000.0, "rate": 0.20, "label": "Next BDT 500,000"},
    {"limit": 2000000.0, "rate": 0.25, "label": "Next BDT 2,000,000"},
    {"limit": float('inf'), "rate": 0.30, "label": "Remaining Balance"}
]

remaining_income = total_income
slab_breakdown = []
calculated_tax = 0.0

for slab in slabs:
    if remaining_income <= 0: 
        break
    taxable_in_slab = min(remaining_income, slab["limit"])
    tax_in_slab = taxable_in_slab * slab["rate"]
    calculated_tax += tax_in_slab
    
    slab_breakdown.append({
        "Slab Bracket": slab["label"], 
        "Tax Rate": f"{slab['rate'] * 100:.0f}%",
        "Income in Slab (BDT)": taxable_in_slab, 
        "Tax Amount (BDT)": tax_in_slab
    })
    remaining_income -= taxable_in_slab

# --- STEP 4: Rebates & Floor Limits Engine ---
max_eligible_investment = min(actual_investment, total_income * 0.20, 10000000.0)
investment_rebate = max_eligible_investment * 0.15
tax_after_rebate = max(0.0, calculated_tax - investment_rebate)

# Minimum Tax Boundary Conditions
if total_income > base_threshold:
    if is_new_taxpayer: 
        min_tax_required = 1000.0
    else:
        if location == "Dhaka North / Dhaka South / Chattogram City Corporation": 
            min_tax_required = 5000.0
        elif location == "Other City Corporation Areas": 
            min_tax_required = 4000.0
        else: 
            min_tax_required = 3000.0
else: 
    min_tax_required = 0.0

final_tax_liability = min_tax_required if (total_income > base_threshold and tax_after_rebate < min_tax_required) else tax_after_rebate

# --- STEP 5: Calculate Effective Tax Rate ---
effective_tax_rate = (final_tax_liability / gross_income * 100.0) if gross_income > 0 else 0.0

# --- UI Rendering Output ---
m1, m2, m3, m4 = st.columns(4)
with m1: 
    st.metric("Statutory Exemption", f"৳ {allowed_exemption:,.2f}")
with m2: 
    st.metric("Net Taxable Base", f"৳ {total_income:,.2f}")
with m3: 
    st.metric("Net Tax Payable", f"৳ {final_tax_liability:,.2f}")
with m4:
    st.metric("Effective Tax Rate", f"{effective_tax_rate:.2f}%")

st.markdown("---")

# Progressive Slab Dataframe Display
if slab_breakdown:
    st.dataframe(pd.DataFrame(slab_breakdown), hide_index=True, use_container_width=True)
else:
    st.info("Net taxable income falls entirely within your specific Zero-Rate Bracket threshold.")

# Financial Summary Matrix
summary_data = {
    "Financial Component Details": [
        "Gross Registered Annual Earnings",
        "Allowed Employment Exemption (1/3 or 500k Cap)",
        "Net Calculation Taxable Base",
        "Tax-Free Allowance Boundary Cap",
        "Raw Progressive Calculated Slab Tax",
        "Investment Rebate Value (15% Credit)",
        "Final Tax Obligation Liability",
        "True Effective Economic Tax Burden"
    ],
    "Amount / Valuation": [
        f"৳ {gross_income:,.2f}", 
        f"৳ {allowed_exemption:,.2f}", 
        f"৳ {total_income:,.2f}", 
        f"৳ {base_threshold:,.2f}", 
        f"৳ {calculated_tax:,.2f}", 
        f"৳ {investment_rebate:,.2f}", 
        f"৳ {final_tax_liability:,.2f}",
        f"{effective_tax_rate:.2f}%"
    ]
}

st.dataframe(
    pd.DataFrame(summary_data), 
    hide_index=True, 
    use_container_width=True
)