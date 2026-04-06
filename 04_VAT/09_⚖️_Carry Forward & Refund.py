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
    
    .refund-box {
        background-color: #f0fdfa;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #0d9488;
        margin-bottom: 15px;
    }
    .flow-step {
        font-weight: bold;
        color: #0d9488;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Refund Management")
st.sidebar.write("Sections 47-48: Managing Excess Credits.")

# --- HEADER ---
st.title("Carry Forward & VAT Refunds")
st.markdown("#### Sections 47-48 | VAT & SD Act, 2012")
st.divider()

# --- THE PROCESS FLOW ---
st.subheader("The Negative Net Amount Lifecycle")

st.markdown("""
<div class="refund-box">
    <span class="flow-step">Step 1: Detection</span><br>
    Your Input Tax Credit > Output Tax. The result is a Negative Net Amount.
</div>
<div class="refund-box">
    <span class="flow-step">Step 2: Carry Forward</span><br>
    The amount is carried forward to the next month as a 'Decreasing Adjustment'. This can continue for <b>6 consecutive tax periods</b>.
</div>
<div class="refund-box">
    <span class="flow-step">Step 3: Application for Refund</span><br>
    If a balance still remains after 6 months, you are eligible to apply for a cash refund via <b>Mushak-10.1</b>.
</div>
""", unsafe_allow_html=True)

# --- SPECIAL CONDITIONS ---
st.subheader("Special Categories & Thresholds")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✈️ Exporters")
    st.write("""
    Exporters (Zero-rated suppliers) do not have to wait 6 months. 
    They can apply for a refund at the end of **any tax period** because 
    their output tax is always zero.
    """)

with col2:
    st.markdown("### 📉 Thresholds")
    st.write("""
    If the negative net amount is less than **Tk. 50,000**, it must be 
    carried forward until it either exceeds this limit or the 
    business is cancelled.
    """)

st.divider()

# --- AUDIT & VERIFICATION ---
st.subheader("📋 Verification Process")
st.markdown("""
Upon receiving a refund application (Mushak-10.1), the Commissioner will:
* Verify the authenticity of the **Mushak-6.3** invoices.
* Ensure all banking channel requirements were met.
* Issue the refund within **3 months** of the application (subject to audit).
""")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** In a factory environment, large capital machinery imports 
often trigger a significant Negative Net Amount. Ensure your team tracks these 
specifically in the **Mushak-9.1** return. If you plan to apply for a refund, 
ensure your **Purchase Register (6.1)** and **Sales Register (6.2)** are perfectly 
reconciled, as a refund application almost always triggers a departmental audit.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Carry Forward & Refund Module © 2026</center>", unsafe_allow_html=True)