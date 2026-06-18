import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🤝 IFRS 3: Business Combinations")
    st.markdown("*Master acquisition accounting, goodwill calculation and fair value of identifiable assets*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Scope and the Acquisition Method")
        st.markdown("""
        **IFRS 3** governs accounting for **business combinations** — transactions where an acquirer obtains **control** of one or more businesses.

        **Mandatory method: The Acquisition Method.** Four steps:
        1. **Identify the acquirer** — the entity obtaining control
        2. **Determine the acquisition date** — date control is obtained
        3. **Recognise and measure** identifiable assets acquired, liabilities assumed, and any NCI
        4. **Recognise and measure goodwill** or a gain from a bargain purchase

        **A "business"** requires inputs + substantive processes that together create outputs. Acquiring a single asset or group of assets without processes = **asset acquisition** (not a business combination) → no goodwill, allocate cost based on relative fair values.
        """)

        st.subheader("2. Identifying the Acquirer")
        st.markdown("""
        Normally the entity that:
        - Transfers cash/assets or incurs liabilities (the one paying)
        - Issues its equity interests (unless reverse acquisition)
        - Is significantly larger
        - Initiates the combination

        **Reverse acquisition:** Legal acquirer is the accounting acquiree when the legal acquiree's former owners gain control of the combined entity (common in reverse mergers/SPAC transactions).
        """)

        st.subheader("3. The Goodwill Formula")
        st.markdown("""
        ```
        Goodwill = Consideration Transferred
                 + Fair Value of NCI (if any)
                 + Fair Value of Previously Held Equity Interest (if step acquisition)
                 − Fair Value of Identifiable Net Assets Acquired
        ```

        **Consideration transferred** includes:
        - Cash paid
        - Fair value of equity instruments issued
        - Contingent consideration at fair value (acquisition date)
        - Liabilities assumed by the acquirer to former owners

        **Excludes:** acquisition-related costs (legal, due diligence fees) → these are **EXPENSED** as incurred, NOT included in consideration.

        **If the result is negative** → **Bargain Purchase Gain**, recognised immediately in **P&L** (after reassessing the calculation).
        """)

        st.subheader("4. Measuring Identifiable Assets and Liabilities")
        st.markdown("""
        **General rule:** Recognise at **acquisition-date fair value** (IFRS 13), regardless of their carrying amount in the acquiree's own books.

        | Item | Special Measurement Rule |
        |---|---|
        | Contingent liabilities | Recognise if present obligation and FV reliably measurable (lower threshold than IAS 37) |
        | Deferred tax assets/liabilities | Per IAS 12 — NOT discounted |
        | Employee benefits | Per IAS 19 |
        | Reacquired rights | Based on remaining contractual term, not market participant assumptions |
        | Indemnification assets | Recognise on the same basis as the indemnified item |
        | Intangible assets | Recognise separately if identifiable (e.g., customer relationships, brands, technology) — even if NOT recognised in acquiree's own books |

        **Measurement period:** Up to **12 months** from acquisition date to finalise provisional amounts, with retrospective adjustment to goodwill.
        """)

        st.subheader("5. Non-Controlling Interest (NCI) — Two Measurement Options")
        st.markdown("""
        At acquisition, for each business combination, choose (election made **per transaction**):

        | Method | NCI Measured At | Goodwill Includes NCI's Share? |
        |---|---|---|
        | **Full Goodwill Method** | Fair value of NCI | YES — goodwill includes NCI's share of goodwill |
        | **Partial Goodwill Method** | NCI's proportionate share of net identifiable assets | NO — only parent's share of goodwill recognised |

        This is a significant area where total goodwill differs depending on the election.
        """)

        st.subheader("6. Step Acquisitions and Subsequent Measurement")
        st.markdown("""
        **Step acquisition** (achieving control after holding a previous stake):
        - Remeasure previously held equity interest to **fair value** at acquisition date
        - Gain/loss on remeasurement → **P&L**

        **After acquisition:**
        - Goodwill is NOT amortised — tested for **impairment annually** (IAS 36)
        - Contingent consideration classified as liability → remeasure through P&L each period
        - Contingent consideration classified as equity → not remeasured
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Basic Goodwill Calculation")
        st.markdown("""
        **Acquirer purchases 100% of Target Co for $5,000,000 cash.**

        | Identifiable Net Assets at Fair Value | $ |
        |---|---|
        | PPE | 2,200,000 |
        | Intangibles (customer relationships) | 800,000 |
        | Inventory | 600,000 |
        | Cash | 300,000 |
        | Less: Liabilities assumed | (1,200,000) |
        | **Fair Value of Net Identifiable Assets** | **2,700,000** |

        **Goodwill = $5,000,000 − $2,700,000 = $2,300,000**

        ```
        Dr  PPE                      2,200,000
        Dr  Intangibles                 800,000
        Dr  Inventory                   600,000
        Dr  Cash                        300,000
        Dr  Goodwill                  2,300,000
            Cr  Liabilities                  1,200,000
            Cr  Cash (consideration paid)    5,000,000
        ```
        """)

        st.subheader("Example 2: Acquisition with NCI — Full vs Partial Goodwill")
        st.markdown("""
        Acquirer purchases **80%** of Target Co for $4,000,000.
        Fair value of net identifiable assets = $4,500,000.
        Fair value of NCI (20%) = $950,000 (slightly more than 20% × $4.5M due to control premium absent for NCI).

        **Method 1 — Full Goodwill:**
        | | $ |
        |---|---|
        | Consideration transferred | 4,000,000 |
        | + Fair value of NCI | 950,000 |
        | − Fair value of net identifiable assets | (4,500,000) |
        | **Goodwill (Full)** | **450,000** |

        **Method 2 — Partial Goodwill:**
        | | $ |
        |---|---|
        | Consideration transferred | 4,000,000 |
        | + NCI's proportionate share (20% × 4,500,000) | 900,000 |
        | − Fair value of net identifiable assets | (4,500,000) |
        | **Goodwill (Partial)** | **400,000** |

        Difference of $50,000 = NCI's share of goodwill, included only under Full Goodwill method.
        """)

        st.subheader("Example 3: Bargain Purchase")
        st.markdown("""
        Acquirer pays $3,000,000 for 100% of Target.
        Fair value of net identifiable assets = $3,400,000.

        **Calculation:** $3,000,000 − $3,400,000 = **($400,000)** — NEGATIVE

        After reassessing all measurements (a mandatory step before recognising a bargain purchase):
        **Bargain Purchase Gain of $400,000 → recognised immediately in P&L**

        ```
        Dr  Net Identifiable Assets    3,400,000
            Cr  Cash                        3,000,000
            Cr  Bargain Purchase Gain (P&L)   400,000
        ```
        """)

        st.subheader("Example 4: Step Acquisition")
        st.markdown("""
        Acquirer held 25% of Associate Co (carrying amount $600,000 under equity method).
        Acquirer now buys an additional 55% for $2,500,000, achieving 80% control.
        Fair value of the original 25% stake at acquisition date = $750,000.

        **Step 1 — Remeasure existing stake:**
        Gain = $750,000 − $600,000 = **$150,000 → P&L**

        **Step 2 — Calculate goodwill:**
        | | $ |
        |---|---|
        | Consideration for additional 55% | 2,500,000 |
        | + Fair value of previously held 25% | 750,000 |
        | + Fair value of NCI (20%) | 700,000 |
        | − Fair value of net identifiable assets | (3,200,000) |
        | **Goodwill** | **750,000** |
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Goodwill Calculator")
        col1, col2 = st.columns(2)
        with col1:
            consideration = st.number_input("Consideration Transferred ($)", value=5000000, step=100000)
            nci_method = st.selectbox("NCI Measurement Method", ["100% Acquired (No NCI)", "Full Goodwill (NCI at Fair Value)", "Partial Goodwill (NCI at Proportionate Share)"])
            if "Full" in nci_method:
                nci_fv = st.number_input("Fair Value of NCI ($)", value=950000, step=10000)
            elif "Partial" in nci_method:
                nci_pct = st.number_input("NCI Ownership %", value=20.0, step=1.0) / 100
            fv_net_assets = st.number_input("Fair Value of Net Identifiable Assets ($)", value=2700000, step=100000)
        with col2:
            if nci_method == "100% Acquired (No NCI)":
                goodwill = consideration - fv_net_assets
                st.markdown(f"""
                | Item | Amount |
                |---|---|
                | Consideration transferred | ${consideration:,.0f} |
                | Less: FV of net identifiable assets | (${fv_net_assets:,.0f}) |
                | **Goodwill / (Bargain Purchase)** | **${goodwill:,.0f}** |
                """)
            elif "Full" in nci_method:
                goodwill = consideration + nci_fv - fv_net_assets
                st.markdown(f"""
                | Item | Amount |
                |---|---|
                | Consideration transferred | ${consideration:,.0f} |
                | + Fair value of NCI | ${nci_fv:,.0f} |
                | Less: FV of net identifiable assets | (${fv_net_assets:,.0f}) |
                | **Goodwill (Full Method)** | **${goodwill:,.0f}** |
                """)
            else:
                nci_share = nci_pct * fv_net_assets
                goodwill = consideration + nci_share - fv_net_assets
                st.markdown(f"""
                | Item | Amount |
                |---|---|
                | Consideration transferred | ${consideration:,.0f} |
                | + NCI proportionate share ({nci_pct*100:.0f}%) | ${nci_share:,.0f} |
                | Less: FV of net identifiable assets | (${fv_net_assets:,.0f}) |
                | **Goodwill (Partial Method)** | **${goodwill:,.0f}** |
                """)
            if goodwill >= 0:
                st.success(f"✅ **Goodwill recognised: ${goodwill:,.0f}**")
            else:
                st.warning(f"⚠️ **Bargain Purchase Gain: ${abs(goodwill):,.0f}** → recognise in P&L immediately (after reassessment)")

        st.markdown("---")
        st.subheader("🔧 Tool 2: Asset Acquisition vs Business Combination Classifier")
        has_inputs = st.checkbox("Does the acquired set include economic resources (inputs)?")
        has_process = st.checkbox("Does it include a substantive process (e.g., workforce, operating procedures)?")
        has_output = st.checkbox("Is it capable of producing outputs (goods/services/revenue)?")
        if st.button("Classify Transaction"):
            if has_inputs and has_process:
                st.success("✅ **BUSINESS COMBINATION** — Apply IFRS 3 acquisition method. Recognise goodwill.")
            else:
                st.info("📦 **ASSET ACQUISITION** — Not a business. Allocate cost based on relative fair values of assets acquired. NO goodwill.")

        st.markdown("---")
        st.subheader("🔧 Tool 3: Step Acquisition Calculator")
        col1, col2 = st.columns(2)
        with col1:
            existing_ca = st.number_input("Carrying amount of existing stake ($)", value=600000, step=10000)
            existing_fv = st.number_input("Fair value of existing stake at acquisition date ($)", value=750000, step=10000)
        with col2:
            remeasure_gain = existing_fv - existing_ca
            st.markdown(f"""
            | Item | Amount |
            |---|---|
            | FV of previously held stake | ${existing_fv:,.0f} |
            | Carrying amount before | ${existing_ca:,.0f} |
            | **Remeasurement Gain/(Loss) → P&L** | **${remeasure_gain:,.0f}** |
            """)

    with tab4:
        st.header("Visualizations")

        st.subheader("Goodwill Build-Up — Waterfall Chart")
        items = ["Consideration\nTransferred", "FV of NCI", "FV of Net\nIdentifiable Assets", "Goodwill"]
        values = [4000000, 950000, -4500000, 450000]
        fig = go.Figure(go.Waterfall(
            name="Goodwill Calc", orientation="v",
            measure=["relative", "relative", "relative", "total"],
            x=items, y=values,
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            decreasing={"marker": {"color": "#F87171"}},
            increasing={"marker": {"color": "#34D399"}},
            totals={"marker": {"color": "#2563EB"}}
        ))
        fig.update_layout(title="Goodwill Calculation Waterfall (Full Goodwill Method)", height=420)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Full vs Partial Goodwill Method Comparison")
        methods = ["Full Goodwill\nMethod", "Partial Goodwill\nMethod"]
        parent_gw = [400000, 400000]
        nci_gw = [50000, 0]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=methods, y=parent_gw, name="Parent's Share of Goodwill", marker_color="#2563EB"))
        fig2.add_trace(go.Bar(x=methods, y=nci_gw, name="NCI's Share of Goodwill", marker_color="#F59E0B"))
        fig2.update_layout(barmode="stack", title="Goodwill Allocation — Full vs Partial Method", yaxis_title="Goodwill ($)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. Under IFRS 3, identifiable assets and liabilities acquired are measured at:**")
        q1 = st.radio("", [
            "Acquirer's carrying amount",
            "Acquiree's carrying amount before acquisition",
            "Acquisition-date fair value",
            "Historical cost to the acquiree"
        ], key="ifrs3q1")
        if st.button("Check Answer", key="ifrs3c1"):
            if q1 == "Acquisition-date fair value":
                st.success("✅ Correct! IFRS 3 requires identifiable assets and liabilities to be measured at acquisition-date FAIR VALUE, regardless of their previous carrying amount in the acquiree's books.")
            else:
                st.error("❌ Acquisition method requires measurement at acquisition-date FAIR VALUE per IFRS 13.")

        st.markdown("---")
        st.markdown("**2. Acquisition-related costs (legal fees, due diligence) are:**")
        q2 = st.radio("", [
            "Included in the consideration transferred",
            "Capitalised as part of goodwill",
            "Expensed as incurred in P&L",
            "Deducted from equity"
        ], key="ifrs3q2")
        if st.button("Check Answer", key="ifrs3c2"):
            if q2 == "Expensed as incurred in P&L":
                st.success("✅ Correct! IFRS 3 requires acquisition-related costs to be EXPENSED as incurred — they are NOT part of consideration transferred and do NOT affect goodwill.")
            else:
                st.error("❌ Acquisition costs are EXPENSED, not capitalised into goodwill or consideration.")

        st.markdown("---")
        st.markdown("**3. If the calculated goodwill is negative, this represents:**")
        q3 = st.radio("", [
            "A bargain purchase gain recognised immediately in P&L (after reassessment)",
            "A reduction to retained earnings",
            "Negative goodwill carried as a liability",
            "An error that must always be corrected to zero"
        ], key="ifrs3q3")
        if st.button("Check Answer", key="ifrs3c3"):
            if q3 == "A bargain purchase gain recognised immediately in P&L (after reassessment)":
                st.success("✅ Correct! Negative goodwill = Bargain Purchase Gain. After reassessing all measurements, recognise the gain immediately in P&L.")
            else:
                st.error("❌ Negative result = Bargain Purchase Gain → P&L immediately (after mandatory reassessment of all amounts).")

        st.markdown("---")
        st.markdown("**4. Under the Full Goodwill method, NCI is measured at:**")
        q4 = st.radio("", [
            "NCI's proportionate share of net identifiable assets",
            "Fair value of the NCI",
            "Historical cost",
            "Zero"
        ], key="ifrs3q4")
        if st.button("Check Answer", key="ifrs3c4"):
            if q4 == "Fair value of the NCI":
                st.success("✅ Correct! Full Goodwill method measures NCI at FAIR VALUE, which means goodwill includes the NCI's share of goodwill too. Partial method uses proportionate share of net assets instead.")
            else:
                st.error("❌ Full Goodwill method → NCI at FAIR VALUE (includes NCI's share of goodwill).")

        st.markdown("---")
        st.markdown("**5. Goodwill recognised in a business combination is subsequently:**")
        q5 = st.radio("", [
            "Amortised over its useful life",
            "Amortised over a maximum of 20 years",
            "Not amortised, but tested for impairment at least annually",
            "Written off immediately to P&L"
        ], key="ifrs3q5")
        if st.button("Check Answer", key="ifrs3c5"):
            if q5 == "Not amortised, but tested for impairment at least annually":
                st.success("✅ Correct! Goodwill is NEVER amortised under IFRS. It is tested for impairment at least annually (and whenever indicators exist) under IAS 36.")
            else:
                st.error("❌ Goodwill is NOT amortised — tested for impairment ANNUALLY under IAS 36.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. The Acquisition Method — 4 Steps
        1. Identify the acquirer
        2. Determine acquisition date (date control obtained)
        3. Measure identifiable assets/liabilities/NCI at fair value
        4. Recognise goodwill or bargain purchase gain

        ### 2. Goodwill Formula
        ```
        Goodwill = Consideration Transferred
                 + FV of NCI (or NCI's proportionate share)
                 + FV of Previously Held Interest (step acquisitions)
                 − FV of Net Identifiable Assets Acquired
        ```

        ### 3. NCI Measurement Choice (per transaction)
        | Method | NCI at | Goodwill Includes NCI Share? |
        |---|---|---|
        | Full Goodwill | Fair value | Yes |
        | Partial Goodwill | Proportionate share of net assets | No |

        ### 4. Key Rules
        - Acquisition costs → **EXPENSED** (not capitalised)
        - Negative goodwill → **Bargain Purchase Gain** → P&L (after reassessment)
        - Goodwill → **NOT amortised**, tested for impairment **annually**
        - Step acquisition → remeasure existing stake to FV → gain/loss to **P&L**
        - Measurement period: up to **12 months** to finalise provisional figures
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Goodwill = Consideration + NCI (FV or proportionate) + Prior stake FV − FV Net Assets
Acquisition costs → EXPENSE (never capitalise)
Negative result → Bargain Purchase Gain → P&L
Goodwill → NEVER amortised, test ANNUALLY for impairment
Measurement period → max 12 months from acquisition date
        """)

        st.success("🎓 **IFRS 3 Complete!** You can now apply the acquisition method, calculate goodwill under both NCI methods, and account for bargain purchases and step acquisitions.")
        st.info("💡 **Next**: IFRS 5 — Non-current Assets Held for Sale and Discontinued Operations")

if __name__ == "__main__":
    show()