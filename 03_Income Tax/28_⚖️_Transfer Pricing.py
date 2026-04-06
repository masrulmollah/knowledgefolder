import streamlit as st
import pandas as pd

# --- STANDARD WEB HEADERS ---
st.markdown("### ⚖️ Transfer Pricing ")
st.markdown("#### Provisions under (Sections 233–240) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("TP Compliance Guide")
menu = st.sidebar.radio("Go to:", 
    ["Core Concepts", "ALP Methods", "Compliance & Reports", "TP Penalty Alert"])

if menu == "Core Concepts":
    st.markdown("##### **International Transactions & Associated Enterprises**")
    st.write("Transfer Pricing rules apply when 'Associated Enterprises' transact across borders.")
    
    st.info("**What is an Associated Enterprise?**")
    st.write("An enterprise is associated if one participates in the management, control, or capital of the other (e.g., Parent-Subsidiary relationship).")
    
    st.markdown("**Scope of Transactions:**")
    st.write("- Purchase, sale, or lease of tangible/intangible property.")
    st.write("- Provision of services (Management fees, Technical fees).")
    st.write("- Lending or borrowing money.")
    st.write("- Mutual cost-sharing arrangements.")

elif menu == "ALP Methods":
    st.markdown("##### **Determination of Arm’s Length Price (ALP)**")
    st.write("The Act mandates the use of the **Most Appropriate Method** to find the market-fair price.")
    
    methods = {
        "Method": ["CUP", "RPM", "CPM", "PSM", "TNMM"],
        "Best Suited For": [
            "Highly comparable goods/commodities.",
            "Distribution/Reselling without adding much value.",
            "Contract manufacturing or service providers.",
            "Complex integrated operations or unique intangibles.",
            "Routine manufacturing or services (Net Profit focus)."
        ]
    }
    st.table(pd.DataFrame(methods))
    
    st.success("**The 30th-70th Percentile Range:** If multiple prices are found, the law uses a range (30th to 70th percentile) to determine if your price is acceptable.")

elif menu == "Compliance & Reports":
    st.markdown("##### **Documentation & Filing Requirements**")
    
    st.warning("**The Tk. 3 Crore Threshold:**")
    st.write("If your total international transactions exceed **Tk. 3 Crore**, you MUST:")
    st.write("1. Maintain a detailed Transfer Pricing (TP) Documentation folder.")
    st.write("2. Submit a report from a **Chartered Accountant** along with your return.")
    
    st.markdown("**TP Documentation Contents:**")
    st.write("- Industry and Profile of associated enterprises.")
    st.write("- Nature and terms of transactions.")
    st.write("- Benchmarking study (Search for comparable companies).")
    st.write("- Justification for the selected ALP method.")

elif menu == "TP Penalty Alert":
    st.markdown("##### **Cost of Non-Compliance**")
    st.error("TP Penalties are significantly higher than standard late filing fees.")
    
    penalties = {
        "Default Type": ["Failure to keep/maintain TP docs", "Failure to produce docs on request", "Failure to file CA Report"],
        "Penalty Amount": ["Up to 1% of Transaction Value", "Up to 1% of Transaction Value", "Up to Tk. 3,00,000"]
    }
    st.table(pd.DataFrame(penalties))
    
    st.info("💡 **Finance Lead Note:** For a multinational like yours, the 'Inter-company Service Agreement' and 'Master File/Local File' structure is critical. Ensure the benchmarking is refreshed annually to match current market margins.")

st.divider()