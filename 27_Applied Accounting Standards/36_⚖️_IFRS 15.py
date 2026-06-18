import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("💰 IFRS 15: Revenue from Contracts with Customers")
    st.markdown("*Master the 5-step revenue recognition model applied to all customer contracts*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Core Principle and Scope")
        st.markdown("""
        **Core Principle:** Recognise revenue to depict the transfer of promised goods or services to customers in an amount that reflects the consideration the entity expects to be entitled to in exchange.

        **IFRS 15 applies to:** All contracts with customers EXCEPT leases (IFRS 16), insurance contracts (IFRS 17), financial instruments (IFRS 9), and certain non-monetary exchanges between entities in the same business to facilitate sales to customers.
        """)

        st.subheader("2. The 5-Step Model")
        steps_data = pd.DataFrame({
            "Step": ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5"],
            "Action": [
                "Identify the contract with a customer",
                "Identify the performance obligations in the contract",
                "Determine the transaction price",
                "Allocate the transaction price to performance obligations",
                "Recognise revenue when (or as) performance obligations are satisfied"
            ],
            "Key Question": [
                "Is there an enforceable agreement with commercial substance?",
                "What distinct promises (goods/services) exist?",
                "How much consideration does the entity expect to receive?",
                "How should the total price be split among multiple obligations?",
                "Is control transferred at a point in time, or over time?"
            ]
        })
        st.dataframe(steps_data, use_container_width=True, hide_index=True)

        st.subheader("3. Step 1 — Identify the Contract")
        st.markdown("""
        A contract exists when ALL FIVE criteria are met:
        1. Parties have approved the contract and are committed to perform
        2. Each party's rights regarding goods/services can be identified
        3. Payment terms can be identified
        4. The contract has commercial substance
        5. Collection of consideration is **probable**
        """)

        st.subheader("4. Step 2 — Identify Performance Obligations")
        st.markdown("""
        A good or service is **distinct** (and thus a separate performance obligation) if BOTH:
        - The customer can benefit from the good/service on its own or with readily available resources
        - The promise is **separately identifiable** from other promises in the contract (not highly interdependent/interrelated)

        **Series of distinct goods/services:** If substantially the same and have the same pattern of transfer, treated as a SINGLE performance obligation (e.g., a monthly cleaning service contract).
        """)

        st.subheader("5. Step 3 — Determine the Transaction Price")
        st.markdown("""
        Transaction price = amount of consideration the entity expects to be entitled to, considering:

        | Component | Treatment |
        |---|---|
        | **Variable consideration** | Estimate using EXPECTED VALUE (probability-weighted) or MOST LIKELY AMOUNT — whichever better predicts the entitlement |
        | **Constraint on variable consideration** | Include variable consideration ONLY to the extent it is HIGHLY PROBABLE that a significant revenue reversal will NOT occur |
        | **Significant financing component** | Adjust for the time value of money if payment timing differs significantly from transfer of goods/services (practical expedient: ignore if period ≤ 1 year) |
        | **Non-cash consideration** | Measure at fair value |
        | **Consideration payable to customer** | Reduce transaction price (unless payment is for a distinct good/service received from the customer) |
        """)

        st.subheader("6. Step 4 — Allocate the Transaction Price")
        st.markdown("""
        Allocate based on **relative standalone selling prices (SSP)** of each performance obligation.

        ```
        Allocated Amount = Total Transaction Price × (Obligation's SSP / Sum of All SSPs)
        ```

        **Estimating SSP** when not directly observable:
        - Adjusted market assessment approach
        - Expected cost plus margin approach
        - Residual approach (only when SSP is highly variable or uncertain)

        **Discounts:** Generally allocated proportionately across all obligations, UNLESS observable evidence shows the discount relates to specific obligation(s) only.
        """)

        st.subheader("7. Step 5 — Recognise Revenue")
        st.markdown("""
        Revenue is recognised when control transfers — either **OVER TIME** or **AT A POINT IN TIME**.

        **Recognise OVER TIME if ANY of these criteria are met:**
        1. Customer simultaneously receives and consumes benefits as the entity performs
        2. The entity's performance creates or enhances an asset the customer controls as it's created
        3. The asset has no alternative use to the entity AND the entity has an enforceable right to payment for performance completed to date

        **If none of the above apply → recognise AT A POINT IN TIME** (when control transfers — consider indicators: present right to payment, legal title, physical possession, risks/rewards, customer acceptance).

        **Measuring progress for over-time recognition:**
        - **Output methods**: units produced/delivered, milestones reached, surveys of performance completed
        - **Input methods**: costs incurred relative to total expected costs, labour hours, machine hours
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Identifying Performance Obligations — Bundled Sale")
        st.markdown("""
        **Telecom company sells a smartphone bundled with a 24-month service plan for $1,200 total.**

        | Component | Standalone Selling Price | Distinct? |
        |---|---|---|
        | Smartphone | $800 | Yes — customer can use phone independently |
        | 24-month service | $600 (=$25/month) | Yes — separately identifiable |
        | **Total SSP** | **$1,400** | |

        **Allocation of $1,200 transaction price:**
        - Phone: $1,200 × ($800/$1,400) = **$685.71** (recognised at point of sale — control transfers immediately)
        - Service: $1,200 × ($600/$1,400) = **$514.29** (recognised over 24 months — over time, as customer consumes service)
        """)

        st.subheader("Example 2: Variable Consideration — Expected Value Method")
        st.markdown("""
        **Construction company contract includes a bonus for early completion:**
        - Base price: $5,000,000
        - Bonus if completed 2 weeks early: $500,000 (entity estimates 60% probability)
        - Bonus if completed on time: $200,000 (entity estimates 30% probability)
        - No bonus if late: 10% probability

        **Expected Value = (60% × $500,000) + (30% × $200,000) + (10% × $0) = $300,000 + $60,000 + $0 = $360,000**

        **Estimated Transaction Price = $5,000,000 + $360,000 = $5,360,000**

        Apply the constraint: is it HIGHLY PROBABLE no significant reversal will occur? If the entity has strong historical track record of hitting bonuses, include the full estimate.
        """)

        st.subheader("Example 3: Over Time vs Point in Time Recognition")
        comparison = pd.DataFrame({
            "Scenario": [
                "Building a custom factory on customer's land (no alternative use, enforceable payment right)",
                "Selling standard inventory off the shelf",
                "Software-as-a-Service (SaaS) subscription",
                "Building a standard house for resale on developer's own land"
            ],
            "Recognition": ["Over Time", "Point in Time", "Over Time", "Point in Time"],
            "Reasoning": [
                "Asset has no alternative use + enforceable right to payment for work completed",
                "Control transfers at delivery — discrete point",
                "Customer simultaneously receives and consumes the service as performed",
                "Customer doesn't control the asset during construction; standard inventory until sold"
            ]
        })
        st.dataframe(comparison, use_container_width=True, hide_index=True)

        st.subheader("Example 4: Percentage of Completion — Input Method")
        st.markdown("""
        **Construction contract: Total contract price $10,000,000. Total estimated costs $8,000,000.**

        | Year | Costs Incurred to Date | % Complete (Costs Incurred/Total Est. Costs) | Cumulative Revenue | Revenue This Year |
        |---|---|---|---|---|
        | 1 | $2,000,000 | 25% | $2,500,000 | $2,500,000 |
        | 2 | $5,200,000 | 65% | $6,500,000 | $4,000,000 |
        | 3 | $8,000,000 | 100% | $10,000,000 | $3,500,000 |

        Revenue recognised proportionately to costs incurred — an INPUT method measuring progress toward completion.
        """)

        st.subheader("Example 5: Significant Financing Component")
        st.markdown("""
        **Customer pays $1,000,000 upfront for goods to be delivered in 2 years. Market interest rate: 5%.**

        Since payment timing significantly precedes delivery (2 years), a financing component exists.

        **Transaction price (revenue) recognised at delivery = $1,000,000 × (1.05)² = $1,102,500**

        - $1,000,000 = Original consideration (recorded as deferred revenue/contract liability initially)
        - $102,500 = Interest expense accrued over 2 years (NOT revenue from goods)

        This reflects that the customer effectively provided financing to the entity.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Transaction Price Allocation Calculator")
        st.markdown("Allocate a bundled transaction price across performance obligations:")
        n_obligations = st.number_input("Number of performance obligations", value=2, min_value=2, max_value=5)
        total_price = st.number_input("Total Transaction Price ($)", value=1200, step=10)

        ssp_values = []
        for i in range(int(n_obligations)):
            ssp = st.number_input(f"Standalone Selling Price — Obligation {i+1} ($)", value=800 if i==0 else 600, step=10, key=f"ssp_{i}")
            ssp_values.append(ssp)

        if st.button("Allocate Transaction Price"):
            total_ssp = sum(ssp_values)
            rows_alloc = []
            for i, ssp in enumerate(ssp_values, 1):
                allocated = total_price * (ssp / total_ssp)
                rows_alloc.append({"Obligation": f"Obligation {i}", "SSP ($)": f"{ssp:,.2f}", "Allocated Price ($)": f"{allocated:,.2f}"})
            st.dataframe(pd.DataFrame(rows_alloc), use_container_width=True, hide_index=True)
            st.info(f"Total SSP: ${total_ssp:,.2f} | Total Transaction Price: ${total_price:,.2f} | Implicit Discount: ${total_ssp - total_price:,.2f}")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Variable Consideration Calculator (Expected Value)")
        st.markdown("Calculate expected value of variable consideration:")
        n_scenarios = st.number_input("Number of outcome scenarios", value=3, min_value=2, max_value=5)
        scenarios = []
        total_prob_check = 0
        for i in range(int(n_scenarios)):
            c1, c2 = st.columns(2)
            amt = c1.number_input(f"Scenario {i+1} Amount ($)", value=500000 if i==0 else (200000 if i==1 else 0), key=f"sc_amt_{i}")
            prob = c2.number_input(f"Scenario {i+1} Probability (%)", value=60.0 if i==0 else (30.0 if i==1 else 10.0), key=f"sc_prob_{i}")
            scenarios.append((amt, prob))
            total_prob_check += prob

        if st.button("Calculate Expected Value"):
            if abs(total_prob_check - 100) > 0.1:
                st.error(f"⚠️ Probabilities must sum to 100%. Current total: {total_prob_check:.1f}%")
            else:
                ev = sum([amt * prob / 100 for amt, prob in scenarios])
                st.success(f"**Expected Value of Variable Consideration = ${ev:,.0f}**")
                base_price = st.number_input("Base/Fixed Price ($)", value=5000000, step=10000, key="base_price_tool")
                st.markdown(f"**Total Estimated Transaction Price = ${base_price:,.0f} + ${ev:,.0f} = ${base_price + ev:,.0f}**")

        st.markdown("---")
        st.subheader("🔧 Tool 3: Percentage of Completion Calculator")
        col1, col2 = st.columns(2)
        with col1:
            contract_price_poc = st.number_input("Total Contract Price ($)", value=10000000, step=100000)
            total_est_costs = st.number_input("Total Estimated Costs ($)", value=8000000, step=100000)
        with col2:
            costs_to_date = st.number_input("Costs Incurred to Date ($)", value=5200000, step=100000)
            prior_revenue = st.number_input("Revenue Recognised in Prior Periods ($)", value=2500000, step=100000)

        if st.button("Calculate Revenue This Period"):
            pct_complete = costs_to_date / total_est_costs * 100
            cumulative_revenue = contract_price_poc * (costs_to_date / total_est_costs)
            current_period_revenue = cumulative_revenue - prior_revenue
            st.markdown(f"""
            | Item | Value |
            |---|---|
            | % Complete | {pct_complete:.1f}% |
            | Cumulative Revenue to Date | ${cumulative_revenue:,.0f} |
            | Less: Prior Period Revenue | (${prior_revenue:,.0f}) |
            | **Revenue This Period** | **${current_period_revenue:,.0f}** |
            """)

    with tab4:
        st.header("Visualizations")

        st.subheader("The 5-Step Revenue Recognition Model")
        st.markdown("""
        ```
        STEP 1                STEP 2              STEP 3              STEP 4               STEP 5
        Identify the    →   Identify the     →  Determine the   →  Allocate the     →   Recognise revenue
        contract            performance          transaction         transaction          when/as performance
                             obligations          price               price to             obligations
                                                                       obligations          satisfied
        ```
        """)

        st.subheader("Percentage of Completion — Revenue Recognition Pattern")
        years_poc = [1, 2, 3]
        cum_revenue_poc = [2500000, 6500000, 10000000]
        period_revenue_poc = [2500000, 4000000, 3500000]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=years_poc, y=period_revenue_poc, name="Revenue This Period", marker_color="#2563EB"))
        fig.add_trace(go.Scatter(x=years_poc, y=cum_revenue_poc, name="Cumulative Revenue", line=dict(color="#F59E0B", width=2), mode="lines+markers", yaxis="y2"))
        fig.update_layout(title="Construction Contract — Revenue Recognition Over Time", barmode="group",
                          yaxis=dict(title="Period Revenue ($)"), yaxis2=dict(title="Cumulative Revenue ($)", overlaying="y", side="right"), height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Bundle Allocation — Smartphone + Service Plan")
        fig2 = go.Figure(go.Pie(labels=["Smartphone (Point in Time)", "Service Plan (Over 24 Months)"],
                                values=[685.71, 514.29], hole=0.4, marker_colors=["#2563EB","#10B981"]))
        fig2.update_layout(title="Transaction Price Allocation ($1,200 Bundle)", height=350)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. The 5-step revenue recognition model under IFRS 15 begins with:**")
        q1 = st.radio("", ["Determining the transaction price", "Identifying the contract with a customer", "Allocating the transaction price", "Recognising revenue"], key="ifrs15q1")
        if st.button("Check Answer", key="ifrs15c1"):
            if q1 == "Identifying the contract with a customer":
                st.success("✅ Correct! Step 1 is identifying the contract — confirming all 5 contract existence criteria are met before proceeding.")
            else:
                st.error("❌ Step 1 = Identify the contract. The full order is: Contract → Performance Obligations → Transaction Price → Allocation → Recognition.")

        st.markdown("---")
        st.markdown("**2. A good or service is 'distinct' (separate performance obligation) when:**")
        q2 = st.radio("", [
            "It costs more than $1,000",
            "The customer can benefit from it on its own AND it is separately identifiable from other promises",
            "It is delivered in a different month than other goods",
            "It has a different supplier"
        ], key="ifrs15q2")
        if st.button("Check Answer", key="ifrs15c2"):
            if q2 == "The customer can benefit from it on its own AND it is separately identifiable from other promises":
                st.success("✅ Correct! BOTH criteria must be met: (1) customer can benefit on its own/with readily available resources, AND (2) it's separately identifiable (not highly interdependent with other promises).")
            else:
                st.error("❌ Distinct = customer benefit on its own AND separately identifiable — both conditions required.")

        st.markdown("---")
        st.markdown("**3. Variable consideration should be included in the transaction price to the extent that:**")
        q3 = st.radio("", [
            "It is certain to be received",
            "It is highly probable that a significant revenue reversal will NOT occur",
            "The customer has paid in advance",
            "Management believes it is appropriate"
        ], key="ifrs15q3")
        if st.button("Check Answer", key="ifrs15c3"):
            if q3 == "It is highly probable that a significant revenue reversal will NOT occur":
                st.success("✅ Correct! The CONSTRAINT on variable consideration requires inclusion only to the extent HIGHLY PROBABLE that a SIGNIFICANT REVERSAL will not occur in future periods.")
            else:
                st.error("❌ The constraint test = highly probable that NO significant revenue reversal will occur — not certainty, prepayment, or pure management discretion.")

        st.markdown("---")
        st.markdown("**4. Revenue should be recognised over time when:**")
        q4 = st.radio("", [
            "The customer pays in installments",
            "The contract duration exceeds 12 months",
            "The asset created has no alternative use AND the entity has an enforceable right to payment for performance completed to date (among other criteria)",
            "The entity prefers smoother revenue recognition"
        ], key="ifrs15q4")
        if st.button("Check Answer", key="ifrs15c4"):
            if q4 == "The asset created has no alternative use AND the entity has an enforceable right to payment for performance completed to date (among other criteria)":
                st.success("✅ Correct! This is one of the three specific criteria for over-time recognition. Payment timing or contract duration alone do NOT determine the recognition pattern.")
            else:
                st.error("❌ Over-time recognition depends on specific criteria (simultaneous receipt/consumption, asset customer controls as created, OR no alternative use + enforceable payment right) — not payment timing or preference.")

        st.markdown("---")
        st.markdown("**5. When allocating the transaction price across multiple performance obligations, the basis is:**")
        q5 = st.radio("", [
            "Equal allocation across all obligations", "Relative standalone selling prices", "The cost of each obligation to the entity", "First-in-first-out allocation"
        ], key="ifrs15q5")
        if st.button("Check Answer", key="ifrs15c5"):
            if q5 == "Relative standalone selling prices":
                st.success("✅ Correct! Allocation is based on RELATIVE STANDALONE SELLING PRICES (SSP) — not equal splits, cost, or arbitrary ordering.")
            else:
                st.error("❌ Allocation = RELATIVE STANDALONE SELLING PRICES of each performance obligation, not equal split or cost-based.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### The 5-Step Model
        ```
        1. Identify the contract        → 5 criteria must be met (incl. collection probable)
        2. Identify performance obligations → Distinct = customer benefit + separately identifiable
        3. Determine transaction price  → Variable consideration (expected value/most likely) + constraint
        4. Allocate transaction price   → Relative standalone selling prices (SSP)
        5. Recognise revenue            → Over time (3 criteria) OR point in time
        ```

        ### Variable Consideration
        - **Expected value** = probability-weighted average (large number of similar contracts)
        - **Most likely amount** = single most likely outcome (binary/few outcomes)
        - **Constraint**: include only if highly probable no significant reversal

        ### Over Time vs Point in Time
        | Over Time (ANY ONE applies) | Point in Time (default) |
        |---|---|
        | Customer simultaneously receives/consumes | Control transfers at delivery |
        | Creates/enhances asset customer controls | Indicators: legal title, physical possession, risk/reward |
        | No alternative use + enforceable payment right | |

        ### Measuring Progress (Over Time)
        - Output methods: units delivered, milestones
        - Input methods: % of costs incurred, labour hours
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
5 Steps: Contract → Obligations → Price → Allocate → Recognise
Distinct = Customer benefit (alone) + Separately identifiable
Variable consideration: Expected Value OR Most Likely Amount + CONSTRAINT
Allocation basis: RELATIVE STANDALONE SELLING PRICES
Over time: simultaneous consumption OR enhances customer asset OR no alt. use + payment right
        """)

        st.success("🎓 **IFRS 15 Complete!** You can now apply the 5-step model to identify contracts, allocate prices, and determine appropriate revenue recognition timing.")
        st.info("💡 **Next**: IFRS 16 — Leases")

if __name__ == "__main__":
    show()