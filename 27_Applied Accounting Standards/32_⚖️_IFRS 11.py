import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("⚖️ IFRS 11: Joint Arrangements")
    st.markdown("*Master joint operations vs joint ventures and the required accounting treatment for each*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Definition of a Joint Arrangement")
        st.markdown("""
        A **joint arrangement** is an arrangement where two or more parties have **joint control**.

        **Joint control** exists when:
        - Decisions about relevant activities require **unanimous consent** of the parties sharing control
        - Control is **contractually shared**

        **Key feature:** Even with 50/50 ownership, joint control only exists if there's a contractual agreement requiring unanimous consent for key decisions.
        """)

        st.subheader("2. Two Types of Joint Arrangements — The Critical Classification")
        st.markdown("""
        IFRS 11 classifies joint arrangements into TWO types based on the **rights and obligations** of the parties:

        | Type | Definition | Accounting |
        |---|---|---|
        | **Joint Operation** | Parties have rights to the **assets** and obligations for the **liabilities** | Recognise own share of assets, liabilities, revenues, expenses (line-by-line) |
        | **Joint Venture** | Parties have rights to the **net assets** (equity interest) | **Equity method** (IAS 28) |

        **Classification depends on:**
        - **Structure:** Not structured through a separate vehicle → automatically a Joint Operation
        - If structured through a separate vehicle → assess further:
          - Legal form of the separate vehicle
          - Terms of the contractual arrangement
          - Other relevant facts and circumstances (e.g., if output is taken by parties in proportion to their interest, and the vehicle's sole purpose is to provide output to the parties → may still be a Joint Operation despite the separate vehicle)
        """)

        st.subheader("3. Joint Operations — Accounting Treatment")
        st.markdown("""
        A party to a joint operation (a **joint operator**) recognises in relation to its interest:
        - **Its assets**, including its share of any jointly held assets
        - **Its liabilities**, including its share of any jointly incurred liabilities
        - **Its revenue** from the sale of its share of the output from the joint operation
        - **Its share of revenue** from the sale of output by the joint operation
        - **Its expenses**, including its share of any jointly incurred expenses

        This is essentially **proportionate consolidation in substance** — recognising your SHARE of each line item directly (not via equity method).
        """)

        st.subheader("4. Joint Ventures — Accounting Treatment")
        st.markdown("""
        A party to a joint venture (a **joint venturer**) accounts for its interest using the **EQUITY METHOD** under IAS 28.

        - Initial recognition: at cost
        - Subsequent: cost + share of post-acquisition profit/loss + share of OCI − dividends received
        - Single line in P&L: "share of profit of joint ventures"

        **No line-by-line consolidation** — this is the major contrast with Joint Operations.
        """)

        st.subheader("5. Assessing the Type — Decision Framework")
        st.markdown("""
        ```
        Is the arrangement structured through a separate vehicle?
                    |
            ┌───────┴────────┐
            NO               YES
            |                 |
        JOINT OPERATION    Assess legal form, contractual terms,
        (automatic)        and other facts/circumstances
                                |
                    ┌───────────┴────────────┐
                Rights to NET ASSETS      Rights to ASSETS &
                (equity interest)          obligations for
                    |                       LIABILITIES
                JOINT VENTURE                   |
                (Equity Method)            JOINT OPERATION
                                         (Recognise share of
                                          assets/liabilities)
        ```
        """)

        st.subheader("6. Common Examples by Industry")
        st.markdown("""
        | Industry | Typical Arrangement | Usual Classification |
        |---|---|---|
        | Oil & Gas exploration | Unincorporated joint operating agreement | Joint Operation |
        | Real estate development | Separate company (SPV) holding net assets | Joint Venture |
        | Manufacturing | Separate jointly-owned company | Joint Venture (usually) |
        | Mining | Direct shared interests in a mine (no separate vehicle) | Joint Operation |
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Joint Operation — Oil & Gas Exploration")
        st.markdown("""
        **Facts:** Two oil companies, A and B, jointly explore an oil field under an unincorporated Joint Operating Agreement (JOA). Each holds a 50% direct interest in the assets and is liable for 50% of the costs. No separate legal entity is created.

        **Classification: JOINT OPERATION** (no separate vehicle)

        **Company A's accounting (50% interest):**
        | Item | A's Share |
        |---|---|
        | Oil rig (asset) | 50% × $10,000,000 = $5,000,000 |
        | Decommissioning provision | 50% × $2,000,000 = $1,000,000 |
        | Operating expenses for the year | 50% × $3,000,000 = $1,500,000 |
        | Revenue from sale of oil (A's allocated share) | $4,200,000 (A sells its own share directly) |

        Company A recognises these amounts **directly on its own balance sheet/P&L** — line by line.
        """)

        st.subheader("Example 2: Joint Venture — Separate Vehicle")
        st.markdown("""
        **Facts:** Companies C and D form a new company, JV Co, to develop a shopping mall. JV Co holds all assets and liabilities in its own name; C and D's recourse is limited to their share of JV Co's net assets (equity interest only).

        **Classification: JOINT VENTURE** (separate vehicle; rights to net assets only)

        **Company C's accounting (50% interest), using equity method:**
        | | $ |
        |---|---|
        | Cost of investment | 3,000,000 |
        | + Share of JV Co's profit for the year (50% × $800,000) | 400,000 |
        | − Dividends received (50% × $300,000) | (150,000) |
        | **Carrying amount of investment** | **3,250,000** |

        Company C does NOT show JV Co's individual assets/liabilities on its own balance sheet — only the single "Investment in Joint Venture" line.
        """)

        st.subheader("Example 3: Separate Vehicle that is STILL a Joint Operation")
        st.markdown("""
        **Facts:** Companies E and F set up SPV Ltd to manufacture a single product, which is taken entirely by E and F in proportion to their ownership (50/50). SPV Ltd's sole activity is to manufacture according to E and F's specifications, essentially acting as a processing facility. The contractual terms state E and F have rights to the assets and are liable for the liabilities, even though a legal entity exists.

        **Classification: JOINT OPERATION (despite the separate vehicle!)**

        This is the classic exception — the legal form (separate vehicle) does NOT override substance when the contractual terms and facts indicate the parties have rights to assets and obligations for liabilities (not merely rights to net assets).
        """)

        st.subheader("Example 4: Comparison Table — Same Economics, Different Classification")
        comparison_data = pd.DataFrame({
            "Feature": ["Balance Sheet Presentation", "Revenue Recognition", "Expense Recognition", "P&L Line Item"],
            "Joint Operation": ["Show share of each asset/liability directly", "Recognise own share of revenue", "Recognise own share of expenses", "Multiple lines (revenue, COGS, etc.)"],
            "Joint Venture": ["Single 'Investment in JV' line", "Not recognised directly", "Not recognised directly", "Single line: 'Share of profit of JV'"]
        })
        st.dataframe(comparison_data, use_container_width=True, hide_index=True)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Joint Arrangement Classifier")
        col1, col2 = st.columns(2)
        with col1:
            separate_vehicle = st.checkbox("Structured through a separate legal vehicle?")
            if separate_vehicle:
                rights_to_assets = st.radio("What rights do the parties have?", ["Rights to specific assets and obligations for specific liabilities", "Rights only to the net assets (residual interest)"])
                output_taken_proportionally = st.checkbox("Does the vehicle's sole purpose appear to be providing output to the parties in proportion to ownership?")
        with col2:
            if not separate_vehicle:
                st.success("📌 **JOINT OPERATION** — No separate vehicle means automatic classification as a Joint Operation. Recognise your share of assets, liabilities, revenue and expenses directly.")
            else:
                if rights_to_assets == "Rights to specific assets and obligations for specific liabilities" or output_taken_proportionally:
                    st.success("📌 **JOINT OPERATION** — Despite the separate vehicle, the substance indicates rights to assets/obligations for liabilities. Recognise your share line-by-line.")
                else:
                    st.info("📌 **JOINT VENTURE** — Separate vehicle with rights limited to net assets. Apply the EQUITY METHOD (IAS 28).")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Joint Operation — Share Calculator")
        ownership_pct = st.number_input("Your ownership/interest %", value=50.0, step=5.0) / 100
        col1, col2 = st.columns(2)
        with col1:
            total_assets_jo = st.number_input("Total Joint Assets ($)", value=10000000, step=100000)
            total_liab_jo = st.number_input("Total Joint Liabilities ($)", value=2000000, step=100000)
        with col2:
            total_revenue_jo = st.number_input("Total Revenue ($)", value=8000000, step=100000)
            total_expenses_jo = st.number_input("Total Expenses ($)", value=5000000, step=100000)

        if st.button("Calculate My Share (Joint Operation)"):
            my_assets = total_assets_jo * ownership_pct
            my_liab = total_liab_jo * ownership_pct
            my_rev = total_revenue_jo * ownership_pct
            my_exp = total_expenses_jo * ownership_pct
            st.markdown(f"""
            **Recognise directly on YOUR balance sheet/P&L:**

            | Item | Your Share ({ownership_pct*100:.0f}%) |
            |---|---|
            | Assets | ${my_assets:,.0f} |
            | Liabilities | ${my_liab:,.0f} |
            | Revenue | ${my_rev:,.0f} |
            | Expenses | ${my_exp:,.0f} |
            | **Net Profit Contribution** | **${my_rev - my_exp:,.0f}** |
            """)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Joint Venture — Equity Method Calculator")
        col1, col2 = st.columns(2)
        with col1:
            jv_cost = st.number_input("Initial Cost of Investment ($)", value=3000000, step=10000)
            jv_ownership = st.number_input("Ownership %", value=50.0, step=5.0, key="jv_own") / 100
            jv_profit = st.number_input("JV's Total Profit for the Year ($)", value=800000, step=10000)
        with col2:
            jv_dividends = st.number_input("JV's Total Dividends Declared ($)", value=300000, step=10000)
            share_profit_jv = jv_profit * jv_ownership
            share_div_jv = jv_dividends * jv_ownership
            closing_jv = jv_cost + share_profit_jv - share_div_jv
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | Opening Investment | ${jv_cost:,.0f} |
            | + Share of Profit ({jv_ownership*100:.0f}%) | ${share_profit_jv:,.0f} |
            | − Dividends Received | (${share_div_jv:,.0f}) |
            | **Closing Investment Carrying Amount** | **${closing_jv:,.0f}** |

            **P&L:** Share of profit of joint venture = ${share_profit_jv:,.0f} (single line item)
            """)

    with tab4:
        st.header("Visualizations")

        st.subheader("Joint Operation vs Joint Venture — Balance Sheet Presentation")
        fig = go.Figure()
        categories_jv = ["Joint Operation\n(line-by-line)", "Joint Venture\n(equity method)"]
        assets_shown = [5000000, 0]
        investment_shown = [0, 3250000]
        fig.add_trace(go.Bar(x=categories_jv, y=assets_shown, name="Assets/Liabilities Shown Directly", marker_color="#2563EB"))
        fig.add_trace(go.Bar(x=categories_jv, y=investment_shown, name="Single 'Investment' Line", marker_color="#10B981"))
        fig.update_layout(barmode="stack", title="Balance Sheet Presentation — Joint Operation vs Joint Venture", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Classification Decision Framework")
        labels_jo = ["Joint Arrangement", "No Separate Vehicle", "Separate Vehicle", "Rights to Assets/Liabilities", "Rights to Net Assets Only"]
        parents_jo = ["", "Joint Arrangement", "Joint Arrangement", "Separate Vehicle", "Separate Vehicle"]
        values_jo = [100, 40, 60, 25, 35]
        fig2 = go.Figure(go.Treemap(labels=labels_jo, parents=parents_jo, values=values_jo,
                                     marker_colors=["#1B3A6B","#34D399","#6366F1","#34D399","#F59E0B"]))
        fig2.update_layout(title="Joint Arrangement Classification Pathways", height=400)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Joint control under IFRS 11 requires:**")
        q1 = st.radio("", ["Exactly 50% ownership by each party", "Contractually agreed sharing of control requiring unanimous consent for key decisions", "Board majority by one party", "Equal profit sharing only"], key="ifrs11q1")
        if st.button("Check Answer", key="ifrs11c1"):
            if q1 == "Contractually agreed sharing of control requiring unanimous consent for key decisions":
                st.success("✅ Correct! Joint control exists when decisions about relevant activities require UNANIMOUS CONSENT of the parties sharing control — this is contractually established, not just based on ownership percentage.")
            else:
                st.error("❌ Joint control = contractual sharing requiring UNANIMOUS CONSENT for relevant activity decisions, not simply 50/50 ownership.")

        st.markdown("---")
        st.markdown("**2. A joint arrangement NOT structured through a separate vehicle is classified as:**")
        q2 = st.radio("", ["Always a Joint Venture", "Always a Joint Operation", "Depends on contractual terms", "Not within IFRS 11 scope"], key="ifrs11q2")
        if st.button("Check Answer", key="ifrs11c2"):
            if q2 == "Always a Joint Operation":
                st.success("✅ Correct! Without a separate vehicle, the parties automatically have direct rights to assets and obligations for liabilities — this is automatically classified as a JOINT OPERATION.")
            else:
                st.error("❌ No separate vehicle = automatic JOINT OPERATION classification — no further assessment needed.")

        st.markdown("---")
        st.markdown("**3. A joint venturer accounts for its interest in a joint venture using:**")
        q3 = st.radio("", ["Proportionate consolidation", "The equity method", "Full consolidation", "Fair value through P&L"], key="ifrs11q3")
        if st.button("Check Answer", key="ifrs11c3"):
            if q3 == "The equity method":
                st.success("✅ Correct! Joint ventures are accounted for using the EQUITY METHOD per IAS 28 — a single line investment, NOT proportionate consolidation (which was eliminated under IFRS 11, replacing the old IAS 31).")
            else:
                st.error("❌ Joint ventures use the EQUITY METHOD (IAS 28). Proportionate consolidation was eliminated when IFRS 11 replaced IAS 31.")

        st.markdown("---")
        st.markdown("**4. A separate vehicle can still be classified as a Joint Operation if:**")
        q4 = st.radio("", ["The vehicle is incorporated in a tax haven", "The legal form, contractual terms and facts indicate parties have rights to assets and obligations for liabilities", "The vehicle has fewer than 2 employees", "One party owns more than the other"], key="ifrs11q4")
        if st.button("Check Answer", key="ifrs11c4"):
            if q4 == "The legal form, contractual terms and facts indicate parties have rights to assets and obligations for liabilities":
                st.success("✅ Correct! Even with a separate vehicle, if the SUBSTANCE (contractual terms, facts and circumstances) shows the parties have direct rights to assets and liabilities — not just net assets — it remains a Joint Operation.")
            else:
                st.error("❌ Substance over form: separate vehicle + rights to assets/obligations for liabilities (per contractual terms) = still a JOINT OPERATION.")

        st.markdown("---")
        st.markdown("**5. In a Joint Operation, a joint operator recognises in its own financial statements:**")
        q5 = st.radio("", ["Only its investment in the joint operation", "Its share of assets, liabilities, revenues and expenses directly (line-by-line)", "Nothing until the arrangement is dissolved", "100% of all joint operation items"], key="ifrs11q5")
        if st.button("Check Answer", key="ifrs11c5"):
            if q5 == "Its share of assets, liabilities, revenues and expenses directly (line-by-line)":
                st.success("✅ Correct! A joint operator recognises its OWN SHARE of assets, liabilities, revenues and expenses directly on its own financial statements — this differs fundamentally from the equity method used for joint ventures.")
            else:
                st.error("❌ Joint operators recognise their SHARE of each line item (assets, liabilities, revenue, expenses) directly — not via a single investment line, and not 100%.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Joint Control Definition
        Contractually agreed sharing of control requiring **unanimous consent** for decisions about relevant activities.

        ### 2. Two Types — The Critical Distinction
        | Type | Rights/Obligations | Accounting |
        |---|---|---|
        | **Joint Operation** | Rights to assets + obligations for liabilities | Recognise SHARE of each item directly |
        | **Joint Venture** | Rights to NET ASSETS only | EQUITY METHOD (IAS 28) |

        ### 3. Classification Process
        ```
        No separate vehicle → AUTOMATIC Joint Operation

        Separate vehicle → Assess:
          - Legal form
          - Contractual terms
          - Other facts/circumstances (e.g., output taken proportionally)
          → Could STILL be Joint Operation despite separate vehicle
        ```

        ### 4. Accounting Summary
        | | Joint Operation | Joint Venture |
        |---|---|---|
        | Balance sheet | Share of each asset/liability | Single "Investment in JV" line |
        | P&L | Share of revenue/expenses | Single "Share of profit" line |
        | Method | Line-by-line (own share) | Equity method |
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Joint Control = Unanimous consent required (contractual)
No Separate Vehicle → AUTOMATIC Joint Operation
Separate Vehicle → Assess substance (could still be Joint Operation)
Joint Operation → Recognise SHARE of assets/liabilities/revenue/expenses directly
Joint Venture → EQUITY METHOD (single line, IAS 28)
NO proportionate consolidation under IFRS 11 (eliminated from old IAS 31)
        """)

        st.success("🎓 **IFRS 11 Complete!** You can now classify joint arrangements and apply the correct accounting treatment for joint operations and joint ventures.")
        st.info("💡 **Next**: IFRS 12 — Disclosure of Interests in Other Entities")

if __name__ == "__main__":
    show()