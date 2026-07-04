import streamlit as st

# ---------------------------------------------------------------------------
# CSS — matches the visual language of the Homepage / Content Index pages
# ---------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }
.block-container { padding-top: 1.2rem !important; }

/* ── Hero header ── */
.in-hero {
    padding: 32px 30px;
    background: linear-gradient(135deg, #0D1B3E 0%, #1B3A6B 100%);
    border-radius: 16px;
    margin-bottom: 26px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18);
}
.in-hero-eyebrow {
    font-size: 12px; font-weight: 700; letter-spacing: 1.2px;
    text-transform: uppercase; color: #8FB0F2; margin-bottom: 8px;
}
.in-hero-title {
    font-size: 30px; font-weight: 800; color: #FFFFFF;
    letter-spacing: -0.4px; margin: 0 0 8px 0; line-height: 1.25;
}
.in-hero-sub {
    font-size: 14.5px; color: rgba(255,255,255,0.78);
    max-width: 760px; line-height: 1.65; margin: 0;
}

/* ── KPI metric cards ── */
.in-kpi-row { display:flex; gap:14px; flex-wrap:wrap; margin-bottom: 26px; }
.in-kpi-box {
    flex:1; min-width:150px; padding:16px 18px;
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:12px; box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.in-kpi-num { font-size:21px; font-weight:800; color:#1B3A6B; line-height:1.2; }
.in-kpi-lbl { font-size:11.5px; color:#6b7999; font-weight:500; margin-top:3px; }

/* ── Section heading ── */
.in-section-head {
    display:flex; align-items:center; gap:10px;
    padding:10px 0 8px 2px; margin-top:8px; margin-bottom:14px;
    border-bottom:2.5px solid #E5EAF2;
}
.in-section-icon { font-size:20px; }
.in-section-title { font-size:17px; font-weight:800; color:#1B3A6B; letter-spacing:-0.2px; }

/* ── Mission banner ── */
.in-mission {
    padding: 20px 24px;
    background: #EEF2FA;
    border-left: 5px solid #2F5FC4;
    border-radius: 10px;
    margin-bottom: 28px;
}
.in-mission-label {
    font-size: 11px; font-weight: 800; letter-spacing: 0.8px;
    text-transform: uppercase; color: #2F5FC4; margin-bottom: 6px;
}
.in-mission-text {
    font-size: 14px; color: #1a2340; line-height: 1.6; font-weight: 500;
}

/* ── Pillar cards ── */
.in-pillar-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:14px; padding:18px 20px;
    margin-bottom: 14px;
    border-left: 5px solid;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.in-pillar-top { display:flex; align-items:center; gap:10px; margin-bottom:8px; }
.in-pillar-num {
    font-size:11px; font-weight:800; color:#FFF;
    width:24px; height:24px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    flex-shrink:0;
}
.in-pillar-title { font-size:15px; font-weight:700; color:#1a2340; }
.in-pillar-desc { font-size:12.5px; color:#5b6680; line-height:1.55; margin-bottom:10px; }
.in-pillar-tags { display:flex; flex-wrap:wrap; gap:6px; }
.in-pillar-tag {
    font-size:11px; font-weight:600; padding:3px 10px;
    border-radius:20px; background:rgba(0,0,0,0.045); color:#3a4566;
}

/* ── Audience cards ── */
.in-aud-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:12px; padding:16px 18px;
    height: 100%;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.in-aud-icon { font-size:24px; margin-bottom:6px; }
.in-aud-title { font-size:13.5px; font-weight:700; color:#1a2340; margin-bottom:5px; }
.in-aud-desc { font-size:12px; color:#6b7385; line-height:1.5; }

/* ── Navigation guide ── */
.in-nav-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:12px; padding:15px 18px;
    display:flex; align-items:flex-start; gap:12px;
    margin-bottom:10px;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.in-nav-icon { font-size:20px; flex-shrink:0; margin-top:1px; }
.in-nav-q { font-size:13px; font-weight:700; color:#1a2340; margin-bottom:2px; }
.in-nav-a { font-size:12.5px; color:#5b6680; }
.in-nav-a b { color:#2F5FC4; }

/* ── Footer note ── */
.in-footer {
    text-align:center; padding: 22px 0 6px 0;
    font-size:12px; color:#9aa3b8; font-style:italic;
}
</style>
"""

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------
PILLARS = [
    {
        "title": "Legal Aspects & Compliance",
        "icon_color": "#2F5FC4",
        "desc": "Navigating the regulatory landscape of Bangladesh with precise, up-to-date interpretations.",
        "tags": ["Income Tax", "VAT", "Customs Act", "Company Act", "Labor Law", "Transfer Pricing"],
    },
    {
        "title": "Analytical & Statistical Skills",
        "icon_color": "#16A372",
        "desc": "Empowering finance professionals to transition from traditional accounting to forward-looking predictive analytics.",
        "tags": ["Data Analytics", "Financial Modeling", "Statistics"],
    },
    {
        "title": "Professional Subjects",
        "icon_color": "#8B5CF6",
        "desc": "Core academic and professional bodies of knowledge required to master the language of business.",
        "tags": ["IFRS", "ISA", "Management Accounting", "Corporate Finance", "Treasury"],
    },
    {
        "title": "Applied Knowledge & Digital Skills",
        "icon_color": "#0EA5E9",
        "desc": "Where financial expertise meets modern technology to automate workflows and drive efficiency.",
        "tags": ["Applied Accounting Standards", "Python", "Machine Learning", "AI"],
    },
    {
        "title": "Corporate Strategy & Leadership",
        "icon_color": "#2E8B57",
        "desc": "Elevating technical accountants into strategic business partners and visionary leaders.",
        "tags": ["Economics", "Foreign Exchange", "Strategy", "Leadership"],
    },
    {
        "title": "Special Collections & Ready Reference",
        "icon_color": "#EA6C1A",
        "desc": "Your daily operational toolkit and continuous learning library.",
        "tags": ["Books Collection", "Talent Pool", "Blogs", "Calculators", "Tax Returns"],
    },
]

AUDIENCES = [
    {"icon": "👔", "title": "Executive Leadership",
     "desc": "CFOs & Finance Directors — for strategic decision-making, treasury management, and high-level regulatory compliance."},
    {"icon": "🧾", "title": "Qualified Professionals",
     "desc": "A ready-reckoner for daily complex treatments of VAT, Tax, and IFRS/ISA."},
    {"icon": "🎓", "title": "Aspiring Professionals",
     "desc": "CA, CMA, ACCA students — a structured learning path bridging academic theory with real-world application."},
    {"icon": "📊", "title": "Data-Driven Analysts",
     "desc": "Finance professionals integrating Python, SQL, and ML into reporting and forecasting."},
]

NAV_GUIDE = [
    {"icon": "⚖️", "q": "Need a compliance check?", "a": "Head over to <b>Legal Aspects</b>."},
    {"icon": "🤖", "q": "Want to automate a manual report?", "a": "Dive into <b>Digital Skills</b>."},
    {"icon": "📚", "q": "Studying for an upcoming board paper?", "a": "Explore <b>Professional Subjects</b>."},
]

KPIS = [
    {"num": "9", "lbl": "Knowledge Pillars"},
    {"num": "25+", "lbl": "Modules Available"},
    {"num": "FCA · ACMA · CIMA", "lbl": "Target Audience"},
    {"num": "Tech + Finance", "lbl": "Core Focus"},
]

# ---------------------------------------------------------------------------
# RENDER
# ---------------------------------------------------------------------------
def show():
    st.markdown(CSS, unsafe_allow_html=True)

    # ── Hero ─────────────────────────────────────────────────
    st.markdown("""
    <div class="in-hero">
        <div class="in-hero-eyebrow">Welcome to the Knowledge Folder</div>
        <div class="in-hero-title">The Professional Repository for Finance Leaders</div>
        <p class="in-hero-sub">
            A curated hub designed specifically for Finance, Accounting, and Business leaders in Bangladesh.
            In an era where financial regulations evolve rapidly and data-driven decision-making is paramount,
            this repository serves as your definitive guide — whether you are a seasoned CFO navigating complex
            compliance, an entrepreneur scaling a business, or an aspiring student aiming to join the ranks of
            qualified professionals (FCA, ACMA, CIMA).
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── KPI row ──────────────────────────────────────────────
    kpi_html = "".join(
        f"""<div class="in-kpi-box">
                <div class="in-kpi-num">{k['num']}</div>
                <div class="in-kpi-lbl">{k['lbl']}</div>
            </div>"""
        for k in KPIS
    )
    st.markdown(f'<div class="in-kpi-row">{kpi_html}</div>', unsafe_allow_html=True)

    # ── Mission ──────────────────────────────────────────────
    st.markdown("""
    <div class="in-mission">
        <div class="in-mission-label">Our Mission</div>
        <div class="in-mission-text">
            Translating complexity into actionable corporate strategy. We bridge the gap between theoretical
            frameworks, local regulatory compliance, and cutting-edge data science.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Core Knowledge Pillars ──────────────────────────────
    st.markdown("""
    <div class="in-section-head">
        <span class="in-section-icon">🏛️</span>
        <span class="in-section-title">Core Knowledge Pillars</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:13px;color:#6b7385;margin-top:-8px;margin-bottom:16px;'>"
        "The repository is structured into six foundational pillars to streamline your professional "
        "development and daily operational execution.</p>",
        unsafe_allow_html=True
    )

    cols = st.columns(2)
    for i, p in enumerate(PILLARS):
        tags_html = "".join(f'<span class="in-pillar-tag">{t}</span>' for t in p["tags"])
        with cols[i % 2]:
            st.markdown(f"""
            <div class="in-pillar-card" style="border-color:{p['icon_color']};">
                <div class="in-pillar-top">
                    <div class="in-pillar-num" style="background:{p['icon_color']};">{i+1}</div>
                    <div class="in-pillar-title">{p['title']}</div>
                </div>
                <div class="in-pillar-desc">{p['desc']}</div>
                <div class="in-pillar-tags">{tags_html}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Who is this for ─────────────────────────────────────
    st.markdown("""
    <div class="in-section-head">
        <span class="in-section-icon">🎯</span>
        <span class="in-section-title">Who Is This For?</span>
    </div>
    """, unsafe_allow_html=True)

    cols2 = st.columns(4)
    for i, a in enumerate(AUDIENCES):
        with cols2[i]:
            st.markdown(f"""
            <div class="in-aud-card">
                <div class="in-aud-icon">{a['icon']}</div>
                <div class="in-aud-title">{a['title']}</div>
                <div class="in-aud-desc">{a['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom:24px'></div>", unsafe_allow_html=True)

    # ── How to navigate ──────────────────────────────────────
    st.markdown("""
    <div class="in-section-head">
        <span class="in-section-icon">🚀</span>
        <span class="in-section-title">How to Navigate the Folder</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:13px;color:#6b7385;margin-top:-8px;margin-bottom:14px;'>"
        "Use the sidebar navigation to explore our modules. We recommend starting based on your immediate need:</p>",
        unsafe_allow_html=True
    )

    for n in NAV_GUIDE:
        st.markdown(f"""
        <div class="in-nav-card">
            <div class="in-nav-icon">{n['icon']}</div>
            <div>
                <div class="in-nav-q">{n['q']}</div>
                <div class="in-nav-a">{n['a']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Connect & Collaborate ───────────────────────────────
    st.markdown("""
    <div class="in-section-head">
        <span class="in-section-icon">📬</span>
        <span class="in-section-title">Connect & Collaborate</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="in-mission" style="border-color:#16A372;background:#EAF6F1;">
        <div class="in-mission-text" style="color:#1a2340;">
            This folder is a living, breathing repository that evolves with industry changes. Explore the
            <b>Team</b> and <b>Contact</b> pages to share feedback, contribute to the content, or discuss
            corporate training collaborations.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Footer ───────────────────────────────────────────────
    st.markdown("""
    <div class="in-footer">
        Optimized for professional excellence. Managed by Finance Leaders, for Finance Leaders.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show()