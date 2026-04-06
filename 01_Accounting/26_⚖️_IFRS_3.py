import streamlit as st

# --- SUBPAGE HEADER ---
st.subheader("IFRS 3: Business Combinations")
st.write("This standard outlines the accounting when an acquirer obtains control of a business (e.g., through an acquisition or merger). It establishes principles for recognizing and measuring the assets acquired and liabilities assumed.")

# --- THE CORE PRINCIPLE ---
st.info("**The Acquisition Method:** All business combinations must be accounted for using the acquisition method, which requires identifying the acquirer, determining the acquisition date, and recognizing goodwill.")

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3 = st.tabs(["The 4-Step Method", "Goodwill & Gain", "Measurement Period"])

with tab1:
    st.markdown("#### 1. The Four Steps of the Acquisition Method")
    
    st.success("**Step 1: Identify the Acquirer**")
    st.write("The entity that obtains control of the acquiree.")
    
    st.success("**Step 2: Determine the Acquisition Date**")
    st.write("The date on which the acquirer effectively obtains control.")
    
    st.success("**Step 3: Recognize & Measure Assets/Liabilities**")
    st.write("Recognize identifiable assets acquired and liabilities assumed at their **Acquisition-Date Fair Values**.")
    
    st.success("**Step 4: Recognize Goodwill or a Bargain Purchase Gain**")
    st.write("The residual difference between the consideration transferred and the net assets acquired.")

    

with tab2:
    st.markdown("#### 2. Calculating Goodwill")
    st.write("Goodwill is recognized as an asset representing future economic benefits arising from assets that are not individually identified and separately recognized.")

    st.latex(r"Goodwill = (Consideration\ Transferred + Non-controlling\ Interest) - Net\ Identifiable\ Assets")

    col1, col2 = st.columns(2)
    with col1:
        st.error("**Bargain Purchase**")
        st.write("If the net assets acquired exceed the consideration paid, the difference is a 'Bargain Purchase Gain' recognized immediately in **Profit or Loss**.")
    with col2:
        st.info("**Non-controlling Interest (NCI)**")
        st.write("IFRS 3 allows a choice for each business combination to measure NCI at either:")
        st.markdown("""
        * **Fair Value** (Full Goodwill method).
        * **Proportionate Share** of the acquiree’s identifiable net assets.
        """)

    with st.expander("💰 What is Consideration Transferred?"):
        st.write("Includes cash, other assets, liabilities incurred by the acquirer, and equity interests issued. It also includes **Contingent Consideration** measured at fair value.")

with tab3:
    st.markdown("#### 3. Specific Rules & Measurement Period")
    
    st.warning("**The Measurement Period**")
    st.write("If the initial accounting for a business combination is incomplete by the end of the reporting period, the acquirer reports **provisional amounts**. The acquirer has up to **one year** from the acquisition date to finalize the fair values.")
    
    st.divider()
    
    with st.expander("🚫 Items Not Part of the Business Combination"):
        st.markdown("""
        * **Acquisition-related costs:** (Legal, advisory, brokerage fees) are **expensed** as incurred (not capitalized into the cost of the investment).
        * **Restructuring costs:** Costs the acquirer expects to incur in the future are NOT liabilities at the acquisition date.
        """)

# --- SIDEBAR CAPTION ---
st.sidebar.caption("Reference: International Financial Reporting Standard 3")