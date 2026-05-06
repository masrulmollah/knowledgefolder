import streamlit as st
import pandas as pd

def show():
    # Custom CSS for a clean, personal development focus
    st.markdown("""
        <style>
        .main-header { font-size: 32px; color: #1E3A8A; font-weight: bold; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; }
        .sub-header { font-size: 24px; color: #1E40AF; margin-top: 25px; font-weight: semi-bold; }
        .content-text { font-size: 18px; line-height: 1.6; }
        .dev-card { background-color: #FDFEE2; padding: 20px; border-radius: 10px; border-left: 5px solid #FACC15; margin-bottom: 20px; }
        .quiz-container { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border: 1px solid #CBD5E1; margin-top: 30px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Module 6: Personal Leadership Development</div>', unsafe_allow_html=True)

    # 1. Executive Presence & 360 Feedback
    st.markdown('<div class="sub-header">1. Executive Presence & Feedback</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="content-text">
    Developing as a leader requires looking inward as much as outward.
    <ul>
        <li><b>Executive Presence:</b> The blend of temperament, competency, and skills that sends the signal you are "in charge" or "ready for charge." It is often defined by <i>Gravitas, Communication, and Appearance</i>.</li>
        <li><b>360-Degree Feedback:</b> A process where you receive confidential, anonymous feedback from the people who work around you (boss, peers, and direct reports).</li>
    </ul>
    </div>
    ''', unsafe_allow_html=True)

    # 2. Mentorship vs. Coaching
    st.markdown('<div class="sub-header">2. Developing Others: Mentorship vs. Coaching</div>', unsafe_allow_html=True)
    st.write("To scale your impact, you must learn to grow other leaders:")
    
    dev_data = {
        "Feature": ["Orientation", "Focus", "Role of Leader", "Timeline"],
        "Coaching": ["Task/Performance", "Immediate Skills", "Asks questions to find answers", "Short-term/Specific"],
        "Mentorship": ["Relationship/Career", "Future Growth", "Shares own experiences/answers", "Long-term/Ongoing"]
    }
    st.table(pd.DataFrame(dev_data))

    # 3. Sustainable Leadership (Burnout Prevention)
    st.markdown('<div class="sub-header">3. Sustainable Leadership</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="dev-card">
    <b>Self-Care as a Strategy:</b> Leadership is a marathon. Sustainable leaders manage their energy, not just their time. 
    They practice <i>Reflective Silence</i> and set boundaries to prevent burnout for themselves and their teams.
    </div>
    ''', unsafe_allow_html=True)

    # Quiz Section
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("📝 Module 6 Mastery Quiz")
    
    q1 = st.radio("Which development approach is more focused on 'asking powerful questions' to help the individual find their own solution?", 
                  ["Mentorship", "Coaching"])
    
    q2 = st.radio("Executive Presence is generally composed of which three pillars?", 
                  ["IQ, Technical Skill, Tenure", "Gravitas, Communication, Appearance", "Power, Control, Authority"])
    
    if st.button("Complete Final Module"): 
        if q1 == "Coaching" and q2 == "Gravitas, Communication, Appearance":
            st.balloons()
            st.success("Congratulations! You have completed the full Leadership Syllabus.")
        else:
            st.error("Almost there! Review the Mentorship vs. Coaching table and the Executive Presence section.")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()