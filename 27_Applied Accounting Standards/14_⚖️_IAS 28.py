import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show():
    st.title("🤝 IAS 28: Investments in Associates and Joint Ventures")
    st.markdown("*Master the equity method of accounting for associates and joint ventures*")
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["📖 Learn","🧮 Examples","💡 Interactive Tools","📊 Visualizations","✅ Quiz","📝 Summary"])

    with tab1:
        st.header("Core Concepts")
        st.subheader("1. Definitions")
        st.markdown("""
| Term | Definition | Ownership Threshold |
|---|---|---|
| **Associate** | Entity over which the investor has significant influence | Typically 20–50% |
| **Joint Venture** | Arrangement where parties have joint control and rights to net assets | Contractually determined |
| **Significant Influence** | Power to participate in financial and operating policy decisions — NOT control | 20–50% |
        """)
        st.subheader("2. Significant Influence — Evidence")
        st.markdown("""
Even without 20% ownership, significant influence may exist through:
- Representation on the board of directors
- Participation in policy-making processes
- Material intercompany transactions
- Interchange of managerial personnel
- Provision of essential technical information

If >20% owned, significant influence is **presumed** (rebuttable).
If <20% owned, significant influence must be **demonstrated**.
        """)
        st.subheader("3. The Equity Method")
        st.markdown("""
**Equity method:** Investor recognises its **share of the associate's profit/loss** in its own P&L, and adjusts the carrying amount of the investment accordingly.

**Initial recognition:**
- Recognise at **cost** (including transaction costs)
- Identify any **fair value adjustments** (excess of FV of net assets over carrying amount)
- Calculate **goodwill** on acquisition (not separately recognised — included in carrying amount)

**Subsequent measurement:**
```
Carrying Amount = Cost + Share of Post-Acquisition Profit/Loss
                        + Share of OCI
                        − Dividends received
                        − Impairment losses
```

**P&L:** Share of associate's profit → single line item in P&L ("Share of profit of associates")
**OCI:** Share of associate's OCI items → investor's OCI
        """)
        st.subheader("4. Impairment of Investment in Associate")
        st.markdown("""
- Apply IAS 36 to assess if the investment in an associate is impaired
- Recoverable amount = higher of Value in Use and Fair Value less Costs to Sell
- Impairment loss → P&L; may be reversed in future periods
        """)
        st.subheader("5. Exemptions from Equity Method")
        st.markdown("""
An entity need NOT use the equity method if:
- The investment is classified as held for sale (IFRS 5)
- The investor is a venture capital organisation, mutual fund, unit trust or similar and ELECTS to measure at fair value through P&L (IFRS 9)

Parent exempt from preparing consolidated statements under IAS 27 → still uses equity method in separate statements if required.
        """)

    with tab2:
        st.header("Practical Examples")
        st.subheader("Example 1: Initial Recognition of Associate")
        st.markdown("""
Entity acquires 30% of ABC Co for **$3,000,000**.
ABC's identifiable net assets at FV = **$8,000,000**.
Entity's share = 30% × $8,000,000 = **$2,400,000**.
Goodwill (included in investment) = $3,000,000 − $2,400,000 = **$600,000**

**Journal:**
```
Dr  Investment in Associate   $3,000,000
    Cr  Cash                      $3,000,000
```
        """)
        st.subheader("Example 2: Equity Method — Year 1")
        st.markdown("""
| Item | ABC Co (100%) | Investor's 30% Share |
|---|---|---|
| Profit for the year | $1,000,000 | $300,000 |
| OCI (revaluation) | $200,000 | $60,000 |
| Dividends paid | $400,000 | $120,000 |

**Investor's Investment Carrying Amount (end of year 1):**

| | $000 |
|---|---|
| Opening carrying amount | 3,000 |
| + Share of profit (P&L) | 300 |
| + Share of OCI | 60 |
| − Dividends received | (120) |
| **Closing carrying amount** | **3,240** |

**Investor's journal entries:**
```
Dr  Investment in Associate   $300,000
    Cr  Share of Profit of Associate (P&L)   $300,000

Dr  Investment in Associate   $60,000
    Cr  OCI (Revaluation Reserve)             $60,000

Dr  Cash                      $120,000
    Cr  Investment in Associate               $120,000
```
        """)
        st.subheader("Example 3: Losses Exceeding Carrying Amount")
        st.markdown("""
If the investor's share of losses exceeds the carrying amount of the investment, the investor **stops recognising losses** once the carrying amount reaches zero.

Additional losses are only recognised if the investor has incurred obligations or made payments on behalf of the associate.
        """)

    with tab3:
        st.header("Interactive Tools")
        st.subheader("🔧 Equity Method Calculator")
        col1, col2 = st.columns(2)
        with col1:
            cost = st.number_input("Initial cost of investment ($)", value=3000000)
            ownership = st.number_input("Ownership stake (%)", value=30.0) / 100
            assoc_profit = st.number_input("Associate's profit for year ($)", value=1000000)
            assoc_oci = st.number_input("Associate's OCI for year ($)", value=200000)
            dividends = st.number_input("Dividends declared by associate ($)", value=400000)
        with col2:
            share_profit = assoc_profit * ownership
            share_oci = assoc_oci * ownership
            divs_received = dividends * ownership
            closing_ca = cost + share_profit + share_oci - divs_received
            st.markdown(f"""
| Item | $|
|---|---|
| Opening investment | {cost:,.0f} |
| + Share of profit ({ownership*100:.0f}%) | {share_profit:,.0f} |
| + Share of OCI | {share_oci:,.0f} |
| − Dividends received | ({divs_received:,.0f}) |
| **Closing carrying amount** | **{closing_ca:,.0f}** |

**P&L: Share of profit = ${share_profit:,.0f}**
**OCI: Share of OCI = ${share_oci:,.0f}**
""")

    with tab4:
        st.header("Visualizations")
        years = ["Year 0","Year 1","Year 2","Year 3","Year 4","Year 5"]
        profits = [0,300,350,280,400,450]
        carrying = [3000]
        for p in profits[1:]:
            carrying.append(carrying[-1] + p - 120)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=years, y=profits, name="Share of Profit", marker_color="#10B981"))
        fig.add_trace(go.Scatter(x=years, y=carrying, name="Investment Carrying Amount", line=dict(color="#2563EB", width=2), mode="lines+markers", yaxis="y2"))
        fig.update_layout(title="Equity Method — Share of Profit and Investment Value ($000)", barmode="group",
                          yaxis=dict(title="Share of Profit ($000)"), yaxis2=dict(title="Carrying Amount ($000)", overlaying="y", side="right"), height=400)
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")
        st.markdown("**1. The equity method requires the investor to:**")
        q1 = st.radio("", ["Consolidate the associate line by line","Recognise its share of the associate's profit/loss in P&L","Measure the investment at fair value through P&L","Measure the investment at cost only"], key="ias28q1")
        if st.button("Check", key="c28_1"):
            if q1 == "Recognise its share of the associate's profit/loss in P&L":
                st.success("✅ Correct! The equity method recognises the investor's share of the associate's profit/loss as a single line in P&L, and adjusts the investment's carrying amount.")
            else:
                st.error("❌ Equity method = share of profit in P&L + adjust carrying amount. NOT line-by-line consolidation.")
        st.markdown("---")
        st.markdown("**2. Dividends received from an associate under the equity method are:**")
        q2 = st.radio("", ["Recognised as income in P&L","Deducted from the carrying amount of the investment","Added to the carrying amount","Treated as return of capital in equity"], key="ias28q2")
        if st.button("Check", key="c28_2"):
            if q2 == "Deducted from the carrying amount of the investment":
                st.success("✅ Correct! Under the equity method, dividends received reduce the carrying amount of the investment (they represent a return of the investment, not income).")
            else:
                st.error("❌ Dividends from associates REDUCE the carrying amount — they are not P&L income (the profit was already recognised via equity method).")
        st.markdown("---")
        st.markdown("**3. Significant influence is PRESUMED when ownership is:**")
        q3 = st.radio("", ["More than 50%","Between 20% and 50%","Exactly 25%","More than 10%"], key="ias28q3")
        if st.button("Check", key="c28_3"):
            if q3 == "Between 20% and 50%":
                st.success("✅ Correct! IAS 28 presumes significant influence when ownership is between 20% and 50%. This presumption is rebuttable.")
            else:
                st.error("❌ Significant influence is presumed at 20–50% ownership.")
        st.markdown("---")
        st.markdown("**4. If the investor's share of losses of an associate exceeds the carrying amount:**")
        q4 = st.radio("", ["Recognise full losses regardless","Stop recognising losses; carrying amount becomes zero (with exceptions)","Recognise losses in OCI instead","Classify investment as held for sale"], key="ias28q4")
        if st.button("Check", key="c28_4"):
            if q4 == "Stop recognising losses; carrying amount becomes zero (with exceptions)":
                st.success("✅ Correct! Recognition stops when the carrying amount reaches zero. Additional losses are recognised only if the investor has legal/constructive obligations.")
            else:
                st.error("❌ Once carrying amount = 0, stop recognising losses unless investor has obligations or makes payments on behalf of the associate.")
        st.markdown("---")
        st.markdown("**5. The associate's OCI items are recognised in the investor's:**")
        q5 = st.radio("", ["P&L only","Not recognised at all","OCI — as the investor's share","Retained earnings directly"], key="ias28q5")
        if st.button("Check", key="c28_5"):
            if q5 == "OCI — as the investor's share":
                st.success("✅ Correct! The investor recognises its proportionate share of the associate's OCI in its own OCI, with corresponding adjustment to the carrying amount of the investment.")
            else:
                st.error("❌ Share of associate's OCI goes through the investor's OCI, not P&L.")

    with tab6:
        st.header("Summary")
        st.markdown("""
### IAS 28 Key Rules

**Scope:** Associates (significant influence: typically 20–50%) and Joint Ventures

**Method:** EQUITY METHOD (mandatory unless exemption applies)

**Carrying Amount Movement:**
```
Opening + Share of Profit/Loss (→ P&L)
       + Share of OCI (→ investor's OCI)
       − Dividends received
       − Impairment
= Closing Carrying Amount
```

**Goodwill** = included in carrying amount (not separately recognised)

**Losses exceeding carrying amount:** Stop at zero (exceptions: legal obligations, payments made on behalf)

**Impairment:** Apply IAS 36; may reverse

**Exemptions:** Held for sale (IFRS 5) | Venture capital entities (IFRS 9 FV option)
        """)
        st.success("🎓 IAS 28 Complete!")
        st.info("💡 Next: IAS 32 — Financial Instruments: Presentation")

if __name__ == "__main__":
    show()