import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

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
    st.title("🔬 Module 4: Exploratory & Statistical Analytics")
    st.caption("Discover hidden patterns, outliers, and anomalies in financial datasets")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Pareto & Segmentation", "📊 Outlier Detector", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Statistical Profiling", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Distribution Analysis Toolkit**
| Statistic | What It Tells You | Finance Application |
|-----------|-------------------|---------------------|
| Mean | Central tendency (sensitive to outliers) | Average deal size, avg cost/unit |
| Median | Robust centre (ignores outliers) | Typical contract value |
| Std Deviation | Spread around the mean | Revenue volatility, cost uncertainty |
| IQR (Q3−Q1) | Middle 50% spread (outlier-robust) | Normal operating range for costs |
| Skewness | Symmetry of distribution | VC returns (positive skew), defaults (negative) |
| Kurtosis | Weight of tails vs normal | Extreme event probability |
| Coefficient of Variation | Std Dev / Mean | Comparing volatility across metrics with different scales |

**Rule of Thumb:**
- Skewness > +1 or < −1: notably skewed, use median over mean
- Kurtosis > 3: fat tails, extreme events more common than a normal model predicts
            """)
        with c2:
            st.markdown("""
**Pareto Analytics (80/20 Rule)**

Identify the vital few that drive the trivial many:
- 20% of SKUs generate 80% of profit → focus product investment
- 20% of customers generate 80% of revenue → focus retention
- 20% of vendors drive 80% of procurement costs → focus supplier negotiation
- 20% of cost lines drive 80% of total cost → focus reduction initiatives

**RFM Segmentation (Customer Analytics)**
| Dimension | Measures | High Score Means |
|-----------|----------|-----------------|
| Recency   | Days since last purchase | Recently active |
| Frequency | Number of purchases | Loyal buyer |
| Monetary  | Total spend | High-value customer |

Combine R + F + M into a score → segment customers into Champions, 
Loyals, At-Risk, Lost. Each segment has a different retention strategy.
            """)

        _sec("Anomaly & Fraud Detection", "🚨")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Z-Score Method:**
```
Z = (Value − Mean) / Standard Deviation
```
Flag values with |Z| > 2.5 or > 3.0 as outliers.
Use for: cost transaction screening, revenue anomalies.

**IQR Method:**
```
Lower Fence = Q1 − 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```
More robust than Z-score when data is non-normal.
Use for: skewed cost distributions, invoice amounts.
            """)
        with c2:
            st.markdown("""
**Benford's Law:**
In naturally occurring numerical datasets (revenues, expenses, populations),
the leading digit follows a predictable logarithmic distribution:
- "1" appears as first digit ~30.1% of the time
- "9" appears as first digit only ~4.6% of the time

**Deviation from Benford = potential manipulation:**
- Round numbers (e.g. $5,000, $10,000 appearing too often) → approval threshold fraud
- Digit "7" or "9" over-represented → values just below approval limits
- Used by auditors and forensic accountants globally

**Other anomaly checks:**
- Duplicate invoice detection
- Three-point deviation rule (>3× normal variation)
- Journal entries posted outside business hours
- Round-number concentration testing
            """)

    # ── PARETO & SEGMENTATION ─────────────────────────────────────────────────
    with tab2:
        _sec("Pareto Analysis & ABC Segmentation", "🧮")
        np.random.seed(42)
        n_skus = st.slider("Number of SKUs / Customers", 10, 50, 25)
        metric_label = st.selectbox("Analyse by:", ["Revenue ($K)", "Gross Profit ($K)", "Procurement Cost ($K)"])

        values = np.random.pareto(1.2, n_skus) * 200 + 10
        values = np.sort(values)[::-1]
        labels = [f"SKU-{i:03d}" for i in range(1, n_skus + 1)]

        cumulative = np.cumsum(values) / values.sum() * 100
        abc_labels = ["A" if c <= 80 else "B" if c <= 95 else "C" for c in cumulative]

        df_pareto = pd.DataFrame({
            "Item": labels,
            metric_label: values.round(1),
            "Cumulative %": cumulative.round(1),
            "ABC Class": abc_labels,
        })

        fig = go.Figure()
        colors = {"A": "#185FA5", "B": "#1D9E75", "C": "#B5D4F4"}
        fig.add_trace(go.Bar(
            x=df_pareto["Item"], y=df_pareto[metric_label],
            marker_color=[colors[c] for c in abc_labels],
            name=metric_label
        ))
        fig.add_trace(go.Scatter(
            x=df_pareto["Item"], y=df_pareto["Cumulative %"],
            name="Cumulative %", yaxis="y2",
            mode="lines+markers", line=dict(color="#E24B4A", width=2)
        ))
        fig.add_hline(y=80, line_dash="dash", line_color="orange",
                      annotation_text="80% threshold (A/B boundary)", yref="y2")
        fig.update_layout(
            title=f"Pareto Chart — {metric_label} by Item",
            yaxis=dict(title=metric_label),
            yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0, 105]),
            xaxis=dict(tickangle=45),
            template="plotly_white", height=420,
            barmode="relative",
            legend=dict(orientation="h", y=1.02)
        )
        st.plotly_chart(fig, use_container_width=True)

        a_count = abc_labels.count("A")
        a_val   = df_pareto[df_pareto["ABC Class"]=="A"][metric_label].sum()
        total_val = df_pareto[metric_label].sum()
        c1, c2, c3 = st.columns(3)
        c1.metric(f"Class A items (≤80%)", f"{a_count} of {n_skus} ({a_count/n_skus*100:.0f}%)")
        c2.metric(f"Class A {metric_label}", f"${a_val:,.0f}K ({a_val/total_val*100:.0f}%)")
        c3.metric("Pareto ratio (A items : A value)", f"{a_count/n_skus*100:.0f}% items → {a_val/total_val*100:.0f}% value")

        st.dataframe(df_pareto.head(10), use_container_width=True, hide_index=True)

    # ── OUTLIER DETECTOR ─────────────────────────────────────────────────────
    with tab3:
        _sec("Outlier & Anomaly Detection Tool", "📊")
        method = st.radio("Detection method:", ["Z-Score", "IQR (Interquartile Range)", "Benford's Law"])

        if method in ["Z-Score", "IQR (Interquartile Range)"]:
            c1, c2 = st.columns(2)
            with c1:
                n_trans = st.slider("Number of transactions", 50, 300, 120)
                anomaly_pct = st.slider("Injected anomaly rate (%)", 1, 10, 3)
            with c2:
                threshold = st.slider("Z-Score threshold" if method == "Z-Score" else "IQR multiplier",
                                      1.5, 4.0, 2.5, 0.1)

            np.random.seed(42)
            base_amounts = np.random.normal(500, 80, n_trans)
            n_anomalies = max(1, int(n_trans * anomaly_pct / 100))
            anomaly_idx = np.random.choice(n_trans, n_anomalies, replace=False)
            for idx in anomaly_idx:
                base_amounts[idx] = np.random.choice([
                    np.random.uniform(900, 1500),
                    np.random.uniform(-200, 50)
                ])

            if method == "Z-Score":
                z = (base_amounts - base_amounts.mean()) / base_amounts.std()
                flagged = np.abs(z) > threshold
                score_label = "Z-Score"
                scores = z
            else:
                q1, q3 = np.percentile(base_amounts, 25), np.percentile(base_amounts, 75)
                iqr = q3 - q1
                lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
                flagged = (base_amounts < lower) | (base_amounts > upper)
                scores = (base_amounts - base_amounts.mean()) / base_amounts.std()
                score_label = "Z-Score (ref)"

            trans_df = pd.DataFrame({
                "Transaction #": range(1, n_trans+1),
                "Amount ($)": base_amounts.round(2),
                score_label: scores.round(3),
                "Status": ["⚠️ ANOMALY" if f else "✅ Normal" for f in flagged]
            })

            fig = go.Figure()
            normal_mask = ~flagged
            fig.add_trace(go.Scatter(
                x=trans_df[normal_mask]["Transaction #"],
                y=trans_df[normal_mask]["Amount ($)"],
                mode="markers", name="Normal",
                marker=dict(color="#185FA5", size=6, opacity=0.6)
            ))
            fig.add_trace(go.Scatter(
                x=trans_df[flagged]["Transaction #"],
                y=trans_df[flagged]["Amount ($)"],
                mode="markers", name="⚠️ Anomaly",
                marker=dict(color="#E24B4A", size=10, symbol="x")
            ))
            fig.update_layout(title=f"Transaction Anomaly Detection — {method}",
                              xaxis_title="Transaction #", yaxis_title="Amount ($)",
                              template="plotly_white", height=380)
            st.plotly_chart(fig, use_container_width=True)

            n_flagged = flagged.sum()
            c1, c2, c3 = st.columns(3)
            c1.metric("Transactions analysed", n_trans)
            c2.metric("Anomalies flagged", n_flagged, delta=f"{n_flagged/n_trans*100:.1f}% of total")
            c3.metric("Total flagged amount", f"${trans_df[flagged]['Amount ($)'].sum():,.0f}")
            st.dataframe(trans_df[flagged].reset_index(drop=True), use_container_width=True, hide_index=True)

        else:  # Benford's Law
            st.markdown("""
Benford's Law predicts the frequency of leading digits in large naturally-occurring datasets.
Generate a dataset below and test whether it follows Benford's Law — deviations suggest manipulation.
            """)
            c1, c2 = st.columns(2)
            with c1:
                n_vals  = st.slider("Dataset size", 100, 2000, 500)
                dist    = st.selectbox("Data type:", ["Natural (follows Benford)", "Manipulated (round numbers)"])

            np.random.seed(42)
            if dist == "Natural (follows Benford)":
                raw = np.random.lognormal(5, 2, n_vals)
            else:
                raw = np.random.choice(
                    [5000, 9999, 4999, 10000, 2500, 7500] * (n_vals // 6 + 1), n_vals)

            leading_digits = [int(str(abs(int(v)))[0]) for v in raw if v > 0]
            actual_freq = pd.Series(leading_digits).value_counts(normalize=True).sort_index() * 100
            benford_expected = {d: np.log10(1 + 1/d) * 100 for d in range(1, 10)}

            fig = go.Figure()
            fig.add_trace(go.Bar(x=list(range(1,10)), y=[benford_expected[d] for d in range(1,10)],
                                 name="Benford Expected %", marker_color="#B5D4F4", opacity=0.8))
            fig.add_trace(go.Scatter(x=list(range(1,10)),
                                     y=[actual_freq.get(d, 0) for d in range(1,10)],
                                     name="Actual %", mode="lines+markers",
                                     line=dict(color="#E24B4A", width=2.5),
                                     marker=dict(size=8)))
            fig.update_layout(title="Benford's Law — Expected vs. Actual Leading Digit Frequency",
                              xaxis_title="Leading Digit", yaxis_title="Frequency (%)",
                              xaxis=dict(tickvals=list(range(1,10))),
                              template="plotly_white", height=400)
            st.plotly_chart(fig, use_container_width=True)

            deviations = {d: abs(actual_freq.get(d, 0) - benford_expected[d]) for d in range(1,10)}
            max_dev = max(deviations.values())
            if dist == "Manipulated (round numbers)":
                st.error(f"⚠️ Large deviation detected (max {max_dev:.1f}pp from Benford expected). This pattern — over-representation of round numbers — is a common indicator of manual overrides or approval-limit gaming. Recommend forensic review.")
            else:
                st.success(f"✅ Dataset broadly follows Benford's Law (max deviation {max_dev:.1f}pp). No significant manipulation signals detected.")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: SKU Profitability Audit — FMCG Company", "🧪")
        st.markdown("""
**Situation:** The Category Finance Manager has been asked: *"Which of our 30 SKUs are actually making money,
and which are destroying value? We want to rationalise the portfolio before the next planning cycle."*
        """)

        np.random.seed(99)
        n = 30
        skus = [f"SKU-{i:03d}" for i in range(1, n+1)]
        revenue  = np.random.pareto(1.1, n) * 500 + 20
        gm_pct   = np.random.normal(38, 15, n)
        vol_cost = revenue * np.random.uniform(0.05, 0.25, n)
        overhead = np.random.uniform(2, 18, n) * 10
        contrib  = revenue * gm_pct/100 - vol_cost - overhead

        df_sku = pd.DataFrame({
            "SKU": skus,
            "Revenue ($K)":    revenue.round(1),
            "GM %":            gm_pct.round(1),
            "Vol/Alloc Cost ($K)": vol_cost.round(1),
            "Contrib Margin ($K)": contrib.round(1),
        })
        df_sku = df_sku.sort_values("Contrib Margin ($K)", ascending=False).reset_index(drop=True)
        df_sku["Cum Rev %"]    = (df_sku["Revenue ($K)"].cumsum() / df_sku["Revenue ($K)"].sum() * 100).round(1)
        df_sku["Cum CM %"]     = (df_sku["Contrib Margin ($K)"].cumsum() / df_sku["Contrib Margin ($K)"].sum() * 100).round(1)
        df_sku["Rec"] = df_sku["Contrib Margin ($K)"].apply(
            lambda v: "✅ Keep & Grow" if v > 30 else "⚠️ Optimise" if v > 0 else "🔴 Delist / Reprice")

        st.markdown("**Step 1 — Full SKU Contribution Margin Ranking**")
        st.dataframe(df_sku, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — Contribution Margin Pareto (which SKUs drive the value?)**")
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_sku["SKU"], y=df_sku["Contrib Margin ($K)"],
            marker_color=["#1D9E75" if v > 0 else "#E24B4A" for v in df_sku["Contrib Margin ($K)"]],
            name="Contribution Margin ($K)"
        ))
        fig.add_hline(y=0, line_color="black", line_width=1)
        fig.update_layout(title="Contribution Margin by SKU ($K)",
                          template="plotly_white", height=380,
                          xaxis=dict(tickangle=45), xaxis_title="SKU", yaxis_title="CM ($K)")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 3 — Revenue vs. Margin Bubble Chart (Size = Revenue)**")
        fig2 = px.scatter(
            df_sku, x="GM %", y="Contrib Margin ($K)", size="Revenue ($K)",
            color="Rec", hover_name="SKU",
            color_discrete_map={"✅ Keep & Grow":"#1D9E75","⚠️ Optimise":"#EF9F27","🔴 Delist / Reprice":"#E24B4A"},
            title="SKU Margin vs. GM% — Bubble Size = Revenue",
            template="plotly_white", height=420,
        )
        fig2.add_vline(x=0,  line_dash="dash", line_color="gray")
        fig2.add_hline(y=0,  line_dash="dash", line_color="gray")
        st.plotly_chart(fig2, use_container_width=True)

        positive_cm  = df_sku[df_sku["Contrib Margin ($K)"] > 0]["Contrib Margin ($K)"].sum()
        negative_cm  = df_sku[df_sku["Contrib Margin ($K)"] <= 0]["Contrib Margin ($K)"].sum()
        n_negative   = (df_sku["Contrib Margin ($K)"] <= 0).sum()
        c1, c2, c3 = st.columns(3)
        c1.metric("Value-creating SKUs", f"{n - n_negative} of {n}")
        c2.metric("Total positive CM",   f"${positive_cm:,.0f}K")
        c3.metric("Value destroyed by loss-makers", f"${abs(negative_cm):,.0f}K")

        st.success(f"""
**Portfolio Rationalisation Recommendation:**

- **{n_negative} SKUs** are destroying **${abs(negative_cm):,.0f}K** in contribution margin annually.
- Delisting or repricing these SKUs would improve total portfolio CM by up to **{abs(negative_cm/positive_cm)*100:.0f}%**.
- Top 5 SKUs by CM account for **{df_sku.head(5)['Contrib Margin ($K)'].sum() / positive_cm * 100:.0f}%** of total positive contribution — protect these at all costs.
- Recommendation: Initiate SKU rationalisation project; model impact of each delist on factory overhead absorption before executing.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 4 Quiz", "❓")
        _quiz("1. Pareto analysis finds that 22% of customers drive 79% of revenue. This means:",
              ["The data has an error — it should be exactly 20/80",
               "The business is broadly following the Pareto principle — concentrate on the top 22%",
               "All customers are equally important",
               "Revenue is too concentrated — no action needed"],
              "The business is broadly following the Pareto principle — concentrate on the top 22%", "fa_m4q1")
        st.divider()
        _quiz("2. In RFM analysis, a customer with high Recency, high Frequency, and high Monetary score is:",
              ["A churned customer", "A 'Champion' — most valuable, recently active",
               "A prospect", "A price-sensitive buyer"],
              "A 'Champion' — most valuable, recently active", "fa_m4q2")
        st.divider()
        _quiz("3. Benford's Law is violated when:",
              ["Transaction amounts are normally distributed",
               "Round numbers (5000, 10000) appear far more often than expected",
               "The leading digit '1' appears 30% of the time",
               "Dataset has more than 1,000 rows"],
              "Round numbers (5000, 10000) appear far more often than expected", "fa_m4q3")
        st.divider()
        _quiz("4. IQR-based outlier detection is preferred over Z-score when:",
              ["Data is perfectly normally distributed",
               "Data is highly skewed or non-normal",
               "You need to detect round-number fraud",
               "The dataset has fewer than 10 rows"],
              "Data is highly skewed or non-normal", "fa_m4q4")
        st.divider()
        _quiz("5. A distribution with kurtosis of 5.2 compared to normal (kurtosis=3) suggests:",
              ["Returns are always positive",
               "Extreme outcomes (very large gains or losses) are more likely than a normal model predicts",
               "The data is perfectly symmetrical",
               "Standard deviation is meaningless"],
              "Extreme outcomes (very large gains or losses) are more likely than a normal model predicts", "fa_m4q5")