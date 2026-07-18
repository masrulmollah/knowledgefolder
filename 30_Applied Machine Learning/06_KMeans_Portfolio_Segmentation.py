"""Module 5: K-Means Clustering - Customer / Portfolio Segmentation"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

st.set_page_config(page_title="K-Means - Portfolio Segmentation", page_icon="🧩", layout="wide")

st.title("🧩 Module 5: K-Means Clustering")
st.subheader("Segmenting customers or portfolios into behavior/risk groups")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    K-Means is **unsupervised** — there's no target label. It groups rows
    into *k* clusters by minimizing the distance between each point and its
    cluster's center. In finance, this powers **customer segmentation**
    (e.g. "high-net-worth conservative investors" vs "young aggressive
    traders") and **portfolio grouping** for risk reporting.

    Two key questions this lab answers:
    - **How many clusters (k) actually fit the data?** → Elbow method
    - **What does each cluster look like in plain English?** → Cluster profiles
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic customer data", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=900, seed=5):
    rng = np.random.default_rng(seed)
    # Three natural segments
    segs = rng.choice([0, 1, 2], size=n, p=[0.4, 0.35, 0.25])
    age = np.where(segs == 0, rng.normal(60, 8, n), np.where(segs == 1, rng.normal(40, 7, n), rng.normal(28, 5, n)))
    portfolio_value = np.where(
        segs == 0, rng.normal(500000, 150000, n), np.where(segs == 1, rng.normal(120000, 40000, n), rng.normal(15000, 8000, n))
    )
    risk_appetite = np.where(segs == 0, rng.normal(2, 0.7, n), np.where(segs == 1, rng.normal(5, 1, n), rng.normal(8, 1, n)))
    trade_frequency_per_month = np.where(
        segs == 0, rng.poisson(1, n), np.where(segs == 1, rng.poisson(5, n), rng.poisson(15, n))
    )
    return pd.DataFrame(
        {
            "age": age.clip(18, 90).round(0),
            "portfolio_value": portfolio_value.clip(1000, None).round(0),
            "risk_appetite_score": risk_appetite.clip(1, 10).round(1),
            "trades_per_month": trade_frequency_per_month,
        }
    )


if data_source == "Synthetic customer data":
    n_points = st.slider("Number of customers", 200, 3000, 900, 100)
    df = make_synthetic_data(n_points)
else:
    uploaded = st.file_uploader("Upload CSV (all numeric feature columns)", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

st.dataframe(df.head(10), use_container_width=True)
feature_cols = st.multiselect("Feature columns to cluster on", df.columns.tolist(), default=df.columns.tolist())
if len(feature_cols) < 2:
    st.warning("Select at least two feature columns.")
    st.stop()

X = df[feature_cols].values
X_scaled = StandardScaler().fit_transform(X)

# ------------------------------------------------------------------
# ELBOW METHOD
# ------------------------------------------------------------------
st.header("2️⃣ How many clusters? (Elbow method)")
max_k = st.slider("Max k to test", 3, 12, 8, 1)
inertias = []
sil_scores = []
for k in range(2, max_k + 1):
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X_scaled)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, km.labels_))

elbow_df = pd.DataFrame({"k": range(2, max_k + 1), "Inertia": inertias, "Silhouette Score": sil_scores})
c1, c2 = st.columns(2)
with c1:
    fig = px.line(elbow_df, x="k", y="Inertia", markers=True, title="Elbow curve (lower = tighter clusters)")
    st.plotly_chart(fig, use_container_width=True)
with c2:
    fig2 = px.line(elbow_df, x="k", y="Silhouette Score", markers=True,
                   title="Silhouette score (higher = better-separated clusters)")
    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------------------------
# TRAIN FINAL MODEL
# ------------------------------------------------------------------
st.header("3️⃣ Train the model & see it work")
k = st.slider("Chosen number of clusters (k)", 2, max_k, 3, 1)
model = KMeans(n_clusters=k, n_init=10, random_state=42)
labels = model.fit_predict(X_scaled)
df_result = df.copy()
df_result["cluster"] = labels.astype(str)

st.metric("Silhouette score at this k", f"{silhouette_score(X_scaled, labels):.3f}")

pca = PCA(n_components=2)
coords = pca.fit_transform(X_scaled)
plot_df = pd.DataFrame({"PC1": coords[:, 0], "PC2": coords[:, 1], "cluster": df_result["cluster"]})
fig3 = px.scatter(plot_df, x="PC1", y="PC2", color="cluster",
                   title="Clusters visualized in 2D (via PCA projection)")
st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------------------------
# CLUSTER PROFILES
# ------------------------------------------------------------------
st.header("4️⃣ Cluster profiles")
profile = df_result.groupby("cluster")[feature_cols].mean().round(2)
profile["count"] = df_result.groupby("cluster").size()
st.dataframe(profile, use_container_width=True)

fig4 = px.imshow(
    StandardScaler().fit_transform(profile[feature_cols]).T,
    x=profile.index, y=feature_cols, text_auto=".2f", aspect="auto",
    labels=dict(x="Cluster", y="Feature", color="Relative level"),
    title="Cluster profile heatmap (standardized — red = above average, blue = below)",
    color_continuous_scale="RdBu_r",
)
st.plotly_chart(fig4, use_container_width=True)

# ------------------------------------------------------------------
# SCENARIO
# ------------------------------------------------------------------
st.header("5️⃣ Modify the model — classify a new customer")
scenario_vals = {}
cols = st.columns(len(feature_cols))
for i, fc in enumerate(feature_cols):
    with cols[i]:
        scenario_vals[fc] = st.number_input(fc, value=float(np.round(df[fc].mean(), 2)))

scaler_for_scenario = StandardScaler().fit(X)
new_point_scaled = scaler_for_scenario.transform([[scenario_vals[fc] for fc in feature_cols]])
assigned_cluster = model.predict(new_point_scaled)[0]
st.success(f"This customer would be assigned to **Cluster {assigned_cluster}**")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
st.markdown(
    f"""
- The silhouette score peaked around **k = {elbow_df.loc[elbow_df['Silhouette Score'].idxmax(), 'k']:.0f}**
  in the elbow analysis above — that's a data-driven starting point for how many segments really exist.
- Look at the **cluster profile heatmap**: each cluster's "red" features are what defines it
  (e.g. a cluster that's red on `trades_per_month` and `risk_appetite_score` = active, aggressive traders).
- Segments like these typically map directly to business actions: tailored product offers,
  different advisory service tiers, or risk-based account monitoring.
"""
)
