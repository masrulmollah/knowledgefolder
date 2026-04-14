import streamlit as st
import os
import base64
import io
from PyPDF2 import PdfReader, PdfWriter

# --- LIBRARY STYLING ---
st.markdown("""
    <style>
    .book-container {
        background-color: #FDFEFE;
        padding: 20px;
        border-radius: 10px;
        border-top: 4px solid #1E3A8A;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .preview-box {
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 10px;
        background-color: #f9f9f9;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Knowledge Repository: Books")
st.markdown("Access technical manuals. *Preview limited to the cover page.*")

# Directory setup
base_path = os.path.dirname(__file__) 

def get_preview_pdf_bytes(file_path):
    """Slices the PDF to only the first page and returns raw bytes"""
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()
        if len(reader.pages) > 0:
            writer.add_page(reader.pages[0])
        
        preview_buffer = io.BytesIO()
        writer.write(preview_buffer)
        return preview_buffer.getvalue()
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return None

def display_pdf_fallback(pdf_bytes):
    """HTML Embed fallback for environments without streamlit[pdf]"""
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf">'
    st.markdown(f'<div class="preview-box">{pdf_display}</div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("📚 Library Navigation")

# Scan for genre folders
genres = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))])

if not genres:
    st.sidebar.warning("No folders found. Check your directory structure.")
else:
    selected_genre = st.sidebar.selectbox("Select Genre", genres)
    
    genre_path = os.path.join(base_path, selected_genre)
    categories = sorted([d for d in os.listdir(genre_path) if os.path.isdir(os.path.join(genre_path, d))])
    
    if not categories:
        st.sidebar.info(f"No categories in {selected_genre}.")
    else:
        selected_cat = st.sidebar.selectbox("Select Category", categories)
        
        final_path = os.path.join(genre_path, selected_cat)
        book_files = sorted([f for f in os.listdir(final_path) if f.lower().endswith('.pdf')])
        
        if not book_files:
            st.sidebar.error(f"No PDFs found in {selected_cat}")
        else:
            selected_book = st.sidebar.selectbox("Select Book Title", book_files)
            book_full_path = os.path.join(final_path, selected_book)

            # --- MAIN CONTENT AREA ---
            st.divider()
            st.markdown('<div class="book-container">', unsafe_allow_html=True)
            
            with open(book_full_path, "rb") as pdf_file:
                full_book_bytes = pdf_file.read()

            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.subheader(f"📖 {selected_book.replace('.pdf', '')}")
            with col_b:
                st.download_button(
                    label="Download Full Book",
                    data=full_book_bytes,
                    file_name=selected_book,
                    mime='application/pdf',
                    use_container_width=True
                )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # --- DISPLAY PREVIEW ---
            with st.expander("View Preview (Cover Page)", expanded=True):
                preview_data = get_preview_pdf_bytes(book_full_path)
                if preview_data:
                    try:
                        # Attempt to use the native high-quality viewer
                        st.pdf(preview_data, height=800)
                    except Exception:
                        # Fallback to base64 if streamlit[pdf] is missing/fails
                        display_pdf_fallback(preview_data)

# --- SIDEBAR FOOTER ---
st.sidebar.divider()
st.sidebar.info("Select a genre and category to browse the repository.")