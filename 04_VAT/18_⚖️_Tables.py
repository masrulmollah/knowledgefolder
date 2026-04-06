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
    p, li { font-size: 1rem !important; line-height: 1.6; color: #374151; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #f1f5f9;
        border-radius: 5px 5px 0 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("VAT Annexures & Reference Tables")
st.markdown("#### Statutory Forms, Rates & System Comparisons")
st.divider()

# --- TABS FOR ANNEXURES ---
tab1, tab2, tab3 = st.tabs([
    "📄 Annex A: Mushak Forms", 
    "📊 Annex B: VAT Rates", 
    "⚖️ Annex C: VAT vs Turnover Tax"
])

# --- ANNEX A: MUSHAK FORMS ---
with tab1:
    st.subheader("Summary of Important Mushak Forms")
    mushak_forms = [
        {"Form No": "Mushak-1.1", "Purpose": "Application for Registration / Enlistment"},
        {"Form No": "Mushak-2.1", "Purpose": "VAT Registration Certificate / Turnover Tax Certificate"},
        {"Form No": "Mushak-4.3", "Purpose": "Input-Output Coefficient (Price Declaration)"},
        {"Form No": "Mushak-6.1", "Purpose": "Purchase Register"},
        {"Form No": "Mushak-6.2", "Purpose": "Sales Register"},
        {"Form No": "Mushak-6.3", "Purpose": "Tax Invoice (Standard)"},
        {"Form No": "Mushak-6.6", "Purpose": "VDS Certificate (Withholding VAT)"},
        {"Form No": "Mushak-6.7 / 6.8", "Purpose": "Credit Note / Debit Note"},
        {"Form No": "Mushak-9.1", "Purpose": "Monthly VAT Return"},
        {"Form No": "Mushak-10.1", "Purpose": "Application for VAT Refund"}
    ]
    st.table(pd.DataFrame(mushak_forms))
    st.caption("Reference: Section 107 of the VAT & SD Act 2012.")

# --- ANNEX B: VAT RATES ---
with tab2:
    st.subheader("Standard vs Reduced VAT Rates")
    st.markdown("Rates applicable for the current fiscal year as per the Third Schedule.")
    
    vat_rates = [
        {"Category": "Standard Rate", "Rate": "15%", "Input Credit": "Allowed"},
        {"Category": "Export / Zero Rated", "Rate": "0%", "Input Credit": "Allowed (Refundable)"},
        {"Category": "Reduced Rate (Services)", "Rate": "5% / 7.5% / 10%", "Input Credit": "Generally Not Allowed"},
        {"Category": "Specific Tax (Fixed)", "Rate": "Fixed Amount", "Input Credit": "Not Allowed"},
        {"Category": "Exempted Goods", "Rate": "0%", "Input Credit": "Not Allowed"}
    ]
    st.table(pd.DataFrame(vat_rates))
    st.info("💡 **Note:** If you pay VAT at a reduced rate, you lose the right to claim Input Tax Credit on your raw materials.")

# --- ANNEX C: COMPARISON ---
with tab3:
    st.subheader("Comparison: VAT vs. Turnover Tax")
    comparison_data = {
        "Feature": ["Eligibility", "Rate", "Input Tax Credit", "Return Filing", "Threshold"],
        "VAT System": ["Annual Turnover > 3 Crore", "Standard 15% (or reduced)", "Full Credit Allowed", "Monthly (Mushak-9.1)", "Compulsory for Ltd Co."],
        "Turnover Tax System": ["Annual Turnover < 3 Crore", "Flat 4%", "No Credit Allowed", "Quarterly (Mushak-9.2)", "Small/Micro businesses"]
    }
    st.table(pd.DataFrame(comparison_data))

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For factory operations, the **Mushak-4.3 (Input-Output Coefficient)** is your most critical master data. If your actual consumption of raw materials 
deviates from the declared coefficient by more than 10%, the NBR can reject 
your Input Tax Credits. Always ensure Annexure A's documents are archived 
digitally for 5 years.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | VAT Annexures Module © 2026</center>", unsafe_allow_html=True)