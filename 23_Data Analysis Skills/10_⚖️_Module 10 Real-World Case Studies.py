import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# NO st.set_page_config() — Homepage.py owns that call.

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
    st.title("🎯 Module 10: Capstone — Real-World Case Studies")
    st.caption("End-to-end analytics applied to realistic business problems")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Overview","🧮 Case 1: P&L Diagnostic","📊 Case 2: Working Capital",
        "🧪 Case 3: M&A Synergies","❓ Final Quiz",
    ])

    # ── OVERVIEW ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Capstone Case Studies", "🗺️")
        st.info("""
This module brings together every technique from Modules 1–9.
Each case study runs end-to-end: **raw data → analysis → insight → recommendation**,
exactly as you would present it in a real finance role.
        """)
        cases = pd.DataFrame({
            "Case": ["Case 1","Case 2","Case 3"],
            "Title":["Full P&L Diagnostic","Working Capital Optimisation","M&A Synergy Tracking"],
            "Business Problem":["EBITDA missed budget by $42M — root-cause and recovery plan",
                                 "Cash conversion cycle deteriorated 18 days — find the cash trap",
                                 "Post-merger Day 100 — are synergy targets on track?"],
            "Modules Applied":["1, 2, 3, 9","2, 3, 5, 9","2, 4, 5, 9"],
            "Deliverable":["EBITDA bridge + root-cause action plan",
                            "DSO/DPO/DIO improvement roadmap",
                            "Synergy dashboard + go/no-go recommendation"],
        })
        st.dataframe(cases, use_container_width=True, hide_index=True)

        st.markdown("**How to use these case studies:**")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
1. Read the business situation
2. Study the data presented
3. Form your own hypothesis first
4. Work through the interactive analysis
5. Compare your conclusion with the model answer
6. Revisit the relevant module for any gap areas
            """)
        with c2:
            st.markdown("""
**A complete analytical case includes:**
- Data quality check (Module 1)
- Descriptive stats on the data (Module 2)
- Root cause decomposition (Module 3)
- Forward-looking forecast (Module 4)
- Decision recommendation (Module 5)
- Insight-driven one-pager (Module 9)
            """)

    # ── CASE 1: P&L DIAGNOSTIC ────────────────────────────────────────────────
    with tab2:
        _sec("Case 1: Full P&L Diagnostic — Industrial Manufacturer Q3 2024", "🔍")

        st.markdown("""
**Business Situation:** You are Group FP&A Manager. Q3 2024 results have closed.
EBITDA came in at **$94M against a budget of $136M** — a miss of **$42M (31%)**.
The CFO needs a full root-cause analysis and recovery plan by 9am tomorrow.
        """)

        st.markdown("**Step 1 — Top-Down P&L Variance**")
        pnl = pd.DataFrame({
            "P&L Line":    ["Revenue","COGS","Gross Profit","SG&A","R&D","EBITDA"],
            "Budget ($M)": [500,-220, 280,-100,-44,136],
            "Actual ($M)": [482,-238, 244,-112,-38, 94],
        })
        pnl["Variance ($M)"] = pnl["Actual ($M)"] - pnl["Budget ($M)"]
        pnl["Variance %"]    = (pnl["Variance ($M)"] / pnl["Budget ($M)"].abs() * 100).round(1)
        pnl["Signal"] = pnl["Variance ($M)"].apply(lambda v: "🔴 Miss" if v<0 else "🟢 Beat")
        st.dataframe(pnl, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — EBITDA Bridge: Budget → Actual**")
        fig = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute","relative","relative","relative","relative","total"],
            x=["Budget EBITDA","Revenue Miss","COGS Overshoot","SGA Over-run","R&D Saving","Actual EBITDA"],
            y=[136, -18, -18, -12, +6, 0],
            text=["$136M","-$18M","-$18M","-$12M","+$6M","$94M"],
            textposition="outside",
            connector={"line":{"color":"#888"}},
            increasing={"marker":{"color":"#1D9E75"}},
            decreasing={"marker":{"color":"#E24B4A"}},
            totals={"marker":{"color":"#185FA5"}},
        ))
        fig.update_layout(title="EBITDA Bridge — Budget to Actual Q3 2024 ($M)",
                          template="plotly_white", height=420)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 3 — Revenue PVM Decomposition**")
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Total Revenue Miss",  "−$18M")
        c2.metric("Price Effect",        "+$8M",  delta="Price increases landed ✅")
        c3.metric("Volume Effect",       "−$22M", delta="Volume shortfall ⚠️")
        c4.metric("Mix Effect",          "−$4M",  delta="Worse product mix ⚠️")
        st.info("📌 The revenue miss is entirely **volume-driven**. Price realisation was actually **ahead of plan** (+$8M). Focus the investigation on volume, not pricing.")

        st.markdown("**Step 4 — Volume Miss by Customer Segment**")
        segs  = ["Enterprise","Mid-Market","SMB","Public Sector"]
        vvars = [+5, -15, -9, +1]
        fig2  = go.Figure(go.Bar(
            x=segs, y=vvars,
            marker_color=["#1D9E75" if v>0 else "#E24B4A" for v in vvars],
            text=[f"${v:+}M" for v in vvars], textposition="outside",
        ))
        fig2.add_hline(y=0, line_color="black", line_width=1)
        fig2.update_layout(title="Revenue Variance by Segment ($M) — Mid-Market is the primary driver",
                           yaxis=dict(range=[-20,12]), template="plotly_white", height=360)
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Step 5 — COGS Anomaly Detection (Z-Score)**")
        np.random.seed(7)
        unit_costs = np.random.normal(42, 4, 60)
        unit_costs[12]=78; unit_costs[35]=81
        z_scores = (unit_costs - unit_costs.mean()) / unit_costs.std()
        flagged  = np.abs(z_scores) > 2.5
        anom_df  = pd.DataFrame({
            "Transaction":["Txn #13","Txn #36"],
            "Unit Cost ($)":["$78","$81"],
            "Normal Range":"$34–$50",
            "Z-Score":["4.1σ","5.1σ"],
            "Root Cause":["Emergency spot-market purchase Jul-24 (supplier shortage)",
                           "Air freight premium — expedited delivery to avoid stockout"],
        })
        st.dataframe(anom_df, use_container_width=True, hide_index=True)
        st.warning("⚠️ 2 anomalous COGS transactions identified — both relate to the raw material supply disruption in Jul-24. These account for ~$6M of the $18M COGS miss.")

        st.success("""
**📋 Root Cause Summary & Recovery Plan**

| Driver | Impact | Root Cause |
|--------|--------|------------|
| Revenue volume miss | −$22M | Mid-Market: 3 accounts churned to a competitor in Aug. SMB: pricing sensitivity post-summer increase. |
| COGS inflation | −$18M | Raw material costs +8.5% above budget. 2 emergency spot-market purchases at 85% premium. |
| SGA over-run | −$12M | 18 headcount hired in Q2 ahead of revenue ramp that did not materialise. |
| R&D under-spend | +$6M | Project Phoenix delayed 1 quarter — costs shift to Q4. |

**Recommended Actions for Q4:**
1. Reactivate churned Mid-Market accounts — targeted retention offer up to 10% discount (CFO to approve)
2. Accelerate supplier diversification RFP — 3 alternative suppliers by Oct-31 (saves est. $4M in Q4)
3. Freeze SGA hiring — remove 4 unfilled roles from plan (saves $3M Q4 run-rate)
4. **Expected Q4 EBITDA recovery: ~$14M above Q3 run-rate**
        """)

    # ── CASE 2: WORKING CAPITAL ───────────────────────────────────────────────
    with tab3:
        _sec("Case 2: Working Capital Optimisation — Consumer Goods Company", "💸")

        st.markdown("""
**Business Situation:** The CFO flags that free cash flow is **$38M below EBITDA conversion expectations**.
Working capital has ballooned over the last 6 months. Diagnose where the cash is trapped
and recommend a structured improvement plan.
        """)

        st.markdown("**Step 1 — Working Capital Dashboard: Actual vs Budget**")
        wc_df = pd.DataFrame({
            "Metric":         ["DSO (Days Sales Outstanding)","DIO (Days Inventory Outstanding)",
                                "DPO (Days Payable Outstanding)","Cash Conversion Cycle"],
            "Budget (days)":  [45, 40, 52, 33],
            "Actual (days)":  [62, 55, 38, 79],
            "Variance (days)":[+17,+15,-14,+46],
            "Cash Impact ($M)":[-21.2,-17.4,-12.8,-51.4],
            "RAG":            ["🔴 Red","🔴 Red","🔴 Red","🔴 Red"],
        })
        st.dataframe(wc_df, use_container_width=True, hide_index=True)
        st.error("⛔ Cash Conversion Cycle has deteriorated by 46 days — $51M of cash trapped above budget levels.")

        st.markdown("**Step 2 — NWC Bridge: Budget to Actual**")
        daily_sales = 482/91
        daily_cogs  = 238/91
        dso_impact  = (62-45) * daily_sales
        dio_impact  = (55-40) * daily_cogs
        dpo_impact  = -(38-52) * daily_cogs

        fig = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute","relative","relative","relative","total"],
            x=["Budget NWC","DSO: 62 vs 45 days","DIO: 55 vs 40 days",
               "DPO: 38 vs 52 days","Actual NWC"],
            y=[100, dso_impact, dio_impact, dpo_impact, 0],
            text=[f"$100M", f"+${dso_impact:.0f}M", f"+${dio_impact:.0f}M",
                  f"+${dpo_impact:.0f}M", f"${100+dso_impact+dio_impact+dpo_impact:.0f}M"],
            textposition="outside",
            connector={"line":{"color":"#888"}},
            increasing={"marker":{"color":"#E24B4A"}},
            decreasing={"marker":{"color":"#1D9E75"}},
            totals={"marker":{"color":"#185FA5"}},
        ))
        fig.update_layout(title="Net Working Capital Bridge: Budget → Actual ($M) — Cash is trapped",
                          template="plotly_white", height=420)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 3 — Root Cause Analysis by Working Capital Driver**")
        rc_df = pd.DataFrame({
            "Driver":    ["DSO +17 days","DIO +15 days","DPO −14 days"],
            "Root Cause":["Collections team underresourced — 3 vacancies unfilled since Jun-24. "
                           "Top 12 customers averaging 78 days to pay vs 45-day terms.",
                           "Demand planning mis-forecast caused overstock of SKUs 200-250. "
                           "Seasonal summer range not depleted before autumn production started.",
                           "3 key suppliers moved to 30-day standard terms (from 45-day) "
                           "after payment disputes in H1-24. DPO has fallen as a result."],
            "Cash Trapped":["$21M","$17M","$13M"],
        })
        st.dataframe(rc_df, use_container_width=True, hide_index=True)

        st.markdown("**Step 4 — Improvement Roadmap & Cash Release Potential**")
        roadmap = pd.DataFrame({
            "Initiative":    ["Collections acceleration programme",
                               "Inventory right-sizing (SKU rationalisation)",
                               "Supplier payment term renegotiation",
                               "Dynamic discounting for early payment"],
            "Target (days)": ["DSO → 50 days","DIO → 45 days","DPO → 48 days","DPO → 52 days"],
            "Cash Release":  ["$15M","$10M","$8M","$13M"],
            "Timeline":      ["Q4-24 (90 days)","Q1-25 (180 days)","Q4-24 (60 days)","Q1-25 (90 days)"],
            "Owner":         ["CFO / AR Manager","Supply Chain Director","Procurement Director","Treasury"],
        })
        st.dataframe(roadmap, use_container_width=True, hide_index=True)

        fig2 = go.Figure(go.Bar(
            x=roadmap["Initiative"], y=[15,10,8,13],
            marker_color="#1D9E75",
            text=["$15M","$10M","$8M","$13M"], textposition="outside",
        ))
        fig2.update_layout(title="Cash Release Potential by Initiative ($M) — Total: $46M",
                           yaxis_title="Cash Released ($M)",
                           template="plotly_white", height=360)
        st.plotly_chart(fig2, use_container_width=True)

        st.success("""
**📋 CFO Recommendation: Working Capital Recovery Plan**

**Total cash release potential: $46M over 6 months**

**Priority 1 (Q4-24, 90 days):** Fill 3 collections vacancies + implement weekly chasing cadence for top-12 customers. Expected DSO improvement: −12 days → $15M cash release.

**Priority 2 (Q4-24, 60 days):** Renegotiate top 5 supplier payment terms back to 45+ days. Target: $8M DPO improvement.

**Priority 3 (Q1-25):** SKU rationalisation — discontinue 30 slow-moving lines. Inventory reduction of $10M.

**KPI targets for Q1-25 management pack:** DSO < 52 days, DIO < 47 days, DPO > 46 days, CCC < 53 days.
        """)

    # ── CASE 3: M&A SYNERGIES ─────────────────────────────────────────────────
    with tab4:
        _sec("Case 3: M&A Synergy Tracking — Day 100 Post-Merger Review", "🤝")

        st.markdown("""
**Business Situation:** Your company acquired Delta Corp 100 days ago.
The deal model assumed **$60M of annual synergies**. The integration team must now
present a Day-100 review to the Board: are synergy targets on track,
and what corrective action is needed?
        """)

        st.markdown("**Step 1 — Synergy Tracker: Target vs Run-Rate Achieved**")
        syn_df = pd.DataFrame({
            "Synergy Category": ["Procurement / COGS savings","Headcount rationalisation",
                                  "Systems & IT consolidation","Revenue cross-sell uplift",
                                  "Facility consolidation"],
            "Annual Target ($M)":[20, 18, 8, 10, 4],
            "Run-Rate Achieved ($M)":[14, 16, 3, 2, 0],
            "Status":             ["🟡 On Track","🟢 On Track","🔴 At Risk","🔴 Behind","⚪ Not Started"],
            "Commentary":         ["Procurement renegotiations complete for 7 of 12 categories",
                                    "Redundancy process complete. 45 of 58 roles exited.",
                                    "ERP migration delayed 2 months. New go-live: Feb-25.",
                                    "Sales teams not yet trained on combined product suite.",
                                    "Lease negotiations not yet initiated."],
        })
        st.dataframe(syn_df, use_container_width=True, hide_index=True)

        total_target   = 60
        total_achieved = 35
        on_track_pct   = total_achieved / total_target * 100

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Annual Synergy Target",   f"${total_target}M")
        c2.metric("Run-Rate Achieved",       f"${total_achieved}M")
        c3.metric("Overall Delivery",        f"{on_track_pct:.0f}%")
        c4.metric("At Risk / Behind",        "$19M", delta="⚠️ Needs action", delta_color="inverse")

        st.markdown("**Step 2 — Synergy Delivery Chart**")
        cats     = syn_df["Synergy Category"]
        targets  = syn_df["Annual Target ($M)"]
        achieved = syn_df["Run-Rate Achieved ($M)"]
        status_colours = {"🟢 On Track":"#1D9E75","🟡 On Track":"#BA7517",
                           "🔴 At Risk":"#E24B4A","🔴 Behind":"#E24B4A","⚪ Not Started":"#AAAAAA"}

        fig = go.Figure()
        fig.add_trace(go.Bar(name="Target", x=cats, y=targets,
                             marker_color="#B0C4DE", opacity=0.6))
        fig.add_trace(go.Bar(name="Achieved",x=cats, y=achieved,
                             marker_color=[status_colours[s] for s in syn_df["Status"]]))
        fig.update_layout(title="Synergy Tracking: Target vs Run-Rate Achieved ($M)",
                          barmode="overlay", template="plotly_white", height=400,
                          legend=dict(orientation="h",y=1.02))
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Grey bars = target. Coloured bars = achieved. Green = on track, Amber = slight risk, Red = material gap, Grey = not started.")

        st.markdown("**Step 3 — Forecast-to-Close: Year 1 Synergy P&L**")
        months       = [f"M{i}" for i in range(1,13)]
        cumulative_t = [60/12*i for i in range(1,13)]
        cumulative_a = [0,0,1.5,3.5,6,9,12,16,20,24.5,29,35]
        forecast_c   = cumulative_a[:] ; forecast_c[9]=27; forecast_c[10]=32; forecast_c[11]=37

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=months, y=cumulative_t, name="Target (cumulative)",
                                  line=dict(color="#185FA5",width=2,dash="dash")))
        fig2.add_trace(go.Scatter(x=months[:10], y=cumulative_a[:10], name="Actual (cumulative)",
                                  line=dict(color="#1D9E75",width=2.5)))
        fig2.add_trace(go.Scatter(x=months[9:], y=forecast_c[9:], name="Forecast (updated)",
                                  line=dict(color="#BA7517",width=2,dash="dot")))
        fig2.add_shape(type="line", x0="M10", x1="M10", y0=0, y1=1,
                       xref="x", yref="paper",
                       line=dict(dash="dash", color="gray"))
        fig2.add_annotation(x="M10", y=1.02, xref="x", yref="paper",
                            text="Today (Day 100)", showarrow=False,
                            font=dict(color="gray"), align="center")
        fig2.update_layout(title="Year 1 Synergy Delivery — Actual vs Target (Cumulative $M)",
                           xaxis_title="Month", yaxis_title="Cumulative Synergies ($M)",
                           template="plotly_white", height=400,
                           legend=dict(orientation="h",y=1.02))
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Step 4 — Gap Analysis and Corrective Actions**")
        st.warning("""
**🔴 Items Requiring Immediate Board Attention:**

**IT Consolidation ($5M gap):** ERP migration 2 months behind. New go-live Feb-25.
Risk: Further delay costs $1.5M per month in dual-running costs.
**Action:** CTO to present recovery plan at Nov Board. Contingency: outsource migration work.

**Revenue Cross-sell ($8M gap):** Sales teams from both entities not yet trained on combined product suite.
Pipeline tracking shows zero cross-sell opportunities logged to date.
**Action:** Combined product training mandatory by Dec-1. Assign dedicated cross-sell quota to top 20 reps.

**Facility Consolidation ($4M gap):** Lease negotiations for 3 offices not yet initiated.
**Action:** Appoint external real estate adviser by Nov-15. Target signed heads of terms by Jan-25.
        """)

        st.success(f"""
**📋 Board Summary — Day 100 Synergy Review**

**Overall status: 🟡 AMBER — $35M of $60M target secured (58%). Year 1 revised forecast: $37M (62% of target).**

**On track ($30M):** Procurement savings and headcount rationalisation are progressing well.
The foundational "quick wins" are delivered.

**At risk ($19M):** IT, cross-sell, and facilities require immediate escalation and dedicated resource.
Without intervention, Year 1 delivery will be ~$37M vs $60M target.

**3-Year Synergy Confidence:** With corrective actions implemented, the full $60M run-rate
remains achievable by end of Year 2. Recommend Board approves additional $2M integration
resource (ROI: 30× on $60M annual synergy target).
        """)

    # ── FINAL QUIZ ────────────────────────────────────────────────────────────
    with tab5:
        _sec("Capstone Final Assessment", "🏆")
        st.markdown("This quiz tests integrated analytical thinking across all modules.")
        st.balloons()

        _quiz("1. In Case 1, EBITDA missed by $42M. Revenue was −$18M, COGS −$18M, SGA −$12M, R&D +$6M. Which two items explain the most?",
              ["Revenue miss and R&D saving",
               "COGS overshoot and SGA overspend",
               "Revenue miss and COGS overshoot",
               "SGA overspend and R&D saving"],
              "Revenue miss and COGS overshoot","m10q1")
        st.divider()

        _quiz("2. Cash Conversion Cycle = DSO + DIO − DPO. If DSO rises from 45 to 62 days, what is the direct cash impact for a $500M revenue company?",
              ["Cash decreases by approx $23M",
               "Cash increases by approx $23M",
               "Cash decreases by approx $9M",
               "No cash impact — it is non-cash"],
              "Cash decreases by approx $23M","m10q2")
        st.divider()

        _quiz("3. In M&A synergy tracking, a synergy is 'At Risk' when:",
              ["The deal has been legally completed",
               "Run-rate is significantly below plan and no credible catch-up path exists",
               "The synergy target exceeds $10M",
               "The integration team has changed"],
              "Run-rate is significantly below plan and no credible catch-up path exists","m10q3")
        st.divider()

        _quiz("4. In the revenue PVM decomposition, Price Effect = (Actual Price − Budget Price) × ___?",
              ["Budget Volume","Actual Volume","Budget Revenue","Actual Revenue"],
              "Actual Volume","m10q4")
        st.divider()

        _quiz("5. Which sequence correctly represents the Analytics Ladder from lowest to highest value?",
              ["Prescriptive → Predictive → Diagnostic → Descriptive",
               "Descriptive → Diagnostic → Predictive → Prescriptive",
               "Diagnostic → Descriptive → Predictive → Prescriptive",
               "Predictive → Descriptive → Diagnostic → Prescriptive"],
              "Descriptive → Diagnostic → Predictive → Prescriptive","m10q5")

        st.markdown("---")
        st.success("""
🎓 **Congratulations — you have completed the Financial Data Analytics Knowledge Folder!**

**Your learning journey:**
- ✅ M1 — Data foundations and quality
- ✅ M2 — Descriptive analytics and charts
- ✅ M3 — Diagnostic analytics and PVM analysis
- ✅ M4 — Predictive analytics and forecasting
- ✅ M5 — Prescriptive analytics and decisions
- ✅ M6 — Valuation and investment analytics
- ✅ M7 — Risk and treasury analytics
- ✅ M8 — Tools, tech and automation
- ✅ M9 — Communication and storytelling
- ✅ M10 — Capstone case studies

Apply these skills to your real financial data. Revisit any module where you want deeper practice.
        """)