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
    
    .audit-card {
        background-color: #f0f9ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #0369a1;
        margin-bottom: 12px;
    }
    .check-item {
        color: #0369a1;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Audit Readiness")
st.sidebar.info("Sections 90-94: The NBR's verification powers.")

# --- HEADER ---
st.title("Audit and Investigation")
st.markdown("#### Sections 90-94 | VAT & SD Act, 2012")
st.divider()

# --- 1. CORE POWERS ---
st.subheader("The Power of Verification")
st.markdown("""
The NBR uses audits to ensure that the 'Self-Assessment' system is working correctly. 
An audit can be routine, or it can be a 'deep dive' investigation based on intelligence.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="audit-card">
        <span class="check-item">Routine Audit</span><br>
        Selection based on risk parameters (e.g., high refund claims, low tax-to-turnover ratio).
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="audit-card">
        <span class="check-item">Intelligence Investigation</span><br>
        Unannounced visits triggered by specific reports of evasion or Mushak-6.3 forgery.
    </div>
    """, unsafe_allow_html=True)

# --- 2. AUDIT CHECKLIST ---
st.subheader("📋 Key Audit Focus Areas")
st.markdown("During a factory audit, the VAT officer will typically focus on:")

with st.expander("1. Input-Output Reconciliation"):
    st.write("""
    The auditor will verify if the raw materials purchased (Mushak-6.1) logically 
    match the finished goods sold (Mushak-6.2). Discrepancies here often suggest 
    'Under-invoicing' or 'Unrecorded Sales'.
    """)

with st.expander("2. Input Tax Credit (ITC) Verification"):
    st.write("""
    They will check the validity of your Mushak-6.3 documents and verify that 
    all payments above Tk. 100,000 were made through banking channels.
    """)

with st.expander("3. VDS Compliance"):
    st.write("""
    The auditor will verify if you have correctly withheld VAT from your 
    suppliers and if you have issued Mushak-6.6 certificates on time.
    """)

# --- 3. AUDIT CYCLE ---
st.subheader("🔄 The Audit Cycle")
st.markdown("""
1. **Notice:** Selection notice sent to the taxpayer.
2. **Field Visit:** Inspection of factory, stock, and records.
3. **Draft Report:** Discrepancies identified.
4. **Show Cause Notice (SCN):** Formal legal notice if evasion is suspected.
5. **Adjudication:** Final order by the Commissioner.
""")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For a Factory Lead, 'Stock Reconciliation' is the 
biggest audit risk. If your ERP shows 1,000 units of stock but your 
**Mushak-6.2** only accounts for 800, the NBR will assume the 200 units were 
sold without VAT and issue a demand for the tax, plus interest and 100% penalty. 
Conduct a 'Mock Audit' every quarter to ensure your physical stock matches your 
VAT registers.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Audit & Investigation Module © 2026</center>", unsafe_allow_html=True)