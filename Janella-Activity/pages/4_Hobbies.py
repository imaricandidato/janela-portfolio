import streamlit as st

st.title("🎮 Hobbies & Interests")
st.markdown("### What I Love to Do")
st.write("---")

# Hobby Categories
st.markdown("#### 🎯 Active Hobbies")

h1, h2 = st.columns(2)

with h1:
    st.info("🏀 Basketball & Badminton")
    st.write("Staying active and competitive!")

with h2:
    st.info("🎮 Online Gaming")
    st.write("Playing games to relax and have fun!")

st.markdown("---")

st.markdown("#### 📚 Learning Hobbies")

h3, h4 = st.columns(2)

with h3:
    st.info("📖 Reading")
    st.write("Law books and stories")

with h4:
    st.info("✨ Astrology")
    st.write("Exploring the stars and zodiac")

st.markdown("---")

st.markdown("#### 🏠 Home Life")

h5, h6 = st.columns(2)

with h5:
    st.info("🧹 Household Chores")
    st.write("Keeping things tidy")

with h6:
    st.info("🎤 Singing & Eating")
    st.write("My favorite pastimes!")

st.markdown("---")

# Fun Summary
st.success("""
✨ When I'm not studying, you'll find me playing games, shooting hoops,
reading interesting stories, or just enjoying good food and music!
""")