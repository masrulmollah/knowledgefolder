"""
================================================================================
APPLIED FINANCIAL MODELS — COURSE OVERVIEW PAGE
================================================================================

A single-page, interactive Streamlit application that serves as the OVERVIEW /
LANDING page for the "Applied Financial Models" learning website.

It presents the full syllabus for finance professionals who want to learn how to
UNDERSTAND, BUILD, INTERPRET and ACT ON financial models. Learners can:
  - Browse the complete curriculum (Parts 0-7 + Capstone)
  - Filter modules by difficulty level and search by keyword
  - Track their own progress with interactive checkboxes
  - Use the "Which model do I need?" wizard to find the right model
  - Understand the standard 5-tab structure used in every module
  - Download the full syllabus as a Markdown file

Each module in the live site opens into 5 tabs:
  Theory & Concepts | Worked Examples | Interactive Exercises |
  Real-Life Practical Cases | Knowledge Test / Quiz

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
    pip install streamlit pandas
    streamlit run Applied_Financial_Models_Overview.py
================================================================================
"""

from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Applied Financial Models — Overview",
    layout="wide",
    page_icon="📈",
)

# --------------------------------------------------------------------------------
# CURRICULUM DATA
# --------------------------------------------------------------------------------
# Each module: (part, part_title, module_code, module_title, level, outcomes)
LEVELS = ["Foundational", "Intermediate", "Advanced"]

CURRICULUM = [
    # Part 0 — Orientation & Foundations
    ("0", "Orientation & Foundations", "0.1", "What is a Financial Model?",
     "Foundational", "Definition, purpose, types, and when models add value vs. mislead."),
    ("0", "Orientation & Foundations", "0.2", "Model Design Principles",
     "Foundational", "Inputs → Calculations → Outputs, logical flow, transparency, the FAST standard."),
    ("0", "Orientation & Foundations", "0.3", "Best Practices & Golden Rules",
     "Foundational", "Formatting conventions, colour-coding, one formula per row, no hardcoding, error checks."),
    ("0", "Orientation & Foundations", "0.4", "Core Building Blocks",
     "Foundational", "Time value of money, discounting, compounding, growth rates, key ratios."),
    ("0", "Orientation & Foundations", "0.5", "Choosing the Right Model",
     "Foundational", "Decision tree: matching the business question to the appropriate model type."),

    # Part 1 — The 3-Statement Model
    ("1", "The Three-Statement Model", "1.1", "Income Statement Modeling",
     "Intermediate", "Revenue drivers, cost behaviour, margins, and forecasting techniques."),
    ("1", "The Three-Statement Model", "1.2", "Balance Sheet Modeling",
     "Intermediate", "Working capital, fixed assets, and debt & equity schedules."),
    ("1", "The Three-Statement Model", "1.3", "Cash Flow Statement Modeling",
     "Intermediate", "Indirect method and linking to the other two statements."),
    ("1", "The Three-Statement Model", "1.4", "Integrating & Balancing the Model",
     "Intermediate", "The plug, circularity, balance checks, and iterative calculation."),
    ("1", "The Three-Statement Model", "1.5", "Supporting Schedules",
     "Intermediate", "Depreciation, debt/interest, working capital, and tax schedules."),

    # Part 2 — Forecasting & Budgeting
    ("2", "Forecasting & Budgeting Models", "2.1", "Revenue Forecasting Techniques",
     "Intermediate", "Top-down vs. bottom-up, volume × price, and market-share methods."),
    ("2", "Forecasting & Budgeting Models", "2.2", "Cost & OPEX Forecasting",
     "Intermediate", "Fixed/variable splits, cost inflation, and step costs."),
    ("2", "Forecasting & Budgeting Models", "2.3", "Budget vs. Actual (Variance) Models",
     "Intermediate", "Rolling forecasts, variance analysis, and bridge charts."),
    ("2", "Forecasting & Budgeting Models", "2.4", "Driver-Based Planning",
     "Intermediate", "Translating operational KPIs into financial outputs (ideal for manufacturing)."),

    # Part 3 — Valuation
    ("3", "Valuation Models", "3.1", "Discounted Cash Flow (DCF)",
     "Advanced", "Free cash flow, WACC, terminal value, enterprise vs. equity value."),
    ("3", "Valuation Models", "3.2", "Comparable Company Analysis (Comps)",
     "Advanced", "Trading multiples (EV/EBITDA, P/E) and peer selection."),
    ("3", "Valuation Models", "3.3", "Precedent Transactions",
     "Advanced", "Deal multiples and control premiums."),
    ("3", "Valuation Models", "3.4", "Dividend Discount Model (DDM)",
     "Advanced", "Gordon growth and multi-stage models."),
    ("3", "Valuation Models", "3.5", "Sum-of-the-Parts (SOTP)",
     "Advanced", "Valuing conglomerates and multi-BU businesses."),

    # Part 4 — Investment Appraisal & Capital Budgeting
    ("4", "Investment Appraisal & Capital Budgeting", "4.1", "NPV & IRR Models",
     "Intermediate", "Cash flow timelines, hurdle rates, and decision rules."),
    ("4", "Investment Appraisal & Capital Budgeting", "4.2", "Payback & Discounted Payback",
     "Intermediate", "Simple vs. discounted payback and their limitations."),
    ("4", "Investment Appraisal & Capital Budgeting", "4.3", "Capex Business Case Model",
     "Advanced", "Full investment appraisal with financing, tax, and terminal value."),
    ("4", "Investment Appraisal & Capital Budgeting", "4.4", "Cost-Benefit & Cost-Savings Models",
     "Intermediate", "Automation/efficiency projects and incremental analysis."),
    ("4", "Investment Appraisal & Capital Budgeting", "4.5", "Replacement & Make-vs-Buy Decisions",
     "Intermediate", "Incremental cash flows and opportunity cost."),

    # Part 5 — Scenario, Sensitivity & Risk
    ("5", "Scenario, Sensitivity & Risk Models", "5.1", "Sensitivity Analysis",
     "Intermediate", "One-way & two-way data tables and tornado charts."),
    ("5", "Scenario, Sensitivity & Risk Models", "5.2", "Scenario Analysis",
     "Intermediate", "Base / Best / Worst cases and scenario managers."),
    ("5", "Scenario, Sensitivity & Risk Models", "5.3", "Monte Carlo Simulation",
     "Advanced", "Probability distributions and risk quantification."),
    ("5", "Scenario, Sensitivity & Risk Models", "5.4", "Break-Even & Margin of Safety",
     "Foundational", "CVP analysis, break-even point, and operating leverage."),

    # Part 6 — Specialized & Advanced
    ("6", "Specialized & Advanced Models", "6.1", "LBO (Leveraged Buyout) Model",
     "Advanced", "Debt structuring, returns to equity, and exit analysis."),
    ("6", "Specialized & Advanced Models", "6.2", "M&A / Accretion-Dilution Model",
     "Advanced", "Deal structuring, synergies, and EPS impact."),
    ("6", "Specialized & Advanced Models", "6.3", "Project Finance Model",
     "Advanced", "Debt sculpting, DSCR, and covenant testing."),
    ("6", "Specialized & Advanced Models", "6.4", "Working Capital Optimization Model",
     "Intermediate", "Cash conversion cycle and inventory/receivables levers."),
    ("6", "Specialized & Advanced Models", "6.5", "Manufacturing / Factory Cost Model",
     "Intermediate", "Absorption costing, wastage analytics, and cost-per-unit."),

    # Part 7 — From Model to Decision
    ("7", "From Model to Decision", "7.1", "Extracting Insights",
     "Intermediate", "Reading outputs and spotting value drivers & red flags."),
    ("7", "From Model to Decision", "7.2", "Storytelling with Models",
     "Intermediate", "Translating numbers into executive recommendations."),
    ("7", "From Model to Decision", "7.3", "Presenting to Decision-Makers",
     "Intermediate", "Dashboards, one-page summaries, and board-ready outputs."),
    ("7", "From Model to Decision", "7.4", "Common Pitfalls & Model Auditing",
     "Advanced", "Spotting errors, avoiding garbage-in-garbage-out, stress-testing assumptions."),
    ("7", "From Model to Decision", "7.5", "Ethics & Assumption Integrity",
     "Foundational", "Bias, over-optimism, and transparency to stakeholders."),
]

PART_ICONS = {
    "0": "🧭", "1": "🏛️", "2": "📊", "3": "💰",
    "4": "🏗️", "5": "🎲", "6": "🚀", "7": "🎯",
}

LEVEL_COLORS = {
    "Foundational": "🟢",
    "Intermediate": "🟡",
    "Advanced": "🔴",
}

TAB_STRUCTURE = [
    ("📚 Theory & Concepts", "Clear explanation of the model, its logic, and when to use it."),
    ("🔢 Worked Examples", "Step-by-step build-through with real numbers."),
    ("✏️ Interactive Exercises", "Live sliders and input boxes — change inputs and watch outputs update in real time."),
    ("🏭 Real-Life Practical Cases", "Industry scenarios (FMCG, manufacturing, services) from real decisions."),
    ("✅ Knowledge Test / Quiz", "Multiple-choice and calculation questions with instant feedback and scoring."),
]

df = pd.DataFrame(
    CURRICULUM,
    columns=["Part", "PartTitle", "Code", "Module", "Level", "Outcomes"],
)

# --------------------------------------------------------------------------------
# SESSION STATE
# --------------------------------------------------------------------------------
if "completed" not in st.session_state:
    st.session_state.completed = set()

# --------------------------------------------------------------------------------
# SIDEBAR — CONTROL PANEL
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Control Panel")
st.sidebar.caption("Filter the curriculum and track your learning journey.")

search_term = st.sidebar.text_input("🔍 Search modules", "").strip().lower()

level_filter = st.sidebar.multiselect(
    "Difficulty level", LEVELS, default=LEVELS,
)

all_parts = df[["Part", "PartTitle"]].drop_duplicates()
part_labels = {
    row.Part: f"{PART_ICONS.get(row.Part, '•')} Part {row.Part} — {row.PartTitle}"
    for row in all_parts.itertuples()
}
part_filter = st.sidebar.multiselect(
    "Curriculum parts",
    options=list(part_labels.keys()),
    default=list(part_labels.keys()),
    format_func=lambda p: part_labels[p],
)

st.sidebar.markdown("---")
st.sidebar.subheader("📈 Your Progress")

total_modules = len(df)
done = len(st.session_state.completed)
pct = int(done / total_modules * 100) if total_modules else 0
st.sidebar.progress(pct / 100)
st.sidebar.metric("Modules completed", f"{done} / {total_modules}", f"{pct}%")

if st.sidebar.button("🔄 Reset progress"):
    st.session_state.completed = set()
    st.sidebar.info("Progress reset.")

st.sidebar.markdown("---")
st.sidebar.caption("Tip: tick modules as you finish them to watch your progress grow.")

# Apply filters
mask = df["Level"].isin(level_filter) & df["Part"].isin(part_filter)
if search_term:
    mask &= (
        df["Module"].str.lower().str.contains(search_term)
        | df["Outcomes"].str.lower().str.contains(search_term)
        | df["PartTitle"].str.lower().str.contains(search_term)
    )
filtered = df[mask]

# --------------------------------------------------------------------------------
# HERO HEADER
# --------------------------------------------------------------------------------
st.title("📈 Applied Financial Models")
st.markdown(
    """
Welcome to **Applied Financial Models** — a hands-on learning path that takes finance professionals
from *understanding* what a model is, to *building* it, to *extracting insights* and *recommending action*.

This is your **course overview**. Explore the full syllabus below, discover which model fits your
business question, and see how every module is structured for active, interactive learning.
"""
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Curriculum Parts", df["Part"].nunique())
c2.metric("Total Modules", len(df))
c3.metric("Learning Tabs / Module", len(TAB_STRUCTURE))
c4.metric("Capstone Project", "1")

st.markdown(
    "**Learning arc:** Understand → Build → Interpret → Decide. "
    "By the end you will know *which* model to use, how to *prepare* it, "
    "how to *read* it, and how to *add value* to your company."
)

tab_labels = [
    "🗂️ Syllabus Overview",
    "🧩 Learning Journey",
    "🧠 Which Model Do I Need?",
    "🔖 Module Tab Structure",
    "🎓 Capstone Project",
    "📄 Export Syllabus",
]
tabs = st.tabs(tab_labels)

# ================================================================================
# TAB 1 — SYLLABUS OVERVIEW
# ================================================================================
with tabs[0]:
    st.subheader("Full Syllabus")
    st.caption(
        f"Showing **{len(filtered)}** of **{len(df)}** modules "
        f"{LEVEL_COLORS['Foundational']} Foundational  "
        f"{LEVEL_COLORS['Intermediate']} Intermediate  "
        f"{LEVEL_COLORS['Advanced']} Advanced"
    )

    if filtered.empty:
        st.warning("No modules match your filters. Try widening the search or level selection.")
    else:
        for part, part_df in filtered.groupby("Part"):
            part_title = part_df["PartTitle"].iloc[0]
            icon = PART_ICONS.get(part, "•")
            with st.expander(f"{icon}  Part {part} — {part_title}  ·  ({len(part_df)} modules)", expanded=True):
                for row in part_df.itertuples():
                    key = f"chk_{row.Code}"
                    col_a, col_b = st.columns([0.06, 0.94])
                    with col_a:
                        checked = st.checkbox(
                            f"Mark module {row.Code} complete",
                            value=row.Code in st.session_state.completed,
                            key=key,
                            label_visibility="collapsed",
                        )
                        if checked:
                            st.session_state.completed.add(row.Code)
                        else:
                            st.session_state.completed.discard(row.Code)
                    with col_b:
                        st.markdown(
                            f"{LEVEL_COLORS[row.Level]} **{row.Code} · {row.Module}**  "
                            f"&nbsp;·&nbsp; _{row.Level}_"
                        )
                        st.caption(row.Outcomes)

# ================================================================================
# TAB 2 — LEARNING JOURNEY
# ================================================================================
with tabs[1]:
    st.subheader("How the Curriculum Flows")
    st.markdown(
        """
The course is deliberately sequenced so each part builds on the last:

1. **🧭 Part 0 — Foundations:** the mental framework and technical baseline.
2. **🏛️ Part 1 — 3-Statement Model:** the backbone of all financial modeling.
3. **📊 Part 2 — Forecasting & Budgeting:** turning drivers into forward-looking numbers.
4. **💰 Part 3 — Valuation:** what a business, project or asset is worth.
5. **🏗️ Part 4 — Investment Appraisal:** *should we invest?* — Capex decisions.
6. **🎲 Part 5 — Scenario, Sensitivity & Risk:** understanding uncertainty.
7. **🚀 Part 6 — Specialized & Advanced:** LBO, M&A, project finance, factory costing.
8. **🎯 Part 7 — From Model to Decision:** the "so what?" — insight and recommendation.
"""
    )

    st.markdown("##### 📊 Modules by Difficulty Level")
    level_counts = df["Level"].value_counts().reindex(LEVELS).fillna(0).astype(int)
    st.bar_chart(level_counts)

    st.markdown("##### 🗂️ Modules per Part")
    part_counts = (
        df.groupby("Part")["Module"].count()
        .rename("Modules")
    )
    part_counts.index = [f"Part {p}" for p in part_counts.index]
    st.bar_chart(part_counts)

    st.info(
        "💡 **Suggested pace:** Foundational modules can be completed quickly to build momentum; "
        "reserve more time for Advanced valuation, LBO/M&A and Monte Carlo modules."
    )

# ================================================================================
# TAB 3 — WHICH MODEL DO I NEED? (WIZARD)
# ================================================================================
with tabs[2]:
    st.subheader("🧠 Which Financial Model Do I Need?")
    st.markdown("Answer one question and get pointed to the right module(s) to start with.")

    question = st.selectbox(
        "What decision or question are you trying to answer?",
        [
            "— Select —",
            "How will my company's financials look over the next 3–5 years?",
            "What is this business / share worth?",
            "Should we invest in this project or piece of equipment?",
            "What happens to my numbers if assumptions change?",
            "How risky is this outcome (range of possibilities)?",
            "How do I finance a large, long-life asset with debt?",
            "How do I reduce cost / improve productivity in a factory?",
            "How do I turn model outputs into a board recommendation?",
        ],
    )

    RECOMMENDATIONS = {
        "How will my company's financials look over the next 3–5 years?":
            ("Part 1 — Three-Statement Model & Part 2 — Forecasting & Budgeting",
             ["1.1", "1.2", "1.3", "1.4", "2.1", "2.4"]),
        "What is this business / share worth?":
            ("Part 3 — Valuation Models",
             ["3.1", "3.2", "3.4", "3.5"]),
        "Should we invest in this project or piece of equipment?":
            ("Part 4 — Investment Appraisal & Capital Budgeting",
             ["4.1", "4.2", "4.3", "4.5"]),
        "What happens to my numbers if assumptions change?":
            ("Part 5 — Sensitivity & Scenario Analysis",
             ["5.1", "5.2", "5.4"]),
        "How risky is this outcome (range of possibilities)?":
            ("Part 5 — Monte Carlo Simulation",
             ["5.3"]),
        "How do I finance a large, long-life asset with debt?":
            ("Part 6 — Project Finance & LBO",
             ["6.1", "6.3"]),
        "How do I reduce cost / improve productivity in a factory?":
            ("Part 6 — Manufacturing / Factory Cost & Working Capital",
             ["6.4", "6.5", "2.2"]),
        "How do I turn model outputs into a board recommendation?":
            ("Part 7 — From Model to Decision",
             ["7.1", "7.2", "7.3"]),
    }

    if question != "— Select —":
        title, codes = RECOMMENDATIONS[question]
        st.success(f"👉 Start here: **{title}**")
        rec = df[df["Code"].isin(codes)]
        for row in rec.itertuples():
            st.markdown(f"- {LEVEL_COLORS[row.Level]} **{row.Code} · {row.Module}** — {row.Outcomes}")
    else:
        st.info("Select a question above to see your recommended learning path.")

# ================================================================================
# TAB 4 — MODULE TAB STRUCTURE
# ================================================================================
with tabs[3]:
    st.subheader("🔖 How Every Module is Structured")
    st.markdown(
        "To make learning **active, not passive**, every model in the site opens into the same "
        "five tabs. This consistency lets learners focus on the content, not the navigation."
    )
    for i, (name, desc) in enumerate(TAB_STRUCTURE, start=1):
        st.markdown(f"**{i}. {name}**")
        st.caption(desc)
        st.markdown("")

    st.markdown("---")
    st.markdown("##### 🔍 Preview: a live module (e.g. NPV & IRR)")
    demo = st.tabs([t[0] for t in TAB_STRUCTURE])
    with demo[0]:
        st.write("Explains discounting, hurdle rates, and the NPV/IRR decision rules.")
    with demo[1]:
        st.write("A €6m Capex example worked through year by year to NPV and IRR.")
    with demo[2]:
        cap = st.slider("Investment (€m)", 1.0, 10.0, 6.0, 0.5)
        sav = st.slider("Annual savings (€m)", 0.5, 5.0, 1.5, 0.1)
        rate = st.slider("Discount rate (%)", 5.0, 20.0, 10.0, 0.5)
        years = 8
        npv = -cap + sum(sav / ((1 + rate / 100) ** y) for y in range(1, years + 1))
        st.metric("Indicative NPV (8 yrs)", f"€{npv:,.2f}m",
                  "Accept ✅" if npv > 0 else "Reject ❌")
        st.caption("A taste of the interactive exercises learners will use in each module.")
    with demo[3]:
        st.write("Real FMCG / manufacturing Capex cases — e.g. automation vs. manual line.")
    with demo[4]:
        st.write("Instant-feedback quiz to confirm mastery before moving on.")

# ================================================================================
# TAB 5 — CAPSTONE PROJECT
# ================================================================================
with tabs[4]:
    st.subheader("🎓 Capstone Project")
    st.markdown(
        """
The course finishes with an **integrated, real-world challenge** that brings every skill together.

**The scenario:** learners receive a realistic business case — for example, a **factory Capex
investment** or a **company valuation**.

**What they do:**
- Build a full model interactively (statements → forecast → appraisal/valuation).
- Run **sensitivity and scenario** analysis to stress-test assumptions.
- **Extract insights** — identify the value drivers and red flags.
- Submit a **clear recommendation** to a decision-maker.

**How it's assessed:** the submission is scored against a **model answer**, with feedback on both
the *technical build* and the *quality of the recommendation*.

> 🎯 **Outcome:** learners leave able to choose the right model, build it correctly, interpret it,
> and add measurable value to their organisation.
"""
    )
    st.success("Complete all modules to unlock the Capstone — a portfolio-ready piece of work.")

# ================================================================================
# TAB 6 — EXPORT SYLLABUS
# ================================================================================
with tabs[5]:
    st.subheader("📄 Export the Full Syllabus")
    st.write("Download the complete curriculum as a Markdown file to share or print.")

    lines = [
        "# Applied Financial Models — Full Syllabus",
        "",
        f"_Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
        "",
        f"- **Parts:** {df['Part'].nunique()}",
        f"- **Modules:** {len(df)}",
        f"- **Tabs per module:** {len(TAB_STRUCTURE)} "
        f"({', '.join(t[0] for t in TAB_STRUCTURE)})",
        "",
    ]
    for part, part_df in df.groupby("Part"):
        icon = PART_ICONS.get(part, "•")
        lines.append(f"## {icon} Part {part} — {part_df['PartTitle'].iloc[0]}")
        lines.append("")
        for row in part_df.itertuples():
            lines.append(f"- **{row.Code} {row.Module}** ({row.Level}) — {row.Outcomes}")
        lines.append("")
    lines.append("## 🎓 Capstone Project")
    lines.append("")
    lines.append("An integrated challenge (e.g. a factory Capex or company valuation): build the "
                 "model, run scenarios, extract insights, and submit a scored recommendation.")
    syllabus_md = "\n".join(lines)

    st.text_area("Preview", syllabus_md, height=320)
    st.download_button(
        "⬇️ Download Syllabus (Markdown)",
        syllabus_md.encode("utf-8"),
        "applied_financial_models_syllabus.md",
        "text/markdown",
    )
    st.download_button(
        "⬇️ Download Curriculum (CSV)",
        df.to_csv(index=False).encode("utf-8"),
        "applied_financial_models_curriculum.csv",
        "text/csv",
    )

st.markdown("---")
st.caption(
    "Applied Financial Models — an interactive learning platform. "
    "Understand the model · Build the model · Interpret the model · Decide with confidence."
)
