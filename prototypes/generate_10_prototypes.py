import os

prototypes = [
    {
        "id": 6,
        "name": "Pastel Lavender Liquid Droplet",
        "bg": "#F5F3FF",
        "text": "#1E1B4B",
        "card_bg": "#FFFFFF",
        "border": "#DDD6FE",
        "accent": "#8B5CF6",
        "font_family": "'Cinzel Decorative', serif",
        "font_body": "'Cormorant Garamond', serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:wght@500;600;700&display=swap",
        "desc": "Liquid Mercury Droplet with harmonic undulating vertex ripples and high-specular pastel reflection.",
        "tool_title": "Sovereign Annuity Cashflow Cascade",
        "tool_desc": "Visualizing post-tax quarterly liquidity sweeps across PPF, Sukanya Samriddhi & G-Sec Gilts.",
        "badge": "PASTEL LAVENDER • PROTO 06",
        "three_script": """
          const geo = new THREE.IcosahedronGeometry(4.2, 32);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xC4B5FD, metalness: 0.85, roughness: 0.1, transmission: 0.6, thickness: 2.0 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          const pos = geo.attributes.position;
          const orig = pos.clone();
          animateHook = (t) => {
            for (let i = 0; i < pos.count; i++) {
              const u = orig.getX(i), v = orig.getY(i), w = orig.getZ(i);
              const dist = Math.sin(t * 3 + u * 1.5 + v * 1.5) * 0.35;
              pos.setXYZ(i, u + u * dist * 0.1, v + v * dist * 0.1, w + w * dist * 0.1);
            }
            pos.needsUpdate = true;
            mesh.rotation.y += 0.008;
          };
        """
    },
    {
        "id": 7,
        "name": "Pastel Mint Liquid Ribbon Wave",
        "bg": "#F0FDF4",
        "text": "#064E3B",
        "card_bg": "#FFFFFF",
        "border": "#A7F3D0",
        "accent": "#10B981",
        "font_family": "'Cabinet Grotesk', sans-serif",
        "font_body": "'Satoshi', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,900&f[]=satoshi@500,700&display=swap",
        "desc": "Endless Mobius Ribbon twisting dynamically in 3D pastel mint space with soft specular sheen.",
        "tool_title": "Fama-French 5-Factor Alpha Decomposer",
        "tool_desc": "Dissecting domestic equity outperformance across Size (SMB), Value (HML), and Momentum (WML).",
        "badge": "PASTEL MINT • PROTO 07",
        "three_script": """
          const geo = new THREE.TorusGeometry(4.8, 1.2, 30, 200);
          const mat = new THREE.MeshStandardMaterial({ color: 0x6EE7B7, metalness: 0.7, roughness: 0.2 });
          mesh = new THREE.Mesh(geo, mat);
          mesh.rotation.x = Math.PI * 0.3;
          scene.add(mesh);
          animateHook = (t) => {
            mesh.rotation.x += 0.01;
            mesh.rotation.y += 0.014;
            mesh.rotation.z = Math.sin(t) * 0.2;
          };
        """
    },
    {
        "id": 8,
        "name": "Pastel Peach Gyroscopic Atom",
        "bg": "#FFF7ED",
        "text": "#7C2D12",
        "card_bg": "#FFFFFF",
        "border": "#FED7AA",
        "accent": "#F97316",
        "font_family": "'Clash Display', sans-serif",
        "font_body": "'Outfit', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=clash-display@700,600&display=swap",
        "desc": "3-Tier Orbital Planetary Core with pastel peach rings and counter-rotating golden electrons.",
        "tool_title": "Grade-A REIT NDCF Yield Matrix",
        "tool_desc": "Live quarterly distribution monitor for Embassy, Mindspace & Brookfield real assets.",
        "badge": "PASTEL PEACH • PROTO 08",
        "three_script": """
          const group = new THREE.Group();
          const core = new THREE.Mesh(new THREE.SphereGeometry(2.2, 32, 32), new THREE.MeshStandardMaterial({ color: 0xFDBA74, metalness: 0.8, roughness: 0.2 }));
          group.add(core);
          const r1 = new THREE.Mesh(new THREE.TorusGeometry(5.2, 0.12, 16, 100), new THREE.MeshBasicMaterial({ color: 0xFB923C, wireframe: true }));
          const r2 = new THREE.Mesh(new THREE.TorusGeometry(6.4, 0.12, 16, 100), new THREE.MeshBasicMaterial({ color: 0xFDBA74, wireframe: true }));
          r1.rotation.x = Math.PI * 0.4; r2.rotation.y = Math.PI * 0.35;
          group.add(r1); group.add(r2);
          scene.add(group);
          animateHook = (t) => {
            group.rotation.y += 0.01;
            r1.rotation.x += 0.015;
            r2.rotation.y += 0.018;
          };
        """
    },
    {
        "id": 9,
        "name": "Pastel Sky Floating Quantum Shards",
        "bg": "#F0F9FF",
        "text": "#0C4A6E",
        "card_bg": "#FFFFFF",
        "border": "#BAE6FD",
        "accent": "#0284C7",
        "font_family": "'DM Serif Display', serif",
        "font_body": "'Plus Jakarta Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap",
        "desc": "24 Floating Prismatic Octahedrons breathing harmonically around a central pastel sky vortex.",
        "tool_title": "Theta Decay Cashflow Scanner",
        "tool_desc": "Monthly covered options theta decay rent schedule generating 0.85%–1.15% passive yield.",
        "badge": "PASTEL SKY • PROTO 09",
        "three_script": """
          const group = new THREE.Group();
          const mat = new THREE.MeshStandardMaterial({ color: 0x7DD3FC, metalness: 0.9, roughness: 0.15 });
          for (let i = 0; i < 20; i++) {
            const sh = new THREE.Mesh(new THREE.OctahedronGeometry(0.7, 0), mat);
            const a = (i / 20) * Math.PI * 2;
            sh.position.set(Math.cos(a) * 5.5, Math.sin(a) * 3.5, (Math.random() - 0.5) * 4);
            group.add(sh);
          }
          scene.add(group);
          animateHook = (t) => {
            group.rotation.y += 0.012;
            group.rotation.z = Math.sin(t * 0.8) * 0.15;
          };
        """
    },
    {
        "id": 10,
        "name": "Pastel Rose Hyper-Torus Knot",
        "bg": "#FFF1F2",
        "text": "#881337",
        "card_bg": "#FFFFFF",
        "border": "#FECDD3",
        "accent": "#E11D48",
        "font_family": "'Playfair Display', serif",
        "font_body": "'Epilogue', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Epilogue:wght@500;700&family=Playfair+Display:wght@700;900&display=swap",
        "desc": "Complex (3,7) Torus Knot in liquid pastel rose metallic gold alloy spinning in perpetual momentum.",
        "tool_title": "Sovereign Gold Bond (SGB) Compounding Modeler",
        "tool_desc": "Calculating 2.50% sovereign coupon reinvestment + 0% Section 47(viic) capital gains tax shield.",
        "badge": "PASTEL ROSE • PROTO 10",
        "three_script": """
          const geo = new THREE.TorusKnotGeometry(3.6, 0.9, 140, 24, 3, 7);
          const mat = new THREE.MeshStandardMaterial({ color: 0xFDA4AF, metalness: 0.85, roughness: 0.2 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          animateHook = (t) => {
            mesh.rotation.x += 0.008;
            mesh.rotation.y += 0.014;
          };
        """
    },
    {
        "id": 11,
        "name": "Pastel Butter Gold Dynamic Waves",
        "bg": "#FEFCE8",
        "text": "#713F12",
        "card_bg": "#FFFFFF",
        "border": "#FEF08A",
        "accent": "#CA8A04",
        "font_family": "'Fraunces', serif",
        "font_body": "'Manrope', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Manrope:wght@500;700&display=swap",
        "desc": "Topological undulating liquid plane simulating sovereign capital market depths in golden pastel.",
        "tool_title": "Small-Cap Discovery Convex Multiplier",
        "tool_desc": "Systematic earnings momentum filter tracking 28.4% historical rolling CAGR outperformance.",
        "badge": "PASTEL GOLD • PROTO 11",
        "three_script": """
          const geo = new THREE.PlaneGeometry(16, 16, 32, 32);
          const mat = new THREE.MeshStandardMaterial({ color: 0xFDE047, metalness: 0.7, roughness: 0.3, wireframe: true });
          mesh = new THREE.Mesh(geo, mat);
          mesh.rotation.x = -Math.PI * 0.35;
          scene.add(mesh);
          const pos = geo.attributes.position;
          const orig = pos.clone();
          animateHook = (t) => {
            for (let i = 0; i < pos.count; i++) {
              const u = orig.getX(i), v = orig.getY(i);
              pos.setZ(i, Math.sin(t * 2 + u * 0.8 + v * 0.8) * 1.2);
            }
            pos.needsUpdate = true;
            mesh.rotation.z += 0.004;
          };
        """
    },
    {
        "id": 12,
        "name": "Pastel Lilac Prismatic Crystal Pyramid",
        "bg": "#FAF5FF",
        "text": "#581C87",
        "card_bg": "#FFFFFF",
        "border": "#E9D5FF",
        "accent": "#9333EA",
        "font_family": "'Syne', sans-serif",
        "font_body": "'Inter', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Inter:wght@500;700&family=Syne:wght@800;900&display=swap",
        "desc": "Multi-faceted 3D Glass Tetrahedron refracting pastel lilac light rays across space.",
        "tool_title": "Global USD Technology (VOO/SMH) FX Shield",
        "tool_desc": "Simulating long-term USD appreciation spread (~3.2% CAGR) protecting Indian domestic wealth.",
        "badge": "PASTEL LILAC • PROTO 12",
        "three_script": """
          const geo = new THREE.TetrahedronGeometry(4.8, 0);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xD8B4FE, metalness: 0.2, roughness: 0.1, transmission: 0.8, thickness: 3.0 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          const wire = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color: 0x9333EA, wireframe: true }));
          wire.scale.set(1.05, 1.05, 1.05);
          scene.add(wire);
          animateHook = (t) => {
            mesh.rotation.x += 0.01;
            mesh.rotation.y += 0.015;
            wire.rotation.x += 0.01;
            wire.rotation.y += 0.015;
          };
        """
    },
    {
        "id": 13,
        "name": "Pastel Coral Floating Double Ring",
        "bg": "#FFF1F2",
        "text": "#9F1239",
        "card_bg": "#FFFFFF",
        "border": "#FECDD3",
        "accent": "#F43F5E",
        "font_family": "'Bebas Neue', sans-serif",
        "font_body": "'Work Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Work+Sans:wght@500;700&display=swap",
        "desc": "Twin Intersecting Pastel Coral Torus Rings spinning on offset Euler axes with metallic gloss.",
        "tool_title": "The 70:15:15 Institutional Asset Rebalancer",
        "tool_desc": "Dynamic quarterly drift rebalancer maintaining 70% Bedrock, 15% Real Assets & 15% Alpha.",
        "badge": "PASTEL CORAL • PROTO 13",
        "three_script": """
          const group = new THREE.Group();
          const mat = new THREE.MeshStandardMaterial({ color: 0xFB7185, metalness: 0.85, roughness: 0.2 });
          const t1 = new THREE.Mesh(new THREE.TorusGeometry(4.5, 0.6, 20, 80), mat);
          const t2 = new THREE.Mesh(new THREE.TorusGeometry(4.5, 0.6, 20, 80), mat);
          t2.rotation.x = Math.PI * 0.5;
          group.add(t1); group.add(t2);
          scene.add(group);
          animateHook = (t) => {
            group.rotation.x += 0.012;
            group.rotation.y += 0.015;
          };
        """
    },
    {
        "id": 14,
        "name": "Pastel Sage Quantum Gyroscope",
        "bg": "#F6FBF7",
        "text": "#14532D",
        "card_bg": "#FFFFFF",
        "border": "#BBF7D0",
        "accent": "#16A34A",
        "font_family": "'General Sans', sans-serif",
        "font_body": "'Satoshi', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=general-sans@700,600&f[]=satoshi@500,700&display=swap",
        "desc": "Triple-Axis Mechanical Gyroscope in calming pastel sage and brushed platinum.",
        "tool_title": "Section 14 Court Attachment Legal Immunity Shield",
        "tool_desc": "Statutory legal analysis protecting PPF & SSY corpora from creditors, debt, and court orders.",
        "badge": "PASTEL SAGE • PROTO 14",
        "three_script": """
          const group = new THREE.Group();
          const mat1 = new THREE.MeshStandardMaterial({ color: 0x86EFAC, metalness: 0.9, roughness: 0.15 });
          const mat2 = new THREE.MeshStandardMaterial({ color: 0x4ADE80, metalness: 0.8, roughness: 0.2 });
          const r1 = new THREE.Mesh(new THREE.TorusGeometry(3.5, 0.2, 16, 80), mat1);
          const r2 = new THREE.Mesh(new THREE.TorusGeometry(5.0, 0.2, 16, 80), mat2);
          const r3 = new THREE.Mesh(new THREE.TorusGeometry(6.5, 0.2, 16, 80), mat1);
          r2.rotation.x = Math.PI * 0.4;
          r3.rotation.y = Math.PI * 0.35;
          group.add(r1); group.add(r2); group.add(r3);
          scene.add(group);
          animateHook = (t) => {
            r1.rotation.x += 0.02;
            r2.rotation.y += 0.015;
            r3.rotation.z += 0.01;
            group.rotation.y += 0.008;
          };
        """
    },
    {
        "id": 15,
        "name": "Pastel Opal Liquid Nebula Core",
        "bg": "#F8FAFC",
        "text": "#0F172A",
        "card_bg": "#FFFFFF",
        "border": "#E2E8F0",
        "accent": "#0EA5E9",
        "font_family": "'Plus Jakarta Sans', sans-serif",
        "font_body": "'JetBrains Mono', monospace",
        "font_url": "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@800;900&display=swap",
        "desc": "Breathing 3D Geometric Opal with dynamic multi-light dispersion and interactive inertia.",
        "tool_title": "200-Module Master Quantitative Codex Engine",
        "tool_desc": "Unified institutional interface spanning all 200 sovereign assets with instant filtering.",
        "badge": "PASTEL OPAL • PROTO 15",
        "three_script": """
          const geo = new THREE.DodecahedronGeometry(4.2, 0);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xBAE6FD, metalness: 0.1, roughness: 0.1, transmission: 0.85, thickness: 2.5 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          const core = new THREE.Mesh(new THREE.IcosahedronGeometry(2.0, 0), new THREE.MeshStandardMaterial({ color: 0x38BDF8, metalness: 0.9, roughness: 0.1 }));
          scene.add(core);
          animateHook = (t) => {
            mesh.rotation.x += 0.008;
            mesh.rotation.y += 0.012;
            core.rotation.y -= 0.02;
          };
        """
    }
]

template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>qnt. | {name} ({badge})</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{font_url}" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{
      background-color: {bg} !important;
      color: {text} !important;
      font-family: {font_body};
      overflow-x: hidden;
    }}
    h1, h2, h3, .font-title {{
      font-family: {font_family} !important;
    }}
    #canvas3d {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
    }}
    .pastel-card {{
      background: {card_bg} !important;
      border: 2.5px solid {border};
      border-radius: 24px;
      box-shadow: 6px 6px 0px {border};
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .pastel-card:hover {{
      transform: translate(-3px, -3px);
      box-shadow: 10px 10px 0px {accent};
      border-color: {accent};
    }}
  </style>
</head>
<body class="relative min-h-screen">
  <canvas id="canvas3d"></canvas>

  <div class="relative z-10 max-w-7xl mx-auto p-6 md:p-12">
    <!-- NAV -->
    <header class="flex justify-between items-center pb-8 border-b-2 border-slate-900/10 mb-12">
      <div class="flex items-center space-x-4">
        <a href="index.html" class="text-xs font-mono font-bold px-4 py-2 rounded-xl bg-white border-2 border-slate-900 shadow-[3px_3px_0px_#000] hover:bg-black hover:text-white transition">
          &larr; Prototype Lab Hub
        </a>
        <div class="text-4xl font-black font-title tracking-tighter">qnt.</div>
      </div>
      <div class="px-4 py-2 rounded-xl bg-white border-2 border-slate-900 text-xs font-mono font-black shadow-[3px_3px_0px_#000]">
        {badge}
      </div>
    </header>

    <!-- HERO -->
    <div class="text-center max-w-4xl mx-auto mb-16">
      <div class="inline-block bg-white border-2 border-slate-900 text-xs font-mono font-black px-4 py-1.5 rounded-full mb-4 shadow-[2px_2px_0px_#000]">
        {desc}
      </div>
      <h1 class="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight mb-4">
        {name}
      </h1>
      <p class="text-sm md:text-base font-medium max-w-2xl mx-auto leading-relaxed opacity-80">
        Deterministic quantitative wealth architecture running in real-time 3D pastel space with zero-void institutional engineering.
      </p>
    </div>

    <!-- BESPOKE ANALYTICAL TOOL -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
      <div class="pastel-card p-8 md:col-span-2">
        <div class="flex justify-between items-start mb-4">
          <div>
            <span class="text-xs font-mono font-black uppercase text-slate-500">BESPOKE ANALYTICAL ENGINE</span>
            <h3 class="text-2xl font-black mt-1">{tool_title}</h3>
          </div>
          <span class="text-xs font-mono font-black bg-white border border-slate-900 px-3 py-1 rounded-lg">LIVE METRIC</span>
        </div>
        <p class="text-xs leading-relaxed mb-6 font-medium opacity-80">{tool_desc}</p>
        
        <div class="grid grid-cols-3 gap-4 font-mono text-xs pt-4 border-t border-slate-900/10">
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="text-[10px] text-slate-500">STATUTORY SHIELD</div>
            <div class="text-lg font-black mt-1">100% Tax-Free</div>
          </div>
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="text-[10px] text-slate-500">ROLLING CAGR</div>
            <div class="text-lg font-black mt-1">15.4% – 28.4%</div>
          </div>
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="text-[10px] text-slate-500">99% VaR MOAT</div>
            <div class="text-lg font-black mt-1">Sub-12% Drawdown</div>
          </div>
        </div>
      </div>

      <div class="pastel-card p-8 flex flex-col justify-between">
        <div>
          <span class="text-xs font-mono font-black uppercase text-slate-500">CODEX ACCESS</span>
          <h3 class="text-xl font-black mt-1 mb-3">Institutional Compendium</h3>
          <p class="text-xs leading-relaxed opacity-80 mb-6">
            The definitive 282-page mathematical monograph covering all 200 sovereign asset modules and 6 institutional desks.
          </p>
        </div>
        <a href="reports/qnt_Universal_Financial_Freedom_Institutional_Compendium.pdf" download class="w-full text-center bg-black text-white font-mono font-black text-xs py-3.5 rounded-xl border-2 border-black shadow-[4px_4px_0px_#000] hover:bg-white hover:text-black transition block">
          Download Monograph PDF &rarr;
        </a>
      </div>
    </div>

  </div>

  <script>
    let scene, camera, renderer, mesh, animateHook = null;
    function init3D() {{
      const canvas = document.getElementById('canvas3d');
      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
      camera.position.z = 20;

      renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true }});
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      // Studio Lights
      const amb = new THREE.AmbientLight(0xffffff, 1.4);
      scene.add(amb);
      const dir = new THREE.DirectionalLight(0xffffff, 2.0);
      dir.position.set(10, 20, 15);
      scene.add(dir);
      const point = new THREE.PointLight(0xffffff, 2.5, 40);
      point.position.set(-10, -5, 10);
      scene.add(point);

      {three_script}

      window.addEventListener('resize', () => {{
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
      }});

      animate();
    }}

    function animate() {{
      requestAnimationFrame(animate);
      const t = Date.now() * 0.0015;
      if (animateHook) animateHook(t);
      renderer.render(scene, camera);
    }}

    window.addEventListener('DOMContentLoaded', init3D);
  </script>
</body>
</html>
"""

for p in prototypes:
    content = template.format(
        id=p["id"],
        name=p["name"],
        bg=p["bg"],
        text=p["text"],
        card_bg=p["card_bg"],
        border=p["border"],
        accent=p["accent"],
        font_family=p["font_family"],
        font_body=p["font_body"],
        font_url=p["font_url"],
        desc=p["desc"],
        tool_title=p["tool_title"],
        tool_desc=p["tool_desc"],
        badge=p["badge"],
        three_script=p["three_script"]
    )
    path = f"/data/project_qnt_netlify/proto{p['id']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {path}")
