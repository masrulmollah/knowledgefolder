import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💡 Module 6: Innovation, Disruption & Digital Strategy")
    st.markdown("*Evaluate innovation investments, respond to disruption, and build the financial case for digital transformation*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Types of Innovation")
        st.markdown("""
        Not all innovation is equal. Finance professionals must distinguish types to apply the right investment framework and risk/return expectation.
        """)
        innovation_types = {
            "Type": ["Incremental", "Architectural", "Radical / Breakthrough", "Disruptive"],
            "Definition": [
                "Small improvements to existing products/processes",
                "Reconfigures existing components in a new way",
                "Entirely new technology or approach",
                "Initially inferior product that starts in low-end market, then moves upmarket"
            ],
            "Risk Level": ["Low", "Medium", "High", "Extreme (unpredictable timing)"],
            "Investment Profile": ["Small, frequent, embedded in opex", "Medium capex, 2–3 year payback", "Large R&D capex, 5–10 year horizon", "Small initial; massive if successful"],
            "Finance Approach": [
                "NPV, payback; built into base budgets",
                "NPV/IRR; business case review",
                "Portfolio approach; real options; accept negative IRR short-term",
                "Venture model; small bets; option to scale rapidly"
            ]
        }
        st.dataframe(pd.DataFrame(innovation_types), use_container_width=True, hide_index=True)

        st.subheader("2. The 3-Horizon Model (McKinsey)")
        st.markdown("""
        Organising innovation investment into three time horizons ensures companies sustain performance TODAY
        while building competitive advantage for TOMORROW.

        | Horizon | Focus | Time | Investment Share | Finance Metric |
        |---------|-------|------|-----------------|---------------|
        | **H1 — Core** | Extend and defend the existing business | 0–2 years | 70% | ROIC, EBITDA margin, cost reduction |
        | **H2 — Emerging** | Build emerging businesses | 2–5 years | 20% | Revenue growth, customer acquisition |
        | **H3 — Visionary** | Create future options | 5+ years | 10% | Option value, strategic optionality |

        **Finance implication**: H1 funds H2 and H3.
        The mix should evolve as H3 bets succeed and graduate to H2, then H1.
        """)

        st.subheader("3. Disruptive Innovation (Christensen)")
        st.markdown("""
        Clayton Christensen's theory: disruption begins with a **simpler, cheaper, more accessible** alternative that
        incumbents initially ignore because it targets their least profitable customers.

        **Disruption sequence:**
        1. Disruptor enters with inferior product at low price (e.g. Netflix DVDs vs Blockbuster)
        2. Incumbent ignores — customers are low-value; margins are low
        3. Disruptor improves quality while maintaining cost advantage
        4. Disruptor moves upmarket — attacks the incumbent's core
        5. Incumbent responds too late — business model can't adapt

        **Finance professional's role in disruption assessment:**
        - Monitor disruptors' unit economics and growth trajectory
        - Model the revenue displacement scenario
        - Build the financial case for a disruptive response BEFORE the threat becomes critical
        - Assess: can you disrupt yourself before someone else does?
        """)

        st.subheader("4. Digital Transformation Strategy")
        st.markdown("""
        Digital transformation is not a technology project — it is a **strategic repositioning** enabled by technology.

        **Four strategic dimensions of digital transformation:**
        | Dimension | What Changes | Finance Impact |
        |-----------|-------------|----------------|
        | **Customer experience** | Digital channels, personalisation, self-service | Revenue uplift, NPS improvement, churn reduction |
        | **Operational efficiency** | Automation, AI, process digitisation | Cost reduction, productivity gains, working capital improvement |
        | **Business model** | New revenue streams, platform models, data monetisation | New P&L lines, recurring revenue mix improvement |
        | **Culture & capability** | Digital skills, agile ways of working, data-driven decisions | Talent investment, speed to market improvement |

        **Finance function digital transformation:**
        - Automated FP&A and reporting (save 40–60% of manual effort)
        - Real-time dashboards and driver-based forecasting
        - AI-powered variance analysis and exception alerting
        - Predictive financial modelling
        """)

        st.subheader("5. Real Options Thinking for Innovation Investment")
        st.markdown("""
        Traditional NPV undervalues innovation investment by ignoring **strategic optionality** — the ability to invest more if the bet succeeds.

        **Real options in innovation:**
        | Option Type | Definition | Innovation Example |
        |-------------|-----------|-------------------|
        | **Option to expand** | Invest more if Phase 1 succeeds | Fund Phase 2 clinical trial if Phase 1 data positive |
        | **Option to defer** | Wait for more information before committing | Pilot digital platform before full rollout |
        | **Option to abandon** | Stop investment if milestones not met | Kill product development if prototype fails |
        | **Option to switch** | Redirect resources to alternative use | Pivot product if target market not responding |

        **Real Option Value = Traditional NPV + Option Premium**

        The option premium reflects the value of flexibility — most significant in high-uncertainty investments.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Disruption Case Study — Netflix vs Blockbuster")
        timeline = {
            "Year": ["1997", "2002", "2005", "2007", "2010", "2013"],
            "Netflix Action": [
                "DVD-by-mail subscription at $20/mo",
                "IPO; 857,000 subscribers",
                "Offers online streaming pilot",
                "Streaming service launched",
                "Available on all devices; 20M subscribers",
                "Original content — House of Cards"
            ],
            "Blockbuster Action": [
                "Peak $6B revenue; 9,000 stores; $40 late fees",
                "Tries online rental service — abandoned",
                "Launches Blockbuster Online; too late",
                "Posts first losses; cuts online investment",
                "Files for bankruptcy — $900M debt",
                "Brand sold for $320M — the remnant"
            ],
            "Financial Signal": [
                "Netflix TAM tiny; Blockbuster ignores",
                "Netflix unit economics improving with scale",
                "Netflix streaming cost falls 80% vs DVD distribution",
                "Streaming NPS 2× higher than DVD-by-mail",
                "Netflix LTV/CAC ratio 5× Blockbuster's store model",
                "Streaming margin 40%+ vs Blockbuster store model 15%"
            ]
        }
        st.dataframe(pd.DataFrame(timeline), use_container_width=True, hide_index=True)
        st.error("💡 **Finance lesson**: Blockbuster's CFO consistently rejected streaming investment because near-term NPV was negative and it would cannibalise the DVD business. The real option value of leading the transition was worth billions. Defending the old model cost everything.")

        st.subheader("Example 2: Digital Transformation Business Case — Finance Function")
        st.markdown("""
        **Initiative**: Automate FP&A reporting and forecasting for a $500M revenue company

        | Cost Item | Year 1 | Year 2 | Year 3 | Total |
        |-----------|--------|--------|--------|-------|
        | Technology (platform) | -$800K | -$200K | -$200K | -$1.2M |
        | Implementation | -$400K | -$100K | -$50K | -$550K |
        | Training & change | -$150K | -$50K | -$25K | -$225K |
        | **Total Investment** | **-$1.35M** | **-$350K** | **-$275K** | **-$1.975M** |

        | Benefit Item | Year 1 | Year 2 | Year 3 | Total |
        |-------------|--------|--------|--------|-------|
        | Staff time saved (12 FTE → 8 FTE) | +$200K | +$400K | +$400K | +$1.0M |
        | Faster close cycle (12→5 days) | +$100K | +$150K | +$150K | +$400K |
        | Better decisions (revenue accuracy) | +$0 | +$500K | +$800K | +$1.3M |
        | **Total Benefits** | **+$300K** | **+$1.05M** | **+$1.35M** | **+$2.7M** |

        **NPV @ 8%: +$415K | IRR: 18.5% | Payback: 2.1 years** ✅
        """)

        st.subheader("Example 3: Innovation Portfolio — 3-Horizon Allocation")
        h_data = {
            "Horizon": ["H1 — Core (70%)", "H2 — Emerging (20%)", "H3 — Visionary (10%)"],
            "Example Initiative": ["Cost reduction programme", "Digital service platform", "AI-powered personalisation"],
            "Budget ($M)": [14.0, 4.0, 2.0],
            "Expected ROIC": ["22% (Year 1)", "15% (Year 3)", "Unknown — option value"],
            "Success Metric": ["Cost savings vs plan", "Customer adoption & revenue", "Proof of concept achieved"],
            "Finance Treatment": ["Tracked in operating budget vs target", "Business case + quarterly milestones", "Small-bet; venture model; option to scale"]
        }
        st.dataframe(pd.DataFrame(h_data), use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "Innovation Investment Evaluator",
            "Digital ROI Calculator",
            "Disruption Risk Radar"
        ])

        if tool == "Innovation Investment Evaluator":
            st.subheader("🔬 Innovation Investment Evaluator")
            st.markdown("Evaluate an innovation investment using NPV + Real Option Value:")
            col1, col2 = st.columns(2)
            with col1:
                project_name = st.text_input("Project Name:", value="Digital Platform Phase 1")
                horizon = st.selectbox("Innovation Horizon:", ["H1 — Core (defend/extend)", "H2 — Emerging (build)", "H3 — Visionary (explore)"])
                initial_invest = st.number_input("Initial Investment ($M):", 0.1, 100.0, 5.0, 0.5)
                annual_benefit = st.number_input("Annual Benefit ($M, from Year 2):", 0.0, 100.0, 2.0, 0.5)
                years = st.slider("Investment Horizon (years):", 2, 10, 5)
                discount_rate = st.slider("Discount Rate (%):", 5.0, 25.0, 10.0, 0.5)
            with col2:
                st.markdown("**Real Option Parameters:**")
                success_prob = st.slider("Probability Phase 1 succeeds (%):", 10, 90, 60)
                phase2_size = st.number_input("Phase 2 investment if success ($M):", 0.0, 200.0, 15.0, 1.0)
                phase2_npv = st.number_input("Phase 2 NPV if successful ($M):", 0.0, 500.0, 40.0, 5.0)
                option_discount = st.slider("Option Discount Rate (%):", 10.0, 30.0, 15.0, 0.5)

            pv_benefits = sum([annual_benefit / (1 + discount_rate / 100) ** t for t in range(2, years + 1)])
            traditional_npv = pv_benefits - initial_invest
            option_value = (success_prob / 100) * max(0, phase2_npv - phase2_size) / (1 + option_discount / 100) ** (years // 2)
            total_value = traditional_npv + option_value

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Traditional NPV", f"${traditional_npv:.2f}M", "Standard DCF")
            with col2: st.metric("Real Option Value", f"${option_value:.2f}M", "Expansion optionality")
            with col3: st.metric("Total Strategic Value", f"${total_value:.2f}M", f"{'✅ Invest' if total_value > 0 else '❌ Reject / Redesign'}")

            if traditional_npv < 0 and total_value > 0:
                st.warning(f"⚠️ Traditional NPV is negative (${traditional_npv:.2f}M) but real option value makes total strategic value positive (${total_value:.2f}M). This investment should proceed on strategic grounds — traditional NPV UNDERSTATES value.")
            elif total_value > 0:
                st.success(f"✅ Strong investment case. Total strategic value: ${total_value:.2f}M. Recommend proceeding.")
            else:
                st.error(f"❌ Neither traditional NPV nor real option value is sufficient to justify investment at these parameters. Revisit scope or phasing.")

        elif tool == "Digital ROI Calculator":
            st.subheader("💻 Digital Transformation ROI Calculator")
            st.markdown("Build a business case for a digital initiative:")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**One-time Costs ($K):**")
                tech_cost = st.number_input("Technology / Platform:", 0.0, 10000.0, 500.0, 50.0)
                impl_cost = st.number_input("Implementation:", 0.0, 5000.0, 300.0, 25.0)
                training_cost = st.number_input("Training & Change Mgmt:", 0.0, 1000.0, 100.0, 10.0)
                st.markdown("**Annual Ongoing Costs ($K):**")
                annual_cost = st.number_input("Annual licensing / support:", 0.0, 2000.0, 150.0, 10.0)
            with col2:
                st.markdown("**Annual Benefits ($K):**")
                cost_saving = st.number_input("Cost savings (automation, efficiency):", 0.0, 5000.0, 400.0, 25.0)
                revenue_uplift = st.number_input("Revenue uplift (better decisions, new channels):", 0.0, 5000.0, 200.0, 25.0)
                risk_reduction = st.number_input("Risk / error reduction value:", 0.0, 1000.0, 100.0, 10.0)

            wacc_d = st.slider("Discount Rate (%):", 5.0, 15.0, 8.0, 0.5)
            project_years = st.slider("Project Life (years):", 2, 8, 5)

            total_capex = tech_cost + impl_cost + training_cost
            annual_net = cost_saving + revenue_uplift + risk_reduction - annual_cost
            npv_d = -total_capex / 1000 + sum([annual_net / 1000 / (1 + wacc_d / 100) ** t for t in range(1, project_years + 1)])
            payback = (total_capex / 1000) / (annual_net / 1000) if annual_net > 0 else float('inf')
            roi_d = ((annual_net / 1000 * project_years - total_capex / 1000) / (total_capex / 1000)) * 100 if total_capex > 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Total Investment", f"${total_capex/1000:.2f}M")
            with col2: st.metric("NPV", f"${npv_d:.2f}M", "✅ Invest" if npv_d > 0 else "❌ Reconsider")
            with col3: st.metric("Payback Period", f"{payback:.1f} years" if payback != float('inf') else "N/A")
            st.metric("Simple ROI (project life)", f"{roi_d:.1f}%")

        else:  # Disruption Risk Radar
            st.subheader("📡 Disruption Risk Radar")
            st.markdown("Assess your industry's vulnerability to digital disruption:")
            questions_d = [
                "Your product or service can be delivered digitally without physical presence",
                "Information asymmetry is a key part of your business model",
                "Customers find your current experience inconvenient or costly",
                "Venture capital is actively funding startups targeting your market",
                "Your current cost structure is significantly higher than a digital-native competitor could achieve",
                "Platform models could aggregate your supply side and serve customers directly",
                "A 10× improvement in customer experience is technically achievable at lower cost"
            ]
            disruption_score = 0
            for i, q in enumerate(questions_d):
                ans = st.radio(f"**{q}**", ["Yes — definitely (3)", "Partially (2)", "Unlikely (1)", "No (0)"], key=f"dr_{i}", horizontal=True)
                disruption_score += int(ans.split("(")[1].replace(")", ""))

            max_score = len(questions_d) * 3
            pct = disruption_score / max_score * 100
            if st.button("🎯 Assess Disruption Risk"):
                st.metric("Disruption Vulnerability Score", f"{disruption_score}/{max_score}", f"{pct:.0f}%")
                if pct >= 70:
                    st.error(f"🚨 **HIGH disruption risk ({pct:.0f}%)** — Strategic priority: invest in digital transformation NOW. Disrupt yourself before someone else does.")
                elif pct >= 40:
                    st.warning(f"⚠️ **MODERATE disruption risk ({pct:.0f}%)** — Monitor digital threats closely. Begin building digital capabilities and customer experience improvements.")
                else:
                    st.success(f"✅ **LOWER disruption risk ({pct:.0f}%)** — Some resilience to digital disruption. Maintain awareness and invest in H2/H3 horizons.")

    with tab4:
        st.header("Visualizations")

        st.subheader("3-Horizon Innovation Investment Model")
        horizons = ["H1: Core (70%)", "H2: Emerging (20%)", "H3: Visionary (10%)"]
        budgets = [70, 20, 10]
        time_frames = ["0–2 years", "2–5 years", "5+ years"]
        fig_3h = go.Figure(go.Bar(
            x=horizons, y=budgets,
            marker_color=["#1B3A6B", "#0D7377", "#D97706"],
            text=[f"{b}% of innovation budget\n{t}" for b, t in zip(budgets, time_frames)],
            textposition="auto", textfont=dict(color="white", size=12)
        ))
        fig_3h.update_layout(title="3-Horizon Model — Innovation Investment Allocation", yaxis_title="% of Innovation Budget", height=400)
        st.plotly_chart(fig_3h, use_container_width=True)

        st.subheader("Disruption S-Curve — Typical Technology Adoption")
        t = np.linspace(0, 10, 200)
        adoption = 100 / (1 + np.exp(-1.2 * (t - 5)))
        incumbent_revenue = 100 * (1 - adoption / 150)
        fig_scurve = go.Figure()
        fig_scurve.add_trace(go.Scatter(x=t, y=adoption, name="Disruptor Adoption (%)", line=dict(color="#E74C3C", width=3)))
        fig_scurve.add_trace(go.Scatter(x=t, y=incumbent_revenue, name="Incumbent Revenue (%)", line=dict(color="#1B3A6B", width=3, dash="dash")))
        fig_scurve.add_vrect(x0=0, x1=3, fillcolor="#27AE60", opacity=0.1, annotation_text="Window to respond")
        fig_scurve.update_layout(title="Disruption S-Curve — Act in the Window, Not at the Cliff", xaxis_title="Time (years)", yaxis_title="Performance / Revenue (%)", height=400)
        st.plotly_chart(fig_scurve, use_container_width=True)

        st.subheader("Digital Transformation — Cost vs Benefit Over Time")
        years_dt = list(range(1, 6))
        costs_dt = [1350, 350, 275, 200, 200]
        benefits_dt = [300, 1050, 1350, 1500, 1600]
        cumul_cost = np.cumsum(costs_dt)
        cumul_benefit = np.cumsum(benefits_dt)
        fig_dt = go.Figure()
        fig_dt.add_trace(go.Bar(x=years_dt, y=[-c for c in costs_dt], name="Annual Cost", marker_color="#E74C3C"))
        fig_dt.add_trace(go.Bar(x=years_dt, y=benefits_dt, name="Annual Benefit", marker_color="#27AE60"))
        fig_dt.add_trace(go.Scatter(x=years_dt, y=cumul_benefit - cumul_cost, name="Cumulative Net Value", line=dict(color="#1B3A6B", width=3), mode="lines+markers"))
        fig_dt.add_hline(y=0, line_color="black", line_width=1, line_dash="dash")
        fig_dt.update_layout(title="Digital Transformation — Cost vs Benefit Profile", barmode="relative", yaxis_title="Value ($K)", height=420)
        st.plotly_chart(fig_dt, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. In Christensen's theory, disruption typically begins with:**")
        q1 = st.radio("", [
            "A superior product targeting the incumbent's best customers",
            "A simpler, cheaper product initially targeting low-end or non-consumers",
            "A heavily funded startup attacking from the premium end",
            "A government regulation that forces incumbents to change"
        ], key="bs6q1")
        if st.button("Check Answer", key="bs6c1"):
            if q1 == "A simpler, cheaper product initially targeting low-end or non-consumers":
                st.success("✅ Correct! Disruptors start below the incumbent's radar — with inferior but cheaper products — then improve and move upmarket.")
            else:
                st.error("❌ Incorrect. Disruption starts at the low end or non-consumption — initially ignored by incumbents.")

        st.markdown("---")
        st.markdown("**2. In the 3-Horizon model, what percentage of innovation budget should typically go to H1 (core)?**")
        q2 = st.radio("", ["10%", "30%", "50%", "70%"], key="bs6q2")
        if st.button("Check Answer", key="bs6c2"):
            if q2 == "70%":
                st.success("✅ Correct! H1 (defend and extend core) receives ~70%, H2 ~20%, H3 ~10%.")
            else:
                st.error("❌ Incorrect. The typical allocation is 70% H1, 20% H2, 10% H3.")

        st.markdown("---")
        st.markdown("**3. Real option value adds to NPV by capturing:**")
        q3 = st.radio("", [
            "The value of sunk costs already incurred",
            "The value of flexibility — ability to expand, defer, or abandon as information emerges",
            "The guaranteed synergies from digital investment",
            "The accounting book value of technology assets"
        ], key="bs6q3")
        if st.button("Check Answer", key="bs6c3"):
            if q3 == "The value of flexibility — ability to expand, defer, or abandon as information emerges":
                st.success("✅ Correct! Real options capture the value of strategic flexibility — traditional NPV misses this completely.")
            else:
                st.error("❌ Incorrect. Real option value = value of flexibility (expand if success, abandon if failure). Traditional NPV ignores this.")

        st.markdown("---")
        st.markdown("**4. Digital transformation is BEST described as:**")
        q4 = st.radio("", [
            "An IT department project to upgrade software",
            "A strategic repositioning of the business enabled by technology",
            "Moving all data to the cloud",
            "Building a mobile app for customers"
        ], key="bs6q4")
        if st.button("Check Answer", key="bs6c4"):
            if q4 == "A strategic repositioning of the business enabled by technology":
                st.success("✅ Correct! Digital transformation is fundamentally strategic — it changes how value is created, delivered, and captured.")
            else:
                st.error("❌ Incorrect. Digital transformation is a STRATEGIC change — technology is the enabler, not the goal.")

        st.markdown("---")
        st.markdown("**5. Which innovation type involves reconfiguring existing components in a new architecture?**")
        q5 = st.radio("", ["Incremental", "Radical", "Architectural", "Disruptive"], key="bs6q5")
        if st.button("Check Answer", key="bs6c5"):
            if q5 == "Architectural":
                st.success("✅ Correct! Architectural innovation combines existing components in a new configuration — e.g. the laptop (existing components, new portable configuration).")
            else:
                st.error("❌ Incorrect. Architectural innovation = existing components in a new configuration (e.g. laptop from desktop components).")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Types of Innovation
        | Type | Risk | Finance Approach |
        |------|------|-----------------|
        | Incremental | Low | NPV; operating budget |
        | Architectural | Medium | Business case; IRR |
        | Radical | High | Portfolio + real options |
        | Disruptive | Extreme | Small bets; option to scale |

        ### 2. 3-Horizon Model
        ```
        H1 (70%) → Defend and extend core → ROIC metric
        H2 (20%) → Build emerging businesses → Revenue growth metric
        H3 (10%) → Create future options → Option value metric
        ```

        ### 3. Disruption — Act Early
        - Disruption starts at low end → improves → attacks core
        - The window to respond is early (Green Zone)
        - Finance role: quantify displacement risk BEFORE it's obvious

        ### 4. Digital Transformation ROI
        ```
        Benefits: Cost savings + Revenue uplift + Risk reduction
        Costs: Technology + Implementation + Training + Annual OpEx
        NPV = PV(Benefits) − Total Investment
        ```

        ### 5. Real Options
        ```
        Total Strategic Value = Traditional NPV + Real Option Value
        Real Option Value = Prob(Success) × Max(0, Phase 2 NPV − Phase 2 Cost)
        ```
        """)
        st.subheader("📌 Key Formulas")
        st.code("Real Option Value = P(Success) × max(0, Phase 2 NPV − Phase 2 Investment)")
        st.code("Digital ROI = (Total Benefits − Total Costs) / Total Investment × 100%")
        st.code("Total Strategic Value = Traditional NPV + Real Option Value")
        st.success("🎓 **Module 6 Complete!** You can now evaluate innovation investments, assess disruption risk, and build financial cases for digital transformation.")
        st.info("💡 **Next**: Module 7 — Strategy & Financial Performance: Linking Strategy to Value")

if __name__ == "__main__":
    show()