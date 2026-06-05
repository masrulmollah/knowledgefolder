import os
import importlib.util
import streamlit as st

# Import all modules by file path
current_dir = os.path.dirname(os.path.abspath(__file__))

def load_module(filename, alias):
    module_path = os.path.join(current_dir, filename)
    spec = importlib.util.spec_from_file_location(alias, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

mod1 = load_module("01_⚖️_Module 1 Introduction to TP in Bangladesh.py", "TP_Module_1_Introduction")
mod2 = load_module("02_⚖️_Module 2 Arm's Length Principle & Comparability Analysis.py", "TP_Module_2_ALP_Comparability")
mod3 = load_module("03_⚖️_Module 3 TP Methods under ITA 2023.py", "TP_Module_3_Methods")
mod4 = load_module("04_⚖️_Module 4 TP Documentation & Compliance.py", "TP_Module_4_Documentation")
mod5 = load_module("05_⚖️_Module 5 TP Audit, Penalties & Dispute Resolution.py", "TP_Module_5_Audit_Penalties")
mod6 = load_module("06_⚖️_Module 6 Advance Pricing Agreements (APA) & Safe Harbours.py", "TP_Module_6_APA_SafeHarbour")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Transfer Pricing in Bangladesh",
        page_icon="🌐",
        layout="wide"
    )

# ─── Sidebar Navigation ───
st.sidebar.title("🌐 Transfer Pricing in Bangladesh")
st.sidebar.markdown("*Income Tax Act 2023*")
st.sidebar.markdown("---")

module = st.sidebar.radio(
    "Select Module:",
    [
        "🏠 Course Overview",
        "📘 Module 1: Introduction & Legal Framework",
        "⚖️ Module 2: Arm's Length Principle",
        "🔢 Module 3: TP Methods",
        "📁 Module 4: Documentation & Compliance",
        "🔍 Module 5: Audit, Penalties & Disputes",
        "🤝 Module 6: APA & Safe Harbours",
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**📚 Course Info**  
6 Modules | ITA 2023  
Each module includes:  
- 📖 Theory & Law  
- 🧮 Examples  
- 💡 Interactive Exercises  
- ✅ Quiz  
- 📝 Summary  
""")

# ─── Main Content ───
if module == "🏠 Course Overview":
    st.title("🌐 Transfer Pricing in Bangladesh")
    st.markdown("### A Comprehensive Course based on the Income Tax Act 2023")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## What You Will Learn

        This course provides a complete, practical guide to **Transfer Pricing (TP) law and practice 
        in Bangladesh**, based on the **Income Tax Act 2023 (ITA 2023)** and the **Income Tax Rules 2023**.

        Transfer pricing is one of the most significant international tax issues facing multinational 
        enterprises (MNEs) operating in Bangladesh, particularly in sectors like **garments, 
        pharmaceuticals, telecommunications, banking, and IT services**.

        ---

        ## 📋 Full Syllabus

        | Module | Topic | Key Law |
        |--------|-------|---------|
        | **1** | Introduction & Legal Framework | Sections 175–177, ITA 2023 |
        | **2** | Arm's Length Principle & Comparability | Section 177, Rule 69 |
        | **3** | Transfer Pricing Methods | Sections 178–179, Rules 71–75 |
        | **4** | Documentation & Compliance | Section 180, Rules 77–78 |
        | **5** | Audit, Penalties & Dispute Resolution | Sections 181–182, 185 |
        | **6** | APA & Safe Harbours | Sections 183–184 |

        ---

        ## 🔑 Legal Framework at a Glance

        ```
        Income Tax Act 2023 — Transfer Pricing Provisions:
        
        Section 175 — Definition: International Transaction
        Section 176 — Definition: Associated Enterprise  
        Section 177 — Arm's Length Price requirement
        Section 178 — Transfer Pricing Methods (6 methods)
        Section 179 — Most Appropriate Method (MAM)
        Section 180 — Documentation obligations
        Section 181 — Transfer Pricing Officer powers
        Section 182 — TP Adjustments, Additional tax & Penalties
        Section 183 — Advance Pricing Agreement (APA)
        Section 184 — Safe Harbour provisions
        Section 185 — Mutual Agreement Procedure (MAP)
        
        Income Tax Rules 2023:
        Rules 68–80 — TP methodology, documentation & compliance
        ```

        ---

        ## 🏭 Key Sectors Affected in Bangladesh

        | Sector | Common TP Issues |
        |--------|-----------------|
        | Ready-Made Garments (RMG) | Contract manufacturing prices, trademark royalties |
        | Pharmaceuticals | API purchase prices, IP royalties, management fees |
        | Telecommunications | Roaming fees, interconnection, management fees |
        | Banking & Financial Services | Intra-group loans, guarantees, shared services |
        | IT & Software Services | Software development pricing, ITES fees |
        | FMCG / Consumer Goods | Brand royalties, distribution margins |
        """)

    with col2:
        st.markdown("## 📊 Quick Stats")
        st.metric("Total Modules", "6")
        st.metric("Legal Sections Covered", "11 (S.175–185)")
        st.metric("TP Methods", "6")
        st.metric("Key Rules", "Rules 68–80")

        st.markdown("---")
        st.markdown("## ⚡ Key Numbers")
        st.info("**BDT 30 Crore** — Specified domestic transaction threshold")
        st.info("**26%** — Share ownership for AE status")
        st.info("**BDT 3,000 Crore** — CbCR threshold")
        st.info("**2%** — Penalty for no documentation")
        st.info("**30 days** — To respond to NBR notice")
        st.info("**5%** — Safe harbour markup (LVAS)")
        st.info("**45 days** — Objection to Commissioner deadline")

        st.markdown("---")
        st.markdown("## 🚀 Get Started")
        st.success("👈 Select a module from the sidebar to begin!")

elif module == "📘 Module 1: Introduction & Legal Framework":
    mod1.show()
elif module == "⚖️ Module 2: Arm's Length Principle":
    mod2.show()
elif module == "🔢 Module 3: TP Methods":
    mod3.show()
elif module == "📁 Module 4: Documentation & Compliance":
    mod4.show()
elif module == "🔍 Module 5: Audit, Penalties & Disputes":
    mod5.show()
elif module == "🤝 Module 6: APA & Safe Harbours":
    mod6.show()