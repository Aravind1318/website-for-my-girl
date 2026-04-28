import streamlit as st
import base64
import os

st.set_page_config(page_title="💍 A Special Question", page_icon="💍", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "question"

def file_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 1 – The Question
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "question":

    yes_clicked = st.button("__YES__", key="yes_hidden")
    if yes_clicked:
        st.session_state.page = "yes"
        st.rerun()

    st.markdown("""
    <style>
    #MainMenu, footer, header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    .stDeployButton { display: none !important; }

    /* Hide the hidden trigger button */
    [data-testid="stMainBlockContainer"] > div:first-child { display: none !important; }

    html, body,
    [data-testid="stApp"],
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .block-container {
        background-color: #FFB6C1 !important;
        font-family: 'Georgia', serif !important;
        padding: 0 !important; margin: 0 !important;
        max-width: 100% !important;
    }

    #proposal-overlay {
        position: fixed; inset: 0;
        background: #FFB6C1;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        z-index: 9999; overflow: hidden;
    }
    .question-text {
        font-size: 3rem; font-weight: bold;
        color: #8B0038; text-align: center;
        text-shadow: 2px 2px 8px rgba(255,255,255,0.5);
        margin-bottom: 0.4rem; padding: 0 1rem;
    }
    .hearts { font-size: 2rem; margin-bottom: 3.5rem; text-align: center; }

    .proposal-btn {
        padding: 18px 56px;
        font-size: 1.45rem; font-weight: bold;
        border: none; border-radius: 50px;
        cursor: pointer; font-family: 'Georgia', serif;
        box-shadow: 0 6px 22px rgba(233,30,99,0.4);
        background: linear-gradient(135deg, #e91e63, #ff4081);
        color: white; white-space: nowrap;
        transition: transform 0.15s, box-shadow 0.15s, font-size 0.25s;
    }
    #yes-btn:hover {
        transform: scale(1.14);
        box-shadow: 0 10px 32px rgba(233,30,99,0.6);
        font-size: 1.62rem;
    }
    #no-btn { position: fixed; }

    #btn-row {
        display: flex; gap: 32px;
        align-items: center; justify-content: center;
    }
    </style>

    <div id="proposal-overlay">
        <div class="question-text">💍 Will You Be My Wife? 💍</div>
        <div class="hearts">💖 💕 💗 💓 💞</div>
        <div id="btn-row">
            <button class="proposal-btn" id="yes-btn" onclick="yesClicked()">Yes! 🥰</button>
            <button class="proposal-btn" id="no-btn"
                    onmouseenter="runAway()"
                    ontouchstart="runAway()">No 😔</button>
        </div>
    </div>

    <script>
    const noTexts = [
        "No 😔","Are you sure? 🤔","Think again! 😅",
        "Please? 🥺","Noooo! 😭","Come on! 💕",
        "Last chance! 😬","Really?? 😢","Don't! 🙈","I'll cry... 😢"
    ];
    let noIdx = 0;
    let noPlaced = false;
    const noBtn = document.getElementById('no-btn');

    function runAway() {
        if (!noPlaced) {
            const r = noBtn.getBoundingClientRect();
            noBtn.style.left = r.left + 'px';
            noBtn.style.top  = r.top  + 'px';
            noPlaced = true;
        }
        const margin = 90;
        const maxX = window.innerWidth  - noBtn.offsetWidth  - margin;
        const maxY = window.innerHeight - noBtn.offsetHeight - margin;
        noBtn.style.left   = (margin + Math.random() * Math.max(0, maxX - margin)) + 'px';
        noBtn.style.top    = (margin + Math.random() * Math.max(0, maxY - margin)) + 'px';
        noBtn.style.right  = 'auto';
        noBtn.style.bottom = 'auto';
        noIdx = (noIdx + 1) % noTexts.length;
        noBtn.innerText = noTexts[noIdx];
    }

    function yesClicked() {
        const allBtns = window.parent.document.querySelectorAll('button');
        for (let b of allBtns) {
            if (b.innerText.trim() === '__YES__') { b.click(); return; }
        }
        const localBtns = document.querySelectorAll('button');
        for (let b of localBtns) {
            if (b.innerText.trim() === '__YES__') { b.click(); return; }
        }
    }
    </script>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 2 – She Said Yes!
# ══════════════════════════════════════════════════════════════════════════════
else:
    docx_path  = os.path.join(os.path.dirname(__file__), "love_letter.docx")
    photo_path = os.path.join(os.path.dirname(__file__), "photo.jpg")

    docx_b64  = file_to_b64(docx_path)  if os.path.exists(docx_path)  else None
    photo_b64 = file_to_b64(photo_path) if os.path.exists(photo_path) else None

    photo_html = (
        f'<img src="data:image/jpeg;base64,{photo_b64}" class="couple-photo" alt="Our photo"/>'
        if photo_b64 else
        '<div class="photo-placeholder">📸<br><small>Add photo.jpg next to app.py and restart</small></div>'
    )
    docx_link = (
        f'<a class="download-btn" href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{docx_b64}" download="love_letter.docx">💌 Download Our Love Letter</a>'
        if docx_b64 else ""
    )

    st.markdown(f"""
    <style>
    #MainMenu, footer, header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {{ display: none !important; }}
    html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"] {{
        background-color: #FFF0F5 !important; font-family: 'Georgia', serif;
    }}
    .block-container {{ padding-top: 1rem !important; }}
    #confetti-canvas {{ position: fixed; inset: 0; width:100%; height:100%; pointer-events:none; z-index:9999; }}
    .yes-card {{
        background: rgba(255,255,255,0.85); backdrop-filter: blur(8px);
        border-radius: 28px; padding: 2.5rem 2rem; max-width: 560px;
        margin: 2rem auto; text-align: center;
        box-shadow: 0 12px 40px rgba(233,30,99,0.18); border: 2px solid #f48fb1;
    }}
    .yes-title {{ font-size: 2.6rem; color: #880E4F; font-weight: bold; margin-bottom: 0.3rem; }}
    .yes-sub   {{ font-size: 1.1rem; color: #c2185b; margin-bottom: 1.8rem; }}
    .couple-photo {{
        width:100%; max-width:420px; border-radius:20px;
        border:4px solid #f48fb1; box-shadow:0 8px 24px rgba(233,30,99,0.25);
        margin:0 auto 1.6rem auto; display:block;
    }}
    .photo-placeholder {{
        width:100%; max-width:420px; height:260px; border-radius:20px;
        border:4px dashed #f48fb1; background:#fce4ec;
        display:flex; flex-direction:column; align-items:center; justify-content:center;
        font-size:3rem; color:#c2185b; margin:0 auto 1.6rem auto;
    }}
    .photo-placeholder small {{ font-size:0.8rem; color:#880E4F; margin-top:0.5rem; }}
    .download-btn {{
        display:inline-block; background:linear-gradient(135deg,#e91e63,#ff4081);
        color:white !important; text-decoration:none; padding:14px 36px;
        border-radius:50px; font-size:1.1rem; font-weight:bold;
        box-shadow:0 6px 20px rgba(233,30,99,0.35);
        transition:transform 0.15s,box-shadow 0.15s; margin-top:0.5rem;
    }}
    .download-btn:hover {{ transform:scale(1.05); box-shadow:0 10px 28px rgba(233,30,99,0.5); }}
    </style>

    <canvas id="confetti-canvas"></canvas>
    <div class="yes-card">
        <div class="yes-title">She Said YES! 💍</div>
        <div class="yes-sub">This is just the beginning of forever 🌹</div>
        {photo_html}
        {docx_link}
    </div>

    <script>
    (function(){{
        const canvas=document.getElementById('confetti-canvas');
        const ctx=canvas.getContext('2d');
        function resize(){{canvas.width=window.innerWidth;canvas.height=window.innerHeight;}}
        resize(); window.addEventListener('resize',resize);
        const COLORS=['#ff4081','#f06292','#e91e63','#ff80ab','#fff176','#ce93d8','#ffffff','#ffb6c1'];
        class Flake{{
            constructor(){{this.reset(true);}}
            reset(init){{
                this.x=Math.random()*canvas.width;
                this.y=init?Math.random()*-canvas.height:-20;
                this.size=6+Math.random()*10; this.speed=1.5+Math.random()*3.5;
                this.drift=(Math.random()-0.5)*1.2; this.rot=Math.random()*Math.PI*2;
                this.rotV=(Math.random()-0.5)*0.08;
                this.color=COLORS[Math.floor(Math.random()*COLORS.length)];
                this.shape=['circle','rect','heart'][Math.floor(Math.random()*3)];
                this.alpha=0.75+Math.random()*0.25;
            }}
            draw(){{
                ctx.save(); ctx.globalAlpha=this.alpha; ctx.fillStyle=this.color;
                ctx.translate(this.x,this.y); ctx.rotate(this.rot);
                if(this.shape==='circle'){{ctx.beginPath();ctx.arc(0,0,this.size/2,0,Math.PI*2);ctx.fill();}}
                else if(this.shape==='rect'){{ctx.fillRect(-this.size/2,-this.size/4,this.size,this.size/2);}}
                else{{
                    const s=this.size*0.35; ctx.beginPath(); ctx.moveTo(0,s);
                    ctx.bezierCurveTo(s*2,-s,s*3.5,s*1.5,0,s*3);
                    ctx.bezierCurveTo(-s*3.5,s*1.5,-s*2,-s,0,s); ctx.fill();
                }}
                ctx.restore();
            }}
            update(){{
                this.y+=this.speed; this.x+=this.drift; this.rot+=this.rotV;
                if(this.y>canvas.height+20)this.reset(false);
            }}
        }}
        const flakes=Array.from({{length:200}},()=>new Flake());
        function loop(){{ctx.clearRect(0,0,canvas.width,canvas.height);flakes.forEach(f=>{{f.update();f.draw();}});requestAnimationFrame(loop);}}
        loop();
    }})();
    </script>
    """, unsafe_allow_html=True)
