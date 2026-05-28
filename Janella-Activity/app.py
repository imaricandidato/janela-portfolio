import streamlit as st

st.set_page_config(
    page_title="Imari | My Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600;700&display=swap');

        * {
            font-family: 'Quicksand', sans-serif;
        }

        /* Background Gradient */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
            color: #2d3748;
        }

        /* Main Text */
        p, li, span, div {
            color: #2d3748 !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }

        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Headers */
        h1, h2, h3, h4 {
            color: #5e3a9e !important;
            font-weight: 700;
        }

        /* Custom Success/Info Boxes */
        .stAlert {
            background: linear-gradient(90deg, #c471ed 0%, #f64f59 100%);
            border-radius: 15px;
            border: none;
            color: white !important;
        }

        /* Buttons or Preview Cards */
        .stButton>button {
            background: linear-gradient(90deg, #8e2de2 0%, #ff6a88 100%);
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 10px 20px;
            font-weight: 600;
        }

        /* Markdown text */
        .markdown-text-container {
            color: #2d3748 !important;
        }

    </style>
""", unsafe_allow_html=True)

st.title("✨ Welcome to My World")
st.markdown("---")
st.write("""
Discover my journey, skills, and interests through this portal.
Let's explore together!
""")

st.markdown("### 🌟 Quick Preview")

# Quick Stats Row
col1, col2, col3 = st.columns(3)
col1.info("📚 Lifelong Learner")
col2.info("⚡ Problem Solver")
col3.info("🌙 Astrology Lover")

# Sidebar Content
with st.sidebar:
    st.markdown("### ✨ Imari Janella")
    st.caption("Student | Dreamer | Creator")
    st.markdown("---")
    st.write("**📌 Navigation**")
    st.write("- Home")
    st.write("- About Me")
    st.write("- Skills")
    st.write("- Hobbies")
    st.write("- Contact")
    st.markdown("---")
    st.caption("© 2024 Imari's Portfolio")