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
    </style>
    """, unsafe_allow_html=True)

st.title("Knowledge Repository: Books")
st.markdown("Access technical manuals. *Preview limited to the cover page.*")

base_path = os.path.dirname(__file__) 

def get_preview_pdf(file_path):
    """Slices the PDF to only the first page for the viewer"""
    reader = PdfReader(file_path)
    writer = PdfWriter()
    
    if len(reader.pages) > 0:
        writer.add_page(reader.pages[0])
    
    preview_buffer = io.BytesIO()
    writer.write(preview_buffer)
    return preview_buffer.getvalue()

def display_pdf(pdf_bytes):
    """Embeds the provided PDF bytes into the iframe"""
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Library Navigation")

genres = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))])

if not genres:
    st.sidebar.warning("No genre folders found.")
else:
    # Moved Genre Selection to Sidebar
    selected_genre = st.sidebar.selectbox("Select Genre", genres)
    
    genre_path = os.path.join(base_path, selected_genre)
    categories = sorted([d for d in os.listdir(genre_path) if os.path.isdir(os.path.join(genre_path, d))])
    
    if not categories:
        st.sidebar.info(f"No categories found in {selected_genre}.")
    else:
        # Moved Category Selection to Sidebar
        selected_cat = st.sidebar.selectbox("Select Category", categories)
        
        final_path = os.path.join(genre_path, selected_cat)
        book_files = sorted([f for f in os.listdir(final_path) if f.lower().endswith('.pdf')])
        
        if not book_files:
            st.sidebar.error(f"No PDF books found in {selected_cat}")
        else:
            # Moved Book Title Selection to Sidebar
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
            
            # Preview (1 page only)
            with st.expander("View Preview (Cover Page)", expanded=True):
                preview_bytes = get_preview_pdf(book_full_path)
                display_pdf(preview_bytes)

# --- SIDEBAR FOOTER ---
st.sidebar.divider()
st.sidebar.info("Select a genre and category to browse the repository.")