# ============================================================================
#  BUSINESS CASE — Section
#  Page 2.4 · Profitability Index (PI)
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="2.4 · Profitability Index (PI)",
    page_icon="📊",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Parts 0–2)
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
        <span class="bc-tag">PART 2 · DISCOUNTED (CORE) METHODS</span>
        <h1>2.4 · Profitability Index (PI)</h1>
        <p>Value created per euro invested — the efficiency ratio that turns NPV into
        the perfect tool for ranking projects when capital is scarce.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Compute the profitability index, apply its decision rule, relate it to "
           "NPV, and use it to rank projects under capital rationing.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def pv_inflows(rate, inflows):
    """PV of a list of inflows starting in Year 1."""
    return sum(cf / (1 + rate) ** (t + 1) for t, cf in enumerate(inflows))


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
        The <b>Profitability Index (PI)</b> — also called the <b>Benefit-Cost Ratio</b> — measures the
        <b>present value of a project's future cash inflows per euro of initial investment</b>. Where
        NPV gives an absolute value, PI gives a <b>relative efficiency ratio</b>, making it ideal for
        comparing projects of different sizes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · The Formula")
    st.latex(r"PI = \frac{\text{PV of future cash inflows}}{\text{Initial Investment}}")
    st.markdown("An equivalent and very useful form linking PI directly to NPV:")
    st.latex(r"PI = 1 + \frac{NPV}{\text{Initial Investment}}")
    st.markdown(
        "<span class='muted'>This second form makes the connection obvious: whenever NPV is positive, "
        "PI is greater than 1.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("3 · The Decision Rule")
    st.markdown(
        """
        <div class="bc-card">
        <h4>📏 Accept / Reject</h4>
        <ul>
          <li><span class="good">PI &gt; 1</span> → <b>Accept.</b> Each euro invested returns more than
          a euro in present-value terms (equivalent to NPV &gt; 0).</li>
          <li><span class="bad">PI &lt; 1</span> → <b>Reject.</b> Value is destroyed (NPV &lt; 0).</li>
          <li><b>PI = 1</b> → Break-even; NPV = 0.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("4 · PI and NPV Always Agree on Accept/Reject")
    agree = pd.DataFrame(
        {
            "Situation": ["Value created", "Break-even", "Value destroyed"],
            "NPV": ["> 0", "= 0", "< 0"],
            "PI": ["> 1", "= 1", "< 1"],
            "Decision": ["Accept", "Indifferent", "Reject"],
        }
    )
    st.table(agree)
    st.info("👉 For a **single** accept/reject decision, PI and NPV never disagree. The difference "
            "appears when you must **rank** projects under a limited budget.")

    st.subheader("5 · Why PI Shines Under Capital Rationing")
    st.markdown(
        """
        When capital is **limited**, you can't fund every positive-NPV project — you must choose the
        combination that creates the **most value per scarce euro**. Because PI measures *value per
        euro invested*, ranking projects by PI (highest first) generally maximises total NPV within
        the budget.
        """
    )
    for t, b in [
        ("💰 Scarce capital → efficiency matters",
         "A €1m project adding €200k NPV (PI 1.20) may beat a €5m project adding €400k NPV (PI 1.08) "
         "if the budget is tight — the smaller one is more efficient per euro."),
        ("📋 Rank, then fill the budget",
         "Order candidate projects by PI, then select down the list until the capital budget is used up."),
        ("⚠️ Watch for indivisibility",
         "PI ranking assumes projects are divisible or combine neatly. With lumpy, indivisible projects "
         "you may need to test combinations for the highest total NPV."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("6 · Strengths & Weaknesses")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👍 Strengths</h4>
            <ul>
              <li>Great for <b>ranking</b> under capital rationing</li>
              <li>Accounts for the <b>time value of money</b> (built on PV)</li>
              <li>Normalises for <b>project size</b> — compares like with like</li>
              <li>Consistent with NPV on accept/reject</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👎 Weaknesses</h4>
            <ul>
              <li>A <b>ratio</b>, not an absolute — can favour small projects over larger value creators</li>
              <li>Can <b>mislead for mutually exclusive</b> projects of different scale (use NPV)</li>
              <li>Sensitive to how the <b>initial investment</b> is defined</li>
              <li>Struggles with <b>multi-period</b> capital outlays</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - PI = PV of inflows ÷ initial investment = **1 + NPV/Investment**.
            - Decision rule: **accept if PI > 1** (identical to NPV > 0).
            - PI is the go-to tool for **ranking under capital rationing**.
            - For **mutually exclusive** projects of different size, prefer **NPV**.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Example A · Computing PI for One Project")
    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> A project costs <b>€500,000</b> and returns <b>€160,000</b> per year for
        <b>5 years</b>, discounted at <b>10%</b>. What is its PI?
        </div>
        """,
        unsafe_allow_html=True,
    )

    r = 0.10
    invest = 500_000
    inflows = [160_000] * 5
    pv_in = pv_inflows(r, inflows)
    npv_val = pv_in - invest
    pi = pv_in / invest

    st.latex(rf"PV_{{inflows}} = €{pv_in:,.0f}, \quad NPV = {pv_in:,.0f} - 500{{,}}000 = €{npv_val:,.0f}")
    st.latex(rf"PI = \frac{{{pv_in:,.0f}}}{{500{{,}}000}} = {pi:.3f} \quad\Longleftrightarrow\quad "
             rf"1 + \frac{{{npv_val:,.0f}}}{{500{{,}}000}} = {pi:.3f}")
    st.success(f"✅ **PI = {pi:.3f} > 1 → ACCEPT.** Every €1 invested generates €{pi:.2f} of "
               f"present-value inflows — i.e. €{pi-1:.2f} of net value per euro.")

    st.markdown("---")
    st.subheader("🧮 Example B · Ranking Under Capital Rationing")
    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> Four independent projects compete for a <b>€1,000,000</b> capital budget.
        All have positive NPVs — but we can't fund them all. Rank by PI to maximise value.
        </div>
        """,
        unsafe_allow_html=True,
    )

    projects = pd.DataFrame(
        {
            "Project": ["A", "B", "C", "D"],
            "Investment (€)": [500_000, 300_000, 400_000, 200_000],
            "PV of inflows (€)": [650_000, 420_000, 480_000, 260_000],
        }
    )
    projects["NPV (€)"] = projects["PV of inflows (€)"] - projects["Investment (€)"]
    projects["PI"] = projects["PV of inflows (€)"] / projects["Investment (€)"]
    projects_ranked = projects.sort_values("PI", ascending=False).reset_index(drop=True)
    projects_ranked.index = projects_ranked.index + 1

    st.dataframe(
        projects_ranked.style.format({"Investment (€)": "{:,.0f}", "PV of inflows (€)": "{:,.0f}",
                                      "NPV (€)": "{:,.0f}", "PI": "{:.3f}"}),
        use_container_width=True,
    )

    # Greedy selection under €1m
    budget = 1_000_000
    spent, total_npv, chosen = 0, 0, []
    for _, row in projects_ranked.iterrows():
        if spent + row["Investment (€)"] <= budget:
            chosen.append(row["Project"])
            spent += row["Investment (€)"]
            total_npv += row["NPV (€)"]

    st.markdown(f"**Ranking by PI:** {' → '.join(projects_ranked['Project'].tolist())}")
    st.success(f"✅ With a €1,000,000 budget, selecting by highest PI funds **projects "
               f"{', '.join(chosen)}** — using €{spent:,.0f} of capital and delivering a combined "
               f"**NPV of €{total_npv:,.0f}**.")

    fig = go.Figure(go.Bar(
        x=projects_ranked["Project"], y=projects_ranked["PI"],
        marker_color=["#1565C0" if p in chosen else "#BBD3F2" for p in projects_ranked["Project"]],
        text=[f"{v:.2f}" for v in projects_ranked["PI"]], textposition="outside",
    ))
    fig.add_hline(y=1.0, line_dash="dash", line_color="#C62828",
                  annotation_text="PI = 1 (break-even)", annotation_position="top left")
    fig.update_layout(title="Projects ranked by PI (dark = funded within budget)",
                      yaxis_title="Profitability Index", height=420, margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.info("⚠️ Note: PI ranking works best when projects are independent and divisible. For lumpy, "
            "indivisible projects, also test combinations for the highest **total NPV** within budget.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Lab A · Single-Project PI Calculator")
    st.markdown("Set the investment, inflows and rate to see PI and its NPV equivalent.")

    c1, c2, c3 = st.columns(3)
    with c1:
        invest = st.number_input("Initial investment (€)", min_value=1, value=500_000, step=25_000)
    with c2:
        rate = st.slider("Discount rate (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
    with c3:
        n_years = st.slider("Number of years", 1, 12, 5)

    pattern = st.radio("Inflow pattern", ["Even (constant)", "Uneven (edit table)"], horizontal=True)
    if pattern.startswith("Even"):
        annual = st.number_input("Annual inflow (€)", min_value=0, value=160_000, step=10_000)
        inflows = [annual] * n_years
    else:
        default = pd.DataFrame({"Year": list(range(1, n_years + 1)),
                                "Cash Flow (€)": [140000, 150000, 160000, 170000, 180000][:n_years]
                                + [160000] * max(0, n_years - 5)})
        edited = st.data_editor(default, use_container_width=True, hide_index=True,
                                num_rows="fixed", key="pi_editor")
        inflows = edited["Cash Flow (€)"].tolist()

    pv_in = pv_inflows(rate, inflows)
    npv_val = pv_in - invest
    pi = pv_in / invest if invest else 0

    m1, m2, m3 = st.columns(3)
    m1.metric("PV of inflows", f"€{pv_in:,.0f}")
    m2.metric("NPV", f"€{npv_val:,.0f}")
    m3.metric("Profitability Index", f"{pi:.3f}")

    if pi > 1:
        st.success(f"✅ **PI = {pi:.3f} > 1 → ACCEPT.** €{pi:.2f} of present value per €1 invested "
                   f"(€{pi-1:.2f} net value per euro). Equivalent to a positive NPV of €{npv_val:,.0f}.")
    elif pi < 1:
        st.error(f"❌ **PI = {pi:.3f} < 1 → REJECT.** Value destroyed; NPV is €{npv_val:,.0f}.")
    else:
        st.info("PI = 1 — the project exactly breaks even (NPV = 0).")

    st.markdown("---")
    st.subheader("🎛️ Lab B · Capital Rationing Ranker")
    st.markdown("Enter competing projects and a budget. The tool ranks them by PI and selects the "
                "value-maximising set within your budget.")

    budget = st.number_input("Capital budget (€)", min_value=0, value=1_000_000, step=100_000)
    default_p = pd.DataFrame(
        {
            "Project": ["A", "B", "C", "D"],
            "Investment (€)": [500_000, 300_000, 400_000, 200_000],
            "PV of inflows (€)": [650_000, 420_000, 480_000, 260_000],
        }
    )
    proj = st.data_editor(default_p, use_container_width=True, hide_index=True,
                          num_rows="dynamic", key="ration_editor")

    proj = proj.copy()
    proj = proj[proj["Investment (€)"] > 0]
    proj["NPV (€)"] = proj["PV of inflows (€)"] - proj["Investment (€)"]
    proj["PI"] = proj["PV of inflows (€)"] / proj["Investment (€)"]
    proj_ranked = proj.sort_values("PI", ascending=False).reset_index(drop=True)

    spent, total_npv, chosen = 0, 0, []
    for _, row in proj_ranked.iterrows():
        if spent + row["Investment (€)"] <= budget:
            chosen.append(row["Project"])
            spent += row["Investment (€)"]
            total_npv += row["NPV (€)"]
    proj_ranked["Funded?"] = proj_ranked["Project"].apply(lambda p: "✅" if p in chosen else "—")

    st.dataframe(
        proj_ranked.style.format({"Investment (€)": "{:,.0f}", "PV of inflows (€)": "{:,.0f}",
                                  "NPV (€)": "{:,.0f}", "PI": "{:.3f}"}),
        use_container_width=True, hide_index=True,
    )

    k1, k2, k3 = st.columns(3)
    k1.metric("Projects funded", ", ".join(chosen) if chosen else "None")
    k2.metric("Capital used", f"€{spent:,.0f}")
    k3.metric("Total NPV captured", f"€{total_npv:,.0f}")

    if chosen:
        fig = go.Figure(go.Bar(
            x=proj_ranked["Project"], y=proj_ranked["PI"],
            marker_color=["#1565C0" if p in chosen else "#BBD3F2" for p in proj_ranked["Project"]],
            text=[f"{v:.2f}" for v in proj_ranked["PI"]], textposition="outside",
        ))
        fig.add_hline(y=1.0, line_dash="dash", line_color="#C62828")
        fig.update_layout(title="PI ranking (dark = funded)", yaxis_title="PI",
                          height=400, margin=dict(t=60, b=40))
        st.plotly_chart(fig, use_container_width=True)

    st.caption("Reminder: PI ranking assumes divisible/independent projects. For mutually exclusive "
               "choices, decide on **NPV**.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. The Profitability Index is calculated as…",
            "options": [
                "Initial investment ÷ PV of inflows",
                "PV of future inflows ÷ initial investment",
                "NPV ÷ IRR",
                "Total profit ÷ number of years",
            ],
            "answer": 1,
            "why": "PI = present value of future inflows divided by the initial investment.",
        },
        {
            "q": "2. Which equivalent formula links PI to NPV?",
            "options": ["PI = NPV × Investment", "PI = 1 + NPV/Investment",
                        "PI = NPV − Investment", "PI = Investment/NPV"],
            "answer": 1,
            "why": "PI = 1 + NPV/Investment, so PI > 1 exactly when NPV > 0.",
        },
        {
            "q": "3. Under the PI rule, a project is accepted when…",
            "options": ["PI < 1", "PI = 0", "PI > 1", "PI is negative"],
            "answer": 2,
            "why": "PI > 1 means value is created — equivalent to a positive NPV.",
        },
        {
            "q": "4. PI is especially useful for…",
            "options": [
                "Ignoring the time value of money",
                "Ranking projects under capital rationing",
                "Measuring accounting profit",
                "Calculating payback",
            ],
            "answer": 1,
            "why": "PI measures value per euro invested, ideal for ranking when capital is limited.",
        },
        {
            "q": "5. For mutually exclusive projects of very different size, you should generally rely on…",
            "options": ["PI, always", "NPV", "Payback", "ARR"],
            "answer": 1,
            "why": "PI is a ratio and can favour small projects; NPV measures absolute value and is the tie-breaker.",
        },
        {
            "q": "6. A project with PI = 1.00 has an NPV of…",
            "options": ["Greater than zero", "Exactly zero", "Less than zero", "Cannot tell"],
            "answer": 1,
            "why": "PI = 1 corresponds precisely to NPV = 0 — the break-even point.",
        },
    ]

    with st.form("quiz_2_4"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q24_{i}")
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
                st.error(f"**Q{i+1}: Not quite ❌** — Correct answer: *{correct_text}*.\n\n{item['why']}")
        pct = score / len(questions) * 100
        st.markdown("---")
        st.metric("Your score", f"{score} / {len(questions)}", f"{pct:.0f}%")
        if pct == 100:
            st.balloons()
            st.success("🏆 Perfect! You've mastered PI — and completed Part 2 (core discounted methods)!")
        elif pct >= 60:
            st.info("👍 Strong work — next up is Part 3, starting with **3.1 · Sensitivity Analysis**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on the PI–NPV link and capital rationing.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `2.3 · Discounted Payback Period`")
with cnext:
    st.markdown("**Next:** `3.1 · Sensitivity Analysis` ➡️")
st.caption("Business Case section · Page 2.4 · Built with Streamlit")
