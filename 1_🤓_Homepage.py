import streamlit as st
import os
import importlib.util

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Knowledge Folder",
    page_icon="📁",
    layout="wide"
)

# ---------------------------------------------------------------------------
# BUCKET + TOPIC ICON DEFINITIONS
# ---------------------------------------------------------------------------
BUCKETS = {
    "🏛️ Home": {
        "light": "#EEF2FA",
        "accent": "#2F5FC4",
        "topics": {
            "Introduction":       "🫥",
            "Objective":              "🎯",
            "Team":      "👷",
            "Content":      "🏛️",
            "Contact":        "👷",
        },
    },

    "⚖️ Legal Aspects": {
        "light": "#EEF2FA",
        "accent": "#2F5FC4",
        "topics": {
            "Income Tax":       "🧾",
            "VAT":              "🏷️",
            "Customs Act":      "🛃",
            "Company Act":      "🏛️",
            "Labor Law":        "👷",
            "Transfer Pricing": "🔄",
        },
    },
    "📊 Analytical Skills": {
        "light": "#EAF6F1",
        "accent": "#16A372",
        "topics": {
            "Data Analytics":               "📈",
            "Data Analysis Skills":         "🔍",
            "Complete Financial Analytics": "💹",
            "Statistics":                   "📉",
        },
    },
    "🎓 Professional Subjects": {
        "light": "#F3EEF9",
        "accent": "#8B5CF6",
        "topics": {
            "Accounting":                   "🧮",
            "Finance":                      "💰",
            "Auditing Standards":           "🔎",
            "Management Accounting":        "📋",
            "Corporate Finance & Treasury": "🏦",
        },
    },
    "🧩 Applied Knowledge": {
        "light": "#FCEFF3",
        "accent": "#C2185B",
        "topics": {
            "Applied Accounting Standards": "📐",
            "Applied Machine Learning": "🖥️",
            "Applied Data Visualization": "📈",
            "Applied Data Analytics": "🔎",	    
        },
    },
    "💻 Digital Skills": {
        "light": "#EAF3FA",
        "accent": "#0EA5E9",
        "topics": {
            "Python":                  "🐍",
            "Machine Learning":        "🤖",
            "Artificial Intelligence": "🧠",
        },
    },
    "📚 Special Collections": {
        "light": "#FDF3EC",
        "accent": "#EA6C1A",
        "topics": {
            "Books Collection": "📖",
            "Talent Pool":      "🌟",
            "Blogs":            "✍️",
        },
    },
    "🔖 Ready Reference": {
        "light": "#FDF8EE",
        "accent": "#D4A017",
        "topics": {
            "My Calculations":        "🧮",
            "Translating Complexity": "🗺️",
	    "Financial Statements": "📖",
	    "Tax Returns": "📝",

        },
    },
    "🧭 Corporate Strategy & Leadership": {
        "light": "#F0FAF4",
        "accent": "#2E8B57",
        "topics": {
            "Foreign Exchange":  "💱",
            "Economics":         "🌐",
            "Leadership":        "🧭",
            "Business Strategy": "♟️",
            "Home":              "🏠",
        },
    },
}

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def clean_label(folder_name: str) -> str:
    label = folder_name.split('_', 1)[-1] if '_' in folder_name else folder_name
    return label.replace('_', ' ').strip()

def fuzzy_match(a: str, b: str) -> bool:
    return a.strip().lower() == b.strip().lower()

def build_folder_map(root_dir: str, ignore_list: list) -> dict:
    items = sorted(os.listdir(root_dir))
    folders = [f for f in items if os.path.isdir(os.path.join(root_dir, f)) and f not in ignore_list]
    return {clean_label(f): f for f in folders}

def assign_buckets(folder_map: dict) -> dict:
    bucket_topics: dict = {b: [] for b in BUCKETS}
    bucket_topics["🧭 Corporate Strategy & Leadership"] = []  # fallback bucket
    for folder_label, folder_name in folder_map.items():
        matched_bucket, matched_icon = None, "📄"
        for bucket_name, meta in BUCKETS.items():
            for topic_name, icon in meta["topics"].items():
                if fuzzy_match(folder_label, topic_name):
                    matched_bucket, matched_icon = bucket_name, icon
                    break
            if matched_bucket:
                break
        if not matched_bucket:
            for bucket_name, meta in BUCKETS.items():
                for topic_name, icon in meta["topics"].items():
                    if topic_name.lower() in folder_label.lower() or folder_label.lower() in topic_name.lower():
                        matched_bucket, matched_icon = bucket_name, icon
                        break
                if matched_bucket:
                    break
        target = matched_bucket if matched_bucket else "🧭 Corporate Strategy & Leadership"
        bucket_topics[target].append((folder_label, matched_icon, folder_name))
    return bucket_topics

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }
.block-container { padding-top: 1.2rem !important; }

/* ── Homepage header ── */
.kf-header {
    display:flex; align-items:center; gap:14px;
    padding:18px 24px;
    background:linear-gradient(135deg,#0D1B3E 0%,#1B3A6B 100%);
    border-radius:14px; margin-bottom:24px;
    box-shadow:0 4px 20px rgba(0,0,0,0.18);
}
.kf-header-icon  { font-size:36px; }
.kf-header-title { font-size:26px; font-weight:700; color:#FFF; letter-spacing:-0.3px; margin:0; }
.kf-header-sub   { font-size:13px; color:rgba(255,255,255,0.6); margin:2px 0 0 0; }

/* ── Section row divider ── */
.section-label {
    display:flex; align-items:center; gap:10px;
    padding:10px 0 8px 2px; margin-top:12px; margin-bottom:6px;
    border-bottom:2px solid;
}
.section-label-text { font-size:13px; font-weight:700; letter-spacing:0.7px; text-transform:uppercase; }

/* ── Topic card buttons — uniform fixed size ── */
div[data-testid="stMain"] div[data-testid="stButton"] > button {
    width: 100% !important;
    height: 110px !important;
    min-height: 110px !important;
    max-height: 110px !important;
    background: #FFFFFF !important;
    border: 1.5px solid #E5EAF2 !important;
    border-radius: 12px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
    padding: 12px 8px !important;
    cursor: pointer !important;
    color: #1a2340 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    line-height: 1.35 !important;
    white-space: pre-wrap !important;
    word-break: break-word !important;
    overflow: hidden !important;
    transition: box-shadow 0.15s ease, border-color 0.15s ease, transform 0.15s ease !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 4px !important;
    text-align: center !important;
}
div[data-testid="stMain"] div[data-testid="stButton"] > button:hover {
    border-color: #99aacc !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.11) !important;
    transform: translateY(-2px) !important;
    background: #FAFBFF !important;
    color: #1a2340 !important;
}
div[data-testid="stMain"] div[data-testid="stButton"] > button:focus {
    box-shadow: 0 0 0 2px rgba(47,95,196,0.2) !important;
    outline: none !important;
}

/* ── Placeholder card (no folder yet) — same size as real cards ── */
.topic-card-placeholder {
    width: 100%;
    height: 110px;
    min-height: 110px;
    max-height: 110px;
    background: repeating-linear-gradient(135deg, #FAFAFA, #FAFAFA 10px, #F3F3F3 10px, #F3F3F3 20px);
    border: 1.5px dashed #D0D5DD;
    border-radius: 12px;
    padding: 12px 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    text-align: center;
    opacity: 0.85;
    cursor: not-allowed;
}
.ph-icon  { font-size: 22px; filter: grayscale(60%); opacity: 0.7; }
.ph-label { font-size: 12px; font-weight: 600; color: #6b7280; line-height: 1.3; }
.ph-tag   {
    font-size: 9.5px; font-weight: 700; letter-spacing: 0.4px; text-transform: uppercase;
    color: #9aa3b2; background: #ECEEF1; padding: 2px 8px; border-radius: 8px; margin-top: 2px;
}

/* ── Topic page header ── */
.topic-header {
    display:flex; align-items:center; gap:12px;
    padding:14px 20px; border-radius:12px; margin-bottom:20px;
    box-shadow:0 2px 10px rgba(0,0,0,0.08);
}
.topic-header-icon  { font-size:30px; }
.topic-header-title { font-size:20px; font-weight:700; color:#FFF; margin:0; }
.topic-header-sub   { font-size:12px; color:rgba(255,255,255,0.7); margin:2px 0 0 0; }

/* ── Sidebar ── */
[data-testid="stSidebar"] { background:#F7F9FC !important; }

/* Home button in sidebar — always fully visible */
div[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    position: relative !important;
    opacity: 1 !important;
    width: 100% !important;
    background: linear-gradient(135deg,#0D1B3E,#1B3A6B) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 10px 16px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    cursor: pointer !important;
    height: auto !important;
    overflow: visible !important;
}
div[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    opacity: 0.92 !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.22) !important;
}
</style>
"""

# ---------------------------------------------------------------------------
# HOMEPAGE VIEW
# ---------------------------------------------------------------------------

def show_homepage(bucket_topics: dict):
    st.markdown("""
    <div class="kf-header">
        <div class="kf-header-icon">📁</div>
        <div>
            <div class="kf-header-title">Knowledge Folder</div>
            <div class="kf-header-sub">Your curated library of professional knowledge — click any topic to open it</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    all_buckets = list(BUCKETS.items())

    for bucket_name, meta in all_buckets:
        accent = meta["accent"]
        light  = meta["light"]

        # Topics that DO have a matching folder on disk
        found_topics = {label: (icon, folder_name) for label, icon, folder_name in bucket_topics.get(bucket_name, [])}

        # Build the full display list: every topic defined in BUCKETS for this
        # section, using the real folder if found, else a placeholder.
        display_topics = []
        for topic_name, default_icon in meta["topics"].items():
            # Try exact match first, then a loose contains-match against found folders
            match = None
            if topic_name in found_topics:
                match = found_topics[topic_name]
            else:
                for flabel, (ficon, ffolder) in found_topics.items():
                    if topic_name.lower() in flabel.lower() or flabel.lower() in topic_name.lower():
                        match = (ficon, ffolder)
                        break
            if match:
                display_topics.append((topic_name, match[0], match[1]))
            else:
                display_topics.append((topic_name, default_icon, None))  # None = not yet created

        st.markdown(f"""
        <div class="section-label" style="border-color:{accent};">
            <span class="section-label-text" style="color:{accent};">{bucket_name}</span>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(min(len(display_topics), 8))
        for i, (label, icon, folder_name) in enumerate(display_topics):
            with cols[i]:
                if folder_name is not None:
                    # Single button styled as a card — no duplicate HTML element
                    if st.button(
                        f"{icon}\n\n{label}",
                        key=f"nav_{bucket_name}_{label}",
                        use_container_width=True,
                        help=f"Open {label}"
                    ):
                        st.session_state.view          = "topic"
                        st.session_state.active_label  = label
                        st.session_state.active_folder = folder_name
                        st.session_state.active_icon   = icon
                        st.session_state.active_accent = accent
                        st.session_state.active_light  = light
                        st.rerun()
                else:
                    # Placeholder card for topics with no matching folder yet
                    st.markdown(f"""
                    <div class="topic-card-placeholder" title="Folder not created yet">
                        <div class="ph-icon">{icon}</div>
                        <div class="ph-label">{label}</div>
                        <div class="ph-tag">Coming soon</div>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom:4px'></div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# TOPIC PAGE VIEW
# ---------------------------------------------------------------------------

def show_topic_page(root_dir: str):
    label  = st.session_state.active_label
    folder = st.session_state.active_folder
    icon   = st.session_state.active_icon
    accent = st.session_state.active_accent
    light  = st.session_state.active_light

    block_path = os.path.join(root_dir, folder)

    if not os.path.isdir(block_path):
        st.error(f"Folder not found: `{block_path}`")
        return

    subpages = sorted([f for f in os.listdir(block_path) if f.endswith('.py')])
    if not subpages:
        st.info(f"No pages found in **{label}**.")
        return

    # Build sub-page name → filename map
    page_names = {}
    for f in subpages:
        name = f.split('_', 1)[-1].replace('.py', '').replace('_', ' ') if '_' in f else f.replace('.py', '')
        page_names[name] = f

    # ── Sidebar ──────────────────────────────────────────────
    # "Back to Homepage" at the very top
    if st.sidebar.button("🏠  Back to Homepage", key="go_home", use_container_width=True):
        st.session_state.view = "home"
        st.rerun()
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### {icon} {label}")
    st.sidebar.markdown("---")
    selected_subpage = st.sidebar.selectbox("Select Topic", options=list(page_names.keys()))

    # ── Topic header (instead of homepage header) ─────────────
    st.markdown(f"""
    <div class="topic-header"
         style="background:linear-gradient(135deg,{accent} 0%,{accent}bb 100%);">
        <div class="topic-header-icon">{icon}</div>
        <div>
            <div class="topic-header-title">{label}</div>
            <div class="topic-header-sub">📁 Knowledge Folder</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if not selected_subpage:
        return

    # ── Load & execute the sub-page module ───────────────────
    file_to_load = os.path.join(block_path, page_names[selected_subpage])
    try:
        spec   = importlib.util.spec_from_file_location("dynamic_module", file_to_load)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "show"):
            module.show()
        else:
            st.error("This module does not have a `show()` function.")
    except Exception as e:
        st.error("### ❌ Page Error")
        st.exception(e)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    # Session-state defaults
    for k, v in {
        "view":          "home",
        "active_label":  None,
        "active_folder": None,
        "active_icon":   "📄",
        "active_accent": "#1B3A6B",
        "active_light":  "#EEF2FA",
    }.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # Filesystem scan
    root_dir = os.getcwd()
    ignore_list = [
        '__pycache__', '.git', '.streamlit', 'venv',
        '1_🤓_Homepage.py', 'main.py', 'requirements.txt', 'credentials.json'
    ]
    folder_map    = build_folder_map(root_dir, ignore_list)
    bucket_topics = assign_buckets(folder_map)

    # Inject CSS
    st.markdown(CSS, unsafe_allow_html=True)

    # Sidebar hint on homepage
    if st.session_state.view == "home":
        st.sidebar.markdown("## 📁 Knowledge Folder")
        st.sidebar.markdown("---")
        st.sidebar.markdown("Select a topic from the main page to begin.")

    # Route to the correct view
    if st.session_state.view == "topic" and st.session_state.active_folder:
        show_topic_page(root_dir)
    else:
        st.session_state.view = "home"
        show_homepage(bucket_topics)


if __name__ == "__main__":
    main()