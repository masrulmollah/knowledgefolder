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
    st.title("📣 Module 9: Insight Communication & Storytelling")
    st.caption("Turn analysis into decisions — the most underrated skill in finance")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Concepts","🧮 Chart Critique","📊 Story Builder","🧪 Worked Example","❓ Quiz",
    ])

    # ── CONCEPTS ──────────────────────────────────────────────────────────────
    with tab1:
        _sec("The Pyramid Principle", "🔺")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
**Lead with the answer — not the analysis:**
```
LEVEL 1 — HEADLINE  (the so-what)
  "EBITDA will miss budget by $42M in FY24"

LEVEL 2 — KEY ARGUMENTS  (the evidence)
  ├── Volume shortfall Mid-Market  (−$22M)
  ├── Input cost inflation COGS    (−$12M)
  └── SGA over-run from hiring     (−$8M)

LEVEL 3 — SUPPORTING DATA
  ├── Churn data by customer cohort
  ├── Commodity price index vs budget
  └── Headcount vs plan by month
```
**Rule:** Most finance presentations reveal the
conclusion last. Executives want the headline first.
            """)
        with c2:
            st.markdown("""
**SCR Framework for Executive Summaries**
| Element | Purpose | Example |
|---------|---------|---------|
| **S**ituation | Shared context | "Q3 closed. Revenue = $482M." |
| **C**omplication | The tension | "This is $18M (4%) below budget." |
| **R**esolution | Recommended action | "3-point plan to close the gap." |

**One-number-per-slide rule**
Every slide answers ONE question with ONE key number.
If a slide needs two numbers, make two slides.

**Direct labelling rule**
Label chart lines and bars directly on the chart.
Never use a legend when you can annotate instead.
            """)

        _sec("Chart Design Principles", "🎨")
        st.dataframe(pd.DataFrame({
            "Principle":        ["Data-ink ratio","Pre-attentive attributes","Colour as signal",
                                  "Zero-based axes","Direct labelling","Declutter gridlines"],
            "What it means":    ["Maximise ink used for data, not decoration",
                                  "Use size, colour and position to guide the eye before conscious reading",
                                  "Use colour only to encode meaning. Max 3–4 colours per chart.",
                                  "Bar charts must start at zero — truncating exaggerates differences",
                                  "Label data directly on chart; avoid legends where possible",
                                  "Use light grey lines only where they add value — or remove entirely"],
            "Finance Example":  ["Remove chart border, background colour, 3D effects, gridlines",
                                  "Highlight the current year bar blue; make prior years light grey",
                                  "Red = adverse variance, Green = favourable, Blue = neutral/actual",
                                  "A revenue bar chart cut off at $450M when data starts at $480M is misleading",
                                  "Write '$142M' directly on the bar; not in a colour-coded legend",
                                  "Light grey horizontal lines at 25%/50%/75% only — or none at all"],
        }), use_container_width=True, hide_index=True)

        _sec("7 Most Costly Communication Errors in Finance", "⚠️")
        st.error("""
1. **Presenting data before the conclusion** — executives skim; put your answer in the slide title
2. **Too many numbers on one slide** — working memory holds 5–7 items; ruthlessly cut
3. **Pie charts with more than 4 slices** — use a sorted horizontal bar chart instead
4. **Dual-axis charts** — almost always misleading; use two separate charts
5. **Colour-only signalling** — ~8% of men are colour-blind; add labels or shapes too
6. **Using absolute values when % change is the story** — or vice versa
7. **Data without insight** — "Revenue was $482M" vs "Revenue missed by 4%, driven by Mid-Market churn"
        """)

    # ── CHART CRITIQUE ────────────────────────────────────────────────────────
    with tab2:
        _sec("Good vs Bad Chart — Interactive Comparison", "🧮")
        choice = st.selectbox("Select scenario", [
            "Revenue split — Pie vs Sorted Bar",
            "Trend over time — Cluttered vs Clean",
            "Variance reporting — Raw table vs Visual",
        ])
        np.random.seed(1)

        if choice == "Revenue split — Pie vs Sorted Bar":
            labels = ["APAC","EMEA","Americas","MEA","LatAm"]
            values = [320, 280, 410, 95, 75]
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**❌ Pie Chart — Hard to compare**")
                fig = go.Figure(go.Pie(labels=labels, values=values, textinfo="label+percent"))
                fig.update_layout(height=320, title="Revenue by Region")
                st.plotly_chart(fig, use_container_width=True)
                st.caption("Problem: Hard to compare APAC vs EMEA (similar sizes). No absolute values. Reader must scan legend.")
            with c2:
                st.markdown("**✅ Sorted Bar — Instantly comparable**")
                df_b = pd.DataFrame({"Region":labels,"Rev":values}).sort_values("Rev",ascending=True)
                colours = ["#185FA5" if r=="Americas" else "#B0C4DE" for r in df_b["Region"]]
                fig = go.Figure(go.Bar(
                    x=df_b["Rev"], y=df_b["Region"], orientation="h",
                    marker_color=colours,
                    text=[f"${v}M" for v in df_b["Rev"]], textposition="outside"))
                fig.update_layout(height=320, title="Americas leads at $410M",
                                  xaxis=dict(range=[0,520]),
                                  template="plotly_white", showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
                st.caption("Fix: Bar lengths are easy to compare. Key item highlighted blue. Values labelled directly. Sorted.")

        elif choice == "Trend over time — Cluttered vs Clean":
            dates = pd.date_range("2022-01-01", periods=24, freq="MS")
            rev   = 400 + np.cumsum(np.random.randn(24)*8+3)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**❌ Cluttered — Chart junk everywhere**")
                fig = go.Figure(go.Scatter(x=dates, y=rev, mode="lines+markers",
                    line=dict(color="red",width=3,dash="dot"),
                    marker=dict(size=10,symbol="diamond")))
                fig.update_layout(height=320,
                    title="Revenue Monthly Data 2022-2024 Detailed Analysis Period Report",
                    plot_bgcolor="lightgrey", paper_bgcolor="lightyellow",
                    font=dict(size=9))
                st.plotly_chart(fig, use_container_width=True)
                st.caption("Problems: Distracting background, oversized markers, vague topic title with no insight.")
            with c2:
                st.markdown("**✅ Clean — Insight-driven**")
                fig = go.Figure(go.Scatter(x=dates, y=rev, mode="lines",
                    line=dict(color="#185FA5",width=2.5)))
                fig.add_annotation(x=dates[-1], y=rev[-1],
                    text=f"  ${rev[-1]:.0f}M", showarrow=False,
                    xanchor="left", font=dict(color="#185FA5",size=13))
                fig.update_layout(height=320,
                    title="Revenue up 14% over 24 months — growth accelerating H2 2024",
                    template="plotly_white",
                    yaxis=dict(range=[0,None]), showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
                st.caption("Fix: Clean background, insight in title, direct annotation, zero-based axis, no chart junk.")

        else:
            divs2 = ["APAC","EMEA","Americas","MEA"]
            bgt   = [180, 220, 300, 80]
            act   = [165, 235, 291, 72]
            var   = [a-b for a,b in zip(act,bgt)]
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**❌ Raw Data Table — Reader does all the work**")
                tbl = pd.DataFrame({"Division":divs2,"Budget ($M)":bgt,
                                     "Actual ($M)":act,"Variance ($M)":var})
                st.dataframe(tbl, use_container_width=True, hide_index=True)
                st.caption("Problem: No visual hierarchy. Reader must calculate % variances mentally. No instant signal of what matters.")
            with c2:
                st.markdown("**✅ Annotated Variance Chart — Instant signal**")
                fig = go.Figure(go.Bar(
                    x=divs2, y=var,
                    marker_color=["#1D9E75" if v>0 else "#E24B4A" for v in var],
                    text=[f"${v:+}M" for v in var], textposition="outside"))
                fig.add_hline(y=0, line_color="black", line_width=1)
                fig.update_layout(height=320, yaxis=dict(range=[-30,22]),
                    title="EMEA outperformed (+$15M); Americas & APAC missed",
                    template="plotly_white", showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
                st.caption("Fix: Red/green gives instant signal. Magnitude easy to compare. Insight-driven title. No mental arithmetic.")

    # ── STORY BUILDER ─────────────────────────────────────────────────────────
    with tab3:
        _sec("SCR Executive Summary Builder", "📊")
        st.markdown("Build a structured financial narrative using the Situation-Complication-Resolution framework.")
        c1, c2 = st.columns(2)
        with c1:
            sit = st.text_area("**S — Situation** (shared context — what is the backdrop?)",
                value="Q3 FY2024 is now closed. Group revenue came in at $482M and EBITDA at $94M.")
            com = st.text_area("**C — Complication** (the tension — what is the problem?)",
                value="Revenue missed budget by $18M (−4%) and EBITDA by $42M (−31%). This is the second consecutive quarter of underperformance against plan.")
            res = st.text_area("**R — Resolution** (recommended action — what should we do?)",
                value="We recommend three actions: (1) Freeze non-critical SGA immediately to save ~$4M in Q4. (2) Re-engage the top 10 at-risk Mid-Market accounts with a targeted retention offer. (3) Accelerate supplier renegotiations to recover $8M of COGS inflation.")
        with c2:
            st.markdown("**📄 Generated Executive Summary**")
            st.markdown("---")
            if sit and com and res:
                st.markdown(f"**Q3 FY2024 Performance Update**\n\n{sit}\n\n{com}\n\n{res}")
                st.markdown("---")
                hl = st.text_input("Key headline number (for your slide title)",
                                   value="EBITDA −$42M vs Budget (31% miss) — Mid-Market churn primary driver")
                if hl:
                    st.info(f"💡 **Recommended slide title:** *{hl}*")
                    st.caption("A great slide title = the conclusion, not the topic. 'Q3 EBITDA Performance' is a topic. 'EBITDA missed by $42M — Mid-Market churn primary driver' is a conclusion.")

    # ── WORKED EXAMPLE ────────────────────────────────────────────────────────
    with tab4:
        _sec("Worked Example: Before & After — Transforming a Finance Presentation", "🧪")

        st.markdown("""
**Business Situation:** The Regional VP asked you to present Q3 results to the Board.
Below are two versions of the same data — the original data dump your predecessor produced,
and the insight-driven version you deliver instead.
        """)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### ❌ BEFORE — The Data Dump Slide")
            st.markdown("---")
            st.markdown("**SLIDE TITLE:** Q3 Revenue Performance Analysis")
            before_df = pd.DataFrame({
                "Division":   ["APAC","EMEA","Americas","MEA","Group"],
                "Budget ($M)":[ 155,   162,    158,      25,   500],
                "Actual ($M)":[ 148,   165,    142,      27,   482],
                "PY ($M)":    [ 132,   148,    131,      30,   441],
                "vs Bgt $":   [  -7,    +3,    -16,      +2,   -18],
                "vs PY $":    [ +16,   +17,    +11,      -3,   +41],
            })
            st.dataframe(before_df, use_container_width=True, hide_index=True)
            st.markdown("""
*Commentary:*
Revenue performance was below budget in the period
under review. EMEA and MEA outperformed whilst
APAC and Americas underperformed in the quarter.
            """)
            st.error("""
**What's wrong:**
- Title is a topic, not a conclusion
- Reader must do all arithmetic to find what matters
- Commentary states facts, not insights
- No signal of urgency or required action
- 5 numbers per row — too many to absorb
            """)

        with c2:
            st.markdown("### ✅ AFTER — The Insight-Driven Slide")
            st.markdown("---")
            st.markdown("**SLIDE TITLE:** Americas missed by $16M — 3 Mid-Market accounts churned in August")

            divs3  = ["APAC","EMEA","Americas","MEA"]
            var3   = [-7, +3, -16, +2]
            fig = go.Figure(go.Bar(
                x=divs3, y=var3,
                marker_color=["#E24B4A" if v<0 else "#1D9E75" for v in var3],
                text=[f"${v:+}M" for v in var3], textposition="outside",
            ))
            fig.add_hline(y=0, line_color="black", line_width=1)
            fig.update_layout(
                height=280, yaxis=dict(range=[-22,10]),
                xaxis_title="Division", yaxis_title="Variance vs Budget ($M)",
                template="plotly_white", showlegend=False,
                margin=dict(t=20))
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
**Key number:** Americas = **$142M** vs Budget **−$16M (−10%)**

**Three bullets — insights, not data:**
- 🔴 Americas: 3 Mid-Market accounts churned in Aug, costing **−$12M**; remainder is pricing mix
- 🟢 EMEA outperformed by **+$3M** — 2 new enterprise logos signed in Jul
- 🔵 APAC pipeline strong — tracker shows 97% probability of Q4 recovery
            """)
            st.success("""
**What's better:**
- Conclusion is in the title — reader knows the story before reading
- One chart does all the comparison work instantly
- Three bullets deliver insight and context, not data
- Clear urgency: Mid-Market churn is named and quantified
            """)

        st.markdown("---")
        st.markdown("**The Rewrite Rules Applied:**")
        rules_df = pd.DataFrame({
            "Original Problem":       ["Topic slide title","Raw data table","Vague commentary",
                                        "No recommended action","Equal weight to all variances"],
            "Fix Applied":            ["Conclusion in title (the so-what)",
                                        "Visual chart (bar) — eyes do the comparison",
                                        "Insight bullets — name the root cause",
                                        "Next step implied by the data shown",
                                        "Americas highlighted; others greyed out"],
            "Principle":              ["Pyramid Principle","Pre-attentive attributes",
                                        "SCR framework","Prescriptive orientation",
                                        "Colour as signal"],
        })
        st.dataframe(rules_df, use_container_width=True, hide_index=True)

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    with tab5:
        _sec("Module 9 Quiz", "❓")
        _quiz("1. In the Pyramid Principle, what comes FIRST in a finance presentation?",
              ["All supporting data","The methodology used",
               "The conclusion or recommendation","The agenda slide"],
              "The conclusion or recommendation","m9q1")
        st.divider()
        _quiz("2. Best replacement for a pie chart with more than 4 slices?",
              ["Doughnut chart","Sorted horizontal bar chart",
               "Scatter plot","Area chart"],
              "Sorted horizontal bar chart","m9q2")
        st.divider()
        _quiz("3. SCR stands for:",
              ["Summary, Context, Results",
               "Situation, Complication, Resolution",
               "Strategy, Challenge, Recommendation",
               "Scope, Calculation, Report"],
              "Situation, Complication, Resolution","m9q3")
        st.divider()
        _quiz("4. 'Revenue was $482M in Q3' is an example of:",
              ["An insight","A recommendation",
               "A data point without insight","A complication"],
              "A data point without insight","m9q4")
        st.divider()
        _quiz("5. Why must bar charts start at zero on the y-axis?",
              ["It is a regulatory requirement",
               "Truncating the axis exaggerates differences and misleads the reader",
               "It makes the chart easier to colour",
               "Zero is always the most important data point"],
              "Truncating the axis exaggerates differences and misleads the reader","m9q5")