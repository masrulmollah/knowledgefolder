import streamlit as st

# ── NO st.set_page_config() here ──────────────────────────────────────────────

def main():

    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a3c5e 0%, #2e6da4 100%);
                padding: 2.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem;">
        <h1 style="color:#FFD700; font-size:2rem; margin:0;">🛃 Customs Act of Bangladesh</h1>
        <h2 style="color:#ffffff; font-size:1.3rem; margin:0.4rem 0 0 0; font-weight:400;">
            Module 5 · Prohibition & Restriction on Import/Export
        </h2>
        <p style="color:#cce0f5; margin:0.6rem 0 0 0; font-size:0.95rem;">
            Sections 15, 16, 17 · Prohibited Goods · Restricted Goods · Import & Export Policy
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f4fd; border-radius:8px; padding:0.7rem 1.2rem;
                margin-bottom:1.5rem; border-left:4px solid #2e6da4;">
        <strong>📍 Progress:</strong> Module 5 of 12 &nbsp;|&nbsp;
        <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜</span>
        &nbsp; 42% Complete
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### 🗂️ Customs Act — All Modules")
        modules = [
            ("✅","1","Introduction"),("✅","2","Key Definitions"),("✅","3","Powers & Duties"),
            ("✅","4","Ports & Stations"),("✅","5","Prohibition & Restriction"),("⬜","6","Customs Valuation"),
            ("⬜","7","Assessment & Duties"),("⬜","8","Import & Export Procedure"),("⬜","9","Conveyances & Passengers"),
            ("⬜","10","Offences & Penalties"),("⬜","11","Agents & Business Records"),("⬜","12","Customs Act 2023"),
        ]
        for icon, num, title in modules:
            active = "background:#2e6da4; color:white; border-radius:6px; padding:2px 6px;" if num == "5" else ""
            st.markdown(f'<div style="{active} margin-bottom:4px;">{icon} <b>M{num}.</b> {title}</div>', unsafe_allow_html=True)

    # ── Three-Category Overview ────────────────────────────────────────────────
    st.subheader("📌 Three Categories Under This Module")
    c1, c2, c3 = st.columns(3)
    for col, sec, title, color, desc in [
        (c1, "Sec 15", "Absolute Prohibition", "#c0392b", "Goods that can NEVER be imported/exported"),
        (c2, "Sec 16", "Conditional Restriction", "#e67e22", "Goods allowed only under specific conditions"),
        (c3, "Sec 17", "Policy-Based Restriction", "#2980b9", "Import/Export Policy Order restrictions"),
    ]:
        col.markdown(f"""
        <div style="background:{color}; color:white; border-radius:10px; padding:1rem;
                    text-align:center; min-height:100px;">
            <div style="font-weight:700; font-size:1.1rem; color:#FFD700;">{sec}</div>
            <div style="font-weight:700; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.8rem;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Section 15 Expander ────────────────────────────────────────────────────
    with st.expander("🚫 Section 15 — Absolutely Prohibited Goods", expanded=True):
        st.error("❌ These goods CANNOT enter Bangladesh by ANY route — air, land, or sea.")

        prohibited = [
            ("💰", "Counterfeit Coin", "Fake coins of any currency"),
            ("💵", "Forged Currency Notes", "Counterfeit banknotes and any counterfeit product"),
            ("📺", "Obscene Material", "Books, pamphlets, drawings, films, videos, CDs or recordings on any media"),
            ("™️", "Counterfeit Trademarks", "Goods with counterfeit trade marks under the Penal Code or Trademark Act 2009"),
            ("🏷️", "False Trade Description", "Goods with false country-of-origin or manufacturer claims"),
            ("📏", "Unmarked Piece Goods", "Foreign-made piece goods without proper length markings in standard meters in Arabic numerals"),
            ("©️", "Copyright Infringing Goods", "Goods with copyrighted designs under Patents and Designs Act 1911 without license"),
            ("🌿", "Harmful Plants/Animals", "Goods prohibited under plant quarantine or livestock importation laws"),
            ("☢️", "Radioactive Material", "Without specific government authorization"),
            ("🔫", "Weapons (Unlicensed)", "Arms and ammunition without proper license"),
        ]

        for i in range(0, len(prohibited), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(prohibited):
                    icon, title, desc = prohibited[i + j]
                    col.markdown(f"""
                    <div style="background:#fdf2f2; border:1px solid #f5c6cb; border-radius:8px;
                                padding:0.8rem; margin-bottom:8px;">
                        <span style="font-size:1.3rem;">{icon}</span>
                        <b style="color:#c0392b;"> {title}</b>
                        <div style="font-size:0.82rem; color:#555; margin-top:0.2rem;">{desc}</div>
                    </div>
                    """, unsafe_allow_html=True)

        st.info("💼 **Finance Lens:** Attempting to import prohibited goods leads to confiscation + penalties. Conduct thorough product compliance checks before LC issuance.")

    with st.expander("⚠️ Section 16 — Conditional / Restricted Goods (Import)", expanded=False):
        st.warning("⚠️ These goods CAN be imported but only under specific conditions, licenses, or permits.")
        st.markdown("""
        **Examples of Conditionally Restricted Imports:**

        | Category | Condition/Authority |
        |----------|-------------------|
        | Drugs & Pharmaceuticals | Drug Administration License |
        | Explosives & Chemicals | Ministry of Home license |
        | Radioactive materials | BAEC authorization |
        | Livestock & Animals | BLRI / Quarantine clearance |
        | Seeds & Plants | DAE Phytosanitary Certificate |
        | Firearms | Ministry of Home permit |
        | Gold & Silver | Bangladesh Bank permission |
        | Hazardous chemicals | DOE / Environmental clearance |
        | Second-hand goods | CCI&E specific permission |
        | Motor vehicles | Age restriction rules |

        **General Rule:**
        > Restricted goods require a **specific import permit** in addition to the standard IRC.
        > The relevant authority (not Customs) issues this permit.
        """)

    with st.expander("📋 Section 17 — Export Restrictions", expanded=False):
        st.markdown("""
        The Government may, by **notification in the official Gazette**, prohibit or restrict the export of
        goods — either generally or from specific ports/areas.

        **Common Export Restrictions:**

        | Category | Restriction |
        |----------|------------|
        | Raw Hides & Skins | Export may be restricted to protect local leather industry |
        | Rice / Food Grains | Restricted during shortage periods |
        | Antiques | Cultural heritage — prohibited |
        | Wildlife | CITES convention compliance required |
        | Jute (raw) | Subject to quantity restrictions |
        | Gas / Energy | Restricted for domestic security |
        | Scrap metal | Regulated for industrial use |

        **Export Policy 2024–2027:** The current Export Policy governs which goods are freely exportable,
        conditionally exportable, or prohibited for export.
        """)
        st.info("💼 **Finance Lens:** Export restrictions affect trade finance — banks may reject LCs for export-restricted goods. Always verify goods against current Export Policy before structuring export finance.")

    # ── Import Policy Overview ─────────────────────────────────────────────────
    with st.expander("📖 Import Policy Order — Classification of Goods", expanded=False):
        st.markdown("""
        The **Import Policy Order** classifies all goods into three categories:

        | Category | Description | Examples |
        |----------|-------------|---------|
        | **Freely Importable** | No restrictions — import on standard docs | Raw materials, machinery, electronics |
        | **Restricted** | Requires additional permit/license | Drugs, explosives, livestock |
        | **Prohibited** | Cannot be imported | Counterfeit goods, obscene material |

        **Import Policy Order 2021–2024** is the current operative order.

        **H.S. Code Classification:**
        > Import policy applicability is determined by the **HS Code** of the goods.
        > The same physical product may fall in different categories based on its HS heading.

        **Finance Application:**
        - Verify goods classification before issuing import LC
        - Wrong classification = customs hold + penalty exposure
        - Use Bangladesh Customs Tariff (BCT) for HS code verification
        """)

    # ── Goods Classifier Tool ─────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🔍 Quick Goods Classification Checker")
    st.markdown("Enter a product and check its general import status:")

    goods_db = {
        "counterfeit": ("🚫 PROHIBITED", "#c0392b", "Section 15 — Absolute prohibition. Cannot be imported under any circumstances."),
        "currency": ("🚫 PROHIBITED", "#c0392b", "Section 15 — Forged/counterfeit currency is absolutely prohibited."),
        "drugs": ("⚠️ RESTRICTED", "#e67e22", "Requires Drug Administration license. Import possible with proper authorization."),
        "explosives": ("⚠️ RESTRICTED", "#e67e22", "Requires Ministry of Home license. Import possible with proper authorization."),
        "medicine": ("⚠️ RESTRICTED", "#e67e22", "Pharmaceutical imports require Drug Administration clearance."),
        "arms": ("⚠️ RESTRICTED", "#e67e22", "Requires specific government authorization. Strictly controlled."),
        "weapons": ("⚠️ RESTRICTED", "#e67e22", "Requires Ministry of Home authorization."),
        "gold": ("⚠️ RESTRICTED", "#e67e22", "Requires Bangladesh Bank permission for commercial import."),
        "machinery": ("✅ FREELY IMPORTABLE", "#27ae60", "Generally freely importable subject to standard import procedures."),
        "fabric": ("✅ FREELY IMPORTABLE", "#27ae60", "Textile raw materials are generally freely importable."),
        "electronics": ("✅ FREELY IMPORTABLE", "#27ae60", "Consumer electronics are generally freely importable."),
        "food": ("✅ FREELY IMPORTABLE", "#27ae60", "Food items generally freely importable subject to BSTI/BFSA standards compliance."),
        "vehicles": ("⚠️ RESTRICTED", "#e67e22", "Subject to age restrictions and specific conditions under import policy."),
        "chemicals": ("⚠️ RESTRICTED", "#e67e22", "Requires DOE/environmental clearance and specific permits."),
        "obscene": ("🚫 PROHIBITED", "#c0392b", "Section 15 — Obscene material is absolutely prohibited."),
        "antiques": ("🚫 PROHIBITED (Export)", "#c0392b", "Export of antiques is prohibited under cultural heritage laws."),
    }

    product_input = st.text_input("Enter product name:", placeholder="e.g. machinery, drugs, gold, weapons...")
    if product_input:
        found = None
        for key, value in goods_db.items():
            if key in product_input.lower():
                found = value
                break
        if found:
            status, color, description = found
            st.markdown(f"""
            <div style="background:{color}; color:white; border-radius:10px; padding:1rem 1.5rem;">
                <h3 style="margin:0; color:white;">{status}</h3>
                <p style="margin:0.5rem 0 0 0;">{description}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("ℹ️ Product not found in quick reference database. Please consult the Bangladesh Customs Tariff (BCT) for the exact HS Code classification and applicable Import Policy Order entry.")

    # ── Quiz ───────────────────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 5")
    questions = [
        {
            "q": "Under which section are absolutely prohibited goods covered?",
            "options": ["Section 14", "Section 15", "Section 16", "Section 17"],
            "answer": "Section 15",
            "explanation": "Section 15 covers goods that are absolutely prohibited from import."
        },
        {
            "q": "Piece-goods manufactured outside Bangladesh must have their length marked in:",
            "options": ["English letters", "Bengali numerals", "Arabic numerals", "Roman numerals"],
            "answer": "Arabic numerals",
            "explanation": "Section 15(f) requires piece goods to have length conspicuously stamped in Arabic numerals."
        },
        {
            "q": "Which of these is an example of a RESTRICTED (not prohibited) import?",
            "options": ["Counterfeit coins", "Forged currency notes", "Pharmaceutical drugs", "Obscene films"],
            "answer": "Pharmaceutical drugs",
            "explanation": "Pharmaceutical drugs can be imported with proper Drug Administration license — they are restricted, not prohibited."
        },
        {
            "q": "Export restrictions under Section 17 are imposed by:",
            "options": ["NBR by circular", "Government by Gazette notification", "Commissioner of Customs", "Ministry of Commerce by order"],
            "answer": "Government by Gazette notification",
            "explanation": "Section 17 empowers the Government to impose export restrictions via official Gazette notification."
        },
    ]
    user_answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"m5_q{i}", index=None, label_visibility="collapsed")
        user_answers.append((ans, q["answer"], q["explanation"]))

    if st.button("✅ Submit Answers — Module 5", type="primary"):
        score = sum(1 for a, c, _ in user_answers if a == c)
        st.markdown(f"### 🎯 Your Score: {score}/{len(questions)}")
        for i, (ans, correct, explanation) in enumerate(user_answers):
            if ans == correct:
                st.success(f"✅ Q{i+1}: Correct! — {explanation}")
            elif ans is None:
                st.warning(f"⚠️ Q{i+1}: Not answered. Correct: **{correct}** — {explanation}")
            else:
                st.error(f"❌ Q{i+1}: You chose **{ans}**. Correct: **{correct}** — {explanation}")

    st.markdown("---")
    st.markdown("""
    <div style="background:linear-gradient(135deg,#e8f4fd,#f0fff4); border-radius:10px;
                padding:1.2rem 1.5rem; border-left:5px solid #2e6da4;">
        <h4 style="color:#1a3c5e; margin-top:0;">💡 Finance Professional Takeaways</h4>
        <ul style="margin:0; color:#333;">
            <li>Always cross-check goods against <b>Section 15</b> before processing import LCs — prohibited goods lead to instant confiscation.</li>
            <li><b>Restricted goods</b> need the permit from the <i>relevant authority</i> (not Customs) — factor permit lead time into supply chain planning.</li>
            <li><b>Export restrictions</b> can change with policy — monitor Export Policy updates, especially for agri-commodities and raw materials.</li>
            <li>HS Code misclassification can inadvertently move a freely importable good into restricted category — verify classifications carefully.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_prev, col_mid, col_next = st.columns([1, 2, 1])
    with col_prev:
        st.markdown('<div style="text-align:left;"><span style="background:#6c757d;color:white;padding:0.4rem 1rem;border-radius:6px;font-size:0.9rem;">← Module 4: Ports & Stations</span></div>', unsafe_allow_html=True)
    with col_mid:
        st.markdown('<div style="text-align:center;color:#888;font-size:0.85rem;">Module 5 of 12 · Customs Act of Bangladesh</div>', unsafe_allow_html=True)
    with col_next:
        st.markdown('<div style="text-align:right;"><span style="background:#2e6da4;color:white;padding:0.4rem 1rem;border-radius:6px;font-size:0.9rem;">Next → Module 6: Customs Valuation</span></div>', unsafe_allow_html=True)


main()