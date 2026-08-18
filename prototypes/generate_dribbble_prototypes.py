import os

# 6 Master Archetypes with distinct funky, cool 3D animations and typography
archetypes = [
    {
        "type": "3D Kinetic Typographic Mesh ($ Q N T)",
        "tag": "FUNKY 3D TYPOGRAPHY",
        "desc": "Floating 3D extruded Frosted Glass '$ Q N T' typographic letters tumbling in multi-axis spring inertia.",
        "three_code": """
          const group = new THREE.Group();
          const glassMat = new THREE.MeshPhysicalMaterial({ color: 0xFFFFFF, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.5, ior: 1.52, transparent: true, opacity: 0.9 });
          const goldMat = new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 });

          // 3D Dollar Symbol
          const dTop = new THREE.Mesh(new THREE.TorusGeometry(1.2, 0.28, 16, 40, Math.PI * 1.3), glassMat);
          dTop.position.set(-2.5, 1.0, 0); dTop.rotation.z = Math.PI * 0.35;
          const dBtm = new THREE.Mesh(new THREE.TorusGeometry(1.2, 0.28, 16, 40, Math.PI * 1.3), glassMat);
          dBtm.position.set(-2.5, -1.0, 0); dBtm.rotation.z = Math.PI * 1.35;
          const dBar = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 4.5, 24), goldMat);
          dBar.position.set(-2.5, 0, 0);
          group.add(dTop); group.add(dBtm); group.add(dBar);

          // 3D 'Q'
          const qRing = new THREE.Mesh(new THREE.TorusGeometry(1.4, 0.3, 16, 50), glassMat);
          qRing.position.set(0, 0, 0);
          const qTail = new THREE.Mesh(new THREE.BoxGeometry(0.4, 1.2, 0.4), goldMat);
          qTail.position.set(1.0, -1.2, 0); qTail.rotation.z = -Math.PI * 0.25;
          group.add(qRing); group.add(qTail);

          // 3D 'N'
          const nBar1 = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 3.2, 24), glassMat); nBar1.position.set(2.2, 0, 0);
          const nBar2 = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 3.2, 24), glassMat); nBar2.position.set(3.6, 0, 0);
          const nDiag = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 3.6, 24), goldMat); nDiag.position.set(2.9, 0, 0); nDiag.rotation.z = Math.PI * 0.38;
          group.add(nBar1); group.add(nBar2); group.add(nDiag);

          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              group.rotation.y = Math.sin(t * 1.2) * 0.45;
              group.rotation.x = Math.cos(t * 0.9) * 0.25;
              group.position.y = Math.sin(t * 1.5) * 0.35;
            }
          };
        """
    },
    {
        "type": "Funky Gravity Physics Playground",
        "tag": "MAGNETIC BOUNCING COINS",
        "desc": "Floating multi-asset magnetic spheres & gold coins bouncing organically with dynamic spring repulsion.",
        "three_code": """
          const group = new THREE.Group();
          const glassMat = new THREE.MeshPhysicalMaterial({ color: 0xBAE6FD, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.0, ior: 1.5 });
          const colors = [0xF59E0B, 0x10B981, 0x06B6D4, 0x8B5CF6, 0xEC4899, 0x3B82F6];
          const balls = [];

          for (let i = 0; i < 8; i++) {
            const rad = 0.7 + Math.random() * 0.5;
            const mat = i % 2 === 0 ? glassMat : new THREE.MeshStandardMaterial({ color: colors[i % colors.length], metalness: 0.9, roughness: 0.15 });
            const ball = new THREE.Mesh(new THREE.SphereGeometry(rad, 24, 24), mat);
            const a = (i / 8) * Math.PI * 2;
            ball.position.set(Math.cos(a) * 3.5, (Math.random() - 0.5) * 4.0, Math.sin(a) * 3.5);
            group.add(ball);
            balls.push({ mesh: ball, angle: a, speed: 0.015 + Math.random() * 0.02, rad: rad, yOffset: Math.random() * Math.PI * 2 });
          }

          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              group.rotation.y += 0.008;
              balls.forEach(b => {
                b.angle += b.speed;
                b.mesh.position.x = Math.cos(b.angle) * 3.8;
                b.mesh.position.z = Math.sin(b.angle) * 3.8;
                b.mesh.position.y = Math.sin(t * 2.5 + b.yOffset) * 1.8;
                b.mesh.rotation.x += 0.02;
                b.mesh.rotation.y += 0.03;
              });
            }
          };
        """
    },
    {
        "type": "Multi-Layered Frosted Glass Credit Card",
        "tag": "DRIBBLE FINTECH GLASS CARD",
        "desc": "Thick 3D frosted glass card with embedded gold chip, magnetic strip, and orbiting laser halo ribbon.",
        "three_code": """
          const group = new THREE.Group();
          const cardGeo = new THREE.BoxGeometry(6.4, 4.0, 0.28);
          const cardMat = new THREE.MeshPhysicalMaterial({
            color: 0xFFFFFF, metalness: 0.15, roughness: 0.05,
            transmission: 0.92, thickness: 2.2, ior: 1.54,
            clearcoat: 1.0, transparent: true, opacity: 0.9
          });
          const card = new THREE.Mesh(cardGeo, cardMat);
          group.add(card);

          // Embedded Gold Chip
          const chip = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.9, 0.32), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
          chip.position.set(-1.8, 0.6, 0.05);
          group.add(chip);

          // Holographic Ribbon
          const ribbon = new THREE.Mesh(new THREE.TorusGeometry(4.8, 0.08, 16, 100), new THREE.MeshBasicMaterial({ color: 0x06B6D4, wireframe: true }));
          ribbon.rotation.x = Math.PI * 0.45;
          group.add(ribbon);

          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              group.rotation.y = Math.sin(t * 1.2) * 0.4;
              group.rotation.x = Math.cos(t * 1.0) * 0.25;
              group.position.y = Math.sin(t * 1.5) * 0.3;
            }
            ribbon.rotation.z += 0.015;
          };
        """
    },
    {
        "type": "Organic Liquid Glass Metasurface Blob",
        "tag": "ORGANIC MORPHING METABLOB",
        "desc": "Real-time Perlin-noise oscillating liquid glass sphere with continuous surface caustics.",
        "three_code": """
          const geo = new THREE.IcosahedronGeometry(3.2, 32);
          const mat = new THREE.MeshPhysicalMaterial({
            color: 0xC4B5FD, metalness: 0.05, roughness: 0.02,
            transmission: 0.98, thickness: 3.5, ior: 1.55,
            clearcoat: 1.0, transparent: true, opacity: 0.95
          });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);

          const core = new THREE.Mesh(new THREE.OctahedronGeometry(1.5, 0), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
          scene.add(core);

          const pos = geo.attributes.position;
          const orig = pos.clone();

          animateHook = (t) => {
            if (!isDragging) {
              for (let i = 0; i < pos.count; i++) {
                const u = orig.getX(i), v = orig.getY(i), w = orig.getZ(i);
                const noise = Math.sin(t * 2.5 + u * 1.5) * Math.cos(t * 2.0 + v * 1.5) * 0.45;
                pos.setXYZ(i, u + u * noise * 0.15, v + v * noise * 0.15, w + w * noise * 0.15);
              }
              pos.needsUpdate = true;
              mesh.rotation.y += 0.01;
              core.rotation.y -= 0.02;
            }
          };
        """
    },
    {
        "type": "Compounding 3D Glass Data Pillars",
        "tag": "ELEVATING DATA PILLARS",
        "desc": "3D Translucent frosted glass bars elevating dynamically with gold capital tips.",
        "three_code": """
          const group = new THREE.Group();
          const glassMat = new THREE.MeshPhysicalMaterial({ color: 0xFDBA74, metalness: 0.1, roughness: 0.05, transmission: 0.92, thickness: 2.0, ior: 1.5 });
          const goldMat = new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 });

          const bars = [];
          for (let i = 0; i < 5; i++) {
            const h = 2.0 + i * 1.2;
            const bar = new THREE.Mesh(new THREE.BoxGeometry(0.9, h, 0.9), glassMat);
            bar.position.set((i - 2) * 1.3, h / 2 - 2.5, 0);
            group.add(bar);

            const tip = new THREE.Mesh(new THREE.BoxGeometry(0.92, 0.3, 0.92), goldMat);
            tip.position.set((i - 2) * 1.3, h - 2.5, 0);
            group.add(tip);
            bars.push({ bar, tip, baseH: h, i });
          }
          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              group.rotation.y = Math.sin(t * 0.8) * 0.3;
              bars.forEach(b => {
                const scaleY = 1 + Math.sin(t * 2 + b.i * 0.8) * 0.2;
                b.bar.scale.y = scaleY;
                b.tip.position.y = (b.baseH * scaleY) - 2.5;
              });
            }
          };
        """
    },
    {
        "type": "Gyroscopic Holographic Portal Ring",
        "tag": "QUANTUM PORTAL VORTEX",
        "desc": "Triple concentric glass and gold orbital halos with a floating quantum diamond core.",
        "three_code": """
          const group = new THREE.Group();
          const r1 = new THREE.Mesh(new THREE.TorusGeometry(3.6, 0.35, 20, 100), new THREE.MeshPhysicalMaterial({ color: 0x6EE7B7, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.2 }));
          const r2 = new THREE.Mesh(new THREE.TorusGeometry(4.8, 0.12, 16, 100), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
          const r3 = new THREE.Mesh(new THREE.TorusGeometry(5.8, 0.08, 16, 100), new THREE.MeshBasicMaterial({ color: 0x06B6D4, wireframe: true }));
          r2.rotation.x = Math.PI * 0.35; r3.rotation.y = Math.PI * 0.45;
          group.add(r1); group.add(r2); group.add(r3);

          const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.6, 0), new THREE.MeshStandardMaterial({ color: 0x10B981, metalness: 0.9, roughness: 0.1 }));
          group.add(core);

          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              r1.rotation.y += 0.015;
              r2.rotation.z += 0.02;
              r3.rotation.x -= 0.012;
              core.rotation.x -= 0.015;
            }
          };
        """
    }
]

palettes = [
    {"bg": "linear-gradient(135deg, #FAF8F5 0%, #E2E8F0 50%, #FAF8F5 100%)", "card_glass": "rgba(255, 255, 255, 0.25)", "card_border": "rgba(255, 255, 255, 0.7)", "text": "#0B0F1D", "accent": "#06B6D4", "font_h": "'Syne', sans-serif", "font_b": "'Plus Jakarta Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&family=Syne:wght@800;900&display=swap"},
    {"bg": "linear-gradient(135deg, #F5F3FF 0%, #DDD6FE 50%, #F5F3FF 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(221, 214, 254, 0.8)", "text": "#1E1B4B", "accent": "#8B5CF6", "font_h": "'Clash Display', sans-serif", "font_b": "'Satoshi', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=clash-display@700,600&f[]=satoshi@500,700&display=swap"},
    {"bg": "linear-gradient(135deg, #F0FDF4 0%, #A7F3D0 50%, #F0FDF4 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(167, 243, 208, 0.8)", "text": "#064E3B", "accent": "#10B981", "font_h": "'Cabinet Grotesk', sans-serif", "font_b": "'Inter', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,900&display=swap"},
    {"bg": "linear-gradient(135deg, #FFF7ED 0%, #FED7AA 50%, #FFF7ED 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(254, 215, 170, 0.8)", "text": "#7C2D12", "accent": "#F97316", "font_h": "'DM Serif Display', serif", "font_b": "'Plus Jakarta Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap"},
    {"bg": "linear-gradient(135deg, #FFF1F2 0%, #FECDD3 50%, #FFF1F2 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(254, 205, 211, 0.8)", "text": "#881337", "accent": "#E11D48", "font_h": "'Playfair Display', serif", "font_b": "'Outfit', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&family=Playfair+Display:wght@700;900&display=swap"},
    {"bg": "linear-gradient(135deg, #F0F9FF 0%, #BAE6FD 50%, #F0F9FF 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(186, 230, 253, 0.8)", "text": "#0C4A6E", "accent": "#0284C7", "font_h": "'Fraunces', serif", "font_b": "'Manrope', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Manrope:wght@500;700&display=swap"},
    {"bg": "linear-gradient(135deg, #FEFCE8 0%, #FEF08A 50%, #FEFCE8 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(254, 240, 138, 0.8)", "text": "#713F12", "accent": "#CA8A04", "font_h": "'Bebas Neue', sans-serif", "font_b": "'Work Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Work+Sans:wght@500;700&display=swap"},
    {"bg": "linear-gradient(135deg, #FAF5FF 0%, #E9D5FF 50%, #FAF5FF 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(233, 213, 255, 0.8)", "text": "#581C87", "accent": "#9333EA", "font_h": "'General Sans', sans-serif", "font_b": "'Satoshi', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=general-sans@700,600&f[]=satoshi@500,700&display=swap"},
    {"bg": "linear-gradient(135deg, #F6FBF7 0%, #BBF7D0 50%, #F6FBF7 100%)", "card_glass": "rgba(255, 255, 255, 0.3)", "card_border": "rgba(187, 247, 208, 0.8)", "text": "#14532D", "accent": "#16A34A", "font_h": "'Space Grotesk', sans-serif", "font_b": "'Inter', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Inter:wght@500;700&family=Space+Grotesk:wght@700&display=swap"},
    {"bg": "linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 50%, #F8FAFC 100%)", "card_glass": "rgba(255, 255, 255, 0.35)", "card_border": "rgba(226, 232, 240, 0.8)", "text": "#0F172A", "accent": "#0EA5E9", "font_h": "'Cinzel Decorative', serif", "font_b": "'Cormorant Garamond', serif", "font_url": "https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:wght@500;600;700&display=swap"}
]

html_template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>qnt. | Dribbble 3D Suite #{id:02d}: {arch_type}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{font_url}" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{
      background: {bg};
      color: {text};
      font-family: {font_b};
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }}

    .dribbble-blob-1 {{
      position: fixed;
      top: -10%;
      left: 15%;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, {accent} 0%, transparent 70%);
      filter: blur(80px);
      opacity: 0.5;
      z-index: 0;
      animation: blobMove 16s ease-in-out infinite alternate;
      pointer-events: none;
    }}
    .dribbble-blob-2 {{
      position: fixed;
      bottom: -10%;
      right: 10%;
      width: 550px;
      height: 550px;
      background: radial-gradient(circle, #F59E0B 0%, transparent 70%);
      filter: blur(90px);
      opacity: 0.4;
      z-index: 0;
      animation: blobMove 20s ease-in-out infinite alternate-reverse;
      pointer-events: none;
    }}

    @keyframes blobMove {{
      0% {{ transform: translate(0, 0) scale(1); }}
      100% {{ transform: translate(80px, 60px) scale(1.15); }}
    }}

    h1, h2, h3, .font-title {{
      font-family: {font_h} !important;
    }}

    .dribbble-glass-card {{
      background: {card_glass} !important;
      backdrop-filter: blur(32px) saturate(210%) brightness(108%);
      -webkit-backdrop-filter: blur(32px) saturate(210%) brightness(108%);
      border: 1.5px solid {card_border};
      border-radius: 36px;
      box-shadow: 
        0 30px 70px -15px rgba(0, 0, 0, 0.15),
        inset 0 1.5px 1.5px 0 rgba(255, 255, 255, 0.8),
        inset 0 -1.5px 2px 0 rgba(0, 0, 0, 0.08);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .dribbble-glass-card:hover {{
      transform: translateY(-5px);
      box-shadow: 
        0 40px 90px -15px rgba(0, 0, 0, 0.22),
        inset 0 0 0 1.5px {accent};
      border-color: {accent};
    }}

    .dribbble-3d-stage {{
      background: rgba(255, 255, 255, 0.18);
      backdrop-filter: blur(24px) saturate(200%);
      -webkit-backdrop-filter: blur(24px) saturate(200%);
      border: 2px solid rgba(255, 255, 255, 0.6);
      border-radius: 36px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.12), inset 0 2px 3px rgba(255, 255, 255, 0.9);
      cursor: grab;
      position: relative;
      overflow: hidden;
    }}
    .dribbble-3d-stage:active {{
      cursor: grabbing;
    }}
  </style>
</head>
<body class="p-6 md:p-12">

  <div class="dribbble-blob-1"></div>
  <div class="dribbble-blob-2"></div>

  <div class="max-w-7xl mx-auto relative z-10">
    
    <!-- TOP BAR -->
    <header class="flex justify-between items-center pb-8 border-b border-black/10 mb-12">
      <div class="flex items-center space-x-4">
        <a href="index.html" class="text-xs font-mono font-black px-4 py-2.5 rounded-2xl bg-white/40 backdrop-blur-md border border-white/70 shadow hover:bg-black hover:text-white transition">
          &larr; 50-Prototype Master Hub
        </a>
        <div class="text-4xl font-black font-title tracking-tighter">qnt.</div>
      </div>
      <div class="px-4 py-2 rounded-2xl bg-white/40 backdrop-blur-md border border-white/70 text-xs font-mono font-black shadow-sm">
        {tag} #{id:02d}
      </div>
    </header>

    <!-- HERO & 3D INTERACTIVE STAGE -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center mb-16">
      
      <div class="lg:col-span-7">
        <div class="inline-block bg-white/50 backdrop-blur-md border border-white/80 text-xs font-mono font-black px-4 py-1.5 rounded-full mb-4 shadow-sm">
          DRIBBLE INSPIRATION • {tag}
        </div>
        <h1 class="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight mb-4 leading-[1.05]">
          {arch_type}
        </h1>
        <p class="text-sm md:text-base font-medium leading-relaxed opacity-85 mb-8 max-w-xl">
          {desc}
        </p>
        <div class="flex gap-4">
          <a href="#tool" class="bg-black text-white font-mono font-black text-xs px-7 py-4 rounded-2xl border-2 border-black shadow-xl hover:bg-white hover:text-black transition">
            Test Analytical Tool &rarr;
          </a>
        </div>
      </div>

      <!-- 3D DRIBBLE STAGE CONTAINER -->
      <div class="lg:col-span-5 h-[400px] sm:h-[460px] dribbble-3d-stage shadow-2xl flex flex-col justify-between p-5">
        <div class="flex justify-between items-center z-10">
          <span class="text-[10px] font-mono font-black bg-black text-white px-3 py-1 rounded-xl">DRIBBLE 3D WEAPON</span>
          <span class="text-[10px] font-mono font-bold text-slate-800 bg-white/70 backdrop-blur-md px-2.5 py-1 rounded-xl border border-white">🖱️ Drag to Spin in 3D</span>
        </div>
        
        <canvas id="canvas3d" class="w-full h-full absolute inset-0 z-0"></canvas>

        <div class="text-[10px] font-mono font-bold text-slate-800 bg-white/70 backdrop-blur-md p-3 rounded-2xl z-10 text-center border border-white">
          Transmission: 0.95 • IOR: 1.52 • Chromatic Iridescence Shader
        </div>
      </div>

    </div>

    <!-- BESPOKE LIQUID GLASS ANALYTICAL TOOL -->
    <div id="tool" class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
      
      <div class="dribbble-glass-card p-8 sm:p-10 lg:col-span-2">
        <div class="flex justify-between items-start mb-4">
          <div>
            <span class="text-xs font-mono font-black uppercase text-slate-500">BESPOKE ANALYTICAL ENGINE</span>
            <h3 class="text-2xl sm:text-3xl font-black mt-1">Deterministic Wealth Architecture</h3>
          </div>
          <span class="text-xs font-mono font-black bg-white/60 border border-black/10 px-3 py-1 rounded-xl">LIVE TELEMETRY</span>
        </div>
        <p class="text-xs sm:text-sm leading-relaxed mb-8 font-medium opacity-85">
          Synchronizing 200 sovereign instruments, multi-factor momentum, commercial real assets, and automated cashflow harvesting into an institutional standard.
        </p>
        
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 font-mono text-xs pt-6 border-t border-black/10">
          <div class="p-5 rounded-2xl bg-white/50 backdrop-blur-md border border-white/70 shadow-sm">
            <div class="text-[10px] text-slate-500 font-bold uppercase">STATUTORY TAX MOAT</div>
            <div class="text-xl font-black mt-1">100% Tax-Free</div>
            <div class="text-[10px] text-emerald-700 font-bold mt-1">Section 10(11A) / 47(viic)</div>
          </div>
          <div class="p-5 rounded-2xl bg-white/50 backdrop-blur-md border border-white/70 shadow-sm">
            <div class="text-[10px] text-slate-500 font-bold uppercase">ROLLING ALPHA CAGR</div>
            <div class="text-xl font-black mt-1">15.4% – 28.4%</div>
            <div class="text-[10px] text-cyan-700 font-bold mt-1">Systematic Multi-Asset</div>
          </div>
          <div class="p-5 rounded-2xl bg-white/50 backdrop-blur-md border border-white/70 shadow-sm">
            <div class="text-[10px] text-slate-500 font-bold uppercase">LEGAL SECURITY</div>
            <div class="text-xl font-black mt-1">Court Immunity</div>
            <div class="text-[10px] text-purple-700 font-bold mt-1">Section 14 PPF Act Moat</div>
          </div>
        </div>
      </div>

      <div class="dribbble-glass-card p-8 sm:p-10 flex flex-col justify-between">
        <div>
          <span class="text-xs font-mono font-black uppercase text-slate-500">INSTITUTIONAL MONOGRAPH</span>
          <h3 class="text-2xl font-black mt-1 mb-3">282-Page Master Codex</h3>
          <p class="text-xs leading-relaxed opacity-85 mb-6 font-medium">
            The authoritative mathematical monograph spanning all 200 sovereign asset modules and 6 factor desks.
          </p>
        </div>
        <a href="reports/qnt_Universal_Financial_Freedom_Institutional_Compendium.pdf" download class="w-full text-center bg-black text-white font-mono font-black text-xs py-4 rounded-2xl border-2 border-black shadow-lg hover:bg-white hover:text-black transition block">
          Download Monograph PDF &rarr;
        </a>
      </div>

    </div>

  </div>

  <script>
    let scene, camera, renderer, mesh, animateHook = null;
    let isDragging = false, previousMousePosition = {{ x: 0, y: 0 }};

    function init3D() {{
      const container = document.querySelector('.dribbble-3d-stage');
      const canvas = document.getElementById('canvas3d');
      const width = container.clientWidth;
      const height = container.clientHeight;

      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
      camera.position.z = 12;

      renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true, powerPreference: "high-performance" }});
      renderer.setSize(width, height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      // STUDIO LIGHTING
      const amb = new THREE.AmbientLight(0xffffff, 1.8);
      scene.add(amb);
      const dir = new THREE.DirectionalLight(0xffffff, 2.5);
      dir.position.set(10, 15, 12);
      scene.add(dir);
      const pt1 = new THREE.PointLight(0x06B6D4, 3.0, 30);
      pt1.position.set(-8, -4, 8);
      scene.add(pt1);
      const pt2 = new THREE.PointLight(0xF59E0B, 2.5, 30);
      pt2.position.set(8, -6, 6);
      scene.add(pt2);

      {three_code}

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

for i in range(1, 51):
    arch = archetypes[(i - 1) % len(archetypes)]
    pal = palettes[(i - 1) % len(palettes)]
    content = html_template.format(
        id=i,
        arch_type=arch["type"],
        tag=arch["tag"],
        desc=arch["desc"],
        bg=pal["bg"],
        card_glass=pal["card_glass"],
        card_border=pal["card_border"],
        text=pal["text"],
        accent=pal["accent"],
        font_h=pal["font_h"],
        font_b=pal["font_b"],
        font_url=pal["font_url"],
        three_code=arch["three_code"]
    )
    path = f"/data/project_qnt_netlify/proto{i}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated all 50 Dribbble-grade 3D liquid glass suites successfully!")
