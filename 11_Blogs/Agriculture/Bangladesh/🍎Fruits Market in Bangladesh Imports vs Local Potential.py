import streamlit as st
import pandas as pd

# 1. Title & Meta
st.markdown("# 🍎 Fruits Market in Bangladesh: Imports vs. Local Potential")
st.caption("Trade & Agribusiness Analysis | Strategic Insights Apr 2026 | By Masrul Mollah")

# Featured Image
st.image("https://images.unsplash.com/photo-1619566636858-adf3ef46400b?q=80&w=1000", 
         caption="Bangladesh is transitioning from 56 to 72 varieties of locally produced fruits.",
         use_container_width=True)

# 2. Executive Summary
st.markdown("""
### Executive Summary
The fruit industry in Bangladesh is undergoing a historic shift. While the country remains a significant importer of 
temperate fruits (Apples, Grapes, Oranges), the local production of exotic varieties like Dragon Fruit and Avocado is 
surging. Most notably, fruit export earnings have skyrocketed from **$0.58M in 2022** to over **$67M in 2025**, 
marking a 116x growth in three years.
""")

# 3. Import Landscape (Statistical Overview)
st.markdown("### 🚢 The Import Reality")
col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Major Imports (FY26 Estimates)**
    * **Apples:** ~280,000 Tons (China, India, Brazil)
    * **Oranges/Malta:** ~190,000 Tons (Egypt, S. Africa, India)
    * **Dates:** ~90,000 Tons (Saudi Arabia, UAE, Tunisia)
    * **Grapes:** ~65,000 Tons (India, China)
    """)

with col2:
    st.warning("""
    **The Cost of Import**
    * Total Import Duties currently exceed **116%** for most fruits.
    * Importers pay roughly **Tk 120–136** in taxes for every **Tk 100** worth of fruit.
    * High dependency on the Chattogram port for 90% of supply.
    """)

st.divider()

# 4. Local Production & Potential
st.markdown("#### 📈 The Export Revolution (USD Millions)")

# Real-world data based on EPB reports
export_data = pd.DataFrame({
    "Fiscal Year": ["2021-22", "2022-23", "2023-24", "2024-25"],
    "Earnings ($M)": [0.58, 15.2, 38.4, 67.5]
})

st.bar_chart(data=export_data, x="Fiscal Year", y="Earnings ($M)", color="#FF8C00")
st.caption("Data Source: Analysis of EPB and DAE Statistics (2026).")

# 5. Strategic Analysis & Recommendations
st.markdown("### 💡 Business Insights")

tab1, tab2 = st.tabs(["For New Entrepreneurs", "For Existing Businesses"])

with tab1:
    st.markdown("""
    **Where to start?**
    * **Exotic Farming:** Focus on Dragon Fruit, Rambutan, and Saudi Dates. These have high margins and low import substitution competition.
    * **Direct Sourcing:** Skip the wholesale 'Arats' by building direct supply lines from districts like Rajshahi (Mango) and Bandarban (Pineapple).
    * **E-commerce:** Quality-assured, chemical-free fruit delivery is a booming niche in Dhaka and Chattogram.
    """)

with tab2:
    st.markdown("""
    **How to scale?**
    * **Cold Chain Investment:** Current post-harvest loss is **25-35%** (worth ~$430M annually). Building specialized cold storage for fruits (not just potatoes) is a massive gap.
    * **Compliance for Export:** Focus on **GAP (Good Agricultural Practices)** and ISO certification to enter EU and Gulf supermarket chains.
    * **Value Addition:** Invest in pulp processing and dry-fruit technologies to manage seasonal gluts of Jackfruit and Mango.
    """)

# 6. Recommendation Summary
st.success("""
**Final Verdict:** The market is moving from 'Quantity' to 'Quality & Compliance'. Entrepreneurs who invest in 
**Traceability** and **Cold-Chain Logistics** will lead the next decade of Bangladesh's Agribusiness.
""")