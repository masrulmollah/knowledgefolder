import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 🔄 Set off and Carry Forward of Losses")
st.markdown("#### According to the Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
section = st.sidebar.radio("Select Section:", 
                           ["General Rules", "Business Losses", "Special Losses", "Summary Table"])

if section == "General Rules":
    st.markdown("##### **Intra-head & Inter-head Set off (Section 70)**")
    st.write("The Act allows taxpayers to adjust losses against income to reduce total tax liability:")
    st.write("- **Within the Same Head:** Loss from one source (e.g., a shop) can be set off against another source (e.g., a factory) under 'Business Income'.")
    st.write("- **Across Different Heads:** A net loss in one head (like 'Rent') can generally be set off against income in another head (like 'Business') in the same year.")
    st.error("**Restriction:** Losses from 'Capital Gains' or 'Speculation' cannot be set off against regular income like Salary.")

elif section == "Business Losses":
    st.markdown("##### **Carry Forward Provisions**")
    st.write("If a business loss cannot be fully adjusted in the current year, it can be carried forward:")
    st.write("- **Duration:** Up to **6 consecutive assessment years**.")
    st.write("- **Condition:** It must be set off against profits from the same business or profession in the future.")
    st.info("Note: Depreciation allowance can be carried forward indefinitely if it cannot be fully set off.")

elif section == "Special Losses":
    st.markdown("##### **Ring-Fenced Losses**")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🎲 Speculation Loss**")
        st.write("- Can ONLY be set off against speculation profits.")
        st.write("- Carry forward: 6 years.")
        
    with col2:
        st.markdown("**💰 Capital Loss**")
        st.write("- Can ONLY be set off against Capital Gains.")
        st.write("- Carry forward: 6 years (if loss > Tk. 5,000).")

elif section == "Summary Table":
    st.markdown("##### **Loss Adjustment Matrix**")
    # Using a simple dictionary to create a clean, standard-sized table
    loss_summary = {
        "Type of Loss": ["Business", "Speculation", "Capital Gain", "Agricultural"],
        "Set off Against": ["Any head*", "Speculation only", "Capital Gain only", "Any head"],
        "Carry Forward": ["6 Years", "6 Years", "6 Years", "6 Years"]
    }
    st.table(loss_summary)
    st.caption("*Business loss cannot be set off against Capital Gains.")

# Bottom Spacing
st.write("")
st.divider()