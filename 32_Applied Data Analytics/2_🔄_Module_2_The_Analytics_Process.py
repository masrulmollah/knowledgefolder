import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Module 2 — The Analytics Process", page_icon="🔄", layout="wide")

st.title("🔄 Module 2: The Data Analytics Process")
st.caption("Learning goal: internalize a repeatable, end-to-end workflow for any analytics problem.")

st.markdown(
    """
Good analytics isn't a single technique — it's a **process**. Miss a step (like cleaning
the data, or clearly defining the objective) and even the fanciest model will mislead you.
"""
)

steps = [
    ("1. Define the objective", "State the business question precisely. 'Sales are down' is not a question — "
                                  "'Why did Q2 gross margin fall 3pts vs Q1, and is it structural or one-off?' is."),
    ("2. Collect the data", "Identify and pull the data sources needed: GL, budget files, transaction data, market data."),
    ("3. Clean & prepare", "Handle missing values, duplicates, outliers and inconsistent formats before analyzing."),
    ("4. Explore (EDA)", "Look at distributions, trends and relationships before modeling — let the data surprise you."),
    ("5. Analyze", "Apply the right technique: ratios, variance, regression, simulation, optimization."),
    ("6. Interpret", "Translate numbers into a business meaning: is this good, bad, expected, actionable?"),
    ("7. Communicate", "Present findings clearly — the right chart, the right level of detail, for the right audience."),
    ("8. Act / Decide", "Turn the insight into a decision or recommendation."),
    ("9. Monitor", "Track the outcome of the decision and feed it back into future analysis."),
]

st.markdown("## 🗺️ The 9-Step Process")
cols = st.columns(3)
for i, (name, desc) in enumerate(steps):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{name}**")
            st.caption(desc)

st.divider()

# ----------------------------------------------------------------------------
# INTERACTIVE EXERCISE: DATA CLEANING
# ----------------------------------------------------------------------------
st.markdown("## 🧹 Interactive Exercise — Step 3: Clean the Data")
st.markdown(
    "Below is a **messy** monthly expense extract. Toggle the cleaning steps and watch "
    "the dataset (and the resulting insight) change."
)

raw = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Mar", "Apr", "May", "Jun"],
    "Marketing_Expense": [12000, 11500, np.nan, 13000, 13000, 145000, 12800],
    "Travel_Expense": [3200, 3100, 3300, 3300, np.nan, 3500, 3400],
})
st.markdown("**Raw extract from the system:**")
st.dataframe(raw, use_container_width=True)

c1, c2, c3 = st.columns(3)
fix_dupes = c1.checkbox("Remove duplicate rows (duplicate 'Mar' entry)", value=False)
fix_missing = c2.checkbox("Fill missing values (with column median)", value=False)
fix_outlier = c3.checkbox("Fix outlier (May Marketing = 145,000 looks like a data-entry error)", value=False)

clean = raw.copy()
if fix_dupes:
    clean = clean.drop_duplicates(subset="Month", keep="first")
if fix_missing:
    clean["Marketing_Expense"] = clean["Marketing_Expense"].fillna(clean["Marketing_Expense"].median())
    clean["Travel_Expense"] = clean["Travel_Expense"].fillna(clean["Travel_Expense"].median())
if fix_outlier:
    med = clean["Marketing_Expense"].median()
    clean.loc[clean["Marketing_Expense"] > med * 3, "Marketing_Expense"] = med

st.markdown("**Cleaned dataset:**")
st.dataframe(clean, use_container_width=True)

avg_before = raw["Marketing_Expense"].mean(skipna=True)
avg_after = clean["Marketing_Expense"].mean(skipna=True)
st.metric("Average monthly Marketing Expense", f"${avg_after:,.0f}",
          delta=f"{avg_after - avg_before:,.0f} vs uncleaned data")

if fix_dupes and fix_missing and fix_outlier:
    st.success(
        "Notice how the average swings wildly depending on whether you clean the data first. "
        "This is exactly why Step 3 comes *before* Step 5 (Analyze) — never analyze raw, unchecked data."
    )
else:
    st.warning("Try toggling all three checkboxes on to see how much the 'average expense' figure changes.")

st.divider()

# ----------------------------------------------------------------------------
# MINI CASE WALKTHROUGH
# ----------------------------------------------------------------------------
st.markdown("## 📂 Mini Case: Applying the Process")
st.markdown(
    """
**Scenario:** You're the finance manager at a mid-size distributor. Gross margin fell from
42% to 39% last quarter. Walk through how the process applies:
"""
)
tabs = st.tabs(["1. Define", "2-3. Collect & Clean", "4. Explore", "5-6. Analyze & Interpret", "7-9. Communicate, Act, Monitor"])
with tabs[0]:
    st.markdown("**Objective:** *Why did gross margin fall 3 points in Q2, and is it likely to persist in Q3?*")
with tabs[1]:
    st.markdown("Pull GL detail by product line, standard costs, and actual purchase prices. "
                "Check for missing product-line tags, duplicated invoice lines, and one-off write-offs.")
with tabs[2]:
    st.markdown("Plot margin by product line and by month. You notice one product line's margin "
                "collapsed in month 2 of the quarter — everything else is stable.")
with tabs[3]:
    st.markdown("Diagnostic analytics (Module 4) shows a supplier price increase hit that one "
                "product line without a matching price increase to customers — a **structural**, not one-off, issue.")
with tabs[4]:
    st.markdown("Recommend either a selling-price adjustment or supplier renegotiation "
                "(Prescriptive, Module 7); monitor margin by product line monthly going forward.")

st.divider()
st.info("➡️ Next: **Module 3 — Descriptive Analytics**, where you'll compute and interpret financial ratios interactively.")
