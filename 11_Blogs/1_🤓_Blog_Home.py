import streamlit as st
import os

# --- STYLING ---
st.markdown("""
    <style>
    .blog-header { color: #001A70; font-family: 'Segoe UI', sans-serif; border-bottom: 2px solid #001A70; padding-bottom: 10px; }
    .content-section { background-color: #ffffff; padding: 25px; border-radius: 12px; border: 1px solid #d1d5db; margin-top: 15px; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); }
    /* Style for the vertical selection labels */
    .stRadio > div { gap: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- DIRECTORY SETTINGS ---
base_path = os.path.dirname(os.path.abspath(__file__))

# --- SIDEBAR: NAVIGATION ---
#st.sidebar.title("📚 Knowledge Center")

# Get Category Folders
categories = sorted([d for d in os.listdir(base_path) 
                    if os.path.isdir(os.path.join(base_path, d)) and not d.startswith('.')])

if not categories:
    st.title("📚 Knowledge Folder Blog")
    st.warning("Please create category folders inside '11_Blogs'.")
else:
    # 1. Select Category
    selected_cat = st.sidebar.selectbox("📁 Category", ["Select..."] + categories)
    
    if selected_cat != "Select...":
        cat_path = os.path.join(base_path, selected_cat)
        sub_categories = sorted([d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d))])
        
        if not sub_categories:
            st.sidebar.info(f"No sub-folders in {selected_cat}")
            st.title("Knowledge Folder")
        else:
            # 2. Select Sub-category
            selected_sub = st.sidebar.selectbox("📂 Sub-category", ["Select..."] + sub_categories)
            
            if selected_sub != "Select...":
                final_path = os.path.join(cat_path, selected_sub)
                blog_files = sorted([f for f in os.listdir(final_path) if f.endswith('.py')])
                
                if blog_files:
                    st.sidebar.divider()
                    st.sidebar.subheader("📄 Select Blog Post")
                    
                    # 3. VERTICAL TABS: Create a radio list in the sidebar for blogs
                    # This places the names one below another as requested
                    blog_display_names = [f.replace(".py", "").replace("_", " ").title() for f in blog_files]
                    
                    selected_blog_name = st.sidebar.radio(
                        "Choose a topic to read:",
                        options=blog_display_names,
                        index=0
                    )

                    # Find the actual filename corresponding to the selected display name
                    selected_index = blog_display_names.index(selected_blog_name)
                    blog_file = blog_files[selected_index]
                    blog_full_path = os.path.join(final_path, blog_file)

                    # --- MAIN BODY RENDERING ---
                    st.title(f"📂 {selected_sub.replace('_', ' ').title()}")
                    
                    # READ AND EXECUTE THE SELECTED BLOG CODE
                    with open(blog_full_path, "r", encoding='utf-8') as f:
                        blog_content = f.read()
                    
                    st.markdown('<div class="content-section">', unsafe_allow_html=True)
                    # We execute the specific blog code directly onto the body
                    exec(blog_content, globals())
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.title(f"📂 {selected_sub}")
                    st.info("No blog posts (.py files) found in this sub-category.")
            else:
                st.title("📚 Knowledge Folder Blog")
                st.info("Please select a sub-category from the sidebar.")
    else:
        st.title("📚 Knowledge Folder Blog")
        st.markdown("### Welcome! \nSelect a category in the sidebar to begin exploring.")
        st.markdown("Here you will find multi categories blogs on various subject written by professionals.")