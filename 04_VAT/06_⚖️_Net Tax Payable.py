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
    
    .formula-box {
        background-color: #f0f4f8;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #d1d5db;
        text-align: center;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Assessment Tools")
st.sidebar.info("This module covers the self-assessment of Net Tax under Section 45.")

# --- HEADER ---
st.title("Assessment of Net Tax Payable")
st.markdown("#### Section 45 | VAT & SD Act, 2012")
st.divider()

# --- THE CALCULATION FORMULA ---
st.subheader("The Statutory Formula")
st.markdown("""
Every registered person must calculate the net tax payable for each tax period (month) 
using the following mechanical calculation:
""")

st.markdown("""
<div class="formula-box">
    Net Tax = (Output Tax + SD + Increasing Adjustments) <br>
    — <br>
    (Input Tax Credit + Decreasing Adjustments)
</div>
""", unsafe_allow_html=True)

# --- BREAKDOWN SECTIONS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ➕ Additions to Liability")
    with st.expander("Output Tax & SD"):
        st.write("Total VAT and Supplementary Duty charged on your sales/supplies during the month.")
    with st.expander("Increasing Adjustments"):
        st.write("""
        - VAT deducted at source (VDS) from your payments by buyers.
        - Adjustments for annual re-calculations.
        - Interest, penalties, or fines payable.
        """)

with col2:
    st.markdown("### ➖ Reductions to Liability")
    with st.expander("Input Tax Credit (ITC)"):
        st.write("VAT paid on raw materials, services, and utilities (requires Mushak-6.3).")
    with st.expander("Decreasing Adjustments"):
        st.write("""
        - VAT on goods returned by you to suppliers.
        - VDS you deducted from your suppliers and deposited.
        - Overpayments from previous periods.
        """)

st.divider()

# --- PAYMENT & DEADLINE ---
st.subheader("🗓️ Payment and Filing Deadline")
st.markdown("""
The Net Tax determined above must be paid into the Government Treasury through 
the designated bank (e.g., Bangladesh Bank or Sonali Bank) or via e-payment.
""")

st.warning("**Deadline:** The tax must be paid and the return (**Mushak-9.1**) must be filed by the **15th of the following month**.")

st.error("""
**Note on Failure:** If the 15th falls on a public holiday, the return must be filed on the 
preceding working day. Failure to file on time attracts a penalty of **Tk. 10,000**.
""")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** For factory accounting, ensure that your **Increasing Adjustments** (like VDS deducted from your company) are supported by a **Mushak-6.6** from your customers. 
Without this certificate, you cannot legally decrease your liability, leading to a double-taxation impact 
on your cash flow.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | VAT Assessment Module © 2026</center>", unsafe_allow_html=True)