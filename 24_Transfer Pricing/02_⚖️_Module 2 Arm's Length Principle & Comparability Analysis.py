import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def show():
    st.title("⚖️ Module 2: Arm's Length Principle & Comparability Analysis")
    st.markdown("*Based on Section 177–179, ITA 2023 & Income Tax Rules 2023 (Rules 68–72)*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Law", "🧮 Examples", "💡 Interactive Exercise",
        "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────────────────────
    with tab1:
        st.header("Theory & Legal Concepts")

        st.subheader("1. The Arm's Length Principle (ALP)")
        st.markdown("""
        The **Arm's Length Principle** is the cornerstone of international transfer pricing.

        > *"The income arising from an international transaction shall be computed having regard to the arm's length price."*  
        > — **Section 177, ITA 2023**

        **Definition of Arm's Length Price (ALP):**  
        The price that would be charged in a transaction **between unrelated independent parties** under 
        **similar circumstances** in the **open market**.

        #### Why is ALP necessary?
        - Independent parties negotiate prices based on **market forces**
        - Related parties may set prices to **minimise group tax**
        - ALP ensures each entity in a group is taxed on its **genuine economic contribution**
        """)

        st.subheader("2. Comparability Analysis — The Foundation of ALP")
        st.markdown("""
        To determine whether a controlled transaction meets the ALP, a **comparability analysis** is required.
        
        **Rule 69, Income Tax Rules 2023** specifies five comparability factors:

        | # | Factor | Description |
        |---|--------|-------------|
        | 1 | **Characteristics of property/services** | Physical features, quality, type, volume |
        | 2 | **Functional analysis** | Functions performed, assets used, risks assumed |
        | 3 | **Contractual terms** | Payment terms, warranties, distribution rights |
        | 4 | **Economic circumstances** | Geographic market, competition, regulations |
        | 5 | **Business strategies** | Market penetration, product lifecycle, R&D |

        > ⚠️ *No two transactions are perfectly comparable. Adjustments must be made for material differences.*
        """)

        st.subheader("3. Functional Analysis (FAR Analysis)")
        st.markdown("""
        The most critical comparability factor is the **FAR Analysis**:

        #### Functions
        - Manufacturing, distribution, marketing, R&D, procurement
        - **More functions = more reward** expected

        #### Assets
        - Tangible assets: plant, machinery, inventory
        - Intangible assets: patents, trademarks, customer lists
        - **Use of valuable intangibles = higher expected return**

        #### Risks
        - Market risk, credit risk, inventory risk, currency risk, R&D risk
        - **Higher risk assumed = higher expected return**

        > 💡 *In practice, the entity that performs more functions, uses more assets and bears more risks 
        > should earn a higher return. An entity performing only routine functions earns a routine (lower) return.*
        """)

        st.subheader("4. Types of Comparables")
        st.markdown("""
        #### Internal Comparables
        Transactions by the **tested party itself** with unrelated parties under similar conditions.
        - *Example: A Bangladeshi company sells product X to its parent at BDT 100. It sells the 
          same product X to an unrelated customer at BDT 95. The BDT 95 is the internal comparable.*

        #### External Comparables
        Transactions between **two independent third parties** in the open market.
        - Found in commercial databases (e.g., Orbis, Prowess, TP Catalyst)
        - NBR may use public data and industry benchmarks

        #### Preference under ITA 2023
        **Internal comparables are preferred** over external comparables when available, as they 
        reflect the most similar conditions.
        """)

        st.subheader("5. Comparability Adjustments")
        st.markdown("""
        When a comparable is identified but differences exist, **adjustments** must be made to 
        eliminate the effect of those differences.

        **Common adjustments:**
        - Working capital adjustments (accounts receivable, payable, inventory)
        - Accounting adjustments (depreciation methods, capitalisation)
        - Geographic market adjustments
        - Volume/quantity adjustments
        - Risk adjustments

        > *Under Rule 70, ITA Rules 2023: Adjustments must be made only where they have a **material** 
        > effect on price or margin, and are capable of being made with **reasonable accuracy**.*
        """)

        st.subheader("6. Arm's Length Range")
        st.markdown("""
        Because comparability is never perfect, ITA 2023 allows for an **Arm's Length Range (ALR)**:

        - A range of prices/margins derived from multiple comparables
        - If the tested party's result falls **within the range** → no adjustment
        - If outside the range → price is adjusted to the **median** of the range

        **Statistical Method:**  
        The **interquartile range (IQR)** — from the **25th to 75th percentile** — is commonly used 
        as the arm's length range, consistent with OECD guidance and NBR practice.
        """)

    # ─────────────────────────────────────────────
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Internal vs External Comparable")
        st.markdown("""
        **Scenario:**  
        Grameen Tech Ltd. (Bangladesh) licenses software to its Dutch parent for USD 50,000/year.
        Grameen Tech also licenses similar software to Unilever Bangladesh (unrelated) for USD 80,000/year.

        **Analysis:**
        | Type | Transaction | Price |
        |------|-------------|-------|
        | Controlled | License to Dutch parent | USD 50,000 |
        | Internal Comparable | License to Unilever Bangladesh | USD 80,000 |

        The internal comparable price is **USD 80,000**.  
        The controlled transaction at **USD 50,000** is **below** the ALP.  
        → **Adjustment required:** NBR can increase taxable income by USD 30,000.
        """)

        st.subheader("Example 2: FAR Analysis in Practice")
        st.markdown("""
        **Scenario:**  
        Prime Garments Ltd. (Bangladesh) manufactures garments and sells to Prime Fashion GmbH (Germany, parent).

        **FAR Analysis:**

        | Factor | Prime Garments (Bangladesh) | Prime Fashion (Germany) |
        |--------|-----------------------------|------------------------|
        | **Functions** | Manufacturing, QC, procurement | Marketing, sales, distribution, brand |
        | **Assets** | Factory, machinery, labour | Brand, customer base, retail network |
        | **Risks** | Production risk, labour risk | Market risk, currency risk, inventory risk |

        **Conclusion:**  
        - Prime Garments performs **contract manufacturing** (limited functions, limited risk)
        - Appropriate return: **Routine/limited return** on cost plus basis
        - Prime Fashion owns the brand and bears market risk → earns higher margins

        ✅ This FAR analysis supports using the **Cost Plus Method** for Prime Garments.
        """)

        st.subheader("Example 3: Arm's Length Range")
        st.markdown("""
        **Scenario:**  
        An NBR audit identifies 6 comparable companies with the following gross margins:

        | Comparable | Gross Margin % |
        |------------|---------------|
        | Co. A | 12% |
        | Co. B | 15% |
        | Co. C | 18% |
        | Co. D | 20% |
        | Co. E | 22% |
        | Co. F | 28% |

        **IQR Calculation:**
        - 25th percentile (Q1): ~15%
        - Median (Q2): 19%
        - 75th percentile (Q3): ~22%
        - **Arm's Length Range: 15% – 22%**

        If the tested party's gross margin is **13%** → **outside the range** → adjustment to median **19%**.  
        If the tested party's gross margin is **17%** → **within the range** → **no adjustment**.
        """)

    # ─────────────────────────────────────────────
    with tab3:
        st.header("Interactive Exercise")

        st.subheader("📊 Arm's Length Range Calculator")
        st.markdown("Enter up to 8 comparable margins (%) to determine the arm's length range:")

        cols = st.columns(4)
        comparables = []
        for i in range(8):
            val = cols[i % 4].number_input(f"Comp {i+1} (%)", min_value=0.0, max_value=100.0,
                                            value=0.0, step=0.5, key=f"comp_{i}")
            if val > 0:
                comparables.append(val)

        tested_margin = st.number_input("Tested party's margin (%)", min_value=0.0, max_value=100.0,
                                         value=15.0, step=0.5)

        if st.button("Calculate Arm's Length Range") and len(comparables) >= 3:
            arr = np.array(comparables)
            q1 = np.percentile(arr, 25)
            median = np.percentile(arr, 50)
            q3 = np.percentile(arr, 75)

            col1, col2, col3 = st.columns(3)
            col1.metric("Q1 (25th percentile)", f"{q1:.1f}%")
            col2.metric("Median", f"{median:.1f}%")
            col3.metric("Q3 (75th percentile)", f"{q3:.1f}%")

            st.markdown(f"**Arm's Length Range: {q1:.1f}% – {q3:.1f}%**")

            if q1 <= tested_margin <= q3:
                st.success(f"✅ Tested party margin ({tested_margin}%) is **WITHIN** the arm's length range. No adjustment required.")
            elif tested_margin < q1:
                st.error(f"❌ Tested party margin ({tested_margin}%) is **BELOW** the arm's length range. Adjustment to median {median:.1f}% required.")
            else:
                st.warning(f"⚠️ Tested party margin ({tested_margin}%) is **ABOVE** the arm's length range. Review required.")

            fig = go.Figure()
            fig.add_trace(go.Box(y=arr, name="Comparables", boxmean=True,
                                  marker_color='steelblue'))
            fig.add_hline(y=tested_margin, line_dash="dash", line_color="red",
                          annotation_text=f"Tested Party: {tested_margin}%")
            fig.update_layout(title="Comparable Margins Distribution",
                               yaxis_title="Margin (%)", height=400)
            st.plotly_chart(fig, use_container_width=True)

        elif st.button("Calculate Arm's Length Range") and len(comparables) < 3:
            st.warning("Please enter at least 3 comparable margins.")

        st.markdown("---")
        st.subheader("🔍 FAR Analysis Tool")
        st.markdown("Assess the functional profile of your entity:")

        functions = st.multiselect("Functions performed by the entity:",
            ["Manufacturing", "Distribution", "Marketing", "R&D", "Procurement",
             "Management services", "Financing", "Quality control"])
        assets = st.multiselect("Assets used:",
            ["Factory/plant", "Machinery", "Inventory", "Patents", "Trademarks",
             "Customer relationships", "Know-how", "Financial assets"])
        risks = st.multiselect("Risks assumed:",
            ["Market risk", "Inventory risk", "Credit risk", "Currency risk",
             "R&D risk", "Product liability", "Regulatory risk"])

        if st.button("Assess Functional Profile"):
            f_score = len(functions)
            a_score = len([a for a in assets if a in ["Patents", "Trademarks", "Know-how", "Customer relationships"]])
            r_score = len(risks)
            total = f_score + a_score + r_score

            if total <= 3:
                profile = "🟢 **Routine / Limited Risk Entity** — Expected return: Low (cost-plus or TNMM)"
            elif total <= 7:
                profile = "🟡 **Medium Functionality Entity** — Expected return: Moderate"
            else:
                profile = "🔴 **Full-Fledged / Entrepreneurial Entity** — Expected return: High (residual profit)"

            st.info(profile)
            st.markdown(f"- Functions: {f_score} | Key Assets: {a_score} | Risks: {r_score}")

    # ─────────────────────────────────────────────
    with tab4:
        st.header("Quiz")

        st.markdown("**1. Under Rule 69 of the Income Tax Rules 2023, how many comparability factors must be considered?**")
        q1 = st.radio("Select:", ["3", "4", "5", "6"], key="m2q1")
        if st.button("Check", key="m2c1"):
            if q1 == "5":
                st.success("✅ Correct! Rule 69 specifies 5 comparability factors: characteristics, functions, contractual terms, economic circumstances, business strategies.")
            else:
                st.error("❌ Incorrect. Rule 69 specifies 5 comparability factors.")

        st.markdown("---")
        st.markdown("**2. In FAR Analysis, 'FAR' stands for:**")
        q2 = st.radio("Select:", [
            "Finance, Assets, Revenue",
            "Functions, Assets, Risks",
            "Factors, Assumptions, Returns",
            "Fees, Allocation, Royalties"
        ], key="m2q2")
        if st.button("Check", key="m2c2"):
            if q2 == "Functions, Assets, Risks":
                st.success("✅ Correct! FAR = Functions performed, Assets used, Risks assumed.")
            else:
                st.error("❌ Incorrect. FAR stands for Functions, Assets, Risks.")

        st.markdown("---")
        st.markdown("**3. When a tested party's result falls OUTSIDE the arm's length range, it is adjusted to:**")
        q3 = st.radio("Select:", ["Q1 (25th percentile)", "Q3 (75th percentile)", "The median", "The maximum"], key="m2q3")
        if st.button("Check", key="m2c3"):
            if q3 == "The median":
                st.success("✅ Correct! Under ITA 2023, if outside the ALR, adjustment is made to the median of the range.")
            else:
                st.error("❌ Incorrect. The adjustment is made to the median of the arm's length range.")

        st.markdown("---")
        st.markdown("**4. Internal comparables are preferred over external comparables because:**")
        q4 = st.radio("Select:", [
            "They are easier to find",
            "They reflect the most similar conditions to the controlled transaction",
            "NBR requires internal comparables by law",
            "External databases are too expensive"
        ], key="m2q4")
        if st.button("Check", key="m2c4"):
            if q4 == "They reflect the most similar conditions to the controlled transaction":
                st.success("✅ Correct! Internal comparables are preferred as they most closely mirror the conditions of the controlled transaction.")
            else:
                st.error("❌ Incorrect. Internal comparables are preferred as they reflect the most similar conditions.")

        st.markdown("---")
        st.markdown("**5. An entity that performs only routine functions, uses limited assets and bears minimal risk should expect:**")
        q5 = st.radio("Select:", [
            "A high entrepreneurial return",
            "A routine / limited return",
            "Residual profits",
            "No taxable income"
        ], key="m2q5")
        if st.button("Check", key="m2c5"):
            if q5 == "A routine / limited return":
                st.success("✅ Correct! Limited function/risk entities earn routine returns; entrepreneurial entities earn residual profits.")
            else:
                st.error("❌ Incorrect. Routine/limited risk entities earn a routine (low) return.")

    # ─────────────────────────────────────────────
    with tab5:
        st.header("Module Summary")

        st.markdown("""
        ### 🎯 Key Takeaways

        | Concept | Key Point |
        |---------|-----------|
        | Arm's Length Principle | Section 177 ITA 2023 — price as between independent parties |
        | Comparability Factors | Rule 69: 5 factors — characteristics, FAR, contractual, economic, strategy |
        | FAR Analysis | Functions, Assets, Risks — determines appropriate return level |
        | Internal Comparables | Preferred — same entity's deals with unrelated parties |
        | External Comparables | Third-party databases (Orbis, Prowess, TP Catalyst) |
        | Adjustments | Made for material differences with reasonable accuracy |
        | Arm's Length Range | IQR (Q1–Q3); adjustment to median if outside range |

        ### 📐 Comparability Analysis Process
        ```
        Step 1: Identify the controlled transaction (type, value, parties)
        Step 2: Perform FAR analysis of tested party
        Step 3: Search for internal comparables
        Step 4: Search external databases if no internal comparables
        Step 5: Make comparability adjustments for material differences
        Step 6: Determine arm's length range (IQR)
        Step 7: Compare tested party result to ALR
        Step 8: Adjust to median if outside range
        ```

        ### 🏭 FAR Profile → Expected Return
        | FAR Profile | Entity Type | Expected Return |
        |-------------|-------------|-----------------|
        | Few functions, limited assets, low risk | Contract manufacturer / distributor | Cost plus low markup (3–10%) |
        | Moderate functions, some assets, moderate risk | Limited risk entity | TNMM — moderate NCP margin |
        | Full functions, owns intangibles, bears major risks | Entrepreneurial entity | Residual / high profit share |
        """)

        st.success("🎓 **Module 2 Complete!** You can now perform comparability analysis and apply the arm's length standard.")
        st.info("💡 **Next**: Proceed to Module 3 — Transfer Pricing Methods under ITA 2023.")

if __name__ == "__main__":
    show()