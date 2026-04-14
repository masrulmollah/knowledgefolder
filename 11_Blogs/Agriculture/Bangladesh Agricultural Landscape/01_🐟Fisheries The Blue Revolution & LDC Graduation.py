import streamlit as st
import pandas as pd
import plotly.express as px

# --- Header Section ---
st.markdown("<h1 style='text-align: center; color: #0077b6;'>🐟 Fisheries: The Blue Revolution & LDC Graduation</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>Analyzing the Impact of Trade Policy on Bangladesh's Aquaculture</p>", unsafe_allow_html=True)
st.write("---")

# --- Sector Insights ---
col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.subheader("The State of the Sector (2026)")
    st.write("""
    Bangladesh is currently the **3rd largest inland fish producer** in the world. However, as we 
    approach LDC graduation, the sector faces a structural pivot. The reliance on inland 
    culture is high, but the future growth lies in the 'Blue Economy'—our vast maritime territory.
    """)
    
    st.markdown("""
    **Core Challenges for 2026:**
    * **LDC Graduation:** Expected withdrawal of export cash incentives (currently 10-15%).
    * **EU Green Deal:** Stricter Traceability and Sanitary/Phytosanitary (SPS) requirements.
    * **Energy Costs:** Rising fuel prices impacting deep-sea trawler ROI.
    """)

with col2:
    st.info("**Key Metric: Export Contribution**")
    # Mock data for export trends
    export_data = pd.DataFrame({
        'Year': ['2023', '2024', '2025', '2026 (F)'],
        'Revenue ($M)': [420, 455, 490, 515]
    })
    st.line_chart(export_data.set_index('Year'))

st.write("---")

# --- Strategic Analysis: The LDC Graduation Impact ---
st.subheader("⚖️ Post-LDC Graduation Analysis")
st.write("""
LDC graduation will remove the 'Least Developed Country' trade preferences. For the fisheries 
sector, this means we must compete on **efficiency and quality** rather than price subsidies.
""")

tab1, tab2 = st.tabs(["📊 Market Mix", "🛠️ Mitigation Strategy"])

with tab1:
    st.write("Currently, inland aquaculture dominates our production. To sustain growth, a mix-shift is required.")
    mix_data = pd.DataFrame({
        'Source': ['Inland Culture', 'Inland Capture', 'Marine'],
        'Production (MT)': [2.7, 1.3, 0.7]
    })
    fig = px.pie(mix_data, values='Production (MT)', names='Source', 
                 title="Production Source Distribution",
                 color_discrete_sequence=['#0077b6', '#00b4d8', '#90e0ef'])
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("""
    **To remain competitive post-2026, the sector must adopt:**
    1.  **Blockchain Traceability:** Providing EU/US buyers with 'Farm-to-Fork' data.
    2.  **Solar-Powered Aeration:** Reducing the cost of production by 15-20%.
    3.  **Value Addition:** Shifting from raw frozen shrimp to 'Ready-to-Cook' processed products.
    """)

# --- Potential: The Blue Economy ---
st.write("---")
st.subheader("🌊 Future Potential: The Blue Economy")
st.success("""
The Bay of Bengal offers a massive frontier for **Seaweed Farming** and **Cage Culture**. 
In 2026, initial pilots in Cox's Bazar show a Benefit-Cost Ratio (BCR) of 2.1, making it a 
highly attractive investment for agro-conglomerates.
""")

# --- Interactive Margin Calculator ---
with st.expander("🧮 Quick Margin Impact Tool"):
    st.write("Simulate how the removal of export incentives affects profit margins.")
    revenue = st.number_input("Average Export Price (USD/kg)", value=12.0)
    cost = st.number_input("Production & Logistics Cost (USD/kg)", value=8.5)
    incentive = st.slider("Current Export Incentive (%)", 0, 15, 10)
    
    current_profit = (revenue - cost) + (revenue * (incentive/100))
    future_profit = (revenue - cost) # 0% incentive
    
    st.metric(label="Current Profit per kg", value=f"${current_profit:.2f}")
    st.metric(label="Post-LDC Profit per kg", value=f"${future_profit:.2f}", 
              delta=f"-{(current_profit - future_profit):.2f} (Incentive Loss)", delta_color="inverse")

# --- Footer ---
st.write("###")
st.caption("Content Source: Department of Fisheries (DoF) & Export Promotion Bureau (EPB) Analysis for 2026.")