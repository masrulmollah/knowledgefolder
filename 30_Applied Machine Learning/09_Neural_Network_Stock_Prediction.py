"""Module 8: Neural Network - Sequence-Based Stock Price Prediction"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

st.set_page_config(page_title="Neural Network - Stock Prediction", page_icon="🧠", layout="wide")

st.title("🧠 Module 8: Neural Network for Stock Prediction")
st.subheader("A sliding-window feedforward network — the intuition behind LSTMs, without the heavy setup")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    Deep learning models for price prediction (LSTM, GRU, Transformers) work
    by feeding the model a **window of past prices** and asking it to predict
    the next value. This lab uses a Multi-Layer Perceptron (MLP) with exactly
    that setup — same idea, lighter to run in-browser than a full LSTM.

    Key neural-network concepts you'll tune here map directly to any deep
    learning model you'd build later in TensorFlow/PyTorch:
    - **Hidden layers / neurons** = model capacity
    - **Learning rate** = how big a step the model takes each update
    - **Epochs (iterations)** = how long it trains
    - **Lookback window** = how much history the model sees per prediction
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic price series", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=800, seed=17):
    rng = np.random.default_rng(seed)
    returns = rng.normal(0.0004, 0.013, n)
    for i in range(1, n):
        returns[i] += 0.2 * returns[i - 1]  # momentum pattern a NN can learn
    price = 100 * np.exp(np.cumsum(returns))
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n, freq="B")
    return pd.DataFrame({"date": dates, "price": price})


if data_source == "Synthetic price series":
    n_points = st.slider("Number of trading days", 200, 2000, 800, 50)
    df = make_synthetic_data(n_points)
else:
    uploaded = st.file_uploader("Upload CSV with a date column and a price column", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

date_col = st.selectbox("Date column", df.columns, index=0)
price_col = st.selectbox("Price column", [c for c in df.columns if c != date_col],
                          index=len(df.columns) - 2 if len(df.columns) > 1 else 0)
df = df[[date_col, price_col]].dropna().rename(columns={date_col: "date", price_col: "price"})
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

st.plotly_chart(go.Figure(go.Scatter(x=df["date"], y=df["price"], mode="lines")).update_layout(
    title="Price history"), use_container_width=True)

# ------------------------------------------------------------------
# WINDOWING
# ------------------------------------------------------------------
st.header("2️⃣ Build sliding-window features")
lookback = st.slider("Lookback window (days of history per prediction)", 5, 60, 20, 5)

prices = df["price"].values
returns = np.diff(np.log(prices))  # model returns, not raw price levels

X, y = [], []
for i in range(lookback, len(returns)):
    X.append(returns[i - lookback:i])
    y.append(returns[i])
X, y = np.array(X), np.array(y)

st.caption(f"Created {len(X)} training samples, each using the previous {lookback} daily returns to predict the next one.")

# ------------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------------
st.header("3️⃣ Train the model")
c1, c2, c3 = st.columns(3)
n_layer1 = c1.slider("Neurons — layer 1", 4, 128, 32, 4)
n_layer2 = c2.slider("Neurons — layer 2 (0 = single layer)", 0, 64, 16, 4)
lr_init = c3.select_slider("Learning rate", options=[0.0001, 0.0005, 0.001, 0.005, 0.01], value=0.001)
epochs = st.slider("Training epochs (iterations)", 50, 1000, 300, 50)

split = int(len(X) * 0.85)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

layers = (n_layer1,) if n_layer2 == 0 else (n_layer1, n_layer2)
model = MLPRegressor(
    hidden_layer_sizes=layers, learning_rate_init=lr_init, max_iter=epochs,
    early_stopping=True, random_state=42,
)
with st.spinner("Training neural network..."):
    model.fit(X_train_s, y_train)

y_pred = model.predict(X_test_s)

col1, col2, col3 = st.columns(3)
col1.metric("Test R²", f"{r2_score(y_test, y_pred):.3f}")
col2.metric("Test RMSE", f"{np.sqrt(mean_squared_error(y_test, y_pred)):.5f}")
col3.metric("Training loss curve length", f"{len(model.loss_curve_)} epochs")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("4️⃣ See it work")
tab1, tab2, tab3 = st.tabs(["Training Loss Curve", "Predicted vs Actual Returns", "Reconstructed Price Path"])

with tab1:
    fig1 = go.Figure(go.Scatter(y=model.loss_curve_, mode="lines"))
    fig1.update_layout(title="Training loss over epochs", xaxis_title="Epoch", yaxis_title="Loss")
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("If the loss is still dropping steeply at the end, add more epochs. If it plateaued early, "
               "more epochs won't help — try more neurons instead.")

with tab2:
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(y=y_test, mode="lines", name="Actual return"))
    fig2.add_trace(go.Scatter(y=y_pred, mode="lines", name="Predicted return"))
    fig2.update_layout(title="Predicted vs actual daily returns (test set)")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    last_train_price = prices[split + lookback]
    actual_path = last_train_price * np.exp(np.cumsum(y_test))
    pred_path = last_train_price * np.exp(np.cumsum(y_pred))
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(y=actual_path, mode="lines", name="Actual price"))
    fig3.add_trace(go.Scatter(y=pred_path, mode="lines", name="Model-implied price"))
    fig3.update_layout(title="Reconstructed price path from predicted returns")
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("Small return-prediction errors compound over time — this is why price-level accuracy "
               "looks worse than single-step return accuracy. Normal, and worth noticing.")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
st.markdown(
    f"""
- Test R² of **{r2_score(y_test, y_pred):.3f}** on next-day returns — daily returns are notoriously
  close to random, so even a modest positive R² here is a meaningful signal, not a rounding error.
- If widening the network (more neurons/layers) doesn't improve test performance, the bottleneck is
  usually **signal, not model capacity** — real markets have a low signal-to-noise ratio.
- This same sliding-window setup is exactly what you'd feed into a production LSTM/Transformer —
  swapping in `keras.layers.LSTM` here is a drop-in upgrade once you're comfortable with the workflow.
"""
)
