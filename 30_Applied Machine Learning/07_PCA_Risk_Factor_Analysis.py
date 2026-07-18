"""Module 6: Principal Component Analysis - Risk Factor Analysis"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="PCA - Risk Factor Analysis", page_icon="🧬", layout="wide")

st.title("🧬 Module 6: Principal Component Analysis (PCA)")
st.subheader("Reducing dozens of correlated risk factors to a handful of drivers")

with st.expander("🎓 60-second theory recap", expanded=True):
    st.markdown(
        """
    Asset returns and risk factors are usually **highly correlated** (e.g. bond
    yields across maturities all move together). PCA finds new, uncorrelated
    "super-factors" (principal components) that are weighted combinations of
    the originals, ranked by how much variance they explain.

    In finance this is exactly how **yield curve models** work: the first 3
    components of a bond yield curve almost always correspond to
    **level, slope, and curvature** — a famous, textbook result you can
    reproduce yourself below.
    """
    )

# ------------------------------------------------------------------
# DATA
# ------------------------------------------------------------------
st.header("1️⃣ Data")
data_source = st.radio("Choose data source", ["Synthetic yield-curve-like data", "Upload my own CSV"], horizontal=True)


@st.cache_data
def make_synthetic_data(n=600, seed=9):
    rng = np.random.default_rng(seed)
    tenors = ["1Y", "2Y", "3Y", "5Y", "7Y", "10Y", "20Y", "30Y"]
    level = rng.normal(0, 1.0, n)
    slope = rng.normal(0, 0.5, n)
    curvature = rng.normal(0, 0.25, n)
    tenor_years = np.array([1, 2, 3, 5, 7, 10, 20, 30])
    data = {}
    for t, ty in zip(tenors, tenor_years):
        loading_level = 1.0
        loading_slope = (ty - 10) / 30
        loading_curv = -((ty - 10) ** 2) / 200 + 1
        noise = rng.normal(0, 0.05, n)
        data[t] = 2.5 + level * loading_level + slope * loading_slope + curvature * loading_curv + noise
    return pd.DataFrame(data)


if data_source == "Synthetic yield-curve-like data":
    n_points = st.slider("Number of daily observations", 100, 2000, 600, 50)
    df = make_synthetic_data(n_points)
    st.caption("Synthetic daily yields across 8 tenors, driven by 3 latent factors (level/slope/curvature).")
else:
    uploaded = st.file_uploader("Upload CSV (numeric columns = correlated risk factors)", type="csv")
    if uploaded is None:
        st.info("Upload a CSV to continue, or switch back to synthetic data above.")
        st.stop()
    df = pd.read_csv(uploaded)

st.dataframe(df.head(10), use_container_width=True)
feature_cols = st.multiselect("Columns to include in PCA", df.columns.tolist(), default=df.columns.tolist())
if len(feature_cols) < 2:
    st.warning("Select at least two columns.")
    st.stop()

st.subheader("Correlation matrix (this is *why* PCA helps)")
corr = df[feature_cols].corr()
fig_corr = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
                      title="Correlation between raw factors")
st.plotly_chart(fig_corr, use_container_width=True)

# ------------------------------------------------------------------
# TRAIN
# ------------------------------------------------------------------
st.header("2️⃣ Run PCA")
n_components = st.slider("Number of components to compute", 2, min(len(feature_cols), 10), min(3, len(feature_cols)))

X_scaled = StandardScaler().fit_transform(df[feature_cols].values)
pca = PCA(n_components=n_components)
scores = pca.fit_transform(X_scaled)

explained = pca.explained_variance_ratio_
st.metric("Cumulative variance explained", f"{explained.sum()*100:.1f}%")

# ------------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------------
st.header("3️⃣ See it work")
tab1, tab2, tab3 = st.tabs(["Variance Explained", "Component Loadings", "Scores (2D projection)"])

with tab1:
    var_df = pd.DataFrame({"Component": [f"PC{i+1}" for i in range(n_components)], "Variance Explained": explained})
    fig = px.bar(var_df, x="Component", y="Variance Explained", title="How much each component explains")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    loadings = pd.DataFrame(
        pca.components_.T, index=feature_cols, columns=[f"PC{i+1}" for i in range(n_components)]
    )
    fig2 = px.imshow(loadings.T, text_auto=".2f", aspect="auto", color_continuous_scale="RdBu_r",
                      title="Loadings: how each original factor maps into each component")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("A large loading means that original factor strongly drives that component.")

with tab3:
    score_df = pd.DataFrame(scores[:, :2], columns=["PC1", "PC2"])
    fig3 = px.scatter(score_df, x="PC1", y="PC2", title="Observations projected onto the top 2 components")
    st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------------------------
# SCENARIO
# ------------------------------------------------------------------
st.header("4️⃣ Modify the model — see PC1's shape change")
st.caption("PC1 usually captures a broad 'level' move. Change how many components you extract above and watch "
           "loadings tab update.")

# ------------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------------
st.header("💡 Insights")
top_component_name = "PC1"
st.markdown(
    f"""
- Just **{n_components} components explain {explained.sum()*100:.1f}%** of the variation across
  {len(feature_cols)} original (highly correlated) factors — this is the core value of PCA:
  massive dimensionality reduction with minimal information loss.
- Look at the **loadings heatmap**: if this is yield-curve-like data, PC1 usually loads roughly
  equally on every tenor (a parallel **level** shift), PC2 loads positive on one end and negative
  on the other (a **slope** move), and PC3 is high in the middle, low at the ends (**curvature**).
- In practice, risk teams use the top 2-3 components instead of dozens of raw factors to run
  **scenario analysis and stress tests** — much simpler, almost as accurate.
"""
)
