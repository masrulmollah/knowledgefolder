import streamlit as st
import pandas as pd

# 1. Title & Branding
st.markdown("# 🌾 The Green Gold: Bangladesh's Agricultural Export Potential")
st.caption("Sector Analysis | Agribusiness & Trade | April 2026")

# Featured Image - Updated with a more reliable direct link
st.image("https://images.pexels.com/photos/2132180/pexels-photo-2132180.jpeg", 
         caption="Fresh produce ready for international markets.",
         use_container_width=True)

# 2. Executive Summary
st.markdown("""
### Executive Summary
As Bangladesh transitions toward a middle-income economy, the agricultural sector is shifting from 'subsistence farming' 
to 'commercial export.' In 2025-26, the sector has shown a **14% CAGR** in export earnings, specifically in processed 
foods, vegetables, and specialized fruits.
""")

# 3. High-Potential Categories
st.markdown("### 🚀 Top 3 High-Growth Categories")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🥭 Fresh Fruits")
    st.write("**Target:** EU & Middle East")
    st.write("Mangoes and Pineapples are leading the surge due to improved GAP (Good Agricultural Practices).")
    
with col2:
    st.subheader("🥬 Vegetables")
    st.write("**Target:** UK & ASEAN")
    st.write("High demand for Pointed Gourd and Potatoes in the diaspora markets.")
    
with col3:
    st.subheader("🍱 Processed Food")
    st.write("**Target:** Global")
    st.write("The largest share of exports, including spices and fruit juices.")

st.divider()

# 4. Export Earnings Data
st.markdown("#### 📈 Annual Export Earnings Trend (USD Millions)")

# Creating the data
earnings_data = pd.DataFrame({
    "Year": ["2022", "2023", "2024", "2025 (P)"],
    "Earnings ($M)": [950, 1020, 1160, 1300]
})

# Displaying the chart
st.line_chart(data=earnings_data, x="Year", y="Earnings ($M)", color="#2E7D32")
st.caption("Trend Analysis: Growth in Agricultural Exports.")

# 5. Bottlenecks & Solutions
with st.expander("🔍 Analysis of Current Challenges"):
    st.markdown("""
    To unlock the full **$2 Billion** potential, we must address:
    1. **Cold Chain Infrastructure:** 25-30% of produce is lost post-harvest.
    2. **Certification:** Scaling up ISO and Halal certifications.
    3. **Air Freight Costs:** High shipping costs compared to regional competitors.
    """)

# 6. Strategic Conclusion
st.success("""
**Conclusion:** With the right investment in **Contract Farming**, Bangladesh can move beyond being a 'Clothing Hub' to becoming a 'Food Basket' for the world.
""")