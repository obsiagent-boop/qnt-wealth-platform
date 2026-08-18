---
name: "qnt-institutional-saas-design-system"
version: "4.2.0"
format: "Google DESIGN.md Spec / DTCG Compliant"
author: "qnt. Quantitative Systems x Fincept Terminal"
last_updated: "2026-08-18"
framework_integrations:
  - "ui.aceternity.com (Bento Grids, Background Glow Meshes, Glassmorphism)"
  - "reactbits.dev (Interactive Animated Stat Cards, Number Streamers)"
  - "componentry.dev (Accessible UI Toggles, Tab Matrices, Modal Dialogs)"
  - "toggle.supply (Micro-Interaction Switches, Tactile Radii, Active States)"
  - "motion.dev (Smooth Elevation Physics, 200ms Cubic Bezier Transitions)"
  - "styles.refero.design (Midnight Precision, Abyssal & Ivory Terminal Styling)"
  - "getdesign.md / designmd.cc (Live Measured Design Tokens & DOM Breakpoints)"

tokens:
  color:
    # 🌌 Cyber Void Dark Mode Palette (Terminal & SaaS Engine)
    void:
      950: "#030509"  # Absolute Deep Ground
      900: "#060811"  # Primary Canvas Background
      850: "#0A0E1A"  # Elevated Container Canvas
      800: "#0F1527"  # Glass Surface / Card Canvas
      700: "#1A233D"  # Structural Border Active

    # ⚡ Radiant Cyan Accents (Focus, Badges & Primary Actions)
    cyan:
      glow: "#06B6D4"    # Primary Action Button & Highlight Glow
      bright: "#22D3EE"  # Active Text Accent & Hover State
      muted: "#0891B2"   # Inactive Ring & Secondary Indicator

    # 🍦 Sovereign Luxury Cream (Document & Monograph Modals)
    cream:
      50: "#FAF8F5"      # Master Monograph Ivory Canvas
      100: "#F4EFEA"     # Secondary Surface Card
      200: "#E6DED5"     # Subtle Header Band

    # 🎨 Fincept 6-Desk Factor Colors
    fincept:
      desk1_equities: "#EA580C"     # Orange / Alpha Factor
      desk2_theta: "#2563EB"        # Blue / Options Cashflow
      desk3_sovereign: "#059669"    # Emerald / Triple-E Sovereign
      desk4_reits: "#9333EA"        # Purple / Commercial Real Assets
      desk5_sgb_gold: "#D97706"     # Gold / Crisis Moat
      desk6_global_usd: "#06B6D4"   # Cyan / US Platform Monopolies

  typography:
    font_family:
      sans: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
      mono: "'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace"
    weights:
      light: 300
      regular: 400
      medium: 500
      semibold: 600
      bold: 700
      black: 900
    scale:
      display_hero: "clamp(3rem, 7vw, 5.5rem) / 1.08 / 900 / tracking-tight"
      h1: "2.5rem (40px) / 1.15 / 800"
      h2: "1.75rem (28px) / 1.25 / 800"
      h3: "1.25rem (20px) / 1.35 / 700"
      body: "0.9375rem (15px) / 1.6 / 400"
      mono_telemetry: "0.8125rem (13px) / 1.45 / 600"
      badge_pill: "0.6875rem (11px) / 1.2 / 800 / uppercase / tracking-wider"

  spacing_and_grid:
    base: "4px"
    scale: [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]
    container_max_width: "1280px (max-w-7xl)"
    grid_gap: "24px (gap-6)"

  shapes_and_radii:
    none: "0px"
    sm: "4px"
    md: "8px"
    lg: "12px"
    xl: "16px"
    "2xl": "24px"
    full_pill: "9999px"

  elevation_and_shadows:
    sm: "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
    glass: "0 8px 32px 0 rgba(0, 0, 0, 0.37)"
    glow_cyan: "0 0 25px rgba(6, 182, 212, 0.35)"
    glow_cyan_hover: "0 0 40px rgba(6, 182, 212, 0.60)"

  breakpoints:
    sm: "640px"
    md: "768px"
    lg: "1024px"
    xl: "1280px"
    "2xl": "1536px"
---

# 🏛️ qnt. Unified Design System Specification (DESIGN.md)

## 1. Overview & Architectural Vision
The **qnt.** design system bridges **deep institutional quantitative finance** with **hyper-modern AI-native user interfaces**. It implements Google's official `DESIGN.md` specification and incorporates measured design tokens from **getdesign.md, designmd.cc, styles.refero.design, and aura.build**.

## 2. Core UI Component Specifications

### A. The Bento Grid Container (Aceternity UI Pattern)
- **Background:** `rgba(15, 21, 39, 0.65)` with `backdrop-filter: blur(16px)`
- **Border:** `1px solid rgba(255, 255, 255, 0.08)`
- **Hover Physics:** Transitions to `border-cyan-500/50` with `-translate-y-1` elevation shift (200ms ease-in-out).

### B. Interactive Compounding Calculator (ReactBits / Componentry Pattern)
- **Principal Selector Pills:** Radio-style buttons for `₹1,000`, `₹10,000`, and `₹1,00,000`.
- **Live Output Streamers:** Instant dynamic calculation of 5Y, 10Y, and 15Y geometric compounding milestones ($A = P(1+r)^t$).
- **Active State:** High-contrast `bg-[#06B6D4]` text-black with cyan shadow glow.

### C. Fincept 6-Desk Factor Indicators (Refero Styles Pattern)
- **Desk I (Equities):** Accent `#EA580C` (Orange)
- **Desk II (F&O Theta Cashflow):** Accent `#2563EB` (Blue)
- **Desk III (Sovereign Fixed):** Accent `#059669` (Emerald)
- **Desk IV (Commercial REITs):** Accent `#9333EA` (Purple)
- **Desk V (Precious Metals/SGB):** Accent `#D97706` (Amber)
- **Desk VI (Global USD):** Accent `#06B6D4` (Cyan)

## 3. UI Micro-Interactions (Toggle Supply & Motion Dev)
1. **Interactive Switches:** Active state changes trigger instant sub-50ms DOM updates.
2. **Hover Light-Leak:** Subtle radial gradient glow follows cursor on cards.
3. **Pill Badges:** Monospace tracking-widest badges (`INSTITUTIONAL AAA`, `LIVE_SYNCED`, `TRIPLE-E`).

## 4. Production Usage Rules
- **Do:** Use pure Inter for headings and JetBrains Mono for financial tickers and math formulas.
- **Do:** Maintain crisp border separation between glass cards and the dark background.
- **Don't:** Use generic AI purple-blue gradients without high-contrast structure.
- **Don't:** Leave non-functional buttons or dead-click placeholder links.
