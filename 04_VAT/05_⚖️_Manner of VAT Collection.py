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
    
    .collection-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #1E3A8A;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DROPDOWN ---
st.sidebar.header("Collection Module")
menu = st.sidebar.selectbox("Manner of Collection:", 
    ["Import Stage", "Domestic Supply Stage", "VDS (Withholding)", "Time of Payment"])

# --- HEADER ---
st.title("Manner of VAT Collection")
st.markdown(f"#### Section 15-21 | VAT & SD Act, 2012")
st.divider()

if menu == "Import Stage":
    st.subheader("Collection on Imports")
    st.markdown("""
    VAT on imported goods is collected as if it were a Customs Duty.
    """)
    
    st.markdown('<div class="collection-card"><b>Authority:</b> Collected by the Commissioner of Customs.</div>', unsafe_allow_html=True)
    st.markdown('<div class="collection-card"><b>Timing:</b> Collected at the time of clearing the goods from the port.</div>', unsafe_allow_html=True)
    
    st.info("**Valuation for Imports:** Taxable Value = AV + CD + RD + SD. VAT (usually 15%) is applied on this total amount.")

elif menu == "Domestic Supply Stage":
    st.subheader("Collection on Local Supplies")
    st.write("For supplies made within Bangladesh, the responsibility lies with the registered person.")
    
    st.markdown("""
    * **The Seller's Duty:** Charge VAT on the invoice, collect it from the buyer, and record it in the **Sales Register (Mushak-6.1)**.
    * **The Return:** The collected amount (Output Tax) is reported in the monthly VAT return (Mushak-9.1).
    * **Net Payment:** The seller pays the Treasury the *difference* between Output Tax and Input Tax Credit.
    """)

elif menu == "VDS (Withholding)":
    st.subheader("VAT Deduction at Source (Section 21)")
    st.write("VDS is a mechanism to ensure collection from the service/goods provider.")
    
    st.warning("⚠️ **Withholding Entities:** Includes Government bodies, NGOs, Banks, Insurance companies, and Limited Companies.")
    
    st.markdown("""
    1. The buyer (Withholding Entity) deducts the VAT amount from the supplier's bill.
    2. The buyer issues a **VDS Certificate (Mushak-6.6)** to the supplier.
    3. The buyer deposits the deducted amount to the Treasury.
    """)
    
    st.info("💡 **Finance Lead Note:** Ensure your AP team collects the Mushak-6.6 for every deduction. Without it, you cannot take an 'Increasing Adjustment' or a 'Decreasing Adjustment' effectively in your records.")

elif menu == "Time of Payment":
    st.subheader("When does the liability arise? (Section 22)")
    st.markdown("""
    VAT becomes payable at the **Time of Supply**. This is triggered by the **earliest** of the following events:
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("🚚 **Delivery**")
        st.caption("When goods are made available to the buyer.")
    with col2:
        st.write("📄 **Invoicing**")
        st.caption("When the Mushak-6.3 is issued.")
    with col3:
        st.write("💰 **Payment**")
        st.caption("When partial or full payment is received.")

# --- FOOTER ---
st.divider()
st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | VAT Collection Module © 2026</center>", unsafe_allow_html=True)