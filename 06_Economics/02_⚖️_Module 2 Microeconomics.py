import streamlit as st

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: #f5f3ee;
    color: #1a1a2e;
}

/* Hero Banner */
.hero {
    background: linear-gradient(135deg, #0d3b2e 0%, #155740 60%, #1a7a55 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "μ";
    position: absolute;
    right: 40px;
    top: -10px;
    font-size: 200px;
    color: rgba(255,255,255,0.05);
    font-family: 'Playfair Display', serif;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    color: #e2f0e8;
    margin: 0 0 8px 0;
}
.hero p {
    color: #a8c8b5;
    font-size: 1.05rem;
    margin: 0;
    font-weight: 300;
}
.hero .badge {
    display: inline-block;
    background: rgba(226,240,232,0.15);
    color: #e2f0e8;
    border: 1px solid rgba(226,240,232,0.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

/* Topic Cards */
.topic-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 16px;
    border-left: 4px solid #155740;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: #0d3b2e;
    margin: 0 0 10px 0;
}
.topic-card p {
    font-size: 0.96rem;
    line-height: 1.8;
    color: #3a3a4a;
    margin: 0;
}

/* Key Term Pills */
.key-terms {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 12px;
}
.term-pill {
    background: #e8f5ee;
    color: #0d3b2e;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid #a8d5b5;
}

/* Takeaway box */
.takeaway {
    background: linear-gradient(135deg, #fff9ee, #fff3d6);
    border: 1px solid #f5d78e;
    border-radius: 10px;
    padding: 14px 18px;
    margin-top: 12px;
    font-size: 0.9rem;
    color: #5a4000;
}
.takeaway strong { color: #b8860b; }

/* Info box */
.info-box {
    background: #eef7f2;
    border: 1px solid #a8d5b5;
    border-radius: 10px;
    padding: 14px 18px;
    margin-top: 12px;
    font-size: 0.9rem;
    color: #0d3b2e;
}

/* Section Divider */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: #1a1a2e;
    margin: 32px 0 16px 0;
    padding-bottom: 8px;
    border-bottom: 2px solid #c8ddd0;
}

/* Progress indicator */
.progress-bar {
    background: #e0dbd0;
    border-radius: 10px;
    height: 6px;
    margin-bottom: 32px;
    overflow: hidden;
}
.progress-fill {
    background: linear-gradient(90deg, #155740, #1a7a55);
    height: 100%;
    width: 25%;
    border-radius: 10px;
}
.progress-label {
    font-size: 0.78rem;
    color: #888;
    margin-bottom: 6px;
    letter-spacing: 0.5px;
}

/* Table styling */
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}
th {
    background-color: #155740;
    color: white;
    padding: 10px 14px;
    text-align: left;
}
td {
    padding: 9px 14px;
    border-bottom: 1px solid #e0e0e0;
    color: #3a3a4a;
}
tr:nth-child(even) td { background-color: #f5faf7; }

/* Sidebar styling */
section[data-testid="stSidebar"] { background-color: #0d3b2e; }
section[data-testid="stSidebar"] * { color: #c8ddd0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">📗 Module 2 of 8</div>
    <h1>Microeconomics</h1>
    <p>Understand how markets work, how prices are set, and how firms and consumers make decisions — the building blocks of financial analysis.</p>
</div>
""", unsafe_allow_html=True)

# ─── Progress Bar ────────────────────────────────────────────────────────────
st.markdown("""
<div class="progress-label">SYLLABUS PROGRESS — MODULE 2 / 8</div>
<div class="progress-bar"><div class="progress-fill"></div></div>
""", unsafe_allow_html=True)

# ─── Sidebar Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📗 Module 2 Topics")
    st.markdown("""
- 2.1 Demand & Supply
- 2.2 Market Equilibrium
- 2.3 Elasticity
- 2.4 Consumer Theory
- 2.5 Production & Costs
- 2.6 Market Structures
- 2.7 Factor Markets
""")
    st.markdown("---")
    st.markdown("### 📚 All Modules")
    st.markdown("""
- ✅ Module 1 – Foundations
- ✅ **Module 2** – Microeconomics *(current)*
- ⬜ Module 3 – Macroeconomics
- ⬜ Module 4 – Money & Banking
- ⬜ Module 5 – Monetary & Fiscal Policy
- ⬜ Module 6 – International Economics
- ⬜ Module 7 – Financial Economics
- ⬜ Module 8 – Contemporary Issues
""")

# ─── Topics ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📖 Topic Summaries</div>', unsafe_allow_html=True)

# ── 2.1 Demand & Supply
with st.expander("📌 2.1 — Demand & Supply: Laws, Curves & Shifts", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>2.1 Demand & Supply</h3>
        <p>
        The <b>Law of Demand</b> states that as price rises, quantity demanded falls (inverse relationship), 
        assuming all other factors remain constant (<i>ceteris paribus</i>). The <b>Law of Supply</b> states 
        that as price rises, producers are willing to supply more (direct relationship).<br><br>
        <b>Shifts in Demand</b> are caused by changes in income, tastes, prices of related goods, expectations, 
        or population. <b>Shifts in Supply</b> are driven by input costs, technology, taxes/subsidies, or 
        number of producers. Understanding what causes shifts vs. movements along a curve is a critical 
        distinction — movements are caused by price changes only.
        </p>
        <div class="key-terms">
            <span class="term-pill">Law of Demand</span>
            <span class="term-pill">Law of Supply</span>
            <span class="term-pill">Ceteris Paribus</span>
            <span class="term-pill">Demand Curve</span>
            <span class="term-pill">Supply Curve</span>
            <span class="term-pill">Shift vs Movement</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Commodity price forecasting relies heavily on demand-supply dynamics. A supply shock (e.g. oil disruption) shifts the supply curve left — pushing prices up, impacting inflation and energy stocks.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 2.2 Market Equilibrium
with st.expander("📌 2.2 — Market Equilibrium & Price Mechanism", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>2.2 Market Equilibrium & Price Mechanism</h3>
        <p>
        <b>Market Equilibrium</b> occurs where quantity demanded equals quantity supplied — the market-clearing 
        price. At prices above equilibrium, there is a <b>surplus</b> (excess supply), which pushes prices 
        down. Below equilibrium, there is a <b>shortage</b> (excess demand), which pushes prices up.<br><br>
        The <b>Price Mechanism</b> acts as a signalling system: rising prices signal producers to supply more 
        and consumers to cut back. It allocates resources without central planning. Government interventions 
        like <b>price ceilings</b> (maximum price) and <b>price floors</b> (minimum price) distort this 
        mechanism and create inefficiencies.
        </p>
        <div class="key-terms">
            <span class="term-pill">Equilibrium Price</span>
            <span class="term-pill">Surplus</span>
            <span class="term-pill">Shortage</span>
            <span class="term-pill">Price Mechanism</span>
            <span class="term-pill">Price Ceiling</span>
            <span class="term-pill">Price Floor</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Financial markets constantly seek equilibrium. Bond yields adjust until supply of bonds meets demand. Stock prices reflect the equilibrium between buyers and sellers at any given moment.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 2.3 Elasticity
with st.expander("📌 2.3 — Elasticity: Price, Income & Cross Elasticity", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>2.3 Elasticity</h3>
        <p>
        <b>Price Elasticity of Demand (PED)</b> measures how sensitive quantity demanded is to a price change. 
        If PED > 1, demand is <b>elastic</b> (luxury goods, many substitutes). If PED < 1, demand is 
        <b>inelastic</b> (essentials like fuel, medicine). Firms use this to set pricing strategy — 
        inelastic goods can sustain price increases without significant volume loss.<br><br>
        <b>Income Elasticity of Demand (YED)</b> measures response to income changes. Normal goods have 
        positive YED; inferior goods have negative YED. <b>Cross Elasticity of Demand (XED)</b> measures 
        how demand for one good responds to price changes in another — positive for substitutes, negative 
        for complements.
        </p>
        <div class="key-terms">
            <span class="term-pill">PED</span>
            <span class="term-pill">YED</span>
            <span class="term-pill">XED</span>
            <span class="term-pill">Elastic</span>
            <span class="term-pill">Inelastic</span>
            <span class="term-pill">Substitutes</span>
            <span class="term-pill">Complements</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Companies with inelastic demand (pharma, utilities, tobacco) have stronger pricing power and more predictable revenues — making them defensive investments in downturns.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📊 Elasticity Quick Reference")
    st.markdown("""
| Type | Formula | Value | Interpretation |
|------|---------|-------|----------------|
| PED | % ΔQd / % ΔP | > 1 | Elastic — sensitive to price |
| PED | % ΔQd / % ΔP | < 1 | Inelastic — not sensitive |
| YED | % ΔQd / % ΔY | Positive | Normal good |
| YED | % ΔQd / % ΔY | Negative | Inferior good |
| XED | % ΔQd(A) / % ΔP(B) | Positive | Substitutes |
| XED | % ΔQd(A) / % ΔP(B) | Negative | Complements |
""")

# ── 2.4 Consumer Theory
with st.expander("📌 2.4 — Consumer Theory: Utility & Indifference Curves", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>2.4 Consumer Theory</h3>
        <p>
        <b>Utility</b> refers to the satisfaction a consumer derives from consuming goods or services. 
        The <b>Law of Diminishing Marginal Utility</b> states that each additional unit consumed gives 
        less additional satisfaction than the previous one — explaining why demand curves slope downward.<br><br>
        <b>Indifference Curves</b> show all combinations of two goods that give a consumer equal satisfaction. 
        They are downward sloping and convex to the origin. The <b>Budget Line</b> represents the combinations 
        affordable given income and prices. A consumer maximises utility where the indifference curve is 
        <b>tangent</b> to the budget line. Changes in income shift the budget line; changes in price rotate it.
        </p>
        <div class="key-terms">
            <span class="term-pill">Utility</span>
            <span class="term-pill">Marginal Utility</span>
            <span class="term-pill">Indifference Curve</span>
            <span class="term-pill">Budget Line</span>
            <span class="term-pill">Consumer Equilibrium</span>
            <span class="term-pill">Diminishing Returns</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Utility theory underpins modern portfolio theory — investors are assumed to maximise utility (returns) subject to a budget constraint (risk tolerance). Indifference curves map risk-return preferences.</div>
    </div>
    """, unsafe_allow_html=True)

# ── 2.5 Production & Costs
with st.expander("📌 2.5 — Production & Costs: Short Run vs Long Run", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>2.5 Production & Costs</h3>
        <p>
        In the <b>Short Run</b>, at least one input (usually capital) is fixed. The <b>Law of Diminishing 
        Returns</b> applies — adding more variable inputs (labour) to fixed capital eventually yields 
        smaller additions to output. Key cost concepts include: <b>Fixed Costs (FC)</b> — don't change 
        with output; <b>Variable Costs (VC)</b> — change with output; <b>Total Cost (TC) = FC + VC</b>.<br><br>
        In the <b>Long Run</b>, all inputs are variable. Firms experience <b>Economies of Scale</b> 
        (falling average costs as output rises) or <b>Diseconomies of Scale</b> (rising average costs). 
        The <b>Long Run Average Cost (LRAC)</b> curve is U-shaped and forms the envelope of all short-run 
        average cost curves.
        </p>
        <div class="key-terms">
            <span class="term-pill">Fixed Cost</span>
            <span class="term-pill">Variable Cost</span>
            <span class="term-pill">Marginal Cost</span>
            <span class="term-pill">Economies of Scale</span>
            <span class="term-pill">LRAC</span>
            <span class="term-pill">Diminishing Returns</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Cost structure analysis is central to equity research. A high fixed-cost business (airlines, steel) has high operating leverage — profits are volatile. Low fixed-cost businesses (software) scale profitably.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📊 Cost Summary Table")
    st.markdown("""
| Cost Type | Definition | Short Run? |
|-----------|-----------|------------|
| Fixed Cost (FC) | Does not change with output | Yes |
| Variable Cost (VC) | Changes with output | Yes |
| Total Cost (TC) | FC + VC | Yes |
| Average Total Cost (ATC) | TC / Output | Yes |
| Marginal Cost (MC) | Change in TC per extra unit | Yes |
| Long Run Average Cost (LRAC) | All inputs variable | No (Long Run) |
""")

# ── 2.6 Market Structures
with st.expander("📌 2.6 — Market Structures: Competition to Monopoly", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>2.6 Market Structures</h3>
        <p>
        Market structure describes the competitive environment in which firms operate. The four main types are:<br><br>
        <b>Perfect Competition:</b> Many sellers, identical products, free entry/exit, price takers. 
        Long-run profit = zero (abnormal profits attract new entrants).<br><br>
        <b>Monopolistic Competition:</b> Many firms, differentiated products, some pricing power. 
        Examples: restaurants, clothing brands.<br><br>
        <b>Oligopoly:</b> Few large firms dominate, interdependent decision-making, high barriers to entry. 
        Prone to collusion. Examples: telecom, airlines, banking.<br><br>
        <b>Monopoly:</b> Single seller, price maker, highest barriers to entry. Can earn sustained supernormal 
        profits but may lead to consumer welfare loss and regulatory scrutiny.
        </p>
        <div class="key-terms">
            <span class="term-pill">Perfect Competition</span>
            <span class="term-pill">Monopoly</span>
            <span class="term-pill">Oligopoly</span>
            <span class="term-pill">Monopolistic Competition</span>
            <span class="term-pill">Barriers to Entry</span>
            <span class="term-pill">Price Maker</span>
            <span class="term-pill">Price Taker</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Market structure determines a company's pricing power and long-run profitability — a key input in equity valuation. Monopolies and oligopolies (e.g. Google, Visa) generate durable supernormal returns (economic moats).</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📊 Market Structure Comparison")
    st.markdown("""
| Feature | Perfect Competition | Monopolistic | Oligopoly | Monopoly |
|---------|-------------------|--------------|-----------|---------|
| Number of firms | Many | Many | Few | One |
| Product type | Identical | Differentiated | Similar/Diff | Unique |
| Price control | None | Some | Some | High |
| Entry barriers | None | Low | High | Very High |
| Long-run profit | Zero | Zero | Possible | Sustained |
| Example | Wheat market | Restaurants | Telecom | Water utility |
""")

# ── 2.7 Factor Markets
with st.expander("📌 2.7 — Factor Markets: Labour, Capital & Land", expanded=False):
    st.markdown("""
    <div class="topic-card">
        <h3>2.7 Factor Markets</h3>
        <p>
        <b>Factor markets</b> are markets where the inputs to production are bought and sold. The four 
        factors of production are <b>Labour, Capital, Land,</b> and <b>Entrepreneurship</b>. Their 
        respective rewards are wages, interest, rent, and profit.<br><br>
        In the <b>Labour Market</b>, the demand for labour is a <b>derived demand</b> — firms hire 
        workers because of demand for their output. Wages are determined by supply and demand for labour. 
        The <b>Marginal Revenue Product (MRP)</b> of labour defines how much an employer is willing to pay 
        — a worker is hired as long as MRP ≥ wage.<br><br>
        <b>Capital Markets</b> allocate financial and physical capital — the interest rate acts as the 
        price of capital. <b>Land</b> is fixed in supply, so its price (rent) is demand-determined.
        </p>
        <div class="key-terms">
            <span class="term-pill">Derived Demand</span>
            <span class="term-pill">MRP</span>
            <span class="term-pill">Wage Rate</span>
            <span class="term-pill">Interest Rate</span>
            <span class="term-pill">Economic Rent</span>
            <span class="term-pill">Labour Market</span>
        </div>
        <div class="takeaway">💡 <strong>Finance Lens:</strong> Labour cost is a key driver of corporate margins. Rising wages (tight labour markets) compress profits. Interest rates — the price of capital — directly affect the cost of debt, discount rates, and asset valuations.</div>
    </div>
    """, unsafe_allow_html=True)

# ─── Interactive: Market Structure Identifier ────────────────────────────────
st.markdown('<div class="section-title">🔍 Market Structure Identifier</div>', unsafe_allow_html=True)
st.markdown("Answer a few questions to identify the market structure of any industry:")

col1, col2 = st.columns(2)
with col1:
    num_firms = st.selectbox("How many firms are in the market?", ["Select...", "One", "Few (2–10)", "Many"])
    product_type = st.selectbox("Product type?", ["Select...", "Identical", "Differentiated", "Unique"])
with col2:
    entry_barriers = st.selectbox("Barriers to entry?", ["Select...", "None / Low", "High", "Very High / Blocked"])
    pricing_power = st.selectbox("Pricing power?", ["Select...", "None (price taker)", "Some", "High (price maker)"])

if st.button("🔎 Identify Market Structure"):
    if "Select..." in [num_firms, product_type, entry_barriers, pricing_power]:
        st.warning("⚠️ Please answer all questions first.")
    elif num_firms == "One":
        st.success("🏢 **Monopoly** — Single seller with high pricing power and blocked entry. Examples: utilities, patented drugs.")
    elif num_firms == "Few (2–10)" and entry_barriers == "High":
        st.success("🏭 **Oligopoly** — Few dominant firms with significant interdependence. Examples: telecom, banking, airlines.")
    elif num_firms == "Many" and product_type == "Differentiated":
        st.success("🛍️ **Monopolistic Competition** — Many firms, differentiated products, low barriers. Examples: restaurants, fashion.")
    elif num_firms == "Many" and product_type == "Identical":
        st.success("⚖️ **Perfect Competition** — Many firms, identical products, no pricing power. Examples: wheat, foreign exchange.")
    else:
        st.info("🤔 The combination suggests a mixed or transitional market structure — possibly oligopolistic with product differentiation.")

# ─── Quick Revision Quiz ─────────────────────────────────────────────────────
st.markdown('<div class="section-title">🧠 Quick Revision Check</div>', unsafe_allow_html=True)

q1 = st.radio(
    "1. If the price of coffee rises and demand for tea increases, what is the relationship between coffee and tea?",
    ["Complements", "Substitutes", "Inferior goods", "Independent goods"],
    index=None, key="m2q1"
)
if q1 == "Substitutes":
    st.success("✅ Correct! Substitutes have a positive cross elasticity of demand — when price of one rises, demand for the other increases.")
elif q1:
    st.error("❌ Substitutes have positive XED. When coffee price rises, consumers switch to tea — showing they are substitutes.")

q2 = st.radio(
    "2. A software company has near-zero marginal cost of serving an extra customer. What does this imply about its cost structure?",
    ["High variable costs", "High fixed costs, low variable costs", "Diseconomies of scale", "Inelastic supply"],
    index=None, key="m2q2"
)
if q2 == "High fixed costs, low variable costs":
    st.success("✅ Correct! Software has high upfront (fixed) development costs but near-zero marginal (variable) cost — leading to massive scalability and operating leverage.")
elif q2:
    st.error("❌ Software firms have high fixed costs (R&D, development) but almost zero variable costs per additional user — the key to their scalability.")

q3 = st.radio(
    "3. Which market structure best describes the global smartphone duopoly of Apple and Samsung?",
    ["Perfect Competition", "Monopoly", "Oligopoly", "Monopolistic Competition"],
    index=None, key="m2q3"
)
if q3 == "Oligopoly":
    st.success("✅ Correct! A few dominant firms, high barriers to entry (brand, technology, scale), and interdependent strategic decisions — classic oligopoly.")
elif q3:
    st.error("❌ Apple and Samsung dominate the premium segment with few rivals, high entry barriers, and strategic interdependence — that's an oligopoly.")

q4 = st.radio(
    "4. A pharmaceutical company raises the price of a life-saving drug by 30% and sales fall by only 3%. Demand is:",
    ["Elastic", "Inelastic", "Unit Elastic", "Perfectly Elastic"],
    index=None, key="m2q4"
)
if q4 == "Inelastic":
    st.success("✅ Correct! PED = 3%/30% = 0.1 — much less than 1, meaning demand is highly inelastic. Life-saving drugs have no close substitutes.")
elif q4:
    st.error("❌ PED = %ΔQd / %ΔP = 3/30 = 0.1 — well below 1, so demand is inelastic. This is typical of essential medicines.")

# ─── Module Navigation ───────────────────────────────────────────────────────
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown("⬅️ **Previous: Module 1 — Foundations**")
with col2:
    st.markdown("<div style='text-align:center; color:#888; font-size:0.85rem;'>Module 2 of 8 — Microeconomics</div>", unsafe_allow_html=True)
with col3:
    st.markdown("➡️ **Next: Module 3 — Macroeconomics**")