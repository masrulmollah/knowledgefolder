import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

# NO set_page_config() — all Streamlit calls inside show()

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
    st.title("📊 Module 2: Descriptive Analytics")
    st.caption("Summarise what has happened using statistics and visualisation")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts","🧮 Stats Calculator","📊 Chart Gallery","🧪 Worked Example","❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────
    with tab1:
        _sec("Descriptive Statistics for Finance","📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Central Tendency**
| Measure | Finance Use |
|---------|-------------|
| Mean    | Average monthly revenue |
| Median  | Typical deal size (skewed data) |
| Mode    | Most common payment term |

**Dispersion**
| Measure  | Finance Use |
|----------|-------------|
| Std Dev  | Annualised vol = σ × √252 |
| Variance | Volatility of returns |
| IQR      | Outlier-robust spread for costs |
            """)
        with c2:
            st.markdown("""
**Distribution Shape**
- **Skewness > 0** → Right tail: rare very large values (VC returns)
- **Skewness < 0** → Left tail: rare very large losses (credit defaults)
- **Kurtosis > 3** → Fat tails: extreme events more likely than normal

**Annualised Volatility**
```
Daily σ × √252 = Annual Volatility
Example: 1.2% daily → ~19% annual
```
⚠️ Normal distribution *understates* financial tail risk.
Always check skewness and kurtosis before modelling.
            """)
        _sec("Chart Selection Guide","📊")
        st.dataframe(pd.DataFrame({
            "Chart":    ["Waterfall","Candlestick","Heat Map","Box Plot","Scatter","Line","Bar"],
            "Best For": ["P&L build-up from revenue to net profit",
                          "OHLC stock/commodity price data",
                          "Correlation matrix or performance grid",
                          "Margin or return distributions across groups",
                          "Relationship between two numeric variables",
                          "Trends over time","Category comparisons"],
            "Avoid When": ["More than 12 line items","Non-price data",
                            "Fewer than 9 data points","Data is normally distributed",
                            "No logical relationship exists","Comparing categories at one point",
                            "Time ordering matters"],
        }), use_container_width=True, hide_index=True)

    # ── STATS CALCULATOR ──────────────────────────────────────────────
    with tab2:
        _sec("Descriptive Statistics Calculator","🧮")
        src = st.radio("Data input", ["Generate sample returns","Enter custom values"])
        if src == "Generate sample returns":
            c1,c2,c3 = st.columns(3)
            with c1: n   = st.slider("Observations",30,500,120)
            with c2: mu  = st.slider("Mean annual return (%)",-10,30,8)
            with c3: sig = st.slider("Annual volatility (%)",5,60,20)
            np.random.seed(42)
            data  = np.random.normal(mu/252, sig/100/np.sqrt(252), n)*100
            label = "Daily Returns (%)"
        else:
            raw = st.text_area("Comma-separated values","12.5,8.2,-3.1,15.4,7.8,-1.2,9.9,22.1,-5.4,11.3")
            try:    data = np.array([float(x.strip()) for x in raw.split(",")]); label="Custom Values"
            except: st.error("Enter valid numbers."); st.stop()

        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Mean",f"{np.mean(data):.4f}"); c2.metric("Median",f"{np.median(data):.4f}")
        c3.metric("Std Dev",f"{np.std(data):.4f}"); c4.metric("Count",len(data))
        c5,c6,c7,c8 = st.columns(4)
        c5.metric("Min",f"{np.min(data):.4f}"); c6.metric("Max",f"{np.max(data):.4f}")
        c7.metric("Skewness",f"{stats.skew(data):.4f}"); c8.metric("Kurtosis",f"{stats.kurtosis(data):.4f}")

        fig = go.Figure(go.Histogram(x=data,nbinsx=40,marker_color="#185FA5",opacity=0.75))
        fig.add_vline(x=np.mean(data),line_dash="dash",line_color="red",
                      annotation_text=f"Mean: {np.mean(data):.2f}")
        fig.add_vline(x=np.median(data),line_dash="dot",line_color="green",
                      annotation_text=f"Median: {np.median(data):.2f}")
        fig.update_layout(title=f"Distribution of {label}",template="plotly_white",height=360)
        st.plotly_chart(fig,use_container_width=True)

    # ── CHART GALLERY ─────────────────────────────────────────────────
    with tab3:
        _sec("Interactive Financial Chart Gallery","📊")
        chart = st.selectbox("Choose chart type",[
            "Waterfall — P&L Build","Candlestick — Price Data",
            "Heat Map — Asset Correlation","Box Plot — Sector Margins","Cohort Retention"])
        np.random.seed(5)
        if chart == "Waterfall — P&L Build":
            labels   = ["Revenue","COGS","Gross Profit","SG&A","EBITDA","D&A","EBIT","Interest","EBT","Tax","Net Profit"]
            measures = ["absolute","relative","total","relative","total","relative","total","relative","total","relative","total"]
            y_vals   = [1000,-420,0,-180,0,-60,0,-40,0,-75,0]
            fig = go.Figure(go.Waterfall(measure=measures,x=labels,y=y_vals,
                connector={"line":{"color":"#888"}},
                increasing={"marker":{"color":"#1D9E75"}},
                decreasing={"marker":{"color":"#E24B4A"}},
                totals={"marker":{"color":"#185FA5"}}))
            fig.update_layout(title="P&L Waterfall — FY2024 ($M)",template="plotly_white",height=400)
            st.plotly_chart(fig,use_container_width=True)
            st.caption("Each bar shows one line item's contribution. Totals bars (blue) show running subtotals.")
        elif chart == "Candlestick — Price Data":
            dates=pd.date_range("2024-01-01","2024-12-31",freq="B"); p=100.0
            opens,highs,lows,closes=[],[],[],[]
            for _ in dates:
                o=p; c2=p*(1+np.random.normal(0.0003,0.012))
                h=max(o,c2)*(1+abs(np.random.normal(0,0.005)))
                l=min(o,c2)*(1-abs(np.random.normal(0,0.005)))
                opens.append(o);highs.append(h);lows.append(l);closes.append(c2);p=c2
            fig=go.Figure(go.Candlestick(x=dates,open=opens,high=highs,low=lows,close=closes))
            fig.update_layout(title="Simulated Stock Price 2024",template="plotly_white",
                              height=400,xaxis_rangeslider_visible=False)
            st.plotly_chart(fig,use_container_width=True)
            st.caption("Green = price rose. Red = price fell. Shows Open-High-Low-Close for each trading day.")
        elif chart == "Heat Map — Asset Correlation":
            assets=["Equities","Bonds","Real Estate","Commodities","FX","Priv.Equity"]
            corr=np.array([[1.00,-0.32,0.54,0.21,0.18,0.67],[-0.32,1.00,-0.11,-0.08,-0.04,-0.28],
                            [0.54,-0.11,1.00,0.15,0.12,0.45],[0.21,-0.08,0.15,1.00,0.33,0.19],
                            [0.18,-0.04,0.12,0.33,1.00,0.14],[0.67,-0.28,0.45,0.19,0.14,1.00]])
            fig=px.imshow(corr,x=assets,y=assets,color_continuous_scale="RdBu_r",zmin=-1,zmax=1,
                          text_auto=".2f",title="Asset Class Correlation Matrix")
            fig.update_layout(template="plotly_white",height=400)
            st.plotly_chart(fig,use_container_width=True)
            st.caption("Blue = positive correlation. Red = negative (diversifying). Darker = stronger relationship.")
        elif chart == "Box Plot — Sector Margins":
            sectors=["Technology","Consumer","Healthcare","Energy","Financials"]
            colours=["#185FA5","#1D9E75","#BA7517","#A32D2D","#534AB7"]
            fig=go.Figure()
            for i,s in enumerate(sectors):
                fig.add_trace(go.Box(y=np.random.normal(0.18+i*0.02,0.07,40)*100,name=s,marker_color=colours[i]))
            fig.update_layout(title="EBITDA Margin Distribution by Sector (%)",template="plotly_white",height=400)
            st.plotly_chart(fig,use_container_width=True)
            st.caption("Box = IQR (25–75th percentile). Centre line = median. Dots = outliers.")
        else:
            cohorts=["Q1-23","Q2-23","Q3-23","Q4-23","Q1-24","Q2-24","Q3-24","Q4-24"]
            periods=["Month 1","Month 3","Month 6","Month 9","Month 12"]
            base=np.array([[100,72,58,49,43],[100,75,61,52,47],[100,68,54,46,41],
                            [100,78,65,56,50],[100,80,67,58,52],[100,76,63,54,48],
                            [100,82,70,62,55],[100,79,66,0,0]],dtype=float)
            base[base==0]=np.nan
            fig=px.imshow(base,x=periods,y=cohorts,text_auto=".0f",
                          color_continuous_scale="Blues",title="Customer Cohort Retention Rate (%)")
            fig.update_layout(template="plotly_white",height=400)
            st.plotly_chart(fig,use_container_width=True)
            st.caption("Each row = customer cohort by acquisition quarter. Darker = higher retention.")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: 36-Month Revenue Descriptive Analysis — Consumer Goods Company","🧪")

        st.markdown("""
**Business Situation:** You are the Finance Manager for a Consumer Goods company.
The CFO asks: *"Give me a clear picture of our revenue performance over the last 3 years —
trends, seasonality, volatility, and any anomalies."*
Here is the full descriptive analysis delivered back to her.
        """)

        # Generate realistic revenue data with trend + seasonality + noise
        np.random.seed(42)
        periods = 36
        dates   = pd.date_range("2022-01-01", periods=periods, freq="MS")
        trend   = 400 + np.arange(periods) * 2.5
        seas    = 35 * np.sin(2 * np.pi * np.arange(periods) / 12 - np.pi/2)
        noise   = np.random.normal(0, 12, periods)
        revenue = trend + seas + noise
        revenue[10] = revenue[10] - 80   # inject anomaly: one-off disruption Oct-22

        df = pd.DataFrame({"Month": dates, "Revenue ($M)": revenue.round(1)})
        df["MA_3M"]      = df["Revenue ($M)"].rolling(3).mean().round(1)
        df["MA_12M"]     = df["Revenue ($M)"].rolling(12).mean().round(1)
        df["YoY_Growth"] = df["Revenue ($M)"].pct_change(12).mul(100).round(1)
        df["MoM_Growth"] = df["Revenue ($M)"].pct_change(1).mul(100).round(1)

        st.markdown("**1. Summary Statistics**")
        rev = df["Revenue ($M)"]
        c1,c2,c3,c4,c5,c6 = st.columns(6)
        c1.metric("Mean Revenue",    f"${rev.mean():.1f}M")
        c2.metric("Median Revenue",  f"${rev.median():.1f}M")
        c3.metric("Std Deviation",   f"${rev.std():.1f}M")
        c4.metric("Min Month",       f"${rev.min():.1f}M")
        c5.metric("Max Month",       f"${rev.max():.1f}M")
        c6.metric("Skewness",        f"{stats.skew(rev):.2f}")

        st.markdown("**2. Trend & Moving Averages**")
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df["Month"], y=df["Revenue ($M)"],
                             name="Monthly Revenue", marker_color="#B0C4DE", opacity=0.6))
        fig.add_trace(go.Scatter(x=df["Month"], y=df["MA_3M"],
                                 name="3-Month Moving Avg", line=dict(color="#E24B4A",width=1.5,dash="dash")))
        fig.add_trace(go.Scatter(x=df["Month"], y=df["MA_12M"],
                                 name="12-Month Moving Avg", line=dict(color="#185FA5",width=2.5)))
        fig.add_annotation(x="2022-11-01", y=revenue[10],
                           text="Oct-22: Supply disruption (-$80M)", showarrow=True,
                           arrowhead=2, arrowcolor="red", font=dict(color="red"))
        fig.update_layout(title="Monthly Revenue with Trend Lines ($M)",
                          template="plotly_white", height=400,
                          legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)
        st.info("📌 Insight: Underlying trend is +$2.5M/month. The 12M moving average clearly shows the structural growth, smoothing out seasonal noise and the Oct-22 one-off disruption.")

        st.markdown("**3. Seasonality Pattern**")
        df["Month_Name"] = df["Month"].dt.month_name().str[:3]
        df["Month_Num"]  = df["Month"].dt.month
        seas_avg = df.groupby("Month_Num").agg(
            Month=("Month_Name","first"),
            Avg_Revenue=("Revenue ($M)","mean")).reset_index()
        grand_avg = rev.mean()
        seas_avg["Seasonal_Index"] = (seas_avg["Avg_Revenue"] / grand_avg * 100).round(1)
        fig2 = go.Figure(go.Bar(
            x=seas_avg["Month"], y=seas_avg["Seasonal_Index"],
            marker_color=["#1D9E75" if v>100 else "#E24B4A" for v in seas_avg["Seasonal_Index"]],
            text=[f"{v:.0f}" for v in seas_avg["Seasonal_Index"]], textposition="outside"))
        fig2.add_hline(y=100, line_dash="dash", line_color="black", annotation_text="Average = 100")
        fig2.update_layout(title="Seasonal Index by Month (100 = average month)",
                           yaxis_title="Seasonal Index", template="plotly_white", height=360,
                           yaxis=dict(range=[70,130]))
        st.plotly_chart(fig2, use_container_width=True)
        st.info("📌 Insight: December is the strongest month (index ~125), driven by holiday season demand. February is weakest (index ~78). Budget assumptions should reflect this pattern.")

        st.markdown("**4. Year-on-Year Growth Analysis**")
        yoy_df = df.dropna(subset=["YoY_Growth"])
        fig3 = go.Figure(go.Bar(
            x=yoy_df["Month"], y=yoy_df["YoY_Growth"],
            marker_color=["#1D9E75" if v>0 else "#E24B4A" for v in yoy_df["YoY_Growth"]],
            text=[f"{v:+.1f}%" for v in yoy_df["YoY_Growth"]], textposition="outside"))
        fig3.add_hline(y=0, line_color="black", line_width=1)
        fig3.update_layout(title="Year-on-Year Revenue Growth (%)",
                           yaxis_title="YoY Growth (%)", template="plotly_white", height=360)
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("**5. CFO Summary — Key Findings**")
        st.success("""
**Revenue Performance Summary — Jan 2022 to Dec 2024**

- **Trend:** Consistent growth averaging +$2.5M/month (+7.2% annualised CAGR).
- **Seasonality:** Strong Q4 seasonal uplift (Dec index = 125). Weak Q1 (Feb index = 78). Budget should incorporate this pattern.
- **Volatility:** Monthly std dev = $18M. Manageable — within normal operating range.
- **Anomaly:** October 2022 was a $80M revenue shortfall due to the Thailand supply disruption — a confirmed one-off, excluded from trend analysis.
- **Skewness:** Negative (-0.4) — confirming one large negative outlier (Oct-22). Underlying distribution is near-normal.
- **Recommendation:** Annualised revenue run-rate entering 2025 is ~$510M. Budget at $520M (+2%) appears achievable given the trend, but carry $490M (−4%) as the downside scenario.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 2 Quiz","❓")
        _quiz("1. A VC fund return dataset has skewness of +2.3. This means:",
              ["Returns are normally distributed",
               "Long right tail — rare very high returns",
               "Long left tail","Mean equals median"],
              "Long right tail — rare very high returns","m2q1")
        st.divider()
        _quiz("2. Best chart for P&L build from revenue to net profit?",
              ["Line chart","Scatter plot","Waterfall chart","Heat map"],
              "Waterfall chart","m2q2")
        st.divider()
        _quiz("3. Daily std dev 1.2% → annualised volatility?",
              ["1.2%","12%","19%","302%"],"19%","m2q3")
        st.divider()
        _quiz("4. Best chart for comparing EBITDA margin distributions across 5 sectors?",
              ["Grouped bar","Box plot","Pie chart","Area chart"],"Box plot","m2q4")
        st.divider()
        _quiz("5. Kurtosis > 3 means:",
              ["Perfectly normal","Returns always positive",
               "Extreme events more likely than normal distribution predicts",
               "Mean higher than median"],
              "Extreme events more likely than normal distribution predicts","m2q5")