"""
Applied Financial Statements
=============================
A self-contained Streamlit web page that renders a full, interlocking set of
financial statements (Income Statement, Balance Sheet, Cash Flow Statement,
Statement of Retained Earnings, and Notes to the Financial Statements) from a
single "Inputs" tab. Every line item on every statement is wired to the
underlying input values, so changing any number on the Inputs tab flows
through to all five statements instantly.

HOW TO RUN
----------
1. Install dependencies (one time):
       pip install streamlit pandas

2. Run the app:
       streamlit run applied_financial_statements.py

3. Embed in an existing website:
   - Easiest: deploy this app (Streamlit Community Cloud, or any server) and
     embed it in your site with an <iframe src="https://your-app-url"></iframe>.
   - Alternatively, host it behind a reverse proxy (e.g. nginx) at a path
     like yoursite.com/applied-financial-statements and link/iframe to it
     from your existing navigation.

DESIGN NOTES
------------
- All inputs live in `st.session_state["inp"]`, a flat dictionary of floats.
- Every statement is a *pure function* of that dictionary: `build_income_statement()`,
  `build_balance_sheet()`, `build_cash_flow()`, `build_retained_earnings()`.
  None of them store their own numbers - they recompute on every rerun, which
  is what gives the "edit one number, everything updates" behavior for free.
- The Balance Sheet is forced to balance: Cash on the Balance Sheet is NOT a
  free input. It is the output of the Cash Flow Statement (ending cash),
  which in turn depends on the Income Statement and on every other Balance
  Sheet input. This mirrors how real 3-statement models are built, and lets
  you use this page to demonstrate/teach articulation between statements.
- Numbers are entered in "thousands" by default (label says so); change
  UNITS_LABEL if you prefer a different convention.
"""

import streamlit as st
import pandas as pd

UNITS_LABEL = "$ in thousands"

# --------------------------------------------------------------------------
# DEFAULT INPUT VALUES
# Every number that a user can type into the "Inputs" tab lives here.
# Grouping comments map roughly to where each value is used downstream.
# --------------------------------------------------------------------------
DEFAULTS = {
    # ---- Company / period meta ----
    "company_name": "Acme Industrial Holdings, Inc.",
    "fy_label_current": "FY2026",
    "fy_label_prior": "FY2025",
    "reporting_currency": "USD",

    # =========================================================
    # INCOME STATEMENT INPUTS
    # =========================================================
    # --- Revenue ---
    "rev_products": 482_000.0,
    "rev_services": 138_500.0,
    "sales_returns_allowances": 9_400.0,
    "sales_discounts": 5_100.0,

    # --- Cost of Goods Sold ---
    "cogs_materials": 196_000.0,
    "cogs_direct_labor": 84_500.0,
    "cogs_factory_overhead": 47_300.0,
    "cogs_depreciation": 18_200.0,
    "cogs_inventory_writedown": 3_100.0,

    # --- Operating Expenses ---
    "sga_salaries": 61_400.0,
    "sga_marketing": 22_300.0,
    "sga_rd": 31_200.0,
    "sga_depreciation_amortization": 9_800.0,
    "sga_bad_debt_expense": 2_600.0,
    "sga_other": 14_700.0,
    "stock_based_compensation": 11_500.0,
    "restructuring_charges": 6_200.0,
    "impairment_charges": 4_000.0,

    # --- Other Income / (Expense) ---
    "interest_income": 2_300.0,
    "interest_expense": 16_800.0,
    "gain_loss_on_sale_of_assets": 1_100.0,      # positive = gain
    "foreign_exchange_gain_loss": -850.0,         # negative = loss
    "equity_method_income": 1_950.0,
    "other_nonoperating_income_expense": -700.0,

    # --- Discontinued operations & extraordinary-type items ---
    "income_loss_discontinued_ops_pretax": -2_400.0,
    "tax_on_discontinued_ops": -500.0,

    # --- Taxes ---
    "effective_tax_rate_pct": 23.5,
    "deferred_tax_expense_benefit": 1_200.0,      # included within tax expense, disclosed separately

    # --- Noncontrolling interest & preferred dividends ---
    "net_income_attributable_to_nci": 1_850.0,
    "preferred_dividends": 2_000.0,

    # --- Per-share data ---
    "weighted_avg_shares_basic": 48_000.0,        # in thousands of shares
    "dilutive_effect_shares": 1_200.0,

    # =========================================================
    # RETAINED EARNINGS INPUTS
    # =========================================================
    "retained_earnings_beginning": 184_300.0,
    "prior_period_adjustment": -1_500.0,          # net of tax, e.g. error correction
    "cumulative_effect_accounting_change": -800.0,
    "common_dividends_declared": 9_600.0,
    "preferred_dividends_declared": 2_000.0,
    "stock_buyback_retirement_effect_on_re": 3_200.0,  # excess of cost over par charged to RE

    # =========================================================
    # BALANCE SHEET INPUTS  (Cash is solved for - NOT entered here)
    # =========================================================
    # --- Current Assets ---
    "bs_short_term_investments": 18_000.0,
    "bs_accounts_receivable_gross": 76_400.0,
    "bs_allowance_doubtful_accounts": 4_200.0,
    "bs_inventory_raw_materials": 22_000.0,
    "bs_inventory_wip": 14_500.0,
    "bs_inventory_finished_goods": 38_700.0,
    "bs_prepaid_expenses": 7_300.0,
    "bs_other_current_assets": 5_100.0,

    # --- Non-Current Assets ---
    "bs_land": 32_000.0,
    "bs_buildings": 145_000.0,
    "bs_machinery_equipment": 198_500.0,
    "bs_accumulated_depreciation": 96_200.0,
    "bs_operating_lease_rou_asset": 24_600.0,
    "bs_goodwill": 67_000.0,
    "bs_intangible_assets_gross": 41_000.0,
    "bs_accumulated_amortization": 16_400.0,
    "bs_equity_method_investments": 19_800.0,
    "bs_deferred_tax_assets": 6_700.0,
    "bs_other_noncurrent_assets": 4_300.0,

    # --- Current Liabilities ---
    "bs_accounts_payable": 58_200.0,
    "bs_accrued_salaries_benefits": 19_400.0,
    "bs_accrued_interest": 2_100.0,
    "bs_income_taxes_payable": 6_800.0,
    "bs_current_portion_lt_debt": 12_000.0,
    "bs_current_operating_lease_liability": 6_100.0,
    "bs_deferred_revenue_current": 14_300.0,
    "bs_dividends_payable": 2_400.0,
    "bs_other_current_liabilities": 5_600.0,

    # --- Non-Current Liabilities ---
    "bs_long_term_debt": 165_000.0,
    "bs_noncurrent_operating_lease_liability": 19_500.0,
    "bs_deferred_tax_liabilities": 11_200.0,
    "bs_pension_postretirement_liability": 23_800.0,
    "bs_deferred_revenue_noncurrent": 4_900.0,
    "bs_other_noncurrent_liabilities": 3_700.0,

    # --- Equity (non-RE items; RE flows from the RE statement) ---
    "bs_preferred_stock_par": 20_000.0,
    "bs_common_stock_par": 4_800.0,
    "bs_additional_paid_in_capital": 98_750.0,
    "bs_treasury_stock": 38_500.0,                # contra-equity, positive = amount subtracted
    "bs_aoci": -6_300.0,                          # accumulated other comprehensive income/(loss)
    "bs_noncontrolling_interest": 27_400.0,

    # =========================================================
    # CASH FLOW STATEMENT - DIRECT INPUTS NOT ALREADY ON IS/BS
    # =========================================================
    "cf_beginning_cash": 41_200.0,                # also ties to prior-year BS cash
    "cf_depreciation_total": 28_000.0,             # total D (cross-check vs COGS+SGA dep.)
    "cf_amortization_total": 9_000.0,
    "cf_deferred_taxes": 1_200.0,
    "cf_stock_compensation": 11_500.0,
    "cf_provision_for_doubtful_accounts": 2_600.0,
    "cf_impairment_noncash": 4_000.0,
    "cf_gain_on_sale_of_assets_adj": -1_100.0,     # remove gain (non-operating) from CFO
    "cf_equity_method_income_adj": -1_950.0,       # remove equity income, add back distributions
    "cf_equity_method_distributions_received": 1_500.0,
    "cf_change_ar": -8_600.0,                       # negative = increase in AR (use of cash)
    "cf_change_inventory": -5_400.0,
    "cf_change_prepaid": -900.0,
    "cf_change_other_current_assets": -300.0,
    "cf_change_ap": 6_700.0,
    "cf_change_accrued_liabilities": 2_300.0,
    "cf_change_income_taxes_payable": 1_100.0,
    "cf_change_deferred_revenue": 1_800.0,
    "cf_change_other_liabilities": -400.0,
    "cf_pension_contributions": -2_200.0,

    "cf_capex_ppe": -42_000.0,
    "cf_capex_intangibles": -6_500.0,
    "cf_proceeds_sale_of_assets": 3_800.0,
    "cf_acquisitions_net_of_cash": -15_000.0,
    "cf_purchases_of_investments": -9_000.0,
    "cf_maturities_sales_of_investments": 6_000.0,
    "cf_loans_to_related_parties": -1_000.0,

    "cf_proceeds_from_lt_debt": 30_000.0,
    "cf_repayments_of_lt_debt": -18_000.0,
    "cf_proceeds_from_revolver": 12_000.0,
    "cf_repayments_of_revolver": -9_000.0,
    "cf_finance_lease_principal_payments": -2_100.0,
    "cf_proceeds_from_stock_issuance": 4_200.0,
    "cf_repurchase_of_common_stock": -8_900.0,
    "cf_dividends_paid_common": -9_200.0,
    "cf_dividends_paid_preferred": -2_000.0,
    "cf_debt_issuance_costs_paid": -600.0,
    "cf_fx_effect_on_cash": -350.0,

    # =========================================================
    # NOTES - SUPPLEMENTAL / DISCLOSURE-ONLY INPUTS
    # =========================================================
    "note_lease_operating_expense": 7_400.0,
    "note_lease_weighted_avg_term_years": 6.5,
    "note_lease_discount_rate_pct": 5.25,

    "note_debt_interest_rate_pct": 6.10,
    "note_debt_maturity_year_1": 12_000.0,
    "note_debt_maturity_year_2": 14_000.0,
    "note_debt_maturity_year_3": 16_000.0,
    "note_debt_maturity_year_4": 18_000.0,
    "note_debt_maturity_year_5": 20_000.0,
    "note_debt_maturity_thereafter": 97_000.0,

    "note_pension_discount_rate_pct": 4.80,
    "note_pension_expected_return_pct": 6.00,
    "note_pension_benefit_obligation": 58_000.0,
    "note_pension_fair_value_plan_assets": 34_200.0,

    "note_sbc_unrecognized_expense": 18_300.0,
    "note_sbc_weighted_avg_period_years": 2.3,

    "note_contingency_legal_accrual": 1_800.0,
    "note_contingency_disclosed_not_accrued": 5_000.0,

    "note_related_party_transactions": 2_900.0,
    "note_subsequent_event_amount": 0.0,

    "note_segment1_name": "Industrial Products",
    "note_segment1_revenue": 410_000.0,
    "note_segment1_op_income": 58_000.0,
    "note_segment2_name": "Services & Support",
    "note_segment2_revenue": 210_500.0,
    "note_segment2_op_income": 21_300.0,

    "note_effective_tax_rate_statutory_pct": 21.0,
}

# --------------------------------------------------------------------------
# SESSION STATE INITIALISATION
# --------------------------------------------------------------------------
if "inp" not in st.session_state:
    st.session_state["inp"] = DEFAULTS.copy()


def reset_to_defaults():
    st.session_state["inp"] = DEFAULTS.copy()


def I(key):
    """Shorthand getter for an input value."""
    return st.session_state["inp"][key]


# --------------------------------------------------------------------------
# FORMATTING HELPERS
# --------------------------------------------------------------------------
def fmt(x, parens_for_negative=True, decimals=0):
    """Format a number with thousands separators; negatives in parentheses."""
    if x is None:
        return ""
    neg = x < 0
    val = abs(x)
    s = f"{val:,.{decimals}f}"
    if neg and parens_for_negative:
        return f"({s})"
    elif neg:
        return f"-{s}"
    return s


def fmt_pct(x, decimals=1):
    return f"{x:,.{decimals}f}%"


def df_to_statement_table(rows):
    """
    rows: list of tuples (label, value_or_None, style)
      style in {"header","subheader","line","subtotal","total","spacer","note"}
    Returns a pandas DataFrame with a 'Label' and 'Amount' column plus a
    hidden 'Style' column we use for display only (we render manually with
    st.markdown for styling rather than relying on DataFrame styling, since
    that renders more reliably across browsers inside Streamlit).
    """
    return rows


def render_statement(rows, amount_header=None, amount_header2=None):
    """
    Render a list of (label, value, style[, value2]) tuples as a clean
    statement using Streamlit columns - this gives us full control over
    bold/indent/rules without fighting HTML rendering quirks.
    """
    has_two_cols = amount_header2 is not None

    if has_two_cols:
        c1, c2, c3 = st.columns([5, 2, 2])
        c1.markdown(f"**{' '}**")
        c2.markdown(f"**{amount_header}**")
        c3.markdown(f"**{amount_header2}**")
    else:
        c1, c2 = st.columns([5, 2])
        c1.markdown(" ")
        c2.markdown(f"**{amount_header or ''}**")

    st.markdown("<hr style='margin-top:-8px; margin-bottom:6px;'>", unsafe_allow_html=True)

    for row in rows:
        label, value = row[0], row[1]
        style = row[2] if len(row) > 2 else "line"
        value2 = row[3] if len(row) > 3 else None

        if style == "spacer":
            st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
            continue

        if has_two_cols:
            c1, c2, c3 = st.columns([5, 2, 2])
        else:
            c1, c2 = st.columns([5, 2])

        if style == "header":
            c1.markdown(f"#### {label}")
            c2.markdown("")
            if has_two_cols:
                c3.markdown("")
        elif style == "subheader":
            c1.markdown(f"**{label}**")
            c2.markdown("")
            if has_two_cols:
                c3.markdown("")
        elif style == "subtotal":
            c1.markdown(f"**{label}**")
            c2.markdown(f"**{fmt(value)}**")
            if has_two_cols:
                c3.markdown(f"**{fmt(value2)}**" if value2 is not None else "")
            st.markdown("<hr style='margin-top:-6px;margin-bottom:6px;'>", unsafe_allow_html=True)
        elif style == "total":
            c1.markdown(f"### {label}")
            c2.markdown(f"### {fmt(value)}")
            if has_two_cols:
                c3.markdown(f"### {fmt(value2)}" if value2 is not None else "")
            st.markdown("<hr style='border-top:3px double #333;margin-top:-10px;margin-bottom:10px;'>", unsafe_allow_html=True)
        elif style == "note":
            c1.markdown(f"<span style='color:gray;font-size:0.85em'>{label}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span style='color:gray;font-size:0.85em'>{fmt(value) if value is not None else ''}</span>", unsafe_allow_html=True)
            if has_two_cols:
                c3.markdown("")
        else:  # plain line
            c1.markdown(f"&nbsp;&nbsp;&nbsp;{label}", unsafe_allow_html=True)
            c2.markdown(fmt(value) if value is not None else "")
            if has_two_cols:
                c3.markdown(fmt(value2) if value2 is not None else "")


# ==========================================================================
# STATEMENT BUILDERS
# Each function returns a dict of computed totals AND the row list used for
# display, so other statements (e.g. Cash Flow needs Net Income; Balance
# Sheet needs ending Retained Earnings and ending Cash) can consume the
# computed values without re-deriving them.
# ==========================================================================

def build_income_statement():
    d = st.session_state["inp"]

    gross_revenue = d["rev_products"] + d["rev_services"]
    net_revenue = gross_revenue - d["sales_returns_allowances"] - d["sales_discounts"]

    total_cogs = (d["cogs_materials"] + d["cogs_direct_labor"] + d["cogs_factory_overhead"]
                  + d["cogs_depreciation"] + d["cogs_inventory_writedown"])
    gross_profit = net_revenue - total_cogs

    total_sga = (d["sga_salaries"] + d["sga_marketing"] + d["sga_rd"]
                 + d["sga_depreciation_amortization"] + d["sga_bad_debt_expense"] + d["sga_other"])

    total_opex = (total_sga + d["stock_based_compensation"]
                  + d["restructuring_charges"] + d["impairment_charges"])

    operating_income = gross_profit - total_opex

    total_other_income = (d["interest_income"] - d["interest_expense"]
                           + d["gain_loss_on_sale_of_assets"] + d["foreign_exchange_gain_loss"]
                           + d["equity_method_income"] + d["other_nonoperating_income_expense"])

    pretax_income_continuing = operating_income + total_other_income

    tax_expense_continuing = pretax_income_continuing * (d["effective_tax_rate_pct"] / 100.0)
    income_from_continuing_ops = pretax_income_continuing - tax_expense_continuing

    income_loss_discontinued_net = d["income_loss_discontinued_ops_pretax"] - d["tax_on_discontinued_ops"]

    net_income = income_from_continuing_ops + income_loss_discontinued_net

    net_income_attributable_to_company = net_income - d["net_income_attributable_to_nci"]

    net_income_available_to_common = net_income_attributable_to_company - d["preferred_dividends"]

    basic_eps = net_income_available_to_common / d["weighted_avg_shares_basic"] if d["weighted_avg_shares_basic"] else 0
    diluted_shares = d["weighted_avg_shares_basic"] + d["dilutive_effect_shares"]
    diluted_eps = net_income_available_to_common / diluted_shares if diluted_shares else 0

    rows = [
        ("INCOME STATEMENT", None, "header"),
        (f"For the Year Ended — {I('fy_label_current')}", None, "subheader"),
        ("spacer", None, "spacer"),

        ("Revenue", None, "subheader"),
        ("Product revenue", d["rev_products"], "line"),
        ("Service revenue", d["rev_services"], "line"),
        ("Gross revenue", gross_revenue, "line"),
        ("Less: Sales returns & allowances", -d["sales_returns_allowances"], "line"),
        ("Less: Sales discounts", -d["sales_discounts"], "line"),
        ("Net revenue", net_revenue, "subtotal"),

        ("Cost of Goods Sold", None, "subheader"),
        ("Direct materials", d["cogs_materials"], "line"),
        ("Direct labor", d["cogs_direct_labor"], "line"),
        ("Factory / manufacturing overhead", d["cogs_factory_overhead"], "line"),
        ("Depreciation (cost of sales)", d["cogs_depreciation"], "line"),
        ("Inventory write-down", d["cogs_inventory_writedown"], "line"),
        ("Total cost of goods sold", -total_cogs, "subtotal"),

        ("Gross Profit", gross_profit, "total"),

        ("Operating Expenses", None, "subheader"),
        ("Selling, general & administrative:", None, "line"),
        ("  Salaries & benefits", d["sga_salaries"], "line"),
        ("  Marketing & advertising", d["sga_marketing"], "line"),
        ("  Research & development", d["sga_rd"], "line"),
        ("  Depreciation & amortization", d["sga_depreciation_amortization"], "line"),
        ("  Provision for doubtful accounts", d["sga_bad_debt_expense"], "line"),
        ("  Other SG&A", d["sga_other"], "line"),
        ("Total SG&A", total_sga, "line"),
        ("Stock-based compensation", d["stock_based_compensation"], "line"),
        ("Restructuring charges", d["restructuring_charges"], "line"),
        ("Impairment charges", d["impairment_charges"], "line"),
        ("Total operating expenses", -total_opex, "subtotal"),

        ("Operating Income (EBIT)", operating_income, "total"),

        ("Other Income (Expense)", None, "subheader"),
        ("Interest income", d["interest_income"], "line"),
        ("Interest expense", -d["interest_expense"], "line"),
        ("Gain (loss) on sale of assets", d["gain_loss_on_sale_of_assets"], "line"),
        ("Foreign exchange gain (loss)", d["foreign_exchange_gain_loss"], "line"),
        ("Equity method investment income", d["equity_method_income"], "line"),
        ("Other non-operating income (expense)", d["other_nonoperating_income_expense"], "line"),
        ("Total other income (expense)", total_other_income, "subtotal"),

        ("Income from continuing operations before tax", pretax_income_continuing, "subtotal"),
        ("Income tax expense", -tax_expense_continuing, "line"),
        ("   of which: deferred tax expense (benefit)", d["deferred_tax_expense_benefit"], "note"),
        ("Income from continuing operations", income_from_continuing_ops, "subtotal"),

        ("Discontinued operations, net of tax", income_loss_discontinued_net, "line"),

        ("Net Income", net_income, "total"),
        ("Less: Net income attributable to noncontrolling interests", -d["net_income_attributable_to_nci"], "line"),
        ("Net income attributable to the Company", net_income_attributable_to_company, "subtotal"),
        ("Less: Preferred stock dividends", -d["preferred_dividends"], "line"),
        ("Net income available to common shareholders", net_income_available_to_common, "total"),

        ("Earnings Per Share", None, "subheader"),
        ("Basic EPS", basic_eps, "line"),
        ("Diluted EPS", diluted_eps, "line"),
        ("Weighted average shares — basic", d["weighted_avg_shares_basic"], "line"),
        ("Weighted average shares — diluted", diluted_shares, "line"),
    ]

    return {
        "rows": rows,
        "gross_revenue": gross_revenue,
        "net_revenue": net_revenue,
        "total_cogs": total_cogs,
        "gross_profit": gross_profit,
        "total_sga": total_sga,
        "total_opex": total_opex,
        "operating_income": operating_income,
        "total_other_income": total_other_income,
        "pretax_income_continuing": pretax_income_continuing,
        "tax_expense_continuing": tax_expense_continuing,
        "income_from_continuing_ops": income_from_continuing_ops,
        "income_loss_discontinued_net": income_loss_discontinued_net,
        "net_income": net_income,
        "net_income_attributable_to_company": net_income_attributable_to_company,
        "net_income_available_to_common": net_income_available_to_common,
        "basic_eps": basic_eps,
        "diluted_eps": diluted_eps,
    }


def build_retained_earnings(income_statement):
    d = st.session_state["inp"]
    ni_company = income_statement["net_income_attributable_to_company"]

    beg_re = d["retained_earnings_beginning"]
    adj_beg_re = beg_re + d["prior_period_adjustment"] + d["cumulative_effect_accounting_change"]

    total_dividends = d["common_dividends_declared"] + d["preferred_dividends_declared"]

    ending_re = (adj_beg_re + ni_company - total_dividends
                 - d["stock_buyback_retirement_effect_on_re"])

    rows = [
        ("STATEMENT OF RETAINED EARNINGS", None, "header"),
        (f"For the Year Ended — {I('fy_label_current')}", None, "subheader"),
        ("spacer", None, "spacer"),

        ("Retained earnings, beginning of period (as previously reported)", beg_re, "line"),
        ("Prior period adjustment (net of tax)", d["prior_period_adjustment"], "line"),
        ("Cumulative effect of accounting change (net of tax)", d["cumulative_effect_accounting_change"], "line"),
        ("Retained earnings, beginning of period (as adjusted)", adj_beg_re, "subtotal"),

        ("Add: Net income attributable to the Company", ni_company, "line"),

        ("Less: Dividends declared", None, "line"),
        ("   Common stock dividends", -d["common_dividends_declared"], "line"),
        ("   Preferred stock dividends", -d["preferred_dividends_declared"], "line"),

        ("Less: Excess of repurchase cost over par (treasury retirement)", -d["stock_buyback_retirement_effect_on_re"], "line"),

        ("Retained Earnings, End of Period", ending_re, "total"),
    ]

    return {"rows": rows, "ending_re": ending_re, "beg_re": beg_re, "adj_beg_re": adj_beg_re,
            "total_dividends": total_dividends}


def build_cash_flow(income_statement):
    d = st.session_state["inp"]
    ni = income_statement["net_income"]

    # --- Operating activities ---
    noncash_adjustments = (
        d["cf_depreciation_total"] + d["cf_amortization_total"] + d["cf_deferred_taxes"]
        + d["cf_stock_compensation"] + d["cf_provision_for_doubtful_accounts"]
        + d["cf_impairment_noncash"] + d["cf_gain_on_sale_of_assets_adj"]
        + d["cf_equity_method_income_adj"] + d["cf_equity_method_distributions_received"]
    )

    wc_changes = (
        d["cf_change_ar"] + d["cf_change_inventory"] + d["cf_change_prepaid"]
        + d["cf_change_other_current_assets"] + d["cf_change_ap"]
        + d["cf_change_accrued_liabilities"] + d["cf_change_income_taxes_payable"]
        + d["cf_change_deferred_revenue"] + d["cf_change_other_liabilities"]
        + d["cf_pension_contributions"]
    )

    cfo = ni + noncash_adjustments + wc_changes

    # --- Investing activities ---
    cfi = (
        d["cf_capex_ppe"] + d["cf_capex_intangibles"] + d["cf_proceeds_sale_of_assets"]
        + d["cf_acquisitions_net_of_cash"] + d["cf_purchases_of_investments"]
        + d["cf_maturities_sales_of_investments"] + d["cf_loans_to_related_parties"]
    )

    # --- Financing activities ---
    cff = (
        d["cf_proceeds_from_lt_debt"] + d["cf_repayments_of_lt_debt"]
        + d["cf_proceeds_from_revolver"] + d["cf_repayments_of_revolver"]
        + d["cf_finance_lease_principal_payments"] + d["cf_proceeds_from_stock_issuance"]
        + d["cf_repurchase_of_common_stock"] + d["cf_dividends_paid_common"]
        + d["cf_dividends_paid_preferred"] + d["cf_debt_issuance_costs_paid"]
    )

    fx_effect = d["cf_fx_effect_on_cash"]

    net_change_in_cash = cfo + cfi + cff + fx_effect
    beginning_cash = d["cf_beginning_cash"]
    ending_cash = beginning_cash + net_change_in_cash

    rows = [
        ("STATEMENT OF CASH FLOWS", None, "header"),
        (f"For the Year Ended — {I('fy_label_current')}  (Indirect Method)", None, "subheader"),
        ("spacer", None, "spacer"),

        ("Cash Flows from Operating Activities", None, "subheader"),
        ("Net income", ni, "line"),
        ("Adjustments to reconcile net income to net cash provided by operations:", None, "line"),
        ("  Depreciation expense", d["cf_depreciation_total"], "line"),
        ("  Amortization expense", d["cf_amortization_total"], "line"),
        ("  Deferred income taxes", d["cf_deferred_taxes"], "line"),
        ("  Stock-based compensation", d["cf_stock_compensation"], "line"),
        ("  Provision for doubtful accounts", d["cf_provision_for_doubtful_accounts"], "line"),
        ("  Impairment charges (non-cash)", d["cf_impairment_noncash"], "line"),
        ("  Gain on sale of assets (removed)", d["cf_gain_on_sale_of_assets_adj"], "line"),
        ("  Equity method income (removed)", d["cf_equity_method_income_adj"], "line"),
        ("  Distributions received from equity method investees", d["cf_equity_method_distributions_received"], "line"),
        ("Changes in operating assets & liabilities:", None, "line"),
        ("  (Increase) decrease in accounts receivable", d["cf_change_ar"], "line"),
        ("  (Increase) decrease in inventory", d["cf_change_inventory"], "line"),
        ("  (Increase) decrease in prepaid expenses", d["cf_change_prepaid"], "line"),
        ("  (Increase) decrease in other current assets", d["cf_change_other_current_assets"], "line"),
        ("  Increase (decrease) in accounts payable", d["cf_change_ap"], "line"),
        ("  Increase (decrease) in accrued liabilities", d["cf_change_accrued_liabilities"], "line"),
        ("  Increase (decrease) in income taxes payable", d["cf_change_income_taxes_payable"], "line"),
        ("  Increase (decrease) in deferred revenue", d["cf_change_deferred_revenue"], "line"),
        ("  Increase (decrease) in other liabilities", d["cf_change_other_liabilities"], "line"),
        ("  Pension contributions", d["cf_pension_contributions"], "line"),
        ("Net Cash Provided by Operating Activities", cfo, "total"),

        ("Cash Flows from Investing Activities", None, "subheader"),
        ("Purchases of property, plant & equipment", d["cf_capex_ppe"], "line"),
        ("Purchases / development of intangible assets", d["cf_capex_intangibles"], "line"),
        ("Proceeds from sale of property & equipment", d["cf_proceeds_sale_of_assets"], "line"),
        ("Acquisitions, net of cash acquired", d["cf_acquisitions_net_of_cash"], "line"),
        ("Purchases of investments", d["cf_purchases_of_investments"], "line"),
        ("Maturities / sales of investments", d["cf_maturities_sales_of_investments"], "line"),
        ("Loans to related parties", d["cf_loans_to_related_parties"], "line"),
        ("Net Cash Used in Investing Activities", cfi, "total"),

        ("Cash Flows from Financing Activities", None, "subheader"),
        ("Proceeds from issuance of long-term debt", d["cf_proceeds_from_lt_debt"], "line"),
        ("Repayments of long-term debt", d["cf_repayments_of_lt_debt"], "line"),
        ("Proceeds from revolving credit facility", d["cf_proceeds_from_revolver"], "line"),
        ("Repayments of revolving credit facility", d["cf_repayments_of_revolver"], "line"),
        ("Finance lease principal payments", d["cf_finance_lease_principal_payments"], "line"),
        ("Proceeds from issuance of common stock", d["cf_proceeds_from_stock_issuance"], "line"),
        ("Repurchase of common stock (treasury)", d["cf_repurchase_of_common_stock"], "line"),
        ("Dividends paid — common", d["cf_dividends_paid_common"], "line"),
        ("Dividends paid — preferred", d["cf_dividends_paid_preferred"], "line"),
        ("Debt issuance costs paid", d["cf_debt_issuance_costs_paid"], "line"),
        ("Net Cash Used in Financing Activities", cff, "total"),

        ("Effect of exchange rate changes on cash", fx_effect, "line"),
        ("Net Increase (Decrease) in Cash", net_change_in_cash, "subtotal"),
        ("Cash, beginning of period", beginning_cash, "line"),
        ("Cash, End of Period", ending_cash, "total"),

        ("Supplemental Disclosures", None, "subheader"),
        ("Cash paid for interest", d["interest_expense"] if "interest_expense" in d else None, "note"),
        ("Cash paid for income taxes", income_statement["tax_expense_continuing"], "note"),
    ]

    return {
        "rows": rows,
        "cfo": cfo, "cfi": cfi, "cff": cff, "fx_effect": fx_effect,
        "net_change_in_cash": net_change_in_cash,
        "beginning_cash": beginning_cash, "ending_cash": ending_cash,
        "noncash_adjustments": noncash_adjustments, "wc_changes": wc_changes,
    }


def build_balance_sheet(retained_earnings, cash_flow):
    d = st.session_state["inp"]
    ending_cash = cash_flow["ending_cash"]
    ending_re = retained_earnings["ending_re"]

    # --- Current Assets ---
    net_ar = d["bs_accounts_receivable_gross"] - d["bs_allowance_doubtful_accounts"]
    total_inventory = d["bs_inventory_raw_materials"] + d["bs_inventory_wip"] + d["bs_inventory_finished_goods"]
    total_current_assets = (ending_cash + d["bs_short_term_investments"] + net_ar + total_inventory
                             + d["bs_prepaid_expenses"] + d["bs_other_current_assets"])

    # --- Non-Current Assets ---
    gross_ppe = d["bs_land"] + d["bs_buildings"] + d["bs_machinery_equipment"]
    net_ppe = gross_ppe - d["bs_accumulated_depreciation"]
    net_intangibles = d["bs_intangible_assets_gross"] - d["bs_accumulated_amortization"]

    total_noncurrent_assets = (net_ppe + d["bs_operating_lease_rou_asset"] + d["bs_goodwill"]
                                + net_intangibles + d["bs_equity_method_investments"]
                                + d["bs_deferred_tax_assets"] + d["bs_other_noncurrent_assets"])

    total_assets = total_current_assets + total_noncurrent_assets

    # --- Current Liabilities ---
    total_current_liabilities = (d["bs_accounts_payable"] + d["bs_accrued_salaries_benefits"]
                                  + d["bs_accrued_interest"] + d["bs_income_taxes_payable"]
                                  + d["bs_current_portion_lt_debt"] + d["bs_current_operating_lease_liability"]
                                  + d["bs_deferred_revenue_current"] + d["bs_dividends_payable"]
                                  + d["bs_other_current_liabilities"])

    # --- Non-Current Liabilities ---
    total_noncurrent_liabilities = (d["bs_long_term_debt"] + d["bs_noncurrent_operating_lease_liability"]
                                     + d["bs_deferred_tax_liabilities"] + d["bs_pension_postretirement_liability"]
                                     + d["bs_deferred_revenue_noncurrent"] + d["bs_other_noncurrent_liabilities"])

    total_liabilities = total_current_liabilities + total_noncurrent_liabilities

    # --- Equity ---
    common_equity_ex_re = (d["bs_common_stock_par"] + d["bs_additional_paid_in_capital"]
                            - d["bs_treasury_stock"] + d["bs_aoci"])

    total_stockholders_equity_attributable = (d["bs_preferred_stock_par"] + common_equity_ex_re + ending_re)

    total_equity = total_stockholders_equity_attributable + d["bs_noncontrolling_interest"]

    total_liabilities_and_equity = total_liabilities + total_equity

    balance_check = total_assets - total_liabilities_and_equity

    rows = [
        ("BALANCE SHEET", None, "header"),
        (f"As of period end — {I('fy_label_current')}", None, "subheader"),
        ("spacer", None, "spacer"),

        ("ASSETS", None, "subheader"),
        ("Current Assets", None, "subheader"),
        ("Cash and cash equivalents  (tied to Cash Flow Statement ending cash)", ending_cash, "line"),
        ("Short-term investments", d["bs_short_term_investments"], "line"),
        ("Accounts receivable, gross", d["bs_accounts_receivable_gross"], "line"),
        ("Less: Allowance for doubtful accounts", -d["bs_allowance_doubtful_accounts"], "line"),
        ("Accounts receivable, net", net_ar, "line"),
        ("Inventory — raw materials", d["bs_inventory_raw_materials"], "line"),
        ("Inventory — work in process", d["bs_inventory_wip"], "line"),
        ("Inventory — finished goods", d["bs_inventory_finished_goods"], "line"),
        ("Total inventory", total_inventory, "line"),
        ("Prepaid expenses", d["bs_prepaid_expenses"], "line"),
        ("Other current assets", d["bs_other_current_assets"], "line"),
        ("Total Current Assets", total_current_assets, "subtotal"),

        ("Non-Current Assets", None, "subheader"),
        ("Land", d["bs_land"], "line"),
        ("Buildings", d["bs_buildings"], "line"),
        ("Machinery & equipment", d["bs_machinery_equipment"], "line"),
        ("Gross property, plant & equipment", gross_ppe, "line"),
        ("Less: Accumulated depreciation", -d["bs_accumulated_depreciation"], "line"),
        ("Property, plant & equipment, net", net_ppe, "line"),
        ("Operating lease right-of-use assets", d["bs_operating_lease_rou_asset"], "line"),
        ("Goodwill", d["bs_goodwill"], "line"),
        ("Intangible assets, gross", d["bs_intangible_assets_gross"], "line"),
        ("Less: Accumulated amortization", -d["bs_accumulated_amortization"], "line"),
        ("Intangible assets, net", net_intangibles, "line"),
        ("Equity method investments", d["bs_equity_method_investments"], "line"),
        ("Deferred tax assets", d["bs_deferred_tax_assets"], "line"),
        ("Other non-current assets", d["bs_other_noncurrent_assets"], "line"),
        ("Total Non-Current Assets", total_noncurrent_assets, "subtotal"),

        ("TOTAL ASSETS", total_assets, "total"),

        ("LIABILITIES", None, "subheader"),
        ("Current Liabilities", None, "subheader"),
        ("Accounts payable", d["bs_accounts_payable"], "line"),
        ("Accrued salaries & benefits", d["bs_accrued_salaries_benefits"], "line"),
        ("Accrued interest", d["bs_accrued_interest"], "line"),
        ("Income taxes payable", d["bs_income_taxes_payable"], "line"),
        ("Current portion of long-term debt", d["bs_current_portion_lt_debt"], "line"),
        ("Current operating lease liability", d["bs_current_operating_lease_liability"], "line"),
        ("Deferred revenue, current", d["bs_deferred_revenue_current"], "line"),
        ("Dividends payable", d["bs_dividends_payable"], "line"),
        ("Other current liabilities", d["bs_other_current_liabilities"], "line"),
        ("Total Current Liabilities", total_current_liabilities, "subtotal"),

        ("Non-Current Liabilities", None, "subheader"),
        ("Long-term debt", d["bs_long_term_debt"], "line"),
        ("Non-current operating lease liability", d["bs_noncurrent_operating_lease_liability"], "line"),
        ("Deferred tax liabilities", d["bs_deferred_tax_liabilities"], "line"),
        ("Pension & post-retirement benefit liability", d["bs_pension_postretirement_liability"], "line"),
        ("Deferred revenue, non-current", d["bs_deferred_revenue_noncurrent"], "line"),
        ("Other non-current liabilities", d["bs_other_noncurrent_liabilities"], "line"),
        ("Total Non-Current Liabilities", total_noncurrent_liabilities, "subtotal"),

        ("TOTAL LIABILITIES", total_liabilities, "total"),

        ("STOCKHOLDERS' EQUITY", None, "subheader"),
        ("Preferred stock, at par", d["bs_preferred_stock_par"], "line"),
        ("Common stock, at par", d["bs_common_stock_par"], "line"),
        ("Additional paid-in capital", d["bs_additional_paid_in_capital"], "line"),
        ("Less: Treasury stock, at cost", -d["bs_treasury_stock"], "line"),
        ("Accumulated other comprehensive income (loss)", d["bs_aoci"], "line"),
        ("Retained earnings  (tied to Statement of Retained Earnings)", ending_re, "line"),
        ("Total Stockholders' Equity attributable to the Company", total_stockholders_equity_attributable, "line"),
        ("Noncontrolling interests", d["bs_noncontrolling_interest"], "line"),
        ("TOTAL EQUITY", total_equity, "subtotal"),

        ("TOTAL LIABILITIES AND EQUITY", total_liabilities_and_equity, "total"),

        ("Balance check (Assets − Liabilities & Equity, should be 0)", balance_check, "note"),
    ]

    return {
        "rows": rows,
        "total_assets": total_assets,
        "total_current_assets": total_current_assets,
        "total_noncurrent_assets": total_noncurrent_assets,
        "total_liabilities": total_liabilities,
        "total_current_liabilities": total_current_liabilities,
        "total_noncurrent_liabilities": total_noncurrent_liabilities,
        "total_equity": total_equity,
        "total_liabilities_and_equity": total_liabilities_and_equity,
        "balance_check": balance_check,
        "net_ppe": net_ppe, "net_ar": net_ar, "total_inventory": total_inventory,
        "gross_ppe": gross_ppe, "net_intangibles": net_intangibles,
    }


def build_notes(income_statement, balance_sheet, cash_flow, retained_earnings):
    d = st.session_state["inp"]

    debt_total = (d["note_debt_maturity_year_1"] + d["note_debt_maturity_year_2"]
                  + d["note_debt_maturity_year_3"] + d["note_debt_maturity_year_4"]
                  + d["note_debt_maturity_year_5"] + d["note_debt_maturity_thereafter"])

    pension_funded_status = d["note_pension_fair_value_plan_assets"] - d["note_pension_benefit_obligation"]

    segment_total_rev = d["note_segment1_revenue"] + d["note_segment2_revenue"]
    segment_total_opinc = d["note_segment1_op_income"] + d["note_segment2_op_income"]

    statutory_vs_effective = d["effective_tax_rate_pct"] - d["note_effective_tax_rate_statutory_pct"]

    return {
        "debt_total": debt_total,
        "pension_funded_status": pension_funded_status,
        "segment_total_rev": segment_total_rev,
        "segment_total_opinc": segment_total_opinc,
        "statutory_vs_effective": statutory_vs_effective,
    }


# ==========================================================================
# SIDEBAR
# ==========================================================================
with st.sidebar:
    st.title("📊 Applied Financial Statements")
    st.caption("A fully-articulated, editable 3-statement model")
    st.markdown("---")
    st.markdown(f"**Units:** {UNITS_LABEL}")
    st.markdown(f"**Currency:** {I('reporting_currency')}")
    st.markdown("---")
    if st.button("🔄 Reset all inputs to default example", use_container_width=True):
        reset_to_defaults()
        st.rerun()
    st.markdown("---")
    st.markdown(
        "**How it works:** Edit any value on the **🧮 Inputs** tab. "
        "Every other tab — Income Statement, Balance Sheet, Cash Flow, "
        "Retained Earnings, and Notes — recalculates automatically because "
        "they are all derived live from the same input values."
    )
    st.markdown("---")
    st.caption("Built with Streamlit · Single-file Python app")

# ==========================================================================
# MAIN PAGE
# ==========================================================================
st.title(I("company_name"))
st.subheader("Applied Financial Statements")
st.caption(f"{UNITS_LABEL} · {I('fy_label_current')} (current year) vs. {I('fy_label_prior')} (prior year reference in Notes)")

tabs = st.tabs([
    "🧮 Inputs",
    "📄 Income Statement",
    "🏛️ Balance Sheet",
    "💵 Cash Flow",
    "📈 Retained Earnings",
    "🗒️ Notes",
])

# --------------------------------------------------------------------------
# TAB 0: INPUTS
# --------------------------------------------------------------------------
with tabs[0]:
    st.header("🧮 Master Inputs")
    st.info(
        "Edit any number below and switch tabs (or just scroll) — the Income "
        "Statement, Balance Sheet, Cash Flow, Retained Earnings, and Notes "
        "tabs all recompute automatically from these values. "
        "**Cash on the Balance Sheet is not entered here** — it is solved "
        "from the Cash Flow Statement, the way it works in a real 3-statement model."
    )

    inp = st.session_state["inp"]

    with st.expander("🏢 Company & Period", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["company_name"] = c1.text_input("Company name", inp["company_name"])
        inp["fy_label_current"] = c2.text_input("Current fiscal year label", inp["fy_label_current"])
        inp["fy_label_prior"] = c3.text_input("Prior fiscal year label", inp["fy_label_prior"])

    with st.expander("📄 Income Statement — Revenue", expanded=False):
        c1, c2 = st.columns(2)
        inp["rev_products"] = c1.number_input("Product revenue", value=inp["rev_products"], step=100.0)
        inp["rev_services"] = c2.number_input("Service revenue", value=inp["rev_services"], step=100.0)
        c1, c2 = st.columns(2)
        inp["sales_returns_allowances"] = c1.number_input("Sales returns & allowances", value=inp["sales_returns_allowances"], step=50.0)
        inp["sales_discounts"] = c2.number_input("Sales discounts", value=inp["sales_discounts"], step=50.0)

    with st.expander("📄 Income Statement — Cost of Goods Sold", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["cogs_materials"] = c1.number_input("Direct materials", value=inp["cogs_materials"], step=100.0)
        inp["cogs_direct_labor"] = c2.number_input("Direct labor", value=inp["cogs_direct_labor"], step=100.0)
        inp["cogs_factory_overhead"] = c3.number_input("Factory overhead", value=inp["cogs_factory_overhead"], step=100.0)
        c1, c2 = st.columns(2)
        inp["cogs_depreciation"] = c1.number_input("Depreciation (COGS)", value=inp["cogs_depreciation"], step=50.0)
        inp["cogs_inventory_writedown"] = c2.number_input("Inventory write-down", value=inp["cogs_inventory_writedown"], step=50.0)

    with st.expander("📄 Income Statement — Operating Expenses", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["sga_salaries"] = c1.number_input("SG&A — Salaries & benefits", value=inp["sga_salaries"], step=100.0)
        inp["sga_marketing"] = c2.number_input("SG&A — Marketing", value=inp["sga_marketing"], step=100.0)
        inp["sga_rd"] = c3.number_input("SG&A — R&D", value=inp["sga_rd"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["sga_depreciation_amortization"] = c1.number_input("SG&A — Depreciation & amortization", value=inp["sga_depreciation_amortization"], step=50.0)
        inp["sga_bad_debt_expense"] = c2.number_input("SG&A — Bad debt expense", value=inp["sga_bad_debt_expense"], step=50.0)
        inp["sga_other"] = c3.number_input("SG&A — Other", value=inp["sga_other"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["stock_based_compensation"] = c1.number_input("Stock-based compensation", value=inp["stock_based_compensation"], step=50.0)
        inp["restructuring_charges"] = c2.number_input("Restructuring charges", value=inp["restructuring_charges"], step=50.0)
        inp["impairment_charges"] = c3.number_input("Impairment charges", value=inp["impairment_charges"], step=50.0)

    with st.expander("📄 Income Statement — Other Income / Expense, Tax, NCI", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["interest_income"] = c1.number_input("Interest income", value=inp["interest_income"], step=50.0)
        inp["interest_expense"] = c2.number_input("Interest expense", value=inp["interest_expense"], step=50.0)
        inp["gain_loss_on_sale_of_assets"] = c3.number_input("Gain (loss) on sale of assets", value=inp["gain_loss_on_sale_of_assets"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["foreign_exchange_gain_loss"] = c1.number_input("FX gain (loss)", value=inp["foreign_exchange_gain_loss"], step=50.0)
        inp["equity_method_income"] = c2.number_input("Equity method income", value=inp["equity_method_income"], step=50.0)
        inp["other_nonoperating_income_expense"] = c3.number_input("Other non-operating income (expense)", value=inp["other_nonoperating_income_expense"], step=50.0)
        c1, c2 = st.columns(2)
        inp["income_loss_discontinued_ops_pretax"] = c1.number_input("Discontinued ops, pre-tax income (loss)", value=inp["income_loss_discontinued_ops_pretax"], step=50.0)
        inp["tax_on_discontinued_ops"] = c2.number_input("Tax on discontinued ops", value=inp["tax_on_discontinued_ops"], step=50.0)
        c1, c2 = st.columns(2)
        inp["effective_tax_rate_pct"] = c1.number_input("Effective tax rate (%)", value=inp["effective_tax_rate_pct"], step=0.5, min_value=0.0, max_value=100.0)
        inp["deferred_tax_expense_benefit"] = c2.number_input("Deferred tax expense (benefit), disclosure only", value=inp["deferred_tax_expense_benefit"], step=50.0)
        c1, c2 = st.columns(2)
        inp["net_income_attributable_to_nci"] = c1.number_input("Net income attributable to NCI", value=inp["net_income_attributable_to_nci"], step=50.0)
        inp["preferred_dividends"] = c2.number_input("Preferred dividends (IS deduction)", value=inp["preferred_dividends"], step=50.0)

    with st.expander("📄 Income Statement — Per-Share Data", expanded=False):
        c1, c2 = st.columns(2)
        inp["weighted_avg_shares_basic"] = c1.number_input("Weighted avg. shares — basic (thousands)", value=inp["weighted_avg_shares_basic"], step=100.0)
        inp["dilutive_effect_shares"] = c2.number_input("Dilutive effect of options/RSUs (thousands)", value=inp["dilutive_effect_shares"], step=50.0)

    with st.expander("📈 Retained Earnings", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["retained_earnings_beginning"] = c1.number_input("Retained earnings, beginning of period", value=inp["retained_earnings_beginning"], step=500.0)
        inp["prior_period_adjustment"] = c2.number_input("Prior period adjustment (net of tax)", value=inp["prior_period_adjustment"], step=50.0)
        inp["cumulative_effect_accounting_change"] = c3.number_input("Cumulative effect of accounting change", value=inp["cumulative_effect_accounting_change"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["common_dividends_declared"] = c1.number_input("Common dividends declared", value=inp["common_dividends_declared"], step=100.0)
        inp["preferred_dividends_declared"] = c2.number_input("Preferred dividends declared", value=inp["preferred_dividends_declared"], step=50.0)
        inp["stock_buyback_retirement_effect_on_re"] = c3.number_input("Treasury retirement excess charged to RE", value=inp["stock_buyback_retirement_effect_on_re"], step=50.0)

    with st.expander("🏛️ Balance Sheet — Current Assets (excl. Cash)", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["bs_short_term_investments"] = c1.number_input("Short-term investments", value=inp["bs_short_term_investments"], step=100.0)
        inp["bs_accounts_receivable_gross"] = c2.number_input("Accounts receivable, gross", value=inp["bs_accounts_receivable_gross"], step=100.0)
        inp["bs_allowance_doubtful_accounts"] = c3.number_input("Allowance for doubtful accounts", value=inp["bs_allowance_doubtful_accounts"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["bs_inventory_raw_materials"] = c1.number_input("Inventory — raw materials", value=inp["bs_inventory_raw_materials"], step=100.0)
        inp["bs_inventory_wip"] = c2.number_input("Inventory — WIP", value=inp["bs_inventory_wip"], step=100.0)
        inp["bs_inventory_finished_goods"] = c3.number_input("Inventory — finished goods", value=inp["bs_inventory_finished_goods"], step=100.0)
        c1, c2 = st.columns(2)
        inp["bs_prepaid_expenses"] = c1.number_input("Prepaid expenses", value=inp["bs_prepaid_expenses"], step=50.0)
        inp["bs_other_current_assets"] = c2.number_input("Other current assets", value=inp["bs_other_current_assets"], step=50.0)
        st.caption("Note: Cash & cash equivalents is computed automatically from the Cash Flow Statement.")

    with st.expander("🏛️ Balance Sheet — Non-Current Assets", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["bs_land"] = c1.number_input("Land", value=inp["bs_land"], step=100.0)
        inp["bs_buildings"] = c2.number_input("Buildings", value=inp["bs_buildings"], step=100.0)
        inp["bs_machinery_equipment"] = c3.number_input("Machinery & equipment", value=inp["bs_machinery_equipment"], step=100.0)
        c1, c2 = st.columns(2)
        inp["bs_accumulated_depreciation"] = c1.number_input("Accumulated depreciation", value=inp["bs_accumulated_depreciation"], step=100.0)
        inp["bs_operating_lease_rou_asset"] = c2.number_input("Operating lease ROU asset", value=inp["bs_operating_lease_rou_asset"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["bs_goodwill"] = c1.number_input("Goodwill", value=inp["bs_goodwill"], step=100.0)
        inp["bs_intangible_assets_gross"] = c2.number_input("Intangible assets, gross", value=inp["bs_intangible_assets_gross"], step=100.0)
        inp["bs_accumulated_amortization"] = c3.number_input("Accumulated amortization", value=inp["bs_accumulated_amortization"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["bs_equity_method_investments"] = c1.number_input("Equity method investments", value=inp["bs_equity_method_investments"], step=100.0)
        inp["bs_deferred_tax_assets"] = c2.number_input("Deferred tax assets", value=inp["bs_deferred_tax_assets"], step=50.0)
        inp["bs_other_noncurrent_assets"] = c3.number_input("Other non-current assets", value=inp["bs_other_noncurrent_assets"], step=50.0)

    with st.expander("🏛️ Balance Sheet — Current Liabilities", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["bs_accounts_payable"] = c1.number_input("Accounts payable", value=inp["bs_accounts_payable"], step=100.0)
        inp["bs_accrued_salaries_benefits"] = c2.number_input("Accrued salaries & benefits", value=inp["bs_accrued_salaries_benefits"], step=100.0)
        inp["bs_accrued_interest"] = c3.number_input("Accrued interest", value=inp["bs_accrued_interest"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["bs_income_taxes_payable"] = c1.number_input("Income taxes payable", value=inp["bs_income_taxes_payable"], step=50.0)
        inp["bs_current_portion_lt_debt"] = c2.number_input("Current portion of LT debt", value=inp["bs_current_portion_lt_debt"], step=100.0)
        inp["bs_current_operating_lease_liability"] = c3.number_input("Current operating lease liability", value=inp["bs_current_operating_lease_liability"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["bs_deferred_revenue_current"] = c1.number_input("Deferred revenue, current", value=inp["bs_deferred_revenue_current"], step=50.0)
        inp["bs_dividends_payable"] = c2.number_input("Dividends payable", value=inp["bs_dividends_payable"], step=50.0)
        inp["bs_other_current_liabilities"] = c3.number_input("Other current liabilities", value=inp["bs_other_current_liabilities"], step=50.0)

    with st.expander("🏛️ Balance Sheet — Non-Current Liabilities", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["bs_long_term_debt"] = c1.number_input("Long-term debt", value=inp["bs_long_term_debt"], step=100.0)
        inp["bs_noncurrent_operating_lease_liability"] = c2.number_input("Non-current operating lease liability", value=inp["bs_noncurrent_operating_lease_liability"], step=100.0)
        inp["bs_deferred_tax_liabilities"] = c3.number_input("Deferred tax liabilities", value=inp["bs_deferred_tax_liabilities"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["bs_pension_postretirement_liability"] = c1.number_input("Pension & post-retirement liability", value=inp["bs_pension_postretirement_liability"], step=100.0)
        inp["bs_deferred_revenue_noncurrent"] = c2.number_input("Deferred revenue, non-current", value=inp["bs_deferred_revenue_noncurrent"], step=50.0)
        inp["bs_other_noncurrent_liabilities"] = c3.number_input("Other non-current liabilities", value=inp["bs_other_noncurrent_liabilities"], step=50.0)

    with st.expander("🏛️ Balance Sheet — Stockholders' Equity (excl. Retained Earnings)", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["bs_preferred_stock_par"] = c1.number_input("Preferred stock, at par", value=inp["bs_preferred_stock_par"], step=100.0)
        inp["bs_common_stock_par"] = c2.number_input("Common stock, at par", value=inp["bs_common_stock_par"], step=100.0)
        inp["bs_additional_paid_in_capital"] = c3.number_input("Additional paid-in capital", value=inp["bs_additional_paid_in_capital"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["bs_treasury_stock"] = c1.number_input("Treasury stock, at cost", value=inp["bs_treasury_stock"], step=100.0)
        inp["bs_aoci"] = c2.number_input("Accumulated other comprehensive income (loss)", value=inp["bs_aoci"], step=50.0)
        inp["bs_noncontrolling_interest"] = c3.number_input("Noncontrolling interest", value=inp["bs_noncontrolling_interest"], step=100.0)
        st.caption("Note: Retained earnings flows automatically from the Statement of Retained Earnings.")

    with st.expander("💵 Cash Flow — Beginning Cash & Operating Adjustments", expanded=False):
        inp["cf_beginning_cash"] = st.number_input("Cash, beginning of period", value=inp["cf_beginning_cash"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_depreciation_total"] = c1.number_input("Depreciation (total, CF add-back)", value=inp["cf_depreciation_total"], step=50.0)
        inp["cf_amortization_total"] = c2.number_input("Amortization (total, CF add-back)", value=inp["cf_amortization_total"], step=50.0)
        inp["cf_deferred_taxes"] = c3.number_input("Deferred taxes (CF add-back)", value=inp["cf_deferred_taxes"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_stock_compensation"] = c1.number_input("Stock-based compensation (CF add-back)", value=inp["cf_stock_compensation"], step=50.0)
        inp["cf_provision_for_doubtful_accounts"] = c2.number_input("Provision for doubtful accounts (CF add-back)", value=inp["cf_provision_for_doubtful_accounts"], step=50.0)
        inp["cf_impairment_noncash"] = c3.number_input("Impairment charges (CF add-back)", value=inp["cf_impairment_noncash"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_gain_on_sale_of_assets_adj"] = c1.number_input("Gain on sale of assets (CF removal, negative)", value=inp["cf_gain_on_sale_of_assets_adj"], step=50.0)
        inp["cf_equity_method_income_adj"] = c2.number_input("Equity method income (CF removal, negative)", value=inp["cf_equity_method_income_adj"], step=50.0)
        inp["cf_equity_method_distributions_received"] = c3.number_input("Distributions received from investees", value=inp["cf_equity_method_distributions_received"], step=50.0)

    with st.expander("💵 Cash Flow — Working Capital Changes", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["cf_change_ar"] = c1.number_input("Change in accounts receivable", value=inp["cf_change_ar"], step=50.0)
        inp["cf_change_inventory"] = c2.number_input("Change in inventory", value=inp["cf_change_inventory"], step=50.0)
        inp["cf_change_prepaid"] = c3.number_input("Change in prepaid expenses", value=inp["cf_change_prepaid"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_change_other_current_assets"] = c1.number_input("Change in other current assets", value=inp["cf_change_other_current_assets"], step=50.0)
        inp["cf_change_ap"] = c2.number_input("Change in accounts payable", value=inp["cf_change_ap"], step=50.0)
        inp["cf_change_accrued_liabilities"] = c3.number_input("Change in accrued liabilities", value=inp["cf_change_accrued_liabilities"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_change_income_taxes_payable"] = c1.number_input("Change in income taxes payable", value=inp["cf_change_income_taxes_payable"], step=50.0)
        inp["cf_change_deferred_revenue"] = c2.number_input("Change in deferred revenue", value=inp["cf_change_deferred_revenue"], step=50.0)
        inp["cf_change_other_liabilities"] = c3.number_input("Change in other liabilities", value=inp["cf_change_other_liabilities"], step=50.0)
        inp["cf_pension_contributions"] = st.number_input("Pension contributions", value=inp["cf_pension_contributions"], step=50.0)

    with st.expander("💵 Cash Flow — Investing Activities", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["cf_capex_ppe"] = c1.number_input("Capex — PP&E purchases", value=inp["cf_capex_ppe"], step=100.0)
        inp["cf_capex_intangibles"] = c2.number_input("Capex — Intangibles", value=inp["cf_capex_intangibles"], step=100.0)
        inp["cf_proceeds_sale_of_assets"] = c3.number_input("Proceeds from sale of assets", value=inp["cf_proceeds_sale_of_assets"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_acquisitions_net_of_cash"] = c1.number_input("Acquisitions, net of cash acquired", value=inp["cf_acquisitions_net_of_cash"], step=100.0)
        inp["cf_purchases_of_investments"] = c2.number_input("Purchases of investments", value=inp["cf_purchases_of_investments"], step=100.0)
        inp["cf_maturities_sales_of_investments"] = c3.number_input("Maturities/sales of investments", value=inp["cf_maturities_sales_of_investments"], step=100.0)
        inp["cf_loans_to_related_parties"] = st.number_input("Loans to related parties", value=inp["cf_loans_to_related_parties"], step=50.0)

    with st.expander("💵 Cash Flow — Financing Activities", expanded=False):
        c1, c2, c3 = st.columns(3)
        inp["cf_proceeds_from_lt_debt"] = c1.number_input("Proceeds from long-term debt", value=inp["cf_proceeds_from_lt_debt"], step=100.0)
        inp["cf_repayments_of_lt_debt"] = c2.number_input("Repayments of long-term debt", value=inp["cf_repayments_of_lt_debt"], step=100.0)
        inp["cf_proceeds_from_revolver"] = c3.number_input("Proceeds from revolver", value=inp["cf_proceeds_from_revolver"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_repayments_of_revolver"] = c1.number_input("Repayments of revolver", value=inp["cf_repayments_of_revolver"], step=100.0)
        inp["cf_finance_lease_principal_payments"] = c2.number_input("Finance lease principal payments", value=inp["cf_finance_lease_principal_payments"], step=50.0)
        inp["cf_proceeds_from_stock_issuance"] = c3.number_input("Proceeds from stock issuance", value=inp["cf_proceeds_from_stock_issuance"], step=50.0)
        c1, c2, c3 = st.columns(3)
        inp["cf_repurchase_of_common_stock"] = c1.number_input("Repurchase of common stock", value=inp["cf_repurchase_of_common_stock"], step=100.0)
        inp["cf_dividends_paid_common"] = c2.number_input("Dividends paid — common", value=inp["cf_dividends_paid_common"], step=50.0)
        inp["cf_dividends_paid_preferred"] = c3.number_input("Dividends paid — preferred", value=inp["cf_dividends_paid_preferred"], step=50.0)
        c1, c2 = st.columns(2)
        inp["cf_debt_issuance_costs_paid"] = c1.number_input("Debt issuance costs paid", value=inp["cf_debt_issuance_costs_paid"], step=50.0)
        inp["cf_fx_effect_on_cash"] = c2.number_input("Effect of exchange rate changes on cash", value=inp["cf_fx_effect_on_cash"], step=50.0)

    with st.expander("🗒️ Notes — Leases, Debt, Pension, SBC, Contingencies, Segments", expanded=False):
        st.markdown("**Leases**")
        c1, c2, c3 = st.columns(3)
        inp["note_lease_operating_expense"] = c1.number_input("Operating lease expense", value=inp["note_lease_operating_expense"], step=50.0)
        inp["note_lease_weighted_avg_term_years"] = c2.number_input("Weighted avg. remaining lease term (yrs)", value=inp["note_lease_weighted_avg_term_years"], step=0.1)
        inp["note_lease_discount_rate_pct"] = c3.number_input("Weighted avg. discount rate (%)", value=inp["note_lease_discount_rate_pct"], step=0.1)

        st.markdown("**Debt maturities (next 5 years + thereafter)**")
        c1, c2, c3 = st.columns(3)
        inp["note_debt_interest_rate_pct"] = c1.number_input("Weighted avg. interest rate on debt (%)", value=inp["note_debt_interest_rate_pct"], step=0.1)
        inp["note_debt_maturity_year_1"] = c2.number_input("Maturities — Year 1", value=inp["note_debt_maturity_year_1"], step=100.0)
        inp["note_debt_maturity_year_2"] = c3.number_input("Maturities — Year 2", value=inp["note_debt_maturity_year_2"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["note_debt_maturity_year_3"] = c1.number_input("Maturities — Year 3", value=inp["note_debt_maturity_year_3"], step=100.0)
        inp["note_debt_maturity_year_4"] = c2.number_input("Maturities — Year 4", value=inp["note_debt_maturity_year_4"], step=100.0)
        inp["note_debt_maturity_year_5"] = c3.number_input("Maturities — Year 5", value=inp["note_debt_maturity_year_5"], step=100.0)
        inp["note_debt_maturity_thereafter"] = st.number_input("Maturities — Thereafter", value=inp["note_debt_maturity_thereafter"], step=100.0)

        st.markdown("**Pension**")
        c1, c2 = st.columns(2)
        inp["note_pension_discount_rate_pct"] = c1.number_input("Discount rate (%)", value=inp["note_pension_discount_rate_pct"], step=0.1)
        inp["note_pension_expected_return_pct"] = c2.number_input("Expected return on plan assets (%)", value=inp["note_pension_expected_return_pct"], step=0.1)
        c1, c2 = st.columns(2)
        inp["note_pension_benefit_obligation"] = c1.number_input("Projected benefit obligation", value=inp["note_pension_benefit_obligation"], step=100.0)
        inp["note_pension_fair_value_plan_assets"] = c2.number_input("Fair value of plan assets", value=inp["note_pension_fair_value_plan_assets"], step=100.0)

        st.markdown("**Stock-Based Compensation**")
        c1, c2 = st.columns(2)
        inp["note_sbc_unrecognized_expense"] = c1.number_input("Unrecognized SBC expense", value=inp["note_sbc_unrecognized_expense"], step=100.0)
        inp["note_sbc_weighted_avg_period_years"] = c2.number_input("Weighted avg. recognition period (yrs)", value=inp["note_sbc_weighted_avg_period_years"], step=0.1)

        st.markdown("**Contingencies & Related Parties**")
        c1, c2, c3 = st.columns(3)
        inp["note_contingency_legal_accrual"] = c1.number_input("Legal contingency accrued", value=inp["note_contingency_legal_accrual"], step=50.0)
        inp["note_contingency_disclosed_not_accrued"] = c2.number_input("Reasonably possible loss, not accrued", value=inp["note_contingency_disclosed_not_accrued"], step=50.0)
        inp["note_related_party_transactions"] = c3.number_input("Related party transactions", value=inp["note_related_party_transactions"], step=50.0)
        inp["note_subsequent_event_amount"] = st.number_input("Subsequent event amount (if any)", value=inp["note_subsequent_event_amount"], step=50.0)

        st.markdown("**Segment Reporting**")
        c1, c2, c3 = st.columns(3)
        inp["note_segment1_name"] = c1.text_input("Segment 1 name", inp["note_segment1_name"])
        inp["note_segment1_revenue"] = c2.number_input("Segment 1 revenue", value=inp["note_segment1_revenue"], step=100.0)
        inp["note_segment1_op_income"] = c3.number_input("Segment 1 operating income", value=inp["note_segment1_op_income"], step=100.0)
        c1, c2, c3 = st.columns(3)
        inp["note_segment2_name"] = c1.text_input("Segment 2 name", inp["note_segment2_name"])
        inp["note_segment2_revenue"] = c2.number_input("Segment 2 revenue", value=inp["note_segment2_revenue"], step=100.0)
        inp["note_segment2_op_income"] = c3.number_input("Segment 2 operating income", value=inp["note_segment2_op_income"], step=100.0)

        inp["note_effective_tax_rate_statutory_pct"] = st.number_input("Statutory tax rate (%), for rate reconciliation", value=inp["note_effective_tax_rate_statutory_pct"], step=0.5)

    st.success("✅ All inputs saved automatically. Switch to any statement tab to see the results update live.")

# ==========================================================================
# BUILD ALL STATEMENTS (single pass, shared across tabs)
# ==========================================================================
IS = build_income_statement()
RE = build_retained_earnings(IS)
CF = build_cash_flow(IS)
BS = build_balance_sheet(RE, CF)
NOTES = build_notes(IS, BS, CF, RE)

# --------------------------------------------------------------------------
# TAB 1: INCOME STATEMENT
# --------------------------------------------------------------------------
with tabs[1]:
    render_statement(IS["rows"], amount_header=I("fy_label_current"))
    with st.expander("📌 Key margins & ratios (auto-calculated)"):
        gm = IS["gross_profit"] / IS["net_revenue"] * 100 if IS["net_revenue"] else 0
        om = IS["operating_income"] / IS["net_revenue"] * 100 if IS["net_revenue"] else 0
        nm = IS["net_income"] / IS["net_revenue"] * 100 if IS["net_revenue"] else 0
        c1, c2, c3 = st.columns(3)
        c1.metric("Gross Margin", fmt_pct(gm))
        c2.metric("Operating Margin", fmt_pct(om))
        c3.metric("Net Margin", fmt_pct(nm))

# --------------------------------------------------------------------------
# TAB 2: BALANCE SHEET
# --------------------------------------------------------------------------
with tabs[2]:
    render_statement(BS["rows"], amount_header=I("fy_label_current"))
    if abs(BS["balance_check"]) > 0.5:
        st.error(f"⚠️ Balance sheet does not balance by {fmt(BS['balance_check'])}. Check inputs.")
    else:
        st.success("✅ Balance sheet balances (Assets = Liabilities + Equity).")
    with st.expander("📌 Key liquidity & leverage ratios (auto-calculated)"):
        current_ratio = BS["total_current_assets"] / BS["total_current_liabilities"] if BS["total_current_liabilities"] else 0
        debt_to_equity = BS["total_liabilities"] / BS["total_equity"] if BS["total_equity"] else 0
        c1, c2 = st.columns(2)
        c1.metric("Current Ratio", f"{current_ratio:,.2f}x")
        c2.metric("Total Debt-to-Equity", f"{debt_to_equity:,.2f}x")

# --------------------------------------------------------------------------
# TAB 3: CASH FLOW
# --------------------------------------------------------------------------
with tabs[3]:
    render_statement(CF["rows"], amount_header=I("fy_label_current"))
    if abs(CF["ending_cash"] - (CF["beginning_cash"] + CF["net_change_in_cash"])) > 0.5:
        st.error("⚠️ Ending cash does not tie to beginning cash + net change. Check inputs.")
    else:
        st.success("✅ Ending cash ties out and flows into the Balance Sheet's cash line.")
    with st.expander("📌 Free cash flow (auto-calculated)"):
        fcf = CF["cfo"] + I("cf_capex_ppe") + I("cf_capex_intangibles")
        st.metric("Free Cash Flow (CFO + Capex)", fmt(fcf))

# --------------------------------------------------------------------------
# TAB 4: RETAINED EARNINGS
# --------------------------------------------------------------------------
with tabs[4]:
    render_statement(RE["rows"], amount_header=I("fy_label_current"))
    st.caption("Ending retained earnings flows directly into the Balance Sheet's Stockholders' Equity section.")

# --------------------------------------------------------------------------
# TAB 5: NOTES
# --------------------------------------------------------------------------
with tabs[5]:
    st.header("🗒️ Notes to the Financial Statements")
    st.caption(f"{I('company_name')} — Notes for the year ended {I('fy_label_current')}")

    st.markdown("### Note 1 — Summary of Significant Accounting Policies")
    st.markdown(
        "- **Basis of presentation:** These statements are presented on an accrual basis "
        "in accordance with a standard 3-statement model framework.\n"
        "- **Revenue recognition:** Product revenue is recognized at a point in time upon "
        "transfer of control; service revenue is recognized over time as services are performed.\n"
        "- **Inventory:** Stated at the lower of cost (FIFO) or net realizable value.\n"
        "- **Property, plant & equipment:** Recorded at cost and depreciated on a straight-line basis.\n"
        "- **Goodwill & indefinite-lived intangibles:** Tested for impairment at least annually."
    )

    st.markdown("### Note 2 — Accounts Receivable, Net")
    ar_table = pd.DataFrame({
        "Item": ["Accounts receivable, gross", "Less: Allowance for doubtful accounts", "Accounts receivable, net"],
        I("fy_label_current"): [I("bs_accounts_receivable_gross"), -I("bs_allowance_doubtful_accounts"), BS["net_ar"]],
    })
    st.dataframe(ar_table, hide_index=True, use_container_width=True)

    st.markdown("### Note 3 — Inventory")
    inv_table = pd.DataFrame({
        "Item": ["Raw materials", "Work in process", "Finished goods", "Total inventory"],
        I("fy_label_current"): [I("bs_inventory_raw_materials"), I("bs_inventory_wip"),
                                  I("bs_inventory_finished_goods"), BS["total_inventory"]],
    })
    st.dataframe(inv_table, hide_index=True, use_container_width=True)

    st.markdown("### Note 4 — Property, Plant & Equipment, Net")
    ppe_table = pd.DataFrame({
        "Item": ["Land", "Buildings", "Machinery & equipment", "Gross PP&E",
                 "Less: Accumulated depreciation", "PP&E, net"],
        I("fy_label_current"): [I("bs_land"), I("bs_buildings"), I("bs_machinery_equipment"),
                                  BS["gross_ppe"], -I("bs_accumulated_depreciation"), BS["net_ppe"]],
    })
    st.dataframe(ppe_table, hide_index=True, use_container_width=True)

    st.markdown("### Note 5 — Goodwill and Intangible Assets")
    intang_table = pd.DataFrame({
        "Item": ["Goodwill", "Intangible assets, gross", "Less: Accumulated amortization", "Intangible assets, net"],
        I("fy_label_current"): [I("bs_goodwill"), I("bs_intangible_assets_gross"),
                                  -I("bs_accumulated_amortization"), BS["net_intangibles"]],
    })
    st.dataframe(intang_table, hide_index=True, use_container_width=True)

    st.markdown("### Note 6 — Leases")
    c1, c2, c3 = st.columns(3)
    c1.metric("Operating lease expense", fmt(I("note_lease_operating_expense")))
    c2.metric("Weighted avg. remaining term", f"{I('note_lease_weighted_avg_term_years'):.1f} yrs")
    c3.metric("Weighted avg. discount rate", fmt_pct(I("note_lease_discount_rate_pct")))
    st.caption(
        f"Operating lease ROU asset of {fmt(I('bs_operating_lease_rou_asset'))} and total lease liability of "
        f"{fmt(I('bs_current_operating_lease_liability') + I('bs_noncurrent_operating_lease_liability'))} "
        f"are recorded on the Balance Sheet."
    )

    st.markdown("### Note 7 — Debt and Maturities")
    debt_table = pd.DataFrame({
        "Period": ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Thereafter", "Total"],
        "Maturities": [
            I("note_debt_maturity_year_1"), I("note_debt_maturity_year_2"), I("note_debt_maturity_year_3"),
            I("note_debt_maturity_year_4"), I("note_debt_maturity_year_5"), I("note_debt_maturity_thereafter"),
            NOTES["debt_total"],
        ],
    })
    st.dataframe(debt_table, hide_index=True, use_container_width=True)
    st.caption(f"Weighted average interest rate on outstanding debt: {fmt_pct(I('note_debt_interest_rate_pct'))}")

    st.markdown("### Note 8 — Pension and Post-Retirement Benefits")
    c1, c2 = st.columns(2)
    c1.metric("Projected benefit obligation", fmt(I("note_pension_benefit_obligation")))
    c2.metric("Fair value of plan assets", fmt(I("note_pension_fair_value_plan_assets")))
    st.metric("Funded status (assets − obligation)", fmt(NOTES["pension_funded_status"]))
    st.caption(
        f"Discount rate: {fmt_pct(I('note_pension_discount_rate_pct'))} · "
        f"Expected long-term return on assets: {fmt_pct(I('note_pension_expected_return_pct'))}"
    )

    st.markdown("### Note 9 — Stock-Based Compensation")
    c1, c2 = st.columns(2)
    c1.metric("SBC expense recognized (current period)", fmt(I("stock_based_compensation")))
    c2.metric("Unrecognized SBC expense", fmt(I("note_sbc_unrecognized_expense")))
    st.caption(f"Expected to be recognized over a weighted-average period of {I('note_sbc_weighted_avg_period_years'):.1f} years.")

    st.markdown("### Note 10 — Income Taxes")
    tax_table = pd.DataFrame({
        "Item": ["Statutory tax rate", "Effective tax rate", "Difference (effective − statutory)"],
        "Rate (%)": [I("note_effective_tax_rate_statutory_pct"), I("effective_tax_rate_pct"),
                     NOTES["statutory_vs_effective"]],
    })
    st.dataframe(tax_table, hide_index=True, use_container_width=True)
    st.caption(f"Deferred tax expense (benefit) included in the total tax provision: {fmt(I('deferred_tax_expense_benefit'))}")

    st.markdown("### Note 11 — Commitments and Contingencies")
    st.markdown(
        f"- Accrued legal contingencies: **{fmt(I('note_contingency_legal_accrual'))}**\n"
        f"- Reasonably possible losses not accrued (disclosed only): **{fmt(I('note_contingency_disclosed_not_accrued'))}**\n"
        f"- The Company is involved in various claims and legal proceedings arising in the "
        f"ordinary course of business. Management believes the ultimate resolution of these "
        f"matters will not have a material adverse effect on the Company's financial position."
    )

    st.markdown("### Note 12 — Related Party Transactions")
    st.markdown(f"Transactions with related parties during the period totaled **{fmt(I('note_related_party_transactions'))}**.")

    st.markdown("### Note 13 — Segment Reporting")
    seg_table = pd.DataFrame({
        "Segment": [I("note_segment1_name"), I("note_segment2_name"), "Total"],
        "Revenue": [I("note_segment1_revenue"), I("note_segment2_revenue"), NOTES["segment_total_rev"]],
        "Operating Income": [I("note_segment1_op_income"), I("note_segment2_op_income"), NOTES["segment_total_opinc"]],
    })
    st.dataframe(seg_table, hide_index=True, use_container_width=True)
    if abs(NOTES["segment_total_rev"] - IS["net_revenue"]) > 0.5:
        st.warning(
            f"Note: Segment revenue total ({fmt(NOTES['segment_total_rev'])}) does not equal "
            f"consolidated net revenue ({fmt(IS['net_revenue'])}). Adjust segment inputs if a tie-out is required."
        )

    st.markdown("### Note 14 — Subsequent Events")
    if I("note_subsequent_event_amount"):
        st.markdown(f"A subsequent event with an estimated financial impact of **{fmt(I('note_subsequent_event_amount'))}** was identified after period end.")
    else:
        st.markdown("Management has evaluated events occurring after the balance sheet date and noted no material subsequent events requiring disclosure.")

    st.markdown("### Note 15 — Earnings Per Share Reconciliation")
    eps_table = pd.DataFrame({
        "Item": ["Net income available to common shareholders", "Weighted avg. shares — basic",
                 "Dilutive effect of options/RSUs", "Weighted avg. shares — diluted", "Basic EPS", "Diluted EPS"],
        "Value": [IS["net_income_available_to_common"], I("weighted_avg_shares_basic"),
                  I("dilutive_effect_shares"), I("weighted_avg_shares_basic") + I("dilutive_effect_shares"),
                  IS["basic_eps"], IS["diluted_eps"]],
    })
    st.dataframe(eps_table, hide_index=True, use_container_width=True)

# --------------------------------------------------------------------------
# FOOTER
# --------------------------------------------------------------------------
st.markdown("---")
st.caption(
    "This page is generated entirely from the values in the **Inputs** tab. "
    "All five statements are recalculated live on every change — there is no "
    "manual re-entry of numbers between statements."
)