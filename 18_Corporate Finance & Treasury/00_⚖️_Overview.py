import streamlit as st

# --- STYLING & CUSTOM CSS ---
st.markdown("""
    <style>
    .main-header {
        color: #1E293B;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        color: #64748B;
        font-size: 18px;
        text-align: center;
        margin-bottom: 40px;
    }
    .module-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        height: 250px;
        transition: transform 0.2s;
    }
    .module-card:hover {
        transform: translateY(-5px);
        border-color: #3B82F6;
    }
    .module-title {
        color: #1E3A8A;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .module-desc {
        color: #475569;
        font-size: 14px;
        line-height: 1.5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header">CFO Mastery Curriculum Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">A comprehensive roadmap from Technical Finance to Corporate Strategy</div>', unsafe_allow_html=True)

# --- MODULE GRID ---
# Creating a 3x2 Grid for the 6 Modules
col1, col2, col3 = st.columns(3)

modules = [
    {
        "id": "M1",
        "title": "1. Finance Foundations",
        "desc": "Master the Time Value of Money, NPV, and WACC. Learn to evaluate projects based on value creation.",
        "color": "#3B82F6", # Blue
        "col": col1
    },
    {
        "id": "M2",
        "title": "2. Capital Structure",
        "desc": "Balance Debt vs. Equity. Understand Tax Shields and Dividend/Buyback strategies to optimize firm value.",
        "color": "#10B981", # Green
        "col": col2
    },
    {
        "id": "M3",
        "title": "3. Treasury Management",
        "desc": "Manage the pulse of the business. Optimize the Cash Conversion Cycle and 13-week liquidity forecasting.",
        "color": "#8B5CF6", # Purple
        "col": col3
    },
    {
        "id": "M4",
        "title": "4. Financial Risk",
        "desc": "Protect the P&L from external volatility. Learn FX Hedging, Interest Rate Swaps, and Derivative strategies.",
        "color": "#EF4444", # Red
        "col": col1
    },
    {
        "id": "M5",
        "title": "5. Treasury Tech",
        "desc": "Modernize the function. Implement TMS systems, secure bank connectivity (SWIFT), and dual controls.",
        "color": "#475569", # Slate
        "col": col2
    },
    {
        "id": "M6",
        "title": "6. Strategic Finance",
        "desc": "The Executive level. Master M&A valuation, Corporate Governance, and International Tax navigation.",
        "color": "#111827", # Black
        "col": col3
    }
]

for mod in modules:
    with mod["col"]:
        st.markdown(f"""
            <div class="module-card" style="border-top: 5px solid {mod['color']};">
                <div class="module-title">{mod['title']}</div>
                <div class="module-desc">{mod['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
        st.write("") # Spacer

st.divider()

# --- INTERACTIVE PROGRESS TRACKER ---
st.subheader("🏁 CFO Readiness Tracker")
st.write("Mark the modules you have completed to see your progress:")

c1, c2 = st.columns([1, 2])
with c1:
    m1_check = st.checkbox("Module 1: Foundations")
    m2_check = st.checkbox("Module 2: Capital Structure")
    m3_check = st.checkbox("Module 3: Treasury Ops")
    m4_check = st.checkbox("Module 4: Risk Management")
    m5_check = st.checkbox("Module 5: Tech & Security")
    m6_check = st.checkbox("Module 6: Strategy & M&A")

# Calculate Progress
checks = [m1_check, m2_check, m3_check, m4_check, m5_check, m6_check]
completed = sum(checks)
progress = completed / 6

with c2:
    st.write(f"### Overall Mastery: {int(progress * 100)}%")
    st.progress(progress)
    
    if completed == 0:
        st.info("Select a module from the sidebar to begin your journey.")
    elif completed < 3:
        st.warning("You are building a strong foundation. Keep going!")
    elif completed < 6:
        st.success("You are moving into advanced strategic territory!")
    else:
        st.balloons()
        st.markdown("🚀 **Congratulations! You have covered the full CFO Syllabus.**")

# --- FOOTER ---
st.divider()
st.caption("Developed for the Modern Finance Professional | 2026 Edition")