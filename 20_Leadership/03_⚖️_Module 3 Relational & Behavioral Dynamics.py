import streamlit as st
import pandas as pd

def show():
    # Custom CSS for a professional look
    st.markdown("""
        <style>
        .main-header { font-size: 32px; color: #1E3A8A; font-weight: bold; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; }
        .sub-header { font-size: 24px; color: #1E40AF; margin-top: 25px; font-weight: semi-bold; }
        .content-text { font-size: 18px; line-height: 1.6; }
        .dynamic-card { background-color: #F9FAFB; padding: 20px; border-radius: 10px; border-left: 5px solid #3B82F6; margin-bottom: 20px; }
        .quiz-container { background-color: #FFF7ED; padding: 20px; border-radius: 10px; border: 1px solid #FED7AA; margin-top: 30px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Module 3: Relational & Behavioral Dynamics</div>', unsafe_allow_html=True)

    # 1. Leader-Member Exchange (LMX) Theory
    st.markdown('<div class="sub-header">1. Leader-Member Exchange (LMX) Theory</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="content-text">
    LMX theory moves away from how leaders treat "groups" and looks at the <b>dyadic relationship</b> between a leader and each individual follower.
    </div>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("**The In-Group**")
        st.write("Based on expanded role responsibilities. Followers receive more information, influence, and confidence from the leader.")
    with col2:
        st.warning("**The Out-Group**")
        st.write("Based on the formal employment contract. Followers are less compatible with the leader and usually just 'do their job'.")

    # 2. Servant and Authentic Leadership
    st.markdown('<div class="sub-header">2. Servant & Authentic Leadership</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="dynamic-card"><b>Servant Leadership:</b> A paradox where the leader is a servant first. It begins with the natural feeling that one wants to serve, to serve first. Then conscious choice brings one to aspire to lead.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="dynamic-card"><b>Authentic Leadership:</b> Focuses on whether leadership is "genuine." Leaders are self-aware, transparent, and guided by internal moral standards rather than external pressures.</div>', unsafe_allow_html=True)

    # 3. The 5 Bases of Power
    st.markdown('<div class="sub-header">3. Power and Influence</div>', unsafe_allow_html=True)
    st.write("To lead effectively, you must understand where your power comes from:")
    
    power_data = {
        "Type of Power": ["Legitimate", "Reward", "Coercive", "Expert", "Referent"],
        "Source": ["Formal Position", "Ability to give bonuses/praise", "Ability to punish", "Knowledge and Skills", "Personal Charisma/Likeability"],
        "Impact": ["Compliance", "Compliance", "Resistance", "Commitment", "Commitment"]
    }
    st.table(pd.DataFrame(power_data))

    # Quiz Section
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("📝 Module 3 Mastery Quiz")
    
    q1 = st.radio("Which type of power is most likely to lead to high team 'Commitment'?", 
                  ["Coercive", "Legitimate", "Expert & Referent"])
    
    q2 = st.radio("In LMX Theory, what defines the 'In-Group' relationship?", 
                  ["High trust and extra responsibilities", "Strict adherence to the contract", "Frequent punishments"])
    
    if st.button("Submit Module 3 Quiz"): 
        if q1 == "Expert & Referent" and q2 == "High trust and extra responsibilities":
            st.balloons()
            st.success("Brilliant! You understand the nuances of leadership relationships.")
        else:
            st.error("Take a quick look at the Power Table and LMX sections again!")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()