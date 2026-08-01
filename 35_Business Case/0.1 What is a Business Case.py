# ============================================================================
#  BUSINESS CASE — Section
#  Page 0.1 · What is a Business Case?
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="0.1 · What is a Business Case?",
    page_icon="📘",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .bc-hero {
            background: linear-gradient(120deg, #0B3D91 0%, #1565C0 55%, #1E88E5 100%);
            padding: 34px 40px; border-radius: 18px; color: #ffffff;
            box-shadow: 0 10px 28px rgba(11,61,145,0.28); margin-bottom: 10px;
        }
        .bc-hero h1 { color:#ffffff; margin:0; font-size:2.05rem; font-weight:800; }
        .bc-hero p  { color:#E8F0FE; margin:8px 0 0 0; font-size:1.05rem; }
        .bc-pill {
            display:inline-block; background:rgba(255,255,255,0.18);
            padding:5px 14px; border-radius:30px; font-size:0.8rem;
            margin-top:14px; letter-spacing:.4px;
        }
        .bc-card {
            background:#ffffff; border:1px solid #E3E8EF; border-left:5px solid #1565C0;
            padding:18px 22px; border-radius:12px; margin:12px 0;
            box-shadow:0 3px 10px rgba(0,0,0,0.05);
        }
        .bc-card h4 { margin-top:0; color:#0B3D91; }
        .bc-key {
            background:#F1F7FF; border:1px solid #CFE2FF; border-radius:12px;
            padding:16px 20px; margin:10px 0;
        }
        .bc-step {
            background:#ffffff; border:1px solid #E3E8EF; border-radius:12px;
            padding:14px 18px; margin:8px 0; box-shadow:0 2px 6px rgba(0,0,0,0.04);
        }
        .bc-step b { color:#1565C0; }
        .bc-tag {
            display:inline-block; background:#0B3D91; color:#fff; border-radius:6px;
            padding:2px 10px; font-size:.72rem; font-weight:700; margin-right:8px;
        }
        .good { color:#1B7F3B; font-weight:700; }
        .bad  { color:#C62828; font-weight:700; }
        .muted{ color:#5A6472; }
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
        <span class="bc-tag">PART 0 · FOUNDATIONS</span>
        <h1>0.1 · What is a Business Case?</h1>
        <p>The foundation of every sound investment decision — why we build one,
        what goes inside it, and the 7-step process from idea to approval.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Understand what a business case is, when it's needed, "
           "and the structured process used to evaluate any investment before committing capital.")

# ----------------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------------
tab_theory, tab_example, tab_lab, tab_quiz = st.tabs(
    ["📘  Theory", "🧮  Worked Example", "🎛️  Interactive Lab", "✅  Quiz"]
)

# ============================================================================
# TAB 1 — THEORY
# ============================================================================
with tab_theory:
    st.subheader("1 · Definition")
    st.markdown(
        """
        <div class="bc-key">
        A <b>Business Case</b> is a structured, evidence-based document that justifies a proposed
        investment by comparing the <b>expected benefits (cash inflows / savings)</b> against the
        <b>expected costs (cash outflows)</b> over the life of the project — and translates them
        into financial metrics that support a clear <b>invest / don't-invest</b> decision.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "> In short: it answers **“Should we spend this money, and why?”** — with numbers, "
        "assumptions, risks, and a recommendation that a decision-maker can trust."
    )

    st.subheader("2 · Why We Prepare a Business Case")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>✅ It helps you…</h4>
            <ul>
              <li>Compare the <b>value created</b> vs the <b>capital committed</b></li>
              <li>Rank competing projects when the budget is limited</li>
              <li>Make assumptions <b>explicit and challengeable</b></li>
              <li>Expose <b>risks</b> before money is spent</li>
              <li>Create <b>accountability</b> and a baseline to track delivery</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>❌ Without one, you risk…</h4>
            <ul>
              <li>Emotion- or politics-driven decisions</li>
              <li>Over-optimistic benefits that never materialise</li>
              <li>Ignoring the <b>time value of money</b></li>
              <li>Hidden costs surfacing after commitment</li>
              <li>No way to hold anyone accountable for the outcome</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    st.subheader("3 · The Core Logic: Inflows vs Outflows")
    st.markdown(
        "Every business case reduces to one question — do the **inflows** (savings or income the "
        "investment generates) outweigh the **outflows** (the money we spend), once we account for "
        "**timing and risk**?"
    )
    st.latex(r"\text{Net Benefit} = \sum \text{Cash Inflows} - \sum \text{Cash Outflows}")
    st.markdown(
        "<span class='muted'>We'll refine this in later pages by <b>discounting</b> those cash flows "
        "to today's value (NPV, IRR, PI, etc.). For now, hold the intuition: value = benefits minus costs, "
        "adjusted for <i>when</i> they occur and <i>how certain</i> they are.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("4 · The 7-Step Business Case Process")
    steps = [
        ("1️⃣ Define the problem / opportunity",
         "State the business need clearly — a cost to reduce, capacity to add, risk to remove, or revenue to capture."),
        ("2️⃣ Identify options",
         "List realistic alternatives, always including the <b>“Do Nothing / Base Case”</b> to serve as the comparison baseline."),
        ("3️⃣ Estimate cash flows",
         "Quantify all <b>incremental</b> inflows (savings, extra revenue) and outflows (capex, opex, working capital) — year by year."),
        ("4️⃣ Choose the discount rate",
         "Select the hurdle rate / WACC that reflects the cost of capital and the project's risk."),
        ("5️⃣ Apply appraisal methods",
         "Run Payback, ARR, <b>NPV, IRR, PI</b> and risk analysis to score each option."),
        ("6️⃣ Assess risk & qualitative factors",
         "Add sensitivity/scenario analysis plus strategic fit, ESG, legal and operational considerations."),
        ("7️⃣ Recommend & decide",
         "Compare options, apply decision rules, and present a clear, defensible recommendation for approval."),
    ]
    for title, body in steps:
        st.markdown(f"<div class='bc-step'><b>{title}</b><br>{body}</div>", unsafe_allow_html=True)

    st.subheader("5 · When is a Business Case Needed?")
    st.markdown(
        """
        - **Capital expenditure (Capex)** — machinery, plant, buildings, IT systems
        - **Cost-savings / efficiency projects** — automation, energy, headcount productivity
        - **New products, markets, or capacity expansions**
        - **Make-vs-buy / outsourcing** and **replacement** decisions
        - **Transformation & digitalisation** programmes
        - Any decision where **significant money is committed today** for **future returns**
        """
    )

    st.subheader("6 · Anatomy of a Good Business Case")
    anatomy = pd.DataFrame(
        {
            "Section": ["Executive Summary", "Problem / Opportunity", "Options Considered",
                        "Financial Analysis", "Risk Assessment", "Assumptions",
                        "Recommendation", "Implementation Plan"],
            "What it contains": [
                "One-page summary of the ask, the numbers, and the recommendation",
                "The business need and its cost of inaction",
                "Alternatives evaluated, including 'Do Nothing'",
                "Cash flows + NPV / IRR / Payback / PI results",
                "Key risks, sensitivities, and mitigations",
                "Explicit, challengeable inputs behind the numbers",
                "Clear invest / don't-invest decision with rationale",
                "Timeline, owners, milestones, and how benefits are tracked",
            ],
        }
    )
    st.table(anatomy)

    with st.expander("🔑 Key terms you'll meet in this section"):
        st.markdown(
            """
            - **Incremental cash flow** — only the cash flows that *change because of* the decision.
            - **Sunk cost** — already spent; **ignore** it in the decision.
            - **Opportunity cost** — value of the next-best alternative given up; **include** it.
            - **Discount rate / WACC** — the rate used to convert future cash to today's value.
            - **Hurdle rate** — the minimum acceptable return for a project to be approved.
            - **Terminal value** — value of the project/asset at the end of the analysis horizon.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 A Simple Business Case — Automating a Packing Line")

    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> A factory is considering installing a semi-automated packing unit.
        It costs <b>€500,000</b> today (Year 0) and is expected to generate
        <b>€160,000</b> of annual net savings (labour + wastage) for <b>5 years</b>.
        We'll walk through the business-case logic — <i>without</i> discounting yet
        (that comes in Part 2).
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Step 1–3 · Lay out the incremental cash flows")
    years = [0, 1, 2, 3, 4, 5]
    outflow = [-500_000, 0, 0, 0, 0, 0]
    inflow = [0, 160_000, 160_000, 160_000, 160_000, 160_000]
    net = [o + i for o, i in zip(outflow, inflow)]
    cumulative = pd.Series(net).cumsum().tolist()

    df = pd.DataFrame(
        {
            "Year": years,
            "Outflow (€)": outflow,
            "Inflow (€)": inflow,
            "Net Cash Flow (€)": net,
            "Cumulative (€)": cumulative,
        }
    )
    st.dataframe(
        df.style.format({c: "{:,.0f}" for c in df.columns if c != "Year"}),
        use_container_width=True, hide_index=True,
    )

    st.markdown("#### Step 5 · Apply a basic method — Payback Period")
    st.latex(r"\text{Payback} = \frac{\text{Initial Investment}}{\text{Annual Net Inflow}} "
             r"= \frac{500{,}000}{160{,}000} \approx 3.13 \text{ years}")

    total_net = sum(net)
    st.markdown(
        f"""
        - **Total undiscounted net benefit** over 5 years = **€{total_net:,.0f}**
        - **Payback** ≈ **3.13 years** (the project recovers its cost partway through Year 4)
        - Cumulative cash flow turns **positive** in Year 4 — see the chart below.
        """
    )

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=net, name="Net cash flow",
                         marker_color=["#C62828"] + ["#1E88E5"] * 5))
    fig.add_trace(go.Scatter(x=years, y=cumulative, name="Cumulative",
                             mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="grey")
    fig.update_layout(
        title="Cash flow profile — packing line automation",
        xaxis_title="Year", yaxis_title="€", height=420,
        legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Step 6–7 · Interpret & recommend")
    st.success(
        "**Interpretation:** With €300k of undiscounted net gain and a ~3.1-year payback on a "
        "5-year asset, the project looks attractive on a basic screen. **But** — this ignores the "
        "time value of money and risk. In Part 2 we'll discount these flows to compute **NPV** and "
        "**IRR**, which give a far more robust recommendation."
    )
    st.info("👉 Notice how the *same cash flows* will be reused as we layer on more advanced "
            "methods throughout this section.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Build Your Own Mini Business Case")
    st.markdown("Change the inputs and watch the cash-flow profile, total net benefit, and simple "
                "payback update instantly.")

    c1, c2, c3 = st.columns(3)
    with c1:
        invest = st.number_input("Initial investment — Year 0 outflow (€)",
                                  min_value=0, value=500_000, step=25_000)
    with c2:
        annual_inflow = st.number_input("Annual net inflow / savings (€)",
                                        min_value=0, value=160_000, step=10_000)
    with c3:
        life = st.slider("Project life (years)", 1, 15, 5)

    c4, c5 = st.columns(2)
    with c4:
        annual_opex = st.number_input("Recurring annual outflow / opex (€)",
                                      min_value=0, value=0, step=5_000)
    with c5:
        growth = st.slider("Annual growth in net inflow (%)", -20, 30, 0) / 100.0

    # Build cash flows
    yrs = list(range(0, life + 1))
    cf_out, cf_in, cf_net = [], [], []
    for y in yrs:
        if y == 0:
            cf_out.append(-invest)
            cf_in.append(0)
            cf_net.append(-invest)
        else:
            infl = annual_inflow * ((1 + growth) ** (y - 1))
            out = -annual_opex
            cf_out.append(out)
            cf_in.append(infl)
            cf_net.append(infl + out)

    cum = pd.Series(cf_net).cumsum().tolist()
    total_net = sum(cf_net)

    # Simple payback (period where cumulative crosses 0)
    payback = None
    for i in range(1, len(cum)):
        if cum[i - 1] < 0 <= cum[i]:
            frac = -cum[i - 1] / (cum[i] - cum[i - 1]) if (cum[i] - cum[i - 1]) != 0 else 0
            payback = (i - 1) + frac
            break

    lab_df = pd.DataFrame(
        {
            "Year": yrs,
            "Outflow (€)": cf_out,
            "Inflow (€)": cf_in,
            "Net (€)": cf_net,
            "Cumulative (€)": cum,
        }
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("Total net benefit (undiscounted)", f"€{total_net:,.0f}")
    m2.metric("Simple payback",
              f"{payback:.2f} yrs" if payback is not None else "Not recovered")
    roi = (total_net / invest * 100) if invest else 0
    m3.metric("Simple ROI over life", f"{roi:,.0f}%")

    st.dataframe(
        lab_df.style.format({c: "{:,.0f}" for c in lab_df.columns if c != "Year"}),
        use_container_width=True, hide_index=True,
    )

    figl = go.Figure()
    figl.add_trace(go.Bar(x=yrs, y=cf_net, name="Net cash flow",
                          marker_color=["#C62828"] + ["#1E88E5"] * life))
    figl.add_trace(go.Scatter(x=yrs, y=cum, name="Cumulative",
                              mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    figl.add_hline(y=0, line_dash="dash", line_color="grey")
    figl.update_layout(xaxis_title="Year", yaxis_title="€", height=420,
                       legend=dict(orientation="h", y=1.12), margin=dict(t=50, b=40))
    st.plotly_chart(figl, use_container_width=True)

    if payback is None:
        st.error("⚠️ At these inputs the investment is **never recovered** within its life — "
                 "the business case fails even the simplest screen.")
    elif total_net > 0:
        st.success(f"✅ Positive net benefit of **€{total_net:,.0f}** with payback in "
                   f"**{payback:.2f} years**. Worth taking to the discounted-cash-flow stage (NPV/IRR).")
    else:
        st.warning("🟠 The project recovers its cost eventually but total net benefit is not "
                   "positive — challenge the assumptions before proceeding.")

    st.caption("Reminder: this lab uses **undiscounted** cash flows for intuition. "
               "The NPV / IRR pages in Part 2 add the time value of money.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 5 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. What is the primary purpose of a business case?",
            "options": [
                "To justify an investment by comparing expected benefits against costs",
                "To record the company's historical financial statements",
                "To calculate the monthly payroll",
                "To replace the annual audit",
            ],
            "answer": 0,
            "why": "A business case justifies an investment by weighing expected inflows (benefits/savings) "
                   "against outflows (costs) to support a decision.",
        },
        {
            "q": "2. Which option should ALWAYS be included when identifying alternatives?",
            "options": [
                "The most expensive option",
                "The 'Do Nothing / Base Case' option",
                "A competitor's strategy",
                "The option preferred by the CEO",
            ],
            "answer": 1,
            "why": "The 'Do Nothing' base case is the essential benchmark against which every "
                   "other option's incremental value is measured.",
        },
        {
            "q": "3. A cost that has already been incurred and cannot be recovered is a…",
            "options": ["Opportunity cost", "Incremental cost", "Sunk cost", "Terminal cost"],
            "answer": 2,
            "why": "A sunk cost is already spent and cannot be recovered, so it must be IGNORED "
                   "in the investment decision.",
        },
        {
            "q": "4. In the 7-step process, choosing the discount rate comes BEFORE…",
            "options": [
                "Defining the problem",
                "Identifying options",
                "Applying appraisal methods such as NPV",
                "Estimating the cash flows",
            ],
            "answer": 2,
            "why": "You must pick the discount rate (Step 4) before you can apply discounted methods "
                   "like NPV/IRR (Step 5).",
        },
        {
            "q": "5. Which cash flows are relevant to a business case?",
            "options": [
                "All historical company cash flows",
                "Only the incremental cash flows that change because of the decision",
                "Only cash inflows, never outflows",
                "Sunk costs and incremental flows combined",
            ],
            "answer": 1,
            "why": "Only INCREMENTAL cash flows — those that change as a direct result of the "
                   "decision — belong in the analysis.",
        },
    ]

    with st.form("quiz_0_1"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q01_{i}")
            responses.append(choice)
            st.markdown("<hr style='margin:6px 0;'>", unsafe_allow_html=True)
        submitted = st.form_submit_button("📊 Submit answers")

    if submitted:
        score = 0
        for i, item in enumerate(questions):
            chosen = responses[i]
            correct_text = item["options"][item["answer"]]
            if chosen == correct_text:
                score += 1
                st.success(f"**Q{i+1}: Correct ✅** — {item['why']}")
            else:
                st.error(
                    f"**Q{i+1}: Not quite ❌** — Correct answer: *{correct_text}*.\n\n{item['why']}"
                )
        pct = score / len(questions) * 100
        st.markdown("---")
        st.metric("Your score", f"{score} / {len(questions)}", f"{pct:.0f}%")
        if pct == 100:
            st.balloons()
            st.success("🏆 Perfect! You've mastered the fundamentals of a business case.")
        elif pct >= 60:
            st.info("👍 Good work — review the explanations above, then move on to "
                    "**0.2 · Cash Flows: Inflows & Outflows**.")
        else:
            st.warning("📖 Revisit the **Theory** tab and try again — the foundations here "
                       "matter for every later page.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Section Overview** · *Business Case*")
with cnext:
    st.markdown("**Next:** `0.2 · Cash Flows: Inflows & Outflows` ➡️")
st.caption("Business Case section · Page 0.1 · Built with Streamlit")
