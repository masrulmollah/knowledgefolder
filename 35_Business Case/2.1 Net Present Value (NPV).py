# ============================================================================
#  BUSINESS CASE — Section
#  Page 2.1 · Net Present Value (NPV)
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
    page_title="2.1 · Net Present Value (NPV)",
    page_icon="💎",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Parts 0–1)
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
        <h1>2.1 · Net Present Value (NPV)</h1>
        <p>The gold standard of investment appraisal — the value a project adds today,
        after discounting every future cash flow at the cost of capital.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Compute NPV, apply the decision rule, read an NPV profile, and explain "
           "why NPV is the theoretically superior appraisal method.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def npv(rate, cashflows):
    """cashflows[0] is Year 0 (typically negative)."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


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
        <b>Net Present Value (NPV)</b> is the sum of all a project's cash flows, each discounted back
        to today at the required rate of return, <b>minus the initial investment</b>. It measures the
        <b>absolute value in today's money</b> that a project is expected to add to the business.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · The Formula")
    st.latex(r"NPV = \sum_{t=0}^{n} \frac{CF_t}{(1 + r)^{t}}")
    st.markdown("Or, separating the initial outlay in Year 0:")
    st.latex(r"NPV = -\,C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1 + r)^{t}}")
    st.markdown(
        """
        Where:
        - $CF_t$ = net cash flow in year $t$ &nbsp;•&nbsp; $C_0$ = initial investment (Year 0)
        - $r$ = discount rate (WACC / hurdle rate) &nbsp;•&nbsp; $n$ = project life in years
        """
    )

    st.subheader("3 · The Decision Rule")
    st.markdown(
        """
        <div class="bc-card">
        <h4>📏 Accept / Reject</h4>
        <ul>
          <li><span class="good">NPV &gt; 0</span> → <b>Accept.</b> The project earns more than the
          cost of capital and <b>adds value</b>.</li>
          <li><span class="bad">NPV &lt; 0</span> → <b>Reject.</b> It destroys value.</li>
          <li><b>NPV = 0</b> → Indifferent; it exactly meets the required return.</li>
          <li>For <b>mutually exclusive</b> projects, choose the <b>highest positive NPV</b>.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("4 · Why NPV Is the Gold Standard")
    for t, b in [
        ("💰 Measures value directly",
         "NPV is expressed in currency — it tells you exactly how much wealth the project creates for owners."),
        ("⏳ Uses the time value of money",
         "Every cash flow is discounted, so timing and the cost of capital are fully respected."),
        ("📊 Uses all cash flows",
         "Unlike payback, it counts every year of the project, including the tail."),
        ("➕ It is additive",
         "NPVs of independent projects can be summed — total value = sum of parts."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("5 · The NPV Profile")
    st.markdown(
        """
        The **NPV profile** plots NPV against different discount rates. It slopes **downward** — the
        higher the rate, the lower the NPV. The rate at which the curve **crosses zero** is the
        project's **Internal Rate of Return (IRR)** — the bridge to the next page.
        """
    )

    st.subheader("6 · Strengths & Limitations")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👍 Strengths</h4>
            <ul>
              <li>Theoretically <b>correct</b> — maximises shareholder wealth</li>
              <li>Accounts for <b>time value</b> and <b>all</b> cash flows</li>
              <li>Gives an <b>absolute €</b> value of wealth created</li>
              <li>Handles <b>uneven</b> cash flows and changing rates</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👎 Limitations</h4>
            <ul>
              <li>Very sensitive to the <b>discount rate</b> assumption</li>
              <li>Requires reliable <b>cash-flow forecasts</b></li>
              <li>An <b>absolute</b> figure — doesn't show return <i>per €</i> (see PI, 2.4)</li>
              <li>Harder to communicate than a simple % or payback</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - NPV = present value of all cash flows − initial investment.
            - Decision rule: **accept if NPV > 0**; pick the highest NPV among alternatives.
            - It fully respects the **time value of money** and uses **all** cash flows.
            - The discount rate where NPV = 0 is the **IRR**.
            - NPV is the **most reliable** single measure of value creation.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Discounting a Project to Find Its NPV")
    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> A project costs <b>€500,000</b> today and returns <b>€160,000</b> per year
        for <b>5 years</b>. The discount rate (WACC) is <b>10%</b>. Does it add value?
        </div>
        """,
        unsafe_allow_html=True,
    )

    r = 0.10
    cfs = [-500_000, 160_000, 160_000, 160_000, 160_000, 160_000]
    years = list(range(len(cfs)))
    dfs = [1 / (1 + r) ** t for t in years]
    pvs = [cf * d for cf, d in zip(cfs, dfs)]
    cum_pv = pd.Series(pvs).cumsum().tolist()
    project_npv = sum(pvs)

    df = pd.DataFrame(
        {
            "Year": years,
            "Cash Flow (€)": cfs,
            "Discount Factor @10%": [round(d, 4) for d in dfs],
            "Present Value (€)": pvs,
            "Cumulative PV (€)": cum_pv,
        }
    )
    st.dataframe(
        df.style.format({"Cash Flow (€)": "{:,.0f}", "Discount Factor @10%": "{:.4f}",
                         "Present Value (€)": "{:,.0f}", "Cumulative PV (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    pv_inflows = sum(pvs[1:])
    st.latex(rf"NPV = -500{{,}}000 + {pv_inflows:,.0f} = €{project_npv:,.0f}")

    if project_npv > 0:
        st.success(f"✅ **NPV = €{project_npv:,.0f} > 0 → ACCEPT.** The project adds about "
                   f"€{project_npv:,.0f} of value in today's money, over and above the 10% required return.")
    else:
        st.error(f"❌ NPV = €{project_npv:,.0f} < 0 → reject.")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=cfs, name="Nominal cash flow", marker_color="#BBD3F2"))
    fig.add_trace(go.Bar(x=years, y=pvs, name="Present value", marker_color="#1565C0"))
    fig.update_layout(title="Nominal vs discounted cash flows @10%",
                      barmode="overlay", xaxis_title="Year", yaxis_title="€",
                      height=420, legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    fig.update_traces(opacity=0.85)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### The NPV profile — where NPV hits zero is the IRR")
    rates = np.linspace(0, 0.35, 36)
    npvs = [npv(rr, cfs) for rr in rates]
    figp = go.Figure(go.Scatter(x=rates * 100, y=npvs, mode="lines",
                                line=dict(color="#0B3D91", width=3)))
    figp.add_hline(y=0, line_dash="dash", line_color="#C62828")
    figp.add_vline(x=10, line_dash="dot", line_color="#1B7F3B",
                   annotation_text="r = 10%", annotation_position="top")
    figp.update_layout(title="NPV profile — NPV vs discount rate",
                       xaxis_title="Discount rate (%)", yaxis_title="NPV (€)",
                       height=420, margin=dict(t=60, b=40))
    st.plotly_chart(figp, use_container_width=True)
    st.info("👉 The curve slopes down and crosses zero near ~18% — that crossing point is the project's "
            "**IRR**, which we'll compute exactly on the next page (2.2).")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ NPV Calculator with Editable Cash Flows")
    st.markdown("Edit the yearly cash flows and the discount rate. The NPV, discounted table, and "
                "NPV profile update instantly.")

    c1, c2, c3 = st.columns(3)
    with c1:
        invest = st.number_input("Initial investment (€, Year 0)", min_value=0, value=500_000, step=25_000)
    with c2:
        rate = st.slider("Discount rate r (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
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
                                num_rows="fixed", key="npv_editor")
        inflows = edited["Cash Flow (€)"].tolist()

    cfs = [-invest] + inflows
    years = list(range(len(cfs)))
    dfs = [1 / (1 + rate) ** t for t in years]
    pvs = [cf * d for cf, d in zip(cfs, dfs)]
    cum_pv = pd.Series(pvs).cumsum().tolist()
    project_npv = sum(pvs)

    tbl = pd.DataFrame(
        {
            "Year": years,
            "Cash Flow (€)": cfs,
            "Discount Factor": [round(d, 4) for d in dfs],
            "Present Value (€)": pvs,
            "Cumulative PV (€)": cum_pv,
        }
    )
    st.dataframe(
        tbl.style.format({"Cash Flow (€)": "{:,.0f}", "Discount Factor": "{:.4f}",
                          "Present Value (€)": "{:,.0f}", "Cumulative PV (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("NPV", f"€{project_npv:,.0f}")
    m2.metric("PV of inflows", f"€{sum(pvs[1:]):,.0f}")
    m3.metric("Undiscounted net", f"€{sum(cfs):,.0f}")

    # NPV profile with IRR crossing
    rates = np.linspace(0, 0.5, 51)
    npvs = [npv(rr, cfs) for rr in rates]
    # crude IRR detection (sign change)
    irr = None
    for i in range(1, len(npvs)):
        if npvs[i - 1] > 0 >= npvs[i]:
            x0, x1, y0, y1 = rates[i - 1], rates[i], npvs[i - 1], npvs[i]
            irr = x0 + (x1 - x0) * y0 / (y0 - y1)
            break

    figp = go.Figure(go.Scatter(x=rates * 100, y=npvs, mode="lines",
                                line=dict(color="#0B3D91", width=3), name="NPV"))
    figp.add_hline(y=0, line_dash="dash", line_color="#C62828")
    figp.add_vline(x=rate * 100, line_dash="dot", line_color="#1B7F3B",
                   annotation_text=f"r = {rate*100:.1f}%", annotation_position="top")
    if irr is not None:
        figp.add_vline(x=irr * 100, line_dash="dot", line_color="#F9A825",
                       annotation_text=f"IRR ≈ {irr*100:.1f}%", annotation_position="bottom")
    figp.update_layout(title="NPV profile", xaxis_title="Discount rate (%)",
                       yaxis_title="NPV (€)", height=420, margin=dict(t=60, b=40))
    st.plotly_chart(figp, use_container_width=True)

    if project_npv > 0:
        st.success(f"✅ **NPV = €{project_npv:,.0f} > 0 → ACCEPT.** The project adds value at a "
                   f"{rate*100:.1f}% cost of capital."
                   + (f" Its IRR is ≈ **{irr*100:.1f}%**." if irr is not None else ""))
    elif project_npv < 0:
        st.error(f"❌ **NPV = €{project_npv:,.0f} < 0 → REJECT.** It destroys value at this rate."
                 + (f" IRR ≈ {irr*100:.1f}% is below the {rate*100:.1f}% hurdle." if irr is not None else ""))
    else:
        st.info("NPV = 0 — the project exactly meets the required return.")

    st.caption("Tip: raise the discount rate and watch NPV fall — where it crosses zero is the IRR, "
               "the subject of page 2.2.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. NPV measures…",
            "options": [
                "The time to recover the investment",
                "The value in today's money that a project adds",
                "The average accounting profit",
                "The discount rate that makes IRR zero",
            ],
            "answer": 1,
            "why": "NPV is the present value of all cash flows minus the outlay — the wealth added today.",
        },
        {
            "q": "2. Under the NPV rule, you accept a project when…",
            "options": ["NPV < 0", "NPV = 0", "NPV > 0", "NPV equals the payback"],
            "answer": 2,
            "why": "A positive NPV means the project earns more than the cost of capital and adds value.",
        },
        {
            "q": "3. As the discount rate rises, a conventional project's NPV…",
            "options": ["Rises", "Falls", "Stays constant", "Always turns positive"],
            "answer": 1,
            "why": "Higher discount rates shrink future cash flows, so NPV falls — the NPV profile slopes down.",
        },
        {
            "q": "4. The discount rate at which NPV equals zero is the…",
            "options": ["WACC", "Hurdle rate", "Internal Rate of Return (IRR)", "Payback rate"],
            "answer": 2,
            "why": "By definition, the IRR is the rate that makes NPV exactly zero.",
        },
        {
            "q": "5. Between two mutually exclusive projects, NPV says choose the one with…",
            "options": [
                "The shorter payback",
                "The highest positive NPV",
                "The lowest discount rate",
                "The higher ARR",
            ],
            "answer": 1,
            "why": "NPV maximises value, so pick the project with the highest positive NPV.",
        },
        {
            "q": "6. A key advantage of NPV over payback and ARR is that it…",
            "options": [
                "Ignores the time value of money",
                "Uses all cash flows and the time value of money",
                "Requires no discount rate",
                "Is based on accounting profit",
            ],
            "answer": 1,
            "why": "NPV discounts every cash flow across the whole life — respecting both timing and completeness.",
        },
    ]

    with st.form("quiz_2_1"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q21_{i}")
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
            st.success("🏆 Perfect! You've mastered the gold-standard method of investment appraisal.")
        elif pct >= 60:
            st.info("👍 Strong work — continue to **2.2 · Internal Rate of Return (IRR & MIRR)**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — NPV underpins everything that follows.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `1.2 · Accounting Rate of Return (ARR)`")
with cnext:
    st.markdown("**Next:** `2.2 · Internal Rate of Return (IRR & MIRR)` ➡️")
st.caption("Business Case section · Page 2.1 · Built with Streamlit")
