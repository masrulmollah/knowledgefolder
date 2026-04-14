import streamlit as st
import pandas as pd

# Note: No set_page_config here to avoid the "MustBeFirstCommandError"
# This file is meant to be called by your Homepage.py exec() logic.

# --- Custom Styling (Applied locally to this content) ---
st.markdown("""
    <style>
    .blog-header {
        color: #1E3A8A;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
    }
    .section-header {
        color: #1E40AF;
        border-bottom: 2px solid #1E40AF;
        padding-bottom: 5px;
        margin-top: 30px;
    }
    .highlight-box {
        background-color: #f0f9ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0369a1;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="blog-header">🌾 Agro-Economics: Markets & Value Chains</p>', unsafe_allow_html=True)
st.caption("Module: Economics & Finance | Knowledge Folder 2026")
st.markdown("---")

# --- Content Navigation ---
# Using tabs instead of sidebar radio to avoid conflicts with your main site sidebar
tab1, tab2, tab3 = st.tabs(["📊 Market Overview", "🔗 Value Chain", "💡 Strategic Potentials"])

with tab1:
    st.markdown('<h2 class="section-header">The Economic Landscape (2026)</h2>', unsafe_allow_html=True)
    st.write("""
    Bangladesh's agricultural economy is transitioning into a **commercialized powerhouse**. 
    With GDP contribution holding steady around **9.8%**, the focus has shifted from mere 
    yield to **market efficiency** and **value addition**.
    """)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Current Economic Drivers")
        st.markdown("""
        * **Inflation Resilience:** Adapting to an 8.5% food inflation rate.
        * **Export Standards:** Meeting Global GAP requirements for LDC graduation.
        * **Institutional Shift:** Growth of formal agro-processing units.
        """)
        
    with col2:
        # Integrated Data Visual
        gdp_data = pd.DataFrame({
            'Sector': ['Agriculture', 'Industry', 'Service'],
            'GDP Share (%)': [9.8, 38.5, 51.7]
        })
        st.bar_chart(gdp_data.set_index('Sector'))

with tab2:
    st.markdown('<h2 class="section-header">Value Chain Analysis</h2>', unsafe_allow_html=True)
    st.write("Optimizing the journey from farm-gate to consumer is the biggest financial opportunity in the sector.")
    
    st.markdown("""
    <div class="highlight-box">
    <strong>The Value Gap:</strong> Intermediaries (Beparis/Aratdars) often capture up to 40% of the 
    final retail price. Digitizing the value chain is essential to return margin to the producer.
    </div>
    """, unsafe_allow_html=True)
    
    # Analysis Table
    st.subheader("Price Spread Analysis (Sample Data)")
    price_data = pd.DataFrame({
        'Commodity': ['Potato', 'Onion', 'Mango', 'Rice (Premium)'],
        'Farm Price (BDT)': [15, 45, 60, 55],
        'Retail Price (BDT)': [35, 85, 150, 80],
        'Margin Gap (%)': ['133%', '88%', '150%', '45%']
    })
    st.table(price_data)

with tab3:
    st.markdown('<h2 class="section-header">Strategic & Future Potentials</h2>', unsafe_allow_html=True)
    
    exp1 = st.expander("🚀 High-Value Crop (HVC) Expansion")
    exp1.write("""
    Shifting land allocation from traditional grains to high-value horticulture (like exotic fruits 
    and organic vegetables) can increase per-acre profitability by 3x.
    """)
    
    exp2 = st.expander("🏗️ Cold Chain Infrastructure")
    exp2.write("""
    Investment in decentralized, solar-powered cold storage could reduce post-harvest losses 
    by an estimated 20%, significantly stabilizing market prices.
    """)
    
    exp3 = st.expander("📱 Agri-Fintech Integration")
    exp3.write("""
    Using Python-based risk scoring and mobile financial services to provide credit to 
    unbanked farmers based on historical production data.
    """)

# --- Footer ---
st.markdown("---")
st.info("This content is part of the automated Knowledge Folder analytics module.")