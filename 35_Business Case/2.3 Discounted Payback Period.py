# ============================================================================
#  BUSINESS CASE — Section
#  Page 2.3 · Discounted Payback Period
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="2.3 · Discounted Payback Period",
    page_icon="⏳",
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
        <h1>2.3 · Discounted Payback Period</h1>
        <p>Payback's smarter cousin — how long until an investment pays for itself
        once every cash flow is discounted to today's value.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Calculate discounted payback, contrast it with simple payback, and "
           "understand what it fixes — and what it still misses.")

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def find_payback(cumulative, cashflow_series):
    """Interpolated period where cumulative crosses zero. Returns None if never."""
    for i in range(1, len(cumulative)):
        if cumulative[i - 1] < 0 <= cumulative[i]:
            denom = cashflow_series[i] if cashflow_series[i] != 0 else 1
            return (i - 1) + (-cumulative[i - 1] / denom)
    return None


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
        The <b>Discounted Payback Period</b> is the time it takes for the <b>cumulative
        <u>discounted</u> cash flows</b> to recover the initial investment. It's the same idea as
        simple payback (page 1.1), but each cash flow is first brought back to today's value using
        the discount rate — so it respects the <b>time value of money</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("2 · How It Works — Three Steps")
    for t, b in [
        ("1️⃣ Discount each cash flow",
         "Multiply every year's cash flow by its discount factor 1/(1+r)ᵗ to get its present value."),
        ("2️⃣ Accumulate the discounted flows",
         "Build a running total of the present values, starting from the negative initial outlay."),
        ("3️⃣ Find the crossing point",
         "The discounted payback is the moment the cumulative discounted cash flow turns positive."),
    ]:
        st.markdown(f"<div class='bc-step'><b>{t}</b><br>{b}</div>", unsafe_allow_html=True)

    st.subheader("3 · The Interpolation Formula")
    st.latex(r"\text{Discounted Payback} = A + \frac{B}{C}")
    st.markdown(
        """
        Where (all on a **discounted** basis):
        - $A$ = last full year **before** cumulative discounted cash flow turns positive
        - $B$ = discounted amount **still unrecovered** at the start of that year
        - $C$ = **discounted** cash inflow during the year recovery completes
        """
    )

    st.subheader("4 · The Decision Rule")
    st.markdown(
        """
        <div class="bc-card">
        <h4>📏 Accept / Reject</h4>
        <ul>
          <li><span class="good">Accept</span> if discounted payback is <b>shorter</b> than the
          maximum acceptable period <b>and</b> occurs within the project's life.</li>
          <li><span class="bad">Reject</span> if it exceeds the cutoff or never occurs.</li>
        </ul>
        <span class="muted">Note: if a project never reaches discounted payback within its life,
        its NPV is negative.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("5 · Simple vs Discounted Payback")
    cmp = pd.DataFrame(
        {
            "Feature": ["Uses time value of money?", "Typical result",
                        "Ignores cash after payback?", "Measures total profitability?"],
            "Simple Payback": ["No", "Shorter", "Yes", "No"],
            "Discounted Payback": ["Yes ✅", "Longer (more conservative)", "Yes", "No"],
        }
    )
    st.table(cmp)
    st.info("👉 Discounted payback is **always ≥ simple payback**, because discounting shrinks the "
            "inflows, so it takes longer to recover the outlay.")

    st.subheader("6 · Strengths & Weaknesses")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>👍 Strengths</h4>
            <ul>
              <li>Fixes payback's biggest flaw — <b>respects the time value of money</b></li>
              <li>Still an intuitive <b>liquidity / risk</b> screen</li>
              <li>More <b>conservative</b> and realistic than simple payback</li>
              <li>Consistent with NPV up to the payback point</li>
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
              <li><b>Still ignores cash flows after</b> the payback point</li>
              <li>Doesn't measure <b>total value</b> created (use NPV)</li>
              <li>The cutoff period remains <b>somewhat arbitrary</b></li>
              <li>Needs a <b>discount rate</b> (unlike simple payback)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    with st.expander("🔑 Key takeaways"):
        st.markdown(
            """
            - Discounted payback = time to recover the outlay using **discounted** cash flows.
            - It **fixes** payback's time-value blind spot but **still ignores** cash beyond payback.
            - It is always **longer than or equal to** simple payback.
            - Best used as a **risk/liquidity screen** alongside NPV & IRR — not a standalone decision.
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Simple vs Discounted Payback — Side by Side")
    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> An investment of <b>€500,000</b> returns <b>€160,000</b> per year for
        <b>5 years</b>. The discount rate is <b>10%</b>. Let's compute both paybacks and compare.
        </div>
        """,
        unsafe_allow_html=True,
    )

    r = 0.10
    cfs = [-500_000, 160_000, 160_000, 160_000, 160_000, 160_000]
    years = list(range(len(cfs)))
    dfs = [1 / (1 + r) ** t for t in years]
    pvs = [cf * d for cf, d in zip(cfs, dfs)]
    cum_simple = pd.Series(cfs).cumsum().tolist()
    cum_disc = pd.Series(pvs).cumsum().tolist()

    df = pd.DataFrame(
        {
            "Year": years,
            "Cash Flow (€)": cfs,
            "Discount Factor @10%": [round(d, 4) for d in dfs],
            "Discounted CF (€)": pvs,
            "Cumulative Simple (€)": cum_simple,
            "Cumulative Discounted (€)": cum_disc,
        }
    )
    st.dataframe(
        df.style.format({"Cash Flow (€)": "{:,.0f}", "Discount Factor @10%": "{:.4f}",
                         "Discounted CF (€)": "{:,.0f}", "Cumulative Simple (€)": "{:,.0f}",
                         "Cumulative Discounted (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    pb_simple = find_payback(cum_simple, cfs)
    pb_disc = find_payback(cum_disc, pvs)

    c1, c2 = st.columns(2)
    c1.metric("Simple payback", f"{pb_simple:.2f} yrs")
    c2.metric("Discounted payback", f"{pb_disc:.2f} yrs" if pb_disc else "Not within life")

    if pb_disc:
        st.latex(rf"\text{{Discounted Payback}} \approx {pb_disc:.2f}\ \text{{years}}")
        st.success(f"✅ Simple payback is **{pb_simple:.2f} years**, but once we discount, it stretches "
                   f"to **{pb_disc:.2f} years** — the more honest figure, because early euros are worth "
                   f"more than later ones.")
    else:
        st.warning("The discounted cumulative never turns positive within the project's life — a red flag.")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=cum_simple, name="Cumulative simple",
                             mode="lines+markers", line=dict(color="#90CAF9", width=3)))
    fig.add_trace(go.Scatter(x=years, y=cum_disc, name="Cumulative discounted",
                             mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="#C62828")
    if pb_simple:
        fig.add_vline(x=pb_simple, line_dash="dot", line_color="#90CAF9")
    if pb_disc:
        fig.add_vline(x=pb_disc, line_dash="dot", line_color="#0B3D91",
                      annotation_text=f"Disc. payback {pb_disc:.2f}y", annotation_position="top")
    fig.update_layout(title="Simple vs discounted cumulative recovery",
                      xaxis_title="Year", yaxis_title="€", height=430,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.info("⚠️ Both measures still ignore the cash flows that arrive **after** the payback point. "
            "For the full picture of value, rely on **NPV** (page 2.1).")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Discounted Payback Calculator")
    st.markdown("Edit the cash flows and discount rate. The calculator finds both the simple and "
                "discounted payback and applies the decision rule.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        invest = st.number_input("Initial investment (€)", min_value=0, value=500_000, step=25_000)
    with c2:
        rate = st.slider("Discount rate (%)", 0.0, 30.0, 10.0, 0.5) / 100.0
    with c3:
        n_years = st.slider("Number of years", 1, 12, 5)
    with c4:
        cutoff = st.number_input("Max acceptable (yrs)", min_value=0.0, value=4.0, step=0.5)

    pattern = st.radio("Inflow pattern", ["Even (constant)", "Uneven (edit table)"], horizontal=True)
    if pattern.startswith("Even"):
        annual = st.number_input("Annual inflow (€)", min_value=0, value=160_000, step=10_000)
        inflows = [annual] * n_years
    else:
        default = pd.DataFrame({"Year": list(range(1, n_years + 1)),
                                "Cash Flow (€)": [140000, 150000, 160000, 170000, 180000][:n_years]
                                + [160000] * max(0, n_years - 5)})
        edited = st.data_editor(default, use_container_width=True, hide_index=True,
                                num_rows="fixed", key="dpb_editor")
        inflows = edited["Cash Flow (€)"].tolist()

    cfs = [-invest] + inflows
    years = list(range(len(cfs)))
    dfs = [1 / (1 + rate) ** t for t in years]
    pvs = [cf * d for cf, d in zip(cfs, dfs)]
    cum_simple = pd.Series(cfs).cumsum().tolist()
    cum_disc = pd.Series(pvs).cumsum().tolist()

    tbl = pd.DataFrame(
        {
            "Year": years,
            "Cash Flow (€)": cfs,
            "Discount Factor": [round(d, 4) for d in dfs],
            "Discounted CF (€)": pvs,
            "Cumulative Discounted (€)": cum_disc,
        }
    )
    st.dataframe(
        tbl.style.format({"Cash Flow (€)": "{:,.0f}", "Discount Factor": "{:.4f}",
                          "Discounted CF (€)": "{:,.0f}", "Cumulative Discounted (€)": "{:,.0f}"}),
        use_container_width=True, hide_index=True,
    )

    pb_simple = find_payback(cum_simple, cfs)
    pb_disc = find_payback(cum_disc, pvs)
    npv_val = sum(pvs)

    m1, m2, m3 = st.columns(3)
    m1.metric("Simple payback", f"{pb_simple:.2f} yrs" if pb_simple else "Never")
    m2.metric("Discounted payback", f"{pb_disc:.2f} yrs" if pb_disc else "Never")
    m3.metric("NPV (context)", f"€{npv_val:,.0f}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=cum_simple, name="Cumulative simple",
                             mode="lines+markers", line=dict(color="#90CAF9", width=3)))
    fig.add_trace(go.Scatter(x=years, y=cum_disc, name="Cumulative discounted",
                             mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="#C62828")
    if pb_disc:
        fig.add_vline(x=pb_disc, line_dash="dot", line_color="#0B3D91",
                      annotation_text=f"Disc. payback {pb_disc:.2f}y", annotation_position="top")
    fig.update_layout(xaxis_title="Year", yaxis_title="€", height=430,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=50, b=40))
    st.plotly_chart(fig, use_container_width=True)

    if pb_disc is None:
        st.error("⚠️ Discounted payback is **never reached** within the project's life → **REJECT** "
                 "(this also means NPV is negative).")
    elif pb_disc <= cutoff:
        st.success(f"✅ Discounted payback of **{pb_disc:.2f} years** ≤ cutoff {cutoff:.1f} → **ACCEPT** "
                   f"on this screen. (Simple payback was {pb_simple:.2f} yrs.)")
    else:
        st.warning(f"🟠 Discounted payback of **{pb_disc:.2f} years** > cutoff {cutoff:.1f} → **REJECT** "
                   f"on this screen, even though it does eventually recover.")

    st.caption("Reminder: discounted payback still ignores cash flows after the recovery point — "
               "confirm the decision with NPV & IRR.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 5 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. Discounted payback differs from simple payback because it…",
            "options": [
                "Ignores the time value of money",
                "Discounts each cash flow before accumulating",
                "Uses accounting profit instead of cash",
                "Counts cash flows after payback",
            ],
            "answer": 1,
            "why": "Discounted payback discounts every cash flow to present value before finding the recovery point.",
        },
        {
            "q": "2. Compared with simple payback, discounted payback is always…",
            "options": ["Shorter", "The same", "Longer or equal", "Negative"],
            "answer": 2,
            "why": "Discounting shrinks the inflows, so recovery takes at least as long — discounted ≥ simple.",
        },
        {
            "q": "3. A limitation that discounted payback STILL shares with simple payback is that it…",
            "options": [
                "Ignores the time value of money",
                "Ignores cash flows occurring after the payback point",
                "Cannot handle uneven cash flows",
                "Requires no discount rate",
            ],
            "answer": 1,
            "why": "Both methods stop counting once the outlay is recovered, ignoring later cash flows.",
        },
        {
            "q": "4. If a project never reaches discounted payback within its life, its NPV is…",
            "options": ["Positive", "Zero", "Negative", "Undefined"],
            "answer": 2,
            "why": "Failing to recover the outlay in discounted terms means the sum of discounted flows is negative — a negative NPV.",
        },
        {
            "q": "5. Discounted payback is best used as…",
            "options": [
                "The sole decision criterion",
                "A time-value-aware liquidity/risk screen alongside NPV & IRR",
                "A replacement for cash-flow forecasting",
                "A measure of total shareholder value",
            ],
            "answer": 1,
            "why": "It's a more realistic risk screen, but final decisions should rest on NPV/IRR.",
        },
    ]

    with st.form("quiz_2_3"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q23_{i}")
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
            st.success("🏆 Perfect! You understand exactly what discounting adds to the payback method.")
        elif pct >= 60:
            st.info("👍 Good work — continue to **2.4 · Profitability Index (PI)**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — focus on what discounted payback fixes vs still misses.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `2.2 · Internal Rate of Return (IRR & MIRR)`")
with cnext:
    st.markdown("**Next:** `2.4 · Profitability Index (PI)` ➡️")
st.caption("Business Case section · Page 2.3 · Built with Streamlit")
