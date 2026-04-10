import streamlit as st

# No st.set_page_config() here as it's assumed to be in your main Homepage file

# --- LEVEL 5 HEADER ---
st.markdown("## ⚙️ Level 5: Automation")
st.markdown("#### *Scaling efficiency by eliminating manual and repetitive tasks.*")

# --- SECTION 1: THE CORE GOAL ---
st.markdown("---")
st.markdown("### 🚀 1. Why Automate?")
st.write(
    "Automation is the final stage of the data maturity curve. It allows finance "
    "professionals to shift their focus from 'data preparation' to 'strategic decision-making'."
)

col1, col2 = st.columns(2)
with col1:
    st.info("""
    **Key Objectives:**
    * Enable automation of routine reporting.
    * Increase efficiency and reduce human error.
    * Standardize analytical tasks across the function.
    """)

with col2:
    st.info("""
    **Primary Benefits:**
    * **Time Savings:** Reclaim hours spent on manual data cleaning.
    * **Accuracy:** Ensure consistent logic every time a report runs.
    * **Scalability:** Handle growing data volumes without extra effort.
    """)

# --- SECTION 2: AUTOMATION TOOLS ---
st.markdown("---")
st.markdown("### 🛠️ 2. Automation Toolkit")
st.write("We focus on two primary paths for automation depending on the complexity of the task:")

c1, c2 = st.columns(2)

with c1:
    st.markdown("##### **Excel Automation (VBA/Power Query)**")
    st.markdown("""
    * **Macros:** Recording and writing VBA scripts for repetitive formatting.
    * **Power Query:** Automating the 'Extract, Transform, Load' (ETL) process within Excel.
    * **Best For:** Standardized monthly templates.
    """)

with c2:
    st.markdown("##### **Python Automation**")
    st.markdown("""
    * **Pandas Scripting:** Automating complex data cleaning across multiple files.
    * **API Integration:** Pulling data automatically from ERP systems or web sources.
    * **Scheduling:** Setting scripts to run at specific times (e.g., every Monday morning).
    """)

# --- SECTION 3: AUTOMATION WORKFLOW ---
st.markdown("---")
st.markdown("### 🔄 3. Identifying Automation Opportunities")
st.write("Use this simple framework to decide what to automate first:")

st.markdown("""
1. **Frequency:** Is this task done daily or weekly?
2. **Rule-Based:** Does the task follow a logical, consistent set of steps?
3. **Data-Heavy:** Does it involve high volumes of data entry or movement?
4. **Prone to Error:** Is the task repetitive enough that human mistakes are common?
""")

# --- SUMMARY OF THE JOURNEY ---
st.markdown("---")
st.success("""
**Congratulations!** You have reached the final level of the Data Analytics Mastery program. 
By combining the context of **Level 1**, the techniques of **Level 2**, the visuals of **Level 3**, 
the predictions of **Level 4**, and the speed of **Level 5**, you are now a fully data-literate 
finance professional.
""")

# --- FINAL BUTTON ---
if st.button("🎓 Complete Training"):
    st.balloons()
    st.write("Training Completed Successfully! You are ready to drive strategic value.")