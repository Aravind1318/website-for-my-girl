import streamlit as st
import random
from streamlit_extras.let_it_rain import rain

st.set_page_config(layout="wide")

if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_x" not in st.session_state:
    st.session_state.no_x = 50
    st.session_state.no_y = 50
    st.session_state.yes_size = 1
    st.session_state.no_text = "No"

def move_no():
    st.session_state.no_x = random.randint(10, 90)
    st.session_state.no_y = random.randint(10, 90)
    st.session_state.yes_size += 0.2

    texts = ["Are you sure?", "Think again 😏", "Really? 😢", "Try Yes 💍"]
    st.session_state.no_text = random.choice(texts)

if not st.session_state.accepted:

    st.markdown(
        """
        <style>
        body {
            background-color: pink;
        }
        .center-box {
            text-align: center;
            margin-top: 150px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    st.markdown("<h1>Will you be my wife? 💍</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💖"):
            st.session_state.accepted = True

    with col2:
        st.markdown(
            f"""
            <div style="
                position: relative;
                left: {st.session_state.no_x}px;
                top: {st.session_state.no_y}px;">
            """,
            unsafe_allow_html=True
        )

        if st.button(st.session_state.no_text):
            move_no()

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

else:
    rain(emoji="🎉", font_size=54, falling_speed=5)

    st.markdown("<h1 style='text-align:center;'>She said YES! ❤️</h1>", unsafe_allow_html=True)

    st.image("your_image.jpg", use_container_width=True)

    with open("letter.docx", "rb") as file:
        st.download_button(
            label="Download my letter 💌",
            data=file,
            file_name="love_letter.docx"
        )
