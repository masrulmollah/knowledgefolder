# ============================================================================
#  BUSINESS CASE — Section
#  Page 4.2 · Mutually Exclusive Projects & Capital Rationing
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from itertools import combinations

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="4.2 · Mutually Exclusive Projects & Capital Rationing",
    page_icon="⚖️",
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
        <h1>4.2 · Mutually Exclusive Projects &amp; Capital Rationing</h1>
        <p>When you can't do everything — how to choose between competing projects,
        handle unequal lives, and squeeze the most value from a limited capital budget.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Choose correctly between mutually exclusive projects (incl. unequal "
           "lives via EAA) and allocate a constrained budget to maximise total NPV.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def eaa(project_npv, rate, life):
    """Equivalent Annual Annuity of an NPV over 'life' years."""
    if rate == 0:
        return project_npv / life
    annuity_factor = (1 - (1 + rate) ** (-life)) / rate
    return project_npv / annuity_factor


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
    st.subheader("1 · Two Related Problems")
    st.markdown(
        """
        <div class="bc-key">
        Real businesses rarely evaluate one project in isolation. Two situations force a choice:
        <br>• <b>Mutually exclusive projects</b> — you can pick <b>only one</b> from a set (e.g. which
        machine to buy). Accepting one means rejecting the others.
        <br>• <b>Capital rationing</b> — you have <b>more good projects than capital</b>, so you must
        select the best <i>combination</i> within a budget.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.subheader("PART A · Mutually Exclusive Projects")

    st.markdown("#### 2 · The Golden Rule — Choose the Highest NPV")
    st.markdown(
        """
        For mutually exclusive projects, always select the one with the **highest positive NPV** —
        because NPV measures the **absolute value** added to the business. IRR, PI and payback can all
        **mislead** here because they are relative or ignore scale/timing.
        """
    )

    st.markdown("#### 3 · Why IRR Can Mislead")
    for t, b in [
        ("📏 The scale problem",
         "IRR is a percentage, so it ignores size. A 50% return on €10k (€5k) looks better than 20% on "
         "€1m (€200k) — but the larger project adds far more value. NPV gets this right."),
        ("⏳ The timing problem",
         "Projects with different cash-flow timing can rank differently under IRR vs NPV because IRR "
         "assumes reinvestment at the IRR (see page 2.2)."),
        ("🔗 The crossover rate",
         "On an NPV profile of two projects, the discount rate where the two lines cross is the "
         "'crossover rate'. Below it, the rankings differ; above it, they agree. Trust NPV."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.markdown("#### 4 · Unequal Lives — The Equivalent Annual Annuity (EAA)")
    st.markdown(
        """
        Comparing a 3-year project with a 5-year one by raw NPV is **unfair** — the longer project has
        more time to accumulate value. The **Equivalent Annual Annuity (EAA)** converts each project's
        NPV into an equivalent **level annual cash flow**, making them directly comparable:
        """
    )
    st.latex(r"EAA = \frac{NPV}{\text{Annuity factor}} = \frac{NPV}{\dfrac{1 - (1+r)^{-n}}{r}}")
    st.markdown(
        "Choose the project with the **highest EAA**. (Equivalent alternative: the *replacement-chain* "
        "method, which repeats each project to a common horizon.)"
    )

    st.markdown("---")
    st.subheader("PART B · Capital Rationing")

    st.markdown("#### 5 · Hard vs Soft Rationing")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>🧱 Hard rationing</h4>
            <p>Externally imposed — capital markets won't supply more funds (credit limits, loan
            covenants). The constraint is real and binding.</p>
            </div>
            """, unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>🧭 Soft rationing</h4>
            <p>Self-imposed by management (internal budgets, divisional caps) to instil discipline —
            even if funds could technically be raised.</p>
            </div>
            """, unsafe_allow_html=True,
        )

    st.markdown("#### 6 · Divisible vs Indivisible Projects")
    st.markdown(
        """
        - **Divisible** (you can fund a fraction): rank by **Profitability Index** (PI, page 2.4) and
          fund down the list until the budget is exhausted — this maximises total NPV.
        - **Indivisible** (all-or-nothing): PI ranking is only a starting point. You must test feasible
          **combinations** of whole projects to find the set with the **highest total NPV** within budget.
        """
    )
    st.info("👉 Single-period rationing → PI ranking (divisible) or combination search (indivisible). "
            "Multi-period rationing needs linear programming — beyond this page, but the principle is "
            "the same: maximise total NPV subject to the constraints.")

    st.markdown("#### 7 · The Overriding Objective")
    st.latex(r"\text{Maximise } \sum_{i \in \text{selected}} NPV_i \quad \text{subject to} \quad "
             r"\sum_{i \in \text{selected}} \text{Investment}_i \le \text{Budget}")

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - **Mutually exclusive** → pick the **highest NPV** (not the highest IRR or PI).
            - IRR misleads on **scale and timing**; the **crossover rate** marks where rankings diverge.
            - **Unequal lives** → compare using **EAA** (or replacement chains).
            - **Capital rationing** → rank by **PI** if divisible; search **combinations** if indivisible.
            - The goal is always to **maximise total NPV within the constraint**.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Example A · NPV vs IRR Conflict (Mutually Exclusive)")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> Two mutually exclusive projects, discount rate <b>10%</b>. Project S is small but
        high-return; Project L is large but lower-return. Which should you choose?
        </div>
        """,
        unsafe_allow_html=True,
    )

    r = 0.10
    proj_S = [-100_000, 65_000, 65_000]          # small
    proj_L = [-1_000_000, 600_000, 600_000]      # large

    npv_S, npv_L = npv(r, proj_S), npv(r, proj_L)

    # crude IRRs via bisection
    def irr(cfs, lo=-0.5, hi=2.0):
        grid = np.linspace(lo, hi, 400)
        prev = npv(grid[0], cfs)
        for x in grid[1:]:
            v = npv(x, cfs)
            if prev * v < 0:
                a, b = x - (grid[1] - grid[0]), x
                for _ in range(100):
                    m = (a + b) / 2
                    if npv(a, cfs) * npv(m, cfs) < 0:
                        b = m
                    else:
                        a = m
                return (a + b) / 2
            prev = v
        return None

    irr_S, irr_L = irr(proj_S), irr(proj_L)

    tbl = pd.DataFrame(
        {
            "Project": ["S (small)", "L (large)"],
            "Investment (€)": [100_000, 1_000_000],
            "NPV (€)": [npv_S, npv_L],
            "IRR (%)": [irr_S * 100, irr_L * 100],
        }
    )
    st.dataframe(
        tbl.style.format({"Investment (€)": "{:,.0f}", "NPV (€)": "{:,.0f}", "IRR (%)": "{:.1f}%"}),
        use_container_width=True, hide_index=True,
    )

    st.markdown(
        f"""
        - **IRR says:** choose **S** (IRR {irr_S*100:.1f}% > {irr_L*100:.1f}%).
        - **NPV says:** choose **L** (NPV €{npv_L:,.0f} > €{npv_S:,.0f}).
        """
    )
    st.success(f"✅ **Follow NPV → choose Project L.** It adds €{npv_L:,.0f} of value versus only "
               f"€{npv_S:,.0f} for S. IRR's higher percentage is on a much smaller base — the classic "
               f"**scale problem**.")

    # NPV profiles + crossover
    rates = np.linspace(0, 0.6, 61)
    npvs_S = [npv(x, proj_S) for x in rates]
    npvs_L = [npv(x, proj_L) for x in rates]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rates * 100, y=npvs_S, name="Project S", line=dict(color="#F9A825", width=3)))
    fig.add_trace(go.Scatter(x=rates * 100, y=npvs_L, name="Project L", line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="#C62828")
    fig.add_vline(x=10, line_dash="dot", line_color="#1B7F3B",
                  annotation_text="r = 10%", annotation_position="top")
    fig.update_layout(title="NPV profiles — the larger project adds more value at 10%",
                      xaxis_title="Discount rate (%)", yaxis_title="NPV (€)", height=430,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("🧮 Example B · Unequal Lives (EAA)")
    st.markdown(
        """
        <div class="bc-key">
        <b>Setup.</b> Machine A (3-year life) vs Machine B (5-year life), both at <b>10%</b>. Raw NPV
        favours the longer machine unfairly — so we compare using the Equivalent Annual Annuity.
        </div>
        """,
        unsafe_allow_html=True,
    )

    machine_A = [-200_000, 100_000, 100_000, 100_000]           # 3 yrs
    machine_B = [-300_000, 100_000, 100_000, 100_000, 100_000, 100_000]  # 5 yrs
    npv_A, npv_B = npv(r, machine_A), npv(r, machine_B)
    eaa_A, eaa_B = eaa(npv_A, r, 3), eaa(npv_B, r, 5)

    tbl2 = pd.DataFrame(
        {
            "Machine": ["A (3-yr)", "B (5-yr)"],
            "NPV (€)": [npv_A, npv_B],
            "Life (yrs)": [3, 5],
            "EAA (€/yr)": [eaa_A, eaa_B],
        }
    )
    st.dataframe(
        tbl2.style.format({"NPV (€)": "{:,.0f}", "EAA (€/yr)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    winner = "A" if eaa_A > eaa_B else "B"
    st.latex(rf"EAA_A = \frac{{{npv_A:,.0f}}}{{2.487}} = €{eaa_A:,.0f}/yr \quad;\quad "
             rf"EAA_B = \frac{{{npv_B:,.0f}}}{{3.791}} = €{eaa_B:,.0f}/yr")
    st.success(f"✅ On an equal-life basis, **Machine {winner} has the higher EAA** "
               f"(€{max(eaa_A, eaa_B):,.0f}/yr) → choose Machine {winner}. Raw NPV alone would have "
               f"been an unfair comparison.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Lab A · Mutually Exclusive Chooser (with EAA)")
    st.markdown("Enter competing projects, their NPVs (or let the tool use your inputs), lives, and the "
                "rate. The tool ranks by NPV and by EAA for unequal lives.")

    rate = st.slider("Discount rate (%)", 0.0, 25.0, 10.0, 0.5, key="me_rate") / 100.0

    default = pd.DataFrame(
        {
            "Project": ["A", "B", "C"],
            "Investment (€)": [200_000, 300_000, 250_000],
            "Annual cash flow (€)": [100_000, 100_000, 90_000],
            "Life (yrs)": [3, 5, 4],
        }
    )
    edited = st.data_editor(default, use_container_width=True, hide_index=True,
                            num_rows="dynamic", key="me_editor")

    ed = edited.copy()
    ed = ed[ed["Life (yrs)"] > 0]
    npvs, eaas = [], []
    for _, row in ed.iterrows():
        life = int(row["Life (yrs)"])
        cfs = [-row["Investment (€)"]] + [row["Annual cash flow (€)"]] * life
        p_npv = npv(rate, cfs)
        npvs.append(p_npv)
        eaas.append(eaa(p_npv, rate, life))
    ed["NPV (€)"] = npvs
    ed["EAA (€/yr)"] = eaas

    st.dataframe(
        ed.style.format({"Investment (€)": "{:,.0f}", "Annual cash flow (€)": "{:,.0f}",
                         "NPV (€)": "{:,.0f}", "EAA (€/yr)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    if len(ed) > 0:
        best_npv = ed.loc[ed["NPV (€)"].idxmax(), "Project"]
        best_eaa = ed.loc[ed["EAA (€/yr)"].idxmax(), "Project"]
        same_life = ed["Life (yrs)"].nunique() == 1

        c1, c2 = st.columns(2)
        c1.metric("Best by NPV", f"Project {best_npv}")
        c2.metric("Best by EAA (unequal lives)", f"Project {best_eaa}")

        fig = go.Figure()
        fig.add_trace(go.Bar(x=ed["Project"], y=ed["NPV (€)"], name="NPV",
                             marker_color="#1565C0"))
        fig.add_trace(go.Bar(x=ed["Project"], y=ed["EAA (€/yr)"], name="EAA",
                             marker_color="#F9A825"))
        fig.update_layout(barmode="group", title="NPV vs EAA by project",
                          yaxis_title="€", height=400, legend=dict(orientation="h", y=1.12),
                          margin=dict(t=60, b=40))
        st.plotly_chart(fig, use_container_width=True)

        if same_life:
            st.success(f"✅ Equal lives → simply pick the **highest NPV**: **Project {best_npv}**.")
        else:
            st.warning(f"🟠 Lives differ → compare on **EAA**: choose **Project {best_eaa}** "
                       f"(highest equivalent annual value). Raw NPV would favour Project {best_npv}, "
                       f"which may be an unfair comparison.")

    st.markdown("---")
    st.subheader("🎛️ Lab B · Capital Rationing Optimiser")
    st.markdown("Enter candidate projects and a budget. The tool ranks by PI (divisible) and also "
                "searches whole-project **combinations** (indivisible) for the highest total NPV.")

    budget = st.number_input("Capital budget (€)", min_value=0, value=1_000_000, step=100_000,
                             key="cr_budget")
    default_cr = pd.DataFrame(
        {
            "Project": ["A", "B", "C", "D", "E"],
            "Investment (€)": [500_000, 300_000, 400_000, 200_000, 350_000],
            "NPV (€)": [150_000, 120_000, 130_000, 95_000, 140_000],
        }
    )
    cr = st.data_editor(default_cr, use_container_width=True, hide_index=True,
                        num_rows="dynamic", key="cr_editor")

    cr = cr.copy()
    cr = cr[cr["Investment (€)"] > 0]
    cr["PV of inflows (€)"] = cr["Investment (€)"] + cr["NPV (€)"]
    cr["PI"] = cr["PV of inflows (€)"] / cr["Investment (€)"]
    cr_ranked = cr.sort_values("PI", ascending=False).reset_index(drop=True)

    # Divisible: greedy PI fill
    spent, tot_npv_div, chosen_div = 0, 0, []
    for _, row in cr_ranked.iterrows():
        if spent + row["Investment (€)"] <= budget:
            chosen_div.append(row["Project"]); spent += row["Investment (€)"]
            tot_npv_div += row["NPV (€)"]

    # Indivisible: best combination search
    projects = cr.to_dict("records")
    best_combo, best_combo_npv, best_combo_cost = [], -1e18, 0
    for k in range(1, len(projects) + 1):
        for combo in combinations(projects, k):
            cost = sum(p["Investment (€)"] for p in combo)
            if cost <= budget:
                tot = sum(p["NPV (€)"] for p in combo)
                if tot > best_combo_npv:
                    best_combo_npv = tot
                    best_combo = [p["Project"] for p in combo]
                    best_combo_cost = cost

    st.dataframe(
        cr_ranked.style.format({"Investment (€)": "{:,.0f}", "NPV (€)": "{:,.0f}",
                                "PV of inflows (€)": "{:,.0f}", "PI": "{:.3f}"}),
        use_container_width=True, hide_index=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("##### 🍰 Divisible (PI ranking)")
        st.metric("Projects funded", ", ".join(chosen_div) if chosen_div else "None")
        st.metric("Total NPV", f"€{tot_npv_div:,.0f}")
        st.caption(f"Capital used: €{spent:,.0f}")
    with c2:
        st.markdown("##### 🧱 Indivisible (best combination)")
        st.metric("Projects funded", ", ".join(best_combo) if best_combo else "None")
        st.metric("Total NPV", f"€{best_combo_npv:,.0f}")
        st.caption(f"Capital used: €{best_combo_cost:,.0f}")

    if best_combo_npv >= tot_npv_div:
        st.success(f"✅ For **indivisible** projects, the best whole-project set is "
                   f"**{', '.join(best_combo)}** delivering **€{best_combo_npv:,.0f}** NPV — note this "
                   f"can differ from the simple PI ranking because projects can't be split.")
    else:
        st.info("ℹ️ Here PI ranking and the combination search agree on the selection.")

    st.caption("Reminder: PI ranking is optimal only when projects are divisible. For all-or-nothing "
               "projects, the combination search finds the true value-maximising set.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. For mutually exclusive projects, the correct primary criterion is…",
            "options": ["Highest IRR", "Highest NPV", "Shortest payback", "Highest PI"],
            "answer": 1,
            "why": "NPV measures absolute value added, so choose the highest positive NPV.",
        },
        {
            "q": "2. IRR can mislead when ranking mutually exclusive projects mainly because of…",
            "options": [
                "Its use of cash flows",
                "Differences in project scale and cash-flow timing",
                "It always equals NPV",
                "It ignores the initial investment",
            ],
            "answer": 1,
            "why": "IRR is a percentage, so it ignores scale; timing differences also cause conflicts with NPV.",
        },
        {
            "q": "3. The crossover rate on two NPV profiles is the discount rate at which…",
            "options": [
                "Both NPVs are zero",
                "The two projects have equal NPV",
                "IRR equals WACC",
                "Payback is reached",
            ],
            "answer": 1,
            "why": "The crossover rate is where the two projects' NPVs are equal — rankings can flip around it.",
        },
        {
            "q": "4. To compare projects with unequal lives you should use…",
            "options": [
                "Raw NPV only",
                "The Equivalent Annual Annuity (or replacement-chain) method",
                "The payback period",
                "The accounting rate of return",
            ],
            "answer": 1,
            "why": "EAA converts each NPV into a level annual figure, enabling a fair comparison across lives.",
        },
        {
            "q": "5. Under capital rationing with DIVISIBLE projects, you should rank by…",
            "options": ["NPV", "Profitability Index (PI)", "IRR", "Payback"],
            "answer": 1,
            "why": "PI (value per euro invested) maximises total NPV within a budget when projects are divisible.",
        },
        {
            "q": "6. For INDIVISIBLE (all-or-nothing) projects under a budget, you should…",
            "options": [
                "Always follow the PI ranking exactly",
                "Test feasible combinations for the highest total NPV",
                "Choose the single highest-IRR project",
                "Ignore the budget constraint",
            ],
            "answer": 1,
            "why": "With indivisible projects, PI ranking may be suboptimal; search whole-project combinations for max total NPV.",
        },
    ]

    with st.form("quiz_4_2"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q42_{i}")
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
            st.success("🏆 Perfect! You can now choose between projects and ration capital like a pro.")
        elif pct >= 60:
            st.info("👍 Good work — continue to **4.3 · Qualitative Factors & Governance**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on NPV-vs-IRR conflicts, EAA, and PI rationing.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `4.1 · Decision Rules & Method Comparison`")
with cnext:
    st.markdown("**Next:** `4.3 · Qualitative Factors & Governance` ➡️")
st.caption("Business Case section · Page 4.2 · Built with Streamlit")
