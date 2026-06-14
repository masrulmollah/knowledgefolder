import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🌐 Module 10: Global Strategy, ESG & Stakeholder Value")
    st.markdown("*Navigate international expansion, integrate ESG into financial strategy, and create long-term value for all stakeholders*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Global vs Multidomestic vs Transnational Strategy")
        st.markdown("""
        Firms competing internationally must balance **global efficiency** (standardisation for cost) against
        **local responsiveness** (customisation for market fit).
        """)
        global_strat = {
            "Strategy Type": ["Global", "Multidomestic", "Transnational", "International (Export)"],
            "Logic": [
                "Standardise globally for maximum scale and cost efficiency",
                "Customise fully to each local market",
                "Optimise globally AND respond locally — the hardest to execute",
                "Sell existing products abroad with minimal adaptation"
            ],
            "Cost Structure": ["Lowest", "Highest", "Medium", "Low initially"],
            "Revenue Flexibility": ["Low", "High", "High", "Medium"],
            "Financial Risk": ["FX, geopolitical concentration", "High cost base, complexity", "Execution complexity, dual costs", "Minimal — low commitment"],
            "Examples": ["Apple, Boeing, Intel", "Unilever (local brands), McDonald's menus", "P&G, Nestlé", "Small exporters, early-stage MNCs"]
        }
        st.dataframe(pd.DataFrame(global_strat), use_container_width=True, hide_index=True)

        st.subheader("2. CAGE Distance Framework")
        st.markdown("""
        The **CAGE framework** (Ghemawat) identifies the four dimensions of 'distance' between countries
        that increase the cost and risk of international expansion.

        | Dimension | Definition | Finance Impact |
        |-----------|-----------|----------------|
        | **Cultural (C)** | Language, norms, values, trust, religion | Marketing adaptation cost, talent cost, local brand investment |
        | **Administrative (A)** | Colonial ties, trade agreements, legal systems, political risk | Regulatory compliance cost, tariffs, FX controls, governance |
        | **Geographic (G)** | Physical distance, time zones, border access | Logistics cost, supply chain complexity, travel cost |
        | **Economic (E)** | Income differences, infrastructure, labour costs | Pricing strategy, wage cost advantage, market size potential |

        **Finance use**: CAGE analysis helps quantify the cost of market entry
        and compare alternative international expansion options on a risk-adjusted basis.
        """)

        st.subheader("3. Internationalisation Modes — Entry Strategy")
        entry_modes = {
            "Entry Mode": ["Exporting", "Licensing / Franchising", "Strategic Alliance / JV", "Greenfield Investment", "Acquisition"],
            "Control Level": ["Low", "Low-Medium", "Medium", "High", "Full"],
            "Investment Required": ["Minimal", "Low", "Medium", "Very High", "Very High + Premium"],
            "Speed to Market": ["Fast", "Fast", "Medium", "Slow (3–5 yrs)", "Fast"],
            "Financial Profile": [
                "Low capex; revenue via sales; FX exposure on receivables",
                "Royalty income stream; capital-light; limits upside",
                "Shared investment; shared risk; shared upside",
                "Full P&L ownership; highest risk; highest long-term return",
                "Immediate scale; acquisition premium; synergy realisation required"
            ],
            "Best When": [
                "Testing market; low strategic commitment required",
                "IP is valuable; local knowledge needed; low risk tolerance",
                "Market knowledge gaps; regulatory requirements; cost sharing needed",
                "Full control needed; no suitable acquisition target; long-term strategic market",
                "Speed critical; capability needed; acquiree available at fair value"
            ]
        }
        st.dataframe(pd.DataFrame(entry_modes), use_container_width=True, hide_index=True)

        st.subheader("4. ESG as Strategic Imperative")
        st.markdown("""
        **ESG (Environmental, Social, Governance)** has moved from a compliance obligation to a **strategic priority**
        that affects cost of capital, market access, talent, and long-term value creation.

        | ESG Pillar | Strategic Dimensions | Financial Impact |
        |-----------|---------------------|-----------------|
        | **Environmental (E)** | Net zero targets, carbon pricing, energy transition, resource efficiency | Carbon cost, stranded asset risk, green capex, energy savings |
        | **Social (S)** | Employee wellbeing, DEI, supply chain ethics, community impact | Talent attraction/retention cost, brand value, litigation risk |
        | **Governance (G)** | Board independence, executive pay, transparency, tax integrity | Cost of capital, governance premium, investor access |

        **ESG and the cost of capital:**
        - Strong ESG profile → lower perceived risk → lower cost of equity and debt
        - ESG-linked bonds carry 15–40bp interest saving
        - Poor ESG profile → exclusion from ESG funds (now 40%+ of AUM) → higher cost of capital
        """)

        st.subheader("5. Stakeholder Strategy & Long-Term Value")
        st.markdown("""
        **Stakeholder capitalism** argues companies should create value for all stakeholders
        (employees, customers, suppliers, communities, environment) — not just shareholders.

        **Freeman's Stakeholder Theory**: Long-term shareholder value is BEST delivered by
        managing all key stakeholder relationships well — not by sacrificing them for short-term profit.

        **Integrated Reporting (IIRC Framework)** reports on six capitals:
        | Capital | Definition | Finance Measurement |
        |---------|-----------|---------------------|
        | Financial | Monetary capital and equity | P&L, BS, Cash Flow |
        | Manufactured | Physical infrastructure | Asset values, capex, depreciation |
        | Intellectual | IP, patents, knowledge systems | Intangible asset valuation |
        | Human | People skills, motivation, culture | HR investment, productivity metrics |
        | Social & Relationship | Brand, community, stakeholder trust | Brand valuation, NPS, community investment |
        | Natural | Environment, resources, ecosystems | Carbon footprint, environmental provisions |
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: CAGE Distance Analysis — UK Retailer Expanding to India vs Germany")
        cage_compare = {
            "CAGE Dimension": ["Cultural Distance", "Administrative Distance", "Geographic Distance", "Economic Distance"],
            "UK → Germany": [
                "Low — shared Western values; relatively similar consumer culture",
                "Low — both EU trade history; similar legal systems; Euro zone adjacent",
                "Low — 1,000km; same time zone; direct transport links",
                "Low — similar income levels; comparable infrastructure"
            ],
            "UK → India": [
                "High — language diversity; different consumer norms; price sensitivity",
                "High — colonial legacy; different legal system; bureaucracy; FDI restrictions",
                "High — 7,000km; 5.5hr time difference; complex logistics",
                "High — income gap; infrastructure variability; price point challenges"
            ],
            "Finance Impact (India premium)": [
                "Higher marketing/localisation cost +$2–4M pa",
                "Legal/compliance cost +$1–2M pa; longer setup timeline",
                "Logistics cost 3× Germany; inventory lead times 6 weeks vs 1 week",
                "Lower ASP; higher volume required; different margin profile"
            ]
        }
        st.dataframe(pd.DataFrame(cage_compare), use_container_width=True, hide_index=True)
        st.info("💡 **Finance conclusion**: Germany entry requires 60% less upfront investment and delivers positive ROIC 2 years sooner than India. India has larger long-term TAM but requires 3–5 year strategic commitment and significantly higher risk-adjusted cost of entry.")

        st.subheader("Example 2: ESG Financial Integration — Carbon Pricing Impact")
        st.markdown("""
        **Company: Industrial Manufacturer — Carbon Pricing Scenario Analysis**

        | Carbon Price ($/tonne CO₂) | Annual Carbon Cost | EBITDA Impact | Strategic Response |
        |---------------------------|-------------------|---------------|-------------------|
        | $0 (today's US level) | $0 | 0% | No immediate action |
        | $30 (EU ETS current) | -$4.5M | -2.3% | Begin energy efficiency investment |
        | $65 (IPCC recommended) | -$9.8M | -4.9% | Accelerate decarbonisation programme |
        | $100 (2030 trajectory) | -$15.0M | -7.5% | Carbon-intensive assets become stranded |
        | $150 (2040 trajectory) | -$22.5M | -11.3% | Business model transformation required |

        **Finance action**: Build carbon price scenarios into LRP from $30 upwards.
        A $65/tonne carbon price justifies a $25M green capex programme on 4-year payback.
        """)
        st.warning("⚠️ **Climate risk is financial risk**: Companies failing to account for carbon pricing in their long-range financial plans are presenting a materially misleading picture to investors and boards.")

        st.subheader("Example 3: Stakeholder Value Map — Financial Services Firm")
        stakeholder_data = {
            "Stakeholder": ["Shareholders", "Employees", "Customers", "Regulators", "Communities", "Environment"],
            "Value They Need": [
                "ROIC > WACC; sustainable dividend; transparent governance",
                "Fair pay; development; career path; safe work environment; inclusion",
                "Fair pricing; data privacy; accessible products; good service",
                "Compliance; stability; consumer protection; systemic safety",
                "Local employment; tax contribution; responsible lending",
                "Carbon footprint reduction; responsible investment screening"
            ],
            "Strategic Investment": ["Capital returns programme; governance improvements", "£45M talent & DEI programme", "£20M digital experience investment", "£15M compliance & RegTech", "£5M community investment fund", "£30M green finance product suite"],
            "Financial Return": ["Lower cost of equity; better rating", "18% lower turnover → £12M/yr saving", "+8% NPS → 5% revenue uplift", "Zero fines; regulatory approval speed", "ESG score improvement; ESG bond access", "Green bond saving 25bp; ESG index inclusion"]
        }
        st.dataframe(pd.DataFrame(stakeholder_data), use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "CAGE Distance Analyser",
            "ESG Financial Impact Calculator",
            "Stakeholder Value Mapping Tool"
        ])

        if tool == "CAGE Distance Analyser":
            st.subheader("🌍 CAGE Distance Analyser")
            st.markdown("Score the distance between your home market and target market (1 = very similar, 5 = very different):")
            col1, col2 = st.columns(2)
            with col1:
                home_market = st.text_input("Home Market:", value="United Kingdom")
                target_market = st.text_input("Target Market:", value="Brazil")
            with col2:
                st.markdown(" ")

            cage_dims = {
                "Cultural (C)": {"desc": "Language, values, consumer norms, religion, social norms", "weight": 0.25},
                "Administrative (A)": {"desc": "Legal system, political risk, trade agreements, FDI rules", "weight": 0.30},
                "Geographic (G)": {"desc": "Physical distance, time zones, logistics, border access", "weight": 0.20},
                "Economic (E)": {"desc": "Income levels, infrastructure, labour costs, consumer purchasing power", "weight": 0.25}
            }
            scores_cage = {}
            for dim, info in cage_dims.items():
                st.markdown(f"**{dim}** — *{info['desc']}*")
                scores_cage[dim] = st.slider("Distance:", 1, 5, 3, key=f"cage_{dim}")

            weighted_distance = sum(scores_cage[d] * cage_dims[d]["weight"] for d in scores_cage)
            if st.button("📊 Assess Market Entry Complexity"):
                col1, col2 = st.columns(2)
                with col1:
                    for dim, score in scores_cage.items():
                        status = "🔴 High" if score >= 4 else ("🟠 Medium" if score >= 3 else "🟢 Low")
                        st.metric(f"{dim} Distance", f"{score}/5", status)
                with col2:
                    st.metric("Weighted CAGE Distance", f"{weighted_distance:.2f}/5")
                    if weighted_distance >= 4:
                        st.error("🔴 **Very High Complexity Market** — significant investment and 3–5yr commitment needed. Consider JV/partnership to share risk.")
                    elif weighted_distance >= 3:
                        st.warning("🟠 **High Complexity Market** — substantial adaptation and local expertise required. Phase entry recommended.")
                    elif weighted_distance >= 2:
                        st.info("🟡 **Moderate Complexity** — manageable with local partner. Direct investment viable with appropriate planning.")
                    else:
                        st.success("🟢 **Low Complexity** — natural expansion market. Direct entry with moderate adaptation. High likelihood of early ROIC.")

                est_entry_cost = weighted_distance * 5
                est_payback = 1.5 + weighted_distance * 0.8
                st.markdown(f"**Estimated Entry Investment Premium**: ~${est_entry_cost:.0f}M vs low-distance market")
                st.markdown(f"**Estimated Payback Period**: ~{est_payback:.1f} years to positive ROIC")

        elif tool == "ESG Financial Impact Calculator":
            st.subheader("🌱 ESG Financial Impact Calculator")
            col1, col2 = st.columns(2)
            with col1:
                revenue_esg = st.number_input("Annual Revenue ($M):", 10.0, 5000.0, 500.0, 10.0)
                ebitda_pct_esg = st.slider("Current EBITDA Margin (%):", 5.0, 50.0, 18.0, 0.5)
                carbon_emissions = st.number_input("Annual CO₂ Emissions (000 tonnes):", 0.1, 1000.0, 150.0, 5.0)
                carbon_price = st.slider("Carbon Price ($/tonne):", 0, 200, 65, 5)
            with col2:
                esg_investment = st.number_input("Annual ESG Investment ($M):", 0.0, 100.0, 10.0, 1.0)
                energy_saving_pct = st.slider("Energy/efficiency savings from ESG investment (%):", 0.0, 30.0, 8.0, 0.5)
                wacc_reduction_esg = st.slider("Estimated WACC reduction from ESG (bp):", 0, 100, 30, 5)
                talent_saving_pct = st.slider("Talent retention improvement (% turnover reduction):", 0.0, 30.0, 12.0, 1.0)

            current_ebitda = revenue_esg * ebitda_pct_esg / 100
            carbon_cost = carbon_emissions * carbon_price / 1000
            energy_saving = revenue_esg * 0.05 * energy_saving_pct / 100
            talent_saving = revenue_esg * 0.02 * talent_saving_pct / 100
            net_esg_benefit = energy_saving + talent_saving - esg_investment - carbon_cost
            new_ebitda = current_ebitda + net_esg_benefit
            new_margin = new_ebitda / revenue_esg * 100

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Current EBITDA", f"${current_ebitda:.1f}M", f"{ebitda_pct_esg:.1f}%")
                st.metric("Carbon Exposure", f"-${carbon_cost:.1f}M/yr", f"@${carbon_price}/tonne")
                st.metric("ESG Investment Cost", f"-${esg_investment:.1f}M/yr")
            with col2:
                st.metric("Energy/Efficiency Saving", f"+${energy_saving:.1f}M/yr")
                st.metric("Talent Retention Saving", f"+${talent_saving:.1f}M/yr")
                st.metric("Net ESG EBITDA Impact", f"${net_esg_benefit:+.1f}M/yr", f"New margin: {new_margin:.1f}%")

            wacc_saving = revenue_esg * 1.5 * wacc_reduction_esg / 10000
            st.metric("WACC Reduction → Cost of Capital Saving (annual)", f"${wacc_saving:.1f}M equivalent")
            if net_esg_benefit > 0:
                st.success(f"✅ ESG investment is NPV-positive: net benefit ${net_esg_benefit:.1f}M/yr + WACC saving ${wacc_saving:.1f}M. Business case is compelling.")
            else:
                st.warning(f"⚠️ ESG investment is currently NPV-negative by ${abs(net_esg_benefit):.1f}M/yr at current carbon price. Increases as carbon price rises. Build in WACC reduction and brand value for full picture.")

        else:  # Stakeholder Mapping
            st.subheader("🗺️ Stakeholder Value Mapping Tool")
            stakeholders = ["Shareholders", "Employees", "Customers", "Regulators", "Suppliers", "Community", "Environment"]
            st.markdown("Rate each stakeholder on **Strategic Importance (1–5)** and **Current Satisfaction (1–5)**:")
            mapping_data = []
            for s in stakeholders:
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1: st.markdown(f"**{s}**")
                with col2: importance = st.slider("Importance:", 1, 5, 3, key=f"sm_imp_{s}")
                with col3: satisfaction = st.slider("Satisfaction:", 1, 5, 3, key=f"sm_sat_{s}")
                priority = "🔴 Highest" if importance >= 4 and satisfaction <= 2 else \
                           "🟠 High" if importance >= 4 and satisfaction == 3 else \
                           "🟡 Monitor" if importance >= 3 else "🟢 Maintain"
                invest_priority = "Urgent investment" if priority in ["🔴 Highest", "🟠 High"] else "Monitor" if priority == "🟡 Monitor" else "Sustain"
                mapping_data.append({"Stakeholder": s, "Importance": importance, "Satisfaction": satisfaction, "Priority": priority, "Action": invest_priority})
            st.dataframe(pd.DataFrame(mapping_data), use_container_width=True, hide_index=True)
            urgent = [r["Stakeholder"] for r in mapping_data if "Urgent" in r["Action"]]
            if urgent:
                st.error(f"🔴 Urgent stakeholder investment required: {', '.join(urgent)} — high importance, low satisfaction creates strategic and reputational risk.")

    with tab4:
        st.header("Visualizations")

        st.subheader("Globalisation Strategy — Integration vs Responsiveness Matrix")
        strategies_g = [("Global", 1.2, 4.2), ("Transnational", 3.8, 4.0), ("International (Export)", 1.0, 1.5), ("Multidomestic", 3.8, 1.2)]
        fig_intresp = go.Figure()
        for name, x, y in strategies_g:
            fig_intresp.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", text=[name],
                                             textposition="top center", marker=dict(size=50, color="#1B3A6B", opacity=0.8),
                                             textfont=dict(size=12), showlegend=False))
        fig_intresp.update_layout(title="Global Strategy Matrix: Integration vs Local Responsiveness", height=450,
                                  xaxis=dict(title="Local Responsiveness →", range=[0, 5], tickvals=[]),
                                  yaxis=dict(title="Global Integration →", range=[0, 5], tickvals=[]))
        fig_intresp.add_vline(x=2.5, line_dash="dash", line_color="#CBD5E1")
        fig_intresp.add_hline(y=2.5, line_dash="dash", line_color="#CBD5E1")
        st.plotly_chart(fig_intresp, use_container_width=True)

        st.subheader("ESG Score vs Cost of Capital — Industry Benchmark")
        esg_scores = [25, 35, 42, 50, 58, 63, 70, 75, 80, 85]
        cost_of_capital = [10.5, 10.0, 9.5, 9.2, 8.8, 8.5, 8.2, 7.9, 7.6, 7.2]
        fig_esg_coc = go.Figure()
        fig_esg_coc.add_trace(go.Scatter(x=esg_scores, y=cost_of_capital, mode="lines+markers",
                                         line=dict(color="#1B3A6B", width=3), marker=dict(size=10, color="#D97706"),
                                         name="Industry benchmark"))
        fig_esg_coc.update_layout(title="ESG Score vs Cost of Capital — Higher ESG → Lower WACC",
                                  xaxis_title="ESG Score (0–100)", yaxis_title="Cost of Capital (WACC %)", height=400)
        st.plotly_chart(fig_esg_coc, use_container_width=True)

        st.subheader("Stakeholder Importance vs Satisfaction Map")
        s_names = ["Shareholders", "Employees", "Customers", "Regulators", "Suppliers", "Community"]
        s_importance = [5, 4, 5, 4, 3, 3]
        s_satisfaction = [4, 2, 3, 4, 4, 3]
        s_colors = ["#27AE60" if sat >= 4 else "#E74C3C" if sat <= 2 else "#E67E22" for sat in s_satisfaction]
        fig_smap = go.Figure()
        for name, imp, sat, color in zip(s_names, s_importance, s_satisfaction, s_colors):
            fig_smap.add_trace(go.Scatter(x=[sat], y=[imp], mode="markers+text", text=[name],
                                          textposition="top center", marker=dict(size=40, color=color, opacity=0.8),
                                          textfont=dict(size=11), showlegend=False))
        fig_smap.add_vline(x=3, line_dash="dash", line_color="#CBD5E1")
        fig_smap.add_hline(y=3, line_dash="dash", line_color="#CBD5E1")
        fig_smap.add_annotation(x=1.5, y=4.8, text="🔴 Urgent — high importance, low satisfaction", font=dict(size=10, color="#E74C3C"), showarrow=False)
        fig_smap.update_layout(title="Stakeholder Map: Importance vs Satisfaction", height=450,
                               xaxis=dict(title="Current Satisfaction →", range=[0, 6]),
                               yaxis=dict(title="Strategic Importance →", range=[0, 6]))
        st.plotly_chart(fig_smap, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. The CAGE framework stands for:**")
        q1 = st.radio("", [
            "Cost, Access, Growth, Efficiency",
            "Cultural, Administrative, Geographic, Economic",
            "Competitive, Agile, Global, Environmental",
            "Capital, Allocation, Governance, Execution"
        ], key="bs10q1")
        if st.button("Check Answer", key="bs10c1"):
            if q1 == "Cultural, Administrative, Geographic, Economic":
                st.success("✅ Correct! CAGE = Cultural, Administrative, Geographic, Economic — the four dimensions of distance that affect international expansion cost and risk.")
            else:
                st.error("❌ Incorrect. CAGE = Cultural, Administrative, Geographic, Economic distance framework for international strategy.")

        st.markdown("---")
        st.markdown("**2. A transnational strategy attempts to:**")
        q2 = st.radio("", [
            "Serve only domestic markets with a global brand",
            "Achieve both global efficiency AND local responsiveness simultaneously",
            "Export products without any local adaptation",
            "Fully customise to each local market at maximum cost"
        ], key="bs10q2")
        if st.button("Check Answer", key="bs10c2"):
            if q2 == "Achieve both global efficiency AND local responsiveness simultaneously":
                st.success("✅ Correct! Transnational strategy is the most complex — it seeks global scale economies AND local market adaptation. Examples: Nestlé, P&G.")
            else:
                st.error("❌ Incorrect. Transnational = combining global integration efficiency with local responsiveness — the hardest strategy to execute.")

        st.markdown("---")
        st.markdown("**3. A strong ESG profile primarily affects a company's finances through:**")
        q3 = st.radio("", [
            "Increasing capital expenditure only",
            "Lowering the cost of capital and improving talent and customer loyalty",
            "Reducing revenue from non-ESG customers",
            "No measurable financial impact — purely reputational"
        ], key="bs10q3")
        if st.button("Check Answer", key="bs10c3"):
            if q3 == "Lowering the cost of capital and improving talent and customer loyalty":
                st.success("✅ Correct! ESG reduces cost of capital (investor risk premium), attracts talent, and builds customer loyalty — all with measurable financial value.")
            else:
                st.error("❌ Incorrect. ESG has direct financial impact: lower WACC, better talent retention, customer preference, and reduced regulatory risk.")

        st.markdown("---")
        st.markdown("**4. In Integrated Reporting, 'Natural Capital' refers to:**")
        q4 = st.radio("", [
            "The company's cash and investment portfolio",
            "Physical infrastructure and manufacturing assets",
            "Environmental resources, ecosystems, and the company's impact on them",
            "Intellectual property and patents"
        ], key="bs10q4")
        if st.button("Check Answer", key="bs10c4"):
            if q4 == "Environmental resources, ecosystems, and the company's impact on them":
                st.success("✅ Correct! Natural Capital in Integrated Reporting covers environmental resources — carbon footprint, water, biodiversity, and ecosystem services.")
            else:
                st.error("❌ Incorrect. Natural Capital = environmental resources and ecosystems — carbon, water, land, biodiversity.")

        st.markdown("---")
        st.markdown("**5. The entry mode requiring the LEAST financial commitment for international expansion is:**")
        q5 = st.radio("", ["Greenfield investment", "Acquisition", "Exporting", "Wholly-owned subsidiary"], key="bs10q5")
        if st.button("Check Answer", key="bs10c5"):
            if q5 == "Exporting":
                st.success("✅ Correct! Exporting requires minimal capex — test the market with existing products before deeper commitment.")
            else:
                st.error("❌ Incorrect. Exporting requires the least capital commitment — it is the lowest-risk, lowest-control entry mode.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Global Strategy Options
        | Strategy | Efficiency | Responsiveness | Best For |
        |----------|-----------|---------------|---------|
        | Global | High | Low | Standardised products (Intel, Boeing) |
        | Multidomestic | Low | High | Culturally-sensitive products |
        | Transnational | High | High | Complex MNCs (Nestlé, P&G) |
        | International | Medium | Low | Early-stage expansion |

        ### 2. CAGE Distance — Entry Cost Drivers
        ```
        Cultural   → Marketing/adaptation cost
        Administrative → Legal/compliance/regulatory cost
        Geographic → Logistics and supply chain cost
        Economic   → Pricing, wage, and market sizing impact
        ```

        ### 3. ESG Financial Impact
        | ESG Benefit | Financial Mechanism |
        |-------------|---------------------|
        | Lower WACC | ESG premium from investors (15–40bp saving) |
        | Cost savings | Energy efficiency, waste reduction |
        | Talent retention | Lower recruitment/training cost |
        | Revenue uplift | Customer preference for ESG brands |
        | Risk reduction | Regulatory fines, carbon cost avoided |

        ### 4. Stakeholder Value Framework
        ```
        High Importance + Low Satisfaction → Urgent investment priority
        High Importance + High Satisfaction → Maintain and protect
        Low Importance + Low Satisfaction → Monitor
        Low Importance + High Satisfaction → Sustain efficiently
        ```
        """)
        st.subheader("📌 Key Formulas")
        st.code("CAGE Weighted Distance = Σ (Score(dimension) × Weight(dimension))")
        st.code("ESG WACC Benefit ($) = Enterprise Value × WACC Reduction (bp) / 10,000")
        st.code("Carbon Cost ($) = Emissions (tonnes) × Carbon Price ($/tonne)")
        st.code("Entry Mode Score = f(Control needed, Capital available, Speed required, Risk tolerance)")
        st.success("🎓 **Module 10 Complete!** You can now design global entry strategies, integrate ESG into financial modelling, and build a stakeholder value framework.")
        st.info("💡 **Next**: Module 11 — Strategic Finance: FP&A, Scenario Modelling & Business Cases")

if __name__ == "__main__":
    show()