# ============================================================================
#  BUSINESS CASE — Section
#  Page 1.1 · Payback Period
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="1.1 · Payback Period",
    page_icon="⏱️",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with Part 0)
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
        <span class="bc-tag">PART 1 · NON-DISCOUNTED METHODS</span>
        <h1>1.1 · Payback Period</h1>
        <p>The simplest screen of all — how long until an investment pays for itself?
        Fast, intuitive, and a great first filter, but with important blind spots.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Calculate payback for even and uneven cash flows, apply the decision "
           "rule, and understand its strengths and limitations.")

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
        The <b>Payback Period</b> is the length of time it takes for the cumulative cash inflows from
        an investment to <b>recover the initial outlay</b>. In plain terms: <i>“How many years until
        we get our money back?”</i>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · The Two Formulas")
    st.markdown("**a) Even cash flows** — when the annual inflow is constant:")
    st.latex(r"\text{Payback} = \frac{\text{Initial Investment}}{\text{Annual Net Cash Inflow}}")
    st.markdown("**b) Uneven cash flows** — accumulate year by year until the outlay is recovered:")
    st.latex(r"\text{Payback} = A + \frac{B}{C}")
    st.markdown(
        """
        Where:
        - $A$ = the last full year **before** cumulative cash flow turns positive
        - $B$ = the amount **still unrecovered** at the start of that year
        - $C$ = the cash inflow **during** the year recovery is completed
        """
    )

    st.subheader("3 · The Decision Rule")
    st.markdown(
        """
        <div class="bc-card">
        <h4>📏 Accept / Reject</h4>
        <ul>
          <li><span class="good">Accept</span> if the payback period is <b>shorter</b> than the
          company's maximum acceptable period (the target/cutoff).</li>
          <li><span class="bad">Reject</span> if it is <b>longer</b> than the cutoff.</li>
          <li>For <b>mutually exclusive</b> projects, prefer the one with the <b>shorter</b> payback.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("4 · Strengths & Weaknesses")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👍 Strengths</h4>
            <ul>
              <li><b>Simple</b> and quick to compute and explain</li>
              <li>Emphasises <b>liquidity</b> — how fast cash returns</li>
              <li>A useful <b>risk screen</b>: shorter payback = less exposure to an uncertain future</li>
              <li>Great <b>first filter</b> before deeper analysis</li>
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
              <li><b>Ignores the time value of money</b> (fixed by <i>Discounted Payback</i>, page 2.3)</li>
              <li><b>Ignores all cash flows after</b> the payback point</li>
              <li>Says nothing about <b>total profitability</b> or value created</li>
              <li>The cutoff period is often <b>arbitrary</b></li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    st.subheader("5 · Where It Fits in a Business Case")
    st.markdown(
        """
        Payback is a **screening tool**, not a decision-maker on its own. Use it to quickly reject
        obviously slow projects and to communicate liquidity risk — but always confirm the decision
        with a **discounted** method (NPV/IRR) that accounts for the time value of money and the
        *whole* project life.
        """
    )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - Payback = time to recover the initial investment.
            - Even flows → divide; uneven flows → accumulate and interpolate.
            - Decision rule: accept if **< cutoff**; shorter is better.
            - Big blind spots: **ignores TVM** and **ignores cash beyond payback**.
            - Best used as a **first-pass screen** alongside NPV/IRR.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Example A · Even Cash Flows")
    st.markdown(
        """
        <div class="bc-key">
        An investment of <b>€500,000</b> returns a steady <b>€160,000</b> per year.
        The company's cutoff is <b>4 years</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )
    pb_even = 500_000 / 160_000
    st.latex(r"\text{Payback} = \frac{500{,}000}{160{,}000} = 3.13\ \text{years}")
    st.success(f"Payback ≈ **{pb_even:.2f} years** < 4-year cutoff → **ACCEPT** ✅ (passes the screen).")

    st.markdown("---")
    st.subheader("🧮 Example B · Uneven Cash Flows")
    st.markdown(
        """
        <div class="bc-key">
        An investment of <b>€500,000</b> returns uneven inflows over 5 years. Let's find the exact
        payback point by accumulating the cash flows.
        </div>
        """,
        unsafe_allow_html=True,
    )

    years = [0, 1, 2, 3, 4, 5]
    cf = [-500_000, 120_000, 150_000, 180_000, 200_000, 150_000]
    cum = pd.Series(cf).cumsum().tolist()

    df = pd.DataFrame({"Year": years, "Cash Flow (€)": cf, "Cumulative (€)": cum})
    st.dataframe(
        df.style.format({"Cash Flow (€)": "{:,.0f}", "Cumulative (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    # find payback
    A, B, C = None, None, None
    for i in range(1, len(cum)):
        if cum[i - 1] < 0 <= cum[i]:
            A = years[i - 1]
            B = -cum[i - 1]
            C = cf[i]
            break
    payback = A + B / C
    st.latex(rf"\text{{Payback}} = {A} + \frac{{{B:,.0f}}}{{{C:,.0f}}} = {payback:.2f}\ \text{{years}}")
    st.markdown(
        f"""
        - At the end of **Year {A}**, €{B:,.0f} is still unrecovered.
        - Year {A+1} brings in €{C:,.0f}, so recovery completes partway through.
        - **Payback ≈ {payback:.2f} years.**
        """
    )

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=cf, name="Cash flow",
                         marker_color=["#C62828"] + ["#1E88E5"] * 5))
    fig.add_trace(go.Scatter(x=years, y=cum, name="Cumulative",
                             mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="grey")
    fig.update_layout(title="Uneven cash flows — recovery point",
                      xaxis_title="Year", yaxis_title="€", height=420,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.info("⚠️ Notice payback ignores the €150,000 that arrives in Year 5 — it stops counting once "
            "the outlay is recovered. That's the method's biggest blind spot.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Payback Calculator (Even or Uneven Cash Flows)")
    st.markdown("Edit the cash flows and set a cutoff. The calculator finds the exact payback point "
                "and applies the decision rule.")

    c1, c2, c3 = st.columns(3)
    with c1:
        invest = st.number_input("Initial investment (€, Year 0)", min_value=0, value=500_000, step=25_000)
    with c2:
        n_years = st.slider("Number of years", 1, 12, 5)
    with c3:
        cutoff = st.number_input("Max acceptable payback (years)", min_value=0.0, value=4.0, step=0.5)

    mode = st.radio("Cash-flow pattern", ["Even (constant)", "Uneven (edit table)"], horizontal=True)

    if mode.startswith("Even"):
        annual = st.number_input("Annual net inflow (€)", min_value=0, value=160_000, step=10_000)
        inflows = [annual] * n_years
    else:
        default = pd.DataFrame({"Year": list(range(1, n_years + 1)),
                                "Cash Flow (€)": [120000, 150000, 180000, 200000, 150000][:n_years]
                                + [150000] * max(0, n_years - 5)})
        edited = st.data_editor(default, use_container_width=True, hide_index=True,
                                num_rows="fixed", key="pb_editor")
        inflows = edited["Cash Flow (€)"].tolist()

    # Build cumulative
    years = list(range(0, n_years + 1))
    cf = [-invest] + inflows
    cum = pd.Series(cf).cumsum().tolist()

    payback = None
    for i in range(1, len(cum)):
        if cum[i - 1] < 0 <= cum[i]:
            denom = cf[i] if cf[i] != 0 else 1
            payback = (i - 1) + (-cum[i - 1] / denom)
            break

    tbl = pd.DataFrame({"Year": years, "Cash Flow (€)": cf, "Cumulative (€)": cum})
    st.dataframe(
        tbl.style.format({"Cash Flow (€)": "{:,.0f}", "Cumulative (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("Payback period", f"{payback:.2f} yrs" if payback is not None else "Not recovered")
    m2.metric("Total net (undiscounted)", f"€{sum(cf):,.0f}")
    m3.metric("Cutoff", f"{cutoff:.1f} yrs")

    figl = go.Figure()
    figl.add_trace(go.Bar(x=years, y=cf, name="Cash flow",
                          marker_color=["#C62828"] + ["#1E88E5"] * n_years))
    figl.add_trace(go.Scatter(x=years, y=cum, name="Cumulative",
                              mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    figl.add_hline(y=0, line_dash="dash", line_color="grey")
    if payback is not None:
        figl.add_vline(x=payback, line_dash="dot", line_color="#1B7F3B",
                       annotation_text=f"Payback {payback:.2f}y", annotation_position="top")
    figl.update_layout(xaxis_title="Year", yaxis_title="€", height=420,
                       legend=dict(orientation="h", y=1.12), margin=dict(t=50, b=40))
    st.plotly_chart(figl, use_container_width=True)

    if payback is None:
        st.error("⚠️ The investment is **never recovered** within its life → **REJECT**.")
    elif payback <= cutoff:
        st.success(f"✅ Payback of **{payback:.2f} years** ≤ cutoff of {cutoff:.1f} years → **ACCEPT** "
                   f"(passes the screen).")
    else:
        st.warning(f"🟠 Payback of **{payback:.2f} years** > cutoff of {cutoff:.1f} years → **REJECT** "
                   f"on this screen.")

    st.caption("Reminder: payback ignores the time value of money and any cash beyond the recovery "
               "point. Confirm with NPV/IRR (Part 2).")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 5 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. The payback period measures…",
            "options": [
                "The total profit of a project",
                "The time to recover the initial investment",
                "The project's internal rate of return",
                "The present value of all cash flows",
            ],
            "answer": 1,
            "why": "Payback is simply the time it takes for cumulative inflows to recover the initial outlay.",
        },
        {
            "q": "2. For an investment of €600,000 with even inflows of €150,000/yr, payback is…",
            "options": ["3 years", "4 years", "5 years", "6 years"],
            "answer": 1,
            "why": "600,000 ÷ 150,000 = 4 years.",
        },
        {
            "q": "3. The standard payback period's biggest weakness is that it…",
            "options": [
                "Is too complex to calculate",
                "Ignores the time value of money and cash flows after payback",
                "Requires a discount rate",
                "Overstates liquidity risk",
            ],
            "answer": 1,
            "why": "It ignores the time value of money AND all cash flows occurring after the payback point.",
        },
        {
            "q": "4. Under the payback decision rule, a project is accepted if its payback is…",
            "options": [
                "Longer than the cutoff period",
                "Equal to the IRR",
                "Shorter than the cutoff period",
                "Greater than the NPV",
            ],
            "answer": 2,
            "why": "Accept if payback is shorter than the maximum acceptable (cutoff) period.",
        },
        {
            "q": "5. Payback is best used as…",
            "options": [
                "The sole basis for major investment decisions",
                "A first-pass screening tool alongside NPV/IRR",
                "A replacement for cash-flow forecasting",
                "A measure of total shareholder value",
            ],
            "answer": 1,
            "why": "It's a quick liquidity/risk screen — confirm decisions with discounted methods.",
        },
    ]

    with st.form("quiz_1_1"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q11_{i}")
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
            st.success("🏆 Perfect! You've mastered the payback method.")
        elif pct >= 60:
            st.info("👍 Good work — continue to **1.2 · Accounting Rate of Return (ARR)**.")
        else:
            st.warning("📖 Revisit the **Theory** tab and retry — payback is a quick but important screen.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `0.3 · Time Value of Money & Discount Rate`")
with cnext:
    st.markdown("**Next:** `1.2 · Accounting Rate of Return (ARR)` ➡️")
st.caption("Business Case section · Page 1.1 · Built with Streamlit")
