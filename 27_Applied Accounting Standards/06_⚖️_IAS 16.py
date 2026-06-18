import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("🏭 IAS 16: Property, Plant and Equipment")
    st.markdown("*Master recognition, measurement, depreciation, revaluation and derecognition of PPE*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Recognition Criteria")
        st.markdown("""
PPE is recognised when:
- It is **probable** that future economic benefits will flow to the entity
- The **cost can be measured reliably**

PPE includes: land, buildings, machinery, vehicles, office equipment, fixtures.
Initial measurement is always at **COST**.
        """)
        st.subheader("2. Cost of PPE")
        st.markdown("""
**Cost includes:**
- Purchase price (net of trade discounts and rebates)
- Import duties and non-refundable purchase taxes
- Directly attributable costs to bring asset to location and condition for intended use (installation, professional fees, testing)
- Initial estimate of dismantling/restoration costs (IAS 37)

**Excludes:** abnormal waste, training costs, administration overheads, general overheads

**Subsequent costs:** Capitalise only if they meet the recognition criteria (i.e., future economic benefits and reliable measurement). Day-to-day servicing costs → expense.
        """)
        st.subheader("3. Measurement Models (choose one per class, apply consistently)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
**Cost Model**
- Carry at cost less accumulated depreciation and accumulated impairment losses
- Simpler to apply
- Most common in practice
            """)
        with col2:
            st.markdown("""
**Revaluation Model**
- Carry at **fair value** at date of revaluation less subsequent depreciation and impairment
- Revalue with sufficient regularity
- Revaluation surplus → **OCI** (Revaluation Reserve in equity)
- Revaluation deficit → **P&L** (unless reversing a prior surplus in OCI)
- Must apply to an **entire class** of PPE
            """)
        st.subheader("4. Depreciation")
        st.markdown("""
- **Depreciable amount** = Cost (or revalued amount) LESS residual value
- Begin depreciation when asset is **available for use**
- Each significant component must be depreciated **separately** (component approach)
- Residual value and useful life reviewed **at least annually**
- Depreciation continues even when asset is idle (unless fully depreciated or held for sale)

**Depreciation methods:**
| Method | Description | Pattern |
|--------|-------------|---------|
| Straight-Line | Even charge over useful life | Constant |
| Reducing Balance | % of carrying amount | Decreasing |
| Units of Production | Based on usage/output | Variable |
        """)
        st.subheader("5. Revaluation — Detailed Treatment")
        st.markdown("""
**Upward revaluation:**
- Dr PPE (gross asset) / Dr Accumulated Depreciation → to eliminate existing depr
- Cr Revaluation Reserve (OCI/Equity) → for surplus

**Downward revaluation:**
- First offset against any existing revaluation surplus (Dr Revaluation Reserve)
- Any excess → Dr P&L

**Revaluation reserve transfer to retained earnings:**
- As asset is used (annual incremental transfer = revalued depr − historical cost depr)
- Or on disposal of the asset

**Deferred tax on revaluation:** Recognise DTL on the revaluation surplus (IAS 12).
        """)
        st.subheader("6. Derecognition")
        st.markdown("""
Derecognise (remove from balance sheet) when:
- Disposed of, OR
- No future economic benefits expected

**Gain/loss on disposal = Proceeds − Carrying amount** → recognised in P&L (not revenue)
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Cost of PPE")
        st.markdown("""
| Cost Element | Amount |
|---|---|
| Purchase price | $500,000 |
| Less: Trade discount | ($25,000) |
| Import duties | $15,000 |
| Freight and installation | $8,000 |
| Testing before use | $4,000 |
| Training staff to use | $6,000 ← **EXCLUDED** |
| **Total PPE Cost** | **$502,000** |
        """)
        st.subheader("Example 2: Depreciation Methods Compared")
        data = pd.DataFrame({
            "Year": [1,2,3,4,5],
            "Straight-Line ($)": [20000,20000,20000,20000,20000],
            "Reducing Balance 40% ($)": [40000,24000,14400,8640,5184],
            "Units of Production ($)": [25000,30000,18000,15000,12000]
        })
        st.dataframe(data, use_container_width=True, hide_index=True)
        st.caption("Asset cost $100,000, residual $0, life 5 years. Units of production based on actual output.")

        st.subheader("Example 3: Revaluation")
        st.markdown("""
**Asset:** Cost $1,000,000 | Accumulated depreciation $300,000 | Carrying amount $700,000
**Fair value at revaluation date:** $900,000

**Journal Entry (Gross Asset Method):**
```
Dr  PPE (gross)                     $300,000  (to eliminate accum. depr.)
    Cr  Accumulated Depreciation        $300,000
Dr  PPE (gross)                     $200,000  (upward revaluation)
    Cr  Revaluation Reserve (OCI)       $200,000
```
Net effect: PPE carrying amount rises from $700,000 to $900,000; Revaluation Reserve = $200,000
        """)
        st.subheader("Example 4: Disposal Gain/Loss")
        st.markdown("""
**Asset carrying amount at disposal:** $150,000 | **Sale proceeds:** $180,000
**Gain on disposal = $180,000 − $150,000 = $30,000 → P&L (other income)**

If sale proceeds were $120,000:
**Loss on disposal = $120,000 − $150,000 = ($30,000) → P&L expense**
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Tool 1: Depreciation Calculator")
        col1,col2 = st.columns(2)
        with col1:
            cost = st.number_input("Asset Cost ($)", value=100000, step=1000)
            residual = st.number_input("Residual Value ($)", value=0, step=1000)
            life = st.number_input("Useful Life (years)", value=5, min_value=1)
            method = st.selectbox("Method:", ["Straight-Line","Reducing Balance","Units of Production"])
            rb_rate = 0.0
            if method == "Reducing Balance":
                rb_rate = st.number_input("Reducing Balance Rate (%)", value=40.0) / 100
        with col2:
            depreciable = cost - residual
            rows = []
            ca = cost
            for yr in range(1, life+1):
                if method == "Straight-Line":
                    depr = depreciable / life
                elif method == "Reducing Balance":
                    depr = ca * rb_rate
                else:
                    depr = depreciable / life  # simplified
                ca -= depr
                rows.append({"Year": yr, "Depreciation ($)": round(depr,2), "Closing Carrying Amount ($)": round(ca,2)})
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔧 Tool 2: Revaluation Entry Calculator")
        old_cost = st.number_input("Original Cost ($)", value=1000000, step=10000, key="rvc")
        accum_depr = st.number_input("Accumulated Depreciation ($)", value=300000, step=10000, key="rvd")
        fair_val = st.number_input("New Fair Value ($)", value=900000, step=10000, key="rvf")
        if st.button("Generate Revaluation Entry"):
            ca = old_cost - accum_depr
            surplus = fair_val - ca
            st.markdown(f"**Carrying amount before revaluation:** ${ca:,.0f}")
            st.markdown(f"**New fair value:** ${fair_val:,.0f}")
            if surplus > 0:
                st.success(f"""
**Upward Revaluation — Surplus: ${surplus:,.0f} → OCI (Revaluation Reserve)**
```
Dr  Accumulated Depreciation    ${accum_depr:,.0f}
Dr  PPE (gross asset)           ${surplus:,.0f}
    Cr  Revaluation Reserve (OCI)   ${accum_depr + surplus:,.0f}
```
""")
            else:
                deficit = abs(surplus)
                st.error(f"""
**Downward Revaluation — Deficit: ${deficit:,.0f} → P&L (or offset against reserve)**
```
Dr  Impairment/Revaluation Loss (P&L)   ${deficit:,.0f}
Dr  Accumulated Depreciation            ${accum_depr:,.0f}
    Cr  PPE (gross asset)                   ${accum_depr + deficit:,.0f}
```
""")

        st.markdown("---")
        st.subheader("🔧 Tool 3: Disposal Gain/Loss Calculator")
        disp_ca = st.number_input("Carrying Amount at Disposal ($)", value=150000, step=1000, key="dca")
        proceeds = st.number_input("Sale Proceeds ($)", value=180000, step=1000, key="dpr")
        if st.button("Calculate Gain/Loss"):
            gl = proceeds - disp_ca
            if gl >= 0:
                st.success(f"**Gain on disposal: ${gl:,.0f}** → recognised in P&L as other income")
            else:
                st.error(f"**Loss on disposal: ${abs(gl):,.0f}** → recognised in P&L as expense")

    with tab4:
        st.header("Visualizations")
        st.subheader("Depreciation Method Comparison")
        cost_v = 100000; residual_v = 0; life_v = 5; rb_v = 0.4
        yrs = list(range(1, life_v+1))
        sl_dep = [(cost_v-residual_v)/life_v]*life_v
        rb_dep = []
        ca_rb = cost_v
        for _ in yrs:
            d = ca_rb * rb_v; rb_dep.append(d); ca_rb -= d
        fig = go.Figure()
        fig.add_trace(go.Bar(x=yrs, y=sl_dep, name="Straight-Line", marker_color="#2563EB"))
        fig.add_trace(go.Bar(x=yrs, y=rb_dep, name="Reducing Balance (40%)", marker_color="#F59E0B"))
        fig.update_layout(barmode="group", title="Annual Depreciation — SL vs Reducing Balance", height=380, xaxis_title="Year", yaxis_title="Depreciation ($)")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Carrying Amount Over Time")
        ca_sl = [cost_v - sl_dep[0]*(i+1) for i in range(life_v)]
        ca_rb_list = []
        cv = cost_v
        for d in rb_dep:
            cv -= d; ca_rb_list.append(cv)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=yrs, y=ca_sl, name="Straight-Line CA", line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig2.add_trace(go.Scatter(x=yrs, y=ca_rb_list, name="Reducing Balance CA", line=dict(color="#F59E0B", width=2), mode="lines+markers"))
        fig2.update_layout(title="Carrying Amount — Decline Over Useful Life", height=350, yaxis_title="Carrying Amount ($)")
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. Which costs are INCLUDED in the initial cost of PPE?**")
        q1 = st.radio("", ["Staff training costs","Directly attributable installation costs","General administration overheads","Marketing costs"], key="ias16q1")
        if st.button("Check", key="c16_1"):
            if q1 == "Directly attributable installation costs":
                st.success("✅ Correct! Directly attributable costs to bring the asset to its working condition are capitalised. Training, admin and marketing are expensed.")
            else:
                st.error("❌ Directly attributable installation costs are capitalised. Training, admin and marketing costs are excluded from PPE cost.")
        st.markdown("---")
        st.markdown("**2. Under the revaluation model, an upward revaluation surplus is recognised in:**")
        q2 = st.radio("", ["Profit or loss","Other Comprehensive Income (OCI)","Retained earnings directly","Notes only"], key="ias16q2")
        if st.button("Check", key="c16_2"):
            if q2 == "Other Comprehensive Income (OCI)":
                st.success("✅ Correct! Revaluation surpluses go to OCI and accumulate in the Revaluation Reserve in equity.")
            else:
                st.error("❌ Revaluation surpluses go through OCI to the Revaluation Reserve in equity — not P&L.")
        st.markdown("---")
        st.markdown("**3. When should depreciation begin under IAS 16?**")
        q3 = st.radio("", ["When purchased","When available for use","When first used","From the following month"], key="ias16q3")
        if st.button("Check", key="c16_3"):
            if q3 == "When available for use":
                st.success("✅ Correct! IAS 16 requires depreciation to begin when the asset is available for use — not when it is actually used.")
            else:
                st.error("❌ Depreciation begins when the asset is AVAILABLE FOR USE (not necessarily when it starts being used).")
        st.markdown("---")
        st.markdown("**4. Gain or loss on disposal of PPE is:**")
        q4 = st.radio("", ["Reported as revenue","Reported in P&L as other income/expense","Reported in OCI","Added to the revaluation reserve"], key="ias16q4")
        if st.button("Check", key="c16_4"):
            if q4 == "Reported in P&L as other income/expense":
                st.success("✅ Correct! Disposal gains/losses = Proceeds minus Carrying Amount → P&L as other income or expense. NOT as revenue.")
            else:
                st.error("❌ Disposal gain/loss goes to P&L as other income/expense — never classified as revenue.")
        st.markdown("---")
        st.markdown("**5. Under the component approach, an aircraft body and its engines must be:**")
        q5 = st.radio("", ["Depreciated together as one asset","Depreciated separately as different components","Written off immediately if replaced","Measured at fair value"], key="ias16q5")
        if st.button("Check", key="c16_5"):
            if q5 == "Depreciated separately as different components":
                st.success("✅ Correct! IAS 16 requires separate depreciation of significant components with different useful lives (e.g., airframe 20 years vs engines 10 years).")
            else:
                st.error("❌ IAS 16 component approach requires significant parts with different useful lives to be depreciated separately.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 16 Key Rules

**Recognition:** Probable future economic benefits + reliable cost measurement

**Initial Measurement:** COST (purchase + directly attributable costs + dismantling provision)

**Two Models (applied to entire class):**
| | Cost Model | Revaluation Model |
|-|-----------|-------------------|
| Carrying amount | Cost − Accum. Depr − Impairment | Fair Value − Subsequent Depr |
| Surplus/deficit | N/A | Surplus → OCI; Deficit → P&L |

**Depreciation:**
```
Depreciable Amount = Cost (or Revalued Amount) − Residual Value
Annual SL Depreciation = Depreciable Amount ÷ Useful Life
```
- Starts when **available for use**
- Review residual value and useful life **annually**
- Component approach for significant parts

**Disposal:**
```
Gain/Loss = Net Proceeds − Carrying Amount → P&L
```
        """)
        st.success("🎓 IAS 16 Complete!")
        st.info("💡 Next: IAS 17 / IFRS 16 — Leases")

if __name__ == "__main__":
    show()