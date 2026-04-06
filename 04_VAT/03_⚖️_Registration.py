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
    
    .compliance-card {
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
st.sidebar.header("Registration Guide")
menu = st.sidebar.selectbox("Select Topic:", 
    ["Registration Thresholds", "Mandatory vs. Voluntary", "Central Registration", "Cancellation & BIN"])

# --- HEADER ---
st.title("VAT Registration & Enlistment")
st.markdown(f"#### VAT & SD Act, 2012")
st.divider()

if menu == "Registration Thresholds":
    st.subheader("Turnover Thresholds (Updated 2026)")
    st.write("The classification of a business depends on its 'Annual Turnover'.")
    
    data = {
        "Annual Turnover Limit": ["Below Tk. 5,000,000", "Tk. 5,000,000 to 30,000,000", "Above Tk. 30,000,000"],
        "Requirement": ["Exempted", "Enlistment (Turnover Tax)", "VAT Registration"],
        "Tax Rate": ["0%", "4% Flat", "15% Standard / Reduced Rates"]
    }
    st.table(pd.DataFrame(data))
    
    st.info("💡 **Note:** 'Turnover' includes all taxable supplies but excludes the value of sale of capital assets.")

elif menu == "Mandatory vs. Voluntary":
    st.subheader("Types of Registration")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Mandatory Registration**")
        st.write("- If turnover exceeds the Tk. 3 Crore limit.")
        st.write("- Mandatory for all Importers & Exporters.")
        st.write("- Mandatory for certain services (e.g., Hotels, Consultants).")
        
    with col2:
        st.markdown("**Voluntary Registration**")
        st.write("- Available for businesses below the threshold.")
        st.write("- Benefit: Can claim Input Tax Credit (ITC).")
        st.write("- Condition: Must remain registered for at least 1 year.")

elif menu == "Central Registration":
    st.subheader("Unit vs. Central Registration (Section 5)")
    st.markdown("""
    For companies with multiple points of supply (like your factories and depots), the choice of registration is vital for MIS.
    """)
    
    st.markdown('<div class="compliance-card"><b>Unit Registration:</b> Each factory/branch has its own BIN and files its own returns.</div>', unsafe_allow_html=True)
    st.markdown('<div class="compliance-card"><b>Central Registration:</b> One BIN for all locations. Requires centralized accounting, record-keeping, and inventory management.</div>', unsafe_allow_html=True)
    
    st.success("For large manufacturers like Unilever, **Central Registration** usually simplifies the Input Tax Credit reconciliation across the supply chain.")

elif menu == "Cancellation & BIN":
    st.subheader("Business Identification Number (BIN)")
    st.write("The BIN is a unique 13-digit number issued by the NBR via the IVAS system.")
    
    st.error("**Cancellation Criteria:**")
    st.write("1. If the economic activity is closed down.")
    st.write("2. If the turnover falls below the enlistment threshold for two consecutive years.")
    st.write("3. If a person voluntarily registered fails to maintain turnover requirements.")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For factory finance, verify that all your vendors have a **Valid 13-digit BIN**. 
Payments made to a non-registered or invalid BIN entity for VDS-applicable services 
can lead to the disallowance of expenses during your corporate tax assessment.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Registration Module © 2026</center>", unsafe_allow_html=True)