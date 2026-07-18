"""Module 1: Linear Regression - Predicting Stock/Portfolio Returns"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

st.set_page_config(page_title="Linear Regression - Stock Returns", page_icon="📈", layout="wide")

st.title("📈 Module 1: Linear Regression")
st.subheader("Predicting stock/portfolio returns from market factors")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    Linear regression fits: **Return = β₀ + β₁·Factor₁ + β₂·Factor₂ + ... + ε**

    In finance this is the backbone of **factor models** (e.g. Fama-French):
    you explain a stock's return using market return, size, value, momentum,
    interest-rate changes, etc. The coefficients (β) tell you the stock's
    *sensitivity* to each factor — exactly what "beta" means in CAPM.

    - **R²** = how much of the return variation the factors explain
    - **Coefficients** = economic sensitivities (interpretable!)
    - **Residuals** = the part of the return factors *can't* explain (alpha + noise)
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")

data_source = st.radio("Choose data source", ["Synthetic market data", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=750, seed=42):
    rng = np.random.default_rng(seed)
    market_return = rng.normal(0.0004, 0.011, n)
    size_factor = rng.normal(0.0, 0.006, n)
    value_factor = rng.normal(0.0, 0.005, n)
    rate_change = rng.normal(0.0, 0.002, n)
    true_beta_market, true_beta_size, true_beta_value, true_beta_rate = 1.15, 0.35, -0.20, -0.8
    noise = rng.normal(0, 0.006, n)
    stock_return = (
        0.0002
        + true_beta_market * market_return
        + true_beta_size * size_factor
        + true_beta_value * value_factor
        + true_beta_rate * rate_change
        + noise
    )
    return pd.DataFrame(
        {
            "market_return": market_return,
            "size_factor": size_factor,
            "value_factor": value_factor,
            "rate_change": rate_change,
            "stock_return": stock_return,
        }
    )


if data_source == "Synthetic market data":
    n_points = st.slider("Number of trading days", 200, 2000, 750, 50)
    df = make_synthetic_data(n_points)
    st.caption("Synthetic daily factor returns + a stock return driven by them (with noise).")
else:
    uploaded = st.file_uploader("Upload CSV (numeric columns, last column = target return)", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

st.dataframe(df.head(10), use_container_width=True)

target_col = st.selectbox("Target column (what we're predicting)", df.columns, index=len(df.columns) - 1)
feature_cols = st.multiselect(
    "Feature columns (predictors)",
    [c for c in df.columns if c != target_col],
    default=[c for c in df.columns if c != target_col],
)

if not feature_cols:
    st.warning("Select at least one feature column.")
    st.stop()

# ------------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------------
st.header("2️⃣ Train the model")

test_size = st.slider("Test set size (%)", 10, 40, 20, 5) / 100

X = df[feature_cols].values
y = df[target_col].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

col1, col2, col3 = st.columns(3)
col1.metric("R² (test set)", f"{r2_score(y_test, y_pred):.3f}")
col2.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, y_pred)):.5f}")
col3.metric("MAE", f"{mean_absolute_error(y_test, y_pred):.5f}")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("3️⃣ See it work")

tab1, tab2, tab3 = st.tabs(["Predicted vs Actual", "Coefficients (sensitivities)", "Residuals"])

with tab1:
    fig = px.scatter(x=y_test, y=y_pred, labels={"x": "Actual return", "y": "Predicted return"},
                      title="Predicted vs Actual Returns")
    lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
    fig.add_trace(go.Scatter(x=lims, y=lims, mode="lines", name="Perfect fit", line=dict(dash="dash")))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    coef_df = pd.DataFrame({"Factor": feature_cols, "Coefficient (Beta)": model.coef_})
    coef_df = coef_df.sort_values("Coefficient (Beta)", key=abs, ascending=False)
    fig2 = px.bar(coef_df, x="Coefficient (Beta)", y="Factor", orientation="h",
                  title="Factor sensitivities (betas)")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption(f"Intercept (alpha): {model.intercept_:.5f}")

with tab3:
    residuals = y_test - y_pred
    fig3 = px.histogram(residuals, nbins=30, title="Residual distribution")
    st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------------------------
# TRY YOUR OWN SCENARIO
# ------------------------------------------------------------------
st.header("4️⃣ Modify the model — test a scenario")
st.caption("Plug in your own factor values and see the predicted return instantly.")

scenario_vals = {}
cols = st.columns(len(feature_cols))
for i, fc in enumerate(feature_cols):
    with cols[i]:
        scenario_vals[fc] = st.number_input(fc, value=float(np.round(df[fc].mean(), 5)), format="%.5f")

scenario_pred = model.predict([[scenario_vals[fc] for fc in feature_cols]])[0]
st.success(f"Predicted return for this scenario: **{scenario_pred:.4%}**")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
top_factor = coef_df.iloc[0]
st.markdown(
    f"""
- The model explains **{r2_score(y_test, y_pred)*100:.1f}%** of the variation in `{target_col}`.
- **`{top_factor['Factor']}`** has the largest impact on the return (coefficient = {top_factor['Coefficient (Beta)']:.3f}).
  A positive coefficient means the return moves *with* that factor; negative means it moves *against* it.
- If R² is low, it usually means important drivers are missing from your feature set, or the
  relationship isn't linear — worth testing Random Forest (Module 3) or XGBoost (Module 4) next.
"""
)
