import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🌐 Module 15: Strategic Management Accounting")
    st.markdown("*Apply advanced strategic tools, sustainability accounting, and emerging technologies*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Strategic Management Accounting (SMA)")
        st.markdown("""
        **Strategic Management Accounting** extends traditional management accounting beyond internal cost control
        to incorporate **external competitive information** and **long-term strategic positioning**.

        #### SMA vs Traditional Management Accounting:
        | Feature | Traditional MA | Strategic MA |
        |---------|---------------|-------------|
        | Focus | Internal costs | External + Internal |
        | Time horizon | Short-term | Long-term |
        | Competitors | Ignored | Central to analysis |
        | Customers | Aggregate | Individual/segment |
        | Value chain | Internal only | Full industry chain |
        | Purpose | Cost control | Competitive advantage |

        #### Key SMA Activities:
        - Strategic cost analysis
        - Competitor cost analysis
        - Value chain analysis
        - Customer profitability analysis
        - Benchmarking
        - Environmental and sustainability accounting
        """)

        st.subheader("2. Strategic Positioning — Porter's Generic Strategies")
        st.markdown("""
        **Michael Porter** identified two fundamental sources of competitive advantage:

        #### Cost Leadership Strategy:
        - Produce at LOWEST cost in industry
        - Price at or below competitors
        - Achieve scale economies, efficiency, lean production
        - **SMA Focus**: Cost reduction, efficiency metrics, process improvement
        - **Examples**: Walmart, Southwest Airlines, IKEA

        #### Differentiation Strategy:
        - Offer UNIQUE product/service customers value and will pay premium for
        - Achieve brand loyalty, premium pricing
        - **SMA Focus**: Revenue drivers, customer value, quality costs, R&D ROI
        - **Examples**: Apple, BMW, Rolex

        #### Focus Strategy:
        - Target a NARROW market segment
        - Apply cost leadership OR differentiation within that segment
        - **Examples**: Ferrari (focus differentiation), Dollar stores (focus cost)

        ```
        Accounting implications:
        Cost Leader → Standard costing, variance analysis, efficiency metrics
        Differentiator → Life-cycle costing, customer profitability, quality costs
        ```
        """)

        st.subheader("3. Value Chain Analysis")
        st.markdown("""
        **Porter's Value Chain** identifies all activities that create value for customers.

        #### Primary Activities (directly create value):
        | Activity | Description | Cost Driver Examples |
        |----------|-------------|---------------------|
        | Inbound Logistics | Receiving, storing materials | Supplier relationships, JIT |
        | Operations | Transforming inputs to products | Process efficiency, automation |
        | Outbound Logistics | Distributing finished products | Distribution network |
        | Marketing & Sales | Creating awareness and demand | Brand investment, channels |
        | Service | After-sale support | Service cost, satisfaction |

        #### Support Activities (enable primary activities):
        - **Firm Infrastructure**: Management, accounting, legal, finance
        - **Human Resource Management**: Hiring, training, development
        - **Technology Development**: R&D, process improvement
        - **Procurement**: Purchasing inputs

        #### Strategic SMA Application:
        ```
        1. Map your full value chain
        2. Identify cost and value drivers for each activity
        3. Compare with competitors' value chains
        4. Find where you can create more value or reduce cost
        5. Make vs buy decisions for each activity
        ```
        """)

        st.subheader("4. Benchmarking")
        st.markdown("""
        **Benchmarking** = Comparing your performance against best-in-class standards.

        #### Types of Benchmarking:
        | Type | Against Whom | Purpose |
        |------|-------------|---------|
        | **Internal** | Other divisions/departments | Identify internal best practices |
        | **Competitive** | Direct competitors | Close performance gaps |
        | **Functional** | Same function, different industry | Learn from world-class performers |
        | **Generic** | Best-in-class any industry | Most innovative improvements |

        #### Benchmarking Process:
        ```
        1. Identify what to benchmark (processes, metrics, costs)
        2. Select benchmark partners
        3. Collect and analyze data
        4. Identify performance gaps
        5. Set improvement targets
        6. Implement improvements
        7. Monitor and repeat
        ```

        #### Key Metrics for Benchmarking:
        - Cost per unit by process step
        - Cycle time and throughput
        - Quality rates and defect levels
        - Customer satisfaction scores
        - Return on invested capital
        """)

        st.subheader("5. Customer Lifetime Value (CLV)")
        st.markdown("""
        **CLV** = Total present value of all future cash flows from a customer relationship.

        ```
        CLV = Σ [(Annual Margin × Retention Rate^t) / (1 + Discount Rate)^t]
              for t = 1 to n years

        Simplified:
        CLV = (Annual Revenue × Gross Margin %) / (1 + Discount Rate − Retention Rate)

        Customer Acquisition Cost (CAC):
        CAC = Total Sales & Marketing Cost / New Customers Acquired

        CLV:CAC Ratio:
        > 3:1 = Healthy (CLV is at least 3× cost to acquire)
        < 1:1 = Problem (costs more to acquire than customer is worth)
        ```
        """)

        st.subheader("6. Sustainability Accounting & Environmental Costs")
        st.markdown("""
        **Sustainability Accounting** integrates environmental and social performance into management accounting.

        #### Environmental Cost Categories:
        | Category | Description | Examples |
        |----------|-------------|---------|
        | **Conventional** | Normal business costs with environmental component | Energy, materials, waste disposal |
        | **Hidden** | Regulatory and compliance costs | Permits, monitoring, reporting |
        | **Contingent** | Future/potential environmental costs | Remediation, fines, litigation |
        | **Relationship** | Image and relationship costs | Community relations, customer perception |

        #### Carbon Accounting:
        ```
        Carbon Footprint = Σ (Activity Level × Emission Factor)

        Scope 1: Direct emissions (own operations, vehicles)
        Scope 2: Indirect emissions (purchased electricity/heat)
        Scope 3: Value chain emissions (suppliers, customers)

        Carbon Cost = Carbon Footprint × Carbon Price per tonne CO₂
        ```

        #### Triple Bottom Line (TBL):
        - **Economic** (Profit): Traditional financial performance
        - **Social** (People): Employee welfare, community impact
        - **Environmental** (Planet): Ecological footprint, resource use
        """)

        st.subheader("7. Integrated Reporting (IR)")
        st.markdown("""
        **Integrated Reporting** communicates how an organization creates value over time
        across six capitals:

        | Capital | Definition | Examples |
        |---------|-----------|---------|
        | **Financial** | Funds available | Equity, debt, retained earnings |
        | **Manufactured** | Physical assets | Buildings, equipment, infrastructure |
        | **Intellectual** | Intangible assets | Patents, brand, systems, R&D |
        | **Human** | People capability | Skills, motivation, experience |
        | **Social & Relationship** | Stakeholder relationships | Brand trust, community license |
        | **Natural** | Environmental resources | Water, land, biodiversity, climate |
        """)

        st.subheader("8. Big Data & Analytics in Management Accounting")
        st.markdown("""
        #### Evolution of Management Accounting Analytics:

        | Level | Type | Description | Tools |
        |-------|------|-------------|-------|
        | 1 | **Descriptive** | What happened? | Reports, dashboards |
        | 2 | **Diagnostic** | Why did it happen? | Drill-down, root cause |
        | 3 | **Predictive** | What will happen? | Forecasting, ML models |
        | 4 | **Prescriptive** | What should we do? | Optimization, AI |

        #### Key Applications:
        - **Predictive cost modeling**: Forecast future costs using historical patterns
        - **Real-time variance analysis**: Instant feedback vs. monthly reports
        - **Customer analytics**: Segment customers by CLV, churn risk
        - **Supply chain optimization**: Dynamic pricing and sourcing decisions
        - **Fraud detection**: Unusual cost patterns flagged automatically
        - **Driver-based planning**: Link financial forecasts to business drivers

        #### Emerging Technologies:
        - **AI & Machine Learning**: Automate routine accounting, anomaly detection
        - **Blockchain**: Immutable audit trails, smart contracts, supply chain transparency
        - **RPA (Robotic Process Automation)**: Automate repetitive accounting tasks
        - **Cloud ERP**: Real-time global financial data integration
        """)

        st.subheader("9. Risk Management & Management Accounting")
        st.markdown("""
        **Enterprise Risk Management (ERM)** integrates risk into planning and decision-making.

        #### Risk Categories:
        ```
        Strategic Risk:   Competitive position, market shifts, technology disruption
        Operational Risk: Process failures, quality issues, supply chain disruption
        Financial Risk:   Currency, interest rate, liquidity, credit risk
        Compliance Risk:  Regulatory, tax, legal, reporting requirements
        Reputational Risk: Brand damage, ESG controversies
        ```

        #### Risk Quantification:
        ```
        Expected Loss = Probability × Impact
        Risk-Adjusted Return = Expected Return − (Risk Premium × Risk Exposure)

        Value at Risk (VaR):
        Maximum expected loss over a period at a given confidence level
        Example: "95% VaR of $1M" means 95% confidence loss will not exceed $1M
        ```
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Value Chain Cost Analysis")
        st.markdown("""
        **Company vs Competitor — Value Chain Cost Analysis:**

        | Value Chain Activity | Our Cost | Competitor Cost | Difference | Advantage |
        |---------------------|---------|-----------------|-----------|-----------|
        | Inbound Logistics | $80,000 | $70,000 | +$10,000 | Competitor |
        | Operations | $200,000 | $250,000 | -$50,000 | **US** |
        | Outbound Logistics | $60,000 | $55,000 | +$5,000 | Competitor |
        | Marketing & Sales | $150,000 | $180,000 | -$30,000 | **US** |
        | Customer Service | $40,000 | $35,000 | +$5,000 | Competitor |
        | **Total** | **$530,000** | **$590,000** | **-$60,000** | **US by $60K** |

        **Strategic Insights:**
        ```
        Our advantages: Operations (lean manufacturing) + Marketing (efficient channels)
        Our weaknesses: Inbound logistics (supplier costs), Outbound logistics (distribution)

        Actions to take:
        1. Consolidate suppliers to reduce inbound logistics cost → Target savings: $8,000
        2. Outsource distribution to specialist → Target savings: $4,000
        3. Protect operational advantage through continued lean investment
        4. Reinvest marketing savings in brand building
        ```
        """)

        st.subheader("Example 2: Customer Lifetime Value")
        st.markdown("""
        **Two Customer Segments:**

        | Item | Segment A (Enterprise) | Segment B (SMB) |
        |------|----------------------|-----------------|
        | Annual Revenue | $120,000 | $12,000 |
        | Gross Margin % | 45% | 35% |
        | Annual Margin | $54,000 | $4,200 |
        | Retention Rate | 90% | 70% |
        | Discount Rate | 10% | 10% |
        | Customer Acq. Cost | $8,000 | $500 |

        **CLV Calculation (Simplified):**
        ```
        Segment A CLV:
        CLV = Annual Margin / (1 + Discount Rate − Retention Rate)
            = $54,000 / (1 + 0.10 − 0.90)
            = $54,000 / 0.20
            = $270,000

        CAC = $8,000
        CLV:CAC = $270,000 / $8,000 = 33.75 : 1  ✅ Excellent!

        Segment B CLV:
        CLV = $4,200 / (1 + 0.10 − 0.70)
            = $4,200 / 0.40
            = $10,500

        CAC = $500
        CLV:CAC = $10,500 / $500 = 21 : 1  ✅ Good!
        ```

        **Strategic Decision:** Segment A is more valuable per customer.
        But Segment B has lower CAC and may offer greater total volume.
        Optimal strategy: Target both, but prioritize Segment A for key account management!
        """)

        st.subheader("Example 3: Sustainability / Carbon Accounting")
        st.markdown("""
        **Manufacturing Plant — Carbon Footprint Analysis:**

        | Emission Source | Quantity | Emission Factor | CO₂ (tonnes) |
        |----------------|---------|-----------------|-------------|
        | Natural gas (Scope 1) | 50,000 GJ | 56.1 kg/GJ | 2,805 |
        | Company vehicles (Scope 1) | 150,000 km | 0.21 kg/km | 31.5 |
        | Electricity (Scope 2) | 2,000,000 kWh | 0.45 kg/kWh | 900 |
        | Business travel (Scope 3) | 500,000 km | 0.18 kg/km | 90 |
        | **Total** | | | **3,826.5** |

        **Financial Impact at $50/tonne CO₂:**
        ```
        Scope 1 emissions cost: (2,805 + 31.5) × $50   = $141,825
        Scope 2 emissions cost: 900 × $50               = $45,000
        Scope 3 emissions cost: 90 × $50                = $4,500
        ─────────────────────────────────────────────────────────
        Total Carbon Cost:                              = $191,325

        Reduction Target (30% by 2030):
        Target reduction: 3,826.5 × 30% = 1,147.95 tonnes
        Cost saving at $50/tonne: $57,398 per year
        Plus avoided compliance costs and reputation benefits!
        ```
        """)

        st.subheader("Example 4: Benchmarking Analysis")
        st.markdown("""
        **Manufacturing Cost Benchmarking — 5 Competitors:**

        | Metric | Our Company | Best in Class | Industry Avg | Gap vs Best |
        |--------|------------|--------------|-------------|------------|
        | Cost per unit | $24.50 | $19.80 | $23.40 | **+$4.70** |
        | Defect rate | 2.1% | 0.3% | 1.5% | **+1.8%** |
        | Inventory turns | 8× | 18× | 10× | **−10×** |
        | On-time delivery | 89% | 98% | 93% | **−9%** |
        | Lead time (days) | 14 | 4 | 10 | **+10 days** |

        **Improvement Priorities:**
        ```
        1. HIGHEST PRIORITY: Cost per unit ($4.70 gap = $4.70M/year at 1M units)
           Actions: Lean, value engineering, supplier negotiation

        2. HIGH PRIORITY: Inventory turns (holding cost reduction)
           Actions: JIT implementation, demand-driven planning

        3. MEDIUM PRIORITY: Lead time and on-time delivery
           Actions: Process flow improvement, constraint elimination

        4. ONGOING: Defect rate improvement (quality program)
           Actions: Six Sigma project, prevention investment
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Calculator:", [
            "🔗 Value Chain Cost Analysis",
            "💎 Customer Lifetime Value (CLV)",
            "🌱 Carbon Footprint & Cost",
            "📊 Competitive Benchmarking",
            "⚖️ Strategic Positioning Assessment",
            "🔮 Predictive Cost Analytics"
        ])

        if calc_choice == "🔗 Value Chain Cost Analysis":
            st.subheader("Value Chain Cost Analysis")
            st.info("Compare your value chain costs against a competitor to identify competitive advantages and areas for improvement.")

            activities = ["Inbound Logistics", "Operations", "Outbound Logistics",
                          "Marketing & Sales", "Customer Service",
                          "Firm Infrastructure", "HR Management", "Technology", "Procurement"]

            num_activities = st.number_input("Number of Activities to Analyze", 3, 9, 5)
            selected_activities = activities[:int(num_activities)]

            vc_data = []
            for activity in selected_activities:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**{activity}:**")
                with col2:
                    our_cost = st.number_input("Our Cost ($)", 0.0, value=100000.0, step=5000.0, key=f"vc_our_{activity}")
                with col3:
                    comp_cost = st.number_input("Competitor Cost ($)", 0.0, value=90000.0, step=5000.0, key=f"vc_comp_{activity}")
                vc_data.append({"activity": activity, "our": our_cost, "comp": comp_cost})

            if st.button("🧮 Analyze Value Chain", type="primary"):
                for item in vc_data:
                    item["diff"] = item["our"] - item["comp"]
                    item["advantage"] = "✅ US" if item["diff"] < 0 else ("❌ Competitor" if item["diff"] > 0 else "🟡 Equal")
                    item["diff_pct"] = item["diff"] / item["comp"] * 100 if item["comp"] > 0 else 0

                total_our = sum([d["our"] for d in vc_data])
                total_comp = sum([d["comp"] for d in vc_data])
                total_diff = total_our - total_comp

                vc_df = pd.DataFrame([{
                    "Activity": d["activity"],
                    "Our Cost": f"${d['our']:,.2f}",
                    "Competitor Cost": f"${d['comp']:,.2f}",
                    "Difference": f"${d['diff']:+,.2f}",
                    "Diff %": f"{d['diff_pct']:+.1f}%",
                    "Advantage": d["advantage"]
                } for d in vc_data])

                total_row = pd.DataFrame([{
                    "Activity": "**TOTAL**",
                    "Our Cost": f"${total_our:,.2f}",
                    "Competitor Cost": f"${total_comp:,.2f}",
                    "Difference": f"${total_diff:+,.2f}",
                    "Diff %": f"{total_diff/total_comp*100:+.1f}%" if total_comp > 0 else "—",
                    "Advantage": "✅ US" if total_diff < 0 else "❌ Competitor"
                }])

                full_df = pd.concat([vc_df, total_row], ignore_index=True)
                st.dataframe(full_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Our Total Cost", f"${total_our:,.2f}")
                with col2: st.metric("Competitor Total", f"${total_comp:,.2f}")
                with col3:
                    st.metric("Net Position", f"${total_diff:+,.2f}",
                              delta="✅ Cost Advantage" if total_diff < 0 else "❌ Cost Disadvantage")

                advantages = [d["activity"] for d in vc_data if d["diff"] < 0]
                weaknesses = [d["activity"] for d in vc_data if d["diff"] > 0]

                if advantages:
                    st.success(f"✅ **Your advantages:** {', '.join(advantages)}")
                if weaknesses:
                    st.error(f"❌ **Areas to improve:** {', '.join(weaknesses)}")

                biggest_gap = max(vc_data, key=lambda x: x["diff"])
                st.info(f"💡 **Priority action:** {biggest_gap['activity']} has the largest gap (${biggest_gap['diff']:+,.2f}). Focus improvement efforts here first.")

        elif calc_choice == "💎 Customer Lifetime Value (CLV)":
            st.subheader("Customer Lifetime Value Calculator")

            num_segments = st.number_input("Number of Customer Segments", 1, 5, 2)
            segments_data = []

            for i in range(int(num_segments)):
                st.markdown(f"### Segment {i+1}:")
                col1, col2, col3 = st.columns(3)
                with col1:
                    seg_name = st.text_input("Segment Name", value=f"Segment {chr(65+i)}", key=f"clv_name_{i}")
                    annual_revenue = st.number_input("Annual Revenue/Customer ($)", 0.0, value=50000.0, step=1000.0, key=f"clv_rev_{i}")
                    gm_pct = st.number_input("Gross Margin (%)", 0.0, 100.0, value=40.0, step=1.0, key=f"clv_gm_{i}")
                with col2:
                    retention = st.number_input("Retention Rate (%)", 0.0, 100.0, value=85.0, step=1.0, key=f"clv_ret_{i}")
                    discount_rate = st.number_input("Discount Rate (%)", 0.0, 50.0, value=10.0, step=0.5, key=f"clv_dr_{i}")
                    cac = st.number_input("Acquisition Cost (CAC) ($)", 0.0, value=2000.0, step=100.0, key=f"clv_cac_{i}")
                with col3:
                    num_customers = st.number_input("Number of Customers", 0, value=500, step=10, key=f"clv_nc_{i}")
                    service_cost_pu = st.number_input("Annual Service Cost/Customer ($)", 0.0, value=2000.0, step=100.0, key=f"clv_sc_{i}")

                annual_margin = annual_revenue * gm_pct / 100 - service_cost_pu
                ret_rate = retention / 100
                dr_rate = discount_rate / 100
                denominator = 1 + dr_rate - ret_rate
                clv = annual_margin / denominator if denominator > 0 else 0
                clv_cac_ratio = clv / cac if cac > 0 else 0
                total_segment_value = clv * num_customers

                segments_data.append({
                    "name": seg_name, "annual_revenue": annual_revenue, "gm_pct": gm_pct,
                    "annual_margin": annual_margin, "retention": retention,
                    "discount_rate": discount_rate, "cac": cac, "clv": clv,
                    "clv_cac": clv_cac_ratio, "num_customers": num_customers,
                    "total_value": total_segment_value
                })

            if st.button("🧮 Calculate CLV Analysis", type="primary"):
                st.markdown("---")
                clv_results = pd.DataFrame([{
                    "Segment": s["name"],
                    "Annual Margin/Customer": f"${s['annual_margin']:,.2f}",
                    "Retention Rate": f"{s['retention']:.1f}%",
                    "CLV": f"${s['clv']:,.2f}",
                    "CAC": f"${s['cac']:,.2f}",
                    "CLV:CAC Ratio": f"{s['clv_cac']:.1f}:1",
                    "# Customers": f"{s['num_customers']:,}",
                    "Total Segment Value": f"${s['total_value']:,.2f}"
                } for s in segments_data])

                st.dataframe(clv_results, use_container_width=True, hide_index=True)

                total_portfolio_value = sum([s["total_value"] for s in segments_data])
                st.metric("Total Customer Portfolio Value", f"${total_portfolio_value:,.2f}")

                for s in segments_data:
                    ratio = s["clv_cac"]
                    if ratio >= 5:
                        st.success(f"✅ **{s['name']}**: CLV:CAC = {ratio:.1f}:1 — Excellent! High-value segment, prioritize growth.")
                    elif ratio >= 3:
                        st.info(f"ℹ️ **{s['name']}**: CLV:CAC = {ratio:.1f}:1 — Healthy. Good segment to invest in.")
                    elif ratio >= 1:
                        st.warning(f"⚠️ **{s['name']}**: CLV:CAC = {ratio:.1f}:1 — Marginal. Review acquisition costs or improve retention.")
                    else:
                        st.error(f"❌ **{s['name']}**: CLV:CAC = {ratio:.1f}:1 — Unprofitable! Costs to acquire exceed lifetime value.")

                # Sensitivity — retention rate impact
                st.markdown("### Retention Rate Sensitivity (Segment 1):")
                s0 = segments_data[0]
                ret_range = np.arange(0.60, 1.00, 0.05)
                clv_range = [s0["annual_margin"] / (1 + s0["discount_rate"]/100 - r) for r in ret_range if (1 + s0["discount_rate"]/100 - r) > 0]
                ret_labels = [f"{r*100:.0f}%" for r in ret_range if (1 + s0["discount_rate"]/100 - r) > 0]

                fig_ret = go.Figure(go.Bar(x=ret_labels, y=clv_range, marker_color="#2E86C1",
                                           text=[f"${v:,.0f}" for v in clv_range], textposition="auto"))
                fig_ret.update_layout(title=f"CLV Sensitivity to Retention Rate — {s0['name']}",
                                       xaxis_title="Retention Rate", yaxis_title="CLV ($)")
                st.plotly_chart(fig_ret, use_container_width=True)

        elif calc_choice == "🌱 Carbon Footprint & Cost":
            st.subheader("Carbon Footprint & Cost Calculator")

            col1, col2 = st.columns(2)
            with col1:
                carbon_price = st.number_input("Carbon Price ($/tonne CO₂)", 0.0, value=50.0, step=5.0)
                reduction_target = st.number_input("Reduction Target (%)", 0.0, 100.0, value=30.0, step=5.0)

            st.markdown("### Emission Sources:")
            emission_sources = []

            default_sources = [
                ("Natural Gas (Scope 1)", 50000, "GJ", 0.0561, "Scope 1"),
                ("Company Vehicles (Scope 1)", 150000, "km", 0.00021, "Scope 1"),
                ("Purchased Electricity (Scope 2)", 2000000, "kWh", 0.00045, "Scope 2"),
                ("Business Travel (Scope 3)", 500000, "km", 0.00018, "Scope 3"),
                ("Supply Chain (Scope 3)", 1000000, "$ spend", 0.00015, "Scope 3")
            ]

            num_sources = st.number_input("Number of Emission Sources", 1, 10, 4)

            for i in range(int(num_sources)):
                default = default_sources[i] if i < len(default_sources) else ("Source", 100000, "units", 0.001, "Scope 1")
                col1, col2, col3, col4, col5 = st.columns(5)
                with col1: source_name = st.text_input("Source", value=default[0], key=f"em_name_{i}")
                with col2: quantity = st.number_input("Quantity", 0.0, value=float(default[1]), key=f"em_qty_{i}")
                with col3: unit = st.text_input("Unit", value=default[2], key=f"em_unit_{i}")
                with col4: ef = st.number_input("Emission Factor (tCO₂/unit)", 0.0, value=default[3], format="%.5f", key=f"em_ef_{i}")
                with col5: scope = st.selectbox("Scope", ["Scope 1", "Scope 2", "Scope 3"], key=f"em_scope_{i}")
                emission_sources.append({"name": source_name, "qty": quantity, "unit": unit, "ef": ef, "scope": scope})

            if st.button("🧮 Calculate Carbon Footprint", type="primary"):
                for s in emission_sources:
                    s["co2"] = s["qty"] * s["ef"]
                    s["cost"] = s["co2"] * carbon_price

                total_co2 = sum([s["co2"] for s in emission_sources])
                total_cost = sum([s["cost"] for s in emission_sources])

                em_df = pd.DataFrame([{
                    "Source": s["name"], "Scope": s["scope"],
                    "Quantity": f"{s['qty']:,.0f} {s['unit']}",
                    "CO₂ (tonnes)": f"{s['co2']:,.1f}",
                    "% of Total": f"{s['co2']/total_co2*100:.1f}%" if total_co2 > 0 else "0%",
                    "Carbon Cost": f"${s['cost']:,.2f}"
                } for s in emission_sources])

                st.dataframe(em_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Total CO₂ (tonnes)", f"{total_co2:,.1f}")
                with col2: st.metric("Total Carbon Cost", f"${total_cost:,.2f}")
                with col3:
                    target_reduction = total_co2 * reduction_target / 100
                    cost_saving = target_reduction * carbon_price
                    st.metric("Reduction Target", f"{target_reduction:,.1f} tonnes",
                              delta=f"Save ${cost_saving:,.2f}/year")

                # Scope breakdown
                scope_totals = {}
                for s in emission_sources:
                    scope_totals[s["scope"]] = scope_totals.get(s["scope"], 0) + s["co2"]

                scope_df = pd.DataFrame(list(scope_totals.items()), columns=["Scope", "CO₂ (tonnes)"])
                fig_scope = px.pie(scope_df, values="CO₂ (tonnes)", names="Scope",
                                   title="Emissions by Scope",
                                   color_discrete_sequence=["#E74C3C", "#E67E22", "#3498DB"])
                st.plotly_chart(fig_scope, use_container_width=True)

                # Reduction roadmap
                st.markdown("### Emission Reduction Roadmap:")
                sorted_sources = sorted(emission_sources, key=lambda x: x["co2"], reverse=True)
                roadmap_rows = []
                cum_reduction = 0
                for idx, s in enumerate(sorted_sources):
                    individual_reduction = s["co2"] * reduction_target / 100
                    cum_reduction += individual_reduction
                    roadmap_rows.append({
                        "Priority": idx + 1,
                        "Source": s["name"],
                        "Current Emissions": f"{s['co2']:,.1f} t",
                        "Target Reduction": f"{individual_reduction:,.1f} t",
                        "Cost Saving": f"${individual_reduction * carbon_price:,.2f}",
                        "Cum. Progress": f"{cum_reduction/total_co2*reduction_target/100*100:.1f}%"
                    })
                st.dataframe(pd.DataFrame(roadmap_rows), use_container_width=True, hide_index=True)

        elif calc_choice == "📊 Competitive Benchmarking":
            st.subheader("Competitive Benchmarking Tool")

            num_metrics = st.number_input("Number of Metrics", 2, 10, 6)
            num_competitors = st.number_input("Number of Competitors", 1, 5, 3)

            default_metrics = [
                ("Cost per Unit ($)", 24.50, 20.0, True),
                ("Defect Rate (%)", 2.1, 0.3, True),
                ("Inventory Turns (×)", 8.0, 18.0, False),
                ("On-Time Delivery (%)", 89.0, 98.0, False),
                ("Lead Time (days)", 14.0, 4.0, True),
                ("Customer Satisfaction (%)", 85.0, 96.0, False),
                ("ROIC (%)", 12.0, 22.0, False),
                ("Revenue/Employee ($K)", 180.0, 280.0, False),
                ("Market Share (%)", 15.0, 25.0, False),
                ("NPS Score", 32.0, 72.0, False)
            ]

            metrics = []
            competitor_names = []
            for j in range(int(num_competitors)):
                comp_name = st.text_input(f"Competitor {j+1} Name", value=f"Competitor {chr(65+j)}", key=f"bm_cn_{j}")
                competitor_names.append(comp_name)

            bm_data = []
            for i in range(int(num_metrics)):
                default = default_metrics[i] if i < len(default_metrics) else ("Metric", 100.0, 80.0, True)
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    metric_name = st.text_input("Metric Name", value=default[0], key=f"bm_mn_{i}")
                    lower_is_better = st.checkbox("Lower = Better?", value=default[3], key=f"bm_lb_{i}")
                with col2:
                    our_value = st.number_input("Our Value", 0.0, value=float(default[1]), step=0.1, key=f"bm_our_{i}")
                with col3:
                    best_value = st.number_input("Best in Class", 0.0, value=float(default[2]), step=0.1, key=f"bm_best_{i}")

                comp_values = [st.number_input(f"{competitor_names[j]}", 0.0,
                                                value=float(default[1] + (default[2]-default[1])*(j+1)/num_competitors),
                                                step=0.1, key=f"bm_cv_{i}_{j}") for j in range(int(num_competitors))]

                metrics.append({"name": metric_name, "our": our_value, "best": best_value,
                                  "lower_is_better": lower_is_better, "comp_values": comp_values})

            if st.button("🧮 Generate Benchmark Report", type="primary"):
                bm_rows = []
                for m in metrics:
                    gap = m["our"] - m["best"]
                    if m["lower_is_better"]:
                        gap_pct = gap / m["best"] * 100 if m["best"] != 0 else 0
                        status = "✅" if m["our"] <= m["best"] else ("⚠️" if gap / m["best"] < 0.2 else "❌")
                    else:
                        gap_pct = -gap / m["best"] * 100 if m["best"] != 0 else 0
                        status = "✅" if m["our"] >= m["best"] else ("⚠️" if abs(gap) / m["best"] < 0.15 else "❌")

                    row = {"Metric": m["name"], "Our Value": f"{m['our']}", "Best in Class": f"{m['best']}",
                           "Gap": f"{gap:+.2f}", "Gap %": f"{gap_pct:+.1f}%", "Status": status}
                    for j, cv in enumerate(m["comp_values"]):
                        row[competitor_names[j]] = f"{cv}"
                    bm_rows.append(row)

                bm_df = pd.DataFrame(bm_rows)
                st.dataframe(bm_df, use_container_width=True, hide_index=True)

                green = sum(1 for r in bm_rows if "✅" in r["Status"])
                yellow = sum(1 for r in bm_rows if "⚠️" in r["Status"])
                red = sum(1 for r in bm_rows if "❌" in r["Status"])

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("✅ At or Above Best", f"{green}/{len(bm_rows)}")
                with col2: st.metric("⚠️ Near Best", f"{yellow}/{len(bm_rows)}")
                with col3: st.metric("❌ Significant Gap", f"{red}/{len(bm_rows)}")

                worst_gaps = sorted([m for m in metrics if m["lower_is_better"] and m["our"] > m["best"]] +
                                    [m for m in metrics if not m["lower_is_better"] and m["our"] < m["best"]],
                                    key=lambda x: abs(x["our"] - x["best"]) / x["best"] if x["best"] != 0 else 0,
                                    reverse=True)

                if worst_gaps:
                    st.markdown("### 🎯 Top Priority Improvements:")
                    for i, m in enumerate(worst_gaps[:3]):
                        gap_size = abs(m["our"] - m["best"])
                        st.markdown(f"**{i+1}. {m['name']}**: Gap = {gap_size:.2f} ({gap_size/m['best']*100:.1f}% vs best in class)")

        elif calc_choice == "⚖️ Strategic Positioning Assessment":
            st.subheader("Strategic Positioning Assessment")
            st.info("Rate your company's position on key strategic dimensions (1=Very Low, 10=Very High)")

            dimensions = {
                "Cost Leadership": {
                    "metrics": ["Relative Cost Position", "Process Efficiency", "Scale Advantages", "Supplier Power"],
                    "description": "How well do you compete on cost?"
                },
                "Differentiation": {
                    "metrics": ["Product Uniqueness", "Brand Strength", "Innovation Rate", "Customer Loyalty"],
                    "description": "How unique and valued is your offering?"
                },
                "Market Focus": {
                    "metrics": ["Segment Clarity", "Customer Knowledge", "Niche Dominance", "Focus Discipline"],
                    "description": "How well do you serve a specific segment?"
                }
            }

            all_scores = {}
            for dim_name, dim_data in dimensions.items():
                st.markdown(f"### {dim_name} — *{dim_data['description']}*")
                cols = st.columns(len(dim_data["metrics"]))
                dim_scores = []
                for idx, metric in enumerate(dim_data["metrics"]):
                    with cols[idx]:
                        score = st.slider(metric, 1, 10, 5, key=f"sp_{dim_name}_{metric}")
                        dim_scores.append(score)
                all_scores[dim_name] = sum(dim_scores) / len(dim_scores)

            if st.button("🧮 Assess Strategic Position", type="primary"):
                dominant_strategy = max(all_scores, key=all_scores.get)
                max_score = all_scores[dominant_strategy]

                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                cols_list = [col1, col2, col3]
                colors_sp = {"Cost Leadership": "#2E86C1", "Differentiation": "#E67E22", "Market Focus": "#27AE60"}

                for idx, (dim, score) in enumerate(all_scores.items()):
                    with cols_list[idx]:
                        st.metric(dim, f"{score:.1f}/10")

                st.markdown(f"### 🎯 Dominant Strategy: **{dominant_strategy}**")
                st.markdown(f"Score: {max_score:.1f}/10")

                if dominant_strategy == "Cost Leadership":
                    st.success("📊 **Cost Leadership Profile** — Focus on operational efficiency, lean manufacturing, supply chain optimization, and scale economies. Key metrics: Cost per unit, productivity, inventory turns.")
                elif dominant_strategy == "Differentiation":
                    st.success("🌟 **Differentiation Profile** — Invest in innovation, brand building, quality, and customer experience. Key metrics: Customer satisfaction, NPS, margin premium, R&D ROI.")
                else:
                    st.success("🎯 **Focus Strategy Profile** — Deep knowledge of chosen segment, specialized offerings. Apply cost or differentiation within your niche.")

                # Radar chart
                categories = list(all_scores.keys())
                values = list(all_scores.values())
                values.append(values[0])
                categories.append(categories[0])

                fig_radar = go.Figure(go.Scatterpolar(
                    r=values, theta=categories, fill="toself",
                    name="Your Position", line=dict(color="#2E86C1")
                ))
                fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                                         showlegend=False, title="Strategic Positioning Radar")
                st.plotly_chart(fig_radar, use_container_width=True)

        else:  # Predictive Cost Analytics
            st.subheader("Predictive Cost Analytics")
            st.info("Use historical cost data to forecast future costs and identify trends.")

            num_periods = st.number_input("Historical Periods", 4, 12, 6)
            cost_type = st.text_input("Cost Type to Analyze", value="Manufacturing Cost per Unit")

            historical_costs = []
            historical_volumes = []
            st.markdown("### Enter Historical Data:")
            for i in range(int(num_periods)):
                col1, col2 = st.columns(2)
                with col1:
                    cost = st.number_input(f"Period {i+1} Cost ($)", 0.0, value=100000.0 - i*1000 + np.random.normal(0,2000), step=500.0, key=f"pca_c_{i}")
                with col2:
                    vol = st.number_input(f"Period {i+1} Volume (units)", 0, value=5000 + i*100, step=50, key=f"pca_v_{i}")
                historical_costs.append(cost)
                historical_volumes.append(vol)

            forecast_periods = st.number_input("Periods to Forecast", 1, 6, 3)

            if st.button("🔮 Generate Forecast", type="primary"):
                n = len(historical_costs)
                x = np.array(range(1, n+1))
                y = np.array(historical_costs)

                # Linear regression
                slope = (n * np.sum(x*y) - np.sum(x)*np.sum(y)) / (n * np.sum(x**2) - np.sum(x)**2)
                intercept = (np.sum(y) - slope * np.sum(x)) / n
                r_squared = 1 - np.sum((y - (intercept + slope*x))**2) / np.sum((y - np.mean(y))**2)

                future_periods = list(range(n+1, n + int(forecast_periods) + 1))
                forecasts = [intercept + slope * p for p in future_periods]

                all_periods = list(range(1, n+1)) + future_periods
                all_costs = historical_costs + [None] * int(forecast_periods)
                trend_line = [intercept + slope * p for p in all_periods]

                fig_pred = go.Figure()
                fig_pred.add_trace(go.Scatter(x=list(range(1, n+1)), y=historical_costs,
                                               mode="lines+markers", name="Historical",
                                               line=dict(color="#2E86C1", width=3),
                                               marker=dict(size=8)))
                fig_pred.add_trace(go.Scatter(x=all_periods, y=trend_line, mode="lines",
                                               name="Trend", line=dict(color="#95A5A6", width=2, dash="dot")))
                fig_pred.add_trace(go.Scatter(x=future_periods, y=forecasts,
                                               mode="lines+markers", name="Forecast",
                                               line=dict(color="#E67E22", width=3, dash="dash"),
                                               marker=dict(size=10, symbol="diamond")))
                fig_pred.add_vline(x=n + 0.5, line_dash="solid", line_color="gray",
                                    annotation_text="Forecast Start")
                fig_pred.update_layout(title=f"Predictive Analytics: {cost_type}",
                                        xaxis_title="Period", yaxis_title="Cost ($)")
                st.plotly_chart(fig_pred, use_container_width=True)

                st.markdown("### Forecast Summary:")
                summary_df = pd.DataFrame({
                    "Period": [f"P{p}" for p in future_periods],
                    "Forecasted Cost": [f"${f:,.2f}" for f in forecasts],
                    "Change from Last Actual": [f"${f - historical_costs[-1]:+,.2f}" for f in forecasts],
                    "Change %": [f"{(f - historical_costs[-1])/historical_costs[-1]*100:+.1f}%" for f in forecasts]
                })
                st.dataframe(summary_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Trend per Period", f"${slope:+,.2f}")
                with col2: st.metric("R² (Fit Quality)", f"{r_squared:.4f}")
                with col3:
                    trend_desc = "📈 Increasing" if slope > 0 else ("📉 Decreasing" if slope < 0 else "➡️ Flat")
                    st.metric("Cost Trend", trend_desc)

                if r_squared > 0.8:
                    st.success(f"✅ Strong linear trend (R² = {r_squared:.3f}). Forecast is reliable.")
                elif r_squared > 0.5:
                    st.warning(f"⚠️ Moderate fit (R² = {r_squared:.3f}). Forecast may be less reliable.")
                else:
                    st.error(f"❌ Weak fit (R² = {r_squared:.3f}). Data is volatile — use forecast with caution.")

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Porter's Generic Strategies Matrix")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=[1, 3, 2], y=[3, 3, 1],
            mode="markers+text",
            marker=dict(size=[80, 80, 80], color=["#2E86C1", "#E67E22", "#27AE60"], opacity=0.8),
            text=["Cost<br>Leadership", "Differentiation", "Focus<br>Strategy"],
            textposition="middle center",
            textfont=dict(size=12, color="white")
        ))
        fig1.update_layout(
            title="Porter's Generic Strategies",
            xaxis=dict(title="Competitive Scope", tickvals=[1, 2, 3], ticktext=["Industry-Wide", "", "Narrow Segment"]),
            yaxis=dict(title="Competitive Advantage", tickvals=[1, 3], ticktext=["Cost", "Uniqueness"]),
            showlegend=False
        )
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Value Chain Waterfall Chart")
        activities_wf = ["Inbound", "Operations", "Outbound", "Marketing", "Service", "Support", "Total"]
        our_costs_wf = [80, 200, 60, 150, 40, 120, 650]
        comp_costs_wf = [70, 250, 55, 180, 35, 110, 700]

        fig2 = go.Figure(data=[
            go.Bar(name="Our Company", x=activities_wf, y=our_costs_wf, marker_color="#2E86C1"),
            go.Bar(name="Competitor", x=activities_wf, y=comp_costs_wf, marker_color="#E74C3C")
        ])
        fig2.update_layout(title="Value Chain Cost Comparison", barmode="group", yaxis_title="Cost ($000)")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Carbon Emissions by Scope")
        scopes = ["Scope 1\n(Direct)", "Scope 2\n(Electricity)", "Scope 3\n(Value Chain)"]
        emissions_scope = [2836, 900, 90]
        fig3 = px.pie(values=emissions_scope, names=scopes,
                      title="Carbon Emissions Distribution",
                      color_discrete_sequence=["#E74C3C", "#E67E22", "#3498DB"])
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Analytics Maturity Journey")
        maturity_levels = ["Descriptive\n(What happened?)", "Diagnostic\n(Why?)", "Predictive\n(What will happen?)", "Prescriptive\n(What should we do?)"]
        maturity_value = [10, 25, 50, 100]
        maturity_complexity = [1, 2, 3, 4]
        fig4 = go.Figure(go.Bar(
            x=maturity_levels, y=maturity_value,
            marker_color=["#AED6F1", "#2E86C1", "#1A5276", "#0E3460"],
            text=[f"Value: {v}%<br>Complexity: {c}/4" for v, c in zip(maturity_value, maturity_complexity)],
            textposition="auto"
        ))
        fig4.update_layout(title="Analytics Maturity Model — Value vs Complexity",
                           yaxis_title="Business Value (%)")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. Strategic Management Accounting differs from traditional MA primarily by:**")
        q1 = st.radio("", [
            "Focusing only on historical financial data",
            "Incorporating external competitive intelligence and long-term strategic focus",
            "Using simpler costing methods",
            "Eliminating the need for variance analysis"
        ], key="m15q1")
        if st.button("Check Q1", key="m15c1"):
            if q1 == "Incorporating external competitive intelligence and long-term strategic focus":
                st.success("✅ Correct! SMA extends beyond internal data to include competitor analysis, market positioning, and long-term strategic value.")
            else:
                st.error("❌ Incorrect. SMA distinguishes itself by incorporating EXTERNAL competitive information and long-term strategic thinking alongside internal data.")

        st.markdown("---")
        st.markdown("**Q2. Under a Cost Leadership strategy, the primary SMA focus should be:**")
        q2 = st.radio("", [
            "R&D investment and innovation metrics",
            "Customer satisfaction and brand equity",
            "Cost reduction, process efficiency, and productivity",
            "Premium pricing and margin analysis"
        ], key="m15q2")
        if st.button("Check Q2", key="m15c2"):
            if q2 == "Cost reduction, process efficiency, and productivity":
                st.success("✅ Correct! Cost leadership demands relentless focus on cost reduction, efficiency improvement, and productivity gains.")
            else:
                st.error("❌ Incorrect. Cost leadership strategy focuses accounting on cost reduction, process efficiency, and productivity metrics.")

        st.markdown("---")
        st.markdown("""
        **Q3. Annual Margin = $40,000. Retention Rate = 80%. Discount Rate = 10%.
        What is the Customer Lifetime Value?**
        """)
        q3 = st.radio("", ["$100,000", "$133,333", "$200,000", "$400,000"], key="m15q3")
        if st.button("Check Q3", key="m15c3"):
            clv_calc = 40000 / (1 + 0.10 - 0.80)
            if q3 == "$133,333":
                st.success(f"✅ Correct! CLV = $40,000 / (1 + 10% − 80%) = $40,000 / 0.30 = ${clv_calc:,.0f}")
            else:
                st.error(f"❌ Incorrect. CLV = $40,000 / (1 + 0.10 − 0.80) = $40,000 / 0.30 = $133,333")

        st.markdown("---")
        st.markdown("**Q4. The Triple Bottom Line in sustainability accounting refers to:**")
        q4 = st.radio("", [
            "Revenue, Profit, and Cash Flow",
            "Short-term, Medium-term, and Long-term profits",
            "People (Social), Planet (Environmental), and Profit (Economic)",
            "Prevention, Appraisal, and Failure costs"
        ], key="m15q4")
        if st.button("Check Q4", key="m15c4"):
            if q4 == "People (Social), Planet (Environmental), and Profit (Economic)":
                st.success("✅ Correct! The Triple Bottom Line framework measures performance across three dimensions: People, Planet, and Profit.")
            else:
                st.error("❌ Incorrect. Triple Bottom Line = People (social impact), Planet (environmental impact), and Profit (economic performance).")

        st.markdown("---")
        st.markdown("**Q5. Prescriptive analytics answers the question:**")
        q5 = st.radio("", [
            "What happened in the past?",
            "Why did something happen?",
            "What is likely to happen?",
            "What should we do about it?"
        ], key="m15q5")
        if st.button("Check Q5", key="m15c5"):
            if q5 == "What should we do about it?":
                st.success("✅ Correct! Prescriptive analytics is the most advanced level — it recommends actions to optimize outcomes.")
            else:
                st.error("❌ Incorrect. Prescriptive analytics answers 'What should we do?' — recommending optimal actions. (Descriptive=What happened, Diagnostic=Why, Predictive=What will happen)")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Strategic Management Accounting Framework")
        sma_df = pd.DataFrame({
            "SMA Tool": ["Value Chain Analysis", "Benchmarking", "Customer Lifetime Value",
                          "Competitor Cost Analysis", "Sustainability Accounting",
                          "Predictive Analytics", "Integrated Reporting"],
            "Purpose": [
                "Identify where value is created/destroyed across activities",
                "Compare performance vs best-in-class to close gaps",
                "Measure long-term value of customer relationships",
                "Understand competitor cost structure and advantage",
                "Account for environmental and social costs",
                "Forecast future costs and performance",
                "Report across all six capitals of value creation"
            ],
            "Key Output": [
                "Cost and value driver map", "Gap analysis and improvement targets",
                "CLV, CAC, CLV:CAC ratio", "Cost advantage/disadvantage analysis",
                "Carbon footprint, ESG metrics", "Cost forecasts, trend analysis",
                "Multi-capital performance report"
            ]
        })
        st.dataframe(sma_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Key Formulas")
        formulas_df = pd.DataFrame({
            "Formula": ["Customer Lifetime Value (simplified)", "CLV:CAC Ratio",
                         "Carbon Footprint", "Carbon Cost",
                         "Benchmarking Gap", "Value Chain Net Position",
                         "Risk-Adjusted Return", "Analytics R² (forecast quality)"],
            "Expression": [
                "Annual Margin / (1 + Discount Rate − Retention Rate)",
                "CLV / Customer Acquisition Cost (target: > 3:1)",
                "Σ (Activity Level × Emission Factor) for all sources",
                "Total CO₂ Tonnes × Carbon Price per Tonne",
                "(Our Value − Best in Class) / Best in Class × 100",
                "Σ (Competitor Cost − Our Cost) for all activities",
                "Expected Return − (Risk Premium × Risk Exposure)",
                "1 − (SS Residuals / SS Total) — closer to 1.0 = better fit"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("🔍 Strategy → Accounting Alignment")
        strategy_accounting = pd.DataFrame({
            "Strategy": ["Cost Leadership", "Differentiation", "Focus"],
            "Primary Metrics": [
                "Cost/unit, productivity, asset utilisation, variance analysis",
                "Customer satisfaction, CLV, quality costs, R&D ROI, brand equity",
                "Segment margin, niche market share, specialised customer metrics"
            ],
            "Key SMA Tools": [
                "Benchmarking, value engineering, lean accounting, activity analysis",
                "Life-cycle costing, CLV, target costing, balanced scorecard",
                "Segment profitability, specialised value chain, niche benchmarks"
            ],
            "Analytics Focus": [
                "Process efficiency, cost trends, productivity prediction",
                "Customer behaviour, churn prediction, innovation metrics",
                "Segment-specific drivers, penetration depth"
            ]
        })
        st.dataframe(strategy_accounting, use_container_width=True, hide_index=True)

        st.subheader("🌱 Sustainability Accounting Quick Reference")
        sustain_df = pd.DataFrame({
            "Scope": ["Scope 1", "Scope 2", "Scope 3"],
            "Definition": [
                "Direct emissions from owned/controlled sources",
                "Indirect emissions from purchased electricity/heat",
                "All other indirect emissions in value chain"
            ],
            "Examples": [
                "Company vehicles, on-site manufacturing, owned boilers",
                "Purchased grid electricity, steam, heating/cooling",
                "Supplier emissions, business travel, product use/disposal"
            ],
            "Control Level": ["Highest", "Medium", "Lowest (but often largest)"]
        })
        st.dataframe(sustain_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Focusing only on internal costs, ignoring competitor intelligence",
                "Using short-term metrics for long-term strategic decisions",
                "Ignoring customer acquisition costs when measuring profitability",
                "Treating environmental costs as non-financial issues",
                "Applying cost leadership metrics to a differentiation strategy",
                "Using descriptive analytics when predictive tools are available",
                "Treating CLV:CAC ratio below 1 as acceptable"
            ],
            "Correct Approach": [
                "SMA integrates external competitive data with internal cost analysis",
                "Align metrics to strategy time horizon (CLV, life-cycle costs for long-term)",
                "Always compute CLV:CAC — true profitability requires both sides",
                "Carbon costs, remediation costs, and ESG risks are financial risks",
                "Align your accounting metrics to your chosen competitive strategy",
                "Progress from descriptive → diagnostic → predictive → prescriptive",
                "CLV:CAC < 1 means destroying value — urgently review pricing and acquisition"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 15 Complete! You have mastered Strategic Management Accounting — the capstone of managerial accounting expertise!")

        st.balloons()

        st.markdown("""
        ---
        ### 🏆 Congratulations — You Have Completed All 15 Modules!

        You now have expert-level knowledge across the full spectrum of managerial accounting:

        ✅ **Foundations** — Cost classification, cost behaviour
        ✅ **CVP Analysis** — Break-even, contribution margin, operating leverage
        ✅ **Costing Systems** — Job order, process, ABC
        ✅ **Cost Allocation** — Service departments, joint products
        ✅ **Reporting Methods** — Variable vs absorption costing
        ✅ **Planning** — Master budgets, standard costs, variance analysis
        ✅ **Performance** — Responsibility accounting, ROI, RI, EVA
        ✅ **Decisions** — Relevant costs, capital budgeting, pricing
        ✅ **Advanced** — Quality, lean, strategic management accounting

        *You are ready to apply these skills professionally and pursue certifications such as CMA, CIMA, or ACCA.*
        """)

if __name__ == "__main__":
    show()