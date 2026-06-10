import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📊 Deferred Tax: Complete Guide under IAS 12")
    st.markdown("*Based on IAS 12 — Income Taxes (International Accounting Standard)*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Concepts", "🧮 Examples", "💡 Interactive Calculator",
        "✅ Quiz", "📝 Summary"
    ])

    # ─────────────────────────────────────────────────────────────────
    # TAB 1: THEORY
    # ─────────────────────────────────────────────────────────────────
    with tab1:
        st.header("Theory & Conceptual Framework")

        st.subheader("1. What is Deferred Tax?")
        st.markdown("""
        **Deferred Tax** arises from **temporary differences** between:
        - The **carrying amount** of an asset or liability in the **financial statements (IFRS/GAAP)**, and
        - Its **tax base** — the amount attributed to that asset or liability for **tax purposes**.

        > 💡 *Key Insight*: Accounting profit and taxable profit are **rarely equal**. This mismatch creates
        > a timing difference — tax is being paid earlier or later than the accounting expense/income is recognised.
        > Deferred tax **bridges this gap**, ensuring the tax charge in the income statement matches the accounting profit.

        **IAS 12 Objective:**
        > *"To prescribe the accounting treatment for income taxes — including all domestic and foreign taxes
        > based on taxable profits, as well as withholding taxes payable by a subsidiary."*
        """)

        st.subheader("2. Core Definitions")
        col1, col2 = st.columns(2)
        with col1:
            st.info("""
            **Tax Base of an Asset**
            The amount deductible for tax purposes against any taxable economic benefits
            that will flow to the entity when it recovers the carrying amount.

            *Formula:*
            `Tax Base = Future Tax Deductions Available`
            """)
            st.info("""
            **Deferred Tax Liability (DTL)**
            Taxes payable in **future periods** in respect of taxable temporary differences.
            They arise when the carrying amount > tax base (for assets) or
            carrying amount < tax base (for liabilities).
            """)
            st.info("""
            **Taxable Temporary Difference**
            A temporary difference that will result in **taxable amounts** in future
            periods (when the asset is recovered or liability is settled).
            → Gives rise to a **Deferred Tax Liability (DTL)**
            """)
        with col2:
            st.info("""
            **Tax Base of a Liability**
            The carrying amount of a liability **minus** any amounts deductible for tax
            purposes in future periods.

            *Formula:*
            `Tax Base = Carrying Amount − Future Tax Deductions`
            """)
            st.info("""
            **Deferred Tax Asset (DTA)**
            Taxes **recoverable** in future periods in respect of:
            - Deductible temporary differences
            - Carried forward unused tax losses
            - Carried forward unused tax credits
            """)
            st.info("""
            **Deductible Temporary Difference**
            A temporary difference that will result in amounts that are **deductible**
            in future periods (when the asset is recovered or liability is settled).
            → Gives rise to a **Deferred Tax Asset (DTA)**
            """)

        st.subheader("3. The Temporary Difference Approach (Balance Sheet Method)")
        st.markdown("""
        IAS 12 uses the **Balance Sheet Method** (also called the liability method):

        ```
        Temporary Difference  =  Carrying Amount  −  Tax Base

        If Temporary Difference is POSITIVE (CA > TB):
            For an ASSET      →  Taxable Temporary Difference  →  DTL
            For a LIABILITY   →  Deductible Temporary Difference →  DTA

        If Temporary Difference is NEGATIVE (CA < TB):
            For an ASSET      →  Deductible Temporary Difference →  DTA
            For a LIABILITY   →  Taxable Temporary Difference  →  DTL
        ```

        **Key Formula:**
        ```
        Deferred Tax Liability / Asset  =  Temporary Difference  ×  Applicable Tax Rate
        ```
        """)

        # Visual diagram of the concept
        st.markdown("#### Visual: How Temporary Differences Create Deferred Tax")
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Carrying Amount (CA)', x=['PPE Example'], y=[100], marker_color='#2196F3'))
        fig.add_trace(go.Bar(name='Tax Base (TB)', x=['PPE Example'], y=[60], marker_color='#FF9800'))
        fig.add_annotation(x=0, y=80, text="Taxable Temp Diff = 40<br>→ DTL = 40 × 30% = 12",
                           showarrow=True, arrowhead=2, bgcolor="lightyellow", bordercolor="gray")
        fig.update_layout(barmode='group', title='Example: CA > TB → Taxable Temp Difference → DTL',
                          yaxis_title='Amount (BDT/USD)', height=350)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("4. Recognition Rules — When to Recognise DTL and DTA")

        st.markdown("#### Deferred Tax Liabilities (DTL)")
        st.markdown("""
        **General Rule (IAS 12.15):** A DTL shall be recognised for **all taxable temporary differences** EXCEPT:

        | Exception | Explanation |
        |-----------|-------------|
        | Initial recognition of goodwill | Not recognised as DTL on goodwill arising from business combination |
        | Initial recognition exemption | Asset/liability arose from a transaction that is NOT a business combination AND at time of transaction affected neither accounting profit nor taxable profit |
        | Investments in subsidiaries, branches, associates, JVs | Where parent can control timing of reversal AND it is probable that the difference will NOT reverse in the foreseeable future |
        """)

        st.markdown("#### Deferred Tax Assets (DTA)")
        st.markdown("""
        **General Rule (IAS 12.24):** A DTA shall be recognised for all **deductible temporary differences**
        to the extent that it is **probable** that sufficient taxable profit will be available against which
        the deductible temporary difference can be utilised.

        **Probability Test — Evidence to Consider:**
        - Future taxable profits from existing assets
        - Tax planning opportunities available
        - Reversal of existing DTLs in the same period
        - Historical profitability track record

        > ⚠️ *Critical Point*: If it is NOT probable that sufficient taxable profit will be available,
        > the DTA must NOT be recognised (or must be partially written down).
        """)

        st.markdown("#### Tax Losses Carried Forward")
        st.markdown("""
        **IAS 12.34–35:** A DTA shall be recognised for carried-forward unused tax losses and unused tax credits
        to the extent it is **probable** that future taxable profit will be available.

        Evidence of probable future profit is **stronger** when:
        - Losses arose from identifiable, non-recurring causes
        - The entity has a history of profitability
        - Taxable temporary differences will reverse in the same period as the losses
        - Tax planning strategies are available
        """)

        st.subheader("5. Measurement of Deferred Tax")
        st.markdown("""
        **IAS 12.46–52:**

        | Aspect | Rule |
        |--------|------|
        | Tax Rate | Use the rate that is **expected to apply** when the asset is realised / liability is settled |
        | Rate Changes | If rate is enacted/substantially enacted by balance sheet date, use new rate |
        | Discounting | **NOT permitted** — deferred tax is NOT discounted to present value |
        | Asset vs. Liability | Deferred tax assets should not exceed deferred tax liabilities without a strong probable taxable profit test |
        | Different Tax Rates | Use the rate applicable to the manner of recovery/settlement (e.g. capital gains rate vs income tax rate) |

        **Rate Used — Decision Framework:**
        ```
        If tax rate is already enacted or substantially enacted by year-end → use NEW rate
        If tax rate change is only proposed (not yet enacted)              → use EXISTING rate
        ```
        """)

        st.subheader("6. Presentation: Current vs Deferred Tax")
        st.markdown("""
        **In the Income Statement:**
        ```
        Profit before tax                         XXX
        Income tax expense:
            Current tax                           (XX)
            Deferred tax:
                Origination of temp differences   (XX)
                Reversal of temp differences       XX
        Total income tax expense                  (XX)
        Profit after tax                          XXX
        ```

        **In the Balance Sheet:**
        - Deferred Tax Assets → Non-current Assets
        - Deferred Tax Liabilities → Non-current Liabilities
        - **Offset is permitted** (IAS 12.74) only when the entity has a legally enforceable right to offset
          AND the deferred taxes relate to income taxes levied by the same taxation authority on the same entity.
        """)

        st.subheader("7. Deferred Tax in Other Comprehensive Income (OCI)")
        st.markdown("""
        **IAS 12.61A:** Current and deferred tax shall be recognised **outside profit or loss**
        (i.e., in OCI or directly in equity) if the tax relates to items that are recognised outside profit or loss.

        **Common OCI items triggering deferred tax:**

        | OCI Item | Deferred Tax Treatment |
        |----------|------------------------|
        | Revaluation surplus (PPE) | DTL recognised in OCI |
        | Actuarial gains/losses (pensions) | DTA/DTL recognised in OCI |
        | Fair value gains — FVOCI investments | DTL recognised in OCI |
        | Cash flow hedge — effective portion | DTA/DTL recognised in OCI |
        | Foreign currency translation reserve | Usually not recognised (investment in subsidiary exception) |

        > 📌 *Rule*: The tax follows the item. If the gain/loss goes to OCI, so does the deferred tax.
        """)

        st.subheader("8. Deferred Tax on Business Combinations")
        st.markdown("""
        **IFRS 3 & IAS 12 interaction:**

        When an entity acquires another in a business combination, assets and liabilities are recognised
        at **fair value**. If the fair value differs from the tax base:

        - **Fair Value > Tax Base** → Taxable temporary difference → **DTL recognised**
        - **Fair Value < Tax Base** → Deductible temporary difference → **DTA recognised** (if probable)

        **Special rule for Goodwill:**
        - No DTL is recognised on initial recognition of goodwill (IAS 12.15(a))
        - But if goodwill is deductible for tax (e.g. in certain jurisdictions), subsequent differences
          may arise and need accounting

        **Deferred tax in a business combination directly adjusts goodwill:**
        ```
        Goodwill = Consideration Paid − FV of Net Assets Acquired (after DT)
        ```
        """)

        st.subheader("9. Intra-group Transactions and Deferred Tax")
        st.markdown("""
        When consolidating, intra-group profit elimination creates temporary differences:

        - **Upstream sale**: Subsidiary sells inventory to Parent at a profit → Parent holds inventory at inflated price
        - On consolidation, unrealised profit is eliminated → **CA of inventory reduced < tax base**
        - → **Deductible Temporary Difference → DTA** (taxed at buyer entity's rate)

        > 💡 The DTA is recognised at the **buyer's** tax rate under IAS 12.68.
        """)

        st.subheader("10. Deferred Tax — Investments in Subsidiaries, Associates & JVs")
        st.markdown("""
        **IAS 12.38–45:** Taxable temporary differences arise from:
        - Undistributed profits of subsidiaries/associates/JVs
        - Foreign exchange translation differences

        **DTL Recognition:**
        - A parent shall recognise a DTL on these differences **UNLESS:**
          - The parent is able to control the timing of the reversal, **AND**
          - It is probable the temporary difference will **NOT reverse** in the foreseeable future

        **DTA Recognition:**
        - Only when it is probable that the temporary difference will reverse in the foreseeable future
          AND sufficient taxable profit will be available.
        """)

        st.subheader("11. Deferred Tax — Reassessment and Change in Tax Rate")
        st.markdown("""
        **Reassessment at each balance sheet date (IAS 12.37):**
        - An entity **reassesses** unrecognised DTAs at each balance sheet date
        - If it becomes probable that sufficient future taxable profit will be available,
          a previously unrecognised DTA is now recognised

        **Impact of Tax Rate Change:**
        - When a new tax rate is **enacted or substantially enacted**, all existing DTAs and DTLs
          are remeasured at the **new rate**
        - The difference flows through the **income statement** (unless the underlying item was in OCI)

        ```
        Impact on P&L = (Old DTA/DTL balance) × (New Rate − Old Rate) / Old Rate
        ```
        """)

    # ─────────────────────────────────────────────────────────────────
    # TAB 2: EXAMPLES
    # ─────────────────────────────────────────────────────────────────
    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Accelerated Tax Depreciation (Most Common DTL)")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A company purchases equipment for **BDT 1,000,000** on 1 January Year 1.

            - **Accounting (IFRS):** Straight-line over 5 years → Annual depreciation = BDT 200,000
            - **Tax:** Accelerated depreciation — 40% reducing balance allowed
            - **Tax Rate:** 30%

            **Year 1 Working:**
            | | Accounting | Tax |
            |-|-----------|-----|
            | Cost | 1,000,000 | 1,000,000 |
            | Depreciation | (200,000) | (400,000) |
            | **Year-end value** | **800,000** | **600,000** |
            | Temporary Difference | | 200,000 (taxable) |
            | **DTL = 200,000 × 30%** | | **= BDT 60,000** |

            **Journal Entry — Year 1:**
            ```
            Dr  Income Tax Expense (Deferred)    60,000
                Cr  Deferred Tax Liability           60,000
            ```

            **Year 2 Working:**
            | | Accounting | Tax |
            |-|-----------|-----|
            | Opening value | 800,000 | 600,000 |
            | Depreciation | (200,000) | (240,000) |
            | **Year-end value** | **600,000** | **360,000** |
            | Cumulative Temp Diff | | 240,000 (taxable) |
            | **DTL = 240,000 × 30%** | | **= BDT 72,000** |

            Movement in DTL Year 2 = 72,000 − 60,000 = **BDT 12,000** (additional DTL)

            **The DTL reverses in later years** when accounting depreciation exceeds tax depreciation.
            """)

            # Chart showing reversal pattern
            years = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']
            ca = [800, 600, 400, 200, 0]
            tb = [600, 360, 216, 130, 0]  # approx reducing balance
            dtl = [(a - b) * 0.3 for a, b in zip(ca, tb)]
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=years, y=ca, mode='lines+markers', name='Carrying Amount', line=dict(color='blue')))
            fig2.add_trace(go.Scatter(x=years, y=tb, mode='lines+markers', name='Tax Base', line=dict(color='orange')))
            fig2.add_trace(go.Bar(x=years, y=dtl, name='DTL Balance', marker_color='red', opacity=0.5, yaxis='y2'))
            fig2.update_layout(
                title='PPE: Carrying Amount vs Tax Base and DTL Over Time',
                yaxis=dict(title='BDT (000s)'),
                yaxis2=dict(title='DTL (BDT 000s)', overlaying='y', side='right'),
                height=380
            )
            st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Example 2: Provision (Warranty) — Deferred Tax Asset")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A company recognises a **warranty provision of BDT 500,000** in Year 1.

            - **Accounting (IAS 37):** Provision recognised immediately in P&L → Carrying Amount = BDT 500,000
            - **Tax:** Warranty costs are only deductible when **actually paid** → Tax Base = BDT 0
            - **Tax Rate:** 25%

            **Analysis:**
            ```
            Carrying Amount of Liability         =  500,000
            Tax Base of Liability                =  0
            Temporary Difference (liability)     =  500,000 − 0 = 500,000

            For a LIABILITY: CA > TB → Deductible Temporary Difference → DTA
            DTA = 500,000 × 25% = BDT 125,000
            ```

            **Journal Entry — Year 1:**
            ```
            Dr  Deferred Tax Asset           125,000
                Cr  Income Tax Expense (Deferred)    125,000
            ```

            **Year 2 — Warranty Claims Paid (BDT 300,000):**
            - Provision reduces to BDT 200,000
            - Tax deduction NOW available for 300,000
            - Remaining DTA = 200,000 × 25% = **BDT 50,000**
            - DTA reduction = 125,000 − 50,000 = **BDT 75,000** → Dr Tax Expense

            > 🔑 The DTA represents the **future tax saving** when the company can actually deduct the warranty cost.
            """)

        st.subheader("Example 3: Revaluation of PPE — Deferred Tax in OCI")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A company revalues its land from cost of **BDT 2,000,000** to fair value of **BDT 3,000,000**.
            Tax base remains at cost = BDT 2,000,000. Tax rate = 30%.

            **Analysis:**
            ```
            Carrying Amount (Fair Value)   =  3,000,000
            Tax Base (Cost)                =  2,000,000
            Taxable Temporary Difference   =  1,000,000
            DTL = 1,000,000 × 30%          =  BDT 300,000
            ```

            **Journal Entries:**
            ```
            Step 1 — Record revaluation:
            Dr  Land (PPE)                    1,000,000
                Cr  Revaluation Surplus (OCI)     1,000,000

            Step 2 — Record deferred tax in OCI:
            Dr  Revaluation Surplus (OCI)       300,000
                Cr  Deferred Tax Liability          300,000
            ```

            **Net Revaluation Surplus in OCI = 1,000,000 − 300,000 = BDT 700,000**

            > 📌 The tax follows the item: because the revaluation goes to OCI, the deferred tax also goes to OCI —
            > NOT to the income statement.
            """)

        st.subheader("Example 4: Tax Loss Carried Forward — Deferred Tax Asset")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A company incurs a **tax loss of BDT 4,000,000** in Year 1. Tax rate = 25%.
            The company has forecast future profits and believes it is **probable** the loss will be utilised.

            **Recognition:**
            ```
            Unused Tax Loss                   =  4,000,000
            DTA = 4,000,000 × 25%             =  BDT 1,000,000
            ```

            **Journal Entry — Year 1:**
            ```
            Dr  Deferred Tax Asset           1,000,000
                Cr  Income Tax Expense (Deferred)    1,000,000
            ```

            **Year 2 — Taxable Profit BDT 1,500,000:**
            - Loss offset: 1,500,000 utilised → remaining loss = 2,500,000
            - Remaining DTA = 2,500,000 × 25% = **BDT 625,000**
            - DTA decrease = 1,000,000 − 625,000 = **BDT 375,000**
            ```
            Dr  Income Tax Expense           375,000
                Cr  Deferred Tax Asset           375,000
            ```

            > ⚠️ If in a later year the outlook deteriorates and it is no longer probable the loss
            > will be utilised, the DTA must be **written down** (impaired).
            """)

        st.subheader("Example 5: Tax Rate Change — Impact on Deferred Tax")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            At 31 December Year 1, an entity has:
            - DTL of BDT 200,000 (measured at 30% tax rate)
            - In December Year 1, government enacts a new tax rate of **25%** effective 1 January Year 2

            **Remeasurement (must use new enacted rate at year-end):**
            ```
            Original temporary difference = 200,000 / 30% = BDT 666,667
            Remeasured DTL at 25%         = 666,667 × 25% = BDT 166,667
            Reduction in DTL              = 200,000 − 166,667 = BDT 33,333
            ```

            **Journal Entry:**
            ```
            Dr  Deferred Tax Liability    33,333
                Cr  Income Tax Expense         33,333
            ```
            *This is a CREDIT to income tax expense — reducing the tax charge (a benefit).*
            """)

        st.subheader("Example 6: Consolidated Intra-group Elimination — Deferred Tax")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            Parent Company sells inventory to Subsidiary for BDT 800,000.
            - Cost to Parent = BDT 500,000 → Intra-group profit = BDT 300,000
            - At year-end, Subsidiary has **not yet sold** the inventory externally
            - Consolidation eliminates the BDT 300,000 unrealised profit
            - Tax rate at Subsidiary = 25%

            **Consolidated Balance Sheet:**
            ```
            Inventory (after elimination):
            Consolidated CA = 800,000 − 300,000 = 500,000
            Tax Base at Subsidiary = 800,000 (what it paid to Parent — its deductible cost)
            Deductible Temp Difference = 800,000 − 500,000 = 300,000
            DTA = 300,000 × 25% = BDT 75,000
            ```

            > 💡 The DTA is recognised because the subsidiary will get a full tax deduction on BDT 800,000
            > when it eventually sells the inventory, but profit is only BDT 500,000 in the consolidated accounts.
            """)

        st.subheader("Example 7: Business Combination — Deferred Tax on Fair Value Uplift")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            Company A acquires Company B. On acquisition:
            - Building fair value = BDT 5,000,000
            - Building tax base (NBV for tax) = BDT 3,000,000
            - Tax rate = 30%

            **Analysis:**
            ```
            Taxable Temporary Difference = 5,000,000 − 3,000,000 = 2,000,000
            DTL recognised on acquisition = 2,000,000 × 30% = BDT 600,000
            ```

            **Impact on Goodwill:**
            ```
            Consideration paid                      10,000,000
            Less: FV of net identifiable assets
                  (including DTL of 600,000)        (8,400,000)
            Goodwill                                 1,600,000
            ```

            > 📌 The DTL recognised on the fair value uplift **increases goodwill** (reduces net assets acquired).
            > No DTL is recognised on the goodwill itself (IAS 12.15(a) exception).
            """)

    # ─────────────────────────────────────────────────────────────────
    # TAB 3: INTERACTIVE CALCULATOR
    # ─────────────────────────────────────────────────────────────────
    with tab3:
        st.header("Interactive Deferred Tax Calculator")

        calc_type = st.selectbox("Select Calculation Type:", [
            "1. PPE: Accelerated Tax Depreciation",
            "2. Provision / Accrual (Deductible on Payment)",
            "3. PPE Revaluation (OCI)",
            "4. Tax Loss Carried Forward",
            "5. Full Balance Sheet Reconciliation"
        ])

        st.markdown("---")

        # ── Calculator 1: PPE Accelerated Depreciation ──
        if calc_type == "1. PPE: Accelerated Tax Depreciation":
            st.subheader("PPE: Accelerated Tax Depreciation")
            col1, col2, col3 = st.columns(3)
            with col1:
                cost = st.number_input("Asset Cost (BDT)", value=1_000_000, step=50_000)
                acctg_life = st.number_input("Accounting Useful Life (years)", value=5, min_value=1, max_value=50)
            with col2:
                tax_rate_pct = st.number_input("Tax Depreciation Rate (%)", value=40.0, step=5.0)
                inc_tax_rate = st.number_input("Income Tax Rate (%)", value=30.0, step=1.0) / 100
            with col3:
                residual = st.number_input("Residual Value (Accounting)", value=0, step=10_000)
                year_sel = st.slider("View Position at End of Year:", 1, acctg_life, 1)

            acctg_dep = (cost - residual) / acctg_life
            ca = cost - acctg_dep * year_sel

            tb = cost
            for _ in range(year_sel):
                tb = tb * (1 - tax_rate_pct / 100)

            td = ca - tb
            if td > 0:
                dt_type = "Taxable Temp Diff → **Deferred Tax Liability (DTL)**"
                dt_val = td * inc_tax_rate
                dt_label = "DTL"
            elif td < 0:
                dt_type = "Deductible Temp Diff → **Deferred Tax Asset (DTA)**"
                dt_val = abs(td) * inc_tax_rate
                dt_label = "DTA"
            else:
                dt_type = "No temporary difference"
                dt_val = 0
                dt_label = "Nil"

            st.markdown(f"""
            **At End of Year {year_sel}:**

            | Item | Amount (BDT) |
            |------|-------------|
            | Carrying Amount (Accounting NBV) | {ca:,.0f} |
            | Tax Base | {tb:,.0f} |
            | Temporary Difference | {td:,.0f} |
            | Tax Rate | {inc_tax_rate*100:.0f}% |
            | **{dt_label}** | **{dt_val:,.0f}** |

            {dt_type}
            """)

            # Build full schedule
            rows = []
            prev_dtl = 0
            for y in range(1, acctg_life + 1):
                ca_y = cost - acctg_dep * y
                tb_y = cost
                for _ in range(y):
                    tb_y = tb_y * (1 - tax_rate_pct / 100)
                td_y = ca_y - tb_y
                dtl_y = max(td_y, 0) * inc_tax_rate
                dta_y = max(-td_y, 0) * inc_tax_rate
                movement = (dtl_y - dta_y) - prev_dtl
                prev_dtl = dtl_y - dta_y
                rows.append({"Year": y, "CA": round(ca_y), "Tax Base": round(tb_y),
                             "Temp Diff": round(td_y), "DTL": round(dtl_y),
                             "DTA": round(dta_y), "Movement": round(movement)})
            df = pd.DataFrame(rows)
            st.markdown("**Full Depreciation & Deferred Tax Schedule:**")
            st.dataframe(df, use_container_width=True)

        # ── Calculator 2: Provision ──
        elif calc_type == "2. Provision / Accrual (Deductible on Payment)":
            st.subheader("Provision — Deductible Only on Payment")
            prov = st.number_input("Provision Recognised (BDT)", value=500_000, step=10_000)
            paid = st.number_input("Amount Paid to Date (BDT)", value=0, step=10_000)
            tax_rt = st.number_input("Income Tax Rate (%)", value=25.0, step=1.0) / 100

            remaining_prov = max(prov - paid, 0)
            dta = remaining_prov * tax_rt

            st.markdown(f"""
            **Analysis:**

            | Item | Amount (BDT) |
            |------|-------------|
            | Original Provision | {prov:,.0f} |
            | Already Paid (tax deductible) | {paid:,.0f} |
            | Remaining Provision (CA of liability) | {remaining_prov:,.0f} |
            | Tax Base of Liability | 0 |
            | Deductible Temp Diff | {remaining_prov:,.0f} |
            | **Deferred Tax Asset (DTA)** | **{dta:,.0f}** |

            ✅ DTA recognised because future tax deduction will be available when claims are paid.
            """)

        # ── Calculator 3: Revaluation ──
        elif calc_type == "3. PPE Revaluation (OCI)":
            st.subheader("PPE Revaluation — Deferred Tax in OCI")
            cost_base = st.number_input("Cost / Tax Base (BDT)", value=2_000_000, step=100_000)
            fair_val = st.number_input("Fair Value after Revaluation (BDT)", value=3_000_000, step=100_000)
            tax_rt = st.number_input("Income Tax Rate (%)", value=30.0, step=1.0) / 100

            uplift = fair_val - cost_base
            dtl = max(uplift, 0) * tax_rt
            net_oci = uplift - dtl

            st.markdown(f"""
            **Analysis:**

            | Item | Amount (BDT) |
            |------|-------------|
            | Fair Value | {fair_val:,.0f} |
            | Tax Base (Cost) | {cost_base:,.0f} |
            | Revaluation Uplift | {uplift:,.0f} |
            | DTL ({tax_rt*100:.0f}%) | {dtl:,.0f} |
            | **Net Revaluation Surplus (OCI)** | **{net_oci:,.0f}** |

            **Journal Entries:**
            ```
            Dr  PPE                        {uplift:,.0f}
                Cr  Revaluation Surplus (OCI)  {uplift:,.0f}

            Dr  Revaluation Surplus (OCI)  {dtl:,.0f}
                Cr  Deferred Tax Liability     {dtl:,.0f}
            ```
            *The deferred tax is recognised in OCI — not in the income statement.*
            """)

        # ── Calculator 4: Tax Loss ──
        elif calc_type == "4. Tax Loss Carried Forward":
            st.subheader("Tax Loss Carried Forward — DTA Recognition")
            tax_loss = st.number_input("Tax Loss Carried Forward (BDT)", value=4_000_000, step=100_000)
            tax_rt = st.number_input("Income Tax Rate (%)", value=25.0, step=1.0) / 100
            probable = st.radio("Is it probable that future taxable profits will be available?", ["Yes", "No"])
            if probable == "Yes":
                prob_pct = st.slider("Estimated % of loss likely to be utilised:", 0, 100, 100)
            else:
                prob_pct = 0

            utilisable = tax_loss * prob_pct / 100
            dta = utilisable * tax_rt
            unrecognised = (tax_loss - utilisable) * tax_rt

            if probable == "Yes":
                st.success(f"""
                **DTA Recognised = BDT {dta:,.0f}** (on utilisable loss of BDT {utilisable:,.0f})
                **Unrecognised DTA = BDT {unrecognised:,.0f}** (disclosed in notes)
                """)
            else:
                st.warning(f"""
                **DTA NOT recognised** — not probable that future taxable profits will be available.
                **Unrecognised DTA = BDT {dta:,.0f}** (disclose in notes per IAS 12.81(e))
                """)

        # ── Calculator 5: Full Balance Sheet Reconciliation ──
        else:
            st.subheader("Full Balance Sheet Deferred Tax Reconciliation")
            st.markdown("Enter all balance sheet items below:")

            n = st.number_input("Number of items to enter:", min_value=1, max_value=15, value=4)
            tax_rate = st.number_input("Income Tax Rate (%)", value=30.0, step=1.0) / 100

            items = []
            total_td_taxable = 0
            total_td_deductible = 0

            for i in range(int(n)):
                st.markdown(f"**Item {i+1}:**")
                c1, c2, c3 = st.columns(3)
                with c1:
                    name = st.text_input(f"Description", value=f"Item {i+1}", key=f"name_{i}")
                    item_type = st.selectbox("Asset or Liability?", ["Asset", "Liability"], key=f"type_{i}")
                with c2:
                    ca = st.number_input("Carrying Amount (BDT)", value=0, step=10_000, key=f"ca_{i}")
                    tb = st.number_input("Tax Base (BDT)", value=0, step=10_000, key=f"tb_{i}")
                with c3:
                    td = ca - tb
                    if item_type == "Asset":
                        if td > 0:
                            td_type = "Taxable → DTL"
                            total_td_taxable += td
                        elif td < 0:
                            td_type = "Deductible → DTA"
                            total_td_deductible += abs(td)
                        else:
                            td_type = "Nil"
                    else:  # Liability
                        if td > 0:
                            td_type = "Deductible → DTA"
                            total_td_deductible += td
                        elif td < 0:
                            td_type = "Taxable → DTL"
                            total_td_taxable += abs(td)
                        else:
                            td_type = "Nil"
                    st.metric("Temp Diff", f"{td:,}")
                    st.markdown(f"*{td_type}*")

                items.append({"Item": name, "CA": ca, "Tax Base": tb, "Temp Diff": td, "Type": td_type})

            st.markdown("---")
            gross_dtl = total_td_taxable * tax_rate
            gross_dta = total_td_deductible * tax_rate
            net_position = gross_dta - gross_dtl

            col1, col2, col3 = st.columns(3)
            col1.metric("Gross DTL", f"BDT {gross_dtl:,.0f}")
            col2.metric("Gross DTA", f"BDT {gross_dta:,.0f}")
            if net_position >= 0:
                col3.metric("Net DTA (after offset)", f"BDT {net_position:,.0f}", delta="Asset")
            else:
                col3.metric("Net DTL (after offset)", f"BDT {abs(net_position):,.0f}", delta="Liability")

            st.dataframe(pd.DataFrame(items), use_container_width=True)

    # ─────────────────────────────────────────────────────────────────
    # TAB 4: QUIZ
    # ─────────────────────────────────────────────────────────────────
    with tab4:
        st.header("Quiz — Test Your Knowledge of IAS 12")
        st.markdown("Answer all questions and check your score.")

        score = [0]

        # Q1
        st.markdown("---")
        st.markdown("**Q1. A machine has a carrying amount of BDT 500,000 and a tax base of BDT 350,000. Tax rate is 25%. What is the deferred tax position?**")
        q1 = st.radio("Select:", [
            "DTA of BDT 37,500",
            "DTL of BDT 37,500",
            "DTA of BDT 125,000",
            "DTL of BDT 125,000"
        ], key="ias12q1")
        if st.button("Check Answer", key="ias12c1"):
            if q1 == "DTL of BDT 37,500":
                st.success("✅ Correct! CA (500,000) > TB (350,000) → Taxable Temp Diff of 150,000 → DTL = 150,000 × 25% = BDT 37,500")
            else:
                st.error("❌ Incorrect. CA (500k) > TB (350k) → Taxable Temp Diff 150k × 25% = **DTL BDT 37,500**")

        # Q2
        st.markdown("---")
        st.markdown("**Q2. A warranty provision of BDT 200,000 is recognised in the accounts. Tax deduction is only available when claims are paid. Tax rate = 30%. What is the deferred tax effect?**")
        q2 = st.radio("Select:", [
            "DTL of BDT 60,000",
            "DTA of BDT 60,000",
            "No deferred tax — provisions are not temporary differences",
            "DTA of BDT 200,000"
        ], key="ias12q2")
        if st.button("Check Answer", key="ias12c2"):
            if q2 == "DTA of BDT 60,000":
                st.success("✅ Correct! Provision CA = 200,000, Tax Base = 0 → Liability where CA > TB → Deductible Temp Diff → DTA = 200,000 × 30% = BDT 60,000")
            else:
                st.error("❌ Incorrect. Liability: CA (200k) > TB (0) → Deductible Temp Diff → **DTA = BDT 60,000**")

        # Q3
        st.markdown("---")
        st.markdown("**Q3. Land is revalued from BDT 1,000,000 to BDT 1,500,000. Tax base = BDT 1,000,000. Tax rate = 25%. Where should the deferred tax be recognised?**")
        q3 = st.radio("Select:", [
            "In the income statement as a current tax expense",
            "In Other Comprehensive Income (OCI)",
            "Directly in equity as retained earnings",
            "No deferred tax on revaluation is allowed under IAS 12"
        ], key="ias12q3")
        if st.button("Check Answer", key="ias12c3"):
            if q3 == "In Other Comprehensive Income (OCI)":
                st.success("✅ Correct! Per IAS 12.61A — tax follows the item. Revaluation goes to OCI, so DTL = 500,000 × 25% = 125,000 also goes to OCI.")
            else:
                st.error("❌ Incorrect. **IAS 12.61A**: Tax follows the item → Revaluation in OCI → DTL in OCI.")

        # Q4
        st.markdown("---")
        st.markdown("**Q4. An entity has a DTL of BDT 300,000 (at 30% rate). The government then enacts a new rate of 20%. What happens?**")
        q4 = st.radio("Select:", [
            "DTL stays at BDT 300,000 — rates only affect current tax",
            "DTL is remeasured to BDT 200,000; reduction of BDT 100,000 credited to P&L",
            "DTL is remeasured to BDT 200,000; reduction goes to OCI",
            "DTL is derecognised entirely"
        ], key="ias12q4")
        if st.button("Check Answer", key="ias12c4"):
            if q4 == "DTL is remeasured to BDT 200,000; reduction of BDT 100,000 credited to P&L":
                st.success("✅ Correct! Temp Diff = 300,000 / 30% = 1,000,000. Remeasured DTL = 1,000,000 × 20% = 200,000. Credit to P&L = BDT 100,000.")
            else:
                st.error("❌ Incorrect. DTAs/DTLs must be remeasured at the **enacted/substantially enacted rate**. Temp Diff = 1,000,000 × 20% = **BDT 200,000** → **BDT 100,000 credit to P&L**.")

        # Q5
        st.markdown("---")
        st.markdown("**Q5. Under IAS 12, a deferred tax asset for a tax loss carried forward should be recognised only when:**")
        q5 = st.radio("Select:", [
            "The loss arises from extraordinary items",
            "It is probable that sufficient future taxable profit will be available",
            "The loss has been agreed by the tax authority",
            "The entity is profitable in the current year"
        ], key="ias12q5")
        if st.button("Check Answer", key="ias12c5"):
            if q5 == "It is probable that sufficient future taxable profit will be available":
                st.success("✅ Correct! IAS 12.34 — DTA for tax losses is recognised only when it is probable that sufficient future taxable profit will be available to utilise the loss.")
            else:
                st.error("❌ Incorrect. **IAS 12.34**: DTA for tax losses → recognised only if **probable** that future taxable profits will be available.")

        # Q6
        st.markdown("---")
        st.markdown("**Q6. Under IAS 12, which of the following creates a deferred tax LIABILITY?**")
        q6 = st.radio("Select:", [
            "Warranty provision recognised in advance",
            "Pension liability where contributions are deductible when paid",
            "Accelerated tax depreciation (tax > accounting depreciation)",
            "Unused tax losses carried forward"
        ], key="ias12q6")
        if st.button("Check Answer", key="ias12c6"):
            if q6 == "Accelerated tax depreciation (tax > accounting depreciation)":
                st.success("✅ Correct! Accelerated tax depreciation → Tax Base < Carrying Amount → Taxable Temp Diff on asset → DTL.")
            else:
                st.error("❌ Incorrect. Accelerated tax depreciation → TB < CA → **DTL**. The other options create DTAs.")

        # Q7
        st.markdown("---")
        st.markdown("**Q7. IAS 12 requires deferred tax to be discounted to present value. True or False?**")
        q7 = st.radio("Select:", ["True", "False"], key="ias12q7")
        if st.button("Check Answer", key="ias12c7"):
            if q7 == "False":
                st.success("✅ Correct! IAS 12.53 explicitly **prohibits** discounting of deferred tax assets and liabilities.")
            else:
                st.error("❌ Incorrect. **IAS 12.53** explicitly PROHIBITS discounting of deferred tax.")

        # Q8
        st.markdown("---")
        st.markdown("**Q8. In a business combination, a DTL is recognised on the fair value uplift of an acquired building. How does this affect goodwill?**")
        q8 = st.radio("Select:", [
            "Goodwill decreases — the DTL is charged directly to goodwill",
            "Goodwill increases — the DTL reduces the fair value of net assets acquired",
            "No effect — DTL in business combinations goes to P&L",
            "The DTL is set off against the fair value of the building only"
        ], key="ias12q8")
        if st.button("Check Answer", key="ias12c8"):
            if q8 == "Goodwill increases — the DTL reduces the fair value of net assets acquired":
                st.success("✅ Correct! DTL reduces net assets acquired → Goodwill (Consideration − Net Assets) increases.")
            else:
                st.error("❌ Incorrect. DTL reduces net identifiable assets → **Goodwill increases**.")

        # Q9
        st.markdown("---")
        st.markdown("**Q9. Under IAS 12, deferred tax assets and liabilities may be offset in the balance sheet when:**")
        q9 = st.radio("Select:", [
            "The entity has positive retained earnings",
            "The entity has a legally enforceable right to offset AND they relate to taxes levied by the same authority on the same entity",
            "The DTA and DTL arise from the same transaction only",
            "Management decides to net them for simplicity"
        ], key="ias12q9")
        if st.button("Check Answer", key="ias12c9"):
            if q9 == "The entity has a legally enforceable right to offset AND they relate to taxes levied by the same authority on the same entity":
                st.success("✅ Correct! IAS 12.74 — both conditions must be met: legally enforceable right AND same tax authority / same taxable entity.")
            else:
                st.error("❌ Incorrect. **IAS 12.74**: Offset permitted only with legally enforceable right AND same tax authority/entity.")

        # Q10
        st.markdown("---")
        st.markdown("**Q10. An entity has a DTA of BDT 500,000. Due to worsening trading conditions, it is no longer probable that future profits will be available. What should the entity do?**")
        q10 = st.radio("Select:", [
            "Keep the DTA — it can be reassessed next year",
            "Write down (reduce) the DTA and charge the reduction to the income statement",
            "Transfer the DTA to equity reserves",
            "Reclassify it as a current tax asset"
        ], key="ias12q10")
        if st.button("Check Answer", key="ias12c10"):
            if q10 == "Write down (reduce) the DTA and charge the reduction to the income statement":
                st.success("✅ Correct! IAS 12.56 — DTA must be reduced (written down) when it is no longer probable that sufficient future taxable profits will be available. The reduction goes to the income statement.")
            else:
                st.error("❌ Incorrect. **IAS 12.56**: DTA must be **written down** — charge to income statement.")

    # ─────────────────────────────────────────────────────────────────
    # TAB 5: SUMMARY
    # ─────────────────────────────────────────────────────────────────
    with tab5:
        st.header("Module Summary — IAS 12 Deferred Tax")

        st.markdown("""
        ### 🎯 The Core Logic at a Glance

        | Position | Asset (CA vs TB) | Liability (CA vs TB) | Deferred Tax |
        |----------|-----------------|----------------------|--------------|
        | CA **>** TB | Taxable Temp Diff | Deductible Temp Diff | **DTL** / **DTA** |
        | CA **<** TB | Deductible Temp Diff | Taxable Temp Diff | **DTA** / **DTL** |
        | CA **=** TB | No difference | No difference | Nil |
        """)

        st.markdown("""
        ### 📋 Key Recognition Rules

        | Item | Rule |
        |------|------|
        | DTL — General | Recognise ALL taxable temp diffs (subject to exceptions) |
        | DTA — General | Recognise IF probable sufficient future taxable profits |
        | DTL — Goodwill | **Do NOT recognise** (IAS 12.15(a)) |
        | DTL — Initial Recognition Exemption | Do not recognise if transaction affected neither accounting nor taxable profit at time of transaction |
        | DTA — Tax Losses | Recognise only if probable future taxable profit available (IAS 12.34) |
        | Investments (subs/assoc) | DTL exempt if parent controls timing AND reversal not probable |
        | Revaluation | Deferred tax in OCI (tax follows the item) |
        | Business Combination | DTL/DTA on FV uplift → adjusts goodwill |
        | Discounting | **PROHIBITED** under IAS 12.53 |
        """)

        st.markdown("""
        ### 🔢 Key Formulas

        ```
        Temporary Difference  =  Carrying Amount  −  Tax Base

        Deferred Tax          =  Temporary Difference  ×  Applicable Tax Rate

        Tax Base of Asset     =  Amount deductible in future against taxable benefits

        Tax Base of Liability =  Carrying Amount − Future tax deductions available

        Net DTA/DTL           =  Total DTA − Total DTL  (after legal right to offset confirmed)
        ```
        """)

        st.markdown("""
        ### ⚠️ Common Pitfalls & Exam Traps

        | Trap | Correct Treatment |
        |------|-------------------|
        | Goodwill → DTL? | ❌ Never recognise DTL on goodwill |
        | Revaluation → P&L tax? | ❌ Tax on revaluation goes to OCI, not P&L |
        | Tax loss → Always DTA? | ❌ Only if PROBABLE future profits available |
        | Discount DTA/DTL? | ❌ Discounting is PROHIBITED |
        | Rate change → Ignore old DTL? | ❌ Must remeasure at newly enacted rate |
        | Always offset DTA and DTL? | ❌ Only if legally enforceable right + same authority |
        | Intra-group elimination → DTA? | ✅ Yes — at buyer's tax rate |
        """)

        st.markdown("""
        ### 📊 Flowchart: Should a DTA be Recognised?

        ```
        Is there a deductible temporary difference (or unused tax loss)?
                            │
                            ▼
                          Yes
                            │
                            ▼
        Is it probable that sufficient future taxable profit will be available?
                ┌───────────┴────────────┐
               Yes                       No
                │                        │
                ▼                        ▼
        ✅ RECOGNISE DTA         ❌ DO NOT RECOGNISE DTA
                                  (Disclose in notes: IAS 12.81(e))
        ```
        """)

        st.markdown("""
        ### 📌 IAS 12 Key Paragraph Reference Map

        ```
        IAS 12
        ├── Para 5        →  Key definitions (tax base, temp diff, DTA, DTL)
        ├── Para 15       →  When NOT to recognise a DTL (goodwill; initial recognition exemption)
        ├── Para 24       →  Recognition of DTA — probability test
        ├── Para 34–35    →  DTA for unused tax losses and tax credits
        ├── Para 37       →  Reassessment of unrecognised DTAs at each year-end
        ├── Para 38–45    →  Investments in subsidiaries, associates, JVs
        ├── Para 46–52    →  Measurement — rates, enacted/substantially enacted
        ├── Para 53       →  Prohibition on discounting
        ├── Para 56       →  Write-down of DTAs when no longer probable
        ├── Para 58       →  Current and deferred tax in P&L
        ├── Para 61A      →  Tax recognised outside P&L (OCI / equity)
        ├── Para 68       →  Intra-group elimination — buyer's tax rate
        ├── Para 74       →  Offsetting conditions
        └── Para 81       →  Disclosure requirements
        ```
        """)

        st.markdown("""
        ### 💡 Practical Tips for Preparers

        1. **Build a deferred tax schedule** — track CA, TB, temp diff, and DT balance for every balance sheet item
        2. **Monitor tax rate changes** — remeasure immediately when new rates are enacted
        3. **Review DTA recoverability annually** — deteriorating profits may require write-down
        4. **Separate OCI items** — always check if the underlying item went through OCI before posting deferred tax
        5. **Business combinations** — obtain a full tax-base schedule from the target's advisors
        6. **Intra-group sales** — set up a separate consolidation adjustment for DTA on unrealised profits
        7. **Disclosures** — IAS 12.81 requires extensive note disclosures including reconciliation of effective tax rate
        """)

        st.success("🎓 **Module Complete!** You now understand the full mechanism of Deferred Tax under IAS 12 — from basic temporary differences to complex business combination and consolidation scenarios.")
        st.info("📘 **Reference Standard:** IAS 12 Income Taxes (as issued by the IASB). Always consult the latest version and local jurisdiction supplements.")


if __name__ == "__main__":
    show()