import streamlit as st

st.title("🧑‍🎓 About Me")
st.markdown("---")

# Intro Section
st.subheader("✨ Who Am I?")
st.write("""
I'm Imari Janella, a dedicated student who loves exploring new ideas and growing 
my abilities every day. I'm detail-oriented, flexible in different situations, 
and always happy to collaborate with my classmates.
""")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🎯 Core Traits")
    st.markdown("""
    - Detail-oriented
    - Flexible & Adaptable
    - Quick Learner
    - Team Player
    - Good Observer
    """)

with col2:
    st.markdown("#### 💜 My Interests")
    st.markdown("""
    - Technology
    - Astrology ✨🌙
    - Health & Wellness
    - Learning New Things
    """)

st.markdown("---")

# Fun Fact
st.subheader("💬 My Philosophy")
st.info("""
I believe that learning never stops. Every day is a chance to grow,
explore new ideas, and become a better version of myself.
""")