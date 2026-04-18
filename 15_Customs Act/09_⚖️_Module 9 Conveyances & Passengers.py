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
            if num == "9":
                st.markdown(
                    f"<div style='background:#2e6da4;color:white;border-radius:6px;"
                    f"padding:3px 8px;margin-bottom:3px;'>✅ M{num}. {title}</div>",
                    unsafe_allow_html=True,
                )
            else:
                done = "✅" if int(num) < 9 else "⬜"
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
            Module 9 · Conveyances &amp; Passengers
          </h2>
          <p style="color:#cce0f5;margin:.5rem 0 0;font-size:.9rem;">
            Sections 103, 135, 136 · Baggage Rules · Duty-Free Allowances · Transhipment
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="background:#e8f4fd;border-radius:8px;padding:.6rem 1.2rem;
                    margin-bottom:1.2rem;border-left:4px solid #2e6da4;">
          <b>Progress:</b> Module 9 of 12 &nbsp;|&nbsp;
          <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜</span>
          &nbsp; 75% Complete
        </div>
        """,
        unsafe_allow_html=True,
    )


def tab_conveyance():
    st.subheader("🚢 Rules Governing Conveyances")

    with st.expander("Section 103 — Goods at Destination Station", expanded=True):
        st.markdown(
            """
**Rule:** Goods on arrival at a customs station of destination are subject to the **same laws
as goods on first importation**.

**Why this matters:**
- Prevents using inland transfers to avoid customs control
- Ensures consistent customs treatment throughout Bangladesh
- Relevant for goods under transit or transhipment procedures

*Example: Goods moving from Chattogram Port to ICD Dhaka remain under the same
customs obligations at the destination as at the original port of entry.*
            """
        )

    with st.expander("Sections 135 & 136 — Returning / Diverted Conveyances", expanded=False):
        st.markdown(
            """
**Section 135 — Goods Re-landed from Returning Conveyance:**
Goods re-landed or transhipped from a conveyance returning to or putting into another
customs station are subject to full customs procedures.

**Section 136 — Conveyance May Enter and Land Goods:**
A conveyance returning to a customs station may enter and land goods, subject to proper customs formalities.

**Practical examples:**
- Vessel departs Chattogram but returns due to bad weather — must notify Customs
- Aircraft diverted mid-flight to a different customs airport — re-clearance required
- Emergency unloading at an unscheduled port — requires Customs authorisation
            """
        )

    st.markdown("### Conveyance Types & Customs Obligations")
    st.markdown(
        """
| Conveyance | Person-in-Charge | Key Document | Route |
|-----------|-----------------|--------------|-------|
| 🚢 Vessel | Master | Import / Export Manifest | Sea |
| ✈️ Aircraft | Commander / Pilot | Aircraft General Declaration | Air |
| 🚂 Railway Train | Conductor / Guard | Customs declaration at border | Land (rail) |
| 🚚 Road Vehicle | Driver | Transit declaration at Land Port | Land (road) |
        """
    )


def tab_baggage():
    st.subheader("🧳 Passenger Baggage Rules")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
### Arriving Passenger Allowances
**Duty-Free:**
- Personal clothing and used personal effects
- 1 laptop, 1 mobile phone, 1 camera (used)
- Gifts up to approx. BDT 5,000 in value
- Foreign currency up to USD 5,000 (declare if over)
- Gold ornaments worn on person (up to 100 g with proof)

**Dutiable:**
- Additional new electronics
- New jewelry / excess gold
- Commercial quantities of goods
- Foreign currency over USD 5,000
            """
        )
    with col2:
        st.markdown(
            """
### Departing Passenger Allowances
**Can Take Out:**
- Personal clothing and effects
- Used personal items
- Foreign currency purchased from authorised bank
- Up to USD 5,000 equivalent without special permission

**Restrictions:**
- Cannot take out Bangladeshi Taka above BDT 5,000
- Goods for export require proper export documentation
- Antiques require a special export permit
- Excess foreign currency requires Bangladesh Bank permission
            """
        )

    st.warning(
        "Baggage rules are updated periodically. Always verify current limits "
        "against NBR's latest Baggage Rules notifications."
    )

    st.markdown("---")
    st.subheader("🧮 Quick Baggage Duty Estimator (illustrative)")
    item_value = st.number_input("Declared value of item (BDT)", min_value=0.0,
                                 value=50_000.0, step=1_000.0)
    category = st.selectbox(
        "Item category:",
        [
            "New Electronics (laptop / tablet)",
            "Gold / Jewelry",
            "New Clothing (commercial quantity)",
            "Perfume / Cosmetics",
            "Other Goods",
        ],
    )
    rates = {
        "New Electronics (laptop / tablet)": 0.37,
        "Gold / Jewelry": 0.15,
        "New Clothing (commercial quantity)": 0.55,
        "Perfume / Cosmetics": 0.45,
        "Other Goods": 0.30,
    }
    if st.button("Estimate Baggage Duty", type="secondary"):
        rate = rates.get(category, 0.30)
        duty = item_value * rate
        st.info(
            f"Estimated duty on **{category}**: approx. **BDT {duty:,.0f}** "
            f"({rate * 100:.0f}% effective rate).\n\n"
            f"*Illustrative only — actual duty depends on HS Code and applicable SROs.*"
        )


def tab_transhipment():
    st.subheader("🔄 Transhipment & Transit")
    st.markdown(
        """
**Transhipment:** Transfer of goods from one conveyance to another at a customs station
*without entering* the domestic market.

**Transit:** Movement of goods *through* Bangladesh from one foreign country to another.

**Key Rules:**
- Transhipped / transit goods are **not subject to import duty** (they don't enter Bangladesh)
- Must remain under customs supervision throughout
- Carrier must file a transhipment / transit declaration
- Time limit applies for completion of transhipment

**Bangladesh's Transit Role:**
Bangladesh has transit arrangements with India and Nepal, allowing goods to pass through
Bangladeshi territory — significant for regional trade facilitation.

**Bonded Trucks (BIVOT):**
Goods moving inland from ports under customs bond — duties suspended until clearance
at the destination customs station.

💼 **Finance Lens:** Transhipment / transit facilities reduce regional trade costs.
For trade finance, transhipped goods do not attract local duties — relevant for re-export structures.
        """
    )


def section_quiz():
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 9")

    questions = [
        {
            "q": "Who is the 'Person-in-Charge' of an aircraft under the Customs Act?",
            "opts": ["Captain of the port", "Commander or Pilot-in-charge",
                     "Cargo supervisor", "Ground handling agent"],
            "ans": "Commander or Pilot-in-charge",
            "exp": "The Person-in-Charge of an aircraft is the Commander or Pilot-in-charge.",
        },
        {
            "q": "Section 103 states that goods arriving at a destination customs station are treated:",
            "opts": [
                "As warehoused goods",
                "Subject to same laws as goods on first importation",
                "Exempt from duty",
                "As transhipped goods",
            ],
            "ans": "Subject to same laws as goods on first importation",
            "exp": "Section 103 — goods at destination station face the same laws as at first importation.",
        },
        {
            "q": "Transhipped goods passing through Bangladesh are:",
            "opts": [
                "Subject to full import duty",
                "Not subject to import duty",
                "Subject to 50% duty",
                "Require Export Registration Certificate",
            ],
            "ans": "Not subject to import duty",
            "exp": "Transhipped goods do not enter the domestic market and are not subject to Bangladesh import duties.",
        },
    ]

    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['q']}**")
        sel = st.radio("", q["opts"], key=f"m9_q{i}", index=None, label_visibility="collapsed")
        answers.append((sel, q["ans"], q["exp"]))

    if st.button("✅ Submit Answers — Module 9", type="primary"):
        score = sum(1 for a, c, _ in answers if a == c)
        st.markdown(f"### 🎯 Score: {score}/{len(questions)}")
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
            "border-radius:6px;font-size:.9rem;'>← Module 8: Procedures</span>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;color:#888;font-size:.85rem;'>"
            "Module 9 of 12 · Customs Act of Bangladesh</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            "<div style='text-align:right;'><span style='background:#2e6da4;color:white;"
            "padding:.4rem 1rem;border-radius:6px;font-size:.9rem;'>"
            "Next → Module 10: Offences &amp; Penalties</span></div>",
            unsafe_allow_html=True,
        )


# ── Main ───────────────────────────────────────────────────────────────────────
sidebar()
hero()

t1, t2, t3 = st.tabs(["🚢 Conveyance Rules", "🧳 Passenger Baggage", "🔄 Transhipment"])
with t1:
    tab_conveyance()
with t2:
    tab_baggage()
with t3:
    tab_transhipment()

section_quiz()
nav_footer()