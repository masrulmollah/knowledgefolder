import streamlit as st
import pandas as pd
import io

# --- 1. CONFIGURATION SAFETY CHECK ---
try:
    st.set_page_config(
        page_title="Python Module 9: Excel Automation",
        page_icon="📁",
        layout="wide"
    )
except st.errors.StreamlitAPIException:
    pass

# --- 2. HEADER ---
st.title("📁 Module 9: Automation & Interacting with Excel")
st.markdown("""
Python isn't meant to replace Excel entirely; it's meant to **automate** it. In this module, we learn how to take our processed data and inject it into professionally formatted Excel workbooks that are ready for your manager's review.
""")

st.divider()

# --- SECTION 1: READING MULTIPLE SHEETS ---
st.header("1. Consolidating Multi-Sheet Workbooks")
st.write("Often, ERP exports come in multiple tabs. Pandas can read these into a 'Dictionary' of DataFrames.")

st.code("""
import pandas as pd

# Reading an entire Excel file with multiple sheets
excel_file = pd.ExcelFile('Monthly_Report.xlsx')
sheet_names = excel_file.sheet_names # ['Revenue', 'OPEX', 'Tax']

# Load a specific sheet
df_opex = pd.read_excel('Monthly_Report.xlsx', sheet_name='OPEX')
""", language="python")

st.divider()

# --- SECTION 2: THE AUTOMATED REPORT GENERATOR ---
st.header("2. Simulation: The Formatted Report Generator")
st.write("Let's simulate creating a formatted 'Variance Report'. This script adds currency formatting and bold headers automatically.")

# Sample Data
report_data = pd.DataFrame({
    "Description": ["Direct Material", "Direct Labor", "Energy Cost", "Freight", "Depreciation"],
    "Budget": [500000, 350000, 120000, 85000, 45000],
    "Actual": [512000, 345000, 135000, 90000, 45000]
})
report_data['Variance'] = report_data['Actual'] - report_data['Budget']

st.dataframe(report_data, use_container_width=True)

# Function to generate formatted Excel in memory
def convert_df_to_excel(df):
    output = io.BytesIO()
    # Using XlsxWriter as the engine for formatting
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Variance_Report')
        
        workbook  = writer.book
        worksheet = writer.sheets['Variance_Report']

        # Define Formats
        header_format = workbook.add_format({
            'bold': True, 
            'bg_color': '#D7E4BC', 
            'border': 1
        })
        currency_format = workbook.add_format({'num_format': '#,##0'})
        
        # Apply header format
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
            
        # Apply currency format to numeric columns
        worksheet.set_column('B:D', 15, currency_format)
        
    return output.getvalue()

if st.button("🚀 Generate & Download Formatted Excel"):
    excel_data = convert_df_to_excel(report_data)
    st.download_button(
        label="📥 Download Excel Report",
        data=excel_data,
        file_name="Automated_Financial_Report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    st.success("Report generated with bold headers and currency formatting!")

st.divider()

# --- SECTION 3: REFRESHER QUIZ ---
st.header("🧠 Module 9 Quiz")
st.write("How do we bridge the gap between data and presentation?")

q_excel = st.radio(
    "Which library is best used alongside Pandas when you need to add cell-level formatting (like colors, borders, and fonts) to an Excel file?",
    ["NumPy", "XlsxWriter / Openpyxl", "PyPDF2"]
)

if st.button("Submit Answer"):
    if "XlsxWriter" in q_excel:
        st.balloons()
        st.success("Correct! While Pandas handles the data, XlsxWriter/Openpyxl handles the visual 'makeup' of the Excel file.")
    else:
        st.error("Not quite. NumPy is for math. For Excel formatting, you need specialized Excel libraries.")

st.markdown("---")
st.caption("Knowledge Folder | Module 9: Automation & Interacting with Excel")