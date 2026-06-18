import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏗️ IFRS 16: Leases")
    st.markdown("*Master lessee accounting for right-of-use assets, lease liabilities and lessor classification*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. The Single Lessee Accounting Model")
        st.markdown("""
        **IFRS 16's biggest change:** Eliminated the operating vs finance lease distinction for LESSEES. Almost ALL leases are now recognised **on-balance-sheet**.

        **A contract is (or contains) a lease if** it conveys the right to **control the use of an identified asset** for a period of time in exchange for consideration.

        **Right to control use requires BOTH:**
        - Right to obtain substantially all economic benefits from use of the asset
        - Right to direct the use of the asset
        """)

        st.subheader("2. Recognition Exemptions (Optional)")
        st.markdown("""
        Lessees MAY elect NOT to apply the on-balance-sheet model for:
        - **Short-term leases** (lease term ≤ 12 months, no purchase option) — expense on straight-line basis
        - **Low-value asset leases** (e.g., laptops, small office equipment — assessed when new, regardless of materiality to the lessee)

        These elections are made on a lease-by-lease basis (short-term) or by asset class (low-value).
        """)

        st.subheader("3. Initial Recognition — Lease Liability")
        st.markdown("""
        ```
        Lease Liability = PV of Lease Payments NOT yet paid, discounted at the
                          interest rate implicit in the lease (or incremental
                          borrowing rate if implicit rate not determinable)
        ```

        **Lease payments included:**
        - Fixed payments (less lease incentives receivable)
        - Variable payments that depend on an index/rate (e.g., CPI-linked)
        - Exercise price of purchase option (if reasonably certain to exercise)
        - Payments for termination penalties (if lease term reflects exercising termination option)
        - Residual value guarantees

        **Excluded:** Variable payments based on usage/performance NOT linked to an index (e.g., % of sales) — these are expensed as incurred.
        """)

        st.subheader("4. Initial Recognition — Right-of-Use (ROU) Asset")
        st.markdown("""
        ```
        ROU Asset = Initial Lease Liability
                  + Lease payments made at or before commencement (less incentives received)
                  + Initial direct costs incurred by lessee
                  + Estimated costs of dismantling/restoring (per IAS 37)
        ```
        """)

        st.subheader("5. Subsequent Measurement")
        st.markdown("""
        **Lease Liability:**
        - Increase by interest expense (effective interest method): Interest = Opening Liability × Discount Rate
        - Decrease by lease payments made
        - Remeasure upon lease modifications or reassessment of lease term/payments

        **ROU Asset:**
        - **Depreciate** over the SHORTER of useful life and lease term (or useful life if ownership transfers at end of lease)
        - Apply IAS 36 for impairment testing
        - Adjust for any remeasurement of the lease liability
        """)

        st.subheader("6. Lessor Accounting — Unchanged from IAS 17")
        st.markdown("""
        Lessors STILL classify leases as either:

        | Type | Criteria | Accounting |
        |---|---|---|
        | **Finance Lease** | Transfers substantially all risks/rewards of ownership | Derecognise asset; recognise net investment in lease (receivable) |
        | **Operating Lease** | Does NOT transfer substantially all risks/rewards | Keep asset on balance sheet; recognise lease income (typically straight-line) |

        **Indicators of a finance lease:** lease transfers ownership by end of term; bargain purchase option; lease term covers majority of asset's economic life; PV of payments ≈ substantially all of fair value; asset is specialised.
        """)

        st.subheader("7. Lease Modifications")
        st.markdown("""
        **Separate lease** if modification: (a) increases scope by adding right to use additional assets, AND (b) consideration increases commensurate with standalone price.

        **Otherwise**, remeasure the lease liability using a revised discount rate, and adjust the ROU asset by the same amount:
        - **Decrease in scope** → reduce ROU asset proportionately; recognise gain/loss on the decrease
        - **Other modifications** → adjust ROU asset for the full remeasurement amount (no P&L impact)
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Initial Recognition — Basic Lease")
        st.markdown("""
        **Lease terms:** 5-year lease of office space. Annual payments of $100,000 at the END of each year. Discount rate (incremental borrowing rate): 6%. Initial direct costs: $10,000.

        **Step 1 — Calculate Lease Liability (PV of payments):**

        | Year | Payment | Discount Factor (6%) | PV |
        |---|---|---|---|
        | 1 | $100,000 | 0.9434 | $94,340 |
        | 2 | $100,000 | 0.8900 | $89,000 |
        | 3 | $100,000 | 0.8396 | $83,960 |
        | 4 | $100,000 | 0.7921 | $79,210 |
        | 5 | $100,000 | 0.7473 | $74,730 |
        | **Total Lease Liability** | | | **$421,240** |

        **Step 2 — ROU Asset:**
        $421,240 (lease liability) + $10,000 (initial direct costs) = **$431,240**

        **Journal at commencement:**
        ```
        Dr  Right-of-Use Asset      $431,240
            Cr  Lease Liability          $421,240
            Cr  Cash (direct costs)       $10,000
        ```
        """)

        st.subheader("Example 2: Subsequent Measurement — Year 1")
        st.markdown("""
        **Continuing Example 1:**

        | Item | Calculation | Amount |
        |---|---|---|
        | Opening Lease Liability | | $421,240 |
        | + Interest Expense (6%) | $421,240 × 6% | $25,274 |
        | − Lease Payment | | ($100,000) |
        | **Closing Lease Liability** | | **$346,514** |

        | Item | Calculation | Amount |
        |---|---|---|
        | ROU Asset (Opening) | | $431,240 |
        | Depreciation (5-year SL) | $431,240 / 5 | ($86,248) |
        | **Closing ROU Asset** | | **$344,992** |

        **P&L Impact Year 1:** Depreciation $86,248 + Interest $25,274 = **$111,522** total expense
        (Compare to old operating lease treatment: straight-line $100,000/year — IFRS 16 front-loads expense recognition)
        """)

        st.subheader("Example 3: Short-Term Lease Exemption")
        st.markdown("""
        **Lease of photocopier:** 9-month term, no purchase/renewal option, monthly payments of $500.

        **Election:** Short-term lease exemption applied (≤12 months)

        **Accounting:** Expense $500/month on a straight-line basis — NO ROU asset, NO lease liability recognised.

        ```
        Dr  Lease Expense (P&L)    $500
            Cr  Cash                   $500
        ```
        """)

        st.subheader("Example 4: Lease Modification — Decrease in Scope")
        st.markdown("""
        Original lease: 10,000 sq ft office, remaining lease liability $800,000, remaining ROU asset $750,000.

        Lessee renegotiates to reduce space to 6,000 sq ft (40% reduction) — partial termination.

        **Step 1:** Reduce ROU asset proportionately: $750,000 × 40% = $300,000 reduction → ROU asset = $450,000

        **Step 2:** Calculate new lease liability based on revised payments and rate = $480,000 (example)

        **Step 3:** Gain/loss on partial termination:
        | | $ |
        |---|---|
        | Decrease in lease liability | $800,000 − $480,000 = $320,000 |
        | Decrease in ROU asset | $300,000 |
        | **Gain on partial termination → P&L** | **$20,000** |
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Lease Liability and ROU Asset Calculator")
        col1, col2 = st.columns(2)
        with col1:
            annual_payment = st.number_input("Annual Lease Payment ($)", value=100000, step=5000)
            lease_term = st.number_input("Lease Term (years)", value=5, min_value=1, max_value=30)
            discount_rate_lease = st.number_input("Discount Rate (%)", value=6.0, step=0.5) / 100
            initial_direct_costs = st.number_input("Initial Direct Costs ($)", value=10000, step=1000)
        with col2:
            rows_lease = []
            total_pv = 0
            for yr in range(1, int(lease_term) + 1):
                df_lease = 1 / (1 + discount_rate_lease)**yr
                pv = annual_payment * df_lease
                total_pv += pv
                rows_lease.append({"Year": yr, "Payment ($)": f"{annual_payment:,.0f}", "Discount Factor": f"{df_lease:.4f}", "PV ($)": f"{pv:,.0f}"})
            st.dataframe(pd.DataFrame(rows_lease), use_container_width=True, hide_index=True)
            rou_asset_calc = total_pv + initial_direct_costs
            st.success(f"**Lease Liability = ${total_pv:,.0f}**\n\n**ROU Asset = ${total_pv:,.0f} + ${initial_direct_costs:,.0f} = ${rou_asset_calc:,.0f}**")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Amortisation Schedule — Lease Liability and ROU Asset")
        if st.button("Generate Full Amortisation Schedule"):
            schedule = []
            liability = total_pv
            rou = rou_asset_calc
            annual_depr_lease = rou_asset_calc / lease_term
            for yr in range(1, int(lease_term) + 1):
                interest = liability * discount_rate_lease
                closing_liability = liability + interest - annual_payment
                rou -= annual_depr_lease
                schedule.append({
                    "Year": yr,
                    "Opening Liability": f"{liability:,.0f}",
                    "Interest": f"{interest:,.0f}",
                    "Payment": f"({annual_payment:,.0f})",
                    "Closing Liability": f"{closing_liability:,.0f}",
                    "ROU Asset (Closing)": f"{max(0,rou):,.0f}"
                })
                liability = closing_liability
            st.dataframe(pd.DataFrame(schedule), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Short-Term/Low-Value Exemption Checker")
        lease_term_months = st.number_input("Lease term (months)", value=9, min_value=1, max_value=240)
        has_purchase_option = st.checkbox("Contains a purchase option?")
        is_low_value = st.checkbox("Asset is low-value when new (e.g., <$5,000)?")

        if st.button("Check Exemption Eligibility"):
            if lease_term_months <= 12 and not has_purchase_option:
                st.success("✅ **SHORT-TERM LEASE EXEMPTION available** — May elect to expense on a straight-line basis. No ROU asset/liability required.")
            elif is_low_value:
                st.success("✅ **LOW-VALUE ASSET EXEMPTION available** — May elect to expense on a straight-line basis. No ROU asset/liability required.")
            else:
                st.error("❌ **NO EXEMPTION available** — Must recognise ROU asset and lease liability under the standard IFRS 16 model.")

    with tab4:
        st.header("Visualizations")

        st.subheader("Lease Liability Amortisation Over Time")
        liab_path = [421240]
        rou_path = [431240]
        for yr in range(5):
            interest = liab_path[-1] * 0.06
            liab_path.append(liab_path[-1] + interest - 100000)
            rou_path.append(rou_path[-1] - 431240/5)
        years_plot = list(range(0, 6))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years_plot, y=liab_path, name="Lease Liability", line=dict(color="#F87171", width=2), mode="lines+markers"))
        fig.add_trace(go.Scatter(x=years_plot, y=rou_path, name="ROU Asset", line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig.update_layout(title="Lease Liability and ROU Asset — 5-Year Amortisation", xaxis_title="Year", yaxis_title="Balance ($)", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Expense Pattern — IFRS 16 (Front-Loaded) vs Old Operating Lease (Straight-Line)")
        years_exp = [1, 2, 3, 4, 5]
        ifrs16_expense = [111522, 107657, 103516, 99077, 94318]  # illustrative declining pattern
        old_opex_expense = [100000, 100000, 100000, 100000, 100000]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=years_exp, y=ifrs16_expense, name="IFRS 16 (Depreciation + Interest)", marker_color="#F59E0B"))
        fig2.add_trace(go.Bar(x=years_exp, y=old_opex_expense, name="Old Operating Lease (Straight-Line)", marker_color="#94A3B8"))
        fig2.update_layout(barmode="group", title="Total P&L Expense Pattern — IFRS 16 vs Old Operating Lease Treatment", yaxis_title="Annual Expense ($)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IFRS 16, lessees must recognise on the balance sheet:**")
        q1 = st.radio("", ["Only finance leases", "Only operating leases", "Almost all leases (right-of-use asset and lease liability), with limited exemptions", "No leases — all are expensed"], key="ifrs16q1")
        if st.button("Check Answer", key="ifrs16c1"):
            if q1 == "Almost all leases (right-of-use asset and lease liability), with limited exemptions":
                st.success("✅ Correct! IFRS 16 eliminated the operating/finance lease distinction for LESSEES — almost all leases go on-balance-sheet, with exemptions only for short-term and low-value leases.")
            else:
                st.error("❌ IFRS 16 requires ON-BALANCE-SHEET treatment for almost ALL lessee leases (limited exemptions for short-term/low-value).")

        st.markdown("---")
        st.markdown("**2. The lease liability is initially measured at:**")
        q2 = st.radio("", ["The total of all undiscounted lease payments", "The present value of lease payments not yet paid, discounted at the appropriate rate", "Fair value of the underlying asset", "Zero — recognised only when payments are made"], key="ifrs16q2")
        if st.button("Check Answer", key="ifrs16c2"):
            if q2 == "The present value of lease payments not yet paid, discounted at the appropriate rate":
                st.success("✅ Correct! Lease liability = PV of remaining lease payments, discounted at the rate implicit in the lease (or incremental borrowing rate).")
            else:
                st.error("❌ Lease liability = DISCOUNTED present value of future payments, not the undiscounted total or fair value of the asset.")

        st.markdown("---")
        st.markdown("**3. The right-of-use asset is depreciated over:**")
        q3 = st.radio("", ["Always the useful life of the underlying asset", "Always the lease term", "The shorter of useful life and lease term (or useful life if ownership transfers)", "Never depreciated — only tested for impairment"], key="ifrs16q3")
        if st.button("Check Answer", key="ifrs16c3"):
            if q3 == "The shorter of useful life and lease term (or useful life if ownership transfers)":
                st.success("✅ Correct! ROU assets are depreciated over the SHORTER of useful life and lease term, UNLESS ownership transfers at the end of the lease (then use useful life).")
            else:
                st.error("❌ Depreciation period = SHORTER of useful life or lease term (exception: useful life if ownership transfers at lease end).")

        st.markdown("---")
        st.markdown("**4. Lessor accounting under IFRS 16 for the classification of leases:**")
        q4 = st.radio("", ["Was eliminated, like lessee accounting", "Remains UNCHANGED from the old finance/operating lease distinction", "Now requires all leases to be treated as finance leases", "Now requires all leases to be treated as operating leases"], key="ifrs16q4")
        if st.button("Check Answer", key="ifrs16c4"):
            if q4 == "Remains UNCHANGED from the old finance/operating lease distinction":
                st.success("✅ Correct! Unlike the lessee model, LESSOR accounting under IFRS 16 retained the dual classification model (finance lease vs operating lease) essentially unchanged from IAS 17.")
            else:
                st.error("❌ Lessor accounting RETAINED the finance/operating lease distinction — only LESSEE accounting was fundamentally changed.")

        st.markdown("---")
        st.markdown("**5. A 9-month lease with no purchase option qualifies for:**")
        q5 = st.radio("", ["Mandatory on-balance-sheet treatment", "The short-term lease exemption (optional)", "Automatic classification as a finance lease", "No accounting treatment is required"], key="ifrs16q5")
        if st.button("Check Answer", key="ifrs16c5"):
            if q5 == "The short-term lease exemption (optional)":
                st.success("✅ Correct! Leases with a term of 12 months or less (and no purchase option) qualify for the SHORT-TERM LEASE EXEMPTION — an OPTIONAL election to expense on a straight-line basis.")
            else:
                st.error("❌ ≤12-month leases without purchase options qualify for the OPTIONAL short-term lease exemption.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Single Lessee Model
        Almost ALL leases → on-balance-sheet (ROU asset + lease liability)

        **Exemptions (optional):** Short-term leases (≤12 months) | Low-value assets

        ### 2. Initial Recognition
        ```
        Lease Liability = PV of remaining lease payments (discounted at implicit or IBR)

        ROU Asset = Lease Liability
                  + Payments made at/before commencement
                  + Initial direct costs
                  + Restoration costs (IAS 37)
        ```

        ### 3. Subsequent Measurement
        | | Lease Liability | ROU Asset |
        |---|---|---|
        | Increases by | Interest expense | — |
        | Decreases by | Payments made | Depreciation |
        | Period | Effective interest method | Shorter of useful life/lease term |

        ### 4. Lessor Accounting (Unchanged)
        | Type | Treatment |
        |---|---|
        | Finance Lease | Derecognise asset; recognise net investment receivable |
        | Operating Lease | Keep asset; recognise lease income (typically straight-line) |

        ### 5. Modifications
        - Scope increase + commensurate price → separate new lease
        - Otherwise → remeasure liability + adjust ROU asset
        - Scope decrease → partial derecognition + gain/loss
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Lessee: Almost ALL leases on-balance-sheet (exemptions: short-term ≤12mo, low-value)
Lease Liability = PV of remaining payments
ROU Asset = Lease Liability + upfront payments + direct costs + restoration costs
ROU Depreciation = SHORTER of useful life or lease term
Lessor accounting UNCHANGED: still Finance vs Operating Lease classification
        """)

        st.success("🎓 **IFRS 16 Complete!** You can now calculate lease liabilities and ROU assets, build amortisation schedules, and apply lessor classification.")
        st.info("💡 **Next**: IFRS 17 — Insurance Contracts")

if __name__ == "__main__":
    show()