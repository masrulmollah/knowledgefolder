import streamlit as st

# --- STANDARD WEB HEADERS ---
st.markdown("### 💰 Income Tax Refunds")
st.markdown("#### Provisions under (Sections 241–251) | Income Tax Act, 2023")
st.divider()

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Refund Guide")
menu = st.sidebar.radio("Go to:", 
    ["Refund Entitlement", "The Refund Process", "Set-off & Adjustments", "Interest on Delayed Refund"])

if menu == "Refund Entitlement":
    st.markdown("##### **Who is entitled to a Refund? (Section 241)**")
    st.write("A refund is due when the total tax paid exceeds the 'properly chargeable' tax.")
    
    st.info("**Common Causes of Refunds:**")
    st.write("- **Excess TDS:** Tax deducted at source by banks or customers is higher than the final tax liability.")
    st.write("- **Overpaid Advance Tax:** Installments paid during the year exceed the final tax calculated in the return.")
    st.write("- **Double Taxation Relief:** Credits from foreign tax payments reducing the local liability.")
    
    st.warning("Note: The right to claim a refund can be exercised by the legal representative if the taxpayer is deceased or incapacitated.")

elif menu == "The Refund Process":
    st.markdown("##### **How to Claim a Refund (Section 242)**")
    st.write("The 2023 Act has simplified the refund process for compliant taxpayers.")
    
    st.success("**Automatic Claim:**")
    st.write("When you file your return under **Universal Self-Assessment (Section 167)** and show a 'Refundable' amount, that return is legally considered your refund application.")
    
    st.markdown("**Timeline:**")
    st.write("- The DCT is required to process and issue the refund within **60 days** of the assessment.")
    st.write("- For refunds arising from Appeal or Tribunal orders, the DCT must act 'suo motu' (on their own) to process the payment.")

elif menu == "Set-off & Adjustments":
    st.markdown("##### **Adjustment of Refund (Section 248)**")
    st.write("Before sending the money to your bank account, the tax office will check for 'Arrears'.")
    
    st.error("**The Set-off Rule:**")
    st.write("The DCT may set off the amount to be refunded against any existing tax liability, penalty, or interest due from you for any previous assessment year.")
    
    st.info("💡 **Finance Lead Note:** For factory audits, if you have a refund in 2024 but an outstanding demand from a 2022 audit, expect the 2024 refund to be adjusted automatically. Always reconcile 'Net Tax Position' across all open years.")

elif menu == "Interest on Delayed Refund":
    st.markdown("##### **Compensation for Delay (Section 249)**")
    st.write("If the government stays your money beyond the legal limit, you are entitled to interest.")
    
    st.markdown("**Current Rate:**")
    st.metric("Simple Interest Rate", "7.5% Per Annum")
    
    st.write("**Conditions:**")
    st.write("- Interest is calculated from the date the refund became due until the date the refund is actually granted.")
    st.write("- Interest is NOT payable if the delay is attributable to the taxpayer (e.g., failure to provide bank details or respond to notices).")

st.divider()