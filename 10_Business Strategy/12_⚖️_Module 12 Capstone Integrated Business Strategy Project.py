import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏆 Module 12: Capstone — Integrated Business Strategy Project")
    st.markdown("*Apply the full Business Strategy syllabus to a real organisation — from strategic analysis to boardroom-ready financial plan*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Capstone Guide", "🧮 Strategic Analysis", "💡 Strategy Development",
        "📊 Financial Plan", "✅ Presentation Prep", "📝 Programme Summary"
    ])

    with tab1:
        st.header("Capstone Project Guide")

        st.subheader("🎯 Capstone Objective")
        st.markdown("""
        The Capstone project is your opportunity to demonstrate mastery of the **complete Business Strategy syllabus**
        in a single, integrated deliverable. You will select a real or realistic organisation and produce:

        1. **Strategic analysis** — External (PESTLE + Five Forces), Internal (VRIN + Value Chain), SWOT/TOWS
        2. **Strategic options** — Using Ansoff, BCG, and generic strategy frameworks
        3. **Financial evaluation** — NPV, ROIC, scenario analysis for preferred strategy
        4. **Implementation plan** — 7-S alignment, KPIs, initiatives, milestones
        5. **Risk register** — Top risks with financial quantification
        6. **Board presentation** — 10-slide executive strategy deck

        **The Capstone tests your ability to think and communicate as a strategic finance professional.**
        """)

        st.subheader("📋 Capstone Deliverable Structure")
        structure = {
            "Section": ["1. Company Overview", "2. External Analysis", "3. Internal Analysis",
                        "4. Strategic Position", "5. Strategic Options", "6. Preferred Strategy",
                        "7. Financial Plan", "8. Implementation Roadmap", "9. Risk Register", "10. Board Recommendation"],
            "Key Frameworks Used": [
                "Mission, vision, three levels of strategy",
                "PESTLE + Porter's Five Forces + Market sizing (TAM/SAM/SOM)",
                "VRIN + Value Chain + Financial capability assessment",
                "SWOT / TOWS + Competitive position + Current ROIC vs WACC",
                "Ansoff Matrix + BCG Matrix + Generic strategies evaluation",
                "SAFe criteria (Suitability, Acceptability, Feasibility) + NPV comparison",
                "Driver-based 3-year model + Scenario analysis (base/bull/bear) + FCF forecast",
                "7-S alignment + Balanced Scorecard + Initiative prioritisation",
                "Strategic risk register + Decision tree + Stress test",
                "1-page executive summary + Financial headline + Clear ask"
            ],
            "Finance Output": [
                "Historical ROIC analysis; capital structure review",
                "Revenue at risk; market opportunity sizing ($M)",
                "Cost/margin analysis by value chain activity; financial capability rating",
                "Current ROIC vs WACC; EVA calculation; competitive financial benchmarking",
                "NPV of each option; risk-adjusted EV analysis",
                "Full business case; NPV / IRR / Payback; synergy analysis if M&A",
                "3-year P&L, BS, CF; ROIC bridge; FCF trajectory",
                "Investment budget; KPI targets; milestone financial tracking",
                "Worst-case financial impact per risk; covenant stress test",
                "Value creation story; capital required; return on investment"
            ]
        }
        st.dataframe(pd.DataFrame(structure), use_container_width=True, hide_index=True)

        st.subheader("📊 Capstone Assessment Criteria")
        criteria = {
            "Criterion": ["Framework Mastery", "Financial Rigour", "Integration Quality", "Strategic Insight", "Communication Quality"],
            "What Examiners Look For": [
                "Correct and sophisticated application of all key frameworks (PESTLE, Five Forces, VRIN, BCG, TOWS, BSC, 7-S)",
                "Accurate financial modelling; NPV, ROIC, EVA; scenario analysis; logical financial assumptions",
                "Seamless connection between external analysis → internal analysis → strategy → financials → implementation",
                "Original, well-reasoned strategic conclusions beyond obvious textbook answers",
                "Clear, concise, visually compelling board-ready presentation — financial story told clearly"
            ],
            "Weight": ["25%", "30%", "20%", "15%", "10%"]
        }
        st.dataframe(pd.DataFrame(criteria), use_container_width=True, hide_index=True)

        st.subheader("🏢 How to Choose Your Company")
        st.markdown("""
        **Best choices:**
        - A company you work for or have worked for (insider knowledge = richer analysis)
        - A publicly listed company with available accounts (e.g. annual report on their website)
        - A sector you know well — your analysis will be more credible and specific

        **Avoid:**
        - Companies so large and complex that the analysis becomes too broad (e.g. Apple, Amazon in full)
        - Companies with no public information available
        - Fictional companies — real-world grounding is essential for financial credibility

        **Tip**: Choose a company facing a clear strategic challenge or opportunity — this gives your analysis focus and your recommendation urgency.
        """)

    with tab2:
        st.header("Strategic Analysis Workbench")

        st.subheader("Step 1: Company Profile")
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company Name:", value="Your Company Name")
            industry = st.text_input("Industry / Sector:", value="e.g. Financial Services")
            revenue = st.number_input("Annual Revenue ($M):", 0.1, 100000.0, 500.0, 10.0)
            ebitda_pct = st.slider("EBITDA Margin (%):", 0.0, 50.0, 15.0, 0.5)
        with col2:
            employees = st.number_input("Number of Employees:", 1, 500000, 2500, 100)
            markets = st.text_input("Key Markets:", value="UK, USA, Europe")
            current_roic = st.number_input("Current ROIC (%):", 0.0, 60.0, 10.0, 0.5)
            wacc_cs = st.number_input("WACC (%):", 4.0, 20.0, 9.0, 0.5)

        ebitda_abs = revenue * ebitda_pct / 100
        spread_cs = current_roic - wacc_cs
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("EBITDA ($M)", f"${ebitda_abs:.1f}M")
        with col2: st.metric("ROIC-WACC Spread", f"{spread_cs:+.1f}pp", "✅ Creating value" if spread_cs > 0 else "❌ Destroying value")
        with col3:
            invested_cap_est = revenue * 0.6
            eva_est = (spread_cs / 100) * invested_cap_est
            st.metric("Annual EVA (est.)", f"${eva_est:+.1f}M")

        st.markdown("---")
        st.subheader("Step 2: PESTLE Summary")
        pestle_factors = ["Political", "Economic", "Social", "Technological", "Legal", "Environmental"]
        pestle_rows = []
        for factor in pestle_factors:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1: st.markdown(f"**{factor}:**")
            with col2: finding = st.text_input("Key finding:", key=f"cap_p_{factor}", value=f"Key {factor.lower()} trend affecting {company_name}")
            with col3:
                impact_p = st.select_slider("Impact:", ["Low", "Med", "High"], value="Med", key=f"cap_pi_{factor}")
            pestle_rows.append({"Factor": factor, "Key Finding": finding, "Impact": impact_p})
        if st.button("Show PESTLE Summary"):
            st.dataframe(pd.DataFrame(pestle_rows), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("Step 3: Five Forces Assessment")
        forces_cap = ["Threat of New Entrants", "Supplier Power", "Buyer Power", "Threat of Substitutes", "Competitive Rivalry"]
        force_scores_cap = []
        for force in forces_cap:
            col1, col2 = st.columns([2, 1])
            with col1: st.markdown(f"**{force}:**")
            with col2: score_f = st.slider("Strength:", 1, 5, 3, key=f"cap_ff_{force}")
            force_scores_cap.append(score_f)
        avg_force = np.mean(force_scores_cap)
        industry_attractive = "Attractive" if avg_force <= 2.5 else ("Moderate" if avg_force <= 3.5 else "Unattractive")
        st.metric("Industry Attractiveness", industry_attractive, f"Avg Force Score: {avg_force:.1f}/5")

        st.markdown("---")
        st.subheader("Step 4: VRIN Capability Rating")
        capabilities = ["Core Technology / Product", "Brand & Reputation", "Customer Relationships", "Financial Strength", "Operational Excellence"]
        vrin_rows = []
        for cap in capabilities:
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
            with col1: st.markdown(f"**{cap}:**")
            with col2: v = st.checkbox("V", key=f"cap_v_{cap}", value=True)
            with col3: r = st.checkbox("R", key=f"cap_r_{cap}")
            with col4: i_cap = st.checkbox("I", key=f"cap_i_{cap}")
            with col5: n = st.checkbox("N", key=f"cap_n_{cap}")
            score_vrin = sum([v, r, i_cap, n])
            status = "🏆 SCA" if score_vrin == 4 else ("⚡ Temp Adv" if score_vrin == 3 else ("⚠️ Parity" if score_vrin == 2 else "❌ Disadv"))
            vrin_rows.append({"Capability": cap, "V": "✅" if v else "❌", "R": "✅" if r else "❌", "I": "✅" if i_cap else "❌", "N": "✅" if n else "❌", "Status": status})
        if st.button("Show VRIN Summary"):
            st.dataframe(pd.DataFrame(vrin_rows), use_container_width=True, hide_index=True)

    with tab3:
        st.header("Strategy Development")

        st.subheader("Step 5: SWOT / TOWS Analysis")
        col1, col2 = st.columns(2)
        with col1:
            strengths = st.text_area("🟢 Strengths:", value="1. \n2. \n3. ", height=100)
            weaknesses = st.text_area("🔴 Weaknesses:", value="1. \n2. \n3. ", height=100)
        with col2:
            opportunities = st.text_area("🔵 Opportunities:", value="1. \n2. \n3. ", height=100)
            threats = st.text_area("🟡 Threats:", value="1. \n2. \n3. ", height=100)

        st.subheader("Step 6: Strategic Options Evaluation")
        st.markdown("Evaluate three strategic options using the SAFe framework:")
        options_eval = []
        for i, option_name in enumerate(["Option A (Growth)", "Option B (Defend & Optimise)", "Option C (Transform)"]):
            st.markdown(f"**{option_name}:**")
            col1, col2, col3, col4 = st.columns(4)
            with col1: desc = st.text_input("Description:", value=f"Strategic option {i+1} description", key=f"opt_d_{i}")
            with col2: suitability = st.slider("Suitability (1–5):", 1, 5, 3, key=f"opt_s_{i}")
            with col3: acceptability = st.slider("Acceptability (1–5):", 1, 5, 3, key=f"opt_a_{i}")
            with col4: feasibility = st.slider("Feasibility (1–5):", 1, 5, 3, key=f"opt_f_{i}")
            safe_score = (suitability + acceptability + feasibility) / 3
            options_eval.append({"Option": option_name, "Description": desc, "Suitability": suitability,
                                 "Acceptability": acceptability, "Feasibility": feasibility,
                                 "SAFe Score": f"{safe_score:.1f}/5"})

        if st.button("🎯 Rank Strategic Options"):
            df_opts = pd.DataFrame(options_eval)
            df_opts["Numeric Score"] = df_opts["SAFe Score"].str.replace("/5","").astype(float)
            df_opts = df_opts.sort_values("Numeric Score", ascending=False).drop("Numeric Score", axis=1)
            df_opts.insert(0, "Rank", range(1, len(df_opts)+1))
            st.dataframe(df_opts, use_container_width=True, hide_index=True)
            st.success(f"✅ Recommended Strategy: **{df_opts.iloc[0]['Option']}** — {df_opts.iloc[0]['Description']}")

        st.subheader("Step 7: Balanced Scorecard — Strategic KPIs")
        bsc_rows = []
        perspectives_bs = {"Financial 💰": ["Revenue Growth (%)", "ROIC (%)", "EBITDA Margin (%)"],
                          "Customer 👥": ["NPS Score", "Market Share (%)", "Retention Rate (%)"],
                          "Internal ⚙️": ["Cost Efficiency (%)", "Cycle Time (days)", "Quality Score (%)"],
                          "Learning 🎓": ["Employee Engagement (%)", "Training Hours/FTE", "Digital Score (1–10)"]}
        for persp, kpis in perspectives_bs.items():
            for kpi in kpis:
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1: st.markdown(f"*{persp}* — **{kpi}**")
                with col2: target_bsc = st.number_input("Target:", value=15.0, key=f"bsc_t_{persp}_{kpi}", step=1.0)
                with col3: current_bsc = st.number_input("Current:", value=12.0, key=f"bsc_c_{persp}_{kpi}", step=1.0)
                gap = target_bsc - current_bsc
                status_bsc = "🟢" if gap <= 0 else ("🟡" if gap / target_bsc <= 0.2 else "🔴")
                bsc_rows.append({"Perspective": persp, "KPI": kpi, "Target": target_bsc, "Current": current_bsc, "Gap": f"{gap:+.1f}", "Status": status_bsc})

    with tab4:
        st.header("Financial Plan")

        st.subheader("Step 8: 3-Year Strategic Financial Plan")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Year 1 Assumptions:**")
            rev_y1 = st.number_input("Revenue Y1 ($M):", 1.0, 5000.0, 500.0, 10.0)
            gm_y1 = st.slider("Gross Margin Y1 (%):", 10.0, 80.0, 40.0, 0.5)
            capex_y1 = st.number_input("Capex Y1 ($M):", 0.0, 200.0, 20.0, 1.0)
        with col2:
            st.markdown("**Growth Assumptions:**")
            rev_growth = st.slider("Revenue Growth Rate (% pa):", -10.0, 30.0, 12.0, 0.5)
            margin_expansion = st.slider("Annual Margin Expansion (pp):", -3.0, 5.0, 1.5, 0.5)
            capex_pct_rev = st.slider("Capex as % Revenue:", 1.0, 15.0, 4.0, 0.5)

        fixed_opex = st.number_input("Fixed Operating Costs per Year ($M):", 1.0, 200.0, rev_y1 * 0.20, 5.0)
        wacc_fp = st.slider("WACC for ROIC calculation (%):", 4.0, 20.0, 9.0, 0.5)
        tax_rate_fp = st.slider("Tax Rate (%):", 0.0, 40.0, 25.0, 0.5)

        fp_rows = []
        rev, gm_rate = rev_y1, gm_y1
        invested_capital_fp = rev_y1 * 0.6
        for yr in range(1, 4):
            if yr > 1:
                rev = rev * (1 + rev_growth / 100)
                gm_rate = min(gm_rate + margin_expansion, 80.0)
            capex_fp = rev * capex_pct_rev / 100
            gp = rev * gm_rate / 100
            ebitda_fp = gp - fixed_opex
            ebit_fp = ebitda_fp - capex_fp * 0.4
            nopat_fp = ebit_fp * (1 - tax_rate_fp / 100)
            invested_capital_fp = invested_capital_fp + capex_fp - capex_fp * 0.4
            roic_fp = nopat_fp / invested_capital_fp * 100 if invested_capital_fp > 0 else 0
            fcf_fp = ebitda_fp - capex_fp
            fp_rows.append({"Year": f"Year {yr}", "Revenue ($M)": f"${rev:.1f}M", "Gross Margin": f"{gm_rate:.1f}%",
                            "EBITDA ($M)": f"${ebitda_fp:.1f}M", "EBITDA %": f"{ebitda_fp/rev*100:.1f}%",
                            "Capex ($M)": f"${capex_fp:.1f}M", "FCF ($M)": f"${fcf_fp:.1f}M",
                            "ROIC (%)": f"{roic_fp:.1f}%",
                            "vs WACC": "✅" if roic_fp > wacc_fp else "❌"})
        st.dataframe(pd.DataFrame(fp_rows), use_container_width=True, hide_index=True)

        st.subheader("Step 9: Scenario Analysis")
        scenarios_cap = {"🐂 Bull Case": (rev_growth + 5, margin_expansion + 1), "📊 Base Case": (rev_growth, margin_expansion), "🐻 Bear Case": (rev_growth - 8, margin_expansion - 1.5)}
        scen_rows = []
        for scen_name, (rgr, mex) in scenarios_cap.items():
            rev_s3 = rev_y1 * (1 + rgr / 100) ** 3
            gm_s3 = min(gm_y1 + mex * 3, 80.0)
            ebitda_s3 = rev_s3 * gm_s3 / 100 - fixed_opex
            fcf_s3 = ebitda_s3 - rev_s3 * capex_pct_rev / 100
            scen_rows.append({"Scenario": scen_name, "Revenue CAGR": f"{rgr:.1f}%", "Y3 Revenue ($M)": f"${rev_s3:.1f}M",
                              "Y3 EBITDA ($M)": f"${ebitda_s3:.1f}M", "Y3 EBITDA %": f"{ebitda_s3/rev_s3*100:.1f}%",
                              "Y3 FCF ($M)": f"${fcf_s3:.1f}M"})
        st.dataframe(pd.DataFrame(scen_rows), use_container_width=True, hide_index=True)

        st.subheader("Step 10: Risk Register")
        st.markdown("Top 5 strategic risks for your plan:")
        cap_risks = []
        for i in range(5):
            col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
            with col1: risk_d = st.text_input("Risk:", value=f"Strategic risk {i+1}", key=f"cap_rsk_{i}")
            with col2: lik_r = st.slider("L:", 1, 5, 3, key=f"cap_l_{i}")
            with col3: imp_r = st.slider("I:", 1, 5, 3, key=f"cap_i_{i}")
            with col4: fin_r = st.number_input("Fin. Impact ($M):", 0.0, 200.0, 10.0, 1.0, key=f"cap_fi_{i}")
            score_r = lik_r * imp_r
            cap_risks.append({"Risk": risk_d, "L": lik_r, "I": imp_r, "Score": score_r,
                              "Rating": "🔴" if score_r >= 16 else ("🟠" if score_r >= 9 else "🟢"),
                              "Financial Impact ($M)": f"${fin_r:.1f}M"})
        if st.button("📋 Generate Risk Summary"):
            st.dataframe(pd.DataFrame(cap_risks).sort_values("Score", ascending=False), use_container_width=True, hide_index=True)

    with tab5:
        st.header("Board Presentation Prep")

        st.subheader("🎤 The 10-Slide Board Strategy Presentation")
        slides = {
            "Slide": ["1. Executive Summary", "2. Strategic Context", "3. Where Are We Now?", "4. Where Are We Going?",
                      "5. How Will We Get There?", "6. Financial Plan", "7. Investment Required", "8. Risk Overview",
                      "9. Implementation Timeline", "10. The Ask"],
            "Key Message": [
                "One-page: situation, complication, resolution. Financial headline upfront.",
                "External environment: top 3 PESTLE findings + Five Forces industry assessment",
                "Internal: VRIN strengths, value chain, ROIC vs WACC, competitive position",
                "Strategic ambition: vision, chosen strategy, TOWS options selected",
                "Balanced Scorecard, key initiatives, 7-S alignment investments",
                "3-year P&L, scenario analysis (bull/base/bear), FCF trajectory",
                "Total capex required, phasing, sources of funding, ROIC bridge",
                "Top 5 risks, mitigation, worst-case financial impact, covenant test",
                "12-month roadmap, milestones, accountabilities, KPI checkpoints",
                "Capital approval amount, governance path, next steps, decision required"
            ],
            "Finance Content": [
                "ROIC vs WACC; EVA; 3-year revenue and EBITDA targets",
                "Market size; revenue at risk from threats; opportunity ($M)",
                "ROIC decomposition; competitive financial benchmarking",
                "NPV of preferred strategy vs alternatives; SAFe evaluation",
                "Initiative investment budget; KPI financial targets",
                "Complete financial model; key assumptions; sensitivities",
                "NPV / IRR / Payback; synergy model if M&A",
                "Worst-case P&L; covenant stress test; liquidity buffer",
                "Milestone-linked financial gates; review cadence",
                "Exact capital amount; approval authority; deadline"
            ]
        }
        st.dataframe(pd.DataFrame(slides), use_container_width=True, hide_index=True)

        st.subheader("🧠 Boardroom Presentation Tips for Finance Professionals")
        st.markdown("""
        **Lead with the financial punchline:**
        > "This strategy will grow ROIC from 10% to 18% over three years, creating $45M of additional economic value. Here's how."

        **Handle challenge with data, not defensiveness:**
        > "That's a fair challenge. Our base case assumes 12% revenue growth — our bear case assumes 4%. Even in the bear case, NPV remains positive at $8M. Here's the sensitivity."

        **Quantify every strategic claim:**
        > ❌ "The digital transformation will improve customer experience."
        > ✅ "The digital transformation will increase NPS by 15 points, which our model shows drives 4% reduction in churn, worth $6M per year in revenue retention."

        **Own the risks proactively:**
        > "The two risks that concern us most are X and Y. If both materialise simultaneously, we breach covenant at Month 18. Our mitigation is Z, which reduces probability to under 10%."

        **End with a clear, specific ask:**
        > "We are requesting board approval for $12M capex to fund Phase 1, with Phase 2 approval conditional on achieving Q4 milestones. Decision required today."
        """)

        st.subheader("📊 Self-Assessment Checklist")
        checklist_items = [
            "External analysis (PESTLE + Five Forces) completed with financial quantification",
            "Internal analysis (VRIN + Value Chain) completed with ROIC diagnosis",
            "SWOT/TOWS strategic options generated and financially evaluated",
            "Preferred strategy selected using SAFe criteria with NPV comparison",
            "3-year driver-based financial model (P&L, BS indication, FCF) built",
            "Scenario analysis (bull/base/bear) completed with covenant stress test",
            "Balanced Scorecard with financial and non-financial KPIs defined",
            "7-S alignment gaps identified and investment budget estimated",
            "Strategic risk register with financial quantification (top 5 risks)",
            "Board presentation: clear financial narrative; specific capital ask; ROIC story"
        ]
        completed = []
        for item in checklist_items:
            done = st.checkbox(item, key=f"cl_{item}")
            completed.append(done)
        score_cl = sum(completed)
        progress_pct = score_cl / len(checklist_items)
        st.progress(progress_pct, text=f"Capstone Completion: {score_cl}/{len(checklist_items)} ({progress_pct*100:.0f}%)")
        if progress_pct >= 0.9:
            st.success("🏆 **Ready to present!** Your capstone is comprehensively prepared.")
        elif progress_pct >= 0.7:
            st.info("📝 **Good progress.** Complete remaining items to ensure a complete, integrated deliverable.")
        else:
            st.warning("⚠️ **More work needed.** Focus on the outstanding sections — particularly the financial model and scenario analysis.")

    with tab6:
        st.header("Business Strategy Programme — Complete Summary")

        st.subheader("🎓 Programme Completion — Module Review")
        modules_summary = {
            "Module": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
            "Title": ["Foundations of Business Strategy", "External Environment Analysis", "Internal Analysis & Competitive Advantage",
                      "Business-Level Strategy & Competitive Positioning", "Corporate Strategy: Growth, Portfolio & Diversification",
                      "Innovation, Disruption & Digital Strategy", "Strategy & Financial Performance",
                      "Strategic Planning, Implementation & Change", "Risk, Resilience & Strategic Decision-Making",
                      "Global Strategy, ESG & Stakeholder Value", "Strategic Finance: FP&A, Scenario Modelling & Business Cases",
                      "Capstone: Integrated Business Strategy Project"],
            "Core Framework": ["Strategic Mgmt Cycle", "PESTLE + Five Forces", "VRIN + Value Chain",
                               "Porter's Generic Strategies + ROIC", "Ansoff + BCG + M&A",
                               "3-Horizon + Disruption + Real Options", "EVA + Balanced Scorecard + DuPont",
                               "7-S Framework + Kotter + Rolling Forecast", "Risk Register + Decision Trees + Scenario Analysis",
                               "CAGE + ESG + Stakeholder Map", "NPV / IRR + Driver Model + Business Case",
                               "Full Integration + Board Presentation"],
            "Finance Output": ["Strategy map; capital allocation framework", "PESTLE risk scores; market sizing ($M)",
                               "VRIN financial assets; value chain cost analysis", "ROIC decomposition; pricing power analysis",
                               "BCG cash flow logic; M&A synergy NPV", "Real option value; digital ROI calculator",
                               "EVA; Balanced Scorecard KPIs; FCF signals", "7-S investment budget; rolling forecast",
                               "Risk register ($M); EV decision model; stress test", "CAGE entry cost; ESG WACC impact",
                               "3-statement model; business case; NPV/IRR", "Complete strategic financial plan + board deck"]
        }
        st.dataframe(pd.DataFrame(modules_summary), use_container_width=True, hide_index=True)

        st.subheader("🏆 The Strategic Finance Professional — Competency Summary")
        st.markdown("""
        By completing all 12 modules of this programme, you have developed the following strategic finance competencies:

        ### Analytical Competencies
        - **External analysis**: PESTLE, Five Forces, market sizing, scenario planning
        - **Internal analysis**: VRIN, Value Chain, DuPont, financial capability assessment
        - **Strategic synthesis**: SWOT/TOWS, competitive benchmarking, ROIC vs WACC diagnosis

        ### Strategic Competencies
        - **Competitive strategy**: Generic strategies, pricing power, moat identification
        - **Corporate strategy**: Portfolio management, M&A valuation, capital allocation
        - **Innovation & disruption**: Real options, 3-horizon model, digital ROI evaluation

        ### Financial Competencies
        - **Value creation**: EVA, ROIC-WACC bridge, FCF analysis, Balanced Scorecard
        - **Investment appraisal**: NPV, IRR, Payback, MIRR, business case development
        - **Financial planning**: Driver-based modelling, scenario analysis, rolling forecasts

        ### Global & Stakeholder Competencies
        - **International strategy**: CAGE analysis, entry mode evaluation, FX impact
        - **ESG integration**: Carbon pricing, WACC impact, stakeholder value mapping
        - **Risk management**: Strategic risk register, decision trees, stress testing

        ### Leadership Competencies
        - **Strategic communication**: Boardroom presentation, financial storytelling
        - **Change leadership**: Kotter's change model, 7-S alignment, transformation business case
        - **Stakeholder management**: Investor relations, board reporting, ESG narrative
        """)

        st.subheader("📌 The Master Formula")
        st.code("""
Strategic Finance Value Creation Formula:

Value Created = f(
    External Opportunity × Internal Capability    [Modules 2–3: Strategic Fit]
    × Competitive Advantage × Pricing Power       [Module 4: Business Strategy]
    × Portfolio Efficiency × M&A Synergies        [Module 5: Corporate Strategy]
    × Innovation Returns × Digital ROI            [Module 6: Innovation]
    × (ROIC − WACC) × Invested Capital           [Module 7: Value Creation]
    × Execution Quality × 7-S Alignment           [Module 8: Implementation]
    ÷ Risk Exposure × Resilience Score            [Module 9: Risk]
    × Global Scale × ESG Premium                  [Module 10: Global/ESG]
    × FP&A Rigour × Business Case Quality        [Module 11: Finance]
)
= Maximum Sustainable Long-Term Stakeholder Value
        """)

        st.success("""
        🎓 **Congratulations — Business Strategy Programme Complete!**

        You have completed a comprehensive, finance-led business strategy education covering all 12 modules.
        You are now equipped to:
        ✅ Analyse any business environment with rigorous strategic and financial frameworks
        ✅ Develop and evaluate strategic options with financial discipline
        ✅ Build boardroom-quality financial models and business cases
        ✅ Lead strategic planning, implementation, and change management
        ✅ Communicate strategy's financial impact to boards, investors, and leadership teams
        ✅ Act as a true strategic co-pilot — the modern finance professional's highest calling
        """)

        fig_prog = go.Figure(go.Indicator(
            mode="gauge+number",
            value=100,
            title={"text": "Programme Completion", "font": {"size": 20}},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#1B3A6B"},
                "steps": [{"range": [0, 50], "color": "#EEF3FB"}, {"range": [50, 80], "color": "#DBEAFE"}, {"range": [80, 100], "color": "#BFDBFE"}],
                "threshold": {"line": {"color": "#D97706", "width": 4}, "thickness": 0.75, "value": 100}
            }
        ))
        fig_prog.update_layout(height=300)
        st.plotly_chart(fig_prog, use_container_width=True)

if __name__ == "__main__":
    show()