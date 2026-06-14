import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🔬 Module 3: Internal Analysis & Competitive Advantage")
    st.markdown("*Identify unique capabilities, analyse the value chain, and convert internal strengths into sustainable financial advantage*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Why Analyse Internally?")
        st.markdown("""
        External analysis tells you where to compete. **Internal analysis tells you whether you can win** there.
        Sustainable competitive advantage comes from unique internal resources and capabilities that competitors cannot easily replicate.

        **Finance professional's internal lens:**
        - Which resources are generating ROIC above WACC?
        - Which capabilities are producing pricing power or cost advantage?
        - Where is value being created or destroyed along the value chain?
        - What financial capabilities (balance sheet strength, capital efficiency) act as strategic assets?
        """)

        st.subheader("2. Resource-Based View (RBV) and VRIN Framework")
        st.markdown("""
        The **Resource-Based View** holds that sustainable competitive advantage comes from resources and capabilities
        that are **VRIN**:
        """)
        vrin_data = {
            "VRIN Criterion": ["Valuable (V)", "Rare (R)", "Inimitable (I)", "Non-Substitutable (N)"],
            "Definition": [
                "Enables exploitation of opportunities or neutralisation of threats",
                "Not possessed by many competitors",
                "Cannot be easily copied (causal ambiguity, path dependency, social complexity)",
                "Cannot be replaced by an alternative resource that does the same job"
            ],
            "Finance Examples": [
                "Proprietary data, patent portfolio, brand premium, low-cost manufacturing",
                "Unique algorithmic model, exclusive supplier relationship, scarce specialist talent",
                "Culture of financial discipline, long-built supplier relationships, network effects",
                "Unique treasury expertise, proprietary risk models, CFO-level strategic relationships"
            ],
            "If Missing...": [
                "Competitive parity at best",
                "Temporary advantage only",
                "Competitors copy → advantage erodes",
                "Competitors find workaround → advantage lost"
            ]
        }
        st.dataframe(pd.DataFrame(vrin_data), use_container_width=True, hide_index=True)

        st.subheader("3. Porter's Value Chain Analysis")
        st.markdown("""
        The value chain maps all **activities** a firm performs to create, produce, deliver, and support its product.
        Understanding where costs are incurred and where value is created enables strategic cost management.

        **Primary Activities** (directly create value):
        - **Inbound Logistics**: Receiving, storing, distributing inputs
        - **Operations**: Transforming inputs into the product
        - **Outbound Logistics**: Collecting, storing, distributing outputs to buyers
        - **Marketing & Sales**: Inducing buyers to purchase and enabling them to do so
        - **Service**: Maintaining and enhancing the product's value after sale

        **Support Activities** (enable primary activities):
        - **Firm Infrastructure**: Finance, accounting, legal, management — *the CFO's domain*
        - **Human Resource Management**: Recruiting, training, development
        - **Technology Development**: R&D, process design, product design
        - **Procurement**: Purchasing inputs used across the value chain

        **Finance professional's value chain role:**
        Activity-Based Costing (ABC) maps costs to value chain activities, revealing which activities
        deliver positive value and which represent waste — a direct input to strategic cost management.
        """)

        st.subheader("4. Financial Capabilities as Strategic Assets")
        fin_cap_data = {
            "Financial Capability": ["Strong Balance Sheet", "Working Capital Efficiency", "Cost Structure Advantage", "Capital Allocation Skill", "Financial Flexibility"],
            "Strategic Advantage": [
                "Ability to invest counter-cyclically; survive downturns; fund M&A",
                "Cash generation speed; operational agility; funding growth organically",
                "Economies of scale; lower prices or higher margins than rivals",
                "Deploy capital to highest-return opportunities; outperform peers on ROIC",
                "Ability to pivot strategy quickly without financial stress"
            ],
            "VRIN Assessment": [
                "V✅ R⚠️ I⚠️ N✅ — Valuable but can be built by rivals with time",
                "V✅ R✅ I✅ N✅ — Hard to replicate quickly; embedded in systems and culture",
                "V✅ R⚠️ I⚠️ N⚠️ — Scale-based; eroded as competitors scale",
                "V✅ R✅ I✅ N✅ — People, process, and culture — hard to copy",
                "V✅ R⚠️ I⚠️ N⚠️ — Built through discipline, lost through poor decisions"
            ]
        }
        st.dataframe(pd.DataFrame(fin_cap_data), use_container_width=True, hide_index=True)

        st.subheader("5. SWOT and TOWS Analysis")
        st.markdown("""
        **SWOT** combines internal (Strengths, Weaknesses) and external (Opportunities, Threats) analysis into a single strategic picture.

        **TOWS Matrix** converts SWOT into actionable strategic options:
        | | Opportunities (O) | Threats (T) |
        |-|------------------|-------------|
        | **Strengths (S)** | **SO — Maxi-Maxi**: Use strengths to exploit opportunities | **ST — Maxi-Mini**: Use strengths to counter threats |
        | **Weaknesses (W)** | **WO — Mini-Maxi**: Overcome weaknesses to exploit opportunities | **WT — Mini-Mini**: Minimise weaknesses; avoid threats |

        **Finance professional's TOWS role:**
        Prioritise strategic options using financial criteria — NPV, ROIC, payback period, and strategic risk assessment.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: VRIN Analysis — Amazon Web Services (AWS)")
        aws_vrin = {
            "Resource/Capability": ["Data centre infrastructure at scale", "Proprietary cloud technology stack", "Developer ecosystem (130M+ users)", "Cost efficiency at scale", "Financial strength of parent (Amazon)"],
            "V": ["✅", "✅", "✅", "✅", "✅"],
            "R": ["✅ Few can match scale", "✅ Unique architecture", "✅ Network effects", "✅ Scale-based", "✅ $60B+ annual FCF"],
            "I": ["✅ $100B+ investment required", "✅ 20 years of development", "✅ Ecosystem lock-in", "⚠️ Replicable eventually", "✅ Amazon's retail subsidises investment"],
            "N": ["✅", "✅", "✅", "⚠️", "✅"],
            "Competitive Advantage": ["SCA", "SCA", "SCA", "Temporary", "SCA"]
        }
        st.dataframe(pd.DataFrame(aws_vrin), use_container_width=True, hide_index=True)
        st.info("💡 SCA = Sustainable Competitive Advantage. AWS generates ~70% of Amazon's operating profit while representing only ~16% of revenue — proof of VRIN resources converting to financial value.")

        st.subheader("Example 2: Value Chain Cost Analysis — Manufacturing Company")
        st.markdown("**Objective**: Identify which value chain activities are most cost-intensive and where value is created")
        vc_data = {
            "Value Chain Activity": ["Inbound Logistics", "Operations (Manufacturing)", "Outbound Logistics", "Marketing & Sales", "After-Sales Service",
                                      "Firm Infrastructure (Finance/Admin)", "HR Management", "Technology Development", "Procurement"],
            "Annual Cost ($000s)": [850, 4200, 620, 1100, 380, 450, 320, 780, 290],
            "% of Total Cost": ["8%", "40%", "6%", "11%", "4%", "4%", "3%", "7%", "3%"],
            "Value Delivered": ["Medium", "High", "Medium", "High", "High", "Support", "Support", "High (future)", "Medium"],
            "Strategic Action": [
                "Optimise — negotiate supplier contracts",
                "Protect & invest — core competitive capability",
                "Benchmark vs 3PL alternatives",
                "Invest further — drives revenue premium",
                "Invest — drives retention and recurring revenue",
                "Digitise finance function — reduce 20% cost",
                "Invest in talent — critical for capability",
                "Increase — innovation drives future advantage",
                "Centralise purchasing — 5–8% saving possible"
            ]
        }
        st.dataframe(pd.DataFrame(vc_data), use_container_width=True, hide_index=True)

        st.subheader("Example 3: TOWS Strategic Options with Financial Evaluation")
        tows_data = {
            "TOWS Quadrant": ["SO — Invest for Growth", "ST — Defend Position", "WO — Fix to Capture", "WT — Risk Management"],
            "Strategic Option": [
                "Expand into Asia using strong brand and excess balance sheet capacity",
                "Lock in key supplier contracts to hedge against supply chain disruption threat",
                "Invest in digital capability to capture e-commerce opportunity",
                "Divest non-core low-margin business unit to reduce exposure to market threat"
            ],
            "NPV Estimate": ["$85M", "$12M (cost saving)", "$45M", "$25M (value unlocked)"],
            "Risk Level": ["Medium", "Low", "High", "Low"],
            "Priority": ["🔴 Highest", "🟠 High", "🟡 Medium", "🟢 Implement now"]
        }
        st.dataframe(pd.DataFrame(tows_data), use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "VRIN Capability Assessor",
            "Value Chain Cost Mapper",
            "SWOT / TOWS Builder"
        ])

        if tool == "VRIN Capability Assessor":
            st.subheader("🔍 VRIN Capability Assessor")
            st.markdown("Assess up to 5 of your organisation's key resources/capabilities:")
            num_resources = st.number_input("Number of resources to assess:", 1, 5, 3)
            results = []
            for i in range(int(num_resources)):
                st.markdown(f"**Resource / Capability {i+1}:**")
                col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
                with col1: name = st.text_input("Name:", value=f"Capability {i+1}", key=f"vrin_n_{i}")
                with col2: v = st.checkbox("Valuable", key=f"vrin_v_{i}", value=True)
                with col3: r = st.checkbox("Rare", key=f"vrin_r_{i}")
                with col4: inimit = st.checkbox("Inimitable", key=f"vrin_i_{i}")
                with col5: n = st.checkbox("Non-Substitutable", key=f"vrin_ns_{i}")
                score = sum([v, r, inimit, n])
                if score == 4: status = "🏆 Sustainable Competitive Advantage"
                elif score == 3: status = "⚡ Temporary Advantage (strengthen remaining)"
                elif score == 2: status = "⚠️ Competitive Parity"
                else: status = "❌ Competitive Disadvantage"
                results.append({"Capability": name, "V": "✅" if v else "❌", "R": "✅" if r else "❌",
                                "I": "✅" if inimit else "❌", "N": "✅" if n else "❌", "Score": f"{score}/4", "Status": status})
            st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

        elif tool == "Value Chain Cost Mapper":
            st.subheader("🔗 Value Chain Cost Mapper")
            activities = ["Inbound Logistics", "Operations", "Outbound Logistics", "Marketing & Sales", "Service",
                         "Firm Infrastructure", "HR Management", "Technology Development", "Procurement"]
            costs = []
            values = []
            st.markdown("Enter cost ($000s) and value delivered (1=low → 5=high) for each activity:")
            for act in activities:
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1: st.markdown(f"**{act}**")
                with col2: cost = st.number_input("Cost ($000s)", 0.0, value=500.0, step=50.0, key=f"vc_{act}")
                with col3: value = st.slider("Value", 1, 5, 3, key=f"vv_{act}")
                costs.append(cost)
                values.append(value)

            if st.button("📊 Analyse Value Chain"):
                total_cost = sum(costs)
                vc_df = pd.DataFrame({"Activity": activities, "Cost ($000s)": costs, "Value Score": values,
                                      "Cost %": [f"{c/total_cost*100:.1f}%" if total_cost > 0 else "0%" for c in costs],
                                      "Value/Cost Ratio": [f"{v/c*1000:.2f}" if c > 0 else "N/A" for v, c in zip(values, costs)]})
                st.dataframe(vc_df, use_container_width=True, hide_index=True)
                low_value_high_cost = [(activities[i], costs[i]) for i in range(len(activities)) if values[i] <= 2 and costs[i] >= np.mean(costs)]
                if low_value_high_cost:
                    st.warning(f"⚠️ **Strategic Cost Alert**: {', '.join([x[0] for x in low_value_high_cost])} — high cost but low value delivered. Consider restructuring or outsourcing.")

        else:  # SWOT/TOWS Builder
            st.subheader("⚖️ SWOT / TOWS Strategic Options Builder")
            col1, col2 = st.columns(2)
            with col1:
                strengths = st.text_area("Strengths (one per line):", value="Strong brand\nLow cost structure\nStrong balance sheet", height=100)
                weaknesses = st.text_area("Weaknesses (one per line):", value="Limited digital capability\nHigh staff turnover\nNarrow product range", height=100)
            with col2:
                opportunities = st.text_area("Opportunities (one per line):", value="Growing Asian market\nDigital transformation demand\nESG investment wave", height=100)
                threats = st.text_area("Threats (one per line):", value="New digital competitors\nRising input costs\nRegulatory tightening", height=100)

            if st.button("Generate TOWS Strategic Options"):
                s_list = [s.strip() for s in strengths.split('\n') if s.strip()]
                o_list = [o.strip() for o in opportunities.split('\n') if o.strip()]
                t_list = [t.strip() for t in threats.split('\n') if t.strip()]
                w_list = [w.strip() for w in weaknesses.split('\n') if w.strip()]
                st.markdown("### 🗺️ TOWS Strategic Options")
                st.markdown(f"**SO (Grow):** Use **{s_list[0] if s_list else 'key strength'}** to capture **{o_list[0] if o_list else 'key opportunity'}**")
                st.markdown(f"**ST (Defend):** Deploy **{s_list[-1] if s_list else 'key strength'}** to counter **{t_list[0] if t_list else 'key threat'}**")
                st.markdown(f"**WO (Fix to Win):** Address **{w_list[0] if w_list else 'key weakness'}** to exploit **{o_list[-1] if o_list else 'key opportunity'}**")
                st.markdown(f"**WT (Survive):** Reduce **{w_list[-1] if w_list else 'key weakness'}** exposure to **{t_list[-1] if t_list else 'key threat'}**")
                st.success("✅ Prioritise SO options (highest return) and WT options (survival-critical) first.")

    with tab4:
        st.header("Visualizations")

        st.subheader("VRIN Framework — Competitive Advantage Pathway")
        criteria = ["Valuable", "Rare", "Inimitable", "Non-Substitutable"]
        outcomes = ["Competitive Parity", "Temporary Advantage", "Sustained Advantage", "Sustainable Competitive Advantage"]
        fig_vrin = go.Figure(go.Bar(
            x=criteria, y=[1, 2, 3, 4],
            marker_color=["#AED6F1", "#F9E79F", "#A9DFBF", "#1B3A6B"],
            text=outcomes, textposition="auto"
        ))
        fig_vrin.update_layout(title="VRIN: Building Toward Sustainable Competitive Advantage", yaxis_title="Level of Competitive Advantage", height=400)
        st.plotly_chart(fig_vrin, use_container_width=True)

        st.subheader("Value Chain Cost Distribution")
        vc_names = ["Inbound Logistics", "Operations", "Outbound Logistics", "Marketing & Sales", "Service",
                    "Infrastructure", "HR", "Technology", "Procurement"]
        vc_costs = [850, 4200, 620, 1100, 380, 450, 320, 780, 290]
        vc_colors = ["#2563EB", "#1B3A6B", "#0D7377", "#D97706", "#7C3AED", "#94A3B8", "#64748B", "#0EA5E9", "#6B7280"]
        fig_vc = go.Figure(go.Bar(
            x=vc_names, y=vc_costs,
            marker_color=vc_colors,
            text=[f"${c:,}" for c in vc_costs],
            textposition="auto"
        ))
        fig_vc.update_layout(title="Value Chain Cost Profile ($000s)", xaxis_title="Activity", yaxis_title="Cost ($000s)", height=400)
        st.plotly_chart(fig_vc, use_container_width=True)

        st.subheader("Internal Capability Radar")
        cap_names = ["Financial Strength", "Brand & Reputation", "Technology", "Operations Efficiency", "Talent & Culture", "Innovation"]
        your_scores = [8, 7, 5, 8, 6, 4]
        competitor_scores = [5, 8, 8, 6, 7, 7]
        fig_cap = go.Figure()
        fig_cap.add_trace(go.Scatterpolar(r=your_scores + [your_scores[0]], theta=cap_names + [cap_names[0]],
                                          fill="toself", name="Your Company", line=dict(color="#1B3A6B", width=3), fillcolor="rgba(27,58,107,0.3)"))
        fig_cap.add_trace(go.Scatterpolar(r=competitor_scores + [competitor_scores[0]], theta=cap_names + [cap_names[0]],
                                          fill="toself", name="Competitor", line=dict(color="#E74C3C", width=2, dash="dash"), fillcolor="rgba(231,76,60,0.1)"))
        fig_cap.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), title="Capability Profile vs Competitor", height=420)
        st.plotly_chart(fig_cap, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. A resource is 'inimitable' when:**")
        q1 = st.radio("", [
            "It is very expensive",
            "It is valuable to customers",
            "Competitors cannot easily copy or replicate it",
            "It is used only by your company"
        ], key="bs3q1")
        if st.button("Check Answer", key="bs3c1"):
            if q1 == "Competitors cannot easily copy or replicate it":
                st.success("✅ Correct! Inimitability means the resource/capability is hard to copy due to causal ambiguity, path dependency, or social complexity.")
            else:
                st.error("❌ Incorrect. Inimitable means competitors cannot easily replicate the resource or capability.")

        st.markdown("---")
        st.markdown("**2. Which of these is a SUPPORT activity in Porter's Value Chain?**")
        q2 = st.radio("", ["Operations", "Marketing & Sales", "Firm Infrastructure (Finance, Accounting)", "Outbound Logistics"], key="bs3q2")
        if st.button("Check Answer", key="bs3c2"):
            if q2 == "Firm Infrastructure (Finance, Accounting)":
                st.success("✅ Correct! Firm Infrastructure (including Finance) is a Support Activity — it enables all primary activities.")
            else:
                st.error("❌ Incorrect. Firm Infrastructure is a Support Activity. Operations, Marketing, and Logistics are Primary Activities.")

        st.markdown("---")
        st.markdown("**3. In the TOWS matrix, a 'WO strategy' means:**")
        q3 = st.radio("", [
            "Use strengths to capture opportunities",
            "Address weaknesses to exploit opportunities",
            "Use strengths to counter threats",
            "Minimise weaknesses to avoid threats"
        ], key="bs3q3")
        if st.button("Check Answer", key="bs3c3"):
            if q3 == "Address weaknesses to exploit opportunities":
                st.success("✅ Correct! WO = Mini-Maxi: overcome internal weaknesses to take advantage of external opportunities.")
            else:
                st.error("❌ Incorrect. WO strategy = overcome weaknesses (W) to exploit opportunities (O).")

        st.markdown("---")
        st.markdown("**4. What does VRIN stand for?**")
        q4 = st.radio("", [
            "Variable, Robust, Important, Notable",
            "Valuable, Rare, Inimitable, Non-Substitutable",
            "Viable, Reliable, Innovative, Necessary",
            "Valuable, Resilient, Integrated, Novel"
        ], key="bs3q4")
        if st.button("Check Answer", key="bs3c4"):
            if q4 == "Valuable, Rare, Inimitable, Non-Substitutable":
                st.success("✅ Correct! VRIN identifies the four criteria a resource must meet to deliver Sustainable Competitive Advantage.")
            else:
                st.error("❌ Incorrect. VRIN = Valuable, Rare, Inimitable, Non-Substitutable.")

        st.markdown("---")
        st.markdown("**5. Which of these represents a financial capability acting as a strategic asset?**")
        q5 = st.radio("", [
            "Preparing monthly financial statements",
            "A fortress balance sheet enabling counter-cyclical investment",
            "Filing annual tax returns",
            "Calculating variance analysis"
        ], key="bs3q5")
        if st.button("Check Answer", key="bs3c5"):
            if q5 == "A fortress balance sheet enabling counter-cyclical investment":
                st.success("✅ Correct! Balance sheet strength is a VRIN financial asset — it enables strategic investments when competitors cannot.")
            else:
                st.error("❌ Incorrect. A fortress balance sheet is a strategic financial asset — it creates real competitive advantage.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. VRIN Framework
        ```
        Valuable → Creates advantage (vs. no advantage)
        + Rare → Temporary advantage (vs. parity)
        + Inimitable → Sustained advantage (vs. temporary)
        + Non-Substitutable → SUSTAINABLE COMPETITIVE ADVANTAGE
        ```

        ### 2. Porter's Value Chain
        - **Primary Activities**: Inbound Logistics → Operations → Outbound Logistics → Marketing → Service
        - **Support Activities**: Firm Infrastructure, HR, Technology, Procurement
        - Finance sits in **Firm Infrastructure** but influences every activity
        - Use Activity-Based Costing to map costs to activities

        ### 3. Financial Capabilities as Strategic Assets
        | Asset | Strategic Value |
        |-------|---------------|
        | Strong balance sheet | Counter-cyclical investment, M&A optionality |
        | Working capital efficiency | Cash generation speed, funding flexibility |
        | Cost structure advantage | Pricing power or higher margins than rivals |
        | Capital allocation skill | ROIC consistently above WACC |

        ### 4. SWOT → TOWS
        | Quadrant | Strategy | Focus |
        |----------|----------|-------|
        | SO | Maxi-Maxi | Grow aggressively |
        | ST | Maxi-Mini | Defend position |
        | WO | Mini-Maxi | Fix weaknesses for growth |
        | WT | Mini-Mini | Survival / risk management |

        ### 5. Key Formula
        """)
        st.code("Competitive Advantage Strength = VRIN Score × Depth of Capability × Speed of Deployment")

        st.success("🎓 **Module 3 Complete!** You can now identify an organisation's strategic resources, map the value chain, and translate internal capabilities into competitive advantage.")
        st.info("💡 **Next**: Module 4 — Business-Level Strategy & Competitive Positioning (Porter's Generic Strategies, ROIC, Pricing Power)")

if __name__ == "__main__":
    show()