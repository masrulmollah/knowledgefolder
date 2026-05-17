import streamlit as st

st.title("Income Tax Section: Syllabus Overview")
st.write("This page provides a complete overview of the Income Tax syllabus, with chapter summaries for every module in the Income Tax section.")

st.markdown("---")

st.header("How to Use This Overview")
st.markdown(
    "- Review the summary bullets for each chapter to understand the topic covered.\n"
    "- Use this page as a navigation guide to explore the full chapter files in the Income Tax section.\n"
    "- The chapter numbers correspond to the Income Tax module file order."
)

st.markdown("---")

chapters = [
    ("01. Tax Administration", "National Board of Revenue (NBR) hierarchy, tribunal process, powers of officers, alternative dispute resolution, and administrative procedure."),
    ("02. Definitions", "Key Income Tax definitions: assessee, assessment year, company, income, resident, and the foundational terms that determine scope and liability."),
    ("03. Tax Rates", "Individual slab rates, corporate rates, dividend withholding, capital gains rates, and key rate structures for residents and non-residents."),
    ("04. Surcharge & Minimum Tax", "Wealth surcharge for high-net-worth individuals, minimum tax on gross receipts for companies and individuals, and TDS-minimum tax interactions."),
    ("05. Income From Employment", "Salary income, allowances, perquisites, retirement income, and valuation rules for employment-related benefits."),
    ("06. Income from Financial Assets", "Interest, dividends, bonds, savings certificates, Islamic finance income, deductions, exemptions, and grossing-up of net receipts."),
    ("07. Income from Rent", "Annual value computation, statutory deductions, municipal taxes, loan interest, vacancy allowance, and taxable rent estimation."),
    ("08. Income from Agriculture", "Scope of agricultural income, deductible costs, statutory 60% deduction rule, and agricultural income calculation guidance."),
    ("09. Income from Business", "Business income scope, allowable expenses, inadmissible expenses, depreciation treatment, and profit calculation logic."),
    ("10. Capital Gains", "Capital asset definitions, gain computation, cost base, exemptions, and capital gains tax estimation for assets and shares."),
    ("11. Income from Other Sources", "Residual income head, dividends, interest, royalties, lottery prizes, deemed income, deductions, and net income estimation."),
    ("12. Depreciation and Amortization", "Tax depreciation rules, Third Schedule rates, amortization of intangibles, pre-commencement expenses, and written down value calculation."),
    ("13. Set off and carry forward of losses", "Rules for intra-head and inter-head loss set-off, carry forward of business losses, ring-fenced speculation and capital losses."),
    ("14. Exemption, Allowances & Tax Holiday", "Tax holiday provisions, exempt income heads, investment rebates, allowances, and special concession regimes for targeted sectors."),
    ("15. Deduction or Collection of Tax at Source", "TDS fundamentals, common withholding rates, deductor compliance, monthly return filing, and TDS certificate procedures."),
    ("16. Advance Payment of Tax", "Advance tax liability thresholds, installment deadlines, calculation logic, and installment estimation for taxpayers."),
    ("17. Return of Income", "Filing eligibility, tax day deadlines, universal self-assessment, filing extensions, and penalties for delayed returns."),
    ("18. Assessment", "Assessment procedures, self-assessment, best judgement assessment, special assessment types, and statutory time limits."),
    ("19. Assessment of Individuals", "Individual assessment rules, exemption thresholds, salary exemptions, investment rebates, surcharge, minimum tax, and tax estimation."),
    ("20. Assessment of Partnership Firms", "Taxation of partnership firms, registered vs unregistered status, disallowed partner payments, and firm tax computation."),
    ("21. Assessment of Companies", "Corporate assessment, tax rates, compliance, audited accounts, CSR tax rebates, minimum tax, and corporate tax estimation."),
    ("22. Assessment Special Cases & Non-Residents", "Representative assessees, non-resident agents, deceased/departing persons, discontinued business cases, and special timing rules."),
    ("23. Tax Avoidance", "General anti-avoidance rules, non-resident transactions, asset transfer anti-avoidance, securities/bond-washing prevention, and GAAR principles."),
    ("24. Power of Income Tax Authorities", "Civil court powers for tax officers, inspection and survey authority, search and seizure rules, retention of seized material."),
    ("25. Penalty", "Penalty provisions for late filing/payment, concealment of income, documentation defaults, audit violations, and penalty estimation."),
    ("26. Recovery of Tax", "Tax recovery mechanisms, notice of demand, garnishee orders, tax recovery officer powers, stay orders, and installment arrangements."),
    ("27. Double Tax Relief", "DTAA framework, unilateral relief, credit and exemption methods, and cross-border tax credit calculations."),
    ("28. Transfer Pricing", "Transfer pricing concepts, arm's length pricing methods, documentation requirements, compliance thresholds, and TP penalties."),
    ("29. Refunds", "Refund entitlement, claim process, set-off against arrears, delayed refund interest, and refund rights for taxpayers."),
    ("30. Appeals", "Appeal procedures, first appeal, tribunal appeal, High Court reference, revision, and fast-track ADR dispute resolution.")
]

for title, summary in chapters:
    with st.expander(title, expanded=False):
        st.write(summary)

st.markdown("---")
st.header("Income Tax Syllabus at a Glance")
row1, row2 = st.columns(2)
with row1:
    st.markdown("**Foundations & Rate Structure**")
    st.write("01. Tax Administration")
    st.write("02. Definitions")
    st.write("03. Tax Rates")
    st.write("04. Surcharge & Minimum Tax")
    st.write("05. Income From Employment")
    st.write("06. Income from Financial Assets")
    st.write("07. Income from Rent")
    st.write("08. Income from Agriculture")
    st.write("09. Income from Business")
    st.write("10. Capital Gains")
with row2:
    st.markdown("**Adjustments, Compliance & Litigation**")
    st.write("11. Income from Other Sources")
    st.write("12. Depreciation and Amortization")
    st.write("13. Set off and carry forward of losses")
    st.write("14. Exemption, Allowances & Tax Holiday")
    st.write("15. Deduction or Collection of Tax at Source")
    st.write("16. Advance Payment of Tax")
    st.write("17. Return of Income")
    st.write("18. Assessment")
    st.write("19. Assessment of Individuals")
    st.write("20. Assessment of Partnership Firms")

st.markdown("---")
row3, row4 = st.columns(2)
with row3:
    st.markdown("**Corporate, Special Cases & Enforcement**")
    st.write("21. Assessment of Companies")
    st.write("22. Assessment Special Cases & Non-Residents")
    st.write("23. Tax Avoidance")
    st.write("24. Power of Income Tax Authorities")
    st.write("25. Penalty")
with row4:
    st.markdown("**Cross-Border, Recovery & Appeals**")
    st.write("26. Recovery of Tax")
    st.write("27. Double Tax Relief")
    st.write("28. Transfer Pricing")
    st.write("29. Refunds")
    st.write("30. Appeals")

st.markdown("---")
st.info("Use this syllabus overview to navigate the Income Tax section quickly and understand the purpose of each chapter before opening the full topic pages.")
