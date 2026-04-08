import streamlit as st

# --- DO NOT CALL set_page_config HERE ---
# It is already handled by 1_🤓_Homepage.py

# --- CUSTOM CSS FOR PROFESSIONAL BRANDING ---
st.markdown("""
    <style>
    .feature-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-top: 5px solid #1E3A8A;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 250px;
    }
    .card-title {
        color: #1E3A8A;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
col_left, col_right = st.columns([1.5, 1])

with col_left:
    #st.title("Knowledge Folder")
    st.subheader("The Professional Repository for Finance Leaders")
    st.markdown("""
    Welcome to a curated hub designed specifically for **Finance and Accounting professionals** in Bangladesh. 
    Whether you are a seasoned CFO or a student aspiring to join the ranks of qualified professionals (FCA, ACMA, CIMA), 
    this folder provides the technical depth and analytical tools you need to excel.
    """)

with col_right:
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=500")

st.divider()

# --- CORE KNOWLEDGE PILLARS ---
st.header("🛠️ Core Knowledge Pillars")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="card-title">⚖️ Regulatory Laws</div>
        <p>Simplified summaries of the <b>Income Tax Act 2023</b>, VAT regulations, and the Companies Act.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="card-title">📊 Analytics & IFRS</div>
        <p>Resources on <b>Python for Finance</b>, Power BI automation, and IAS/IFRS interpretations.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="card-title">💼 Talent & Careers</div>
        <p>Showcasing a <b>CV Bank</b> of elite, qualified finance professionals in Bangladesh.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("<center>Knowledge Folder | Designed for the Leaders of Tomorrow</center>", unsafe_allow_html=True)