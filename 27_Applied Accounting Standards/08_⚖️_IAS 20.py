import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show():
    st.title("🏛️ IAS 20: Government Grants and Disclosure of Government Assistance")
    st.markdown("*Master the recognition, measurement and presentation of government grants under IFRS*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Definitions")
        st.markdown("""
**Government grants:** Transfers of resources by government to an entity in return for compliance with conditions attached to them.

**Types of grants:**
- **Grants related to assets** – given to purchase, construct or acquire long-term assets (e.g., grant to buy machinery)
- **Grants related to income** – compensation for expenses or losses incurred, or financial support (e.g., employment subsidy, R&D grant)
        """)
        st.subheader("2. Recognition Criteria")
        st.markdown("""
Recognise a government grant **only when:**
1. The entity will **comply** with the conditions attached to it, AND
2. The grants will be **received** (reasonable assurance)

Do NOT recognise based on cash receipt alone — receipts that do not meet conditions remain as liabilities (deferred income).
        """)
        st.subheader("3. Two Presentation Approaches for Asset Grants")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
**Approach 1: Deferred Income**
- Recognise grant as deferred income (liability)
- Release to P&L systematically over the asset's useful life
- More common in practice
            """)
        with col2:
            st.markdown("""
**Approach 2: Deducted from Asset Cost**
- Deduct grant from carrying amount of asset
- Lower asset cost → lower depreciation
- Less common but permitted
            """)
        st.subheader("4. Income Grants")
        st.markdown("""
- Recognise in P&L **on a systematic basis** over the period in which the related costs are recognised
- If grant is to compensate costs already incurred → recognise immediately in P&L
- **Never** credit directly to equity
        """)
        st.subheader("5. Repayment of Grants")
        st.markdown("""
If a grant becomes repayable (conditions not met):

**Asset grant (deferred income method):**
- Increase the carrying amount of deferred income by the repayment amount
- Recognise any cumulative excess beyond unamortised deferred income → immediately in P&L

**Income grant repayable:**
- Recognise full repayment immediately in P&L

**Asset grant (asset deduction method):**
- Increase asset carrying amount by repayment
- Extra depreciation that would have been charged → P&L
        """)
        st.subheader("6. Government Assistance vs Government Grants")
        st.markdown("""
**Government assistance** that cannot be measured reliably (e.g., free technical advice, tax concessions) is disclosed but NOT recognised as a grant. IAS 20 only covers measurable transfers.
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Asset Grant — Deferred Income Method")
        st.markdown("""
- Government grant received: **$200,000** to purchase machinery costing $500,000
- Useful life of machinery: 5 years, straight-line

| Year | Depreciation on Full Cost | Grant Released to P&L | Net Annual Charge |
|---|---|---|---|
| 1 | $100,000 | ($40,000) | $60,000 |
| 2 | $100,000 | ($40,000) | $60,000 |
| ... | ... | ... | ... |

**Journal entries at purchase:**
```
Dr  Machinery                $500,000
    Cr  Cash                    $500,000
Dr  Cash                     $200,000
    Cr  Deferred Income          $200,000
```
**Each year:**
```
Dr  Depreciation Expense     $100,000
    Cr  Accumulated Depreciation   $100,000
Dr  Deferred Income          $40,000
    Cr  Grant Income (P&L)         $40,000
```
        """)
        st.subheader("Example 2: Asset Grant — Deduct from Asset Method")
        st.markdown("""
Same facts as above:

**Machinery net cost = $500,000 − $200,000 = $300,000**
**Annual depreciation = $300,000 ÷ 5 = $60,000**

Journal at purchase:
```
Dr  Machinery (net)         $300,000
    Cr  Cash                    $500,000
    Cr  Grant (credit to asset)  $200,000  ← net presentation
```
Result: Lower asset on balance sheet; lower annual depreciation; same total income statement effect over 5 years.
        """)
        st.subheader("Example 3: Income Grant — Employment Subsidy")
        st.markdown("""
Government pays a wage subsidy of **$50,000** for employing 10 workers for 12 months.

Since grant compensates for wage costs incurred over 12 months:
- Recognise **$50,000 ÷ 12 = $4,167/month** as income in P&L, matching the wage expense

```
Dr  Grant Receivable        $50,000
    Cr  Grant Income            $50,000   (over 12 months)
```
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Grant Recognition Checker")
        grant_received = st.checkbox("Grant has been received (or receivable)?")
        conditions_met = st.checkbox("Entity will comply with all attached conditions?")
        reasonable_assurance = st.checkbox("Reasonable assurance that conditions will be met?")
        if st.button("Check Recognition"):
            if grant_received and conditions_met and reasonable_assurance:
                st.success("✅ **RECOGNISE** the government grant in the financial statements.")
            else:
                missing = []
                if not grant_received: missing.append("Grant received/receivable")
                if not conditions_met: missing.append("Compliance with conditions")
                if not reasonable_assurance: missing.append("Reasonable assurance")
                st.error(f"❌ **DO NOT RECOGNISE** — conditions not met: {', '.join(missing)}. Treat as deferred income until conditions are satisfied.")

        st.markdown("---")
        st.subheader("🔧 Asset Grant — Annual Release Calculator")
        col1, col2 = st.columns(2)
        with col1:
            asset_cost = st.number_input("Asset Cost ($)", value=500000, step=10000)
            grant_amount = st.number_input("Grant Amount ($)", value=200000, step=10000)
            useful_life = st.number_input("Useful Life (years)", value=5, min_value=1)
        with col2:
            annual_depr = asset_cost / useful_life
            annual_grant_release = grant_amount / useful_life
            net_charge = annual_depr - annual_grant_release
            st.markdown(f"""
| Item | Annual ($) |
|---|---|
| Depreciation (on full cost) | {annual_depr:,.0f} |
| Grant release to P&L | ({annual_grant_release:,.0f}) |
| **Net annual P&L charge** | **{net_charge:,.0f}** |
| Total over {useful_life} years | {net_charge * useful_life:,.0f} |
""")
            st.markdown(f"**Asset deduction method — annual depreciation:** ${(asset_cost - grant_amount) / useful_life:,.0f}")

    with tab4:
        st.header("Visualizations")
        years_list = list(range(1, 6))
        asset_c = 500000; grant_a = 200000; life = 5
        depr_y = [asset_c / life] * life
        grant_release = [grant_a / life] * life
        net = [d - g for d, g in zip(depr_y, grant_release)]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=years_list, y=depr_y, name="Gross Depreciation", marker_color="#F87171"))
        fig.add_trace(go.Bar(x=years_list, y=[-g for g in grant_release], name="Grant Released to P&L", marker_color="#34D399"))
        fig.add_trace(go.Scatter(x=years_list, y=net, name="Net P&L Charge", line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig.update_layout(barmode="relative", title="Asset Grant — P&L Effect Over Useful Life ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. A government grant should be recognised when:**")
        q1 = st.radio("", ["Cash is received from government","Conditions are met and reasonable assurance exists","Board approves the project","Grant is publicly announced"], key="ias20q1")
        if st.button("Check", key="c20_1"):
            if q1 == "Conditions are met and reasonable assurance exists":
                st.success("✅ Correct! Recognise when (1) conditions will be complied with AND (2) there is reasonable assurance that the grant will be received.")
            else:
                st.error("❌ Receipt alone is not sufficient. Recognition requires compliance with conditions AND reasonable assurance.")
        st.markdown("---")
        st.markdown("**2. Under IAS 20, government grants related to assets may be presented as:**")
        q2 = st.radio("", ["Only as deferred income","Only deducted from the asset","Either deferred income or deducted from the asset","Credited directly to retained earnings"], key="ias20q2")
        if st.button("Check", key="c20_2"):
            if q2 == "Either deferred income or deducted from the asset":
                st.success("✅ Correct! IAS 20 allows two methods: (1) deferred income released over useful life, or (2) deducted from the asset's carrying amount.")
            else:
                st.error("❌ Both methods are permitted: deferred income OR deducted from asset carrying amount.")
        st.markdown("---")
        st.markdown("**3. An income grant compensating for already-incurred costs should be recognised:**")
        q3 = st.radio("", ["Over the next 5 years","Immediately in P&L in the period costs were incurred","As deferred income","In OCI"], key="ias20q3")
        if st.button("Check", key="c20_3"):
            if q3 == "Immediately in P&L in the period costs were incurred":
                st.success("✅ Correct! Grants compensating for already-incurred costs are recognised immediately in P&L in the same period as those costs.")
            else:
                st.error("❌ Income grants compensating already-incurred costs are recognised immediately in P&L — matching the related expense.")
        st.markdown("---")
        st.markdown("**4. If a grant becomes repayable, the repayment is:**")
        q4 = st.radio("", ["Ignored if conditions changed","Recognised immediately as a reduction in deferred income or P&L charge","Treated as a prior period error","Offset against the asset directly"], key="ias20q4")
        if st.button("Check", key="c20_4"):
            if q4 == "Recognised immediately as a reduction in deferred income or P&L charge":
                st.success("✅ Correct! Repayments reduce the unamortised deferred income balance first; any excess is recognised immediately in P&L.")
            else:
                st.error("❌ Repayment: first reduce deferred income; excess immediately in P&L.")
        st.markdown("---")
        st.markdown("**5. Government assistance that cannot be measured reliably is:**")
        q5 = st.radio("", ["Recognised at a nominal amount","Disclosed but not recognised as a grant","Ignored completely","Recognised at fair value"], key="ias20q5")
        if st.button("Check", key="c20_5"):
            if q5 == "Disclosed but not recognised as a grant":
                st.success("✅ Correct! IAS 20 only applies to measurable transfers. Unmeasurable assistance is disclosed in notes but not recognised.")
            else:
                st.error("❌ Unmeasurable government assistance is disclosed but not recognised as a grant under IAS 20.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 20 Key Rules

**Recognition:** Reasonable assurance of compliance AND receipt

**Asset Grants — Two Methods:**
| Method | Balance Sheet | P&L |
|---|---|---|
| Deferred Income | Grant = liability released over useful life | Annual grant income |
| Deduct from Asset | Reduced asset cost | Lower annual depreciation |

**Income Grants:** Recognise systematically over the period matching related costs; immediately if costs already incurred

**Never:** Credit grants directly to equity or recognise before conditions are met

**Repayment:** Reduce deferred income first; any excess to P&L immediately
        """)
        st.success("🎓 IAS 20 Complete!")
        st.info("💡 Next: IAS 21 — Effects of Changes in Foreign Exchange Rates")

if __name__ == "__main__":
    show()