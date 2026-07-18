"""
Module 8 — Pie, Donut & 100% Stacked Charts: Composition
==========================================================
Run standalone:
    streamlit run pages/8_🥧_Pie_Donut_Charts.py
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Pie & Donut Charts", page_icon="🥧", layout="wide")

st.title("🥧 Module 8: Pie, Donut & 100% Stacked Charts — Composition")

with st.expander("📌 When should you use a pie/donut chart?", expanded=True):
    st.markdown(
        """
    Use a **pie/donut chart** when you have:
    - A single categorical breakdown of a whole (parts summing to 100%)
    - And there are **relatively few categories** (ideally under ~6-7)

    Typical finance examples: portfolio asset allocation, revenue mix by product line,
    expense breakdown by category.

    ⚠️ **Known weakness**: humans are bad at comparing angles/areas precisely.
    If you have many categories, similar-sized slices, or need to compare composition
    **across multiple time periods**, a **100% stacked bar chart** communicates it better —
    this module lets you build both so you can see the difference yourself.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_data():
    data = {
        "Category": ["US Equities", "Intl Equities", "Bonds", "Real Estate", "Cash", "Alternatives"],
        "2024 Allocation (%)": [35, 20, 25, 8, 5, 7],
        "2025 Allocation (%)": [40, 18, 20, 10, 4, 8],
    }
    return pd.DataFrame(data)

if src == "Upload my own CSV":
    up = st.file_uploader("Upload a CSV with a category column and one or more numeric columns", type="csv")
    if up is not None:
        df = pd.read_csv(up)
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_data()
else:
    df = make_sample_data()

cat_cols = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
st.dataframe(df, use_container_width=True)

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2 = st.columns(2)
with c1:
    cat_col = st.selectbox("Category column", cat_cols, index=0 if cat_cols else None)
with c2:
    val_col = st.selectbox("Value column (single period)", num_cols, index=0 if num_cols else None)

view = st.radio("Chart style", ["Pie", "Donut", "100% Stacked Bar (compare across periods)"], horizontal=True)

if view == "100% Stacked Bar (compare across periods)":
    period_cols = st.multiselect(
        "Select 2+ numeric columns representing different periods to compare",
        num_cols, default=num_cols[: min(2, len(num_cols))],
    )
    if len(period_cols) < 1:
        st.warning("Select at least one period column.")
        st.stop()
    long_df = df.melt(id_vars=[cat_col], value_vars=period_cols, var_name="Period", value_name="Value")
    fig = px.bar(long_df, x="Period", y="Value", color=cat_col, barmode="stack")
    fig.update_layout(barnorm="percent", height=550)
else:
    hole = 0.55 if view == "Donut" else 0
    fig = px.pie(df, names=cat_col, values=val_col, hole=hole)
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(height=550)

st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
if view == "100% Stacked Bar (compare across periods)":
    st.markdown(
        """
    - Each **bar is normalized to 100%**, so you're comparing *mix*, not absolute size.
    - **Segment height** = that category's share of the total in that period.
    - **Track a single color across bars** to see how that category's share grew or shrank
      over time — this is much easier than comparing two separate pie charts side by side.
    """
    )
else:
    st.markdown(
        """
    - **Slice angle/area** = that category's share of the whole (all slices sum to 100%).
    - Slices are easiest to compare when there are **few categories and clearly different sizes**.
    - When slices are similar in size, or there are many categories, exact ranking becomes hard
      to eyeball — this is the chart's main limitation, and worth stating explicitly when you
      present one.
    - A **donut** frees up the center for a label (e.g., total portfolio value) but reads
      identically to a pie otherwise.
    """
    )

st.header("💡 Step 4 — Extract the insight")
if view != "100% Stacked Bar (compare across periods)":
    sorted_df = df[[cat_col, val_col]].sort_values(val_col, ascending=False)
    top = sorted_df.iloc[0]
    share = top[val_col] / df[val_col].sum() * 100
    st.success(
        f"**Auto-insight:** **{top[cat_col]}** is the largest component at "
        f"**{share:.1f}%** of the total — "
        + ("a meaningful concentration worth monitoring." if share > 35 else "a reasonably diversified mix.")
    )
else:
    if len(period_cols) >= 2:
        shifts = (df.set_index(cat_col)[period_cols[-1]] / df[period_cols[-1]].sum()
                  - df.set_index(cat_col)[period_cols[0]] / df[period_cols[0]].sum()) * 100
        biggest_gain = shifts.idxmax()
        biggest_drop = shifts.idxmin()
        st.success(
            f"**Auto-insight:** From **{period_cols[0]}** to **{period_cols[-1]}**, "
            f"**{biggest_gain}**'s share grew the most ({shifts[biggest_gain]:+.1f} pts), "
            f"while **{biggest_drop}**'s share shrank the most ({shifts[biggest_drop]:+.1f} pts)."
        )

with st.expander("📝 Practice checklist"):
    st.checkbox("I can identify the largest and smallest slice at a glance")
    st.checkbox("I tried the 100% stacked bar version and can explain when it beats a pie chart")
    st.checkbox("I can articulate the known weakness of pie charts with many similar-sized slices")
    st.checkbox("I flagged a concentration risk (one slice being too dominant) if present")