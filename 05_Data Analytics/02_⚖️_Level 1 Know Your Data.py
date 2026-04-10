import streamlit as st

# No st.set_page_config() here as it's assumed to be in your main Homepage file

# --- LEVEL 1 HEADER ---
st.markdown("## 📂 Level 1: Know Your Data")
st.markdown("#### *The foundation of impactful data analysis is a deep understanding of the context.*")

# --- SECTION 1: INDUSTRY & COMPANY CONTEXT ---
st.markdown("---")
st.markdown("### 🏢 1. Industry & Company Context")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Industry Overview")
    st.markdown("""
    * **Key Players:** Identifying major competitors in the FMCG sector.
    * **Market Trends:** Understanding current trends and challenges[cite: 10].
    * **Growth Areas:** Spotting opportunities for innovation[cite: 11].
    * **Regulatory Landscape:** Navigating compliance and tax requirements[cite: 11, 16].
    """)

with col2:
    st.markdown("#### Company Specific (Unilever Bangladesh)")
    st.markdown("""
    * **Business Model:** Operating in Skin Cleansing, Laundry, Skin Care, and Hair Care[cite: 12, 16].
    * **Strategic Goals:** Increasing market share and margin through raw material import and sales via distributors[cite: 13, 16].
    * **Data Culture:** Heavy reliance on data analytics and ERP systems like **SAP**[cite: 14, 16].
    """)

# --- SECTION 2: ROLE & FUNCTION ---
st.markdown("---")
st.markdown("### 👤 2. Role and Function")
st.write(
    "As a **Factory Finance Manager**, your role is to ensure cost governance and identify "
    "optimization opportunities to help the company make right financial decisions."
)

col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Key Responsibilities")
    st.markdown("""
    * **Tasks:** Data cleaning, cost accounting, reporting, and visualization[cite: 17, 20].
    * **Metrics:** Performance is measured by data accuracy, insights generated, and business impact[cite: 18].
    """)

with col4:
    st.markdown("#### Team & Tools")
    st.markdown("""
    * **Collaboration:** Part of the total finance team, working closely with Logistics and Procurement[cite: 26].
    * **Infrastructure:** Using **TM1** for MIS and sharing reports via **Excel** or **Power BI**[cite: 28].
    """)

# --- SECTION 3: DATA & VARIABLES ---
st.markdown("---")
st.markdown("### 📊 3. Data and Variables")

st.markdown("#### Factory Cost Data Breakdown")
st.write(
    "Data is typically analyzed on a **monthly basis** and measured as **cost per ton**. "
    "Key data points include labor, utility, and repair costs[cite: 35]."
)

st.info("""
**Key Variable: Volume** Volume is a primary variable. As volume increases, cost lines like labor and utility 
increase to a certain extent.
""")

# --- SECTION 4: FACTORS & DRIVERS ---
st.markdown("---")
st.markdown("### ⚙️ 4. Factors and Drivers")
st.write("Understanding what truly drives your end data is critical for controllable cost management[cite: 37, 38].")

st.markdown("""
* **Repair & Maintenance:** Primarily driven by machine breakdowns.
* **Utility Costs:** Dependent on steam/electricity requirements and total **loading hours** of the machines.
* **Control:** Analysis must distinguish between **controllable factors** and uncontrollable market shifts[cite: 38].
""")

st.success("Level 1 complete! You now have the context needed to move to Level 2: Data Analysis.")