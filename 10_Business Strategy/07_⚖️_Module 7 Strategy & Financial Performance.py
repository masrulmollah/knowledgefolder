import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📊 Module 7: Strategy & Financial Performance — Linking Strategy to Value")
    st.markdown("*Master ROIC-WACC, Balanced Scorecard, DuPont analysis, and capital structure decisions that drive long-term value creation*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. The Value Creation Framework")
        st.markdown("""
        All strategy ultimately exists to **create value**. Finance translates strategic choices into quantified value.

        **The fundamental test of value creation:**
        ```
        Economic Value Created = (ROIC − WACC) × Invested Capital
        ```

        **Value drivers — the four levers every strategy must pull:**
        | Value Driver | Description | How Strategy Moves It |
        |-------------|-------------|----------------------|
        | **Revenue Growth** | Top-line expansion rate | Differentiation, market development, innovation |
        | **Margin Improvement** | EBIT and NOPAT margin % | Cost leadership, pricing power, operational efficiency |
        | **Capital Efficiency** | Asset turnover (revenue per $1 of capital) | Working capital management, asset-light models |
        | **Cost of Capital** | WACC — the minimum acceptable return | Capital structure, risk reduction, ESG |

        **Shareholder Value Analysis (SVA)**: Strategy creates value when the increase in PV(future cash flows) exceeds the capital invested.
        """)

        st.subheader("2. The Balanced Scorecard")
        st.markdown("""
        Developed by Kaplan & Norton, the Balanced Scorecard translates strategy into **financial and non-financial KPIs**
        across four interconnected perspectives.
        """)
        bsc_data = {
            "Perspective": ["💰 Financial", "👥 Customer", "⚙️ Internal Process", "🎓 Learning & Growth"],
            "Key Question": [
                "How do we look to shareholders?",
                "How do customers see us?",
                "What must we excel at?",
                "How can we continue to improve and create value?"
            ],
            "Typical KPIs": [
                "ROIC, Revenue growth, EBITDA margin, EPS, Free Cash Flow",
                "NPS, Customer retention, Market share, CLV, Win rate",
                "Cost per unit, Cycle time, Quality rate, On-time delivery, Process efficiency",
                "Employee engagement, Training hours, Innovation pipeline, Digital capability score"
            ],
            "Strategy Link": [
                "Financial outcomes — results of strategic execution",
                "Customer value proposition — differentiator in competitive strategy",
                "Operational excellence — execution engine of strategy",
                "Foundation — capabilities that power all other perspectives"
            ]
        }
        st.dataframe(pd.DataFrame(bsc_data), use_container_width=True, hide_index=True)

        st.subheader("3. DuPont Analysis — Diagnosing Strategy Financial Performance")
        st.markdown("""
        DuPont decomposes ROIC (or ROE) into its component drivers, revealing **where** performance comes from
        and **where** it is breaking down.

        **3-Factor DuPont (ROIC version):**
        ```
        ROIC = NOPAT Margin × Asset Turnover

        NOPAT Margin = NOPAT / Revenue  (profitability driver)
        Asset Turnover = Revenue / Invested Capital  (efficiency driver)
        ```

        **5-Factor DuPont (ROE version):**
        ```
        ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
            = (Net Income/Revenue) × (Revenue/Assets) × (Assets/Equity)
        ```

        | Company Type | Margin | Turnover | ROIC Profile |
        |-------------|--------|----------|-------------|
        | Premium retailer (Luxury) | High (30–50%) | Low (0.5–0.8×) | ROIC driven by margin |
        | Discount retailer (Walmart) | Low (2–4%) | High (2.5–3.5×) | ROIC driven by turnover |
        | Tech platform (Google) | Very high (25–35%) | Medium (0.8–1.2×) | Both high — exceptional ROIC |
        """)

        st.subheader("4. Free Cash Flow as a Strategic Signal")
        st.markdown("""
        **Free Cash Flow (FCF)** is the clearest financial signal of strategic health:
        ```
        FCF = EBITDA − Tax − Capex − Change in Working Capital
        FCF = NOPAT − Net Reinvestment
        ```

        | FCF Pattern | Strategic Interpretation |
        |-------------|------------------------|
        | Growing FCF, rising ROIC | Competitive advantage strengthening — invest and grow |
        | Flat FCF, stable ROIC | Competitive parity — protect position, consider reallocation |
        | Declining FCF, falling ROIC | Moat eroding — strategic change required urgently |
        | Negative FCF, rising ROIC | Growth investment phase — assess sustainability of burn |
        """)

        st.subheader("5. Capital Structure & Strategy")
        st.markdown("""
        Capital structure is a strategic choice — the right mix of debt and equity affects WACC, financial flexibility, and strategic optionality.

        | Capital Structure Decision | Strategic Implication |
        |--------------------------|----------------------|
        | **Low debt (fortress BS)** | Strategic flexibility; counter-cyclical investment; M&A optionality |
        | **Optimal leverage** | Lowest WACC; highest value; tax shield benefit |
        | **High debt** | Limited strategic flexibility; distress risk in downturns; constrains investment |
        | **Share buybacks** | Signal confidence; return surplus capital; improve EPS |
        | **Dividends** | Commit to returning capital; limits reinvestment flexibility |
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Balanced Scorecard — Retail Bank Strategy")
        bsc_example = {
            "Perspective": ["Financial", "Financial", "Customer", "Customer", "Internal Process", "Internal Process", "Learning & Growth", "Learning & Growth"],
            "Strategic Objective": [
                "Grow revenue 12% pa", "Achieve cost-income ratio below 50%",
                "Become #1 in customer NPS in our segment", "Improve digital channel adoption to 80%",
                "Reduce loan approval time to 24 hours", "Achieve zero critical compliance failures",
                "Build data analytics team to 50 FTE", "80% of staff complete digital skills training"
            ],
            "KPI": ["Revenue growth %", "Cost-to-income ratio", "NPS score", "Digital active users %", "Avg loan approval time (hours)", "Critical compliance incidents", "Data analytics FTE", "Training completion %"],
            "Target": ["12%", "< 50%", "> 65", "80%", "< 24 hrs", "0", "50", "80%"],
            "Current": ["8%", "58%", "42", "61%", "72 hrs", "3", "18", "45%"],
            "Status": ["🟠 Behind", "🔴 Behind", "🔴 Behind", "🟠 Behind", "🔴 Behind", "🔴 Behind", "🟡 On track", "🟡 On track"]
        }
        st.dataframe(pd.DataFrame(bsc_example), use_container_width=True, hide_index=True)
        st.warning("💡 **Finance insight**: The Balanced Scorecard reveals this bank's strategy is underperforming across all perspectives. The Learning & Growth lag (data talent, digital skills) is the root cause — it will continue to cascade into process, customer, and financial underperformance.")

        st.subheader("Example 2: DuPont Analysis — Two Competing Retailers")
        st.markdown("""
        | Metric | Luxury Retailer | Discount Retailer |
        |--------|----------------|-----------------|
        | Revenue | $500M | $2,000M |
        | NOPAT | $100M | $60M |
        | Invested Capital | $400M | $600M |
        | **NOPAT Margin** | **20%** | **3%** |
        | **Asset Turnover** | **1.25×** | **3.33×** |
        | **ROIC** | **25%** | **10%** |

        Both businesses earn positive ROIC above WACC (8%) — but via completely different strategic paths.
        The luxury retailer uses **high margin** (premium pricing, differentiation).
        The discount retailer uses **high turnover** (volume, operational efficiency).

        **Finance action**: Each business must protect and strengthen its ROIC driver —
        luxury protects brand premium; discounter protects cost structure and asset efficiency.
        """)

        st.subheader("Example 3: FCF as Strategic Signal — Diagnostic")
        st.markdown("""
        **Company: Industrial Manufacturer — 5-Year FCF Trend Analysis**
        """)
        fcf_data = pd.DataFrame({
            "Year": ["2019", "2020", "2021", "2022", "2023"],
            "EBITDA ($M)": [85, 72, 90, 88, 75],
            "Capex ($M)": [25, 30, 28, 35, 42],
            "Working Capital Δ ($M)": [3, -5, 8, 12, 18],
            "FCF ($M)": [57, 47, 54, 41, 15],
            "ROIC (%)": ["14%", "12%", "15%", "11%", "8%"],
            "Signal": ["✅ Strong", "⚠️ COVID dip", "✅ Recovery", "🟠 Pressure", "🔴 Warning"]
        })
        st.dataframe(fcf_data, use_container_width=True, hide_index=True)
        st.error("🔴 **Strategic Diagnosis**: Rising capex (possible overinvestment or declining efficiency) + working capital build (supply chain issues or collection problems) + falling ROIC signals competitive position is eroding. Finance must challenge whether capex is maintaining/building the moat or represents poor capital allocation.")

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "Balanced Scorecard Builder",
            "DuPont ROIC Analyser",
            "Value Creation Bridge Calculator"
        ])

        if tool == "Balanced Scorecard Builder":
            st.subheader("📋 Balanced Scorecard Builder")
            perspectives = {
                "💰 Financial": [("Revenue Growth Target (%)", 12.0), ("EBITDA Margin Target (%)", 25.0), ("ROIC Target (%)", 18.0), ("FCF Growth Target (%)", 10.0)],
                "👥 Customer": [("NPS Target", 65.0), ("Customer Retention Target (%)", 90.0), ("Market Share Target (%)", 15.0), ("New Customer Acquisition ($M)", 5.0)],
                "⚙️ Internal Process": [("Cost Reduction Target (%)", 8.0), ("On-time Delivery Target (%)", 98.0), ("Cycle Time Reduction Target (%)", 20.0), ("Quality Rate Target (%)", 99.5)],
                "🎓 Learning & Growth": [("Employee Engagement Target (%)", 80.0), ("Training Hours per Employee", 40.0), ("Digital Capability Score (1–10)", 7.0), ("Innovation Projects in Pipeline", 5.0)]
            }
            scorecard_rows = []
            for perspective, kpis in perspectives.items():
                st.markdown(f"**{perspective}:**")
                cols = st.columns(len(kpis))
                for j, (kpi_name, default) in enumerate(kpis):
                    with cols[j]:
                        target = st.number_input(kpi_name, value=default, key=f"bsc_{perspective}_{j}")
                        current = st.number_input(f"Current:", value=default * 0.8, key=f"bsc_c_{perspective}_{j}")
                        pct_achieved = current / target * 100 if target > 0 else 0
                        status = "🟢" if pct_achieved >= 90 else ("🟡" if pct_achieved >= 70 else "🔴")
                        scorecard_rows.append({"Perspective": perspective, "KPI": kpi_name, "Target": target, "Current": current, "Achievement %": f"{pct_achieved:.0f}%", "Status": status})

            if st.button("📊 Generate Scorecard Report"):
                df_sc = pd.DataFrame(scorecard_rows)
                st.dataframe(df_sc, use_container_width=True, hide_index=True)
                red_count = sum(1 for r in scorecard_rows if r["Status"] == "🔴")
                green_count = sum(1 for r in scorecard_rows if r["Status"] == "🟢")
                if red_count > len(scorecard_rows) * 0.5:
                    st.error(f"❌ {red_count} KPIs critically behind target. Strategy execution is at risk.")
                elif green_count > len(scorecard_rows) * 0.7:
                    st.success(f"✅ {green_count} KPIs on/above target. Strategy executing well.")

        elif tool == "DuPont ROIC Analyser":
            st.subheader("🔍 DuPont ROIC Analyser")
            st.markdown("Enter financials for up to 3 companies/periods to compare ROIC drivers:")
            num_companies = st.radio("Number of companies to compare:", [1, 2, 3], horizontal=True)
            results = []
            for i in range(num_companies):
                st.markdown(f"**{'Your Company' if i == 0 else f'Competitor {i}'}:**")
                col1, col2, col3 = st.columns(3)
                with col1: revenue = st.number_input("Revenue ($M):", 0.1, 10000.0, 100.0 * (i + 1), key=f"dp_r_{i}")
                with col2: nopat = st.number_input("NOPAT ($M):", 0.0, 1000.0, 15.0 * (i + 1), key=f"dp_n_{i}")
                with col3: inv_cap = st.number_input("Invested Capital ($M):", 0.1, 5000.0, 80.0 * (i + 1), key=f"dp_ic_{i}")
                margin = nopat / revenue * 100 if revenue > 0 else 0
                turnover = revenue / inv_cap if inv_cap > 0 else 0
                roic = nopat / inv_cap * 100 if inv_cap > 0 else 0
                results.append({"Entity": "Your Company" if i == 0 else f"Competitor {i}",
                               "NOPAT Margin": f"{margin:.1f}%", "Asset Turnover": f"{turnover:.2f}x",
                               "ROIC": f"{roic:.1f}%", "Strategy Type": "Margin-led" if margin > 15 else ("Turnover-led" if turnover > 2.5 else "Balanced")})
            st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

        else:  # Value Creation Bridge
            st.subheader("🌉 Value Creation Bridge Calculator")
            st.markdown("Calculate how strategic initiatives will move the ROIC-WACC spread:")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Current State:**")
                current_roic = st.number_input("Current ROIC (%):", 0.0, 50.0, 9.5, 0.5)
                wacc_v = st.number_input("WACC (%):", 4.0, 20.0, 9.0, 0.5)
                invested_capital_v = st.number_input("Invested Capital ($M):", 1.0, 5000.0, 200.0, 10.0)
            with col2:
                st.markdown("**Strategic Initiatives Impact:**")
                margin_uplift = st.number_input("Margin improvement from strategy (pp):", 0.0, 10.0, 2.0, 0.5)
                turnover_improvement = st.number_input("Asset turnover improvement (×):", 0.0, 1.0, 0.1, 0.05)
                wacc_reduction = st.number_input("WACC reduction from ESG/structure (pp):", 0.0, 3.0, 0.5, 0.1)

            current_spread = current_roic - wacc_v
            current_eva = current_spread / 100 * invested_capital_v
            new_roic = current_roic + margin_uplift + (turnover_improvement * current_roic * 0.5)
            new_wacc = wacc_v - wacc_reduction
            new_spread = new_roic - new_wacc
            new_eva = new_spread / 100 * invested_capital_v
            value_created = new_eva - current_eva

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Current**")
                st.metric("ROIC", f"{current_roic:.1f}%")
                st.metric("ROIC-WACC Spread", f"{current_spread:+.1f}pp")
                st.metric("Annual EVA", f"${current_eva:.1f}M")
            with col2:
                st.markdown("**Post-Strategy**")
                st.metric("New ROIC", f"{new_roic:.1f}%", f"{new_roic - current_roic:+.1f}pp")
                st.metric("New Spread", f"{new_spread:+.1f}pp", f"{new_spread - current_spread:+.1f}pp improvement")
                st.metric("New Annual EVA", f"${new_eva:.1f}M", f"${value_created:+.1f}M created")

    with tab4:
        st.header("Visualizations")

        st.subheader("DuPont ROIC Tree")
        fig_dt = go.Figure()
        nodes = ["ROIC", "NOPAT Margin", "Asset Turnover", "NOPAT", "Revenue (for margin)", "Revenue (for turnover)", "Invested Capital"]
        x = [0.5, 0.2, 0.8, 0.1, 0.3, 0.7, 0.9]
        y = [1.0, 0.6, 0.6, 0.2, 0.2, 0.2, 0.2]
        colors = ["#1B3A6B", "#0D7377", "#0D7377", "#D97706", "#D97706", "#D97706", "#D97706"]
        for node, xi, yi, c in zip(nodes, x, y, colors):
            fig_dt.add_trace(go.Scatter(x=[xi], y=[yi], mode="markers+text", text=[node],
                                       textposition="bottom center", marker=dict(size=40, color=c),
                                       textfont=dict(size=10, color="white" if c != "#D97706" else "#1B3A6B"),
                                       showlegend=False))
        connections = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
        for start, end in connections:
            fig_dt.add_shape(type="line", x0=x[start], y0=y[start], x1=x[end], y1=y[end], line=dict(color="#94A3B8", width=2))
        fig_dt.update_layout(title="DuPont ROIC Decomposition Tree", height=450,
                            xaxis=dict(visible=False, range=[-0.1, 1.1]), yaxis=dict(visible=False, range=[0, 1.3]))
        st.plotly_chart(fig_dt, use_container_width=True)

        st.subheader("Strategy → Financial Outcome: Cause and Effect Chain")
        stages = ["Build Digital Capabilities", "Improve Customer Experience", "Grow Market Share", "Improve Revenue Mix", "Higher EBITDA Margin", "Higher ROIC", "Shareholder Value Created"]
        values = [10, 30, 50, 65, 80, 90, 100]
        fig_chain = go.Figure(go.Funnel(y=stages, x=values, textinfo="label+value+percent previous",
                                       marker=dict(color=["#94A3B8", "#60A5FA", "#2563EB", "#0D7377", "#27AE60", "#D97706", "#1B3A6B"])))
        fig_chain.update_layout(title="Strategy Execution → Value Creation Chain", height=500)
        st.plotly_chart(fig_chain, use_container_width=True)

        st.subheader("FCF Trend — Strategic Health Signal")
        years_f = [2019, 2020, 2021, 2022, 2023]
        fcf_f = [57, 47, 54, 41, 15]
        roic_f = [14, 12, 15, 11, 8]
        fig_fcf = go.Figure()
        fig_fcf.add_trace(go.Bar(x=years_f, y=fcf_f, name="Free Cash Flow ($M)", marker_color=["#27AE60" if f > 40 else "#E74C3C" for f in fcf_f]))
        fig_fcf.add_trace(go.Scatter(x=years_f, y=roic_f, name="ROIC (%)", yaxis="y2", mode="lines+markers",
                                    line=dict(color="#1B3A6B", width=3), marker=dict(size=8)))
        fig_fcf.add_hline(y=9, line_dash="dash", line_color="#E74C3C", annotation_text="WACC 9%", yref="y2")
        fig_fcf.update_layout(title="FCF & ROIC Trend — Strategic Health Dashboard", height=420,
                              yaxis=dict(title="FCF ($M)"),
                              yaxis2=dict(title="ROIC (%)", overlaying="y", side="right", range=[0, 20]))
        st.plotly_chart(fig_fcf, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Economic Value Added (EVA) is calculated as:**")
        q1 = st.radio("", ["EBITDA − Depreciation", "(ROIC − WACC) × Invested Capital", "Net Income − Dividends", "Revenue − Operating Costs"], key="bs7q1")
        if st.button("Check Answer", key="bs7c1"):
            if q1 == "(ROIC − WACC) × Invested Capital":
                st.success("✅ Correct! EVA = (ROIC − WACC) × Invested Capital. It is the monetary measure of economic profit beyond the cost of capital.")
            else:
                st.error("❌ Incorrect. EVA = (ROIC − WACC) × Invested Capital. It measures economic profit after charging for the cost of capital.")

        st.markdown("---")
        st.markdown("**2. In DuPont analysis, a discount retailer typically achieves acceptable ROIC through:**")
        q2 = st.radio("", ["Very high profit margins", "High asset turnover (volume efficiency)", "Low cost of capital", "Premium pricing strategy"], key="bs7q2")
        if st.button("Check Answer", key="bs7c2"):
            if q2 == "High asset turnover (volume efficiency)":
                st.success("✅ Correct! Discount retailers like Walmart have thin margins but compensate with very high asset turns — selling a huge volume per $1 of invested capital.")
            else:
                st.error("❌ Incorrect. Discount retailers achieve ROIC via HIGH asset turnover — volume and efficiency, not premium margins.")

        st.markdown("---")
        st.markdown("**3. The Balanced Scorecard's 'Learning & Growth' perspective represents:**")
        q3 = st.radio("", [
            "The company's investment portfolio returns",
            "Staff bonuses and compensation schemes",
            "The foundation capabilities (talent, technology, culture) that power all other perspectives",
            "Revenue generated from knowledge-based products"
        ], key="bs7q3")
        if st.button("Check Answer", key="bs7c3"):
            if q3 == "The foundation capabilities (talent, technology, culture) that power all other perspectives":
                st.success("✅ Correct! Learning & Growth is the foundation — capabilities here enable better processes, which enable customer satisfaction, which drives financial results.")
            else:
                st.error("❌ Incorrect. L&G = foundational capabilities (people, tech, culture) that cause better processes → better customer outcomes → financial results.")

        st.markdown("---")
        st.markdown("**4. A 'fortress balance sheet' strategy (low debt) provides which strategic benefit?**")
        q4 = st.radio("", [
            "It minimises the WACC to the lowest possible level",
            "It maximises the tax shield from interest payments",
            "It provides strategic flexibility — ability to invest, acquire, or survive downturns",
            "It guarantees the highest ROIC in the industry"
        ], key="bs7q4")
        if st.button("Check Answer", key="bs7c4"):
            if q4 == "It provides strategic flexibility — ability to invest, acquire, or survive downturns":
                st.success("✅ Correct! Low debt = financial resilience and strategic optionality. The ability to invest counter-cyclically when rivals cannot is a major competitive advantage.")
            else:
                st.error("❌ Incorrect. Fortress balance sheet = strategic flexibility — ability to invest when peers cannot, survive downturns, and fund opportunistic M&A.")

        st.markdown("---")
        st.markdown("**5. Declining FCF combined with falling ROIC over 3+ years signals:**")
        q5 = st.radio("", [
            "A healthy growth investment phase",
            "Strong capital discipline",
            "Competitive moat erosion — strategy change required",
            "Successful digital transformation in progress"
        ], key="bs7q5")
        if st.button("Check Answer", key="bs7c5"):
            if q5 == "Competitive moat erosion — strategy change required":
                st.success("✅ Correct! Declining FCF + declining ROIC = the competitive position is weakening. Strategic intervention is urgently needed.")
            else:
                st.error("❌ Incorrect. Declining FCF AND declining ROIC together signal moat erosion — the strategy needs urgent review and change.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Value Creation Framework
        ```
        Four value drivers:
        1. Revenue Growth  →  Top-line strategy
        2. Margin Improvement  →  Pricing + cost strategy
        3. Capital Efficiency  →  Asset management strategy
        4. WACC Reduction  →  Capital structure + risk strategy

        EVA = (ROIC − WACC) × Invested Capital
        ```

        ### 2. Balanced Scorecard
        | Perspective | Role | Finance KPIs |
        |-------------|------|-------------|
        | Financial | Outcome | ROIC, FCF, Revenue growth |
        | Customer | Enabler | NPS, Retention, Market share |
        | Internal Process | Engine | Cost efficiency, Quality, Cycle time |
        | Learning & Growth | Foundation | Talent, Tech capability, Engagement |

        ### 3. DuPont ROIC Analysis
        ```
        ROIC = NOPAT Margin × Asset Turnover
        Margin-led ROIC → Differentiation strategy
        Turnover-led ROIC → Cost leadership / efficiency strategy
        ```

        ### 4. FCF Strategic Signals
        ```
        Growing FCF + Rising ROIC  →  ✅ Invest and grow
        Flat FCF + Stable ROIC    →  ⚠️  Defend and optimise
        Falling FCF + Falling ROIC →  🔴 Urgent strategic review
        ```
        """)
        st.subheader("📌 Key Formulas")
        st.code("EVA = (ROIC − WACC) × Invested Capital")
        st.code("ROIC = NOPAT Margin × Asset Turnover = (NOPAT/Revenue) × (Revenue/Invested Capital)")
        st.code("FCF = NOPAT − Net Reinvestment (Capex + ΔNWC − Depreciation)")
        st.code("WACC = (E/V × Re) + (D/V × Rd × (1−T))")
        st.success("🎓 **Module 7 Complete!** You can now link every strategic decision to its financial value impact using EVA, DuPont, Balanced Scorecard, and FCF analysis.")
        st.info("💡 **Next**: Module 8 — Strategic Planning, Implementation & Change Management")

if __name__ == "__main__":
    show()