# ============================================================================
#  BUSINESS CASE — Section
#  Page 4.3 · Qualitative Factors & Governance
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="4.3 · Qualitative Factors & Governance",
    page_icon="🏛️",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Parts 0–4)
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
        <span class="bc-tag">PART 4 · DECISION-MAKING FRAMEWORK</span>
        <h1>4.3 · Qualitative Factors &amp; Governance</h1>
        <p>The numbers rarely decide alone. Strategic fit, ESG, risk and stakeholder
        impact — plus the approval governance that turns a business case into a decision.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Weigh non-financial factors systematically, understand capital "
           "governance and approval workflows, and combine qualitative and quantitative evidence.")

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
    st.subheader("1 · Why Numbers Aren't Enough")
    st.markdown(
        """
        <div class="bc-key">
        A positive NPV is <b>necessary but not always sufficient</b>. Two projects with similar NPVs
        can differ hugely in <b>strategic value, risk, and stakeholder impact</b>. Qualitative factors
        capture what the financial model can't easily quantify — and sometimes they <b>override</b> the
        numbers entirely (for compliance, safety, or strategy).
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · The Key Qualitative Factors")
    for t, b in [
        ("🎯 Strategic fit",
         "Does the project support the company's long-term strategy, core capabilities and competitive "
         "position? A high-NPV project that pulls you off-strategy may still be wrong."),
        ("🌍 ESG & sustainability",
         "Environmental impact, carbon footprint, social license to operate, and governance standards. "
         "Increasingly board-critical and sometimes regulated."),
        ("⚠️ Risk & resilience",
         "Operational, technological, supply-chain, reputational and regulatory risk beyond what the "
         "cash-flow model captures."),
        ("👥 Stakeholder impact",
         "Effects on employees, customers, communities, unions, regulators and partners — and the "
         "relationships that sustain the business."),
        ("⚖️ Legal & compliance",
         "Some investments are mandatory (safety, environmental, legal). NPV may be negative but the "
         "project is non-negotiable — a 'licence to operate' spend."),
        ("🔗 Interdependency & flexibility",
         "Does it enable or block other projects? Does it create future options (see real options, 3.4)?"),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("3 · Weighted Scoring — Making Qualitative Rigorous")
    st.markdown(
        """
        Qualitative doesn't mean *arbitrary*. A **weighted scoring model** brings discipline:
        assign a **weight** to each factor (importance), **score** each option against each factor,
        and compute a weighted total.
        """
    )
    st.latex(r"\text{Weighted Score} = \sum_{i} w_i \times s_i \qquad \text{where} \quad \sum_i w_i = 1")
    st.markdown(
        "<span class='muted'>Where $w_i$ is the weight of factor $i$ and $s_i$ its score (e.g. 1–5). "
        "This makes trade-offs explicit and challengeable — the hallmark of a good business case.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("4 · Combining Qualitative & Quantitative")
    st.markdown(
        """
        Two common approaches:
        - **Two-lens view (recommended):** Present financials (NPV/IRR) and a qualitative scorecard
          *side by side*, letting decision-makers weigh both. Transparent and hard to game.
        - **Blended score:** Combine a normalised financial score with the qualitative score using
          agreed weights into a single index. Convenient, but can hide the underlying trade-offs.
        """
    )

    st.markdown("---")
    st.subheader("PART B · Capital Governance")

    st.subheader("5 · What Governance Provides")
    st.markdown(
        """
        **Capital governance** is the framework of policies, authority levels and controls that ensures
        capital is committed **wisely, consistently and accountably**. It typically covers:
        - **Authorisation limits** — who can approve what value (delegation of authority)
        - **Standardised business-case templates** and appraisal methods
        - **Independent review / challenge** (finance, risk, technical)
        - **Post-investment audit** — did the project deliver the promised benefits?
        """
    )

    st.subheader("6 · A Typical Approval Workflow")
    workflow = pd.DataFrame(
        {
            "Stage": ["1 · Idea / concept", "2 · Business case prepared", "3 · Financial review",
                      "4 · Approval (by authority level)", "5 · Execution", "6 · Post-investment audit"],
            "Owner": ["Sponsor", "Project team + Finance", "Finance / Controllers",
                      "Manager / CFO / Board (by value)", "Project team", "Finance / Internal audit"],
            "Key question": ["Is there a real need?", "Do benefits exceed costs?",
                             "Are assumptions & numbers sound?", "Is it approved to proceed?",
                             "Is it delivered on time & budget?", "Did it deliver the benefits?"],
        }
    )
    st.table(workflow)

    st.subheader("7 · Delegation of Authority (Illustrative)")
    doa = pd.DataFrame(
        {
            "Investment size": ["< €50k", "€50k – €250k", "€250k – €1m", "€1m – €5m", "> €5m"],
            "Approval authority": ["Department Manager", "Site / Factory Head",
                                   "Divisional Director", "CFO", "Board of Directors"],
        }
    )
    st.table(doa)
    st.info("👉 Higher value and higher risk push approval **up** the authority ladder. Always check "
            "your own organisation's Delegation of Authority (DoA) matrix.")

    st.subheader("8 · Post-Investment Review — Closing the Loop")
    st.markdown(
        """
        The most **overlooked** governance step. Comparing actual outcomes to the business-case
        promises:
        - Improves the **realism** of future forecasts (reduces optimism bias)
        - Creates **accountability** for benefit delivery
        - Surfaces lessons on estimation, execution and risk
        """
    )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - A positive NPV is **necessary but not always sufficient** — qualitative factors matter.
            - Key factors: **strategic fit, ESG, risk, stakeholders, legal/compliance, flexibility**.
            - Use a **weighted scoring model** to make qualitative assessment rigorous and transparent.
            - **Governance** = authorisation limits, standardised templates, independent challenge, and
              **post-investment audit**.
            - Approval authority rises with **value and risk**; always close the loop with a review.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Two-Lens Decision — Numbers + Qualitative Scorecard")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> Two projects have <b>similar NPVs</b>, so the financials alone don't separate them.
        We build a <b>weighted qualitative scorecard</b> (factors scored 1–5) to inform the choice.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Financial lens")
    fin = pd.DataFrame(
        {
            "Project": ["Automation upgrade", "New product line"],
            "NPV (€)": [420_000, 445_000],
            "IRR (%)": [17.5, 16.2],
            "Payback (yrs)": [3.4, 3.9],
        }
    )
    st.dataframe(
        fin.style.format({"NPV (€)": "{:,.0f}", "IRR (%)": "{:.1f}%", "Payback (yrs)": "{:.1f}"}),
        use_container_width=True, hide_index=True,
    )
    st.caption("Financially near-identical — the qualitative lens will be decisive.")

    st.markdown("#### Qualitative lens — weighted scorecard (scores 1–5)")
    factors = ["Strategic fit", "ESG impact", "Risk (lower = better score)",
               "Stakeholder support", "Future flexibility"]
    weights = [0.30, 0.15, 0.25, 0.15, 0.15]
    score_A = [5, 3, 4, 4, 5]   # Automation upgrade
    score_B = [3, 4, 3, 3, 3]   # New product line

    wa = sum(w * s for w, s in zip(weights, score_A))
    wb = sum(w * s for w, s in zip(weights, score_B))

    sc = pd.DataFrame(
        {
            "Factor": factors,
            "Weight": weights,
            "Automation (score)": score_A,
            "New line (score)": score_B,
            "Automation (weighted)": [w * s for w, s in zip(weights, score_A)],
            "New line (weighted)": [w * s for w, s in zip(weights, score_B)],
        }
    )
    st.dataframe(
        sc.style.format({"Weight": "{:.0%}", "Automation (weighted)": "{:.2f}",
                         "New line (weighted)": "{:.2f}"}),
        use_container_width=True, hide_index=True,
    )

    m1, m2 = st.columns(2)
    m1.metric("Automation weighted score", f"{wa:.2f} / 5")
    m2.metric("New line weighted score", f"{wb:.2f} / 5")

    # radar chart
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=score_A + [score_A[0]], theta=factors + [factors[0]],
                                  fill="toself", name="Automation upgrade",
                                  line_color="#1565C0"))
    fig.add_trace(go.Scatterpolar(r=score_B + [score_B[0]], theta=factors + [factors[0]],
                                  fill="toself", name="New product line",
                                  line_color="#F9A825"))
    fig.update_layout(title="Qualitative profile comparison",
                      polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                      height=460, legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    winner = "Automation upgrade" if wa > wb else "New product line"
    st.success(f"✅ Despite near-identical NPVs, the **{winner}** wins on the weighted qualitative "
               f"score ({max(wa, wb):.2f} vs {min(wa, wb):.2f}) — driven mainly by stronger strategic "
               f"fit and lower risk. The two-lens view makes the trade-off transparent for the board.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Lab A · Weighted Qualitative Scorecard")
    st.markdown("Define your factors and weights, score two options (1–5), and see the weighted result "
                "and radar profile. Weights are auto-normalised to sum to 100%.")

    default = pd.DataFrame(
        {
            "Factor": ["Strategic fit", "ESG impact", "Risk profile", "Stakeholder support",
                       "Future flexibility"],
            "Weight (%)": [30, 15, 25, 15, 15],
            "Option A score (1-5)": [5, 3, 4, 4, 5],
            "Option B score (1-5)": [3, 4, 3, 3, 3],
        }
    )
    ed = st.data_editor(default, use_container_width=True, hide_index=True,
                        num_rows="dynamic", key="qual_editor")

    ca, cb = st.columns(2)
    with ca:
        name_a = st.text_input("Option A name", value="Automation upgrade")
    with cb:
        name_b = st.text_input("Option B name", value="New product line")

    ed = ed.copy()
    ed = ed[ed["Weight (%)"].notna() & (ed["Weight (%)"] > 0)]
    w_sum = ed["Weight (%)"].sum()
    if w_sum == 0:
        st.warning("Add at least one factor with a positive weight.")
    else:
        norm_w = ed["Weight (%)"] / w_sum
        ed["Weighted A"] = norm_w * ed["Option A score (1-5)"]
        ed["Weighted B"] = norm_w * ed["Option B score (1-5)"]
        wa = ed["Weighted A"].sum()
        wb = ed["Weighted B"].sum()

        if abs(w_sum - 100) > 0.01:
            st.caption(f"ℹ️ Weights sum to {w_sum:.0f}% — auto-normalised to 100%.")

        st.dataframe(
            ed.style.format({"Weight (%)": "{:.0f}%", "Weighted A": "{:.2f}", "Weighted B": "{:.2f}"}),
            use_container_width=True, hide_index=True,
        )

        m1, m2 = st.columns(2)
        m1.metric(f"{name_a} score", f"{wa:.2f} / 5")
        m2.metric(f"{name_b} score", f"{wb:.2f} / 5")

        factors = ed["Factor"].tolist()
        sA = ed["Option A score (1-5)"].tolist()
        sB = ed["Option B score (1-5)"].tolist()
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=sA + [sA[0]], theta=factors + [factors[0]],
                                      fill="toself", name=name_a, line_color="#1565C0"))
        fig.add_trace(go.Scatterpolar(r=sB + [sB[0]], theta=factors + [factors[0]],
                                      fill="toself", name=name_b, line_color="#F9A825"))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                          height=440, legend=dict(orientation="h", y=1.12), margin=dict(t=40, b=40))
        st.plotly_chart(fig, use_container_width=True)

        if abs(wa - wb) < 0.05:
            st.info(f"🤝 Very close on qualitative grounds ({wa:.2f} vs {wb:.2f}) — let the financials "
                    f"and risk appetite decide.")
        else:
            win = name_a if wa > wb else name_b
            st.success(f"✅ **{win}** leads on the weighted qualitative score "
                       f"({max(wa, wb):.2f} vs {min(wa, wb):.2f}).")

    st.markdown("---")
    st.subheader("🎛️ Lab B · Approval Authority Checker")
    st.markdown("Enter an investment value and risk level to see who should approve it under an "
                "illustrative Delegation of Authority (DoA) matrix.")

    c1, c2 = st.columns(2)
    with c1:
        value = st.number_input("Investment value (€)", min_value=0, value=750_000, step=50_000)
    with c2:
        risk = st.select_slider("Risk level", options=["Low", "Medium", "High"], value="Medium")

    # base authority by value
    if value < 50_000:
        base_level, base_auth = 1, "Department Manager"
    elif value < 250_000:
        base_level, base_auth = 2, "Site / Factory Head"
    elif value < 1_000_000:
        base_level, base_auth = 3, "Divisional Director"
    elif value < 5_000_000:
        base_level, base_auth = 4, "CFO"
    else:
        base_level, base_auth = 5, "Board of Directors"

    # risk escalation
    escalation = {"Low": 0, "Medium": 0, "High": 1}[risk]
    ladder = {1: "Department Manager", 2: "Site / Factory Head", 3: "Divisional Director",
              4: "CFO", 5: "Board of Directors"}
    final_level = min(base_level + escalation, 5)
    final_auth = ladder[final_level]

    m1, m2, m3 = st.columns(3)
    m1.metric("Value-based authority", base_auth)
    m2.metric("Risk adjustment", f"+{escalation} level" if escalation else "None")
    m3.metric("Required approver", final_auth)

    if escalation and final_auth != base_auth:
        st.warning(f"🟠 Because risk is **{risk}**, approval escalates from **{base_auth}** to "
                   f"**{final_auth}**.")
    else:
        st.success(f"✅ This investment should be approved by the **{final_auth}** under the "
                   f"illustrative DoA matrix.")

    st.caption("Note: this is an illustrative matrix — always apply your own organisation's DoA policy.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. A positive NPV is…",
            "options": [
                "Always sufficient to approve a project",
                "Necessary but not always sufficient — qualitative factors also matter",
                "Irrelevant if strategy is good",
                "The only thing that matters",
            ],
            "answer": 1,
            "why": "A positive NPV is necessary but qualitative factors (strategy, risk, ESG, compliance) can still be decisive.",
        },
        {
            "q": "2. Which of these is a qualitative factor in a business case?",
            "options": ["Internal Rate of Return", "Strategic fit",
                        "Discounted payback", "Net Present Value"],
            "answer": 1,
            "why": "Strategic fit is qualitative; the others are quantitative financial metrics.",
        },
        {
            "q": "3. A weighted scoring model makes qualitative assessment rigorous by…",
            "options": [
                "Ignoring less important factors",
                "Assigning weights and scores so trade-offs are explicit",
                "Using only financial data",
                "Removing all subjectivity",
            ],
            "answer": 1,
            "why": "It multiplies each factor's weight by its score, making trade-offs explicit and challengeable.",
        },
        {
            "q": "4. A project mandated by safety or environmental law may proceed even if…",
            "options": ["Its NPV is negative", "Its IRR is very high",
                        "It has a short payback", "It has strong ESG credentials"],
            "answer": 0,
            "why": "Compliance/'licence to operate' spend can be non-negotiable regardless of a negative NPV.",
        },
        {
            "q": "5. In a typical Delegation of Authority matrix, approval authority rises with…",
            "options": [
                "Lower investment value",
                "Higher investment value and risk",
                "Shorter project duration",
                "The number of team members",
            ],
            "answer": 1,
            "why": "Larger, riskier investments require approval higher up the authority ladder.",
        },
        {
            "q": "6. The post-investment review (audit) primarily helps to…",
            "options": [
                "Speed up execution",
                "Compare actual outcomes to promises, improving accountability and future forecasts",
                "Replace the business case",
                "Eliminate the need for governance",
            ],
            "answer": 1,
            "why": "Post-investment review closes the loop — checking delivered benefits and reducing optimism bias.",
        },
    ]

    with st.form("quiz_4_3"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q43_{i}")
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
            st.success("🏆 Perfect! You've mastered qualitative appraisal & governance — and completed Part 4!")
        elif pct >= 60:
            st.info("👍 Good work — next is Part 5, the **End-to-End Case Builder**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on weighted scoring and the approval workflow.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `4.2 · Mutually Exclusive Projects & Capital Rationing`")
with cnext:
    st.markdown("**Next:** `5.1 · End-to-End Case Builder` ➡️")
st.caption("Business Case section · Page 4.3 · Built with Streamlit")
