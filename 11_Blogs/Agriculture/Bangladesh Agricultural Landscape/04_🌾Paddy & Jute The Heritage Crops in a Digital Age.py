import streamlit as st
import pandas as pd
import plotly.express as px

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #365314;'>🌾 Paddy & Jute: Heritage Crops in a Digital Age</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4d7c0f;'>Reinventing Traditional Staples through Data and Sustainability</p>", unsafe_allow_html=True)
st.write("---")

# --- Overview ---
st.write("""
Paddy and Jute are the pillars of Bangladesh's agricultural history. While **Rice** ensures our 
food security, **Jute** (The Golden Fiber) is making a comeback as a global biodegradable 
alternative to plastic. In 2026, the challenge is shifting from 'Yield' to 'Efficiency'.
""")

# --- Section 1: Rice - Food Security vs. Production Cost ---
st.subheader("1. Paddy: The Cost of Food Security")
st.write("""
Despite being the 3rd largest producer, the **Cost of Production** for rice has risen by 18% 
due to labor shortages and fuel price hikes.
""")

col1, col2 = st.columns([1.2, 0.8])

with col1:
    # Production Data
    rice_stats = pd.DataFrame({
        'Season': ['Boro', 'Aman', 'Aus'],
        'Production (MT)': [21.5, 16.2, 3.8],
        'Cost Index': [120, 105, 95] # 100 as base
    })
    fig_rice = px.bar(rice_stats, x='Season', y='Production (MT)', 
                     title="Production by Season (2025-26)",
                     color='Cost Index', color_continuous_scale='YlGn')
    st.plotly_chart(fig_rice, use_container_width=True)

with col2:
    st.markdown("""
    <div style="background-color: #f7fee7; padding: 15px; border-radius: 10px; border-left: 5px solid #4d7c0f;">
    <strong>Strategic Analysis:</strong><br>
    Boro remains the most expensive yet most productive season. The focus for 2026 is 
    reducing water usage via <b>AWD (Alternate Wetting and Drying)</b> technology.
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- Section 2: Jute - The Golden Fiber's Renaissance ---
st.subheader("2. Jute: Beyond Sacks and Strings")
st.write("""
Jute is transitioning from a packaging material to a high-tech industrial input. 
From **Jute-tin** (housing) to **Sonali Bag** (bioplastic), the market potential is expanding.
""")

# BCR Table (Benefit-Cost Ratio)
st.markdown("#### **Profitability Analysis (Financial Year 2025-26)**")
jute_economics = pd.DataFrame({
    'Metric': ['Average Yield (per Hectare)', 'Production Cost (BDT)', 'Net Return (BDT)', 'Benefit-Cost Ratio (BCR)'],
    'Traditional Jute': ['2.1 Tons', '95,000', '42,000', '1.44'],
    'Certified High-Yield': ['2.8 Tons', '105,000', '67,500', '1.64']
})
st.table(jute_economics)

# --- Section 3: Digital Transformation & Automation ---
st.write("---")
st.subheader("3. Bridging the Labor Gap")

tab_rice, tab_jute = st.tabs(["🤖 Paddy Automation", "🧬 Jute Research"])

with tab_rice:
    st.write("""
    **The Rise of Combine Harvesters:** With rural labor costs hitting 800-1000 BDT/day, machine harvesting has reached 
    a 25% adoption rate in the Haor regions, saving farmers nearly **30% in post-harvest costs**.
    """)
    st.progress(25, text="Mechanization Adoption Rate")

with tab_jute:
    st.write("""
    **Genome Mapping:** Following the 2010 decoding of the Jute genome, 2026 sees the rollout of 
    **short-duration varieties** that allow farmers to squeeze in an extra crop between 
    Jute and Rice seasons.
    """)

# --- Sidebar: Farm Management Logic ---
st.sidebar.header("Crop Choice Analyzer")
land_size = st.sidebar.number_input("Land Size (Decimal)", value=33)
labor_cost = st.sidebar.slider("Labor Cost (BDT/Day)", 500, 1500, 850)

# Simple Decision Logic
st.sidebar.divider()
if labor_cost > 900:
    st.sidebar.warning("Recommendation: Use Mechanical Harvester for higher ROI.")
else:
    st.sidebar.info("Recommendation: Traditional labor remains competitive at current rates.")

# --- Footer ---
st.write("###")
st.divider()
st.caption("Sources: Bangladesh Rice Research Institute (BRRI), BJRI (Jute Research Institute), & MOA 2026 Forecast.")