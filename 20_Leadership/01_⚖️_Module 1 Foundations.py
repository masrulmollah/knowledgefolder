import streamlit as st

def show():
    # Page header and custom styling
    st.markdown("""
        <style>
        .main-header { font-size: 32px; color: #1E3A8A; font-weight: bold; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; }
        .sub-header { font-size: 24px; color: #1E40AF; margin-top: 25px; font-weight: semi-bold; }
        .content-text { font-size: 18px; line-height: 1.6; }
        .highlight-box { background-color: #F3F4F6; padding: 20px; border-left: 5px solid #1E3A8A; border-radius: 5px; margin: 15px 0; }
        .quiz-container { background-color: #EFF6FF; padding: 20px; border-radius: 10px; border: 1px solid #BFDBFE; margin-top: 30px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Module 1: Foundations of Leadership</div>', unsafe_allow_html=True)

    # 1. Leadership vs Management
    st.markdown('<div class="sub-header">1. Leadership vs. Management</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="content-text">
    While often used interchangeably, leadership and management are distinct functions.
    <ul>
        <li><b>Management:</b> Focuses on systems and processes. It is about order, predictability, and efficiency.</li>
        <li><b>Leadership:</b> Focuses on people and vision. It is about alignment, motivation, and inspiration.</li>
    </ul>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="highlight-box"><b>Real-World Example:</b> A <i>Manager</i> ensures a complex 12,000-asset audit is completed on schedule. A <i>Leader</i> inspires the team to understand that their accuracy protects the organization\'s reputation.</div>', unsafe_allow_html=True)

    # 2. Core Traits
    st.markdown('<div class="sub-header">2. Core Traits & The Born vs. Made Debate</div>', unsafe_allow_html=True)
    st.write("The **Trait Approach** focuses on innate qualities like Intelligence, Self-Confidence, and Integrity. In contrast, the **Behavioral Approach** argues that leadership is a set of skills that can be observed and learned over time.")

    # 3. Emotional Intelligence (EQ)
    st.markdown('<div class="sub-header">3. Emotional Intelligence (EQ)</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="content-text">
    EQ is often considered the "secret sauce" of great leaders. It consists of five key pillars:
    <ul>
        <li><b>Self-Awareness:</b> Recognizing your own emotions and their impact.</li>
        <li><b>Self-Regulation:</b> Thinking before acting and controlling impulses.</li>
        <li><b>Motivation:</b> A passion to work for reasons beyond money or status.</li>
        <li><b>Empathy:</b> Understanding the emotional makeup of others.</li>
        <li><b>Social Skill:</b> Proficiency in managing relationships and building networks.</li>
    </ul>
    </div>
    ''', unsafe_allow_html=True)

    # Quiz Section
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("📝 Module 1 Mastery Quiz")
    
    q1 = st.radio("1. Which role is primarily concerned with 'Inspiring and Aligning People'?", ["Management", "Leadership"])
    q2 = st.radio("2. Which EQ component involves the ability to 'think before you act'?", ["Self-Awareness", "Self-Regulation", "Empathy"])
    
    if st.button("Submit Quiz"): 
        if q1 == "Leadership" and q2 == "Self-Regulation":
            st.balloons()
            st.success("Perfect! You've mastered the foundations of Module 1.")
        else:
            st.warning("Almost there! Review the sections above and try again.")
    st.markdown('</div>', unsafe_allow_html=True)

# Calling the function to render content
if __name__ == "__main__":
    show()