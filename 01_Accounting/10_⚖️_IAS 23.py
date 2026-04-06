import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 23: Borrowing Costs")
st.write("This standard prescribes the accounting treatment for borrowing costs, which are interest and other costs that an entity incurs in connection with the borrowing of funds.")

# --- THE CAPITALIZATION RULE ---
st.error("**Core Principle:** Borrowing costs that are directly attributable to the acquisition, construction, or production of a **qualifying asset** form part of the cost of that asset. Other borrowing costs are recognized as an expense.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Qualifying Assets", "Capitalization Process", "Cessation & Disclosure"])

with tab1:
    st.markdown("#### 1. What is a Qualifying Asset?")
    st.write("An asset that necessarily takes a **substantial period of time** to get ready for its intended use or sale.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Examples**")
        st.markdown("""
        * **Manufacturing plants** (Factories).
        * Power generation facilities.
        * Intangible assets (e.g., major software development).
        * Investment properties.
        """)
        
    with col2:
        st.warning("**Non-Qualifying**")
        st.markdown("""
        * Assets ready for use/sale when acquired.
        * Inventories produced over a short period.
        * Assets measured at fair value (e.g., biological assets).
        """)

with tab2:
    st.markdown("#### 2. The Capitalization Period")
    st.write("Capitalization should occur when all three of the following conditions are met:")
    
    st.info("""
    1. **Expenditures** for the asset are being incurred.
    2. **Borrowing costs** are being incurred.
    3. **Activities** necessary to prepare the asset are in progress.
    """)

    

    st.markdown("#### Suspension of Capitalization")
    st.write("Capitalization shall be suspended during extended periods in which **active development is interrupted** (e.g., a strike or legal dispute stops construction).")

with tab3:
    st.markdown("#### 3. Calculation & Cessation")
    
    with st.expander("📊 Specific vs. General Borrowing"):
        st.write("**Specific Borrowing:** The actual borrowing costs incurred on that loan, less any investment income on the temporary investment of those borrowings.")
        st.write("**General Borrowing:** Apply a **capitalization rate** (weighted average of borrowing costs) to the expenditures on that asset.")
        
    with st.expander("🛑 When to Stop?"):
        st.write("An entity shall cease capitalizing borrowing costs when **substantially all the activities** necessary to prepare the qualifying asset for its intended use or sale are complete.")

    st.divider()
    st.markdown("#### 4. Required Disclosures")
    st.markdown("""
    1. The **amount** of borrowing costs capitalized during the period.
    2. The **capitalization rate** used to determine the amount of borrowing costs eligible for capitalization.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 23")