import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show():
    st.title("💰 IAS 23: Borrowing Costs")
    st.markdown("*Master capitalisation of borrowing costs on qualifying assets*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Core Principle")
        st.markdown("""
**Borrowing costs that are directly attributable to the acquisition, construction or production of a qualifying asset MUST be capitalised as part of the cost of that asset.**

All other borrowing costs are expensed as incurred.

*Note: This is a mandatory requirement — there is no choice under IAS 23.*
        """)
        st.subheader("2. Qualifying Asset")
        st.markdown("""
A **qualifying asset** is an asset that necessarily takes a **substantial period of time** to get ready for its intended use or sale.

**Examples of qualifying assets:**
- Manufacturing plants under construction
- Power generation facilities
- Investment property under development
- Inventories requiring substantial production periods (e.g., whisky, wine)
- Intangible assets developed internally

**NOT qualifying assets:**
- Assets routinely manufactured (short production cycle)
- Assets already ready for intended use or sale when acquired
- Financial assets
        """)
        st.subheader("3. Borrowing Costs Eligible for Capitalisation")
        st.markdown("""
| Type | Eligible? |
|---|---|
| Interest expense (effective interest method per IFRS 9) | ✅ Yes |
| Amortisation of discount/premium on borrowings | ✅ Yes |
| Finance charges on lease liabilities (IFRS 16) | ✅ Yes |
| Exchange differences on foreign currency borrowings (to extent they are an adjustment to interest) | ✅ Yes |

**Borrowing costs NOT eligible:**
- General administrative costs
- Dividend payments
        """)
        st.subheader("4. Commencement, Suspension and Cessation")
        st.markdown("""
**Commence capitalisation when ALL three conditions are met:**
1. Expenditures on the asset are being incurred
2. Borrowing costs are being incurred
3. Activities to prepare the asset for use/sale are in progress

**Suspend capitalisation** during extended periods of active development suspension (exclude interruptions for normal technical delays).

**Cease capitalisation** when substantially all activities necessary to prepare the asset are complete.
        """)
        st.subheader("5. Specific vs General Borrowings")
        st.markdown("""
**Specific borrowing:** Borrowed specifically for the asset
- Capitalise actual borrowing costs less any investment income earned on temporary investments

**General borrowings:** No specific loan for the asset
- Apply a **capitalisation rate** (weighted average cost of general borrowings) to expenditures on qualifying assets
- Capitalisation rate = Weighted average interest rate of outstanding general borrowings during the period
- Amount capitalised ≤ actual borrowing costs incurred in the period
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Specific Borrowing")
        st.markdown("""
- Loan of **$5,000,000** at 8% specifically to build a factory
- Construction period: 18 months
- During construction, $500,000 was temporarily invested at 3% for 6 months

| Item | Amount |
|---|---|
| Gross interest (8% × $5M × 18/12) | $600,000 |
| Less: Investment income (3% × $500k × 6/12) | ($7,500) |
| **Borrowing costs to capitalise** | **$592,500** |
        """)
        st.subheader("Example 2: General Borrowings — Capitalisation Rate")
        st.markdown("""
Entity has two outstanding loans (not specific to any qualifying asset):

| Loan | Balance | Interest Rate | Annual Interest |
|---|---|---|---|
| Bank Loan A | $10,000,000 | 6% | $600,000 |
| Bank Loan B | $5,000,000 | 8% | $400,000 |
| **Total** | **$15,000,000** | | **$1,000,000** |

**Capitalisation rate = $1,000,000 / $15,000,000 = 6.67%**

Expenditure on qualifying asset during period = $3,000,000
**Borrowing costs to capitalise = $3,000,000 × 6.67% = $200,000**

Check: $200,000 ≤ $1,000,000 (total borrowing costs) ✅
        """)
        st.subheader("Example 3: Suspension of Capitalisation")
        st.markdown("""
- Building under construction from Jan to Dec
- From May to August: construction halted due to contractor dispute (NOT a normal delay)
- Capitalise: Jan–Apr + Sep–Dec (8 months)
- Suspend: May–Aug (4 months) — borrowing costs expensed during suspension

*Normal technical delays (e.g., concrete curing time) do NOT trigger suspension.*
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Borrowing Cost Capitalisation Calculator")
        borrowing_type = st.radio("Borrowing type:", ["Specific Borrowing","General Borrowings"], key="ias23type")
        if borrowing_type == "Specific Borrowing":
            col1, col2 = st.columns(2)
            with col1:
                loan_amount = st.number_input("Loan Amount ($)", value=5000000, step=100000)
                rate = st.number_input("Interest Rate (%)", value=8.0) / 100
                months = st.number_input("Construction Period (months)", value=18, min_value=1)
            with col2:
                temp_inv = st.number_input("Temporarily Invested Amount ($)", value=500000, step=10000)
                inv_rate = st.number_input("Investment Return (%)", value=3.0) / 100
                inv_months = st.number_input("Investment Period (months)", value=6, min_value=0)
            gross_interest = loan_amount * rate * months / 12
            inv_income = temp_inv * inv_rate * inv_months / 12
            net_cap = gross_interest - inv_income
            st.markdown(f"""
| Item | Amount |
|---|---|
| Gross borrowing costs | ${gross_interest:,.0f} |
| Less: temporary investment income | (${inv_income:,.0f}) |
| **Borrowing costs to CAPITALISE** | **${net_cap:,.0f}** |
""")
        else:
            st.markdown("Enter your general borrowings:")
            n_loans = st.number_input("Number of loans", value=2, min_value=1, max_value=5)
            total_bal = 0; total_int = 0
            for i in range(int(n_loans)):
                c1,c2 = st.columns(2)
                bal = c1.number_input(f"Loan {i+1} Balance ($)", value=10000000, key=f"lb{i}")
                rt = c2.number_input(f"Loan {i+1} Rate (%)", value=6.0, key=f"lr{i}")
                total_bal += bal; total_int += bal * rt / 100
            cap_rate = total_int / total_bal if total_bal > 0 else 0
            expenditure = st.number_input("Qualifying asset expenditure ($)", value=3000000)
            cap_amount = expenditure * cap_rate
            if cap_amount > total_int:
                cap_amount = total_int
            st.markdown(f"""
| Item | Amount |
|---|---|
| Total general borrowings | ${total_bal:,.0f} |
| Total interest on general borrowings | ${total_int:,.0f} |
| **Capitalisation Rate** | **{cap_rate*100:.2f}%** |
| Expenditure on qualifying asset | ${expenditure:,.0f} |
| **Borrowing costs to capitalise** | **${cap_amount:,.0f}** |
| Actual total borrowing costs | ${total_int:,.0f} |
| **Check (capped at total borrowing costs):** | {"✅ OK" if cap_amount <= total_int else "⚠️ Cap applied"} |
""")

    with tab4:
        st.header("Visualizations")
        months = list(range(1,19))
        monthly_int = 5000000*0.08/12
        capitalised = [monthly_int if m not in [5,6,7,8] else 0 for m in months]
        expensed = [monthly_int - c for c, monthly_int_v in zip(capitalised, [monthly_int]*18)]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=months, y=capitalised, name="Capitalised", marker_color="#34D399"))
        fig.add_trace(go.Bar(x=months, y=[monthly_int - c for c in capitalised], name="Expensed (Suspended)", marker_color="#F87171"))
        fig.update_layout(barmode="stack", title="Monthly Borrowing Cost Treatment — Capitalised vs Expensed", xaxis_title="Month", yaxis_title="Borrowing Cost ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. Under IAS 23, borrowing costs on qualifying assets must be:**")
        q1 = st.radio("", ["Expensed always","Capitalised always","Capitalised if directly attributable; otherwise expensed","Disclosed only"], key="ias23q1")
        if st.button("Check", key="c23_1"):
            if q1 == "Capitalised if directly attributable; otherwise expensed":
                st.success("✅ Correct! Borrowing costs directly attributable to a qualifying asset MUST be capitalised. All other borrowing costs are expensed.")
            else:
                st.error("❌ IAS 23: Directly attributable borrowing costs → capitalise. Others → expense.")
        st.markdown("---")
        st.markdown("**2. Which of the following is a qualifying asset under IAS 23?**")
        q2 = st.radio("", ["Inventory purchased for immediate resale","Financial assets","Power plant under 2-year construction","A computer purchased ready for use"], key="ias23q2")
        if st.button("Check", key="c23_2"):
            if q2 == "Power plant under 2-year construction":
                st.success("✅ Correct! A qualifying asset takes substantial time to prepare for use. A power plant under construction clearly qualifies. Items ready for use do not qualify.")
            else:
                st.error("❌ A qualifying asset takes substantial time to prepare. Only the power plant under construction qualifies here.")
        st.markdown("---")
        st.markdown("**3. For specific borrowings, borrowing costs eligible for capitalisation are:**")
        q3 = st.radio("", ["Total interest on the specific loan","Total interest less investment income earned on temporary investments","Average rate × expenditure","Total interest plus investment income"], key="ias23q3")
        if st.button("Check", key="c23_3"):
            if q3 == "Total interest less investment income earned on temporary investments":
                st.success("✅ Correct! For specific borrowings: gross interest minus any income from temporarily investing the loan proceeds.")
            else:
                st.error("❌ Specific borrowings: gross interest MINUS investment income on temporarily invested funds.")
        st.markdown("---")
        st.markdown("**4. Capitalisation must be SUSPENDED when:**")
        q4 = st.radio("", ["Normal technical delays occur","Extended periods where active development is interrupted","The asset is temporarily idle","Material expenditure pauses for one week"], key="ias23q4")
        if st.button("Check", key="c23_4"):
            if q4 == "Extended periods where active development is interrupted":
                st.success("✅ Correct! Suspend during extended periods of active development suspension. Normal interruptions (technical delays) do NOT trigger suspension.")
            else:
                st.error("❌ Suspend only for extended interruptions in development. Normal delays don't trigger suspension.")
        st.markdown("---")
        st.markdown("**5. The general borrowings capitalisation rate is:**")
        q5 = st.radio("", ["The highest interest rate on any single loan","The prime lending rate","Weighted average interest rate on outstanding general borrowings","The risk-free rate"], key="ias23q5")
        if st.button("Check", key="c23_5"):
            if q5 == "Weighted average interest rate on outstanding general borrowings":
                st.success("✅ Correct! The capitalisation rate = weighted average of interest rates on all outstanding general borrowings during the period.")
            else:
                st.error("❌ The capitalisation rate = WEIGHTED AVERAGE interest rate of all outstanding general borrowings.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 23 Key Rules

**Core Rule:** Directly attributable borrowing costs on qualifying assets → **MUST CAPITALISE**

**Qualifying Asset:** Takes substantial time to prepare for use/sale (factories, developments, some inventories)

**Specific Borrowings:**
```
Capitalise = Gross Interest − Temporary Investment Income
```

**General Borrowings:**
```
Capitalisation Rate = Total Interest on General Borrowings ÷ Total General Borrowings
Amount = Capitalisation Rate × Expenditure on Qualifying Asset
Cap: Cannot exceed actual borrowing costs incurred
```

**Timing:**
- Start: All three conditions met (expenditure + borrowing costs + active development)
- Suspend: Extended inactive periods
- Stop: Substantially all activities complete
        """)
        st.success("🎓 IAS 23 Complete!")
        st.info("💡 Next: IAS 24 — Related Party Disclosures")

if __name__ == "__main__":
    show()