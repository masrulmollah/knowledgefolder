import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📊 IFRS 8: Operating Segments")
    st.markdown("*Master identification, measurement and disclosure of operating segments using the management approach*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Scope and the Management Approach")
        st.markdown("""
        **IFRS 8** applies to entities whose securities are publicly traded (or are in the process of issuing securities publicly).

        **Core principle — The Management Approach:** Segment information is reported on the SAME basis used **internally** by the **Chief Operating Decision Maker (CODM)** to evaluate performance and allocate resources.

        This differs from older approaches that defined segments based on external risk/reward criteria — IFRS 8 follows how management ACTUALLY runs the business.
        """)

        st.subheader("2. Definition of an Operating Segment")
        st.markdown("""
        A component of an entity:
        1. That engages in business activities from which it may earn revenues and incur expenses
        2. Whose operating results are **regularly reviewed by the CODM** to make decisions about resources and assess performance
        3. For which **discrete financial information** is available

        **CODM** is a function, not necessarily a specific individual — could be a CEO, a group of executives, or a management committee.
        """)

        st.subheader("3. Quantitative Thresholds — The 10% Tests")
        st.markdown("""
        A segment is **reportable** if it meets ANY ONE of these tests:

        | Test | Threshold |
        |---|---|
        | **Revenue Test** | Segment revenue (external + intersegment) ≥ 10% of total revenue of all segments |
        | **Profit/Loss Test** | Segment profit or loss ≥ 10% of the greater of: (a) total profit of all profitable segments, or (b) total loss of all loss-making segments |
        | **Assets Test** | Segment assets ≥ 10% of total assets of all segments |

        **75% Reporting Sufficiency Test:** If reportable segments' combined external revenue is less than 75% of total entity revenue, identify ADDITIONAL reportable segments until the 75% threshold is reached.

        **No upper limit** on number of segments, but if there are too many, consider combining segments with similar economic characteristics.
        """)

        st.subheader("4. Aggregation Criteria")
        st.markdown("""
        Two or more operating segments may be **aggregated** into a single reportable segment if:
        - Aggregation is **consistent with the core principle** of IFRS 8
        - The segments have **similar economic characteristics**, AND
        - They are similar in ALL of the following:
          - Nature of products/services
          - Nature of production processes
          - Type/class of customers
          - Distribution methods
          - Regulatory environment (if applicable)
        """)

        st.subheader("5. Required Disclosures for Each Reportable Segment")
        st.markdown("""
        - General information: factors used to identify segments, types of products/services
        - **Segment profit or loss** (as reported to CODM)
        - **Segment assets and liabilities** (if regularly provided to CODM)
        - Specific items: revenues from external customers, intersegment revenues, interest revenue/expense, depreciation/amortisation, material non-cash items, income tax expense, material items of income/expense

        **Reconciliations required:**
        - Total reportable segment revenue → entity's total revenue
        - Total reportable segment profit/loss → entity's profit/loss before tax
        - Total reportable segment assets → entity's total assets
        - Total reportable segment liabilities → entity's total liabilities (if disclosed)
        """)

        st.subheader("6. Entity-Wide Disclosures (Required Regardless of Segment Structure)")
        st.markdown("""
        Even entities with only ONE reportable segment must disclose:
        - **Information about products and services** — revenue from each major product/service
        - **Geographical information** — revenue and non-current assets split between domestic and foreign, with material individual countries disclosed separately
        - **Major customer information** — if revenue from a single external customer ≥ 10% of total entity revenue, disclose this fact and the segment(s) reporting the revenue (customer identity not required)
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Applying the 10% Revenue Test")
        revenue_data = pd.DataFrame({
            "Segment": ["Electronics", "Appliances", "Furniture", "Automotive Parts", "Total"],
            "External Revenue ($M)": [450, 280, 90, 80, 900],
            "Intersegment Revenue ($M)": [20, 0, 10, 0, 30],
            "Total Segment Revenue ($M)": [470, 280, 100, 80, 930],
            "% of Total Revenue": ["50.5%", "30.1%", "10.8%", "8.6%", "100%"],
            "Passes 10% Test?": ["✅ Yes", "✅ Yes", "✅ Yes", "❌ No", ""]
        })
        st.dataframe(revenue_data, use_container_width=True, hide_index=True)
        st.markdown("""
        **Automotive Parts** fails the revenue test (8.6% < 10%). Check if it passes the profit or assets test instead.
        If it fails ALL THREE tests, it may still be separately reported if management believes it would be useful, or it gets combined with another segment / reported as "Other".
        """)

        st.subheader("Example 2: Applying the Profit/Loss Test")
        st.markdown("""
        | Segment | Profit/(Loss) ($M) |
        |---|---|
        | Electronics | 80 |
        | Appliances | 45 |
        | Furniture | (15) |
        | Automotive Parts | 8 |

        - Total profit of profitable segments = 80 + 45 + 8 = **133**
        - Total loss of loss-making segments = **15**
        - Greater of the two = **133**
        - 10% threshold = **13.3**

        **Automotive Parts profit of $8M < $13.3M → FAILS profit test too.**

        If it also fails the assets test, and overall doesn't meet 75% sufficiency requirements with other segments, it may be combined into "All Other Segments."
        """)

        st.subheader("Example 3: 75% Reporting Sufficiency Test")
        st.markdown("""
        Total entity external revenue = $900M
        75% threshold = $675M

        Combined external revenue of reportable segments (Electronics + Appliances + Furniture):
        $450M + $280M + $90M = **$820M**

        $820M / $900M = **91.1%** — **EXCEEDS 75%** ✅

        No additional segments need to be separately identified. Automotive Parts can be combined into "All Other Segments" in the reconciliation.
        """)

        st.subheader("Example 4: Reconciliation Disclosure")
        st.markdown("""
        **Segment Profit Reconciliation to Entity Profit Before Tax:**

        | | $M |
        |---|---|
        | Total profit of reportable segments | 133 |
        | Loss of "All Other Segments" (Furniture, Auto Parts combined) | (7) |
        | Unallocated corporate expenses | (25) |
        | Elimination of intersegment profits | (3) |
        | **Entity profit before tax** | **98** |
        """)

        st.subheader("Example 5: Major Customer Disclosure")
        st.markdown("""
        Entity's largest customer, a global retail chain, generates $95M of revenue out of total entity revenue of $900M.

        $95M / $900M = **10.6%** ≥ 10% threshold → **disclosure required**

        Note: *"Revenues from one customer of the Electronics segment represented approximately 10.6% of the Group's total revenues."*
        (Customer name not required to be disclosed — just the fact and which segment(s) report the revenue.)
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Reportable Segment Identifier")
        st.markdown("Enter segment data to test against IFRS 8's quantitative thresholds:")

        n_segments = st.number_input("Number of segments", value=4, min_value=2, max_value=10)
        segment_data = []
        for i in range(int(n_segments)):
            st.markdown(f"**Segment {i+1}:**")
            c1, c2, c3, c4 = st.columns(4)
            name = c1.text_input(f"Name", value=f"Segment {i+1}", key=f"seg_name_{i}")
            rev = c2.number_input(f"Revenue ($M)", value=100.0, key=f"seg_rev_{i}")
            profit = c3.number_input(f"Profit/(Loss) ($M)", value=10.0, key=f"seg_prof_{i}")
            assets = c4.number_input(f"Assets ($M)", value=200.0, key=f"seg_assets_{i}")
            segment_data.append({"name": name, "revenue": rev, "profit": profit, "assets": assets})

        if st.button("Run 10% Tests"):
            total_rev = sum([s["revenue"] for s in segment_data])
            profitable_total = sum([s["profit"] for s in segment_data if s["profit"] > 0])
            loss_total = abs(sum([s["profit"] for s in segment_data if s["profit"] < 0]))
            profit_threshold_base = max(profitable_total, loss_total)
            total_assets = sum([s["assets"] for s in segment_data])

            results = []
            for s in segment_data:
                rev_pct = s["revenue"] / total_rev * 100 if total_rev else 0
                profit_pct = abs(s["profit"]) / profit_threshold_base * 100 if profit_threshold_base else 0
                assets_pct = s["assets"] / total_assets * 100 if total_assets else 0
                passes = rev_pct >= 10 or profit_pct >= 10 or assets_pct >= 10
                results.append({
                    "Segment": s["name"],
                    "Revenue %": f"{rev_pct:.1f}%",
                    "Profit/Loss %": f"{profit_pct:.1f}%",
                    "Assets %": f"{assets_pct:.1f}%",
                    "Reportable?": "✅ YES" if passes else "❌ NO"
                })
            st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)

            reportable_rev = sum([s["revenue"] for s in segment_data if (s["revenue"]/total_rev*100 >= 10 or abs(s["profit"])/profit_threshold_base*100 >= 10 or s["assets"]/total_assets*100 >= 10)])
            sufficiency = reportable_rev / total_rev * 100 if total_rev else 0
            st.markdown(f"**75% Sufficiency Test:** Reportable segments cover {sufficiency:.1f}% of total revenue")
            if sufficiency >= 75:
                st.success("✅ Passes 75% sufficiency test — no additional segments required")
            else:
                st.warning("⚠️ Below 75% — must identify additional reportable segments")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Major Customer Threshold Checker")
        total_entity_revenue = st.number_input("Total Entity Revenue ($M)", value=900.0, key="mc_total")
        customer_revenue = st.number_input("Revenue from Single Customer ($M)", value=95.0, key="mc_cust")
        if st.button("Check Major Customer Disclosure"):
            pct = customer_revenue / total_entity_revenue * 100
            if pct >= 10:
                st.warning(f"📢 **DISCLOSURE REQUIRED** — Customer represents {pct:.1f}% of total revenue (≥10% threshold)")
            else:
                st.success(f"✅ No disclosure required — Customer represents {pct:.1f}% of total revenue (<10% threshold)")

    with tab4:
        st.header("Visualizations")

        st.subheader("Segment Revenue Contribution")
        segs = ["Electronics", "Appliances", "Furniture", "Automotive Parts"]
        rev_vals = [470, 280, 100, 80]
        fig = go.Figure(go.Bar(x=segs, y=rev_vals, marker_color=["#2563EB","#10B981","#F59E0B","#94A3B8"]))
        fig.add_hline(y=93, line_dash="dash", line_color="#F87171", annotation_text="10% Threshold (93M)")
        fig.update_layout(title="Segment Revenue vs 10% Reportability Threshold", yaxis_title="Revenue ($M)", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("75% Sufficiency Test Visualization")
        fig2 = go.Figure(go.Pie(labels=["Reportable Segments (Electronics+Appliances+Furniture)", "Other/Unallocated"],
                                values=[820, 80], hole=0.5, marker_colors=["#34D399","#F87171"]))
        fig2.update_layout(title="75% Reporting Sufficiency — Coverage of Total Revenue", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IFRS 8, operating segments are identified based on:**")
        q1 = st.radio("", [
            "External risk and reward characteristics determined by auditors",
            "Geographic regions only",
            "The management approach — how the CODM internally reviews the business",
            "Legal entity structure"
        ], key="ifrs8q1")
        if st.button("Check Answer", key="ifrs8c1"):
            if q1 == "The management approach — how the CODM internally reviews the business":
                st.success("✅ Correct! IFRS 8 uses the MANAGEMENT APPROACH — segments are based on how the Chief Operating Decision Maker actually reviews performance and allocates resources internally.")
            else:
                st.error("❌ IFRS 8 = MANAGEMENT APPROACH, following internal reporting to the CODM, not external risk/reward analysis or legal structure.")

        st.markdown("---")
        st.markdown("**2. A segment is reportable if it meets the 10% threshold on:**")
        q2 = st.radio("", [
            "Revenue only",
            "Profit only",
            "Assets only",
            "ANY ONE of: revenue, profit/loss, or assets"
        ], key="ifrs8q2")
        if st.button("Check Answer", key="ifrs8c2"):
            if q2 == "ANY ONE of: revenue, profit/loss, or assets":
                st.success("✅ Correct! A segment is reportable if it meets ANY ONE of the three 10% tests (revenue, profit/loss, or assets) — not all three.")
            else:
                st.error("❌ Only ONE of the three tests (revenue, profit/loss, assets) needs to be met for a segment to be reportable.")

        st.markdown("---")
        st.markdown("**3. The 75% sufficiency test requires that:**")
        q3 = st.radio("", [
            "75% of segments must be profitable",
            "Reportable segments' combined external revenue must be at least 75% of total entity revenue",
            "75% of assets must be in reportable segments",
            "No more than 75% of revenue can come from one segment"
        ], key="ifrs8q3")
        if st.button("Check Answer", key="ifrs8c3"):
            if q3 == "Reportable segments' combined external revenue must be at least 75% of total entity revenue":
                st.success("✅ Correct! If reportable segments don't collectively cover at least 75% of total external revenue, additional segments must be identified until the threshold is met.")
            else:
                st.error("❌ The 75% test checks whether REPORTABLE SEGMENTS' combined external revenue reaches 75% of TOTAL entity revenue.")

        st.markdown("---")
        st.markdown("**4. Major customer disclosure is required when:**")
        q4 = st.radio("", [
            "Any customer purchases more than $1 million",
            "Revenue from a single external customer is ≥10% of total entity revenue",
            "The customer is a related party",
            "The customer is located overseas"
        ], key="ifrs8q4")
        if st.button("Check Answer", key="ifrs8c4"):
            if q4 == "Revenue from a single external customer is ≥10% of total entity revenue":
                st.success("✅ Correct! IFRS 8 requires disclosure when a single external customer contributes ≥10% of total entity revenue — disclose the fact and which segment(s), but not the customer's name.")
            else:
                st.error("❌ Major customer threshold = ≥10% of TOTAL ENTITY revenue from a SINGLE external customer.")

        st.markdown("---")
        st.markdown("**5. Two operating segments may be aggregated if they have similar economic characteristics AND are similar in:**")
        q5 = st.radio("", [
            "Only their geographic location",
            "Nature of products/services, production processes, customer type, distribution methods, and regulatory environment",
            "Only their reporting currency",
            "Only the size of their workforce"
        ], key="ifrs8q5")
        if st.button("Check Answer", key="ifrs8c5"):
            if q5 == "Nature of products/services, production processes, customer type, distribution methods, and regulatory environment":
                st.success("✅ Correct! Aggregation requires similar economic characteristics PLUS similarity in ALL FIVE qualitative factors: products/services, production process, customer type, distribution method, and regulatory environment.")
            else:
                st.error("❌ Aggregation requires similarity across all FIVE qualitative criteria, not just one factor like geography or currency.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Core Principle — Management Approach
        Segments follow how the **CODM** internally reviews the business — NOT external definitions.

        ### 2. Reportable Segment — 10% Tests (meet ANY ONE)
        | Test | Threshold |
        |---|---|
        | Revenue | ≥10% of total segment revenue |
        | Profit/Loss | ≥10% of greater of (total profits) or (total losses) |
        | Assets | ≥10% of total segment assets |

        ### 3. 75% Sufficiency Test
        ```
        Reportable Segments' External Revenue ÷ Total Entity Revenue ≥ 75%
        If not met → identify MORE reportable segments
        ```

        ### 4. Aggregation Criteria (ALL must be similar)
        - Similar economic characteristics
        - Products/services, production process, customer type, distribution method, regulatory environment

        ### 5. Required Disclosures
        - Segment profit/loss, assets, liabilities (as reported to CODM)
        - Reconciliations to entity totals
        - Entity-wide: products/services, geography, major customers (≥10%)
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Management Approach = follow internal CODM reporting (not external definitions)
10% Test: Revenue OR Profit/Loss OR Assets (any ONE triggers reportability)
75% Sufficiency: Reportable Segments' Revenue / Total Revenue ≥ 75%
Major Customer: ≥10% of total entity revenue from one customer → disclose
Aggregation: similar economics + similar in ALL 5 qualitative factors
        """)

        st.success("🎓 **IFRS 8 Complete!** You can now identify reportable segments, apply quantitative thresholds, and prepare required segment disclosures.")
        st.info("💡 **Next**: IFRS 9 — Financial Instruments")

if __name__ == "__main__":
    show()