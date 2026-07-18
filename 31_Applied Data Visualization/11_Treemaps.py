"""
Module 10 — Treemaps: Hierarchical Composition at Scale
==========================================================
Run standalone:
    streamlit run pages/10_🗂️_Treemaps.py
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Treemaps", page_icon="🗂️", layout="wide")

st.title("🗂️ Module 10: Treemaps — Hierarchical Composition at Scale")

with st.expander("📌 When should you use a treemap?", expanded=True):
    st.markdown(
        """
    Use a **treemap** when you have:
    - A **hierarchy** (e.g., sector → company, or fund family → strategy → fund)
    - A **sizing metric** (market cap, AUM, revenue) that varies a lot in magnitude
    - Optionally, a **second metric** (like return) you want to overlay as color

    Typical finance examples: index composition by sector and constituent, AUM by
    strategy and fund, expenses by department and line item.

    Treemaps handle **many more categories** than a pie chart can, because area — not
    angle — encodes magnitude, and rectangles pack efficiently regardless of count.
    """
    )

st.divider()

st.header("🛠️ Step 1 — Get data")
src = st.radio("Choose a data source", ["Use sample data", "Upload my own CSV"], horizontal=True)

@st.cache_data
def make_sample_data(seed=13):
    rng = np.random.default_rng(seed)
    sector_companies = {
        "Technology": ["AlphaSoft", "NanoChip", "CloudNet", "DataForge"],
        "Financials": ["FirstNat Bank", "Capital Trust", "Meridian Ins."],
        "Healthcare": ["BioGen Labs", "MedCore", "PharmaPlus"],
        "Energy": ["PetroWest", "SolarGrid", "GasCo"],
        "Consumer": ["RetailMax", "FoodChain Co", "BrandWorks"],
    }
    rows = []
    for sector, companies in sector_companies.items():
        for c in companies:
            market_cap = rng.uniform(5, 300)
            ret = rng.normal(4, 12)
            rows.append({"Sector": sector, "Company": c, "Market Cap ($B)": round(market_cap, 1), "YTD Return (%)": round(ret, 1)})
    return pd.DataFrame(rows)

if src == "Upload my own CSV":
    up = st.file_uploader("Upload a CSV with one or more hierarchy columns and a numeric size column", type="csv")
    if up is not None:
        df = pd.read_csv(up)
    else:
        st.info("No file uploaded yet — showing sample data below instead.")
        df = make_sample_data()
else:
    df = make_sample_data()

cat_cols = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
st.dataframe(df.head(10), use_container_width=True)

st.header("🎛️ Step 2 — Build & edit the chart live")
c1, c2, c3 = st.columns(3)
with c1:
    hierarchy = st.multiselect(
        "Hierarchy levels (order matters: broadest first)", cat_cols,
        default=cat_cols[: min(2, len(cat_cols))],
    )
with c2:
    size_col = st.selectbox("Size by", num_cols, index=0 if num_cols else None)
with c3:
    color_col = st.selectbox("Color by (optional, e.g. a performance metric)", ["(none)"] + num_cols)

if not hierarchy:
    st.warning("Select at least one hierarchy level.")
    st.stop()

color = None if color_col == "(none)" else color_col
fig = px.treemap(
    df, path=hierarchy, values=size_col, color=color,
    color_continuous_scale="RdYlGn" if color else None,
    color_continuous_midpoint=0 if color else None,
)
fig.update_layout(height=600, margin=dict(t=30, l=10, r=10, b=10))
st.plotly_chart(fig, use_container_width=True)

st.header("🔍 Step 3 — How to read this chart")
st.markdown(
    """
- **Rectangle area** = magnitude of the sizing metric — bigger box = bigger value.
- **Nesting** shows hierarchy — a large box divided into smaller boxes shows how a
  category breaks down into sub-categories.
- If you added a **color metric**, it typically overlays performance — e.g., green boxes
  are outperforming, red boxes are underperforming — letting you spot "big AND
  underperforming" (a red flag) at a glance.
- **Click into a box** in the live chart to zoom into that branch of the hierarchy.
"""
)

st.header("💡 Step 4 — Extract the insight")
top_level = hierarchy[0]
by_top = df.groupby(top_level)[size_col].sum().sort_values(ascending=False)
biggest = by_top.index[0]
share = by_top.iloc[0] / by_top.sum() * 100

msg = (
    f"**Auto-insight:** **{biggest}** is the largest group by {size_col}, "
    f"representing **{share:.1f}%** of the total shown."
)
if color:
    entity_col = hierarchy[-1]
    big_and_bad = df[(df[size_col] > df[size_col].median()) & (df[color] < 0)]
    if not big_and_bad.empty:
        flagged = big_and_bad.sort_values(size_col, ascending=False).iloc[0]
        msg += (
            f" Watch **{flagged[entity_col]}** — it's above-median in size but has a "
            f"negative {color} ({flagged[color]:.1f}), a large position dragging on performance."
        )
st.success(msg)

with st.expander("📝 Practice checklist"):
    st.checkbox("I can tell which category dominates just from box size")
    st.checkbox("I can navigate the hierarchy (zoom into a sector to see its constituents)")
    st.checkbox("I added a color metric and identified a 'large but underperforming' entity")
    st.checkbox("I can explain why a treemap scales to more categories better than a pie chart")