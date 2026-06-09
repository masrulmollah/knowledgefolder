import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

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
    st.title("🏆 Module 2: Comparative & Benchmarking Analytics")
    st.caption("Understand relative performance — against peers, internal units, and market benchmarks")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts", "🧮 Peer Benchmarker", "📊 BCG Matrix", "🧪 Worked Example", "❓ Quiz"])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("Types of Benchmarking", "📐")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Internal Cross-Sectional Analytics**

*Same-Block / Cross-Block Cohort Analysis:*
Comparing identical operational units against each other at the same point in time.
- Factory A vs. Factory B vs. Factory C — cost per unit, OEE %
- Region North vs. Region South vs. Region East — revenue per rep
- Channel: Direct vs. Distribution vs. E-commerce — contribution margin

*Purpose:* Isolates which unit is the best performer and why — enabling best-practice replication.

**Portfolio Rationalization:**
| Tool | What It Shows |
|------|---------------|
| BCG Matrix | Growth rate vs. relative market share |
| Contribution Margin Ranking | Best and worst SKUs by absolute margin |
| Pareto (80/20) | Which 20% of SKUs drive 80% of profit |
| Margin per Capacity Minute | True profitability per unit of constrained resource |
            """)
        with c2:
            st.markdown("""
**External & Market Benchmarking**

*Peer Group Analysis:*
Comparing financial ratios and cost structures against direct competitors of similar scale.
Key metrics: EBITDA margin, COGS%, Capex/Revenue, DSO, net debt/EBITDA.

*Best-in-Class Benchmarking:*
Comparing specific operational costs (e.g. procurement, logistics) against world-class standards
— regardless of geography or industry. Identifies structural improvement potential.

*Macro-Market Correlation:*
| External Driver | Internal Metric |
|-----------------|-----------------|
| CPI / Inflation index | Input cost trends |
| Commodity exchange prices | Raw material cost vs. market |
| GDP growth / PMI | Revenue growth rate |
| FX rates | Export revenue, import cost |
| Interest rate cycle | Finance charges, working capital cost |

*Key rule:* Correlation ≠ causation. Use external data as a signal, not a conclusion.
            """)

        _sec("Benchmarking Quadrant Framework", "📊")
        st.markdown("""
When benchmarking a business unit or product, plot it on two dimensions simultaneously:

| | **Above Benchmark on Metric A** | **Below Benchmark on Metric A** |
|--|--|--|
| **Above Benchmark on Metric B** | ⭐ Star: protect and invest | 🔄 Mixed: fix metric A |
| **Below Benchmark on Metric B** | 🔄 Mixed: fix metric B | 🔴 Problem: urgent intervention |

This 2×2 approach forces prioritisation and avoids single-metric tunnel vision.
        """)
        st.info("💡 Best practice: benchmark on at least 3 dimensions — profitability, efficiency, and growth. A unit that looks weak on margins may be a strong growth engine, or vice versa.")

    # ── PEER BENCHMARKER ──────────────────────────────────────────────────────
    with tab2:
        _sec("Peer Group Ratio Benchmarker", "🧮")
        st.markdown("Compare your company against up to 5 peers across key financial ratios:")

        companies = ["Your Company", "Peer A", "Peer B", "Peer C", "Peer D", "Peer E"]
        defaults = {
            "Revenue ($M)":      [545, 620, 480, 890, 310, 750],
            "EBITDA Margin %":   [22.8, 19.5, 24.1, 17.2, 28.4, 21.0],
            "Net Margin %":      [11.4, 9.2, 12.8, 8.5, 15.1, 10.3],
            "DSO (days)":        [38, 45, 32, 52, 28, 41],
            "DIO (days)":        [42, 55, 38, 61, 34, 49],
            "Debt/EBITDA":       [1.8, 2.4, 1.2, 3.1, 0.9, 2.0],
            "Revenue Growth %":  [9.4, 6.2, 11.5, 5.1, 14.2, 8.0],
        }

        input_data = {}
        for metric, defs in defaults.items():
            cols = st.columns(6)
            st.markdown(f"**{metric}**")
            row = []
            c2s = st.columns(6)
            for i, (co, d) in enumerate(zip(companies, defs)):
                with c2s[i]:
                    val = st.number_input(co, value=float(d), key=f"bm_{metric}_{i}",
                                         label_visibility="visible" if i==0 else "visible")
                    row.append(val)
            input_data[metric] = row

        df_bench = pd.DataFrame(input_data, index=companies)

        st.markdown("**Ranking Table (Your Company highlighted)**")
        rank_data = []
        for metric in defaults.keys():
            vals = input_data[metric]
            your_val = vals[0]
            better_higher = metric not in ["DSO (days)", "DIO (days)", "Debt/EBITDA"]
            sorted_vals = sorted(vals, reverse=better_higher)
            rank = sorted_vals.index(your_val) + 1
            percentile = (1 - (rank-1)/len(companies)) * 100
            rank_data.append({
                "Metric": metric,
                "Your Company": your_val,
                "Peer Avg": round(np.mean(vals[1:]), 1),
                "Best in Group": max(vals) if better_higher else min(vals),
                "Rank": f"{rank} / {len(companies)}",
                "Percentile": f"{percentile:.0f}th",
                "vs. Peer Avg": "✅ Better" if (your_val > np.mean(vals[1:]) and better_higher) or
                                              (your_val < np.mean(vals[1:]) and not better_higher)
                               else "🔴 Weaker",
            })
        st.dataframe(pd.DataFrame(rank_data), use_container_width=True, hide_index=True)

        # Spider / radar chart
        metrics_radar = ["EBITDA Margin %", "Net Margin %", "Revenue Growth %"]
        your_vals_r = [input_data[m][0] for m in metrics_radar]
        peer_avg_r  = [np.mean(input_data[m][1:]) for m in metrics_radar]

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=metrics_radar, y=your_vals_r, name="Your Company",
            marker_color="#185FA5", text=[f"{v:.1f}" for v in your_vals_r], textposition="outside"))
        fig.add_trace(go.Bar(
            x=metrics_radar, y=peer_avg_r, name="Peer Average",
            marker_color="#B5D4F4", text=[f"{v:.1f}" for v in peer_avg_r], textposition="outside"))
        fig.update_layout(title="Your Company vs. Peer Average — Key Margin Metrics",
                          barmode="group", template="plotly_white", height=380)
        st.plotly_chart(fig, use_container_width=True)

    # ── BCG MATRIX ────────────────────────────────────────────────────────────
    with tab3:
        _sec("BCG Matrix — Product Portfolio Mapping", "📊")
        st.markdown("Map your product portfolio by market growth rate vs. relative market share:")

        product_names = ["Product Alpha","Product Beta","Product Gamma","Product Delta","Product Epsilon"]
        defaults_bcg = {
            "Market Growth %":        [18, 22, 5, 8, 15],
            "Relative Market Share":  [1.8, 0.6, 1.5, 0.4, 0.9],
            "Revenue ($M)":           [120, 45, 210, 30, 75],
        }

        input_bcg = {}
        for metric, defs in defaults_bcg.items():
            st.markdown(f"**{metric}**")
            cols2 = st.columns(5)
            row = []
            for i, (nm, d) in enumerate(zip(product_names, defs)):
                with cols2[i]:
                    v = st.number_input(nm, value=float(d), key=f"bcg_{metric}_{i}",
                                        label_visibility="visible")
                    row.append(v)
            input_bcg[metric] = row

        growth = input_bcg["Market Growth %"]
        share  = input_bcg["Relative Market Share"]
        sizes  = input_bcg["Revenue ($M)"]

        def bcg_quadrant(g, s):
            if g >= 10 and s >= 1.0: return "⭐ Star"
            elif g >= 10 and s < 1.0: return "❓ Question Mark"
            elif g < 10 and s >= 1.0: return "🐄 Cash Cow"
            else: return "🐕 Dog"

        quadrants = [bcg_quadrant(g, s) for g, s in zip(growth, share)]

        colors_map = {"⭐ Star":"#1D9E75","❓ Question Mark":"#EF9F27","🐄 Cash Cow":"#185FA5","🐕 Dog":"#E24B4A"}
        fig = go.Figure()
        for i, nm in enumerate(product_names):
            fig.add_trace(go.Scatter(
                x=[share[i]], y=[growth[i]],
                mode="markers+text",
                marker=dict(size=max(sizes[i]/5, 15), color=colors_map[quadrants[i]], opacity=0.8,
                            line=dict(color="white", width=2)),
                text=[f"{nm}<br>{quadrants[i]}"],
                textposition="top center",
                name=nm,
                showlegend=True,
            ))

        fig.add_hline(y=10, line_dash="dash", line_color="gray", annotation_text="Growth threshold (10%)")
        fig.add_vline(x=1.0, line_dash="dash", line_color="gray", annotation_text="Market share threshold (1.0×)")
        fig.update_layout(
            title="BCG Matrix — Product Portfolio (bubble size = revenue)",
            xaxis_title="Relative Market Share (higher = stronger)",
            yaxis_title="Market Growth Rate (%)",
            template="plotly_white", height=480,
            annotations=[
                dict(x=0.3, y=22, text="❓ Question Marks", showarrow=False, font=dict(size=10, color="gray")),
                dict(x=1.8, y=22, text="⭐ Stars", showarrow=False, font=dict(size=10, color="gray")),
                dict(x=0.3, y=3,  text="🐕 Dogs", showarrow=False, font=dict(size=10, color="gray")),
                dict(x=1.8, y=3,  text="🐄 Cash Cows", showarrow=False, font=dict(size=10, color="gray")),
            ]
        )
        st.plotly_chart(fig, use_container_width=True)

        bcg_df = pd.DataFrame({
            "Product": product_names,
            "Growth %": growth, "Rel. Share": share, "Revenue ($M)": sizes,
            "BCG Category": quadrants,
            "Strategic Action": [
                "Invest to maintain leadership" if q=="⭐ Star" else
                "Harvest cash, minimal reinvestment" if q=="🐄 Cash Cow" else
                "Invest selectively or divest" if q=="❓ Question Mark" else
                "Consider divestment or repositioning"
                for q in quadrants]
        })
        st.dataframe(bcg_df, use_container_width=True, hide_index=True)

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Factory Benchmarking — Global Cement Group", "🧪")
        st.markdown("""
**Business Situation:** You are the Group Manufacturing Analytics Manager.
The COO wants to know which of the 5 factories is most efficient, why, and what the worst performers need to do.
You have a single dataset: one year of operational and financial data across 5 plants.
        """)

        factories = ["Plant Mumbai","Plant Jakarta","Plant Cairo","Plant São Paulo","Plant Karachi"]
        data = {
            "Plant": factories,
            "Production (kT)":    [850, 720, 640, 910, 580],
            "Cost/Ton ($)":       [38.2, 44.5, 51.3, 36.8, 57.1],
            "OEE %":              [82, 74, 66, 85, 61],
            "Energy $/Ton":       [12.1, 15.8, 18.4, 11.6, 21.2],
            "Waste %":            [3.1, 4.8, 6.2, 2.9, 7.5],
            "On-time Delivery %": [94, 88, 82, 96, 78],
        }
        df_fact = pd.DataFrame(data)

        st.markdown("**Step 1 — Raw Performance Data**")
        st.dataframe(df_fact, use_container_width=True, hide_index=True)

        st.markdown("**Step 2 — Benchmarking Heatmap (Green = best, Red = worst)**")
        metrics_to_rank = ["Cost/Ton ($)","OEE %","Energy $/Ton","Waste %","On-time Delivery %"]
        rank_matrix = pd.DataFrame(index=factories)
        for m in metrics_to_rank:
            ascending = m not in ["OEE %","On-time Delivery %"]
            ranks = pd.Series(data[m]).rank(ascending=ascending)
            rank_matrix[m] = ranks.values

        fig_heat = px.imshow(
            rank_matrix.T.astype(float),
            x=factories, y=metrics_to_rank,
            color_continuous_scale="RdYlGn_r",
            title="Plant Benchmarking Heatmap (1=Best, 5=Worst)",
            text_auto=True,
            aspect="auto",
        )
        fig_heat.update_layout(template="plotly_white", height=360)
        st.plotly_chart(fig_heat, use_container_width=True)

        st.markdown("**Step 3 — Overall Efficiency Score**")
        rank_matrix["Total Score"] = rank_matrix.sum(axis=1)
        rank_matrix["Rank"] = rank_matrix["Total Score"].rank()
        score_df = rank_matrix[["Total Score","Rank"]].reset_index()
        score_df.columns = ["Plant","Total Rank Score","Overall Rank"]
        score_df["Overall Rank"] = score_df["Overall Rank"].astype(int)
        score_df = score_df.sort_values("Overall Rank")
        st.dataframe(score_df, use_container_width=True, hide_index=True)

        st.markdown("**Step 4 — Cost Gap to Best-in-Class ($)**")
        best_cost = min(data["Cost/Ton ($)"])
        gaps = [round((c - best_cost) * v, 0) for c, v in zip(data["Cost/Ton ($)"], data["Production (kT)"])]
        fig2 = go.Figure(go.Bar(
            x=factories, y=gaps,
            marker_color=["#1D9E75" if g==0 else "#E24B4A" for g in gaps],
            text=[f"${g:,.0f}K" for g in gaps], textposition="outside"))
        fig2.update_layout(title="Annual Cost Gap vs. Best-in-Class Plant Mumbai ($K)",
                           yaxis_title="Cost Gap ($K)", template="plotly_white", height=360)
        st.plotly_chart(fig2, use_container_width=True)

        total_saving = sum(g for g in gaps if g > 0)
        st.success(f"""
**COO Briefing — Factory Benchmarking Findings**

- **Best performer:** Plant Mumbai — lowest cost/ton ($38.2), highest OEE (82%), lowest waste (3.1%)
- **Worst performer:** Plant Karachi — cost/ton 49% above Mumbai, OEE 21pp below, waste 2.4× higher
- **Key opportunity:** If Plant Karachi and Plant Cairo reach Plant Mumbai's cost/ton levels, total annual saving = **${total_saving/1000:,.0f}M**
- **Priority actions:** (1) Energy audit at Karachi — $21.2/ton vs $11.6/ton benchmark is the single largest gap. (2) OEE improvement programme at Karachi and Cairo. (3) Root cause analysis on waste % — target <4% across all plants.
        """)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 2 Quiz", "❓")
        _quiz("1. A 'Cash Cow' in the BCG matrix has:",
              ["High growth, high market share",
               "Low growth, high relative market share",
               "High growth, low market share",
               "Low growth, low market share"],
              "Low growth, high relative market share", "fa_m2q1")
        st.divider()
        _quiz("2. Best-in-class benchmarking differs from peer benchmarking because:",
              ["It uses only internal data",
               "It compares against world-class standards regardless of industry",
               "It focuses only on revenue metrics",
               "It is limited to companies of the same size"],
              "It compares against world-class standards regardless of industry", "fa_m2q2")
        st.divider()
        _quiz("3. Your EBITDA margin is 18% vs. peer average of 22%. This tells you:",
              ["You have a structural cost disadvantage — investigate COGS and SG&A",
               "Your revenue is too low",
               "Your peers are overpriced",
               "Nothing — margins are irrelevant"],
              "You have a structural cost disadvantage — investigate COGS and SG&A", "fa_m2q3")
        st.divider()
        _quiz("4. Cross-block comparison (e.g. Factory A vs Factory B) is most useful for:",
              ["Forecasting next year's revenue",
               "Identifying which unit has a structural cost advantage to replicate",
               "Calculating tax provisions",
               "Fraud detection"],
              "Identifying which unit has a structural cost advantage to replicate", "fa_m2q4")
        st.divider()
        _quiz("5. Macro correlation analysis linking internal revenue growth to GDP growth helps to:",
              ["Prove that GDP drives revenue",
               "Quantify how much of revenue growth is market-driven vs. company-specific",
               "Replace the need for a budget",
               "Calculate interest expense"],
              "Quantify how much of revenue growth is market-driven vs. company-specific", "fa_m2q5")