import os
import importlib.util
import streamlit as st

# ── Lazy module loader — only loads when user selects that page ────────────────
BASE_DIR = os.path.dirname(__file__)

def _load(filename, alias):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location(alias, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# ── File map: sidebar label → (filename, alias) ───────────────────────────────
FILE_MAP = {
    "🏠  Home — Complete Financial Analytics":           None,
    "📊  M1 — Descriptive & Historical Analytics":       ("FA_M1_Descriptive_Historical.py",    "fa_m1"),
    "🏆  M2 — Comparative & Benchmarking Analytics":     ("FA_M2_Comparative_Benchmarking.py",  "fa_m2"),
    "🔍  M3 — Diagnostic & Variance Analytics":          ("FA_M3_Diagnostic_Variance.py",       "fa_m3"),
    "🔬  M4 — Exploratory & Statistical Analytics":      ("FA_M4_Exploratory_Statistical.py",   "fa_m4"),
    "📈  M5 — Predictive & Forecasting Analytics":       ("FA_M5_Predictive_Forecasting.py",    "fa_m5"),
    "💰  M6 — Commercial, Customer & Value Analytics":   ("FA_M6_Commercial_Customer_Value.py", "fa_m6"),
    "🏦  M7 — Cash Flow & Working Capital Analytics":    ("FA_M7_CashFlow_WorkingCapital.py",   "fa_m7"),
    "🤖  M8 — Advanced & AI-Powered Analytics":          ("FA_M8_Advanced_AI_Analytics.py",     "fa_m8"),
    "📣  M9 — Insight Communication & Storytelling":     ("FA_M9_Insight_Communication.py",     "fa_m9"),
    "🎯  M10 — Capstone Real-World Case Studies":        ("FA_M10_Capstone_Case_Studies.py",    "fa_m10"),
}

MODULE_META = [
    ("📊", "M1",  "Descriptive & Historical Analytics",
     "What happened?",
     "YoY / CAGR / trend analysis, common-size statements, ratio analysis, DuPont, CCC",
     ["YoY & CAGR", "Trend Indexation", "Ratio Dashboard", "DuPont ROE", "Common-Size P&L"],
     "#E6F1FB", "#0C447C"),

    ("🏆", "M2",  "Comparative & Benchmarking Analytics",
     "How did we compare?",
     "Peer benchmarking, BCG matrix, internal cross-unit comparison, macro correlation",
     ["Peer Benchmarker", "BCG Matrix", "Factory Comparison", "Heatmap Ranking", "Market Correlation"],
     "#E1F5EE", "#085041"),

    ("🔍", "M3",  "Diagnostic & Variance Analytics",
     "Why did it happen?",
     "PVM bridge, standard cost variances, activity-based costing, CVP, break-even",
     ["PVM Revenue Bridge", "EBITDA Waterfall", "Break-Even CVP", "5-Why Analysis", "Anomaly Z-Score"],
     "#FAEEDA", "#633806"),

    ("🔬", "M4",  "Exploratory & Statistical Analytics",
     "What patterns are hidden?",
     "Distribution analysis, Pareto 80/20, RFM segmentation, Benford's Law, outlier detection",
     ["Pareto 80/20", "ABC Classification", "RFM Segmentation", "Benford's Law", "IQR Outliers"],
     "#EEEDFE", "#3C3489"),

    ("📈", "M5",  "Predictive & Forecasting Analytics",
     "What is likely to happen?",
     "Moving averages, exponential smoothing, regression, scenario planning, Monte Carlo",
     ["Time-Series Forecast", "Regression Model", "Scenario Planning", "Sensitivity Analysis", "MAPE Tracking"],
     "#FAECE7", "#712B13"),

    ("💰", "M6",  "Commercial, Customer & Value Analytics",
     "Where is value created and lost?",
     "CLV, CAC, cost-to-serve, discount waterfall, DCF, NPV, IRR, EVA",
     ["CLV & CAC", "Cost-to-Serve", "DCF / NPV / IRR", "Discount Waterfall", "EVA"],
     "#FBEAF0", "#72243E"),

    ("🏦", "M7",  "Cash Flow & Working Capital Analytics",
     "Where is cash trapped or freed?",
     "FCF analysis, CCC, DSO/DIO/DPO, AR aging, 13-week cash forecast, WC optimisation",
     ["Cash Flow Builder", "WC Simulator", "AR Aging", "13-Week Forecast", "Cash Burn & Runway"],
     "#EAF3DE", "#27500A"),

    ("🤖", "M8",  "Advanced & AI-Powered Analytics",
     "What can advanced analytics and AI reveal?",
     "Monte Carlo, tornado charts, ML driver importance, EVA storytelling, SCR framework",
     ["Monte Carlo", "Tornado Chart", "ML Driver Importance", "EVA Value Map", "SCR Narrative"],
     "#FCEBEB", "#791F1F"),

    ("📣", "M9",  "Insight Communication & Storytelling",
     "How do we turn numbers into decisions?",
     "SCR framework, Pyramid Principle, chart design, board narratives, So-What test",
     ["SCR Builder", "Chart Design Lab", "Pyramid Principle", "Insight Framework", "Board Narrative"],
     "#FEF3E2", "#7A4200"),

    ("🎯", "M10", "Capstone Real-World Case Studies",
     "Can I apply everything end-to-end?",
     "4 full cases: Manufacturing review, FMCG rationalisation, Pharma M&A, Financial distress",
     ["Manufacturing FPA", "FMCG SKU Audit", "M&A Valuation", "Distress Turnaround", "Capstone Quiz"],
     "#F0EEF8", "#3C2070"),
]

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📚 Complete Financial Analytics")
    st.markdown("*A practitioner's guide for finance professionals*")
    st.markdown("---")
    selection = st.radio(
        "Navigate to module:",
        list(FILE_MAP.keys()),
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(
        "<div style='font-size:12px;color:#888;'>"
        "10 Modules · 60+ Techniques<br>"
        "25+ Interactive Tools · 70+ Quiz Questions<br><br>"
        "Each module covers:<br>"
        "📖 Concepts &amp; Theory<br>"
        "🧮 Interactive Calculators<br>"
        "📊 Live Visualisations<br>"
        "🧪 Worked Business Examples<br>"
        "❓ Quiz &amp; Self-Assessment"
        "</div>",
        unsafe_allow_html=True,
    )

# ── Route to module or home ────────────────────────────────────────────────────
file_info = FILE_MAP[selection]

if file_info is None:
    # ── HOME PAGE ──────────────────────────────────────────────────────────────

    # Hero banner
    st.markdown("""
<div style="background: linear-gradient(135deg, #0C447C 0%, #185FA5 60%, #1D9E75 100%);
            border-radius: 16px; padding: 36px 32px; margin-bottom: 28px;">
    <h1 style="color:white; margin:0; font-size:28px; font-weight:600;">
        Complete Financial Analytics
    </h1>
    <p style="color:rgba(255,255,255,0.85); margin: 10px 0 0 0; font-size:15px; max-width:700px;">
        A structured, practitioner-grade learning resource covering every analytics technique
        used by finance professionals — from descriptive fundamentals to AI-powered forecasting
        and real-world capstone case studies. Built for FP&amp;A analysts, finance managers,
        CFOs, and anyone who turns data into decisions.
    </p>
</div>
""", unsafe_allow_html=True)

    # Stats bar
    c1, c2, c3, c4, c5 = st.columns(5)
    for col, val, lbl in zip(
        [c1, c2, c3, c4, c5],
        ["10", "60+", "25+", "70+", "10"],
        ["Modules", "Analytics Techniques", "Interactive Tools", "Quiz Questions", "Worked Case Studies"],
    ):
        with col:
            st.markdown(
                f"<div style='text-align:center; padding:14px 8px; background:#F0F4F8; "
                f"border-radius:10px; margin-bottom:4px;'>"
                f"<div style='font-size:26px; font-weight:700; color:#185FA5;'>{val}</div>"
                f"<div style='font-size:11px; color:#666; margin-top:2px;'>{lbl}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # Analytics progression
    st.markdown("#### The Analytics Progression — From Data to Decision")
    progression = [
        ("📊", "Describe",  "What happened?",          "#E6F1FB", "#0C447C"),
        ("🏆", "Compare",   "How did we rank?",         "#E1F5EE", "#085041"),
        ("🔍", "Diagnose",  "Why did it happen?",       "#FAEEDA", "#633806"),
        ("🔬", "Explore",   "What's hidden?",           "#EEEDFE", "#3C3489"),
        ("📈", "Predict",   "What comes next?",         "#FAECE7", "#712B13"),
        ("💰", "Value",     "Where is value?",          "#FBEAF0", "#72243E"),
        ("🏦", "Cash",      "Where is cash?",           "#EAF3DE", "#27500A"),
        ("🤖", "AI",        "What can AI reveal?",      "#FCEBEB", "#791F1F"),
        ("📣", "Narrate",   "How do we communicate?",   "#FEF3E2", "#7A4200"),
        ("🎯", "Apply",     "Can I do it end-to-end?",  "#F0EEF8", "#3C2070"),
    ]
    prog_cols = st.columns(10)
    for col, (icon, label, q, bg, fg) in zip(prog_cols, progression):
        with col:
            st.markdown(
                f"<div style='background:{bg}; border-radius:10px; padding:8px 4px; "
                f"text-align:center; height:92px; display:flex; flex-direction:column; "
                f"justify-content:center;'>"
                f"<div style='font-size:16px;'>{icon}</div>"
                f"<div style='font-size:10px; font-weight:600; color:{fg}; margin-top:3px;"
                f"line-height:1.3;'>{label}</div>"
                f"<div style='font-size:9px; color:{fg}; opacity:0.7; margin-top:2px;"
                f"line-height:1.3;'>{q}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # Module cards
    st.markdown("#### Explore All 10 Modules")
    for i in range(0, len(MODULE_META), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j >= len(MODULE_META):
                break
            icon, num, name, question, desc, tools, bg, fg = MODULE_META[i + j]
            tools_html = "".join(
                f"<span style='background:white; border:1px solid {fg}30; color:{fg}; "
                f"font-size:10px; padding:2px 7px; border-radius:12px; margin:2px 2px 2px 0; "
                f"display:inline-block;'>{t}</span>"
                for t in tools
            )
            with col:
                st.markdown(
                    f"<div style='background:{bg}; border:1px solid {fg}25; border-radius:14px; "
                    f"padding:18px 18px 14px; margin-bottom:12px; min-height:170px;'>"
                    f"<div style='display:flex; align-items:flex-start; gap:10px; margin-bottom:8px;'>"
                    f"  <span style='font-size:22px;'>{icon}</span>"
                    f"  <div>"
                    f"    <div style='font-size:11px; font-weight:500; color:{fg}; opacity:0.7; "
                    f"         text-transform:uppercase; letter-spacing:.06em;'>{num}</div>"
                    f"    <div style='font-size:15px; font-weight:600; color:{fg}; "
                    f"         line-height:1.3;'>{name}</div>"
                    f"    <div style='font-size:12px; color:{fg}; opacity:0.75; "
                    f"         font-style:italic; margin-top:1px;'>{question}</div>"
                    f"  </div>"
                    f"</div>"
                    f"<div style='font-size:12px; color:#444; margin-bottom:10px; "
                    f"     line-height:1.5;'>{desc}</div>"
                    f"<div>{tools_html}</div>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("<br>", unsafe_allow_html=True)

    # How each module is structured
    st.markdown("#### How Each Module Is Structured")
    c1, c2, c3, c4, c5 = st.columns(5)
    for col, icon, title, desc in zip(
        [c1, c2, c3, c4, c5],
        ["📖", "🧮", "📊", "🧪", "❓"],
        ["Concepts", "Calculators", "Visualisations", "Worked Examples", "Quiz"],
        ["Theory, formulas, frameworks, and when to apply each technique",
         "Interactive tools — change inputs and see outputs update in real time",
         "Live charts: waterfall, bridge, heatmap, scatter, histogram and more",
         "Real business scenarios with complete step-by-step analytics narratives",
         "5–10 multiple-choice questions with instant feedback to test understanding"],
    ):
        with col:
            st.markdown(
                f"<div style='background:#F8F9FA; border-radius:10px; padding:14px; "
                f"text-align:center; height:155px;'>"
                f"<div style='font-size:24px; margin-bottom:6px;'>{icon}</div>"
                f"<div style='font-weight:600; font-size:13px; margin-bottom:6px; color:#185FA5;'>{title}</div>"
                f"<div style='font-size:11px; color:#666; line-height:1.5;'>{desc}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick reference expander
    with st.expander("📋 Quick Reference — All Analytics Techniques Covered"):
        techniques = {
            "📊 M1 — Descriptive & Historical": [
                "Year-on-Year (YoY), MoM, QoQ growth analysis",
                "Base-year indexation (growth index)",
                "CAGR (Compound Annual Growth Rate) modelling",
                "Common-size income statement & balance sheet",
                "Per-unit & operational volume metrics",
                "Liquidity ratios: Current ratio, Quick ratio",
                "Solvency ratios: Debt/Equity, Interest Coverage",
                "Efficiency ratios: DIO, DSO, DPO, CCC",
                "Profitability: Gross Margin, EBITDA Margin, ROE, ROCE",
                "DuPont ROE decomposition",
                "Altman Z-Score (financial distress prediction)",
            ],
            "🏆 M2 — Comparative & Benchmarking": [
                "Same-block cohort comparison (factory, region, channel)",
                "Cross-block performance benchmarking",
                "Peer group financial ratio benchmarking",
                "Best-in-class operational benchmarking",
                "Macro-market correlation analysis",
                "BCG matrix (growth vs. relative market share)",
                "Contribution margin ranking & SKU rationalisation",
                "Benchmarking heatmaps & ranking tables",
                "Share of wallet analysis",
            ],
            "🔍 M3 — Diagnostic & Variance": [
                "Budget vs. actual variance analysis",
                "Price-Volume-Mix (PVM) revenue bridge",
                "EBITDA waterfall bridge chart",
                "Standard costing: material price / usage variance",
                "Standard costing: labour rate / efficiency variance",
                "Overhead spending and volume variance",
                "Activity-Based Costing (ABC)",
                "Cost behaviour: fixed, variable, semi-variable, step",
                "High-low method for cost separation",
                "CVP analysis and break-even modelling",
                "Margin of safety calculation",
                "Operating leverage analysis",
                "5-Why root cause framework",
            ],
            "🔬 M4 — Exploratory & Statistical": [
                "Distribution analysis: mean, median, std dev, skewness, kurtosis",
                "Coefficient of variation",
                "Pareto 80/20 analysis",
                "ABC inventory / customer / SKU classification",
                "RFM segmentation (Recency, Frequency, Monetary)",
                "Z-score outlier detection",
                "IQR-based anomaly flagging",
                "Benford's Law fraud detection",
                "Duplicate invoice detection",
                "Round-number concentration testing",
                "Control charts for process monitoring",
            ],
            "📈 M5 — Predictive & Forecasting": [
                "Simple and weighted moving averages",
                "Exponential smoothing (SES, Holt, Holt-Winters)",
                "Seasonal index calculation and adjustment",
                "Time-series decomposition (Trend + Seasonality + Cycle + Noise)",
                "CAGR-based long-range forecasting",
                "Linear regression forecasting",
                "Multiple regression with leading indicators",
                "Forecast accuracy: MAPE, MAE, RMSE",
                "Sensitivity analysis (one-variable what-if)",
                "Scenario planning (Best / Base / Worst case)",
                "Tornado chart",
                "Monte Carlo simulation",
            ],
            "💰 M6 — Commercial, Customer & Value": [
                "Customer Lifetime Value (CLV)",
                "Customer Acquisition Cost (CAC) & CAC payback",
                "LTV:CAC ratio",
                "Cost-to-serve analysis (hidden loss-makers)",
                "Price realization analysis",
                "Pocket margin analysis",
                "Discount waterfall",
                "Price elasticity modelling",
                "Revenue mix-adjusted pricing",
                "DCF (Discounted Cash Flow)",
                "NPV, IRR, Payback Period",
                "Profitability Index",
                "WACC modelling",
                "EVA (Economic Value Added)",
                "ROIC analysis",
                "Working capital optimisation modelling",
            ],
            "🏦 M7 — Cash Flow & Working Capital": [
                "Cash flow statement analysis (indirect method)",
                "Free Cash Flow (FCF) calculation",
                "EBITDA-to-cash conversion rate",
                "Cash burn rate & runway analysis",
                "13-week cash flow forecast (direct method)",
                "Operating vs. structural vs. financing cash",
                "Cash Conversion Cycle (CCC) trend analysis",
                "DIO, DSO, DPO trend analysis",
                "Cash released per day of WC improvement",
                "Receivables aging (AR bucket analysis)",
                "Inventory aging analysis",
                "Bad debt provision modelling",
                "Payables optimisation modelling",
                "Supply chain finance modelling",
            ],
            "🤖 M8 — Advanced & AI-Powered": [
                "Multiple regression with feature selection",
                "Decision tree modelling (churn, credit risk)",
                "Random Forest feature importance",
                "Gradient boosting forecasting",
                "K-Means customer / SKU segmentation",
                "Principal Component Analysis (PCA)",
                "Isolation Forest anomaly detection",
                "Monte Carlo simulation (full distribution)",
                "Tornado chart (sensitivity ranking)",
                "AI-driven variance commentary generation",
                "NLP on earnings call transcripts",
                "LLM-assisted financial modelling",
                "EVA-based value creation mapping",
                "SCR storytelling framework",
                "Insight → Action → Outcome framework",
                "Chart design principles for finance",
            ],
            "📣 M9 — Insight Communication & Storytelling": [
                "SCR (Situation → Complication → Resolution) framework",
                "Pyramid Principle (top-down communication)",
                "The So-What? Test — 4 levels of insight value",
                "Insight → Action → Outcome framework",
                "Chart type selection guide",
                "10 chart design rules for finance",
                "Before & after chart redesign examples",
                "Executive KPI summary card design",
                "Board pack narrative structure",
                "3-minute CEO verbal briefing script",
                "Governing thought formulation",
            ],
            "🎯 M10 — Capstone Real-World Cases": [
                "Case 1: Apex Industrial — Full-year FP&A review (manufacturing)",
                "Case 2: BrightMart FMCG — SKU rationalisation & customer profitability",
                "Case 3: MediCore Pharma — M&A acquisition valuation & synergy analysis",
                "Case 4: StructoGroup — Financial distress & turnaround analytics",
                "Altman Z-Score distress diagnostics",
                "13-week survival cash flow forecast",
                "Covenant headroom analysis",
                "DCF valuation with Monte Carlo range",
                "PVM bridge + cost-to-serve integration",
                "Turnaround roadmap with leverage reduction path",
                "10-question integrated capstone quiz",
            ],
        }

        for mod_name, tech_list in techniques.items():
            st.markdown(f"**{mod_name}**")
            cols_t = st.columns(2)
            for i, t in enumerate(tech_list):
                with cols_t[i % 2]:
                    st.markdown(f"- {t}")
            st.markdown("")

    # How to run
    st.markdown("---")
    c1, c2 = st.columns([3, 1])
    with c1:
        st.info(
            "**How to run:** Place all 11 .py files in the same folder.  \n"
            "Run: `streamlit run FA_Overview.py`  \n"
            "Requires: `streamlit`, `pandas`, `numpy`, `plotly`, `scipy`  \n"
            "Install: `pip install streamlit pandas numpy plotly scipy`"
        )
    with c2:
        st.markdown(
            "<div style='background:#F0F4F8; border-radius:10px; padding:14px; text-align:center;'>"
            "<div style='font-size:12px; color:#666;'>All 11 files needed:</div>"
            "<div style='font-size:10px; color:#185FA5; line-height:1.9; margin-top:4px; text-align:left;'>"
            "FA_Overview.py<br>"
            "FA_M1_Descriptive_Historical.py<br>"
            "FA_M2_Comparative_Benchmarking.py<br>"
            "FA_M3_Diagnostic_Variance.py<br>"
            "FA_M4_Exploratory_Statistical.py<br>"
            "FA_M5_Predictive_Forecasting.py<br>"
            "FA_M6_Commercial_Customer_Value.py<br>"
            "FA_M7_CashFlow_WorkingCapital.py<br>"
            "FA_M8_Advanced_AI_Analytics.py<br>"
            "FA_M9_Insight_Communication.py<br>"
            "FA_M10_Capstone_Case_Studies.py"
            "</div></div>",
            unsafe_allow_html=True,
        )

else:
    # ── LAZY LOAD & RUN selected module ───────────────────────────────────────
    filename, alias = file_info
    filepath = os.path.join(BASE_DIR, filename)

    if not os.path.exists(filepath):
        st.error(
            f"**Module file not found:** `{filename}`  \n\n"
            f"Please make sure all module files are in the **same folder** as `FA_Overview.py`.  \n"
            f"Expected path: `{filepath}`"
        )
        st.info(
            "**All 11 files must be in the same directory:**  \n"
            "FA_Overview.py, FA_M1_Descriptive_Historical.py, FA_M2_Comparative_Benchmarking.py, "
            "FA_M3_Diagnostic_Variance.py, FA_M4_Exploratory_Statistical.py, "
            "FA_M5_Predictive_Forecasting.py, FA_M6_Commercial_Customer_Value.py, "
            "FA_M7_CashFlow_WorkingCapital.py, FA_M8_Advanced_AI_Analytics.py, "
            "FA_M9_Insight_Communication.py, FA_M10_Capstone_Case_Studies.py"
        )
    else:
        mod = _load(filename, alias)
        if mod is not None:
            mod.show()
        else:
            st.error(f"Could not load module: {filename}")