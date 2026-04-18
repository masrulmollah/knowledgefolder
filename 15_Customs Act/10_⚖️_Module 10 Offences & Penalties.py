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
            if num == "10":
                st.markdown(
                    f"<div style='background:#2e6da4;color:white;border-radius:6px;"
                    f"padding:3px 8px;margin-bottom:3px;'>✅ M{num}. {title}</div>",
                    unsafe_allow_html=True,
                )
            else:
                done = "✅" if int(num) < 10 else "⬜"
                st.markdown(f"{done} M{num}. {title}")


def hero():
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#1a3c5e,#2e6da4);
                    padding:2.2rem 2rem;border-radius:12px;margin-bottom:1.2rem;">
          <h1 style="color:#FFD700;font-size:1.9rem;margin:0;">
            🛃 Customs Act of Bangladesh
          </h1>
          <h2 style="color:#fff;font-size:1.2rem;margin:.4rem 0 0;font-weight:400;">
            Module 10 · Offences &amp; Penalties
          </h2>
          <p style="color:#cce0f5;margin:.5rem 0 0;font-size:.9rem;">
            Sections 32, 156, 173–177 · Misdeclaration · Smuggling · Search &amp; Seizure · Appeals
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="background:#e8f4fd;border-radius:8px;padding:.6rem 1.2rem;
                    margin-bottom:1.2rem;border-left:4px solid #2e6da4;">
          <b>Progress:</b> Module 10 of 12 &nbsp;|&nbsp;
          <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜</span>
          &nbsp; 83% Complete
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_sec32():
    with st.expander("Section 32 — Untrue Statements & Misdeclaration", expanded=True):
        st.error("Misdeclaration in customs is a serious criminal offence under Section 32.")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
**Three ways to commit this offence:**

1. **False Documents** — Making, signing, or delivering to a Customs officer any
declaration, notice, certificate, or document that is untrue in any material particular.

2. **False Statements** — Making any statement in answer to a question by a
Customs officer which is untrue.

3. **Electronic Misdeclaration** — Transmitting any statement, document, or information
through an electronic device that is false.
                """
            )
        with c2:
            st.markdown(
                """
**Consequence:**
Where, by reason of such documents, statements, or **collusion**, any duty is
evaded — the person is guilty of an offence.

**Common forms of misdeclaration:**
- Under-valuing goods (invoice manipulation)
- Wrong HS Code declaration
- False country-of-origin declaration
- Wrong quantity declaration
- False description of goods
                """
            )
        st.info(
            "💼 **Finance Lens:** Transfer pricing and intercompany import transactions "
            "are the highest-risk area for valuation misdeclaration. "
            "Maintain arm's-length documentation."
        )


def section_sec156():
    with st.expander("Section 156 — Schedule of Offences & Penalties", expanded=False):
        offences = [
            ("Smuggling (Section 2n)",
             "Confiscation of goods + Fine up to 5× value + Up to 7 years imprisonment",
             "#c0392b", "Severe"),
            ("Misdeclaration of value or quantity",
             "Fine up to 3× the evaded duty + Confiscation (discretionary)",
             "#c0392b", "Severe"),
            ("False HS Code declaration",
             "Fine + Possible confiscation",
             "#e67e22", "High"),
            ("Unauthorised removal from customs area",
             "Fine up to BDT 50,000 + Confiscation",
             "#e67e22", "High"),
            ("Failure to produce documents on demand",
             "Fine up to BDT 10,000",
             "#f39c12", "Moderate"),
            ("Obstruction of a Customs Officer",
             "Fine + Possible arrest",
             "#e67e22", "High"),
            ("Unlicensed C&F agent operations",
             "Fine + Licence suspension / cancellation",
             "#f39c12", "Moderate"),
            ("Failure to maintain records (Sec 211)",
             "Fine up to BDT 25,000",
             "#f39c12", "Moderate"),
        ]
        for offence, penalty, colour, level in offences:
            st.markdown(
                f"<div style='background:#fdf8f8;border-left:4px solid {colour};"
                f"border-radius:6px;padding:.7rem 1rem;margin-bottom:5px;'>"
                f"<b style='color:#1a3c5e;'>{offence}</b>"
                f"<div style='font-size:.86rem;color:#444;margin-top:.2rem;'>"
                f"Penalty: {penalty}</div>"
                f"<div style='font-size:.79rem;color:{colour};margin-top:.15rem;'>"
                f"Severity: {level}</div></div>",
                unsafe_allow_html=True,
            )


def section_enforcement():
    with st.expander("Sections 173–177 — Search, Seizure & Enforcement Powers", expanded=False):
        st.markdown(
            """
| Section | Power |
|---------|-------|
| **173** | Procedure for High Court Division applications for release of detained packages |
| **174** | Power to require production of order permitting clearance of goods imported / exported by land |
| **175** | Power to prevent making or transmission of certain signals or messages |
| **176** | Power to station customs officers in certain factories |
| **177** | Restriction on possession of goods in certain areas |

**General Search & Seizure:**
- Customs officers may search persons, conveyances, and premises with or without warrant
- Goods suspected of smuggling may be seized pending investigation
- Seized goods are inventoried and held in customs custody

**Arrest Powers:**
- Customs officers can arrest persons suspected of serious customs offences
- Arrested person must be produced before magistrate within 24 hours
            """
        )


def section_appeals():
    with st.expander("Appeals Process — Representation to Supreme Court", expanded=False):
        steps = [
            ("1", "Internal Representation",
             "Written representation to the assessing officer requesting review of assessment.",
             "#2980b9"),
            ("2", "Commissioner (Appeals)",
             "Appeal to the Commissioner of Customs (Appeals) — file within 30 days of assessment notice.",
             "#8e44ad"),
            ("3", "Customs Excise & VAT Appellate Tribunal",
             "Second level — more formal tribunal proceedings.",
             "#e67e22"),
            ("4", "High Court Division",
             "Legal questions; Section 173 covers applications for release of detained goods.",
             "#c0392b"),
            ("5", "Appellate Division (Supreme Court)",
             "Final appeal on substantial questions of law.",
             "#1a3c5e"),
        ]
        for num, title, desc, colour in steps:
            st.markdown(
                f"<div style='display:flex;margin-bottom:7px;'>"
                f"<div style='background:{colour};color:white;border-radius:6px;"
                f"padding:.25rem .55rem;font-weight:700;font-size:.85rem;"
                f"flex-shrink:0;margin-right:10px;margin-top:2px;'>{num}</div>"
                f"<div style='background:#f8f9fa;border-radius:6px;padding:.6rem 1rem;"
                f"flex:1;border-left:3px solid {colour};'>"
                f"<b>{title}</b>"
                f"<div style='font-size:.85rem;color:#555;margin-top:.2rem;'>{desc}</div>"
                f"</div></div>",
                unsafe_allow_html=True,
            )


def section_scenarios():
    st.markdown("---")
    st.subheader("Compliance Risk Scenarios — Identify the Offence")

    scenarios = [
        (
            "An importer declares fabric as 'raw material' (5% CD) when it is actually finished garments (25% CD).",
            ["Value misdeclaration", "HS Code / description misdeclaration",
             "Quantity misdeclaration", "No offence"],
            "HS Code / description misdeclaration",
            "Declaring finished garments as raw material is a false description — HS Code misdeclaration.",
        ),
        (
            "An invoice shows USD 10,000 for machinery, but the actual transaction was USD 25,000.",
            ["HS Code misdeclaration", "Value misdeclaration / under-invoicing",
             "Unauthorised removal", "No offence"],
            "Value misdeclaration / under-invoicing",
            "Declaring a lower value than the actual price evades duty — value misdeclaration.",
        ),
        (
            "A truck removes imported goods from the customs area before the Out-Pass is issued.",
            ["Value misdeclaration", "Smuggling / unauthorised removal",
             "False document", "No offence"],
            "Smuggling / unauthorised removal",
            "Removing goods from customs area without clearance is unauthorised removal — may be treated as smuggling.",
        ),
        (
            "A C&F agent provides a backdated certificate to claim an expired duty exemption.",
            ["False document (Section 32)", "Value misdeclaration",
             "Unauthorised removal", "No offence"],
            "False document (Section 32)",
            "Providing a false or backdated document to claim exemption is an offence under Section 32.",
        ),
    ]

    for i, (scenario, opts, correct, exp) in enumerate(scenarios):
        st.markdown(f"**Scenario {i + 1}:** _{scenario}_")
        sel = st.radio("Identify the offence:", opts,
                       key=f"m10_scen{i}", index=None, label_visibility="collapsed")
        if sel:
            if sel == correct:
                st.success(f"Correct! — {exp}")
            else:
                st.error(f"Incorrect. Correct: **{correct}** — {exp}")
        st.markdown("")


def section_quiz():
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 10")

    questions = [
        {
            "q": "Section 32 covers which type of offence?",
            "opts": ["Smuggling of goods", "Untrue statement / misdeclaration",
                     "Failure to pay duty", "Unauthorised warehousing"],
            "ans": "Untrue statement / misdeclaration",
            "exp": "Section 32 specifically covers untrue statements and misdeclaration in customs declarations.",
        },
        {
            "q": "Electronic misdeclaration via ASYCUDA is:",
            "opts": ["Not covered by customs law", "Covered under Section 32",
                     "Only a civil matter", "Exempt if unintentional"],
            "ans": "Covered under Section 32",
            "exp": "Section 32 explicitly includes electronic transmission of false information.",
        },
        {
            "q": "The first step in the customs appeals process is typically:",
            "opts": ["Filing at High Court", "Going to the Appellate Tribunal",
                     "Representation to the assessing officer", "Filing with Supreme Court"],
            "ans": "Representation to the assessing officer",
            "exp": "Appeals begin internally with a representation to the assessing officer.",
        },
    ]

    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['q']}**")
        sel = st.radio("", q["opts"], key=f"m10_q{i}", index=None, label_visibility="collapsed")
        answers.append((sel, q["ans"], q["exp"]))

    if st.button("✅ Submit Answers — Module 10", type="primary"):
        score = sum(1 for a, c, _ in answers if a == c)
        st.markdown(f"### Score: {score}/{len(questions)}")
        for i, (sel, correct, exp) in enumerate(answers):
            if sel == correct:
                st.success(f"✅ Q{i + 1}: Correct! — {exp}")
            elif sel is None:
                st.warning(f"⚠️ Q{i + 1}: Not answered. Correct: **{correct}** — {exp}")
            else:
                st.error(f"❌ Q{i + 1}: You chose **{sel}**. Correct: **{correct}** — {exp}")


def takeaways():
    st.markdown("---")
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#e8f4fd,#f0fff4);border-radius:10px;
                    padding:1.2rem 1.5rem;border-left:5px solid #2e6da4;">
          <h4 style="color:#1a3c5e;margin-top:0;">💡 Finance Professional Takeaways</h4>
          <ul style="margin:0;color:#333;">
            <li>Transfer pricing / related-party imports are the highest risk area for valuation misdeclaration.</li>
            <li>Electronic declarations in ASYCUDA carry the same legal weight as physical documents.</li>
            <li>Contemporaneous documentation helps distinguish good-faith errors from deliberate misdeclaration.</li>
            <li>Always resolve customs disputes at the lowest level possible — High Court proceedings are slow and expensive.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def nav_footer():
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        st.markdown(
            "<span style='background:#6c757d;color:white;padding:.4rem 1rem;"
            "border-radius:6px;font-size:.9rem;'>← Module 9: Conveyances</span>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;color:#888;font-size:.85rem;'>"
            "Module 10 of 12 · Customs Act of Bangladesh</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            "<div style='text-align:right;'><span style='background:#2e6da4;color:white;"
            "padding:.4rem 1rem;border-radius:6px;font-size:.9rem;'>"
            "Next → Module 11: Agents &amp; Records</span></div>",
            unsafe_allow_html=True,
        )


# ── Main ───────────────────────────────────────────────────────────────────────
sidebar()
hero()
section_sec32()
section_sec156()
section_enforcement()
section_appeals()
section_scenarios()
section_quiz()
takeaways()
nav_footer()