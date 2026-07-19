"""
================================================================================
 DATA ANALYTICS CASE EXERCISE PLATFORM
================================================================================
A single-page, interactive Streamlit application for practicing end-to-end
data analytics: data cleaning, descriptive stats, visualization, correlation,
time-series analysis, customer segmentation (RFM + KMeans), predictive
modeling (regression), hypothesis testing, and insight/report generation.

HOW TO RUN
----------
    pip install streamlit pandas numpy matplotlib seaborn plotly scikit-learn scipy
    streamlit run analytics_exercise_app.py

The dataset is a synthetic retail sales dataset generated on first run. You can:
  - Edit it directly in the app (add/remove/change rows)
  - Upload your own CSV to replace it
  - Reset back to the sample dataset at any time
================================================================================
"""

import io
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Data Analytics Case Exercise", layout="wide", page_icon="📊")

STANDARD_COLS = [
    "OrderID", "Date", "CustomerID", "Region", "Category", "Product",
    "CustomerSegment", "CustomerAge", "PaymentMethod", "UnitsSold",
    "UnitPrice", "Discount(%)", "Revenue", "Cost", "Profit",
]

# --------------------------------------------------------------------------------
# SAMPLE DATA GENERATION
# --------------------------------------------------------------------------------
@st.cache_data
def generate_sample_data(seed=42, n=320):
    rng = np.random.default_rng(seed)
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=int(d)) for d in rng.integers(0, 365, n)]
    regions = rng.choice(["North", "South", "East", "West"], n, p=[0.30, 0.25, 0.25, 0.20])
    categories = rng.choice(["Electronics", "Clothing", "Furniture", "Groceries", "Sports"], n)

    products_map = {
        "Electronics": ["Headphones", "Smartphone", "Laptop", "Tablet", "Smartwatch"],
        "Clothing": ["T-Shirt", "Jeans", "Jacket", "Shoes", "Cap"],
        "Furniture": ["Chair", "Table", "Sofa", "Bookshelf", "Bed"],
        "Groceries": ["Rice", "Snacks", "Beverages", "Dairy", "Spices"],
        "Sports": ["Football", "Yoga Mat", "Dumbbells", "Cycle", "Tennis Racket"],
    }
    products = [rng.choice(products_map[c]) for c in categories]
    customer_ids = rng.choice([f"C{i:03d}" for i in range(1, 81)], n)
    segments = rng.choice(["Consumer", "Corporate", "Home Office"], n, p=[0.55, 0.30, 0.15])
    ages = rng.integers(18, 65, n)
    payment = rng.choice(["Credit Card", "Debit Card", "UPI/Wallet", "Cash"], n, p=[0.40, 0.25, 0.25, 0.10])
    units = rng.integers(1, 12, n)

    base_price = {"Electronics": 250, "Clothing": 40, "Furniture": 180, "Groceries": 15, "Sports": 60}
    unit_price = np.array([base_price[c] * rng.uniform(0.8, 1.3) for c in categories]).round(2)
    discount = rng.choice([0, 5, 10, 15, 20], n, p=[0.40, 0.25, 0.15, 0.12, 0.08])

    df = pd.DataFrame({
        "OrderID": [f"ORD{i:04d}" for i in range(1, n + 1)],
        "Date": dates,
        "CustomerID": customer_ids,
        "Region": regions,
        "Category": categories,
        "Product": products,
        "CustomerSegment": segments,
        "CustomerAge": ages,
        "PaymentMethod": payment,
        "UnitsSold": units,
        "UnitPrice": unit_price,
        "Discount(%)": discount,
    })
    df["Revenue"] = (df["UnitsSold"] * df["UnitPrice"] * (1 - df["Discount(%)"] / 100)).round(2)
    df["Cost"] = (df["UnitsSold"] * df["UnitPrice"] * 0.6).round(2)
    df["Profit"] = (df["Revenue"] - df["Cost"]).round(2)
    df["Date"] = pd.to_datetime(df["Date"])

    # Introduce a bit of messiness on purpose -> gives students something to clean
    messy_idx = rng.choice(df.index, 12, replace=False)
    df.loc[messy_idx[:6], "CustomerAge"] = np.nan
    df.loc[messy_idx[6:10], "Region"] = None
    dup_rows = df.sample(5, random_state=seed)
    df = pd.concat([df, dup_rows], ignore_index=True)

    return df.sort_values("Date").reset_index(drop=True)


def has_standard_schema(df):
    required = ["Date", "Region", "Category", "Revenue", "Profit", "CustomerID",
                "UnitsSold", "UnitPrice", "Discount(%)", "CustomerSegment", "PaymentMethod"]
    return all(c in df.columns for c in required)


# --------------------------------------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------------------------------------
if "df" not in st.session_state:
    st.session_state.df = generate_sample_data()
if "student_insights" not in st.session_state:
    st.session_state.student_insights = ""
if "student_recommendations" not in st.session_state:
    st.session_state.student_recommendations = ""

# --------------------------------------------------------------------------------
# SIDEBAR: DATA SOURCE + FILTERS
# --------------------------------------------------------------------------------
st.sidebar.title("⚙️ Control Panel")
st.sidebar.caption("Configure your dataset and filters. Changes apply across every tab.")

data_source = st.sidebar.radio("Data Source", ["Use Sample Dataset", "Upload Your Own CSV"])

if data_source == "Upload Your Own CSV":
    uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded is not None:
        try:
            new_df = pd.read_csv(uploaded)
            if "Date" in new_df.columns:
                new_df["Date"] = pd.to_datetime(new_df["Date"], errors="coerce")
            st.session_state.df = new_df
            st.sidebar.success(f"Loaded {len(new_df)} rows.")
        except Exception as e:
            st.sidebar.error(f"Could not read file: {e}")

if st.sidebar.button("🔄 Reset to Sample Data"):
    st.session_state.df = generate_sample_data()
    st.sidebar.info("Data reset to the default sample dataset.")

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Global Filters")

df_full = st.session_state.df.copy()
schema_ok = has_standard_schema(df_full)

if schema_ok and not df_full.empty:
    min_date, max_date = df_full["Date"].min(), df_full["Date"].max()
    date_range = st.sidebar.date_input("Date Range", [min_date, max_date])
    regions_sel = st.sidebar.multiselect(
        "Region", sorted(df_full["Region"].dropna().unique()),
        default=sorted(df_full["Region"].dropna().unique()),
    )
    cat_sel = st.sidebar.multiselect(
        "Category", sorted(df_full["Category"].dropna().unique()),
        default=sorted(df_full["Category"].dropna().unique()),
    )
    seg_sel = st.sidebar.multiselect(
        "Customer Segment", sorted(df_full["CustomerSegment"].dropna().unique()),
        default=sorted(df_full["CustomerSegment"].dropna().unique()),
    )

    mask = pd.Series(True, index=df_full.index)
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        mask &= (df_full["Date"] >= pd.Timestamp(date_range[0])) & (df_full["Date"] <= pd.Timestamp(date_range[1]))
    mask &= df_full["Region"].isin(regions_sel)
    mask &= df_full["Category"].isin(cat_sel)
    mask &= df_full["CustomerSegment"].isin(seg_sel)
    filtered_df = df_full[mask].copy()
else:
    filtered_df = df_full.copy()
    st.sidebar.warning("Dataset doesn't match the standard schema — filters are limited. "
                        "Reset to sample data for the full exercise experience.")

st.sidebar.markdown("---")
st.sidebar.metric("Rows in view", len(filtered_df))

# --------------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------------
st.title("📊 Data Analytics Case Exercise Platform")
st.markdown(
    """
Welcome to your **interactive data analytics learning lab**. This single page takes you through a complete
analytics workflow — from raw, messy data to business recommendations — using an editable retail sales dataset.

**What you'll practice:** data cleaning · descriptive statistics · exploratory visualization · correlation analysis ·
time-series trends · customer segmentation (RFM + clustering) · predictive modeling (regression) · statistical
hypothesis testing · insight generation · analytics reporting.

Use the sidebar to edit, upload, or filter data — every tab below updates automatically.
"""
)

tab_labels = [
    "1️⃣ Data Overview & Editing",
    "2️⃣ Data Cleaning",
    "3️⃣ Descriptive Statistics",
    "4️⃣ Visual Exploration",
    "5️⃣ Correlation & Relationships",
    "6️⃣ Time Series Analysis",
    "7️⃣ Segmentation (RFM + Clustering)",
    "8️⃣ Predictive Modeling",
    "9️⃣ Hypothesis Testing",
    "🔟 Insights & Recommendations",
    "📄 Full Report Export",
]
tabs = st.tabs(tab_labels)

# ================================================================================
# TAB 1 — DATA OVERVIEW & EDITING
# ================================================================================
with tabs[0]:
    st.subheader("Dataset Overview & Editing")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Records", len(df_full))
    if schema_ok:
        c2.metric("Total Revenue", f"${df_full['Revenue'].sum():,.0f}")
        c3.metric("Total Profit", f"${df_full['Profit'].sum():,.0f}")
        c4.metric("Date Range", f"{df_full['Date'].min().date()} → {df_full['Date'].max().date()}")

    st.markdown("#### Preview & Edit")
    st.caption("Double-click a cell to edit. Use the ➕ row at the bottom to add data, or select a row and press "
               "delete to remove it. Changes apply instantly across the whole app.")
    edited_df = st.data_editor(df_full, num_rows="dynamic", width='stretch', key="data_editor_main")
    st.session_state.df = edited_df

    st.download_button(
        "⬇️ Download Current Dataset (CSV)",
        edited_df.to_csv(index=False).encode("utf-8"),
        "dataset.csv",
        "text/csv",
    )

    with st.expander("📋 Column Reference"):
        st.write(
            "OrderID, Date, CustomerID, Region, Category, Product, CustomerSegment, CustomerAge, "
            "PaymentMethod, UnitsSold, UnitPrice, Discount(%), Revenue, Cost, Profit"
        )

# ================================================================================
# TAB 2 — DATA CLEANING
# ================================================================================
with tabs[1]:
    st.subheader("Data Cleaning & Preparation")
    st.write("Real-world data is rarely perfect. Inspect and fix quality issues before analyzing.")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Missing Values by Column**")
        missing = df_full.isna().sum()
        missing = missing[missing > 0]
        if len(missing):
            st.dataframe(missing.rename("Missing Count"), width='stretch')
        else:
            st.success("No missing values found.")
    with col2:
        dup_count = int(df_full.duplicated().sum())
        st.metric("Duplicate Rows", dup_count)
        st.write("**Data Types**")
        st.dataframe(pd.DataFrame(df_full.dtypes.astype(str), columns=["Dtype"]), width='stretch')

    st.markdown("#### Cleaning Actions")
    a1, a2, a3 = st.columns(3)
    if a1.button("🧹 Remove Duplicate Rows"):
        st.session_state.df = df_full.drop_duplicates().reset_index(drop=True)
        st.success("Duplicates removed.")
        st.rerun()
    if a2.button("🔢 Fill Missing Numeric with Median"):
        temp = df_full.copy()
        num_cols = temp.select_dtypes(include=np.number).columns
        temp[num_cols] = temp[num_cols].fillna(temp[num_cols].median())
        st.session_state.df = temp
        st.success("Missing numeric values filled with the column median.")
        st.rerun()
    if a3.button("🚫 Drop Rows with Any Missing Value"):
        st.session_state.df = df_full.dropna().reset_index(drop=True)
        st.success("Rows containing missing values were dropped.")
        st.rerun()

    st.info(
        "💡 **Exercise prompt:** Which cleaning strategy is more appropriate here — dropping rows or "
        "imputing values? What would each choice do to your later averages and model results?"
    )

# ================================================================================
# TAB 3 — DESCRIPTIVE STATISTICS
# ================================================================================
with tabs[2]:
    st.subheader("Descriptive Statistics")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        st.write("**Numeric Summary**")
        st.dataframe(filtered_df.describe().T.round(2), width='stretch')

        st.write("**Categorical Breakdown**")
        cat_cols = ["Region", "Category", "CustomerSegment", "PaymentMethod"]
        cc1, cc2 = st.columns(2)
        for i, col in enumerate(cat_cols):
            target = cc1 if i % 2 == 0 else cc2
            with target:
                counts = filtered_df[col].value_counts().reset_index()
                counts.columns = [col, "Count"]
                fig = px.bar(counts, x=col, y="Count", title=f"Records by {col}", color=col)
                fig.update_layout(showlegend=False, height=320)
                st.plotly_chart(fig, width='stretch')

        st.markdown("#### Key Metrics")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Avg Order Value", f"${filtered_df['Revenue'].mean():,.2f}")
        m2.metric("Avg Profit Margin", f"{(filtered_df['Profit'].sum()/filtered_df['Revenue'].sum()*100):.1f}%")
        m3.metric("Total Units Sold", f"{filtered_df['UnitsSold'].sum():,}")
        m4.metric("Unique Customers", filtered_df["CustomerID"].nunique())

# ================================================================================
# TAB 4 — VISUAL EXPLORATION
# ================================================================================
with tabs[3]:
    st.subheader("Visual Exploration (EDA)")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        numeric_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = ["Region", "Category", "CustomerSegment", "PaymentMethod"]

        st.markdown("##### Distribution Explorer")
        d1, d2 = st.columns([1, 2])
        with d1:
            hist_col = st.selectbox("Numeric column", numeric_cols, index=numeric_cols.index("Revenue"))
            group_col = st.selectbox("Group / color by", categorical_cols)
        with d2:
            fig = px.histogram(filtered_df, x=hist_col, color=group_col, marginal="box", barmode="overlay",
                                opacity=0.7, title=f"Distribution of {hist_col} by {group_col}")
            st.plotly_chart(fig, width='stretch')

        st.markdown("##### Category Performance")
        e1, e2 = st.columns(2)
        with e1:
            agg = filtered_df.groupby("Category", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
            fig2 = px.bar(agg, x="Category", y="Revenue", title="Total Revenue by Category", color="Category")
            fig2.update_layout(showlegend=False)
            st.plotly_chart(fig2, width='stretch')
        with e2:
            agg2 = filtered_df.groupby("CustomerSegment", as_index=False)["Revenue"].sum()
            fig3 = px.pie(agg2, names="CustomerSegment", values="Revenue", title="Revenue Share by Customer Segment",
                          hole=0.4)
            st.plotly_chart(fig3, width='stretch')

        st.markdown("##### Box Plot Comparison")
        box_col = st.selectbox("Metric for box plot", numeric_cols, index=numeric_cols.index("Profit"), key="box_metric")
        box_group = st.selectbox("Compare across", categorical_cols, index=0, key="box_group")
        fig4 = px.box(filtered_df, x=box_group, y=box_col, color=box_group, points="outliers",
                      title=f"{box_col} by {box_group}")
        fig4.update_layout(showlegend=False)
        st.plotly_chart(fig4, width='stretch')

        st.info("💡 **Exercise prompt:** Which category shows the widest spread of profit? Does that suggest "
                "inconsistent pricing, discounting, or product mix?")

# ================================================================================
# TAB 5 — CORRELATION & RELATIONSHIPS
# ================================================================================
with tabs[4]:
    st.subheader("Correlation & Relationship Analysis")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        numeric_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()
        corr = filtered_df[numeric_cols].corr().round(2)

        st.markdown("##### Correlation Heatmap")
        fig = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r", aspect="auto",
                         title="Correlation Matrix of Numeric Variables")
        st.plotly_chart(fig, width='stretch')

        st.markdown("##### Scatter Explorer with Trend Line")
        s1, s2, s3 = st.columns(3)
        x_col = s1.selectbox("X axis", numeric_cols, index=numeric_cols.index("UnitPrice"))
        y_col = s2.selectbox("Y axis", numeric_cols, index=numeric_cols.index("Revenue"))
        color_col = s3.selectbox("Color by", ["Category", "Region", "CustomerSegment"])

        fig2 = px.scatter(filtered_df, x=x_col, y=y_col, color=color_col, opacity=0.7,
                           title=f"{y_col} vs {x_col}")
        # manual OLS trend line (avoids extra statsmodels dependency)
        valid = filtered_df[[x_col, y_col]].dropna()
        if len(valid) > 1:
            m, b = np.polyfit(valid[x_col], valid[y_col], 1)
            xs = np.linspace(valid[x_col].min(), valid[x_col].max(), 50)
            fig2.add_trace(go.Scatter(x=xs, y=m * xs + b, mode="lines", name="Trend line",
                                       line=dict(color="black", dash="dash")))
            r = np.corrcoef(valid[x_col], valid[y_col])[0, 1]
            st.caption(f"Pearson correlation (r) between **{x_col}** and **{y_col}**: **{r:.3f}**")
        st.plotly_chart(fig2, width='stretch')

        st.info("💡 **Exercise prompt:** Correlation isn't causation — what confounding variable could explain "
                "a correlation between UnitPrice and Revenue?")

# ================================================================================
# TAB 6 — TIME SERIES ANALYSIS
# ================================================================================
with tabs[5]:
    st.subheader("Time Series Analysis")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        freq_label = st.radio("Aggregation level", ["Daily", "Weekly", "Monthly"], horizontal=True)
        freq_map = {"Daily": "D", "Weekly": "W", "Monthly": "ME"}
        ts = (
            filtered_df.set_index("Date")
            .resample(freq_map[freq_label])["Revenue"]
            .sum()
            .reset_index()
        )
        ts["Moving Avg (3)"] = ts["Revenue"].rolling(3, min_periods=1).mean()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ts["Date"], y=ts["Revenue"], mode="lines+markers", name="Revenue"))
        fig.add_trace(go.Scatter(x=ts["Date"], y=ts["Moving Avg (3)"], mode="lines", name="Moving Average (3)",
                                  line=dict(dash="dot")))
        fig.update_layout(title=f"{freq_label} Revenue Trend", xaxis_title="Date", yaxis_title="Revenue")
        st.plotly_chart(fig, width='stretch')

        st.markdown("##### Day-of-Week Pattern")
        dow = filtered_df.copy()
        dow["DayOfWeek"] = dow["Date"].dt.day_name()
        order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dow_agg = dow.groupby("DayOfWeek", as_index=False)["Revenue"].mean()
        dow_agg["DayOfWeek"] = pd.Categorical(dow_agg["DayOfWeek"], categories=order, ordered=True)
        dow_agg = dow_agg.sort_values("DayOfWeek")
        fig2 = px.bar(dow_agg, x="DayOfWeek", y="Revenue", title="Average Revenue by Day of Week")
        st.plotly_chart(fig2, width='stretch')

        if len(ts) >= 2:
            first_half = ts["Revenue"].iloc[: len(ts) // 2].mean()
            second_half = ts["Revenue"].iloc[len(ts) // 2:].mean()
            growth = ((second_half - first_half) / first_half * 100) if first_half else 0
            st.metric("Trend: 1st half vs 2nd half avg revenue", f"{growth:+.1f}%")

        st.info("💡 **Exercise prompt:** Is there seasonality here, or is the pattern closer to random noise? "
                "What business action would a sustained downward trend justify?")

# ================================================================================
# TAB 7 — SEGMENTATION (RFM + CLUSTERING)
# ================================================================================
with tabs[6]:
    st.subheader("Customer Segmentation — RFM + K-Means Clustering")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        st.markdown(
            "**RFM** stands for **Recency** (days since last purchase), **Frequency** (number of orders), "
            "and **Monetary** value (total spend) — a classic customer-segmentation technique."
        )
        ref_date = filtered_df["Date"].max() + pd.Timedelta(days=1)
        rfm = filtered_df.groupby("CustomerID").agg(
            Recency=("Date", lambda x: (ref_date - x.max()).days),
            Frequency=("OrderID", "count"),
            Monetary=("Revenue", "sum"),
        ).reset_index()

        if len(rfm) < 4:
            st.warning("Not enough customers in the current filter to cluster. Broaden your filters.")
        else:
            k = st.slider("Number of clusters (k)", 2, 6, 3)
            scaler = StandardScaler()
            X = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])
            km = KMeans(n_clusters=k, random_state=42, n_init=10)
            rfm["Cluster"] = km.fit_predict(X).astype(str)

            c1, c2 = st.columns([2, 1])
            with c1:
                fig = px.scatter(
                    rfm, x="Frequency", y="Monetary", color="Cluster", size="Recency",
                    hover_data=["CustomerID", "Recency"], title="Customer Segments: Frequency vs Monetary Value"
                )
                st.plotly_chart(fig, width='stretch')
            with c2:
                st.write("**Cluster Profiles (averages)**")
                profile = rfm.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean().round(1)
                profile["Customers"] = rfm["Cluster"].value_counts()
                st.dataframe(profile, width='stretch')

            # simple auto-labeling: rank clusters by Monetary desc
            ranked = profile.sort_values("Monetary", ascending=False)
            labels = ["🏆 High Value", "⭐ Growing", "➖ Average", "⚠️ At Risk", "🔻 Low Value", "🔻 Low Value"]
            label_map = {cl: labels[i] if i < len(labels) else "Segment" for i, cl in enumerate(ranked.index)}
            st.write("**Suggested Segment Labels**")
            st.dataframe(
                pd.DataFrame({"Cluster": ranked.index, "Suggested Label": [label_map[c] for c in ranked.index]}),
                width='stretch',
            )

            st.download_button(
                "⬇️ Download RFM + Cluster Table (CSV)",
                rfm.to_csv(index=False).encode("utf-8"),
                "rfm_segments.csv",
                "text/csv",
            )

        st.info("💡 **Exercise prompt:** Which segment would you target with a loyalty campaign, and which "
                "would you target with a win-back discount?")

# ================================================================================
# TAB 8 — PREDICTIVE MODELING
# ================================================================================
with tabs[7]:
    st.subheader("Predictive Modeling — Revenue Regression")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        st.markdown("Build a simple linear regression model to predict **Revenue** from order attributes.")

        model_df = filtered_df.dropna(subset=["UnitsSold", "UnitPrice", "Discount(%)", "Category", "Region", "Revenue"]).copy()
        feature_cols_raw = ["UnitsSold", "UnitPrice", "Discount(%)", "Category", "Region"]
        X = pd.get_dummies(model_df[feature_cols_raw], columns=["Category", "Region"], drop_first=True)
        y = model_df["Revenue"]

        test_size = st.slider("Test set size (%)", 10, 50, 20) / 100.0

        if len(model_df) < 10:
            st.warning("Not enough rows to train a reliable model with the current filters.")
        else:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            m1, m2, m3 = st.columns(3)
            m1.metric("R² (test)", f"{r2_score(y_test, y_pred):.3f}")
            m2.metric("RMSE", f"{np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
            m3.metric("MAE", f"{mean_absolute_error(y_test, y_pred):.2f}")

            p1, p2 = st.columns(2)
            with p1:
                fig = px.scatter(x=y_test, y=y_pred, labels={"x": "Actual Revenue", "y": "Predicted Revenue"},
                                  title="Actual vs Predicted Revenue")
                lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
                fig.add_trace(go.Scatter(x=lims, y=lims, mode="lines", name="Perfect Prediction",
                                          line=dict(dash="dash", color="red")))
                st.plotly_chart(fig, width='stretch')
            with p2:
                coef_df = pd.DataFrame({"Feature": X.columns, "Coefficient": model.coef_}).sort_values(
                    "Coefficient", key=abs, ascending=False
                )
                fig2 = px.bar(coef_df, x="Coefficient", y="Feature", orientation="h",
                              title="Feature Impact on Predicted Revenue")
                st.plotly_chart(fig2, width='stretch')

            st.markdown("##### 🔮 Try Your Own Prediction")
            i1, i2, i3, i4, i5 = st.columns(5)
            in_units = i1.number_input("Units Sold", 1, 50, 5)
            in_price = i2.number_input("Unit Price", 1.0, 2000.0, 100.0)
            in_disc = i3.number_input("Discount (%)", 0, 50, 10)
            in_cat = i4.selectbox("Category", sorted(model_df["Category"].unique()))
            in_region = i5.selectbox("Region", sorted(model_df["Region"].unique()))

            new_row = pd.DataFrame([{
                "UnitsSold": in_units, "UnitPrice": in_price, "Discount(%)": in_disc,
                "Category": in_cat, "Region": in_region,
            }])
            new_X = pd.get_dummies(new_row, columns=["Category", "Region"], drop_first=True)
            new_X = new_X.reindex(columns=X.columns, fill_value=0)
            prediction = model.predict(new_X)[0]
            st.success(f"Predicted Revenue: **${prediction:,.2f}**")

        st.info("💡 **Exercise prompt:** Is a linear model appropriate here, or would a non-linear model "
                "(e.g. decision tree) capture the relationship better? What does R² actually tell you?")

# ================================================================================
# TAB 9 — HYPOTHESIS TESTING
# ================================================================================
with tabs[8]:
    st.subheader("Statistical Hypothesis Testing")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        alpha = 0.05

        st.markdown("##### Test 1: Two-Sample T-Test — Compare Mean Profit Between Two Regions")
        regions = sorted(filtered_df["Region"].dropna().unique())
        if len(regions) >= 2:
            t1, t2 = st.columns(2)
            reg_a = t1.selectbox("Region A", regions, index=0)
            reg_b = t2.selectbox("Region B", regions, index=1 if len(regions) > 1 else 0)
            group_a = filtered_df.loc[filtered_df["Region"] == reg_a, "Profit"].dropna()
            group_b = filtered_df.loc[filtered_df["Region"] == reg_b, "Profit"].dropna()
            if reg_a != reg_b and len(group_a) > 1 and len(group_b) > 1:
                t_stat, p_val = stats.ttest_ind(group_a, group_b, equal_var=False)
                st.write(f"t-statistic = **{t_stat:.3f}**, p-value = **{p_val:.4f}**")
                if p_val < alpha:
                    st.success(f"p < {alpha} → statistically significant difference in mean profit between {reg_a} and {reg_b}.")
                else:
                    st.info(f"p ≥ {alpha} → no statistically significant difference detected between {reg_a} and {reg_b}.")
            else:
                st.warning("Pick two different regions with enough data.")
        else:
            st.warning("Need at least two regions in the current filter.")

        st.markdown("---")
        st.markdown("##### Test 2: One-Way ANOVA — Revenue Across Categories")
        cats = filtered_df["Category"].dropna().unique()
        groups = [filtered_df.loc[filtered_df["Category"] == c, "Revenue"].dropna() for c in cats]
        groups = [g for g in groups if len(g) > 1]
        if len(groups) >= 2:
            f_stat, p_val2 = stats.f_oneway(*groups)
            st.write(f"F-statistic = **{f_stat:.3f}**, p-value = **{p_val2:.4f}**")
            if p_val2 < alpha:
                st.success(f"p < {alpha} → at least one category has a significantly different mean revenue.")
            else:
                st.info(f"p ≥ {alpha} → no significant difference in mean revenue across categories.")
        else:
            st.warning("Need at least two categories with sufficient data.")

        st.markdown("---")
        st.markdown("##### Test 3: Chi-Square Test — Category vs Payment Method Independence")
        contingency = pd.crosstab(filtered_df["Category"], filtered_df["PaymentMethod"])
        if contingency.shape[0] > 1 and contingency.shape[1] > 1:
            chi2, p_val3, dof, _ = stats.chi2_contingency(contingency)
            st.dataframe(contingency, width='stretch')
            st.write(f"Chi-square = **{chi2:.3f}**, df = **{dof}**, p-value = **{p_val3:.4f}**")
            if p_val3 < alpha:
                st.success(f"p < {alpha} → Category and Payment Method appear statistically dependent.")
            else:
                st.info(f"p ≥ {alpha} → no evidence of dependence between Category and Payment Method.")
        else:
            st.warning("Need more variety in Category/PaymentMethod to run this test.")

        st.info("💡 **Exercise prompt:** A p-value below 0.05 tells you a difference is unlikely due to chance — "
                "it does not tell you the difference is large or business-relevant. What else would you check?")

# ================================================================================
# TAB 10 — INSIGHTS & RECOMMENDATIONS
# ================================================================================
with tabs[9]:
    st.subheader("Insights & Recommendations")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        st.markdown("##### 🤖 Auto-Generated Insights (from current filtered data)")
        top_category = filtered_df.groupby("Category")["Revenue"].sum().idxmax()
        top_region = filtered_df.groupby("Region")["Revenue"].sum().idxmax()
        best_margin_seg = (
            filtered_df.groupby("CustomerSegment").apply(lambda d: d["Profit"].sum() / d["Revenue"].sum())
            .idxmax()
        )
        avg_discount = filtered_df["Discount(%)"].mean()
        overall_margin = filtered_df["Profit"].sum() / filtered_df["Revenue"].sum() * 100

        ts = filtered_df.set_index("Date").resample("ME")["Revenue"].sum()
        trend_note = "not enough data to assess a trend"
        if len(ts) >= 2:
            growth = (ts.iloc[-1] - ts.iloc[0]) / ts.iloc[0] * 100 if ts.iloc[0] else 0
            trend_note = f"revenue moved {growth:+.1f}% from the first to the last period in view"

        auto_insights = [
            f"**{top_category}** is the top-performing category by total revenue.",
            f"**{top_region}** region generates the highest total revenue.",
            f"The **{best_margin_seg}** segment has the best profit margin.",
            f"Overall profit margin across the filtered data is **{overall_margin:.1f}%**.",
            f"Average discount applied is **{avg_discount:.1f}%**.",
            f"Over the selected period, {trend_note}.",
        ]
        for ins in auto_insights:
            st.markdown(f"- {ins}")

        st.markdown("---")
        st.markdown("##### ✍️ Your Turn — Write Your Own Insights & Recommendations")
        st.session_state.student_insights = st.text_area(
            "Key Insights (what patterns did YOU find?)",
            value=st.session_state.student_insights,
            height=120,
            placeholder="e.g. Discounts above 15% correlate with lower profit margin in the Furniture category...",
        )
        st.session_state.student_recommendations = st.text_area(
            "Recommendations (what should the business DO?)",
            value=st.session_state.student_recommendations,
            height=120,
            placeholder="e.g. Cap discounts in Furniture at 10% and reallocate marketing spend toward North region...",
        )
        st.success("Your entries are saved and will be included in the exported report (Tab 11).")

# ================================================================================
# TAB 11 — FULL REPORT EXPORT
# ================================================================================
with tabs[10]:
    st.subheader("📄 Full Analytics Report Export")
    if not schema_ok:
        st.warning("This section needs the standard schema. Reset to the sample dataset to use it.")
    else:
        st.write("This compiles everything from the exercise into a single downloadable Markdown report.")

        top_category = filtered_df.groupby("Category")["Revenue"].sum().idxmax()
        top_region = filtered_df.groupby("Region")["Revenue"].sum().idxmax()
        overall_margin = filtered_df["Profit"].sum() / filtered_df["Revenue"].sum() * 100

        report_md = f"""# Data Analytics Case Exercise — Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 1. Dataset Summary
- Records analyzed: {len(filtered_df)}
- Date range: {filtered_df['Date'].min().date()} to {filtered_df['Date'].max().date()}
- Total Revenue: ${filtered_df['Revenue'].sum():,.2f}
- Total Profit: ${filtered_df['Profit'].sum():,.2f}
- Overall Profit Margin: {overall_margin:.1f}%

## 2. Descriptive Statistics
```
{filtered_df.describe().T.round(2).to_string()}
```

## 3. Key Automated Findings
- Top revenue category: **{top_category}**
- Top revenue region: **{top_region}**
- Average discount applied: {filtered_df['Discount(%)'].mean():.1f}%

## 4. Student Insights
{st.session_state.student_insights or "_(not yet filled in — see Tab 10)_"}

## 5. Student Recommendations
{st.session_state.student_recommendations or "_(not yet filled in — see Tab 10)_"}

## 6. Methodology Notes
- Correlation analysis via Pearson's r
- Customer segmentation via RFM + K-Means clustering
- Predictive modeling via multiple linear regression (train/test split)
- Hypothesis testing via t-test, one-way ANOVA, and chi-square test of independence

---
*Report generated by the Data Analytics Case Exercise Platform.*
"""
        st.text_area("Preview", report_md, height=350)
        st.download_button(
            "⬇️ Download Report (Markdown)",
            report_md.encode("utf-8"),
            "analytics_case_exercise_report.md",
            "text/markdown",
        )
        st.download_button(
            "⬇️ Download Filtered Dataset (CSV)",
            filtered_df.to_csv(index=False).encode("utf-8"),
            "filtered_dataset.csv",
            "text/csv",
        )

st.markdown("---")
st.caption("Built as a hands-on data analytics learning exercise — edit the data, run the analysis, and draw your own conclusions.")