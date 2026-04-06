import streamlit as st

# --- DO NOT CALL set_page_config HERE (Handled by Homepage) ---

# --- STANDARD WEBPAGE STYLING ---
st.markdown("""
    <style>
    html, body, [class*="st-"] {
        font-size: 16px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1 { font-size: 2.1rem !important; color: #1E3A8A !important; }
    h2 { font-size: 1.6rem !important; color: #1E40AF !important; margin-top: 1.5rem !important; }
    h3 { font-size: 1.25rem !important; color: #1E40AF !important; }
    p, li { font-size: 1rem !important; line-height: 1.6; color: #374151; }
    
    .deadline-card {
        background-color: #fffaf0;
        padding: 20px;
        border-radius: 10px;
        border: 2px dashed #ed8936;
        text-align: center;
        margin: 20px 0;
    }
    .mushak-label {
        font-weight: bold;
        color: #fff;
        background-color: #1E3A8A;
        padding: 3px 8px;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Return Management")
st.sidebar.info("Section 64: The Monthly Compliance Deadline.")

# --- HEADER ---
st.title("Submission of VAT Returns")
st.markdown("#### Sections 64-66 | VAT & SD Act, 2012")
st.divider()

# --- 1. THE DEADLINE ---
st.subheader("🗓️ The Golden Rule of 15 Days")
st.markdown("""
Every registered person must submit a return for each tax period, whether 
taxable supplies were made or not.
""")

st.markdown("""
<div class="deadline-card">
    <h3 style="color: #c05621; margin:0;">Submission Deadline</h3>
    <p style="font-size: 1.2rem; font-weight: bold; margin: 10px 0;">15th Day of the Following Month</p>
    <p style="font-size: 0.9rem; color: #718096;">(Example: July Return is due by August 15th)</p>
</div>
""", unsafe_allow_html=True)

# --- 2. FORMS & TYPES ---
st.subheader("📋 Types of Returns")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Standard VAT Return** <span class="mushak-label">Mushak-9.1</span>  
    - Filed Monthly.  
    - Used by all VAT registered entities.  
    - Includes Output Tax, ITC, and Adjustments.
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    **Turnover Tax Return** <span class="mushak-label">Mushak-9.2</span>  
    - Filed Quarterly.  
    - Used by entities with turnover < Tk. 3 Crore.  
    - Simple 4% calculation.
    """, unsafe_allow_html=True)

# --- 3. AMENDMENTS & ERRORS ---
st.subheader("⚖️ Correcting Mistakes")
st.markdown("""
If you discover an error in a previously submitted return, the law allows for 
corrections under certain conditions:
""")

with st.expander("Amended Returns (Section 66)"):
    st.write("""
    * **Criteria:** Can be filed if the amendment doesn't decrease the tax payable or increase a refund (unless approved by the Commissioner).
    * **Restriction:** Cannot be filed if the NBR has already initiated an audit for that period.
    * **Time Limit:** Generally within 4 years of the original submission.
    """)

# --- 4. PENALTIES ---
st.error("""
**⚠️ Consequences of Late Filing:**
1. **Financial Penalty:** A non-negotiable fine of **Tk. 10,000**.
2. **BIN Suspension:** If returns are missing for 2 consecutive months, the BIN is locked in the IVAS system, stopping all factory imports and exports.
3. **Interest:** 2% simple interest per month on any unpaid tax amount.
""")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** In a manufacturing setup, the '15th' is a hard deadline. 
Ensure your **Mushak-9.1** reconciliation is completed by the 12th of every month 
to allow 48 hours for Treasury Challan processing and portal uploading. 
Remember: A 'Nil' return is mandatory if the factory is idle; never leave a 
month unfiled.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | VAT Return Module © 2026</center>", unsafe_allow_html=True)