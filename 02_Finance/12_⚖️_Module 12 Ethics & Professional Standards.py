import streamlit as st

# FIX: Wrapped in try-except to handle multipage application execution
try:
    st.set_page_config(page_title="Module 12 · Ethics & Professional Standards", page_icon="⚖️", layout="wide")
except st.errors.StreamlitAPIException:
    pass

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Crimson+Pro:wght@300;400;600&display=swap');
html, body, [class*=\"css\"] { font-family: 'Crimson Pro', serif; }
.hero { background: linear-gradient(135deg, #1a1a1a 0%, #2d3748 50%, #4a5568 100%); border-radius: 16px; padding: 48px 40px; margin-bottom: 28px; position: relative; overflow: hidden; }
.hero::before { content: '⚖️'; font-size: 180px; position: absolute; right: 30px; top: -20px; opacity: 0.07; }
.hero-tag { background: rgba(255,255,255,0.12); color: #edf2f7; font-size: 12px; letter-spacing: 3px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 16px; }
.hero h1 { font-family: 'Cinzel', serif; color: #fff; font-size: 38px; margin: 0 0 12px 0; line-height: 1.2; }
.hero p { color: #cbd5e0; font-size: 16px; margin: 0; max-width: 600px; line-height: 1.7; }
.card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 22px; margin-bottom: 14px; border-left: 5px solid #2d3748; }
.card h3 { font-family: 'Cinzel', serif; color: #1a202c; font-size: 15px; margin: 0 0 8px; }
.card p { color: #4a5568; font-size: 15px; line-height: 1.7; margin: 0; }
.insight { background: #f7fafc; border-left: 4px solid #4a5568; border-radius: 0 10px 10px 0; padding: 14px 18px; margin: 12px 0; }
.insight p { color: #2d3748; font-size: 15px; margin: 0; line-height: 1.6; }
.sh { font-family: 'Cinzel', serif; color: #1a202c; font-size: 22px; margin: 28px 0 14px; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0; }
.qok { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 10px; padding: 14px; color: #276749; margin-top: 8px; }
.qerr { background: #fff5f5; border: 1px solid #feb2b2; border-radius: 10px; padding: 14px; color: #9b2c2c; margin-top: 8px; }
.pb { background: #e2e8f0; border-radius: 10px; height: 6px; margin: 6px 0 24px; }
.pbi { background: linear-gradient(90deg,#1a202c,#4a5568); border-radius: 10px; height: 6px; width: 100%; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><div class="hero-tag">Module 12 of 12</div>
<h1>Ethics & Professional Standards</h1>
<p>The moral compass of the financial industry. Integrity, objectivity, and the duty of care to clients and the public interest.</p></div>
<div><div style="display:flex;justify-content:space-between;font-size:12px;color:#2d3748;margin-bottom:4px;"><span>Course progress</span><span>Module 12 / 12</span></div>
<div class="pb"><div class="pbi"></div></div></div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🏛️ Code of Ethics", "🛡️ Standards of Conduct", "⚠️ Ethical Dilemmas", "✅ Final Quiz"])

with tab1:
    st.markdown('<div class="sh">The Code of Ethics</div>', unsafe_allow_html=True)
    ethics = [
        ("Integrity", "Act with integrity, competence, diligence, and respect in an ethical manner with the public, clients, prospective clients, employers, and colleagues."),
        ("Professionalism", "Place the integrity of the investment profession and the interests of clients above personal interests."),
        ("Duty of Care", "Use reasonable care and exercise independent professional judgment when conducting investment analysis and making investment recommendations."),
        ("Public Interest", "Practice and encourage others to practice in a professional and ethical manner that will reflect credit on themselves and the profession."),
        ("Global Capital Markets", "Promote the integrity and viability of the global capital markets for the ultimate benefit of society."),
    ]
    for t, b in ethics:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="sh">Standards of Professional Conduct</div>', unsafe_allow_html=True)
    standards = [
        ("Professionalism", "Knowledge of the Law, Independence and Objectivity, Misrepresentation, and Misconduct. Professionals must comply with the stricter of applicable law or the ethical standards."),
        ("Integrity of Capital Markets", "Material Nonpublic Information and Market Manipulation. Avoid trading on 'insider' info and do not artificially distort market prices or volume."),
        ("Duties to Clients", "Loyalty, Prudence, and Care. Fair Dealing, Suitability, Performance Presentation, and Preservation of Confidentiality."),
        ("Duties to Employers", "Loyalty, Additional Compensation Arrangements, and Responsibilities of Supervisors. Avoid conflict of interest and do not cause harm to your employer."),
        ("Investment Analysis", "Diligence and Reasonable Basis, Communication with Clients, and Record Retention. Thorough research is required before any recommendation."),
        ("Conflicts of Interest", "Disclosure of Conflicts, Priority of Transactions, and Referral Fees. Always put client interests first and disclose any potential bias."),
    ]
    for t, b in standards:
        st.markdown(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="sh">Ethical Dilemmas in Finance</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="insight">
        <p><strong>Scenario: The IPO Allocation</strong><br>
        A broker-dealer receives an oversubscribed IPO. They are tempted to allocate more shares to their biggest clients or to friends. 
        <strong>Ethical Standard:</strong> Fair Dealing. All clients must be treated fairly, regardless of their size or personal relationship to the firm.</p>
    </div>
    <div class="insight">
        <p><strong>Scenario: The Research Report</strong><br>
        An analyst is pressured by their firm's investment banking arm to issue a 'Buy' rating on a company they are trying to win as a client. 
        <strong>Ethical Standard:</strong> Independence and Objectivity. The analyst must remain unbiased and not allow external pressures to influence their research findings.</p>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="sh">Knowledge Check — Module 12</div>', unsafe_allow_html=True)
    qs = [
        {"q": "If an investment professional is subject to two sets of rules (e.g., local law and CFA ethics) that conflict, they must:",
         "options": ["Follow local law only", "Follow the CFA ethics only", "Follow the stricter of the two", "Choose the one that is most practical"],
         "answer": "Follow the stricter of the two",
         "exp": "The standard of Professionalism requires following the stricter law or regulation to ensure the highest ethical conduct is maintained."},
        {"q": "Which of the following constitutes 'Material Nonpublic Information'?",
         "options": ["A company's quarterly earnings reported on their website", "A casual conversation about a company's general industry trend", "Information about a pending merger that has not been announced", "A published analyst report with a 'Sell' rating"],
         "answer": "Information about a pending merger that has not been announced",
         "exp": "Material information is anything that would likely affect the price of a security. Nonpublic means it has not been broadly disseminated to the market. Trading on this is a violation of market integrity."},
        {"q": "The duty of 'Loyalty, Prudence, and Care' means a professional must act:",
         "options": ["In their own best interest", "In their employer's best interest", "In the client's best interest", "In the market's best interest"],
         "answer": "In the client's best interest",
         "exp": "Fiduciary duty or duty of care requires that the client's interests are always placed above those of the firm or the individual professional."},
    ]
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"q12_{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == q["answer"]:
                st.markdown(f'<div class="qok">✅ Correct! {q["exp"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="qerr">❌ Incorrect. Correct: <strong>{q["answer"]}</strong><br>{q["exp"]}</div>', unsafe_allow_html=True)
        st.markdown("---")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#a0aec0;font-size:13px;padding:16px 0;">🎉 <strong>Course Complete!</strong> You have finished all 12 modules of the Finance Series. &nbsp;|&nbsp; 📚 Knowledge Folder</div>', unsafe_allow_html=True)