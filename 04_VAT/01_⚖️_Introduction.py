import streamlit as st
import pandas as pd

# --- DO NOT CALL set_page_config HERE ---
# It is already handled by your main 1_🤓_Homepage.py file.

# --- PROFESSIONAL WEBPAGE STYLING ---
st.markdown("""
    <style>
    /* Standardizing global font size to 16px */
    html, body, [class*="st-"] {
        font-size: 16px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Standard Web Headings */
    h1 { font-size: 2.2rem !important; color: #1E3A8A !important; }
    h2 { font-size: 1.75rem !important; color: #1E40AF !important; margin-top: 1.5rem !important; }
    h3 { font-size: 1.25rem !important; color: #1E40AF !important; }
    
    /* Standard Paragraphs */
    p { font-size: 1rem !important; line-height: 1.6; color: #374151; }

    /* Alert and Note Boxes */
    .lead-note {
        background-color: #f0f7ff;
        padding: 15px;
        border-left: 5px solid #1E3A8A;
        border-radius: 4px;
        font-size: 0.95rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("Value Added Tax (VAT) in Bangladesh")
st.markdown("### Introduction to VAT & SD Act, 2012")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("VAT Module")
menu = st.sidebar.radio("Navigation", 
    ["Overview", "Registration Thresholds", "Key Definitions", "VAT Rate Structure"])

if menu == "Overview":
    st.markdown("## Introduction")
    st.markdown("""
    Value Added Tax (VAT) is a modern, indirect tax imposed on the value addition at each stage of the 
    production and distribution of goods and services. The tax is ultimately borne by the final consumer, 
    making it a consumption-based tax system.
    """)
    
    st.info("**Legislative Framework:** The current regime is governed by the **Value Added Tax and Supplementary Duty Act, 2012**, which became effective on July 1, 2019.")
    
    st.markdown("### Core Features")
    st.markdown("""
    * **Multi-stage Tax:** Collected at every point of sale from manufacture to retail.
    * **Input Tax Credit:** Prevents the "tax on tax" effect by allowing businesses to offset purchase VAT.
    * **Self-Assessment:** Taxpayers are responsible for determining their own tax liability.
    """)

elif menu == "Registration Thresholds":
    st.markdown("## Registration & Enlistment Thresholds")
    st.markdown("Determining whether an entity must register for VAT or Enlist for Turnover Tax depends on annual turnover.")
    
    threshold_data = {
        "Annual Turnover Range": ["Below Tk. 3,000,000", "Tk. 3,000,001 to 5,000,000", "Above Tk. 5,000,000"],
        "Classification": ["Exempted", "Turnover Tax (Enlistment)", "VAT (Registration)"],
        "Tax Obligation": ["None", "4% Turnover Tax", "15% Standard or Reduced Rates"]
    }
    st.table(pd.DataFrame(threshold_data))
    
    st.warning("⚠️ **Mandatory Registration:** Regardless of turnover, certain sectors like importers, large manufacturers, and specific service providers must register for VAT.")

elif menu == "Key Definitions":
    st.markdown("## Key Regulatory Definitions")
    
    with st.expander("Economic Activity"):
        st.markdown("Any activity carried on regularly for profit or otherwise. It includes business, trade, and manufacturing but **excludes** services provided by an employee to an employer (Salary).")
        
    with st.expander("Input Tax Credit (VDS)"):
        st.markdown("The tax paid on your business inputs (Raw materials, utilities). For a factory, this is the most critical area to manage to reduce overall tax burden.")
        
    with st.expander("Taxable Supply"):
        st.markdown("Any supply of goods or services made in Bangladesh other than an exempted supply.")

elif menu == "VAT Rate Structure":
    st.markdown("## Current VAT Rates (FY 2025-26)")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Standard Rate", "15%")
        st.write("Full input tax credit allowed.")
    with c2:
        st.metric("Turnover Tax", "4%")
        st.write("No input tax credit allowed.")
    
    st.divider()
    st.markdown("### Reduced Rates & Zero Rating")
    st.markdown("""
    * **0% (Zero-rated):** Exports and deemed exports.
    * **5% / 7.5% / 10%:** Specific essential items and services (e.g., ITES, specific construction materials).
    * **Fixed/Specific Tax:** Applied to certain items like bricks or petroleum.
    """)

# --- FOOTER ---
st.divider()
st.markdown(f"""
<div class="lead-note">
    <b>💡 Finance Lead Note:</b> As an accountant, ensure your <b>Mushak-6.3</b> (Tax Invoice) 
    reconciliation is performed monthly. Any gap in documentation results in the loss of Input Tax Credits, 
    directly impacting factory profitability.
</div>
""", unsafe_allow_html=True)