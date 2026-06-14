import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💰 Module 11: Strategic Finance — FP&A, Scenario Modelling & Business Cases")
    st.markdown("*Build driver-based financial models, design rolling forecasts, and develop boardroom-ready business cases*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Strategic FP&A — Beyond Budgeting")
        st.markdown("""
        Traditional FP&A focuses on **reporting variance against budget**. Strategic FP&A focuses on
        **forward-looking insight that drives better decisions**.

        | Traditional FP&A | Strategic FP&A |
        |-----------------|---------------|
        | Budget vs actual variance | Driver-based rolling forecasts |
        | Annual cycle | Continuous insight |
        | Backward-looking | Forward-looking |
        | Cost focus | Value creation focus |
        | Reports to finance | Partners with business |
        | Answers "What happened?" | Answers "What should we do?" |

        **The Finance Business Partner** is the bridge between strategic intent and financial reality —
        translating ambiguous commercial situations into clear financial models that support decisions.
        """)

        st.subheader("2. Driver-Based Financial Modelling")
        st.markdown("""
        A **driver-based model** links financial outputs (revenue, costs, cash flow) directly to the
        **operational and commercial drivers** that management can actually influence.

        **Driver hierarchy example — SaaS business:**
        ```
        Strategic Drivers → Operational Drivers → Financial Outputs

        Market growth rate   → New logo additions      → New ARR ($)
        Sales team size      → Pipeline coverage       → Bookings ($)
        Win rate %          → Deals won               → ↑
        Product adoption    → Expansion/upsell rate   → Expansion ARR ($)
        Customer success    → Gross retention %       → Churned ARR ($)
                                                       ────────────────
                                                       NET ARR ($)
                                                       × Gross Margin %
                                                       = Gross Profit ($)
                                                       − Operating Costs
                                                       = EBITDA ($)
        ```

        **Finance use**: Change one driver assumption → model automatically updates all financial outputs.
        This creates a **living model** that supports real-time strategic decisions.
        """)

        st.subheader("3. Investment Appraisal — NPV, IRR, Payback, MIRR")
        appraisal_data = {
            "Method": ["Net Present Value (NPV)", "Internal Rate of Return (IRR)", "Payback Period", "Modified IRR (MIRR)"],
            "Definition": [
                "PV of future cash flows minus initial investment",
                "Discount rate at which NPV = 0",
                "Time to recover the initial investment",
                "IRR assuming reinvestment at WACC, not IRR itself"
            ],
            "Decision Rule": [
                "Accept if NPV > 0; choose highest NPV if mutually exclusive",
                "Accept if IRR > WACC; higher is better",
                "Accept if payback < company's target (e.g. 3 years)",
                "Accept if MIRR > WACC; more realistic than IRR"
            ],
            "Key Limitation": [
                "Assumes reinvestment at WACC; sensitive to terminal value",
                "Multiple IRRs possible; assumes reinvestment at IRR (often too high)",
                "Ignores cash flows after payback; ignores time value of money",
                "Still requires estimated reinvestment rate"
            ],
            "Best Used For": [
                "All major investment decisions — the primary method",
                "Ranking projects; communicating returns to non-finance executives",
                "Quick filter; liquidity-constrained businesses",
                "When IRR inflates returns due to aggressive reinvestment assumption"
            ]
        }
        st.dataframe(pd.DataFrame(appraisal_data), use_container_width=True, hide_index=True)

        st.subheader("4. The Anatomy of a Business Case")
        st.markdown("""
        A **business case** is the structured financial and strategic justification for a significant investment decision.

        **Nine components of a compelling business case:**
        1. **Executive Summary** — One-page: what, why, how much, key risk, recommendation
        2. **Strategic Context** — How does this support the strategic plan?
        3. **Options Appraisal** — At least 3 options including "do nothing"
        4. **Financial Modelling** — NPV, IRR, payback for preferred option and alternatives
        5. **Assumptions & Sensitivities** — Transparent; tornado chart for key drivers
        6. **Benefit Realisation Plan** — How and when benefits are measured and tracked
        7. **Risk Assessment** — Top 5 risks, likelihood, impact, mitigation
        8. **Funding & Capital Requirements** — Timing, source, covenant impact
        9. **Recommendation & Governance** — Clear ask; decision authority; next steps

        **Finance professional's role**: Own the financial model, challenge the assumptions, and present the
        numbers with complete intellectual honesty — including the downside scenarios.
        """)

        st.subheader("5. Strategic Management Reporting")
        st.markdown("""
        Strategic management reporting converts data into **decisions**. The best boards and ExCos don't read reports —
        they make decisions from them.

        **Design principles for strategic reports:**
        - **Exception-based**: Highlight what matters, not everything
        - **Forward-looking**: Lead with forecast, then actuals
        - **Insight, not data**: "Why did this happen? What does it mean? What should we do?"
        - **Right audience**: Board sees strategy; ExCo sees management; Operations sees execution
        - **Visual first**: Charts, RAG indicators, trends over tables of numbers
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Driver-Based Revenue Model — Retail Business")
        st.markdown("**Model architecture: Revenue built from operational drivers**")
        driver_model = pd.DataFrame({
            "Driver": ["Total Store Count", "New Store Openings (pa)", "Store Closures (pa)", "Average Revenue per Store ($K)", "Same-Store Sales Growth (%)", "Online Revenue ($M)", "Online Growth (%)", "Total Revenue ($M)"],
            "Year 1": [245, 15, 5, 1850, "3.5%", 42, "25%", ""],
            "Year 2": [255, 12, 2, 1918, "3.5%", 53, "25%", ""],
            "Year 3": [265, 12, 2, 1985, "3.5%", 66, "25%", ""]
        })
        for col in ["Year 1", "Year 2", "Year 3"]:
            driver_model.loc[driver_model["Driver"] == "Total Revenue ($M)", col] = \
                f"${int(driver_model[driver_model['Driver']=='Total Store Count'][col].values[0]) * 1850 / 1000 + float(driver_model[driver_model['Driver']=='Online Revenue ($M)'][col].values[0]):.0f}M"
        st.dataframe(driver_model, use_container_width=True, hide_index=True)
        st.info("💡 **Power of driver-based models**: If the CFO wants to test 'What if we open 20 stores instead of 15?' — one input change cascades automatically through the entire P&L, balance sheet, and cash flow. No manual re-calculation needed.")

        st.subheader("Example 2: Full Business Case — ERP System Replacement")
        bc_data = {
            "Item": ["Strategic Context", "Option 1: Do Nothing", "Option 2: Upgrade Existing", "Option 3 (Preferred): New Cloud ERP",
                     "NPV (10yr @ 8%)", "IRR", "Payback Period", "Key Risk", "Recommendation"],
            "Detail": [
                "Current ERP is 12 years old; no vendor support from 2025; unable to support new digital strategy",
                "NPV: -$8.5M (cost of legacy, risk, inefficiency). Not viable.",
                "NPV: +$2.1M; IRR: 11%; Payback: 4.8yrs. Maintains status quo risk.",
                "Investment: $4.2M capex + $0.8M/yr OpEx. Benefits: $2.1M/yr cost savings + $0.9M/yr business decisions improvement.",
                "+$12.4M (vs do nothing baseline)",
                "24% — well above WACC of 9%",
                "2.8 years",
                "Implementation disruption — mitigated by phased rollout and parallel run",
                "Proceed with Cloud ERP (Option 3). Board approval for $4.2M capex requested."
            ]
        }
        st.dataframe(pd.DataFrame(bc_data), use_container_width=True, hide_index=True)

        st.subheader("Example 3: Three-Statement Financial Model Linkages")
        st.markdown("""
        **Every strategic initiative flows through the three financial statements:**

        | Driver Change | P&L Impact | Balance Sheet Impact | Cash Flow Impact |
        |--------------|-----------|--------------------|-----------------:|
        | +5% revenue increase | +$5M gross profit | +$1M trade receivables | +$4.2M operating CF |
        | Acquire competitor ($50M deal) | +$8M EBIT (synergies Year 3) | +$50M goodwill; -$50M cash | -$50M investing CF |
        | New capex programme ($20M) | +$2M depreciation | +$20M fixed assets; -$20M cash | -$20M investing CF |
        | Working capital improvement | No P&L impact | -$8M debtors/inventory | +$8M operating CF |
        | Issue new debt ($30M) | +$1.2M interest cost | +$30M cash; +$30M debt | +$30M financing CF |
        """)

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "Investment Appraisal Calculator (NPV / IRR / Payback)",
            "Driver-Based Revenue Model",
            "Business Case Builder"
        ])

        if tool == "Investment Appraisal Calculator (NPV / IRR / Payback)":
            st.subheader("📐 Investment Appraisal Calculator")
            col1, col2 = st.columns(2)
            with col1:
                initial_invest = st.number_input("Initial Investment ($M):", 0.1, 500.0, 10.0, 0.5)
                wacc_ia = st.slider("WACC / Discount Rate (%):", 4.0, 25.0, 9.0, 0.5)
                project_life = st.slider("Project Life (years):", 1, 15, 7)
            with col2:
                terminal_growth = st.slider("Terminal Growth Rate (%):", 0.0, 5.0, 2.0, 0.5)
                tax_rate_ia = st.slider("Tax Rate (%):", 0.0, 40.0, 25.0, 0.5)

            st.markdown("**Annual Free Cash Flows ($M):**")
            cash_flows = []
            cols = st.columns(min(project_life, 7))
            for i in range(project_life):
                with cols[i % 7]:
                    default_cf = 1.5 + i * 0.3
                    cf = st.number_input(f"Yr {i+1}", value=round(default_cf, 1), key=f"ia_cf_{i}", step=0.5)
                    cash_flows.append(cf)

            terminal_value = cash_flows[-1] * (1 + terminal_growth / 100) / ((wacc_ia - terminal_growth) / 100) if wacc_ia > terminal_growth else 0
            pv_flows = [cf / (1 + wacc_ia / 100) ** (i + 1) for i, cf in enumerate(cash_flows)]
            pv_terminal = terminal_value / (1 + wacc_ia / 100) ** project_life
            npv_ia = sum(pv_flows) + pv_terminal - initial_invest

            cumulative = -initial_invest
            payback_year = None
            for i, cf in enumerate(cash_flows):
                cumulative += cf
                if cumulative >= 0 and payback_year is None:
                    payback_year = i + 1 - (cumulative - cf) / cf if cf > 0 else i + 1

            def calc_irr(cfs, initial):
                flows = [-initial] + cfs
                low, high = -0.99, 10.0
                for _ in range(1000):
                    mid = (low + high) / 2
                    npv_test = sum([f / (1 + mid) ** t for t, f in enumerate(flows)])
                    if npv_test > 0: low = mid
                    else: high = mid
                return mid * 100

            irr_val = calc_irr(cash_flows, initial_invest)

            col1, col2, col3, col4 = st.columns(4)
            with col1: st.metric("NPV", f"${npv_ia:.2f}M", "✅ Accept" if npv_ia > 0 else "❌ Reject")
            with col2: st.metric("IRR", f"{irr_val:.1f}%", f"{irr_val - wacc_ia:+.1f}pp vs WACC")
            with col3: st.metric("Payback", f"{payback_year:.1f} yrs" if payback_year else ">project life")
            with col4: st.metric("Terminal Value (PV)", f"${pv_terminal:.1f}M", f"{pv_terminal/(npv_ia+initial_invest)*100:.0f}% of total value")

            if npv_ia > 0 and irr_val > wacc_ia:
                st.success(f"✅ **Invest**: NPV ${npv_ia:.2f}M positive; IRR {irr_val:.1f}% exceeds WACC {wacc_ia:.1f}%. Value-creating investment.")
            elif npv_ia > 0 and irr_val <= wacc_ia:
                st.warning("⚠️ Mixed signals — check discount rate and cash flow assumptions.")
            else:
                st.error(f"❌ **Reject**: NPV ${npv_ia:.2f}M negative. Investment destroys value at this cost of capital.")

        elif tool == "Driver-Based Revenue Model":
            st.subheader("📈 Driver-Based Revenue Model Builder")
            st.markdown("Build a 3-year revenue model from operational drivers:")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Volume Drivers:**")
                base_customers = st.number_input("Current Active Customers:", 100, 100000, 5000, 100)
                new_cust_growth = st.slider("New Customer Growth Rate (% pa):", -10.0, 50.0, 15.0, 1.0)
                churn_rate = st.slider("Annual Customer Churn Rate (%):", 0.0, 50.0, 12.0, 0.5)
            with col2:
                st.markdown("**Value Drivers:**")
                avg_rev_per_cust = st.number_input("Avg Annual Revenue per Customer ($):", 100.0, 100000.0, 2500.0, 100.0)
                price_increase = st.slider("Annual Price Increase (%):", -5.0, 20.0, 3.0, 0.5)
                upsell_rate = st.slider("Annual Upsell/Expansion Rate (%):", 0.0, 30.0, 8.0, 0.5)

            results_db = []
            customers = base_customers
            arpc = avg_rev_per_cust
            for yr in range(1, 4):
                new_customers = customers * (new_cust_growth / 100)
                churned = customers * (churn_rate / 100)
                customers = customers + new_customers - churned
                arpc = arpc * (1 + price_increase / 100) * (1 + upsell_rate / 100)
                revenue = customers * arpc / 1000000
                results_db.append({"Year": f"Year {yr}", "Active Customers": f"{int(customers):,}",
                                   "Avg Revenue/Customer ($)": f"${arpc:,.0f}", "Total Revenue ($M)": f"${revenue:.2f}M",
                                   "YoY Growth": f"{(new_cust_growth - churn_rate + price_increase + upsell_rate):.1f}%"})
            st.dataframe(pd.DataFrame(results_db), use_container_width=True, hide_index=True)
            final_rev = float(results_db[-1]["Total Revenue ($M)"].replace("$","").replace("M",""))
            base_rev = base_customers * avg_rev_per_cust / 1000000
            st.metric("Revenue CAGR (3yr)", f"{((final_rev/base_rev)**(1/3)-1)*100:.1f}%")

        else:  # Business Case Builder
            st.subheader("📋 Business Case Builder")
            st.markdown("Complete each section to build a structured business case:")
            proj_name = st.text_input("Project / Initiative Name:", value="Strategic Initiative Name")
            strategic_link = st.text_area("Strategic Context (how does this support the strategy?):", value="Link to Module 2 external analysis / Module 3 capability gap / Module 5 growth strategy...", height=60)

            col1, col2, col3 = st.columns(3)
            with col1:
                total_invest = st.number_input("Total Investment Required ($M):", 0.1, 500.0, 5.0, 0.5)
                invest_yr1 = st.number_input("Year 1 investment ($M):", 0.1, 500.0, 3.0, 0.5)
            with col2:
                annual_benefit = st.number_input("Annual recurring benefit ($M):", 0.0, 100.0, 2.0, 0.5)
                benefit_start_yr = st.slider("Benefits start (Year):", 1, 5, 2)
            with col3:
                wacc_bc = st.slider("Discount Rate (%):", 5.0, 20.0, 9.0, 0.5)
                project_years_bc = st.slider("Analysis period (years):", 3, 15, 7)

            top_risk = st.text_input("Top Risk:", value="Implementation delay / cost overrun")
            mitigation = st.text_input("Risk Mitigation:", value="Phased delivery; contingency 15%")

            invest_flows = [-invest_yr1] + [-((total_invest - invest_yr1) / (project_years_bc - 1)) if yr > 0 and yr <= benefit_start_yr - 1 else annual_benefit for yr in range(1, project_years_bc)]
            npv_bc = sum([cf / (1 + wacc_bc / 100) ** t for t, cf in enumerate(invest_flows)])
            cumul = 0
            pb_bc = None
            for i, cf in enumerate(invest_flows):
                cumul += cf
                if cumul >= 0 and pb_bc is None:
                    pb_bc = i

            if st.button("📄 Generate Business Case Summary"):
                st.markdown(f"""
                ---
                ## 📄 Business Case: {proj_name}

                **Strategic Context**: {strategic_link}

                | Item | Value |
                |------|-------|
                | Total Investment | ${total_invest:.1f}M |
                | Annual Benefit (from Year {benefit_start_yr}) | ${annual_benefit:.1f}M/yr |
                | NPV @ {wacc_bc}% | ${npv_bc:.2f}M |
                | Payback Period | {pb_bc} years |
                | Top Risk | {top_risk} |
                | Mitigation | {mitigation} |

                **Recommendation**: {'✅ **INVEST** — NPV positive; proceed subject to governance approval.' if npv_bc > 0 else '❌ **DO NOT INVEST** — NPV negative. Reassess scope, phasing, or benefit assumptions.'}
                """)

    with tab4:
        st.header("Visualizations")

        st.subheader("NPV Sensitivity — Tornado Chart")
        assumptions = ["Revenue Growth (±5%)", "Gross Margin (±3pp)", "WACC (±2pp)", "Capex (±15%)", "Working Capital (±10%)", "Terminal Growth (±1pp)"]
        upside_npv = [8.5, 5.2, 4.8, 2.1, 1.8, 3.5]
        downside_npv = [-9.2, -5.8, -5.5, -1.8, -1.5, -2.8]
        sorted_idx = sorted(range(len(upside_npv)), key=lambda i: upside_npv[i] - downside_npv[i], reverse=True)
        assumptions_s = [assumptions[i] for i in sorted_idx]
        upside_s = [upside_npv[i] for i in sorted_idx]
        downside_s = [downside_npv[i] for i in sorted_idx]
        fig_tornado = go.Figure()
        fig_tornado.add_trace(go.Bar(y=assumptions_s, x=upside_s, orientation="h", name="Upside", marker_color="#27AE60"))
        fig_tornado.add_trace(go.Bar(y=assumptions_s, x=downside_s, orientation="h", name="Downside", marker_color="#E74C3C"))
        fig_tornado.add_vline(x=0, line_color="black", line_width=2)
        fig_tornado.update_layout(title="NPV Sensitivity — Key Assumption Drivers", barmode="overlay",
                                  xaxis_title="NPV Swing ($M)", height=400)
        st.plotly_chart(fig_tornado, use_container_width=True)

        st.subheader("Investment Appraisal — Cumulative Cash Flow")
        years_ia = list(range(0, 8))
        cash_flows_ia = [-10, 1.2, 1.8, 2.5, 3.0, 3.5, 4.0, 4.5]
        cumulative_cf = [sum(cash_flows_ia[:i+1]) for i in range(len(cash_flows_ia))]
        fig_cf = go.Figure()
        fig_cf.add_trace(go.Bar(x=years_ia, y=cash_flows_ia, name="Annual Cash Flow ($M)", marker_color=["#E74C3C" if c < 0 else "#27AE60" for c in cash_flows_ia]))
        fig_cf.add_trace(go.Scatter(x=years_ia, y=cumulative_cf, name="Cumulative CF ($M)", mode="lines+markers",
                                    line=dict(color="#1B3A6B", width=3), marker=dict(size=8)))
        fig_cf.add_hline(y=0, line_color="black", line_width=2, line_dash="dash")
        payback_x = next((i for i, c in enumerate(cumulative_cf) if c >= 0), None)
        if payback_x:
            fig_cf.add_vline(x=payback_x, line_dash="dot", line_color="#D97706", annotation_text=f"Payback Yr {payback_x}")
        fig_cf.update_layout(title="Cash Flow Profile — Annual & Cumulative", yaxis_title="$M", height=400)
        st.plotly_chart(fig_cf, use_container_width=True)

        st.subheader("Driver-Based Model — Revenue Build")
        categories = ["Opening Customers", "New Customers", "Churned Customers", "Net Customers", "Price/Mix Uplift", "Total Revenue Yr 3"]
        values = [5000, 2600, -1800, 5800, 0, 0]
        measure = ["absolute", "relative", "relative", "total", "relative", "total"]
        fig_wf = go.Figure(go.Waterfall(
            name="Revenue Bridge", orientation="v",
            measure=["absolute", "relative", "relative", "total", "relative", "total"],
            x=["Base Customers", "New Customers", "Churned", "Net Volume", "Price/ARPC Uplift", "Total Revenue"],
            y=[5000, 2600, -1800, 0, 850, 0],
            text=["+5,000", "+2,600", "-1,800", "=5,800", "+850", "~$29M"],
            connector=dict(line=dict(color="#CBD5E1")),
            increasing=dict(marker=dict(color="#27AE60")),
            decreasing=dict(marker=dict(color="#E74C3C")),
            totals=dict(marker=dict(color="#1B3A6B"))
        ))
        fig_wf.update_layout(title="Driver-Based Revenue Bridge — Year 3 Build", height=400)
        st.plotly_chart(fig_wf, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. NPV should be used as the PRIMARY investment appraisal method because:**")
        q1 = st.radio("", [
            "It is the easiest to calculate",
            "It directly measures wealth created in dollar terms, accounting for time value of money",
            "It always gives the same answer as IRR",
            "It does not require a discount rate"
        ], key="bs11q1")
        if st.button("Check Answer", key="bs11c1"):
            if q1 == "It directly measures wealth created in dollar terms, accounting for time value of money":
                st.success("✅ Correct! NPV directly quantifies value created (in $) after accounting for the time value of money and the cost of capital.")
            else:
                st.error("❌ Incorrect. NPV is preferred because it measures actual dollar value created, properly accounts for time value and risk through WACC.")

        st.markdown("---")
        st.markdown("**2. A driver-based financial model links revenue to:**")
        q2 = st.radio("", [
            "Last year's actual figures plus an inflation factor",
            "The CFO's top-down revenue target",
            "Underlying operational and commercial drivers that management can influence",
            "The average of the last three years"
        ], key="bs11q2")
        if st.button("Check Answer", key="bs11c2"):
            if q2 == "Underlying operational and commercial drivers that management can influence":
                st.success("✅ Correct! Driver-based models build financial outputs from operational drivers (e.g. customer count, win rate, price) — enabling scenario analysis and decision support.")
            else:
                st.error("❌ Incorrect. Driver-based models derive financial outputs from operational drivers — making assumptions explicit and enabling scenario analysis.")

        st.markdown("---")
        st.markdown("**3. IRR should NOT be used as the sole investment criterion because:**")
        q3 = st.radio("", [
            "It is too difficult to explain to the board",
            "It assumes reinvestment of cash flows at the IRR rate, which is often unrealistically high",
            "It always gives a lower result than NPV",
            "It cannot be used for projects with negative cash flows"
        ], key="bs11q3")
        if st.button("Check Answer", key="bs11c3"):
            if q3 == "It assumes reinvestment of cash flows at the IRR rate, which is often unrealistically high":
                st.success("✅ Correct! IRR assumes all intermediate cash flows are reinvested at the IRR — which for high-return projects is unrealistic. MIRR corrects this using WACC.")
            else:
                st.error("❌ Incorrect. IRR's key flaw is assuming reinvestment at the IRR rate — often far above the actual reinvestment rate (WACC). Use MIRR or NPV.")

        st.markdown("---")
        st.markdown("**4. A business case must always include which of the following?**")
        q4 = st.radio("", [
            "Only the preferred option",
            "A 'do nothing' option for comparison",
            "A minimum of 10 financial scenarios",
            "External consultant sign-off"
        ], key="bs11q4")
        if st.button("Check Answer", key="bs11c4"):
            if q4 == "A 'do nothing' option for comparison":
                st.success("✅ Correct! Every business case must include a 'do nothing' baseline — it defines the cost of inaction and sets the NPV comparison benchmark.")
            else:
                st.error("❌ Incorrect. A proper options appraisal must include at least a 'do nothing' option — otherwise you cannot assess the incremental value of investing.")

        st.markdown("---")
        st.markdown("**5. A rolling forecast differs from a traditional budget primarily because:**")
        q5 = st.radio("", [
            "It is prepared by the operations team, not finance",
            "It always covers exactly 12 months and is updated monthly, maintaining a constant forward horizon",
            "It focuses only on capital expenditure",
            "It is submitted to external auditors"
        ], key="bs11q5")
        if st.button("Check Answer", key="bs11c5"):
            if q5 == "It always covers exactly 12 months and is updated monthly, maintaining a constant forward horizon":
                st.success("✅ Correct! Rolling forecasts always look the same distance forward — they provide a consistent, continuously-updated forward view.")
            else:
                st.error("❌ Incorrect. Rolling forecasts maintain a constant forward horizon (e.g. 12 months), updated regularly — unlike an annual budget that becomes stale after Q1.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Strategic FP&A — The Shift
        ```
        Traditional FP&A:  Variance analysis → "What happened?"
        Strategic FP&A:    Driver-based forecasting → "What should we do?"
        ```

        ### 2. Driver-Based Modelling
        ```
        Strategic Drivers → Operational Drivers → Financial Outputs
        (Market growth)  → (New customers)    → (Revenue $)
                         → (Win rate %)       →
                         → (Churn %)          →
                         → (Price/ARPC)       →
        ```

        ### 3. Investment Appraisal
        | Method | Rule | Use For |
        |--------|------|---------|
        | NPV | Accept if > 0 | Primary method — all investments |
        | IRR | Accept if > WACC | Ranking and communication |
        | Payback | Accept if < target | Quick filter; liquidity check |
        | MIRR | Accept if > WACC | When IRR overstates returns |

        ### 4. Business Case — Nine Components
        1. Executive Summary | 2. Strategic Context | 3. Options Appraisal
        4. Financial Model | 5. Assumptions & Sensitivities | 6. Benefits Realisation
        7. Risk Assessment | 8. Funding & Governance | 9. Recommendation

        ### 5. Strategic Reporting Principles
        - Exception-based | Forward-looking | Insight not data
        - Right audience | Visual first
        """)
        st.subheader("📌 Key Formulas")
        st.code("NPV = Σ [CFt / (1+r)^t] − Initial Investment")
        st.code("IRR = discount rate where NPV = 0")
        st.code("Payback = Initial Investment / Annual Cash Flow (simple)")
        st.code("MIRR = (FV of positive CFs at WACC / PV of costs)^(1/n) − 1")
        st.success("🎓 **Module 11 Complete!** You can now build driver-based financial models, develop investment business cases, and design strategic management reporting.")
        st.info("💡 **Next**: Module 12 — Capstone: Integrated Business Strategy Project")

if __name__ == "__main__":
    show()