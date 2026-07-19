"""
Applied Data Visualization for Finance Professionals
=====================================================
OVERVIEW / HOME PAGE

This is the entry point of a multi-page Streamlit app. Every module lives
in its own file inside the `pages/` folder, and Streamlit automatically
turns each one into a page in the left sidebar navigation.

Run with:
    streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="Applied Data Visualization for Finance",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------
st.title("📊 Applied Data Visualization for Finance Professionals")
st.markdown(
    """
Welcome. This section teaches you how to turn raw financial data into
charts that **decision-makers can actually read and act on**.

Every module below follows the same four-step learning loop:

1. **Which data fits this chart?** — the data shapes and finance use-cases the chart is built for
2. **How is it built?** — you construct it live, tweaking real parameters
3. **How do you read it?** — an annotated guide to interpreting the axes, encodings, and shapes
4. **What insight can you pull out?** — a guided exercise using your own uploaded data or a sample dataset

Use the sidebar to jump into any module. Each module lets you **upload your own CSV**,
edit the chart's parameters live, and see the visualization update instantly.
"""
)

st.divider()

# ----------------------------------------------------------------------
# SYLLABUS
# ----------------------------------------------------------------------
st.header("🗺️ Course Syllabus")

modules = [
    {
        "no": "01",
        "title": "Line Charts — Time Series & Trend Analysis",
        "icon": "📈",
        "data": "Stock prices, index levels, interest rates, revenue over time — any single continuous variable measured repeatedly over time.",
        "learn": "Plotting single/multi-series time series, moving averages, rebasing to 100, log vs linear scale, annotating events.",
        "read": "Slope = rate of change, crossovers between lines, divergence between two series, volatility as line 'noisiness'.",
        "insight": "Detect trend reversals, compare relative performance of two assets, spot momentum shifts.",
    },
    {
        "no": "02",
        "title": "Bar & Column Charts — Comparing Categories",
        "icon": "📊",
        "data": "Revenue by segment/region, YoY growth by quarter, headcount by department — categorical comparisons.",
        "learn": "Vertical vs horizontal bars, grouped vs stacked bars, sorting for readability, adding value labels.",
        "read": "Bar length = magnitude, stacked segments = composition, grouped bars = side-by-side comparison across a second category.",
        "insight": "Rank business units by contribution, spot which segment drives total growth, compare period-over-period changes.",
    },
    {
        "no": "03",
        "title": "Histograms & Distribution Plots — Understanding Spread and Risk",
        "icon": "📉",
        "data": "Daily/monthly returns, P&L outcomes, loan default scores — any single numeric variable's distribution.",
        "learn": "Choosing bin width, overlaying a normal curve, switching between histogram / KDE / density plots.",
        "read": "Shape (normal, skewed, fat-tailed), spread (std dev), central tendency (mean/median), tail risk.",
        "insight": "Quantify downside risk, detect skewness/fat tails in returns, compare risk profiles of two assets.",
    },
    {
        "no": "04",
        "title": "Scatter Plots — Relationships & Correlation",
        "icon": "🔵",
        "data": "Risk vs return by asset, beta vs alpha, valuation multiple vs growth rate — two continuous variables per entity.",
        "learn": "Adding trendlines/regression, sizing/coloring points by a third variable (bubble charts), log scales.",
        "read": "Direction and tightness of the point cloud = correlation strength, outliers, clusters of similar assets.",
        "insight": "Identify over/undervalued assets relative to a trend line, find diversification candidates with low correlation.",
    },
    {
        "no": "05",
        "title": "Box Plots — Comparing Spread Across Groups",
        "icon": "📦",
        "data": "Return distributions across sectors, volatility across fund managers, deal sizes across years.",
        "learn": "Reading quartiles, whiskers, outlier points; grouping by category; switching to violin plots.",
        "read": "Median line, IQR box (middle 50%), whisker range, outlier dots beyond 1.5×IQR.",
        "insight": "Compare consistency/volatility across groups, spot outlier events, rank groups by median performance.",
    },
    {
        "no": "06",
        "title": "Heatmaps & Correlation Matrices",
        "icon": "🔥",
        "data": "Asset correlation matrices, monthly seasonality tables, sector performance grids.",
        "learn": "Building a correlation matrix from raw price/return data, choosing color scales, clustering/reordering rows.",
        "read": "Color intensity = magnitude, diagonal = self-correlation, symmetric halves in correlation matrices.",
        "insight": "Find highly correlated assets to avoid concentration risk, detect seasonal patterns.",
    },
    {
        "no": "07",
        "title": "Candlestick & OHLC Charts — Price Action",
        "icon": "🕯️",
        "data": "Daily/intraday Open-High-Low-Close price data for equities, FX, commodities.",
        "learn": "Constructing candlesticks from OHLC data, adding volume bars, overlaying moving averages.",
        "read": "Candle body = open/close range, wicks = intraday high/low, color = up/down day, patterns (doji, engulfing).",
        "insight": "Spot momentum and reversal patterns, gauge intraday volatility, confirm trend with volume.",
    },
    {
        "no": "08",
        "title": "Pie, Donut & 100% Stacked Charts — Composition",
        "icon": "🥧",
        "data": "Portfolio allocation, revenue mix by product line, expense breakdown — parts of a whole.",
        "learn": "When a pie chart is appropriate vs when it misleads, donut variants, converting to a 100% stacked bar for comparison across time.",
        "read": "Slice angle/area = share of total; comparing many similar-sized slices is hard — this is called out explicitly.",
        "insight": "Identify concentration risk in a portfolio, track how a mix shifts across two periods.",
    },
    {
        "no": "09",
        "title": "Area & Waterfall Charts — Cumulative Value and Bridges",
        "icon": "🌊",
        "data": "Cumulative portfolio growth, stacked cumulative revenue, P&L bridge from budget to actual.",
        "learn": "Stacked area charts for cumulative composition over time; waterfall charts for sequential positive/negative contributions.",
        "read": "Area thickness = magnitude at a point in time; in a waterfall, floating bars show incremental additions/subtractions to a running total.",
        "insight": "Explain a variance (e.g., budget vs actual) driver-by-driver, see how each holding contributes to portfolio growth.",
    },
    {
        "no": "10",
        "title": "Treemaps — Hierarchical Composition at Scale",
        "icon": "🗂️",
        "data": "Market cap by sector and company, AUM by strategy and fund, expenses by department and line item.",
        "learn": "Building nested hierarchies, sizing rectangles by one metric and coloring by another (e.g., size = market cap, color = return).",
        "read": "Rectangle area = magnitude of the sizing metric, color = a second metric (often performance), nesting = hierarchy level.",
        "insight": "Spot which few names dominate an index, find pockets of over/underperformance within a sector.",
    },
]

for m in modules:
    with st.container(border=True):
        c1, c2 = st.columns([0.08, 0.92])
        with c1:
            st.markdown(f"### {m['icon']}")
            st.markdown(f"**Module {m['no']}**")
        with c2:
            st.markdown(f"#### {m['title']}")
            t1, t2, t3, t4 = st.tabs(["📌 When to use", "🛠️ How it's built", "🔍 How to read it", "💡 Insight focus"])
            with t1:
                st.write(m["data"])
            with t2:
                st.write(m["learn"])
            with t3:
                st.write(m["read"])
            with t4:
                st.write(m["insight"])

st.divider()

# ----------------------------------------------------------------------
# HOW TO USE
# ----------------------------------------------------------------------
st.header("🎯 How Each Module Works")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("1. Upload or sample")
    st.write("Upload your own CSV, or use the built-in sample finance dataset to start immediately.")
with col2:
    st.subheader("2. Tune it live")
    st.write("Sidebar controls let you change chart type, aggregation, colors, and encodings in real time.")
with col3:
    st.subheader("3. Read the chart")
    st.write("An annotated 'how to read this' panel sits next to every chart you build.")
with col4:
    st.subheader("4. Extract insight")
    st.write("Guided prompts and auto-computed stats help you practice pulling a conclusion, not just a picture.")

st.divider()
st.info(
    "👈 **Start with Module 1 (Line Charts)** in the sidebar, or jump to whichever "
    "chart type is most relevant to your current work."
)