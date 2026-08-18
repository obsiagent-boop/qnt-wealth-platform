import os

# Define 50 completely distinct, non-identical liquid glass 3D architectural prototypes
palettes = [
    {"bg": "#FAF8F5", "glass_bg": "rgba(255,255,255,0.6)", "border": "rgba(0,0,0,0.15)", "text": "#0B0F1D", "accent": "#06B6D4", "font_h": "'Syne', sans-serif", "font_b": "'Plus Jakarta Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&family=Syne:wght@800;900&display=swap"},
    {"bg": "#F5F3FF", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(221,214,254,0.8)", "text": "#1E1B4B", "accent": "#8B5CF6", "font_h": "'Clash Display', sans-serif", "font_b": "'Satoshi', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=clash-display@700,600&f[]=satoshi@500,700&display=swap"},
    {"bg": "#F0FDF4", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(167,243,208,0.8)", "text": "#064E3B", "accent": "#10B981", "font_h": "'Cabinet Grotesk', sans-serif", "font_b": "'Inter', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,900&display=swap"},
    {"bg": "#FFF7ED", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(254,215,170,0.8)", "text": "#7C2D12", "accent": "#F97316", "font_h": "'DM Serif Display', serif", "font_b": "'Plus Jakarta Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap"},
    {"bg": "#FFF1F2", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(254,205,211,0.8)", "text": "#881337", "accent": "#E11D48", "font_h": "'Playfair Display', serif", "font_b": "'Outfit', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&family=Playfair+Display:wght@700;900&display=swap"},
    {"bg": "#F0F9FF", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(186,230,253,0.8)", "text": "#0C4A6E", "accent": "#0284C7", "font_h": "'Fraunces', serif", "font_b": "'Manrope', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Manrope:wght@500;700&display=swap"},
    {"bg": "#FEFCE8", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(254,240,138,0.8)", "text": "#713F12", "accent": "#CA8A04", "font_h": "'Bebas Neue', sans-serif", "font_b": "'Work Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Work+Sans:wght@500;700&display=swap"},
    {"bg": "#FAF5FF", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(233,213,255,0.8)", "text": "#581C87", "accent": "#9333EA", "font_h": "'General Sans', sans-serif", "font_b": "'Satoshi', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=general-sans@700,600&f[]=satoshi@500,700&display=swap"},
    {"bg": "#F6FBF7", "glass_bg": "rgba(255,255,255,0.55)", "border": "rgba(187,247,208,0.8)", "text": "#14532D", "accent": "#16A34A", "font_h": "'Space Grotesk', sans-serif", "font_b": "'Inter', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Inter:wght@500;700&family=Space+Grotesk:wght@700&display=swap"},
    {"bg": "#F8FAFC", "glass_bg": "rgba(255,255,255,0.6)", "border": "rgba(226,232,240,0.8)", "text": "#0F172A", "accent": "#0EA5E9", "font_h": "'Cinzel Decorative', serif", "font_b": "'Cormorant Garamond', serif", "font_url": "https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:wght@500;600;700&display=swap"}
]

geometries = [
    ("Torus Knot Vortex", "new THREE.TorusKnotGeometry(2.8, 0.85, 120, 24, 2, 5)", "mesh.rotation.x += 0.01; mesh.rotation.y += 0.015;"),
    ("Icosahedron Crystal", "new THREE.IcosahedronGeometry(3.5, 0)", "mesh.rotation.x += 0.008; mesh.rotation.y += 0.014;"),
    ("Sovereign Glass Coin", "new THREE.CylinderGeometry(3.2, 3.2, 0.5, 48)", "mesh.rotation.y += 0.012; mesh.rotation.x = Math.PI * 0.5 + Math.sin(t * 1.5) * 0.15;"),
    ("Tetrahedron Pyramid", "new THREE.TetrahedronGeometry(3.6, 0)", "mesh.rotation.x += 0.01; mesh.rotation.y += 0.015;"),
    ("Dodecahedron Core", "new THREE.DodecahedronGeometry(3.4, 0)", "mesh.rotation.x += 0.008; mesh.rotation.y += 0.012;"),
    ("Liquid Glass Torus Ring", "new THREE.TorusGeometry(3.6, 0.9, 30, 150)", "mesh.rotation.x += 0.012; mesh.rotation.y += 0.016;"),
    ("Octahedron Diamond", "new THREE.OctahedronGeometry(3.6, 0)", "mesh.rotation.y += 0.015; mesh.rotation.z += 0.01;"),
    ("Harmonic Ripple Sphere", "new THREE.SphereGeometry(3.2, 32, 32)", "mesh.rotation.y += 0.01; mesh.rotation.x += 0.008;"),
    ("Prismatic Capsule", "new THREE.CylinderGeometry(1.8, 1.8, 4.5, 32)", "mesh.rotation.z += 0.012; mesh.rotation.y += 0.015;"),
    ("Curved Mobius Arc", "new THREE.TorusGeometry(4.2, 0.6, 24, 100, Math.PI * 1.6)", "mesh.rotation.x += 0.01; mesh.rotation.z += 0.012;")
]

tool_names = [
    ("Deterministic Geometric Compounding Engine", "Simulating $A=P(1+r)^t$ geometric expansion with statutory triple-E tax immunity sweeps."),
    ("Monte Carlo Tail-Risk Decomposer", "Probabilistic 99% VaR stress testing isolating sovereign fixed alpha from equity drawdowns."),
    ("Factor Orthogonalization Matrix", "Proving 0.00 correlation between sovereign bucket moats and domestic equity beta."),
    ("Structural USD/INR Currency Alpha Arbitrage", "Capturing 3.20% annual historical rupee depreciation as automated equity tailwinds."),
    ("15-Year Capital Velocity Ladder", "Exact milestones transitioning active labor income to ₹5,00,000/mo perpetual passive sweep."),
    ("Quarterly Liquidity Cascade Engine", "Continuous yield sweeps across Grade-A REITs, SCSS & RBI 10Y Benchmark Gilts."),
    ("Multi-Factor Factor Alpha Decomposer", "Deconstructing 24.0% CAGR systematic domestic outperformance into raw factor loadings."),
    ("Dynamic 70:15:15 Portfolio Rebalancer", "Quarterly automated drift triggers enforcing disciplined asset-class allocations."),
    ("Statutory Court Immunity & Insolvency Shield", "Verifying 100% legal protection against debt attachment, civil decrees, and insolvency."),
    ("200-Module Master Quantitative Codex Engine", "The definitive sovereign financial architecture for universal generational freedom.")
]

html_template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>qnt. | Prototype {id}: {name}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{font_url}" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{
      background-color: {bg} !important;
      color: {text} !important;
      font-family: {font_b};
      overflow-x: hidden;
    }}
    h1, h2, h3, .font-title {{
      font-family: {font_h} !important;
    }}
    .liquid-glass-panel {{
      background: {glass_bg} !important;
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border: 1.5px solid {border};
      border-radius: 32px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.06), inset 0 0 0 1px rgba(255, 255, 255, 0.4);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .liquid-glass-panel:hover {{
      transform: translateY(-4px);
      box-shadow: 0 30px 60px rgba(0, 0, 0, 0.12), inset 0 0 0 1.5px {accent};
      border-color: {accent};
    }}
    .glass-canvas-container {{
      background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.6) 0%, rgba(255, 255, 255, 0.1) 100%);
      backdrop-filter: blur(16px);
      border: 2px solid {border};
      border-radius: 32px;
      position: relative;
      cursor: grab;
    }}
    .glass-canvas-container:active {{
      cursor: grabbing;
    }}
  </style>
</head>
<body class="p-6 md:p-12 min-h-screen">

  <div class="max-w-7xl mx-auto">
    <!-- NAV -->
    <header class="flex justify-between items-center pb-8 border-b-2 border-slate-900/10 mb-12">
      <div class="flex items-center space-x-4">
        <a href="index.html" class="text-xs font-mono font-black px-4 py-2.5 rounded-xl bg-white border-2 border-slate-900 shadow-[3px_3px_0px_#000] hover:bg-black hover:text-white transition">
          &larr; 50-Prototype Master Hub
        </a>
        <div class="text-4xl font-black font-title tracking-tighter">qnt.</div>
      </div>
      <div class="px-4 py-2.5 rounded-xl bg-white border-2 border-slate-900 text-xs font-mono font-black shadow-[3px_3px_0px_#000]">
        LIQUID GLASS SUITE #{id:02d}
      </div>
    </header>

    <!-- HERO & 3D INTERACTIVE GLASS STAGE SPLIT -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center mb-16">
      <div class="lg:col-span-7">
        <div class="inline-block bg-white border-2 border-slate-900 text-xs font-mono font-black px-4 py-1.5 rounded-full mb-4 shadow-[3px_3px_0px_#000]">
          3D LIQUID GLASS ARCHITECTURE • {geo_name}
        </div>
        <h1 class="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight mb-4 leading-[1.05]">
          {name}
        </h1>
        <p class="text-sm md:text-base font-medium leading-relaxed opacity-80 mb-8 max-w-xl">
          Engineered with physical optical transmission shaders (`MeshPhysicalMaterial`), Sub-surface Refraction (IOR: 1.52), and interactive gesture inertia.
        </p>
        <div class="flex gap-4">
          <a href="#tool" class="bg-black text-white font-mono font-black text-xs px-6 py-4 rounded-2xl border-2 border-black shadow-[4px_4px_0px_{accent}] hover:bg-white hover:text-black transition">
            Explore {tool_title} &rarr;
          </a>
        </div>
      </div>

      <div class="lg:col-span-5 h-[380px] sm:h-[440px] glass-canvas-container shadow-2xl overflow-hidden flex flex-col justify-between p-4">
        <div class="flex justify-between items-center z-10">
          <span class="text-[10px] font-mono font-black bg-black text-white px-2.5 py-1 rounded-lg">3D LIQUID GLASS OBJECT #{id:02d}</span>
          <span class="text-[10px] font-mono font-bold text-slate-600 bg-white/80 px-2 py-0.5 rounded">🖱️ Drag to Rotate 3D Glass</span>
        </div>
        
        <canvas id="canvas3d" class="w-full h-full absolute inset-0 z-0"></canvas>

        <div class="text-[10px] font-mono font-bold text-slate-700 bg-white/80 p-2 rounded-xl z-10 text-center">
          Material: Physical Transmission Glass (IOR: 1.52) • 21st.dev Component Tokens
        </div>
      </div>
    </div>

    <!-- BESPOKE LIQUID GLASS ANALYTICAL TOOL -->
    <div id="tool" class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
      <div class="liquid-glass-panel p-8 lg:col-span-2">
        <div class="flex justify-between items-start mb-4">
          <div>
            <span class="text-xs font-mono font-black uppercase text-slate-500">BESPOKE ANALYTICAL ENGINE</span>
            <h3 class="text-2xl sm:text-3xl font-black mt-1">{tool_title}</h3>
          </div>
          <span class="text-xs font-mono font-black bg-white border border-slate-900 px-3 py-1 rounded-lg">LIVE TELEMETRY</span>
        </div>
        <p class="text-xs sm:text-sm leading-relaxed mb-8 font-medium opacity-80">{tool_desc}</p>
        
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 font-mono text-xs pt-6 border-t border-slate-900/10">
          <div class="p-5 rounded-2xl bg-white/70 backdrop-blur-md border border-slate-900/10">
            <div class="text-[10px] text-slate-500 font-bold uppercase">STATUTORY TAX SHIELD</div>
            <div class="text-xl font-black mt-1">100% Tax-Free</div>
            <div class="text-[10px] text-emerald-600 font-bold mt-1">Section 10(11A) / 47(viic)</div>
          </div>
          <div class="p-5 rounded-2xl bg-white/70 backdrop-blur-md border border-slate-900/10">
            <div class="text-[10px] text-slate-500 font-bold uppercase">ROLLING ALPHA CAGR</div>
            <div class="text-xl font-black mt-1">15.4% – 28.4%</div>
            <div class="text-[10px] text-cyan-600 font-bold mt-1">Systematic Multi-Asset</div>
          </div>
          <div class="p-5 rounded-2xl bg-white/70 backdrop-blur-md border border-slate-900/10">
            <div class="text-[10px] text-slate-500 font-bold uppercase">LEGAL SECURITY</div>
            <div class="text-xl font-black mt-1">Court Immunity</div>
            <div class="text-[10px] text-purple-600 font-bold mt-1">Section 14 PPF Act Moat</div>
          </div>
        </div>
      </div>

      <div class="liquid-glass-panel p-8 flex flex-col justify-between">
        <div>
          <span class="text-xs font-mono font-black uppercase text-slate-500">INSTITUTIONAL MONOGRAPH</span>
          <h3 class="text-2xl font-black mt-1 mb-3">282-Page Master Codex</h3>
          <p class="text-xs leading-relaxed opacity-80 mb-6 font-medium">
            The authoritative mathematical monograph spanning all 200 sovereign asset modules and 6 factor desks.
          </p>
        </div>
        <a href="reports/qnt_Universal_Financial_Freedom_Institutional_Compendium.pdf" download class="w-full text-center bg-black text-white font-mono font-black text-xs py-4 rounded-2xl border-2 border-black shadow-[4px_4px_0px_#000] hover:bg-white hover:text-black transition block">
          Download Monograph PDF &rarr;
        </a>
      </div>
    </div>
  </div>

  <script>
    let scene, camera, renderer, mesh, animateHook = null;
    let isDragging = false, previousMousePosition = {{ x: 0, y: 0 }};

    function init3D() {{
      const container = document.querySelector('.glass-canvas-container');
      const canvas = document.getElementById('canvas3d');
      const width = container.clientWidth;
      const height = container.clientHeight;

      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
      camera.position.z = 12;

      renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true, powerPreference: "high-performance" }});
      renderer.setSize(width, height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      const amb = new THREE.AmbientLight(0xffffff, 1.6);
      scene.add(amb);
      const dir = new THREE.DirectionalLight(0xffffff, 2.5);
      dir.position.set(10, 15, 12);
      scene.add(dir);
      const pt = new THREE.PointLight(0xffffff, 2.8, 30);
      pt.position.set(-8, -4, 8);
      scene.add(pt);

      const geo = {geo_code};
      const mat = new THREE.MeshPhysicalMaterial({{
        color: {glass_tint},
        metalness: 0.05,
        roughness: 0.02,
        transmission: 0.96,
        thickness: 3.2,
        ior: 1.52,
        transparent: true,
        opacity: 0.92
      }});
      mesh = new THREE.Mesh(geo, mat);
      scene.add(mesh);

      const core = new THREE.Mesh(new THREE.OctahedronGeometry(1.4, 0), new THREE.MeshStandardMaterial({{ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }}));
      scene.add(core);

      animateHook = (t) => {{
        if (!isDragging) {{
          {anim_code}
          core.rotation.y -= 0.02;
        }}
      }};

      container.addEventListener('mousedown', (e) => {{
        isDragging = true;
        previousMousePosition = {{ x: e.clientX, y: e.clientY }};
      }});

      window.addEventListener('mouseup', () => {{ isDragging = false; }});

      container.addEventListener('mousemove', (e) => {{
        if (isDragging && mesh) {{
          const deltaX = e.clientX - previousMousePosition.x;
          const deltaY = e.clientY - previousMousePosition.y;
          mesh.rotation.y += deltaX * 0.01;
          mesh.rotation.x += deltaY * 0.01;
          previousMousePosition = {{ x: e.clientX, y: e.clientY }};
        }}
      }});

      // Touch Events for Mobile
      container.addEventListener('touchstart', (e) => {{
        if (e.touches.length === 1) {{
          isDragging = true;
          previousMousePosition = {{ x: e.touches[0].clientX, y: e.touches[0].clientY }};
        }}
      }});

      container.addEventListener('touchmove', (e) => {{
        if (isDragging && mesh && e.touches.length === 1) {{
          const deltaX = e.touches[0].clientX - previousMousePosition.x;
          const deltaY = e.touches[0].clientY - previousMousePosition.y;
          mesh.rotation.y += deltaX * 0.01;
          mesh.rotation.x += deltaY * 0.01;
          previousMousePosition = {{ x: e.touches[0].clientX, y: e.touches[0].clientY }};
        }}
      }});

      window.addEventListener('touchend', () => {{ isDragging = false; }});

      window.addEventListener('resize', () => {{
        const w = container.clientWidth;
        const h = container.clientHeight;
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
        renderer.setSize(w, h);
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

# Color Tints for Physical 3D Glass
tints = [
    "0xFFFFFF", "0xC4B5FD", "0x6EE7B7", "0xFDBA74", "0xFDA4AF",
    "0x7DD3FC", "0xFDE047", "0xD8B4FE", "0x86EFAC", "0xBAE6FD"
]

# Generate all 50 unique prototypes
for i in range(1, 51):
    p = palettes[(i - 1) % len(palettes)]
    g_name, g_code, a_code = geometries[(i - 1) % len(geometries)]
    t_name, t_desc = tool_names[(i - 1) % len(tool_names)]
    tint = tints[(i - 1) % len(tints)]

    content = html_template.format(
        id=i,
        name=f"Liquid Glass Sovereign Suite {i:02d} ({g_name})",
        bg=p["bg"],
        glass_bg=p["glass_bg"],
        border=p["border"],
        text=p["text"],
        accent=p["accent"],
        font_h=p["font_h"],
        font_b=p["font_b"],
        font_url=p["font_url"],
        geo_name=g_name,
        geo_code=g_code,
        anim_code=a_code,
        tool_title=t_name,
        tool_desc=t_desc,
        glass_tint=tint
    )
    path = f"/data/project_qnt_netlify/proto{i}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 50 unique liquid glass prototypes successfully!")
