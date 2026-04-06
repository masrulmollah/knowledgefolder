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
    
    .imposition-card {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DROPDOWN ---
st.sidebar.header("Imposition Guide")
menu = st.sidebar.selectbox("Select Topic:", 
    ["Scope of Imposition", "VAT Rate Structure", "Valuation of Supply", "Supplementary Duty (SD)"])

# --- HEADER ---
st.title("Imposition of VAT")
st.markdown(f"#### VAT & SD Act, 2012")
st.divider()

if menu == "Scope of Imposition":
    st.subheader("When is VAT Imposed? (Section 15)")
    st.markdown("""
    VAT is imposed on the following 'Taxable Events':
    """)
    
    st.markdown('<div class="imposition-card"><b>1. Import of Goods/Services:</b> Imposed on all imports into Bangladesh unless specifically exempted.</div>', unsafe_allow_html=True)
    st.markdown('<div class="imposition-card"><b>2. Taxable Supplies:</b> Imposed on goods or services supplied within Bangladesh by a registered person in the course of economic activity.</div>', unsafe_allow_html=True)
    
    st.info("💡 **Key Rule:** If a person is required to be registered but is not, they are still liable for the VAT on their supplies.")

elif menu == "VAT Rate Structure":
    st.subheader("Applicable VAT Rates (FY 2025-26)")
    
    rates_data = {
        "Rate Type": ["Standard Rate", "Reduced Rates", "Zero Rate", "Specific Tax"],
        "Percentage/Value": ["15%", "5%, 7.5%, 10%", "0%", "Fixed Amount"],
        "Application": ["Default for all supplies", "Essential items/services", "Exports & Deemed Exports", "Bricks, Petroleum, etc."]
    }
    st.table(pd.DataFrame(rates_data))
    
    st.warning("⚠️ **Note:** If you use Reduced Rates (other than 15%), you generally **cannot** claim Input Tax Credit (ITC) unless specifically allowed by the SRO.")

elif menu == "Valuation of Supply":
    st.subheader("Determining the Taxable Value (Section 16)")
    st.markdown("""
    The tax is calculated on the 'Value of Supply'. Here is how it is determined:
    """)
    
    with st.expander("Scenario A: Cash Consideration"):
        st.write("Value = (Total Consideration received) - (VAT amount included in that consideration).")
        
    with st.expander("Scenario B: Related Person / No Price"):
        st.write("Value = **Fair Market Value** of the supply (excluding VAT).")
        
    with st.expander("Scenario C: Imports"):
        st.write("Value = Assessable Value for Customs Duty + CD + RD + SD (if any).")

elif menu == "Supplementary Duty (SD)":
    st.subheader("Supplementary Duty (Section 18)")
    st.write("SD is an additional tax imposed on specific luxury or sensitive goods.")
    
    st.markdown("""
    * **Trigger:** Imposed at the time of import OR at the stage of manufacture/supply by the producer.
    * **Calculation:** SD is calculated on the value of the supply **before** VAT is applied.
    * **Non-Creditability:** Unlike VAT, SD paid on inputs is generally **not** creditable (except in very specific export cases).
    """)

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For factory costing, always distinguish between **15% standard VAT** (which is a balance sheet item/credit) and **SD or Reduced Rate VAT** (which often becomes a direct cost to the P&L). 
Ensure the sales team uses the correct 'Fair Market Value' for any promotional samples or inter-factory transfers.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Imposition Module © 2026</center>", unsafe_allow_html=True)