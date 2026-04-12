import streamlit as st

# Color palette
PRIMARY = "#1a3a5c"
ACCENT = "#c8922a"
LIGHT_BG = "#f4f1eb"
CARD_BG = "#ffffff"
SUCCESS = "#2d7a4f"
WARNING = "#c8922a"
DANGER = "#b33a3a"
TEXT = "#2c2c2c"

def apply_base_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Source+Sans+3:wght@300;400;600&family=Fira+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Source Sans 3', sans-serif;
        background-color: #f4f1eb;
        color: #2c2c2c;
    }

    .stApp { background-color: #f4f1eb; }

    /* Hide default streamlit header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* --- SIDEBAR STYLING FIXES --- */
    section[data-testid="stSidebar"] {
        background: #1a3a5c;
    }

    /* Target standard text in sidebar to be white */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] span {
        color: rgba(255,255,255,0.87) !important;
    }

    /* FIX: Visibility for Selectbox/Dropdown text */
    /* Closed state box */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        color: #1a3a5c !important; 
        background-color: #ffffff !important;
        border-radius: 8px;
    }

    /* Dropdown menu items (when clicked) */
    div[data-baseweb="popover"] ul, 
    div[data-baseweb="popover"] li {
        color: #1a3a5c !important;
        background-color: #ffffff !important;
    }

    /* Ensure labels for inputs are still legible in white */
    section[data-testid="stSidebar"] label p {
        color: rgba(255,255,255,0.9) !important;
    }

    /* --- COMPONENTS --- */
    .hero-banner {
        background: linear-gradient(135deg, #1a3a5c 0%, #0d2340 60%, #2c5f8a 100%);
        border-radius: 16px; padding: 48px 40px; margin-bottom: 32px;
        position: relative; overflow: hidden;
    }
    .hero-title {
        font-family: 'Playfair Display', serif; font-size: 2.6rem;
        font-weight: 700; color: #ffffff; margin-bottom: 16px;
    }
    .hero-subtitle { color: rgba(255,255,255,0.75); line-height: 1.7; }

    .section-heading {
        font-family: 'Playfair Display', serif; font-size: 1.5rem;
        font-weight: 600; color: #1a3a5c; border-left: 4px solid #c8922a;
        padding-left: 14px; margin: 28px 0 16px 0;
    }

    .info-card {
        background: #ffffff; border-radius: 12px; padding: 22px 24px;
        margin-bottom: 16px; border: 1px solid #e8e0d0;
        box-shadow: 0 2px 8px rgba(26,58,92,0.06);
    }

    .law-section-box {
        background: linear-gradient(135deg, #1a3a5c08, #c8922a10);
        border: 1px solid #c8922a40; border-left: 4px solid #c8922a;
        border-radius: 10px; padding: 16px 20px;
        font-family: 'Fira Mono', monospace; font-size: 0.88rem;
    }

    .warning-box {
        background: #fff5f5; border: 1px solid #f0a0a0;
        border-left: 4px solid #b33a3a; padding: 16px 20px; color: #7a2020;
    }

    .success-box {
        background: #f0faf4; border: 1px solid #90d0a8;
        border-left: 4px solid #2d7a4f; padding: 16px 20px; color: #1a4a30;
    }

    .recap-box {
        background: linear-gradient(135deg, #1a3a5c, #0d2340);
        border-radius: 14px; padding: 28px 32px; color: #fff;
    }
    .recap-box h3 { font-family: 'Playfair Display', serif; color: #c8922a; }

    /* Table styling */
    table { width: 100%; border-collapse: collapse; margin: 12px 0; }
    th { background: #1a3a5c; color: white; padding: 10px 14px; text-align: left; }
    td { padding: 9px 14px; border-bottom: 1px solid #e8e0d0; }
    tr:nth-child(even) td { background: #f9f6f0; }

    </style>
    """, unsafe_allow_html=True)

# Helper functions
def hero(module_num, title, subtitle, icon="📘"):
    st.markdown(f"""
    <div class="hero-banner">
        <div style="font-family:'Fira Mono',monospace; font-size:12px; color:#c8922a; letter-spacing:3px; text-transform:uppercase; margin-bottom:12px;">
            📚 Company Act of Bangladesh &nbsp;|&nbsp; Module {module_num}
        </div>
        <div class="hero-title">{icon} {title}</div>
        <div class="hero-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def section_heading(text):
    st.markdown(f'<div class="section-heading">{text}</div>', unsafe_allow_html=True)

def law_box(text):
    st.markdown(f'<div class="law-section-box">⚖️ &nbsp;{text}</div>', unsafe_allow_html=True)

def tip_box(title, body):
    st.markdown(f"""
    <div class="tip-box" style="background:linear-gradient(135deg, #fff8ec, #fff3e0); border: 1px solid #f0c060; border-radius:12px; padding:18px 22px; margin:16px 0;">
        <div style="font-family:'Playfair Display',serif; font-size:0.95rem; font-weight:700; color:#b07a10; margin-bottom:6px;">💡 {title}</div>
        <div style="font-size:0.92rem; color:#5a4a20; line-height:1.6;">{body}</div>
    </div>
    """, unsafe_allow_html=True)

def warning_box(text):
    st.markdown(f'<div class="warning-box">⚠️ &nbsp;{text}</div>', unsafe_allow_html=True)

def success_box(text):
    st.markdown(f'<div class="success-box">✅ &nbsp;{text}</div>', unsafe_allow_html=True)

def gold_divider():
    st.markdown('<hr style="border:none; height:2px; background:linear-gradient(to right, #c8922a, transparent); margin:24px 0;">', unsafe_allow_html=True)

def recap_box(points: list):
    items = "".join(f"<li>{p}</li>" for p in points)
    st.markdown(f"""
    <div class="recap-box">
        <h3>🔁 Quick Recap</h3>
        <ul>{items}</ul>
    </div>
    """, unsafe_allow_html=True)

def metric_row(metrics: list):
    cols = st.columns(len(metrics))
    for col, (num, label) in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div style="background:#ffffff; border-radius:10px; padding:18px 16px; text-align:center; border:1px solid #e8e0d0; box-shadow:0 2px 6px rgba(26,58,92,0.05);">
                <div style="font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:#1a3a5c;">{num}</div>
                <div style="font-size:0.82rem; color:#888; text-transform:uppercase; letter-spacing:1px;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

def sidebar_nav():
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center; padding: 20px 0 10px 0;">
            <div style="font-family:'Playfair Display',serif; font-size:1.3rem; color:#c8922a; font-weight:700;">
                📚 Knowledge Folder
            </div>
            <div style="font-size:0.78rem; color:rgba(255,255,255,0.5); margin-top:4px; letter-spacing:2px;">
                COMPANY ACT OF BANGLADESH
            </div>
        </div>
        <hr style="border-color:rgba(255,255,255,0.1); margin:10px 0 18px 0;">
        """, unsafe_allow_html=True)