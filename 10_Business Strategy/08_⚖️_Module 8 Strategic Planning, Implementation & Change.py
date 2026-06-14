import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🗺️ Module 8: Strategic Planning, Implementation & Change Management")
    st.markdown("*Translate strategy into executable plans, integrate with financial planning, and lead organisational transformation*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. The Strategic Planning Process")
        st.markdown("""
        Strategic planning converts strategic intent into an **actionable, financially resourced, time-bound plan**.

        **Integrated planning calendar — linking strategy to finance:**
        | Month | Activity | Finance Output |
        |-------|----------|---------------|
        | Jan–Feb | Environmental scanning & strategic review | External trend report; updated scenarios |
        | Mar–Apr | Strategic options development | Business cases; scenario models |
        | May–Jun | Board strategic workshop | Agreed strategic priorities |
        | Jul–Aug | Long-range planning (3–5yr) | LRP: P&L, BS, CF by scenario |
        | Sep–Oct | Annual budget and operating plan | Year 1 detailed budget |
        | Nov–Dec | KPI setting and cascade | Balanced Scorecard targets |

        **Three-horizon integration**: Long-range plan (H3) → 3-year plan (H2) → Annual budget (H1)
        """)

        st.subheader("2. McKinsey 7-S Framework")
        st.markdown("""
        Effective implementation requires aligning **seven interdependent organisational elements**.
        """)
        s7_data = {
            "Element": ["Strategy", "Structure", "Systems", "Shared Values", "Skills", "Style", "Staff"],
            "Type": ["Hard", "Hard", "Hard", "Soft (centre)", "Soft", "Soft", "Soft"],
            "Definition": [
                "The plan to achieve competitive advantage",
                "How the organisation is divided and coordinated",
                "Processes, procedures, and reporting frameworks",
                "Core values and culture — the centre of the model",
                "Capabilities and competencies of employees",
                "Leadership approach and management culture",
                "People — talent, roles, capabilities needed"
            ],
            "Finance Implication": [
                "All other S elements must support the chosen strategy",
                "Organisational design affects cost structure and accountability",
                "Planning, budgeting, and reporting systems must enable strategic decisions",
                "Culture of financial discipline vs. risk-taking determines investment quality",
                "Finance skills must match strategic complexity (FP&A, M&A, ESG)",
                "CFO leadership style shapes how data is used in decisions",
                "Right finance talent in right roles for strategic execution"
            ]
        }
        st.dataframe(pd.DataFrame(s7_data), use_container_width=True, hide_index=True)

        st.subheader("3. Strategy Execution Gap")
        st.markdown("""
        Research shows **67% of strategies fail in execution**, not formulation. Common causes:

        | Execution Barrier | Root Cause | Finance Solution |
        |------------------|-----------|-----------------|
        | **Vision gap** | People don't understand the strategy | Cascaded BSC; clear financial targets |
        | **Resource gap** | Capital not allocated to strategic priorities | Zero-based budgeting aligned to strategy |
        | **Management gap** | No regular strategic performance reviews | Monthly strategy dashboards; rolling forecast |
        | **People gap** | Incentives don't reward strategic behaviour | KPIs and bonus tied to strategic milestones |

        **Finance's role**: Ensure resources (capital, people, time) follow strategic priorities — not historical budget patterns.
        """)

        st.subheader("4. Kotter's 8-Step Change Model")
        kotter_data = {
            "Step": ["1. Create Urgency", "2. Form Coalition", "3. Create Vision", "4. Communicate Vision",
                     "5. Remove Obstacles", "6. Short-term Wins", "7. Build on Change", "8. Anchor in Culture"],
            "Finance Professional's Role": [
                "Build the financial burning platform — quantify cost of inaction vs benefit of change",
                "CFO as key member; bring financial credibility to the case for change",
                "Develop the financial narrative — what value does the transformation create?",
                "Translate strategy into financial impact for each audience (board, staff, investors)",
                "Identify and fund changes to financial systems, processes, and controls that block transformation",
                "Report early financial wins; build credibility for continued investment",
                "Reallocate resources to accelerating transformation; expand financial model",
                "Embed new financial KPIs and incentive structures that reinforce the new way"
            ]
        }
        st.dataframe(pd.DataFrame(kotter_data), use_container_width=True, hide_index=True)

        st.subheader("5. Agile Strategy & Rolling Forecasts")
        st.markdown("""
        Traditional annual planning is too slow for today's environment.
        **Agile strategy** continuously adapts direction based on new information.

        **Rolling Forecast vs Traditional Budget:**
        | Feature | Annual Budget | Rolling Forecast |
        |---------|--------------|-----------------|
        | Time horizon | Fixed 12 months | Rolling 12–18 months |
        | Update frequency | Once a year | Monthly or quarterly |
        | Focus | Cost control vs plan | Strategic decision support |
        | Flexibility | Low — locked in | High — adapts to changes |
        | Finance value | Accountability | Forward-looking insight |

        **Best practice**: Combine the Annual Budget (performance accountability) with Rolling Forecasts (strategic decision support).
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: 7-S Alignment Diagnosis — Technology Company Transformation")
        alignment = {
            "Element": ["Strategy", "Structure", "Systems", "Shared Values", "Skills", "Style", "Staff"],
            "Current State": [
                "Shift from product to SaaS platform",
                "Product-based silos (hardware, software, services teams)",
                "Annual budgeting; quarterly reporting; legacy ERP",
                "Engineering excellence; build quality",
                "Strong product engineering; weak digital marketing, data analytics",
                "Command-and-control; slow decision-making",
                "1,200 staff; 60% in hardware engineering"
            ],
            "Required State": [
                "Customer-centric SaaS growth; recurring revenue",
                "Customer segment-aligned squads; platform model",
                "Real-time dashboards; agile budgeting; cloud analytics",
                "Customer obsession; speed; data-driven decisions",
                "Growth marketing, data science, platform engineering, finance analytics",
                "Agile; empowered teams; experimental",
                "Re-skill hardware engineers; hire 200 in digital roles"
            ],
            "Alignment Gap": ["✅ Set", "🔴 Misaligned — restructure", "🟠 Partial — upgrade systems",
                             "🔴 Culture shift needed", "🔴 Major skills investment", "🟠 Change management needed", "🔴 Talent transformation required"]
        }
        st.dataframe(pd.DataFrame(alignment), use_container_width=True, hide_index=True)
        st.warning("💡 **Finance insight**: A 7-S gap analysis like this defines the cost of transformation. Each gap requires financial investment — restructuring costs, systems investment, training costs, recruitment costs. The CFO must build the transformation business case and track milestones.")

        st.subheader("Example 2: Strategic Initiative Prioritisation — Investment Committee Framework")
        initiatives = {
            "Strategic Initiative": ["Digital sales platform", "Asia market entry", "Cost automation programme", "New product line", "M&A — bolt-on acquisition", "ESG reporting framework"],
            "Strategic Fit (1–5)": [5, 4, 4, 3, 4, 3],
            "NPV ($M)": [12.5, 8.0, 18.0, 5.0, 22.0, 1.5],
            "Investment Required ($M)": [3.0, 8.0, 4.0, 6.0, 35.0, 0.8],
            "Risk Level": ["Medium", "High", "Low", "Medium", "High", "Low"],
            "Payback (Years)": [2.1, 4.5, 1.8, 3.2, 4.0, "N/A"],
            "Priority": ["🔴 Highest", "🟡 Selective", "🔴 Highest", "🟠 Medium", "🟡 Selective", "🟢 Proceed"]
        }
        st.dataframe(pd.DataFrame(initiatives), use_container_width=True, hide_index=True)
        st.info("💡 Priority logic: Cost automation (best NPV/$ invested, lowest risk, fastest payback) and Digital platform (highest strategic fit) lead. Asia entry and M&A are attractive but resource-intensive and higher risk — sequence for Year 2.")

        st.subheader("Example 3: Rolling Forecast — 4-Quarter View")
        st.markdown("**Rolling P&L Forecast — updated monthly, 12-month horizon always maintained**")
        rolling_df = pd.DataFrame({
            "Quarter": ["Q3 2024 (Actual)", "Q4 2024 (Forecast)", "Q1 2025 (Forecast)", "Q2 2025 (Forecast)"],
            "Revenue ($M)": [28.5, 30.0, 31.5, 33.0],
            "Gross Margin (%)": ["42%", "43%", "44%", "45%"],
            "EBITDA ($M)": [5.7, 6.3, 7.0, 7.6],
            "FCF ($M)": [3.2, 4.1, 4.8, 5.5],
            "Key Assumption": ["Actual", "Price increase +2%; new contract wins", "New product launch; cost savings start", "Full impact of automation programme"],
            "Key Risk": ["—", "Competitor response to price increase", "New product adoption risk", "Implementation risk on automation"]
        })
        st.dataframe(rolling_df, use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "7-S Alignment Analyser",
            "Strategic Initiative Prioritiser",
            "Rolling Forecast Builder"
        ])

        if tool == "7-S Analyser":
            pass

        if tool == "7-S Alignment Analyser":
            st.subheader("⚙️ 7-S Alignment Analyser")
            st.markdown("Rate alignment of each S element with your chosen strategy (1 = completely misaligned, 5 = fully aligned):")
            elements = ["Strategy (clarity)", "Structure (design)", "Systems (planning & reporting)", "Shared Values (culture)", "Skills (capabilities)", "Style (leadership)", "Staff (talent)"]
            scores = []
            for elem in elements:
                score = st.slider(f"**{elem}:**", 1, 5, 3, key=f"s7_{elem}")
                scores.append(score)

            avg_score = np.mean(scores)
            misaligned = [elements[i] for i, s in enumerate(scores) if s <= 2]
            partially = [elements[i] for i, s in enumerate(scores) if s == 3]

            if st.button("🔍 Generate Alignment Report"):
                results_7s = pd.DataFrame({"Element": elements, "Alignment Score": scores,
                                          "Status": ["✅ Aligned" if s >= 4 else ("🟠 Partial" if s == 3 else "🔴 Misaligned") for s in scores]})
                st.dataframe(results_7s, use_container_width=True, hide_index=True)
                st.metric("Overall 7-S Alignment Score", f"{avg_score:.1f}/5")
                if misaligned:
                    st.error(f"🔴 Critical misalignments requiring urgent investment: {', '.join(misaligned)}")
                if partially:
                    st.warning(f"🟠 Partial alignments to address in Year 1: {', '.join(partially)}")
                investment_needed = (5 - avg_score) * 20
                st.info(f"💰 Estimated transformation investment required: ~${investment_needed:.0f}M–${investment_needed*1.5:.0f}M (indexed to alignment gap)")

        elif tool == "Strategic Initiative Prioritiser":
            st.subheader("🎯 Strategic Initiative Prioritiser")
            num_initiatives = st.number_input("Number of initiatives to evaluate:", 2, 8, 4)
            init_data = []
            for i in range(int(num_initiatives)):
                st.markdown(f"**Initiative {i+1}:**")
                col1, col2, col3, col4 = st.columns(4)
                with col1: init_name = st.text_input("Name:", value=f"Initiative {i+1}", key=f"ini_n_{i}")
                with col2:
                    strat_fit = st.slider("Strategic Fit (1–5):", 1, 5, 3, key=f"ini_sf_{i}")
                    npv_i = st.number_input("NPV ($M):", -50.0, 200.0, float(10 + i * 5), 1.0, key=f"ini_npv_{i}")
                with col3:
                    invest_i = st.number_input("Investment ($M):", 0.1, 100.0, float(3 + i * 2), 0.5, key=f"ini_inv_{i}")
                    risk_i = st.selectbox("Risk:", ["Low", "Medium", "High"], key=f"ini_risk_{i}", index=min(i, 2))
                with col4:
                    payback_i = st.number_input("Payback (years):", 0.5, 10.0, float(2 + i * 0.5), 0.5, key=f"ini_pb_{i}")
                risk_adj = {"Low": 0.9, "Medium": 0.7, "High": 0.5}[risk_i]
                priority_score = (strat_fit * 2 + (npv_i / invest_i) * risk_adj + (5 / payback_i)) / 3
                init_data.append({"Initiative": init_name, "Strategic Fit": f"{strat_fit}/5", "NPV ($M)": f"${npv_i:.1f}M",
                                  "Investment ($M)": f"${invest_i:.1f}M", "Risk": risk_i, "Payback": f"{payback_i:.1f} yrs",
                                  "Priority Score": round(priority_score, 2)})

            if st.button("📊 Generate Priority Ranking"):
                df_init = pd.DataFrame(init_data).sort_values("Priority Score", ascending=False)
                df_init["Rank"] = range(1, len(df_init) + 1)
                st.dataframe(df_init, use_container_width=True, hide_index=True)
                st.success(f"🥇 **Highest priority**: {df_init.iloc[0]['Initiative']} — implement first. Lowest priority: {df_init.iloc[-1]['Initiative']} — defer or descope.")

        else:  # Rolling Forecast Builder
            st.subheader("📅 Rolling Forecast Builder")
            st.markdown("Build a 4-quarter rolling forecast:")
            quarters = ["Q1", "Q2", "Q3", "Q4"]
            revenues, margins, capex_list = [], [], []
            for q in quarters:
                col1, col2, col3 = st.columns(3)
                with col1: rev = st.number_input(f"{q} Revenue ($M):", 1.0, 500.0, float(25 + quarters.index(q) * 2), 0.5, key=f"rf_r_{q}")
                with col2: gm = st.slider(f"{q} Gross Margin (%):", 20.0, 70.0, float(40 + quarters.index(q) * 1.5), 0.5, key=f"rf_gm_{q}")
                with col3: capex = st.number_input(f"{q} Capex ($M):", 0.0, 50.0, 3.0, 0.5, key=f"rf_capex_{q}")
                revenues.append(rev)
                margins.append(gm)
                capex_list.append(capex)

            fixed_costs = st.number_input("Fixed costs per quarter ($M):", 1.0, 50.0, 5.0, 0.5)
            if st.button("📊 Generate Rolling Forecast"):
                forecast_rows = []
                for i, q in enumerate(quarters):
                    gp = revenues[i] * margins[i] / 100
                    ebitda = gp - fixed_costs
                    ebitda_m = ebitda / revenues[i] * 100 if revenues[i] > 0 else 0
                    fcf = ebitda - capex_list[i]
                    forecast_rows.append({"Quarter": q, "Revenue ($M)": f"${revenues[i]:.1f}M", "Gross Profit ($M)": f"${gp:.1f}M",
                                         "EBITDA ($M)": f"${ebitda:.1f}M", "EBITDA Margin": f"{ebitda_m:.1f}%", "Capex ($M)": f"${capex_list[i]:.1f}M",
                                         "FCF ($M)": f"${fcf:.1f}M", "FCF Status": "✅" if fcf > 0 else "⚠️"})
                st.dataframe(pd.DataFrame(forecast_rows), use_container_width=True, hide_index=True)
                total_fcf = sum([rev * m / 100 - fc - capex for rev, m, capex in zip(revenues, margins, capex_list)]) - fixed_costs * 4
                st.metric("Total Rolling 4-Quarter FCF", f"${total_fcf:.1f}M", "✅ Cash generative" if total_fcf > 0 else "⚠️ Cash consuming")

    with tab4:
        st.header("Visualizations")

        st.subheader("McKinsey 7-S Framework")
        labels = ["Shared\nValues", "Strategy", "Structure", "Systems", "Skills", "Style", "Staff"]
        r = [0, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
        theta = [0, 0, 60, 120, 180, 240, 300]
        x_pos = [0] + [0.6 * np.cos(np.radians(t)) for t in [0, 60, 120, 180, 240, 300]]
        y_pos = [0] + [0.6 * np.sin(np.radians(t)) for t in [0, 60, 120, 180, 240, 300]]
        colors_7s = ["#D97706", "#1B3A6B", "#0D7377", "#2563EB", "#7C3AED", "#E74C3C", "#27AE60"]
        fig_7s = go.Figure()
        for i, (label, x, y, c) in enumerate(zip(labels, x_pos, y_pos, colors_7s)):
            fig_7s.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", text=[label],
                                       textposition="middle center", marker=dict(size=70, color=c, opacity=0.85),
                                       textfont=dict(color="white", size=10), showlegend=False))
            if i > 0:
                fig_7s.add_shape(type="line", x0=0, y0=0, x1=x, y1=y, line=dict(color="#CBD5E1", width=1.5))
        fig_7s.update_layout(title="McKinsey 7-S Framework", height=500,
                            xaxis=dict(visible=False, range=[-1, 1]), yaxis=dict(visible=False, range=[-1, 1]))
        st.plotly_chart(fig_7s, use_container_width=True)

        st.subheader("Kotter's 8-Step Change Model")
        steps_k = ["1. Create Urgency", "2. Form Coalition", "3. Create Vision", "4. Communicate Vision",
                  "5. Remove Obstacles", "6. Short-term Wins", "7. Build on Change", "8. Anchor in Culture"]
        completion = [95, 85, 80, 70, 60, 75, 45, 30]
        fig_kotter = go.Figure(go.Bar(
            x=steps_k, y=completion,
            marker_color=["#27AE60" if c >= 70 else "#E67E22" if c >= 50 else "#E74C3C" for c in completion],
            text=[f"{c}% complete" for c in completion], textposition="auto"
        ))
        fig_kotter.update_layout(title="Kotter's 8-Step Change Progress Dashboard", yaxis_title="% Complete", height=420,
                                xaxis_tickangle=-25)
        st.plotly_chart(fig_kotter, use_container_width=True)

        st.subheader("Rolling Forecast vs Annual Budget")
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        budget_line = [10.0] * 12
        actual_forecast = [9.8, 10.2, 10.5, 9.9, 10.8, 11.0, 11.2, 11.5, 11.8, 12.0, 12.3, 12.5]
        rolling_upper = [a * 1.08 for a in actual_forecast]
        rolling_lower = [a * 0.92 for a in actual_forecast]
        fig_rf = go.Figure()
        fig_rf.add_trace(go.Scatter(x=months, y=budget_line, name="Annual Budget", line=dict(color="#E74C3C", width=2, dash="dash")))
        fig_rf.add_trace(go.Scatter(x=months, y=actual_forecast, name="Rolling Forecast (Best Estimate)", line=dict(color="#1B3A6B", width=3)))
        fig_rf.add_trace(go.Scatter(x=months + months[::-1], y=rolling_upper + rolling_lower[::-1],
                                   fill="toself", fillcolor="rgba(27,58,107,0.1)", line=dict(color="rgba(255,255,255,0)"),
                                   name="Forecast Range", showlegend=True))
        fig_rf.update_layout(title="Rolling Forecast vs Annual Budget — Forward View", yaxis_title="Revenue ($M)", height=400)
        st.plotly_chart(fig_rf, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. In Kotter's change model, what is Step 1?**")
        q1 = st.radio("", ["Form the guiding coalition", "Create a vision for change", "Create a sense of urgency", "Consolidate gains"], key="bs8q1")
        if st.button("Check Answer", key="bs8c1"):
            if q1 == "Create a sense of urgency":
                st.success("✅ Correct! Without urgency, people default to business-as-usual. The finance professional's role here is to quantify the cost of inaction.")
            else:
                st.error("❌ Incorrect. Step 1 in Kotter's model is Creating Urgency — making the case for WHY change is necessary now.")

        st.markdown("---")
        st.markdown("**2. In the McKinsey 7-S model, the central element (linking all others) is:**")
        q2 = st.radio("", ["Strategy", "Structure", "Shared Values", "Systems"], key="bs8q2")
        if st.button("Check Answer", key="bs8c2"):
            if q2 == "Shared Values":
                st.success("✅ Correct! Shared Values (culture) sit at the centre of the 7-S model — they connect and influence all other six elements.")
            else:
                st.error("❌ Incorrect. Shared Values (organisational culture) is the central element of the 7-S model.")

        st.markdown("---")
        st.markdown("**3. A rolling forecast differs from a traditional annual budget because:**")
        q3 = st.radio("", [
            "It is prepared by external consultants",
            "It extends forward by a fixed period (e.g. 12 months) and is updated regularly, always looking ahead",
            "It focuses only on capital expenditure",
            "It replaces the need for a Balanced Scorecard"
        ], key="bs8q3")
        if st.button("Check Answer", key="bs8c3"):
            if q3 == "It extends forward by a fixed period (e.g. 12 months) and is updated regularly, always looking ahead":
                st.success("✅ Correct! Rolling forecasts maintain a constant forward view — always 12–18 months ahead — and adapt as the environment changes.")
            else:
                st.error("❌ Incorrect. Rolling forecasts extend forward dynamically, always maintaining the same horizon, updated as new information arrives.")

        st.markdown("---")
        st.markdown("**4. The '7-S' in McKinsey's framework are all internal organisational elements. True or False?**")
        q4 = st.radio("", ["True — all seven Ss are internal", "False — some Ss analyse the external environment"], key="bs8q4")
        if st.button("Check Answer", key="bs8c4"):
            if q4 == "True — all seven Ss are internal":
                st.success("✅ Correct! The 7-S framework analyses internal organisational alignment — Strategy, Structure, Systems, Shared Values, Skills, Style, Staff.")
            else:
                st.error("❌ Incorrect. The 7-S framework is entirely internal — it assesses alignment of seven internal organisational elements.")

        st.markdown("---")
        st.markdown("**5. Research suggests that most strategy failures happen during:**")
        q5 = st.radio("", ["Strategy formulation", "External analysis", "Strategy execution and implementation", "Board approval process"], key="bs8q5")
        if st.button("Check Answer", key="bs8c5"):
            if q5 == "Strategy execution and implementation":
                st.success("✅ Correct! 67% of strategies fail in execution, not formulation. The implementation gap — vision, resources, management, people — is the primary failure point.")
            else:
                st.error("❌ Incorrect. Strategy execution is where most strategies fail — not in the analysis or formulation stage.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Integrated Strategic Planning Calendar
        ```
        Jan–Feb → Environmental scan + scenario refresh
        Mar–Apr → Strategic options & business cases
        May–Jun → Board strategic decisions
        Jul–Aug → Long-range plan (3–5yr P&L, BS, CF)
        Sep–Oct → Annual budget
        Nov–Dec → KPI setting & cascade
        ```

        ### 2. McKinsey 7-S Framework
        | Hard Ss | Soft Ss |
        |---------|---------|
        | Strategy | Shared Values (centre) |
        | Structure | Skills |
        | Systems | Style |
        | | Staff |

        All seven must align with each other and with the chosen strategy.

        ### 3. Strategy Execution — Four Gaps
        ```
        Vision Gap → People don't understand strategy → Cascade BSC
        Resource Gap → Capital not aligned to priorities → Strategic budgeting
        Management Gap → No regular strategy reviews → Monthly dashboards
        People Gap → Incentives misaligned → KPI-linked remuneration
        ```

        ### 4. Kotter's 8 Steps (Finance Focus)
        - Step 1: Quantify urgency (cost of inaction)
        - Step 3: Develop financial narrative
        - Step 6: Report and celebrate early financial wins
        - Step 8: Embed new KPIs and incentive structures

        ### 5. Rolling Forecast Benefits
        - Always 12–18 months forward-looking
        - Adapts to new strategic information
        - Supports strategic decision-making (not just control)
        - Combined with annual budget: best of both worlds
        """)
        st.subheader("📌 Key Formulas")
        st.code("Transformation Cost = Σ (Gap size × Cost to close each 7-S gap)")
        st.code("Initiative Priority Score = (Strategic Fit × 2 + NPV/Investment × Risk Adj + 5/Payback) / 3")
        st.success("🎓 **Module 8 Complete!** You can now design integrated strategic planning processes, apply 7-S alignment analysis, lead change, and build rolling forecasts.")
        st.info("💡 **Next**: Module 9 — Risk, Resilience & Strategic Decision-Making Under Uncertainty")

if __name__ == "__main__":
    show()