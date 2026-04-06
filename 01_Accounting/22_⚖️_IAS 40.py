import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 40: Investment Property")
st.write("This standard prescribes the accounting treatment for investment property and related disclosure requirements.")

# --- THE KEY DEFINITION ---
st.info("**Definition:** Investment property is property (land or a building—or part of a building—or both) held to earn **rentals** or for **capital appreciation** (or both), rather than for use in the production or supply of goods or services or for administrative purposes.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Scope & Recognition", "Measurement Models", "Transfers & Disposals"])

with tab1:
    st.markdown("#### 1. Scope: What is Investment Property?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Included**")
        st.markdown("""
        * Land held for long-term capital appreciation.
        * Land held for a currently undetermined future use.
        * A building owned by the entity and leased out under an operating lease.
        * A vacant building held to be leased out.
        """)
    with col2:
        st.error("**Excluded (Non-IAS 40)**")
        st.markdown("""
        * **Owner-occupied property** (IAS 16).
        * Property held for sale in the ordinary course of business (IAS 2).
        * Property being constructed for third parties (IFRS 15).
        """)

    st.divider()
    st.markdown("#### Recognition Criteria")
    st.write("Recognize as an asset only when it is probable that future economic benefits will flow to the entity and the cost can be measured reliably.")

with tab2:
    st.markdown("#### 2. Measurement After Recognition")
    st.write("An entity must choose either the **Fair Value Model** or the **Cost Model** for all of its investment property.")

    c1, c2 = st.columns(2)
    with c1:
        st.warning("**Fair Value Model**")
        st.markdown("""
        * Property is measured at **fair value** at each reporting date.
        * Gains or losses arising from changes in fair value are recognized in **Profit or Loss**.
        * **No depreciation** is charged.
        """)
    with c2:
        st.info("**Cost Model**")
        st.markdown("""
        * Follows the treatment in **IAS 16**.
        * Measured at cost less accumulated depreciation and impairment.
        * The fair value must still be **disclosed** in the notes.
        """)

    

with tab3:
    st.markdown("#### 3. Transfers & Disposals")
    st.write("Transfers to or from investment property shall be made when, and only when, there is a **change in use**.")
    
    with st.expander("🔄 Examples of Change in Use"):
        st.markdown("""
        * **Commencement of owner-occupation:** Transfer from Investment Property to PPE (IAS 16).
        * **Commencement of development with a view to sale:** Transfer from Investment Property to Inventory (IAS 2).
        * **End of owner-occupation:** Transfer from PPE to Investment Property.
        """)
        
    st.divider()
    st.error("**Disposals**")
    st.write("""
    An investment property shall be derecognized on disposal or when the investment property is permanently withdrawn from use and no future economic benefits are expected.
    Gains or losses are calculated as the difference between net disposal proceeds and the carrying amount.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 40")