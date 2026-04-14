import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Custom Styling ---
st.markdown("""
    <style>
    .stat-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #e1e4e8;
        text-align: center;
    }
    .stat-val {
        font-size: 28px;
        font-weight: bold;
        color: #047857;
    }
    .stat-label {
        font-size: 14px;
        color: #6b7280;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #065f46;'>📊 Agro-Statistics: Data & Trends</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280;'>Statistical Analysis of Bangladesh Agricultural Landscape (2025-2026)</p>", unsafe_allow_html=True)
st.write("---")

# --- KPI Dashboard Row ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="stat-card"><p class="stat-label">Agri GDP Share</p><p class="stat-val">9.8%</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><p class="stat-label">Agri Workforce</p><p class="stat-val">38.2%</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><p class="stat-label">Food Inflation</p><p class="stat-val">8.5%</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-card"><p class="stat-label">Export Growth</p><p class="stat-val">+12%</p></div>', unsafe_allow_html=True)

st.write("###")

# --- Main Statistical Sections ---
tab1, tab2 = st.tabs(["📈 Production Trends", "⚖️ Economic Indicators"])

with tab1:
    st.subheader("Crop Production Volatility Analysis")
    st.info("Historical data vs. 2026 Forecasts based on recent climate-resilient seed adoption.")
    
    # Mock Statistical Data for Visualization
    crop_data = pd.DataFrame({
        'Year': [2021, 2022, 2023, 2024, 2025, 2026],
        'Rice (MT)': [38.5, 39.1, 40.2, 39.8, 41.5, 42.1],
        'Wheat (MT)': [1.1, 1.0, 1.2, 1.4, 1.6, 1.8],
        'Maize (MT)': [5.4, 5.6, 6.1, 6.5, 7.0, 7.4]
    })
    
    # Plotly Chart
    fig = px.line(crop_data, x='Year', y=['Rice (MT)', 'Wheat (MT)', 'Maize (MT)'], 
                  title="Major Crop Production Trends (Million Metric Tons)",
                  markers=True, color_discrete_sequence=px.colors.qualitative.Safe)
    fig.update_layout(hovermode="x unified", plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("View Statistical Observations"):
        st.write("""
        * **Rice Stability:** Despite flood events in late 2025, production remains stable due to Boro-season efficiency.
        * **Maize Growth:** Seeing a **CAGR of ~7%**, driven by the rising demand from the poultry and aqua-feed industries.
        * **Wheat Deficit:** Production is rising but still meets only 25% of domestic consumption.
        """)

with tab2:
    st.subheader("Price Indices & Workforce Distribution")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        # Pie Chart for Workforce
        labor_data = pd.DataFrame({
            'Category': ['Agriculture', 'Manufacturing', 'Services', 'Others'],
            'Percentage': [38.2, 21.5, 36.3, 4.0]
        })
        fig_pie = px.pie(labor_data, values='Percentage', names='Category', 
                         title="Labor Force Distribution (2026)",
                         hole=0.4, color_discrete_sequence=px.colors.sequential.Greens_r)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_b:
        # Input Cost Analysis
        cost_index = pd.DataFrame({
            'Input': ['Urea Fertilizer', 'Diesel/Fuel', 'Seedling', 'Labor Cost'],
            'Index Change (%)': [46, 18, 12, 25]
        })
        fig_bar = px.bar(cost_index, x='Input', y='Index Change (%)', 
                         title="Agricultural Input Cost Increase (YoY)",
                         color='Index Change (%)', color_continuous_scale='Reds')
        st.plotly_chart(fig_bar, use_container_width=True)

# --- Analysis Sidebar Logic (Internal to the Page) ---
st.sidebar.markdown("---")
st.sidebar.subheader("Data Controls")
data_filter = st.sidebar.multiselect("Select Crops to Analyze", ['Rice', 'Wheat', 'Maize', 'Potato'], default=['Rice', 'Maize'])

# --- Footer ---
st.write("---")
st.caption("Statistical Source: BBS (Bangladesh Bureau of Statistics) & Ministry of Agriculture Forecasts 2026.")