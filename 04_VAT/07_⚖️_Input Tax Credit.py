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
    
    .compliance-box {
        background-color: #f0fdf4;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #16a34a;
        margin-bottom: 15px;
    }
    .warning-box {
        background-color: #fef2f2;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #dc2626;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("ITC Management")
st.sidebar.info("Section 46: The 'Heart' of the VAT System.")

# --- HEADER ---
st.title("Input Tax Credit (ITC)")
st.markdown("#### Section 46 | VAT & SD Act, 2012")
st.divider()

# --- 1. CORE ENTITLEMENT ---
st.subheader("Entitlement to Credit")
st.markdown("""
A registered person is entitled to an input tax credit if the goods or services 
are imported or acquired for use in an **economic activity**.
""")

st.markdown("""
<div class="compliance-box">
    <b>✅ Mandatory Documents for ITC:</b><br>
    1. Import: Bill of Entry (duly cleared).<br>
    2. Local Purchase: Tax Invoice (Mushak-6.3) in the name of the buyer.<br>
    3. Payment: Bank transfer proof for amounts > Tk. 100,000.
</div>
""", unsafe_allow_html=True)

# --- 2. THE 4-MONTH RULE ---
st.subheader("⏳ The Limitation Period")
st.info("""
Under the current law, an Input Tax Credit must be claimed in the return of the 
tax period in which the invoice was issued, or within the **following 4 tax periods**.
""")

# --- 3. NEGATIVE LIST ---
st.subheader("🚫 Non-Eligible for Credit")
st.markdown("Even if VAT is paid, credit is **NOT** allowed for the following:")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    * Luxury goods or entertainment.
    * Passenger motor vehicles (unless for rent/sale).
    * Fuel for passenger vehicles.
    """)

with col2:
    st.markdown("""
    * Exempted supplies.
    * Reduced rate purchases (e.g., 5% or 7.5% VAT) unless specifically permitted.
    * Supplies without a 13-digit BIN.
    """)

# --- 4. PARTIAL INPUT TAX ---
st.subheader("⚖️ Partial Input Tax Credit")
st.markdown("""
If you use inputs for both taxable and exempted supplies, you must calculate 
the credit proportionately:
""")
st.latex(r"Credit = \text{Input Tax} \times \frac{\text{Value of Taxable Supplies}}{\text{Total Value of Supplies}}")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For a factory, the 'Input Tax Credit' is a cash asset. 
Ensure your procurement team never accepts a **Mushak-6.3** with errors in the BIN or Address. 
A single clerical error on an invoice can lead to the disallowance of millions in credits 
during a post-clearance audit.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Input Tax Credit Module © 2026</center>", unsafe_allow_html=True)