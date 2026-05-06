import streamlit as st
import pandas as pd

def show():
    # Custom CSS for a clean, executive aesthetic
    st.markdown("""
        <style>
        .main-header { font-size: 36px; color: #1E3A8A; font-weight: bold; border-bottom: 3px solid #1E3A8A; padding-bottom: 10px; }
        .overview-card { background-color: #FFFFFF; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); margin-bottom: 20px; }
        .module-tag { background-color: #1E3A8A; color: white; padding: 4px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; }
        .summary-text { font-size: 16px; color: #475569; margin-top: 10px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Leadership Mastery: Executive Overview</div>', unsafe_allow_html=True)
    st.write("Welcome to the comprehensive leadership development journey. This overview summarizes the core pillars of modern leadership excellence.")

    # 1. The Leadership Roadmap (Summary Table)
    st.subheader("📍 The Leadership Roadmap")
    roadmap_data = {
        "Module": ["1. Foundations", "2. Classic Models", "3. Dynamics", "4. Strategic", "5. Modern", "6. Personal"],
        "Core Focus": ["DNA & EQ", "Styles & Adaptation", "Power & Relationships", "Change & Teams", "Ethics & Global", "Presence & Coaching"],
        "Key Outcome": ["Mindset Shift", "Flexibility", "Trust Building", "Growth & Vision", "Resilience", "Legacy"]
    }
    st.table(pd.DataFrame(roadmap_data))

    # 2. Module Summaries
    st.subheader("📚 Module Deep-Dive Summaries")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
        <div class="overview-card">
            <span class="module-tag">Module 1</span>
            <div class="summary-text"><b>Foundations:</b> Transitioning from management to leadership. Focuses on Emotional Intelligence (EQ) and core character traits like integrity.</div>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <div class="overview-card">
            <span class="module-tag">Module 3</span>
            <div class="summary-text"><b>Dynamics:</b> Understanding the "In-Group" vs "Out-Group" (LMX Theory) and leveraging the 5 Bases of Power effectively.</div>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <div class="overview-card">
            <span class="module-tag">Module 5</span>
            <div class="summary-text"><b>Modern Challenges:</b> Navigating the complexities of inclusive leadership, remote teams, and the ethical "Bathsheba Syndrome."</div>
        </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
        <div class="overview-card">
            <span class="module-tag">Module 2</span>
            <div class="summary-text"><b>Classic Models:</b> Mastering Situational Leadership and Path-Goal Theory to clear obstacles for your team.</div>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <div class="overview-card">
            <span class="module-tag">Module 4</span>
            <div class="summary-text"><b>Strategic/Adaptive:</b> Leading through Tuckman's stages (Forming to Performing) and solving adaptive challenges.</div>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('''
        <div class="overview-card">
            <span class="module-tag">Module 6</span>
            <div class="summary-text"><b>Personal Growth:</b> Refining Executive Presence and moving from a "doer" to a "coach and mentor."</div>
        </div>
        ''', unsafe_allow_html=True)

    # 3. Final Reflection
    st.info("**The Golden Rule of this Syllabus:** Leadership is not a rank to attain, but a responsibility to live. Use these modules to build a framework that is authentic to your style and values.")

if __name__ == "__main__":
    show()