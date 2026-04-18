import streamlit as st

# ── NO st.set_page_config() here ──────────────────────────────────────────────

def main():

    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a3c5e 0%, #2e6da4 100%);
                padding: 2.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem;">
        <h1 style="color:#FFD700; font-size:2rem; margin:0;">🛃 Customs Act of Bangladesh</h1>
        <h2 style="color:#ffffff; font-size:1.3rem; margin:0.4rem 0 0 0; font-weight:400;">
            Module 4 · Customs Ports, Airports & Stations
        </h2>
        <p style="color:#cce0f5; margin:0.6rem 0 0 0; font-size:0.95rem;">
            Sections 9, 10 · Declaration · Landing Places · Customs Jurisdiction
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f4fd; border-radius:8px; padding:0.7rem 1.2rem;
                margin-bottom:1.5rem; border-left:4px solid #2e6da4;">
        <strong>📍 Progress:</strong> Module 4 of 12 &nbsp;|&nbsp;
        <span style="color:#2e6da4;">⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜</span>
        &nbsp; 33% Complete
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### 🗂️ Customs Act — All Modules")
        modules = [
            ("✅","1","Introduction"),("✅","2","Key Definitions"),("✅","3","Powers & Duties"),
            ("✅","4","Ports & Stations"),("⬜","5","Prohibition & Restriction"),("⬜","6","Customs Valuation"),
            ("⬜","7","Assessment & Duties"),("⬜","8","Import & Export Procedure"),("⬜","9","Conveyances & Passengers"),
            ("⬜","10","Offences & Penalties"),("⬜","11","Agents & Business Records"),("⬜","12","Customs Act 2023"),
        ]
        for icon, num, title in modules:
            active = "background:#2e6da4; color:white; border-radius:6px; padding:2px 6px;" if num == "4" else ""
            st.markdown(f'<div style="{active} margin-bottom:4px;">{icon} <b>M{num}.</b> {title}</div>', unsafe_allow_html=True)

    with st.expander("⚓ Section 9 — Declaration of Customs Ports, Airports & Land Stations", expanded=True):
        st.markdown("""
        The Government may, by **notification in the official Gazette**, declare:
        - Any place to be a **Customs Port** for the shipment and landing of goods
        - Any place to be a **Customs Airport** for the entry and departure of aircraft carrying goods
        - Any place to be a **Land Customs Station** for clearance of goods transported by land

        **Why this matters:** Goods can only be legally imported/exported through **declared customs stations**.
        Any import/export through an undeclared point is considered smuggling.
        """)

        st.markdown("### 🗺️ Major Customs Stations in Bangladesh")
        stations = {
            "🌊 Seaports": [
                ("Chattogram Port", "Largest seaport — handles ~92% of Bangladesh's trade"),
                ("Mongla Port", "Second seaport — southwestern region"),
                ("Payra Port", "Newest deep-sea port — Patuakhali"),
            ],
            "✈️ Airports": [
                ("Hazrat Shahjalal Intl Airport (DAC)", "Dhaka — main international airport"),
                ("Shah Amanat Intl Airport (CGP)", "Chattogram airport customs"),
                ("Osmani Intl Airport (ZYL)", "Sylhet airport customs"),
            ],
            "🚚 Land Stations": [
                ("Benapole", "Largest land port — India-Bangladesh border"),
                ("Burimari", "North Bengal — India/Bhutan trade"),
                ("Bhomra", "Satkhira — southwest India border"),
                ("Akhaura", "Tripura-Bangladesh corridor"),
                ("Tamabil", "Sylhet-Meghalaya India border"),
            ],
            "🏗️ ICDs & Others": [
                ("ICD Dhaka (Kamalapur)", "Inland Container Depot — Dhaka"),
                ("ICD Comilla", "Inland Container Depot — Comilla"),
            ],
        }
        for category, items in stations.items():
            st.markdown(f"**{category}**")
            for name, desc in items:
                st.markdown(f"- **{name}** — {desc}")

    with st.expander("📏 Section 10 — Power to Approve Landing Places & Specify Limits", expanded=False):
        st.markdown("""
        The Commissioner of Customs may, by **notification in the Official Gazette**:
        - **Approve** landing places within a customs port
        - **Specify the limits** of a customs station

        **Practical Implications:**
        - Not every berth within a port is automatically approved for all goods
        - Specific goods (dangerous, perishable, bulk) may require designated landing areas
        - The **limits of the customs station** define the **customs area** — goods inside are under customs control

        **Jetty vs Port Authority:**
        > Even if a private jetty exists within the port limits, goods can only land/depart from
        > **approved landing places** under Section 10.
        """)
        st.info("💼 **Finance Lens:** Private berth operators (refineries, cement plants) need Section 10 approval for their jetties. Verify this in trade finance due diligence.")

    # ── Types of Customs Stations ──────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🏭 Types of Customs Entry Points")
    tab1, tab2, tab3, tab4 = st.tabs(["🌊 Seaports", "✈️ Airports", "🚚 Land Ports", "🏗️ ICDs / Others"])

    with tab1:
        st.markdown("""
        ### Customs Seaports
        Goods entering/exiting by **sea vessel** must pass through a declared customs port.

        **Key Procedures at Seaports:**
        - Import/Export Manifest filing by ship's agent
        - Bill of Entry / Bill of Export lodgment
        - Physical or document examination
        - Duty assessment and payment
        - Release order issuance

        **Chattogram Port** handles approximately **92%** of Bangladesh's total trade by volume.
        """)

    with tab2:
        st.markdown("""
        ### Customs Airports
        Goods and passengers arriving by **air** must clear through a declared customs airport.

        **Special Considerations:**
        - **Air cargo** — faster clearance, higher freight costs, time-sensitive goods
        - **Passenger baggage** — separate baggage rules apply
        - **Courier** — express clearance procedures (de minimis rules)
        - **Aircraft stores** — duty-free provisions for aircraft

        **SHAJALAL (DAC)** processes most of Bangladesh's air cargo and passenger traffic.
        """)

    with tab3:
        st.markdown("""
        ### Land Customs Stations (LCS)
        Goods transported by **road or rail** across Bangladesh's land borders.

        **Key Land Borders:**

        | LCS | Country | Primary Trade |
        |-----|---------|---------------|
        | Benapole | India (West Bengal) | General merchandise, food |
        | Burimari | India (West Bengal) | Coal, stone, food |
        | Bhomra | India (West Bengal) | Agri-goods |
        | Akhaura | India (Tripura) | Border trade |
        | Tamabil | India (Meghalaya) | Coal, stone |
        | Hili | India (West Bengal) | General goods |
        | Sonamasjid | India (West Bengal) | Stone, food |
        """)

    with tab4:
        st.markdown("""
        ### ICDs — Inland Container Depots
        Dry ports / inland customs clearance facilities away from physical seaports.

        **Purpose:**
        - Decongest main ports
        - Allow clearance close to importer/exporter premises
        - Container stuffing/stripping under customs supervision

        **Major ICDs in Bangladesh:**
        - **ICD Dhaka (Kamalapur)** — largest inland container depot
        - **ICD Comilla** — serving EPZ and surrounding industries
        - **DEPZ ICD** — Dhaka Export Processing Zone
        """)

    # ── Interactive: Station Identifier ───────────────────────────────────────
    st.markdown("---")
    st.subheader("🎮 Scenario: Identify the Correct Entry Point")
    st.markdown("Match each shipment scenario to the correct type of customs entry point:")

    scenarios = [
        ("A garment factory imports 50 FCL containers of fabric from China by sea.",
         ["Customs Port (Seaport)", "Customs Airport", "Land Customs Station", "ICD"],
         "Customs Port (Seaport)", "FCL sea cargo must pass through a declared customs seaport — Chattogram or Mongla."),
        ("A pharmaceutical company imports temperature-sensitive APIs by air freight.",
         ["Customs Port (Seaport)", "Customs Airport", "Land Customs Station", "ICD"],
         "Customs Airport", "Air freight goes through a customs airport — DAC for most pharmaceutical imports."),
        ("A stone crushing company imports limestone from Meghalaya, India by truck.",
         ["Customs Port (Seaport)", "Customs Airport", "Land Customs Station", "ICD"],
         "Land Customs Station", "Land transport from India requires clearance through a Land Customs Station like Tamabil."),
        ("A Dhaka-based importer wants to clear containers at a facility near their factory, not at Chattogram port.",
         ["Customs Port (Seaport)", "Customs Airport", "Land Customs Station", "ICD"],
         "ICD", "ICDs like Kamalapur allow clearance inland, away from the main port."),
    ]

    for i, (scenario, options, correct, explanation) in enumerate(scenarios):
        st.markdown(f"**Scenario {i+1}:** _{scenario}_")
        ans = st.radio("Entry point:", options, key=f"m4_scen{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == correct:
                st.success(f"✅ Correct! — {explanation}")
            else:
                st.error(f"❌ Incorrect. Correct: **{correct}** — {explanation}")
        st.markdown("")

    # ── Quiz ───────────────────────────────────────────────────────────────────
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 4")
    questions = [
        {
            "q": "Under which Section can the Government declare a place as a Customs Port?",
            "options": ["Section 3", "Section 9", "Section 10", "Section 19"],
            "answer": "Section 9",
            "explanation": "Section 9 empowers the Government to declare customs ports, airports, and land stations."
        },
        {
            "q": "Who has the authority to approve specific landing places within a customs port?",
            "options": ["NBR Board", "Government", "Commissioner of Customs", "Appropriate Officer"],
            "answer": "Commissioner of Customs",
            "explanation": "Under Section 10, the Commissioner of Customs approves landing places and specifies station limits."
        },
        {
            "q": "What percentage of Bangladesh's trade does Chattogram Port approximately handle?",
            "options": ["50%", "75%", "92%", "100%"],
            "answer": "92%",
            "explanation": "Chattogram Port handles approximately 92% of Bangladesh's total trade volume."
        },
    ]
    user_answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"m4_q{i}", index=None, label_visibility="collapsed")
        user_answers.append((ans, q["answer"], q["explanation"]))

    if st.button("✅ Submit Answers — Module 4", type="primary"):
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
            <li>Port of entry affects <b>applicable SROs and tariff orders</b> — different stations may have different concessions.</li>
            <li><b>Private jetty operators</b> must have Section 10 approval — relevant for project finance due diligence.</li>
            <li><b>ICDs</b> reduce working capital needs by allowing faster local clearance and reducing demurrage costs.</li>
            <li>Land port vs seaport choice can <b>materially affect landed cost</b> — factor into import cost analysis.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_prev, col_mid, col_next = st.columns([1, 2, 1])
    with col_prev:
        st.markdown('<div style="text-align:left;"><span style="background:#6c757d;color:white;padding:0.4rem 1rem;border-radius:6px;font-size:0.9rem;">← Module 3: Powers & Duties</span></div>', unsafe_allow_html=True)
    with col_mid:
        st.markdown('<div style="text-align:center;color:#888;font-size:0.85rem;">Module 4 of 12 · Customs Act of Bangladesh</div>', unsafe_allow_html=True)
    with col_next:
        st.markdown('<div style="text-align:right;"><span style="background:#2e6da4;color:white;padding:0.4rem 1rem;border-radius:6px;font-size:0.9rem;">Next → Module 5: Prohibition & Restriction</span></div>', unsafe_allow_html=True)


main()