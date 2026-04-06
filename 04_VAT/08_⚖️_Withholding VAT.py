import streamlit as st
import pandas as pd

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
    
    .vds-card {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("Withholding VAT (VDS) Portal")
st.markdown("#### Section 21 & VDS Rules | VAT & SD Act, 2012")
st.divider()

# --- TABS FOR ORGANIZATION ---
tab1, tab2 = st.tabs(["🔍 Search Rate Chart", "⚖️ Legal & Compliance Details"])

with tab1:
    st.subheader("VDS Service Code & Rate Schedule")
    
    # Full data from pages 511-513
    vds_data = [
        {"SL": 1, "Service Code": "S001.00", "Description": "Hotel", "Rate of VDS": "15%"},
        {"SL": 2, "Service Code": "S002.00", "Description": "Restaurants", "Rate of VDS": "15% (Non-AC: 7.5%)"},
        {"SL": 3, "Service Code": "S003.10", "Description": "Decorator & Caterer", "Rate of VDS": "15%"},
        {"SL": 4, "Service Code": "S003.20", "Description": "Motor vehicle garage & workshop", "Rate of VDS": "10%"},
        {"SL": 5, "Service Code": "S004.00", "Description": "Dockyard", "Rate of VDS": "10%"},
        {"SL": 6, "Service Code": "S007.00", "Description": "Advertising Firm", "Rate of VDS": "15%"},
        {"SL": 7, "Service Code": "S008.10", "Description": "Printing Press", "Rate of VDS": "10%"},
        {"SL": 8, "Service Code": "S010.10", "Description": "Auction Firm", "Rate of VDS": "10%"},
        {"SL": 9, "Service Code": "S014.00", "Description": "Land Development Firm", "Rate of VDS": "2% or 3%"},
        {"SL": 10, "Service Code": "S015.10", "Description": "Construction Firm", "Rate of VDS": "7.5%"},
        {"SL": 11, "Service Code": "S020.00", "Description": "Survey Agency", "Rate of VDS": "15%"},
        {"SL": 12, "Service Code": "S024.00", "Description": "Courier Service", "Rate of VDS": "15%"},
        {"SL": 13, "Service Code": "S032.00", "Description": "Culture/Entertainment service", "Rate of VDS": "15%"},
        {"SL": 14, "Service Code": "S037.00", "Description": "Procurement Provider", "Rate of VDS": "5%"},
        {"SL": 15, "Service Code": "S040.00", "Description": "Security Service", "Rate of VDS": "10%"},
        {"SL": 16, "Service Code": "S048.00", "Description": "Consultancy & Supervisory Firm", "Rate of VDS": "15%"},
        {"SL": 17, "Service Code": "S049.00", "Description": "Lease Holder", "Rate of VDS": "15%"},
        {"SL": 20, "Service Code": "S060.00", "Description": "Chartered Flight/Helicopter", "Rate of VDS": "15%"},
        {"SL": 21, "Service Code": "S065.00", "Description": "Cleaning/Maintenance Firm", "Rate of VDS": "10%"},
        {"SL": 23, "Service Code": "S071.00", "Description": "Information Technology Enabled Services (ITES)", "Rate of VDS": "5%"},
        {"SL": 24, "Service Code": "S099.10", "Description": "Other Miscellaneous Services", "Rate of VDS": "15%"}
    ]
    df = pd.DataFrame(vds_data)

    # Search Bar
    search_q = st.text_input("Quick Search (Code or Description):", placeholder="Search 'S037' or 'Consultancy'...")
    
    if search_q:
        df = df[df['Description'].str.contains(search_q, case=False) | df['Service Code'].str.contains(search_q, case=False)]

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.caption("Note: Rates are indicative of the 2025-26 fiscal year schedules.")

with tab2:
    st.subheader("Core VDS Compliance Rules")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Who Must Withhold?**
        - All Limited Companies.
        - Government & Semi-govt bodies.
        - NGOs, Banks, and Insurance.
        
        **The 15% Standard Rule:**
        Generally, if a supplier provides a **15% Mushak-6.3**, VDS is not required (except for specific services like Construction or Procurement).
        """)
        
    with col2:
        st.markdown("""
        **The Mushak-6.6 Certificate:**
        - Must be issued within **15 days** of deduction.
        - Required by the supplier to take a **Decreasing Adjustment**.
        - Valid for only **4 tax periods**.
        """)

    st.divider()
    st.error("**⚠️ Penalty for Non-Compliance:** Failure to deduct or deposit VDS leads to personal liability for the amount, plus a **2% monthly interest** penalty.")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For factory MIS, reconcile the VDS payable ledger monthly. 
Ensure the **Service Code** used in the search table above matches exactly with your 
supplier's Mushak-6.3. Any mismatch can trigger an audit objection during NBR inspections.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | VDS Integrated Portal © 2026</center>", unsafe_allow_html=True)