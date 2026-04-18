import streamlit as st

# ── NO st.set_page_config() here ──────────────────────────────────────────────

def main():

    st.markdown("""
    <div style="background: linear-gradient(135deg, #1a3c5e 0%, #2e6da4 100%);
                padding: 2.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem;">
        <h1 style="color:#FFD700; font-size:2rem; margin:0;">🛃 Customs Act of Bangladesh</h1>
        <h2 style="color:#ffffff; font-size:1.3rem; margin:0.4rem 0 0 0; font-weight:400;">
            Module 3 · Powers & Duties of Officers
        </h2>
        <p style="color:#cce0f5; margin:0.6rem 0 0 0; font-size:0.95rem;">
            Sections 3, 4, 6, 19, 20 · Appointment · Exemptions · Delegation
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f4fd; border-radius:8px; padding:0.7rem 1.2rem;
                margin-bottom:1.5rem; border-left:4px solid #2e6da4;">
        <strong>📍 Progress:</strong> Module 3 of 12 &nbsp;|&nbsp;
        <span style="color:#2e6da4;">⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜</span>
        &nbsp; 25% Complete
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### 🗂️ Customs Act — All Modules")
        modules = [
            ("✅","1","Introduction"),("✅","2","Key Definitions"),("✅","3","Powers & Duties"),
            ("⬜","4","Ports & Stations"),("⬜","5","Prohibition & Restriction"),("⬜","6","Customs Valuation"),
            ("⬜","7","Assessment & Duties"),("⬜","8","Import & Export Procedure"),("⬜","9","Conveyances & Passengers"),
            ("⬜","10","Offences & Penalties"),("⬜","11","Agents & Business Records"),("⬜","12","Customs Act 2023"),
        ]
        for icon, num, title in modules:
            active = "background:#2e6da4; color:white; border-radius:6px; padding:2px 6px;" if num == "3" else ""
            st.markdown(f'<div style="{active} margin-bottom:4px;">{icon} <b>M{num}.</b> {title}</div>', unsafe_allow_html=True)

    # ── Section Cards ──────────────────────────────────────────────────────────
    st.subheader("📌 Key Sections in This Module")
    cols = st.columns(4)
    for col, sec, title in zip(cols, ["Sec 3","Sec 4","Sec 6","Sec 19 & 20"],
                                ["Appointment","Powers & Duties","Delegation","Exemptions"]):
        col.markdown(f"""
        <div style="background:#1a3c5e; color:white; border-radius:10px; padding:1rem;
                    text-align:center; min-height:80px;">
            <div style="font-weight:700; color:#FFD700; font-size:1rem;">{sec}</div>
            <div style="font-size:0.85rem; margin-top:0.3rem;">{title}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("👮 Section 3 — Appointment of Customs Officers", expanded=True):
        st.markdown("""
        The Government may appoint such persons as it thinks fit to be officers of customs.

        **Hierarchy of Customs Officers:**

        | Rank | Designation |
        |------|-------------|
        | 1 | Commissioner of Customs |
        | 2 | Additional Commissioner |
        | 3 | Joint Commissioner |
        | 4 | Deputy Commissioner |
        | 5 | Assistant Commissioner |
        | 6 | Revenue Officer / Superintendent |
        | 7 | Inspector of Customs |
        | 8 | Preventive Officer / Seaman |

        💼 **Finance Lens:** Knowing the hierarchy helps you address appeals and representations to the *correct level* of authority.
        """)

    with st.expander("⚙️ Section 4 — Powers and Duties of Officers", expanded=False):
        st.markdown("""
        > *"An officer of customs appointed under Section 3 shall exercise such powers and discharge such
        > duties as are conferred or imposed on him by or under this Act; and he shall also be competent
        > to exercise all powers and discharge all duties conferred or imposed upon any officer subordinate
        > to him."*

        **Key Principles:**
        - Each officer has **specific powers** defined by the Act
        - A senior officer **can exercise powers of subordinates**
        - The Board may impose **limitations or conditions** on the exercise of powers

        **Proviso:** The Board may, by general or special order, impose such limitations or conditions on the
        exercise of such powers as it thinks fit.
        """)
        st.info("💼 **Finance Application:** If a Deputy Commissioner delays your clearance beyond his authorized scope, you can escalate — powers are defined and bounded.")

    with st.expander("🔄 Section 6 — Entrustment of Functions to Other Officers (Delegation)", expanded=False):
        st.markdown("""
        > *"The Board may, by notification in the official Gazette, entrust, either conditionally or
        > unconditionally, any functions of any officer of customs under this Act to any officer of the
        > Government."*

        **What this means:**
        - Customs functions can be **delegated** to non-Customs government officers
        - Delegation can be **conditional** (with restrictions) or **unconditional**
        - Must be done via **official Gazette notification**

        **Common Examples:**
        - Drug Administration officers assisting Customs in drug seizures
        - BSTI officials exercising customs functions for standard-testing at ports
        """)
        st.warning("⚠️ Always verify whether an officer acting on customs matters has proper delegation authority — a Gazette notification is required.")

    with st.expander("🎟️ Section 19 — General Power to Exempt from Customs Duties", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Conditions for Exemption:**
            1. Government must be **satisfied** it is in the **public interest**
            2. Must **consult the Board** (NBR)
            3. Issued by **notification in official Gazette**
            4. Subject to **conditions, limitations or restrictions**

            **Scope:**
            - Goods imported **into Bangladesh**
            - Goods exported **from Bangladesh**
            - From specified ports, stations, or areas
            - From **whole or any part** of customs duties
            """)
        with col2:
            st.markdown("""
            **Important Proviso:**
            > If in a financial year, exemption under this section is given in respect of any goods,
            > the rate of duty **cannot be changed more than once** in that year so as to increase that rate.

            **Sub-section (2):**
            > An exemption shall be **effective from the date mentioned** in the notification.

            **Common Exemption Categories:**
            - Development projects (NGOs, aid)
            - Export-oriented industries (RMG, leather)
            - Diplomatic missions
            - Essential medicines and food
            """)
        st.info("💼 **Finance Lens:** S.19 exemptions form the basis of SRO-based duty exemptions. Always check for valid SRO numbers and expiry dates in import files.")

    with st.expander("🚨 Section 20 — Exemption in Exceptional Circumstances", expanded=False):
        st.markdown("""
        > *"If the Government is satisfied that it is necessary in the public interest to do so, it may,
        > under circumstances of exceptional nature, by a special order in each case recording such
        > circumstances, exempt any goods from payment of the whole or any part of customs duties."*

        **Differences from Section 19:**

        | Feature | Section 19 | Section 20 |
        |---------|-----------|-----------|
        | Mechanism | Gazette Notification | Special Order |
        | Applicability | General / Broad | Specific case only |
        | Basis | Public interest + Board consultation | Exceptional circumstances |
        | Scope | Recurring exemptions | One-off situations |

        **Examples of Section 20 Use:**
        - Natural disaster relief goods
        - Emergency medical supplies
        - Pandemic-related imports
        """)

    # ── Interactive: Which Section Applies? ───────────────────────────────────
    st.markdown("---")
    st.subheader("🎮 Interactive Scenario: Which Section Applies?")
    st.markdown("Read each scenario and identify the relevant section:")

    scenarios = [
        ("The government issues a Gazette notification exempting garment machinery from customs duty for export-oriented industries.",
         ["Section 3", "Section 4", "Section 19", "Section 20"], "Section 19",
         "This is a general public interest exemption issued through the Gazette — Section 19."),
        ("A cyclone devastates coastal areas. The government exempts emergency food imports from duty by special order.",
         ["Section 3", "Section 6", "Section 19", "Section 20"], "Section 20",
         "Emergency/exceptional circumstances with a special order — Section 20."),
        ("NBR delegates customs inspection functions to a BSTI officer at Chattogram port via Gazette.",
         ["Section 3", "Section 4", "Section 6", "Section 19"], "Section 6",
         "Delegation of customs functions to another government officer via Gazette — Section 6."),
        ("A Commissioner of Customs exercises the powers of a Superintendent during a port inspection.",
         ["Section 3", "Section 4", "Section 6", "Section 20"], "Section 4",
         "Senior officers can exercise powers of subordinate officers — Section 4."),
    ]

    for i, (scenario, options, correct, explanation) in enumerate(scenarios):
        st.markdown(f"**Scenario {i+1}:** {scenario}")
        ans = st.radio("Which section applies?", options, key=f"m3_scen{i}", index=None, label_visibility="collapsed")
        if ans:
            if ans == correct:
                st.success(f"✅ Correct! — {explanation}")
            else:
                st.error(f"❌ Not quite. Correct: **{correct}** — {explanation}")
        st.markdown("---")

    # ── Quiz ───────────────────────────────────────────────────────────────────
    st.subheader("🧠 Quick Knowledge Check — Module 3")
    questions = [
        {
            "q": "Under Section 19, how many times can duty rate be increased for an exempted good in a financial year?",
            "options": ["Never", "Once", "Twice", "As many times as needed"],
            "answer": "Once",
            "explanation": "The proviso to Section 19 states that the duty rate cannot be changed more than once in a year to increase it."
        },
        {
            "q": "Section 6 requires delegation of customs functions to be done via:",
            "options": ["Verbal order", "Special order", "Official Gazette notification", "Board circular"],
            "answer": "Official Gazette notification",
            "explanation": "Section 6 requires delegation to be notified in the official Gazette."
        },
        {
            "q": "What is the key difference between Section 19 and Section 20 exemptions?",
            "options": [
                "Section 19 is for exports only; Section 20 for imports",
                "Section 19 is general via Gazette; Section 20 is exceptional via special order",
                "Section 20 requires Board consultation; Section 19 does not",
                "There is no difference"
            ],
            "answer": "Section 19 is general via Gazette; Section 20 is exceptional via special order",
            "explanation": "Section 19 is for general exemptions via Gazette notification; Section 20 is for exceptional circumstances via special order in each case."
        },
    ]
    user_answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}. {q['q']}**")
        ans = st.radio("", q["options"], key=f"m3_q{i}", index=None, label_visibility="collapsed")
        user_answers.append((ans, q["answer"], q["explanation"]))

    if st.button("✅ Submit Answers — Module 3", type="primary"):
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
            <li><b>Section 19 SROs</b> are the most commonly referenced in import files — verify SRO number, effective date, and applicable goods.</li>
            <li><b>Section 20 orders</b> are time-bound and specific — don't assume they create ongoing precedent.</li>
            <li><b>Delegation (Sec 6)</b> must be via Gazette — if an officer acts without published authority, the action may be challengeable.</li>
            <li><b>Hierarchy (Sec 4)</b> — a senior officer can step in at any level, which matters in appeals and representations.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_prev, col_mid, col_next = st.columns([1, 2, 1])
    with col_prev:
        st.markdown('<div style="text-align:left;"><span style="background:#6c757d;color:white;padding:0.4rem 1rem;border-radius:6px;font-size:0.9rem;">← Module 2: Key Definitions</span></div>', unsafe_allow_html=True)
    with col_mid:
        st.markdown('<div style="text-align:center;color:#888;font-size:0.85rem;">Module 3 of 12 · Customs Act of Bangladesh</div>', unsafe_allow_html=True)
    with col_next:
        st.markdown('<div style="text-align:right;"><span style="background:#2e6da4;color:white;padding:0.4rem 1rem;border-radius:6px;font-size:0.9rem;">Next → Module 4: Ports & Stations</span></div>', unsafe_allow_html=True)


main()