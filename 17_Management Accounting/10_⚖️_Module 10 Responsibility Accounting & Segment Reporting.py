import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏢 Module 10: Responsibility Accounting & Segment Reporting")
    st.markdown("*Evaluate performance across decentralized business units using ROI, RI, and EVA*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Decentralization")
        st.markdown("""
        **Decentralization** means delegating decision-making authority to lower-level managers who are closest to customers, suppliers, and operations.

        | Advantages | Disadvantages |
        |-----------|---------------|
        | Faster decisions — managers act without waiting | Risk of sub-optimal decisions (local vs company) |
        | Better use of local knowledge | Possible duplication of effort |
        | Develops future managers | Requires sophisticated control systems |
        | Frees top management for strategy | May lose economies of scale |
        | Higher motivation for local managers | Coordination challenges between units |
        """)

        st.subheader("2. Responsibility Centers — Four Types")
        centers_df = pd.DataFrame({
            "Center Type": ["Cost Center", "Revenue Center", "Profit Center", "Investment Center"],
            "Manager Controls": ["Costs only", "Revenues only", "Both revenues and costs", "Revenues, costs, AND assets"],
            "Primary Measure": ["Cost variances vs budget", "Revenue vs target", "Segment / divisional profit", "ROI, Residual Income, EVA"],
            "Examples": [
                "Production dept, IT dept, HR dept",
                "Sales territory, sales region",
                "Product division, geographic division",
                "Subsidiary, major business unit"
            ]
        })
        st.dataframe(centers_df, use_container_width=True, hide_index=True)

        st.subheader("3. Segment Reporting — Contribution Approach")
        st.markdown("""
        **Traceable vs Common Fixed Costs — the critical distinction:**
        - **Traceable Fixed Costs**: Would disappear if the segment were eliminated. Directly caused by the segment.
        - **Common Fixed Costs**: Shared corporate costs that continue even if the segment is dropped. Should NOT be allocated to segments for performance evaluation.

        ```
        Sales Revenue
        − Variable Costs (variable COGS + variable S&A)
        ─────────────────────────────────────────────────
        Contribution Margin
        − Traceable Fixed Costs  (caused by this segment)
        ─────────────────────────────────────────────────
        Segment Margin             ← KEY PERFORMANCE METRIC
        − Common Fixed Costs       (NOT allocated to segments)
        ─────────────────────────────────────────────────
        Company Net Operating Income
        ```

        **Segment Margin** = the best measure of a segment's long-run profitability.
        A segment should be kept if its Segment Margin is positive (it covers its traceable costs).
        """)

        st.subheader("4. Return on Investment (ROI)")
        st.markdown("""
        **ROI** measures how effectively a division uses its assets to generate profit.

        ```
        ROI = Net Operating Income / Average Operating Assets

        ──── DUPONT DECOMPOSITION ────
        ROI = Margin × Asset Turnover

        Margin         = Net Operating Income / Sales
        Asset Turnover = Sales / Average Operating Assets

        ──── INTERPRETATION ────
        ROI = 15% means: for every $1 of assets, the division earns $0.15 of operating income
        ```

        **Improving ROI:**
        - Increase margin: raise prices, reduce costs
        - Increase turnover: reduce assets (reduce inventory, collect receivables faster)
        - Combination of both
        """)

        st.subheader("5. Residual Income (RI)")
        st.markdown("""
        **Residual Income** = Net Operating Income above a minimum required return.

        ```
        RI = Net Operating Income − (Required Return % × Average Operating Assets)

        RI > 0 → Division is creating value ABOVE the minimum required return ✅
        RI < 0 → Division is destroying value ❌
        RI = 0 → Division is meeting exactly the minimum return
        ```

        **Why RI is better than ROI:**
        ROI can lead managers to REJECT profitable projects that would dilute their current high ROI
        but would ADD to RI. RI always encourages accepting projects above the required rate!
        """)

        st.subheader("6. Economic Value Added (EVA)")
        st.markdown("""
        EVA is a sophisticated form of residual income used by large corporations.

        ```
        EVA = After-Tax Net Operating Profit − (WACC × Total Capital Employed)

        WACC = Weighted Average Cost of Capital
        ```

        **EVA Adjustments (common):**
        - R&D expensed → capitalized
        - Operating leases → capitalized
        - LIFO reserve added back
        - Goodwill amortization reversed

        Positive EVA = Shareholder wealth created. Negative EVA = Shareholder wealth destroyed.
        """)

        st.subheader("7. Transfer Pricing")
        st.markdown("""
        **Transfer Price**: The price one division charges another division for internally transferred goods/services.

        | Method | Formula | When to Use |
        |--------|---------|------------|
        | **Market Price** | Current external market price | Competitive external market exists |
        | **Variable Cost** | Variable cost of producing unit | Excess capacity exists |
        | **Full Cost** | Total unit cost (variable + fixed) | Common but has limitations |
        | **Cost-Plus** | Full cost + markup | Internal pricing with profit element |
        | **Negotiated** | Agreed between divisions | No clear external price |

        ```
        Transfer Price Range:
        Minimum TP = Selling Division's Variable Cost + Opportunity Cost
        Maximum TP = Buying Division's External Market Price

        Any price within this range benefits both divisions and the company!
        ```
        """)

        st.subheader("8. Balanced Scorecard")
        st.markdown("""
        Translates strategy into operational measures across four perspectives:

        | Perspective | Key Question | Examples |
        |------------|-------------|---------|
        | **Financial** | How do shareholders see us? | ROI, EVA, revenue growth, cost reduction |
        | **Customer** | How do customers see us? | Satisfaction, retention, market share |
        | **Internal Process** | What must we excel at? | Quality, cycle time, on-time delivery |
        | **Learning & Growth** | Can we continue to improve? | Employee training, innovation, IT capability |
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Segment Income Statement")
        st.markdown("""
        **Company X — Three Product Lines:**

        |  | Total | Product A | Product B | Product C |
        |--|-------|-----------|-----------|-----------|
        | Sales | $900,000 | $400,000 | $350,000 | $150,000 |
        | Variable Costs | $520,000 | $220,000 | $200,000 | $100,000 |
        | **Contribution Margin** | **$380,000** | **$180,000** | **$150,000** | **$50,000** |
        | Traceable Fixed Costs | $200,000 | $80,000 | $90,000 | $30,000 |
        | **Segment Margin** | **$180,000** | **$100,000** | **$60,000** | **$20,000** |
        | Common Fixed Costs | $120,000 | | | |
        | **Net Operating Income** | **$60,000** | | | |

        **Analysis:**
        - All three products have positive Segment Margins → keep all three
        - CM Ratios: A = 45%, B = 42.9%, C = 33.3% → Product A most efficient
        - Segment Margin %: A = 25%, B = 17.1%, C = 13.3% → Product A most profitable

        ⚠️ **Do NOT drop Product C just because it looks unprofitable on a full-cost basis!**
        Its Segment Margin of $20,000 covers its traceable costs — dropping it loses $20,000 of contribution.
        """)

        st.subheader("Example 2: ROI, RI and EVA Calculation")
        st.markdown("""
        **Division Data:**
        | Item | Amount |
        |------|--------|
        | Sales | $2,000,000 |
        | Net Operating Income | $300,000 |
        | Average Operating Assets | $1,500,000 |
        | Required Rate of Return | 15% |
        | WACC | 12% |
        | After-Tax NOI | $225,000 |

        **ROI:**
        ```
        ROI = $300,000 / $1,500,000 = 20%

        DuPont breakdown:
        Margin = $300,000 / $2,000,000 = 15%
        Turnover = $2,000,000 / $1,500,000 = 1.333×
        ROI = 15% × 1.333 = 20% ✓
        ```

        **Residual Income:**
        ```
        RI = $300,000 − (15% × $1,500,000)
           = $300,000 − $225,000
           = $75,000 ✅ Positive — creating value!
        ```

        **EVA:**
        ```
        EVA = $225,000 − (12% × $1,500,000)
            = $225,000 − $180,000
            = $45,000 ✅ Shareholder value created!
        ```
        """)

        st.subheader("Example 3: Transfer Pricing — Should Division Transfer?")
        st.markdown("""
        **Division A** produces a component and **Division B** wants to buy it.
        - Division A variable cost: $30/unit, full cost: $45/unit, market price: $55/unit
        - Division A currently operating at **full capacity**
        - Division B can buy externally at **$52/unit**

        ```
        Minimum TP for Division A:
        = Variable Cost + Opportunity Cost (lost external margin)
        = $30 + ($55 − $30)   [must give up external sale]
        = $30 + $25 = $55

        Maximum TP for Division B:
        = External purchase price = $52

        Since Min TP ($55) > Max TP ($52) → No transfer should occur!
        Division B should buy externally at $52.
        ```

        **BUT if Division A has excess capacity:**
        ```
        Minimum TP = $30 + $0 (no opportunity cost) = $30
        Maximum TP = $52

        Any price $30–$52 benefits BOTH divisions!
        Optimal for company: transfer at any price in this range.
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Calculator:", [
            "📊 Segment Income Statement",
            "📈 ROI DuPont Analysis",
            "💰 Residual Income",
            "💎 EVA Calculator",
            "🔄 Transfer Pricing Analysis",
            "🎯 Balanced Scorecard Builder"
        ])

        if calc_choice == "📊 Segment Income Statement":
            st.subheader("Segment Income Statement Builder")
            num_segments = st.number_input("Number of Segments", 1, 6, 3)

            segments = []
            for i in range(int(num_segments)):
                st.markdown(f"**Segment {i+1}:**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    name = st.text_input("Name", value=f"Division {chr(65+i)}", key=f"seg_name_{i}")
                    sales = st.number_input("Sales ($)", 0.0, value=300000.0 + i*50000, step=5000.0, key=f"seg_s_{i}")
                with col2:
                    var_costs = st.number_input("Variable Costs ($)", 0.0, value=165000.0 + i*30000, step=5000.0, key=f"seg_vc_{i}")
                    trace_fixed = st.number_input("Traceable Fixed ($)", 0.0, value=65000.0 + i*15000, step=5000.0, key=f"seg_tf_{i}")
                with col3:
                    st.markdown(" ")
                segments.append({"name": name, "sales": sales, "var_costs": var_costs, "trace_fixed": trace_fixed})

            common_fixed = st.number_input("Company-Wide Common Fixed Costs ($)", 0.0, value=80000.0, step=5000.0)

            if st.button("🧮 Build Segment Report", type="primary"):
                results = []
                for s in segments:
                    cm = s["sales"] - s["var_costs"]
                    seg_margin = cm - s["trace_fixed"]
                    cm_pct = cm / s["sales"] * 100 if s["sales"] > 0 else 0
                    sm_pct = seg_margin / s["sales"] * 100 if s["sales"] > 0 else 0
                    results.append({
                        "Segment": s["name"], "Sales": s["sales"],
                        "Variable Costs": s["var_costs"], "Contribution Margin": cm,
                        "CM %": round(cm_pct, 1),
                        "Traceable Fixed": s["trace_fixed"], "Segment Margin": seg_margin,
                        "SM %": round(sm_pct, 1)
                    })

                df = pd.DataFrame(results)
                total_cm = df["Contribution Margin"].sum()
                total_sm = df["Segment Margin"].sum()
                net_income = total_sm - common_fixed

                display_df = df.copy()
                for col in ["Sales", "Variable Costs", "Contribution Margin", "Traceable Fixed", "Segment Margin"]:
                    display_df[col] = display_df[col].apply(lambda x: f"${x:,.2f}")
                display_df["CM %"] = display_df["CM %"].apply(lambda x: f"{x:.1f}%")
                display_df["SM %"] = display_df["SM %"].apply(lambda x: f"{x:.1f}%")

                st.dataframe(display_df, use_container_width=True, hide_index=True)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Total Segment Margin", f"${total_sm:,.2f}")
                with col2: st.metric("Common Fixed Costs", f"(${common_fixed:,.2f})")
                with col3: st.metric("Net Operating Income", f"${net_income:,.2f}")

                if net_income > 0:
                    st.success(f"✅ Company profitable at ${net_income:,.2f}")
                else:
                    st.error(f"❌ Company loss of ${abs(net_income):,.2f} — review cost structure!")

                # Highlight weak segments
                for r in results:
                    if r["Segment Margin"] < 0:
                        st.warning(f"⚠️ {r['Segment']} has NEGATIVE Segment Margin — consider eliminating!")
                    elif r["Segment Margin"] < r["Sales"] * 0.05:
                        st.info(f"ℹ️ {r['Segment']} has very low Segment Margin ({r['SM %']:.1f}%) — investigate!")

        elif calc_choice == "📈 ROI DuPont Analysis":
            st.subheader("ROI DuPont Decomposition Calculator")

            col1, col2 = st.columns(2)
            with col1:
                noi = st.number_input("Net Operating Income ($)", 0.0, value=300000.0, step=5000.0)
                sales = st.number_input("Sales Revenue ($)", 0.0, value=2000000.0, step=50000.0)
            with col2:
                avg_assets = st.number_input("Average Operating Assets ($)", 0.0, value=1500000.0, step=50000.0)
                required_return = st.number_input("Required Rate of Return (%)", 0.0, 100.0, 15.0, step=0.5)

            if avg_assets > 0 and sales > 0:
                margin = noi / sales * 100
                turnover = sales / avg_assets
                roi = noi / avg_assets * 100
                ri = noi - (required_return / 100 * avg_assets)

                st.markdown("---")
                st.markdown("### 📊 ROI Analysis:")
                col1, col2, col3, col4 = st.columns(4)
                with col1: st.metric("Margin", f"{margin:.2f}%")
                with col2: st.metric("Asset Turnover", f"{turnover:.3f}×")
                with col3: st.metric("ROI", f"{roi:.2f}%")
                with col4:
                    ri_label = f"${ri:,.2f}"
                    st.metric("Residual Income", ri_label, delta="✅ Value Added" if ri > 0 else "❌ Value Destroyed")

                st.markdown(f"""
                **DuPont Breakdown:**
                ```
                ROI = Margin × Asset Turnover
                ROI = {margin:.2f}% × {turnover:.3f}×
                ROI = {roi:.2f}%

                Residual Income:
                RI = ${noi:,.2f} − ({required_return:.1f}% × ${avg_assets:,.2f})
                RI = ${noi:,.2f} − ${required_return/100*avg_assets:,.2f}
                RI = ${ri:,.2f}
                ```
                """)

                if roi > required_return:
                    st.success(f"✅ ROI ({roi:.1f}%) exceeds required return ({required_return:.1f}%) — Division is creating value!")
                else:
                    st.error(f"❌ ROI ({roi:.1f}%) is below required return ({required_return:.1f}%) — Division is underperforming!")

                # Improvement scenarios
                st.markdown("---")
                st.subheader("🔧 What-If Improvement Scenarios:")
                col1, col2, col3 = st.columns(3)
                with col1:
                    cost_save = st.number_input("Cost Savings Scenario ($)", 0.0, value=20000.0, step=1000.0)
                    new_roi_cost = (noi + cost_save) / avg_assets * 100
                    st.metric("ROI if Costs Reduced", f"{new_roi_cost:.2f}%", f"{new_roi_cost - roi:+.2f}%")
                with col2:
                    rev_increase = st.number_input("Revenue Increase Scenario ($)", 0.0, value=100000.0, step=5000.0)
                    new_margin = (noi + rev_increase * 0.5) / (sales + rev_increase) * 100
                    new_roi_rev = (noi + rev_increase * 0.5) / avg_assets * 100
                    st.metric("ROI if Revenue Increases", f"{new_roi_rev:.2f}%", f"{new_roi_rev - roi:+.2f}%")
                with col3:
                    asset_reduce = st.number_input("Asset Reduction Scenario ($)", 0.0, value=100000.0, step=5000.0)
                    new_roi_asset = noi / (avg_assets - asset_reduce) * 100 if (avg_assets - asset_reduce) > 0 else 0
                    st.metric("ROI if Assets Reduced", f"{new_roi_asset:.2f}%", f"{new_roi_asset - roi:+.2f}%")

        elif calc_choice == "💰 Residual Income":
            st.subheader("Residual Income Calculator")

            col1, col2 = st.columns(2)
            with col1:
                noi_ri = st.number_input("Net Operating Income ($)", 0.0, value=300000.0, step=5000.0)
                assets_ri = st.number_input("Average Operating Assets ($)", 0.0, value=1500000.0, step=50000.0)
            with col2:
                req_ret = st.number_input("Required Rate of Return (%)", 0.0, 100.0, 15.0, step=0.5)

            min_return = req_ret / 100 * assets_ri
            ri = noi_ri - min_return

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Net Operating Income", f"${noi_ri:,.2f}")
            with col2: st.metric("Minimum Required Return", f"${min_return:,.2f}")
            with col3: st.metric("Residual Income", f"${ri:,.2f}")

            if ri > 0:
                st.success(f"✅ Positive RI of ${ri:,.2f} — Division earns ${ri:,.2f} ABOVE the minimum required return!")
            else:
                st.error(f"❌ Negative RI of ${abs(ri):,.2f} — Division earns ${abs(ri):,.2f} BELOW the minimum required return!")

            st.markdown(f"""
            **Calculation:**
            ```
            RI = Net Operating Income − (Required Return × Assets)
            RI = ${noi_ri:,.2f} − ({req_ret:.1f}% × ${assets_ri:,.2f})
            RI = ${noi_ri:,.2f} − ${min_return:,.2f}
            RI = ${ri:,.2f}
            ```
            """)

            # New project evaluation
            st.markdown("---")
            st.subheader("📌 Evaluate a New Investment Project:")
            st.info("Residual Income avoids the ROI rejection problem — a manager will ALWAYS accept a project if it has positive RI impact!")

            col1, col2 = st.columns(2)
            with col1:
                project_assets = st.number_input("Project Investment ($)", 0.0, value=200000.0, step=10000.0)
            with col2:
                project_noi = st.number_input("Project Net Operating Income ($)", 0.0, value=36000.0, step=1000.0)

            project_roi = project_noi / project_assets * 100 if project_assets > 0 else 0
            project_ri = project_noi - (req_ret / 100 * project_assets)
            current_roi = noi_ri / assets_ri * 100 if assets_ri > 0 else 0
            new_combined_roi = (noi_ri + project_noi) / (assets_ri + project_assets) * 100
            new_combined_ri = ri + project_ri

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Project ROI", f"{project_roi:.1f}%")
            with col2:
                st.metric("Project RI", f"${project_ri:,.2f}")
            with col3:
                st.metric("New Combined ROI", f"{new_combined_roi:.1f}%",
                          delta=f"{new_combined_roi - current_roi:+.1f}%")

            if project_ri > 0:
                st.success(f"✅ Accept the project! Positive RI of ${project_ri:,.2f}. Company adds value even if it dilutes ROI from {current_roi:.1f}% to {new_combined_roi:.1f}%.")
            else:
                st.error(f"❌ Reject the project. Negative RI of ${abs(project_ri):,.2f}. Project return ({project_roi:.1f}%) is below required return ({req_ret:.1f}%).")

        elif calc_choice == "💎 EVA Calculator":
            st.subheader("Economic Value Added (EVA) Calculator")

            col1, col2 = st.columns(2)
            with col1:
                nopat = st.number_input("After-Tax Net Operating Profit ($)", 0.0, value=225000.0, step=5000.0)
                total_capital = st.number_input("Total Capital Employed ($)", 0.0, value=1500000.0, step=50000.0)
            with col2:
                wacc = st.number_input("WACC — Weighted Average Cost of Capital (%)", 0.0, 100.0, 12.0, step=0.5)
                tax_rate = st.number_input("Tax Rate (%)", 0.0, 100.0, 25.0, step=1.0)

            capital_charge = wacc / 100 * total_capital
            eva = nopat - capital_charge

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Capital Charge (WACC × Capital)", f"${capital_charge:,.2f}")
            with col2: st.metric("After-Tax NOPAT", f"${nopat:,.2f}")
            with col3:
                st.metric("Economic Value Added (EVA)", f"${eva:,.2f}",
                          delta="✅ Value Created" if eva > 0 else "❌ Value Destroyed")

            if eva > 0:
                st.success(f"✅ Positive EVA of ${eva:,.2f} — Shareholder wealth is being CREATED!")
            else:
                st.error(f"❌ Negative EVA of ${abs(eva):,.2f} — Shareholder wealth is being DESTROYED!")

            st.markdown(f"""
            **Calculation:**
            ```
            EVA = After-Tax NOPAT − (WACC × Total Capital)
            EVA = ${nopat:,.2f} − ({wacc:.1f}% × ${total_capital:,.2f})
            EVA = ${nopat:,.2f} − ${capital_charge:,.2f}
            EVA = ${eva:,.2f}
            ```
            """)

        elif calc_choice == "🔄 Transfer Pricing Analysis":
            st.subheader("Transfer Pricing Analysis")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Selling Division:**")
                var_cost = st.number_input("Variable Cost per Unit ($)", 0.0, value=30.0, step=1.0)
                full_cost = st.number_input("Full Cost per Unit ($)", 0.0, value=45.0, step=1.0)
                ext_market_price = st.number_input("External Market Price ($)", 0.0, value=55.0, step=1.0)
                capacity_available = st.radio("Selling Division Capacity:", ["Full capacity — must give up external sales", "Excess capacity — no opportunity cost"])

            with col2:
                st.markdown("**Buying Division:**")
                ext_purchase_price = st.number_input("Buying Division External Purchase Price ($)", 0.0, value=52.0, step=1.0)
                proposed_tp = st.number_input("Proposed Transfer Price ($)", 0.0, value=40.0, step=1.0)

            if capacity_available == "Full capacity — must give up external sales":
                opp_cost = ext_market_price - var_cost
            else:
                opp_cost = 0

            min_tp = var_cost + opp_cost
            max_tp = ext_purchase_price

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Min Transfer Price (Seller's floor)", f"${min_tp:.2f}")
            with col2: st.metric("Max Transfer Price (Buyer's ceiling)", f"${max_tp:.2f}")
            with col3: st.metric("Acceptable Range", f"${min_tp:.2f} — ${max_tp:.2f}" if min_tp <= max_tp else "No acceptable range!")

            if min_tp <= max_tp:
                st.success(f"✅ Transfer should occur! Any price between ${min_tp:.2f} and ${max_tp:.2f} benefits BOTH divisions.")
                if min_tp <= proposed_tp <= max_tp:
                    seller_gain = proposed_tp - min_tp
                    buyer_gain = max_tp - proposed_tp
                    st.info(f"Proposed TP of ${proposed_tp:.2f} is acceptable. Seller gains ${seller_gain:.2f}/unit above minimum, Buyer saves ${buyer_gain:.2f}/unit vs external.")
                else:
                    st.warning(f"⚠️ Proposed TP of ${proposed_tp:.2f} is outside the acceptable range!")
            else:
                st.error(f"❌ No transfer should occur! Min price (${min_tp:.2f}) > Max price (${max_tp:.2f}). Buyer should purchase externally at ${ext_purchase_price:.2f}.")

            st.markdown(f"""
            **Transfer Pricing Logic:**
            ```
            Minimum TP (Seller's floor):
            = Variable Cost + Opportunity Cost (lost external CM)
            = ${var_cost:.2f} + ${opp_cost:.2f}
            = ${min_tp:.2f}

            Maximum TP (Buyer's ceiling):
            = External market price for buying division
            = ${max_tp:.2f}

            Company-wide result:
            {'Transfer benefits company — avoids external market costs' if min_tp <= max_tp else 'No transfer — external purchase is better for company'}
            ```
            """)

        else:  # Balanced Scorecard
            st.subheader("Balanced Scorecard Builder")
            st.markdown("Build your division's Balanced Scorecard with metrics and targets:")

            perspectives = {
                "💰 Financial": [("Revenue Growth", "15%"), ("ROI", "20%"), ("EVA", "$50,000"), ("Cost Reduction", "5%")],
                "👥 Customer": [("Customer Satisfaction", "90%"), ("Market Share", "25%"), ("Retention Rate", "85%"), ("On-Time Delivery", "95%")],
                "⚙️ Internal Process": [("Quality Defect Rate", "<1%"), ("Cycle Time", "3 days"), ("Process Efficiency", "90%"), ("Innovation Pipeline", "5 projects")],
                "📚 Learning & Growth": [("Employee Training Hours", "40 hrs/yr"), ("Staff Turnover", "<10%"), ("Employee Satisfaction", "80%"), ("New Skills Acquired", "3/employee")]
            }

            scorecard_rows = []
            for perspective, metrics in perspectives.items():
                st.markdown(f"**{perspective} Perspective:**")
                cols = st.columns(4)
                for j, (metric, default) in enumerate(metrics):
                    with cols[j]:
                        actual = st.text_input(f"{metric}", value=default, key=f"bsc_{perspective}_{j}")
                        target = st.text_input(f"Target", value=default, key=f"bsc_t_{perspective}_{j}")
                        status = st.selectbox("Status", ["✅ On Track", "⚠️ Monitor", "❌ Off Track"], key=f"bsc_s_{perspective}_{j}")
                        scorecard_rows.append({
                            "Perspective": perspective, "Metric": metric,
                            "Actual": actual, "Target": target, "Status": status
                        })

            if st.button("📊 Display Balanced Scorecard", type="primary"):
                bsc_df = pd.DataFrame(scorecard_rows)
                st.dataframe(bsc_df, use_container_width=True, hide_index=True)

                on_track = len([r for r in scorecard_rows if "✅" in r["Status"]])
                monitor = len([r for r in scorecard_rows if "⚠️" in r["Status"]])
                off_track = len([r for r in scorecard_rows if "❌" in r["Status"]])
                total = len(scorecard_rows)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("✅ On Track", f"{on_track}/{total}")
                with col2: st.metric("⚠️ Monitor", f"{monitor}/{total}")
                with col3: st.metric("❌ Off Track", f"{off_track}/{total}")

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Segment Performance Comparison")
        seg_data = pd.DataFrame({
            "Segment": ["Division A", "Division B", "Division C"],
            "Sales": [400000, 350000, 150000],
            "CM": [180000, 150000, 50000],
            "Segment Margin": [100000, 60000, 20000]
        })
        seg_data["CM %"] = seg_data["CM"] / seg_data["Sales"] * 100
        seg_data["SM %"] = seg_data["Segment Margin"] / seg_data["Sales"] * 100

        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=seg_data["Segment"], y=seg_data["CM %"],
                               name="CM %", marker_color="#2E86C1",
                               text=[f"{v:.1f}%" for v in seg_data["CM %"]], textposition="auto"))
        fig1.add_trace(go.Bar(x=seg_data["Segment"], y=seg_data["SM %"],
                               name="SM %", marker_color="#27AE60",
                               text=[f"{v:.1f}%" for v in seg_data["SM %"]], textposition="auto"))
        fig1.update_layout(title="Segment Profitability: CM% vs Segment Margin%",
                           barmode="group", yaxis_title="Percentage (%)")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("ROI Comparison Across Divisions")
        div_data = pd.DataFrame({
            "Division": ["North", "South", "East", "West"],
            "ROI": [20, 14, 25, 10],
            "RI": [75000, -15000, 150000, -60000]
        })

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=div_data["Division"], y=div_data["ROI"],
                               marker_color=["#27AE60" if r > 15 else "#E74C3C" for r in div_data["ROI"]],
                               text=[f"{r}%" for r in div_data["ROI"]], textposition="auto",
                               name="ROI"))
        fig2.add_hline(y=15, line_dash="dash", line_color="navy", annotation_text="Required Return 15%")
        fig2.update_layout(title="Division ROI vs Required Return", yaxis_title="ROI (%)")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Residual Income by Division")
        fig3 = go.Figure(go.Bar(
            x=div_data["Division"],
            y=div_data["RI"],
            marker_color=["#27AE60" if r > 0 else "#E74C3C" for r in div_data["RI"]],
            text=[f"${r:,.0f}" for r in div_data["RI"]], textposition="auto"
        ))
        fig3.add_hline(y=0, line_color="black", line_width=2)
        fig3.update_layout(title="Residual Income by Division (Positive = Value Created)",
                           yaxis_title="Residual Income ($)")
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("DuPont ROI Components")
        du_pont_data = pd.DataFrame({
            "Division": ["North", "South", "East", "West"],
            "Margin": [15, 10, 20, 8],
            "Turnover": [1.33, 1.40, 1.25, 1.25]
        })
        du_pont_data["ROI"] = du_pont_data["Margin"] * du_pont_data["Turnover"]

        fig4 = go.Figure()
        fig4.add_trace(go.Bar(x=du_pont_data["Division"], y=du_pont_data["Margin"],
                               name="Margin %", marker_color="#3498DB"))
        fig4.add_trace(go.Scatter(x=du_pont_data["Division"], y=du_pont_data["ROI"],
                                   name="ROI %", mode="lines+markers",
                                   line=dict(color="#E67E22", width=3), marker=dict(size=10)))
        fig4.update_layout(title="Margin and ROI by Division", yaxis_title="Percentage (%)")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. An Investment Center manager is responsible for:**")
        q1 = st.radio("", [
            "Costs only",
            "Revenues only",
            "Revenues and costs only",
            "Revenues, costs, AND invested assets"
        ], key="m10q1")
        if st.button("Check Q1", key="m10c1"):
            if q1 == "Revenues, costs, AND invested assets":
                st.success("✅ Correct! Investment centers control revenues, costs, AND the assets used.")
            else:
                st.error("❌ Incorrect. Investment center managers control revenues, costs, AND the invested asset base.")

        st.markdown("---")
        st.markdown("**Q2. Traceable Fixed Costs are costs that:**")
        q2 = st.radio("", [
            "Are shared by all segments equally",
            "Would disappear if the segment were eliminated",
            "Remain constant regardless of segment decisions",
            "Cannot be traced to any segment"
        ], key="m10q2")
        if st.button("Check Q2", key="m10c2"):
            if q2 == "Would disappear if the segment were eliminated":
                st.success("✅ Correct! Traceable fixed costs are caused by the segment's existence and disappear when it's eliminated.")
            else:
                st.error("❌ Incorrect. Traceable fixed costs disappear if the segment is eliminated — they're directly caused by the segment.")

        st.markdown("---")
        st.markdown("""
        **Q3. NOI = $120,000. Average Assets = $600,000. Sales = $800,000.
        What is the ROI?**
        """)
        q3 = st.radio("", ["15%", "20%", "25%", "30%"], key="m10q3")
        if st.button("Check Q3", key="m10c3"):
            if q3 == "20%":
                st.success("✅ Correct! ROI = $120,000 / $600,000 = 20%")
            else:
                st.error("❌ Incorrect. ROI = NOI / Average Assets = $120,000 / $600,000 = 20%")

        st.markdown("---")
        st.markdown("""
        **Q4. ROI = 18%. Required return = 12%. Assets = $500,000.
        What is the Residual Income?**
        """)
        q4 = st.radio("", ["$30,000", "$60,000", "$90,000", "$30,000"], key="m10q4")
        if st.button("Check Q4", key="m10c4"):
            noi_q4 = 0.18 * 500000
            ri_q4 = noi_q4 - (0.12 * 500000)
            if q4 == "$30,000":
                st.success(f"✅ Correct! NOI = 18% × $500K = $90K. RI = $90K − (12% × $500K) = $90K − $60K = ${ri_q4:,.0f}")
            else:
                st.error(f"❌ Incorrect. NOI = $90,000. RI = $90,000 − $60,000 = $30,000")

        st.markdown("---")
        st.markdown("**Q5. The MAIN advantage of Residual Income over ROI is:**")
        q5 = st.radio("", [
            "It is easier to calculate",
            "It prevents managers from rejecting value-adding investments that dilute their ROI",
            "It includes WACC in the calculation",
            "It is always a higher number"
        ], key="m10q5")
        if st.button("Check Q5", key="m10c5"):
            if q5 == "It prevents managers from rejecting value-adding investments that dilute their ROI":
                st.success("✅ Correct! RI prevents the ROI rejection problem — managers will accept any project with positive RI impact.")
            else:
                st.error("❌ Incorrect. RI's key advantage is avoiding the ROI rejection problem — managers won't turn down profitable projects that dilute their ROI.")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Key Formulas")
        formulas_df = pd.DataFrame({
            "Metric": ["ROI", "Margin", "Asset Turnover", "ROI (DuPont)", "Residual Income", "EVA", "Min Transfer Price", "Max Transfer Price"],
            "Formula": [
                "Net Operating Income / Average Operating Assets",
                "Net Operating Income / Sales",
                "Sales / Average Operating Assets",
                "Margin × Asset Turnover",
                "NOI − (Required Return % × Average Operating Assets)",
                "After-Tax NOPAT − (WACC × Total Capital Employed)",
                "Selling Division Variable Cost + Opportunity Cost",
                "Buying Division's External Purchase Price"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Responsibility Centers Summary")
        centers_sum = pd.DataFrame({
            "Type": ["Cost Center", "Revenue Center", "Profit Center", "Investment Center"],
            "Controls": ["Costs", "Revenues", "Revenues + Costs", "Revenue + Costs + Assets"],
            "Key Metric": ["Cost variances", "Revenue variances", "Segment Margin", "ROI / RI / EVA"],
            "Example": ["HR, IT, Production Dept", "Sales territory", "Product division", "Subsidiary, SBU"]
        })
        st.dataframe(centers_sum, use_container_width=True, hide_index=True)

        st.subheader("🔍 ROI vs RI vs EVA")
        compare_df = pd.DataFrame({
            "Feature": ["Measures", "Best for", "Weakness", "Unit", "Accepts projects above required return?", "Considers asset size?"],
            "ROI": ["% return on assets", "Comparing divisions of different sizes", "Reject good projects that dilute ROI", "Percentage", "❌ Not always", "❌ No — % based"],
            "Residual Income": ["$ value above min return", "Internal decision-making", "Cannot compare divisions of different sizes", "Dollar amount", "✅ Always", "✅ Yes"],
            "EVA": ["$ shareholder value created", "External reporting, executive compensation", "Complex adjustments required", "Dollar amount", "✅ Always", "✅ Yes"]
        })
        st.dataframe(compare_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Allocating common fixed costs to segments for drop/keep decisions",
                "Using ROI alone to evaluate all investment decisions",
                "Setting transfer price below variable cost",
                "Evaluating segments using full-cost absorption format",
                "Ignoring opportunity costs in transfer pricing",
                "Using ROI to compare divisions of very different sizes"
            ],
            "Correct Approach": [
                "Only use traceable costs for segment decisions; common costs are irrelevant",
                "Use RI alongside ROI — RI avoids the project rejection problem",
                "Minimum TP must at least cover variable cost + opportunity cost",
                "Use contribution approach: CM − Traceable Fixed = Segment Margin",
                "Full capacity = opportunity cost exists; excess capacity = no opportunity cost",
                "Use Residual Income ($) to compare divisions of different sizes"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 10 Complete! You can evaluate segment performance and make transfer pricing decisions.")
        st.info("💡 Next: Module 11 — Relevant Costs for Decision Making")

if __name__ == "__main__":
    show()