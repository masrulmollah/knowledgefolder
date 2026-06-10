import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🏢 Leases: Complete Guide under IFRS 16")
    st.markdown("*Based on IFRS 16 — Leases (International Financial Reporting Standard, effective 1 January 2019)*")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory & Concepts", "🧮 Examples", "💡 Interactive Calculator",
        "✅ Quiz", "📝 Summary"
    ])

    # ═══════════════════════════════════════════════════════════════════
    # TAB 1 — THEORY & CONCEPTS
    # ═══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("Theory & Conceptual Framework")

        # ── 1. What is IFRS 16? ──────────────────────────────────────
        st.subheader("1. What is IFRS 16 and Why Does It Matter?")
        st.markdown("""
        **IFRS 16 Leases** (effective 1 January 2019) replaced IAS 17 and introduced a **single lessee accounting model**:
        virtually all leases are now recognised **on the balance sheet**.

        > 💡 *Key Shift from IAS 17*: Under the old standard, operating leases were kept **off balance sheet**
        > — the asset and liability never appeared. IFRS 16 changed this entirely. Now lessees must
        > recognise a **Right-of-Use (ROU) Asset** and a **Lease Liability** for almost every lease.

        **Why it matters:**
        - Brings **transparency** — all lease obligations are visible to investors
        - Affects **gearing ratios**, **EBITDA**, **interest cover**, and **asset turnover**
        - Only **two exemptions** allow off-balance-sheet treatment (short-term and low-value leases)

        **Scope:** IFRS 16 applies to all leases except:
        - Leases of biological assets (IAS 41)
        - Service concession arrangements (IFRIC 12)
        - Leases of intangible assets (optional exemption)
        - Exploration / extraction of minerals
        """)

        # ── 2. Definition of a Lease ─────────────────────────────────
        st.subheader("2. Identifying a Lease — The Core Definition")
        st.markdown("""
        **IFRS 16.9:** A contract is, or contains, a lease if it conveys the right to **control the use of an
        identified asset** for a **period of time** in exchange for **consideration**.

        **Three Criteria — ALL must be met for a lease to exist:**
        """)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("""
            **① Identified Asset**
            The asset is specified (explicitly or implicitly) in the contract.
            The supplier does NOT have a substantive substitution right.

            *Supplier substitution is only substantive if:*
            - Right exists throughout the period of use, AND
            - Supplier benefits economically from substituting
            """)
        with col2:
            st.info("""
            **② Right to Obtain Substantially All Economic Benefits**
            The customer has the right to obtain substantially all the economic
            benefits from use of the identified asset throughout the period of use.

            *Consider: output, by-products, other economic benefits from use*
            """)
        with col3:
            st.info("""
            **③ Right to Direct the Use**
            The customer has the right to direct HOW and FOR WHAT PURPOSE
            the asset is used throughout the period of use.

            *If how/for what purpose is predetermined:*
            Does the customer operate the asset? Or design it?
            """)

        st.markdown("""
        **Decision Tree — Does a Contract Contain a Lease?**
        ```
        Is there an IDENTIFIED ASSET?
            No  →  Not a Lease (Service contract)
            Yes ↓
        Does customer get SUBSTANTIALLY ALL ECONOMIC BENEFITS?
            No  →  Not a Lease
            Yes ↓
        Does customer have RIGHT TO DIRECT USE (how and for what purpose)?
            No  →  Not a Lease
            Yes →  ✅ CONTRACT CONTAINS A LEASE
        ```
        """)

        # ── 3. Lessee Exemptions ─────────────────────────────────────
        st.subheader("3. Lessee Recognition Exemptions (Practical Expedients)")
        st.markdown("""
        **IFRS 16.5:** A lessee MAY elect NOT to apply the on-balance-sheet model to:

        | Exemption | Definition | Accounting Treatment |
        |-----------|-----------|---------------------|
        | **Short-term leases** | Lease term ≤ 12 months at commencement date (no purchase option) | Lease payments recognised as expense — straight-line or systematic basis |
        | **Low-value asset leases** | Underlying asset has a low value **when new** (IASB guidance: ≈ USD 5,000) | Lease payments recognised as expense — regardless of materiality to lessee |

        > ⚠️ *The low-value test is applied on an individual asset basis — even if the total portfolio is material.*
        > Common examples: laptops, tablets, small office furniture, personal computers.

        > ⚠️ *Short-term exemption is elected by CLASS of underlying asset; low-value is per individual asset.*
        """)

        # ── 4. Lease Term ────────────────────────────────────────────
        st.subheader("4. Determining the Lease Term")
        st.markdown("""
        **IFRS 16.19:** The lease term is the **non-cancellable period** of a lease, together with:
        - **Optional extension periods** — if the lessee is **reasonably certain** to exercise the extension option
        - **Optional termination periods** — if the lessee is **reasonably certain NOT** to exercise the termination option

        **Factors affecting "reasonably certain" assessment:**
        - Significance of leasehold improvements
        - Importance of underlying asset to lessee's operations
        - Costs of relocation / replacement
        - Past practice of exercising / not exercising options
        - Contractual terms (e.g. below-market extension rentals)

        > 📌 *IFRS 16 requires reassessment of lease term when there is a significant event or change in
        > circumstances that is within the control of the lessee.*
        """)

        # ── 5. Lessee: Initial Recognition ───────────────────────────
        st.subheader("5. Lessee Accounting — Initial Recognition")
        st.markdown("""
        At the **commencement date**, a lessee recognises:

        **A. Right-of-Use (ROU) Asset:**
        ```
        ROU Asset  =  Initial Lease Liability
                    + Lease Payments Made at/Before Commencement (net of incentives received)
                    + Initial Direct Costs incurred by Lessee
                    + Estimated Cost of Dismantling / Restoring (if obligation exists — IAS 37)
        ```

        **B. Lease Liability:**
        ```
        Lease Liability  =  Present Value of Lease Payments NOT yet paid at Commencement Date
        ```

        **Lease Payments included in Lease Liability:**
        - Fixed payments (including in-substance fixed payments), net of lease incentives receivable
        - Variable lease payments that depend on an index or rate (initially measured using index/rate at commencement)
        - Amounts expected to be payable under residual value guarantees
        - Exercise price of a purchase option — if lessee is reasonably certain to exercise
        - Penalty for terminating — if lease term reflects lessee exercising a termination option

        **Discount Rate Used:**
        - **Implicit rate in the lease** (if readily determinable) — preferred
        - **Lessee's Incremental Borrowing Rate (IBR)** — if implicit rate cannot be readily determined
        """)

        # ── 6. Lessee: Subsequent Measurement ───────────────────────
        st.subheader("6. Lessee Accounting — Subsequent Measurement")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### ROU Asset — After Commencement")
            st.info("""
            **Cost Model (default):**
            - Depreciate over SHORTER of: lease term or useful economic life
            - (If ownership transfer or purchase option reasonably certain → depreciate over UEL)
            - Test for impairment (IAS 36)
            - Adjust for remeasurement of lease liability

            **Revaluation Model (if underlying asset class uses revaluation):**
            - Apply IAS 16 revaluation model

            **Fair Value Model (Investment Property):**
            - Apply IAS 40 fair value model
            """)
        with col2:
            st.markdown("#### Lease Liability — After Commencement")
            st.info("""
            **Carry at amortised cost using effective interest method:**

            Each period:
            1. **Increase** by interest accrued (Lease Liability × IBR)
            2. **Decrease** by lease payments made

            ```
            Closing Liability
            = Opening Liability
            + Interest Charge
            − Lease Payment
            ```

            Interest is recognised in P&L as a **finance cost** (not operating expense).
            """)

        st.markdown("""
        **P&L Impact for Lessee:**
        ```
        Operating Expenses:
            Depreciation of ROU Asset           (XXX)   ← in operating profit / EBIT

        Finance Costs:
            Interest on Lease Liability         (XXX)   ← below operating profit

        Total P&L charge each year = Depreciation + Interest
        Note: Total charge is FRONT-LOADED (higher in early years) because interest is higher early on
        ```

        > 💡 *EBITDA increases under IFRS 16* — depreciation and interest are excluded from EBITDA,
        > whereas the old operating lease expense (IAS 17) was included as an operating cost.
        """)

        # ── 7. Lease Modifications ───────────────────────────────────
        st.subheader("7. Lease Modifications — Lessee")
        st.markdown("""
        A **lease modification** is a change in the scope or consideration of a lease that was not part of the original terms.

        **Two accounting treatments depending on whether it is a separate lease:**

        | Situation | Treatment |
        |-----------|-----------|
        | Modification adds right to use **additional** asset AND consideration increases by an amount commensurate with standalone price | **Separate new lease** — account for the new lease independently |
        | All other modifications | **Remeasure the existing lease liability** at a revised discount rate; adjust the ROU asset |

        **Remeasurement triggers (not modifications) — use original discount rate:**
        - Change in residual value guarantee amounts
        - Change in assessment of purchase option exercise
        - Change in assessment of termination option exercise
        - Change in index/rate for variable lease payments

        **Remeasurement triggers — use revised discount rate:**
        - Change in lease term
        - Change in assessment of purchase option (i.e. the lease scope changes)
        """)

        # ── 8. Sale and Leaseback ────────────────────────────────────
        st.subheader("8. Sale and Leaseback Transactions")
        st.markdown("""
        **IFRS 16.98–103:** When an entity sells an asset and leases it back:

        **Step 1:** Determine whether the transfer is a **sale** under IFRS 15
        - Yes → Sale and Leaseback
        - No → Financial arrangement (loan)

        **If it IS a sale:**
        ```
        Seller-Lessee recognises:
        - ROU Asset = Proportion of previous CA retained (related to right retained)
        - Lease Liability = PV of future lease payments
        - Gain/Loss recognised ONLY on the portion of rights transferred to buyer
        ```

        **If it is NOT a sale (IFRS 15 criteria not met):**
        ```
        - Seller-Lessee: does NOT derecognise the asset
        - Recognises a financial liability equal to proceeds received
        - Buyer-Lessor: does NOT recognise the asset; recognises a financial asset
        ```

        **Fair Value vs Book Value difference:**
        - If proceeds > fair value: excess is prepaid lease payment (reduce lease liability)
        - If proceeds < fair value: shortfall is additional lease payment (increase lease liability)
        """)

        # ── 9. Lessor Accounting ─────────────────────────────────────
        st.subheader("9. Lessor Accounting — Classification")
        st.markdown("""
        > 📌 *Key difference*: IFRS 16 did NOT fundamentally change lessor accounting from IAS 17.
        > Lessors still classify leases as **Finance Leases** or **Operating Leases**.

        **Finance Lease** (IFRS 16.63): A lease that transfers **substantially all the risks and rewards**
        incidental to ownership of the underlying asset.

        **Indicators of a Finance Lease (IFRS 16.63–65):**

        | Indicator | Explanation |
        |-----------|-------------|
        | Ownership transfer | Lease transfers ownership to lessee by end of term |
        | Purchase option | Lessee has option to buy at price expected to be sufficiently lower than fair value |
        | Lease term = major part of economic life | Lease runs for the major part of the asset's remaining economic life |
        | PV of payments ≈ fair value | Present value of minimum lease payments ≈ substantially all of fair value of asset |
        | Specialised nature | Asset is so specialised that only lessee can use it without major modifications |
        | Loss on cancellation | Lessee bears lessor's loss if lessee cancels |
        | Residual value risk | Lessee bears gains/losses from fair value fluctuations |
        | Below-market continuation | Option to continue at below-market rent |

        No single indicator is conclusive — **substance over form** applies.
        """)

        # ── 10. Lessor: Finance Lease Accounting ─────────────────────
        st.subheader("10. Lessor Accounting — Finance Lease")
        st.markdown("""
        **Initial Recognition:**
        ```
        Derecognise the underlying asset
        Recognise a NET INVESTMENT IN THE LEASE (Lease Receivable)

        Net Investment  =  PV of:
                           - Lease payments receivable
                           - Unguaranteed residual value
                           (discounted at the interest rate implicit in the lease)
        ```

        **Subsequent Measurement — Effective Interest Method:**
        ```
        Each period:
        Recognise finance income  =  Net Investment × Implicit Interest Rate
        Reduce net investment     =  by lease payments received less finance income
        ```

        **Manufacturer / Dealer Lessors:**
        - Recognise a **selling profit or loss** at commencement (same as if they had sold the asset outright)
        - Selling profit = Fair Value of asset − Carrying amount of asset
        - Finance income is earned over the lease term
        - If artificially low interest rate is used → restrict selling profit; recognise interest at market rate
        """)

        # ── 11. Lessor: Operating Lease Accounting ───────────────────
        st.subheader("11. Lessor Accounting — Operating Lease")
        st.markdown("""
        **The lessor retains the underlying asset on its balance sheet.**

        **P&L Treatment:**
        ```
        Rental income   →  Recognised on a straight-line basis (or another systematic basis)
                           over the lease term
        Depreciation    →  Charged on the underlying asset (per the asset's own accounting policy)
        Initial direct costs → Deferred and added to the carrying amount of the leased asset;
                               recognised over the lease term on same basis as rental income
        ```

        **Balance Sheet:**
        - Underlying asset remains as PPE / Investment Property (etc.) on lessor's balance sheet
        - Depreciated normally per IAS 16 / IAS 40
        - Any lease incentives paid to the lessee are amortised over the lease term as a reduction of rental income
        """)

        # ── 12. Sub-leases ───────────────────────────────────────────
        st.subheader("12. Sub-leases")
        st.markdown("""
        When an **intermediate lessor** (a party who is both a lessee and a lessor) sub-leases an asset:

        **Classification is based on the ROU asset** (not the underlying physical asset):

        | Outcome | Treatment |
        |---------|-----------|
        | Sub-lease is a **Finance Lease** | Intermediate lessor derecognises ROU asset; recognises net investment in sub-lease |
        | Sub-lease is an **Operating Lease** | Intermediate lessor retains ROU asset; recognises rental income on straight-line basis |

        > 📌 *The head lease (with the head lessor) continues to be recognised as normal by the intermediate lessor.*
        """)

        # ── 13. Variable Lease Payments ──────────────────────────────
        st.subheader("13. Variable Lease Payments")
        st.markdown("""
        | Type | Included in Lease Liability? | P&L Treatment |
        |------|------------------------------|---------------|
        | **Index/rate-linked** (e.g. CPI, LIBOR) | ✅ Yes — at current index/rate at commencement | Remeasure lease liability when index/rate changes |
        | **In-substance fixed** (unavoidable in practice) | ✅ Yes | — |
        | **Usage-based** (e.g. per km, per unit) | ❌ No | Expensed when incurred |
        | **Performance-contingent** | ❌ No | Expensed when incurred |
        """)

        # ── 14. Deferred Tax on Leases ───────────────────────────────
        st.subheader("14. Deferred Tax Interaction with IFRS 16 Leases")
        st.markdown("""
        IFRS 16 creates **temporary differences** for deferred tax purposes (IAS 12):

        | Item | Carrying Amount | Tax Base (typically) | Result |
        |------|-----------------|---------------------|--------|
        | ROU Asset | Depreciated cost | Zero (lease payments deductible when paid) | Taxable temp diff → **DTL** |
        | Lease Liability | PV of future payments | Zero (deductible when paid) | Deductible temp diff → **DTA** |

        > 💡 *Since ROU Asset ≈ Lease Liability at commencement, the DTL and DTA roughly offset.*
        > However, they diverge over time due to different depreciation vs amortisation profiles.

        **Initial Recognition Exemption (IAS 12.15(b) / IAS 12.24):**
        - Applies only if the transaction is NOT a business combination AND affects NEITHER
          accounting profit NOR taxable profit at the time
        - For most IFRS 16 leases on first-time adoption, the exemption may apply
        - For new leases after adoption, entities generally recognise both DTA and DTL
          because recognising only one would distort the tax charge
        """)

        # ── 15. Disclosures ──────────────────────────────────────────
        st.subheader("15. Disclosure Requirements (IFRS 16.47–60)")
        st.markdown("""
        **Lessee Disclosures:**

        | Disclosure | Description |
        |------------|-------------|
        | Depreciation of ROU assets | By class of underlying asset |
        | Interest on lease liabilities | Finance cost in P&L |
        | Short-term lease expense | If practical expedient used |
        | Low-value lease expense | If practical expedient used |
        | Variable lease payment expense | Not included in liability measurement |
        | Subleases income | From ROU assets |
        | Total cash outflow for leases | Including principal and interest |
        | ROU asset additions | Movements during the period |
        | Maturity analysis of lease liabilities | Undiscounted payments |

        **Lessor Disclosures:**
        - Finance leases: maturity analysis of lease receivables, reconciliation of gross/net investment
        - Operating leases: maturity analysis of lease payments, ROU asset disclosures

        > 📌 *IFRS 16.59*: Lessees must also disclose a maturity analysis showing undiscounted cash flows
        > for at least each of the first five years and a total for the remaining years.
        """)

    # ═══════════════════════════════════════════════════════════════════
    # TAB 2 — EXAMPLES
    # ═══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("Practical Examples")

        # ── Example 1: Basic Lessee ───────────────────────────────────
        st.subheader("Example 1: Basic Lessee — Office Lease (Fixed Payments)")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            On 1 January Year 1, a company leases office space for **5 years** with annual payments
            of **BDT 500,000** payable at the **end** of each year. The lessee's **Incremental Borrowing Rate (IBR) = 8%**.
            No purchase option. No residual value guarantee.

            **Step 1 — Calculate Lease Liability (PV of annuity):**
            ```
            PV = 500,000 × [1 − (1 + 0.08)^−5] / 0.08
               = 500,000 × 3.9927
               = BDT 1,996,355
            ```

            **Step 2 — ROU Asset:**
            ```
            ROU Asset = Lease Liability (no initial direct costs / prepayments)
                      = BDT 1,996,355
            ```

            **Step 3 — Depreciation (straight-line over 5 years):**
            ```
            Annual Depreciation = 1,996,355 / 5 = BDT 399,271
            ```

            **Step 4 — Lease Liability Amortisation Schedule:**
            """)

            rate = 0.08
            pmt = 500_000
            n = 5
            bal = round(pmt * (1 - (1 + rate)**-n) / rate, 0)
            rows = []
            for y in range(1, n + 1):
                interest = round(bal * rate, 0)
                principal = pmt - interest
                closing = bal - principal
                rows.append({"Year": y, "Opening Liability": f"{bal:,.0f}",
                              "Interest (8%)": f"{interest:,.0f}",
                              "Payment": f"{pmt:,.0f}",
                              "Principal Repaid": f"{principal:,.0f}",
                              "Closing Liability": f"{max(closing,0):,.0f}"})
                bal = max(closing, 0)
            st.dataframe(pd.DataFrame(rows), use_container_width=True)

            st.markdown("""
            **P&L Charge Each Year:**

            | Year | Depreciation | Interest | Total Charge |
            |------|-------------|----------|--------------|
            | 1    | 399,271     | 159,708  | 558,979      |
            | 2    | 399,271     | 137,485  | 536,756      |
            | 3    | 399,271     | 113,283  | 512,554      |
            | 4    | 399,271     | 86,944   | 486,215      |
            | 5    | 399,271     | 58,299   | 457,570      |

            > 💡 Note: The total charge is **front-loaded** (higher in Year 1, reducing each year).
            > Under IAS 17 operating lease model, the charge would have been a flat **BDT 500,000** each year.

            **Journal Entries — Year 1:**
            ```
            At commencement:
            Dr  ROU Asset                     1,996,355
                Cr  Lease Liability               1,996,355

            Year-end depreciation:
            Dr  Depreciation Expense            399,271
                Cr  Accumulated Depreciation        399,271

            Year-end interest accrual:
            Dr  Finance Cost (Interest)         159,708
                Cr  Lease Liability                  159,708

            Lease payment:
            Dr  Lease Liability                 500,000
                Cr  Cash                             500,000
            ```
            """)

        # ── Example 2: Lease with Extension Option ───────────────────
        st.subheader("Example 2: Lease with Extension Option — Reassessment")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A company leases a warehouse for a **non-cancellable period of 3 years**,
            with an **option to extend for 2 more years**. Annual payment = BDT 300,000. IBR = 7%.

            At inception, management is **NOT** reasonably certain to exercise the extension.

            **Year 1 — Initial Recognition (3-year term):**
            ```
            PV (3 yrs @ 7%) = 300,000 × 2.6243 = BDT 787,290
            ROU Asset = Lease Liability = BDT 787,290
            ```

            **End of Year 2 — Reassessment:**
            The company makes significant leasehold improvements (BDT 400,000) and is now
            **reasonably certain** to exercise the extension option.

            **Revised Lease Term = 3 years total (1 remaining + 2 extension)**
            ```
            Revised Lease Liability = PV of 3 remaining payments @ revised IBR of 7.5%
                                    = 300,000 × 2.6005 = BDT 780,150

            Opening Lease Liability (before remeasurement) = BDT 247,583 (approx)
            Adjustment to Lease Liability = 780,150 − 247,583 = BDT 532,567

            Journal Entry — Remeasurement:
            Dr  ROU Asset                      532,567
                Cr  Lease Liability                 532,567
            ```

            > 📌 When remeasuring for change in lease term, use the **revised discount rate** (IBR at reassessment date).
            > The ROU asset is adjusted by the same amount as the lease liability.
            """)

        # ── Example 3: Lessor Finance Lease ──────────────────────────
        st.subheader("Example 3: Lessor — Finance Lease with Manufacturer")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A manufacturer leases equipment to a customer for **4 years**.
            - Fair value of equipment = BDT 2,000,000
            - Carrying amount (cost) of equipment = BDT 1,500,000
            - Annual lease payment = BDT 580,000 (payable at year-end)
            - Interest rate implicit in lease = 9%
            - Unguaranteed residual value = BDT 100,000

            **Step 1 — Net Investment in Lease:**
            ```
            PV of lease payments  = 580,000 × 3.2397 = 1,879,026
            PV of residual value  = 100,000 × (1.09)^-4 = 70,843
            Net Investment        = 1,879,026 + 70,843 = BDT 1,949,869
            ```

            **Step 2 — Selling Profit:**
            ```
            Revenue recognised (FV of asset) = BDT 2,000,000
            Cost of sale (CA of asset)       = BDT 1,500,000
            Selling Profit                   = BDT 500,000
            ```

            *(If the rate implicit in the lease was artificially low, restrict profit and use market rate for finance income)*

            **Step 3 — Finance Income Schedule:**
            """)

            rate_l = 0.09
            pmt_l = 580_000
            bal_l = 1_949_869
            rows_l = []
            for y in range(1, 5):
                fi = round(bal_l * rate_l, 0)
                principal_l = pmt_l - fi
                closing_l = bal_l - principal_l
                rows_l.append({"Year": y,
                                "Opening Net Investment": f"{bal_l:,.0f}",
                                "Finance Income (9%)": f"{fi:,.0f}",
                                "Payment Received": f"{pmt_l:,.0f}",
                                "Closing Net Investment": f"{max(closing_l,0):,.0f}"})
                bal_l = max(closing_l, 0)
            st.dataframe(pd.DataFrame(rows_l), use_container_width=True)

            st.markdown("""
            **Opening Journals — Lessor:**
            ```
            Derecognise asset:
            Dr  Cost of Sales                 1,500,000
                Cr  Inventory / PPE                1,500,000

            Recognise revenue and receivable:
            Dr  Net Investment in Lease       1,949,869
            Dr  Loss on Lease (balancing)        50,131
                Cr  Revenue                       2,000,000
            ```
            *(In practice: selling profit = 500,000; the net investment reflects discounted value)*
            """)

        # ── Example 4: Lessor Operating Lease ────────────────────────
        st.subheader("Example 4: Lessor — Operating Lease")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A property company leases an office building (CA = BDT 5,000,000; UEL = 20 years) to a tenant.
            - Lease term: **3 years**
            - Annual rent: Year 1 = BDT 400,000; Year 2 = BDT 450,000; Year 3 = BDT 500,000
            - Lease incentive paid to tenant at inception: BDT 120,000

            **Annual Straight-line Rental Income:**
            ```
            Total rentals = 400,000 + 450,000 + 500,000 = 1,350,000
            Less: Incentive paid = (120,000)
            Net total = 1,230,000
            Annual straight-line income = 1,230,000 / 3 = BDT 410,000 per year
            ```

            **P&L each year:**
            ```
            Rental income (straight-line)    410,000
            Depreciation (5,000,000/20)     (250,000)
            Net income from lease            160,000
            ```

            **Balance Sheet — accrual/deferral:**

            | Year | Cash Rent | SL Income | Accrual/(Deferral) |
            |------|-----------|-----------|-------------------|
            | 1    | 400,000   | 410,000   | Accrual +10,000   |
            | 2    | 450,000   | 410,000   | Deferral (40,000) |
            | 3    | 500,000   | 410,000   | Deferral (90,000) |
            """)

        # ── Example 5: Sale and Leaseback ────────────────────────────
        st.subheader("Example 5: Sale and Leaseback")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            Company sells its building (CA = BDT 3,000,000) for BDT 4,000,000 (= fair value).
            It immediately leases it back for 5 years at annual rent of BDT 400,000. IBR = 8%.
            Transfer meets IFRS 15 sale criteria.

            **Step 1 — Lease Liability:**
            ```
            PV = 400,000 × 3.9927 = BDT 1,597,084
            ```

            **Step 2 — Proportion of Asset Retained vs Sold:**
            ```
            Proportion retained = Lease Liability / Fair Value
                                = 1,597,084 / 4,000,000 = 39.93%
            Proportion sold     = 1 − 39.93% = 60.07%
            ```

            **Step 3 — ROU Asset:**
            ```
            ROU Asset = 39.93% × 3,000,000 (previous CA) = BDT 1,197,900
            ```

            **Step 4 — Gain on Disposal:**
            ```
            Gain relates only to the portion SOLD (60.07%)
            Gain on sold portion = 60.07% × (4,000,000 − 3,000,000) = BDT 600,700

            (The remaining gain of 399,300 — the retained portion — is NOT recognised)
            ```

            **Journal Entry:**
            ```
            Dr  Cash                         4,000,000
            Dr  ROU Asset                    1,197,900
                Cr  Building (CA)                3,000,000
                Cr  Lease Liability               1,597,084
                Cr  Gain on Sale (P&L)              600,816
            ```
            *(Small rounding differences may arise)*
            """)

        # ── Example 6: Variable Payments (Index-Linked) ──────────────
        st.subheader("Example 6: Index-Linked Variable Lease Payments")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            A company leases a factory for 4 years. Annual rent = BDT 200,000 × CPI index.
            CPI at commencement = 100. IBR = 6%.

            **Initial Measurement (use current CPI = 100):**
            ```
            Annual payment = BDT 200,000 × (100/100) = BDT 200,000
            Lease Liability = 200,000 × 3.4651 = BDT 693,020
            ```

            **End of Year 2 — CPI rises to 110:**
            ```
            Revised annual payment = 200,000 × (110/100) = BDT 220,000
            Remaining 2 years: revised liability = 220,000 × 1.8334 = BDT 403,348
            Old remaining liability (approx) = BDT 370,876

            Remeasurement increase = 403,348 − 370,876 = BDT 32,472
            Dr  ROU Asset    32,472
                Cr  Lease Liability  32,472
            ```

            > 📌 Index/rate changes trigger remeasurement of the lease liability.
            > Use the **same discount rate** (IBR at commencement) unless it is a change in floating rate.
            """)

        # ── Example 7: Sub-lease ─────────────────────────────────────
        st.subheader("Example 7: Sub-lease — Intermediate Lessor")
        with st.expander("Click to expand full working"):
            st.markdown("""
            **Scenario:**
            Company A (intermediate lessor) leases an office from Owner (head lessor) for 6 years
            at BDT 100,000/year. IBR = 7%.
            Company A then sub-leases to Tenant B for **all 6 years** at BDT 130,000/year.
            Implicit rate in sub-lease = 8%.

            **Is the sub-lease a Finance Lease?**
            - Sub-lease term (6 years) = entire remaining life of ROU asset ✅
            - PV of sub-lease payments ≈ substantially all of ROU asset ✅
            → **Finance Lease sub-lease**

            **Company A's accounting:**
            ```
            Head lease (as Lessee):
            ROU Asset = PV of 100,000 × 6 yrs @ 7% = 100,000 × 4.7665 = BDT 476,654
            Lease Liability = BDT 476,654

            Sub-lease (as Lessor — Finance Lease):
            Derecognise ROU Asset: Cr ROU Asset 476,654
            Recognise Net Investment: Dr Net Investment in Sub-lease
                = PV of 130,000 × 6 yrs @ 8% = 130,000 × 4.6229 = BDT 601,172

            Day 1 gain = 601,172 − 476,654 = BDT 124,518 (recognised in P&L)
            ```

            > 💡 If the sub-lease were an operating lease, Company A would retain the ROU asset
            > and recognise rental income from Tenant B on a straight-line basis.
            """)

    # ═══════════════════════════════════════════════════════════════════
    # TAB 3 — INTERACTIVE CALCULATOR
    # ═══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("Interactive IFRS 16 Calculator")

        calc_type = st.selectbox("Select Calculation Type:", [
            "1. Lessee: Basic Lease Schedule (Annuity in Arrears)",
            "2. Lessee: Lease with Initial Direct Costs & Prepayment",
            "3. Lessee: Lease Modification / Remeasurement",
            "4. Lessor: Finance Lease Schedule",
            "5. Lessor: Operating Lease — Straight-line Income",
            "6. Sale and Leaseback Calculator"
        ])

        st.markdown("---")

        # ──────────────────────────────────────────────────────────────
        if calc_type == "1. Lessee: Basic Lease Schedule (Annuity in Arrears)":
            st.subheader("Lessee: Basic Lease Liability & ROU Asset Schedule")
            col1, col2, col3 = st.columns(3)
            with col1:
                annual_pmt = st.number_input("Annual Lease Payment (BDT)", value=500_000, step=10_000)
                lease_term = st.number_input("Lease Term (years)", value=5, min_value=1, max_value=30)
            with col2:
                ibr = st.number_input("Discount Rate / IBR (%)", value=8.0, step=0.25) / 100
                payment_timing = st.selectbox("Payment Timing", ["Arrears (End of Year)", "Advance (Start of Year)"])
            with col3:
                init_direct_cost = st.number_input("Initial Direct Costs (BDT)", value=0, step=5_000)
                prepayment = st.number_input("Prepaid Rent at Commencement (BDT)", value=0, step=5_000)
                residual_guar = st.number_input("Residual Value Guarantee (BDT)", value=0, step=5_000)

            # PV calculation
            if payment_timing == "Arrears (End of Year)":
                if ibr > 0:
                    pv_factor = (1 - (1 + ibr)**-lease_term) / ibr
                else:
                    pv_factor = lease_term
                pv_rvg = residual_guar / (1 + ibr)**lease_term if ibr > 0 else residual_guar
            else:
                if ibr > 0:
                    pv_factor = ((1 - (1 + ibr)**-lease_term) / ibr) * (1 + ibr)
                else:
                    pv_factor = lease_term
                pv_rvg = residual_guar / (1 + ibr)**lease_term if ibr > 0 else residual_guar

            lease_liab = annual_pmt * pv_factor + pv_rvg
            rou_asset = lease_liab + init_direct_cost + prepayment
            annual_dep = rou_asset / lease_term

            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Initial Lease Liability", f"BDT {lease_liab:,.0f}")
            col_b.metric("ROU Asset (Initial)", f"BDT {rou_asset:,.0f}")
            col_c.metric("Annual Depreciation", f"BDT {annual_dep:,.0f}")

            # Amortisation table
            rows = []
            bal = lease_liab
            for y in range(1, lease_term + 1):
                if payment_timing == "Advance (Start of Year)":
                    payment_this = annual_pmt
                    interest = round((bal - annual_pmt) * ibr, 0)
                    principal = annual_pmt - interest
                    closing = bal - annual_pmt + interest
                    # Adjust for advance
                    opening_disp = bal
                    interest_disp = round((bal - annual_pmt) * ibr if bal > annual_pmt else 0, 0)
                    closing_disp = max(bal - annual_pmt + interest_disp, 0)
                    rows.append({"Year": y,
                                 "Opening Liability": f"{bal:,.0f}",
                                 f"Interest ({ibr*100:.2f}%)": f"{interest_disp:,.0f}",
                                 "Payment": f"{annual_pmt:,.0f}",
                                 "Closing Liability": f"{closing_disp:,.0f}",
                                 "Depreciation": f"{annual_dep:,.0f}",
                                 "Total P&L": f"{annual_dep + interest_disp:,.0f}"})
                    bal = closing_disp
                else:
                    interest = round(bal * ibr, 0)
                    closing = max(bal + interest - annual_pmt, 0)
                    rows.append({"Year": y,
                                 "Opening Liability": f"{bal:,.0f}",
                                 f"Interest ({ibr*100:.2f}%)": f"{interest:,.0f}",
                                 "Payment": f"{annual_pmt:,.0f}",
                                 "Closing Liability": f"{closing:,.0f}",
                                 "Depreciation": f"{annual_dep:,.0f}",
                                 "Total P&L": f"{annual_dep + interest:,.0f}"})
                    bal = closing

            df = pd.DataFrame(rows)
            st.markdown("**Lease Amortisation & P&L Impact Schedule:**")
            st.dataframe(df, use_container_width=True)

            # Chart
            years_list = [r["Year"] for r in rows]
            liab_list = [float(r["Closing Liability"].replace(",", "")) for r in rows]
            rou_list = [max(rou_asset - annual_dep * y, 0) for y in years_list]
            interest_list = [float(r[f"Interest ({ibr*100:.2f}%)"].replace(",", "")) for r in rows]
            dep_list = [annual_dep] * lease_term

            fig = go.Figure()
            fig.add_trace(go.Bar(x=years_list, y=dep_list, name='Depreciation', marker_color='#2196F3'))
            fig.add_trace(go.Bar(x=years_list, y=interest_list, name='Interest', marker_color='#FF5722'))
            fig.add_trace(go.Scatter(x=years_list, y=liab_list, name='Lease Liability Balance',
                                     line=dict(color='green', width=2), mode='lines+markers', yaxis='y2'))
            fig.add_trace(go.Scatter(x=years_list, y=rou_list, name='ROU Asset Balance',
                                     line=dict(color='purple', width=2, dash='dash'), mode='lines+markers', yaxis='y2'))
            fig.update_layout(
                barmode='stack',
                title='P&L Charge (Stacked) and Balance Sheet Values Over Lease Term',
                yaxis=dict(title='P&L Charge (BDT)'),
                yaxis2=dict(title='Balance Sheet (BDT)', overlaying='y', side='right'),
                height=420, legend=dict(orientation='h', y=-0.2)
            )
            st.plotly_chart(fig, use_container_width=True)

        # ──────────────────────────────────────────────────────────────
        elif calc_type == "2. Lessee: Lease with Initial Direct Costs & Prepayment":
            st.subheader("Lessee: ROU Asset Build-up")
            c1, c2 = st.columns(2)
            with c1:
                lease_liab_2 = st.number_input("Lease Liability at Commencement (BDT)", value=1_500_000, step=50_000)
                idc = st.number_input("Initial Direct Costs (BDT)", value=30_000, step=1_000)
            with c2:
                prepay = st.number_input("Lease Payments Made Before/At Commencement (BDT)", value=50_000, step=1_000)
                incentive = st.number_input("Lease Incentives Received from Lessor (BDT)", value=20_000, step=1_000)
                dismantling = st.number_input("Estimated Dismantling/Restoration Cost (BDT, PV)", value=15_000, step=1_000)

            rou = lease_liab_2 + idc + prepay - incentive + dismantling

            st.markdown("**ROU Asset Calculation:**")
            build_df = pd.DataFrame({
                "Component": [
                    "Initial Lease Liability",
                    "Initial Direct Costs",
                    "Prepaid Lease Payments",
                    "Lease Incentives Received",
                    "Dismantling / Restoration Provision (IAS 37)",
                    "**ROU Asset**"
                ],
                "Amount (BDT)": [
                    f"{lease_liab_2:,.0f}",
                    f"{idc:,.0f}",
                    f"{prepay:,.0f}",
                    f"({incentive:,.0f})",
                    f"{dismantling:,.0f}",
                    f"**{rou:,.0f}**"
                ]
            })
            st.table(build_df)

            lt2 = st.number_input("Lease Term for Depreciation (years)", value=5, min_value=1)
            st.metric("Annual Straight-line Depreciation", f"BDT {rou/lt2:,.0f}")

        # ──────────────────────────────────────────────────────────────
        elif calc_type == "3. Lessee: Lease Modification / Remeasurement":
            st.subheader("Lessee: Lease Modification — Remeasurement")
            st.markdown("Enter the **current position** (before modification) and the **revised terms**:")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Before Modification:**")
                old_liab = st.number_input("Carrying Amount of Lease Liability (BDT)", value=800_000, step=10_000)
                old_rou = st.number_input("Carrying Amount of ROU Asset (BDT)", value=750_000, step=10_000)
            with c2:
                st.markdown("**Revised Terms:**")
                new_pmt = st.number_input("Revised Annual Payment (BDT)", value=350_000, step=5_000)
                new_term = st.number_input("Remaining Lease Term after Modification (years)", value=4, min_value=1)
                new_rate = st.number_input("Revised Discount Rate (%)", value=9.0, step=0.25) / 100

            new_liab = new_pmt * (1 - (1 + new_rate)**-new_term) / new_rate if new_rate > 0 else new_pmt * new_term
            adjustment = new_liab - old_liab

            st.markdown("---")
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Old Lease Liability", f"BDT {old_liab:,.0f}")
            col_b.metric("Revised Lease Liability", f"BDT {new_liab:,.0f}")
            if adjustment >= 0:
                col_c.metric("Adjustment to ROU Asset", f"+BDT {adjustment:,.0f}", delta="Increase")
            else:
                col_c.metric("Adjustment to ROU Asset", f"BDT {adjustment:,.0f}", delta="Decrease")

            new_rou = old_rou + adjustment
            st.markdown(f"""
            **Journal Entry — Lease Modification:**
            ```
            {"Dr  ROU Asset" if adjustment >= 0 else "Dr  Lease Liability"}   {"  " + f"{abs(adjustment):,.0f}"}
                {"Cr  Lease Liability" if adjustment >= 0 else "Cr  ROU Asset"}    {"  " + f"{abs(adjustment):,.0f}"}
            ```

            | Item | Before | After |
            |------|--------|-------|
            | Lease Liability | {old_liab:,.0f} | {new_liab:,.0f} |
            | ROU Asset | {old_rou:,.0f} | {new_rou:,.0f} |
            | New Annual Depreciation | — | {new_rou/new_term:,.0f} |
            """)

        # ──────────────────────────────────────────────────────────────
        elif calc_type == "4. Lessor: Finance Lease Schedule":
            st.subheader("Lessor: Finance Lease — Net Investment Schedule")
            c1, c2, c3 = st.columns(3)
            with c1:
                annual_receipt = st.number_input("Annual Lease Receipt (BDT)", value=600_000, step=10_000)
                l_term = st.number_input("Lease Term (years)", value=4, min_value=1, max_value=20)
            with c2:
                impl_rate = st.number_input("Interest Rate Implicit in Lease (%)", value=9.0, step=0.25) / 100
                unguaranteed_rv = st.number_input("Unguaranteed Residual Value (BDT)", value=100_000, step=5_000)
            with c3:
                asset_fv = st.number_input("Fair Value of Asset (BDT)", value=2_000_000, step=50_000)
                asset_ca = st.number_input("Carrying Amount of Asset (BDT)", value=1_600_000, step=50_000)

            pv_pmts = annual_receipt * (1 - (1 + impl_rate)**-l_term) / impl_rate if impl_rate > 0 else annual_receipt * l_term
            pv_rv = unguaranteed_rv / (1 + impl_rate)**l_term if impl_rate > 0 else unguaranteed_rv
            net_inv = pv_pmts + pv_rv
            selling_profit = asset_fv - asset_ca

            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Net Investment in Lease", f"BDT {net_inv:,.0f}")
            col_b.metric("Selling Profit", f"BDT {selling_profit:,.0f}")
            col_c.metric("Implicit Rate", f"{impl_rate*100:.2f}%")

            rows_f = []
            bal_f = net_inv
            for y in range(1, l_term + 1):
                fi = round(bal_f * impl_rate, 0)
                closing_f = max(bal_f + fi - annual_receipt, 0)
                rows_f.append({
                    "Year": y,
                    "Opening Net Investment": f"{bal_f:,.0f}",
                    f"Finance Income ({impl_rate*100:.2f}%)": f"{fi:,.0f}",
                    "Receipt": f"{annual_receipt:,.0f}",
                    "Closing Net Investment": f"{closing_f:,.0f}"
                })
                bal_f = closing_f
            st.dataframe(pd.DataFrame(rows_f), use_container_width=True)

        # ──────────────────────────────────────────────────────────────
        elif calc_type == "5. Lessor: Operating Lease — Straight-line Income":
            st.subheader("Lessor: Operating Lease — Straight-line Rental Income")
            n_years = st.number_input("Lease Term (years)", value=3, min_value=1, max_value=20)
            st.markdown("Enter annual cash rental for each year:")
            rents = []
            cols = st.columns(min(int(n_years), 5))
            for i in range(int(n_years)):
                with cols[i % 5]:
                    r = st.number_input(f"Year {i+1} Rent (BDT)", value=400_000 + i * 50_000, step=10_000, key=f"rent_{i}")
                    rents.append(r)

            incentive_paid = st.number_input("Lease Incentive Paid to Tenant (BDT)", value=0, step=5_000)
            asset_cost = st.number_input("Asset Cost / CA (BDT)", value=5_000_000, step=100_000)
            uel = st.number_input("Asset Useful Economic Life (years)", value=20, min_value=1)

            total_rent = sum(rents) - incentive_paid
            sl_income = total_rent / n_years
            annual_dep_lessor = asset_cost / uel

            rows_ol = []
            cumulative_accrual = 0
            for i, r in enumerate(rents):
                accrual = sl_income - r
                cumulative_accrual += accrual
                rows_ol.append({
                    "Year": i + 1,
                    "Cash Rent": f"{r:,.0f}",
                    "SL Income": f"{sl_income:,.0f}",
                    "Accrual / (Deferral)": f"{accrual:,.0f}",
                    "Cumulative Balance": f"{cumulative_accrual:,.0f}",
                    "Depreciation": f"{annual_dep_lessor:,.0f}",
                    "Net P&L": f"{sl_income - annual_dep_lessor:,.0f}"
                })
            st.dataframe(pd.DataFrame(rows_ol), use_container_width=True)
            st.info(f"Annual Straight-line Rental Income: **BDT {sl_income:,.0f}** | Annual Depreciation: **BDT {annual_dep_lessor:,.0f}**")

        # ──────────────────────────────────────────────────────────────
        else:  # Sale and Leaseback
            st.subheader("Sale and Leaseback Calculator")
            c1, c2 = st.columns(2)
            with c1:
                asset_ca_sb = st.number_input("Carrying Amount of Asset (BDT)", value=3_000_000, step=50_000)
                proceeds = st.number_input("Sale Proceeds (BDT)", value=4_000_000, step=50_000)
                fv_sb = st.number_input("Fair Value of Asset (BDT)", value=4_000_000, step=50_000)
            with c2:
                sb_pmt = st.number_input("Annual Leaseback Payment (BDT)", value=400_000, step=10_000)
                sb_term = st.number_input("Leaseback Term (years)", value=5, min_value=1)
                sb_rate = st.number_input("IBR (%)", value=8.0, step=0.25) / 100

            lease_liab_sb = sb_pmt * (1 - (1 + sb_rate)**-sb_term) / sb_rate if sb_rate > 0 else sb_pmt * sb_term
            prop_retained = lease_liab_sb / fv_sb
            prop_sold = 1 - prop_retained
            rou_sb = prop_retained * asset_ca_sb

            # Adjust for non-arm's length proceeds
            proceeds_adj = proceeds
            if proceeds > fv_sb:
                extra = proceeds - fv_sb
                lease_liab_sb_adj = lease_liab_sb - extra  # excess is prepaid rent
                adj_note = f"Proceeds > FV by BDT {extra:,.0f} → reduce Lease Liability (prepaid rent)"
            elif proceeds < fv_sb:
                shortfall = fv_sb - proceeds
                lease_liab_sb_adj = lease_liab_sb + shortfall  # shortfall is additional lease payment
                adj_note = f"Proceeds < FV by BDT {shortfall:,.0f} → increase Lease Liability (additional rent)"
            else:
                lease_liab_sb_adj = lease_liab_sb
                adj_note = "Proceeds = Fair Value — no adjustment needed"

            gain_recognised = prop_sold * (fv_sb - asset_ca_sb)

            st.markdown(f"**ℹ️ Adjustment Note:** {adj_note}")
            st.markdown("---")

            sum_df = pd.DataFrame({
                "Item": ["Lease Liability (PV of payments)", "Proportion of Asset Retained",
                         "Proportion Sold", "ROU Asset", "Gain Recognised in P&L"],
                "Amount": [f"BDT {lease_liab_sb:,.0f}", f"{prop_retained*100:.1f}%",
                           f"{prop_sold*100:.1f}%", f"BDT {rou_sb:,.0f}",
                           f"BDT {gain_recognised:,.0f}"]
            })
            st.table(sum_df)

            st.markdown(f"""
            **Journal Entry:**
            ```
            Dr  Cash                            {proceeds:,.0f}
            Dr  ROU Asset                       {rou_sb:,.0f}
                Cr  Asset (Carrying Amount)         {asset_ca_sb:,.0f}
                Cr  Lease Liability                  {lease_liab_sb_adj:,.0f}
                Cr  Gain on Disposal (P&L)           {gain_recognised:,.0f}
            ```
            *(Rounding differences may arise depending on adjustment)*
            """)

    # ═══════════════════════════════════════════════════════════════════
    # TAB 4 — QUIZ
    # ═══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("Quiz — Test Your Knowledge of IFRS 16")
        st.markdown("Answer each question and check your score.")

        # Q1
        st.markdown("---")
        st.markdown("**Q1. Under IFRS 16, which of the following statements is CORRECT about the lessee accounting model?**")
        q1 = st.radio("Select:", [
            "Operating leases remain off-balance sheet as under IAS 17",
            "All leases (except short-term and low-value) must be recognised on the balance sheet as a ROU Asset and Lease Liability",
            "Only finance leases are recognised on the balance sheet",
            "The choice of on- or off-balance sheet is an accounting policy election for each lease"
        ], key="ifrs16q1")
        if st.button("Check Answer", key="ifrs16c1"):
            if q1 == "All leases (except short-term and low-value) must be recognised on the balance sheet as a ROU Asset and Lease Liability":
                st.success("✅ Correct! IFRS 16 requires virtually all leases to be on the balance sheet. Only the two practical expedients (short-term ≤ 12 months and low-value assets) allow off-balance-sheet treatment.")
            else:
                st.error("❌ Incorrect. **IFRS 16** requires a ROU Asset and Lease Liability for all leases except short-term (≤12 months) and low-value assets.")

        # Q2
        st.markdown("---")
        st.markdown("**Q2. A company leases a photocopier worth USD 4,000 when new, for 2 years. What is the correct accounting treatment?**")
        q2 = st.radio("Select:", [
            "Recognise ROU Asset and Lease Liability — it's a 2-year lease",
            "Apply the low-value asset exemption — expense payments on a straight-line basis",
            "Apply the short-term lease exemption — expense payments on a straight-line basis",
            "Either low-value or short-term exemption may apply — choose the more convenient"
        ], key="ifrs16q2")
        if st.button("Check Answer", key="ifrs16c2"):
            if q2 == "Apply the low-value asset exemption — expense payments on a straight-line basis":
                st.success("✅ Correct! The asset value when new (≈ USD 4,000) is below the IASB's guidance threshold of approximately USD 5,000 → low-value asset exemption applies regardless of lease term.")
            else:
                st.error("❌ Incorrect. The low-value test is based on the asset value **when new** (≈ USD 5,000 threshold). Photocopier qualifies → **low-value exemption**.")

        # Q3
        st.markdown("---")
        st.markdown("**Q3. The ROU Asset at commencement date equals which of the following?**")
        q3 = st.radio("Select:", [
            "Only the initial lease liability",
            "Initial lease liability + initial direct costs + prepaid rent − lease incentives received + dismantling costs",
            "Present value of all future lease payments",
            "Fair value of the underlying asset"
        ], key="ifrs16q3")
        if st.button("Check Answer", key="ifrs16c3"):
            if q3 == "Initial lease liability + initial direct costs + prepaid rent − lease incentives received + dismantling costs":
                st.success("✅ Correct! The ROU Asset is built up from the lease liability plus additional components. IFRS 16.24 specifies all these adjustments.")
            else:
                st.error("❌ Incorrect. **IFRS 16.24**: ROU Asset = Lease Liability + Initial Direct Costs + Prepaid Rent − Incentives Received + Dismantling Provision.")

        # Q4
        st.markdown("---")
        st.markdown("**Q4. How is interest on the lease liability classified in the lessee's income statement?**")
        q4 = st.radio("Select:", [
            "As an operating expense alongside depreciation",
            "As a finance cost — below operating profit",
            "As a reduction in the lease payments (not shown in P&L)",
            "Capitalised into the ROU asset"
        ], key="ifrs16q4")
        if st.button("Check Answer", key="ifrs16c4"):
            if q4 == "As a finance cost — below operating profit":
                st.success("✅ Correct! Interest on the lease liability is a finance cost per IFRS 16.49(b), shown below operating profit. This is a key difference from IAS 17 where the operating lease cost was in operating expenses.")
            else:
                st.error("❌ Incorrect. Interest on the lease liability = **finance cost** (below operating profit). Depreciation is the operating expense.")

        # Q5
        st.markdown("---")
        st.markdown("**Q5. A lessee has an option to extend a 3-year lease by 2 years. At commencement, the lessee is 'reasonably certain' to exercise the option. What is the lease term used for measurement?**")
        q5 = st.radio("Select:", [
            "3 years — the non-cancellable period only",
            "5 years — including the extension period",
            "2 years — the extension option period only",
            "3 years — unless the option is contractually exercised"
        ], key="ifrs16q5")
        if st.button("Check Answer", key="ifrs16c5"):
            if q5 == "5 years — including the extension period":
                st.success("✅ Correct! IFRS 16.19 — the lease term includes optional extension periods when the lessee is reasonably certain to exercise them. Lease term = 3 + 2 = 5 years.")
            else:
                st.error("❌ Incorrect. **IFRS 16.19**: Lease term includes extension periods when **reasonably certain** to exercise → 3 + 2 = **5 years**.")

        # Q6
        st.markdown("---")
        st.markdown("**Q6. Under IFRS 16, how does a LESSOR classify leases?**")
        q6 = st.radio("Select:", [
            "All leases are treated as finance leases",
            "All leases are treated as operating leases (since IFRS 16 only changed lessee accounting)",
            "Leases are classified as either finance or operating based on transfer of risks and rewards",
            "Lessors apply the same single model as lessees (ROU asset + lease receivable)"
        ], key="ifrs16q6")
        if st.button("Check Answer", key="ifrs16c6"):
            if q6 == "Leases are classified as either finance or operating based on transfer of risks and rewards":
                st.success("✅ Correct! IFRS 16 did NOT change lessor accounting significantly. Lessors still classify leases as Finance (risks/rewards transferred) or Operating (risks/rewards retained) — similar to IAS 17.")
            else:
                st.error("❌ Incorrect. IFRS 16 kept the **dual lessor model**: Finance Lease (risks/rewards transferred) vs Operating Lease (risks/rewards retained).")

        # Q7
        st.markdown("---")
        st.markdown("**Q7. In a finance lease, what does the lessor recognise at commencement?**")
        q7 = st.radio("Select:", [
            "The underlying asset at cost, and deferred rental income",
            "Derecognise the asset and recognise a net investment in the lease (lease receivable)",
            "A ROU asset from the lessee's perspective",
            "Rental income on a straight-line basis over the lease term"
        ], key="ifrs16q7")
        if st.button("Check Answer", key="ifrs16c7"):
            if q7 == "Derecognise the asset and recognise a net investment in the lease (lease receivable)":
                st.success("✅ Correct! IFRS 16.67 — the lessor derecognises the underlying asset and recognises a net investment in the lease equal to the PV of lease payments + PV of unguaranteed residual value.")
            else:
                st.error("❌ Incorrect. **IFRS 16.67**: Finance lease lessor derecognises the asset and recognises a **net investment in the lease** (receivable at implicit rate).")

        # Q8
        st.markdown("---")
        st.markdown("**Q8. A sale and leaseback transaction qualifies as a sale under IFRS 15. Proceeds equal fair value. What gain does the seller-lessee recognise?**")
        q8 = st.radio("Select:", [
            "The full gain: proceeds minus carrying amount of the asset",
            "No gain — all profit is deferred and amortised over the lease term",
            "Only the gain relating to the proportion of rights transferred to the buyer",
            "The gain is offset against the ROU Asset and not shown in P&L"
        ], key="ifrs16q8")
        if st.button("Check Answer", key="ifrs16c8"):
            if q8 == "Only the gain relating to the proportion of rights transferred to the buyer":
                st.success("✅ Correct! IFRS 16.100 — only the portion of the gain related to the rights sold (not retained via the leaseback) is recognised in P&L. The retained portion adjusts the ROU asset.")
            else:
                st.error("❌ Incorrect. **IFRS 16.100**: Only gain on the **proportion SOLD** (rights transferred) is recognised in P&L. The retained portion increases the ROU Asset.")

        # Q9
        st.markdown("---")
        st.markdown("**Q9. A lease modification adds the right to use an additional floor of a building, and consideration increases by an amount equal to the standalone price. How is this accounted for?**")
        q9 = st.radio("Select:", [
            "Remeasure the existing lease liability at the revised discount rate",
            "Account for it as a new, separate lease",
            "Expense the additional consideration immediately",
            "Adjust the existing ROU asset upwards with no change to liability"
        ], key="ifrs16q9")
        if st.button("Check Answer", key="ifrs16c9"):
            if q9 == "Account for it as a new, separate lease":
                st.success("✅ Correct! IFRS 16.44 — when a modification adds the right to use an additional asset AND consideration increases by the standalone price, it is treated as a new, separate lease.")
            else:
                st.error("❌ Incorrect. **IFRS 16.44**: Additional asset + standalone-price increase = **new separate lease**. Remeasurement applies only to all other modifications.")

        # Q10
        st.markdown("---")
        st.markdown("**Q10. Variable lease payments that depend on usage (e.g. per kilometre driven) are:**")
        q10 = st.radio("Select:", [
            "Included in the lease liability at the expected usage amount",
            "Included using the current usage rate at commencement",
            "Excluded from the lease liability and expensed as incurred",
            "Capitalised into the ROU asset and depreciated"
        ], key="ifrs16q10")
        if st.button("Check Answer", key="ifrs16c10"):
            if q10 == "Excluded from the lease liability and expensed as incurred":
                st.success("✅ Correct! IFRS 16.38(b) — variable lease payments that do NOT depend on an index or rate (i.e. usage-based) are excluded from the lease liability measurement. They are expensed in the period incurred.")
            else:
                st.error("❌ Incorrect. **IFRS 16.38(b)**: Usage-based variable payments are **excluded** from the lease liability and expensed when incurred.")

        # Q11
        st.markdown("---")
        st.markdown("**Q11. What is the correct depreciation period for a lessee's ROU asset when there is NO purchase option and no indication ownership will transfer?**")
        q11 = st.radio("Select:", [
            "The useful economic life of the underlying asset",
            "The shorter of: the lease term and the useful economic life of the underlying asset",
            "The longer of: the lease term and the useful economic life",
            "Always 10 years (the maximum practical expedient)"
        ], key="ifrs16q11")
        if st.button("Check Answer", key="ifrs16c11"):
            if q11 == "The shorter of: the lease term and the useful economic life of the underlying asset":
                st.success("✅ Correct! IFRS 16.31 — depreciate over the shorter of the lease term and the UEL. If ownership transfers or a purchase option is reasonably certain, use the UEL of the asset.")
            else:
                st.error("❌ Incorrect. **IFRS 16.31**: Depreciation period = **shorter of lease term and UEL** (unless ownership transfer/purchase option is reasonably certain → use UEL).")

        # Q12
        st.markdown("---")
        st.markdown("**Q12. How does an intermediate lessor classify a sub-lease under IFRS 16?**")
        q12 = st.radio("Select:", [
            "Based on the underlying physical asset",
            "Based on the ROU asset arising from the head lease",
            "Always as a finance lease since the intermediate lessor is also a lessee",
            "Always as an operating lease — classification is irrelevant for sub-leases"
        ], key="ifrs16q12")
        if st.button("Check Answer", key="ifrs16c12"):
            if q12 == "Based on the ROU asset arising from the head lease":
                st.success("✅ Correct! IFRS 16.B58 — an intermediate lessor classifies a sub-lease with reference to the ROU asset arising from the head lease, NOT the underlying physical asset.")
            else:
                st.error("❌ Incorrect. **IFRS 16.B58**: Sub-lease is classified based on the **ROU asset** from the head lease — not the physical asset itself.")

    # ═══════════════════════════════════════════════════════════════════
    # TAB 5 — SUMMARY
    # ═══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("Module Summary — IFRS 16 Leases")

        st.markdown("""
        ### 🎯 The Core IFRS 16 Framework at a Glance

        | Party | Lease Type | Balance Sheet | P&L Impact |
        |-------|-----------|---------------|------------|
        | **Lessee** | All leases (except exemptions) | ROU Asset + Lease Liability | Depreciation (ops) + Interest (finance) |
        | **Lessee** | Short-term / Low-value | Nothing | Straight-line lease expense (ops) |
        | **Lessor** | Finance Lease | Net Investment in Lease (receivable) | Finance income + Selling profit |
        | **Lessor** | Operating Lease | Underlying asset retained | Rental income (S/L) − Depreciation |
        """)

        st.markdown("""
        ### 🔢 Key Formulas

        ```
        Lease Liability (initial)
            = PV of: Fixed payments + Index-linked variable payments
                   + Amounts under RVG + Purchase option price (if reasonably certain)
                   + Termination penalties (if lease term reflects exercise)
              discounted at: Implicit rate (preferred) OR Lessee's IBR

        ROU Asset (initial)
            = Lease Liability
            + Initial Direct Costs
            + Lease Payments Made at/Before Commencement (net of incentives)
            + Dismantling/Restoration Provision (IAS 37)

        Lease Liability (subsequent)
            = Opening Balance + Interest Accrued − Lease Payment

        Net Investment in Lease (Lessor — Finance)
            = PV of Lease Payments Receivable + PV of Unguaranteed Residual Value
              (at rate implicit in the lease)

        Sale & Leaseback Gain
            = (Proceeds − CA) × Proportion Sold
            where Proportion Sold = 1 − (Lease Liability / Fair Value)
        ```
        """)

        st.markdown("""
        ### 📋 Recognition: Key Rules

        | Rule | Detail |
        |------|--------|
        | Short-term exemption | Lease term ≤ 12 months at commencement; elected by CLASS |
        | Low-value exemption | Asset value when new ≈ ≤ USD 5,000; per individual asset |
        | Lease term — extension | Include if lessee is **reasonably certain** to exercise |
        | Lease term — termination | Include remaining term if lessee is **reasonably certain NOT** to exercise |
        | Discount rate | Implicit rate preferred; IBR if implicit not determinable |
        | Depreciation period | Shorter of lease term and UEL (unless ownership/purchase option certain → UEL) |
        | Modification → new lease | Only when: new asset + commensurate standalone price increase |
        | Sub-lease classification | Based on **ROU Asset** (not physical asset) |
        | Deferred tax | ROU Asset → DTL; Lease Liability → DTA (often offset at commencement) |
        """)

        st.markdown("""
        ### ⚠️ Common Pitfalls & Exam Traps

        | Trap | Correct Treatment |
        |------|-------------------|
        | All leases off-balance-sheet? | ❌ Only short-term and low-value qualify for off-B/S |
        | Lease expense in operating profit? | ❌ Depreciation in ops; **Interest is finance cost** |
        | Low-value = immaterial to the entity? | ❌ Low-value is tested on the **underlying asset when new** — not materiality to lessee |
        | ROU Asset = Lease Liability always? | ❌ ROU Asset also includes IDC, prepayments, dismantling costs |
        | Modification always remeasures existing lease? | ❌ New asset + standalone price → **new separate lease** |
        | Sub-lease based on physical asset? | ❌ Sub-lease classification based on **ROU asset** |
        | Lessor changed significantly under IFRS 16? | ❌ Lessor accounting largely unchanged from IAS 17 |
        | Full sale gain in Sale & Leaseback? | ❌ Only gain on **proportion SOLD** is recognised |
        | Usage-based payments in lease liability? | ❌ Usage-based payments are excluded; expensed when incurred |
        | Discount using proposed (not yet enacted) rate? | ❌ Use IBR at **commencement date** (enacted rate) |
        """)

        st.markdown("""
        ### 📊 Decision Flowchart: Lessee Accounting

        ```
        Does the contract contain a lease? (Identified asset + economic benefits + direct use)
                        │
                  Yes   │   No → Expense as service cost
                        ▼
        Is it SHORT-TERM (≤ 12 months) or LOW-VALUE (asset ≤ ~USD 5,000 when new)?
                ┌───────┴────────┐
               Yes              No
                │                │
                ▼                ▼
        Expense on          Recognise on Balance Sheet:
        straight-line       ROU Asset + Lease Liability
                                │
                                ▼
                    P&L: Depreciation (ops) + Interest (finance)
        ```
        """)

        st.markdown("""
        ### 📊 Decision Flowchart: Lessor Classification

        ```
        Does the lease transfer substantially all risks and rewards of ownership?
                ┌─────────────────────────────────────────────┐
               YES                                            NO
                │                                             │
                ▼                                             ▼
        FINANCE LEASE                               OPERATING LEASE
        ─────────────                               ───────────────
        Derecognise asset                           Keep asset on balance sheet
        Recognise Net Investment                    Recognise rental income (S/L)
        Finance income via EIM                      Continue to depreciate asset
        Manufacturer lessor:                        Deferred initial direct costs
        → recognise selling profit                  amortised over lease term
        ```
        """)

        st.markdown("""
        ### 📌 IFRS 16 Key Paragraph Reference Map

        ```
        IFRS 16
        ├── Para 9–11     →  Definition of a lease (identified asset, economic benefits, direct use)
        ├── Para 5        →  Scope exclusions
        ├── Para 5(a)–(b) →  Short-term and low-value practical expedients
        ├── Para 19–21    →  Lease term determination (including options)
        ├── Para 22–28    →  Lessee: initial recognition (Lease Liability & ROU Asset)
        ├── Para 26–28    →  Components of ROU Asset
        ├── Para 29–33    →  Lessee: subsequent measurement of ROU Asset
        ├── Para 36–46    →  Lessee: subsequent measurement of Lease Liability
        ├── Para 44–46    →  Lease modifications — lessee
        ├── Para 47–60    →  Lessee: presentation and disclosure
        ├── Para 61–65    →  Lessor: classification (finance vs operating)
        ├── Para 67–80    →  Lessor: finance lease accounting
        ├── Para 81–97    →  Lessor: operating lease accounting
        ├── Para 98–103   →  Sale and leaseback transactions
        ├── Para B58–B62  →  Sub-leases
        └── Appendix A    →  Defined terms
        ```
        """)

        st.markdown("""
        ### 💡 Practical Tips for Preparers

        1. **Build a lease register** — track every lease, including commencement date, term, payments, IBR, ROU asset and liability balances
        2. **Review extension options** annually — reassess "reasonably certain" judgement when facts change
        3. **Document the IBR** — it is a key judgement; use a rate for a similar asset, term, and credit quality
        4. **Variable payments** — distinguish index/rate-linked (in liability) from usage-based (expensed)
        5. **Modification checklist** — always first ask: does this add a new asset at standalone price? If yes → new lease
        6. **Sale & leaseback** — determine IFRS 15 sale first; then calculate proportion retained vs sold
        7. **Deferred tax** — map ROU Asset to DTL and Lease Liability to DTA at each reporting date
        8. **Disclosures** — prepare a maturity analysis of undiscounted lease payments (at least 5 years + remaining)
        """)

        st.success("🎓 **Module Complete!** You now understand the full mechanism of Leases under IFRS 16 — from identifying a lease and lessee on-balance-sheet accounting, to lessor classification, sale and leaseback, modifications, sub-leases, and variable payments.")
        st.info("📘 **Reference Standard:** IFRS 16 Leases (as issued by the IASB, effective 1 January 2019). Always consult the latest version and applicable jurisdiction supplements.")


if __name__ == "__main__":
    show()