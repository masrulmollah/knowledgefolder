import streamlit as st
import pandas as pd

# ── Custom CSS — matches Overview page color palette ─────────────────────────
st.markdown("""
<style>
    /* ── Section headers — matches module card header style ── */
    .section-header {
        background: linear-gradient(90deg, #2E86C1, #3498DB);
        color: #ffffff;
        padding: 10px 18px;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: 700;
        margin: 18px 0 10px 0;
        letter-spacing: 0.4px;
    }

    /* ── Statement rows ── */
    .row-label {
        font-size: 0.88rem;
        color: #2C3E50;
        padding: 3px 0;
    }
    .row-label-bold {
        font-size: 0.90rem;
        color: #1A252F;
        font-weight: 700;
        padding: 3px 0;
    }
    .row-subtotal {
        font-size: 0.89rem;
        color: #2E86C1;
        font-weight: 600;
        border-top: 1px solid #AED6F1;
        padding: 5px 0 3px 0;
    }
    .row-total {
        font-size: 0.93rem;
        color: #1A252F;
        font-weight: 700;
        border-top: 2.5px solid #2E86C1;
        padding: 6px 0 3px 0;
    }

    /* ── Ratio cards — uses Overview module card style ── */
    .ratio-card {
        border-radius: 8px;
        padding: 14px 16px;
        margin-bottom: 10px;
        border-left: 5px solid #999;
        min-height: 155px;
    }
    /* Green  — #27AE60 like Module 2 */
    .ratio-card-green  { background-color: #27AE6022; border-left-color: #27AE60; }
    /* Amber  — #F39C12 like Module 14 */
    .ratio-card-amber  { background-color: #F39C1222; border-left-color: #F39C12; }
    /* Red    — #E74C3C like Module 5/13 */
    .ratio-card-red    { background-color: #E74C3C22; border-left-color: #E74C3C; }
    /* Neutral — #2C3E50 like Module 8 */
    .ratio-card-neutral{ background-color: #2C3E5015; border-left-color: #95A5A6; }

    .ratio-name  { font-size: 0.88rem; font-weight: 700; color: #1A252F; }
    .ratio-value { font-size: 1.45rem; font-weight: 800; margin: 4px 0; }
    .ratio-val-green   { color: #1E8449; }
    .ratio-val-amber   { color: #D68910; }
    .ratio-val-red     { color: #C0392B; }
    .ratio-val-neutral { color: #717D7E; }
    .ratio-formula { font-size: 0.74rem; color: #5D6D7E; font-style: italic; margin-top: 4px; }
    .ratio-bench   { font-size: 0.74rem; color: #717D7E; margin-top: 3px; }
    .ratio-status  { font-size: 0.78rem; font-weight: 700; margin-top: 5px; }
    .status-green  { color: #1E8449; }
    .status-amber  { color: #D68910; }
    .status-red    { color: #C0392B; }

    /* ── Number colours in statements ── */
    .num-positive { color: #2E86C1; font-weight: 600; }
    .num-negative { color: #E74C3C; font-weight: 600; }
    .num-total    { color: #1A252F; font-weight: 700; }

    /* ── Scorecard metric boxes ── */
    .score-box {
        border-radius: 10px;
        padding: 18px;
        text-align: center;
        font-size: 1.0rem;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }
    .score-green  { background-color: #27AE60; }
    .score-amber  { background-color: #F39C12; }
    .score-red    { background-color: #E74C3C; }
    .score-grey   { background-color: #95A5A6; }

    /* ── Page title ── */
    .page-title {
        color: #2E86C1;
        font-size: 1.9rem;
        font-weight: 800;
        margin-bottom: 2px;
    }
    .page-sub {
        color: #5D6D7E;
        font-size: 0.9rem;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# HELPERS
# ════════════════════════════════════════════════════════════════════════════

def fmt(val):
    if val is None: return "—"
    if val < 0:     return f"({abs(val):,.0f})"
    return f"{val:,.0f}"

def stat_row(label, val, style="normal"):
    lbl_map = {
        "normal":   ("row-label",       "row-label"),
        "bold":     ("row-label-bold",  "row-label-bold"),
        "subtotal": ("row-subtotal",    "row-subtotal"),
        "total":    ("row-total",       "row-total"),
    }
    lbl_cls, val_cls = lbl_map.get(style, lbl_map["normal"])
    if style == "total":
        val_html = f'<span class="num-total">{fmt(val)}</span>'
    elif val is not None and val < 0:
        val_html = f'<span class="num-negative">{fmt(val)}</span>'
    else:
        val_html = f'<span class="num-positive">{fmt(val)}</span>'
    c1, c2 = st.columns([3, 1])
    c1.markdown(f'<p class="{lbl_cls}">{label}</p>', unsafe_allow_html=True)
    c2.markdown(f'<p class="{val_cls}" style="text-align:right">{val_html}</p>', unsafe_allow_html=True)

def spacer(h=6):
    st.markdown(f"<div style='height:{h}px'></div>", unsafe_allow_html=True)

def safe_div(a, b):
    return a / b if b and b != 0 else None

# ════════════════════════════════════════════════════════════════════════════
# DEFAULT VALUES
# ════════════════════════════════════════════════════════════════════════════

D = {
    "revenue": 1_200_000, "cogs": 720_000, "operating_exp": 180_000,
    "depreciation": 40_000, "interest_exp": 25_000, "other_income": 10_000,
    "tax_rate": 25.0,
    "cash": 150_000, "accounts_rec": 200_000, "inventory": 180_000,
    "prepaid_exp": 20_000, "ppe_gross": 800_000, "accum_dep": 320_000,
    "intangibles": 100_000, "other_lt_assets": 50_000,
    "accounts_pay": 140_000, "short_term_debt": 80_000, "accrued_liab": 60_000,
    "long_term_debt": 300_000, "deferred_tax": 40_000,
    "common_stock": 200_000, "add_paid_cap": 150_000,
    "capex": 90_000, "proceeds_asset": 15_000,
    "debt_issued": 50_000, "debt_repaid": 80_000,
    "dividends_paid": 30_000, "shares_issued": 20_000,
    "re_beginning": 250_000,
}

# ════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("## ⚙️ Input Parameters")
    st.caption("Edit any value — all statements and ratios update instantly.")

    st.markdown("---")
    st.markdown("### 📋 Income Statement")
    revenue       = st.number_input("Revenue",                  value=D["revenue"],         step=1000)
    cogs          = st.number_input("Cost of Goods Sold",       value=D["cogs"],            step=1000)
    operating_exp = st.number_input("Operating Expenses",       value=D["operating_exp"],   step=1000)
    depreciation  = st.number_input("Depreciation & Amort.",    value=D["depreciation"],    step=1000)
    interest_exp  = st.number_input("Interest Expense",         value=D["interest_exp"],    step=1000)
    other_income  = st.number_input("Other Income",             value=D["other_income"],    step=1000)
    tax_rate      = st.number_input("Tax Rate (%)",             value=D["tax_rate"],        step=0.5, min_value=0.0, max_value=100.0)

    st.markdown("---")
    st.markdown("### 🏦 Balance Sheet — Assets")
    cash          = st.number_input("Cash & Equivalents",       value=D["cash"],            step=1000)
    accounts_rec  = st.number_input("Accounts Receivable",      value=D["accounts_rec"],    step=1000)
    inventory     = st.number_input("Inventory",                value=D["inventory"],       step=1000)
    prepaid_exp   = st.number_input("Prepaid Expenses",         value=D["prepaid_exp"],     step=1000)
    ppe_gross     = st.number_input("PP&E (Gross)",             value=D["ppe_gross"],       step=1000)
    accum_dep     = st.number_input("Accumulated Depreciation", value=D["accum_dep"],       step=1000)
    intangibles   = st.number_input("Intangible Assets",        value=D["intangibles"],     step=1000)
    other_lt      = st.number_input("Other LT Assets",          value=D["other_lt_assets"], step=1000)

    st.markdown("---")
    st.markdown("### 🏦 Balance Sheet — Liabilities & Equity")
    accounts_pay  = st.number_input("Accounts Payable",         value=D["accounts_pay"],    step=1000)
    short_debt    = st.number_input("Short-Term Debt",          value=D["short_term_debt"], step=1000)
    accrued_liab  = st.number_input("Accrued Liabilities",      value=D["accrued_liab"],    step=1000)
    long_debt     = st.number_input("Long-Term Debt",           value=D["long_term_debt"],  step=1000)
    deferred_tax  = st.number_input("Deferred Tax Liability",   value=D["deferred_tax"],    step=1000)
    common_stock  = st.number_input("Common Stock",             value=D["common_stock"],    step=1000)
    add_paid_cap  = st.number_input("Additional Paid-in Capital",value=D["add_paid_cap"],   step=1000)

    st.markdown("---")
    st.markdown("### 💰 Cash Flow Adjustments")
    capex          = st.number_input("Capital Expenditures",        value=D["capex"],          step=1000)
    proceeds_asset = st.number_input("Proceeds from Asset Sales",   value=D["proceeds_asset"], step=1000)
    debt_issued    = st.number_input("Debt Issued",                 value=D["debt_issued"],    step=1000)
    debt_repaid    = st.number_input("Debt Repaid",                 value=D["debt_repaid"],    step=1000)
    dividends_paid = st.number_input("Dividends Paid",              value=D["dividends_paid"], step=1000)
    shares_issued  = st.number_input("Proceeds — Share Issuance",   value=D["shares_issued"],  step=1000)

    st.markdown("---")
    st.markdown("### 📈 Retained Earnings")
    re_beginning  = st.number_input("Retained Earnings (Beginning)", value=D["re_beginning"], step=1000)

# ════════════════════════════════════════════════════════════════════════════
# COMPUTED VALUES
# ════════════════════════════════════════════════════════════════════════════

gross_profit   = revenue - cogs
ebitda         = gross_profit - operating_exp
ebit           = ebitda - depreciation
ebt            = ebit - interest_exp + other_income
tax_expense    = max(ebt * (tax_rate / 100), 0)
net_income     = ebt - tax_expense

ppe_net               = ppe_gross - accum_dep
total_current_assets  = cash + accounts_rec + inventory + prepaid_exp
total_lt_assets       = ppe_net + intangibles + other_lt
total_assets          = total_current_assets + total_lt_assets

total_current_liab    = accounts_pay + short_debt + accrued_liab
total_lt_liab         = long_debt + deferred_tax
total_liabilities     = total_current_liab + total_lt_liab
retained_earnings_bs  = total_assets - total_liabilities - common_stock - add_paid_cap
total_equity          = common_stock + add_paid_cap + retained_earnings_bs
total_liab_equity     = total_liabilities + total_equity

cfo             = net_income + depreciation - (accounts_rec - D["accounts_rec"]) \
                  - (inventory - D["inventory"]) + (accounts_pay - D["accounts_pay"])
cfi             = -capex + proceeds_asset
cff             = debt_issued - debt_repaid + shares_issued - dividends_paid
net_change_cash = cfo + cfi + cff

re_ending       = re_beginning + net_income - dividends_paid
total_debt      = short_debt + long_debt
shares_out      = 100_000

# ════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ════════════════════════════════════════════════════════════════════════════

st.markdown('<p class="page-title">💵 Financial Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="page-sub">Interactive Financial Statements & Ratio Analysis — edit any value in the sidebar</p>', unsafe_allow_html=True)
st.markdown("---")

# ════════════════════════════════════════════════════════════════════════════
# TABS
# ════════════════════════════════════════════════════════════════════════════

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Income Statement",
    "🏦 Balance Sheet",
    "💰 Cash Flow",
    "📈 Retained Earnings",
    "📐 Ratio Analysis",
])

# ── Tab 1 : Income Statement ─────────────────────────────────────────────────
with tab1:
    st.markdown('<div class="section-header">📋 Income Statement  (USD)</div>', unsafe_allow_html=True)
    stat_row("Revenue",                              revenue)
    stat_row("  Less: Cost of Goods Sold",           -cogs)
    stat_row("Gross Profit",                         gross_profit,   "subtotal")
    spacer()
    stat_row("  Less: Operating Expenses",           -operating_exp)
    stat_row("  Less: Depreciation & Amortisation",  -depreciation)
    stat_row("EBIT  (Operating Income)",             ebit,           "subtotal")
    spacer()
    stat_row("  Add: Other Income",                  other_income)
    stat_row("  Less: Interest Expense",             -interest_exp)
    stat_row("Earnings Before Tax  (EBT)",           ebt,            "subtotal")
    spacer()
    stat_row("  Less: Income Tax Expense",           -tax_expense)
    stat_row("Net Income",                           net_income,     "total")
    spacer(10)
    st.caption(f"EBITDA: {fmt(ebitda)}  |  Effective Tax Rate: {tax_rate:.1f}%  |  EPS (100k shares): {net_income/shares_out:,.2f}")

# ── Tab 2 : Balance Sheet ─────────────────────────────────────────────────────
with tab2:
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown('<div class="section-header">Assets</div>', unsafe_allow_html=True)
        st.markdown("**Current Assets**")
        stat_row("Cash & Cash Equivalents",   cash)
        stat_row("Accounts Receivable",       accounts_rec)
        stat_row("Inventory",                 inventory)
        stat_row("Prepaid Expenses",          prepaid_exp)
        stat_row("Total Current Assets",      total_current_assets, "subtotal")
        spacer()
        st.markdown("**Non-Current Assets**")
        stat_row("PP&E (Gross)",              ppe_gross)
        stat_row("  Less: Accum. Deprec.",    -accum_dep)
        stat_row("PP&E (Net)",                ppe_net)
        stat_row("Intangible Assets",         intangibles)
        stat_row("Other LT Assets",           other_lt)
        stat_row("Total Non-Current Assets",  total_lt_assets, "subtotal")
        spacer()
        stat_row("TOTAL ASSETS",              total_assets, "total")

    with col_b:
        st.markdown('<div class="section-header">Liabilities & Equity</div>', unsafe_allow_html=True)
        st.markdown("**Current Liabilities**")
        stat_row("Accounts Payable",          accounts_pay)
        stat_row("Short-Term Debt",           short_debt)
        stat_row("Accrued Liabilities",       accrued_liab)
        stat_row("Total Current Liabilities", total_current_liab, "subtotal")
        spacer()
        st.markdown("**Non-Current Liabilities**")
        stat_row("Long-Term Debt",            long_debt)
        stat_row("Deferred Tax Liability",    deferred_tax)
        stat_row("Total LT Liabilities",      total_lt_liab, "subtotal")
        stat_row("TOTAL LIABILITIES",         total_liabilities, "subtotal")
        spacer()
        st.markdown("**Shareholders' Equity**")
        stat_row("Common Stock",              common_stock)
        stat_row("Additional Paid-in Capital",add_paid_cap)
        stat_row("Retained Earnings",         retained_earnings_bs)
        stat_row("Total Equity",              total_equity, "subtotal")
        spacer()
        stat_row("TOTAL LIABILITIES & EQUITY",total_liab_equity, "total")
        spacer(6)
        if abs(total_assets - total_liab_equity) < 1:
            st.success("✅ Balance Sheet balances")
        else:
            st.warning(f"⚠️ Out of balance by: {fmt(total_assets - total_liab_equity)}")

# ── Tab 3 : Cash Flow ─────────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-header">💰 Cash Flow Statement  (USD)</div>', unsafe_allow_html=True)

    st.markdown("**Operating Activities**")
    stat_row("Net Income",                      net_income)
    stat_row("Add: Depreciation & Amort.",      depreciation)
    stat_row("Change in Accounts Receivable",   -(accounts_rec - D["accounts_rec"]))
    stat_row("Change in Inventory",             -(inventory    - D["inventory"]))
    stat_row("Change in Accounts Payable",       (accounts_pay - D["accounts_pay"]))
    stat_row("Net Cash from Operations (CFO)",  cfo, "subtotal")
    spacer()

    st.markdown("**Investing Activities**")
    stat_row("Capital Expenditures (CapEx)",    -capex)
    stat_row("Proceeds from Asset Sales",       proceeds_asset)
    stat_row("Net Cash from Investing (CFI)",   cfi, "subtotal")
    spacer()

    st.markdown("**Financing Activities**")
    stat_row("Debt Issued",                     debt_issued)
    stat_row("Debt Repaid",                     -debt_repaid)
    stat_row("Shares Issued",                   shares_issued)
    stat_row("Dividends Paid",                  -dividends_paid)
    stat_row("Net Cash from Financing (CFF)",   cff, "subtotal")
    spacer()

    stat_row("Net Change in Cash",              net_change_cash, "total")
    spacer(10)
    st.caption(f"Free Cash Flow (FCF) = CFO − CapEx = {fmt(cfo - capex)}")

# ── Tab 4 : Retained Earnings ─────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-header">📈 Statement of Retained Earnings  (USD)</div>', unsafe_allow_html=True)
    stat_row("Retained Earnings — Beginning of Period", re_beginning)
    stat_row("Add: Net Income for the Period",          net_income)
    stat_row("Less: Dividends Declared",                -dividends_paid)
    stat_row("Retained Earnings — End of Period",       re_ending, "total")
    spacer(10)
    st.caption("Note: Ending retained earnings feeds back into the Balance Sheet equity section.")

# ════════════════════════════════════════════════════════════════════════════
# TAB 5 — RATIO ANALYSIS
# ════════════════════════════════════════════════════════════════════════════

with tab5:
    st.markdown('<div class="section-header">📐 Financial Ratio Analysis</div>', unsafe_allow_html=True)

    # colour legend in Overview style
    c1, c2, c3 = st.columns(3)
    c1.markdown("""<div style="background:#27AE6022;border-left:5px solid #27AE60;
        border-radius:6px;padding:8px 14px;font-size:0.85rem;font-weight:700;color:#1E8449;">
        🟢 Good — meets standard benchmark</div>""", unsafe_allow_html=True)
    c2.markdown("""<div style="background:#F39C1222;border-left:5px solid #F39C12;
        border-radius:6px;padding:8px 14px;font-size:0.85rem;font-weight:700;color:#D68910;">
        🟡 Caution — approaching concern zone</div>""", unsafe_allow_html=True)
    c3.markdown("""<div style="background:#E74C3C22;border-left:5px solid #E74C3C;
        border-radius:6px;padding:8px 14px;font-size:0.85rem;font-weight:700;color:#C0392B;">
        🔴 Concern — below acceptable threshold</div>""", unsafe_allow_html=True)
    spacer(14)

    # ── Ratio definitions ────────────────────────────────────────────────────
    ratios = [
        {
            "category": "💧 Liquidity Ratios",
            "color": "#2E86C1",
            "items": [
                {"name": "Current Ratio",
                 "value": safe_div(total_current_assets, total_current_liab),
                 "formula": "Current Assets ÷ Current Liabilities",
                 "bench": "≥2.0 Good | 1.0–2.0 Caution | <1.0 Concern",
                 "green": lambda v: v >= 2.0, "amber": lambda v: 1.0 <= v < 2.0,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Quick Ratio (Acid-Test)",
                 "value": safe_div(cash + accounts_rec, total_current_liab),
                 "formula": "(Cash + Receivables) ÷ Current Liabilities",
                 "bench": "≥1.0 Good | 0.5–1.0 Caution | <0.5 Concern",
                 "green": lambda v: v >= 1.0, "amber": lambda v: 0.5 <= v < 1.0,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Cash Ratio",
                 "value": safe_div(cash, total_current_liab),
                 "formula": "Cash ÷ Current Liabilities",
                 "bench": "≥0.5 Good | 0.2–0.5 Caution | <0.2 Concern",
                 "green": lambda v: v >= 0.5, "amber": lambda v: 0.2 <= v < 0.5,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Operating CF Ratio",
                 "value": safe_div(cfo, total_current_liab),
                 "formula": "CFO ÷ Current Liabilities",
                 "bench": "≥1.0 Good | 0.4–1.0 Caution | <0.4 Concern",
                 "green": lambda v: v >= 1.0, "amber": lambda v: 0.4 <= v < 1.0,
                 "fmt": ".2f", "suffix": "x"},
            ]
        },
        {
            "category": "📈 Profitability Ratios",
            "color": "#27AE60",
            "items": [
                {"name": "Gross Profit Margin",
                 "value": safe_div(gross_profit, revenue) * 100 if revenue else None,
                 "formula": "Gross Profit ÷ Revenue × 100",
                 "bench": "≥40% Good | 20–40% Caution | <20% Concern",
                 "green": lambda v: v >= 40, "amber": lambda v: 20 <= v < 40,
                 "fmt": ".1f", "suffix": "%"},
                {"name": "EBITDA Margin",
                 "value": safe_div(ebitda, revenue) * 100 if revenue else None,
                 "formula": "EBITDA ÷ Revenue × 100",
                 "bench": "≥25% Good | 10–25% Caution | <10% Concern",
                 "green": lambda v: v >= 25, "amber": lambda v: 10 <= v < 25,
                 "fmt": ".1f", "suffix": "%"},
                {"name": "Operating Profit Margin",
                 "value": safe_div(ebit, revenue) * 100 if revenue else None,
                 "formula": "EBIT ÷ Revenue × 100",
                 "bench": "≥20% Good | 8–20% Caution | <8% Concern",
                 "green": lambda v: v >= 20, "amber": lambda v: 8 <= v < 20,
                 "fmt": ".1f", "suffix": "%"},
                {"name": "Net Profit Margin",
                 "value": safe_div(net_income, revenue) * 100 if revenue else None,
                 "formula": "Net Income ÷ Revenue × 100",
                 "bench": "≥15% Good | 5–15% Caution | <5% Concern",
                 "green": lambda v: v >= 15, "amber": lambda v: 5 <= v < 15,
                 "fmt": ".1f", "suffix": "%"},
                {"name": "Return on Assets (ROA)",
                 "value": safe_div(net_income, total_assets) * 100 if total_assets else None,
                 "formula": "Net Income ÷ Total Assets × 100",
                 "bench": "≥10% Good | 5–10% Caution | <5% Concern",
                 "green": lambda v: v >= 10, "amber": lambda v: 5 <= v < 10,
                 "fmt": ".1f", "suffix": "%"},
                {"name": "Return on Equity (ROE)",
                 "value": safe_div(net_income, total_equity) * 100 if total_equity else None,
                 "formula": "Net Income ÷ Shareholders' Equity × 100",
                 "bench": "≥15% Good | 8–15% Caution | <8% Concern",
                 "green": lambda v: v >= 15, "amber": lambda v: 8 <= v < 15,
                 "fmt": ".1f", "suffix": "%"},
                {"name": "ROCE",
                 "value": safe_div(ebit, total_assets - total_current_liab) * 100,
                 "formula": "EBIT ÷ Capital Employed × 100",
                 "bench": "≥15% Good | 8–15% Caution | <8% Concern",
                 "green": lambda v: v >= 15, "amber": lambda v: 8 <= v < 15,
                 "fmt": ".1f", "suffix": "%"},
            ]
        },
        {
            "category": "🏗️ Leverage / Solvency Ratios",
            "color": "#8E44AD",
            "items": [
                {"name": "Debt-to-Equity Ratio",
                 "value": safe_div(total_debt, total_equity),
                 "formula": "Total Debt ÷ Shareholders' Equity",
                 "bench": "≤0.5 Good | 0.5–1.5 Caution | >1.5 Concern",
                 "green": lambda v: v <= 0.5, "amber": lambda v: 0.5 < v <= 1.5,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Debt-to-Assets Ratio",
                 "value": safe_div(total_liabilities, total_assets),
                 "formula": "Total Liabilities ÷ Total Assets",
                 "bench": "≤0.4 Good | 0.4–0.6 Caution | >0.6 Concern",
                 "green": lambda v: v <= 0.4, "amber": lambda v: 0.4 < v <= 0.6,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Interest Coverage (TIE)",
                 "value": safe_div(ebit, interest_exp),
                 "formula": "EBIT ÷ Interest Expense",
                 "bench": "≥3.0 Good | 1.5–3.0 Caution | <1.5 Concern",
                 "green": lambda v: v >= 3.0, "amber": lambda v: 1.5 <= v < 3.0,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Debt Service Coverage (DSCR)",
                 "value": safe_div(ebitda, interest_exp + debt_repaid),
                 "formula": "EBITDA ÷ (Interest + Debt Repayment)",
                 "bench": "≥1.5 Good | 1.0–1.5 Caution | <1.0 Concern",
                 "green": lambda v: v >= 1.5, "amber": lambda v: 1.0 <= v < 1.5,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Equity Multiplier",
                 "value": safe_div(total_assets, total_equity),
                 "formula": "Total Assets ÷ Shareholders' Equity",
                 "bench": "≤2.0 Good | 2.0–4.0 Caution | >4.0 Concern",
                 "green": lambda v: v <= 2.0, "amber": lambda v: 2.0 < v <= 4.0,
                 "fmt": ".2f", "suffix": "x"},
            ]
        },
        {
            "category": "⚙️ Efficiency / Activity Ratios",
            "color": "#E67E22",
            "items": [
                {"name": "Asset Turnover",
                 "value": safe_div(revenue, total_assets),
                 "formula": "Revenue ÷ Total Assets",
                 "bench": "≥1.0 Good | 0.5–1.0 Caution | <0.5 Concern",
                 "green": lambda v: v >= 1.0, "amber": lambda v: 0.5 <= v < 1.0,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Inventory Turnover",
                 "value": safe_div(cogs, inventory),
                 "formula": "COGS ÷ Inventory",
                 "bench": "≥6x Good | 3–6x Caution | <3x Concern",
                 "green": lambda v: v >= 6, "amber": lambda v: 3 <= v < 6,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Days Inventory Outstanding",
                 "value": safe_div(inventory, cogs) * 365 if cogs else None,
                 "formula": "(Inventory ÷ COGS) × 365",
                 "bench": "≤45 days Good | 45–90 Caution | >90 Concern",
                 "green": lambda v: v <= 45, "amber": lambda v: 45 < v <= 90,
                 "fmt": ".1f", "suffix": " days"},
                {"name": "Receivables Turnover",
                 "value": safe_div(revenue, accounts_rec),
                 "formula": "Revenue ÷ Accounts Receivable",
                 "bench": "≥8x Good | 4–8x Caution | <4x Concern",
                 "green": lambda v: v >= 8, "amber": lambda v: 4 <= v < 8,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Days Sales Outstanding (DSO)",
                 "value": safe_div(accounts_rec, revenue) * 365 if revenue else None,
                 "formula": "(Accounts Receivable ÷ Revenue) × 365",
                 "bench": "≤30 days Good | 30–60 Caution | >60 Concern",
                 "green": lambda v: v <= 30, "amber": lambda v: 30 < v <= 60,
                 "fmt": ".1f", "suffix": " days"},
                {"name": "Payables Turnover",
                 "value": safe_div(cogs, accounts_pay),
                 "formula": "COGS ÷ Accounts Payable",
                 "bench": "≥8x Good | 4–8x Caution | <4x Concern",
                 "green": lambda v: v >= 8, "amber": lambda v: 4 <= v < 8,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Days Payable Outstanding (DPO)",
                 "value": safe_div(accounts_pay, cogs) * 365 if cogs else None,
                 "formula": "(Accounts Payable ÷ COGS) × 365",
                 "bench": "30–60 days Good | 60–90 Caution | >90 Concern",
                 "green": lambda v: 30 <= v <= 60, "amber": lambda v: (20 <= v < 30) or (60 < v <= 90),
                 "fmt": ".1f", "suffix": " days"},
                {"name": "Cash Conversion Cycle",
                 "value": (
                     (safe_div(inventory, cogs) * 365 if cogs else 0) +
                     (safe_div(accounts_rec, revenue) * 365 if revenue else 0) -
                     (safe_div(accounts_pay, cogs) * 365 if cogs else 0)
                 ),
                 "formula": "DIO + DSO − DPO",
                 "bench": "≤30 days Good | 30–60 Caution | >60 Concern",
                 "green": lambda v: v <= 30, "amber": lambda v: 30 < v <= 60,
                 "fmt": ".1f", "suffix": " days"},
            ]
        },
        {
            "category": "💵 Cash Flow Ratios",
            "color": "#1ABC9C",
            "items": [
                {"name": "CFO to Net Income",
                 "value": safe_div(cfo, net_income) if net_income else None,
                 "formula": "Operating Cash Flow ÷ Net Income",
                 "bench": "≥1.1 Good | 0.8–1.1 Caution | <0.8 Concern",
                 "green": lambda v: v >= 1.1, "amber": lambda v: 0.8 <= v < 1.1,
                 "fmt": ".2f", "suffix": "x"},
                {"name": "Free Cash Flow Margin",
                 "value": safe_div(cfo - capex, revenue) * 100 if revenue else None,
                 "formula": "(CFO − CapEx) ÷ Revenue × 100",
                 "bench": "≥10% Good | 3–10% Caution | <3% Concern",
                 "green": lambda v: v >= 10, "amber": lambda v: 3 <= v < 10,
                 "fmt": ".1f", "suffix": "%"},
                {"name": "CapEx to CFO",
                 "value": safe_div(capex, cfo) * 100 if cfo else None,
                 "formula": "CapEx ÷ CFO × 100",
                 "bench": "≤30% Good | 30–60% Caution | >60% Concern",
                 "green": lambda v: v <= 30, "amber": lambda v: 30 < v <= 60,
                 "fmt": ".1f", "suffix": "%"},
            ]
        },
        {
            "category": "📦 Per-Share & Payout Ratios",
            "color": "#3498DB",
            "items": [
                {"name": "Earnings Per Share (EPS)",
                 "value": safe_div(net_income, shares_out),
                 "formula": "Net Income ÷ Shares Outstanding (100,000)",
                 "bench": ">0 Good | =0 Caution | <0 Concern",
                 "green": lambda v: v > 0, "amber": lambda v: v == 0,
                 "fmt": ".2f", "suffix": " USD"},
                {"name": "Dividend Payout Ratio",
                 "value": safe_div(dividends_paid, net_income) * 100 if net_income > 0 else None,
                 "formula": "Dividends Paid ÷ Net Income × 100",
                 "bench": "25–50% Good | 50–75% Caution | >75% Concern",
                 "green": lambda v: 25 <= v <= 50,
                 "amber": lambda v: (10 <= v < 25) or (50 < v <= 75),
                 "fmt": ".1f", "suffix": "%"},
                {"name": "Book Value Per Share",
                 "value": safe_div(total_equity, shares_out),
                 "formula": "Total Equity ÷ Shares Outstanding",
                 "bench": ">0 Good | reflects net assets per share",
                 "green": lambda v: v > 0, "amber": lambda v: v == 0,
                 "fmt": ".2f", "suffix": " USD"},
            ]
        },
    ]

    # ── Render ratio cards ────────────────────────────────────────────────────
    green_c = amber_c = red_c = na_c = 0

    for section in ratios:
        # Section header — uses the section's own accent color like Overview module cards
        st.markdown(
            f'<div style="background-color:{section["color"]}22; border-left:5px solid {section["color"]}; '
            f'padding:9px 16px; border-radius:8px; margin:18px 0 10px 0; '
            f'font-size:1.05rem; font-weight:700; color:{section["color"]};">'
            f'{section["category"]}</div>',
            unsafe_allow_html=True
        )
        cols = st.columns(4)
        for i, r in enumerate(section["items"]):
            val = r["value"]
            with cols[i % 4]:
                if val is None:
                    card_cls, val_cls, status, stat_cls = "ratio-card-neutral", "ratio-val-neutral", "⚪ N/A", ""
                    na_c += 1
                elif r["green"](val):
                    card_cls, val_cls, status, stat_cls = "ratio-card-green", "ratio-val-green", "🟢 Good", "status-green"
                    green_c += 1
                elif r["amber"](val):
                    card_cls, val_cls, status, stat_cls = "ratio-card-amber", "ratio-val-amber", "🟡 Caution", "status-amber"
                    amber_c += 1
                else:
                    card_cls, val_cls, status, stat_cls = "ratio-card-red", "ratio-val-red", "🔴 Concern", "status-red"
                    red_c += 1

                val_str = f"{val:{r['fmt']}}{r['suffix']}" if val is not None else "—"
                st.markdown(f"""
                <div class="ratio-card {card_cls}">
                    <div class="ratio-name">{r['name']}</div>
                    <div class="ratio-value {val_cls}">{val_str}</div>
                    <div class="ratio-formula">Formula: {r['formula']}</div>
                    <div class="ratio-bench">{r['bench']}</div>
                    <div class="ratio-status {stat_cls}">{status}</div>
                </div>""", unsafe_allow_html=True)
        spacer(6)

    # ── Scorecard summary ─────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown(
        f'<div style="background-color:#2E86C122; border-left:5px solid #2E86C1; '
        f'padding:9px 16px; border-radius:8px; margin:10px 0; '
        f'font-size:1.05rem; font-weight:700; color:#2E86C1;">🏆 Ratio Scorecard Summary</div>',
        unsafe_allow_html=True
    )
    total_r = green_c + amber_c + red_c
    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        pct = f"{green_c/total_r*100:.0f}%" if total_r else "—"
        st.markdown(f'<div class="score-box score-green">🟢 Good<br><span style="font-size:2rem">{green_c}</span><br><small>{pct}</small></div>', unsafe_allow_html=True)
    with sc2:
        pct = f"{amber_c/total_r*100:.0f}%" if total_r else "—"
        st.markdown(f'<div class="score-box score-amber">🟡 Caution<br><span style="font-size:2rem">{amber_c}</span><br><small>{pct}</small></div>', unsafe_allow_html=True)
    with sc3:
        pct = f"{red_c/total_r*100:.0f}%" if total_r else "—"
        st.markdown(f'<div class="score-box score-red">🔴 Concern<br><span style="font-size:2rem">{red_c}</span><br><small>{pct}</small></div>', unsafe_allow_html=True)
    with sc4:
        st.markdown(f'<div class="score-box score-grey">⚪ N/A<br><span style="font-size:2rem">{na_c}</span><br><small>&nbsp;</small></div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("💵 Financial Dashboard · Python Streamlit · All figures in USD · For illustrative purposes only.")