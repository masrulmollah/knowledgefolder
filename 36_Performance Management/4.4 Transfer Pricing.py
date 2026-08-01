"""
Performance Management — Applied Learning Series
Module 4.4 · Transfer Pricing
------------------------------------------------------------
Setting the price for internal transfers between divisions so that
divisional and GROUP interests stay aligned (goal congruence).
  • The general rule: TP = marginal cost + opportunity cost
  • Spare-capacity vs. full-capacity cases
  • The negotiable range (supplier floor .. buyer ceiling)

Run with:  streamlit run 4.4_Transfer_Pricing.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="4.4 · Transfer Pricing",
    page_icon="🔀",
    layout="wide",
)

# ------------------------------------------------------------------
# LIGHT THEME / STYLING (consistent with the site)
# ------------------------------------------------------------------
st.markdown(
    """
    <style>
        .big-title   {font-size:2.1rem; font-weight:800; color:#1f3b57; margin-bottom:0;}
        .subtle      {color:#5c6b7a; font-size:1.02rem;}
        .zone-header {font-size:1.35rem; font-weight:700; color:#1f3b57;
                      border-left:5px solid #2e86de; padding-left:10px; margin-top:8px;}
        .pill        {display:inline-block; padding:4px 12px; border-radius:14px;
                      background:#eaf2fb; color:#2e86de; font-weight:600; font-size:0.8rem;}
        .good        {color:#1e8449; font-weight:700;}
        .bad         {color:#c0392b; font-weight:700;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# ① HEADER ZONE
# ------------------------------------------------------------------
st.markdown('<p class="pill">MODULE 4 · PERFORMANCE MEASUREMENT — FINANCIAL</p>', unsafe_allow_html=True)
st.markdown('<p class="big-title">4.4 · Transfer Pricing</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtle">Objective: set a transfer price that keeps <b>both divisions and the group</b> '
    'making goal-congruent decisions, using the general rule <b>TP = marginal cost + opportunity cost</b>, '
    'and identify the <b>negotiable range</b>.</p>',
    unsafe_allow_html=True,
)
st.divider()

# ------------------------------------------------------------------
# ② CONCEPT ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">② The Concept</p>', unsafe_allow_html=True)

c1, c2 = st.columns([1.35, 1])
with c1:
    st.markdown(
        """
A **transfer price** is the internal price at which one division (the **supplying** division)
sells goods or services to another (the **receiving** division) in the same group. It is
revenue to the seller and a cost to the buyer, so it directly shapes each division's reported
profit — and therefore each manager's behaviour.

**The goal:** set a price that leads each divisional manager, acting in their own interest, to
make the decision that is **best for the group as a whole** (goal congruence).

**The general rule:**

- **Transfer price = Marginal cost + Opportunity cost** (to the supplying division)

Two cases follow:

- **Spare capacity** — the supplier has no better use for the units, so opportunity cost is
  **zero**. The minimum acceptable transfer price is just **marginal (variable) cost**.
- **Full capacity** — supplying internally means **giving up an external sale**, so the
  opportunity cost is the **lost contribution**. The minimum transfer price rises to
  **marginal cost + lost contribution** (usually the external market price).

**The negotiable range:**

- **Supplier's floor** = its marginal cost + any opportunity cost (won't sell below this).
- **Buyer's ceiling** = the lower of the **external price** it could buy at, or the **net
  revenue** it can earn from the final product (won't buy above this).
- A transfer is worthwhile for the group **only if a range exists** (floor ≤ ceiling); the
  actual price is then negotiated within it.

**Methods in practice:** market-based, cost-based (marginal or full cost, ±mark-up),
two-part tariffs, and negotiated prices — each with trade-offs in fairness and simplicity.
        """
    )
with c2:
    st.info(
        "**Why it matters in finance**\n\n"
        "Transfer pricing is where divisional autonomy collides with group profit. Set it wrong and "
        "a manager optimising their own P&L will destroy group value — buying outside when internal "
        "supply is cheaper, or refusing a profitable internal transfer. It also drives tax and "
        "regulatory exposure in multinationals.",
        icon="💡",
    )

st.divider()

# ------------------------------------------------------------------
# ③ INTERACTIVE MODEL ZONE — Transfer Price Engine
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">③ Interactive Model — The Transfer-Price Engine</p>',
            unsafe_allow_html=True)
st.caption("Set each division's economics and the capacity situation; the engine finds the range and tests goal congruence.")

left, right = st.columns([1, 1.5])

with left:
    st.markdown("#### 🎛️ Supplying division")
    var_cost   = st.number_input("Marginal (variable) cost per unit (BDT)", 0.0, 100000.0, 40.0, step=1.0)
    ext_price  = st.number_input("External market price per unit (BDT)", 0.0, 100000.0, 70.0, step=1.0)
    capacity   = st.selectbox("Capacity situation", ["Spare capacity", "Full capacity"])

    st.markdown("#### 🎛️ Receiving division")
    final_price = st.number_input("Final selling price of end product (BDT)", 0.0, 1000000.0, 150.0, step=5.0)
    further_cost = st.number_input("Receiver's own further costs per unit (BDT)", 0.0, 1000000.0, 60.0, step=1.0)
    ext_buy_price = st.number_input("Price to buy externally instead (BDT)", 0.0, 100000.0, 72.0, step=1.0)

    proposed_tp = st.slider("Proposed transfer price (BDT)", 0.0, 200.0, 55.0, step=1.0)

# ---- Logic ----
# Opportunity cost to supplier
if capacity == "Full capacity":
    opp_cost = ext_price - var_cost   # lost contribution from external sale
else:
    opp_cost = 0.0

supplier_floor = var_cost + opp_cost
# Buyer ceiling: lower of external buy price OR net revenue from final product
net_revenue = final_price - further_cost
buyer_ceiling = min(ext_buy_price, net_revenue)

range_exists = supplier_floor <= buyer_ceiling

with right:
    st.markdown("#### 📊 The Negotiable Range")
    a, b, c = st.columns(3)
    a.metric("Supplier's floor", f"{supplier_floor:,.1f} BDT",
             "MC only" if capacity == "Spare capacity" else "MC + lost contribution")
    b.metric("Buyer's ceiling", f"{buyer_ceiling:,.1f} BDT",
             "min(ext price, net rev)")
    c.metric("Range width", f"{max(buyer_ceiling - supplier_floor, 0):,.1f} BDT",
             "exists ✅" if range_exists else "none ❌",
             delta_color="normal" if range_exists else "inverse")

    # Range chart
    fig = go.Figure()
    lo = min(supplier_floor, buyer_ceiling, proposed_tp) - 10
    hi = max(supplier_floor, buyer_ceiling, proposed_tp, ext_price) + 10
    # range band
    if range_exists:
        fig.add_shape(type="rect", x0=supplier_floor, x1=buyer_ceiling, y0=0, y1=1,
                      fillcolor="#abebc6", opacity=0.5, line_width=0)
    fig.add_vline(x=supplier_floor, line=dict(color="#c0392b", width=2),
                  annotation_text="Floor", annotation_position="top")
    fig.add_vline(x=buyer_ceiling, line=dict(color="#2e86de", width=2),
                  annotation_text="Ceiling", annotation_position="top")
    fig.add_vline(x=proposed_tp, line=dict(color="#e67e22", width=3, dash="dash"),
                  annotation_text="Proposed TP", annotation_position="bottom")
    fig.update_layout(height=200, margin=dict(t=40, b=30),
                      xaxis_title="Transfer price (BDT)", yaxis=dict(visible=False),
                      xaxis=dict(range=[lo, hi]), plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

    # Profit split at proposed TP (per unit)
    supplier_profit = proposed_tp - var_cost
    buyer_profit = final_price - further_cost - proposed_tp
    group_profit = final_price - further_cost - var_cost

    st.markdown("**Per-unit profit at the proposed transfer price**")
    split = pd.DataFrame({
        "Party": ["Supplying division", "Receiving division", "Group total"],
        "Profit per unit (BDT)": [supplier_profit, buyer_profit, group_profit],
    })
    st.dataframe(split.style.format({"Profit per unit (BDT)": "{:,.1f}"}),
                 use_container_width=True, hide_index=True)

st.divider()

# ------------------------------------------------------------------
# ④ INTERPRETATION ZONE — dynamic
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">④ Interpretation</p>', unsafe_allow_html=True)

# Group-level decision
if group_profit > 0:
    group_msg = (f"At group level, internal supply **creates {group_profit:,.1f} BDT per unit** "
                 f"(final {final_price:,.0f} − further {further_cost:,.0f} − marginal {var_cost:,.0f}), "
                 f"so the group **should** want the transfer to happen.")
else:
    group_msg = (f"At group level, the end product **destroys value** ({group_profit:,.1f} BDT per unit) — "
                 f"the group should not make it at all, regardless of transfer price.")

st.markdown(f"- 🏢 **Group view:** {group_msg}")

if range_exists:
    st.markdown(
        f"""
- ✅ **A range exists: {supplier_floor:,.1f} – {buyer_ceiling:,.1f} BDT.** Any price in this band leaves
  **both** divisions better off transferring internally than not, so it is goal-congruent. The exact
  point just splits the group profit between them.
        """
    )
    # Check proposed TP position
    if supplier_floor <= proposed_tp <= buyer_ceiling:
        st.success(
            f"**Proposed TP of {proposed_tp:,.1f} BDT sits inside the range.** Supplier earns "
            f"{supplier_profit:,.1f}, receiver earns {buyer_profit:,.1f}, and together they capture the "
            f"full group profit of {group_profit:,.1f} per unit. A well-chosen transfer price. ✅",
            icon="✅",
        )
    elif proposed_tp < supplier_floor:
        st.warning(
            f"**Proposed TP ({proposed_tp:,.1f}) is below the supplier's floor ({supplier_floor:,.1f}).** "
            f"The supplying manager loses on every unit and will **refuse to transfer** — even though the "
            f"group benefits. Raise the price into the range.",
            icon="⚠️",
        )
    else:
        st.warning(
            f"**Proposed TP ({proposed_tp:,.1f}) is above the buyer's ceiling ({buyer_ceiling:,.1f}).** "
            f"The receiving manager would rather buy externally (or stop making the product) and will "
            f"**refuse to buy internally**. Lower the price into the range.",
            icon="⚠️",
        )
else:
    st.error(
        f"**No range exists — floor ({supplier_floor:,.1f}) is above ceiling ({buyer_ceiling:,.1f}).** "
        f"No single transfer price satisfies both divisions. If the supplier is at **full capacity** and "
        f"can earn {ext_price:,.0f} externally while the buyer can source at {ext_buy_price:,.0f}, the "
        f"group is usually **better off trading externally** on both sides. Internal transfer isn't "
        f"worthwhile here.",
        icon="🔴",
    )

# Capacity note
if capacity == "Spare capacity":
    st.caption(f"💡 With **spare capacity**, opportunity cost is zero, so the floor is just marginal "
               f"cost ({var_cost:,.0f} BDT). This is why spare-capacity transfers should be priced low "
               f"to encourage internal trade.")
else:
    st.caption(f"💡 At **full capacity**, the floor rises to marginal cost + lost contribution "
               f"= {var_cost:,.0f} + {opp_cost:,.0f} = {supplier_floor:,.0f} BDT, because each internal "
               f"unit sacrifices an external sale.")

st.divider()

# ------------------------------------------------------------------
# ⑤ APPLY IT ZONE
# ------------------------------------------------------------------
st.markdown('<p class="zone-header">⑤ Apply It</p>', unsafe_allow_html=True)

a1, a2 = st.columns([1, 1])
with a1:
    st.markdown("**Takeaway checklist**")
    st.markdown(
        """
        - [ ] **TP = marginal cost + opportunity cost** (the general rule).
        - [ ] **Spare capacity** → opportunity cost = 0 → floor = marginal cost.
        - [ ] **Full capacity** → floor = marginal cost + lost contribution.
        - [ ] Range = **supplier floor .. buyer ceiling**; transfer only if it exists.
        - [ ] A good TP keeps **divisional and group** interests aligned.
        """
    )
with a2:
    with st.expander("📘 Key rules in this module"):
        st.markdown(
            """
            - **General rule:** TP = marginal cost + opportunity cost
            - **Supplier's minimum** = marginal cost + lost contribution (0 if spare capacity)
            - **Buyer's maximum** = min(external purchase price, net revenue from final product)
            - **Group net benefit/unit** = final price − further cost − marginal cost
            """
        )
    with st.expander("🧭 Transfer-pricing methods compared"):
        st.markdown(
            """
            | Method | Pro | Con |
            |---|---|---|
            | **Market price** | Objective, fair | Needs a market; price volatile |
            | **Marginal cost** | Group-optimal in short run | Supplier makes no profit |
            | **Full cost (+mark-up)** | Covers costs | Can distort decisions |
            | **Negotiated** | Autonomy, motivation | Time-consuming; power imbalance |
            | **Two-part tariff** | Splits fixed & variable | Complex to administer |
            """
        )

# Downloadable summary
template = pd.DataFrame({
    "Item": ["Capacity situation", "Marginal cost/unit", "External price/unit",
             "Opportunity cost/unit", "Supplier floor", "Buyer ceiling", "Range exists?",
             "Proposed TP", "Supplier profit/unit", "Receiver profit/unit", "Group profit/unit"],
    "Value": [capacity, var_cost, ext_price, opp_cost, round(supplier_floor, 1),
              round(buyer_ceiling, 1), "Yes" if range_exists else "No", proposed_tp,
              round(supplier_profit, 1), round(buyer_profit, 1), round(group_profit, 1)],
})
st.download_button(
    "⬇️ Download the transfer-pricing analysis (CSV)",
    data=template.to_csv(index=False).encode("utf-8"),
    file_name="transfer_pricing.csv",
    mime="text/csv",
)

st.divider()

# ------------------------------------------------------------------
# NAVIGATION
# ------------------------------------------------------------------
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    st.button("◀ Previous: 4.3 · Ratio Analysis for Performance", use_container_width=True, disabled=True)
with nav3:
    st.button("Next: 5.1 · The Balanced Scorecard ▶", use_container_width=True, disabled=True)

st.caption("Performance Management · Applied Learning Series · Module 4.4")
