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
    
    .sd-card {
        background-color: #fff7ed;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #ea580c;
        margin-bottom: 15px;
    }
    .formula-text {
        font-family: 'Courier New', monospace;
        background-color: #f1f5f9;
        padding: 10px;
        border-radius: 4px;
        display: block;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("SD Module")
st.sidebar.warning("SD is a 'Non-Creditable' tax for most local supplies.")

# --- HEADER ---
st.title("Supplementary Duty (SD)")
st.markdown("#### Chapter 33 | Section 18-19 | VAT & SD Act, 2012")
st.divider()

# --- 1. THE CHARGING TRIGGER ---
st.subheader("Scope of Imposition")
st.markdown("""
SD is an additional tax over and above VAT. It is imposed on goods and services 
listed in the **Second Schedule** of the Act.
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="sd-card"><b>At Import Stage:</b> Collected by Customs on items like luxury vehicles, ACs, and high-end cosmetics.</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="sd-card"><b>At Manufacturing Stage:</b> Imposed when goods (e.g. beverages, cigarettes) are "removed" from the factory.</div>', unsafe_allow_html=True)

# --- 2. VALUATION LOGIC ---
st.subheader("How is SD Calculated?")

with st.expander("Formula for Local Manufacture"):
    st.markdown("The SD is calculated on the value **excluding** VAT.")
    st.markdown('<span class="formula-text">Value for SD = (Fair Market Price / 1.15) if VAT is 15%</span>', unsafe_allow_html=True)

with st.expander("Formula for Imports"):
    st.markdown("SD is calculated on a 'cascading' basis after Customs Duty.")
    st.markdown('<span class="formula-text">Value for SD = Assessable Value (AV) + CD + RD</span>', unsafe_allow_html=True)

# --- 3. COMMON SD RATES ---
st.subheader("Common SD Applicable Items")
sd_rates = {
    "Item Description": ["Carbonated Beverages", "Cigarettes/Tobacco", "Luxury Motor Cars", "SIM Card Services", "Cosmetics (Imported)"],
    "Typical SD Rate": ["25%", "65% - 150%", "20% - 500%", "15%", "10% - 20%"],
    "Basis": ["Ex-factory Price", "Retail Price", "Assessable Value", "Talk-time Value", "Assessable Value"]
}
st.table(pd.DataFrame(sd_rates))

# --- 4. NON-CREDITABILITY ---
st.subheader("⚖️ The 'Credit' Rule")
st.error("""
**Critical Limitation:** Unlike VAT, Supplementary Duty paid on inputs is **NOT** allowed as a credit 
against the Output VAT or Output SD of the final product. 
**Exception:** SD can be refunded ONLY if the final product is exported out of Bangladesh.
""")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For a factory producing FMCG (like beverages or personal care), 
SD is a direct cost to the P&L. Because you cannot take an 'Input Tax Credit' for SD 
paid on raw materials, it must be factored into your **COGS (Cost of Goods Sold)** and pricing strategy to protect margins.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Supplementary Duty Module © 2026</center>", unsafe_allow_html=True)