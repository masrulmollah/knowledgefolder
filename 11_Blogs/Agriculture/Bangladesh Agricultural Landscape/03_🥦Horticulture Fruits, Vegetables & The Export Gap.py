import streamlit as st
import pandas as pd
import plotly.express as px

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #15803d;'>🥦 Horticulture: Fruits, Vegetables & The Export Gap</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #166534;'>Analyzing the $1 Billion Potential in Fresh Produce Exports</p>", unsafe_allow_html=True)
st.write("---")

# --- Overview: The Paradox of Plenty ---
st.subheader("The Export Paradox")
st.write("""
Bangladesh is the **3rd largest vegetable producer** and **7th largest mango producer** globally. 
However, our export earnings from this sector remain below **$100 Million**, representing a 
massive untapped fiscal opportunity.
""")

# --- KPI Section ---
c1, c2, c3 = st.columns(3)
with c1:
    st.info("**Post-Harvest Loss**\n\n~33% of total yield")
with c2:
    st.success("**Export Growth**\n\n+12.5% (2025-26)")
with c3:
    st.warning("**Target Potential**\n\n$1.0 Billion by 2030")

st.write("---")

# --- Section 1: Post-Harvest Loss Analysis ---
st.subheader("1. The Logistics Leakage")
st.write("""
The biggest 'Export Gap' isn't production; it's **preservation**. Due to a lack of cold-chain 
infrastructure, nearly a third of our perishables never reach the market.
""")

loss_data = pd.DataFrame({
    'Crop': ['Mango', 'Tomato', 'Leafy Greens', 'Potato', 'Jackfruit'],
    'Loss %': [35, 40, 45, 15, 30]
})
fig_loss = px.bar(loss_data, x='Crop', y='Loss %', 
                 title="Post-Harvest Loss by Crop Type",
                 color='Loss %', color_continuous_scale='Greens')
st.plotly_chart(fig_loss, use_container_width=True)

# --- Section 2: Market Standards (The GAP Barrier) ---
st.write("---")
st.subheader("2. Compliance & The 'GAP' Barrier")
col_text, col_img = st.columns([1.2, 0.8])

with col_text:
    st.write("""
    To enter premium markets like the EU, Middle East, and Japan, Bangladesh must adhere to 
    **Global Good Agricultural Practices (GAP)**. 
    
    **Current Bottlenecks:**
    * **Traceability:** Inability to track a mango back to a specific orchard.
    * **Pesticide Residue:** Lack of accredited labs for MRL (Maximum Residue Limit) testing.
    * **Cold Chain:** Breakage in temperature control during airport transit.
    """)
    st.markdown("`Solution: Digitizing the Supply Chain via Python-based Traceability Apps.`")

with col_img:
    st.write("###")
    st.markdown("""
    <div style="background-color: #f0fdf4; padding: 20px; border-radius: 10px; border-left: 5px solid #16a34a;">
    <strong>Strategic Win:</strong> In 2026, the first 'Vapor Heat Treatment' (VHT) plant in 
    Rajshahi began operation, unlocking the Japanese market for Himsagar mangoes.
    </div>
    """, unsafe_allow_html=True)

# --- Section 3: High-Value Frontier ---
st.write("---")
st.subheader("3. High-Value Export Forecast")

# Forecast Data
forecast_data = pd.DataFrame({
    'Market': ['Middle East', 'European Union', 'UK', 'ASEAN'],
    'Current (2026)': [45, 12, 8, 5],
    'Potential (2030)': [150, 80, 40, 30]
})

fig_forecast = px.bar(forecast_data, x='Market', y=['Current (2026)', 'Potential (2030)'],
                      title="Market Potential (USD Millions)",
                      barmode='group', color_discrete_sequence=['#86efac', '#166534'])
st.plotly_chart(fig_forecast, use_container_width=True)

# --- Interactive Margin Tool ---
st.sidebar.header("Export Logistics Calculator")
air_freight = st.sidebar.number_input("Air Freight (BDT/kg)", value=220)
packaging = st.sidebar.number_input("Packaging/Processing (BDT/kg)", value=45)
farm_gate = st.sidebar.number_input("Farm-gate Price (BDT/kg)", value=60)
export_price = st.sidebar.number_input("FOB Export Price (USD/kg)", value=4.5)

# Logic: Convert USD to BDT (Approx 118)
total_cost = air_freight + packaging + farm_gate
revenue_bdt = export_price * 118
margin = revenue_bdt - total_cost

st.sidebar.divider()
st.sidebar.metric("Net Margin (BDT/kg)", f"{margin:.2f}")

if margin < 50:
    st.sidebar.error("Low Margin: Optimize Logistics")
else:
    st.sidebar.success("High Margin: Export Viable")

# --- Footer ---
st.write("###")
st.caption("Sources: Export Promotion Bureau (EPB), Hortex Foundation, & FAO Production Statistics 2026.")