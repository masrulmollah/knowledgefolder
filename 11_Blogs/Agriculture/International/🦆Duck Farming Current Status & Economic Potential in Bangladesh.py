import streamlit as st
import pandas as pd

# 1. Title & Meta
st.markdown("# 🦆 Duck Farming: Current Status & Potential in Bangladesh")
st.caption("Livestock Sector Analysis | Agribusiness Development | April 2026")

# 2. Stable Featured Image (Wikimedia Commons)
# This source is highly reliable for web embedding.
st.image("https://upload.wikimedia.org/wikipedia/commons/a/a1/Duck_rearing_in_Bangladesh.jpg", 
         caption="Integrated duck farming in the wetlands of Bangladesh.",
         use_container_width=True)

# 3. Executive Summary
st.markdown("""
### Executive Summary
Duck farming is a critical livestock sub-sector in Bangladesh, especially in the wetland (*Haor*) regions. 
It provides a steady source of protein and income for over **1.2 million households**.
""")

# 4. Market Data Visualization
st.markdown("#### 📈 Projected Market Growth")
data = pd.DataFrame({
    "Year": ["2023", "2024", "2025", "2026 (F)"],
    "Egg Production (Billions)": [4.2, 4.8, 5.5, 6.2]
})
st.line_chart(data=data, x="Year", y="Egg Production (Billions)", color="#FF4B4B")

# 5. Potential & Recommendations
st.success("""
**Strategic Potential:**
* **Integrated Farming:** High potential for 'Duck-cum-Fish' models.
* **Low Input Cost:** Ducks scavenge for natural feed in vast water bodies.
* **Resilience:** Highly resistant to many common avian diseases.
""")

# 6. Conclusion
st.info("Conclusion: Structured investment in hatcheries and cold chains can turn this into a major export pillar.")