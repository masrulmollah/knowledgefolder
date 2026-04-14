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
    /* Helps ensure the PDF embed takes up the full width */
    embed {
        border-radius: 8px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Knowledge Repository: Books")
st.markdown("Access technical manuals. *Preview limited to the cover page.*")

# This looks inside the current folder
base_path = os.path.dirname(__file__) 

def get_preview_pdf(file_path):
    """Slices the PDF to only the first page for the viewer"""
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

def display_pdf(pdf_bytes):
    """
    Embeds the provided PDF bytes using an <embed> tag.
    This is generally more compatible with Chrome's security settings than <iframe>.
    """
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    # Using <embed> instead of <iframe> to resolve "Blocked by Chrome" errors
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("📚 Library Navigation")

# Get list of Genre folders
genres = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))])

if not genres:
    st.sidebar.warning("No genre folders found.")
    st.info("Please create folders (e.g., 'Economics', 'Finance') in the app directory.")
else:
    # 1. Select Genre
    selected_genre = st.sidebar.selectbox("Select Genre", genres)
    
    genre_path = os.path.join(base_path, selected_genre)
    categories = sorted([d for d in os.listdir(genre_path) if os.path.isdir(os.path.join(genre_path, d))])
    
    if not categories:
        st.sidebar.info(f"No categories found in {selected_genre}.")
    else:
        # 2. Select Category
        selected_cat = st.sidebar.selectbox("Select Category", categories)
        
        final_path = os.path.join(genre_path, selected_cat)
        book_files = sorted([f for f in os.listdir(final_path) if f.lower().endswith('.pdf')])
        
        if not book_files:
            st.sidebar.error(f"No PDF books found in {selected_cat}")
        else:
            # 3. Select Book
            selected_book = st.sidebar.selectbox("Select Book Title", book_files)
            book_full_path = os.path.join(final_path, selected_book)

            # --- MAIN CONTENT AREA ---
            st.divider()
            st.markdown('<div class="book-container">', unsafe_allow_html=True)
            
            # Read full file for download button
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
            
            # Generate and Display PREVIEW (1 page only)
            with st.expander("View Preview (Cover Page)", expanded=True):
                preview_bytes = get_preview_pdf(book_full_path)
                if preview_bytes:
                    display_pdf(preview_bytes)

# --- SIDEBAR FOOTER ---
st.sidebar.divider()
st.sidebar.info("Use the filters above to browse the technical library.")