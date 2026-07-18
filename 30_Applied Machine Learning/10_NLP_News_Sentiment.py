"""Module 9: NLP Sentiment Analysis - Financial News Headlines"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

st.set_page_config(page_title="NLP - News Sentiment", page_icon="📰", layout="wide")

st.title("📰 Module 9: NLP Sentiment Analysis")
st.subheader("Scoring financial news headlines to generate a trading signal")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    Text has to be turned into numbers before any ML model can use it.
    **TF-IDF** (Term Frequency – Inverse Document Frequency) weights each
    word by how distinctive it is to a document — common words like "the"
    get near-zero weight, rare/informative words like "bankruptcy" or
    "record-profit" get high weight.

    This lab trains a **classifier on headline text** to predict sentiment
    (positive/negative), then shows how a stream of headline sentiment
    scores could feed into a trading signal.
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic financial headlines", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_headlines(seed=21):
    rng = np.random.default_rng(seed)
    positive_templates = [
        "{co} beats earnings expectations, shares surge",
        "{co} reports record quarterly profit",
        "{co} raises full-year guidance after strong demand",
        "Analysts upgrade {co} to buy on strong outlook",
        "{co} announces major new contract win",
        "{co} stock rallies on positive analyst coverage",
        "{co} expands into new markets, investors optimistic",
        "{co} beats revenue forecast, margins improve",
    ]
    negative_templates = [
        "{co} misses earnings estimates, shares tumble",
        "{co} warns of weaker demand ahead",
        "{co} faces regulatory investigation over accounting",
        "Analysts downgrade {co} amid growth concerns",
        "{co} announces layoffs after disappointing results",
        "{co} stock falls on profit warning",
        "{co} cuts full-year guidance, investors react",
        "{co} reports declining margins and rising costs",
    ]
    companies = ["Acme Corp", "Northbridge Holdings", "Zenith Bank", "Vertex Industries", "Solara Energy",
                 "Marlin Retail", "Ionix Tech", "Kestrel Airlines", "Bramble Foods", "Halcyon Capital"]
    rows = []
    for _ in range(600):
        co = rng.choice(companies)
        if rng.uniform() < 0.5:
            text = rng.choice(positive_templates).format(co=co)
            label = 1
        else:
            text = rng.choice(negative_templates).format(co=co)
            label = 0
        rows.append({"headline": text, "sentiment": label})
    return pd.DataFrame(rows).drop_duplicates().reset_index(drop=True)


if data_source == "Synthetic financial headlines":
    df = make_synthetic_headlines()
    st.caption(f"{len(df)} synthetic headlines, labeled positive/negative from templates + company names.")
else:
    uploaded = st.file_uploader("Upload CSV with a text column and a 0/1 sentiment column", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

st.dataframe(df.head(10), use_container_width=True)
text_col = st.selectbox("Text column", df.columns, index=0)
label_col = st.selectbox("Sentiment label column (0/1)", [c for c in df.columns if c != text_col],
                          index=len(df.columns) - 2 if len(df.columns) > 1 else 0)

# ------------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------------
st.header("2️⃣ Train the model")
c1, c2, c3 = st.columns(3)
max_features = c1.slider("Max vocabulary size (TF-IDF)", 100, 3000, 800, 100)
ngram_max = c2.selectbox("Max n-gram size", [1, 2, 3], index=1)
test_size = c3.slider("Test set size (%)", 10, 40, 20, 5) / 100

X_text = df[text_col].astype(str)
y = df[label_col].astype(int)
X_train_text, X_test_text, y_train, y_test = train_test_split(
    X_text, y, test_size=test_size, random_state=42, stratify=y
)

vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=(1, ngram_max), stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train_text)
X_test_vec = vectorizer.transform(X_test_text)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)
y_pred = model.predict(X_test_vec)

col1, col2 = st.columns(2)
col1.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.3f}")
col2.metric("F1 score", f"{f1_score(y_test, y_pred):.3f}")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("3️⃣ See it work")
tab1, tab2 = st.tabs(["Most Predictive Words", "Confusion Matrix"])

with tab1:
    feature_names = np.array(vectorizer.get_feature_names_out())
    coefs = model.coef_[0]
    top_pos_idx = np.argsort(coefs)[-15:]
    top_neg_idx = np.argsort(coefs)[:15]
    words_df = pd.DataFrame({
        "word": list(feature_names[top_pos_idx]) + list(feature_names[top_neg_idx]),
        "weight": list(coefs[top_pos_idx]) + list(coefs[top_neg_idx]),
        "direction": ["Positive"] * 15 + ["Negative"] * 15,
    }).sort_values("weight")
    fig = px.bar(words_df, x="weight", y="word", color="direction", orientation="h",
                 title="Words/phrases most associated with positive vs negative sentiment",
                 color_discrete_map={"Positive": "#2ca02c", "Negative": "#d62728"})
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    cm = confusion_matrix(y_test, y_pred)
    fig2 = px.imshow(cm, text_auto=True, labels=dict(x="Predicted", y="Actual"),
                      x=["Negative", "Positive"], y=["Negative", "Positive"])
    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------------
# TRY YOUR OWN HEADLINE
# ------------------------------------------------------------------
st.header("4️⃣ Modify the model — score your own headline")
custom_headline = st.text_input("Enter a financial headline", "Company reports surprise profit and raises guidance")
if custom_headline:
    vec = vectorizer.transform([custom_headline])
    prob = model.predict_proba(vec)[0, 1]
    st.success(f"Predicted sentiment: **{'Positive' if prob >= 0.5 else 'Negative'}** "
               f"(positive probability = {prob:.1%})")

# ------------------------------------------------------------------
# SIGNAL EXAMPLE
# ------------------------------------------------------------------
st.header("5️⃣ From sentiment to a trading signal")
st.caption("A simple illustration: score every headline in the test set and aggregate to a daily-style signal.")
scored = pd.DataFrame({"headline": X_test_text.values, "actual": y_test.values,
                        "predicted_prob_positive": model.predict_proba(X_test_vec)[:, 1]})
st.dataframe(scored.head(15), use_container_width=True)
avg_signal = scored["predicted_prob_positive"].mean()
st.metric("Average sentiment score across sample headlines", f"{avg_signal:.2f}")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
st.markdown(
    f"""
- Model accuracy of **{accuracy_score(y_test, y_pred):.1%}** on held-out headlines shows how well
  word patterns alone can separate positive from negative financial news.
- The **most predictive words** panel is the "why" behind the model — in production, always sanity-check
  that these words make financial sense (avoids the model latching onto spurious patterns).
- A real sentiment-trading pipeline aggregates scores like `predicted_prob_positive` per stock, per day,
  and tests whether the resulting signal actually predicts *next-day returns* — a natural follow-up
  combining this module with Module 1 (Linear Regression) or Module 7 (ARIMA).
"""
)
