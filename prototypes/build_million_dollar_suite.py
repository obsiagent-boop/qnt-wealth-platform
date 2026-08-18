import os

million_prototypes = [
    {
        "id": 1,
        "name": "The Sovereign Liquid Vault",
        "theme": "Frosted Liquid Quartz & Platinum Gold",
        "bg": "#FAF8F5",
        "glass_bg": "rgba(255, 255, 255, 0.45)",
        "glass_border": "rgba(255, 255, 255, 0.8)",
        "text": "#0B0F1D",
        "accent": "#06B6D4",
        "font_head": "'Syne', sans-serif",
        "font_body": "'Plus Jakarta Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Syne:wght@700;800;900&display=swap",
        "tagline": "3D Interactive Liquid Frosted Glass Sovereign Vault with Real-Time Drag Physics",
        "ux_pattern": "Bento Grid v3 + 200-Module Asset Terminal + Interactive 3D Currency Physics Widget",
        "tool_title": "Deterministic Geometric Compounding Engine",
        "tool_desc": "Simulating $A=P(1+r)^t$ geometric expansion with statutory triple-E tax immunity sweeps.",
        "badge": "LIQUID GLASS • SUITE 01",
        "three_code": """
          // 3D Glass Sovereign Coin in Dedicated Widget Box
          const coinGeo = new THREE.CylinderGeometry(3.2, 3.2, 0.5, 48);
          const glassMat = new THREE.MeshPhysicalMaterial({
            color: 0xFFFFFF,
            metalness: 0.1,
            roughness: 0.05,
            transmission: 0.95,
            thickness: 2.2,
            ior: 1.52,
            transparent: true,
            opacity: 0.9
          });
          const goldCoreMat = new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.15 });
          
          mesh = new THREE.Mesh(coinGeo, glassMat);
          mesh.rotation.x = Math.PI * 0.5;
          scene.add(mesh);
          
          const core = new THREE.Mesh(new THREE.TorusGeometry(1.6, 0.3, 16, 40), goldCoreMat);
          mesh.add(core);

          const halo = new THREE.Mesh(new THREE.TorusGeometry(4.2, 0.08, 16, 80), new THREE.MeshBasicMaterial({ color: 0x06B6D4, wireframe: true }));
          halo.rotation.x = Math.PI * 0.4;
          scene.add(halo);

          animateHook = (t) => {
            if (!isDragging) {
              mesh.rotation.y += 0.012;
              mesh.rotation.x = Math.PI * 0.5 + Math.sin(t * 1.5) * 0.15;
            }
            halo.rotation.z += 0.01;
          };
        """
    },
    {
        "id": 2,
        "name": "Prismatic Crystal Matrix",
        "theme": "Pastel Lavender & Refractive Glass",
        "bg": "#F5F3FF",
        "glass_bg": "rgba(255, 255, 255, 0.5)",
        "glass_border": "rgba(221, 214, 254, 0.8)",
        "text": "#1E1B4B",
        "accent": "#8B5CF6",
        "font_head": "'Clash Display', sans-serif",
        "font_body": "'Satoshi', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=clash-display@700,600&f[]=satoshi@500,700&display=swap",
        "tagline": "3D Refractive Prismatic Glass Icosahedron with Internal Multi-Light Dispersion",
        "ux_pattern": "Spotlight Glass Cards + 10,000-Path Monte Carlo Probabilistic Fan Chart",
        "tool_title": "Monte Carlo Tail-Risk Decomposer",
        "tool_desc": "Probabilistic 99% VaR stress testing isolating sovereign fixed alpha from equity drawdowns.",
        "badge": "LIQUID GLASS • SUITE 02",
        "three_code": """
          const geo = new THREE.IcosahedronGeometry(3.5, 0);
          const mat = new THREE.MeshPhysicalMaterial({
            color: 0xC4B5FD,
            metalness: 0.05,
            roughness: 0.02,
            transmission: 0.98,
            thickness: 3.5,
            ior: 1.65,
            transparent: true,
            opacity: 0.95
          });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);

          const core = new THREE.Mesh(new THREE.OctahedronGeometry(1.6, 0), new THREE.MeshStandardMaterial({ color: 0x8B5CF6, metalness: 0.9, roughness: 0.1 }));
          scene.add(core);

          animateHook = (t) => {
            if (!isDragging) {
              mesh.rotation.x += 0.008;
              mesh.rotation.y += 0.014;
              core.rotation.y -= 0.02;
            }
          };
        """
    },
    {
        "id": 3,
        "name": "Cybernetic Orthogonal Flow",
        "theme": "Pastel Mint & Liquid Glass Torus",
        "bg": "#F0FDF4",
        "glass_bg": "rgba(255, 255, 255, 0.5)",
        "glass_border": "rgba(167, 243, 208, 0.8)",
        "text": "#064E3B",
        "accent": "#10B981",
        "font_head": "'Cabinet Grotesk', sans-serif",
        "font_body": "'Inter', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,900&display=swap",
        "tagline": "Topological (2,5) Glass Torus Knot in Continuous Hydrodynamic Refraction",
        "ux_pattern": "Interactive Cross-Asset Factor Correlation Heatmap with Live Drift Triggers",
        "tool_title": "Factor Orthogonalization Matrix",
        "tool_desc": "Proving 0.00 correlation between sovereign bucket moats and domestic equity beta.",
        "badge": "LIQUID GLASS • SUITE 03",
        "three_code": """
          const geo = new THREE.TorusKnotGeometry(2.8, 0.85, 120, 24, 2, 5);
          const mat = new THREE.MeshPhysicalMaterial({
            color: 0x6EE7B7,
            metalness: 0.1,
            roughness: 0.05,
            transmission: 0.92,
            thickness: 2.5,
            ior: 1.45,
            transparent: true,
            opacity: 0.9
          });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              mesh.rotation.x += 0.01;
              mesh.rotation.y += 0.015;
            }
          };
        """
    },
    {
        "id": 4,
        "name": "Global Macro Barbell Stage",
        "theme": "Pastel Peach & Glass Satellites",
        "bg": "#FFF7ED",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "glass_border": "rgba(254, 215, 170, 0.8)",
        "text": "#7C2D12",
        "accent": "#F97316",
        "font_head": "'DM Serif Display', serif",
        "font_body": "'Plus Jakarta Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap",
        "tagline": "4 Liquid Glass Planetary Currency Spheres ($ / ₹ / £ / €) Orbiting in 3D Space",
        "ux_pattern": "Global Macro Yield Spread Visualizer + 10Y Sovereign G-Sec Arbitrage Telemetry",
        "tool_title": "Structural USD/INR Currency Alpha Arbitrage",
        "tool_desc": "Capturing 3.20% annual historical rupee depreciation as automated equity tailwinds.",
        "badge": "LIQUID GLASS • SUITE 04",
        "three_code": """
          const group = new THREE.Group();
          const core = new THREE.Mesh(new THREE.SphereGeometry(1.8, 32, 32), new THREE.MeshPhysicalMaterial({ color: 0xFDBA74, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.0 }));
          group.add(core);

          const colors = [0xF97316, 0x10B981, 0x06B6D4, 0x8B5CF6];
          const sats = [];
          for (let i = 0; i < 4; i++) {
            const s = new THREE.Mesh(new THREE.SphereGeometry(0.9, 24, 24), new THREE.MeshStandardMaterial({ color: colors[i], metalness: 0.85, roughness: 0.2 }));
            group.add(s);
            sats.push({ mesh: s, angle: (i / 4) * Math.PI * 2, dist: 4.8 });
          }
          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              core.rotation.y += 0.015;
              sats.forEach(s => {
                s.angle += 0.018;
                s.mesh.position.x = Math.cos(s.angle) * s.dist;
                s.mesh.position.y = Math.sin(s.angle) * (s.dist * 0.4);
                s.mesh.position.z = Math.sin(s.angle) * (s.dist * 0.8);
              });
            }
          };
        """
    },
    {
        "id": 5,
        "name": "Geometric Capital Helix",
        "theme": "Pastel Coral & Glass DNA Ladder",
        "bg": "#FFF1F2",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "glass_border": "rgba(254, 205, 211, 0.8)",
        "text": "#881337",
        "accent": "#E11D48",
        "font_head": "'Playfair Display', serif",
        "font_body": "'Outfit', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&family=Playfair+Display:wght@700;900&display=swap",
        "tagline": "3D Double-Helix Liquid Glass Nodes Compounding Upward in Real Time",
        "ux_pattern": "15-Year Life Cycle Milestone Roadmap (Bedrock ➔ Acceleration ➔ Perpetual Sweep)",
        "tool_title": "15-Year Capital Velocity Ladder",
        "tool_desc": "Exact milestones transitioning active labor income to ₹5,00,000/mo perpetual passive sweep.",
        "badge": "LIQUID GLASS • SUITE 05",
        "three_code": """
          const group = new THREE.Group();
          const gMat = new THREE.MeshPhysicalMaterial({ color: 0xF43F5E, metalness: 0.1, roughness: 0.05, transmission: 0.9, thickness: 1.5 });
          const rMat = new THREE.MeshStandardMaterial({ color: 0xFB7185, metalness: 0.9, roughness: 0.2 });

          for (let i = 0; i < 24; i++) {
            const t = (i / 24) * Math.PI * 4;
            const y = (i - 12) * 0.55;
            const s1 = new THREE.Mesh(new THREE.SphereGeometry(0.3, 16, 16), gMat);
            s1.position.set(Math.cos(t) * 2.8, y, Math.sin(t) * 2.8);
            group.add(s1);
            const s2 = new THREE.Mesh(new THREE.SphereGeometry(0.3, 16, 16), rMat);
            s2.position.set(Math.cos(t + Math.PI) * 2.8, y, Math.sin(t + Math.PI) * 2.8);
            group.add(s2);
          }
          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              group.rotation.y += 0.018;
            }
          };
        """
    },
    {
        "id": 6,
        "name": "Harmonic Liquid Nebula",
        "theme": "Pastel Sky & Liquid Mercury Glass",
        "bg": "#F0F9FF",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "glass_border": "rgba(186, 230, 253, 0.8)",
        "text": "#0C4A6E",
        "accent": "#0284C7",
        "font_head": "'Fraunces', serif",
        "font_body": "'Manrope', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Manrope:wght@500;700&display=swap",
        "tagline": "Liquid Mercury Glass Droplet with Interactive Oscillating Vertex Shaders",
        "ux_pattern": "Sovereign Annuity Cashflow Cascade with Automated Quarterly ECS Sweep Simulation",
        "tool_title": "Quarterly Liquidity Cascade Engine",
        "tool_desc": "Continuous yield sweeps across Grade-A REITs, SCSS & RBI 10Y Benchmark Gilts.",
        "badge": "LIQUID GLASS • SUITE 06",
        "three_code": """
          const geo = new THREE.IcosahedronGeometry(3.2, 32);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0x7DD3FC, metalness: 0.1, roughness: 0.02, transmission: 0.96, thickness: 3.0, ior: 1.5 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);

          const pos = geo.attributes.position;
          const orig = pos.clone();
          animateHook = (t) => {
            if (!isDragging) {
              for (let i = 0; i < pos.count; i++) {
                const u = orig.getX(i), v = orig.getY(i), w = orig.getZ(i);
                const dist = Math.sin(t * 3 + u * 2 + v * 2) * 0.3;
                pos.setXYZ(i, u + u * dist * 0.12, v + v * dist * 0.12, w + w * dist * 0.12);
              }
              pos.needsUpdate = true;
              mesh.rotation.y += 0.01;
            }
          };
        """
    },
    {
        "id": 7,
        "name": "Endless Mobius Continuum",
        "theme": "Pastel Butter & Liquid Glass Gold",
        "bg": "#FEFCE8",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "glass_border": "rgba(254, 240, 138, 0.8)",
        "text": "#713F12",
        "accent": "#CA8A04",
        "font_head": "'Bebas Neue', sans-serif",
        "font_body": "'Work Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Work+Sans:wght@500;700&display=swap",
        "tagline": "Endless 3D Liquid Glass Mobius Ribbon with Specular Refraction",
        "ux_pattern": "Fama-French 5-Factor Alpha Decomposer (SMB, HML, RMW, CMA, WML)",
        "tool_title": "Multi-Factor Alpha Decomposer",
        "tool_desc": "Deconstructing 24.0% CAGR systematic domestic outperformance into raw factor loadings.",
        "badge": "LIQUID GLASS • SUITE 07",
        "three_code": """
          const geo = new THREE.TorusGeometry(3.6, 0.9, 30, 150);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xFDE047, metalness: 0.1, roughness: 0.05, transmission: 0.94, thickness: 2.5, ior: 1.48 });
          mesh = new THREE.Mesh(geo, mat);
          mesh.rotation.x = Math.PI * 0.3;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              mesh.rotation.x += 0.012;
              mesh.rotation.y += 0.016;
            }
          };
        """
    },
    {
        "id": 8,
        "name": "Prismatic Quartz Pyramid",
        "theme": "Pastel Lilac & Glass Tetrahedron",
        "bg": "#FAF5FF",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "glass_border": "rgba(233, 213, 255, 0.8)",
        "text": "#581C87",
        "accent": "#9333EA",
        "font_head": "'General Sans', sans-serif",
        "font_body": "'Satoshi', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=general-sans@700,600&f[]=satoshi@500,700&display=swap",
        "tagline": "Multi-Faceted Glass Tetrahedron Refracting Light Rays with Dynamic Glare",
        "ux_pattern": "The 70:15:15 Institutional Asset Rebalancing Engine with Real-Time Drift Triggers",
        "tool_title": "Dynamic 70:15:15 Portfolio Rebalancer",
        "tool_desc": "Quarterly automated drift triggers enforcing disciplined asset-class allocations.",
        "badge": "LIQUID GLASS • SUITE 08",
        "three_code": """
          const geo = new THREE.TetrahedronGeometry(3.6, 0);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xD8B4FE, metalness: 0.1, roughness: 0.02, transmission: 0.95, thickness: 3.0, ior: 1.62 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              mesh.rotation.x += 0.01;
              mesh.rotation.y += 0.015;
            }
          };
        """
    },
    {
        "id": 9,
        "name": "Sovereign Legal Bastion",
        "theme": "Pastel Sage & Platinum Glass",
        "bg": "#F6FBF7",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "glass_border": "rgba(187, 247, 208, 0.8)",
        "text": "#14532D",
        "accent": "#16A34A",
        "font_head": "'Space Grotesk', sans-serif",
        "font_body": "'Inter', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Inter:wght@500;700&family=Space+Grotesk:wght@700&display=swap",
        "tagline": "Triple-Axis Mechanical Quantum Gyroscope in Frosted Liquid Glass & Platinum",
        "ux_pattern": "Section 14 Court Attachment Legal Immunity Shield Validator (PPF & SSY)",
        "tool_title": "Statutory Court Immunity & Insolvency Shield",
        "tool_desc": "Verifying 100% legal protection against debt attachment, civil decrees, and insolvency.",
        "badge": "LIQUID GLASS • SUITE 09",
        "three_code": """
          const group = new THREE.Group();
          const mat = new THREE.MeshPhysicalMaterial({ color: 0x86EFAC, metalness: 0.1, roughness: 0.05, transmission: 0.95, thickness: 2.0 });
          const r1 = new THREE.Mesh(new THREE.TorusGeometry(2.5, 0.18, 16, 80), mat);
          const r2 = new THREE.Mesh(new THREE.TorusGeometry(3.6, 0.18, 16, 80), mat);
          const r3 = new THREE.Mesh(new THREE.TorusGeometry(4.8, 0.18, 16, 80), mat);
          r2.rotation.x = Math.PI * 0.4; r3.rotation.y = Math.PI * 0.35;
          group.add(r1); group.add(r2); group.add(r3);
          mesh = group;
          scene.add(mesh);

          animateHook = (t) => {
            if (!isDragging) {
              r1.rotation.x += 0.02;
              r2.rotation.y += 0.015;
              r3.rotation.z += 0.01;
            }
          };
        """
    },
    {
        "id": 10,
        "name": "Master Universal Terminal",
        "theme": "Pastel Opal & 3D Glass Dodecahedron",
        "bg": "#FAF8F5",
        "glass_bg": "rgba(255, 255, 255, 0.55)",
        "glass_border": "rgba(0, 0, 0, 0.12)",
        "text": "#0F172A",
        "accent": "#06B6D4",
        "font_head": "'Syne', sans-serif",
        "font_body": "'Plus Jakarta Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&family=Syne:wght@800;900&display=swap",
        "tagline": "Breathing 3D Geometric Glass Dodecahedron with Multi-Light Specular Dispersion",
        "ux_pattern": "Unified Institutional Operating System Integrating all 6 Desks & 200 Asset Modules",
        "tool_title": "200-Module Master Quantitative Codex Engine",
        "tool_desc": "The definitive sovereign financial architecture for universal generational freedom.",
        "badge": "LIQUID GLASS • SUITE 10",
        "three_code": """
          const geo = new THREE.DodecahedronGeometry(3.4, 0);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xBAE6FD, metalness: 0.05, roughness: 0.02, transmission: 0.98, thickness: 3.2, ior: 1.55 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);

          const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.6, 0), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
          scene.add(core);

          animateHook = (t) => {
            if (!isDragging) {
              mesh.rotation.x += 0.008;
              mesh.rotation.y += 0.012;
              core.rotation.y -= 0.02;
            }
          };
        """
    }
]

template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>qnt. | {name}</title>
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
      font-family: {font_head} !important;
    }}
    
    /* TRUE LIQUID FROSTED GLASS EFFECT */
    .liquid-glass-panel {{
      background: {glass_bg} !important;
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border: 1.5px solid {glass_border};
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
      border: 2px solid {glass_border};
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
          &larr; Liquid Glass Lab Hub
        </a>
        <div class="text-4xl font-black font-title tracking-tighter">qnt.</div>
      </div>
      <div class="px-4 py-2.5 rounded-xl bg-white border-2 border-slate-900 text-xs font-mono font-black shadow-[3px_3px_0px_#000]">
        {badge}
      </div>
    </header>

    <!-- HERO & 3D INTERACTIVE GLASS STAGE SPLIT -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center mb-16">
      
      <!-- LEFT HERO CONTENT -->
      <div class="lg:col-span-7">
        <div class="inline-block bg-white border-2 border-slate-900 text-xs font-mono font-black px-4 py-1.5 rounded-full mb-4 shadow-[3px_3px_0px_#000]">
          {tagline}
        </div>
        <h1 class="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight mb-4 leading-[1.05]">
          {name}
        </h1>
        <p class="text-sm md:text-base font-medium leading-relaxed opacity-80 mb-8 max-w-xl">
          Architecture: <strong class="underline">{ux_pattern}</strong>. Physical glass transmission shaders running on Three.js WebGL with tactile drag &amp; inertial physics.
        </p>
        <div class="flex gap-4">
          <a href="#tool" class="bg-black text-white font-mono font-black text-xs px-6 py-4 rounded-2xl border-2 border-black shadow-[4px_4px_0px_{accent}] hover:bg-white hover:text-black transition">
            Test Analytical Tool &rarr;
          </a>
        </div>
      </div>

      <!-- RIGHT 3D LIQUID GLASS INTERACTIVE STAGE (DRAG & ROTATE DIRECTLY ON CANVAS) -->
      <div class="lg:col-span-5 h-[380px] sm:h-[440px] glass-canvas-container shadow-2xl overflow-hidden flex flex-col justify-between p-4">
        <div class="flex justify-between items-center z-10">
          <span class="text-[10px] font-mono font-black bg-black text-white px-2.5 py-1 rounded-lg">3D LIQUID GLASS OBJECT</span>
          <span class="text-[10px] font-mono font-bold text-slate-600 bg-white/80 px-2 py-0.5 rounded">🖱️ Drag to Rotate 3D Glass</span>
        </div>
        
        <canvas id="canvas3d" class="w-full h-full absolute inset-0 z-0"></canvas>

        <div class="text-[10px] font-mono font-bold text-slate-700 bg-white/80 p-2 rounded-xl z-10 text-center">
          Material: Transmission Glass (IOR: 1.52) • Sub-surface Refraction
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

      {three_code}

      // DIRECT 3D MOUSE & TOUCH INTERACTION ON THE GLASS CONTAINER
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

# Regenerate all 10 prototypes with direct liquid glass canvas stage and drag physics
for p in million_prototypes:
    content = template.format(
        id=p["id"],
        name=p["name"],
        theme=p["theme"],
        bg=p["bg"],
        glass_bg=p["glass_bg"],
        glass_border=p["glass_border"],
        text=p["text"],
        accent=p["accent"],
        font_head=p["font_head"],
        font_body=p["font_body"],
        font_url=p["font_url"],
        tagline=p["tagline"],
        ux_pattern=p["ux_pattern"],
        tool_title=p["tool_title"],
        tool_desc=p["tool_desc"],
        badge=p["badge"],
        three_code=p["three_code"]
    )
    path = f"/data/project_qnt_netlify/proto{p['id']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated Liquid Glass {path}")
