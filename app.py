import streamlit as st
import base64
import os
import random

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="💍 A Special Question", page_icon="💍", layout="centered")

# ── Session state ─────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "question"

# ── Helper: encode file to base64 ────────────────────────────────────────────
def file_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 1 – The Question
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "question":

    st.markdown("""
    <style>
    /* ── Global reset & pink background ── */
    html, body, [data-testid="stApp"] {
        background-color: #FFB6C1 !important;
        font-family: 'Georgia', serif;
    }
    [data-testid="stAppViewContainer"] { background-color: #FFB6C1 !important; }
    [data-testid="stHeader"]           { background-color: transparent !important; }
    [data-testid="stToolbar"]          { display: none !important; }
    .block-container { padding-top: 4rem !important; }

    /* ── Question text ── */
    .question-text {
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        color: #8B0038;
        text-shadow: 2px 2px 6px rgba(255,255,255,0.6);
        margin-bottom: 0.4rem;
        line-height: 1.3;
    }
    .hearts { text-align: center; font-size: 2rem; margin-bottom: 2.5rem; }

    /* ── Button area ── */
    .btn-area {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-top: 1rem;
        position: relative;
        min-height: 140px;
    }

    /* ── YES button ── */
    #yes-btn {
        background: linear-gradient(135deg, #e91e63, #ff4081);
        color: white;
        border: none;
        padding: 18px 52px;
        font-size: 1.5rem;
        font-weight: bold;
        border-radius: 50px;
        cursor: pointer;
        box-shadow: 0 6px 20px rgba(233,30,99,0.45);
        transition: transform 0.15s ease, box-shadow 0.15s ease, font-size 0.3s ease;
        font-family: 'Georgia', serif;
    }
    #yes-btn:hover {
        transform: scale(1.18);
        box-shadow: 0 10px 30px rgba(233,30,99,0.6);
        font-size: 1.65rem;
    }

    /* ── NO button ── */
    #no-btn {
        background: linear-gradient(135deg, #9e9e9e, #bdbdbd);
        color: white;
        border: none;
        padding: 14px 40px;
        font-size: 1.2rem;
        border-radius: 50px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transition: background 0.2s;
        font-family: 'Georgia', serif;
        position: absolute;
    }

    /* ── Streamlit button hide ── */
    #yes-trigger { display: none !important; }
    </style>

    <div class="question-text">💍 Will You Be My Wife? 💍</div>
    <div class="hearts">💖 💕 💗 💓 💞</div>

    <div class="btn-area" id="btn-area">
        <button id="yes-btn" onclick="yesClicked()">Yes! 🥰</button>
        <button id="no-btn" onmouseenter="runAway(this)" onclick="runAway(this)">No 😔</button>
    </div>

    <!-- hidden streamlit trigger -->
    <button id="yes-trigger" onclick="void(0)"></button>

    <script>
    const noTexts = [
        "No 😔", "Are you sure? 🤔", "Think again! 😅",
        "Please? 🥺", "Noooo! 😭", "Come on! 💕",
        "Last chance! 😬", "Really?? 😢", "Don't do this! 🙈"
    ];
    let noIdx = 0;

    function runAway(btn) {
        const area = document.getElementById('btn-area');
        const areaRect = area.getBoundingClientRect();
        const maxX = areaRect.width  - btn.offsetWidth  - 10;
        const maxY = areaRect.height - btn.offsetHeight - 10;
        const rx = Math.max(0, Math.random() * maxX);
        const ry = Math.max(0, Math.random() * maxY);
        btn.style.left = rx + 'px';
        btn.style.top  = ry + 'px';
        noIdx = (noIdx + 1) % noTexts.length;
        btn.innerText = noTexts[noIdx];
    }

    function yesClicked() {
        // Fire the hidden Streamlit button to flip session state
        const btns = window.parent.document.querySelectorAll('button');
        for (let b of btns) {
            if (b.innerText.trim() === '__YES__') { b.click(); break; }
        }
    }
    </script>
    """, unsafe_allow_html=True)

    # Hidden Streamlit button that JS triggers
    if st.button("__YES__", key="yes_hidden"):
        st.session_state.page = "yes"
        st.rerun()

    # Visible fallback YES (in case JS blocked)
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("✨ Yes! ✨", key="yes_fallback", help="Click here if the button above doesn't work"):
            st.session_state.page = "yes"
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 2 – She Said Yes! 🎉
# ══════════════════════════════════════════════════════════════════════════════
else:
    # ── Prepare downloadable docx ──────────────────────────────────────────
    docx_path = os.path.join(os.path.dirname(__file__), "love_letter.docx")
    docx_b64 = file_to_b64(docx_path) if os.path.exists(docx_path) else None

    # ── Prepare photo (placeholder or real) ───────────────────────────────
    photo_path = os.path.join(os.path.dirname(__file__), "photo.jpg")
    photo_exists = os.path.exists(photo_path)
    if photo_exists:
        photo_b64  = file_to_b64(photo_path)
        photo_html = f'<img src="data:image/jpeg;base64,{photo_b64}" class="couple-photo" alt="Our photo"/>'
    else:
        photo_html = """
        <div class="photo-placeholder">
            📸<br>
            <small>Replace <code>photo.jpg</code> in the app folder<br>with your photo and restart!</small>
        </div>"""

    docx_link = ""
    if docx_b64:
        docx_link = f"""
        <a class="download-btn" href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{docx_b64}"
           download="love_letter.docx">
            💌 Download Our Love Letter
        </a>"""

    st.markdown(f"""
    <style>
    html, body, [data-testid="stApp"],
    [data-testid="stAppViewContainer"] {{
        background-color: #FFF0F5 !important;
        font-family: 'Georgia', serif;
    }}
    [data-testid="stHeader"] {{ background: transparent !important; }}
    [data-testid="stToolbar"] {{ display:none !important; }}
    .block-container {{ padding-top: 1rem !important; }}

    /* ── Confetti canvas ── */
    #confetti-canvas {{
        position: fixed; top: 0; left: 0;
        width: 100%; height: 100%;
        pointer-events: none; z-index: 9999;
    }}

    /* ── Content card ── */
    .yes-card {{
        background: rgba(255,255,255,0.82);
        backdrop-filter: blur(8px);
        border-radius: 28px;
        padding: 2.5rem 2rem;
        max-width: 560px;
        margin: 2rem auto;
        text-align: center;
        box-shadow: 0 12px 40px rgba(233,30,99,0.18);
        border: 2px solid #f48fb1;
    }}
    .yes-title {{
        font-size: 2.6rem;
        color: #880E4F;
        font-weight: bold;
        margin-bottom: 0.3rem;
    }}
    .yes-sub {{
        font-size: 1.1rem;
        color: #c2185b;
        margin-bottom: 1.8rem;
    }}
    .couple-photo {{
        width: 100%; max-width: 420px;
        border-radius: 20px;
        border: 4px solid #f48fb1;
        box-shadow: 0 8px 24px rgba(233,30,99,0.25);
        margin-bottom: 1.6rem;
        display: block; margin-left: auto; margin-right: auto;
    }}
    .photo-placeholder {{
        width: 100%; max-width: 420px;
        height: 260px;
        border-radius: 20px;
        border: 4px dashed #f48fb1;
        background: #fce4ec;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        font-size: 3rem; color: #c2185b;
        margin: 0 auto 1.6rem auto;
    }}
    .photo-placeholder small {{
        font-size: 0.8rem; color: #880E4F; margin-top: 0.5rem; line-height: 1.5;
    }}
    .download-btn {{
        display: inline-block;
        background: linear-gradient(135deg, #e91e63, #ff4081);
        color: white !important;
        text-decoration: none;
        padding: 14px 36px;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 6px 20px rgba(233,30,99,0.35);
        transition: transform 0.15s, box-shadow 0.15s;
        margin-top: 0.5rem;
    }}
    .download-btn:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 28px rgba(233,30,99,0.5);
    }}
    </style>

    <!-- Confetti canvas -->
    <canvas id="confetti-canvas"></canvas>

    <div class="yes-card">
        <div class="yes-title">She Said YES! 💍</div>
        <div class="yes-sub">This is just the beginning of forever 🌹</div>
        {photo_html}
        {docx_link}
    </div>

    <script>
    // ── Confetti ────────────────────────────────────────────────────────────
    (function() {{
        const canvas = document.getElementById('confetti-canvas');
        const ctx    = canvas.getContext('2d');

        function resize() {{
            canvas.width  = window.innerWidth;
            canvas.height = window.innerHeight;
        }}
        resize();
        window.addEventListener('resize', resize);

        const COLORS = ['#ff4081','#f06292','#e91e63','#ff80ab',
                         '#fff176','#ce93d8','#80cbc4','#ffffff','#ffb6c1'];
        const SHAPES = ['circle','rect','heart'];

        class Flake {{
            constructor() {{ this.reset(true); }}
            reset(initial) {{
                this.x     = Math.random() * canvas.width;
                this.y     = initial ? Math.random() * -canvas.height : -20;
                this.size  = 6 + Math.random() * 10;
                this.speed = 1.5 + Math.random() * 3.5;
                this.drift = (Math.random() - 0.5) * 1.2;
                this.rot   = Math.random() * Math.PI * 2;
                this.rotV  = (Math.random() - 0.5) * 0.08;
                this.color = COLORS[Math.floor(Math.random() * COLORS.length)];
                this.shape = SHAPES[Math.floor(Math.random() * SHAPES.length)];
                this.alpha = 0.75 + Math.random() * 0.25;
            }}
            draw() {{
                ctx.save();
                ctx.globalAlpha = this.alpha;
                ctx.fillStyle   = this.color;
                ctx.translate(this.x, this.y);
                ctx.rotate(this.rot);
                if (this.shape === 'circle') {{
                    ctx.beginPath();
                    ctx.arc(0, 0, this.size / 2, 0, Math.PI * 2);
                    ctx.fill();
                }} else if (this.shape === 'rect') {{
                    ctx.fillRect(-this.size/2, -this.size/4, this.size, this.size/2);
                }} else {{
                    // heart
                    const s = this.size * 0.35;
                    ctx.beginPath();
                    ctx.moveTo(0, s);
                    ctx.bezierCurveTo( s*2,  -s,  s*3.5, s*1.5, 0, s*3);
                    ctx.bezierCurveTo(-s*3.5, s*1.5, -s*2,  -s,  0, s);
                    ctx.fill();
                }}
                ctx.restore();
            }}
            update() {{
                this.y   += this.speed;
                this.x   += this.drift;
                this.rot += this.rotV;
                if (this.y > canvas.height + 20) this.reset(false);
            }}
        }}

        const flakes = Array.from({{length: 180}}, () => new Flake());

        function loop() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            flakes.forEach(f => {{ f.update(); f.draw(); }});
            requestAnimationFrame(loop);
        }}
        loop();
    }})();
    </script>
    """, unsafe_allow_html=True)
