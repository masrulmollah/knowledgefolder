"""
Module 9 — Area & Waterfall Charts: Cumulative Value and Bridges
==================================================================
Run standalone:
    streamlit run pages/9_🌊_Area_Waterfall_Charts.py
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Area & Waterfall Charts", page_icon="🌊", layout="wide")

st.title("🌊 Module 9: Area & Waterfall Charts — Cumulative Value and Bridges")

with st.expander("📌 When should you use these charts?", expanded=True):
    st.markdown(
        """
    **Stacked area charts** are for a numeric variable measured over time, broken into
    components, where you care about **both the trend and the composition** simultaneously
    (e.g., cumulative portfolio growth, split by holding).

    **Waterfall charts** are for explaining how you get from a **starting value to an
    ending value** through a sequence of positive and negative contributions — the
    classic finance example is a **P&L bridge** (Budget → Price effect → Volume effect →
    FX effect → Actual).
    """
    )

tab_area, tab_waterfall = st.tabs(["🌊 Area Chart", "🧱 Waterfall Chart"])

# ======================================================================
# AREA CHART
# ======================================================================
with tab_area:
    st.header("🛠️ Step 1 — Get data (Area Chart)")
    src = st.radio("Data source", ["Use sample data", "Upload my own CSV"], horizontal=True, key="area_src")

    @st.cache_data
    def make_area_sample(seed=6):
        rng = np.random.default_rng(seed)
        dates = pd.date_range(end=pd.Timestamp.today(), periods=36, freq="ME")
        holdings = ["Equities", "Bonds", "Cash", "Alternatives"]
        rows = []
        base = {"Equities": 40, "Bonds": 25, "Cash": 10, "Alternatives": 5}
        for d in dates:
            for h in holdings:
                growth = rng.normal(0.01, 0.03)
                base[h] = max(1, base[h] * (1 + growth))
                rows.append({"Date": d, "Holding": h, "Value ($M)": round(base[h], 2)})
        return pd.DataFrame(rows)

    if src == "Upload my own CSV":
        up = st.file_uploader("Upload a CSV with Date, Category, Value columns (long format)", type="csv", key="area_upload")
        if up is not None:
            area_df = pd.read_csv(up)
        else:
            st.info("No file uploaded yet — showing sample data below instead.")
            area_df = make_area_sample()
    else:
        area_df = make_area_sample()

    st.dataframe(area_df.head(8), use_container_width=True)

    cols = list(area_df.columns)
    st.header("🎛️ Step 2 — Build & edit the chart live")
    c1, c2, c3 = st.columns(3)
    with c1:
        date_col = st.selectbox("Date/sequence column", cols, key="area_date")
    with c2:
        cat_col = st.selectbox("Category column (stacked components)", cols, key="area_cat")
    with c3:
        val_col = st.selectbox("Value column", cols, key="area_val")

    normalize = st.checkbox("Normalize to 100% (show composition, not absolute values)", value=False)

    fig = px.area(
        area_df, x=date_col, y=val_col, color=cat_col,
        groupnorm="percent" if normalize else None,
    )
    fig.update_layout(height=500, legend=dict(orientation="h", yanchor="bottom", y=1.02))
    st.plotly_chart(fig, use_container_width=True)

    st.header("🔍 Step 3 — How to read this chart")
    st.markdown(
        """
    - **Total height** of the stack at any point = the sum across all categories at that time.
    - **Each band's thickness** = that category's value at that time.
    - A **growing band** = that component is gaining share/value; a shrinking band is losing it.
    - **Normalizing to 100%** removes the total's growth so you can focus purely on how the
      *mix* between categories evolves.
    """
    )

    st.header("💡 Step 4 — Extract the insight")
    latest = area_df[area_df[date_col] == area_df[date_col].max()]
    if not latest.empty:
        top_cat = latest.loc[latest[val_col].idxmax()]
        st.success(
            f"**Auto-insight:** As of the latest period, **{top_cat[cat_col]}** is the "
            f"largest component at **{top_cat[val_col]:,.1f}**."
        )

# ======================================================================
# WATERFALL CHART
# ======================================================================
with tab_waterfall:
    st.header("🛠️ Step 1 — Get data (Waterfall Chart)")
    st.caption("Define a starting value, a sequence of +/- contributions, and an ending value (or let it auto-total).")

    src_w = st.radio("Data source", ["Use sample data", "Upload my own CSV"], horizontal=True, key="wf_src")

    @st.cache_data
    def make_waterfall_sample():
        return pd.DataFrame({
            "Label": ["Budgeted Revenue", "Price Effect", "Volume Effect", "FX Effect", "One-off Cost", "Actual Revenue"],
            "Value": [500, 35, -20, 12, -8, None],
            "Type": ["absolute", "relative", "relative", "relative", "relative", "total"],
        })

    if src_w == "Upload my own CSV":
        up_w = st.file_uploader(
            "Upload a CSV with columns: Label, Value, Type (Type = absolute/relative/total)",
            type="csv", key="wf_upload",
        )
        if up_w is not None:
            wf_df = pd.read_csv(up_w)
        else:
            st.info("No file uploaded yet — showing sample data below instead.")
            wf_df = make_waterfall_sample()
    else:
        wf_df = make_waterfall_sample()

    edited = st.data_editor(wf_df, num_rows="dynamic", use_container_width=True, key="wf_editor")

    measures = edited["Type"].fillna("relative").tolist()
    values = edited["Value"].tolist()
    values = [0 if (pd.isna(v) and t != "total") else (v if not pd.isna(v) else 0) for v, t in zip(values, measures)]

    fig_wf = go.Figure(go.Waterfall(
        x=edited["Label"], measure=measures, y=values,
        connector={"line": {"color": "rgb(120,120,120)"}},
        increasing={"marker": {"color": "seagreen"}},
        decreasing={"marker": {"color": "indianred"}},
        totals={"marker": {"color": "steelblue"}},
    ))
    fig_wf.update_layout(height=500, showlegend=False)
    st.plotly_chart(fig_wf, use_container_width=True)

    st.header("🔍 Step 3 — How to read this chart")
    st.markdown(
        """
    - **Blue bars** ("absolute"/"total") are anchor points — a true starting or ending value,
      floating from zero.
    - **Green floating bars** are positive contributions that add to the running total.
    - **Red floating bars** are negative contributions that subtract from the running total.
    - Reading left to right **tells the whole story of "how we got from A to B"** — this is
      why waterfalls are the standard way to present budget-vs-actual or YoY bridges.
    """
    )

    st.header("💡 Step 4 — Extract the insight")
    relative_rows = edited[edited["Type"] == "relative"]
    if not relative_rows.empty:
        biggest_driver = relative_rows.loc[relative_rows["Value"].abs().idxmax()]
        st.success(
            f"**Auto-insight:** The single biggest driver of the bridge is "
            f"**{biggest_driver['Label']}** ({biggest_driver['Value']:+.1f}), "
            + ("a positive contributor." if biggest_driver["Value"] > 0 else "a drag on the total.")
        )

with st.expander("📝 Practice checklist"):
    st.checkbox("I can distinguish absolute/total bars (anchors) from relative bars (contributions) in a waterfall")
    st.checkbox("I identified the single biggest driver in a P&L-style bridge")
    st.checkbox("I can explain what a stacked area chart's thickness represents at any point in time")
    st.checkbox("I toggled the 100% normalization and can explain what changed in the story")