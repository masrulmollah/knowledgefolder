import streamlit as st
import pandas as pd
import plotly.express as px

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #92400e;'>🍗 Poultry & Cattle: The Protein Price Index</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #78350f; text-align: center;'>Analyzing Supply Chain Volatility and Commercialization in 2026</p>", unsafe_allow_html=True)
st.write("---")

# --- Top Level Metrics (2026 Snapshots) ---
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Annual Egg Production", "23.37 Billion", "+15% YoY")
with m2:
    st.metric("Poultry Meat Output", "1.46M Tons", "Steady")
with m3:
    st.metric("Feed Market CAGR", "2.57%", "2026-2034")

st.write("###")

# --- Section 1: The Feed-Price Correlation ---
st.subheader("1. Feed Economics: The Primary Driver")
st.write("""
In 2026, **feed costs represent nearly 70% of total production expenses**. With the Bangladesh 
animal feed market projected to hit **$2.86 Billion by 2034**, the focus has shifted toward 
optimizing 'Feed Conversion Ratios' (FCR).
""")

# Data for Feed vs Meat Price Trends
trend_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Soyameal Index': [100, 112, 118, 125, 122, 130],
    'Broiler Retail Price': [100, 105, 110, 118, 115, 122]
})

fig_price = px.line(trend_data, x='Month', y=['Soyameal Index', 'Broiler Retail Price'],
                    title="Correlation: Feed Input vs. Retail Poultry Price (2026)",
                    markers=True, color_discrete_sequence=['#b45309', '#f59e0b'])
st.plotly_chart(fig_price, use_container_width=True)

# --- Section 2: Cattle & Beef Outlook ---
st.write("---")
st.subheader("2. Cattle & Beef: Quality over Quantity")
col_a, col_b = st.columns([1, 1])

with col_a:
    st.write("""
    While beef consumption shows a slight 0.4% decline due to high retail prices, 
    **production is growing at 0.2% annually**. 
    
    The industry is moving toward **scientifically formulated pellet feeds** (now 40% of the market) 
    to improve weight gain in indigenous breeds.
    """)
    st.markdown("""
    **Emerging Trends:**
    * **Peri-urban Dairy Hubs:** Rapid expansion around Dhaka and Chattogram.
    * **Electricity Rebates:** The 20% bill rebate for farms is improving bottom-line margins.
    * **Waste Recycling:** Using agro-byproducts for sustainable feed formulations.
    """)

with col_b:
    # Distribution of Feed Market by Animal Type (2025/26 data)
    feed_dist = pd.DataFrame({
        'Category': ['Poultry', 'Cattle/Livestock', 'Aquaculture', 'Others'],
        'Market Share (%)': [38, 32, 25, 5]
    })
    fig_pie = px.pie(feed_dist, values='Market Share (%)', names='Category', 
                     hole=0.4, title="Feed Demand by Sector",
                     color_discrete_sequence=px.colors.sequential.YlOrBr_r)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- Section 3: Strategic Challenges & Potential ---
st.write("---")
st.subheader("3. Strategic Frontiers")

with st.expander("🚀 Export Ambitions & The $2.4B Gap"):
    st.write("""
    Bangladesh's poultry industry has attracted **Tk 400 Billion in investment**. However, 
    the lack of **internationally recognized certification** and **cold chain logistics** results in nearly **$2.4 Billion in annual losses**. 
    
    Bridging this gap would allow Bangladesh to compete with global leaders like Brazil and Thailand 
    in the Middle Eastern Halal meat market.
    """)

# --- Simulation Tool ---
st.sidebar.header("Profitability Simulator")
feed_cost_change = st.sidebar.slider("Feed Cost Flux (%)", -20, 20, 0)
retail_price_change = st.sidebar.slider("Retail Price Flux (%)", -20, 20, 0)

# Mock Calculation
base_margin = 15 # BDT per bird
simulated_margin = base_margin + (retail_price_change * 0.5) - (feed_cost_change * 0.7)

st.sidebar.markdown(f"### Simulated Margin: **{simulated_margin:.2f} BDT/Bird**")
if simulated_margin < 5:
    st.sidebar.error("Warning: High Risk of Net Loss")
elif simulated_margin > 20:
    st.sidebar.success("Optimal Profitability Zone")

# --- Footer ---
st.write("###")
st.caption("Data Sources: Bangladesh Bureau of Statistics (BBS), IMARC Group Feed Market Report, & BPICC 2026 Forecasts.")