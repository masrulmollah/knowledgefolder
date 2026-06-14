import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("⚔️ Module 4: Business-Level Strategy & Competitive Positioning")
    st.markdown("*Master Porter's generic strategies, pricing power, ROIC analysis, and how to build sustainable competitive moats*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. What Is Business-Level Strategy?")
        st.markdown("""
        Business-level strategy defines **how a firm competes** within a specific market or industry.
        It answers: *How do we win against rivals to attract and retain customers profitably?*

        **Two fundamental sources of competitive advantage:**
        - **Cost Advantage**: Delivering comparable value at lower cost than rivals
        - **Differentiation Advantage**: Delivering superior value at a premium price customers are willing to pay

        **Finance implication**: Cost advantage → higher gross margins at competitive price.
        Differentiation advantage → higher price realisation → higher revenue per unit.
        Both → ROIC above WACC → economic value creation.
        """)

        st.subheader("2. Porter's Generic Competitive Strategies")
        generic_data = {
            "Strategy": ["Cost Leadership", "Differentiation", "Cost Focus", "Differentiation Focus"],
            "Competitive Scope": ["Broad market", "Broad market", "Narrow segment", "Narrow segment"],
            "Advantage Source": ["Lowest cost", "Unique features / premium value", "Lowest cost in segment", "Premium in niche segment"],
            "Margin Profile": ["High volume, thin-to-moderate margin", "Moderate volume, high margin", "Low-moderate volume, moderate margin", "Low volume, very high margin"],
            "Finance Metrics": ["COGS%, unit economics, scale efficiency", "Gross margin%, pricing power, brand value", "Segment ROIC, cost per unit vs peers", "Segment margin%, CLV, willingness-to-pay"],
            "Risk": ["Technology disruption, new low-cost entrant", "Imitation, price premium erodes", "Segment shrinks or loses attractiveness", "Niche targeted by larger competitor"]
        }
        st.dataframe(pd.DataFrame(generic_data), use_container_width=True, hide_index=True)

        st.subheader("3. The Strategy Clock")
        st.markdown("""
        Bowman's Strategy Clock extends Porter by showing **eight competitive positions** on two axes:
        perceived customer value (low → high) vs. price (low → high).

        | Position | Strategy | Viable? |
        |----------|----------|---------|
        | 1 | No frills (low price, low value) | Yes — cost leadership in price-sensitive segments |
        | 2 | Low price | Yes — requires cost advantage to sustain |
        | 3 | Hybrid (low price, high value) | Yes — very powerful if cost base allows |
        | 4 | Differentiation | Yes — sustainable with genuine value advantage |
        | 5 | Focused differentiation | Yes — premium niche strategy |
        | 6 | Increased price, same value | Risky — monopoly-like; unsustainable |
        | 7 | Increased price, lower value | Failure strategy |
        | 8 | Low value, standard price | Failure strategy |

        **Finance insight**: Position 3 (Hybrid) is strategically powerful but financially demanding — requires simultaneous cost discipline and value investment.
        """)

        st.subheader("4. ROIC as the Core Strategy Metric")
        st.markdown("""
        **Return on Invested Capital (ROIC)** is the definitive financial measure of competitive strategy success.
        It answers: *Is the strategy creating economic value above the cost of capital?*

        ```
        ROIC = NOPAT / Invested Capital
        NOPAT = Net Operating Profit After Tax
        Invested Capital = Fixed Assets + Net Working Capital

        Value Created = (ROIC - WACC) × Invested Capital
        ```

        | ROIC vs WACC | Strategic Signal | Finance Action |
        |-------------|-----------------|----------------|
        | ROIC >> WACC | Strong competitive advantage | Invest aggressively; grow the business |
        | ROIC ≈ WACC | Competitive parity; no moat | Improve positioning or reallocate capital |
        | ROIC < WACC | Value destruction; strategy failing | Restructure, exit, or transform strategy |
        """)

        st.subheader("5. Pricing Strategy")
        st.markdown("""
        Pricing is the most powerful lever in business strategy — a 1% price increase typically improves EBIT by 8–11%.

        | Pricing Approach | Logic | Best Used When |
        |-----------------|-------|---------------|
        | **Value-based pricing** | Price = willingness to pay | Differentiated products; strong brand |
        | **Cost-plus pricing** | Price = cost + target margin | Commodity products; government contracts |
        | **Competitive pricing** | Price = market benchmark | Undifferentiated products; price-sensitive markets |
        | **Penetration pricing** | Low price to gain share | Market entry; network effect businesses |
        | **Skimming** | High price, then reduce | Premium launches; innovation first-movers |
        """)

        st.subheader("6. Building and Defending Competitive Moats")
        st.markdown("""
        A **moat** is a durable structural advantage that protects ROIC over time.

        | Moat Type | How It Works | Financial Signature |
        |-----------|-------------|---------------------|
        | **Network Effects** | Value increases as more users join | Accelerating revenue, high margins at scale |
        | **Switching Costs** | Painful for customers to leave | High retention, recurring revenue, pricing power |
        | **Cost Advantages** | Structural low-cost position | Consistently low COGS%, peers can't compete on price |
        | **Intangible Assets** | Brand, patents, licenses, regulatory approvals | Pricing premium, gross margin premium vs. peers |
        | **Efficient Scale** | Market too small for second competitor | Near-monopoly returns; high ROIC |
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Generic Strategy Identification — Real Companies")
        companies = {
            "Company": ["Ryanair", "Apple iPhone", "Rolex", "IKEA", "Tesla Model S"],
            "Strategy": ["Cost Leadership", "Broad Differentiation", "Focused Differentiation", "Cost Leadership / Hybrid", "Focused Differentiation"],
            "Evidence": [
                "€29 fares; stripped-back service; ~98% seat utilisation; no frills",
                "Premium pricing ($999–$1,599); ecosystem lock-in; brand loyalty; 40%+ gross margins",
                "$10,000–$50,000 watches; craftsmanship heritage; waitlists; ultra-premium brand",
                "Low prices + strong Scandinavian design aesthetic; flat-pack efficiency; massive scale",
                "$80,000+ EV; performance + sustainability; software-defined; OTA updates"
            ],
            "Gross Margin": ["~25%", "~44%", "~55%+", "~38%", "~18%"],
            "ROIC (approx)": ["18%", "60%+", "35%+", "22%", "8–12%"],
            "Finance Lesson": [
                "Low margin but high asset turns → respectable ROIC",
                "Differentiation drives pricing power → exceptional ROIC",
                "Focused differentiation → extraordinary gross margin in niche",
                "Hybrid requires cost excellence AND value delivery simultaneously",
                "Premium positioning but capital-intensive → ROIC improving as scale builds"
            ]
        }
        st.dataframe(pd.DataFrame(companies), use_container_width=True, hide_index=True)

        st.subheader("Example 2: ROIC Tree Decomposition")
        st.markdown("""
        **Company: Retail business — ROIC analysis to diagnose competitive strategy effectiveness**

        ```
        ROIC = NOPAT Margin × Asset Turnover

        Year 1 (Cost Leadership strategy working well):
        ROIC = 8% × 2.5x = 20%  ✅ Strong — above WACC of 9%

        Year 3 (New low-cost competitor enters):
        ROIC = 5% × 2.2x = 11%  ⚠️ Weakening — moat eroding

        Year 5 (Failed to differentiate or reduce costs further):
        ROIC = 3% × 2.0x = 6%   ❌ Below WACC — value destruction
        ```

        **Strategic diagnosis**: The business lost its cost advantage without building differentiation.
        Finance action: Either invest in genuine differentiation (brand, service, tech) or radically restructure cost base.
        """)
        st.warning("💡 **Finance Insight**: ROIC decomposition via the DuPont framework (Margin × Turnover) reveals WHETHER a strategy is working and WHERE it's breaking down — margin compression vs. capital inefficiency.")

        st.subheader("Example 3: Pricing Power Financial Impact")
        st.markdown("""
        **Scenario**: Company with £100M revenue, 30% gross margin, 10% EBIT margin

        | Pricing Change | Revenue | Gross Profit | EBIT | EBIT Change |
        |---------------|---------|-------------|------|------------|
        | Base (no change) | £100M | £30M | £10M | — |
        | +1% price increase | £101M | £31M | £11M | **+10%** |
        | +5% price increase | £105M | £35M | £15M | **+50%** |
        | -2% price cut | £98M | £28M | £8M | **-20%** |

        **Key insight**: A 1% price increase with no volume loss delivers a ~10% EBIT uplift because the incremental revenue flows almost entirely to profit.
        This is why **pricing power is the #1 financial indicator of competitive advantage**.
        """)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "ROIC Calculator & Value Creation Analyser",
            "Pricing Power Simulator",
            "Competitive Strategy Scorer"
        ])

        if tool == "ROIC Calculator & Value Creation Analyser":
            st.subheader("📊 ROIC Calculator & Value Creation Analyser")
            col1, col2 = st.columns(2)
            with col1:
                revenue = st.number_input("Revenue ($M):", min_value=0.1, value=100.0, step=1.0)
                ebit_margin = st.slider("EBIT Margin (%):", 0.0, 50.0, 12.0, 0.5)
                tax_rate = st.slider("Tax Rate (%):", 0.0, 40.0, 25.0, 0.5)
            with col2:
                fixed_assets = st.number_input("Fixed Assets ($M):", min_value=0.1, value=60.0, step=1.0)
                net_working_capital = st.number_input("Net Working Capital ($M):", min_value=0.0, value=20.0, step=1.0)
                wacc = st.slider("WACC (%):", 4.0, 20.0, 9.0, 0.5)

            ebit = revenue * (ebit_margin / 100)
            nopat = ebit * (1 - tax_rate / 100)
            invested_capital = fixed_assets + net_working_capital
            roic = (nopat / invested_capital * 100) if invested_capital > 0 else 0
            spread = roic - wacc
            eva = (spread / 100) * invested_capital

            col1, col2, col3, col4 = st.columns(4)
            with col1: st.metric("NOPAT", f"${nopat:.1f}M")
            with col2: st.metric("Invested Capital", f"${invested_capital:.1f}M")
            with col3: st.metric("ROIC", f"{roic:.1f}%", f"{spread:+.1f}% vs WACC")
            with col4:
                eva_label = f"+${eva:.1f}M VALUE CREATED" if eva > 0 else f"-${abs(eva):.1f}M VALUE DESTROYED"
                st.metric("Economic Value Added", f"${eva:.1f}M")

            if spread > 5:
                st.success(f"🏆 **Strong Competitive Advantage**: ROIC {roic:.1f}% is {spread:.1f}pp above WACC. Strategy is creating significant economic value. Invest to grow.")
            elif spread > 0:
                st.info(f"✅ **Competitive Parity**: ROIC {roic:.1f}% modestly above WACC {wacc:.1f}%. Some advantage but moat is narrow. Strengthen differentiation or reduce invested capital.")
            else:
                st.error(f"❌ **Value Destruction**: ROIC {roic:.1f}% is {abs(spread):.1f}pp BELOW WACC {wacc:.1f}%. Strategy is failing. Urgent restructuring required.")

            st.markdown("### 🔍 DuPont Decomposition")
            nopat_margin = nopat / revenue * 100 if revenue > 0 else 0
            asset_turnover = revenue / invested_capital if invested_capital > 0 else 0
            decomp = pd.DataFrame({
                "Driver": ["NOPAT Margin (%)", "× Asset Turnover (x)", "= ROIC (%)"],
                "Value": [f"{nopat_margin:.1f}%", f"{asset_turnover:.2f}x", f"{roic:.1f}%"],
                "Interpretation": [
                    "Profitability per $1 of revenue — driven by pricing power and cost efficiency",
                    "Revenue generated per $1 of invested capital — driven by asset efficiency",
                    "Overall return on capital deployed — the ultimate strategy scorecard"
                ]
            })
            st.dataframe(decomp, use_container_width=True, hide_index=True)

        elif tool == "Pricing Power Simulator":
            st.subheader("💰 Pricing Power Simulator")
            st.markdown("See the financial impact of pricing decisions on EBIT:")
            col1, col2 = st.columns(2)
            with col1:
                base_revenue = st.number_input("Base Revenue ($M):", min_value=1.0, value=100.0, step=5.0)
                variable_cost_pct = st.slider("Variable Cost (% of Revenue):", 10, 80, 60)
                fixed_costs = st.number_input("Fixed Costs ($M):", min_value=0.1, value=25.0, step=1.0)
            with col2:
                price_change = st.slider("Price Change (%):", -20, 30, 0)
                volume_elasticity = st.slider("Volume Elasticity (% volume change per 1% price change):", -3.0, 0.0, -0.5, 0.1)

            volume_change = price_change * volume_elasticity
            new_revenue = base_revenue * (1 + price_change / 100) * (1 + volume_change / 100)
            new_variable_costs = new_revenue * (variable_cost_pct / 100)
            new_gross_profit = new_revenue - new_variable_costs
            new_ebit = new_gross_profit - fixed_costs

            base_variable = base_revenue * (variable_cost_pct / 100)
            base_gross = base_revenue - base_variable
            base_ebit = base_gross - fixed_costs
            ebit_change = ((new_ebit - base_ebit) / base_ebit * 100) if base_ebit != 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("New Revenue", f"${new_revenue:.1f}M", f"{(new_revenue - base_revenue):+.1f}M")
            with col2:
                st.metric("New Gross Profit", f"${new_gross_profit:.1f}M", f"{(new_gross_profit - base_gross):+.1f}M")
            with col3:
                st.metric("New EBIT", f"${new_ebit:.1f}M", f"{ebit_change:+.1f}% change")

            if price_change > 0 and ebit_change > 0:
                st.success(f"✅ {price_change}% price increase with {volume_change:.1f}% volume change → EBIT improves {ebit_change:.1f}%. Strong pricing power.")
            elif price_change > 0 and ebit_change < 0:
                st.error(f"❌ {price_change}% price increase caused too much volume loss ({volume_change:.1f}%) → EBIT worsens {abs(ebit_change):.1f}%. Pricing power is weak.")

        else:  # Competitive Strategy Scorer
            st.subheader("🎯 Competitive Strategy Scorer")
            st.markdown("Assess which generic strategy your business is pursuing:")
            questions = [
                ("We compete primarily on lowest price in the market", "cost"),
                ("Our product/service commands a significant price premium vs competitors", "diff"),
                ("We serve a narrow, well-defined customer segment", "focus"),
                ("We continuously invest in cost reduction, automation, and efficiency", "cost"),
                ("Our brand, design, or technology is a key reason customers choose us", "diff"),
                ("We know our target customers better than any competitor", "focus"),
                ("Our gross margins are driven by volume, not price premium", "cost"),
                ("Customers say they would miss our unique features if we disappeared", "diff"),
            ]
            cost_score = diff_score = focus_score = 0
            for i, (q, qtype) in enumerate(questions):
                ans = st.radio(f"**{q}**", ["Strongly Agree (5)", "Agree (4)", "Neutral (3)", "Disagree (2)", "Strongly Disagree (1)"], key=f"cs_{i}", horizontal=True)
                val = int(ans.split("(")[1].replace(")", ""))
                if qtype == "cost": cost_score += val
                elif qtype == "diff": diff_score += val
                else: focus_score += val

            if st.button("🎯 Identify My Strategy"):
                total = {"Cost Leadership": cost_score, "Differentiation": diff_score, "Focus": focus_score}
                dominant = max(total, key=total.get)
                st.markdown("### Your Strategic Profile")
                for strat, score in total.items():
                    st.progress(score / 40, text=f"{strat}: {score}/40")
                st.success(f"🏆 **Dominant Strategy: {dominant}** — with a score of {total[dominant]}/40")
                if dominant == "Cost Leadership":
                    st.info("Finance focus: COGS%, asset turnover, economies of scale, unit economics, cost transformation roadmap.")
                elif dominant == "Differentiation":
                    st.info("Finance focus: Gross margin%, pricing power, brand investment ROI, willingness-to-pay analysis.")
                else:
                    st.info("Finance focus: Segment ROIC, niche market share, CLV, segment-specific cost-to-serve.")

    with tab4:
        st.header("Visualizations")

        st.subheader("Porter's Generic Strategies — Competitive Space")
        fig_generic = go.Figure()
        strategies = [("Cost Leadership", 1.5, 3.5, "#1B3A6B"), ("Differentiation", 3.5, 3.5, "#0D7377"),
                      ("Cost Focus", 1.5, 1.5, "#D97706"), ("Diff. Focus", 3.5, 1.5, "#7C3AED")]
        for name, x, y, color in strategies:
            fig_generic.add_shape(type="rect", x0=x-1.3, y0=y-1.3, x1=x+1.3, y1=y+1.3,
                                  fillcolor=color, opacity=0.7, line=dict(color="white", width=2))
            fig_generic.add_annotation(x=x, y=y, text=f"<b>{name}</b>", font=dict(color="white", size=14), showarrow=False)
        fig_generic.add_annotation(x=2.5, y=5.2, text="← BROAD MARKET →", font=dict(size=12, color="#64748B"), showarrow=False)
        fig_generic.add_annotation(x=2.5, y=-0.3, text="← NARROW SEGMENT →", font=dict(size=12, color="#64748B"), showarrow=False)
        fig_generic.update_layout(title="Porter's Generic Competitive Strategies", height=420,
                                  xaxis=dict(visible=False, range=[0, 5]), yaxis=dict(visible=False, range=[-0.5, 5.5]))
        st.plotly_chart(fig_generic, use_container_width=True)

        st.subheader("ROIC vs WACC — Strategy Performance Benchmark")
        companies_r = ["Ryanair", "Apple", "Rolex", "IKEA", "Amazon AWS", "Average Airline", "Commodity Steel"]
        roic_vals = [18, 60, 38, 22, 55, 6, 7]
        wacc_val = 9
        colors_r = ["#27AE60" if r > wacc_val else "#E74C3C" for r in roic_vals]
        fig_roic = go.Figure()
        fig_roic.add_trace(go.Bar(x=companies_r, y=roic_vals, marker_color=colors_r,
                                  text=[f"{r}%" for r in roic_vals], textposition="auto"))
        fig_roic.add_hline(y=wacc_val, line_dash="dash", line_color="#E74C3C", annotation_text=f"WACC = {wacc_val}%")
        fig_roic.update_layout(title="ROIC vs WACC — Which Strategies Create Value?",
                               yaxis_title="ROIC (%)", height=420)
        st.plotly_chart(fig_roic, use_container_width=True)

        st.subheader("Pricing Power Impact on EBIT")
        price_changes = [-5, -2, -1, 0, 1, 2, 5, 10]
        ebit_impacts = [p * 10 for p in price_changes]
        fig_price = go.Figure(go.Bar(
            x=[f"{p}%" for p in price_changes], y=ebit_impacts,
            marker_color=["#E74C3C" if e < 0 else "#27AE60" for e in ebit_impacts],
            text=[f"{e:+}%" for e in ebit_impacts], textposition="auto"
        ))
        fig_price.add_hline(y=0, line_color="black", line_width=1)
        fig_price.update_layout(title="Price Change → EBIT % Impact (Typical High-Margin Business)",
                                xaxis_title="Price Change (%)", yaxis_title="EBIT Impact (%)", height=380)
        st.plotly_chart(fig_price, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. A company competing with the lowest price across the entire market is pursuing:**")
        q1 = st.radio("", ["Differentiation Focus", "Cost Leadership", "Differentiation", "Cost Focus"], key="bs4q1")
        if st.button("Check Answer", key="bs4c1"):
            if q1 == "Cost Leadership":
                st.success("✅ Correct! Cost Leadership = lowest cost across a broad market, enabling lowest price or highest margins at market price.")
            else:
                st.error("❌ Incorrect. Cost Leadership is competing on lowest cost across the entire (broad) market.")

        st.markdown("---")
        st.markdown("**2. ROIC = 6%, WACC = 9%. This means the business is:**")
        q2 = st.radio("", ["Creating economic value", "At competitive parity", "Destroying economic value", "Perfectly positioned"], key="bs4q2")
        if st.button("Check Answer", key="bs4c2"):
            if q2 == "Destroying economic value":
                st.success("✅ Correct! ROIC < WACC means the strategy is returning less than the cost of capital — economic value is being destroyed.")
            else:
                st.error("❌ Incorrect. When ROIC < WACC, the business earns less than its cost of capital and destroys economic value.")

        st.markdown("---")
        st.markdown("**3. Which pricing approach sets price based on the customer's willingness to pay?**")
        q3 = st.radio("", ["Cost-plus pricing", "Competitive pricing", "Value-based pricing", "Penetration pricing"], key="bs4q3")
        if st.button("Check Answer", key="bs4c3"):
            if q3 == "Value-based pricing":
                st.success("✅ Correct! Value-based pricing anchors the price to what the customer values — not to cost or competitor prices.")
            else:
                st.error("❌ Incorrect. Value-based pricing sets price equal to the customer's willingness to pay for the value delivered.")

        st.markdown("---")
        st.markdown("**4. In the DuPont decomposition, ROIC = ?**")
        q4 = st.radio("", ["Revenue × Margin", "NOPAT Margin × Asset Turnover", "Gross Profit / Equity", "Revenue / Fixed Assets"], key="bs4q4")
        if st.button("Check Answer", key="bs4c4"):
            if q4 == "NOPAT Margin × Asset Turnover":
                st.success("✅ Correct! ROIC = NOPAT/Revenue × Revenue/Invested Capital = NOPAT Margin × Asset Turnover.")
            else:
                st.error("❌ Incorrect. ROIC = NOPAT Margin × Asset Turnover — the DuPont decomposition reveals which driver is most important.")

        st.markdown("---")
        st.markdown("**5. A 'moat' based on high switching costs means:**")
        q5 = st.radio("", [
            "The product is very expensive to make",
            "It is painful or costly for customers to switch to a competitor",
            "There are very few competitors in the market",
            "The company has the lowest prices"
        ], key="bs4q5")
        if st.button("Check Answer", key="bs4c5"):
            if q5 == "It is painful or costly for customers to switch to a competitor":
                st.success("✅ Correct! Switching cost moats lock in customers — driving high retention, recurring revenue, and pricing power.")
            else:
                st.error("❌ Incorrect. A switching cost moat means customers find it difficult or costly to leave — protecting revenue and pricing power.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Porter's Generic Strategies
        | Strategy | Scope | Advantage | Finance Signal |
        |----------|-------|-----------|----------------|
        | Cost Leadership | Broad | Lowest cost | High asset turnover, lean COGS% |
        | Differentiation | Broad | Premium value | High gross margin, pricing power |
        | Cost Focus | Narrow | Low-cost niche | Segment ROIC, unit economics |
        | Diff. Focus | Narrow | Premium niche | Very high segment margin |

        ### 2. ROIC — The Strategy Scorecard
        ```
        ROIC = NOPAT / Invested Capital
        ROIC = NOPAT Margin × Asset Turnover

        Value Created = (ROIC − WACC) × Invested Capital

        ROIC >> WACC → Invest and grow
        ROIC ≈ WACC → Defend or reposition
        ROIC < WACC  → Restructure urgently
        ```

        ### 3. Pricing Power — The #1 Financial Signal of Competitive Advantage
        - 1% price increase → ~10% EBIT improvement (typical business)
        - Pricing power = differentiation working
        - No pricing power = cost leadership only viable option

        ### 4. Competitive Moats
        | Moat | Protects | Financial Signature |
        |------|---------|---------------------|
        | Network effects | Revenue from scale | Accelerating margin at scale |
        | Switching costs | Customer retention | High recurring revenue, NRR > 100% |
        | Intangible assets | Price premium | Gross margin premium vs. peers |
        | Cost advantage | Market share | COGS% structurally below peers |
        """)
        st.subheader("📌 Key Formulas")
        st.code("ROIC = NOPAT / Invested Capital")
        st.code("NOPAT = EBIT × (1 − Tax Rate)")
        st.code("EVA = (ROIC − WACC) × Invested Capital")
        st.code("Price Impact on EBIT ≈ Price Change (%) × (1 / EBIT Margin)")
        st.success("🎓 **Module 4 Complete!** You can now evaluate competitive strategy using ROIC, pricing analysis, and competitive moat assessment.")
        st.info("💡 **Next**: Module 5 — Corporate Strategy: Growth, Portfolio & Diversification")

if __name__ == "__main__":
    show()