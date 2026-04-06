import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IAS 19: Employee Benefits")
st.write("This standard prescribes the accounting and disclosure for employee benefits. It requires an entity to recognize a liability when an employee has provided service in exchange for employee benefits to be paid in the future.")

# --- THE PRINCIPLE ---
st.info("**Core Principle:** The cost of providing employee benefits should be recognized in the period in which the benefit is earned by the employee, rather than when it is paid.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["Short-term Benefits", "Post-Employment", "Other Long-term", "Termination"])

with tab1:
    st.markdown("#### 1. Short-term Employee Benefits")
    st.write("Benefits expected to be settled wholly before twelve months after the end of the reporting period.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**Examples**")
        st.markdown("""
        * Wages, salaries, and social security contributions.
        * Paid annual leave and sick leave.
        * Profit-sharing and bonuses.
        * Non-monetary benefits (e.g., medical care, housing, cars).
        """)
        
    with col2:
        st.info("**Accounting Treatment**")
        st.write("Recognize the undiscounted amount of short-term employee benefits expected to be paid in exchange for that service as a liability (accrued expense) and as an expense.")

with tab2:
    st.markdown("#### 2. Post-Employment Benefits")
    st.write("Formal or informal arrangements under which an entity provides benefits after the completion of employment.")

    

    c1, c2 = st.columns(2)
    
    with c1:
        st.warning("**Defined Contribution (DC)**")
        st.write("Entity pays fixed contributions into a separate fund. The entity has no legal or constructive obligation to pay further contributions.")
        st.caption("Expense = Contribution payable for the period.")

    with c2:
        st.error("**Defined Benefit (DB)**")
        st.write("The entity’s obligation is to provide the agreed benefits to current and former employees.")
        st.markdown("""
        * Actuarial risk and investment risk fall on the entity.
        * Requires actuarial assumptions to measure the obligation.
        """)

with tab3:
    st.markdown("#### 3. Other Long-term Benefits")
    st.write("Benefits not expected to be settled wholly within twelve months.")
    
    st.markdown("""
    * **Examples:** Long-service leave, jubilee benefits, long-term disability benefits.
    * **Measurement:** Similar to defined benefit plans, but the **re-measurements** are recognized in Profit or Loss (not OCI).
    """)

with tab4:
    st.markdown("#### 4. Termination Benefits")
    st.write("Employee benefits provided in exchange for the termination of an employee’s employment.")
    
    st.error("**Recognition Trigger**")
    st.write("An entity shall recognize a liability and expense for termination benefits at the **earlier** of:")
    st.markdown("""
    1. When the entity can no longer withdraw the offer of those benefits.
    2. When the entity recognizes costs for a restructuring (under IAS 37) that involves the payment of termination benefits.
    """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Accounting Standard 19")