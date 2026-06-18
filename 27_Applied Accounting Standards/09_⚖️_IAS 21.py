import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show():
    st.title("💱 IAS 21: The Effects of Changes in Foreign Exchange Rates")
    st.markdown("*Master functional currency, translation of transactions, and foreign operation consolidation*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Key Definitions")
        st.markdown("""
| Term | Definition |
|---|---|
| **Functional Currency** | Currency of the primary economic environment in which the entity operates |
| **Presentation Currency** | Currency in which financial statements are presented (may differ from functional) |
| **Foreign Currency** | Any currency other than the functional currency |
| **Spot Rate** | Exchange rate at the date of the transaction |
| **Closing Rate** | Spot rate at balance sheet date |
        """)
        st.subheader("2. Determining Functional Currency")
        st.markdown("""
**Primary indicators (most important):**
- Currency in which sales prices are denominated and settled
- Currency of the country whose competitive forces mainly determine prices

**Secondary indicators:**
- Currency in which labour, materials and costs are denominated
- Currency in which finance is raised
- Currency in which receipts from operating activities are retained
        """)
        st.subheader("3. Translating Foreign Currency Transactions")
        st.markdown("""
**Initial recognition:** Translate at the **spot rate** on the transaction date (or average rate for practical purposes).

**At each balance sheet date:**
| Item | Exchange Rate Used |
|---|---|
| **Monetary items** (cash, receivables, payables, loans) | **Closing rate** |
| **Non-monetary items at historical cost** (PPE at cost, inventories) | **Historical rate** (rate at transaction date) |
| **Non-monetary items at fair value** (PPE revalued, equity investments at FV) | **Rate when fair value was determined** |

**Exchange differences on monetary items:** Recognised in **P&L** in the period they arise.
        """)
        st.subheader("4. Foreign Operations — Translation into Presentation Currency")
        st.markdown("""
When translating a **foreign subsidiary** into the parent's presentation currency:

| Item | Rate |
|---|---|
| Assets and liabilities | **Closing rate** |
| Income and expenses | **Rate at date of transactions** (or average rate for period) |
| Equity items (share capital, retained earnings) | **Historical rates** |
| Exchange differences | **OCI — Translation Reserve** (recyclable when operation is disposed) |

This is the **closing rate / net investment method**.
        """)
        st.subheader("5. Disposal of Foreign Operation")
        st.markdown("""
On disposal of a foreign operation:
- The cumulative exchange difference in OCI (translation reserve) is **reclassified to P&L** (recycled)
- This is one of the key **recyclable OCI** items under IFRS
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Foreign Currency Transaction — Trade Receivable")
        st.markdown("""
**Entity functional currency: SGD. Customer invoice in USD.**

| Date | Event | USD | Rate | SGD |
|---|---|---|---|---|
| 1 Nov | Sale recognised | $100,000 | 1.35 | SGD 135,000 |
| 31 Dec | Year-end closing rate | $100,000 | 1.38 | SGD 138,000 |
| 15 Jan | Cash received | $100,000 | 1.36 | SGD 136,000 |

**Year-end:** Retranslate receivable → SGD 138,000. Exchange gain = SGD 3,000 → P&L.
**On collection:** Cash at 1.36 = SGD 136,000. Exchange loss = SGD 2,000 → P&L.
        """)
        st.subheader("Example 2: Historical Rate for Non-Monetary Asset")
        st.markdown("""
**Entity buys machinery in USD for $200,000 when rate = 1.30 SGD/USD**
- Initial recognition: $200,000 × 1.30 = **SGD 260,000**
- At year-end (rate 1.38): **Still SGD 260,000** — historical rate applies
- No exchange difference on non-monetary items carried at historical cost
        """)
        st.subheader("Example 3: Foreign Subsidiary Translation")
        data = pd.DataFrame({
            "Item": ["Machinery (non-current asset)","Trade receivables","Cash","Share capital","Retained earnings","Revenue","Expenses"],
            "GBP (functional)": ["£500,000","£80,000","£40,000","£(200,000)","£(320,000)","£1,200,000","£(900,000)"],
            "Rate": ["1.75 (historical)","1.80 (closing)","1.80 (closing)","1.60 (historical)","Various historical","1.72 (average)","1.72 (average)"],
            "SGD (presentation)": ["875,000","144,000","72,000","(320,000)","Various","2,064,000","(1,548,000)"]
        })
        st.dataframe(data, use_container_width=True, hide_index=True)
        st.caption("Translation differences arise from using different rates → OCI Translation Reserve")

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Tool 1: FX Transaction Gain/Loss Calculator")
        col1, col2 = st.columns(2)
        with col1:
            item = st.selectbox("Item type:", ["Trade Receivable (asset)","Trade Payable (liability)","Loan payable (liability)","Cash in foreign currency"])
            fc_amount = st.number_input("Foreign Currency Amount", value=100000.0)
            initial_rate = st.number_input("Rate at Transaction Date (FC → Functional)", value=1.35)
            closing_rate = st.number_input("Closing Rate at Year-End", value=1.38)
        with col2:
            initial_fc = fc_amount * initial_rate
            closing_fc = fc_amount * closing_rate
            diff = closing_fc - initial_fc
            is_asset = "Receivable" in item or "Cash" in item
            if is_asset:
                gain_loss = diff
                label = "Gain" if gain_loss >= 0 else "Loss"
            else:
                gain_loss = -diff
                label = "Gain" if gain_loss >= 0 else "Loss"
            st.markdown(f"""
| | Amount (Functional Currency) |
|---|---|
| Initial recognition | {initial_fc:,.2f} |
| Year-end carrying amount | {closing_fc:,.2f} |
| Exchange {label} | {abs(gain_loss):,.2f} |
| Recognised in | **P&L** |
""")
            if gain_loss >= 0:
                st.success(f"Exchange GAIN of {abs(gain_loss):,.2f} → P&L income")
            else:
                st.error(f"Exchange LOSS of {abs(gain_loss):,.2f} → P&L expense")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Monetary vs Non-Monetary Item Classifier")
        item2 = st.selectbox("Select item:", ["Trade receivable","PPE at historical cost","Inventory at cost","Cash and bank","Prepaid expenses","Loans payable","Equity investments at FV","Deferred revenue"], key="mnclass")
        monetary = {"Trade receivable": True, "Cash and bank": True, "Loans payable": True}
        non_monetary = {"PPE at historical cost": "Historical rate", "Inventory at cost": "Historical rate", "Prepaid expenses": "Historical rate", "Equity investments at FV": "Rate when FV determined", "Deferred revenue": "Historical rate"}
        if item2 in monetary:
            st.success("✅ **MONETARY** — retranslate at CLOSING RATE at each balance sheet date. Exchange differences → P&L.")
        else:
            st.info(f"📌 **NON-MONETARY** — translate at {non_monetary.get(item2, 'historical rate')}. No retranslation at year-end.")

    with tab4:
        st.header("Visualizations")
        rates = [1.30, 1.32, 1.35, 1.38, 1.40, 1.36]
        dates = ["Jan","Mar","May","Jul(sale)","Dec(year-end)","Feb(collect)"]
        receivable_sgd = [0,0,0,100000*1.35,100000*1.40,100000*1.36]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=rates, name="USD/SGD Rate", line=dict(color="#2563EB",width=2), mode="lines+markers"))
        fig.add_trace(go.Bar(x=dates, y=receivable_sgd, name="Receivable SGD", yaxis="y2", marker_color="#10B981", opacity=0.5))
        fig.update_layout(title="FX Rate Movement and Receivable Balance", yaxis=dict(title="Rate"), yaxis2=dict(title="SGD Receivable", overlaying="y", side="right"), height=380)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. The functional currency is determined by:**")
        q1 = st.radio("", ["Management's preference","The currency in which the entity's shares are listed","The primary economic environment in which the entity operates","The currency of the country of incorporation"], key="ias21q1")
        if st.button("Check", key="c21_1"):
            if q1 == "The primary economic environment in which the entity operates":
                st.success("✅ Correct! Functional currency = currency of the primary economic environment. Key indicator: currency in which sales prices are denominated.")
            else:
                st.error("❌ Functional currency is determined by the primary economic environment — mainly where sales prices are denominated and settled.")
        st.markdown("---")
        st.markdown("**2. At year-end, a foreign currency trade payable is retranslated at:**")
        q2 = st.radio("", ["Historical rate (rate when payable arose)","Closing rate","Average rate for the period","Rate when payment is expected"], key="ias21q2")
        if st.button("Check", key="c21_2"):
            if q2 == "Closing rate":
                st.success("✅ Correct! Monetary items (including trade payables) are retranslated at the closing rate at each balance sheet date. Differences go to P&L.")
            else:
                st.error("❌ Monetary items (payables, receivables, cash) use the CLOSING RATE at year-end.")
        st.markdown("---")
        st.markdown("**3. PPE acquired for foreign currency and carried at historical cost is translated using:**")
        q3 = st.radio("", ["Closing rate at year-end","Average rate for the year","Historical rate at the date of acquisition","Fair value rate"], key="ias21q3")
        if st.button("Check", key="c21_3"):
            if q3 == "Historical rate at the date of acquisition":
                st.success("✅ Correct! Non-monetary assets at historical cost use the HISTORICAL RATE (rate at date of transaction). No retranslation at year-end.")
            else:
                st.error("❌ Non-monetary items at historical cost → historical rate. No retranslation at year-end.")
        st.markdown("---")
        st.markdown("**4. When translating a foreign subsidiary into the parent's presentation currency, assets and liabilities use:**")
        q4 = st.radio("", ["Average rate","Historical rates","Closing rate","Rate at date of acquisition"], key="ias21q4")
        if st.button("Check", key="c21_4"):
            if q4 == "Closing rate":
                st.success("✅ Correct! Under the closing rate/net investment method, all assets and liabilities of a foreign operation are translated at the closing rate.")
            else:
                st.error("❌ Assets and liabilities of foreign operations use the CLOSING RATE when translating into presentation currency.")
        st.markdown("---")
        st.markdown("**5. On disposal of a foreign operation, the cumulative translation reserve is:**")
        q5 = st.radio("", ["Kept in OCI permanently","Transferred to retained earnings directly","Reclassified from OCI to P&L (recycled)","Written off against goodwill"], key="ias21q5")
        if st.button("Check", key="c21_5"):
            if q5 == "Reclassified from OCI to P&L (recycled)":
                st.success("✅ Correct! The cumulative FX translation reserve in OCI is RECYCLED (reclassified) to P&L on disposal of the foreign operation. This is a key recyclable OCI item.")
            else:
                st.error("❌ Cumulative FX differences in OCI are RECYCLED to P&L on disposal of the foreign operation.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 21 Key Rules

**Functional Currency** = Primary economic environment (where sales prices are denominated)

**Foreign Currency Transactions:**
| Item | Rate at Year-End | Exchange Difference |
|---|---|---|
| Monetary items | Closing rate | P&L |
| Non-monetary at cost | Historical rate | None |
| Non-monetary at FV | Rate when FV determined | P&L or OCI (per other standard) |

**Foreign Subsidiary Translation:**
| Item | Rate |
|---|---|
| Assets & liabilities | Closing rate |
| P&L items | Average rate (approximate) |
| Share capital | Historical rate |
| Translation differences | OCI — Translation Reserve |

**Disposal of Foreign Operation:** Cumulative OCI translation reserve → recycled to P&L
        """)
        st.success("🎓 IAS 21 Complete!")
        st.info("💡 Next: IAS 23 — Borrowing Costs")

if __name__ == "__main__":
    show()