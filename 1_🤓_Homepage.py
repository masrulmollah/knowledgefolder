import streamlit as st
import os
import importlib.util

# --- 1. SET PAGE CONFIG ---
# This sets the browser tab title and favicon
st.set_page_config(
    page_title="Knowledge Folder", 
    page_icon="📁", 
    layout="wide"
)

def main():
    # --- 2. STATIC CUSTOM HEADER ---
    # This remains visible at the top of every page
    st.markdown("""
        <style>
        .main-header {
            font-size: 22px !important;
            font-weight: 700;
            color: #2E4053;
            background-color: #FBFCFC;
            padding: 8px 15px;
            border-radius: 8px;
            border-left: 5px solid #001A70; /* Unilever Blue Accent */
            margin-bottom: 25px;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        </style>
        <div class="main-header">
            📁 Knowledge Folder
        </div>
    """, unsafe_allow_html=True)

    # --- 3. DIRECTORY SCANNING ---
    root_dir = os.getcwd() 
    # Files/folders to hide from the navigation menu
    ignore_list = ['__pycache__', '.git', '.streamlit', 'venv', '1_🤓_Homepage.py', 'main.py']
    
    # Identify Main Block folders
    main_blocks = sorted([d for d in os.listdir(root_dir) 
                         if os.path.isdir(os.path.join(root_dir, d)) 
                         and d not in ignore_list])

    if not main_blocks:
        st.error("No Category folders found! Please create folders like 'Accounting' or 'Machine_Learning'.")
        return

    # --- 4. TOP NAVIGATION (MAIN BLOCKS) ---
    # Clean folder names for display (e.g., '01_Accounting' becomes 'Accounting')
    tab_labels = [d.split('_', 1)[-1].replace('_', ' ') if '_' in d else d for d in main_blocks]
    
    selected_tab_label = st.segmented_control(
        label="Category Selection", 
        options=tab_labels, 
        selection_mode="single",
        default=tab_labels[0],
        label_visibility="collapsed" 
    )

    # Map selected label back to the folder path
    selected_index = tab_labels.index(selected_tab_label)
    selected_block = main_blocks[selected_index]

    # --- 5. SIDEBAR NAVIGATION (SUBPAGES) ---
    block_path = os.path.join(root_dir, selected_block)
    subpages = sorted([f for f in os.listdir(block_path) if f.endswith('.py')])

    if subpages:
        # Clean subpage names for the sidebar dropdown
        page_names = {}
        for f in subpages:
            clean_n = f.split('_', 1)[-1].replace('.py', '').replace('_', ' ') if '_' in f else f.replace('.py', '')
            page_names[clean_n] = f
        
        selected_subpage = st.sidebar.selectbox(
            "Select Topic", 
            options=list(page_names.keys()),
            key="topic_selector"
        )

        # --- 6. CONTENT RENDERING ---
        if selected_subpage:
            # Add a small buffer before content starts
            st.write("") 
            
            file_to_load = os.path.join(block_path, page_names[selected_subpage])
            
            # This logic dynamically executes the code inside your subpage file
            spec = importlib.util.spec_from_file_location("module.name", file_to_load)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
    else:
        st.info(f"The folder '{selected_block}' is currently empty. Add .py files to start.")

# --- 7. RUN THE APP ---
if __name__ == "__main__":
    main()