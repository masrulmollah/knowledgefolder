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
            Module 1 · Introduction to Bangladesh Customs
        </h2>
        <p style="color:#cce0f5; margin:0.6rem 0 0 0; font-size:0.95rem;">
            History · Institutional Framework · NBR · Vision & Mission · Functions
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Progress Indicator ─────────────────────────────────────────────────────
    st.markdown("""
    <div style="background:#e8f4fd; border-radius:8px; padding:0.7rem 1.2rem;
                margin-bottom:1.5rem; border-left:4px solid #2e6da4;">
        <strong>📍 Progress:</strong> Module 1 of 12 &nbsp;|&nbsp;
        <span style="color:#2e6da4;">⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜</span>
        &nbsp; 8% Complete
    </div>
    """, unsafe_allow_html=True)

    # ── Sidebar Navigation ─────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown("### 🗂️ Customs Act — All Modules")
        modules = [
            ("✅", "1", "Introduction"),
            ("⬜", "2", "Key Definitions"),
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
            active = "background:#2e6da4; color:white; border-radius:6px; padding:2px 6px;" if num == "1" else ""
            st.markdown(
                f'<div style="{active} margin-bottom:4px;">{icon} <b>M{num}.</b> {title}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("---")
        st.info("📘 **Tip:** Each module builds on the previous one. Study in order for best results.")

    # ── Overview Cards ─────────────────────────────────────────────────────────
    st.subheader("📌 What You Will Learn")
    c1, c2, c3, c4 = st.columns(4)
    for col, icon, title, desc in [
        (c1, "🏛️", "History", "From 1969 Act to 2023 Reform"),
        (c2, "🏢", "NBR", "Structure & Tax Functions"),
        (c3, "🎯", "Vision & Mission", "Customs Core Purpose"),
        (c4, "⚙️", "Functions", "Key Roles of Customs"),
    ]:
        col.markdown(f"""
        <div style="background:#f0f7ff; border-radius:10px; padding:1rem;
                    text-align:center; border:1px solid #c5dff8; height:120px;">
            <div style="font-size:1.8rem;">{icon}</div>
            <div style="font-weight:700; color:#1a3c5e; margin-top:0.3rem;">{title}</div>
            <div style="font-size:0.8rem; color:#555;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Topic Expanders ────────────────────────────────────────────────────────

    with st.expander("📜 1.1 — History of Customs Act in Bangladesh", expanded=True):
        st.markdown("""
        **Timeline of Bangladesh Customs Law:**

        | Year | Event |
        |------|-------|
        | 1969 | **Customs Act 1969** enacted — formed the original legal basis |
        | 1972 | NBR established under President's Order No. 76 of 1972 |
        | 2000 | Customs Valuation Rules introduced |
        | 2022 | Major amendments to key sections |
        | **2023** | **New Customs Act 2023** — 269 sections (reduced from 286) |

        **Why the 2023 Act?**
        > To incorporate international best practices including the **WCO Revised Kyoto Convention**,
        > **WCO Safe Framework of Standards**, and **WTO Trade Facilitation Agreement (TFA)**.

        💡 **Finance Lens:** Understanding the legislative timeline helps you apply the *correct version*
        of the Act in assessments, audits, and compliance work.
        """)

    with st.expander("🏢 1.2 — NBR: National Board of Revenue", expanded=False):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            **Established:** President's Order No. 76 of 1972

            **Key Revenue Functions:**
            - 🔵 Import & Customs Duties
            - 🔵 Value Added Tax (VAT)
            - 🔵 Supplementary Duty
            - 🔵 Excise Duty
            - 🔵 Income Tax
            - 🔵 Other Fees & Charges
            """)
        with col2:
            st.markdown("""
            **Regulatory Functions:**
            - Formulate tax laws & policies
            - Administer Customs, VAT & Income Tax (under IRD)
            - Negotiate international tax treaties
            - Liaison with WCO, WTO, RILO, OPCW
            - Participate in international fiscal deliberations
            """)
        st.info("💼 **Finance Application:** NBR is the authority you deal with in all import/export tax matters, audit queries, and duty refund claims.")

    with st.expander("🎯 1.3 — Vision & Mission of Bangladesh Customs", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background:#1a3c5e; color:white; border-radius:10px;
                        padding:1.2rem; height:200px;">
                <h4 style="color:#FFD700;">👁️ Vision</h4>
                <p style="font-size:0.9rem;">
                An <b>innovative, professional and ethical</b> Customs service
                that contributes significantly to the happiness, safety,
                economic prosperity and environmental health of Bangladesh
                through ongoing modernization in line with international best practices.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background:#2e6da4; color:white; border-radius:10px;
                        padding:1.2rem; height:200px;">
                <h4 style="color:#FFD700;">🎯 Mission</h4>
                <p style="font-size:0.9rem;">
                Manage the border to <b>protect the community and environment</b>,
                provide efficient and timely revenue collection,
                implement government trade and fiscal policy,
                and facilitate trade and travel in accordance with
                international standards and best practices.
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("⚙️ 1.4 — Key Functions of Customs", expanded=False):
        functions = [
            ("💰", "Revenue Collection", "Collect duties and taxes at import & export stages — the primary fiscal function."),
            ("📋", "Law Enforcement", "Implement laws and regulations on transnational trade and commerce."),
            ("🚀", "Trade Facilitation", "Ensure expeditious and hassle-free clearance of legitimate goods."),
            ("🚫", "Anti-Smuggling", "Prevent illicit trade, smuggling, and money laundering activities."),
            ("🤝", "Business Support", "Provide support to legitimate trade and ensure ease of doing business."),
            ("🌍", "International Standards", "Align procedures with WCO, WTO, and bilateral trade agreements."),
        ]
        for i in range(0, len(functions), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(functions):
                    icon, title, desc = functions[i + j]
                    col.markdown(f"""
                    <div style="background:#f8fbff; border:1px solid #d0e8fb;
                                border-radius:8px; padding:0.9rem; margin-bottom:8px; min-height:110px;">
                        <div style="font-size:1.4rem;">{icon}</div>
                        <div style="font-weight:700; color:#1a3c5e; margin:0.3rem 0;">{title}</div>
                        <div style="font-size:0.82rem; color:#444;">{desc}</div>
                    </div>
                    """, unsafe_allow_html=True)

    with st.expander("👥 1.5 — Stakeholders of Bangladesh Customs", expanded=False):
        st.markdown("Customs operates within a wide ecosystem of stakeholders:")
        stakeholders = {
            "Trade Participants": ["Importers", "Exporters"],
            "Logistics & Agents": ["Clearing & Forwarding (C&F) Agents", "Shipping Agents", "Freight Forwarding Agents", "Courier Service Operators", "Airline Operators"],
            "Infrastructure": ["Seaports", "Airports", "Land Port Authorities", "Civil Aviation Authority"],
            "Financial": ["Banks & Financial Institutions", "AD (Authorised Dealer) Banks"],
            "Government Agencies": ["Drug Administration", "BSTI", "Atomic Energy Commission", "Quarantine Dept", "CCI&E", "DPHN"],
        }
        for category, items in stakeholders.items():
            st.markdown(f"**{category}:** " + " · ".join(f"`{i}`" for i in items))

    with st.expander("📄 1.6 — Licensing Requirements for Import & Export", expanded=False):
        st.markdown("Before you can import or export, you need the following registrations:")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Mandatory for All:**
            1. 🏪 Trade License (Local Government)
            2. 🔢 TIN Certificate (Income Tax Dept)
            3. 📊 VAT Registration (VAT Dept)
            4. 📥 IRC — Import Registration Certificate (CCI&E)
            5. 📤 ERC — Export Registration Certificate (CCI&E)
            6. 🏦 LC/LCA Opening (AD Bank)
            """)
        with col2:
            st.markdown("""
            **Sector-Specific:**
            - 💊 Drug License (Drug Administration)
            - 💣 Explosives License (Explosives Dept)
            - ☣️ Chemical License (Ministry of Home)
            - 🌿 Phytosanitary Certificate (Agriculture)
            - Other permits under allied Acts
            """)
        st.info("💼 **Finance Lens:** IRC/ERC validity and compliance are prerequisites for Letter of Credit (LC) issuance. Non-compliance leads to customs hold and financial penalties.")

    with st.expander("📚 1.7 — Laws Implemented by Customs", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Primary Acts:**
            - Customs Act, 1969 / 2023
            - Imports and Exports Control Act, 1950
            - Foreign Exchange Regulation Act, 1947
            - Import Policy Order & Export Policy
            """)
        with col2:
            st.markdown("""
            **Allied Acts:**
            - Arms Act, 1878
            - Narcotics Control Act, 1990
            - Anti-Money Laundering Act, 2002
            - Trademark Act, 2009
            - Copyright Act, 2000
            - Merchant Shipping Act, 1923
            - Patent and Design Act, 1911
            """)

    # ── Interactive Quiz ───────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 1")

    questions = [
        {
            "q": "In which year was the National Board of Revenue (NBR) established?",
            "options": ["1969", "1971", "1972", "1975"],
            "answer": "1972",
            "explanation": "NBR was established under President's Order No. 76 of 1972."
        },
        {
            "q": "How many sections does the new Customs Act 2023 contain?",
            "options": ["286", "269", "250", "300"],
            "answer": "269",
            "explanation": "The 2023 Act has 269 sections, reduced from 286 in the 1969 Act."
        },
        {
            "q": "Which international convention does the Customs Act 2023 align with?",
            "options": ["UNCITRAL Model Law", "WCO Revised Kyoto Convention", "Basel Convention", "Vienna Convention"],
            "answer": "WCO Revised Kyoto Convention",
            "explanation": "The 2023 Act incorporates WCO Revised Kyoto Convention, WCO Safe Framework, and WTO TFA."
        },
    ]

    score = 0
    user_answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("Select your answer:", q["options"], key=f"m1_q{i}", index=None, label_visibility="collapsed")
        user_answers.append((ans, q["answer"], q["explanation"]))

    if st.button("✅ Submit Answers — Module 1", type="primary"):
        score = sum(1 for ans, correct, _ in user_answers if ans == correct)
        st.markdown(f"### 🎯 Your Score: {score}/{len(questions)}")
        for i, (ans, correct, explanation) in enumerate(user_answers):
            if ans == correct:
                st.success(f"✅ Q{i+1}: Correct! — {explanation}")
            elif ans is None:
                st.warning(f"⚠️ Q{i+1}: Not answered. Correct answer: **{correct}** — {explanation}")
            else:
                st.error(f"❌ Q{i+1}: You chose **{ans}**. Correct: **{correct}** — {explanation}")

    # ── Key Takeaways ──────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("""
    <div style="background:linear-gradient(135deg,#e8f4fd,#f0fff4); border-radius:10px;
                padding:1.2rem 1.5rem; border-left:5px solid #2e6da4;">
        <h4 style="color:#1a3c5e; margin-top:0;">💡 Finance Professional Takeaways</h4>
        <ul style="margin:0; color:#333;">
            <li>The Customs Act 2023 replaces the 1969 Act and brings Bangladesh in line with global trade standards.</li>
            <li>NBR's dual role as policy-maker and administrator affects how disputes are handled — appeals go through NBR channels.</li>
            <li>IRC and ERC are foundational documents — lapses affect LC opening and import/export compliance.</li>
            <li>Understanding stakeholder roles helps identify where delays or compliance gaps arise in trade finance.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ── Navigation Footer ──────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    col_prev, col_mid, col_next = st.columns([1, 2, 1])
    with col_mid:
        st.markdown("""
        <div style="text-align:center; color:#888; font-size:0.85rem;">
            Module 1 of 12 · Customs Act of Bangladesh
        </div>
        """, unsafe_allow_html=True)
    with col_next:
        st.markdown("""
        <div style="text-align:right;">
            <span style="background:#2e6da4; color:white; padding:0.4rem 1rem;
                         border-radius:6px; font-size:0.9rem;">
                Next → Module 2: Key Definitions
            </span>
        </div>
        """, unsafe_allow_html=True)


main()