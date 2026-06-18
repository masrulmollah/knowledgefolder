import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🛡️ IFRS 17: Insurance Contracts")
    st.markdown("*Master the General Model, Premium Allocation Approach and Variable Fee Approach for insurance contracts*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Scope")
        st.markdown("""
        **IFRS 17** establishes principles for recognition, measurement, presentation and disclosure of **insurance contracts** — replacing the patchwork approach under the previous IFRS 4.

        **An insurance contract** is a contract under which one party (the issuer) accepts **significant insurance risk** from another party by agreeing to compensate them if a specified uncertain future event adversely affects them.

        **Significant insurance risk test:** A scenario must exist in which the insurer pays significantly more than it would if the insured event did NOT occur.
        """)

        st.subheader("2. The Three Measurement Models")
        models_data = pd.DataFrame({
            "Model": ["General Model (GMM)", "Premium Allocation Approach (PAA)", "Variable Fee Approach (VFA)"],
            "Also Known As": ["Building Block Approach (BBA)", "Simplified Approach", "VFA"],
            "When Used": [
                "Default model for most long-duration contracts",
                "Optional simplification for SHORT-duration contracts (coverage period ≤ 1 year, or if it doesn't differ materially from GMM)",
                "MANDATORY for contracts with direct participation features (e.g., unit-linked, with-profits)"
            ],
            "Key Feature": [
                "Full building blocks: fulfilment cash flows + CSM",
                "Similar to unearned premium reserve under old models — simpler",
                "CSM adjusted for changes in entity's share of underlying items (not locked in like GMM)"
            ]
        })
        st.dataframe(models_data, use_container_width=True, hide_index=True)

        st.subheader("3. General Model — The Four Building Blocks")
        st.markdown("""
        The insurance contract liability comprises:

        | Building Block | Description |
        |---|---|
        | **1. Estimates of Future Cash Flows** | Probability-weighted estimate of future premiums, claims, expenses |
        | **2. Discounting** | Adjust for time value of money using current discount rates |
        | **3. Risk Adjustment (RA)** | Compensation required for bearing uncertainty about amount/timing of cash flows |
        | **4. Contractual Service Margin (CSM)** | Unearned profit — recognised in P&L as service is provided over the coverage period |

        ```
        Insurance Contract Liability = Fulfilment Cash Flows (1+2+3) + CSM
        Fulfilment Cash Flows = PV of Future Cash Flows + Risk Adjustment
        ```

        **CSM cannot be negative** — if the initial calculation would be negative (the contract is "onerous"), recognise a **loss immediately in P&L** instead of a CSM asset.
        """)

        st.subheader("4. Contractual Service Margin (CSM) — Key Mechanics")
        st.markdown("""
        - Represents the **unearned profit** the entity will recognise as it provides insurance coverage
        - **At initial recognition:** calibrated so that NO gain arises (day 1 profit is deferred, not immediately recognised)
        - **Subsequently:** released to P&L systematically over the coverage period, based on **coverage units** (reflecting quantity of benefits provided)
        - **Adjusted for:** changes in estimates of future cash flows relating to FUTURE service (changes relating to PAST/CURRENT service go to P&L immediately)
        - CSM is **NOT discounted to a new rate** — accretes interest at the LOCKED-IN rate from initial recognition (under GMM)
        """)

        st.subheader("5. Premium Allocation Approach (PAA)")
        st.markdown("""
        Simplified approach similar to unearned premium accounting:
        - **Liability for Remaining Coverage (LRC)** = premiums received less amounts recognised as revenue (similar to unearned premium reserve)
        - **Liability for Incurred Claims (LIC)** = estimate of claims incurred but not yet paid (discounted if expected to be settled >1 year later)
        - No explicit CSM tracking — profit emerges naturally as revenue is recognised over the coverage period
        - Eligibility: coverage period ≤ 1 year, OR result would not differ materially from the General Model
        """)

        st.subheader("6. Presentation — Insurance Revenue and Service Result")
        st.markdown("""
        **Key change:** Premiums received are NO LONGER simply "revenue" — IFRS 17 separates:

        | Component | Where Recognised |
        |---|---|
        | **Insurance Revenue** | P&L — reflects services provided (excludes investment components) |
        | **Insurance Service Expenses** | P&L — claims, expenses, amortisation of acquisition costs |
        | **Insurance Finance Income/Expenses** | P&L or OCI (entity's accounting policy choice) — effect of time value of money and financial risk |

        **No more "premium = revenue"** — this eliminates premium volume distortion that existed under IFRS 4.
        """)

        st.subheader("7. Level of Aggregation")
        st.markdown("""
        Contracts are grouped into **portfolios** (similar risks, managed together), then divided by:
        1. **Onerous contracts** at initial recognition
        2. Contracts with **no significant possibility of becoming onerous**
        3. **Remaining contracts** in the portfolio

        Cannot offset losses in one group against profits in another — groups are NOT combined.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Initial Recognition — General Model")
        st.markdown("""
        **5-year life insurance contract. Premium received: $500,000**

        | Building Block | Amount |
        |---|---|
        | PV of expected future claims | $350,000 |
        | PV of expected future expenses | $50,000 |
        | Risk Adjustment | $40,000 |
        | **Fulfilment Cash Flows** | **$440,000** |
        | Premium received | $500,000 |
        | **CSM (Day 1 profit deferred)** | **$60,000** |

        **Initial liability recognised = Fulfilment Cash Flows + CSM = $440,000 + $60,000 = $500,000** (equals premium — no day-1 gain)

        ```
        Dr  Cash                          $500,000
            Cr  Insurance Contract Liability   $500,000
                (comprising: FCF $440,000 + CSM $60,000)
        ```
        """)

        st.subheader("Example 2: CSM Release Over Coverage Period")
        st.markdown("""
        **CSM of $60,000, 5-year coverage period, coverage units (assume equal allocation): 20% per year**

        | Year | Opening CSM | Interest Accretion (5%) | CSM Release to P&L | Closing CSM |
        |---|---|---|---|---|
        | 1 | $60,000 | $3,000 | ($12,600) | $50,400 |
        | 2 | $50,400 | $2,520 | ($10,584) | $42,336 |
        | 3 | $42,336 | $2,117 | ($8,891) | $35,562 |
        | 4 | $35,562 | $1,778 | ($7,468) | $29,872 |
        | 5 | $29,872 | $1,494 | ($6,277)* | $0 |

        *Final year releases remaining balance. Each year's release = (Opening + Interest) × 20% coverage units, adjusted in the final year.
        """)

        st.subheader("Example 3: Onerous Contract (Loss Recognised Immediately)")
        st.markdown("""
        **Contract with adverse pricing:**

        | | Amount |
        |---|---|
        | Premium received | $300,000 |
        | PV of expected claims | $280,000 |
        | PV of expected expenses | $60,000 |
        | Risk Adjustment | $20,000 |
        | **Fulfilment Cash Flows** | **$360,000** |

        **CSM calculation = $300,000 − $360,000 = ($60,000) → NEGATIVE**

        Since CSM cannot be negative: **recognise a LOSS of $60,000 immediately in P&L** at initial recognition. No CSM asset is created.

        ```
        Dr  Insurance Service Expense (Loss)   $60,000
        Dr  Cash                              $300,000
            Cr  Insurance Contract Liability        $360,000
        ```
        """)

        st.subheader("Example 4: Premium Allocation Approach (PAA) — Annual Motor Insurance")
        st.markdown("""
        **1-year motor insurance contract. Premium: $1,200, paid upfront.**

        | Period | Liability for Remaining Coverage | Revenue Recognised |
        |---|---|---|
        | Inception | $1,200 | $0 |
        | After 3 months (25% elapsed) | $900 | $300 |
        | After 6 months (50% elapsed) | $600 | $300 |
        | After 9 months (75% elapsed) | $300 | $300 |
        | After 12 months (100% elapsed) | $0 | $300 |

        Revenue recognised straight-line as coverage is provided — simpler than the General Model's building blocks.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: CSM Calculator at Initial Recognition")
        col1, col2 = st.columns(2)
        with col1:
            premium = st.number_input("Premium Received ($)", value=500000, step=10000)
            pv_claims = st.number_input("PV of Expected Future Claims ($)", value=350000, step=10000)
            pv_expenses = st.number_input("PV of Expected Future Expenses ($)", value=50000, step=5000)
            risk_adj = st.number_input("Risk Adjustment ($)", value=40000, step=5000)
        with col2:
            fcf = pv_claims + pv_expenses + risk_adj
            csm = premium - fcf
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | PV of Claims | ${pv_claims:,.0f} |
            | PV of Expenses | ${pv_expenses:,.0f} |
            | Risk Adjustment | ${risk_adj:,.0f} |
            | **Fulfilment Cash Flows** | **${fcf:,.0f}** |
            | Premium Received | ${premium:,.0f} |
            | **CSM (or Loss if negative)** | **${csm:,.0f}** |
            """)
            if csm >= 0:
                st.success(f"✅ CSM = ${csm:,.0f} (Unearned profit — released to P&L over coverage period)")
            else:
                st.error(f"⚠️ Contract is ONEROUS — Loss of ${abs(csm):,.0f} recognised IMMEDIATELY in P&L. No CSM asset created.")

        st.markdown("---")
        st.subheader("🔧 Tool 2: CSM Release Schedule Calculator")
        col1, col2 = st.columns(2)
        with col1:
            initial_csm = st.number_input("Initial CSM ($)", value=60000, step=1000)
            coverage_years = st.number_input("Coverage Period (years)", value=5, min_value=1, max_value=30)
            interest_rate_csm = st.number_input("Interest Accretion Rate (%)", value=5.0, step=0.5) / 100
        with col2:
            release_pct = st.number_input("Annual Release % (coverage units)", value=20.0, step=1.0) / 100

        if st.button("Generate CSM Schedule"):
            rows_csm = []
            opening = initial_csm
            for yr in range(1, int(coverage_years) + 1):
                interest = opening * interest_rate_csm
                release = (opening + interest) * release_pct
                closing = opening + interest - release
                rows_csm.append({"Year": yr, "Opening CSM ($)": f"{opening:,.0f}", "Interest ($)": f"{interest:,.0f}", "Release to P&L ($)": f"({release:,.0f})", "Closing CSM ($)": f"{closing:,.0f}"})
                opening = closing
            st.dataframe(pd.DataFrame(rows_csm), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Model Selector")
        coverage_period_months = st.number_input("Coverage period (months)", value=12, min_value=1, max_value=600)
        has_participation = st.checkbox("Contract has direct participation features (e.g., unit-linked, with-profits)?")

        if st.button("Determine Appropriate Model"):
            if has_participation:
                st.success("📌 **Variable Fee Approach (VFA)** — Mandatory for contracts with direct participation features.")
            elif coverage_period_months <= 12:
                st.info("📌 **Premium Allocation Approach (PAA)** — Eligible due to coverage period ≤12 months. (General Model also permitted.)")
            else:
                st.warning("📌 **General Model (GMM)** — Default model for longer-duration contracts without direct participation features.")

    with tab4:
        st.header("Visualizations")

        st.subheader("CSM Release Over Coverage Period")
        years_csm = [1, 2, 3, 4, 5]
        csm_balance = [60000, 50400, 42336, 35562, 29872]
        csm_release = [12600, 10584, 8891, 7468, 6277]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=years_csm, y=csm_release, name="CSM Release to P&L", marker_color="#2563EB"))
        fig.add_trace(go.Scatter(x=years_csm, y=csm_balance, name="CSM Balance", line=dict(color="#F59E0B", width=2), mode="lines+markers", yaxis="y2"))
        fig.update_layout(title="CSM Release Pattern Over 5-Year Coverage Period", barmode="group",
                          yaxis=dict(title="Annual Release ($)"), yaxis2=dict(title="CSM Balance ($)", overlaying="y", side="right"), height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Insurance Contract Liability — Building Blocks")
        labels_ifrs17 = ["Insurance Liability", "Fulfilment Cash Flows", "CSM", "PV of Cash Flows", "Risk Adjustment"]
        parents_ifrs17 = ["", "Insurance Liability", "Insurance Liability", "Fulfilment Cash Flows", "Fulfilment Cash Flows"]
        values_ifrs17 = [500000, 440000, 60000, 400000, 40000]
        fig2 = go.Figure(go.Treemap(labels=labels_ifrs17, parents=parents_ifrs17, values=values_ifrs17,
                                     marker_colors=["#1B3A6B","#2563EB","#10B981","#60A5FA","#34D399"]))
        fig2.update_layout(title="Insurance Contract Liability — Building Block Structure", height=420)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. The CSM represents:**")
        q1 = st.radio("", ["The risk margin for uncertainty", "The unearned profit to be recognised as service is provided", "The premium received", "Total claims expected"], key="ifrs17q1")
        if st.button("Check Answer", key="ifrs17c1"):
            if q1 == "The unearned profit to be recognised as service is provided":
                st.success("✅ Correct! The Contractual Service Margin represents UNEARNED PROFIT, deferred and released to P&L systematically over the coverage period as insurance services are provided.")
            else:
                st.error("❌ CSM = unearned profit, NOT the risk margin (that's the Risk Adjustment), premium, or claims estimate.")

        st.markdown("---")
        st.markdown("**2. If the initial CSM calculation would be negative, the contract is:**")
        q2 = st.radio("", ["Not permitted under IFRS 17", "Recognised as a negative CSM asset", "Treated as onerous — loss recognised immediately in P&L", "Deferred until claims are paid"], key="ifrs17q2")
        if st.button("Check Answer", key="ifrs17c2"):
            if q2 == "Treated as onerous — loss recognised immediately in P&L":
                st.success("✅ Correct! CSM CANNOT be negative. If the calculation produces a negative result, the contract is ONEROUS — the loss is recognised IMMEDIATELY in P&L.")
            else:
                st.error("❌ Negative CSM = ONEROUS contract → immediate loss recognition in P&L. CSM itself is never negative.")

        st.markdown("---")
        st.markdown("**3. The Premium Allocation Approach (PAA) is typically used for:**")
        q3 = st.radio("", ["All insurance contracts", "Long-duration life insurance contracts", "Short-duration contracts (coverage period ≤1 year) as a simplification", "Only reinsurance contracts"], key="ifrs17q3")
        if st.button("Check Answer", key="ifrs17c3"):
            if q3 == "Short-duration contracts (coverage period ≤1 year) as a simplification":
                st.success("✅ Correct! PAA is an optional SIMPLIFICATION for short-duration contracts (typically ≤1 year coverage period), similar to old unearned premium reserve accounting.")
            else:
                st.error("❌ PAA is the SIMPLIFIED approach for SHORT-duration contracts — General Model or VFA apply to longer-duration contracts.")

        st.markdown("---")
        st.markdown("**4. The Variable Fee Approach (VFA) is MANDATORY for contracts with:**")
        q4 = st.radio("", ["Fixed premiums", "Direct participation features (e.g., unit-linked)", "Coverage periods under 6 months", "No insurance risk"], key="ifrs17q4")
        if st.button("Check Answer", key="ifrs17c4"):
            if q4 == "Direct participation features (e.g., unit-linked)":
                st.success("✅ Correct! VFA is MANDATORY for contracts with direct participation features — where policyholders share in the performance of underlying items (e.g., unit-linked or with-profits policies).")
            else:
                st.error("❌ VFA is mandatory specifically for DIRECT PARTICIPATION contracts (unit-linked, with-profits), not based on premium structure or coverage period.")

        st.markdown("---")
        st.markdown("**5. Under IFRS 17, insurance revenue presented in P&L:**")
        q5 = st.radio("", ["Equals total premiums received (as under old IFRS 4)", "Excludes investment components and reflects services provided", "Is always zero in the first year", "Includes claims paid"], key="ifrs17q5")
        if st.button("Check Answer", key="ifrs17c5"):
            if q5 == "Excludes investment components and reflects services provided":
                st.success("✅ Correct! IFRS 17 fundamentally changed revenue presentation — insurance revenue reflects SERVICES PROVIDED (not premium cash received) and EXCLUDES investment components, eliminating premium volume distortion.")
            else:
                st.error("❌ IFRS 17 revenue ≠ premiums received. It reflects services provided and excludes investment components — a major change from IFRS 4.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Three Measurement Models
        | Model | Use Case |
        |---|---|
        | General Model (GMM) | Default for most contracts |
        | Premium Allocation Approach (PAA) | Optional simplification, short-duration (≤1yr) |
        | Variable Fee Approach (VFA) | Mandatory for direct participation contracts |

        ### 2. General Model — Four Building Blocks
        ```
        Insurance Liability = Fulfilment Cash Flows + CSM
        Fulfilment Cash Flows = PV of Future Cash Flows + Risk Adjustment
        ```
        - CSM = unearned profit, released over coverage period
        - **CSM cannot be negative** → onerous contract → immediate P&L loss

        ### 3. CSM Mechanics
        - Calibrated to ZERO day-1 profit at initial recognition
        - Accretes interest at locked-in rate (GMM)
        - Released based on coverage units
        - Adjusted for changes relating to FUTURE service; changes relating to PAST/CURRENT service → P&L immediately

        ### 4. Presentation
        - Insurance Revenue (excludes investment components) ≠ premiums received
        - Insurance Service Expenses
        - Insurance Finance Income/Expenses (P&L or OCI policy choice)

        ### 5. Level of Aggregation
        Group by: portfolio → onerous / no significant possibility of onerous / remaining
        NO offsetting losses against profits across groups
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Insurance Liability = Fulfilment Cash Flows (PV + Risk Adj) + CSM
CSM = Unearned profit, NEVER negative (negative → onerous loss immediately)
PAA = simplification for SHORT-duration (≤1yr) contracts
VFA = MANDATORY for direct participation contracts
Insurance Revenue ≠ Premiums Received (excludes investment components)
        """)

        st.success("🎓 **IFRS 17 Complete!** You can now apply the three measurement models, calculate CSM, and identify onerous contracts.")
        st.info("💡 **Next**: IFRS 18 — Presentation and Disclosure in Financial Statements")

if __name__ == "__main__":
    show()