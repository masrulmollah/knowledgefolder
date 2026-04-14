import streamlit as st

# 1. Title & Meta
st.markdown("# 🌍 Impact of US-Iran Conflict on Bangladesh (2026)")
st.caption("Economic Analyst Report | Masrul Mollah, FCA | April 2026")

# 2. Visual Header
st.image("https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=1000", 
         caption="The Strait of Hormuz: A Global Energy Chokepoint")

# 3. Core Analysis
st.markdown("""
### Executive Summary
As of April 2026, the escalation between the US and Iran has created a 'Stagflationary' risk for Bangladesh. 
With Brent crude crossing **$110/barrel**, the domestic economy faces a dual crisis of rising costs and falling inflows.

#### 🚨 Critical Impact Areas:
1. **Energy Inflation:** Every \$10 rise in oil prices increases Bangladesh's import bill by approximately **\$75M per month**.
2. **Remittance Crisis:** 80% of our migrants are in the Middle East. Over **900 flights** were cancelled in March 2026 alone, disrupting the flow of the \$32B remittance lifeline.
3. **Fertilizer Shortage:** 30% of global urea passes through the Strait of Hormuz. LNG price spikes have already hit local urea production.
""")

# 4. Data Visualization
st.markdown("#### 📊 GDP Growth Scenarios for Bangladesh")
chart_data = {
    "Scenario": ["Pre-War (Actual)", "Localized Tension", "Full-Scale Conflict"],
    "GDP Growth %": [6.8, 5.5, 4.1]
}
st.bar_chart(data=chart_data, x="Scenario", y="GDP Growth %", color="#001A70")

# 5. Strategic Conclusion
st.success("""
**Strategic Recommendation:** Bangladesh must fast-track its strategic fuel reserves and diversify RMG exports toward 
the ASEAN region to offset the European and Middle Eastern market volatility.
""")