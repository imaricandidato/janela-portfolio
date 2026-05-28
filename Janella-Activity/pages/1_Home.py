import streamlit as st

st.title("🏠 Home")
st.markdown("### Hi, I'm Imari Janella! ✨")

# Three Column Layout
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.metric("🎓 Student", "Active")

with col2:
    st.metric("🌟 Learner", "Growing")

with col3:
    st.metric("🤝 Team Player", "Ready")

st.markdown("---")

# Main Introduction
st.subheader("💜 Welcome to My Space")
st.write("""
I am a dedicated student who loves exploring new ideas and growing my abilities every day.
This is my little corner of the internet where I share a bit about myself,
my skills, and what I love to do.
""")

st.markdown("#### 🌙 My Current Vibes")
st.progress(75)

# Quote Box
st.success("""
*"Every day is a new opportunity to learn something extraordinary."*
— Imari
""")