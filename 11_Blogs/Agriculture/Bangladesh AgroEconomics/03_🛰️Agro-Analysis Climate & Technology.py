import streamlit as st
import pandas as pd
import numpy as np

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🛰️ Agro-Analysis: Climate & Technology</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>Bridging Environmental Resilience with Digital Innovation</p>", unsafe_allow_html=True)
st.write("---")

# --- Layout: Two Columns for Content ---
col_left, col_right = st.columns([1.2, 0.8])

with col_left:
    st.subheader("1. The Climate Challenge")
    st.write("""
    Bangladesh remains one of the most climate-vulnerable nations. For agriculture, this 
    translates to **salinity intrusion** in the south and **erratic rainfall** in the north. 
    Analytical modeling is now used to predict yield loss and optimize planting windows.
    """)
    
    st.markdown("""
    **Core Resilience Strategies:**
    * **Salinity-Tolerant Seeds:** Analyzing the adoption rate of BINA-8 and BINA-10 rice varieties.
    * **Submergence Modeling:** Using satellite data to map flood-prone areas for deep-water rice.
    * **Heat Stress Analysis:** Correlating rising temperatures with pollination failure in winter crops.
    """)

with col_right:
    # A decorative/informative block for Tech Stack
    st.info("**Tech Stack for Agro-Analysis**")
    st.code("""
# Modern Stack:
- Python (Pandas/XGBoost)
- Remote Sensing (Sentinel-2)
- IoT (Soil Moisture Sensors)
- Streamlit (Reporting)
    """, language="python")

st.write("---")

# --- Interactive Segment: Climate Impact Simulator ---
st.subheader("2. 🧮 Climate Risk Simulator (Mock Model)")
st.write("Adjust the parameters to see the projected impact on crop yield based on historical climate correlations.")

c1, c2, c3 = st.columns(3)
with c1:
    temp_rise = st.slider("Temperature Rise (°C)", 0.0, 4.0, 1.5)
with c2:
    salinity = st.select_slider("Salinity Level", options=["Low", "Medium", "High", "Critical"])
with c3:
    tech_adop = st.checkbox("Enable Precision Tech Adop.", value=True)

# Simple Mock Logic for Calculation
base_yield = 100
impact = (temp_rise * 5) + ({"Low": 0, "Medium": 10, "High": 20, "Critical": 40}[salinity])
if tech_adop:
    impact = impact * 0.5  # Technology mitigates 50% of the risk

final_yield = max(0, base_yield - impact)

# Display Result
st.metric(label="Projected Yield Resilience", value=f"{final_yield}%", delta=f"{-impact}% Risk")

st.write("---")

# --- Technology Integration Section ---
st.subheader("3. The 'Smart Farm' Framework")

tab_iot, tab_ai, tab_drones = st.tabs(["🌐 IoT Integration", "🤖 AI & Machine Learning", "🛸 Remote Sensing"])

with tab_iot:
    st.write("""
    Real-time monitoring of soil pH, nitrogen, and moisture levels. 
    By automating irrigation, factories and farms can reduce water wastage by **35%**.
    """)
    st.image("https://img.icons8.com/clouds/100/000000/microchip.png", width=80)

with tab_ai:
    st.write("""
    Using Python-based libraries like **Scikit-learn** and **XGBoost** to forecast harvest 
    dates. Predictive analytics help in managing supply chain logistics for large entities 
    like Unilever.
    """)
    st.markdown("`Status: Prototype Development in Progress`")

with tab_drones:
    st.write("""
    Satellite imagery (NDVI) is used to detect pest infestations 10 days before they 
    become visible to the naked eye. This allows for localized pesticide application, 
    lowering chemical costs.
    """)

# --- Footer ---
st.write("###")
st.markdown("""
<div style="background-color: #f8fafc; padding: 15px; border-radius: 5px; border: 1px solid #e2e8f0;">
    <strong>Analyst's Note:</strong> The integration of technology in Bangladesh agriculture 
    is moving from 'experimental' to 'operational'. The focus for 2026 is on <strong>Scaling 
    Affordable Innovation</strong> for smallholder farmers.
</div>
""", unsafe_allow_html=True)