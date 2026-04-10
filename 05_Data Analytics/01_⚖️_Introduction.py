import streamlit as st

# We do not use st.set_page_config() here because it is already 
# called in your main 1_🤓_Homepage.py file.

# --- MAIN TITLE (Standardized Size) ---
st.markdown("## 🎓 Data Analytics Mastery: A Practical Guide")
st.markdown("##### *More Data - More Insights - Better Confidence...*")

# --- SUMMARY SECTION ---
st.markdown("---")
st.markdown("### 📖 Program Summary")
st.write(
    "The purpose of this data analysis training program is to empower finance professionals "
    "and aspiring finance professionals with the essential data analysis soft skills and "
    "technical proficiencies needed to excel in their roles. This training provides "
    "a logical progression and a practical guide to improve your data analysis skills, "
    "helping you achieve your targets and deliver the best for your organization."
)

# --- OBJECTIVES SECTION ---
st.markdown("---")
st.markdown("### 🎯 Training Objectives")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🧠 Enhance Soft Skills")
    st.markdown("""
    * **Understand Financial Data:** Develop a strong grasp of data structures.
    * **Strategic Thinking:** Align data analysis with business objectives.
    * **Communication:** Refine the ability to share insights clearly.
    * **Process Management:** Establish robust KPI setting and performance management.
    """)

with col2:
    st.markdown("#### 🛠️ Develop Technical Skills")
    st.markdown("""
    * **Tool Proficiency:** Master tools like **Excel** and **Python**.
    * **Visualization:** Learn techniques using **PowerPoint** and **Power BI**.
    * **Automation:** Enable the automation of routine reporting for increased efficiency.
    """)

# --- BENEFITS SECTION ---
st.markdown("---")
st.markdown("### 🚀 Program Benefits")

# Using a standard list for better readability
st.markdown("""
* **Strategic Contribution:** Drive value directly from your work area.
* **Better Decision Making:** Help the company take correct financial and strategic decisions.
* **Transformation:** Become a data-literate professional who can leverage data confidently.
* **Efficiency:** Reduce manual effort through modern technical proficiencies.
""")

# --- PROGRAM STRUCTURE ---
st.markdown("---")
st.markdown("### 📂 Curriculum Overview")
st.write("The program is structured into five levels to ensure a comprehensive learning journey:")

# Using a standard bullet point list instead of large metrics or buttons
st.markdown("""
1. **Level 1:** Know Your Data
2. **Level 2:** Data Analysis
3. **Level 3:** Visualization
4. **Level 4:** Machine Learning
5. **Level 5:** Automation
""")