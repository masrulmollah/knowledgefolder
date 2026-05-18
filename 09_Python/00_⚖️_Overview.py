import streamlit as st

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Syllabus Overview",
        page_icon="📋",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. CUSTOM STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .module-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #007bff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .metric-box {
        background-color: #e9ecef;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER SECTION ---
st.title("📋 Python for Finance & Accounting: Syllabus Overview")
st.markdown("""
Welcome to the **Python Programming Language** refresher directory. This curriculum is specifically engineered 
to transition finance professionals from traditional spreadsheet patterns into high-impact data automation, 
advanced analytics, and predictive modeling.
""")

st.divider()

# --- SECTION 1: THE ROADMAP AT A GLANCE ---
st.header("🎯 The Learning Journey")
st.write("The curriculum is split into three distinct phases to manage the learning curve seamlessly.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-box">
        <h3>🌱 Phase 1: Foundations</h3>
        <p><b>Modules 1 - 4</b></p>
        <small>Syntax, variables, loops, and building custom calculation engines.</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <h3>🐼 Phase 2: Data Manipulation</h3>
        <p><b>Modules 5 - 7</b></p>
        <small>Replacing Excel & Power Query using NumPy arrays and Pandas DataFrames.</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <h3>🚀 Phase 3: Presentation & ML</h3>
        <p><b>Modules 8 - 10</b></p>
        <small>Interactive executive charts, automated Excel generation, and predictive forecasting.</small>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- SECTION 2: INTERACTIVE SYLLABUS EXPLORER ---
st.header("🔍 Interactive Module Explorer")
st.write("Select any module from the dropdown below to see its core topics, financial use cases, and technical requirements.")

# Module Metadata Dictionary
modules_repo = {
    "Module 1: The Finance Setup": {
        "Icon": "🐍", "Phase": "Foundations", "Core Libraries": "None (Base Python)",
        "Topics": ["Anaconda vs. Base Python installation", "VS Code & Jupyter Notebooks", "Virtual Environments", "Package management (pip/conda)"],
        "Use_Case": "Setting up an isolated 'Audit Folder' workspace for dynamic automation projects."
    },
    "Module 2: Foundations & Financial Logic": {
        "Icon": "📈", "Phase": "Foundations", "Core Libraries": "None (Base Python)",
        "Topics": ["Data types (Strings, Integers, Floats)", "Arithmetic operators", "Lists for sequential data", "Dictionaries for Chart of Accounts (COA)"],
        "Use_Case": "Building mathematical logic templates (e.g., CAGR and NPV calculators) without cells."
    },
    "Module 3: Flow Control & Audit Logic": {
        "Icon": "⚖️", "Phase": "Foundations", "Core Libraries": "None (Base Python)",
        "Topics": ["Conditional Statements (if-elif-else)", "Loops (for, while)", "Exception handling (try-except)"],
        "Use_Case": "Automating internal audit threshold alerts (e.g., flagging cost center budget variances over 10%)."
    },
    "Module 4: Functions & Modular Code": {
        "Icon": "📦", "Phase": "Foundations", "Core Libraries": "None (Base Python)",
        "Topics": ["Defining functions (def)", "Arguments and Return statements", "Global vs. Local scope"],
        "Use_Case": "Creating a central 'Tax or Depreciation Engine' that can be safely reused across multiple scripts."
    },
    "Module 5: Powering Data with NumPy": {
        "Icon": "🔢", "Phase": "Data Manipulation", "Core Libraries": "NumPy",
        "Topics": ["Vectorized arrays", "Statistical methods (Mean, Median, Std Dev)", "Random sampling for financial risk"],
        "Use_Case": "Analyzing large population datasets instantly for standard deviations and potential entry anomalies."
    },
    "Module 6: Mastering Pandas (The Excel Killer)": {
        "Icon": "🐼", "Phase": "Data Manipulation", "Core Libraries": "Pandas",
        "Topics": ["DataFrames & Series structures", "Ingesting CSV/Excel/SQL data", "Data cleaning (Nulls, string clean-ups)"],
        "Use_Case": "Scrubbing unformatted or messy ERP trial balances and converting currency strings to float numbers."
    },
    "Module 7: Advanced Data Manipulation": {
        "Icon": "🧬", "Phase": "Data Manipulation", "Core Libraries": "Pandas",
        "Topics": ["Merging and Joining tables", "GroupBy aggregations", "Pivot Tables in code"],
        "Use_Case": "Replicating Power Queries and VLOOKUPs to instantly merge sub-ledgers with department operational mappings."
    },
    "Module 8: Visualization for Executive Reporting": {
        "Icon": "📊", "Phase": "Presentation & ML", "Core Libraries": "Plotly Express",
        "Topics": ["Line charts for trend analysis", "Grouped bar charts", "Interactive pie/donut charts for cost breakdowns"],
        "Use_Case": "Constructing dynamic boardroom charts where managers can hover, isolate categories, and zoom in on specific quarters."
    },
    "Module 9: Automation & Interacting with Excel": {
        "Icon": "📁", "Phase": "Presentation & ML", "Core Libraries": "Openpyxl, XlsxWriter",
        "Topics": ["Multi-sheet compilation", "Styling spreadsheets (Borders, colors, bolding)", "Automated report extraction"],
        "Use_Case": "Generating fully formatted, client-ready variance workbooks and exporting them with zero manual intervention."
    },
    "Module 10: Financial Analytics & ML": {
        "Icon": "🤖", "Phase": "Presentation & ML", "Core Libraries": "Scikit-Learn",
        "Topics": ["Cost driver relationships", "Linear Regression models", "Predictive modeling basics"],
        "Use_Case": "Separating fixed and variable factory costs dynamically to build a machine-learning-powered budget forecaster."
    }
}

selected_module = st.selectbox("Choose a Module to Review:", list(modules_repo.keys()))
mod_data = modules_repo[selected_module]

# Display Card based on selection
st.markdown(f"""
<div class="module-card">
    <h2>{mod_data['Icon']} {selected_module}</h2>
    <p><b>📈 Target Phase:</b> {mod_data['Phase']} | <b>🛠️ Tools Required:</b> <code>{mod_data['Core Libraries']}</code></p>
    <hr>
    <h4>💼 Real-World Finance Use Case:</h4>
    <p><i>"{mod_data['Use_Case']}"</i></p>
</div>
""", unsafe_allow_html=True)

# Split details into columns
c_left, c_right = st.columns(2)
with c_left:
    st.subheader("📚 Key Technical Concepts Covered")
    for topic in mod_data['Topics']:
        st.write(f"🔹 {topic}")

with c_right:
    st.subheader("💡 Readiness Indicator")
    st.info(f"Going through the interactive section of **{selected_module}** will provide the codebase needed to implement this module's financial use case directly into your workspace.")

st.divider()

# --- SECTION 3: SYLLABUS METRICS & NAVIGATION REMINDER ---
st.header("🧠 Quick Knowledge Calibration")
st.write("Ready to check your starting proficiency?")

user_level = st.select_slider(
    "How would you rate your current capability with handling raw files outside of Excel tools?",
    options=["Absolute Beginner", "Familiar with basic macros", "Comfortable with database queries", "Ready to fully automate scripts"]
)

if "automate" in user_level:
    st.balloons()
    st.success("Excellent! Skip straight to Phase 2 (Modules 5-7) to harness the full power of Pandas DataFrames.")
else:
    st.warning("Perfect. We highly recommend proceeding sequentially through Phase 1 (Modules 1-4) to build robust programming logic foundations first.")

# --- FOOTER ---
st.markdown("---")
st.caption("Knowledge Folder | Complete Python Programming Syllabus Directory | Tailored for Corporate Finance Professionals")