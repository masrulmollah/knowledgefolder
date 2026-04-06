import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 26: Accounting and Reporting by Retirement Benefit Plans")
st.write("This standard is applied in the reports of retirement benefit plans where such reports are prepared. It regards a retirement benefit plan as a reporting entity separate from the employers of the participants in the plan.")

# --- THE REPORTING ENTITY ---
st.info("**Scope:** IAS 26 applies to both Defined Contribution and Defined Benefit plans. It complements IAS 19, which deals with the employer's cost of employee benefits.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["Defined Contribution Plans", "Defined Benefit Plans", "Valuation & Disclosures"])

with tab1:
    st.markdown("#### 1. Defined Contribution (DC) Plans")
    st.write("The report of a defined contribution plan shall contain a statement of net assets available for benefits and a description of the funding policy.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Core Objective**")
        st.write("To provide information about the plan and the performance of its investments.")
        
    with col2:
        st.info("**Report Contents**")
        st.markdown("""
        * Statement of net assets available for benefits.
        * Description of funding policy.
        * Summary of plan activities for the period.
        """)

with tab2:
    st.markdown("#### 2. Defined Benefit (DB) Plans")
    st.write("The report of a defined benefit plan shall contain either:")
    st.markdown("""
    * A statement showing net assets available for benefits, the actuarial present value of promised retirement benefits, and the resulting excess or deficit; **OR**
    * A statement of net assets available for benefits including either a note disclosing the actuarial present value or a reference to this information in an accompanying actuarial report.
    """)

    

    st.warning("**Measurement of Benefits**")
    st.write("""
    The actuarial present value of promised retirement benefits should be based on the benefits promised under the terms of the plan using **current salary levels** or **projected salary levels**, with disclosure of the basis used.
    """)

with tab3:
    st.markdown("#### 3. Asset Valuation & Disclosures")
    
    st.error("**Valuation of Plan Investments**")
    st.write("Retirement benefit plan investments shall be carried at **fair value**. In the case of marketable securities, fair value is market value.")
    
    st.divider()
    
    with st.expander("📝 Required Disclosures for All Plans"):
        st.markdown("""
        1. **Statement of Changes** in net assets available for benefits.
        2. **Summary** of significant accounting policies.
        3. **Description** of the plan and the effect of any changes in the plan during the period.
        4. **Investment Assets** categories and concentration risks.
        """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 26")