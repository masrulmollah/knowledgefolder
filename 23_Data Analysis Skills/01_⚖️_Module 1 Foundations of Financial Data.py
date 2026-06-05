import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import random

# NO set_page_config() here — Homepage.py owns that call.
# ALL Streamlit commands are inside show(). Nothing runs at import time.

def _sec(title, icon=""):
    st.markdown(f"### {icon} {title}")
    st.markdown("---")

def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans: st.success("✅ Correct!")
        else: st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def show():
    st.title("📁 Module 1: Foundations of Financial Data")
    st.caption("Understand the data landscape before any analysis begins")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Data Explorer", "📊 Visualisation", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────
    with tab1:
        _sec("Financial Data Types", "🗂️")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Structured Financial Data**")
            st.dataframe(pd.DataFrame({
                "Type":      ["Balance Sheet","Income Statement","Cash Flow","Market Prices","Macro Indicators"],
                "Frequency": ["Quarterly/Annual","Quarterly/Annual","Quarterly/Annual","Daily/Real-time","Monthly"],
                "Source":    ["Company Filings","Company Filings","Company Filings","Exchanges","Central Banks"],
            }), use_container_width=True, hide_index=True)
        with c2:
            st.markdown("**Alternative & Unstructured Data**")
            st.markdown("""
- 📡 **Satellite imagery** — retail foot traffic, oil storage levels
- 🌐 **Web scraping** — pricing data, job postings, reviews
- 📱 **Social sentiment** — NLP on earnings call transcripts
- 💳 **Transaction data** — card spend patterns by merchant
- 🏭 **ESG data** — emissions reports, governance scores
            """)

        _sec("Data Quality Dimensions", "✅")
        st.dataframe(pd.DataFrame({
            "Dimension":       ["Completeness","Accuracy","Consistency","Timeliness","Lineage","Uniqueness"],
            "Definition":      ["No missing values in key fields","Data reflects true reality",
                                 "Same metric defined identically everywhere",
                                 "Available when needed for decisions",
                                 "Full audit trail from source to report",
                                 "No duplicate records inflating figures"],
            "Finance Example": ["All 12 months of revenue data present",
                                 "Revenue matches audited accounts",
                                 "EBITDA defined identically in Board and subsidiary reports",
                                 "Month-end close within 3 business days",
                                 "Trace any P&L line back to source GL entry",
                                 "Each invoice counted exactly once in AR"],
        }), use_container_width=True, hide_index=True)

        _sec("Data Structures", "🏗️")
        c1, c2, c3 = st.columns(3)
        with c1: st.info("**Time-Series**\n\nOne entity tracked over many time points.\n\nBest for: trends, seasonality, forecasting.\n\nExample: Monthly revenue 2019–2024.")
        with c2: st.info("**Cross-Sectional**\n\nMany entities at one point in time.\n\nBest for: benchmarking, comps, ranking.\n\nExample: EV/EBITDA of 50 companies at Dec-23.")
        with c3: st.info("**Panel / Longitudinal**\n\nMany entities over many periods.\n\nBest for: regression with fixed effects.\n\nExample: P&L of 50 subsidiaries over 5 years.")
        st.success("💡 Most modelling errors come from poor data foundations — mislabelled columns, inconsistent dates, duplicate rows. Always audit before you model.")

    # ── DATA EXPLORER ─────────────────────────────────────────────────
    with tab2:
        _sec("Interactive Dataset Builder & Quality Checker", "🧮")
        c1, c2, c3 = st.columns(3)
        with c1: n_cos   = st.slider("Number of companies", 5, 50, 20)
        with c2: n_yrs   = st.slider("Years of data", 2, 10, 5)
        with c3: add_iss = st.checkbox("Introduce data quality issues", value=True)

        np.random.seed(42)
        sectors = ["Technology","Consumer","Healthcare","Financials","Energy"]
        rows = []
        for co in [f"Co_{i:02d}" for i in range(1, n_cos + 1)]:
            sec = random.choice(sectors)
            rev = np.random.uniform(100, 5000)
            for yr in range(2024 - n_yrs + 1, 2025):
                rev *= np.random.uniform(0.85, 1.25)
                rows.append({"Company": co, "Sector": sec, "Year": yr,
                              "Revenue ($M)": round(rev, 1),
                              "EBITDA ($M)":  round(rev * np.random.uniform(0.08, 0.35), 1),
                              "Net Debt ($M)": round(np.random.uniform(-200, 3000), 1)})
        df = pd.DataFrame(rows)
        if add_iss:
            idx = np.random.choice(df.index, size=max(1, int(len(df)*0.05)), replace=False)
            df.loc[idx, "EBITDA ($M)"] = np.nan
            df = pd.concat([df, df.sample(3, random_state=1)], ignore_index=True)

        st.dataframe(df, use_container_width=True, height=260)
        c1, c2, c3 = st.columns(3)
        c1.metric("Total rows",     len(df))
        c2.metric("Missing values", int(df.isnull().sum().sum()))
        c3.metric("Duplicate rows", int(df.duplicated().sum()))

        st.markdown("**Automated Data Quality Report**")
        qr = pd.DataFrame({
            "Column":     list(df.columns),
            "Non-Null":   [df[c].notna().sum() for c in df.columns],
            "Null Count": [df[c].isna().sum()  for c in df.columns],
            "Null %":     [f"{df[c].isna().mean()*100:.1f}%" for c in df.columns],
            "Data Type":  [str(df[c].dtype) for c in df.columns],
        })
        st.dataframe(qr, use_container_width=True, hide_index=True)

    # ── VISUALISATION ──────────────────────────────────────────────────
    with tab3:
        _sec("Data Structures Visualised", "📊")
        viz = st.selectbox("Select structure to visualise", ["Time-Series","Cross-Sectional","Panel Data"])
        np.random.seed(7)
        if viz == "Time-Series":
            dates = pd.date_range("2019-01-01","2024-12-31", freq="QS")
            rev   = 1000 + np.cumsum(np.random.randn(len(dates))*30 + 15)
            fig   = go.Figure(go.Scatter(x=dates, y=rev, mode="lines+markers",
                                         line=dict(color="#185FA5", width=2)))
            fig.update_layout(title="Quarterly Revenue — Time-Series ($M)",
                              xaxis_title="Quarter", yaxis_title="Revenue ($M)",
                              template="plotly_white", height=380)
            st.plotly_chart(fig, use_container_width=True)
            st.caption("One company tracked over 24 quarters. Reveals trend, seasonality, and cycles.")
        elif viz == "Cross-Sectional":
            comps = [f"Co{i}" for i in range(1,16)]
            ev    = np.random.uniform(5,25,15)
            secs  = np.random.choice(["Tech","Consumer","Healthcare","Financials"],15)
            fig   = px.bar(x=comps, y=ev, color=secs,
                           title="EV/EBITDA Multiples at Dec-2024 — Cross-Sectional",
                           labels={"x":"Company","y":"EV/EBITDA","color":"Sector"},
                           template="plotly_white", height=380)
            st.plotly_chart(fig, use_container_width=True)
            st.caption("15 companies at one point in time. Best for benchmarking and relative valuation.")
        else:
            prows = []
            for co in ["Alpha Corp","Beta Ltd","Gamma Inc"]:
                base = np.random.uniform(200,800)
                for yr in range(2019,2025):
                    base *= np.random.uniform(0.9,1.2)
                    prows.append({"Company":co,"Year":yr,"Revenue":round(base,1)})
            fig = px.line(pd.DataFrame(prows), x="Year", y="Revenue", color="Company",
                          title="Revenue Panel Data — 3 Companies × 6 Years",
                          template="plotly_white", height=380, markers=True)
            st.plotly_chart(fig, use_container_width=True)
            st.caption("Multiple companies across multiple periods. Supports fixed-effects regression.")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Subsidiary P&L Data Audit — Unilever Asia Division", "🧪")

        st.markdown("""
**Business Situation:** You are the Regional FP&A Analyst for Asia. 
The month-end GL extract has just arrived from the ERP system for October 2024. 
Before building the management report, you must validate the data quality. 
Here is what the raw data looks like and what you find:
        """)

        # Simulate a realistic raw GL extract
        np.random.seed(10)
        months     = ["Oct-24"] * 20
        cost_cents = (["CC-101"]*7 + ["CC-102"]*6 + ["CC-103"]*7)
        gl_accts   = (["4001-Revenue","4002-Revenue","5001-COGS","5002-COGS","6001-SGA","6002-SGA","TOTAL_REV"]*2
                      + ["4001-Revenue","4002-Revenue","5001-COGS","5002-COGS","6001-SGA","6002-SGA"])[:20]
        amounts    = np.round(np.random.uniform(50, 800, 20), 1)

        raw_df = pd.DataFrame({
            "Month":       months,
            "Cost_Centre": cost_cents,
            "GL_Account":  gl_accts,
            "Amount ($K)": amounts,
            "Posted_By":   np.random.choice(["User_A","User_B","User_C"], 20),
        })

        # Introduce issues
        raw_df.loc[3, "Amount ($K)"] = np.nan   # missing value
        raw_df.loc[7, "Amount ($K)"] = np.nan   # missing value
        raw_df = pd.concat([raw_df, raw_df.iloc[[5]]], ignore_index=True)  # duplicate

        st.markdown("**Step 1 — Raw Data Extract (21 rows, as received from ERP)**")
        st.dataframe(raw_df, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — Data Quality Findings**")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total rows",     len(raw_df))
        col2.metric("Missing values", int(raw_df.isnull().sum().sum()),
                    delta="⚠️ 2 null amounts", delta_color="inverse")
        col3.metric("Duplicate rows", 1,
                    delta="⚠️ 1 duplicate found", delta_color="inverse")
        col4.metric("Rows after clean", len(raw_df.dropna().drop_duplicates()))

        st.markdown("**Step 3 — Null Value Location**")
        null_map = raw_df[raw_df["Amount ($K)"].isnull()][["Month","Cost_Centre","GL_Account","Posted_By"]]
        null_map["Issue"] = "❌ Missing Amount"
        st.dataframe(null_map, use_container_width=True, hide_index=True)
        st.warning("Action: Contact User_B to confirm the Oct-24 amounts for CC-101 GL 5002-COGS and CC-102 GL 5001-COGS before closing.")

        st.markdown("**Step 4 — After Cleaning: Revenue Reconciliation Check**")
        clean_df = raw_df.dropna().drop_duplicates().reset_index(drop=True)
        rev_lines  = clean_df[clean_df["GL_Account"].str.contains("Revenue")].groupby("Cost_Centre")["Amount ($K)"].sum().reset_index()
        rev_lines.columns = ["Cost_Centre","Calculated Revenue ($K)"]
        rev_lines["Reported Total ($K)"] = [412.5, 389.1, 441.8]
        rev_lines["Variance ($K)"]       = (rev_lines["Calculated Revenue ($K)"] - rev_lines["Reported Total ($K)"]).round(1)
        rev_lines["Status"] = rev_lines["Variance ($K)"].apply(lambda x: "✅ Match" if abs(x)<1 else "❌ Mismatch")
        st.dataframe(rev_lines, use_container_width=True, hide_index=True)

        st.markdown("**Step 5 — Data Quality Score Summary**")
        quality_df = pd.DataFrame({
            "Check":          ["Null values","Duplicates","Revenue reconciliation","Date format","GL mapping"],
            "Result":         ["2 nulls in Amount","1 duplicate row","CC-102 has $2.1K mismatch","✅ All dates valid","✅ All GL codes mapped"],
            "Severity":       ["High","Medium","High","Low","Low"],
            "Action Required":["Get corrected amounts from User_B",
                                "Remove duplicate — confirmed system glitch",
                                "Investigate CC-102 postings with local accountant",
                                "None","None"],
        })
        st.dataframe(quality_df, use_container_width=True, hide_index=True)
        st.error("⛔ Do NOT publish the management report until the 2 null amounts and the CC-102 revenue mismatch are resolved.")
        st.success("📌 Key Learning: A clean data audit before modelling prevents compounding errors downstream. In this case, publishing with nulls would have understated Asia COGS by an estimated $120K.")

    # ── QUIZ ──────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 1 Quiz", "❓")
        _quiz("1. Best data structure for comparing EV/EBITDA across 30 companies at one point in time?",
              ["Time-Series","Cross-Sectional","Panel Data","Unstructured"],
              "Cross-Sectional","m1q1")
        st.divider()
        _quiz("2. Which quality dimension ensures EBITDA is calculated the same way in every report?",
              ["Completeness","Accuracy","Consistency","Timeliness"],
              "Consistency","m1q2")
        st.divider()
        _quiz("3. Satellite imagery of retail car parks is an example of:",
              ["Structured financial data","Alternative data","Macro indicator data","Ledger data"],
              "Alternative data","m1q3")
        st.divider()
        _quiz("4. A revenue reconciliation finds that calculated totals differ from reported totals. Which quality dimension has failed?",
              ["Timeliness","Uniqueness","Accuracy","Lineage"],
              "Accuracy","m1q4")
        st.divider()
        _quiz("5. Panel data differs from time-series because:",
              ["It only has one time period",
               "It tracks multiple entities across multiple time periods",
               "It contains no numerical values","It is always unstructured"],
              "It tracks multiple entities across multiple time periods","m1q5")