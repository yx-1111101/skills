---
name: figma-style-migration
description: Redesign functional pages on Figma canvas by transferring visual style from a reference. Supports clone-based, rebuild, and multi-style exploration workflows. Activate when the user provides a Figma reference + functional source and asks to redesign, match a style, migrate visual language, or 按照这个风格重新设计.
---

# Figma Style Migration

Transfer a visual language from a Figma reference to functional pages — directly on the Figma canvas.

## Prerequisites

Before ANY `use_figma` call, load these upstream skills (they cover API rules, error recovery, and screen-building workflow):

1. [figma-use](../../.cursor/plugins/cache/cursor-public/figma/d8bcb41b17ae473b3a830129bcd451ee1911e512/skills/figma-use/SKILL.md)
2. [figma-generate-design](../../.cursor/plugins/cache/cursor-public/figma/d8bcb41b17ae473b3a830129bcd451ee1911e512/skills/figma-generate-design/SKILL.md) — if building screens from scratch

Always pass `skillNames: "figma-style-migration"` in `use_figma` calls.

## Decision Tree

```
User provides reference + target
  │
  ├─ Reference and target share structure? ──► Strategy A: Clone & Customize
  │    (same domain, similar screens)          (default — highest fidelity)
  │
  ├─ Different domains, can't clone frames? ─► Strategy B: Extract & Rebuild
  │    (reference = social, target = finance)   (clone components, rebuild layout)
  │
  └─ User unsure about direction? ───────────► Strategy C: Multi-Style Exploration
       ("出几个方案" / "你觉得哪种好")           (2-3 variants side-by-side)
```

After choosing a strategy, load [strategies.md](strategies.md) for the detailed workflow.
If the user references a specific product style (e.g. "ChatGPT 风格", "iOS 风", "Linear 那种"), load [style-catalog.md](style-catalog.md) for that style's design language.
Before writing `use_figma` code, review [pitfalls.md](pitfalls.md) for non-obvious traps not covered by `figma-use`.

## Workflow (all strategies)

### 1. Understand

- Enumerate reference file: pages, frames, IDs, sizes (`get_metadata` / `use_figma`)
- Screenshot key frames (`get_screenshot`)
- Analyze target functional requirements (code, descriptions, PRD)
- Build a **frame mapping table** and a **feature delta list** (target features absent in reference)
- Present mapping to user for confirmation before proceeding

### 2. Execute

Load [strategies.md](strategies.md) and follow the chosen strategy.

### 3. Verify

After every frame: `get_screenshot` → compare → fix with targeted `use_figma` calls.
Never move to the next frame until the current one passes visual review.

## Principles

1. **Clone over rebuild.** Cloned elements preserve production-quality polish that raw API construction cannot reproduce.
2. **Never generate icons, never use emoji as icons.** Always clone from the file's icon library page (`icon` page, `General` frame). Never use `createNodeFromSvg()`, hand-built vectors, or emoji characters — all produce inconsistent, low-quality results. If the icon doesn't exist in the library, ask the user to add it first. See [pitfalls.md](pitfalls.md) §5–6 for the full pattern and exception rules.
3. **Pair list + detail.** Any list/market page needs its matching detail page in the same style; shipping one without the other creates review gaps.
4. **One hero > uniform grid.** A single prominent card with gradient/visual treatment draws focus better than equal-sized tiles.
5. **Icons are optional.** If title + subtitle convey enough hierarchy, removing icons often yields a cleaner result.
6. **Verify incrementally.** Screenshot after each frame or major section — catch overflow and font issues early.
