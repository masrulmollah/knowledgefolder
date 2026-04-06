import streamlit as st
import pandas as pd
import numpy as np

st.header("Linear Regression")
st.write("Welcome to the Linear Regression module.")

# Sample Logic
st.info("Formula: $Y = \beta_0 + \beta_1X + \epsilon$")

data = pd.DataFrame(np.random.randn(20, 2), columns=['X', 'Y'])
st.line_chart(data)