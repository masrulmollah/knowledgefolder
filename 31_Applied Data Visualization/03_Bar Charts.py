"""
Module 2 — Bar & Column Charts: Comparing Categories
======================================================
Run standalone:
    streamlit run pages/2_📊_Bar_Charts.py
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Bar Charts", page_icon="📊", layout="wide")

st.title("📊 Module 2: Bar & Column Charts — Comparing Categories")

with st.expander("📌 When should you use a bar chart?", expanded=True):
    st.markdown(
        """
    Use a **bar/column chart** when you have:
    - A **categorical variable** (segment, region, quarter, department, sector)
    - Paired with a **numeric measure** you want to compare across categories

    Typical finance examples: revenue by business segment, YoY growth by quarter,
    expense breakdown by department, headcount by region.

    Choose **grouped bars** to compare two categories side by side (e.g., segment × year),
    or **stacked bars** to show composition (parts of a whole) across categories.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_data():
    segments = ["Retail Banking", "Wealth Mgmt", "Investment Banking", "Insurance", "Asset Mgmt"]
    years = [2023, 2024, 2025]
    rng = np.random.default_rng(3)
    rows = []
    base = {"Retail Banking": 420, "Wealth Mgmt": 180, "Investment Banking": 260, "Insurance": 140, "Asset Mgmt": 95}
    for y in years:
        for s in segments:
            growth = rng.uniform(-0.05, 0.18)
            base[s] = base[s] * (1 + growth)
            rows.append({"Segment": s, "Year": y, "Revenue ($M)": round(base[s], 1)})
    return pd.DataFrame(rows)

if src == "Upload my own CSV":
    up = st.file_uploader("Upload a CSV with a category column and a numeric column", type="csv")
    if up is not None:
        df = pd.read_csv(up)
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_data()
else:
    df = make_sample_data()

st.dataframe(df.head(10), use_container_width=True)

cat_cols = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2, c3 = st.columns(3)
with c1:
    cat_col = st.selectbox("Category (x-axis)", cat_cols, index=0 if cat_cols else None)
with c2:
    val_col = st.selectbox("Value (bar height/length)", num_cols, index=0 if num_cols else None)
with c3:
    group_col = st.selectbox("Group/color by (optional)", ["(none)"] + cat_cols)

c4, c5, c6 = st.columns(3)
with c4:
    orientation = st.radio("Orientation", ["Vertical", "Horizontal"], horizontal=True)
with c5:
    mode = st.radio("Mode (if grouped)", ["Grouped", "Stacked", "100% Stacked"], horizontal=True)
with c6:
    sort_desc = st.checkbox("Sort by value (descending)", value=True)

group = None if group_col == "(none)" else group_col

plot_df = df.copy()
if group is None:
    plot_df = plot_df.groupby(cat_col, as_index=False)[val_col].sum()
    if sort_desc:
        plot_df = plot_df.sort_values(val_col, ascending=False)
else:
    if sort_desc:
        order = plot_df.groupby(cat_col)[val_col].sum().sort_values(ascending=False).index
        plot_df[cat_col] = pd.Categorical(plot_df[cat_col], categories=order, ordered=True)
        plot_df = plot_df.sort_values(cat_col)

barmode = {"Grouped": "group", "Stacked": "stack", "100% Stacked": "stack"}[mode]

kwargs = dict(
    x=val_col if orientation == "Horizontal" else cat_col,
    y=cat_col if orientation == "Horizontal" else val_col,
    color=group,
    barmode=barmode,
    text_auto=".2s",
)
if mode == "100% Stacked" and group is not None:
    totals = plot_df.groupby(cat_col)[val_col].transform("sum")
    plot_df = plot_df.assign(**{val_col: plot_df[val_col] / totals * 100})
    kwargs["labels"] = {val_col: f"{val_col} (% of total)"}

fig = px.bar(plot_df, **kwargs, orientation="h" if orientation == "Horizontal" else "v")
fig.update_layout(height=500, legend=dict(orientation="h", yanchor="bottom", y=1.02))
st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- **Bar length/height** encodes magnitude — longer bar = larger value.
- **Grouped bars** let you compare a second category side-by-side within each main category
  (e.g., each segment's revenue across three years, bars next to each other).
- **Stacked bars** show how sub-categories add up to a total — the full bar height is the total,
  each colored segment is a component.
- **100% stacked bars** strip out the total and show only the *mix* (share of 100%) —
  useful for comparing composition even when totals differ wildly.
- **Sorting** by value (rather than alphabetically) makes the biggest/smallest categories
  immediately visible.
"""
)

st.header("💡 Step 4 — Extract the insight")
if group is None:
    top = plot_df.iloc[0]
    bottom = plot_df.iloc[-1]
    st.success(
        f"**Auto-insight:** **{top[cat_col]}** is the largest at "
        f"{top[val_col]:,.1f}, while **{bottom[cat_col]}** is the smallest at "
        f"{bottom[val_col]:,.1f} — a gap of {top[val_col]-bottom[val_col]:,.1f}."
    )
else:
    totals_by_cat = df.groupby(cat_col)[val_col].sum().sort_values(ascending=False)
    st.success(
        f"**Auto-insight:** Summed across all groups, **{totals_by_cat.index[0]}** "
        f"contributes the most overall ({totals_by_cat.iloc[0]:,.1f})."
    )

with st.expander("📝 Practice checklist"):
    st.checkbox("I can explain the difference between grouped and stacked bars")
    st.checkbox("I know when a 100% stacked bar is more useful than a regular stacked bar")
    st.checkbox("I sorted the bars and can explain why this improves readability")
    st.checkbox("I uploaded my own categorical dataset and built this chart on it")