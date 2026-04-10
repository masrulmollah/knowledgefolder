import streamlit as st

# No st.set_page_config() here as it's assumed to be in your main Homepage file

# --- LEVEL 3 HEADER ---
st.markdown("## 📊 Level 3: Data Visualization")
st.markdown("#### *Turning data into stories that drive decisions.*")

# --- SECTION 1: THE CORE OBJECTIVE ---
st.markdown("---")
st.markdown("### 🎯 1. Purpose of Visualization")
st.write(
    "Visualization is not just about making charts; it is about communication. "
    "A good visual should answer a business question at a glance."
)

col1, col2 = st.columns(2)
with col1:
    st.info("""
    **Key Principles:**
    * **Know your Audience:** Is it for a Factory Manager or the CFO?
    * **Simplicity:** Remove clutter that doesn't add value.
    * **Clarity:** Ensure labels and scales are easy to read.
    """)

with col2:
    st.info("""
    **Tools of the Trade:**
    * **Power BI:** For interactive dashboards and real-time tracking.
    * **PowerPoint:** For executive presentations and storytelling.
    * **Excel Charts:** For quick, ad-hoc analysis.
    """)

# --- SECTION 2: SELECTING THE RIGHT VISUAL ---
st.markdown("---")
st.markdown("### 📈 2. Choosing the Right Chart Type")
st.write("Selecting the wrong visual can lead to misinterpretation. Follow these standards:")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("##### **Trend & Time**")
    st.markdown("""
    * **Line Charts:** Best for showing trends over months/years.
    * **Area Charts:** To show changes in totals over time.
    """)

with c2:
    st.markdown("##### **Comparison**")
    st.markdown("""
    * **Bar Charts:** Comparing different categories (e.g., Cost by Department).
    * **Waterfall Charts:** Great for showing bridge analysis (e.g., LY vs CY).
    """)

with c3:
    st.markdown("##### **Composition**")
    st.markdown("""
    * **Tree Maps:** Showing relative sizes of components.
    * **Donut Charts:** Showing proportions of a whole (use sparingly).
    """)

# --- SECTION 3: STORYTELLING WITH DATA ---
st.markdown("---")
st.markdown("### 🗣️ 3. Data Storytelling")
st.write(
    "A visualization is complete when it provides **Context** and **Action**. "
    "Don't just show 'Utility Cost is Up'; show 'Utility Cost is Up due to Machine Loading Hours'."
)

st.success("""
**Visualization Checklist:**
1. Does this visual have a clear title?
2. Is the most important information highlighted?
3. Can the audience reach a conclusion within 5 seconds?
4. Is there a clear recommendation or next step?
""")

# --- NAVIGATION FOOTER ---
st.markdown("---")
st.write("Ready to advance to advanced modeling and prediction?")
if st.button("Proceed to Level 4: Machine Learning"):
    st.write("Navigate to the Level 4 page in the sidebar.")