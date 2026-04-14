import streamlit as st
import os
import importlib.util

# --- 1. SET PAGE CONFIG ---
st.set_page_config(
    page_title="Knowledge Folder", 
    page_icon="📁", 
    layout="wide"
)

def main():
    # --- 2. STATIC CUSTOM HEADER ---
    st.markdown("""
        <style>
        .main-header {
            font-size: 22px !important;
            font-weight: 700;
            color: #2E4053;
            background-color: #FBFCFC;
            padding: 8px 15px;
            border-radius: 8px;
            border-left: 5px solid #001A70; 
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
    ignore_list = [
        '__pycache__', '.git', '.streamlit', 'venv', 
        '1_🤓_Homepage.py', 'main.py', 'requirements.txt', 'credentials.json'
    ]
    
    items = sorted(os.listdir(root_dir))
    main_blocks = [
        f for f in items 
        if os.path.isdir(os.path.join(root_dir, f)) and f not in ignore_list
    ]

    if not main_blocks:
        st.warning("No category folders found.")
        return

    tab_labels = [f.split('_', 1)[-1].replace('_', ' ') if '_' in f else f for f in main_blocks]

    # --- 4. TOP NAVIGATION ---
    selected_tab_label = st.segmented_control(
        "Select Category",
        options=tab_labels,
        default=tab_labels[0],
        selection_mode="single" 
    )

    if not selected_tab_label:
        return

    selected_index = tab_labels.index(selected_tab_label)
    selected_block = main_blocks[selected_index]

    # --- 5. SIDEBAR NAVIGATION ---
    block_path = os.path.join(root_dir, selected_block)
    subpages = sorted([f for f in os.listdir(block_path) if f.endswith('.py')])

    if subpages:
        page_names = { (f.split('_', 1)[-1].replace('.py', '').replace('_', ' ') if '_' in f else f.replace('.py', '')): f for f in subpages }
        
        selected_subpage = st.sidebar.selectbox("Select Topic", options=list(page_names.keys()))

        # --- 6. CONTENT RENDERING (FIXED) ---
        if selected_subpage:
            file_to_load = os.path.join(block_path, page_names[selected_subpage])
            
            try:
                spec = importlib.util.spec_from_file_location("dynamic_module", file_to_load)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # CRITICAL FIX: Explicitly call the show() function
                if hasattr(module, "show"):
                    module.show()
                else:
                    st.error("This module does not have a show() function.")
            
            except Exception as e:
                st.error(f"### ❌ Page Error")
                st.exception(e)
    else:
        st.info("This category is empty.")

if __name__ == "__main__":
    main()