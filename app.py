import streamlit as st

st.set_page_config(
    page_title="Hemanth Reddy | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

skills = {
    "PYTHON":      ["Numpy", "Pandas", "Scikit-learn", "Matplotlib", "Seaborn", "BeautifulSoup"],
    "SQL":         ["MySQL", "RDBMS", "CRUD", "DDL/DML", "Joins/Aggregations"],
    "POWER BI":    ["Visualization", "Power Queries", "Power Pivot", "DAX", "Drill Through"],
    "STATISTICS":  ["Descriptive Stats", "Probability Dist.", "Inferential Stats", "Data Gathering"],
    "DEV TOOLS":   ["Jupyter Notebook", "VS Code", "Git/GitHub", "Django", "Linux"],
}

# Added "link" keys here for you to easily replace later
projects = [
    {"tag":"MACHINE LEARNING", "title":"Malicious URL Detection",    "desc":"Classification pipeline to detect malicious URLs using 1,500+ samples. Engineered features via TF-IDF and WHOIS API. Deployed real-time risk assessment app.",  "stack":"Python · Random Forest · SVM · Django · TF-IDF", "link": "https://www.google.com"},
    {"tag":"WEB SCRAPING · EDA", "title":"Job Market Data Analysis", "desc":"Built a scraping pipeline extracting 1,500+ listings from TimesJobs. Standardized data with RegEx and visualized high-demand tech skills via Heatmaps.",       "stack":"Python · BeautifulSoup · Pandas · RegEx", "link": "https://www.google.com"},
    {"tag":"DATABASE ANALYSIS",  "title":"Library Database Analysis", "desc":"Analyzed DB with SQL to assess inventory and identify user patterns. Executed complex queries using JOINs, GROUP BY, and HAVING for management insights.",              "stack":"SQL · MySQL · ER Diagrams", "link": "https://www.google.com"},
    {"tag":"DATA ANALYTICS",     "title":"Telangana Weather Forecasting","desc":"End-to-end ETL pipeline processing 100k+ data points. Engineered a dynamic Power BI dashboard to visualize seasonal trends across 33 districts.",            "stack":"Pandas · Power BI · ETL · Jupyter", "link": "https://www.google.com"},
]

skill_cells = "".join(
    f'<div class="skill-cell"><span class="cat">{cat}</span><span class="name">{item}</span></div>'
    for cat, items in skills.items() for item in items
)

# Added the onclick event to the div wrapper
proj_cards = "".join(f"""
<div class="proj-card" onclick="window.open('{p['link']}', '_blank')">
  <div class="proj-tag">{p['tag']}</div>
  <h3>{p['title']}</h3>
  <p>{p['desc']}</p>
  <div class="proj-stack">{p['stack']}</div>
</div>""" for p in projects)

# --- FULLSCREEN STREAMLIT OVERRIDE ---
st.markdown("""<style>
/* Hide Streamlit UI elements completely */
header[data-testid="stHeader"], 
[data-testid="stToolbar"], 
footer, 
#MainMenu, 
[data-testid="stDecoration"] {
    display: none !important;
}

/* Remove all padding and margins from the main app containers */
[data-testid="stAppViewContainer"], 
[data-testid="stAppViewContainer"] > .main, 
.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

/* Force the iframe to fill the entire screen natively */
iframe {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw !important;
    height: 100vh !important;
    border: none;
    z-index: 999999;
}
</style>""", unsafe_allow_html=True)

# HTML Component
st.components.v1.html(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<script type="importmap">
{{
  "imports": {{
    "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
    "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
  }}
}}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&family=JetBrains+Mono:wght@300;400&display=swap');

:root {{
  --btc: #f7931a;
  --btc-dim: rgba(247,147,26,0.12);
  --white: #f0ede8;
  --muted: rgba(240,237,232,0.50);
  --glass: rgba(4,4,6,0.62);
  --glass-b: rgba(247,147,26,0.18);
}}

* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{
  width:100%; height:100%;
  background:#000;
  color:var(--white);
  font-family:'Space Grotesk',sans-serif;
  overflow-x:hidden;
}}

#canvas-wrap {{
  position:fixed;
  top:0; left:0;
  width:100vw; height:100vh;
  z-index:0;
}}

#content {{
  position:relative;
  z-index:10;
  pointer-events:none;
}}
#content * {{ pointer-events:auto; }}

.hero {{
  height:100vh;
  display:flex; flex-direction:column;
  align-items:center; justify-content:flex-end;
  padding-bottom:9vh; text-align:center;
  pointer-events:none;
}}
.hero-eye {{
  font-family:'JetBrains Mono',monospace;
  font-size:0.62rem; letter-spacing:0.42em;
  color:var(--btc); margin-bottom:1.1rem;
}}
.hero h1 {{
  font-weight:700;
  font-size:clamp(3rem,7vw,6.2rem);
  letter-spacing:-0.02em; line-height:1.04;
  color:var(--white);
  text-shadow:0 0 60px rgba(247,147,26,0.35);
  margin-bottom:0.7rem;
}}
.hero h1 span {{ color:var(--btc); }}
.hero-sub {{
  font-family:'JetBrains Mono',monospace;
  font-size:clamp(0.65rem,1.3vw,0.88rem);
  color:var(--muted); letter-spacing:0.2em;
  margin-bottom:3rem;
}}
.cue {{
  font-family:'JetBrains Mono',monospace;
  font-size:0.55rem; letter-spacing:0.38em;
  color:rgba(247,147,26,0.5);
}}

.section {{
  max-width:900px; margin:0 auto;
  padding:5rem 2rem 1rem;
}}
.s-label {{
  display:block;
  font-family:'JetBrains Mono',monospace;
  font-size:0.58rem; letter-spacing:0.42em;
  color:var(--btc); margin-bottom:0.4rem;
}}
.section h2 {{
  font-weight:700;
  font-size:clamp(1.7rem,3.5vw,2.6rem);
  letter-spacing:-0.01em; color:var(--white); margin:0;
}}
.hr {{
  width:34px; height:2px;
  background:var(--btc);
  margin:0.9rem 0 2.4rem; border-radius:2px;
}}
.glass {{
  background:var(--glass);
  border:1px solid var(--glass-b);
  border-radius:4px;
}}
.about-card {{ padding:2.4rem 2.8rem; }}
.about-card p {{
  font-size:1.04rem; line-height:1.92;
  color:var(--muted); font-weight:300;
}}
.about-card p strong {{ color:var(--btc); font-weight:500; }}

.skills-grid {{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(155px,1fr));
  gap:1px;
  border:1px solid var(--glass-b);
  border-radius:4px; overflow:hidden;
}}
.skill-cell {{
  background:rgba(0,0,0,0.55);
  padding:1.25rem 1.1rem;
  transition:background .2s;
}}
.skill-cell:hover {{ background:var(--btc-dim); }}
.skill-cell .cat {{
  display:block;
  font-family:'JetBrains Mono',monospace;
  font-size:0.48rem; letter-spacing:0.36em;
  color:var(--btc); margin-bottom:0.42rem;
}}
.skill-cell .name {{
  font-size:0.82rem; color:var(--white); font-weight:400;
}}

.proj-grid {{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(255px,1fr));
  gap:1px;
  border:1px solid var(--glass-b);
  border-radius:4px; overflow:hidden;
}}
.proj-card {{
  background:rgba(0,0,0,0.55);
  padding:2rem 1.8rem;
  transition:background .2s, transform .2s;
  cursor: pointer; /* Added pointer cursor so it feels clickable */
}}
.proj-card:hover {{ 
  background:rgba(247,147,26,0.08); 
}}
.proj-tag {{
  font-family:'JetBrains Mono',monospace;
  font-size:0.5rem; letter-spacing:0.34em;
  color:var(--btc); margin-bottom:0.75rem;
}}
.proj-card h3 {{
  font-size:1rem; font-weight:500;
  color:var(--white); margin:0 0 0.6rem;
}}
.proj-card p {{
  font-size:0.84rem; line-height:1.75;
  color:var(--muted); font-weight:300; margin:0 0 1rem;
}}
.proj-stack {{
  font-family:'JetBrains Mono',monospace;
  font-size:0.55rem;
  color:rgba(247,147,26,0.55); letter-spacing:0.1em;
}}

.contact-card {{ padding:2.4rem 2.8rem; }}
.c-row {{
  display:flex; align-items:center; gap:1.4rem;
  padding-bottom:1.1rem; margin-bottom:1.1rem;
  border-bottom:1px solid rgba(247,147,26,0.08);
}}
.c-row:last-child {{ border-bottom:none; margin-bottom:0; padding-bottom:0; }}
.c-key {{
  font-family:'JetBrains Mono',monospace;
  font-size:0.56rem; letter-spacing:0.32em;
  color:var(--btc); min-width:88px;
}}
.c-row a {{
  font-size:0.9rem; color:var(--white);
  text-decoration:none; transition:color .2s;
}}
.c-row a:hover {{ color:var(--btc); }}

.footer {{
  text-align:center; padding:4rem 0 5rem;
  font-family:'JetBrains Mono',monospace;
  font-size:0.52rem; letter-spacing:0.4em;
  color:rgba(247,147,26,0.2);
}}

::-webkit-scrollbar {{ width:3px; }}
::-webkit-scrollbar-track {{ background:transparent; }}
::-webkit-scrollbar-thumb {{ background:rgba(247,147,26,0.25); border-radius:2px; }}
</style>
</head>
<body>

<div id="canvas-wrap"></div>

<div id="content">
  <div class="hero">
    <div class="hero-eye">📊 &nbsp; DATA SCIENCE ENGINEER</div>
    <h1>HEMANTH REDDY <span>YANAMALA</span></h1>
    <div class="hero-sub">MACHINE LEARNING &nbsp;·&nbsp; DATA ANALYTICS &nbsp;·&nbsp; PYTHON DEVELOPER</div>
    <div class="cue">▼ &nbsp; SCROLL TO EXPLORE</div>
  </div>

  <div class="section">
    <span class="s-label">// 01 &nbsp; ABOUT</span>
    <h2>Extracting signal from noise.</h2>
    <div class="hr"></div>
    <div class="about-card glass">
      <p>I am a proactive <strong>Computer Science Engineering student</strong> specializing in <strong>Data Science</strong>. 
      I build robust machine learning models, extract actionable insights from complex datasets, and design dynamic visualization dashboards.<br><br>
      Currently based in <strong>Hyderabad, India</strong>. Passionate about leveraging data to solve real-world problems and actively open to data science roles and collaborative projects.</p>
    </div>
  </div>

  <div class="section" style="padding-top:4rem">
    <span class="s-label">// 02 &nbsp; SKILLS</span>
    <h2>Tools of the trade.</h2>
    <div class="hr"></div>
    <div class="skills-grid">{skill_cells}</div>
  </div>

  <div class="section" style="padding-top:4rem">
    <span class="s-label">// 03 &nbsp; PROJECTS</span>
    <h2>Selected work.</h2>
    <div class="hr"></div>
    <div class="proj-grid">{proj_cards}</div>
  </div>

  <div class="section" style="padding-top:4rem">
    <span class="s-label">// 04 &nbsp; CONTACT</span>
    <h2>Connect the nodes.</h2>
    <div class="hr"></div>
    <div class="contact-card glass">
      <div class="c-row"><span class="c-key">EMAIL</span><a href="mailto:hemanthreddyyanamala73@gmail.com">hemanthreddyyanamala73@gmail.com</a></div>
      <div class="c-row"><span class="c-key">PHONE</span><a href="tel:+919392892973">+91 93928 92973</a></div>
      <div class="c-row"><span class="c-key">GITHUB</span><a href="https://github.com/hemanthreddyyanamala" target="_blank">github.com/hemanthreddyyanamala</a></div>
      <div class="c-row"><span class="c-key">LINKEDIN</span><a href="https://linkedin.com/in/yanamala-hemanth-reddy" target="_blank">linkedin.com/in/yanamala-hemanth-reddy</a></div>
    </div>
  </div>

  <div class="footer">📊 &nbsp;·&nbsp; DATA DRIVEN &nbsp;·&nbsp; 2025</div>
</div>

<script type="module">
import * as THREE from 'three';
import {{ OrbitControls }}   from 'three/addons/controls/OrbitControls.js';

const COUNT  = 10000;   // half original — still looks dense
const SPREAD = 140;
const GOLDEN = 2.39996322973;
const wrap   = document.getElementById('canvas-wrap');

const scene  = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(60, window.innerWidth/window.innerHeight, 0.1, 2000);
camera.position.set(0, 0, 120);

const renderer = new THREE.WebGLRenderer({{
  antialias: false,               
  powerPreference: 'high-performance'
}});
renderer.setPixelRatio(1);        
renderer.setSize(window.innerWidth, window.innerHeight);
wrap.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping   = true;
controls.dampingFactor   = 0.06;
controls.autoRotate      = true;
controls.autoRotateSpeed = 0.5;   
controls.enablePan       = false;
controls.minDistance     = 60;
controls.maxDistance     = 220;

const dummy  = new THREE.Object3D();
const color  = new THREE.Color();
const target = new THREE.Vector3();

const geo   = new THREE.TetrahedronGeometry(0.3);
const mat   = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
const iMesh = new THREE.InstancedMesh(geo, mat, COUNT);
iMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
scene.add(iMesh);

const baseX     = new Float32Array(COUNT);
const baseY     = new Float32Array(COUNT);
const baseZ     = new Float32Array(COUNT);
const seedA     = new Float32Array(COUNT);  
const litBaked  = new Float32Array(COUNT);  

for (let i = 0; i < COUNT; i++) {{
  const u   = i / COUNT;
  const el  = Math.asin(-0.92 + 1.84 * u);
  const az  = i * GOLDEN;
  const cx  = Math.cos(el), sx = Math.sin(el);
  const cz  = Math.cos(az), sz = Math.sin(az);
  const shell = Math.sqrt(u);
  
  const cA  = 0.55 + 0.45 * Math.sin(i * 0.017);
  const cB  = 0.55 + 0.45 * Math.sin(i * 0.011 + 1.7);
  const r   = SPREAD * shell * (0.6 + 0.25 * cA + 0.15 * cB);
  baseX[i]  = cz * cx * r;
  baseY[i]  = sx * r;
  baseZ[i]  = sz * cx * r;

  seedA[i]  = ((i * 7919) % 10000) / 10000;
  litBaked[i] = 0.28 + seedA[i] * 0.14;
}}

const positions = [];
for (let i = 0; i < COUNT; i++) {{
  positions.push(new THREE.Vector3(
    (Math.random() - 0.5) * 100,
    (Math.random() - 0.5) * 100,
    (Math.random() - 0.5) * 100
  ));
  iMesh.setColorAt(i, color.setHSL(0.083, 0.82, litBaked[i]));
}}

iMesh.instanceColor.needsUpdate = true;

const clock = new THREE.Clock();

function animate() {{
  requestAnimationFrame(animate);
  const t = clock.getElapsedTime();
  controls.update();

  const waveT = t * 0.15;

  for (let i = 0; i < COUNT; i++) {{
    const wave = 1.0 + 0.04 * Math.sin(seedA[i] * 6.2832 + waveT);

    target.set(
      baseX[i] * wave,
      baseY[i] * wave,
      baseZ[i] * wave
    );

    positions[i].lerp(target, 0.035);  
    dummy.position.copy(positions[i]);
    dummy.updateMatrix();
    iMesh.setMatrixAt(i, dummy.matrix);
  }}

  iMesh.instanceMatrix.needsUpdate = true;
  renderer.render(scene, camera);
}}
animate();

window.addEventListener('resize', () => {{
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}});
</script>
</body>
</html>""", height=800, scrolling=True)