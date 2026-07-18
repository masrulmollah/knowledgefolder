"""Module 4: Gradient Boosting (XGBoost) - Transaction Fraud Detection"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    roc_auc_score, roc_curve, precision_recall_curve, confusion_matrix,
    precision_score, recall_score, f1_score,
)

st.set_page_config(page_title="XGBoost - Fraud Detection", page_icon="🕵️", layout="wide")

st.title("🕵️ Module 4: Gradient Boosting (XGBoost)")
st.subheader("Detecting fraudulent transactions in highly imbalanced data")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    Gradient boosting builds trees **sequentially**, where each new tree
    focuses on correcting the errors of the trees before it. XGBoost is the
    industry-standard implementation — fast, regularized, and typically the
    top performer on tabular fraud/credit data in Kaggle competitions and
    production systems alike.

    Fraud data is almost always **imbalanced** (e.g. 0.5% fraud rate), so this
    lab focuses on **precision/recall trade-offs** rather than plain accuracy —
    accuracy is meaningless when 99.5% of transactions are "not fraud" anyway.
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic transaction data", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=8000, fraud_rate=0.03, seed=3):
    rng = np.random.default_rng(seed)
    amount = rng.lognormal(3.5, 1.2, n)
    hour = rng.integers(0, 24, n)
    distance_from_home = rng.exponential(15, n)
    is_new_merchant = rng.binomial(1, 0.15, n)
    txn_velocity_1h = rng.poisson(1.5, n)

    n_fraud = int(n * fraud_rate)
    idx_fraud = rng.choice(n, n_fraud, replace=False)
    fraud = np.zeros(n, dtype=int)
    fraud[idx_fraud] = 1

    amount[idx_fraud] *= rng.uniform(2, 8, n_fraud)
    distance_from_home[idx_fraud] *= rng.uniform(3, 10, n_fraud)
    is_new_merchant[idx_fraud] = rng.binomial(1, 0.7, n_fraud)
    txn_velocity_1h[idx_fraud] += rng.poisson(4, n_fraud)
    hour[idx_fraud] = rng.integers(0, 6, n_fraud)  # fraud skews to odd hours

    return pd.DataFrame(
        {
            "amount": amount.round(2),
            "hour_of_day": hour,
            "distance_from_home_km": distance_from_home.round(1),
            "is_new_merchant": is_new_merchant,
            "txn_velocity_last_hour": txn_velocity_1h,
            "is_fraud": fraud,
        }
    )


if data_source == "Synthetic transaction data":
    n_points = st.slider("Number of transactions", 2000, 30000, 8000, 1000)
    fraud_rate = st.slider("Fraud rate", 0.01, 0.10, 0.03, 0.01)
    df = make_synthetic_data(n_points, fraud_rate)
    st.caption(f"Synthetic transactions — actual fraud rate: {df['is_fraud'].mean():.2%}")
else:
    uploaded = st.file_uploader("Upload CSV (last column = 0/1 fraud label)", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

st.dataframe(df.head(10), use_container_width=True)
target_col = st.selectbox("Target column (binary)", df.columns, index=len(df.columns) - 1)
feature_cols = st.multiselect(
    "Feature columns", [c for c in df.columns if c != target_col],
    default=[c for c in df.columns if c != target_col],
)
if not feature_cols:
    st.warning("Select at least one feature column.")
    st.stop()

# ------------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------------
st.header("2️⃣ Train the model")
c1, c2, c3 = st.columns(3)
n_estimators = c1.slider("Number of boosting rounds", 20, 500, 150, 10)
max_depth = c2.slider("Max tree depth", 1, 10, 4, 1)
lr = c3.select_slider("Learning rate", options=[0.01, 0.03, 0.05, 0.1, 0.2, 0.3], value=0.1)
threshold = st.slider("Classification threshold", 0.05, 0.95, 0.5, 0.05)

X = df[feature_cols].values
y = df[target_col].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

scale_pos_weight = (y_train == 0).sum() / max((y_train == 1).sum(), 1)
model = XGBClassifier(
    n_estimators=n_estimators, max_depth=max_depth, learning_rate=lr,
    scale_pos_weight=scale_pos_weight, eval_metric="logloss", random_state=42,
)
model.fit(X_train, y_train)
y_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_proba >= threshold).astype(int)

col1, col2, col3, col4 = st.columns(4)
col1.metric("ROC-AUC", f"{roc_auc_score(y_test, y_proba):.3f}")
col2.metric("Precision", f"{precision_score(y_test, y_pred, zero_division=0):.3f}")
col3.metric("Recall", f"{recall_score(y_test, y_pred, zero_division=0):.3f}")
col4.metric("F1", f"{f1_score(y_test, y_pred, zero_division=0):.3f}")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("3️⃣ See it work")
tab1, tab2, tab3, tab4 = st.tabs(["Precision-Recall Curve", "ROC Curve", "Confusion Matrix", "Feature Importance"])

with tab1:
    prec, rec, _ = precision_recall_curve(y_test, y_proba)
    fig = px.line(x=rec, y=prec, labels={"x": "Recall", "y": "Precision"},
                  title="Precision-Recall Curve (more informative than ROC when data is imbalanced)")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    fig2 = px.area(x=fpr, y=tpr, title=f"ROC Curve (AUC = {roc_auc_score(y_test, y_proba):.3f})",
                    labels={"x": "False Positive Rate", "y": "True Positive Rate"})
    fig2.add_shape(type="line", x0=0, y0=0, x1=1, y1=1, line=dict(dash="dash"))
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    cm = confusion_matrix(y_test, y_pred)
    fig3 = px.imshow(cm, text_auto=True, labels=dict(x="Predicted", y="Actual"),
                      x=["Legit", "Fraud"], y=["Legit", "Fraud"])
    st.plotly_chart(fig3, use_container_width=True)
    n_flagged = y_pred.sum()
    st.caption(f"At this threshold, {n_flagged} of {len(y_pred)} test transactions get flagged for review.")

with tab4:
    imp_df = pd.DataFrame({"Feature": feature_cols, "Importance": model.feature_importances_}).sort_values(
        "Importance", ascending=True
    )
    fig4 = px.bar(imp_df, x="Importance", y="Feature", orientation="h")
    st.plotly_chart(fig4, use_container_width=True)

# ------------------------------------------------------------------
# SCENARIO
# ------------------------------------------------------------------
st.header("4️⃣ Modify the model — score a hypothetical transaction")
scenario_vals = {}
cols = st.columns(len(feature_cols))
for i, fc in enumerate(feature_cols):
    with cols[i]:
        scenario_vals[fc] = st.number_input(fc, value=float(np.round(df[fc].mean(), 2)))

prob_new = model.predict_proba([[scenario_vals[fc] for fc in feature_cols]])[0, 1]
st.success(f"Predicted fraud probability: **{prob_new:.1%}** "
           f"→ {'🚩 FLAG FOR REVIEW' if prob_new >= threshold else '✅ Pass through'}")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
top_feat = imp_df.sort_values("Importance", ascending=False).iloc[0]
st.markdown(
    f"""
- **`{top_feat['Feature']}`** contributes most to fraud scores in this dataset.
- Watch the **precision vs recall trade-off**: raising the threshold means fewer false alarms
  (analysts aren't swamped) but some fraud slips through; lowering it catches more fraud at the
  cost of flagging legitimate customers — a direct operations-cost vs fraud-loss decision.
- `scale_pos_weight` is set automatically from the class imbalance in your data — this is why
  boosting handles rare-event fraud detection better than plain accuracy-optimized models.
"""
)
