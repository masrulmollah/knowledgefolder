import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📦 IAS 2: Inventories")
    st.markdown("*Master the measurement, cost formulas, and write-down rules for inventory under IFRS*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Scope")
        st.markdown("""
        **IAS 2** prescribes the accounting treatment for inventories, including the **determination of cost** and
        its subsequent recognition as an expense.

        **Inventories are assets:**
        - Held for sale in the ordinary course of business
        - In the process of production for such sale (WIP)
        - In the form of materials to be consumed in production or rendering services

        **IAS 2 does NOT apply to:**
        - WIP arising from construction contracts (IFRS 15)
        - Financial instruments (IFRS 9)
        - Biological assets (IAS 41) and agricultural produce at point of harvest
        - Commodity broker-traders who measure at FV less costs to sell
        - Producers of agricultural and forest products measured at NRV
        """)

        st.subheader("2. Measurement — Cost of Inventories")
        st.markdown("""
        **Inventories must be measured at the LOWER OF cost and net realisable value (NRV).**

        **Cost of inventories includes:**
        """)
        cost_data = {
            "Cost Component": ["Purchase costs", "Conversion costs", "Other costs"],
            "Includes": [
                "Purchase price + import duties + transport + handling; LESS trade discounts, rebates",
                "Direct labour + fixed & variable production overheads (based on normal capacity)",
                "Costs to bring inventory to its present location and condition"
            ],
            "Excludes": [
                "Abnormal waste, storage costs (unless in production), admin overheads, selling costs",
                "Idle capacity costs go to P&L; abnormal waste excluded",
                "Borrowing costs (unless IAS 23 qualifying asset)"
            ]
        }
        st.dataframe(pd.DataFrame(cost_data), use_container_width=True, hide_index=True)

        st.subheader("3. Cost Formulas")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **FIFO** (First In, First Out)
            - Oldest inventory used first
            - Closing stock = most recent costs
            - Higher profit in rising price environment
            - Allowed under IAS 2
            """)
        with col2:
            st.markdown("""
            **Weighted Average Cost**
            - Average cost applied to all units
            - Smooths out price fluctuations
            - Periodic or perpetual WAC
            - Allowed under IAS 2
            """)
        with col3:
            st.markdown("""
            **LIFO** ❌
            - Last in, First Out
            - **NOT permitted under IAS 2**
            - Allowed under US GAAP
            - Key IFRS vs US GAAP difference
            """)

        st.markdown("""
        > **Specific Identification** must be used for items that are not ordinarily interchangeable and 
        goods/services produced for specific projects.
        """)

        st.subheader("4. Net Realisable Value (NRV)")
        st.markdown("""
        **NRV = Estimated selling price − Estimated costs of completion − Estimated selling costs**

        **When to write down to NRV:**
        - Inventory is damaged
        - Inventory is wholly or partially obsolete
        - Selling prices have declined
        - Estimated costs of completion or selling have increased

        **Write-down rules:**
        - Write down on an **item-by-item** basis (or by groups of similar items)
        - Write-down is recognised as an expense in the period it occurs
        - **Reversals are required** if NRV subsequently recovers (limited to original write-down amount)
        - Reversal is recognised as a **reduction in cost of goods sold**

        **NRV vs Fair Value:**
        NRV is entity-specific (what *this* entity can realise).
        Fair value is market-based (what *market participants* would receive — IFRS 13).
        """)

        st.subheader("5. Recognition as Expense")
        st.markdown("""
        When inventories are sold, the carrying amount is recognised as an expense (Cost of Goods Sold) in the
        same period as the related revenue — **matching principle**.

        Any write-down to NRV and any inventory losses are also recognised as expense in the period of write-down.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: FIFO vs Weighted Average Cost")
        st.markdown("""
        **Purchases and sales during January 2024:**
        - 1 Jan: Opening inventory — 100 units @ $10 = $1,000
        - 10 Jan: Purchase — 200 units @ $12 = $2,400
        - 20 Jan: Sale — 250 units
        - 31 Jan: Closing inventory — 50 units
        """)

        method_data = {
            "Method": ["FIFO", "Weighted Average Cost"],
            "Cost of Sales (250 units)": [
                "(100 × $10) + (150 × $12) = $2,800",
                "WAC = ($1,000 + $2,400) / 300 = $11.33\n250 × $11.33 = $2,833"
            ],
            "Closing Inventory (50 units)": [
                "50 × $12 = $600",
                "50 × $11.33 = $567"
            ],
            "Gross Profit (Sales $3,750)": [
                "$3,750 − $2,800 = $950",
                "$3,750 − $2,833 = $917"
            ]
        }
        st.dataframe(pd.DataFrame(method_data), use_container_width=True, hide_index=True)
        st.info("📌 In a rising price environment, FIFO produces higher profit and higher closing inventory than WAC.")

        st.subheader("Example 2: NRV Write-Down")
        nrv_data = {
            "Product": ["Widget A", "Widget B", "Widget C"],
            "Cost ($)": [50, 80, 30],
            "Estimated Selling Price ($)": [70, 75, 45],
            "Estimated Completion Costs ($)": [5, 0, 8],
            "Estimated Selling Costs ($)": [3, 4, 2],
            "NRV ($)": [62, 71, 35],
            "Lower of Cost/NRV": [50, 71, 30],
            "Write-Down Required ($)": [0, 9, 0]
        }
        st.dataframe(pd.DataFrame(nrv_data), use_container_width=True, hide_index=True)
        st.markdown("""
        - **Widget A**: NRV $62 > Cost $50 → carry at cost $50 (no write-down)
        - **Widget B**: NRV $71 < Cost $80 → write down to NRV $71 (write-down of $9)
        - **Widget C**: NRV $35 > Cost $30 → carry at cost $30 (no write-down)
        """)

        st.subheader("Example 3: Overhead Absorption — Normal vs Abnormal")
        st.markdown("""
        **Factory produces 10,000 units per month (normal capacity). Fixed overheads = $50,000/month.**

        | Scenario | Actual Production | Fixed OH per Unit | Treatment |
        |----------|------------------|-------------------|-----------|
        | Normal month | 10,000 units | $50,000 / 10,000 = $5.00 | $5.00 absorbed into inventory |
        | Low activity | 5,000 units | $50,000 / 10,000 = $5.00 | Only $25,000 absorbed; $25,000 idle capacity → P&L expense |
        | Overproduction | 12,000 units | $50,000 / 12,000 = $4.17 | Use $4.17 actual rate (cannot exceed normal capacity rate) |

        > **Key rule:** Fixed overhead absorption is based on **normal capacity**, not actual production.
        Unabsorbed overheads due to idle capacity are expensed immediately — not hidden in inventory.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Inventory Cost Calculator (FIFO & WAC)")

        st.markdown("Enter transactions below:")
        col1, col2 = st.columns(2)
        with col1:
            open_units = st.number_input("Opening Units", 0, 10000, 100, key="inv_open_u")
            open_cost = st.number_input("Opening Unit Cost ($)", 0.0, 1000.0, 10.0, key="inv_open_c")
            purch_units = st.number_input("Purchase Units", 0, 10000, 200, key="inv_pu")
            purch_cost = st.number_input("Purchase Unit Cost ($)", 0.0, 1000.0, 12.0, key="inv_pc")
        with col2:
            sold_units = st.number_input("Units Sold", 0, 10000, 250, key="inv_sold")
            selling_price = st.number_input("Selling Price per Unit ($)", 0.0, 1000.0, 15.0, key="inv_sp")

        if st.button("Calculate", key="inv_calc"):
            total_units = open_units + purch_units
            closing_units = total_units - sold_units

            if closing_units < 0:
                st.error("❌ Cannot sell more units than available!")
            else:
                # FIFO
                if sold_units <= open_units:
                    fifo_cos = sold_units * open_cost
                    fifo_closing = (open_units - sold_units) * open_cost + purch_units * purch_cost
                else:
                    fifo_cos = open_units * open_cost + (sold_units - open_units) * purch_cost
                    fifo_closing = closing_units * purch_cost

                # WAC
                total_cost = open_units * open_cost + purch_units * purch_cost
                wac = total_cost / total_units if total_units > 0 else 0
                wac_cos = sold_units * wac
                wac_closing = closing_units * wac

                revenue = sold_units * selling_price

                result_data = {
                    "Metric": ["Total Cost Available", "Cost of Sales", "Closing Inventory", "Gross Profit"],
                    "FIFO ($)": [f"{total_cost:,.2f}", f"{fifo_cos:,.2f}", f"{fifo_closing:,.2f}", f"{revenue - fifo_cos:,.2f}"],
                    "WAC ($)": [f"{total_cost:,.2f}", f"{wac_cos:,.2f}", f"{wac_closing:,.2f}", f"{revenue - wac_cos:,.2f}"]
                }
                st.dataframe(pd.DataFrame(result_data), use_container_width=True, hide_index=True)
                st.caption(f"WAC per unit: ${wac:.4f} | Revenue: ${revenue:,.2f}")

        st.markdown("---")
        st.subheader("🔧 Tool 2: NRV Write-Down Calculator")
        col1, col2 = st.columns(2)
        with col1:
            cost = st.number_input("Cost per unit ($)", 0.0, 10000.0, 80.0, key="nrv_cost")
            sell_price = st.number_input("Estimated selling price ($)", 0.0, 10000.0, 90.0, key="nrv_sp")
        with col2:
            completion = st.number_input("Costs to complete ($)", 0.0, 5000.0, 8.0, key="nrv_comp")
            sell_costs = st.number_input("Costs to sell ($)", 0.0, 5000.0, 5.0, key="nrv_sc")
            units = st.number_input("Number of units", 1, 100000, 100, key="nrv_units")

        if st.button("Calculate NRV", key="nrv_calc"):
            nrv = sell_price - completion - sell_costs
            carrying = min(cost, nrv)
            write_down = max(0, cost - nrv)
            st.markdown(f"**NRV per unit = ${sell_price:.2f} − ${completion:.2f} − ${sell_costs:.2f} = ${nrv:.2f}**")
            if nrv >= cost:
                st.success(f"✅ No write-down required. Carry at cost: **${cost:.2f}** per unit (${cost*units:,.2f} total)")
            else:
                st.warning(f"⚠️ Write-down required!\n\nCarrying value: **${nrv:.2f}** per unit\nWrite-down: **${write_down:.2f}** per unit\nTotal write-down expense: **${write_down * units:,.2f}**")

    with tab4:
        st.header("Visualizations")

        st.subheader("FIFO vs WAC: Impact on Profit in Rising Price Environment")
        prices = list(range(10, 21))
        fifo_profits = []
        wac_profits = []
        for p in prices:
            opening = 100 * 10
            purchase = 200 * p
            total = opening + purchase
            wac_v = total / 300
            fifo_cos = 100 * 10 + 150 * p
            wac_cos = 250 * wac_v
            rev = 250 * (p * 1.3)
            fifo_profits.append(rev - fifo_cos)
            wac_profits.append(rev - wac_cos)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=prices, y=fifo_profits, name="FIFO Profit", line=dict(color="#2563EB", width=2)))
        fig.add_trace(go.Scatter(x=prices, y=wac_profits, name="WAC Profit", line=dict(color="#10B981", width=2)))
        fig.update_layout(title="FIFO vs WAC Gross Profit — Rising Purchase Prices",
                          xaxis_title="Purchase Price ($)", yaxis_title="Gross Profit ($)", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Overhead Absorption — Normal vs Actual Capacity")
        capacities = [4000, 6000, 8000, 10000, 12000, 14000]
        normal_cap = 10000
        fixed_oh = 50000
        absorbed = [min(c, normal_cap) / normal_cap * fixed_oh for c in capacities]
        unabsorbed = [max(0, fixed_oh - a) for a in absorbed]

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=[str(c) for c in capacities], y=absorbed, name="Absorbed into Inventory", marker_color="#34D399"))
        fig2.add_trace(go.Bar(x=[str(c) for c in capacities], y=unabsorbed, name="Idle Capacity → P&L Expense", marker_color="#F87171"))
        fig2.update_layout(barmode="stack", title="Fixed Overhead Absorption (Normal Capacity = 10,000 units)",
                           xaxis_title="Actual Production (Units)", yaxis_title="Fixed Overhead ($)", height=400)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IAS 2, which cost formula is NOT permitted?**")
        q1 = st.radio("", ["FIFO", "Weighted Average Cost", "LIFO", "Specific Identification"], key="ias2q1")
        if st.button("Check Answer", key="ias2c1"):
            if q1 == "LIFO":
                st.success("✅ Correct! LIFO (Last In, First Out) is explicitly prohibited by IAS 2. Only FIFO, WAC and specific identification are permitted.")
            else:
                st.error("❌ Incorrect. IAS 2 prohibits LIFO. FIFO, WAC and specific identification are all allowed.")

        st.markdown("---")
        st.markdown("**2. NRV is defined as:**")
        q2 = st.radio("", [
            "The current replacement cost of inventory",
            "Fair value less costs to sell",
            "Estimated selling price less estimated costs of completion and estimated selling costs",
            "The lower of historical cost and current market price"
        ], key="ias2q2")
        if st.button("Check Answer", key="ias2c2"):
            if q2 == "Estimated selling price less estimated costs of completion and estimated selling costs":
                st.success("✅ Correct! NRV = Estimated selling price − Estimated costs of completion − Estimated selling costs. This is entity-specific, unlike fair value.")
            else:
                st.error("❌ Incorrect. NRV is entity-specific: estimated selling price minus costs to complete and costs to sell.")

        st.markdown("---")
        st.markdown("**3. If NRV recovers after an inventory write-down, the reversal should be:**")
        q3 = st.radio("", [
            "Ignored — write-downs are permanent",
            "Recognised in OCI",
            "Recognised as a reduction in cost of goods sold (i.e., as income)",
            "Added to a revaluation reserve"
        ], key="ias2q3")
        if st.button("Check Answer", key="ias2c3"):
            if q3 == "Recognised as a reduction in cost of goods sold (i.e., as income)":
                st.success("✅ Correct! IAS 2 requires reversal of write-downs when NRV recovers. The reversal reduces COGS (or the expense line where the write-down was recorded).")
            else:
                st.error("❌ Incorrect. IAS 2 mandates reversal when NRV recovers — recognised as a reduction in the amount of inventory expense (COGS).")

        st.markdown("---")
        st.markdown("**4. Fixed overhead absorption into inventory cost is based on:**")
        q4 = st.radio("", [
            "Actual production in the period",
            "Maximum possible production capacity",
            "Normal production capacity",
            "Budgeted production for the following period"
        ], key="ias2q4")
        if st.button("Check Answer", key="ias2c4"):
            if q4 == "Normal production capacity":
                st.success("✅ Correct! IAS 2 requires fixed overheads to be absorbed based on normal production capacity. Under-absorption due to idle capacity is expensed immediately, not stored in inventory.")
            else:
                st.error("❌ Incorrect. IAS 2 uses normal production capacity for overhead absorption — idle capacity costs go to P&L, not inventory.")

        st.markdown("---")
        st.markdown("**5. Which of the following costs should be EXCLUDED from the cost of inventory?**")
        q5 = st.radio("", [
            "Import duties on raw materials",
            "Direct labour in production",
            "Storage costs for finished goods awaiting sale",
            "Freight charges on raw material delivery"
        ], key="ias2q5")
        if st.button("Check Answer", key="ias2c5"):
            if q5 == "Storage costs for finished goods awaiting sale":
                st.success("✅ Correct! IAS 2 excludes storage costs (unless necessary in the production process), abnormal waste, selling costs and administrative overheads from inventory cost.")
            else:
                st.error("❌ Incorrect. Storage costs for finished goods awaiting sale are EXCLUDED from inventory cost under IAS 2.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Measurement Principle
        **Inventories = Lower of Cost and NRV**

        ### 2. Cost of Inventory Includes:
        | Include | Exclude |
        |---------|---------|
        | Purchase price (net of discounts) | Abnormal waste |
        | Import duties and transport | Idle capacity overheads |
        | Direct labour | Selling and admin costs |
        | Absorbed production overheads (normal capacity) | Storage costs (unless production-related) |

        ### 3. Cost Formulas Allowed Under IAS 2
        - ✅ FIFO
        - ✅ Weighted Average Cost (WAC)
        - ✅ Specific Identification (for non-interchangeable items)
        - ❌ LIFO — **PROHIBITED**

        ### 4. NRV Formula
        ```
        NRV = Estimated Selling Price − Costs to Complete − Costs to Sell
        ```

        ### 5. Write-Down and Reversal
        - Write down when cost > NRV
        - Done on item-by-item basis (or similar groups)
        - Reversals are **mandatory** when NRV recovers
        - Reversal cannot exceed original write-down

        ### 6. Key IFRS vs US GAAP Difference
        | IAS 2 (IFRS) | US GAAP |
        |--------------|---------|
        | LIFO prohibited | LIFO permitted |
        | Reversals of write-downs required | Reversals NOT allowed |
        """)

        st.subheader("📌 Key Formulas")
        st.code("""
Inventory (Balance Sheet) = Lower of Cost and NRV
NRV = Estimated Selling Price − Costs to Complete − Costs to Sell
COGS = Opening Inventory + Purchases − Closing Inventory
WAC per unit = Total Cost Available ÷ Total Units Available
Fixed OH per unit = Total Fixed OH ÷ Normal Capacity (not actual)
        """)

        st.success("🎓 **IAS 2 Complete!** You can now measure inventory correctly, apply cost formulas, calculate NRV and account for write-downs and reversals.")
        st.info("💡 **Next**: IAS 7 — Statement of Cash Flows")

if __name__ == "__main__":
    show()