# DESIGN.md — 学习工作台 30 秒宣传片

## Style Prompt

Dark-tech product promo for a student study workbench. The palette is inherited
directly from the shipped product UI (workbench/index.html): deep navy canvas,
indigo-to-cyan brand accents used as localized radial glows, glass-like cards
that recreate the real product. Bold rounded Chinese display type against a
serif body and a monospace data voice. Medium energy: clean push-slide
transitions, confident calm pacing, one vertical-push accent at the topic
change, blur crossfade into the outro.

## Colors

| Role | Hex |
| --- | --- |
| background (deep navy) | #0B1020 |
| foreground (cool off-white) | #E8ECF8 |
| dim text | #9AA3BD |
| brand indigo | #818CF8 |
| brand cyan | #22D3EE |
| success green | #34D399 |

The indigo/cyan-on-dark combination is the actual product brand, not a default
aesthetic choice; keep it consistent with workbench/index.html.

## Typography

- Display: "ZCOOL QingKe HuangYou" — Chinese display face, headlines only.
- Body: "Noto Serif SC" — serif body voice, weights 300/500/700.
- Data: "IBM Plex Mono" — kickers, timers, URLs, tech credits; tabular-nums.

## What NOT to Do

- No full-screen linear gradients on the dark canvas (H.264 banding); radial
  glows and solid navy only.
- No gradient-clipped text; headlines are solid off-white.
- No pure #000 or #fff; neutrals stay tinted toward indigo.
- No exit animations before transitions (final scene fade-out only).
- No emoji glyphs; icons are inline SVG or CSS shapes.
