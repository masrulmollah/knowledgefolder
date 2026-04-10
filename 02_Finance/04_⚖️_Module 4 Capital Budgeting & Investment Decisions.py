import streamlit as st
import pandas as pd

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 4 · Capital Budgeting", page_icon="💼", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;700&family=Outfit:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
.hero { background: linear-gradient(135deg, #240046 0%, #3c096c 50%, #5a189a 100%);
    border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '💼'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.15); color: #c77dff; font-size: 12px;
    letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Cormorant Garamond', serif; color: #fff; font-size: 42px; margin: 0 0 12px 0; }
.hero p { color: #c77dff; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #e9d8fd; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #5a189a; }
.card h3 { font-family: 'Cormorant Garamond', serif; color: #240046; font-size: 18px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 14px; line-height: 1.7; margin: 0; }
.formula-box { background: #f3e8ff; border-radius: 8px; padding: 14px 18px; font-family: 'Courier New', monospace; font-size: 14px; color: #3c096c; margin: 10px 0; font-weight: 600; }
.insight { background: #faf5ff; border-left: 4px solid #9f7aea; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #553c9a; font-size: 14px; margin: 0; line-height: 1.6; }
.sh { font-family: 'Cormorant Garamond', serif; color: #240046; font-size: 24px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #e9d8fd; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #e9d8fd; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#240046,#9f7aea); border-radius: 10px; height: 6px; width: 33%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 4 of 12</div>
<h1>Capital Budgeting & Investment Decisions</h1>
<p>Learn the analytical tools that drive the most consequential decisions a company makes — where to invest capital for the long term.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#6b46c1;margin-bottom:4px;"><span>Course progress</span><span>Module 4 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📖 Core Concepts", "🔢 Key Methods", "📊 NPV / IRR Calculator", "✅ Quiz"])

with tab1:
    st.markdown('<div class="sh">Capital Budgeting Fundamentals</div>', unsafe_allow_html=True)
    concepts = [
        ("Capital Budgeting", "The process of evaluating and selecting long-term investments (projects, assets, acquisitions) that are expected to generate returns over multiple years. It is the most important financial decision because it commits large sums for extended periods."),
        ("Relevant Cash Flows", "Only incremental, after-tax cash flows are relevant. Sunk costs (already spent) are irrelevant. Opportunity costs (foregone returns) must be included. Working capital changes and terminal salvage values are often overlooked but are important."),
        ("Net Present Value (NPV)", "The gold standard method. NPV = PV of all future cash inflows − Initial Investment. If NPV > 0, the project creates shareholder value and should be accepted. NPV directly measures value created in absolute terms."),
        ("Internal Rate of Return (IRR)", "The discount rate at which NPV = 0. If IRR > Required Rate of Return (hurdle rate / WACC), accept the project. IRR is a relative measure (%) and popular in practice for its intuitive appeal."),
        ("Payback Period", "The time it takes to recover the initial investment from cash flows. Simple and easy to understand. Ignores the time value of money and cash flows after payback. Used as a quick screening tool, not the primary criterion."),
        ("Modified IRR (MIRR)", "Addresses the reinvestment rate problem in IRR by assuming cash inflows are reinvested at the WACC rather than at the IRR itself. More realistic than traditional IRR."),
        ("Capital Rationing", "When capital is limited and not all positive-NPV projects can be funded, projects must be ranked using the Profitability Index (PI = NPV / Initial Investment). Select projects in descending PI order until the budget is exhausted."),
    ]
    for t, b in concepts:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">Comparison of Methods</div>', unsafe_allow_html=True)
    df = pd.DataFrame([
        ["NPV", "PV of CFs − Investment", "NPV > 0 → Accept", "Best method; measures absolute value created", "Requires WACC estimate; less intuitive to non-finance"],
        ["IRR", "Rate where NPV = 0", "IRR > Hurdle Rate", "Intuitive % return; popular with management", "Multiple IRRs possible; ignores scale; reinvestment assumption"],
        ["Payback Period", "Years to recover investment", "PP < Threshold", "Simple; measures liquidity risk", "Ignores TVM; ignores post-payback flows"],
        ["Discounted Payback", "Years using PV of CFs", "DPP < Threshold", "Improvements over payback", "Still ignores post-payback flows"],
        ["Profitability Index", "NPV / Initial Investment", "PI > 1.0", "Useful for capital rationing", "Can conflict with NPV in mutually exclusive choices"],
        ["MIRR", "Modified reinvestment rate", "MIRR > Hurdle Rate", "Solves reinvestment assumption flaw of IRR", "Less well-known than IRR"],
    ], columns=["Method", "Formula / Definition", "Decision Rule", "Strengths", "Weaknesses"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown('<div class="insight"><p><strong>Rule of thumb:</strong> Always use NPV as the primary decision criterion. Use IRR as a supplementary check. Use Payback for liquidity screening. When projects are mutually exclusive, always defer to NPV, not IRR, in case of conflict.</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="sh">NPV & IRR Calculator</div>', unsafe_allow_html=True)
    st.markdown("Enter the project's initial investment and up to 8 years of cash flows.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        initial_inv = st.number_input("Initial Investment (₹)", value=1000000.0, step=50000.0)
        wacc = st.slider("Required Return / WACC (%)", 5, 30, 12)
        n_years = st.slider("Project Life (years)", 1, 8, 5)
    with col2:
        cfs = []
        for y in range(1, n_years + 1):
            default = [300000, 350000, 400000, 380000, 350000, 320000, 300000, 280000]
            cf = st.number_input(f"Year {y} Cash Flow (₹)", value=float(default[y-1]), step=10000.0, key=f"cf_{y}")
            cfs.append(cf)
    
    r = wacc / 100
    npv = -initial_inv + sum(cf / (1+r)**t for t, cf in enumerate(cfs, 1))
    
    # IRR via bisection
    def calc_npv(rate, inv, flows):
        return -inv + sum(f/(1+rate)**t for t, f in enumerate(flows, 1))
    
    lo, hi = 0.0001, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if calc_npv(mid, initial_inv, cfs) > 0:
            lo = mid
        else:
            hi = mid
    irr = mid * 100
    
    pi = (initial_inv + npv) / initial_inv
    
    cum = 0
    payback = None
    for t, cf in enumerate(cfs, 1):
        cum += cf
        if cum >= initial_inv and payback is None:
            payback = t - 1 + (initial_inv - (cum - cf)) / cf
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("NPV", f"₹{npv:,.0f}", delta="✅ Accept" if npv > 0 else "❌ Reject")
    col2.metric("IRR", f"{irr:.2f}%", delta="vs WACC " + ("✅" if irr > wacc else "❌"))
    col3.metric("Profitability Index", f"{pi:.3f}", delta="✅" if pi > 1 else "❌")
    col4.metric("Payback Period", f"{payback:.1f} yrs" if payback else ">project life")
    
    # Cash flow table
    rows = []
    cumulative_npv = -initial_inv
    for t, cf in enumerate(cfs, 1):
        pv_cf = cf / (1 + r) ** t
        cumulative_npv += pv_cf
        rows.append({"Year": t, "Cash Flow (₹)": f"₹{cf:,.0f}", "PV Factor": f"{1/(1+r)**t:.4f}", "PV of CF (₹)": f"₹{pv_cf:,.0f}", "Cumulative NPV (₹)": f"₹{cumulative_npv:,.0f}"})
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 4</div>', unsafe_allow_html=True)
    qs = [
        {"q": "A project has NPV = ₹50,000 and Initial Investment = ₹2,00,000. What is the Profitability Index?",
         "options": ["0.25", "1.25", "4.00", "0.80"], "answer": "1.25",
         "exp": "PI = (NPV + Initial Investment) / Initial Investment = (50,000 + 2,00,000) / 2,00,000 = 2,50,000 / 2,00,000 = 1.25."},
        {"q": "When NPV and IRR give conflicting rankings for mutually exclusive projects, you should rely on:",
         "options": ["IRR", "NPV", "Payback Period", "MIRR"], "answer": "NPV",
         "exp": "NPV is always the correct criterion for mutually exclusive projects. It measures absolute value created. IRR can be misleading when projects have different scales or cash flow timing patterns."},
        {"q": "The IRR method assumes that intermediate cash flows are reinvested at:",
         "options": ["The WACC", "The risk-free rate", "The IRR itself", "Zero"], "answer": "The IRR itself",
         "exp": "The standard IRR method implicitly assumes reinvestment of intermediate cash flows at the IRR — which is often unrealistic. MIRR corrects this by using WACC as the reinvestment rate."},
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q4_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">📚 Knowledge Folder · Finance Series · Module 4 of 12 &nbsp;|&nbsp; Next: <strong>Module 5 — Cost of Capital & Capital Structure</strong></div>', unsafe_allow_html=True)