import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏷️ IFRS 5: Non-current Assets Held for Sale and Discontinued Operations")
    st.markdown("*Master classification, measurement and presentation of assets held for sale and discontinued operations*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Two Key Concepts")
        st.markdown("""
        **IFRS 5** addresses two related but distinct topics:
        1. **Classification and measurement** of non-current assets (or disposal groups) held for sale
        2. **Presentation** of discontinued operations

        A **disposal group** is a group of assets to be disposed of together in a single transaction, including any directly associated liabilities.
        """)

        st.subheader("2. Classification as Held for Sale — Strict Criteria")
        st.markdown("""
        An asset (or disposal group) is classified as **held for sale** ONLY when ALL of the following are met:
        1. The asset is **available for immediate sale** in its present condition
        2. The sale is **highly probable**
        3. Management is **committed to a plan** to sell
        4. An **active programme to locate a buyer** has been initiated
        5. The asset is being **actively marketed** at a reasonable price relative to fair value
        6. The sale is expected to be **completed within one year** of classification
        7. It is **unlikely** that the plan will change significantly or be withdrawn

        **Extension beyond one year** is permitted only if the delay is caused by events/circumstances beyond the entity's control AND the entity remains committed to the plan.
        """)

        st.subheader("3. Measurement of Assets Held for Sale")
        st.markdown("""
        ```
        Measure at: LOWER OF Carrying Amount and Fair Value Less Costs to Sell (FVLCTS)
        ```

        **Key rules:**
        - **STOP depreciating/amortising** once classified as held for sale
        - Recognise an **impairment loss** if FVLCTS < carrying amount → P&L
        - If FVLCTS subsequently increases → recognise a **gain** (but not exceeding cumulative impairment previously recognised)
        - Present **separately** on the face of the balance sheet (current assets/liabilities section) — do NOT reclassify comparative balance sheets
        """)

        st.subheader("4. Discontinued Operations")
        st.markdown("""
        A **discontinued operation** is a component of an entity that either has been disposed of OR is classified as held for sale, AND:
        - Represents a **separate major line of business** or geographical area of operations, OR
        - Is part of a single coordinated plan to dispose of a separate major line of business/geographical area, OR
        - Is a **subsidiary acquired exclusively with a view to resale**

        **Presentation:** Single amount on the face of the P&L showing:
        - Post-tax profit/loss of discontinued operations, PLUS
        - Post-tax gain/loss on remeasurement to FVLCTS or on disposal

        **Comparative periods ARE restated** for discontinued operations (unlike held-for-sale balance sheet items).
        """)

        st.subheader("5. Disposal Groups — Allocation of Impairment")
        st.markdown("""
        When a disposal group is impaired, allocate the loss in this order:
        1. First, reduce **goodwill** allocated to the disposal group (if any)
        2. Then, reduce the carrying amounts of the remaining non-current assets **pro-rata**

        **Excluded from remeasurement under IFRS 5** (continue to apply their own standard):
        - Financial assets (IFRS 9)
        - Deferred tax assets (IAS 12)
        - Employee benefit assets (IAS 19)
        - Investment property at fair value (IAS 40)
        - Biological assets at FV (IAS 41)
        """)

        st.subheader("6. Changes in Plan / Reclassification Out of Held for Sale")
        st.markdown("""
        If an asset no longer meets the held-for-sale criteria:
        - Measure at the **LOWER OF**:
          - Carrying amount **before** classification as held for sale, adjusted for any depreciation/amortisation that would have been recognised had it not been classified as held for sale, OR
          - **Recoverable amount** at the date of the decision not to sell

        Any adjustment → included in profit/loss from **continuing operations**.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Classification and Measurement — Held for Sale")
        st.markdown("""
        **Facts:**
        - Manufacturing equipment: carrying amount $800,000
        - Board approves sale plan on 1 October 2024; meets all 7 IFRS 5 criteria
        - Fair value: $750,000 | Estimated costs to sell: $30,000

        **FVLCTS = $750,000 − $30,000 = $720,000**

        **Measurement = LOWER OF Carrying Amount ($800,000) and FVLCTS ($720,000) = $720,000**

        **Impairment loss = $800,000 − $720,000 = $80,000 → P&L**

        ```
        Dr  Impairment Loss (P&L)        $80,000
            Cr  Accumulated Impairment        $80,000
        ```
        From 1 October 2024, **STOP depreciating** the equipment.
        """)

        st.subheader("Example 2: Subsequent Increase in Fair Value")
        st.markdown("""
        **Continuing Example 1:** At year-end 31 December 2024, FVLCTS increases to $760,000.

        **Gain recognised = $760,000 − $720,000 = $40,000**

        Cap check: cumulative impairment previously recognised = $80,000. Gain of $40,000 is within this cap → fully recognised.

        ```
        Dr  Accumulated Impairment        $40,000
            Cr  Gain on Remeasurement (P&L)   $40,000
        ```
        New carrying amount = $760,000
        """)

        st.subheader("Example 3: Discontinued Operations — P&L Presentation")
        st.markdown("""
        **Entity sells its entire Consumer Electronics Division (a separate major line of business) on 30 June 2024.**

        | | 2024 ($000) | 2023 ($000, restated) |
        |---|---|---|
        | **Continuing operations:** | | |
        | Revenue | 18,000 | 16,500 |
        | Profit from continuing operations | 2,800 | 2,200 |
        | **Discontinued operations:** | | |
        | Post-tax profit/(loss) from Consumer Electronics | 450 | 600 |
        | Post-tax loss on remeasurement to FVLCTS | (200) | — |
        | **Total discontinued operations** | **250** | **600** |
        | **Total Profit for the Year** | **3,050** | **2,800** |

        Note: The 2023 comparative is **restated** to separate the discontinued operation results.
        """)

        st.subheader("Example 4: Disposal Group — Impairment Allocation")
        st.markdown("""
        **Disposal Group (Division X):**

        | Asset | Carrying Amount |
        |---|---|
        | Goodwill | $150,000 |
        | PPE | $500,000 |
        | Inventory (IAS 2 — excluded from IFRS 5 remeasurement) | $200,000 |
        | **Total** | **$850,000** |

        **FVLCTS of disposal group = $600,000**
        **Total impairment = $850,000 − $600,000 = $250,000**

        **Allocation:**
        1. Goodwill first: $150,000 (fully written off)
        2. Remaining $100,000 allocated to PPE only (inventory excluded — already at lower of cost/NRV per IAS 2)
        3. **PPE after impairment: $500,000 − $100,000 = $400,000**
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Held-for-Sale Classification Checker")
        st.markdown("Check whether an asset meets ALL IFRS 5 criteria:")
        c1 = st.checkbox("Available for immediate sale in present condition?")
        c2 = st.checkbox("Sale is highly probable?")
        c3 = st.checkbox("Management committed to a formal plan to sell?")
        c4 = st.checkbox("Active programme to locate a buyer initiated?")
        c5 = st.checkbox("Actively marketed at a reasonable price?")
        c6 = st.checkbox("Sale expected to complete within 12 months?")
        c7 = st.checkbox("Unlikely that the plan will change significantly?")

        if st.button("Check Classification"):
            criteria = [c1, c2, c3, c4, c5, c6, c7]
            if all(criteria):
                st.success("✅ **CLASSIFY AS HELD FOR SALE** — All 7 IFRS 5 criteria are met.")
            else:
                missing_count = criteria.count(False)
                st.error(f"❌ **DO NOT CLASSIFY AS HELD FOR SALE** — {missing_count} criteria not yet met. Continue normal classification (e.g., PPE under IAS 16) until ALL criteria are satisfied.")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Held-for-Sale Measurement Calculator")
        col1, col2 = st.columns(2)
        with col1:
            carrying_hfs = st.number_input("Carrying Amount Before Reclassification ($)", value=800000, step=10000)
            fv_hfs = st.number_input("Fair Value ($)", value=750000, step=10000)
            costs_to_sell = st.number_input("Estimated Costs to Sell ($)", value=30000, step=1000)
        with col2:
            fvlcts = fv_hfs - costs_to_sell
            measurement = min(carrying_hfs, fvlcts)
            impairment_hfs = max(0, carrying_hfs - fvlcts)
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | Fair Value | ${fv_hfs:,.0f} |
            | Less: Costs to sell | (${costs_to_sell:,.0f}) |
            | **FVLCTS** | **${fvlcts:,.0f}** |
            | Carrying Amount | ${carrying_hfs:,.0f} |
            | **New Measurement (lower of)** | **${measurement:,.0f}** |
            | **Impairment Loss → P&L** | **${impairment_hfs:,.0f}** |
            """)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Discontinued Operations P&L Builder")
        col1, col2 = st.columns(2)
        with col1:
            cont_revenue = st.number_input("Continuing Operations Revenue ($000)", value=18000)
            cont_profit = st.number_input("Continuing Operations Profit ($000)", value=2800)
        with col2:
            disc_profit = st.number_input("Discontinued Ops Post-tax Profit ($000)", value=450)
            disc_remeasure = st.number_input("Post-tax Gain/(Loss) on Remeasurement ($000, use negative for loss)", value=-200)

        if st.button("Build P&L Presentation"):
            total_disc = disc_profit + disc_remeasure
            total_profit = cont_profit + total_disc
            pl_table = pd.DataFrame({
                "Line Item": ["Revenue (Continuing)", "Profit from Continuing Operations",
                              "Post-tax Profit from Discontinued Operations", "Post-tax Gain/(Loss) on Remeasurement",
                              "Total Discontinued Operations", "**Total Profit for the Year**"],
                "Amount ($000)": [f"{cont_revenue:,.0f}", f"{cont_profit:,.0f}",
                                   f"{disc_profit:,.0f}", f"{disc_remeasure:,.0f}",
                                   f"{total_disc:,.0f}", f"**{total_profit:,.0f}**"]
            })
            st.dataframe(pl_table, use_container_width=True, hide_index=True)

    with tab4:
        st.header("Visualizations")

        st.subheader("Held-for-Sale Measurement Over Time")
        periods = ["Classification\nDate", "Year-End 1", "Year-End 2 (sold)"]
        carrying_vals = [720000, 760000, 760000]
        fv_vals_chart = [720000, 760000, 760000]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=periods, y=carrying_vals, name="Carrying Amount (lower of CA/FVLCTS)", marker_color="#2563EB"))
        fig.update_layout(title="Held for Sale — Carrying Amount Path (No Depreciation)", yaxis_title="Amount ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Continuing vs Discontinued Operations — P&L Split")
        categories_disc = ["2023\n(Restated)", "2024"]
        cont_vals = [2200, 2800]
        disc_vals = [600, 250]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=categories_disc, y=cont_vals, name="Continuing Operations", marker_color="#34D399"))
        fig2.add_trace(go.Bar(x=categories_disc, y=disc_vals, name="Discontinued Operations", marker_color="#F59E0B"))
        fig2.update_layout(barmode="stack", title="Profit Split — Continuing vs Discontinued ($000)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. A non-current asset classified as held for sale is measured at:**")
        q1 = st.radio("", [
            "Fair value only",
            "Carrying amount only",
            "The lower of carrying amount and fair value less costs to sell",
            "The higher of carrying amount and fair value less costs to sell"
        ], key="ifrs5q1")
        if st.button("Check Answer", key="ifrs5c1"):
            if q1 == "The lower of carrying amount and fair value less costs to sell":
                st.success("✅ Correct! IFRS 5 requires measurement at the LOWER of carrying amount and FVLCTS — this is a conservative approach reflecting impending sale.")
            else:
                st.error("❌ Held for sale = LOWER of carrying amount and FVLCTS (not higher, and not either alone).")

        st.markdown("---")
        st.markdown("**2. Once an asset is classified as held for sale, depreciation is:**")
        q2 = st.radio("", [
            "Continued at the same rate",
            "Accelerated to write off the asset faster",
            "Stopped immediately",
            "Reduced by 50%"
        ], key="ifrs5q2")
        if st.button("Check Answer", key="ifrs5c2"):
            if q2 == "Stopped immediately":
                st.success("✅ Correct! IFRS 5 requires depreciation/amortisation to STOP once an asset is classified as held for sale, since the asset's value will now be recovered through sale rather than use.")
            else:
                st.error("❌ Depreciation/amortisation must STOP upon classification as held for sale.")

        st.markdown("---")
        st.markdown("**3. For a sale to be classified as 'highly probable' and meet held-for-sale criteria, the expected completion period is normally:**")
        q3 = st.radio("", [
            "Within 6 months",
            "Within 1 year of classification",
            "Within 2 years",
            "No time limit applies"
        ], key="ifrs5q3")
        if st.button("Check Answer", key="ifrs5c3"):
            if q3 == "Within 1 year of classification":
                st.success("✅ Correct! IFRS 5 expects the sale to complete within ONE YEAR of classification. Extensions beyond a year are permitted only due to events beyond the entity's control.")
            else:
                st.error("❌ The standard expectation is completion WITHIN ONE YEAR, with limited exceptions for circumstances beyond the entity's control.")

        st.markdown("---")
        st.markdown("**4. Discontinued operations are presented in the P&L as:**")
        q4 = st.radio("", [
            "Spread across each individual revenue and expense line",
            "A single line showing post-tax profit/loss and post-tax gain/loss on remeasurement or disposal",
            "Only in the notes, not on the face of P&L",
            "Combined with continuing operations with a footnote"
        ], key="ifrs5q4")
        if st.button("Check Answer", key="ifrs5c4"):
            if q4 == "A single line showing post-tax profit/loss and post-tax gain/loss on remeasurement or disposal":
                st.success("✅ Correct! IFRS 5 requires a SINGLE AMOUNT on the face of P&L for discontinued operations, comprising post-tax profit/loss PLUS post-tax gain/loss on remeasurement or disposal.")
            else:
                st.error("❌ Discontinued operations = single line on P&L face (post-tax profit/loss + post-tax remeasurement/disposal gain/loss).")

        st.markdown("---")
        st.markdown("**5. When impairing a disposal group, the loss is first allocated to:**")
        q5 = st.radio("", [
            "Inventory within the group",
            "Financial assets within the group",
            "Goodwill allocated to the disposal group",
            "Cash and cash equivalents"
        ], key="ifrs5q5")
        if st.button("Check Answer", key="ifrs5c5"):
            if q5 == "Goodwill allocated to the disposal group":
                st.success("✅ Correct! Following the same logic as CGU impairment (IAS 36), goodwill is written off FIRST, then remaining loss is allocated pro-rata to other non-current assets within scope.")
            else:
                st.error("❌ Disposal group impairment: GOODWILL first, then pro-rata to remaining qualifying non-current assets. Inventory/financial assets are excluded (governed by their own standards).")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Held-for-Sale Classification — 7 Criteria (ALL must be met)
        1. Available for immediate sale
        2. Sale highly probable
        3. Management committed to plan
        4. Active programme to find buyer
        5. Actively marketed at reasonable price
        6. Expected completion within 1 year
        7. Unlikely the plan changes significantly

        ### 2. Measurement
        ```
        Carrying Amount = LOWER OF (Carrying Amount, Fair Value Less Costs to Sell)
        STOP depreciation/amortisation upon classification
        ```

        ### 3. Discontinued Operations
        - Major line of business OR geographical area being disposed
        - Single line in P&L: post-tax profit/loss + post-tax remeasurement/disposal gain/loss
        - Comparatives ARE restated (unlike balance sheet held-for-sale items)

        ### 4. Disposal Group Impairment Order
        1. Goodwill first
        2. Then pro-rata to other qualifying non-current assets
        (Financial assets, deferred tax, employee benefits excluded — apply own standards)

        ### 5. Reversal/Reclassification
        - Gains on FVLCTS increase: recognise, capped at cumulative impairment
        - If criteria no longer met: measure at LOWER of (adjusted pre-classification carrying amount) or (recoverable amount)
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Held for Sale = LOWER OF (Carrying Amount, FVLCTS)
STOP depreciation immediately upon classification
Discontinued Ops = single P&L line; comparatives RESTATED
Disposal group impairment: Goodwill first, then pro-rata
Sale expected within 1 YEAR (exceptions: beyond entity's control)
        """)

        st.success("🎓 **IFRS 5 Complete!** You can now classify and measure held-for-sale assets, present discontinued operations, and handle disposal group impairments.")
        st.info("💡 **Next**: IFRS 7 — Financial Instruments: Disclosures")

if __name__ == "__main__":
    show()