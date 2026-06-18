import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("📢 IFRS 12: Disclosure of Interests in Other Entities")
    st.markdown("*Master the disclosure requirements for subsidiaries, joint arrangements, associates and structured entities*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Scope")
        st.markdown("""
        **IFRS 12** consolidates ALL disclosure requirements relating to an entity's interests in:
        - **Subsidiaries** (IFRS 10)
        - **Joint arrangements** (IFRS 11) — joint operations and joint ventures
        - **Associates** (IAS 28)
        - **Unconsolidated structured entities**

        **Objective:** Enable users to evaluate:
        1. The **nature of, and risks associated with**, interests in other entities
        2. The **effects** of those interests on financial position, performance and cash flows
        """)

        st.subheader("2. Significant Judgements in Determining Control/Influence")
        st.markdown("""
        Disclose significant judgements made in determining:
        - Whether the entity has **control** of another entity (especially when control is not based on majority voting rights — e.g., de facto control)
        - Whether the entity has **joint control** or **significant influence**
        - The **type of joint arrangement** (joint operation vs joint venture) when structured through a separate vehicle

        These disclosures are critical when the conclusion is NOT obvious from simple majority ownership.
        """)

        st.subheader("3. Disclosures for Subsidiaries")
        st.markdown("""
        - Composition of the group
        - Interest that NCI have in the group's activities and cash flows
        - For each subsidiary with MATERIAL NCI:
          - Name, principal place of business
          - Proportion of ownership/voting rights held by NCI
          - Profit/loss allocated to NCI
          - Accumulated NCI at the end of the period
          - Summarised financial information (assets, liabilities, revenue, profit, cash flows)
        - **Nature and extent of significant restrictions** on the parent's ability to access group assets (e.g., regulatory restrictions on transferring cash out of a subsidiary)
        - Nature of risks from **consolidated structured entities** (e.g., sponsored investment vehicles)
        """)

        st.subheader("4. Disclosures for Joint Arrangements and Associates")
        st.markdown("""
        For each **individually material** joint venture or associate:
        - Name, principal place of business, proportion of ownership
        - Whether measured using equity method or fair value
        - Summarised financial information (assets, liabilities, revenue, profit/loss)
        - Fair value of investment (if quoted price available)

        For joint ventures and associates **in aggregate** (immaterial individually):
        - Aggregate carrying amount of investments
        - Aggregate amounts of share of profit/loss, OCI, and total comprehensive income

        **Risks:** Disclose nature/extent of significant restrictions on JV/associate's ability to transfer funds to the entity (dividends, loan repayments).
        """)

        st.subheader("5. Disclosures for Unconsolidated Structured Entities")
        st.markdown("""
        A **structured entity** is designed so that voting rights are NOT the dominant factor in deciding who controls it (e.g., securitisation vehicles, asset-backed financing entities).

        For UNCONSOLIDATED structured entities the reporting entity has an interest in (but does NOT control):
        - Nature and extent of interests held
        - Nature of risks (including maximum exposure to loss)
        - Information about any support provided (financial or otherwise) without contractual obligation to do so, including reasons for providing such support

        This disclosure is critical for identifying "shadow" exposures not visible on the balance sheet.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Material NCI Disclosure")
        st.markdown("""
        **Subsidiary X — 70% owned by Parent (30% NCI):**

        | Disclosure Item | Value |
        |---|---|
        | Proportion of ownership/voting rights held by NCI | 30% |
        | Profit allocated to NCI for the year | $1,200,000 |
        | Accumulated NCI at year-end | $8,500,000 |
        | Dividends paid to NCI | $360,000 |

        **Summarised financial information of Subsidiary X (100%):**
        | | $000 |
        |---|---|
        | Current assets | 15,000 |
        | Non-current assets | 25,000 |
        | Current liabilities | (8,000) |
        | Non-current liabilities | (4,000) |
        | Revenue | 32,000 |
        | Profit for the year | 4,000 |
        """)

        st.subheader("Example 2: Significant Judgement — De Facto Control")
        st.markdown("""
        *Extract from Notes:*

        *"The Group holds 42% of the voting rights of XYZ Corp. Management has concluded that the Group has control over XYZ Corp because the remaining 58% is held by numerous unrelated shareholders, none holding more than 3%, and historical attendance at general meetings has been below 25%. As a result, the Group's 42% holding has been sufficient to direct the relevant activities of XYZ Corp at recent shareholder meetings. XYZ Corp is consolidated as a subsidiary."*

        This disclosure is REQUIRED because the conclusion is not obvious from ownership percentage alone.
        """)

        st.subheader("Example 3: Restrictions on Accessing Group Assets")
        st.markdown("""
        *Extract from Notes:*

        *"The Group's subsidiary in Country Z is subject to local exchange control regulations restricting the transfer of cash out of the country without central bank approval. At 31 December 2024, cash and cash equivalents of $4.2 million held by this subsidiary were subject to these restrictions."*

        This alerts users that not all consolidated cash is freely available to the group.
        """)

        st.subheader("Example 4: Unconsolidated Structured Entity")
        st.markdown("""
        *Extract from Notes:*

        *"The Group sponsors a securitisation vehicle (SecureCo) to which it sold $50 million of trade receivables. The Group does not consolidate SecureCo as it does not control the entity — decision-making rights rest with the trustee and noteholders. The Group's maximum exposure to loss is limited to a $2 million subordinated note retained, plus reputational risk should the Group choose to provide support beyond its contractual obligations. No such support has been provided during the year."*

        This discloses the "shadow" risk of an entity NOT on the balance sheet.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: NCI Disclosure Builder")
        col1, col2 = st.columns(2)
        with col1:
            sub_name = st.text_input("Subsidiary Name", value="Subsidiary X")
            nci_pct_disc = st.number_input("NCI Ownership %", value=30.0, step=5.0)
            sub_profit_disc = st.number_input("Subsidiary's Total Profit ($000)", value=4000)
            sub_equity_disc = st.number_input("Subsidiary's Total Equity ($000)", value=28000)
        with col2:
            nci_profit = sub_profit_disc * nci_pct_disc / 100
            nci_equity = sub_equity_disc * nci_pct_disc / 100
            st.markdown(f"""
            **Required IFRS 12 NCI Disclosure for {sub_name}:**

            | Item | Amount |
            |---|---|
            | Proportion of ownership held by NCI | {nci_pct_disc:.0f}% |
            | Profit allocated to NCI | ${nci_profit:,.0f}k |
            | Accumulated NCI at year-end | ${nci_equity:,.0f}k |
            """)
            if nci_pct_disc >= 10:
                st.warning("⚠️ This NCI is likely MATERIAL — full summarised financial information disclosure required.")
            else:
                st.info("ℹ️ This NCI may be aggregated with other immaterial NCI holdings.")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Structured Entity Risk Assessment")
        sponsors_se = st.checkbox("Does the entity sponsor a structured entity (e.g., securitisation vehicle)?")
        if sponsors_se:
            controls_se = st.radio("Does the entity control the structured entity?", ["Yes — consolidate under IFRS 10", "No — does not control"])
            if controls_se == "No — does not control":
                max_exposure = st.number_input("Maximum exposure to loss ($)", value=2000000, step=100000)
                support_provided = st.checkbox("Has the entity provided support without contractual obligation?")
                st.markdown(f"""
                **IFRS 12 Disclosure Required:**
                - Nature and extent of interest held in the structured entity
                - Maximum exposure to loss: **${max_exposure:,.0f}**
                - {"⚠️ Disclose details of support provided and reasons" if support_provided else "✅ No discretionary support provided during the period — disclose this fact"}
                """)
            else:
                st.success("✅ Entity is consolidated under IFRS 10 — IFRS 12 disclosures relate to NCI and group composition instead.")

    with tab4:
        st.header("Visualizations")

        st.subheader("IFRS 12 Disclosure Framework — Coverage")
        labels_d = ["IFRS 12 Disclosures", "Subsidiaries", "Joint Arrangements", "Associates", "Structured Entities"]
        parents_d = ["", "IFRS 12 Disclosures", "IFRS 12 Disclosures", "IFRS 12 Disclosures", "IFRS 12 Disclosures"]
        values_d = [100, 35, 25, 25, 15]
        fig = go.Figure(go.Treemap(labels=labels_d, parents=parents_d, values=values_d,
                                    marker_colors=["#1B3A6B","#2563EB","#10B981","#F59E0B","#F87171"]))
        fig.update_layout(title="IFRS 12 — Scope of Disclosure Requirements", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("NCI Profit/Equity Allocation Example")
        items_nci = ["Profit Attributable to Parent", "Profit Attributable to NCI"]
        vals_nci = [2800, 1200]
        fig2 = go.Figure(go.Pie(labels=items_nci, values=vals_nci, hole=0.4, marker_colors=["#2563EB","#F59E0B"]))
        fig2.update_layout(title="Profit Allocation — Parent vs NCI ($000)", height=350)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. IFRS 12 disclosures apply to interests in:**")
        q1 = st.radio("", ["Subsidiaries only", "Subsidiaries, joint arrangements and associates only", "Subsidiaries, joint arrangements, associates AND unconsolidated structured entities", "Only listed investees"], key="ifrs12q1")
        if st.button("Check Answer", key="ifrs12c1"):
            if q1 == "Subsidiaries, joint arrangements, associates AND unconsolidated structured entities":
                st.success("✅ Correct! IFRS 12 covers ALL FOUR categories: subsidiaries, joint arrangements, associates, AND unconsolidated structured entities.")
            else:
                st.error("❌ IFRS 12 scope is broader — it includes subsidiaries, joint arrangements, associates, AND unconsolidated structured entities.")

        st.markdown("---")
        st.markdown("**2. Significant judgement disclosures are particularly important when:**")
        q2 = st.radio("", ["The entity owns exactly 100% of a subsidiary", "Control or significant influence is NOT obvious from voting rights alone (e.g., de facto control)", "All investments are publicly listed", "The reporting period exceeds 12 months"], key="ifrs12q2")
        if st.button("Check Answer", key="ifrs12c2"):
            if q2 == "Control or significant influence is NOT obvious from voting rights alone (e.g., de facto control)":
                st.success("✅ Correct! These disclosures are most important when the conclusion isn't straightforward — such as de facto control with less than majority ownership.")
            else:
                st.error("❌ Significant judgement disclosures matter most when control/influence ISN'T obvious from simple ownership percentages.")

        st.markdown("---")
        st.markdown("**3. For a structured entity that is NOT consolidated, IFRS 12 requires disclosure of:")
        q3 = st.radio("", ["Nothing — unconsolidated entities are outside scope", "The maximum exposure to loss and nature of risks", "Full consolidated financial statements", "Only the entity's legal name"], key="ifrs12q3")
        if st.button("Check Answer", key="ifrs12c3"):
            if q3 == "The maximum exposure to loss and nature of risks":
                st.success("✅ Correct! Even unconsolidated structured entities require disclosure of the nature of interests held and MAXIMUM EXPOSURE TO LOSS — this surfaces 'shadow' risks not on the balance sheet.")
            else:
                st.error("❌ Unconsolidated structured entities still require risk disclosures — particularly MAXIMUM EXPOSURE TO LOSS.")

        st.markdown("---")
        st.markdown("**4. For subsidiaries with MATERIAL non-controlling interests, summarised financial information must be disclosed:**")
        q4 = st.radio("", ["Only if requested by auditors", "For each individually material subsidiary with material NCI", "Never — NCI disclosures are aggregate only", "Only for wholly-owned subsidiaries"], key="ifrs12q4")
        if st.button("Check Answer", key="ifrs12c4"):
            if q4 == "For each individually material subsidiary with material NCI":
                st.success("✅ Correct! IFRS 12 requires detailed summarised financial information for EACH subsidiary that has MATERIAL non-controlling interests.")
            else:
                st.error("❌ Detailed disclosure is required for EACH subsidiary with MATERIAL NCI, not aggregated or only for wholly-owned entities.")

        st.markdown("---")
        st.markdown("**5. Restrictions on a parent's ability to access group assets (e.g., FX controls in a subsidiary's country) must be:**")
        q5 = st.radio("", ["Ignored as immaterial", "Disclosed, including nature and extent of significant restrictions", "Only disclosed if requested by regulators", "Recognised as an impairment"], key="ifrs12q5")
        if st.button("Check Answer", key="ifrs12c5"):
            if q5 == "Disclosed, including nature and extent of significant restrictions":
                st.success("✅ Correct! IFRS 12 requires disclosure of significant restrictions on the parent's ability to access or use group assets — important for assessing real liquidity/flexibility.")
            else:
                st.error("❌ Significant restrictions on accessing group assets MUST be disclosed — this affects users' understanding of true group liquidity.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Scope — Four Categories
        1. Subsidiaries (IFRS 10)
        2. Joint arrangements (IFRS 11)
        3. Associates (IAS 28)
        4. Unconsolidated structured entities

        ### 2. Objective
        Help users evaluate:
        - **Nature and risks** of interests in other entities
        - **Effects** on financial position, performance, cash flows

        ### 3. Key Disclosures by Category
        | Category | Key Disclosures |
        |---|---|
        | Subsidiaries | Significant judgements on control; material NCI details; restrictions on accessing assets |
        | JV/Associates | Summarised financial info; restrictions on fund transfers |
        | Structured Entities | Nature of interests; MAXIMUM EXPOSURE TO LOSS; support provided |

        ### 4. Significant Judgements
        Disclose reasoning when control/joint control/significant influence is NOT obvious from voting rights alone (e.g., de facto control).
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
IFRS 12 Scope = Subsidiaries + Joint Arrangements + Associates + Structured Entities
Material NCI → detailed summarised financial info required PER subsidiary
Structured Entities (unconsolidated) → disclose MAXIMUM EXPOSURE TO LOSS
Significant judgements → disclose when control/influence conclusion isn't obvious
Restrictions on group assets → MUST disclose nature and extent
        """)

        st.success("🎓 **IFRS 12 Complete!** You can now prepare comprehensive disclosures for all types of interests in other entities.")
        st.info("💡 **Next**: IFRS 13 — Fair Value Measurement")

if __name__ == "__main__":
    show()