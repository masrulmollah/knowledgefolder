import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.title("🌐 Module 1: Introduction to Transfer Pricing in Bangladesh")
    st.markdown("*Based on the Income Tax Act 2023 (ITA 2023) of Bangladesh*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Law", "🧮 Examples", "💡 Interactive Exercise",
        "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────────────────────
    with tab1:
        st.header("Theory & Legal Concepts")

        st.subheader("1. What is Transfer Pricing?")
        st.markdown("""
        **Transfer Pricing** refers to the prices charged for transactions between **associated enterprises** 
        (related parties) operating in different tax jurisdictions. These transactions include:

        - Sale/purchase of goods or tangible assets
        - Provision of services (management, technical, administrative)
        - Licensing of intangible property (patents, trademarks, know-how)
        - Financing arrangements (loans, guarantees)
        - Cost-sharing arrangements

        > 🏦 *Example*: A Bangladeshi subsidiary buys raw materials from its parent company in Singapore.
        > The price charged for this intra-group transaction is the **transfer price**.
        """)

        st.subheader("2. Why Transfer Pricing Matters")
        st.markdown("""
        Without regulation, multinational enterprises (MNEs) may manipulate transfer prices to:
        - **Shift profits** from high-tax jurisdictions (like Bangladesh) to low-tax ones
        - **Minimise global tax liability** at the expense of the Bangladeshi tax base
        - **Erode the tax base** of developing countries

        Transfer pricing rules ensure that Bangladesh collects its **fair share of tax** on genuine economic activity.
        """)

        st.subheader("3. Legal Framework in Bangladesh")
        st.markdown("""
        #### Primary Legislation
        | Source | Provision |
        |--------|-----------|
        | Income Tax Act 2023 (ITA 2023) | Sections 175–185 (Transfer Pricing) |
        | Income Tax Rules 2023 | Rules 68–80 (TP Methodology & Documentation) |
        | SRO Notifications | NBR supplementary circulars |

        #### Key Definitions under ITA 2023

        **Section 175 – "International Transaction"** means a transaction between two or more associated enterprises, 
        either or both of which are non-residents, including:
        - Purchase, sale, lease of tangible/intangible property
        - Provision or receipt of services
        - Lending or borrowing of money
        - Any other transaction affecting profit, income, loss or assets

        **Section 176 – "Associated Enterprise"** means an enterprise that:
        - Directly or indirectly participates in the management, control or capital of another enterprise, **or**
        - The same persons participate in the management, control or capital of both enterprises

        **Deemed association triggers (Section 176):**
        - One enterprise holds ≥ 26% voting power/shares in the other
        - One enterprise advances a loan of ≥ 51% of the book value of the other's assets
        - One enterprise guarantees ≥ 10% of total borrowings of the other
        - Common directors/managers hold ≥ 50% of the board
        - One enterprise wholly depends on the other's intellectual property
        """)

        st.subheader("4. The Arm's Length Standard")
        st.markdown("""
        The foundation of transfer pricing law worldwide (and in Bangladesh) is the **Arm's Length Principle (ALP)**:

        > *"A transaction between associated enterprises shall be determined having regard to the arm's length price."*
        > — **Section 177, ITA 2023**

        **Arm's Length Price (ALP)** is the price that would be charged between **independent unrelated parties** 
        in comparable uncontrolled transactions under similar circumstances.

        #### Why ALP?
        - Reflects genuine market value
        - Prevents artificial profit shifting
        - Consistent with OECD Guidelines (Bangladesh is aligned)
        - Internationally accepted standard
        """)

        st.subheader("5. Scope & Applicability")
        st.markdown("""
        Transfer pricing provisions under ITA 2023 apply to:

        ✅ Any **international transaction** between associated enterprises  
        ✅ Transactions where **one party is a non-resident**  
        ✅ **Specified domestic transactions** exceeding BDT **30 crore** in aggregate in a year  
        ✅ Transactions by a **Permanent Establishment (PE)** with its head office/group entities  

        ❌ **Not applicable to:**
        - Transactions between unrelated independent parties
        - Purely domestic transactions below the threshold (except specified domestic transactions)
        """)

        st.subheader("6. Role of the National Board of Revenue (NBR)")
        st.markdown("""
        The **National Board of Revenue (NBR)** of Bangladesh:
        - Administers and enforces transfer pricing rules
        - Issues Transfer Pricing Orders (TPO)
        - Conducts TP audits through **Transfer Pricing Officers**
        - Issues guidelines via SRO/circular
        - Signs **Advance Pricing Agreements (APAs)** with taxpayers

        Bangladesh introduced formal TP regulations in **2012** (Finance Act 2012) and significantly 
        upgraded them under the **ITA 2023**.
        """)

    # ─────────────────────────────────────────────
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Identifying an International Transaction")
        st.markdown("""
        **Scenario:**  
        RMG Bangladesh Ltd. (a garment manufacturer in Bangladesh) purchases fabric from Tex Holdings Pte. Ltd. 
        (its parent company in Singapore). RMG Bangladesh also receives management services from Tex Holdings.

        **Analysis:**

        | Transaction | Type | International? | TP Applicable? |
        |-------------|------|----------------|----------------|
        | Fabric purchase | Tangible goods | ✅ Yes (cross-border) | ✅ Yes |
        | Management fee | Services | ✅ Yes (cross-border) | ✅ Yes |
        | Sale of goods to Bangladeshi customer | Tangible goods | ❌ No (domestic) | ❌ No |

        **Conclusion:** Both cross-border intra-group transactions are **international transactions** under 
        Section 175, ITA 2023, and must be priced at arm's length.
        """)

        st.subheader("Example 2: Identifying Associated Enterprise Status")
        st.markdown("""
        **Scenario:**  
        Alpha Corp (UK) holds 30% of the shares of Beta Ltd. (Bangladesh).

        **Legal Analysis under Section 176, ITA 2023:**

        - Threshold for share ownership: **≥ 26%**
        - Alpha Corp holds **30%** → exceeds 26% threshold
        - Therefore, Alpha Corp and Beta Ltd. are **Associated Enterprises**

        ✅ Any transaction between them is an **international transaction** subject to TP rules.
        """)

        st.subheader("Example 3: Profit Shifting — Why TP Rules Exist")
        with st.expander("Click to see profit shifting illustration"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                **Without Arm's Length Pricing:**
                | | Bangladesh (30% tax) | Low-tax Country (5% tax) |
                |--|--|--|
                | Revenue | 100 | 50 |
                | Cost (inflated) | 80 | 5 |
                | Profit | 20 | 45 |
                | Tax | 6 | 2.25 |
                | **Total Tax** | **8.25** | |
                """)
            with col2:
                st.markdown("""
                **With Arm's Length Pricing:**
                | | Bangladesh (30% tax) | Low-tax Country (5% tax) |
                |--|--|--|
                | Revenue | 100 | 50 |
                | Cost (ALP) | 60 | 5 |
                | Profit | 40 | 45 |
                | Tax | 12 | 2.25 |
                | **Total Tax** | **14.25** | |
                """)
            st.info("💡 By inflating intra-group charges, BDT 6 of Bangladesh tax is avoided. TP rules prevent this.")

        st.subheader("Example 4: Specified Domestic Transaction")
        st.markdown("""
        **Scenario:**  
        Meghna Pharma Ltd. and its sister concern Meghna Chemicals Ltd. (both Bangladeshi companies) 
        are associated enterprises under a common holding company. Meghna Pharma purchases raw chemicals 
        worth BDT 35 crore from Meghna Chemicals in FY 2023-24.

        **Analysis:**
        - Both are domestic entities → normally outside TP scope
        - But the transaction exceeds **BDT 30 crore** threshold
        - This qualifies as a **Specified Domestic Transaction** under ITA 2023
        - **TP rules apply** → transaction must be at arm's length
        """)

    # ─────────────────────────────────────────────
    with tab3:
        st.header("Interactive Exercise")

        st.subheader("🔍 Exercise 1: Is it an Associated Enterprise?")
        st.markdown("Enter the ownership percentage and check if TP rules apply:")

        ownership = st.slider("Ownership / Voting Power (%)", 0, 100, 20)
        loan_pct = st.slider("Loan as % of book value of assets", 0, 100, 30)
        common_directors = st.slider("Common directors as % of total board", 0, 100, 40)

        ae_triggered = False
        reasons = []
        if ownership >= 26:
            ae_triggered = True
            reasons.append(f"✅ Ownership {ownership}% ≥ 26% threshold (Section 176)")
        if loan_pct >= 51:
            ae_triggered = True
            reasons.append(f"✅ Loan {loan_pct}% ≥ 51% of book value (Section 176)")
        if common_directors >= 50:
            ae_triggered = True
            reasons.append(f"✅ Common directors {common_directors}% ≥ 50% of board (Section 176)")

        if ae_triggered:
            st.error("⚠️ **Associated Enterprise status triggered! Transfer Pricing rules apply.**")
            for r in reasons:
                st.markdown(r)
        else:
            st.success("✅ No associated enterprise relationship detected under current thresholds.")
            st.markdown("*(Adjust sliders to trigger association)*")

        st.markdown("---")
        st.subheader("🔍 Exercise 2: Transaction Classifier")
        st.markdown("Classify your transaction and check TP applicability:")

        is_crossborder = st.selectbox("Is the transaction cross-border?", ["Yes", "No"])
        is_associated = st.selectbox("Are the parties associated enterprises?", ["Yes", "No"])
        txn_value = st.number_input("Transaction value (BDT Crore)", min_value=0.0, value=10.0, step=1.0)
        is_domestic = st.selectbox("Is this a purely domestic transaction?", ["No", "Yes"])

        if st.button("Check TP Applicability"):
            if is_crossborder == "Yes" and is_associated == "Yes":
                st.error("🔴 **Transfer Pricing rules APPLY** — International transaction between associated enterprises.")
            elif is_domestic == "Yes" and is_associated == "Yes" and txn_value >= 30:
                st.warning("🟡 **Transfer Pricing rules APPLY** — Specified Domestic Transaction (≥ BDT 30 Crore).")
            elif is_domestic == "Yes" and is_associated == "Yes" and txn_value < 30:
                st.success("🟢 TP rules do NOT apply — domestic transaction below BDT 30 crore threshold.")
            else:
                st.success("🟢 TP rules do NOT apply to this transaction.")

    # ─────────────────────────────────────────────
    with tab4:
        st.header("Quiz")

        score = 0
        total = 5

        st.markdown("**1. Under Section 176 of ITA 2023, what is the minimum share ownership percentage to be deemed an 'Associated Enterprise'?**")
        q1 = st.radio("Select:", ["10%", "20%", "26%", "51%"], key="m1q1")
        if st.button("Check", key="m1c1"):
            if q1 == "26%":
                st.success("✅ Correct! Section 176 sets the threshold at ≥ 26% voting power/shares.")
            else:
                st.error("❌ Incorrect. The correct threshold is 26% under Section 176, ITA 2023.")

        st.markdown("---")
        st.markdown("**2. What is the threshold for a domestic transaction to qualify as a 'Specified Domestic Transaction' under ITA 2023?**")
        q2 = st.radio("Select:", ["BDT 10 Crore", "BDT 20 Crore", "BDT 30 Crore", "BDT 50 Crore"], key="m1q2")
        if st.button("Check", key="m1c2"):
            if q2 == "BDT 30 Crore":
                st.success("✅ Correct! The specified domestic transaction threshold is BDT 30 Crore.")
            else:
                st.error("❌ Incorrect. The threshold is BDT 30 Crore under ITA 2023.")

        st.markdown("---")
        st.markdown("**3. The Arm's Length Principle requires that intra-group transactions be priced as if:**")
        q3 = st.radio("Select:", [
            "The parent company determines the price",
            "The price maximises group profit",
            "Independent unrelated parties negotiated the price",
            "The NBR fixes the price"
        ], key="m1q3")
        if st.button("Check", key="m1c3"):
            if q3 == "Independent unrelated parties negotiated the price":
                st.success("✅ Correct! The ALP mirrors what independent parties in comparable transactions would agree to.")
            else:
                st.error("❌ Incorrect. ALP = price that would be charged between independent unrelated parties.")

        st.markdown("---")
        st.markdown("**4. Which section of ITA 2023 defines 'International Transaction'?**")
        q4 = st.radio("Select:", ["Section 150", "Section 175", "Section 200", "Section 80"], key="m1q4")
        if st.button("Check", key="m1c4"):
            if q4 == "Section 175":
                st.success("✅ Correct! Section 175, ITA 2023 defines 'International Transaction'.")
            else:
                st.error("❌ Incorrect. The correct answer is Section 175, ITA 2023.")

        st.markdown("---")
        st.markdown("**5. Which government body administers transfer pricing in Bangladesh?**")
        q5 = st.radio("Select:", ["Bangladesh Bank", "Ministry of Finance", "NBR (National Board of Revenue)", "BIDA"], key="m1q5")
        if st.button("Check", key="m1c5"):
            if q5 == "NBR (National Board of Revenue)":
                st.success("✅ Correct! NBR administers and enforces Bangladesh's transfer pricing rules.")
            else:
                st.error("❌ Incorrect. NBR (National Board of Revenue) is the correct answer.")

    # ─────────────────────────────────────────────
    with tab5:
        st.header("Module Summary")

        st.markdown("""
        ### 🎯 Key Takeaways

        | Concept | Key Point |
        |---------|-----------|
        | Transfer Pricing | Prices for intra-group cross-border transactions |
        | Governing Law | Income Tax Act 2023, Sections 175–185 |
        | International Transaction | Defined under Section 175, ITA 2023 |
        | Associated Enterprise | Section 176 — ≥ 26% ownership / 51% loan / 50% directors |
        | Arm's Length Principle | Section 177 — must price as if between independent parties |
        | Specified Domestic Txn | Domestic related-party transactions ≥ BDT 30 Crore |
        | Regulator | National Board of Revenue (NBR) |
        | TP introduced in BD | Finance Act 2012; upgraded under ITA 2023 |

        ### 📌 Legal Reference Map
        ```
        ITA 2023
        ├── Section 175  →  Definition: International Transaction
        ├── Section 176  →  Definition: Associated Enterprise
        ├── Section 177  →  Arm's Length Price requirement
        ├── Section 178  →  TP Methods
        ├── Section 179  →  Most Appropriate Method
        ├── Section 180  →  Documentation obligations
        ├── Section 181  →  TP Officer powers
        ├── Section 182  →  Adjustment & Penalties
        ├── Section 183  →  Advance Pricing Agreement
        ├── Section 184  →  Safe Harbour provisions
        └── Section 185  →  Mutual Agreement Procedure (MAP)
        ```

        ### 🔑 Why It Matters for Bangladesh
        - Protects the domestic **tax base** from profit shifting by MNEs
        - Ensures **fair taxation** of genuine economic activity in Bangladesh
        - Aligns Bangladesh with **OECD BEPS** (Base Erosion and Profit Shifting) framework
        - Critical for **FDI-heavy sectors** (garments, pharma, telecom, banking)
        """)

        st.success("🎓 **Module 1 Complete!** You now understand the foundation of Transfer Pricing law in Bangladesh.")
        st.info("💡 **Next**: Proceed to Module 2 — Arm's Length Principle & Comparability Analysis.")

if __name__ == "__main__":
    show()