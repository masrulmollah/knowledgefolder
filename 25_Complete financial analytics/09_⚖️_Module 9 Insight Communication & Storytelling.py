import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

def _sec(title, icon=""):
    st.markdown(f"### {icon} {title}")
    st.markdown("---")

def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans: st.success("✅ Correct!")
        else: st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def show():
    st.title("📣 Module 9: Insight Communication & Data Storytelling")
    st.caption("Turn numbers into decisions — frameworks, chart design, executive narratives, and board-ready communication")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Story Builder", "📊 Chart Design Lab", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Why Communication Is the Last Mile of Analytics", "📐")
        st.markdown("""
> *"An insight no one acts on is just an interesting fact. Communication is what converts analysis into value."*

Finance professionals who can analyse AND communicate are exponentially more impactful than those who can only do one.
The best analysis in the world, buried in a 40-tab Excel file or a wall of numbers, creates zero value.
        """)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**The SCR (Situation → Complication → Resolution) Framework**

Originally developed by Barbara Minto (McKinsey), SCR forces a logical narrative arc:

| Layer | Question | Example |
|-------|----------|---------|
| **Situation** | What is the agreed current state? | "Q3 EBITDA closed at $94M." |
| **Complication** | What has changed or is at risk? | "This is $42M (31%) below budget." |
| **Resolution** | What should we do about it? | "Three actions will recover $28M in Q4." |

**Why it works:** It respects the audience's time. Most executives want the "so what?" first,
not a data tour. SCR forces the analyst to decide what matters before presenting.

**Common failure mode:** Starting with the situation and never reaching the resolution.
Executives call this "giving me data, not insight."
            """)
        with c2:
            st.markdown("""
**The Pyramid Principle (Minto)**

Structure all financial communication top-down:

```
Top:    Governing Thought (The single key message)
         ↓
Middle: Supporting Arguments (3–4 key findings)
         ↓
Base:   Data & Evidence (Charts, tables, calculations)
```

*Example:*
- **Governing Thought:** "We must act on three operational gaps or miss FY target by $25M."
- **Argument 1:** Volume is tracking 8% below plan in two regions.
- **Argument 2:** Raw material costs are $12M above budget due to supplier concentration.
- **Argument 3:** SG&A run-rate must be cut by $4M to offset the revenue gap.
- **Evidence:** P&L bridge, regional split, cost breakdown tables.

**Key rule:** The governing thought should fit in one sentence. If it doesn't, the analysis isn't finished.
            """)

        _sec("The So-What? Test & Insight Hierarchy", "🎯")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Insight Hierarchy — 4 Levels of Value:**

| Level | Type | Example | Value |
|-------|------|---------|-------|
| 1 | Observation | "Revenue is $482M" | None |
| 2 | Variance | "Revenue is $18M below budget" | Low |
| 3 | Diagnosis | "Miss is 100% volume-driven — price is ahead" | Medium |
| 4 | Recommendation | "Reactivate 3 churned accounts by Friday to recover $12M" | High |

**Always aim for Level 4.** Most finance reports stop at Level 2.

**The So-What? Test — apply to every slide:**
1. Write down the data point.
2. Ask: "So what does this mean for the business?"
3. If you can't answer in one sentence → the analysis is incomplete.
4. The answer to "So what?" becomes the chart title or headline.
            """)
        with c2:
            st.markdown("""
**The Insight → Action → Outcome Framework:**

Every insight must be connected to an action and an expected outcome:

```
Insight:  Revenue mix is shifting to lower-margin products.
          (Measured: Premium SKUs down from 42% to 31% of mix)

Action:   Redesign sales incentive to reward margin, not volume.
          Target: premium SKUs back to 40% within 2 quarters.

Outcome:  +1.8pp GM improvement = +$9M EBITDA at current revenue.
          Measurable by Q2 mix report.
```

**Why this matters:**
Without the Action and Outcome, the Insight is just an observation.
Without the Insight and Outcome, the Action has no justification.
Without the Insight and Action, the Outcome has no owner.
All three are required for a complete, actionable financial narrative.
            """)

        _sec("Chart Design Principles for Finance", "📊")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Chart Selection Guide:**
| Purpose | Best Chart | Avoid |
|---------|-----------|-------|
| Show a trend over time | Line / bar | Pie, donut |
| Build from revenue to profit | Waterfall | Stacked bar |
| Compare many categories | Horizontal bar | Vertical if > 8 labels |
| Show two variables' relationship | Scatter | Line |
| Show distribution | Histogram / box plot | Bar chart |
| Show performance vs. target | Bullet chart | Simple bar |
| Show correlation matrix | Heat map | Table |
| Rank by magnitude | Sorted bar | Unsorted |

**Colour rules:**
- 🔴 Red = bad (miss, decline, risk)
- 🟢 Green = good (beat, growth, improvement)
- ⬜ Grey = context / prior period
- 🔵 Blue = current / focus
- Use ONE highlight colour per chart maximum
            """)
        with c2:
            st.markdown("""
**The 10 Chart Design Rules for Finance:**
1. **Title = insight, not metric.** "Volume miss drives 80% of EBITDA shortfall" not "EBITDA Analysis"
2. **Lead with the most important number** — top left corner of the eye's natural path
3. **Remove all chart junk** — gridlines, borders, 3D effects, shadows, unnecessary legends
4. **Annotate the key data point** — don't make the audience find the insight themselves
5. **Start Y-axis at zero** for bar charts (truncated axes are misleading)
6. **Sort bars** by value unless time-ordering matters
7. **Limit colours** to 2–3 maximum; use grey for everything non-essential
8. **Round all numbers** — $482.3471M becomes $482M in board communication
9. **Use consistent scales** when comparing charts side-by-side
10. **Test with a stranger** — if they can't read the key message in 8 seconds, redesign it

**Table design:**
- Highlight the total row
- Right-align all numbers
- Use consistent decimal places
- Conditional formatting for variances (red/green)
- Never use more than 5 columns in a board table
            """)

        st.info("💡 **The dual test:** Every piece of financial communication should pass two tests: "
                "(1) The Grandmother Test — could a non-finance person understand the key message? "
                "(2) The CEO Test — could the CEO make a decision from this in 60 seconds?")

    # ── STORY BUILDER ─────────────────────────────────────────────────────────
    with tab2:
        _sec("Interactive SCR Narrative Builder", "🧮")
        st.markdown("""
Build a structured management narrative using the **SCR framework**.
Fill in the fields below and generate a board-ready paragraph.
        """)

        c1, c2 = st.columns(2)
        with c1:
            metric_name  = st.text_input("Metric being reported:",       value="EBITDA", key="sb_metric")
            actual_val   = st.number_input("Actual value ($M):",          value=94.0,  step=1.0, key="sb_act")
            budget_val   = st.number_input("Budget / Target value ($M):", value=136.0, step=1.0, key="sb_bud")
            period_label = st.text_input("Period:",                       value="Q3 2024", key="sb_period")
        with c2:
            primary_driver = st.text_input("Primary driver of variance:",
                                           value="Volume shortfall in Mid-Market (-$22M) and COGS inflation (+$18M)",
                                           key="sb_driver")
            action1 = st.text_input("Recommended action 1:",
                                    value="Reactivate 3 churned Mid-Market accounts — CFO to approve 10% retention offer",
                                    key="sb_a1")
            action2 = st.text_input("Recommended action 2:",
                                    value="Accelerate alternative supplier RFP to reduce raw material cost exposure",
                                    key="sb_a2")
            action3 = st.text_input("Recommended action 3:",
                                    value="Freeze discretionary SG&A for Q4; target $4M run-rate reduction",
                                    key="sb_a3")
            recovery_val = st.number_input("Expected recovery ($M):", value=28.0, step=1.0, key="sb_rec")

        variance   = actual_val - budget_val
        var_pct    = variance / budget_val * 100 if budget_val != 0 else 0
        direction  = "below" if variance < 0 else "above"
        signal     = "miss" if variance < 0 else "beat"

        st.markdown("---")
        st.markdown("#### 📋 Generated SCR Narrative")

        narrative = f"""
**SITUATION —** {metric_name} for {period_label} closed at **${actual_val:.0f}M** against a budget of **${budget_val:.0f}M**.

**COMPLICATION —** This represents a **${abs(variance):.0f}M ({abs(var_pct):.0f}%) {signal}** {direction} budget. \
The primary driver of this variance is: *{primary_driver}*. \
Without corrective action, the full-year {metric_name} target is at risk.

**RESOLUTION —** Three actions are recommended to recover approximately **${recovery_val:.0f}M** before year-end:
1. {action1}
2. {action2}
3. {action3}
        """

        st.markdown(
            f"<div style='background:#F0F7FF; border-left:4px solid #185FA5; border-radius:8px; "
            f"padding:20px 24px; font-size:14px; line-height:1.8;'>{narrative}</div>",
            unsafe_allow_html=True
        )

        # KPI summary card
        st.markdown("---")
        st.markdown("#### 📌 Executive KPI Summary Card")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric(f"{metric_name} — Actual",  f"${actual_val:.0f}M")
        c2.metric(f"{metric_name} — Budget",  f"${budget_val:.0f}M")
        c3.metric("Variance ($M)",  f"${variance:+.0f}M",
                  delta=f"{var_pct:+.0f}% vs budget", delta_color="inverse" if variance < 0 else "normal")
        c4.metric("Recovery Target", f"${recovery_val:.0f}M",
                  delta=f"Closes {recovery_val/abs(variance)*100:.0f}% of gap" if variance != 0 else "N/A")

        # Pyramid visual
        st.markdown("---")
        st.markdown("#### 🔺 Pyramid Structure of This Narrative")
        pyramid_levels = [
            ("🔺 Governing Thought",
             f"{metric_name} is ${abs(variance):.0f}M {direction} budget — {len([action1,action2,action3])} actions required to recover ${recovery_val:.0f}M.",
             "#0C447C", "white"),
            ("📊 Key Finding 1", f"Primary driver: {primary_driver[:80]}...", "#185FA5", "white"),
            ("📊 Key Finding 2", f"Recovery roadmap: ${recovery_val:.0f}M identified across 3 actionable levers.", "#2D7DD2", "white"),
            ("📋 Evidence Base", f"P&L variance analysis, PVM bridge, root-cause diagnostics — see supporting appendix.", "#B5D4F4", "#0C447C"),
        ]
        for level, text, bg, fg in pyramid_levels:
            st.markdown(
                f"<div style='background:{bg}; color:{fg}; border-radius:8px; padding:12px 18px; "
                f"margin-bottom:6px;'><strong>{level}:</strong> {text}</div>",
                unsafe_allow_html=True
            )

    # ── CHART DESIGN LAB ──────────────────────────────────────────────────────
    with tab3:
        _sec("Chart Design Lab — Before & After", "📊")
        st.markdown("""
Compare **poor chart design** (common mistakes) against **best-practice design** (board-ready).
Select a scenario to see the transformation.
        """)

        scenario = st.selectbox("Choose scenario:", [
            "EBITDA Variance Analysis",
            "Regional Revenue Performance",
            "Cost Structure Trend",
            "Customer Segment Profitability",
        ])

        np.random.seed(42)

        if scenario == "EBITDA Variance Analysis":
            categories = ["Revenue\nMiss", "COGS\nOvershoot", "SG&A\nOver-run", "R&D\nSaving", "Net\nImpact"]
            values     = [-18, -16, -8, 6, -36]

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**❌ Poor Design — Common Mistakes**")
                fig_bad = go.Figure(go.Bar(
                    x=categories, y=values,
                    marker_color="#7B68EE",  # one colour for everything
                    name="Variance"
                ))
                fig_bad.update_layout(
                    title="EBITDA Q3 2024",  # no insight in title
                    template="plotly_white", height=360,
                    showlegend=True,  # unnecessary legend
                )
                st.plotly_chart(fig_bad, use_container_width=True)
                st.error("❌ Issues: No insight in title · Same colour for all bars (no signal) · "
                         "No annotation of key message · Legend adds no value · Y-axis label missing")

            with col2:
                st.markdown("**✅ Best Practice — Board-Ready Design**")
                fig_good = go.Figure(go.Bar(
                    x=categories, y=values,
                    marker_color=["#E24B4A","#E24B4A","#E24B4A","#1D9E75","#E24B4A"],
                    text=[f"${v:+}M" for v in values],
                    textposition="outside",
                    showlegend=False
                ))
                fig_good.add_hline(y=0, line_color="black", line_width=0.8)
                fig_good.update_layout(
                    title="COGS inflation and volume miss drive $36M EBITDA shortfall in Q3",
                    template="plotly_white", height=360,
                    yaxis_title="Variance vs. Budget ($M)",
                    annotations=[dict(x=3, y=8, text="Only saving:<br>R&D deferral",
                                      showarrow=True, arrowhead=2, font=dict(color="#1D9E75"))]
                )
                st.plotly_chart(fig_good, use_container_width=True)
                st.success("✅ Insight in title · Red = negative / Green = positive · "
                           "Values labelled directly · Key data point annotated · Clean, no clutter")

        elif scenario == "Regional Revenue Performance":
            regions  = ["North America", "Europe", "Asia Pacific", "Latin America", "MEA"]
            actual   = [210, 148, 95, 52, 38]
            budget   = [195, 160, 105, 48, 42]
            variance = [a - b for a, b in zip(actual, budget)]

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**❌ Poor Design**")
                fig_bad = go.Figure()
                fig_bad.add_trace(go.Bar(x=regions, y=actual,  name="Actual",  marker_color="#FF6B6B"))
                fig_bad.add_trace(go.Bar(x=regions, y=budget,  name="Budget",  marker_color="#4ECDC4"))
                fig_bad.update_layout(title="Revenue by Region", barmode="group",
                                       template="plotly_white", height=360)
                st.plotly_chart(fig_bad, use_container_width=True)
                st.error("❌ Issues: Grouped bars hard to read variance · Clashing colours · "
                         "Title is a label, not an insight · Audience must calculate gap mentally")

            with col2:
                st.markdown("**✅ Best Practice**")
                sorted_idx = np.argsort(variance)
                sorted_reg = [regions[i] for i in sorted_idx]
                sorted_var = [variance[i] for i in sorted_idx]
                fig_good = go.Figure(go.Bar(
                    y=sorted_reg, x=sorted_var, orientation="h",
                    marker_color=["#1D9E75" if v >= 0 else "#E24B4A" for v in sorted_var],
                    text=[f"${v:+}M" for v in sorted_var], textposition="outside",
                    showlegend=False
                ))
                fig_good.add_vline(x=0, line_color="black", line_width=0.8)
                fig_good.update_layout(
                    title="Europe and Asia Pacific drag total revenue $22M below plan",
                    template="plotly_white", height=360, xaxis_title="Variance vs. Budget ($M)"
                )
                st.plotly_chart(fig_good, use_container_width=True)
                st.success("✅ Variance shown directly · Sorted by magnitude · Horizontal labels readable · "
                           "Colour signals direction · Insight-led title")

        elif scenario == "Cost Structure Trend":
            years   = [2020, 2021, 2022, 2023, 2024]
            cogs_p  = [60.2, 59.8, 61.4, 58.9, 57.2]
            sga_p   = [20.1, 19.8, 20.5, 20.2, 20.0]
            rd_p    = [8.8,  9.0,  9.2,  8.8,  7.1]

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**❌ Poor Design**")
                fig_bad = go.Figure()
                for label, vals, colour in [("COGS%", cogs_p, "red"), ("SG&A%", sga_p, "green"), ("R&D%", rd_p, "blue")]:
                    fig_bad.add_trace(go.Scatter(x=years, y=vals, name=label,
                                                  mode="lines+markers", line=dict(color=colour, width=1)))
                fig_bad.update_layout(title="Cost % Analysis 2020–2024",
                                       template="plotly_white", height=360)
                st.plotly_chart(fig_bad, use_container_width=True)
                st.error("❌ Issues: No insight in title · All lines same visual weight · "
                         "No annotation of key trend · Default colours · Y-axis doesn't contextualise")

            with col2:
                st.markdown("**✅ Best Practice**")
                fig_good = go.Figure()
                fig_good.add_trace(go.Scatter(x=years, y=cogs_p, name="COGS % Rev",
                                               mode="lines+markers", line=dict(color="#185FA5", width=2.5),
                                               marker=dict(size=7)))
                fig_good.add_trace(go.Scatter(x=years, y=sga_p, name="SG&A % Rev",
                                               mode="lines+markers", line=dict(color="#AAAAAA", width=1.5, dash="dot"),
                                               marker=dict(size=5)))
                fig_good.add_trace(go.Scatter(x=years, y=rd_p, name="R&D % Rev",
                                               mode="lines+markers", line=dict(color="#E24B4A", width=2),
                                               marker=dict(size=7)))
                fig_good.add_annotation(x=2024, y=57.2, text="COGS: −3pp\nimprovement",
                                         showarrow=True, arrowhead=2, font=dict(color="#185FA5", size=11))
                fig_good.add_annotation(x=2024, y=7.1, text="R&D under-invested\nvs. peers",
                                         showarrow=True, arrowhead=2, ax=40, font=dict(color="#E24B4A", size=11))
                fig_good.update_layout(
                    title="COGS efficiency improving but R&D spend falling below industry threshold",
                    template="plotly_white", height=360, yaxis_title="% of Revenue",
                    legend=dict(orientation="h", y=1.02)
                )
                st.plotly_chart(fig_good, use_container_width=True)
                st.success("✅ Key lines emphasised · Grey for context · Insight-led title · "
                           "Annotations explain both the positive and the concern")

        else:  # Customer Segment Profitability
            segs     = ["Enterprise", "Mid-Market", "SMB", "E-commerce"]
            rev      = [250, 180, 95, 62]
            gm_pct   = [52, 44, 38, 28]
            net_cm   = [88, 52, 22, -8]

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**❌ Poor Design**")
                fig_bad = go.Figure(go.Pie(labels=segs, values=rev,
                                            hole=0, textinfo="label+percent"))
                fig_bad.update_layout(title="Revenue by Segment",
                                       template="plotly_white", height=360)
                st.plotly_chart(fig_bad, use_container_width=True)
                st.error("❌ Issues: Pie chart shows revenue only — hides margin story completely · "
                         "Cannot compare magnitudes in a pie · No actionable insight possible")

            with col2:
                st.markdown("**✅ Best Practice**")
                fig_good = px.scatter(
                    pd.DataFrame({"Segment": segs, "Revenue ($M)": rev,
                                  "GM %": gm_pct, "Net CM ($M)": net_cm}),
                    x="Revenue ($M)", y="GM %", size=[max(abs(v), 5) for v in net_cm],
                    color=["🔴 Loss" if v < 0 else "✅ Profit" for v in net_cm],
                    text="Segment",
                    color_discrete_map={"🔴 Loss": "#E24B4A", "✅ Profit": "#1D9E75"},
                    title="E-commerce: highest revenue growth but only segment destroying margin",
                    template="plotly_white", height=360,
                )
                fig_good.update_traces(textposition="top center")
                fig_good.add_hline(y=35, line_dash="dash", line_color="gray",
                                    annotation_text="Minimum viable GM% threshold")
                st.plotly_chart(fig_good, use_container_width=True)
                st.success("✅ Shows revenue AND margin simultaneously · Exposes hidden loss-maker · "
                           "Insight-led title directs action · Threshold line gives context")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Building the Board Pack Narrative — Consumer Goods Group H1 2024", "🧪")
        st.markdown("""
**Situation:** You are the Group FP&A Director. H1 2024 results have closed.
The CEO needs a 3-minute verbal briefing for the Board, supported by one summary slide.
Your job: take a full dataset and compress it into a structured, insight-led narrative
that enables the Board to make a decision — not just receive information.
        """)

        st.markdown("**Step 1 — The Raw Numbers (what most analysts stop at)**")
        raw_data = pd.DataFrame({
            "Metric":        ["Revenue", "Gross Profit", "SG&A", "EBITDA",
                              "FCF", "DSO", "Inventory Days", "Net Debt"],
            "H1 2024":       [542, 238, 108, 130, 84, 48, 52, 312],
            "H1 2023":       [498, 217,  96, 121, 96, 44, 45, 285],
            "H1 Budget":     [560, 246, 112, 134, 95, 45, 50, 300],
            "vs. Budget ($M/days)": [-18, -8, -4, -4, -11, "+3", "+2", "+12"],
            "vs. Prior Year": ["+$44M", "+$21M", "+$12M", "+$9M", "-$12M", "+4d", "+7d", "+$27M"],
        })
        st.dataframe(raw_data, use_container_width=True, hide_index=True)
        st.caption("Raw numbers — data, not insight. A board cannot make a decision from this table alone.")

        st.markdown("**Step 2 — Apply the So-What Test to Each Line**")
        sowhat_data = pd.DataFrame({
            "Metric":     ["Revenue", "EBITDA", "FCF", "Working Capital", "Net Debt"],
            "Number":     ["$542M (−$18M vs budget)", "$130M (−$4M vs budget)",
                           "$84M (−$11M vs budget)", "DSO +3d, DIO +2d vs plan",
                           "$312M (+$12M vs budget)"],
            "So What?":   [
                "Revenue miss is 100% volume — price is +$6M ahead. Two regions are underperforming.",
                "EBITDA near budget despite revenue miss. Cost discipline is working.",
                "FCF materially below budget. Working capital build is consuming cash.",
                "Inventory and AR both above plan — $18M extra cash tied up.",
                "Leverage rising. Covenant headroom tightening if H2 FCF stays weak.",
            ],
            "Action Needed?": ["Yes — fix volume", "Monitor", "Yes — WC release", "Yes — DIO/DSO plan", "Yes — FCF recovery"],
        })
        st.dataframe(sowhat_data, use_container_width=True, hide_index=True)

        st.markdown("**Step 3 — Pyramid: The One-Page Board Narrative**")
        st.markdown(
            """
<div style='background:#0C447C; color:white; border-radius:12px; padding:18px 22px; margin-bottom:10px;'>
<strong>🔺 GOVERNING THOUGHT (the single message):</strong><br>
H1 2024: EBITDA is near plan thanks to cost control, but FCF is $11M short due to working capital build —
and volume recovery is essential to protect the full-year target.
</div>
            """, unsafe_allow_html=True
        )

        cols_pyr = st.columns(3)
        findings = [
            ("📊 Finding 1 — Revenue", "#185FA5",
             "Revenue is $18M (3%) below budget. The miss is entirely volume-driven — "
             "price realisation is $6M ahead of plan. Europe (−$12M) and Asia Pacific (−$8M) "
             "are the primary underperforming regions."),
            ("💧 Finding 2 — FCF", "#1D9E75",
             "FCF of $84M is $11M below budget. EBITDA is near plan, so the shortfall "
             "is working capital driven: DSO +3 days and DIO +2 days vs. plan = $18M extra cash tied up "
             "in receivables and inventory."),
            ("⚠️ Finding 3 — Risk", "#BA7517",
             "Net debt has risen to $312M (+$12M vs. plan). Leverage is 2.4× EBITDA vs. "
             "covenant limit of 3.0×. If H2 FCF does not recover, headroom will narrow "
             "to <0.3× by December — covenant monitoring required."),
        ]
        for col, (title, bg, body) in zip(cols_pyr, findings):
            with col:
                st.markdown(
                    f"<div style='background:{bg}; color:white; border-radius:10px; "
                    f"padding:14px; height:180px; font-size:12px; line-height:1.6;'>"
                    f"<strong>{title}</strong><br><br>{body}</div>",
                    unsafe_allow_html=True
                )

        st.markdown("**Step 4 — The Three Actions (Resolution)**")
        actions_df = pd.DataFrame({
            "Priority": ["1 — Urgent", "2 — Urgent", "3 — Monitor"],
            "Action": [
                "Volume recovery plan: reactivate 5 deferred accounts in Europe and APAC — target $15M H2 revenue uplift",
                "Working capital sprint: 5-day DSO reduction programme + DIO reduction in 3 product categories",
                "Net debt monitoring: weekly covenant headroom tracking; pre-agree RCF extension with bank if needed",
            ],
            "Owner": ["CCO + Regional GMs", "CFO + Supply Chain Director", "CFO + Treasury"],
            "Deadline": ["31 July 2024", "30 September 2024", "Ongoing"],
            "Expected Impact": ["+$15M revenue / +$3M EBITDA", "$18M cash release", "Covenant protection"],
        })
        st.dataframe(actions_df, use_container_width=True, hide_index=True)

        st.markdown("**Step 5 — Visual: H1 Performance Summary (Board Slide)**")
        fig_board = go.Figure()
        metrics_b = ["Revenue", "Gross Profit", "EBITDA", "FCF"]
        budget_b  = [560, 246, 134, 95]
        actual_b  = [542, 238, 130, 84]
        fig_board.add_trace(go.Bar(x=metrics_b, y=budget_b, name="Budget",
                                    marker_color="#D5E8F5", width=0.35))
        fig_board.add_trace(go.Bar(x=metrics_b, y=actual_b, name="Actual",
                                    marker_color=["#E24B4A" if a < b else "#1D9E75"
                                                  for a, b in zip(actual_b, budget_b)],
                                    width=0.35, text=[f"${v}M" for v in actual_b],
                                    textposition="outside"))
        fig_board.update_layout(
            title="H1 2024: EBITDA near budget — FCF shortfall requires working capital action",
            barmode="group", template="plotly_white", height=400,
            yaxis_title="$M", legend=dict(orientation="h", y=1.02)
        )
        st.plotly_chart(fig_board, use_container_width=True)

        st.success("""
**CEO Verbal Briefing Script (3 minutes):**

"Board, H1 2024 EBITDA landed at $130M — $4M short of budget, but this is largely offset
by cost discipline and price realisation that's running $6M ahead.

The real story is FCF. At $84M, we're $11M below plan — not because of earnings, but because
working capital has built by $18M above plan. DSO and inventory days are both slightly elevated.
This is fixable, and the team has a concrete 90-day plan to release that cash.

Our net leverage is 2.4×, inside covenant but trending upward. The CFO is monitoring weekly
and has pre-agreed a contingency RCF extension with our bank.

Three decisions needed from the Board today:
1. Approve the Volume Recovery Plan targeting $15M H2 uplift — CCO to lead.
2. Endorse the Working Capital Sprint Programme — CFO target $18M cash release by Q3.
3. Note the covenant monitoring protocol — CFO to report back monthly.

Full pack is in the appendix. Do you have questions before we move to decisions?"
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 9 Quiz", "❓")
        _quiz("1. In the SCR framework, what does the 'Complication' layer represent?",
              ["The supporting data and evidence",
               "What has changed, gone wrong, or is at risk — the tension that requires action",
               "The background context and current state",
               "The recommended next steps"],
              "What has changed, gone wrong, or is at risk — the tension that requires action", "fa_m9q1")
        st.divider()
        _quiz("2. A Level 4 insight (the highest value) is best described as:",
              ["A data observation with a chart",
               "A variance calculation showing budget vs. actual",
               "A diagnosis of root cause",
               "A specific recommendation with an expected outcome tied to a decision-maker"],
              "A specific recommendation with an expected outcome tied to a decision-maker", "fa_m9q2")
        st.divider()
        _quiz("3. Which chart type is most appropriate for showing how revenue builds to net profit?",
              ["Pie chart", "Waterfall chart", "Line chart", "Scatter plot"],
              "Waterfall chart", "fa_m9q3")
        st.divider()
        _quiz("4. A chart title that reads 'Revenue Analysis Q3 2024' is a problem because:",
              ["It is too short",
               "It is a label, not an insight — the audience must interpret the chart themselves",
               "It should include a subtitle",
               "Revenue analysis is not a valid financial topic"],
              "It is a label, not an insight — the audience must interpret the chart themselves", "fa_m9q4")
        st.divider()
        _quiz("5. The Pyramid Principle in finance communication means:",
              ["Start with the most detailed data and build to the conclusion",
               "Use exactly three levels of analysis in every report",
               "Lead with the key message, then support it with arguments, then evidence",
               "Always present three scenarios: best, base, and worst case"],
              "Lead with the key message, then support it with arguments, then evidence", "fa_m9q5")
        st.divider()
        _quiz("6. The Insight → Action → Outcome framework requires all three elements because:",
              ["Regulators require all three in financial reports",
               "Without Action and Outcome, an Insight is just an observation with no business value",
               "It is a legal requirement in board reporting",
               "Outcomes replace the need for further analysis"],
              "Without Action and Outcome, an Insight is just an observation with no business value", "fa_m9q6")
        st.divider()
        _quiz("7. When should you use a horizontal bar chart instead of a vertical bar chart?",
              ["When comparing only 2 categories",
               "When the category labels are long or there are more than 6–8 items",
               "When the Y-axis represents time",
               "When all values are positive"],
              "When the category labels are long or there are more than 6–8 items", "fa_m9q7")