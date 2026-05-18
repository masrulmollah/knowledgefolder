import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 10: Financial Analytics",
        page_icon="🤖",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("🤖 Module 10: Introduction to Financial Analytics & ML")
st.markdown("""
Welcome to the final frontier. In this module, we move beyond simple sums and pivots. We use **Machine Learning** to find relationships between variables and predict future financial outcomes.
""")

st.divider()

# --- SECTION 1: PREDICTIVE MODELING SIMULATION ---
st.header("1. Cost Driver Analysis (Linear Regression)")
st.write("""
In a factory environment, costs often vary with production volume. 
Let's build a model to find the **Variable Cost per Unit** and the **Fixed Cost**.
""")

# Generate synthetic historical data
np.random.seed(42)
volume = np.random.randint(1000, 5000, 20)
# Formula: Total Cost = 5000 (Fixed) + 2.5 * Volume + Noise
costs = 5000 + (2.5 * volume) + np.random.normal(0, 500, 20)

df_factory = pd.DataFrame({"Volume": volume, "Total_Cost": costs})

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Historical Data")
    st.dataframe(df_factory.sort_values("Volume"), hide_index=True)

with col2:
    st.subheader("Training the Model")
    # Prepare the data for Scikit-Learn
    X = df_factory[['Volume']]
    y = df_factory['Total_Cost']
    
    model = LinearRegression()
    model.fit(X, y)
    
    fixed_cost = model.intercept_
    variable_cost = model.coef_[0]
    
    st.success("Model Trained Successfully!")
    st.metric("Estimated Fixed Cost", f"${fixed_cost:,.2f}")
    st.metric("Estimated Variable Cost/Unit", f"${variable_cost:,.2f}")

st.divider()

# --- SECTION 2: THE FORECASTER ---
st.header("2. Budget Forecaster")
st.write("Now, use your model to predict next month's total cost based on planned production volume.")

planned_vol = st.number_input("Enter Planned Production Volume for Next Month:", value=6000)
predicted_cost = model.predict([[planned_vol]])[0]

st.info(f"💡 Based on historical patterns, your predicted total cost for **{planned_vol:,} units** is **${predicted_cost:,.2f}**.")

# Visualization
df_factory['Prediction'] = model.predict(X)
fig = px.scatter(df_factory, x="Volume", y="Total_Cost", trendline="ols", 
                 title="Cost Correlation & Regression Line")
st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- SECTION 3: THE FINAL STEP - STREAMLIT APPS ---
st.header("3. Turning Code into Applications")
st.write("""
You have completed the syllabus! The final step in your journey is what you are doing right now: **Streamlit**.
Streamlit allows you to take your Python scripts and turn them into interactive web applications for your team.
""")

st.code("""
# The final workflow:
1. Data Cleaning (Pandas)
2. Calculation (Functions)
3. Prediction (Machine Learning)
4. Presentation (Streamlit Dashboard)
""", language="python")

st.divider()

# --- FINAL REFRESHER QUIZ ---
st.header("🧠 Final Knowledge Check")

q_final = st.radio(
    "Which Machine Learning model is most commonly used to predict a continuous numerical value (like next month's expense)?",
    ["Classification", "Linear Regression", "Clustering"]
)

if st.button("Complete Module 10"):
    if q_final == "Linear Regression":
        st.balloons()
        st.success("🏆 **Congratulations!** You have completed the Python Programming for Finance series.")
    else:
        st.warning("Almost there! Regression is used for predicting numbers. You're ready to review the modules!")

st.markdown("---")
st.caption("Knowledge Folder | Module 10: Financial Analytics & ML | End of Series")