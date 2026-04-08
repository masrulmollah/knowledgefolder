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
    # Files/folders to hide from the navigation menu
    ignore_list = [
        '__pycache__', '.git', '.streamlit', 'venv', 
        '1_🤓_Homepage.py', 'main.py', 'requirements.txt', 'credentials.json'
    ]
    
    # Identify Main Block folders (e.g., 01_VAT, 02_Talent_Pool)
    items = sorted(os.listdir(root_dir))
    main_blocks = [
        f for f in items 
        if os.path.isdir(os.path.join(root_dir, f)) and f not in ignore_list
    ]

    if not main_blocks:
        st.warning("No category folders found in the root directory.")
        return

    # Clean the folder names for the top menu (remove numbers and emojis for the label)
    tab_labels = []
    for folder in main_blocks:
        # Removes numbers and underscores, e.g., "01_⚖️_VAT" -> "⚖️ VAT"
        clean_name = folder.split('_', 1)[-1].replace('_', ' ') if '_' in folder else folder
        tab_labels.append(clean_name)

    # --- 4. TOP NAVIGATION (MAIN BLOCKS) ---
    selected_tab_label = st.segmented_control(
        "Select Category",
        options=tab_labels,
        default=tab_labels[0],
        selection_mode="single" 
    )

    if not selected_tab_label:
        st.info("Please select a category from the top menu.")
        return

    # Map selected label back to the actual folder path
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

        # --- 6. CONTENT RENDERING WITH ERROR HANDLING ---
        if selected_subpage:
            st.write("") 
            file_to_load = os.path.join(block_path, page_names[selected_subpage])
            
            try:
                # Dynamically execute the subpage
                spec = importlib.util.spec_from_file_location("module.name", file_to_load)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            
            except ModuleNotFoundError as e:
                st.error(f"### ⚠️ Missing Library")
                st.info(f"The page you are trying to view requires a library that isn't installed: **{e.name}**")
                st.markdown("""
                **How to fix:**
                1. Add `{}` to your `requirements.txt` file in GitHub.
                2. Wait a moment for Streamlit to reboot.
                """.format(e.name))
            
            except Exception as e:
                st.error(f"### ❌ Page Error")
                st.exception(e)
    else:
        st.info("This category folder is currently empty.")

if __name__ == "__main__":
    main()