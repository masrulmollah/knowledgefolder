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
            if num == "7":
                st.markdown(
                    f"<div style='background:#2e6da4;color:white;border-radius:6px;"
                    f"padding:3px 8px;margin-bottom:3px;'>✅ M{num}. {title}</div>",
                    unsafe_allow_html=True,
                )
            else:
                done = "✅" if int(num) < 7 else "⬜"
                st.markdown(f"{done} M{num}. {title}")
        st.info("Use the Full Duty Calculator — the most practical tool in this module!")


def hero():
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#1a3c5e,#2e6da4);
                    padding:2.2rem 2rem;border-radius:12px;margin-bottom:1.2rem;">
          <h1 style="color:#FFD700;font-size:1.9rem;margin:0;">
            🛃 Customs Act of Bangladesh
          </h1>
          <h2 style="color:#fff;font-size:1.2rem;margin:.4rem 0 0;font-weight:400;">
            Module 7 · Assessment of Duties &amp; Taxes
          </h2>
          <p style="color:#cce0f5;margin:.5rem 0 0;font-size:.9rem;">
            Sections 18, 30, 30A, 31, 80–83C · CD · RD · SD · VAT · AT · AIT
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="background:#e8f4fd;border-radius:8px;padding:.6rem 1.2rem;
                    margin-bottom:1.2rem;border-left:4px solid #2e6da4;">
          <b>Progress:</b> Module 7 of 12 &nbsp;|&nbsp;
          <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜</span>
          &nbsp; 58% Complete
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_key_sections():
    with st.expander("📜 Key Sections — 18, 30, 30A, 31, 80–83C", expanded=True):
        rows = [
            ("Section 18", "Goods Dutiable",
             "All goods imported into Bangladesh are liable to customs duty at the rate in the First Schedule (Customs Tariff)."),
            ("Section 30", "Date for Determination of Duty & Value",
             "Rate of duty and value applicable is that in force on the **date the Bill of Entry is filed**."),
            ("Section 30A", "Exchange Rate",
             "Rate of exchange used is the **rate notified by NBR** — not the inter-bank market rate."),
            ("Section 31", "Goods Re-imported",
             "Re-imported goods may be exempt from or liable to duty depending on circumstances of original export."),
            ("Section 80", "Assessment Procedure",
             "Bill of Entry is examined; goods may be physically inspected; duty assessed by appropriate officer."),
            ("Section 81", "Examination of Goods",
             "Customs may physically examine goods before assessment — importer/C&F agent must be present."),
            ("Section 82", "Goods Not Cleared Within Time",
             "Goods not cleared, warehoused, or transhipped within the specified period may be auctioned."),
            ("Section 82A", "Goods Not Assessed After Bill of Entry",
             "If Customs does not assess within the specified period after Bill of Entry filing, specific procedures apply."),
            ("Section 83A", "Amendment of Assessment",
             "Assessment can be amended within prescribed time limits if errors are discovered."),
            ("Section 83B", "Time Limit for Amendment",
             "Amendments must be made within the time specified; beyond this, the assessment becomes final."),
            ("Section 83C", "Audit of Records (PCA)",
             "Customs has power to audit importer/exporter records — Post Clearance Audit."),
        ]
        for sec, title, desc in rows:
            st.markdown(f"**{sec} — {title}:** {desc}")


def section_tax_chain():
    st.markdown("---")
    st.subheader("🔗 The Import Tax Chain")
    st.markdown(
        "All import taxes are calculated **sequentially** — each builds on the one before it."
    )

    chain = [
        ("CD",  "Customs Duty",        "On Assessable Value (CIF)",          "#1a3c5e",
         "Primary revenue source; protects domestic industry"),
        ("RD",  "Regulatory Duty",     "On Assessable Value",                 "#c0392b",
         "Levied when CD rate is 25%; additional protection layer"),
        ("SD",  "Supplementary Duty",  "On (AV + CD + RD)",                   "#8e44ad",
         "On luxury, harmful, or protected goods; ranges 10%–500%"),
        ("VAT", "Value Added Tax",     "On (AV + CD + RD + SD)",              "#27ae60",
         "Standard 15%; most imports are subject to VAT"),
        ("AT",  "Advance Tax",         "On (AV + CD + RD + SD + VAT)",        "#e67e22",
         "3% advance payment; adjustable against income tax"),
        ("AIT", "Advance Income Tax",  "On Assessable Value",                 "#2980b9",
         "5% for commercial importers; adjustable against annual income tax"),
    ]

    for short, name, base, colour, note in chain:
        st.markdown(
            f"<div style='background:{colour};color:white;border-radius:8px;"
            f"padding:.7rem 1.2rem;margin-bottom:5px;'>"
            f"<b style='font-size:1.1rem;color:#FFD700;'>{short}</b>"
            f"<span style='margin-left:.5rem;font-weight:600;'>{name}</span>"
            f"<span style='font-size:.82rem;margin-left:.5rem;opacity:.9;'>Base: {base}</span>"
            f"<div style='font-size:.8rem;opacity:.85;margin-top:.2rem;'>{note}</div>"
            f"</div>",
            unsafe_allow_html=True,
        )


def section_rates():
    with st.expander("📊 Standard Customs Duty (CD) Rates — Bangladesh Tariff Structure", expanded=False):
        st.markdown(
            """
| CD Rate | Category |
|---------|----------|
| **0%**  | Essential goods, capital machinery, priority sector raw materials |
| **1%**  | Basic raw materials not produced locally |
| **5%**  | Intermediate raw materials |
| **10%** | Intermediate goods; some consumer items |
| **15%** | Finished goods (standard rate) |
| **25%** | Luxury / sensitive goods — also triggers Regulatory Duty |

**VAT:** Standard 15% on most imports.

**Regulatory Duty (RD):** Applies when CD = 25%; typically 3%–35%.

**Supplementary Duty (SD):** 10%–500% depending on goods.

> Always verify actual rates against the current **Bangladesh Customs Tariff (BCT)**
> for the relevant fiscal year.
            """
        )


def section_calculator():
    st.markdown("---")
    st.subheader("🧮 Full Import Duty Calculator")
    st.markdown("Enter the assessable value and applicable rates to compute all import taxes:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Goods & Value**")
        av = st.number_input("Assessable Value / CIF (BDT)", min_value=0.0,
                             value=1_000_000.0, step=10_000.0, format="%.0f")
        cd_rate = st.selectbox("Customs Duty (CD) Rate",
                               [0, 1, 5, 10, 15, 25], index=4,
                               format_func=lambda x: f"{x}%")
        rd_rate = st.number_input("Regulatory Duty (RD) Rate (%)",
                                  min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    with col2:
        st.markdown("**Other Taxes**")
        sd_rate = st.number_input("Supplementary Duty (SD) Rate (%)",
                                  min_value=0.0, max_value=500.0, value=0.0, step=5.0)
        vat_rate = st.number_input("VAT Rate (%)",
                                   min_value=0.0, max_value=100.0, value=15.0, step=1.0)
        at_rate = st.number_input("Advance Tax (AT) Rate (%)",
                                  min_value=0.0, max_value=20.0, value=3.0, step=0.5)
        ait_rate = st.number_input("Advance Income Tax (AIT) Rate (%)",
                                   min_value=0.0, max_value=10.0, value=5.0, step=0.5)

    if st.button("🧮 Calculate Total Duties", type="primary"):
        cd  = av * (cd_rate / 100)
        rd  = av * (rd_rate / 100)
        sd  = (av + cd + rd) * (sd_rate / 100)
        vat = (av + cd + rd + sd) * (vat_rate / 100)
        at  = (av + cd + rd + sd + vat) * (at_rate / 100)
        ait = av * (ait_rate / 100)
        total = cd + rd + sd + vat + at + ait
        landed = av + total
        eff_rate = (total / av * 100) if av > 0 else 0

        st.markdown("### Detailed Duty Computation")

        header = (
            "<div style='background:#1a3c5e;color:white;border-radius:8px 8px 0 0;"
            "padding:.6rem 1rem;'>"
            "<div style='display:grid;grid-template-columns:3fr 1.2fr 1.2fr 1.2fr;"
            "font-weight:700;'>"
            "<span>Tax Component</span>"
            "<span style='text-align:right;'>Rate</span>"
            "<span style='text-align:right;'>Base (BDT)</span>"
            "<span style='text-align:right;'>Amount (BDT)</span>"
            "</div></div>"
        )
        st.markdown(header, unsafe_allow_html=True)

        rows = [
            ("Assessable Value (AV)", "—",     av,                          av),
            ("Customs Duty (CD)",     f"{cd_rate}%",   av,                  cd),
            ("Regulatory Duty (RD)",  f"{rd_rate}%",   av,                  rd),
            ("Supplementary Duty (SD)", f"{sd_rate}%", av + cd + rd,        sd),
            ("VAT",                   f"{vat_rate}%",  av + cd + rd + sd,   vat),
            ("Advance Tax (AT)",      f"{at_rate}%",   av + cd + rd + sd + vat, at),
            ("Advance Income Tax (AIT)", f"{ait_rate}%", av,                ait),
        ]
        bgs = ["#f8f9fa", "#e8f4fd", "#e8f4fd", "#f0e8fd", "#e8fdf0", "#fdf5e8", "#fde8e8"]
        for (label, rate, base, amount), bg in zip(rows, bgs):
            base_str = "—" if label == "Assessable Value (AV)" else f"{base:,.0f}"
            st.markdown(
                f"<div style='background:{bg};padding:.45rem 1rem;"
                f"border-bottom:1px solid #dee2e6;'>"
                f"<div style='display:grid;grid-template-columns:3fr 1.2fr 1.2fr 1.2fr;'>"
                f"<span>{label}</span>"
                f"<span style='text-align:right;'>{rate}</span>"
                f"<span style='text-align:right;font-size:.83rem;color:#666;'>{base_str}</span>"
                f"<span style='text-align:right;font-weight:600;'>{amount:,.0f}</span>"
                f"</div></div>",
                unsafe_allow_html=True,
            )

        st.markdown(
            f"<div style='background:#1a3c5e;color:white;border-radius:0 0 8px 8px;"
            f"padding:.6rem 1rem;'>"
            f"<div style='display:grid;grid-template-columns:3fr 1.2fr 1.2fr 1.2fr;"
            f"font-weight:700;'>"
            f"<span>Total Tax Burden</span>"
            f"<span style='text-align:right;color:#FFD700;'>{eff_rate:.1f}% eff.</span>"
            f"<span></span>"
            f"<span style='text-align:right;color:#FFD700;'>BDT {total:,.0f}</span>"
            f"</div></div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<div style='background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;"
            f"border-radius:8px;padding:1rem 1.5rem;margin-top:.8rem;text-align:center;'>"
            f"<div style='font-size:.9rem;'>Total Landed Cost (AV + All Taxes)</div>"
            f"<div style='font-size:1.8rem;font-weight:700;'>BDT {landed:,.0f}</div>"
            f"<div style='font-size:.85rem;opacity:.9;'>"
            f"Effective tax rate: {eff_rate:.1f}% of Assessable Value</div>"
            f"</div>",
            unsafe_allow_html=True,
        )


def section_quiz():
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 7")

    questions = [
        {
            "q": "Under Section 30, the applicable duty rate is determined on which date?",
            "opts": ["Date of shipment", "Date of LC opening",
                     "Date of Bill of Entry filing", "Date of payment"],
            "ans": "Date of Bill of Entry filing",
            "exp": "Section 30 — the rate in force on the date the Bill of Entry is filed applies.",
        },
        {
            "q": "VAT on imports is calculated on which base?",
            "opts": ["Assessable Value only", "AV + CD",
                     "AV + CD + RD + SD", "Invoice value"],
            "ans": "AV + CD + RD + SD",
            "exp": "VAT is calculated on Assessable Value plus Customs Duty, Regulatory Duty, and Supplementary Duty.",
        },
        {
            "q": "Advance Income Tax (AIT) paid at import stage is:",
            "opts": [
                "A final tax — cannot be claimed back",
                "Adjustable against annual income tax",
                "Refundable only for exporters",
                "Not applicable to commercial importers",
            ],
            "ans": "Adjustable against annual income tax",
            "exp": "AIT paid at import stage is adjustable (creditable) against the annual income tax liability.",
        },
        {
            "q": "Under Section 30A, the exchange rate for customs duty is:",
            "opts": [
                "Inter-bank market rate",
                "Rate notified by Bangladesh Bank",
                "Rate notified by NBR",
                "Rate on the LC date",
            ],
            "ans": "Rate notified by NBR",
            "exp": "Section 30A — exchange rate for customs duty is the rate notified by NBR.",
        },
    ]

    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['q']}**")
        sel = st.radio("", q["opts"], key=f"m7_q{i}", index=None, label_visibility="collapsed")
        answers.append((sel, q["ans"], q["exp"]))

    if st.button("✅ Submit Answers — Module 7", type="primary"):
        score = sum(1 for a, c, _ in answers if a == c)
        st.markdown(f"### 🎯 Score: {score}/{len(questions)}")
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
            <li><b>Cascading tax structure</b> — effective total rate can be 50–80%+ for high-duty goods.</li>
            <li><b>Section 30 date rule</b> — duty rate changes between LC opening and Bill of Entry filing affect landed cost.</li>
            <li><b>NBR exchange rate vs bank rate</b> — the difference can materially affect duty on large shipments.</li>
            <li><b>AT and AIT are adjustable</b> — maintain proper documentation to claim credits in your income tax return.</li>
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
            "border-radius:6px;font-size:.9rem;'>← Module 6: Customs Valuation</span>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;color:#888;font-size:.85rem;'>"
            "Module 7 of 12 · Customs Act of Bangladesh</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            "<div style='text-align:right;'><span style='background:#2e6da4;color:white;"
            "padding:.4rem 1rem;border-radius:6px;font-size:.9rem;'>"
            "Next → Module 8: Import &amp; Export Procedure</span></div>",
            unsafe_allow_html=True,
        )


# ── Main ───────────────────────────────────────────────────────────────────────
sidebar()
hero()
section_key_sections()
section_tax_chain()
section_rates()
section_calculator()
section_quiz()
takeaways()
nav_footer()