import streamlit as st
import os
import base64

# --- STYLING ---
st.markdown("""
    <style>
    .cv-header {
        color: #001A70;
        font-family: 'Segoe UI', sans-serif;
        border-bottom: 2px solid #001A70;
        padding-bottom: 10px;
    }
    .download-section {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 1px solid #d1d5db;
    }
    .preview-box {
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 10px;
        background-color: #f9f9f9;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Talent Pool Viewer")
st.markdown("Browse and download candidate CVs by department and experience level.")

# --- DIRECTORY SETTINGS ---
base_path = os.path.dirname(__file__) 

def display_pdf(file_path):
    """
    Renders the PDF CV. 
    Uses st.pdf for native viewing or a base64 fallback for published environments.
    """
    try:
        with open(file_path, "rb") as f:
            pdf_bytes = f.read()
        
        # Try the high-quality native viewer first
        if hasattr(st, "pdf"):
            try:
                st.pdf(pdf_bytes, height=1000)
                return
            except Exception:
                pass # Fallback to HTML if streamlit[pdf] is missing
        
        # Fallback for published environments or older versions
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf">'
        st.markdown(f'<div class="preview-box">{pdf_display}</div>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Error loading PDF: {e}")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Filter Candidates")

# Get Departments
departments = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))])

if not departments:
    st.sidebar.warning("No department folders found.")
    st.warning("Please create folders like 'Finance' or 'Engineer' in the directory.")
else:
    # Department Selection in Sidebar
    selected_dept = st.sidebar.selectbox("Select Department", departments)
    
    dept_path = os.path.join(base_path, selected_dept)
    exp_levels = sorted([d for d in os.listdir(dept_path) if os.path.isdir(os.path.join(dept_path, d))])
    
    if not exp_levels:
        st.sidebar.info(f"No experience levels in {selected_dept}.")
    else:
        # Experience Level Selection in Sidebar
        selected_exp = st.sidebar.selectbox("Years of Experience", exp_levels)
        
        final_path = os.path.join(dept_path, selected_exp)
        cv_files = sorted([f for f in os.listdir(final_path) if f.lower().endswith('.pdf')])
        
        if not cv_files:
            st.error(f"No PDF CVs found in {selected_dept} > {selected_exp}")
        else:
            # Candidate Selection in Sidebar
            selected_cv = st.sidebar.selectbox("Select Candidate CV", cv_files)
            cv_full_path = os.path.join(final_path, selected_cv)

            # --- MAIN CONTENT AREA ---
            st.divider()
            
            # --- DOWNLOAD OPTION ---
            with open(cv_full_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.markdown('<div class="download-section">', unsafe_allow_html=True)
            st.write(f"📄 **Ready to download:** {selected_cv}")
            st.download_button(
                label="Click here to Download CV",
                data=PDFbyte,
                file_name=selected_cv,
                mime='application/pdf',
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # --- RENDER CV PREVIEW ---
            with st.expander("Preview CV Content", expanded=True):
                display_pdf(cv_full_path)

# --- FOOTER ---
st.sidebar.divider()
st.sidebar.info("Use the dropdowns above to filter the talent pool.")