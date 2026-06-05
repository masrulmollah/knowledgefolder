import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

def _sec(t, i=""): st.markdown(f"### {i} {t}"); st.markdown("---")
def _quiz(q, opts, ans, key):
    st.markdown(f"**{q}**")
    c = st.radio("", opts, key=key, index=None)
    if c is not None:
        if c == ans: st.success("✅ Correct!")
        else: st.error(f"❌ Incorrect. Correct answer: **{ans}**")

def show():
    st.title("🔍 Module 3: Diagnostic Analytics")
    st.caption("Identify WHY something happened — root cause & variance analysis")
    st.markdown("---")
    tab1,tab2,tab3,tab4,tab5 = st.tabs([
        "📖 Concepts","🧮 PVM Calculator","📊 Correlation Tool","🧪 Worked Example","❓ Quiz"])

    with tab1:
        _sec("Price-Volume-Mix Decomposition","📐")
        c1,c2 = st.columns(2)
        with c1:
            st.markdown("""
**Core Formula**
```
Revenue Variance = Price + Volume + Mix

Price Effect  = (Actual Price  − Budget Price)  × Actual Volume
Volume Effect = (Actual Volume − Budget Volume) × Budget Price
Mix Effect    = Total Variance − Price − Volume
```
**The 5-Why Framework**
| Level | Question | Example |
|-------|----------|---------|
| Why 1 | Why did EBITDA miss? | Revenue lower than plan |
| Why 2 | Why was revenue lower? | Volume down 8% |
| Why 3 | Why volume down? | Key customer churned |
| Why 4 | Why did they churn? | Competitor undercut on price |
| Why 5 | Why weren't we aware? | No early-warning KRI |
            """)
        with c2:
            st.markdown("""
**ROIC Driver Tree**
```
ROIC
├── NOPAT Margin
│   ├── Gross Margin
│   └── OpEx Ratio (SG&A, R&D)
└── Capital Turns
    ├── Fixed Asset Turns
    └── Working Capital Turns
        ├── DSO — Days Sales Outstanding
        ├── DPO — Days Payable Outstanding
        └── DIO — Days Inventory Outstanding
```
**Anomaly Detection Methods**
- **Z-score:** flag values > 3σ from mean
- **IQR:** flag outside Q1−1.5×IQR / Q3+1.5×IQR
- **Benford's Law:** first-digit test for fraud detection
            """)
        st.warning("⚠️ **Correlation ≠ Causation.** Always test causal direction with Granger causality, difference-in-differences, or domain logic before drawing conclusions.")

    with tab2:
        _sec("Price-Volume-Mix Variance Calculator","🧮")
        products=["Product A","Product B","Product C"]
        db=[(500,10.0),(300,15.0),(200,20.0)]; da=[(480,11.0),(340,14.0),(190,22.0)]
        hdr=st.columns([2,1.5,1.5,1.5,1.5])
        for h,lbl in zip(hdr,["Product","Budget Vol","Budget Price","Actual Vol","Actual Price"]):
            h.markdown(f"**{lbl}**")
        bvs,bps,avs,aps=[],[],[],[]
        for i,prod in enumerate(products):
            c1,c2,c3,c4,c5=st.columns([2,1.5,1.5,1.5,1.5])
            with c1: st.markdown(f"*{prod}*")
            with c2: bv=st.number_input(f"bv{i}",value=float(db[i][0]),key=f"bv{i}",label_visibility="collapsed")
            with c3: bp=st.number_input(f"bp{i}",value=db[i][1],key=f"bp{i}",label_visibility="collapsed")
            with c4: av=st.number_input(f"av{i}",value=float(da[i][0]),key=f"av{i}",label_visibility="collapsed")
            with c5: ap=st.number_input(f"ap{i}",value=da[i][1],key=f"ap{i}",label_visibility="collapsed")
            bvs.append(bv);bps.append(bp);avs.append(av);aps.append(ap)
        rows=[];tb,ta,tpe,tve,tme=0,0,0,0,0
        for i,prod in enumerate(products):
            br=bvs[i]*bps[i];ar=avs[i]*aps[i]
            pe=(aps[i]-bps[i])*avs[i];ve=(avs[i]-bvs[i])*bps[i];me=(ar-br)-pe-ve
            rows.append({"Product":prod,"Budget":round(br,1),"Actual":round(ar,1),
                         "Total Var":round(ar-br,1),"Price Eff":round(pe,1),"Vol Eff":round(ve,1),"Mix Eff":round(me,1)})
            tb+=br;ta+=ar;tpe+=pe;tve+=ve;tme+=me
        st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
        tv=ta-tb
        c1,c2,c3,c4=st.columns(4)
        c1.metric("Total Variance",f"${tv:+.1f}",delta=f"{tv/tb*100:+.1f}%")
        c2.metric("Price Effect",f"${tpe:+.1f}"); c3.metric("Volume Effect",f"${tve:+.1f}"); c4.metric("Mix Effect",f"${tme:+.1f}")
        fig=go.Figure(go.Waterfall(orientation="v",
            measure=["absolute","relative","relative","relative","total"],
            x=["Budget","Price Effect","Volume Effect","Mix Effect","Actual"],
            y=[tb,tpe,tve,tme,0],
            text=[f"${tb:,.0f}",f"${tpe:+,.0f}",f"${tve:+,.0f}",f"${tme:+,.0f}",f"${ta:,.0f}"],
            textposition="outside",
            increasing={"marker":{"color":"#1D9E75"}},decreasing={"marker":{"color":"#E24B4A"}},
            totals={"marker":{"color":"#185FA5"}}))
        fig.update_layout(title="Price-Volume-Mix Revenue Bridge",template="plotly_white",height=380)
        st.plotly_chart(fig,use_container_width=True)

    with tab3:
        _sec("Correlation Analysis Tool","📊")
        c1,c2=st.columns(2)
        with c1: vx=st.selectbox("Variable X",["Revenue Growth","GDP Growth","Interest Rate","Inflation"])
        with c2: vy=st.selectbox("Variable Y",["Revenue Growth","GDP Growth","Interest Rate","Inflation"],index=1)
        n=st.slider("Sample size (quarters)",20,100,40)
        tc=st.slider("True underlying correlation (simulation)",-1.0,1.0,0.65)
        np.random.seed(42)
        x=np.random.randn(n);y=tc*x+np.sqrt(1-tc**2)*np.random.randn(n)
        x=x*3+5;y=y*4+4
        r,p=stats.pearsonr(x,y);rho,_=stats.spearmanr(x,y)
        c1,c2,c3=st.columns(3)
        c1.metric("Pearson r",f"{r:.3f}");c2.metric("Spearman ρ",f"{rho:.3f}")
        c3.metric("P-value",f"{p:.4f}",delta="Significant" if p<0.05 else "Not significant")
        fig=px.scatter(x=x,y=y,labels={"x":vx,"y":vy},title=f"{vx} vs {vy}  (r = {r:.3f})",
                       trendline="ols",template="plotly_white",height=380)
        st.plotly_chart(fig,use_container_width=True)

    with tab4:
        _sec("Worked Example: Diagnosing a $42M EBITDA Miss — Industrial Company Q3 2024","🧪")

        st.markdown("""
**Business Situation:** You are the Group FP&A Manager. Q3 2024 results have just closed.
EBITDA came in at **$94M against a budget of $136M** — a miss of **$42M (31%)**.
The CFO needs a full root-cause analysis by 9am tomorrow. Here is the complete diagnostic.
        """)

        st.markdown("**Step 1 — Top-Down P&L Variance**")
        pnl = pd.DataFrame({
            "P&L Line":    ["Revenue","COGS","Gross Profit","SG&A","R&D","EBITDA"],
            "Budget ($M)": [500, -220, 280, -100, -44, 136],
            "Actual ($M)": [482, -238, 244, -112, -38,  94],
        })
        pnl["Variance ($M)"]  = pnl["Actual ($M)"] - pnl["Budget ($M)"]
        pnl["Variance (%)"]   = (pnl["Variance ($M)"] / pnl["Budget ($M)"].abs() * 100).round(1)
        pnl["Signal"] = pnl["Variance ($M)"].apply(lambda v: "🔴 Miss" if v < 0 else "🟢 Beat")
        st.dataframe(pnl, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — EBITDA Bridge: Budget to Actual**")
        fig = go.Figure(go.Waterfall(orientation="v",
            measure=["absolute","relative","relative","relative","relative","total"],
            x=["Budget EBITDA","Revenue Miss","COGS Overshoot","SG&A Over-run","R&D Saving","Actual EBITDA"],
            y=[136, -18, -18, -12, 6, 0],
            text=["$136M","-$18M","-$18M","-$12M","+$6M","$94M"], textposition="outside",
            connector={"line":{"color":"#888"}},
            increasing={"marker":{"color":"#1D9E75"}},
            decreasing={"marker":{"color":"#E24B4A"}},
            totals={"marker":{"color":"#185FA5"}}))
        fig.update_layout(title="EBITDA Bridge — Budget to Actual Q3 2024 ($M)",
                          template="plotly_white",height=420,yaxis_title="EBITDA ($M)")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Step 3 — Revenue PVM Decomposition**")
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Total Revenue Miss","-$18M")
        c2.metric("Price Effect","+$8M",delta="Price increases landed — positive")
        c3.metric("Volume Effect","-$22M",delta="Volume shortfall — primary driver")
        c4.metric("Mix Effect","-$4M",delta="Shift to lower-margin products")
        st.markdown("*Conclusion: The revenue miss is entirely volume-driven. Price realisation was actually ahead of plan.*")

        st.markdown("**Step 4 — Volume Miss by Customer Segment**")
        segs = ["Enterprise","Mid-Market","SMB","Public Sector"]
        var  = [5, -15, -9, 1]
        fig2 = go.Figure(go.Bar(x=segs, y=var,
            marker_color=["#1D9E75" if v>0 else "#E24B4A" for v in var],
            text=[f"${v:+}M" for v in var],textposition="outside"))
        fig2.add_hline(y=0,line_color="black",line_width=1)
        fig2.update_layout(title="Revenue Variance vs Budget by Segment ($M) — Mid-Market is primary driver",
                           template="plotly_white",height=360,yaxis=dict(range=[-20,12]))
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Step 5 — COGS Anomaly Detection**")
        np.random.seed(7)
        unit_costs = np.random.normal(42, 4, 60)
        unit_costs[12] = 78; unit_costs[35] = 81   # inject anomalies
        z_scores   = (unit_costs - unit_costs.mean()) / unit_costs.std()
        flagged    = np.abs(z_scores) > 2.5
        cost_df    = pd.DataFrame({
            "Transaction #": range(1, 61),
            "Unit Cost ($)": unit_costs.round(1),
            "Z-Score":       z_scores.round(2),
            "Flag":          ["⚠️ Anomaly" if f else "✅ Normal" for f in flagged]})
        anomalies  = cost_df[cost_df["Flag"]=="⚠️ Anomaly"]
        st.dataframe(anomalies[["Transaction #","Unit Cost ($)","Z-Score","Flag"]],
                     use_container_width=True, hide_index=True)
        st.warning(f"2 anomalous unit cost transactions found (avg unit cost = ${unit_costs.mean():.0f}, flagged at >${unit_costs.mean()+2.5*unit_costs.std():.0f}). These relate to emergency spot-market purchases of raw materials in Jul-24 due to supplier shortage.")

        st.success("""
**Root Cause Summary — $42M EBITDA Miss**

| Driver | Impact | Root Cause |
|--------|--------|------------|
| Revenue Volume | -$22M | Mid-Market: 3 accounts churned to competitor. SMB: pricing sensitivity post-summer increase. |
| COGS Inflation | -$18M | Raw material costs +8.5% above budget. 2 spot-market purchases at 85% premium in Jul-24. |
| SG&A Over-run  | -$12M | 18 headcount hired Q2 ahead of revenue ramp that didn't materialise. |
| R&D Under-spend | +$6M | Project Phoenix delayed 1 quarter — costs shift to Q4. |

**Recommended Actions:**
1. Reactivate churned Mid-Market accounts with targeted retention offer (CFO to approve up to 10% discount).
2. Accelerate supplier renegotiation for raw materials — RFP to 3 alternative suppliers by Oct-31.
3. Freeze SGA hiring for Q4. Reduce run-rate by $4M.
        """)

    with tab5:
        _sec("Module 3 Quiz","❓")
        _quiz("1. Revenue var = −$25M. Volume = −$30M, Mix = +$5M. Price Effect?",
              ["−$50M","+$30M","+$0M","−$20M"],"+$0M","m3q1")
        st.divider()
        _quiz("2. Which test checks if X helps forecast Y beyond Y's own history?",
              ["Pearson correlation","Granger causality test","Z-score","Benford's Law"],
              "Granger causality test","m3q2")
        st.divider()
        _quiz("3. Strong revenue-headcount correlation most likely exists because:",
              ["Hiring causes revenue","Revenue causes headcount",
               "Both driven by company growth (confounding variable)","Spurious coincidence"],
              "Both driven by company growth (confounding variable)","m3q3")
        st.divider()
        _quiz("4. Benford's Law is most useful for:",
              ["Forecasting revenues","Detecting fraud or data manipulation",
               "Calculating correlations","Building regressions"],
              "Detecting fraud or data manipulation","m3q4")
        st.divider()
        _quiz("5. In a ROIC driver tree, which is a second-level driver?",
              ["Stock price","Days Sales Outstanding (DSO)","ROIC itself","Dividend yield"],
              "Days Sales Outstanding (DSO)","m3q5")