import streamlit as st
import pandas as pd

# 1. Title & Meta
st.markdown("# 🐄 Cattle Farming in Bangladesh: Economic Frontier")
st.caption("Livestock Sector Analysis | Dairy & Beef Value Chain | April 2026")

# 2. Featured Image (Wikimedia Commons - High Reliability)
st.image("https://github.com/masrulmollah/free-images-link/blob/main/cow%20farming%20in%20bangladesh.jpg", 
         caption="The transition to high-yielding crossbred cattle is transforming the rural economy.",
         use_container_width=True)

# 3. Executive Summary
st.markdown("""
### Executive Summary
Cattle farming is a cornerstone of Bangladesh's agricultural GDP, contributing significantly to the national protein supply and rural employment. 
With the country reaching near self-sufficiency in meat production during recent Eids, the focus has now shifted toward **yield optimization** and **milk processing**. The sector currently manages a population of approximately **25.5 million cattle**.
""")

# 4. Sector Statistics & Insights
st.markdown("### 📊 Market Snapshot")
col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Key Statistics (2025-26)**
    * **Total Population:** ~25.5 Million heads.
    * **Milk Production:** ~15.2 Million Metric Tons.
    * **Meat Production:** ~9.1 Million Metric Tons.
    * **GDP Contribution:** ~1.90% of total National GDP.
    """)

with col2:
    st.success("""
    **Strategic Insights**
    * **Self-Sufficiency:** Bangladesh no longer depends on cattle imports for religious festivals.
    * **Genetic Shift:** 60% of commercial farms have moved to Friesian/Sahiwal crossbreeds.
    * **Digital Integration:** Growth in 'Online Haats' and traceability apps.
    """)

st.divider()

# 5. Production Trend Analysis
st.markdown("#### 📈 Milk and Meat Production Growth (MT Millions)")

# Analysis of DLS (Department of Livestock Services) growth trends
trend_data = pd.DataFrame({
    "Year": ["2022", "2023", "2024", "2025 (P)"],
    "Milk Production": [13.07, 14.11, 14.80, 15.20],
    "Meat Production": [8.44, 8.71, 8.95, 9.10]
})

st.line_chart(data=trend_data, x="Year", y=["Milk Production", "Meat Production"], color=["#001A70", "#FF4B4B"])
st.caption("Data Source: Analysis based on DLS and Yearly Economic Review.")

# 6. Strategic Considerations for Entrepreneurs
st.markdown("### 💡 Business Roadmap & Recommendations")

tab1, tab2, tab3 = st.tabs(["Pre-Entry Checklist", "Challenges", "Future Potential"])

with tab1:
    st.markdown("""
    **Considerations for New Entrants:**
    1. **Breed Selection:** Choose *Holstein Friesian* cross for dairy or *Brahman* cross for beef fattening.
    2. **Feed Management:** Feed costs account for **60-70%** of operational expenses. Investing in silage (maize/napier) is mandatory for profitability.
    3. **Biosecurity:** Proper shed design with ventilation and strict vaccination for FMD (Foot and Mouth Disease).
    4. **Market Access:** Secure a contract with processors (e.g., Milk Vita, Pran, Aarong) or establish a direct-to-consumer niche.
    """)

with tab2:
    st.markdown("""
    **Major Bottlenecks:**
    * **High Feed Cost:** Rising prices of soybean meal and wheat bran.
    * **Cold Chain:** Lack of milk cooling centers at the village level leading to 10-15% spoilage in summer.
    * **Technical Gap:** Limited access to high-quality semen for Artificial Insemination (AI).
    """)

with tab3:
    st.markdown("""
    **The Future (2027-2030):**
    * **Export Potential:** Potential for Halal Meat export to Gulf countries if FMD-free zones are established.
    * **Value Addition:** High demand for cheese, butter, and powdered milk production.
    * **Bio-Gas & Fertilizer:** Large-scale farms can generate additional revenue through organic fertilizers and electricity.
    """)

# 7. Final Recommendation
st.success("""
**Strategic Verdict:** For existing businessmen, the profit lies in **Vertical Integration** (owning the feed mill and the cooling center). 
For new entrepreneurs, **Beef Fattening** offers faster turnover and lower daily management complexity than dairy.
""")