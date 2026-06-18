import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("⚖️ IAS 32: Financial Instruments: Presentation")
    st.markdown("*Master the classification of financial instruments as debt or equity, and the offsetting rules*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Scope")
        st.markdown("""
        **IAS 32** establishes principles for **presenting** financial instruments as liabilities or equity and for **offsetting** 
        financial assets and liabilities. It works alongside IFRS 9 (recognition/measurement) and IFRS 7 (disclosures).

        IAS 32 applies to all types of financial instruments EXCEPT:
        - Interests in subsidiaries, associates, JVs (IFRS 10, IAS 27, IAS 28)
        - Employer benefit plans (IAS 19)
        - Insurance contracts (IFRS 17)
        - Share-based payment transactions (IFRS 2)
        """)

        st.subheader("2. Key Definitions")
        defs = pd.DataFrame({
            "Term": ["Financial Instrument", "Financial Asset", "Financial Liability", "Equity Instrument"],
            "Definition": [
                "Any contract that gives rise to a financial asset of one entity and a financial liability or equity instrument of another",
                "Cash; contractual right to receive cash/financial asset; contractual right to exchange on favourable terms; equity instrument of another entity",
                "Contractual obligation to deliver cash/financial asset OR to exchange on potentially unfavourable terms",
                "Any contract that evidences a residual interest in the assets of an entity after deducting all of its liabilities"
            ]
        })
        st.dataframe(defs, use_container_width=True, hide_index=True)

        st.subheader("3. Liability vs Equity — The Critical Distinction")
        st.markdown("""
        **The classification is determined by the SUBSTANCE of the contractual arrangement, not its legal form.**

        **Financial Liability** if the instrument contains a contractual obligation to:
        - Deliver cash or another financial asset to another entity, OR
        - Exchange financial assets/liabilities under potentially unfavourable conditions

        **Equity Instrument** if:
        - The instrument evidences a residual interest in net assets
        - There is NO contractual obligation to deliver cash or another financial asset
        - If settled in own shares: fixed number of own shares for a fixed amount of cash (the "fixed-for-fixed" test)
        """)

        st.subheader("4. Preference Shares — Liability or Equity?")
        pref_data = pd.DataFrame({
            "Feature": [
                "Mandatory redeemable preference shares",
                "Non-redeemable preference shares with discretionary dividends",
                "Non-redeemable preference shares with mandatory dividends",
                "Convertible preference shares (fixed shares for fixed cash)"
            ],
            "Classification": ["Liability", "Equity", "Liability", "Equity (if fixed-for-fixed)"],
            "Reason": [
                "Contractual obligation to repay cash at redemption date",
                "No obligation to pay dividends or return capital",
                "Contractual obligation to pay mandatory dividends",
                "Fixed-for-fixed test met → equity"
            ]
        })
        st.dataframe(pref_data, use_container_width=True, hide_index=True)

        st.subheader("5. Compound Financial Instruments")
        st.markdown("""
        A **compound financial instrument** contains both a liability component and an equity component.

        **Example:** Convertible bond — the holder can convert to shares.

        **Split accounting at issuance:**
        1. Calculate the **liability component** = PV of contractual cash flows discounted at market rate for equivalent non-convertible debt
        2. **Equity component** = Issue proceeds − Liability component (residual)

        No gain or loss arises on initial recognition or conversion.

        **Dividends on instruments classified as liability** → P&L expense (finance cost)
        **Dividends on instruments classified as equity** → deducted from equity, not P&L
        """)

        st.subheader("6. Offsetting Financial Assets and Liabilities")
        st.markdown("""
        **Offset and present NET only when BOTH conditions are met:**
        1. The entity has a **legally enforceable right** to offset the amounts, AND
        2. The entity **intends** to settle on a net basis OR to realise the asset and settle the liability simultaneously

        **Both conditions must be met — failing either means gross presentation.**

        Common scenarios where offset is NOT permitted:
        - Master netting agreements where settlement is not simultaneous
        - Different counterparties
        - Contingent right of offset
        """)

        st.subheader("7. Treasury Shares")
        st.markdown("""
        When an entity reacquires its own equity instruments (treasury shares):
        - **Deducted from equity** — never recognised as a financial asset
        - No gain or loss recognised in P&L on purchase, sale, issue or cancellation of treasury shares
        - Consideration paid/received → directly in equity
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Compound Financial Instrument — Convertible Bond")
        st.markdown("""
        **Facts:**
        - $1,000,000 convertible bond issued at par, 3% coupon, 3-year term
        - Market rate for equivalent non-convertible bond = 8%
        - Conversion option: convert to 50,000 ordinary shares at any time

        **Step 1 — Calculate Liability Component (PV at 8%):**
        """)
        bond_data = pd.DataFrame({
            "Year": [1, 2, 3, "Total"],
            "Cash Flow ($)": [30000, 30000, 1030000, ""],
            "Discount Factor (8%)": [0.9259, 0.8573, 0.7938, ""],
            "PV ($)": [27778, 25720, 817614, "871,112"]
        })
        st.dataframe(bond_data, use_container_width=True, hide_index=True)
        st.markdown("""
        **Step 2 — Equity Component:**
        - Issue proceeds: $1,000,000
        - Less: Liability component: ($871,112)
        - **Equity component (conversion option): $128,888**

        **Journal at issue:**
        ```
        Dr  Cash                     $1,000,000
            Cr  Financial Liability       $871,112
            Cr  Equity (conversion opt)  $128,888
        ```
        """)

        st.subheader("Example 2: Preference Shares — Substance over Form")
        st.markdown("""
        | Type of Preference Share | Classification | Dividend Treatment |
        |---|---|---|
        | Redeemable at fixed date, 6% mandatory dividend | **Liability** | Finance cost in P&L |
        | Non-redeemable, dividend at directors' discretion | **Equity** | Deducted from equity |
        | Non-redeemable, 5% mandatory cumulative dividend | **Liability** | Finance cost in P&L |
        | Convertible to fixed number of shares for fixed cash | **Equity** | Deducted from equity |

        The legal label "preference share" is irrelevant — it is the contractual terms that determine classification.
        """)

        st.subheader("Example 3: Offsetting — Permitted vs Not Permitted")
        st.markdown("""
        | Scenario | Offset Permitted? | Reason |
        |---|---|---|
        | Bank account asset $500k and overdraft $200k — same bank, simultaneous settlement | ✅ YES | Legal right + simultaneous settlement intended |
        | Trade receivable from Customer A $300k and payable to Customer A $100k | ❌ NO | Typically no legal right to offset trade balances |
        | Derivative asset $50k and derivative liability $30k under master netting agreement — settle gross | ❌ NO | No intent to settle net |
        | Tax asset and tax liability with same authority, same entity | ✅ YES | IAS 12 criteria met |
        """)

        st.subheader("Example 4: Interest/Dividends — P&L vs Equity")
        st.markdown("""
        **Classification drives the income statement treatment:**

        | Instrument | Classification | Distribution Treatment |
        |---|---|---|
        | 6% redeemable preference shares | Liability | 6% dividend = **finance cost in P&L** |
        | Ordinary shares | Equity | Dividend = **deducted from retained earnings** |
        | Convertible notes | Compound | Interest on liability part = P&L; no P&L for equity part |
        | Mandatorily redeemable bonds | Liability | All coupon payments = **finance cost in P&L** |
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Liability or Equity Classifier")
        st.markdown("Classify a financial instrument based on its key features:")

        col1, col2 = st.columns(2)
        with col1:
            mandatory_redeem = st.checkbox("Mandatory redemption date (entity must repay cash)?")
            mandatory_dividend = st.checkbox("Mandatory fixed dividend (contractually obligated)?")
            convertible = st.checkbox("Convertible to shares?")
            if convertible:
                fixed_for_fixed = st.checkbox("Fixed number of shares for fixed amount of cash? (fixed-for-fixed)")

        with col2:
            if mandatory_redeem or mandatory_dividend:
                st.error("📌 **FINANCIAL LIABILITY** — Contractual obligation to deliver cash exists")
                if mandatory_dividend:
                    st.markdown("→ Mandatory dividends = **finance cost in P&L**")
                if mandatory_redeem:
                    st.markdown("→ Redemption = **liability on balance sheet**")
            elif convertible and fixed_for_fixed:
                st.info("📌 **EQUITY INSTRUMENT** — Fixed-for-fixed test met; conversion option is equity")
            elif convertible and not fixed_for_fixed:
                st.warning("📌 **FINANCIAL LIABILITY** — Variable shares or variable cash → does not meet fixed-for-fixed")
            else:
                st.success("📌 **EQUITY INSTRUMENT** — No contractual obligation to deliver cash; residual interest")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Compound Instrument — Split Calculator")
        st.markdown("Calculate the liability and equity components of a convertible bond:")

        col1, col2 = st.columns(2)
        with col1:
            face_value = st.number_input("Face value / issue proceeds ($)", value=1000000, step=10000)
            coupon_rate = st.number_input("Coupon rate (%)", value=3.0, step=0.5) / 100
            years_cv = st.number_input("Term (years)", value=3, min_value=1, max_value=30)
            market_rate = st.number_input("Market rate for equivalent non-convertible debt (%)", value=8.0, step=0.5) / 100

        with col2:
            annual_coupon = face_value * coupon_rate
            pv_coupons = sum([annual_coupon / (1 + market_rate)**t for t in range(1, int(years_cv) + 1)])
            pv_principal = face_value / (1 + market_rate)**years_cv
            liability_comp = pv_coupons + pv_principal
            equity_comp = face_value - liability_comp

            st.markdown(f"""
            | Component | Amount |
            |---|---|
            | PV of coupon payments | ${pv_coupons:,.0f} |
            | PV of principal repayment | ${pv_principal:,.0f} |
            | **Liability Component** | **${liability_comp:,.0f}** |
            | Issue Proceeds | ${face_value:,.0f} |
            | **Equity Component (residual)** | **${equity_comp:,.0f}** |
            | Equity as % of proceeds | {equity_comp/face_value*100:.1f}% |
            """)

        st.markdown("---")
        st.subheader("🔧 Tool 3: Offset Eligibility Checker")
        legal_right = st.checkbox("Does a legally enforceable right to offset exist?")
        same_counterparty = st.checkbox("Same counterparty for both asset and liability?")
        net_settlement = st.checkbox("Entity intends to settle net OR settle simultaneously?")

        if st.button("Check Offset Eligibility"):
            if legal_right and net_settlement:
                st.success("✅ **OFFSET PERMITTED** — Both IAS 32 conditions are satisfied. Present the net amount.")
            else:
                missing = []
                if not legal_right:
                    missing.append("No legally enforceable right to offset")
                if not net_settlement:
                    missing.append("No intent to settle net or simultaneously")
                st.error(f"❌ **GROSS PRESENTATION REQUIRED** — Missing: {'; '.join(missing)}")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Visualizations")

        st.subheader("Compound Instrument — Liability vs Equity Split at Different Market Rates")
        market_rates = [4, 5, 6, 7, 8, 9, 10, 11, 12]
        face = 1000000; coupon = 30000; yrs = 3
        liab_vals = []
        equity_vals = []
        for mr in market_rates:
            r = mr / 100
            pv_c = sum([coupon / (1 + r)**t for t in range(1, yrs + 1)])
            pv_p = face / (1 + r)**yrs
            lv = pv_c + pv_p
            liab_vals.append(lv)
            equity_vals.append(face - lv)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=market_rates, y=liab_vals, name="Liability Component", marker_color="#2563EB"))
        fig.add_trace(go.Bar(x=market_rates, y=equity_vals, name="Equity Component", marker_color="#10B981"))
        fig.update_layout(barmode="stack", title="Convertible Bond — Split at Different Market Rates ($1M face, 3% coupon)",
                          xaxis_title="Market Rate (%)", yaxis_title="Amount ($)", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Preference Share Classification Decision Tree")
        labels = ["Preference Share", "Mandatory Redemption?", "Liability", "Mandatory Dividend?",
                  "Liability (dividend clause)", "Equity", "Convertible? Fixed-for-fixed?", "Equity", "Liability (variable)"]
        parents = ["", "Preference Share", "Mandatory Redemption?", "Mandatory Redemption?",
                   "Mandatory Dividend?", "Mandatory Dividend?", "Mandatory Dividend?",
                   "Convertible? Fixed-for-fixed?", "Convertible? Fixed-for-fixed?"]
        values = [100, 40, 40, 60, 20, 25, 15, 10, 5]
        fig2 = go.Figure(go.Treemap(labels=labels, parents=parents, values=values,
                                     marker_colors=["#1B3A6B","#6366F1","#F87171","#6366F1","#F87171","#34D399","#F59E0B","#34D399","#F87171"]))
        fig2.update_layout(title="Preference Share Classification Framework", height=400)
        st.plotly_chart(fig2, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IAS 32, the classification of a financial instrument as liability or equity is based on:**")
        q1 = st.radio("", [
            "Its legal form (e.g., if it says 'share' it is equity)",
            "Management's intention at the time of issue",
            "The substance of the contractual arrangement",
            "The accounting standards of the country of incorporation"
        ], key="ias32q1")
        if st.button("Check Answer", key="ias32c1"):
            if q1 == "The substance of the contractual arrangement":
                st.success("✅ Correct! IAS 32 requires classification based on SUBSTANCE, not legal form. A preference share may be a liability if it carries mandatory redemption or mandatory dividends.")
            else:
                st.error("❌ Incorrect. IAS 32 uses SUBSTANCE over form. Legal labels are irrelevant — contractual terms determine classification.")

        st.markdown("---")
        st.markdown("**2. Mandatorily redeemable preference shares should be classified as:**")
        q2 = st.radio("", [
            "Equity — they are shares",
            "Financial liability — there is a contractual obligation to repay cash",
            "Compound instrument — split into liability and equity",
            "Either equity or liability — management's choice"
        ], key="ias32q2")
        if st.button("Check Answer", key="ias32c2"):
            if q2 == "Financial liability — there is a contractual obligation to repay cash":
                st.success("✅ Correct! Mandatory redemption creates a contractual obligation to deliver cash → Financial Liability, regardless of the 'share' label.")
            else:
                st.error("❌ Mandatorily redeemable preference shares = Financial Liability because of the obligation to repay cash.")

        st.markdown("---")
        st.markdown("**3. For a compound financial instrument (e.g., convertible bond), the equity component is:**")
        q3 = st.radio("", [
            "The full face value of the bond",
            "Zero — convertible bonds are purely liabilities",
            "The residual after deducting the liability component from the proceeds",
            "The present value of the conversion option at market price"
        ], key="ias32q3")
        if st.button("Check Answer", key="ias32c3"):
            if q3 == "The residual after deducting the liability component from the proceeds":
                st.success("✅ Correct! Split accounting: calculate liability component first (PV of cash flows at market rate), then equity = proceeds minus liability component.")
            else:
                st.error("❌ Equity component = Issue proceeds − Liability component (PV of contractual cash flows at market rate for non-convertible debt).")

        st.markdown("---")
        st.markdown("**4. Financial assets and liabilities may be offset when:**")
        q4 = st.radio("", [
            "Management decides it is more informative",
            "Both parties agree to present net amounts",
            "There is a legally enforceable right to offset AND intent to settle net or simultaneously",
            "The amounts relate to the same counterparty"
        ], key="ias32q4")
        if st.button("Check Answer", key="ias32c4"):
            if q4 == "There is a legally enforceable right to offset AND intent to settle net or simultaneously":
                st.success("✅ Correct! IAS 32 requires BOTH conditions: (1) legally enforceable right AND (2) intent to settle net or simultaneously. Failing either = gross presentation.")
            else:
                st.error("❌ Both conditions must be met: (1) legal right to offset + (2) intent to settle net or simultaneously.")

        st.markdown("---")
        st.markdown("**5. Dividends paid on instruments classified as financial liabilities are presented in P&L as:**")
        q5 = st.radio("", [
            "Distribution of equity",
            "Finance costs (interest expense)",
            "Other comprehensive income",
            "Not recognised in the financial statements"
        ], key="ias32q5")
        if st.button("Check Answer", key="ias32c5"):
            if q5 == "Finance costs (interest expense)":
                st.success("✅ Correct! Dividends on instruments classified as liabilities = finance costs in P&L (same as interest). This follows the substance-over-form principle.")
            else:
                st.error("❌ Dividends on liability-classified instruments = finance costs in P&L. Only dividends on equity instruments are deducted from equity.")

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Core Principle
        **Substance over form** — classification as liability or equity follows the contractual terms, not the legal label.

        ### 2. Financial Liability vs Equity
        | Financial Liability | Equity Instrument |
        |---|---|
        | Contractual obligation to deliver cash | No obligation to deliver cash |
        | Mandatory redeemable shares | Non-redeemable, discretionary dividend shares |
        | Mandatory dividend preference shares | Fixed-for-fixed convertibles |
        | Variable-for-fixed convertibles | Ordinary shares |

        ### 3. Compound Instruments — Split Accounting
        ```
        Liability Component = PV of contractual cash flows at market rate (non-convertible)
        Equity Component    = Issue Proceeds − Liability Component
        ```

        ### 4. Dividends / Interest — P&L vs Equity
        | Classification | Distribution Treatment |
        |---|---|
        | Liability | Finance cost in **P&L** |
        | Equity | Deducted from **equity** |

        ### 5. Offsetting — Two Conditions (BOTH required)
        1. **Legally enforceable right** to offset
        2. **Intent to settle net** or simultaneously

        ### 6. Treasury Shares
        - Reacquired own shares → **deducted from equity** (never a financial asset)
        - No P&L gain/loss on treasury share transactions
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Substance over Form — always classify by contractual terms
Mandatory cash obligation (redemption/dividend) → LIABILITY
Fixed-for-fixed convertible → EQUITY
Dividends on liability instruments → P&L (finance cost)
Dividends on equity instruments → deducted from equity
Offset: need BOTH legal right AND net settlement intent
Treasury shares → deduct from equity, never a financial asset
        """)

        st.success("🎓 **IAS 32 Complete!** You can now classify financial instruments, apply compound instrument split accounting, and determine offset eligibility.")
        st.info("💡 **Next**: IAS 36 — Impairment of Assets")

if __name__ == "__main__":
    show()