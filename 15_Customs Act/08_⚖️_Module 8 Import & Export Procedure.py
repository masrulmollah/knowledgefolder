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
            if num == "8":
                st.markdown(
                    f"<div style='background:#2e6da4;color:white;border-radius:6px;"
                    f"padding:3px 8px;margin-bottom:3px;'>✅ M{num}. {title}</div>",
                    unsafe_allow_html=True,
                )
            else:
                done = "✅" if int(num) < 8 else "⬜"
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
            Module 8 · Import &amp; Export Procedures
          </h2>
          <p style="color:#cce0f5;margin:.5rem 0 0;font-size:.9rem;">
            Sections 43, 44, 53, 79, 103, 131 · Step-by-step clearance · Documents · Warehousing
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="background:#e8f4fd;border-radius:8px;padding:.6rem 1.2rem;
                    margin-bottom:1.2rem;border-left:4px solid #2e6da4;">
          <b>Progress:</b> Module 8 of 12 &nbsp;|&nbsp;
          <span style="color:#2e6da4;">⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜</span>
          &nbsp; 67% Complete
        </div>
        """,
        unsafe_allow_html=True,
    )


def tab_import():
    st.subheader("📥 Step-by-Step Import Clearance")

    steps = [
        ("1", "Vessel / Cargo Arrival",
         "Carrier files Import Manifest (Sections 43 & 44) before/upon arrival. Contains details of all cargo on board.",
         "#1a3c5e"),
        ("2", "Manifest Verification",
         "Customs verifies manifest against actual cargo. Short-landing or excess-landing reports filed if discrepancies.",
         "#2980b9"),
        ("3", "Bill of Entry Filing (Sec 79)",
         "Importer / C&F Agent lodges Bill of Entry electronically via ASYCUDA — HS Code, quantity, value, country of origin.",
         "#8e44ad"),
        ("4", "Risk Assessment (ASYCUDA)",
         "Risk engine selects Bill of Entry lane: Green (auto-clear), Yellow (document check), Red (physical examination).",
         "#e67e22"),
        ("5", "Examination (Sec 81)",
         "For Yellow / Red lanes: Customs examines goods or checks documents. Importer or C&F agent must be present.",
         "#c0392b"),
        ("6", "Duty Assessment (Sec 80)",
         "Appropriate officer assesses CD, RD, SD, VAT, AT, AIT and issues duty assessment notice.",
         "#27ae60"),
        ("7", "Duty Payment",
         "Importer pays assessed duties through authorised bank. Treasury challan issued as proof of payment.",
         "#16a085"),
        ("8", "Out-Pass / Delivery Order",
         "Customs issues Out-Pass after duty payment. Goods released from customs area.",
         "#1a3c5e"),
    ]

    for num, title, desc, colour in steps:
        st.markdown(
            f"<div style='display:flex;margin-bottom:7px;align-items:flex-start;'>"
            f"<div style='background:{colour};color:white;border-radius:50%;width:30px;"
            f"height:30px;display:flex;align-items:center;justify-content:center;"
            f"font-weight:700;flex-shrink:0;margin-right:10px;margin-top:3px;'>{num}</div>"
            f"<div style='background:#f8f9fa;border-radius:8px;padding:.7rem 1rem;"
            f"flex:1;border-left:4px solid {colour};'>"
            f"<b>{title}</b>"
            f"<div style='font-size:.86rem;color:#444;margin-top:.2rem;'>{desc}</div>"
            f"</div></div>",
            unsafe_allow_html=True,
        )

    st.markdown("### Required Import Documents")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
**Commercial Documents:**
- Commercial Invoice
- Packing List
- Bill of Lading / Airway Bill
- Certificate of Origin
- Letter of Credit (LC) copy
            """
        )
    with c2:
        st.markdown(
            """
**Regulatory Documents:**
- Import Registration Certificate (IRC)
- UD — Utilization Declaration (if applicable)
- PSI Certificate (if required)
- BSTI Certificate (for controlled goods)
- Sector-specific permits (Drugs, Chemicals, etc.)
            """
        )


def tab_export():
    st.subheader("📤 Step-by-Step Export Clearance")

    steps = [
        ("1", "Bill of Export Filing (Sec 131)",
         "Exporter / C&F Agent files Bill of Export electronically via ASYCUDA."),
        ("2", "Document Verification",
         "Customs verifies export documents — invoice, packing list, ERC, export LC if applicable."),
        ("3", "Physical Examination",
         "Selective examination of export cargo for compliance with restrictions and declared specifications."),
        ("4", "Customs Clearance / Let-Export Order",
         "Customs issues clearance / let-export order after document and examination checks."),
        ("5", "Loading onto Vessel / Aircraft",
         "Goods loaded under customs supervision."),
        ("6", "Export Manifest Filing (Sec 53)",
         "Carrier (ship / airline agent) files Export Manifest declaring all loaded cargo."),
        ("7", "EXP Form Certification",
         "Customs certifies EXP form — required for export-proceeds repatriation tracking by Bangladesh Bank."),
    ]

    for num, title, desc in steps:
        st.markdown(
            f"<div style='display:flex;margin-bottom:7px;'>"
            f"<div style='background:#2e6da4;color:white;border-radius:50%;width:28px;"
            f"height:28px;display:flex;align-items:center;justify-content:center;"
            f"font-weight:700;flex-shrink:0;margin-right:10px;margin-top:2px;'>{num}</div>"
            f"<div style='background:#f0f7ff;border-radius:6px;padding:.65rem 1rem;"
            f"flex:1;border-left:3px solid #2e6da4;'>"
            f"<b>{title}</b>"
            f"<div style='font-size:.86rem;color:#444;margin-top:.2rem;'>{desc}</div>"
            f"</div></div>",
            unsafe_allow_html=True,
        )

    st.info(
        "💼 **Finance Lens:** Export proceeds must be repatriated within 4 months under FERA. "
        "The EXP form is the customs document Bangladesh Bank uses to track repatriation compliance."
    )


def tab_warehousing():
    st.subheader("🏭 Warehousing — Bonded Goods")
    st.markdown(
        """
**Bonded Warehouses** allow goods to be stored under customs control **without immediate duty payment**.

| Type | Description |
|------|-------------|
| Public Bonded Warehouse | General storage; open to all importers |
| Private Bonded Warehouse | Company-specific; for own goods only |
| Special Bonded Warehouse | For export-oriented industries (garments, leather, etc.) |

**Key Rules:**
- Goods remain under **customs control** until duty is paid
- Duty becomes payable on: (a) removal for local sale, or (b) re-export
- Interest / penalty applies for goods not removed within warehousing period

**Section 82 — Goods Not Cleared Within Time:**
> Goods not cleared, warehoused, or transhipped within the specified period may be
> auctioned by Customs after due notice.

💼 **Finance Lens:** Bonded warehouses defer duty payment — improving working capital.
EPZ manufacturers use Special Bonded Warehouses to import duty-free for export production.
        """
    )


def section_checklist():
    st.markdown("---")
    st.subheader("✅ Import Document Checklist")
    mode = st.radio(
        "Select import type:",
        ["Sea Import (Commercial)", "Air Import", "Land Import"],
        horizontal=True,
    )

    base = [
        "Commercial Invoice",
        "Packing List",
        "Bill of Lading / AWB",
        "Import Registration Certificate (IRC)",
        "Letter of Credit (L/C) copy",
        "Certificate of Origin",
    ]
    extra = {
        "Sea Import (Commercial)": [
            "Original Bill of Lading",
            "Shipping Agent's Delivery Order",
            "Port Release Order",
        ],
        "Air Import": [
            "Airway Bill (AWB)",
            "Express Release Authorisation",
        ],
        "Land Import": [
            "Truck / Lorry Receipt",
            "Land Customs Station Gate Pass",
        ],
    }
    all_docs = base + extra.get(mode, [])
    checked = [d for d in all_docs if st.checkbox(d, key=f"doc_{d}")]
    missing = [d for d in all_docs if d not in checked]

    if not missing:
        st.success("✅ All required documents are ready for clearance!")
    else:
        st.warning(f"⚠️ Still needed: {', '.join(missing)}")


def section_quiz():
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check — Module 8")

    questions = [
        {
            "q": "Under which Section is the Import Manifest delivered?",
            "opts": ["Section 43 & 44", "Section 53", "Section 79", "Section 131"],
            "ans": "Section 43 & 44",
            "exp": "The Import Manifest is delivered under Sections 43 and 44.",
        },
        {
            "q": "Under which Section is the Export Manifest delivered?",
            "opts": ["Section 43", "Section 53", "Section 79", "Section 131"],
            "ans": "Section 53",
            "exp": "The Export Manifest is delivered under Section 53.",
        },
        {
            "q": "In ASYCUDA risk management, a 'Green Lane' Bill of Entry means:",
            "opts": [
                "Physical examination required",
                "Document check required",
                "Auto-clearance without examination",
                "Refer to senior officer",
            ],
            "ans": "Auto-clearance without examination",
            "exp": "Green = auto-clearance. Yellow = document check. Red = physical examination.",
        },
    ]

    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q['q']}**")
        sel = st.radio("", q["opts"], key=f"m8_q{i}", index=None, label_visibility="collapsed")
        answers.append((sel, q["ans"], q["exp"]))

    if st.button("✅ Submit Answers — Module 8", type="primary"):
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
            "border-radius:6px;font-size:.9rem;'>← Module 7: Assessment</span>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            "<div style='text-align:center;color:#888;font-size:.85rem;'>"
            "Module 8 of 12 · Customs Act of Bangladesh</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            "<div style='text-align:right;'><span style='background:#2e6da4;color:white;"
            "padding:.4rem 1rem;border-radius:6px;font-size:.9rem;'>"
            "Next → Module 9: Conveyances</span></div>",
            unsafe_allow_html=True,
        )


# ── Main ───────────────────────────────────────────────────────────────────────
sidebar()
hero()

t1, t2, t3 = st.tabs(["📥 Import Procedure", "📤 Export Procedure", "🏭 Warehousing"])
with t1:
    tab_import()
with t2:
    tab_export()
with t3:
    tab_warehousing()

section_checklist()
section_quiz()
nav_footer()