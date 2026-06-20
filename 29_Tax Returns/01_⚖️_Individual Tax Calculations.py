"""
Bangladesh Individual Income Tax Calculator
============================================
Income Tax Act 2023 | Finance Ordinance 2025
Covers Assessment Years: AY 2024-25, AY 2025-26, AY 2026-27 & AY 2027-28

HOW TO RUN
----------
    pip install streamlit pandas
    streamlit run bd_income_tax_calculator.py

TABS
----
  🧮 Inputs          — All personal details, income heads, investments
  📄 Salary Income   — Detailed salary computation with exemptions
  🏠 Other Income    — House property, business, capital gains, other sources
  📊 Tax Computation — Slab-wise tax, rebate, surcharge, final liability
  💰 Investment Rebate — Detailed rebate computation (Section 78)
  💼 Wealth & Surcharge — Net wealth statement and surcharge calculation
  🗒️ Tax Return Summary — Complete return-ready summary with TDS reconciliation
  📚 Tax Guide       — Key provisions reference under ITA 2023
"""

import streamlit as st
import pandas as pd

# ── PAGE IDENTITY ──────────────────────────────────────────────────────────
BDT = "৳"   # taka symbol

# ── TAX SLABS BY ASSESSMENT YEAR ──────────────────────────────────────────
# Each slab: (upper_limit_or_None, rate)
# None = remaining / top bracket

TAX_SLABS = {
    "AY 2024-25": [
        (350_000,  0.00),
        (100_000,  0.05),
        (400_000,  0.10),
        (500_000,  0.15),
        (2_000_000, 0.20),
        (None,     0.25),
    ],
    "AY 2025-26": [
        (350_000,  0.00),
        (100_000,  0.05),
        (400_000,  0.10),
        (500_000,  0.15),
        (500_000,  0.20),
        (2_000_000, 0.25),
        (None,     0.30),
    ],
    "AY 2026-27": [
        (375_000,  0.00),
        (300_000,  0.10),
        (400_000,  0.15),
        (500_000,  0.20),
        (2_000_000, 0.25),
        (None,     0.30),
    ],
    "AY 2027-28": [
        (375_000,  0.00),
        (300_000,  0.10),
        (400_000,  0.15),
        (500_000,  0.20),
        (2_000_000, 0.25),
        (None,     0.30),
    ],
}

# Tax-free thresholds by taxpayer category & AY
TAX_FREE = {
    "AY 2024-25": {
        "General (Male)": 350_000,
        "Female / Age 65+": 400_000,
        "Person with Disability": 475_000,
        "Third Gender": 475_000,
        "War-Wounded Freedom Fighter": 500_000,
        "Parent/Guardian of Disabled Child (+50k)": 400_000,
    },
    "AY 2025-26": {
        "General (Male)": 350_000,
        "Female / Age 65+": 400_000,
        "Person with Disability": 475_000,
        "Third Gender": 475_000,
        "War-Wounded Freedom Fighter": 500_000,
        "Parent/Guardian of Disabled Child (+50k)": 400_000,
    },
    "AY 2026-27": {
        "General (Male)": 375_000,
        "Female / Age 65+": 425_000,
        "Person with Disability": 500_000,
        "Third Gender": 500_000,
        "War-Wounded Freedom Fighter / July Fighter 2024": 525_000,
        "Parent/Guardian of Disabled Child (+50k)": 425_000,
    },
    "AY 2027-28": {
        "General (Male)": 375_000,
        "Female / Age 65+": 425_000,
        "Person with Disability": 500_000,
        "Third Gender": 500_000,
        "War-Wounded Freedom Fighter / July Fighter 2024": 525_000,
        "Parent/Guardian of Disabled Child (+50k)": 425_000,
    },
}

# Minimum tax by area & AY
MIN_TAX = {
    "AY 2024-25": {"Dhaka / Chittagong City Corp.": 5_000, "Other City Corporations": 4_000, "District / Upazila": 3_000},
    "AY 2025-26": {"Dhaka / Chittagong City Corp.": 5_000, "Other City Corporations": 4_000, "District / Upazila": 3_000},
    "AY 2026-27": {"Dhaka / Chittagong City Corp.": 5_000, "Other City Corporations": 5_000, "District / Upazila": 5_000},
    "AY 2027-28": {"Dhaka / Chittagong City Corp.": 5_000, "Other City Corporations": 5_000, "District / Upazila": 5_000},
}

# Surcharge thresholds (net wealth in BDT crore)
SURCHARGE_RATES = [
    (4_00_00_000,   10_00_00_000, 0.10),   # 4–10 crore
    (10_00_00_000,  20_00_00_000, 0.20),   # 10–20 crore
    (20_00_00_000,  50_00_00_000, 0.25),   # 20–50 crore
    (50_00_00_000,  None,         0.30),   # >50 crore
]

# ── SESSION STATE ──────────────────────────────────────────────────────────
DEFAULTS = {
    # Identity
    "taxpayer_name": "Md. Rafiqul Islam",
    "tin": "123456789012",
    "assessment_year": "AY 2025-26",
    "taxpayer_category": "General (Male)",
    "residential_area": "Dhaka / Chittagong City Corp.",
    "resident_status": "Resident",
    "is_new_taxpayer": False,

    # Salary income
    "basic_salary": 600_000.0,
    "house_rent_allowance": 300_000.0,
    "medical_allowance": 60_000.0,
    "conveyance_allowance": 36_000.0,
    "festival_bonus": 100_000.0,
    "performance_bonus": 50_000.0,
    "leave_encashment": 20_000.0,
    "employer_pf_contribution": 60_000.0,
    "employee_pf_contribution": 60_000.0,
    "gratuity_received": 0.0,
    "other_allowances": 24_000.0,
    "car_provided_by_employer": False,
    "car_cc": "Up to 2500 cc",
    "accommodation_provided": False,

    # House property income
    "annual_rent_received": 180_000.0,
    "municipal_tax_paid": 5_000.0,
    "interest_on_home_loan": 30_000.0,
    "vacancy_allowance_pct": 0.0,
    "has_rental_income": True,

    # Business / profession income
    "business_profit": 0.0,
    "professional_income": 0.0,
    "has_business_income": False,

    # Agricultural income
    "agricultural_income": 0.0,
    "has_agri_income": False,

    # Capital gains
    "capital_gain_shares_listed": 0.0,
    "capital_gain_shares_unlisted": 0.0,
    "capital_gain_property_lt5yr": 0.0,    # held ≤5 years — added to income
    "capital_gain_property_gt5yr": 0.0,    # held >5 years — flat 15%
    "has_capital_gains": False,

    # Other income
    "bank_interest": 45_000.0,
    "savings_cert_interest": 80_000.0,
    "dividend_listed": 30_000.0,
    "dividend_unlisted": 0.0,
    "foreign_remittance": 0.0,
    "other_income": 10_000.0,
    "has_other_income": True,

    # TDS / Advance Tax
    "tds_salary": 18_000.0,
    "tds_bank_interest": 6_750.0,       # typically 10% withheld
    "tds_savings_cert": 0.0,
    "tds_rent": 0.0,
    "tds_other": 0.0,
    "advance_tax_paid": 0.0,
    "tax_paid_with_return": 0.0,

    # Investment / Rebate (Section 78)
    "inv_life_insurance": 24_000.0,
    "inv_pf_employee": 60_000.0,
    "inv_pf_employer": 60_000.0,        # included but may have limits
    "inv_dps": 60_000.0,
    "inv_sanchayapatra": 200_000.0,
    "inv_govt_securities": 0.0,
    "inv_listed_shares_mf": 50_000.0,
    "inv_approved_debentures": 0.0,
    "inv_housing_loan_principal": 0.0,
    "inv_zakat": 0.0,
    "inv_donation_approved": 10_000.0,
    "inv_other": 0.0,

    # Net wealth for surcharge
    "wealth_cash_bank": 500_000.0,
    "wealth_investments": 350_000.0,
    "wealth_sanchayapatra": 200_000.0,
    "wealth_loans_receivable": 0.0,
    "wealth_land_building": 3_000_000.0,
    "wealth_vehicles": 800_000.0,
    "wealth_business_capital": 0.0,
    "wealth_jewellery": 200_000.0,
    "wealth_furniture": 150_000.0,
    "wealth_other_assets": 100_000.0,
    "wealth_liabilities": 500_000.0,
    "owns_multiple_cars": False,
    "property_area_sqft": 0.0,
}

if "bd" not in st.session_state:
    st.session_state["bd"] = DEFAULTS.copy()

def reset():
    st.session_state["bd"] = DEFAULTS.copy()

def V(k):
    return st.session_state["bd"][k]

# ── FORMATTERS ─────────────────────────────────────────────────────────────
def fmt(x, d=0):
    if x is None: return ""
    neg = x < 0
    s = f"{abs(x):,.{d}f}"
    return f"({s})" if neg else s

def bdt(x, d=0):
    return f"{BDT} {fmt(x, d)}"

def pct_fmt(x, d=2):
    return f"{x*100:.{d}f}%"

# ── CORE COMPUTATION ENGINE ────────────────────────────────────────────────

def compute():
    v = st.session_state["bd"]
    ay = v["assessment_year"]
    cat = v["taxpayer_category"]
    area = v["residential_area"]

    # ── 1. SALARY INCOME ──────────────────────────────────────────────────
    gross_salary = (v["basic_salary"] + v["house_rent_allowance"] + v["medical_allowance"]
                    + v["conveyance_allowance"] + v["festival_bonus"] + v["performance_bonus"]
                    + v["leave_encashment"] + v["employer_pf_contribution"]
                    + v["other_allowances"])

    # Employer car perquisite
    car_perquisite = 0.0
    if v["car_provided_by_employer"]:
        car_perquisite = 60_000.0 if v["car_cc"] == "Up to 2500 cc" else 120_000.0

    # Employer accommodation perquisite (if no HRA)
    accommodation_perquisite = 0.0
    if v["accommodation_provided"]:
        accommodation_perquisite = v["basic_salary"] * 0.25  # 25% of basic

    gross_salary_with_perqs = gross_salary + car_perquisite + accommodation_perquisite

    # Exemption: lower of 1/3 of employment income or BDT 500,000
    salary_exemption_limit = 500_000 if ay in ("AY 2025-26","AY 2026-27","AY 2027-28") else 450_000
    salary_exemption = min(gross_salary_with_perqs / 3, salary_exemption_limit)

    # PF: employee contribution — exempt; employer contribution taxable if >1/3 basic or >150k
    pf_employee = v["employee_pf_contribution"]  # deducted separately via rebate
    pf_employer = v["employer_pf_contribution"]
    pf_taxable_limit = min(v["basic_salary"] / 3, 150_000)
    pf_employer_taxable = max(0, pf_employer - pf_taxable_limit)

    # Gratuity: exempt if from approved fund (assume approved here; user can adjust)
    gratuity_taxable = 0.0  # fully exempt from approved fund

    taxable_salary = max(0, gross_salary_with_perqs + pf_employer_taxable
                         + gratuity_taxable - salary_exemption - pf_employee)

    # ── 2. HOUSE PROPERTY INCOME ─────────────────────────────────────────
    taxable_house_property = 0.0
    annual_rent = v["annual_rent_received"] if v["has_rental_income"] else 0.0
    if annual_rent > 0:
        # Allowable deductions: 30% repair & collection + municipal tax + home loan interest
        repair_deduction = annual_rent * 0.30
        net_rent = annual_rent - repair_deduction - v["municipal_tax_paid"] - v["interest_on_home_loan"]
        vacancy_deduction = net_rent * (v["vacancy_allowance_pct"] / 100)
        taxable_house_property = max(0, net_rent - vacancy_deduction)

    # ── 3. BUSINESS / PROFESSIONAL INCOME ───────────────────────────────
    taxable_business = 0.0
    if v["has_business_income"]:
        taxable_business = v["business_profit"] + v["professional_income"]

    # ── 4. AGRICULTURAL INCOME ───────────────────────────────────────────
    taxable_agri = 0.0
    if v["has_agri_income"]:
        taxable_agri = v["agricultural_income"]

    # ── 5. CAPITAL GAINS ─────────────────────────────────────────────────
    cap_gain_normal = 0.0   # added to total income → taxed at slab
    cap_gain_flat15 = 0.0   # taxed at flat 15%
    if v["has_capital_gains"]:
        # Listed shares — 15% flat (final withholding, usually)
        cap_gain_flat15 += v["capital_gain_shares_listed"]
        # Unlisted shares — added to income
        cap_gain_normal += v["capital_gain_shares_unlisted"]
        # Property held ≤5 years — added to income
        cap_gain_normal += v["capital_gain_property_lt5yr"]
        # Property held >5 years — flat 15%
        cap_gain_flat15 += v["capital_gain_property_gt5yr"]

    # ── 6. OTHER INCOME ──────────────────────────────────────────────────
    bank_interest = v["bank_interest"] if v["has_other_income"] else 0.0
    sanchayapatra_interest = v["savings_cert_interest"] if v["has_other_income"] else 0.0
    dividend_listed = v["dividend_listed"] if v["has_other_income"] else 0.0
    dividend_unlisted = v["dividend_unlisted"] if v["has_other_income"] else 0.0
    foreign_remittance = v["foreign_remittance"] if v["has_other_income"] else 0.0
    other_misc = v["other_income"] if v["has_other_income"] else 0.0

    # Dividend exemption: first BDT 25,000 exempt for listed companies
    dividend_listed_taxable = max(0, dividend_listed - 25_000)
    # Foreign remittance — fully exempt if received through banking channel
    foreign_remittance_taxable = 0.0  # exempt

    taxable_other = (bank_interest + sanchayapatra_interest
                     + dividend_listed_taxable + dividend_unlisted
                     + other_misc)

    # ── 7. TOTAL INCOME ──────────────────────────────────────────────────
    total_income = (taxable_salary + taxable_house_property + taxable_business
                    + taxable_agri + cap_gain_normal + taxable_other)

    # ── 8. TAX-FREE THRESHOLD ────────────────────────────────────────────
    threshold = TAX_FREE[ay][cat]

    # ── 9. SLAB-WISE TAX ON NORMAL INCOME ───────────────────────────────
    slabs_used = []
    remaining = total_income
    gross_tax_normal = 0.0
    slabs = TAX_SLABS[ay]

    for i, (band, rate) in enumerate(slabs):
        if remaining <= 0:
            break
        # Adjust first band for threshold
        if i == 0:
            taxable_in_band = max(0, min(remaining, threshold) - 0)
            # First slab is 0% so no tax regardless
            if band is None:
                chunk = remaining
            else:
                chunk = min(remaining, band)
            tax_in_band = max(0, chunk - threshold) * rate if threshold < band else 0.0
            taxable_chunk = max(0, chunk - threshold) if threshold < (band or float('inf')) else 0.0
            slabs_used.append((f"First {bdt(band or 0)} (0%)", chunk, 0.0, 0.0))
            remaining -= chunk
            # now account for threshold
        else:
            chunk = min(remaining, band) if band is not None else remaining
            tax_in_band = chunk * rate
            gross_tax_normal += tax_in_band
            label = f"Next {bdt(band)} @ {rate*100:.0f}%" if band else f"Remaining @ {rate*100:.0f}%"
            slabs_used.append((label, chunk, rate, tax_in_band))
            remaining -= chunk
        if remaining <= 0:
            break

    # Proper slab calculation
    slabs_used = []
    gross_tax_normal = 0.0
    remaining = max(0, total_income - threshold)

    for band, rate in slabs[1:]:  # skip 0% band
        if remaining <= 0:
            break
        chunk = min(remaining, band) if band is not None else remaining
        tax_in_band = chunk * rate
        gross_tax_normal += tax_in_band
        label = (f"Next {bdt(band)} @ {rate*100:.0f}%" if band
                 else f"Remaining @ {rate*100:.0f}%")
        slabs_used.append((label, chunk, rate, tax_in_band))
        remaining -= chunk

    # ── 10. TAX ON FLAT-RATE INCOME ──────────────────────────────────────
    tax_cap_gain_flat15 = cap_gain_flat15 * 0.15

    # ── 11. GROSS TAX ────────────────────────────────────────────────────
    gross_tax = gross_tax_normal + tax_cap_gain_flat15

    # ── 12. NON-RESIDENT ─────────────────────────────────────────────────
    if v["resident_status"] == "Non-Resident (Foreign National)":
        gross_tax = total_income * 0.30
        slabs_used = [("Flat 30% (Non-Resident)", total_income, 0.30, gross_tax)]

    # ── 13. INVESTMENT REBATE (Section 78) ───────────────────────────────
    # Eligible investments
    total_investment = (v["inv_life_insurance"] + v["inv_pf_employee"]
                        + min(v["inv_dps"], 60_000)  # DPS capped at 60k
                        + v["inv_sanchayapatra"]
                        + v["inv_govt_securities"]
                        + v["inv_listed_shares_mf"]
                        + v["inv_approved_debentures"]
                        + v["inv_housing_loan_principal"]
                        + v["inv_zakat"]
                        + v["inv_donation_approved"]
                        + v["inv_other"])

    # Admissible investment: lower of (a) actual, (b) 25% of total income, (c) BDT 1 crore
    admissible_investment = min(
        total_investment,
        total_income * 0.25,
        10_000_000  # BDT 1 crore cap
    )

    # Rebate: 15% of admissible investment
    investment_rebate = admissible_investment * 0.15

    # Rebate cannot exceed gross tax
    investment_rebate = min(investment_rebate, gross_tax)

    # ── 14. TAX AFTER REBATE ─────────────────────────────────────────────
    tax_after_rebate = max(0, gross_tax - investment_rebate)

    # ── 15. MINIMUM TAX ──────────────────────────────────────────────────
    is_new_taxpayer = v["is_new_taxpayer"]
    min_tax_amount = MIN_TAX[ay][area]
    if is_new_taxpayer and ay in ("AY 2026-27","AY 2027-28"):
        min_tax_amount = 1_000
    elif is_new_taxpayer:
        min_tax_amount = 0  # no minimum for new taxpayers in earlier years

    # Minimum tax applies only if income exceeds tax-free threshold
    if total_income <= threshold:
        min_tax_amount = 0

    final_tax_before_surcharge = max(tax_after_rebate, min_tax_amount)
    applied_min_tax = final_tax_before_surcharge > tax_after_rebate

    # ── 16. SURCHARGE ────────────────────────────────────────────────────
    net_wealth = (v["wealth_cash_bank"] + v["wealth_investments"] + v["wealth_sanchayapatra"]
                  + v["wealth_loans_receivable"] + v["wealth_land_building"]
                  + v["wealth_vehicles"] + v["wealth_business_capital"]
                  + v["wealth_jewellery"] + v["wealth_furniture"] + v["wealth_other_assets"]
                  - v["wealth_liabilities"])

    surcharge_rate = 0.0
    surcharge_reason = "No surcharge (net wealth ≤ BDT 4 crore)"
    for low, high, rate in SURCHARGE_RATES:
        if net_wealth > low:
            if high is None or net_wealth <= high:
                surcharge_rate = rate
                surcharge_reason = f"{rate*100:.0f}% surcharge (net wealth {bdt(low)}–{bdt(high) if high else 'above'})"
                break

    # Special: own >1 car OR property >8000 sq ft AND wealth >4 crore → min 10%
    if (v["owns_multiple_cars"] or v["property_area_sqft"] > 8_000) and net_wealth > 4_00_00_000:
        if surcharge_rate < 0.10:
            surcharge_rate = 0.10
            surcharge_reason = "10% surcharge (multiple cars / large property + wealth >4 crore)"

    surcharge = final_tax_before_surcharge * surcharge_rate

    # ── 17. TOTAL TAX LIABILITY ──────────────────────────────────────────
    total_tax_liability = final_tax_before_surcharge + surcharge

    # ── 18. TDS & ADVANCE TAX ────────────────────────────────────────────
    total_tds = (v["tds_salary"] + v["tds_bank_interest"] + v["tds_savings_cert"]
                 + v["tds_rent"] + v["tds_other"])
    total_credits = total_tds + v["advance_tax_paid"] + v["tax_paid_with_return"]
    tax_payable_or_refund = total_tax_liability - total_credits

    return {
        # Salary
        "gross_salary": gross_salary, "car_perquisite": car_perquisite,
        "accommodation_perquisite": accommodation_perquisite,
        "gross_salary_with_perqs": gross_salary_with_perqs,
        "salary_exemption": salary_exemption, "salary_exemption_limit": salary_exemption_limit,
        "pf_employer_taxable": pf_employer_taxable, "taxable_salary": taxable_salary,
        # House property
        "annual_rent": annual_rent, "taxable_house_property": taxable_house_property,
        "repair_deduction": annual_rent * 0.30 if annual_rent > 0 else 0,
        # Business
        "taxable_business": taxable_business,
        # Agri
        "taxable_agri": taxable_agri,
        # Capital gains
        "cap_gain_normal": cap_gain_normal, "cap_gain_flat15": cap_gain_flat15,
        "tax_cap_gain_flat15": tax_cap_gain_flat15,
        # Other
        "bank_interest": bank_interest, "sanchayapatra_interest": sanchayapatra_interest,
        "dividend_listed_taxable": dividend_listed_taxable,
        "dividend_unlisted": dividend_unlisted, "taxable_other": taxable_other,
        # Totals
        "total_income": total_income, "threshold": threshold,
        "taxable_above_threshold": max(0, total_income - threshold),
        # Slab tax
        "slabs_used": slabs_used, "gross_tax_normal": gross_tax_normal,
        "gross_tax": gross_tax,
        # Rebate
        "total_investment": total_investment, "admissible_investment": admissible_investment,
        "investment_rebate": investment_rebate,
        # Final
        "tax_after_rebate": tax_after_rebate,
        "min_tax_amount": min_tax_amount, "applied_min_tax": applied_min_tax,
        "final_tax_before_surcharge": final_tax_before_surcharge,
        # Surcharge
        "net_wealth": net_wealth, "surcharge_rate": surcharge_rate,
        "surcharge_reason": surcharge_reason, "surcharge": surcharge,
        # Total
        "total_tax_liability": total_tax_liability,
        # Credits
        "total_tds": total_tds, "advance_tax_paid": v["advance_tax_paid"],
        "total_credits": total_credits,
        "tax_payable_or_refund": tax_payable_or_refund,
        # Effective rates
        "effective_rate": total_tax_liability / total_income if total_income > 0 else 0,
        "marginal_rate": slabs_used[-1][2] if slabs_used else 0,
    }

# ── SIDEBAR ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🇧🇩 BD Tax Calculator")
    st.caption("Income Tax Act 2023\nFinance Ordinance 2025")
    st.markdown("---")
    r = compute()
    st.metric("Total Income", bdt(r["total_income"]))
    st.metric("Gross Tax", bdt(r["gross_tax"]))
    st.metric("Investment Rebate", f"– {bdt(r['investment_rebate'])}")
    st.metric("Net Tax Liability", bdt(r["total_tax_liability"]))
    color = "🟢" if r["tax_payable_or_refund"] <= 0 else "🔴"
    label = "Refund Due" if r["tax_payable_or_refund"] < 0 else "Tax Payable"
    st.metric(f"{color} {label}", bdt(abs(r["tax_payable_or_refund"])))
    st.markdown("---")
    if st.button("🔄 Reset to defaults", use_container_width=True):
        reset(); st.rerun()
    st.caption("All amounts in BDT (Bangladeshi Taka)")

# ── MAIN PAGE ──────────────────────────────────────────────────────────────
st.title("🇧🇩 Bangladesh Individual Income Tax Calculator")
st.caption("Income Tax Act 2023 | Finance Ordinance 2025 | NBR Bangladesh")

tabs = st.tabs([
    "🧮 Inputs",
    "📄 Salary Income",
    "🏠 Other Income",
    "📊 Tax Computation",
    "💰 Investment Rebate",
    "💼 Wealth & Surcharge",
    "🗒️ Return Summary",
    "📚 Tax Guide",
])

# ═══════════════════════════════════════════════════════════════════════════
# TAB 0 — INPUTS
# ═══════════════════════════════════════════════════════════════════════════
with tabs[0]:
    st.header("🧮 Taxpayer Inputs")
    st.info("Fill in all applicable fields. Switch to any tab to see the results update instantly. All amounts in BDT.")

    v = st.session_state["bd"]

    with st.expander("👤 Personal Details & Assessment Year", expanded=True):
        c1, c2 = st.columns(2)
        v["taxpayer_name"]    = c1.text_input("Taxpayer Name", v["taxpayer_name"], key="k_name")
        v["tin"]              = c2.text_input("TIN (12-digit)", v["tin"], key="k_tin")
        c1, c2, c3 = st.columns(3)
        v["assessment_year"]  = c1.selectbox("Assessment Year", list(TAX_SLABS.keys()),
                                              index=list(TAX_SLABS.keys()).index(v["assessment_year"]), key="k_ay")
        cats = list(TAX_FREE[v["assessment_year"]].keys())
        if v["taxpayer_category"] not in cats:
            v["taxpayer_category"] = cats[0]
        v["taxpayer_category"] = c2.selectbox("Taxpayer Category", cats,
                                               index=cats.index(v["taxpayer_category"]), key="k_cat")
        v["residential_area"] = c3.selectbox("Residential Area",
                                              list(MIN_TAX[v["assessment_year"]].keys()),
                                              key="k_area")
        c1, c2 = st.columns(2)
        v["resident_status"]  = c1.selectbox("Resident Status",
                                              ["Resident", "Non-Resident Bangladeshi (NRB)", "Non-Resident (Foreign National)"],
                                              key="k_res")
        v["is_new_taxpayer"]  = c2.checkbox("First-time / New Taxpayer", value=v["is_new_taxpayer"], key="k_new")

    with st.expander("💼 Salary & Employment Income", expanded=True):
        st.caption("Enter annual (full-year) amounts in BDT")
        c1, c2, c3 = st.columns(3)
        v["basic_salary"]            = c1.number_input("Basic Salary", value=v["basic_salary"], step=1000.0, min_value=0.0, key="k_bs")
        v["house_rent_allowance"]    = c2.number_input("House Rent Allowance (HRA)", value=v["house_rent_allowance"], step=1000.0, min_value=0.0, key="k_hra")
        v["medical_allowance"]       = c3.number_input("Medical Allowance", value=v["medical_allowance"], step=500.0, min_value=0.0, key="k_med")
        c1, c2, c3 = st.columns(3)
        v["conveyance_allowance"]    = c1.number_input("Conveyance Allowance", value=v["conveyance_allowance"], step=500.0, min_value=0.0, key="k_conv")
        v["festival_bonus"]          = c2.number_input("Festival Bonus", value=v["festival_bonus"], step=1000.0, min_value=0.0, key="k_fest")
        v["performance_bonus"]       = c3.number_input("Performance / Other Bonus", value=v["performance_bonus"], step=1000.0, min_value=0.0, key="k_perf")
        c1, c2, c3 = st.columns(3)
        v["leave_encashment"]        = c1.number_input("Leave Encashment", value=v["leave_encashment"], step=500.0, min_value=0.0, key="k_leave")
        v["employer_pf_contribution"]= c2.number_input("Employer PF Contribution", value=v["employer_pf_contribution"], step=500.0, min_value=0.0, key="k_epf")
        v["employee_pf_contribution"]= c3.number_input("Employee PF Contribution", value=v["employee_pf_contribution"], step=500.0, min_value=0.0, key="k_eepf")
        c1, c2 = st.columns(2)
        v["gratuity_received"]       = c1.number_input("Gratuity Received (from approved fund)", value=v["gratuity_received"], step=1000.0, min_value=0.0, key="k_grat")
        v["other_allowances"]        = c2.number_input("Other Allowances", value=v["other_allowances"], step=500.0, min_value=0.0, key="k_oall")
        st.markdown("**Employer-Provided Benefits (Perquisites)**")
        c1, c2 = st.columns(2)
        v["car_provided_by_employer"]= c1.checkbox("Car provided by employer?", value=v["car_provided_by_employer"], key="k_car")
        if v["car_provided_by_employer"]:
            v["car_cc"] = c2.selectbox("Car engine capacity", ["Up to 2500 cc", "Above 2500 cc"], key="k_carcc")
        v["accommodation_provided"]  = c1.checkbox("Employer-provided accommodation?", value=v["accommodation_provided"], key="k_acc")

    with st.expander("🏠 House Property Income", expanded=False):
        v["has_rental_income"] = st.checkbox("I have rental / house property income", value=v["has_rental_income"], key="k_hasrent")
        if v["has_rental_income"]:
            c1, c2 = st.columns(2)
            v["annual_rent_received"]   = c1.number_input("Annual Rent Received (BDT)", value=v["annual_rent_received"], step=1000.0, min_value=0.0, key="k_rent")
            v["municipal_tax_paid"]     = c2.number_input("Municipal / Union Tax Paid", value=v["municipal_tax_paid"], step=100.0, min_value=0.0, key="k_muni")
            c1, c2 = st.columns(2)
            v["interest_on_home_loan"]  = c1.number_input("Interest on Home Loan (deductible)", value=v["interest_on_home_loan"], step=500.0, min_value=0.0, key="k_homeloan")
            v["vacancy_allowance_pct"]  = c2.number_input("Vacancy Allowance (%)", value=v["vacancy_allowance_pct"], step=1.0, min_value=0.0, max_value=100.0, key="k_vacancy")
            st.caption("Note: 30% of gross rent is automatically allowed as repair & collection charge.")

    with st.expander("🏢 Business / Professional Income", expanded=False):
        v["has_business_income"] = st.checkbox("I have business or professional income", value=v["has_business_income"], key="k_hasbiz")
        if v["has_business_income"]:
            c1, c2 = st.columns(2)
            v["business_profit"]    = c1.number_input("Net Business Profit (BDT)", value=v["business_profit"], step=1000.0, min_value=0.0, key="k_bizprofit")
            v["professional_income"]= c2.number_input("Professional / Freelance Income (BDT)", value=v["professional_income"], step=1000.0, min_value=0.0, key="k_profin")
            st.caption("Enter net profit after allowable business expenses.")

    with st.expander("🌾 Agricultural Income", expanded=False):
        v["has_agri_income"] = st.checkbox("I have agricultural income", value=v["has_agri_income"], key="k_hasagri")
        if v["has_agri_income"]:
            v["agricultural_income"] = st.number_input("Agricultural Income (BDT)", value=v["agricultural_income"], step=1000.0, min_value=0.0, key="k_agri")

    with st.expander("📈 Capital Gains", expanded=False):
        v["has_capital_gains"] = st.checkbox("I have capital gains", value=v["has_capital_gains"], key="k_hascg")
        if v["has_capital_gains"]:
            c1, c2 = st.columns(2)
            v["capital_gain_shares_listed"]    = c1.number_input("Gain from listed shares (flat 15%)", value=v["capital_gain_shares_listed"], step=1000.0, min_value=0.0, key="k_cgl")
            v["capital_gain_shares_unlisted"]  = c2.number_input("Gain from unlisted shares (added to income)", value=v["capital_gain_shares_unlisted"], step=1000.0, min_value=0.0, key="k_cgul")
            c1, c2 = st.columns(2)
            v["capital_gain_property_lt5yr"]   = c1.number_input("Property gain (held ≤5 yrs, added to income)", value=v["capital_gain_property_lt5yr"], step=1000.0, min_value=0.0, key="k_cgp5")
            v["capital_gain_property_gt5yr"]   = c2.number_input("Property gain (held >5 yrs, flat 15%)", value=v["capital_gain_property_gt5yr"], step=1000.0, min_value=0.0, key="k_cgp15")

    with st.expander("💰 Other Income Sources", expanded=False):
        v["has_other_income"] = st.checkbox("I have other income sources", value=v["has_other_income"], key="k_hasother")
        if v["has_other_income"]:
            c1, c2, c3 = st.columns(3)
            v["bank_interest"]       = c1.number_input("Bank / FDR Interest", value=v["bank_interest"], step=500.0, min_value=0.0, key="k_bank")
            v["savings_cert_interest"]= c2.number_input("Sanchayapatra / Savings Cert. Interest", value=v["savings_cert_interest"], step=500.0, min_value=0.0, key="k_sanch")
            v["dividend_listed"]     = c3.number_input("Dividend — Listed Companies", value=v["dividend_listed"], step=500.0, min_value=0.0, key="k_divl")
            c1, c2, c3 = st.columns(3)
            v["dividend_unlisted"]   = c1.number_input("Dividend — Unlisted Companies", value=v["dividend_unlisted"], step=500.0, min_value=0.0, key="k_divul")
            v["foreign_remittance"]  = c2.number_input("Foreign Remittance (exempt if via bank)", value=v["foreign_remittance"], step=1000.0, min_value=0.0, key="k_remit")
            v["other_income"]        = c3.number_input("Other Miscellaneous Income", value=v["other_income"], step=500.0, min_value=0.0, key="k_misc")
            st.caption("Listed dividend: first BDT 25,000 exempt. Foreign remittance via banking channel: fully exempt.")

    with st.expander("📑 Tax Deducted at Source (TDS) & Advance Tax", expanded=False):
        st.caption("Enter amounts already deducted / paid during the income year.")
        c1, c2, c3 = st.columns(3)
        v["tds_salary"]          = c1.number_input("TDS on Salary", value=v["tds_salary"], step=500.0, min_value=0.0, key="k_tdss")
        v["tds_bank_interest"]   = c2.number_input("TDS on Bank Interest", value=v["tds_bank_interest"], step=100.0, min_value=0.0, key="k_tdsb")
        v["tds_savings_cert"]    = c3.number_input("TDS on Sanchayapatra", value=v["tds_savings_cert"], step=100.0, min_value=0.0, key="k_tdssc")
        c1, c2, c3 = st.columns(3)
        v["tds_rent"]            = c1.number_input("TDS on Rent Received", value=v["tds_rent"], step=100.0, min_value=0.0, key="k_tdsr")
        v["tds_other"]           = c2.number_input("TDS — Other", value=v["tds_other"], step=100.0, min_value=0.0, key="k_tdso")
        v["advance_tax_paid"]    = c3.number_input("Advance Tax Paid", value=v["advance_tax_paid"], step=500.0, min_value=0.0, key="k_adv")
        v["tax_paid_with_return"]= st.number_input("Tax Paid with Return (challan)", value=v["tax_paid_with_return"], step=500.0, min_value=0.0, key="k_challan")

    with st.expander("📂 Investment & Rebate Claims (Section 78)", expanded=False):
        st.caption(f"Rebate = 15% of admissible amount. Admissible = min(actual, 25% of total income, BDT 1 crore)")
        c1, c2, c3 = st.columns(3)
        v["inv_life_insurance"]         = c1.number_input("Life Insurance Premium", value=v["inv_life_insurance"], step=500.0, min_value=0.0, key="k_li")
        v["inv_pf_employee"]            = c2.number_input("Employee PF Contribution", value=v["inv_pf_employee"], step=500.0, min_value=0.0, key="k_pfe")
        v["inv_dps"]                    = c3.number_input("DPS (max BDT 60,000/yr)", value=v["inv_dps"], step=500.0, min_value=0.0, max_value=60_000.0, key="k_dps")
        c1, c2, c3 = st.columns(3)
        v["inv_sanchayapatra"]          = c1.number_input("Sanchayapatra / Savings Certs.", value=v["inv_sanchayapatra"], step=1000.0, min_value=0.0, key="k_sp")
        v["inv_govt_securities"]        = c2.number_input("Government Securities / T-Bills", value=v["inv_govt_securities"], step=1000.0, min_value=0.0, key="k_gs")
        v["inv_listed_shares_mf"]       = c3.number_input("Listed Shares / Mutual Funds", value=v["inv_listed_shares_mf"], step=1000.0, min_value=0.0, key="k_mf")
        c1, c2, c3 = st.columns(3)
        v["inv_approved_debentures"]    = c1.number_input("Approved Debentures / Bonds", value=v["inv_approved_debentures"], step=1000.0, min_value=0.0, key="k_deb")
        v["inv_housing_loan_principal"] = c2.number_input("Housing Loan Principal Repayment", value=v["inv_housing_loan_principal"], step=1000.0, min_value=0.0, key="k_hlp")
        v["inv_zakat"]                  = c3.number_input("Zakat to approved fund", value=v["inv_zakat"], step=500.0, min_value=0.0, key="k_zak")
        c1, c2 = st.columns(2)
        v["inv_donation_approved"]      = c1.number_input("Donation to approved institutions", value=v["inv_donation_approved"], step=500.0, min_value=0.0, key="k_don")
        v["inv_other"]                  = c2.number_input("Other approved investments", value=v["inv_other"], step=500.0, min_value=0.0, key="k_invo")

    with st.expander("🏦 Net Wealth Statement (for Surcharge)", expanded=False):
        st.caption("Required to determine surcharge liability. Surcharge applies if net wealth > BDT 4 crore.")
        c1, c2, c3 = st.columns(3)
        v["wealth_cash_bank"]      = c1.number_input("Cash & Bank Balance", value=v["wealth_cash_bank"], step=10000.0, min_value=0.0, key="k_wc")
        v["wealth_investments"]    = c2.number_input("Shares & Investments", value=v["wealth_investments"], step=10000.0, min_value=0.0, key="k_wi")
        v["wealth_sanchayapatra"]  = c3.number_input("Sanchayapatra balance", value=v["wealth_sanchayapatra"], step=10000.0, min_value=0.0, key="k_ws")
        c1, c2, c3 = st.columns(3)
        v["wealth_loans_receivable"]= c1.number_input("Loans / Advances Receivable", value=v["wealth_loans_receivable"], step=10000.0, min_value=0.0, key="k_wl")
        v["wealth_land_building"]  = c2.number_input("Land & Buildings", value=v["wealth_land_building"], step=50000.0, min_value=0.0, key="k_wlb")
        v["wealth_vehicles"]       = c3.number_input("Motor Vehicles", value=v["wealth_vehicles"], step=10000.0, min_value=0.0, key="k_wv")
        c1, c2, c3 = st.columns(3)
        v["wealth_business_capital"]= c1.number_input("Business Capital", value=v["wealth_business_capital"], step=10000.0, min_value=0.0, key="k_wbc")
        v["wealth_jewellery"]      = c2.number_input("Jewellery & Gold", value=v["wealth_jewellery"], step=5000.0, min_value=0.0, key="k_wj")
        v["wealth_furniture"]      = c3.number_input("Furniture & Electronics", value=v["wealth_furniture"], step=5000.0, min_value=0.0, key="k_wf")
        c1, c2 = st.columns(2)
        v["wealth_other_assets"]   = c1.number_input("Other Assets", value=v["wealth_other_assets"], step=5000.0, min_value=0.0, key="k_woa")
        v["wealth_liabilities"]    = c2.number_input("Total Liabilities", value=v["wealth_liabilities"], step=10000.0, min_value=0.0, key="k_wlia")
        c1, c2 = st.columns(2)
        v["owns_multiple_cars"]    = c1.checkbox("Own more than 1 motor car?", value=v["owns_multiple_cars"], key="k_wmc")
        v["property_area_sqft"]    = c2.number_input("Total property area (sq ft, if applicable)", value=v["property_area_sqft"], step=100.0, min_value=0.0, key="k_sqft")

    st.success("✅ All inputs saved. Switch to any tab to see your tax computation.")

# ── COMPUTE RESULTS ────────────────────────────────────────────────────────
r = compute()
v = st.session_state["bd"]
ay = v["assessment_year"]

# ═══════════════════════════════════════════════════════════════════════════
# TAB 1 — SALARY INCOME
# ═══════════════════════════════════════════════════════════════════════════
with tabs[1]:
    st.header("📄 Computation of Salary Income")
    st.caption(f"Assessment Year: {ay}  |  Taxpayer: {V('taxpayer_name')}")

    data = [
        ("GROSS SALARY COMPONENTS", None, "header"),
        ("Basic Salary", v["basic_salary"]),
        ("House Rent Allowance (HRA)", v["house_rent_allowance"]),
        ("Medical Allowance", v["medical_allowance"]),
        ("Conveyance Allowance", v["conveyance_allowance"]),
        ("Festival Bonus", v["festival_bonus"]),
        ("Performance / Other Bonus", v["performance_bonus"]),
        ("Leave Encashment", v["leave_encashment"]),
        ("Employer PF Contribution (gross)", v["employer_pf_contribution"]),
        ("Other Allowances", v["other_allowances"]),
        ("Total Gross Salary", r["gross_salary"], "subtotal"),
        ("", None),
        ("ADD: PERQUISITES", None, "header"),
        ("Car perquisite (employer-provided car)", r["car_perquisite"]),
        ("Accommodation perquisite (25% of basic)", r["accommodation_perquisite"]),
        ("Gross Salary incl. Perquisites", r["gross_salary_with_perqs"], "subtotal"),
        ("", None),
        ("LESS: EXEMPTIONS", None, "header"),
        (f"Salary exemption [1/3 of salary or BDT {r['salary_exemption_limit']:,.0f}, lower]", -r["salary_exemption"]),
        ("Employee PF contribution (deductible)", -v["employee_pf_contribution"]),
        (f"Employer PF — exempt portion (lower of 1/3 basic or BDT 1,50,000)", -(v["employer_pf_contribution"] - r["pf_employer_taxable"])),
        ("Gratuity (from approved fund — fully exempt)", -v["gratuity_received"]),
        ("", None),
        ("TAXABLE SALARY INCOME", r["taxable_salary"], "total"),
    ]

    for row in data:
        if len(row) == 2:
            label, val = row
            style = "line"
        else:
            label, val, style = row

        if style == "header":
            st.markdown(f"**{label}**")
            continue
        if not label:
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            continue

        c1, c2 = st.columns([5, 2])
        if style == "subtotal":
            c1.markdown(f"**{label}**")
            c2.markdown(f"**{bdt(val)}**")
            st.markdown("<hr style='margin:2px 0'>", unsafe_allow_html=True)
        elif style == "total":
            c1.markdown(f"### {label}")
            c2.markdown(f"### {bdt(val)}")
            st.markdown("<hr style='border-top:3px double #333;margin:4px 0'>", unsafe_allow_html=True)
        else:
            c1.markdown(f"&nbsp;&nbsp;&nbsp;{label}", unsafe_allow_html=True)
            c2.markdown(bdt(val) if val is not None else "")

    st.info(
        f"**Exemption Rule (Section 76):** The lower of (a) one-third of total employment income "
        f"= {bdt(r['gross_salary_with_perqs']/3)} or (b) BDT {r['salary_exemption_limit']:,.0f} "
        f"= **{bdt(r['salary_exemption'])}** is exempt."
    )

# ═══════════════════════════════════════════════════════════════════════════
# TAB 2 — OTHER INCOME
# ═══════════════════════════════════════════════════════════════════════════
with tabs[2]:
    st.header("🏠 Other Income Heads")
    st.caption(f"Assessment Year: {ay}")

    st.subheader("House Property Income")
    if r["annual_rent"] > 0:
        hp_rows = [
            ("Gross Annual Rent Received", r["annual_rent"]),
            ("Less: Repair & Collection (30% of rent)", -r["repair_deduction"]),
            ("Less: Municipal / Union Tax", -v["municipal_tax_paid"]),
            ("Less: Interest on Home Loan", -v["interest_on_home_loan"]),
            ("Net Rent (before vacancy)", r["annual_rent"] - r["repair_deduction"] - v["municipal_tax_paid"] - v["interest_on_home_loan"]),
            ("Less: Vacancy Allowance", -(r["annual_rent"] - r["repair_deduction"] - v["municipal_tax_paid"] - v["interest_on_home_loan"]) * (v["vacancy_allowance_pct"]/100)),
        ]
        for label, val in hp_rows:
            c1, c2 = st.columns([5, 2])
            c1.markdown(f"&nbsp;&nbsp;&nbsp;{label}", unsafe_allow_html=True)
            c2.markdown(bdt(val))
        st.markdown(f"**Taxable House Property Income: {bdt(r['taxable_house_property'])}**")
    else:
        st.info("No rental income entered. Toggle 'I have rental income' in Inputs tab.")

    st.markdown("---")
    st.subheader("Business / Professional Income")
    if v["has_business_income"]:
        c1, c2 = st.columns([5, 2])
        c1.markdown("Net Business Profit")
        c2.markdown(bdt(v["business_profit"]))
        c1, c2 = st.columns([5, 2])
        c1.markdown("Professional / Freelance Income")
        c2.markdown(bdt(v["professional_income"]))
        st.markdown(f"**Taxable Business / Professional Income: {bdt(r['taxable_business'])}**")
    else:
        st.info("No business income entered.")

    st.markdown("---")
    st.subheader("Capital Gains")
    if v["has_capital_gains"]:
        cg_df = pd.DataFrame({
            "Type": [
                "Listed shares (flat 15% final tax)",
                "Unlisted shares (added to total income)",
                "Property sold — held ≤5 years (added to income)",
                "Property sold — held >5 years (flat 15%)",
                "TOTAL CAPITAL GAINS",
            ],
            "Amount (BDT)": [
                v["capital_gain_shares_listed"], v["capital_gain_shares_unlisted"],
                v["capital_gain_property_lt5yr"], v["capital_gain_property_gt5yr"],
                v["capital_gain_shares_listed"] + v["capital_gain_shares_unlisted"] + v["capital_gain_property_lt5yr"] + v["capital_gain_property_gt5yr"],
            ],
            "Treatment": [
                "Final withholding @ 15%", "Progressive slabs", "Progressive slabs", "Flat 15%", "",
            ],
        })
        st.dataframe(cg_df, hide_index=True, use_container_width=True)
    else:
        st.info("No capital gains entered.")

    st.markdown("---")
    st.subheader("Other Income Sources")
    if v["has_other_income"]:
        other_df = pd.DataFrame({
            "Income Source": [
                "Bank / FDR Interest", "Sanchayapatra / Savings Certificate Interest",
                "Dividend — Listed Companies (gross)", "Dividend exemption (first BDT 25,000)",
                "Dividend — Listed (taxable net)", "Dividend — Unlisted Companies",
                "Foreign Remittance (exempt via banking channel)",
                "Other Miscellaneous Income", "Total Other Income",
            ],
            "Amount (BDT)": [
                v["bank_interest"], v["savings_cert_interest"],
                v["dividend_listed"], -min(25_000, v["dividend_listed"]),
                r["dividend_listed_taxable"], v["dividend_unlisted"],
                v["foreign_remittance"],
                v["other_income"], r["taxable_other"],
            ],
        })
        st.dataframe(other_df, hide_index=True, use_container_width=True)
    else:
        st.info("No other income entered.")

    st.markdown("---")
    st.subheader("Summary of All Income Heads")
    summary_df = pd.DataFrame({
        "Head of Income": [
            "Salary & Employment", "House Property", "Business / Professional",
            "Agricultural", "Capital Gains (normal slab)", "Other Sources", "TOTAL INCOME",
        ],
        "Taxable Amount (BDT)": [
            r["taxable_salary"], r["taxable_house_property"], r["taxable_business"],
            r["taxable_agri"], r["cap_gain_normal"], r["taxable_other"], r["total_income"],
        ],
    })
    st.dataframe(summary_df, hide_index=True, use_container_width=True)
    if r["cap_gain_flat15"] > 0:
        st.caption(f"+ Capital Gains taxed at flat 15%: {bdt(r['cap_gain_flat15'])} → Tax: {bdt(r['tax_cap_gain_flat15'])}")

# ═══════════════════════════════════════════════════════════════════════════
# TAB 3 — TAX COMPUTATION
# ═══════════════════════════════════════════════════════════════════════════
with tabs[3]:
    st.header("📊 Tax Computation — Slab-wise")
    st.caption(f"{ay}  |  {V('taxpayer_category')}  |  Threshold: {bdt(r['threshold'])}")

    # KPI row
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Income", bdt(r["total_income"]))
    c2.metric("Tax-Free Threshold", bdt(r["threshold"]))
    c3.metric("Taxable Above Threshold", bdt(r["taxable_above_threshold"]))
    c4.metric("Effective Tax Rate", f"{r['effective_rate']*100:.2f}%")

    st.markdown("---")
    st.subheader("Step 1 — Tax-free Income Threshold")
    threshold_df = pd.DataFrame({
        "Category": [v["taxpayer_category"]],
        "Tax-Free Limit (BDT)": [r["threshold"]],
        "Assessment Year": [ay],
    })
    st.dataframe(threshold_df, hide_index=True, use_container_width=True)

    st.subheader("Step 2 — Slab-wise Tax on Normal Income")
    if r["slabs_used"]:
        slab_df = pd.DataFrame(r["slabs_used"], columns=["Income Slab", "Amount (BDT)", "Rate", "Tax (BDT)"])
        slab_df["Rate"] = slab_df["Rate"].apply(lambda x: f"{x*100:.0f}%")
        slab_df["Amount (BDT)"] = slab_df["Amount (BDT)"].apply(lambda x: f"{x:,.0f}")
        slab_df["Tax (BDT)"] = slab_df["Tax (BDT)"].apply(lambda x: f"{x:,.0f}")
        st.dataframe(slab_df, hide_index=True, use_container_width=True)

        c1, c2 = st.columns([5, 2])
        c1.markdown(f"**Plus: Tax on income exceeding threshold (nil band) = {bdt(r['threshold'])}**")
        c1.markdown(f"**Tax on normal income (progressive slabs)**")
        c2.markdown(f"**{bdt(r['gross_tax_normal'])}**")

    if r["cap_gain_flat15"] > 0:
        st.subheader("Step 2b — Flat 15% Tax on Certain Capital Gains")
        c1, c2 = st.columns([5, 2])
        c1.markdown(f"Capital gains @ flat 15%: {bdt(r['cap_gain_flat15'])}")
        c2.markdown(bdt(r["tax_cap_gain_flat15"]))

    st.subheader("Step 3 — Gross Tax Before Rebate")
    c1, c2 = st.columns([5, 2])
    c1.markdown("### Gross Tax")
    c2.markdown(f"### {bdt(r['gross_tax'])}")

    st.markdown("---")
    st.subheader("Step 4 — Investment Rebate (Section 78)")
    c1, c2 = st.columns([5, 2])
    c1.markdown(f"&nbsp;&nbsp;&nbsp;Total eligible investments: {bdt(r['total_investment'])}", unsafe_allow_html=True)
    c1.markdown(f"&nbsp;&nbsp;&nbsp;25% of total income: {bdt(r['total_income'] * 0.25)}", unsafe_allow_html=True)
    c1.markdown(f"&nbsp;&nbsp;&nbsp;Cap: BDT 1,00,00,000", unsafe_allow_html=True)
    c1.markdown(f"**Admissible investment (lower of above three)**")
    c2.markdown(f"**{bdt(r['admissible_investment'])}**")
    c1, c2 = st.columns([5, 2])
    c1.markdown(f"**Investment Rebate @ 15%**")
    c2.markdown(f"**– {bdt(r['investment_rebate'])}**")
    st.markdown("<hr style='margin:2px 0'>", unsafe_allow_html=True)

    c1, c2 = st.columns([5, 2])
    c1.markdown("**Tax after Investment Rebate**")
    c2.markdown(f"**{bdt(r['tax_after_rebate'])}**")

    st.markdown("---")
    st.subheader("Step 5 — Minimum Tax")
    c1, c2 = st.columns([5, 2])
    c1.markdown(f"Minimum tax ({v['residential_area']}): {bdt(r['min_tax_amount'])}")
    c1.markdown(f"Tax after rebate: {bdt(r['tax_after_rebate'])}")
    if r["applied_min_tax"]:
        st.warning(f"⚠️ Minimum tax of {bdt(r['min_tax_amount'])} is higher than slab tax after rebate. Minimum tax applies.")
    else:
        st.success(f"✅ Slab tax {bdt(r['tax_after_rebate'])} ≥ minimum tax {bdt(r['min_tax_amount'])}. Slab tax applies.")
    c1, c2 = st.columns([5, 2])
    c1.markdown("### Tax Before Surcharge")
    c2.markdown(f"### {bdt(r['final_tax_before_surcharge'])}")

    st.markdown("---")
    st.subheader("Step 6 — Surcharge")
    if r["surcharge"] > 0:
        st.warning(f"Surcharge applies: {r['surcharge_reason']}")
        c1, c2 = st.columns([5, 2])
        c1.markdown(f"Net Wealth: {bdt(r['net_wealth'])}")
        c1.markdown(f"Surcharge Rate: {r['surcharge_rate']*100:.0f}%")
        c2.markdown(f"+ {bdt(r['surcharge'])}")
    else:
        st.success(f"✅ {r['surcharge_reason']}")

    st.markdown("---")
    st.subheader("TOTAL TAX LIABILITY")
    c1, c2 = st.columns([5, 2])
    c1.markdown(f"### 🏛️ Total Tax Payable")
    c2.markdown(f"### {bdt(r['total_tax_liability'])}")
    st.markdown("<hr style='border-top:3px double #333'>", unsafe_allow_html=True)

    c1, c2 = st.columns([5, 2])
    c1.markdown(f"Marginal Tax Rate")
    c2.markdown(f"{r['marginal_rate']*100:.0f}%")
    c1, c2 = st.columns([5, 2])
    c1.markdown(f"Effective Tax Rate")
    c2.markdown(f"{r['effective_rate']*100:.2f}%")

# ═══════════════════════════════════════════════════════════════════════════
# TAB 4 — INVESTMENT REBATE
# ═══════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.header("💰 Investment Rebate — Section 78")
    st.caption("Tax rebate on investment in approved instruments / expenditure")

    st.info(
        "**How it works:** Resident and Non-Resident Bangladeshi taxpayers can claim a rebate "
        "equal to **15%** of the 'admissible amount'. The admissible amount is the **lowest** of: "
        "(a) actual eligible investment, (b) 25% of total income, (c) BDT 1,00,00,000 (1 crore)."
    )

    inv_df = pd.DataFrame({
        "Approved Investment / Expenditure": [
            "Life insurance premium",
            "Employee contribution to Recognised Provident Fund (RPF)",
            "Deposit Pension Scheme — DPS (capped BDT 60,000/yr)",
            "Sanchayapatra / National Savings Certificates",
            "Government Securities / Treasury Bills",
            "Listed shares / Mutual Funds / ETFs",
            "Approved debentures / bonds",
            "Housing loan principal repayment",
            "Zakat to approved fund",
            "Donation to approved charitable institutions",
            "Other approved investments",
            "TOTAL ACTUAL INVESTMENT",
        ],
        "Amount (BDT)": [
            v["inv_life_insurance"], v["inv_pf_employee"], min(v["inv_dps"], 60_000),
            v["inv_sanchayapatra"], v["inv_govt_securities"], v["inv_listed_shares_mf"],
            v["inv_approved_debentures"], v["inv_housing_loan_principal"],
            v["inv_zakat"], v["inv_donation_approved"], v["inv_other"],
            r["total_investment"],
        ],
    })
    st.dataframe(inv_df, hide_index=True, use_container_width=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("(a) Actual eligible investment", bdt(r["total_investment"]))
    c2.metric("(b) 25% of total income", bdt(r["total_income"] * 0.25))
    c3.metric("(c) Maximum cap", bdt(10_000_000))

    st.markdown(f"**Admissible Amount = Lower of (a), (b), (c) = {bdt(r['admissible_investment'])}**")
    st.markdown(f"**Investment Rebate = 15% × {bdt(r['admissible_investment'])} = {bdt(r['investment_rebate'])}**")

    if r["total_investment"] > r["admissible_investment"]:
        unused = r["total_investment"] - r["admissible_investment"]
        st.warning(f"Note: BDT {unused:,.0f} of your investments could not be claimed this year due to the 25%-of-income cap or BDT 1-crore ceiling.")

# ═══════════════════════════════════════════════════════════════════════════
# TAB 5 — WEALTH & SURCHARGE
# ═══════════════════════════════════════════════════════════════════════════
with tabs[5]:
    st.header("💼 Net Wealth Statement & Surcharge Computation")

    wealth_df = pd.DataFrame({
        "Asset / Liability": [
            "Cash & Bank Balances", "Shares & Investments", "Sanchayapatra Balance",
            "Loans & Advances Receivable", "Land & Buildings",
            "Motor Vehicles", "Business Capital", "Jewellery & Gold",
            "Furniture & Electronics", "Other Assets",
            "TOTAL GROSS ASSETS", "Less: Total Liabilities", "NET WEALTH",
        ],
        "Amount (BDT)": [
            v["wealth_cash_bank"], v["wealth_investments"], v["wealth_sanchayapatra"],
            v["wealth_loans_receivable"], v["wealth_land_building"],
            v["wealth_vehicles"], v["wealth_business_capital"], v["wealth_jewellery"],
            v["wealth_furniture"], v["wealth_other_assets"],
            sum([v["wealth_cash_bank"], v["wealth_investments"], v["wealth_sanchayapatra"],
                 v["wealth_loans_receivable"], v["wealth_land_building"],
                 v["wealth_vehicles"], v["wealth_business_capital"], v["wealth_jewellery"],
                 v["wealth_furniture"], v["wealth_other_assets"]]),
            -v["wealth_liabilities"], r["net_wealth"],
        ],
    })
    st.dataframe(wealth_df, hide_index=True, use_container_width=True)

    st.markdown("---")
    st.subheader("Surcharge Rates (on regular income tax)")
    sc_df = pd.DataFrame({
        "Net Wealth Range": [
            "Up to BDT 4 crore", "BDT 4–10 crore", "BDT 10–20 crore",
            "BDT 20–50 crore", "Above BDT 50 crore",
        ],
        "Surcharge Rate": ["Nil", "10%", "20%", "25%", "30%"],
    })
    st.dataframe(sc_df, hide_index=True, use_container_width=True)

    st.caption("Special rule: Minimum 10% surcharge if net wealth >BDT 4 crore AND taxpayer owns more than 1 car OR property >8,000 sq ft.")

    if r["surcharge"] > 0:
        st.error(f"🔴 Surcharge Applicable: {r['surcharge_reason']}")
        c1, c2 = st.columns(2)
        c1.metric("Net Wealth", bdt(r["net_wealth"]))
        c2.metric("Surcharge", bdt(r["surcharge"]))
    else:
        st.success(f"✅ No surcharge. Net wealth: {bdt(r['net_wealth'])} (below BDT 4 crore threshold).")

# ═══════════════════════════════════════════════════════════════════════════
# TAB 6 — RETURN SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
with tabs[6]:
    st.header("🗒️ Income Tax Return Summary")
    st.caption(f"Taxpayer: {V('taxpayer_name')}  |  TIN: {V('tin')}  |  {ay}")

    st.subheader("A. Income Summary")
    ret_income_df = pd.DataFrame({
        "Head of Income": [
            "1. Salary & Employment Income",
            "2. House / Property Income",
            "3. Business / Professional Income",
            "4. Agricultural Income",
            "5. Capital Gains (normal slab)",
            "6. Other Sources",
            "TOTAL INCOME",
        ],
        "Amount (BDT)": [
            r["taxable_salary"], r["taxable_house_property"],
            r["taxable_business"], r["taxable_agri"],
            r["cap_gain_normal"], r["taxable_other"], r["total_income"],
        ],
    })
    st.dataframe(ret_income_df, hide_index=True, use_container_width=True)

    st.subheader("B. Tax Computation Summary")
    ret_tax_df = pd.DataFrame({
        "Item": [
            "Gross Tax (slab-wise on normal income)",
            "Tax on flat-rate capital gains (@15%)",
            "Total Gross Tax",
            "Less: Investment Rebate (Section 78)",
            "Tax After Rebate",
            "Minimum Tax (applicable)",
            "Tax Before Surcharge (higher of above two)",
            "Add: Surcharge",
            "TOTAL TAX LIABILITY",
        ],
        "Amount (BDT)": [
            r["gross_tax_normal"], r["tax_cap_gain_flat15"], r["gross_tax"],
            -r["investment_rebate"], r["tax_after_rebate"],
            r["min_tax_amount"], r["final_tax_before_surcharge"],
            r["surcharge"], r["total_tax_liability"],
        ],
    })
    st.dataframe(ret_tax_df, hide_index=True, use_container_width=True)

    st.subheader("C. TDS & Tax Credit Reconciliation")
    ret_tds_df = pd.DataFrame({
        "Tax Credit Item": [
            "TDS on Salary (by employer)",
            "TDS on Bank / FDR Interest",
            "TDS on Sanchayapatra",
            "TDS on Rent",
            "TDS — Other",
            "Advance Tax Paid",
            "Tax Paid with Return (challan)",
            "TOTAL TAX CREDITS",
        ],
        "Amount (BDT)": [
            v["tds_salary"], v["tds_bank_interest"], v["tds_savings_cert"],
            v["tds_rent"], v["tds_other"], v["advance_tax_paid"],
            v["tax_paid_with_return"], r["total_credits"],
        ],
    })
    st.dataframe(ret_tds_df, hide_index=True, use_container_width=True)

    st.markdown("---")
    if r["tax_payable_or_refund"] > 0:
        st.error(f"### 🔴 Net Tax Payable with Return: {bdt(r['tax_payable_or_refund'])}")
    elif r["tax_payable_or_refund"] < 0:
        st.success(f"### 🟢 Refund Due: {bdt(abs(r['tax_payable_or_refund']))}")
    else:
        st.success("### ✅ No tax payable or refundable (fully settled via TDS / advance tax)")

    st.subheader("D. Investment Details")
    st.markdown(f"- Total eligible investments: **{bdt(r['total_investment'])}**")
    st.markdown(f"- Admissible amount: **{bdt(r['admissible_investment'])}**")
    st.markdown(f"- Tax rebate claimed: **{bdt(r['investment_rebate'])}**")

    st.subheader("E. Net Wealth")
    st.markdown(f"- Net wealth as at year-end: **{bdt(r['net_wealth'])}**")
    st.markdown(f"- Surcharge: **{bdt(r['surcharge'])}** ({r['surcharge_reason']})")

    st.subheader("F. Key Compliance Notes")
    st.markdown(
        "- **Tax Day:** 30 November of the assessment year (extendable by up to 2 months).\n"
        "- **PSR (Proof of Submission of Return):** Required for credit card, savings certificates "
        "> BDT 5,00,000, trade licence, etc. (Section 264, ITA 2023).\n"
        "- **Late filing penalty:** 2% per month on outstanding tax (Section 174).\n"
        "- **Advance tax:** Required if estimated liability > BDT 10,000 (Section 145).\n"
        "- **Withholding by employer:** Employer must deduct TDS monthly on estimated annual salary tax.\n"
        "- **Late payment interest:** 2% per month on unpaid tax after Tax Day.\n"
        "- **E-filing:** Available via NBR's eTaxNBR portal (etaxnbr.gov.bd)."
    )

# ═══════════════════════════════════════════════════════════════════════════
# TAB 7 — TAX GUIDE
# ═══════════════════════════════════════════════════════════════════════════
with tabs[7]:
    st.header("📚 Bangladesh Income Tax — Quick Reference Guide")
    st.caption("Income Tax Act 2023 | Finance Ordinance 2025 | NBR Bangladesh")

    st.subheader("1. Tax Slabs — All Assessment Years")
    for ay_label, slabs in TAX_SLABS.items():
        with st.expander(f"📅 {ay_label}", expanded=(ay_label == ay)):
            slab_rows = []
            cumulative = 0
            for i, (band, rate) in enumerate(slabs):
                if i == 0:
                    slab_rows.append((f"First {bdt(band)}", f"{rate*100:.0f}%"))
                    cumulative += band
                elif band is None:
                    slab_rows.append((f"Above {bdt(cumulative)} (remaining)", f"{rate*100:.0f}%"))
                else:
                    slab_rows.append((f"Next {bdt(band)}", f"{rate*100:.0f}%"))
                    cumulative += band
            st.dataframe(pd.DataFrame(slab_rows, columns=["Income Range", "Rate"]),
                         hide_index=True, use_container_width=True)
            thresh = TAX_FREE[ay_label]
            st.caption("Tax-free thresholds: " + " | ".join([f"{k}: {bdt(v)}" for k, v in thresh.items()]))

    st.subheader("2. Tax-Free Thresholds by Category")
    thresh_data = []
    for ay_label, cats in TAX_FREE.items():
        for cat, amt in cats.items():
            thresh_data.append({"AY": ay_label, "Category": cat, "Threshold (BDT)": f"{amt:,.0f}"})
    st.dataframe(pd.DataFrame(thresh_data), hide_index=True, use_container_width=True)

    st.subheader("3. Key Exemptions (Section 76)")
    st.markdown(
        "| Item | Exemption |\n"
        "|---|---|\n"
        "| Salary exemption | Lower of 1/3 of salary or BDT 5,00,000 |\n"
        "| Gratuity (approved fund) | Fully exempt |\n"
        "| Employee PF contribution | Fully deductible from salary |\n"
        "| Employer PF — excess over 1/3 basic or BDT 1,50,000 | Taxable |\n"
        "| Dividend from listed companies | First BDT 25,000 exempt |\n"
        "| Foreign remittance (via banking channel) | Fully exempt |\n"
        "| Govt. pension / superannuation fund | Up to BDT 2.5 crore exempt |\n"
        "| Gifts from spouse, parents, children | Exempt |\n"
        "| PF/RPF interest | Exempt if ≤ lower of BDT 1,50,000 or 1/3 of salary |\n"
    )

    st.subheader("4. Investment Rebate (Section 78)")
    st.markdown(
        "- **Rate:** 15% of admissible amount\n"
        "- **Admissible:** Minimum of (a) actual investment, (b) 25% of total income, (c) BDT 1 crore\n"
        "- **Eligible instruments:** Life insurance, PF, DPS (max BDT 60k), Sanchayapatra, "
        "listed shares/MFs, govt. securities, approved debentures, housing loan principal, zakat, "
        "approved donations\n"
        "- **Who can claim:** Resident individuals and Non-Resident Bangladeshis\n"
        "- **Filing condition:** Rebate not available if return filed after Tax Day (Finance Ordinance 2025 "
        "relaxed this for some items)"
    )

    st.subheader("5. Capital Gains")
    st.markdown(
        "| Asset | Holding Period | Tax Treatment |\n"
        "|---|---|---|\n"
        "| Listed shares | Any | Flat 15% (final withholding) |\n"
        "| Unlisted shares | Any | Added to income, progressive slab |\n"
        "| Immovable property | ≤ 5 years | Added to income, progressive slab |\n"
        "| Immovable property | > 5 years | Flat 15% |\n"
        "| Property in Dhaka/Chattogram/Gazipur | — | 4% of deed value or per sq-m rate |\n"
        "| Property in other city corps | — | 3% of deed value |\n"
        "| Property — other areas | — | 2% of deed value |\n"
    )

    st.subheader("6. Minimum Tax")
    st.markdown("Applies when income exceeds tax-free threshold but slab tax (after rebate) is below minimum:")
    for ay_label, areas in MIN_TAX.items():
        st.markdown(f"**{ay_label}:** " + " | ".join([f"{a}: {bdt(m)}" for a, m in areas.items()]))
    st.markdown("From AY 2026-27: **flat BDT 5,000** for all areas. New taxpayer: BDT 1,000.")

    st.subheader("7. Surcharge on Net Wealth")
    st.markdown(
        "| Net Wealth | Surcharge on Tax |\n"
        "|---|---|\n"
        "| Up to BDT 4 crore | Nil |\n"
        "| BDT 4–10 crore | 10% |\n"
        "| BDT 10–20 crore | 20% |\n"
        "| BDT 20–50 crore | 25% |\n"
        "| Above BDT 50 crore | 30% |\n"
        "\n**Special:** Minimum 10% surcharge if net wealth > BDT 4 crore AND own >1 car OR property >8,000 sq ft."
    )

    st.subheader("8. Non-Residents")
    st.markdown(
        "- **Non-Resident Bangladeshis (NRB):** Same slab rates as residents. Foreign income exempt. "
        "Bangladesh-source income taxed at normal progressive rates.\n"
        "- **Non-Resident Foreign Nationals:** Flat **30%** on all Bangladesh-source income. "
        "No slab benefits or personal exemptions."
    )

    st.subheader("9. Key Compliance Dates & Penalties")
    st.markdown(
        "| Item | Provision |\n"
        "|---|---|\n"
        "| Tax Day (due date) | 30 November of the Assessment Year |\n"
        "| Extension possible | Up to 2 months (max 31 January) |\n"
        "| Late filing penalty | 2% per month of outstanding tax |\n"
        "| Late payment interest | 2% per month |\n"
        "| Advance tax required if | Estimated liability > BDT 10,000 |\n"
        "| e-Filing portal | etaxnbr.gov.bd |\n"
        "| NBR helpline | 16555 |\n"
    )

    st.subheader("10. PSR — Proof of Submission of Return (Section 264)")
    st.markdown(
        "PSR is mandatory when:\n"
        "- Applying for a credit card\n"
        "- Opening/operating a post office savings account > BDT 5,00,000\n"
        "- Purchasing savings certificates > BDT 5,00,000\n"
        "- Obtaining / renewing a trade licence\n"
        "- Registering / transferring immovable property (above certain values)\n"
        "- Importing goods (in many categories)\n"
        "- Membership of a professional body\n"
        "- Many government tenders and contracts"
    )

    st.info("**Disclaimer:** This calculator is for educational and planning purposes only. "
            "Tax laws change frequently. Always consult a qualified tax professional or "
            "the National Board of Revenue (NBR) website (nbr.gov.bd) for official guidance.")

# ── FOOTER ─────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "🇧🇩 Bangladesh Individual Income Tax Calculator | Income Tax Act 2023 | "
    "Finance Ordinance 2025 | All amounts in BDT | "
    "For official rules visit: nbr.gov.bd | e-Filing: etaxnbr.gov.bd"
)