import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏢 IAS 40: Investment Property")
    st.markdown("*Master the recognition, measurement models and disclosure of investment property under IFRS*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Definition and Scope")
        st.markdown("""
        **Investment property** is property (land or building, or part of a building, or both) held by the owner or by the lessee as a right-of-use asset to earn **rentals** or for **capital appreciation** or **both**.

        Investment property is NOT:
        - Property used in production/supply of goods or services or administration → **IAS 16 (PPE)**
        - Property held for sale in the ordinary course of business → **IAS 2 (Inventories)**
        - Owner-occupied property → **IAS 16**

        **Examples of Investment Property:**
        - Land held for long-term capital appreciation
        - Land held for currently undetermined future use
        - Building leased out under operating leases
        - Vacant building held to be leased under operating lease
        - Property being constructed for future use as investment property
        """)

        st.subheader("2. Initial Measurement")
        st.markdown("""
        Investment property is measured **initially at cost**, including:
        - Purchase price
        - Directly attributable transaction costs (legal fees, transfer taxes)

        Initial cost of a leased investment property = right-of-use asset measured per IFRS 16.
        """)

        st.subheader("3. Two Measurement Models — Choose One, Apply to All")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Fair Value Model** *(most common choice)*
            - Carry at **fair value** at each balance sheet date
            - Changes in fair value → **P&L** (not OCI)
            - No depreciation
            - Must use if lessee applies to right-of-use investment property
            - Requires reliable fair value at all times
            """)
        with col2:
            st.markdown("""
            **Cost Model** *(fallback)*
            - Carry at **cost less accumulated depreciation and impairment**
            - Same as IAS 16 cost model
            - Must **disclose fair value** in notes
            - Used when fair value cannot be reliably determined
            """)

        st.info("⚠️ Key difference from IAS 16 revaluation model: Under IAS 40 fair value model, gains/losses go to **P&L** — NOT OCI.")

        st.subheader("4. Transfers Between Categories")
        transfer_data = {
            "Transfer": [
                "Investment property → Owner-occupied (PPE)",
                "Owner-occupied (PPE) → Investment property (fair value model)",
                "Inventory → Investment property (fair value model)",
                "Investment property → Inventory (for sale)"
            ],
            "Trigger": [
                "Change of use: entity begins to occupy",
                "Change of use: entity ceases to occupy",
                "Completion of construction/development for investment",
                "Change of use: entity begins to develop for sale"
            ],
            "Measurement at Transfer": [
                "Deemed cost = Fair value at date of transfer",
                "Revalue to FV first (any gain to OCI per IAS 16); then carry at FV",
                "Any difference between carrying amount and FV → P&L",
                "Transfer at carrying amount (cost model continues)"
            ]
        }
        st.dataframe(pd.DataFrame(transfer_data), use_container_width=True, hide_index=True)

        st.subheader("5. Disposal and Derecognition")
        st.markdown("""
        Derecognise investment property on disposal or when permanently withdrawn from use with no future economic benefits expected.

        **Gain/loss on disposal = Proceeds − Carrying Amount → P&L**

        For fair value model: carrying amount = most recent fair value, so gain/loss reflects only changes since last valuation.
        """)

        st.subheader("6. Disclosure Requirements")
        st.markdown("""
        **Both models require:**
        - Whether fair value or cost model is used
        - Criteria for classifying property as investment property
        - Methods and assumptions used in determining fair value
        - Rental income earned
        - Direct operating expenses (whether or not rental income was earned)

        **Fair value model also requires:**
        - Reconciliation of opening/closing carrying amount
        - Fair value gain/loss recognised in P&L

        **Cost model also requires:**
        - Fair value of investment property disclosed in notes
        - Depreciation methods and rates used
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Fair Value Model — Year-End Revaluation")
        st.markdown("""
        Entity owns a commercial building as investment property.
        - Carrying amount (FV at last year-end): **$5,000,000**
        - Fair value at current year-end: **$5,400,000**
        - Rental income received during year: **$300,000**
        - Operating expenses on property: **$80,000**

        **Journal entries:**
        ```
        Dr  Investment Property         $400,000
            Cr  Fair Value Gain (P&L)       $400,000

        Dr  Cash                        $300,000
            Cr  Rental Income (P&L)         $300,000

        Dr  Property Expenses (P&L)     $80,000
            Cr  Cash                        $80,000
        ```
        **Net P&L impact = $400,000 + $300,000 − $80,000 = $620,000 gain**
        """)

        st.subheader("Example 2: Cost Model — Annual Depreciation")
        st.markdown("""
        Entity uses cost model for investment property:
        - Building cost: **$4,000,000** (land $500,000 + building $3,500,000)
        - Useful life of building: 40 years | Residual value: $0
        - Fair value at year-end (disclosed in notes): **$5,200,000**

        **Annual depreciation = $3,500,000 / 40 = $87,500**
        ```
        Dr  Depreciation Expense       $87,500
            Cr  Accumulated Depreciation    $87,500
        ```
        **Balance sheet:** Investment Property $4,000,000 − Accumulated Depreciation $87,500 = **$3,912,500**
        **Notes:** Fair value = $5,200,000 (disclosed but not recognised under cost model)
        """)

        st.subheader("Example 3: Transfer from Owner-Occupied to Investment Property")
        st.markdown("""
        Entity stops using its head office building and leases it out to a third party under an operating lease.
        Entity uses the **fair value model** for investment property.

        - Cost of building: $3,000,000 | Accumulated depreciation: $600,000
        - **Carrying amount at transfer date: $2,400,000**
        - **Fair value at transfer date: $3,200,000**

        **Step 1:** Revalue under IAS 16 before reclassifying:
        ```
        Dr  PPE                         $800,000
            Cr  Revaluation Reserve (OCI)   $800,000
        ```
        **Step 2:** Reclassify to Investment Property at fair value:
        ```
        Dr  Investment Property         $3,200,000
            Cr  PPE                         $3,200,000
        ```
        Revaluation reserve of $800,000 remains in equity (transferred to retained earnings as property is used/sold).
        """)

        st.subheader("Example 4: Partial Investment Property")
        st.markdown("""
        A building has:
        - Ground floor leased to tenants (40% of floor area) → **Investment Property**
        - Upper floors used as company headquarters (60% of floor area) → **PPE (IAS 16)**

        Can the portions be sold separately? If YES → account for each portion separately.
        If NO → classify the entire building as PPE (IAS 16) UNLESS the owner-occupied portion is insignificant.

        Judgement is required — document the basis for classification.
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Investment Property Classifier")
        st.markdown("Determine whether a property qualifies as investment property:")
        col1, col2 = st.columns(2)
        with col1:
            earn_rental = st.checkbox("Held to earn rental income?")
            capital_app = st.checkbox("Held for capital appreciation?")
            owner_occupied = st.checkbox("Entity uses it in its own operations?")
            held_for_sale = st.checkbox("Held for sale in ordinary course of business?")
            under_construction = st.checkbox("Under construction for future investment property use?")
        with col2:
            if owner_occupied:
                st.error("🏢 **PPE (IAS 16)** — Owner-occupied property. Cannot classify as investment property.")
            elif held_for_sale:
                st.warning("📦 **Inventory (IAS 2)** — Property held for sale in ordinary course. Not investment property.")
            elif earn_rental or capital_app or under_construction:
                st.success("🏦 **INVESTMENT PROPERTY (IAS 40)** — Qualifies for IAS 40 treatment.")
                if earn_rental:
                    st.markdown("✅ Rental income purpose confirmed")
                if capital_app:
                    st.markdown("✅ Capital appreciation purpose confirmed")
                if under_construction:
                    st.markdown("✅ Construction for investment property confirmed")
            else:
                st.info("ℹ️ Select the purpose of the property to classify it.")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Fair Value Model — P&L Calculator")
        col1, col2 = st.columns(2)
        with col1:
            opening_fv = st.number_input("Opening Fair Value ($)", value=5000000, step=50000)
            closing_fv = st.number_input("Closing Fair Value ($)", value=5400000, step=50000)
            rental_income = st.number_input("Rental Income Received ($)", value=300000, step=10000)
            direct_costs = st.number_input("Direct Operating Expenses ($)", value=80000, step=5000)
        with col2:
            fv_gain_loss = closing_fv - opening_fv
            net_pl = fv_gain_loss + rental_income - direct_costs
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | Fair value gain/(loss) → P&L | ${fv_gain_loss:,.0f} |
            | Rental income | ${rental_income:,.0f} |
            | Direct operating expenses | (${direct_costs:,.0f}) |
            | **Net P&L contribution** | **${net_pl:,.0f}** |
            | Closing carrying amount | ${closing_fv:,.0f} |
            """)
            if fv_gain_loss > 0:
                st.success(f"✅ Fair value GAIN of ${fv_gain_loss:,.0f} recognised in P&L")
            else:
                st.error(f"⚠️ Fair value LOSS of ${abs(fv_gain_loss):,.0f} recognised in P&L")

        st.markdown("---")
        st.subheader("🔧 Tool 3: Cost Model vs Fair Value Model Comparison")
        prop_cost = st.number_input("Property Cost (building only) ($)", value=3500000, step=100000, key="ip_cost")
        useful_life_ip = st.number_input("Useful Life (years)", value=40, min_value=10, max_value=100)
        annual_fv_growth = st.number_input("Annual Fair Value Growth (%)", value=3.0, step=0.5) / 100
        years_proj = st.number_input("Projection Years", value=5, min_value=1, max_value=20)

        if st.button("Compare Models"):
            annual_depr = prop_cost / useful_life_ip
            rows = []
            cost_ca = prop_cost
            fv_ca = prop_cost
            for yr in range(1, int(years_proj) + 1):
                cost_ca -= annual_depr
                fv_ca = fv_ca * (1 + annual_fv_growth)
                rows.append({
                    "Year": yr,
                    "Cost Model CA ($)": f"{cost_ca:,.0f}",
                    "Fair Value CA ($)": f"{fv_ca:,.0f}",
                    "FV Gain in P&L ($)": f"{fv_ca * annual_fv_growth:,.0f}",
                    "Cost Model Depr ($)": f"({annual_depr:,.0f})"
                })
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            st.info("Under the Fair Value model, gains go to **P&L** (no depreciation). Under Cost model, depreciation is charged to **P&L** and fair value is only disclosed in notes.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("Fair Value Model vs Cost Model — Carrying Amount Over 10 Years")
        yrs = list(range(0, 11))
        cost_vals = [3500000 - 3500000/40 * y for y in yrs]
        fv_vals = [3500000 * (1.03)**y for y in yrs]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=yrs, y=cost_vals, name="Cost Model (after depr)", line=dict(color="#F87171", width=2), mode="lines+markers"))
        fig.add_trace(go.Scatter(x=yrs, y=fv_vals, name="Fair Value Model", line=dict(color="#34D399", width=2), mode="lines+markers"))
        fig.update_layout(title="Investment Property — Cost vs Fair Value Model Carrying Amount (3% annual growth)",
                          xaxis_title="Year", yaxis_title="Carrying Amount ($)", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("P&L Impact Comparison — Fair Value vs Cost Model")
        fv_pl = [3500000 * (1.03)**y * 0.03 for y in range(1, 11)]
        cost_pl = [-3500000/40] * 10
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=list(range(1,11)), y=fv_pl, name="FV Gain to P&L", marker_color="#34D399"))
        fig2.add_trace(go.Bar(x=list(range(1,11)), y=cost_pl, name="Depreciation to P&L", marker_color="#F87171"))
        fig2.update_layout(barmode="group", title="Annual P&L Impact — Fair Value Gain vs Depreciation ($)",
                           xaxis_title="Year", yaxis_title="P&L Amount ($)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Investment Property Classification Decision Tree")
        st.markdown("""
        ```
        Is the property held for:
                    |
        ┌───────────┼────────────┐
        Earn rentals /     Own operations?    For sale in ordinary
        Capital appreciation?                 course of business?
              |                  |                    |
        IAS 40              IAS 16 PPE           IAS 2 Inventories
        Investment Property  Owner-Occupied       Inventory
        ```
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IAS 40 fair value model, changes in fair value of investment property are recognised in:**")
        q1 = st.radio("", [
            "Other Comprehensive Income (OCI)",
            "Profit or Loss (P&L)",
            "Retained Earnings directly",
            "Revaluation Reserve"
        ], key="ias40q1")
        if st.button("Check Answer", key="ias40c1"):
            if q1 == "Profit or Loss (P&L)":
                st.success("✅ Correct! Under IAS 40 fair value model, ALL fair value changes go directly to **P&L** — this is a key difference from IAS 16 revaluation model where surpluses go to OCI.")
            else:
                st.error("❌ Incorrect. IAS 40 fair value model: FV changes → P&L (not OCI). This differs from IAS 16 where revaluation surplus goes to OCI.")

        st.markdown("---")
        st.markdown("**2. Under the IAS 40 fair value model, investment property is:**")
        q2 = st.radio("", [
            "Depreciated and tested for impairment annually",
            "Not depreciated; carried at fair value with changes in P&L",
            "Depreciated but revalued to fair value at year-end",
            "Carried at the lower of cost or fair value"
        ], key="ias40q2")
        if st.button("Check Answer", key="ias40c2"):
            if q2 == "Not depreciated; carried at fair value with changes in P&L":
                st.success("✅ Correct! Under the fair value model, NO depreciation is charged. The property is remeasured to fair value each period with gains/losses in P&L.")
            else:
                st.error("❌ Fair value model = no depreciation + fair value at each year-end with changes in P&L.")

        st.markdown("---")
        st.markdown("**3. When an entity transfers a property from owner-occupied to investment property (using fair value model), the difference between carrying amount and fair value at transfer date is:**")
        q3 = st.radio("", [
            "Recognised in P&L immediately",
            "Treated as a revaluation under IAS 16 first, with gain to OCI; then reclassify at fair value",
            "Recognised directly in retained earnings",
            "Deferred and amortised over remaining useful life"
        ], key="ias40q3")
        if st.button("Check Answer", key="ias40c3"):
            if q3 == "Treated as a revaluation under IAS 16 first, with gain to OCI; then reclassify at fair value":
                st.success("✅ Correct! When transferring from PPE to investment property (FV model): first apply IAS 16 revaluation (gain to OCI), then reclassify the property at fair value.")
            else:
                st.error("❌ Transfer from PPE to IP (FV model): revalue under IAS 16 first (surplus to OCI), then reclassify at fair value to investment property.")

        st.markdown("---")
        st.markdown("**4. Under the IAS 40 cost model, the fair value of investment property must be:**")
        q4 = st.radio("", [
            "Recognised in the financial statements",
            "Disclosed in the notes",
            "Neither recognised nor disclosed",
            "Disclosed only if it exceeds carrying amount by more than 20%"
        ], key="ias40q4")
        if st.button("Check Answer", key="ias40c4"):
            if q4 == "Disclosed in the notes":
                st.success("✅ Correct! Under the cost model, the fair value must be DISCLOSED in the notes — it is not recognised in the balance sheet but users still need to know the market value.")
            else:
                st.error("❌ Cost model: fair value NOT recognised on balance sheet but MUST be disclosed in notes.")

        st.markdown("---")
        st.markdown("**5. A building used 60% for the entity's own office and 40% leased to third parties. Can the portions be separated? If NO, the entire building is classified as:**")
        q5 = st.radio("", [
            "Investment property (IAS 40)",
            "PPE (IAS 16) — unless the owner-occupied portion is insignificant",
            "Part inventory, part investment property",
            "Financial asset"
        ], key="ias40q5")
        if st.button("Check Answer", key="ias40c5"):
            if q5 == "PPE (IAS 16) — unless the owner-occupied portion is insignificant":
                st.success("✅ Correct! If the portions cannot be sold separately and the owner-occupied portion is significant, the entire building is classified as PPE under IAS 16.")
            else:
                st.error("❌ If portions are inseparable: classify entire building as PPE (IAS 16) unless owner-occupied part is insignificant.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. What is Investment Property?
        Property held to earn **rentals** or for **capital appreciation** (or both) — NOT owner-occupied, NOT for sale.

        ### 2. Two Measurement Models (choose one, apply to all)
        | | Fair Value Model | Cost Model |
        |---|---|---|
        | Carrying amount | Fair value | Cost − Depreciation − Impairment |
        | FV changes | P&L | Disclosed in notes only |
        | Depreciation | None | Yes |
        | Impairment test | Not needed (FV used) | Yes (IAS 36) |

        ### 3. Key Distinction from IAS 16
        - IAS 16 revaluation surplus → **OCI**
        - IAS 40 fair value change → **P&L**

        ### 4. Transfers Between Categories
        ```
        PPE → Investment Property (FV model): Revalue under IAS 16 first (OCI), then reclassify at FV
        Inventory → Investment Property: Difference between carrying amount and FV → P&L
        Investment Property → PPE: Deemed cost = FV at date of transfer
        ```

        ### 5. Disposal
        ```
        Gain/Loss = Proceeds − Carrying Amount → P&L
        ```
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Investment Property = Held for rentals OR capital appreciation (not owner-occupied)
Fair Value Model → FV changes to P&L (NOT OCI) + NO depreciation
Cost Model → Depreciate + disclose FV in notes
Transfer PPE→IP (FV model): IAS 16 revalue first (OCI surplus), then reclassify at FV
Gain/loss on disposal → P&L
        """)

        st.success("🎓 **IAS 40 Complete!** You can now classify investment property, apply both measurement models, account for transfers and disposals.")
        st.info("💡 **Next**: IAS 41 — Agriculture")

if __name__ == "__main__":
    show()