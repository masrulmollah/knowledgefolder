import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# NO st.set_page_config() — Homepage.py owns that call.

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
    st.title("💰 Module 6: Valuation & Investment Analytics")
    st.caption("Apply analytics to equity, credit and asset valuation")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts","🧮 DCF Analyser","📊 Comps Tool","🧪 Worked Example","❓ Quiz"
    ])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Valuation Methodologies", "🏦")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**DCF Formula**
```
EV = Σ FCFt / (1+WACC)^t  +  TV / (1+WACC)^n

FCF  = EBIT×(1−Tax) + D&A − CapEx − ΔNWC
TV   = FCFn×(1+g) / (WACC−g)   [Gordon Growth]

WACC = Ke×E/(D+E) + Kd×(1−t)×D/(D+E)
Ke   = Rf + β×(Rm−Rf)           [CAPM]
```
**Sensitivity order (highest → lowest):**
1. WACC
2. Terminal growth rate
3. Terminal EBITDA margin
4. CapEx intensity
            """)
        with c2:
            st.markdown("""
**Comparable Company Multiples**
| Multiple   | Best Used For                  |
|------------|-------------------------------|
| EV/Revenue | High-growth, low/neg margin   |
| EV/EBITDA  | Mature, capital-light          |
| EV/EBIT    | Capital-intensive sectors      |
| P/E        | Listed equities                |
| P/BV       | Banks, insurance               |
| EV/FCF     | Cash-generative businesses     |

**Earnings Quality Flags**
- Accruals ratio = (Net Income − CFO) / Assets
  → > 5% is a red flag for aggressive accounting
- Cash conversion < 0.8× → earnings not converting
- Revenue growing faster than cash collections
            """)
        _sec("Equity Factor Analytics", "📐")
        st.dataframe(pd.DataFrame({
            "Factor":           ["Value","Momentum","Quality","Size","Low Volatility"],
            "Definition":       ["Cheap vs fundamentals (P/B, P/E, P/CF)",
                                  "Recent price outperformance over 6–12 months",
                                  "High ROE, stable earnings, low debt",
                                  "Small-cap premium over large-cap",
                                  "Low beta / low realised volatility"],
            "Historical Premium": ["+3–4% pa","+4–5% pa","+2–3% pa","+2–3% pa","+1–2% pa"],
            "Underperforms When": ["Growth/tech bull markets","Market reversals",
                                    "Leveraged growth rewarded","Large-cap dominates",
                                    "Bull market with strong momentum"],
        }), use_container_width=True, hide_index=True)

    # ── DCF ANALYSER ──────────────────────────────────────────────────────────
    with tab2:
        _sec("DCF Sensitivity Analyser", "🧮")
        c1, c2, c3 = st.columns(3)
        with c1:
            be = st.number_input("Current EBITDA ($M)", value=100.0, step=5.0)
            eg = st.slider("EBITDA CAGR (%)", 0.0, 30.0, 8.0)
            fy = st.slider("Forecast years", 3, 10, 5)
        with c2:
            wc = st.slider("WACC (%)", 5.0, 20.0, 10.0)
            tg = st.slider("Terminal growth rate (%)", 0.0, 5.0, 2.5)
            tx = st.slider("Tax rate (%)", 15.0, 40.0, 25.0)
        with c3:
            cp = st.slider("CapEx as % EBITDA", 5.0, 50.0, 20.0)
            dp = st.slider("D&A as % EBITDA", 5.0, 30.0, 12.0)
            np2= st.slider("NWC change as % EBITDA", 0.0, 20.0, 5.0)
            nd = st.number_input("Net Debt ($M)", value=150.0, step=10.0)

        pv = 0.0
        for yr in range(1, fy+1):
            ebitda = be * ((1+eg/100)**yr)
            da     = ebitda * dp/100
            nopat  = (ebitda - da) * (1 - tx/100)
            fcf    = nopat + da - ebitda*cp/100 - ebitda*np2/100
            pv    += fcf / (1+wc/100)**yr

        t_ebitda = be * ((1+eg/100)**fy)
        t_da     = t_ebitda * dp/100
        t_nopat  = (t_ebitda - t_da) * (1 - tx/100)
        t_fcf    = t_nopat + t_da - t_ebitda*cp/100 - t_ebitda*np2/100
        pv_tv    = (t_fcf*(1+tg/100) / ((wc-tg)/100)) / (1+wc/100)**fy
        ev       = pv + pv_tv
        equity   = ev - nd
        tv_pct   = pv_tv / ev * 100

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Enterprise Value",     f"${ev:,.0f}M")
        c2.metric("PV of FCFs",           f"${pv:,.0f}M")
        c3.metric("PV Terminal Value",    f"${pv_tv:,.0f}M")
        c4.metric("Equity Value",         f"${equity:,.0f}M")

        if tv_pct > 80:
            st.warning(f"⚠️ Terminal value = {tv_pct:.1f}% of EV. Highly sensitive to WACC and growth assumptions.")
        else:
            st.success(f"✅ Terminal value = {tv_pct:.1f}% of EV. Reasonable balance.")

        st.markdown("**EV Sensitivity Table ($M) — WACC vs Terminal Growth**")
        waccs   = [wc-2, wc-1, wc, wc+1, wc+2]
        growths = [tg-1, tg-0.5, tg, tg+0.5, tg+1]
        tbl = {}
        for g in growths:
            row = []
            for w in waccs:
                if w <= g: row.append("N/A")
                else:
                    tv_s = (t_fcf*(1+g/100)/((w-g)/100)) / (1+w/100)**fy
                    row.append(f"${pv+tv_s:,.0f}M")
            tbl[f"g={g:.1f}%"] = row
        st.dataframe(pd.DataFrame(tbl, index=[f"WACC={w:.1f}%" for w in waccs]),
                     use_container_width=True)

    # ── COMPS TOOL ────────────────────────────────────────────────────────────
    with tab3:
        _sec("Comparable Company Analysis", "📊")
        c1, c2 = st.columns(2)
        with c1: te = st.number_input("Target EBITDA ($M)", value=85.0, step=5.0)
        with c2: tr = st.number_input("Target Revenue ($M)", value=400.0, step=10.0)

        comps = pd.DataFrame({
            "Company":      ["Alpha Corp","Beta Industries","Gamma Ltd","Delta Group","Epsilon PLC"],
            "EV ($M)":      [1200, 850, 2100, 600, 1750],
            "Revenue ($M)": [380, 270, 650, 195, 550],
            "EBITDA ($M)":  [95, 68, 175, 52, 140],
        })
        comps["EV/Revenue"] = (comps["EV ($M)"] / comps["Revenue ($M)"]).round(2)
        comps["EV/EBITDA"]  = (comps["EV ($M)"] / comps["EBITDA ($M)"]).round(2)
        st.dataframe(comps, use_container_width=True, hide_index=True)

        me = comps["EV/EBITDA"].median()
        mr = comps["EV/Revenue"].median()
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Median EV/EBITDA",     f"{me:.1f}x")
        c2.metric("Implied EV (EBITDA)",  f"${te*me:,.0f}M")
        c3.metric("Median EV/Revenue",    f"{mr:.1f}x")
        c4.metric("Implied EV (Revenue)", f"${tr*mr:,.0f}M")

        fig = go.Figure(go.Bar(x=comps["Company"], y=comps["EV/EBITDA"],
                               marker_color="#185FA5",
                               text=[f"{v:.1f}x" for v in comps["EV/EBITDA"]],
                               textposition="outside"))
        fig.add_hline(y=me, line_dash="dash", line_color="#1D9E75",
                      annotation_text=f"Median: {me:.1f}x")
        fig.update_layout(title="EV/EBITDA Trading Multiples — Comparable Companies",
                          yaxis_title="EV/EBITDA (x)", template="plotly_white", height=360)
        st.plotly_chart(fig, use_container_width=True)

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Acquisition Valuation — TechTarget Ltd", "🧪")

        st.markdown("""
**Business Situation:** Your company is considering acquiring **TechTarget Ltd**, a B2B software
business. The M&A team needs a valuation range to set the bid price.
You run a full valuation using three methods: DCF, EV/EBITDA comps, and EV/Revenue comps.
        """)

        st.markdown("**Target Company Financial Profile**")
        fin_df = pd.DataFrame({
            "Metric":   ["Revenue","EBITDA","EBITDA Margin","Net Debt","Revenue Growth (3yr CAGR)","FCF Conversion"],
            "FY2022":   ["$180M","$32M","17.8%","$45M","—","72%"],
            "FY2023":   ["$210M","$40M","19.0%","$38M","16.7%","78%"],
            "FY2024E":  ["$245M","$51M","20.8%","$30M","16.7%","81%"],
        })
        st.dataframe(fin_df, use_container_width=True, hide_index=True)

        st.markdown("**Method 1 — DCF Valuation**")
        ebitda_base = 51; ebitda_cagr = 12; years = 5
        wacc_dcf = 10.5; tg_dcf = 2.5; tax = 25; capex_pct = 18; da_pct = 10; nwc_pct = 4; net_debt = 30

        pv_fcf = 0
        fcf_table = []
        for yr in range(1, years+1):
            ebitda = ebitda_base * (1+ebitda_cagr/100)**yr
            da     = ebitda * da_pct/100
            nopat  = (ebitda - da) * (1-tax/100)
            fcf    = nopat + da - ebitda*capex_pct/100 - ebitda*nwc_pct/100
            pv     = fcf / (1+wacc_dcf/100)**yr
            pv_fcf += pv
            fcf_table.append({"Year": f"FY{2024+yr}", "EBITDA ($M)": round(ebitda,1),
                               "FCF ($M)": round(fcf,1), "PV of FCF ($M)": round(pv,1)})
        t_ebitda = ebitda_base * (1+ebitda_cagr/100)**years
        t_da     = t_ebitda * da_pct/100
        t_fcf    = (t_ebitda-t_da)*(1-tax/100) + t_da - t_ebitda*capex_pct/100 - t_ebitda*nwc_pct/100
        pv_tv_dcf = (t_fcf*(1+tg_dcf/100)/((wacc_dcf-tg_dcf)/100)) / (1+wacc_dcf/100)**years
        ev_dcf   = pv_fcf + pv_tv_dcf
        eq_dcf   = ev_dcf - net_debt

        st.dataframe(pd.DataFrame(fcf_table), use_container_width=True, hide_index=True)
        c1,c2,c3 = st.columns(3)
        c1.metric("PV of FCFs",          f"${pv_fcf:.0f}M")
        c2.metric("PV of Terminal Value", f"${pv_tv_dcf:.0f}M ({pv_tv_dcf/ev_dcf*100:.0f}% of EV)")
        c3.metric("DCF Equity Value",     f"${eq_dcf:.0f}M")

        st.markdown("**Method 2 — Comparable Company Multiples**")
        sector_comps = pd.DataFrame({
            "Company":    ["SoftCo A","SoftCo B","SoftCo C","SoftCo D","SoftCo E"],
            "EV/EBITDA":  [18.2, 21.5, 16.8, 22.1, 19.4],
            "EV/Revenue": [3.8, 4.5, 3.2, 4.8, 4.1],
        })
        med_evebitda = sector_comps["EV/EBITDA"].median()
        med_evrev    = sector_comps["EV/Revenue"].median()
        ev_comps_ebitda  = 51 * med_evebitda
        ev_comps_revenue = 245 * med_evrev
        eq_comps_ebitda  = ev_comps_ebitda  - net_debt
        eq_comps_revenue = ev_comps_revenue - net_debt

        st.dataframe(sector_comps, use_container_width=True, hide_index=True)
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Median EV/EBITDA",    f"{med_evebitda:.1f}x")
        c2.metric("Implied Equity Value", f"${eq_comps_ebitda:.0f}M")
        c3.metric("Median EV/Revenue",   f"{med_evrev:.1f}x")
        c4.metric("Implied Equity Value", f"${eq_comps_revenue:.0f}M")

        st.markdown("**Method 3 — Valuation Football Field**")
        methods = ["DCF", "EV/EBITDA Comps", "EV/Revenue Comps"]
        low_vals = [eq_dcf * 0.85, eq_comps_ebitda * 0.90, eq_comps_revenue * 0.90]
        high_vals= [eq_dcf * 1.15, eq_comps_ebitda * 1.10, eq_comps_revenue * 1.10]
        mid_vals = [(l+h)/2 for l,h in zip(low_vals, high_vals)]

        fig = go.Figure()
        for i, method in enumerate(methods):
            fig.add_trace(go.Bar(
                name=method, x=[high_vals[i]-low_vals[i]], y=[method],
                base=[low_vals[i]], orientation="h",
                marker_color=["#185FA5","#1D9E75","#BA7517"][i],
                text=[f"${low_vals[i]:.0f}M – ${high_vals[i]:.0f}M"],
                textposition="inside",
            ))
        fig.add_vline(x=np.mean(mid_vals), line_dash="dash", line_color="red",
                      annotation_text=f"Mid-point avg: ${np.mean(mid_vals):.0f}M")
        fig.update_layout(title="Valuation Football Field — Equity Value Range ($M)",
                          xaxis_title="Equity Value ($M)", barmode="overlay",
                          template="plotly_white", height=320, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

        st.success(f"""
**📋 Valuation Summary & Bid Recommendation:**

| Method           | Equity Value Range   | Mid-Point  |
|------------------|----------------------|------------|
| DCF              | ${eq_dcf*0.85:.0f}M – ${eq_dcf*1.15:.0f}M | ${eq_dcf:.0f}M |
| EV/EBITDA Comps  | ${eq_comps_ebitda*0.9:.0f}M – ${eq_comps_ebitda*1.1:.0f}M | ${eq_comps_ebitda:.0f}M |
| EV/Revenue Comps | ${eq_comps_revenue*0.9:.0f}M – ${eq_comps_revenue*1.1:.0f}M | ${eq_comps_revenue:.0f}M |

**Recommended bid range:** ${np.mean(mid_vals)*0.95:.0f}M – ${np.mean(mid_vals)*1.05:.0f}M

**Key risks to value:** Revenue growth deceleration below 10% CAGR (DCF is very sensitive), or WACC rising 2pp due to rate environment (reduces equity value by ~${eq_dcf*0.18:.0f}M).
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 6 Quiz", "❓")
        _quiz("1. Which variable has the highest sensitivity on DCF Enterprise Value?",
              ["Year 1 revenue growth","Tax rate","WACC","D&A as % EBITDA"],
              "WACC","m6q1")
        st.divider()
        _quiz("2. Net Income=$50M, CFO=$15M, Avg Assets=$500M. Accruals ratio?",
              ["0.03","0.07","0.10","0.30"],"0.07","m6q2")
        st.divider()
        _quiz("3. EV/Revenue is preferred over EV/EBITDA when:",
              ["Company is highly profitable",
               "Company is high-growth with negative or minimal EBITDA",
               "Company has stable cash flows","Interest rates are rising"],
              "Company is high-growth with negative or minimal EBITDA","m6q3")
        st.divider()
        _quiz("4. The Value factor means buying stocks that are:",
              ["Growing faster than market",
               "Cheap relative to fundamentals like book value or earnings",
               "Less volatile than the index","Recently outperforming peers"],
              "Cheap relative to fundamentals like book value or earnings","m6q4")
        st.divider()
        _quiz("5. Terminal Value = 85% of Enterprise Value in a DCF. This means:",
              ["The model is very reliable",
               "The model is heavily sensitive to WACC and long-term growth assumptions",
               "Near-term cash flows are intentionally low",
               "The DCF is below the comps range"],
              "The model is heavily sensitive to WACC and long-term growth assumptions","m6q5")