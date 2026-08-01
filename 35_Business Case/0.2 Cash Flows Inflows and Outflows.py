# ============================================================================
#  BUSINESS CASE — Section
#  Page 0.2 · Cash Flows: Inflows & Outflows
#  Streamlit multi-page app module
# ============================================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="0.2 · Cash Flows: Inflows & Outflows",
    page_icon="💰",
    layout="wide",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLES  (shared look with 0.1)
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
        .in  { color:#1B7F3B; font-weight:700; }
        .out { color:#C62828; font-weight:700; }
        .muted{ color:#5A6472; }
        .chip-in {
            background:#E7F6EC; color:#1B7F3B; border:1px solid #B7E1C4;
            border-radius:20px; padding:4px 12px; font-size:.8rem; font-weight:700;
            display:inline-block; margin:3px;
        }
        .chip-out {
            background:#FDECEC; color:#C62828; border:1px solid #F4C0C0;
            border-radius:20px; padding:4px 12px; font-size:.8rem; font-weight:700;
            display:inline-block; margin:3px;
        }
        .chip-ignore {
            background:#F0F0F0; color:#5A6472; border:1px solid #D5D5D5;
            border-radius:20px; padding:4px 12px; font-size:.8rem; font-weight:700;
            display:inline-block; margin:3px;
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
        <span class="bc-tag">PART 0 · FOUNDATIONS</span>
        <h1>0.2 · Cash Flows: Inflows &amp; Outflows</h1>
        <p>The raw material of every business case. Learn which cash flows count,
        which to ignore, and how to build a clean, incremental, year-by-year cash-flow model.</p>
        <div class="bc-pill">📘 Theory &nbsp;•&nbsp; 🧮 Worked Example &nbsp;•&nbsp; 🎛️ Interactive Lab &nbsp;•&nbsp; ✅ Quiz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("💡 Learning goal: Confidently identify and classify relevant cash flows — applying the "
           "incremental principle, handling sunk & opportunity costs, working capital, and terminal value.")

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
    st.subheader("1 · What Counts as a Cash Flow?")
    st.markdown(
        """
        <div class="bc-key">
        A business case is built on <b>cash</b>, not accounting profit. We care about the actual
        movement of money — <span class="in">inflows</span> (cash coming in: savings, extra revenue,
        salvage) and <span class="out">outflows</span> (cash going out: capex, opex, working capital).
        Non-cash items like <b>depreciation</b> are <i>not</i> cash flows — though they matter
        indirectly through their <b>tax shield</b>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="bc-card">
            <h4>💚 Typical INFLOWS</h4>
            <ul>
              <li>Incremental <b>revenue</b> from new sales/capacity</li>
              <li><b>Cost savings</b> — labour, energy, wastage, maintenance</li>
              <li><b>Salvage / residual value</b> of the asset at the end</li>
              <li><b>Working-capital release</b> at project close</li>
              <li><b>Tax savings</b> from depreciation (the tax shield)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="bc-card">
            <h4>❤️ Typical OUTFLOWS</h4>
            <ul>
              <li><b>Capital expenditure</b> (Capex) — the initial investment</li>
              <li><b>Operating costs</b> (Opex) — running, maintenance, licences</li>
              <li><b>Increase in working capital</b> (inventory, receivables)</li>
              <li><b>Installation, training &amp; commissioning</b> costs</li>
              <li><b>Taxes</b> payable on incremental profit</li>
            </ul>
            </div>
            """, unsafe_allow_html=True,
        )

    st.subheader("2 · The Golden Rule — Use INCREMENTAL Cash Flows")
    st.markdown(
        "Only include cash flows that **change as a direct result of the decision**. "
        "Compare the world **with** the project against the world **without** it (the base case)."
    )
    st.latex(r"\text{Incremental CF} = \text{Cash Flow}_{\text{with project}} - \text{Cash Flow}_{\text{without project}}")

    st.subheader("3 · Four Cash Flows People Get Wrong")
    rules = [
        ("🚫 Sunk costs — IGNORE",
         "Money already spent and unrecoverable (e.g. a feasibility study done last year). "
         "It doesn't change with the decision, so it never belongs in the analysis."),
        ("✅ Opportunity costs — INCLUDE",
         "The value of the next-best use you give up (e.g. renting out the warehouse you'll now use "
         "for the new line). It's a real economic cost even though no cash is paid."),
        ("✅ Working capital — INCLUDE (and release it)",
         "An investment often locks up cash in inventory & receivables. Treat the increase as an "
         "outflow when it happens, and the release as an inflow at the end of the project."),
        ("✅ Terminal / salvage value — INCLUDE",
         "Cash from selling the asset (net of tax) or the ongoing value at the end of the horizon. "
         "Often a large, easy-to-forget inflow in the final year."),
    ]
    for title, body in rules:
        st.markdown(f"<div class='bc-step'><b>{title}</b><br>{body}</div>", unsafe_allow_html=True)

    st.subheader("4 · The Depreciation Trap")
    st.markdown(
        """
        Depreciation is **not** a cash outflow — it's an accounting allocation. But because it's
        **tax-deductible**, it reduces the tax you pay, creating a real cash inflow called the
        **tax shield**:
        """
    )
    st.latex(r"\text{Tax Shield} = \text{Depreciation} \times \text{Tax Rate}")
    st.markdown(
        "<span class='muted'>So we <b>add back depreciation</b> after tax when converting profit to "
        "cash, or model the tax shield directly. We'll use this in the NPV pages.</span>",
        unsafe_allow_html=True,
    )

    st.subheader("5 · From Profit to Free Cash Flow")
    st.markdown("A common way to build the yearly operating cash flow:")
    st.latex(r"\text{Operating CF} = (\text{Revenue} - \text{Cash Costs}) \times (1 - t) + (\text{Depreciation} \times t)")
    st.markdown(
        """
        Then the **total project cash flow** each year is:
        """
    )
    st.latex(r"\text{Project CF} = \text{Operating CF} - \text{Capex} - \Delta\text{Working Capital} + \text{Salvage}")

    st.subheader("6 · A Standard Cash-Flow Timeline")
    tl = pd.DataFrame(
        {
            "Timing": ["Year 0", "Years 1 → n-1", "Year n (final)"],
            "Typical Inflows": ["—", "Savings / revenue, tax shield",
                                 "Savings + salvage value + working-capital release"],
            "Typical Outflows": ["Capex + initial working capital + install/training",
                                 "Opex + taxes + any top-up working capital",
                                 "Opex + taxes"],
        }
    )
    st.table(tl)

    with st.expander("🔑 Quick reference — INCLUDE vs IGNORE"):
        st.markdown(
            """
            | Item | Treatment |
            |------|-----------|
            | Initial capex | ✅ Outflow, Year 0 |
            | Incremental revenue / savings | ✅ Inflow |
            | Sunk cost (already spent) | 🚫 Ignore |
            | Opportunity cost | ✅ Include as outflow |
            | Allocated head-office overhead (unchanged) | 🚫 Ignore |
            | Additional overhead caused by project | ✅ Include |
            | Depreciation (as an expense) | 🚫 Not a cash flow |
            | Depreciation **tax shield** | ✅ Inflow |
            | Increase in working capital | ✅ Outflow |
            | Working-capital release at end | ✅ Inflow |
            | Salvage value (net of tax) | ✅ Inflow, final year |
            """
        )

# ============================================================================
# TAB 2 — WORKED EXAMPLE
# ============================================================================
with tab_example:
    st.subheader("🧮 Building Incremental Cash Flows — New Production Line")

    st.markdown(
        """
        <div class="bc-key">
        <b>Scenario.</b> A new line costs <b>€800,000</b> (Year 0) and needs <b>€100,000</b> of
        working capital upfront. It generates <b>€400,000</b> incremental revenue and
        <b>€180,000</b> cash operating costs per year for <b>4 years</b>. Depreciation is straight-line
        (<b>€200,000</b>/yr), tax is <b>30%</b>, salvage value is <b>€120,000</b>, and the working
        capital is recovered at the end. A €30,000 feasibility study was already paid last year.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Step 1 · Sort the items")
    colA, colB, colC = st.columns(3)
    colA.markdown("**Inflows**<br><span class='chip-in'>Revenue €400k/yr</span>"
                  "<span class='chip-in'>Salvage €120k</span>"
                  "<span class='chip-in'>WC release €100k</span>"
                  "<span class='chip-in'>Tax shield</span>", unsafe_allow_html=True)
    colB.markdown("**Outflows**<br><span class='chip-out'>Capex €800k</span>"
                  "<span class='chip-out'>WC €100k</span>"
                  "<span class='chip-out'>Opex €180k/yr</span>"
                  "<span class='chip-out'>Tax</span>", unsafe_allow_html=True)
    colC.markdown("**Ignore**<br><span class='chip-ignore'>Sunk study €30k</span>"
                  "<span class='chip-ignore'>Depreciation (as expense)</span>", unsafe_allow_html=True)

    st.markdown("#### Step 2 · Compute yearly operating cash flow")
    rev, opex, dep, tax_rate = 400_000, 180_000, 200_000, 0.30
    ebit = rev - opex - dep
    tax = ebit * tax_rate
    nopat = ebit - tax
    ocf = nopat + dep  # add back non-cash depreciation

    st.latex(rf"EBIT = 400{{,}}000 - 180{{,}}000 - 200{{,}}000 = €{ebit:,.0f}")
    st.latex(rf"Tax = {ebit:,.0f} \times 0.30 = €{tax:,.0f}")
    st.latex(rf"Operating\ CF = ({ebit:,.0f} - {tax:,.0f}) + 200{{,}}000 = €{ocf:,.0f}")

    st.markdown("#### Step 3 · Lay out the full incremental cash-flow table")
    salvage_net = 120_000 * (1 - tax_rate)  # simple net-of-tax salvage
    years = [0, 1, 2, 3, 4]
    capex = [-800_000, 0, 0, 0, 0]
    wc = [-100_000, 0, 0, 0, +100_000]
    op = [0, ocf, ocf, ocf, ocf]
    salv = [0, 0, 0, 0, salvage_net]
    net = [capex[i] + wc[i] + op[i] + salv[i] for i in range(5)]
    cum = pd.Series(net).cumsum().tolist()

    df = pd.DataFrame(
        {
            "Year": years,
            "Capex (€)": capex,
            "Working Capital (€)": wc,
            "Operating CF (€)": op,
            "Salvage net (€)": salv,
            "Net Cash Flow (€)": net,
            "Cumulative (€)": cum,
        }
    )
    st.dataframe(
        df.style.format({c: "{:,.0f}" for c in df.columns if c != "Year"}),
        use_container_width=True, hide_index=True,
    )

    st.info(f"🔎 Note the **€30,000 feasibility study is excluded** (sunk), the **working capital "
            f"€100k is an outflow in Year 0 and an inflow in Year 4**, and salvage is shown "
            f"net of tax (€{salvage_net:,.0f}).")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=net, name="Net cash flow",
                         marker_color=["#C62828"] + ["#1E88E5"] * 4))
    fig.add_trace(go.Scatter(x=years, y=cum, name="Cumulative",
                             mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    fig.add_hline(y=0, line_dash="dash", line_color="grey")
    fig.update_layout(title="Incremental cash-flow profile — new production line",
                      xaxis_title="Year", yaxis_title="€", height=420,
                      legend=dict(orientation="h", y=1.12), margin=dict(t=70, b=40))
    st.plotly_chart(fig, use_container_width=True)

    st.success("These clean incremental cash flows are exactly what we'll discount in the "
               "**NPV / IRR** pages. Garbage in = garbage out: getting this table right is the "
               "single most important step in any business case.")

# ============================================================================
# TAB 3 — INTERACTIVE LAB
# ============================================================================
with tab_lab:
    st.subheader("🎛️ Lab A · Classify the Cash Flow")
    st.markdown("Pick how each item should be treated in an incremental business case, then submit.")

    classify_items = [
        ("Cost of new machine purchased for the project", "Outflow (include)"),
        ("Market research paid for last year", "Ignore (sunk cost)"),
        ("Rent forgone on a warehouse now used by the project", "Outflow (include)"),
        ("Annual labour savings from automation", "Inflow (include)"),
        ("Depreciation charge (as an expense)", "Ignore (non-cash)"),
        ("Salvage value of equipment at end of life", "Inflow (include)"),
        ("Increase in inventory needed to run the line", "Outflow (include)"),
        ("Head-office overhead that does NOT change", "Ignore (not incremental)"),
    ]
    options = ["Inflow (include)", "Outflow (include)", "Ignore (sunk cost)",
               "Ignore (non-cash)", "Ignore (not incremental)"]

    with st.form("classify_form"):
        answers = []
        for i, (item, _) in enumerate(classify_items):
            ans = st.selectbox(f"{i+1}. {item}", options, index=None,
                               placeholder="Choose classification…", key=f"cls_{i}")
            answers.append(ans)
        c_sub = st.form_submit_button("✅ Check classifications")

    if c_sub:
        correct = 0
        for i, (item, sol) in enumerate(classify_items):
            # 'sunk', 'non-cash' and 'not incremental' all map to an Ignore family,
            # but we grade against the specific correct reason.
            if answers[i] == sol:
                correct += 1
                st.success(f"**{i+1}. Correct ✅** — {item} → *{sol}*")
            else:
                st.error(f"**{i+1}. Not quite ❌** — {item} → correct: *{sol}* "
                         f"(you chose: {answers[i] if answers[i] else '—'})")
        st.metric("Classification score", f"{correct} / {len(classify_items)}",
                  f"{correct/len(classify_items)*100:.0f}%")

    st.markdown("---")
    st.subheader("🎛️ Lab B · Build an Incremental Cash-Flow Model")
    st.markdown("Adjust the drivers and watch the yearly cash flows, operating CF, and cumulative "
                "profile update. Depreciation is handled as a **tax shield**, not a cash cost.")

    c1, c2, c3 = st.columns(3)
    with c1:
        capex0 = st.number_input("Capex — Year 0 (€)", min_value=0, value=800_000, step=50_000)
        wc0 = st.number_input("Initial working capital (€)", min_value=0, value=100_000, step=10_000)
    with c2:
        rev = st.number_input("Annual incremental revenue (€)", min_value=0, value=400_000, step=25_000)
        opex = st.number_input("Annual cash operating cost (€)", min_value=0, value=180_000, step=10_000)
    with c3:
        life = st.slider("Project life (years)", 1, 12, 4)
        tax_rate = st.slider("Tax rate (%)", 0, 50, 30) / 100.0

    c4, c5 = st.columns(2)
    with c4:
        salvage = st.number_input("Salvage value at end (€, pre-tax)", min_value=0, value=120_000, step=10_000)
    with c5:
        recover_wc = st.checkbox("Recover working capital in final year", value=True)

    # Straight-line depreciation over life (assume salvage not deducted for simplicity)
    dep = capex0 / life if life else 0

    def op_cf():
        ebit = rev - opex - dep
        tax = max(ebit, 0) * tax_rate  # no tax benefit modelled on losses here
        return (ebit - tax) + dep

    ocf = op_cf()
    salvage_net = salvage * (1 - tax_rate)

    yrs = list(range(0, life + 1))
    capex_row, wc_row, op_row, salv_row, net_row = [], [], [], [], []
    for y in yrs:
        cpx = -capex0 if y == 0 else 0
        if y == 0:
            wcf = -wc0
        elif y == life and recover_wc:
            wcf = wc0
        else:
            wcf = 0
        opf = 0 if y == 0 else ocf
        slv = salvage_net if y == life else 0
        capex_row.append(cpx); wc_row.append(wcf); op_row.append(opf); salv_row.append(slv)
        net_row.append(cpx + wcf + opf + slv)

    cum = pd.Series(net_row).cumsum().tolist()
    total_net = sum(net_row)

    lab_df = pd.DataFrame(
        {
            "Year": yrs,
            "Capex (€)": capex_row,
            "Working Capital (€)": wc_row,
            "Operating CF (€)": op_row,
            "Salvage net (€)": salv_row,
            "Net Cash Flow (€)": net_row,
            "Cumulative (€)": cum,
        }
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("Annual operating CF", f"€{ocf:,.0f}")
    m2.metric("Total net cash (undiscounted)", f"€{total_net:,.0f}")
    m3.metric("Depreciation / yr", f"€{dep:,.0f}")

    st.dataframe(
        lab_df.style.format({c: "{:,.0f}" for c in lab_df.columns if c != "Year"}),
        use_container_width=True, hide_index=True,
    )

    figl = go.Figure()
    figl.add_trace(go.Bar(x=yrs, y=net_row, name="Net cash flow",
                          marker_color=["#C62828"] + ["#1E88E5"] * life))
    figl.add_trace(go.Scatter(x=yrs, y=cum, name="Cumulative",
                              mode="lines+markers", line=dict(color="#0B3D91", width=3)))
    figl.add_hline(y=0, line_dash="dash", line_color="grey")
    figl.update_layout(xaxis_title="Year", yaxis_title="€", height=420,
                       legend=dict(orientation="h", y=1.12), margin=dict(t=50, b=40))
    st.plotly_chart(figl, use_container_width=True)

    st.caption("Reminder: still **undiscounted** here. Part 2 discounts these very cash flows "
               "to compute NPV, IRR and PI.")

# ============================================================================
# TAB 4 — QUIZ
# ============================================================================
with tab_quiz:
    st.subheader("✅ Check Your Understanding")
    st.markdown("Answer all 6 questions, then click **Submit** to see your score and explanations.")

    questions = [
        {
            "q": "1. A business case should be built on…",
            "options": ["Accounting profit", "Incremental cash flows",
                        "Depreciation charges", "Total historical revenue"],
            "answer": 1,
            "why": "We value cash, and only the incremental cash flows that change because of the decision.",
        },
        {
            "q": "2. A €30,000 study already paid for last year is a…",
            "options": ["Relevant outflow", "Opportunity cost",
                        "Sunk cost to be ignored", "Terminal value"],
            "answer": 2,
            "why": "It's already spent and unrecoverable — a sunk cost, excluded from the analysis.",
        },
        {
            "q": "3. Rent you give up by using your own warehouse for the project is a…",
            "options": ["Sunk cost", "Opportunity cost to include",
                        "Non-cash item to ignore", "Financing cash flow"],
            "answer": 1,
            "why": "The forgone rent is an opportunity cost — a real economic cost that must be included.",
        },
        {
            "q": "4. Why does depreciation matter to cash flow even though it isn't cash?",
            "options": [
                "It is a direct cash outflow",
                "It creates a tax shield that reduces tax paid",
                "It increases working capital",
                "It has no effect at all",
            ],
            "answer": 1,
            "why": "Depreciation is tax-deductible, so it lowers tax — the 'tax shield' = depreciation × tax rate.",
        },
        {
            "q": "5. How is working capital typically treated?",
            "options": [
                "Ignored entirely",
                "Outflow when invested, inflow (release) at the end",
                "Always an inflow",
                "Only an accounting entry, never cash",
            ],
            "answer": 1,
            "why": "An increase in working capital is an outflow; it is released as an inflow at project end.",
        },
        {
            "q": "6. Salvage value of an asset at the end of the project is…",
            "options": [
                "Ignored because it's non-cash",
                "An outflow in the final year",
                "An inflow (net of tax) in the final year",
                "A sunk cost",
            ],
            "answer": 2,
            "why": "Salvage is a real inflow, usually recognised net of tax in the final year.",
        },
    ]

    with st.form("quiz_0_2"):
        responses = []
        for i, item in enumerate(questions):
            choice = st.radio(item["q"], item["options"], index=None, key=f"q02_{i}")
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
            st.success("🏆 Excellent! You can now build a clean incremental cash-flow model.")
        elif pct >= 60:
            st.info("👍 Solid — review the misses, then continue to "
                    "**0.3 · Time Value of Money & Discount Rate**.")
        else:
            st.warning("📖 Revisit the **Theory** tab — nailing cash-flow classification is essential "
                       "before we start discounting.")

# ----------------------------------------------------------------------------
# FOOTER NAV
# ----------------------------------------------------------------------------
st.markdown("---")
cprev, cnext = st.columns([1, 1])
with cprev:
    st.markdown("⬅️ **Previous:** `0.1 · What is a Business Case?`")
with cnext:
    st.markdown("**Next:** `0.3 · Time Value of Money & Discount Rate` ➡️")
st.caption("Business Case section · Page 0.2 · Built with Streamlit")
