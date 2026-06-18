import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("\U0001f9fe IAS 12: Income Taxes")
    st.markdown("*Master current tax, deferred tax assets and liabilities, and the tax effects in financial statements*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "\U0001f4d6 Learn", "\U0001f9ee Examples", "\U0001f4a1 Interactive Tools",
        "\U0001f4ca Visualizations", "\u2705 Quiz", "\U0001f4dd Summary"
    ])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Objective")
        st.markdown("""
        IAS 12 prescribes the accounting treatment for **income taxes**, including both:
        - **Current tax** – the amount payable/refundable for the current period based on taxable profit
        - **Deferred tax** – future tax consequences of temporary differences between carrying amounts and tax bases
        """)

        st.subheader("2. Current Tax")
        st.markdown("""
        - Calculated using **tax rates enacted or substantively enacted** at the balance sheet date
        - Underpaid tax → **current tax liability**; overpaid → **current tax asset**
        - Recognise in P&L unless it relates to an OCI item or a business combination
        """)

        st.subheader("3. Temporary Differences — The Engine of Deferred Tax")
        st.markdown("**Temporary difference = Carrying Amount − Tax Base**")
        df = pd.DataFrame({
            "Difference Type": ["Taxable Temporary Difference", "Deductible Temporary Difference"],
            "Asset arises when": ["Carrying Amount > Tax Base", "Tax Base > Carrying Amount"],
            "Liability arises when": ["Tax Base > Carrying Amount", "Carrying Amount > Tax Base"],
            "Creates": ["Deferred Tax LIABILITY (DTL)", "Deferred Tax ASSET (DTA)"]
        })
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.subheader("4. Recognition Rules")
        st.markdown("""
        **DTL:** Recognise for ALL taxable temporary differences **EXCEPT:**
        - Initial recognition of goodwill
        - Initial recognition of asset/liability in a non-business combination transaction that affects neither accounting nor taxable profit

        **DTA:** Recognise only when it is **probable that sufficient future taxable profit** will be available to utilise the deductible difference.

        **Unused tax losses and credits:** Recognise DTA only to the extent recovery is probable.
        """)

        st.subheader("5. Measurement")
        st.markdown("""
        - Use **enacted (or substantively enacted) tax rates** expected to apply when the difference reverses
        - **Do NOT discount** deferred tax assets/liabilities
        - Tax rate changes → **remeasure DTA/DTL** through P&L (unless the underlying item was in OCI)
        """)

        st.subheader("6. Presentation")
        st.markdown("""
        - Current tax: separate line in P&L
        - Deferred tax: always **non-current**
        - Offset DTA and DTL only if: (1) legal right AND (2) same taxable entity AND same tax authority
        - Effective tax rate reconciliation: typically disclosed in notes
        """)

        st.subheader("7. Common Temporary Differences")
        examples_df = pd.DataFrame({
            "Source": ["Accelerated tax depreciation", "Warranty provision", "Development costs capitalised",
                       "Revaluation of PPE", "Tax loss carry-forward", "Unearned revenue (deferred income)"],
            "Carrying Amount vs Tax Base": ["CA > TB (asset)", "CA > TB (liability)", "CA > 0; TB = 0",
                                             "CA > TB (asset)", "No asset; future deduction", "CA > TB (liability)"],
            "Creates": ["DTL", "DTA", "DTL", "DTL", "DTA (if recoverable)", "DTA"]
        })
        st.dataframe(examples_df, use_container_width=True, hide_index=True)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Accelerated Tax Depreciation → DTL")
        st.markdown("""
        - Asset cost: **$100,000** | Accounting life: 5 years | Tax life: 2 years | Tax rate: 25%
        - **Year 1 accounting depreciation:** $100,000 ÷ 5 = $20,000 → Carrying amount = **$80,000**
        - **Year 1 tax depreciation:** $100,000 ÷ 2 = $50,000 → Tax base = **$50,000**
        - **Taxable temporary difference:** $80,000 − $50,000 = **$30,000**
        - **DTL = $30,000 × 25% = $7,500**

        Journal entry:
        ```
        Dr  Income Tax Expense (Deferred)   $7,500
            Cr  Deferred Tax Liability           $7,500
        ```
        """)

        st.subheader("Example 2: Warranty Provision → DTA")
        st.markdown("""
        - Warranty provision recognised: **$150,000** (tax deductible only when claims are paid)
        - Tax base of the provision liability = $0 (no amount is yet deductible)
        - Carrying amount of liability $150,000 > Tax base $0 → **deductible temporary difference**
        - **DTA = $150,000 × 25% = $37,500**

        Journal entry:
        ```
        Dr  Deferred Tax Asset   $37,500
            Cr  Income Tax Income (Deferred)   $37,500
        ```
        """)

        st.subheader("Example 3: Tax Loss Carry-Forward")
        st.markdown("""
        - Taxable loss in 2024: **$400,000**; future taxable profits probable: $300,000
        - DTA recognisable: **$300,000 × 25% = $75,000**
        - Remaining $100,000 loss → DTA NOT recognised (insufficient probable future profit)
        - If future profits improve, the unrecognised DTA is recognised prospectively
        """)

        st.subheader("Example 4: Tax Rate Change")
        st.markdown("""
        - DTA on warranty = $37,500 (recorded at 25%)
        - New tax rate substantively enacted: **20%**
        - Remeasured DTA = $150,000 × 20% = **$30,000**
        - Adjustment: **Dr Income Tax Expense $7,500 / Cr DTA $7,500** (recognised in P&L)
        """)

        st.subheader("Example 5: Effective Tax Rate Reconciliation")
        recon_df = pd.DataFrame({
            "Item": ["Profit before tax", "Tax at 25% (statutory)", "Non-deductible entertainment",
                     "Tax-exempt dividend income", "Rate change adjustment", "Total tax expense", "Effective tax rate"],
            "$000": ["1,000", "250", "8", "(5)", "12", "265", "26.5%"]
        })
        st.dataframe(recon_df, use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("\U0001f527 Tool 1: Deferred Tax Calculator")
        col1, col2 = st.columns(2)
        with col1:
            item_type = st.selectbox("Balance sheet item:", ["Asset", "Liability"], key="dt_it")
            carrying = st.number_input("Carrying Amount ($)", value=80000, step=1000, key="dt_ca")
            tax_base = st.number_input("Tax Base ($)", value=50000, step=1000, key="dt_tb")
            tax_rate_pct = st.number_input("Tax Rate (%)", value=25.0, step=0.5, key="dt_tr")
        with col2:
            tax_rate = tax_rate_pct / 100
            if item_type == "Asset":
                diff = carrying - tax_base
                if diff > 0:
                    st.error(f"**Deferred Tax LIABILITY**\nTaxable temporary difference: ${diff:,.0f}\nDTL = ${diff * tax_rate:,.0f}")
                elif diff < 0:
                    st.success(f"**Deferred Tax ASSET**\nDeductible temporary difference: ${abs(diff):,.0f}\nDTA = ${abs(diff) * tax_rate:,.0f}")
                else:
                    st.info("No temporary difference — no deferred tax required.")
            else:
                diff = carrying - tax_base
                if diff > 0:
                    st.success(f"**Deferred Tax ASSET**\nDeductible temporary difference: ${diff:,.0f}\nDTA = ${diff * tax_rate:,.0f}")
                elif diff < 0:
                    st.error(f"**Deferred Tax LIABILITY**\nTaxable temporary difference: ${abs(diff):,.0f}\nDTL = ${abs(diff) * tax_rate:,.0f}")
                else:
                    st.info("No temporary difference — no deferred tax required.")

        st.markdown("---")
        st.subheader("\U0001f527 Tool 2: Effective Tax Rate Reconciliation Builder")
        pbt = st.number_input("Profit Before Tax ($000)", value=1000, key="etr_pbt")
        stat_rate = st.number_input("Statutory Tax Rate (%)", value=25.0, key="etr_rate")
        non_ded = st.number_input("Non-deductible expenses ($000)", value=30, key="etr_nd")
        exempt = st.number_input("Tax-exempt income ($000)", value=20, key="etr_ex")
        rate_chg = st.number_input("Tax rate change adjustment ($000)", value=15, key="etr_rc")
        if st.button("Calculate Effective Tax Rate"):
            sr = stat_rate / 100
            standard_tax = pbt * sr
            total_tax = standard_tax + non_ded * sr - exempt * sr + rate_chg
            etr = (total_tax / pbt * 100) if pbt else 0
            result_df = pd.DataFrame({
                "Item": ["Profit before tax", f"Tax at {stat_rate:.0f}% (statutory)",
                         "Non-deductible expenses", "Tax-exempt income",
                         "Rate change adjustment", "Total tax expense", "Effective Tax Rate"],
                "$000": [f"{pbt:,}", f"{standard_tax:,.1f}", f"{non_ded*sr:,.1f}",
                         f"({exempt*sr:,.1f})", f"{rate_chg:,.1f}", f"{total_tax:,.1f}", f"{etr:.1f}%"]
            })
            st.dataframe(result_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("\U0001f527 Tool 3: DTA Recoverability Test")
        st.markdown("Assess whether a deferred tax asset can be recognised:")
        dta_amount = st.number_input("Gross DTA before recoverability ($000)", value=100)
        future_profit = st.number_input("Probable future taxable profit ($000)", value=300)
        existing_dtl = st.number_input("Existing DTL that can be offset ($000)", value=50)
        tax_r = st.number_input("Tax Rate (%)", value=25.0, key="dta_tr") / 100
        if st.button("Test Recoverability"):
            deductible_diff = dta_amount / tax_r
            available = future_profit * tax_r + existing_dtl * tax_r
            recognisable = min(dta_amount, available)
            unrecognised = max(0, dta_amount - recognisable)
            st.markdown(f"""
| Item | $000 |
|------|------|
| Gross DTA | {dta_amount:,} |
| Future taxable profit available | {future_profit:,} |
| DTA recoverable against future profit | {future_profit * tax_r:,.1f} |
| DTA recoverable against DTL | {existing_dtl * tax_r:,.1f} |
| **DTA Recognisable** | **{recognisable:,.1f}** |
| DTA NOT recognised | {unrecognised:,.1f} |
""")
            if unrecognised > 0:
                st.warning(f"${unrecognised:,.1f}k of DTA is NOT recognised — insufficient probable future taxable profit.")
            else:
                st.success("Full DTA can be recognised.")

    with tab4:
        st.header("Visualizations")
        st.subheader("Deferred Tax — How Temporary Differences Reverse")
        years = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
        acc_dep = [20, 20, 20, 20, 20]
        tax_dep = [50, 50, 0, 0, 0]
        dtl_bal = [7.5, 15, 10, 5, 0]

        fig = go.Figure()
        fig.add_trace(go.Bar(x=years, y=acc_dep, name="Accounting Depreciation", marker_color="#2563EB"))
        fig.add_trace(go.Bar(x=years, y=tax_dep, name="Tax Depreciation", marker_color="#F59E0B"))
        fig.add_trace(go.Scatter(x=years, y=dtl_bal, name="DTL Balance ($000)", yaxis="y2",
                                  line=dict(color="#EF4444", width=3), mode="lines+markers"))
        fig.update_layout(
            barmode="group", title="Accelerated Depreciation — DTL Build and Reversal",
            yaxis=dict(title="Depreciation ($000)"),
            yaxis2=dict(title="DTL Balance ($000)", overlaying="y", side="right"),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("DTA vs DTL — Common Sources")
        sources = ["Accelerated Tax Depr", "Warranty Provision", "Tax Losses", "PPE Revaluation", "Dev Costs Capitalised"]
        dta_vals = [0, 37.5, 75, 0, 0]
        dtl_vals = [7.5, 0, 0, 25, 12.5]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=sources, y=dta_vals, name="Deferred Tax Asset", marker_color="#34D399"))
        fig2.add_trace(go.Bar(x=sources, y=[-v for v in dtl_vals], name="Deferred Tax Liability", marker_color="#F87171"))
        fig2.update_layout(title="DTA vs DTL — Common Sources ($000)", barmode="relative",
                           yaxis_title="$000", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Accelerated tax depreciation results in:**")
        q1 = st.radio("", ["Deferred Tax Asset", "Deferred Tax Liability", "Current Tax Asset", "No deferred tax"], key="ias12q1")
        if st.button("Check Answer", key="ias12c1"):
            if q1 == "Deferred Tax Liability":
                st.success("✅ Correct! Accelerated depreciation means carrying amount > tax base (asset) → taxable temporary difference → DTL.")
            else:
                st.error("❌ Incorrect. Accelerated tax depreciation: carrying amount > tax base → DTL.")
        st.markdown("---")

        st.markdown("**2. A warranty provision of $200,000 (tax-deductible when paid) at 20% tax rate creates:**")
        q2 = st.radio("", ["DTL $40,000", "DTA $40,000", "No deferred tax", "DTL $160,000"], key="ias12q2")
        if st.button("Check Answer", key="ias12c2"):
            if q2 == "DTA $40,000":
                st.success("✅ Correct! Warranty liability CA $200k > Tax base $0 → deductible temp. difference → DTA = $200k × 20% = $40,000.")
            else:
                st.error("❌ Incorrect. Warranty provision: liability CA > tax base → deductible difference → DTA = $200,000 × 20% = $40,000.")
        st.markdown("---")

        st.markdown("**3. Deferred tax assets are recognised:**")
        q3 = st.radio("", ["Always for all deductible differences", "Only if probable future taxable profit is available",
                           "Only if approved by tax authorities", "Never — only DTLs are recognised"], key="ias12q3")
        if st.button("Check Answer", key="ias12c3"):
            if q3 == "Only if probable future taxable profit is available":
                st.success("✅ Correct! IAS 12 requires a recoverability test — DTAs are recognised only to the extent that future taxable profits are probable.")
            else:
                st.error("❌ Incorrect. DTAs require a probability test on future taxable profit availability.")
        st.markdown("---")

        st.markdown("**4. When a new tax rate is substantively enacted, deferred tax balances are:**")
        q4 = st.radio("", ["Left unchanged until effective date", "Remeasured through P&L",
                           "Remeasured through OCI always", "Disclosed only, no remeasurement"], key="ias12q4")
        if st.button("Check Answer", key="ias12c4"):
            if q4 == "Remeasured through P&L":
                st.success("✅ Correct! DTA/DTL are remeasured at the new enacted rate. Effect goes through P&L (unless the underlying item was through OCI).")
            else:
                st.error("❌ Incorrect. IAS 12 requires remeasurement at newly enacted rates — through P&L.")
        st.markdown("---")

        st.markdown("**5. Deferred tax on initial recognition of goodwill is:**")
        q5 = st.radio("", ["Recognised as DTL", "Recognised as DTA", "Prohibited", "Optional"], key="ias12q5")
        if st.button("Check Answer", key="ias12c5"):
            if q5 == "Prohibited":
                st.success("✅ Correct! IAS 12 specifically prohibits recognising deferred tax arising from the initial recognition of goodwill.")
            else:
                st.error("❌ Incorrect. Deferred tax on initial recognition of goodwill is PROHIBITED under IAS 12.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 12 — Key Rules

**Current Tax** = Taxable profit × Enacted tax rate

**Temporary Difference = Carrying Amount − Tax Base**

| Situation | Creates |
|-----------|---------|
| Asset: CA > TB | Taxable diff → **DTL** |
| Asset: TB > CA | Deductible diff → **DTA** |
| Liability: CA > TB | Deductible diff → **DTA** |
| Liability: TB > CA | Taxable diff → **DTL** |

**DTA Recognition:** Only when probable future taxable profit exists

**Measurement:** Enacted future tax rates — NO discounting

**Key Exceptions (no deferred tax):**
- Initial recognition of goodwill
- Initial recognition of asset/liability outside business combination affecting neither P&L

**Presentation:** Always non-current | Offset within same entity/jurisdiction

**Formula:**
```
DTL or DTA = Temporary Difference × Future Enacted Tax Rate
Tax Expense = Current Tax + Deferred Tax Expense/(Income)
ETR = Total Tax Expense / Profit Before Tax
```
        """)
        st.success("🎓 IAS 12 Complete!")
        st.info("💡 Next: IAS 16 — Property, Plant and Equipment")

if __name__ == "__main__":
    show()