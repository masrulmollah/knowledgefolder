import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📉 IAS 36: Impairment of Assets")
    st.markdown("*Master impairment testing, recoverable amount calculation, and CGU allocation*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and Scope")
        st.markdown("""
        **IAS 36** ensures that assets are **not carried at more than their recoverable amount**. If carrying amount > recoverable amount, the asset is impaired and must be written down.

        **Applies to:** PPE (IAS 16), intangible assets (IAS 38), investment property at cost, investments in subsidiaries/associates/JVs, right-of-use assets (IFRS 16), goodwill.

        **Excluded (have their own impairment rules):** Inventories (IAS 2), financial assets (IFRS 9), deferred tax assets (IAS 12), investment property at fair value (IAS 40), biological assets at FV (IAS 41), non-current assets held for sale (IFRS 5).
        """)

        st.subheader("2. When to Test for Impairment")
        st.markdown("""
        **Annual mandatory testing (regardless of indicators):**
        - Intangible assets with indefinite useful lives
        - Intangible assets not yet available for use
        - **Goodwill acquired in a business combination**

        **Trigger-based testing (all other assets — test when indicators exist):**

        | External Indicators | Internal Indicators |
        |---|---|
        | Significant decline in market value | Evidence of obsolescence or physical damage |
        | Adverse changes in technology/market/economy/law | Asset more idle than expected |
        | Increase in market interest rates | Net assets of entity > market capitalisation |
        | Market capitalisation below net asset value | Evidence from internal reporting of poor performance |
        """)

        st.subheader("3. Recoverable Amount")
        st.markdown("""
        ```
        Recoverable Amount = HIGHER of:
            Fair Value Less Costs of Disposal (FVLCD)
            Value in Use (VIU)
        ```

        **Fair Value Less Costs of Disposal (FVLCD):**
        - Best estimate of amount obtainable from sale in an arm's length transaction
        - Less the direct costs of disposal
        - Per IFRS 13 fair value hierarchy

        **Value in Use (VIU):**
        - PV of future cash flows expected from the asset
        - Use pre-tax cash flows and pre-tax discount rate
        - Cash flows include operations + eventual disposal
        - Discount rate = pre-tax rate reflecting current market assessments of time value and risks specific to the asset
        """)

        st.subheader("4. Cash-Generating Units (CGUs)")
        st.markdown("""
        When it is **not possible to estimate recoverable amount of an individual asset**, identify the smallest group of assets that generates independent cash inflows — the **CGU**.

        **Key rules:**
        - Identify CGUs consistently from period to period
        - CGU recoverable amount tested against CGU carrying amount (including allocated goodwill)
        - Goodwill must be allocated to CGUs for impairment testing purposes
        - Corporate assets that cannot be allocated directly → allocate on a reasonable and consistent basis

        **Impairment loss allocation within CGU:**
        1. First: reduce carrying amount of any **goodwill** allocated to the CGU
        2. Then: reduce carrying amounts of other assets **pro-rata** based on carrying amount
        3. Never reduce below the highest of: FVLCD, VIU, or zero
        """)

        st.subheader("5. Impairment Loss Recognition")
        st.markdown("""
        - **Cost model assets:** impairment loss → **P&L** immediately
        - **Revaluation model assets (IAS 16/38):** impairment loss first reduces the **revaluation surplus** for that asset in OCI; excess → P&L
        - Adjust future depreciation based on revised carrying amount and remaining useful life

        **Reversal of Impairment:**
        - Assess at each balance sheet date for indicators that prior impairment may have reversed
        - Reverse if recoverable amount has increased
        - Maximum reversal = **carrying amount that would have been recorded (net of depreciation) had no impairment occurred**
        - **Goodwill impairment: NEVER reversed**
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Single Asset Impairment Test")
        st.markdown("""
        **Machine:** Carrying amount = $500,000 | FVLCD = $380,000 | VIU = $420,000

        - **Recoverable Amount** = max($380,000, $420,000) = **$420,000**
        - **Impairment Loss** = $500,000 − $420,000 = **$80,000 → P&L**

        ```
        Dr  Impairment Loss (P&L)    $80,000
            Cr  Accumulated Impairment     $80,000
        ```
        """)

        st.subheader("Example 2: CGU with Goodwill — Impairment Allocation")
        st.markdown("""
        **CGU carrying amounts:**

        | Asset | Carrying Amount |
        |---|---|
        | Goodwill | $200,000 |
        | PPE | $600,000 |
        | Intangibles | $300,000 |
        | Net Working Capital | $100,000 |
        | **Total CGU** | **$1,200,000** |

        **Recoverable Amount of CGU = $900,000**
        **Impairment Loss = $1,200,000 − $900,000 = $300,000**

        **Allocation:**
        | Asset | Before | Impairment | After |
        |---|---|---|---|
        | Goodwill | $200,000 | ($200,000) — first | $0 |
        | PPE | $600,000 | ($66,667)* | $533,333 |
        | Intangibles | $300,000 | ($33,333)* | $266,667 |
        | Net WC | $100,000 | $0 — not impaired below NRV | $100,000 |
        | **Total** | **$1,200,000** | **(300,000)** | **$900,000** |

        *Remaining $100,000 allocated pro-rata: PPE = 600/900 × 100k; Intangibles = 300/900 × 100k
        """)

        st.subheader("Example 3: Value in Use Calculation")
        st.markdown("""
        **Asset: Production machine. Discount rate: 10% (pre-tax)**

        | Year | Cash Inflow | Cash Outflow | Net Cash Flow | Discount Factor | PV |
        |---|---|---|---|---|---|
        | 1 | $300,000 | ($180,000) | $120,000 | 0.909 | $109,091 |
        | 2 | $280,000 | ($170,000) | $110,000 | 0.826 | $90,909 |
        | 3 | $260,000 | ($160,000) | $100,000 | 0.751 | $75,131 |
        | 3 (disposal) | $50,000 | ($5,000) | $45,000 | 0.751 | $33,809 |
        | **VIU** | | | | | **$308,940** |
        """)

        st.subheader("Example 4: Reversal of Impairment")
        st.markdown("""
        **Facts:**
        - Original cost: $1,000,000 | Useful life 10 years
        - Year 3 impairment to $600,000 | Revised RA of $600,000
        - Year 5: recoverable amount now $750,000

        **Carrying amount at Year 5 (post-impairment depreciation):**
        - Year 3 CA: $600,000; remaining life 7 years → depreciation $85,714/year
        - Year 5 CA: $600,000 − (2 × $85,714) = **$428,571**

        **CA had no impairment occurred:**
        - $1,000,000 − (5 × $100,000) = **$500,000**

        **Reversal = min(RA, original CA) − current CA = min($750,000, $500,000) − $428,571 = $71,429**
        → Capped at what would have been recognised had no impairment occurred.
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Recoverable Amount Calculator")
        col1, col2 = st.columns(2)
        with col1:
            carrying = st.number_input("Carrying Amount ($)", value=500000, step=10000)
            fvlcd = st.number_input("Fair Value Less Costs of Disposal ($)", value=380000, step=10000)
            viu = st.number_input("Value in Use ($)", value=420000, step=10000)
        with col2:
            ra = max(fvlcd, viu)
            impairment = max(0, carrying - ra)
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | FVLCD | ${fvlcd:,.0f} |
            | Value in Use | ${viu:,.0f} |
            | **Recoverable Amount (higher)** | **${ra:,.0f}** |
            | Carrying Amount | ${carrying:,.0f} |
            | **Impairment Loss** | **${impairment:,.0f}** |
            """)
            if impairment > 0:
                st.error(f"⚠️ Impairment loss of ${impairment:,.0f} must be recognised in P&L.")
            else:
                st.success("✅ No impairment — carrying amount does not exceed recoverable amount.")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Value in Use Calculator (DCF)")
        discount_rate = st.number_input("Pre-tax Discount Rate (%)", value=10.0, step=0.5) / 100
        n_years = st.number_input("Projection Period (years)", value=5, min_value=1, max_value=10)
        st.markdown("Enter annual net cash flows:")
        cash_flows = []
        cols = st.columns(int(n_years))
        for i, col in enumerate(cols):
            cf = col.number_input(f"Year {i+1} ($)", value=100000, step=5000, key=f"cf_{i}")
            cash_flows.append(cf)
        terminal_value = st.number_input("Terminal/Disposal Value at end ($)", value=50000, step=5000)

        if st.button("Calculate VIU"):
            rows = []
            total_viu = 0
            for i, cf in enumerate(cash_flows):
                yr = i + 1
                df = 1 / (1 + discount_rate)**yr
                pv = cf * df
                total_viu += pv
                rows.append({"Year": yr, "Net Cash Flow ($)": f"{cf:,.0f}", "Discount Factor": f"{df:.4f}", "PV ($)": f"{pv:,.0f}"})
            tv_pv = terminal_value / (1 + discount_rate)**int(n_years)
            total_viu += tv_pv
            rows.append({"Year": f"Yr {int(n_years)} (disposal)", "Net Cash Flow ($)": f"{terminal_value:,.0f}", "Discount Factor": f"{1/(1+discount_rate)**int(n_years):.4f}", "PV ($)": f"{tv_pv:,.0f}"})
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            st.success(f"**Value in Use = ${total_viu:,.0f}**")

        st.markdown("---")
        st.subheader("🔧 Tool 3: CGU Impairment Allocation")
        st.markdown("Allocate impairment loss across a CGU:")
        goodwill_cv = st.number_input("Goodwill ($)", value=200000, step=10000)
        ppe_cv = st.number_input("PPE ($)", value=600000, step=10000)
        intangibles_cv = st.number_input("Intangibles ($)", value=300000, step=10000)
        other_cv = st.number_input("Other assets ($)", value=100000, step=10000)
        cgu_ra = st.number_input("CGU Recoverable Amount ($)", value=900000, step=10000)

        if st.button("Allocate Impairment"):
            total_cgu = goodwill_cv + ppe_cv + intangibles_cv + other_cv
            total_imp = max(0, total_cgu - cgu_ra)
            if total_imp == 0:
                st.success(f"✅ No impairment. CGU carrying amount ${total_cgu:,.0f} ≤ RA ${cgu_ra:,.0f}")
            else:
                gw_imp = min(goodwill_cv, total_imp)
                remaining_imp = total_imp - gw_imp
                other_assets = ppe_cv + intangibles_cv + other_cv
                ppe_imp = (ppe_cv / other_assets) * remaining_imp if other_assets > 0 else 0
                int_imp = (intangibles_cv / other_assets) * remaining_imp if other_assets > 0 else 0
                oth_imp = (other_cv / other_assets) * remaining_imp if other_assets > 0 else 0
                alloc = pd.DataFrame({
                    "Asset": ["Goodwill", "PPE", "Intangibles", "Other", "TOTAL"],
                    "Before ($)": [f"{goodwill_cv:,.0f}", f"{ppe_cv:,.0f}", f"{intangibles_cv:,.0f}", f"{other_cv:,.0f}", f"{total_cgu:,.0f}"],
                    "Impairment ($)": [f"({gw_imp:,.0f})", f"({ppe_imp:,.0f})", f"({int_imp:,.0f})", f"({oth_imp:,.0f})", f"({total_imp:,.0f})"],
                    "After ($)": [f"{goodwill_cv-gw_imp:,.0f}", f"{ppe_cv-ppe_imp:,.0f}", f"{intangibles_cv-int_imp:,.0f}", f"{other_cv-oth_imp:,.0f}", f"{cgu_ra:,.0f}"]
                })
                st.dataframe(alloc, use_container_width=True, hide_index=True)
                st.warning(f"Total impairment: ${total_imp:,.0f} — Goodwill written down first (${gw_imp:,.0f}), remainder allocated pro-rata.")

    with tab4:
        st.header("Visualizations")

        st.subheader("Impairment Test — Decision Flow")
        st.markdown("""
        ```
        Asset at Carrying Amount
                    |
                    ▼
        Check Impairment Indicators (or annual test for GW/indefinite life)
                    |
                    ▼
        Calculate Recoverable Amount = max(FVLCD, VIU)
                    |
            ┌───────┴───────┐
        CA ≤ RA          CA > RA
        No impairment    IMPAIRMENT LOSS = CA − RA
                              |
                         Recognised in P&L
                         (or first vs OCI for revalued assets)
        ```
        """)

        st.subheader("Carrying Amount vs Recoverable Amount — Sensitivity")
        discount_rates = [6, 7, 8, 9, 10, 11, 12, 13, 14]
        annual_cf = 120000; yrs_s = 5; terminal = 80000
        vius = []
        for dr in discount_rates:
            r = dr / 100
            v = sum([annual_cf / (1+r)**t for t in range(1, yrs_s+1)]) + terminal / (1+r)**yrs_s
            vius.append(v)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=discount_rates, y=vius, name="Value in Use", line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig.add_hline(y=500000, line_dash="dash", line_color="#F87171", annotation_text="Carrying Amount $500k")
        fig.update_layout(title="VIU Sensitivity to Discount Rate (Annual CF $120k, 5 years)", xaxis_title="Discount Rate (%)", yaxis_title="Value in Use ($)", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Recoverable amount is defined as:**")
        q1 = st.radio("", [
            "The lower of FVLCD and Value in Use",
            "The higher of FVLCD and Value in Use",
            "Fair value less costs of disposal only",
            "The net book value of the asset"
        ], key="ias36q1")
        if st.button("Check Answer", key="ias36c1"):
            if q1 == "The higher of FVLCD and Value in Use":
                st.success("✅ Correct! Recoverable Amount = HIGHER of FVLCD and VIU. The entity can choose whichever represents the best use of the asset.")
            else:
                st.error("❌ Recoverable Amount = HIGHER of FVLCD and VIU (not the lower).")

        st.markdown("---")
        st.markdown("**2. Goodwill impairment losses:**")
        q2 = st.radio("", [
            "Can be reversed in future periods if conditions improve",
            "Are allocated last in a CGU impairment",
            "Are never reversed",
            "Are recognised in OCI"
        ], key="ias36q2")
        if st.button("Check Answer", key="ias36c2"):
            if q2 == "Are never reversed":
                st.success("✅ Correct! IAS 36 explicitly prohibits reversal of goodwill impairment losses. All other asset impairments may be reversed if conditions improve.")
            else:
                st.error("❌ Goodwill impairment losses are NEVER reversed — this is a specific IAS 36 prohibition.")

        st.markdown("---")
        st.markdown("**3. When allocating a CGU impairment loss, the order is:**")
        q3 = st.radio("", [
            "Pro-rata across all assets including goodwill",
            "First to goodwill, then pro-rata to other assets",
            "First to the largest asset, then to goodwill",
            "To intangibles first, then goodwill, then PPE"
        ], key="ias36q3")
        if st.button("Check Answer", key="ias36c3"):
            if q3 == "First to goodwill, then pro-rata to other assets":
                st.success("✅ Correct! Impairment is first allocated to reduce goodwill to zero, then the remainder is allocated pro-rata to other assets in the CGU (subject to floor limits).")
            else:
                st.error("❌ Allocation order: (1) Goodwill first, (2) then pro-rata to other CGU assets.")

        st.markdown("---")
        st.markdown("**4. Value in Use must use:**")
        q4 = st.radio("", [
            "Post-tax cash flows and post-tax discount rate",
            "Pre-tax cash flows and pre-tax discount rate",
            "Post-tax cash flows and pre-tax discount rate",
            "Management's most optimistic projections"
        ], key="ias36q4")
        if st.button("Check Answer", key="ias36c4"):
            if q4 == "Pre-tax cash flows and pre-tax discount rate":
                st.success("✅ Correct! IAS 36 requires pre-tax cash flows discounted at a pre-tax discount rate. Post-tax approaches should theoretically give the same result but IAS 36 specifies pre-tax.")
            else:
                st.error("❌ VIU must use PRE-TAX cash flows discounted at a PRE-TAX discount rate.")

        st.markdown("---")
        st.markdown("**5. For assets carried under the revaluation model, an impairment loss is:**")
        q5 = st.radio("", [
            "Always recognised immediately in P&L",
            "Always recognised in OCI",
            "First recognised against any existing revaluation surplus for that asset; excess in P&L",
            "Deferred until disposal"
        ], key="ias36q5")
        if st.button("Check Answer", key="ias36c5"):
            if q5 == "First recognised against any existing revaluation surplus for that asset; excess in P&L":
                st.success("✅ Correct! For revalued assets, the impairment loss first offsets any existing revaluation surplus (OCI). Any amount exceeding the surplus is recognised in P&L.")
            else:
                st.error("❌ Revalued assets: impairment first against OCI revaluation surplus, excess to P&L.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Core Rule
        **If Carrying Amount > Recoverable Amount → Impairment Loss**

        ### 2. Recoverable Amount
        ```
        Recoverable Amount = max(FVLCD, VIU)
        FVLCD = Fair Value − Costs of Disposal
        VIU   = PV of future cash flows (pre-tax rate, pre-tax flows)
        ```

        ### 3. Annual Testing Required (no indicators needed)
        - Goodwill from business combinations
        - Intangible assets with indefinite useful lives
        - Intangible assets not yet available for use

        ### 4. CGU Impairment Allocation
        ```
        1st → Goodwill (to zero)
        2nd → Other assets pro-rata (never below floor: max of FVLCD, VIU, zero)
        ```

        ### 5. Reversal Rules
        | Asset | Reversal Permitted? |
        |---|---|
        | PPE, Intangibles, Other | ✅ Yes (capped at would-have-been CA) |
        | **Goodwill** | ❌ **Never** |

        ### 6. P&L vs OCI Treatment
        - Cost model assets → **P&L**
        - Revaluation model → first **OCI** (surplus), excess to **P&L**
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Recoverable Amount = max(FVLCD, VIU)   ← HIGHER not lower
VIU = Pre-tax cash flows × Pre-tax discount rate
Goodwill → mandatory annual test → impairment NEVER reversed
CGU allocation → Goodwill first, then pro-rata
Reversal cap = CA that would have existed (net of depreciation) had no impairment occurred
        """)

        st.success("🎓 **IAS 36 Complete!** You can now identify impairment indicators, calculate recoverable amounts, allocate CGU losses, and account for reversals.")
        st.info("💡 **Next**: IAS 37 — Provisions, Contingent Liabilities and Contingent Assets")

if __name__ == "__main__":
    show()