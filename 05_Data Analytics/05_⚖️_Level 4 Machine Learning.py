import streamlit as st

# No st.set_page_config() here as it's assumed to be in your main Homepage file

# --- LEVEL 4 HEADER ---
st.markdown("## 🤖 Level 4: Machine Learning (ML)")
st.markdown("#### *Leveraging Python to predict future trends and automate complex decisions.*")

# --- SECTION 1: INTRODUCTION TO ML IN FINANCE ---
st.markdown("---")
st.markdown("### 🧠 1. Why Machine Learning for Finance?")
st.write(
    "Machine Learning allows finance professionals to handle large datasets that are too "
    "complex for traditional Excel models. It helps in finding hidden patterns and "
    "making highly accurate forecasts."
)

col1, col2 = st.columns(2)
with col1:
    st.info("""
    **Core Objectives:**
    * Understand ML foundations and financial use cases.
    * Learn to build models using **Python**.
    * Transition from descriptive to predictive analytics.
    """)

with col2:
    st.info("""
    **Key Financial Applications:**
    * **Forecasting:** Predicting future sales or commodity prices.
    * **Risk Management:** Detecting anomalies or potential fraud.
    * **Optimization:** Identifying the best mix of resources for cost savings.
    """)

# --- SECTION 2: KEY MODELS & TECHNIQUES ---
st.markdown("---")
st.markdown("### 📊 2. Essential ML Models")
st.write("In this level, we focus on three primary types of modeling used in financial environments:")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("##### **Regression**")
    st.markdown("""
    * **Linear Regression:** Modeling the relationship between variables (e.g., how Volume affects Total Cost).
    * **Use Case:** Predicting Spend based on historical drivers.
    """)

with c2:
    st.markdown("##### **Classification**")
    st.markdown("""
    * **Decision Trees:** Categorizing data into branches to reach a conclusion.
    * **Use Case:** Identifying whether a transaction is 'High Risk' or 'Low Risk'.
    """)

with c3:
    st.markdown("##### **Time Series**")
    st.markdown("""
    * **Prophet / ARIMA:** Specialized models for data that changes over time.
    * **Use Case:** Monthly budget forecasting and trend projection.
    """)

# --- SECTION 3: THE PYTHON WORKFLOW ---
st.markdown("---")
st.markdown("### 🐍 3. The Technical Workflow")
st.write("The process of building an ML model follows a structured path:")

st.steps = [
    "**Data Collection:** Gathering historical data from SAP, TM1, or Excel.",
    "**Pre-processing:** Cleaning and normalizing data using Python (Pandas/NumPy).",
    "**Model Training:** Teaching the algorithm using historical patterns.",
    "**Evaluation:** Testing accuracy against real-world 'out-of-sample' data.",
    "**Deployment:** Using the model to generate future insights for the business."
]

for step in st.steps:
    st.write(f"🔹 {step}")

# --- NAVIGATION FOOTER ---
st.markdown("---")
st.write("Ready to scale your insights through automation?")
if st.button("Proceed to Level 5: Automation"):
    st.write("Navigate to the Level 5 page in the sidebar.")