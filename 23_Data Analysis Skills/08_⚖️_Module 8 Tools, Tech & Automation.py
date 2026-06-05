import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# ══════════════════════════════════════════════════════════════════════════════
# NO st.set_page_config() in this file — ever.
# Homepage.py owns that call.
# ALL Streamlit commands live inside show().
# Nothing executes at import or exec_module time.
# ══════════════════════════════════════════════════════════════════════════════

def _sec(title, icon=""):
    st.markdown(f"### {icon} {title}")
    st.markdown("---")

def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def show():
    st.title("🛠️ Module 8: Tools, Tech & Automation")
    st.caption("The technical stack every modern finance analyst needs")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Python Demo", "📊 SQL Patterns",
        "🧪 Worked Example", "❓ Quiz",
    ])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("The Modern Finance Tech Stack", "🏗️")
        st.dataframe(pd.DataFrame({
            "Layer":          ["Data Sources","Data Storage","Data Processing",
                                "Analysis","Visualisation","Automation"],
            "Tools":          ["Bloomberg, Refinitiv, SAP/Oracle ERP, APIs",
                                "Snowflake, BigQuery, Azure Data Lake",
                                "Python (Pandas), SQL, Power Query, dbt",
                                "Python (NumPy, sklearn), Excel, R",
                                "Power BI, Tableau, Plotly/Dash, Streamlit",
                                "Python scripts, Azure Functions, Power Automate"],
            "Finance Use":    ["Pull market data, load ERP extracts",
                                "Central store for models and reporting data",
                                "Clean, transform, join financial datasets",
                                "Statistical models, forecasting, scenario analysis",
                                "Dashboards, management reports, ad-hoc charts",
                                "Scheduled reports, email alerts, reconciliations"],
        }), use_container_width=True, hide_index=True)

        _sec("Python Essentials for Finance", "🐍")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
**Data Manipulation — Pandas**
```python
# Group and summarise
df.groupby("Division")["Revenue"].sum()

# Reshape long → wide
df.pivot_table(
    index="Year",
    columns="Division",
    values="EBITDA",
)

# Time-series resampling
df.resample("QS").sum()

# YoY growth
df["YoY"] = (
  df.groupby("Div")["Rev"]
    .pct_change(12) * 100
)
```
            """)
        with c2:
            st.markdown("""
**Statistical Analysis**
```python
import statsmodels.api as sm

# OLS regression
X = sm.add_constant(X_vars)
model = sm.OLS(y, X).fit()
print(model.summary())

# Rolling statistics
df["MA_3M"]  = df["Rev"].rolling(3).mean()
df["MA_12M"] = df["Rev"].rolling(12).mean()

# Outlier detection
z = (df["cost"] - df["cost"].mean()
    ) / df["cost"].std()
anomalies = df[z.abs() > 2.5]
```
            """)
        with c3:
            st.markdown("""
**Visualisation — Plotly**
```python
import plotly.graph_objects as go

# Waterfall chart
fig = go.Figure(go.Waterfall(
    measure=measures,
    x=labels,
    y=values,
))

# Interactive line chart
fig = px.line(
    df, x="Date", y="Revenue",
    facet_col="Division",
    template="plotly_white",
)
```
            """)

        _sec("SQL Window Functions for Finance", "🗄️")
        st.markdown("""
Window functions are the single most powerful SQL skill for finance analysts.
They let you calculate running totals, YoY growth, and rankings **without collapsing rows**.

```sql
-- Year-over-Year growth using LAG()
SELECT
    company,
    fiscal_year,
    revenue,
    LAG(revenue, 1) OVER (
        PARTITION BY company
        ORDER BY fiscal_year
    ) AS prior_year_revenue,
    ROUND(
        (revenue - LAG(revenue,1) OVER (PARTITION BY company ORDER BY fiscal_year))
        / NULLIF(LAG(revenue,1) OVER (PARTITION BY company ORDER BY fiscal_year), 0) * 100
    , 2) AS yoy_growth_pct
FROM financial_data.income_statement
ORDER BY company, fiscal_year;

-- Running YTD cumulative revenue
SELECT month, monthly_revenue,
    SUM(monthly_revenue) OVER (
        PARTITION BY fiscal_year
        ORDER BY month
        ROWS UNBOUNDED PRECEDING
    ) AS ytd_revenue
FROM monthly_revenue;
```
        """)

    # ── PYTHON DEMO ───────────────────────────────────────────────────────────
    with tab2:
        _sec("Live Python / Pandas Financial Data Demo", "🧮")
        op = st.selectbox("Select operation to see", [
            "Group by & aggregation",
            "Pivot table — P&L by Division × Year",
            "Year-over-Year growth calculation",
            "Rolling average & trend detection",
            "Outlier detection (Z-score)",
        ])

        np.random.seed(42)
        divs  = ["APAC","EMEA","Americas"]
        years = [2021,2022,2023,2024]
        rows  = []
        for d in divs:
            base = {"APAC":300,"EMEA":450,"Americas":600}[d]
            for y in years:
                rev = base*(1.08**(y-2021))*np.random.uniform(0.92,1.08)
                rows.append({"Division":d,"Year":y,
                              "Revenue":round(rev,1),
                              "EBITDA":round(rev*np.random.uniform(0.18,0.30),1)})
        df = pd.DataFrame(rows)

        if op == "Group by & aggregation":
            st.markdown("**Operation:** `df.groupby('Division').agg(...)` — sum revenue and average EBITDA per division")
            result = df.groupby("Division").agg(
                Total_Revenue=("Revenue","sum"),
                Avg_EBITDA=("EBITDA","mean"),
                Years=("Year","count"),
            ).round(1).reset_index()
            st.dataframe(result, use_container_width=True, hide_index=True)
            fig = go.Figure(go.Bar(x=result["Division"], y=result["Total_Revenue"],
                                   marker_color="#185FA5",
                                   text=[f"${v:.0f}M" for v in result["Total_Revenue"]],
                                   textposition="outside"))
            fig.update_layout(title="Total Revenue by Division ($M)",
                              template="plotly_white", height=320)
            st.plotly_chart(fig, use_container_width=True)

        elif op == "Pivot table — P&L by Division × Year":
            st.markdown("**Operation:** `df.pivot_table(index='Division', columns='Year', values='Revenue')` — classic P&L matrix view")
            pivot = df.pivot_table(index="Division", columns="Year",
                                   values="Revenue", aggfunc="sum").round(1)
            st.dataframe(pivot, use_container_width=True)
            fig = px.bar(df, x="Year", y="Revenue", color="Division",
                         barmode="group", title="Revenue by Division and Year ($M)",
                         template="plotly_white", height=360)
            st.plotly_chart(fig, use_container_width=True)

        elif op == "Year-over-Year growth calculation":
            st.markdown("**Operation:** `groupby().shift(1)` to get prior year, then calculate % change")
            ds = df.sort_values(["Division","Year"]).copy()
            ds["Prior_Year_Rev"] = ds.groupby("Division")["Revenue"].shift(1)
            ds["YoY_%"]          = ((ds["Revenue"]/ds["Prior_Year_Rev"]-1)*100).round(1)
            display_cols = ["Division","Year","Revenue","Prior_Year_Rev","YoY_%"]
            st.dataframe(ds[display_cols].dropna(), use_container_width=True, hide_index=True)
            fig = px.line(ds.dropna(), x="Year", y="YoY_%", color="Division",
                          markers=True, title="Year-on-Year Revenue Growth (%)",
                          template="plotly_white", height=360)
            fig.add_hline(y=0, line_dash="dash", line_color="black")
            st.plotly_chart(fig, use_container_width=True)

        elif op == "Rolling average & trend detection":
            st.markdown("**Operation:** `rolling(N).mean()` — smooth out noise to reveal the underlying trend")
            monthly = pd.Series(
                np.random.normal(100 + np.arange(36)*0.8, 5, 36),
                index=pd.date_range("2022-01-01", periods=36, freq="MS"),
            )
            fig = go.Figure()
            fig.add_trace(go.Bar(x=monthly.index, y=monthly,
                                 name="Monthly", marker_color="#B0C4DE", opacity=0.6))
            fig.add_trace(go.Scatter(x=monthly.index, y=monthly.rolling(3).mean(),
                                     name="3M Moving Avg",
                                     line=dict(color="#E24B4A",dash="dash",width=2)))
            fig.add_trace(go.Scatter(x=monthly.index, y=monthly.rolling(12).mean(),
                                     name="12M Moving Avg",
                                     line=dict(color="#185FA5",width=2.5)))
            fig.update_layout(title="Revenue with Rolling Averages ($M)",
                              template="plotly_white", height=380,
                              legend=dict(orientation="h",y=1.02))
            st.plotly_chart(fig, use_container_width=True)
            st.caption("The 12M moving average strips out seasonality and noise to show the true trend direction.")

        else:  # Outlier detection
            st.markdown("**Operation:** Z-score method — flag transactions more than 2.5 standard deviations from the mean")
            np.random.seed(10)
            costs = np.random.normal(50, 8, 100)
            costs[15]=120; costs[42]=18; costs[77]=135   # inject anomalies
            z_scores   = (costs - costs.mean()) / costs.std()
            is_outlier = np.abs(z_scores) > 2.5
            fig = go.Figure(go.Scatter(
                x=list(range(len(costs))), y=costs, mode="markers",
                marker=dict(
                    color=["#E24B4A" if o else "#185FA5" for o in is_outlier],
                    size=[14 if o else 6 for o in is_outlier],
                    symbol=["diamond" if o else "circle" for o in is_outlier],
                )))
            fig.add_hline(y=costs.mean()+2.5*costs.std(), line_dash="dash",
                          line_color="red", annotation_text="+2.5σ threshold")
            fig.add_hline(y=costs.mean()-2.5*costs.std(), line_dash="dash",
                          line_color="red", annotation_text="-2.5σ threshold")
            fig.update_layout(
                title=f"Outlier Detection — {is_outlier.sum()} flagged (red diamonds) of {len(costs)} transactions",
                xaxis_title="Transaction #", yaxis_title="Unit Cost ($)",
                template="plotly_white", height=380)
            st.plotly_chart(fig, use_container_width=True)
            flagged_df = pd.DataFrame({
                "Transaction #": [i+1 for i,o in enumerate(is_outlier) if o],
                "Unit Cost ($)":  [round(costs[i],1) for i,o in enumerate(is_outlier) if o],
                "Z-Score":        [round(z_scores[i],2) for i,o in enumerate(is_outlier) if o],
                "Action":         ["Investigate — spot market purchase?" for _ in range(is_outlier.sum())],
            })
            st.dataframe(flagged_df, use_container_width=True, hide_index=True)

    # ── SQL PATTERNS ──────────────────────────────────────────────────────────
    with tab3:
        _sec("SQL Query Pattern Library", "📊")
        pattern = st.selectbox("Select pattern", [
            "YoY growth with LAG()",
            "Running YTD cumulative",
            "Sector ranking by EBITDA margin",
            "Budget vs Actual variance report",
        ])
        sqls = {
            "YoY growth with LAG()": """-- Year-over-Year Revenue Growth
SELECT
    company,
    fiscal_year,
    revenue,
    LAG(revenue, 1) OVER (
        PARTITION BY company
        ORDER BY fiscal_year
    ) AS prior_year_revenue,
    ROUND(
        (revenue
         - LAG(revenue,1) OVER (PARTITION BY company ORDER BY fiscal_year))
        / NULLIF(
            LAG(revenue,1) OVER (PARTITION BY company ORDER BY fiscal_year)
          , 0) * 100
    , 2) AS yoy_growth_pct
FROM income_statement
WHERE fiscal_year BETWEEN 2020 AND 2024
ORDER BY company, fiscal_year;""",

            "Running YTD cumulative": """-- Running YTD Revenue with % of Full-Year Total
SELECT
    fiscal_year,
    month,
    monthly_revenue,
    SUM(monthly_revenue) OVER (
        PARTITION BY fiscal_year
        ORDER BY month
        ROWS UNBOUNDED PRECEDING
    ) AS ytd_revenue,
    ROUND(
        SUM(monthly_revenue) OVER (
            PARTITION BY fiscal_year
            ORDER BY month
        ) / SUM(monthly_revenue) OVER (
            PARTITION BY fiscal_year
        ) * 100
    , 1) AS ytd_pct_of_full_year
FROM monthly_revenue
ORDER BY fiscal_year, month;""",

            "Sector ranking by EBITDA margin": """-- Rank Companies by EBITDA Margin Within Sector
SELECT
    company,
    sector,
    revenue,
    ebitda,
    ROUND(ebitda / NULLIF(revenue, 0) * 100, 1) AS ebitda_margin_pct,
    RANK() OVER (
        PARTITION BY sector
        ORDER BY ebitda / NULLIF(revenue, 0) DESC
    ) AS rank_in_sector,
    ROUND(
        AVG(ebitda / NULLIF(revenue, 0))
            OVER (PARTITION BY sector) * 100
    , 1) AS sector_avg_margin_pct
FROM company_financials
WHERE fiscal_year = 2024
ORDER BY sector, rank_in_sector;""",

            "Budget vs Actual variance report": """-- Budget vs Actual with Significance Flag
SELECT
    d.division_name,
    a.gl_account_desc,
    b.budget_amount,
    a.actual_amount,
    a.actual_amount - b.budget_amount
        AS variance_amount,
    ROUND(
        (a.actual_amount - b.budget_amount)
        / NULLIF(ABS(b.budget_amount), 0) * 100
    , 1) AS variance_pct,
    CASE
        WHEN ABS(
            (a.actual_amount - b.budget_amount)
            / NULLIF(ABS(b.budget_amount), 0)
        ) > 0.10 THEN 'Significant Variance'
        ELSE 'Within Tolerance'
    END AS flag
FROM actuals a
JOIN budget    b  ON a.cost_centre = b.cost_centre
                 AND a.gl_account  = b.gl_account
JOIN divisions d  ON a.cost_centre = d.cost_centre
WHERE a.fiscal_period = '2024-Q3'
ORDER BY ABS(variance_amount) DESC;""",
        }
        st.code(sqls[pattern], language="sql")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Automating the Month-End Management Pack — FMCG Company", "🧪")

        st.markdown("""
**Business Situation:** You are Senior Finance Analyst at a fast-moving consumer goods company.
Every month-end you manually spend **4 hours** copying numbers from the ERP extract into Excel,
calculating variances, and emailing the management pack. You automate the entire process.

Here is what the automation produces — **in under 2 minutes.**
        """)

        st.markdown("**Output 1 — Automated P&L Summary (from GL Extract)**")
        np.random.seed(5)
        divs_pnl   = ["APAC","EMEA","Americas","MEA"]
        pnl_lines  = ["Revenue","COGS","Gross Profit","SG&A","EBITDA"]
        budget_vals= {
            "Revenue":      [155, 162, 158, 25],
            "COGS":         [-68, -71, -70, -11],
            "Gross Profit": [87,  91,  88,  14],
            "SG&A":         [-32, -36, -35,  -5],
            "EBITDA":       [55,  55,  53,   9],
        }
        actual_vals= {
            "Revenue":      [148, 165, 142, 27],
            "COGS":         [-71, -70, -77, -11],
            "Gross Profit": [77,  95,  65,  16],
            "SG&A":         [-33, -35, -42,  -5],
            "EBITDA":       [44,  60,  23,  11],
        }
        pnl_rows = []
        for line in pnl_lines:
            row = {"P&L Line": line}
            for i, div in enumerate(divs_pnl):
                b = budget_vals[line][i]
                a = actual_vals[line][i]
                row[f"{div} Budget"] = b
                row[f"{div} Actual"] = a
                row[f"{div} Var"]    = a - b
            pnl_rows.append(row)
        pnl_df = pd.DataFrame(pnl_rows)
        st.dataframe(pnl_df, use_container_width=True, hide_index=True)

        st.markdown("**Output 2 — EBITDA Bridge: Budget to Actual (Total Group)**")
        total_b_rev  = sum(budget_vals["Revenue"])
        total_a_rev  = sum(actual_vals["Revenue"])
        total_b_cogs = sum(budget_vals["COGS"])
        total_a_cogs = sum(actual_vals["COGS"])
        total_b_sga  = sum(budget_vals["SG&A"])
        total_a_sga  = sum(actual_vals["SG&A"])
        total_b_eb   = sum(budget_vals["EBITDA"])
        total_a_eb   = sum(actual_vals["EBITDA"])

        fig = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute","relative","relative","total"],
            x=["Budget EBITDA","Revenue Variance","COGS + SGA Variance","Actual EBITDA"],
            y=[total_b_eb,
               total_a_rev  - total_b_rev,
               (total_a_cogs - total_b_cogs) + (total_a_sga - total_b_sga),
               0],
            text=[f"${total_b_eb}M",
                  f"${total_a_rev-total_b_rev:+}M",
                  f"${(total_a_cogs-total_b_cogs)+(total_a_sga-total_b_sga):+}M",
                  f"${total_a_eb}M"],
            textposition="outside",
            connector={"line":{"color":"#888"}},
            increasing={"marker":{"color":"#1D9E75"}},
            decreasing={"marker":{"color":"#E24B4A"}},
            totals={"marker":{"color":"#185FA5"}},
        ))
        fig.update_layout(title="Group EBITDA Bridge — Budget to Actual ($M)",
                          template="plotly_white", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Output 3 — Automated Variance Flags (lines > 10% off budget)**")
        flag_rows = []
        for line in pnl_lines:
            for i, div in enumerate(divs_pnl):
                b = budget_vals[line][i]
                a = actual_vals[line][i]
                if b != 0:
                    var_pct = (a - b) / abs(b) * 100
                    if abs(var_pct) > 10:
                        flag_rows.append({
                            "Division":   div,
                            "P&L Line":   line,
                            "Budget ($M)": b,
                            "Actual ($M)": a,
                            "Variance %":  f"{var_pct:+.1f}%",
                            "RAG":         "🔴 Red" if abs(var_pct)>20 else "🟡 Amber",
                        })
        flag_df = pd.DataFrame(flag_rows).sort_values("Variance %", key=lambda x: x.str.strip('%+').astype(float).abs(), ascending=False)
        st.dataframe(flag_df, use_container_width=True, hide_index=True)

        st.markdown("**Output 4 — Auto-generated Commentary (what the script writes into the report)**")
        worst_div = "Americas"
        worst_var = total_a_eb - total_b_eb
        st.info(f"""
**November 2024 — Group Finance Management Commentary (Auto-generated)**

Group EBITDA came in at **${total_a_eb}M** against a budget of **${total_b_eb}M**, 
a miss of **${worst_var}M ({worst_var/total_b_eb*100:.1f}%)**.

**Revenue** was **${total_a_rev-total_b_rev:+}M** vs budget, with EMEA outperforming (+$3M) 
offset by Americas underperformance (-$16M) due to Mid-Market account churn.

**Costs** were **${(total_a_cogs-total_b_cogs)+(total_a_sga-total_b_sga):+}M** vs budget, 
primarily driven by Americas SG&A over-run (-$7M) from unplanned headcount additions in Q3.

*[Report generated automatically — 1 min 47 sec runtime. Manual process previously: 4 hours.]*
        """)

        st.success("""
**💡 Key Automation Benefits Delivered:**
- **Time saved:** 4 hours → 2 minutes every month (47× faster)
- **Accuracy:** Zero manual copy-paste errors — data flows directly from GL extract
- **Consistency:** Same methodology applied every month, every division
- **Scalability:** Adding a new division requires only one line of configuration change
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 8 Quiz", "❓")
        _quiz("1. Pandas function to reshape a DataFrame from long to wide format (P&L by year across divisions)?",
              ["df.groupby()","df.pivot_table()","df.merge()","df.stack()"],
              "df.pivot_table()","m8q1")
        st.divider()
        _quiz("2. SQL LAG() function is used to:",
              ["Calculate a running total",
               "Rank rows within a partition",
               "Access the value from a prior row (e.g. prior year revenue)",
               "Filter rows based on a condition"],
              "Access the value from a prior row (e.g. prior year revenue)","m8q2")
        st.divider()
        _quiz("3. `df['Revenue'].rolling(12).mean()` computes:",
              ["Mean of the entire Revenue column",
               "A 12-period moving average",
               "Cumulative sum over 12 months",
               "Median over the last 12 rows"],
              "A 12-period moving average","m8q3")
        st.divider()
        _quiz("4. In SQL, PARTITION BY in a window function is used to:",
              ["Filter rows like a WHERE clause",
               "Join two tables together",
               "Reset the window calculation for each group (e.g. each company or division)",
               "Sort the output"],
              "Reset the window calculation for each group (e.g. each company or division)","m8q4")
        st.divider()
        _quiz("5. Primary advantage of a Data Warehouse (e.g. Snowflake) over storing financials in Excel?",
              ["Excel cannot do pivot tables",
               "Scalability, single source of truth, access control, and query performance at scale",
               "Data warehouses are always cheaper",
               "Excel cannot store numerical data"],
              "Scalability, single source of truth, access control, and query performance at scale","m8q5")