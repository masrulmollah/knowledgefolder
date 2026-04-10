import streamlit as st

# No st.set_page_config() here as it's assumed to be in your main Homepage file

# --- LEVEL 2 HEADER ---
st.markdown("## ⚖️ Level 2: Data Analysis")
st.markdown("#### *Transforming raw data into strategic business insights.*")

# --- SECTION 1: THE ANALYSIS PROCESS ---
st.markdown("---")
st.markdown("### 📋 1. Defining the Purpose")
st.write(
    "Before diving into the data, a Finance Manager must define the objective. "
    "This ensures the analysis remains relevant to the business problem."
)

col1, col2 = st.columns(2)
with col1:
    st.info("""
    **Key Questions:**
    * Why are we doing this analysis?
    * What business problem are we solving?
    * Who is the intended audience?
    """)

with col2:
    st.info("""
    **Desired Outcomes:**
    * Executive Summary
    * Clear Findings
    * Actionable Recommendations
    """)

# --- SECTION 2: DATA ANALYSIS TECHNIQUES ---
st.markdown("---")
st.markdown("### 🛠️ 2. Analysis Techniques")
st.write("Based on the objective, choose the appropriate technique to 'slice and dice' the data:")

tab1, tab2, tab3 = st.tabs(["Comparative Analysis", "Impact & Variance", "Forward Looking"])

with tab1:
    st.markdown("#### Comparative & Trend Analysis")
    st.markdown("""
    * **Slicing and Dicing:** Filtering data into granular subsets (e.g., specific product categories or regions).
    * **Trend Analysis:** Comparing current performance against historical data (e.g., Year-to-Date vs. Last Year).
    * **Benchmarking:** Comparing performance against similar units or industry best practices.
    """)

with tab2:
    st.markdown("#### Variance & Impact Analysis")
    st.markdown("""
    * **Variance Analysis:** Dissecting deviations from expected performance (Price, Volume, or Mix variances).
    * **Impact Analysis:** Quantifying how specific factors affect KPIs like Gross Profit or Turnover.
    * **Driver Analysis:** Drilling down into components (Units, Rates, etc.) influencing KPIs.
    """)

with tab3:
    st.markdown("#### Predictive & Forward Looking")
    st.markdown("""
    * **Sensitivity Analysis:** Evaluating how changes in input variables (e.g., raw material price) affect the outcome.
    * **Scenario Analysis:** Exploring Best-Case, Base-Case, and Worst-Case outcomes.
    * **Performance Tracking:** Monitoring run rates to measure progress against end-of-year targets.
    """)

# --- SECTION 3: THE DEEP DIVE ---
st.markdown("---")
st.markdown("### 🔍 3. Execution (The Deep Dive)")
st.write(
    "In this phase, you use your technical tools (Excel/Python) to identify root causes. "
    "You are looking for the 'Story' behind the numbers."
)

st.success("""
**Pro Tip:** Always validate your findings with the 'Field Reality.' If the data shows a spike in utility costs, 
correlate it with machine loading hours or maintenance logs identified in Level 1.
""")

# --- NAVIGATION FOOTER ---
st.markdown("---")
st.write("Ready to present these insights visually?")
if st.button("Proceed to Level 3: Visualization"):
    st.write("Navigate to the Level 3 page in the sidebar.")