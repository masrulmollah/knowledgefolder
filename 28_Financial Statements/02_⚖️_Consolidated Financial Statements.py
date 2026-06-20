"""
Consolidated (Group) Financial Statements
==========================================
A self-contained Streamlit page presenting a full set of CONSOLIDATED
financial statements for a multi-subsidiary group:

  • Consolidated Income Statement  (with intercompany revenue / COGS elimination)
  • Consolidated Statement of Comprehensive Income
  • Consolidated Balance Sheet     (with intercompany AR/AP elimination; cash solved from CF)
  • Consolidated Cash Flow Statement (indirect method, including NCI dividends)
  • Consolidated Statement of Changes in Equity (RE + AOCI + NCI)
  • Notes to the Consolidated Financial Statements
  • 🧮 Master Inputs tab (every number editable; all statements update live)

KEY DIFFERENCES vs. a standalone entity file
---------------------------------------------
1. Intercompany eliminations: Revenue↔COGS, AR↔AP, interest income↔expense,
   unrealised profit in inventory are all explicitly eliminated in the Inputs
   tab and labelled in every statement.
2. Noncontrolling interests (NCI): NCI share of net income is deducted on the
   Income Statement; NCI equity roll-forward appears on the equity statement
   and Balance Sheet; NCI dividends appear in the Cash Flow.
3. Goodwill on consolidation: Goodwill arising from acquisitions is shown
   as a separate non-current asset with a segment breakdown in the Notes.
4. Comprehensive income: A separate statement shows OCI components
   (FX translation, pension re-measurements, cash-flow hedges, fair-value
   movements on investments) and total comprehensive income attributable to
   the parent and to NCI.
5. Subsidiary listing: Notes disclose each subsidiary, country, ownership %, and
   method of consolidation.
6. Three operating segments: Revenue and operating income are disaggregated by
   segment in both the Income Statement and the Segment Note.

HOW TO RUN
----------
    pip install streamlit pandas
    streamlit run consolidated_financial_statements.py

EMBEDDING IN YOUR WEBSITE
--------------------------
Deploy this app (Streamlit Community Cloud / any server) and embed it with:
    <iframe src="https://your-deployed-url" width="100%" height="900"></iframe>
Or serve it behind a reverse proxy at  yoursite.com/consolidated-financials.
"""

import streamlit as st
import pandas as pd

UNITS_LABEL = "$ in thousands"
AOCI_BEGINNING = -4_800.0   # hard-wired opening AOCI; users can adjust via inputs
NCI_BS_BEGINNING = 32_600.0  # opening NCI balance on consolidated BS

# ==========================================================================
# DEFAULT INPUTS
# ==========================================================================
DEFAULTS = {
    # ---- Group meta ----
    "group_name": "Acme Industrial Group, Inc.",
    "fy_current": "FY2026",
    "fy_prior": "FY2025",
    "currency": "USD",
    "reporting_basis": "IFRS / US GAAP Consolidated",

    # ---- Subsidiary register ----
    "sub1_name": "Acme Europe GmbH", "sub1_country": "Germany", "sub1_ownership": 100.0,
    "sub2_name": "Acme Asia Pacific Pte. Ltd.", "sub2_country": "Singapore", "sub2_ownership": 80.0,
    "sub3_name": "TechCore Solutions Inc.", "sub3_country": "United States", "sub3_ownership": 100.0,
    "sub4_name": "Acme Distribution LLC", "sub4_country": "United States", "sub4_ownership": 75.0,

    # =========================================================
    # INCOME STATEMENT
    # =========================================================
    "rev_segment1": 580_000.0,
    "rev_segment2": 310_000.0,
    "rev_segment3": 195_000.0,
    "interco_revenue_elim": 42_000.0,   # revenue between group entities to eliminate
    "sales_returns": 11_200.0,
    "sales_discounts": 6_300.0,

    "cogs_materials": 438_000.0,
    "cogs_direct_labor": 172_000.0,
    "cogs_overhead": 68_500.0,
    "cogs_depreciation": 22_000.0,
    "cogs_inventory_writedown": 3_800.0,
    "interco_cogs_elim": 38_000.0,     # intercompany COGS to eliminate (mirrors interco revenue)

    "sga_salaries": 94_000.0,
    "sga_marketing": 32_500.0,
    "sga_rd": 48_000.0,
    "sga_da": 12_000.0,
    "sga_bad_debt": 3_100.0,
    "sga_other": 21_200.0,
    "sbc": 13_500.0,
    "restructuring": 7_400.0,
    "impairment": 5_200.0,
    "acquisition_costs": 3_600.0,

    "interest_income": 2_800.0,
    "interest_expense": 21_500.0,
    "interco_interest_elim": 1_200.0,  # intercompany interest to eliminate
    "gain_loss_assets": 1_400.0,
    "fx_gain_loss": -1_050.0,
    "equity_method_income": 2_400.0,
    "bargain_purchase_gain": 0.0,
    "other_nonop": -850.0,

    "disc_ops_pretax": -3_100.0,
    "disc_ops_tax": -650.0,

    "eff_tax_rate_pct": 24.0,
    "deferred_tax_exp": 1_450.0,

    "nci_net_income": 4_200.0,
    "preferred_divs": 2_500.0,
    "shares_basic": 62_000.0,
    "dilutive_shares": 1_800.0,

    # =========================================================
    # OTHER COMPREHENSIVE INCOME
    # =========================================================
    "oci_fx_translation": -3_200.0,
    "oci_pension_adj": -1_800.0,
    "oci_hedging": 950.0,
    "oci_investments": 420.0,

    # =========================================================
    # CONSOLIDATED RETAINED EARNINGS
    # =========================================================
    "re_beginning": 198_500.0,
    "prior_period_adj": -1_800.0,
    "cumeff_acctg_change": -600.0,
    "common_divs_declared": 11_200.0,
    "pref_divs_declared": 2_500.0,
    "buyback_re_effect": 4_100.0,

    # =========================================================
    # CONSOLIDATED BALANCE SHEET — Current Assets (excl. Cash)
    # =========================================================
    "bs_str_investments": 22_000.0,
    "bs_ar_gross": 94_500.0,
    "bs_allowance": 5_100.0,
    "interco_ar_elim": 6_800.0,        # intercompany AR to eliminate
    "bs_inventory_rm": 28_500.0,
    "bs_inventory_wip": 18_200.0,
    "bs_inventory_fg": 47_300.0,
    "bs_prepaid": 8_900.0,
    "bs_other_ca": 6_200.0,
    "bs_assets_held_for_sale": 4_500.0,

    # =========================================================
    # CONSOLIDATED BALANCE SHEET — Non-Current Assets
    # =========================================================
    "bs_land": 38_500.0,
    "bs_buildings": 178_000.0,
    "bs_machinery": 241_000.0,
    "bs_accum_dep": 118_500.0,
    "bs_rou_operating": 31_200.0,
    "bs_rou_finance": 8_600.0,
    "bs_goodwill": 142_000.0,
    "bs_intangibles_gross": 68_000.0,
    "bs_accum_amort": 24_500.0,
    "bs_equity_method_inv": 24_300.0,
    "bs_deferred_tax_assets": 8_200.0,
    "bs_other_nca": 5_400.0,

    # =========================================================
    # CONSOLIDATED BALANCE SHEET — Current Liabilities
    # =========================================================
    "bs_ap": 71_500.0,
    "interco_ap_elim": 6_800.0,        # intercompany AP to eliminate (mirrors interco_ar_elim)
    "bs_accrued_sal": 23_800.0,
    "bs_accrued_int": 2_600.0,
    "bs_itp": 8_200.0,
    "bs_current_ltd": 15_000.0,
    "bs_current_op_lease": 7_800.0,
    "bs_current_fin_lease": 2_100.0,
    "bs_deferred_rev_curr": 17_400.0,
    "bs_divs_payable": 2_800.0,
    "bs_other_cl": 6_700.0,

    # =========================================================
    # CONSOLIDATED BALANCE SHEET — Non-Current Liabilities
    # =========================================================
    "bs_ltd": 198_000.0,
    "bs_nc_op_lease": 24_600.0,
    "bs_nc_fin_lease": 6_900.0,
    "bs_dtl": 13_800.0,
    "bs_pension": 29_400.0,
    "bs_deferred_rev_nc": 5_800.0,
    "bs_other_ncl": 4_600.0,

    # =========================================================
    # EQUITY (excl. RE, AOCI, NCI — those are computed)
    # =========================================================
    "bs_preferred_par": 25_000.0,
    "bs_common_par": 6_200.0,
    "bs_apic": 214_410.0,              # computed to balance — users can adjust
    "bs_treasury": 46_000.0,

    # =========================================================
    # CONSOLIDATED CASH FLOW STATEMENT
    # =========================================================
    "cf_beg_cash": 51_800.0,
    "cf_dep_total": 34_000.0,
    "cf_amort_total": 11_000.0,
    "cf_def_tax": 1_450.0,
    "cf_sbc": 13_500.0,
    "cf_prov_doubtful": 3_100.0,
    "cf_impairment_nc": 5_200.0,
    "cf_gain_adj": -1_400.0,
    "cf_eq_income_adj": -2_400.0,
    "cf_eq_distributions": 1_800.0,
    "cf_chg_ar": -10_200.0,
    "cf_chg_inv": -6_800.0,
    "cf_chg_prepaid": -1_100.0,
    "cf_chg_oca": -400.0,
    "cf_chg_ap": 8_100.0,
    "cf_chg_accr": 2_800.0,
    "cf_chg_itp": 1_300.0,
    "cf_chg_def_rev": 2_200.0,
    "cf_chg_other_liab": -500.0,
    "cf_pension_contrib": -2_700.0,
    "cf_capex_ppe": -52_000.0,
    "cf_capex_int": -8_200.0,
    "cf_proc_sale_assets": 4_600.0,
    "cf_acquisitions": -28_000.0,      # net of cash acquired
    "cf_purch_investments": -11_000.0,
    "cf_mat_investments": 7_500.0,
    "cf_loans_rp": -1_200.0,
    "cf_proc_ltd": 38_000.0,
    "cf_repay_ltd": -22_000.0,
    "cf_proc_rev": 15_000.0,
    "cf_repay_rev": -11_000.0,
    "cf_fin_lease_pmts": -2_600.0,
    "cf_proc_stock": 5_100.0,
    "cf_repurch_stock": -10_800.0,
    "cf_divs_common": -11_000.0,
    "cf_divs_preferred": -2_500.0,
    "cf_divs_nci": -1_800.0,           # dividends paid to NCI shareholders
    "cf_debt_issuance": -750.0,
    "cf_fx_cash": -420.0,

    # =========================================================
    # NOTES
    # =========================================================
    "note_seg1_name": "Industrial Products",
    "note_seg1_rev": 538_000.0,
    "note_seg1_opinc": 71_000.0,
    "note_seg1_assets": 480_000.0,
    "note_seg2_name": "Technology Solutions",
    "note_seg2_rev": 267_700.0,
    "note_seg2_opinc": 32_500.0,
    "note_seg2_assets": 290_000.0,
    "note_seg3_name": "Services & Distribution",
    "note_seg3_rev": 183_000.0,
    "note_seg3_opinc": 19_800.0,
    "note_seg3_assets": 143_986.0,
    "note_goodwill_seg1": 89_000.0,
    "note_goodwill_seg2": 35_000.0,
    "note_goodwill_seg3": 18_000.0,
    "note_lease_op_exp": 9_200.0,
    "note_lease_term": 7.2,
    "note_lease_rate": 5.50,
    "note_debt_rate": 6.35,
    "note_debt_yr1": 15_000.0,
    "note_debt_yr2": 18_000.0,
    "note_debt_yr3": 20_000.0,
    "note_debt_yr4": 22_000.0,
    "note_debt_yr5": 25_000.0,
    "note_debt_thereafter": 113_000.0,
    "note_pension_disc": 4.90,
    "note_pension_ret": 6.20,
    "note_pension_pbo": 72_000.0,
    "note_pension_assets": 42_800.0,
    "note_sbc_unrec": 22_400.0,
    "note_sbc_period": 2.6,
    "note_contingency_accrued": 2_200.0,
    "note_contingency_possible": 6_500.0,
    "note_rpt": 3_500.0,
    "note_subsequent": 0.0,
    "note_stat_tax_rate": 21.0,
    "note_geo_rev_americas": 512_000.0,
    "note_geo_rev_emea": 318_500.0,
    "note_geo_rev_apac": 195_000.0,
    "note_unrealised_interco_profit": 4_000.0,  # unrealised profit still in inventory
}

# ==========================================================================
# SESSION STATE
# ==========================================================================
if "grp" not in st.session_state:
    st.session_state["grp"] = DEFAULTS.copy()

def reset():
    st.session_state["grp"] = DEFAULTS.copy()

def G(k):
    return st.session_state["grp"][k]

# ==========================================================================
# FORMATTERS
# ==========================================================================
def fmt(x, decimals=0):
    if x is None: return ""
    neg = x < 0
    s = f"{abs(x):,.{decimals}f}"
    return f"({s})" if neg else s

def pct(x, d=1): return f"{x:,.{d}f}%"

def render(rows, col1_header="", col2_header="", col3_header=None):
    has3 = col3_header is not None
    if has3:
        c1,c2,c3 = st.columns([5,2,2])
        c1.markdown(f"**{col1_header}**"); c2.markdown(f"**{col2_header}**"); c3.markdown(f"**{col3_header}**")
    else:
        c1,c2 = st.columns([5,2])
        c1.markdown(f"**{col1_header}**"); c2.markdown(f"**{col2_header}**")
    st.markdown("<hr style='margin:4px 0 6px'>", unsafe_allow_html=True)

    for row in rows:
        label = row[0]; val = row[1]
        style = row[2] if len(row)>2 else "line"
        val2 = row[3] if len(row)>3 else None

        if style == "spacer":
            st.markdown("<div style='height:5px'></div>", unsafe_allow_html=True); continue

        if has3:
            c1,c2,c3 = st.columns([5,2,2])
        else:
            c1,c2 = st.columns([5,2])

        v2str = fmt(val2) if val2 is not None else ""

        if style == "header":
            c1.markdown(f"#### {label}")
            if has3: c2.markdown(""); c3.markdown("")
            else: c2.markdown("")
        elif style == "subheader":
            c1.markdown(f"**{label}**")
            if has3: c2.markdown(""); c3.markdown("")
            else: c2.markdown("")
        elif style == "elim":
            c1.markdown(f"<span style='color:#888;font-style:italic'>&nbsp;&nbsp;&nbsp;{label}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span style='color:#888;font-style:italic'>{fmt(val)}</span>", unsafe_allow_html=True)
            if has3: c3.markdown(f"<span style='color:#888;font-style:italic'>{v2str}</span>", unsafe_allow_html=True)
        elif style == "note":
            c1.markdown(f"<span style='color:gray;font-size:.85em'>{label}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span style='color:gray;font-size:.85em'>{fmt(val) if val is not None else ''}</span>", unsafe_allow_html=True)
            if has3: c3.markdown("")
        elif style == "subtotal":
            c1.markdown(f"**{label}**"); c2.markdown(f"**{fmt(val)}**")
            if has3: c3.markdown(f"**{v2str}**")
            st.markdown("<hr style='margin:-4px 0 6px'>", unsafe_allow_html=True)
        elif style == "total":
            c1.markdown(f"### {label}"); c2.markdown(f"### {fmt(val)}")
            if has3: c3.markdown(f"### {v2str}")
            st.markdown("<hr style='border-top:3px double #333;margin:-8px 0 10px'>", unsafe_allow_html=True)
        else:
            c1.markdown(f"&nbsp;&nbsp;&nbsp;{label}", unsafe_allow_html=True)
            c2.markdown(fmt(val) if val is not None else "")
            if has3: c3.markdown(v2str)

# ==========================================================================
# STATEMENT BUILDERS
# ==========================================================================

def build_income_statement():
    g = st.session_state["grp"]
    gross_rev = g["rev_segment1"]+g["rev_segment2"]+g["rev_segment3"]
    net_rev = gross_rev - g["interco_revenue_elim"] - g["sales_returns"] - g["sales_discounts"]

    total_cogs = (g["cogs_materials"]+g["cogs_direct_labor"]+g["cogs_overhead"]
                  +g["cogs_depreciation"]+g["cogs_inventory_writedown"] - g["interco_cogs_elim"])
    gross_profit = net_rev - total_cogs

    total_sga = g["sga_salaries"]+g["sga_marketing"]+g["sga_rd"]+g["sga_da"]+g["sga_bad_debt"]+g["sga_other"]
    total_opex = total_sga + g["sbc"] + g["restructuring"] + g["impairment"] + g["acquisition_costs"]
    op_income = gross_profit - total_opex

    total_other = (g["interest_income"] - g["interest_expense"] + g["interco_interest_elim"]
                   + g["gain_loss_assets"] + g["fx_gain_loss"]
                   + g["equity_method_income"] + g["bargain_purchase_gain"] + g["other_nonop"])
    pretax = op_income + total_other
    tax = pretax * (g["eff_tax_rate_pct"]/100.0)
    income_cont = pretax - tax
    disc_net = g["disc_ops_pretax"] - g["disc_ops_tax"]
    net_income = income_cont + disc_net

    ni_parent = net_income - g["nci_net_income"]
    ni_common = ni_parent - g["preferred_divs"]
    diluted_shares = g["shares_basic"] + g["dilutive_shares"]
    basic_eps = ni_common / g["shares_basic"] if g["shares_basic"] else 0
    diluted_eps = ni_common / diluted_shares if diluted_shares else 0

    rows = [
        ("CONSOLIDATED INCOME STATEMENT", None, "header"),
        (f"For the Year Ended — {G('fy_current')}", None, "subheader"),
        ("spacer",None,"spacer"),

        ("Revenue by Segment", None, "subheader"),
        (f"  {G('note_seg1_name')}", g["rev_segment1"], "line"),
        (f"  {G('note_seg2_name')}", g["rev_segment2"], "line"),
        (f"  {G('note_seg3_name')}", g["rev_segment3"], "line"),
        ("Gross segment revenue (before eliminations)", gross_rev, "line"),
        ("  Less: Intercompany revenue eliminated", -g["interco_revenue_elim"], "elim"),
        ("  Less: Sales returns & allowances", -g["sales_returns"], "line"),
        ("  Less: Sales discounts", -g["sales_discounts"], "line"),
        ("Net consolidated revenue", net_rev, "subtotal"),

        ("Cost of Goods Sold", None, "subheader"),
        ("  Direct materials", g["cogs_materials"], "line"),
        ("  Direct labor", g["cogs_direct_labor"], "line"),
        ("  Manufacturing overhead", g["cogs_overhead"], "line"),
        ("  Depreciation (cost of sales)", g["cogs_depreciation"], "line"),
        ("  Inventory write-down", g["cogs_inventory_writedown"], "line"),
        ("  Less: Intercompany COGS eliminated", -g["interco_cogs_elim"], "elim"),
        ("Total cost of goods sold", -total_cogs, "subtotal"),

        ("Gross Profit", gross_profit, "total"),

        ("Operating Expenses", None, "subheader"),
        ("  Selling, general & administrative:", None, "line"),
        ("    Salaries & employee benefits", g["sga_salaries"], "line"),
        ("    Marketing & advertising", g["sga_marketing"], "line"),
        ("    Research & development", g["sga_rd"], "line"),
        ("    Depreciation & amortization", g["sga_da"], "line"),
        ("    Provision for doubtful accounts", g["sga_bad_debt"], "line"),
        ("    Other SG&A", g["sga_other"], "line"),
        ("  Total SG&A", total_sga, "line"),
        ("  Stock-based compensation", g["sbc"], "line"),
        ("  Restructuring & severance charges", g["restructuring"], "line"),
        ("  Asset impairment charges", g["impairment"], "line"),
        ("  Acquisition-related costs", g["acquisition_costs"], "line"),
        ("Total operating expenses", -total_opex, "subtotal"),

        ("Operating Income (EBIT)", op_income, "total"),

        ("Other Income (Expense)", None, "subheader"),
        ("  Interest income", g["interest_income"], "line"),
        ("  Interest expense", -g["interest_expense"], "line"),
        ("  Less: Intercompany interest eliminated", g["interco_interest_elim"], "elim"),
        ("  Gain (loss) on disposal of assets", g["gain_loss_assets"], "line"),
        ("  Foreign exchange gain (loss)", g["fx_gain_loss"], "line"),
        ("  Share of profit of equity-accounted investees", g["equity_method_income"], "line"),
        ("  Bargain purchase gain on acquisition", g["bargain_purchase_gain"], "line"),
        ("  Other non-operating income (expense)", g["other_nonop"], "line"),
        ("Total other income (expense), net", total_other, "subtotal"),

        ("Income from continuing operations before tax", pretax, "subtotal"),
        ("Income tax expense", -tax, "line"),
        (f"  of which: current tax", -(tax - g["deferred_tax_exp"]), "note"),
        (f"  of which: deferred tax expense (benefit)", g["deferred_tax_exp"], "note"),
        ("Income from continuing operations, net of tax", income_cont, "subtotal"),
        ("Income (loss) from discontinued operations, net of tax", disc_net, "line"),

        ("Net Income (Group)", net_income, "total"),
        ("  Attributable to noncontrolling interests (NCI)", -g["nci_net_income"], "line"),
        ("  Attributable to shareholders of the parent", ni_parent, "subtotal"),
        ("  Less: Preferred dividends", -g["preferred_divs"], "line"),
        ("Net income available to common shareholders (parent)", ni_common, "total"),

        ("Earnings Per Share — Parent", None, "subheader"),
        ("  Basic EPS", basic_eps, "line"),
        ("  Diluted EPS", diluted_eps, "line"),
        ("  Weighted avg. shares — basic (thousands)", g["shares_basic"], "line"),
        ("  Weighted avg. shares — diluted (thousands)", diluted_shares, "line"),
    ]
    return dict(rows=rows, gross_rev=gross_rev, net_rev=net_rev, total_cogs=total_cogs,
                gross_profit=gross_profit, total_sga=total_sga, total_opex=total_opex,
                op_income=op_income, total_other=total_other, pretax=pretax, tax=tax,
                income_cont=income_cont, disc_net=disc_net, net_income=net_income,
                ni_parent=ni_parent, ni_common=ni_common, basic_eps=basic_eps,
                diluted_eps=diluted_eps, diluted_shares=diluted_shares)


def build_oci(IS):
    g = st.session_state["grp"]
    total_oci = g["oci_fx_translation"]+g["oci_pension_adj"]+g["oci_hedging"]+g["oci_investments"]
    total_comprehensive = IS["net_income"] + total_oci
    comp_parent = IS["ni_parent"] + total_oci   # simplified: full OCI to parent
    comp_nci = g["nci_net_income"]              # NCI share is just their NI here
    ending_aoci = AOCI_BEGINNING + total_oci

    rows = [
        ("CONSOLIDATED STATEMENT OF COMPREHENSIVE INCOME", None, "header"),
        (f"For the Year Ended — {G('fy_current')}", None, "subheader"),
        ("spacer",None,"spacer"),
        ("Net income (Group)", IS["net_income"], "line"),
        ("Other Comprehensive Income (Loss), net of tax", None, "subheader"),
        ("  Foreign currency translation adjustments", g["oci_fx_translation"], "line"),
        ("  Pension & post-retirement re-measurement", g["oci_pension_adj"], "line"),
        ("  Effective portion of cash-flow hedges", g["oci_hedging"], "line"),
        ("  Net unrealised gains (losses) on investments", g["oci_investments"], "line"),
        ("Total other comprehensive income (loss)", total_oci, "subtotal"),
        ("Total Comprehensive Income (Group)", total_comprehensive, "total"),
        ("  Attributable to noncontrolling interests", comp_nci, "line"),
        ("  Attributable to shareholders of the parent", comp_parent, "subtotal"),
    ]
    return dict(rows=rows, total_oci=total_oci, total_comprehensive=total_comprehensive,
                ending_aoci=ending_aoci)


def build_retained_earnings(IS):
    g = st.session_state["grp"]
    adj_beg = g["re_beginning"] + g["prior_period_adj"] + g["cumeff_acctg_change"]
    ending_re = adj_beg + IS["ni_parent"] - g["common_divs_declared"] - g["pref_divs_declared"] - g["buyback_re_effect"]

    rows = [
        ("CONSOLIDATED STATEMENT OF RETAINED EARNINGS", None, "header"),
        (f"For the Year Ended — {G('fy_current')} (attributable to parent shareholders)", None, "subheader"),
        ("spacer",None,"spacer"),
        ("Retained earnings, beginning of period (as previously reported)", g["re_beginning"], "line"),
        ("Prior period restatement / error correction (net of tax)", g["prior_period_adj"], "line"),
        ("Cumulative effect of change in accounting policy", g["cumeff_acctg_change"], "line"),
        ("Retained earnings, beginning of period (as restated)", adj_beg, "subtotal"),
        ("Add: Net income attributable to parent shareholders", IS["ni_parent"], "line"),
        ("Less: Common dividends declared", -g["common_divs_declared"], "line"),
        ("Less: Preferred dividends declared", -g["pref_divs_declared"], "line"),
        ("Less: Excess of treasury share cost over par charged to RE", -g["buyback_re_effect"], "line"),
        ("Retained Earnings, End of Period", ending_re, "total"),
    ]
    return dict(rows=rows, ending_re=ending_re, adj_beg=adj_beg)


def build_equity_statement(IS, OCI, RE):
    g = st.session_state["grp"]
    nci_end = NCI_BS_BEGINNING + g["nci_net_income"] - g["cf_divs_nci"]
    rows = [
        ("CONSOLIDATED STATEMENT OF CHANGES IN EQUITY", None, "header"),
        (f"For the Year Ended — {G('fy_current')}", None, "subheader"),
        ("spacer",None,"spacer"),
        ("Component", None, "subheader"),
        ("Opening retained earnings (as restated)", RE["adj_beg"], "line"),
        ("Net income attributable to parent", IS["ni_parent"], "line"),
        ("Dividends declared (common & preferred)", -(g["common_divs_declared"]+g["pref_divs_declared"]), "line"),
        ("Treasury share retirement effect on RE", -g["buyback_re_effect"], "line"),
        ("Closing retained earnings", RE["ending_re"], "subtotal"),
        ("spacer",None,"spacer"),
        ("Opening AOCI", AOCI_BEGINNING, "line"),
        ("Total OCI for the period (net of tax)", OCI["total_oci"], "line"),
        ("Closing AOCI", OCI["ending_aoci"], "subtotal"),
        ("spacer",None,"spacer"),
        ("Noncontrolling interests — opening balance", NCI_BS_BEGINNING, "line"),
        ("NCI share of net income", g["nci_net_income"], "line"),
        ("Dividends paid to NCI shareholders", -g["cf_divs_nci"], "line"),
        ("NCI — closing balance", nci_end, "subtotal"),
    ]
    return dict(rows=rows, nci_end=nci_end)


def build_cash_flow(IS):
    g = st.session_state["grp"]
    noncash = (g["cf_dep_total"]+g["cf_amort_total"]+g["cf_def_tax"]+g["cf_sbc"]
               +g["cf_prov_doubtful"]+g["cf_impairment_nc"]
               +g["cf_gain_adj"]+g["cf_eq_income_adj"]+g["cf_eq_distributions"])
    wc = (g["cf_chg_ar"]+g["cf_chg_inv"]+g["cf_chg_prepaid"]+g["cf_chg_oca"]
          +g["cf_chg_ap"]+g["cf_chg_accr"]+g["cf_chg_itp"]
          +g["cf_chg_def_rev"]+g["cf_chg_other_liab"]+g["cf_pension_contrib"])
    cfo = IS["net_income"] + noncash + wc
    cfi = (g["cf_capex_ppe"]+g["cf_capex_int"]+g["cf_proc_sale_assets"]
           +g["cf_acquisitions"]+g["cf_purch_investments"]+g["cf_mat_investments"]+g["cf_loans_rp"])
    cff = (g["cf_proc_ltd"]+g["cf_repay_ltd"]+g["cf_proc_rev"]+g["cf_repay_rev"]
           +g["cf_fin_lease_pmts"]+g["cf_proc_stock"]+g["cf_repurch_stock"]
           +g["cf_divs_common"]+g["cf_divs_preferred"]+g["cf_divs_nci"]+g["cf_debt_issuance"])
    net_chg = cfo + cfi + cff + g["cf_fx_cash"]
    ending_cash = g["cf_beg_cash"] + net_chg

    rows = [
        ("CONSOLIDATED STATEMENT OF CASH FLOWS", None, "header"),
        (f"For the Year Ended — {G('fy_current')}  (Indirect Method)", None, "subheader"),
        ("spacer",None,"spacer"),

        ("Cash Flows from Operating Activities", None, "subheader"),
        ("Net income (Group, including NCI)", IS["net_income"], "line"),
        ("Adjustments for non-cash and non-operating items:", None, "line"),
        ("  Depreciation of PP&E (total group)", g["cf_dep_total"], "line"),
        ("  Amortisation of intangible assets", g["cf_amort_total"], "line"),
        ("  Deferred income taxes", g["cf_def_tax"], "line"),
        ("  Share-based compensation expense", g["cf_sbc"], "line"),
        ("  Provision for expected credit losses", g["cf_prov_doubtful"], "line"),
        ("  Asset impairment charges (non-cash)", g["cf_impairment_nc"], "line"),
        ("  Gain on disposal of assets (removed)", g["cf_gain_adj"], "line"),
        ("  Share of profit of equity-accounted investees (removed)", g["cf_eq_income_adj"], "line"),
        ("  Distributions received from equity-accounted investees", g["cf_eq_distributions"], "line"),
        ("Changes in consolidated working capital:", None, "line"),
        ("  (Increase) decrease in trade receivables", g["cf_chg_ar"], "line"),
        ("  (Increase) decrease in inventories", g["cf_chg_inv"], "line"),
        ("  (Increase) decrease in prepayments", g["cf_chg_prepaid"], "line"),
        ("  (Increase) decrease in other current assets", g["cf_chg_oca"], "line"),
        ("  Increase (decrease) in trade payables", g["cf_chg_ap"], "line"),
        ("  Increase (decrease) in accrued liabilities", g["cf_chg_accr"], "line"),
        ("  Increase (decrease) in income taxes payable", g["cf_chg_itp"], "line"),
        ("  Increase (decrease) in deferred revenue", g["cf_chg_def_rev"], "line"),
        ("  Increase (decrease) in other liabilities", g["cf_chg_other_liab"], "line"),
        ("  Pension fund contributions", g["cf_pension_contrib"], "line"),
        ("Net Cash Generated from Operating Activities", cfo, "total"),

        ("Cash Flows from Investing Activities", None, "subheader"),
        ("  Purchases of property, plant & equipment (Capex)", g["cf_capex_ppe"], "line"),
        ("  Purchases / development of intangible assets", g["cf_capex_int"], "line"),
        ("  Proceeds from disposal of PP&E", g["cf_proc_sale_assets"], "line"),
        ("  Acquisition of subsidiaries, net of cash acquired", g["cf_acquisitions"], "line"),
        ("  Purchases of financial investments", g["cf_purch_investments"], "line"),
        ("  Maturities and sales of investments", g["cf_mat_investments"], "line"),
        ("  Loans advanced to related parties", g["cf_loans_rp"], "line"),
        ("Net Cash Used in Investing Activities", cfi, "total"),

        ("Cash Flows from Financing Activities", None, "subheader"),
        ("  Proceeds from issuance of long-term borrowings", g["cf_proc_ltd"], "line"),
        ("  Repayment of long-term borrowings", g["cf_repay_ltd"], "line"),
        ("  Drawdowns on revolving credit facilities", g["cf_proc_rev"], "line"),
        ("  Repayments of revolving credit facilities", g["cf_repay_rev"], "line"),
        ("  Payment of finance lease liabilities", g["cf_fin_lease_pmts"], "line"),
        ("  Proceeds from issuance of ordinary shares", g["cf_proc_stock"], "line"),
        ("  Repurchase of ordinary shares (treasury)", g["cf_repurch_stock"], "line"),
        ("  Dividends paid — parent company common shareholders", g["cf_divs_common"], "line"),
        ("  Dividends paid — preferred shareholders", g["cf_divs_preferred"], "line"),
        ("  Dividends paid to noncontrolling interests", g["cf_divs_nci"], "line"),
        ("  Debt issuance costs paid", g["cf_debt_issuance"], "line"),
        ("Net Cash Used in Financing Activities", cff, "total"),

        ("Effect of exchange rate changes on cash & equivalents", g["cf_fx_cash"], "line"),
        ("Net Increase (Decrease) in Cash & Cash Equivalents", net_chg, "subtotal"),
        ("Cash & cash equivalents, beginning of period", g["cf_beg_cash"], "line"),
        ("Cash & Cash Equivalents, End of Period", ending_cash, "total"),

        ("Supplemental Disclosures", None, "subheader"),
        ("Cash paid for interest", g["interest_expense"], "note"),
        ("Cash paid for income taxes", IS["tax"], "note"),
        ("Non-cash: ROU assets recognised on lease commencement", None, "note"),
        ("Non-cash: Shares issued as acquisition consideration", None, "note"),
    ]
    return dict(rows=rows, cfo=cfo, cfi=cfi, cff=cff, net_chg=net_chg,
                ending_cash=ending_cash, noncash=noncash, wc=wc)


def build_balance_sheet(RE, OCI, EQ, CF):
    g = st.session_state["grp"]
    ending_cash = CF["ending_cash"]
    ending_re = RE["ending_re"]
    ending_aoci = OCI["ending_aoci"]
    nci_bs = EQ["nci_end"]

    net_ar = g["bs_ar_gross"] - g["bs_allowance"] - g["interco_ar_elim"]
    total_inv = g["bs_inventory_rm"]+g["bs_inventory_wip"]+g["bs_inventory_fg"]
    total_ca = (ending_cash + g["bs_str_investments"] + net_ar + total_inv
                + g["bs_prepaid"] + g["bs_other_ca"] + g["bs_assets_held_for_sale"])

    gross_ppe = g["bs_land"]+g["bs_buildings"]+g["bs_machinery"]
    net_ppe = gross_ppe - g["bs_accum_dep"]
    net_intang = g["bs_intangibles_gross"] - g["bs_accum_amort"]
    total_nca = (net_ppe + g["bs_rou_operating"] + g["bs_rou_finance"]
                 + g["bs_goodwill"] + net_intang
                 + g["bs_equity_method_inv"] + g["bs_deferred_tax_assets"] + g["bs_other_nca"])
    total_assets = total_ca + total_nca

    net_ap = g["bs_ap"] - g["interco_ap_elim"]
    total_cl = (net_ap + g["bs_accrued_sal"] + g["bs_accrued_int"] + g["bs_itp"]
                + g["bs_current_ltd"] + g["bs_current_op_lease"] + g["bs_current_fin_lease"]
                + g["bs_deferred_rev_curr"] + g["bs_divs_payable"] + g["bs_other_cl"])
    total_ncl = (g["bs_ltd"] + g["bs_nc_op_lease"] + g["bs_nc_fin_lease"]
                 + g["bs_dtl"] + g["bs_pension"] + g["bs_deferred_rev_nc"] + g["bs_other_ncl"])
    total_liabilities = total_cl + total_ncl

    equity_ex_re_aoci_nci = (g["bs_preferred_par"] + g["bs_common_par"]
                              + g["bs_apic"] - g["bs_treasury"])
    total_parent_equity = equity_ex_re_aoci_nci + ending_re + ending_aoci
    total_equity = total_parent_equity + nci_bs
    total_l_and_e = total_liabilities + total_equity
    balance_check = total_assets - total_l_and_e

    rows = [
        ("CONSOLIDATED BALANCE SHEET", None, "header"),
        (f"As of Period End — {G('fy_current')}", None, "subheader"),
        ("spacer",None,"spacer"),

        ("ASSETS", None, "subheader"),
        ("Current Assets", None, "subheader"),
        ("Cash & cash equivalents  (tied to Consolidated Cash Flow Statement)", ending_cash, "line"),
        ("Short-term financial investments", g["bs_str_investments"], "line"),
        ("Trade receivables, gross", g["bs_ar_gross"], "line"),
        ("  Less: Allowance for expected credit losses", -g["bs_allowance"], "line"),
        ("  Less: Intercompany receivables eliminated on consolidation", -g["interco_ar_elim"], "elim"),
        ("Trade receivables, net", net_ar, "line"),
        ("Inventories — raw materials", g["bs_inventory_rm"], "line"),
        ("Inventories — work in process", g["bs_inventory_wip"], "line"),
        ("Inventories — finished goods", g["bs_inventory_fg"], "line"),
        ("Total inventories", total_inv, "line"),
        ("Prepayments & other current assets", g["bs_prepaid"], "line"),
        ("Other current assets", g["bs_other_ca"], "line"),
        ("Assets classified as held for sale", g["bs_assets_held_for_sale"], "line"),
        ("Total Current Assets", total_ca, "subtotal"),

        ("Non-Current Assets", None, "subheader"),
        ("Land", g["bs_land"], "line"),
        ("Buildings", g["bs_buildings"], "line"),
        ("Plant, machinery & equipment", g["bs_machinery"], "line"),
        ("Gross property, plant & equipment", gross_ppe, "line"),
        ("Less: Accumulated depreciation", -g["bs_accum_dep"], "line"),
        ("PP&E, net", net_ppe, "line"),
        ("Right-of-use assets — operating leases", g["bs_rou_operating"], "line"),
        ("Right-of-use assets — finance leases", g["bs_rou_finance"], "line"),
        ("Goodwill on consolidation", g["bs_goodwill"], "line"),
        ("Other intangible assets, gross", g["bs_intangibles_gross"], "line"),
        ("Less: Accumulated amortisation", -g["bs_accum_amort"], "line"),
        ("Intangible assets, net", net_intang, "line"),
        ("Investments in equity-accounted associates", g["bs_equity_method_inv"], "line"),
        ("Deferred tax assets", g["bs_deferred_tax_assets"], "line"),
        ("Other non-current assets", g["bs_other_nca"], "line"),
        ("Total Non-Current Assets", total_nca, "subtotal"),

        ("TOTAL CONSOLIDATED ASSETS", total_assets, "total"),

        ("LIABILITIES", None, "subheader"),
        ("Current Liabilities", None, "subheader"),
        ("Trade payables, gross", g["bs_ap"], "line"),
        ("  Less: Intercompany payables eliminated on consolidation", -g["interco_ap_elim"], "elim"),
        ("Trade payables, net", net_ap, "line"),
        ("Accrued salaries & employee benefits", g["bs_accrued_sal"], "line"),
        ("Accrued interest payable", g["bs_accrued_int"], "line"),
        ("Income taxes payable", g["bs_itp"], "line"),
        ("Current portion of long-term borrowings", g["bs_current_ltd"], "line"),
        ("Current portion — operating lease liabilities", g["bs_current_op_lease"], "line"),
        ("Current portion — finance lease liabilities", g["bs_current_fin_lease"], "line"),
        ("Deferred revenue, current", g["bs_deferred_rev_curr"], "line"),
        ("Dividends payable", g["bs_divs_payable"], "line"),
        ("Other current liabilities", g["bs_other_cl"], "line"),
        ("Total Current Liabilities", total_cl, "subtotal"),

        ("Non-Current Liabilities", None, "subheader"),
        ("Long-term borrowings", g["bs_ltd"], "line"),
        ("Non-current operating lease liabilities", g["bs_nc_op_lease"], "line"),
        ("Non-current finance lease liabilities", g["bs_nc_fin_lease"], "line"),
        ("Deferred tax liabilities", g["bs_dtl"], "line"),
        ("Pension & post-employment benefit obligations", g["bs_pension"], "line"),
        ("Deferred revenue, non-current", g["bs_deferred_rev_nc"], "line"),
        ("Other non-current liabilities", g["bs_other_ncl"], "line"),
        ("Total Non-Current Liabilities", total_ncl, "subtotal"),

        ("TOTAL CONSOLIDATED LIABILITIES", total_liabilities, "total"),

        ("EQUITY", None, "subheader"),
        ("Equity attributable to shareholders of the parent", None, "subheader"),
        ("  Preferred stock / preference shares, at par", g["bs_preferred_par"], "line"),
        ("  Ordinary / common share capital, at par", g["bs_common_par"], "line"),
        ("  Additional paid-in capital (share premium)", g["bs_apic"], "line"),
        ("  Less: Treasury shares, at cost", -g["bs_treasury"], "line"),
        ("  Accumulated other comprehensive income (loss) — AOCI", ending_aoci, "line"),
        ("  Retained earnings  (tied to Statement of Retained Earnings)", ending_re, "line"),
        ("Total equity attributable to parent shareholders", total_parent_equity, "subtotal"),
        ("Noncontrolling interests (NCI) in subsidiaries", nci_bs, "line"),
        ("TOTAL CONSOLIDATED EQUITY", total_equity, "subtotal"),

        ("TOTAL CONSOLIDATED LIABILITIES AND EQUITY", total_l_and_e, "total"),
        ("Balance check (Assets − L&E, must be 0)", balance_check, "note"),
    ]
    return dict(rows=rows, total_assets=total_assets, total_ca=total_ca, total_nca=total_nca,
                total_liabilities=total_liabilities, total_cl=total_cl, total_ncl=total_ncl,
                total_equity=total_equity, total_parent_equity=total_parent_equity,
                total_l_and_e=total_l_and_e, balance_check=balance_check,
                net_ppe=net_ppe, net_ar=net_ar, total_inv=total_inv,
                gross_ppe=gross_ppe, net_intang=net_intang, net_ap=net_ap)


# ==========================================================================
# SIDEBAR
# ==========================================================================
with st.sidebar:
    st.title("📊 Group Consolidated Financial Statements")
    st.caption("Full intercompany-eliminated, NCI-adjusted 3-statement model")
    st.markdown("---")
    st.markdown(f"**Units:** {UNITS_LABEL}")
    st.markdown(f"**Basis:** {G('reporting_basis')}")
    st.markdown("---")
    if st.button("🔄 Reset to default example", use_container_width=True):
        reset(); st.rerun()
    st.markdown("---")
    st.markdown(
        "**Group features:**\n"
        "- Intercompany revenue/COGS eliminations\n"
        "- Intercompany AR/AP eliminations\n"
        "- Intercompany interest elimination\n"
        "- Noncontrolling interests (NCI)\n"
        "- Goodwill on consolidation\n"
        "- OCI & AOCI roll-forward\n"
        "- NCI dividends in Cash Flow\n"
        "- Segment & geographic revenue splits\n"
        "- Subsidiary register in Notes"
    )

# ==========================================================================
# MAIN PAGE
# ==========================================================================
st.title(G("group_name"))
st.subheader("Applied Consolidated Financial Statements")
st.caption(f"{UNITS_LABEL} · {G('fy_current')} · {G('reporting_basis')}")

tabs = st.tabs([
    "🧮 Inputs",
    "📄 Income Statement",
    "💹 Comprehensive Income",
    "🏛️ Balance Sheet",
    "💵 Cash Flow",
    "📈 Retained Earnings & Equity",
    "🗒️ Notes",
])

# --------------------------------------------------------------------------
# TAB 0 — INPUTS
# --------------------------------------------------------------------------
with tabs[0]:
    st.header("🧮 Master Inputs — Consolidated Group")
    st.info(
        "Edit any value and switch to any statement tab — all six consolidated "
        "statements recalculate live. "
        "**Intercompany eliminations** (revenue, COGS, AR, AP, interest) are "
        "entered here as positive amounts and subtracted automatically. "
        "**Cash** on the Balance Sheet is solved from the Cash Flow Statement."
    )
    g = st.session_state["grp"]

    with st.expander("🏢 Group Identification", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["group_name"] = c1.text_input("Group / parent entity name", g["group_name"], key='k001')
        g["fy_current"] = c2.text_input("Current fiscal year label", g["fy_current"], key='k002')
        g["fy_prior"] = c3.text_input("Prior fiscal year label", g["fy_prior"], key='k003')
        g["reporting_basis"] = st.text_input("Reporting basis", g["reporting_basis"], key='k004')

    with st.expander("🗂️ Subsidiary Register", expanded=False):
        st.caption("List the entities included in the consolidation scope.")
        for i in range(1,5):
            c1,c2,c3 = st.columns([3,2,1])
            g[f"sub{i}_name"] = c1.text_input(f"Subsidiary {i} name", g[f"sub{i}_name"], key=f"sn{i}")
            g[f"sub{i}_country"] = c2.text_input(f"Country", g[f"sub{i}_country"], key=f"sc{i}")
            g[f"sub{i}_ownership"] = c3.number_input(f"Ownership %", value=g[f"sub{i}_ownership"], step=1.0, min_value=0.0, max_value=100.0, key=f"so{i}")

    with st.expander("📄 Revenue (by Segment & Eliminations)", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["rev_segment1"] = c1.number_input(f"Segment 1 — {G('note_seg1_name')} revenue", value=g["rev_segment1"], step=500.0, key='k005')
        g["rev_segment2"] = c2.number_input(f"Segment 2 — {G('note_seg2_name')} revenue", value=g["rev_segment2"], step=500.0, key='k006')
        g["rev_segment3"] = c3.number_input(f"Segment 3 — {G('note_seg3_name')} revenue", value=g["rev_segment3"], step=500.0, key='k007')
        c1,c2,c3 = st.columns(3)
        g["interco_revenue_elim"] = c1.number_input("Intercompany revenue elimination (positive, key='k008')", value=g["interco_revenue_elim"], step=100.0)
        g["sales_returns"] = c2.number_input("Sales returns & allowances", value=g["sales_returns"], step=100.0, key='k009')
        g["sales_discounts"] = c3.number_input("Sales discounts", value=g["sales_discounts"], step=100.0, key='k010')

    with st.expander("📄 Cost of Goods Sold & Interco COGS Elimination", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["cogs_materials"] = c1.number_input("Direct materials", value=g["cogs_materials"], step=500.0, key='k011')
        g["cogs_direct_labor"] = c2.number_input("Direct labor", value=g["cogs_direct_labor"], step=500.0, key='k012')
        g["cogs_overhead"] = c3.number_input("Manufacturing overhead", value=g["cogs_overhead"], step=500.0, key='k013')
        c1,c2,c3 = st.columns(3)
        g["cogs_depreciation"] = c1.number_input("Depreciation in COGS", value=g["cogs_depreciation"], step=100.0, key='k014')
        g["cogs_inventory_writedown"] = c2.number_input("Inventory write-down", value=g["cogs_inventory_writedown"], step=50.0, key='k015')
        g["interco_cogs_elim"] = c3.number_input("Intercompany COGS elimination (positive, key='k016')", value=g["interco_cogs_elim"], step=100.0)
        st.caption("Intercompany COGS elimination removes the cost recognised by the buying entity on goods sold within the group.")

    with st.expander("📄 Operating Expenses", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["sga_salaries"] = c1.number_input("SG&A — Salaries & benefits", value=g["sga_salaries"], step=500.0, key='k017')
        g["sga_marketing"] = c2.number_input("SG&A — Marketing", value=g["sga_marketing"], step=100.0, key='k018')
        g["sga_rd"] = c3.number_input("SG&A — R&D", value=g["sga_rd"], step=100.0, key='k019')
        c1,c2,c3 = st.columns(3)
        g["sga_da"] = c1.number_input("SG&A — Depreciation & amortisation", value=g["sga_da"], step=100.0, key='k020')
        g["sga_bad_debt"] = c2.number_input("SG&A — Provision for credit losses", value=g["sga_bad_debt"], step=50.0, key='k021')
        g["sga_other"] = c3.number_input("SG&A — Other", value=g["sga_other"], step=100.0, key='k022')
        c1,c2,c3 = st.columns(3)
        g["sbc"] = c1.number_input("Share-based compensation", value=g["sbc"], step=50.0, key='k023')
        g["restructuring"] = c2.number_input("Restructuring & severance", value=g["restructuring"], step=50.0, key='k024')
        g["impairment"] = c3.number_input("Asset impairment", value=g["impairment"], step=50.0, key='k025')
        g["acquisition_costs"] = st.number_input("Acquisition-related costs", value=g["acquisition_costs"], step=50.0, key='k026')

    with st.expander("📄 Other Income / Expense, Tax, NCI", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["interest_income"] = c1.number_input("Interest income (group, key='k027')", value=g["interest_income"], step=50.0)
        g["interest_expense"] = c2.number_input("Interest expense (group, key='k028')", value=g["interest_expense"], step=100.0)
        g["interco_interest_elim"] = c3.number_input("Intercompany interest elimination (positive, key='k029')", value=g["interco_interest_elim"], step=50.0)
        c1,c2,c3 = st.columns(3)
        g["gain_loss_assets"] = c1.number_input("Gain/(loss, key='k030') on asset disposals", value=g["gain_loss_assets"], step=50.0)
        g["fx_gain_loss"] = c2.number_input("Foreign exchange gain/(loss, key='k031')", value=g["fx_gain_loss"], step=50.0)
        g["equity_method_income"] = c3.number_input("Share of profit of associates", value=g["equity_method_income"], step=50.0, key='k032')
        c1,c2,c3 = st.columns(3)
        g["bargain_purchase_gain"] = c1.number_input("Bargain purchase gain on acquisition", value=g["bargain_purchase_gain"], step=50.0, key='k033')
        g["other_nonop"] = c2.number_input("Other non-operating income/(expense, key='k034')", value=g["other_nonop"], step=50.0)
        g["eff_tax_rate_pct"] = c3.number_input("Effective tax rate (%, key='k035')", value=g["eff_tax_rate_pct"], step=0.5, min_value=0.0, max_value=100.0)
        c1,c2 = st.columns(2)
        g["deferred_tax_exp"] = c1.number_input("Deferred tax expense/(benefit, key='k036')", value=g["deferred_tax_exp"], step=50.0)
        g["nci_net_income"] = c2.number_input("NCI share of net income", value=g["nci_net_income"], step=50.0, key='k037')
        c1,c2 = st.columns(2)
        g["disc_ops_pretax"] = c1.number_input("Discontinued ops pre-tax income/(loss, key='k038')", value=g["disc_ops_pretax"], step=50.0)
        g["disc_ops_tax"] = c2.number_input("Tax on discontinued ops", value=g["disc_ops_tax"], step=50.0, key='k039')
        c1,c2 = st.columns(2)
        g["preferred_divs"] = c1.number_input("Preferred dividends (IS deduction, key='k040')", value=g["preferred_divs"], step=50.0)
        g["shares_basic"] = c2.number_input("Weighted avg. shares — basic (thousands, key='k041')", value=g["shares_basic"], step=500.0)
        g["dilutive_shares"] = st.number_input("Dilutive effect — options/RSUs (thousands, key='k042')", value=g["dilutive_shares"], step=50.0)

    with st.expander("💹 Other Comprehensive Income (OCI)", expanded=False):
        c1,c2 = st.columns(2)
        g["oci_fx_translation"] = c1.number_input("FX translation adjustment", value=g["oci_fx_translation"], step=50.0, key='k043')
        g["oci_pension_adj"] = c2.number_input("Pension re-measurement (net of tax, key='k044')", value=g["oci_pension_adj"], step=50.0)
        c1,c2 = st.columns(2)
        g["oci_hedging"] = c1.number_input("Cash-flow hedge reserve movement", value=g["oci_hedging"], step=50.0, key='k045')
        g["oci_investments"] = c2.number_input("Fair-value movements on financial investments", value=g["oci_investments"], step=50.0, key='k046')
        st.caption(f"Opening AOCI = {AOCI_BEGINNING:,.0f} (hard-coded; closing AOCI is computed automatically).")

    with st.expander("📈 Retained Earnings", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["re_beginning"] = c1.number_input("Opening retained earnings", value=g["re_beginning"], step=500.0, key='k047')
        g["prior_period_adj"] = c2.number_input("Prior period restatement (net of tax, key='k048')", value=g["prior_period_adj"], step=50.0)
        g["cumeff_acctg_change"] = c3.number_input("Cumulative effect of accounting change", value=g["cumeff_acctg_change"], step=50.0, key='k049')
        c1,c2,c3 = st.columns(3)
        g["common_divs_declared"] = c1.number_input("Common dividends declared", value=g["common_divs_declared"], step=100.0, key='k050')
        g["pref_divs_declared"] = c2.number_input("Preferred dividends declared", value=g["pref_divs_declared"], step=50.0, key='k051')
        g["buyback_re_effect"] = c3.number_input("Treasury buy-back — excess charged to RE", value=g["buyback_re_effect"], step=50.0, key='k052')

    with st.expander("🏛️ Consolidated Balance Sheet — Current Assets (excl. Cash)", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["bs_str_investments"] = c1.number_input("Short-term investments", value=g["bs_str_investments"], step=100.0, key='k053')
        g["bs_ar_gross"] = c2.number_input("Trade receivables, gross", value=g["bs_ar_gross"], step=100.0, key='k054')
        g["bs_allowance"] = c3.number_input("Allowance for expected credit losses", value=g["bs_allowance"], step=50.0, key='k055')
        g["interco_ar_elim"] = st.number_input("Intercompany receivables eliminated (positive, key='k056')", value=g["interco_ar_elim"], step=50.0)
        c1,c2,c3 = st.columns(3)
        g["bs_inventory_rm"] = c1.number_input("Inventories — raw materials", value=g["bs_inventory_rm"], step=100.0, key='k057')
        g["bs_inventory_wip"] = c2.number_input("Inventories — WIP", value=g["bs_inventory_wip"], step=100.0, key='k058')
        g["bs_inventory_fg"] = c3.number_input("Inventories — finished goods", value=g["bs_inventory_fg"], step=100.0, key='k059')
        c1,c2,c3 = st.columns(3)
        g["bs_prepaid"] = c1.number_input("Prepayments", value=g["bs_prepaid"], step=50.0, key='k060')
        g["bs_other_ca"] = c2.number_input("Other current assets", value=g["bs_other_ca"], step=50.0, key='k061')
        g["bs_assets_held_for_sale"] = c3.number_input("Assets held for sale", value=g["bs_assets_held_for_sale"], step=50.0, key='k062')
        st.caption("Cash is solved automatically from the Consolidated Cash Flow Statement.")

    with st.expander("🏛️ Consolidated Balance Sheet — Non-Current Assets", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["bs_land"] = c1.number_input("Land", value=g["bs_land"], step=100.0, key='k063')
        g["bs_buildings"] = c2.number_input("Buildings", value=g["bs_buildings"], step=100.0, key='k064')
        g["bs_machinery"] = c3.number_input("Plant, machinery & equipment", value=g["bs_machinery"], step=100.0, key='k065')
        c1,c2,c3 = st.columns(3)
        g["bs_accum_dep"] = c1.number_input("Accumulated depreciation", value=g["bs_accum_dep"], step=100.0, key='k066')
        g["bs_rou_operating"] = c2.number_input("ROU assets — operating leases", value=g["bs_rou_operating"], step=100.0, key='k067')
        g["bs_rou_finance"] = c3.number_input("ROU assets — finance leases", value=g["bs_rou_finance"], step=50.0, key='k068')
        c1,c2,c3 = st.columns(3)
        g["bs_goodwill"] = c1.number_input("Goodwill on consolidation", value=g["bs_goodwill"], step=100.0, key='k069')
        g["bs_intangibles_gross"] = c2.number_input("Other intangibles, gross", value=g["bs_intangibles_gross"], step=100.0, key='k070')
        g["bs_accum_amort"] = c3.number_input("Accumulated amortisation", value=g["bs_accum_amort"], step=100.0, key='k071')
        c1,c2,c3 = st.columns(3)
        g["bs_equity_method_inv"] = c1.number_input("Investments in associates (equity method, key='k072')", value=g["bs_equity_method_inv"], step=100.0)
        g["bs_deferred_tax_assets"] = c2.number_input("Deferred tax assets", value=g["bs_deferred_tax_assets"], step=50.0, key='k073')
        g["bs_other_nca"] = c3.number_input("Other non-current assets", value=g["bs_other_nca"], step=50.0, key='k074')

    with st.expander("🏛️ Consolidated Balance Sheet — Current Liabilities", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["bs_ap"] = c1.number_input("Trade payables, gross", value=g["bs_ap"], step=100.0, key='k075')
        g["interco_ap_elim"] = c2.number_input("Intercompany payables eliminated (positive, key='k076')", value=g["interco_ap_elim"], step=50.0)
        g["bs_accrued_sal"] = c3.number_input("Accrued salaries & benefits", value=g["bs_accrued_sal"], step=100.0, key='k077')
        c1,c2,c3 = st.columns(3)
        g["bs_accrued_int"] = c1.number_input("Accrued interest", value=g["bs_accrued_int"], step=50.0, key='k078')
        g["bs_itp"] = c2.number_input("Income taxes payable", value=g["bs_itp"], step=50.0, key='k079')
        g["bs_current_ltd"] = c3.number_input("Current portion of borrowings", value=g["bs_current_ltd"], step=100.0, key='k080')
        c1,c2,c3 = st.columns(3)
        g["bs_current_op_lease"] = c1.number_input("Current operating lease liability", value=g["bs_current_op_lease"], step=50.0, key='k081')
        g["bs_current_fin_lease"] = c2.number_input("Current finance lease liability", value=g["bs_current_fin_lease"], step=50.0, key='k082')
        g["bs_deferred_rev_curr"] = c3.number_input("Deferred revenue, current", value=g["bs_deferred_rev_curr"], step=50.0, key='k083')
        c1,c2 = st.columns(2)
        g["bs_divs_payable"] = c1.number_input("Dividends payable", value=g["bs_divs_payable"], step=50.0, key='k084')
        g["bs_other_cl"] = c2.number_input("Other current liabilities", value=g["bs_other_cl"], step=50.0, key='k085')

    with st.expander("🏛️ Consolidated Balance Sheet — Non-Current Liabilities", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["bs_ltd"] = c1.number_input("Long-term borrowings", value=g["bs_ltd"], step=100.0, key='k086')
        g["bs_nc_op_lease"] = c2.number_input("Non-current operating lease liability", value=g["bs_nc_op_lease"], step=100.0, key='k087')
        g["bs_nc_fin_lease"] = c3.number_input("Non-current finance lease liability", value=g["bs_nc_fin_lease"], step=50.0, key='k088')
        c1,c2,c3 = st.columns(3)
        g["bs_dtl"] = c1.number_input("Deferred tax liabilities", value=g["bs_dtl"], step=50.0, key='k089')
        g["bs_pension"] = c2.number_input("Pension & post-employment obligations", value=g["bs_pension"], step=100.0, key='k090')
        g["bs_deferred_rev_nc"] = c3.number_input("Deferred revenue, non-current", value=g["bs_deferred_rev_nc"], step=50.0, key='k091')
        g["bs_other_ncl"] = st.number_input("Other non-current liabilities", value=g["bs_other_ncl"], step=50.0, key='k092')

    with st.expander("🏛️ Consolidated Equity (excl. RE, AOCI, NCI — those are computed)", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["bs_preferred_par"] = c1.number_input("Preference shares, at par", value=g["bs_preferred_par"], step=100.0, key='k093')
        g["bs_common_par"] = c2.number_input("Ordinary share capital, at par", value=g["bs_common_par"], step=100.0, key='k094')
        g["bs_apic"] = c3.number_input("Share premium / Additional paid-in capital", value=g["bs_apic"], step=100.0, key='k095')
        g["bs_treasury"] = st.number_input("Treasury shares, at cost (contra-equity, key='k096')", value=g["bs_treasury"], step=100.0)
        st.caption("Retained earnings, AOCI, and NCI are all computed from the other statements and flow in automatically.")

    with st.expander("💵 Cash Flow — Beginning Cash & Operating Adjustments", expanded=False):
        g["cf_beg_cash"] = st.number_input("Cash, beginning of period", value=g["cf_beg_cash"], step=100.0, key='k097')
        c1,c2,c3 = st.columns(3)
        g["cf_dep_total"] = c1.number_input("Depreciation (group total, key='k098')", value=g["cf_dep_total"], step=100.0)
        g["cf_amort_total"] = c2.number_input("Amortisation (group total, key='k099')", value=g["cf_amort_total"], step=50.0)
        g["cf_def_tax"] = c3.number_input("Deferred tax", value=g["cf_def_tax"], step=50.0, key='k100')
        c1,c2,c3 = st.columns(3)
        g["cf_sbc"] = c1.number_input("Share-based compensation", value=g["cf_sbc"], step=50.0, key='k101')
        g["cf_prov_doubtful"] = c2.number_input("Provision for credit losses", value=g["cf_prov_doubtful"], step=50.0, key='k102')
        g["cf_impairment_nc"] = c3.number_input("Non-cash impairment", value=g["cf_impairment_nc"], step=50.0, key='k103')
        c1,c2,c3 = st.columns(3)
        g["cf_gain_adj"] = c1.number_input("Remove gain on disposal (negative, key='k104')", value=g["cf_gain_adj"], step=50.0)
        g["cf_eq_income_adj"] = c2.number_input("Remove equity-method income (negative, key='k105')", value=g["cf_eq_income_adj"], step=50.0)
        g["cf_eq_distributions"] = c3.number_input("Distributions from associates", value=g["cf_eq_distributions"], step=50.0, key='k106')

    with st.expander("💵 Cash Flow — Working Capital Changes", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["cf_chg_ar"] = c1.number_input("Change in trade receivables", value=g["cf_chg_ar"], step=50.0, key='k107')
        g["cf_chg_inv"] = c2.number_input("Change in inventories", value=g["cf_chg_inv"], step=50.0, key='k108')
        g["cf_chg_prepaid"] = c3.number_input("Change in prepayments", value=g["cf_chg_prepaid"], step=50.0, key='k109')
        c1,c2,c3 = st.columns(3)
        g["cf_chg_oca"] = c1.number_input("Change in other current assets", value=g["cf_chg_oca"], step=50.0, key='k110')
        g["cf_chg_ap"] = c2.number_input("Change in trade payables", value=g["cf_chg_ap"], step=50.0, key='k111')
        g["cf_chg_accr"] = c3.number_input("Change in accrued liabilities", value=g["cf_chg_accr"], step=50.0, key='k112')
        c1,c2,c3 = st.columns(3)
        g["cf_chg_itp"] = c1.number_input("Change in income taxes payable", value=g["cf_chg_itp"], step=50.0, key='k113')
        g["cf_chg_def_rev"] = c2.number_input("Change in deferred revenue", value=g["cf_chg_def_rev"], step=50.0, key='k114')
        g["cf_chg_other_liab"] = c3.number_input("Change in other liabilities", value=g["cf_chg_other_liab"], step=50.0, key='k115')
        g["cf_pension_contrib"] = st.number_input("Pension contributions paid", value=g["cf_pension_contrib"], step=50.0, key='k116')

    with st.expander("💵 Cash Flow — Investing Activities (incl. Acquisitions)", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["cf_capex_ppe"] = c1.number_input("Capex — PP&E", value=g["cf_capex_ppe"], step=100.0, key='k117')
        g["cf_capex_int"] = c2.number_input("Capex — Intangibles", value=g["cf_capex_int"], step=100.0, key='k118')
        g["cf_proc_sale_assets"] = c3.number_input("Proceeds from asset disposals", value=g["cf_proc_sale_assets"], step=50.0, key='k119')
        c1,c2,c3 = st.columns(3)
        g["cf_acquisitions"] = c1.number_input("Acquisition of subsidiaries, net of cash", value=g["cf_acquisitions"], step=100.0, key='k120')
        g["cf_purch_investments"] = c2.number_input("Purchases of investments", value=g["cf_purch_investments"], step=100.0, key='k121')
        g["cf_mat_investments"] = c3.number_input("Maturities / sales of investments", value=g["cf_mat_investments"], step=100.0, key='k122')
        g["cf_loans_rp"] = st.number_input("Loans to related parties", value=g["cf_loans_rp"], step=50.0, key='k123')

    with st.expander("💵 Cash Flow — Financing Activities (incl. NCI Dividends)", expanded=False):
        c1,c2,c3 = st.columns(3)
        g["cf_proc_ltd"] = c1.number_input("Proceeds from borrowings", value=g["cf_proc_ltd"], step=100.0, key='k124')
        g["cf_repay_ltd"] = c2.number_input("Repayment of borrowings", value=g["cf_repay_ltd"], step=100.0, key='k125')
        g["cf_proc_rev"] = c3.number_input("Drawdown on revolving credit", value=g["cf_proc_rev"], step=100.0, key='k126')
        c1,c2,c3 = st.columns(3)
        g["cf_repay_rev"] = c1.number_input("Repayment of revolving credit", value=g["cf_repay_rev"], step=100.0, key='k127')
        g["cf_fin_lease_pmts"] = c2.number_input("Finance lease principal payments", value=g["cf_fin_lease_pmts"], step=50.0, key='k128')
        g["cf_proc_stock"] = c3.number_input("Proceeds from share issuance", value=g["cf_proc_stock"], step=50.0, key='k129')
        c1,c2,c3 = st.columns(3)
        g["cf_repurch_stock"] = c1.number_input("Share repurchases (treasury, key='k130')", value=g["cf_repurch_stock"], step=100.0)
        g["cf_divs_common"] = c2.number_input("Dividends paid — common", value=g["cf_divs_common"], step=50.0, key='k131')
        g["cf_divs_preferred"] = c3.number_input("Dividends paid — preferred", value=g["cf_divs_preferred"], step=50.0, key='k132')
        c1,c2 = st.columns(2)
        g["cf_divs_nci"] = c1.number_input("Dividends paid to NCI shareholders", value=g["cf_divs_nci"], step=50.0, key='k133')
        g["cf_debt_issuance"] = c2.number_input("Debt issuance costs paid", value=g["cf_debt_issuance"], step=50.0, key='k134')
        g["cf_fx_cash"] = st.number_input("FX effect on cash & equivalents", value=g["cf_fx_cash"], step=50.0, key='k135')

    with st.expander("🗒️ Notes — Segments, Debt, Pensions, SBC, Leases, Tax, Geography", expanded=False):
        st.markdown("**Segment reporting**")
        for i in range(1,4):
            c1,c2,c3,c4 = st.columns([2,2,2,2])
            g[f"note_seg{i}_name"] = c1.text_input(f"Segment {i} name", g[f"note_seg{i}_name"], key=f"sname{i}")
            g[f"note_seg{i}_rev"] = c2.number_input(f"Seg {i} revenue", value=g[f"note_seg{i}_rev"], step=100.0, key=f"srev{i}")
            g[f"note_seg{i}_opinc"] = c3.number_input(f"Seg {i} op. income", value=g[f"note_seg{i}_opinc"], step=100.0, key=f"soinc{i}")
            g[f"note_seg{i}_assets"] = c4.number_input(f"Seg {i} assets", value=g[f"note_seg{i}_assets"], step=100.0, key=f"sass{i}")

        st.markdown("**Goodwill by segment**")
        c1,c2,c3 = st.columns(3)
        g["note_goodwill_seg1"] = c1.number_input("Goodwill — Seg 1", value=g["note_goodwill_seg1"], step=100.0, key='k136')
        g["note_goodwill_seg2"] = c2.number_input("Goodwill — Seg 2", value=g["note_goodwill_seg2"], step=100.0, key='k137')
        g["note_goodwill_seg3"] = c3.number_input("Goodwill — Seg 3", value=g["note_goodwill_seg3"], step=100.0, key='k138')

        st.markdown("**Geographic revenue**")
        c1,c2,c3 = st.columns(3)
        g["note_geo_rev_americas"] = c1.number_input("Americas revenue", value=g["note_geo_rev_americas"], step=100.0, key='k139')
        g["note_geo_rev_emea"] = c2.number_input("EMEA revenue", value=g["note_geo_rev_emea"], step=100.0, key='k140')
        g["note_geo_rev_apac"] = c3.number_input("Asia Pacific revenue", value=g["note_geo_rev_apac"], step=100.0, key='k141')

        st.markdown("**Debt maturities**")
        c1,c2,c3 = st.columns(3)
        g["note_debt_rate"] = c1.number_input("Wtd. avg. borrowing rate (%, key='k142')", value=g["note_debt_rate"], step=0.1)
        g["note_debt_yr1"] = c2.number_input("Maturing — Year 1", value=g["note_debt_yr1"], step=100.0, key='k143')
        g["note_debt_yr2"] = c3.number_input("Maturing — Year 2", value=g["note_debt_yr2"], step=100.0, key='k144')
        c1,c2,c3 = st.columns(3)
        g["note_debt_yr3"] = c1.number_input("Maturing — Year 3", value=g["note_debt_yr3"], step=100.0, key='k145')
        g["note_debt_yr4"] = c2.number_input("Maturing — Year 4", value=g["note_debt_yr4"], step=100.0, key='k146')
        g["note_debt_yr5"] = c3.number_input("Maturing — Year 5", value=g["note_debt_yr5"], step=100.0, key='k147')
        g["note_debt_thereafter"] = st.number_input("Maturing — Thereafter", value=g["note_debt_thereafter"], step=100.0, key='k148')

        st.markdown("**Pension**")
        c1,c2 = st.columns(2)
        g["note_pension_disc"] = c1.number_input("Discount rate (%, key='k149')", value=g["note_pension_disc"], step=0.1)
        g["note_pension_ret"] = c2.number_input("Expected return on assets (%, key='k150')", value=g["note_pension_ret"], step=0.1)
        c1,c2 = st.columns(2)
        g["note_pension_pbo"] = c1.number_input("Projected benefit obligation", value=g["note_pension_pbo"], step=100.0, key='k151')
        g["note_pension_assets"] = c2.number_input("Fair value of plan assets", value=g["note_pension_assets"], step=100.0, key='k152')

        st.markdown("**SBC, Leases, Tax, Contingencies**")
        c1,c2,c3 = st.columns(3)
        g["note_sbc_unrec"] = c1.number_input("Unrecognised SBC expense", value=g["note_sbc_unrec"], step=100.0, key='k153')
        g["note_sbc_period"] = c2.number_input("Wtd. avg. recognition period (yrs, key='k154')", value=g["note_sbc_period"], step=0.1)
        g["note_lease_op_exp"] = c3.number_input("Operating lease expense", value=g["note_lease_op_exp"], step=50.0, key='k155')
        c1,c2,c3 = st.columns(3)
        g["note_lease_term"] = c1.number_input("Wtd. avg. remaining lease term (yrs, key='k156')", value=g["note_lease_term"], step=0.1)
        g["note_lease_rate"] = c2.number_input("Wtd. avg. lease discount rate (%, key='k157')", value=g["note_lease_rate"], step=0.1)
        g["note_stat_tax_rate"] = c3.number_input("Statutory tax rate (%, key='k158')", value=g["note_stat_tax_rate"], step=0.5)
        c1,c2 = st.columns(2)
        g["note_contingency_accrued"] = c1.number_input("Legal contingencies accrued", value=g["note_contingency_accrued"], step=50.0, key='k159')
        g["note_contingency_possible"] = c2.number_input("Reasonably possible losses (disclosed, key='k160')", value=g["note_contingency_possible"], step=50.0)
        c1,c2 = st.columns(2)
        g["note_rpt"] = c1.number_input("Related-party transactions", value=g["note_rpt"], step=50.0, key='k161')
        g["note_subsequent"] = c2.number_input("Subsequent event amount (if any, key='k162')", value=g["note_subsequent"], step=50.0)
        g["note_unrealised_interco_profit"] = st.number_input("Unrealised intercompany profit remaining in inventory", value=g["note_unrealised_interco_profit"], step=50.0, key='k163')

    st.success("✅ All inputs saved. Switch to any tab to see consolidated statements update live.")

# ==========================================================================
# BUILD ALL STATEMENTS (single pass)
# ==========================================================================
IS  = build_income_statement()
OCI = build_oci(IS)
RE  = build_retained_earnings(IS)
EQ  = build_equity_statement(IS, OCI, RE)
CF  = build_cash_flow(IS)
BS  = build_balance_sheet(RE, OCI, EQ, CF)

# --------------------------------------------------------------------------
# TAB 1 — INCOME STATEMENT
# --------------------------------------------------------------------------
with tabs[1]:
    render(IS["rows"], col2_header=G("fy_current"))
    with st.expander("📌 Group margin analysis"):
        gm = IS["gross_profit"]/IS["net_rev"]*100 if IS["net_rev"] else 0
        om = IS["op_income"]/IS["net_rev"]*100 if IS["net_rev"] else 0
        nm = IS["net_income"]/IS["net_rev"]*100 if IS["net_rev"] else 0
        npm = IS["ni_parent"]/IS["net_rev"]*100 if IS["net_rev"] else 0
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Gross Margin", pct(gm))
        c2.metric("Operating Margin", pct(om))
        c3.metric("Net Margin (Group)", pct(nm))
        c4.metric("Net Margin (Parent)", pct(npm))
        st.caption(
            f"Intercompany revenue eliminated: {fmt(G('interco_revenue_elim'))} | "
            f"Intercompany COGS eliminated: {fmt(G('interco_cogs_elim'))} | "
            f"Intercompany interest eliminated: {fmt(G('interco_interest_elim'))}"
        )

# --------------------------------------------------------------------------
# TAB 2 — COMPREHENSIVE INCOME
# --------------------------------------------------------------------------
with tabs[2]:
    render(OCI["rows"], col2_header=G("fy_current"))
    st.caption(f"Opening AOCI: {fmt(AOCI_BEGINNING)} → Closing AOCI: {fmt(OCI['ending_aoci'])}")

# --------------------------------------------------------------------------
# TAB 3 — BALANCE SHEET
# --------------------------------------------------------------------------
with tabs[3]:
    render(BS["rows"], col2_header=G("fy_current"))
    if abs(BS["balance_check"]) > 0.5:
        st.error(f"⚠️ Consolidated balance sheet does not balance by {fmt(BS['balance_check'])}. Check inputs.")
    else:
        st.success("✅ Consolidated balance sheet balances (Total Assets = Total Liabilities + Equity).")
    with st.expander("📌 Consolidated financial health ratios"):
        curr = BS["total_ca"]/BS["total_cl"] if BS["total_cl"] else 0
        dte = BS["total_liabilities"]/BS["total_equity"] if BS["total_equity"] else 0
        c1,c2 = st.columns(2)
        c1.metric("Current Ratio", f"{curr:.2f}x")
        c2.metric("Total Debt-to-Equity", f"{dte:.2f}x")

# --------------------------------------------------------------------------
# TAB 4 — CASH FLOW
# --------------------------------------------------------------------------
with tabs[4]:
    render(CF["rows"], col2_header=G("fy_current"))
    st.success("✅ Ending cash ties into the Consolidated Balance Sheet.")
    with st.expander("📌 Free cash flow"):
        fcf = CF["cfo"] + G("cf_capex_ppe") + G("cf_capex_int")
        st.metric("Free Cash Flow (CFO + Capex)", fmt(fcf))
        st.metric("Cash Conversion (CFO / Net Income)", f"{CF['cfo']/IS['net_income']*100:.1f}%" if IS["net_income"] else "n/a")

# --------------------------------------------------------------------------
# TAB 5 — RETAINED EARNINGS & EQUITY
# --------------------------------------------------------------------------
with tabs[5]:
    render(RE["rows"], col2_header=G("fy_current"))
    st.markdown("---")
    render(EQ["rows"], col2_header=G("fy_current"))

# --------------------------------------------------------------------------
# TAB 6 — NOTES
# --------------------------------------------------------------------------
with tabs[6]:
    st.header("🗒️ Notes to the Consolidated Financial Statements")
    st.caption(f"{G('group_name')} — Notes for the year ended {G('fy_current')}")

    st.markdown("### Note 1 — Basis of Consolidation & Significant Accounting Policies")
    st.markdown(
        "**Basis of consolidation:** The consolidated financial statements incorporate "
        "the financial statements of the parent entity and all subsidiaries controlled "
        "by the Group. Control is assessed in accordance with IFRS 10 / ASC 810. "
        "All intercompany transactions, balances, income, expenses, unrealised profits "
        "and losses on transactions between group entities are fully eliminated.\n\n"
        "**Business combinations:** Acquisitions are accounted for using the acquisition "
        "method. Goodwill represents the excess of consideration transferred, plus the "
        "recognised amount of any NCI, over the fair value of the net identifiable assets "
        "acquired.\n\n"
        "**Noncontrolling interests (NCI):** NCI are measured at their proportionate share "
        "of the acquiree's net identifiable assets at the acquisition date. The NCI share "
        "of profit or loss and OCI is presented separately in the consolidated Income "
        "Statement and Statement of Comprehensive Income.\n\n"
        "**Foreign currency translation:** The functional currency of each entity is the "
        "local currency. On consolidation, assets and liabilities are translated at the "
        "closing rate; income and expenses at average rates. Translation differences are "
        "recognised in OCI and accumulated in the foreign currency translation reserve within equity.\n\n"
        "**Revenue recognition:** Revenue is recognised when, or as, performance obligations "
        "are satisfied. Product revenue is point-in-time; service revenue is recognised "
        "over the service period."
    )

    st.markdown("### Note 2 — Subsidiaries Included in Consolidation")
    sub_data = {
        "Subsidiary": [G(f"sub{i}_name") for i in range(1,5)],
        "Country": [G(f"sub{i}_country") for i in range(1,5)],
        "Ownership %": [G(f"sub{i}_ownership") for i in range(1,5)],
        "Method": ["Full consolidation" if G(f"sub{i}_ownership")>=50 else "Equity method" for i in range(1,5)],
    }
    st.dataframe(pd.DataFrame(sub_data), hide_index=True, use_container_width=True)

    st.markdown("### Note 3 — Intercompany Eliminations")
    interco_total = G("interco_revenue_elim")
    elim_table = pd.DataFrame({
        "Elimination": ["Revenue & COGS (intercompany sales)", "AR & AP (intercompany balances)",
                        "Interest income & expense (intercompany loans)",
                        "Unrealised profit remaining in consolidated inventory"],
        "Amount Eliminated": [G("interco_revenue_elim"), G("interco_ar_elim"),
                               G("interco_interest_elim"), G("note_unrealised_interco_profit")],
    })
    st.dataframe(elim_table, hide_index=True, use_container_width=True)

    st.markdown("### Note 4 — Segment Reporting")
    seg_rev_total = G("note_seg1_rev")+G("note_seg2_rev")+G("note_seg3_rev")
    seg_opinc_total = G("note_seg1_opinc")+G("note_seg2_opinc")+G("note_seg3_opinc")
    seg_assets_total = G("note_seg1_assets")+G("note_seg2_assets")+G("note_seg3_assets")
    seg_df = pd.DataFrame({
        "Segment": [G("note_seg1_name"), G("note_seg2_name"), G("note_seg3_name"), "Total"],
        "Revenue": [G("note_seg1_rev"), G("note_seg2_rev"), G("note_seg3_rev"), seg_rev_total],
        "Operating Income": [G("note_seg1_opinc"), G("note_seg2_opinc"), G("note_seg3_opinc"), seg_opinc_total],
        "Segment Assets": [G("note_seg1_assets"), G("note_seg2_assets"), G("note_seg3_assets"), seg_assets_total],
        "Op. Margin %": [pct(G(f"note_seg{i}_opinc")/G(f"note_seg{i}_rev")*100 if G(f"note_seg{i}_rev") else 0) for i in range(1,4)] + [""],
    })
    st.dataframe(seg_df, hide_index=True, use_container_width=True)

    st.markdown("### Note 5 — Geographic Revenue")
    geo_total = G("note_geo_rev_americas")+G("note_geo_rev_emea")+G("note_geo_rev_apac")
    geo_df = pd.DataFrame({
        "Geography": ["Americas", "EMEA", "Asia Pacific", "Total"],
        "Revenue": [G("note_geo_rev_americas"), G("note_geo_rev_emea"), G("note_geo_rev_apac"), geo_total],
        "% of Total": [pct(G("note_geo_rev_americas")/geo_total*100 if geo_total else 0),
                       pct(G("note_geo_rev_emea")/geo_total*100 if geo_total else 0),
                       pct(G("note_geo_rev_apac")/geo_total*100 if geo_total else 0), "100.0%"],
    })
    st.dataframe(geo_df, hide_index=True, use_container_width=True)

    st.markdown("### Note 6 — Goodwill on Consolidation")
    gw_total = G("note_goodwill_seg1")+G("note_goodwill_seg2")+G("note_goodwill_seg3")
    gw_df = pd.DataFrame({
        "Segment": [G("note_seg1_name"), G("note_seg2_name"), G("note_seg3_name"), "Total goodwill"],
        "Goodwill": [G("note_goodwill_seg1"), G("note_goodwill_seg2"), G("note_goodwill_seg3"), gw_total],
    })
    st.dataframe(gw_df, hide_index=True, use_container_width=True)
    st.caption("Goodwill is tested for impairment at least annually at the cash-generating unit (CGU) level.")

    st.markdown("### Note 7 — Noncontrolling Interests (NCI)")
    nci_df = pd.DataFrame({
        "Item": ["Opening NCI balance", "NCI share of net income", "Dividends paid to NCI", "Closing NCI balance"],
        "Amount": [NCI_BS_BEGINNING, G("nci_net_income"), -G("cf_divs_nci"), EQ["nci_end"]],
    })
    st.dataframe(nci_df, hide_index=True, use_container_width=True)
    st.caption(
        f"NCI arises from {G('sub2_name')} ({G('sub2_ownership'):.0f}% owned) and "
        f"{G('sub4_name')} ({G('sub4_ownership'):.0f}% owned). "
        f"NCI share = {100-G('sub2_ownership'):.0f}% and {100-G('sub4_ownership'):.0f}% respectively."
    )

    st.markdown("### Note 8 — Other Comprehensive Income (OCI) Components")
    oci_df = pd.DataFrame({
        "Component": ["FX translation adjustments", "Pension re-measurement", "Cash-flow hedge reserve", "Investments at FVTOCI", "Total OCI"],
        "Amount (net of tax)": [G("oci_fx_translation"), G("oci_pension_adj"), G("oci_hedging"), G("oci_investments"), OCI["total_oci"]],
    })
    st.dataframe(oci_df, hide_index=True, use_container_width=True)

    st.markdown("### Note 9 — Inventories")
    inv_df = pd.DataFrame({
        "Item": ["Raw materials", "Work in process", "Finished goods", "Total inventories"],
        G("fy_current"): [G("bs_inventory_rm"), G("bs_inventory_wip"), G("bs_inventory_fg"),
                          G("bs_inventory_rm")+G("bs_inventory_wip")+G("bs_inventory_fg")],
    })
    st.dataframe(inv_df, hide_index=True, use_container_width=True)

    st.markdown("### Note 10 — Property, Plant & Equipment")
    gross_ppe = G("bs_land")+G("bs_buildings")+G("bs_machinery")
    ppe_df = pd.DataFrame({
        "Item": ["Land", "Buildings", "Plant, machinery & equipment", "Gross PP&E", "Less: Accumulated depreciation", "PP&E, net"],
        G("fy_current"): [G("bs_land"), G("bs_buildings"), G("bs_machinery"),
                          gross_ppe, -G("bs_accum_dep"), gross_ppe-G("bs_accum_dep")],
    })
    st.dataframe(ppe_df, hide_index=True, use_container_width=True)

    st.markdown("### Note 11 — Leases")
    c1,c2,c3 = st.columns(3)
    c1.metric("Operating lease expense", fmt(G("note_lease_op_exp")))
    c2.metric("Wtd. avg. remaining term", f"{G('note_lease_term'):.1f} yrs")
    c3.metric("Wtd. avg. discount rate", pct(G("note_lease_rate")))

    st.markdown("### Note 12 — Borrowings and Debt Maturities")
    debt_total = sum(G(f"note_debt_yr{i}") for i in range(1,6)) + G("note_debt_thereafter")
    debt_df = pd.DataFrame({
        "Period": ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Thereafter", "Total"],
        "Maturity": [G(f"note_debt_yr{i}") for i in range(1,6)] + [G("note_debt_thereafter"), debt_total],
    })
    st.dataframe(debt_df, hide_index=True, use_container_width=True)
    st.caption(f"Weighted average interest rate on outstanding borrowings: {pct(G('note_debt_rate'))}")

    st.markdown("### Note 13 — Pension & Post-Employment Benefits")
    funded = G("note_pension_assets") - G("note_pension_pbo")
    c1,c2,c3 = st.columns(3)
    c1.metric("Projected benefit obligation (PBO)", fmt(G("note_pension_pbo")))
    c2.metric("Fair value of plan assets", fmt(G("note_pension_assets")))
    c3.metric("Funded status (deficit)", fmt(funded))
    st.caption(f"Discount rate: {pct(G('note_pension_disc'))} · Expected return: {pct(G('note_pension_ret'))}")

    st.markdown("### Note 14 — Share-Based Compensation")
    c1,c2 = st.columns(2)
    c1.metric("SBC recognised this period", fmt(G("sbc")))
    c2.metric("Unrecognised SBC (to be expensed)", fmt(G("note_sbc_unrec")))
    st.caption(f"To be recognised over a weighted average period of {G('note_sbc_period'):.1f} years.")

    st.markdown("### Note 15 — Income Taxes")
    stat_diff = G("eff_tax_rate_pct") - G("note_stat_tax_rate")
    tax_df = pd.DataFrame({
        "Item": ["Statutory rate", "Effective rate", "Difference"],
        "Rate (%)": [G("note_stat_tax_rate"), G("eff_tax_rate_pct"), stat_diff],
    })
    st.dataframe(tax_df, hide_index=True, use_container_width=True)
    st.caption(f"Deferred tax (expense)/benefit included in tax provision: {fmt(G('deferred_tax_exp'))}")

    st.markdown("### Note 16 — Commitments and Contingencies")
    st.markdown(
        f"- Legal contingencies accrued: **{fmt(G('note_contingency_accrued'))}**\n"
        f"- Reasonably possible losses (disclosed, not accrued): **{fmt(G('note_contingency_possible'))}**\n"
        f"- The Group is involved in various legal and regulatory proceedings arising in "
        f"the ordinary course of business across its jurisdictions of operation."
    )

    st.markdown("### Note 17 — Related Party Transactions")
    st.markdown(f"Total related-party transactions in the period: **{fmt(G('note_rpt'))}**.")
    st.caption("Key management personnel compensation and transactions with associates are disclosed separately in the Group's full annual report.")

    st.markdown("### Note 18 — Earnings Per Share")
    ni_common = IS["ni_common"]
    dil = IS["diluted_shares"]
    eps_df = pd.DataFrame({
        "Item": ["Net income available to common shareholders (parent)",
                 "Wtd. avg. shares — basic", "Dilutive effect", "Wtd. avg. shares — diluted",
                 "Basic EPS", "Diluted EPS"],
        "Value": [ni_common, G("shares_basic"), G("dilutive_shares"), dil, IS["basic_eps"], IS["diluted_eps"]],
    })
    st.dataframe(eps_df, hide_index=True, use_container_width=True)

    st.markdown("### Note 19 — Subsequent Events")
    if G("note_subsequent"):
        st.markdown(f"A material subsequent event with an estimated financial impact of **{fmt(G('note_subsequent'))}** was identified after the balance sheet date.")
    else:
        st.markdown("Management evaluated events occurring after the balance sheet date. No material subsequent events requiring disclosure were identified.")

# ==========================================================================
# FOOTER
# ==========================================================================
st.markdown("---")
st.caption(
    "All six consolidated statements (Income Statement, Comprehensive Income, Balance Sheet, "
    "Cash Flow, Retained Earnings & Equity Statement, and Notes) are derived live from the "
    "**🧮 Inputs** tab. Intercompany eliminations, NCI, OCI, and ending cash are all computed "
    "automatically — no manual re-entry between statements."
)