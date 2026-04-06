import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 2: Inventories")
st.write("This standard prescribes the accounting treatment for inventories, focusing on the amount of cost to be recognized as an asset and carried forward until the related revenues are recognized.")

# --- MEASUREMENT PRINCIPLE ---
st.error("**Core Rule:** Inventories shall be measured at the **lower of Cost and Net Realizable Value (NRV).**")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Cost Measurement", "NRV & Write-downs", "Cost Formulas"])

with tab1:
    st.markdown("#### What is Included in Cost?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Included Costs**")
        st.markdown("""
        * **Purchase Costs:** Price, import duties, transport, and handling.
        * **Conversion Costs:** Direct labor and fixed/variable production overheads.
        * **Other Costs:** Only if incurred in bringing inventories to their present location/condition.
        """)
        
    with col2:
        st.warning("**Excluded Costs**")
        st.markdown("""
        * **Abnormal Waste:** Wasted materials, labor, or other production costs.
        * **Storage Costs:** Unless necessary for the production process.
        * **Administrative Overheads:** That do not contribute to location/condition.
        * **Selling Costs:** Marketing and distribution.
        """)

with tab2:
    st.markdown("#### Net Realizable Value (NRV)")
    st.write("**NRV Definition:** Estimated selling price in the ordinary course of business less the estimated costs of completion and the estimated costs necessary to make the sale.")

    

    st.info("**The Write-down Rule**")
    st.write("""
    If Cost > NRV, the inventory must be written down to NRV. 
    The amount of any write-down is recognized as an **expense** in the period the write-down occurs.
    """)
    
    with st.expander("📝 Example Calculation"):
        st.write("""
        * **Cost of Item:** $100
        * **Estimated Selling Price:** $110
        * **Cost to Sell:** $15
        * **NRV:** $110 - $15 = $95
        * **Result:** Value at **$95** (Write-down of $5 recognized in P&L).
        """)

with tab3:
    st.markdown("#### Cost Formulas")
    st.write("For items that are not ordinarily interchangeable, specific identification is used. For all others, use:")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.info("**FIFO (First-In, First-Out)**")
        st.write("Assumes that the items of inventory that were purchased or produced first are sold first.")
        
    with c2:
        st.info("**Weighted Average Cost**")
        st.write("The cost of each item is determined from the weighted average of the cost of similar items at the beginning of a period and the cost of similar items purchased/produced during the period.")

    st.error("⚠️ **Note:** LIFO (Last-In, First-Out) is **NOT** permitted under IAS 2.")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 2")