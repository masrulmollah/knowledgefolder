import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🎯 IFRS 2: Share-based Payment")
    st.markdown("*Master equity-settled, cash-settled and choice share-based transactions*")

    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Scope and Objective")
        st.markdown("""
        **IFRS 2** prescribes accounting for **share-based payment transactions** — transactions where the entity:
        - Receives goods or services in exchange for **equity instruments** (equity-settled), OR
        - Incurs liabilities based on the price of **equity instruments** (cash-settled)

        This includes employee share option plans, share purchase plans, share appreciation rights, and payments to suppliers in shares.

        **Fundamental principle:** Recognise the fair value of goods/services received. If FV of goods/services cannot be estimated, measure indirectly via FV of equity instruments granted.
        """)
        st.subheader("2. Equity-Settled Transactions")
        st.markdown("""
        **Measurement:** Fair value of equity instruments at the **grant date** (NOT exercise date or vesting date).

        **Recognition:**
        - Expense recognised over the **vesting period** (the period services are received)
        - Corresponding entry → **equity** (Share-based Payment Reserve)
        - Once recognised in equity → **never reversed**, even if options lapse unexercised

        **Market conditions** (e.g., share price targets):
        - Factored into the grant date fair value using option pricing models
        - Do NOT adjust the cumulative expense if market conditions are not met

        **Non-market conditions** (e.g., service conditions, EPS targets):
        - NOT factored into grant date FV
        - Adjust cumulative expense based on best estimate of number of instruments expected to vest
        """)
        st.subheader("3. Cash-Settled Transactions")
        st.markdown("""
        **Measurement:** Fair value of the **liability** at each balance sheet date (until settled).

        **Recognition:**
        - Expense recognised over vesting period
        - Corresponding entry → **liability**
        - Liability remeasured to fair value at **every balance sheet date** — changes in FV go to P&L
        - On settlement: liability derecognised, cash paid

        **Key difference from equity-settled:**
        | | Equity-Settled | Cash-Settled |
        |---|---|---|
        | Measurement date | Grant date (fixed) | Every balance sheet date (remeasured) |
        | Balance sheet entry | Equity reserve | Liability |
        | P&L after vesting | No further adjustment | Remeasurement to P&L until settled |
        """)
        st.subheader("4. Vesting Conditions")
        st.markdown("""
        | Condition Type | Factored into FV? | Adjust Expense If Not Met? |
        |---|---|---|
        | **Market condition** (share price target) | YES (in grant date FV) | NO |
        | **Non-market condition** (service, EPS) | NO | YES — adjust estimate of vesting numbers |
        | **Service condition** | NO | YES |
        | **Non-vesting condition** | YES (in grant date FV) | NO |
        """)
        st.subheader("5. Modifications, Cancellations and Settlements")
        st.markdown("""
        **Modification** — any change in terms/conditions after grant date:
        - If modification is **beneficial** to employee → recognise incremental fair value over remaining vesting period
        - If modification is **detrimental** → ignore the change; continue as if unmodified (cannot reduce expense)

        **Cancellation or settlement:**
        - Treat as accelerated vesting — recognise immediately any unrecognised grant date FV
        - Cash paid on settlement → deduct from equity reserve; any excess above equity reserve → P&L

        **Lapse of options (unexercised after vesting):**
        - Do NOT reverse the cumulative expense — it remains in equity
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Equity-Settled Share Options — Graded Vesting")
        st.markdown("""
        **Grant date:** 1 January 2022
        **Options granted:** 1,000 options per employee × 100 employees = 100,000 options
        **Exercise price:** $5.00 | **Fair value at grant date:** $2.50 per option
        **Vesting period:** 3 years (service condition — must remain employed)
        **Expected forfeitures:** 5% per year

        | Year | Cumulative Employees Expected to Vest | Cumulative Expense | Annual Expense |
        |---|---|---|---|
        | 2022 | 100 × 95% = 95 employees | 95×1,000×$2.50×1/3 = **$79,167** | $79,167 |
        | 2023 | 100 × 90% = 90 employees | 90×1,000×$2.50×2/3 = **$150,000** | $70,833 |
        | 2024 | Actual: 88 employees vested | 88×1,000×$2.50×3/3 = **$220,000** | $70,000 |

        **Journal Year 1:**
        ```
        Dr  Employee Expense (P&L)       $79,167
            Cr  Share-based Payment Reserve    $79,167
        ```
        """)
        st.subheader("Example 2: Cash-Settled — Share Appreciation Rights (SARs)")
        st.markdown("""
        **Grant:** 500 SARs to employee | **Service period:** 2 years
        - Year 1 FV per SAR: $3.00 → Liability = 500 × $3.00 × 1/2 = **$750**
        - Year 2 FV per SAR: $4.50 → Liability = 500 × $4.50 × 2/2 = **$2,250**
        - Year 2 P&L: $2,250 − $750 = **$1,500** (expense + remeasurement)
        - Settlement: Employee receives 500 × $4.50 = $2,250 cash

        ```
        Year 1: Dr Employee Expense $750 / Cr SAR Liability $750
        Year 2: Dr Employee Expense $1,500 / Cr SAR Liability $1,500
        Settlement: Dr SAR Liability $2,250 / Cr Cash $2,250
        ```
        """)
        st.subheader("Example 3: Market vs Non-Market Conditions")
        st.markdown("""
        **Options granted with TWO conditions:**
        1. Share price reaches $10 within 3 years (**market condition**)
        2. Employee serves 3 years (**service condition — non-market**)

        **Treatment:**
        - Market condition ($10 target): **built into the grant date FV** using a model (e.g., Monte Carlo)
        - Grant date FV (reflecting market condition): $1.80 per option
        - If share price never reaches $10 but employee serves 3 years → **still expense $1.80 per option** (market conditions do not adjust expense)
        - If employee leaves before 3 years → **reverse expense** (service condition not met)
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Tool 1: Equity-Settled Options — Annual Expense Calculator")
        col1, col2 = st.columns(2)
        with col1:
            n_employees = st.number_input("Employees granted options", value=100)
            options_each = st.number_input("Options per employee", value=1000)
            fv_grant = st.number_input("Fair value at grant date ($ per option)", value=2.50, step=0.10)
            vesting_yrs = st.number_input("Vesting period (years)", value=3, min_value=1, max_value=10)
            forfeiture_pct = st.number_input("Expected forfeiture per year (%)", value=5.0, step=0.5) / 100
        with col2:
            rows = []
            total_options = n_employees * options_each
            prev_cum = 0.0
            for yr in range(1, int(vesting_yrs) + 1):
                expected_remain = n_employees * ((1 - forfeiture_pct) ** yr)
                cum_expense = expected_remain * options_each * fv_grant * (yr / vesting_yrs)
                annual = cum_expense - prev_cum
                rows.append({"Year": yr, "Expected Employees": f"{expected_remain:.0f}", "Cumulative Expense ($)": f"{cum_expense:,.0f}", "Annual Expense ($)": f"{annual:,.0f}"})
                prev_cum = cum_expense
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            total_final = rows[-1]["Cumulative Expense ($)"]
            st.success(f"Total expense over vesting period: {total_final}")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Cash-Settled SAR Liability Calculator")
        sars = st.number_input("Number of SARs granted", value=500)
        vest_yrs_sar = st.number_input("Vesting period (years)", value=2, min_value=1, key="sar_vest")
        st.markdown("Enter fair value per SAR at each year-end:")
        fv_vals = []
        cols_sar = st.columns(int(vest_yrs_sar))
        for i, col in enumerate(cols_sar):
            fv = col.number_input(f"Year {i+1} FV ($)", value=3.0+i*1.5, step=0.5, key=f"sar_fv{i}")
            fv_vals.append(fv)
        if st.button("Calculate SAR Liability"):
            rows_sar = []
            prev_liab = 0.0
            for yr, fv in enumerate(fv_vals, 1):
                liability = sars * fv * (yr / vest_yrs_sar)
                expense = liability - prev_liab
                rows_sar.append({"Year": yr, "FV/SAR ($)": f"{fv:.2f}", "Cumulative Liability ($)": f"{liability:,.0f}", "P&L Expense/(Income) ($)": f"{expense:,.0f}"})
                prev_liab = liability
            st.dataframe(pd.DataFrame(rows_sar), use_container_width=True, hide_index=True)
            st.info(f"Settlement cash = ${sars * fv_vals[-1]:,.0f} (SARs × final FV)")

    with tab4:
        st.header("Visualizations")
        yrs = [1, 2, 3]
        eq_cum = [79167, 150000, 220000]
        eq_ann = [79167, 70833, 70000]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=yrs, y=eq_ann, name="Annual Expense", marker_color="#2563EB"))
        fig.add_trace(go.Scatter(x=yrs, y=eq_cum, name="Cumulative Expense", line=dict(color="#F59E0B", width=2), mode="lines+markers", yaxis="y2"))
        fig.update_layout(title="Equity-Settled Options — Annual and Cumulative Expense ($)", barmode="group",
                          yaxis=dict(title="Annual Expense ($)"), yaxis2=dict(title="Cumulative ($)", overlaying="y", side="right"), height=380)
        st.plotly_chart(fig, use_container_width=True)

        sar_yr = [1, 2]
        sar_liab = [750, 2250]
        sar_pl = [750, 1500]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=sar_yr, y=sar_pl, name="P&L Expense", marker_color="#F87171"))
        fig2.add_trace(go.Scatter(x=sar_yr, y=sar_liab, name="Liability Balance", line=dict(color="#2563EB", width=2), mode="lines+markers", yaxis="y2"))
        fig2.update_layout(title="Cash-Settled SARs — P&L Expense and Liability Balance ($)", yaxis=dict(title="Expense ($)"), yaxis2=dict(title="Liability ($)", overlaying="y", side="right"), height=350)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. For equity-settled share-based payments, fair value is measured at:**")
        q1 = st.radio("", ["Exercise date","Vesting date","Grant date","Each balance sheet date"], key="ifrs2q1")
        if st.button("Check Answer", key="ifrs2c1"):
            if q1 == "Grant date":
                st.success("✅ Correct! IFRS 2 equity-settled: fair value fixed at the GRANT DATE and never remeasured.")
            else:
                st.error("❌ Equity-settled = grant date FV (fixed). Cash-settled = remeasured at every balance sheet date.")
        st.markdown("---")
        st.markdown("**2. For cash-settled share-based payments, the liability is measured at:**")
        q2 = st.radio("", ["Grant date fair value (fixed)","Fair value at each balance sheet date until settled","Intrinsic value only","Exercise price × number of SARs"], key="ifrs2q2")
        if st.button("Check Answer", key="ifrs2c2"):
            if q2 == "Fair value at each balance sheet date until settled":
                st.success("✅ Correct! Cash-settled liabilities are remeasured to fair value at EVERY balance sheet date. Changes go to P&L.")
            else:
                st.error("❌ Cash-settled = remeasured at every balance sheet date until settlement.")
        st.markdown("---")
        st.markdown("**3. If share options lapse unexercised after vesting, the cumulative expense recognised is:**")
        q3 = st.radio("", ["Reversed back to zero","Transferred from equity reserve to retained earnings","Left in equity — never reversed","Transferred to P&L income"], key="ifrs2q3")
        if st.button("Check Answer", key="ifrs2c3"):
            if q3 == "Left in equity — never reversed":
                st.success("✅ Correct! IFRS 2 is clear: once expense is recognised in equity, it is NEVER reversed even if options lapse unexercised. The reserve may be transferred within equity.")
            else:
                st.error("❌ Lapsed options: cumulative expense stays in equity — NEVER reversed to P&L.")
        st.markdown("---")
        st.markdown("**4. A market condition (e.g., share price target) is treated by:**")
        q4 = st.radio("", ["Adjusting the number of options expected to vest","Factoring it into the grant date FV; not adjusting expense if not met","Recognising expense only if the condition is met","Excluding the options from IFRS 2 scope"], key="ifrs2q4")
        if st.button("Check Answer", key="ifrs2c4"):
            if q4 == "Factoring it into the grant date FV; not adjusting expense if not met":
                st.success("✅ Correct! Market conditions are built into the grant date FV (e.g., via Monte Carlo simulation). If market conditions are not met, the expense is NOT adjusted.")
            else:
                st.error("❌ Market conditions → built into grant date FV using option pricing model. Non-achievement does NOT adjust the cumulative expense.")
        st.markdown("---")
        st.markdown("**5. The journal entry for equity-settled share options expensed during vesting is:**")
        q5 = st.radio("", ["Dr Cash / Cr Share Capital","Dr Employee Expense / Cr Share-based Payment Reserve (equity)","Dr Employee Expense / Cr Liability","Dr Share-based Reserve / Cr P&L"], key="ifrs2q5")
        if st.button("Check Answer", key="ifrs2c5"):
            if q5 == "Dr Employee Expense / Cr Share-based Payment Reserve (equity)":
                st.success("✅ Correct! Dr Employee Expense (P&L) / Cr Share-based Payment Reserve (equity). This is the standard entry for equity-settled transactions over the vesting period.")
            else:
                st.error("❌ Equity-settled: Dr Employee Expense (P&L) / Cr Share-based Payment Reserve (equity).")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IFRS 2 — Two Types of SBP Transactions

| Feature | Equity-Settled | Cash-Settled |
|---|---|---|
| Measurement date | **Grant date** (fixed) | **Every balance sheet date** |
| Balance sheet | Equity reserve | **Liability** |
| Remeasurement | None | Yes — every year-end to P&L |
| Exercise/settlement | No further P&L | Cash paid, derecognise liability |

### Vesting Conditions
```
Market conditions → in grant date FV → expense NOT adjusted if not met
Non-market (service, EPS) → NOT in FV → adjust estimate of vesting numbers
```

### Key Entries
```
Equity-settled:  Dr Expense / Cr SBP Reserve (equity)
Cash-settled:    Dr Expense / Cr SAR Liability
Settlement cash: Dr SAR Liability / Cr Cash
Lapsed options:  NO reversal — leave in equity reserve
```

### Modification Rule
- Beneficial modification → recognise incremental FV
- Detrimental modification → ignore (continue as original)
        """)
        st.success("🎓 IFRS 2 Complete!")
        st.info("💡 Next: IFRS 3 — Business Combinations")

if __name__ == "__main__":
    show()