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
            if num == "6":
                st.markdown(
                    f"<div style='background:#2e6da4;color:white;border-radius:6px;"
                    f"padding:3px 8px;margin-bottom:3px;'>✅ M{num}. {title}</div>",
                    unsafe_allow_html=True,
                )
            else:
                done = "✅" if int(num) < 6 else "⬜"
                st.markdown(f"{done} M{num}. {title}")
        st.info("Use the Assessable Value Calculator below!")


def hero():
    st.markdown(
        """
        <div style="background:linear-gradient(135deg,#1a3c5e,#2e6da4);
                    padding:2.2rem 2rem;border-radius:12px;margin-bottom:1.2rem;">
          <h1 style="color:#FFD700;font-size:1.9rem;margin:0;">
            🛃 Customs Act of Bangladesh
          </h1>
          <h2 style="color:#fff;font-size:1.2rem;margin:.4rem 0 0;font-weight:400;">
            Module 6 · Customs Valuation
          </h2>
          <p style="color:#cce0f5;margin:.5rem 0 0;font-size:.9rem;">
            Section 25 · Valuation Rules 2000 · 6 Methods · Assessable Value Calculator
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="background:#e8f4fd;border-radius:8px;padding:.6rem 1.2rem;
                    margin-bottom:1.2rem;border-left:4px solid #2e6da4;">
          <b>Progress:</b> Module 6 of 12 &nbsp;|&nbsp;
          <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜</span>
          &nbsp; 50% Complete
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_legal():
    with st.expander("📜 Legal Basis — Section 25 & Valuation Rules 2000", expanded=True):
        st.markdown(
            """
**Section 25 of the Customs Act** provides the framework for determining the **assessable value**
(customs value) of imported goods.

**Customs Valuation Rules, 2000** (SRO no. 57-law/2000) detail the 6 sequential methods.

**Additional Instruments:**
- **Tariff Value** — Government-declared fixed values for specific goods
- **Minimum Value** — Floor price below which customs value cannot be accepted
  (SRO no. 203-Law/2022)

> **Core Principle (WTO CVA / GATT Article VII):** Customs value is the base on which
> *every* import tax is calculated — CIF basis in Bangladesh.

**CIF = Cost of Goods + Insurance + Freight** (to Bangladeshi port of entry)
            """
        )


def section_methods():
    st.markdown("---")
    st.subheader("📊 The 6 Valuation Methods — Applied Sequentially")
    st.info("⚡ Methods must be applied **in order**. Only move to the next if the previous cannot be used.")

    methods = [
        (
            "1", "Transaction Value", "Rule 3 / Section 25",
            "The **price actually paid or payable** for the goods when sold for export to Bangladesh, "
            "adjusted for certain additions (freight, insurance, royalties, etc.).",
            ["Invoice value", "Freight", "Insurance", "Royalties & licence fees", "Packing costs"],
            "Most commonly used (>95% of cases). Always start here.",
            "#27ae60",
        ),
        (
            "2", "Transaction Value of Identical Goods", "Rule 4",
            "Based on the transaction value of **identical goods** (same physical characteristics, "
            "quality, reputation) sold for export to Bangladesh at or about the same time.",
            ["Same physical characteristics", "Same quality", "Same reputation", "Produced in same country"],
            "Used when invoice value is disputed or unavailable.",
            "#2980b9",
        ),
        (
            "3", "Transaction Value of Similar Goods", "Rule 5",
            "Based on the transaction value of **similar goods** that closely resemble and are "
            "commercially interchangeable with the imported goods.",
            ["Similar characteristics", "Similar quality", "Commercially interchangeable", "Same country of production"],
            "Used when identical goods data is unavailable.",
            "#8e44ad",
        ),
        (
            "4", "Deductive Value Method", "Rule 6",
            "Based on the **unit price at which goods are sold** in Bangladesh in the greatest "
            "aggregate quantity, with deductions for local costs and duties.",
            ["Local sale price", "Less: Commissions", "Less: Local transport/insurance", "Less: Import duties", "Less: Profit margin"],
            "Works backwards from the local selling price.",
            "#e67e22",
        ),
        (
            "5", "Computed Value Method", "Rule 7",
            "Based on the **cost of production** — adding materials, fabrication, profit, "
            "and general expenses in the exporting country.",
            ["Cost of materials", "Cost of fabrication", "Profit in exporting country", "General expenses"],
            "Requires detailed cost data from manufacturer — rarely used.",
            "#c0392b",
        ),
        (
            "6", "Residual / Fall-back Method", "Rule 8",
            "Determined using **flexible application** of methods 1–5 or other reasonable means "
            "consistent with WTO CVA principles.",
            ["Flexible use of Methods 1–5", "Published price lists", "Reasonable estimates"],
            "Last resort — used when no other method is applicable.",
            "#7f8c8d",
        ),
    ]

    for num, name, ref, desc, components, tip, colour in methods:
        with st.expander(f"Method {num}: {name}  ({ref})", expanded=(num == "1")):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown(f"**Definition:** {desc}")
                st.markdown("**Key Components:**")
                for c in components:
                    st.markdown(f"- {c}")
            with col2:
                st.markdown(
                    f"<div style='background:{colour};color:white;border-radius:8px;"
                    f"padding:.9rem;font-size:.88rem;'>"
                    f"<b>Practical Tip</b><br>{tip}</div>",
                    unsafe_allow_html=True,
                )


def section_additions():
    with st.expander("➕ Additions & Exclusions to Transaction Value (Rule 3)", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
**Amounts to ADD:**
- Commissions & brokerage *(except buying commission)*
- Cost of containers & packing
- Assists (materials/tools supplied free by buyer)
- Royalties & licence fees
- Proceeds of any subsequent resale going to seller
- **Freight** to Bangladesh port
- **Insurance** for transport
- Handling charges at port of export
                """
            )
        with col2:
            st.markdown(
                """
**Amounts NOT included:**
- Cost of transport *after* arrival in Bangladesh
- Import duties/taxes payable in Bangladesh
- Post-importation construction or maintenance costs
- **Buying commissions** (excluded explicitly)
- Financing charges if shown separately
                """
            )
        st.info(
            "💼 **Finance Lens:** Bangladesh uses **CIF basis**. "
            "If your LC is on FOB terms, always add freight & insurance to arrive at customs value."
        )


def section_tariff():
    with st.expander("📌 Tariff Value & Minimum Value", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
**Tariff Value**
- Government-declared **fixed value** for specific goods
- Published via SRO (Statutory Regulatory Order)
- **Overrides** all other methods where it exists
- Common for: edible oils, petroleum products, sugar, cigarettes
                """
            )
        with col2:
            st.markdown(
                """
**Minimum Value**
- **Floor price** — customs value cannot fall below this
- Prevents invoice under-valuation
- Published via SRO no. 203-Law/2022
- Common for: garments, electronics, consumer goods
                """
            )
        st.warning(
            "⚠️ If your intercompany import price is below the Minimum Value, "
            "Customs will assess on the minimum value — increasing your duty burden."
        )


def section_calculator():
    st.markdown("---")
    st.subheader("🧮 Assessable Value Calculator (Transaction Value / CIF Basis)")
    st.markdown("Fill in the import details to compute the customs assessable value:")

    col1, col2 = st.columns(2)
    with col1:
        invoice = st.number_input("Invoice Value (USD)", min_value=0.0, value=10000.0, step=100.0)
        freight = st.number_input("Freight Cost (USD)", min_value=0.0, value=500.0, step=50.0)
        insurance = st.number_input("Insurance Cost (USD)", min_value=0.0, value=50.0, step=10.0)
    with col2:
        fx = st.number_input("Exchange Rate (BDT per USD)", min_value=1.0, value=110.0, step=0.5)
        commission = st.number_input("Commissions / Brokerage (USD) — excl. buying commission",
                                     min_value=0.0, value=0.0, step=50.0)
        royalties = st.number_input("Royalties / Licence Fees (USD)", min_value=0.0, value=0.0, step=50.0)

    if st.button("📊 Calculate Assessable Value", type="primary"):
        cif_usd = invoice + freight + insurance + commission + royalties
        av_bdt = cif_usd * fx

        st.markdown("### Calculation Breakdown")
        rows = [
            ("Invoice Value", invoice),
            ("+ Freight", freight),
            ("+ Insurance", insurance),
            ("+ Commissions", commission),
            ("+ Royalties", royalties),
        ]
        for label, val in rows:
            c1, c2, c3 = st.columns([3, 1, 1])
            c1.write(label)
            c2.write(f"USD {val:,.2f}")
            c3.write(f"BDT {val * fx:,.0f}")

        st.markdown("---")
        ca, cb, cc = st.columns([3, 1, 1])
        ca.markdown("**🎯 ASSESSABLE VALUE (CIF)**")
        cb.markdown(f"**USD {cif_usd:,.2f}**")
        cc.markdown(f"**BDT {av_bdt:,.0f}**")

        st.success(
            f"Customs Assessable Value = **BDT {av_bdt:,.0f}** "
            f"(USD {cif_usd:,.2f} × {fx})"
        )
        st.info(
            "This assessable value is the **base** for Customs Duty, Regulatory Duty, "
            "VAT, and other taxes. See Module 7 for the full duty chain."
        )


def section_quiz():
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 6")

    questions = [
        {
            "q": "What is the FIRST valuation method to be applied under the Customs Valuation Rules?",
            "opts": ["Computed Value", "Transaction Value", "Deductive Value", "Residual Method"],
            "ans": "Transaction Value",
            "exp": "Transaction Value (Rule 3) is always applied first — it is the primary method.",
        },
        {
            "q": "Bangladesh uses which basis for calculating customs value?",
            "opts": ["FOB", "CFR", "CIF", "EXW"],
            "ans": "CIF",
            "exp": "Bangladesh uses CIF — freight and insurance are included in the assessable value.",
        },
        {
            "q": "A Government-declared 'Tariff Value' for a specific good:",
            "opts": [
                "Is always lower than the invoice value",
                "Overrides all other valuation methods for that good",
                "Applies only to exports",
                "Is negotiable with the Customs officer",
            ],
            "ans": "Overrides all other valuation methods for that good",
            "exp": "Tariff Value is fixed by the Government and takes precedence over all other methods.",
        },
        {
            "q": "Buying commissions paid by the importer to their buying agent are:",
            "opts": [
                "Added to the transaction value",
                "Not added to the transaction value",
                "Deducted from invoice value",
                "Subject to separate customs duty",
            ],
            "ans": "Not added to the transaction value",
            "exp": "Buying commissions are explicitly excluded from additions under the Valuation Rules.",
        },
    ]

    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['q']}**")
        sel = st.radio("", q["opts"], key=f"m6_q{i}", index=None, label_visibility="collapsed")
        answers.append((sel, q["ans"], q["exp"]))

    if st.button("✅ Submit Answers — Module 6", type="primary"):
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
            <li><b>CIF vs FOB</b> — Bangladesh uses CIF. Add freight & insurance when LC is on FOB terms.</li>
            <li><b>Royalties and licence fees</b> must be added — common audit finding for branded goods importers.</li>
            <li><b>Minimum Value SROs</b> set transfer-pricing floors — intercompany prices below minimum trigger reassessment.</li>
            <li><b>Valuation disputes</b> are common — keep freight, insurance, and charges documentation for audit defence.</li>
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
            "border-radius:6px;font-size:.9rem;'>← Module 5: Prohibition</span>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;color:#888;font-size:.85rem;'>"
            "Module 6 of 12 · Customs Act of Bangladesh</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            "<div style='text-align:right;'><span style='background:#2e6da4;color:white;"
            "padding:.4rem 1rem;border-radius:6px;font-size:.9rem;'>"
            "Next → Module 7: Assessment & Duties</span></div>",
            unsafe_allow_html=True,
        )


# ── Main ───────────────────────────────────────────────────────────────────────
sidebar()
hero()
section_legal()
section_methods()
section_additions()
section_tariff()
section_calculator()
section_quiz()
takeaways()
nav_footer()