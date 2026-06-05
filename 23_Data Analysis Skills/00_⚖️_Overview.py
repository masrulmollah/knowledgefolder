import os
import importlib.util
import streamlit as st

# ── Import modules ─────────────────────────────────────────────────────────────
# Each module file defines ONE function: show()
# Nothing else executes when these files are imported or exec'd.
# The homepage app already calls st.set_page_config(), so imported modules
# must not call it again.

BASE_DIR = os.path.dirname(__file__)

def _load_module(filename, alias):
    path = os.path.join(BASE_DIR, filename)
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

m01 = _load_module("01_⚖️_Module 1 Foundations of Financial Data.py", "m01")
m02 = _load_module("02_⚖️_Module 2 Descriptive Analytics.py", "m02")
m03 = _load_module("03_⚖️_Module 3 Diagnostic Analytics.py", "m03")
m04 = _load_module("04_⚖️_Module 4 Predictive Analytics & Forecasting.py", "m04")
m05 = _load_module("05_⚖️_Module 5 Prescriptive Analytics & Decision Modelling.py", "m05")
m06 = _load_module("06_⚖️_Module 6 Valuation & Investment Analytics.py", "m06")
m07 = _load_module("07_⚖️_Module 7 Risk & Treasury Analytics.py", "m07")
m08 = _load_module("08_⚖️_Module 8 Tools, Tech & Automation.py", "m08")
m09 = _load_module("09_⚖️_Module 9 Insight Communication & Storytelling.py", "m09")
m10 = _load_module("10_⚖️_Module 10 Real-World Case Studies.py", "m10")

# ── Navigation ─────────────────────────────────────────────────────────────────
PAGES = {
    "🏠  Home":                                  None,
    "📁  M1 — Foundations of Financial Data":    m01,
    "📊  M2 — Descriptive Analytics":           m02,
    "🔍  M3 — Diagnostic Analytics":            m03,
    "📈  M4 — Predictive Analytics":             m04,
    "⚖️  M5 — Prescriptive Analytics":           m05,
    "💰  M6 — Valuation Analytics":              m06,
    "🏦  M7 — Risk & Treasury Analytics":        m07,
    "🛠️  M8 — Tools, Tech & Automation":         m08,
    "📣  M9 — Communication & Storytelling":     m09,
    "🎯  M10 — Capstone Case Studies":           m10,
}

with st.sidebar:
    st.markdown("## 📚 Knowledge Folder")
    st.markdown("**Financial Data Analytics**")
    st.markdown("---")
    selection = st.radio(
        "Navigate to:",
        list(PAGES.keys()),
        label_visibility="collapsed",
    )

module = PAGES[selection]

# ── Home page ──────────────────────────────────────────────────────────────────
if module is None:
    st.title("📊 Financial Data Analytics — Knowledge Folder")
    st.markdown("---")
    st.markdown(
        "A complete skill-development resource for finance professionals. "
        "Select any module from the sidebar to begin."
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Modules",      "10")
    c2.metric("Topics",       "58+")
    c3.metric("Calculators",  "20+")
    c4.metric("Quiz Questions","50+")
    st.markdown("---")

    cards = [
        ("�","M1","Foundations of Financial Data", "Data types, quality dimensions, structured vs unstructured finance data"),
        ("📊","M2","Descriptive Analytics",        "Summary stats, dashboards, variance analysis, KPI tracking"),
        ("🔍","M3","Diagnostic Analytics",         "Root cause analysis, correlation, variance bridge, ratio modelling"),
        ("📈","M4","Predictive Analytics",         "ARIMA, regression, Monte Carlo, driver-based forecasting"),
        ("⚖️","M5","Prescriptive Analytics",       "Decision trees, capital allocation, portfolio optimisation"),
        ("💰","M6","Valuation Analytics",          "DCF, comps, factor analytics, earnings quality"),
        ("🏦","M7","Risk & Treasury",              "VaR, IFRS 9 ECL, liquidity risk, FX analytics"),
        ("🛠️","M8","Tools & Automation",           "Python, SQL window functions, Power BI, pipelines"),
        ("📣","M9","Communication",                 "Pyramid principle, chart design, SCR storytelling"),
        ("🎯","M10","Capstone",                    "End-to-end case studies: P&L, working capital, M&A"),
    ]
    for i in range(0, len(cards), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(cards):
                icon, num, name, desc = cards[i + j]
                with col:
                    st.markdown(
                        f"<div style='border:1px solid #ddd;border-radius:8px;"
                        f"padding:14px;margin-bottom:10px;background:#fafafa;'>"
                        f"<b>{icon} {num} — {name}</b><br>"
                        f"<span style='font-size:13px;color:#555;'>{desc}</span></div>",
                        unsafe_allow_html=True,
                    )
    st.markdown("---")
    st.info(
        "**How to run:** Place all .py files in the same folder. "
        "Run:  `streamlit run Homepage.py`"
    )

# ── Load selected module ────────────────────────────────────────────────────────
else:
    # Calls show() — the only function in each module file.
    # No Streamlit commands run at module level, so set_page_config() is never
    # triggered twice regardless of how the file was loaded.
    module.show()