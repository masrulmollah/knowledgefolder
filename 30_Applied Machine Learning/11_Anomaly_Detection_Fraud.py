"""Module 10: Anomaly Detection (Isolation Forest) - Unsupervised Fraud Flagging"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, confusion_matrix, precision_score, recall_score

st.set_page_config(page_title="Anomaly Detection - Fraud", page_icon="🚨", layout="wide")

st.title("🚨 Module 10: Anomaly Detection (Isolation Forest)")
st.subheader("Flagging unusual transactions without any labeled fraud examples")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    Sometimes you don't have labeled fraud data at all — new fraud patterns
    emerge before anyone's tagged them. **Isolation Forest** solves this by
    exploiting a simple idea: anomalies are *easier to isolate* with random
    splits than normal points, because they sit in sparse regions of the
    feature space. No labels required to train it.

    The **contamination rate** (expected % of anomalies) is the main knob —
    it's a business assumption, not something learned from data, so this lab
    lets you set it directly and see how the flagged set changes.
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic transaction data", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=3000, anomaly_rate=0.03, seed=23):
    rng = np.random.default_rng(seed)
    amount = rng.lognormal(3.3, 1.0, n)
    hour = rng.integers(6, 23, n)
    merchant_risk_score = rng.beta(2, 8, n)
    txn_velocity_1h = rng.poisson(1.0, n)

    n_anom = int(n * anomaly_rate)
    idx = rng.choice(n, n_anom, replace=False)
    is_anomaly = np.zeros(n, dtype=int)
    is_anomaly[idx] = 1
    amount[idx] *= rng.uniform(4, 12, n_anom)
    hour[idx] = rng.integers(0, 5, n_anom)
    merchant_risk_score[idx] = rng.beta(6, 2, n_anom)
    txn_velocity_1h[idx] += rng.poisson(6, n_anom)

    return pd.DataFrame({
        "amount": amount.round(2),
        "hour_of_day": hour,
        "merchant_risk_score": merchant_risk_score.round(3),
        "txn_velocity_last_hour": txn_velocity_1h,
        "is_anomaly_ground_truth": is_anomaly,  # only used to evaluate, not to train
    })


if data_source == "Synthetic transaction data":
    n_points = st.slider("Number of transactions", 500, 10000, 3000, 500)
    true_rate = st.slider("Hidden true anomaly rate (for evaluation only)", 0.01, 0.10, 0.03, 0.01)
    df = make_synthetic_data(n_points, true_rate)
    st.caption("Note: `is_anomaly_ground_truth` exists only so we can grade the model — the model itself "
               "never sees it during fitting, exactly like a real unsupervised deployment.")
else:
    uploaded = st.file_uploader("Upload CSV (all numeric feature columns; optional ground-truth label column)",
                                 type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

st.dataframe(df.head(10), use_container_width=True)

possible_label_cols = [c for c in df.columns if df[c].dropna().isin([0, 1]).all() and df[c].nunique() <= 2]
label_col = st.selectbox("Ground-truth label column (optional, for evaluation only — not used in training)",
                          ["None"] + possible_label_cols)
feature_cols = st.multiselect(
    "Feature columns to detect anomalies on",
    [c for c in df.columns if c != label_col],
    default=[c for c in df.columns if c != label_col],
)
if len(feature_cols) < 1:
    st.warning("Select at least one feature column.")
    st.stop()

# ------------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------------
st.header("2️⃣ Train the model")
c1, c2 = st.columns(2)
contamination = c1.slider("Contamination rate (expected % anomalies)", 0.01, 0.20, 0.03, 0.01)
n_estimators = c2.slider("Number of trees", 50, 500, 150, 10)

X = df[feature_cols].values
X_scaled = StandardScaler().fit_transform(X)

model = IsolationForest(contamination=contamination, n_estimators=n_estimators, random_state=42)
model.fit(X_scaled)
anomaly_pred = (model.predict(X_scaled) == -1).astype(int)  # -1 = anomaly, 1 = normal
anomaly_score = -model.score_samples(X_scaled)  # higher = more anomalous

df_result = df.copy()
df_result["anomaly_score"] = anomaly_score
df_result["flagged"] = anomaly_pred

st.metric("Transactions flagged", f"{anomaly_pred.sum()} of {len(df)} ({anomaly_pred.mean():.1%})")

if label_col != "None":
    y_true = df[label_col].astype(int).values
    col1, col2, col3 = st.columns(3)
    col1.metric("ROC-AUC (vs ground truth)", f"{roc_auc_score(y_true, anomaly_score):.3f}")
    col2.metric("Precision", f"{precision_score(y_true, anomaly_pred, zero_division=0):.3f}")
    col3.metric("Recall", f"{recall_score(y_true, anomaly_pred, zero_division=0):.3f}")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("3️⃣ See it work")
tab1, tab2, tab3 = st.tabs(["Anomaly Score Distribution", "2D Visualization", "Flagged Transactions"])

with tab1:
    fig1 = px.histogram(df_result, x="anomaly_score", color="flagged", nbins=50, barmode="overlay",
                         title="Anomaly score distribution (higher = more unusual)")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    pca = PCA(n_components=2)
    coords = pca.fit_transform(X_scaled)
    plot_df = pd.DataFrame({"PC1": coords[:, 0], "PC2": coords[:, 1],
                             "status": np.where(anomaly_pred == 1, "Flagged", "Normal")})
    fig2 = px.scatter(plot_df, x="PC1", y="PC2", color="status",
                       color_discrete_map={"Flagged": "#d62728", "Normal": "#1f77b4"},
                       title="Transactions in 2D (PCA projection) — flagged points highlighted")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.dataframe(
        df_result[df_result["flagged"] == 1].sort_values("anomaly_score", ascending=False).head(25),
        use_container_width=True,
    )

# ------------------------------------------------------------------
# SCENARIO
# ------------------------------------------------------------------
st.header("4️⃣ Modify the model — score a hypothetical transaction")
scenario_vals = {}
cols = st.columns(len(feature_cols))
for i, fc in enumerate(feature_cols):
    with cols[i]:
        scenario_vals[fc] = st.number_input(fc, value=float(np.round(df[fc].mean(), 2)))

scaler_for_scenario = StandardScaler().fit(X)
new_point_scaled = scaler_for_scenario.transform([[scenario_vals[fc] for fc in feature_cols]])
new_score = -model.score_samples(new_point_scaled)[0]
new_flag = model.predict(new_point_scaled)[0] == -1
st.success(f"Anomaly score: **{new_score:.3f}** → {'🚨 FLAGGED AS ANOMALY' if new_flag else '✅ Looks normal'}")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
st.markdown(
    f"""
- The **contamination rate** is a business assumption, not a learned parameter — raising it flags more
  transactions (catches more real fraud, but also more false positives); lowering it does the opposite.
  This is the unsupervised equivalent of the threshold slider in the supervised fraud module (Module 4).
- Unlike Module 4 (XGBoost), this model needed **zero labeled fraud examples** to train — valuable when
  fraud patterns are new or labels are scarce/delayed.
- In production, teams often run **both**: Isolation Forest to catch novel/unknown patterns, and a
  supervised model (Module 4) to catch known fraud patterns with high precision.
"""
)
