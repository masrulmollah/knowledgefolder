import streamlit as st
import os

# ---------------------------------------------------------------------------
# BUCKET DEFINITIONS  — icons & colours only; subtopics come from disk
# ---------------------------------------------------------------------------
BUCKETS = {
    "⚖️ Legal Aspects": {
        "accent": "#2F5FC4", "light": "#EEF2FA",
        "topics": {
            "Income Tax": "🧾", "VAT": "🏷️", "Customs Act": "🛃",
            "Company Act": "🏛️", "Labor Law": "👷", "Transfer Pricing": "🔄",
        },
    },
    "📊 Analytical Skills": {
        "accent": "#16A372", "light": "#EAF6F1",
        "topics": {
            "Data Analytics": "📈", "Data Analysis Skills": "🔍",
            "Complete Financial Analytics": "💹", "Statistics": "📉",
        },
    },
    "🎓 Professional Subjects": {
        "accent": "#8B5CF6", "light": "#F3EEF9",
        "topics": {
            "Accounting": "🧮", "Finance": "💰", "Auditing Standards": "🔎",
            "Management Accounting": "📋", "Corporate Finance & Treasury": "🏦",
        },
    },
    "🧩 Applied Knowledge": {
        "accent": "#C2185B", "light": "#FCEFF3",
        "topics": {
            "Applied Accounting Standards": "📐",
        },
    },
    "💻 Digital Skills": {
        "accent": "#0EA5E9", "light": "#EAF3FA",
        "topics": {
            "Python": "🐍", "Machine Learning": "🤖", "Artificial Intelligence": "🧠",
        },
    },
    "📚 Special Collections": {
        "accent": "#EA6C1A", "light": "#FDF3EC",
        "topics": {
            "Books Collection": "📖", "Talent Pool": "🌟", "Blogs": "✍️",
        },
    },
    "🔖 Ready Reference": {
        "accent": "#D4A017", "light": "#FDF8EE",
        "topics": {
            "My Calculations": "🧮", "Translating Complexity": "🗺️",
            "Financial Statements": "📖", "Tax Returns": "📝",
        },
    },
    "🧭 Corporate Strategy & Leadership": {
        "accent": "#2E8B57", "light": "#F0FAF4",
        "topics": {
            "Foreign Exchange": "💱", "Economics": "🌐",
            "Leadership": "🧭", "Business Strategy": "♟️",
        },
    },
}

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', 'Segoe UI', sans-serif; }
.block-container { padding-top: 1.2rem !important; }

/* ── Page header ── */
.ct-header {
    display:flex; align-items:center; gap:16px;
    padding:20px 28px;
    background:linear-gradient(135deg,#0D1B3E 0%,#1B3A6B 100%);
    border-radius:14px; margin-bottom:24px;
    box-shadow:0 4px 20px rgba(0,0,0,0.18);
}
.ct-header-icon  { font-size:38px; }
.ct-header-title { font-size:26px; font-weight:800; color:#FFF; letter-spacing:-0.3px; margin:0; }
.ct-header-sub   { font-size:13px; color:rgba(255,255,255,0.6); margin:3px 0 0 0; }

/* ── Stats row ── */
.ct-stats { display:flex; gap:14px; flex-wrap:wrap; margin-bottom:20px; }
.ct-stat-box {
    flex:1; min-width:120px; padding:14px 16px;
    background:#FFFFFF; border:1.5px solid #E5EAF2;
    border-radius:12px; text-align:center;
    box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.ct-stat-num { font-size:24px; font-weight:800; color:#1B3A6B; }
.ct-stat-lbl { font-size:11px; color:#6b7999; font-weight:500; margin-top:2px; }

/* ── Section divider ── */
.ct-section {
    display:flex; align-items:center; gap:10px;
    padding:11px 0 9px 2px; margin-top:14px; margin-bottom:8px;
    border-bottom:2.5px solid;
}
.ct-section-text { font-size:12px; font-weight:800; letter-spacing:0.8px; text-transform:uppercase; }

/* ── Topic card buttons ── */
div[data-testid="stMain"] div[data-testid="stButton"] > button {
    width:100% !important; min-height:68px !important; height:auto !important;
    background:#FFFFFF !important; border:1.5px solid #E5EAF2 !important;
    border-radius:10px !important; box-shadow:0 1px 4px rgba(0,0,0,0.05) !important;
    padding:10px !important; cursor:pointer !important;
    color:#1a2340 !important; font-size:12px !important; font-weight:600 !important;
    line-height:1.4 !important; white-space:pre-wrap !important; word-break:break-word !important;
    transition:box-shadow 0.15s ease,border-color 0.15s ease,transform 0.15s ease !important;
    display:flex !important; flex-direction:column !important;
    align-items:center !important; justify-content:center !important;
    gap:4px !important; text-align:center !important;
}
div[data-testid="stMain"] div[data-testid="stButton"] > button:hover {
    border-color:#99aacc !important; box-shadow:0 4px 14px rgba(0,0,0,0.11) !important;
    transform:translateY(-2px) !important; background:#FAFBFF !important;
}

/* ── Subtopic panel ── */
.ct-active-card {
    border-radius:12px; padding:18px 20px;
    margin-top:6px; margin-bottom:4px; border-left:5px solid;
}
.ct-active-title { font-size:15px; font-weight:700; margin-bottom:12px; }
.ct-count-badge {
    display:inline-block; font-size:10px; font-weight:700;
    padding:2px 7px; border-radius:20px; margin-left:6px;
    vertical-align:middle; opacity:0.75;
}
.ct-subtopic-list { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:5px; }
.ct-subtopic-item {
    display:flex; align-items:center; gap:10px;
    padding:8px 12px; background:rgba(255,255,255,0.78);
    border-radius:8px; font-size:13px; font-weight:500; color:#1a2340;
    border:1px solid rgba(0,0,0,0.07);
}
.ct-subtopic-num { font-size:11px; font-weight:700; color:rgba(0,0,0,0.28); min-width:20px; text-align:right; }
.ct-subtopic-dot { width:6px; height:6px; border-radius:50%; flex-shrink:0; }

/* ── Empty state ── */
.ct-empty {
    padding:12px 16px; border-radius:8px; background:#F5F7FA;
    border:1px dashed #D0D7E6; color:#8896b0;
    font-size:12px; font-style:italic; margin-top:4px;
}
</style>
"""

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
def clean_label(fname: str) -> str:
    """Strip leading number prefix and convert underscores to spaces."""
    name = fname.replace('.py', '')
    if '_' in name:
        name = name.split('_', 1)[-1]
    return name.replace('_', ' ').strip()

def get_disk_files(root_dir: str, folder_name: str) -> list[str]:
    """
    Return cleaned page titles from .py files inside a topic folder.
    Mirrors exactly how the homepage reads sub-pages.
    """
    folder_path = os.path.join(root_dir, folder_name)
    if not os.path.isdir(folder_path):
        return []
    files = sorted(f for f in os.listdir(folder_path) if f.endswith('.py'))
    return [clean_label(f) for f in files]

def fuzzy_match(a: str, b: str) -> bool:
    return a.strip().lower() == b.strip().lower()

def find_folder(root_dir: str, topic_name: str, ignore: list) -> str | None:
    """Find the disk folder whose cleaned label matches the topic name."""
    try:
        items = sorted(os.listdir(root_dir))
    except Exception:
        return None
    for f in items:
        if f in ignore or not os.path.isdir(os.path.join(root_dir, f)):
            continue
        label = clean_label(f)
        if fuzzy_match(label, topic_name):
            return f
        # loose contains-match
        if topic_name.lower() in label.lower() or label.lower() in topic_name.lower():
            return f
    return None

IGNORE = ['__pycache__', '.git', '.streamlit', 'venv',
          '1_🤓_Homepage.py', 'main.py', 'requirements.txt', 'credentials.json']

# ---------------------------------------------------------------------------
# RENDER SUBTOPIC LIST (reads from disk)
# ---------------------------------------------------------------------------
def render_subtopic_panel(topic_name: str, icon: str, accent: str, light: str,
                           root_dir: str, folder_name: str | None):
    if folder_name:
        subs = get_disk_files(root_dir, folder_name)
    else:
        subs = []

    if subs:
        items_html = "".join(
            f"""<li class="ct-subtopic-item">
                    <span class="ct-subtopic-num">{i+1:02d}</span>
                    <span class="ct-subtopic-dot" style="background:{accent};"></span>
                    <span>{s}</span>
                </li>"""
            for i, s in enumerate(subs)
        )
        content_html = f'<ul class="ct-subtopic-list">{items_html}</ul>'
        badge = f'<span class="ct-count-badge" style="background:{accent}20;color:{accent};">{len(subs)} pages</span>'
    else:
        content_html = '<div class="ct-empty">📂 No pages found in this folder yet.</div>'
        badge = ""

    st.markdown(f"""
    <div class="ct-active-card" style="background:{light}; border-color:{accent};">
        <div class="ct-active-title" style="color:{accent};">
            {icon} {topic_name} {badge}
        </div>
        {content_html}
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    st.markdown(CSS, unsafe_allow_html=True)

    root_dir = os.getcwd()

    # ── Header ───────────────────────────────────────────────
    st.markdown("""
    <div class="ct-header">
        <div class="ct-header-icon">🗂️</div>
        <div>
            <div class="ct-header-title">Content Index</div>
            <div class="ct-header-sub">Browse every section and topic — click any card to see its pages</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats ────────────────────────────────────────────────
    n_sections = len(BUCKETS)
    n_topics   = sum(len(v["topics"]) for v in BUCKETS.values())
    st.markdown(f"""
    <div class="ct-stats">
        <div class="ct-stat-box">
            <div class="ct-stat-num">{n_sections}</div>
            <div class="ct-stat-lbl">Sections</div>
        </div>
        <div class="ct-stat-box">
            <div class="ct-stat-num">{n_topics}</div>
            <div class="ct-stat-lbl">Topics</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Search bar ───────────────────────────────────────────
    search_query = st.text_input(
        "search", placeholder="🔍  Search topics…",
        label_visibility="collapsed", key="ct_search"
    )

    # ── Session state for open/close ─────────────────────────
    if "ct_open" not in st.session_state:
        st.session_state.ct_open = {}

    # ── Build search results if query present ────────────────
    if search_query.strip():
        q = search_query.strip().lower()
        found_any = False
        for bucket_name, meta in BUCKETS.items():
            for topic_name, icon in meta["topics"].items():
                if q in topic_name.lower():
                    folder = find_folder(root_dir, topic_name, IGNORE)
                    render_subtopic_panel(topic_name, icon, meta["accent"], meta["light"], root_dir, folder)
                    found_any = True
        if not found_any:
            st.warning("No topics matched your search. Try a different keyword.")
        return

    # ── Full index ───────────────────────────────────────────
    for bucket_name, meta in BUCKETS.items():
        accent = meta["accent"]
        light  = meta["light"]
        topics = meta["topics"]

        st.markdown(f"""
        <div class="ct-section" style="border-color:{accent};">
            <span class="ct-section-text" style="color:{accent};">{bucket_name}</span>
            <span style="color:{accent};opacity:0.5;font-size:11px;font-weight:600;">
                — {len(topics)} topic(s)
            </span>
        </div>
        """, unsafe_allow_html=True)

        topic_list = list(topics.items())
        max_cols   = min(len(topic_list), 6)
        cols       = st.columns(max_cols)

        for i, (topic_name, icon) in enumerate(topic_list):
            key     = f"{bucket_name}||{topic_name}"
            is_open = st.session_state.ct_open.get(key, False)
            label   = f"{icon}\n\n{'▾ ' if is_open else ''}{topic_name}"

            with cols[i % max_cols]:
                if st.button(label, key=f"ct_{bucket_name}_{topic_name}",
                             use_container_width=True):
                    st.session_state.ct_open[key] = not is_open
                    st.rerun()

        # Render open panels beneath the row
        for topic_name, icon in topic_list:
            key = f"{bucket_name}||{topic_name}"
            if st.session_state.ct_open.get(key, False):
                folder = find_folder(root_dir, topic_name, IGNORE)
                render_subtopic_panel(topic_name, icon, accent, light, root_dir, folder)

        st.markdown("<div style='margin-bottom:4px'></div>", unsafe_allow_html=True)


# Called by homepage loader via exec_module
def show():
    main()

if __name__ == "__main__":
    main()