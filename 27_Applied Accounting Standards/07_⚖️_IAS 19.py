import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("👥 IAS 19: Employee Benefits")
    st.markdown("*Master short-term benefits, defined contribution, defined benefit plans and termination benefits*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Categories of Employee Benefits")
        cats = pd.DataFrame({
            "Category": ["Short-term benefits","Post-employment: Defined Contribution","Post-employment: Defined Benefit","Other long-term benefits","Termination benefits"],
            "Examples": ["Wages, salaries, annual leave, sick pay, bonuses","Company pays fixed contributions to pension fund","Company promises a pension based on salary/service","Long-service leave, sabbaticals","Redundancy payments, involuntary termination"],
            "Accounting": ["Accrue as obligation; recognise expense when service rendered","Expense contribution when due; no further obligation","Complex actuarial calculations; DBO − Plan assets","Similar to defined benefit","Recognise when demonstrably committed"]
        })
        st.dataframe(cats, use_container_width=True, hide_index=True)

        st.subheader("2. Defined Contribution Plans")
        st.markdown("""
- Entity pays **fixed contributions** to a separate fund
- Entity has **no further legal/constructive obligation** once contributions are paid
- Risk borne entirely by the **employee**
- Accounting: **Expense the contribution** as the employee renders service
- Simple — no actuarial assumptions needed
        """)

        st.subheader("3. Defined Benefit Plans — Full Framework")
        st.markdown("""
**The entity bears the actuarial and investment risk.**

**Balance Sheet Position:**
```
Net Defined Benefit Liability (Asset) = 
    Defined Benefit Obligation (DBO) − Fair Value of Plan Assets
```

**Three components recognised in the period:**

| Component | Recognised In |
|-----------|---------------|
| **Service cost** (current + past + gains/losses on settlement) | P&L |
| **Net interest** (Net DBO/Asset × discount rate) | P&L |
| **Remeasurements** (actuarial gains/losses + return on plan assets exc. interest) | **OCI (never recycled)** |

**Actuarial assumptions:** discount rate (high-quality corporate bond rate), salary growth, mortality, staff turnover.

**Discount rate:** Use yield on high-quality corporate bonds (or government bonds where no deep market).
        """)

        st.subheader("4. Short-Term Benefits — Accumulating Compensated Absences")
        st.markdown("""
**Accumulating leave** (e.g., annual leave that carries forward): accrue as earned — recognise a liability
for unused entitlement at balance sheet date.

**Non-accumulating leave** (e.g., maternity — lapses if not taken): recognise only when the absence occurs.
        """)

        st.subheader("5. Termination Benefits")
        st.markdown("""
Recognise when the entity is **demonstrably committed** to either:
- Terminate employment before normal retirement date, OR
- Provide termination benefits as a result of an offer to encourage voluntary redundancy

If expected to be settled more than 12 months after reporting period → discount to present value.
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Defined Contribution — Accounting")
        st.markdown("""
**Company contributes 5% of salary to pension fund. Total salaries: $2,000,000.**

Pension contribution = $2,000,000 × 5% = **$100,000**

```
Dr  Pension Expense (P&L)   $100,000
    Cr  Cash / Payable           $100,000
```
No further obligation. Plan assets and actuarial risk belong to the employee.
        """)

        st.subheader("Example 2: Defined Benefit — Net DBO Calculation")
        st.markdown("""
| Item | $000 |
|---|---|
| Defined Benefit Obligation (DBO) at year-end | 5,200 |
| Fair Value of Plan Assets at year-end | (4,800) |
| **Net DB Liability (Balance Sheet)** | **400** |

Components in P&L:
| Item | $000 |
|---|---|
| Current Service Cost | 280 |
| Net Interest (net DBO × discount rate 5%) = $400k × 5% | 20 |
| **Total P&L charge** | **300** |

OCI:
| Item | $000 |
|---|---|
| Actuarial loss on DBO | 80 |
| Return on plan assets (exc. interest) | (30) |
| **Net Remeasurement in OCI** | **50** (loss) |
        """)

        st.subheader("Example 3: Movement in Net DBO")
        st.markdown("""
| | DBO ($000) | Plan Assets ($000) | Net Liability ($000) |
|-|---|---|---|
| Opening balance | 4,800 | 4,500 | 300 |
| Current service cost | 280 | — | 280 |
| Interest (5%) | 240 | 225 | 15 |
| Contributions paid | — | 200 | (200) |
| Benefits paid | (200) | (200) | — |
| Actuarial losses (remeasurement) | 80 | (30) | 110 |
| **Closing balance** | **5,200** | **4,695** | **505** |
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Tool 1: Defined Benefit Obligation — P&L vs OCI Split")
        col1,col2 = st.columns(2)
        with col1:
            opening_ndbo = st.number_input("Opening Net DBO ($000)", value=300)
            curr_svc = st.number_input("Current Service Cost ($000)", value=280)
            disc_rate = st.number_input("Discount Rate (%)", value=5.0) / 100
            actuarial_loss = st.number_input("Actuarial Loss on DBO ($000)", value=80)
            asset_return_exc = st.number_input("Excess Return on Plan Assets ($000, positive=gain)", value=30)
        with col2:
            net_interest = opening_ndbo * disc_rate
            pl_charge = curr_svc + net_interest
            oci_remeasure = actuarial_loss - asset_return_exc
            st.markdown(f"""
**P&L:**
| Item | $000 |
|---|---|
| Current Service Cost | {curr_svc:,.1f} |
| Net Interest on DBO | {net_interest:,.1f} |
| **Total P&L charge** | **{pl_charge:,.1f}** |

**OCI (non-recyclable):**
| Item | $000 |
|---|---|
| Actuarial loss on DBO | {actuarial_loss:,.1f} |
| Return on assets (exc. interest) | ({asset_return_exc:,.1f}) |
| **Net OCI remeasurement** | **{oci_remeasure:,.1f}** |
""")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Leave Accrual Calculator")
        employees = st.number_input("Number of employees", value=100)
        annual_leave = st.number_input("Annual leave entitlement (days/year)", value=20)
        leave_taken = st.number_input("Average days taken in year", value=15.0)
        daily_salary = st.number_input("Average daily salary ($)", value=500)
        if st.button("Calculate Leave Accrual"):
            unused = annual_leave - leave_taken
            accrual = employees * unused * daily_salary
            st.success(f"Unused leave: {unused} days/employee\n\nTotal leave liability: **${accrual:,.0f}**")

    with tab4:
        st.header("Visualizations")
        st.subheader("DB Plan — DBO vs Plan Assets Over Time")
        years = ["2020","2021","2022","2023","2024"]
        dbo = [4000, 4300, 4600, 4900, 5200]
        plan_assets = [3800, 4000, 4200, 4500, 4800]
        net_liab = [d-a for d,a in zip(dbo, plan_assets)]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=years, y=dbo, name="DBO", marker_color="#F87171"))
        fig.add_trace(go.Bar(x=years, y=plan_assets, name="Plan Assets", marker_color="#34D399"))
        fig.add_trace(go.Scatter(x=years, y=net_liab, name="Net Liability", line=dict(color="#2563EB",width=3), mode="lines+markers", yaxis="y2"))
        fig.update_layout(barmode="group", title="Defined Benefit — DBO vs Plan Assets ($000)", height=420,
                          yaxis=dict(title="$000"), yaxis2=dict(title="Net Liability", overlaying="y", side="right"))
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("P&L vs OCI — DB Cost Breakdown")
        fig2 = go.Figure(go.Pie(
            labels=["Current Service Cost","Net Interest","Actuarial Remeasurement (OCI)","Excess Return OCI"],
            values=[280, 20, 80, 30],
            hole=0.4,
            marker_colors=["#2563EB","#10B981","#F59E0B","#34D399"]
        ))
        fig2.update_layout(title="DB Cost Components — P&L vs OCI Split", height=350)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. In a defined contribution plan, who bears the investment risk?**")
        q1 = st.radio("", ["The employer","The employee","Both equally","The pension fund trustee"], key="ias19q1")
        if st.button("Check", key="c19_1"):
            if q1 == "The employee":
                st.success("✅ Correct! In a DC plan, the employer's obligation ends when contributions are paid. The employee bears all investment and actuarial risk.")
            else:
                st.error("❌ In a DC plan, the EMPLOYEE bears the risk. The employer's only obligation is to pay the fixed contribution.")
        st.markdown("---")
        st.markdown("**2. Actuarial gains and losses (remeasurements) on defined benefit plans are recognised in:**")
        q2 = st.radio("", ["P&L immediately","OCI and subsequently recycled to P&L","OCI and NEVER recycled","Deferred and amortised (corridor method)"], key="ias19q2")
        if st.button("Check", key="c19_2"):
            if q2 == "OCI and NEVER recycled":
                st.success("✅ Correct! IAS 19 remeasurements go to OCI permanently — they are NEVER reclassified to P&L. This is a non-recyclable OCI item.")
            else:
                st.error("❌ Under current IAS 19, remeasurements go to OCI and are NEVER recycled to P&L (the corridor method was eliminated).")
        st.markdown("---")
        st.markdown("**3. Net interest on the defined benefit net liability is calculated using:**")
        q3 = st.radio("", ["Expected return on plan assets","Discount rate applied to the net DBO/asset","Actual return on plan assets","Actuarial expected rate"], key="ias19q3")
        if st.button("Check", key="c19_3"):
            if q3 == "Discount rate applied to the net DBO/asset":
                st.success("✅ Correct! Net interest = Opening net DBO/asset × discount rate (high-quality corporate bond yield). This replaces the old 'expected return on plan assets'.")
            else:
                st.error("❌ Net interest = Opening net DBO × discount rate. IAS 19 uses one rate (discount rate) for both DBO and plan assets.")
        st.markdown("---")
        st.markdown("**4. Termination benefits are recognised when:**")
        q4 = st.radio("", ["Employees are actually terminated","The entity is demonstrably committed to termination","Board approves the plan","When paid to employees"], key="ias19q4")
        if st.button("Check", key="c19_4"):
            if q4 == "The entity is demonstrably committed to termination":
                st.success("✅ Correct! Termination benefits are recognised when the entity is demonstrably committed to a formal plan to terminate employment.")
            else:
                st.error("❌ Termination benefits are recognised when the entity is demonstrably committed — before actual termination occurs.")
        st.markdown("---")
        st.markdown("**5. The discount rate for measuring DB obligations uses:**")
        q5 = st.radio("", ["Expected return on plan assets","Government bond yields always","High-quality corporate bond yields (or government bonds where no deep market exists)","Central bank policy rate"], key="ias19q5")
        if st.button("Check", key="c19_5"):
            if q5 == "High-quality corporate bond yields (or government bonds where no deep market exists)":
                st.success("✅ Correct! IAS 19 requires the discount rate to reference high-quality corporate bonds. Where no deep corporate bond market exists, use government bond yields.")
            else:
                st.error("❌ IAS 19 requires using yields on high-quality corporate bonds (AA-rated) or government bonds where no deep market exists.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 19 — Four Categories of Benefits

| Category | Key Accounting Rule |
|---|---|
| Short-term | Accrue as service rendered |
| Defined Contribution | Expense fixed contribution when due; no further obligation |
| Defined Benefit | Net DBO − Plan Assets; 3-component recognition |
| Termination | Recognise when demonstrably committed |

### Defined Benefit — Three Cost Components

| Component | Where Recognised |
|---|---|
| Service cost (current + past) | P&L |
| Net interest on net DBO | P&L |
| Remeasurements (actuarial + excess asset return) | OCI (NEVER recycled) |

### Key Formula
```
Net DB Liability = DBO − Fair Value of Plan Assets
Net Interest = Opening Net Liability × Discount Rate
Discount Rate = Yield on high-quality corporate bonds
```
        """)
        st.success("🎓 IAS 19 Complete!")
        st.info("💡 Next: IAS 20 — Government Grants")

if __name__ == "__main__":
    show()