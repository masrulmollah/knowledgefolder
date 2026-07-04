import streamlit as st

# ---------------------------------------------------------------------------
# CSS — matches the visual language of the Homepage / Introduction / Objective pages
# ---------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }
.block-container { padding-top: 1.2rem !important; }

/* ── Hero header ── */
.cn-hero {
    padding: 32px 30px;
    background: linear-gradient(135deg, #0D1B3E 0%, #1B3A6B 100%);
    border-radius: 16px;
    margin-bottom: 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18);
}
.cn-hero-eyebrow {
    font-size: 12px; font-weight: 700; letter-spacing: 1.2px;
    text-transform: uppercase; color: #8FB0F2; margin-bottom: 8px;
}
.cn-hero-title {
    font-size: 28px; font-weight: 800; color: #FFFFFF;
    letter-spacing: -0.4px; margin: 0 0 8px 0; line-height: 1.25;
}
.cn-hero-sub {
    font-size: 14px; color: rgba(255,255,255,0.78);
    max-width: 760px; line-height: 1.65; margin: 0;
}

/* ── Section heading ── */
.cn-section-head {
    display:flex; align-items:center; gap:10px;
    padding:10px 0 8px 2px; margin-top:6px; margin-bottom:16px;
    border-bottom:2.5px solid #E5EAF2;
}
.cn-section-icon { font-size:20px; }
.cn-section-title { font-size:17px; font-weight:800; color:#1B3A6B; letter-spacing:-0.2px; }

/* ── Profile card ── */
.cn-profile-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:16px; padding:26px 28px;
    margin-bottom: 28px;
    border-left: 5px solid #2F5FC4;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
    display:flex; gap:20px; align-items:center; flex-wrap:wrap;
}
.cn-profile-avatar {
    width:74px; height:74px; border-radius:50%;
    background:linear-gradient(135deg,#2F5FC4,#1B3A6B);
    display:flex; align-items:center; justify-content:center;
    font-size:30px; color:#fff; flex-shrink:0;
    box-shadow:0 4px 14px rgba(47,95,196,0.3);
}
.cn-profile-name { font-size:19px; font-weight:800; color:#1a2340; margin-bottom:4px; }
.cn-profile-creds {
    font-size:12.5px; font-weight:700; color:#2F5FC4;
    margin-bottom: 6px; letter-spacing:0.2px;
}
.cn-profile-role { font-size:13px; color:#5b6680; font-weight:500; margin-bottom:10px; }
.cn-profile-desc { font-size:12.5px; color:#5b6680; line-height:1.6; max-width: 640px; }

/* ── Contact channel cards ── */
.cn-channel-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:14px; padding:20px 18px;
    text-align:center; height:100%;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
    transition: box-shadow 0.15s ease, transform 0.15s ease;
}
.cn-channel-icon {
    font-size:26px; margin-bottom:10px;
    width:52px; height:52px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    margin-left:auto; margin-right:auto;
}
.cn-channel-label { font-size:11px; font-weight:700; letter-spacing:0.5px; text-transform:uppercase; color:#9aa3b8; margin-bottom:6px; }
.cn-channel-detail { font-size:14px; font-weight:700; color:#1a2340; margin-bottom:14px; word-break:break-word; }

/* Streamlit link_button styling override to match card aesthetic */
div[data-testid="stMain"] a[data-testid="stBaseLinkButton-secondary"],
div[data-testid="stMain"] div[data-testid="stLinkButton"] > a {
    width:100% !important;
    border-radius:8px !important;
    font-weight:600 !important;
    font-size:12.5px !important;
    border: 1.5px solid #E5EAF2 !important;
    box-shadow:none !important;
    transition: all 0.15s ease !important;
}

/* ── Collaboration cards ── */
.cn-collab-card {
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:14px; padding:20px 20px;
    margin-bottom: 14px;
    border-left: 5px solid;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
    height:100%;
}
.cn-collab-top { display:flex; align-items:center; gap:10px; margin-bottom:8px; }
.cn-collab-icon { font-size:22px; }
.cn-collab-title { font-size:14.5px; font-weight:700; color:#1a2340; }
.cn-collab-desc { font-size:12.5px; color:#5b6680; line-height:1.6; }

/* ── Closing banner ── */
.cn-closing {
    padding: 22px 26px;
    background: #EEF2FA;
    border-left: 5px solid #2F5FC4;
    border-radius: 10px;
    margin-top: 10px;
    margin-bottom: 18px;
    text-align:center;
}
.cn-closing-text {
    font-size: 13.5px; color: #1a2340; line-height: 1.6; font-weight: 500;
}

/* ── Footer note ── */
.cn-footer {
    text-align:center; padding: 18px 0 6px 0;
    font-size:12px; color:#9aa3b8; font-style:italic;
}
</style>
"""

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------
CHANNELS = [
    {
        "icon": "📞", "color": "#16A372", "light": "#EAF6F1",
        "label": "Phone / WhatsApp",
        "detail": "+88 (0)1739573935",
        "action_label": "Call / Message Directly",
        "url": "https://wa.me/8801739573935",
    },
    {
        "icon": "📧", "color": "#2F5FC4", "light": "#EEF2FA",
        "label": "Email",
        "detail": "masrulmollah@gmail.com",
        "action_label": "Send an Email",
        "url": "mailto:masrulmollah@gmail.com",
    },
    {
        "icon": "🌐", "color": "#0EA5E9", "light": "#EAF3FA",
        "label": "Professional Network",
        "detail": "linkedin.com/in/masrulmollah",
        "action_label": "Connect on LinkedIn",
        "url": "https://linkedin.com/in/masrulmollah",
    },
]

COLLABORATIONS = [
    {
        "icon": "📚", "color": "#EA6C1A",
        "title": "Knowledge Sharing",
        "desc": "Contributing articles, interpretations, or case studies on recent changes in Bangladesh Tax, VAT, or IFRS updates.",
    },
    {
        "icon": "🤖", "color": "#0EA5E9",
        "title": "Finance Automation",
        "desc": "Discussing Python, Machine Learning, and Streamlit use-cases tailored specifically for enterprise corporate finance.",
    },
    {
        "icon": "🎓", "color": "#8B5CF6",
        "title": "Talent Development",
        "desc": "Engaging in mentorship or technical training sessions for aspiring finance professionals (CA, CMA, ACCA students).",
    },
]

# ---------------------------------------------------------------------------
# RENDER
# ---------------------------------------------------------------------------
def show():
    st.markdown(CSS, unsafe_allow_html=True)

    # ── Hero ─────────────────────────────────────────────────
    st.markdown("""
    <div class="cn-hero">
        <div class="cn-hero-eyebrow">Contact & Collaboration</div>
        <div class="cn-hero-title">Connect with the Author</div>
        <p class="cn-hero-sub">
            Thank you for visiting the Knowledge Folder. This platform is a continuous, evolving repository
            designed to elevate the standard of financial leadership, regulatory compliance, and digital
            data transformation in Bangladesh. Whether you want to discuss complex accounting standards,
            collaborate on a finance automation project using Python, share feedback on the tools provided,
            or explore corporate training opportunities, your insights are highly valued.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Professional Profile ────────────────────────────────
    st.markdown("""
    <div class="cn-section-head">
        <span class="cn-section-icon">👔</span>
        <span class="cn-section-title">Professional Profile</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cn-profile-card">
        <div class="cn-profile-avatar">👤</div>
        <div>
            <div class="cn-profile-name">Md. Masrul Mollah</div>
            <div class="cn-profile-creds">FCA (ICAB) &nbsp;|&nbsp; ACA (ICAEW) &nbsp;|&nbsp; ACMA, CGMA (CIMA)</div>
            <div class="cn-profile-role">Senior Finance Leader & Tech-Finance Practitioner</div>
            <div class="cn-profile-desc">
                With professional qualifications spanning national and international bodies, Masrul bridges
                the gap between rigid regulatory compliance and forward-looking, data-driven financial
                strategy. His focus lies in transforming traditional finance workflows through automation,
                statistical forecasting, and structural leadership.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Reach Out Directly ───────────────────────────────────
    st.markdown("""
    <div class="cn-section-head">
        <span class="cn-section-icon">📬</span>
        <span class="cn-section-title">Reach Out Directly</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:13px;color:#6b7385;margin-top:-8px;margin-bottom:16px;'>"
        "Feel free to connect through any of the channels below for professional inquiries, "
        "networking, or knowledge sharing.</p>",
        unsafe_allow_html=True
    )

    cols = st.columns(3)
    for i, ch in enumerate(CHANNELS):
        with cols[i]:
            st.markdown(f"""
            <div class="cn-channel-card">
                <div class="cn-channel-icon" style="background:{ch['light']};">{ch['icon']}</div>
                <div class="cn-channel-label">{ch['label']}</div>
                <div class="cn-channel-detail">{ch['detail']}</div>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(ch["action_label"], ch["url"], use_container_width=True)

    st.markdown("<div style='margin-bottom:14px'></div>", unsafe_allow_html=True)

    # ── Areas for Collaboration ──────────────────────────────
    st.markdown("""
    <div class="cn-section-head">
        <span class="cn-section-icon">🤝</span>
        <span class="cn-section-title">Areas for Collaboration</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:13px;color:#6b7385;margin-top:-8px;margin-bottom:16px;'>"
        "We are always looking to expand the depth of this folder. Reach out if you are interested in:</p>",
        unsafe_allow_html=True
    )

    cols2 = st.columns(3)
    for i, c in enumerate(COLLABORATIONS):
        with cols2[i]:
            st.markdown(f"""
            <div class="cn-collab-card" style="border-color:{c['color']};">
                <div class="cn-collab-top">
                    <span class="cn-collab-icon">{c['icon']}</span>
                    <span class="cn-collab-title">{c['title']}</span>
                </div>
                <div class="cn-collab-desc">{c['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Closing note ─────────────────────────────────────────
    st.markdown("""
    <div class="cn-closing">
        <div class="cn-closing-text">
            📩 Whether it's a quick question or a long-term collaboration idea — every message is welcome.
            Let's build a stronger finance community together.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Footer ───────────────────────────────────────────────
    st.markdown("""
    <div class="cn-footer">
        Optimized for professional excellence. Managed by Finance Leaders, for Finance Leaders.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    show()