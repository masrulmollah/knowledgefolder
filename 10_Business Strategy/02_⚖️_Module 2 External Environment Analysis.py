import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🌍 Module 2: External Environment Analysis")
    st.markdown("*Master PESTLE, Porter's Five Forces, and scenario planning to identify strategic opportunities and threats*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Why Analyse the External Environment?")
        st.markdown("""
        No business operates in isolation. External forces shape market attractiveness, competitive intensity, and
        financial performance. Finance professionals must translate external trends into **quantified financial risks and
        opportunities** — informing revenue forecasts, cost projections, and capital allocation decisions.

        **Two levels of external analysis:**
        - **Macro-Environment (PESTLE)** — broad forces affecting all industries
        - **Industry Environment (Five Forces)** — forces specific to your competitive arena
        """)

        st.subheader("2. PESTLE Analysis")
        pestle_data = {
            "Factor": ["Political (P)", "Economic (E)", "Social (S)", "Technological (T)", "Legal (L)", "Environmental (E)"],
            "Key Questions": [
                "Government stability? Trade policy? Tax regime? Regulation?",
                "GDP growth? Inflation? Interest rates? Exchange rates? Unemployment?",
                "Demographics? Consumer attitudes? ESG expectations? Cultural shifts?",
                "Digital disruption? Automation? AI? R&D intensity? Tech adoption?",
                "Antitrust? Labour law? Data privacy (GDPR)? IP protection?",
                "Climate risk? Carbon regulation? Net zero targets? Resource scarcity?"
            ],
            "Finance Impact": [
                "Tax planning, political risk premium in discount rate, regulatory compliance costs",
                "Revenue forecasting, cost of debt, FX hedging, demand modelling",
                "Market sizing, pricing power, workforce costs, brand value",
                "Capex requirements, obsolescence risk, digital investment ROI",
                "Legal provisions, compliance costs, litigation risk",
                "Stranded asset risk, carbon cost, green capex, sustainability-linked finance"
            ]
        }
        st.dataframe(pd.DataFrame(pestle_data), use_container_width=True, hide_index=True)

        st.subheader("3. Porter's Five Forces")
        st.markdown("""
        Michael Porter's Five Forces framework assesses **industry attractiveness** — how much profit potential
        exists in a given industry. High forces = low profit potential; Low forces = high profit potential.
        """)
        forces_data = {
            "Force": ["Threat of New Entrants", "Bargaining Power of Suppliers", "Bargaining Power of Buyers",
                      "Threat of Substitutes", "Competitive Rivalry"],
            "High When...": [
                "Low capital requirements, few patents, easy access to distribution",
                "Few suppliers, high switching costs, unique inputs, forward integration threat",
                "Few large buyers, standardised products, easy switching, backward integration threat",
                "Many alternatives exist, low switching costs, substitutes offer better value",
                "Many competitors, slow growth, high fixed costs, low differentiation, high exit barriers"
            ],
            "Finance Implication": [
                "Margin erosion risk; higher cost of maintaining competitive position",
                "Cost pressure; input price volatility; procurement strategy critical",
                "Pricing power limited; revenue at risk; discounting pressure",
                "Revenue displacement risk; need for innovation investment",
                "Price wars erode margins; heavy marketing/R&D spend required"
            ]
        }
        st.dataframe(pd.DataFrame(forces_data), use_container_width=True, hide_index=True)

        st.subheader("4. Strategic Group Analysis")
        st.markdown("""
        Strategic groups are clusters of firms within an industry pursuing **similar strategies** with similar resources.
        - **Mobility barriers** prevent movement between groups (capital, expertise, brand)
        - Firms within the same group are most direct competitors
        - **Finance use**: identify which competitive group drives your pricing, cost structure, and investment requirements
        """)

        st.subheader("5. Market Sizing: TAM, SAM, SOM")
        st.markdown("""
        | Metric | Definition | Finance Use |
        |--------|-----------|------------|
        | **TAM** — Total Addressable Market | The total market demand if you had 100% share | Sets the maximum revenue opportunity |
        | **SAM** — Serviceable Addressable Market | The portion of TAM your business model can serve | Realistic revenue ceiling for strategic planning |
        | **SOM** — Serviceable Obtainable Market | The share of SAM you can realistically capture | Revenue target for 3–5 year financial model |

        **Finance professional's role:** Build bottom-up and top-down market sizing models to validate strategic growth assumptions in financial plans.
        """)

        st.subheader("6. Scenario Planning")
        st.markdown("""
        Scenario planning translates external uncertainty into **financially modelled alternative futures**.

        **Four-Step Process:**
        1. Identify the two most uncertain and impactful external variables (axes)
        2. Construct 3–4 plausible scenarios at extremes and midpoints
        3. Assess strategic and financial implications of each scenario
        4. Build financial models for each scenario (base, bull, bear)

        **Finance deliverable:** Scenario-based P&L, balance sheet, and cash flow — tested against different external conditions.
        The scenario with the best **risk-adjusted NPV** typically wins capital allocation.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: PESTLE Analysis — Global Fast Food Chain")
        example_pestle = {
            "Factor": ["Political", "Economic", "Social", "Technological", "Legal", "Environmental"],
            "Finding": [
                "New import tariffs on beef in key markets (US, EU)",
                "Consumer spending slowing; inflation driving menu price sensitivity",
                "Growing demand for plant-based options; health consciousness rising",
                "Mobile ordering apps reducing labour costs; AI-driven supply chain",
                "Minimum wage increases across US and UK markets",
                "Carbon footprint of beef supply chain under investor/regulator scrutiny"
            ],
            "Strategic Response": [
                "Diversify supply chain; increase local sourcing; lobby for tariff relief",
                "Introduce value tier menu; optimise portion sizes; lock in supplier prices",
                "Launch plant-based menu range; reformulate recipes for health credentials",
                "Invest in app technology; automate kitchen operations",
                "Model labour cost impact in financial plan; explore further automation",
                "Commit to net-zero supply chain; reduce beef portion; explore carbon offset"
            ],
            "Financial Impact": [
                "COGS increase 3–5%; reduce by dual-sourcing strategy",
                "Risk of 5% revenue decline in recession scenario",
                "Plant-based items carry 8% higher margin — upside opportunity",
                "Save $2.5M/yr in labour; $5M capex investment required",
                "Labour cost +$18M annually; payback via automation in 3 years",
                "ESG investment $10M over 3 years; protects brand value and investor relations"
            ]
        }
        st.dataframe(pd.DataFrame(example_pestle), use_container_width=True, hide_index=True)

        st.subheader("Example 2: Porter's Five Forces — Airline Industry")
        st.markdown("""
        **Industry: Commercial Aviation (Short-haul)**

        | Force | Strength | Financial Implication |
        |-------|----------|----------------------|
        | New Entrants | **Low–Medium** (high capital barriers, slot constraints, safety regulations) | Existing players somewhat protected; capital barrier deters mass entry |
        | Supplier Power | **High** (Boeing/Airbus duopoly; jet fuel price volatility; pilot shortage) | COGS highly exposed to input price shocks; fuel hedging critical |
        | Buyer Power | **High** (price comparison sites; low switching costs; commoditised product) | Pricing power limited; margins thin; revenue management critical |
        | Substitutes | **Medium** (high-speed rail for short routes; video conferencing post-COVID) | Revenue risk on 1–3 hour routes; business travel decline structural |
        | Rivalry | **Very High** (many competitors; LCC disruption; capacity surplus; exit barriers) | Margin pressure; constant promotional pricing; EBIT margins 2–5% typically |

        **Five Forces Conclusion:** Airlines face a structurally unattractive industry (high forces, thin margins).
        Finance implications: high capital intensity, poor ROIC, need for ancillary revenue to offset commodity core business.
        """)
        st.warning("💡 **Finance Insight**: An industry with very high Five Forces intensity typically delivers ROIC below WACC — meaning the industry destroys economic value. Finance professionals use Five Forces to set realistic return expectations and determine whether capital investment is justified.")

        st.subheader("Example 3: Scenario Planning — Tech Startup")
        st.markdown("**Uncertainty Axes: Regulation intensity (High/Low) × Technology adoption speed (Fast/Slow)**")
        scenarios = {
            "Scenario": ["🌟 Blue Sky", "⚡ Fast Lane", "🔒 Locked In", "🌧️ Storm Clouds"],
            "Conditions": [
                "Light regulation + Fast adoption",
                "Fast adoption + Medium regulation",
                "Heavy regulation + Fast adoption",
                "Heavy regulation + Slow adoption"
            ],
            "Revenue Forecast (Year 5)": ["$120M", "$90M", "$60M", "$35M"],
            "EBITDA Margin": ["35%", "25%", "18%", "10%"],
            "Strategic Priority": [
                "Aggressive growth; market share capture",
                "Scale quickly; invest in network effects",
                "Compliance-first; build regulatory moat",
                "Pivot product; seek niche; reduce burn rate"
            ],
            "Capital Required": ["$50M Series B", "$40M Series B", "$30M + legal reserves", "$20M bridge round"]
        }
        st.dataframe(pd.DataFrame(scenarios), use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "PESTLE Impact Scorer",
            "Five Forces Industry Attractiveness Rater",
            "Market Size Calculator (TAM/SAM/SOM)"
        ])

        if tool == "PESTLE Impact Scorer":
            st.subheader("🌍 PESTLE Impact Scorer")
            st.markdown("Rate each external factor on **Impact** (1=negligible → 5=critical) and **Likelihood** (1=unlikely → 5=certain):")
            factors = ["Political", "Economic", "Social", "Technological", "Legal", "Environmental"]
            colors_map = {"Political": "#E74C3C", "Economic": "#27AE60", "Social": "#3498DB",
                         "Technological": "#9B59B6", "Legal": "#E67E22", "Environmental": "#1ABC9C"}
            results = []
            for f in factors:
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    desc = st.text_input(f"{f} — Key finding:", value=f"Enter key {f.lower()} trend or risk", key=f"p_{f}")
                with col2:
                    impact = st.slider("Impact", 1, 5, 3, key=f"pi_{f}")
                with col3:
                    likelihood = st.slider("Likelihood", 1, 5, 3, key=f"pl_{f}")
                priority = impact * likelihood
                results.append({"Factor": f, "Finding": desc, "Impact": impact, "Likelihood": likelihood,
                                "Priority Score": priority, "Rating": "🔴 Critical" if priority >= 16 else ("🟠 High" if priority >= 9 else "🟢 Monitor")})
            df_results = pd.DataFrame(results).sort_values("Priority Score", ascending=False)
            st.markdown("### 📊 PESTLE Priority Matrix")
            st.dataframe(df_results[["Factor", "Impact", "Likelihood", "Priority Score", "Rating"]], use_container_width=True, hide_index=True)
            top = df_results.iloc[0]
            st.warning(f"🚨 **Highest Priority Factor: {top['Factor']}** — Score {top['Priority Score']}/25. Requires immediate strategic and financial response planning.")

        elif tool == "Five Forces Industry Attractiveness Rater":
            st.subheader("⚙️ Five Forces Attractiveness Rater")
            st.markdown("Rate each force: **1 = Very Low (favourable) → 5 = Very High (unfavourable)**")
            forces_list = ["Threat of New Entrants", "Supplier Bargaining Power", "Buyer Bargaining Power",
                          "Threat of Substitutes", "Competitive Rivalry"]
            scores = []
            for force in forces_list:
                col1, col2 = st.columns([2, 1])
                with col1: st.markdown(f"**{force}**")
                with col2: score = st.slider("", 1, 5, 3, key=f"ff_{force}")
                scores.append(score)

            avg = np.mean(scores)
            total = sum(scores)
            if st.button("📊 Assess Industry Attractiveness"):
                if avg <= 2:
                    st.success(f"🟢 **Highly Attractive Industry** — Average Force Score: {avg:.1f}/5")
                    st.markdown("Low competitive pressure. High profit potential. Strong case for capital investment and market entry.")
                elif avg <= 3:
                    st.info(f"🟡 **Moderately Attractive Industry** — Average Force Score: {avg:.1f}/5")
                    st.markdown("Mixed conditions. Profitability possible but requires strong positioning. Selective investment justified.")
                else:
                    st.error(f"🔴 **Unattractive Industry** — Average Force Score: {avg:.1f}/5")
                    st.markdown("High competitive pressure. Structural margin erosion. Requires exceptional capability or niche to earn ROIC > WACC.")

                st.markdown("### 📈 Estimated Financial Benchmarks")
                industry_margin = max(1, 25 - (avg * 4))
                roic_estimate = max(2, 20 - (avg * 3))
                st.markdown(f"""
                | Metric | Estimate |
                |--------|---------|
                | Typical EBITDA Margin | ~{industry_margin:.0f}% |
                | Expected ROIC Range | ~{roic_estimate:.0f}–{roic_estimate+5:.0f}% |
                | Pricing Power | {'Strong' if avg < 2.5 else ('Moderate' if avg < 3.5 else 'Weak')} |
                | Capital Investment Attractiveness | {'High' if avg < 2.5 else ('Selective' if avg < 3.5 else 'Caution — requires strategic justification')} |
                """)

        else:  # Market Size Calculator
            st.subheader("📐 Market Size Calculator (TAM / SAM / SOM)")
            col1, col2 = st.columns(2)
            with col1:
                total_population = st.number_input("Total Target Population (people or businesses):", min_value=1000, value=50000000, step=100000, format="%d")
                avg_spend = st.number_input("Average Annual Spend per Customer ($):", min_value=1.0, value=500.0, step=10.0)
            with col2:
                sam_pct = st.slider("SAM — % of TAM your model can serve:", 1, 100, 30)
                som_pct = st.slider("SOM — % of SAM you can realistically capture in 3–5 yrs:", 1, 100, 10)

            tam = total_population * avg_spend
            sam = tam * (sam_pct / 100)
            som = sam * (som_pct / 100)

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("TAM — Total Addressable Market", f"${tam/1e9:.2f}B" if tam >= 1e9 else f"${tam/1e6:.1f}M")
            with col2: st.metric("SAM — Serviceable Market", f"${sam/1e9:.2f}B" if sam >= 1e9 else f"${sam/1e6:.1f}M", f"{sam_pct}% of TAM")
            with col3: st.metric("SOM — Obtainable Market", f"${som/1e6:.1f}M", f"{som_pct}% of SAM")

            st.info(f"💡 **Revenue Target**: A realistic 3–5 year revenue target based on this market sizing is approximately **${som/1e6:.1f}M**. Build your financial model around capturing this SOM.")

    with tab4:
        st.header("Visualizations")

        st.subheader("Five Forces Radar Chart")
        force_names = ["New Entrants", "Supplier Power", "Buyer Power", "Substitutes", "Rivalry"]
        force_scores = [2, 4, 3, 2, 4]
        fig_radar = go.Figure(go.Scatterpolar(
            r=force_scores + [force_scores[0]],
            theta=force_names + [force_names[0]],
            fill="toself", name="Industry Forces",
            line=dict(color="#E74C3C", width=3),
            fillcolor="rgba(231,76,60,0.3)"
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
            title="Five Forces Profile — Industry Attractiveness", height=400
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        st.subheader("PESTLE Factor Priority Heatmap")
        pestle_factors = ["Political", "Economic", "Social", "Technological", "Legal", "Environmental"]
        impact_scores = [3, 4, 3, 5, 2, 4]
        likelihood_scores = [2, 4, 4, 5, 3, 3]
        priority_scores = [i * l for i, l in zip(impact_scores, likelihood_scores)]
        fig_pestle = go.Figure(go.Bar(
            x=pestle_factors, y=priority_scores,
            marker_color=["#E74C3C" if p >= 16 else "#E67E22" if p >= 9 else "#27AE60" for p in priority_scores],
            text=[f"Score: {p}" for p in priority_scores],
            textposition="auto"
        ))
        fig_pestle.update_layout(title="PESTLE Priority Scores (Impact × Likelihood)", yaxis_title="Priority Score (max 25)", height=400)
        st.plotly_chart(fig_pestle, use_container_width=True)

        st.subheader("TAM → SAM → SOM Funnel")
        fig_funnel = go.Figure(go.Funnel(
            y=["TAM — Total Addressable Market", "SAM — Serviceable Market", "SOM — Obtainable Market"],
            x=[1000, 300, 30],
            textinfo="value+percent initial",
            marker=dict(color=["#2563EB", "#0D7377", "#D97706"])
        ))
        fig_funnel.update_layout(title="Market Opportunity Funnel (TAM → SAM → SOM)", height=400)
        st.plotly_chart(fig_funnel, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Which PESTLE factor would cover rising interest rates?**")
        q1 = st.radio("", ["Political", "Economic", "Social", "Legal"], key="bs2q1")
        if st.button("Check Answer", key="bs2c1"):
            if q1 == "Economic":
                st.success("✅ Correct! Interest rates are an Economic factor — they affect cost of debt, consumer spending, and NPV calculations.")
            else:
                st.error("❌ Incorrect. Interest rates fall under Economic in the PESTLE framework.")

        st.markdown("---")
        st.markdown("**2. A high 'Threat of New Entrants' in Porter's Five Forces means:**")
        q2 = st.radio("", [
            "Existing companies are very profitable",
            "Industry margins are likely to be compressed over time",
            "Suppliers have very high bargaining power",
            "There are very few competitors"
        ], key="bs2q2")
        if st.button("Check Answer", key="bs2c2"):
            if q2 == "Industry margins are likely to be compressed over time":
                st.success("✅ Correct! High new entrant threat means more competition, eroding existing firms' margins.")
            else:
                st.error("❌ Incorrect. High threat of entry attracts competitors, compressing margins over time.")

        st.markdown("---")
        st.markdown("**3. SAM stands for:**")
        q3 = st.radio("", ["Strategic Addressable Metrics", "Serviceable Addressable Market", "Scaled Attainable Market", "Surplus Asset Management"], key="bs2q3")
        if st.button("Check Answer", key="bs2c3"):
            if q3 == "Serviceable Addressable Market":
                st.success("✅ Correct! SAM is the portion of TAM that your business model can realistically serve.")
            else:
                st.error("❌ Incorrect. SAM = Serviceable Addressable Market — the share of TAM your model can serve.")

        st.markdown("---")
        st.markdown("**4. In scenario planning, the 'base case' financial model represents:**")
        q4 = st.radio("", [
            "The worst-case outcome",
            "The most optimistic revenue projection",
            "The most likely outcome given current external trends",
            "The target set by the board"
        ], key="bs2q4")
        if st.button("Check Answer", key="bs2c4"):
            if q4 == "The most likely outcome given current external trends":
                st.success("✅ Correct! The base case reflects the most probable external environment — not best or worst case.")
            else:
                st.error("❌ Incorrect. The base case is the most probable scenario, not the best or worst.")

        st.markdown("---")
        st.markdown("**5. Which of the Five Forces most directly affects a company's ability to raise prices?**")
        q5 = st.radio("", ["Supplier Power", "Buyer Bargaining Power", "Threat of New Entrants", "Competitive Rivalry"], key="bs2q5")
        if st.button("Check Answer", key="bs2c5"):
            if q5 == "Buyer Bargaining Power":
                st.success("✅ Correct! When buyers have strong bargaining power, they can push back on price increases — limiting pricing power.")
            else:
                st.error("❌ Incorrect. Buyer Bargaining Power is the most direct constraint on a company's ability to raise prices.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. PESTLE Analysis — Six External Forces
        | Factor | Finance Implications |
        |--------|---------------------|
        | Political | Tax regime, regulatory compliance costs, political risk premium |
        | Economic | Revenue forecasting, cost of debt, FX exposure |
        | Social | Market sizing, pricing power, workforce costs |
        | Technological | Capex requirements, digital investment ROI |
        | Legal | Compliance costs, litigation risk provisions |
        | Environmental | Carbon costs, stranded asset risk, green capex |

        ### 2. Porter's Five Forces
        - Assess **industry-level profit potential**
        - Five forces: New Entrants, Supplier Power, Buyer Power, Substitutes, Rivalry
        - High forces = structurally unattractive = likely ROIC < WACC
        - Finance use: set return expectations, justify capital investment decisions

        ### 3. Market Sizing
        ```
        TAM → Defines maximum revenue opportunity
        SAM → Defines realistic addressable market for your model
        SOM → Drives your 3–5 year revenue targets in the financial plan
        ```

        ### 4. Scenario Planning
        - Build 3–4 financially modelled scenarios around key uncertainties
        - Test strategy against base, bull, and bear external conditions
        - Capital allocation should favour strategies robust across multiple scenarios

        ### 5. Key Tools
        | Tool | Purpose | Finance Output |
        |------|---------|---------------|
        | PESTLE | Macro trend identification | Risk-adjusted revenue/cost assumptions |
        | Five Forces | Industry profitability assessment | Expected ROIC range, margin benchmarks |
        | Strategic Groups | Competitive cluster analysis | Peer benchmarking, competitive cost analysis |
        | Scenario Planning | Uncertainty modelling | Scenario financial models (P&L, CF, BS) |
        """)

        st.subheader("📌 Key Formulas")
        st.code("PESTLE Priority Score = Impact Rating × Likelihood Rating")
        st.code("Five Forces Average = Sum of all force scores / 5  (lower = more attractive)")
        st.code("TAM = Total Population × Average Annual Spend per Customer")
        st.code("SAM = TAM × % Serviceable by your business model")
        st.code("SOM = SAM × % Realistically capturable in planning horizon")

        st.success("🎓 **Module 2 Complete!** You can now systematically analyse the external environment and translate external trends into financial assumptions.")
        st.info("💡 **Next**: Module 3 — Internal Analysis & Competitive Advantage (VRIN, Value Chain, SWOT)")

if __name__ == "__main__":
    show()