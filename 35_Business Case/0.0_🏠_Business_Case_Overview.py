# ============================================================================
#  BUSINESS CASE — Section
#  Page 0 · Overview / Landing Page
#  Streamlit multi-page app module  (place FIRST in the pages order)
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Business Case · Overview",
    page_icon="🏠",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with all section pages)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .bc-hero {
            background: linear-gradient(120deg, #0B3D91 0%, #1565C0 55%, #1E88E5 100%);
            padding: 40px 44px; border-radius: 20px; color: #ffffff;
            box-shadow: 0 12px 32px rgba(11,61,145,0.30); margin-bottom: 14px;
        }
        .bc-hero h1 { color:#ffffff; margin:0; font-size:2.4rem; font-weight:800; }
        .bc-hero p  { color:#E8F0FE; margin:10px 0 0 0; font-size:1.12rem; max-width:900px; }
        .bc-pill {
            display:inline-block; background:rgba(255,255,255,0.18);
            padding:6px 16px; border-radius:30px; font-size:0.82rem;
            margin-top:16px; margin-right:8px; letter-spacing:.4px;
        }
        .bc-card {
            background:#ffffff; border:1px solid #E3E8EF; border-left:5px solid #1565C0;
            padding:18px 22px; border-radius:12px; margin:12px 0;
            box-shadow:0 3px 10px rgba(0,0,0,0.05); height:100%;
        }
        .bc-card h4 { margin-top:0; color:#0B3D91; }
        .bc-key {
            background:#F1F7FF; border:1px solid #CFE2FF; border-radius:12px;
            padding:18px 22px; margin:12px 0;
        }
        .bc-step {
            background:#ffffff; border:1px solid #E3E8EF; border-radius:12px;
            padding:14px 18px; margin:8px 0; box-shadow:0 2px 6px rgba(0,0,0,0.04);
        }
        .bc-step b { color:#1565C0; }
        .part-head {
            background:#0B3D91; color:#fff; border-radius:8px; padding:8px 16px;
            font-weight:700; font-size:1.02rem; margin:14px 0 4px 0;
        }
        .tag {
            display:inline-block; background:#E7F0FF; color:#0B3D91; border:1px solid #CFE2FF;
            border-radius:20px; padding:3px 12px; font-size:.76rem; font-weight:700; margin:3px;
        }
        .muted{ color:#5A6472; }
        .big-num {
            font-size:2.0rem; font-weight:800; color:#1565C0; line-height:1;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="bc-hero">
        <h1>📊 Business Case</h1>
        <p>An interactive, practice-oriented masterclass in <b>investment evaluation</b> — everything a
        finance professional needs to appraise a project, quantify its risk, and make a defensible
        invest / don't-invest decision. Learn the theory, work through examples, experiment in live
        labs, and test yourself with quizzes.</p>
        <div>
            <span class="bc-pill">🎓 17 interactive pages</span>
            <span class="bc-pill">🧮 Basic → Advanced methods</span>
            <span class="bc-pill">🎛️ Hands-on labs</span>
            <span class="bc-pill">✅ Quizzes + final certificate</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# QUICK STATS
# ----------------------------------------------------------------------------
s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="bc-card"><div class="big-num">7</div>'
                '<div class="muted">Parts, foundations to assessment</div></div>',
                unsafe_allow_html=True)
with s2:
    st.markdown('<div class="bc-card"><div class="big-num">12+</div>'
                '<div class="muted">Appraisal methods covered</div></div>',
                unsafe_allow_html=True)
with s3:
    st.markdown('<div class="bc-card"><div class="big-num">4</div>'
                '<div class="muted">Tabs per page: Theory · Example · Lab · Quiz</div></div>',
                unsafe_allow_html=True)
with s4:
    st.markdown('<div class="bc-card"><div class="big-num">1</div>'
                '<div class="muted">Capstone builder + final exam</div></div>',
                unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------------
tab_about, tab_syllabus, tab_objectives, tab_process = st.tabs(
    ["🎯  About This Section", "🗂️  Full Syllabus", "🎓  Learning Objectives", "🧭  How to Learn"]
)

# ============================================================================
# TAB 1 — ABOUT
# ============================================================================
with tab_about:
    st.subheader("What is this section about?")
    st.markdown(
        """
        <div class="bc-key">
        As a finance manager, every significant investment — a new machine, a factory automation, a
        product launch, a cost-savings project — requires an <b>investment evaluation exercise</b> we
        call a <b>Business Case</b>. You estimate the <b>cash inflows</b> (savings or income the
        investment generates) and <b>cash outflows</b> (what you spend), then apply a series of methods
        to judge whether the investment creates value — before committing capital.
        <br><br>
        This section teaches that end-to-end skill, <b>step by step</b>, from the most basic screen to
        advanced risk techniques, and shows you how to turn the analysis into a <b>clear, governed
        recommendation</b> you can take to the board.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Who is it for?")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👩‍💼 Finance professionals</h4>
            Analysts, controllers and managers who prepare or review business cases and capex proposals.
            </div>
            """, unsafe_allow_html=True)
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>🏭 Business & operations leaders</h4>
            Anyone sponsoring projects who needs to understand how investment decisions are justified.
            </div>
            """, unsafe_allow_html=True)
    with c3:
        st.markdown(
            """
            <div class="bc-card">
            <h4>🎓 Students & learners</h4>
            Those studying corporate finance who want hands-on, practical mastery — not just theory.
            </div>
            """, unsafe_allow_html=True)

    st.subheader("What makes it different?")
    for t, b in [
        ("🎛️ Interactive, not passive",
         "Every method has a live lab — change inputs, edit cash-flow tables, and watch NPV, IRR and "
         "charts recompute instantly. You learn by doing."),
        ("🪜 Truly step-by-step",
         "The section builds logically: identify cash flows → discount them → apply each method → "
         "analyse risk → decide. Each page builds on the last."),
        ("🧰 Basic to advanced in one place",
         "From simple payback to Monte Carlo simulation and real options — a complete toolkit under "
         "one roof."),
        ("📝 Decision-focused",
         "It doesn't stop at the maths. You learn to weigh qualitative factors, apply governance, and "
         "write a defensible recommendation."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

# ============================================================================
# TAB 2 — FULL SYLLABUS
# ============================================================================
with tab_syllabus:
    st.subheader("🗂️ The Complete Syllabus")
    st.markdown("Seven parts, seventeen pages. Each page (except this overview and the final quiz) "
                "follows the same **Theory → Worked Example → Interactive Lab → Quiz** structure.")

    syllabus = {
        "Part 0 · Foundations": [
            ("0.1 · What is a Business Case?", "Definition, purpose, the 7-step process, when it's needed"),
            ("0.2 · Cash Flows: Inflows & Outflows", "Relevant cash flows, incremental principle, sunk costs, working capital, terminal value"),
            ("0.3 · Time Value of Money & Discount Rate", "PV/FV, WACC, hurdle rate, choosing the right rate"),
        ],
        "Part 1 · Non-Discounted (Basic) Methods": [
            ("1.1 · Payback Period", "Simple & uneven-cash-flow payback, the cutoff rule, pros & cons"),
            ("1.2 · Accounting Rate of Return (ARR)", "ARR on initial vs average investment, profit vs cash"),
        ],
        "Part 2 · Discounted (Core) Methods": [
            ("2.1 · Net Present Value (NPV)", "The gold standard — decision rule, NPV profile"),
            ("2.2 · Internal Rate of Return (IRR & MIRR)", "IRR, reinvestment trap, multiple IRRs, MIRR fix"),
            ("2.3 · Discounted Payback Period", "Payback that respects the time value of money"),
            ("2.4 · Profitability Index (PI)", "Value per euro, ideal for capital rationing"),
        ],
        "Part 3 · Advanced Evaluation & Risk": [
            ("3.1 · Sensitivity Analysis", "One-variable-at-a-time, tornado charts, break-even values"),
            ("3.2 · Scenario Analysis", "Base / Best / Worst bundles, probability-weighted expected NPV"),
            ("3.3 · Monte Carlo Simulation", "Distributions, thousands of trials, probability of loss"),
            ("3.4 · Real Options & EVA", "Value of flexibility (expand/defer/abandon) + economic profit"),
        ],
        "Part 4 · Decision-Making Framework": [
            ("4.1 · Decision Rules & Method Comparison", "Accept/reject rules, NPV vs IRR conflicts"),
            ("4.2 · Mutually Exclusive Projects & Capital Rationing", "Ranking, EAA method, constrained budgets"),
            ("4.3 · Qualitative Factors & Governance", "Strategic fit, ESG, risk, approval workflow"),
        ],
        "Part 5 · Build a Real Business Case": [
            ("5.1 · End-to-End Case Builder", "Editable template combining every method into one appraisal + printable recommendation"),
        ],
        "Part 6 · Assessment": [
            ("6.1 · Master Quiz", "Mixed 18-question test with scoring and a certificate-style pass summary"),
        ],
    }

    for part, pages in syllabus.items():
        st.markdown(f"<div class='part-head'>{part}</div>", unsafe_allow_html=True)
        df = pd.DataFrame(pages, columns=["Page", "What you'll learn"])
        st.dataframe(df, use_container_width=True, hide_index=True)

    st.info("💡 Pages appear in the left-hand sidebar in this exact order — just click any page to jump "
            "straight to it.")

# ============================================================================
# TAB 3 — LEARNING OBJECTIVES
# ============================================================================
with tab_objectives:
    st.subheader("🎓 Learning Objectives")
    st.markdown(
        """
        <div class="bc-key">
        By the end of this section, you will be able to <b>independently prepare, analyse and defend a
        complete business case</b> for any investment in your organisation.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### By the end, you will be able to…")
    objectives = [
        ("🧾 Identify the right cash flows",
         "Distinguish incremental from sunk costs, handle opportunity costs, working capital and "
         "terminal value, and build a clean year-by-year cash-flow model."),
        ("⏳ Apply the time value of money",
         "Discount future cash flows correctly and choose an appropriate discount rate / WACC."),
        ("🧮 Use every appraisal method",
         "Compute and interpret Payback, ARR, NPV, IRR, MIRR, Discounted Payback and PI — and know "
         "when each is appropriate."),
        ("🎲 Quantify and communicate risk",
         "Run sensitivity, scenario and Monte Carlo analysis, and understand real options and EVA."),
        ("⚖️ Make the right decision",
         "Apply accept/reject rules, resolve NPV-vs-IRR conflicts, rank projects, and allocate a "
         "limited budget."),
        ("📝 Produce a governed recommendation",
         "Weigh qualitative factors, respect approval governance, and write a clear, defensible "
         "invest / don't-invest recommendation."),
    ]
    cols = st.columns(2)
    for i, (t, b) in enumerate(objectives):
        with cols[i % 2]:
            st.markdown(f"<div class='bc-card'><h4>{t}</h4>{b}</div>", unsafe_allow_html=True)

    st.markdown("#### Skills you'll practise")
    st.markdown(
        """
        <div>
          <span class="tag">Cash-flow modelling</span>
          <span class="tag">Discounting & WACC</span>
          <span class="tag">Payback / ARR</span>
          <span class="tag">NPV</span>
          <span class="tag">IRR / MIRR</span>
          <span class="tag">Profitability Index</span>
          <span class="tag">Sensitivity / tornado</span>
          <span class="tag">Scenario analysis</span>
          <span class="tag">Monte Carlo</span>
          <span class="tag">Real options</span>
          <span class="tag">EVA</span>
          <span class="tag">EAA & capital rationing</span>
          <span class="tag">Qualitative scoring</span>
          <span class="tag">Governance & approvals</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================================
# TAB 4 — HOW TO LEARN (PROCESS)
# ============================================================================
with tab_process:
    st.subheader("🧭 How to Get the Most From This Section")

    st.markdown("#### The 4-tab learning method (on every page)")
    st.markdown(
        "Each topic page is structured the same way so you can learn consistently and build real "
        "understanding, not just memorise formulas:"
    )
    m = pd.DataFrame(
        {
            "Tab": ["📘 Theory", "🧮 Worked Example", "🎛️ Interactive Lab", "✅ Quiz"],
            "Purpose": [
                "Understand the concept, formula, when/why to use it, and its pros & cons",
                "See it solved step by step with real numbers and charts",
                "Experiment hands-on — change inputs and watch the results update live",
                "Check your understanding with instant, explained feedback",
            ],
            "How to use it": [
                "Read first; note the key formula and decision rule",
                "Follow each step; make sure you can reproduce the logic",
                "Try to break it — test extremes and edge cases to build intuition",
                "Aim for 100%; revisit Theory for anything you miss",
            ],
        }
    )
    st.table(m)

    st.markdown("#### Recommended learning path")
    for t, b in [
        ("1️⃣ Start with Foundations (Part 0)",
         "Don't skip these. Cash flows and the time value of money underpin every method that follows."),
        ("2️⃣ Build up through the methods (Parts 1 → 2)",
         "Learn the basic screens first, then the discounted core methods (NPV, IRR, PI). Notice how "
         "each fixes the limitations of the last."),
        ("3️⃣ Add risk & judgement (Parts 3 → 4)",
         "Layer on risk analysis, then the decision framework — how to actually choose between projects "
         "and govern the decision."),
        ("4️⃣ Build a real case (Part 5)",
         "Use the End-to-End Case Builder with your own project numbers to produce a full appraisal and "
         "recommendation."),
        ("5️⃣ Prove it (Part 6)",
         "Take the Master Quiz. Score 70%+ to earn your certificate of completion."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    # Simple visual roadmap
    st.markdown("#### Your journey at a glance")
    stages = ["Foundations", "Basic Methods", "Discounted Methods",
              "Risk & Advanced", "Decision Framework", "Build a Case", "Assessment"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(len(stages))), y=[1] * len(stages),
        mode="markers+lines+text",
        line=dict(color="#1565C0", width=4),
        marker=dict(size=26, color="#0B3D91", line=dict(color="#ffffff", width=2)),
        text=[f"P{i}" for i in range(len(stages))],
        textposition="middle center", textfont=dict(color="white", size=11),
        hovertext=stages, hoverinfo="text",
    ))
    for i, s in enumerate(stages):
        fig.add_annotation(x=i, y=1, text=s, showarrow=False, yshift=-38,
                           font=dict(size=11, color="#0B3D91"))
    fig.update_layout(height=200, margin=dict(t=20, b=40, l=20, r=20),
                      xaxis=dict(visible=False), yaxis=dict(visible=False, range=[0.5, 1.5]),
                      plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### A few tips for success")
    st.markdown(
        """
        - ✍️ **Learn by doing** — the labs are where intuition is built. Always try your own numbers.
        - 🔁 **Revisit** — it's fine to loop back to Foundations when a later method feels shaky.
        - 🧪 **Test extremes** — push inputs to their limits to see how each metric behaves.
        - 🎯 **Apply it** — bring a real project from your own work into the Case Builder (Part 5).
        """
    )
    st.success("👈 Ready to begin? Open **`0.1 · What is a Business Case?`** from the sidebar and start "
               "your journey. Good luck! 🚀")

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown("---")
c1, c2 = st.columns([2, 1])
with c1:
    st.markdown("**Business Case section** · An interactive investment-evaluation masterclass")
with c2:
    st.markdown("**Start here:** `0.1 · What is a Business Case?` ➡️")
st.caption("Overview · Built with Streamlit")
