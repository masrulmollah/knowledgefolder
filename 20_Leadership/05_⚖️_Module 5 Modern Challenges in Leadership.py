import streamlit as st
import pandas as pd

def show():
    # Custom CSS for a modern, clean aesthetic
    st.markdown("""
        <style>
        .main-header { font-size: 32px; color: #1E3A8A; font-weight: bold; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px; }
        .sub-header { font-size: 24px; color: #1E40AF; margin-top: 25px; font-weight: semi-bold; }
        .content-text { font-size: 18px; line-height: 1.6; }
        .modern-card { background-color: #F0F9FF; padding: 20px; border-radius: 10px; border-right: 5px solid #0EA5E9; margin-bottom: 20px; }
        .quiz-container { background-color: #F0FDFA; padding: 20px; border-radius: 10px; border: 1px solid #5EEAD4; margin-top: 30px; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-header">Module 5: Modern Challenges in Leadership</div>', unsafe_allow_html=True)

    # 1. Inclusive and Remote Leadership
    st.markdown('<div class="sub-header">1. Diversity & Remote Work</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="content-text">
    In today's global environment, leadership requires a shift in how we manage presence and participation.
    <ul>
        <li><b>Inclusive Leadership:</b> Ensuring every voice is heard, regardless of background. This reduces "Groupthink."</li>
        <li><b>Remote/Hybrid Leadership:</b> Shifting from "Time-at-Desk" to "Value-Produced." It requires high trust and asynchronous communication.</li>
    </ul>
    </div>
    ''', unsafe_allow_html=True)

    # 2. Crisis Leadership Table
    st.markdown('<div class="sub-header">2. Leading Through Crisis</div>', unsafe_allow_html=True)
    st.write("When the stakes are high and information is low, leaders must act decisively:")
    
    crisis_data = {
        "Phase": ["Preparation", "Response", "Recovery"],
        "Leader's Focus": ["Risk Assessment & Planning", "Clear Communication & Fast Action", "Learning & Rebuilding Trust"],
        "Key Skill": ["Foresight", "Composure", "Reflection"]
    }
    st.table(pd.DataFrame(crisis_data))

    # 3. The Bathsheba Syndrome (Ethical Leadership)
    st.markdown('<div class="sub-header">3. The Ethics of Success</div>', unsafe_allow_html=True)
    st.markdown('''
    <div class="modern-card">
    <b>The Bathsheba Syndrome:</b> A phenomenon where highly successful leaders fail ethically, not because of pressure, 
    but because they begin to feel "above the rules" due to their status. 
    <br><br>
    <i>Prevention:</i> Maintain a strong accountability circle and stay grounded in core values.
    </div>
    ''', unsafe_allow_html=True)

    # Quiz Section
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    st.subheader("📝 Module 5 Mastery Quiz")
    
    q1 = st.radio("What is the primary cause of ethical failure in 'The Bathsheba Syndrome'?", 
                  ["Financial pressure", "A sense of entitlement following success", "Lack of education"])
    
    q2 = st.radio("When leading remote teams, what should be the primary metric of success?", 
                  ["Hours spent online", "Value and output produced", "Number of meetings attended"])
    
    if st.button("Submit Module 5 Quiz"): 
        if q1 == "A sense of entitlement following success" and q2 == "Value and output produced":
            st.balloons()
            st.success("Modern Leadership Mastery Achieved! You are ready for the final module.")
        else:
            st.error("Consider the ethical and remote work sections again!")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()