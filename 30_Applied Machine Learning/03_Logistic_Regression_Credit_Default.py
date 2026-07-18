"""Module 2: Logistic Regression - Credit Default Prediction"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, precision_score, recall_score, f1_score

st.set_page_config(page_title="Logistic Regression - Credit Default", page_icon="💳", layout="wide")

st.title("💳 Module 2: Logistic Regression")
st.subheader("Predicting the probability a borrower defaults")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    Logistic regression models the **probability of a binary outcome**
    (default / no default) using a sigmoid curve instead of a straight line:

    **P(default) = 1 / (1 + e^-(β₀ + β₁x₁ + ... ))**

    Widely used for credit scoring because it's interpretable: each
    coefficient converts to an **odds ratio** — "each extra unit of debt-to-income
    multiplies default odds by e^β".

    Key evaluation tools: **ROC-AUC** (ranking quality) and the
    **confusion matrix** (how threshold choice trades off false positives
    vs false negatives — a real business decision in lending).
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic loan data", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=1500, seed=7):
    rng = np.random.default_rng(seed)
    income = rng.normal(60000, 20000, n).clip(15000, None)
    debt_to_income = rng.beta(2, 5, n) * 0.9
    credit_score = rng.normal(680, 70, n).clip(300, 850)
    late_payments = rng.poisson(1.2, n)
    loan_amount = rng.normal(15000, 7000, n).clip(1000, None)

    logit = (
        -6
        + 4.5 * debt_to_income
        - 0.012 * (credit_score - 680)
        + 0.35 * late_payments
        + 0.00003 * loan_amount
        - 0.00002 * (income - 60000) / 1000
    )
    prob = 1 / (1 + np.exp(-logit))
    default = (rng.uniform(0, 1, n) < prob).astype(int)
    return pd.DataFrame(
        {
            "income": income.round(0),
            "debt_to_income": debt_to_income.round(3),
            "credit_score": credit_score.round(0),
            "late_payments_last_year": late_payments,
            "loan_amount": loan_amount.round(0),
            "default": default,
        }
    )


if data_source == "Synthetic loan data":
    n_points = st.slider("Number of loan records", 300, 5000, 1500, 100)
    df = make_synthetic_data(n_points)
    st.caption(f"Synthetic loan book — default rate: {df['default'].mean():.1%}")
else:
    uploaded = st.file_uploader("Upload CSV (last column should be 0/1 default label)", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

st.dataframe(df.head(10), use_container_width=True)

target_col = st.selectbox("Target column (binary: 0/1)", df.columns, index=len(df.columns) - 1)
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
c1, c2 = st.columns(2)
test_size = c1.slider("Test set size (%)", 10, 40, 25, 5) / 100
threshold = c2.slider("Classification threshold", 0.05, 0.95, 0.5, 0.05)
reg_strength = st.select_slider("Regularization strength (C) — lower = more regularized", 
                                 options=[0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0], value=1.0)

X = df[feature_cols].values
y = df[target_col].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

model = LogisticRegression(C=reg_strength, max_iter=1000)
model.fit(X_train_s, y_train)
y_proba = model.predict_proba(X_test_s)[:, 1]
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
tab1, tab2, tab3 = st.tabs(["ROC Curve", "Confusion Matrix", "Odds Ratios"])

with tab1:
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    fig = px.area(x=fpr, y=tpr, labels={"x": "False Positive Rate", "y": "True Positive Rate"},
                  title=f"ROC Curve (AUC = {roc_auc_score(y_test, y_proba):.3f})")
    fig.add_shape(type="line", x0=0, y0=0, x1=1, y1=1, line=dict(dash="dash"))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    cm = confusion_matrix(y_test, y_pred)
    fig2 = px.imshow(cm, text_auto=True, labels=dict(x="Predicted", y="Actual"),
                      x=["No Default", "Default"], y=["No Default", "Default"],
                      title=f"Confusion Matrix at threshold={threshold}")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Lowering the threshold catches more defaulters (higher recall) but flags more good "
               "borrowers too (lower precision) — a real risk-appetite decision.")

with tab3:
    odds = pd.DataFrame({"Feature": feature_cols, "Coefficient": model.coef_[0],
                          "Odds Ratio (e^coef)": np.exp(model.coef_[0])})
    odds = odds.sort_values("Coefficient", key=abs, ascending=False)
    st.dataframe(odds, use_container_width=True)
    fig3 = px.bar(odds, x="Coefficient", y="Feature", orientation="h", title="Standardized coefficients")
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

x_new = scaler.transform([[scenario_vals[fc] for fc in feature_cols]])
prob_new = model.predict_proba(x_new)[0, 1]
st.success(f"Predicted default probability: **{prob_new:.1%}**  "
           f"→ classified as **{'DEFAULT RISK' if prob_new >= threshold else 'LIKELY OK'}** at threshold {threshold}")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
top = odds.iloc[0]
st.markdown(
    f"""
- The model separates defaulters from non-defaulters with an AUC of **{roc_auc_score(y_test, y_proba):.3f}**
  (0.5 = random, 1.0 = perfect).
- **`{top['Feature']}`** is the strongest driver of default risk in this dataset (standardized coefficient = {top['Coefficient']:.2f}).
- Moving the **threshold slider** is the real business lever: a bank tightening credit standards
  raises the threshold (fewer approvals, fewer bad loans); a growth-focused lender lowers it.
"""
)
