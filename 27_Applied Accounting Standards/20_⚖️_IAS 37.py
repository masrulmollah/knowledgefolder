import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def show():
    st.title("⚠️ IAS 37: Provisions, Contingent Liabilities and Contingent Assets")
    st.markdown("*Master when to recognise provisions, disclose contingencies, and measure uncertain obligations*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Definitions — The Critical Distinctions")
        defs = pd.DataFrame({
            "Item": ["Provision", "Contingent Liability", "Contingent Asset"],
            "Definition": [
                "A liability of uncertain timing or amount",
                "Possible obligation depending on future events; OR present obligation where outflow is not probable or amount cannot be measured reliably",
                "Possible asset depending on uncertain future events — NOT controlled by entity"
            ],
            "Accounting Treatment": [
                "RECOGNISE in financial statements (Dr Expense / Cr Provision)",
                "DISCLOSE in notes only (if possible obligation) OR do nothing (if remote)",
                "DISCLOSE in notes only if probable; NEVER recognise unless virtually certain"
            ]
        })
        st.dataframe(defs, use_container_width=True, hide_index=True)

        st.subheader("2. Recognition Criteria for a Provision")
        st.markdown("""
        Recognise a provision when ALL THREE conditions are met:
        1. **Present obligation** (legal or constructive) as a result of a past event
        2. **Probable** that an outflow of economic benefits will be required (>50%)
        3. A **reliable estimate** can be made of the amount of the obligation

        **Legal obligation:** arises from a contract, legislation or other legal operation of law
        **Constructive obligation:** arises from established practice, published policy, or specific statement that creates a valid expectation in others
        """)

        st.subheader("3. Measurement of Provisions")
        st.markdown("""
        **Best estimate** = the amount the entity would rationally pay to settle or transfer the obligation.

        | Scenario | Measurement |
        |---|---|
        | Single obligation | Most likely outcome (but consider other possible outcomes) |
        | Large population (e.g., warranties) | **Expected value** = probability-weighted average |
        | Long-term obligation | **Discounted to PV** using pre-tax risk-free rate |

        **Reimbursements (e.g., insurance recoveries):**
        - Recognise separately as an asset ONLY when virtually certain to be received
        - Present separately from provision (cannot net off)
        - In P&L: expense and income may be netted

        **Changes in provisions:** Reviewed at each balance sheet date and adjusted to reflect current best estimate.
        """)

        st.subheader("4. Specific Types of Provisions")
        st.markdown("""
        | Type | Key Rules |
        |---|---|
        | **Restructuring** | Recognise only when a detailed formal plan exists AND entity has raised valid expectation through announcement; cannot include future operating losses |
        | **Onerous contracts** | Recognise when unavoidable costs exceed expected benefits; measure at lower of cost to fulfil or cost to exit |
        | **Warranties** | Expected value approach across entire warranty portfolio |
        | **Decommissioning/restoration** | Recognise when obligation arises (even if asset not yet built); capitalise as part of PPE cost |
        | **Legal claims** | Recognise if probable; disclose if possible; nothing if remote |
        """)

        st.subheader("5. Contingent Liabilities and Assets — Decision Rules")
        st.markdown("""
        **Contingent Liability — three-way treatment:**
        - **Probable outflow** → RECOGNISE as a provision
        - **Possible outflow (not probable)** → DISCLOSE in notes
        - **Remote** → NO disclosure required

        **Contingent Asset:**
        - **Virtually certain** → RECOGNISE as an asset (it becomes certain)
        - **Probable** → DISCLOSE in notes
        - **Possible or remote** → NO disclosure
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Warranty Provision — Expected Value")
        st.markdown("""
        Entity sells 10,000 units. Warranty experience:
        - 70% probability: no defects → cost $0
        - 20% probability: minor defects → cost $50 per unit
        - 10% probability: major defects → cost $200 per unit

        **Expected cost per unit:**
        = (70% × $0) + (20% × $50) + (10% × $200)
        = $0 + $10 + $20 = **$30 per unit**

        **Total warranty provision = 10,000 × $30 = $300,000**

        ```
        Dr  Warranty Expense     $300,000
            Cr  Warranty Provision    $300,000
        ```
        """)

        st.subheader("Example 2: Legal Claim — Provision vs Contingency")
        legal_data = pd.DataFrame({
            "Scenario": [
                "Court verdict received — entity must pay $500k",
                "Legal case ongoing — lawyers say 75% chance of losing, estimated $500k",
                "Legal case — lawyers say 30% chance of losing",
                "Frivolous claim — 5% chance of any outflow"
            ],
            "Treatment": ["Provision $500k", "Provision $500k (probable)", "Disclose contingent liability in notes", "No disclosure required (remote)"],
            "P&L Impact": ["Dr Expense $500k", "Dr Expense $500k", "None — notes only", "None"]
        })
        st.dataframe(legal_data, use_container_width=True, hide_index=True)

        st.subheader("Example 3: Restructuring Provision")
        st.markdown("""
        **Board approves restructuring plan on 20 December 2024:**
        - Plan affects 50 employees across 3 divisions
        - Estimated redundancy cost: $2,000,000
        - Employees notified before year-end 31 December 2024

        **Is a provision required at 31 Dec 2024?**
        ✅ YES — detailed formal plan exists AND employees have been notified → constructive obligation exists.

        **Provision = $2,000,000**

        ⚠️ Note: Cannot include future operating losses in restructuring provision.
        Cannot include costs to retrain retained staff.
        Cannot include relocation of ongoing activities (only closure/exit costs).
        """)

        st.subheader("Example 4: Decommissioning Provision")
        st.markdown("""
        Entity installs an oil rig. Estimated decommissioning cost in 20 years = $5,000,000.
        Discount rate = 5%.

        **PV of decommissioning obligation = $5,000,000 / (1.05)²⁰ = $1,884,447**

        **Journal at installation:**
        ```
        Dr  PPE (decommissioning asset)    $1,884,447
            Cr  Decommissioning Provision      $1,884,447
        ```

        Each year: unwinding of discount → interest expense in P&L
        Year 1: $1,884,447 × 5% = $94,222 → Dr Finance Cost / Cr Provision
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Provision Recognition Checker")
        col1, col2 = st.columns(2)
        with col1:
            past_event = st.checkbox("Past obligating event has occurred?")
            present_obligation = st.checkbox("Present obligation exists (legal or constructive)?")
            probable_outflow = st.checkbox("Outflow of economic benefits is probable (>50%)?")
            reliable_estimate = st.checkbox("Reliable estimate of amount can be made?")
        with col2:
            if all([past_event, present_obligation, probable_outflow, reliable_estimate]):
                st.success("✅ **RECOGNISE A PROVISION** — All three IAS 37 criteria are met.")
            elif present_obligation and not probable_outflow:
                st.warning("📋 **DISCLOSE AS CONTINGENT LIABILITY** — Obligation exists but outflow not probable.")
            elif not present_obligation:
                st.info("📋 **DISCLOSE OR IGNORE** — No present obligation. Disclose if possible; ignore if remote.")
            else:
                missing = []
                if not past_event: missing.append("Past event")
                if not probable_outflow: missing.append("Probable outflow")
                if not reliable_estimate: missing.append("Reliable estimate")
                st.warning(f"📋 Cannot recognise provision — missing: {', '.join(missing)}")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Warranty Provision Calculator (Expected Value)")
        units = st.number_input("Units sold under warranty", value=10000, step=100)
        st.markdown("Enter probability and cost for each defect scenario:")
        col1, col2, col3 = st.columns(3)
        with col1:
            p_none = st.number_input("Probability: No defect (%)", value=70.0, step=5.0)
            c_none = st.number_input("Cost per unit: No defect ($)", value=0.0)
        with col2:
            p_minor = st.number_input("Probability: Minor defect (%)", value=20.0, step=5.0)
            c_minor = st.number_input("Cost per unit: Minor defect ($)", value=50.0)
        with col3:
            p_major = st.number_input("Probability: Major defect (%)", value=10.0, step=5.0)
            c_major = st.number_input("Cost per unit: Major defect ($)", value=200.0)

        if st.button("Calculate Warranty Provision"):
            total_prob = p_none + p_minor + p_major
            if abs(total_prob - 100) > 0.1:
                st.error(f"⚠️ Probabilities must sum to 100%. Current total: {total_prob:.1f}%")
            else:
                ev_per_unit = (p_none/100)*c_none + (p_minor/100)*c_minor + (p_major/100)*c_major
                total_prov = ev_per_unit * units
                st.markdown(f"""
                | Scenario | Probability | Cost/Unit | Weighted Cost |
                |---|---|---|---|
                | No defect | {p_none}% | ${c_none:,.2f} | ${p_none/100*c_none:,.2f} |
                | Minor defect | {p_minor}% | ${c_minor:,.2f} | ${p_minor/100*c_minor:,.2f} |
                | Major defect | {p_major}% | ${c_major:,.2f} | ${p_major/100*c_major:,.2f} |
                | **Expected cost per unit** | | | **${ev_per_unit:,.2f}** |
                | **Total warranty provision** ({units:,} units) | | | **${total_prov:,.0f}** |
                """)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Decommissioning Provision Calculator")
        col1, col2 = st.columns(2)
        with col1:
            future_cost = st.number_input("Estimated decommissioning cost ($)", value=5000000, step=100000)
            years_ahead = st.number_input("Years until decommissioning", value=20, min_value=1, max_value=50)
            disc_rate = st.number_input("Risk-free discount rate (%)", value=5.0, step=0.25) / 100
        with col2:
            pv_decomm = future_cost / (1 + disc_rate)**years_ahead
            yr1_unwind = pv_decomm * disc_rate
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | Future decommissioning cost | ${future_cost:,.0f} |
            | Discount factor | {1/(1+disc_rate)**years_ahead:.4f} |
            | **PV of provision (add to PPE cost)** | **${pv_decomm:,.0f}** |
            | Year 1 unwinding of discount (finance cost) | ${yr1_unwind:,.0f} |
            """)

    with tab4:
        st.header("Visualizations")

        st.subheader("Provision vs Contingent Liability vs Contingent Asset — Decision Framework")
        fig = go.Figure()
        categories = ["Probable\n(>50%)", "Possible\n(not probable)", "Remote\n(<5%)"]
        liability_action = ["RECOGNISE\nas Provision", "DISCLOSE\nin Notes", "NO ACTION\nRequired"]
        asset_action = ["DISCLOSE\nin Notes", "NO ACTION", "NO ACTION"]
        colors_l = ["#F87171", "#F59E0B", "#34D399"]
        colors_a = ["#10B981", "#D1D5DB", "#D1D5DB"]
        fig.add_trace(go.Bar(x=categories, y=[3, 2, 1], name="Liability Treatment", marker_color=colors_l,
                             text=liability_action, textposition="inside", textfont=dict(color="white", size=11)))
        fig.add_trace(go.Bar(x=categories, y=[3, 2, 1], name="Asset Treatment", marker_color=colors_a,
                             text=asset_action, textposition="inside", textfont=dict(color="white", size=11),
                             visible=False))
        fig.update_layout(title="IAS 37 — Treatment by Probability", yaxis=dict(visible=False), height=350)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Decommissioning Provision — PV Over Time")
        base_pv = 1884447
        disc = 0.05
        years_range = list(range(0, 21))
        provision_balance = [base_pv * (1.05)**y for y in years_range]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=years_range, y=provision_balance, name="Provision Balance",
                                   line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig2.add_hline(y=5000000, line_dash="dash", line_color="#F87171", annotation_text="Final Settlement $5M")
        fig2.update_layout(title="Decommissioning Provision Growth (Unwinding of Discount at 5%)", xaxis_title="Year", yaxis_title="Provision Balance ($)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. A provision is recognised when:**")
        q1 = st.radio("", [
            "Management decides it is prudent to set money aside",
            "A past event creates a present obligation, outflow is probable, and a reliable estimate can be made",
            "A legal case has been filed against the entity",
            "The entity has a possible obligation depending on future events"
        ], key="ias37q1")
        if st.button("Check Answer", key="ias37c1"):
            if q1 == "A past event creates a present obligation, outflow is probable, and a reliable estimate can be made":
                st.success("✅ Correct! All three criteria must be met: (1) past obligating event → present obligation, (2) probable outflow, (3) reliable estimate.")
            else:
                st.error("❌ Three conditions: past event → present obligation, probable outflow (>50%), and reliable estimate — ALL must be met.")

        st.markdown("---")
        st.markdown("**2. A restructuring provision can be recognised when:**")
        q2 = st.radio("", [
            "Board internally approves the plan (no announcement yet)",
            "A detailed formal plan exists AND the entity has raised a valid expectation by announcement",
            "The restructuring begins to be implemented",
            "Future operating losses from the restructuring are estimated"
        ], key="ias37q2")
        if st.button("Check Answer", key="ias37c2"):
            if q2 == "A detailed formal plan exists AND the entity has raised a valid expectation by announcement":
                st.success("✅ Correct! Both conditions are needed: a detailed formal plan AND a valid expectation raised in affected parties through announcement or commencement.")
            else:
                st.error("❌ Restructuring provision requires: (1) detailed formal plan + (2) valid expectation raised (e.g., announcement to employees).")

        st.markdown("---")
        st.markdown("**3. A contingent asset that is PROBABLE should be:**")
        q3 = st.radio("", [
            "Recognised as an asset immediately",
            "Disclosed in the notes to the financial statements",
            "Neither recognised nor disclosed",
            "Netted against any related provision"
        ], key="ias37q3")
        if st.button("Check Answer", key="ias37c3"):
            if q3 == "Disclosed in the notes to the financial statements":
                st.success("✅ Correct! A probable contingent asset is DISCLOSED in notes. Only when inflow is virtually certain does recognition occur (it then becomes a real asset, not contingent).")
            else:
                st.error("❌ Probable contingent asset → DISCLOSE only. Recognise only when virtually certain.")

        st.markdown("---")
        st.markdown("**4. An onerous contract provision is measured at:**")
        q4 = st.radio("", [
            "The full contract value",
            "The lower of: cost to fulfil the contract OR cost to exit/cancel",
            "The higher of: cost to fulfil OR cost to exit",
            "Only the penalties for early termination"
        ], key="ias37q4")
        if st.button("Check Answer", key="ias37c4"):
            if q4 == "The lower of: cost to fulfil the contract OR cost to exit/cancel":
                st.success("✅ Correct! Onerous contract provision = lower of (cost to fulfil) or (cost to exit/cancel including penalties). The entity would rationally choose whichever is cheaper.")
            else:
                st.error("❌ Onerous contract = LOWER of cost to fulfil or cost to exit. The entity would choose the cheaper option.")

        st.markdown("---")
        st.markdown("**5. Insurance reimbursements expected from a provision event should be:**")
        q5 = st.radio("", [
            "Netted against the provision immediately",
            "Recognised as an asset only when virtually certain; presented separately",
            "Recognised when claimed from insurer",
            "Ignored until cash is received"
        ], key="ias37q5")
        if st.button("Check Answer", key="ias37c5"):
            if q5 == "Recognised as an asset only when virtually certain; presented separately":
                st.success("✅ Correct! Reimbursements are recognised as a separate asset only when VIRTUALLY CERTAIN. The provision and reimbursement asset are presented gross (separately) on the balance sheet.")
            else:
                st.error("❌ Reimbursements: recognise SEPARATELY as an asset only when virtually certain. Present gross — not netted against the provision.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Three-Way Decision Framework

        | Situation | Treatment |
        |---|---|
        | Present obligation + probable outflow + reliable estimate | **RECOGNISE provision** |
        | Possible obligation OR obligation but not probable/not measurable | **DISCLOSE contingent liability** |
        | Remote possibility | **NO action** |
        | Probable contingent asset | **DISCLOSE** |
        | Virtually certain contingent asset | **RECOGNISE** as asset |

        ### 2. Provision Recognition — 3 Conditions (ALL required)
        1. Past obligating event → **present obligation** (legal or constructive)
        2. Outflow of resources is **probable** (>50%)
        3. **Reliable estimate** can be made

        ### 3. Measurement
        ```
        Single obligation → most likely outcome
        Large population (warranties) → expected value (probability-weighted)
        Long-term → discount to PV using pre-tax risk-free rate
        ```

        ### 4. Key Specific Provisions
        - **Restructuring:** Formal plan + valid expectation raised → no future operating losses
        - **Onerous contracts:** Lower of cost to fulfil vs cost to exit
        - **Decommissioning:** Recognise when obligation arises → capitalise in PPE cost
        - **Reimbursements:** Separate asset, only when virtually certain

        ### 5. Cannot Recognise Provisions For
        - Future operating losses
        - General reserves or "rainy day" provisions
        - Self-insurance reserves (unless legal/constructive obligation)
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
3 Conditions to RECOGNISE: Past event → obligation + Probable + Reliable estimate
Contingent liability (possible) → DISCLOSE only
Contingent asset (probable) → DISCLOSE; (virtually certain) → RECOGNISE
Restructuring: Formal plan + Announcement → NO future operating losses
Onerous contract: Lower of (fulfil cost) vs (exit cost)
Reimbursements: SEPARATE asset, only VIRTUALLY CERTAIN
        """)

        st.success("🎓 **IAS 37 Complete!** You can now distinguish provisions from contingencies, apply recognition criteria, and measure uncertain obligations correctly.")
        st.info("💡 **Next**: IAS 38 — Intangible Assets")

if __name__ == "__main__":
    show()