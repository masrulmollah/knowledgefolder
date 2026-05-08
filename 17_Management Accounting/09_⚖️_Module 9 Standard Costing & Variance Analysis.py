import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("🎯 Module 9: Standard Costing & Variance Analysis")
    st.markdown("*Master the language of cost control — analyze every cost variance in detail*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Calculators",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Standard Costs — What and Why")
        st.markdown("""
        **Standard Cost:** A carefully predetermined cost per unit under efficient operating conditions.

        | Type | Description | Typical Use |
        |------|-------------|------------|
        | **Ideal Standards** | Perfect efficiency — no waste, no breaks, no defects | Theoretical maximum |
        | **Practical Standards** | Efficient but realistic — allows for normal downtime/waste | Most widely used ✅ |
        | **Historical Standards** | Based on past performance — may perpetuate inefficiency | Some industries |

        #### Benefits of Standard Costing:
        - Provides unit cost for pricing decisions
        - Enables management by exception (focus on variances)
        - Simplifies bookkeeping
        - Motivates managers to meet targets
        - Facilitates budgeting
        """)

        st.subheader("2. Standard Cost Card")
        st.markdown("""
        ```
        ─────────────────────────────────────────────────────
        STANDARD COST CARD — Product XYZ  (per unit)
        ─────────────────────────────────────────────────────
        Direct Materials:  5 lbs  × $10.00/lb    =   $50.00
        Direct Labor:      2 hrs  × $20.00/hr    =   $40.00
        Variable OH:       2 hrs  × $6.00/hr     =   $12.00
        Fixed OH:          2 hrs  × $8.00/hr     =   $16.00
        ─────────────────────────────────────────────────────
        Total Standard Cost per Unit              =  $118.00
        ─────────────────────────────────────────────────────
        ```
        """)

        st.subheader("3. Variance — Favorable vs Unfavorable")
        st.markdown("""
        | Result | Symbol | Meaning |
        |--------|--------|---------|
        | Actual Cost < Standard Cost | **F (Favorable)** | Spent less than planned — generally good |
        | Actual Cost > Standard Cost | **U (Unfavorable)** | Spent more than planned — generally bad |
        | Actual Cost = Standard Cost | Zero variance | Perfectly on target |

        ⚠️ **Important:** A favorable variance is not always good, and unfavorable is not always bad.
        Buying cheap materials might save money (F price) but cause excessive waste (U quantity)!
        """)

        st.subheader("4. Direct Materials Variances")
        st.markdown("""
        **Two variances — each with a specific formula:**

        **Price Variance (MPV) — Purchasing department responsible:**
        ```
        MPV = (Actual Price − Standard Price) × Actual Quantity PURCHASED
              (AP − SP) × AQ purchased

        Favorable if AP < SP
        ```

        **Quantity Variance (MQV) — Production department responsible:**
        ```
        MQV = (Actual Quantity Used − Standard Quantity Allowed) × Standard Price
              (AQ used − SQ allowed) × SP

        Standard Quantity Allowed = Standard qty per unit × Actual units produced
        Favorable if AQ used < SQ allowed
        ```

        **Total DM Variance = MPV + MQV**
        """)

        st.subheader("5. Direct Labor Variances")
        st.markdown("""
        **Rate Variance (LRV) — HR / payroll responsible:**
        ```
        LRV = (Actual Rate − Standard Rate) × Actual Hours Worked
              (AR − SR) × AH

        Favorable if AR < SR
        ```

        **Efficiency Variance (LEV) — Production supervisor responsible:**
        ```
        LEV = (Actual Hours Worked − Standard Hours Allowed) × Standard Rate
              (AH − SH allowed) × SR

        Standard Hours Allowed = Standard hrs per unit × Actual units produced
        Favorable if AH < SH allowed
        ```

        **Total DL Variance = LRV + LEV**
        """)

        st.subheader("6. Variable Overhead Variances")
        st.markdown("""
        **Spending Variance:**
        ```
        VOHSV = Actual VOH − (Actual Hours × Standard VOH Rate)
        Favorable if actual spending < expected for hours worked
        ```

        **Efficiency Variance:**
        ```
        VOHEV = (Actual Hours − Standard Hours Allowed) × Standard VOH Rate
        Favorable if AH < SH allowed (same as DL efficiency)
        ```
        """)

        st.subheader("7. Fixed Overhead Variances")
        st.markdown("""
        **Budget (Spending) Variance:**
        ```
        FOHBV = Actual Fixed OH − Budgeted Fixed OH
        Favorable if Actual < Budgeted
        ```

        **Volume Variance:**
        ```
        FOHVV = Budgeted Fixed OH − (Standard Rate × Standard Hours Allowed)
        Favorable if actual output > denominator volume (used capacity well)
        ```
        """)

    with tab2:
        st.header("Worked Examples")

        st.subheader("Example: Full Variance Analysis (1,000 units produced)")
        st.markdown("""
        **Standard Cost Card:**
        - DM: 5 lbs × $10/lb = $50
        - DL: 2 hrs × $20/hr = $40
        - VOH: 2 hrs × $6/hr = $12

        **Actual Results:**
        | Item | Actual |
        |------|--------|
        | DM purchased | 5,500 lbs @ $9.80/lb |
        | DM used | 5,300 lbs |
        | DL | 2,100 hours @ $20.50/hr |
        | Actual VOH | $12,800 |
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Direct Materials Variances:**
            ```
            Standard Qty Allowed = 5 × 1,000 = 5,000 lbs

            Price Variance:
            (AP − SP) × AQ purchased
            ($9.80 − $10.00) × 5,500
            = −$0.20 × 5,500
            = $1,100 F  ✅

            Quantity Variance:
            (AQ used − SQ allowed) × SP
            (5,300 − 5,000) × $10
            = 300 × $10
            = $3,000 U  ❌
            ─────────────────────────
            Net DM Variance: $1,900 U
            ```
            """)
        with col2:
            st.markdown("""
            **Direct Labor Variances:**
            ```
            Standard Hours Allowed = 2 × 1,000 = 2,000 hrs

            Rate Variance:
            (AR − SR) × AH
            ($20.50 − $20.00) × 2,100
            = $0.50 × 2,100
            = $1,050 U  ❌

            Efficiency Variance:
            (AH − SH) × SR
            (2,100 − 2,000) × $20
            = 100 × $20
            = $2,000 U  ❌
            ─────────────────────────
            Net DL Variance: $3,050 U
            ```
            """)

        st.markdown("""
        **Variable Overhead Variances:**
        ```
        Standard Hours Allowed = 2,000 hrs

        Spending Variance:
        Actual VOH − (AH × SR)
        $12,800 − (2,100 × $6)
        = $12,800 − $12,600
        = $200 U  ❌

        Efficiency Variance:
        (AH − SH) × SR
        (2,100 − 2,000) × $6
        = 100 × $6
        = $600 U  ❌
        ─────────────────────────────────
        Net VOH Variance: $800 U
        ```

        **Total Variance Summary:**
        | Variance | Amount | F/U |
        |----------|--------|-----|
        | DM Price | $1,100 | F |
        | DM Quantity | $3,000 | U |
        | DL Rate | $1,050 | U |
        | DL Efficiency | $2,000 | U |
        | VOH Spending | $200 | U |
        | VOH Efficiency | $600 | U |
        | **Total** | **$5,750** | **U** |
        """)

    with tab3:
        st.header("💡 Interactive Calculators")

        var_type = st.selectbox("Choose Variance Calculator:", [
            "📦 Direct Materials Variances",
            "👷 Direct Labor Variances",
            "⚙️ Variable Overhead Variances",
            "🏢 Fixed Overhead Variances",
            "📊 Complete Variance Dashboard"
        ])

        def fav_label(v):
            if v < 0:
                return f"${abs(v):,.2f} ✅ Favorable"
            elif v > 0:
                return f"${v:,.2f} ❌ Unfavorable"
            else:
                return "$0.00 — On Target"

        if var_type == "📦 Direct Materials Variances":
            st.subheader("Direct Materials Variance Calculator")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Standards:**")
                sp = st.number_input("Standard Price ($/lb)", 0.0, value=10.0, step=0.10)
                sq_per_unit = st.number_input("Standard Quantity per Unit (lbs)", 0.0, value=5.0, step=0.25)
                actual_units = st.number_input("Actual Units Produced", 0, value=1000, step=10)
            with col2:
                st.markdown("**Actuals:**")
                ap = st.number_input("Actual Price Paid ($/lb)", 0.0, value=9.80, step=0.01)
                aq_purchased = st.number_input("Actual Quantity PURCHASED (lbs)", 0.0, value=5500.0, step=50.0)
                aq_used = st.number_input("Actual Quantity USED (lbs)", 0.0, value=5300.0, step=50.0)

            sq_allowed = sq_per_unit * actual_units
            price_var = (ap - sp) * aq_purchased
            qty_var = (aq_used - sq_allowed) * sp
            total_var = price_var + qty_var

            st.markdown("---")
            st.markdown("### Results:")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Standard Qty Allowed", f"{sq_allowed:,.0f} lbs")
            with col2:
                st.metric("Price Variance", fav_label(price_var))
            with col3:
                st.metric("Quantity Variance", fav_label(qty_var))

            st.metric("Total DM Variance", fav_label(total_var))

            st.markdown(f"""
            **Detailed Calculations:**
            ```
            Standard Qty Allowed = {sq_per_unit} lbs/unit × {actual_units:,} units = {sq_allowed:,.0f} lbs

            Price Variance = (AP − SP) × AQ Purchased
            = (${ap:.2f} − ${sp:.2f}) × {aq_purchased:,.0f} lbs
            = ${price_var:,.2f}  {'✅ Favorable (paid less than standard)' if price_var < 0 else '❌ Unfavorable (paid more than standard)'}

            Quantity Variance = (AQ Used − SQ Allowed) × SP
            = ({aq_used:,.0f} − {sq_allowed:,.0f}) × ${sp:.2f}
            = ${qty_var:,.2f}  {'✅ Favorable (used less than standard)' if qty_var < 0 else '❌ Unfavorable (used more than standard)'}

            Total DM Variance = ${price_var:,.2f} + ${qty_var:,.2f} = ${total_var:,.2f}
            ```
            """)

            if price_var < 0 and qty_var > 0:
                st.warning("⚠️ Common pattern: Favorable price variance but unfavorable quantity. Did buying cheaper material cause excessive waste?")

        elif var_type == "👷 Direct Labor Variances":
            st.subheader("Direct Labor Variance Calculator")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Standards:**")
                sr = st.number_input("Standard Rate ($/hr)", 0.0, value=20.0, step=0.50)
                sh_per_unit = st.number_input("Standard Hours per Unit", 0.0, value=2.0, step=0.25)
                actual_units = st.number_input("Actual Units Produced", 0, value=1000, step=10)
            with col2:
                st.markdown("**Actuals:**")
                ar = st.number_input("Actual Rate Paid ($/hr)", 0.0, value=20.50, step=0.10)
                ah = st.number_input("Actual Hours Worked", 0.0, value=2100.0, step=10.0)

            sh_allowed = sh_per_unit * actual_units
            rate_var = (ar - sr) * ah
            eff_var = (ah - sh_allowed) * sr
            total_var = rate_var + eff_var

            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Standard Hours Allowed", f"{sh_allowed:,.0f} hrs")
            with col2: st.metric("Rate Variance", fav_label(rate_var))
            with col3: st.metric("Efficiency Variance", fav_label(eff_var))
            st.metric("Total DL Variance", fav_label(total_var))

            st.markdown(f"""
            **Detailed Calculations:**
            ```
            Standard Hours Allowed = {sh_per_unit} hrs/unit × {actual_units:,} units = {sh_allowed:,.0f} hrs

            Rate Variance = (AR − SR) × Actual Hours
            = (${ar:.2f} − ${sr:.2f}) × {ah:,.0f} hrs
            = ${rate_var:,.2f}  {'✅ Favorable' if rate_var < 0 else '❌ Unfavorable'}

            Efficiency Variance = (Actual Hours − Standard Hours) × SR
            = ({ah:,.0f} − {sh_allowed:,.0f}) × ${sr:.2f}
            = ${eff_var:,.2f}  {'✅ Favorable' if eff_var < 0 else '❌ Unfavorable'}

            Total DL Variance = ${rate_var:,.2f} + ${eff_var:,.2f} = ${total_var:,.2f}
            ```
            """)

        elif var_type == "⚙️ Variable Overhead Variances":
            st.subheader("Variable Overhead Variance Calculator")
            col1, col2 = st.columns(2)
            with col1:
                voh_rate = st.number_input("Standard VOH Rate ($/hr)", 0.0, value=6.0, step=0.50)
                sh_per_unit = st.number_input("Standard DLH per Unit", 0.0, value=2.0, step=0.25)
                actual_units = st.number_input("Actual Units Produced", 0, value=1000, step=10)
            with col2:
                actual_voh = st.number_input("Actual Variable OH ($)", 0.0, value=12800.0, step=100.0)
                actual_hours = st.number_input("Actual Direct Labor Hours", 0.0, value=2100.0, step=10.0)

            sh_allowed = sh_per_unit * actual_units
            applied_voh = sh_allowed * voh_rate
            spending_var = actual_voh - (actual_hours * voh_rate)
            eff_var = (actual_hours - sh_allowed) * voh_rate
            total_var = spending_var + eff_var

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("VOH Applied", f"${applied_voh:,.2f}")
            with col2: st.metric("Spending Variance", fav_label(spending_var))
            with col3: st.metric("Efficiency Variance", fav_label(eff_var))
            st.metric("Total VOH Variance", fav_label(total_var))

            st.markdown(f"""
            **Detailed Calculations:**
            ```
            Standard Hours Allowed = {sh_per_unit} × {actual_units:,} = {sh_allowed:,.0f} hrs

            Spending Variance = Actual VOH − (AH × Standard Rate)
            = ${actual_voh:,.2f} − ({actual_hours:,.0f} × ${voh_rate:.2f})
            = ${actual_voh:,.2f} − ${actual_hours*voh_rate:,.2f}
            = ${spending_var:,.2f}  {'✅ Favorable' if spending_var < 0 else '❌ Unfavorable'}

            Efficiency Variance = (AH − SH) × Standard Rate
            = ({actual_hours:,.0f} − {sh_allowed:,.0f}) × ${voh_rate:.2f}
            = ${eff_var:,.2f}  {'✅ Favorable' if eff_var < 0 else '❌ Unfavorable'}
            ```
            """)

        elif var_type == "🏢 Fixed Overhead Variances":
            st.subheader("Fixed Overhead Variance Calculator")
            col1, col2 = st.columns(2)
            with col1:
                budgeted_foh = st.number_input("Budgeted Fixed OH ($)", 0.0, value=80000.0, step=1000.0)
                denominator_hrs = st.number_input("Denominator Hours (capacity)", 0.0, value=10000.0, step=100.0)
                sh_per_unit = st.number_input("Standard Hours per Unit", 0.0, value=2.0, step=0.25)
                actual_units = st.number_input("Actual Units Produced", 0, value=4800, step=10)
            with col2:
                actual_foh = st.number_input("Actual Fixed OH ($)", 0.0, value=82000.0, step=500.0)

            foh_rate = budgeted_foh / denominator_hrs if denominator_hrs > 0 else 0
            sh_allowed = sh_per_unit * actual_units
            applied_foh = foh_rate * sh_allowed
            budget_var = actual_foh - budgeted_foh
            volume_var = budgeted_foh - applied_foh
            total_var = budget_var + volume_var

            st.metric("Fixed OH Rate", f"${foh_rate:.2f}/hr")

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Applied Fixed OH", f"${applied_foh:,.2f}")
            with col2: st.metric("Budget Variance", fav_label(budget_var))
            with col3: st.metric("Volume Variance", fav_label(volume_var))
            st.metric("Total FOH Variance", fav_label(total_var))

            st.markdown(f"""
            **Detailed Calculations:**
            ```
            Fixed OH Rate = ${budgeted_foh:,.2f} / {denominator_hrs:,.0f} hrs = ${foh_rate:.2f}/hr
            Standard Hours Allowed = {sh_per_unit} × {actual_units:,} = {sh_allowed:,.0f} hrs
            Applied FOH = {sh_allowed:,.0f} × ${foh_rate:.2f} = ${applied_foh:,.2f}

            Budget Variance = Actual FOH − Budgeted FOH
            = ${actual_foh:,.2f} − ${budgeted_foh:,.2f} = ${budget_var:,.2f}
            {'✅ Favorable' if budget_var < 0 else '❌ Unfavorable'}

            Volume Variance = Budgeted FOH − Applied FOH
            = ${budgeted_foh:,.2f} − ${applied_foh:,.2f} = ${volume_var:,.2f}
            {'✅ Favorable — produced more than denominator' if volume_var < 0 else '❌ Unfavorable — produced less than denominator'}
            ```
            """)

        else:  # Complete Variance Dashboard
            st.subheader("Complete Variance Dashboard")
            st.markdown("### Standard Cost Card:")
            col1, col2, col3 = st.columns(3)
            with col1:
                std_dm_qty = st.number_input("Std DM Qty/unit (lbs)", 0.0, value=5.0)
                std_dm_price = st.number_input("Std DM Price ($/lb)", 0.0, value=10.0)
            with col2:
                std_dl_hrs = st.number_input("Std DL hrs/unit", 0.0, value=2.0)
                std_dl_rate = st.number_input("Std DL rate ($/hr)", 0.0, value=20.0)
            with col3:
                std_voh_rate = st.number_input("Std VOH rate ($/hr)", 0.0, value=6.0)
                actual_units_prod = st.number_input("Actual units produced", 0, value=1000)

            st.markdown("### Actual Results:")
            col1, col2, col3 = st.columns(3)
            with col1:
                act_dm_purchased = st.number_input("DM Qty Purchased (lbs)", 0.0, value=5500.0)
                act_dm_price = st.number_input("DM Actual Price ($/lb)", 0.0, value=9.80)
                act_dm_used = st.number_input("DM Qty Used (lbs)", 0.0, value=5300.0)
            with col2:
                act_dl_hrs = st.number_input("DL Hours Worked", 0.0, value=2100.0)
                act_dl_rate = st.number_input("DL Actual Rate ($/hr)", 0.0, value=20.50)
            with col3:
                act_voh = st.number_input("Actual VOH ($)", 0.0, value=12800.0)

            if st.button("🧮 Calculate All Variances", type="primary"):
                sq = std_dm_qty * actual_units_prod
                mpv = (act_dm_price - std_dm_price) * act_dm_purchased
                mqv = (act_dm_used - sq) * std_dm_price

                sh = std_dl_hrs * actual_units_prod
                lrv = (act_dl_rate - std_dl_rate) * act_dl_hrs
                lev = (act_dl_hrs - sh) * std_dl_rate

                voh_sv = act_voh - (act_dl_hrs * std_voh_rate)
                voh_ev = (act_dl_hrs - sh) * std_voh_rate

                variances = [
                    ("DM Price Variance", mpv, "Purchasing Dept"),
                    ("DM Quantity Variance", mqv, "Production Dept"),
                    ("DL Rate Variance", lrv, "HR / Payroll"),
                    ("DL Efficiency Variance", lev, "Production Supervisor"),
                    ("VOH Spending Variance", voh_sv, "Production Dept"),
                    ("VOH Efficiency Variance", voh_ev, "Production Supervisor"),
                ]

                var_df = pd.DataFrame([{
                    "Variance": v[0],
                    "Amount": f"${abs(v[1]):,.2f}",
                    "F / U": "✅ Favorable" if v[1] < 0 else ("❌ Unfavorable" if v[1] > 0 else "On Target"),
                    "Responsible": v[2]
                } for v in variances])

                st.dataframe(var_df, use_container_width=True, hide_index=True)

                total_fav = sum(v[1] for v in variances if v[1] < 0)
                total_unfav = sum(v[1] for v in variances if v[1] > 0)
                net = sum(v[1] for v in variances)

                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Total Favorable", f"${abs(total_fav):,.2f}")
                with col2: st.metric("Total Unfavorable", f"${total_unfav:,.2f}")
                with col3: st.metric("Net Variance", fav_label(net))

    with tab4:
        st.header("📊 Visual Analytics")

        st.subheader("Variance Summary Chart")
        var_names = ["DM Price", "DM Quantity", "DL Rate", "DL Efficiency", "VOH Spending", "VOH Efficiency"]
        var_amounts = [-1100, 3000, 1050, 2000, 200, 600]
        colors = ["#27AE60" if v < 0 else "#E74C3C" for v in var_amounts]

        fig1 = go.Figure(go.Bar(
            x=var_names, y=var_amounts,
            marker_color=colors,
            text=[f"${abs(v):,} {'F' if v < 0 else 'U'}" for v in var_amounts],
            textposition="auto"
        ))
        fig1.add_hline(y=0, line_color="black", line_width=2)
        fig1.update_layout(
            title="Variance Analysis Summary (Negative = Favorable, Positive = Unfavorable)",
            xaxis_title="Variance Type", yaxis_title="Amount ($)"
        )
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Three-Box Model for Direct Materials")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **Box 1 — Actual Input × Actual Price:**
            ```
            5,500 lbs × $9.80
            = $53,900
            ```
            """)
        with col2:
            st.markdown("""
            **Box 2 — Actual Input × Standard Price:**
            ```
            5,500 lbs × $10.00
            = $55,000
            ```
            """)
        with col3:
            st.markdown("""
            **Box 3 — Std Input Allowed × Std Price:**
            ```
            5,000 lbs × $10.00
            = $50,000
            ```
            """)

        st.markdown("""
        ```
        Box1 ←──────────────────→ Box2 ←──────────────────→ Box3
        $53,900                   $55,000                   $50,000
                 Price Variance             Quantity Variance
                 $55,000 − $53,900          $55,000 − $50,000
                 = $1,100 F ✅              = $5,000 U  (but for used qty)
        ```
        """)

        st.subheader("Variance Pie — Favorable vs Unfavorable")
        total_fav = 1100
        total_unfav = 3000 + 1050 + 2000 + 200 + 600
        fig2 = px.pie(
            values=[total_fav, total_unfav],
            names=["Favorable", "Unfavorable"],
            title="Total Favorable vs Unfavorable Variances",
            color_discrete_map={"Favorable": "#27AE60", "Unfavorable": "#E74C3C"}
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Actual vs Standard Cost Comparison")
        categories = ["DM", "DL", "VOH", "Total"]
        std_costs = [50000, 40000, 12000, 102000]
        act_costs = [51900, 43050, 12800, 107750]

        fig3 = go.Figure(data=[
            go.Bar(name="Standard Cost", x=categories, y=std_costs, marker_color="#2E86C1"),
            go.Bar(name="Actual Cost", x=categories, y=act_costs, marker_color="#E74C3C")
        ])
        fig3.update_layout(title="Actual vs Standard Cost Comparison", barmode="group", yaxis_title="Cost ($)")
        st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        st.header("✅ Knowledge Check Quiz")
        st.subheader("Test Your Understanding")

        st.markdown("**Q1. A FAVORABLE variance means:**")
        q1 = st.radio("", [
            "Actual cost is greater than standard cost",
            "Actual cost is less than standard cost",
            "Actual cost equals standard cost",
            "The company made a profit"
        ], key="m9q1")
        if st.button("Check Q1", key="m9c1"):
            if q1 == "Actual cost is less than standard cost":
                st.success("✅ Correct! Favorable = actual cost < standard cost (spent less than planned).")
            else:
                st.error("❌ Incorrect. Favorable means actual cost is LESS than standard — you spent less than planned.")

        st.markdown("---")
        st.markdown("**Q2. The Materials Price Variance uses Actual Quantity:**")
        q2 = st.radio("", [
            "Used in production",
            "Purchased (not used)",
            "Standard quantity allowed",
            "Ending inventory"
        ], key="m9q2")
        if st.button("Check Q2", key="m9c2"):
            if q2 == "Purchased (not used)":
                st.success("✅ Correct! MPV = (AP − SP) × Actual Quantity PURCHASED.")
            else:
                st.error("❌ Incorrect. Price variance uses quantity PURCHASED to reflect the purchasing decision.")

        st.markdown("---")
        st.markdown("""
        **Q3. Standard: 4 lbs × $5 per unit. Actual: 4,400 lbs used for 1,000 units.
        Materials Quantity Variance = ?**
        """)
        q3 = st.radio("", ["$1,000 F", "$2,000 U", "$2,000 F", "$1,000 U"], key="m9q3")
        if st.button("Check Q3", key="m9c3"):
            if q3 == "$2,000 U":
                sq = 4 * 1000
                mqv = (4400 - sq) * 5
                st.success(f"✅ Correct! SQ Allowed = 4 × 1,000 = {sq:,}. MQV = ({4400:,} − {sq:,}) × $5 = ${mqv:,} U")
            else:
                st.error("❌ Incorrect. SQ Allowed = 4,000. MQV = (4,400 − 4,000) × $5 = $2,000 U")

        st.markdown("---")
        st.markdown("**Q4. The DL Efficiency Variance formula is:**")
        q4 = st.radio("", [
            "(Actual Rate − Standard Rate) × Actual Hours",
            "(Actual Hours − Standard Hours Allowed) × Standard Rate",
            "(Actual Hours − Standard Hours Allowed) × Actual Rate",
            "(Standard Rate − Actual Rate) × Standard Hours"
        ], key="m9q4")
        if st.button("Check Q4", key="m9c4"):
            if q4 == "(Actual Hours − Standard Hours Allowed) × Standard Rate":
                st.success("✅ Correct! LEV = (AH − SH Allowed) × SR")
            else:
                st.error("❌ Incorrect. LEV = (Actual Hours − Standard Hours Allowed) × Standard Rate")

        st.markdown("---")
        st.markdown("""
        **Q5. 1,200 units produced. Standard 2 hrs × $15/hr. Actual: 2,300 hrs @ $14.50/hr.
        What is the Labor Rate Variance?**
        """)
        q5 = st.radio("", ["$1,150 F", "$1,150 U", "$2,500 F", "$2,500 U"], key="m9q5")
        if st.button("Check Q5", key="m9c5"):
            lrv = (14.50 - 15.00) * 2300
            if q5 == "$1,150 F":
                st.success(f"✅ Correct! LRV = ($14.50 − $15.00) × 2,300 = ${lrv:,.2f} F")
            else:
                st.error(f"❌ Incorrect. LRV = ($14.50 − $15.00) × 2,300 = ${abs(lrv):,.2f} F (paid less than standard)")

    with tab6:
        st.header("📝 Module Summary & Recap")

        st.subheader("🎯 Complete Variance Formula Reference")
        formulas_df = pd.DataFrame({
            "Variance": [
                "DM Price Variance (MPV)", "DM Quantity Variance (MQV)",
                "DL Rate Variance (LRV)", "DL Efficiency Variance (LEV)",
                "VOH Spending Variance", "VOH Efficiency Variance",
                "FOH Budget Variance", "FOH Volume Variance",
                "Standard Qty Allowed", "Standard Hrs Allowed"
            ],
            "Formula": [
                "(AP − SP) × AQ PURCHASED",
                "(AQ Used − SQ Allowed) × SP",
                "(AR − SR) × AH Worked",
                "(AH Worked − SH Allowed) × SR",
                "Actual VOH − (AH × Standard VOH Rate)",
                "(AH − SH Allowed) × Standard VOH Rate",
                "Actual FOH − Budgeted FOH",
                "Budgeted FOH − (FOH Rate × SH Allowed)",
                "Standard Qty per Unit × Actual Units Produced",
                "Standard Hrs per Unit × Actual Units Produced"
            ],
            "Favorable When": [
                "AP < SP (paid less per unit)", "AQ Used < SQ (used less material)",
                "AR < SR (paid lower wage rate)", "AH < SH (worked fewer hours)",
                "Spent less on VOH than expected for hours", "AH < SH (same driver as DL efficiency)",
                "Actual FOH < Budget", "Produced more than denominator volume",
                "—", "—"
            ]
        })
        st.dataframe(formulas_df, use_container_width=True, hide_index=True)

        st.subheader("📌 Responsibility for Each Variance")
        resp_df = pd.DataFrame({
            "Variance": ["DM Price", "DM Quantity", "DL Rate", "DL Efficiency",
                          "VOH Spending", "VOH Efficiency", "FOH Budget", "FOH Volume"],
            "Typically Responsible": [
                "Purchasing Department", "Production Manager",
                "HR / Payroll Manager", "Production Supervisor",
                "Production Department", "Production Supervisor",
                "Plant / Cost Center Manager", "Production Planning"
            ],
            "Common Causes": [
                "Market price changes, order size, supplier quality",
                "Machine problems, worker skill, material quality",
                "Union contracts, overtime, skill mix",
                "Training, machine efficiency, material quality",
                "Utility rate changes, waste, inefficiency",
                "Same causes as DL efficiency",
                "Unexpected rent, insurance, salary changes",
                "Actual output above/below expected capacity"
            ]
        })
        st.dataframe(resp_df, use_container_width=True, hide_index=True)

        st.subheader("🚨 Common Mistakes to Avoid")
        mistakes_df = pd.DataFrame({
            "Mistake": [
                "Using AQ Used for price variance (should be AQ Purchased)",
                "Using AQ Purchased for quantity variance (should be AQ Used)",
                "Forgetting Standard Qty Allowed is based on ACTUAL production",
                "Using AQ instead of SQ in the standard box for verification",
                "Treating all unfavorable variances as bad",
                "Ignoring interdependencies between variances"
            ],
            "Correct Approach": [
                "MPV always uses quantity PURCHASED — reflects purchasing decision",
                "MQV always uses quantity USED — reflects production efficiency",
                "SQ Allowed = Standard/unit × ACTUAL units produced (not budgeted)",
                "Always verify: Actual − Standard = Sum of all variances",
                "Sometimes unfavorable is acceptable (e.g., better quality materials)",
                "Cheap materials (F price) often cause wastage (U quantity) — investigate together"
            ]
        })
        st.dataframe(mistakes_df, use_container_width=True, hide_index=True)

        st.success("🎓 Module 9 Complete! You can calculate, interpret, and investigate all cost variances.")
        st.info("💡 Next: Module 10 — Responsibility Accounting & Segment Reporting")

if __name__ == "__main__":
    show()