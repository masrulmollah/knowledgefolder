import streamlit as st

# ── NO st.set_page_config() here ──────────────────────────────────────────────

def main():

    # ── Hero Banner ────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a3c5e 0%, #2e6da4 100%);
                padding: 2.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem;">
        <h1 style="color:#FFD700; font-size:2rem; margin:0;">
            🛃 Customs Act of Bangladesh
        </h1>
        <h2 style="color:#ffffff; font-size:1.3rem; margin:0.4rem 0 0 0; font-weight:400;">
            Module 2 · Key Definitions (Section 2)
        </h2>
        <p style="color:#cce0f5; margin:0.6rem 0 0 0; font-size:0.95rem;">
            Agent · Bill of Entry · Goods · Smuggle · Customs Area & more
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Progress Indicator ─────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:#e8f4fd; border-radius:8px; padding:0.7rem 1.2rem;
                margin-bottom:1.5rem; border-left:4px solid #2e6da4;">
        <strong>📍 Progress:</strong> Module 2 of 12 &nbsp;|&nbsp;
        <span style="color:#2e6da4;">⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜</span>
        &nbsp; 17% Complete
    </div>
    """, unsafe_allow_html=True)

    # ── Sidebar Navigation ─────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("### 🗂️ Customs Act — All Modules")
        modules = [
            ("✅", "1", "Introduction"),
            ("✅", "2", "Key Definitions"),
            ("⬜", "3", "Powers & Duties"),
            ("⬜", "4", "Ports & Stations"),
            ("⬜", "5", "Prohibition & Restriction"),
            ("⬜", "6", "Customs Valuation"),
            ("⬜", "7", "Assessment & Duties"),
            ("⬜", "8", "Import & Export Procedure"),
            ("⬜", "9", "Conveyances & Passengers"),
            ("⬜", "10", "Offences & Penalties"),
            ("⬜", "11", "Agents & Business Records"),
            ("⬜", "12", "Customs Act 2023 — New Provisions"),
        ]
        for icon, num, title in modules:
            active = "background:#2e6da4; color:white; border-radius:6px; padding:2px 6px;" if num == "2" else ""
            st.markdown(
                f'<div style="{active} margin-bottom:4px;">{icon} <b>M{num}.</b> {title}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("---")
        st.info("📘 Definitions are tested heavily in exams. Use the Definition Finder tool below!")

    # ── All Definitions ────────────────────────────────────────────────────────
    definitions = {
        "Agent [Sec 2(a)]": {
            "icon": "🤝",
            "text": "Any person, including a **Shipping Agent**, **Clearing and Forwarding Agent**, **Cargo Agent**, and **Freight Forwarding Agent**, licensed under Section 207, or any person permitted to transact any business under Section 208.",
            "key_terms": ["Shipping Agent", "C&F Agent", "Section 207", "Section 208"],
            "finance_tip": "C&F agents are your primary interface with Customs. Their license status directly impacts your clearance timelines and liability."
        },
        "Appropriate Officer [Sec 2(b)]": {
            "icon": "👮",
            "text": "In relation to any functions to be performed under this Act, means the **officer of customs** to whom such functions have been **assigned** by or under this Act.",
            "key_terms": ["Officer of Customs", "Assigned Functions"],
            "finance_tip": "Knowing which officer has jurisdiction is critical when filing protests or seeking redress."
        },
        "Bill of Entry [Sec 2(c)]": {
            "icon": "📥",
            "text": "A bill of entry **delivered under Section 79**, and includes an **electronically transmitted** bill of entry in such cases and in such manner containing such particulars as the Board may specify.",
            "key_terms": ["Section 79", "Electronic Bill of Entry", "Import Declaration"],
            "finance_tip": "The Bill of Entry is the core import document — errors here trigger misdeclaration penalties. Always verify HS Code, quantity, and value."
        },
        "Bill of Export [Sec 2(d)]": {
            "icon": "📤",
            "text": "A bill of export **delivered under Section 131**, and includes an **electronically transmitted** bill of export in such cases and in such manner as the Board may specify.",
            "key_terms": ["Section 131", "Electronic Bill of Export", "Export Declaration"],
            "finance_tip": "Required for all export shipments. Errors can delay export clearance and affect export incentive claims."
        },
        "Conveyance [Sec 2(e)]": {
            "icon": "🚢",
            "text": "Any **means of transport** used for carrying goods or passengers — such as a **vessel, aircraft, vehicle or animal**.",
            "key_terms": ["Vessel", "Aircraft", "Vehicle", "Animal"],
            "finance_tip": "The type of conveyance determines which port/station has jurisdiction and applicable duty rates for certain goods."
        },
        "Customs Area [Sec 2(f)]": {
            "icon": "📍",
            "text": "The **limits of the customs station** specified under Section 10, and includes any area in which **imported goods or goods for export are ordinarily kept** before clearance by the customs authorities.",
            "key_terms": ["Customs Station", "Section 10", "Import Storage", "Pre-clearance Area"],
            "finance_tip": "Goods within the customs area are under customs control — unauthorized removal is an offence regardless of duty payment status."
        },
        "Customs Computer System [Sec 2(g)]": {
            "icon": "💻",
            "text": "The **customs computerized entry processing system** (ASYCUDA) established by the Board for the purposes of this Act.",
            "key_terms": ["ASYCUDA", "Electronic Processing", "Automated System"],
            "finance_tip": "ASYCUDA World is Bangladesh's customs IT system. Electronic submissions through this system are legally equivalent to paper submissions."
        },
        "Customs Port [Sec 2(h)]": {
            "icon": "⚓",
            "text": "Any place **declared under Section 9** to be a port for the **shipment and landing of goods**.",
            "key_terms": ["Section 9", "Designated Port", "Shipment", "Landing"],
            "finance_tip": "Goods can only be legally imported/exported through declared customs ports — Chattogram, Mongla, Benapole, etc."
        },
        "Customs Station [Sec 2(i)]": {
            "icon": "🏭",
            "text": "Any **customs port**, **customs airport**, or any **land customs station**.",
            "key_terms": ["Customs Port", "Customs Airport", "Land Customs Station"],
            "finance_tip": "The appropriate customs station determines which tariff schedules and local SROs apply."
        },
        "Export Manifest [Sec 2(j)]": {
            "icon": "📋",
            "text": "An export manifest **delivered under Section 53**, and includes **electronically transmitted** export manifest in such cases and manner as the Board may specify.",
            "key_terms": ["Section 53", "Electronic Manifest", "Cargo List"],
            "finance_tip": "The Export Manifest is submitted by the carrier (ship/aircraft agent) — discrepancies with Bill of Export trigger penalties."
        },
        "Goods [Sec 2(k)]": {
            "icon": "📦",
            "text": "All **movable goods** and includes — **conveyances, stores and materials, baggage, currency and negotiable instruments, electronic data**.",
            "key_terms": ["Movable Property", "Currency", "Negotiable Instruments", "Electronic Data", "Baggage"],
            "finance_tip": "Note that 'goods' includes electronic data — this has implications for digital trade, software imports, and data storage devices."
        },
        "Import Manifest [Sec 2(l)]": {
            "icon": "📑",
            "text": "An import manifest **delivered under Sections 43 and 44**, and includes **electronically transmitted** import manifest in such cases and manner as the Board may specify.",
            "key_terms": ["Section 43", "Section 44", "Cargo Manifest", "Carrier Declaration"],
            "finance_tip": "Filed by the carrier before arrival. Discrepancies between the manifest and actual cargo lead to short-landing or excess landing reports."
        },
        "Person-in-Charge [Sec 2(m)]": {
            "icon": "👤",
            "text": "In relation to a **vessel** — master; **aircraft** — commander/pilot; **railway train** — conductor/guard; **other conveyance** — driver or person in control.",
            "key_terms": ["Master", "Commander", "Pilot", "Conductor", "Driver"],
            "finance_tip": "The person-in-charge is legally responsible for the conveyance's customs compliance — including proper manifests and route adherence."
        },
        "Smuggle [Sec 2(n)]": {
            "icon": "🚨",
            "text": "To **bring into or take out of Bangladesh** in breach of any prohibition or restriction for the time being in force; **or evading payment** of customs duties or taxes leviable thereon.",
            "key_terms": ["Prohibition Breach", "Restriction Breach", "Duty Evasion"],
            "finance_tip": "Smuggling carries severe penalties including confiscation and imprisonment. Even unintentional underpayment can be treated as smuggling if intent is inferred."
        },
    }

    # ── Interactive Definition Finder ──────────────────────────────────────────
    st.subheader("🔍 Definition Finder — Search Any Term")
    search_term = st.text_input("Type a term (e.g. 'agent', 'goods', 'smuggle'):", placeholder="Search definitions...")

    if search_term:
        results = {k: v for k, v in definitions.items()
                   if search_term.lower() in k.lower()
                   or search_term.lower() in v["text"].lower()}
        if results:
            for term, data in results.items():
                st.markdown(f"""
                <div style="background:#e8f4fd; border-left:5px solid #2e6da4;
                            border-radius:8px; padding:1rem; margin-bottom:0.8rem;">
                    <b style="color:#1a3c5e;">{data['icon']} {term}</b><br>
                    <span style="color:#333;">{data['text'].replace('**', '')}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No matching definition found. Try a different keyword.")

    st.markdown("---")

    # ── Full Definitions Expanders ─────────────────────────────────────────────
    st.subheader("📖 All Definitions — Expanded")

    for term, data in definitions.items():
        with st.expander(f"{data['icon']} {term}"):
            st.markdown(data["text"])
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**🔑 Key Terms:**")
                for kt in data["key_terms"]:
                    st.markdown(f"- `{kt}`")
            with col2:
                st.info(f"💼 **Finance Lens:** {data['finance_tip']}")

    # ── Comparison Table ───────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("📊 Quick Reference: Document Types Compared")
    st.markdown("""
    | Document | Direction | Filed By | Legal Section |
    |----------|-----------|----------|---------------|
    | Bill of Entry | Import | Importer / C&F Agent | Section 79 |
    | Bill of Export | Export | Exporter / C&F Agent | Section 131 |
    | Import Manifest | Import | Carrier (Ship/Airline) | Sections 43 & 44 |
    | Export Manifest | Export | Carrier (Ship/Airline) | Section 53 |
    """)
    st.info("💡 **Key Difference:** Bills are filed by the **trader/agent**; Manifests are filed by the **carrier**.")

    # ── Interactive Quiz ───────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 2")

    questions = [
        {
            "q": "Under which Section is a 'Bill of Entry' delivered?",
            "options": ["Section 53", "Section 79", "Section 131", "Section 207"],
            "answer": "Section 79",
            "explanation": "Bill of Entry is delivered under Section 79 of the Customs Act."
        },
        {
            "q": "Which of the following is NOT included in the definition of 'Goods' under the Customs Act?",
            "options": ["Currency", "Negotiable Instruments", "Electronic Data", "Real Estate"],
            "answer": "Real Estate",
            "explanation": "'Goods' means movable goods — immovable property like real estate is excluded."
        },
        {
            "q": "Who is considered the 'Person-in-Charge' in relation to a vessel?",
            "options": ["Commander", "Master", "Conductor", "Driver"],
            "answer": "Master",
            "explanation": "In relation to a vessel, the 'Person-in-Charge' is the Master of the vessel."
        },
        {
            "q": "Under which Section is a 'Bill of Export' delivered?",
            "options": ["Section 79", "Section 53", "Section 131", "Section 43"],
            "answer": "Section 131",
            "explanation": "Bill of Export is delivered under Section 131 of the Customs Act."
        },
    ]

    user_answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("Select your answer:", q["options"], key=f"m2_q{i}", index=None, label_visibility="collapsed")
        user_answers.append((ans, q["answer"], q["explanation"]))

    if st.button("✅ Submit Answers — Module 2", type="primary"):
        score = sum(1 for ans, correct, _ in user_answers if ans == correct)
        st.markdown(f"### 🎯 Your Score: {score}/{len(questions)}")
        for i, (ans, correct, explanation) in enumerate(user_answers):
            if ans == correct:
                st.success(f"✅ Q{i+1}: Correct! — {explanation}")
            elif ans is None:
                st.warning(f"⚠️ Q{i+1}: Not answered. Correct: **{correct}** — {explanation}")
            else:
                st.error(f"❌ Q{i+1}: You chose **{ans}**. Correct: **{correct}** — {explanation}")

    # ── Key Takeaways ──────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("""
    <div style="background:linear-gradient(135deg,#e8f4fd,#f0fff4); border-radius:10px;
                padding:1.2rem 1.5rem; border-left:5px solid #2e6da4;">
        <h4 style="color:#1a3c5e; margin-top:0;">💡 Finance Professional Takeaways</h4>
        <ul style="margin:0; color:#333;">
            <li>The definition of <b>Goods</b> is broad — it includes electronic data, currency, and negotiable instruments.</li>
            <li><b>Smuggling</b> includes duty evasion, not just physical contraband — relevant for transfer pricing and customs valuation compliance.</li>
            <li><b>Bill of Entry vs Import Manifest</b> — understanding the difference prevents document mismatch issues during clearance.</li>
            <li>The <b>Customs Computer System</b> (ASYCUDA) means electronic records have full legal standing — maintain digital trails.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ── Navigation Footer ──────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    col_prev, col_mid, col_next = st.columns([1, 2, 1])
    with col_prev:
        st.markdown("""
        <div style="text-align:left;">
            <span style="background:#6c757d; color:white; padding:0.4rem 1rem;
                         border-radius:6px; font-size:0.9rem;">
                ← Module 1: Introduction
            </span>
        </div>
        """, unsafe_allow_html=True)
    with col_mid:
        st.markdown("""
        <div style="text-align:center; color:#888; font-size:0.85rem;">
            Module 2 of 12 · Customs Act of Bangladesh
        </div>
        """, unsafe_allow_html=True)
    with col_next:
        st.markdown("""
        <div style="text-align:right;">
            <span style="background:#2e6da4; color:white; padding:0.4rem 1rem;
                         border-radius:6px; font-size:0.9rem;">
                Next → Module 3: Powers & Duties
            </span>
        </div>
        """, unsafe_allow_html=True)


main()