import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def show():
    st.title("🔢 Module 3: Transfer Pricing Methods under ITA 2023")
    st.markdown("*Based on Section 178–179, ITA 2023 & Rules 71–76, Income Tax Rules 2023*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Law", "🧮 Examples", "💡 Interactive Exercise",
        "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────────────────────
    with tab1:
        st.header("Theory & Legal Concepts")

        st.subheader("1. Overview of TP Methods")
        st.markdown("""
        **Section 178, ITA 2023** prescribes six approved methods to compute the **Arm's Length Price (ALP)**:

        | # | Method | Abbrev. | Best For |
        |---|--------|---------|----------|
        | 1 | Comparable Uncontrolled Price | **CUP** | Goods, commodities, loans |
        | 2 | Resale Price Method | **RPM** | Distribution transactions |
        | 3 | Cost Plus Method | **CPM** | Manufacturing, services |
        | 4 | Profit Split Method | **PSM** | Highly integrated transactions, intangibles |
        | 5 | Transactional Net Margin Method | **TNMM** | Wide applicability (most common) |
        | 6 | Any other method | **OTM** | As approved by NBR if none of above suitable |

        **Section 179, ITA 2023** — the **Most Appropriate Method (MAM)** rule:
        > The method that best suits the facts and circumstances of each transaction, based on comparability and 
        > availability of reliable data, shall be the most appropriate method.
        """)

        st.subheader("2. Method 1: Comparable Uncontrolled Price (CUP)")
        st.markdown("""
        **Principle:** Compares the **price** in a controlled transaction to the price in a comparable 
        uncontrolled transaction.

        ```
        ALP = Price in comparable uncontrolled transaction
              (adjusted for material differences)
        ```

        **Rule 71, IT Rules 2023:**
        - Most direct and reliable method when comparables are available
        - Internal CUP (same party, different customer) preferred over external CUP

        **Best suited for:**
        - Commodity transactions (jute, rice, cotton, crude oil)
        - Loans (compare interest rate to bank lending rate)
        - Software/IP licences with market benchmarks
        - Financial guarantees

        **Limitations:**
        - Requires very similar products and conditions
        - Difficult to find perfect comparables for unique products
        """)

        st.subheader("3. Method 2: Resale Price Method (RPM)")
        st.markdown("""
        **Principle:** Starts with the **resale price** to an unrelated party, deducts an appropriate 
        gross margin (resale margin), leaving the arm's length purchase price.

        ```
        ALP = Resale Price × (1 − Arm's Length Gross Margin %)
        ```

        **Or equivalently:**
        ```
        Gross Margin % = (Resale Price − Purchase Price) / Resale Price
        ```

        **Rule 72, IT Rules 2023:**
        - Functional analysis critical: distributor's functions and risks determine the arm's length gross margin
        - Simple distributors (low risk) → lower gross margin retained
        - Value-added distributors (high risk, brand building) → higher gross margin retained

        **Best suited for:**
        - Distribution and trading transactions
        - Where the reseller adds limited value before resale
        """)

        st.subheader("4. Method 3: Cost Plus Method (CPM)")
        st.markdown("""
        **Principle:** Starts with the **cost of production**, adds an appropriate mark-up on costs.

        ```
        ALP = Cost of Production × (1 + Arm's Length Mark-up %)
        ```

        **Or equivalently:**
        ```
        Gross Margin % = (Selling Price − Cost) / Cost
        ```

        **Rule 73, IT Rules 2023:**

        **Best suited for:**
        - Contract manufacturing (routine manufacturing with limited risk)
        - Intra-group services (IT services, shared services, management services)
        - Semi-finished goods transferred between group members

        **Important:** 'Cost' must be consistently defined across comparables 
        (include/exclude selling expenses, R&D, etc.)
        """)

        st.subheader("5. Method 4: Profit Split Method (PSM)")
        st.markdown("""
        **Principle:** The combined profit of associated enterprises is split between them based on 
        their relative **contributions** (functions, assets, risks).

        **Two approaches under Rule 74:**

        1. **Contribution Analysis:**  
           Combined profit split in proportion to each party's relative contribution (FAR analysis)

        2. **Residual Analysis:**
           ```
           Step 1: Allocate routine return to each party (using TNMM)
           Step 2: Residual profit split based on relative value of unique intangibles
           ```

        **Best suited for:**
        - Highly integrated transactions where one party cannot be a tested party
        - Transactions involving **unique and valuable intangibles** (patents, trade secrets)
        - Global trading of financial instruments
        """)

        st.subheader("6. Method 5: Transactional Net Margin Method (TNMM)")
        st.markdown("""
        **Principle:** Compares the **net profit margin** (relative to an appropriate base: costs, 
        sales, assets) of the controlled transaction to that of comparable uncontrolled transactions.

        **Common profit level indicators (PLIs):**

        | PLI | Formula | Best For |
        |-----|---------|---------|
        | Net Cost Plus Markup (NCPM) | Net profit / Total costs | Manufacturing, services |
        | Operating Margin (OM) | Operating profit / Sales | Distribution |
        | Return on Assets (ROA) | Operating profit / Assets | Capital-intensive businesses |
        | Berry Ratio | Gross profit / Operating expenses | Pure distributors |

        **Rule 75, IT Rules 2023:**
        - Most widely used method in Bangladesh (due to availability of comparables)
        - Can be applied even when transaction-level comparables are hard to find
        - The **tested party** is typically the least complex entity in the transaction

        **Limitation:** Net margins can be affected by factors unrelated to TP (e.g., management efficiency)
        """)

        st.subheader("7. Selecting the Most Appropriate Method")
        st.markdown("""
        Under **Section 179, ITA 2023**, the Most Appropriate Method (MAM) selection considers:

        1. **Nature of the transaction** (goods, services, IP, loans)
        2. **Availability and reliability of data** (internal vs. external comparables)
        3. **Degree of comparability** (fewer adjustments = more reliable)
        4. **FAR analysis** of the tested party

        **Priority Hierarchy (ITA 2023 aligned with OECD):**
        ```
        Traditional transaction methods (CUP, RPM, CPM) 
        are preferred over 
        Transactional profit methods (TNMM, PSM)
        when equally reliable comparables exist.
        ```
        """)

    # ─────────────────────────────────────────────
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: CUP Method — Interest on Intra-Group Loan")
        st.markdown("""
        **Scenario:**  
        ABC Bangladesh Ltd. borrows USD 5 million from its UK parent at **3% interest**.  
        The prevailing market rate for a comparable loan in Bangladesh is **7.5%**.

        **CUP Analysis:**
        ```
        Comparable uncontrolled price (market rate) = 7.5%
        Controlled transaction rate = 3.0%
        
        Arm's Length Price = 7.5%
        
        Annual interest adjustment:
        = USD 5,000,000 × (7.5% − 3.0%)
        = USD 5,000,000 × 4.5%
        = USD 225,000 additional taxable income
        ```
        **Conclusion:** NBR can add back USD 225,000 to taxable income of ABC Bangladesh.
        """)

        st.subheader("Example 2: RPM — Intra-Group Distribution")
        st.markdown("""
        **Scenario:**  
        Sun Electronics Bangladesh purchases mobile phones from Sun Korea (parent) for BDT 8,000/unit 
        and resells to local retailers at BDT 12,000/unit.  
        Comparable independent distributors earn a **gross margin of 25–30%**.

        **RPM Calculation:**
        ```
        Actual gross margin = (12,000 − 8,000) / 12,000 = 33.3%
        Arm's length range = 25% – 30%
        
        33.3% is ABOVE the arm's length range.
        
        At arm's length (at 27.5% midpoint):
        ALP Purchase Price = 12,000 × (1 − 0.275) = BDT 8,700/unit
        ```
        **Conclusion:** The actual purchase price (BDT 8,000) is too low → Bangladesh subsidiary 
        is over-earning → may indicate transfer from Korea is underpriced.
        """)

        st.subheader("Example 3: CPM — Contract Manufacturing")
        st.markdown("""
        **Scenario:**  
        Delta Garments Ltd. (Bangladesh) manufactures shirts for its French parent at cost + 5%.  
        Comparable contract manufacturers earn a **cost plus markup of 8–12%**.

        **CPM Analysis:**
        ```
        Delta's cost of production per shirt = BDT 600
        Controlled price = BDT 600 × (1 + 5%) = BDT 630
        
        Arm's length range = 8% to 12% (i.e., BDT 648 to BDT 672)
        
        BDT 630 is BELOW the arm's length range.
        Adjustment to median (10%): ALP = BDT 600 × 1.10 = BDT 660
        ```
        **Adjustment:** NBR adjusts taxable income by BDT 30 per shirt.
        """)

        st.subheader("Example 4: TNMM — IT Services")
        st.markdown("""
        **Scenario:**  
        TechBD Ltd. provides software development services to its Singapore parent.  
        TechBD earns a Net Cost Plus Margin (NCPM) of **4%**.  
        Comparable independent IT service companies earn NCPM of **8–14%** (IQR).

        **TNMM Analysis:**
        ```
        Tested party NCPM = 4%
        ALR (IQR) = 8% – 14%, Median = 11%
        
        4% is BELOW the arm's length range.
        Adjustment to median: NCPM adjusted to 11%.
        
        If TechBD total costs = BDT 10 Crore:
        At 4%: Profit = BDT 40 lakh
        At 11%: Profit = BDT 110 lakh
        Adjustment = BDT 70 lakh added to taxable income
        ```
        """)

    # ─────────────────────────────────────────────
    with tab3:
        st.header("Interactive Exercise")

        method = st.selectbox("Select a TP Method to Calculate:",
            ["CUP Method", "Resale Price Method (RPM)", "Cost Plus Method (CPM)", "TNMM"])

        st.markdown("---")

        if method == "CUP Method":
            st.subheader("CUP Method Calculator")
            principal = st.number_input("Principal Amount (BDT or USD)", min_value=0.0, value=10000000.0, step=100000.0)
            controlled_rate = st.number_input("Controlled transaction rate (%)", min_value=0.0, value=3.0, step=0.5)
            alp_rate = st.number_input("Arm's length rate / comparable rate (%)", min_value=0.0, value=7.5, step=0.5)
            if st.button("Calculate CUP Adjustment"):
                diff = alp_rate - controlled_rate
                adjustment = principal * diff / 100
                st.metric("Rate difference", f"{diff:.2f}%")
                st.metric("Annual TP adjustment (income understatement)", f"{adjustment:,.0f}")
                if diff > 0:
                    st.error(f"❌ Controlled rate ({controlled_rate}%) is below ALP ({alp_rate}%). Income understated by {adjustment:,.0f}.")
                elif diff < 0:
                    st.warning(f"⚠️ Controlled rate ({controlled_rate}%) is above ALP ({alp_rate}%). Review overpayment.")
                else:
                    st.success("✅ Controlled rate equals ALP. No adjustment required.")

        elif method == "Resale Price Method (RPM)":
            st.subheader("RPM Calculator")
            resale_price = st.number_input("Resale price to unrelated party (BDT)", min_value=0.0, value=12000.0)
            purchase_price = st.number_input("Actual purchase price from related party (BDT)", min_value=0.0, value=8000.0)
            alp_margin_min = st.number_input("ALP gross margin - minimum (%)", min_value=0.0, value=25.0)
            alp_margin_max = st.number_input("ALP gross margin - maximum (%)", min_value=0.0, value=30.0)
            if st.button("Calculate RPM"):
                actual_margin = (resale_price - purchase_price) / resale_price * 100
                alp_min_price = resale_price * (1 - alp_margin_max / 100)
                alp_max_price = resale_price * (1 - alp_margin_min / 100)
                alp_mid_price = resale_price * (1 - (alp_margin_min + alp_margin_max) / 2 / 100)
                st.metric("Actual Gross Margin", f"{actual_margin:.1f}%")
                st.markdown(f"ALP purchase price range: **BDT {alp_min_price:,.0f} – BDT {alp_max_price:,.0f}**")
                if alp_min_price <= purchase_price <= alp_max_price:
                    st.success("✅ Purchase price is within arm's length range. No adjustment required.")
                elif purchase_price < alp_min_price:
                    st.error(f"❌ Purchase price (BDT {purchase_price:,.0f}) is BELOW ALP minimum. Adjustment needed. ALP midpoint: BDT {alp_mid_price:,.0f}")
                else:
                    st.warning(f"⚠️ Purchase price (BDT {purchase_price:,.0f}) is ABOVE ALP maximum. Review required.")

        elif method == "Cost Plus Method (CPM)":
            st.subheader("CPM Calculator")
            cost = st.number_input("Cost of production/service (BDT)", min_value=0.0, value=600.0)
            controlled_markup = st.number_input("Actual markup charged (%)", min_value=0.0, value=5.0)
            alp_markup_min = st.number_input("ALP markup - minimum (%)", min_value=0.0, value=8.0)
            alp_markup_max = st.number_input("ALP markup - maximum (%)", min_value=0.0, value=12.0)
            if st.button("Calculate CPM"):
                actual_price = cost * (1 + controlled_markup / 100)
                alp_price_min = cost * (1 + alp_markup_min / 100)
                alp_price_max = cost * (1 + alp_markup_max / 100)
                alp_median = cost * (1 + (alp_markup_min + alp_markup_max) / 2 / 100)
                st.metric("Actual Transfer Price", f"BDT {actual_price:,.2f}")
                st.markdown(f"ALP price range: **BDT {alp_price_min:,.2f} – BDT {alp_price_max:,.2f}**")
                if alp_price_min <= actual_price <= alp_price_max:
                    st.success("✅ Actual transfer price is within arm's length range.")
                elif actual_price < alp_price_min:
                    adj = alp_median - actual_price
                    st.error(f"❌ Price BDT {actual_price:,.2f} is below ALP. Adjustment: +BDT {adj:,.2f} per unit to reach median BDT {alp_median:,.2f}.")
                else:
                    st.warning(f"⚠️ Price above ALP maximum. Review required.")

        elif method == "TNMM":
            st.subheader("TNMM Calculator")
            revenue = st.number_input("Revenue of tested party (BDT Lakh)", min_value=0.0, value=500.0)
            total_costs = st.number_input("Total costs of tested party (BDT Lakh)", min_value=0.0, value=480.0)
            alp_ncpm_min = st.number_input("ALP NCPM - minimum (%)", min_value=0.0, value=8.0)
            alp_ncpm_max = st.number_input("ALP NCPM - maximum (%)", min_value=0.0, value=14.0)
            if st.button("Calculate TNMM"):
                actual_profit = revenue - total_costs
                actual_ncpm = actual_profit / total_costs * 100
                alp_profit_min = total_costs * alp_ncpm_min / 100
                alp_profit_max = total_costs * alp_ncpm_max / 100
                alp_median_profit = total_costs * (alp_ncpm_min + alp_ncpm_max) / 2 / 100
                st.metric("Actual Profit (BDT Lakh)", f"{actual_profit:,.2f}")
                st.metric("Actual NCPM", f"{actual_ncpm:.1f}%")
                st.markdown(f"ALP profit range: **BDT {alp_profit_min:,.2f} – BDT {alp_profit_max:,.2f} Lakh**")
                if alp_profit_min <= actual_profit <= alp_profit_max:
                    st.success("✅ Actual NCPM is within arm's length range.")
                elif actual_profit < alp_profit_min:
                    adj = alp_median_profit - actual_profit
                    st.error(f"❌ NCPM {actual_ncpm:.1f}% is below ALP. Adjustment: +BDT {adj:,.2f} Lakh to taxable income.")
                else:
                    st.info("ℹ️ NCPM is above ALP range. No downward adjustment available under Bangladesh law (adjustments only upward).")

    # ─────────────────────────────────────────────
    with tab4:
        st.header("Quiz")

        st.markdown("**1. Which TP method is most suitable for commodity transactions (e.g., jute exports)?**")
        q1 = st.radio("Select:", ["TNMM", "RPM", "CUP Method", "Profit Split Method"], key="m3q1")
        if st.button("Check", key="m3c1"):
            if q1 == "CUP Method":
                st.success("✅ Correct! CUP is most reliable for commodity transactions where market prices are available.")
            else:
                st.error("❌ Incorrect. CUP Method is most appropriate for commodities due to available market price data.")

        st.markdown("---")
        st.markdown("**2. Under the Resale Price Method, the arm's length purchase price is calculated as:**")
        q2 = st.radio("Select:", [
            "Cost × (1 + Markup%)",
            "Resale Price × (1 − Arm's Length Gross Margin%)",
            "Net profit / Total costs",
            "Combined profit × Contribution ratio"
        ], key="m3q2")
        if st.button("Check", key="m3c2"):
            if q2 == "Resale Price × (1 − Arm's Length Gross Margin%)":
                st.success("✅ Correct! RPM formula: ALP = Resale Price × (1 − Arm's Length Gross Margin%)")
            else:
                st.error("❌ Incorrect. RPM: ALP = Resale Price × (1 − Arm's Length Gross Margin%)")

        st.markdown("---")
        st.markdown("**3. The TNMM is most widely used in Bangladesh because:**")
        q3 = st.radio("Select:", [
            "It requires no comparables",
            "It is mandatory under ITA 2023",
            "Comparables are more available at the net margin level than transaction level",
            "It always gives the highest adjustment"
        ], key="m3q3")
        if st.button("Check", key="m3c3"):
            if q3 == "Comparables are more available at the net margin level than transaction level":
                st.success("✅ Correct! TNMM is popular because net margin comparables from databases are more readily available.")
            else:
                st.error("❌ Incorrect. TNMM is widely used because net margin level comparables are more accessible.")

        st.markdown("---")
        st.markdown("**4. The Profit Split Method is most appropriate when:**")
        q4 = st.radio("Select:", [
            "Transactions involve routine manufacturing",
            "The tested party is a simple distributor",
            "Transactions are highly integrated and involve unique intangibles",
            "A CUP comparable is available"
        ], key="m3q4")
        if st.button("Check", key="m3c4"):
            if q4 == "Transactions are highly integrated and involve unique intangibles":
                st.success("✅ Correct! PSM is used for highly integrated transactions where one party cannot be the tested party.")
            else:
                st.error("❌ Incorrect. PSM is appropriate for highly integrated transactions with unique intangibles.")

        st.markdown("---")
        st.markdown("**5. Under Section 179 ITA 2023 (Most Appropriate Method), when two methods give equally reliable results, which takes priority?**")
        q5 = st.radio("Select:", [
            "TNMM takes priority",
            "Traditional transaction methods (CUP, RPM, CPM) take priority",
            "The taxpayer chooses freely",
            "Profit Split Method takes priority"
        ], key="m3q5")
        if st.button("Check", key="m3c5"):
            if q5 == "Traditional transaction methods (CUP, RPM, CPM) take priority":
                st.success("✅ Correct! ITA 2023 (aligned with OECD) gives preference to traditional transaction methods when equally reliable comparables exist.")
            else:
                st.error("❌ Incorrect. Traditional transaction methods take precedence over profit methods when equally reliable.")

    # ─────────────────────────────────────────────
    with tab5:
        st.header("Module Summary")

        st.markdown("""
        ### 🎯 Key Takeaways

        | Method | Formula | Best For |
        |--------|---------|---------|
        | **CUP** | ALP = Comparable price ± adjustments | Commodities, loans, IP licences |
        | **RPM** | ALP = Resale Price × (1 − ALP Margin%) | Distribution, trading |
        | **CPM** | ALP = Cost × (1 + ALP Markup%) | Manufacturing, services |
        | **PSM** | Split combined profit by FAR contribution | Integrated, unique intangibles |
        | **TNMM** | Compare net margin (NCPM, OM, ROA) | Wide applicability |

        ### 📋 Method Selection Guide
        ```
        Is there a reliable market price (commodity, publicly traded)?
          → YES → CUP Method

        Is the tested party a distributor with limited value-add?
          → YES → Resale Price Method

        Is the tested party a contract manufacturer or service provider?
          → YES → Cost Plus Method

        Are both parties highly integrated with unique intangibles?
          → YES → Profit Split Method

        None of the above / wider comparables needed?
          → TNMM
        ```

        ### 📊 Common PLIs for TNMM in Bangladesh
        | Industry | PLI Used |
        |----------|---------|
        | Garment manufacturing | Net Cost Plus Margin (NCPM) |
        | IT/Software services | NCPM |
        | Distribution | Operating Margin (OM) |
        | Financial services | Return on Assets (ROA) |
        | Trading/intermediary | Berry Ratio |
        """)

        st.success("🎓 **Module 3 Complete!** You can now select and apply the appropriate TP method under ITA 2023.")
        st.info("💡 **Next**: Proceed to Module 4 — TP Documentation & Compliance Requirements.")

if __name__ == "__main__":
    show()