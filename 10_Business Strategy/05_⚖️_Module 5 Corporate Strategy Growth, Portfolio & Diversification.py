import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏢 Module 5: Corporate Strategy — Growth, Portfolio & Diversification")
    st.markdown("*Master Ansoff, BCG, M&A valuation, and capital allocation across a diversified corporation*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Corporate vs. Business-Level Strategy")
        st.markdown("""
        **Corporate strategy** answers: *What businesses should we be in, and how does owning them together create more value than if they were separate?*

        **Corporate parenting advantage** = the value HQ adds to business units beyond what they could achieve alone.
        - Capital allocation across units
        - Shared capabilities and knowledge
        - Risk diversification
        - Governance and management standards

        **Finance critical test**: Does corporate HQ create or destroy value? If the **sum of parts > whole** (conglomerate discount), break-up may unlock value.
        """)

        st.subheader("2. Ansoff Growth Matrix")
        ansoff_data = {
            "Strategy": ["Market Penetration", "Market Development", "Product Development", "Diversification"],
            "Definition": [
                "Sell more of existing products to existing markets",
                "Sell existing products in new markets (geography, segment)",
                "Develop new products for existing markets",
                "Enter new markets with new products"
            ],
            "Risk Level": ["Lowest", "Low-Medium", "Medium-High", "Highest"],
            "Investment Required": ["Low (operational efficiency)", "Medium (market entry costs)", "Medium-High (R&D, development)", "Very High (capability + market build)"],
            "Finance Focus": [
                "Improve asset utilisation, pricing power, cost-to-serve",
                "Market entry costs, geographic expansion model, FX risk",
                "R&D investment appraisal, innovation ROI, NPD pipeline",
                "M&A valuation, synergies, diversification premium vs discount"
            ],
            "Financial Metrics": ["Revenue growth %, market share, ROIC improvement", "Revenue from new markets, market entry cost per $1 of revenue", "New product revenue %, R&D ROI, development payback", "Conglomerate ROIC vs sum-of-parts, synergy realisation"]
        }
        st.dataframe(pd.DataFrame(ansoff_data), use_container_width=True, hide_index=True)

        st.subheader("3. BCG Growth-Share Matrix")
        st.markdown("""
        The BCG matrix classifies business units by **market growth rate** (investment needs) and **relative market share** (competitive position / cash generation).

        | Quadrant | Growth | Share | Cash Flow | Strategy |
        |----------|--------|-------|-----------|---------|
        | ⭐ **Stars** | High | High | Neutral (invest = generate) | Invest to maintain leadership |
        | ❓ **Question Marks** | High | Low | Negative (needs cash) | Invest selectively or divest |
        | 🐄 **Cash Cows** | Low | High | Positive (harvest) | Milk for cash; minimal investment |
        | 🐕 **Dogs** | Low | Low | Neutral/Negative | Divest or restructure |

        **Finance implication**: Cash Cows fund Stars and selective Question Marks.
        Dogs should be divested unless strategic reasons justify retention.
        """)

        st.subheader("4. GE-McKinsey Matrix")
        st.markdown("""
        More sophisticated than BCG — uses **industry attractiveness** (multiple PESTLE/Five Forces factors) vs
        **business unit strength** (multiple VRIN/competitive factors) to guide investment decisions.

        | Zone | Action | Finance Decision |
        |------|--------|-----------------|
        | Top-right (attractive + strong) | Invest / Grow | High capital allocation, growth investment |
        | Middle diagonal | Hold / Selectively invest | Maintain; improve selectively |
        | Bottom-left (unattractive + weak) | Harvest / Divest | Reduce capex; manage for cash; explore exit |
        """)

        st.subheader("5. M&A Strategy — Rationale & Valuation")
        st.markdown("""
        **Strategic rationale for M&A:**
        - **Market access**: Enter new geography or segment quickly
        - **Capability acquisition**: Buy technology, talent, or IP
        - **Scale synergies**: Cost reduction through consolidation
        - **Revenue synergies**: Cross-selling, combined market power

        **Valuation approaches:**
        | Method | Approach | Best Used When |
        |--------|----------|---------------|
        | DCF | PV of future free cash flows | Long-term asset, stable cash flows |
        | Comparable Companies (EV/EBITDA) | Peer group multiples | Active market comparables available |
        | Precedent Transactions | Historical deal multiples | Recent comparable transactions |
        | Sum-of-Parts | Value each business separately | Diversified conglomerate |

        **Synergy types:**
        - **Cost synergies**: Headcount reduction, facility consolidation, procurement savings — usually 70–80% achievable
        - **Revenue synergies**: Cross-sell, new markets, pricing — usually 30–40% achievable
        """)

        st.subheader("6. Capital Allocation Framework")
        st.markdown("""
        **The CFO's most important strategic role**: allocate finite capital to the highest-return opportunities.

        **Capital allocation hierarchy:**
        1. **Maintain** — reinvest to maintain existing competitive position (keep moat)
        2. **Grow** — invest in strategic growth initiatives with ROIC > WACC
        3. **M&A** — acquire if price + integration creates value (synergy NPV > premium paid)
        4. **Return to shareholders** — dividends and buybacks when no better internal use

        **Capital allocation scorecard**: ROIC on each category of investment vs. WACC hurdle rate.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Ansoff Matrix in Practice — Starbucks")
        starbucks = {
            "Strategy": ["Market Penetration", "Market Development", "Product Development", "Diversification"],
            "Starbucks Action": [
                "Loyalty programme driving visit frequency; mobile ordering reducing friction",
                "China expansion — 6,000+ stores; India market entry",
                "Oat milk range; Starbucks Reserve premium tier; food menu expansion",
                "Starbucks Channel Development (CPG grocery sales of packaged coffee)"
            ],
            "Financial Result": [
                "Same-store sales growth 5–7% pa; comp sales outperform peers",
                "China now 2nd largest market; $1B+ revenue; 20%+ growth pa",
                "Premium Reserve stores carry 3× average unit volume",
                "CPG segment generates $2B+ revenue at 30%+ operating margin"
            ],
            "Risk Realised": [
                "Minimal — deep market knowledge, operational excellence",
                "Cultural adaptation challenges; higher pre-opening losses",
                "Product development costs; cannabilisation of existing lines",
                "Brand confusion; management distraction from core business"
            ]
        }
        st.dataframe(pd.DataFrame(starbucks), use_container_width=True, hide_index=True)

        st.subheader("Example 2: BCG Matrix — Consumer Goods Conglomerate")
        bcg_example = {
            "Business Unit": ["Premium Skincare", "Household Cleaning", "Low-Cost Shampoo", "Fax Machine Supplies"],
            "BCG Quadrant": ["⭐ Star", "🐄 Cash Cow", "❓ Question Mark", "🐕 Dog"],
            "Market Growth": ["18%", "2%", "12%", "-5%"],
            "Relative Market Share": ["1.4x", "2.1x", "0.4x", "0.6x"],
            "Annual Cash Flow": ["-$15M", "+$45M", "-$28M", "+$2M"],
            "Recommended Action": [
                "Invest $20M pa to maintain leadership position",
                "Harvest cash; minimal investment; fund Stars",
                "Invest $15M to build share OR divest if unachievable",
                "Divest — return capital; no strategic future"
            ],
            "Finance Logic": [
                "High market growth demands investment; high share protects return",
                "Low growth = low reinvestment need; high share = strong ROIC",
                "High growth but low share = cash drain; must earn right to invest",
                "No growth + low share = capital trap; divest at best available price"
            ]
        }
        st.dataframe(pd.DataFrame(bcg_example), use_container_width=True, hide_index=True)

        st.subheader("Example 3: M&A Synergy Analysis")
        st.markdown("""
        **Acquisition: Company A (Acquirer) buying Company B (Target)**

        **Target Financials:**
        - Revenue: $80M | EBITDA: $12M (15% margin) | Asking price: $72M (6× EBITDA)

        **Synergy Analysis:**
        | Synergy Type | Annual Value | Confidence | NPV (8% discount, 5yr) |
        |-------------|-------------|------------|----------------------|
        | Cost synergies — headcount | $3.5M | High (90%) | $14.0M |
        | Cost synergies — facilities | $1.2M | High (85%) | $4.8M |
        | Revenue synergies — cross-sell | $2.0M | Medium (50%) | $5.0M (risk-adjusted) |
        | Revenue synergies — pricing | $0.8M | Low (30%) | $1.1M (risk-adjusted) |
        | **Total Synergy NPV** | | | **$24.9M** |

        **Deal Economics:**
        - Price paid: $72M
        - Target standalone value (DCF): $55M
        - Premium paid: $17M
        - Synergy NPV: $24.9M
        - **Net value created: $24.9M − $17M = $7.9M** ✅ Deal creates value

        **Warning**: Revenue synergies are rarely fully achieved. Conservative CFOs model cost synergies only.
        """)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "BCG Portfolio Analyser",
            "M&A Synergy & Value Calculator",
            "Capital Allocation Optimizer"
        ])

        if tool == "BCG Portfolio Analyser":
            st.subheader("📊 BCG Portfolio Analyser")
            num_units = st.number_input("Number of business units:", 2, 6, 4)
            units = []
            for i in range(int(num_units)):
                st.markdown(f"**Business Unit {i+1}:**")
                col1, col2, col3, col4 = st.columns(4)
                with col1: name = st.text_input("Name:", value=f"Unit {chr(65+i)}", key=f"bcg_n_{i}")
                with col2: growth = st.number_input("Market Growth (%):", -10.0, 40.0, float(10 - i * 4), 0.5, key=f"bcg_g_{i}")
                with col3: rms = st.number_input("Rel. Market Share (x):", 0.1, 5.0, float(1.5 - i * 0.3), 0.1, key=f"bcg_s_{i}")
                with col4: revenue = st.number_input("Revenue ($M):", 1.0, 500.0, float(50 + i * 20), 5.0, key=f"bcg_r_{i}")
                if growth >= 10 and rms >= 1.0: quadrant = "⭐ Star"
                elif growth >= 10 and rms < 1.0: quadrant = "❓ Question Mark"
                elif growth < 10 and rms >= 1.0: quadrant = "🐄 Cash Cow"
                else: quadrant = "🐕 Dog"
                units.append({"Unit": name, "Growth (%)": f"{growth:.1f}%", "Rel. Share": f"{rms:.1f}x", "Revenue ($M)": f"${revenue:.0f}M", "Quadrant": quadrant,
                              "Recommendation": "Invest to maintain leadership" if quadrant == "⭐ Star" else ("Milk for cash; minimal capex" if quadrant == "🐄 Cash Cow" else ("Invest selectively or divest" if quadrant == "❓ Question Mark" else "Divest; redeploy capital"))})

            st.dataframe(pd.DataFrame(units), use_container_width=True, hide_index=True)
            stars = sum(1 for u in units if "Star" in u["Quadrant"])
            cows = sum(1 for u in units if "Cow" in u["Quadrant"])
            qmarks = sum(1 for u in units if "Question" in u["Quadrant"])
            dogs = sum(1 for u in units if "Dog" in u["Quadrant"])
            if cows > 0 and stars > 0:
                st.success(f"✅ Healthy portfolio: {cows} Cash Cow(s) funding {stars} Star(s). Continue investing in Stars.")
            if dogs > 0:
                st.warning(f"⚠️ {dogs} Dog(s) identified. Consider divestiture to redeploy capital to Stars and Question Marks.")

        elif tool == "M&A Synergy & Value Calculator":
            st.subheader("🤝 M&A Synergy & Value Calculator")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Target Company:**")
                target_ebitda = st.number_input("Target EBITDA ($M):", 0.1, 500.0, 20.0, 1.0)
                deal_multiple = st.number_input("Deal Multiple (EV/EBITDA):", 3.0, 20.0, 8.0, 0.5)
                standalone_value = st.number_input("Standalone DCF Value ($M):", 0.1, 500.0, 120.0, 5.0)
            with col2:
                st.markdown("**Synergies:**")
                cost_synergies = st.number_input("Annual Cost Synergies ($M):", 0.0, 100.0, 8.0, 0.5)
                cost_confidence = st.slider("Cost Synergy Confidence (%):", 0, 100, 80)
                rev_synergies = st.number_input("Annual Revenue Synergies ($M):", 0.0, 100.0, 5.0, 0.5)
                rev_confidence = st.slider("Revenue Synergy Confidence (%):", 0, 100, 40)

            discount_rate = st.slider("Discount Rate for Synergy NPV (%):", 5.0, 15.0, 8.0, 0.5)
            synergy_years = st.slider("Synergy Duration (years):", 3, 10, 5)

            deal_price = target_ebitda * deal_multiple
            premium_paid = deal_price - standalone_value
            pv_factor = sum([1 / (1 + discount_rate / 100) ** t for t in range(1, synergy_years + 1)])
            cost_npv = cost_synergies * (cost_confidence / 100) * pv_factor
            rev_npv = rev_synergies * (rev_confidence / 100) * pv_factor
            total_synergy_npv = cost_npv + rev_npv
            net_value_created = total_synergy_npv - premium_paid

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Deal Price", f"${deal_price:.1f}M")
                st.metric("Premium Paid", f"${premium_paid:.1f}M")
            with col2:
                st.metric("Cost Synergy NPV", f"${cost_npv:.1f}M")
                st.metric("Revenue Synergy NPV", f"${rev_npv:.1f}M")
            with col3:
                st.metric("Total Synergy NPV", f"${total_synergy_npv:.1f}M")
                st.metric("Net Value Created", f"${net_value_created:.1f}M", f"{'✅ Accretive' if net_value_created > 0 else '❌ Dilutive'}")

            if net_value_created > 0:
                st.success(f"✅ **Deal creates value**: Synergy NPV (${total_synergy_npv:.1f}M) > Premium Paid (${premium_paid:.1f}M) by ${net_value_created:.1f}M.")
            else:
                st.error(f"❌ **Deal destroys value**: Premium Paid (${premium_paid:.1f}M) exceeds achievable Synergy NPV (${total_synergy_npv:.1f}M) by ${abs(net_value_created):.1f}M.")

        else:  # Capital Allocation
            st.subheader("💰 Capital Allocation Optimizer")
            total_capital = st.number_input("Total Capital Available ($M):", 10.0, 1000.0, 100.0, 10.0)
            wacc_hurdle = st.slider("WACC / Hurdle Rate (%):", 5.0, 15.0, 9.0, 0.5)
            st.markdown("**Allocate across strategic priorities:**")
            options = ["Maintain Core Business", "Organic Growth (Stars)", "M&A", "Digital Transformation", "Shareholder Returns (Buy-back/Dividend)"]
            expected_returns = [7.0, 15.0, 12.0, 11.0, 0.0]
            allocations = []
            for opt, er in zip(options, expected_returns):
                col1, col2 = st.columns([2, 1])
                with col1: alloc = st.slider(f"{opt} (Expected ROIC: {er}%):", 0.0, float(total_capital), float(total_capital / len(options)), 1.0, key=f"ca_{opt}")
                with col2: st.markdown(f"**${alloc:.0f}M**")
                allocations.append((opt, alloc, er))

            total_allocated = sum(a[1] for a in allocations)
            weighted_return = sum(a[1] * a[2] for a in allocations) / total_allocated if total_allocated > 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Total Allocated", f"${total_allocated:.0f}M", f"${total_allocated - total_capital:+.0f}M vs available")
            with col2: st.metric("Weighted Expected Return", f"{weighted_return:.1f}%", f"{weighted_return - wacc_hurdle:+.1f}% vs WACC")
            with col3:
                value_creating = sum(a[1] for a in allocations if a[2] > wacc_hurdle)
                st.metric("Capital in Value-Creating Use", f"${value_creating:.0f}M", f"{value_creating / total_allocated * 100:.0f}% of deployed" if total_allocated > 0 else "0%")

            if total_allocated > total_capital * 1.05:
                st.error("❌ Over-allocated! Reduce allocations or secure additional capital.")
            elif weighted_return > wacc_hurdle:
                st.success(f"✅ Portfolio weighted return ({weighted_return:.1f}%) exceeds WACC ({wacc_hurdle}%) — capital plan is value-creating.")
            else:
                st.warning(f"⚠️ Weighted return ({weighted_return:.1f}%) is below WACC ({wacc_hurdle}%). Reallocate toward higher-return opportunities.")

    with tab4:
        st.header("Visualizations")

        st.subheader("BCG Matrix — Portfolio Map")
        bcu_names = ["Premium Skincare", "Household Cleaning", "Discount Shampoo", "Fax Supplies", "Digital Health"]
        growth_rates = [18, 2, 12, -5, 22]
        market_shares = [1.4, 2.1, 0.4, 0.6, 0.3]
        revenues = [80, 150, 40, 20, 35]
        quad_colors = []
        for g, s in zip(growth_rates, market_shares):
            if g >= 10 and s >= 1.0: quad_colors.append("#1B3A6B")
            elif g >= 10 and s < 1.0: quad_colors.append("#D97706")
            elif g < 10 and s >= 1.0: quad_colors.append("#27AE60")
            else: quad_colors.append("#E74C3C")

        fig_bcg = go.Figure()
        fig_bcg.add_shape(type="rect", x0=1, y0=10, x1=3, y1=35, fillcolor="rgba(27,58,107,0.1)", line=dict(color="gray", width=1))
        fig_bcg.add_shape(type="rect", x0=0, y0=10, x1=1, y1=35, fillcolor="rgba(215,119,6,0.1)", line=dict(color="gray", width=1))
        fig_bcg.add_shape(type="rect", x0=1, y0=-10, x1=3, y1=10, fillcolor="rgba(39,174,96,0.1)", line=dict(color="gray", width=1))
        fig_bcg.add_shape(type="rect", x0=0, y0=-10, x1=1, y1=10, fillcolor="rgba(231,76,60,0.1)", line=dict(color="gray", width=1))
        for name, g, s, r, c in zip(bcu_names, growth_rates, market_shares, revenues, quad_colors):
            fig_bcg.add_trace(go.Scatter(x=[s], y=[g], mode="markers+text", text=[name],
                                         textposition="top center", marker=dict(size=r * 0.6, color=c, opacity=0.8),
                                         name=name, showlegend=False))
        fig_bcg.add_vline(x=1.0, line_dash="dash", line_color="gray", annotation_text="Relative Share = 1.0")
        fig_bcg.add_hline(y=10, line_dash="dash", line_color="gray", annotation_text="Growth = 10%")
        fig_bcg.update_layout(title="BCG Matrix — Portfolio Map (bubble size = revenue)", height=500,
                              xaxis_title="Relative Market Share", yaxis_title="Market Growth Rate (%)")
        st.plotly_chart(fig_bcg, use_container_width=True)

        st.subheader("Ansoff Matrix — Risk-Return Profile")
        strategies_a = ["Market Penetration", "Market Development", "Product Development", "Diversification"]
        risks_a = [1, 2, 3, 4]
        returns_a = [1.5, 2.5, 3.5, 5.0]
        fig_ansoff = go.Figure()
        colors_a = ["#27AE60", "#2563EB", "#D97706", "#E74C3C"]
        for s, r, ret, c in zip(strategies_a, risks_a, returns_a, colors_a):
            fig_ansoff.add_trace(go.Scatter(x=[r], y=[ret], mode="markers+text", text=[s],
                                            textposition="top right", marker=dict(size=30, color=c),
                                            name=s, showlegend=True))
        fig_ansoff.update_layout(title="Ansoff Matrix — Risk vs Return Profile", height=400,
                                 xaxis=dict(title="Risk Level", range=[0, 5], tickvals=[1, 2, 3, 4], ticktext=["Low", "Med-Low", "Med-High", "High"]),
                                 yaxis=dict(title="Expected Return Potential", range=[0, 6]))
        st.plotly_chart(fig_ansoff, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. In the BCG Matrix, a 'Cash Cow' is characterised by:**")
        q1 = st.radio("", ["High market growth and high market share", "Low market growth and high relative market share",
                           "High market growth and low market share", "Low growth and low share"], key="bs5q1")
        if st.button("Check Answer", key="bs5c1"):
            if q1 == "Low market growth and high relative market share":
                st.success("✅ Correct! Cash Cows are in mature (low-growth) markets but have strong market positions — generating excess cash to fund Stars.")
            else:
                st.error("❌ Incorrect. Cash Cow = low market growth (mature) + high relative market share (strong position = cash generation).")

        st.markdown("---")
        st.markdown("**2. Which Ansoff strategy carries the HIGHEST risk?**")
        q2 = st.radio("", ["Market Penetration", "Market Development", "Product Development", "Diversification"], key="bs5q2")
        if st.button("Check Answer", key="bs5c2"):
            if q2 == "Diversification":
                st.success("✅ Correct! Diversification involves both a new product AND a new market — unfamiliar territory on both dimensions.")
            else:
                st.error("❌ Incorrect. Diversification (new product + new market) carries the highest risk in the Ansoff matrix.")

        st.markdown("---")
        st.markdown("**3. In M&A, 'synergies' refer to:**")
        q3 = st.radio("", [
            "The premium paid above standalone value",
            "The additional value created by combining two companies beyond their standalone values",
            "The integration costs after an acquisition",
            "The target company's existing profitability"
        ], key="bs5q3")
        if st.button("Check Answer", key="bs5c3"):
            if q3 == "The additional value created by combining two companies beyond their standalone values":
                st.success("✅ Correct! Synergies = cost savings + revenue uplift achieved by combining — the financial justification for paying an acquisition premium.")
            else:
                st.error("❌ Incorrect. Synergies are the incremental value from combining (cost + revenue) beyond what each company creates independently.")

        st.markdown("---")
        st.markdown("**4. What is the correct capital allocation priority hierarchy?**")
        q4 = st.radio("", [
            "Buybacks → M&A → Growth → Maintenance",
            "Maintenance → Growth → M&A → Return to shareholders",
            "M&A → Growth → Maintenance → Dividends",
            "Growth → M&A → Buybacks → Maintenance"
        ], key="bs5q4")
        if st.button("Check Answer", key="bs5c4"):
            if q4 == "Maintenance → Growth → M&A → Return to shareholders":
                st.success("✅ Correct! First maintain competitive position, then invest in growth, then M&A if value-creative, then return surplus capital.")
            else:
                st.error("❌ Incorrect. Priority: 1) Maintain, 2) Grow organically, 3) M&A, 4) Return capital when no better use exists.")

        st.markdown("---")
        st.markdown("**5. A conglomerate discount occurs when:**")
        q5 = st.radio("", [
            "The combined company trades at a premium to the sum of its parts",
            "The market values the diversified company BELOW the sum of its individual parts",
            "Interest rates rise after a large acquisition",
            "The acquiring company pays too little"
        ], key="bs5q5")
        if st.button("Check Answer", key="bs5c5"):
            if q5 == "The market values the diversified company BELOW the sum of its individual parts":
                st.success("✅ Correct! A conglomerate discount signals investors believe HQ is destroying value — break-up may unlock shareholder value.")
            else:
                st.error("❌ Incorrect. A conglomerate discount = market value < sum-of-parts value, signalling corporate HQ is destroying value.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Ansoff Growth Matrix
        | Strategy | Risk | Finance Focus |
        |----------|------|--------------|
        | Market Penetration | Low | ROIC improvement, operational efficiency |
        | Market Development | Medium | Entry costs, FX risk, market sizing |
        | Product Development | Medium-High | R&D ROI, NPD pipeline, development payback |
        | Diversification | Highest | M&A valuation, synergy model, sum-of-parts |

        ### 2. BCG Portfolio Strategy
        ```
        ⭐ Stars → Invest to maintain leadership
        🐄 Cash Cows → Harvest; fund Stars
        ❓ Question Marks → Invest selectively or exit
        🐕 Dogs → Divest; redeploy capital
        ```

        ### 3. M&A Value Test
        ```
        Deal creates value IF:
        Synergy NPV > Premium Paid

        Net Value Created = Synergy NPV − Premium Paid
        ```

        ### 4. Capital Allocation Hierarchy
        ```
        1. Maintain competitive position (protect moat)
        2. Organic growth (ROIC > WACC investments)
        3. M&A (if synergy NPV > premium)
        4. Return capital (buybacks / dividends)
        ```
        """)
        st.subheader("📌 Key Formulas")
        st.code("BCG Relative Market Share = Your Market Share / Largest Competitor Share")
        st.code("M&A Net Value = Synergy NPV − Acquisition Premium")
        st.code("Conglomerate Value = Sum of parts − Conglomerate Discount")
        st.code("Synergy NPV = PV(Cost Synergies × Confidence%) + PV(Revenue Synergies × Confidence%)")
        st.success("🎓 **Module 5 Complete!** You can now evaluate corporate growth strategies, analyse M&A deals, and design capital allocation frameworks.")
        st.info("💡 **Next**: Module 6 — Innovation, Disruption & Digital Strategy")

if __name__ == "__main__":
    show()