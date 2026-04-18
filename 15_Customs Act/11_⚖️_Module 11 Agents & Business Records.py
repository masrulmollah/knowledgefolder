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
            if num == "11":
                st.markdown(
                    f"<div style='background:#2e6da4;color:white;border-radius:6px;"
                    f"padding:3px 8px;margin-bottom:3px;'>✅ M{num}. {title}</div>",
                    unsafe_allow_html=True,
                )
            else:
                done = "✅" if int(num) < 11 else "⬜"
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
            Module 11 · Agents &amp; Business Records
          </h2>
          <p style="color:#cce0f5;margin:.5rem 0 0;font-size:.9rem;">
            Sections 207, 208, 211 · C&amp;F Agent Licensing · Record-Keeping Requirements
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="background:#e8f4fd;border-radius:8px;padding:.6rem 1.2rem;
                    margin-bottom:1.2rem;border-left:4px solid #2e6da4;">
          <b>Progress:</b> Module 11 of 12 &nbsp;|&nbsp;
          <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜</span>
          &nbsp; 92% Complete
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_sec207():
    with st.expander("Section 207 — Licensing of Customs Agents", expanded=True):
        st.markdown(
            """
No person shall act as a customs Agent unless **licensed under Section 207**.

**Agent types requiring licences:**

| Agent Type | Primary Role |
|-----------|-------------|
| **Clearing & Forwarding (C&F) Agent** | Files Bill of Entry / Export; handles physical clearance |
| **Shipping Agent** | Represents the vessel / carrier at port |
| **Cargo Agent** | Handles air cargo clearance and forwarding |
| **Freight Forwarding Agent** | Arranges transport, logistics, and documentation |

**Licence Requirements:**
- Application to the Commissioner of Customs
- Security deposit
- Fit and proper person criteria
- Office and infrastructure requirements
- Annual renewal

**Licence Conditions:**
- Must maintain proper records
- Cannot act where a conflict of interest exists
- Must file declarations accurately on behalf of clients
- Equally responsible for accuracy of declarations filed
            """
        )
        st.warning(
            "An agent filing a false declaration is **equally liable** as the importer / exporter — "
            "even if acting on client instructions."
        )


def section_sec208():
    with st.expander("Section 208 — Persons Permitted to Transact Business", expanded=False):
        st.markdown(
            """
The Commissioner of Customs may **permit** certain persons to transact customs business
without being fully licensed under Section 207.

**When used:**
- Company employees clearing goods for their own employer
- One-time or infrequent importers
- Situations where full licensing is impractical

**Key Differences:**

| Feature | Section 207 (Licensed Agent) | Section 208 (Permitted Person) |
|---------|------------------------------|-------------------------------|
| Nature | Commercial licence | Specific permission |
| Continuity | Ongoing licence | Transaction-specific |
| Goods handled | Clients' goods | Own / employer's goods |
| Security deposit | Required | Generally not required |

💼 **Finance Lens:** Large companies often have in-house customs teams operating under
Section 208 permission rather than engaging a full C&F agent for every transaction.
            """
        )


def section_sec211():
    with st.expander("Section 211 — Business Books & Records", expanded=False):
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
**Who must maintain records?**
- All importers and exporters
- Customs agents (C&F, Shipping, Cargo)
- Warehouse operators
- Any person involved in customs transactions

**What records must be kept?**
- Commercial Invoice & Packing List
- Bill of Lading / Airway Bill
- Bill of Entry / Bill of Export
- Duty payment challans
- LC documents
- Certificate of Origin
- Customs examination reports
- SRO / exemption certificates used
                """
            )
        with c2:
            st.markdown(
                """
**Retention Period:**
- Generally **5 years** from the date of transaction
- Longer if under audit, investigation, or dispute

**Form of Records:**
- Can be maintained in **electronic format**
  (Notification no. 129/2001/Customs)
- Must be accessible and readable on demand
- Must be produced when required by Customs

**Consequences of Non-Compliance:**
- Failure to produce records = offence under Section 156
- Fine up to BDT 25,000
- Post Clearance Audit (Section 83C) may review records
                """
            )
        st.info(
            "💼 **Finance Lens:** Customs record-keeping requirements overlap with VAT and Income Tax "
            "requirements. A unified document management system serves all three compliance areas."
        )


def section_comparison():
    st.markdown("---")
    st.subheader("🔍 Agent Type Comparison Tool")
    selected = st.multiselect(
        "Select agent types to compare:",
        ["C&F Agent", "Shipping Agent", "Cargo Agent", "Freight Forwarding Agent"],
        default=["C&F Agent", "Shipping Agent"],
    )

    data = {
        "C&F Agent": {
            "Full Name": "Clearing & Forwarding Agent",
            "Licensed Under": "Section 207",
            "Primary Function": "Files Bill of Entry / Export; handles customs clearance",
            "Represents": "Importer or Exporter",
            "Key Documents": "Bill of Entry, Bill of Export, Duty Challan",
            "Liability": "Co-liable for declarations filed",
        },
        "Shipping Agent": {
            "Full Name": "Shipping / Stevedoring Agent",
            "Licensed Under": "Section 207",
            "Primary Function": "Represents the vessel; files Import / Export Manifest",
            "Represents": "Vessel Owner / Shipping Line",
            "Key Documents": "Import Manifest, Export Manifest, Delivery Order",
            "Liability": "Liable for manifest accuracy and vessel compliance",
        },
        "Cargo Agent": {
            "Full Name": "Air Cargo / IATA Agent",
            "Licensed Under": "Section 207",
            "Primary Function": "Air cargo clearance and forwarding at airports",
            "Represents": "Airline / Air freight consignees",
            "Key Documents": "Airway Bill, Air Cargo Manifest, Import Declaration",
            "Liability": "Co-liable for air cargo declarations",
        },
        "Freight Forwarding Agent": {
            "Full Name": "Freight Forwarding Agent / NVOCC",
            "Licensed Under": "Section 207",
            "Primary Function": "Arranges multimodal transport; may issue House B/L",
            "Represents": "Cargo owners (consignors / consignees)",
            "Key Documents": "House Bill of Lading, FCR, Forwarder Certificate",
            "Liability": "Responsible for transport arrangement and documentation",
        },
    }

    attrs = ["Full Name", "Licensed Under", "Primary Function", "Represents",
             "Key Documents", "Liability"]

    if selected:
        cols = st.columns(len(selected))
        for col, agent in zip(cols, selected):
            col.markdown(
                f"<div style='background:#1a3c5e;color:white;border-radius:8px 8px 0 0;"
                f"padding:.6rem;text-align:center;font-weight:700;color:#FFD700;'>"
                f"{agent}</div>",
                unsafe_allow_html=True,
            )
            for attr in attrs:
                col.markdown(
                    f"<div style='background:#f8f9fa;border-bottom:1px solid #dee2e6;"
                    f"padding:.45rem .7rem;'>"
                    f"<div style='font-size:.73rem;color:#888;font-weight:600;'>{attr}</div>"
                    f"<div style='font-size:.86rem;color:#333;'>{data[agent][attr]}</div>"
                    f"</div>",
                    unsafe_allow_html=True,
                )


def section_checklist():
    st.markdown("---")
    st.subheader("✅ Records Retention Compliance Checklist (Section 211)")

    records = [
        "Commercial Invoice (original) — 5 years",
        "Bill of Lading / Airway Bill (original) — 5 years",
        "Bill of Entry (signed copy) — 5 years",
        "Duty Payment Challan — 5 years",
        "Letter of Credit documents — 5 years",
        "Certificate of Origin — 5 years",
        "Customs examination reports — 5 years",
        "Import / Export Register — 5 years",
        "C&F Agent correspondence — 5 years",
        "SRO / Exemption certificates used — 7 years",
    ]

    checked = [r for r in records if st.checkbox(r, key=f"rec_{r}")]
    missing = [r for r in records if r not in checked]
    pct = len(checked) / len(records) * 100

    if pct == 100:
        st.success("All required records are being maintained.")
    elif pct >= 70:
        st.warning(f"{len(missing)} record type(s) still need attention.")
    else:
        st.error(
            f"{len(missing)} record types are not maintained. "
            "Risk of Section 156 penalty in a Post Clearance Audit."
        )


def section_quiz():
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 11")

    questions = [
        {
            "q": "Under which Section must Clearing & Forwarding Agents be licensed?",
            "opts": ["Section 207", "Section 208", "Section 211", "Section 156"],
            "ans": "Section 207",
            "exp": "Section 207 covers the licensing of all customs agents including C&F agents.",
        },
        {
            "q": "How long must customs-related business records generally be retained?",
            "opts": ["1 year", "3 years", "5 years", "10 years"],
            "ans": "5 years",
            "exp": "Section 211 records must generally be maintained for 5 years from the transaction date.",
        },
        {
            "q": "Section 208 permits which type of person to transact customs business?",
            "opts": [
                "Any member of the public",
                "Licensed customs brokers only",
                "Persons specifically permitted (e.g. employees for own employer's goods)",
                "Foreign nationals only",
            ],
            "ans": "Persons specifically permitted (e.g. employees for own employer's goods)",
            "exp": "Section 208 permits specific persons — not commercially licensed agents — in limited circumstances.",
        },
    ]

    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['q']}**")
        sel = st.radio("", q["opts"], key=f"m11_q{i}", index=None, label_visibility="collapsed")
        answers.append((sel, q["ans"], q["exp"]))

    if st.button("✅ Submit Answers — Module 11", type="primary"):
        score = sum(1 for a, c, _ in answers if a == c)
        st.markdown(f"### Score: {score}/{len(questions)}")
        for i, (sel, correct, exp) in enumerate(answers):
            if sel == correct:
                st.success(f"✅ Q{i + 1}: Correct! — {exp}")
            elif sel is None:
                st.warning(f"⚠️ Q{i + 1}: Not answered. Correct: **{correct}** — {exp}")
            else:
                st.error(f"❌ Q{i + 1}: You chose **{sel}**. Correct: **{correct}** — {exp}")


def nav_footer():
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        st.markdown(
            "<span style='background:#6c757d;color:white;padding:.4rem 1rem;"
            "border-radius:6px;font-size:.9rem;'>← Module 10: Offences</span>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;color:#888;font-size:.85rem;'>"
            "Module 11 of 12 · Customs Act of Bangladesh</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            "<div style='text-align:right;'><span style='background:#2e6da4;color:white;"
            "padding:.4rem 1rem;border-radius:6px;font-size:.9rem;'>"
            "Next → Module 12: Customs Act 2023</span></div>",
            unsafe_allow_html=True,
        )


# ── Main ───────────────────────────────────────────────────────────────────────
sidebar()
hero()
section_sec207()
section_sec208()
section_sec211()
section_comparison()
section_checklist()
section_quiz()
nav_footer()