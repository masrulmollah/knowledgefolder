import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏛️ IFRS 10: Consolidated Financial Statements")
    st.markdown("*Master the control model, consolidation procedures and non-controlling interests*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and the Single Control Model")
        st.markdown("""
        **IFRS 10** establishes a SINGLE control model applicable to ALL types of entities, replacing the previous mixed model (risks-and-rewards for SPEs, voting rights for others).

        A parent **must consolidate** all entities it controls — there is no choice.
        """)

        st.subheader("2. Definition of Control — Three Elements (ALL must be present)")
        st.markdown("""
        An investor **controls** an investee when it has ALL THREE of:

        1. **Power** — existing rights that give the current ability to direct the relevant activities (the activities that significantly affect the investee's returns)
        2. **Exposure to variable returns** — rights to variable returns from involvement with the investee (can be positive, negative, or both)
        3. **Ability to use power to affect returns** — a link between power and returns (not merely an agent)

        **Power typically arises from:**
        - Voting rights (>50% ownership is the most common indicator, but not always determinative)
        - Potential voting rights (options, convertible instruments) if substantive
        - Contractual arrangements
        - De facto control (large minority stake combined with dispersed other shareholders)
        """)

        st.subheader("3. Voting Rights and De Facto Control")
        st.markdown("""
        | Ownership | Typical Control Conclusion |
        |---|---|
        | >50% voting rights | Control presumed (rebuttable) |
        | Exactly 50% | Joint control likely (IFRS 11) unless tie-breaker exists |
        | <50% but largest shareholder, others dispersed | **De facto control** possible — assess voting patterns at recent shareholder meetings |
        | <50% with substantive potential voting rights (currently exercisable options) | May still have control if rights are substantive |

        **Substantive rights** must be currently exercisable and provide practical ability to exercise — not merely protective rights.
        """)

        st.subheader("4. Principal vs Agent Assessment")
        st.markdown("""
        When an investor has decision-making power, assess whether it is acting as a **principal** (controls) or an **agent** (does not control) for other parties.

        **Factors to consider:**
        - Scope of decision-making authority
        - Rights held by other parties (removal rights, other substantive rights)
        - Remuneration the decision-maker is entitled to
        - Exposure to variability of returns from other interests held

        A **fund manager** is typically an agent (does not consolidate the fund) unless it also holds a substantial direct investment exposing it to variable returns.
        """)

        st.subheader("5. Consolidation Procedures")
        st.markdown("""
        **Steps:**
        1. Combine like items of assets, liabilities, equity, income, expenses, cash flows of parent and subsidiaries LINE BY LINE
        2. **Eliminate** the carrying amount of the parent's investment in each subsidiary against the parent's share of equity
        3. **Eliminate** intragroup assets, liabilities, equity, income, expenses, and cash flows IN FULL (100%, regardless of NCI%)
        4. Recognise **Non-Controlling Interest (NCI)** for the portion of equity not attributable to the parent

        **Uniform accounting policies:** Adjust subsidiary's financial statements to align with group accounting policies before consolidating.

        **Same reporting date:** Use the same reporting date for parent and subsidiaries; if impractical, use the most recent subsidiary financials adjusted for significant transactions, with no more than 3 months difference.
        """)

        st.subheader("6. Loss of Control")
        st.markdown("""
        When a parent loses control of a subsidiary:
        - **Derecognise** the subsidiary's assets/liabilities and any NCI at their carrying amounts
        - Recognise the **fair value of consideration received** (if any)
        - Recognise any **retained investment** at fair value
        - Recognise the resulting **gain or loss in P&L**
        - Reclassify amounts previously in OCI per the same basis as if the parent had directly disposed of the assets/liabilities (e.g., recycle FX translation reserve)
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Control Assessment — Majority Voting Rights")
        st.markdown("""
        Parent owns **65%** of Subsidiary's voting shares. No special arrangements exist.

        **Assessment:**
        - Power: ✅ Majority voting rights give power over relevant activities
        - Variable returns: ✅ Entitled to 65% of dividends/profits
        - Link: ✅ Can use voting power to influence dividend policy and operations

        **Conclusion: CONTROL EXISTS → Consolidate**
        """)

        st.subheader("Example 2: De Facto Control with Minority Stake")
        st.markdown("""
        Investor owns **40%** of voting shares. Remaining 60% is held by thousands of dispersed small shareholders, none owning more than 1%, who rarely attend meetings.

        **Historical voting pattern:** At the last 5 shareholder meetings, the investor's 40% has been sufficient to pass all resolutions due to low attendance by other shareholders.

        **Conclusion: DE FACTO CONTROL likely exists → Consolidate** (must assess based on facts and circumstances)
        """)

        st.subheader("Example 3: Consolidation Worksheet — Elimination Entries")
        st.markdown("""
        **Parent acquires 80% of Subsidiary for $4,000,000. Subsidiary's net assets at acquisition = $4,500,000.**

        | | Parent (Standalone) | Subsidiary (100%) | Adjustments | Consolidated |
        |---|---|---|---|---|
        | Investment in Subsidiary | $4,000,000 | — | ($4,000,000) elimination | $0 |
        | Net Assets of Subsidiary | — | $4,500,000 | Consolidate 100% | $4,500,000 |
        | Goodwill | — | — | +$400,000* | $400,000 |
        | NCI (20%) | — | — | ($900,000)** | ($900,000) |

        *Goodwill (full method) = $4,000,000 + FV of NCI ($950,000) − $4,500,000 = $450,000 (simplified for illustration)
        **NCI = 20% × $4,500,000 = $900,000 (partial method, illustrative)

        Intragroup balances (e.g., parent's receivable from subsidiary) are eliminated 100% regardless of NCI%.
        """)

        st.subheader("Example 4: NCI Share of Profit")
        st.markdown("""
        Subsidiary (80% owned) reports profit of **$1,000,000** for the year.

        | | Amount |
        |---|---|
        | Total subsidiary profit | $1,000,000 |
        | Attributable to Parent (80%) | $800,000 |
        | **Attributable to NCI (20%)** | **$200,000** |

        Presented in the consolidated P&L as "Profit attributable to: Owners of the parent $X / Non-controlling interests $200,000"
        """)

        st.subheader("Example 5: Loss of Control — Disposal of Subsidiary")
        st.markdown("""
        Parent sells its 80% stake in Subsidiary for $5,500,000 cash, losing control.
        - Carrying amount of subsidiary's net assets at disposal: $5,000,000
        - NCI carrying amount: $1,000,000
        - Cumulative FX translation reserve relating to subsidiary: $200,000 (gain, in OCI)

        **Calculation of gain on loss of control:**
        | | $ |
        |---|---|
        | Consideration received | 5,500,000 |
        | Less: Net assets derecognised | (5,000,000) |
        | Less: NCI derecognised | (1,000,000) |
        | Add: Reclassify FX reserve from OCI | 200,000 |
        | **Loss on disposal → P&L** | **(300,000)** |
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Control Assessment Checker")
        col1, col2 = st.columns(2)
        with col1:
            voting_pct = st.number_input("Voting rights held (%)", value=65.0, step=5.0)
            other_dispersed = st.checkbox("Remaining shares widely dispersed among small holders?")
            historical_pattern = st.checkbox("Historical voting pattern shows sufficient control at meetings?")
            potential_voting = st.checkbox("Substantive potential voting rights held (e.g., currently exercisable options)?")
        with col2:
            if voting_pct > 50:
                st.success("✅ **CONTROL** — Majority voting rights (>50%) → presumption of control (rebuttable)")
            elif voting_pct == 50:
                st.warning("⚠️ **POSSIBLE JOINT CONTROL** — Exactly 50% suggests joint control (assess under IFRS 11) unless a tie-breaker mechanism exists")
            elif other_dispersed and historical_pattern:
                st.success(f"✅ **DE FACTO CONTROL** likely — {voting_pct}% combined with dispersed shareholding and historical voting pattern")
            elif potential_voting:
                st.info(f"📊 **ASSESS FURTHER** — {voting_pct}% direct + substantive potential voting rights may give control")
            else:
                st.error(f"❌ **NO CONTROL** — {voting_pct}% voting rights insufficient without other supporting factors. Consider IAS 28 (associate) if significant influence exists (20-50%).")

        st.markdown("---")
        st.subheader("🔧 Tool 2: NCI Profit Allocation Calculator")
        sub_profit = st.number_input("Subsidiary's Total Profit ($)", value=1000000, step=10000)
        nci_pct = st.number_input("NCI Ownership %", value=20.0, step=1.0) / 100
        if st.button("Allocate Profit"):
            parent_share = sub_profit * (1 - nci_pct)
            nci_share = sub_profit * nci_pct
            st.markdown(f"""
            | Allocation | Amount |
            |---|---|
            | Attributable to Parent ({(1-nci_pct)*100:.0f}%) | ${parent_share:,.0f} |
            | **Attributable to NCI ({nci_pct*100:.0f}%)** | **${nci_share:,.0f}** |
            """)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Loss of Control Gain/Loss Calculator")
        col1, col2 = st.columns(2)
        with col1:
            consideration_lc = st.number_input("Consideration Received ($)", value=5500000, step=10000)
            net_assets_lc = st.number_input("Net Assets Derecognised ($)", value=5000000, step=10000)
        with col2:
            nci_lc = st.number_input("NCI Derecognised ($)", value=1000000, step=10000)
            oci_reclass = st.number_input("OCI Reclassified (e.g., FX reserve, + for gain) ($)", value=200000, step=10000)

        if st.button("Calculate Gain/Loss on Loss of Control"):
            gain_loss = consideration_lc - net_assets_lc - nci_lc + oci_reclass
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | Consideration received | ${consideration_lc:,.0f} |
            | Less: Net assets derecognised | (${net_assets_lc:,.0f}) |
            | Less: NCI derecognised | (${nci_lc:,.0f}) |
            | Add: OCI reclassified | ${oci_reclass:,.0f} |
            | **Gain/(Loss) on Loss of Control → P&L** | **${gain_loss:,.0f}** |
            """)
            if gain_loss >= 0:
                st.success(f"✅ Gain of ${gain_loss:,.0f} recognised in P&L")
            else:
                st.error(f"⚠️ Loss of ${abs(gain_loss):,.0f} recognised in P&L")

    with tab4:
        st.header("Visualizations")

        st.subheader("Control Assessment Framework")
        st.markdown("""
        ```
                        CONTROL = Power + Exposure to Variable Returns + Link
                                            |
                ┌───────────────────────────┼────────────────────────┐
            Power?                  Variable Returns?            Use Power to
                |                           |                     Affect Returns?
        Voting rights (>50%)         Dividends, fees,           Principal vs
        Potential voting rights      residual interests,        Agent assessment
        Contractual arrangements     losses                          |
        De facto control                                       Decision-maker
                                                                 acting for self
                                                                 (principal) or
                                                                 others (agent)?
        ```
        """)

        st.subheader("Consolidated vs Parent-Only Financial Statements")
        categories_c = ["Total Assets", "Total Liabilities", "Equity (Parent)", "NCI"]
        parent_only = [10000, 6000, 4000, 0]
        consolidated = [16000, 9500, 5600, 900]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=categories_c, y=parent_only, name="Parent Only", marker_color="#94A3B8"))
        fig.add_trace(go.Bar(x=categories_c, y=consolidated, name="Consolidated Group", marker_color="#2563EB"))
        fig.update_layout(barmode="group", title="Parent-Only vs Consolidated Financial Position ($000)", height=400)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IFRS 10, control requires ALL of the following EXCEPT:**")
        q1 = st.radio("", ["Power over the investee", "Exposure to variable returns", "Ability to use power to affect returns", "Majority board representation"], key="ifrs10q1")
        if st.button("Check Answer", key="ifrs10c1"):
            if q1 == "Majority board representation":
                st.success("✅ Correct! Control requires power + exposure to variable returns + ability to use power to affect returns. Board representation is just ONE possible indicator of power, not a separate required element.")
            else:
                st.error("❌ The three REQUIRED elements are: power, exposure to variable returns, and the link between them. Board representation is just an indicator, not a separate requirement.")

        st.markdown("---")
        st.markdown("**2. De facto control may exist when an investor holds less than 50% of voting rights if:**")
        q2 = st.radio("", ["The investor is the largest customer of the investee", "The investor holds a large minority stake and other shares are widely dispersed with low attendance at meetings", "The investee operates in the same industry", "The investor has provided a loan to the investee"], key="ifrs10q2")
        if st.button("Check Answer", key="ifrs10c2"):
            if q2 == "The investor holds a large minority stake and other shares are widely dispersed with low attendance at meetings":
                st.success("✅ Correct! De facto control can arise from a large minority stake combined with dispersed remaining ownership and historical voting patterns showing the investor effectively controls outcomes.")
            else:
                st.error("❌ De facto control requires assessing the relative size of the holding plus dispersion of other holders and voting patterns — not customer relationships or loans.")

        st.markdown("---")
        st.markdown("**3. When consolidating, intragroup transactions are eliminated:**")
        q3 = st.radio("", ["In proportion to the parent's ownership percentage", "100% regardless of NCI percentage", "Only if material", "Only for intragroup sales, not loans"], key="ifrs10q3")
        if st.button("Check Answer", key="ifrs10c3"):
            if q3 == "100% regardless of NCI percentage":
                st.success("✅ Correct! IFRS 10 requires FULL elimination (100%) of intragroup balances and transactions, regardless of the NCI percentage — the group is treated as a single economic entity.")
            else:
                st.error("❌ Intragroup eliminations are always 100% — NOT proportional to ownership percentage.")

        st.markdown("---")
        st.markdown("**4. A fund manager who manages assets on behalf of investors, with limited exposure to variable returns, is typically considered:**")
        q4 = st.radio("", ["A principal who must consolidate the fund", "An agent who does not consolidate the fund", "Always required to consolidate regardless of returns", "Exempt from any assessment"], key="ifrs10q4")
        if st.button("Check Answer", key="ifrs10c4"):
            if q4 == "An agent who does not consolidate the fund":
                st.success("✅ Correct! A fund manager acting primarily for the benefit of investors (limited own exposure to variable returns, market-based fees) is typically an AGENT and does not consolidate.")
            else:
                st.error("❌ Fund managers with limited own variable return exposure are typically AGENTS — they do not consolidate the fund they manage.")

        st.markdown("---")
        st.markdown("**5. On loss of control of a subsidiary, any retained investment is measured at:**")
        q5 = st.radio("", ["Original cost", "Carrying amount immediately before loss of control", "Fair value at the date control is lost", "Zero"], key="ifrs10q5")
        if st.button("Check Answer", key="ifrs10c5"):
            if q5 == "Fair value at the date control is lost":
                st.success("✅ Correct! Any retained investment is remeasured to FAIR VALUE at the date control is lost — this fair value becomes the new cost basis for subsequent accounting (e.g., as an associate under IAS 28).")
            else:
                st.error("❌ Retained investments are remeasured to FAIR VALUE at the date control is lost, with any gain/loss recognised in P&L.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. The Control Model — Three Required Elements
        1. **Power** over the investee
        2. **Exposure** to variable returns
        3. **Ability to use power** to affect those returns

        ### 2. Sources of Power
        - Majority voting rights (>50%) — presumption of control
        - Substantive potential voting rights
        - Contractual arrangements
        - **De facto control** (large minority + dispersed others)

        ### 3. Consolidation Procedures
        ```
        1. Combine line-by-line (100% of subsidiary, regardless of NCI%)
        2. Eliminate investment in subsidiary against parent's share of equity
        3. Eliminate ALL intragroup transactions/balances (100%)
        4. Recognise NCI for the non-parent portion of equity
        ```

        ### 4. Principal vs Agent
        - Principal → consolidates
        - Agent (e.g., typical fund manager) → does NOT consolidate

        ### 5. Loss of Control
        ```
        Gain/Loss = Consideration Received
                  − Net Assets Derecognised
                  − NCI Derecognised
                  + OCI Reclassification (e.g., FX reserve)
                  → Recognised in P&L
        Retained investment → remeasured to FAIR VALUE
        ```
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Control = Power + Variable Returns Exposure + Link between them
>50% voting → presumption of control (rebuttable)
De facto control → large minority + dispersed shareholders + voting pattern
Intragroup eliminations → ALWAYS 100% (never proportional)
Agent (e.g., fund manager) → does NOT consolidate
Loss of control → retained investment remeasured to FV; gain/loss to P&L
        """)

        st.success("🎓 **IFRS 10 Complete!** You can now assess control, perform consolidation procedures, and account for loss of control scenarios.")
        st.info("💡 **Next**: IFRS 11 — Joint Arrangements")

if __name__ == "__main__":
    show()