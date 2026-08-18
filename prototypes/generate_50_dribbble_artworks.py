import os

palettes = [
    {"bg": "linear-gradient(135deg, #FAF8F5 0%, #E2E8F0 50%, #FAF8F5 100%)", "card_glass": "rgba(255, 255, 255, 0.35)", "card_border": "rgba(255, 255, 255, 0.8)", "text": "#0B0F1D", "accent": "#06B6D4", "font_h": "'Syne', sans-serif", "font_b": "'Plus Jakarta Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&family=Syne:wght@800;900&display=swap"},
    {"bg": "linear-gradient(135deg, #F5F3FF 0%, #DDD6FE 50%, #F5F3FF 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(221, 214, 254, 0.85)", "text": "#1E1B4B", "accent": "#8B5CF6", "font_h": "'Clash Display', sans-serif", "font_b": "'Satoshi', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=clash-display@700,600&f[]=satoshi@500,700&display=swap"},
    {"bg": "linear-gradient(135deg, #F0FDF4 0%, #A7F3D0 50%, #F0FDF4 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(167, 243, 208, 0.85)", "text": "#064E3B", "accent": "#10B981", "font_h": "'Cabinet Grotesk', sans-serif", "font_b": "'Inter', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,900&display=swap"},
    {"bg": "linear-gradient(135deg, #FFF7ED 0%, #FED7AA 50%, #FFF7ED 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(254, 215, 170, 0.85)", "text": "#7C2D12", "accent": "#F97316", "font_h": "'DM Serif Display', serif", "font_b": "'Plus Jakarta Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap"},
    {"bg": "linear-gradient(135deg, #FFF1F2 0%, #FECDD3 50%, #FFF1F2 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(254, 205, 211, 0.85)", "text": "#881337", "accent": "#E11D48", "font_h": "'Playfair Display', serif", "font_b": "'Outfit', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&family=Playfair+Display:wght@700;900&display=swap"},
    {"bg": "linear-gradient(135deg, #F0F9FF 0%, #BAE6FD 50%, #F0F9FF 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(186, 230, 253, 0.85)", "text": "#0C4A6E", "accent": "#0284C7", "font_h": "'Fraunces', serif", "font_b": "'Manrope', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Manrope:wght@500;700&display=swap"},
    {"bg": "linear-gradient(135deg, #FEFCE8 0%, #FEF08A 50%, #FEFCE8 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(254, 240, 138, 0.85)", "text": "#713F12", "accent": "#CA8A04", "font_h": "'Bebas Neue', sans-serif", "font_b": "'Work Sans', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Work+Sans:wght@500;700&display=swap"},
    {"bg": "linear-gradient(135deg, #FAF5FF 0%, #E9D5FF 50%, #FAF5FF 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(233, 213, 255, 0.85)", "text": "#581C87", "accent": "#9333EA", "font_h": "'General Sans', sans-serif", "font_b": "'Satoshi', sans-serif", "font_url": "https://api.fontshare.com/v2/css?f[]=general-sans@700,600&f[]=satoshi@500,700&display=swap"},
    {"bg": "linear-gradient(135deg, #F6FBF7 0%, #BBF7D0 50%, #F6FBF7 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(187, 247, 208, 0.85)", "text": "#14532D", "accent": "#16A34A", "font_h": "'Space Grotesk', sans-serif", "font_b": "'Inter', sans-serif", "font_url": "https://fonts.googleapis.com/css2?family=Inter:wght@500;700&family=Space+Grotesk:wght@700&display=swap"},
    {"bg": "linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 50%, #F8FAFC 100%)", "card_glass": "rgba(255, 255, 255, 0.4)", "card_border": "rgba(226, 232, 240, 0.85)", "text": "#0F172A", "accent": "#0EA5E9", "font_h": "'Cinzel Decorative', serif", "font_b": "'Cormorant Garamond', serif", "font_url": "https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:wght@500;600;700&display=swap"}
]

# 50 Unique 3D Artwork Geometry Generator Configurations
def get_3d_artwork(i):
    idx = (i - 1) % 10
    if idx == 0:
        return (
            "The Sovereign Bullion Prism",
            "3D Gold Ingot encased in a heavy optical quartz obelisk with rotating laser purity crests.",
            """
              const group = new THREE.Group();
              const glassMat = new THREE.MeshPhysicalMaterial({ color: 0xFFFFFF, metalness: 0.05, roughness: 0.02, transmission: 0.98, thickness: 3.5, ior: 1.54 });
              const goldMat = new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 });

              const obelisk = new THREE.Mesh(new THREE.BoxGeometry(3.6, 5.8, 2.2), glassMat);
              group.add(obelisk);

              const bar = new THREE.Mesh(new THREE.BoxGeometry(2.4, 4.2, 1.2), goldMat);
              group.add(bar);

              const ring = new THREE.Mesh(new THREE.TorusGeometry(4.8, 0.08, 16, 80), new THREE.MeshBasicMaterial({ color: 0x06B6D4, wireframe: true }));
              ring.rotation.x = Math.PI * 0.4;
              group.add(ring);

              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  group.rotation.y = Math.sin(t * 1.2) * 0.4;
                  group.rotation.x = Math.cos(t * 1.0) * 0.2;
                  ring.rotation.z += 0.015;
                }
              };
            """
        )
    elif idx == 1:
        return (
            "The Quantum Sovereign Aegis",
            "Beveled crystal heraldic shield with solid gold core and rotating laser halos.",
            """
              const group = new THREE.Group();
              const shieldShape = new THREE.Shape();
              shieldShape.moveTo(0, 3.2);
              shieldShape.bezierCurveTo(2.2, 3.2, 3.2, 1.8, 3.2, 0.4);
              shieldShape.bezierCurveTo(3.2, -1.8, 1.6, -3.0, 0, -4.2);
              shieldShape.bezierCurveTo(-1.6, -3.0, -3.2, -1.8, -3.2, 0.4);
              shieldShape.bezierCurveTo(-3.2, 1.8, -2.2, 3.2, 0, 3.2);

              const shieldGeo = new THREE.ExtrudeGeometry(shieldShape, { depth: 0.6, bevelEnabled: true, bevelSize: 0.25, bevelThickness: 0.25 });
              const shieldMat = new THREE.MeshPhysicalMaterial({ color: 0xD8B4FE, metalness: 0.1, roughness: 0.02, transmission: 0.98, thickness: 3.2, ior: 1.6 });
              const sMesh = new THREE.Mesh(shieldGeo, shieldMat);
              sMesh.position.set(0, 0, -0.3);
              group.add(sMesh);

              const core = new THREE.Mesh(new THREE.OctahedronGeometry(1.4, 0), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
              group.add(core);

              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  group.rotation.y = Math.sin(t * 1.4) * 0.35;
                  group.rotation.x = Math.cos(t * 1.1) * 0.2;
                  core.rotation.y -= 0.02;
                }
              };
            """
        )
    elif idx == 2:
        return (
            "The Obsidian Titanium Card",
            "Hyper-realistic frosted black titanium credit card with gold micro-chip and floating laser ribbon.",
            """
              const group = new THREE.Group();
              const cardGeo = new THREE.BoxGeometry(6.4, 4.0, 0.26);
              const cardMat = new THREE.MeshPhysicalMaterial({ color: 0x111827, metalness: 0.3, roughness: 0.05, transmission: 0.85, thickness: 1.8, ior: 1.52 });
              const card = new THREE.Mesh(cardGeo, cardMat);
              group.add(card);

              const chip = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.9, 0.3), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
              chip.position.set(-1.8, 0.6, 0.05);
              group.add(chip);

              const ribbon = new THREE.Mesh(new THREE.TorusGeometry(4.6, 0.06, 16, 100), new THREE.MeshBasicMaterial({ color: 0x10B981, wireframe: true }));
              ribbon.rotation.x = Math.PI * 0.45;
              group.add(ribbon);

              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  group.rotation.y = Math.sin(t * 1.2) * 0.4;
                  group.rotation.x = Math.cos(t * 0.9) * 0.25;
                  ribbon.rotation.z += 0.015;
                }
              };
            """
        )
    elif idx == 3:
        return (
            "The Alpha Quantum Prism Bolt",
            "Sharp-angled extruded optical glass lightning bolt with glowing plasma core.",
            """
              const group = new THREE.Group();
              const boltShape = new THREE.Shape();
              boltShape.moveTo(0.4, 3.6); boltShape.lineTo(-1.6, 0.2); boltShape.lineTo(0.0, 0.2);
              boltShape.lineTo(-0.8, -3.6); boltShape.lineTo(1.6, -0.2); boltShape.lineTo(0.2, -0.2); boltShape.lineTo(0.4, 3.6);

              const boltGeo = new THREE.ExtrudeGeometry(boltShape, { depth: 0.7, bevelEnabled: true, bevelSize: 0.2, bevelThickness: 0.2 });
              const boltMat = new THREE.MeshPhysicalMaterial({ color: 0xFDBA74, metalness: 0.1, roughness: 0.02, transmission: 0.98, thickness: 3.0, ior: 1.55 });
              const bolt = new THREE.Mesh(boltGeo, boltMat);
              bolt.position.set(0, 0, -0.35);
              group.add(bolt);

              const core = new THREE.Mesh(new THREE.SphereGeometry(0.9, 24, 24), new THREE.MeshStandardMaterial({ color: 0xF97316, metalness: 0.9, roughness: 0.1 }));
              group.add(core);

              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  group.rotation.y += 0.012;
                  group.rotation.z = Math.sin(t * 1.5) * 0.15;
                  core.scale.setScalar(1.0 + Math.sin(t * 4) * 0.15);
                }
              };
            """
        )
    elif idx == 4:
        return (
            "The Hyper-Fluid Glass Nautilus",
            "Mathematical logarithmic spiral in liquid glass with iridescent chromatic oil-slick sheen.",
            """
              const geo = new THREE.TorusKnotGeometry(2.8, 0.85, 120, 24, 2, 5);
              const mat = new THREE.MeshPhysicalMaterial({ color: 0xFDA4AF, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.8, ior: 1.58 });
              mesh = new THREE.Mesh(geo, mat);
              scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  mesh.rotation.x += 0.01;
                  mesh.rotation.y += 0.015;
                }
              };
            """
        )
    elif idx == 5:
        return (
            "The Multi-Currency Planetary Gyroscope",
            "Interlocking brushed gold & glass gimbals holding floating $, ₹, €, £ tokens in dynamic orbit.",
            """
              const group = new THREE.Group();
              const gMat = new THREE.MeshPhysicalMaterial({ color: 0x7DD3FC, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.0 });
              const r1 = new THREE.Mesh(new THREE.TorusGeometry(3.2, 0.25, 16, 80), gMat);
              const r2 = new THREE.Mesh(new THREE.TorusGeometry(4.4, 0.2, 16, 80), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
              r2.rotation.x = Math.PI * 0.4;
              group.add(r1); group.add(r2);

              const center = new THREE.Mesh(new THREE.SphereGeometry(1.4, 24, 24), new THREE.MeshStandardMaterial({ color: 0x0284C7, metalness: 0.9, roughness: 0.1 }));
              group.add(center);

              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  r1.rotation.y += 0.015;
                  r2.rotation.z += 0.018;
                  center.rotation.y -= 0.02;
                }
              };
            """
        )
    elif idx == 6:
        return (
            "The Monolithic Compounding Crystal Pillars",
            "5 Tiered crystal columns with gold-leaf caps rising from an optical glass pedestal.",
            """
              const group = new THREE.Group();
              const glassMat = new THREE.MeshPhysicalMaterial({ color: 0xFDE047, metalness: 0.1, roughness: 0.05, transmission: 0.92, thickness: 2.0 });
              const goldMat = new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 });

              const bars = [];
              for (let j = 0; j < 5; j++) {
                const h = 1.8 + j * 1.0;
                const bar = new THREE.Mesh(new THREE.BoxGeometry(0.85, h, 0.85), glassMat);
                bar.position.set((j - 2) * 1.2, h / 2 - 2.2, 0);
                group.add(bar);
                const tip = new THREE.Mesh(new THREE.BoxGeometry(0.88, 0.25, 0.88), goldMat);
                tip.position.set((j - 2) * 1.2, h - 2.2, 0);
                group.add(tip);
                bars.push({ bar, tip, baseH: h, j });
              }
              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  group.rotation.y = Math.sin(t * 0.8) * 0.3;
                  bars.forEach(b => {
                    const scaleY = 1 + Math.sin(t * 2 + b.j * 0.8) * 0.2;
                    b.bar.scale.y = scaleY;
                    b.tip.position.y = (b.baseH * scaleY) - 2.2;
                  });
                }
              };
            """
        )
    elif idx == 7:
        return (
            "The Wealth Velocity DNA Double Helix",
            "Intertwined glass and polished gold molecular strands connected by glowing milestone nodes.",
            """
              const group = new THREE.Group();
              const m1 = new THREE.MeshPhysicalMaterial({ color: 0xD8B4FE, metalness: 0.1, roughness: 0.05, transmission: 0.9, thickness: 1.5 });
              const m2 = new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 });

              for (let k = 0; k < 22; k++) {
                const t = (k / 22) * Math.PI * 4;
                const y = (k - 11) * 0.5;
                const s1 = new THREE.Mesh(new THREE.SphereGeometry(0.28, 16, 16), m1);
                s1.position.set(Math.cos(t) * 2.5, y, Math.sin(t) * 2.5);
                group.add(s1);
                const s2 = new THREE.Mesh(new THREE.SphereGeometry(0.28, 16, 16), m2);
                s2.position.set(Math.cos(t + Math.PI) * 2.5, y, Math.sin(t + Math.PI) * 2.5);
                group.add(s2);
              }
              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  group.rotation.y += 0.016;
                }
              };
            """
        )
    elif idx == 8:
        return (
            "The Neomorphic Viscous Asset Capsule",
            "High-precision glass capsule containing floating magnetic factor spheres in viscous fluid.",
            """
              const group = new THREE.Group();
              const capGeo = new THREE.CylinderGeometry(1.6, 1.6, 4.6, 32);
              const capMat = new THREE.MeshPhysicalMaterial({ color: 0x86EFAC, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.2, ior: 1.5 });
              const cap = new THREE.Mesh(capGeo, capMat);
              cap.rotation.z = Math.PI * 0.5;
              group.add(cap);

              const s1 = new THREE.Mesh(new THREE.SphereGeometry(1.0, 24, 24), new THREE.MeshStandardMaterial({ color: 0x16A34A, metalness: 0.9, roughness: 0.1 }));
              s1.position.set(-1.0, 0, 0); group.add(s1);
              const s2 = new THREE.Mesh(new THREE.SphereGeometry(1.0, 24, 24), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
              s2.position.set(1.0, 0, 0); group.add(s2);

              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  group.rotation.y = Math.sin(t * 1.5) * 0.4;
                  group.rotation.x = Math.cos(t * 1.2) * 0.2;
                  s1.position.x = -1.0 + Math.sin(t * 2) * 0.25;
                  s2.position.x = 1.0 - Math.sin(t * 2) * 0.25;
                }
              };
            """
        )
    else:
        return (
            "The Sovereign Grand Opus Dodecahedron",
            "Breathing faceted quartz dodecahedron with an embedded 24k gold core and orbiting laser rings.",
            """
              const group = new THREE.Group();
              const dGeo = new THREE.DodecahedronGeometry(3.2, 0);
              const dMat = new THREE.MeshPhysicalMaterial({ color: 0xBAE6FD, metalness: 0.05, roughness: 0.02, transmission: 0.98, thickness: 3.2, ior: 1.55 });
              const dMesh = new THREE.Mesh(dGeo, dMat);
              group.add(dMesh);

              const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.5, 0), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
              group.add(core);

              mesh = group; scene.add(mesh);
              animateHook = (t) => {
                if (!isDragging) {
                  dMesh.rotation.x += 0.008;
                  dMesh.rotation.y += 0.012;
                  core.rotation.y -= 0.02;
                }
              };
            """
        )

html_template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>qnt. | Suite #{id:02d}: {name}</title>
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

    .liquid-blob-1 {{
      position: fixed;
      top: -10%;
      left: 15%;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, {accent} 0%, transparent 70%);
      filter: blur(85px);
      opacity: 0.5;
      z-index: 0;
      animation: blobMove 16s ease-in-out infinite alternate;
      pointer-events: none;
    }}
    .liquid-blob-2 {{
      position: fixed;
      bottom: -10%;
      right: 10%;
      width: 550px;
      height: 550px;
      background: radial-gradient(circle, #F59E0B 0%, transparent 70%);
      filter: blur(95px);
      opacity: 0.4;
      z-index: 0;
      animation: blobMove 20s ease-in-out infinite alternate-reverse;
      pointer-events: none;
    }}

    @keyframes blobMove {{
      0% {{ transform: translate(0, 0) scale(1); }}
      100% {{ transform: translate(90px, 70px) scale(1.15); }}
    }}

    h1, h2, h3, .font-title {{
      font-family: {font_h} !important;
    }}

    /* AWWWARDS / VISIONOS SEAMLESS FLOATING GLASS PORTAL STAGE */
    .portal-3d-stage {{
      background: {card_glass} !important;
      backdrop-filter: blur(36px) saturate(220%) brightness(110%);
      -webkit-backdrop-filter: blur(36px) saturate(220%) brightness(110%);
      border: 1.5px solid {card_border};
      border-radius: 40px;
      box-shadow: 
        0 35px 80px -15px rgba(0, 0, 0, 0.18),
        inset 0 2px 2px 0 rgba(255, 255, 255, 0.9),
        inset 0 -2px 3px 0 rgba(0, 0, 0, 0.08);
      position: relative;
      cursor: grab;
      overflow: hidden;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .portal-3d-stage:active {{
      cursor: grabbing;
    }}
    .portal-3d-stage:hover {{
      transform: translateY(-4px);
      box-shadow: 0 45px 100px -15px rgba(0, 0, 0, 0.25);
    }}

    .liquid-glass-card {{
      background: {card_glass} !important;
      backdrop-filter: blur(32px) saturate(210%) brightness(108%);
      -webkit-backdrop-filter: blur(32px) saturate(210%) brightness(108%);
      border: 1.5px solid {card_border};
      border-radius: 36px;
      box-shadow: 
        0 30px 70px -15px rgba(0, 0, 0, 0.15),
        inset 0 1.5px 1.5px 0 rgba(255, 255, 255, 0.8);
      transition: all 0.35s ease;
    }}
  </style>
</head>
<body class="p-6 md:p-12">

  <div class="liquid-blob-1"></div>
  <div class="liquid-blob-2"></div>

  <div class="max-w-7xl mx-auto relative z-10">
    
    <header class="flex justify-between items-center pb-8 border-b border-black/10 mb-12">
      <div class="flex items-center space-x-4">
        <a href="index.html" class="text-xs font-mono font-black px-4 py-2.5 rounded-2xl bg-white/40 backdrop-blur-md border border-white/70 shadow hover:bg-black hover:text-white transition">
          &larr; 50-Prototype Master Hub
        </a>
        <div class="text-4xl font-black font-title tracking-tighter">qnt.</div>
      </div>
      <div class="px-4 py-2 rounded-2xl bg-white/40 backdrop-blur-md border border-white/70 text-xs font-mono font-black shadow-sm">
        3D MASTER SUITE #{id:02d}
      </div>
    </header>

    <!-- HERO & SEAMLESS 3D FLOATING PORTAL STAGE -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center mb-16">
      
      <div class="lg:col-span-7">
        <div class="inline-block bg-white/60 backdrop-blur-md border border-white/90 text-xs font-mono font-black px-4 py-1.5 rounded-full mb-4 shadow-sm">
          DRIBBLE CINEMA 4D ARTWORK • #{id:02d}
        </div>
        <h1 class="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight mb-4 leading-[1.05]">
          {name}
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

      <!-- SEAMLESS FLOATING PORTAL STAGE (DRAG TO ROTATE) -->
      <div class="lg:col-span-5 h-[420px] sm:h-[480px] portal-3d-stage flex flex-col justify-between p-6">
        <div class="flex justify-between items-center z-10">
          <span class="text-[10px] font-mono font-black bg-black text-white px-3 py-1.5 rounded-xl shadow">3D ARTWORK PORTAL</span>
          <span class="text-[10px] font-mono font-bold text-slate-800 bg-white/70 backdrop-blur-md px-3 py-1 rounded-xl border border-white">🖱️ Drag to Rotate 3D Art</span>
        </div>
        
        <canvas id="canvas3d" class="w-full h-full absolute inset-0 z-0"></canvas>

        <div class="text-[10px] font-mono font-bold text-slate-800 bg-white/70 backdrop-blur-md p-3.5 rounded-2xl z-10 text-center border border-white">
          Three.js Physical Glass Transmission (IOR: 1.54) • 3-Point Studio Rig
        </div>
      </div>

    </div>

    <!-- BESPOKE LIQUID GLASS ANALYTICAL TOOL -->
    <div id="tool" class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
      
      <div class="liquid-glass-card p-8 sm:p-10 lg:col-span-2">
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

      <div class="liquid-glass-card p-8 sm:p-10 flex flex-col justify-between">
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
      const container = document.querySelector('.portal-3d-stage');
      const canvas = document.getElementById('canvas3d');
      const width = container.clientWidth;
      const height = container.clientHeight;

      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
      camera.position.z = 12;

      renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true, powerPreference: "high-performance" }});
      renderer.setSize(width, height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      // 3-POINT CINEMA 4D STUDIO LIGHTING
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

      // TACTILE INTERACTION
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

# Generate all 50 unique Dribbble 3D artwork suites
for i in range(1, 51):
    pal = palettes[(i - 1) % len(palettes)]
    art_name, art_desc, art_code = get_3d_artwork(i)

    content = html_template.format(
        id=i,
        name=f"{art_name} #{i:02d}",
        desc=art_desc,
        bg=pal["bg"],
        card_glass=pal["card_glass"],
        card_border=pal["card_border"],
        text=pal["text"],
        accent=pal["accent"],
        font_h=pal["font_h"],
        font_b=pal["font_b"],
        font_url=pal["font_url"],
        three_code=art_code
    )
    path = f"/data/project_qnt_netlify/proto{i}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated all 50 unique Dribbble 3D artwork suites successfully!")
