import streamlit as st
import random

st.set_page_config(layout="wide")

# ---------------- SESSION STATE ----------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_x" not in st.session_state:
    st.session_state.no_x = 0
    st.session_state.no_y = 0
    st.session_state.yes_scale = 1
    st.session_state.no_text = "No 😢"

# ---------------- FUNCTIONS ----------------
def move_no():
    st.session_state.no_x = random.randint(-200, 200)
    st.session_state.no_y = random.randint(-100, 100)
    st.session_state.yes_scale += 0.1

    texts = [
        "Are you sure? 😳",
        "Think again 😏",
        "Really? 😭",
        "Please say yes 💍",
        "Don't break my heart 💔"
    ]
    st.session_state.no_text = random.choice(texts)

# ---------------- PAGE 1 ----------------
if not st.session_state.accepted:

    st.markdown("""
    <style>
    .main {
        background-color: pink;
    }
    .center {
        text-align: center;
        margin-top: 120px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.markdown("<h1>Will you be my wife? 💍</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # YES BUTTON
    with col1:
        yes_style = f"""
        <style>
        div.stButton > button:first-child {{
            transform: scale({st.session_state.yes_scale});
            background-color: #ff4d6d;
            color: white;
            font-size: 20px;
            padding: 10px 20px;
        }}
        </style>
        """
        st.markdown(yes_style, unsafe_allow_html=True)

        if st.button("YES 💖"):
            st.session_state.accepted = True

    # NO BUTTON (moves)
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

# ---------------- PAGE 2 ----------------
else:
    st.balloons()

    st.markdown(
        "<h1 style='text-align:center; color:#ff4d6d;'>She said YES! ❤️</h1>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # IMAGE (replace with your file)
    st.image("your_image.jpg", use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # DOWNLOAD DOCX
    with open("letter.docx", "rb") as file:
        st.download_button(
            label="Download my letter 💌",
            data=file,
            file_name="love_letter.docx"
        )
