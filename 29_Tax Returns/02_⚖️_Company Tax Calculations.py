"""
Bangladesh Company Income Tax Calculator
=========================================
Income Tax Act 2023 | Finance Ordinance 2025 | NBR Bangladesh
Assessment Years: AY 2024-25, AY 2025-26, AY 2026-27, AY 2027-28

TABS
----
  🧮 Inputs              — Company identity, income heads, expenses, adjustments
  📄 Profit & Loss       — Accounting profit → Statutory taxable income computation
  🔧 Tax Adjustments     — Add-backs, disallowances, allowable deductions, depreciation
  📊 Tax Computation     — Corporate tax rate, minimum tax (gross receipts), three-way test
  💸 Withholding & TDS   — TDS deducted at source, advance tax, final tax reconciliation
  🏭 Special Incentives  — Tax holidays, reduced rates, SEZ, export, IT/startup exemptions
  🗒️ Return Summary      — Complete return-ready computation with challan reconciliation
  📚 Corporate Tax Guide — Key provisions reference under ITA 2023

HOW TO RUN
----------
    pip install streamlit pandas
    streamlit run bd_company_tax_calculator.py
"""

import streamlit as st
import pandas as pd

BDT = "৳"

# ═══════════════════════════════════════════════════════════════════════════
# TAX RATE TABLES  (Finance Ordinance 2025 / ITA 2023)
# ═══════════════════════════════════════════════════════════════════════════

# Standard corporate tax rates by entity type and AY
# (normal_rate, reduced_rate_if_banking_conditions_met, reduced_rate_label)
CORP_RATES = {
    "Publicly Listed Company (IPO > 10% paid-up)": {
        "AY 2024-25": (22.5, 20.0,  "20% (if banking conditions met)"),
        "AY 2025-26": (22.5, 20.0,  "20% (if banking conditions met)"),
        "AY 2026-27": (25.0, 22.5,  "22.5% (if banking conditions met)"),
        "AY 2027-28": (25.0, 22.5,  "22.5% (if banking conditions met)"),
    },
    "Publicly Listed Company (IPO ≤ 10% paid-up)": {
        "AY 2024-25": (25.0, 22.5,  "22.5% (if banking conditions met)"),
        "AY 2025-26": (25.0, 22.5,  "22.5% (if banking conditions met)"),
        "AY 2026-27": (27.5, 25.0,  "25% (if banking conditions met)"),
        "AY 2027-28": (27.5, 25.0,  "25% (if banking conditions met)"),
    },
    "Non-Listed / Private Limited Company": {
        "AY 2024-25": (27.5, 25.0,  "25% (if banking conditions met)"),
        "AY 2025-26": (27.5, 25.0,  "25% (if banking conditions met)"),
        "AY 2026-27": (27.5, 25.0,  "25% (if banking conditions met)"),
        "AY 2027-28": (27.5, 25.0,  "25% (if banking conditions met)"),
    },
    "One Person Company (OPC)": {
        "AY 2024-25": (22.5, 20.0,  "20% (if banking conditions met)"),
        "AY 2025-26": (22.5, 20.0,  "20% (if banking conditions met)"),
        "AY 2026-27": (27.5, 27.5,  "27.5% (fixed, no reduced rate)"),
        "AY 2027-28": (27.5, 27.5,  "27.5% (fixed, no reduced rate)"),
    },
    "Bank / Insurance / NBFI (Listed)": {
        "AY 2024-25": (37.5, 37.5,  "37.5% (no reduction)"),
        "AY 2025-26": (37.5, 37.5,  "37.5% (no reduction)"),
        "AY 2026-27": (37.5, 37.5,  "37.5% (no reduction)"),
        "AY 2027-28": (37.5, 37.5,  "37.5% (no reduction)"),
    },
    "Bank / Insurance / NBFI (Non-Listed)": {
        "AY 2024-25": (40.0, 40.0,  "40% (no reduction)"),
        "AY 2025-26": (40.0, 40.0,  "40% (no reduction)"),
        "AY 2026-27": (40.0, 40.0,  "40% (no reduction)"),
        "AY 2027-28": (40.0, 40.0,  "40% (no reduction)"),
    },
    "Merchant Bank": {
        "AY 2024-25": (37.5, 37.5,  "37.5%"),
        "AY 2025-26": (27.5, 27.5,  "27.5% (reduced by Finance Ordinance 2025)"),
        "AY 2026-27": (27.5, 27.5,  "27.5%"),
        "AY 2027-28": (27.5, 27.5,  "27.5%"),
    },
    "Mobile Phone Operator (Telecom)": {
        "AY 2024-25": (45.0, 45.0,  "45% (no reduction)"),
        "AY 2025-26": (45.0, 45.0,  "45% (no reduction)"),
        "AY 2026-27": (45.0, 45.0,  "45% (no reduction)"),
        "AY 2027-28": (45.0, 45.0,  "45% (no reduction)"),
    },
    "Cigarette / Tobacco Company": {
        "AY 2024-25": (45.0, 45.0,  "45% + 2.5% surcharge"),
        "AY 2025-26": (45.0, 45.0,  "45% + 2.5% surcharge"),
        "AY 2026-27": (45.0, 45.0,  "45% + 2.5% surcharge"),
        "AY 2027-28": (45.0, 45.0,  "45% + 2.5% surcharge"),
    },
    "Co-operative Society": {
        "AY 2024-25": (20.0, 20.0,  "20%"),
        "AY 2025-26": (20.0, 20.0,  "20%"),
        "AY 2026-27": (20.0, 20.0,  "20%"),
        "AY 2027-28": (20.0, 20.0,  "20%"),
    },
    "Private University / Medical / Engineering College": {
        "AY 2024-25": (15.0, 15.0,  "15%"),
        "AY 2025-26": (15.0, 15.0,  "15%"),
        "AY 2026-27": (15.0, 15.0,  "15%"),
        "AY 2027-28": (15.0, 15.0,  "15%"),
    },
    "Branch of Foreign Company": {
        "AY 2024-25": (27.5, 27.5,  "27.5%"),
        "AY 2025-26": (27.5, 27.5,  "27.5%"),
        "AY 2026-27": (27.5, 27.5,  "27.5%"),
        "AY 2027-28": (27.5, 27.5,  "27.5%"),
    },
}

# Minimum tax on gross receipts
# (standard_rate, tobacco_rate, telecom_rate, manufacturing_first3yr_rate)
MIN_TAX_RATES = {
    "AY 2024-25": (0.006, 0.01, 0.02, 0.001),
    "AY 2025-26": (0.010, 0.01, 0.02, 0.001),
    "AY 2026-27": (0.010, 0.01, 0.02, 0.001),
    "AY 2027-28": (0.010, 0.01, 0.02, 0.001),
}

# Depreciation rates (ITA 2023, Schedule 3) — reducing balance method
DEPR_RATES = {
    "Buildings (permanent structure)": 2.5,
    "Buildings (temporary structure)": 10.0,
    "Furniture & fittings": 10.0,
    "Plant & machinery (general)": 20.0,
    "Plant & machinery (industrial)": 30.0,
    "Computer & IT equipment": 30.0,
    "Motor vehicles (passenger, capped BDT 30L cost)": 20.0,
    "Motor vehicles (commercial/delivery)": 20.0,
    "Ships & vessels": 10.0,
    "Aircraft": 10.0,
    "Intangibles / goodwill": 10.0,
    "Pre-commencement expenses (straight-line)": 20.0,
}

# ═══════════════════════════════════════════════════════════════════════════
# DEFAULT INPUTS
# ═══════════════════════════════════════════════════════════════════════════
DEFAULTS = {
    # Company identity
    "company_name": "ABC Manufacturing Ltd.",
    "tin": "987654321012",
    "incorporation_date": "2015-01-01",
    "assessment_year": "AY 2025-26",
    "income_year_end": "31 December 2024",
    "company_type": "Non-Listed / Private Limited Company",
    "industry_sector": "Manufacturing",
    "banking_conditions_met": True,
    "is_first_3yr_manufacturer": False,
    "has_tobacco_surcharge": False,

    # Revenue / gross receipts
    "revenue_sales": 50_000_000.0,
    "revenue_services": 5_000_000.0,
    "revenue_export": 8_000_000.0,
    "revenue_other_operating": 1_200_000.0,
    "total_gross_receipts_override": 0.0,   # 0 = computed from above

    # Non-operating income
    "interest_income": 800_000.0,
    "dividend_from_listed": 400_000.0,
    "dividend_from_unlisted": 200_000.0,
    "capital_gain_listed_shares": 300_000.0,
    "capital_gain_other": 150_000.0,
    "rent_income": 600_000.0,
    "other_income": 250_000.0,

    # Allowable operating expenses
    "cost_of_goods_sold": 28_000_000.0,
    "salaries_wages": 6_500_000.0,
    "rent_office": 1_200_000.0,
    "utilities": 800_000.0,
    "repairs_maintenance": 400_000.0,
    "insurance": 300_000.0,
    "traveling_conveyance": 500_000.0,
    "foreign_travel": 200_000.0,    # capped at 1.25% of disclosed turnover
    "advertising_promotion": 250_000.0,  # capped at 0.5% of disclosed turnover
    "bank_charges": 150_000.0,
    "legal_professional_fees": 300_000.0,
    "audit_fees": 200_000.0,
    "bad_debt_written_off": 180_000.0,
    "donation_approved": 100_000.0,  # capped at 10% of net profit (first 3yr) or 8%
    "provident_fund_contribution": 520_000.0,
    "gratuity_fund_contribution": 200_000.0,
    "other_operating_expenses": 600_000.0,

    # Finance costs
    "interest_expense": 1_200_000.0,
    "bank_loan_interest": 800_000.0,

    # Accounting depreciation (per books)
    "accounting_depreciation": 2_500_000.0,

    # Depreciation schedule (tax)
    "depr_buildings_wdv": 5_000_000.0,
    "depr_buildings_rate": 2.5,
    "depr_plant_machinery_wdv": 8_000_000.0,
    "depr_plant_machinery_rate": 30.0,
    "depr_computers_wdv": 1_200_000.0,
    "depr_computers_rate": 30.0,
    "depr_furniture_wdv": 800_000.0,
    "depr_furniture_rate": 10.0,
    "depr_vehicles_wdv": 2_000_000.0,  # capped at BDT 3M cost
    "depr_vehicles_rate": 20.0,
    "depr_other_wdv": 500_000.0,
    "depr_other_rate": 10.0,

    # Add-backs / disallowances
    "addback_cash_payment_over_limit": 500_000.0,   # cash payment >50k single or >5L annual
    "addback_perquisite_over_limit": 0.0,            # employee perquisites >BDT 1M per employee
    "addback_foreign_travel_excess": 0.0,            # excess over 1.25% of turnover
    "addback_promotion_excess": 0.0,                 # excess over 0.5% of turnover
    "addback_tds_non_compliance": 0.0,               # expenses where TDS not deducted
    "addback_donation_excess": 0.0,                  # donation over 10%/8% of net profit
    "addback_provision_not_written_off": 0.0,        # general provisions not allowable
    "addback_prior_year_expenses": 0.0,
    "addback_personal_expenses": 0.0,
    "addback_capital_expenditure_misclassified": 0.0,
    "addback_fine_penalty": 50_000.0,               # fines/penalties never deductible
    "addback_other": 0.0,

    # Special deductions
    "dedn_export_cash_incentive": 0.0,
    "dedn_workers_profit_participation_fund": 0.0,   # 5% of net profit
    "dedn_scientific_research": 0.0,
    "dedn_charitable_donation_allowable": 100_000.0,
    "dedn_other": 0.0,

    # Exempt income (already included in accounting profit)
    "exempt_foreign_remittance": 0.0,
    "exempt_dividend_from_listed": 400_000.0,        # often exempt at company level
    "exempt_agri_income": 0.0,
    "exempt_other": 0.0,

    # Tax holiday / incentives
    "has_tax_holiday": False,
    "tax_holiday_type": "None",
    "tax_holiday_years_remaining": 0,
    "tax_holiday_income_amount": 0.0,
    "export_tax_rebate_pct": 0.0,           # % rebate on tax for export income
    "reduced_rate_income": 0.0,             # income eligible for reduced/concessional rate
    "reduced_rate_pct": 0.0,

    # Carried-forward losses
    "bf_business_loss_yr1": 0.0,
    "bf_business_loss_yr2": 0.0,
    "bf_business_loss_yr3": 0.0,
    "bf_business_loss_yr4": 0.0,
    "bf_business_loss_yr5": 0.0,
    "bf_capital_loss": 0.0,
    "bf_unabsorbed_depreciation": 0.0,

    # TDS / Advance Tax credits
    "tds_on_sales_receipts": 350_000.0,     # Sec 82C — TDS on sales proceeds
    "tds_on_services_received": 80_000.0,
    "tds_on_import": 120_000.0,
    "tds_on_export_proceeds": 0.0,
    "tds_on_bank_interest": 80_000.0,       # 10% TDS on interest
    "tds_on_rent_paid": 0.0,                # TDS deducted by tenant on rent paid to company
    "tds_on_dividend": 0.0,
    "tds_other": 0.0,
    "advance_tax_q1": 150_000.0,            # 15 Sep installment
    "advance_tax_q2": 150_000.0,            # 15 Dec installment
    "advance_tax_q3": 150_000.0,            # 15 Mar installment
    "advance_tax_q4": 150_000.0,            # 15 Jun installment
    "tax_paid_with_return": 0.0,

    # Minimum tax override
    "use_gross_receipts_override": False,

    # Notes
    "notes_foreign_employees": 0,           # number of unauthorised foreign employees
}

if "co" not in st.session_state:
    st.session_state["co"] = DEFAULTS.copy()

def reset():
    st.session_state["co"] = DEFAULTS.copy()

def V(k):
    return st.session_state["co"][k]

def fmt(x, d=0):
    if x is None: return ""
    neg = x < 0
    s = f"{abs(x):,.{d}f}"
    return f"({s})" if neg else s

def bdt(x, d=0):
    if x is None: return ""
    return f"{BDT} {fmt(x, d)}"

def pct(x, d=2):
    return f"{x:.{d}f}%"

# ═══════════════════════════════════════════════════════════════════════════
# CORE COMPUTATION
# ═══════════════════════════════════════════════════════════════════════════
def compute():
    co = st.session_state["co"]
    ay = co["assessment_year"]
    ct = co["company_type"]

    # ── 1. GROSS RECEIPTS ────────────────────────────────────────────────
    operating_revenue = (co["revenue_sales"] + co["revenue_services"]
                         + co["revenue_export"] + co["revenue_other_operating"])
    total_non_op_income = (co["interest_income"] + co["dividend_from_listed"]
                           + co["dividend_from_unlisted"] + co["capital_gain_listed_shares"]
                           + co["capital_gain_other"] + co["rent_income"] + co["other_income"])
    total_gross_receipts = (co["total_gross_receipts_override"] if co["total_gross_receipts_override"] > 0
                            else operating_revenue + total_non_op_income)

    # ── 2. ACCOUNTING PROFIT ─────────────────────────────────────────────
    total_income_accounting = operating_revenue + total_non_op_income
    total_operating_exp = (co["cost_of_goods_sold"] + co["salaries_wages"] + co["rent_office"]
                           + co["utilities"] + co["repairs_maintenance"] + co["insurance"]
                           + co["traveling_conveyance"] + co["foreign_travel"]
                           + co["advertising_promotion"] + co["bank_charges"]
                           + co["legal_professional_fees"] + co["audit_fees"]
                           + co["bad_debt_written_off"] + co["donation_approved"]
                           + co["provident_fund_contribution"] + co["gratuity_fund_contribution"]
                           + co["other_operating_expenses"])
    total_finance_cost = co["interest_expense"] + co["bank_loan_interest"]
    accounting_profit_before_dep = total_income_accounting - total_operating_exp - total_finance_cost
    accounting_profit = accounting_profit_before_dep - co["accounting_depreciation"]

    # ── 3. TAX DEPRECIATION ───────────────────────────────────────────────
    depr_buildings    = co["depr_buildings_wdv"]    * co["depr_buildings_rate"]    / 100
    depr_plant        = co["depr_plant_machinery_wdv"] * co["depr_plant_machinery_rate"] / 100
    depr_computers    = co["depr_computers_wdv"]    * co["depr_computers_rate"]    / 100
    depr_furniture    = co["depr_furniture_wdv"]    * co["depr_furniture_rate"]    / 100
    depr_vehicles     = co["depr_vehicles_wdv"]     * co["depr_vehicles_rate"]     / 100
    depr_other        = co["depr_other_wdv"]        * co["depr_other_rate"]        / 100
    total_tax_depr    = depr_buildings + depr_plant + depr_computers + depr_furniture + depr_vehicles + depr_other

    depr_timing_diff = total_tax_depr - co["accounting_depreciation"]

    # ── 4. ADD-BACKS (DISALLOWANCES) ─────────────────────────────────────
    # Compute turnover-based limits
    disclosed_turnover = operating_revenue
    max_foreign_travel = disclosed_turnover * 0.0125
    max_promotion      = disclosed_turnover * 0.005
    net_profit_for_donation = accounting_profit
    max_donation = net_profit_for_donation * (0.10 if co["is_first_3yr_manufacturer"] else 0.08)
    max_donation = max(max_donation, 0)

    addback_foreign_travel_excess = max(0, co["foreign_travel"] - max_foreign_travel)
    addback_promotion_excess = max(0, co["advertising_promotion"] - max_promotion)
    addback_donation_excess = max(0, co["donation_approved"] - max_donation)

    total_addbacks = (co["addback_cash_payment_over_limit"]
                      + co["addback_perquisite_over_limit"]
                      + addback_foreign_travel_excess
                      + addback_promotion_excess
                      + co["addback_tds_non_compliance"]
                      + addback_donation_excess
                      + co["addback_provision_not_written_off"]
                      + co["addback_prior_year_expenses"]
                      + co["addback_personal_expenses"]
                      + co["addback_capital_expenditure_misclassified"]
                      + co["addback_fine_penalty"]
                      + co["addback_other"])

    # ── 5. SPECIAL DEDUCTIONS ─────────────────────────────────────────────
    total_special_dedns = (co["dedn_export_cash_incentive"]
                           + co["dedn_workers_profit_participation_fund"]
                           + co["dedn_scientific_research"]
                           + co["dedn_charitable_donation_allowable"]
                           + co["dedn_other"])

    # ── 6. EXEMPT INCOME ─────────────────────────────────────────────────
    total_exempt = (co["exempt_foreign_remittance"] + co["exempt_dividend_from_listed"]
                    + co["exempt_agri_income"] + co["exempt_other"])

    # ── 7. ADJUSTED PROFIT BEFORE LOSS SET-OFF ───────────────────────────
    # Start from accounting profit, reverse accounting dep, add tax dep
    statutory_profit = (accounting_profit
                        + co["accounting_depreciation"]   # reverse book dep
                        - total_tax_depr                  # apply tax dep
                        + total_addbacks                  # add-backs
                        - total_special_dedns             # extra deductions
                        - total_exempt)                   # exempt income removed

    # ── 8. CARRIED-FORWARD LOSSES ─────────────────────────────────────────
    bf_total_loss = (co["bf_business_loss_yr1"] + co["bf_business_loss_yr2"]
                     + co["bf_business_loss_yr3"] + co["bf_business_loss_yr4"]
                     + co["bf_business_loss_yr5"])
    bf_unabsorbed_dep = co["bf_unabsorbed_depreciation"]
    bf_cap_loss = co["bf_capital_loss"]

    set_off_business_loss = min(max(0, statutory_profit), bf_total_loss)
    profit_after_loss = max(0, statutory_profit - set_off_business_loss)
    set_off_unabsorbed_dep = min(profit_after_loss, bf_unabsorbed_dep)
    profit_after_unabsorbed_dep = max(0, profit_after_loss - set_off_unabsorbed_dep)

    # ── 9. TAX HOLIDAY / EXEMPT BUSINESS INCOME ──────────────────────────
    tax_holiday_income = co["tax_holiday_income_amount"] if co["has_tax_holiday"] else 0.0
    taxable_income = max(0, profit_after_unabsorbed_dep - tax_holiday_income)
    if taxable_income < 0:
        taxable_income = 0.0

    # ── 10. DETERMINE CORPORATE TAX RATE ─────────────────────────────────
    rates = CORP_RATES[ct][ay]
    normal_rate, reduced_rate, reduced_label = rates
    applied_rate = reduced_rate if co["banking_conditions_met"] else normal_rate
    applied_rate_label = reduced_label if co["banking_conditions_met"] else f"{normal_rate}% (banking conditions NOT met)"

    # ── 11. GROSS TAX ON NORMAL INCOME ───────────────────────────────────
    gross_tax_normal = taxable_income * (applied_rate / 100.0)

    # Tobacco surcharge: 2.5% on tax
    tobacco_surcharge = gross_tax_normal * 0.025 if co["has_tobacco_surcharge"] else 0.0

    # ── 12. CAPITAL GAINS TAX ─────────────────────────────────────────────
    cgt_listed = co["capital_gain_listed_shares"] * 0.10   # 10% for resident companies
    cgt_other  = co["capital_gain_other"] * 0.15

    gross_tax = gross_tax_normal + tobacco_surcharge + cgt_listed + cgt_other

    # ── 13. MINIMUM TAX ON GROSS RECEIPTS (Three-way test) ───────────────
    mr = MIN_TAX_RATES[ay]
    std_min_rate, tobacco_min_rate, telecom_min_rate, mfg_min_rate = mr

    if co["company_type"] == "Cigarette / Tobacco Company":
        min_tax_rate = tobacco_min_rate
    elif co["company_type"] == "Mobile Phone Operator (Telecom)":
        min_tax_rate = telecom_min_rate
    elif co["is_first_3yr_manufacturer"]:
        min_tax_rate = mfg_min_rate
    else:
        min_tax_rate = std_min_rate

    # Minimum tax applies only if gross receipts > BDT 5 million
    min_tax_gross_receipts = 0.0
    if total_gross_receipts >= 5_000_000:
        min_tax_gross_receipts = total_gross_receipts * min_tax_rate

    # Three-way test: max of (gross_tax, min_tax_gross_receipts) but note WHT is separate
    final_tax_before_credits = max(gross_tax, min_tax_gross_receipts)
    min_tax_applied = final_tax_before_credits == min_tax_gross_receipts and min_tax_gross_receipts > gross_tax

    # ── 14. TAX CREDITS / TDS ─────────────────────────────────────────────
    total_tds = (co["tds_on_sales_receipts"] + co["tds_on_services_received"]
                 + co["tds_on_import"] + co["tds_on_export_proceeds"]
                 + co["tds_on_bank_interest"] + co["tds_on_rent_paid"]
                 + co["tds_on_dividend"] + co["tds_other"])
    total_advance_tax = (co["advance_tax_q1"] + co["advance_tax_q2"]
                         + co["advance_tax_q3"] + co["advance_tax_q4"])
    total_credits = total_tds + total_advance_tax + co["tax_paid_with_return"]
    net_tax_payable = max(0, final_tax_before_credits - total_credits)
    refund_due = max(0, total_credits - final_tax_before_credits)

    # ── 15. EFFECTIVE RATES ───────────────────────────────────────────────
    eff_rate = gross_tax / taxable_income * 100 if taxable_income > 0 else 0.0
    eff_rate_on_accounting = gross_tax / accounting_profit * 100 if accounting_profit > 0 else 0.0

    # Foreign employee additional tax (if applicable)
    foreign_emp_tax = 0.0
    if co["notes_foreign_employees"] > 0:
        foreign_emp_tax = max(gross_tax * 0.50, 500_000) * co["notes_foreign_employees"]

    return {
        "operating_revenue": operating_revenue, "total_non_op_income": total_non_op_income,
        "total_gross_receipts": total_gross_receipts,
        "total_income_accounting": total_income_accounting,
        "total_operating_exp": total_operating_exp, "total_finance_cost": total_finance_cost,
        "accounting_profit_before_dep": accounting_profit_before_dep,
        "accounting_profit": accounting_profit,
        "depr_buildings": depr_buildings, "depr_plant": depr_plant,
        "depr_computers": depr_computers, "depr_furniture": depr_furniture,
        "depr_vehicles": depr_vehicles, "depr_other": depr_other,
        "total_tax_depr": total_tax_depr, "depr_timing_diff": depr_timing_diff,
        "max_foreign_travel": max_foreign_travel, "max_promotion": max_promotion,
        "max_donation": max_donation,
        "addback_foreign_travel_excess": addback_foreign_travel_excess,
        "addback_promotion_excess": addback_promotion_excess,
        "addback_donation_excess": addback_donation_excess,
        "total_addbacks": total_addbacks, "total_special_dedns": total_special_dedns,
        "total_exempt": total_exempt, "statutory_profit": statutory_profit,
        "bf_total_loss": bf_total_loss, "set_off_business_loss": set_off_business_loss,
        "profit_after_loss": profit_after_loss,
        "set_off_unabsorbed_dep": set_off_unabsorbed_dep,
        "profit_after_unabsorbed_dep": profit_after_unabsorbed_dep,
        "tax_holiday_income": tax_holiday_income, "taxable_income": taxable_income,
        "applied_rate": applied_rate, "applied_rate_label": applied_rate_label,
        "normal_rate": normal_rate, "reduced_rate": reduced_rate,
        "gross_tax_normal": gross_tax_normal, "tobacco_surcharge": tobacco_surcharge,
        "cgt_listed": cgt_listed, "cgt_other": cgt_other, "gross_tax": gross_tax,
        "min_tax_rate": min_tax_rate, "min_tax_gross_receipts": min_tax_gross_receipts,
        "final_tax_before_credits": final_tax_before_credits,
        "min_tax_applied": min_tax_applied,
        "total_tds": total_tds, "total_advance_tax": total_advance_tax,
        "total_credits": total_credits, "net_tax_payable": net_tax_payable,
        "refund_due": refund_due, "eff_rate": eff_rate,
        "eff_rate_on_accounting": eff_rate_on_accounting,
        "foreign_emp_tax": foreign_emp_tax,
        "disclosed_turnover": disclosed_turnover,
    }

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.title("🏢 BD Corporate Tax")
    st.caption("Income Tax Act 2023\nFinance Ordinance 2025")
    st.markdown("---")
    r = compute()
    st.metric("Gross Receipts", bdt(r["total_gross_receipts"]))
    st.metric("Accounting Profit", bdt(r["accounting_profit"]))
    st.metric("Taxable Income", bdt(r["taxable_income"]))
    st.metric("Gross Tax", bdt(r["gross_tax"]))
    st.metric("Min. Tax (GR basis)", bdt(r["min_tax_gross_receipts"]))
    col = "🔴" if r["net_tax_payable"] > 0 else "🟢"
    label = "Tax Payable" if r["net_tax_payable"] > 0 else "Refund Due"
    st.metric(f"{col} {label}", bdt(r["net_tax_payable"] if r["net_tax_payable"] > 0 else r["refund_due"]))
    st.markdown("---")
    st.markdown(f"**Rate Applied:** {r['applied_rate']:.1f}%")
    st.markdown(f"**Effective Rate:** {r['eff_rate']:.2f}%")
    if st.button("🔄 Reset to defaults", use_container_width=True):
        reset(); st.rerun()
    st.caption("All amounts in BDT")

# ═══════════════════════════════════════════════════════════════════════════
# MAIN PAGE
# ═══════════════════════════════════════════════════════════════════════════
st.title("🏢 Bangladesh Company Income Tax Calculator")
st.caption("Income Tax Act 2023 | Finance Ordinance 2025 | NBR Bangladesh")

tabs = st.tabs([
    "🧮 Inputs",
    "📄 Profit & Loss",
    "🔧 Tax Adjustments",
    "📊 Tax Computation",
    "💸 TDS & Credits",
    "🏭 Incentives & Holidays",
    "🗒️ Return Summary",
    "📚 Corporate Tax Guide",
])

# ═══════════════════════════════════════════════════════════════════════════
# TAB 0 — INPUTS
# ═══════════════════════════════════════════════════════════════════════════
with tabs[0]:
    st.header("🧮 Company Tax Inputs")
    st.info("Enter all figures in BDT. All tabs recompute automatically. Negative values can be entered where applicable.")
    co = st.session_state["co"]

    with st.expander("🏢 Company Identity & Assessment Details", expanded=True):
        c1, c2 = st.columns(2)
        co["company_name"]    = c1.text_input("Company Name", co["company_name"], key="k_cn")
        co["tin"]             = c2.text_input("TIN (12-digit)", co["tin"], key="k_tin")
        c1, c2, c3 = st.columns(3)
        co["assessment_year"] = c1.selectbox("Assessment Year", list(MIN_TAX_RATES.keys()),
                                              index=list(MIN_TAX_RATES.keys()).index(co["assessment_year"]), key="k_ay")
        co["income_year_end"] = c2.text_input("Income Year End (e.g. 31 Dec 2024)", co["income_year_end"], key="k_iye")
        co["company_type"]    = c3.selectbox("Company / Entity Type", list(CORP_RATES.keys()),
                                              index=list(CORP_RATES.keys()).index(co["company_type"]), key="k_ct")
        c1, c2, c3 = st.columns(3)
        co["industry_sector"] = c1.text_input("Industry Sector", co["industry_sector"], key="k_ind")
        co["banking_conditions_met"] = c2.checkbox("Banking channel conditions met?", value=co["banking_conditions_met"], key="k_bc")
        co["is_first_3yr_manufacturer"] = c3.checkbox("Industrial manufacturer, first 3 income years?", value=co["is_first_3yr_manufacturer"], key="k_f3y")
        co["has_tobacco_surcharge"] = st.checkbox("Tobacco / cigarette company — apply 2.5% surcharge on tax?", value=co["has_tobacco_surcharge"], key="k_tob")

    with st.expander("💰 Revenue & Gross Receipts", expanded=True):
        st.caption("Enter annual gross receipts for the income year")
        c1, c2 = st.columns(2)
        co["revenue_sales"]           = c1.number_input("Sales / Product Revenue", value=co["revenue_sales"], step=100_000.0, min_value=0.0, key="k_rs")
        co["revenue_services"]        = c2.number_input("Service Revenue", value=co["revenue_services"], step=100_000.0, min_value=0.0, key="k_rsv")
        c1, c2 = st.columns(2)
        co["revenue_export"]          = c1.number_input("Export Revenue", value=co["revenue_export"], step=100_000.0, min_value=0.0, key="k_re")
        co["revenue_other_operating"] = c2.number_input("Other Operating Revenue", value=co["revenue_other_operating"], step=50_000.0, min_value=0.0, key="k_roo")
        co["total_gross_receipts_override"] = st.number_input(
            "Override: Total Gross Receipts (leave 0 to auto-compute from above)", value=co["total_gross_receipts_override"],
            step=100_000.0, min_value=0.0, key="k_tgr")

    with st.expander("📈 Non-Operating & Other Income", expanded=False):
        c1, c2, c3 = st.columns(3)
        co["interest_income"]             = c1.number_input("Interest / FDR Income", value=co["interest_income"], step=10_000.0, min_value=0.0, key="k_ii")
        co["dividend_from_listed"]        = c2.number_input("Dividend from Listed Companies", value=co["dividend_from_listed"], step=10_000.0, min_value=0.0, key="k_dl")
        co["dividend_from_unlisted"]      = c3.number_input("Dividend from Unlisted Companies", value=co["dividend_from_unlisted"], step=10_000.0, min_value=0.0, key="k_du")
        c1, c2, c3 = st.columns(3)
        co["capital_gain_listed_shares"]  = c1.number_input("Capital Gain — Listed Shares (10% tax)", value=co["capital_gain_listed_shares"], step=10_000.0, min_value=0.0, key="k_cgl")
        co["capital_gain_other"]          = c2.number_input("Capital Gain — Other Assets (15% tax)", value=co["capital_gain_other"], step=10_000.0, min_value=0.0, key="k_cgo")
        co["rent_income"]                 = c3.number_input("Rental Income", value=co["rent_income"], step=10_000.0, min_value=0.0, key="k_ri")
        co["other_income"]                = st.number_input("Other Miscellaneous Income", value=co["other_income"], step=10_000.0, min_value=0.0, key="k_oi")

    with st.expander("🧾 Cost of Goods Sold & Operating Expenses", expanded=False):
        c1, c2 = st.columns(2)
        co["cost_of_goods_sold"]        = c1.number_input("Cost of Goods Sold (COGS)", value=co["cost_of_goods_sold"], step=100_000.0, min_value=0.0, key="k_cogs")
        co["salaries_wages"]            = c2.number_input("Salaries & Wages", value=co["salaries_wages"], step=100_000.0, min_value=0.0, key="k_sw")
        c1, c2, c3 = st.columns(3)
        co["rent_office"]               = c1.number_input("Office Rent", value=co["rent_office"], step=50_000.0, min_value=0.0, key="k_ro")
        co["utilities"]                 = c2.number_input("Utilities (electricity, gas, water)", value=co["utilities"], step=10_000.0, min_value=0.0, key="k_ut")
        co["repairs_maintenance"]       = c3.number_input("Repairs & Maintenance", value=co["repairs_maintenance"], step=10_000.0, min_value=0.0, key="k_rm")
        c1, c2, c3 = st.columns(3)
        co["insurance"]                 = c1.number_input("Insurance", value=co["insurance"], step=10_000.0, min_value=0.0, key="k_ins")
        co["traveling_conveyance"]      = c2.number_input("Traveling & Conveyance (local)", value=co["traveling_conveyance"], step=10_000.0, min_value=0.0, key="k_tc")
        co["foreign_travel"]            = c3.number_input("Foreign Travel", value=co["foreign_travel"], step=10_000.0, min_value=0.0, key="k_ft")
        c1, c2, c3 = st.columns(3)
        co["advertising_promotion"]     = c1.number_input("Advertising & Promotion", value=co["advertising_promotion"], step=10_000.0, min_value=0.0, key="k_ap")
        co["bank_charges"]              = c2.number_input("Bank Charges & Commission", value=co["bank_charges"], step=5_000.0, min_value=0.0, key="k_bc2")
        co["legal_professional_fees"]   = c3.number_input("Legal & Professional Fees", value=co["legal_professional_fees"], step=10_000.0, min_value=0.0, key="k_lpf")
        c1, c2, c3 = st.columns(3)
        co["audit_fees"]                = c1.number_input("Audit Fees", value=co["audit_fees"], step=5_000.0, min_value=0.0, key="k_af")
        co["bad_debt_written_off"]      = c2.number_input("Bad Debts Written Off", value=co["bad_debt_written_off"], step=10_000.0, min_value=0.0, key="k_bd")
        co["donation_approved"]         = c3.number_input("Donation (approved institution)", value=co["donation_approved"], step=10_000.0, min_value=0.0, key="k_don")
        c1, c2, c3 = st.columns(3)
        co["provident_fund_contribution"]= c1.number_input("Provident Fund Contribution", value=co["provident_fund_contribution"], step=10_000.0, min_value=0.0, key="k_pf")
        co["gratuity_fund_contribution"] = c2.number_input("Gratuity Fund Contribution", value=co["gratuity_fund_contribution"], step=10_000.0, min_value=0.0, key="k_gf")
        co["other_operating_expenses"]  = c3.number_input("Other Operating Expenses", value=co["other_operating_expenses"], step=10_000.0, min_value=0.0, key="k_ooe")

    with st.expander("🏦 Finance Costs & Accounting Depreciation", expanded=False):
        c1, c2, c3 = st.columns(3)
        co["interest_expense"]        = c1.number_input("Interest Expense (term loan)", value=co["interest_expense"], step=10_000.0, min_value=0.0, key="k_ie")
        co["bank_loan_interest"]      = c2.number_input("Bank Overdraft / Revolver Interest", value=co["bank_loan_interest"], step=10_000.0, min_value=0.0, key="k_bli")
        co["accounting_depreciation"] = c3.number_input("Accounting Depreciation (per books)", value=co["accounting_depreciation"], step=50_000.0, min_value=0.0, key="k_adep")

    with st.expander("🔧 Tax Depreciation Schedule (Written Down Value Method)", expanded=False):
        st.caption("Enter Written Down Value (WDV) at start of year and the applicable tax depreciation rate")
        c1, c2, c3 = st.columns(3)
        co["depr_buildings_wdv"]       = c1.number_input("Buildings WDV", value=co["depr_buildings_wdv"], step=100_000.0, min_value=0.0, key="k_dbw")
        co["depr_buildings_rate"]      = c2.number_input("Buildings Rate (%)", value=co["depr_buildings_rate"], step=0.5, min_value=0.0, max_value=50.0, key="k_dbr")
        c3.metric("Tax Dep (Buildings)", bdt(co["depr_buildings_wdv"] * co["depr_buildings_rate"] / 100))
        c1, c2, c3 = st.columns(3)
        co["depr_plant_machinery_wdv"] = c1.number_input("Plant & Machinery WDV", value=co["depr_plant_machinery_wdv"], step=100_000.0, min_value=0.0, key="k_dpmw")
        co["depr_plant_machinery_rate"]= c2.number_input("Plant & Machinery Rate (%)", value=co["depr_plant_machinery_rate"], step=0.5, min_value=0.0, max_value=50.0, key="k_dpmr")
        c3.metric("Tax Dep (Plant)", bdt(co["depr_plant_machinery_wdv"] * co["depr_plant_machinery_rate"] / 100))
        c1, c2, c3 = st.columns(3)
        co["depr_computers_wdv"]       = c1.number_input("Computers & IT WDV", value=co["depr_computers_wdv"], step=50_000.0, min_value=0.0, key="k_dcw")
        co["depr_computers_rate"]      = c2.number_input("Computers Rate (%)", value=co["depr_computers_rate"], step=0.5, min_value=0.0, max_value=50.0, key="k_dcr")
        c3.metric("Tax Dep (Computers)", bdt(co["depr_computers_wdv"] * co["depr_computers_rate"] / 100))
        c1, c2, c3 = st.columns(3)
        co["depr_furniture_wdv"]       = c1.number_input("Furniture & Fixtures WDV", value=co["depr_furniture_wdv"], step=50_000.0, min_value=0.0, key="k_dfw")
        co["depr_furniture_rate"]      = c2.number_input("Furniture Rate (%)", value=co["depr_furniture_rate"], step=0.5, min_value=0.0, max_value=50.0, key="k_dfr")
        c3.metric("Tax Dep (Furniture)", bdt(co["depr_furniture_wdv"] * co["depr_furniture_rate"] / 100))
        c1, c2, c3 = st.columns(3)
        co["depr_vehicles_wdv"]        = c1.number_input("Motor Vehicles WDV (cost capped @ BDT 30L)", value=co["depr_vehicles_wdv"], step=50_000.0, min_value=0.0, key="k_dvw")
        co["depr_vehicles_rate"]       = c2.number_input("Vehicles Rate (%)", value=co["depr_vehicles_rate"], step=0.5, min_value=0.0, max_value=50.0, key="k_dvr")
        c3.metric("Tax Dep (Vehicles)", bdt(co["depr_vehicles_wdv"] * co["depr_vehicles_rate"] / 100))
        c1, c2, c3 = st.columns(3)
        co["depr_other_wdv"]           = c1.number_input("Other Assets WDV", value=co["depr_other_wdv"], step=50_000.0, min_value=0.0, key="k_dow")
        co["depr_other_rate"]          = c2.number_input("Other Assets Rate (%)", value=co["depr_other_rate"], step=0.5, min_value=0.0, max_value=50.0, key="k_dor")
        c3.metric("Tax Dep (Other)", bdt(co["depr_other_wdv"] * co["depr_other_rate"] / 100))

    with st.expander("➕ Add-backs / Disallowances (override auto-computed)", expanded=False):
        st.caption("Auto-computed: foreign travel excess, promotion excess, donation excess. Others enter manually.")
        c1, c2, c3 = st.columns(3)
        co["addback_cash_payment_over_limit"]          = c1.number_input("Cash payments exceeding limits", value=co["addback_cash_payment_over_limit"], step=10_000.0, min_value=0.0, key="k_acpl")
        co["addback_perquisite_over_limit"]            = c2.number_input("Perquisites over BDT 1M per employee", value=co["addback_perquisite_over_limit"], step=10_000.0, min_value=0.0, key="k_apol")
        co["addback_tds_non_compliance"]               = c3.number_input("Expenses — TDS not deducted (Sec 55)", value=co["addback_tds_non_compliance"], step=10_000.0, min_value=0.0, key="k_atnc")
        c1, c2, c3 = st.columns(3)
        co["addback_provision_not_written_off"]        = c1.number_input("General provisions (not specific w/o)", value=co["addback_provision_not_written_off"], step=10_000.0, min_value=0.0, key="k_apnwo")
        co["addback_prior_year_expenses"]              = c2.number_input("Prior year expenses charged this year", value=co["addback_prior_year_expenses"], step=10_000.0, min_value=0.0, key="k_apye")
        co["addback_personal_expenses"]                = c3.number_input("Personal / non-business expenses", value=co["addback_personal_expenses"], step=10_000.0, min_value=0.0, key="k_ape")
        c1, c2, c3 = st.columns(3)
        co["addback_capital_expenditure_misclassified"]= c1.number_input("Capex charged as revenue (misclassified)", value=co["addback_capital_expenditure_misclassified"], step=10_000.0, min_value=0.0, key="k_acm")
        co["addback_fine_penalty"]                     = c2.number_input("Fines, penalties (always disallowed)", value=co["addback_fine_penalty"], step=5_000.0, min_value=0.0, key="k_afp")
        co["addback_other"]                            = c3.number_input("Other disallowances", value=co["addback_other"], step=10_000.0, min_value=0.0, key="k_ao")

    with st.expander("➖ Special Deductions & Exempt Income", expanded=False):
        c1, c2, c3 = st.columns(3)
        co["dedn_export_cash_incentive"]          = c1.number_input("Export cash incentive / subsidy", value=co["dedn_export_cash_incentive"], step=10_000.0, min_value=0.0, key="k_deci")
        co["dedn_workers_profit_participation_fund"]= c2.number_input("Workers' Profit Participation Fund (5%)", value=co["dedn_workers_profit_participation_fund"], step=10_000.0, min_value=0.0, key="k_dwppf")
        co["dedn_scientific_research"]            = c3.number_input("Approved scientific research expenditure", value=co["dedn_scientific_research"], step=10_000.0, min_value=0.0, key="k_dsr")
        c1, c2 = st.columns(2)
        co["dedn_charitable_donation_allowable"]  = c1.number_input("Allowable charitable donation (after cap check)", value=co["dedn_charitable_donation_allowable"], step=10_000.0, min_value=0.0, key="k_dcd")
        co["dedn_other"]                          = c2.number_input("Other allowable deductions", value=co["dedn_other"], step=10_000.0, min_value=0.0, key="k_do")
        st.markdown("**Exempt Income (included in accounting profit — to be removed)**")
        c1, c2, c3 = st.columns(3)
        co["exempt_foreign_remittance"]           = c1.number_input("Foreign remittance (exempt)", value=co["exempt_foreign_remittance"], step=10_000.0, min_value=0.0, key="k_efr")
        co["exempt_dividend_from_listed"]         = c2.number_input("Dividend from listed companies (exempt)", value=co["exempt_dividend_from_listed"], step=10_000.0, min_value=0.0, key="k_edl")
        co["exempt_agri_income"]                  = c3.number_input("Agricultural income (if exempt)", value=co["exempt_agri_income"], step=10_000.0, min_value=0.0, key="k_eai")
        co["exempt_other"]                        = st.number_input("Other exempt income", value=co["exempt_other"], step=10_000.0, min_value=0.0, key="k_eo")

    with st.expander("📉 Carried-Forward Losses & Unabsorbed Depreciation", expanded=False):
        st.caption("Business losses can be carried forward up to 6 years. Unabsorbed depreciation: indefinitely.")
        c1, c2, c3 = st.columns(3)
        co["bf_business_loss_yr1"] = c1.number_input("B/F Business Loss — Year 1", value=co["bf_business_loss_yr1"], step=10_000.0, min_value=0.0, key="k_bly1")
        co["bf_business_loss_yr2"] = c2.number_input("B/F Business Loss — Year 2", value=co["bf_business_loss_yr2"], step=10_000.0, min_value=0.0, key="k_bly2")
        co["bf_business_loss_yr3"] = c3.number_input("B/F Business Loss — Year 3", value=co["bf_business_loss_yr3"], step=10_000.0, min_value=0.0, key="k_bly3")
        c1, c2, c3 = st.columns(3)
        co["bf_business_loss_yr4"] = c1.number_input("B/F Business Loss — Year 4", value=co["bf_business_loss_yr4"], step=10_000.0, min_value=0.0, key="k_bly4")
        co["bf_business_loss_yr5"] = c2.number_input("B/F Business Loss — Year 5", value=co["bf_business_loss_yr5"], step=10_000.0, min_value=0.0, key="k_bly5")
        co["bf_capital_loss"]      = c3.number_input("B/F Capital Loss", value=co["bf_capital_loss"], step=10_000.0, min_value=0.0, key="k_bcl")
        co["bf_unabsorbed_depreciation"] = st.number_input("B/F Unabsorbed Depreciation (carried forward perpetually)", value=co["bf_unabsorbed_depreciation"], step=10_000.0, min_value=0.0, key="k_bud")

    with st.expander("🏭 Tax Holidays & Special Incentives", expanded=False):
        co["has_tax_holiday"]       = st.checkbox("Company has a tax holiday / exemption?", value=co["has_tax_holiday"], key="k_hth")
        if co["has_tax_holiday"]:
            c1, c2, c3 = st.columns(3)
            co["tax_holiday_type"]  = c1.selectbox("Tax holiday type",
                ["IT/Software (full exemption)", "Export-Oriented RMG", "Power Generation (SRO)",
                 "SEZ / Hi-Tech Park", "Agro-processing", "Other"], key="k_tht")
            co["tax_holiday_years_remaining"] = c2.number_input("Years remaining", value=co["tax_holiday_years_remaining"], step=1, min_value=0, max_value=15, key="k_thyr")
            co["tax_holiday_income_amount"] = c3.number_input("Income eligible for exemption", value=co["tax_holiday_income_amount"], step=100_000.0, min_value=0.0, key="k_thia")
        c1, c2 = st.columns(2)
        co["export_tax_rebate_pct"]  = c1.number_input("Export tax rebate (%)", value=co["export_tax_rebate_pct"], step=1.0, min_value=0.0, max_value=50.0, key="k_etrp")
        co["reduced_rate_income"]    = c2.number_input("Income at concessional / reduced rate", value=co["reduced_rate_income"], step=10_000.0, min_value=0.0, key="k_rri")
        co["reduced_rate_pct"]       = st.number_input("Concessional tax rate (%)", value=co["reduced_rate_pct"], step=1.0, min_value=0.0, max_value=45.0, key="k_rrp")

    with st.expander("💸 TDS Deducted at Source & Advance Tax Credits", expanded=False):
        st.caption("TDS collected by payers and advance tax paid — these are credits against final liability.")
        c1, c2, c3 = st.columns(3)
        co["tds_on_sales_receipts"]  = c1.number_input("TDS on Sales Receipts (Sec 82C)", value=co["tds_on_sales_receipts"], step=10_000.0, min_value=0.0, key="k_tdssr")
        co["tds_on_services_received"]= c2.number_input("TDS on Services Received", value=co["tds_on_services_received"], step=5_000.0, min_value=0.0, key="k_tdssv")
        co["tds_on_import"]          = c3.number_input("TDS/AT on Import", value=co["tds_on_import"], step=10_000.0, min_value=0.0, key="k_tdsim")
        c1, c2, c3 = st.columns(3)
        co["tds_on_export_proceeds"] = c1.number_input("TDS on Export Proceeds", value=co["tds_on_export_proceeds"], step=10_000.0, min_value=0.0, key="k_tdsex")
        co["tds_on_bank_interest"]   = c2.number_input("TDS on Bank Interest (10%)", value=co["tds_on_bank_interest"], step=5_000.0, min_value=0.0, key="k_tdsbi")
        co["tds_on_rent_paid"]       = c3.number_input("TDS on Rent Paid to Company", value=co["tds_on_rent_paid"], step=5_000.0, min_value=0.0, key="k_tdsrp")
        c1, c2 = st.columns(2)
        co["tds_on_dividend"]        = c1.number_input("TDS on Dividend Received", value=co["tds_on_dividend"], step=5_000.0, min_value=0.0, key="k_tdsdiv")
        co["tds_other"]              = c2.number_input("TDS — Other", value=co["tds_other"], step=5_000.0, min_value=0.0, key="k_tdso")
        st.markdown("**Advance Tax Installments (Sec 145 — 4 quarterly installments)**")
        c1, c2, c3, c4 = st.columns(4)
        co["advance_tax_q1"] = c1.number_input("Q1 (15 Sep)", value=co["advance_tax_q1"], step=10_000.0, min_value=0.0, key="k_atq1")
        co["advance_tax_q2"] = c2.number_input("Q2 (15 Dec)", value=co["advance_tax_q2"], step=10_000.0, min_value=0.0, key="k_atq2")
        co["advance_tax_q3"] = c3.number_input("Q3 (15 Mar)", value=co["advance_tax_q3"], step=10_000.0, min_value=0.0, key="k_atq3")
        co["advance_tax_q4"] = c4.number_input("Q4 (15 Jun)", value=co["advance_tax_q4"], step=10_000.0, min_value=0.0, key="k_atq4")
        co["tax_paid_with_return"] = st.number_input("Tax paid with return (pay-order / challan)", value=co["tax_paid_with_return"], step=10_000.0, min_value=0.0, key="k_tpwr")

    with st.expander("⚠️ Compliance & Penalty Items", expanded=False):
        co["notes_foreign_employees"] = st.number_input(
            "Number of unauthorised foreign employees (if any — triggers 50% additional tax or BDT 5L per employee, whichever higher)",
            value=float(co["notes_foreign_employees"]), step=1.0, min_value=0.0, key="k_nfe")
        co["notes_foreign_employees"] = int(co["notes_foreign_employees"])

    st.success("✅ All inputs saved. Switch to any tab to see the tax computation.")

# ── RECOMPUTE ──────────────────────────────────────────────────────────────
r = compute()
co = st.session_state["co"]
ay = co["assessment_year"]

# helper for simple 2-col row rendering
def row2(label, val, bold=False):
    c1, c2 = st.columns([5, 2])
    if bold:
        c1.markdown(f"**{label}**"); c2.markdown(f"**{bdt(val)}**")
    else:
        c1.markdown(f"&nbsp;&nbsp;&nbsp;{label}", unsafe_allow_html=True); c2.markdown(bdt(val))

def divider():
    st.markdown("<hr style='margin:3px 0'>", unsafe_allow_html=True)

def double_divider():
    st.markdown("<hr style='border-top:3px double #333;margin:6px 0'>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# TAB 1 — PROFIT & LOSS
# ═══════════════════════════════════════════════════════════════════════════
with tabs[1]:
    st.header("📄 Accounting Profit & Loss Computation")
    st.caption(f"{V('company_name')}  |  {ay}  |  Year ended: {V('income_year_end')}")

    c1,c2,c3 = st.columns(3)
    c1.metric("Gross Receipts", bdt(r["total_gross_receipts"]))
    c2.metric("Accounting Profit", bdt(r["accounting_profit"]))
    c3.metric("Taxable Income", bdt(r["taxable_income"]))

    st.markdown("---")
    st.markdown("**INCOME**")
    row2("Sales / Product Revenue", co["revenue_sales"])
    row2("Service Revenue", co["revenue_services"])
    row2("Export Revenue", co["revenue_export"])
    row2("Other Operating Revenue", co["revenue_other_operating"])
    row2("Total Operating Revenue", r["operating_revenue"], bold=True); divider()
    row2("Interest / FDR Income", co["interest_income"])
    row2("Dividend from listed companies", co["dividend_from_listed"])
    row2("Dividend from unlisted companies", co["dividend_from_unlisted"])
    row2("Capital gain — listed shares", co["capital_gain_listed_shares"])
    row2("Capital gain — other assets", co["capital_gain_other"])
    row2("Rental income", co["rent_income"])
    row2("Other miscellaneous income", co["other_income"])
    row2("Total Non-Operating Income", r["total_non_op_income"], bold=True); divider()
    st.markdown(f"### TOTAL INCOME:  {bdt(r['total_income_accounting'])}"); double_divider()

    st.markdown("**EXPENSES**")
    row2("Cost of Goods Sold", co["cost_of_goods_sold"])
    row2("Salaries & Wages", co["salaries_wages"])
    row2("Office Rent", co["rent_office"])
    row2("Utilities", co["utilities"])
    row2("Repairs & Maintenance", co["repairs_maintenance"])
    row2("Insurance", co["insurance"])
    row2("Travelling & Conveyance", co["traveling_conveyance"])
    row2("Foreign Travel", co["foreign_travel"])
    row2("Advertising & Promotion", co["advertising_promotion"])
    row2("Bank Charges", co["bank_charges"])
    row2("Legal & Professional Fees", co["legal_professional_fees"])
    row2("Audit Fees", co["audit_fees"])
    row2("Bad Debts Written Off", co["bad_debt_written_off"])
    row2("Donation (approved)", co["donation_approved"])
    row2("Provident Fund Contribution", co["provident_fund_contribution"])
    row2("Gratuity Fund Contribution", co["gratuity_fund_contribution"])
    row2("Other Operating Expenses", co["other_operating_expenses"])
    row2("Total Operating Expenses", r["total_operating_exp"], bold=True); divider()
    row2("Interest Expense (term loan)", co["interest_expense"])
    row2("Bank Overdraft / Revolver Interest", co["bank_loan_interest"])
    row2("Total Finance Costs", r["total_finance_cost"], bold=True); divider()
    row2("Accounting Depreciation", co["accounting_depreciation"])
    st.markdown(f"### ACCOUNTING PROFIT:  {bdt(r['accounting_profit'])}"); double_divider()

# ═══════════════════════════════════════════════════════════════════════════
# TAB 2 — TAX ADJUSTMENTS
# ═══════════════════════════════════════════════════════════════════════════
with tabs[2]:
    st.header("🔧 Tax Adjustments — Accounting Profit → Taxable Income")
    st.caption(f"ITA 2023 | {ay}")

    row2("Accounting Profit (per books)", r["accounting_profit"], bold=True); divider()

    st.markdown("**ADD: Accounting Depreciation (reversed)**")
    row2("Book depreciation added back", co["accounting_depreciation"])
    row2("Profit before depreciation adjustment", r["accounting_profit_before_dep"], bold=True); divider()

    st.markdown("**LESS: Tax Depreciation (Schedule 3, ITA 2023)**")
    depr_rows = [
        (f"Buildings @ {co['depr_buildings_rate']}% of WDV {bdt(co['depr_buildings_wdv'])}", r["depr_buildings"]),
        (f"Plant & Machinery @ {co['depr_plant_machinery_rate']}% of WDV {bdt(co['depr_plant_machinery_wdv'])}", r["depr_plant"]),
        (f"Computers & IT @ {co['depr_computers_rate']}% of WDV {bdt(co['depr_computers_wdv'])}", r["depr_computers"]),
        (f"Furniture @ {co['depr_furniture_rate']}% of WDV {bdt(co['depr_furniture_wdv'])}", r["depr_furniture"]),
        (f"Vehicles @ {co['depr_vehicles_rate']}% of WDV {bdt(co['depr_vehicles_wdv'])}", r["depr_vehicles"]),
        (f"Other Assets @ {co['depr_other_rate']}% of WDV {bdt(co['depr_other_wdv'])}", r["depr_other"]),
    ]
    for label, val in depr_rows:
        row2(label, val)
    row2("Total Tax Depreciation (allowable)", r["total_tax_depr"], bold=True)
    diff_label = "ADD: Timing difference (book dep > tax dep)" if r["depr_timing_diff"] < 0 else "LESS: Timing difference (tax dep > book dep)"
    row2(diff_label, r["depr_timing_diff"]); divider()

    st.markdown("**ADD: Disallowances / Add-backs**")
    auto_addbacks = [
        (f"Cash payments exceeding limit (>BDT 50k single / >BDT 5L annual)", co["addback_cash_payment_over_limit"]),
        (f"Employee perquisites over BDT 1M per employee per year", co["addback_perquisite_over_limit"]),
        (f"Foreign travel excess (limit = 1.25% × {bdt(r['disclosed_turnover'])} = {bdt(r['max_foreign_travel'])})", r["addback_foreign_travel_excess"]),
        (f"Advertising/promotion excess (limit = 0.5% × turnover = {bdt(r['max_promotion'])})", r["addback_promotion_excess"]),
        ("Expenses — TDS not deducted (fully disallowed per Sec 55)", co["addback_tds_non_compliance"]),
        (f"Donation excess (limit = {8 if not co['is_first_3yr_manufacturer'] else 10}% of net profit = {bdt(r['max_donation'])})", r["addback_donation_excess"]),
        ("General provisions (not specific write-offs)", co["addback_provision_not_written_off"]),
        ("Prior year expenses", co["addback_prior_year_expenses"]),
        ("Personal / non-business expenses", co["addback_personal_expenses"]),
        ("Capex misclassified as revenue expense", co["addback_capital_expenditure_misclassified"]),
        ("Fines & penalties (always disallowed)", co["addback_fine_penalty"]),
        ("Other disallowances", co["addback_other"]),
    ]
    for label, val in auto_addbacks:
        if val > 0:
            row2(label, val)
    row2("Total Add-backs / Disallowances", r["total_addbacks"], bold=True); divider()

    st.markdown("**LESS: Special Deductions**")
    row2("Export cash incentive / subsidy", co["dedn_export_cash_incentive"])
    row2("Workers' Profit Participation Fund (5% of profit)", co["dedn_workers_profit_participation_fund"])
    row2("Approved scientific research expenditure", co["dedn_scientific_research"])
    row2("Allowable charitable donation (within cap)", co["dedn_charitable_donation_allowable"])
    row2("Other allowable deductions", co["dedn_other"])
    row2("Total Special Deductions", r["total_special_dedns"], bold=True); divider()

    st.markdown("**LESS: Exempt Income**")
    row2("Foreign remittance (via banking channel — exempt)", co["exempt_foreign_remittance"])
    row2("Dividend from listed companies (exempt at company level)", co["exempt_dividend_from_listed"])
    row2("Agricultural income (if exempt)", co["exempt_agri_income"])
    row2("Other exempt income", co["exempt_other"])
    row2("Total Exempt Income", r["total_exempt"], bold=True); divider()

    st.markdown(f"### Statutory Profit (before loss set-off):  {bdt(r['statutory_profit'])}"); double_divider()

    st.markdown("**LESS: Carried-Forward Losses**")
    row2("B/F Business Losses (years 1–5)", r["bf_total_loss"])
    row2("Business loss set off", -r["set_off_business_loss"])
    row2("Profit after business loss set-off", r["profit_after_loss"], bold=True)
    row2("B/F Unabsorbed Depreciation set off", -r["set_off_unabsorbed_dep"])
    row2("Profit after unabsorbed depreciation set-off", r["profit_after_unabsorbed_dep"], bold=True); divider()

    st.markdown("**LESS: Tax Holiday / Exempt Business Income**")
    row2("Tax holiday income (exempt)", r["tax_holiday_income"]); divider()

    st.markdown(f"### TAXABLE INCOME:  {bdt(r['taxable_income'])}"); double_divider()

# ═══════════════════════════════════════════════════════════════════════════
# TAB 3 — TAX COMPUTATION
# ═══════════════════════════════════════════════════════════════════════════
with tabs[3]:
    st.header("📊 Corporate Tax Computation")
    st.caption(f"{V('company_name')}  |  {ay}  |  {V('company_type')}")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Taxable Income", bdt(r["taxable_income"]))
    c2.metric("Tax Rate Applied", pct(r["applied_rate"]))
    c3.metric("Gross Tax", bdt(r["gross_tax"]))
    c4.metric("Effective Rate", pct(r["eff_rate"]))

    st.markdown("---")
    st.subheader("Step 1 — Corporate Tax Rate")
    rate_df = pd.DataFrame({
        "Item": ["Company type", "Assessment year", "Banking conditions met?",
                 "Normal rate (non-compliant)", "Reduced rate (compliant)", "Rate applied"],
        "Value": [V("company_type"), ay, str(V("banking_conditions_met")),
                  pct(r["normal_rate"]), pct(r["reduced_rate"]), r["applied_rate_label"]],
    })
    st.dataframe(rate_df, hide_index=True, use_container_width=True)

    st.subheader("Step 2 — Tax on Normal / Business Income")
    row2("Taxable income", r["taxable_income"])
    row2(f"Corporate tax @ {r['applied_rate']:.1f}%", r["gross_tax_normal"])
    if co["has_tobacco_surcharge"]:
        row2("Tobacco surcharge @ 2.5% on tax", r["tobacco_surcharge"])
    row2("Tax on normal income", r["gross_tax_normal"] + r["tobacco_surcharge"], bold=True); divider()

    st.subheader("Step 3 — Capital Gains Tax")
    row2(f"Capital gain on listed shares {bdt(co['capital_gain_listed_shares'])} × 10%", r["cgt_listed"])
    row2(f"Capital gain on other assets {bdt(co['capital_gain_other'])} × 15%", r["cgt_other"])
    row2("Total Capital Gains Tax", r["cgt_listed"] + r["cgt_other"], bold=True); divider()

    st.markdown(f"### Gross Tax (normal + CGT): {bdt(r['gross_tax'])}"); double_divider()

    st.subheader("Step 4 — Three-Way Test (Minimum Tax on Gross Receipts)")
    st.info(
        "Under ITA 2023, the final tax liability is the **higher** of: "
        "(A) Tax on taxable income (slab/rate) and (B) Minimum tax on gross receipts. "
        "The minimum tax applies if gross receipts > BDT 50 lakh (BDT 5 million)."
    )
    three_way_df = pd.DataFrame({
        "Test": [
            f"(A) Tax on taxable income @ {r['applied_rate']:.1f}% + CGT",
            f"(B) Min. tax on gross receipts {bdt(r['total_gross_receipts'])} @ {r['min_tax_rate']*100:.2f}%",
            "FINAL TAX (higher of A and B)",
        ],
        "Amount (BDT)": [
            f"{r['gross_tax']:,.0f}",
            f"{r['min_tax_gross_receipts']:,.0f}",
            f"{r['final_tax_before_credits']:,.0f}",
        ],
        "Status": [
            "✅ APPLIES" if not r["min_tax_applied"] else "",
            "✅ APPLIES (MINIMUM TAX)" if r["min_tax_applied"] else "",
            "",
        ],
    })
    st.dataframe(three_way_df, hide_index=True, use_container_width=True)

    if r["min_tax_applied"]:
        st.warning(
            f"⚠️ Minimum tax ({pct(r['min_tax_rate']*100)} on gross receipts) = "
            f"{bdt(r['min_tax_gross_receipts'])} is **higher** than tax on income = "
            f"{bdt(r['gross_tax'])}. Minimum tax applies."
        )
    else:
        st.success(
            f"✅ Tax on income {bdt(r['gross_tax'])} > minimum tax {bdt(r['min_tax_gross_receipts'])}. "
            f"Normal tax applies."
        )

    st.markdown(f"### FINAL TAX LIABILITY:  {bdt(r['final_tax_before_credits'])}"); double_divider()

    if r["foreign_emp_tax"] > 0:
        st.error(
            f"⚠️ Additional Tax for Unauthorised Foreign Employees: "
            f"{co['notes_foreign_employees']} employee(s) × 50% of annual tax or BDT 5,00,000 "
            f"(whichever higher) = {bdt(r['foreign_emp_tax'])}"
        )

    st.subheader("Summary of All Tax Rates — Current Assessment Year")
    all_types = list(CORP_RATES.keys())
    summary_rows = []
    for et in all_types:
        nr, rr, rl = CORP_RATES[et][ay]
        summary_rows.append({"Entity Type": et, "Normal Rate": pct(nr), "Reduced Rate (if banking conditions)": rl})
    st.dataframe(pd.DataFrame(summary_rows), hide_index=True, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# TAB 4 — TDS & CREDITS
# ═══════════════════════════════════════════════════════════════════════════
with tabs[4]:
    st.header("💸 TDS, Advance Tax & Final Tax Reconciliation")
    st.caption("All TDS and advance tax paid are credits against the final corporate tax liability")

    st.subheader("A. TDS Deducted at Source (Received by Company)")
    tds_df = pd.DataFrame({
        "TDS Type": [
            "TDS on Sales Receipts (Sec 82C — by buyers)",
            "TDS on Services (withheld by clients)",
            "TDS / AT on Import",
            "TDS on Export Proceeds",
            "TDS on Bank Interest (10%)",
            "TDS on Rent Paid to Company",
            "TDS on Dividend Received",
            "TDS — Other",
            "TOTAL TDS",
        ],
        "Amount (BDT)": [
            co["tds_on_sales_receipts"], co["tds_on_services_received"], co["tds_on_import"],
            co["tds_on_export_proceeds"], co["tds_on_bank_interest"], co["tds_on_rent_paid"],
            co["tds_on_dividend"], co["tds_other"], r["total_tds"],
        ],
    })
    st.dataframe(tds_df, hide_index=True, use_container_width=True)

    st.subheader("B. Advance Tax Paid (4 Quarterly Installments)")
    adv_df = pd.DataFrame({
        "Quarter": ["Q1 — 15 September", "Q2 — 15 December", "Q3 — 15 March", "Q4 — 15 June", "Total Advance Tax"],
        "Amount (BDT)": [co["advance_tax_q1"], co["advance_tax_q2"], co["advance_tax_q3"],
                         co["advance_tax_q4"], r["total_advance_tax"]],
    })
    st.dataframe(adv_df, hide_index=True, use_container_width=True)

    st.markdown("---")
    st.subheader("C. Final Reconciliation")
    row2("Final Tax Liability (per computation)", r["final_tax_before_credits"], bold=True); divider()
    row2("Less: Total TDS credits", -r["total_tds"])
    row2("Less: Total Advance Tax", -r["total_advance_tax"])
    row2("Less: Tax paid with return (challan)", -co["tax_paid_with_return"]); divider()

    net = r["net_tax_payable"]
    ref = r["refund_due"]
    if net > 0:
        st.error(f"### 🔴 Net Tax Payable with Return:  {bdt(net)}")
    elif ref > 0:
        st.success(f"### 🟢 Refund Due:  {bdt(ref)}")
    else:
        st.success("### ✅ Fully settled — No additional tax payable")

    st.subheader("D. Common TDS Rates Reference (ITA 2023 / FY 2025-26)")
    tds_ref_df = pd.DataFrame({
        "Payment Type": [
            "Sale of goods — TDS by buyer (Sec 82C)",
            "Professional / Technical services",
            "Contractor / supplier",
            "Rent (building) — deducted by tenant",
            "Interest on bank deposits",
            "Dividend to resident company",
            "Dividend to non-resident",
            "Royalty / technical fees to non-resident",
            "Import at C&F value",
            "Salary (deducted by employer)",
        ],
        "TDS Rate": ["1–7% (varies)", "10%", "3–7%", "5%", "10%", "20%", "20–30%", "20%", "3–5%", "slab rates"],
        "Section": ["82C", "52A", "52", "53A", "53F", "54", "54", "55A", "53BB", "50"],
    })
    st.dataframe(tds_ref_df, hide_index=True, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# TAB 5 — INCENTIVES & HOLIDAYS
# ═══════════════════════════════════════════════════════════════════════════
with tabs[5]:
    st.header("🏭 Special Incentives, Tax Holidays & Reduced Rates")
    st.caption("ITA 2023 | NBR SROs | Bangladesh Investment Development Authority (BIDA)")

    st.subheader("1. Tax Holiday Provisions (ITA 2023 & SROs)")
    holiday_df = pd.DataFrame({
        "Sector / Type": [
            "IT / Software / ITES",
            "Export-Oriented RMG (100% export)",
            "Power Generation (gas-based, SRO)",
            "Power Generation (renewable / solar)",
            "Private power (coal-excluded)",
            "SEZ / Export Processing Zone",
            "Hi-Tech Park",
            "Agro-processing industries",
            "Garment & Knitwear accessories",
            "Start-ups (registered under ITA 2023)",
        ],
        "Exemption / Holiday": [
            "100% — until 2031 (current SRO)",
            "Full exemption during holiday period",
            "Graduated: 100%→80%→60%→40%→20%",
            "Tax-free for 10 years",
            "Graduated tax holiday 10–15 years",
            "Tax holiday during operation",
            "Tax holiday during operation",
            "Graduated exemption (NBR notification)",
            "Reduced rate",
            "Various concessions — report to NBR",
        ],
        "Condition": [
            "Must be in designated tech parks",
            "100% export income",
            "Specific SRO approval required",
            "SRO / BIDA approval",
            "Approval from BPDB / BIDA",
            "BEZA membership",
            "Hi-Tech Park Authority",
            "NBR approval",
            "Export condition",
            "Registration under ITA 2023",
        ],
    })
    st.dataframe(holiday_df, hide_index=True, use_container_width=True)

    st.subheader("2. Current Company — Tax Holiday Status")
    if co["has_tax_holiday"]:
        c1, c2, c3 = st.columns(3)
        c1.metric("Holiday Type", co["tax_holiday_type"])
        c2.metric("Years Remaining", co["tax_holiday_years_remaining"])
        c3.metric("Exempt Income", bdt(co["tax_holiday_income_amount"]))
        st.success(f"Tax holiday active: {bdt(co['tax_holiday_income_amount'])} of income is exempt from corporate tax.")
    else:
        st.info("No tax holiday entered. Toggle 'Company has a tax holiday' in Inputs tab.")

    st.subheader("3. Banking Channel Compliance Conditions")
    st.markdown(
        "Companies must meet **all** of the following to qualify for reduced (lower) corporate tax rates:\n\n"
        "1. All **receipts and income** must be received via bank transfer\n"
        "2. All **payments and investments** individually exceeding BDT 5,00,000 (or BDT 36,00,000 annually in aggregate) must be via bank transfer\n"
        "3. Annual income tax return must be filed on time\n"
        "4. Audited financial statements must be maintained\n\n"
        "**Non-compliance:** Tax is assessed at the **higher (normal) rate** and the excess is treated as special business income."
    )
    if co["banking_conditions_met"]:
        st.success(f"✅ Banking conditions met — Reduced rate of {r['reduced_rate']:.1f}% applies")
    else:
        st.error(f"❌ Banking conditions NOT met — Normal rate of {r['normal_rate']:.1f}% applies (difference = {r['normal_rate'] - r['reduced_rate']:.1f}%)")
        potential_saving = r["taxable_income"] * (r["normal_rate"] - r["reduced_rate"]) / 100
        st.warning(f"Potential tax saving if banking conditions are met: {bdt(potential_saving)}")

    st.subheader("4. Start-up Concessions (ITA 2023)")
    st.markdown(
        "Start-ups registered under ITA 2023 that grant the income tax authority permanent access to their systems:\n"
        "- Relieved from routine reporting requirements (but must still file returns)\n"
        "- May qualify for income tax exemptions in defined 'growth years'\n"
        "- First 3 income years: 0.10% minimum tax on gross receipts (vs. standard 0.6%/1%)\n"
        "- Certain deductions and concessions available — consult NBR notification"
    )

    st.subheader("5. Export Income — Special Treatment")
    st.markdown(
        "- Export-oriented companies may receive **cash incentives / subsidies** (treated as income but separately considered)\n"
        "- Tax rebate on export income: enter percentage in Inputs tab\n"
        "- 100% export revenue companies may qualify for full tax holidays\n"
        "- TDS on export proceeds at reduced rates (check latest NBR circular)"
    )

# ═══════════════════════════════════════════════════════════════════════════
# TAB 6 — RETURN SUMMARY
# ═══════════════════════════════════════════════════════════════════════════
with tabs[6]:
    st.header("🗒️ Corporate Income Tax Return Summary")
    st.caption(f"{V('company_name')}  |  TIN: {V('tin')}  |  {ay}  |  Year end: {V('income_year_end')}")

    st.subheader("A. Gross Receipts & Accounting Profit")
    a_df = pd.DataFrame({
        "Item": ["Total Operating Revenue", "Total Non-Operating Income",
                 "Total Gross Receipts", "Total Operating Expenses", "Finance Costs",
                 "Accounting Depreciation", "ACCOUNTING PROFIT"],
        "BDT": [r["operating_revenue"], r["total_non_op_income"], r["total_gross_receipts"],
                -r["total_operating_exp"], -r["total_finance_cost"],
                -co["accounting_depreciation"], r["accounting_profit"]],
    })
    st.dataframe(a_df, hide_index=True, use_container_width=True)

    st.subheader("B. Statutory Taxable Income")
    b_df = pd.DataFrame({
        "Adjustment": [
            "Accounting Profit", "Add: Book depreciation reversed",
            "Less: Tax depreciation (Sch. 3)", "Add: Total disallowances / add-backs",
            "Less: Special deductions", "Less: Exempt income",
            "Statutory Profit (before losses)", "Less: B/F business loss set-off",
            "Less: Unabsorbed depreciation set-off",
            "Less: Tax holiday / exempt income", "TAXABLE INCOME",
        ],
        "BDT": [
            r["accounting_profit"], co["accounting_depreciation"],
            -r["total_tax_depr"], r["total_addbacks"],
            -r["total_special_dedns"], -r["total_exempt"],
            r["statutory_profit"], -r["set_off_business_loss"],
            -r["set_off_unabsorbed_dep"],
            -r["tax_holiday_income"], r["taxable_income"],
        ],
    })
    st.dataframe(b_df, hide_index=True, use_container_width=True)

    st.subheader("C. Tax Computation")
    c_df = pd.DataFrame({
        "Item": [
            f"Corporate tax on taxable income @ {r['applied_rate']:.1f}%",
            "Tobacco surcharge @ 2.5% (if applicable)",
            "Capital gains tax — listed shares @ 10%",
            "Capital gains tax — other assets @ 15%",
            "Gross Tax",
            f"Minimum tax on gross receipts @ {r['min_tax_rate']*100:.2f}%",
            "FINAL TAX LIABILITY (higher of gross tax or minimum tax)",
        ],
        "BDT": [
            r["gross_tax_normal"], r["tobacco_surcharge"],
            r["cgt_listed"], r["cgt_other"], r["gross_tax"],
            r["min_tax_gross_receipts"], r["final_tax_before_credits"],
        ],
        "Note": [
            r["applied_rate_label"], "Only for tobacco companies", "Resident company rate",
            "Flat 15%", "", f"GR = {bdt(r['total_gross_receipts'])}",
            "✅ MINIMUM TAX" if r["min_tax_applied"] else "✅ NORMAL TAX",
        ],
    })
    st.dataframe(c_df, hide_index=True, use_container_width=True)

    st.subheader("D. TDS Credits & Balance Tax")
    d_df = pd.DataFrame({
        "Item": [
            "Final tax liability",
            "Less: TDS on sales receipts",
            "Less: TDS on services",
            "Less: TDS on imports",
            "Less: TDS on bank interest",
            "Less: TDS — others",
            "Less: Advance tax (4 installments)",
            "Less: Tax paid with return",
            "NET TAX PAYABLE / (REFUND)",
        ],
        "BDT": [
            r["final_tax_before_credits"],
            -co["tds_on_sales_receipts"], -co["tds_on_services_received"],
            -co["tds_on_import"], -co["tds_on_bank_interest"],
            -(co["tds_on_export_proceeds"]+co["tds_on_rent_paid"]+co["tds_on_dividend"]+co["tds_other"]),
            -r["total_advance_tax"], -co["tax_paid_with_return"],
            r["net_tax_payable"] - r["refund_due"],
        ],
    })
    st.dataframe(d_df, hide_index=True, use_container_width=True)

    net = r["net_tax_payable"]
    ref = r["refund_due"]
    if net > 0:
        st.error(f"### 🔴 Tax Payable with Return: {bdt(net)}")
    elif ref > 0:
        st.success(f"### 🟢 Refund Due: {bdt(ref)}")
    else:
        st.success("### ✅ No tax payable or refundable")

    st.subheader("E. Key Metrics")
    metrics_df = pd.DataFrame({
        "Metric": [
            "Gross Receipts", "Accounting Profit", "Taxable Income",
            "Effective Tax Rate", "Minimum Tax Rate (GR basis)",
            "Tax Rate Applied", "Banking Conditions Met",
        ],
        "Value": [
            bdt(r["total_gross_receipts"]), bdt(r["accounting_profit"]),
            bdt(r["taxable_income"]), pct(r["eff_rate"]),
            pct(r["min_tax_rate"] * 100), r["applied_rate_label"],
            "Yes" if co["banking_conditions_met"] else "No",
        ],
    })
    st.dataframe(metrics_df, hide_index=True, use_container_width=True)

    st.subheader("F. Compliance Notes")
    st.markdown(
        f"- **Filing Deadline:** 15 July of the assessment year (if fiscal year = Jan–Dec). "
        f"For other year-ends, within 6 months of year-end.\n"
        f"- **Advance Tax:** 4 quarterly installments — 15 Sep, 15 Dec, 15 Mar, 15 Jun.\n"
        f"- **Late filing penalty:** Disallowance of certain deductions + interest @ 2% per month.\n"
        f"- **WHT compliance (Sec 55):** Entire expense disallowed if TDS not deducted & deposited.\n"
        f"- **PSR (Proof of Submission of Return):** Required for LC opening, govt. contracts, etc.\n"
        f"- **Audited accounts:** Mandatory for all companies (RJSC requirement).\n"
        f"- **Transfer pricing:** Arm's-length standard applies to transactions with foreign affiliates.\n"
        f"- **NBR e-filing portal:** etaxnbr.gov.bd"
    )

# ═══════════════════════════════════════════════════════════════════════════
# TAB 7 — CORPORATE TAX GUIDE
# ═══════════════════════════════════════════════════════════════════════════
with tabs[7]:
    st.header("📚 Bangladesh Corporate Tax — Quick Reference Guide")
    st.caption("Income Tax Act 2023 | Finance Ordinance 2025 | NBR Bangladesh")

    st.subheader("1. Corporate Tax Rates — All Entity Types & Assessment Years")
    all_rows = []
    for etype in CORP_RATES:
        for ayr in list(MIN_TAX_RATES.keys()):
            nr, rr, rl = CORP_RATES[etype][ayr]
            all_rows.append({"Entity Type": etype, "AY": ayr, "Normal Rate": pct(nr), "Reduced Rate": rl})
    st.dataframe(pd.DataFrame(all_rows), hide_index=True, use_container_width=True)

    st.subheader("2. Minimum Tax on Gross Receipts")
    st.markdown(
        "Applies to all companies/firms with gross receipts > BDT 50 lakh (BDT 5 million).\n\n"
        "| Entity Category | AY 2024-25 | AY 2025-26 onwards |\n"
        "|---|---|---|\n"
        "| General companies | 0.60% | 1.00% |\n"
        "| Tobacco / cigarette manufacturers | 1.00% | 1.00% |\n"
        "| Mobile phone operators | 2.00% | 2.00% |\n"
        "| Manufacturers — first 3 income years | 0.10% | 0.10% |\n"
    )

    st.subheader("3. Allowable Deductions — Key Rules")
    st.markdown(
        "| Expense | Rule / Limit |\n"
        "|---|---|\n"
        "| Salaries & wages | Fully deductible if paid via bank (>BDT 20,000/month) |\n"
        "| Cash payment — single transaction | Disallowed if > BDT 50,000 |\n"
        "| Cash payment — annual aggregate | Disallowed if > BDT 5,00,000 |\n"
        "| Employee perquisites (non-cash) | Capped at BDT 10,00,000 per employee per year |\n"
        "| Foreign travel | Max 1.25% of disclosed turnover |\n"
        "| Advertising & promotion | Max 0.50% of disclosed turnover |\n"
        "| Donation (approved institution) | Max 10% of net profit (first 3 yrs) or 8% thereafter |\n"
        "| Bad debts | Specific write-off only (general provisions disallowed) |\n"
        "| Pre-commencement expenses | Amortized at 20% straight-line |\n"
        "| Interest on loans | Allowable; must be capitalized before asset put to use |\n"
        "| Vehicle depreciation | Cost base capped at BDT 30,00,000 |\n"
        "| Fines & penalties | Always disallowed |\n"
        "| Expenses — TDS not deducted | Entire expense disallowed (Sec 55) |\n"
    )

    st.subheader("4. Tax Depreciation Rates (Schedule 3, ITA 2023)")
    depr_df = pd.DataFrame({
        "Asset Category": list(DEPR_RATES.keys()),
        "Rate (%)": list(DEPR_RATES.values()),
        "Method": ["Reducing Balance"] * (len(DEPR_RATES)-1) + ["Straight Line"],
    })
    st.dataframe(depr_df, hide_index=True, use_container_width=True)
    st.caption("Motor vehicle cost base capped at BDT 30,00,000. Unabsorbed depreciation can be carried forward indefinitely.")

    st.subheader("5. Capital Gains Tax")
    st.markdown(
        "| Asset | Rate |\n"
        "|---|---|\n"
        "| Listed shares — Resident company | 10% |\n"
        "| Listed shares — Non-resident | 15% |\n"
        "| Other assets (land, unlisted shares, etc.) | 15% |\n"
        "| Govt. listed securities | Exempt |\n"
    )

    st.subheader("6. Loss Carry-Forward")
    st.markdown(
        "- **Business losses:** May be carried forward and set off against future profits for up to **6 assessment years**\n"
        "- **Unabsorbed depreciation:** May be carried forward **indefinitely** (no time limit)\n"
        "- **Capital losses:** Set off only against capital gains\n"
        "- **No carry-back** of losses to prior years under ITA 2023\n"
        "- Speculation losses: only set off against speculation income"
    )

    st.subheader("7. Transfer Pricing & Foreign Affiliates")
    st.markdown(
        "- Payments to foreign affiliates deductible only if: (a) for business purpose, (b) arm's-length, (c) not capital\n"
        "- Tax withheld as required; otherwise expense is disallowed\n"
        "- Bangladesh has Double Tax Avoidance Treaties (DTAAs) with several countries"
    )

    st.subheader("8. Banking Channel Conditions for Reduced Rate")
    st.markdown(
        "To qualify for the lower corporate tax rate:\n"
        "1. **All receipts:** Must be via bank transfer\n"
        "2. **Payments >BDT 5,00,000** (single) or **>BDT 36,00,000** (aggregate annually): Must be via bank\n"
        "3. Return filed on time\n"
        "4. Audited financial statements maintained\n\n"
        "Non-compliance: Higher rate applies and excess is treated as **special business income** taxable at regular rate."
    )

    st.subheader("9. Key Filing Deadlines")
    st.markdown(
        "| Event | Deadline |\n"
        "|---|---|\n"
        "| Annual return (FY = Jan–Dec) | 15 July of AY |\n"
        "| Annual return (other FY) | Within 6 months of year-end |\n"
        "| Advance tax — Q1 | 15 September |\n"
        "| Advance tax — Q2 | 15 December |\n"
        "| Advance tax — Q3 | 15 March |\n"
        "| Advance tax — Q4 | 15 June |\n"
        "| WHT / TDS deposit | 25th of following month (Finance Ordinance 2025) |\n"
        "| WHT return | Monthly |\n"
    )

    st.subheader("10. Penalties & Consequences")
    st.markdown(
        "| Offence | Consequence |\n"
        "|---|---|\n"
        "| Late filing of return | Deductions disallowed + 2% per month interest |\n"
        "| Failure to deduct TDS (Sec 55) | Entire related expense disallowed |\n"
        "| Cash payment >BDT 50,000 (single) | Expense disallowed |\n"
        "| Unauthorised foreign employees | 50% of annual tax OR BDT 5,00,000 per employee |\n"
        "| Under-declaration of income | Penalty under Sec 127 + back-tax + interest |\n"
        "| Failure to submit WHT returns | Penalty per day of default |\n"
    )

    st.info(
        "**Disclaimer:** This calculator is for educational and planning purposes only. "
        "Corporate tax law changes annually via Finance Acts / Ordinances. "
        "Always consult a qualified Chartered Accountant or tax advisor and refer to "
        "the National Board of Revenue: **nbr.gov.bd** | e-filing: **etaxnbr.gov.bd**"
    )

# ── FOOTER ─────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "🇧🇩 Bangladesh Company Income Tax Calculator | Income Tax Act 2023 | "
    "Finance Ordinance 2025 | All amounts in BDT | "
    "NBR Bangladesh: nbr.gov.bd | e-Filing: etaxnbr.gov.bd"
)