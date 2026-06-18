import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🌾 IAS 41: Agriculture")
    st.markdown("*Master the accounting for biological assets, agricultural produce and government grants in agriculture*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Scope and Key Definitions")
        defs = {
            "Term": ["Biological Asset", "Agricultural Produce", "Agricultural Activity", "Harvest"],
            "Definition": [
                "A living animal or plant",
                "The harvested product of the entity's biological assets",
                "Management by an entity of the biological transformation of biological assets for sale, into agricultural produce, or into additional biological assets",
                "Detachment of produce from a biological asset or cessation of a biological asset's life processes"
            ],
            "Examples": [
                "Cattle, pigs, sheep, trees in a plantation, vines, fruit trees, dairy cows",
                "Milk (from dairy cows), wool (from sheep), harvested grapes, cut timber, picked fruit",
                "Raising livestock, cultivating orchards, fish farming, growing timber",
                "Milking a cow, shearing sheep, picking fruit, logging timber"
            ]
        }
        st.dataframe(pd.DataFrame(defs), use_container_width=True, hide_index=True)

        st.subheader("2. Measurement Principle — Fair Value Less Costs to Sell")
        st.markdown("""
        **Biological assets are measured at FAIR VALUE LESS COSTS TO SELL (FVLCTS) at every balance sheet date.**

        This applies from **initial recognition** through to the point of harvest.

        **Gains and losses from changes in FVLCTS → P&L**

        **Why fair value?**
        - Biological transformation (growth, procreation, production) creates value changes continuously
        - Historical cost would fail to reflect the changing nature of living organisms
        - Fair value provides the most relevant information for agricultural activities

        **Costs to sell** include commissions, levies, transfer taxes, but NOT transport costs to market.
        """)

        st.subheader("3. Agricultural Produce at Point of Harvest")
        st.markdown("""
        At the **point of harvest**, agricultural produce is measured at **FVLCTS at harvest date**.

        This becomes the **cost** for subsequent accounting under IAS 2 (Inventories).

        **After harvest → IAS 2 applies.** IAS 41 only covers up to the point of harvest.

        | Stage | Standard | Measurement |
        |---|---|---|
        | Growing crops/animals (pre-harvest) | **IAS 41** | FVLCTS |
        | At point of harvest | **IAS 41** | FVLCTS at harvest date |
        | Post-harvest (stored/processed) | **IAS 2** | Lower of cost or NRV |
        | Bearer plants (IAS 16 amendment) | **IAS 16** | Cost or Revaluation model |
        """)

        st.subheader("4. Exception — When Fair Value Cannot Be Reliably Measured")
        st.markdown("""
        If fair value cannot be reliably measured at initial recognition **and no active market exists**, measure at:

        **Cost − Accumulated Depreciation − Accumulated Impairment Losses**

        This exception is presumed NOT to apply after initial recognition (fair value becomes available).

        Once fair value becomes reliably measurable → switch to FVLCTS measurement.
        """)

        st.subheader("5. Bearer Plants (IAS 16 Amendment)")
        st.markdown("""
        **Bearer plants** (e.g., grape vines, rubber trees, oil palm trees) that are used to bear produce over multiple periods are accounted for under **IAS 16** (not IAS 41).

        - Bearer plants themselves → **IAS 16** (cost or revaluation model)
        - **Produce growing on bearer plants** → **IAS 41** (FVLCTS)

        Example: A rubber plantation — the rubber trees (bearer plants) → IAS 16; the rubber latex growing on them → IAS 41.
        """)

        st.subheader("6. Government Grants")
        st.markdown("""
        **Unconditional government grants** relating to biological assets measured at FVLCTS:
        → Recognise in **P&L when the grant becomes receivable**

        **Conditional government grants:**
        → Recognise in P&L **only when conditions are met**

        This differs from IAS 20 which recognises grants systematically over the period they compensate for costs.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Dairy Cattle — FVLCTS Measurement")
        st.markdown("""
        Entity has a herd of 100 dairy cows.

        | | Per Cow | Total Herd |
        |---|---|---|
        | FVLCTS at 1 Jan (opening) | $2,000 | $200,000 |
        | Births during year (20 calves) | $500 each | $10,000 |
        | FVLCTS increase due to growth | $300/cow | $30,000 (100 cows) |
        | Calves FVLCTS at year-end | $650 each | $13,000 (20 calves) |
        | FVLCTS at 31 Dec for original herd | $2,300/cow | $230,000 |

        **Total fair value gain recognised in P&L:**
        - Gain on original herd: $230,000 − $200,000 = $30,000
        - Gain on new calves: $13,000 − $10,000 = $3,000
        - **Total P&L gain = $33,000**

        Journal:
        ```
        Dr  Biological Assets (Cattle)    $33,000
            Cr  Fair Value Gain (P&L)         $33,000
        ```
        """)

        st.subheader("Example 2: Timber Plantation — FVLCTS Movement")
        st.markdown("""
        100 hectares of pine forest (10-year growing cycle):

        | Item | Amount |
        |---|---|
        | Opening FVLCTS | $1,500,000 |
        | Price change (market timber prices rose 5%) | +$75,000 |
        | Physical change (growth — trees matured) | +$120,000 |
        | Harvested timber removed (FVLCTS at harvest) | ($200,000) |
        | Closing FVLCTS | $1,495,000 |

        **P&L gains:** $75,000 (price change) + $120,000 (physical change) = **$195,000**

        IAS 41 encourages disclosure of price change vs physical change components separately.

        Harvested timber at $200,000 → transferred to **IAS 2 Inventory** at that amount.
        """)

        st.subheader("Example 3: Reconciliation of Biological Assets")
        st.markdown("""
        **Movement schedule for dairy herd (year ended 31 Dec 2024):**

        | Item | $000 |
        |---|---|
        | Opening balance (FVLCTS) | 200 |
        | Purchases of cattle | 50 |
        | Gain from price changes → P&L | 18 |
        | Gain from physical changes → P&L | 25 |
        | Decreases due to sales | (35) |
        | Decreases due to harvest (milk at FV) | (15) |
        | **Closing balance (FVLCTS)** | **243** |
        """)

        st.subheader("Example 4: Government Grant — Unconditional")
        st.markdown("""
        Government provides an unconditional grant of $50,000 to a cattle farmer (biological assets at FVLCTS).

        **Treatment:** Recognise entire $50,000 in **P&L immediately** when the grant becomes receivable.

        ```
        Dr  Grant Receivable     $50,000
            Cr  Grant Income (P&L)   $50,000
        ```

        Note: This differs from IAS 20 which spreads the grant over the period it relates to.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Biological Asset or Agricultural Produce Classifier")
        item = st.selectbox("Select item:", [
            "A living dairy cow producing milk",
            "Milk just extracted from a cow",
            "Wool growing on a sheep",
            "Wool just shorn from sheep",
            "Grapes growing on a vine",
            "Harvested grapes in storage",
            "A mature grape vine (bearer plant)",
            "Timber trees in a plantation (not bearer plants)",
            "Cut timber ready for sale"
        ])
        classifications = {
            "A living dairy cow producing milk": ("Biological Asset", "IAS 41", "FVLCTS at each balance sheet date"),
            "Milk just extracted from a cow": ("Agricultural Produce — Post Harvest", "IAS 2", "Measure at FVLCTS at harvest date (becomes IAS 2 cost)"),
            "Wool growing on a sheep": ("Biological Asset (part of sheep)", "IAS 41", "FVLCTS — part of sheep's fair value"),
            "Wool just shorn from sheep": ("Agricultural Produce — Post Harvest", "IAS 2", "FVLCTS at harvest date → IAS 2 inventory cost"),
            "Grapes growing on a vine": ("Agricultural Produce on Bearer Plant", "IAS 41", "FVLCTS — produce growing on bearer plant"),
            "Harvested grapes in storage": ("Agricultural Produce — Post Harvest", "IAS 2", "Carried at FVLCTS at harvest date as deemed cost under IAS 2"),
            "A mature grape vine (bearer plant)": ("Bearer Plant", "IAS 16", "Cost or revaluation model (IAS 16 amendment)"),
            "Timber trees in a plantation (not bearer plants)": ("Biological Asset", "IAS 41", "FVLCTS at each balance sheet date"),
            "Cut timber ready for sale": ("Agricultural Produce — Post Harvest", "IAS 2", "Carried at FVLCTS at harvest date as deemed IAS 2 cost")
        }
        asset_type, standard, treatment = classifications[item]
        if "IAS 41" in standard:
            st.success(f"🌱 **{asset_type}**

Standard: **{standard}**
Measurement: {treatment}")
        elif "IAS 16" in standard:
            st.warning(f"🌳 **{asset_type}**

Standard: **{standard}**
Measurement: {treatment}")
        else:
            st.info(f"📦 **{asset_type}**

Standard: **{standard}**
Measurement: {treatment}")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Biological Asset Fair Value Movement Calculator")
        col1, col2 = st.columns(2)
        with col1:
            opening_ba = st.number_input("Opening FVLCTS ($)", value=200000, step=5000)
            purchases = st.number_input("Purchases during year ($)", value=50000, step=5000)
            price_change = st.number_input("Gain/(loss) from price changes ($)", value=18000, step=1000)
            physical_change = st.number_input("Gain/(loss) from physical changes ($)", value=25000, step=1000)
            sales = st.number_input("Decreases from sales ($)", value=35000, step=1000)
            harvest = st.number_input("Decreases from harvest ($)", value=15000, step=1000)
        with col2:
            closing_ba = opening_ba + purchases + price_change + physical_change - sales - harvest
            total_gain = price_change + physical_change
            st.markdown(f"""
            | Item | $|
            |---|---|
            | Opening balance | {opening_ba:,.0f} |
            | + Purchases | {purchases:,.0f} |
            | + Price change gain/(loss) → P&L | {price_change:,.0f} |
            | + Physical change gain/(loss) → P&L | {physical_change:,.0f} |
            | − Sales | ({sales:,.0f}) |
            | − Harvest | ({harvest:,.0f}) |
            | **Closing FVLCTS** | **{closing_ba:,.0f}** |
            | **Total P&L gain/(loss)** | **{total_gain:,.0f}** |
            """)

    with tab4:
        st.header("Visualizations")

        st.subheader("Biological Asset Value Growth Over Time (Cattle Herd)")
        years = list(range(0, 11))
        herd_size = [100 + y*5 for y in years]
        fv_per_head = [2000 * (1.04)**y for y in years]
        total_fv = [h * f for h, f in zip(herd_size, fv_per_head)]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=years, y=total_fv, name="Total Herd FVLCTS", marker_color="#34D399"))
        fig.add_trace(go.Scatter(x=years, y=fv_per_head, name="FV per Head ($)", yaxis="y2", line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig.update_layout(title="Dairy Cattle Herd — Total FVLCTS and Per-Head Value Over 10 Years",
                          xaxis_title="Year", yaxis=dict(title="Total Herd Value ($)"),
                          yaxis2=dict(title="FV per Head ($)", overlaying="y", side="right"), height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("IAS 41 vs IAS 2 — Agricultural Life Cycle")
        fig2 = go.Figure()
        stages = ["Seed/Birth", "Growing", "Maturing", "Harvest Point", "Storage", "Processing", "Sale"]
        standards_used = ["IAS 41", "IAS 41", "IAS 41", "IAS 41 → IAS 2", "IAS 2", "IAS 2", "IAS 2"]
        values_bar = [1, 2, 3, 4, 4, 4.5, 5]
        colors_bar = ["#34D399","#34D399","#34D399","#F59E0B","#2563EB","#2563EB","#2563EB"]
        fig2.add_trace(go.Bar(x=stages, y=values_bar, marker_color=colors_bar,
                              text=standards_used, textposition="inside",
                              textfont=dict(color="white", size=10)))
        fig2.update_layout(title="Agricultural Product Lifecycle — IAS 41 (green) vs IAS 2 (blue)",
                           yaxis=dict(visible=False), height=350)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IAS 41, biological assets are measured at:**")
        q1 = st.radio("", [
            "Historical cost less accumulated depreciation",
            "Net realisable value",
            "Fair value less costs to sell",
            "The lower of cost or fair value"
        ], key="ias41q1")
        if st.button("Check Answer", key="ias41c1"):
            if q1 == "Fair value less costs to sell":
                st.success("✅ Correct! IAS 41 requires biological assets to be measured at FAIR VALUE LESS COSTS TO SELL (FVLCTS) at every balance sheet date. Changes in FVLCTS go to P&L.")
            else:
                st.error("❌ Biological assets → Fair Value Less Costs to Sell (FVLCTS) at every balance sheet date.")

        st.markdown("---")
        st.markdown("**2. At the point of harvest, agricultural produce is measured at:**")
        q2 = st.radio("", [
            "Historical cost",
            "Net realisable value",
            "Fair value less costs to sell at the date of harvest",
            "Standard cost"
        ], key="ias41q2")
        if st.button("Check Answer", key="ias41c2"):
            if q2 == "Fair value less costs to sell at the date of harvest":
                st.success("✅ Correct! At the harvest point, agricultural produce is measured at FVLCTS at the date of harvest. This then becomes the cost for subsequent IAS 2 accounting.")
            else:
                st.error("❌ At harvest: FVLCTS at harvest date. This becomes the IAS 2 'cost' for post-harvest inventory accounting.")

        st.markdown("---")
        st.markdown("**3. Bearer plants (e.g., grape vines, rubber trees) are accounted for under:**")
        q3 = st.radio("", [
            "IAS 41 at fair value less costs to sell",
            "IAS 2 as inventory",
            "IAS 16 Property, Plant and Equipment",
            "IAS 40 Investment Property"
        ], key="ias41q3")
        if st.button("Check Answer", key="ias41c3"):
            if q3 == "IAS 16 Property, Plant and Equipment":
                st.success("✅ Correct! Bearer plants are accounted for under IAS 16 (cost or revaluation model). However, the agricultural produce GROWING ON the bearer plants is still under IAS 41 (FVLCTS).")
            else:
                st.error("❌ Bearer plants → IAS 16. But produce growing on them → IAS 41 at FVLCTS.")

        st.markdown("---")
        st.markdown("**4. Gains and losses from changes in fair value of biological assets are recognised in:**")
        q4 = st.radio("", [
            "Other Comprehensive Income (OCI)",
            "Profit or Loss (P&L)",
            "Revaluation Reserve in equity",
            "Deferred to the period of sale"
        ], key="ias41q4")
        if st.button("Check Answer", key="ias41c4"):
            if q4 == "Profit or Loss (P&L)":
                st.success("✅ Correct! All gains and losses from changes in FVLCTS of biological assets go directly to P&L — both price changes and physical changes from biological transformation.")
            else:
                st.error("❌ FVLCTS changes on biological assets → P&L immediately. Not OCI.")

        st.markdown("---")
        st.markdown("**5. Under IAS 41, an unconditional government grant related to biological assets at FVLCTS is recognised:**")
        q5 = st.radio("", [
            "Over the useful life of the biological asset",
            "When conditions attached to it are met",
            "In P&L when the grant becomes receivable",
            "As deferred income on the balance sheet"
        ], key="ias41q5")
        if st.button("Check Answer", key="ias41c5"):
            if q5 == "In P&L when the grant becomes receivable":
                st.success("✅ Correct! IAS 41 states unconditional grants related to biological assets at FVLCTS are recognised in P&L when the grant becomes receivable — different from IAS 20 systematic recognition.")
            else:
                st.error("❌ Unconditional grant under IAS 41 → P&L immediately when receivable. This differs from IAS 20 treatment.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. IAS 41 Scope
        - **Biological assets** (living animals and plants)
        - **Agricultural produce** at the point of harvest
        - **Government grants** related to biological assets at FVLCTS

        ### 2. Core Measurement Rule
        ```
        Biological Assets = Fair Value Less Costs to Sell (FVLCTS)
        → At EVERY balance sheet date
        → Changes in FVLCTS → P&L
        ```

        ### 3. Life Cycle Accounting
        | Stage | Standard | Measurement |
        |---|---|---|
        | Living/Growing | IAS 41 | FVLCTS |
        | At harvest point | IAS 41 | FVLCTS at harvest date |
        | Post-harvest | IAS 2 | Lower of cost (= harvest FVLCTS) or NRV |
        | Bearer plants | IAS 16 | Cost or revaluation model |

        ### 4. Bearer Plants Exception
        - Bearer plants → **IAS 16** (not IAS 41)
        - Produce on bearer plants → **IAS 41** (FVLCTS)

        ### 5. Government Grants
        - Unconditional → **P&L immediately** when receivable
        - Conditional → **P&L when conditions are met**

        ### 6. P&L Disclosure (encouraged)
        - Separate disclosure of: price changes vs physical changes from biological transformation
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Biological Assets → FVLCTS (always, every balance sheet date)
FVLCTS changes → P&L (not OCI)
At harvest → FVLCTS at harvest = IAS 2 cost
Post-harvest → IAS 2 applies
Bearer plants → IAS 16 (not IAS 41)
Unconditional grants → P&L when receivable
        """)

        st.success("🎓 **IAS 41 Complete!** You can now apply FVLCTS to biological assets, account for harvested produce and bearer plants, and handle agricultural government grants.")
        st.info("💡 **Next**: IFRS 1 — First-time Adoption of IFRS")

if __name__ == "__main__":
    show()