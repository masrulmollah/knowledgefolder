import streamlit as st

# NO st.set_page_config() here - already called in Homepage


def sidebar():
    with st.sidebar:
        st.markdown("### Customs Act — All Modules")
        items = [
            ("1", "Introduction"), ("2", "Key Definitions"), ("3", "Powers & Duties"),
            ("4", "Ports & Stations"), ("5", "Prohibition & Restriction"), ("6", "Customs Valuation"),
            ("7", "Assessment & Duties"), ("8", "Import & Export Procedure"),
            ("9", "Conveyances & Passengers"), ("10", "Offences & Penalties"),
            ("11", "Agents & Business Records"), ("12", "Customs Act 2023"),
        ]
        for num, title in items:
            if num == "12":
                st.markdown(
                    f"<div style='background:#2e6da4;color:white;border-radius:6px;"
                    f"padding:3px 8px;margin-bottom:3px;'>✅ M{num}. {title}</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(f"✅ M{num}. {title}")
        st.success("All 12 modules complete!")


def hero():
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#1a3c5e,#2e6da4);
                    padding:2.2rem 2rem;border-radius:12px;margin-bottom:1.2rem;">
          <h1 style="color:#FFD700;font-size:1.9rem;margin:0;">
            🛃 Customs Act of Bangladesh
          </h1>
          <h2 style="color:#fff;font-size:1.2rem;margin:.4rem 0 0;font-weight:400;">
            Module 12 · Customs Act 2023 — New Provisions &amp; Final Review
          </h2>
          <p style="color:#cce0f5;margin:.5rem 0 0;font-size:.9rem;">
            e-Declaration · Risk Management · PCA · Advance Ruling · Allied Acts · Full Summary
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="background:#e8f4fd;border-radius:8px;padding:.6rem 1.2rem;
                    margin-bottom:1.2rem;border-left:4px solid #FFD700;">
          <b>Progress:</b> Module 12 of 12 &nbsp;|&nbsp;
          <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛</span>
          &nbsp; <b style="color:#27ae60;">100% Complete!</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.success("You have reached the final module! Complete this to finish the full syllabus.")


def section_new_provisions():
    st.subheader("New Provisions — Customs Act 2023")
    st.markdown(
        "The 2023 Act introduces modernising features aligned with WCO and WTO standards:"
    )

    provisions = [
        (
            "💻", "Electronic Declaration",
            "All customs declarations may be filed electronically. ASYCUDA World is the official "
            "system. Paper-based declarations are being phased out.",
            "Digital audit trails become the norm — ensure electronic records are properly archived.",
        ),
        (
            "🎯", "Risk Management System",
            "Formal risk-based examination using intelligence and selectivity criteria. "
            "Replaces routine examination with targeted inspection.",
            "Low-risk importers get faster clearance — maintaining good compliance history "
            "reduces examination rates.",
        ),
        (
            "🔍", "Non-Intrusive Inspection (NII)",
            "Use of scanning technology (X-ray scanners) to examine cargo without physically "
            "opening containers.",
            "Faster clearance for legitimate cargo; reduces demurrage and storage costs.",
        ),
        (
            "📊", "Post Clearance Audit (PCA)",
            "Formal audit of customs transactions after goods have been released. Customs can "
            "review records for up to 5 years.",
            "Clearance is not the end of customs compliance — maintain all records for PCA readiness.",
        ),
        (
            "📋", "Advance Ruling",
            "Importers / exporters can obtain binding rulings on HS classification, origin, and "
            "valuation BEFORE importing.",
            "Advance rulings eliminate cost uncertainty — use before importing new products.",
        ),
        (
            "ℹ️", "National Enquiry Point",
            "A dedicated centre for trade information — provides transparency on customs procedures, "
            "tariffs, and requirements.",
            "Use the National Enquiry Point for official clarifications before challenging Customs decisions.",
        ),
        (
            "✈️", "Advanced Passenger Information (API)",
            "Airlines must transmit passenger data to Customs before arrival for risk assessment "
            "and security screening.",
            "Affects travel compliance — relevant for companies with frequent international travellers.",
        ),
        (
            "🌐", "WCO / WTO Standards Alignment",
            "Formally incorporates WCO Revised Kyoto Convention, WCO SAFE Framework, and WTO TFA.",
            "Bangladesh's customs now aligns with global best practices — reduces trade friction "
            "with WCO member countries.",
        ),
    ]

    for icon, title, desc, tip in provisions:
        with st.expander(f"{icon} {title}", expanded=False):
            c1, c2 = st.columns([3, 2])
            with c1:
                st.markdown(desc)
            with c2:
                st.info(f"💼 **Finance Lens:** {tip}")


def section_comparison():
    with st.expander("Customs Act 1969 vs 2023 — Key Differences", expanded=False):
        st.markdown(
            """
| Feature | Customs Act 1969 | Customs Act 2023 |
|---------|-----------------|-----------------|
| Total Sections | 286 | 269 |
| Filing Method | Paper-based (primary) | Electronic (primary) |
| Examination | Routine / random | Risk-based |
| Post Clearance Audit | Limited | Formal PCA system |
| Advance Ruling | Not available | Formally available |
| International Standards | Partial | Full WCO / WTO alignment |
| Scanning / NII | Not specified | Formally recognised |
| Passenger Data | Not specified | Advanced Passenger Information |
| National Enquiry Point | Not specified | Formally established |
            """
        )


def section_allied():
    with st.expander("Allied Acts — Quick Reference", expanded=False):
        allied = [
            ("Imports and Exports Control Act, 1950",
             "Controls which goods can be imported / exported; basis for Import Policy Order"),
            ("Foreign Exchange Regulation Act (FERA), 1947",
             "Controls foreign currency; export proceeds repatriation within 4 months"),
            ("Import Policy Order 2021–2024",
             "Classifies goods as freely importable, restricted, or prohibited"),
            ("Export Policy 2024–2027",
             "Sets rules for export of goods from Bangladesh"),
            ("Arms Act, 1878",
             "Controls import of arms and ammunition"),
            ("Narcotics Control Act, 1990",
             "Prohibits import / export of controlled substances"),
            ("Anti-Money Laundering Act, 2002",
             "Customs role in preventing trade-based money laundering"),
            ("Trademark Act, 2009",
             "Customs enforcement of trademark rights at borders"),
            ("Copyright Act, 2000",
             "Customs enforcement of copyright at borders"),
            ("Patent and Design Act, 1911",
             "Customs enforcement of design patents"),
            ("Merchant Shipping Act, 1923",
             "Governs vessels and shipping operations"),
            ("Post Office Act, 1898",
             "Rules for goods imported / exported via postal services"),
        ]
        c1, c2 = st.columns(2)
        for i, (act, purpose) in enumerate(allied):
            col = c1 if i % 2 == 0 else c2
            col.markdown(
                f"<div style='background:#f0f7ff;border-radius:6px;padding:.55rem .8rem;"
                f"margin-bottom:5px;border-left:3px solid #2e6da4;'>"
                f"<b style='font-size:.86rem;color:#1a3c5e;'>{act}</b>"
                f"<div style='font-size:.79rem;color:#555;margin-top:.15rem;'>{purpose}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )


def section_summary():
    st.markdown("---")
    st.subheader("Complete Course Summary — All 12 Modules")

    rows = [
        ("1",  "Introduction",              "History, NBR, Vision/Mission, Functions, Stakeholders, Licensing"),
        ("2",  "Key Definitions",           "Section 2: Agent, Bill of Entry, Goods, Smuggle, Customs Area, Person-in-Charge"),
        ("3",  "Powers & Duties",           "Sections 4, 6, 19, 20: Officer powers, Delegation, Exemptions"),
        ("4",  "Ports & Stations",          "Sections 9, 10: Customs ports, airports, land stations, landing places"),
        ("5",  "Prohibition & Restriction", "Sections 15, 16, 17: Prohibited goods, restricted goods, export restrictions"),
        ("6",  "Customs Valuation",         "Section 25: 6 valuation methods, CIF basis, Tariff Value, Minimum Value"),
        ("7",  "Assessment & Duties",       "Sections 18, 30, 80–83C: CD, RD, SD, VAT, AT, AIT — full tax chain"),
        ("8",  "Import & Export Procedure", "Sections 43, 53, 79, 131: Step-by-step clearance, documents, warehousing"),
        ("9",  "Conveyances & Passengers",  "Sections 103, 135, 136: Baggage rules, transhipment, transit"),
        ("10", "Offences & Penalties",      "Sections 32, 156, 173–177: Misdeclaration, smuggling, search, appeals"),
        ("11", "Agents & Business Records", "Sections 207, 208, 211: C&F licensing, record-keeping requirements"),
        ("12", "Customs Act 2023",          "e-Declaration, NII, PCA, Advance Ruling, API, WCO/WTO alignment, Allied Acts"),
    ]

    for num, title, coverage in rows:
        st.markdown(
            f"<div style='display:flex;margin-bottom:5px;'>"
            f"<div style='background:#2e6da4;color:white;border-radius:50%;width:27px;"
            f"height:27px;display:flex;align-items:center;justify-content:center;"
            f"font-weight:700;flex-shrink:0;margin-right:9px;font-size:.83rem;'>{num}</div>"
            f"<div style='background:#f8f9fa;border-radius:6px;padding:.5rem .9rem;flex:1;'>"
            f"<b style='color:#1a3c5e;'>{title}</b>"
            f"<span style='font-size:.82rem;color:#555;'> — {coverage}</span>"
            f"</div></div>",
            unsafe_allow_html=True,
        )


def section_final_quiz():
    st.markdown("---")
    st.subheader("🏆 Final Review Quiz — Mixed Questions from All Modules")

    questions = [
        {
            "q": "Which Section covers the licensing of C&F Agents?",
            "opts": ["Section 4", "Section 79", "Section 207", "Section 211"],
            "ans": "Section 207",
            "exp": "Section 207 — Licensing of customs agents.",
        },
        {
            "q": "Post Clearance Audit (PCA) is empowered under which Section?",
            "opts": ["Section 80", "Section 83C", "Section 156", "Section 211"],
            "ans": "Section 83C",
            "exp": "Section 83C empowers Customs to conduct Post Clearance Audits.",
        },
        {
            "q": "Bangladesh uses which basis for customs valuation?",
            "opts": ["FOB", "CIF", "CFR", "EXW"],
            "ans": "CIF",
            "exp": "Bangladesh uses CIF (Cost + Insurance + Freight) as the customs value basis.",
        },
        {
            "q": "The Customs Act 2023 has how many sections?",
            "opts": ["286", "300", "269", "250"],
            "ans": "269",
            "exp": "The 2023 Act has 269 sections, reduced from 286 in the 1969 Act.",
        },
        {
            "q": "Which new provision gives a binding decision on HS classification before importing?",
            "opts": ["Post Clearance Audit", "Advance Ruling",
                     "National Enquiry Point", "Risk Management"],
            "ans": "Advance Ruling",
            "exp": "Advance Ruling provides binding decisions on classification, origin, and valuation before importation.",
        },
        {
            "q": "Supplementary Duty (SD) is calculated on which base?",
            "opts": ["Assessable Value only", "AV + CD", "AV + CD + RD", "AV + CD + RD + SD"],
            "ans": "AV + CD + RD",
            "exp": "SD is calculated on Assessable Value plus Customs Duty plus Regulatory Duty.",
        },
    ]

    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['q']}**")
        sel = st.radio("", q["opts"], key=f"m12_q{i}", index=None, label_visibility="collapsed")
        answers.append((sel, q["ans"], q["exp"]))

    if st.button("🏆 Submit Final Quiz", type="primary"):
        score = sum(1 for a, c, _ in answers if a == c)
        total = len(questions)
        pct = score / total * 100

        if pct == 100:
            st.balloons()
            st.markdown(
                f"<div style='background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;"
                f"border-radius:12px;padding:1.4rem;text-align:center;'>"
                f"<h2 style='color:white;margin:0;'>Perfect Score! {score}/{total}</h2>"
                f"<p style='margin:.4rem 0 0;'>Outstanding — you have mastered the Customs Act of Bangladesh!</p>"
                f"</div>",
                unsafe_allow_html=True,
            )
        elif pct >= 70:
            st.markdown(
                f"<div style='background:#2980b9;color:white;border-radius:12px;"
                f"padding:1.4rem;text-align:center;'>"
                f"<h2 style='color:white;margin:0;'>Good Score: {score}/{total} ({pct:.0f}%)</h2>"
                f"<p style='margin:.4rem 0 0;'>Well done! Review the questions you missed.</p>"
                f"</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div style='background:#e67e22;color:white;border-radius:12px;"
                f"padding:1.4rem;text-align:center;'>"
                f"<h2 style='color:white;margin:0;'>Keep Studying: {score}/{total} ({pct:.0f}%)</h2>"
                f"<p style='margin:.4rem 0 0;'>Review the modules where you made errors and try again!</p>"
                f"</div>",
                unsafe_allow_html=True,
            )

        st.markdown("### Answer Review:")
        for i, (sel, correct, exp) in enumerate(answers):
            if sel == correct:
                st.success(f"✅ Q{i + 1}: Correct! — {exp}")
            elif sel is None:
                st.warning(f"⚠️ Q{i + 1}: Not answered. Correct: **{correct}** — {exp}")
            else:
                st.error(f"❌ Q{i + 1}: You chose **{sel}**. Correct: **{correct}** — {exp}")


def section_takeaways():
    st.markdown("---")
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#1a3c5e,#2e6da4);color:white;
                    border-radius:12px;padding:1.4rem 1.8rem;">
          <h3 style="color:#FFD700;margin-top:0;">Top 10 Finance Professional Takeaways</h3>
          <ol style="color:#cce0f5;line-height:2.0;">
            <li>The Customs Act 2023 replaces 1969 — align compliance procedures with the new Act.</li>
            <li>Bangladesh uses <b>CIF basis</b> for customs valuation — always include freight &amp; insurance.</li>
            <li>Import duties are <b>cascading</b> — effective rates can be 50–80%+ for high-duty goods.</li>
            <li>HS Code classification determines every aspect of import duty — get it right.</li>
            <li>Post Clearance Audit (PCA) means clearance does not end liability — keep records for 5 years.</li>
            <li>Advance Ruling eliminates uncertainty — use it before importing new products.</li>
            <li>AIT and AT paid at import are <b>adjustable</b> against annual income tax — don't lose these credits.</li>
            <li>Misdeclaration (Section 32) extends to <b>electronic filings</b> — ASYCUDA data has full legal weight.</li>
            <li>Section 19 SRO exemptions are time-bound and conditional — verify before applying.</li>
            <li>C&amp;F Agents are co-liable for declarations — choose agents with strong compliance records.</li>
          </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )


def completion_banner():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;
                    border-radius:12px;padding:1.4rem;text-align:center;">
          <h2 style="color:white;margin:0;">Congratulations!</h2>
          <p style="margin:.4rem 0 0;font-size:1rem;">
            You have completed all 12 modules of the Customs Act of Bangladesh.
          </p>
          <p style="margin:.2rem 0 0;font-size:.88rem;opacity:.9;">
            Knowledge Folder · Customs Act Series
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def nav_footer():
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, _ = st.columns([1, 2, 1])
    with c1:
        st.markdown(
            "<span style='background:#6c757d;color:white;padding:.4rem 1rem;"
            "border-radius:6px;font-size:.9rem;'>← Module 11: Agents &amp; Records</span>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;color:#888;font-size:.85rem;'>"
            "Module 12 of 12 · Customs Act of Bangladesh · Complete!</div>",
            unsafe_allow_html=True,
        )


# ── Main ───────────────────────────────────────────────────────────────────────
sidebar()
hero()
section_new_provisions()
section_comparison()
section_allied()
section_summary()
section_final_quiz()
section_takeaways()
completion_banner()
nav_footer()