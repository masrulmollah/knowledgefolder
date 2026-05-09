import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💰 Module 12: Capital Budgeting")
    st.markdown("*Evaluate long-term investment decisions using NPV, IRR, Payback, and Profitability Index*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. What is Capital Budgeting?")
        st.markdown("""
        **Capital Budgeting** is the process of evaluating and selecting long-term investment projects that 
        require significant capital outlay and generate returns over multiple years.

        #### Types of Investment Decisions:
        | Type | Examples |
        |------|---------|
        | **Expansion** | New factory, new product line, entering new market |
        | **Replacement** | Replace old equipment with newer, more efficient machines |
        | **Cost Reduction** | Automation to reduce labor costs |
        | **Regulatory/Safety** | Pollution control, safety equipment (often mandatory) |
        | **Research & Development** | New product development |

        #### Time Value of Money — The Foundation:
        ```
        A dollar received TODAY is worth MORE than a dollar received in the FUTURE.
        Why? Because money today can be invested and earn a return.

        Present Value:  PV = FV / (1 + r)^n
        Future Value:   FV = PV × (1 + r)^n

        Annuity PV Factor = [1 − (1+r)^−n] / r
        ```
        """)

        st.subheader("2. Payback Period")
        st.markdown("""
        **Payback Period** = Time required to recover the initial investment from cash inflows.

        #### Equal Cash Flows:
        ```
        Payback Period = Initial Investment / Annual Net Cash Flow
        ```

        #### Unequal Cash Flows:
        Accumulate cash flows year by year until investment is recovered.
        ```
        Payback = Year before recovery + (Remaining Amount / Cash Flow in Recovery Year)
        ```

        | Advantages | Disadvantages |
        |-----------|---------------|
        | Simple and easy to understand | Ignores time value of money |
        | Measures liquidity and risk | Ignores cash flows AFTER payback |
        | Quick screening tool | Arbitrary cutoff point |
        | Useful in uncertain environments | Does not measure profitability |

        **Discounted Payback Period:** Same concept but uses discounted (PV) cash flows.
        Eliminates the time value weakness but still ignores post-payback flows.
        """)

        st.subheader("3. Net Present Value (NPV)")
        st.markdown("""
        **NPV** = Sum of present values of all cash inflows minus initial investment.

        ```
        NPV = Σ [CFt / (1 + r)^t] − Initial Investment

        Decision Rule:
        NPV > 0  →  ACCEPT  (project adds value to company)
        NPV < 0  →  REJECT  (project destroys value)
        NPV = 0  →  INDIFFERENT (project earns exactly the required return)
        ```

        **NPV is the BEST capital budgeting method because:**
        - Considers time value of money ✅
        - Measures dollar value added ✅
        - Uses all cash flows over project life ✅
        - No multiple solutions ✅
        - Additive: NPV(A+B) = NPV(A) + NPV(B) ✅
        """)

        st.subheader("4. Internal Rate of Return (IRR)")
        st.markdown("""
        **IRR** = The discount rate that makes NPV exactly equal to zero.

        ```
        Find r such that: Σ [CFt / (1 + r)^t] = Initial Investment

        Decision Rule:
        IRR > Required Rate of Return  →  ACCEPT
        IRR < Required Rate of Return  →  REJECT
        ```

        **IRR Limitations:**
        - May give multiple IRRs for unconventional cash flows
        - Can conflict with NPV when ranking mutually exclusive projects
        - Assumes reinvestment at the IRR rate (often unrealistic)
        """)

        st.subheader("5. Profitability Index (PI)")
        st.markdown("""
        **PI** = PV of Future Cash Flows / Initial Investment

        ```
        PI = PV of Future Cash Flows / Initial Investment

        Decision Rule:
        PI > 1  →  ACCEPT (project generates more than $1 PV per $1 invested)
        PI < 1  →  REJECT
        PI = 1  →  INDIFFERENT
        ```

        **Best Use:** When capital is RATIONED — rank projects by PI to maximize total NPV per dollar invested.
        """)

        st.subheader("6. After-Tax Cash Flow Estimation")
        st.markdown("""
        **All capital budgeting should use AFTER-TAX, INCREMENTAL cash flows.**

        #### Types of Cash Flows:
        ```
        Initial Investment:
        − Equipment purchase price
        − Installation costs
        − Increase in working capital
        + Salvage value of old equipment (after-tax)

        Annual Operating Cash Flows:
        Method 1: After-Tax NOI + Depreciation
        = Net Income + Depreciation
        = (Sales − Costs − Depreciation) × (1 − Tax Rate) + Depreciation

        Method 2 (shortcut):
        = Pretax Cash Flow × (1 − Tax Rate) + (Depreciation × Tax Rate)
        = After-Tax Operating CF + Depreciation Tax Shield

        Depreciation Tax Shield = Depreciation × Tax Rate

        Terminal Cash Flows (end of project):
        + After-Tax Salvage Value = Salvage − (Salvage − Book Value) × Tax Rate
        + Recovery of Working Capital
        ```
        """)

        st.subheader("7. Ranking Mutually Exclusive Projects")
        st.markdown("""
        When projects are **mutually exclusive** (can only choose one):
        - **Always use NPV** as the primary ranking criterion
        - IRR can give misleading rankings (scale problem)
        - PI can give misleading rankings when projects have different sizes

        **Example of IRR vs NPV conflict:**
        ```
        Project A: Invest $100K, NPV = $40K, IRR = 35%
        Project B: Invest $500K, NPV = $120K, IRR = 28%

        IRR says choose A. NPV says choose B.
        → If mutually exclusive, choose B (adds $120K vs $40K)
        ```
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example 1: Complete NPV and Payback Analysis")
        st.markdown("""
        **Project Data:**
        - Initial Investment: $200,000
        - Useful Life: 5 years
        - Annual Cash Inflows: $65,000
        - Salvage Value: $20,000
        - Required Rate of Return: 12%

        **Step 1 — Payback Period:**
        ```
        Annual CF = $65,000
        After 3 years: $65,000 × 3 = $195,000
        Remaining: $200,000 − $195,000 = $5,000

        Payback = 3 + ($5,000 / $65,000) = 3.08 years
        ```

        **Step 2 — NPV Calculation:**
        ```
        PV Annuity Factor (12%, 5 yrs) = [1 − (1.12)^−5] / 0.12 = 3.6048

        PV of annual CFs: $65,000 × 3.6048    = $234,312
        PV of salvage:    $20,000 × (1.12)^−5  =  $11,349

        Total PV of inflows:                   = $245,661
        − Initial Investment:                  = ($200,000)
        ───────────────────────────────────────────────────
        NPV:                                   = $45,661  ✅ ACCEPT!
        ```

        **Step 3 — Profitability Index:**
        ```
        PI = $245,661 / $200,000 = 1.23 > 1 ✅ ACCEPT!
        ```
        """)

        st.subheader("Example 2: After-Tax Cash Flows with Depreciation")
        st.markdown("""
        **Equipment: $300,000. Life: 5 years. No salvage. Straight-line depreciation.**
        **Annual Revenue Increase: $120,000. Annual Cost Savings: $30,000.**
        **Tax Rate: 30%. Required Return: 10%.**

        **Annual Depreciation = $300,000 / 5 = $60,000**

        **Method 1 — Net Income + Depreciation:**
        ```
        Revenue / Cost Savings          $150,000
        − Depreciation                  ($60,000)
        ─────────────────────────────────────────
        Pre-Tax Income                   $90,000
        − Tax (30%)                     ($27,000)
        ─────────────────────────────────────────
        Net Income                       $63,000
        + Depreciation (add back)        $60,000
        ─────────────────────────────────────────
        Annual After-Tax Cash Flow      $123,000
        ```

        **Method 2 — Shortcut:**
        ```
        Depreciation Tax Shield = $60,000 × 30% = $18,000
        After-Tax Operating CF  = $150,000 × (1 − 30%) = $105,000
        Total Annual CF         = $105,000 + $18,000 = $123,000 ✓
        ```

        **NPV:**
        ```
        PV Factor (10%, 5 yrs) = 3.7908
        NPV = $123,000 × 3.7908 − $300,000
            = $466,268 − $300,000
            = $166,268 ✅ ACCEPT!
        ```
        """)

        st.subheader("Example 3: Capital Rationing with PI")
        st.markdown("""
        **Budget: $500,000. Four available projects (mutually exclusive within each):**

        | Project | Investment | NPV | PI | Rank |
        |---------|-----------|-----|-----|------|
        | A | $200,000 | $60,000 | 1.30 | 1st |
        | B | $150,000 | $40,000 | 1.27 | 2nd |
        | C | $300,000 | $70,000 | 1.23 | 3rd |
        | D | $100,000 | $20,000 | 1.20 | 4th |

        **Optimal Selection (PI ranking, $500K budget):**
        ```
        Choose A: $200,000 used, $300,000 remaining, NPV = $60,000
        Choose B: $150,000 used, $150,000 remaining, NPV = $40,000
        Choose D: $100,000 used, $50,000 remaining,  NPV = $20,000
        ────────────────────────────────────────────────────────────
        Total NPV: $120,000 from $450,000 invested

        (Cannot afford C at $300,000 with only $50,000 remaining)
        ```
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        calc_choice = st.selectbox("Choose Calculator:", [
            "⏱️ Payback Period",
            "📊 Net Present Value (NPV)",
            "📈 IRR Calculator",
            "🎯 Profitability Index",
            "🏗️ Complete Project Evaluation",
            "💼 Capital Rationing (PI Method)"
        ])

        if calc_choice == "⏱️ Payback Period":
            st.subheader("Payback Period Calculator")
            initial_inv = st.number_input("Initial Investment ($)", 0.0, value=200000.0, step=5000.0)
            equal_flows = st.checkbox("Equal Annual Cash Flows?", value=False)

            if equal_flows:
                annual_cf = st.number_input("Annual Cash Flow ($)", 0.0, value=65000.0, step=1000.0)
                if annual_cf > 0:
                    payback = initial_inv / annual_cf
                    years = int(payback)
                    months = (payback - years) * 12
                    st.metric("Payback Period", f"{years} years {months:.1f} months ({payback:.3f} years)")

                    # Discounted payback
                    disc_rate = st.number_input("Discount Rate for Discounted Payback (%)", 0.0, value=12.0)
                    n = st.number_input("Project Life (years)", 1, 30, 5)
                    cum_pv = 0
                    dpb = None
                    for yr in range(1, int(n)+1):
                        pv = annual_cf / (1 + disc_rate/100)**yr
                        cum_pv += pv
                        if cum_pv >= initial_inv and dpb is None:
                            prev_cum = cum_pv - pv
                            dpb = yr - 1 + (initial_inv - prev_cum) / pv
                    if dpb:
                        st.metric("Discounted Payback Period", f"{dpb:.2f} years")
                    else:
                        st.warning("Investment not recovered within project life at this discount rate.")
            else:
                num_years = st.number_input("Number of Years", 1, 20, 6)
                cfs = []
                for i in range(int(num_years)):
                    cf = st.number_input(f"Year {i+1} Cash Flow ($)", value=50000.0 + i*5000, key=f"pb_cf_{i}")
                    cfs.append(cf)

                disc_rate_pb = st.number_input("Discount Rate for Discounted Payback (%)", 0.0, value=12.0)

                if st.button("🧮 Calculate Payback", type="primary"):
                    cumulative = 0
                    payback_year = None
                    disc_cumulative = 0
                    disc_payback = None
                    rows = []
                    for i, cf in enumerate(cfs):
                        cumulative += cf
                        pv_cf = cf / (1 + disc_rate_pb/100)**(i+1)
                        disc_cumulative += pv_cf

                        if cumulative >= initial_inv and payback_year is None:
                            prev = cumulative - cf
                            payback_year = i + (initial_inv - prev) / cf
                        if disc_cumulative >= initial_inv and disc_payback is None:
                            prev_d = disc_cumulative - pv_cf
                            disc_payback = i + (initial_inv - prev_d) / pv_cf

                        rows.append({
                            "Year": i+1,
                            "Cash Flow": f"${cf:,.2f}",
                            "Cumulative CF": f"${cumulative:,.2f}",
                            "PV Cash Flow": f"${pv_cf:,.2f}",
                            "Discounted Cumulative": f"${disc_cumulative:,.2f}",
                            "Recovered?": "✅" if cumulative >= initial_inv else "❌"
                        })

                    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
                    col1, col2 = st.columns(2)
                    with col1:
                        if payback_year:
                            st.metric("Payback Period", f"{payback_year:.2f} years")
                        else:
                            st.error("❌ Not recovered within project life!")
                    with col2:
                        if disc_payback:
                            st.metric("Discounted Payback Period", f"{disc_payback:.2f} years")
                        else:
                            st.error("❌ Discounted payback not achieved!")

        elif calc_choice == "📊 Net Present Value (NPV)":
            st.subheader("Net Present Value Calculator")
            initial = st.number_input("Initial Investment ($)", 0.0, value=200000.0, step=5000.0)
            rate = st.number_input("Required Rate of Return (%)", 0.0, value=12.0, step=0.5) / 100
            equal_cf_npv = st.checkbox("Equal Annual Cash Flows?", value=True)

            if equal_cf_npv:
                annual_cf_npv = st.number_input("Annual Cash Flow ($)", 0.0, value=65000.0, step=1000.0)
                n_npv = st.number_input("Project Life (years)", 1, 30, 5)
                salvage = st.number_input("Salvage Value ($)", 0.0, value=20000.0, step=1000.0)

                if rate > 0:
                    pv_factor = (1 - (1+rate)**(-n_npv)) / rate
                else:
                    pv_factor = n_npv
                pv_annuity = annual_cf_npv * pv_factor
                pv_salvage = salvage / (1+rate)**n_npv
                total_pv = pv_annuity + pv_salvage
                npv = total_pv - initial
                pi = total_pv / initial if initial > 0 else 0

                st.markdown("---")
                st.markdown(f"""
                **NPV Calculation:**
                ```
                PV Annuity Factor ({rate*100:.1f}%, {int(n_npv)} yrs) = {pv_factor:.4f}

                PV of Annual CFs:  ${annual_cf_npv:,.2f} × {pv_factor:.4f} = ${pv_annuity:,.2f}
                PV of Salvage:     ${salvage:,.2f} / (1+{rate*100:.1f}%)^{int(n_npv)} = ${pv_salvage:,.2f}
                ─────────────────────────────────────────────────────────────
                Total PV of Inflows:                                 ${total_pv:,.2f}
                − Initial Investment:                               (${initial:,.2f})
                ─────────────────────────────────────────────────────────────
                NPV:                                                 ${npv:,.2f}
                Profitability Index:                                  {pi:.4f}
                ```
                """)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("NPV", f"${npv:,.2f}")
                with col2: st.metric("Profitability Index", f"{pi:.4f}")
                with col3:
                    if npv > 0:
                        st.success("✅ ACCEPT — Positive NPV!")
                    else:
                        st.error("❌ REJECT — Negative NPV!")

            else:
                num_years_npv = st.number_input("Number of Years", 1, 20, 5)
                cfs_npv = []
                for i in range(int(num_years_npv)):
                    cf = st.number_input(f"Year {i+1} Cash Flow ($)", value=50000.0 + i*5000, key=f"npv_cf_{i}")
                    cfs_npv.append(cf)

                if st.button("🧮 Calculate NPV", type="primary"):
                    rows = []
                    total_pv_npv = 0
                    cum_npv = -initial
                    for i, cf in enumerate(cfs_npv):
                        pv_f = 1 / (1+rate)**(i+1)
                        pv = cf * pv_f
                        total_pv_npv += pv
                        cum_npv += pv
                        rows.append({
                            "Year": i+1, "Cash Flow": f"${cf:,.2f}",
                            "PV Factor": f"{pv_f:.6f}", "Present Value": f"${pv:,.2f}",
                            "Cumulative NPV": f"${cum_npv:,.2f}"
                        })
                    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
                    npv = total_pv_npv - initial
                    pi = total_pv_npv / initial if initial > 0 else 0
                    col1, col2 = st.columns(2)
                    with col1: st.metric("NPV", f"${npv:,.2f}")
                    with col2: st.metric("PI", f"{pi:.4f}")
                    if npv > 0:
                        st.success("✅ ACCEPT — Positive NPV!")
                    else:
                        st.error("❌ REJECT — Negative NPV!")

        elif calc_choice == "📈 IRR Calculator":
            st.subheader("IRR Calculator")
            initial_irr = st.number_input("Initial Investment ($)", 0.0, value=200000.0, step=5000.0)
            equal_cf_irr = st.checkbox("Equal Annual Cash Flows?", value=True)
            required_rate_irr = st.number_input("Required Rate of Return (%)", 0.0, value=12.0, step=0.5)

            if equal_cf_irr:
                annual_cf_irr = st.number_input("Annual Cash Flow ($)", 0.0, value=65000.0, step=1000.0)
                n_irr = st.number_input("Project Life (years)", 1, 30, 5)
                salvage_irr = st.number_input("Salvage Value ($)", 0.0, value=0.0, step=1000.0)

                def npv_at_rate(r, cf, n, inv, salv):
                    if r == 0:
                        pv = cf * n + salv
                    else:
                        pv = cf * (1 - (1+r)**(-n)) / r + salv / (1+r)**n
                    return pv - inv

                lo, hi = 0.0001, 5.0
                for _ in range(200):
                    mid = (lo + hi) / 2
                    if npv_at_rate(mid, annual_cf_irr, n_irr, initial_irr, salvage_irr) > 0:
                        lo = mid
                    else:
                        hi = mid
                irr = (lo + hi) / 2 * 100

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("IRR", f"{irr:.2f}%")
                with col2: st.metric("Required Return", f"{required_rate_irr:.1f}%")
                with col3:
                    spread = irr - required_rate_irr
                    st.metric("Spread", f"{spread:+.2f}%", delta="✅ Accept" if spread > 0 else "❌ Reject")

                if irr > required_rate_irr:
                    st.success(f"✅ ACCEPT — IRR ({irr:.2f}%) > Required Return ({required_rate_irr:.1f}%)")
                else:
                    st.error(f"❌ REJECT — IRR ({irr:.2f}%) < Required Return ({required_rate_irr:.1f}%)")

                # NPV Profile chart
                rates_range = np.linspace(0.001, irr/100 * 2.2, 80)
                npvs_range = [npv_at_rate(r, annual_cf_irr, n_irr, initial_irr, salvage_irr) for r in rates_range]

                fig_irr = go.Figure()
                fig_irr.add_trace(go.Scatter(x=rates_range*100, y=npvs_range, mode="lines",
                                              name="NPV Profile", line=dict(color="#2E86C1", width=3)))
                fig_irr.add_hline(y=0, line_color="black", line_width=2)
                fig_irr.add_vline(x=irr, line_dash="dash", line_color="green",
                                   annotation_text=f"IRR = {irr:.1f}%")
                fig_irr.add_vline(x=required_rate_irr, line_dash="dot", line_color="red",
                                   annotation_text=f"Required = {required_rate_irr:.1f}%")
                fig_irr.update_layout(title="NPV Profile — Sensitivity to Discount Rate",
                                       xaxis_title="Discount Rate (%)", yaxis_title="NPV ($)")
                st.plotly_chart(fig_irr, use_container_width=True)

        elif calc_choice == "🎯 Profitability Index":
            st.subheader("Profitability Index Calculator")
            num_projects_pi = st.number_input("Number of Projects", 1, 8, 4)
            pi_data = []
            for i in range(int(num_projects_pi)):
                col1, col2, col3 = st.columns(3)
                with col1: p_name = st.text_input("Project Name", value=f"Project {chr(65+i)}", key=f"pi_n_{i}")
                with col2: p_inv = st.number_input("Investment ($)", 0.0, value=200000.0 - i*30000, step=5000.0, key=f"pi_i_{i}")
                with col3: p_npv = st.number_input("NPV ($)", 0.0, value=40000.0 + i*10000, step=1000.0, key=f"pi_npv_{i}")
                pi_val = (p_inv + p_npv) / p_inv if p_inv > 0 else 0
                pi_data.append({"name": p_name, "inv": p_inv, "npv": p_npv, "pi": pi_val})

            pi_sorted = sorted(pi_data, key=lambda x: x["pi"], reverse=True)
            pi_df = pd.DataFrame([{
                "Rank": idx+1, "Project": p["name"],
                "Investment": f"${p['inv']:,.2f}", "NPV": f"${p['npv']:,.2f}",
                "PI": f"{p['pi']:.4f}",
                "Accept?": "✅ Accept" if p["pi"] >= 1 else "❌ Reject"
            } for idx, p in enumerate(pi_sorted)])
            st.dataframe(pi_df, use_container_width=True, hide_index=True)
            st.info("💡 PI ranking is especially useful when capital is limited (capital rationing). Choose highest PI projects first!")

        elif calc_choice == "🏗️ Complete Project Evaluation":
            st.subheader("Complete After-Tax Capital Budgeting Analysis")
            st.markdown("### Project Details:")
            col1, col2, col3 = st.columns(3)
            with col1:
                equip_cost = st.number_input("Equipment Cost ($)", 0.0, value=300000.0, step=5000.0)
                working_cap = st.number_input("Working Capital Required ($)", 0.0, value=20000.0, step=1000.0)
                salvage_val = st.number_input("Salvage Value at End ($)", 0.0, value=30000.0, step=1000.0)
            with col2:
                project_life = st.number_input("Project Life (years)", 1, 30, 5)
                annual_revenue = st.number_input("Annual Revenue Increase ($)", 0.0, value=150000.0, step=5000.0)
                annual_costs = st.number_input("Annual Cash Costs ($)", 0.0, value=50000.0, step=2000.0)
            with col3:
                tax_rate_cb = st.number_input("Tax Rate (%)", 0.0, 100.0, 30.0) / 100
                req_return_cb = st.number_input("Required Return (%)", 0.0, 50.0, 10.0) / 100
                dep_method = st.radio("Depreciation", ["Straight-Line", "Double Declining"])

            total_initial = equip_cost + working_cap
            annual_dep = equip_cost / project_life if project_life > 0 else 0

            pretax_cf = annual_revenue - annual_costs
            after_tax_op = pretax_cf * (1 - tax_rate_cb)
            dep_tax_shield = annual_dep * tax_rate_cb
            annual_atcf = after_tax_op + dep_tax_shield

            # Terminal CF
            book_value = 0  # fully depreciated (SL)
            if salvage_val > book_value:
                tax_on_gain = (salvage_val - book_value) * tax_rate_cb
            else:
                tax_on_gain = 0
            after_tax_salvage = salvage_val - tax_on_gain
            terminal_cf = after_tax_salvage + working_cap

            # NPV
            if req_return_cb > 0:
                pv_factor_cb = (1 - (1+req_return_cb)**(-project_life)) / req_return_cb
            else:
                pv_factor_cb = project_life
            pv_terminal_factor = 1 / (1+req_return_cb)**project_life
            pv_operations = annual_atcf * pv_factor_cb
            pv_terminal = terminal_cf * pv_terminal_factor
            total_pv_cb = pv_operations + pv_terminal
            npv_cb = total_pv_cb - total_initial
            pi_cb = total_pv_cb / total_initial if total_initial > 0 else 0
            payback_cb = total_initial / annual_atcf if annual_atcf > 0 else float('inf')

            st.markdown("---")
            st.markdown("### Results:")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Cash Flow Summary:**")
                cf_df = pd.DataFrame({
                    "Item": ["Annual Depreciation", "Pre-Tax Operating CF",
                              "After-Tax Operating CF", "Depreciation Tax Shield",
                              "Annual After-Tax CF", "Terminal Cash Flow"],
                    "Amount": [f"${annual_dep:,.2f}", f"${pretax_cf:,.2f}",
                                f"${after_tax_op:,.2f}", f"${dep_tax_shield:,.2f}",
                                f"${annual_atcf:,.2f}", f"${terminal_cf:,.2f}"]
                })
                st.dataframe(cf_df, use_container_width=True, hide_index=True)

            with col2:
                st.markdown("**Investment Decision Metrics:**")
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("NPV", f"${npv_cb:,.2f}", delta="✅ ACCEPT" if npv_cb > 0 else "❌ REJECT")
                    st.metric("Payback Period", f"{payback_cb:.2f} years")
                with col_b:
                    st.metric("Profitability Index", f"{pi_cb:.4f}")
                    st.metric("PV of All CFs", f"${total_pv_cb:,.2f}")

            # Year by year table
            st.markdown("### Year-by-Year Cash Flow Table:")
            yearly_rows = []
            cum_npv_cb = -total_initial
            for yr in range(1, int(project_life)+1):
                cf_yr = annual_atcf + (terminal_cf if yr == int(project_life) else 0)
                pv_yr = cf_yr / (1+req_return_cb)**yr
                cum_npv_cb += pv_yr
                yearly_rows.append({
                    "Year": yr,
                    "Operating ATCF": f"${annual_atcf:,.2f}",
                    "Terminal CF": f"${terminal_cf:,.2f}" if yr == int(project_life) else "$0",
                    "Total CF": f"${cf_yr:,.2f}",
                    "PV Factor": f"{1/(1+req_return_cb)**yr:.4f}",
                    "PV of CF": f"${pv_yr:,.2f}",
                    "Cumulative NPV": f"${cum_npv_cb:,.2f}"
                })
            st.dataframe(pd.DataFrame(yearly_rows), use_container_width=True, hide_index=True)

            if npv_cb > 0:
                st.success(f"✅ ACCEPT — Project adds ${npv_cb:,.2f} in value. PI = {pi_cb:.2f}. Payback in {payback_cb:.1f} years.")
            else:
                st.error(f"❌ REJECT — Project destroys ${abs(npv_cb):,.2f} in value.")

        else:  # Capital Rationing
            st.subheader("Capital Rationing — Profitability Index Method")
            budget_cap = st.number_input("Total Capital Budget ($)", 0.0, value=500000.0, step=10000.0)
            num_proj_cr = st.number_input("Number of Available Projects", 1, 10, 5)

            projects_cr = []
            for i in range(int(num_proj_cr)):
                col1, col2, col3 = st.columns(3)
                with col1: cr_name = st.text_input("Project", value=f"Project {chr(65+i)}", key=f"cr_n_{i}")
                with col2: cr_inv = st.number_input("Investment ($)", 0.0, value=200000.0 - i*20000, step=5000.0, key=f"cr_i_{i}")
                with col3: cr_npv = st.number_input("NPV ($)", 0.0, value=60000.0 - i*5000, step=1000.0, key=f"cr_npv_{i}")
                cr_pi = (cr_inv + cr_npv) / cr_inv if cr_inv > 0 else 0
                projects_cr.append({"name": cr_name, "inv": cr_inv, "npv": cr_npv, "pi": cr_pi})

            if st.button("🧮 Optimize Capital Budget", type="primary"):
                sorted_cr = sorted(projects_cr, key=lambda x: x["pi"], reverse=True)
                remaining_budget = budget_cap
                selected = []
                total_npv_selected = 0

                for p in sorted_cr:
                    if p["inv"] <= remaining_budget:
                        selected.append(p["name"])
                        remaining_budget -= p["inv"]
                        total_npv_selected += p["npv"]

                result_rows = []
                for p in sorted_cr:
                    result_rows.append({
                        "Project": p["name"],
                        "Investment": f"${p['inv']:,.2f}",
                        "NPV": f"${p['npv']:,.2f}",
                        "PI": f"{p['pi']:.4f}",
                        "Selected": "✅ Yes" if p["name"] in selected else "❌ No (budget insufficient)"
                    })

                st.dataframe(pd.DataFrame(result_rows), use_container_width=True, hide_index=True)
                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Total NPV from Selected", f"${total_npv_selected:,.2f}")
                with col2: st.metric("Budget Used", f"${budget_cap - remaining_budget:,.2f}")
                with col3: st.metric("Budget Remaining", f"${remaining_budget:,.2f}")
                st.success(f"✅ Optimal selection: {', '.join(selected)} — Total NPV = ${total_npv_selected:,.2f}")

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("NPV Profile — Sensitivity to Discount Rate")
        inv_viz = 200000
        annual_cf_viz = 65000
        n_viz = 5
        salvage_viz = 20000
        rates_viz = np.linspace(0.001, 0.40, 100)
        npvs_viz = []
        for r in rates_viz:
            pv = annual_cf_viz * (1-(1+r)**(-n_viz))/r + salvage_viz/(1+r)**n_viz
            npvs_viz.append(pv - inv_viz)

        irr_approx = 0.285
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=rates_viz*100, y=npvs_viz, mode="lines",
                                   name="NPV", line=dict(color="#2E86C1", width=3),
                                   fill="tozeroy", fillcolor="rgba(46,134,193,0.1)"))
        fig1.add_hline(y=0, line_color="black", line_width=2)
        fig1.add_vline(x=12, line_dash="dot", line_color="red", annotation_text="Required 12%")
        fig1.add_vline(x=irr_approx*100, line_dash="dash", line_color="green",
                       annotation_text=f"IRR ≈ {irr_approx*100:.0f}%")
        fig1.update_layout(title="NPV Profile — How NPV Changes with Discount Rate",
                           xaxis_title="Discount Rate (%)", yaxis_title="NPV ($)",
                           hovermode="x unified")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Cumulative Cash Flow — Payback Visualization")
        cfs_pb = [-200000, 65000, 65000, 65000, 65000, 65000+20000]
        cum_cfs_pb = []
        cum = 0
        for cf in cfs_pb:
            cum += cf
            cum_cfs_pb.append(cum)

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=list(range(6)), y=cum_cfs_pb, mode="lines+markers",
                                   name="Cumulative CF", line=dict(color="#2E86C1", width=3),
                                   marker=dict(size=10)))
        fig2.add_hline(y=0, line_color="red", line_dash="dash", annotation_text="Break-Even (Payback)")
        fig2.update_xaxes(tickvals=list(range(6)), ticktext=["0", "Y1", "Y2", "Y3", "Y4", "Y5"])
        fig2.update_layout(title="Cumulative Cash Flow — Payback Visualization",
                           xaxis_title="Year", yaxis_title="Cumulative Cash Flow ($)")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Capital Budgeting Methods Comparison")
        methods_comp = ["Payback Period", "NPV", "IRR", "Profitability Index"]
        scores_tvm = [1, 5, 4, 4]
        scores_practical = [4, 5, 3, 4]

        fig3 = go.Figure(data=[
            go.Bar(name="Considers TVM", x=methods_comp, y=scores_tvm, marker_color="#2E86C1"),
            go.Bar(name="Practical Use", x=methods_comp, y=scores_practical, marker_color="#27AE60")
        ])
        fig3.update_layout(title="Capital Budgeting Methods — Attribute Scores (1-5)",
                           barmode="group", yaxis_title="Score (1=Low, 5=High)", yaxis_range=[0,6])
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("Effect of Depreciation Tax Shield on Project Value")
        inv_dep = 300000
        n_dep = 5
        dep_per_year = inv_dep / n_dep
        req_r = 0.10
        tax_rates_range = np.linspace(0, 0.50, 50)
        npvs_dep = []
        for tr in tax_rates_range:
            shield_pv = dep_per_year * tr * (1-(1+req_r)**(-n_dep))/req_r
            npvs_dep.append(shield_pv)

        fig4 = go.Figure(go.Scatter(
            x=tax_rates_range*100, y=npvs_dep, mode="lines",
            line=dict(color="#E67E22", width=3), fill="tozeroy"
        ))
        fig4.update_layout(title="PV of Depreciation Tax Shield vs Tax Rate (Straight-Line, $300K, 5 yrs, 10%)",
                           xaxis_title="Tax Rate (%)", yaxis_title="PV of Tax Shield ($)")
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. NPV > 0 means:**")
        q1 = st.radio("", [
            "Project earns exactly the required return",
            "Project creates value — accept!",
            "Project destroys value — reject!",
            "IRR equals the required return"
        ], key="m12q1")
        if st.button("Check Q1", key="m12c1"):
            if q1 == "Project creates value — accept!":
                st.success("✅ Correct! NPV > 0 means the project returns MORE than the required rate — it adds value!")
            else:
                st.error("❌ Incorrect. NPV > 0 means the project creates value above the required return — ACCEPT it!")

        st.markdown("---")
        st.markdown("**Q2. Initial investment = $120,000. Annual cash flow = $30,000. Payback period = ?**")
        q2 = st.radio("", ["2 years", "3 years", "4 years", "5 years"], key="m12q2")
        if st.button("Check Q2", key="m12c2"):
            if q2 == "4 years":
                st.success("✅ Correct! Payback = $120,000 / $30,000 = 4 years")
            else:
                st.error("❌ Incorrect. Payback = $120,000 / $30,000 = 4 years")

        st.markdown("---")
        st.markdown("**Q3. The main weakness of the Payback Period method is:**")
        q3 = st.radio("", [
            "It is too complex to calculate",
            "It ignores time value of money and cash flows after payback",
            "It always gives a shorter period than NPV",
            "It requires WACC as the discount rate"
        ], key="m12q3")
        if st.button("Check Q3", key="m12c3"):
            if q3 == "It ignores time value of money and cash flows after payback":
                st.success("✅ Correct! Payback ignores TVM and all cash flows after the payback point is reached.")
            else:
                st.error("❌ Incorrect. Payback's two main weaknesses are ignoring TVM and ignoring post-payback cash flows.")

        st.markdown("---")
        st.markdown("""
        **Q4. Depreciation is $50,000/year. Tax rate is 30%. 
        What is the annual depreciation tax shield?**
        """)
        q4 = st.radio("", ["$10,000", "$15,000", "$35,000", "$50,000"], key="m12q4")
        if st.button("Check Q4", key="m12c4"):
            if q4 == "$15,000":
                shield = 50000 * 0.30
                st.success(f"✅ Correct! Tax Shield = Depreciation × Tax Rate = $50,000 × 30% = ${shield:,.0f}")
            else:
                st.error("❌ Incorrect. Tax Shield = $50,000 × 30% = $15,000 (cash saved because depreciation reduces taxable income)")

        st.markdown("---")
        st.markdown("""
        **Q5. Projects A and B are mutually exclusive. 
        Project A: IRR = 25%, NPV = $30,000. Project B: IRR = 20%, NPV = $80,000.
        Which project should be chosen?**
        """)
        q5 = st.radio("", [
            "Project A — higher IRR means better return",
            "Project B — higher NPV means more value added",
            "Both — IRR and NPV agree",
            "Neither — need more information"
        ], key="m12q5")
        if st.button("Check Q5", key="m12c5"):
            if q5 == "Project B — higher NPV means more value added":
                st.success("✅ Correct! When mutually exclusive, ALWAYS use NPV. B adds $80K vs A's $30K — choose B!")
            else:
                st.error("❌ Incorrect. For mutually exclusive projects, NPV is the correct decision criterion. B has higher NPV ($80K vs $30K).")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Capital Budgeting Methods — Complete Reference")
        methods_df = pd.DataFrame({
            "Method": ["Payback Period", "Discounted Payback", "Net Present Value (NPV)",
                        "Internal Rate of Return (IRR)", "Profitability Index (PI)"],
            "Formula": [
                "Initial Investment / Annual CF (equal) or Cumulate CFs",
                "Cumulate discounted CFs until investment recovered",
                "Σ [CFt/(1+r)^t] − Initial Investment",
                "Rate r where NPV = 0",
                "PV of Future CFs / Initial Investment"
            ],
            "Accept if": ["Short payback", "Short discounted payback", "NPV > 0", "IRR > Required Return", "PI > 1"],
            "TVM?": ["❌", "✅", "✅", "✅", "✅"],
            "Best for": ["Quick screen", "Risk/liquidity", "Best — all decisions", "% return communication", "Capital rationing"]
        })
        st.dataframe(methods_df, use_container_width=True, hide_index=True)

        st.subheader("📌 After-Tax Cash Flow Formulas")
        st.markdown("""
        ```
        ─── Initial Investment ───
        Equipment cost + Installation + Working Capital − After-tax salvage of old equipment

        ─── Annual After-Tax Cash Flow (Method 1) ───
        Pre-tax Cash Flow × (1 − Tax Rate) + (Depreciation × Tax Rate)
        = After-Tax Operating CF + Depreciation Tax Shield

        ─── Annual After-Tax Cash Flow (Method 2) ───
        Net Income + Depreciation
        = [(Revenue − Costs − Dep) × (1−T)] + Dep

        ─── Depreciation Tax Shield ───
        Annual Depreciation × Tax Rate

        ─── Terminal Cash Flow ───
        After-Tax Salvage Value + Working Capital Recovery
        After-Tax Salvage = Salvage − (Salvage − Book Value) × Tax Rate
        ```
        """)

        st.subheader("🔍 Key Decision Rules")
        rules_df = pd.DataFrame({
            "Scenario": [
                "Single independent project",
                "Multiple independent projects (unlimited capital)",
                "Mutually exclusive projects",
                "Capital rationing (limited budget)",
                "IRR vs NPV conflict"
            ],
            "Best Method": ["NPV or IRR", "Accept all with NPV>0", "NPV (always!)", "PI ranking", "Use NPV"],
            "Rule": [
                "Accept if NPV>0 or IRR>Required Return",
                "Accept all positive NPV projects",
                "Choose highest NPV — not highest IRR",
                "Select highest PI projects until budget exhausted",
                "NPV maximizes shareholder wealth — trust it!"
            ]
        })
        st.dataframe(rules_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Using pre-tax cash flows instead of after-tax",
                "Forgetting the depreciation tax shield",
                "Ignoring working capital in initial investment",
                "Ignoring salvage value (or its tax effect)",
                "Using IRR to rank mutually exclusive projects",
                "Using book value instead of market value for old assets",
                "Including sunk costs in the analysis"
            ],
            "Correct Approach": [
                "Always use after-tax cash flows for NPV/IRR",
                "ATCF = Pretax CF × (1−T) + (Dep × T)",
                "Working capital is an initial outflow (recovered at end)",
                "Terminal CF = After-tax salvage + Working capital recovery",
                "Use NPV for mutually exclusive — IRR can mislead",
                "Opportunity cost = current market value, not book value",
                "Sunk costs already spent — irrelevant to future analysis"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 12 Complete! You can evaluate capital investments using all major methods with after-tax cash flows.")
        st.info("💡 Next: Module 13 — Pricing Decisions & Target Costing")

if __name__ == "__main__":
    show()