from flask import Flask, render_template_string

app = Flask(__name__)

PORTFOLIO = {
    "name": "Benson Varghese",
    "role": "Data Professional",
    "sub_tagline": "Data Professional | Delivering Data-Driven Insights | Visualisation and making ML Models",
    "location": "Dubai",
    "email": "benson.varghese16@gmail.com",
    "available": True,
    "stats": [
        {"num": "4+",  "label": "Years"},
        {"num": "5", "label": "Projects"},
        {"num": "4",  "label": "Companies Worked"},
        #{"num": "#", "label": "Coffee-powered"},
    ],
    "skills": [
        {"name": "R",        "color": "#61DAFB"},
        {"name": "MyExcel",   "color": "#3178C6"},
        {"name": "Python",       "color": "#FFD43B"},
        {"name": "ML Models",      "color": "#68A063"},
        {"name": "PostgreSQL",   "color": "#336791"},
        {"name": "SQL",          "color": "#FF9900"},
        {"name": "NoSQL",       "color": "#2496ED"},
        {"name": "MySQL",      "color": "#E10098"},
        {"name": "Tableau",        "color": "#F24E1E"},
        {"name": "Power BI","color": "#A855F7"},
    ],
    "projects": [
        {
            "num": "01", "name": "FinFlow", "sub": "Analytics Dashboard",
            "desc": "Real-time financial analytics platform for 50k+ users. Built with React + D3.js.",
            "tags": ["React", "D3.js", "FastAPI"], "color": "#00F5FF", 
        },
        {
            "num": "02", "name": "Hive", "sub": "Design System",
            "desc": "80+ components adopted across 3 product teams. Fully documented in Storybook.",
            "tags": ["TypeScript", "Storybook", "Figma"], "color": "#FFD700", 
        },
        {
            "num": "03", "name": "Orbit", "sub": "API Gateway",
            "desc": "High-throughput gateway handling 2M+ req/day. Custom rate limiting & auth.",
            "tags": ["Node.js", "Redis", "AWS"], "color": "#FF6B9D", 
        },
        {
            "num": "04", "name": "Atlas", "sub": "Workspace Platform",
            "desc": "Real-time collab platform — 8k users in 6 months. Acquired by a Series B startup.",
            "tags": ["Next.js", "WebSockets", "PostgreSQL"], "color": "#7CFF6B", 
        },
    ],
    "experience": [
        {"date": "2022–Now",  "role": "Senior SWE",       "company": "Stripe",   "emoji": "💳"},
        {"date": "2020–2022", "role": "Software Engineer", "company": "Grab",     "emoji": "🚗"},
        {"date": "2019–2020", "role": "Frontend Engineer", "company": "Shopback", "emoji": "🛒"},
        {"date": "2018–2019", "role": "B.Eng CS",          "company": "NUS",      "emoji": "🎓"},
    ],
    "socials": [
        {"label": "GitHub",   "url": "#"},
        {"label": "LinkedIn", "url": "www.linkedin.com/in/benson-varghese-ab4512106"},
        {"label": "Twitter",  "url": "#"},
    ],
}

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ p.name }} — Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#07070f;--c1:#00F5FF;--c2:#FF6B9D;--c3:#FFD700;--c4:#7CFF6B;
  --text:#f5f5f0;--muted:#888;--surface:#0f0f1a;--border:rgba(255,255,255,0.08);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Space Mono',monospace;overflow-x:hidden}
#bg-canvas{position:fixed;inset:0;z-index:0;pointer-events:none}
.cur{position:fixed;width:10px;height:10px;background:#fff;border-radius:50%;
  transform:translate(-50%,-50%);pointer-events:none;z-index:9999;transition:transform .1s;mix-blend-mode:difference}
.cur-ring{position:fixed;width:44px;height:44px;border:1.5px solid rgba(255,255,255,.4);border-radius:50%;
  transform:translate(-50%,-50%);transition:all .22s ease;pointer-events:none;z-index:9998}
body{cursor:none}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:500;display:flex;align-items:center;
  justify-content:space-between;padding:1.2rem 2.5rem;
  background:rgba(7,7,15,.85);backdrop-filter:blur(24px);border-bottom:1px solid var(--border)}
.nav-logo{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:1.3rem;
  background:linear-gradient(90deg,var(--c1),var(--c2),var(--c3));background-size:200%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:gradMove 4s linear infinite}
@keyframes gradMove{0%{background-position:0%}100%{background-position:200%}}
.nav-links{display:flex;gap:2rem;list-style:none}
.nav-links a{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  text-decoration:none;transition:color .2s;position:relative}
.nav-links a::after{content:'';position:absolute;left:0;bottom:-2px;width:0;height:1px;
  background:var(--c1);transition:width .2s}
.nav-links a:hover{color:var(--text)}.nav-links a:hover::after{width:100%}
.nav-btn{font-family:'Bricolage Grotesque',sans-serif;font-size:.78rem;font-weight:700;
  padding:.6rem 1.6rem;border:none;border-radius:100px;cursor:none;
  background:linear-gradient(90deg,var(--c1),var(--c2));color:#07070f;
  transition:transform .2s,box-shadow .2s;box-shadow:0 0 20px rgba(0,245,255,.2)}
.nav-btn:hover{transform:translateY(-2px);box-shadow:0 0 35px rgba(0,245,255,.45)}

/* HERO */
.hero{min-height:100vh;display:flex;flex-direction:column;justify-content:center;
  padding:8rem 2.5rem 4rem;position:relative;z-index:1}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;font-size:.7rem;letter-spacing:.12em;
  text-transform:uppercase;padding:.4rem 1rem;border-radius:100px;
  border:1px solid rgba(0,245,255,.3);color:var(--c1);background:rgba(0,245,255,.05);
  margin-bottom:2rem;animation:fadeUp .7s .1s both}
.badge-dot{width:7px;height:7px;border-radius:50%;background:var(--c4);animation:pulse 1.5s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(1.4)}}
.hero-greeting{font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);
  margin-bottom:.4rem;animation:fadeUp .7s .2s both}
.hero-name{font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(3.5rem,9vw,8rem);
  font-weight:800;line-height:.95;letter-spacing:-.02em;animation:fadeUp .7s .3s both}
.hero-name .ital{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;
  font-size:clamp(3rem,8vw,7rem);
  background:linear-gradient(90deg,var(--c1),var(--c2),var(--c3),var(--c4));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  background-size:300%;animation:gradMove 5s linear infinite}
.hero-role{font-size:clamp(.9rem,2vw,1.3rem);color:var(--muted);margin-top:1.5rem;
  animation:fadeUp .7s .4s both;max-width:560px}
.hero-role strong{color:var(--text);font-weight:400}
.hero-actions{display:flex;align-items:center;gap:1.5rem;margin-top:3rem;flex-wrap:wrap;
  animation:fadeUp .7s .5s both}
.btn-p{font-family:'Bricolage Grotesque',sans-serif;font-size:.85rem;font-weight:700;
  padding:.9rem 2.2rem;border-radius:100px;text-decoration:none;
  background:linear-gradient(90deg,var(--c1),var(--c2));color:#07070f;
  box-shadow:0 0 30px rgba(0,245,255,.25);transition:transform .2s,box-shadow .2s;display:inline-block}
.btn-p:hover{transform:translateY(-3px) scale(1.02);box-shadow:0 8px 40px rgba(0,245,255,.45)}
.btn-s{font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  text-decoration:none;display:flex;align-items:center;gap:.5rem;transition:color .2s}
.btn-s:hover{color:var(--text)}.btn-s svg{transition:transform .2s}.btn-s:hover svg{transform:translateX(4px)}
.hero-stats{display:flex;gap:3rem;margin-top:5rem;padding-top:2.5rem;
  border-top:1px solid var(--border);flex-wrap:wrap;animation:fadeUp .7s .6s both}
.stn{font-family:'Bricolage Grotesque',sans-serif;font-size:2.2rem;font-weight:800;line-height:1;
  background:linear-gradient(135deg,var(--c1),var(--c2));-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text}
.stl{font-size:.65rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-top:.2rem}

/* MARQUEE */
.mq{padding:1.4rem 0;overflow:hidden;border-top:1px solid var(--border);
  border-bottom:1px solid var(--border);background:rgba(0,245,255,.02);position:relative;z-index:1}
.mq-track{display:flex;width:max-content;animation:mq 22s linear infinite}
@keyframes mq{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.mq-item{display:flex;align-items:center;gap:.7rem;padding:0 2.5rem;
  font-family:'Bricolage Grotesque',sans-serif;font-size:.95rem;font-weight:600;
  white-space:nowrap;color:var(--muted)}
.mq-dot{width:6px;height:6px;border-radius:50%;background:var(--c2);flex-shrink:0}

/* SECTIONS */
.sec{padding:7rem 2.5rem;position:relative;z-index:1;border-top:1px solid var(--border)}
.slabel{font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;color:var(--c1);margin-bottom:.6rem}
.stitle{font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(2rem,5vw,3.2rem);
  font-weight:800;line-height:1;letter-spacing:-.02em;margin-bottom:3.5rem}
.stitle em{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;color:var(--c2)}

/* SKILLS */
.sk-grid{display:flex;flex-wrap:wrap;gap:.75rem}
.sk-pill{display:flex;align-items:center;gap:.5rem;font-size:.75rem;font-weight:700;
  letter-spacing:.05em;padding:.5rem 1.1rem;border-radius:100px;
  background:var(--surface);border:1px solid var(--border);transition:all .25s;cursor:none}
.sk-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.sk-pill:hover{transform:translateY(-3px) scale(1.06);
  border-color:var(--sc);box-shadow:0 8px 28px color-mix(in srgb,var(--sc) 30%,transparent)}

/* BENTO */
.bento{display:grid;grid-template-columns:repeat(2,1fr);gap:1.2rem}
.bc{background:var(--surface);border:1px solid var(--border);border-radius:20px;
  padding:2rem;position:relative;overflow:hidden;cursor:none;
  transition:transform .3s,border-color .3s,box-shadow .3s}
.bc::before{content:'';position:absolute;inset:0;border-radius:20px;
  background:radial-gradient(ellipse at top left,color-mix(in srgb,var(--cc) 10%,transparent),transparent 60%);
  opacity:0;transition:opacity .3s}
.bc:hover{transform:translateY(-7px);box-shadow:0 24px 60px rgba(0,0,0,.4)}
.bc:hover::before{opacity:1}
.bc:hover{border-color:color-mix(in srgb,var(--cc) 50%,transparent)}
.ct{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1.5rem}
.cem{font-size:2.5rem;line-height:1}
.cnum{font-family:'Bricolage Grotesque',sans-serif;font-size:.65rem;font-weight:700;
  letter-spacing:.15em;text-transform:uppercase;padding:.3rem .7rem;border-radius:100px;
  color:var(--cc);border:1px solid var(--cc);background:color-mix(in srgb,var(--cc) 10%,transparent)}
.cname{font-family:'Bricolage Grotesque',sans-serif;font-size:1.5rem;font-weight:800;margin-bottom:.2rem}
.csub{font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:1rem}
.cdesc{font-size:.78rem;line-height:1.7;color:var(--muted);margin-bottom:1.5rem}
.ctags{display:flex;flex-wrap:wrap;gap:.4rem}
.ctag{font-size:.6rem;letter-spacing:.08em;text-transform:uppercase;padding:.25rem .65rem;
  border-radius:100px;background:rgba(255,255,255,.05);color:var(--muted);border:1px solid var(--border)}
.carrow{position:absolute;bottom:1.5rem;right:1.5rem;width:36px;height:36px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;border:1px solid var(--border);
  color:var(--muted);transition:all .2s;font-size:1rem}
.bc:hover .carrow{background:var(--cc);border-color:var(--cc);color:#07070f;transform:rotate(-45deg)}

/* EXPERIENCE */
.eg{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}
.ec{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:1.75rem;display:flex;align-items:center;gap:1.25rem;transition:all .25s;cursor:none}
.ec:hover{transform:translateY(-4px);border-color:rgba(0,245,255,.35);
  box-shadow:0 12px 40px rgba(0,245,255,.1)}
.eemoji{font-size:2rem;line-height:1;flex-shrink:0}
.edate{font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;color:var(--c1);margin-bottom:.2rem}
.erole{font-family:'Bricolage Grotesque',sans-serif;font-size:1rem;font-weight:700;margin-bottom:.15rem}
.eco{font-size:.75rem;color:var(--muted)}

/* CONTACT */
.ctc{background:var(--surface);border:1px solid var(--border);border-radius:24px;
  padding:4rem;text-align:center;position:relative;overflow:hidden}
.ctc::before{content:'';position:absolute;inset:0;border-radius:24px;
  background:radial-gradient(ellipse at 50% 0%,rgba(0,245,255,.07),transparent 55%);pointer-events:none}
.ctc-big{font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(2.5rem,7vw,6rem);
  font-weight:800;line-height:1;letter-spacing:-.03em;margin-bottom:1.5rem;
  background:linear-gradient(90deg,var(--c1),var(--c2),var(--c3),var(--c4));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  background-size:300%;animation:gradMove 6s linear infinite}
.ctc-sub{font-size:.85rem;color:var(--muted);line-height:1.8;max-width:480px;
  margin:0 auto 2.5rem}
.ctc-email{font-family:'Instrument Serif',serif;font-style:italic;font-size:1.8rem;
  color:var(--text);text-decoration:none;border-bottom:2px solid rgba(0,245,255,.3);
  padding-bottom:.2rem;transition:border-color .2s,color .2s;display:inline-block;margin-bottom:3rem}
.ctc-email:hover{border-color:var(--c1);color:var(--c1)}
.socs{display:flex;justify-content:center;gap:1rem}
.soc{font-family:'Bricolage Grotesque',sans-serif;font-size:.72rem;font-weight:700;
  letter-spacing:.08em;text-transform:uppercase;text-decoration:none;
  padding:.6rem 1.4rem;border-radius:100px;border:1px solid var(--border);
  color:var(--muted);transition:all .2s}
.soc:hover{border-color:var(--c1);color:var(--c1);background:rgba(0,245,255,.06)}

/* FOOTER */
footer{padding:2rem 2.5rem;border-top:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center;position:relative;z-index:1}
.fl{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:.9rem;
  background:linear-gradient(90deg,var(--c1),var(--c2));-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text}
.fr{font-size:.62rem;letter-spacing:.1em;color:var(--muted)}

@keyframes fadeUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}
.reveal{opacity:0;transform:translateY(32px);
  transition:opacity .65s cubic-bezier(.16,1,.3,1),transform .65s cubic-bezier(.16,1,.3,1)}
.reveal.on{opacity:1;transform:none}
.reveal[data-d="1"]{transition-delay:.1s}.reveal[data-d="2"]{transition-delay:.2s}
.reveal[data-d="3"]{transition-delay:.3s}.reveal[data-d="4"]{transition-delay:.4s}

@media(max-width:768px){
  nav{padding:1rem 1.2rem}.nav-links{display:none}
  .hero{padding:6rem 1.2rem 3rem}
  .sec{padding:4rem 1.2rem}
  .bento,.eg{grid-template-columns:1fr}
  .ctc{padding:2.5rem 1.5rem}
  footer{flex-direction:column;gap:.75rem;text-align:center}
}
</style>
</head>
<body>

<canvas id="bg-canvas"></canvas>
<div class="cur" id="cur"></div>
<div class="cur-ring" id="ring"></div>

<!-- NAV -->
<nav>
  <div class="nav-logo">{{ p.name.split()[0][0] }}{{ p.name.split()[1][0] }}</div>
  <ul class="nav-links">
    <li><a href="#skills">Skills</a></li>
    <li><a href="#projects">Work</a></li>
    <li><a href="#exp">Experience</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <button class="nav-btn">Let's Talk 🚀</button>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-badge">
    <span class="badge-dot"></span>
    {% if p.available %}Available for projects{% else %}Currently busy{% endif %} · {{ p.location }}
  </div>
  <div class="hero-greeting">Hey there  I'm</div>
  <h1 class="hero-name">
    {{ p.name.split()[0] }}<br>
    <span class="ital">{{ p.name.split()[1] }}</span>
  </h1>
  <p class="hero-role"><strong>{{ p.role }}</strong> — {{ p.sub_tagline }}</p>
  <div class="hero-actions">
    <a href="#projects" class="btn-p">See My Work ✨</a>
    <a href="#contact" class="btn-s">
      Get in touch
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M3 8H13M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </a>
  </div>
  <div class="hero-stats">
    {% for s in p.stats %}
    <div>
      <div class="stn">{{ s.num }}</div>
      <div class="stl">{{ s.label }}</div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- MARQUEE -->
<div class="mq">
  <div class="mq-track">
    {% for sk in p.skills %}<div class="mq-item"><span class="mq-dot"></span>{{ sk.name }}</div>{% endfor %}
    {% for sk in p.skills %}<div class="mq-item"><span class="mq-dot"></span>{{ sk.name }}</div>{% endfor %}
    {% for sk in p.skills %}<div class="mq-item"><span class="mq-dot"></span>{{ sk.name }}</div>{% endfor %}
  </div>
</div>

<!-- SKILLS -->
<section class="sec" id="skills">
  <div class="slabel reveal">What I use</div>
  <h2 class="stitle reveal">My <em>Toolkit</em></h2>
  <div class="sk-grid">
    {% for sk in p.skills %}
    <div class="sk-pill reveal" data-d="{{ loop.index % 4 + 1 }}" style="--sc:{{ sk.color }}">
      <span class="sk-dot" style="background:{{ sk.color }}"></span>{{ sk.name }}
    </div>
    {% endfor %}
  </div>
</section>

<!-- PROJECTS -->
<section class="sec" id="projects">
  <div class="slabel reveal">Selected work</div>
  <h2 class="stitle reveal">Things I've <em>Built</em></h2>
  <div class="bento">
    {% for proj in p.projects %}
    <div class="bc reveal" data-d="{{ loop.index }}" style="--cc:{{ proj.color }}">
      <div class="ct">
        <div class="cem">{{ proj.emoji }}</div>
        <div class="cnum">{{ proj.num }}</div>
      </div>
      <div class="cname">{{ proj.name }}</div>
      <div class="csub">{{ proj.sub }}</div>
      <p class="cdesc">{{ proj.desc }}</p>
      <div class="ctags">
        {% for tag in proj.tags %}<span class="ctag">{{ tag }}</span>{% endfor %}
      </div>
      <div class="carrow">→</div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- EXPERIENCE -->
<section class="sec" id="exp">
  <div class="slabel reveal">Where I've been</div>
  <h2 class="stitle reveal">My <em>Journey</em></h2>
  <div class="eg">
    {% for e in p.experience %}
    <div class="ec reveal" data-d="{{ loop.index }}">
      <div class="eemoji">{{ e.emoji }}</div>
      <div>
        <div class="edate">{{ e.date }}</div>
        <div class="erole">{{ e.role }}</div>
        <div class="eco">{{ e.company }}</div>
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- CONTACT -->
<section class="sec" id="contact">
  <div class="ctc reveal">
    <div class="ctc-big">Let's Work<br>Together!</div>
    <p class="ctc-sub">Open to full-time roles, consulting & exciting side projects. Drop me a line — I reply fast ⚡</p>
    <a href="mailto:{{ p.email }}" class="ctc-email">{{ p.email }}</a>
    <div class="socs">
      {% for s in p.socials %}<a href="{{ s.url }}" class="soc">{{ s.label }}</a>{% endfor %}
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="fl">{{ p.name.split()[0][0] }}{{ p.name.split()[1][0] }} ✦</div>
  <div class="fr">© 2026 {{ p.name }}. Built with Python 🐍 + Flask</div>
</footer>

<script>
// ── Canvas background ──────────────────────────────────────────
const canvas=document.getElementById('bg-canvas');
const ctx=canvas.getContext('2d');
let W,H;const COLS=['#00F5FF','#FF6B9D','#FFD700','#7CFF6B'];
const mouse={x:innerWidth/2,y:innerHeight/2};

function resize(){W=canvas.width=innerWidth;H=canvas.height=innerHeight}
resize();addEventListener('resize',resize);
addEventListener('mousemove',e=>{mouse.x=e.clientX;mouse.y=e.clientY});

// Grid
function drawGrid(){
  ctx.strokeStyle='rgba(255,255,255,0.025)';ctx.lineWidth=1;
  for(let x=0;x<W;x+=80){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke()}
  for(let y=0;y<H;y+=80){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
}

// Particles
class P{
  constructor(init=false){this.reset(init)}
  reset(init=false){
    this.x=Math.random()*W;this.y=init?Math.random()*H:H+10;
    this.r=Math.random()*2+.4;this.c=COLS[Math.floor(Math.random()*4)];
    this.vx=(Math.random()-.5)*.3;this.vy=-(Math.random()*.4+.1);
    this.a=Math.random()*.4+.1;this.tw=Math.random()*Math.PI*2;
  }
  tick(){
    this.x+=this.vx;this.y+=this.vy;this.tw+=.03;
    const dx=this.x-mouse.x,dy=this.y-mouse.y,d=Math.hypot(dx,dy);
    if(d<100){this.x+=dx/d*1.5;this.y+=dy/d*1.5}
    if(this.y<-10)this.reset();
  }
  draw(){
    ctx.save();ctx.globalAlpha=this.a*(.7+.3*Math.sin(this.tw));
    ctx.fillStyle=this.c;ctx.shadowColor=this.c;ctx.shadowBlur=10;
    ctx.beginPath();ctx.arc(this.x,this.y,this.r,0,Math.PI*2);ctx.fill();ctx.restore();
  }
}

const pts=[];for(let i=0;i<140;i++)pts.push(new P(true));

// Shooting stars
const stars=[];let nextShoot=0;
function maybeShoot(now){
  if(now<nextShoot)return;
  stars.push({x:Math.random()*W,y:0,vx:(Math.random()-.5)*7,vy:Math.random()*4+2,
    len:Math.random()*120+60,c:COLS[Math.floor(Math.random()*4)],life:1});
  nextShoot=now+Math.random()*3500+1500;
}

function loop(ts=0){
  ctx.clearRect(0,0,W,H);
  drawGrid();
  pts.forEach(p=>{p.tick();p.draw()});
  maybeShoot(ts);
  stars.forEach((s,i)=>{
    s.x+=s.vx;s.y+=s.vy;s.life-=.02;
    if(s.life<=0){stars.splice(i,1);return}
    const g=ctx.createLinearGradient(s.x-s.vx*(s.len/6),s.y-s.vy*(s.len/6),s.x,s.y);
    g.addColorStop(0,'transparent');
    g.addColorStop(1,s.c+(Math.max(0,Math.round(s.life*220)).toString(16).padStart(2,'0')));
    ctx.strokeStyle=g;ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(s.x-s.vx*(s.len/6),s.y-s.vy*(s.len/6));ctx.lineTo(s.x,s.y);ctx.stroke();
  });
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);

// ── Cursor ─────────────────────────────────────────────────────
const cur=document.getElementById('cur'),ring=document.getElementById('ring');
let cx=0,cy=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{cx=e.clientX;cy=e.clientY;
  cur.style.left=cx+'px';cur.style.top=cy+'px'});
(function animCur(){
  rx+=(cx-rx)*.1;ry+=(cy-ry)*.1;
  ring.style.left=rx+'px';ring.style.top=ry+'px';
  requestAnimationFrame(animCur);
})();
document.querySelectorAll('a,button,.bc,.sk-pill,.ec').forEach(el=>{
  el.addEventListener('mouseenter',()=>{
    ring.style.transform='translate(-50%,-50%) scale(1.9)';
    ring.style.borderColor='rgba(0,245,255,.6)';
    cur.style.transform='translate(-50%,-50%) scale(0)';
  });
  el.addEventListener('mouseleave',()=>{
    ring.style.transform='translate(-50%,-50%) scale(1)';
    ring.style.borderColor='rgba(255,255,255,.4)';
    cur.style.transform='translate(-50%,-50%) scale(1)';
  });
});

// ── Scroll reveal ──────────────────────────────────────────────
new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('on')});
},{threshold:.1}).observe.bind(
  new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('on')});
  },{threshold:.1})
);
const io=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('on')});
},{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

// ── Count-up ───────────────────────────────────────────────────
document.querySelectorAll('.stn').forEach(el=>{
  const raw=el.textContent.trim();
  const num=parseFloat(raw);if(isNaN(num))return;
  const sfx=raw.replace(/[\d.]/g,'');
  let st=null;
  const step=ts=>{
    if(!st)st=ts;
    const p=Math.min((ts-st)/1400,1),e=1-Math.pow(1-p,3);
    el.textContent=(num<10?(e*num).toFixed(1):Math.floor(e*num))+sfx;
    if(p<1)requestAnimationFrame(step);
  };
  new IntersectionObserver((ents,obs)=>{
    if(ents[0].isIntersecting){requestAnimationFrame(step);obs.disconnect()}
  },{threshold:.5}).observe(el);
});
</script>
</body>
</html>"""


@app.route("/")
def index():
    return render_template_string(TEMPLATE, p=PORTFOLIO)


if __name__ == "__main__":
    print("🚀  Portfolio running → http://localhost:8080")
    app.run(debug=True, port=8080)
