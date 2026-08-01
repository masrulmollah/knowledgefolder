# ============================================================================
#  BUSINESS CASE — Section
#  Page 6.1 · Master Quiz  (FINAL ASSESSMENT)
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="6.1 · Master Quiz",
    page_icon="🏆",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Parts 0–5)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .bc-hero {
            background: linear-gradient(120deg, #0B3D91 0%, #1565C0 55%, #1E88E5 100%);
            padding: 34px 40px; border-radius: 18px; color: #ffffff;
            box-shadow: 0 10px 28px rgba(11,61,145,0.28); margin-bottom: 10px;
        }
        .bc-hero h1 { color:#ffffff; margin:0; font-size:2.0rem; font-weight:800; }
        .bc-hero p  { color:#E8F0FE; margin:8px 0 0 0; font-size:1.05rem; }
        .bc-pill {
            display:inline-block; background:rgba(255,255,255,0.18);
            padding:5px 14px; border-radius:30px; font-size:0.8rem;
            margin-top:14px; letter-spacing:.4px;
        }
        .bc-key {
            background:#F1F7FF; border:1px solid #CFE2FF; border-radius:12px;
            padding:16px 20px; margin:10px 0;
        }
        .cert {
            background: linear-gradient(135deg, #FFFDF5 0%, #FFF7E6 100%);
            border:2px solid #F5D9A0; border-radius:16px; padding:30px 34px; margin:16px 0;
            text-align:center; box-shadow:0 6px 20px rgba(249,168,37,0.18);
        }
        .cert h2 { color:#B8860B; margin:0 0 6px 0; }
        .cert .big { font-size:2.6rem; font-weight:800; color:#0B3D91; margin:6px 0; }
        .cert .sub { color:#5A6472; }
        .bc-tag {
            display:inline-block; background:#0B3D91; color:#fff; border-radius:6px;
            padding:2px 10px; font-size:.72rem; font-weight:700; margin-right:8px;
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
        <span class="bc-tag">PART 6 · ASSESSMENT</span>
        <h1>🏆 6.1 · Master Quiz</h1>
        <p>The final challenge. 18 mixed questions spanning the whole Business Case
        section — from cash flows and discounting to NPV, IRR, risk analysis and governance.
        Score 70%+ to pass.</p>
        <div class="bc-pill">📚 6 Parts &nbsp;•&nbsp; ❓ 18 Questions &nbsp;•&nbsp; 🎯 70% to Pass</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Tip: This pulls together every page. If you get one wrong, the explanation tells you "
           "which concept (and page) to revisit.")

# ----------------------------------------------------------------------------
# QUESTION BANK  (answer = index of correct option)
# ----------------------------------------------------------------------------
QUESTIONS = [
    # ---- Part 0 · Foundations ----
    {"part": "0 · Foundations",
     "q": "1. Which cash flows are relevant to a business case?",
     "options": ["All historical cash flows", "Only incremental cash flows that change with the decision",
                 "Only cash inflows", "Sunk costs plus incremental flows"],
     "answer": 1,
     "why": "Only incremental cash flows belong in the analysis (page 0.1/0.2)."},
    {"part": "0 · Foundations",
     "q": "2. A cost already incurred and unrecoverable is a…",
     "options": ["Opportunity cost", "Sunk cost", "Incremental cost", "Terminal value"],
     "answer": 1,
     "why": "Sunk costs are ignored in the decision (page 0.2)."},
    {"part": "0 · Foundations",
     "q": "3. The present value of €1 received in n years at rate r is…",
     "options": ["1 × (1+r)ⁿ", "1 / (1+r)ⁿ", "1 × r × n", "1 / (r×n)"],
     "answer": 1,
     "why": "Discounting divides by (1+r)ⁿ (page 0.3)."},
    # ---- Part 1 · Basic methods ----
    {"part": "1 · Basic Methods",
     "q": "4. The payback period measures…",
     "options": ["Total project profit", "Time to recover the initial investment",
                 "The IRR", "The present value of inflows"],
     "answer": 1,
     "why": "Payback = time for cumulative inflows to recover the outlay (page 1.1)."},
    {"part": "1 · Basic Methods",
     "q": "5. The biggest weakness shared by payback and ARR is that they…",
     "options": ["Are hard to compute", "Ignore the time value of money",
                 "Require a discount rate", "Overstate risk"],
     "answer": 1,
     "why": "Both non-discounted methods ignore the time value of money (pages 1.1–1.2)."},
    {"part": "1 · Basic Methods",
     "q": "6. ARR is based on…",
     "options": ["Cash flow before depreciation", "Accounting profit after depreciation",
                 "Only salvage value", "Free cash flow"],
     "answer": 1,
     "why": "ARR uses accounting profit (after depreciation), not cash (page 1.2)."},
    # ---- Part 2 · Discounted methods ----
    {"part": "2 · Discounted Methods",
     "q": "7. Under the NPV rule you accept a project when…",
     "options": ["NPV < 0", "NPV = 0", "NPV > 0", "NPV = payback"],
     "answer": 2,
     "why": "A positive NPV adds value (page 2.1)."},
    {"part": "2 · Discounted Methods",
     "q": "8. The IRR is the discount rate at which…",
     "options": ["NPV is maximised", "NPV equals zero", "Payback equals the cutoff", "PI equals 1"],
     "answer": 1,
     "why": "IRR is the rate where NPV = 0 (page 2.2). Note PI = 1 also ↔ NPV = 0, but IRR is defined via NPV=0 across rates."},
    {"part": "2 · Discounted Methods",
     "q": "9. A standard IRR unrealistically assumes interim cash flows are reinvested at…",
     "options": ["The inflation rate", "The IRR itself", "The risk-free rate", "Zero"],
     "answer": 1,
     "why": "IRR assumes reinvestment at the IRR; MIRR fixes this (page 2.2)."},
    {"part": "2 · Discounted Methods",
     "q": "10. The Profitability Index equals…",
     "options": ["Investment ÷ PV of inflows", "PV of inflows ÷ investment",
                 "NPV ÷ IRR", "Profit ÷ years"],
     "answer": 1,
     "why": "PI = PV of inflows ÷ initial investment = 1 + NPV/Investment (page 2.4)."},
    {"part": "2 · Discounted Methods",
     "q": "11. Discounted payback differs from simple payback because it…",
     "options": ["Ignores the time value of money", "Discounts cash flows before accumulating",
                 "Uses accounting profit", "Counts cash after payback"],
     "answer": 1,
     "why": "It discounts each cash flow first (page 2.3)."},
    # ---- Part 3 · Risk ----
    {"part": "3 · Risk & Advanced",
     "q": "12. A tornado chart ranks variables by…",
     "options": ["Alphabetical order", "Their impact on the result",
                 "Their cost", "The year they occur"],
     "answer": 1,
     "why": "Tornado charts order variables by impact, widest on top (page 3.1)."},
    {"part": "3 · Risk & Advanced",
     "q": "13. Expected NPV in scenario analysis is…",
     "options": ["The best-case NPV", "Σ (probability × scenario NPV)",
                 "The average of best and worst", "NPV ÷ scenarios"],
     "answer": 1,
     "why": "It's the probability-weighted average of scenario NPVs (page 3.2)."},
    {"part": "3 · Risk & Advanced",
     "q": "14. The main output of a Monte Carlo simulation is…",
     "options": ["A single NPV", "A full probability distribution of outcomes",
                 "The payback period", "The ARR"],
     "answer": 1,
     "why": "Thousands of trials produce a distribution, incl. probability of loss (page 3.3)."},
    {"part": "3 · Risk & Advanced",
     "q": "15. EVA is calculated as…",
     "options": ["NOPAT − (Capital × WACC)", "EBIT + depreciation",
                 "Revenue − variable cost", "NPV ÷ investment"],
     "answer": 0,
     "why": "EVA charges for all capital: NOPAT − capital charge (page 3.4)."},
    # ---- Part 4 · Decision framework ----
    {"part": "4 · Decision Framework",
     "q": "16. For mutually exclusive projects, the primary criterion is…",
     "options": ["Highest IRR", "Highest NPV", "Shortest payback", "Highest PI"],
     "answer": 1,
     "why": "NPV measures absolute value added — choose the highest (page 4.2)."},
    {"part": "4 · Decision Framework",
     "q": "17. To compare projects with unequal lives you should use…",
     "options": ["Raw NPV", "Equivalent Annual Annuity (EAA)", "Payback", "ARR"],
     "answer": 1,
     "why": "EAA converts NPV into a comparable annual figure (page 4.2)."},
    {"part": "4 · Decision Framework",
     "q": "18. A project mandated by safety law may proceed even if…",
     "options": ["Its NPV is negative", "Its IRR is high", "Its payback is short", "Its PI exceeds 1"],
     "answer": 0,
     "why": "Compliance / licence-to-operate spend can override a negative NPV (page 4.3)."},
]

PASS_MARK = 0.70

# ----------------------------------------------------------------------------
# QUIZ FORM
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="bc-key">
    <b>Instructions.</b> Answer all 18 questions, then click <b>Submit Master Quiz</b>. You'll get your
    overall score, a per-part breakdown, explanations for any misses, and — if you score 70% or more —
    a completion certificate. 🎓
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("master_quiz"):
    responses = []
    current_part = None
    for i, item in enumerate(QUESTIONS):
        if item["part"] != current_part:
            current_part = item["part"]
            st.markdown(f"### 📚 Part {current_part}")
        choice = st.radio(item["q"], item["options"], index=None, key=f"mq_{i}")
        responses.append(choice)
        st.markdown("<hr style='margin:6px 0;'>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🏁 Submit Master Quiz", type="primary")

# ----------------------------------------------------------------------------
# RESULTS
# ----------------------------------------------------------------------------
if submitted:
    total = len(QUESTIONS)
    answered = sum(1 for r in responses if r is not None)

    if answered < total:
        st.warning(f"⚠️ You've answered {answered} of {total} questions. Unanswered questions are "
                   f"marked incorrect. Scroll up to complete them, or review your results below.")

    # Score + per-part tally
    score = 0
    part_totals, part_correct = {}, {}
    for i, item in enumerate(QUESTIONS):
        part = item["part"]
        part_totals[part] = part_totals.get(part, 0) + 1
        correct_text = item["options"][item["answer"]]
        if responses[i] == correct_text:
            score += 1
            part_correct[part] = part_correct.get(part, 0) + 1

    pct = score / total * 100
    passed = (score / total) >= PASS_MARK

    st.markdown("## 📊 Your Results")
    m1, m2, m3 = st.columns(3)
    m1.metric("Score", f"{score} / {total}")
    m2.metric("Percentage", f"{pct:.0f}%")
    m3.metric("Result", "PASS ✅" if passed else "Not yet ❌")

    # Gauge
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=pct,
        number={"suffix": "%"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#1565C0"},
            "steps": [
                {"range": [0, 70], "color": "#FDECEC"},
                {"range": [70, 100], "color": "#E7F6EC"},
            ],
            "threshold": {"line": {"color": "#C62828", "width": 4}, "thickness": 0.8, "value": 70},
        },
        title={"text": "Overall score (pass mark 70%)"},
    ))
    gauge.update_layout(height=320, margin=dict(t=50, b=10))
    st.plotly_chart(gauge, use_container_width=True)

    # Per-part breakdown
    st.markdown("### 📚 Breakdown by Part")
    breakdown = pd.DataFrame(
        {
            "Part": list(part_totals.keys()),
            "Correct": [part_correct.get(p, 0) for p in part_totals],
            "Total": [part_totals[p] for p in part_totals],
        }
    )
    breakdown["Score %"] = (breakdown["Correct"] / breakdown["Total"] * 100).round(0)
    st.dataframe(
        breakdown.style.format({"Score %": "{:.0f}%"}),
        use_container_width=True, hide_index=True,
    )

    figb = go.Figure(go.Bar(
        x=breakdown["Part"], y=breakdown["Score %"],
        marker_color=["#1B7F3B" if v >= 70 else "#C62828" for v in breakdown["Score %"]],
        text=[f"{v:.0f}%" for v in breakdown["Score %"]], textposition="outside",
    ))
    figb.add_hline(y=70, line_dash="dash", line_color="#F9A825",
                   annotation_text="Pass 70%", annotation_position="top left")
    figb.update_layout(title="Performance by part", yaxis_title="Score %",
                       height=400, margin=dict(t=60, b=90))
    figb.update_xaxes(tickangle=-20)
    st.plotly_chart(figb, use_container_width=True)

    # Certificate or encouragement
    if passed:
        st.balloons()
        st.markdown(
            f"""
            <div class="cert">
                <h2>🎓 Certificate of Completion</h2>
                <div class="sub">This certifies successful completion of the</div>
                <div class="big">Business Case &amp; Investment Evaluation</div>
                <div class="sub">interactive learning section</div>
                <div class="big" style="font-size:1.8rem; color:#1B7F3B;">Score: {pct:.0f}%</div>
                <div class="sub">Payback · ARR · NPV · IRR/MIRR · PI · Sensitivity · Scenario ·
                Monte Carlo · Real Options · EVA · Decision Frameworks · Governance</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.success("🏆 Congratulations! You've demonstrated command of the full business-case toolkit — "
                   "from identifying cash flows to producing a governed, defensible recommendation.")
    else:
        st.info(f"📖 You scored {pct:.0f}%. You need {int(PASS_MARK*total)}/{total} (70%) to pass. "
                f"Review the explanations below — focus on the parts with the lowest scores — and try again.")

    # Detailed review
    st.markdown("### 🔍 Detailed Review")
    for i, item in enumerate(QUESTIONS):
        correct_text = item["options"][item["answer"]]
        chosen = responses[i]
        if chosen == correct_text:
            st.success(f"**Q{i+1}: Correct ✅** — {item['why']}")
        else:
            st.error(f"**Q{i+1}: Incorrect ❌** — Your answer: *{chosen if chosen else 'blank'}* · "
                     f"Correct: *{correct_text}*.\n\n{item['why']}")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `5.1 · End-to-End Case Builder`")
with cnext:
    st.markdown("🎉 **You've reached the end of the Business Case section!**")
st.caption("Business Case section · Page 6.1 · Final Assessment · Built with Streamlit")
