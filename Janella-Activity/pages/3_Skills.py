import streamlit as st

st.title("⚡ Skills")
st.markdown("### What I Bring to the Table")
st.write("---")

# Creative Skills Display
st.markdown("#### 🔧 Technical Skills")

# Skill bars with different styling
st.markdown("**Electrical Wiring**")
st.progress(85)

st.markdown("**Problem Solving**")
st.progress(80)

st.markdown("**Technology Knowledge**")
st.progress(70)

st.markdown("---")

# Personal Skills
st.markdown("#### 🌟 Personal Skills")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👀 Good Observer", "High", "")

with c2:
    st.metric("⚡ Quick Learner", "High", "")

with c3:
    st.metric("🤝 Team Player", "High", "")

st.markdown("---")

# Additional Skills
st.markdown("#### 📋 Additional Strengths")
st.write("""
✅ Detail-oriented  ✅ Flexible  ✅ Adaptable  
✅ Willing to collaborate  ✅ Open to new ideas
""")