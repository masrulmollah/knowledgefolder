import streamlit as st
import pandas as pd

def show():
    # Custom CSS for a professional, strategic look
    st.markdown("""
        <style>
        .main-header { font-size: 32px; color: #1E3A8A; font-weight: bold; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; }
        .sub-header { font-size: 24px; color: #1E40AF; margin-top: 25px; font-weight: semi-bold; }
        .content-text { font-size: 18px; line-height: 1.6; }
        .strategic-card { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border-top: 5px solid #0EA5E9; margin-bottom: 20px; }
        .quiz-container { background-color: #FDF2F8; padding: 20px; border-radius: 10px; border: 1px solid #FBCFE8; margin-top: 30px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Module 4: Strategic & Adaptive Leadership</div>', unsafe_allow_html=True)

    # 1. Adaptive Leadership
    st.markdown('<div class="sub-header">1. Adaptive Leadership</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="content-text">
    Adaptive leadership is the practice of mobilizing people to tackle tough challenges and thrive. It distinguishes between:
    <ul>
        <li><b>Technical Challenges:</b> Problems with known solutions that experts can solve (e.g., fixing a software bug).</li>
        <li><b>Adaptive Challenges:</b> Problems with no clear answers that require changes in people's values, beliefs, or habits (e.g., changing company culture).</li>
    </ul>
    </div>
    ''', unsafe_allow_html=True)

    # 2. Tuckman’s Stages of Group Development
    st.markdown('<div class="sub-header">2. Building High-Performing Teams</div>', unsafe_allow_html=True)
    st.write("To lead a team strategically, you must recognize which stage of development they are in:")
    
    stages_data = {
        "Stage": ["Forming", "Storming", "Norming", "Performing", "Adjourning"],
        "Team Behavior": [
            "High dependence on leader for guidance.",
            "Competition and conflict as individualities emerge.",
            "Agreement and consensus; roles become clear.",
            "Strategic awareness; high degree of autonomy.",
            "Task completion; feeling of loss or achievement."
        ]
    }
    st.table(pd.DataFrame(stages_data))

    # 3. Visionary Leadership & Decision Making
    st.markdown('<div class="sub-header">3. Vision & Decision Frameworks</div>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="strategic-card">
    <b>Visionary Leadership:</b> The ability to see beyond the current state and communicate a future that inspires others. 
    It requires <i>Environmental Scanning</i> (understanding external trends) and <i>Strategic Alignment</i> (linking team goals to the big picture).
    </div>
    ''', unsafe_allow_html=True)

    # Quiz Section
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("📝 Module 4 Mastery Quiz")
    
    q1 = st.radio("Which type of challenge requires a change in people's values and habits?", 
                  ["Technical Challenge", "Adaptive Challenge"])
    
    q2 = st.radio("In which of Tuckman's stages is the team most autonomous and effective?", 
                  ["Storming", "Norming", "Performing"])
    
    if st.button("Submit Module 4 Quiz"): 
        if q1 == "Adaptive Challenge" and q2 == "Performing":
            st.balloons()
            st.success("Strategic Thinking Confirmed! You've mastered Module 4.")
        else:
            st.error("Review the difference between Technical vs. Adaptive challenges and the Tuckman table!")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()