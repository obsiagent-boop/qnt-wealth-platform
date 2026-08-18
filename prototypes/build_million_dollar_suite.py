import os

million_prototypes = [
    {
        "id": 1,
        "name": "The Sovereign Liquid Vault (Linear x Stripe Luxury)",
        "theme": "Pastel Cream & Platinum Obsidian",
        "bg": "#FAF8F5",
        "card_bg": "#FFFFFF",
        "text": "#0B0F1D",
        "border": "#E2E8F0",
        "accent": "#06B6D4",
        "font_head": "'Syne', sans-serif",
        "font_body": "'Plus Jakarta Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Syne:wght@700;800;900&display=swap",
        "tagline": "Liquid Mercury Quantum Dollar with Gyroscopic Inertia Shaders",
        "ux_pattern": "Bento Grid v3 + Real-Time 200-Module Asset Terminal with Instant Search",
        "tool_title": "Deterministic Geometric Compounding Engine",
        "tool_desc": "Simulating $A=P(1+r)^t$ geometric expansion with statutory triple-E tax immunity sweeps.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 01",
        "three_code": """
          const geo = new THREE.TorusGeometry(4.5, 1.2, 32, 120);
          const mat = new THREE.MeshPhysicalMaterial({
            color: 0xF59E0B, metalness: 0.95, roughness: 0.1,
            clearcoat: 1.0, clearcoatRoughness: 0.1,
            reflectivity: 1.0
          });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          const h1 = new THREE.Mesh(new THREE.TorusGeometry(7.2, 0.08, 16, 100), new THREE.MeshBasicMaterial({ color: 0x06B6D4, wireframe: true }));
          const h2 = new THREE.Mesh(new THREE.TorusGeometry(8.5, 0.06, 16, 100), new THREE.MeshBasicMaterial({ color: 0xF59E0B, wireframe: true }));
          h1.rotation.x = Math.PI * 0.4; h2.rotation.y = Math.PI * 0.35;
          scene.add(h1); scene.add(h2);
          animateHook = (t) => {
            mesh.rotation.x += 0.01;
            mesh.rotation.y += 0.015;
            h1.rotation.z += 0.012;
            h2.rotation.x -= 0.01;
          };
        """
    },
    {
        "id": 2,
        "name": "Prismatic Crystal Matrix (Vercel Precision x 21st.dev)",
        "theme": "Pastel Lavender & Electric Indigo",
        "bg": "#F5F3FF",
        "card_bg": "#FFFFFF",
        "text": "#1E1B4B",
        "border": "#DDD6FE",
        "accent": "#8B5CF6",
        "font_head": "'Clash Display', sans-serif",
        "font_body": "'Satoshi', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=clash-display@700,600&f[]=satoshi@500,700&display=swap",
        "tagline": "Liquid Glass Icosahedron with Chromatic Dispersion & Embedded Gold Core",
        "ux_pattern": "Dynamic Spotlight Cards + 10,000-Path Monte Carlo Probabilistic Fan Chart",
        "tool_title": "Monte Carlo Tail-Risk Decomposer",
        "tool_desc": "Probabilistic 99% VaR stress testing isolating sovereign fixed alpha from equity drawdowns.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 02",
        "three_code": """
          const geo = new THREE.IcosahedronGeometry(4.6, 0);
          const mat = new THREE.MeshPhysicalMaterial({
            color: 0xC4B5FD, metalness: 0.1, roughness: 0.05,
            transmission: 0.95, thickness: 3.5, transparent: true, opacity: 0.9
          });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          const core = new THREE.Mesh(new THREE.OctahedronGeometry(2.2, 0), new THREE.MeshStandardMaterial({ color: 0x8B5CF6, metalness: 0.9, roughness: 0.1 }));
          scene.add(core);
          animateHook = (t) => {
            mesh.rotation.x += 0.008;
            mesh.rotation.y += 0.014;
            core.rotation.y -= 0.02;
          };
        """
    },
    {
        "id": 3,
        "name": "Cybernetic Orthogonal Flow (Raycast x Aceternity)",
        "theme": "Pastel Mint & Cyber Emerald",
        "bg": "#F0FDF4",
        "card_bg": "#FFFFFF",
        "text": "#064E3B",
        "border": "#A7F3D0",
        "accent": "#10B981",
        "font_head": "'Cabinet Grotesk', sans-serif",
        "font_body": "'Inter', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,900&display=swap",
        "tagline": "Topological (2,5) Torus Knot in Continuous Hydrodynamic Fluid Flow",
        "ux_pattern": "Interactive Cross-Asset Correlation Heatmap with Zero-Beta Alpha Extraction",
        "tool_title": "Factor Orthogonalization Matrix",
        "tool_desc": "Proving 0.00 correlation between sovereign bucket moats and domestic equity beta.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 03",
        "three_code": """
          const geo = new THREE.TorusKnotGeometry(3.6, 1.1, 120, 24, 2, 5);
          const mat = new THREE.MeshStandardMaterial({ color: 0x6EE7B7, metalness: 0.85, roughness: 0.2 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          const wire = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color: 0x059669, wireframe: true, transparent: true, opacity: 0.4 }));
          wire.scale.set(1.06, 1.06, 1.06);
          scene.add(wire);
          animateHook = (t) => {
            mesh.rotation.x += 0.01;
            mesh.rotation.y += 0.015;
            wire.rotation.x -= 0.008;
            wire.rotation.y -= 0.012;
          };
        """
    },
    {
        "id": 4,
        "name": "Global Macro Barbell Stage (Apple Enterprise x Refero)",
        "theme": "Pastel Peach & Sunset Amber",
        "bg": "#FFF7ED",
        "card_bg": "#FFFFFF",
        "text": "#7C2D12",
        "border": "#FED7AA",
        "accent": "#F97316",
        "font_head": "'DM Serif Display', serif",
        "font_body": "'Plus Jakarta Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap",
        "tagline": "4 Interconnected Gravitational Planetary Currency Satellites ($ / ₹ / £ / €)",
        "ux_pattern": "Global Macro Yield Spread Visualizer + 10Y Sovereign G-Sec Arbitrage Telemetry",
        "tool_title": "Structural USD/INR Currency Alpha Arbitrage",
        "tool_desc": "Capturing 3.20% annual historical rupee depreciation as automated equity tailwinds.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 04",
        "three_code": """
          const group = new THREE.Group();
          const core = new THREE.Mesh(new THREE.SphereGeometry(2.4, 32, 32), new THREE.MeshStandardMaterial({ color: 0xFB923C, metalness: 0.9, roughness: 0.15 }));
          group.add(core);
          const colors = [0xF97316, 0x10B981, 0x06B6D4, 0x8B5CF6];
          const sats = [];
          for (let i = 0; i < 4; i++) {
            const s = new THREE.Mesh(new THREE.SphereGeometry(1.2, 24, 24), new THREE.MeshStandardMaterial({ color: colors[i], metalness: 0.85, roughness: 0.2 }));
            group.add(s);
            sats.push({ mesh: s, angle: (i / 4) * Math.PI * 2, dist: 6.5 });
          }
          scene.add(group);
          animateHook = (t) => {
            core.rotation.y += 0.015;
            sats.forEach(s => {
              s.angle += 0.015;
              s.mesh.position.x = Math.cos(s.angle) * s.dist;
              s.mesh.position.y = Math.sin(s.angle) * (s.dist * 0.4);
              s.mesh.position.z = Math.sin(s.angle) * (s.dist * 0.8);
            });
          };
        """
    },
    {
        "id": 5,
        "name": "Geometric Capital Helix (Framer Motion x Supabase UI)",
        "theme": "Pastel Coral & Crimson Quartz",
        "bg": "#FFF1F2",
        "card_bg": "#FFFFFF",
        "text": "#881337",
        "border": "#FECDD3",
        "accent": "#E11D48",
        "font_head": "'Playfair Display', serif",
        "font_body": "'Outfit', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&family=Playfair+Display:wght@700;900&display=swap",
        "tagline": "3D Double-Helix Geometric Growth Ladder Compounding Upward in Real Time",
        "ux_pattern": "15-Year Life Cycle Milestone Roadmap (Bedrock ➔ Acceleration ➔ Perpetual Sweep)",
        "tool_title": "15-Year Capital Velocity Ladder",
        "tool_desc": "Exact milestones transitioning active labor income to ₹5,00,000/mo perpetual passive sweep.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 05",
        "three_code": """
          const group = new THREE.Group();
          const m1 = new THREE.MeshStandardMaterial({ color: 0xFB7185, metalness: 0.9, roughness: 0.2 });
          const m2 = new THREE.MeshStandardMaterial({ color: 0xF43F5E, metalness: 0.85, roughness: 0.2 });
          for (let i = 0; i < 28; i++) {
            const t = (i / 28) * Math.PI * 4;
            const y = (i - 14) * 0.65;
            const s1 = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 16), m1);
            s1.position.set(Math.cos(t) * 3.8, y, Math.sin(t) * 3.8);
            group.add(s1);
            const s2 = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 16), m2);
            s2.position.set(Math.cos(t + Math.PI) * 3.8, y, Math.sin(t + Math.PI) * 3.8);
            group.add(s2);
          }
          scene.add(group);
          animateHook = (t) => {
            group.rotation.y += 0.015;
          };
        """
    },
    {
        "id": 6,
        "name": "Harmonic Liquid Nebula (Linear Luxury x Resend)",
        "theme": "Pastel Sky & Sapphire Ice",
        "bg": "#F0F9FF",
        "card_bg": "#FFFFFF",
        "text": "#0C4A6E",
        "border": "#BAE6FD",
        "accent": "#0284C7",
        "font_head": "'Fraunces', serif",
        "font_body": "'Manrope', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Manrope:wght@500;700&display=swap",
        "tagline": "Liquid Mercury Droplet with Undulating High-Specular Vertex Ripples",
        "ux_pattern": "Sovereign Annuity Cashflow Cascade with Automated Quarterly ECS Sweep Simulation",
        "tool_title": "Quarterly Liquidity Cascade Engine",
        "tool_desc": "Continuous yield sweeps across Grade-A REITs, SCSS & RBI 10Y Benchmark Gilts.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 06",
        "three_code": """
          const geo = new THREE.IcosahedronGeometry(4.2, 32);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0x7DD3FC, metalness: 0.9, roughness: 0.1, transmission: 0.7, thickness: 2.5 });
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
        "name": "Endless Mobius Continuum (Superhuman x Notion)",
        "theme": "Pastel Butter & Imperial Amber",
        "bg": "#FEFCE8",
        "card_bg": "#FFFFFF",
        "text": "#713F12",
        "border": "#FEF08A",
        "accent": "#CA8A04",
        "font_head": "'Bebas Neue', sans-serif",
        "font_body": "'Work Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Work+Sans:wght@500;700&display=swap",
        "tagline": "Endless 3D Mobius Ribbon Twisting in Liquid Gold Pastel Space",
        "ux_pattern": "Fama-French 5-Factor Alpha Decomposer (SMB, HML, RMW, CMA, WML)",
        "tool_title": "Multi-Factor Factor Alpha Decomposer",
        "tool_desc": "Deconstructing 24.0% CAGR systematic domestic outperformance into raw factor loadings.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 07",
        "three_code": """
          const geo = new THREE.TorusGeometry(4.8, 1.2, 30, 200);
          const mat = new THREE.MeshStandardMaterial({ color: 0xFDE047, metalness: 0.75, roughness: 0.2 });
          mesh = new THREE.Mesh(geo, mat);
          mesh.rotation.x = Math.PI * 0.3;
          scene.add(mesh);
          animateHook = (t) => {
            mesh.rotation.x += 0.01;
            mesh.rotation.y += 0.014;
          };
        """
    },
    {
        "id": 8,
        "name": "Prismatic Quartz Pyramid (Stripe Press x Figma UI)",
        "theme": "Pastel Lilac & Velvet Amethyst",
        "bg": "#FAF5FF",
        "card_bg": "#FFFFFF",
        "text": "#581C87",
        "border": "#E9D5FF",
        "accent": "#9333EA",
        "font_head": "'General Sans', sans-serif",
        "font_body": "'Satoshi', sans-serif",
        "font_url": "https://api.fontshare.com/v2/css?f[]=general-sans@700,600&f[]=satoshi@500,700&display=swap",
        "tagline": "Multi-Faceted Glass Tetrahedron Refracting Light Rays with Dynamic Glare",
        "ux_pattern": "The 70:15:15 Institutional Asset Rebalancing Engine with Real-Time Drift Triggers",
        "tool_title": "Dynamic 70:15:15 Portfolio Rebalancer",
        "tool_desc": "Quarterly automated drift triggers enforcing disciplined asset-class allocations.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 08",
        "three_code": """
          const geo = new THREE.TetrahedronGeometry(4.8, 0);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xD8B4FE, metalness: 0.2, roughness: 0.1, transmission: 0.85, thickness: 3.0 });
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
        "id": 9,
        "name": "Sovereign Legal Bastion (Anthropic x Vercel Dark)",
        "theme": "Pastel Sage & Forest Emerald",
        "bg": "#F6FBF7",
        "card_bg": "#FFFFFF",
        "text": "#14532D",
        "border": "#BBF7D0",
        "accent": "#16A34A",
        "font_head": "'Space Grotesk', sans-serif",
        "font_body": "'Inter', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Inter:wght@500;700&family=Space+Grotesk:wght@700&display=swap",
        "tagline": "Triple-Axis Mechanical Quantum Gyroscope in Calming Pastel Sage",
        "ux_pattern": "Section 14 Court Attachment Legal Immunity Shield Validator (PPF & SSY)",
        "tool_title": "Statutory Court Immunity & Insolvency Shield",
        "tool_desc": "Verifying 100% legal protection against debt attachment, civil decrees, and insolvency.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 09",
        "three_code": """
          const group = new THREE.Group();
          const mat1 = new THREE.MeshStandardMaterial({ color: 0x86EFAC, metalness: 0.9, roughness: 0.15 });
          const r1 = new THREE.Mesh(new THREE.TorusGeometry(3.5, 0.2, 16, 80), mat1);
          const r2 = new THREE.Mesh(new THREE.TorusGeometry(5.0, 0.2, 16, 80), mat1);
          const r3 = new THREE.Mesh(new THREE.TorusGeometry(6.5, 0.2, 16, 80), mat1);
          r2.rotation.x = Math.PI * 0.4; r3.rotation.y = Math.PI * 0.35;
          group.add(r1); group.add(r2); group.add(r3);
          scene.add(group);
          animateHook = (t) => {
            r1.rotation.x += 0.02;
            r2.rotation.y += 0.015;
            r3.rotation.z += 0.01;
          };
        """
    },
    {
        "id": 10,
        "name": "The Master Universal Terminal (Sovereign Grand Opus)",
        "theme": "Pastel Opal & High-Contrast Cyber Black",
        "bg": "#FAF8F5",
        "card_bg": "#FFFFFF",
        "text": "#0F172A",
        "border": "#000000",
        "accent": "#06B6D4",
        "font_head": "'Syne', sans-serif",
        "font_body": "'Plus Jakarta Sans', sans-serif",
        "font_url": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800;900&family=Syne:wght@800;900&display=swap",
        "tagline": "Breathing 3D Geometric Opal with Multi-Light Specular Dispersion & Live Feeds",
        "ux_pattern": "Unified Institutional Operating System Integrating all 6 Desks & 200 Asset Modules",
        "tool_title": "200-Module Master Quantitative Codex Engine",
        "tool_desc": "The definitive sovereign financial architecture for universal generational freedom.",
        "badge": "MILLION-DOLLAR SUITE • ARCHITECTURE 10",
        "three_code": """
          const geo = new THREE.DodecahedronGeometry(4.4, 0);
          const mat = new THREE.MeshPhysicalMaterial({ color: 0xBAE6FD, metalness: 0.2, roughness: 0.1, transmission: 0.85, thickness: 2.5 });
          mesh = new THREE.Mesh(geo, mat);
          scene.add(mesh);
          const core = new THREE.Mesh(new THREE.IcosahedronGeometry(2.2, 0), new THREE.MeshStandardMaterial({ color: 0xF59E0B, metalness: 0.95, roughness: 0.1 }));
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
    #canvas3d {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
    }}
    .million-card {{
      background: {card_bg} !important;
      border: 2px solid {border};
      border-radius: 28px;
      box-shadow: 6px 6px 0px {border};
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .million-card:hover {{
      transform: translate(-3px, -3px);
      box-shadow: 12px 12px 0px {accent};
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
        <a href="index.html" class="text-xs font-mono font-black px-4 py-2.5 rounded-xl bg-white border-2 border-slate-900 shadow-[3px_3px_0px_#000] hover:bg-black hover:text-white transition">
          &larr; Million-Dollar Prototype Lab
        </a>
        <div class="text-4xl font-black font-title tracking-tighter">qnt.</div>
      </div>
      <div class="px-4 py-2.5 rounded-xl bg-white border-2 border-slate-900 text-xs font-mono font-black shadow-[3px_3px_0px_#000]">
        {badge}
      </div>
    </header>

    <!-- HERO -->
    <div class="text-center max-w-4xl mx-auto mb-16">
      <div class="inline-block bg-white border-2 border-slate-900 text-xs font-mono font-black px-4 py-1.5 rounded-full mb-4 shadow-[3px_3px_0px_#000]">
        {tagline}
      </div>
      <h1 class="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight mb-4 leading-[1.08]">
        {name}
      </h1>
      <p class="text-sm md:text-base font-medium max-w-2xl mx-auto leading-relaxed opacity-80 mb-8">
        Architecture Pattern: <strong class="underline">{ux_pattern}</strong>. Engineered with sovereign institutional quantitative precision.
      </p>
      <div class="flex justify-center gap-4">
        <a href="#tool" class="bg-black text-white font-mono font-black text-xs px-6 py-3.5 rounded-xl border-2 border-black shadow-[4px_4px_0px_{accent}] hover:bg-white hover:text-black transition">
          Explore Analytical Engine &rarr;
        </a>
      </div>
    </div>

    <!-- BESPOKE ANALYTICAL TOOL -->
    <div id="tool" class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
      <div class="million-card p-8 lg:col-span-2">
        <div class="flex justify-between items-start mb-4">
          <div>
            <span class="text-xs font-mono font-black uppercase text-slate-500">BESPOKE ANALYTICAL ENGINE</span>
            <h3 class="text-2xl sm:text-3xl font-black mt-1">{tool_title}</h3>
          </div>
          <span class="text-xs font-mono font-black bg-white border border-slate-900 px-3 py-1 rounded-lg">VERIFIED TELEMETRY</span>
        </div>
        <p class="text-xs sm:text-sm leading-relaxed mb-8 font-medium opacity-80">{tool_desc}</p>
        
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 font-mono text-xs pt-6 border-t border-slate-900/10">
          <div class="p-5 rounded-2xl bg-white border-2 border-slate-900/10">
            <div class="text-[10px] text-slate-500 font-bold uppercase">STATUTORY TAX MOAT</div>
            <div class="text-xl font-black mt-1">100% Tax-Free</div>
            <div class="text-[10px] text-emerald-600 font-bold mt-1">Section 10(11A) / 47(viic)</div>
          </div>
          <div class="p-5 rounded-2xl bg-white border-2 border-slate-900/10">
            <div class="text-[10px] text-slate-500 font-bold uppercase">ROLLING ALPHA CAGR</div>
            <div class="text-xl font-black mt-1">15.4% – 28.4%</div>
            <div class="text-[10px] text-cyan-600 font-bold mt-1">Systematic Multi-Asset</div>
          </div>
          <div class="p-5 rounded-2xl bg-white border-2 border-slate-900/10">
            <div class="text-[10px] text-slate-500 font-bold uppercase">LEGAL SECURITY</div>
            <div class="text-xl font-black mt-1">Court Immunity</div>
            <div class="text-[10px] text-purple-600 font-bold mt-1">Section 14 PPF Act Shield</div>
          </div>
        </div>
      </div>

      <div class="million-card p-8 flex flex-col justify-between">
        <div>
          <span class="text-xs font-mono font-black uppercase text-slate-500">INSTITUTIONAL DOSSIER</span>
          <h3 class="text-2xl font-black mt-1 mb-3">282-Page Master Monograph</h3>
          <p class="text-xs leading-relaxed opacity-80 mb-6 font-medium">
            The complete institutional mathematical compendium spanning all 200 sovereign asset modules and 6 factor desks.
          </p>
        </div>
        <a href="reports/qnt_Universal_Financial_Freedom_Institutional_Compendium.pdf" download class="w-full text-center bg-black text-white font-mono font-black text-xs py-4 rounded-xl border-2 border-black shadow-[4px_4px_0px_#000] hover:bg-white hover:text-black transition block">
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
      camera.position.z = 22;

      renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true }});
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      const amb = new THREE.AmbientLight(0xffffff, 1.4);
      scene.add(amb);
      const dir = new THREE.DirectionalLight(0xffffff, 2.2);
      dir.position.set(12, 20, 15);
      scene.add(dir);
      const pt = new THREE.PointLight(0xffffff, 2.5, 40);
      pt.position.set(-10, -5, 10);
      scene.add(pt);

      {three_code}

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

# Clean old prototypes
for f in os.listdir("/data/project_qnt_netlify"):
    if f.startswith("proto") and f.endswith(".html"):
        os.remove(os.path.join("/data/project_qnt_netlify", f))

for p in million_prototypes:
    content = template.format(
        id=p["id"],
        name=p["name"],
        theme=p["theme"],
        bg=p["bg"],
        card_bg=p["card_bg"],
        text=p["text"],
        border=p["border"],
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
    print(f"Generated {path}")
