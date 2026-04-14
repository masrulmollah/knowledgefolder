import streamlit as st
import pandas as pd

# --- Custom Styling for "Growth" Theme ---
st.markdown("""
    <style>
    .growth-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-top: 5px solid #8b5cf6;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 250px;
    }
    .growth-title {
        color: #5b21b6;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 10px;
    }
    .growth-text {
        color: #4b5563;
        font-size: 14px;
    }
    .status-badge {
        background-color: #ede9fe;
        color: #7c3aed;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #4c1d95;'>🚀 Agro-Potentials: High-Growth Frontiers</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280;'>Identifying the Next S-Curve in Bangladesh's Agriculture</p>", unsafe_allow_html=True)
st.write("---")

# --- Introduction ---
st.write("""
Beyond traditional rice and jute production, Bangladesh is sitting on several **untapped frontiers**. 
As a finance professional, viewing these through the lens of **ROI and Scalability** reveals 
significant opportunities for 2026 and beyond.
""")

# --- Growth Frontiers Grid ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="growth-card">
        <span class="status-badge">HIGH GROWTH</span>
        <p class="growth-title">🌊 The Blue Economy</p>
        <p class="growth-text">
        With a massive coastline, the potential for <b>Seaweed Farming</b> and <b>Marine Aquaculture</b> 
        is valued at over $1.2 billion. Seaweed is a low-input, high-output crop for the 
        global cosmetics and food additive industries.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("###") # Spacer
    
    st.markdown("""
    <div class="growth-card">
        <span class="status-badge">STRATEGIC</span>
        <p class="growth-title">📦 Niche Export Markets</p>
        <p class="growth-text">
        High-value horticulture (Mangoes, Lychees, and Organic Vegetables) targeted at 
        EU and Middle Eastern markets. Meeting GAP (Good Agricultural Practices) 
        standards is the key bottleneck to unlock this growth.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="growth-card">
        <span class="status-badge">TECH-DRIVEN</span>
        <p class="growth-title">💳 Agri-Fintech (Embedded Finance)</p>
        <p class="growth-text">
        Bridging the $2.5 billion credit gap for smallholders. Using <b>alternative data</b> 
        (satellite imagery, past yield) to provide instant loans, bypassing 
        traditional collateral requirements.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("###") # Spacer
    
    st.markdown("""
    <div class="growth-card">
        <span class="status-badge">URBANIZATION</span>
        <p class="growth-title">🏙️ Vertical & Controlled Farming</p>
        <p class="growth-text">
        As arable land shrinks by 1% annually, hydroponics and rooftop farming in Dhaka/Chittagong 
        offer a solution for year-round, chemical-free vegetable production near the consumer.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- Strategic Deep Dive ---
st.write("---")
st.subheader("Investment & Scalability Matrix")

# Sample Data for Potential Analysis
potential_data = pd.DataFrame({
    'Sector': ['Blue Economy', 'Niche Exports', 'Agri-Fintech', 'Vertical Farming'],
    'Growth Potential': [85, 70, 95, 60],
    'Initial CapEx': ['Medium', 'High', 'Low', 'Very High'],
    'Time to Market': ['2-3 Years', '1-2 Years', '< 1 Year', '1 Year']
})

st.dataframe(potential_data, use_container_width=True)

# --- Future Outlook Expander ---
with st.expander("🔍 Future Outlook: 2030 Vision"):
    st.write("""
    1.  **Circular Bio-Economy:** Utilizing agro-waste (rice husk, poultry litter) for bio-energy and organic fertilizer.
    2.  **Seed Sovereignty:** Heavy investment in indigenous R&D for climate-smart hybrid seeds.
    3.  **Logistics Transformation:** The emergence of "Uber for Tractors" and cold-chain-as-a-service providers.
    """)

# --- Footer ---
st.write("###")
st.warning("Potential outcomes are subject to global commodity price stability and infrastructure development speed.")
st.caption("Developed for the 'Knowledge Folder' Strategic Module.")