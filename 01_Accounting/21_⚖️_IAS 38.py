import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 38: Intangible Assets")
st.write("This standard outlines the accounting treatment for intangible assets that are not dealt with specifically in another standard. It requires an entity to recognize an intangible asset only if specific criteria are met.")

# --- THE DEFINITION ---
st.info("**Definition:** An intangible asset is an identifiable non-monetary asset without physical substance. It must be **identifiable**, **controlled** by the entity, and provide **future economic benefits**.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Recognition & Research", "Development Phase", "Measurement & Life"])

with tab1:
    st.markdown("#### 1. Recognition Criteria")
    st.write("An intangible asset shall be recognized if, and only if:")
    st.success("""
    1. It is probable that the expected **future economic benefits** will flow to the entity.
    2. The **cost** of the asset can be measured reliably.
    """)
    
    st.divider()
    st.error("**The Research Phase**")
    st.write("No intangible asset arising from research shall be recognized. Expenditure on research shall be recognized as an **expense** when it is incurred.")
    st.caption("Examples: Activities aimed at obtaining new knowledge or searching for alternatives for materials/products.")

with tab2:
    st.markdown("#### 2. The Development Phase (PIRATE)")
    st.write("An intangible asset arising from development shall be **capitalized** if an entity can demonstrate all of the following (the 'PIRATE' criteria):")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**P** - Probable future economic benefits.")
        st.info("**I** - Intention to complete and use/sell.")
        st.info("**R** - Resources (technical/financial) available.")
    with col2:
        st.info("**A** - Ability to use or sell.")
        st.info("**T** - Technical feasibility of completion.")
        st.info("**E** - Expenditure can be measured reliably.")

    

    st.warning("**Internally Generated Brands:** Internally generated brands, mastheads, publishing titles, and customer lists shall NOT be recognized as intangible assets.")

with tab3:
    st.markdown("#### 3. Useful Life & Amortization")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Finite Useful Life**")
        st.write("Amortized over its useful life. The residual value is usually assumed to be zero.")
    with c2:
        st.markdown("**Indefinite Useful Life**")
        st.write("Not amortized. Instead, it must be tested for **impairment annually** (under IAS 36).")

    st.divider()
    with st.expander("📊 Measurement After Recognition"):
        st.write("**Cost Model:** Cost less any accumulated amortization and impairment losses.")
        st.write("**Revaluation Model:** Fair value at the date of revaluation less subsequent amortization/impairment.")
        st.caption("Note: Revaluation is only allowed if there is an active market for the asset (rare for intangibles).")

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 38")