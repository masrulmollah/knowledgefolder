import streamlit as st
import pandas as pd

def show():
    st.title("🤝 IAS 24: Related Party Disclosures")
    st.markdown("*Master identification of related parties and required disclosure of related party transactions*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Objective")
        st.markdown("""
IAS 24 ensures financial statements contain disclosures necessary to draw attention to the possibility that
the entity's financial position and profit or loss may have been affected by transactions with related parties.

Related party transactions may not be at arm's length — they could distort financial results.
        """)
        st.subheader("2. Who is a Related Party?")
        st.markdown("""
**A person is a related party if they:**
- Control or have joint control over the entity
- Have significant influence over the entity
- Are a member of key management personnel (KMP) of the entity or its parent

**An entity is a related party if:**
- It is a parent, subsidiary, fellow subsidiary, associate or joint venture
- Both entities are joint ventures of the same third party
- It is a post-employment benefit plan for employees of the entity
- It is controlled or jointly controlled by a related party person
- A person with significant influence over the entity controls it
- A person is a close member of family of a person who controls the entity

**Close members of family** = spouse/domestic partner, children, dependants of the person or their partner.
        """)
        st.subheader("3. Key Management Personnel (KMP)")
        st.markdown("""
Those who have authority and responsibility for planning, directing and controlling activities:
- Directors (executive and non-executive)
- C-suite executives (CEO, CFO, COO)
- Compensation of KMP must be disclosed in total and by category:
  - Short-term benefits
  - Post-employment benefits
  - Other long-term benefits
  - Termination benefits
  - Share-based payments
        """)
        st.subheader("4. Required Disclosures")
        st.markdown("""
**Regardless of whether transactions occurred:**
- Relationships between parents and subsidiaries must ALWAYS be disclosed
- Name of immediate and ultimate controlling party (even if no transactions)

**If transactions occurred:**
- Nature of the related party relationship
- Amount of transactions
- Outstanding balances (terms, conditions, guarantees)
- Provisions for doubtful debts on related party balances
- Expense recognised for bad/doubtful related party debts

**Disclosure by category of related party** (not a single aggregate):
Parent | Subsidiaries | Associates | Joint ventures | KMP | Other related parties
        """)
        st.subheader("5. Exemptions")
        st.markdown("""
**Government-related entities:** An entity that is government-controlled need not disclose all transactions with other government-controlled entities in detail — but must disclose:
- Name of the government and nature of relationship
- Individually significant transactions
- Collectively significant transactions (qualitative + quantitative description)
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Identifying Related Parties")
        data = pd.DataFrame({
            "Party": ["ABC Ltd (parent owns 80%)","XYZ Ltd (fellow subsidiary)","DEF Ltd (entity owns 30%, significant influence)","CEO of the entity","CEO's spouse's company","Pension fund for employees","Another company controlled by major shareholder"],
            "Related Party?": ["✅ Yes — subsidiary","✅ Yes — fellow subsidiary","✅ Yes — associate","✅ Yes — KMP","✅ Yes — close family member's entity","✅ Yes — post-employment benefit plan","✅ Yes — major shareholder controls both"],
            "Relationship": ["Subsidiary","Fellow subsidiary","Associate","Key Management Personnel","Close family of KMP","Benefit plan for employees","Common control relationship"]
        })
        st.dataframe(data, use_container_width=True, hide_index=True)

        st.subheader("Example 2: KMP Compensation Disclosure")
        kmp = pd.DataFrame({
            "Category": ["Short-term employee benefits","Post-employment benefits","Other long-term benefits","Termination benefits","Share-based payments","Total KMP Compensation"],
            "2024 ($000)": [3200, 480, 120, 0, 850, 4650],
            "2023 ($000)": [2900, 420, 100, 200, 720, 4340]
        })
        st.dataframe(kmp, use_container_width=True, hide_index=True)

        st.subheader("Example 3: Related Party Transaction Note")
        st.markdown("""
*Extract from Notes — Related Party Transactions:*

**Transactions with parent company (XYZ Holdings):**
- Management fees charged by parent: $500,000 (2023: $450,000)
- Outstanding balance payable at year-end: $125,000 (unsecured, no fixed repayment terms, 0% interest)

**Sales to associates:**
- Sales of goods to DEF Associates Ltd: $1,200,000 (2023: $980,000) at arm's length prices
- Outstanding receivable: $320,000 (no provision for doubtful debts)

*"All related party transactions are conducted on normal commercial terms."*
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Related Party Identifier")
        relationship = st.selectbox("What is the relationship?", [
            "Entity owns 60% of the other entity",
            "Entity owns 30% (significant influence)",
            "Both entities owned by the same government",
            "CEO of the reporting entity",
            "CEO's adult child's company",
            "A bank that provides financing only",
            "Trade customer with no ownership link",
            "Joint venture partner (50/50)"
        ])
        rp_map = {
            "Entity owns 60% of the other entity": ("✅ Related Party", "Subsidiary — control exists"),
            "Entity owns 30% (significant influence)": ("✅ Related Party", "Associate — significant influence"),
            "Both entities owned by the same government": ("⚠️ Partial Exemption", "Government-related entities — simplified disclosure applies"),
            "CEO of the reporting entity": ("✅ Related Party", "Key Management Personnel"),
            "CEO's adult child's company": ("✅ Related Party", "Close family member of KMP controls this entity"),
            "A bank that provides financing only": ("❌ Not a Related Party", "Mere commercial relationship without control or significant influence"),
            "Trade customer with no ownership link": ("❌ Not a Related Party", "Arm's length commercial relationship — not a related party"),
            "Joint venture partner (50/50)": ("✅ Related Party", "Joint venture — both parties are related to each other")
        }
        result, reason = rp_map[relationship]
        if "✅" in result:
            st.success(f"{result}\n\n{reason}")
        elif "⚠️" in result:
            st.warning(f"{result}\n\n{reason}")
        else:
            st.info(f"{result}\n\n{reason}")

    with tab4:
        st.header("Visualizations")
        st.markdown("### Related Party Network Map")
        st.markdown("""
```
                    ULTIMATE PARENT
                         |
               ┌─────────┴──────────┐
          PARENT CO              OTHER SUBSIDIARY
               |                      (Fellow Subsidiary)
        ┌──────┴──────┐
   REPORTING     SUBSIDIARY
    ENTITY            ↑ (related)
        |
   ┌────┴────────────┐
ASSOCIATE        JOINT VENTURE
(30% owned)       (50% owned)
        |
    KMP (Directors, CEO, CFO)
        |
   Close Family Members
   & Their Entities
```
        """)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. A fellow subsidiary (entity with the same parent) is:**")
        q1 = st.radio("", ["Not a related party","A related party","Related only if there are transactions between them","Related only if combined ownership exceeds 50%"], key="ias24q1")
        if st.button("Check", key="c24_1"):
            if q1 == "A related party":
                st.success("✅ Correct! Fellow subsidiaries (sharing the same parent) are related parties under IAS 24 regardless of whether transactions occur.")
            else:
                st.error("❌ Fellow subsidiaries are ALWAYS related parties — no transactions are needed to trigger the relationship.")
        st.markdown("---")
        st.markdown("**2. Must parent-subsidiary relationships always be disclosed, even with no transactions?**")
        q2 = st.radio("", ["Yes — always disclose","No — only if material transactions exist","Only in the parent's financial statements","Only if the subsidiary is material"], key="ias24q2")
        if st.button("Check", key="c24_2"):
            if q2 == "Yes — always disclose":
                st.success("✅ Correct! IAS 24 ALWAYS requires disclosure of parent-subsidiary relationships and the name of the ultimate controlling party, even if no transactions occurred.")
            else:
                st.error("❌ Parent-subsidiary relationships must ALWAYS be disclosed regardless of whether transactions took place.")
        st.markdown("---")
        st.markdown("**3. The spouse of the CEO of a reporting entity is:**")
        q3 = st.radio("", ["Not a related party","A related party as a close family member of KMP","Only a related party if they work in the entity","Related only if they own shares"], key="ias24q3")
        if st.button("Check", key="c24_3"):
            if q3 == "A related party as a close family member of KMP":
                st.success("✅ Correct! Close family members (including spouses) of KMP are related parties under IAS 24. Any entity they control would also be a related party.")
            else:
                st.error("❌ Spouses and close family of KMP are related parties under IAS 24 — no employment needed.")
        st.markdown("---")
        st.markdown("**4. KMP compensation must be disclosed:**")
        q4 = st.radio("", ["As one total figure only","By individual director","By category (short-term, post-employment, share-based etc.)","Only if exceeding a materiality threshold"], key="ias24q4")
        if st.button("Check", key="c24_4"):
            if q4 == "By category (short-term, post-employment, share-based etc.)":
                st.success("✅ Correct! IAS 24 requires KMP compensation to be disclosed in total, broken down by category of benefit.")
            else:
                st.error("❌ KMP compensation is disclosed in total AND by category (short-term, post-employment, LTI, termination, share-based).")
        st.markdown("---")
        st.markdown("**5. Under the government-related entity exemption, what must still be disclosed?**")
        q5 = st.radio("", ["Nothing — full exemption","The name of the government, nature of relationship, and individually significant transactions","Only the total value of all transactions","The specific terms of each transaction"], key="ias24q5")
        if st.button("Check", key="c24_5"):
            if q5 == "The name of the government, nature of relationship, and individually significant transactions":
                st.success("✅ Correct! Even under the government exemption, entities must disclose: the government's name, the relationship, and individually and collectively significant transactions.")
            else:
                st.error("❌ Government exemption still requires: government name, relationship nature, and individually significant transactions.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 24 Key Rules

**Always disclose:** Parent-subsidiary relationships + ultimate controlling party name

**Related Parties include:**
- Parent, subsidiaries, fellow subsidiaries
- Associates and joint ventures
- Key Management Personnel (KMP)
- Close family of KMP and entities they control
- Post-employment benefit plans

**Transaction Disclosures (if any):**
- Nature of relationship + amount of transactions
- Outstanding balances + terms
- Provisions for related party bad debts

**KMP Compensation:** Disclose by category (5 types)

**NOT related parties:** Banks providing only finance, government regulators, trade customers (no control/influence)
        """)
        st.success("🎓 IAS 24 Complete!")
        st.info("💡 Next: IAS 27 — Separate Financial Statements")

if __name__ == "__main__":
    show()