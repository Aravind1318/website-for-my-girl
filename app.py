import streamlit as st
import base64
import os
import random

st.set_page_config(page_title="💍 A Special Question", page_icon="💍", layout="wide")

if "accepted" not in st.session_state:
    st.session_state.accepted = False

def file_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 1 – The Question
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.accepted:

    trigger = st.button("__YES_TRIGGER__", key="yes_trigger")
    if trigger:
        st.session_state.accepted = True
        st.rerun()

    st.markdown(r"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400&display=swap');

    /* ── Reset everything ── */
    #MainMenu, footer, header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    .stDeployButton,
    [data-testid="stMainBlockContainer"] > div:first-child { display: none !important; }

    html, body,
    [data-testid="stApp"],
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .block-container {
        background: transparent !important;
        padding: 0 !important; margin: 0 !important;
        max-width: 100% !important; width: 100% !important;
    }

    /* ── Full screen canvas ── */
    #bg-canvas {
        position: fixed; inset: 0; z-index: 0;
        pointer-events: none;
    }

    /* ── Overlay ── */
    #proposal-overlay {
        position: fixed; inset: 0; z-index: 10;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        font-family: 'Playfair Display', serif;
        overflow: hidden;
    }

    /* ── Floating petals bg ── */
    .petal {
        position: fixed; pointer-events: none; z-index: 1;
        font-size: 1.4rem; opacity: 0;
        animation: floatPetal linear infinite;
    }
    @keyframes floatPetal {
        0%   { transform: translateY(-60px) rotate(0deg);   opacity: 0; }
        10%  { opacity: 0.7; }
        90%  { opacity: 0.5; }
        100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
    }

    /* ── Card ── */
    #card {
        position: relative; z-index: 20;
        background: rgba(255,255,255,0.18);
        backdrop-filter: blur(18px);
        border: 1.5px solid rgba(255,255,255,0.55);
        border-radius: 32px;
        padding: 3.5rem 4rem;
        max-width: 620px; width: 90vw;
        text-align: center;
        box-shadow:
            0 8px 48px rgba(199, 21, 90, 0.22),
            0 2px 0 rgba(255,255,255,0.6) inset;
        animation: cardIn 0.9s cubic-bezier(0.34,1.56,0.64,1) both;
    }
    @keyframes cardIn {
        from { opacity: 0; transform: scale(0.75) translateY(40px); }
        to   { opacity: 1; transform: scale(1)    translateY(0); }
    }

    /* ── Ring icon ── */
    #ring-icon {
        font-size: 4rem; margin-bottom: 0.5rem;
        animation: ringPulse 2s ease-in-out infinite;
        display: block;
    }
    @keyframes ringPulse {
        0%,100% { transform: scale(1) rotate(-5deg); }
        50%      { transform: scale(1.15) rotate(5deg); }
    }

    /* ── Heading ── */
    #question-heading {
        font-family: 'Playfair Display', serif;
        font-size: clamp(2rem, 5vw, 2.9rem);
        font-weight: 700;
        color: #6d0030;
        line-height: 1.25;
        margin: 0.4rem 0 0.2rem 0;
        text-shadow: 0 2px 12px rgba(199,21,90,0.18);
        animation: fadeSlideUp 0.7s 0.3s ease both;
    }
    #question-sub {
        font-family: 'Lato', sans-serif;
        font-size: 1rem; font-weight: 300;
        color: #c2185b; letter-spacing: 0.12em;
        margin-bottom: 2.6rem;
        animation: fadeSlideUp 0.7s 0.5s ease both;
    }
    @keyframes fadeSlideUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ── Divider ── */
    .divider {
        width: 60px; height: 2px;
        background: linear-gradient(90deg, transparent, #e91e63, transparent);
        margin: 0 auto 2rem auto;
        animation: fadeSlideUp 0.7s 0.6s ease both;
    }

    /* ── Button row ── */
    #btn-row {
        display: flex; gap: 24px;
        align-items: center; justify-content: center;
        animation: fadeSlideUp 0.7s 0.7s ease both;
    }

    /* ── YES button ── */
    #yes-btn {
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem; font-weight: 700;
        padding: 16px 52px;
        background: linear-gradient(135deg, #e91e63 0%, #ff80ab 100%);
        color: white; border: none; border-radius: 50px;
        cursor: pointer; letter-spacing: 0.04em;
        box-shadow:
            0 6px 24px rgba(233,30,99,0.4),
            0 1px 0 rgba(255,255,255,0.3) inset;
        transition: transform 0.18s cubic-bezier(0.34,1.56,0.64,1),
                    box-shadow 0.18s ease,
                    font-size 0.3s ease;
        position: relative; overflow: hidden;
    }
    #yes-btn::after {
        content: '';
        position: absolute; inset: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.25), transparent);
        border-radius: inherit;
    }
    #yes-btn:hover {
        transform: scale(1.13) translateY(-2px);
        box-shadow: 0 14px 36px rgba(233,30,99,0.55), 0 1px 0 rgba(255,255,255,0.3) inset;
        font-size: 1.38rem;
    }
    #yes-btn:active { transform: scale(0.97); }

    /* ── NO button ── */
    #no-btn {
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem; font-weight: 400;
        padding: 16px 52px;
        background: rgba(255,255,255,0.35);
        color: #880e4f; border: 1.5px solid rgba(233,30,99,0.35);
        border-radius: 50px; cursor: pointer;
        letter-spacing: 0.04em;
        backdrop-filter: blur(6px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        transition: background 0.2s, color 0.2s;
        position: fixed; /* roam the screen */
        white-space: nowrap;
    }
    #no-btn:hover { background: rgba(255,200,210,0.5); }

    /* ── Heartbeat on card when Yes hovered ── */
    #card.heartbeat {
        animation: cardPulse 0.4s ease;
    }
    @keyframes cardPulse {
        0%   { box-shadow: 0 8px 48px rgba(199,21,90,0.22); }
        50%  { box-shadow: 0 8px 72px rgba(233,30,99,0.55); }
        100% { box-shadow: 0 8px 48px rgba(199,21,90,0.22); }
    }
    </style>

    <!-- Gradient mesh background -->
    <canvas id="bg-canvas"></canvas>

    <!-- Floating petals -->
    <div id="petals-container"></div>

    <!-- Main card -->
    <div id="proposal-overlay">
        <div id="card">
            <span id="ring-icon">💍</span>
            <h1 id="question-heading">Will You Be My Wife?</h1>
            <p id="question-sub">a question from my heart to yours</p>
            <div class="divider"></div>
            <div id="btn-row">
                <button id="yes-btn" onclick="yesClicked()" onmouseenter="yesHover()">Yes 🥰</button>
                <button id="no-btn"  onmouseenter="noFlee()" ontouchstart="noFlee()">No 😔</button>
            </div>
        </div>
    </div>

    <script>
    /* ── Animated gradient mesh background ── */
    (function() {
        const canvas = document.getElementById('bg-canvas');
        const ctx    = canvas.getContext('2d');
        let t = 0;
        function resize() { canvas.width = innerWidth; canvas.height = innerHeight; }
        resize(); window.addEventListener('resize', resize);

        function draw() {
            const w = canvas.width, h = canvas.height;
            // Animated base gradient
            const g = ctx.createRadialGradient(
                w * (0.3 + 0.15 * Math.sin(t * 0.4)),
                h * (0.3 + 0.12 * Math.cos(t * 0.3)),
                0,
                w * 0.5, h * 0.5, Math.max(w, h) * 0.9
            );
            g.addColorStop(0,   `hsl(${340 + 12*Math.sin(t*0.5)}, 100%, 85%)`);
            g.addColorStop(0.4, `hsl(${350 + 8 *Math.cos(t*0.4)}, 90%,  78%)`);
            g.addColorStop(0.75,`hsl(${330 + 10*Math.sin(t*0.6)}, 80%,  75%)`);
            g.addColorStop(1,   `hsl(${320},                       70%,  70%)`);
            ctx.fillStyle = g;
            ctx.fillRect(0, 0, w, h);

            // Soft blobs
            [[0.15,0.2,'rgba(255,105,135,0.22)',220],
             [0.8, 0.15,'rgba(255,160,180,0.18)',180],
             [0.6, 0.75,'rgba(250,80,120,0.16)',260],
             [0.1, 0.8, 'rgba(255,180,200,0.2)',200]].forEach(([fx,fy,c,r]) => {
                const bx = w * fx + 60 * Math.sin(t * 0.35 + fx * 10);
                const by = h * fy + 50 * Math.cos(t * 0.28 + fy * 8);
                const bg = ctx.createRadialGradient(bx,by,0,bx,by,r);
                bg.addColorStop(0, c); bg.addColorStop(1, 'transparent');
                ctx.fillStyle = bg; ctx.fillRect(0,0,w,h);
            });

            t += 0.012;
            requestAnimationFrame(draw);
        }
        draw();
    })();

    /* ── Floating petals ── */
    const PETALS = ['🌸','🌷','💕','✨','🌹','💗','🫧'];
    const cont = document.getElementById('petals-container');
    for (let i = 0; i < 22; i++) {
        const p = document.createElement('div');
        p.className = 'petal';
        p.innerText = PETALS[i % PETALS.length];
        p.style.left = (Math.random() * 100) + 'vw';
        p.style.fontSize = (0.9 + Math.random() * 1.4) + 'rem';
        const dur = 7 + Math.random() * 10;
        p.style.animationDuration  = dur + 's';
        p.style.animationDelay     = -(Math.random() * dur) + 's';
        cont.appendChild(p);
    }

    /* ── NO button flee logic ── */
    const noTexts = [
        "No 😔","Are you sure? 🤔","Think again! 😅",
        "Please? 🥺","Noooo! 😭","Come on! 💕",
        "Last chance! 😬","Really?? 😢","I'll cry 😢",
        "Don't! 🙈","My heart... 💔"
    ];
    let noIdx = 0, noPlaced = false;
    const noBtn = document.getElementById('no-btn');

    function noFlee() {
        if (!noPlaced) {
            const r = noBtn.getBoundingClientRect();
            noBtn.style.left = r.left + 'px';
            noBtn.style.top  = r.top  + 'px';
            noPlaced = true;
        }
        const m = 80;
        const maxX = innerWidth  - noBtn.offsetWidth  - m;
        const maxY = innerHeight - noBtn.offsetHeight - m;
        noBtn.style.left   = (m + Math.random() * Math.max(0, maxX - m)) + 'px';
        noBtn.style.top    = (m + Math.random() * Math.max(0, maxY - m)) + 'px';
        noBtn.style.right  = 'auto';
        noBtn.style.bottom = 'auto';
        noBtn.style.transition = 'left 0.22s cubic-bezier(0.34,1.56,0.64,1), top 0.22s cubic-bezier(0.34,1.56,0.64,1)';
        noIdx = (noIdx + 1) % noTexts.length;
        noBtn.innerText = noTexts[noIdx];
    }

    /* ── YES hover – card heartbeat + grow ── */
    let yesScale = 1;
    function yesHover() {
        yesScale = Math.min(yesScale + 0.06, 1.5);
        const yesBtn = document.getElementById('yes-btn');
        yesBtn.style.fontSize = (1.25 * yesScale) + 'rem';
        yesBtn.style.padding  = `${16}px ${Math.round(52 * Math.min(yesScale,1.25))}px`;
        const card = document.getElementById('card');
        card.classList.remove('heartbeat');
        void card.offsetWidth;
        card.classList.add('heartbeat');
    }

    /* ── YES click → trigger Streamlit ── */
    function yesClicked() {
        // Burst of hearts on click
        for (let i = 0; i < 14; i++) {
            const h = document.createElement('div');
            h.innerText = ['💖','💗','💕','💓'][i % 4];
            h.style.cssText = `
                position:fixed; z-index:9999; pointer-events:none;
                left:${40+Math.random()*20}%; top:40%;
                font-size:${1.5+Math.random()*1.5}rem;
                animation: burstHeart 1.1s ease forwards;
                --dx:${(Math.random()-0.5)*300}px;
                --dy:${-(80+Math.random()*200)}px;
            `;
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 1200);
        }

        // Trigger Streamlit
        setTimeout(() => {
            const allBtns = window.parent.document.querySelectorAll('button');
            for (let b of allBtns) {
                if (b.innerText.trim() === '__YES_TRIGGER__') { b.click(); return; }
            }
            const localBtns = document.querySelectorAll('button');
            for (let b of localBtns) {
                if (b.innerText.trim() === '__YES_TRIGGER__') { b.click(); return; }
            }
        }, 500);
    }
    </script>
    <style>
    @keyframes burstHeart {
        0%   { opacity:1; transform: translate(0,0) scale(1); }
        100% { opacity:0; transform: translate(var(--dx), var(--dy)) scale(0.3); }
    }
    </style>
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
        '<div class="photo-placeholder">📸<br><small>Add <code>photo.jpg</code> next to app.py and restart</small></div>'
    )
    docx_link = (
        f'<a class="dl-btn" href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{docx_b64}" download="love_letter.docx">💌 Download Our Love Letter</a>'
        if docx_b64 else ""
    )

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400&display=swap');

    #MainMenu, footer, header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {{ display: none !important; }}

    html, body, [data-testid="stApp"],
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .block-container {{
        background: transparent !important;
        padding: 0 !important; margin: 0 !important;
        max-width: 100% !important;
    }}

    #yes2-bg {{
        position: fixed; inset: 0; z-index: 0;
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4ef 50%, #fff8fb 100%);
    }}

    #confetti-canvas {{
        position: fixed; inset: 0; z-index: 9999;
        pointer-events: none; width: 100%; height: 100%;
    }}

    .yes-page {{
        position: relative; z-index: 10;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        min-height: 100vh; padding: 3rem 1rem;
        font-family: 'Playfair Display', serif;
    }}

    .yes-badge {{
        font-size: 3.5rem;
        animation: badgePop 0.8s cubic-bezier(0.34,1.56,0.64,1) both;
        margin-bottom: 0.5rem;
    }}
    @keyframes badgePop {{
        from {{ opacity:0; transform:scale(0.3) rotate(-20deg); }}
        to   {{ opacity:1; transform:scale(1)   rotate(0deg); }}
    }}

    .yes-title {{
        font-size: clamp(2.2rem, 6vw, 3.4rem);
        font-weight: 700; color: #880e4f;
        margin: 0 0 0.3rem 0;
        animation: fadeUp 0.8s 0.2s ease both;
        text-shadow: 0 2px 16px rgba(199,21,90,0.15);
    }}
    .yes-sub {{
        font-family: 'Lato', sans-serif;
        font-size: 1rem; font-weight: 300;
        color: #c2185b; letter-spacing: 0.14em;
        margin-bottom: 2.5rem;
        animation: fadeUp 0.8s 0.4s ease both;
    }}
    @keyframes fadeUp {{
        from {{ opacity:0; transform:translateY(18px); }}
        to   {{ opacity:1; transform:translateY(0); }}
    }}

    .photo-frame {{
        position: relative;
        border-radius: 24px;
        padding: 10px;
        background: white;
        box-shadow:
            0 20px 60px rgba(199,21,90,0.2),
            0 2px 0 rgba(255,255,255,0.9) inset;
        max-width: 440px; width: 88vw;
        animation: fadeUp 0.9s 0.5s ease both;
        margin-bottom: 2rem;
    }}
    .couple-photo {{
        width: 100%; border-radius: 16px;
        display: block;
    }}
    .photo-placeholder {{
        width: 100%; height: 280px; border-radius: 16px;
        background: #fce4ec;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        font-size: 3rem; color: #c2185b;
    }}
    .photo-placeholder small {{ font-size: 0.8rem; margin-top: 0.5rem; font-family:'Lato',sans-serif; }}

    /* Polaroid corner decorations */
    .photo-frame::before, .photo-frame::after {{
        content: '✨'; position: absolute;
        font-size: 1.4rem;
    }}
    .photo-frame::before {{ top: -10px; left: -10px; }}
    .photo-frame::after  {{ bottom: -10px; right: -10px; }}

    .dl-btn {{
        font-family: 'Playfair Display', serif;
        font-size: 1.15rem; font-weight: 700;
        display: inline-flex; align-items: center; gap: 8px;
        padding: 16px 48px;
        background: linear-gradient(135deg, #e91e63 0%, #ff80ab 100%);
        color: white !important; text-decoration: none;
        border-radius: 50px;
        box-shadow: 0 8px 28px rgba(233,30,99,0.4);
        transition: transform 0.2s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.2s;
        animation: fadeUp 0.9s 0.7s ease both;
    }}
    .dl-btn:hover {{
        transform: scale(1.07) translateY(-3px);
        box-shadow: 0 16px 40px rgba(233,30,99,0.5);
    }}
    </style>

    <div id="yes2-bg"></div>
    <canvas id="confetti-canvas"></canvas>

    <div class="yes-page">
        <div class="yes-badge">💍</div>
        <h1 class="yes-title">She Said YES!</h1>
        <p class="yes-sub">and now forever begins ✨</p>
        <div class="photo-frame">{photo_html}</div>
        {docx_link}
    </div>

    <script>
    /* ── Confetti ── */
    (function(){{
        const canvas = document.getElementById('confetti-canvas');
        const ctx    = canvas.getContext('2d');
        function resize(){{ canvas.width=innerWidth; canvas.height=innerHeight; }}
        resize(); window.addEventListener('resize',resize);

        const COLORS=['#ff4081','#f06292','#e91e63','#ff80ab','#fff176','#ce93d8','#ffffff','#ffb6c1','#f8bbd0'];
        class Flake{{
            constructor(){{ this.reset(true); }}
            reset(init){{
                this.x=Math.random()*canvas.width;
                this.y=init?Math.random()*-canvas.height:-30;
                this.size=5+Math.random()*11; this.speed=1.8+Math.random()*3.8;
                this.drift=(Math.random()-0.5)*1.5; this.rot=Math.random()*Math.PI*2;
                this.rotV=(Math.random()-0.5)*0.09;
                this.color=COLORS[Math.floor(Math.random()*COLORS.length)];
                this.shape=['circle','rect','heart','star'][Math.floor(Math.random()*4)];
                this.alpha=0.7+Math.random()*0.3;
            }}
            draw(){{
                ctx.save(); ctx.globalAlpha=this.alpha; ctx.fillStyle=this.color;
                ctx.translate(this.x,this.y); ctx.rotate(this.rot);
                if(this.shape==='circle'){{
                    ctx.beginPath(); ctx.arc(0,0,this.size/2,0,Math.PI*2); ctx.fill();
                }} else if(this.shape==='rect'){{
                    ctx.fillRect(-this.size/2,-this.size/3,this.size,this.size/1.5);
                }} else if(this.shape==='heart'){{
                    const s=this.size*0.32; ctx.beginPath(); ctx.moveTo(0,s);
                    ctx.bezierCurveTo(s*2,-s,s*3.5,s*1.5,0,s*3);
                    ctx.bezierCurveTo(-s*3.5,s*1.5,-s*2,-s,0,s); ctx.fill();
                }} else {{
                    // star
                    ctx.beginPath();
                    for(let i=0;i<5;i++){{
                        const a=Math.PI/2+i*Math.PI*2/5;
                        const b=a+Math.PI/5;
                        const r=this.size/2, ri=r*0.4;
                        if(i===0) ctx.moveTo(Math.cos(a)*r,Math.sin(a)*r);
                        else ctx.lineTo(Math.cos(a)*r,Math.sin(a)*r);
                        ctx.lineTo(Math.cos(b)*ri,Math.sin(b)*ri);
                    }}
                    ctx.closePath(); ctx.fill();
                }}
                ctx.restore();
            }}
            update(){{
                this.y+=this.speed; this.x+=this.drift; this.rot+=this.rotV;
                if(this.y>canvas.height+30) this.reset(false);
            }}
        }}
        const flakes=Array.from({{length:220}},()=>new Flake());
        function loop(){{
            ctx.clearRect(0,0,canvas.width,canvas.height);
            flakes.forEach(f=>{{f.update();f.draw();}});
            requestAnimationFrame(loop);
        }}
        loop();
    }})();
    </script>
    """, unsafe_allow_html=True)
