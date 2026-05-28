import streamlit as st

st.title("📞 Contact Me")
st.markdown("### Let's Connect!")
st.write("---")

# Contact Info Card
st.markdown("#### 💜 Get in Touch")

st.markdown("""
**📱 Phone:** 09853725583  
**📧 Email:** candidatojanella48@gmail.com
""")

st.markdown("---")

# Simple Contact Form
st.markdown("#### ✉️ Send a Message")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send ✨")

    if submit:
        if name and email and message:
            st.success(f"Thank you, {name}! Message sent successfully! 💜")
        else:
            st.error("Please fill in all fields.")

st.markdown("---")
st.caption("© 2024 Imari's Portfolio | Created with 💜")