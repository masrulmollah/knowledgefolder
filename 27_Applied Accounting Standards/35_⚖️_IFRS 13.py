import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("⚖️ IFRS 13: Fair Value Measurement")
    st.markdown("*Master the single IFRS framework for measuring and disclosing fair value across all standards*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📖 Learn", "🧮 Examples", "💡 Interactive Tools",
        "📊 Visualizations", "✅ Quiz", "📝 Summary"
    ])

    with tab1:
        st.header("Core Concepts")

        st.subheader("1. Objective and the Single Definition")
        st.markdown("""
        **IFRS 13** does NOT determine WHEN fair value is required (that's specified by other standards like IFRS 9, IAS 16, IAS 40) — it defines HOW to measure fair value consistently and what to disclose.

        **Fair Value Definition:**
        > *"The price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date."*

        This is an **exit price** notion — what you'd receive to SELL, not what you'd pay to acquire.
        """)

        st.subheader("2. Key Concepts in the Definition")
        st.markdown("""
        | Concept | Meaning |
        |---|---|
        | **Orderly transaction** | NOT a forced sale or distressed liquidation — assumes normal market exposure |
        | **Market participants** | Independent, knowledgeable, willing and able to transact — NOT entity-specific |
        | **Principal market** | The market with greatest volume/activity for the asset/liability |
        | **Most advantageous market** | Used only if no principal market is identifiable — maximizes amount received (asset) or minimizes amount paid (liability) |
        | **Highest and best use** | For non-financial assets — physically possible, legally permissible, financially feasible use that maximizes value |
        """)

        st.subheader("3. The Fair Value Hierarchy — Three Levels")
        st.markdown("""
        IFRS 13 establishes a hierarchy that prioritizes inputs used in valuation techniques:

        | Level | Inputs | Examples |
        |---|---|---|
        | **Level 1** | Quoted prices in ACTIVE markets for IDENTICAL assets/liabilities | Listed shares, exchange-traded bonds |
        | **Level 2** | Observable inputs other than Level 1 quoted prices (directly or indirectly) | Interest rate curves, quoted prices for similar assets, market-corroborated inputs |
        | **Level 3** | UNOBSERVABLE inputs | Discounted cash flow models with entity-specific assumptions, private equity valuations |

        **Hierarchy preference:** Maximize use of Level 1, minimize use of Level 3. The level assigned is based on the LOWEST level input that is significant to the entire measurement.
        """)

        st.subheader("4. Valuation Techniques")
        st.markdown("""
        Three main approaches (use the technique(s) appropriate given available data):

        | Technique | Description | Best Used When |
        |---|---|---|
        | **Market Approach** | Uses prices from identical/comparable transactions | Active market data available |
        | **Income Approach** | Converts future cash flows/income to a single discounted present value | DCF valuations, option pricing models |
        | **Cost Approach** | Reflects the amount required to replace the asset's service capacity (replacement cost) | Specialised assets with no active market |

        Use consistently; change technique only if it results in equally/more representative fair value.
        """)

        st.subheader("5. Measuring Liabilities and Own Equity Instruments")
        st.markdown("""
        - Liabilities are measured assuming **transfer to a market participant**, not settlement
        - If a quoted price for transferring the identical liability isn't available, use the quoted price of the IDENTICAL item held as an asset by another party (if available)
        - **No adjustment for restrictions** preventing transfer of the liability (already inherent)
        - Include effect of **non-performance risk** (including the entity's own credit risk) in liability fair value measurement
        """)

        st.subheader("6. Disclosure Requirements")
        st.markdown("""
        For items measured at fair value (recurring or non-recurring):
        - Fair value hierarchy level for each class of asset/liability
        - For Level 3: reconciliation of opening to closing balances, including gains/losses, purchases/sales, transfers in/out
        - Valuation techniques and significant unobservable inputs used for Level 2/3
        - Sensitivity analysis for Level 3 (how reasonably possible alternative assumptions would change FV)
        - Transfers between hierarchy levels and reasons for the transfer

        For items NOT measured at fair value but where fair value is disclosed (e.g., financial instruments at amortised cost) → similar disclosures apply.
        """)

    with tab2:
        st.header("Practical Examples")

        st.subheader("Example 1: Fair Value Hierarchy Classification")
        hierarchy_examples = pd.DataFrame({
            "Asset/Liability": [
                "Shares listed on NYSE",
                "Corporate bond priced using yield curve from similar bonds",
                "Unlisted equity investment valued using DCF with entity-specific growth assumptions",
                "Government bond actively traded on a major exchange",
                "Investment property valued using comparable sales (similar properties, adjusted)",
                "Complex derivative valued using a proprietary model with unobservable correlation assumptions"
            ],
            "Level": ["Level 1", "Level 2", "Level 3", "Level 1", "Level 2", "Level 3"],
            "Reasoning": [
                "Quoted price, active market, identical asset",
                "Observable market data (yield curves) used to derive price",
                "Unobservable inputs (entity-specific growth rate) significant to valuation",
                "Quoted price, active market, identical asset",
                "Comparable transactions are observable but require adjustment",
                "Significant unobservable inputs (correlation assumptions)"
            ]
        })
        st.dataframe(hierarchy_examples, use_container_width=True, hide_index=True)

        st.subheader("Example 2: Principal Market vs Most Advantageous Market")
        st.markdown("""
        **Asset can be sold in two markets:**

        | Market | Price | Transaction Costs | Net Amount Received | Volume |
        |---|---|---|---|---|
        | Market A | $100 | $5 | $95 | High (Principal Market) |
        | Market B | $102 | $8 | $94 | Lower |

        **If Market A is the PRINCIPAL market** (highest volume) → use Market A's price = **$100** (fair value, BEFORE transaction costs — transaction costs are NOT deducted from fair value itself, though they may affect net proceeds disclosed elsewhere)

        If NO principal market is identifiable → use the most advantageous market (Market A, since net $95 > net $94)
        """)

        st.subheader("Example 3: Income Approach — DCF Valuation")
        st.markdown("""
        **Unlisted investment fair value using DCF (Level 3):**

        | Year | Forecast Cash Flow | Discount Factor (12%) | PV |
        |---|---|---|---|
        | 1 | $200,000 | 0.893 | $178,600 |
        | 2 | $250,000 | 0.797 | $199,250 |
        | 3 | $300,000 | 0.712 | $213,600 |
        | Terminal Value | $2,500,000 | 0.712 | $1,780,000 |
        | **Fair Value** | | | **$2,371,450** |

        Key unobservable inputs requiring disclosure: discount rate (12%), terminal growth rate, cash flow projections.
        """)

        st.subheader("Example 4: Level 3 Reconciliation Disclosure")
        st.markdown("""
        | | $000 |
        |---|---|
        | Opening balance (Level 3 assets) | 5,200 |
        | Purchases | 800 |
        | Sales | (300) |
        | Gains recognised in P&L | 150 |
        | Losses recognised in OCI | (50) |
        | Transfers into Level 3 | 200 |
        | Transfers out of Level 3 | (100) |
        | **Closing balance (Level 3 assets)** | **5,900** |

        Plus required sensitivity disclosure: e.g., "A 1% increase in the discount rate would decrease fair value by approximately $180,000."
        """)

    with tab3:
        st.header("Interactive Tools")

        st.subheader("🔧 Tool 1: Fair Value Hierarchy Classifier")
        instrument_type = st.selectbox("Select the asset/liability:", [
            "Quoted equity shares on a major stock exchange",
            "Bond priced using observable yield curves for similar instruments",
            "Private equity investment valued with unobservable management projections",
            "Exchange-traded commodity futures",
            "Property valued using adjusted comparable sales data",
            "Complex structured derivative with proprietary correlation model"
        ])
        level_map = {
            "Quoted equity shares on a major stock exchange": ("Level 1", "Direct quoted price in active market for identical instrument"),
            "Bond priced using observable yield curves for similar instruments": ("Level 2", "Uses observable market inputs, but not a direct quote for the identical instrument"),
            "Private equity investment valued with unobservable management projections": ("Level 3", "Significant unobservable inputs (management's own projections/assumptions)"),
            "Exchange-traded commodity futures": ("Level 1", "Quoted price in active market for identical contract"),
            "Property valued using adjusted comparable sales data": ("Level 2", "Observable comparable transactions with adjustments — generally Level 2 unless adjustments are highly subjective"),
            "Complex structured derivative with proprietary correlation model": ("Level 3", "Unobservable correlation/volatility assumptions significant to the valuation")
        }
        level, reasoning = level_map[instrument_type]
        if level == "Level 1":
            st.success(f"📊 **{level}**\n\n{reasoning}")
        elif level == "Level 2":
            st.info(f"📊 **{level}**\n\n{reasoning}")
        else:
            st.warning(f"📊 **{level}**\n\n{reasoning}")

        st.markdown("---")
        st.subheader("🔧 Tool 2: DCF Fair Value Calculator (Income Approach)")
        col1, col2 = st.columns(2)
        with col1:
            discount_rate_fv = st.number_input("Discount Rate (%)", value=12.0, step=0.5) / 100
            n_years_fv = st.number_input("Forecast Years", value=3, min_value=1, max_value=10)
            terminal_value = st.number_input("Terminal Value ($)", value=2500000, step=50000)
        with col2:
            cash_flows_fv = []
            for i in range(int(n_years_fv)):
                cf = st.number_input(f"Year {i+1} Cash Flow ($)", value=200000+i*50000, step=10000, key=f"fv_cf_{i}")
                cash_flows_fv.append(cf)

        if st.button("Calculate Fair Value (DCF)"):
            total_pv = 0
            rows_fv = []
            for i, cf in enumerate(cash_flows_fv, 1):
                df_val = 1 / (1 + discount_rate_fv)**i
                pv = cf * df_val
                total_pv += pv
                rows_fv.append({"Year": i, "Cash Flow ($)": f"{cf:,.0f}", "Discount Factor": f"{df_val:.3f}", "PV ($)": f"{pv:,.0f}"})
            tv_pv = terminal_value / (1 + discount_rate_fv)**int(n_years_fv)
            total_pv += tv_pv
            rows_fv.append({"Year": f"Terminal (Yr {int(n_years_fv)})", "Cash Flow ($)": f"{terminal_value:,.0f}", "Discount Factor": f"{1/(1+discount_rate_fv)**int(n_years_fv):.3f}", "PV ($)": f"{tv_pv:,.0f}"})
            st.dataframe(pd.DataFrame(rows_fv), use_container_width=True, hide_index=True)
            st.success(f"**Fair Value (Level 3, Income Approach) = ${total_pv:,.0f}**")

        st.markdown("---")
        st.subheader("🔧 Tool 3: Principal Market Selector")
        col1, col2 = st.columns(2)
        with col1:
            market_a_price = st.number_input("Market A Price ($)", value=100.0)
            market_a_costs = st.number_input("Market A Transaction Costs ($)", value=5.0)
            market_a_volume = st.selectbox("Market A — Higher Volume?", [True, False])
        with col2:
            market_b_price = st.number_input("Market B Price ($)", value=102.0)
            market_b_costs = st.number_input("Market B Transaction Costs ($)", value=8.0)

        if st.button("Determine Fair Value"):
            if market_a_volume:
                st.success(f"**Principal Market = Market A** (highest volume)\n\n**Fair Value = ${market_a_price:.2f}** (the quoted price BEFORE transaction costs)")
            else:
                net_a = market_a_price - market_a_costs
                net_b = market_b_price - market_b_costs
                if net_a > net_b:
                    st.info(f"No clear principal market — use Most Advantageous Market.\nMarket A net: ${net_a:.2f} > Market B net: ${net_b:.2f}\n\n**Fair Value = ${market_a_price:.2f}** (Market A's quoted price)")
                else:
                    st.info(f"No clear principal market — use Most Advantageous Market.\nMarket B net: ${net_b:.2f} > Market A net: ${net_a:.2f}\n\n**Fair Value = ${market_b_price:.2f}** (Market B's quoted price)")

    with tab4:
        st.header("Visualizations")

        st.subheader("Fair Value Hierarchy Pyramid")
        fig = go.Figure(go.Funnel(
            y=["Level 1: Quoted Prices\n(Active Markets)", "Level 2: Observable\nInputs", "Level 3: Unobservable\nInputs"],
            x=[100, 60, 25],
            marker={"color": ["#34D399", "#F59E0B", "#F87171"]}
        ))
        fig.update_layout(title="IFRS 13 Fair Value Hierarchy — Preference Order", height=400)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("DCF Fair Value Sensitivity to Discount Rate")
        rates_sens = [8, 9, 10, 11, 12, 13, 14, 15, 16]
        fvs = []
        for r in rates_sens:
            rate = r/100
            pv = sum([(200000+i*50000)/(1+rate)**(i+1) for i in range(3)]) + 2500000/(1+rate)**3
            fvs.append(pv)
        fig2 = go.Figure(go.Scatter(x=rates_sens, y=fvs, line=dict(color="#2563EB", width=2), mode="lines+markers"))
        fig2.update_layout(title="Fair Value Sensitivity to Discount Rate Changes (Level 3 Asset)",
                          xaxis_title="Discount Rate (%)", yaxis_title="Fair Value ($)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    with tab5:
        st.header("Knowledge Check Quiz")

        st.markdown("**1. IFRS 13 defines fair value as:**")
        q1 = st.radio("", [
            "The amount the entity originally paid for an asset",
            "The price to sell an asset or transfer a liability in an orderly transaction between market participants",
            "The entity's own estimate of an asset's worth",
            "The replacement cost of an asset"
        ], key="ifrs13q1")
        if st.button("Check Answer", key="ifrs13c1"):
            if q1 == "The price to sell an asset or transfer a liability in an orderly transaction between market participants":
                st.success("✅ Correct! This is the EXIT PRICE notion — what you'd receive to sell (or pay to transfer), assuming an orderly (non-forced) transaction between knowledgeable, willing market participants.")
            else:
                st.error("❌ Fair value = EXIT PRICE in an orderly transaction between market participants — not historical cost, entity-specific value, or replacement cost (though cost approach may sometimes be used as a technique).")

        st.markdown("---")
        st.markdown("**2. Level 1 inputs in the fair value hierarchy are:**")
        q2 = st.radio("", [
            "Unobservable inputs based on management assumptions",
            "Observable inputs other than quoted prices",
            "Quoted prices in active markets for identical assets/liabilities",
            "Cost-based estimates"
        ], key="ifrs13q2")
        if st.button("Check Answer", key="ifrs13c2"):
            if q2 == "Quoted prices in active markets for identical assets/liabilities":
                st.success("✅ Correct! Level 1 = the highest quality inputs: quoted prices in ACTIVE markets for IDENTICAL items, with no adjustment needed.")
            else:
                st.error("❌ Level 1 = quoted prices in ACTIVE markets for IDENTICAL assets/liabilities. Level 2 = other observable inputs. Level 3 = unobservable inputs.")

        st.markdown("---")
        st.markdown("**3. The fair value hierarchy level assigned to a measurement is based on:**")
        q3 = st.radio("", [
            "The highest level input used", "The lowest level input that is significant to the entire measurement", "An average of all inputs used", "Management's preference"
        ], key="ifrs13q3")
        if st.button("Check Answer", key="ifrs13c3"):
            if q3 == "The lowest level input that is significant to the entire measurement":
                st.success("✅ Correct! Even if most inputs are observable (Level 1/2), if a SIGNIFICANT unobservable input (Level 3) is used, the ENTIRE measurement is classified as Level 3.")
            else:
                st.error("❌ The level is determined by the LOWEST level input that is SIGNIFICANT — one significant Level 3 input makes the whole measurement Level 3.")

        st.markdown("---")
        st.markdown("**4. When measuring the fair value of a liability, the entity should include the effect of:**")
        q4 = st.radio("", [
            "Only market interest rate risk",
            "Non-performance risk, including the entity's own credit risk",
            "Only the counterparty's credit risk",
            "No credit risk adjustments are permitted"
        ], key="ifrs13q4")
        if st.button("Check Answer", key="ifrs13c4"):
            if q4 == "Non-performance risk, including the entity's own credit risk":
                st.success("✅ Correct! IFRS 13 requires including non-performance risk — including the REPORTING ENTITY'S OWN credit risk — when measuring fair value of a liability.")
            else:
                st.error("❌ Liability fair value must reflect non-performance risk INCLUDING the entity's OWN credit risk.")

        st.markdown("---")
        st.markdown("**5. The 'highest and best use' concept applies to:**")
        q5 = st.radio("", [
            "All financial instruments", "Non-financial assets", "Financial liabilities only", "Cash and cash equivalents"
        ], key="ifrs13q5")
        if st.button("Check Answer", key="ifrs13c5"):
            if q5 == "Non-financial assets":
                st.success("✅ Correct! 'Highest and best use' is specifically a concept for NON-FINANCIAL ASSETS — it considers the use that maximizes the asset's value (physically possible, legally permissible, financially feasible). Financial instruments don't have alternative 'uses' in this sense.")
            else:
                st.error("❌ 'Highest and best use' applies specifically to NON-FINANCIAL assets (e.g., land, buildings) — not financial instruments.")

    with tab6:
        st.header("Summary")

        st.markdown("""
        ### 1. Fair Value Definition
        **Exit price** — price to SELL an asset or TRANSFER a liability in an orderly transaction between market participants at the measurement date.

        ### 2. Fair Value Hierarchy
        | Level | Input Type | Priority |
        |---|---|---|
        | Level 1 | Quoted prices, active markets, identical items | Highest |
        | Level 2 | Observable inputs (not Level 1) | Middle |
        | Level 3 | Unobservable inputs | Lowest (use minimally) |

        **Classification rule:** Based on the LOWEST significant input level.

        ### 3. Valuation Techniques
        - Market Approach (comparable transactions)
        - Income Approach (DCF, option pricing)
        - Cost Approach (replacement cost)

        ### 4. Key Special Rules
        - **Principal market** (highest volume) used first; **most advantageous market** only if no principal market
        - **Liabilities**: include non-performance risk (own credit risk)
        - **Non-financial assets**: consider "highest and best use"
        - Transaction costs are NOT part of fair value itself

        ### 5. Disclosures
        - Hierarchy level for each FV item
        - Level 3 reconciliation + sensitivity analysis
        - Valuation techniques and significant inputs
        """)

        st.subheader("📌 Key Rules to Remember")
        st.code("""
Fair Value = EXIT PRICE (what you'd receive to SELL)
Hierarchy: Level 1 (quoted, identical) > Level 2 (observable) > Level 3 (unobservable)
Classification = LOWEST significant input level used
Liability FV → includes OWN credit risk (non-performance risk)
Highest and best use → applies to NON-FINANCIAL assets only
Principal market first; most advantageous market only as fallback
        """)

        st.success("🎓 **IFRS 13 Complete!** You can now classify fair value measurements by hierarchy level, apply valuation techniques, and prepare required disclosures.")
        st.info("💡 **Next**: IFRS 15 — Revenue from Contracts with Customers")

if __name__ == "__main__":
    show()