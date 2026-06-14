import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("⚠️ Module 9: Risk, Resilience & Strategic Decision-Making Under Uncertainty")
    st.markdown("*Quantify strategic risk, apply decision trees and scenario analysis, and build financial resilience frameworks*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Strategic vs Operational vs Financial Risk")
        st.markdown("""
        Finance professionals must distinguish between risk types to apply the right mitigation and measurement framework.
        """)
        risk_types = {
            "Risk Type": ["Strategic Risk", "Operational Risk", "Financial Risk", "Compliance / Legal Risk", "Reputational Risk"],
            "Definition": [
                "Risks that affect the viability or success of the strategic direction",
                "Risks from people, processes, systems, or external events",
                "Risks from financial markets, capital structure, liquidity",
                "Risks from regulatory changes, legal actions, non-compliance",
                "Risks that damage brand, trust, or stakeholder relationships"
            ],
            "Examples": [
                "Disruptive competitor, technology obsolescence, market shift, M&A failure",
                "Supply chain failure, cyber attack, talent loss, product quality",
                "Interest rate spike, FX volatility, credit downgrade, covenant breach",
                "GDPR violation, antitrust investigation, environmental breach",
                "ESG controversy, data breach, product safety issue, executive misconduct"
            ],
            "Finance Response": [
                "Scenario modelling, strategic risk register, stress testing strategy",
                "Insurance, business continuity planning, operational KPIs",
                "Hedging, liquidity buffers, covenant monitoring, credit risk management",
                "Legal provisions, compliance monitoring, regulatory capital",
                "ESG investment, governance standards, crisis communications cost"
            ]
        }
        st.dataframe(pd.DataFrame(risk_types), use_container_width=True, hide_index=True)

        st.subheader("2. Strategic Risk Register")
        st.markdown("""
        A **Strategic Risk Register** systematically identifies, assesses, and manages the risks that could prevent
        the organisation from achieving its strategic objectives.

        **Key components of each risk entry:**
        - **Risk description**: What could happen?
        - **Likelihood** (1–5): How probable is it?
        - **Impact** (1–5): How severe if it occurs?
        - **Inherent Risk Score** = Likelihood × Impact
        - **Current Controls**: What is already in place?
        - **Residual Risk**: Risk remaining after controls
        - **Owner**: Who is responsible?
        - **Financial Quantification**: What is the potential P&L / cash flow impact?

        **Finance professional's role**: Translate all risk ratings into **financial impact ranges** (best, expected, worst case) to feed into scenario modelling and stress testing.
        """)

        st.subheader("3. Decision Trees & Expected Value")
        st.markdown("""
        Decision trees structure complex strategic choices by mapping out **decisions, possible outcomes, probabilities, and payoffs**.

        ```
        Decision Tree Anatomy:
        □ Decision Node → You choose (e.g. Enter market vs Don't enter)
        ○ Chance Node  → Nature chooses (e.g. Market grows vs Stagnates)
        △ Terminal Node → Payoff value (NPV, cash flow, ROIC)

        Expected Value (EV) = Σ (Probability × Payoff) for each path

        Optimal Decision = the branch with highest EV (adjusted for risk tolerance)
        ```

        **Finance use**: Decision trees are essential for evaluating stage-gate investments,
        go/no-go decisions at project milestones, and comparing mutually exclusive strategic options.
        """)

        st.subheader("4. Scenario Analysis & Stress Testing")
        st.markdown("""
        Scenario analysis builds **multiple financially modelled futures** to test how strategy performs under different external conditions.

        | Type | Purpose | Finance Output |
        |------|---------|---------------|
        | **Base Case** | Most likely outcome — current trend continuation | Core financial plan and budget |
        | **Upside (Bull)** | Optimistic — key drivers better than expected | Max capital deployment plan |
        | **Downside (Bear)** | Pessimistic — key drivers worse than expected | Minimum viable financial plan |
        | **Stress Test** | Extreme but plausible shock (e.g. -40% revenue) | Covenant testing, liquidity analysis, survival test |

        **Tornado chart**: Ranks risk factors by their impact on a key output (e.g. NPV).
        The longest bar = the most important risk driver — deserves most management attention.
        """)

        st.subheader("5. Behavioural Biases in Strategic Decisions")
        st.markdown("""
        Finance professionals must guard against cognitive biases that corrupt strategic and financial judgment.

        | Bias | Description | Finance Defence |
        |------|-------------|----------------|
        | **Overconfidence** | Overestimate accuracy of own forecasts | Widen forecast ranges; reference class forecasting |
        | **Anchoring** | Over-rely on first number seen (e.g. initial ask price) | Independent valuation benchmarks |
        | **Sunk Cost Fallacy** | Continue investing because of past spend | Evaluate only future cash flows |
        | **Groupthink** | Suppress dissenting views for consensus | Devil's advocate; pre-mortem analysis |
        | **Optimism Bias** | Systematically over-project revenues, under-project costs | Systematic adjustment; outside view |
        | **Confirmation Bias** | Seek only data that confirms existing view | Structured challenge; red team analysis |
        """)

        st.subheader("6. Building Strategic Resilience")
        st.markdown("""
        Strategic resilience = the capacity to absorb shocks, adapt, and recover stronger.

        **Four dimensions of financial resilience:**
        1. **Liquidity resilience**: Sufficient cash and undrawn facilities to survive downturns
        2. **Earnings resilience**: Diversified revenue streams that don't all decline together
        3. **Capital resilience**: Balance sheet strength to avoid distress when ROIC temporarily falls
        4. **Operational resilience**: Business continuity and supply chain flexibility to maintain revenue during shocks

        **Finance resilience test**: Can the business survive EBITDA declining 40% for 18 months without covenant breach?
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Strategic Risk Register — Retail Business")
        risk_register = {
            "Risk": ["E-commerce disruption", "Key supplier failure", "FX devaluation in export markets",
                     "Minimum wage legislation increase", "Climate regulation — carbon tax",
                     "Cyber attack on customer data", "CFO departure — financial controls"],
            "Likelihood (1–5)": [4, 2, 3, 4, 3, 3, 2],
            "Impact (1–5)": [5, 4, 3, 4, 4, 5, 4],
            "Risk Score": [20, 8, 9, 16, 12, 15, 8],
            "Rating": ["🔴 Critical", "🟢 Low", "🟠 Medium", "🔴 High", "🟠 Medium", "🔴 High", "🟠 Medium"],
            "Financial Impact ($M, worst case)": ["-$45M revenue", "-$8M EBITDA", "-$6M EBITDA", "-$12M EBITDA", "-$9M EBITDA", "-$20M one-off + reputational", "-$5M controls failure"]
        }
        st.dataframe(pd.DataFrame(risk_register), use_container_width=True, hide_index=True)
        st.error("🔴 **Top priority risks**: E-commerce disruption (score 20) and minimum wage increase (score 16) require immediate strategic and financial response plans.")

        st.subheader("Example 2: Decision Tree — Market Entry Decision")
        st.markdown("""
        **Decision: Enter Southeast Asian market now (invest $15M) vs Wait 2 years (invest $8M)**

        ```
        OPTION A — Enter Now ($15M investment):
        ├── 60% probability: Market grows strongly → NPV = $45M
        │   └── EV contribution: 0.60 × $45M = $27.0M
        ├── 30% probability: Market grows slowly → NPV = $12M
        │   └── EV contribution: 0.30 × $12M = $3.6M
        └── 10% probability: Market fails → NPV = -$15M (loss of investment)
            └── EV contribution: 0.10 × -$15M = -$1.5M
        ─────────────────────────────────────────
        Expected Value (Enter Now) = $29.1M

        OPTION B — Wait 2 Years ($8M investment, less risk):
        ├── 50% probability: Market grows strongly → NPV = $22M
        │   └── EV contribution: 0.50 × $22M = $11.0M
        ├── 35% probability: Market grows slowly → NPV = $9M
        │   └── EV contribution: 0.35 × $9M = $3.2M
        └── 15% probability: Market fails → NPV = -$8M
            └── EV contribution: 0.15 × -$8M = -$1.2M
        ─────────────────────────────────────────
        Expected Value (Wait) = $13.0M
        ```

        **Decision**: Enter Now has EV of $29.1M vs $13.0M for Wait.
        However, risk-averse boards may prefer Wait — lower downside, lower commitment.
        Finance role: present both EV and risk-adjusted view, and test against financial resilience.
        """)
        st.success("✅ **Finance Insight**: Enter Now is the rational expected-value choice. The $16M EV advantage justifies the additional $7M investment and higher variance.")

        st.subheader("Example 3: Scenario Stress Test — Revenue Shock")
        stress_data = {
            "Scenario": ["Base Case", "Mild Downturn", "Severe Recession", "Catastrophic Shock"],
            "Revenue Decline": ["0%", "-15%", "-30%", "-45%"],
            "Revenue ($M)": [200, 170, 140, 110],
            "EBITDA ($M)": [40, 26, 14, 3],
            "EBITDA Margin": ["20%", "15%", "10%", "3%"],
            "FCF ($M)": [28, 14, 2, -12],
            "Net Debt / EBITDA": ["1.5×", "2.3×", "4.3×", "20×+"],
            "Covenant (max 4×)": ["✅ Pass", "✅ Pass", "⚠️ Near breach", "🔴 Covenant breach"],
            "Action Required": ["None", "Cost review", "Emergency cost programme", "Refinancing / equity raise"]
        }
        st.dataframe(pd.DataFrame(stress_data), use_container_width=True, hide_index=True)
        st.warning("💡 The business can survive a 30% revenue decline but breaches covenants in a catastrophic scenario. Finance action: negotiate covenant headroom, build liquidity buffer, or reduce debt before the next downturn.")

    with tab3:
        st.header("Interactive Tools")

        tool = st.selectbox("Select Tool:", [
            "Strategic Risk Register Builder",
            "Decision Tree Expected Value Calculator",
            "Scenario Stress Testing Model"
        ])

        if tool == "Strategic Risk Register Builder":
            st.subheader("📋 Strategic Risk Register Builder")
            num_risks = st.number_input("Number of risks to assess:", 2, 8, 5)
            risks = []
            for i in range(int(num_risks)):
                st.markdown(f"**Risk {i+1}:**")
                col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
                with col1:
                    risk_name = st.text_input("Risk description:", value=f"Strategic risk {i+1}", key=f"rr_n_{i}")
                with col2:
                    likelihood = st.slider("Likelihood (1–5):", 1, 5, 3, key=f"rr_l_{i}")
                with col3:
                    impact = st.slider("Impact (1–5):", 1, 5, 3, key=f"rr_i_{i}")
                with col4:
                    fin_impact = st.number_input("Worst-case financial impact ($M):", 0.0, 500.0, 10.0, 1.0, key=f"rr_f_{i}")
                score = likelihood * impact
                rating = "🔴 Critical" if score >= 16 else ("🟠 High" if score >= 9 else ("🟡 Medium" if score >= 4 else "🟢 Low"))
                risks.append({"Risk": risk_name, "Likelihood": likelihood, "Impact": impact, "Score": score,
                               "Rating": rating, "Worst-Case ($M)": f"${fin_impact:.1f}M"})

            df_risks = pd.DataFrame(risks).sort_values("Score", ascending=False)
            st.dataframe(df_risks, use_container_width=True, hide_index=True)
            critical = df_risks[df_risks["Score"] >= 16]
            total_worst = sum(float(r["Worst-Case ($M)"].replace("$","").replace("M","")) for r in risks)
            col1, col2 = st.columns(2)
            with col1: st.metric("Critical Risks", len(critical), "Require immediate response plan")
            with col2: st.metric("Aggregate Worst-Case Exposure", f"${total_worst:.1f}M", "Inform stress test & liquidity buffer")
            if len(critical) > 0:
                st.error(f"🔴 Critical risks identified: {', '.join(critical['Risk'].tolist())} — escalate to board immediately.")

        elif tool == "Decision Tree Expected Value Calculator":
            st.subheader("🌳 Decision Tree Expected Value Calculator")
            st.markdown("Compare two strategic options using expected value analysis:")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Option A:**")
                a_invest = st.number_input("Option A — Investment ($M):", 0.1, 200.0, 15.0, 1.0)
                st.markdown("*Three outcomes:*")
                a_p1 = st.slider("P(High Success) %:", 0, 100, 50, key="dt_ap1")
                a_v1 = st.number_input("NPV if High Success ($M):", 0.0, 500.0, 50.0, 5.0, key="dt_av1")
                a_p2 = st.slider("P(Moderate) %:", 0, 100 - a_p1, min(30, 100 - a_p1), key="dt_ap2")
                a_v2 = st.number_input("NPV if Moderate ($M):", -100.0, 200.0, 15.0, 5.0, key="dt_av2")
                a_p3 = 100 - a_p1 - a_p2
                st.markdown(f"P(Failure) = **{a_p3}%** (auto-calculated)")
                a_v3 = st.number_input("NPV if Failure ($M):", -200.0, 0.0, -a_invest, 1.0, key="dt_av3")

            with col2:
                st.markdown("**Option B:**")
                b_invest = st.number_input("Option B — Investment ($M):", 0.1, 200.0, 8.0, 1.0)
                st.markdown("*Three outcomes:*")
                b_p1 = st.slider("P(High Success) %:", 0, 100, 40, key="dt_bp1")
                b_v1 = st.number_input("NPV if High Success ($M):", 0.0, 500.0, 30.0, 5.0, key="dt_bv1")
                b_p2 = st.slider("P(Moderate) %:", 0, 100 - b_p1, min(35, 100 - b_p1), key="dt_bp2")
                b_v2 = st.number_input("NPV if Moderate ($M):", -100.0, 200.0, 10.0, 5.0, key="dt_bv2")
                b_p3 = 100 - b_p1 - b_p2
                st.markdown(f"P(Failure) = **{b_p3}%** (auto-calculated)")
                b_v3 = st.number_input("NPV if Failure ($M):", -200.0, 0.0, -b_invest, 1.0, key="dt_bv3")

            ev_a = (a_p1/100)*a_v1 + (a_p2/100)*a_v2 + (a_p3/100)*a_v3 - a_invest
            ev_b = (b_p1/100)*b_v1 + (b_p2/100)*b_v2 + (b_p3/100)*b_v3 - b_invest
            max_loss_a = a_v3 - a_invest
            max_loss_b = b_v3 - b_invest

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Option A — Expected Value (net)", f"${ev_a:.1f}M")
                st.metric("Option A — Maximum Loss", f"${max_loss_a:.1f}M")
            with col2:
                st.metric("Option B — Expected Value (net)", f"${ev_b:.1f}M")
                st.metric("Option B — Maximum Loss", f"${max_loss_b:.1f}M")

            if ev_a > ev_b:
                st.success(f"📊 **Rational choice: Option A** (EV ${ev_a:.1f}M vs ${ev_b:.1f}M). However, if risk tolerance is low, note Option A's max loss is ${max_loss_a:.1f}M vs ${max_loss_b:.1f}M for B.")
            else:
                st.success(f"📊 **Rational choice: Option B** (EV ${ev_b:.1f}M vs ${ev_a:.1f}M). Lower EV advantage but also lower maximum downside risk.")

        else:  # Scenario Stress Testing
            st.subheader("📉 Scenario Stress Testing Model")
            col1, col2 = st.columns(2)
            with col1:
                base_revenue = st.number_input("Base Revenue ($M):", 10.0, 2000.0, 200.0, 10.0)
                base_ebitda_pct = st.slider("Base EBITDA Margin (%):", 5.0, 50.0, 20.0, 0.5)
                fixed_cost_pct = st.slider("Fixed Cost as % of Total Costs:", 30.0, 90.0, 55.0, 1.0)
            with col2:
                net_debt = st.number_input("Net Debt ($M):", 0.0, 2000.0, 60.0, 5.0)
                interest_rate = st.slider("Average Interest Rate (%):", 1.0, 12.0, 4.5, 0.5)
                covenant_max = st.slider("Covenant Max Net Debt/EBITDA (×):", 2.0, 8.0, 4.0, 0.5)

            scenarios_st = {"Base Case": 0, "Mild Downturn": -15, "Severe Recession": -30, "Catastrophic": -45}
            rows = []
            for scen, decline in scenarios_st.items():
                rev = base_revenue * (1 + decline / 100)
                base_costs = base_revenue * (1 - base_ebitda_pct / 100)
                fixed_costs = base_costs * (fixed_cost_pct / 100)
                variable_costs = (base_costs - fixed_costs) * (1 + decline / 100)
                ebitda = rev - fixed_costs - variable_costs
                ebitda_m = ebitda / rev * 100 if rev > 0 else 0
                interest = net_debt * (interest_rate / 100)
                fcf = ebitda - interest - (base_revenue * 0.04)
                leverage = net_debt / ebitda if ebitda > 0 else 999
                covenant_status = "✅ Pass" if leverage <= covenant_max else "🔴 BREACH"
                rows.append({"Scenario": scen, "Revenue ($M)": f"${rev:.0f}M", "EBITDA ($M)": f"${ebitda:.0f}M",
                              "EBITDA %": f"{ebitda_m:.1f}%", "FCF ($M)": f"${fcf:.0f}M",
                              "Net Debt/EBITDA": f"{leverage:.1f}×" if leverage < 99 else "N/M",
                              "Covenant Test": covenant_status})
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            breaches = sum(1 for r in rows if "BREACH" in r["Covenant Test"])
            if breaches > 0:
                st.error(f"⚠️ Covenant breached in {breaches} scenario(s). Consider: renegotiate covenants, reduce debt, or build larger liquidity buffer before downturn.")
            else:
                st.success("✅ No covenant breaches in any scenario. Business demonstrates strong financial resilience.")

    with tab4:
        st.header("Visualizations")

        st.subheader("Risk Heat Map — Likelihood vs Impact")
        risks_hm = ["E-Commerce Disruption", "Supplier Failure", "FX Devaluation", "Wage Legislation",
                    "Carbon Tax", "Cyber Attack", "Key Talent Loss", "Regulatory Change"]
        likelihood_hm = [4, 2, 3, 4, 3, 3, 3, 2]
        impact_hm = [5, 4, 3, 4, 4, 5, 3, 3]
        scores_hm = [l * i for l, i in zip(likelihood_hm, impact_hm)]
        colors_hm = ["#E74C3C" if s >= 16 else "#E67E22" if s >= 9 else "#F9E79F" for s in scores_hm]
        fig_hm = go.Figure()
        for risk, l, i, c, s in zip(risks_hm, likelihood_hm, impact_hm, colors_hm, scores_hm):
            fig_hm.add_trace(go.Scatter(x=[i], y=[l], mode="markers+text", text=[f"{risk}<br>Score:{s}"],
                                        textposition="top center", marker=dict(size=40, color=c, opacity=0.8),
                                        textfont=dict(size=9), showlegend=False))
        fig_hm.add_shape(type="rect", x0=3.5, y0=3.5, x1=5.5, y1=5.5, fillcolor="rgba(231,76,60,0.1)", line=dict(color="#E74C3C", dash="dot"))
        fig_hm.update_layout(title="Strategic Risk Heat Map (Likelihood × Impact)", height=450,
                             xaxis=dict(title="Impact (1–5)", range=[0, 6], tickvals=[1,2,3,4,5]),
                             yaxis=dict(title="Likelihood (1–5)", range=[0, 6], tickvals=[1,2,3,4,5]))
        st.plotly_chart(fig_hm, use_container_width=True)

        st.subheader("Tornado Chart — NPV Sensitivity to Key Risk Drivers")
        drivers = ["Market Growth Rate", "Competitive Response", "Cost of Capital (WACC)", "Input Cost Inflation",
                   "Regulatory Change", "FX Movement", "Technology Risk"]
        upside = [18, 12, 9, 7, 6, 8, 5]
        downside = [-22, -15, -11, -9, -8, -7, -6]
        fig_tornado = go.Figure()
        fig_tornado.add_trace(go.Bar(y=drivers, x=upside, orientation="h", name="Upside (+)", marker_color="#27AE60"))
        fig_tornado.add_trace(go.Bar(y=drivers, x=downside, orientation="h", name="Downside (−)", marker_color="#E74C3C"))
        fig_tornado.add_vline(x=0, line_color="black", line_width=2)
        fig_tornado.update_layout(title="Tornado Chart — NPV Sensitivity by Risk Driver ($M swing)", barmode="overlay",
                                  xaxis_title="NPV Impact ($M)", height=420)
        st.plotly_chart(fig_tornado, use_container_width=True)

        st.subheader("Scenario Outcomes — Revenue & EBITDA Bridge")
        scen_names = ["Base Case", "Mild Downturn", "Severe Recession", "Catastrophic"]
        rev_vals = [200, 170, 140, 110]
        ebitda_vals = [40, 26, 14, 3]
        fig_scen = go.Figure()
        fig_scen.add_trace(go.Bar(x=scen_names, y=rev_vals, name="Revenue ($M)", marker_color="#2563EB", opacity=0.7))
        fig_scen.add_trace(go.Bar(x=scen_names, y=ebitda_vals, name="EBITDA ($M)", marker_color="#1B3A6B"))
        fig_scen.add_hline(y=60, line_dash="dash", line_color="#E74C3C", annotation_text="Covenant trigger: EBITDA $14M")
        fig_scen.update_layout(title="Scenario Analysis — Revenue & EBITDA Outcomes", barmode="group",
                               yaxis_title="$M", height=400)
        st.plotly_chart(fig_scen, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. In a strategic risk register, the 'inherent risk score' is calculated as:**")
        q1 = st.radio("", [
            "Impact + Likelihood",
            "Impact × Likelihood",
            "Impact / Likelihood",
            "Impact − Controls Effectiveness"
        ], key="bs9q1")
        if st.button("Check Answer", key="bs9c1"):
            if q1 == "Impact × Likelihood":
                st.success("✅ Correct! Risk Score = Likelihood × Impact. A score ≥ 16 (out of 25) is typically classified as Critical.")
            else:
                st.error("❌ Incorrect. Inherent Risk Score = Likelihood × Impact (each rated 1–5, giving a max of 25).")

        st.markdown("---")
        st.markdown("**2. In a decision tree, Expected Value (EV) is calculated as:**")
        q2 = st.radio("", [
            "The highest possible payoff",
            "The sum of (Probability × Payoff) across all outcomes",
            "The average of the best and worst cases",
            "Net Present Value minus investment cost"
        ], key="bs9q2")
        if st.button("Check Answer", key="bs9c2"):
            if q2 == "The sum of (Probability × Payoff) across all outcomes":
                st.success("✅ Correct! EV = Σ(P × V) across all possible outcomes. It is the probability-weighted average payoff.")
            else:
                st.error("❌ Incorrect. Expected Value = Σ (Probability × Payoff) for each outcome — the probability-weighted average.")

        st.markdown("---")
        st.markdown("**3. A 'tornado chart' in scenario analysis is used to:**")
        q3 = st.radio("", [
            "Show the sequence of strategic milestones",
            "Rank risk factors by their magnitude of impact on a key output like NPV",
            "Display the organisational hierarchy",
            "Plot cash flow over time"
        ], key="bs9q3")
        if st.button("Check Answer", key="bs9c3"):
            if q3 == "Rank risk factors by their magnitude of impact on a key output like NPV":
                st.success("✅ Correct! A tornado chart ranks assumptions/drivers by how much they move the output — the widest bar = most critical assumption.")
            else:
                st.error("❌ Incorrect. A tornado chart shows which assumptions drive the most variance in a key output — widest bar = biggest risk driver.")

        st.markdown("---")
        st.markdown("**4. The 'sunk cost fallacy' occurs when a decision-maker:**")
        q4 = st.radio("", [
            "Ignores past investments when making future decisions",
            "Continues investing in a failing project because of money already spent",
            "Underestimates the cost of a new project",
            "Overestimates the probability of success"
        ], key="bs9q4")
        if st.button("Check Answer", key="bs9c4"):
            if q4 == "Continues investing in a failing project because of money already spent":
                st.success("✅ Correct! Sunk costs are irrelevant to future decisions — only future incremental cash flows matter. Finance professionals must challenge sunk cost reasoning.")
            else:
                st.error("❌ Incorrect. Sunk cost fallacy = continuing to invest because of past spend. Only future incremental cash flows are relevant.")

        st.markdown("---")
        st.markdown("**5. Financial resilience is best tested by:**")
        q5 = st.radio("", [
            "Calculating the current year budget variance",
            "Stress testing EBITDA and cash flow against severe but plausible downside scenarios",
            "Reviewing last year's audit opinion",
            "Comparing gross margins to industry benchmarks"
        ], key="bs9q5")
        if st.button("Check Answer", key="bs9c5"):
            if q5 == "Stress testing EBITDA and cash flow against severe but plausible downside scenarios":
                st.success("✅ Correct! Resilience testing requires severe scenario modelling — testing covenants, liquidity, and FCF under stressed conditions.")
            else:
                st.error("❌ Incorrect. Financial resilience testing = stress testing P&L and cash flow against severe downside scenarios, testing covenants and survival.")

    with tab6:
        st.header("Module Summary")
        st.subheader("🎯 Key Takeaways")
        st.markdown("""
        ### 1. Risk Categories
        | Type | Finance Response |
        |------|----------------|
        | Strategic | Scenario modelling, risk register, stress testing |
        | Operational | Insurance, BCP, operational KPIs |
        | Financial | Hedging, liquidity buffers, covenant monitoring |
        | Compliance | Legal provisions, regulatory capital |
        | Reputational | ESG investment, governance standards |

        ### 2. Strategic Risk Register
        ```
        Risk Score = Likelihood (1–5) × Impact (1–5)
        ≥ 16  → Critical — immediate response plan
        9–15  → High — active mitigation
        4–8   → Medium — monitor and manage
        1–3   → Low — accept and watch
        ```

        ### 3. Decision Tree Expected Value
        ```
        EV = Σ (Probability × Payoff) for each outcome
        Optimal decision = highest EV
        Risk-adjusted decision = EV discounted by variance/downside tolerance
        ```

        ### 4. Scenario Analysis Framework
        ```
        Base Case  → Core financial plan
        Upside     → Max investment deployment plan
        Downside   → Minimum viable plan; cost triggers
        Stress     → Covenant testing; survival analysis; liquidity buffer sizing
        ```

        ### 5. Six Behavioural Biases to Guard Against
        - Overconfidence → Optimism Bias → Anchoring
        - Sunk Cost Fallacy → Groupthink → Confirmation Bias
        """)
        st.subheader("📌 Key Formulas")
        st.code("Inherent Risk Score = Likelihood (1–5) × Impact (1–5)")
        st.code("Expected Value = Σ [Probability(i) × Payoff(i)] for all outcomes i")
        st.code("Residual Risk = Inherent Risk − Control Effectiveness")
        st.code("Liquidity Buffer = Max monthly cash burn × (3–6 months survival horizon)")
        st.success("🎓 **Module 9 Complete!** You can now build strategic risk registers, apply decision trees, run scenario stress tests, and design financially resilient organisations.")
        st.info("💡 **Next**: Module 10 — Global Strategy, ESG & Stakeholder Value")

if __name__ == "__main__":
    show()