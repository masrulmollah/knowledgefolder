import streamlit as st

# --- DO NOT CALL set_page_config HERE (Handled by Homepage) ---

# --- STANDARD WEBPAGE STYLING ---
st.markdown("""
    <style>
    /* Standardizing global font size to 16px */
    html, body, [class*="st-"] {
        font-size: 16px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Standard Web Headings */
    h1 { font-size: 2.1rem !important; color: #1E3A8A !important; }
    h2 { font-size: 1.6rem !important; color: #1E40AF !important; margin-top: 1.5rem !important; }
    h3 { font-size: 1.25rem !important; color: #1E40AF !important; }
    
    /* Standard Paragraphs */
    p, li { font-size: 1rem !important; line-height: 1.6; color: #374151; }

    /* Custom Definition Box */
    .definition-box {
        background-color: #fcfcfc;
        padding: 15px;
        border-radius: 6px;
        border-left: 5px solid #1E3A8A;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .term-title {
        font-weight: bold;
        color: #1E3A8A;
        font-size: 1.1rem;
        display: block;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DROPDOWN FACILITY ---
st.sidebar.header("🔍 Definition Finder")
st.sidebar.write("Select a category or specific term to view the statutory summary.")

# Options for the dropdown
options = [
    "All Definitions",
    "Economic Activity",
    "Resident",
    "Input",
    "Withholding Entity",
    "Tax Period",
    "Fair Market Price",
    "Consideration",
    "Supply (Goods & Services)",
    "Export & Deemed Export",
    "Adjustments (Inc/Dec)",
    "Adjustment Event",
    "Time of Supply"
]

selection = st.sidebar.selectbox("Jump to Section:", options)

# --- HEADER ---
st.title("VAT Statutory Definitions")
st.markdown(f"#### Showing: **{selection}**")
st.divider()

# --- HELPER FUNCTION TO RENDER BOX ---
def render_def(term, definition):
    st.markdown(f"""
    <div class="definition-box">
        <span class="term-title">{term}</span>
        {definition}
    </div>
    """, unsafe_allow_html=True)

# --- LOGIC TO SHOW DEFINITIONS BASED ON DROPDOWN ---

if selection in ["All Definitions", "Economic Activity"]:
    render_def("Economic Activity", "Any activity carried on regularly or continuously for the purpose of making a profit or otherwise. Includes business, trade, and manufacture. <b>Exclusion:</b> Services provided by an employee to an employer.")

if selection in ["All Definitions", "Resident"]:
    render_def("Resident", "An individual who lives in Bangladesh for more than 182 days in a tax year, or a company/entity incorporated or controlled in Bangladesh.")

if selection in ["All Definitions", "Input"]:
    render_def("Input", "All raw materials, services, fuel, and energy used in the process of manufacturing or providing a service. Crucially, this forms the base for Input Tax Credit.")

if selection in ["All Definitions", "Withholding Entity"]:
    render_def("Withholding Entity", "A government entity, NGO, bank, or large company required to deduct VAT at source (VDS) from a supplier’s payment.")

if selection in ["All Definitions", "Tax Period"]:
    render_def("Tax Period", "A period of one month of the Gregorian calendar for a registered or enlisted person (e.g., January 1st to January 31st).")

if selection in ["All Definitions", "Fair Market Price"]:
    render_def("Fair Market Price", "The consideration in money which a supply would fetch in an open market transaction between persons who are not related.")

if selection in ["All Definitions", "Consideration"]:
    render_def("Consideration", "Any payment made (in money or kind) in response to a supply, including any amount payable upon a condition or a grant.")

if selection in ["All Definitions", "Supply (Goods & Services)"]:
    st.subheader("Types of Supply")
    render_def("Supply of Goods", "Transfer of the right to dispose of tangible property as owner, including hire-purchase agreements.")
    render_def("Supply of Services", "Any supply that is not a supply of goods, money, or immovable property (e.g., consulting, utilities).")

if selection in ["All Definitions", "Export & Deemed Export"]:
    st.subheader("International Trade")
    render_def("Export", "A supply of goods or services from inside Bangladesh to a destination outside Bangladesh.")
    render_def("Deemed Export", "Supplies of goods/services consumed outside Bangladesh or supplied against foreign currency inside Bangladesh (e.g., to EPZ or for international tenders).")

if selection in ["All Definitions", "Adjustments (Inc/Dec)"]:
    st.subheader("Tax Adjustments")
    st.info("**Increasing Adjustment:** An amount added to the output tax in the return (e.g., VDS deducted from you or a canceled credit note).")
    st.success("**Decreasing Adjustment:** An amount subtracted from the output tax (e.g., Input Tax Credit or a valid Debit Note).")

if selection in ["All Definitions", "Adjustment Event"]:
    render_def("Adjustment Event", "An event occurring after a supply (like cancellation, price change, or return) that requires an amendment to the tax already accounted for.")

if selection in ["All Definitions", "Time of Supply"]:
    render_def("Time of Supply", "The point when tax becomes due. Earliest of: when goods are removed, services rendered, an invoice is issued, or payment is received.")

# --- FOOTER ---
st.divider()
st.info("""
**💡 Finance Lead Note:** Use the sidebar to quickly filter these terms during a VAT audit. 
The NBR officers strictly follow these **Statutory Definitions**; knowing the exact 
wording for **'Economic Activity'** or **'Input'** can help defend your tax positions.
""")

st.markdown("<center style='font-size: 0.85rem; color: #9CA3AF;'>Knowledge Folder | Statutory Definitions © 2026</center>", unsafe_allow_html=True)