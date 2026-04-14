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
    </style>
    """, unsafe_allow_html=True)

st.title("Talent Pool Viewer")
st.markdown("Browse and download candidate CVs by department and experience level.")

# --- DIRECTORY SETTINGS ---
# This looks inside the current '02_👥_Talent_Pool' folder
base_path = os.path.dirname(__file__) 

def display_pdf(file_path):
    """Helper function to embed PDF in Streamlit"""
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
departments = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))])

if not departments:
    st.warning("No department folders found. Please create folders like 'Finance' or 'Engineer'.")
else:
    col1, col2 = st.columns(2)
    
    with col1:
        selected_dept = st.selectbox("Select Department", departments)
    
    dept_path = os.path.join(base_path, selected_dept)
    exp_levels = sorted([d for d in os.listdir(dept_path) if os.path.isdir(os.path.join(dept_path, d))])
    
    if not exp_levels:
        st.info(f"No experience subfolders found in {selected_dept}.")
    else:
        with col2:
            selected_exp = st.selectbox("Years of Experience", exp_levels)
        
        final_path = os.path.join(dept_path, selected_exp)
        cv_files = sorted([f for f in os.listdir(final_path) if f.lower().endswith('.pdf')])
        
        if not cv_files:
            st.error(f"No PDF CVs found in {selected_dept} > {selected_exp}")
        else:
            st.divider()
            selected_cv = st.selectbox("Select Candidate CV", cv_files)
            cv_full_path = os.path.join(final_path, selected_cv)

            # --- DOWNLOAD OPTION ---
            with open(cv_full_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.markdown('<div class="download-section">', unsafe_allow_html=True)
            st.write(f"📄 **Ready to download:** {selected_cv}")
            st.download_button(
                label="Click here to Download CV",
                data=PDFbyte,
                file_name=selected_cv,
                mime='application/octet-stream',
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # --- RENDER CV PREVIEW ---
            with st.expander("Preview CV Content", expanded=True):
                display_pdf(cv_full_path)

# --- FOOTER ---
st.sidebar.divider()
st.sidebar.info("Select a department and experience level to filter the talent pool.")