import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("📐 IAS 8: Accounting Policies, Changes in Accounting Estimates and Errors")
    st.markdown("*Master how to select accounting policies, account for changes in estimates, and correct prior-period errors*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Accounting Policies")
        st.markdown("""
        **Accounting policies** are the specific principles, bases, conventions, rules and practices applied by
        an entity in preparing and presenting financial statements.

        **Selection hierarchy (when IFRS does not specifically address a transaction):**
        1. Apply an IFRS standard that deals with a similar and related issue
        2. Refer to the IASB Conceptual Framework definitions and recognition criteria
        3. Consider the most recent pronouncements of other standard-setting bodies using a similar framework
        4. Consider accepted industry practices

        **Consistency:** Once an accounting policy is selected, it must be applied consistently unless:
        - A change is required by a new or revised IFRS
        - The change results in more reliable and relevant information
        """)

        st.subheader("2. Three Types of Changes — Critical Distinction")
        types_data = {
            "Type": [
                "Change in Accounting Policy",
                "Change in Accounting Estimate",
                "Correction of Prior-Period Error"
            ],
            "Definition": [
                "Moving from one acceptable accounting treatment to another (e.g., FIFO to WAC)",
                "Revising an estimate due to new information (e.g., changing useful life of PPE)",
                "Correcting a material omission or misstatement from a prior period"
            ],
            "Accounting Treatment": [
                "RETROSPECTIVE restatement — restate comparative periods; adjust opening retained earnings",
                "PROSPECTIVE — adjust current and future periods only; no restatement",
                "RETROSPECTIVE restatement — restate comparative periods; adjust opening retained earnings"
            ],
            "P&L Impact": [
                "No new P&L impact in current year; prior periods restated",
                "Recognised in P&L in current and future periods",
                "Error correction goes to retained earnings; comparatives restated"
            ]
        }
        st.dataframe(pd.DataFrame(types_data), use_container_width=True, hide_index=True)

        st.subheader("3. Change in Accounting Policy — Detailed Rules")
        st.markdown("""
        **Retrospective application means:**
        - Adjust the opening balance of each affected equity component for the earliest prior period
        - Restate comparative financial statements as if the new policy had always been applied
        - If it is impracticable to apply retrospectively for a specific prior period, apply from the earliest
          period for which retrospective application is practicable

        **Required disclosures:**
        - Nature of the change
        - The reasons why the new policy provides reliable, more relevant information
        - Amount of adjustment for current period and each prior period presented
        - Amount of adjustment relating to periods before those presented (opening retained earnings)
        - If retrospective application is impracticable, the circumstances and how the change was applied

        **Impracticable:** Applying a requirement is impracticable when the entity cannot apply it after making
        every reasonable effort to do so.
        """)

        st.subheader("4. Change in Accounting Estimate — Detailed Rules")
        st.markdown("""
        Changes in estimates arise from new information or developments — they are NOT corrections of errors.

        **Common examples:**
        - Change in useful life of PPE
        - Change in residual value of PPE
        - Change in bad debt provision rate
        - Change in inventory write-down estimates
        - Change in actuarial assumptions (IAS 19)

        **Prospective treatment:**
        - Affect only the current period if the change affects only this period
        - Affect current and future periods if the change affects both
        - NO restatement of prior periods required
        - Disclose the nature and amount of the change (if material)

        **Key distinction:** If it is difficult to distinguish between a policy change and an estimate change,
        treat it as a **change in accounting estimate**.
        """)

        st.subheader("5. Prior-Period Errors")
        st.markdown("""
        **Errors** include mathematical mistakes, mistakes in applying accounting policies, oversights or
        misinterpretations of facts, and fraud.

        **Materiality determines treatment:**
        - **Material prior-period errors** → retrospective restatement (restate comparatives + adjust opening retained earnings)
        - **Immaterial prior-period errors** → correct in current period P&L

        **Retrospective restatement:**
        - Correct by restating the comparative amounts for the prior period(s) presented
        - If the error occurred before the earliest period presented, restate the opening balances

        **Third balance sheet:**
        When there is a retrospective restatement that affects the opening balance sheet, IAS 1 requires
        presentation of **three statements of financial position** (current, prior period, and beginning of prior period).
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Change in Accounting Policy — Revenue Recognition")
        st.markdown("""
        **Scenario:** Entity changes from completed contract method to stage of completion for long-term contracts.

        This is a **change in accounting policy** → **retrospective application**.

        | Year | As Previously Reported Revenue | Restated Revenue | Difference |
        |------|--------------------------------|------------------|------------|
        | 2022 | $4,200k | $4,800k | $600k higher |
        | 2023 (comparative) | $5,100k | $5,500k | $400k higher |
        | Opening retained earnings 2022 | — | Increased by $600k | |

        **Journal entry to restate opening position:**
        Dr Contract Asset (or Revenue) $600k
        Cr Opening Retained Earnings $600k
        """)

        st.subheader("Example 2: Change in Accounting Estimate — Useful Life of Machinery")
        st.markdown("""
        **Scenario:** Equipment cost $500,000, originally estimated useful life 10 years (no residual value).
        After 4 years, new assessment: remaining life is 4 years (not the original remaining 6).

        **Previous depreciation:** $500,000 / 10 = $50,000/year × 4 years = $200,000 accumulated depreciation
        **Carrying amount at start of Year 5:** $500,000 − $200,000 = $300,000

        **New annual depreciation:** $300,000 / 4 remaining years = **$75,000/year** (prospective only)

        | | Before Change | After Change |
        |--|---------------|--------------|
        | Annual Depreciation | $50,000 | $75,000 |
        | Treatment | Prospective from Year 5 | No restatement |
        | P&L Impact | Current year increase of $25,000 | Yes, Year 5 onwards |
        """)

        st.subheader("Example 3: Prior-Period Error — Omitted Expense")
        st.markdown("""
        **Scenario:** In 2024, the entity discovers that a warranty provision of $800,000 was omitted in 2023.
        This is material.

        **Treatment:** Retrospective restatement

        | | 2023 (Restated) | 2023 (Originally Reported) |
        |--|-----------------|---------------------------|
        | Warranty Provision Expense | $800,000 | $0 |
        | Profit Before Tax | Reduced by $800,000 | — |
        | Trade Payables/Provisions | Increased by $800,000 | — |

        **Opening retained earnings for 2024** are restated (reduced by $800,000 after tax).
        Disclosure in 2024 notes: nature of error, period in which it arose, correction amount.
        """)

        st.subheader("Example 4: Distinguishing Policy vs Estimate")
        distinguish_data = {
            "Scenario": [
                "Moving from straight-line to reducing balance depreciation",
                "Changing useful life from 10 to 8 years",
                "Changing from FIFO to WAC for inventory costing",
                "Revising the bad debt provision % from 2% to 3%",
                "Adopting IFRS 16 Leases for the first time"
            ],
            "Type": [
                "Change in Accounting Policy",
                "Change in Accounting Estimate",
                "Change in Accounting Policy",
                "Change in Accounting Estimate",
                "Change in Accounting Policy (new standard)"
            ],
            "Treatment": [
                "Retrospective",
                "Prospective",
                "Retrospective",
                "Prospective",
                "As specified by IFRS 16 transition provisions"
            ]
        }
        st.dataframe(pd.DataFrame(distinguish_data), use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Change Classifier")
        scenario = st.selectbox("Select the scenario:", [
            "Entity switches from straight-line to reducing balance depreciation",
            "Entity increases bad debt provision rate from 2% to 4%",
            "Entity discovers it incorrectly expensed PPE in a prior period",
            "Entity changes useful life estimate of a machine from 10 to 7 years",
            "Entity adopts a new IFRS standard",
            "Entity changes from gross presentation to net presentation of revenues",
            "Entity revises residual value estimate of an asset"
        ])

        policies = {
            "Entity switches from straight-line to reducing balance depreciation": ("Change in Accounting Policy", "Retrospective restatement of comparative periods"),
            "Entity increases bad debt provision rate from 2% to 4%": ("Change in Accounting Estimate", "Prospective — affect current and future periods only"),
            "Entity discovers it incorrectly expensed PPE in a prior period": ("Prior-Period Error", "Retrospective restatement; restate comparatives; third balance sheet may be required"),
            "Entity changes useful life estimate of a machine from 10 to 7 years": ("Change in Accounting Estimate", "Prospective — new depreciation charge from current period onwards"),
            "Entity adopts a new IFRS standard": ("Change in Accounting Policy", "As specified by transition provisions of the new standard"),
            "Entity changes from gross presentation to net presentation of revenues": ("Change in Accounting Policy", "Retrospective restatement of comparative periods"),
            "Entity revises residual value estimate of an asset": ("Change in Accounting Estimate", "Prospective — affects current and future depreciation charge")
        }

        change_type, treatment = policies[scenario]
        if "Policy" in change_type:
            st.warning(f"📘 **{change_type}**\n\nTreatment: {treatment}")
        elif "Estimate" in change_type:
            st.success(f"📗 **{change_type}**\n\nTreatment: {treatment}")
        else:
            st.error(f"📕 **{change_type}**\n\nTreatment: {treatment}")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Depreciation Change Calculator (Estimate Change)")
        col1, col2 = st.columns(2)
        with col1:
            asset_cost = st.number_input("Asset Cost ($)", value=500000, step=10000)
            original_life = st.number_input("Original Useful Life (years)", value=10, min_value=1)
            years_elapsed = st.number_input("Years Already Depreciated", value=4, min_value=0)
            original_residual = st.number_input("Original Residual Value ($)", value=0)
        with col2:
            new_remaining_life = st.number_input("New Remaining Useful Life (years)", value=4, min_value=1)
            new_residual = st.number_input("Revised Residual Value ($)", value=0)

        if st.button("Calculate New Depreciation"):
            old_depr = (asset_cost - original_residual) / original_life
            accumulated = old_depr * years_elapsed
            carrying = asset_cost - accumulated
            new_depr = (carrying - new_residual) / new_remaining_life

            st.markdown(f"""
            | Item | Amount |
            |------|--------|
            | Original annual depreciation | ${old_depr:,.2f} |
            | Accumulated depreciation ({years_elapsed} years) | ${accumulated:,.2f} |
            | Carrying amount at change date | ${carrying:,.2f} |
            | **New annual depreciation (prospective)** | **${new_depr:,.2f}** |
            | Change in annual charge | ${new_depr - old_depr:+,.2f} |
            """)
            st.info("ℹ️ This is a PROSPECTIVE change — no restatement of prior periods required.")

    with tab4:
        st.header("Visualizations")

        st.subheader("Decision Tree: How to Account for a Change")
        st.markdown("""
        ```
        START: Something has changed in accounting
                |
                v
        Is it a correction of a mistake? ──YES──► Prior-Period ERROR
                |                                  → Retrospective Restatement
                NO
                |
                v
        Is it a move between two acceptable ──YES──► Change in ACCOUNTING POLICY
        accounting treatments?                      → Retrospective Application
                |
                NO
                |
                v
        Is it a revision of a judgment or ──YES──► Change in ACCOUNTING ESTIMATE
        estimate based on new information?          → Prospective Application
        ```
        """)

        st.subheader("Impact on Financial Statements")
        categories = ["Change in Accounting Policy", "Change in Accounting Estimate", "Prior Period Error"]
        restate_prior = [1, 0, 1]
        adjust_opening_equity = [1, 0, 1]
        current_pl = [0, 1, 0]
        three_balance_sheets = [0, 0, 1]

        fig = go.Figure()
        fig.add_trace(go.Bar(name="Restate Prior Periods", x=categories, y=restate_prior, marker_color="#2563EB"))
        fig.add_trace(go.Bar(name="Adjust Opening Equity", x=categories, y=adjust_opening_equity, marker_color="#0D7377"))
        fig.add_trace(go.Bar(name="P&L in Current Period", x=categories, y=current_pl, marker_color="#10B981"))
        fig.add_trace(go.Bar(name="3 Balance Sheets Required", x=categories, y=three_balance_sheets, marker_color="#F59E0B"))
        fig.update_layout(barmode="group", title="Accounting Treatment Comparison (1=Yes, 0=No)", height=400, yaxis=dict(range=[0, 1.5]))
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. A company changes its inventory cost formula from FIFO to Weighted Average. This is a:**")
        q1 = st.radio("", [
            "Change in accounting estimate — apply prospectively",
            "Change in accounting policy — apply retrospectively",
            "Prior-period error — restate and disclose",
            "Not permitted under IAS 2"
        ], key="ias8q1")
        if st.button("Check Answer", key="ias8c1"):
            if q1 == "Change in accounting policy — apply retrospectively":
                st.success("✅ Correct! Changing from FIFO to WAC is a change in accounting policy. IAS 8 requires retrospective application — restate comparative periods.")
            else:
                st.error("❌ Incorrect. Changing inventory cost formulas is a change in accounting policy → retrospective restatement required.")

        st.markdown("---")
        st.markdown("**2. A company increases its estimate of bad debt provision from 2% to 5%. This should be treated as:**")
        q2 = st.radio("", [
            "Change in accounting policy → retrospective restatement",
            "Prior-period error → retrospective restatement",
            "Change in accounting estimate → prospective application",
            "No accounting entry required"
        ], key="ias8q2")
        if st.button("Check Answer", key="ias8c2"):
            if q2 == "Change in accounting estimate → prospective application":
                st.success("✅ Correct! Changing a provision percentage is a revision of a judgment — a change in accounting estimate. Apply prospectively. No prior period restatement.")
            else:
                st.error("❌ Incorrect. A change in bad debt provision rate is a change in accounting estimate → prospective only.")

        st.markdown("---")
        st.markdown("**3. When is a third statement of financial position (balance sheet) required under IAS 1?**")
        q3 = st.radio("", [
            "Every reporting period",
            "When the entity changes its year-end",
            "When there is a retrospective restatement of a material prior-period error or change in accounting policy",
            "When the entity acquires a subsidiary"
        ], key="ias8q3")
        if st.button("Check Answer", key="ias8c3"):
            if q3 == "When there is a retrospective restatement of a material prior-period error or change in accounting policy":
                st.success("✅ Correct! A third balance sheet is required when retrospective restatement occurs (error correction or policy change) — showing the balance sheet at the beginning of the comparative period.")
            else:
                st.error("❌ Incorrect. Three balance sheets are required on retrospective restatement (IAS 1.10(f)).")

        st.markdown("---")
        st.markdown("**4. When is it acceptable to apply a change in accounting policy prospectively rather than retrospectively?**")
        q4 = st.radio("", [
            "Always — prospective is the default",
            "When retrospective application is impracticable",
            "When the change was required by a new standard",
            "Prospective application of a policy change is never acceptable"
        ], key="ias8q4")
        if st.button("Check Answer", key="ias8c4"):
            if q4 == "When retrospective application is impracticable":
                st.success("✅ Correct! If it is impracticable to determine the cumulative effect of the change, the entity applies the new policy prospectively from the earliest date practicable.")
            else:
                st.error("❌ Incorrect. Retrospective application is required for policy changes UNLESS it is impracticable, in which case prospective application from the earliest practicable date is used.")

        st.markdown("---")
        st.markdown("**5. If it is difficult to distinguish a change in accounting policy from a change in estimate, IAS 8 requires:**")
        q5 = st.radio("", [
            "Treat it as a change in accounting policy and restate",
            "Treat it as a change in accounting estimate and apply prospectively",
            "Seek guidance from the auditors before any accounting",
            "Disclose in notes but make no accounting entry"
        ], key="ias8q5")
        if st.button("Check Answer", key="ias8c5"):
            if q5 == "Treat it as a change in accounting estimate and apply prospectively":
                st.success("✅ Correct! IAS 8 states that if it is difficult to distinguish between a policy change and an estimate change, treat it as a change in accounting estimate (prospective).")
            else:
                st.error("❌ Incorrect. IAS 8 says: when in doubt, treat as a change in accounting estimate → prospective treatment.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. The Three Types — Critical IAS 8 Distinction

        | Type | Treatment | P&L Impact |
        |------|-----------|------------|
        | **Change in Accounting Policy** | Retrospective restatement | Prior periods restated; no new current-year P&L |
        | **Change in Accounting Estimate** | Prospective | Recognised in current + future periods |
        | **Prior-Period Error** | Retrospective restatement | Prior periods restated; adjust opening equity |

        ### 2. Change in Accounting Policy
        - Retrospective application required
        - Adjust opening retained earnings of earliest period presented
        - Restate all comparative periods
        - Exception: impracticable (very high threshold)
        - Triggers third balance sheet requirement (IAS 1)

        ### 3. Change in Accounting Estimate
        - Apply PROSPECTIVELY — only affects current and future periods
        - No restatement of prior periods
        - Examples: useful life, residual value, bad debt provision rate
        - When in doubt between policy/estimate → treat as estimate

        ### 4. Prior-Period Errors
        - Material errors → retrospective restatement
        - Immaterial errors → correct in current period
        - Requires third balance sheet (IAS 1)
        - Disclose: nature, amount, impact on each affected period

        ### 5. Selecting Accounting Policies
        Hierarchy when IFRS is silent:
        1. Similar IFRS standard
        2. IASB Conceptual Framework
        3. Other standard-setters' pronouncements
        4. Industry practice
        """)

        st.subheader("📌 Memory Aid")
        st.code("""
Policy Change  → RetroPOLICE (restate the past — like policing history)
Estimate Change → ProsPECT (look forward into the future)
Prior Error     → RetroERROR (fix the past mistakes)

The GOLDEN RULE: When unsure policy vs estimate → treat as ESTIMATE (prospective)
        """)

        st.success("🎓 **IAS 8 Complete!** You can now correctly identify and account for policy changes, estimate changes and prior-period errors.")
        st.info("💡 **Next**: IAS 10 — Events After the Reporting Period")

if __name__ == "__main__":
    show()