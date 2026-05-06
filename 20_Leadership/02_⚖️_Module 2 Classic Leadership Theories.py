import streamlit as st

def show():
    # Custom CSS for a professional look
    st.markdown("""
        <style>
        .main-header { font-size: 32px; color: #1E3A8A; font-weight: bold; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; }
        .sub-header { font-size: 24px; color: #1E40AF; margin-top: 25px; font-weight: semi-bold; }
        .content-text { font-size: 18px; line-height: 1.6; }
        .theory-card { background-color: #FFFFFF; padding: 20px; border-radius: 10px; border: 1px solid #E5E7EB; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .quiz-container { background-color: #F0FDF4; padding: 20px; border-radius: 10px; border: 1px solid #BBF7D0; margin-top: 30px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Module 2: Classic Leadership Theories & Models</div>', unsafe_allow_html=True)

    # 1. Path-Goal Theory
    st.markdown('<div class="sub-header">1. Path-Goal Theory</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="theory-card">
    <div class="content-text">
    Developed by Robert House, this theory focuses on how leaders motivate subordinates to accomplish designated goals. 
    The leader’s role is to <b>clear the path</b> for employees by:
    <ul>
        <li>Defining goals clearly.</li>
        <li>Clarifying the path to the goal.</li>
        <li>Removing obstacles.</li>
        <li>Providing support and rewards.</li>
    </ul>
    </div>
    </div>
    ''', unsafe_allow_html=True)

    # 2. Situational Leadership (Hersey-Blanchard)
    st.markdown('<div class="sub-header">2. Situational Leadership (Hersey-Blanchard)</div>', unsafe_allow_html=True)
    st.write("This model suggests there is no 'single best' style. A leader must adapt based on the **Readiness** (Competence + Commitment) of the team.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Directing", "Low Skill", "High Will")
    col2.metric("Coaching", "Some Skill", "Low Will")
    col3.metric("Supporting", "High Skill", "Variable Will")
    col4.metric("Delegating", "High Skill", "High Will")

    # 3. Transactional vs. Transformational
    st.markdown('<div class="sub-header">3. Transactional vs. Transformational</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="content-text">
    <ul>
        <li><b>Transactional Leadership:</b> Based on a system of exchange (rewards for performance, penalties for failure). It focuses on "getting the job done" within existing rules.</li>
        <li><b>Transformational Leadership:</b> Inspires followers to transcend their own self-interest for the sake of the organization. It involves <i>Idealized Influence, Inspirational Motivation, and Intellectual Stimulation</i>.</li>
    </ul>
    </div>
    ''', unsafe_allow_html=True)

    # Quiz Section
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("📝 Module 2 Mastery Quiz")
    
    q1 = st.radio("1. In Path-Goal Theory, what is the leader's primary responsibility?", 
                  ["Creating a new vision", "Clearing obstacles and clarifying the path", "Punishing low performance"])
    
    q2 = st.radio("2. Which leadership style is best for a team member who has 'High Skill' and 'High Will' (highly ready)?", 
                  ["Directing", "Coaching", "Delegating"])
    
    q3 = st.radio("3. Which theory focuses on 'inspiring' followers to transcend self-interest?", 
                  ["Transactional", "Transformational", "Path-Goal"])
    
    if st.button("Check Answers"): 
        if q1 == "Clearing obstacles and clarifying the path" and q2 == "Delegating" and q3 == "Transformational":
            st.balloons()
            st.success("Mastery Confirmed! You've successfully navigated the classic models.")
        else:
            st.error("Some answers were incorrect. Review the theories and try again!")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()