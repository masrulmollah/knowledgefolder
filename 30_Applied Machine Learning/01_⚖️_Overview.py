"""
Overview.py
------------------------------------------------------------
Landing page for the "Applied Machine Learning for Finance" section.
Run with:  streamlit run Overview.py
Streamlit will auto-list every page inside pages/ in the sidebar.
------------------------------------------------------------
"""

import streamlit as st

st.set_page_config(
    page_title="Applied ML for Finance",
    page_icon="💹",
    layout="wide",
)

# ------------------------------------------------------------------
# HERO
# ------------------------------------------------------------------
st.title("💹 Applied Machine Learning for Finance")
st.subheader("Learn the models finance teams actually use — by building them yourself.")

st.markdown(
    """
This section is **not** a slide deck. Every model below is a live lab:
you generate or upload data, train the model in your browser, tune its
knobs, and read the results — the same workflow you'd use on the job.

**How to use this section**
1. Pick a module from the sidebar (left).
2. Read the 60-second theory recap at the top of that page.
3. Use the built-in synthetic dataset, or upload your own CSV.
4. Train the model, tweak hyperparameters, and watch metrics/plots update.
5. Read the "Insights" box — it translates the model output into a
   finance decision (e.g. *"which features actually drive default risk"*).
"""
)

st.divider()

# ------------------------------------------------------------------
# SYLLABUS
# ------------------------------------------------------------------
st.header("📚 Module Syllabus")

modules = [
    {
        "num": "1",
        "title": "Linear Regression",
        "finance_use": "Predicting stock/portfolio returns from macro & factor variables",
        "concepts": "OLS, R², residual diagnostics, multicollinearity",
        "page": "pages/1_Linear_Regression_Stock_Returns.py",
    },
    {
        "num": "2",
        "title": "Logistic Regression",
        "finance_use": "Credit default / loan approval classification",
        "concepts": "Odds ratios, ROC-AUC, decision threshold trade-offs",
        "page": "pages/2_Logistic_Regression_Credit_Default.py",
    },
    {
        "num": "3",
        "title": "Random Forest",
        "finance_use": "Credit scoring with non-linear feature interactions",
        "concepts": "Bagging, feature importance, overfitting control",
        "page": "pages/3_Random_Forest_Credit_Scoring.py",
    },
    {
        "num": "4",
        "title": "Gradient Boosting (XGBoost)",
        "finance_use": "Transaction fraud detection at scale",
        "concepts": "Boosting, class imbalance, precision/recall trade-offs",
        "page": "pages/4_XGBoost_Fraud_Detection.py",
    },
    {
        "num": "5",
        "title": "K-Means Clustering",
        "finance_use": "Segmenting customers or portfolios into risk/behavior groups",
        "concepts": "Unsupervised learning, elbow method, cluster profiling",
        "page": "pages/5_KMeans_Portfolio_Segmentation.py",
    },
    {
        "num": "6",
        "title": "Principal Component Analysis (PCA)",
        "finance_use": "Reducing dozens of risk factors to a handful of drivers",
        "concepts": "Variance explained, loadings, dimensionality reduction",
        "page": "pages/6_PCA_Risk_Factor_Analysis.py",
    },
    {
        "num": "7",
        "title": "ARIMA Time Series",
        "finance_use": "Forecasting a stock price / index level",
        "concepts": "Stationarity, ACF/PACF, (p,d,q) tuning, backtesting",
        "page": "pages/7_ARIMA_Stock_Forecasting.py",
    },
    {
        "num": "8",
        "title": "Neural Network (MLP/LSTM-style)",
        "finance_use": "Sequence-based price prediction",
        "concepts": "Layers, epochs, learning rate, over/underfitting",
        "page": "pages/8_Neural_Network_Stock_Prediction.py",
    },
    {
        "num": "9",
        "title": "NLP Sentiment Analysis",
        "finance_use": "Scoring financial news/headlines for trading signals",
        "concepts": "Text vectorization, lexicon vs ML scoring, signal correlation",
        "page": "pages/9_NLP_News_Sentiment.py",
    },
    {
        "num": "10",
        "title": "Anomaly Detection (Isolation Forest)",
        "finance_use": "Flagging unusual transactions without labeled fraud data",
        "concepts": "Unsupervised outlier scoring, contamination rate, thresholds",
        "page": "pages/10_Anomaly_Detection_Fraud.py",
    },
]

for m in modules:
    with st.container(border=True):
        c1, c2 = st.columns([5, 1])
        with c1:
            st.markdown(f"### {m['num']}. {m['title']}")
            st.markdown(f"**Finance use case:** {m['finance_use']}")
            st.markdown(f"**Core concepts:** {m['concepts']}")
        with c2:
            st.caption("Open from menu:")
            st.code(m["page"].split("/")[-1], language=None)

st.divider()

# ------------------------------------------------------------------
# LEARNING PATH SUGGESTION
# ------------------------------------------------------------------
st.header("🧭 Suggested learning path")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Foundations**")
    st.markdown("1. Linear Regression\n2. Logistic Regression\n3. Random Forest")
with col2:
    st.markdown("**Scaling up**")
    st.markdown("4. XGBoost\n5. K-Means\n6. PCA")
with col3:
    st.markdown("**Specialized**")
    st.markdown("7. ARIMA\n8. Neural Networks\n9. NLP Sentiment\n10. Anomaly Detection")

st.info(
    "💡 Each lab is self-contained — you can also jump straight to whichever "
    "model is most relevant to your role (credit risk, trading, fraud, etc.)."
)