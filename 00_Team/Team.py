import streamlit as st

# ---------------------------------------------------------------------------
# CSS — matches the visual language of the Homepage / Introduction / Objective / Contact pages
# ---------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }
.block-container { padding-top: 1.2rem !important; }

/* ── Hero header ── */
.tm-hero {
    padding: 32px 30px;
    background: linear-gradient(135deg, #0D1B3E 0%, #1B3A6B 100%);
    border-radius: 16px;
    margin-bottom: 26px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18);
}
.tm-hero-eyebrow {
    font-size: 12px; font-weight: 700; letter-spacing: 1.2px;
    text-transform: uppercase; color: #8FB0F2; margin-bottom: 8px;
}
.tm-hero-title {
    font-size: 28px; font-weight: 800; color: #FFFFFF;
    letter-spacing: -0.4px; margin: 0 0 8px 0; line-height: 1.25;
}
.tm-hero-sub {
    font-size: 14px; color: rgba(255,255,255,0.78);
    max-width: 780px; line-height: 1.65; margin: 0;
}

/* ── Section heading ── */
.tm-section-head {
    display:flex; align-items:center; gap:10px;
    padding:10px 0 8px 2px; margin-top:6px; margin-bottom:16px;
    border-bottom:2.5px solid #E5EAF2;
}
.tm-section-icon { font-size:20px; }
.tm-section-title { font-size:17px; font-weight:800; color:#1B3A6B; letter-spacing:-0.2px; }

/* ── Team member card ── */
.tm-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:16px; padding:24px 26px;
    margin-bottom: 18px;
    border-left: 5px solid;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.tm-card-top { display:flex; align-items:flex-start; gap:16px; margin-bottom:14px; flex-wrap:wrap; }
.tm-avatar {
    width:62px; height:62px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:26px; color:#fff; flex-shrink:0;
    box-shadow:0 4px 14px rgba(0,0,0,0.18);
}
.tm-name { font-size:17.5px; font-weight:800; color:#1a2340; line-height:1.3; margin-bottom:3px; }
.tm-creds { font-size:12px; font-weight:700; letter-spacing:0.2px; margin-bottom:5px; }
.tm-role {
    display:inline-block; font-size:11.5px; font-weight:700;
    padding:3px 11px; border-radius:20px; margin-top:2px;
}

.tm-block-label {
    font-size:11px; font-weight:800; letter-spacing:0.6px; text-transform:uppercase;
    color:#9aa3b8; margin:14px 0 5px 0;
}
.tm-block-text { font-size:12.5px; color:#3a4566; line-height:1.65; }
.tm-block-text b { color:#1a2340; }

.tm-milestone {
    margin-top: 14px; padding: 12px 14px;
    border-radius: 10px;
    font-size: 12px; color:#1a2340; line-height:1.6;
}
.tm-milestone-label {
    font-size: 10.5px; font-weight:800; letter-spacing:0.6px; text-transform:uppercase;
    margin-bottom: 4px;
}

/* ── Combined strength banner ── */
.tm-strength {
    padding: 22px 26px;
    background: #EEF2FA;
    border-left: 5px solid #2F5FC4;
    border-radius: 10px;
    margin-top: 8px;
    margin-bottom: 18px;
}
.tm-strength-label {
    font-size: 11px; font-weight: 800; letter-spacing: 0.8px;
    text-transform: uppercase; color: #2F5FC4; margin-bottom: 6px;
}
.tm-strength-text {
    font-size: 13.5px; color: #1a2340; line-height: 1.65; font-weight: 500;
}

/* ── Footer note ── */
.tm-footer {
    text-align:center; padding: 18px 0 6px 0;
    font-size:12px; color:#9aa3b8; font-style:italic;
}
</style>
"""

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------
TEAM = [
    {
        "icon": "🛡️",
        "color": "#2F5FC4",
        "light": "#EEF2FA",
        "name": "Md. Masrul Mollah",
        "creds": "FCA (ICAB) &nbsp;|&nbsp; ACA (ICAEW) &nbsp;|&nbsp; ACMA, CGMA (CIMA)",
        "role": "Founder & Tech-Finance Lead",
        "background": "Over 14 years of premier finance leadership experience, including 4.3 years at KPMG and 10 years at Unilever. He currently drives high-volume financial operations as the Head of Factory Finance at Unilever Bangladesh.",
        "focus": "Strategic financial planning &amp; analysis (FP&amp;A), corporate governance, capital investment modeling, and supply chain cost structures.",
        "extra_label": "Digital Frontier",
        "extra": "Specialized in bridging traditional corporate finance with modern Data Science, utilizing Python and PowerBI to build predictive algorithms, process automations, and advanced MIS platforms.",
    },
    {
        "icon": "🏛️",
        "color": "#16A372",
        "light": "#EAF6F1",
        "name": "Md. Kamruzzaman",
        "creds": "FCA",
        "role": "Co-Lead — Taxation, Compliance & Accounts",
        "background": "A highly decorated tax and compliance expert with over 17 years of experience. His career spans 9 years across top-tier listed accountancy firms (including serving as Assistant Manager at KPMG Bangladesh) and over 8 years as the Head of Function for Pendekar Energy Limited.",
        "focus": "Corporate taxation, direct/indirect tax litigations, treasury management, and structural cross-border transaction advisory.",
        "extra_label": "Key Milestones",
        "extra": "Recipient of the Excellent Financial Staff Award (2024) under CGN Energy International and successfully secured billions in BDT cash tax savings through strategic appeals and alternative dispute resolutions (ADR).",
    },
    {
        "icon": "📊",
        "color": "#8B5CF6",
        "light": "#F3EEF9",
        "name": "Md. Enamul Haque",
        "creds": "Assistant Officer",
        "role": "Tax & Advisory Services",
        "background": "An intensive compliance practitioner with extensive hands-on experience in the Tax and Advisory department of Rahman Rahman Huq (KPMG Bangladesh).",
        "focus": "End-to-end execution of operational taxation, including Advance Income Tax (AIT), Withholding Tax (WHT), and Withholding VAT (WHVAT).",
        "extra_label": "Key Milestones",
        "extra": "Specializes in processing annual corporate tax returns, resolving regulatory audit queries, managing government treasury deposits, and handling tax compliance portfolios for a massive array of global multinational corporations.",
    },
]

# ---------------------------------------------------------------------------
# RENDER
# ---------------------------------------------------------------------------
def show():
    st.markdown(CSS, unsafe_allow_html=True)

    # ── Hero ─────────────────────────────────────────────────
    st.markdown("""
    <div class="tm-hero">
        <div class="tm-hero-eyebrow">Meet the Team</div>
        <div class="tm-hero-title">The Experts Behind the Knowledge Folder</div>
        <p class="tm-hero-sub">
            The Knowledge Folder is built and managed by seasoned finance practitioners who combine deep
            institutional expertise in corporate finance, advanced taxation, and digital analytics. Our team
            leverages collective experience from "Big Four" auditing firms and global multinational giants
            to deliver actionable, enterprise-grade insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Team members ─────────────────────────────────────────
    st.markdown("""
    <div class="tm-section-head">
        <span class="tm-section-icon">👥</span>
        <span class="tm-section-title">Leadership & Expertise</span>
    </div>
    """, unsafe_allow_html=True)

    for member in TEAM:
        card_html = (
            f'<div class="tm-card" style="border-color:{member["color"]};">'
            f'<div class="tm-card-top">'
            f'<div class="tm-avatar" style="background:linear-gradient(135deg,{member["color"]},{member["color"]}cc);">'
            f'{member["icon"]}'
            f'</div>'
            f'<div>'
            f'<div class="tm-name">{member["name"]}</div>'
            f'<div class="tm-creds" style="color:{member["color"]};">{member["creds"]}</div>'
            f'<span class="tm-role" style="background:{member["light"]};color:{member["color"]};">'
            f'{member["role"]}'
            f'</span>'
            f'</div>'
            f'</div>'
            f'<div class="tm-block-label">Background</div>'
            f'<div class="tm-block-text">{member["background"]}</div>'
            f'<div class="tm-block-label">Core Focus</div>'
            f'<div class="tm-block-text">{member["focus"]}</div>'
            f'<div class="tm-milestone" style="background:{member["light"]};">'
            f'<div class="tm-milestone-label" style="color:{member["color"]};">{member["extra_label"]}</div>'
            f'{member["extra"]}'
            f'</div>'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    # ── Combined Strength ────────────────────────────────────
    st.markdown("""
    <div class="tm-section-head">
        <span class="tm-section-icon">🤝</span>
        <span class="tm-section-title">Our Combined Strength</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tm-strength">
        <div class="tm-strength-label">United by Purpose</div>
        <div class="tm-strength-text">
            By merging global corporate practices with localized tactical compliance and modern data
            analytics, our team ensures the Knowledge Folder remains the ultimate repository for
            high-performing finance leaders across Bangladesh.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Footer ───────────────────────────────────────────────
    st.markdown("""
    <div class="tm-footer">
        Optimized for professional excellence. Managed by Finance Leaders, for Finance Leaders.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show()