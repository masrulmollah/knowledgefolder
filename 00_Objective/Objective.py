import streamlit as st

# ---------------------------------------------------------------------------
# CSS — matches the visual language of the Homepage / Introduction pages
# ---------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }
.block-container { padding-top: 1.2rem !important; }

/* ── Hero header ── */
.ob-hero {
    padding: 32px 30px;
    background: linear-gradient(135deg, #0D1B3E 0%, #1B3A6B 100%);
    border-radius: 16px;
    margin-bottom: 22px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18);
}
.ob-hero-eyebrow {
    font-size: 12px; font-weight: 700; letter-spacing: 1.2px;
    text-transform: uppercase; color: #8FB0F2; margin-bottom: 8px;
}
.ob-hero-title {
    font-size: 30px; font-weight: 800; color: #FFFFFF;
    letter-spacing: -0.4px; margin: 0 0 8px 0; line-height: 1.25;
}
.ob-hero-sub {
    font-size: 14.5px; color: rgba(255,255,255,0.78);
    max-width: 760px; line-height: 1.6; margin: 0;
}

/* ── Mandate banner ── */
.ob-mandate {
    padding: 20px 24px;
    background: #EEF2FA;
    border-left: 5px solid #2F5FC4;
    border-radius: 10px;
    margin-bottom: 30px;
}
.ob-mandate-label {
    font-size: 11px; font-weight: 800; letter-spacing: 0.8px;
    text-transform: uppercase; color: #2F5FC4; margin-bottom: 6px;
}
.ob-mandate-text {
    font-size: 14px; color: #1a2340; line-height: 1.6; font-weight: 500;
}

/* ── Section heading ── */
.ob-section-head {
    display:flex; align-items:center; gap:10px;
    padding:10px 0 8px 2px; margin-top:6px; margin-bottom:16px;
    border-bottom:2.5px solid #E5EAF2;
}
.ob-section-icon { font-size:20px; }
.ob-section-title { font-size:17px; font-weight:800; color:#1B3A6B; letter-spacing:-0.2px; }

/* ── Objective pillar card (2x2 grid) ── */
.ob-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:14px; padding:22px 22px 20px 22px;
    margin-bottom: 18px;
    border-top: 5px solid;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
    height: 100%;
}
.ob-card-top { display:flex; align-items:center; gap:12px; margin-bottom:10px; }
.ob-card-num {
    font-size:13px; font-weight:800; color:#FFF;
    width:30px; height:30px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    flex-shrink:0;
}
.ob-card-icon { font-size: 22px; }
.ob-card-title { font-size:15.5px; font-weight:700; color:#1a2340; line-height:1.3; }
.ob-card-intro { font-size:12.5px; color:#5b6680; line-height:1.55; margin-bottom:14px; }

.ob-bullet {
    display:flex; align-items:flex-start; gap:9px;
    margin-bottom:11px;
}
.ob-bullet:last-child { margin-bottom:0; }
.ob-bullet-dot {
    width:7px; height:7px; border-radius:50%;
    flex-shrink:0; margin-top:5px;
}
.ob-bullet-text { font-size:12.5px; color:#3a4566; line-height:1.55; }
.ob-bullet-text b { color:#1a2340; font-weight:700; }

/* ── Philosophy banner ── */
.ob-philosophy {
    padding: 26px 28px;
    background: linear-gradient(135deg, #1B3A6B 0%, #0D1B3E 100%);
    border-radius: 16px;
    margin-top: 8px;
    margin-bottom: 18px;
    text-align: center;
}
.ob-phil-icon { font-size: 26px; margin-bottom: 8px; }
.ob-phil-quote {
    font-size: 18px; font-weight: 800; color: #FFFFFF;
    letter-spacing: -0.2px; margin-bottom: 12px;
}
.ob-phil-text {
    font-size: 13.5px; color: rgba(255,255,255,0.78);
    line-height: 1.65; max-width: 720px; margin: 0 auto;
}
.ob-phil-text b { color: #8FB0F2; font-weight: 700; }

/* ── Three pillars strip under philosophy ── */
.ob-pillar-strip { display:flex; gap:14px; flex-wrap:wrap; margin-bottom: 26px; }
.ob-pillar-chip {
    flex:1; min-width:200px; padding:14px 16px;
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:12px; text-align:center;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.ob-pillar-chip-icon { font-size: 20px; margin-bottom: 4px; }
.ob-pillar-chip-title { font-size:12.5px; font-weight:700; color:#1a2340; }

/* ── Footer note ── */
.ob-footer {
    text-align:center; padding: 18px 0 6px 0;
    font-size:12px; color:#9aa3b8; font-style:italic;
}
</style>
"""

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------
OBJECTIVES = [
    {
        "num": "1",
        "icon": "🎯",
        "color": "#2F5FC4",
        "title": "Bridging the Gap Between Theory and Execution",
        "intro": "Academic definitions and text-book standards often lack the operational nuance required in a fast-paced corporate environment.",
        "bullets": [
            "<b>Actionable Standards</b>: Translate complex International Financial Reporting Standards (IFRS) and Auditing Standards (ISA) into real-world, practical applications tailored for corporate execution.",
            "<b>Local Compliance Mastery</b>: Demystify the intricacies of Bangladeshi fiscal laws — Income Tax Act, VAT and Supplementary Duty Act, Customs Act, and Labor Law — with clear, actionable guides for everyday compliance.",
        ],
    },
    {
        "num": "2",
        "icon": "🤖",
        "color": "#0EA5E9",
        "title": "Driving Digital Transformation in Finance",
        "intro": "The future of finance belongs to professionals who can code, automate, and look forward, not just look backward.",
        "bullets": [
            "<b>The \"Tech-Finance\" Hybrid</b>: Equip traditional accountants with modern digital competencies, encouraging adoption of Python, Machine Learning, and AI inside the finance function.",
            "<b>Automated Intelligence</b>: Move organizations away from rigid, manual spreadsheets toward dynamic, reproducible financial analytics platforms and predictive forecasting models.",
        ],
    },
    {
        "num": "3",
        "icon": "📈",
        "color": "#2E8B57",
        "title": "Developing Visionary Corporate Leaders",
        "intro": "Technical skills alone do not make a CFO. A true leader must understand macroeconomics, strategy, and people.",
        "bullets": [
            "<b>Strategic Capability</b>: Cultivate an advanced understanding of Corporate Strategy, Treasury operations, Foreign Exchange risk management, and Applied Economics.",
            "<b>People & Influence</b>: Provide frameworks for leadership, executive communication, and high-performing team management.",
        ],
    },
    {
        "num": "4",
        "icon": "📚",
        "color": "#EA6C1A",
        "title": "Democratizing Executive-Level Knowledge",
        "intro": "Quality technical knowledge shouldn't be locked behind corporate silos.",
        "bullets": [
            "<b>A Continuous Learning Engine</b>: Offer a structured, open-access repository where aspiring students (CA, CMA, ACCA) can learn directly from the knowledge bases built by seasoned industry practitioners (FCA, ACMA, CIMA).",
            "<b>The Ready Reference Toolkit</b>: Create a central hub of \"Ready References\" — from standard calculation tools to structured templates — speeding up daily workflows and decision-making for finance professionals nationwide.",
        ],
    },
]

PHILOSOPHY_PILLARS = [
    {"icon": "⚖️", "title": "Absolute Integrity through Total Regulatory Compliance"},
    {"icon": "📊", "title": "Sharp Decision-Making powered by Advanced Data Analytics"},
    {"icon": "🧭", "title": "Leadership Capacity to Guide Corporate Strategy"},
]

# ---------------------------------------------------------------------------
# RENDER
# ---------------------------------------------------------------------------
def show():
    st.markdown(CSS, unsafe_allow_html=True)

    # ── Hero ─────────────────────────────────────────────────
    st.markdown("""
    <div class="ob-hero">
        <div class="ob-hero-eyebrow">Our Objectives</div>
        <div class="ob-hero-title">Empowering Finance Leaders, Elevating Standards, and Envisioning the Future</div>
        <p class="ob-hero-sub">
            The financial landscape is changing rapidly. Today's finance professionals are no longer just
            custodians of historical data; they are expected to be strategic business partners, tech-forward
            innovators, and masters of complex local and international regulations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Mandate banner ───────────────────────────────────────
    st.markdown("""
    <div class="ob-mandate">
        <div class="ob-mandate-label">Our Mandate</div>
        <div class="ob-mandate-text">
            The Knowledge Folder was established with a singular, clear mandate: to build a bridge between
            technical expertise, regulatory compliance, and modern data analytics for the finance ecosystem
            in Bangladesh. Our core objectives are structured across four fundamental pillars.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Four Objectives — 2x2 grid ───────────────────────────
    st.markdown("""
    <div class="ob-section-head">
        <span class="ob-section-icon">🧭</span>
        <span class="ob-section-title">Four Fundamental Pillars</span>
    </div>
    """, unsafe_allow_html=True)

    for row_start in range(0, len(OBJECTIVES), 2):
        cols = st.columns(2)
        for i, obj in enumerate(OBJECTIVES[row_start:row_start + 2]):
            bullets_html = "".join(
                f"""<div class="ob-bullet">
                        <span class="ob-bullet-dot" style="background:{obj['color']};"></span>
                        <span class="ob-bullet-text">{b}</span>
                    </div>"""
                for b in obj["bullets"]
            )
            with cols[i]:
                with st.container():
                    st.markdown(f"""
                    <div class="ob-card" style="border-color:{obj['color']};">
                        <div class="ob-card-top">
                            <div class="ob-card-num" style="background:{obj['color']};">{obj['num']}</div>
                            <span class="ob-card-icon">{obj['icon']}</span>
                            <div class="ob-card-title">{obj['title']}</div>
                        </div>
                        <div class="ob-card-intro">{obj['intro']}</div>
                        {bullets_html}
                    </div>
                    """, unsafe_allow_html=True)

    # ── Philosophy ───────────────────────────────────────────
    st.markdown("""
    <div class="ob-section-head">
        <span class="ob-section-icon">🏛️</span>
        <span class="ob-section-title">The Philosophy Driving This Folder</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="ob-philosophy">
        <div class="ob-phil-icon">🏛️</div>
        <div class="ob-phil-quote">"Data-Driven, Regulatory-Compliant, Strategy-Focused."</div>
        <div class="ob-phil-text">
            We believe that a modern finance leader in Bangladesh must stand on three pillars:
            <b>absolute integrity</b> through total regulatory compliance, <b>sharp decision-making</b>
            powered by advanced data analytics, and the <b>leadership capacity</b> to guide corporate
            strategy. This folder exists to cultivate that exact blend of skills.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Three pillars strip ──────────────────────────────────
    chips_html = "".join(
        f"""<div class="ob-pillar-chip">
                <div class="ob-pillar-chip-icon">{p['icon']}</div>
                <div class="ob-pillar-chip-title">{p['title']}</div>
            </div>"""
        for p in PHILOSOPHY_PILLARS
    )
    st.markdown(f'<div class="ob-pillar-strip">{chips_html}</div>', unsafe_allow_html=True)

    # ── Footer ───────────────────────────────────────────────
    st.markdown("""
    <div class="ob-footer">
        Optimized for professional excellence. Managed by Finance Leaders, for Finance Leaders.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show()