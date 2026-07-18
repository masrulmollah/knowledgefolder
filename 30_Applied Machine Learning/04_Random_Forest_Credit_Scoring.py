"""Module 3: Random Forest - Credit Scoring"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, accuracy_score

st.set_page_config(page_title="Random Forest - Credit Scoring", page_icon="🌲", layout="wide")

st.title("🌲 Module 3: Random Forest")
st.subheader("Credit scoring with non-linear feature interactions")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    A Random Forest builds **many decision trees** on random subsets of data
    and features, then averages their votes. This captures **non-linear
    relationships and interactions** (e.g. "high debt-to-income is only risky
    when credit score is also low") that plain logistic regression misses.

    Trade-off: less directly interpretable than logistic regression, but
    **feature importance** and **partial views** recover most of the insight,
    and accuracy is usually higher on messy, real-world credit data.
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic credit data", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=1500, seed=11):
    rng = np.random.default_rng(seed)
    income = rng.normal(58000, 22000, n).clip(15000, None)
    debt_to_income = rng.beta(2, 5, n) * 0.9
    credit_score = rng.normal(670, 75, n).clip(300, 850)
    late_payments = rng.poisson(1.1, n)
    utilization = rng.beta(2, 3, n)
    years_employed = rng.gamma(3, 2, n)

    # Non-linear interaction: high utilization AND low credit score is much riskier
    risk_score = (
        3.0 * debt_to_income
        + 2.5 * utilization * (credit_score < 640)
        - 0.01 * (credit_score - 670)
        + 0.4 * late_payments
        - 0.05 * years_employed
        + rng.normal(0, 0.5, n)
    )
    prob = 1 / (1 + np.exp(-(risk_score - 1)))
    default = (rng.uniform(0, 1, n) < prob).astype(int)
    return pd.DataFrame(
        {
            "income": income.round(0),
            "debt_to_income": debt_to_income.round(3),
            "credit_score": credit_score.round(0),
            "late_payments_last_year": late_payments,
            "credit_utilization": utilization.round(3),
            "years_employed": years_employed.round(1),
            "default": default,
        }
    )


if data_source == "Synthetic credit data":
    n_points = st.slider("Number of loan records", 300, 5000, 1500, 100)
    df = make_synthetic_data(n_points)
    st.caption(f"Synthetic loan book — default rate: {df['default'].mean():.1%}")
else:
    uploaded = st.file_uploader("Upload CSV (last column = 0/1 default label)", type="csv")
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
n_estimators = c1.slider("Number of trees", 10, 500, 200, 10)
max_depth = c2.slider("Max tree depth (0 = unlimited)", 0, 20, 6, 1)
test_size = c3.slider("Test set size (%)", 10, 40, 25, 5) / 100

X = df[feature_cols].values
y = df[target_col].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

model = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=None if max_depth == 0 else max_depth,
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)
y_proba = model.predict_proba(X_test)[:, 1]
y_pred = model.predict(X_test)

col1, col2 = st.columns(2)
col1.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.3f}")
col2.metric("ROC-AUC", f"{roc_auc_score(y_test, y_proba):.3f}")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("3️⃣ See it work")
tab1, tab2, tab3 = st.tabs(["Feature Importance", "ROC Curve", "Confusion Matrix"])

with tab1:
    imp_df = pd.DataFrame({"Feature": feature_cols, "Importance": model.feature_importances_})
    imp_df = imp_df.sort_values("Importance", ascending=True)
    fig = px.bar(imp_df, x="Importance", y="Feature", orientation="h",
                 title="What drives the model's predictions?")
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
                      x=["No Default", "Default"], y=["No Default", "Default"])
    st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------------------------
# SCENARIO
# ------------------------------------------------------------------
st.header("4️⃣ Modify the model — score a hypothetical borrower")
scenario_vals = {}
cols = st.columns(len(feature_cols))
for i, fc in enumerate(feature_cols):
    with cols[i]:
        scenario_vals[fc] = st.number_input(fc, value=float(np.round(df[fc].mean(), 2)))

prob_new = model.predict_proba([[scenario_vals[fc] for fc in feature_cols]])[0, 1]
st.success(f"Predicted default probability: **{prob_new:.1%}**")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
top_feat = imp_df.sort_values("Importance", ascending=False).iloc[0]
st.markdown(
    f"""
- **`{top_feat['Feature']}`** is the single most important predictor the forest found
  (importance = {top_feat['Importance']:.3f}).
- Try increasing **max tree depth** — accuracy on the training set will climb, but if test-set
  AUC starts to *fall*, that's overfitting: the forest is memorizing noise, not learning patterns.
- Compare this AUC to the Logistic Regression module (Module 2) on the same data — the gap
  (if any) tells you how much non-linear interaction the simpler model was missing.
"""
)
